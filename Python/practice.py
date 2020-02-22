# global variable for the cost of shipping
premium_shipping_cost = 125.00

# returns the cost for ground shipping
def calculate_ground_shipping(weight):
  flat_charge = 20
  total = 0

  if weight <= 2:
    total += 1.50*weight + flat_charge
  elif weight > 2 and weight <= 6:
    total += 3.00*weight + flat_charge
  elif weight > 6 and weight <= 10:
    total += 4.00*weight + flat_charge
  else:
    total += 4.75*weight + flat_charge

  return total

# returns the cost for drone shipping
def calculate_drone_shipping(weight):
  total = 0

  if weight <= 2:
    total += 4.50*weight
  elif weight > 2 and weight <= 6:
    total += 9.00*weight
  elif weight > 6 and weight <= 10:
    total += 12.00*weight
  else:
    total += 14.75*weight
  return total

# test code
print(str(calculate_ground_shipping(8.4)))
print(str(calculate_drone_shipping(1.5)))

# TODO: Tell the user the cheapest way to get their package delivered
# TODO: Create a method to find the cheapest option, given the weight
def get_cheapest_option(weight):
  calculate_ground = calculate_ground_shipping(weight)
  calculate_drone = calculate_drone_shipping(weight)

  # track the lowest value
  current_lowest = 0
  # track the name of the lowest
  current_lowest_name = ""

  # decide which is the cheapest for the given weight
  if calculate_ground < calculate_drone and calculate_ground < premium_shipping_cost:
    current_lowest = calculate_ground
    current_lowest_name = "Ground Shipping"
  elif calculate_drone < premium_shipping_cost:
      current_lowest = calculate_drone
      current_lowest_name = "Drone Shipping"
  else:
      current_lowest = premium_shipping_cost
      current_lowest_name = "Premium Shipping"
  return current_lowest_name, current_lowest

weightOfItem = float(input("Please enter the weight of your item: "))
cheapest_name, cheapest_value = get_cheapest_option(weightOfItem)

print("Your cheapest option is to get " + cheapest_name + " for " + str(cheapest_value) + " dollars.")
