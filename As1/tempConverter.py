def celToFah(temperature):
    return 32 + 1.8 * temperature


def FahToCel(temperature):
    return (temperature - 32) / 1.8


def mainProgram():
    scale = int(input("Please select the temperature scale(1 for Celsius and 2 for Fahrenheit): "))
    while scale != 1 and scale != 2:
        print("Input Invalid!")
        scale = int(input("Please select the temperature scale(1 for Celsius and 2 for Fahrenheit): "))
    temperature = float(input("Please enter the temperature: "))
    if scale == 1:
        print("The temperature", temperature, "in Celsius is equivalent to", celToFah(temperature), "in Fahrenheit.")
    else:
        print("The temperature", temperature, "in Fahrenheit is equivalent to", FahToCel(temperature), "in Celsius.")


mainProgram()
