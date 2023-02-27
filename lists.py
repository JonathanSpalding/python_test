#printing lists
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
print(motorcycles[0])
#-1 is last in list. -2 is second to last, etc.
print(motorcycles[-1])

#modifying elements in a list
motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("honda")

motorcycles.insert(0, 'kawasaki')
print(motorcycles)
#deleting items with del statement
del motorcycles[0]

#popping elements
popped_motorcycles = motorcycles.pop()
#printing shows that it popped the last element like popping off of a stack.
print(popped_motorcycles)

#removing items
#you can't remove just by number place. You have to specify the actual element by name. But this is nice if you don't know where it is, then you don't have to run a loop to find it.
motorcycles.remove("yamaha")
print(motorcycles)
#this only removes the first element of this. If there are two yamahas, then it'll only remove the first one.



print(f"The last bike is {motorcycles.pop().title()}.")


#sorting.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#sorted function doesn't change the list, but displays how you want.
print(sorted(cars))
print(cars)

#this is different than where we did (reverse=true) earlier, sort of. This reverse, rather than sorting anti-alphabetical. So you can sort in reverse, or just do in reverse from wherever it was.
cars.reverse()
print(cars)

#length
print(len(cars))
len(motorcycles)











