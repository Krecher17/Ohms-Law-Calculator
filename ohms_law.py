"""Ohm's law calculator: find voltage, current, resistance or power."""


def voltage(current, resistance):
    """V = I * R"""
    return current * resistance


def current(voltage, resistance):
    """I = V / R"""
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance


def resistance(voltage, current):
    """R = V / I"""
    if current == 0:
        raise ValueError("Current cannot be zero.")
    return voltage / current


def power(voltage, current):
    """P = V * I"""
    return voltage * current


def ask_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def main():
    print("Ohm's Law Calculator")
    print("1. Voltage (V)")
    print("2. Current (A)")
    print("3. Resistance (ohm)")
    print("4. Power (W)")
    choice = input("What do you want to find? (1-4): ").strip()

    try:
        if choice == "1":
            i = ask_number("Current in amperes: ")
            r = ask_number("Resistance in ohms: ")
            print(f"Voltage = {voltage(i, r):.2f} V")
        elif choice == "2":
            v = ask_number("Voltage in volts: ")
            r = ask_number("Resistance in ohms: ")
            print(f"Current = {current(v, r):.2f} A")
        elif choice == "3":
            v = ask_number("Voltage in volts: ")
            i = ask_number("Current in amperes: ")
            print(f"Resistance = {resistance(v, i):.2f} ohm")
        elif choice == "4":
            v = ask_number("Voltage in volts: ")
            i = ask_number("Current in amperes: ")
            print(f"Power = {power(v, i):.2f} W")
        else:
            print("Please choose 1, 2, 3 or 4.")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
