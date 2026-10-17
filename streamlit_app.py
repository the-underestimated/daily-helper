import streamlit as st
import pandas as pd
import functions as fn
import numpy as np
import datetime
import openpyxl
import traceback

st.title("Daily Helper by Gz.")

with st.sidebar:
    st.title("Procedures and Notes")
    with st.popover("Patch Notes v1.0.0"):
        st.write("Initial release of East Route-r by Gz.")
    st.subheader("App usage procedures:")
    st.write("1. Download the GSS Daily Report WG from the GSS SharePoint site by clicking the 'File' tab, then 'Create a Copy', then 'Download a Copy'.")
    st.write("2. Upload the downloaded .xlsx file using the file uploader below.")
    st.write("3. Copy and paste the east route aircraft list to the input")
    st.write("4. Click the 'Process the Data!' button to process the data and generate the readiness report.")
    st.write("5. The generated report will be displayed below the button. You can copy and paste it into your chat application.")

dataDCRRaw = st.file_uploader("Choose File .xlsx from the DCR+PAXLIST file", type='xlsx')
dataPilotCategoryRaw = st.file_uploader("Choose File .xlsx from the Pilot Categorization file", type='xlsx')
dataReadinessRaw = st.file_uploader("Choose File .xlsx from GSS Daily Report WG", type='xlsx')
dataHMBTHRaw = st.file_uploader("Choose File .xlsx from HMBTH Aircraft File", type='xlsx')

if (dataDCRRaw and dataPilotCategoryRaw and dataReadinessRaw and dataHMBTHRaw) is not None:
    if st.button("Process the Data!", type="primary"): 
        print("Yay")
        
        """
        try:
            
            dataReadinessWG1 = fn.readReadinessData(dataRaw, 1)
            dataReadinessWG2 = fn.readReadinessData(dataRaw, 2)
            dataReadinessWG3 = fn.readReadinessData(dataRaw, 3)
            dataReadinessWG13 = fn.readReadinessData(dataRaw, 13)
            allWGGoodData = pd.concat([dataReadinessWG1, dataReadinessWG2, dataReadinessWG3, dataReadinessWG13], ignore_index=True)

            dataACStatus = fn.ACStatus(allWGGoodData)
            dataEastRouteMessage = fn.readEastRouteMessage(textACEastRoute)
            dataMasterEastRoute = fn.createDataMaster(dataEastRouteMessage, dataACStatus)
            finalReport = fn.createWAMessage(dataMasterEastRoute, textACEastRoute, eastRouteTime)

            st.divider()
            st.header("Generated Report")
            st.code(finalReport, language='markdown')

        except Exception as e:
            st.error(f"Error: {e}")
            st.code(traceback.format_exc())
        """