<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ClosingDateProcedure (Object)

The ClosingDateProcedure object enables to retrieve the closing date procedure definition. This object is applicable for cluster B (country-specific for Japan only). Source table: OCDP.

**Remarks:** To display the form in the application: - Select Administration > Definitions > Business Partners > Define Closing Date Procedure. The application logic is similar to the Payment Terms calculation for the Closing date. In addition, the Closing Date is always greater or equal to Baseline Date (posting date or system date). When Closing Date is earlier than Baseline date, the month of Closing date will be added by 1. For example, Closing Date is every 20th, when posting date is April 19, Closing Date is April 20; when posting date is April 21, Closing Date is May 20.

## Properties (8)
- `Public Property BaselineDate() As BoClosingDateProcedureBaseDateEnum` [R] Returns the reference date for executing a transaction: Posting Date or System Date. Field name: BsLineDate.
  - remarks: Default: System Date.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ClosingDateCode() As String` [R] Returns the code of the closing date procedure. Field name: ClsDtCode. Length: 30 characters.
- `Public Property ClosingDateNum() As Long` [R] Returns the closing date procedure number. Field name: ClsDateNum.
- `Public Property DueMonth() As BoClosingDateProcedureDueMonthEnum` [R] Returns the start from date for calculating the transaction due date: begining date of the month, middle date of the month, or end date of the month. Field name: DueMonth.
- `Public Property ExtraDay() As Long` [R] Returns the number of additional days for calculating the due date. Field name: ExtraDay.
- `Public Property ExtraMonth() As Long` [R] Returns the number of additional months for calculating the due date. Field name: ExtraMonth.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (4)
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal ClosingDateNum As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ClosingDateNum`: ClosingDateNum.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
