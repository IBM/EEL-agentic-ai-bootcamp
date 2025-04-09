from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, after_kickoff

from assistance_crew.tools import WebSearchTool, PortfolioFetcherTool



@CrewBase
class AssistanceAgents:
    """Assistants crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self, llm: LLM, **kwargs):
        self.llm = llm
        self.intermediate_steps = kwargs.pop("intermediate_steps", None)

    @after_kickoff  # Optional hook to be executed after the crew has finished
    def log_results(self, output):
        # Example of logging results, dynamically changing the output
        print(f"Results: {output}")
        return output
    
    @agent
    def investment_strategy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["investment_strategy_agent"], 
            tools=[PortfolioFetcherTool(), WebSearchTool()], 
            verbose=True, 
            llm=self.llm
        )

    @agent
    def asset_allocation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["asset_allocation_agent"], 
            tools=[PortfolioFetcherTool(), WebSearchTool()],
            verbose=True,
            llm=self.llm)

    @agent
    def impact_assessment_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["impact_assessment_agent"], 
            tools=[WebSearchTool()],
            verbose=True,
            llm=self.llm)

    @agent
    def near_term_recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["near_term_recommendation_agent"], tools=[WebSearchTool()],
            verbose=True,
            llm=self.llm)

    @agent
    def report_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer_agent"],
            verbose=True,
            llm=self.llm)

    @task
    def investment_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["investment_strategy_task"],
        )

    @task
    def asset_allocation_task(self) -> Task:
        return Task(
            config=self.tasks_config["asset_allocation_task"],
        )

    @task
    def impact_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config["impact_assessment_task"],
        )

    @task
    def near_term_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config["near_term_recommendation_task"],
        )

    @task
    def write_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_report_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AI Assistant crew"""

        def task_callback(step_output):
            self.intermediate_steps.append(step_output)

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            step_callback=task_callback,
        )


