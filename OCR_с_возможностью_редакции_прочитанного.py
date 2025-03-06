import easyocr
import tkinter as tk
from tkinter import scrolledtext, messagebox

def load_text():
    """Загружает текст для редактирования."""
    extracted_text = "Это пример текста, который пользователь может редактировать."
    text_area.delete(1.0, tk.END)  # Очищаем текстовое поле
    text_area.insert(tk.END, extracted_text)  # Вставляем текст

def save_text():
    """Сохраняет измененный текст и закрывает окно."""
    edited_text = text_area.get(1.0, tk.END)  # Получаем текст из текстового поля
    # Здесь можно добавить код для сохранения текста в файл или базе данных
    messagebox.showinfo("Сохранение", "Текст успешно сохранен!")
    root.destroy()

def split_questions_and_answers(text):
    """
    Функция для разделения текста на вопросы и ответы.
    """
    # Разделяем текст по слову "Вопрос"
    question_parts = text.split("Вопрос:")

    # Список для хранения вопросов и ответов
    qa_pairs = []

    for part in question_parts[1:]:  # Пропускаем первую часть, так как она пустая
        # Разделяем по слову "Ответ"
        answer_parts = part.split("Ответ:")
        question = answer_parts[0].strip()  # Вопрос
        answer = answer_parts[1].strip() if len(answer_parts) > 1 else ""  # Ответ (если есть)

        # Добавляем пару вопрос-ответ в список
        qa_pairs.append((question, answer))

    return qa_pairs

def save_to_text_file(qa_pairs, output_file):
    """
    Функция для сохранения вопросов и ответов в текстовый файл.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for i, (question, answer) in enumerate(qa_pairs, start=1):
            file.write(f"Вопрос {i}: {question}\n")
            file.write(f"Ответ {i}: {answer}\n\n")
    print(f"Результаты успешно сохранены в файл: {output_file}")


# Создание экземпляра EasyOCR
reader = easyocr.Reader(['ru'])  # Укажите язык, например, 'ru' для русского

# Путь к изображению
image_path = 'Фото.png'

# Выполнение OCR непосредственно из файла
results = reader.readtext(image_path)

# Извлечение и вывод текста
extracted_text = ""
for (bbox, text, prob) in results:
    extracted_text += text + ' '  # Используем перенос строки для разделения

print("Распознанный текст:")
print(extracted_text)

# Разделяем вопросы и ответы
qa_pairs = split_questions_and_answers(extracted_text)

# Вывод результатов в консоль
for i, (question, answer) in enumerate(qa_pairs, start=1):
    print(f"Вопрос {i}: {question}")
    print(f"Ответ {i}: {answer}\n")

# Сохраняем результаты в текстовый файл
output_file = "результаты.txt"
save_to_text_file(qa_pairs, output_file)


# Создаем главное окно
root = tk.Tk()
root.title("Редактор текста")

# Создаем область для многострочного текста
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
text_area.pack(padx=10, pady=10)

# Кнопка загрузки текста
load_button = tk.Button(root, text="Загрузить текст", command=load_text)
load_button.pack(pady=5)

# Кнопка сохранения текста
save_button = tk.Button(root, text="Сохранить текст", command=save_text)
save_button.pack(pady=5)

# Запускаем главный цикл приложения
root.mainloop()

