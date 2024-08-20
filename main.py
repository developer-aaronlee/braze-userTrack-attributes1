import csv
import json
import requests

url = 'https://rest.iad-06.braze.com/users/track'
API_KEY = 'Bearer api_key'
headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('batch_test_1.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        if len(row)==0:
            continue
        temp = row[0].split(",")
        dic = {}
        if temp[0] == "external_id":
            continue
        if temp[0] != "":
            dic["external_id"] = temp[0]
        if temp[1] != "":
            dic["currently_active"] = temp[1]
        if temp[2] != "":
            dic["offer_codes_used"] = temp[2]
        if temp[3] != "":
            dic["source"] = temp[3]
        if temp[4] != "":
            dic["source_type"] = temp[4]
        if temp[5] != "":
            dic["subscription_interval"] = temp[5]
        if temp[6] != "":
            dic["total_videos_watched"] = temp[6]
        if temp[7] != "":
            dic["user_created_date"] = temp[7]

        body = json.dumps({"attributes" : [dic]})
        response = requests.post(url, data=body, headers=headers)
        print(response.json())
