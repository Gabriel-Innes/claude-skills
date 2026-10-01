<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Payments_Checks (Object)

Represents checks that are tied to an outgoing payment document. Checks that are not tied to a document are represented by the ChecksforPayment object. Source tables: RCT1 (incoming payments) and VPM1 (outgoing payments).

**Remarks:** Mandatory fields in SAP Business One: BankCode and CheckSum. To display the form in the application: - For RCT1 table, select Sales - A/R --> A/R Invoice. - or - For VPM1 table, select Purchasing - A/P --> A/P Invoice. - On the toolbar, click the Payment Means icon (or press CTRL+Y). - Select the Check tab.

## Properties (20)
- `Public Property AccounttNum() As String` [R/W] Sets or returns the bank account number of the check. Field name: AcctNum. Length: 50 characters.
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code of the check. Field name: BankCode. Mandatory property. Length: 30 characters.
- `Public Property Branch() As String` [R/W] Sets or returns the branch name of the bank. Field name: Branch. Length: 50 characters.
- `Public Property CheckAbsEntry() As Long` [R] Returns the absolute entry of this Check. Field name: CheckAbs. This is a foreign key to the Payments Object
- `Public Property CheckAccount() As String` [R/W] Sets or returns the G/L account associated with this Check Account. Field name: CheckAct. Length: 15 characters.
- `Public Property CheckNumber() As Long` [R/W] Sets or returns this check number. Field name: CheckNum.
- `Public Property CheckSum() As Double` [R/W] Sets or returns the amount of the check. Mandatory property. Field name: CheckSum.
- `Public Property Count() As Long` [R] Returns the number of checks in this payment.
  - remarks: The value of this property updates automatically, after you add new lines to the document.
- `Public Property CountryCode() As String` [R/W] Sets or returns the country code of the bank. Field name: CountryCod. Length: 3 characters. This is a foreign key to the Countries table (OCRY) - not exposed through the DI API.
  - remarks: You can set any country code that is defined in the Countries table in SAP Business One.
- `Public Property Details() As String` [R/W] Sets or returns a description of the check. Field name: Details. Length: 254 characters.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date of the check. Field name: DueDate.
- `Public Property ECheck() As BoYesNoEnum` [R/W] Specify whether the account is relevant for e-check functionality or not. Field name: ECheck.
- `Public Property EndorsableCheckNo() As Long` [R/W] property EndorsableCheckNo
- `Public Property Endorse() As BoYesNoEnum` [R/W] property Endorse
- `Public Property FiscalID() As String` [R/W] property FiscalID
- `Public Property LineNum() As Long` [R] Returns the number of the current line in the document. Field name: LineID.
- `Public Property ManualCheck() As BoYesNoEnum` [R/W] Indicates that the check number was entered manually. Field name: ManualChk
- `Public Property OriginallyIssuedBy() As String` [R/W] property OriginallyIssuedBy
- `Public Property Trnsfrable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the check can be transferred to a third-party. Field name: Trnsfrable.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
