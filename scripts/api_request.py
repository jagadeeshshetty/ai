# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:31:51 2017

@author: jagadeesh
"""

import requests
import json


api = "https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=votes&site=stackoverflow&tagged=python&accepted=True&title=how"

response = requests.get(api)

json_response = json.loads(response.text)

for item in json_response["items"]:
    print(item["owner"]["link"])
    
    
    
    
    