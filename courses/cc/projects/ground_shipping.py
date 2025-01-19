weight = float(input("Please enter weight of package: "))

# Ground Shipping
def calc_shipping(weight, price_per_pound, flat_charge):
  return weight * price_per_pound + flat_charge

if weight <= 2:
  price_ground_shipping = calc_shipping(weight, 1.5, 20)
elif weight <= 6:
  price_ground_shipping = calc_shipping(weight, 3, 20)
elif weight <= 10:
  price_ground_shipping = calc_shipping(weight, 4, 20)
else:
  price_ground_shipping = calc_shipping(weight, 4.75, 20)

print("Ground Shipping:         $", price_ground_shipping)

# Ground Premium Shipping
price_premium_ground_shipping = calc_shipping(weight, 0, 125)
print("Ground Shipping Premium: $", price_premium_ground_shipping)

# Drone Shipping
if weight <= 2:
  price_drone_shipping = calc_shipping(weight, 4.5, 0)
elif weight <= 6:
  price_drone_shipping = calc_shipping(weight, 9, 0)
elif weight <= 10:
  price_drone_shipping = calc_shipping(weight, 12, 0)
else:
  price_drone_shipping = calc_shipping(weight, 14.25, 0)

print("Drone Shipping:          $", price_drone_shipping)
