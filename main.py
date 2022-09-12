import numpy as np


# lista_elemetos = []
# for x in range(num_elementos):
#     lista_elemetos.append(x)
#     print(lista_elemetos[-1])

num_elementos = 100000000

array_elements = np.arange(num_elementos)
# print(array_elements[-1])

# criar array em numpy

array_teste = np.array([0,1,2,3])
# print(f'criancao array numpy \n{array_teste}')
# print(f'{np.ones([100])}')
# print(f'{np.arange(100)}')


# random
rng = np.random.default_rng()
# print(rng.random(10))

#vetor = array de uma dimensao
#vetor = rng.random(4)
# print(vetor)
#matirz

# matriz = rng.random([4,4])
# print(matriz)

#tensor = 3 dimensoes



#ordernar

array_1 = rng.random([2,3])
print(array_1)
print(np.sort(array_1, axis= 1))








