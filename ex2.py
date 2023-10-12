n = int(input("Fibonacci sonlarini nechta chiqarishni hohlaysiz? "))

fibonacci_sonlari = [0, 1]
for i in range(2, n):
    fibonacci_sonlari.append(fibonacci_sonlari[i-1] + fibonacci_sonlari[i-2])
for son in fibonacci_sonlari:
    print(son)