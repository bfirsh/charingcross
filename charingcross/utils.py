import github

def github_from_request(request):
    provider = request.user.social_auth.get(provider='github-org')
    return github.Github(provider.extra_data['access_token'])
