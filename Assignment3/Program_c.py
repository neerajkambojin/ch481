# Cars

cars = {'1':12,'2':11,'3':7,'4':6,'5':14.5,'6':13,'7':9.5,'8':8,'9':12.5,'10':6.5} # Making dictionary of cars

#Updating car prices according to discounts
updated = {}
for car in cars:
    if cars[car] < 10:
        updated[car] = cars[car]*0.9
    else:
        updated[car] = cars[car] * 0.8

# Filtering for affordable options
amay_money = 11
affordable = {}

#Applying discounts
for key in updated:
    if updated[key] <= 11:
        affordable[key] = updated[key]

max_possible = max(affordable.values()) # Getting highest priced car under affordable options

for car_number in affordable:
    if affordable[car_number] == max_possible: # Getting car number of the highest affordable car
        break

#Printing output
print(f'The car with the highest price which Amay can buy under Rs. 11 lakhs is {car_number} at Rs. {max_possible} '
      f'(Original price : Rs. {cars[car_number]} lakh).\n')
print('Car Number : Price(In lakhs)')
for car in affordable:
    print(f'     {car}    :   {affordable[car]}')
print(f'Total options: {len(affordable)}')

# Writing output to file
with open('cars.txt', 'w') as file:
    file.write(f'The car with the highest price which Amay can buy under Rs. 11 lakhs is {car_number} at Rs. {max_possible} '
      f'(Original price : Rs. {cars[car_number]} lakh).\n')
    file.write('Amay has the following options under Rs. 11 lakh:\n')
    file.write('Car Number : Price(In lakhs)\n')
    for car in affordable:
        file.write(f'     {car}    :   {affordable[car]}\n')
    file.write(f'Total options: {len(affordable)}')