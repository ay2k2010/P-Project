from core.advanced_shapes import *

class PolyShape(AdvancedShape):

     def __init__(self, pos, sides):


         self.square = Rectangle(Point(position.getX() - size, position.getY() - size),
                                Point(position.getX() + size, position.getY() + size))

     def tick_event(self):
         self.polygon.setFill(random.choice(["blue", "red", "green", "yellow", "purple", "teal"]))

     def click_event(self, click_event):
         self.square.move(click_event.getX() - self.square.getCenter().getX(),
                         click_event.getY() - self.square.getCenter().getY())

     def key_event(self, key_event):
          if key_event == "w":
            self.square.move(1, 5)
          elif key_event == "a":
            self.square.move(-5, -5)
          elif key_event == "s":
            self.square.move(1, -5)
          elif key_event == "d":
            self.square.move(5, 5)

     def display(self, window):
         self.square.draw(window)




