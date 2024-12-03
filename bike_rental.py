import json
import datetime
import smtplib
import os

def rent_bike(customer_name: str, rental_duration):
    rental = {"clientName": customer_name, "rentalDuration": rental_duration, "rentalCost": calculate_cost(rental_duration)}
    save_rental(rental)
    return 0

def calculate_cost(rental_duration: int):
    rental_duration = rental_duration - 1
    if rental_duration >= 0 : 
        finalCost = 10 + 5 * rental_duration
        return finalCost
    else:
        print("Invalid rental time")
        return 0
    

def save_rental(rental: dict):
    path = './data/rentals.json'
    isExist = os.path.exists(path) 
    if(isExist):  
        with open("data/rentals.json", mode='r', encoding='utf-8') as out_file:
            data = json.load(out_file)
            data = list(data)
            print(data)
            data.append(rental)
            print(data)
        with open("data/rentals.json", mode='w+', encoding='utf-8') as out_file:
            json.dump(data, out_file)
        print("Added entry")
    else:
        if not os.path.exists("./data"):
            os.makedirs("./data")
        with open("data/rentals.json", mode='w+', encoding='utf-8') as out_file:
            data = []
            data.append(rental)
            json.dump(data, out_file)
        print("Added entry")


def load_rentals():
    path = './data/rentals.json'
    isExist = os.path.exists(path) 
    if(isExist):
        with open("data/rentals.json", 'r') as out_file:
            data = json.load(out_file)
        for i in range(len(data)):
            print(f"Client {data[i]["clientName"]} rented a bike for {data[i]["rentalDuration"]} with a cost of {data[i]["rentalCost"]} PLN.")
    else:
        print("The given file does not exists.")
    
def cancel_rental(customer_name:str):
    path = './data/rentals.json'
    isExist = os.path.exists(path) 
    if(isExist):  
        with open("data/rentals.json", mode='r', encoding='utf-8') as out_file:
            data = json.load(out_file)
            data = list(data)
        i = 0
        while(i < len(data)):
            if(data[i]["clientName"].lower() == customer_name.lower()):
                print(f"Succesfully deleted{data[i]}")
                del data[i]
                i = i-1
                print("Deleted entry") 
            i = i + 1
            with open("data/rentals.json", mode='w+', encoding='utf-8') as out_file:
                json.dump(data, out_file)        
    else:
        print("The given file does not exists.")
        
def generate_daily_report():
    filePath = (f"data/daily_report_{datetime.now():%Y-%m-%d}.json")
    print(filePath)
    data = load_rentals()
    with open(filePath, mode='w+', encoding='utf-8') as out_file:
            json.dump(data, out_file,indent=6)
        
def send_rental_invoice_email(customer_email, rental_details: dict):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = "testemail@outlook.com"
    PASSWORD = "somepassword"

    MESSAGE = f"""Subject: Invoice email - Bike Rental Company
    Thanks for renting one of our bikes!

    Name: {rental_details["clientName"]}
    Duration: {rental_details["rentalDuration"]}
    Cost: {rental_details["rentalCost"]}
    Date: {rental_details["rentalDate"]}
    
    Bike Rental Company
    """
    smpt = smtplib.SMTP(HOST, PORT)

    status_code, response = smpt.ehlo()
    print(f"Server echo: {status_code}, {response}")

    status_code, response = smpt.starttls()
    print(f"Starting: {status_code}, {response}")

    status_code, response = smpt.login(FROM_EMAIL, PASSWORD)
    print(f"Logging in: {status_code}, {response}")

    smpt.sendmail(FROM_EMAIL, customer_email, MESSAGE)
    smpt.quit()
