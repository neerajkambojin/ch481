import numpy.random

patients_list = []

# Importing patients name file and adding the names to patients list
with open('patients.txt') as patients:
    for patient in patients.readlines():
        patients_list.append(patient.strip())

# Initializing starting time
hours = 10
minutes = '00'
vel = 'am'

# Assigning random patients the timing from 10 am at regular interval of 10 mins and writing the output to txt file
with open('Visit.txt', 'w') as visits:
    visits.write('The schedule for patients appointment is:\n')
    for i in range(20):
        patient = numpy.random.choice(patients_list)
        visits.write(f'{patient} : {hours}:{minutes} {vel}\n')
        patients_list.remove(patient)

        if minutes == 50:
            hours += 1
            minutes = '00'
        else:
            minutes = int(minutes) + 10

        if hours == 12:
            vel = 'pm'
        if f'{hours}:{minutes}' == '13:00':
            hours = 1;
            minutes = '00'
