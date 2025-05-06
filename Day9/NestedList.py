# Nested list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# task is access list elements
print(travel_log["France"][1])


# Nested List
# Access inside list list elements

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

# Dictionary inside dictionary

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
# Access the elements inside
# print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])