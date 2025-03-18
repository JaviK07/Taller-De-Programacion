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

questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3) # zip agrupa en tuplas las preguntas, respuestas y respuestas correctas; list las hace accesibles a un bucle formandola en lista
#el parametro 'k' garantiza la cantidad de selecciones. 'Random.Choices' puede repetir preguntas en este caso. 'Random.Samples' hace que no se repitan las preguntas
# El usuario responde 3 preguntas seleccionadas
for question, answer_options, correct_index in questions_to_ask:
    print(question)
    for i, answer in enumerate(answer_options):
        print(f"{i + 1}. {answer}")

    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
        except ValueError:
            print("Respuesta No Valida")
            sys.exit(1)

        if user_answer >= 4 or user_answer < 0:
            print("Respuesta No Valida")
            sys.exit(1)

        if user_answer == correct_index:
            print("¡Correcto!")
            score += 1
            break
        else:
            score -= 0.5
            score = max(score, 0)
    else:
        print("Incorrecto. La respuesta correcta es:")
        print(answer_options[correct_index])

print('-------------------')
print('SCORE:', score)
print('-------------------')