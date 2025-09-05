"""
Project Analysis Crew
=====================

This crew is responsible for reviewing projects as a whole for architecture, design, and big picture issues.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ProjectAnalysisCrew():
    """Project Analysis Crew"""

    @agent
    def architect(self) -> Agent:
        return Agent(
            config=self.agents_config['architect'],
            verbose=True
        )

    @agent
    def design_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['design_reviewer'],
            verbose=True
        )

    @agent
    def scalability_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['scalability_expert'],
            verbose=True
        )

    @task
    def project_architecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_architecture_task'],
        )

    @task
    def design_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_review_task'],
        )

    @task
    def scalability_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['scalability_assessment_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Project Analysis Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )