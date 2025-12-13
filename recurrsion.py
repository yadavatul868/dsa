

# Recurrsion

def find_sum(n):

    if n == 1:
        return 1
    else:
        return n +  find_sum(n-1)
    

# 0, 1, 1, 2, 3, 5
# ----------------
# 0, 1, 2, 3, 4, 5

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    


if __name__ == '__main__':
    print(find_sum(5))
    print(fib(10))
