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
                zindow.geometry("500x700")

                beton1 = Label(zindow, text="Bestandteile",
                               font=("Times New Roman", 15))
                zmnt = Button(zindow, text="Zement", font=(
                    "Times New Roman", 11), padx=27, command=clicked4g)
                wasser = Button(zindow, text="Wasser",
                                font=("Times New Roman", 11), padx=27)
                gstkrn = Button(zindow, text="Gesteinskörnung",
                                font=("Times New Roman", 11))
                zusatzst = Button(zindow, text="Zusatzstoffe",
                                  font=("Times New ROman", 11), padx=13)
                zusatzmttl = Button(zindow, text="Zusatzmittel",
                                    font=("Times New Roman", 11), padx=14)
                stahlf = Button(zindow, text="Stahlfassern",
                                font=("Times New Roman", 11), padx=13)
                beton2 = Label(zindow, text="\nMischverhältnis",
                               font=("Times New Roman", 15))
                mischverhaeltnis = Label(zindow, text="Die korrekte Zuordnung des Bauteiles/Bauwerkes zu Expositionsklassen,\n je nach Umgebungsbedingungen ist\n eine wichtige Voraussetzung für die Zusammensetzung des Betons.\n In Abhängigkeit der zu erwartenden Beanspruchungen, die auf das Bauteil wirken,\n werden in den Expositionsklassen Anforderungen vorgegeben.", font=("Times New Roman", 11))
                TdE = Button(zindow, text="Tabelle der Expositionsklassen", font=(
                    "Times New Roman", 11))
                beton3 = Label(zindow, text="\nProzessstufen bei der Herstellung", font=(
                    "Times New Roman", 15))
                PbdH = Label(
                    zindow, text="1. Herstellen(Mischen) im Transportbetonwerk\n2. Befördern im Fahrmischer\n3. Frischbeton ausbreiten\n4. Nachbehandeln (mit Wasser oder Nachbehandlungsmitteln) um das\nTrocknen zu verhindern -> Beton härtet, d.h chem. Reaktionen finden statt\n5. Festbeton ausschalen", font=("Times New Roman", 11))
                beton4 = Label(zindow, text="\nStruktur und Eigenschaften", font=(
                    "Times New Roman", 15))
                SuE = Label(
                    zindow, text="Zement + Wasser -> CSH-Phasen + Portlandit\n3CaO + SiO2(Alit) + H2O -> Ca(OH)2\n2CaO + SiO2(Belit) + H20\n\nhohe Druckfestigkeit, dicht,wasserbeständig\nKapillarporen ->Frostprobleme, keine Dauerhaftigkeit", font=("Times New Roman", 11))

                beton1.pack()
                zmnt.pack()
                wasser.pack()
                gstkrn.pack()
                zusatzst.pack()
                zusatzmttl.pack()
                stahlf.pack()
                beton2.pack()
                mischverhaeltnis.pack()
                TdE.pack()
                beton3.pack()
                PbdH.pack()
                beton4.pack()
                SuE.pack()
                zindow.mainloop()

            def clicked4b():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Gips")
                zindow.geometry("500x500")

                gips1 = Label(zindow, text="Vorkommen",
                              font=("Times New Roman", 15))
                gips2 = Label(zindow, text="\nStruktur und Eigenschaften", font=(
                    "Times New Roman", 15))

                gips1.pack()
                gips2.pack()

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
                "Times New Roman", 15), padx=100, pady=50)
            lf4.grid(column=0, row=0)
            Beton = Button(lf4, text="Beton", font=(
                "Times New Roman", 11), padx=17, command=clicked4a)
            Gips = Button(lf4, text="Gips", font=(
                "Times New Roman", 11), padx=21, command=clicked4b)
            Glas = Button(lf4, text="Glas", font=(
                "Times New Roman", 11), padx=21, command=clicked4c)
            Kalk = Button(lf4, text="Kalk", font=(
                "Times New Roman", 11), padx=20, command=clicked4d)
            Lehm = Button(lf4, text="Lehm", font=(
                "Times New Roman", 11), padx=18, command=clicked4e)
            Naturstein = Button(lf4, text="Naturstein", font=(
                "Times New Roman", 11), padx=5, command=clicked4f)
            Zement = Button(lf4, text="Zement", font=(
                "Times New Roman", 11), padx=14, command=clicked4g)
            Ziegelstein = Button(lf4, text="Ziegelstein", font=(
                "Times New Roman", 11), padx=3, command=clicked4h)
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
