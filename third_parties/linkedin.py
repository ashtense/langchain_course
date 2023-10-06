import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    api_key = "qapNJ5ofcmD1TqHK9w7nBQ"
    headers = {"Authorization": "Bearer " + api_key}
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    params = {
        "linkedin_profile_url": linkedin_profile_url,
        "extra": "include",
        "github_profile_id": "include",
        "facebook_profile_id": "include",
        "twitter_profile_id": "include",
        "personal_contact_number": "include",
        "personal_email": "include",
        "inferred_salary": "include",
        "skills": "include",
        "use_cache": "if-present",
        "fallback_to_cache": "on-error",
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    print(response.json())


def mock_scrape_linkedin_profile(linkedin_profile_url: str):
    gist_response = requests.get(
        "https://gist.githubusercontent.com/ashtense/631cc2eb16b4056002847339cbda77be/raw/3184518cbe1ada715397ccd9bee6aa4b9c5a09cb/gistfile1.txt"
    )
    return clean_response(gist_response)


def clean_response(original_response):
    api_response = original_response.json()
    clean_response = {}
    for key, value in api_response.items():
        if value not in ([], "", " ", None):
            clean_response[key] = value
    return clean_response
