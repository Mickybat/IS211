def unit_converter():
    fromUnit = input("Please input what type of unit you would like to convert:")
    toUnit = input("Please input to what type of unit you would like to convert to:")
    value = float(input("Please enter the value of the unit:"))

    if fromUnit == "celsius" and toUnit == "kelvin":
        ans = float(value) + 273.15
        print("The value of your conversion", ans)
    elif fromUnit == "celsius" and toUnit == "fahrenheit":
        ans = float(value) * 1.8 + 32
        print("The value of your conversion", ans)
    elif fromUnit == "fahrenheit" and toUnit == "celsius":
        ans = (float(value) - 32) * 5 / 9
        print("The value of your conversion", ans)
    elif fromUnit == "fahrenheit" and toUnit == "kelvin":
        ans = 273.15 + (float(value - 32) * (5 / 9))
        print("The value of your conversion", ans)
    elif fromUnit == "kelvin" and toUnit == "fahrenheit":
        ans = 1.8 * (float(value - 273.15)) + 32
        print("The value of your conversion", ans)
    elif fromUnit == "kelvin" and toUnit == "celsius":
        ans = float(value - 273.15)
        print("The value of your conversion", ans)
    elif fromUnit == "miles" and toUnit == "yards":
        ans = float(value * 1760)
        print("The value of your conversion", ans)
    elif fromUnit == "miles" and toUnit == "meters":
        ans = float(value * 1609.344)
        print("The value of your conversion", ans)
    elif fromUnit == "yards" and toUnit == "miles":
        ans = float(value / 1760)
        print("The value of your conversion", ans)
    elif fromUnit == "yards" and toUnit == "meters":
        ans = float(value * 0.9144)
        print("The value of your conversion", ans)
    elif fromUnit == "meters" and toUnit == "yards":
        ans = float(value * 1.09361)
        print("The value of your conversion", ans)
    elif fromUnit == "meters" and toUnit == "miles":
        ans = float(value * 0.00062137)
        print("The value of your conversion", ans)
    elif fromUnit == "celsius" and toUnit == "celsius":
        ans = float(value)
        print("The value of your conversion", ans)
    elif fromUnit == "fahrenheit" and toUnit == "fahrenheit":
        ans = float(value)
        print("The value of your conversion", ans)
    elif fromUnit == "kelvin" and toUnit == "kelvin":
        ans = float(value)
        print("The value of your conversion", ans)
    elif fromUnit == "yards" and toUnit == "yards":
        ans = float(value)
        print("The value of your conversion", ans)
    elif fromUnit == "miles" and toUnit == "miles":
        ans = float(value)
        print("The value of your conversion", ans)
    elif fromUnit == "meters" and toUnit == "meters":
        ans = float(value)
        print("The value of your conversion", ans)
    else:
        raise Exception(fromUnit + " cannot be converted to " + toUnit)


unit_converter()