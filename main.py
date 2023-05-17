restaurants = ("Tayyabs", "Rasa", "Dishoom", "Xi' and impression", "Silk Road", "New Ming", "Trullo", "Manteca", "Ciao Bella")

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

indian_restaurant_prices = {
    "Tayyabs" : "£20-30",
    "Rasa" : "£15-25",
    "Dishoom" : "£20-30"}

chinese_restaurant_prices = {
    "Xi' and impression" : "£15-25",
    "Silk Road" : "£15-25",
    "New Ming" : "£10-20"
}

italian_restaurant_prices = {
     "Trullo" : "£30-40",
    "Manteca" : "£40-50",
    "Ciao Bella" : "£20-30"
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

indian_restaurant_tube_stations = {
    "Tayyabs": "Whitechapel",
    "Rasa": "St. John's Wood",
    "Dishoom": "Covent Garden"
}

chinese_restaurant_tube_stations = {
    "Xi' and impression": "Highbury & Islington",
    "Silk Road": "London Bridge",
    "New Ming": "Abbey Wood"
}

italian_restaurant_tube_stations = {
    "Trullo": "Highbury & Islington",
    "Manteca": "Barbican",
    "Ciao Bella": "Tottenham Court Road"
}

indian_restaurants = {
    "Tayyabs": {
        "price": "£20-30",
        "tube_station": "Whitechapel"
    },
    "Rasa": {
        "price": "£15-25",
        "tube_station": "St. John's Wood"
    },
    "Dishoom": {
        "price": "£20-30",
        "tube_station": "Covent Garden, Shoreditch High Street, Canary Wharf, King's Cross St. Pancras"
    },
    "Masala Zone": {
        "price": "£15-25",
        "tube_station": "Earl's Court"
    },
    "Chutney Mary": {
        "price": "£30-40",
        "tube_station": "Sloane Square"
    }
}

chinese_restaurants = {
    "Xi'an Impression": {
        "price": "£15-25",
        "tube_station": "Highbury & Islington"
    },
    "Silk Road": {
        "price": "£15-25",
        "tube_station": "London Bridge"
    },
    "New Ming": {
        "price": "£10-20",
        "tube_station": "Abbey Wood"
    },
    "Duddell's": {
        "price": "£40-50",
        "tube_station": "London Bridge"
    },
    "Dumplings' Legend": {
        "price": "£15-25",
        "tube_station": "Leicester Square"
    }
}

italian_restaurants = {
    "Trullo": {
        "price": "£30-40",
        "tube_station": "Highbury & Islington"
    },
    "Manteca": {
        "price": "£40-50",
        "tube_station": "Barbican"
    },
    "Ciao Bella": {
        "price": "£20-30",
        "tube_station": "Tottenham Court Road"
    },
    "Padella": {
        "price": "£10-20",
        "tube_station": "London Bridge"
    },
    "Vapiano": {
        "price": "£7-13",
        "tube_station": "Tottenham Court Road, London Bridge, Paddington"
    }
}

mexican_restaurants = {
    "Cielo Blanco": {
        "price": "£15-25",
        "tube_station": "Leeds"
    },
    "Wahaca": {
        "price": "£10-20",
        "tube_station": "Covent Garden"
    },
    "El Pastor": {
        "price": "£20-30",
        "tube_station": "London Bridge"
    },
    "DF / Mexico": {
        "price": "£15-25",
        "tube_station": "Spitalfields"
    },
    "La Bodega Negra": {
        "price": "£20-30",
        "tube_station": "Leicester Square"
    }
}

japanese_restaurants = {
    "Nobu": {
        "price": "£50-100",
        "tube_station": "Old Street"
    },
    "Roka": {
        "price": "£40-60",
        "tube_station": "Fitzrovia"
    },
    "Yashin Ocean House": {
        "price": "£30-50",
        "tube_station": "South Kensington"
    },
    "Kikuchi": {
        "price": "£40-60",
        "tube_station": "West Hampstead"
    },
    "Sushisamba": {
        "price": "£50-100",
        "tube_station": "Liverpool Street, Tottenham Court Road"
    }
}




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

nightlife_activities = {
    "Be at One": {
        "price": "£10",
        "tube_station": "Covent Garden"
    },
    "Moonshine Saloon": {
        "price": "£15",
        "tube_station": "Borough"
    },
    "ABQ London": {
        "price": "£20",
        "tube_station": "Hackney Wick"
    },
    "Cahoots": {
        "price": "£18",
        "tube_station": "Oxford Circus"
    },
    "Jazz Café": {
        "price": "£20",
        "tube_station": "Camden Town"
    }
}

sights_landmarks_activities = {
    "The Shard": {
        "price": "£30",
        "tube_station": "London Bridge"
    },
    "London Eye": {
        "price": "£25",
        "tube_station": "Waterloo"
    },
    "Sky Garden": {
        "price": "£20",
        "tube_station": "Bank"
    },
    "Buckingham Palace": {
        "price": "Free",
        "tube_station": "Victoria"
    },
    "Tower of London": {
        "price": "£28",
        "tube_station": "Tower Hill"
    }
}

fun_games_activities = {
    "Fairground": {
        "price": "£15",
        "tube_station": "Oxford Circus"
    },
    "Flight Club": {
        "price": "£25",
        "tube_station": "Shoreditch High Street"
    },
    "Puttshack": {
        "price": "£18",
        "tube_station": "White City"
    },
    "Bounce": {
        "price": "£20",
        "tube_station": "Old Street"
    },
    "Boom Battle Bar": {
        "price": "£9",
        "tube_station": "North Greenwich"
    }
}

def getActivity():
    chooseTheme = input("What theme of activity are you looking for? Please select from 'nightlife' or 'sights' or 'games'. ")
    if chooseTheme == "nightlife":
        print("Nightlife:")
        for activity, data in nightlife_activities.items():
            print(activity, "- Price:", data["price"], "- Nearest Tube Station:", data["tube_station"], "\n")
    elif chooseTheme == "sights":
        print("Sights and Landmarks:")
        for activity, data in sights_landmarks_activities.items():
            print(activity, "- Price:", data["price"], "- Nearest Tube Station:", data["tube_station"], "\n")
    elif chooseTheme == "games":
        print("Fun and Games:")
        for activity, data in fun_games_activities.items():
            print(activity, "- Price:", data["price"], "- Nearest Tube Station:", data["tube_station"], "\n")
    else:
        return "This is not an option! Please select from 'nightlife' or 'sights' or 'games'.  "


def getCuisine():
    print("Cuisines to choose from: Indian, Chinese, Italian")
    chooseCuisine = input("What cuisine are you feeling? Select 'Indian', 'Chinese', 'Italian', 'Mexican' or 'Japanese'. ")
    if chooseCuisine == "Indian":
        print("Indian restaurants:")
        for restaurant, data in indian_restaurants.items():
            print(restaurant, "- Price:", data["price"], "- Nearest Tube Station:", data["tube_station"], "\n")
    elif chooseCuisine == "Chinese":
        print("Chinese restaurants:")
        for restaurant, data in chinese_restaurants.items():
            print(restaurant, "- Price:", data["price"], "- Nearest Tube Station:", data["tube_station"], "\n")
    elif chooseCuisine == "Italian":
        print("Italian restaurants:")
        for restaurant, data in italian_restaurants.items():
            print(restaurant, "- Price:", data["price"], "- Nearest Tube Station:", data["tube_station"], "\n")
    elif chooseCuisine == "Mexican":
        print("Mexican restaurants:")
        for restaurant, data in mexican_restaurants.items():
            print(restaurant, "- Price:", data["price"], "- Nearest Tube Station:", data["tube_station"], "\n")
    elif chooseCuisine == "Japanese":
        print("Japanese restaurants:")
        for restaurant, data in japanese_restaurants.items():
            print(restaurant, "- Price:", data["price"], "- Nearest Tube Station:", data["tube_station"], "\n")
    else:
        return "This is not an option! Please select from a cuisine listed above."


def menu():
    print("Welcome to Jeeivan's guide for going out in London!")
    print("Disclaimer- All prices are average prices are found online and are subject to change")
    usersinput = input("Are you looking to do an activity or go to a restuarant or both? Please select 'activity', 'restuarant', or 'both'. ")
    if usersinput == 'activity':
        getActivity()
    elif usersinput == 'restaurant':
        getCuisine()
    elif usersinput == 'both':
        print("Activities:")
        getActivity()
        print("\nRestaurants:")
        getCuisine()
    else:
        print("This is not an option! Please select 'activity', 'restuarant', or 'both'. ")
    menu()

menu()