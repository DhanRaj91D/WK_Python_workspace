from flask import Flask, request, jsonify
from flask_cors import CORS
import hospitalMAnagment.sqlite_Dbmanager as db
from hospitalMAnagment.patient import patient

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get_handler():
    print("Inside get handler")
    response = jsonify(message='<h1>All patients</h1>' + get_all_patient())
    return response


def get_all_patient():
    con = db.initialize_conn()
    allpatent = con.cursor().execute("SELECT * FROM patients").fetchall()
    print(allpatent[0])
    patientdata = ''

    for patient in allpatent:
        patientdata = patientdata + '<h3>' + str(patient[0]) + " " + \
                      patient[1] + " " + patient[2] + " " + patient[3] + " " + str(patient[4]) + '</h3><br>'

    return patientdata


@app.route('/', methods=['POST'])
# @cross_origin()
def post_handler():
    req_data = request.get_json()
    write_to_db(req_data)
    return 'Data sent successfully'


def write_to_db(req_data):
    print(req_data)
    conn = db.initialize_conn()
    patient_id, firstName, lastName, gender, age = req_data.values()
    db.insert_patient_from_flask(conn, patient_id, firstName, lastName, gender, age)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
