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
