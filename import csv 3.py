import csv
class Physician:
    __slots__ = ['id', 'name', 'specialty']
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    def get_id(self):
        return self.id 

    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_specialty(self):
        return self.specialty

    def set_specialty(self, specialty):
        self.specialty = specialty

    def __str__(self):
        return " A " + self.specialty + " physician.\n"

    def __repr__(self):
        return "\n Physician:\n  id = " + str(self.id) \
            + "\n  name = " + str(self.name) \
            + "\n  specialty = " + \
            str(self.specialty)

# Question 2

class Patient:
    __slots__ = ['id', 'name', 'gender', 'phone_number']
    def __init__(self, id, name, gender, phone_number):
        self.id = id
        self.name = name
        self.gender = gender
        self.phone_number = phone_number

    def get_emr_id(self):
        return self.id

    def set_emr_id(self, id):
        self.id = id

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender
    
    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def __repr__(self):
        return "\n Patient:\n  id = " + str(self.id) \
            + "\n  name = " + str(self.name) \
            + "\n  gender = " + str(self.gender) \
            + "\n   phone number = " + \
            str(self.phone_number)

# Question 3

class Encounter:
    __slots__ = ['physician', 'patient', 'date', 'disease', 'medication']
    def __init__(self, physician, patient, date, disease, medication):
        self.physician = physician
        self.patient = patient
        self.date = date
        self.disease = disease
        self.medication = medication
    
    def __repr__(self):
        return "\n Encounter:\n  physician = " + str(self.physician) \
            + "\n  patient = " + str(self.patient) \
            + "\n  date = " + str(self.date) \
            + "\n  disease = " + str(self.disease) \
            + "\n  medication = " + \
            str(self.medication)


def csv_read():

    with open('patients.csv','r') as file:
        csv_reader = csv.reader(file)
        for read in csv_reader:
            print(read)

    with open('physicians.csv', 'r') as file1:
        csv_reader1 = csv.reader(file1)
        for read_1 in csv_reader1:
            print(read_1)

def csv_write(write1, write2, write3, write4, write5):
    with open('encounter.csv','w') as file2:
        data = str(write1) + '\n' + str(write2) + '\n' + str(write3) + '\n' + str(write4) + '\n' + str(write5)
        file2.write(data)


def main():

    physician1 = Physician('6527657A', 'Dr. Mina', 'dermatology')
    physician2 = Physician('3498540K', 'Dr. Omar', 'neurology')
    physician3 = Physician('9540801S', 'Dr. Billy', 'cardiology')

    patient1 = Patient('784-1978-0796371-6', 'Hoda', 'Female', 565521178)
    patient2 = Patient('784-2003-0171006-4', 'Mina', 'Male', 529370878)
    patient3 = Patient('784-1989-9677883-2', 'Salma', 'Female', 539209254)
    patient4 = Patient('784-2009-8199449-1', 'Rana', 'Female', 501671336)
    patient5 = Patient('784-1967-3467868-9', 'Moemen', 'Male', 501118600)
    patient6 = Patient('784-1999-0185965-7', 'Zara', 'Female', 520161813)
    patient7 = Patient('784-2004-6788284-4', 'Samir', 'Male', 587299816)
    patient8 = Patient('784-1990-1886091-1', 'Bashar', 'Male', 562533091)
    patient9 = Patient('784-2002-0925631-2', 'Mohammed', 'Male', 540880965)
    patient10 = Patient('784-1987-6532465-5', 'Ali', 'Female', 502959606)

    encounter1 = Encounter(physician1, patient5, "16-9-2021", 'Eczema', 'Cetaphil')
    encounter2 = Encounter(physician3, patient7, "27-8-2021", 'Arrhythmia', 'Amiodarone')
    encounter3 = Encounter(physician2, patient1, "20-3-2021", 'Epilepsy', 'Topiramate')
    encounter4 = Encounter(physician3, patient3, "5-2-2021", 'Coronary artery disease', 'Nitroglycerin')
    encounter5 = Encounter(physician1, patient10, "30-5-2021", 'Rosacea', 'Metronidazole')

    print(physician1)
    print(physician2)
    print(physician3)

    print(patient1)
    print(patient2)
    print(patient3)
    print(patient4)
    print(patient5)
    print(patient6)
    print(patient7)
    print(patient8)
    print(patient9)
    print(patient10)

    print(encounter1)
    print(encounter2)
    print(encounter3)
    print(encounter4)
    print(encounter5)

    csv_read()
    csv_write(encounter1, encounter2, encounter3, encounter4, encounter5)

main()