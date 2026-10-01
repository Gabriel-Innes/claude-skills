<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallActivities (Object)

ServiceCallActivities is a child object of the ServiceCalls object in the Service module. The service call activities are associated with the Activities with Business Partners table. Source table: SCL5.

**Remarks:** Mandatory field in SAP Business One: ActivityCode. To display the form in the application: - Select Service --> Service Call. - Select the Activities tab.

## Properties (4)
- `Public Property ActivityCode() As Long` [R/W] Sets or returns the activity code. Mandatory property. Field name: ClgID. This is a foreign key to the Contacts object.
- `Public Property Count() As Long` [R] Returns the total rows in the activities table.
- `Public Property LineNum() As Long` [R] Returns the current row number. Field name: Line.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: You cannot delete a line if the service call is closed.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ServiceCalls oSrvCall;

    // Delete service call activity
    if(oSrvCall.GetByKey(1) == true)
    {
        oSrvCall.Activities.SetCurrentLine(1);
        oSrvCall.Activities.Delete();
        oSrvCall.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
