import tkinter.simpledialog
from tkinter import *
from tkinter import ttk, filedialog
from readerstudytoplevel import SpecimenWindow
import json
import os
import CompileReaderStudy
import math
import slicer
import time


class MainGui:
    def __init__(self, master, name, progress, studysection):
        # Create Master Frame, Name, Labels
        master.title("Reader Study")
        self.validationdict = dict()
        self.patientdict = dict()
        self.ARFIdict = dict()
        self.validated = 0
        self.timeelapsed = 0
        self.slicerpath = self.getslicerpath()
        self.studysection = studysection
        if self.studysection == "test":
            self.caseorder = self.loadcaseorder()
            self.progressindex = self.caseorder.index(progress)
        else:
            iosbucket = progress[1]
            progress = progress[0]
            self.caseorder = self.loadtrainingcaseorder()
            self.progressindex = self.caseorder.index(progress)
            self.trainingios = self.loadtrainingcaseIOS()

        # Patient and Reader Name Label
        Label(master, text="Case Number\tReader Name", font="Helvetica 12").grid(column=1, row=0, pady=(5, 5))
        self.labelButtons = Frame(master)
        self.labelButtons.grid(column=1, row=1, padx=(0, 0), pady=(5, 5))
        self.caseNumberEntry = Entry(self.labelButtons, width=15, justify=CENTER)
        self.caseNumberEntry.grid(column=0, row=0, pady=(5, 5), padx=(5, 60))
        self.caseNumberEntry.insert(END, progress)
        # Reader Name Label
        self.readerIDEntry = Entry(self.labelButtons, width=15, justify=CENTER)
        self.readerIDEntry.grid(column=1, row=0, pady=(5, 5), padx=(0, 0))
        self.readerIDEntry.insert(END, name)
        self.AdditionalFrames = False

        # ARFI Labels
        self.ARFICoresNumber = 0
        self.ARFIbuttons = dict()
        Label(master, text="ARFI Cores", font="Helvetica 10 underline").grid(column=1, row=2, pady=(5, 5), padx=(5, 5))
        self.ARFIbtn = Button(master, text="Add ARFI Core", bg="purple1", fg="white",
                              command=lambda: self.addARFICore(master))
        self.ARFIbtn.grid(column=1, row=self.ARFICoresNumber + 3, pady=(5, 5), padx=(5, 5))
        self.removeARFIbtn = Button(master, text="Remove ARFI Core", bg="purple3", fg="white",
                                    command=lambda: self.removeARFICore(master))
        self.removeARFIbtn.grid(column=1, row=self.ARFICoresNumber + 4, pady=(5, 5), padx=(5, 5))

        # Patient Notes Entry
        self.ptlabel = Label(master, text="Patient Review Notes:", font="Helvetica 10")
        self.ptlabel.grid(column=0, row=self.ARFICoresNumber + 5, padx=(5, 5), pady=(5, 5))
        self.reviewNotesEntry = Entry(master, width=50, justify=LEFT)
        self.reviewNotesEntry.insert(END, "NA")
        self.reviewNotesEntry.grid(column=1, columnspan=2, row=self.ARFICoresNumber + 5, padx=(5, 5), pady=(5, 5))

        # Submission Label
        self.submitCasebtn = Button(master, text="Submit Case", bg='green', fg="white", state=DISABLED,
                                    command=lambda: self.submitCase(master))
        self.submitCasebtn.grid(column=2, row=1, padx=(15, 5), pady=(5, 5))

        # New Case Label
        self.newCasebtn = Button(master, text="Clear Case", bg="green", fg="white",
                                 command=lambda: newCase(master, name, progress, self.studysection))
        self.newCasebtn.grid(column=0, row=1, padx=(5, 5), pady=(5, 5))

        # Load Case Label
        self.loadCasebtn = Button(master, text="Load Case", bg="green", fg="white",
                                  command=lambda: self.loadCase(master))
        self.loadCasebtn.grid(column=0, row=0, padx=(5, 5), pady=(5, 5))

        # Refresh Label
        self.refreshbtn = Button(master, text="Refresh", bg="green", fg="white",
                                 command=lambda: self.validateSubmitButton(master))
        self.refreshbtn.grid(column=2, row=0, padx=(15, 5), pady=(5, 5))

        # Initialization
        self.validationdict = {"ARFI": {}}

        # Validate Submit Error Display
        self.errorDisplay = Label(master, text="", font="Helvetica 10", fg="red")

        # Add next case button
        self.nextcasebtn = Button(master, text="Next Case", bg="blue", fg="white", state=DISABLED,
                                  command=lambda: self.nextcase(master))
        self.nextcasebtn.grid(column=2, row=2, pady=(5, 5), padx=(5, 5))

        # Most Suspicious to Least Suspicious Label:
        Label(master, text="Most Suspicious ->", font="Helvetica 10").grid(column=0, row=3, pady=(5, 5), padx=(5, 5))
        self.leastlabel = Label(master, text="Least Suspicious ->", font="Helvetica 10")
        self.leastlabel.grid(column=0, row=3, pady=(5, 5), padx=(5, 5))
        self.leastlabel.grid_remove()

        # Study Progress Display
        Label(master, text="Progress: %d/%d" % (self.progressindex+1,
                                                len(self.caseorder)), font="Helvetica 10").grid(column=2,
                                                                                                  row=3,
                                                                                                  pady=(5, 5),
                                                                                                  padx=(5, 5))

        # Add previous case button
        self.previouscasebtn = Button(master, text="Previous Case", bg="blue", fg="white",
                                      command=lambda: self.previouscase(master))
        self.previouscasebtn.grid(column=0, row=2, pady=(5, 5), padx=(5, 5))

        # Load case
        filepath = os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get() + "\\" + self.caseNumberEntry.get() + "_" + self.readerIDEntry.get() + "ReaderStudy.json"
        if os.path.exists(filepath):
            with open(filepath, 'r') as infile:
                self.patientdict = json.loads(infile.read())

            # Populate loaded json
            self.populateARFI(master)

            # Populate case number and ReviewNotes
            self.caseNumberEntry.delete(0, END)
            self.caseNumberEntry.insert(END, self.patientdict["SubjectID"])
            self.reviewNotesEntry.delete(0, END)
            self.reviewNotesEntry.insert(END, self.patientdict["ReviewNotes"])
            self.readerIDEntry.delete(0, END)
            self.readerIDEntry.insert(END, self.patientdict["ReaderID"])

            # Validate submit button
            self.validateSubmitButton(master)

        else:
            # Automatically populate first ARFI
            self.addARFICore(master)

        # Control Slicer
        if self.studysection == "test":
            self.controlslicer(self.caseNumberEntry.get())
        else:
            self.controlslicer(self.caseNumberEntry.get(), self.trainingios)

        # Start timer
        self.starttime = time.time()

        # If Training, deactivate certain buttons and change functions of other buttons to prevent functionality
        if self.studysection == "training":
            self.previouscasebtn.configure(state=DISABLED)
            self.loadCasebtn.configure(state=DISABLED)
            self.submitCasebtn.configure(command=lambda: self.trainingsubmit(master, iosbucket))

    def trainingsubmit(self, master, iosbucket):
        print("OPEN")
        case = self.caseNumberEntry.get()
        # Open Training File
        os.system('start %s' % (os.getcwd() + "\\Training\\" + iosbucket + "\\" + case + "\\%s_TrainingDocument.pdf" % case))
        self.submitCase(master)

    def getslicerpath(self):
        with open("..\\slicerpath.txt", "r") as infile:
            slicerpath = infile.readlines()

        return os.path.abspath(slicerpath[0])

    def loadcaseorder(self):
        """

        Returns:

        """
        filepath = os.getcwd() + "\\StudyOrder.csv"

        # Open and store file
        with open(filepath, "r") as infile:
            caseorder = (infile.read()).split("\n")

        # Remove space
        for index in range(0, len(caseorder)-1):
            caseorder[index] = caseorder[index].strip()

        return caseorder

    def loadtrainingcaseorder(self):
        filepath = os.getcwd() + "\\Training\\TrainingOrder.csv"

        # Open and store file
        with open(filepath, "r") as infile:
            cases = (infile.read()).split("\n")

        # Remove space
        for index in range(0, len(cases)):
            cases[index] = cases[index].strip().split(",")[0]

        return cases

    def loadtrainingcaseIOS(self):
        filepath = os.getcwd() + "\\Training\\TrainingOrder.csv"

        # Open and store file
        with open(filepath, "r") as infile:
            ios = (infile.read()).split("\n")

        # Remove space
        for index in range(0, len(ios)):
            ios[index] = ios[index].strip().split(",")[1]

        return ios[self.progressindex]

    def controlslicer(self, casenumber, ios=None):
        """

        Returns:

        """
        # Save F-node
        try:
            self.savefnode()

            # Close current Scene
        except AttributeError:
            print("No Scene Open")

        # Open next scene
        if self.studysection == "test":
            # If prior scene exists, open that scene
            if any(fname.endswith('.mrml') for fname in os.listdir(os.getcwd()+"\\"+casenumber+"\\slicer\\"+self.readerIDEntry.get()+"\\")):
                filepath = os.getcwd()+"\\"+casenumber+"\\slicer\\"+self.readerIDEntry.get()+"\\"
            # Else, open normal scene
            else:
                filepath = os.getcwd()+"\\"+casenumber+"\\slicer\\"
        else:
            filepath = os.getcwd() + "\\Training\\"+ios+"\\"+casenumber+"\\slicer\\"
        for file in os.listdir(filepath):
            if file.endswith(".mrml"):
                slicerscene = filepath + file
        os.system('start %s %s' % (self.slicerpath, slicerscene))

    def savefnode(self):
        fnode = slicer.getNode('F')
        storagenode = fnode.CreateDefaultStorageNode()
        nodepath = os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get() + "\\F.mrk.json"
        storagenode.SetFileName(nodepath)
        storagenode.WriteData(fnode)

    def nextcase(self, master):
        """

        Args:
            master:
            name:
            progress:

        Returns:

        """
        progresscase = self.caseorder[self.progressindex+1]
        newCase(master, self.readerIDEntry.get(), progresscase, self.studysection)
        #self.controlslicer(progresscase)

    def previouscase(self, master):
        """

        Args:
            master:
            name:
            progress:

        Returns:

        """
        if self.progressindex > 0:
            progresscase = self.caseorder[self.progressindex-1]
            newCase(master, self.readerIDEntry.get(), progresscase, self.studysection)
            #self.controlslicer(progresscase)

    def loadCase(self, master):
        """
        Load presaved Case
        Args:
            master: GUI

        Returns:

        """
        # Open Json
        self.openFile()

        # Populate loaded json
        self.populateARFI(master)

        # Populate case number and ReviewNotes
        self.caseNumberEntry.delete(0, END)
        self.caseNumberEntry.insert(END, self.patientdict["SubjectID"])
        self.reviewNotesEntry.delete(0, END)
        self.reviewNotesEntry.insert(END, self.patientdict["ReviewNotes"])
        self.readerIDEntry.delete(0, END)
        self.readerIDEntry.insert(END, self.patientdict["ReaderID"])

        # Validate submit button
        self.validateSubmitButton(master)

        # Control slicer
        self.controlslicer(self.caseNumberEntry.get())

        # Start timer
        self.starttime = time.time()

    def populateARFI(self, master):
        """
        Loop through and populate each ARFI core with information stored
        Args:
            master:

        Returns:

        """
        for core in self.patientdict["ARFICores"]:
            self.ARFIdict[int(core)] = self.patientdict["ARFICores"][core]  # Store core
            self.ARFICoresNumber += 1  # Iterate total number of ARFI cores
            self.validationdict["ARFI"][self.ARFICoresNumber] = True  # Validate core entry

            # Adjust ARFI Button locations
            self.ARFIbuttons[self.ARFICoresNumber] = Button(master, text=str(self.ARFICoresNumber), bg='green',
                                                            fg='white',
                                                            command=lambda a=self.ARFICoresNumber: self.inputARFICore(
                                                                master, a))
            self.ARFIbuttons[self.ARFICoresNumber].grid(column=1, row=self.ARFICoresNumber + 2, pady=(5, 5),
                                                        padx=(5, 5))
            self.ARFIbtn.grid(column=1, row=self.ARFICoresNumber + 3)
            self.removeARFIbtn.grid(column=1, row=self.ARFICoresNumber + 4)

            # Adjust Review entry
            self.ptlabel.grid(column=0, row=self.ARFICoresNumber + 5, padx=(5, 5), pady=(5, 5))
            self.reviewNotesEntry.grid(column=1, columnspan=2, row=self.ARFICoresNumber + 5, padx=(5, 5),
                                       pady=(5, 5))

            # Adjust label
            if self.ARFICoresNumber > 1:
                self.leastlabel.grid(column=0, row=self.ARFICoresNumber + 2, padx=(5, 5), pady=(5, 5))

            # Check if ARFI Cores has IOSCategories
            if "IOSCategories" not in self.ARFIdict[int(core)]:
                ios = self.ARFIdict[int(core)]["IndexOfSuspicion"]
                self.ARFIdict[int(core)]["IOSCategories"] = {"Asymmetry": "Select", "Contrast": "Select", "Texture": "Select", "Margin": "Select"}
                self.ARFIbuttons[self.ARFICoresNumber].configure(bg='red')

    def openFile(self):
        """
        Open json to load
        Returns:

        """
        ftypes = [('json files', '*.json'), ('All Files', '*')]  # Specify json filetype
        filepath = os.path.abspath(filedialog.askopenfilename(filetypes=ftypes))

        # Open and store file
        with open(filepath, 'r') as infile:
            self.patientdict = json.loads(infile.read())

    def initializeSpecimen(self, specimenType, corenumber):
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
        self.ARFIdict[corenumber] = specimendict

    def addARFICore(self, master):
        """
        Add and initialize new ARFI Core
        Args:
            master: GUI

        Returns:

        """
        if self.ARFICoresNumber < 4:
            self.ARFICoresNumber += 1  # Store increase in ARFI Cores saved
            self.initializeSpecimen("ARFI", self.ARFICoresNumber)  # Initialize new ARFI Core
            self.validationdict["ARFI"][self.ARFICoresNumber] = False  # Signal new core needing validation
            self.errorDisplay.destroy()

            # Move ARFI Buttons
            self.ARFIbuttons[self.ARFICoresNumber] = Button(master, text=str(self.ARFICoresNumber), bg='red', fg='white',
                                                            command=lambda a=self.ARFICoresNumber: self.inputARFICore(
                                                                master, a))
            self.ARFIbuttons[self.ARFICoresNumber].grid(column=1, row=self.ARFICoresNumber + 2, pady=(5, 5), padx=(5, 5))
            self.ARFIbtn.grid(column=1, row=self.ARFICoresNumber + 3)
            self.removeARFIbtn.grid(column=1, row=self.ARFICoresNumber + 4)

            # Move Review Notes entry
            self.ptlabel.grid(column=0, row=self.ARFICoresNumber + 5, padx=(5, 5), pady=(5, 5))
            self.reviewNotesEntry.grid(column=1, columnspan=2, row=self.ARFICoresNumber + 5, padx=(5, 5),
                                       pady=(5, 5))

            # Adjust least suspicous label
            self.leastlabel.grid(column=0, row=self.ARFICoresNumber + 2, padx=(5, 5), pady=(5, 5))

            # Revalidate submit button - should turn submission off
            self.validateSubmitButton(master)

    def removeARFICore(self, master):
        """
        Remove existing ARFI Core
        Args:
            master: GUI

        Returns:

        """
        # Remove only if core exists
        if validateCoreNumber(self.ARFICoresNumber) and self.ARFICoresNumber > 1:
            self.ARFIbuttons[self.ARFICoresNumber].destroy()  # Remove ARFI Button
            self.ARFIdict.pop(self.ARFICoresNumber)  # Remove Core from temp dict
            self.validationdict["ARFI"].pop(self.ARFICoresNumber)  # Do not require core validation
            self.ARFICoresNumber -= 1  # Signal removal of core from total number present
            self.errorDisplay.destroy()

            # Move ARFI Buttons
            self.ARFIbtn.grid(column=1, row=self.ARFICoresNumber + 3)
            self.removeARFIbtn.grid(column=1, row=self.ARFICoresNumber + 4)

            # Move review Notes Entry
            self.ptlabel.grid(column=0, row=self.ARFICoresNumber + 5, padx=(5, 5), pady=(5, 5))
            self.reviewNotesEntry.grid(column=1, columnspan=2, row=self.ARFICoresNumber + 5, padx=(5, 5),
                                       pady=(5, 5))

            # Adjust Least Suspicous Label
            self.leastlabel.grid(column=0, row=self.ARFICoresNumber + 2, padx=(5, 5), pady=(5, 5))
            if self.ARFICoresNumber <= 1:
                self.leastlabel.grid_remove()

            # Validate Submit Button
            self.validateSubmitButton(master)

    def inputCore(self, master, specimendict):
        """
        Pop up top level to allow inputting information of new core
        Args:
            master: GUI
            specimendict: storage of existing core information

        Returns:

        """
        # Open top level GUI
        toplevelroot = Toplevel()
        toplevelGUI = SpecimenWindow(toplevelroot, specimendict)
        toplevelroot.geometry(loadgeometry("readerstudytoplevel"))
        toplevelroot.attributes('-topmost', True)
        toplevelroot.wait_window()

        # Check if core entry was completed upon close of top level
        if toplevelGUI.updatedflag:
            # Update temp dict with new information
            self.updateCoreDicts(toplevelGUI.specimendict)

            # Validate submit button
            self.validateSubmitButton(master)

        return toplevelGUI.updatedflag

    def inputARFICore(self, master, coreNumber):
        """
        Input and store new ARFI core information
        Args:
            master: GUI
            coreNumber: Core Number

        Returns:

        """
        # Pop up required entry for ARFI Core and submit button
        valid = self.inputCore(master, self.ARFIdict[coreNumber])

        # Upon validated TopLevel submit, change button color and validate cases
        if valid:
            self.ARFIbuttons[coreNumber].configure(bg='green')

    def displayErrors(self, errors, master):
        """
        Checks validity of all value and displays errors to user
        Args:
            errors: dataframe errors

        Returns:

        """
        errorText = ""
        for error in errors:
            errorText = errorText + ("ARFI Core %d Error on Column %s\n" % (error.row + 1, error.column))

        self.errorDisplay.destroy()
        self.errorDisplay = Label(master, text=errorText, font="Helvetica 10", fg="red")
        self.errorDisplay.grid(column=0, columnspan=5, row=self.ARFICoresNumber + 6, padx=(5, 5), pady=(5, 5))

    def validateFiducialLocations(self):
        """
        Validate fiducial locations json exists

        Returns:

        """
        validatepath = os.path.exists(os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get() + "\\fiducialLocations.json")
        validatenumbers = False
        if validatepath:
            filepath = os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get() + "\\fiducialLocations.json"
            with open(filepath, "r") as infile:
                data = json.loads(infile.read())

            validatenumbers = len(data["Fiducial Location"]) == self.ARFICoresNumber
        return validatepath and validatenumbers

    def validateSubmitButton(self, master):
        """
        Check if all cores are complete to allow submission of case
        Returns:

        """
        # Check if all inputted cases are validated and case number and review notes entered
        if False not in self.validationdict["ARFI"].values() and \
                self.validateSubjectID() and self.validateReviewNotes() and self.validateReaderID():

            # Create dictionary
            self.createPatientDict()

            if self.validateFiducialLocations():
                # Fiducial Locations
                self.addFiducialLocations()

            errors = CompileReaderStudy.validateSubmit(self.patientdict)

            # Display Errors to fix before submit
            if len(errors) > 0:
                # Display errors on GUI
                self.displayErrors(errors, master)
                #if not self.validateFiducialLocations():
                #    self.errorDisplay = Label(master,
                #                              text="FiducialLocations.json does not exist or Invalid Number of Fiducials",
                #                              font="Helvetica 10",
                #                              fg="red")
                #    self.errorDisplay.grid(column=0, columnspan=5,
                #                           row=self.ARFICoresNumber + 7, padx=(5, 5), pady=(5, 5))

                # Configure Submit button
                self.submitCasebtn.configure(state=DISABLED, bg='green', fg="white")
                self.nextcasebtn.configure(state=DISABLED)

            else:
                # Configure Submit Button
                self.errorDisplay.destroy()
                self.submitCasebtn.configure(state=NORMAL, bg='green', fg="white")
                filepath = os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get() + "\\" + self.caseNumberEntry.get() + "_" + self.readerIDEntry.get() + "ReaderStudy.json"
                if os.path.exists(filepath):
                    self.nextcasebtn.configure(state=NORMAL)

        else:
            self.errorDisplay.destroy()
            self.submitCasebtn.configure(state=DISABLED, bg='green', fg="white")
            self.nextcasebtn.configure(state=DISABLED)

    def validateSubjectID(self):
        """
        Validate subject ID is entered
        Returns:

        """
        return self.caseNumberEntry.get() != ""

    def validateReaderID(self):
        """
        Validate ReaderID is entered
        Returns:

        """
        return self.readerIDEntry.get() != ""

    def validateReviewNotes(self):
        """
        Validate review notes are entered
        Returns:

        """
        return self.reviewNotesEntry.get() != ""

    def addFiducialLocations(self):
        """

        Returns:

        """
        fiduciallocationsfilepath = os.path.abspath(os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get() + "\\fiducialLocations.json")
        with open(fiduciallocationsfilepath, "r") as infile:
            data = json.loads(infile.read())

        for coretype in self.patientdict:
            if coretype == "ARFICores":
                for core in self.patientdict[coretype]:
                    # Store appropriate location data of core
                    lateral = data["Depths"][int(core) - 1] * math.sin(
                        math.radians(data["Encoder Angles"][int(core) - 1]))
                    axial = data["Depths"][int(core) - 1] * math.cos(
                        math.radians(data["Encoder Angles"][int(core) - 1]))
                    depth = data["Distances"][int(core) - 1]

                    self.patientdict[coretype][core]["LateralLocation"] = lateral
                    self.patientdict[coretype][core]["AxialLocation"] = axial
                    self.patientdict[coretype][core]["DepthLocation"] = depth

            elif coretype in ["SOCCores", "MRCores"]:
                for core in self.patientdict[coretype]:
                    self.patientdict[coretype][core]["LateralLocation"] = "NAVU"
                    self.patientdict[coretype][core]["AxialLocation"] = "NAVU"
                    self.patientdict[coretype][core]["DepthLocation"] = "NAVU"

    def submitCase(self, master):
        """
        Create saved patient dictionary and prompt to find location for saving json
        Args:
            master: GUI

        Returns:

        """
        if self.studysection == "test":
            # End time
            self.timeelapsed = (time.time() - self.starttime) / 60

            # Create Patient dict
            self.createPatientDict()

            # Fiducial Locations
            if os.path.exists(os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get() + "\\fiducialLocations.json"):
                self.addFiducialLocations()

            # Dump Patient Dict to File Location
            filename = str(self.patientdict["SubjectID"] + "_" + str(self.patientdict["ReaderID"]) + "ReaderStudy.json")
            initialdir = os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get()
            #filepath = os.path.abspath(filedialog.asksaveasfilename(initialfile=filename, initialdir=initialdir))
            filepath = initialdir + "\\" + filename
            print(filepath)
            with open(filepath, 'w') as outfile:
                json.dump(self.patientdict, outfile, indent=4, sort_keys=True)

            # Add Reader Study to ARFI II Reader Study Export
            #filepath = os.path.abspath(filedialog.askdirectory(initialdir=os.getcwd()))
            filepath = os.getcwd()
            print(filepath)
            CompileReaderStudy.submit(self.patientdict, filepath)

            # If submission is beyond where current progress is, then update submission. Otherwise, ignore.
            progressindex = self.caseorder.index(self.caseNumberEntry.get())
            if progressindex == self.progressindex:
                # Update
                readersprogress = self.loadreaders()
                readersprogress[self.readerIDEntry.get()] = self.caseorder[self.progressindex + 1]
                with open(os.getcwd() + "\\ReadersProgress.json", 'w') as outfile:
                    json.dump(readersprogress, outfile, indent=4, sort_keys=True)

        filepath = os.getcwd() + "\\" + self.caseNumberEntry.get() + "\\slicer\\" + self.readerIDEntry.get() + "\\" + self.caseNumberEntry.get() + "_" + self.readerIDEntry.get() + "ReaderStudy.json"

        # Save F node
        #self.savefnode()

        if os.path.exists(filepath) or self.studysection == "training":
            self.nextcasebtn.configure(state=NORMAL)

        self.submitCasebtn.configure(state=DISABLED, bg='darkgreen', fg="white")

        if self.studysection == "test":
            # Add box to remind user to save Slicer Scene in their directory
            popupmsg("Reminder", "SAVE SLICER SCENE TO YOUR DIRECTORY BEFORE PROCEEDING")
        else:
            popupmsg("TRAINING", "Compare your targets with the training document")

    def loadreaders(self):
        filepath = os.getcwd() + "\\ReadersProgress.json"

        # Open and store file
        with open(filepath, 'r') as infile:
            readers = json.loads(infile.read())

        return readers

    def updateCoreDicts(self, returneddict):
        """
        Add new cores to temp dictionaries for storage
        Args:
            returneddict: top level gui dict to store in temp

        Returns:

        """
        self.ARFIdict[returneddict["SpecimenID"]] = returneddict
        self.validationdict["ARFI"][returneddict["SpecimenID"]] = True

    def createPatientDict(self):
        """
        Create patient dictionary for saving json file of case
        Returns:

        """
        self.patientdict = dict()
        self.patientdict["SubjectID"] = self.caseNumberEntry.get()  # Store subject ID
        self.patientdict["ReaderID"] = self.readerIDEntry.get()  # Store Reader ID
        self.patientdict["ARFICores"] = self.ARFIdict  # Store all ARFI cores saved
        self.patientdict["ReviewNotes"] = self.reviewNotesEntry.get()  # Pull patient case information
        self.patientdict["ReviewTime"] = self.timeelapsed


