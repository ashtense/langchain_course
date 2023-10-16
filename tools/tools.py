from typing import Any

from langchain.serpapi import SerpAPIWrapper


class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        resp = SerpAPIWrapper._process_response(res)
        if "organic_results" in res.keys():
            first_organic_result = res["organic_results"][0]
            if "link" in first_organic_result.keys():
                resp = first_organic_result["link"]
        return resp


def get_profile_url(text: str) -> str:
    """Searches for LinkedIn profile page and returns its url"""
    return CustomSerpAPIWrapper().run(f"{text}")
