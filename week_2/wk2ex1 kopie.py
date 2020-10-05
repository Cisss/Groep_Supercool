def test():
    
    
    e = [2, 7, 1]
    pi = [3, 1, 4, 1, 5, 9]

    # [2, 7, 5, 9]
    answer0 = e[0:2] + pi[-2:]
    print("answer 0:", answer0)

    # [7, 1]
    answer1 = e[1:]  
    print("answer 1:", answer1)
    
    # [1, 1, 2]
    answer2 = [pi[1]] + e[::-2]
    print("answer 2:", answer2)

    # [1, 4, 1, 5, 9]
    answer3 = pi[1:]
    print("answer 3:", answer3)

    # [1, 2, 3, 4, 5]
    answer4 = e[::-2] + pi[::2]
    print("answer 4:", answer4)