"""
Deployment Troubleshooter Crew
==============================

This crew is responsible for reviewing, configuring, and troubleshooting deployment issues.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class DeploymentTroubleshooterCrew():
    """Deployment Troubleshooter Crew"""

    @agent
    def deployment_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['deployment_engineer'],
            verbose=True
        )

    @agent
    def infrastructure_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['infrastructure_specialist'],
            verbose=True
        )

    @agent
    def security_auditor(self) -> Agent:
        return Agent(
            config=self.agents_config['security_auditor'],
            verbose=True
        )

    @task
    def deployment_configuration_task(self) -> Task:
        return Task(
            config=self.tasks_config['deployment_configuration_task'],
        )

    @task
    def infrastructure_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['infrastructure_review_task'],
        )

    @task
    def deployment_security_audit_task(self) -> Task:
        return Task(
            config=self.tasks_config['deployment_security_audit_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Deployment Troubleshooter Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )