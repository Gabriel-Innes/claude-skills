<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserActionRecord (Object)

Displays the access details and the actions of SAP Business One users who have logged on and logged off with the SAP Business One client or the DI API. Source table: USR5.

**Remarks:** In the SAP Business One application, to open the Access Log window, in the SAP Business One menu bar, choose Tools --> Access Log. To open the Access Log Details window, in the Access Log window, double-click the table row of a user whose access information you want to display.

**Example:**
- C# example (from SAP's help):
  ```csharp
  UserActionRecord oUserActionRecord = (UserActionRecord)oCompany.GetBusinessObject(BoObjectTypes.oUserActionRecord);
  Recordset rs = (Recordset)oCompany.GetBusinessObject(BoObjectTypes.BoRecordset);
  rs.DoQuery("select * from USR5 where UserID = 'manager' and Date > '2009-11-01'");

  oUserActionRecord.Browser.Recordset = rs;
  oUserActionRecord.Browser.MoveFirst();

  while (!oUserActionRecord.Browser.EoF)
  {
      Console.Write(oUserActionRecord.UserCode + "\t");
      Console.Write(oUserActionRecord.Action + "\t");
      Console.Write(oUserActionRecord.ActionBy + "\t");
      Console.Write(oUserActionRecord.ClientIP + "\t");
      Console.Write(oUserActionRecord.ClientName + "\t");
      Console.Write(oUserActionRecord.ActionDate + "\t");
      Console.Write(oUserActionRecord.ActionTime + "\t");
      Console.WriteLine();

      oUserActionRecord.Browser.MoveNext();
  }
  ```

## Properties (14)
- `Public Property Action() As UserActionTypeEnum` [R] The action that the user performed. Field name: Action.
- `Public Property ActionBy() As String` [R] The user ID of the user who performed the action. Field name: ActionBy. Length: 8 characters.
- `Public Property ActionDate() As Date` [R] The date of the action. Field name: Date.
- `Public Property ActionTime() As Date` [R] The time of the action. Field name: Time.
- `Public Property AliveDuration() As Long` [R] property AliveDuration
- `Public Property ClientIP() As String` [R] The IP addresses of the SAP Business One client computer in use by the user. Field name: ClientIP. Length: 200 characters.
- `Public Property ClientName() As String` [R] The name of the SAP Business One client computer in use by the user. Field name: ClientName. Length: 32 characters.
- `Public Property Count() As Long` [R] Returns the total number of records.
- `Public Property ProcessID() As Long` [R] The process ID of the SAP Business One application. Field name: ProcessID.
- `Public Property ProcessName() As String` [R] The process name of the logged-on application. Field name: ProcName. Length: 80 characters.
- `Public Property UserCode() As String` [R] Returns the user code. This is the foreign key to the Users object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WindowsSession() As Long` [R] The windows session ID. Field name: WinSessnID.
- `Public Property WindowsUser() As String` [R] The windows user name. Field name: WinUsrName. Length: 100 characters.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
