#tuples are one of the data type in python
#they are ordered and unchangeable
#u cant update delete remove inssert in tuples
#written in  normal or circle round brackets






fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#loop 
thistuple = ("bmw","audi","mercedes","lamborghini")
for x in thistuple:
 print(x)

 #####################
 thiscars = ("tata","maruti","mahindra")
 for i in range(len(thiscars)):
     print(thiscars[2])

#join tuples
tuple1 = ("john","tripleh","batista")
tuple2  = (2,4,5)

tuple3 = tuple1+tuple2
print(tuple3)

#multiply tuples
fruits = ("apple","banna","cherry")
mytuple = fruits*2
print(mytuple)