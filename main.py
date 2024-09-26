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