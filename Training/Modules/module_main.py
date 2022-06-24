import module1

print(module1.patient)

# importing modules with alias
import module1 as m1

print(m1.patient)

# importing specific thing from module

from module1 import patient

print(patient)

# you can import all but directly use it by name

from module1 import *

print_detail(patient)
