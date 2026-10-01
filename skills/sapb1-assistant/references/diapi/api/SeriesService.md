<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SeriesService (Object)

SeriesService manages the Series object, a component of the document numbering system. Source table: NNM1 (Documents Numbering - Series).

**Remarks:** See the documentation for the SeriesService methods for more code samples. In general, to use a DI service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or - You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method.

## Methods (22)
- `Public Function AddElectronicSeries(ByVal pIElectronicSeries As ElectronicSeries) As ElectronicSeriesParams` AddElectronicSeries
  - param `pIElectronicSeries`: 
- `Public Function AddSeries(ByVal pISeries As Series) As SeriesParams` Adds a new Series to the series Service and returns the SeriesParams identification key.
  - param `pISeries`: Specifies the Series you want to add.
- `Public Sub AttachSeriesToDocument(ByVal pIDocumentSeriesParams As DocumentSeriesParams)` Attach a Series to a document, both defined by a DocumentSeriesParams.
  - param `pIDocumentSeriesParams`: The DocumentSeriesParams that identifies the Series and the document.
  - example note: The following is a VB.NET sample related to the the Belgium localization, which is different than other localizations. It shows how to add a series, attach it to a document and set it as the default series.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    Dim oDocSeriesParam As DocumentSeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'create a new series data structure

    oSeries = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeries)

    'set series name

    oSeries.Name = "Series1"

    'set the period indicator

    oSeries.PeriodIndicator = "Default"

    'set the group code

    '(enum BoSeriesGroupEnum has all Group Enum)

    oSeries.GroupCode = 1

    'set the first number

    oSeries.InitialNumber = 300

    'set last number

    oSeries.LastNumber = 350

    'add new series

    oSeriesParams = oSeriesService.AddSeries(oSeries)

    'create a new DocumentSeriesParams data structure

    oDocSeriesParam = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentSeriesParams)

    'set document type(e.g. Deliveries=15)

    oDocSeriesParam.Document = "15"

    'set the series code

    oDocSeriesParam.Series = oSeriesParams.Series

    'attach Series to document

    Call oSeriesService.AttachSeriesToDocument(oDocSeriesParam)

    'set the series to be the default series for the specify document

    Call oSeriesService.SetDefaultSeriesForCurrentUser(oDocSeriesParam)
    ```
- `Public Sub ChangeDocumentMenuName(ByVal pIDocumentChangeMenuName As DocumentChangeMenuName)` Modifies the menu name for a specific document type/document subtype.
  - param `pIDocumentChangeMenuName`: A document type/document subtype and its new menu name.
  - C# example (from SAP's help):
    ```csharp
    Company oCompany = new SAPbobsCOM.Company();

        // ... specify some parameters for the company object

    int iRetCode = oCompany.Connect();
    CompanyService companyService = oCompany.GetCompanyService();

    SeriesService seriesService = (SeriesService)companyService.GetBusinessService(ServiceTypes.SeriesService);

    DocumentTypeParams documentTypeParams = (DocumentTypeParams)seriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentTypeParams);
    documentTypeParams.Document = "10000105";
    documentTypeParams.DocumentSubType = "--";

    DocumentChangeMenuName documentChangeMenuName = seriesService.GetDocumentChangedMenuName(documentTypeParams);
    documentChangeMenuName.ChangedMenuName = "My New Name";

    seriesService.ChangeDocumentMenuName(documentChangeMenuName);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SeriesServiceDataInterfaces) As Object` Creates an empty data structure.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/SeriesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - example note: Shows how to get a Series from an XML file.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    Dim oSeriesFromFile As Series

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 5

    'get the series

    oSeries = oSeriesService.GetSeries(oSeriesParams)

    'save series to file

    oSeries.ToXMLFile("c:\MySeries.xml")

    'create a new series data structure and fill it with the data from

    'the xml file

    oSeriesFromFile = oSeriesService.GetDataInterfaceFromXMLFile("c:\MySeries.xml")
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Get the data interface from an XML String.
  - param `bstrXMLString`: Specifies the XML string.
  - example note: Shows how to get a Series from an XML string.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    Dim oSeriesFromStr As Series

    Dim sSeriesXmlString As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 5

    'get the series

    oSeries = oSeriesService.GetSeries(oSeriesParams)

    'save series to string

    sSeriesXmlString = oSeries.ToXMLString()

    'create a new series data structure and fill it with the data from

    'the xml file

    oSeriesFromStr = oSeriesService.GetDataInterfaceFromXMLString(sSeriesXmlString)
    ```
