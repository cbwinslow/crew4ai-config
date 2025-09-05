"""
Full Project Implementation Crew
================================

This crew is responsible for leading the implementation of software projects from
planning to completion, including task breakdown, code generation, testing, and documentation.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class FullProjectImplementationCrew():
    """Full Project Implementation Crew"""

    @agent
    def implementation_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['implementation_lead'],
            verbose=True
        )

    @agent
    def task_breakdown_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['task_breakdown_specialist'],
            verbose=True
        )

    @agent
    def code_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['code_generator'],
            verbose=True
        )

    @agent
    def testing_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['testing_specialist'],
            verbose=True
        )

    @agent
    def documentation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['documentation_specialist'],
            verbose=True
        )

    @task
    def task_breakdown_task(self) -> Task:
        return Task(
            config=self.tasks_config['task_breakdown_task'],
        )

    @task
    def code_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_generation_task'],
        )

    @task
    def testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['testing_task'],
        )

    @task
    def documentation_task(self) -> Task:
        return Task(
            config=self.tasks_config['documentation_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Full Project Implementation Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )