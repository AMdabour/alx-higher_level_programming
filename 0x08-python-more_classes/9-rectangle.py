#!/usr/bin/python3

"""define a class named rectangle"""


class Rectangle:

    """represents a class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize any created instance with width and height"""

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __del__(self):
        """delete an instance"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """a method for retrieving width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter function"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """a method for retrieving height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter function"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of a rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method returns the bigger instance"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size"""

        return (cls(size, size))

    def __str__(self):
        """returns a string representation"""

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            self.output = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    self.output += str(self.print_symbol)
                if i != self.__height - 1:
                    self.output += "\n"
            return self.output

    def __repr__(self):
        """returns a valid python expression as string"""

        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return ret