- `Public Function GetDefaultElectronicSeries(ByVal pISeriesParams As SeriesParams) As ElectronicSeriesParams` GetDefaultElectronicSeries
  - param `pISeriesParams`: 
- `Public Function GetDefaultSeries(ByVal pIDocumentTypeParams As DocumentTypeParams) As Series` Return the default Series object for a document identified by its DocumentTypeParams.
  - param `pIDocumentTypeParams`: Specified by the DocumentTypeParams identification key.
  - example note: The following is a VB.NET sample that retrieves the default series of a specified document type.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oDocumentTypeParams As DocumentTypeParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get new series

    oSeries = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeries)

    'get DocumentTypeParams for filling the document type

    oDocumentTypeParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentTypeParams)

    'set the document type (e.g. A/R Invoice=13)

    oDocumentTypeParams.Document = 13

    'get the default series of the SaleOrder documentset the document type

    oSeries = oSeriesService.GetDefaultSeries(oDocumentTypeParams)

    'print the default series name

    Debug.WriteLine(oSeries.Name)

    'print the first number of the series

    Debug.WriteLine(oSeries.InitialNumber)
    ```
- `Public Function GetDocumentChangedMenuName(ByVal pIDocumentTypeParams As DocumentTypeParams) As DocumentChangeMenuName` Retrieves the DocumentChangeMenuName object for modifying the menu name for a specific document type/document subtype.
  - param `pIDocumentTypeParams`: The document type/document subtype for which you want to change the menu name
- `Public Function GetDocumentSeries(ByVal pIDocumentTypeParams As DocumentTypeParams) As SeriesCollection` Returns the SeriesCollection of all the Series that match a document identified by its DocumentTypeParams.
  - param `pIDocumentTypeParams`: Specified by the DocumentTypeParams identification key.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeriesCollection As SeriesCollection

    Dim oSeries As Series

    Dim oDocumentTypeParams As DocumentTypeParams

    Dim i As Integer

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series collection

    oSeriesCollection =     oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesCollection)

    'get Document Type Params

    oDocumentTypeParams =     oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentTypeParams)

    'set the document type

    '(e.g. SaleInvoice=13 , BoObjectTypes has all document types)

    oDocumentTypeParams.Document = 13

    'get series collection

    oSeriesCollection = oSeriesService.GetDocumentSeries(oDocumentTypeParams)

    For i = 0 To oSeriesCollection.Count - 1

        'print the series name

        Debug.WriteLine(oSeries.Name)

        'print the series first number

        Debug.WriteLine(oSeries.InitialNumber)

    Next
    ```
- `Public Function GetElectronicSeries(ByVal pElectronicSeriesParams As ElectronicSeriesParams) As ElectronicSeries` GetElectronicSeries
  - param `pElectronicSeriesParams`: 
- `Public Function GetSeries(ByVal pSeriesParams As SeriesParams) As Series` Returns a Series object identified by its SeriesParams.
  - param `pSeriesParams`: The SeriesParams identification key of the Series you want to get.
  - example note: The following is a VB.NET sample that retrieves the series by its parameters.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 84

    'get the series

    oSeries = oSeriesService.GetSeries(oSeriesParams)

    'print the series name

    Debug.WriteLine(oSeries.Name)
    ```
- `Public Sub RemoveElectronicSeries(ByVal pIElectronicSeriesParam As ElectronicSeriesParams)` RemoveElectronicSeries
  - param `pIElectronicSeriesParam`: 
- `Public Sub RemoveSeries(ByVal pISeriesParam As SeriesParams)` Removes a Series identified by its SeriesParams.
  - param `pISeriesParam`: The SeriesParams identification key of the Series that you want to remove.
  - example note: Remove a Series
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeriesParams As SeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 29

    'remove series

    oSeriesService.RemoveSeries(oSeriesParams)
    ```
