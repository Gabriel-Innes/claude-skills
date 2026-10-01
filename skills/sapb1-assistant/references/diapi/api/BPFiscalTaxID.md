<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPFiscalTaxID (Object)

BPFiscalTaxID is a child object of the BusinessPartners and indicates the Brazilian Fiscal IDs info for each business partner. You can retrieve or set this object by using the FiscalTaxID property of the BusinessPartners object. This object enables you to: - Add the Fiscal IDs of the business partner. - Define the Fiscal TAX IDs for Business Partner Master Data. Source table: CRD7

**Remarks:** This Object is specific to Cluster 2B (Country specific property for Brazil only).

## Properties (22)
- `Public Property Address() As String` [R/W] Sets or returns the Business Partner address. Field name: Address. Length: 50 characters.
- `Public Property AddrType() As BoAddressType` [R] Indicates the type of address for this fiscal ID.
- `Public Property AuthorizationForRetrieveFromSEFAZ() As BoYesNoEnum` [R/W] Authorization for retrieve from SEFAZ. Field name: AToRetrNFe.
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property CNAECode() As Long` [R/W] Sets or returns the Brazil CNAE code. Field name: CNAEId. This is a foreign key to the CNAE (Change Notification Agent Code) table (OCNA), not exposed through the DI API.
- `Public Property Count() As Long` [R] Returns the number of Fiscal IDs for current BusinessPartner.
- `Public Property TaxId0() As String` [R/W] Sets or returns the Fiscal Tax ID 0. Field name: TaxId0. Length: 100 characters.
  - remarks: For India localizations, this number represents the PAN number. If the SubjectToWithholdingTax property of the BusinessPartners object is set to yes, then TaxId0 is mandatory and must be set to a 10-character value.
- `Public Property TaxId1() As String` [R/W] Sets or returns the Fiscal Tax ID 1. Field name: TaxId1. Length: 100 characters.
- `Public Property TaxId10() As String` [R/W] Sets or returns the Fiscal Tax ID 10. Field name: TaxId10. Length: 100 characters.
- `Public Property TaxId11() As String` [R/W] Sets or returns the Fiscal Tax ID 11. Field name: TaxId11. Length: 100 characters.
- `Public Property TaxId12() As String` [R/W] Sets or returns the Fiscal Tax ID 12. Field name: TaxId12. Length: 50 characters.
- `Public Property TaxId13() As String` [R/W] Sets or returns the Deductee Ref. No. in India. Field name: TaxId13. Length: 100 characters.
- `Public Property TaxId14() As String` [R/W] Sets or returns the ITR Filing. Field name: TaxId14. Length: 250 characters.
- `Public Property TaxId2() As String` [R/W] Sets or returns the Fiscal Tax ID 2. Field name: TaxId2. Length: 100 characters.
- `Public Property TaxId3() As String` [R/W] Sets or returns the Fiscal Tax ID 3. Field name: TaxId3. Length: 100 characters.
- `Public Property TaxId4() As String` [R/W] Sets or returns the Fiscal Tax ID 4. Field name: TaxId4. Length: 100 characters.
- `Public Property TaxId5() As String` [R/W] Sets or returns the Fiscal Tax ID 5. Field name: TaxId5. Length: 100 characters.
- `Public Property TaxId6() As String` [R/W] Sets or returns the Fiscal Tax ID 6. Field name: TaxId6. Length: 100 characters.
- `Public Property TaxId7() As String` [R/W] Sets or returns the Fiscal Tax ID 7. Field name: TaxId7. Length: 100 characters.
- `Public Property TaxId8() As String` [R/W] Sets or returns the Fiscal Tax ID 8. Field name: TaxId8. Length: 100 characters.
- `Public Property TaxId9() As String` [R/W] Sets or returns the Fiscal Tax ID 9. Field name: TaxId9. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new record to the CRD7 table.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
