"""
System Monitor Tool
===================

A tool for monitoring system resources and analyzing performance metrics.
"""
import psutil
import os
from typing import Type, Any
from pydantic import BaseModel, Field
from crewai_tools import BaseTool

class SystemMonitorToolSchema(BaseModel):
    """Input for SystemMonitorTool."""
    metric: str = Field(..., description="Metric to monitor (cpu, memory, disk, network, processes)")

class SystemMonitorTool(BaseTool):
    name: str = "System Monitor Tool"
    description: str = "Monitors system resources and analyzes performance metrics."
    args_schema: Type[BaseModel] = SystemMonitorToolSchema

    def _run(self, **kwargs: Any) -> Any:
        metric = kwargs.get('metric', 'cpu')
        
        try:
            if metric == 'cpu':
                cpu_percent = psutil.cpu_percent(interval=1)
                cpu_count = psutil.cpu_count()
                cpu_stats = psutil.cpu_stats()
                return {
                    "cpu_percent": cpu_percent,
                    "cpu_count": cpu_count,
                    "cpu_stats": {
                        "ctx_switches": cpu_stats.ctx_switches,
                        "interrupts": cpu_stats.interrupts,
                        "soft_interrupts": cpu_stats.soft_interrupts,
                        "syscalls": cpu_stats.syscalls
                    }
                }
            elif metric == 'memory':
                memory = psutil.virtual_memory()
                swap = psutil.swap_memory()
                return {
                    "virtual_memory": {
                        "total": memory.total,
                        "available": memory.available,
                        "percent": memory.percent,
                        "used": memory.used,
                        "free": memory.free
                    },
                    "swap_memory": {
                        "total": swap.total,
                        "used": swap.used,
                        "free": swap.free,
                        "percent": swap.percent
                    }
                }
            elif metric == 'disk':
                disk_usage = psutil.disk_usage('/')
                disk_io = psutil.disk_io_counters()
                return {
                    "disk_usage": {
                        "total": disk_usage.total,
                        "used": disk_usage.used,
                        "free": disk_usage.free,
                        "percent": disk_usage.percent
                    },
                    "disk_io": {
                        "read_count": disk_io.read_count,
                        "write_count": disk_io.write_count,
                        "read_bytes": disk_io.read_bytes,
                        "write_bytes": disk_io.write_bytes
                    }
                }
            elif metric == 'network':
                net_io = psutil.net_io_counters()
                net_connections = len(psutil.net_connections())
                return {
                    "network_io": {
                        "bytes_sent": net_io.bytes_sent,
                        "bytes_recv": net_io.bytes_recv,
                        "packets_sent": net_io.packets_sent,
                        "packets_recv": net_io.packets_recv
                    },
                    "connections": net_connections
                }
            elif metric == 'processes':
                processes = []
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                    try:
                        processes.append(proc.info)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
                # Sort by CPU usage and return top 10
                processes.sort(key=lambda x: x['cpu_percent'] if x['cpu_percent'] is not None else 0, reverse=True)
                return processes[:10]
            else:
                return f"Unknown metric: {metric}"
        except Exception as e:
            return f"Error monitoring system: {str(e)}"