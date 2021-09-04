import pymysql
import pandas as pd
import requests

def getDiamondList():
    url = 'https://cn.chowsangsang.com/eshop-cn/zh_CN/DIYList/getDIYProductList/anonymous/Jewellery-ByGemstone?sort=&q=&pageSize=5000&page=0&country=--'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    response = requests.get(url, headers=headers)
    text = response.json()
    product_list = pd.DataFrame.from_dict(text['productRefinements'][0]['productList'])

    return product_list


def insertIntoDatabase(product_list, host, port, user, password, database):
    conn = pymysql.connect(host, port, user, password, database)
    cursor = conn.cursor()
    sql = 'TRUNCATE TABLE bi_diamond'
    cursor.execute(sql)

    data = ((product_list.iloc[i, 0],
             product_list.iloc[i, 1],
             product_list.iloc[i, 2],
             product_list.iloc[i, 3],
             product_list.iloc[i, 4],
             product_list.iloc[i, 5],
             product_list.iloc[i, 6],
             product_list.iloc[i, 7],
             product_list.iloc[i, 8],
             product_list.iloc[i, 9],
             product_list.iloc[i, 10],
             product_list.iloc[i, 11],
             product_list.iloc[i, 12],
             product_list.iloc[i, 13],
             product_list.iloc[i, 14],
             product_list.iloc[i, 15],
             product_list.iloc[i, 16],
             product_list.iloc[i, 17],
             product_list.iloc[i, 18],
             product_list.iloc[i, 19],
             product_list.iloc[i, 20],
             product_list.iloc[i, 21],
             product_list.iloc[i, 22],
             product_list.iloc[i, 23],
             product_list.iloc[i, 24],
             product_list.iloc[i, 25],
             product_list.iloc[i, 26],
             product_list.iloc[i, 27],
             product_list.iloc[i, 28],
             product_list.iloc[i, 29],
             product_list.iloc[i, 30]) for i in range(0, len(product_list[['documentId']])))
    sql = 'INSERT INTO bi_diamond values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    cursor.executemany(sql, data)
    conn.commit()
    conn.close()