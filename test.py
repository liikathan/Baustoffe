import tkinter as tk
from tkinter import ttk


# Vorlage für Frames in denen man scrollen kann
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


root = tk.Tk()

# Hier erzeugst du so einen Frame und sagst dass er in root (das Fenster soll)
frame = ScrollableFrame(root)

# Hier tust du irgendwas in den Frame, ist nur ein eispiel von einer Seite, aber da kann alles rein, auch Bilder und sonst alles
# for i in range(50):
#    ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

# Wenn alles drin ist pack
frame.pack()
# Das brauchst du halt immer
root.mainloop()
