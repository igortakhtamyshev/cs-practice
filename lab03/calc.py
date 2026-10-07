x = float(input("x = "))
y = float(input("y = "))

summ = x + y
diff = x - y
prod = x * y

print("Сумма", summ)
print("разность", diff)
print("Произведение", prod)
if y != 0:
    print("Частное", x / y)
else:
    print("Частное - ошибка")
