print("Program Mengurutkan Bilangan")
print("----------------------------")

a = input("Masukan Bilangan Pertama = ")
b = input(" Masukan Bilangan Kedua = ")
c = input("Masukan Bilangan Ketiga =")

if a < b and a < c:
        if b < c:
            print(a, b, c)
        else:
            print(a, c, b)
elif b < a and b < c:
        if a < c:
            print(b, a, c)
        else:
            print(b, c, a)
else:
        if a < b:
            print(c, a, b)
        else:
            print(c, b, a)

print(" ")
print('Selesai')

