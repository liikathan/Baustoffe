import tkinter as tk
from tkinter import ttk
from mineralisch import *
from organisch import *
from grundlagen import ano


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


def metall(window=None):
    window = neuesFensters(window)

    lf4 = tk.LabelFrame(window, text="Wähle einen Baustoff", font=(
        "Times New Roman", 15), padx=100, pady=50)
    lf4.grid(column=0, row=0)
    Aluminium = tk.Button(lf4, text="Aluminium", font=(
        "Times New Roman", 11), padx=9, command=lambda: aluminium(window)).pack()
    Kupfer = tk.Button(lf4, text="Kupfer", font=(
        "Times New Roman", 11), padx=20, command=lambda: kupfer(window)).pack()
    Stahl = tk.Button(lf4, text="Stahl", font=(
        "Times New Roman", 11), padx=26, command=lambda: stahl(window)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: ano(window)).grid(column=0, row=1)


def stahl(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    v1 = tk.Label(scrollbar.scrollable_frame, text="Überschrift 1", font=(
        "Times New Roman", 15)).pack()
    v2 = tk.Label(scrollbar.scrollable_frame, text="Text1", font=(
        "Times New Roman", 11)).pack()
    v3 = tk.Label(scrollbar.scrollable_frame,
                  text="Überschrift 2", font=("Times New Roman", 15)).pack()
    v4 = tk.Label(scrollbar.scrollable_frame,
                  text="Text2", font=("Times New Roman", 11)).pack()
    v5 = tk.Label(scrollbar.scrollable_frame,
                  text="Überschrift 3", font=("Times New Roman", 15)).pack()
    v6 = tk.Label(scrollbar.scrollable_frame, text="Text 3",
                  font=("Times New Roman", 11)).pack()
    v7 = tk.Label(scrollbar.scrollable_frame, text="Überschrift 4", font=(
        "Times New Roman", 15)).pack()
    v8 = tk.Label(scrollbar.scrollable_frame,
                  text="Text 4", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: metall(window)).pack()

    scrollbar.pack()


def aluminium(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    v1 = tk.Label(scrollbar.scrollable_frame, text="Überschrift 1", font=(
        "Times New Roman", 15)).pack()
    v2 = tk.Label(scrollbar.scrollable_frame, text="Text1", font=(
        "Times New Roman", 11)).pack()
    v3 = tk.Label(scrollbar.scrollable_frame,
                  text="Überschrift 2", font=("Times New Roman", 15)).pack()
    v4 = tk.Label(scrollbar.scrollable_frame,
                  text="Text2", font=("Times New Roman", 11)).pack()
    v5 = tk.Label(scrollbar.scrollable_frame,
                  text="Überschrift 3", font=("Times New Roman", 15)).pack()
    v6 = tk.Label(scrollbar.scrollable_frame, text="Text 3",
                  font=("Times New Roman", 11)).pack()
    v7 = tk.Label(scrollbar.scrollable_frame, text="Überschrift 4", font=(
        "Times New Roman", 15)).pack()
    v8 = tk.Label(scrollbar.scrollable_frame,
                  text="Text 4", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: metall(window)).pack()

    scrollbar.pack()


def kupfer(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    v1 = tk.Label(scrollbar.scrollable_frame, text="Überschrift 1", font=(
        "Times New Roman", 15)).pack()
    v2 = tk.Label(scrollbar.scrollable_frame, text="Text1", font=(
        "Times New Roman", 11)).pack()
    v3 = tk.Label(scrollbar.scrollable_frame,
                  text="Überschrift 2", font=("Times New Roman", 15)).pack()
    v4 = tk.Label(scrollbar.scrollable_frame,
                  text="Text2", font=("Times New Roman", 11)).pack()
    v5 = tk.Label(scrollbar.scrollable_frame,
                  text="Überschrift 3", font=("Times New Roman", 15)).pack()
    v6 = tk.Label(scrollbar.scrollable_frame, text="Text 3",
                  font=("Times New Roman", 11)).pack()
    v7 = tk.Label(scrollbar.scrollable_frame, text="Überschrift 4", font=(
        "Times New Roman", 15)).pack()
    v8 = tk.Label(scrollbar.scrollable_frame,
                  text="Text 4", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: metall(window)).pack()

    scrollbar.pack()
