from tkinter import *
import os
import json
#from structures import Location, Diagnosis, Specimen


class SpecimenWindow:
    def __init__(self, master, specimendict):
        self.updatedflag = False
        self.coreNumber = specimendict["SpecimenID"]
        self.specimendict = specimendict
        master.title("%s Core Number %d" % (self.specimendict["SpecimenType"], self.coreNumber))

        # Define Variables
        self.lcr = StringVar()
        self.mlm = StringVar()
        self.amb = StringVar()
        self.pta = StringVar()
        self.amp = StringVar()
        self.ios = StringVar()
        self.asymmetry = StringVar()
        self.contrast = StringVar()
        self.texture = StringVar()
        self.margin = StringVar()
        self.description = StringVar()

        # Location RadioButtons
        Label(master, text="Location", font="Helvetica 12 underline").grid(column=0, columnspan=6, row=0, pady=(2, 2),
                                                                           padx=(2, 2))

        # LCR Required
        Label(master, text="Left or Right or Central:", font="Helvetica 10").grid(column=0, row=1, pady=(2, 2),
                                                                                  padx=(2, 2))
        Radiobutton(master, text="Left", variable=self.lcr, value="left", tristatevalue=0).grid(column=1, row=1,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))
        Radiobutton(master, text="Right", variable=self.lcr, value="right", tristatevalue=0).grid(column=2, row=1,
                                                                                                  pady=(2, 2),
                                                                                                  padx=(2, 2))
        Radiobutton(master, text="Central", variable=self.lcr, value="central", tristatevalue=0).grid(column=3, row=1,
                                                                                                      pady=(2, 2),
                                                                                                      padx=(2, 2))
        Radiobutton(master, text="NAVU", variable=self.lcr, value="NAVU", tristatevalue=0).grid(column=4, row=1,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))
        # MLM Required
        Label(master, text="Medial or Lateral or Mediolateral:", font="Helvetica 10").grid(column=0, row=2,
                                                                                           pady=(2, 2), padx=(2, 2))
        Radiobutton(master, text="Mediolateral", variable=self.mlm, value="mediolateral", tristatevalue=0).grid(
            column=3, row=2, pady=(2, 2), padx=(2, 2))

        Radiobutton(master, text="Medial", variable=self.mlm, value="medial", tristatevalue=0).grid(column=1, row=2,
                                                                                                    pady=(2, 2),
                                                                                                    padx=(2, 2))
        Radiobutton(master, text="Lateral", variable=self.mlm, value="lateral", tristatevalue=0).grid(column=2, row=2,
                                                                                                      pady=(2, 2),
                                                                                                      padx=(2, 2))
        Radiobutton(master, text="NAVU", variable=self.mlm, value="NAVU", tristatevalue=0).grid(column=4, row=2,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))
        # AMB Required
        Label(master, text="Apex or Mid-Gland or Base:", font="Helvetica 10").grid(column=0, row=3, pady=(2, 2),
                                                                                   padx=(2, 2))
        Radiobutton(master, text="Apex", variable=self.amb, value="apex", tristatevalue=0).grid(column=1, row=3,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))
        Radiobutton(master, text="Mid-Gland", variable=self.amb, value="mid-gland", tristatevalue=0).grid(column=2,
                                                                                                          row=3,
                                                                                                          pady=(2, 2),
                                                                                                          padx=(2, 2))
        Radiobutton(master, text="Base", variable=self.amb, value="base", tristatevalue=0).grid(column=3, row=3,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))
        Radiobutton(master, text="NAVU", variable=self.amb, value="NAVU", tristatevalue=0).grid(column=4, row=3,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))
        # PTA Required
        Label(master, text="PZ or TZ or AFMS:", font="Helvetica 10").grid(column=0, row=4, pady=(2, 2), padx=(2, 2))
        Radiobutton(master, text="PZ", variable=self.pta, value="peripheral zone", tristatevalue=0).grid(column=1,
                                                                                                         row=4,
                                                                                                         pady=(2, 2),
                                                                                                         padx=(2, 2))
        Radiobutton(master, text="TZ", variable=self.pta, value="transition zone", tristatevalue=0).grid(column=2,
                                                                                                         row=4,
                                                                                                         pady=(2, 2),
                                                                                                         padx=(2, 2))
        Radiobutton(master, text="AFMS", variable=self.pta, value="AFMS", tristatevalue=0).grid(column=3, row=4,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))
        Radiobutton(master, text="NAVU", variable=self.pta, value="NAVU", tristatevalue=0).grid(column=4, row=4,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))
        # AMP Required
        Label(master, text="Anterior or Mid or Posterior:", font="Helvetica 10").grid(column=0, row=5, pady=(2, 2),
                                                                                      padx=(2, 2))
        Radiobutton(master, text="Anterior", variable=self.amp, value="anterior", tristatevalue=0).grid(column=1,
                                                                                                        row=5,
                                                                                                        pady=(2, 2),
                                                                                                        padx=(2, 2))
        Radiobutton(master, text="Mid", variable=self.amp, value="mid", tristatevalue=0).grid(column=2, row=5,
                                                                                                        pady=(2, 2),
                                                                                                        padx=(2, 2))
        Radiobutton(master, text="Posterior", variable=self.amp, value="posterior", tristatevalue=0).grid(column=3,
                                                                                                          row=5,
                                                                                                          pady=(2, 2),
                                                                                                          padx=(2, 2))
        Radiobutton(master, text="NAVU", variable=self.amp, value="NAVU", tristatevalue=0).grid(column=4, row=5,
                                                                                                pady=(2, 2),
                                                                                                padx=(2, 2))

        # Notes Required
        Label(master, text="Biopsy Specimen Location Notes:", font="Helvetica 10").grid(column=0, row=6, pady=(2, 2),
                                                                                        padx=(5, 0))
        self.biopsylocationnotes = Entry(master, width=45, justify=LEFT)
        self.biopsylocationnotes.grid(column=1, columnspan=3, row=6, pady=(2, 2), padx=(0, 5))
        # Populate Notes Button
        self.populateLocationbtn = Button(master, text="Populate", bg='green', fg="white",
                                          command=lambda: self.populateNotes(master))
        self.populateLocationbtn.grid(column=4, columnspan=2, row=6, padx=(2, 2), pady=(2, 2))

        # Biopsy Specimen Characteristics
        Label(master, text="Biopsy Specimen Characteristics", font="Helvetica 12 underline").grid(column=0,
                                                                                                  columnspan=6, row=7,
                                                                                                  pady=(2, 2),
                                                                                                  padx=(2, 2))
        # Index of Suspicion Required for ARFI
        Label(master, text="Index of Suspicion:", font="Helvetica 10").grid(column=0, row=8, pady=(2, 2), padx=(2, 2))
        Radiobutton(master, text="1", variable=self.ios, value="1", tristatevalue=0).grid(column=1, row=8, pady=(2, 2),
                                                                                          padx=(2, 2))
        Radiobutton(master, text="2", variable=self.ios, value="2", tristatevalue=0).grid(column=2, row=8, pady=(2, 2),
                                                                                          padx=(2, 2))
        Radiobutton(master, text="3", variable=self.ios, value="3", tristatevalue=0).grid(column=3, row=8, pady=(2, 2),
                                                                                          padx=(2, 2))
        Radiobutton(master, text="4", variable=self.ios, value="4", tristatevalue=0).grid(column=4, row=8, pady=(2, 2),
                                                                                          padx=(2, 2))
        Radiobutton(master, text="5", variable=self.ios, value="5", tristatevalue=0).grid(column=5, row=8, pady=(2, 2),
                                                                                          padx=(2, 2))
        # IOS of each category
        self.options = ["1", "2", "3", "4", "5"]
        self.asymmetry.set("Select"), self.contrast.set("Select"), self.texture.set("Select"), self.margin.set("Select")
        Label(master, text="Category IOS:", font="Helvetica 10").grid(column=0, row=9, rowspan=2, pady=(2, 2), padx=(2, 2))
        Label(master, text="Asymmetry").grid(column=1, row=9, pady=(2, 2), padx=(2, 2))
        Label(master, text="Contrast").grid(column=2, row=9, pady=(2, 2), padx=(2, 2))
        Label(master, text="Texture").grid(column=3, row=9, pady=(2, 2), padx=(2, 2))
        Label(master, text="Margin").grid(column=4, row=9, pady=(2, 2), padx=(2, 2))
        OptionMenu(master, self.asymmetry, *self.options).grid(column=1, row=10, pady=(2, 2), padx=(2, 2))
        OptionMenu(master, self.contrast, *self.options).grid(column=2, row=10, pady=(2, 2), padx=(2, 2))
        OptionMenu(master, self.texture, *self.options).grid(column=3, row=10, pady=(2, 2), padx=(2, 2))
        OptionMenu(master, self.margin, *self.options).grid(column=4, row=10, pady=(2, 2), padx=(2, 2))

        # F Number
        Label(master, text="Fiducial Number:", font="Helvetica 10").grid(column=1, columnspan=1, row=11, padx=(2, 2), pady=(2, 2))
        self.fnumber = Entry(master, width=10, justify=LEFT)
        self.fnumber.grid(column=2, row=11, columnspan=1, padx=(2, 2), pady=(2, 2))

        # Submit Button
        self.submitcorebtn = Button(master, text="Submit Core", bg='green', fg="white",
                                    command=lambda: self.submitCore(master))
        self.submitcorebtn.grid(column=0, columnspan=7, row=12, padx=(2, 2), pady=(2, 2))

        # Validate Response
        self.invalidCoreEntry = Label(master, text="*Incomplete Core", font="Helvetica 10", fg="red")

        # Set Variables
        self.setvariables()

    def setvariables(self):
        """
        Initialize top level with input dictionary
        Returns:

        """
        # Set location radiobuttons
        self.lcr.set(self.specimendict["Location"]["lcr"])
        self.mlm.set(self.specimendict["Location"]["mlm"])
        self.amb.set(self.specimendict["Location"]["amb"])
        self.pta.set(self.specimendict["Location"]["pta"])
        self.amp.set(self.specimendict["Location"]["amp"])

        # Set IOS
        self.ios.set(self.specimendict["IndexOfSuspicion"])

        # Set required entry box
        self.setnonevariable(self.specimendict["Location"]["Notes"], self.biopsylocationnotes)

        # Set F number
        self.setnonevariable(self.specimendict["FiducialNumber"], self.fnumber)

        # Set IOS Categories
        self.asymmetry.set(self.specimendict["IOSCategories"]["Asymmetry"])
        self.contrast.set(self.specimendict["IOSCategories"]["Contrast"])
        self.texture.set(self.specimendict["IOSCategories"]["Texture"])
        self.margin.set(self.specimendict["IOSCategories"]["Margin"])

    def populateNotes(self, master):
        """
        Populate Location Notes based on Location Entries
        Args:
            master: GUI

        Returns:

        """
        self.biopsylocationnotes.delete(0, END)  # Delete Current Entry
        location = " " + self.lcr.get() + " " + self.mlm.get() + " " + self.amb.get() + " " + self.pta.get() + " "  # Create Location Entry
        self.biopsylocationnotes.insert(END, (location.replace(" NAVU", "") + "prostate").strip())

    def populateioscategories(self, master):
        """

        Args:
            master:

        Returns:

        """
        print(self.asymmetry.get())
        print(self.contrast.get())
        print(self.texture.get())
        print(self.margin.get())
        print(self.ios.get())
        if self.asymmetry.get() == "Select":
            self.asymmetry.set(self.ios.get())
        if self.contrast.get() == "Select":
            self.contrast.set(self.ios.get())
        if self.texture.get() == "Select":
            self.texture.set(self.ios.get())
        if self.margin.get() == "Select":
            self.margin.set(self.ios.get())

    def setnonevariable(self, specimendictindex, guivariable):
        """
        Required Entry boxes may be None to begin and need handling to initialize
        Args:
            specimendictindex: Contents of required entry
            guivariable: Required entry box of gui

        Returns:

        """
        if specimendictindex is None or specimendictindex == "":
            pass  # Do not place anything in entry box if value is None
        else:
            guivariable.insert(END, specimendictindex)  # Insert stored value if present

    def validatecore(self):
        """
        Check if core has been completed to allow submission
        Returns:

        """
        # Check all information checked
        print(self.specimendict)
        if "" not in self.specimendict["Location"].values() and "" != self.specimendict["IndexOfSuspicion"] and "F-" != self.specimendict["FiducialNumber"]:
            return True

        return False

    def submitCore(self, master):
        """
        Check if core valid and close top level window
        Args:
            master:

        Returns:

        """
        # Populate location notes
        self.populateNotes(master)

        # Populate IOS of each category if not already set
        self.populateioscategories(master)

        # Update return dictionary using values inputted
        self.updatespecimendict()

        # Submit if core valid
        if self.validatecore():
            # Close Window and Return specimendict
            self.updatedflag = True
            master.destroy()
        else:
            # Should indicate which entries not complete
            self.invalidCoreEntry.grid(column=0, row=11, pady=(2, 2), padx=(2, 2))

    def updatespecimendict(self):
        """
        Update Specimen Dictionary being returned
        Returns:

        """
        self.specimendict["Location"] = {"lcr": self.lcr.get(), "mlm": self.mlm.get(), "amb": self.amb.get(),
                                         "pta": self.pta.get(), "amp": self.amp.get(),
                                         "Notes": self.biopsylocationnotes.get()}
        self.specimendict["IndexOfSuspicion"] = self.ios.get()
        self.specimendict["FiducialNumber"] = self.fnumber.get()
        self.specimendict["IOSCategories"] = {"Asymmetry": self.asymmetry.get(), "Contrast": self.contrast.get(),
                                              "Texture": self.texture.get(), "Margin": self.margin.get()}


