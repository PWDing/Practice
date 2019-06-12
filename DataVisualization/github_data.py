import json
import pygal
import requests
from matplotlib import pyplot as plt
from pygal.style import LightenStyle as ls
from pygal.style import LightColorizedStyle as lcs


class DataVisualization:
    def __init__(self):
        self.x_values = None
        self.y_values = None

    def get_file_data(self, filename):
        with open(filename) as f:
            data = json.load(f)
        return data

    def get_web_data(self, url):
        reponse = requests.get(url)
        if reponse.status_code == 200:
            content = reponse.json()
            return content['items']

    def display_stars(self, data_sets):
        project_names, project_stars = [], []
        for data in data_sets:
            project_names.append(data_sets['name'])
            project_stars.append(data_sets['stargazers_count'])

        git_style = ls('#333366', base_style=lcs)
        chart = pygal.Bar(style=git_style, x_label_rotation=45, show_legend=False)
        chart.title = 'Most-Starred Python Projects on GitHub'
        chart.x_labels = project_names

        chart.add('', project_stars)
        chart.render_to_file('python_repos.svg')


if __name__ == '__main__':
    my_data_visual = DataVisualization()
    myurl = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    date_set = my_data_visual.get_web_data(myurl)
    my_data_visual.display_stars(date_set)
