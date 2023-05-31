class Sphere:

    def __init__ (self, radius, mass):
        self._radius = radius
        self._mass = mass

    def get_radius(self):
        return self._radius

    def get_mass(self):
        return self._mass

    def get_volume(self):
        import math
        volume = (4 * math.pi * (self._radius ** 3))/3
        return round(volume, 5)

    def get_surface_area(self):
        import math
        area = 4 * math.pi * (self._radius ** 2)
        return round(area, 5)

    def get_density(self):
        import math
        density = self._mass/((4 * math.pi * (self._radius ** 3))/3)
        return round(density, 5)





ball = Sphere(2, 50)

print(ball.get_density())
