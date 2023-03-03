import tkinter as tk
from math import sqrt


class Calculator:
    def __init__(self, master: tk.Tk):
        self.a = tk.Entry(master)
        self.a.pack()
        self.b = tk.Entry(master)
        self.b.pack()
        self.c = tk.Entry(master)
        self.c.pack()
        self.output_label = tk.Label(master)
        self.output_label.pack()
        self.calculate_button = tk.Button(master, text="Вычислить", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        try:
            a, b, c = int(self.a.get()), int(self.b.get()), int(self.c.get()),
        except ValueError:
            self.output_label.config(text="Error")
            return
        d = b * b - 4 * a * c
        if d < 0:
            self.output_label.config(text="Нет корней")
            return
        roots = {(-b - sqrt(d)) / 2*a, (-b + sqrt(d)) / 2*a}
        if len(roots) == 2:
            n1, n2 = sorted(roots)
            self.output_label.config(text=f"Корни: {n1}; {n2}")
        else:
            n = roots.pop()
            self.output_label.config(text=f"Корень: {n}")


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

