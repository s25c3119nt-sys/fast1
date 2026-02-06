from fractions import Fraction

if __name__ == "__main__":
    f = Fraction()
    n = 100000

    for i in range(n):
        f = f + Fraction(1,n)
    print(f"f = {float(f)}")
