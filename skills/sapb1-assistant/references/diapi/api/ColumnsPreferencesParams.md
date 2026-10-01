<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ColumnsPreferencesParams (Object)

The ColumnsPreferencesParams specifies the identification key combination (user and FormId) for which the FormPreferencesService is related. Source table: CPRF.

**Remarks:** To display the Form Preferences settings in the application: - Select a form. - From the main menu, select Tools --> Form Settings.

## Properties (2)
- `Public Property FormID() As String` [R/W] Sets or returns the form identification key. Field name: FormID. Mandatory property. Length: 20 characters.
  - remarks: The entered value must be a valid form ID (the system does not validate the entered value). To display the form ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property User() As Long` [R/W] Sets or returns the identification key of the user to whom this form preferences applies. Mandatory property. Field name: UserSign.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data. Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data. Creates an XML string that represents the object data.
