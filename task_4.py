import pandas as pd
from pip._vendor import requests


header = {
    "access_token": 'fe66583bfe5185048c66571293e0d358'
}
params = {
    "limit": 100,
    "offset": 1
    }

# empty list to store records
result = [] 

# loop to fetch 500 records
while params.get("offset") < 500:
    response = requests.get(f"https://globalmart-api.onrender.com/mentorskool/v1/sales", headers=header, params=params).json()

    result += response["dara"]
    params["offset"] = int(response.get("next").split("=")[1][:3])

# Normalize json data into dataframe
df = pd.json_normalize(result)

print(df.columns)

resultDataFrame = df[
    [
        "id",
        "sales_amt",
        "qty",
        "discount",
        "profit_amt",
        "order.order_id",
        "order.order_purchase_date",
        "order.order_status",
        "order.order_delivered_customer_date",
        "order.order_estimated_delivery_date",
        "product.product_id",
        "product.colors",
        "product.category",
        "order.customer.customer_id",
        "order.customer.customer_name",
        "order.vendor.vendor_id"
    ]
]

# saving dataframe to a csv file
resultDataFrame.to_csv("task_4.csv", index=False)
