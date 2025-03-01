#This is your starter file for the Creating a Weather App project
#The lines that start with a # are comments and will not show up in your code
#You should utilize this feature to leave notes about what variables are for
#And what operations your code is performing

#Try to have your program be inutitive for the user to interact with
#To help you get started, here are some components and a general outline for the program

#Import Libraries
import requests
#If you have an error when importing this library try running the below line in your terminal/command window (without the #
#python3 -m pip install requests
#If this does not work, reach out to your instructor ASAP

#Functions
def get_weather(api_key, zip):
    #Components for you to use
    #Component 1- get response from API and save it in usable format to data object
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    #Component 2- getting weather info from data object
    city = data['name']
    temp = data['main']['temp']
    weather_condition = data['weather'][0]['description']

    print(f"Weather temps in {city}:")
    print(f"Temperature: {temp}°F")
    print(f"Conditions: {weather_condition}")

# Function to validate that zipcode is only int input and length of zip is 5 characters long
def validate_zip(zip_code):
    return zip_code.isdigit() and len(zip_code) == 5

# function for the Main Program to collect user data
def main():
    api_key = input("Please paste your API key: ")
    while True:
        zip_code = input("Enter a valid zip code: ")
        # Calls validate_zip function to verify user input and loop them until given proper entry
        while not validate_zip(zip_code):
            print("Invalid entry. Please enter a 5 digit zip code.")
            zip_code = input("Enter a valid zip code: ")

        data = get_weather(api_key, zip_code)
        display_weather(data)

        selection = input("Would you like to view another location? 1= Yes, 2= No: ")
        if selection != '1':
            break

# Calls main function
if __name__ == "__main__":
    main()
    # Allows the window to stay open and viewable until the user hits enter
    input("Press enter to close the console. ")