#Necessary Imports
from unittest import result
import requests
import os
import json
from pprint import pprint


url = "https://raw.githubusercontent.com/amcypher/PII-Scrubber-and-Sample-Data/main/pii-json.json"
#headers = {"Content-Type": "application/json", "X-Auth-Key": key, "X-Auth-Email": email}

#Method to pull data from the API      
def pull_data(url):

    #Set our headers for the HTTP Request
    headers = {"Content-Type": "application/json"}
    #Try catch to handle failed HTTP Requests
    try:
        response = requests.get(url, headers=headers)
        #Return the response if HTTP 200
        if response.status_code == 200:return json.loads(response.text)
        #Non 200 Response
        else:
            print('Status Code' + response.status_code)
            return False
    except:
        #Exception Occured
        print("API Fetch Failed")
        return False

def scrubba(result):
    #Removing the PII that we know exists in these Key Value Pairs
    #Could wrap in a try catch to be wary of KeyError Exceptions etc but we'll assume the data always has these fields
    #Object references passed to this function
    result['pii_instances'][2]['ssn'] = "xxx-xx-xxxx"  
    result['pii_instances'][1]['date_of_birth'] = 'xxxx/xx/xx'

#Main
def main():
    #Get the data
    my_results = pull_data(url)
    #Check the outcome
    if my_results != False:
        #Scrub the data
        scrubba(my_results)
        #Print the keys
        pprint(my_results.keys())
        #Print the scrubbed version
        pprint(my_results)
    else:
        #Something went wrong
        print("Exiting Program")
        exit()

if __name__ == "__main__":
    main()
