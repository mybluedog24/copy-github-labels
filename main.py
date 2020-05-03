from github import Github


def delete_all_old_labels_in_repo(g, repo):
    '''Delete all labels in repo.'''

    to_repo = g.get_user().get_repo(repo)
    to_labels = to_repo.get_labels()
    for label in to_labels:
        label.delete()

def copy_labels_from_repo_to_repo(g, from_repo, to_repo):
    '''Copy all labels from repo to repo. It label exists throws error.'''

    to_repo = g.get_user().get_repo(to_repo)
    from_repo = g.get_user().get_repo(from_repo)
    from_labels = from_repo.get_labels()
    for label in from_labels:
        if label.description:
            to_repo.create_label(label.name, label.color, label.description)
        else:
            to_repo.create_label(label.name, label.color)


if __name__ == "__main__":
    username = "username"
    password = "password"
    from_repo = "your repo name that you want to copy from"
    to_repo = "your repo name that you want to copy to"

    g = Github(username, password)

    ##### DO NOT RECOMMEND USE DELETE FUNCTION unless you are sure the repo is the one you want to delete.
    ##### If you input a wrong repo, all labels in that repo will be deleted. (My own experience..)
    # delete_all_old_labels_in_repo(g, to_repo)
    
    copy_labels_from_repo_to_repo(g, from_repo, to_repo)
