# Base class Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def charge(self, hours):
        self.battery_life += hours * 10
        print(f"Charged for {hours} hours. Battery life is now {self.battery_life} hours.")

# Inheritance: GamingSmartphone inherits Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, gpu_power):
        super().__init__(brand, model, battery_life)
        self.gpu_power = gpu_power  # e.g., 'High', 'Medium', 'Low'

    def play_game(self, game_name):
        print(f"Playing {game_name} with {self.gpu_power} GPU on {self.brand} {self.model}")

    # Encapsulation: private method (conventionally)
    def __optimize_performance(self):
        print("Optimizing performance for gaming...")

    def start_gaming_session(self, game_name):
        self.__optimize_performance()
        self.play_game(game_name)

# Testing the classes
phone = Smartphone("Apple", "iPhone 14", 20)
phone.make_call("123-456-7890")
phone.charge(2)

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 15, "High")
gaming_phone.start_gaming_session("Call of Duty")
