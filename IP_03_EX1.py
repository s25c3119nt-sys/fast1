i = float(input("1つ目の値を入力してください "))
j = float(input("2つ目の値を入力してください "))

print("1つ目の値 = {}".format(i))
print("2つ目の値 = {}".format(j))

result = i / j

int_part = int(result)
frac_part = result - int_part

print("{} と {} の割り算の整数部分は{}".format(i, j, int_part))
print("{} と {} の割り算の小数部分は{}".format(i, j, frac_part))