from prettytable import PrettyTable
from github import Github

# User name
USERNAME = ""

# API_KEY
g = Github("")

# Table parameters
pt = PrettyTable()
pt.field_names = ["name", "size", "contributors", "branch name", "is Protected"]

user = g.get_user(USERNAME)
print("Is Working....")

for repo in user.get_repos():
    br = str((list(repo.get_branches())[0]))
    x = list(repo.get_branches())
    if len(x)>0:
        prt = (repo.get_branch("master").protected)
    pt.add_row([repo.name, repo.size, repo.get_contributors().totalCount,br[13:-2], prt])

print(pt)
