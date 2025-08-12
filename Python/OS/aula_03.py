num = []
for i in range(0,21):
    num.append(i)

for u in range(0,21):
        

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} Não é primo")
            break
        else:
            print(f"{num}, É primo")
elif num == 0:
    print(f"{num}, É zero")

elif num == 1:
    print(f"{num}, É primo")

elif num < 0:
    print(f"{num}, É negativo")
