<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FinancialYearsService (Object)

The FinancialYearsService service enables you to add, look up and remove financial roles for TDS (withholding tax) reports. To see the list of employee roles and create a new one, select Administration --> Setup --> Financials --> TDS --> Financial Year Master. Source table: OFYM.

**Remarks:** For India only.

## Methods (8)
- `Public Function AddFinancialYear(ByVal pIFinancialYear As FinancialYear) As FinancialYearParams` Adds a financial year.
  - param `pIFinancialYear`: The data for the new financial year
  - returns: Contains the key (AbsId) of the new financial year.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.FinancialYear oFY;
        oFY = (SAPbobsCOM.FinancialYear)oFYSrv.GetDataInterface(FinancialYearsServiceDataInterfaces.fysFinancialYear);
        oFY.Code = "200703";
        oFY.Description = "FY 07-08";
        DateTime otime = DateTime.Parse("01/03/2007");
        oFY.StartDate = otime;
        oFY.AssessYear = "200703";
        oFYSrv.AddFinancialYear(oFY);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteFinancialYear(ByVal pIFinancialYearParams As FinancialYearParams)` Deletes an existing financial year. The financial year is specified by its key (AbsId), which is contained in the FinancialYearParams object passed to the method.
  - param `pIFinancialYearParams`: The key of the financial year to be deleted
  - remarks: You cannot delete a financial year if it is associated with a record in the OACM (accumulation) or OACK (acknowledge number) tables.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.FinancialYearParams oDeleteLine;
        oDeleteLine = (SAPbobsCOM.FinancialYearParams)oFYSrv.GetDataInterface(FinancialYearsServiceDataInterfaces.fysFinancialYearParams);
        oDeleteLine.AbsEntry = 4;
        oFYSrv.DeleteFinancialYear(oDeleteLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As FinancialYearsServiceDataInterfaces) As Object` Creates an empty data structure for use with the FinancialYearsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/FinancialYearsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetFinancialYear(ByVal pIFinancialYearParams As FinancialYearParams) As FinancialYear` Retrieves a specific financial year. The financial year is specified by its key (AbsId), which is contained in the FinancialYearParams object passed to the method.
  - param `pIFinancialYearParams`: The key of the financial year to retrieve
  - returns: The financial year with the specified key
- `Public Function GetFinancialYearList() As FinancialYearsParams` Retrieves the keys and names of all the financial years.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.FinancialYearsParams oGetList = oFYSrv.GetFinancialYearList();
        String result;
        foreach(SAPbobsCOM.FinancialYearParams oGetItem in oGetList)
        {
            result = oGetItem.AbsEntry + " " + oGetItem.Code + " " + oGetItem.Description;
            Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub UpdateFinancialYear(ByVal pIFinancialYear As FinancialYear)` Updates an existing financial year. The data for the financial year, including the key of the financial year to be updated, is contained in the FinancialYear passed to the method. To update a financial year, you must first retrieve it using the GetFinancialYear method.
  - param `pIFinancialYear`: The data for the financial year to be updated. The FinancialYear object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.FinancialYear oUpdateLine;
        SAPbobsCOM.FinancialYearParams oGetLine;

        oGetLine = (SAPbobsCOM.FinancialYearParams)oFYSrv.GetDataInterface(FinancialYearsServiceDataInterfaces.fysFinancialYearParams);
        oGetLine.AbsEntry = 4;
        oUpdateLine = oFYSrv.GetFinancialYear(oGetLine);
         DateTime otime = DateTime.Parse("01/05/2008");
         oUpdateLine.StartDate = otime;
        oUpdateLine.Description = "updated";
        oFYSrv.UpdateFinancialYear(oUpdateLine);

    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
