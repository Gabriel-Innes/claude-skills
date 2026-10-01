<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DownPaymentsToDraw (Object)

Represents down payments drawn into A/R or A/P invoices. The Documents.DownPaymentAmount property is updated with the total amount to draw. Source tables: INV9, PCH9, RIN9, RPC9, DRF9

## Properties (21)
- `Public Property AmountToDraw() As Double` [R/W] The net amount (without tax) drawn to the invoice. Field name: DrawnSum
  - remarks: The amount to draw cannot exceed the open amount.
- `Public Property AmountToDrawFC() As Double` [R/W] The net amount (without tax) drawn to the invoice in foreign currency. Field name: DrawnSumFc
  - remarks: The amount to be drawn cannot be more than the open amount.
- `Public Property AmountToDrawSC() As Double` [R/W] The net amount (without tax) drawn to the invoice in system currency. Field name: DrawnSumSc
  - remarks: The amount to be drawn cannot be more than the open amount.
- `Public Property Count() As Long` [R] The number of downpayment lines in the collection.
- `Public Property Details() As String` [R] Set to the Remarks field in the down payment invoice. Field name: BsComments
- `Public Property DocEntry() As Long` [R/W] An internal key to the down payment document. Field name: BaseAbs
- `Public Property DocInternalID() As Long` [R] A key to the invoice for which the down payment is used. Field name: DocEntry
- `Public Property DocNumber() As Long` [R] The document number of the down payment document. Field name: BaseDocNum
- `Public Property DownPaymentsToDrawDetails() As DownPaymentsToDrawDetails` [R] The details for this drawn downpayment. A drawn downpayment can be applied to various tax groups and in different ways.
- `Public Property DownPaymentType() As DownPaymentTypeEnum` [R] Indicates whether the down payment document is an invoice or a request. Field name: Posted
- `Public Property DueDate() As Date` [R] Returns the due date of the down payment invoice. Field name: BsDueDate
- `Public Property GrossAmountToDraw() As Double` [R/W] The gross amount (with tax) drawn to the invoice. Field name: Gross
- `Public Property GrossAmountToDrawFC() As Double` [R/W] The gross amount (with tax) drawn to the invoice in foreign currency. Field name: GrossFc
- `Public Property GrossAmountToDrawSC() As Double` [R/W] The gross amount (with tax) drawn to the invoice in system currency. Field name: GrossSc
- `Public Property IsGrossLine() As BoYesNoEnum` [R] Indicates whether the gross amount was entered and all other fields were calculated based on the gross amount. Field name: IsGross
- `Public Property Name() As String` [R] The full name of the business partner. Field name: BsCardName
- `Public Property PostingDate() As Date` [R] The posting date of the down payment invoice. Field name: BsDocDate
- `Public Property RowNum() As Long` [R] The row number of the current drawn payment in the collection. Field name: LineNum
- `Public Property Tax() As Double` [R] The part of the drawn downpayment to be used for tax. Field name: Vat
- `Public Property TaxFC() As Double` [R] The part of the drawn downpayment to be used for tax in foreign currency. Field name: VatFc
- `Public Property TaxSC() As Double` [R] The part of the drawn downpayment to be used for tax in system currency. Field name: VatSc

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
