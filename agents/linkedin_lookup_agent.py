from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from tools.tools import get_profile_url


def lookup(name: str, company_name: str) -> str:
    template = """
        Given the full name {name_of_person} I want you to get it me a link to their 
        Linkedin profile page. Filter should also be done on the company name {company_name}.
        Your answer should definitely contain only a URL
    """
    tools_for_agent = [
        Tool(
            name="Crawl google 4 linkedin profile page",
            func=get_profile_url,
            description="Useful for when you want to find someone's linked profile url directly",
        )
    ]
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        input_variables=["name_of_person", "company_name"], template=template
    )
    linked_profile_url = agent.run(
        prompt_template.format_prompt(name_of_person=name, company_name=company_name)
    )
    return linked_profile_url
