<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallSolutions (Object)

ServiceCallSolutions is a child object of the ServiceCalls object in the Service module. The service call solutions are associated with the Knowledge Base Solutions table. Source table: SCL1.

**Remarks:** Mandatory field in SAP Business One: SolutionID. To display the form in the application: - Select Service --> Service Call. - Select the Solutions tab.

## Properties (4)
- `Public Property Count() As Long` [R] Returns the total rows in the solutions table.
- `Public Property LineNum() As Long` [R] Returns the current row number. Field name: line.
- `Public Property SolutionID() As Long` [R/W] KnowledgeBaseSolutionsSets or returns the solution ID. Mandatory property. Field name: solutionID. This is a foreign key to the KnowledgeBaseSolutions object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ServiceCalls oSrvCall;

    // Delete service call solution
    if (oSrvCall.GetByKey(2) == true)
    {
        oSrvCall.Solutions.SetCurrentLine(1);
        oSrvCall.Solutions.Delete();
        oSrvCall.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
