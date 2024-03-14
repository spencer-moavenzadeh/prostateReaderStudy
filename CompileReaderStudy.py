import csv
import pandas as pd
import pandas_schema
import tkinter as tk
from tkinter import filedialog
import easygui
import os
import json
from pandas_schema import Column
from pandas_schema.validation import CustomElementValidation
import numpy as np


def createdf(df1, core, specimenID, readerID, reviewtime):
    """
    Append new core to existing case dataframe
    Required Columns return None if not valid
    Non-required Columns return np.nan if not valid
    Args:
        df1: current data frame containing previous cores
        core: New Core
        specimenID: Specimen identifier - primary key

    Returns:

    """
    # Create new core df
    df = pd.DataFrame({
        'CaseID': specimenID,  # Required
        'ReaderID': readerID,  # Required
        'SpecimenType': validateSpecimenType(core["SpecimenType"]),  # Required
        'amb': validateamb(core["Location"]["amb"]),  # Required
        'lcr': validatelcr(core["Location"]["lcr"]),  # Required
        'mlm': validatemlm(core["Location"]["mlm"]),  # Required
        'pta': validatepta(core["Location"]["pta"]),  # Required
        'amp': validateamp(core["Location"]["amp"]),  # Required
        'LocationNotes': str(core["Location"]["Notes"]),  # Required
        'ios': validateios(core["IndexOfSuspicion"]),  # Required
        'FiducialNumber': validatefnumber(core["FiducialNumber"]),  # Required
        'Asymmetry': validateioscategory(core["IOSCategories"]["Asymmetry"]),
        'Contrast': validateioscategory(core["IOSCategories"]["Contrast"]),
        'Texture': validateioscategory(core["IOSCategories"]["Texture"]),
        'Margin': validateioscategory(core["IOSCategories"]["Margin"]),
        'LateralLocation': validateCoreLocation(core["LateralLocation"]),  # Required if ARFI Core
        'AxialLocation': validateCoreLocation(core["AxialLocation"]),  # Required if ARFI Core
        'DepthLocation': validateCoreLocation(core["DepthLocation"]),  # Required if ARFI Core
        'ReviewTime': validateTime(reviewtime),
        'GleasonScore': np.nan,
        'LocationDescription': np.nan,
        'Study': 'ReaderStudy'
    }, index=[0])

    # Concat new core with existing case df
    return pd.concat([df1, df], ignore_index=True).reset_index(drop=True)


def validateioscategory(ioscategory):
    """

    Args:
        ioscategory:

    Returns:

    """
    try:
        if 1 <= int(ioscategory) <= 5:
            return int(ioscategory)
        else:
            return None
    except ValueError:
        return None


def validateamp(amp):
    """
    Validate column is valid amp location
    Args:
        amp: column value

    Returns:

    """
    if amp in ["anterior", "mid", "posterior"]:
        return amp
    elif amp == "NAVU":
        return np.nan
    return None


def validateTime(reviewtime):
    """

    Args:
        reviewtime:

    Returns:

    """
    if reviewtime > 0:
        return reviewtime
    else:
        return np.nan


def validatefnumber(fnumber):
    """
    Validate Fiducial number is given
    Args:
        fnumber:

    Returns:

    """
    if fnumber == "":
        return None
    else:
        return fnumber


def validateCoreLocation(corelocation):
    """
    Validate core location is float if coretype is ARFI
    Args:
        corelocation:

    Returns:

    """
    if corelocation == "":
        return "NAVU"
    try:
        float(corelocation)
    except ValueError:
        return None
    return float(corelocation)


def validateios(ios):
    """
    Validate IOS is int or not provided
    Args:
        ios: stored ios

    Returns:

    """
    try:
        if 1 <= int(ios) <= 5:
            return int(ios)
        else:
            return None
    except ValueError:
        return None


