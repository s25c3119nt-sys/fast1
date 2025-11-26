if __name__ == "__main__":
    f = 0.0
    n = 100000
    s = 1.0 / n       
    l = 0.0 #積み残し

    for _ in range(n):
        id = s + l
        new_f = f + id
        ac = new_f - f
        l = id - ac
        f = new_f

    print(f"f = {f:.24f}")

