from enum import Enum


class Folder(Enum):
    SCANS = "Scanned Documents/"
    DOWNLOADS = "C:/Users/Gebker/Downloads/"


class Faecher(Enum):
    DB = "/007_Datenbanken/"
    ST = "/103_Stochastik/"
    DMA = "/008_DataMining/"
    RS = "/006_RechnerBetriebssysteme/0061_Rechnerstrukturen/"


def checkFileName(file):
    fileStart = file[0:2]

    fachOrdnerName = ""
    if fileStart in Faecher._member_names_:
        fachOrdnerName = Faecher._member_map_[fileStart].value

    return fachOrdnerName
