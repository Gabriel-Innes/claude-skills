<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallInventoryExpenses (Object)

ServiceCallInventoryExpenses is a child object of the ServiceCalls object in the Service module. Source table: SCL4.

**Remarks:** To display the form in the application: - Select Service --> Service Call. - Select the Expenses tab.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the total rows in the inventory expenses table associated with the service call.
- `Public Property DocEntry() As Long` [R/W] Sets or returns the internal key of the document associated with the service call inventory expenses. Field name: DocAbs.
- `Public Property DocumentNumber() As Long` [R/W] Sets or returns the number of the document associated with the service call inventory expenses. Field name: DocNumber.
- `Public Property DocumentPostingDate() As Date` [R] Returns the date of the document posting. Field name: DocPstDate.
- `Public Property DocumentType() As BoSvcEpxDocTypes` [R/W] Sets or returns a valid value of BoSvcEpxDocTypes that specifies the document type associated with the service call inventory expenses. Field name: Object.
- `Public Property LineNum() As Long` [R] Returns the current row number. Field name: Line.
- `Public Property PartType() As BoSvcExpPartTypes` [R] Not supported. Field name: PartType.
- `Public Property StockTransferDirection() As BoStckTrnDir` [R/W] Sets or returns a valid value of BoStckTrnDir type that specifies the transfer direction of items related to the service call, to or from the technician. Field name: StckTrnDir.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ServiceCalls oSrvCall;

    // Delete service call expense
    if (oSrvCall.GetByKey(2) == true)
    {
        oSrvCall.Expenses.SetCurrentLine(1);
        oSrvCall.Expenses.Delete();
        oSrvCall.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
