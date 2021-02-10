# -*- coding: utf-8 -*-
# restaurants_searcher.py

import json
import csv
import requests

# 初期設定
KEYID = "メールに記載されていたアクセスキーをここに入力"
HIT_PER_PAGE = 100
PREF = "PREF13"
FREEWORD_CONDITION = 1
FREEWORD = "渋谷駅"

#パラメータ設定
PARAMS = {"keyid": KEYID, "hit_per_page":HIT_PER_PAGE, "pref":PREF, "freeword_condition":FREEWORD_CONDITION, "freeword":FREEWORD}

def write_data_to_csv(params):
    restaurants = [["名称","住所","営業日","電話番号"]]
    json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/", params=params).text
    response = json.loads(json_res)
    if "error" in response:
        return print("エラーが発生しました！")
    for restaurant in response["rest"]:
        rest_info = [restaurant["name"], restaurant["address"], restaurant["opentime"], restaurant["tel"]]
        restaurants.append(rest_info)
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(restaurants)
    return print(restaurants)

write_data_to_csv(PARAMS)