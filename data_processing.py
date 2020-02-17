# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:45:44 2020

@author: wtjang
"""

"""
계측 파일 전처리 함수 
"""


import os
import pandas as pd

path_dir = r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일'
file_list = os.listdir(path_dir)
file_list.sort()

f = open(path_dir +  '\\' +  file_list[3]) # SFX200 가져오기

lines = f.readlines()
labels = lines[0].split(',') # line 0 : Factor  
df = pd.DataFrame(columns = labels)

for i in range(2, len(lines)):
    temp = lines[i]
    temp = temp.split(',')
    
    df.loc[i-2] = temp


del df[df.iloc[:,-1].name] # 제일 마지막 빈 열 삭제
df_Meta = df.loc[:, ['SLOT', 'LOT ID', 'COLLECTION DATE/TIME', 'RECIPE', 'MATERIAL']]
df_Stat = df.loc[:, ['RESULT TYPE', 'MEAN', 'MIN', 'MAX', '% STDDEV', 'STDDEV', '3 % STDDEV', '3 STDDEV', 'RANGE']]
df_Point = df.loc[:, 'DATA[1]':(df.iloc[:,-1]).name]


num_first_Wafer = int(df_Meta.loc[0,'SLOT']) 
num_last_Wafer = int(df_Meta.loc[len(df_Meta)-1,'SLOT'])

num_Wafer =num_last_Wafer - num_first_Wafer + 1
num_Feature = len(df_Meta) / num_Wafer

df_Meta_final = pd.DataFrame(columns = df_Meta.columns)
for k in range(0, num_Wafer):
    df_Meta_final.loc[k] = df_Meta.loc[k*num_Feature]
    

'''
사용자가 만약에 19번 Wafer를 호출한다

num_random_Wafer = 19 # 아마도 나중에 사용자 입력받을 값

df_Meta_final['SLOT'] == str(num_random_Wafer) #이거는 그냥 인넥스 판별용이구
df_Meta_final.loc[df_Meta_final['SLOT'] == str(num_random_Wafer)] # 이걸로 해당하는 데이터 프레임 가져옴


통계량 데이터 프레임에서 임의의 Wafer 번호가 주어지면 그에 해당하는 데이터 프레임 가져옴

df_Stat_T = df_Stat.T
df_Stat_T.loc[:,((num_random_Wafer - num_first_Wafer) * num_Feature):((num_random_Wafer - num_first_Wafer) * num_Feature)+2]
가져오는 형식도 Dataframe 형태임.


데이터 포인트 프레임도 마찬가지

df_Point_T = df_Point.T
df_Point_T.loc[:,((num_random_Wafer - num_first_Wafer) * num_Feature):((num_random_Wafer - num_first_Wafer) * num_Feature)+2]

'''

num_random_Wafer = 12

df_Meta_final.loc[df_Meta_final['SLOT'] == str(num_random_Wafer)]

df_Stat_T = df_Stat.T
df_Stat_T.loc[:,((num_random_Wafer - num_first_Wafer) * num_Feature):((num_random_Wafer - num_first_Wafer) * num_Feature)+2]

df_Point_T = df_Point.T
df_Point_T.loc[:,((num_random_Wafer - num_first_Wafer) * num_Feature):((num_random_Wafer - num_first_Wafer) * num_Feature)+2]




