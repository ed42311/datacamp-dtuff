def raise_to_power(value1, value2):
  """Raise value1 to the power of value2"""
  return value1 ** value2

raised = raise_to_power(2,3)
print("Raised to power ",raised)

def raise_both(value1, value2):
  """Raise and return value1 by value2 and vice versa"""
  return ((value1 ** value2), (value2 ** value1))

both = raise_both(3,4)
print("both raised: ", both)
