<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WithholdingTaxLines (Object)

WithholdingTaxLines is a child object of Document_Lines object and supports Withholding Tax in a line level (as opposed to WithholdingTaxData object, which supports Withholding Tax in a document level). The WithholdingTaxLines object is applicable for cluster B only (country-specific for Brazil only). Source table: INV5. Relevant only for the following tables: OINV, ORIN, ODLN, ORDR, ORDN, OPCH, ORPC, OPDN, ORPD, OPOR, ODRF, OCSI, OCSV, OCPI, and OCPV.

**Remarks:** The data for the Withholding tax table consists on WithholdingTaxCodes definitions. To define withholding tax codes in the application: - Select Administration --> Setup --> Financials --> Tax --> Withholding Tax. To display the form in the application: - Select a document (for example, select Sales - A/R --> A/R Invoice). - Select a document line. - From the main menu, select Go to --> WT Table.

## Properties (22)
- `Public Property BaseDocEntry() As Long` [R/W] Sets or returns the source document ID.
- `Public Property BaseDocLine() As Long` [R/W] Sets or returns the line number of the source document.
- `Public Property BaseDocType() As Long` [R/W] Sets or returns the source document.
- `Public Property BaseType() As String` [R] Returns the amount type (Gross, Net, or VAT) on which the withholding tax calculation is based. Length: 1 character.
  - remarks: The valid values are: - G - Gross. Total amount including VAT (country-specific for Europe only). - N - Net. Total amount without VAT (country-specific for Europe and Latin America). - V - VAT. VAT amount only (country-specific for Latin America only).
- `Public Property Category() As String` [R] Returns a valid value that indicates the cause for posting the withholding tax, either Payment (P) or Invoice (I). Length: 1 character.
- `Public Property Count() As Long` [R] Returns the total withholding tax data lines.
- `Public Property Criteria() As String` [R] Returns the type of accounting under which the withholding tax is recorded. Length: 1 character.
- `Public Property CSTCodeIncoming() As String` [R/W] property CSTCodeIncoming
- `Public Property CSTCodeOutgoing() As String` [R/W] property CSTCodeOutgoing
- `Public Property GLAccount() As String` [R] Sets or returns the G/L account to which withholding tax is posted. Length: 15 characters.
- `Public Property LineNum() As Long` [R] Returns the number of the withholding tax line.
- `Public Property Rate() As Double` [R] Returns the percentage rate for calculating the withholding tax amount.
- `Public Property RoundingType() As String` [R] Returns the rounding method for calculating the withholding tax. Length: 1 character.
  - remarks: The valid values are: - T - Truncated (known as Penalty Withholding Tax). Truncates the decimal value of both the base amount (TaxableAmount) and the calculated withholding tax amount (WTAmount). - C - Commercial rounding (known as Voluntary Withholding Tax). Round down 1 - 49 cents and round up 50 -99 cents of the calculated withholding tax amount (WTAmount).
- `Public Property TaxableAmount() As Double` [R/W] Sets or returns the amount (in local currenxy) that is subject to withholding.
- `Public Property TaxableAmountFC() As Double` [R/W] Sets or returns the taxable amount (in foreign currency) that is subject to withholding.
- `Public Property TaxableAmountinSys() As Double` [R/W] Sets or returns the taxable amount (in system currency) that is subject to withholding.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WithholdingType() As String` [R] Returns the withholding tax type. Length: 1 character.
  - remarks: The valid values are: - I - Income withholding. This type is used when the supplier provides professional services and issues an invoice to the company. The company withholds the withholding tax amount, and then transfers this amount to the tax authority on behalf of the supplier. - V - VAT withholding. This type is used when the supplier cannot issue an invoice to the company and therefore the company withholds the VAT amount (or part of it) and issues a purchase invoice.
- `Public Property WTAmount() As Double` [R/W] Sets or returns the withholding tax amount in local currency.
- `Public Property WTAmountFC() As Double` [R/W] Sets or returns the withholding tax amount in foreign currency.
- `Public Property WTAmountSys() As Double` [R/W] Sets or returns the withholding tax amount in system currency.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code. Length: 4 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
