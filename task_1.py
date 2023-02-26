from pip._vendor import requests

header = {
    "access_token": 'fe66583bfe5185048c66571293e0d358'
}

offset = 1
limit = 500

response = requests.get(f"https://globalmart-api.onrender.com/mentorskool/v1/sales?offset={offset}&limit={limit}",headers=header)

if response.status_code == 200:
    data = response.json()
    # print(data)
else:
    print('Error:',response.status_code)