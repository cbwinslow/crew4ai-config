"""
Project Planning and Task Breakdown Crew
========================================

This crew is responsible for breaking down complex projects into manageable tasks
and creating implementation plans.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ProjectPlanningCrew():
    """Project Planning and Task Breakdown Crew"""

    @agent
    def task_breakdown_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['task_breakdown_specialist'],
            verbose=True
        )

    @agent
    def planning_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['planning_expert'],
            verbose=True
        )

    @task
    def project_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_planning_task'],
        )

    @task
    def task_breakdown_task(self) -> Task:
        return Task(
            config=self.tasks_config['task_breakdown_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Project Planning Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )