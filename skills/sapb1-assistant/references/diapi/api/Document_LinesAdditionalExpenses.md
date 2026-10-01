<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Document_LinesAdditionalExpenses (Object)

Document_LinesAdditionalExpenses is a child object of Document_Lines and represents the line entries of the additional expenses document in the Marketing Documents module. The source table for each document is according to the document type as follows: INV2, RIN2, DLN2, RDN2, RDR2, QUT2, PCH2, RPC2, PDN2, RPD2, POR2, and DRF2.

**Remarks:** Mandatory field in SAP Business One: ExpenseCode and of Name of AdditionalExpenses object. You can add up to three (3) additional expenses in a row of a document and SAP Business One assigns a number (GroupCode) for each of the additional expenses. If no additional expense is defined in SAP Business One, the GetByKey method will retrieve null.

## Properties (48)
- `Public Property AquisitionTax() As BoYesNoEnum` [R] Specifies whether or not the additional expense is subject to acquisition tax. Relevant to input tax groups (A/P) only. Field name: IsAcquistn.
  - remarks: The acquisition tax is a procedure used when you record goods purchased from EU countries. In this case, tax is not calculated in the document but an appropriate amount is recorded in the journal entry and affects the tax report.
- `Public Property BaseGroup() As Long` [R/W] Sets or returns the number of the additional expense to draw from the base document (per line). Field name: BaseGroup.
  - remarks: Valid values are: -1 - None 0 - Additional expense No. 1 1 - Additional expense No. 2 2 - Additional expense No. 3
- `Public Property Count() As Long` [R] Returns total rows in the additional expenses table.
- `Public Property CUSplit() As BoYesNoEnum` [R/W] If this flag is set to true, the amounts that are not subject to withholding tax and are not supplier income amounts are distinguished and split in a standalone report page.
  - remarks: Italy only, for the withholding tax single certification (Certificazione Unica).
- `Public Property DeductibleTaxSum() As Double` [R] Internal use only. Field name: DedVatSum.
- `Public Property DeductibleTaxSumFC() As Double` [R] Internal use only. Field name: DedVatSumF.
- `Public Property DeductibleTaxSumSys() As Double` [R] Internal use only. Field name: DedVatSumS.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property EBooksDetails() As EBooks_Doc_Details` [R] property EBooksDetails
- `Public Property EqualizationTaxFC() As Double` [R] Returns the equalization tax amount, in foreign currency, calculated for the additional expense. Field name: EquVatSumF.
- `Public Property EqualizationTaxPercent() As Double` [R] Returns the equalization tax percent for the additional expense calculations. Field name: EquVatPer.
- `Public Property EqualizationTaxSum() As Double` [R] Returns the equalization tax amount, calculated for the additional expense. Field name: EquVatSum.
- `Public Property EqualizationTaxSys() As Double` [R] Returns the equalization tax amount, calculated for the additional expense in system currency. Field name: EquVatSumS.
- `Public Property ExpenseCode() As Long` [R/W] Sets or returns the freight code . Field name: ExpnsCode. This is a foreign key to the AdditionalExpenses object. Sets or returns the code of the additional expense as defined by SAP Business One. Field name: ExpnsCode. This is a foreign key to the AdditionalExpenses object.
  - remarks: Mandatory field in SAP Business One.
- `Public Property ExternalCalcTaxAmount() As Double` [R/W] property ExternalCalcTaxAmount
- `Public Property ExternalCalcTaxAmountFC() As Double` [R] property ExternalCalcTaxAmountFC
- `Public Property ExternalCalcTaxAmountSC() As Double` [R] property ExternalCalcTaxAmountSC
- `Public Property ExternalCalcTaxRate() As Double` [R/W] property ExternalCalcTaxRate
- `Public Property GroupCode() As Long` [R/W] Returns the number of the additional expense in the row of the document (0, 1, or 2). Field name: GroupNum.
- `Public Property LineNumber() As Long` [R/W] Sets or returns the row number in the list in the parent document (such as INV1 table). Field name: LineNum.
- `Public Property LineTotal() As Double` [R/W] Sets or returns the total amount (in local currency) of the additional expense. Field name: LineTotal.
- `Public Property LineTotalFC() As Double` [R] Returns the total amount of the additional expense in foreign currency. Field name: TotalFrgn.
- `Public Property LineTotalSys() As Double` [R] Returns the total amount of the additional expense in system currency. Field name: TotalSumSy).
- `Public Property PaidToDate() As Double` [R] Returns the paid amount of the additional expense in local currency. Field name: PaidToDate. Not supported in DI API version 6.5.
- `Public Property PaidToDateFC() As Double` [R] Returns the total amount of the additional expense in foreign currency. Field name: PaidFC.
- `Public Property PaidToDateSys() As Double` [R] Returns the paid amount of the additional expense in system currency. Field name: PaidSys). Not supported in DI API version 6.5.
- `Public Property Project() As String` [R/W] The project that relates to the freight. Field: Project. Length: 20 characters.
- `Public Property TaxCode() As String` [R/W] Sets or returns the sales Tax Code Id. Field name: TaxCode. Length: 8 characters. This is a foreign key to the SalesTaxCodes Object.
- `Public Property TaxJurisdictions() As TaxJurisdictions` [R] Returns the TaxJurisdictions object.
- `Public Property TaxLiable() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the additional expense is VAT liable. Field name: TaxStatus.
- `Public Property TaxPaid() As Double` [R] Not used. Field name: PaidToDate.
- `Public Property TaxPaidFC() As Double` [R] Not used. Field name: PaidFC.
- `Public Property TaxPaidSys() As Double` [R] Not used. Field name: PaidSys.
- `Public Property TaxPercent() As Double` [R] Returns the tax percentage for the additional expense. Field name: VatPrcnt.
- `Public Property TaxSum() As Double` [R/W] The tax amount, in local currency, calculated for the additional expense. You can manually adjust the tax amount according to the business need. Field name: VatSum.
- `Public Property TaxSumFC() As Double` [R] Returns the tax amount, in foreign currency, calculated for the additional expense. Field name: VatSumFrgn.
- `Public Property TaxSumSys() As Double` [R] Returns the total tax amount, in system currency, calculated for the additional expense. Field name: VatSumSy.
- `Public Property TaxTotalSum() As Double` [R] Returns the total tax amount (TaxSum + EqualizationTaxSum) in local currency. Field name: EquVatSum.
- `Public Property TaxTotalSumFC() As Double` [R] Returns the total tax amount (TaxSumFC + EqualizationTaxFC) in foreign currency. Field name: EquVatSumF.
- `Public Property TaxTotalSumSys() As Double` [R] Returns the total tax amount (TaxSumSys + EqualizationTaxSys) in system currency. Field name: EquVatSumS.
- `Public Property TaxType() As BoAdEpnsTaxTypes` [R/W] Returns a valid value of BoAdEpnsTaxTypes type that specifies tax type for the additional expense. Field name: TaxType.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatGroup() As String` [R/W] Sets or returns the VAT group for the additional expense. Field name: VatGroup. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: Country-specific property for EU.
- `Public Property WTLiable() As BoYesNoEnum` [R/W] Returns a valid value of BoYesNoEnum type that specifies whether or not the additional expense is subject to Withholding tax. Field name: TaxStatus.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
