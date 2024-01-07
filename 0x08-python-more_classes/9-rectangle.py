#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns: Area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns: Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rectang_1, rectang_2):
        """Returns a rectangle with a greater or equal area.

        Raises:
            TypeError: If either of rectang_1 or rectang_2 is not a Rectangle.
        Args:
            rectang_1 (Rectangle): The first Rectangle.
            rectang_2 (Rectangle): The second Rectangle.
        """
        if not isinstance(rectang_1, Rectangle):
            raise TypeError("rectang_1 must be an instance of Rectangle")
        if not isinstance(rectang_2, Rectangle):
            raise TypeError("rectang_2 must be an instance of Rectangle")
        if rectang_1.area() >= rectang_2.area():
            return (rectang_1)
        return (rectang_2)

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size.

        Args:
            size (int): Size of the square.
        """
        return (cls(size, size))

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns: String representation of the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectang = []
        for i in range(self.__height):
            [rectang.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rectang.append("\n")
        return ("".join(rectang))

    def __repr__(self):
        """Return a string representation that can be used to recreate a new instance."""
        rectang = "Rectangle(" + str(self.__width)
        rectang += ", " + str(self.__height) + ")"
        return (rectang)

    def __del__(self):
        """Print a message when a rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