def validateSpecimenType(specimenType):
    """
    Validate Column is Valid specimen type
    Args:
        specimenType: column value

    Returns:

    """
    if specimenType == "ARFI":
        return specimenType
    return None


def validateamb(amb):
    """
    Validate column is valid amb location
    Args:
        amb: column value

    Returns:

    """
    if amb in ["apex", "mid-gland", "base"]:
        return amb
    elif amb == "NAVU":
        return np.nan
    return None


def validatepta(pta):
    """
    Validate column is valid pta location
    Args:
        pta: column value

    Returns:

    """
    if pta in ["peripheral zone", "transition zone", "AFMS"]:
        return pta
    elif pta == "NAVU":
        return np.nan
    return None


def validatemlm(mlm):
    """
    Validate column is valid mlm location
    Args:
        mlm: column value

    Returns:

    """
    if mlm in ["anterior horn", "mediolateral", "medial", "lateral"]:
        return mlm
    elif mlm == "NAVU":
        return np.nan
    return None


def validatelcr(lcr):
    """
    Validate column is valid lcr location
    Args:
        lcr: column value

    Returns:

    """
    if lcr in ["left", "right", "central"]:
        return lcr
    elif lcr == "NAVU":
        return np.nan
    return None


def noneValidation(value):
    """

    Args:
        value:

    Returns:

    """
    return value is not None


def validationSchema(df):
    """
    Check case dataframe meets schema where required entries are met
    Args:
        df: input case dataframe

    Returns:

    """
    # Validation Elements
    nullValidation = [CustomElementValidation(lambda n: noneValidation(n), "is Null")]

    # Define validation schema on dataframe
    schema = pandas_schema.Schema([
        Column('CaseID', nullValidation),
        Column('ReaderID', nullValidation),
        Column('SpecimenType', nullValidation),
        Column('amb', nullValidation),
        Column('lcr', nullValidation),
        Column('mlm', nullValidation),
        Column('pta', nullValidation),
        Column('amp', nullValidation),
        Column('LocationNotes', nullValidation),
        Column('ios', nullValidation),
        Column('FiducialNumber', nullValidation),
        Column('Asymmetry', nullValidation),
        Column('Contrast', nullValidation),
        Column('Texture', nullValidation),
        Column('Margin', nullValidation),
        Column('LateralLocation', nullValidation),
        Column('AxialLocation', nullValidation),
        Column('DepthLocation', nullValidation),
        Column('ReviewTime', nullValidation),
        Column('GleasonScore', nullValidation),
        Column('LocationDescription', nullValidation),
        Column('Study', nullValidation)
    ])
    # Store errored rows and corresponding reason
    errors = schema.validate(df)
    errorRows = [error.row for error in errors]
    errorCol = [error.column for error in errors]
    return errorRows, errors, errorCol


def cleanData(df, errorRows):
    """
    Drop errored rows from dataframe
    Args:
        df: existing case df with errors
        errorRows: indexes of all rows with errors

    Returns:

    """
    df.drop(index=errorRows, inplace=True)


def loadCase(filepath):
    """
    Load json of case
    Args:
        filepath: path to json

    Returns:

    """
    with open(filepath, "r") as infile:
        data = json.load(infile)
    return data


def saveData(df, filepath):
    """

    Args:
        df: cleaned case df
        filepath: filepath to save csv

    Returns:

    """
    # Check if file exists to determine if need header
    headerFlag = not os.path.exists(filepath)

    # Save to csv
    df.to_csv(filepath, mode="a", header=headerFlag, index=False)


def validateSubmit(data):
    """

    Args:
        data:

    Returns:

    """
    # Append json to df
    df = pd.DataFrame({})
    for corenumber in data["ARFICores"]:
        df = createdf(df, data["ARFICores"][corenumber], data["SubjectID"], data["ReaderID"], data["ReviewTime"])

    # Validate all fields
    errorRows, errors, errorCol = validationSchema(df)

    return errors


