mylist = [1, 2, 9, 3, 4, 5, 6, 7, 9, 11]

for x in mylist:
    if x % 2 == 0:
        print("list contain even no")
        break


even_num = []

for num in mylist:
    if num % 2 == 0:
        even_num.append(num)

print(f"even no in list are {even_num}")