#a list of destinations we will use for testing
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]

#a traveler for testing
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#afunction tha takes the city as a parameter and tretrieves the index in the list
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#function that returns the index of the traveler destination in the list destinations
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#code for testing
#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

attractions = [ [] for destination in destinations]

#code for testing
#print(attractions)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return
  
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])

#code for testing
#print(attractions)

#adding more attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#code for testing
#print(attractions)

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction[0]
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction)
  return attractions_with_interest

#code for testing
#la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)

#a function to find the travelers interests in all the cities in the app and retrieve the information
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi "
  interests_string += traveler[0]
  interests_string += ", we think you'll like these places around "
  interests_string += traveler_destination
  interests_string += ": "
  for i in range(len(traveler_attractions)):
    if (traveler_attractions[i] == traveler_attractions[-1]) and (len(traveler_attractions) == 1):  
      interests_string += "the " + traveler_attractions[i] + "."
    elif (traveler_attractions[i] == traveler_attractions[-1]) and (len(traveler_attractions) > 1):  
      interests_string += "and the " + traveler_attractions[i] + "."
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
  return interests_string

#code for testing
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)