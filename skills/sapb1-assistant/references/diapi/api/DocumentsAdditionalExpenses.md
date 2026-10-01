<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DocumentsAdditionalExpenses (Object)

DocumentsAdditionalExpenses is a child object of Documents object and represents the documents of additional expenses in the Marketing Documents module. The source table for each document is according to the document type as follows: INV3, RIN3, DLN3, RDN3, RDR3, QUT3, PCH3, RPC3, PDN3, RPD3, POR3, and DRF3.

**Remarks:** Mandatory fields in SAP Business One: ExpenseCode and of Name of AdditionalExpenses object. For each type of additional expense you can add one row that summarizes all expenses of that type. To display the form in the application, first define expenses in documents as follows: - Select Administration --> System Initialization --> Document Settings. - In the General tab, select Manage Expenses In Documents. - Click Define Expenses. Then, - For INV3 table, select Sales - A/R --> A/R Invoice. Click Add. Expenses. - For RIN3 table, select Sales - A/R --> A/R Credit Memo. Click Add. Expenses. - For DLN3 table, select Sales - A/R --> Delivery. Click Add. Expenses. - For RDN3 table, select Sales - A/R --> Returns. Click Add. Expenses. - For RDR3 table, select Sales - A/R --> Order. Click Add. Expenses. - For QUT3 table, select Sales - A/R --> Quotation. Click Add. Expenses. - For PCH3 table, select Purchasing - A/P --> A/P Invoice. Click Add. Expenses. - For RPC3 table, select Purchasing - A/P --> A/P Credit Memo. Click Add. Expenses. - For PDN3 table, select Purchasing - A/P --> Goods Receipt PO. Click Add. Expenses. - For RPD3 table, select Purchasing - A/P --> Goods Returns. Click Add. Expenses. - For POR3 table, select Purchasing - A/P --> A/R Invoice. Click Add. Expenses. - For DRF3 table, select Sales - A/R (or Purchasing - A/P) --> Document Draft. Set your selection criteria, and click OK. Click Add. Expenses.

## Properties (60)
- `Public Property AquisitionTax() As BoYesNoEnum` [R] Specifies whether or not the additional expense is subject to acquisition tax. Relevant to input tax groups (A/P) only. Field name: IsAcquistn.
  - remarks: The acquisition tax is a procedure used when you record goods purchased from EU countries. In this case, tax is not calculated in the document but an appropriate amount is recorded in the journal entry and affects the tax report.
- `Public Property BaseDocEntry() As Long` [R/W] Sets or returns the source document ID. Field name: DocEntry.
  - remarks: Use the BaseDocEntry, BaseDocType, and BaseDocLine properties to extract data from one document to another. For example, to extract data from a Quotation to an Order.
- `Public Property BaseDocLine() As Long` [R/W] Sets or returns the line number of the source document. Field name: BaseLnNum.
  - remarks: Use the BaseDocLine, BaseDocEntry, and BaseDocType properties to extract data from one document to another. For example, to extract data from a Quotation to an Order.
- `Public Property BaseDocType() As Long` [R/W] Sets or returns the source document type. Field name: BaseType.
  - remarks: Use the BaseDocType, BaseDocEntry, and BaseDocLine properties to extract data from one document to another. For example, to extract data from a Quotation to an Order. To view the document type numbers, see BoAPARDocumentTypes.
- `Public Property BaseDocumentReference() As Long` [R] Returns this line number. Field name: LineNum.
- `Public Property Count() As Long` [R] Returns total rows in the additional expenses table.
- `Public Property CUSplit() As BoYesNoEnum` [R/W] If this flag is set to true, the amounts that are not subject to withholding tax and are not supplier income amounts are distinguished and split in a standalone report page.
  - remarks: Italy only, for the withholding tax single certification (Certificazione Unica).
