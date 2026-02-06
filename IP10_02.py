if __name__ == "__main__":
    n = 1
    t = 1.0

    for i in range(1,100):
        n *= i
        t += 1.0/n
    print(f"{t:.15f}")
    print("2.718281828459045")
