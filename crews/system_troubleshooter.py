"""
System Troubleshooter Crew
==========================

This crew is responsible for analyzing system logs, processes, CPU usage, I/O issues, network anomalies, etc.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class SystemTroubleshooterCrew():
    """System Troubleshooter Crew"""

    @agent
    def system_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['system_analyst'],
            verbose=True
        )

    @agent
    def performance_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['performance_engineer'],
            verbose=True
        )

    @agent
    def network_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['network_specialist'],
            verbose=True
        )

    @task
    def system_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['system_analysis_task'],
        )

    @task
    def performance_diagnostics_task(self) -> Task:
        return Task(
            config=self.tasks_config['performance_diagnostics_task'],
        )

    @task
    def network_diagnostics_task(self) -> Task:
        return Task(
            config=self.tasks_config['network_diagnostics_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the System Troubleshooter Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )