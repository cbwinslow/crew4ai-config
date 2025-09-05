"""
Code Review Crew
================

This crew is responsible for reviewing code files for quality, best practices, and potential issues.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CodeReviewCrew():
    """Code Review Crew"""

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['code_reviewer'],
            verbose=True
        )

    @agent
    def security_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['security_analyst'],
            verbose=True
        )

    @agent
    def performance_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['performance_optimizer'],
            verbose=True
        )

    @task
    def code_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_review_task'],
        )

    @task
    def security_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['security_analysis_task'],
        )

    @task
    def performance_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['performance_optimization_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Code Review Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
        )