import tkinter as tk
from tkinter import ttk


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


def o(window=None):
    window = neuesFensters(window)

    lf4 = tk.LabelFrame(window, text="Wähle einen Baustoff", font=(
        "Times New Roman", 15), padx=100, pady=50)
    lf4.grid(column=0, row=0)
    Kunststoffe = tk.Button(lf4, text="Kunststoffe", font=(
        "Times New Roman", 11), padx=7, command=lambda: kunststoff(window)).pack()
    Holz = tk.Button(lf4, text="Holz", font=(
        "Times New Roman", 11), padx=28, command=lambda: holz(window)).pack()
    Bitumen = tk.Button(lf4, text="Bitumen", font=(
        "Times New Roman", 11), padx=17, command=lambda: bitumen(window)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: select(window)).grid(column=0, row=1)


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


def mineral(window=None):
    window = neuesFensters(window)
    lf4 = tk.LabelFrame(window, text="Wähle einen Baustoff", font=(
        "Times New Roman", 15), padx=100, pady=50)
    lf4.grid(column=0, row=0)
    Beton = tk.Button(lf4, text="Beton", font=(
        "Times New Roman", 11), padx=17, command=lambda: beton(window)).pack()
    Gips = tk.Button(lf4, text="Gips", font=(
        "Times New Roman", 11), padx=21, command=lambda: gips(window)).pack()
    Glas = tk.Button(lf4, text="Glas", font=(
        "Times New Roman", 11), padx=21, command=lambda: glas(window)).pack()
    Kalk = tk.Button(lf4, text="Kalk", font=(
        "Times New Roman", 11), padx=20, command=lambda: kalk(window)).pack()
    Lehm = tk.Button(lf4, text="Lehm", font=(
        "Times New Roman", 11), padx=17, command=lambda: lehm(window)).pack()
    Mauerstein = tk.Button(lf4, text="Mauerstein", font=(
        "Times New Roman", 11), padx=1, command=lambda: mauerstein(window)).pack()
    Zement = tk.Button(lf4, text="Zement", font=(
        "Times New Roman", 11), padx=12, command=lambda: zement(window)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: ano(window)).grid(column=0, row=1)


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


