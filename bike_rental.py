import json
import datetime
import smtplib
import os

def rent_bike(customer_name: str, rental_duration):
    rental = {
        "clientName" : customer_name,
        "rentalDuration" : rental_duration,
        "rentalCost" : calculate_cost(rental_duration)
    }
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
    return 0 

