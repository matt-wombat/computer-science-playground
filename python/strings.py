a = "Munich"
b = "Frankfurt"
c = "Berlin"

# f-String
print(f"We are doing a road trip from {a} through {b} to {c}")

# Template string
template = "We are doing a road trip from {} through {} to {}"
print(template.format(a, b, c))
# equivalent to:
print("We are doing a road trip from {} through {} to {}".format(a, b, c))