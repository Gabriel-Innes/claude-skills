<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPPaymentMethods (Object)

BPPaymentMethods is a child object of the BusinessPartners object that represents the payment methods related to the business partner. Source table: CRD2.

## Properties (5)
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the number of payment methods related to the business partner. Returns the total number of records in the object.
- `Public Property PaymentMethodCode() As String` [R/W] Sets or returns the payment method related to the business partner. Field name: PymCode. This is a foreign key to the WizardPaymentMethods Object. Length: 15 characters.
- `Public Property RowNumber() As Long` [R] Returns the available row number. Field name: LineNum.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Add a new PaymentMethod to the object. Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the row specified by the parameter to be the current active row. Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
