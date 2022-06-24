def print_details(name, age, profession):
    print(f"{name} is {age} years old.{name} is a {profession}")


# calling function with positional arrguement
# print_details("Jhon", 50)

# calling function in keyword arrgument
# print_details(age=50, name="Jhon")

print_details("Jhon", 50, profession="Teacher")


def print_det_again(name, age=20, profession="student"):
    print(f"{name} is {age} years old.{name} is a {profession}")


print_det_again("Dhanraj")

# we can also modify the default values
print_det_again("Dhanraj", 24, "developer")


# function with variable number of arguments
def print_var_params(*params):
    print(params)


print_var_params(1, 2, 3, 4, 5, 6)
