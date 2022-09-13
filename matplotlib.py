import matplotlib.pyplot as plt

# usado matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
# usando lib sympy para resolver as equações
from sympy import Symbol
from sympy.solvers import solve
# definindo y como simbolo
y = Symbol('y')

# valores de X definidos pela tarefa
x1 = 5
x2 = 7
x3 = 9
# tres ultimos numeros do ru
a = 3
b = 3
c = 1
#y = ax + bx - c
# equações  com valores de x correspondente

equacaoUm = a * x1 + b * x1 - c - y
equacaoDois = a * x2 + b * x2 - c - y
equacaoTres = a * x3 + b * x3 - c - y

# usando o solve para achar o y de cada equação
equacaoResultUm = solve(equacaoUm, y)
equacaoResultDois = solve(equacaoDois, y)
equacaoResultTres = solve(equacaoTres, y)

# é preciso fazer um tratamento para o resultado usando solve
# transforma em string e remove [] e ()
removeColcheteEqUm = str(equacaoResultUm).strip('[]')
resultadoTratadoEqUmY = removeColcheteEqUm.strip('()')
removeColcheteEqDois = str(equacaoResultDois).strip('[]')
resultadoTratadoEqDoisY = removeColcheteEqDois.strip('()')
removeColcheteEqTres = str(equacaoResultTres).strip('[]')
resultadoTratadoEqTresY = removeColcheteEqTres.strip('()')
# inserindo legenda
fig, ax = plt.subplots()
red_patch = mpatches.Patch(
    color='blue', label='Reta formada pela ligação dos pares ordenados')
ax.legend(handles=[red_patch])

# personalizando o gráfico
# tamanho da linha e style
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'

#reta com mudança da cor padrão
plt.plot([x1, x2, x3], [resultadoTratadoEqUmY,
         resultadoTratadoEqDoisY, resultadoTratadoEqTresY], color="blue")
plt.ylabel('Eixo y')
plt.xlabel('Eixo x')
plt.show()
