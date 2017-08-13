import pandas as pd
import requests

for i in range(1,19):
    url = 'http://yarbis.yildiz.edu.tr/home/search/areaSearch?keyArea=%25%25%25&sort=level2_unit_name_tr-total.desc&page='+str(i)
    df = pd.read_html(requests.get(url).content)[0]
    df = pd.DataFrame(df)
    df.to_csv("academicians.csv",mode='a', header = False, index = False, encoding = 'utf-8')
