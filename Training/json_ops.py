import json


def load_data() -> dict:
    with open('Resources/patient_data.json', 'r') as patient_data_file:
        pdata = json.load(patient_data_file)
        return pdata


def update_data(id, name, pdata):
    for patient in pdata["patients_list"]:
        print(type(patient["patient_id"]))
        if patient["patient_id"] == id:
            patient["firstName"] = name


def save_data(pdata):
    with open('Resources/patient_data.json', 'w') as patient_data_file:
        json.dump(pdata, patient_data_file, indent=4)


patient_data = load_data()
print(patient_data)
update_data(2, "Dhanraj", patient_data)
print(patient_data)
save_data(patient_data)


