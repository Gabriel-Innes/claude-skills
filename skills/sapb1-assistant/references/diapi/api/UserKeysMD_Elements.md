<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserKeysMD_Elements (Object)

UserKeysMD_Elements is a child object of the UserKeysMD object. UserKeysMD_Elements defines the fields that combine the key index. Source table: UKD1.

## Properties (3)
- `Public Property ColumnAlias() As String` [R/W] Sets or returns the field name in the database. Field name: ColAlias. Length: 18 characters.
- `Public Property Count() As Long` [R] Returns the total key indexes that exist in the collection.
- `Public Property SubKeyIndex() As Long` [R] Returns the internal key of the field. Used for reference only. Field name: SubKeyId.

## Methods (2)
- `Public Sub Add()` Adds a field to an existing key index.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
