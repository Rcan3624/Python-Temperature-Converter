import os              # Open files for Windows
import subprocess, sys # Open files for Linux

# Display the program name and instructions when the program is started. This will not be displayed again while the program is running.
print("Python Temperature Conversion \n Written by Ryan Cannon")
input("Press enter to continue")


# Just a few goodies I added to this program just for kicks
def easterEggs(option):

    # Foreigner - Hot Blooded
    if (option == "hot blooded") or (option == "i'm hot blooded"):
        print("♪ Check it and see ♪")
        temperature = 103  # Set the Fahrenheit temperature to 103
        unitSymbol = "°F"
        print("The Temperature in Fahrenheit is:", temperature, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\hotblooded.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/hotblooded.ogg'])
        input("Press enter to continue")
        main()

    # Foreigner - Cold As Ice
    elif (option == "cold as ice") or (option == "you're as cold as ice"):
        print("♪ You're willing to sacrifice our love ♪")
        temperature = 32 # Set the Fahrenheit temperature to 32
        unitSymbol = "°F"
        print("The Temperature in Fahrenheit is:", temperature, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\coldasice.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/coldasice.ogg'])
        input("Press enter to continue")
        main()

    # Snow Miser from The Year Without a Santa Claus
    elif (option == "snow miser") or (option == "i'm mr white christmas"):
        print("♪ He's Mr White Christmas ♪\n♪ He's Mr Snow ♪")
        temperature = -10 # Set the Fahrenheit temperature to -10
        unitSymbol = "°F"
        print("The Temperature in Fahrenheit is:", temperature, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\snowmiser.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/snowmiser.ogg'])
        input("Press enter to continue")
        main()

    # Heat Miser from The Year Without a Santa Claus
    elif (option == "heat miser") or (option == "i'm mr green christmas"):
        print("♪ He's Mr Green Christmas ♪\n♪ He's Mr Sun ♪")
        temperature = 101 # Set the Fahrenheit temperature to 101
        unitSymbol = "°F"
        print("The Temperature in Fahrenheit is:", temperature, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\heatmiser.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/heatmiser.ogg'])
        input("Press enter to continue")
        main()

    # Mr Freeze from Batman & Robin
    elif (option == "mr freeze") or (option == "winter has come at last"):
        print("The Iceman cometh!")
        temperature = 23 # Set the Fahrenheit temperature to 23
        unitSymbol = "°F"
        print("The Temperature in Fahrenheit is:", temperature, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\mrfreeze.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/mrfreeze.ogg'])
        input("Press enter to continue")
        main()


    # I couldn't help it
    elif (option == "what is the temperature of the sun") or (option == "vegeta, what does the thermometer say about the temperature of the sun?"):
        print("It's over 9000!")
        temperature = 10000 # Set the Fahrenheit temperature to 10,000
        unitSymbol = "°F"
        print("The Temperature in Fahrenheit is:", temperature, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\over9000.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/over9000.ogg'])
        input("Press enter to continue")
        main()

    # Some crappy 90s rapper
    elif (option == "ice ice baby") or (option == "i'm ice ice baby"):
        print("Did you mean: Trash")
        input("Press enter to continue")
        main()

    # If no "special" inputs where typed in, resume normal operations
    else:
        pass


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
            temperature = ((userTemperature-32) * (5/9) + 273.15)
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
            temperature = ((userTemperature-273.15) * 9/5 + 32)
            temperatureUnit = "Fahrenheit"
            unitSymbol = "°F"
            return temperature, temperatureUnit, unitSymbol
        except:
            print("Error: You must enter a number and not enter anything with letters")
            main()
    # Exit the program
    elif (option == "exit") or (option == "quit"):
        exit()
    # Display Error if user enters a non-valid option
    else:
        print("Invalid option")
        main()



def main():
    option = input("1. Convert from Fahrenheit to Celsius \n2. Convert from Celsius to Fahrenheit \n3. Convert from Celsius to Kelvin"
                   "\n4. Convert from Kelvin to Celsius\n5. Convert from Fahrenheit to Kelvin"
                   "\n6. Convert from Kelvin to Fahrenheit: ").lower()
    easterEggs(option)
    temperature, temperatureUnit, unitSymbol = convertTemperature(option)
    print(f"The temperature in {temperatureUnit} is:", temperature, unitSymbol)
    ExitorContinue()


main()
