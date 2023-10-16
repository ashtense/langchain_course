from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import mock_scrape_linkedin_profile, scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser

if __name__ == "__main__":
    # Initializing the agent
    linked_lookup_url = linkedin_lookup_agent(
        name="Ashwani Solanki", company_name="Amdocs"
    )
    print(linked_lookup_url)
    summary = """
        given the information {information} about a person, I want you to create:
        1. A short  summary about the person
        2. 2 interesting facts about the person
        3. A topic that may interest them
        4. 2 creative ice breakers to open a conversation with them
            \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )

    """
        We fetch profile information of this person form LinkedIn web scraper and feed it into prompt template.
        profile_json = scrape_linkedin_profile(linked_lookup_url=linked_lookup_url)
        Commented the above line and using below mocked api response in order to save on the API usage cost.  
    """

    profile_json = mock_scrape_linkedin_profile(linkedin_profile_url="Dummy URL")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    result = chain.run(information=profile_json)
    result = summary_parser.parse(result)
    print(result)
