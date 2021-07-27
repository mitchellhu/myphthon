import pandas as pd
import io
import requests

url = "http://dts.twse.com.tw/opendata/t187ap03_L.csv"
# load form local Drive
df = pd.read_csv(r"D:\t187ap03_L.csv")
companynamelist =df["公司名稱"]
print(companynamelist)



