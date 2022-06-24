mylist = ["python", "java", "go", "HTML", "Node", "c Sharp", "Ruby"]

print(mylist)
print(len(mylist))  # returns length of list
print(mylist[1])  # returns item at specified index
print(mylist[-1], mylist[-2])  # negative indexing returns item from backside of list
print(mylist[2:5])  # returns item from that range start from 2 but 5th element will not be included
print(mylist[:5])  # returns item from beginning to the less than range provided not include 4
print(mylist[2:])  # returns item from 2nd index to end of list

# you can change item from given index

mylist[3] = "javaScript"
print(mylist)

# this can also be done using range

mylist[1:3] = ["c", "cpp"]
print(mylist)

# insert item at specific index

mylist.insert(3, "PHP")
print(mylist)

# append

mylist.append("javascript")
print(mylist)

# Extend list we can concat two list by using extend function
# by using this method we can append any iterable not only list but tuple set etc also

mylist2 = ["Bootstrap", "sql"]
mylist.extend(mylist2)
print(mylist)
mytuple = ("jquery", "ajax")
mylist.extend(mytuple)
print(mylist)
print(mylist2)

# remove specified item

mylist.remove("PHP")
print(mylist)

# remove specified index
# if not specified index pop removes last item

mylist.pop(4)
print(mylist)
mylist.pop()
print(mylist)

# del keyword also removes specified index
# del keyword also delete the total list

del mylist[3]
print(mylist)

# clear method empty the list means list still remain, but it has no contain
# mylist.clear()
# print(mylist)

# Looping over list

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

# Whileloop

i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

# shorthand for loop to print list
[print(x) for x in mylist]

# sorting list
# default ascending
# default sensitive sorts all capital letter before lower case letter
mylist.sort()
print(mylist)

# Reverse

mylist.sort(reverse=True)
print(mylist)


# customize sort function

def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

mylist.sort(key = str.lower)
print(mylist)


# Reverse

mylist.reverse()
print(mylist)


# copy list

copylist= mylist.copy()
print(copylist)

copylist = list(mylist)

print(copylist)


# join list

joinlist = mylist + copylist

print(mylist)

# append method

for x in mylist:
    copylist.append(x)

print(copylist)

# using extend method

copylist.extend(mylist)
print(copylist)