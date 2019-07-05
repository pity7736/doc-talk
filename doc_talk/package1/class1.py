
class Class1Package1:
    """ Class1Package1

    This is a test class for the doc talk

    """

    def __init__(self):
        pass

    def do_something(self, arg1: str, arg2: int):
        """
        This method do something

        Examples:

            obj = Class1Package1()
            obj.do_something('hello', 1)

        Args:
            arg1: any string
            arg2: any integer

        Returns:
            str: a string with self, arg1 and arg2 concatenated

        """
        return f'{self} - {arg1} - {arg2}'
