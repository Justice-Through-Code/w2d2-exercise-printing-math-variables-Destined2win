
def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
     celsius_100 = (100 - 32) * 5/9
     print(celsius_100)

    # Is the resulting temperature you get an integer or float? float
    # Print 'float' if it is a float or 'int' if it is an int
     if isinstance(celsius_100, float):
         print('float')
         
    # How do you know? Write a comment below your code explaining how you know which it is
    # After I print my variable I am giving an output of 37.7 which is a decimal. All numbers with a decimal are considered float.


convert_100_to_celsius()

def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    fahrenheit = 0
    # Save this to a variable called celsius_0, and use print() to print out the value
    celsius_0 = (fahrenheit - 32) * 5/9
    print(celsius_0)

   
    
convert_0_to_celsius()

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    print((34.2 - 32) * 5/9)
    # Do this one all in one print statement without saving any variables
    


convert_34_2_to_celsius()


# Now, can you convert back?


def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    celsius_temperature = 5
    fahrenheit_temperature = (celsius_temperature * 9/5) + 32
    print(fahrenheit_temperature)

convert_5_to_fahrenheit()

def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
    fahrenheit_temp = 85.1
    celsius_temp = (fahrenheit_temp -32) * 5/9

    if celsius_temp > 30.2:
         print(f"{celsius_temp:.1f} degrees celsius is hotter") 
    else: 
        print("30.2 degrees celsius is hotter")
        
hotter_temp()