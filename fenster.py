import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Baustoffe")
window.geometry("500x500")


def clicked1():
    window.destroy()
    vindow = tk.Tk()
    vindow.title("Baustoffe")
    vindow.geometry("500x500")

    def clicked2a():
        vindow.destroy()
        xindow = tk.Tk()
        xindow.title("anorganische Baustoffe")
        xindow.geometry("500x500")

        def clicked3a():
            xindow.destroy()
            yindow = tk.Tk()
            yindow.title("metallische Baustoffe")
            yindow.geometry("500x500")

        def clicked3b():
            xindow.destroy()
            yindow = tk.Tk()
            yindow.title("mineralische Baustofe")
            yindow.geometry("500x500")

            def clicked4a():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Beton")
                zindow.geometry("500x500")

                beton1 = Label(zindow, text="Bestandteile",
                               font=("Times New Roman", 15), padx=10)
                beton2 = Label(zindow, text="Zement, Wasser, Gesteinskörnung, Zusatzstoffe, Zusatzmittel, Stahlfasern", font=(
                    "Times New Roman", 11))

                beton1.pack()
                beton2.pack()
                zindow.mainloop()

            def clicked4b():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Gips")
                zindow.geometry("500x500")

            def clicked4c():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Glas")
                zindow.geometry("500x500")

            def clicked4d():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Kalk")
                zindow.geometry("500x500")

            def clicked4e():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Lehm")
                zindow.geometry("500x500")

            def clicked4f():
                yindow.destroy()
                zindow = tk.TK()
                zindow.title("Naturstein")
                zindow.geometry("500x500")

            def clicked4g():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Zement")
                zindow.geometry("500x500")

            def clicked4h():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Ziegelstein")
                zindow.geometry("500x500")

            lf4 = LabelFrame(yindow, text="Wähle einen Baustoff", font=(
                "Times New Roman", 15), padx=75, pady=100)
            lf4.grid(column=0, row=0)
            Beton = Button(lf4, text="Beton", font=(
                "Times New Roman", 11), padx=17, command=clicked4a)
            Beton.grid(column=0, row=0)
            Gips = Button(lf4, text="Gips", font=(
                "Times New Roman", 11), padx=21, command=clicked4b)
            Gips.grid(column=1, row=0)
            Glas = Button(lf4, text="Glas", font=(
                "Times New Roman", 11), padx=21, command=clicked4c)
            Glas.grid(column=0, row=1)
            Kalk = Button(lf4, text="Kalk", font=(
                "Times New Roman", 11), padx=20, command=clicked4d)
            Kalk.grid(column=1, row=1)
            Lehm = Button(lf4, text="Lehm", font=(
                "Times New Roman", 11), padx=18, command=clicked4e)
            Lehm.grid(column=0, row=2)
            Naturstein = Button(lf4, text="Naturstein", font=(
                "Times New Roman", 11), padx=2, command=clicked4f)
            Naturstein.grid(column=1, row=2)
            Zement = Button(lf4, text="Zement", font=(
                "Times New Roman", 11), padx=12, command=clicked4g)
            Zement.grid(column=0, row=3)
            Ziegelstein = Button(lf4, text="Ziegelstein", font=(
                "Times New Roman", 11), command=clicked4h)
            Ziegelstein.grid(column=1, row=3)

            Beton.pack()
            Gips.pack()
            Glas.pack()
            Kalk.pack()
            Lehm.pack()
            Naturstein.pack()
            Zement.pack()
            Ziegelstein.pack()
            yindow.mainloop()

        lf3 = LabelFrame(xindow, text="mineralisch oder metallisch", font=(
            "Times New Roman", 15), padx=75, pady=100)
        lf3.grid(column=0, row=0)
        mineralisch = Button(lf3, text="mineralischer Baustoff", font=(
            "Times New Roman", 11), padx=7, command=clicked3b)
        metallisch = Button(lf3, text="metallischer Baustoff", font=(
            "Times New Roman", 11), padx=10, command=clicked3a)

        mineralisch.pack()
        metallisch.pack()
        xindow.mainloop()

    def clicked2b():
        vindow.destroy()
        xindow = tk.Tk()
        xindow.title("organische Baustoffe")
        xindow.geometry("500x500")

    lf2 = LabelFrame(vindow, text="organisch oder anorganisch",
                     font=("Times New Roman", 15), padx=75, pady=100)
    lf2.grid(column=0, row=0)
    organisch = Button(lf2, text="organischer Baustoff",
                       font=("Times New Roman", 11), padx=16, command=clicked2b)
    anorganisch = Button(lf2, text="anorganischer Baustoff",
                         font=("Times New Roman", 11), padx=10, command=clicked2a)

    organisch.pack()
    anorganisch.pack()
    vindow.mainloop()


lf1 = LabelFrame(window, text="Baustoffe", font=("Times New Roman", 15))
lf1.grid(column=0, row=0)
Inhalt = "Die Natur bietet dem Menschen *Naturstoffe*.\n Diese werden zu *Rohstoffen*,\n wenn sie durch menschliche Arbeit gewonnen werden\n (bsp.Erze/ Kies).\n Bearbeitet man die Rohstoffe industriell,\n so werden sie zu *Werkstoffen*.\n Werkstoffe, die in der Bauindustrie verwendet werden,\n bezeichnet man als *Baustoff*.\n Aus Baustoffen werden Bauwerke"
lbl1 = Label(lf1, text=Inhalt, font=(
    "Times New Roman", 11), width=45, height=15)
nxt = Button(lf1, text="weiter", font=(
    "Times New Roman", 11), command=clicked1)

lbl1.pack()
nxt.pack()

window.mainloop()
