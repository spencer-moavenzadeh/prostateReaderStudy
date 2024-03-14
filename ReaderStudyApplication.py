import tkinter as tk
from tkinter import ttk, filedialog, simpledialog
from tkinter import *
from ReaderStudyGUI import MainGui
from trainingGUI import TrainingGUI
import os
import json


class MainWindow:
    def __init__(self, master):
        # Set the main window title
        master.title("Personalized Window Launcher")

        # Create a list to store the names
        self.readers = dict()
        self.loadreaders()
        self.readercount = 0
        self.readercount = len(self.readers)

        # Create a list to store the buttons
        self.buttons = dict()

        # Create a list to store the remove buttons
        self.remove_buttons = dict()

        # Add an "Add Name" button
        add_button = Button(master, text="Add Reader", command=lambda: self.add_name(master), bg="purple1", fg="white")
        add_button.grid(column=0, row=0, pady=(10, 5), padx=(10, 10))

        # Add refresh button
        self.refreshbtn = Button(master, text="Refresh", bg="blue", fg="white",
                                 command=lambda: refresh(master))
        self.refreshbtn.grid(column=1, row=0, padx=(10, 5), pady=(10, 10))

        # Add training button
        self.trainingbtn = Button(master, text="New Reader Training", bg="darkgreen", fg="white",
                                  command=lambda: self.launchtraining())
        self.trainingbtn.grid(column=0, row=1, columnspan=2, padx=(5, 5), pady=(10, 10))

        # Add buttons for all readers
        for reader in self.readers:
            self.addnamebuttons(master, reader, self.readers[reader])

    def launchtraining(self):
        """
        Open menu of training cases, where can select which case in training, under the training bucket label (?),
        Args:
            master:

        Returns:

        """
        # Open top level GUI
        trainingroot = Toplevel()
        trainingGUI = TrainingGUI(trainingroot)
        trainingroot.geometry(loadgeometry("ReaderStudyApplication"))
        #trainingroot.attributes('-topmost', True)

    def add_name(self, master):
        # Ask the user for a new name
        name = tk.simpledialog.askstring("Add Reader", "Enter a new name:")

        if not self.nameexists(name):
            # Add the name to the list and create a button for it
            self.addnamebuttons(master, name, "Patient120")
            self.addnamedirectories(name)
            refresh(master)
        else:
            print("Name Already Exists")

    def addnamedirectories(self, name):
        caseorder = self.loadcaseorder()
        print(os.getcwd())
        for case in caseorder:
            os.system("mkdir %s\\slicer\\%s" % (case, name))

    def loadcaseorder(self):
        """

        Returns:

        """
        filepath = os.getcwd() + "\\StudyOrder.csv"

        # Open and store file
        with open(filepath, "r") as infile:
            caseorder = (infile.read()).split("\n")

        # Remove space
        for index in range(0, len(caseorder) - 1):
            caseorder[index] = caseorder[index].strip()

        return caseorder

    def addnamebuttons(self, master, name, progress):
        self.storename(name, progress)
        # Add the name to the list and create a button for it
        self.readers[name] = progress
        self.readercount += 1
        self.buttons[name] = Button(master, text=name, command=lambda name=name, progress=self.readers[name]: self.openreaderstudy(name, progress), bg="green",
                                    fg="white")
        self.buttons[name].grid(column=0, row=self.readercount + 3, pady=(10, 10), padx=(5, 5))
        self.remove_buttons[name] = Button(master, text="Remove", command=lambda: self.remove_name(master, name),
                                           bg="red", fg="white")
        self.remove_buttons[name].grid(column=1, row=self.readercount + 3, pady=(10, 10), padx=(5, 5))

    def storename(self, name, progress):
        self.readers[name] = progress
        with open(os.getcwd() + "\\ReadersProgress.json", 'w') as outfile:
            json.dump(self.readers, outfile, indent=4, sort_keys=True)

    def remove_name(self, master, name):
        # Remove the name from the list and its corresponding button
        if name in self.readers:
            self.readers.pop(name)
            self.buttons[name].destroy()
            self.remove_buttons[name].destroy()

    def openreaderstudy(self, name, progress):
        # Open top level GUI
        readerstudyroot = Toplevel()
        readerstudyGUI = MainGui(readerstudyroot, name, progress, "test")
        readerstudyroot.geometry(loadgeometry("ReaderStudyGUI"))
        readerstudyroot.attributes('-topmost', True)
        #readerstudyroot.wait_window()

    def loadreaders(self):
        filepath = os.getcwd() + "\\ReadersProgress.json"

        # Open and store file
        with open(filepath, 'r') as infile:
            self.readers = json.loads(infile.read())

    def nameexists(self, name):
        return name in self.readers


def refresh(master):
    master.destroy()

    root = Tk()
    appgui = MainWindow(root)
    root.geometry(loadgeometry("ReaderStudyApplication"))
    #root.attributes('-topmost', True)
    root.mainloop()


def stay_on_top(window):
   window.lift()
   window.after(2000, stay_on_top(window))


def loadgeometry(window):
    filepath = os.getcwd() + "\\ApplicationGeometry.json"

    with open(filepath, "r") as infile:
        applicationgeometrydict = json.loads(infile.read())

    return applicationgeometrydict[window]


if __name__ == "__main__":
    root = Tk()
    appgui = MainWindow(root)
    root.geometry(loadgeometry("ReaderStudyApplication"))
    #root.attributes('-topmost', True)
    root.mainloop()
