"""
Code Generation Crew
====================

This crew is responsible for writing high-quality, well-documented code based on
specifications and requirements.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CodeGenerationCrew():
    """Code Generation Crew"""

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
        """Creates the Code Generation Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )