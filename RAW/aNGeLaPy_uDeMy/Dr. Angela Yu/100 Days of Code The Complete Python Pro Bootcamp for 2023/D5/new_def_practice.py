# quadratic equation of 3x^2 + x + 1, x = 3
def quadratic(x,const=1):
    """
    Prints both required and default parameters.

    Parameters:
    - required_param: The required parameter.
    - default_param: The parameter with a default value (default is 'Default Value').
    """
    y = 3*(x**2)+ x + const
    return y
quadratic(3,1)