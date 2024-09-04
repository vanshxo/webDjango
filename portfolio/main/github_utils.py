# github_utils.py
import requests

GITHUB_API_URL = "https://api.github.com"
ACCESS_TOKEN = "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"

def get_github_repositories(username):
    headers = {'Authorization': f'token {ACCESS_TOKEN}'}
    response = requests.get(f'{GITHUB_API_URL}/users/{username}/repos', headers=headers)
    return response.json() if response.status_code == 200 else None

def get_github_user(username):
    headers = {'Authorization': f'token {ACCESS_TOKEN}'}
    response = requests.get(f'{GITHUB_API_URL}/users/{username}', headers=headers)
    return response.json() if response.status_code == 200 else None