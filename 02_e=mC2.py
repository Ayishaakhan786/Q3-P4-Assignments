C: int = 299792458  # The speed of light in m/s

def main():
    while True:
        try:
            mass_in_kg: float = float(input("Enter kilos of mass: "))
            
            # Calculate energy
            energy_in_joules: float = mass_in_kg * (C ** 2)
            
            # Display work to the user
            print("e = m * C^2...")
            print(f"m = {mass_in_kg} kg")
            print(f"C = {C} m/s")
            
            print(f"{energy_in_joules} joules of energy!\n")
        except ValueError:
            print("Invalid input! Please enter a numerical value for mass.")

# Calling the main function if the script is run directly
if __name__ == '__main__':
    main()