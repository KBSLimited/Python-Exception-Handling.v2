# Task 1: Start - Get valid temperature input
def get_temperature_input():
    while True:
        try:
            # Ask the user to enter the temperature in Fahrenheit
            temp_fahrenheit = input("Please enter the temperature in Fahrenheit: ")
            
            # Try converting the input to a float
            temp_fahrenheit = float(temp_fahrenheit)
            
            # Check if the temperature is within a reasonable range
            if temp_fahrenheit < -200 or temp_fahrenheit > 150:
                print("Error: The temperature seems unrealistic. Please enter a valid temperature.")
                continue
            
            return temp_fahrenheit
        
        except ValueError:
            # Handle case where the input is not a number
            print("Error: Invalid input. Please enter a numerical value for temperature.")

# Task 2: Temperature Conversion
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def provide_forecast(temperature_fahrenheit):
    """Provide a simple weather forecast based on the temperature."""
    temperature_celsius = convert_to_celsius(temperature_fahrenheit)
    
    print(f"\nTemperature in Fahrenheit: {temperature_fahrenheit}°F")
    print(f"Temperature in Celsius: {temperature_celsius:.2f}°C")

    # Simple weather forecast based on temperature ranges
    if temperature_fahrenheit <= 32:
        print("It's cold! Consider wearing a jacket or coat.")
    elif 33 <= temperature_fahrenheit <= 60:
        print("It's a bit chilly. A sweater should be enough.")
    elif 61 <= temperature_fahrenheit <= 85:
        print("The weather is mild and comfortable.")
    else:
        print("It's hot! Stay hydrated and avoid the sun during peak hours.")

# Task 3: Main function to run the program
def main():
    # Step 1: Get a valid temperature input from the user
    temperature_fahrenheit = get_temperature_input()
    
    # Step 2: Provide the weather forecast
    provide_forecast(temperature_fahrenheit)

    # Thank the user for using the application
    print("\nThank you for using the Weather Forecast Application!")

if __name__ == "__main__":
    main()