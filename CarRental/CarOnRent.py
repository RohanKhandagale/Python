class CarRental:
    def __init__(self):
        self.cars = {
            "Toyota Corolla": True,
            "Honda Civic": True,
            "Ford Focus": True,
            "Chevrolet Malibu": True
        }

    def show_available_cars(self):
        print("\nAvailable Cars:")
        for car, available in self.cars.items():
            if available:
                print(f"{car} is available.")

    def rent_car(self):
        car_choice = input("\nEnter the car you want to rent (e.g., Toyota Corolla): ").title()
        if car_choice in self.cars and self.cars[car_choice]:
            self.cars[car_choice] = False
            print(f"{car_choice} has been rented. Enjoy your drive!")
        elif car_choice in self.cars:
            print(f"Sorry, {car_choice} is already rented.")
        else:
            print("Invalid car name. Please try again.")

    def return_car(self):
        car_choice = input("\nEnter the car you want to return (e.g., Toyota Corolla): ").title()
        if car_choice in self.cars and not self.cars[car_choice]:
            self.cars[car_choice] = True
            print(f"{car_choice} has been returned. Thank you!")
        elif car_choice in self.cars:
            print(f"{car_choice} was not rented. Cannot return it.")
        else:
            print("Invalid car name. Please try again.")

# Run the Car Rental System
car_rental = CarRental()
car_rental.show_available_cars()
car_rental.rent_car()
car_rental.return_car()
