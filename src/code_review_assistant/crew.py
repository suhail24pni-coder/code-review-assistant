from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from code_review_assistant.tools.custom_tool import LineLengthChecker

@CrewBase
class CodeReviewAssistantCrew():
    """CodeReviewAssistant crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def bug_hunter(self) -> Agent:
        return Agent(
            config=self.agents_config['bug_hunter'],
            verbose=True
        )

    @agent
    def style_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['style_reviewer'],
            tools=[LineLengthChecker()], # Assign custom tool here
            verbose=True
        )

    @agent
    def refactor_suggester(self) -> Agent:
        return Agent(
            config=self.agents_config['refactor_suggester'],
            verbose=True
        )

    @task
    def bug_hunting_task(self) -> Task:
        return Task(config=self.tasks_config['bug_hunting_task'])

    @task
    def style_review_task(self) -> Task:
        return Task(config=self.tasks_config['style_review_task'])

    @task
    def refactor_suggestion_task(self) -> Task:
        return Task(
            config=self.tasks_config['refactor_suggestion_task'],
            output_file='code_review.md' 
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential, # Tasks run one after another
            verbose=True,
        )