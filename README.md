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
    # Получите ввод от пользователя и разделите его на список чисел
    numbers = entry.get().split()

    # Initialize the result to 0
    result = 0

    # Iterate over each number in the list
    for number in numbers:
        # Convert the number to an integer and add it to the result
        number = int(number)
        result += number

        # Update the label with the current sum
        label.config(text=f"Сумма чисел - {result}")


# Create the main window
root = tk.Tk()
root.title("Cyммa чисел")  # Set the title of the window
root.geometry("500x300")  # Set the size of the window

# Create a label to display the instructions
label = tk.Label(root, font=("Arial", 14), text="Введите через пробел")
label.pack()  # Add the label to the window

# Create an entry field for the user to input numbers
entry = tk.Entry(root)
entry.delete(0, tk.END)  # Очистить поле ввода
entry.pack()  # Добавьте поле ввода в окно

# Create a button to trigger the sum calculation
button = tk.Button(root, font=("Arial", 14), text="Пocчитать сумму", command=my_summa)
button.pack()  # Добавьте кнопку в окно

# Start the main event loop
root.mainloop()

```
