<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# NatureOfAssesseesService (Object)

The NatureOfAssesseesService service enables you to add, look up and remove nature of assessees in the nature of assessee master data table. Nature of assessees are used to specify a type of entity subject to TDS (withholding tax). Source table: ONOA

**Remarks:** For India only.

## Methods (8)
- `Public Function AddNatureOfAssessee(ByVal pINatureOfAssessee As NatureOfAssessee) As NatureOfAssesseeParams` Adds a nature of assessee.
  - param `pINatureOfAssessee`: The data for the new nature of assessee.
  - returns: Contains the key (AbsId) of the new nature of assessee.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.NatureOfAssessee oNOA = (SAPbobsCOM.NatureOfAssessee)oNASrv.GetDataInterface(NatureOfAssesseesServiceDataInterfaces.noasNatureOfAssessee);
        oNOA.Code = "COM";
        oNOA.Description = "Company";
        oNOA.AssesseeType = AssesseeTypeEnum.atCompany;
        oNASrv.AddNatureOfAssessee(oNOA);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteNatureOfAssessee(ByVal pINatureOfAssesseeParams As NatureOfAssesseeParams)` Deletes an existing nature of assessee. The nature of assessee is specified by its key (AbsId), which is contained in the NatureOfAssesseeParams object passed to the method.
  - param `pINatureOfAssesseeParams`: The key of the nature of assessee to be deleted.
  - remarks: You cannot delete a nature of assessee that is associated with a withholding tax code (WithholdingTaxCodes).
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.NatureOfAssesseeParams oNOAParams = (SAPbobsCOM.NatureOfAssesseeParams)oNASrv.GetDataInterface(NatureOfAssesseesServiceDataInterfaces.noasNatureOfAssesseeParams);
        oNOAParams.AbsEntry = 1;
        oNASrv.DeleteNatureOfAssessee(oNOAParams);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As NatureOfAssesseesServiceDataInterfaces) As Object` Creates an empty data structure for use with the NatureOfAssesseesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/NatureOfAssesseesServiceDataInterfaces.md`
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
- `Public Function GetNatureOfAssessee(ByVal pINatureOfAssesseeParams As NatureOfAssesseeParams) As NatureOfAssessee` Retrieves a nature of assessee. The nature of assessee is specified by its key (AbsId), which is contained in the NatureOfAssesseeParams object passed to the method.
  - param `pINatureOfAssesseeParams`: The key of the nature of assessee to retrieve.
  - returns: The nature of assessee with the specified key.
- `Public Function GetNatureOfAssesseeList() As NatureOfAssesseesParams` Retrieves the keys and codes of all nature of assessees.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.NatureOfAssesseesParams oNAList = oNASrv.GetNatureOfAssesseeList();
        String result = "";
        foreach(SAPbobsCOM.NatureOfAssesseeParams oNAPar in oNAList)
        {
            result = oNAPar.Code + " " + oNAPar.Description + "\n";
        }
        Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub UpdateNatureOfAssessee(ByVal pINatureOfAssessee As NatureOfAssessee)` Updates an existing nature of assessee. The data for the nature of assessee, including the key of the nature of assessee to be updated, is contained in the NatureOfAssessee passed to the method. To update a nature of assessee, you must first retrieve it using the GetNatureOfAssessee method.
  - param `pINatureOfAssessee`: The data for the nature of assessee to be updated. The NatureOfAssessee object must contain the key of the object to be updated.
  - remarks: If the nature of assessee is associated with a withholding tax code (WithholdingTaxCodes), you cannot update the Code and AssesseeType properties.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.NatureOfAssesseeParams oNOAParams = (SAPbobsCOM.NatureOfAssesseeParams)oNASrv.GetDataInterface(NatureOfAssesseesServiceDataInterfaces.noasNatureOfAssesseeParams);
        oNOAParams.AbsEntry = 1;

        SAPbobsCOM.NatureOfAssessee oNOA = oNASrv.GetNatureOfAssessee(oNOAParams);
        oNOA.Description = "Updated";
        oNASrv.UpdateNatureOfAssessee(oNOA);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
