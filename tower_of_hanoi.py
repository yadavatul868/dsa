
def tower_hanoi(n, s, d, h):

    # base condition
    if n == 1:
        print('moving plate from {} to {}'.format(s, d))
        return

    # recurrsive call
    tower_hanoi((n-1), s, h, d)

    # induction step
    print('moving plate from {} to {}'.format(s, d))
    tower_hanoi((n-1), h, d, s)

    return


