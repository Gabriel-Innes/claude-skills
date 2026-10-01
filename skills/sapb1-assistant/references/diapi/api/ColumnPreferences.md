<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ColumnPreferences (Object)

ColumnPreferences is a Data structure related to the FormPreferencesService. Source table: CPRF.

**Remarks:** To display the Form Preferences settings in the application: - Select a form. - From the main menu, select Tools --> Form Settings.

## Properties (11)
- `Public Property Column() As String` [R/W] Sets or returns the column identification key. Field name: ColumnId. Mandatory property for Table fields. The default value is -1 (Title field). Length: 10 characters.
- `Public Property EditableInExpanded() As BoYesNoEnum` [R/W] Determines whether or not the item in the form can be edited in expanded display mode. Field name: EditInEXP.
- `Public Property EditableInForm() As BoYesNoEnum` [R/W] Determines whether or not the item in the form can be edited in normal display mode (that is, not expanded mode). Property type Read-write property " --> Field name: EditInForm.
- `Public Property ExpandedIndex() As Long` [R/W] Sets or returns the expanded index of this column. Field name: ExpandIndx.
- `Public Property FormID() As String` [R/W] Sets or returns the form identification key. Field name: FormID. Mandatory property. Length: 20 characters.
  - remarks: The entered value must be a valid form ID (the system does not validate the entered value). To display the form ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property ItemNumber() As String` [R/W] Sets or returns the ID of the field or the table in a form (primary key with FormID). Field name: ItemID. Mandatory property. Length: 10 characters.
  - remarks: The entered value must be a valid item ID (the system does not validate the entered value). In case the ItemID specifies a table, set also the Column, otherwise the system sets the value -1. To display the item ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property TabsLayout() As Long` [R/W] Sets or returns the display order of the item in the form. For example, set 1 to display the form item in the first column in the table (starting from left). Property type Read-write property " --> Field name: VisualIndx.
- `Public Property User() As Long` [R/W] Sets or returns the signature of the user that sets this column. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property VisibleInExpanded() As BoYesNoEnum` [R/W] Determines whether or not the item in the form is visible in expanded display mode. Field name: VisInExpnd.
- `Public Property VisibleInForm() As BoYesNoEnum` [R/W] Determines whether or not the item is visible in the form in normal display mode (that is, not expanded mode). Field name: VisInForm.
- `Public Property Width() As Long` [R/W] Sets or returns the number of characters to determine the column width. Mandatory property. Field name: Width.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
