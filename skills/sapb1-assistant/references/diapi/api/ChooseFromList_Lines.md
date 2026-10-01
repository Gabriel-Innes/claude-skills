<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ChooseFromList_Lines (Object)

ChooseFromList_Lines is a child object of ChooseFromList. Source table: CHFL.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the total rows in the database table.
- `Public Property DisplayedName() As String` [R/W] Sets or returns name displayed in the column header. Field name: DispName. Length: 30 characters.
- `Public Property FieldNo() As String` [R/W] Sets or returns column number in the specified database table. Field name: FldNum. Length: 10 characters.
- `Public Property GroupBy() As BoYesNoEnum` [R/W] Determines whether or not to group all the rows by the specified field. Field name: GroupBy.
  - remarks: You can set up to three groups for a specified object. Set to Y - to group all the rows for the specified field. The user can expand or collapse all the records. Set to N - to display all the records.
- `Public Property ShowType() As BoYesNoEnum` [R/W] Determines whether to display the valid value description or the valid value. For example, for BP Type, set Y to display Customer or set N to display C. Field name: DispDesc.
  - remarks: Applicable only for properties that contain valid values.
- `Public Property SortOrder() As SortOrderEnum` [R/W] Sets or returns the sort order - Ascending or Descending - of the columns in the Choose from List form. Field name: SortOrder.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Visible() As BoYesNoEnum` [R/W] Determines whether or not to display the column. Field name: Visible.
- `Public Property VisualIndex() As Long` [R/W] Sets or returns the display order number of the column. Field name: VisIndex.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
