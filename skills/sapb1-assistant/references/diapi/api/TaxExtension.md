<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxExtension (Object)

TaxExtension is a child object of the Documents object. It stores fiscal IDs of marketing documents. Every marketing document has a set of fiscal IDs. The TaxExtension object is applicable for cluster B (country-specific for Brazil and India). Source tables: CPI12, CPV12, CSI12, CSV12, DLN12, DRF12, IGE12, IGN12, INV12, PCH12, PDN12, POR12, QUT12, RDN12, RDR12, RIN12, RPC12, RPD12, and WTR12.

**Remarks:** To display the form in the application: - Select a marketing document. - Select the Tax tab. - Click the Fiscal IDs button.

## Properties (58)
- `Public Property BillOfEntryDate() As Date` [R/W] property BillOfEntryDate
- `Public Property BillOfEntryNo() As String` [R/W] property BillOfEntryNo
- `Public Property BlockB() As String` [R/W] Sets or returns the block of the bill-to address.
- `Public Property BlockS() As String` [R/W] Sets or returns the block of the ship-to address.
- `Public Property BoEValue() As Double` [R/W] property BoEValue
- `Public Property Brand() As String` [R/W] Sets or returns the brand fiscal Id. Field name: Brand. Length: 20 characters.
- `Public Property BuildingB() As String` [R/W] Sets or returns the Building of the bill-to address.
- `Public Property BuildingS() As String` [R/W] Sets or returns the Building of the ship-to address. Field name: Building.
- `Public Property Carrier() As String` [R/W] Sets or returns the carrier code. Field name: Carrier. Length: 15 characters.
- `Public Property CityB() As String` [R/W] Sets or returns the Building of the bill-to address.
- `Public Property CityS() As String` [R/W] Sets or returns the City of the ship-to address.
- `Public Property ClaimRefund() As BoYesNoEnum` [R/W] property ClaimRefund
- `Public Property CountryB() As String` [R/W] Sets or returns the Country of the bill-to address.
- `Public Property CountryS() As String` [R/W] Sets or returns the Country of the ship-to address.
- `Public Property County() As String` [R/W] Sets or returns the county code. Field name: County. Length: 7 characters.
- `Public Property CountyB() As String` [R/W] Sets or returns the County of the bill-to address.
- `Public Property CountyS() As String` [R/W] Sets or returns the County of the Ship-to address.
- `Public Property DifferentialOfTaxRate() As Long` [R/W] property DifferentialOfTaxRate
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property GlobalLocationNumberB() As String` [R/W] property GlobalLocationNumberB
- `Public Property GlobalLocationNumberS() As String` [R/W] property GlobalLocationNumberS
- `Public Property GrossWeight() As Double` [R/W] Sets or returns the gross weight.
- `Public Property ImportOrExport() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether the Sales Tax Invoice is for import or export. Applicable for cluster B (country-specific for India). Field name: ImpOrExp (INV12).
- `Public Property ImportOrExportType() As ImportOrExportTypeEnum` [R/W] property ImportOrExportType
- `Public Property Incoterms() As String` [R/W] Sets or returns the Internationally Accepted Commerce terms. Field name: Incoterms. Length: 3 characters.
- `Public Property IsIGSTAccount() As BoYesNoEnum` [R/W] property IsIGSTAccount
- `Public Property MainUsage() As Long` [R/W] property MainUsage
- `Public Property NetWeight() As Double` [R/W] Sets or returns the net weight. Field name: NetWeight.
- `Public Property NFRef() As String` [R/W] Sets or returns the NF reference. Field name: NfRef.
- `Public Property OriginalBillOfEntryDate() As Date` [R/W] property OriginalBillOfEntryDate
- `Public Property OriginalBillOfEntryNo() As String` [R/W] property OriginalBillOfEntryNo
- `Public Property PackDescription() As String` [R/W] Sets or returns the pack description. Field name: PackDesc.
- `Public Property PackQuantity() As Long` [R/W] Sets or returns the quantity of packs. Field name: QoP.
- `Public Property PortCode() As String` [R/W] property PortCode
- `Public Property ShipUnitNo() As Long` [R/W] Sets or returns the number of shipping unit. Field name: NoSU.
- `Public Property State() As String` [R/W] Sets or returns the state code. Field name: State. Length: 3 characters.
- `Public Property StateB() As String` [R/W] Sets or returns the Building of the bill-to address.
- `Public Property StateS() As String` [R/W] Sets or returns the State of the bill-to address.
- `Public Property StreetB() As String` [R/W] Sets or returns the Street of the bill-to address.
- `Public Property StreetS() As String` [R/W] Sets or returns the Street of the Ship-to address.
- `Public Property TaxId0() As String` [R/W] Sets or returns the CNPJ code (country-specific to Brazil). Field name: TaxId0. Length: 100 characters.
- `Public Property TaxId1() As String` [R/W] Sets or returns the I.E. (country-specific to Brazil). Field name: TaxId1. Length: 100 characters.
- `Public Property TaxId12() As String` [R/W] Tax ID 12. Field name: TaxId12. Length: 50 characters.
- `Public Property TaxId13() As String` [R/W] Deductee Ref. No. in India. Field name: TaxId13. Length: 100 characters.
- `Public Property TaxId14() As String` [R/W] ITR Filing. Field name: TaxId14. Length: 250 characters.
- `Public Property TaxId2() As String` [R/W] Sets or returns the I.E.S.T (country-specific to Brazil). Field name: TaxId2. Length: 100 characters.
- `Public Property TaxId3() As String` [R/W] Sets or returns the I.M. (country-specific to Brazil). Field name: TaxId3. Length: 100 characters.
- `Public Property TaxId4() As String` [R/W] Sets or returns the CPF code (country-specific to Brazil). Field name: TaxId4. Length: 100 characters.
- `Public Property TaxId5() As String` [R/W] Sets or returns the Foreigner ID (country-specific to Brazil). Field name: TaxId5. Length: 100 characters.
- `Public Property TaxId6() As String` [R/W] Sets or returns the Foreigner description (country-specific to Brazil). Field name: TaxId6. Length: 100 characters.
- `Public Property TaxId7() As String` [R/W] Sets or returns the INSS Inscription (country-specific to Brazil). Field name: TaxId7. Length: 100 characters.
- `Public Property TaxId8() As String` [R/W] Sets or returns the Suframa (country-specific to Brazil). Field name: TaxId8. Length: 100 characters.
- `Public Property TaxId9() As String` [R/W] Reserved. Field name: TaxId9. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Vehicle() As String` [R/W] Sets or returns the vehicle ID. Field name: Vehicle. Length: 10 characters.
- `Public Property VehicleState() As String` [R/W] Sets or returns the state of the vehicle ID. Field name: VidState. Length: 3 characters.
- `Public Property ZipCodeB() As String` [R/W] Sets or returns the Zip Code of the bill-to address.
- `Public Property ZipCodeS() As String` [R/W] Sets or returns the Zip Code part of the Ship-to address.
