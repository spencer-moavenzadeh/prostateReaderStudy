import tkinter as tk
from tkinter import *
from ReaderStudyGUI import MainGui
import os
import json


class TrainingGUI:
    def __init__(self, master):
        master.title("Training Window")

        # Create list to store training cases
        self.cases = dict()
        self.loadtraining()
        self.trainingcount = 0

        # Create a list to store the buttons
        self.trainingbtns = dict()
        self.documentbtns = dict()

        # Make Labels
        Label(master, text="Training Cases:", font="Helvetica 12 underline").grid(column=0, row=0, columnspan=3, pady=(5, 5), padx=(5, 5))

        # Add buttons for all training cases
        for trainingcase in self.cases:
            self.addtrainingcase(master, self.cases[trainingcase])

    def loadtraining(self):
        filepath = os.getcwd() + "\\Training\\TrainingOrder.csv"

        # Open and store file
        with open(filepath, "r") as infile:
            cases = (infile.read()).split("\n")

        # Remove space
        for index in range(0, len(cases)):
            self.cases[index] = cases[index].strip().split(",")

    def addtrainingcase(self, master, trainingcaselist):
        trainingcase = trainingcaselist[0]
        iosbucket = trainingcaselist[1]
        Label(master, text="%d. %s:" % (self.trainingcount+1, trainingcase), font="Helvetica 10", anchor="w").grid(column=0, row=self.trainingcount + 1, pady=(7, 7), padx=(5, 5))
        self.trainingbtns[trainingcase] = Button(master, text="Slicer", command=lambda case=trainingcase, iosbucket=iosbucket: self.opentrainingstudy(case, iosbucket), bg="green",
                                                 fg="white")
        self.trainingbtns[trainingcase].grid(column=1, row=self.trainingcount + 1, pady=(7, 7), padx=(5, 5))
        self.documentbtns[trainingcase] = Button(master, text="Training File", command=lambda case=trainingcase, iosbucket=iosbucket: self.opentrainingdocument(case, iosbucket), bg="red",
                                                 fg="white")
        self.documentbtns[trainingcase].grid(column=2, row=self.trainingcount + 1, pady=(7, 7), padx=(5, 5))
        self.documentbtns[trainingcase].configure(state=DISABLED)
        self.trainingcount += 1

    def opentrainingdocument(self, case, iosbucket):
        # Open training document
        os.system('start %s' % (os.getcwd() + "\\Training\\" + iosbucket + "\\" + case + "\\%s_TrainingDocument.pdf" % case))

    def opentrainingstudy(self, case, iosbucket):
        # Open top level GUI
        readerstudyroot = Toplevel()
        readerstudyGUI = MainGui(readerstudyroot, "TRAINING", [case, iosbucket], "training")
        readerstudyroot.geometry(loadgeometry("ReaderStudyGUI"))
        readerstudyroot.attributes('-topmost', True)
        self.documentbtns[case].configure(state=NORMAL)


def loadgeometry(window):
    filepath = os.getcwd() + "\\ApplicationGeometry.json"

    with open(filepath, "r") as infile:
        applicationgeometrydict = json.loads(infile.read())

    return applicationgeometrydict[window]


if __name__ == "__main__":
    root = Tk()
    appgui = TrainingGUI(root)
    root.geometry(loadgeometry("ReaderStudyApplication"))
    #root.attributes('-topmost', True)
    root.mainloop()