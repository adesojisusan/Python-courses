
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
}, 
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(countries_visted, no_of_countries, cities_of_countries):
  new_countries={}
  new_countries["coutry"]=countries_visted
  new_countries["number"]=no_of_countries
  new_countries["numbers"]=cities_of_countries
  travel_log.append(new_countries)

   


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)



