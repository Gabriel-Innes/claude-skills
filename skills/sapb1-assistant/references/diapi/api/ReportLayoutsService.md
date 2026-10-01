<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ReportLayoutsService (Object)

The ReportLayoutsService service enables you to do the following: - Copy a PLD report layout from one company to another. - Add a Crystal Reports layout or standalone report. Source table: RDOC (report layouts) and RDFL (associates default report with user, business partners)

**Remarks:** To work with report layouts in SAP Business One: - Open a marketing document form (for example, Sales A/R -- Sales Quotation). - Select Tools --> Print Layout Designer (or select the pencil icon on the toolbar). The Layout Designer - Selection Criteria form opens. - Click Edit. The Report and Layout Manager opens. To work with the Print Layout Designer: - Open the Report and Layout Manager, as described above. - Select a PLD report layout. - Click Edit.

## Methods (15)
- `Public Function AddReportLayout(ByVal pIReportLayout As ReportLayout) As ReportLayoutParams` Adds a new report/report layout.
  - param `pIReportLayout`: The data for the new report/report layout.
  - returns: Contains the key (DocCode) of the new report/report layout.
  - remarks: For Crystal Reports, use this method to add a report (as a standalone report or as a report layout) by setting the fields Name, TypeCode, Author and Category of the ReportLayout object. Set Category to Crystal Reports and set TypeCode to either RCRI (for standalone report) or a document type (for report layouts). For PLD report layouts, use this only to transfer report layouts from one company to another. When transferring a system layout, change the following properties before adding the layout to the destination company: - Author: Change from System to a different name. If left unchanged, an exception is thrown. - Editable: Change from NO to Yes to make the new layout editable. - Name: Give the report layout a new name. Do not change any other properties.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportLayout As ReportLayout

    Dim oReportLayoutParam As ReportLayoutParams

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportLayoutParam = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportLayoutParams)

    oReportLayoutParam.LayoutCode = "POR20002"

    'Get report layout

    oReportLayout = oReportLayoutService.GetReportLayout(oReportLayoutParam)

    'Add report layout

    oReportLayoutService.AddReportLayout(oReportLayout)
    ```
- `Public Function AddReportLayoutToMenu(ByVal ppIReportLayout As ReportLayout, ByVal MenuID As String) As ReportLayoutParams` 
  - param `ppIReportLayout`: 
  - param `MenuID`: 
- `Public Sub DeleteReportLayout(ByVal pIReportLayoutParams As ReportLayoutParams)` 
  - param `pIReportLayoutParams`: A pointer to a ReportLayoutParams object.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportLayoutParams As ReportLayoutParams

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportLayoutParams = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportLayoutParams)

    oReportLayoutParams.LayoutCode = "POR20002"

    'Delete report layout

    oReportLayoutService.DeleteReportLayout(oReportLayoutParams)
    ```
- `Public Sub DeleteReportLayoutAndMenu(ByVal ppIReportLayoutParams As ReportLayoutParams)` 
  - param `ppIReportLayoutParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ReportLayoutsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ReportLayoutsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ReportLayoutsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - example note: Shows how to get a Report Layout from an XML file.
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
  - example note: Shows how to get a Report Layout from an XML string.
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
- `Public Function GetDefaultReport(ByVal pIReportParams As ReportParams) As DefaultReportParams` Retrieves the default report layout for a specific document type.
  - param `pIReportParams`: Specifies a document type, as well as a user or business partner, for which to retrieve the default report layout.
  - remarks: This method is similar to the GetDefaultReportLayout method, except that this method returns the key to the report layout and not the ReportLayout object for the report layout.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportParam As ReportParams

    Dim oReportParaDefault As DefaultReportParams

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportParam = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportParams)

    oReportParam.ReportCode = "POR2"

    'Get default layout for specific document (Purchase Order)

    oReportParaDefault = oReportLayoutService.GetDefaultReport(oReportParam)

    'Print the layout code

    Debug.WriteLine(oReportParaDefault.LayoutCode)
    ```
- `Public Function GetDefaultReportLayout(ByVal pIReportParams As ReportParams) As ReportLayout` Retrieves the default report layout for a specific document type.
  - param `pIReportParams`: Specifies a document type, as well as a user or business partner, for which to retrieve the default report layout.
  - remarks: This method is similar to the GetDefaultReport method, except that this method returns the ReportLayout object for the report layout and not just the key.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportLayout As ReportLayout

    Dim oReportParam As ReportParams

    'Get report layout  service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService =     oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportParam = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportParams)

    oReportParam.ReportCode = "POR2"

    'Get the default layout for the specific document

    oReportLayout = oReportLayoutService.GetDefaultReportLayout(oReportParam)

    'Print the report layout name

    Debug.WriteLine(oReportLayout.Name)
    ```
- `Public Function GetReportLayout(ByVal pIReportLayoutParams As ReportLayoutParams) As ReportLayout` Retrieves a report layout.
  - param `pIReportLayoutParams`: The key of the report layout to retrieve.
  - returns: The report layout with the specified key.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oReportLayoutParam As ReportLayoutParams

    Dim oReportLayout As ReportLayout

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oReportLayoutParam = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiReportLayoutParams)

    oReportLayoutParam.LayoutCode = "POR20002"

    'Get the report layout

    oReportLayout = oReportLayoutService.GetReportLayout(oReportLayoutParam)

    'Print the report layout name

    Debug.WriteLine(oReportLayout.Name)
    ```
- `Public Function GetReportLayoutList(ByVal pIReportParams As ReportParams) As ReportLayoutsParams` Retrieves the keys and names of all the report layouts.
  - param `pIReportParams`: Specifies the report layouts to retrieve.
- `Public Sub Print(ByVal ppIReportLayoutPrintParams As ReportLayoutPrintParams)` 
  - param `ppIReportLayoutPrintParams`: 
- `Public Sub SetDefaultReport(ByVal ppIDefaultReportParams As DefaultReportParams)` Sets the specified report layout as default for a specific document type.
  - param `ppIDefaultReportParams`: Specifies a report to set as the default for a specific document type.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oReportLayoutService As ReportLayoutsService

    Dim oDefaultReportParams As DefaultReportParams

    'Get report layout service

    oCmpSrv = oCompany.GetCompanyService

    oReportLayoutService = oCmpSrv.GetBusinessService(ServiceTypes.ReportLayoutsService)

    'Set parameters

    oDefaultReportParams = oReportLayoutService.GetDataInterface(ReportLayoutsServiceDataInterfaces.rlsdiDefaultReportParams)

    oDefaultReportParams.LayoutCode = "POR20005"

    oDefaultReportParams.ReportCode = "POR2"

    oDefaultReportParams.UserID = 1

    'Set the report as default

    oReportLayoutService.SetDefaultReport(oDefaultReportParams)
    ```
- `Public Sub UpdateLanguageReport(ByVal ppIReportLayout As ReportLayout)` 
  - param `ppIReportLayout`: 
- `Public Sub UpdatePrinterSettings(ByVal pIReportLayout As ReportLayout)` 
  - param `pIReportLayout`:
