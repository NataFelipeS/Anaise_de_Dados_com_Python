import numpy as np

# Criando Arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
matriz = np.array([[1,2,3], [3,4,5], [6,7,8]])
zeros = np.array([0, 0, 0, 0, 0])
matrizdois = np.array([[1,1,1], [1,1,1]])
print("Original array:", arr)
print("Matriz 3x3 array:\n",matriz)
print("Matriz 2x3 array:\n",matrizdois)
print("-----------------------------------")

# Indexação e fatiamento
print(arr[-1],0)
print(arr[1:6])
print(matriz[1,2])
print(matriz[0])
print()
print("-----------------------------------")

# Indexação Booleana
print(arr[arr % 2 == 0])
print(arr[arr > 10])
arr[arr < 5] = 0
print(arr)
print("-----------------------------------")

# Manipulação de Arrays
arr[2] = 99
print(arr[2])
arr = np.arange(1,10)
arr_reshape = arr.reshape(3, 3)
print("\nArray redimensionado para 3x3: \n", arr_reshape)
print("-----------------------------------")

# Concatenação de Arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6])
concatenado = np.concatenate((arr1, arr2))
print(concatenado)
print("-----------------------------------")

# Operações Matemáticas
print("Array + 10:", arr1 + 10)
print("Array * 2:", arr1 * 2)
print("Array ao quadrado:", arr1 **2)
print("Raiz quadrada:", np.sqrt(arr1))
print("-----------------------------------")

# Estatísticas Básicas
arr10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Média:", np.mean(arr10))
print("Desvio padrão:", np.exp(arr10))
print("Soma total:", np.sum(arr10))

