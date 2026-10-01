<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserValidValues (Object)

UserValidValues is an object related to the FormattedSearches object. It enables to define valid values for the field specified by the FormattedSearches object. Source table: CUVV.

**Remarks:** This object is relevant for fields that their search Action is set to bofsaValidValues. To display the form in the application: - Open a document and click any field. - From the menu bar, select Tools --> Search Function --> Define. - In the Define Formatted Search form, select the Search in Existing Values option. - Click the [...] button. The Define Field Values form opens.

## Properties (3)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property FieldValue() As String` [R/W] Sets or returns the valid value of the field that is specified in the Index property of the FormattedSearches object. Field name: Value. Length: 254 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
