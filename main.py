coffee_prices =[('cappucino', 1.50),
               ('expresso',1.20),
               ('mocha',1.90)]

#problem #1 retrieve the coffee names and price from the above tuple. Make sure it is in a readable format(hint: f strings)

#create a function that iterates through the tuple list above and returns the highest priced coffee only. You probably want to create a function that has argumentstvhh

# for coffee, price in coffee_prices:
#   print(f"{coffee} costs: {price}")
# def Most_expensive(coffee_prices):
#   maximum= max(price) #idk
#   print(f"{maximum} This is the most expensive coffee price")
# Most_expensive(coffee_prices)


def my_most_expensive_coffee(coffee_prices):
  #establish what the highest prices are
  #my most expensive coffee
  highest_price = 0
  my_most_expensive_coffee = ""
  
  for coffee, price in coffee_prices:
    if price > highest_price:
      highest_price = price
      my_most_expensive_coffee = coffee
    else:
      pass
  return (my_most_expensive_coffee, highest_price)
x=my_most_expensive_coffee(coffee_prices)
print(x)