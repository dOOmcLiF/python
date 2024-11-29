import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
import numpy as np

class Athlete:
    def __init__(self, name, sport, age, weight, height, achievements):
        self.name = name
        self.sport = sport
        self.age = int(age)
        self.weight = float(weight)
        self.height = float(height)
        self.achievements = achievements

class SportApp:
    def __init__(self, master):
        self.master = master
        master.title("Управление спортсменами")
        master.geometry("800x600")

        # Список спортсменов
        self.athletes = []

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Фрейм для кнопок управления
        control_frame = tk.Frame(self.master)
        control_frame.pack(pady=10, fill='x')

        # Кнопки управления
        tk.Button(control_frame, text="Загрузить", command=self.load_file).pack(side='left', padx=5)
        tk.Button(control_frame, text="Добавить", command=self.add_athlete).pack(side='left', padx=5)
        tk.Button(control_frame, text="Сохранить", command=self.save_file).pack(side='left', padx=5)
        tk.Button(control_frame, text="Статистика", command=self.show_statistics).pack(side='left', padx=5)

        # Фрейм для сортировки и фильтрации
        filter_frame = tk.Frame(self.master)
        filter_frame.pack(pady=10, fill='x')

        # Выпадающий список для выбора признака сортировки
        tk.Label(filter_frame, text="Сортировка:").pack(side='left', padx=5)
        self.sort_var = tk.StringVar()
        sort_options = ["Имя", "Возраст", "Вес", "Рост"]
        self.sort_combo = ttk.Combobox(filter_frame, textvariable=self.sort_var, values=sort_options)
        self.sort_combo.pack(side='left', padx=5)

        # Радиокнопки для порядка сортировки
        self.sort_order = tk.StringVar(value="ascending")
        tk.Radiobutton(filter_frame, text="По возрастанию", variable=self.sort_order, value="ascending").pack(side='left', padx=5)
        tk.Radiobutton(filter_frame, text="По убыванию", variable=self.sort_order, value="descending").pack(side='left', padx=5)
        tk.Button(filter_frame, text="Сортировать", command=self.sort_athletes).pack(side='left', padx=5)

        # Таблица
        self.tree = ttk.Treeview(self.master, columns=("Имя", "Вид спорта", "Возраст", "Вес", "Рост", "Достижения"), show="headings")
        self.tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Настройка колонок
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')

    def load_file(self):
        filename = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV файлы", "*.csv")])
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader)  # Пропуск заголовков
                    self.athletes = [Athlete(*row) for row in reader]
                self.update_table()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")

    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV файлы", "*.csv")])
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Имя", "Вид спорта", "Возраст", "Вес", "Рост", "Достижения"])
                    for athlete in self.athletes:
                        writer.writerow([athlete.name, athlete.sport, athlete.age, athlete.weight, athlete.height, athlete.achievements])
                messagebox.showinfo("Успех", "Данные сохранены")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

    def add_athlete(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Добавление спортсмена")
        add_window.geometry("400x300")

        # Поля ввода
        fields = ["Имя", "Вид спорта", "Возраст", "Вес", "Рост", "Достижения"]
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(add_window, text=field).grid(row=i, column=0, padx=10, pady=5)
            entries[field] = tk.Entry(add_window, width=30)
            entries[field].grid(row=i, column=1, padx=10, pady=5)

        def save_new_athlete():
            try:
                new_athlete = Athlete(
                    entries["Имя"].get(),
                    entries["Вид спорта"].get(),
                    entries["Возраст"].get(),
                    entries["Вес"].get(),
                    entries["Рост"].get(),
                    entries["Достижения"].get()
                )
                self.athletes.append(new_athlete)
                self.update_table()
                add_window.destroy()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Некорректные данные: {e}")

        tk.Button(add_window, text="Сохранить", command=save_new_athlete).grid(row=len(fields), column=1, pady=10)

    def update_table(self):
        # Очистка таблицы
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Заполнение таблицы
        for athlete in self.athletes:
            self.tree.insert('', 'end', values=(athlete.name, athlete.sport, athlete.age, athlete.weight, athlete.height, athlete.achievements))

    def sort_athletes(self):
        sort_key = self.sort_var.get()
        reverse = self.sort_order.get() == "descending"

        key_map = {
            "Имя": lambda x: x.name,
            "Возраст": lambda x: x.age,
            "Вес": lambda x: x.weight,
            "Рост": lambda x: x.height
        }

        if sort_key in key_map:
            self.athletes.sort(key=key_map[sort_key], reverse=reverse)
            self.update_table()
        else:
            messagebox.showwarning("Предупреждение", "Выберите признак сортировки")

    def show_statistics(self):
        stat_window = tk.Toplevel(self.master)
        stat_window.title("Статистика")
        stat_window.geometry("400x300")

        def calculate_stats(attr):
            values = [getattr(athlete, attr) for athlete in self.athletes]
            return {
                "min": min(values),
                "max": max(values),
                "mean": np.mean(values),
                "std": np.std(values)
            }

        stats_options = ["Возраст", "Вес", "Рост"]
        tk.Label(stat_window, text="Выберите признак:").pack(pady=10)
        stat_var = tk.StringVar()
        stat_combo = ttk.Combobox(stat_window, textvariable=stat_var, values=stats_options)
        stat_combo.pack(pady=10)

        result_text = tk.Text(stat_window, height=10, width=50)
        result_text.pack(pady=10)

        def show_selected_stats():
            selected = stat_var.get()
            key_map = {
                "Возраст": "age",
                "Вес": "weight",
                "Рост": "height"
            }
            if selected in key_map:
                stats = calculate_stats(key_map[selected])
                result_text.delete(1.0, tk.END)
                for key, value in stats.items():
                    result_text.insert(tk.END, f"{key}: {value:.2f}\n")

        tk.Button(stat_window, text="Рассчитать", command=show_selected_stats).pack(pady=10)

def main():
    root = tk.Tk()
    app = SportApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()