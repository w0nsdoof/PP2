def solve(heads, legs):
    rabbits = int(legs/2 - heads)
    chickens = int(heads - rabbits)

    print("Chickens: " + str(chickens))
    print("Rabbits: " + str(rabbits))

heads = int(input())
legs = int(input())

solve(heads, legs)

'''
 35 heads 94 legs
 chicken = 2 legs, rabbits = 4 legs

 func(heads, legs) -> rabbits num, chicken num

(heads - x)*2 + 4x = legs
heads - x + 2x = legs/2
x = rabbits = legs/2 - heads = 47 - 35
'''