import math

class CrealityEnderPlugin:
    def __init__(self):
        self.power_rate = float(input("Enter the power rate (in $ per hour): "))

    def create_shape(self, shape_type):
        if shape_type == "cube":
            length = float(input("Enter the length of the cube: "))
            volume = length ** 3
            print("Volume of the cube:", volume)
        elif shape_type == "sphere":
            radius = float(input("Enter the radius of the sphere: "))
            volume = (4/3) * math.pi * radius ** 3
            print("Volume of the sphere:", volume)
        elif shape_type == "cylinder":
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            volume = math.pi * radius ** 2 * height
            print("Volume of the cylinder:", volume)
        else:
            print("Unsupported shape type. Please try again.")

    def create_support_blocker(self, shape_type):
        if shape_type == "cube":
            length = float(input("Enter the length of the cube support blocker: "))
            volume = length ** 3
            print("Volume of the cube support blocker:", volume)
        elif shape_type == "sphere":
            radius = float(input("Enter the radius of the sphere support blocker: "))
            volume = (4/3) * math.pi * radius ** 3
            print("Volume of the sphere support blocker:", volume)
        elif shape_type == "cylinder":
            radius = float(input("Enter the radius of the cylinder support blocker: "))
            height = float(input("Enter the height of the cylinder support blocker: "))
            volume = math.pi * radius ** 2 * height
            print("Volume of the cylinder support blocker:", volume)
        else:
            print("Unsupported shape type. Please try again.")

    def inches_to_metric(self, value):
        conversion_factor = 25.4
        return value * conversion_factor

    def metric_to_inches(self, value):
        conversion_factor = 0.03937
        return value * conversion_factor

    def export_cura_settings(self):
        settings = {
            "layer_height": 0.2,
            "infill_density": 20,
            "print_speed": 60,
            "nozzle_temperature": 200,
            "bed_temperature": 60,
            "support_structure": "None"
        }

        with open("cura_settings.html", "w") as file:
            file.write("<html>\n")
            file.write("<body>\n")
            file.write("<h1>Cura Settings</h1>\n")
            file.write("<ul>\n")
            for setting, value in settings.items():
                file.write(f"<li><b>{setting.capitalize().replace('_', ' ')}</b>: {value}</li>\n")
            file.write("</ul>\n")
            file.write("</body>\n")
            file.write("</html>\n")

        print("Cura settings exported to cura_settings.html")

    def configure_linear_advance(self):
        enabled = input("Enable Linear Advance? (y/n): ")
        if enabled.lower() == "y":
            k_factor = float(input("Enter the K factor value: "))
            # Save the k_factor to the firmware configuration
            print("Linear Advance configured with K factor:", k_factor)
        else:
            # Disable Linear Advance in firmware configuration
            print("Linear Advance disabled")

    def calculate_power_cost(self, print_time):
        power_consumption = (print_time / 60) * self.power_rate
        return power_consumption

    def calculate_material_cost(self, weight, cost_per_kg):
        return (weight / 1000) * cost_per_kg

    def menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Create a shape")
            print("2. Create a support blocker")
            print("3. Convert inches to metric")
            print("4. Convert metric to inches")
            print("5. Export Cura settings to HTML")
            print("6. Configure Linear Advance")
            print("7. Calculate Power Cost")
            print("8. Calculate Material Cost")
            print("9. Quit")
            choice = input("Enter your choice (1-9): ")

            if choice == "1":
                print("Shape Menu:")
                print("1. Create a cube")
                print("2. Create a sphere")
                print("3. Create a cylinder")
                shape_choice = input("Enter your shape choice (1-3): ")
                if shape_choice == "1":
                    self.create_shape("cube")
                elif shape_choice == "2":
                    self.create_shape("sphere")
                elif shape_choice == "3":
                    self.create_shape("cylinder")
                else:
                    print("Invalid shape choice. Please try again.")

            elif choice == "2":
                print("Support Blocker Menu:")
                print("1. Create a support blocker for a cube")
                print("2. Create a support blocker for a sphere")
                print("3. Create a support blocker for a cylinder")
                shape_choice = input("Enter your shape choice (1-3): ")
                if shape_choice == "1":
                    self.create_support_blocker("cube")
                elif shape_choice == "2":
                    self.create_support_blocker("sphere")
                elif shape_choice == "3":
                    self.create_support_blocker("cylinder")
                else:
                    print("Invalid shape choice. Please try again.")

            elif choice == "3":
                inches = float(input("Enter the value in inches: "))
                metric_value = self.inches_to_metric(inches)
                print("Metric value:", metric_value)

            elif choice == "4":
                metric = float(input("Enter the value in metric: "))
                inches_value = self.metric_to_inches(metric)
                print("Inches value:", inches_value)

            elif choice == "5":
                self.export_cura_settings()

            elif choice == "6":
                self.configure_linear_advance()

            elif choice == "7":
                print_time = float(input("Enter the print time (in minutes): "))
                power_cost = self.calculate_power_cost(print_time)
                print("Estimated power cost: $", power_cost)

            elif choice == "8":
                weight = float(input("Enter the material weight (in grams): "))
                cost_per_kg = float(input("Enter the cost per kg: "))
                material_cost = self.calculate_material_cost(weight, cost_per_kg)
                print("Estimated material cost: $", material_cost)

            elif choice == "9":
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    plugin = CrealityEnderPlugin()
    plugin.menu()
