# Programmeren I, Week 2 Opgave 3
# Bestandsnaam: wk2ex3.py
# Naam:
# Problemomschrijving: Feest met functies!


#
# voorbeeldfunctie leng uit het college
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    else:
        print(s)
        return 1 + leng(s[1:])

def flipside(s):
    """flipside swaps s's sides
       Argument s: a string
    """
    x = len(s) // 2
    return s[x:] + s[:x]


#
# Tests
#
assert flipside("zijkant") == "kantzij"
assert flipside("huiswerk") == "werkhuis"
assert flipside("flipside") == "sideflip"
assert flipside("az") == "za"
assert flipside("a") == "a"
assert flipside("") == ""

def mult(n, m):
    """ this function multiplies n with m in a recursive way
       Argument n & m: integers
    """
    if m == 0:
        return 0
    elif m < 0:
        return -n + mult(n, (m+1))
    else:
        return n + mult(n, (m-1))

assert mult(6, 7) == 42
assert mult(6, -7) == -42
assert mult(-6, 7) == -42
assert mult(-6, -7) == 42
assert mult(6, 0) == 0
assert mult(0, 7) == 0
assert mult(0, 0) == 0

def dot(l, k):
    """ this function gives the inside product of l and k
       Argument l & k: integers
    """
    if leng(l) != leng(k) or l  == []:
        return 0
    else:
        return l[0] * k[0] + dot(l[1:], k[1:])