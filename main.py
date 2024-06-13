import tkinter as tk

root = tk.Tk()
root.title("Первый ПРОЕКТ")
root.geometry("300x200")

label = tk.Label(root, font=("Arial", 12), text="Ввести свое имя : ")
label.pack()

text = ""
entry = tk.Entry(root)
entry.insert(0, text)
name = entry.get()
entry.pack()


def on_button_click():
    name_entry = entry.get()
    label.config(font=("Arial", 14), text="Привет, " + name_entry)
    entry.delete(0, tk.END)


button = tk.Button(root, text="Нажми меня!", command=on_button_click)
button.pack()

root.mainloop()