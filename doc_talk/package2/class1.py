from doc_talk.package1.class1 import Class1Package1


class Class1Package2:
    """Class1Package2

    This class collaborate with :class:`doc_talk.package1.class1.Class1Package1`.
    """

    def __init__(self, obj: Class1Package1):
        self._obj = obj

    def do_something(self, arg1: str, arg2: int):
        """
        This method do something

        Example:

        .. code-block:: python

            obj1 = Class1Package1()
            obj = Class2Package1(obj1)
            obj.do_something(arg='hello', arg2=1)

        Args:
            arg1 (str): any string
            arg2 (int): any integer

        Returns:
            str: a ``str`` with obj, arg1 and arg2 concatenated

        """
        return self._obj.do_something(arg1=arg1, arg2=arg2)
