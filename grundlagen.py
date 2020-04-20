import tkinter as tk
from tkinter import ttk
from mineralisch import mineral
from metall import metall
from organisch import o


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, * args, **kwargs)
        tk.canvas = tk.Canvas(self)

        scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=tk.canvas.yview)
        self.scrollable_frame = ttk.Frame(tk.canvas)

        self.scrollable_frame.bind(
            "<Configure>", lambda e: tk.canvas.configure(scrollregion=tk.canvas.bbox("all")))

        tk.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw")

        tk.canvas.configure(yscrollcommand=scrollbar.set)

        tk.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def neuesFensters(altesFenster=None, geometry="500x500"):
    if not altesFenster == None:
        altesFenster.destroy()
    window = tk.Tk()
    window.title("Baustoffe")
    window.geometry(geometry)

    return window


def start(window=None):
    window = neuesFensters(window)

    lf1 = tk.LabelFrame(window, text="Baustoffe", font=("Times New Roman", 15))
    lf1.grid(column=0, row=0)
    lbl1 = tk.Label(lf1, text="Die Natur bietet dem Menschen Naturstoffe.\n Diese werden zu Rohstoffen,\n wenn sie durch menschliche Arbeit gewonnen werden\n (bsp.Erze/ Kies).\n Bearbeitet man die Rohstoffe industriell,\n so werden sie zu Werkstoffen.\n Werkstoffe, die in der Bauindustrie verwendet werden,\n bezeichnet man als Baustoff.\n Aus Baustoffen werden Bauwerke", font=(
        "Times New Roman", 11), width=45, height=15).pack()
    nxt = tk.Button(window, text="weiter", padx=86, font=(
        "Times New Roman", 11), command=lambda: select(window)).grid(column=0, row=1)
    grund = tk.Button(lf1, text="Grundlagen des Baustoffverhaltens", font=(
        "Times New Roman", 11), command=lambda: grundlagen(window)).pack()


def select(window=None):
    window = neuesFensters(window)

    lf2 = tk.LabelFrame(window, text="organisch oder anorganisch",
                        font=("Times New Roman", 15), padx=75, pady=100)
    lf2.grid(column=0, row=0)
    organisch = tk.Button(lf2, text="organischer Baustoff",
                          font=("Times New Roman", 11), padx=16, command=lambda: o(window)).pack()
    anorganisch = tk.Button(lf2, text="anorganischer Baustoff",
                            font=("Times New Roman", 11), padx=10, command=lambda: ano(window)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: start(window)).grid(column=0, row=1)


def ano(window=None):
    window = neuesFensters(window)

    lf3 = tk.LabelFrame(window, text="mineralisch oder metallisch", font=(
        "Times New Roman", 15), padx=75, pady=100)
    lf3.grid(column=0, row=0)
    mineralisch = tk.Button(lf3, text="mineralischer Baustoff", font=(
        "Times New Roman", 11), padx=7, command=lambda: mineral(window)).pack()
    metallisch = tk.Button(lf3, text="metallischer Baustoff", font=(
        "Times New Roman", 11), padx=10, command=lambda: metall(window)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: select(window)).grid(column=0, row=1)


def grundlagen(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: start(window)).pack()

    scrollbar.pack()


start()
tk.mainloop()
