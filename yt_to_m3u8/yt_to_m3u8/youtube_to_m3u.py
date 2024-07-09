import requests
import pandas as pd
data = pd.read_csv("youtube_channel.csv")
i = 0
last_id = data['id'].iloc[-1]
for i in range(last_id+1):
  file_name = data[data['id'] == i]['file_name'].values[0]
  url = data[data['id'] == i]['url'].values[0]
  response = requests.get(url, timeout=15).text
  if '.m3u8' not in response:
    m3u8link = "https://raw.githubusercontent.com/misaoi/tv/main/yt_to_m3u8/yt_to_m3u8/nolive/index.m3u8"
  else:
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
      if 'https://' in response[end-tuner : end]:
        link = response[end-tuner : end]
        start = link.find('https://')
        end = link.find('.m3u8') + 5
        break
      else:
        tuner += 5
    m3u8link = link[start : end]
    m3u8_1 = "#EXTM3U"
    m3u8_2 = "#EXT-X-VERSION:3"
    m3u8_3 = "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=540000"
    f = open("m3u_list/"+ file_name + ".m3u8", 'w')
    f.write(m3u8_1 + '\n' + m3u8_2 + '\n' + m3u8_3+ '\n' + m3u8link)
    f.close()
