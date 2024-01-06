#!/usr/bin/python3

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
        """Prints a message when a rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
