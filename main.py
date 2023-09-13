import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Este archivo contiene la simulación de un sistema físico masa-amortiguador-resorte hecha en Python utilizando numpy,
# matplotlib y scipy.

# Dentro de la bibliografía consultada para su realización se encuentra:
# -	Solving Differential Equations in Python: Higher order ODEs with solve_ivp – University of Edinburgh https://media.ed.ac.uk/media/Solving+Differential+Equations+in+PythonA+Higher+order+ODEs+with+solve_ivp/1_c8g7fwhw
# - Modelado de Sistemas Dinámicos – Universidad de Baja California https://uabc-msd.blogspot.com/2009/04/masa-resorte-amortiguador.html

# NOTAS PARA SU USO:
# - En caso de querer simular con valores determinados, ir a línea 27 donde se define la función sistema
# y cambiar en ellas los parámetros de la función a gusto.
# - Se ha considerado que se le ejerce una fuerza f contraria a la superficie que se modela en el tiempo con una función
# escalon. En caso de querer otra entrada, modificar la función f en línea 18.

# Función f de entrada. Representa la fuerza que se ejerce en el cuerpo en dirección contraria a la superficie.
# Es una función escalón, por lo que optamos por escribir una genérica.
def f(t, t0, t1, a):
    if t >= t0 and t1 > t:
        return a
    else: return 0


# La siguiente función devuelve el lado derecho de la ecuación de la segunda derivadad de la posición x con respecto
# al tiempo. En este caso se realiza un cambio de variable explicado en el informe, y pasamos de una EDO de orden 2
# a dos EDO de orden 1 acopladas.

# t es tiempo, ci son condiciones iniciales, b es constante de viscosidad, k es constante de elasticidad y f
# es la entrada descrita previamente.
def sistema(t, y):

    # Definimos parámetros del sistema
    t0 = 0  # Tiempo inicial en segundos
    t1 = 15  # Tiempo final en segundos
    a = 1000  # Fuerza en Newton
    b = 3000  # Viscosidad en Netwon*s/m
    k = 2500  # Elasticidad en Newton/m
    m = 50  # En kilogramos

    # Definimos f
    fun = f(t, t0, t1, a)

    # Igualamos variables a condiciones iniciales
    x = y[0]
    z = y[1]

    return [z, (- b * z - k * x + fun)/m]


# Definimos arreglo de tiempo
t = np.linspace(0, 50, 1000)
t_span = (0,50)


# Definimos condiciones iniciales
ci = [0, 0]

# Resolvemos
respuesta = solve_ivp(sistema, t_span, [0, 0], method='RK45', t_eval=t)

# Ploteamos resultado
plt.plot(respuesta.t, respuesta.y[0])
plt.ylabel('Posición del cuerpo respecto\n a posición inicial [cm]')
plt.xlabel('Tiempo [s]')
plt.show()

# Se puede descomentar la siguiente línea si quiere verse la solución que arroja solve_ivp, que es un objeto con campos
# que muestran información de la solución.
#print(respuesta)

# Dejo esta parte comentada porque sirve para verificar que la entrada f es correcta.
# arr = []
# for i in np.arange(0,len(t)):
#     arr.append(f(t[i],0,15,2000))
#
# plt.plot(respuesta.t, arr)
# plt.ylabel('Posición del cuerpo respecto\n a posición inicial [cm]')
# plt.xlabel('Tiempo [s]')

# plt.show()

# Ploteamos resultado

#Imprimimos respuesta
plt.plot(respuesta.t, respuesta.y[0])
plt.ylabel('Posición del cuerpo respecto\n a posición inicial [m]')
plt.xlabel('Tiempo [s]')
plt.show()
