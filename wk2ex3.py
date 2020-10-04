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

def ind(e, L):
    if L == [] or L == '':
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

#
# Tests
#
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100))) == 42
assert ind("hoi", ["hallo", 42, True]) == 3
assert ind("hoi", ["oh", "hoi", "daar"]) == 1
assert ind("i", "team") == 4
assert ind(" ", "nader onderzoek") == 5

def letter_score(let):
    """ This function gives the value of the letter
       Argument let: string with one letter
    """
    if let in 'AaDdEeIiNnOoRrSsTt':
        return 1
    elif let in 'GgHhLl':
        return 2
    elif let in 'BbCcMmPp':
        return 3
    elif let in 'JjKkUuVvWw':
        return 4
    elif let in 'Ff':
        return 5
    elif let in 'Zz':
        return 6
    elif let in 'XxYy':
        return 8
    elif let in 'Qq':
        return 10
    else:
        return 0

def scrabble_score(s):
    """ This function gives the score of the word using the letter_score() function on eevery letter
    Argument s: a string
    """
    if s == '':
        return 0
    else:
        return letter_score(s[0]) + scrabble_score(s[1:])

#
# Tests
#
assert scrabble_score("quotums") == 24
assert scrabble_score("jacquet") == 24
assert scrabble_score("pyjama") == 20
assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 84
assert scrabble_score("?!@#$%^&*()") == 0
assert scrabble_score("") == 0


def transcribe(s):
    """ 
    """
    if s == '':
        return ''
    elif s[0] in "ACGT":
        return one_dna_to_rna(s[0]) + transcribe(s[1:])
    else:
        return " " + transcribe(s[1:])


def one_dna_to_rna(c):
    if c == 'A':
        return 'U'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'
    else:
        return 'A'


