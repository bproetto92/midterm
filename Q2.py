#
# QUESTION 2
#

tweets = [
    {
        "id": 100200297,
        "full_text": "Look at this delicious sandwich!",
        "img_url": "https://sandwhoa.com/sandwich.png",
        "user": {"screen_name": "sandwhoa", "followers": 5000},
        "likes_count": 150
    },
    {
        "id": 100200298,
        "full_text": "I love sandwiches",
        "img_url": None,
        "user": {"screen_name": "person1", "followers": 100},
        "likes_count": 5
    },
    {
        "id": 100200299,
        "full_text": "@sandwhoa yumm...",
        "img_url": None,
        "user": {"screen_name": "person2", "followers": 200},
        "likes_count": 10
    },
    {
        "id": 100200300,
        "full_text": "@sandwhoa that sandwich looks amazing!!",
        "img_url": None,
        "user": {"screen_name": "person3", "followers": 300},
        "likes_count": 35
    },
    {
        "id": 100200301,
        "full_text": "I ate a great sandwich today",
        "img_url": None,
        "user": {"screen_name": "person4", "followers": 400},
        "likes_count": 50
    }
]

print("------------------")
print("PROCESSING SOCIAL MEDIA DATA...")
print("------------------")

#
# PART A
#

print("------------------------")
print("Part A")

# todo: write some Python code here to answer the question!
first = tweets[0]
print(first["user"]["screen_name"])

#
# PART B
#

print("------------------------")
print("Part B")

# todo: write some Python code here to answer the question!
for id in tweets:
    if "@sandwhoa" in id["full_text"]:
        print(id["user"]["screen_name"])

    
# todo: write some Python code here to answer the question!


#
# PART C
#

print("------------------------")
print("Part C")

# todo: write some Python code here to answer the question!
likes = []

for id in tweets:
    if "@sandwhoa" in id["full_text"]:
        likes.append(id)

likes2 = sorted(likes, key = lambda i: i['likes_count'],reverse=True)
likes2 = likes2[0]
print(likes2["user"]["screen_name"])

#https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/

