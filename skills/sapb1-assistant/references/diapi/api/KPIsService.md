<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# KPIsService (Object)

The KPIsService service enables you to add, look up, update, and remove dashboard parameters. Source table: OKPI.

**Remarks:** To open the Dashboard Parameters - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> General --> Dashboard Parameters.

## Methods (8)
- `Public Function Add(ByVal pIKPI As KPI) As KPIParams` Adds a dashboard parameter.
  - param `pIKPI`: The data for the new dashboard parameter.
- `Public Sub Delete(ByVal pIKPIParams As KPIParams)` Deletes an existing dashboard parameter.
  - param `pIKPIParams`: The key of the dashboard parameter to be deleted.
- `Public Function Get(ByVal pIKPIParams As KPIParams) As KPI` Retrieves a dashboard parameter. The dashboard parameter is specified by its key, which is contained in the KPIParams object passed to the method.
  - param `pIKPIParams`: The key of the dashboard parameter to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As KPIsServiceDataInterfaces) As Object` Creates an empty data structure for use with the KPIsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/KPIsServiceDataInterfaces.md`
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
- `Public Function GetList() As KPIsParams` Returns the KPIsParams data collection that identifies all dashboard parameters.
- `Public Sub Update(ByVal pIKPI As KPI)` Updates an existing dashboard parameter.
  - param `pIKPI`: The data for the dashboard parameter to be updated. The KPI object must contain the key of the object to be updated.
