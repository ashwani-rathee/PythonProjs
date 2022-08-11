import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2


class Car:
    def __init__(self, x, y, angle=0.0, length=4, max_steering=30, max_acceleration=100.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 20
        self.brake_deceleration = 10
        self.free_deceleration = 2

        self.acceleration = 0.0
        self.steering = 0.0

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Swarm Robots Simulator")
        width = 1080
        height = 840
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "bots/robot_0.png")
        car_image_0 = pygame.image.load(image_path)
        image_path = os.path.join(current_dir, "bots/robot_1.png")
        car_image_1 = pygame.image.load(image_path)
        car_0 = Car(0, 0)
        car_1 = Car(40, 40)
        ppu = 32
        i = 1
        cars = [car_0,car_1]
        print(cars[1].position)
        while not self.exit:

            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                print(cars[i].position)
                if cars[i].velocity.x < 0:
                    cars[i].acceleration = cars[i].brake_deceleration
                else:
                    cars[i].acceleration += 1 * dt
            elif pressed[pygame.K_DOWN]:
                if cars[i].velocity.x > 0:
                    cars[i].acceleration = -cars[i].brake_deceleration
                else:
                    cars[i].acceleration -= 1 * dt
            elif pressed[pygame.K_SPACE]:
                if abs(cars[i].velocity.x) > dt * cars[i].brake_deceleration:
                    cars[i].acceleration = -copysign(cars[i].brake_deceleration, cars[i].velocity.x)
                else:
                    cars[i].acceleration = -cars[i].velocity.x / dt
            else:
                if abs(cars[i].velocity.x) > dt * cars[i].free_deceleration:
                    cars[i].acceleration = -copysign(cars[i].free_deceleration, cars[i].velocity.x)
                else:
                    if dt != 0:
                        cars[i].acceleration = -cars[i].velocity.x / dt
            cars[i].acceleration = max(-cars[i].max_acceleration, min(cars[i].acceleration, cars[i].max_acceleration))

            if pressed[pygame.K_RIGHT]:
                cars[i].steering -= 30 * dt
            elif pressed[pygame.K_LEFT]:
                cars[i].steering += 30 * dt
            else:
                cars[i].steering = 0
            cars[i].steering = max(-cars[i].max_steering, min(cars[i].steering, cars[i].max_steering))

            # Logic
            cars[i].update(dt)

            # Drawing
            self.screen.fill((0, 0, 0))
            rotated = pygame.transform.rotate(car_image_0, cars[i].angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, cars[i].position * ppu - (rect.width / 2, rect.height / 2))
            pygame.display.flip()

            self.clock.tick(self.ticks)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
