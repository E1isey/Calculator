import tkinter as tk
from math import sqrt


class Calculator:
    def __init__(self, master: tk.Tk):
        self.str1 = tk.StringVar()
        self.str1.trace_add("write", self.change_formula)
        self.str2 = tk.StringVar()
        self.str2.trace_add("write", self.change_formula)
        self.str3 = tk.StringVar()
        self.str3.trace_add("write", self.change_formula)

        for i in range(3):
            master.columnconfigure(i, weight=1)
        for i in range(3):
            master.rowconfigure(i, weight=1)

        self.formula_label = tk.Label(master)
        self.formula_label.grid(row=0, column=0, columnspan=3)

        frame_a = tk.Frame(master)
        tk.Label(frame_a, text="a").grid(row=0, column=0)
        self.a = tk.Entry(frame_a, textvariable=self.str1)
        self.a.grid(row=0, column=1)
        frame_a.grid(row=1, column=0)

        frame_b = tk.Frame(master)
        tk.Label(frame_b, text="b").grid(row=0, column=0)
        self.b = tk.Entry(frame_b, textvariable=self.str2)
        self.b.grid(row=0, column=1)
        frame_b.grid(row=1, column=1)

        frame_c = tk.Frame(master)
        tk.Label(frame_c, text="c").grid(row=0, column=0)
        self.c = tk.Entry(frame_c, textvariable=self.str3)
        self.c.grid(row=0, column=1)
        frame_c.grid(row=1, column=2)

        self.output_label = tk.Label(master)
        self.output_label.grid(row=2, column=0, columnspan=3)
        self.calculate_button = tk.Button(master, text="Вычислить", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=3)

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

    def change_formula(self, *args):
        try:
            a, b, c = int(self.a.get()), int(self.b.get()), int(self.c.get()),
        except ValueError:
            return
        self.formula_label.config(text=f"{a}x{chr(178)} {'-' if b < 0 else '+'} {abs(b)}x {'-' if c < 0 else '+'} {abs(c)} = 0")


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

