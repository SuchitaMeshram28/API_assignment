from pip._vendor import requests
import pprint

header = {
    "access_token": 'fe66583bfe5185048c66571293e0d358'
}

try:
    # parameters to fetch records
    params = {
    "limit": 100,
    "offset": 1
    }

    # empty list to store records
    all_records = [] 

    # loop to fetch 500 records
    while params.get("offset") < 500:
        response = requests.get(f"https://globalmart-api.onrender.com/mentorskool/v1/sales", headers=header, params=params).json()

        all_records.append(response)
        params["offset"] = int(response.get("next").split("=")[1][:3])
        pprint.pprint(all_records)
        print(len(all_records))

except IndexError:
    print("Invalid Index")

except requests.exceptions.HTTPError as err:
    print(err)
    
except requests.exceptions.RequestException as r:
    print(r)