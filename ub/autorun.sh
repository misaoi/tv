#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests
python3 -m pip install pandas

cd $(dirname $0)/ub/

python3 ublink.py
