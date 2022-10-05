import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800 # Size of the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # creating window
pygame.display.set_caption("Solar System Simulation") # text show on title bar

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (40, 122, 184)     # DEFINING COLORS FOR LATER USER
RED = (193, 68, 14)
DARK_GRAY = (116, 123, 129)

FONT = pygame.font.SysFont("comicsans", 16) # font for all planets
FONT1 = pygame.font.SysFont("comicsans", 20) # font for the Sun because color is to be changed

class Planet:  #  create class Planet
    AU = 149.6e6 * 1000 # Astronomical Unit ( For Scale)
    G = 6.67428e-11 # Universal Gravitational Constant
    SCALE  = 250 / AU # 1 AU = 100 pixels
    TIME_STEP = 3600 * 24 # 1 Day = 1 Second in simulation


    def __init__(self, name, x, y, radius, color, mass): # initialize planets
        self.name = name
        self.x = x # x position
        self.y = y # y position
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = [] # All the points a planet goes through while orbiting (List of tuples)
        self.sun = False # if sun is defined it will be set to True
        self.distance_to_sun = 0 # Distance of current planet from the sun

        self.x_vel = 0 # velocity in x - axis
        self.y_vel = 0 # velocity in y - axis

    def update_position(self, planets): # for moving planets
        total_fx = 0 # intitilize total force in x axis
        total_fy = 0 # intitilize total force in y axis
        for planet in planets: # list planets
            if self == planet: # If planet is itself then skip because its distance and attraction from itself is zero
                continue

            fx, fy = self.attraction(planet) # x and y force of every other planet on given planet
            total_fx += fx # total force in x axis from every other planet
            total_fy += fy # total force in y axis from every other planet

        self.x_vel += total_fx / self.mass * self.TIME_STEP # calculate x velocity using F = ma
        self.y_vel += total_fy / self.mass * self.TIME_STEP # calculate y velocity using F = ma

        self.x += self.x_vel * self.TIME_STEP   # using velocity calculate displacement
        self.y += self.y_vel * self.TIME_STEP
        self.orbit.append((self.x, self.y)) # append to orbit

    def draw(self, win): # draw in window
        x = self.x * self.SCALE + WIDTH / 2    # off set to centre
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2   # same offset as planets
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
            pygame.draw.lines(win, self.color, False, updated_points, 2) # draw line on updated points on each iteration

        pygame.draw.circle(win, self.color, (x, y), self.radius) # draw planets

        text = FONT.render("SOLAR SYSTEM SIMULATION", 1, WHITE)
        win.blit(text, (0,0))

        if not self.sun: # if it is not sun
            distance_text = FONT.render(f"{round(self.distance_to_sun / 1000, 1)}KM({self.name})", 1, WHITE)  # distance from sun in meters
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2)) # bring text to centre of planet

        else: # if it's sun
            sun_name = FONT1.render("SUN",  1, (0,0,0))
            sun_x = WIDTH / 2   # Exact centre
            sun_y = HEIGHT / 2
            win.blit(sun_name, (sun_x - sun_name.get_width() / 2, sun_y - sun_name.get_height() / 2)) # bring text to centre of SUN

    def attraction(self, other): # attraction of current planet from other planet
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2) # calculate distance from self to other planet
        if other.sun:
            self.distance_to_sun = distance # If other is sun then save it as distance from sun as defined in Planet class

        force = self.G * self.mass * other.mass / distance ** 2 # calculate force
        theta = math.atan2(distance_y, distance_x) # calculate angle
        force_x = math.cos(theta) * force  # x component of force
        force_y = math.sin(theta) * force # y component of force

        return force_x, force_y # return x and y components of force


def main():

    run = True
    clock = pygame.time.Clock() # to synchronise clock for a constant frame rate

    sun = Planet("Sun", 0, 0, 30, YELLOW, 1.98892 * 10 ** 30)    # mass in KGs
    sun.sun = True

    earth = Planet("Earth", -1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)
    earth.y_vel = 29.783 * 1000
                                                                                # defining all planets and their intial y velocity to get them moving
    mars = Planet("Mars", -1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet("Mercury", 0.387 * Planet.AU, 0, 8, DARK_GRAY, 0.330 * 10 **24)
    mercury.y_vel = -47.4 * 1000

    venus = Planet("Venus", 0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus] # list of defined planets

    while run:
        clock.tick(60) # maximum frame rate
        WIN.fill((0, 0, 0)) # color of backgroung

        for event in pygame.event.get(): # get all events in pygame
            if event.type == pygame.QUIT: # if user click the "red-cross",
                run = False  # break the loop

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update() # update display so the chages can be seen at run-time

    pygame.quit() # if loop breaks, quit app

main() # call the main function to run the app