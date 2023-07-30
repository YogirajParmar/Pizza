class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Pizza:
    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        self.toppings.remove(topping)

    def calculate_total_cost(self):
        total_cost = sum(topping.price for topping in self.toppings)
        return total_cost


class PricePredictor:
    def __init__(self, topping_prices):
        self.topping_prices = topping_prices

    def predict_pizza_price(self, selected_toppings):
        total_cost = sum(self.topping_prices[topping] for topping in selected_toppings)
        return total_cost


class PizzaToppingsInput:
    def __init__(self):
        self.toppings = {}

    def add_topping(self, name, price):
        self.toppings[name] = price

    def get_toppings_input(self):
        print("Welcome to the pizza topping selection!")
        print("Please enter the toppings you want to add to your pizza.")
        print("Enter 'done' when you finish adding toppings.")

        while True:
            topping_name = input("Enter topping name: ")
            if topping_name.lower() == "done":
                break

            try:
                topping_price = float(input(f"Enter the price of {topping_name}: "))
                self.add_topping(topping_name, topping_price)
                print(f"{topping_name} added with a price of {topping_price:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid price.")

        print("Toppings selection completed!")

    def get_toppings(self):
        return self.toppings


class PizzaCustomizationApp:
    def __init__(self):
        self.pizza_toppings_input = PizzaToppingsInput()
        self.selected_toppings = {}
        self.price_predictor = None

    def run(self):
        self.pizza_toppings_input.get_toppings_input()
        self.selected_toppings = self.pizza_toppings_input.get_toppings()
        self.price_predictor = PricePredictor(self.selected_toppings)

    def print_selected_toppings(self):
        print("Selected Toppings:")
        for topping, price in self.selected_toppings.items():
            print(f"{topping}: ${price:.2f}")

    def predict_pizza_price(self):
        selected_toppings_list = list(self.selected_toppings.keys())
        predicted_cost = self.price_predictor.predict_pizza_price(selected_toppings_list)
        print("Predicted cost of the pizza:", predicted_cost)


if __name__ == "__main__":
    pizza_app = PizzaCustomizationApp()
    pizza_app.run()
    pizza_app.print_selected_toppings()
    pizza_app.predict_pizza_price()
