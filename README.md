# Observables-Y-Medidas📐 👀
Este repositorio contiene la aplicación de diferentes operaciones dentro de los observables y medidas de un sistema cuántico, además de la explicación de unos ejercicios para afianzar el conocimiento
## Autor:
***Sebastian Cardona***

## El repositorio contiene: 

### ***libreria capitulo4.py:***
esta es la librería principal, es decir aquí se encuentran las funciones necesarias para las operaciones dentro del tema observables y medidas. 
1. **funciones de apoyo:**
Funciones no tan revelantes que son necesarias para operaciones más complejas, funcion de modulo cuadrado esta funcion simplemente calcula el modulo al cuadrado de un número complejo, funcion normal, esta función devuelve el normal de un vector y la funcion normalizar que normaliza un vector, tambien estan las funciones de vectores y valores propios que devuelven de una matriz los vectores y valores propios de la misma
2. **función probabilidad:**
Aqui la función devuelve la probabilidad de que en un sistema donde una particula esté confinada en unas posiciones dadas, esta misma particula se encuentre en una posición x después de observarlo
3. **función transición:**
Dado dos estados o kets, esta funcón devuelve la probabilidad de que se transite del uno al otro después de observar
4. **función media:**
Tambien llamado valor esperado simplemente devuelve el valor promedio que se obtiene después de hacer muchas observaciones
5. **función varianza**
Devuelve un valor, si es muy alto indica que la mayoria de valores propios estan lejos de la media, y si es bajo nos dice que la mayoria de valores propios estan cerca a la media
6. **función transitar a vectores propios**
devuelve una lista con las probabilidades de que el estado transite a un vector propio del observable, es decir el primer elemento de la lista indica la amplitud de transicion del estado a el primer vector propio y asi sucesivamente
7. **Función finalstate**
Dada una secuencia de matrices unitarias en una dinámica del sistema, lo que devolverá será el estado final después de pasar por todas las matrices
### ***librerias de apoyo.py:***
Son las librerias de libvecspaces.py y salto_clasico_cuántico.py y simplemente se usaron para poder desarrolar la libreria principal, la explicación de cada una de estas librerias ya está en su propio repositorios
### ***libreria testobser_med.py:***
Aquí se encuentran las pruebas que se hicieron a las funciones de capitulo4.py son soportes que idican que las funciones funcionan correctamente, se hicieron dos pruebas por funcion, al correr usted este código recibirá un ok que indica que en todos los test el resultado es correcto
### ***Discusión 4.5.2 y 4.5.3.py:***
es un archivo PDF donde se encuentra la solución a los puntos 4.5.2 y 4.5.3 del libro Quantum Computing for computers scientists de Mannucci y Yanofsky
### ***Solucion problemas:***
