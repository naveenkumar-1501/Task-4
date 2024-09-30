class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.on_off_status = False
        self.volume = 50
    def increase_volume(self):
        self.volume = min(self.volume + 5, 100)
    def decrease_volume(self):
        self.volume = max(self.volume - 5, 0)
    def set_channel(self, channel):
        self.channel = max(1, min(channel, 50))
    def reset_tv(self):
        self.channel = 1
        self.volume = 50
    def get_status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
    def display_details(self):
        return f"LED TV ({self.brand}, {self.inches} inches):\n" \
               f"Screen thickness: {self.screen_thickness}\n" \
               f"Energy usage: {self.energy_usage}\n" \
               f"Lifespan: {self.lifespan} years\n" \
               f"Refresh rate: {self.refresh_rate} Hz"

class PlasmaTV(TV):
    def __init__(self, brand, price, inches, viewing_angle, backlight, lifespan):
        super().__init__(brand, price, inches)
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.lifespan = lifespan
    def display_details(self):
        return f"Plasma TV ({self.brand}, {self.inches} inches):\n" \
               f"Viewing angle: {self.viewing_angle}\n" \
               f"Backlight: {self.backlight}\n" \
               f"Lifespan: {self.lifespan} years"
my_tv = TV(brand="Sony", price=1000, inches=55)
my_tv.increase_volume()
my_tv.set_channel(8)
print(my_tv.get_status())
my_led_tv = LedTV(brand="Samsung", price=1500, inches=65, screen_thickness="Slim", energy_usage="Low", lifespan=5, refresh_rate=120)
print(my_led_tv.display_details())
my_plasma_tv = PlasmaTV(brand="LG", price=1200, inches=60, viewing_angle="180 degrees", backlight="Full array", lifespan=7)
print(my_plasma_tv.display_details())
