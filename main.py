restaurants = ("Tayyabs", "Rasa", "Dishoom", "Xi' and impression", "Silk Road", "New Ming", "Trullo", "Manteca", "Ciao Bella")

iterated_restuarants = []

for restaurant in restaurants:
    iterated_restuarants.append(restaurant)

restaurant_cuisine = {
    "Indian": ["Tayyabs", "Rasa", "Dishoom"],
    "Chinese": ["Xi'an Impression", "Silk Road", "New Ming"],
    "Italian": ["Trullo", "Manteca", "Ciao Bella"]
}

indian_restaurants = restaurant_cuisine["Indian"]
chinese_restaurants = restaurant_cuisine["Chinese"]
italian_restaurants = restaurant_cuisine["Italian"]

restaurant_prices = {
    "Tayyabs" : "£20-30",
    "Rasa" : "£15-25",
    "Dishoom" : "£20-30",
    "Xi' and impression" : "£15-25",
    "Silk Road" : "£15-25",
    "New Ming" : "£10-20",
    "Trullo" : "£30-40",
    "Manteca" : "£40-50",
    "Ciao Bella" : "£20-30",

}

restaurant_tube_stations = {
    "Tayyabs": "Whitechapel",
    "Rasa": "St. John's Wood",
    "Dishoom": "Covent Garden",
    "Xi'an Impression": "Highbury & Islington",
    "Silk Road": "London Bridge",
    "New Ming": "Abbey Wood",
    "Trullo": "Highbury & Islington",
    "Manteca": "Barbican",
    "Ciao Bella": "Tottenham Court Road"
}

def getCuisine():
    print("Cuisines to choose from: Indian, Chinese, Italian")
    chooseCuisine = input("What cuisine are you feeling? Select 'Indian', 'Chinese' or 'Italian'. ")
    if chooseCuisine == "Indian":
        print("Indian restaurants:")
        return indian_restaurants
    elif chooseCuisine == "Chinese":
        print("Chinese restaurants:")
        return chinese_restaurants
    elif chooseCuisine == "Italian":
        # print("Italian restaurants:")
        return italian_restaurants
    else:
        return "This is not an option! Please select from a cuisine listed above."


def getCheapest():
    cheapest_restaurants = []
    print("Here are the restaurants that you can spend under £30:")
    for restaurant, price in restaurant_prices.items():
        price_range = price.replace("£", "")
        price_values = price_range.split("-")
        min_price = int(price_values[0])
        if min_price < 30:
            cheapest_restaurants.append(restaurant + ": " + price)
    return cheapest_restaurants

def getFancy():
    fancy_restaurants = []
    for restaurant, price in restaurant_prices.items():
        price_range = price.replace("£", "")
        price_values = price_range.split("-")
        min_price = int(price_values[0])
        if min_price >= 30:
            fancy_restaurants.append(restaurant + ": " + price)
    return fancy_restaurants

def getLocation():
    for restaurant in restaurants:
        print(restaurant)
    chooseRestaurant = input("Which restaurant would you like to know the nearest tube station to? Please enter the exact name of the restaurant. ")
    # return restaurant_tube_stations[chooseRestaurant]
    if chooseRestaurant in restaurant_tube_stations:
        return restaurant_tube_stations[chooseRestaurant]
    else:
        return "You have not selected a restaurant from the list above! Please make sure it is spelt the same way."

# def menu():
#     print("Welcome to my London food guide!")
#     print("1. List all restaurants")
#     print("2. Select cuisine")
#     print("3. Are times tough?")
#     print("4. Feeling fancy?")
#     print("5. Get nearest tube station to restaurant")
#     usersInput = input("Enter your option here: ")
#     if usersInput == "1":
#         for restaurant in restaurants:
#             print(restaurant)
#     elif usersInput == "2":
#         cuisine = getCuisine()
#         if isinstance(cuisine, list):
#             for restaurant in cuisine:
#                 print("- " + restaurant)
#         else:
#             print(cuisine)
#     elif usersInput == "3":
#         cheapest_restaurants = getCheapest()
#         for restaurant in cheapest_restaurants:
#             print(restaurant)
#     elif usersInput == "4":
#         fancy_restaurants = getFancy()
#         for restaurant in fancy_restaurants:
#             print(restaurant)
#     elif usersInput == "5":
#         print(getLocation())
#     else:
#         print("That is not an option! Please select a number from the menu above :)")
#     menu()

# menu()

activities = {
    "nightlife" : ["Be at One", "Moonshine Saloon", "ABQ London"],
    "sights and landmarks" : ["The Shard", "London Eye", "Sky Garden"],
    "fun and games" : ["Fairground", "Flight Club", "Puttshack"]
}

activity_prices = {
    "Be at One": "£10", 
    "Moonshine Saloon": "£15", 
    "ABQ London": "£20", 
    "The Shard": "£30", 
    "London Eye": "£25",  
    "Sky Garden": "£20",  
    "Fairground": "£15",  
    "Flight Club": "£25", 
    "Puttshack": "£18"
}

activity_tube_stations = {
    "Be at One": "Covent Garden",  
    "Moonshine Saloon": "Borough",  
    "ABQ London": "Hackney Wick",  
    "The Shard": "London Bridge",
    "London Eye": "Waterloo",
    "Sky Garden": "Bank", 
    "Fairground": "Oxford Circus",  
    "Flight Club": "Shoreditch High Street",  
    "Puttshack": "White City" 
}

def getActivity():
    chooseTheme = input("What theme of activity are you looking for? Please select from 'nightlife' or 'sights' or 'games'. ")
    if chooseTheme == "nightlife":
        print("Nightlife:")
        return activities["nightlife"]
    elif chooseTheme == "sights":
        print("Sights and Landmarks:")
        return activities["sights and landmarks"]
    elif chooseTheme == "games":
        # print("Fun and Games:")
        return activities["fun and games"]
    else:
        return "This is not an option! Please select from 'nightlife' or 'sights' or 'games'.  "

def menu():
    print("Welcome to Jeeivan's guide for going out in London!")
    usersinput = input("Are you looking to do an activity or go to a restuarant or both? Please select 'activity', 'restuarant', or 'both'. ")
    if usersinput == 'activity':
        activities = getActivity()
        if isinstance(activities, list):
            for activity in activities:
                print("- " + activity)
    elif usersinput == 'restaurant':
        cuisine = getCuisine()
        if isinstance(cuisine, list):
            for restaurant in cuisine:
                print("- " + restaurant)
        else:
            print(cuisine)
    elif usersinput == 'both':
        activities = getActivity()
        cuisine = getCuisine()
        if isinstance(activities, list) and isinstance(cuisine, list):
            print("Activities:")
            for activity in activities:
                print("- " + activity)
            print("\nRestaurants:")
            for restaurant in cuisine:
                print("- " + restaurant)
        else:
            print("Invalid selection!")
    else:
        print("This is not an option! Please select 'activity', 'restuarant', or 'both'. ")
    menu()

menu()