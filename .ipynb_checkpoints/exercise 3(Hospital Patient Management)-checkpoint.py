patient_info = [
    {
        "name": "Thomas",
        "age": 27,
        "temperature": 40,
        "blood_pressure": 120
    },
    {
        "name": "Daniel",
        "age": 33,
        "temperature": 38.3,
        "blood_pressure": 101
    },
    {
        "name": "Kevin",
        "age": 23,
        "temperature": 35.9,
        "blood_pressure": 85
    },
    {
        "name": "David",
        "age": 36,
        "temperature": 36.9,
        "blood_pressure": 125
    },
    {
        "name": "Jack",
        "age": 19,
        "temperature": 36.5,
        "blood_pressure": 110
    }

]



print("======HOSPITAL REPORT======")
total_patients = len(patient_info)
normal_temp = 0
fever_temp = 0
high_bp_case = 0
for patient in patient_info:
    if patient["temperature"] > 39:
        temp_status = "High fever"
    elif patient["temperature"] > 37.6:
        temp_status = "Mild fever"
    elif patient["temperature"] > 36.1:
        temp_status = "Normal"
    else:
        temp_status = "Hypothermia"
    if patient["blood_pressure"] > 120:
        bp_status = "High"
    elif 90 <= patient["blood_pressure"] <=120:
        bp_status = "Normal"
    else:
        bp_status = "Low"

    print(f"Name: {patient['name']}  Temp: {patient['temperature']} | Temp status: {temp_status}")
    print(f"Age: {patient['age']} | BP: {patient['blood_pressure']} |BP status: {bp_status}")
    print("=====================================")

    if temp_status != "Normal":
        fever_temp += 1
    else:
        normal_temp += 1
    if bp_status == "High" :
        high_bp_case += 1
    patient["BP case"] = bp_status
    patient["Fever case"] = temp_status

print(f"Total patients: {total_patients}")
print(f"Normal Temp: {normal_temp}")
print(f"Fever Temp: {fever_temp}")
print(f"High BP Cases: {high_bp_case}")


