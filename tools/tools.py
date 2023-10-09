from langchain.serpapi import SerpAPIWrapper

class CustomSerpAPIWrapper(SerpAPIWrapper):

    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

def get_profile_url(text: str) -> str:
    """Searches for LinkedIn profile page and returns its url"""
    return SerpAPIWrapper().run(f"{text}")
