<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesTaxCodes_Lines (Object)

TaxCodes_Lines is a child object of the SalesTaxCodes object and represents the tax authorities/types from which the tax code is combined. Source table: STC1.

## Properties (12)
- `Public Property Count() As Long` [R] Returns the total rows in the table.
- `Public Property CSTCodeIn() As String` [R/W] property CSTCodeIn
- `Public Property CSTSuffix() As String` [R/W] property CSTSuffix
- `Public Property EffectiveRate() As Double` [R] Returns the effective rate based on the rate of the specified tax authority/type (Rate) and tax-on-tax calculation (STATaxonTaxCode and STATaxOnTaxType). Field name: EfctivRate.
  - remarks: For example, if a tax code is combined of two lines (two tax jurisdictions): - New York state - tax rate 4 - New York city - tax rate 10 The effective rate of the first line equals to 4STATaxonTaxCode and STATaxOnTaxType relates to New York state, then the effective rate of the second line equals to 10.4"> (10 + 10 x 4Rate) is 14.4"> (4). If the values of STATaxonTaxCode and STATaxOnTaxType relates to null, then the effective rate of the second line equals to 10Rate) is 14"> (4 + 10).
- `Public Property FormulaId() As Long` [R/W] property FormulaId
- `Public Property RowNumber() As Long` [R] Returns the current available row number (starts from 1). Field name: Line_ID.
- `Public Property STACode() As String` [R/W] Sets or returns the code of the tax authority. Field name: e. Length: 8 characters.
  - remarks: STACode is the primary key.
- `Public Property STATaxonTaxCode() As String` [R/W] Sets or returns the code of the tax authority on which the tax-on-tax is based. Field name: TaxOnTCod. Length: 8 characters.
- `Public Property STATaxOnTaxType() As Long` [R/W] Sets or returns the type of the sales tax authority on which the tax-on-tax is based. Field name: TaxOnTType.
- `Public Property STAType() As Long` [R/W] Sets or returns the type of the sales tax authority on which the tax rate of the current line is based. Field name: STAType. This is a foreign key to the SalesTaxAuthorities object.
- `Public Property STCCode() As String` [R] Sets or returns the code of the tax authority on which the the tax rate of the current line is based. Field name: STCCode. Length: 8 characters. This is a foreign key to the SalesTaxCodes object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
