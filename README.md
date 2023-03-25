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
en la libreria principal capitulo4.py después de las funciones usted encontrará unos numerales como 4.3.1, son algunos ejercicios desarrollados con la ayuda de las funciones que aqui vamos a explicar:
1. **4.3.1:  Find all the possible states the system described in Exercise 4.2.2 can transition into after a measurement has been carried out.**
en contexto el ejercicio 4.2.2 nos da el estado [1,0] y observable [[0,1],[1,0]] si se nos pregunta por los posibles estados a los que el estado inicial puede transitar despues de una medición, en realidad nos preguntan por los vectores propios del observable, cuya respuesta está en la libreria y son los estados: (1/√2)[1,-1] y (1/√2)[1,1], a esos estados puede ir
2. **4.3.2:  Perform the same calculations as in the last example, using Exercise 4.3.1. Then draw the probability distribution of the eigenvalues as in the previous example.**
con el mismo estado anterior nos piden las probabilidades de que ese estado transite a cada uno de los vectores propios del observable, dicha respuesta está en la primera lista resultante del punto, en este caso la probabilidad1 = 0.5 y la probabilidad2 = 0.5 es decir que en ambos casos, el estado tiene la misma probabilidad de transitar a cualquiera de sus vectores propios. ahora, los valores propios del observable son 1 y -1 que son la segunda lista dada en la solucion en el archivo py, si hacemos pi*1-1*p2 eso será igual a cero, valor que es igual a la media o valor esperado del estado en el observable dado
3. **4.4.1: Verify that [[0,1],[1,0]] and (√2)/2[[1,1],[1,-1]] are unitary matrices. Multiply them and verify that their product is also unitary.**
este ejercicio es sencillo, simplemente usamos la funcion en la libreria de espacios vectoriales o libvecspaces, la funcion se llama unitario y recibe la matriz, para luego decirme si lo es o no, es por eso que se uso primero para saber si las matrices dadas son unitarias, como resultado es que si, y luego se hace la multiplicacion con otra función de libvecspaces, para preguntar si es unitaria y como resultado tenermos que si, como se evidencia en el archivo python
4. **4.4.2: Go back to Example 3.3.2 (quantum billiard ball), keep the same initial state vector [1,0,0,0]T, but change the unitary map to (...) Determine the state of the system after three time steps. What is the chance of the quantum ball to be found at point 3?.**
en el ejemplo 3.3.2 nos dan una matriz doblemente estocastica, cuyo valor usted observará en el archivo python como billar1, ahora se nos da otra matriz, cuyo valor se observa en el archivo python como billar y nos dan el mismo estado para preguntarnos que pasa despues de 3 clicks de tiempo, para solución de este problema se acudio a la libreria de salto_clasico_cuantico y obtuvimos dos estados finales, uno que se llama state y esta relacionado a la matriz billar y state1 relacionado a billar1, se observo que state es: [0,-1/√2+1/√2i,0,0] y state1 es [0,1/√2,1/√2,0] (recuerde que la probabilidad se da con el conjugado al cuadrado de cada uno) en conclusión se obtuvo que en state la particula despues de 3 clics estará en la posicion 1 en vez de la posicion 0, mientras que en state1 la particula tendra un 50% de probabilidad que esté en la posición 1 o 50% de que esté en la posición 2.
