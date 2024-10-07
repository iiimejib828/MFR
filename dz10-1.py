import tkinter as tk

# Добавление задачи в список
def add_task():
    task = task_entry.get()  # Получаем текст из поля для ввода
    if task:
        task_listBox.insert(tk.END, task)  # Вставляем задачу в конец списка
        task_entry.delete(0, tk.END)  # Очищаем поле ввода

# Удаление выбранной задачи
def delete_task():
    selected_tasks = task_listBox.curselection()  # Получаем кортеж с индексами выбранных задач
    for index in reversed(selected_tasks):  # Проходим по выбранным индексам (обратно, чтобы корректно удалять)
        task_listBox.delete(index)  # Удаляем задачу из списка

# Отметить задачу как выполненную
def mark_task():
    selected_tasks = task_listBox.curselection()  # Получаем кортеж с индексами выбранных задач
    for index in selected_tasks:
        task_listBox.itemconfig(index, {'bg': 'slate blue', 'fg': 'white'})  # Меняем цвет фона и текста
        task_listBox.select_clear(index)  # Снимаем выделение после изменения

# Настройка окна приложения
root = tk.Tk()
root.title("Task list")
root.configure(background="azure3")

# Текстовый лейбл
text1 = tk.Label(root, text="Введите вашу задачу:", bg="azure3")
text1.pack(pady=5)

# Поле для ввода задачи
task_entry = tk.Entry(root, width=30, bg="aquamarine3")
task_entry.pack(pady=10)

# Frame для горизонтального расположения кнопок
button_frame = tk.Frame(root, bg="azure3")
button_frame.pack(pady=10)

# Кнопка для добавления задачи
add_task_button = tk.Button(button_frame, text="Добавить задачу", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=5)  # Кнопки идут горизонтально

# Кнопка для удаления задачи
delete_button = tk.Button(button_frame, text="Удалить задачу", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Кнопка для отметки выполнения задачи
mark_button = tk.Button(button_frame, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(side=tk.LEFT, padx=5)

# Текстовый лейбл
text2 = tk.Label(root, text="Список задач:", bg="azure3")
text2.pack(pady=5)

# Список задач (Listbox)
task_listBox = tk.Listbox(root, height=10, width=50, bg="aquamarine3", selectmode=tk.MULTIPLE)  # Множественный выбор
task_listBox.pack(pady=10)

# Запуск основного цикла Tkinter
root.mainloop()
