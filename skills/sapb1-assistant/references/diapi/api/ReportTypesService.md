<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ReportTypesService (Object)

The ReportTypesService service enables you to add, look up, and delete the report types in SAP Business One. Source table: RTYP.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.ReportTypesService rptTypeService = (SAPbobsCOM.ReportTypesService)oCompany.GetCompanyService().GetBusinessService(SAPbobsCOM.ServiceTypes.ReportTypesService);
  SAPbobsCOM.ReportType newType = (SAPbobsCOM.ReportType)rptTypeService.GetDataInterface(SAPbobsCOM.ReportTypesServiceDataInterfaces.rtsReportType);
  newType.TypeName = "Addon Demo Type 3";
  newType.AddonName = "SimpleForm";
  newType.AddonFormType = "MySimpleForm";
  newType.MenuID = "MySubMenu01";
  SAPbobsCOM.ReportTypeParams newTypeParam = rptTypeService.AddReportType(newType);
  ```

## Methods (8)
- `Public Function AddReportType(ByVal pIReportType As ReportType) As ReportTypeParams` Adds a new report type.
  - param `pIReportType`: The data for the new report type.
- `Public Sub DeleteReportType(ByVal pIReportType As ReportType)` Deletes an existing report type.
  - param `pIReportType`: The key of the report type to be deleted.
  - remarks: Before the deletion of the report type, you should delete all layouts related to the ReportType object. The deletion of a layout cannot be completed when the layout is the default layout of a ReportType object. Use the UpdateReportType method to reset the DefaultReportLayout property to null.
- `Public Function GetDataInterface(ByVal enumMSDI As ReportTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ReportTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ReportTypesServiceDataInterfaces.md`
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
- `Public Function GetReportType(ByVal pIReportTypeParams As ReportTypeParams) As ReportType` Retrieves a report type. The report type is specified by its key, which is contained in the ReportTypeParams object passed to the method.
  - param `pIReportTypeParams`: The key of the report type to retrieve.
- `Public Function GetReportTypeList() As ReportTypesParams` Returns the ReportTypesParams data collection that identify all report types.
- `Public Sub UpdateReportType(ByVal pIReportType As ReportType)` Updates an existing report type. The data for the report type, including the key of the report type to be updated, is contained in the ReportType object passed to the method. To update a report type, you must first retrieve it using the GetReportType method.
  - param `pIReportType`: The data for the report type to be updated. The ReportType object must contain the key of the object to be updated.
