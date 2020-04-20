import tkinter as tk
from tkinter import ttk
from grundlagen import select


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
    v6 = tk.Label(scrollbar.scrollable_frame,
                  text="Holz wird wegen\nseiner geringen Dichte und Wärmeleitfähigkeit,\nseiner hohen Zähigkeit und\nseiner leichten Bearbeitbarkeit zum Bauen verwendet.\n\nHolz weist in verschiedenen Richtungen unterschiedliche Eigenschaften auf (anisotrop).\nDas Materialverhalten von Holz wird durch Holzfehler\n(z. B. Äste) beeinträchtigt.\n\nMehr oder weniger homogene Holzwerkstoffe, die durch das\nZusammensetzen von kleinen fehlerfreien Holzteilen entstehen\nnennt man Holzwerkstoffe.\n\nHolzwerkstoffe sind Funierschnittholz, Sperrholz, Spanplatten,\nOSB-Platten, Holzfaserplatten\nVollholzprodukte sind Bauschnittholz, Konstruktionsvollholz und Brettschichtholz\n",
                  font=("Times New Roman", 11)).pack()
    v7 = tk.Label(scrollbar.scrollable_frame, text="Holzschutzmaßnahmen", font=(
        "Times New Roman", 15)).pack()
    v8 = tk.Label(scrollbar.scrollable_frame,
                  text="Zerstörung von Holz durch Pilze\nFür die Entwicklung von holzzerstörenden Pilzen sind vor allem\neine hohe Holzfeuchte von ≥ 20 M.-% sowie Wärme und geringe Luftbewegung günstig.\nDie Pilze entziehen dem Holz (besonders dem Splintholz)\nCellulose und Lignin und verursachen dadurch Fäulnis und Zerfall.\nAm gefährlichsten ist der echte Hausschwamm\n\nZerstörung von Holz durch Insekten\nDie eigentlichen Schädlinge sind Larven bestimmter Insekten.\nDie Larven zerfressen das Holz, vor allem das weichere Splintholz.\nAm weitesten verbreitet ist der Hausbock.\nDie Larven sind bis 30 mm lang.\n\nSchutzgegen Pilze und Insekten\nDie Holzschutzmaßnahmen sind in DIN 68 800 beschrieben:\nDIN 68 800-2: Vorbeugende bauliche Maßnahmen•DIN 68 800-3: Vorbeugende chemische Maßnahmen\nDIN 68 800-4: Bekämpfende Maßnahmen nach Befall\nDurch die Einführung der DIN 68 800-2 wird der\nGesundheits-und Umweltschutz betont im Unterschied zum früher\nverfolgten Gedanken des reinen Materialschutzes.\nChemie –so wenig wie möglich und so viel wie nötig!\nFür die üblichen Anwendungsfälle im Hochbau ist durch die Verwendung\nvon qualitätsgesichert technisch getrocknetes Vollholzsichergestellt,\ndass die für GK 1 geforderten Eigenschaften gegen holzzerstörende\nInsekten erfüllt sind.\nKernholz besteht aus abgestorbenen Zellen, die nicht mehr\ndem Nährstofftransport dienen und ist aufgrund eingelagerter\nStoffe oft auffallend dunkel gefärbt.\nDie eingelagerten Fette, Harze und Gerbstoffe\nverändern die Eigenschaften des Holzes.\nKernholz ist im Vergleich zu Splintholz schwerer,\nhärter und dauerhafter gegenüber holzzerstörenden Pilzen\nund Insekten.\n\n", font=("Times New Roman", 11)).pack()
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
