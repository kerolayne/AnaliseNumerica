# coding: utf-8
ponto = [(-2.5,0.89),(-2.0,-1.18),(-1.5,1.88),(-1.0,4.06),(-0.5,1.21)]
pont = [(-2.5,-3.99), (-2.0,-5.26), (-1.5,0.54), (-1.0,-4.29), (-0.5,-2.59), (0.0,-0.95), (0.5,-0.15)]
pon = [(-2.5,0.94), (-2.0,-3.08), (-1.5,5.33), (-1.0,2.57), (-0.5,-5.94), (0.0,4.39), (0.5,-2.35), (1.0,0.17), (1.5,5.38),
(2.0,-1.13), (2.5,-2.63)]
pontos = [(-2.5,-5.6), (-2.0,-4.03), (-1.5,-0.4), (-1.0,-1.12), (-0.5,1.51), (0.0,2.98), (0.5,-4.59), (1.0,0.56), (1.5,-4.43),
(2.0,-5.53), (2.5,2.14), (3.0,4.02), (3.5,0.85), (4.0,1.37), (4.5,5.26), (5.0,2.79), (5.5,5.16), (6.0,-2.28), (6.5,-2.9),
(7.0,-0.61), (7.5,-3.93), (8.0,2.04), (8.5,5.61), (9.0,-2.09), (9.5,1.55), (10.0,-0.59), (10.5,-5.47), (11.0,-5.5),
(11.5,2.64), (12.0,2.0), (12.5,5.1)]
xs, ys = zip(*pontos)
n = len(pontos)

# auxiliares
def prod(lista):
    p = 1
    for i in lista:
        p *= i
    return p

def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

# algoritmo
def tabela(pontos):
    Y = {}
    Y[0] = {k: v for k, v in enumerate(ys)}
    for j in range(1, n):
        Y[j] = {}
        for i in range(n - j):
            Y[j][i] = (Y[j - 1][i + 1] - Y[j - 1][i]) / (xs[j + i] - xs[i])
    return Y

t = tabela(pontos)
a = [v[0] for k, v in t.items()]

def p(x):
    soma = 0
    for k in range(n):
        termo_k = prod([(x - xi) for i, xi in enumerate(xs) if i < k])
        soma += a[k] * termo_k
    return soma

def eq(coefs):
    equation = ""
    for k in range(n):
        
        termo_k = "*".join([f'(x{sign(-xi)})' for i, xi in enumerate(xs) if i < k])
        print ("Interação", k, " -  Termo",(termo_k),"\n         Equação - ",equation,"\n\n")
        if k == 0:
            equation += str(a[k])
        else:
            equation += f'{sign(a[k])}*' + termo_k
    return equation

poly = eq(a)
print(poly)

# Método das diferenças divididas (de Newton)

import matplotlib.pyplot as plt
import numpy as np

def poly_f(x):
    return eval(poly)

a, b = min(xs) - 0.5, max(xs) + 0.5
t = np.arange(a, b, 0.01)
plt.scatter(xs, ys)
plt.plot(t, poly_f(t), color="red", label="polinomio interpolador")
plt.show()


