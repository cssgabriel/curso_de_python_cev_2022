# Exercício 63. Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.

print("-" * 15)
print("Sequência de Fibonacci")
print("-" * 15)
termos = int(input("Quantos termos você quer mostrar? "))
print("~"*15)
c = 0
fib = 1
anterior1 = 0
anterior0 = 0
while c < termos:
    if c == 0:
        fib += anterior0 + anterior1
    else:
        fib = anterior0 + anterior1
    anterior1 = anterior0
    anterior0 = fib
    c += 1
    print("{} -> ".format(fib),end="")
print("FIM!")
print("~"*15)

# solucação professor

termos = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print("{} -> {} -> ".format(t1, t2),end="")
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print("{} -> ".format(t3),end="")
    t1 = t2
    t2 = t3
    cont += 1
print("FIM!")