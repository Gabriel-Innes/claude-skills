<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ReportFilterService (Object)

The Report Filter Service is a business object that manages the information displaied by tax report. This object enables user to: - Add new Tax report filter to the service. - Delete a Tax report filter from the service. - Get a list of all Tax report filter Ids that exists in the service. - Update Tax report filter. - Get Data interfaces. Source table: OVTR.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: - Select -- .

## Methods (8)
- `Public Function AddTaxReportFilter(ByVal pITaxReportFilter As TaxReportFilter) As TaxReportFilterParams` Adds new TaxReportFilter to the ReportFilterService Object.
  - param `pITaxReportFilter`: The TaxReportFilter Object you want to add.
  - example note: Add a new Filter that is based on an existing Filter
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oTaxReportFilterParams As TaxReportFilterParams

    Dim oTaxReportFilter As TaxReportFilter

    'get a new Filter Params structure

    oTaxReportFilterParams = oTaxReportFilterService.GetDataInterface(ReportFilterServiceDataInterfaces.rfsdiTaxReportFilterParams)

    'set an existing Filter code

    oTaxReportFilterParams.Code = 4

    'get Report Filter

    oTaxReportFilter = oTaxReportFilterService.GetTaxReportFilter(oTaxReportFilterParams)

    'Change properties: set a new name

    oTaxReportFilter.Name = "My Filter"

    'add a new Filter

    Call oTaxReportFilterService.AddTaxReportFilter(oTaxReportFilter)
    ```
- `Public Sub DeleteTaxReportFilter(ByVal pITaxReportFilterParams As TaxReportFilterParams)` Delete the TaxReportFilter by it key.
  - param `pITaxReportFilterParams`: The TaxReportFilterParams identification key.
  - example note: Delete an existing Filter
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oTaxReportFilterParams As TaxReportFilterParams

    Dim oTaxReportFilter As TaxReportFilter

    'get a new Filter Params structure

    oTaxReportFilterParams = oTaxReportFilterService.GetDataInterface(ReportFilterServiceDataInterfaces.rfsdiTaxReportFilterParams)

    'set an existing Filter code

    oTaxReportFilterParams.Code = 5

    'delete Filter

    Call oTaxReportFilterService.DeleteTaxReportFilter(oTaxReportFilterParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ReportFilterServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ReportFilterServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an empty data structure defined by data from an XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an empty data structure defined by data from an XML string.
  - param `bstrXMLString`: Specifies the the XML string.
- `Public Function GetTaxReportFilter(ByVal pITaxReportFilterParams As TaxReportFilterParams) As TaxReportFilter` Get a TaxReportFilter by its TaxReportFilterParams identification key.
  - param `pITaxReportFilterParams`: TaxReportFilterParams identification key.
- `Public Function GetTaxReportFilterList(ByVal pITaxReportFilterParams As TaxReportFilterParams) As TaxReportFiltersParams` Returns a TaxReportFiltersParams object, a data collection of all the instances of TaxReportFilterParams Identification keys that match a given TaxReportFilterParams identification key.
  - param `pITaxReportFilterParams`: TaxReportFilterParams identification key.
  - example note: Get a list of Report Filter Params.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oTaxReportFiltersParams As TaxReportFiltersParams

    Dim oTaxReportFilter As TaxReportFilter

    Dim oTaxReportFilterParams As TaxReportFilterParams

    'get a new Filter Param structure

    oTaxReportFilterParams = oTaxReportFilterService.GetDataInterface(ReportFilterServiceDataInterfaces.rfsdiTaxReportFilterParams)

    'set the type of the requested filters

    oTaxReportFilterParams.FilterType =TaxReportFilterType.trft_SalesReport

    'get list of Report Filter Params

    oTaxReportFiltersParams = oTaxReportFilterService.GetTaxReportFilterList(oTaxReportFilterParams)

    'get the first Filter Params

    oTaxReportFilterParams = oTaxReportFiltersParams.Item(0)
    ```
- `Public Sub UpdateTaxReportFilter(ByVal pITaxReportFilter As TaxReportFilter)` Replace this TaxReportFilter Object with the target TaxReportFilter.
  - param `pITaxReportFilter`: The target TaxReportFilter Object.
  - example note: Update Report Filter
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oTaxReportFilterParams As TaxReportFilterParams

    Dim oTaxReportFilter As TaxReportFilter

    'get a new Filter Params structure

    oTaxReportFilterParams = oTaxReportFilterService.GetDataInterface(ReportFilterServiceDataInterfaces.rfsdiTaxReportFilterParams)

    'set an existing Filter code

    oTaxReportFilterParams.Code = 5

    'get Report Filter

    oTaxReportFilter = oTaxReportFilterService.GetTaxReportFilter(oTaxReportFilterParams)

    'set a new name

    oTaxReportFilter.Name = "My Filter"

    'update Filter

    oTaxReportFilterService.UpdateTaxReportFilter(oTaxReportFilter)
    ```
