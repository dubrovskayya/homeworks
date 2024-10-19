
import pandas as pd
import json

#1
def from_json(s_json):
    try:
        res=json.loads(s_json)
        print(res)
    except json.JSONDecodeError:
        print('string is not a json')

from_json('dfghj')
#?

#2

try:
    df=pd.read_excel('exam.xls')
    print(len(df))
except FileNotFoundError:
    print('noy')

#4
x=pd.read_excel('second.xls')
y=pd.read_excel('first.xls')
result=pd.concat([x,y],axis=0)
result.to_excel('result.xlsx', index=False)
