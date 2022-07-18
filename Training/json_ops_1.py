import json


def show_main_menu():
    print("Choose 1 for Patient menu")
    print('Choose 2 for Appointment menu')
    choice = int(input())
    match choice:
        case 1:
            show_patient_menu()
        case 2:
            show_Appointment_menu()


def show_patient_menu():
    print('choose 1 to add a new Patient')
    print('choose 2 to update an existing patient')
    print('choose 3 to delete an existing patient')
    choice = int(input())
    match choice:
        case 1:
            patient_data = load_data()
            add_patient(patient_data)
            save_data(patient_data)

        case 2:
            edit_patient()
        case 3:
            delete_patient()
        case default:
            print("Incorrect input")



def show_Appointment_menu():
    pass



def add_patient(pdata):
    pass


def delete_patient():
    pdata = load_data()
    display_patient_data(pdata)
    pid = int(input(f'Enter the ID of patient to be deleted: '))
    confirmation = input(f"are you sure you want to delete the info of patient with ID {pid} (yes/ no) ?")
    if confirmation == "yes":
        print("delete")


def display_patient_data(pdata):
    plist = pdata["patients_list"]
    for p in plist:
        print(f"patient Id :{p['patient_id']}")
        print(f"patient Name : {p['firstName']}")


def edit_patient():
    pdata = load_data()
    display_patient_data(pdata)
    pid = int(input(f'Enter the ID of patient to be edited: '))
    confirmation = input(f"are you sure you want to edit the info of patient with ID {pid} (yes/ no) ?")
    if confirmation == "yes":
        update_data(pid, input("enter name:"), pdata)
        save_data(pdata)
        print("edited successfully")


def load_data() -> dict:
    with open('Resources/patient_data.json', 'r') as patient_data_file:
        pdata = json.load(patient_data_file)
        return pdata


def update_data(id, name, pdata):
    for patient in pdata["patients_list"]:
        if patient["patient_id"] == id:
            patient["firstName"] = name


def save_data(pdata):
    with open('Resources/patient_data.json', 'w') as patient_data_file:
        json.dump(pdata, patient_data_file, indent=4)


# patient_data = load_data()
# print(patient_data)
# update_data(2, "Dhanraj", patient_data)
# print(patient_data)
# save_data(patient_data)

# delete_patient()
# edit_patient()

show_main_menu()
