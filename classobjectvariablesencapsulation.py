class Car:
    # Class variable it can be used throughout the program
    brand_name = "Bugatti Chiron"

    def __init__(self):
        self.speed = 0
        self.gear = 0                    #These are Instance variables
        self.engine_on = False

    def engineStart(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"{Car.brand_name} engine started.")
        else:
            print("Engine is already running!")

    def engineStop(self):
        if self.engine_on:          #means engine is already on
            self.engine_on = False
            self.speed = 0
            self.gear = 0
            print(f"{Car.brand_name} engine stopped.")
        else:
            print("Engine is already off!")

    def accelerate(self):
        if not self.engine_on:
            print("Start the engine first!")
            return

        if self.speed < 300:
            self.speed += 25
            print(f"Accelerating... Speed is now {self.speed}km/h")
        else:
            print("Max speed reached!(300 km/h)")

    def brake(self):
        if self.speed > 0:
            self.speed -= 25
            print(f"Braking... Speed is now {self.speed}km/h")
        else:
            print("Car is already stopped.")

    def suddenBrake(self):
        self.speed = 0
        print("Sudden brake applied!Car stopped immediately.")

    def changeGear(self):
        if not self.engine_on:
            print("Start the engine first!")
            return

        if self.gear < 5:
            self.gear += 1
            print(f"Gear changed to {self.gear}")
        else:
            print("Already in top gear (5).")

car1 = Car()

car1.engineStart()
car1.changeGear()
car1.accelerate()
car1.accelerate()
car1.changeGear()
car1.accelerate()
car1.brake()
car1.suddenBrake()
car1.engineStop()
car1.engineStop()
car1.brake()
