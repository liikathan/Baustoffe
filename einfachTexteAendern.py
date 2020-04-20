import tkinter as tk


class Baustoffe:
    texte = [
        "Die Natur bietet dem Menschen *Naturstoffe*.\n Diese werden zu *Rohstoffen*,\n wenn sie durch menschliche Arbeit gewonnen werden\n (bsp.Erze/ Kies).\n Bearbeitet man die Rohstoffe industriell,\n so werden sie zu *Werkstoffen*.\n Werkstoffe, die in der Bauindustrie verwendet werden,\n bezeichnet man als *Baustoff*.\n Aus Baustoffen werden Bauwerke",
        "Text 2 ist auch ok",
        "Text 3 ist perfekt"
    ]

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT)

        # Eingabe
        self.text = tk.Entry(root)
        self.text.pack(side=tk.LEFT)

        # Anzeigen vom Text
        self.lf = tk.Label(root, text="Test")
        self.lf.pack(side=tk.LEFT)

        # Text 1 anzeigen
        self.changeButton1 = tk.Button(
            frame, text="Text 1", command=lambda: self.changeText(self.lf, self.texte[0]))
        self.changeButton1.pack(side=tk.LEFT)

        # Text 2 anzeigen
        self.changeButton2 = tk.Button(
            frame, text="Text 2", command=lambda: self.changeText(self.lf, self.texte[1]))
        self.changeButton2.pack(side=tk.LEFT)

        # Text 3 anzeigen
        self.changeButton3 = tk.Button(
            frame, text="Text 3", command=lambda: self.changeText(self.lf, self.texte[2]))
        self.changeButton3.pack(side=tk.LEFT)

        # Text von Label zu Text aus Entry
        self.changeButton4 = tk.Button(
            frame, text="Text 3", command=lambda: self.changeText(self.lf, self.text.get()))
        self.changeButton4.pack(side=tk.LEFT)

        # Beenden
        self.quitButton = tk.Button(
            frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=tk.LEFT)

    def changeText(self, target, text):
        # Text von bestimmten Label aendern
        target["text"] = text


# Fenster oeffnen
root = tk.Tk()
root.title("Baustoffe")
root.geometry("500x500")

frame = Baustoffe(root)  # Frame Baustoffe in Root-Window

root.mainloop()
