from django.views.generic import TemplateView
from charingcross.utils import github_from_request

class RepoView(TemplateView):
    template_name = "repo.html"

    def get_context_data(self, **kwargs):
        context = super(RepoView, self).get_context_data(**kwargs)
        gh = github_from_request(self.request)
        repo = gh.get_repo(kwargs['full_name'])
        milestones = repo.get_milestones()
        issues = repo.get_issues(
            labels=[repo.get_label('kind/roadmap')],
            state='all'
        )

        for issue in issues:
            if issue.state == "closed":
                issue.extended_state = "closed"
            elif filter(lambda l: l.name == "status/in-progress", issue.labels):
                issue.extended_state = "in-progress"
            else:
                issue.extended_state = "open"

        for milestone in milestones:
            milestone.issues = filter(lambda i: i.milestone == milestone, issues)

        return {
            'repo': repo,
            'milestones': milestones,
        }
