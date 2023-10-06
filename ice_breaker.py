from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import mock_scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":

    linked_lookup_url = linkedin_lookup_agent(name = "ashwani solanki")
    print(linked_lookup_url)
    summary = """
        given the information {information} about a person, I want you to create:
        1. A short  summary about the person
        2. 2 interesting facts about the person
        3. Figure out the occupation of the person in one word and in the exact format like: Occupation = []
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary
    )
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )
    # We fetch profile information of this person form linkedin web scraper and feed it into prompt template.
    profile_json = mock_scrape_linkedin_profile("Ashwani Solanki")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)


    print(chain.run(information=profile_json))
