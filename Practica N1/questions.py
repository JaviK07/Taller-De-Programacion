import random
import sys

questions = [ # Preguntas para el juego
    "¿Que función se usa para obtener la longitud de una cadena en Python?",
    "¿Cual de las siguientes opciones es un número entero en Python?",
    "¿Como se solicita entrada del usuario en Python?",
    "¿Cual de las siguientes expresiones es un comentario válido en Python?",
    "¿Cual es el operador de comparación para verificar si dos valores son iguales?",
]

answers = [ # Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

correct_answers_index = [1, 2, 0, 3, 1] # Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
score = 0

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    question_index = random.randint(0, len(questions) - 1) # Se selecciona una pregunta aleatoria
    
    print(questions[question_index]) # Se muestra la pregunta y las respuestas posibles
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    for intento in range(2): # El usuario tiene 2 intentos para responder correctamente
        try: # Cláusula TRY-EXCEPT utilizado para capturar errores y que el programa pueda seguir su ejecucion según se desee.
            user_answer = int(input("Respuesta: ")) - 1
        except ValueError:
            print("Respuesta No Valida")
            sys.exit(1) # Modulo incluido en Python para finalizar con un programa en ejecución.
        
        if user_answer == correct_answers_index[question_index]: # Se verifica si la respuesta es correcta
            print("¡Correcto!")
            score += 1
            break
        elif user_answer >= 4 or user_answer < 0:
            print('Respuesta No Valida')
            sys.exit(1)
        else:
            score -= 0.5
            score = max(score, 0)
    else:
        print("Incorrecto. La respuesta correcta es:") # Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
        print(answers[question_index] [correct_answers_index[question_index]])

print('-------------------')            
print('SCORE:',score)
print('-------------------')            
print() # Se imprime un blanco al final de la pregunta
