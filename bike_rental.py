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

def calculate_cost(rental_duration):
    return 0

def save_rental(rental: dict):
    return 0 

