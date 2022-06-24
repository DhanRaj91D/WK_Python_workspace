mystr = "abcdefg hijklmn opqrstuvw xyz"
print(len(mystr))

print("x" in mystr)

# Slicing
# you can slice string using range
print(mystr[12:17])

# modify string

print(mystr.upper())  # lower can convert string to lower case
print(mystr)

# removes any white spaces from beginning or from end
print(mystr.strip())

# replacing

print(mystr.replace("x", "z"))

# split

print(mystr.split(" "))


