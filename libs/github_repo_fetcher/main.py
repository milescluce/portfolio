from contextlib import contextmanager
from github import Github, Auth
from functools import partial

AUTH = Auth.Token("access_token")

@contextmanager
def gh(user: bool = False) -> Github:
    g = Github(auth=AUTH)
    try:
        yield g if not user else g.get_user()
    finally:
        g.close()

ghu = partial(gh, user=True)

def print_repos():
    with ghu() as g:
        g.get_repos()

