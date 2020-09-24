def tpl(x):
    """Returns thrice the argument

    :param x: The value to triple
    :type x: int, float or string
    :rtype: int, float or string
    """
    if type(x) == float or type(x) == int:
        return 3 * x
    else:
        return "This function only returns a float or an integer"

def sq(x):
    """Returns the square of the argument
        - argument must be an integer
    """
    if (type(x) == int):
        return x**2
    else:
        return "This function only returns an integer"
def interp(low, high, fraction):
    """Return the fraction
    """
    diffrence = high - low
    return (diffrence * fraction) + low

def checkends(s):
    """ Check if ends of a string consist the same caracter
            - returns true or false
    """
    x = len(s) - 1
    return s[0] == s[x]

def flipside(s):
    """ Cut string in half and put the last half before the first half
    """
    x = int(len(s) // 2)
    return s[x:] + s[:x]

def convert_from_seconds(s):
    """ convert seconds to
            - days
            - hours
            - minutes
            - seconds
    """
    days = s // (24*60*60)
    s = s % (24*60*60)
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // 60
    seconds = s % 60
    return [days, hours, minutes, seconds]
    