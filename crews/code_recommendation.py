"""
Code Recommendation Crew
========================

This crew is responsible for analyzing code and providing detailed recommendations
for improvements, optimizations, and best practices.
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CodeRecommendationCrew():
    """Code Recommendation Crew"""

    @agent
    def code_recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['code_recommender'],
            verbose=True
        )

    @task
    def code_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_recommendation_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Code Recommendation Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )