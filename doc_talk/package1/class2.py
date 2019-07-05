from .class1 import Class1Package1


class Class2Package1:
    """Class2Package1

    This class collaborate with Class1Package1.
    """

    def __init__(self, obj: Class1Package1):
        self._obj = obj

    def do_something(self, arg1: str, arg2: int):
        """
        This method do something

        Examples:

            obj1 = Class1Package1()
            obj = Class2Package1(obj1)
            obj.do_something('hello', 1)

        Args:
            arg1: any string
            arg2: any integer

        Returns:
            str: a string with obj, arg1 and arg2 concatenated

        """
        self._private_method()
        return self._obj.do_something(arg1=arg1, arg2=arg2)

    def _private_method(self):
        """_private_method.

        I do nothing, it's only an example!
        """
