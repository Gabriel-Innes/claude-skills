<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# IndiaHsnService (Object)

India HSN master data. Source table: OCHP.

**Remarks:** Inventory --> Item Master Data --> General tab --> HSN field (for India only)

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.IndiaHsnService hsnService = (SAPbobsCOM.IndiaHsnService)cmpy.GetCompanyService().GetBusinessService(SAPbobsCOM.ServiceTypes.IndiaHsnService);
  SAPbobsCOM.IndiaHsn hsn = (SAPbobsCOM.IndiaHsn)hsnService.GetDataInterface(IndiaHsnServiceDataInterfaces.iscIndiaHsn);

  hsn.Chapter = ""22"";
  hsn.Heading = ""02"";
  hsn.SubHeading = ""0102"";
  hsn.Description = ""Add "" + hsn.Chapter + hsn.Heading + hsn.SubHeading + "" from DI"";

  var hsnParams = hsnService.Add(hsn);
  ```

## Methods (8)
- `Public Function Add(ByVal pIIndiaHsn As IndiaHsn) As IndiaHsnParams` Add
  - param `pIIndiaHsn`: 
- `Public Sub Delete(ByVal pIIndiaHsnParams As IndiaHsnParams)` Delete
  - param `pIIndiaHsnParams`: 
- `Public Function Get(ByVal pIIndiaHsnParams As IndiaHsnParams) As IndiaHsn` Get
  - param `pIIndiaHsnParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IndiaHsnServiceDataInterfaces) As Object` Creates an empty data structure for use with the IndiaHsnService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/IndiaHsnServiceDataInterfaces.md`
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
- `Public Function GetList() As IndiaHsnParamsCollection` GetList
- `Public Sub Update(ByVal pIIndiaHsn As IndiaHsn)` Update
  - param `pIIndiaHsn`:
