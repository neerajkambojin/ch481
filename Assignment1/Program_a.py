# Program to convert temperature from °F to °C

temperature_in_f = float(input("Give temperature in °F: ")) # To take input in °F

temperature_in_c = (5 / 9) * (temperature_in_f - 32) # Conversion from °F to °C

print("The temperature is", temperature_in_c, "°C") # Output in °C

temperature_in_f = 300

temperature_in_c = (5 / 9) * (temperature_in_f - 32) # Conversion from 300 °F to °C

print('300 °F is equal to', temperature_in_c, '°C') # Printing output
