#
# QUESTION 1
#

trip = {
    "driver": {
        "first_name": "Danny",
        "last_name": "Dreyfus",
        "avg_rating": 3.6,
        "total_rides": 950
    },
    "vehicle": {
        "make": "Tesla",
        "model": "Cybertruck",
        "year": 2021,
        "color": "silver"
    },
    "rideshare": True,
    "pickup_location": "Grand Central Terminal",
    "stops": [
        {"sequence": 1, "passenger": "Vishal", "destination": "Madison Square", "fare": 3.99},
        {"sequence": 2, "passenger": "Clara", "destination": "Union Square", "fare": 5.99},
        {"sequence": 3, "passenger": "Lee", "destination": "Washington Square", "fare": 7.99}
    ]
}

print("------------------")
print("PROCESSING RIDESHARE DATA...")
print("------------------")

#
# PART A
#

print("-----------------------")
print("Part A")

# todo: write some Python code here to answer the question!
print("Your driver is ",trip["driver"]["first_name"])


#
# PART B
#

print("-----------------------")
print("Part B")

# todo: write some Python code here to answer the question!
stops = len(trip["stops"])
print("This trip will make",stops, "stops")

#
# PART C
#
print("-----------------------")
print("Part C")

# todo: write some Python code here to answer the question!

stoplist = trip["stops"]
destination = stoplist[len(stoplist)-1]
print(destination["destination"])




#
# PART D
#

print("-----------------------")
print("Part D")
# todo: write some Python code here to answer the question!

for id in stoplist:
    print(id["passenger"])