- `Public Property DeductibleTaxSum() As Double` [R/W] Internal use only. Field name: DedVatSum.
- `Public Property DeductibleTaxSumFC() As Double` [R] Internal use only. Field name: DedVatSumF.
- `Public Property DeductibleTaxSumSys() As Double` [R] Internal use only. Field name: DedVatSumS.
- `Public Property DistributionMethod() As BoAdEpnsDistribMethods` [R/W] Sets or returns a valid value of BoAdEpnsDistribMethods type that specifies the distribution method of the additional expenses in documents. Field name: DistrbMthd.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property EBooksDetails() As EBooks_Doc_Details` [R] property EBooksDetails
- `Public Property EqualizationTaxFC() As Double` [R] Returns the equalization tax amount, in foreign currency, calculated for the additional expense. Field name: EquVatSumF.
- `Public Property EqualizationTaxPercent() As Double` [R] Returns the equalization tax percentage for the additional expense. Field name: EquVatPer.
- `Public Property EqualizationTaxSum() As Double` [R] Returns the equalization tax amount, in local currency, calculated for the additional expense. Field name: EquVatSum.
- `Public Property EqualizationTaxSys() As Double` [R] Returns the equalization tax amount, in system currency, calculated for the additional expense. Field name: EquVatSumS.
- `Public Property ExpenseCode() As Long` [R/W] Sets or returns the code of the additional expense as defined by SAP Business One. Field name: ExpnsCode. This is a foreign key to the AdditionalExpenses object.
  - remarks: Mandatory field in SAP Business One.
- `Public Property ExternalCalcTaxAmount() As Double` [R/W] property ExternalCalcTaxAmount
- `Public Property ExternalCalcTaxAmountFC() As Double` [R] property ExternalCalcTaxAmountFC
- `Public Property ExternalCalcTaxAmountSC() As Double` [R] property ExternalCalcTaxAmountSC
- `Public Property ExternalCalcTaxRate() As Double` [R/W] property ExternalCalcTaxRate
- `Public Property LastPurchasePrice() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not this is the Last Purchase Price. Field name: LstPchPrce.
- `Public Property LineGross() As Double` [R/W] property LineGross
- `Public Property LineGrossFC() As Double` [R] property LineGrossFC
- `Public Property LineGrossSys() As Double` [R] property LineGrossSys
- `Public Property LineNum() As Long` [R] Returns this document line number. Field name: LineNum.
- `Public Property LineTotal() As Double` [R/W] Sets or returns the total amount (in local currency) of the additional expense. Field name: LineTotal.
- `Public Property LineTotalFC() As Double` [R] Returns the total amount (in foreign currency) of the additional expense. Field name: TotalFrgn.
- `Public Property LineTotalSys() As Double` [R] Returns the total amount (in system currency) of the additional expense. Field name: TotalSumSy.
- `Public Property PaidToDate() As Double` [R] Returns the paid amount (in local currency) of the additional expense. Field name: PaidToDate. Not supported in DI API version 6.5.
- `Public Property PaidToDateFC() As Double` [R] Returns the paid amount (in foreign currency) of the additional expense. Field name: PaidFC. Not supported in DI API version 6.5.
- `Public Property PaidToDateSys() As Double` [R] Returns the paid amount (in system currency) of the additional expense. Field name: PaidSys. Not supported in DI API version 6.5.
- `Public Property Project() As String` [R/W] The project that relates to the freight. Field: Project. Length: 20 characters.
- `Public Property Remarks() As String` [R/W] Sets or returns comments regarding the additional expense. Field name: Comments. Length: 100 characters.
- `Public Property Status() As BoStatus` [R] Returns a valid value that determines this document Status, (open or Close). Field name: Status.
- `Public Property Stock() As BoYesNoEnum` [R/W] Sets or returns a valid value that Determines whether or not a Stock exists. Field name: Stock.
- `Public Property TargetAbsEntry() As Long` [R] Returns the Target Absolute Entry of this document. Field name: TrgAbsEnt.
- `Public Property TargetType() As Long` [R] Returns the Target Type for this document. Field name: TrgType.
- `Public Property TaxCode() As String` [R/W] Sets or returns the sales tax code for the item specified in the row. Field name: TaxCode. Length: 8 characters. This is a foreign key to the SalesTaxCodes object. Sets or returns the sales tax code for the item specified in the row. Field name: TaxCode. Length: 8 characters. This is a foreign key to the SalesTaxCodes object.
  - remarks: Country-specific property for USA. The tax code represents the sales tax related to specific locations where the business transaction occurs. Tax codes are defined in SAP Business One. Country-specific property for USA. The tax code represents the sales tax related to specific locations where the business transaction occurs. Tax codes are defined in SAP Business One.
- `Public Property TaxJurisdictions() As TaxJurisdictions` [R] Returns the TaxJurisdictions object.
- `Public Property TaxLiable() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the additional expense is VAT liable. Field name: TaxStatus.
- `Public Property TaxPaid() As Double` [R] Not used. Field name: LineVat.
- `Public Property TaxPaidFC() As Double` [R] Not used. Field name: LineVatF.
- `Public Property TaxPaidSys() As Double` [R] Not used. Field name: LineVatS.
- `Public Property TaxPercent() As Double` [R] Returns the tax percentage for the additional expense. Field name: VatPrcnt.
- `Public Property TaxSum() As Double` [R/W] The tax amount, in local currency, calculated for the additional expense. You can manually adjust the tax amount according to the business need. Field name: VatSum.
- `Public Property TaxSumFC() As Double` [R] Returns the tax amount, in foreign currency, calculated for the additional expense. Field name: VatSumFrgn.
- `Public Property TaxSumSys() As Double` [R] Returns the total tax amount, in system currency, calculated for the additional expense. Field name: VatSumSy.
- `Public Property TaxTotalSum() As Double` [R] Returns the total tax amount (TaxSum + EqualizationTaxSum) in local currency. Field name: EquVatSum.
- `Public Property TaxTotalSumFC() As Double` [R] Returns the total tax amount (TaxSumFC + EqualizationTaxFC) in foreign currency. Field name: EquVatSumF.
- `Public Property TaxTotalSumSys() As Double` [R] Returns the total tax amount ( TaxSumSys + EqualizationTaxSys) in system currency. Field name: EquVatSumS.
- `Public Property TaxType() As BoAdEpnsTaxTypes` [R] Returns a valid value of BoAdEpnsTaxTypes type that specifies tax type for the additional expense. Field name: TaxType.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatGroup() As String` [R/W] Sets or returns the VAT group for the additional expense. Field name: VatGroup. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: Country-specific property for EU.
- `Public Property WTLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not this document is subject to Withholding Tax. Field name: TaxStatus.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number. Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
