<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReportFilter (Object)

TaxReportFilter is a data structure related to the TaxReportsService. Source table: OVTR.

## Properties (35)
- `Public Property AppendixOorPSelection() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not this Appendix is O or P selection. Field name: ApndxOOrP.
- `Public Property Cancellation() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not cancelation is required for For EU Sales Report. Field name: ApndxOOrP.
- `Public Property Code() As Long` [R] Returns the Abs Entry (numerator) of this tax report. Field name: AbsEntry.
- `Public Property DeclarationType() As TaxReportFilterDeclarationType` [R/W] Sets or returns a valid value that determines whether this declaration type is original, substitute or complementary. Field name: Declration.
- `Public Property DiplayCreditMemosInSeparateColumn() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to display credit memos in separate column. Field name: CreditMemo.
- `Public Property DocumentType() As TaxReportFilterApArDocumentType` [R/W] Sets or returns a valid value that determines whether or not this document is an A/P Document or an A/R Document. Field name: DocType.
- `Public Property ExcludeWT() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to exclude withholding tax for this report. Field name: ExcludeWT.
- `Public Property FilterType() As TaxReportFilterType` [R/W] Sets or returns a valid value that determines the Selection Criteria Type to be used with this report. Field name: Selection Criteria Type.
- `Public Property FirstPrintedNumber() As Long` [R/W] Sets or returns the first printed number in this report. Field name: FirstPrint.
- `Public Property FirstRegisterNumber() As Long` [R/W] Sets or returns the first register number in this report. Field name: FirstReg.
- `Public Property FromDate() As Date` [R/W] Sets or returns this report period start date. Field name: FromDate.
- `Public Property FromSeries() As Long` [R/W] Sets or returns this report first Series. Field name: FromSeries.
- `Public Property HideTaxWithoutTransaction() As BoYesNoEnum` [R/W] Determines whether or not to hide tax without Transaction. Field name: HideNTrans.
- `Public Property IncludeCustomers() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to include customers in this report. Field name: CustomerIn.
- `Public Property IncludeDocumentType() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include document type in report. Field name: DocTyp.
- `Public Property IncludeGLAccounts() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include GL Accounts in this report. Field name: AccountIn.
- `Public Property IncludeSeriesFilter() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include series filter in this report. Field name: SerieeIn.
- `Public Property IncludeVendors() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include vendors in this report . Field name: VendorIn.
- `Public Property Name() As String` [R/W] Sets or returns this report name. Field name: ReportName. Length: 50 characters.
- `Public Property OpeningAndClosingBalance() As BoYesNoEnum` [R/W] Sets or returns the opening and closing balance of this report. Field name: DispOBCB.
- `Public Property Period() As TaxReportFilterPeriod` [R/W] Sets or returns the tax report filter period of this report. Field name: Period.
- `Public Property Quarter() As Long` [R/W] Sets or returns the quarter number of this report . Field name: quarter.
- `Public Property QuarterOrDates() As TaxReportFilterQuarterOrDates` [R/W] Sets or returns a valid value that determines wether this report period is defined by quarters or by start / end dates. Field name: DateRBtn.
- `Public Property ReportLayout() As TaxReportFilterReportLayoutType` [R/W] Sets or returns a valid value that determines the report layout, register book, declaration or base layout. Field name: RptLayout.
- `Public Property RoundAmount() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to round this report amount. Field name: RoundSum.
- `Public Property ShowPaymentsWithDeferredTax() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not . Field name: DeferTaxIn.
- `Public Property TaxDate() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include tax date. Field name: TaxDate.
- `Public Property TaxReportAccounts() As TaxReportAccounts` [R] Returns the TaxReportAccounts object, a Data Collection of TaxReportAccount data structures.
- `Public Property TaxReportBusinessPartners() As TaxReportBusinessPartners` [R] Returns the TaxReportBusinessPartners object, a Data Collection of TaxReportBusinessPartner data structures.
- `Public Property TaxReportDocuments() As TaxReportDocuments` [R] Returns the TaxReportDocuments object, a Data Collection of TaxReportDocument data structures.
- `Public Property TaxReportGroups() As TaxReportGroups` [R] Returns the TaxReportGroups object, a Data Collection of TaxReportGroup data structures.
- `Public Property TaxReportSeriesCollection() As TaxReportSeriesCollection` [R] Returns the TaxReportSeriesCollection object, a Data Collection of TaxReportSeries data structures.
- `Public Property ToDate() As Date` [R/W] Sets or returns the end date of this report period. Field name: ToDate.
- `Public Property ToSeries() As Long` [R/W] Sets or returns the last Series of this report . Field name: ToSeries.
- `Public Property Year() As Long` [R/W] Sets or returns the year field of this document date. Field name: Year.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