def submit(data, dir):
    """

    Args:
        data:
        dir:

    Returns:

    """
    # Open Currently Saved File
    filepath = os.path.abspath(dir + "\\ReaderStudy.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        # Drop all data previously saved with same subject ID to allow replacement and remove duplicates
        df.drop(df.loc[(df["CaseID"] == " " + data["SubjectID"]) & (df["ReaderID"] == data["ReaderID"])].index, inplace=True)
    else:
        df = pd.DataFrame({})

    # Append to df
    for corenumber in data["ARFICores"]:
        df = createdf(df, data["ARFICores"][corenumber], " " + data["SubjectID"], data["ReaderID"], data["ReviewTime"])
    print(df.to_string())

    # Write to CSV
    df.to_csv(filepath, index=False)


def loadcaseorder():
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


def loadreaders():
    filepath = os.getcwd() + "\\ReadersProgress.json"

    # Open and store file
    with open(filepath, 'r') as infile:
        readers = json.loads(infile.read())

    return readers


def main():
    # Load dataframe
    datafilepath = os.getcwd() + "\\ReaderStudy.csv"
    readerstudypd = pd.read_csv(datafilepath)

    # Load list of patients
    caseorder = loadcaseorder()

    # Load list of readers
    readers = loadreaders()
    print(caseorder)
    print(readers)
    # Loop through each patient folder
    for file in os.listdir(os.getcwd()):
        if os.path.isdir(os.getcwd() + "\\" + file):
            if file in caseorder:
                # Loop through each reader folder
                for reader in os.listdir(os.getcwd() + "\\" + file + "\\slicer"):
                    if os.path.isdir(os.getcwd() + "\\" + file + "\\slicer\\" + reader):
                        if reader in readers:
                            # Check if _readerstudy.json exists
                            filepathroot = os.getcwd() + "\\" + file + "\\slicer\\" + reader + "\\" + "%s_%sReaderStudy.json" % (file, reader)
                            if os.path.isfile(filepathroot) and reader != "test":
                                print("%s_%sReaderStudy.json" % (file, reader))
                                # Drop info from pd
                                readerstudypd.drop(readerstudypd.loc[(readerstudypd["CaseID"] == " " + file) & (readerstudypd["ReaderID"] == reader)].index, inplace=True)

                                # Read json
                                data = loadCase(filepathroot)

                                # Append to df
                                for corenumber in data["ARFICores"]:
                                    # If json does not have
                                    '''if "IOSCategories" not in data["ARFICores"][corenumber]:
                                        data["ARFICores"][corenumber]["IOSCategories"] = {"Asymmetry": data["ARFICores"][corenumber]["IndexOfSuspicion"], 
                                                                                          "Contrast": data["ARFICores"][corenumber]["IndexOfSuspicion"], 
                                                                                          "Texture": data["ARFICores"][corenumber]["IndexOfSuspicion"], 
                                                                                          "Margin": data["ARFICores"][corenumber]["IndexOfSuspicion"]}'''
                                    readerstudypd = createdf(readerstudypd, data["ARFICores"][corenumber], " " + data["SubjectID"], data["ReaderID"], data["ReviewTime"])

                                # Validate all fields
                                errorRows, errors, errorCol = validationSchema(readerstudypd)

                                # Clean df
                                cleanData(readerstudypd, errorRows)

                                # Save error rows
                                #errorfilepath = os.getcwd() + "\\"
                                #errordf = pd.DataFrame(
                                #    {"SubjectID": data["SubjectID"], 'Row': errorRows, 'Col': errorCol})
                                #saveData(errordf, filepath)
    print(readerstudypd.to_string())
    # Write to CSV
    #saveData(readerstudypd, datafilepath)
    # Check if file exists to determine if need header
    headerFlag = os.path.exists(datafilepath)

    # Save to csv
    readerstudypd.to_csv(datafilepath, mode="w", header=headerFlag, index=False)


if __name__ == "__main__":
    main()
