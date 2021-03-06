from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://anupamAdmin:anupamAdmin@cluster0.2c2zj.mongodb.net/student_db")
db = client.get_database("student_db")
records = db.get_collection("student_records")
records.count_documents({})


def findBool(number, date):
    flag = 0
    found = records.find({})

    for i in found:
        # print(i)
        if(i["Enrollment_No"] == number and i["Date"] == date):
            flag = 1
            break
        else:
            flag = 0
            continue

    if flag:
        return True
    return False


def insert(name, number, date, time):
    if findBool(number=number, date=date):
        print("Attendance marked")
    else:
        new_Attendance = {
            "Enrollment_No": number,
            "Name": name,
            "Date": date,
            "Time": time
        }
        records.insert_one(new_Attendance)
        print("New attendance taken")
