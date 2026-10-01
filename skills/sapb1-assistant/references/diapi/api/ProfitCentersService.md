<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProfitCentersService (Object)

The ProfitCentersService service enables you to add, look up and remove profit centers. To see the list of profit centers, select Financials --> Cost Accounting --> Cost Centers, and then choose Open Table. Source table: OPRC

**Remarks:** The terminology "Profit Center" and "Cost Center" are the same.

## Methods (8)
- `Public Function AddProfitCenter(ByVal pIProfitCenter As ProfitCenter) As ProfitCenterParams` Adds a profit center.
  - param `pIProfitCenter`: The data for the new profit center.
  - returns: Contains the key (PrcCode) of the new profit center.
  - remarks: When you add a profit center, a distribution rule is automatically created with the same name and one line. The rule distributes the cost or expense 100 percent to the profit center, and the rule cannot be changed.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oCmpSrv = oCompany.GetCompanyService()

    Dim oPCService As SAPbobsCOM.IProfitCentersService

    Dim oPC As SAPbobsCOM.IProfitCenter

    Dim oPCParams As SAPbobsCOM.IProfitCenterParams

    Dim oPCsParams As SAPbobsCOM.IProfitCentersParams

    oPCService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.ProfitCentersService)

    oPCParams = oPCService.GetDataInterface(SAPbobsCOM.DimensionsServiceDataInterfaces.dsDimensionParams)

    oPC = oPCService.GetDataInterface(SAPbobsCOM.ProfitCentersServiceDataInterfaces.pcsProfitCenter)

    oPC.CenterCode = "code"

    oPC.CenterName = "name"

    oPC.GroupCode = "GRP"

    oPC.InWhichDimension = 1

    oPCParams = oPCService.AddProfitCenter(oPC)

    oStr = oPCParams.CenterCode
    ```
- `Public Sub DeleteProfitCenter(ByVal pIProfitCenterParams As ProfitCenterParams)` Deletes an existing profit center. The profit center is specified by its key (PrcCode), which is contained in the ProfitCenterParams object passed to the method.
  - param `pIProfitCenterParams`: The key of the profit center to be deleted.
  - remarks: If the profit center is system defined or is linked to a distribution rule, the profit center cannot be deleted. A profit center is system defined if the Locked field in the OPRC table is set to Y.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oPCParams.CenterCode = "Code"

    oPCService.DeleteProfitCenter(oPCParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ProfitCentersServiceDataInterfaces) As Object` Creates an empty data structure for use with the ProfitCentersService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ProfitCentersServiceDataInterfaces.md`
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
- `Public Function GetProfitCenter(ByVal pIProfitCenterParams As ProfitCenterParams) As ProfitCenter` Retrieves a profit center. The profit center is specified by its key (PrcCode), which is contained in the ProfitCenterParams object passed to the method.
  - param `pIProfitCenterParams`: The key of the profit center to retrieve.
  - returns: The profit center with the specified key.
- `Public Function GetProfitCenterList() As ProfitCentersParams` Retrieves the keys and names of all the profit centers.
- `Public Sub UpdateProfitCenter(ByVal pIProfitCenter As ProfitCenter)` Updates an existing profit center. The data for the profit center, including the key of the profit center to be updated, is contained in the ProfitCenter object passed to the method. To update a profit center, you must first retrieve it using the GetProfitCenter method.
  - param `pIProfitCenter`: The data for the profit center to be updated. The ProfitCenter object must contain the key of the object to be updated.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oPCParams.CenterCode = "Code"

    oPC = oPCService.GetProfitCenter(oPCParams)

    oPC.InWhichDimension = 1

    oPCService.UpdateProfitCenter(oPC)
    ```
