"""
@file src/mainframe/mainframe.py
@version 1.1
@author CN
@author Gudule
@date jan 2017

Cette fenêtre donne accès à certaines fonctions de potiron (pour l'instant
très peu).

@todo aucune fonctionnalité intéressante accessible.

"""


from tkinter import W, E, N, S, END
from tkinter import Button
from tkinter import Frame, Label
import tkinter
import tkinter.filedialog as filedialog
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext
from tkinter import Text

import random
import os
from lexicon import lookup

try:
    from tagger.tagger import Tagger
    TAGGER = True
except ImportError as e:
    print("Vous utilisez actuellement Potiron sans Tagger.")
    TAGGER = False


#=================================

FONT_BUTTONS = 'helvetica', 12, "bold"
FONT_LABELS = 'helvetica', 12, 'bold'

#==================================


class MainFrame(Frame):
    """
    @class MainFrame

    Fenêtre principale de l'application.
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=0, column=0)

        # the main text zone
        self.text = Text(self, undo=True)
        # self.text['font'] = FONT

        # the output text zone
        self.output = scrolledtext.ScrolledText(self, undo=False)

        # bind the main controls to the frame
        self._root().bind('<Control-q>', self.on_closing)
        self._root().protocol("WM_DELETE_WINDOW", self.on_closing)

        self.buttonlookup = Button(self, font=FONT_BUTTONS,
               width=18,
               text="Lookup",
               command=self.on_lookup)
        self.buttontag = Button(self, font=FONT_BUTTONS,
               width=18,
               text="Tag",
               command=self.on_tag)
        self.buttongramtag = Button(self, font=FONT_BUTTONS,
               width=18,
               text="Tagger tag",
               command=self.on_tagger_tag)

        if TAGGER:
            self.tagger = Tagger()
        else:
            self.tagger = None

        self.buttonlookup.grid(row=0, column=0, sticky=E+W+N+S)
        self.buttontag.grid(row=0, column=1, sticky=E+W+N+S)
        self.buttongramtag.grid(row=0, column=2, sticky=E+W+N+S)
        self.text.grid(row=1, column=0, columnspan=3, rowspan=3, sticky=E+W+N+S)
        self.output.grid(row=1, column=4, columnspan=4, rowspan=3, sticky=E+W+N+S)



    def on_closing(self, event=None):
        """
        Lorsque l'application est fermée.
        """
        if TAGGER:
            self.tagger.close()
        self._root().destroy()

    def on_lookup(self, event=None):
        """
        Lors d'une recherche dans le lexique.

        @todo mauvais comportement
        """
        content = self.text.get("1.0", END).lstrip().rstrip()
        res = []
        for l in [lookup(content, "NOM"), lookup(content, "VER") , lookup(content, "ADJ"), lookup(content, "ADV")]:
            if l:
                res.append(l)
        out = "\n".join([str(t) for t in res])
        self.output.delete("1.0", END)
        self.output.insert("1.0", out)

    def on_tag(self, event=None):
        """
        Tagguer un texte.
        """
        if TAGGER:
            content = self.text.get("1.0", END).lstrip().rstrip()
            self.output.delete("1.0", END)
            out = str(self.tagger.tag(content))
            self.output.insert("1.0", out)
        else:
            print("Cette fonction n'est pas disponible.")

    def on_tagger_tag(self, event=None):
        if TAGGER:
            content = self.text.get("1.0", END).lstrip().rstrip()
            self.output.delete("1.0", END)
            out = str(self.tagger.taggertag(content))
            self.output.insert("1.0", out)
        else:
            print("Cette fonction n'est pas disponible.")
