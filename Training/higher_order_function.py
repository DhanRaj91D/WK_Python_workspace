patient_dobs = ['21-02-1981', '03-02-2006', '12-01-1950']
curr_yr = 2022


def get_yob(dobs):
    patient_yobs = []
    for dob in dobs:
        patient_yobs.append(dob.split('-')[2])
    return patient_yobs


def get_ages(yobs):
    ages = []
    for yr in yobs:
        ages.append(curr_yr - int(yr))
    return ages


def get_patient_status(get_yob, get_ages, dobs):
    is_mejor = []
    ages = get_ages(get_yob(dobs))
    for age in ages:
        if age >= 18:
            is_mejor.append(age)
        return is_mejor


print(get_patient_status(get_yob, get_ages, patient_dobs))
