#prompt the user using inpu() built-in function
fahrenheit_str = input('Input fahrenheit: ')

#convert the string to float
fahrenheit = float(fahrenheit_str)

#calculate the celsius temperature
celsius = (fahrenheit - 32)*5/9
celsius = round(celsius, 2)

print(f'Celsius: {celsius}°C')
