class Wrapper:
    """Wrapper of a function.

    It could be used to reduce repetition of calling a function with the same arguments.
    
    Args:
        `func`: The function needs to be wrapped.
        `*args`: The positional arguments of `func`.
        `**kwargs`: The keyword arguments of `func`.
    """
    def __init__(self, func, *args, **kwargs):
        self.__func = lambda: func(*args, **kwargs)
    
    def __call__(self):
        """Call the instance as the wrapped function.
        """
        return self.__func()