def initializeSpecimen(specimenType, corenumber):
    """
    Initialize a new core
    Args:
        specimenType: specimen type ARFI, MR, SOC
        corenumber: Core Number

    Returns:

    """
    # Initialize Specimen
    specimendict = dict()
    specimendict["SpecimenType"] = specimenType
    specimendict["SpecimenID"] = corenumber
    specimendict["Location"] = {"lcr": "NAVU", "mlm": "NAVU", "amb": "NAVU", "pta": "NAVU", "amp": "NAVU", "Notes": ""}
    specimendict["SpecimenNotes"] = ""
    specimendict["IndexOfSuspicion"] = ""
    specimendict["IOSCategories"] = {"Asymmetry": "Select", "Contrast": "Select", "Texture": "Select", "Margin": "Select"}
    specimendict["FiducialNumber"] = "F-"
    specimendict["LateralLocation"] = ""
    specimendict["AxialLocation"] = ""
    specimendict["DepthLocation"] = ""

    return specimendict


def loadgeometry(window):
    filepath = os.getcwd() + "\\ApplicationGeometry.json"

    with open(filepath, "r") as infile:
        applicationgeometrydict = json.loads(infile.read())

    return applicationgeometrydict[window]


if __name__ == "__main__":
    specimendict = initializeSpecimen("ARFI", 1)

    toplevelroot = Tk()
    toplevelGUI = SpecimenWindow(toplevelroot, specimendict)
    toplevelroot.geometry(loadgeometry("readerstudytoplevel"))
    toplevelroot.mainloop()
