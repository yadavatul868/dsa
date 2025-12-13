

def kth_symbol(N, k):


    # base condition
    if ((N == 1) & (k == 1)):
        return 0

    # otherwise calculate length first
    c = pow(2, (N-1))
    mid = int(c / 2)

    # now recurrsive call
    if k <= mid:
        return kth_symbol(N-1, k)
    else:
        return 0 if kth_symbol(N-1, k - mid) == 1 else 1



