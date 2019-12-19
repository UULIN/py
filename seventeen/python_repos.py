import requests
import pygal
from pygal.style import LightColorizedStyle as lcs, LightenStyle as ls

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])


# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
names, stars = [], []
# print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = ls('#333366', base_style=lcs)
chart = pygal.Bar(style=my_style, x_lable_rotation=45, show_legend=False)
chart.title = "Most-Starred Pyhon Projects on Github"
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('./data/python_repos.svg')

"""  print('name:', repo_dict['name'])
    print('Onwer:', repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])"""