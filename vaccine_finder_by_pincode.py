
import requests
import datetime
import json

POST_CODE = "302015"
age = 25

# Print details flag
print_flag = 'Y'

numdays = 20

print("Checking for pincode: {}".format(POST_CODE))
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]



for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        # print(json.dumps(resp_json, indent = 1))
        flag = False
        if resp_json["centers"]:
            print("Available on: {}".format(INP_DATE))
            if(print_flag=='y' or print_flag=='Y'):
                for center in resp_json["centers"]:
                    for session in center["sessions"]:
                        if session["min_age_limit"] <= age:
                            if session["available_capacity"] == 0:
                                print("\t", "zero capacity")
                            else:
                                print("\t", center["name"])
                                print("\t", center["block_name"])
                                print("\t Price: ", center["fee_type"])
                                print("\t Available Capacity: ", session["available_capacity"])
                                if(session["vaccine"] != ''):
                                    print("\t Vaccine: ", session["vaccine"])
                                print("\n\n")
                        else:  
                                print("\t", "No slots for the age limit")
            
                
        else:
            print("No available slots on {}".format(INP_DATE))2. 