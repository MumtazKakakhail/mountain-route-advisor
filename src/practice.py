prices = {"apple":120, "mango":200, "banana":60}

print(prices["mango"])

cheapest = min(prices, key=prices.get)
print(cheapest)