# -*- coding: utf-8 -*-
# restaurants_searcher.py

import json
import csv
import requests

# 初期設定
KEYID = "メールに記載されていたアクセスキーをここに入力"
COUNT = 100
PREF = "Z011" #東京
FORMAT = "json"


PARAMS = {"key":KEYID, "count":COUNT, "large_area":PREF, "format":FORMAT}

def write_data_to_csv(params):
    restaurants = [["名称","住所","営業日"]]
    json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params).text
    response = json.loads(json_res)
    if "error" in response:
        return print("エラーが発生しました！")

    for restaurant in response["results"]["shop"]:
        rest_info = [restaurant["name"], restaurant["address"], restaurant["open"]]
        restaurants.append(rest_info)

    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(restaurants)

    return print(restaurants)

write_data_to_csv(PARAMS)