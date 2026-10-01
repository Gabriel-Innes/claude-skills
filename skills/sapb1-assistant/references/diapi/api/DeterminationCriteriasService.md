<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DeterminationCriteriasService (Object)

The DeterminationCriteriasService service enables you to look up and update determination criteria. Source table: ODMC.

**Remarks:** To open the Determination Criteria window, from the SAP Business One Main Menu, choose Administration -> Setup -> Financials -> G/L Account Determination -> Determination Criteria. This window is available only if the Enable Advanced G/L Account Determination checkbox is selected (Administration -> System Initialization -> Company Details -> Basic Initialization tab).

**Example:**
- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
  ```vb
  Dim oDeterminationCriteriasService As DeterminationCriteriasService =
  oCompany.GetCompanyService().GetBusinessService(ServiceTypes. DeterminationCriteriasService)

  Dim oDeterminationCriteria As SAPbobsCOM.DeterminationCriteria =
  oDeterminationCriteriasServices.GetDataInterface
  (DeterminationCriteriasServiceDataInterfaces.dcDeterminationCriteria)

  Dim param As SAPbobsCOM. DeterminationCriteriaParams =
  oDeterminationCriteriasServices.GetDataInterface
  (DeterminationCriteriasServiceDataInterfaces.dcDeterminationCriteriaParams)
          param.DmcId = 1
          oDeterminationCriteria = oDeterminationCriteriasService.Get(param)
          oDeterminationCriteria.IsActive = SAPbobsCOM.BoYesNoEnum.tYES
          oDeterminationCriteria.Priority = 8
          oDeterminationCriteriasService.Update(oDeterminationCriteria)
  ```

## Methods (6)
- `Public Function Get(ByVal pIDeterminationCriteriaParams As DeterminationCriteriaParams) As DeterminationCriteria` Retrieves a determination criteria. The determination criteria is specified by its key, which is contained in the DeterminationCriteriaParams object passed to the method.
  - param `pIDeterminationCriteriaParams`: The key of the determination criteria to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As DeterminationCriteriasServiceDataInterfaces) As Object` Creates an empty data structure for use with the DeterminationCriteriasService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DeterminationCriteriasServiceDataInterfaces.md`
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
- `Public Function GetList() As DeterminationCriteriaParamsCollection` Returns the DeterminationCriteriaParamsCollection data collection that identifies all determination criteria.
- `Public Sub Update(ByVal pIDeterminationCriteria As DeterminationCriteria)` Updates an existing determination criteria.
  - param `pIDeterminationCriteria`: The data for the determination criteria to be updated.
