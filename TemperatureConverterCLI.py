""" Temperature Conversion Program
 Written by Ryan Cannon
 4/25/2022 4:39 P.M.

 Update 5/1/2022 2:42 A.M. 1. Added input() functions after the print statements in the main function so that the
 program doesn't automatically close when the program is executed outside an IDE.

 2. Made some adjustments to the options in the main function for user convenience

 3. Update 9/11/2022 12:02 A.M.(Or 0:02): Did some code restructuring as well as added comments to my code(Which I should have done in the first place) for maintenance and future analyzing purposes

 4. Update 10/9/2022 3:15 P.M. (or 15:15): Added some error checking as well as have the program convert
    any uppercase prompts to lower case for convenience. Also gave users the option of continuing or exiting
     the program
 5. Update 10/9/2022 8:42 P.M. (or 20:42): Modified the option section for the temperature and exitorcontinue
    to accept the full words such as yes or no, Celsius or Fahrenheit to be accepted in the prompts
    if the user wishes to type those instead
 6. Update 10/9/2022 10:45 P.M. (or 22:45): Added a try error exception to the prompts asking the user to enter the temperature
    so that the program wouldn't crash and exit if they entered a string value instead of a number
 7. Update 10/18/2022 11:29 P.M. (or 23:29) : It turns there is another temperature unit that I didn't know about before.
    After looking at the Google temperature converter, it turns out Kelvin is actually a thing. At first, I wasn't sure
    I was going to implement it into my temp conversion program since it would require rewriting quite a bit of my
    program and not many people use it. However, after one of my uncle's mentioned it after looking at my program
    and the fact that I could use this program as a template for other conversion programs such as a speed converter
    and a currency converter, I've decided to go ahead and implement Kelvin into my program.

 8. Update 1/22/2023 8:11 P.M. (or 20:11) : Fixed some errors in the program and added the features from the final home version
    into the pro edition."""




# Make sure the user enters a number when asked for the temperature
def ExitorContinue():
    print("Do you want to convert again?")
    # Added the .lower() function so that if the user types the letter in uppercase, the program will accept it
    choice = input("Enter y to continue \nEnter n to exit: ").lower()
    if (choice == "y") or (choice == "yes"):
        main()
    elif (choice == "n") or (choice == "no"):
        quit()
    else:
        # If the user enters something else other than what was asked of them to enter,
        # give them this error message then go back to the start of the prompt.
        print("Invalid option")
        ExitorContinue()


def convertTemperature(option):
    # Convert from Fahrenheit to Celsius
    if (option == "1"):
        try:
            userTemperature = float(input("Enter Temperature in Fahrenheit: "))
            temperature = (userTemperature - 32) * 5 / 9
            temperatureUnit = "Celsius"
            unitSymbol = "°C"
            return temperature, temperatureUnit, unitSymbol
        except:
            print("Error: You must enter a number and not enter anything with letters")
            main()
    # Convert from Celsius to Fahrenheit
    elif (option == "2"):
        try:
            userTemperature = float(input("Enter Temperature in Celsius: "))
            temperature = (userTemperature * 9 / 5) + 32
            temperatureUnit = "Fahrenheit"
            unitSymbol = "°F"
            return temperature, temperatureUnit, unitSymbol
        except:
            print("Error: You must enter a number and not enter anything with letters")
            main()
    # Convert from Celsius to Kelvin
    elif (option == "3"):
        try:
            userTemperature = float(input("Enter Temperature in Celsius: "))
            temperature = (userTemperature + 273.15)
            temperatureUnit = "Kelvin"
            unitSymbol = "K"
            return temperature, temperatureUnit, unitSymbol
        except:
            print("Error: You must enter a number and not enter anything with letters")
            main()
    # Convert from Kelvin to Celsius
    elif (option == "4"):
        try:
            userTemperature = float(input("Enter Temperature in Kelvin: "))
            temperature = (userTemperature - 273.15)
            temperatureUnit = "Celsius"
            unitSymbol = "°C"
            return temperature, temperatureUnit, unitSymbol
        except:
            print("Error: You must enter a number and not enter anything with letters")
            main()

    # Convert from Fahrenheit to Kelvin
    elif (option == "5"):
        try:
            userTemperature = float(input("Enter Temperature in Fahrenheit: "))
            temperature = ((userTemperature - 32) * (5 / 9) + 273.15)
            temperatureUnit = "Kelvin"
            unitSymbol = "K"
            return temperature, temperatureUnit, unitSymbol
        except:
            print("Error: You must enter a number and not enter anything with letters")
            main()
    # Convert from Kelvin to Fahrenheit
    elif (option == "6"):
        try:
            userTemperature = float(input("Enter Temperature in Kelvin: "))
            temperature = ((userTemperature - 273.15) * 9 / 5 + 32)
            temperatureUnit = "Fahrenheit"
            unitSymbol = "°F"
            return temperature, temperatureUnit, unitSymbol
        except:
            print("Error: You must enter a number and not enter anything with letters")
            main()
    # Exit the program
    elif (option == "exit") or (option == "Exit"):
        exit()

    elif option == "about":
        print("Temperature Converter (Home Edition) \nWritten by Ryan Mitchell Cannon \nusing PyCharm 2022.2.2 Community Edition \nin the year of 2022")
        input("Press enter to continue")
        main()

    # Display Error if user enters a non-valid option
    else:
        print("Invalid option")
        main()



def main():
    option = input("1. Convert from Fahrenheit to Celsius \n2. Convert from Celsius to Fahrenheit \n3. Convert from Celsius to Kelvin"
                   "\n4. Convert from Kelvin to Celsius\n5. Convert from Fahrenheit to Kelvin"
                   "\n6. Convert from Kelvin to Fahrenheit: ")
    temperature, temperatureUnit, unitSymbol = convertTemperature(option)
    print(f"The temperature in {temperatureUnit} is:", temperature, unitSymbol)
    ExitorContinue()


main()
