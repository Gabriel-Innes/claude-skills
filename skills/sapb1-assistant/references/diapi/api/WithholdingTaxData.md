<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WithholdingTaxData (Object)

WithholdingTaxData is a child object of Documents object and represents the Withholding tax table related to the document. Source tables: INV5, RIN5, RDN5, RDN5, PCH5, RPC5, DPI5, DPO5, DRF5. The WithholdingTaxData object is relevant only to the following document types: - Documents(oInvoices), Documents(oCorrectionInvoice), Documents(oCorrectionInvoiceReversal) - OINV - Documents(oCreditNotes) - ORIN - Documents(oReturns) - ORDN - Documents(oPurchaseInvoices), Documents(oCorrectionPurchaseInvoice), Documents(oCorrectionPurchaseInvoiceReversal) - OPCH - Documents(oPurchaseCreditNotes) - ORPC - Documents(oDownPaymentsInput) - ODPI (not exposed through the DI API) - Documents(oDownPaymentsOutput) - ODPO (not exposed through the DI API) - Documents(oDrafts) - ODRF

**Remarks:** The data for the Withholding tax table consists on WithholdingTaxCodes definitions. To define withholding tax codes in the application: - Select Administration --> Setup --> Financials --> Tax --> Withholding Tax. To display the form in the application: - Select a document (for example, select Sales - A/R --> A/R Invoice). - From the main menu, select Go to --> WT Table.

## Properties (24)
- `Public Property BaseDocEntry() As Long` [R/W] Sets or returns the source document ID. Field name: BaseAbsEnt.
  - remarks: Use the BaseDocEntry, BaseDocType, and BaseDocLine properties to extract data from one document to another.
- `Public Property BaseDocLine() As Long` [R/W] Sets or returns the line number of the source document. Field name: BaseLine.
  - remarks: Use the BaseDocLine, BaseDocType, BaseDocEntry and properties to extract data from one document to another.
- `Public Property BaseDocType() As Long` [R/W] Sets or returns the source document type. Field name: BaseNum.
  - remarks: Use the BaseDocType, BaseDocEntry, and BaseDocLine properties to extract data from one document to another. To view the document type numbers, see BoAPARDocumentTypes.
- `Public Property BaseDocumentReference() As Long` [R] Returns the Base Document Reference number. Field name: BaseRef.
- `Public Property BaseType() As String` [R] Returns the amount type (Gross, Net, or VAT) on which the withholding tax calculation is based. Field name: BaseType. Length: 1 character.
  - remarks: The valid values are: - G - Gross. Total amount including VAT (country-specific for Europe only). - N - Net. Total amount without VAT (country-specific for Europe and Latin America). - V - VAT. VAT amount only (country-specific for Latin America only).
- `Public Property Category() As String` [R] Returns a valid value that indicates the cause for posting the withholding tax, either Payment (P) or Invoice (I). Field name: Category. Length: 1 character.
- `Public Property Count() As Long` [R] property Count
  - remarks: Returns the total withholding tax data lines.
- `Public Property Criteria() As String` [R] Returns the type of accounting under which the withholding tax is recorded. Length: 1 character. Field name: Criteria.
  - remarks: The valid values are: - Y - Accrual. - N - Cash.
- `Public Property GLAccount() As String` [R] Sets or returns the G/L account to which withholding tax is posted. Field name: Account. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property LineNum() As Long` [R] Returns the number of the withholding tax data line. Field name: LineNum.
- `Public Property Rate() As Double` [R] Returns the rate for calculating the withholding tax amount. Field name: Rate.
- `Public Property RoundingType() As String` [R] Returns the rounding method for calculating the withholding tax. Field name: RoundType. Length: 1 character.
  - remarks: Country-specific for Australia and New Zealand. The valid values are: - T - Truncated (known as Penalty Withholding Tax). Truncates the decimal value of both the base amount (TaxableAmount) and the calculated withholding tax amount (WTAmount). - C - Commercial rounding (known as Voluntary Withholding Tax). Round down 1 - 49 cents and round up 50 -99 cents of the calculated withholding tax amount (WTAmount).
- `Public Property Status() As BoStatus` [R] Determines whether the withholding tax status is Open or Close. Field name: status.
- `Public Property TargetAbsEntry() As Long` [R] Returns the target sum before the withholding tax calculations. Field name: TrgAbsEntr.
- `Public Property TargetDocumentType() As Long` [R] Returns the type of the target document. Field name: TrgType.
- `Public Property TaxableAmount() As Double` [R/W] Sets or returns the amount (in local currency) that is subject to withholding. Field name: TaxbleAmnt.
- `Public Property TaxableAmountFC() As Double` [R/W] Sets or returns the amount (in foreign currency) that is subject to withholding. Field name: TxblAmntFC.
- `Public Property TaxableAmountinSys() As Double` [R/W] Sets or returns the amount (in system currency) that is subject to withholding. Field name: TxblAmntSC.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WithholdingType() As String` [R] Returns the withholding tax type. Field name: Type. Length: 1 character.
  - remarks: Country-specific to Latin America. The valid values are: - I - Income withholding. This type is used when the supplier provides professional services and issues an invoice to the company. The company withholds the withholding tax amount, and then transfers this amount to the tax authority on behalf of the supplier. - V - VAT withholding. This type is used when the supplier cannot issue an invoice to the company, and therefore the company withholds the VAT amount (or part of it) and issues a purchase invoice.
- `Public Property WTAmount() As Double` [R/W] Sets or returns the withholding tax amount in local currency. Field name: ).
  - remarks: WTAmount is calculated as follows: WTAmount = TaxableAmount * Rate
- `Public Property WTAmountFC() As Double` [R/W] Sets or returns the withholding tax amount in foreign currency. Field name: WTAmntFC.
  - remarks: WTAmountFC is calculated as follows: WTAmountFC = TaxableAmountFC * Rate
- `Public Property WTAmountSys() As Double` [R/W] Sets or returns the withholding tax amount in system currency. Field name: WTAmntSC.
  - remarks: WTAmountSys is calculated as follows: WTAmountSys = TaxableAmountinSys * Rate
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code. Field name: WTCode. Length: 4 characters. This is a foreign key to the WithholdingTaxCodes Object.
  - remarks: You can set only WT codes that are relevant to the business partner as defined in BPWithholdingTax object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
