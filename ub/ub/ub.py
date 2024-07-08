import requests
import re
import os
import pandas as pd
data = pd.read_csv("data.csv")
i = 0
last_id = data['id'].iloc[-1]
for i in range(last_id+1):
  channel_name = data[data['id'] == i]['channel_name'].values[0]
  channel_id = data[data['id'] == i]['channel_id'].values[0]
  file_name = data[data['id'] == i]['file_name'].values[0]
  url = "http://tonkiang.us/?channel="+channel_name
  response = requests.get(url)
  m3u8_links = re.findall(r'https://.*?.ubtvfans.com/.*?/'+str(channel_id)+'/.*?/index.m3u8', response.text)
  if m3u8_links:
    m3u8_1 = "#EXTM3U"
    m3u8_2 = "#EXT-X-VERSION:3"
    m3u8_3 = "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=540000"
    f = open("m3u_list/"+file_name+".m3u8", 'w')
    f.write(m3u8_1 + '\n' + m3u8_2 + '\n' + m3u8_3 + '\n' + m3u8_links[0])
    f.close()
  else:
    if os.path.exists("nolink/nolink.txt"):
      with open("nolink/nolink.txt", 'a') as f:
        f.write('\n'+file_name)
    else:
      f = open("nolink/nolink.txt", 'w')
      f.write(file_name)
      f.close()