import math

def create_shape(shape_type):
    if shape_type == "cube":
        length = float(input("Enter the length of the cube: "))
        volume = length ** 3
        print("Volume of the cube:", volume)
    elif shape_type == "sphere":
        radius = float(input("Enter the radius of the sphere: "))
        volume = (4/3) * math.pi * radius ** 3
        print("Volume of the sphere:", volume)
    # Add more shape options here

def create_support_blocker(shape_type):
    if shape_type == "cube":
        length = float(input("Enter the length of the cube support blocker: "))
        volume = length ** 3
        print("Volume of the cube support blocker:", volume)
    elif shape_type == "sphere":
        radius = float(input("Enter the radius of the sphere support blocker: "))
        volume = (4/3) * math.pi * radius ** 3
        print("Volume of the sphere support blocker:", volume)
    # Add more shape options here

def inches_to_metric(value):
    conversion_factor = 25.4
    return value * conversion_factor

def metric_to_inches(value):
    conversion_factor = 0.03937
    return value * conversion_factor

def export_cura_settings():
    settings = {
        "layer_height": 0.2,
        "infill_density": 20,
        "print_speed": 60,
        # Add more Cura settings here
    }

    with open("cura_settings.html", "w") as file:
        file.write("<html>\n")
        file.write("<body>\n")
        file.write("<h1>Cura Settings</h1>\n")
        file.write("<ul>\n")
        for setting, value in settings.items():
            file.write(f"<li><b>{setting.capitalize()}</b>: {value}</li>\n")
        file.write("</ul>\n")
        file.write("</body>\n")
        file.write("</html>\n")

    print("Cura settings exported to cura_settings.html")

def configure_linear_advance():
    enabled = input("Enable Linear Advance? (y/n): ")
    if enabled.lower() == "y":
        k_factor = float(input("Enter the K factor value: "))
        # Save the k_factor to the firmware configuration
        print("Linear Advance configured with K factor:", k_factor)
    else:
        # Disable Linear Advance in firmware configuration
        print("Linear Advance disabled")

def calculate_power_cost(print_time, power_rate):
    power_consumption = (print_time / 60) * power_rate
    return power_consumption

def main():
    power_rate = float(input("Enter the power rate (in $ per hour): "))
    
    while True:
        print("Main Menu:")
        print("1. Create a shape")
        print("2. Create a support blocker")
        print("3. Convert inches to metric")
        print("4. Convert metric to inches")
        print("5. Export Cura settings to HTML")
        print("6. Configure Linear Advance")
        print("7. Calculate Power Cost")
        print("8. Quit")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            print("Shape Menu:")
            print("1. Create a cube")
            print("2. Create a sphere")
            shape_choice = input("Enter your shape choice (1-2): ")
            if shape_choice == "1":
                create_shape("cube")
            elif shape_choice == "2":
                create_shape("sphere")
            else:
                print("Invalid shape choice. Please try again.")

        elif choice == "2":
            print("Support Blocker Menu:")
            print("1. Create a support blocker for a cube")
            print("2. Create a support blocker for a sphere")
            shape_choice = input("Enter your shape choice (1-2): ")
            if shape_choice == "1":
                create_support_blocker("cube")
            elif shape_choice == "2":
                create_support_blocker("sphere")
            else:
                print("Invalid shape choice. Please try again.")

        elif choice == "3":
            inches = float(input("Enter the value in inches: "))
            metric_value = inches_to_metric(inches)
            print("Metric value:", metric_value)

        elif choice == "4":
            metric = float(input("Enter the value in metric: "))
            inches_value = metric_to_inches(metric)
            print("Inches value:", inches_value)

        elif choice == "5":
            export_cura_settings()

        elif choice == "6":
            configure_linear_advance()

        elif choice == "7":
            print_time = float(input("Enter the print time (in minutes): "))
            power_cost = calculate_power_cost(print_time, power_rate)
            print("Estimated power cost: $", power_cost)

        elif choice == "8":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()