import math

if __name__ == "__main__":
    a = 1.0
    b = 1.000000001
    c = 0.000000001

    sd = math.sqrt(b*b - 4*a*c)

    alpha = (-b - sd) / (2*a)
    beta  = c / (a * alpha)
    
    print(f"alpha = {alpha:.1f} \t beta = {beta:.23f}")
    print(f"alpha = -1.0 \t beta = -0.000000001")
    print(f"sd= {sd}")