"""
Questão 4 - Primeiro Polinomio -
Interação 0  -  Termo
         Equação -


Interação 1  -  Termo (x+2.5)
         Equação -  0.89


Interação 2  -  Termo (x+2.5)*(x+2.0)
         Equação -  0.89-4.14*(x+2.5)


Interação 3  -  Termo (x+2.5)*(x+2.0)*(x+1.5)
         Equação -  0.89-4.14*(x+2.5)+10.259999999999998*(x+2.5)*(x+2.0)


Interação 4  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)
         Equação -  0.89-4.14*(x+2.5)+10.259999999999998*(x+2.5)*(x+2.0)-8.013333333333332*(x+2.5)*(x+2.0)*(x+1.5)


0.89-4.14*(x+2.5)+10.259999999999998*(x+2.5)*(x+2.0)-8.013333333333332*(x+2.5)*(x+2.0)*(x+1.5)+1.2399999999999998*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)











Questão 4 - Segundo Polinomio - 

Interação 0  -  Termo
         Equação -


Interação 1  -  Termo (x+2.5)
         Equação -  -3.99


Interação 2  -  Termo (x+2.5)*(x+2.0)
         Equação -  -3.99-2.539999999999999*(x+2.5)


Interação 3  -  Termo (x+2.5)*(x+2.0)*(x+1.5)
         Equação -  -3.99-2.539999999999999*(x+2.5)+14.139999999999999*(x+2.5)*(x+2.0)


Interação 4  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)
         Equação -  -3.99-2.539999999999999*(x+2.5)+14.139999999999999*(x+2.5)*(x+2.0)-23.599999999999998*(x+2.5)*(x+2.0)*(x+1.5)


Interação 5  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)
         Equação -  -3.99-2.539999999999999*(x+2.5)+14.139999999999999*(x+2.5)*(x+2.0)-23.599999999999998*(x+2.5)*(x+2.0)*(x+1.5)+23.24*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)


Interação 6  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)
         Equação -  -3.99-2.539999999999999*(x+2.5)+14.139999999999999*(x+2.5)*(x+2.0)-23.599999999999998*(x+2.5)*(x+2.0)*(x+1.5)+23.24*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-15.629333333333332*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)


-3.99-2.539999999999999*(x+2.5)+14.139999999999999*(x+2.5)*(x+2.0)-23.599999999999998*(x+2.5)*(x+2.0)*(x+1.5)+23.24*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-15.629333333333332*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)+7.8373333333333335*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)









Questão 4 - Terceiro Polinomio

Interação 0  -  Termo
         Equação -


Interação 1  -  Termo (x+2.5)
         Equação -  0.94


Interação 2  -  Termo (x+2.5)*(x+2.0)
         Equação -  0.94-8.04*(x+2.5)


Interação 3  -  Termo (x+2.5)*(x+2.0)*(x+1.5)
         Equação -  0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)


Interação 4  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)
         Equação -  0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)-31.46666666666667*(x+2.5)*(x+2.0)*(x+1.5)


Interação 5  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)
         Equação -  0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)-31.46666666666667*(x+2.5)*(x+2.0)*(x+1.5)+19.346666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)


Interação 6  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)
         Equação -  0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)-31.46666666666667*(x+2.5)*(x+2.0)*(x+1.5)+19.346666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-2.6266666666666665*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)


Interação 7  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)
         Equação -  0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)-31.46666666666667*(x+2.5)*(x+2.0)*(x+1.5)+19.346666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-2.6266666666666665*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)-6.206222222222222*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)


Interação 8  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)
         Equação -  0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)-31.46666666666667*(x+2.5)*(x+2.0)*(x+1.5)+19.346666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-2.6266666666666665*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)-6.206222222222222*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)+6.913777777777779*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)


Interação 9  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)*(x-1.5)
         Equação -  0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)-31.46666666666667*(x+2.5)*(x+2.0)*(x+1.5)+19.346666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-2.6266666666666665*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)-6.206222222222222*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)+6.913777777777779*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)-4.396952380952381*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)


Interação 10  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)*(x-1.5)*(x-2.0)
         Equação -  0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)-31.46666666666667*(x+2.5)*(x+2.0)*(x+1.5)+19.346666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-2.6266666666666665*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)-6.206222222222222*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)+6.913777777777779*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)-4.396952380952381*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)+2.047111111111111*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)*(x-1.5)


0.94-8.04*(x+2.5)+24.86*(x+2.5)*(x+2.0)-31.46666666666667*(x+2.5)*(x+2.0)*(x+1.5)+19.346666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-2.6266666666666665*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)-6.206222222222222*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)+6.913777777777779*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)-4.396952380952381*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)+2.047111111111111*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)*(x-1.5)-0.7488169312169312*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)*(x-1.5)*(x-2.0)







Questão 4 - Quarto Polinômio - 
Interação 0  -  Termo
         Equação -


Interação 1  -  Termo (x+2.5)
         Equação -  -5.6


Interação 2  -  Termo (x+2.5)*(x+2.0)
         Equação -  -5.6+3.139999999999999*(x+2.5)


Interação 3  -  Termo (x+2.5)*(x+2.0)*(x+1.5)
         Equação -  -5.6+3.139999999999999*(x+2.5)+4.120000000000002*(x+2.5)*(x+2.0)


Interação 4  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)
         Equação -  -5.6+3.139999999999999*(x+2.5)+4.120000000000002*(x+2.5)*(x+2.0)-8.546666666666669*(x+2.5)*(x+2.0)*(x+1.5)


Interação 5  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)
         Equação -  -5.6+3.139999999999999*(x+2.5)+4.120000000000002*(x+2.5)*(x+2.0)-8.546666666666669*(x+2.5)*(x+2.0)*(x+1.5)+9.406666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)


Interação 6  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)
         Equação -  -5.6+3.139999999999999*(x+2.5)+4.120000000000002*(x+2.5)*(x+2.0)-8.546666666666669*(x+2.5)*(x+2.0)*(x+1.5)+9.406666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-7.018666666666666*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)


Interação 7  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)
         Equação -  -5.6+3.139999999999999*(x+2.5)+4.120000000000002*(x+2.5)*(x+2.0)-8.546666666666669*(x+2.5)*(x+2.0)*(x+1.5)+9.406666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-7.018666666666666*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)+3.1253333333333333*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)


Interação 8  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)
         Equação -  -5.6+3.139999999999999*(x+2.5)+4.120000000000002*(x+2.5)*(x+2.0)-8.546666666666669*(x+2.5)*(x+2.0)*(x+1.5)+9.406666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-7.018666666666666*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)+3.1253333333333333*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)-0.279111111111111*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)


Interação 9  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)*(x-1.5)
         Equação -  -5.6+3.139999999999999*(x+2.5)+4.120000000000002*(x+2.5)*(x+2.0)-8.546666666666669*(x+2.5)*(x+2.0)*(x+1.5)+9.406666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-7.018666666666666*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)+3.1253333333333333*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)-0.279111111111111*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)-0.764761904761905*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)


Interação 10  -  Termo (x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)*(x-1.5)*(x-2.0)
         Equação -  -5.6+3.139999999999999*(x+2.5)+4.120000000000002*(x+2.5)*(x+2.0)-8.546666666666669*(x+2.5)*(x+2.0)*(x+1.5)+9.406666666666668*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)-7.018666666666666*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)+3.1253333333333333*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)-0.279111111111111*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)-0.764761904761905*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)+0.7265326278659613*(x+2.5)*(x+2.0)*(x+1.5)*(x+1.0)*(x+0.5)*(x+-0.0)*(x-0.5)*(x-1.0)*(x-1.5)





"""