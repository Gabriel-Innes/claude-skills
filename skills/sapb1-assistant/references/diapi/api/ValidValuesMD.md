<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ValidValuesMD (Object)

ValidValuesMD enables you to add valid values to a specified user defined field (UserFieldsMD). Source table: UFD1.

**Remarks:** To display the form in the application: - From the main menu bar, select Tools --> Manage User Fields. - Click User Tables.

## Properties (3)
- `Public Property Count() As Long` [R] Retrieves the number of the valid values in the collection.
- `Public Property Description() As String` [R/W] Sets or returns the description of the valid value. Field name: Descr. Length: 254 characters.
- `Public Property Value() As String` [R/W] Sets or returns the valid value. Field name: FldValue. Length: 254 characters.

## Methods (3)
- `Public Sub Add()` Adds a new valid value to the collection.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.UserFieldsMD oUFMD;

    // Delete valid value
    if(oUFMD.GetByKey("@MyObj", 0) == true)
    {
        oUFMD.ValidValues.SetCurrentLine(0);
        oUFMD.ValidValues.Delete();
        oUFMD.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
