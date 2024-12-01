# Питання від першого студента
first_student_surname = "Самков"
question_for_next_student = "Що таке список у Python і як з ним працювати?"

file_name = "students_questions.txt"

try:
    # Відкриваємо файл для запису. Якщо файл не існує, він буде створений.
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"Студент: {first_student_surname}\n")
        file.write(f"Запитання: {question_for_next_student}\n")
    print("Файл успішно створено та записано.")
except Exception as e:
    # Обробка можливих помилок під час роботи з файлом
    print(f"Виникла помилка під час запису у файл: {e}")

# Сідельнік Юлія, КН-31
file_name = "students_questions.txt"

# Перший студент додає своє питання
first_student_surname = "Самков"
question_for_next_student = "Що таке список у Python і як з ним працювати?"

try:
    # Створення нового текстового файлу та запис першого питання
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"Студент: {first_student_surname}\n")
        file.write(f"Запитання: {question_for_next_student}\n")
    print("Файл успішно створено та записано.")
except Exception as e:
    # Обробка можливих помилок
    print(f"Виникла помилка під час запису у файл: {e}")

# Другий студент додає відповідь на попереднє питання та своє питання
second_student_surname = "Святішенко"
answer_for_previous_question = ("Список у Python — це змінний впорядкований контейнер "
                                "для зберігання елементів будь-якого типу. Основні операції: "
                                "створення, додавання, видалення, перебір.")
question_for_next_student = "Що таке кортеж у Python і чим він відрізняється від списку?"

try:
    # Відкриття існуючого файлу для додавання нових даних
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"Студент: {second_student_surname}\n")
        file.write(f"Відповідь: {answer_for_previous_question}\n")
        file.write(f"Запитання: {question_for_next_student}\n")
    print("Файл успішно змінено.")
except Exception as e:
    # Обробка можливих помилок
    print(f"Виникла помилка під час запису у файл: {e}")
