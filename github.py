import os
import httpx

def get_repo_info(owner: str, repo: str):
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = httpx.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception("GitHub repo not found")
