# We have some data that contains a mixture of flower and shrubs in a list.
# Our customer would like two separate lists, one called "flowers" and one called "shrubs"
# Write code to populate the two lists with appropriate plants from "data"

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for plant in data:
    if "Flower" in plant:
        flowers.append(plant)
    elif "Shrub" in plant:
        shrubs.append(plant)

for number, a in enumerate(flowers):
    print("{}. {}".format(number + 1, a))

print()
print("-" * 10)
print()

for number, b in enumerate(shrubs):
    print("{}. {}".format(number + 1, b))

# In addition to splitting data into two lists, I wanted each list to be numbered
# I was able to achieve this using the code on lines 36/37 and 43/44
