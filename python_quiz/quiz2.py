for x in range(2, 10):
    for y in range(1, 10):
        if y == 1:
            print('-' * 11)
        print(f'{x} x {y} = {x*y}')
        if x == 9 and y == 9:
            print('-' * 11)