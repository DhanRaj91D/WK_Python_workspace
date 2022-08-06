import sqlite3

conn = sqlite3.connect('patient.db')

cursor = conn.cursor()


def initialize_conn():
    try:
        con = sqlite3.connect(r'patient.db')
        return con
    except Exception as e:
        print(e)


def create_table():
    cursor.execute("""CREATE TABLE patients(
                    patient_id integer, 
                    firstname text, 
                    lastname text, 
                    gender text, 
                    age integer
                    )""")


def insert_patient(conn, patient_p):
    with conn:
        cursor.execute("INSERT INTO patients VALUES(:patient_id, :firstname, :lastname, :gender, :age)",
                       {'patient_id': patient_p.patient_id, 'firstname': patient_p.firstName,
                        'lastname': patient_p.lastName,
                        'gender': patient_p.gender, 'age': patient_p.age})


def insert_patient_from_flask(con, patient_id, firstName, lastName, gender, age):
    with con:
        con.cursor().execute("INSERT INTO patients VALUES(:patient_id, :firstname, :lastname, :gender, :age)",
                             {'patient_id': int(patient_id), 'firstname': firstName,
                              'lastname': lastName,
                              'gender': gender, 'age': int(age)})


def get_patient_by_name(name):
    cursor.execute("SELECT * FROM patients WHERE firstname=:firstname", {'firstname': name})
    return cursor.fetchall()


def get_all_patients_from_flask(con):
    con.cursor().execute("SELECT * FROM patients")
    allpatent = cursor.fetchall()
    return allpatent


def get_all_patients():
    cursor.execute("SELECT * FROM patients")
    return cursor.fetchall()


def update_patient_age(p_id, age):
    conn.execute(f"update patients set age={age} where patient_id={p_id}")
    conn.commit()


# "UPDATE patients SET age = age WHERE patient_id = patient_id ",
#                        {'patient_id': patient_id, 'age': age}

def delete_patient(p_id):
    conn.execute('''DELETE FROM patients WHERE patient_id = 3''')


def delete_all_patient():
    with conn:
        cursor.execute("DELETE from patients ")
