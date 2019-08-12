import os

from flask_dance.contrib.github import github, make_github_blueprint
from flask_api import status
from flask import Flask, redirect, url_for, render_template


"""..."""
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", ".env")
app.config["GITHUB_OAUTH_CLIENT_ID"] = os.environ.get(
    "GITHUB_OAUTH_CLIENT_ID", ".env")
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = os.environ.get(
    "GITHUB_OAUTH_CLIENT_SECRET", ".env")
app.register_blueprint(blueprint=make_github_blueprint(
    scope='public_repo'),
    url_prefix="/login")
username = os.environ.get("GITHUB_USERNAME", ".env")
repo_name = os.environ.get("REPOSITORY_NAME", ".env")


def get_link(username, repo):
    """..."""
    return f"https://github.com/{username}/{repo}"


@app.route('/')
def replication():
    """..."""
    if not github.authorized:
        return redirect(url_for("github.login"))

    user_resp = github.get("/user")

    if not user_resp.ok:
        return "WOW! Something went wrong :( , try to refresh page!!!"

    link_to_repo = get_link(user_resp.json()["login"], repo_name)
    forking = github.post(f'/repos/{username}/{repo_name}/forks')

    if not forking.ok:
        if forking.status_code == status.HTTP_404_NOT_FOUND:
            return f"You are trying to fork the repo which does not exist."

        return "WOW! Something went wrong :( , try to refresh page!!!"

    return render_template("base.html", link_to_repo=link_to_repo)


if __name__ == '__main__':
    app.run()

