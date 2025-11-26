import math
if __name__ == "__main__":
    N = 5000000

    s = 0
    c = 0
    for i in range(N):
        x = (i + 0.5)/N
        f = math.sqrt(1 - x*x)
        y = f - c
        t = s + y
        c = (t - s) - y    #積み残し
        s = t

    print(f"pi = {4.0*s/N}")
    print(f"pi = {math.pi}")
