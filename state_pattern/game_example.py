"""
In this example, the State class defines the interface for the concrete state classes NormalState and SelectedState.
The NormalState class draws a white circle on the screen and listens for mouse button down events.
The SelectedState class draws a red circle on the screen and listens for mouse button up events.

The Object class contains a reference to the current state and implements the handle_events and draw methods,
which delegate to the current state's corresponding methods.
The set_state method allows the state to be changed at runtime.

The Pygame code sets up the window, creates an instance of the Object class, and enters the main loop. In the main loop,
events are processed and the object's state is updated accordingly.
The object is then drawn on the screen and the display is updated.

This example demonstrates how the behavior of an object in a computer graphics application can change dynamically
based on user input or other events, without having to change the object's class.
"""

import pygame


class State:
    def handle_events(self, event):
        pass

    def draw(self, screen):
        pass


class NormalState(State):
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button down in normal state")

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (100, 100), 50)


class SelectedState(State):
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse button up in selected state")

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (100, 100), 50)


class Object:
    def __init__(self):
        self._state = NormalState()

    def set_state(self, state):
        self._state = state

    def handle_events(self, event):
        self._state.handle_events(event)

    def draw(self, screen):
        self._state.draw(screen)


# Pygame initialization code
pygame.init()
screen = pygame.display.set_mode((200, 200))

obj = Object()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        obj.handle_events(event)

    screen.fill((0, 0, 0))
    obj.draw(screen)
    pygame.display.update()

pygame.quit()
