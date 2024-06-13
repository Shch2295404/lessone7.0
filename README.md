# lessone7.0

```python
import tkinter as tk


def my_summa():
    """
    Вычисляет сумму чисел, введенных пользователем.

    Эта функция получает ввод от пользователя, разбивает его на список чисел,
    преобразует каждое число в целое и вычисляет сумму. Затем результат
    выводится на экран в виде ярлыка.
    """
    # Получаем ввод от пользователя и разделите его на список чисел
    numbers = entry.get().split()

    # Инициализируем результат в 0
    result = 0

    # Итерация по каждому числу в списке
    for number in numbers:
        # Преобразуйем число в целое и добавьте его к результату
        number = int(number)
        result += number

        # Обновление метки с текущей суммой
        label.config(text=f"Сумма чисел - {result}")


# Создание главного окна
root = tk.Tk()
root.title("Cyммa чисел")  # Set the title of the window
root.geometry("500x300")  # Set the size of the window

# Создаем метку для отображения инструкций
label = tk.Label(root, font=("Arial", 14), text="Введите через пробел")
label.pack()  # Add the label to the window

# Создаем поле для ввода чисел
entry = tk.Entry(root)
entry.delete(0, tk.END)  # Очистить поле ввода
entry.pack()  # Добавьте поле ввода в окно

# Создаем кнопку для запуска вычисления суммы
button = tk.Button(root, font=("Arial", 14), text="Пocчитать сумму", command=my_summa)
button.pack()  # Добавить кнопку в окно

# Запускаем основной цикл обработки событий
root.mainloop()

```
