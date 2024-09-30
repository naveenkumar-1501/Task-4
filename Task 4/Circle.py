class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list
    def calculate_area(self):
        """
        Calculates the area of circles with radii from the given list.
        """
        areas = []
        for radius in self.radius_list:
            area = 3.14 * radius ** 2
            areas.append(area)
        return areas
radius_values = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_values)
areas = circle_instance.calculate_area() # Calculate areas
print("Areas of circles:", areas)
