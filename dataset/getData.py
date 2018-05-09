import requests
import time
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
url = "http://data.tmd.go.th/nwpapi/v1/forecast/location/daily/at"
headers = {
     'accept': "application/json",
     'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImI0M2YzNzcyNzNkYmI4MjFhMmMxYThmODA4ODUwYzU1ZWY1NmFiYzJmNjdjYmIyNTA4MTgxZjFhMzM4OGE0ZDdkZmU0ZjkxMzFkMjBiYWUzIn0.eyJhdWQiOiIyIiwianRpIjoiYjQzZjM3NzI3M2RiYjgyMWEyYzFhOGY4MDg4NTBjNTVlZjU2YWJjMmY2N2NiYjI1MDgxODFmMWEzMzg4YTRkN2RmZTRmOTEzMWQyMGJhZTMiLCJpYXQiOjE1MjU3MDQzMzAsIm5iZiI6MTUyNTcwNDMzMCwiZXhwIjoxNTU3MjQwMzMwLCJzdWIiOiI1MCIsInNjb3BlcyI6W119.djgcKe6xV59871lQbT68OOcO2Cq34ru_oq0oaFroAvMcVQzMCB1K5d3mK4YZ26RPPU2a3SkZEAJ36LQN0iOTh-bulGybBV2vRgEui6_lD7TABHTDZVYbk_jJyh9DBcfNHm8dndHDut2AW9lO8Ry0yS16664aX0lHF--oNirC7zkGhKmyBfvnlcVgRTHfzuCNyhJQrA87v3rqob5ZkyQwhLI577KZJXTJsssVS4ey9TsYXF9lTcPvpQnuE20oI4D9ho4uBDDYOUlP1-xCBOAwD1fznjUaQI5lNol4IDxVu-g4oQHeFrjURF_f2UoQhyfddpwfX-wj9v7DR-q-kJwSrSc2GhWG0ih8bYAZA-0IrYFPJsEDZT-7YC3UIlT6vRtVPBvdAOc2AR4Tv-7rBMZ4AHoHEQOqPUabG1VQbNZX6Uiah9aN_faC4u6P6pVsuc-d80VlhgPmFEecPUf9GY_TRU6OrrDYJVMBShrOZur0p5PBoXSmxZhKPKkxsY5lfTkm5ld9biItoJXCuUI1Nt819hKaxOb8PKwWewXfBnoJRJ-H_2mOfFwRE_3KyTrK5s1A_ZmtbgSmHq13jDfRFWm1oM74YMp5rcecbZBv5yR_kxawA89Tbyj8yxrWCbZroA5_66i4RInb-P8pigdbrbYLPmUngb0j3csqgE7_K2GWJrA",
}
with open('tumbun-Sheet2.csv','rb') as f:
    data = list(csv.reader(f))
    for row in data:
        if(row[10]=="LAT"):
            continue
        print row[10], row[11] 
        querystring = {
            "lat":row[10], "lon":row[11], 
            "fields":"tc,rh,slp,rain,ws10m,ws925,ws850,ws700,ws500,ws200,cloudlow,cloudmed,cloudhigh", 
            "date":"2018-01-27", 
            "duration":"126"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        res =  json.loads(response.text)
        for r in res['WeatherForecasts'][0]['forecasts']:
            with open('data.csv','a') as ff:
                rdata = r['data']
                pdata = str(row[10])+","+str(row[11])+","+str(rdata['tc'])+","+str(rdata['rh'])+","+str(rdata['slp'])+","+str(rdata['rain'])+","+str(rdata['ws10m'])+","+str(rdata['ws925'])+","+str(rdata['ws850'])+","+str(rdata['ws700'])+","+str(rdata['ws500'])+","+str(rdata['ws200'])+","+str(rdata['cloudlow'])+","+str(rdata['cloudmed'])+","+str(rdata['cloudhigh'])+","+str(r['time'])+"\n"
                ff.write(pdata)
                ff.close()
        time.sleep(1.5)
