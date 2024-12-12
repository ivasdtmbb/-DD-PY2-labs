# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

# --------------------------------------------------POINT-------------------------------------------#
class Point:
    """"
    The class describes a point in Cartesian coordinate system.
    """

    def __init__(self, x: Union[int, float], y: Union[int, float]):
        """
        Initialize an instance of the Point class
        :param x: X coordinate
        :param y: Y coordinate

        Examples:
        >>> point = Point(-3, 2.5) # Initialization of an instance of the class
        >>> print(point.x, point.y)
        -3 2.5
        """

        self.x = None
        self.y = None

        self.set_x(x)
        self.set_y(y)

    def set_x(self, x: Union[int, float]) -> None:
        """"
        Set X coordinate for the Point instance
        :param x: X coordinate

        :raise TypeError: if an x coordinate has invalid type, raise an Error

        Examples:
        >>> point = Point (0, 0)
        >>> point.set_x(1)
        >>> print(point.x)
        1
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Error: Enter the correct X coordinate (int or float)")
        self.x = x

    def set_y(self, y: Union[int, float]) -> None:
        """
        Set Y coordinate for the Point instance
        :param y: Y coordinate

        :raise TypeError: if a y coordinate has invalid type, raise an Error

        Examples:
        >>> point = Point (0, 0)
        >>> point.set_y(3)
        >>> print(point.y)
        3
        """
        if not isinstance(y, (int, float)):
            raise TypeError("Error: Enter the correct Y coordinate (int or float)")
        self.y = y

    def get_x(self) -> Union[int, float]:
        """"
        Get X coordinate for the Point instance

        Example:
        >>> point = Point (2, 3)
        >>> point.get_x()
        2
        """
        return self.x

    def get_y(self) -> Union[int, float]:
        """"
        Get Y coordinate for the Point instance

        Example:
        >>> point = Point (2, 3)
        >>> point.get_y()
        3
        """
        return self.y

    def get_quadrant(self) -> int:
        """"
        Get the point's Cartesian quadrant

        :return: point's Cartesian quadrant

        Example:
        >>> point = Point(-2, -3)
        >>> point.get_quadrant()
        """
        ...

# --------------------------------------------------RECTANGLE-------------------------------------------#
class Rectangle:
    """"
    Class describes a Rectangle object
    """
    def __init__(self, bottom_left_point: Point, top_right_point: Point):
        """"
        Initialize an instance of the Rectangle class

        :param bottom_left_point: Bottom left point
        :param top_right_point: Top right point

        Examples:
        >>> rectangle = Rectangle(Point(1, 2), Point(4, 5)) # Class instance initialization
        """
        if not isinstance(bottom_left_point, Point):
            raise TypeError("First argument should be a Point")
        if not isinstance(top_right_point, Point):
            raise TypeError("Second argument should be a Point")
        if not (bottom_left_point.get_x() < top_right_point.get_x()):
            raise ValueError("First point's X coordinate is too high")
        if not (bottom_left_point.get_y() < top_right_point.get_y()):
            raise ValueError("First point's Y coordinate is too high")
        self.a = bottom_left_point
        self.b = top_right_point
        self.figure_name = "RECTANGLE"
        ...

    def getArea(self) -> Union[int, float]:
        """"
        Method calculates a rectangle's area

        :return: Rectangle's area

        Examples:
        >>> rectangle = Rectangle(Point(1, 2), Point(4, 5))
        >>> rectangle.getArea()
        """
        ...

    def getCenter(self) -> Point:
        """"
        Method returns a rectangle's center Point

        :return: center Point

        Examples:
        >>> rectangle = Rectangle(Point(1, 2), Point(4, 5))
        >>> rectangle.getCenter()
        """
        ...
    def getName(self) -> str:
        """"
        Method returns a figure's name

        :return: "RECTANGLE" str

        Examples:
        >>> rectangle = Rectangle(Point(1, 2), Point(4, 5))
        >>> rectangle.getName()
        """
        ...

# --------------------------------------------------TRIANGLE-------------------------------------------#
class Triangle:
    """"
    Class describes a Triangle object
    """
    def __init__(self, a: Point, b: Point, c: Point):
        """"
        Initialize an instance of the Rectangle class

        :param a: triangle point a
        :param b: triangle point b
        :param c: triangle point c

        Examples:
        >>> triangle = Triangle(Point(1, 2), Point(4, 3), Point(3, 5)) # Class instance initialization
        """
        if not isinstance(a, Point):
            raise TypeError("First argument should be a Point")
        if not isinstance(b, Point):
            raise TypeError("Second argument should be a Point")
        if not isinstance(c, Point):
            raise TypeError("Third argument should be a Point")
        self.a = a
        self.b = b
        self.c = c
        self.figure_name = "TRIANGLE"

    def scale(self, scale_coefficient: Union[int, float]) -> None:
        """"
        The method does an isotropic scaling of a triangle's instance,
        a center point remains the same after implementing the method. 
        
        :param scale_coefficient: scale coefficient
        :return: None

        Examples:
        >>> triangle = Triangle(Point(1, 2), Point(4, 3), Point(3, 5))
        >>> triangle.scale(2.2)
        """
        if not isinstance(scale_coefficient, (int, float)):
            raise TypeError("Error: Enter the correct scale coefficient value (int or float)")
        ...

    def move_to_origin(self) -> None:
        """"
        The method moves a Triangle object so the triangle's center
        aligns with the coordinate origin.
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