def newCase(master, name, progress, studysection):
    """
    Destroy and rest GUI for new Case
    Args:
        master: GUI

    Returns:

    """
    # Destroy existing GUI with all information
    master.destroy()

    # Pop up new GUI
    root = Tk()
    ARFI_gui = MainGui(root, name, progress, studysection)
    root.geometry(loadgeometry("ReaderStudyGUI"))
    root.attributes('-topmost', True)
    root.mainloop()


def validateCoreNumber(corenumber):
    """
    Validate core exists
    Args:
        corenumber:

    Returns:

    """
    return corenumber > 0


class CustomButton(Canvas):
    def __init__(self, parent, width, height, color, command=None):
        """
        Create Custom round button
        Args:
            parent:
            width:
            height:
            color:
            command:
        """
        Canvas.__init__(self, parent, borderwidth=1,
                        relief="raised", highlightthickness=0)
        self.command = command

        padding = 4
        id = self.create_oval((padding, padding,
                               width + padding, height + padding), outline=color, fill=color)
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1 - x0) + padding
        height = (y1 - y0) + padding
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()


def popupmsg(title, msg):
    popup = tkinter.Tk()
    popup.wm_title(title)
    label = ttk.Label(popup, text=msg, foreground="Red")
    label.pack(side="top", fill="x", pady=(10, 10), padx=(10, 10))
    B1 = ttk.Button(popup, text="Close", command=popup.destroy)
    B1.pack()
    popup.attributes('-topmost', True)
    popup.geometry(loadgeometry("popupmsg"))
    popup.mainloop()


def loadgeometry(window):
    filepath = os.getcwd() + "\\ApplicationGeometry.json"

    with open(filepath, "r") as infile:
        applicationgeometrydict = json.loads(infile.read())

    return applicationgeometrydict[window]


if __name__ == '__main__':
    root = Tk()
    ARFI_gui = MainGui(root, "test", "Patient101", "test")
    root.geometry(loadgeometry("ReaderStudyGUI"))
    root.attributes('-topmost', True)
    root.mainloop()
