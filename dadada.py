

fruitBasket = ['Apple','Orange','Dragonfruit','Longan','Grapefruit']
#elements of array

vegetableBasket = []


print((fruitBasket)[4])


a = [1,2,3,4,5]

a[3] = 10

print(a)

b = [a, 123]
#squarebrackets always indicate a list

print(b)

c = "Louise sucks!!!!!"

print(c)


dogs = ['Spot', 'Doggo', 'Goldfish']
cats = ['Stripey','Cat', 'Cat2']

pets = dogs + cats
#print((pets[0])[1]) this prints p, dunno why



print(1 == 1)

print(True == True)

print(False == False)


print((9 >= 10) and (1 ==1))
#prints out as False

'''
if temperature > 30:
    print("it's too hot")


else:
    print("it's cold actually")
'''
#just left this here to show what the dots do

temperature = 25
#change this variable

if temperature > 30:
    print("it's too hot")
elif temperature > 20:
    print("a bit toasty")
elif temperature > 10:
    print("Perfect!")
else:
    print("it's cold actually")
