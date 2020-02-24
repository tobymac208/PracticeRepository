# load in our data
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[], [], [], [], []]

# grab the index that pertains to the specified destination
def get_destination_index(destination):
    destination_index = 0

    # look through the list and see where that destination is located
    for index in range(len(destinations)):
        if destinations[index] == destination:
            destination_index = index

    return destination_index
# test the above method
#print(get_destination_index("Paris, France"))

# get the location of any given traveler
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

# add an attraction to a destination
def add_attraction(destination, attraction):
    try:
        # grab the destination of the attraction
        destination_index = get_destination_index(destination)
        # grab the list from attractions
        attractions_for_destination = attractions[destination_index]
        # we now want to add that attraction to our list
        attractions_for_destination.append(attraction)

        return
    except ValueError:
        # simply return
        return

# add sample attractions -- passed in a location and an attraction with a description
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

# finds a destinatio nthe pertains to a traveler's interests
def find_attractions(destination, interests):
    # find our destination to search our attractions
    destination_index = get_destination_index(destination)
    # we now can grab the attractions in that location
    attractions_in_city = attractions[destination_index]

    # this will be populated if any of our traveler's interests coincide
    # with any of the descriptions from our attraction's list
    attractions_with_interest = []
    attraction_tags = []

    # retrieve all tags
    for possible_attraction in attractions_in_city:
        attraction_tags.append(possible_attraction)
        # check if each interest matches the current possible_attraction
        for interest in interests:
            for attraction_tag in attraction_tags:
                # check the lists in each tag
                for item in attraction_tag[1]:
                    if item == interest:
                        attractions_with_interest.append(attraction_tag[0])

    # give the user the list
    return attractions_with_interest


# practice our above method -- does Los Angeles have an attraction for art?
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)
