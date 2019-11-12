import requests
import re
from bs4 import BeautifulSoup as bs
import json
from lxml import etree
import pandas as pd
from fake_useragent import UserAgent
import os
import sys
from urllib import parse
import datetime


class History:
    def __init__(self):
        self.urls = {
            "story": "https://www.xuexi.cn/a626e7afac9036a3c48a3db17cdf0d6b/5957f69bffab66811b99940516ec8784.html",
            "study": "https://www.xuexi.cn/e85d4f098b1153e29d96cec73c8d97c9/5957f69bffab66811b99940516ec8784.html",
            "knowledge": "https://www.xuexi.cn/35635435be41dacf475c07d0a94e3f6a/8c5129d583985f2380c340b69c8f4734.html"
        }
    
    def get_json(self, urls):
        '''
        get detailed json address
        '''
        data_list = []
        for title, url in urls.items():
            json_url_temp = url.rsplit("/")
            json_url = json_url_temp[0] + "//" + json_url_temp[2] + "/lgdata/" + json_url_temp[3] + "/" + json_url_temp[4].replace("html", "json")

            respond = requests.get(json_url)
            respond.encoding = "utf-8"
            for key, value in json.loads(respond.text, encoding="utf-8").items():
                if key == "pageData":
                    item = value["channel"]
                    channel_url = json_url_temp[0] + "//" + json_url_temp[2] + "/lgdata/" + item["channelId"] + ".json"
                    data_list.append(channel_url)
        return data_list

    def get_articles(self, json_data):
        articles = []
        today = str(datetime.date.today())
        for data in json_data:
            respond = requests.get(data)
            respond.encoding = "utf-8"
            values = list(json.loads(respond.text, encoding="utf-8"))
            for value in values:
                if today in value["publishTime"]:
                    articles.append({"category": value["channelNames"][0], "url": value["url"], "date": today})
        return articles

    def get_content(self, articles):
        '''
        get detail content
        '''
        article_list = []
        for article_data in articles:
            print("读取地址{0}的数据".format(article_data))
            article_category = article_data["category"]
            article_date = article_data["date"]
            url_temp = article_data["url"].rsplit("/")
            if "?id" in article_data["url"]:
                # get ID if you know parameter
                query = dict(parse.parse_qsl(parse.urlsplit(article_data["url"]).query))
                js_url = url_temp[0] + "//boot-source.xuexi.cn/data/app/" + query["id"] + ".js"
                respond = requests.get(js_url)
                respond.encoding = "utf-8"
                data = json.loads(respond.text.lstrip("callback(").rstrip(")"))
                article_title = data["title"]
                html = data["content"]

                # delete html tags
                content = re.compile(r"<[^>]+", re.S)
                paragraphs = content.sub(" ", html).rsplit(">")
                article = ""
                for paragraph in paragraphs:
                    if paragraph != " ":
                        article += paragraph
                        article += "\n"
                article_list.append([article_category, article_title, article, article_date])
            else:
                js_url = url_temp[0] + "//" + url_temp[2] + "/" + url_temp[3] + "/data" + url_temp[4].replace("html", "js")
                respond = requests.get(js_url)
                respond.encoding = "utf-8"
                for key, value in json.loads(respond.text.lstrip("globalCache = ").rstrip(":"), encoding="utf-8").items():
                    if key == "fp8ttetzkclds001":
                        content = value["detail"]["content"]
                        title = value["detail"]["first_name"]
                        article_list.append([article_category, title, content, article_date])
        return article_list
    
    def create_file(self, list_info):
        if not os.path.exists(r"data/学习强国"):
            os.mkdir(r"data/学习强国")
        for info in list_info:
            # create folder
            folder_path = r"data/学习强国/" + info[3]
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            path = r"data/学习强国/" + info[3] + r"/" + info[0] + ".txt"
            with open(path, "a+", encoding="utf-8") as f:
                f.write(info[1])
                f.write("\n")
                f.write(info[2])
                for i in range(10):
                    f.write("\n")


if __name__ == '__main__':
    history = History()
    json_data = history.get_json(history.urls)
    articles = history.get_articles(json_data)
    article_list = history.get_content(articles)
    history.create_file(article_list)
