import rapid_auth
import json


##
## First setup config.py with your API key and crypting key
##

print("Press 1 for Sign Up and 2 for Sign In")

input_1 = input()

signed_in = False

while signed_in == False:
    if input_1 == "1":
        print("Enter Username: ")
        username = input()
        print("Enter Password: ")
        password = input()
        json_response = json.loads(rapid_auth.sign_up_user(username, password))
        if json_response["status"] == "success":
            print("Successfully Signed Up")
            signed_in = True
        else:
            print("Failed to Sign Up")
            print("Error: " + json_response["message"])
    elif  input_1 == "2":
        print("Enter Username: ")
        username = input()
        print("Enter Password: ")
        password = input()
        json_response = json.loads(rapid_auth.sign_in_user(username, password))
        if json_response["status"] == "success":
            print("Successfully Signed In")
            signed_in = True
        else:
            print("Failed to Sign In")
            print("Error: " + json_response["message"])

print("Press 1 to get active keys and 2 redeem a key")
input_2 = input()
if input_2 == "1":
    json_response = json.loads(rapid_auth.get_active_keys(username, password))
    if json_response["status"] == "success":
        counter = 1
        for product in json_response["products"]:
            print("Product " + str(counter) + ": " + product["product_name"])
            print("Days left: " + str(product["days_left"]))
            print("Lifetime: " + str(product["lifetime"]))
            print("Key name: " + product["key_name"])
            print("\n\n")
            counter += 1
    else:
        print("Failed to get active keys")
        print("Error: " + json_response["message"])
elif input_2 == "2":
    print("Enter License Key: ")
    license_key = input()
    json_response = json.loads(rapid_auth.redeem_license_key(username, password, license_key))
    if json_response["status"] == "success":
        print("Successfully Redeemed License Key")
    else:
        print("Failed to Redeem License Key")
        print("Error: " + json_response["message"])