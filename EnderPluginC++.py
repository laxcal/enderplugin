#include <iostream>
#include <cmath>
#include <fstream>
#include <string>

using namespace std;

void createShape(string shapeType) {
    if (shapeType == "cube") {
        double length;
        cout << "Enter the length of the cube: ";
        cin >> length;
        double volume = pow(length, 3);
        cout << "Volume of the cube: " << volume << endl;
    } else if (shapeType == "sphere") {
        double radius;
        cout << "Enter the radius of the sphere: ";
        cin >> radius;
        double volume = (4.0 / 3.0) * M_PI * pow(radius, 3);
        cout << "Volume of the sphere: " << volume << endl;
    }
    // Add more shape options here
}

void createSupportBlocker(string shapeType) {
    if (shapeType == "cube") {
        double length;
        cout << "Enter the length of the cube support blocker: ";
        cin >> length;
        double volume = pow(length, 3);
        cout << "Volume of the cube support blocker: " << volume << endl;
    } else if (shapeType == "sphere") {
        double radius;
        cout << "Enter the radius of the sphere support blocker: ";
        cin >> radius;
        double volume = (4.0 / 3.0) * M_PI * pow(radius, 3);
        cout << "Volume of the sphere support blocker: " << volume << endl;
    }
    // Add more shape options here
}

double inchesToMetric(double value) {
    double conversionFactor = 25.4;
    return value * conversionFactor;
}

double metricToInches(double value) {
    double conversionFactor = 0.03937;
    return value * conversionFactor;
}

void exportCuraSettings() {
    ofstream file("cura_settings.html");
    if (file.is_open()) {
        file << "<html>\n";
        file << "<body>\n";
        file << "<h1>Cura Settings</h1>\n";
        file << "<ul>\n";
        file << "<li><b>layer_height</b>: 0.2</li>\n";
        file << "<li><b>infill_density</b>: 20</li>\n";
        file << "<li><b>print_speed</b>: 60</li>\n";
        // Add more Cura settings here
        file << "</ul>\n";
        file << "</body>\n";
        file << "</html>\n";
        file.close();
        cout << "Cura settings exported to cura_settings.html" << endl;
    } else {
        cout << "Unable to export Cura settings." << endl;
    }
}

void configureLinearAdvance() {
    char enableLinearAdvance;
    cout << "Enable Linear Advance? (y/n): ";
    cin >> enableLinearAdvance;
    if (tolower(enableLinearAdvance) == 'y') {
        double kFactor;
        cout << "Enter the K factor value: ";
        cin >> kFactor;
        // Save the kFactor to the firmware configuration
        cout << "Linear Advance configured with K factor: " << kFactor << endl;
    } else {
        // Disable Linear Advance in firmware configuration
        cout << "Linear Advance disabled" << endl;
    }
}

double calculatePowerCost(double printTime, double powerRate) {
    double powerConsumption = (printTime / 60.0) * powerRate;
    return powerConsumption;
}

int main() {
    double powerRate;
    cout << "Enter the power rate (in $ per hour): ";
    cin >> powerRate;

    while (true) {
        cout << "Main Menu:\n";
        cout << "1. Create a shape\n";
        cout << "2. Create a support blocker\n";
        cout << "3. Convert inches to metric\n";
        cout << "4. Convert metric to inches\n";
        cout << "5. Export Cura settings to HTML\n";
        cout << "6. Configure Linear Advance\n";
        cout << "7. Calculate Power Cost\n";
        cout << "8. Quit\n";
        cout << "Enter your choice (1-8): ";

        int choice;
        cin >> choice;

        if (choice == 1) {
            cout << "Shape Menu:\n";
            cout << "1. Create a cube\n";
            cout << "2. Create a sphere\n";
            cout << "Enter your shape choice (1-2): ";

            int shapeChoice;
            cin >> shapeChoice;

            if (shapeChoice == 1) {
                createShape("cube");
            } else if (shapeChoice == 2) {
                createShape("sphere");
            } else {
                cout << "Invalid shape choice. Please try again." << endl;
            }

        } else if (choice == 2) {
            cout << "Support Blocker Menu:\n";
            cout << "1. Create a support blocker for a cube\n";
            cout << "2. Create a support blocker for a sphere\n";
            cout << "Enter your shape choice (1-2): ";

            int shapeChoice;
            cin >> shapeChoice;

            if (shapeChoice == 1) {
                createSupportBlocker("cube");
            } else if (shapeChoice == 2) {
                createSupportBlocker("sphere");
            } else {
                cout << "Invalid shape choice. Please try again." << endl;
            }

        } else if (choice == 3) {
            double inches;
            cout << "Enter the value in inches: ";
            cin >> inches;
            double metricValue = inchesToMetric(inches);
            cout << "Metric value: " << metricValue << endl;

        } else if (choice == 4) {
            double metric;
            cout << "Enter the value in metric: ";
            cin >> metric;
            double inchesValue = metricToInches(metric);
            cout << "Inches value: " << inchesValue << endl;

        } else if (choice == 5) {
            exportCuraSettings();

        } else if (choice == 6) {
            configureLinearAdvance();

        } else if (choice == 7) {
            double printTime;
            cout << "Enter the print time (in minutes): ";
            cin >> printTime;
            double powerCost = calculatePowerCost(printTime, powerRate);
            cout << "Estimated power cost: $" << powerCost << endl;

        } else if (choice == 8) {
            break;

        } else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
