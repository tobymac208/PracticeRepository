destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    destination_index = 0

    # look through the list and see where that destination is located
    for index in range(len(destinations)):
        if destinations[index] == destination:
            destination_index = index

    return destination_index

print(get_destination_index("Paris, France"))


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = [[], [], [], [], []]

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)

        attractions_for_destination = attractions

        return attractions_for_destination
    except ValueError:
        # simply return
        return
