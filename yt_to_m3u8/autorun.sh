#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests
python3 -m pip install pandas

cd $(dirname $0)/yt_to_m3u8/

python3 youtube_to_m3u.py
