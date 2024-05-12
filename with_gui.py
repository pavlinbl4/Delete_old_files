import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def delete_files_older_than(dir_path, extension, days):
    """
    Удаляет все файлы с определенным расширением из директории, которые старше указанного числа дней.
    """
    deleted_files = []

    # Получаем текущую дату и время
    now = datetime.now()
    # Расчитываем максимальную допустимую дату
    max_date = now - timedelta(days=days)

    # Перебираем файлы в директории
    for filename in os.listdir(dir_path):
        # Проверяем расширение файла
        if filename.endswith(extension):
            # Получаем время создания файла
            file_path = os.path.join(dir_path, filename)
            file_creation_time = os.path.getctime(file_path)
            file_creation_date = datetime.fromtimestamp(file_creation_time)

            # Проверяем, не старше ли файл максимальной даты
            if file_creation_date < max_date:
                # Удаляем файл и добавляем в список удаленных файлов
                os.remove(file_path)
                deleted_files.append(filename)

    return deleted_files


def main():
    # Создаем окно GUI
    root = tk.Tk()
    root.title("Удаление старых файлов")
    root.geometry("400x250")

    # Создаем поля ввода и ярлыки для них
    dir_label = tk.Label(root, text="Директория:")
    dir_label.grid(row=0, column=0, padx=10, pady=10)
    dir_entry = tk.Entry(root)
    dir_entry.grid(row=0, column=1, padx=10, pady=10)

    ext_label = tk.Label(root, text="Расширение:")
    ext_label.grid(row=1, column=0, padx=10, pady=10)
    ext_entry = tk.Entry(root)
    ext_entry.grid(row=1, column=1, padx=10, pady=10)

    days_label = tk.Label(root, text="Дни:")
    days_label.grid(row=2, column=0, padx=10, pady=10)
    days_entry = tk.Entry(root)
    days_entry.grid(row=2, column=1, padx=10, pady=10)

    # Функция для автоматического закрытия окна после выполнения
    def close_window():
        root.quit()
        root.destroy()

    # Кнопка для выбора директории
    def select_dir():
        dir_path = filedialog.askdirectory()
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, dir_path)

    dir_button = tk.Button(root, text="Выбрать", command=select_dir)
    dir_button.grid(row=0, column=2, padx=10, pady=10)

    # Кнопка для удаления файлов
    def delete_files():
        dir_path = dir_entry.get()
        extension = ext_entry.get()
        days = int(days_entry.get())
        deleted_files = delete_files_older_than(dir_path, extension, days)

        # Показываем сообщение с перечнем удаленных файлов
        show_message(deleted_files)

        close_window()

    delete_button = tk.Button(root, text="Удалить", command=delete_files)
    delete_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    # Функция для показа сообщения с перечнем удаленных файлов
    def show_message(deleted_files):
        message = "Удаленные файлы:\n" + "\n".join(deleted_files)
        messagebox.showinfo("Удаленные файлы", message)
    root.mainloop()

    # Задержка перед закрытием окна (например, 2 секунды)
    close_timeout = 2

    # Запуск функции закрытия через определенное время
    root.after(close_timeout * 1000, close_window)


if __name__ == "__main__":
    main()
