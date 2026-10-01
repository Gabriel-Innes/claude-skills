<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FormPreferencesService (Object)

The FormPreferencesService manages the display preferences of a specified form for a specified user. Form preferences include settings such as, column width, visual order of columns, and more.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: - Select a form. - From the main menu, select Tools --> Form Settings. Mandatory properties: - FormID and User (ColumnsPreferencesParams) - Column, ItemNumber and Width (ColumnPreferences).

## Methods (5)
- `Public Function GetColumnsPreferences(ByVal pIColumnsPreferencesParams As ColumnsPreferencesParams) As ColumnsPreferences` Retrieves the column preferences of a specified form for a specified user.
  - param `pIColumnsPreferencesParams`: Returns the data structure that specifies the identification key combination (user and form) of the Form Preferences.
- `Public Function GetDataInterface(ByVal enumMSDI As FormPreferencesServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/FormPreferencesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: XML string.
  - example note: Shows how to get a Columns Preferences from an XML string
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oFormPreferencesService As FormPreferencesService

    Dim oColsPreferences As ColumnsPreferences

    Dim oColPreferencesParams As ColumnsPreferencesParams

    Dim oColsPreferencesXmlStr As ColumnsPreferences

    Dim sColsPreferencesStr As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get Form Preferences Service

    oFormPreferencesService = oCmpSrv.GetBusinessService(ServiceTypes.FormPreferencesService)

    'get Columns Preferences Params

    oColPreferencesParams = oFormPreferencesService.GetDataInterface(FormPreferencesServiceDataInterfaces.fpsdiColumnsPreferencesParams)

    'set the form id (e.g. A/R invoice=133)

    oColPreferencesParams.FormID = "133"

    'set the user id (e.g manager= 1)

    oColPreferencesParams.User = 1

    'get the Columns Preferences according to the formId & user id

    oColsPreferences = oFormPreferencesService.GetColumnsPreferences(oColPreferencesParams)

    'save Columns Preferences to string

    sColsPreferencesStr = oColsPreferences.ToXMLString()

    'create Columns Preferences object from string

    oColsPreferencesXmlStr = oFormPreferencesService.GetDataInterfaceFromXMLString(sColsPreferencesStr)
    ```
- `Public Sub UpdateColumnsPreferences(ByVal pIColumnsPreferencesParams As ColumnsPreferencesParams, ByVal pIColumnsPreferences As ColumnsPreferences)` Updates the column preferences of a specified form for a specified user with the data specified in ColumnsPreferences data structure.
  - param `pIColumnsPreferencesParams`: Returns the data structure that specifies the identification key combination (user and form) of the Form Preferences.
  - param `pIColumnsPreferences`: Returns the data structure that specifies the data for update the Form Preferences.
  - example note: The following is a VB.NET sample that updates the width of all the visible items in the invoice form settings.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oFormPreferencesService As FormPreferencesService

    Dim oColsPreferences As ColumnsPreferences

    Dim oColPreferencesParams As ColumnsPreferencesParams

    Dim i As Integer

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get Form Preferences Service

    oFormPreferencesService = oCmpSrv.GetBusinessService(ServiceTypes.FormPreferencesService)

    'get Columns Preferences Params

    oColPreferencesParams = oFormPreferencesService.GetDataInterface(FormPreferencesServiceDataInterfaces.fpsdiColumnsPreferencesParams)

    'set the form id (e.g. A/R invoice=133)

    oColPreferencesParams.FormID = "133"

    'set the user id (e.g manager= 1)

    oColPreferencesParams.User = 1

    'get the Columns Preferences according to the formId & user id

    oColsPreferences =  oFormPreferencesService.GetColumnsPreferences(oColPreferencesParams)

    'change the width of all the visible items

    For i = 0 To oColsPreferences.Count - 1

        'check if the item is visible

        If oColsPreferences.Item(i).VisibleInForm = BoYesNoEnum.tYES Then

            'set the width of the item

            oColsPreferences.Item(i).Width = 100

        End If

    Next

    'update all changes

    oFormPreferencesService.UpdateColumnsPreferences(oColPreferencesParams, oColsPreferences)
    ```