- `Public Sub SetDefaultElectronicSeries(ByVal pIDefaultElectronicSeriesParams As DefaultElectronicSeriesParams)` SetDefaultElectronicSeries
  - param `pIDefaultElectronicSeriesParams`: 
- `Public Sub SetDefaultSeriesForAllUsers(ByVal pIDocumentSeriesParams As DocumentSeriesParams)` Set a Series, identified by its DocumentTypeParams, as a default Series for all users.
  - param `pIDocumentSeriesParams`: The DocumentSeriesParams that defines the document type and series number.
  - example note: Description: shows how to set a default Series for all the users.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oDocumentSeriesParams As DocumentSeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oDocumentSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentSeriesParams)

    ''set doument type(e.g. Deliveries=15)

    oDocumentSeriesParams.Document = 15

    'set the number of an existing series

    oDocumentSeriesParams.Series = 28

    'set default series

    oSeriesService.SetDefaultSeriesForAllUsers(oDocumentSeriesParams)
    ```
- `Public Sub SetDefaultSeriesForCurrentUser(ByVal pIDocumentSeriesParams As DocumentSeriesParams)` Set a Series, identified by its DocumentTypeParams, as a default Series for current user.
  - param `pIDocumentSeriesParams`: The DocumentSeriesParams that defines the document type and series number.
  - example note: Shows how to set a default Series for a current user.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oDocumentSeriesParams As DocumentSeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oDocumentSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentSeriesParams)

    'set doument type(e.g. Deliveries=15)

    oDocumentSeriesParams.Document = 15

    'set the number of an existing series

    oDocumentSeriesParams.Series = 28

    'set default series

    oSeriesService.SetDefaultSeriesForCurrentUser(oDocumentSeriesParams)
    ```
- `Public Sub SetDefaultSeriesForUser(ByVal pIDocumentSeriesUserParams As DocumentSeriesUserParams)` Set a default Series for a specific user where the user Id, Series number and the document type are defined by DocumentSeriesUserParams.
  - param `pIDocumentSeriesUserParams`: Specifies the DocumentSeriesUserParams identification key.
- `Public Sub UnattachSeriesFromDocument(ByVal pIDocumentSeriesParams As DocumentSeriesParams)` Disconnect a Series from a document where the Series and the document are identified by DocumentSeriesParams.
  - param `pIDocumentSeriesParams`: Specifies the DocumentSeriesParams identification key that defines both series and document that you want to separate.
  - example note: Shows how to unattach a Series from a document (related only to the the Belgium localization)
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oDocumentSeriesParams As DocumentSeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oDocumentSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentSeriesParams)

    'set the number of an existing series

    oDocumentSeriesParams.Series = 7

    'set doument type(e.g. Deliveries=15)

    oDocumentSeriesParams.Document = 15

    'unattach the series from the document

    oSeriesService.UnattachSeriesFromDocument(oDocumentSeriesParams)
    ```
- `Public Sub UpdateElectronicSeries(ByVal pIElectronicSeries As ElectronicSeries)` UpdateElectronicSeries
  - param `pIElectronicSeries`: 
- `Public Sub UpdateSeries(ByVal pISeries As Series)` Replace a Series by another Series.
  - param `pISeries`: Specifies the Series that will replace the current series.
  - example note: Description: shows how to update a Series.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 28

    'get the series

    oSeries = oSeriesService.GetSeries(oSeriesParams)

    'set the series name

    oSeries.Name = "MySeries"

    'update series

    oSeriesService.UpdateSeries(oSeries)
    ```
