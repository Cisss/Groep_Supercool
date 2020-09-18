def test():
    
    
    e = [2, 7, 1]
    pi = [3, 1, 4, 1, 5, 9]
    h = "hanze"
    s = "hogeschool"
    g = "groningen"

    # Opgave 0: [2, 7, 5, 9]
    answer0 = e[0:2] + pi[-2:]
    print("answer 0:", answer0)

    # Opgave 1: [7, 1]
    answer1 = e[1:]  
    print("answer 1:", answer1)
    
    # Opgave 2: [1, 1, 2]
    answer2 = [pi[1]] + e[::-2]
    print("answer 2:", answer2)

    # Opgave 3: [1, 4, 1, 5, 9]
    answer3 = pi[1:]
    print("answer 3:", answer3)

    # Opgave 4: [1, 2, 3, 4, 5]
    answer4 = e[::-2] + pi[::2]
    print("answer 4:", answer4)

    # Opgave 5: 'hoi' maken
    answer5 = s[0:2] + g[4]
    print("answer 5:", answer5)

    # Opgave 6: 'schoenen' maken
    answer6 = s[4:8] + g[-2:] + g[-2:]
    print("answer 6:", answer6)

    # Opgave 7: 'anzeogeschool' maken
    answer7 = h[1:] + s[1:]
    print("answer 7:", answer7)

    # Opgave 8: 'gnagnahahahahaha' maken
    answer8 = 2*(g[0] + h[-3:-5:-1]) + 5*(h[0:2])
    print("answer 8:", answer8)

    # Opgave 9: 'legonoego' maken
    answer9 = s[-1] + h[-1] + g[0:3:2]
    print("answer 9:", answer9)