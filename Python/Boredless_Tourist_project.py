# load in our data
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# grab the index that pertains to the specified destination
def get_destination_index(destination):
    destination_index = 0

    # look through the list and see where that destination is located
    for index in range(len(destinations)):
        if destinations[index] == destination:
            destination_index = index

    return destination_index
# test the above method
print(get_destination_index("Paris, France"))

# get the location of any given traveler
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = [[], [], [], [], []]

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

# add a sample attraction -- passed in a location and an attraction with a description
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)
