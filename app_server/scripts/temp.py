from social_core.backends.github import GithubOAuth2
from social_django.utils import load_backend, load_strategy
token = "frfer.ferg.g"

def main():
    # strategy = load_strategy(request=request)
    # backend = load_backend()
    backend = GithubOAuth2()
    backend._user_data(token)
    user = backend.do_auth(access_token=token)



if __name__ == '__main__':
    main()