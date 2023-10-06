from langchain.serpapi import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for LinkedIn profile page and returns its url"""
    return SerpAPIWrapper().run(f"{text}")
