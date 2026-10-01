<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Payments_Invoices (Object)

Payments_Invoices is a child object of the Payments object and represents the invoices related to the payments in the Banking module. Source tables: RCT2 (incoming payments) and VPM2 (outgoing payments).

**Remarks:** Mandatory field in SAP Business One: DocEntry. To display the form in the application: - For RCT2 table, select Banking --> Incoming Payments --> Incoming Payments. - For VPM2 table, select Banking --> Outgoing Payments --> Payments to Vendors.

## Properties (24)
- `Public Property AppliedFC() As Double` [R/W] Sets or returns the amount paid in foreign currency. Field name: AppliedFC.
  - remarks: If the invoice does not use foreign currency, enter 0 in this field.
- `Public Property Count() As Long` [R] Returns the number of lines in this document.
  - remarks: The value of this property increases automatically, after adding a new line to the document.
- `Public Property DiscountPercent() As Double` [R/W] Sets or returns the discount percentage you specify for a customer, or the discount percentage a supplier specifies for you. Field name: Discount. Sets or returns the discount percentage you specify for a customer, or the discount percentage a supplier specifies for you. Field name: Discount.
  - remarks: The default value is retrieved from DiscountPercent property of the BusinessPartners object. You can update the value of the DiscountPercent property only in sales quotations, sales orders, purchase quotations, and purchase orders. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types. The default value is retrieved from DiscountPercent property of the BusinessPartners object. You can update the value of the DiscountPercent property only in sales quotations, sales orders, purchase quotations, and purchase orders. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types. This property is not relevant when using Down Payment.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for dimension 1 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode This is a foreign key to the DistributionRule object.
- `Public Property DistributionRule2() As String` [R/W] The distribution rule for dimension 2 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode2 This is a foreign key to the DistributionRule object.
- `Public Property DistributionRule3() As String` [R/W] The distribution rule for dimension 3 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode3 This is a foreign key to the DistributionRule object.
- `Public Property DistributionRule4() As String` [R/W] The distribution rule for dimension 4 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode4 This is a foreign key to the DistributionRule object.
- `Public Property DistributionRule5() As String` [R/W] The distribution rule for dimension 5 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode5 This is a foreign key to the DistributionRule object.
- `Public Property DocEntry() As Long` [R/W] Sets or returns the invoice key. Mandatory property. Field name: DocEntry. This is a foreign key to the Documents object.
  - remarks: You can use this key to as a reference to an invoice.
- `Public Property DocLine() As Long` [R/W] Sets or returns the row key in the invoice document. Field name: DocLine.
- `Public Property DocNum() As Long` [R] Document number. Field name: DocNum.
- `Public Property InstallmentId() As Long` [R/W] Sets or returns the installment ID of the invoice payment. Field name: InstId.
- `Public Property InvoiceType() As BoRcptInvTypes` [R/W] Sets or returns a valid value of BoRcptInvTypes type that specifies the invoice type (incoming payment, tax invoice, correction invoice, and so on). Field name: InvType. Length: 20 characters.
- `Public Property LineNum() As Long` [R] Returns the active row number. Field name: DocLine.
- `Public Property LinkDate() As Date` [R] Returns the date when the payment was connected to the invoice. Field name: DpmPosted.
  - remarks: Country-specific for Poland only. This property is used when a payment is made before receiving the invoice. For example, when a payment is made upon a proforma invoice and the invoice is received later.
- `Public Property PaidSum() As Double` [R] Returns the amount (of the invoice) paid that applies to the 1099 report. Field name: PaidSum.
  - remarks: Country-specific field for US.
- `Public Property SumApplied() As Double` [R/W] Sets or returns the amount (of the invoice) paid. Field name: SumApplied.
- `Public Property TotalDiscount() As Double` [R/W] The total discount (from the cash discount settings) in local currency. Field name: DcntSum
  - remarks: If TotalDiscount, DiscountPercent and SumApplied are provided, then DiscountPercent is recalculated. If DiscountPercent and SumApplied are provided, then TotalDiscount is calculated. If TotalDiscount and DiscountPercent are provided, then SumApplied is calculated. DiscountPercent is recalculated beause TotalDiscount has higher priority than DiscountPercent.
- `Public Property TotalDiscountFC() As Double` [R/W] The total discount (from the cash discount settings) in foreign currency. Field name: DcntSumFC
  - remarks: For more information on the business logic, see TotalDiscount.
- `Public Property TotalDiscountSC() As Double` [R] The total discount (from the cash discount settings) in system currency. Field name: DcntSumSy
  - remarks: For more information on the business logic, see TotalDiscount.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WitholdingTaxApplied() As Double` [R] Returns the amount of the withholding tax that was applied for the invoice (in local currency). Field name: WtAppld.
  - remarks: The posting date of the withholding tax depends on the withholding category as defined in SAP Business One: - Payment Category: Withholding tax is posted upon payment. - Invoice Category: Withholding tax is posted upon invoice.
- `Public Property WitholdingTaxAppliedFC() As Double` [R] Returns the amount of the withholding tax that applied for the invoice (in foreign currency). Field name: WtAppldFC.
- `Public Property WitholdingTaxAppliedSC() As Double` [R] Returns the amount of the withholding tax that applied for the invoice (in system currency). Field name: WtAppldSC.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
