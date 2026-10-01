<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Payments_Accounts (Object)

Payments_Accounts is a child object of the Payments object and represents the payments through account transfers in the Banking module. Source tables: RCT4 (incoming payments) and VPM4 (outgoing payments).

**Remarks:** Mandatory fields in SAP Business One: AccountCode and SumPaid. For account segmentation add the string _SYS00. To display the form in the application: - For RCT4 table, select Banking --> Incoming Payments --> Incoming Payments. - or - For VPM4 table, select Banking --> Outgoing Payments --> Payments to Vendors. - Select Account document type (instead of Customer or Vendor).

## Properties (18)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code of the business partner as defined in Chart of Accounts. Field name: AcctCode. Mandatory property. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
  - remarks: To set the AccountCode value when working with segmentation, use the FormatCode to find its key value (for example, _SYS00000000010) as follows: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010).
- `Public Property AccountName() As String` [R/W] Returns the G/L account name of the business partner as defined in Chart of Accounts. Field name: AcctName. Length: 100 characters.
- `Public Property Count() As Long` [R] Returns the number of lines in this document.
- `Public Property Decription() As String` [R/W] Sets or returns a description about the account. Field name: Descrip. Length: 250 characters.
- `Public Property EqualizationVatAmount() As Double` [R] Equalization tax amount. Field name: EquVatSum
  - remarks: For Spain only.
- `Public Property GrossAmount() As Double` [R/W] Sets or returns this payment account Gross amount. Field name: GrossAmnt
- `Public Property LineNum() As Long` [R] Returns the number of the current line. Field name: LineId.
- `Public Property LocationCode() As Long` [R] Returns the location code in incoming and outgoing payments. Applicable for cluster B. Field name: LocCode.
- `Public Property ProfitCenter() As String` [R/W] A distribution rule for dimension 1. Field name: OcrCode Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProfitCenter2() As String` [R/W] A distribution rule for dimension 2. Field name: OcrCode2 Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProfitCenter3() As String` [R/W] A distribution rule for dimension 3. Field name: OcrCode3 Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProfitCenter4() As String` [R/W] A distribution rule for dimension 4. Field name: OcrCode4 Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProfitCenter5() As String` [R/W] A distribution rule for dimension 5. Field name: OcrCode5 Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code. Field name: Project. Length: 8 characters. This is a foreign key to the OPRJ object.
- `Public Property SumPaid() As Double` [R/W] Sets or returns the amount paid. Field name: SumApplied. Mandatory property.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatAmount() As Double` [R/W] Sets or returns the VAT amount of incoming or outgoing payments. Field name: VatAmnt.
- `Public Property VatGroup() As String` [R/W] Sets or returns the VAT group for this payment. Field name: VatGroup. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: The VAT group specifies how much VAT the payment is liable to.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
