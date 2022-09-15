import time
import random as rnd

#Creamos las variables de cada color que utilizaremos para imprimir los textos.
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[39m"
#Inicializaremos una variable 'puntaje = 0' para el puntaje de la trivia.
puntaje = 0
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.
#Pedimos al usuario su nombre.
nombre = input("Ingrese su nombre y presione 'Enter' para empezar: ")
#Mostramos en pantalla un texto de bienvenida para el jugador
print(GREEN+"Hola,",nombre,", bienvenido a mi trivia. Pondré a prueba tus conocimientos sobre cultura general. Al empezar esta trivia tienes", puntaje,"puntos. Y al terminarla veremos cuanto puntaje alcanzaste."+RESET)
#Damos las instrucciones de cómo jugar.
print(MAGENTA+"Para responder las siguientes preguntas deberás escribir la letra de la alternativa y después presionar 'Enter' para verificar si tu respuesta es correcta.\n"+RESET)
while iniciar_trivia == True:
 intentos +=1
 puntaje=0
 print(YELLOW+"\nIntento número: ",intentos)
 input("Presiona 'Enter' para continuar.")
 print(CYAN+"Empezamos en: "+RESET)
 for i in range(5,0,-1):
    print(i)
    time.sleep(1)
#Pregunta 1
 print(RED+"\n1) ¿Cuál es el país más poblado del mundo?"+RESET)
 time.sleep(3)
 print(BLUE+"a) Rusia")
 print("b) India")
 print("c) China")
 print("d) Estados Unidos"+RESET)
 respuesta_1 = input("\nTu respuesta: ")
 while respuesta_1 not in ("a","A","b","B","c","C","d","D"):
  respuesta_1 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
 if respuesta_1 == "a" or respuesta_1 == "A":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 elif respuesta_1 == "b" or respuesta_1 == "B":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 elif respuesta_1 == "c" or respuesta_1 == "C":
    puntaje += 5
    print(YELLOW+"Respuesta correcta. Sigue así!"+RESET)
 else:
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 print(BLACK+"Tu puntaje hasta ahora es: ",puntaje,"puntos"+RESET)
 time.sleep(3)
#Pregunta 2
 print(RED+"\n2) ¿Quién escribió 'Hamlet'?"+RESET)
 time.sleep(3)
 print(BLUE+"a) Goethe")
 print("b) Edgar Allan Poe")
 print("c) José María Arguedas")
 print("d) William Shakespeare"+RESET)
 respuesta_2 = input("\nTu respuesta: ")
 while respuesta_2 not in ("a","A","b","B","c","C","d","D"):
  respuesta_2 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
 if respuesta_2 == "a" or respuesta_2 == "A":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 elif respuesta_2 == "b" or respuesta_2 == "B":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 elif respuesta_2 == "c" or respuesta_2 == "C":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 else:
    puntaje += 5
    print(YELLOW+"Respuesta correcta. Lo haces muy bien!"+RESET)
 print(BLACK+"Tu puntaje hasta ahora es: ",puntaje,"puntos"+RESET)
 time.sleep(3)
#Pregunta 3
 print(RED+"\n3) ¿De qué famoso grupo formaba parte Paul McCartney?"+RESET)
 time.sleep(3)
 print(BLUE+"a) Queen")
 print("b) The Beatles")
 print("c) The Police")
 print("d) The Rolling Stones"+RESET)
 respuesta_3 = input("\nTu respuesta: ")
 while respuesta_3 not in ("a","A","b","B","c","C","d","D"):
  respuesta_3 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
 if respuesta_3 == "a" or respuesta_3 == "A":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 elif respuesta_3 == "b" or respuesta_3 == "B":
    puntaje +=5
    print(YELLOW+"Respuesta correcta. Estas en racha!"+RESET)
 elif respuesta_3 == "c" or respuesta_3 == "C":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 else:
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 print(BLACK+"Tu puntaje hasta ahora es: ",puntaje,"puntos"+RESET)
 time.sleep(3)
#Pregunta 4
 print(RED+"\n4)¿Cuál es la película más taquillera de la historia?"+RESET)
 time.sleep(3)
 print(BLUE+"a) Spiderman no way home")
 print("b) Avengers Endgame")
 print("c) Avatar")
 print("d) Titanic"+RESET)
 respuesta_4 = input("\nTu respuesta: ")
 while respuesta_4 not in ("a","A","b","B","c","C","d","D"):
  respuesta_4 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
 if respuesta_4 == "a" or respuesta_4 == "A":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 elif respuesta_4 == "b" or respuesta_4 == "B":
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 elif respuesta_4 == "c" or respuesta_4 == "C":
    puntaje += 5
    print(YELLOW+"Respuesta correcta. Excelente!"+RESET)
 else:
    puntaje -=2
    print(YELLOW+"Respuesta incorrecta."+RESET)
 print(BLACK+"Tu puntaje hasta ahora es: ",puntaje,"puntos"+RESET)
 time.sleep(3)

 if puntaje<15:
  print(GREEN+"A continuación, para que puedas subir tu puntaje te aparecerá ALEATORIAMENTE un número entero del 0 al 5, el cual indicará el nivel de dificultad de la pregunta que te tocará, siendo 0 el nivel de la pregunta más fácil y 5 la de la más difícil. OJO: Las preguntas son de historia del Perú. Suerte!"+RESET)
  numero = rnd.randint(0,5)
  time.sleep(6)
  for i in range(5,0,-1):
    print(i)
    time.sleep(1)
  print("\nEl número que te toca es: ",numero)
  time.sleep(5)
  if numero == 0:
    print(RED+"¿Quién proclamó la independencia del Perú?"+RESET)
    time.sleep(3)
    print(BLUE+"a) José de San Martín")
    print("b) Simón Bolivar")
    print("c) Ricardo Palma")
    print("d) Francisco Bolognesi"+RESET)
    rpta_0 = input("\nTu respuesta: ")
    while rpta_0 not in ("a","A","b","B","c","C","d","D"):
     rpta_0 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
    if rpta_0 == "a" or rpta_0 == "A":
     puntaje +=5
     print(YELLOW+"Respuesta correcta. Bien hecho!"+RESET)
    elif rpta_0 == "b" or rpta_0 == "B":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_0 == "c" or rpta_0 == "C":
     puntaje -= 5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    else:
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta. Excelente!"+RESET)
    time.sleep(3)
    print(MAGENTA+"Gracias,",nombre,",por jugar mi trivia, lograste alcanzar", puntaje," puntos."+RESET)
  elif numero == 1:
    print(RED+"Peruano que recibió el premio nobel de literatura en el 2010: "+RESET)
    time.sleep(3)
    print(BLUE+"a) Gabriela Mistral")
    print("b) Abraham Valdelomar")
    print("c) Mario Vargas Llosa")
    print("d) Ernest Hemingway"+RESET)
    rpta_1 = input("\nTu respuesta: ")
    while rpta_1 not in ("a","A","b","B","c","C","d","D"):
     rpta_1 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
    if rpta_1 == "a" or rpta_1 == "A":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_1 == "b" or rpta_1 == "B":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_1 == "c" or rpta_1 == "C":
     puntaje += 5
     print(YELLOW+"Respuesta correcta. Excelente!"+RESET)
    else:
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    time.sleep(3)
    print(MAGENTA+"Gracias,",nombre,",por jugar mi trivia, lograste alcanzar", puntaje," puntos."+RESET)

  elif numero == 2:
    print(RED+"¿Quién es el héroe de la aviación peruana?"+RESET)
    time.sleep(3)
    print(BLUE+"a) Alfonso Ugarte ")
    print("b) José Abelardo Quiñones")
    print("c) Agustín Gamarra")
    print("d) José Olaya"+RESET)
    rpta_2 = input("\nTu respuesta: ")
    while rpta_2 not in ("a","A","b","B","c","C","d","D"):
     rpta_2 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
    if rpta_2 == "a" or rpta_2 == "A":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_2 == "b" or rpta_2 == "B":
     puntaje +=5
     print(YELLOW+"Respuesta correcta. Bien hecho!"+RESET)
    elif rpta_2 == "c" or rpta_2 == "C":
     puntaje -= 5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    else:
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    time.sleep(3)
    print(MAGENTA+"Gracias,",nombre,",por jugar mi trivia, lograste alcanzar", puntaje," puntos."+RESET)

  elif numero == 3:
    print(RED+"¿A qué cultura preincaica del Perú perteneció el 'señor de Sipán'?"+RESET)
    time.sleep(3)
    print(BLUE+"a) Chavín")
    print("b) Nazca")
    print("c) Mochica")
    print("d) Paracas"+RESET)
    rpta_3 = input("\nTu respuesta: ")
    while rpta_3 not in ("a","A","b","B","c","C","d","D"):
     rpta_3 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
    if rpta_3 == "a" or rpta_3 == "A":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_3 == "b" or rpta_3 == "B":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_3 == "c" or rpta_3 == "C":
     puntaje += 5
     print(YELLOW+"Respuesta correcta. Excelente!"+RESET)
    else:
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    time.sleep(3)
    print(MAGENTA+"Gracias,",nombre,",por jugar mi trivia, lograste alcanzar", puntaje," puntos."+RESET)


  elif numero == 4:
    print(RED+"¿Qué héroe peruano fue llamado 'El brujo de los andes'"+RESET)
    time.sleep(3)
    print(BLUE+"a) Ramón Castilla")
    print("b) Mariano Melgar")
    print("c) Miguel Grau")
    print("d) Andrés Avelino Cáceres"+RESET)
    rpta_4 = input("\nTu respuesta: ")
    while rpta_4 not in ("a","A","b","B","c","C","d","D"):
     rpta_4 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
    if rpta_4 == "a" or rpta_4 == "A":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_4 == "b" or rpta_4 == "B":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_4 == "c" or rpta_4 == "C":
     puntaje -= 5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    else:
     puntaje +=5
     print(YELLOW+"Respuesta correcta. Excelente!"+RESET)
    time.sleep(3)
    print(MAGENTA+"Gracias,",nombre,",por jugar mi trivia, lograste alcanzar", puntaje," puntos."+RESET)

  else:
    print(RED+"¿Quién fue el primer virrey del Perú?"+RESET)
    time.sleep(3)
    print(BLUE+"a) José Fernando de Abascal")
    print("b) Agustín de Jáuregui")
    print("c) Francisco de Toledo")
    print("d) Blasco Núñez de Vela"+RESET)
    rpta_5 = input("\nTu respuesta: ")
    while rpta_5 not in ("a","A","b","B","c","C","d","D"):
     rpta_5 = input("Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
    if rpta_5 == "a" or rpta_5 == "A":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_5 == "b" or rpta_5 == "B":
     puntaje -=5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    elif rpta_5 == "c" or rpta_5 == "C":
     puntaje -= 5
     print(YELLOW+"Respuesta incorrecta."+RESET)
    else:
     puntaje +=5
     print(YELLOW+"Respuesta correcta. Excelente!"+RESET)
    time.sleep(3)
    print(MAGENTA+"Gracias,",nombre,",por jugar mi trivia, lograste alcanzar", puntaje," puntos."+RESET)

 else:
  print(CYAN+"Gracias,",nombre,",por jugar mi trivia, lograste alcanzar", puntaje," puntos."+RESET)
 
 print(RED+"¿Deseas intentar la trivia nuevamente?"+RESET)  
 repetir_trivia = input("Ingresa 'si' para repetirlo o cualquier otra tecla para finalizar: ").lower()
 if repetir_trivia != "si":
     print(BLUE+"\nEspero que lo hayas pasado bien,",nombre,".Hasta pronto!"+RESET)
     iniciar_trivia = False



