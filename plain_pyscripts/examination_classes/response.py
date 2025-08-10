from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Shape is an abstract class, and therefore must inherit from ABC (Abstract Base Class)
    """
    @abstractmethod
    def perimeter(self, rounding: int = 0) -> float:
        """
        Calculate the perimeter of this shape, which can be rounded to a certain number of decimal digits.

        Parameters:
            rounding: The number of rounded decimal digits. If rounding <= 0, the returned value will not be rounded.

        Returns:
            the perimeter of this shape, rounded or not.
        """
        pass

    @abstractmethod
    def area(self, rounding: int = 0) -> float:
        """
        Calculate the area of this shape, which can be rounded to a certain number of decimal digits.

        Parameters:
            rounding: The number of rounded decimal digits. If rounding <= 0, the returned value will not be rounded.

        Returns:
            the perimeter of this shape, rounded or not.
        """
        pass

class Circle(Shape):
    """
    A Circle is a Shape.
    """

    def __init__(self, radius: int | float = 5):
        """
        Instantiates a circle with a certain radius.

        Parameters:
            radius: The radius of this circle, set to 5 units by default
        """
        assert type(radius) == int or type(radius) == float, f'radius ({radius}) is not an int nor float'
        self.radius = radius
    
    def get_radius(self, rounding: int = 0):
        """
        This getter method returns the radius of this circle, which can be rounded to a certain number of decimal digits.

        Parameters:
            rounding: The number of rounded decimal digits. If rounding <= 0, the returned value will not be rounded.

        Returns:
            the radius of this circle
        """
        assert type(rounding) == int, f'rounding ({rounding}) is not an int'
        # If rounding <= 0, do not round.
        if rounding <= 0:
            return self.radius
        return round(self.radius, rounding) # Round to {rounding} decimal digits


    def perimeter(self, rounding: int = 0) -> float: # Circumference
        """
        Calculate the perimeter, or more properly the circumference, of this shape, which can be
        rounded to a certain number of decimal digits.

        Parameters:
            rounding: The number of rounded decimal digits. If rounding <= 0, the returned value will not be rounded.

        Returns:
            the perimeter of this shape, rounded or not.
        """
        assert type(rounding) == int, f'rounding ({rounding}) is not an int'
        diameter = self.radius * 2
        perimeter = diameter * math.pi
        # If rounding <= 0, do not round.
        if rounding <= 0:
            return perimeter
        return round(perimeter, rounding) # Round to {rounding} decimal digits
    
    def area(self, rounding: int = 0) -> float:
        assert type(rounding) == int, f'rounding ({rounding}) is not an int'
        area = (self.radius ** 2) * math.pi
        # If rounding <= 0, do not round.
        if rounding <= 0:
            return area
        return round(area, rounding) # Round to {rounding} decimal digits
    
    def set_radius(self, radius: int | float):
        """
        Sets the radius of this circle.

        Parameters:
            radius: The radius of this circle
        """
        assert type(radius) == int or type(radius) == float, f'radius ({radius}) is not an int nor float'
        self.radius = radius
    
class Rectangle(Shape):
    """
    A Rectangle is a Shape.
    """
    def __init__(self, width: int | float, height: int | float):
        """
        Instantiates a rectangle with a certain width and height.

        Parameters:
            width: The width of this rectangle
            height: The height of this rectangle
        """
        assert type(width) == int or type(width) == float, f'width {width} is not an int nor a float'
        assert type(height) == int or type(height) == float, f'height {height} is not an int nor a float'
        
        self.width = width
        self.height = height

    def get_width(self, rounding: int = 0):
        """
        This getter method returns the width of this rectangle, which can be rounded to a certain number of decimal digits.

        Parameters:
            rounding: The number of rounded decimal digits. If rounding <= 0, the returned value will not be rounded.

        Returns:
            the width of this rectangle
        """
        assert type(rounding) == int, f'rounding ({rounding}) is not an int'
        # If rounding <= 0, do not round.
        if rounding <= 0:
            return self.width
        return round(self.width, rounding) # Round to {rounding} decimal digits
    
    def get_height(self, rounding: int = 0):
        """
        This getter method returns the height of this rectangle, which can be rounded to a certain number of decimal digits.

        Parameters:
            rounding: The number of rounded decimal digits. If rounding <= 0, the returned value will not be rounded.

        Returns:
            the height of this rectangle
        """
        assert type(rounding) == int, f'rounding ({rounding}) is not an int'
        # If rounding <= 0, do not round.
        if rounding <= 0:
            return self.height
        return round(self.height, rounding) # Round to {rounding} decimal digits

    def perimeter(self, rounding: int = 0) -> float:
        assert type(rounding) == int, f'rounding ({rounding}) is not an int'
        perimeter = (self.width + self.height) * 2
        # If rounding <= 0, do not round.
        if rounding <= 0:
            return perimeter
        return round(perimeter, rounding) # Round to {rounding} decimal digits
    
    def area(self, rounding: int = 0) -> float:
        assert type(rounding) == int, f'rounding ({rounding}) is not an int'
        area = self.width * self.height
        # If rounding <= 0, do not round.
        if rounding <= 0:
            return area
        return round(area, rounding) # Round to {rounding} decimal digits
    
    def set_width(self, width: int | float):
        """
        Sets the width of this rectangle.

        Parameters:
            width: The width of this rectangle
        """
        assert type(width) == int or type(width) == float, f'radius ({width}) is not an int nor float'
        self.width = width
    
    def set_length(self, length: int | float):
        """
        Sets the length of this rectangle.

        Parameters:
            length: The length of this rectangle
        """
        assert type(length) == int or type(length) == float, f'radius ({length}) is not an int nor float'
        self.length = length
    
class Square(Rectangle):
    """
    A Square is a Rectangle, which is also a Shape.
    """
    def __init__(self, side: int | float = 5):
        """
        Instantiates a square with a certain side length.

        Parameters:
            side: The side length of this square, set to 5 units by default
        """
        assert type(side) == int or type(side) == float, f'side {side} is not an int nor a float'
        super().__init__(side, side)
    
    def get_side(self, rounding: int = 0):
        """
        This getter method returns the side length of this rectangle, which can be rounded to a certain number of decimal digits.

        Parameters:
            rounding: The number of rounded decimal digits. If rounding <= 0, the returned value will not be rounded.

        Returns:
            the side length of this rectangle
        """
        assert type(rounding) == int, f'rounding ({rounding}) is not an int'

        # self.width is used here since self.width == self.height

        # If rounding <= 0, do not round.
        if rounding <= 0:
            return self.width
        return round(self.width, rounding) # Round to {rounding} decimal digits
    
    def set_side(self, side: int | float):
        """
        Sets the side length of this square.

        Parameters:
            width: The side length of this square
        """
        assert type(side) == int or type(side) == float, f'radius ({side}) is not an int nor float'
        self.width = side
        self.length = side

    def set_length(self, length):
        self.set_side(length)

    def set_width(self, width):
        self.set_side(width)