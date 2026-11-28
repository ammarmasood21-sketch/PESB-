prices = [450, 1200, 300, 980, 75]
#Created list

highest = prices[0]        #created highest variable + first value in the list
lowest = prices[0]         #created highest variable + first value in the list

#450 is assumed lowest in the list

for price in prices:    #for loop

    if price > highest:  #tell the highest value by the function
        highest = price

    if price < lowest:   #tell the lowest value 
        lowest = price

print("Highest:", highest)
print("Lowest:", lowest)