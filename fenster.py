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
                    zindow, text="Zement + Wasser -> CSH-Phasen + Portlandit\n3CaO * SiO2(Alit) + H2O -> Ca(OH)2\n2CaO * SiO2(Belit) + H20\n\nhohe Druckfestigkeit, dicht,wasserbeständig\nKapillarporen ->Frostprobleme, keine Dauerhaftigkeit", font=("Times New Roman", 11))
                back = Button(zindow, text="Zurück", font=(
                    "Times New Roman", 11), command=clicked3b)

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
                back.pack()
                zindow.mainloop()

            def clicked4b():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Gips")
                zindow.geometry("500x600")

                gips1 = Label(zindow, text="Vorkommen",
                              font=("Times New Roman", 15))
                render = PhotoImage(
                    file="Rauchgasentschwefelung.gif")
                img = Label(zindow, image=render)
                img.image = render
                gips2 = Label(zindow, compound=BOTTOM, text="Natürliches Vorkommen\n\nIndustrielles Restprodukt (bei der Rauchgasentschwefelung)\nCalciumsulfit + Luft -> Calciumsulfat\n2 CaSO3 + O2 → 2 CaSO4", image=render, font=(
                    "Times New Roman", 11))
                gips3 = Label(zindow, text="\nStruktur und Eigenschaften", font=(
                    "Times New Roman", 15))
                gips4 = Label(zindow, text="CaSO4 * 2H2O\nBeim Brennen findet keine chemische Reaktion statt\nErhärten ist ein Kristallisationsvorgang (->CaSO4)",
                              font=("Times New Roman", 11))
                back = Button(yindow, text="Zurück", font=(
                    "Times New Roman", 11), command=clicked3b)

                gips1.pack()
                gips2.pack()
                gips3.pack()
                gips4.pack()
                back.pack()
                zindow.mainloop()

            def clicked4c():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Glas")
                zindow.geometry("500x600")

                render = PhotoImage(
                    file="floatglass.png")
                glas1 = Label(zindow, compound=BOTTOM, text="Herstellung", image=render, font=(
                    "Times New Roman", 15))
                glas2 = Label(zindow, text="\nVerwendung",
                              font=("Times New Roman", 15))
                glas3 = Label(
                    zindow, text="Fenster und zunehmend tragende Strukturen\n\nBauglas = Alkali-Silikat-Gläser\nFensterglas = Kalk-Natron- Glas", font=("Times New Roman", 11))
                glas4 = Label(zindow, text="\nStruktur und Eigenschaften", font=(
                    "Times New Roman", 15))
                glas5 = Label(
                    zindow, text="Sammelbegriff für alle amorphen Feststoffe\n->auch amorph erstarrte Metalle\n->teilweise organischen Ursprungs (bspw.Bernstein)\n\namorph -> unterkühlte zähe Flüssigkeit -> keine Nahordnung =/= kristallin\n\nHohe Lichtdruchlässigkeit\nSehr hohe Druckfestigkeit\nSehr spröde und schlagempfinglich\nähnlich hohe Dichte wie Beton", font=("Times New Roman", 11))

                glas1.pack()
                glas2.pack()
                glas3.pack()
                glas4.pack()
                glas5.pack()
                zindow.mainloop()

            def clicked4d():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Kalk")
                zindow.geometry("500x500")

                kalk1 = Label(zindow, text="Vorkommen und Zusammensetzung", font=(
                    "Times New Roman", 15))
                kkl = PhotoImage(file="kalkkreislauf.png")
                img = Label(zindow, image=kkl)
                img.image = kkl
                kalk2 = Label(zindow, compound=BOTTOM, text="Zement + Wasser -> CSH-Phasen + Portlandit\nPortlandit = Löschkalk (niedriger Ph-Wert)\nC3S/C2S + H20 -> CaO/SiO2/H20 + Ca(OH)2\n\nPortlandit->Kalkstein (hoher Ph-Wert)\nCa(OH)2 + CO2 + H2O -> CaCO3 + 2H2O", image=kkl, font=("Times New Roman", 11))
                kalk3 = Label(zindow, text="\nVerwendung",
                              font=("Times New Roman", 15))
                kalk4 = Label(
                    zindow, text="1.Als Bindemittel:\n- Putz\n- Mauermörtel\n- Bestandteil von Beton\n2.Zum Knochenaufbau\n3.Zum Bierbrauen", font=("Times New Roman", 11))

                kalk1.pack()
                kalk2.pack()
                kalk3.pack()
                kalk4.pack()

            def clicked4e():
                yindow.destroy()
                zindow = tk.Tk()
                zindow.title("Lehm")
                zindow.geometry("500x500")
                canvas_width = 500
                canvas_height = 850
                w = Canvas(zindow,
                           width=canvas_width,
                           height=canvas_height)
                s = Scrollbar(w)
                s.pack(side=RIGHT)
                # Ich kann da keine Höhe angeben, dann ist alles weg
                w.pack()

                lehm = PhotoImage(file="llehm.png")
                img = Label(zindow, image=lehm)
                img.image = lehm
                lehm1 = Label(w, text="Vorkommen und Zusammensetzung", font=(
                    "Times New Roman", 15))
                lehm2 = Label(w, compound=BOTTOM, text="Verwitterungsprodukt von Urgestein\nGemisch aus Ton, Wasser und Sand\nTon = Koalinit + Montmorillonit, Korngröße>=0,002mm",
                              image=lehm, font=("Times New Roman", 11))
                lehm3 = Label(
                    w, text="Wasser = fester Ton enthält grundsätzlich gebundenes Wasser\nSand = Sio2, Korngröße 0,06-2mm", font=("Times New Roman", 11))
                lehm4 = Label(w, text="\nEigenschaften",
                              font=("Times New Roman", 15))
                lehm5 = Label(w, text="Lehm ist ein mineralisches, bindigesm Lockergestein\nHydration von Ton = Ton wird durch Wasserzufuhr plastisch biegsam\n=\nLehm ist wasserempfindlich = wetterunbeständig\nLehm ist recyclebar (ohne Energiezufuhr\nLehm hat gute Sorptionseigenschaften (gesundes Raumklima)\nLehm ist en guter Wärmespeicher (Durch Zugabe von purösen Stoffen Warmedämmung gegeben (z.B Bims))", font=("Times New Roman", 11))
                lehm6 = Label(w, text="\nBauen mit Lehm",
                              font=("Times New Roman", 15))
                lehm7 = Label(w, text="Beginn des Lehmbau 5000 v. Chr.\nSchibam in Südjemen = älteste Hochhausstadt aus Lehmbauten\nTurm von Babel (7 Jhd v. Chr)\nChinesische Mauer (vor 400 Jahren)\nHeute lebt 1/3 der Menschheit in Lehmbauten\n\nLehmbautechniken zum Bau tragender Wände:\nStampflehmbau (Mithilfe von Schalungen)\nWellerbau (Schalungsloses Aufbauen der Wand u. Abtragen der Oberfläche\nLehmsteinbau (Ziegelsteinbau mit Luftgetrockneten Lehmbausteinen)\n\nAufgrund der Wasserbeständigkeit sind beim Bauen mit Lehm Wasserschutzmaßnahmen nötig", font=("Times New Roman", 11))

                s.config(command=w.yview)

                lehm1.pack()
                lehm2.pack()
                lehm3.pack()
                lehm4.pack()
                lehm5.pack()
                lehm6.pack()
                lehm7.pack()
                zindow.mainloop()

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

                zement2 = tk.Label(zindow, text="Zement ist ein anorganisches, fein gemalenes, hydraulisch wirkendes Bindemittel\nfür Mörtel und Beton\nMörtel: Gesteinskörnung <=4mm\nBeton: Gesteinskörnung >4mm", font=(
                    "Times New Roman", 11)).pack()

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
lbl1 = Label(lf1, text="Die Natur bietet dem Menschen Naturstoffe.\n Diese werden zu Rohstoffen,\n wenn sie durch menschliche Arbeit gewonnen werden\n (bsp.Erze/ Kies).\n Bearbeitet man die Rohstoffe industriell,\n so werden sie zu Werkstoffen.\n Werkstoffe, die in der Bauindustrie verwendet werden,\n bezeichnet man als Baustoff.\n Aus Baustoffen werden Bauwerke", font=(
    "Times New Roman", 11), width=45, height=15)
nxt = Button(lf1, text="weiter", font=(
    "Times New Roman", 11), command=clicked1)

lbl1.pack()
nxt.pack()

window.mainloop()
