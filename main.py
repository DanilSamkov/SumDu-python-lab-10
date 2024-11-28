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


# Відповідь та нове питання від другого студента

first_student_surname = "Святішенко"
answer_for_previous_question = "Список у Python — це змінний впорядкований контейнер для зберігання елементів будь-якого типу. Основні операції: створення, додавання, видалення, перебір"
question_for_next_student = "Що таке кортеж у Python і чим він відрізняється від списку?"

try:
    # Відкриваємо файл для запису. Якщо файл не існує, він буде створений.
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"Студент: {first_student_surname}\n")
        file.write(f"Відповідь: {answer_for_previous_question}\n")

        file.write(f"Студент: {first_student_surname}\n")
        file.write(f"Запитання: {question_for_next_student}\n")
    print("Файл успішно змінено.")
except Exception as e:
    # Обробка можливих помилок під час роботи з файлом
    print(f"Виникла помилка під час запису у файл: {e}")


# Відповідь та нове питання від третього студента (Ленди Микити)

third_student_surname = "Ленда"
answer_for_previous_question = "Кортеж у Python — це впорядкований, але незмінний набір елементів, що створюється за допомогою круглих дужок () і займає менше пам'яті, ніж список. На відміну від списків, які є змінними і дозволяють додавання, видалення та зміну елементів, кортежі використовуються для зберігання даних, які не потребують змін. Кортежі швидші в обробці, підходять для постійних даних і забезпечують доступ до елементів за індексом, як і списки."
question_for_next_student = "Що станеться, якщо спробувати змінити елемент кортежу в Python?"
try:
    # Відкриваємо файл для запису. Якщо файл не існує, він буде створений.
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"Студент: {third_student_surname}\n")
        file.write(f"Відповідь: {answer_for_previous_question}\n")
        file.write(f"Запитання: {question_for_next_student}\n")
    print("Файл успішно змінено.")
except Exception as e:
    # Обробка можливих помилок під час роботи з файлом
    print(f"Виникла помилка під час запису у файл: {e}")