def kunststoff(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    ks1 = tk.Label(scrollbar.scrollable_frame, text="Herstellung", font=(
        "Times New Roman", 15)).pack()
    ks2 = tk.Label(scrollbar.scrollable_frame,
                   text="Niedermolekulare Ausgangsstoffe (Monomere) werden durch\nSynthese zu hochmolekularen Stoffen (Polymere) verkettet.\nFür die Verkettung gibt es je nach Art der Grundbaustoffe\n(Monomere) verschiedene Arten der Makromolekularbildung.", font=(
                       "Times New Roman", 11)).pack()
    ksa0 = tk.Button(scrollbar.scrollable_frame, text="Polymerisation", font=(
        "Times New Roman", 11), padx=27, command=lambda: poly(window)).pack()
    ks2 = tk.Label(scrollbar.scrollable_frame, text="Polyaddition\nPolykondensation\n", font=(
        "Times New Roman", 12)).pack()
    ks3 = tk.Label(scrollbar.scrollable_frame, text="Eigenschaften",
                   font=("Times New Roman", 15)).pack()
    ks4 = tk.Label(scrollbar.scrollable_frame,
                   text="POSITIV:\nLeichte Formbarkeit\nGeringes Gewicht (Rohdichte)\nNiedrige Wärmeleitfähigkeit\nGutes elektrisches Isoliervermögen\nGroße Beständigkeit gegenüber Wasser und aggressiven Stoffen\n\nNEGATIV:\nNiedriger E-Modul\nIm Allgemeinen nicht formbeständig bei höheren Temperaturen\nVersprödungsgefahr bei tiefen Temperaturen\nGroßer Wärmeausdehnungskoeffizient\n", font=("Times New Roman", 11)).pack()
    ks5 = tk.Label(scrollbar.scrollable_frame, text="Kunststoffarten",
                   font=("Times New Roman", 15)).pack()
    ks6 = tk.Label(scrollbar.scrollable_frame,
                   text="Die Makromoleküle erhalten je nach Synthese\nund Stoffart einen unterschiedlichen Aufbau.\nDie Molekülkettenstruktur ist maßgeblich für das\nthermische und mechanische Verhalten der Kunststoffe,\nund dementsprechend der Eignung eines Kunststoffes.\nNach der Anordnung der Molekülketten unterschiedet man:\n",
                   font=("Times New Roman", 11)).pack()
    ksa1 = tk.Button(scrollbar.scrollable_frame, text="Thermoplaste", font=(
        "Times New Roman", 11), padx=27, command=lambda: thermo(window)).pack()
    ksa2 = tk.Button(scrollbar.scrollable_frame, text="Elastomere",
                     font=("Times New Roman", 11), padx=27, command=lambda: elasto(window)).pack()
    ksa3 = tk.Button(scrollbar.scrollable_frame, text="Duroplaste",
                     font=("Times New Roman", 11), command=lambda: duro(window)).pack()
    ks8 = tk.Label(scrollbar.scrollable_frame,
                   text="\n", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: o(window)).pack()

    scrollbar.pack()


def poly(window=None):
    window = neuesFensters(window)

    v1 = tk.Label(window, text="Reaktion, bei der sich Monomere unter Einfluss von Inhibitoren\n(Anregern) zu Makromolekülen mit langen Ketten verbinden\n\nH  H     H  H      H  H  H  H\n|   |         |   |          |   |   |   |\nC=C -> -C-C- -> -C-C-C-C-\n|   |         |   |          |   |   |   |\nH  H     H  H      H  H  H  H\nEthylen                  Polyethylen\n\nCH3HCH3H H H   CH3HCH3HCH3H   CH3HHHCH3H\n|   |   |   |   |   |         |   |   |   |   |   |          |   |   |   |   |   |\n-C-C-C-C-C-C-      -C-C-C-C-C-C-      -C-C-C-C-C-C-\n|   |   |   |   |   |         |   |   |   |   |   |          |   |   |   |   |   |\nH H H HCH3H     H H H H H H        HHCH3HH H\nataktisch                isotaktisch              syndiotaktisch\n", font=(
        "Times New Roman", 11)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: kunststoff(window)).pack()


def thermo(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    v1 = tk.Label(scrollbar.scrollable_frame, text="Struktur", font=(
        "Times New Roman", 15)).pack()
    v2 = tk.Label(scrollbar.scrollable_frame, text="Lineare, fadenförmige Makromoleküle\n", font=(
        "Times New Roman", 11)).pack()
    v3 = tk.Label(scrollbar.scrollable_frame, text="Mechanische Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    met1 = tk.PhotoImage(file="met1.png")
    m1 = tk.Label(scrollbar.scrollable_frame, image=met1)
    m1.pack()
    met2 = tk.PhotoImage(file="met2.png")
    m2 = tk.Label(scrollbar.scrollable_frame, image=met1)
    m2.pack()
    met3 = tk.PhotoImage(file="met3.png")
    v4 = tk.Label(scrollbar.scrollable_frame, image=met1)
    v4.pack()
    v5 = tk.Label(scrollbar.scrollable_frame, text="Thermomechanische Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    tmt = tk.PhotoImage(file="tmt.png")
    v6 = tk.Label(scrollbar.scrollable_frame, image=tmt)
    v6.pack()
    v7 = tk.Label(scrollbar.scrollable_frame, text="Anwendung", font=(
        "Times New Roman", 15)).pack()
    v8 = tk.Label(scrollbar.scrollable_frame, text="Wasserschutzfolien, Dichtungsfolien, Trinkwasserrohre, Rohre,\nProfile, Bodenbeläge, Folien, Schaumstoffe\n",
                  font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: kunststoff(window)).pack()

    scrollbar.pack()


def elasto(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    v1 = tk.Label(scrollbar.scrollable_frame, text="Struktur", font=(
        "Times New Roman", 15)).pack()
    v2 = tk.Label(scrollbar.scrollable_frame, text="Weitmaschig vernetzte Makromoleküle", font=(
        "Times New Roman", 11)).pack()
    v3 = tk.Label(scrollbar.scrollable_frame, text="Mechanische Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    mee = tk.PhotoImage(file="mee.png")
    v4 = tk.Label(scrollbar.scrollable_frame, image=mee)
    v4.pack()
    v5 = tk.Label(scrollbar.scrollable_frame, text="Thermomechanische Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    tme = tk.PhotoImage(file="tme.png")
    v6 = tk.Label(scrollbar.scrollable_frame, image=tme)
    v6.pack()
    v7 = tk.Label(scrollbar.scrollable_frame, text="Anwendung", font=(
        "Times New Roman", 15)).pack()
    v8 = tk.Label(scrollbar.scrollable_frame,
                  text="Bindemittel für Estrich u. Beschichtungsmaßen,\nKlebstoffe, Schaumstoffe\n", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: kunststoff(window)).pack()

    scrollbar.pack()


def duro(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    v1 = tk.Label(scrollbar.scrollable_frame, text="Struktur", font=(
        "Times New Roman", 15)).pack()
    v2 = tk.Label(scrollbar.scrollable_frame, text="Engmaschig vernetzte Makromoleküle", font=(
        "Times New Roman", 11)).pack()
    v3 = tk.Label(scrollbar.scrollable_frame, text="Mechanische Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    med = tk.PhotoImage(file="med.png")
    v4 = tk.Label(scrollbar.scrollable_frame, image=med)
    v4.pack()
    v5 = tk.Label(scrollbar.scrollable_frame, text="Thermomechanische Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    tmd = tk.PhotoImage(file="tmd.png")
    v6 = tk.Label(scrollbar.scrollable_frame, image=tmd)
    v6.pack()
    v7 = tk.Label(scrollbar.scrollable_frame, text="Anwendung", font=(
        "Times New Roman", 15)).pack()
    v8 = tk.Label(scrollbar.scrollable_frame, text="Bindemittel für Kunstharzbeton u. Estrich,\nKleber, Imprägnierungen, Harz für GFK\n", font=(
        "Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: kunststoff(window)).pack()

    scrollbar.pack()


def holz(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    v1 = tk.Label(scrollbar.scrollable_frame, text="Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    v2 = tk.Label(scrollbar.scrollable_frame, text="Text1", font=(
        "Times New Roman", 11)).pack()
    v3 = tk.Label(scrollbar.scrollable_frame,
                  text="Struktureller Aufbau", font=("Times New Roman", 15)).pack()
    v4 = tk.Label(scrollbar.scrollable_frame,
                  text="Text2", font=("Times New Roman", 11)).pack()
    v5 = tk.Label(scrollbar.scrollable_frame,
                  text="Verwendung", font=("Times New Roman", 15)).pack()
    v6 = tk.Label(scrollbar.scrollable_frame, text="Holz wird wegen\nseiner geringen Dichte und Wärmeleitfähigkeit,\nseiner hohen Zähigkeit und\nseiner leichten Bearbeitbarkeit zum Bauen verwendet.\n\nHolz weist in verschiedenen Richtungen unterschiedliche Eigenschaften auf (anisotrop).\nDas Materialverhalten von Holz wird durch Holzfehler\n(z. B. Äste) beeinträchtigt.\n\nMehr oder weniger homogene Holzwerkstoffe, die durch das\nZusammensetzen von kleinen fehlerfreien Holzteilen entstehen\nnennt man Holzwerkstoffe.\n\nHolzwerkstoffe sind Funierschnittholz, Sperrholz, Spanplatten,\nOSB-Platten, Holzfaserplatten\nVollholzprodukte sind Bauschnittholz, Konstruktionsvollholz und Brettschichtholz\n",
                  font=("Times New Roman", 11)).pack()
    v7 = tk.Label(scrollbar.scrollable_frame, text="Holzschutzmaßnahmen", font=(
        "Times New Roman", 15)).pack()
    v8 = tk.Label(scrollbar.scrollable_frame,
                  text="Text 4\n", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: o(window)).pack()

    scrollbar.pack()


def bitumen(window=None):
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
        "Times New Roman", 11), command=lambda: o(window)).pack()

    scrollbar.pack()


def beton(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    beton1 = tk.Label(scrollbar.scrollable_frame, text="Bestandteile",
                      font=("Times New Roman", 15)).pack()
    zmnt = tk.Button(scrollbar.scrollable_frame, text="Zement", font=(
        "Times New Roman", 11), padx=27, command=lambda: zement(window)).pack()
    wasser = tk.Button(scrollbar.scrollable_frame, text="Wasser",
                       font=("Times New Roman", 11), padx=27, command=lambda: WZ(window)).pack()
    gstkrn = tk.Button(scrollbar.scrollable_frame, text="Gesteinskörnung",
                       font=("Times New Roman", 11), command=lambda: gesteinskörnung(window)).pack()
    zusatzst = tk.Button(scrollbar.scrollable_frame, text="Zusatzstoffe",
                         font=("Times New ROman", 11), padx=13, command=lambda: zss(window)).pack()
    zusatzmttl = tk.Button(scrollbar.scrollable_frame, text="Zusatzmittel",
                           font=("Times New Roman", 11), padx=14, command=lambda: zsm(window)).pack()
    stahlf = tk.Button(scrollbar.scrollable_frame, text="Stahlfassern",
                       font=("Times New Roman", 11), padx=13, command=lambda: sf(window)).pack()
    beton2 = tk.Label(scrollbar.scrollable_frame, text="\nMischverhältnis",
                      font=("Times New Roman", 15)).pack()
    mischverhaeltnis = tk.Label(scrollbar.scrollable_frame, text="Die korrekte Zuordnung des Bauteiles/Bauwerkes zu Expositionsklassen,\n je nach Umgebungsbedingungen ist\n eine wichtige Voraussetzung für die Zusammensetzung des Betons.\n In Abhängigkeit der zu erwartenden Beanspruchungen, die auf das Bauteil wirken,\n werden in den Expositionsklassen Anforderungen vorgegeben.", font=("Times New Roman", 11)).pack()
    TdE = tk.Button(scrollbar.scrollable_frame, text="Tabelle der Expositionsklassen", font=(
        "Times New Roman", 11), command=lambda: explo(window)).pack()
    beton3 = tk.Label(scrollbar.scrollable_frame, text="\nProzessstufen bei der Herstellung", font=(
        "Times New Roman", 15)).pack()
    PbdH = tk.Label(
        scrollbar.scrollable_frame, text="1. Herstellen(Mischen) im Transportbetonwerk\n2. Befördern im Fahrmischer\n3. Frischbeton ausbreiten\n4. Nachbehandeln (mit Wasser oder Nachbehandlungsmitteln) um das\nTrocknen zu verhindern -> Beton härtet, d.h chem. Reaktionen finden statt\n5. Festbeton ausschalen", font=("Times New Roman", 11)).pack()
    beton4 = tk.Label(scrollbar.scrollable_frame, text="\nStruktur und Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    SuE = tk.Label(
        scrollbar.scrollable_frame, text="Zement + Wasser -> CSH-Phasen + Portlandit\n3CaO * SiO2(Alit) + H2O -> Ca(OH)2\n2CaO * SiO2(Belit) + H20\n\nhohe Druckfestigkeit, dicht,wasserbeständig\nKapillarporen ->Frostprobleme, keine Dauerhaftigkeit\n", font=("Times New Roman\n", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()

    scrollbar.pack()


def gips(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    gips1 = tk.Label(scrollbar.scrollable_frame, text="Vorkommen",
                     font=("Times New Roman", 15)).pack()
    render = tk.PhotoImage(
        file="Rauchgasentschwefelung.gif")
    img = tk.Label(scrollbar.scrollable_frame, image=render)
    img.image = render
    gips2 = tk.Label(scrollbar.scrollable_frame, compound=tk.BOTTOM, text="Natürliches Vorkommen\n\nIndustrielles Restprodukt (bei der Rauchgasentschwefelung)\nCalciumsulfit + Luft -> Calciumsulfat\n2 CaSO3 + O2 → 2 CaSO4",
                     image=render, font=("Times New Roman", 11)).pack()
    gips3 = tk.Label(scrollbar.scrollable_frame, text="\nStruktur und Eigenschaften",
                     font=("Times New Roman", 15)).pack()
    gips4 = tk.Label(scrollbar.scrollable_frame, text="CaSO4 * 2H2O\nBeim Brennen findet keine chemische Reaktion statt\nErhärten ist ein Kristallisationsvorgang\n (->CaSO4)",
                     font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()

    scrollbar.pack()


def glas(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    render = tk.PhotoImage(file="floatglass.png")
    img = tk.Label(scrollbar.scrollable_frame, image=render)
    img.image = render
    glas1 = tk.Label(scrollbar.scrollable_frame, compound=tk.BOTTOM, text="Herstellung", image=render, font=(
        "Times New Roman", 15)).pack()
    glas2 = tk.Label(scrollbar.scrollable_frame, text="\nVerwendung",
                     font=("Times New Roman", 15)).pack()
    glas3 = tk.Label(
        scrollbar.scrollable_frame, text="Fenster und zunehmend tragende Strukturen\n\nBauglas = Alkali-Silikat-Gläser\nFensterglas = Kalk-Natron- Glas", font=("Times New Roman", 11)).pack()
    glas4 = tk.Label(scrollbar.scrollable_frame, text="\nStruktur und Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    glas5 = tk.Label(
        scrollbar.scrollable_frame, text="Sammelbegriff für alle amorphen Feststoffe\n->auch amorph erstarrte Metalle\n->teilweise organischen Ursprungs (bspw.Bernstein)\n\namorph -> unterkühlte zähe Flüssigkeit -> keine Nahordnung =/= kristallin\n\nHohe Lichtdruchlässigkeit\nSehr hohe Druckfestigkeit\nSehr spröde und schlagempfinglich\nähnlich hohe Dichte wie Beton\n", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()

    scrollbar.pack()


def kalk(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    kalk1 = tk.Label(scrollbar.scrollable_frame, text="Vorkommen und Zusammensetzung", font=(
        "Times New Roman", 15)).pack()
    kkl = tk.PhotoImage(file="kalkkreislauf.png")
    img = tk.Label(scrollbar.scrollable_frame, image=kkl)
    img.image = kkl
    kalk2 = tk.Label(scrollbar.scrollable_frame, compound=tk.BOTTOM,
                     text="Zement + Wasser -> CSH-Phasen + Portlandit\nPortlandit = Löschkalk (niedriger Ph-Wert)\nC3S/C2S + H20 -> CaO/SiO2/H20 + Ca(OH)2\n\nPortlandit->Kalkstein (hoher Ph-Wert)\nCa(OH)2 + CO2 + H2O -> CaCO3 + 2H2O\n", image=kkl, font=("Times New Roman", 11)).pack()
    kalk3 = tk.Label(scrollbar.scrollable_frame,
                     text="\nVerwendung", font=("Times New Roman", 15)).pack()
    kalk4 = tk.Label(scrollbar.scrollable_frame,
                     text="1.Als Bindemittel:\n- Putz\n- Mauermörtel\n- Bestandteil von Beton\n2.Zum Knochenaufbau\n3.Zum Bierbrauen\n", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()

    scrollbar.pack()


def lehm(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    lehm = tk.PhotoImage(file="llehm.png")
    img = tk.Label(scrollbar.scrollable_frame, image=lehm)
    img.image = lehm
    lehm1 = tk.Label(scrollbar.scrollable_frame, text="Vorkommen und Zusammensetzung", font=(
        "Times New Roman", 15)).pack()
    lehm2 = tk.Label(scrollbar.scrollable_frame, compound=tk.BOTTOM, text="Verwitterungsprodukt von Urgestein\nGemisch aus Ton, Wasser und Sand\nTon = Koalinit + Montmorillonit, Korngröße>=0,002mm",
                     image=lehm, font=("Times New Roman", 11)).pack()
    lehm3 = tk.Label(scrollbar.scrollable_frame,
                     text="Wasser = fester Ton enthält grundsätzlich gebundenes Wasser\nSand = Sio2, Korngröße 0,06-2mm", font=("Times New Roman", 11)).pack()
    lehm4 = tk.Label(scrollbar.scrollable_frame, text="\nEigenschaften",
                     font=("Times New Roman", 15)).pack()
    lehm5 = tk.Label(scrollbar.scrollable_frame, text="Lehm ist ein mineralisches, bindigesm Lockergestein\nHydration von Ton = Ton wird durch Wasserzufuhr plastisch biegsam\n=\nLehm ist wasserempfindlich = wetterunbeständig\nLehm ist recyclebar (ohne Energiezufuhr\nLehm hat gute Sorptionseigenschaften (gesundes Raumklima)\nLehm ist en guter Wärmespeicher (Durch Zugabe von purösen Stoffen Warmedämmung gegeben (z.B Bims))", font=("Times New Roman", 11)).pack()
    lehm6 = tk.Label(scrollbar.scrollable_frame, text="\nBauen mit Lehm",
                     font=("Times New Roman", 15)).pack()
    lehm7 = tk.Label(scrollbar.scrollable_frame, text="Beginn des Lehmbau 5000 v. Chr.\nSchibam in Südjemen = älteste Hochhausstadt aus Lehmbauten\nTurm von Babel (7 Jhd v. Chr)\nChinesische Mauer (vor 400 Jahren)\nHeute lebt 1/3 der Menschheit in Lehmbauten\n\nLehmbautechniken zum Bau tragender Wände:\nStampflehmbau (Mithilfe von Schalungen)\nWellerbau (Schalungsloses Aufbauen der Wand u. Abtragen der Oberfläche\nLehmsteinbau (Ziegelsteinbau mit Luftgetrockneten Lehmbausteinen)\n\nAufgrund der Wasserbeständigkeit sind beim Bauen mit Lehm Wasserschutzmaßnahmen nötig", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()

    scrollbar.pack()


def mauerstein(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    ms1 = tk.Label(scrollbar.scrollable_frame, text="Varianten",
                   font=("Times New Roman", 15)).pack()
    ms2 = tk.Label(scrollbar.scrollable_frame, text="- Natursteine (Magmasteine, Sedimente, Umwandlungsgesteine)\n- Kalksandstein\n- Mauerziegel\na) Vollziegel (früher)\nb) Hochlochziegel (geringere Wärmeleitfähigkeit (=Dämmungswirkung), Materialsparend)\n- Beton und Leichtbetonsteine\n- Porenbetonsteine\n", font=("Times New Roman", 11)).pack()
    ms3 = tk.Label(scrollbar.scrollable_frame, text="Herstellung (Ziegeln)", font=(
        "Times New Roman", 15)).pack()
    ms4 = tk.Label(scrollbar.scrollable_frame,
                   text="- Rohstoffgewinnung\n- Rohstoffverarbeitung\n- Formgebung\n- Trocknung\n- Brennen\n- Planschleifen -> Planziegel (=exakt gleiche Maße)\nFüllung mit Wärmedämmstoff", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()

    scrollbar.pack()


def zement(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    zement1 = tk.Label(scrollbar.scrollable_frame, text="Struktur und Eigenschaften", font=(
        "Times New Roman", 15)).pack()
    zement2 = tk.Label(scrollbar.scrollable_frame, text="Zement ist ein anorganisches, fein gemalenes, hydraulisch wirkendes Bindemittel für Mörtel und Beton\nMörtel: Gesteinskörnung <=4mm\nBeton: Gesteinskörnung >4mm\n5-8% der weltweiten CO2-Emission stammen aus der Zementproduktion\nErhärtet auch unter Wasser\nBildet mit Wasser Zementleim -> Erhärteter Zementleim = Zementstein\n", font=(
        "Times New Roman", 11)).pack()
    zement3 = tk.Label(scrollbar.scrollable_frame,
                       text="Herstellung", font=("Times New Roman", 15)).pack()
    zement4 = tk.Label(scrollbar.scrollable_frame,
                       text="Gewinnen u. Brechen der Rohstoffe aus einem Sandsteinbruch\nKalk = CaCO3|Ton = Al2O3|Sand = SiO2\nHomogenisieren u. Lagern der Ausgangsstoffe\nMahlen der Mischung\nTrocknen und Entsäuern (Entsäuern = CO2 EMISSION)\nFiltern in einem Elektrofilter\nErwärmen im Drehrohrofen -> (Zement)Klinker\nMahlen\nLagern des fertigen Zement\nVerladen\n", font=("Times New Roman", 11)).pack()
    zement5 = tk.Label(scrollbar.scrollable_frame,
                       text="Zementarten", font=("Times New Roman", 15)).pack()
    zement6 = tk.Label(scrollbar.scrollable_frame, text="CEMI Portlandzement (früher am häufigsten in Deutschland\nCEMII Portlandkompositzement (CEMI + Zumahlstoffe; Heute am häufigsten in Deutschland\nCEMIII (für große Bauteile)\nCEMIV\nCEMV\n\nInsgesamt 27 Zementarten\n\nPuzzolane, Hüttensand, Flugasche etc tragen zur Erhärtung bei\n\nPuzzolane = kieselsäurehaltige u. manchmal tonerdehaltige Stoffe\nmit natürlichem Vorkommen (oft vulkanischem Ursprung\n", font=("Times New Roman", 11)).pack()
    zement7 = tk.Label(scrollbar.scrollable_frame, text="Abfallprodukte", font=(
        "Times New Roman", 15)).pack()
    zement8 = tk.Label(scrollbar.scrollable_frame,
                       text="Roheisen -> Verarbeitet zu Stahl\nSchlacke -> Abgekühlt zu Hüttensand\n", font=("Times New Roman", 11)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()

    scrollbar.pack()


def WZ(window=None):
    window = neuesFensters(window)

    wasser1 = tk.Label(window, text="Wasserzementwert (WZ-Wert)",
                       font=("Times New Roman", 15)).pack()
    wasser2 = tk.Label(window, text="Massenverhältnis von Wasser- u. Zement im Frischbeton\nJe höher der WZ-Wert, desto mehr Kapilarporen\n",
                       font=("Times New Roman", 11)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()


def gesteinskörnung(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    gsk1 = tk.Label(scrollbar.scrollable_frame, text="Definition und Eigenschaften",
                    font=("Times New Roman", 15)).pack()
    gsk2 = tk.Label(scrollbar.scrollable_frame, text="Unter Gesteinskörnung versteht man ein körniges Material, welches mit Wasser\nund Zement für die Herstellung von Beton geeignet ist und hierfür verwendet wird.\nGesteinskörnungen werden entsprechend ihrer Herkunft, dem Gefüge\n und der Kornrohdichte eingeteilt.\nSie können natürlich, industriell hergestellt oder rezykliertsein.\nNach der Kornrohdichte wird unterschieden in leichte,\n normale (Kornrohdichte 2 000 bis 3 000 kg/m³) und schwere Gesteinskörnungen.\nGesteinskörnungen für Normal-und Schwerbeton müssen den Anforderungen\n der DIN EN 12620 entsprechen.\nLeichte Gesteinskörnungen sind in der DIN EN 13055-1 geregelt.\n", font=("Times New Roman", 11)).pack()
    sl = tk.PhotoImage(file="Sieblinien.gif")
    img = tk.Label(scrollbar.scrollable_frame, image=sl)
    img.image = sl
    gsk3 = tk.Label(scrollbar.scrollable_frame, compound=tk.BOTTOM, text="Sieblinien", image=sl,
                    font=("Times New Roman", 15)).pack()
    back = tk.Button(scrollbar.scrollable_frame, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()

    scrollbar.pack()


def zsm(window=None):
    window = neuesFensters(window)

    zsm = tk.Label(window, text="\nBei/ gegen schlechte(r) Verarbeitbarkeit des Frischbetons\n\nNormalbeton ist ein 3-Stoff-System,\ndurch Zusatzstoffe und Zusatzmittel erhält man Hochleistungsbeton",
                   font=("Times New Roman", 11)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()


def zss(window=None):
    window = neuesFensters(window)

    zss = tk.Label(window, text="\nCa(OH2) + SiO2 -> CSH-Phase\n->Kristallbildung wird begünstigt\n->Kristalle in den Hohlräumen = Höhere Festigkeit\n\nBspw.Silikatstaub SiO2 oder Flugsasche\n\nNormalbeton ist ein 3-Stoff-System,\ndurch Zusatzstoffe und Zusatzmittel erhält man Hochleistungsbeton\n",
                   font=("Times New Roman", 11)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()


def sf(window=None):
    window = neuesFensters(window)

    sf = tk.Label(window, text="\nBei/ gegen spröde(m/s) Materialverhalten\n",
                  font=("Times New Roman", 11)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()


def explo(window=None):
    window = neuesFensters(window)
    window.geometry("700x700")

    tabelle = tk.PhotoImage(file="tabelle.png")
    img = tk.Label(window, image=tabelle)
    img.image = tabelle
    explo = tk.Label(window, compound=tk.BOTTOM, text="Zusammensetzung der Explosionsklassen",
                     image=tabelle, font=("Times New Roman", 11)).pack()
    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: mineral(window)).pack()


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


def grundlagen(window=None):
    window = neuesFensters(window)
    scrollbar = ScrollableFrame(window)

    back = tk.Button(window, text="Zurück", font=(
        "Times New Roman", 11), command=lambda: start(window)).pack()

    scrollbar.pack()


start()
tk.mainloop()
