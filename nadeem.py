import requests
from tqdm import tqdm
import time
import pandas as pd
from datetime import date

url = "https://www.travelplusapp.com/company/v1/corporate/admin/bookings"
params = {
    "page": "1",
    "size": "100",
    "type": "CURRENT",
    "showOnlyAwaitingConfirmation": "false",
    "sortOrder": "ASC",
    "sortBy": "checkOut"
}
token = "7f9c8dde-58b7-4343-9547-c6819d0aabfa"
cookies = {
    "token": token
}

response = requests.get(url, params=params, cookies=cookies)

if response.status_code == 200:
    for i in tqdm(range(10)):
        time.sleep(0.1)  # Simulating some work
    print("Data Pulled successfully ----------------------->>>>>>>>>>>>>>>>>>>>>>>>>>")
    res_data = response.json()
    table_data = res_data.get("data", {}).get("bookings", {}).get("content", [])
    temp_dict = {"EMPLOYEE NAME": [], "NUMBER": [], "PROPERTY NAME": [], "CITY": [], "CHECK IN": [], "CHECK OUT": [],
                 "BID": []}

    # EMPLOYEE NAME, NUMBER, PROPERTY NAME , CITY, CHECK IN , CHECK OUT, BID
    for each in table_data:
        temp_dict["PROPERTY NAME"].append(each.get("property", "-"))
        temp_dict["CITY"].append(each.get("city", "-"))
        temp_dict["CHECK IN"].append(each.get("checkInDate", "-"))
        temp_dict["CHECK OUT"].append(each.get("checkOutDate", "-"))
        temp_dict["BID"].append(each.get("bookingId", "-"))

        ## nested data
        travellar_data = each.get('travellers', [])[0] if each.get('travellers', []) else {}
        name = travellar_data.get("firstName", "") + travellar_data.get("lastName", "")
        temp_dict["EMPLOYEE NAME"].append(name)
        temp_dict["NUMBER"].append(travellar_data.get("mobile", ""))

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(temp_dict)

    # Create an Excel writer using pandas
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=False)

    # Close the writer and save the Excel file
    writer._save()
    print()
    print("Done Successfully !!!!!")
else:
    print("Request failed with status code:", response.status_code)

