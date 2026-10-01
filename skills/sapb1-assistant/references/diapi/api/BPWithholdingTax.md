<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPWithholdingTax (Object)

BPWithholdingTax is a child object of the BusinessPartners object that represents the withholding tax data related to the business partner. Source table: CRD4.

## Properties (4)
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the total number of records in the object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code assigned to the business partner. Field name: WTCode. Length: 4 characters. This is a foreign key to the WithholdingTaxCodes object.
  - remarks: This is a foreign key to WithholdingTaxCodes object. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, India, and Portugal. For India localizations, if this property is set to yes, then the TaxId0 property of the BPFiscalTaxID object is mandatory and must be set to a 10-character value.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
