import pandas as pd
import numpy as np
import re
from datetime import date

def readPilotData(DCRFilePath, pilotCategoryData):
    
    
    intlFlightStation = ['PEN', 'SYX', 'FOC', 'CAN', 'NKG', 'WUH', 'CSX', 'SZX', 'KUL']
    codePattern = '|'.join(intlFlightStation)

    
    intlFlight = DCRPaxlistData[DCRPaxlistData['ROUTE'].str.contains(codePattern, regex=True, na=False)]
    intlFlight = intlFlight[intlFlight['RANK'].isin(['CPT', 'FO'])]
    intlFlight[['CREW ID', 'CREW NAME']] = intlFlight['CREW LIST'].str.split('/', n=1, expand=True)

    pilotDataCategorization = pilotData[['ID', 'Categorization']]
    pilotDataCategorization = pilotDataCategorization.rename({'ID': 'CREW ID'}, axis=1)
    pilotDataCategorization['CREW ID'] = pilotDataCategorization['CREW ID'].astype(str)
    intlFlight = intlFlight.merge(pilotDataCategorization[['CREW ID', 'Categorization']], on='CREW ID', how='left')

    daily1Table = intlFlight[['CREW ID', 'CREW NAME', 'RANK', 'Categorization', 'ROUTE']]

def readReadinessData(readinessFilePath, WG):
