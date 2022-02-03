import numpy.random

patients_list = []

with open('patients.txt') as patients:
    for patient in patients.readlines():
        patients_list.append(patient.strip())

print(patients_list)
hours = 10
minutes = '00'
vel = 'am'

with open('Visit.txt', 'w') as visits:

    for i in range(20):
        patient = numpy.random.choice(patients_list)
        visits.write(f'{patient} : {hours}:{minutes} {vel}\n')
        patients_list.remove(patient)

        if minutes == 50:
            hours+= 1
            minutes = '00'
        else:
            minutes = int(minutes) +10

        if hours == 12:
            vel = 'pm'

print(patients_list)