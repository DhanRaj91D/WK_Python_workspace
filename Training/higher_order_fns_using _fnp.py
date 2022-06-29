from functools import reduce

patient_dobs = ['21-02-1981', '03-02-2006', '12-01-1950']
curr_yr = 2022


def get_yob(dob):
    return int(dob.split('-')[2])


patient_yobs = list(map(get_yob, patient_dobs))
print(patient_yobs)


def get_age(yob):
    return curr_yr - yob


patient_ages = list(map(get_age, patient_yobs))
print(patient_ages)

# we can ue lambda functions also for same
# Lambda <argument> : <expression>
patient_ages1 = list(map(lambda yob: curr_yr - yob, patient_yobs))
print(patient_ages1)

# we can store lambda function in variable

status = lambda age: age >= 18
print(status(30))


# find adult patient age

adult_patient_age = list(filter(lambda age: age >= 18, patient_ages))
print(adult_patient_age)

# find avg age of patient using reduce
# reduce function is from functools module 
avg_patient_age = reduce(lambda age1, age2: age1 + age2, patient_ages)/len(patient_ages)
print(avg_patient_age)