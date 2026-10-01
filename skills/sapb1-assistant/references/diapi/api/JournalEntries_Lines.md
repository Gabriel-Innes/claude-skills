<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# JournalEntries_Lines (Object)

Journal_Entries_Lines is a child object of the JournalEntries object, and represents the line entries of each transaction. This object enables you to add a journal transaction line. Source table: JDT1.

**Remarks:** Mandatory fields in SAP Business One: ShortName, and Credit or Debit, . To display the form in the application: - Select Financials --> Journal Entry (view in Expand Editing Mode).

## Properties (67)
- `Public Property AccountCode() As String` [R/W] Sets or returns the control account code, or G/L account code as defined in Chart of Accounts. Field name: Account. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property AdditionalReference() As String` [R/W] Sets or returns the additional reference number to the journal entry transaction line. Field name: Ref3Line. Length: 27 characters.
- `Public Property BaseSum() As Double` [R/W] Sets or returns the base amount including VAT. Field name: BaseSum.
  - remarks: Applicable for countries where using tax groups.
- `Public Property BlockReason() As Long` [R/W] Specify a reason for the payment block. Field name: PayBlckRef. Length: 50 characters.
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property CheckAbs() As Long` [R] Returns the Internal Check Number. Field name: CheckAbs.
- `Public Property Cig() As Long` [R/W] property Cig
- `Public Property ContraAccount() As String` [R/W] Sets or returns the offsetting account code to credit or debit opposed to the current account. Field name: ContraAct. Length: 15 characters.
- `Public Property ControlAccount() As String` [R/W] The control account for this journal entry. Field name: Account This is a foreign key to the ChartOfAccounts object.
- `Public Property CostElementCode() As String` [R] property CostElementCode
- `Public Property CostingCode() As String` [R/W] The distribution rule for dimension 1 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: ProfitCode This is a foreign key to the DistributionRule object.
- `Public Property CostingCode2() As String` [R/W] The distribution rule for dimension 2 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode2 This is a foreign key to the DistributionRule object.
- `Public Property CostingCode3() As String` [R/W] The distribution rule for dimension 3 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode3 This is a foreign key to the DistributionRule object.
- `Public Property CostingCode4() As String` [R/W] The distribution rule for dimension 4 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode4 This is a foreign key to the DistributionRule object.
- `Public Property CostingCode5() As String` [R/W] The distribution rule for dimension 5 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode5 This is a foreign key to the DistributionRule object.
- `Public Property Count() As Long` [R] Returns the total journal entries.
  - remarks: When you add a new journal entry, the value is increased automatically.
- `Public Property Credit() As Double` [R/W] Sets or returns the amount of credit in the current transaction. Mandatory property. Field name: Credit.
- `Public Property CreditSys() As Double` [R/W] Returns the amount of credit in system currency. Field name: SYSCred.
- `Public Property Cup() As Long` [R/W] property Cup
- `Public Property Debit() As Double` [R/W] Sets or returns the amount to debit the G/L account. Field name: Debit. Mandatory property.
- `Public Property DebitSys() As Double` [R/W] Returns the amount of debit in system currency. Field name: SYSDeb.
- `Public Property DocumentArray() As Long` [R] property DocumentArray
- `Public Property DocumentLine() As Long` [R] property DocumentLine
- `Public Property DueDate() As Date` [R/W] Sets or returns the value date of journal entry line. Field name: DueDate.
- `Public Property EqualizationTaxAmount() As Double` [R] Equalization tax amount. Field name: EquVatSum
  - remarks: For Spain only.
- `Public Property ExpensesClassificationCategory() As Long` [R/W] property ExpensesClassificationCategory
- `Public Property ExpensesClassificationType() As Long` [R/W] property ExpensesClassificationType
- `Public Property ExposedTransNumber() As Long` [R/W] property ExposedTransNumber
- `Public Property FCCredit() As Double` [R/W] Returns the amount of credit in foreign currency. Field name: FCCredit.
- `Public Property FCCurrency() As String` [R/W] Sets or returns the foreign currency used in this line. Field name: FCCurrency. Length: 3 characters.
- `Public Property FCDebit() As Double` [R/W] Returns the amount of debit in foreign currency. Field name: FCDebit.
- `Public Property FederalTaxID() As String` [R/W] property FederalTaxID
- `Public Property GrossValue() As Double` [R/W] Returns the total amount including VAT in the journal entry line. Field name: GrossValue.
  - remarks: Country-specific for Europe localization only (where VAT Per Line is used). Applicable only when Journal Entry documents use automatic VAT (AutoVat field in the OADM or ORCR tables is set to Yes). To display the OADM settings in the application, select Administration --> System Initialization --> Document Settings. In the Per Document tab, from the Document box, select Journal Entry. ORCR is not exposed through the DI API. To display the ORCR settings in the application, select Financials --> Recurring Postings.
- `Public Property IncomeClassificationCategory() As Long` [R/W] property IncomeClassificationCategory
- `Public Property IncomeClassificationType() As Long` [R/W] property IncomeClassificationType
- `Public Property Line_ID() As Long` [R] Returns the current line number. Field name: Line_ID.
- `Public Property LineMemo() As String` [R/W] Sets or returns the details of the current transaction line. Field name: LineMemo. Length: 50 characters.
- `Public Property LocationCode() As Long` [R/W] Sets or returns the location code in journal entries line. Applicable for cluster B. Field name: LocCode.
- `Public Property PaymentBlock() As BoYesNoEnum` [R/W] Indicates whether the document is blocked and excluded from the payment wizard run. Field name: PayBlckRef
- `Public Property PaymentOrdered() As BoYesNoEnum` [R] property PaymentOrdered
- `Public Property PrimaryFormItems() As CashFlowAssignments` [R] property PrimaryFormItems
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code related to the journal entry. Field name: Project, length: 8 characters. This is a foriegn key to Project Codes table, exposed via ProjectsService. In SAP Business One, you can relate business transactions to projects. This can help you to create cost/income analyzes reports based on projects.
  - remarks: Editing project code in the Journal Entry header does not affect the project code assigned to Journal Entry lines. To enforce the change on the lines, you must set JournalEntries_Lines.ProjectCode.
- `Public Property Reference1() As String` [R/W] Sets or returns the first reference code. Field name: Ref1. Length: 100 characters.
- `Public Property Reference2() As String` [R/W] Sets or returns the second reference code. Field name: Ref2. Length: 100 characters.
- `Public Property ReferenceDate1() As Date` [R/W] Not used. Field name: RefDate.
- `Public Property ReferenceDate2() As Date` [R/W] Not used. Field name: Ref2Date.
- `Public Property ShortName() As String` [R/W] Sets or returns the account name/description as defined in Chart of Accounts. Field name: ShortName. Length: 15 characters.
- `Public Property SystemBaseAmount() As Double` [R/W] Sets or returns the base amount (without VAT) in system currency. Relevant to tax a account only (an account that is related to a tax group or stamp tax) Field name: SYSBaseSum.
- `Public Property SystemEqualizationTaxAmount() As Double` [R] System equalization tax amount. Field name: EquVatSum
  - remarks: For Spain only.
- `Public Property SystemTotalTax() As Double` [R] Total system tax amount. Field name: SYSEquSum
  - remarks: For Spain only.
- `Public Property SystemVatAmount() As Double` [R/W] Sets or returns the VAT amount in system currency. Relevant to tax a account only (an account that is related to a tax group or stamp tax) field name: SYSVatSum
- `Public Property TaxCode() As String` [R/W] Sets or returns the tax code. This is a foreign key to SalesTaxCodes object. Country-specific for Canada, USA, Chile, and Mexico. Field name: TaxCode. Length: 8 characters.
  - remarks: TaxCode is applicable only when AutoVAT (JournalEntries object) is set to tYes.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TaxGroup() As String` [R/W] Sets or returns the tax group as defined in SAP Business One. Field name: VatGroup). Length: 8 characters. This is a foreign key to the VatGroups object.
- `Public Property TaxPostAccount() As BoTaxPostAccEnum` [R/W] Sets or returns a valid value that specifies the tax posting account type for the journal entry line. Country-specific for Canada, USA, Chile, and Mexico. Field name: TaxPostAcc.
  - remarks: TaxPostAccount is applicable only when AutoVAT (JournalEntries object) is set to tYes.
- `Public Property TotalTax() As Double` [R] Total tax amount. Field name: TotalVat
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatAmount() As Double` [R/W] Sets or returns the total tax amount payed. Field name: VatAmount.
  - remarks: SAP Business One calculates the tax according to the selected TaxGroup.
- `Public Property VatClassificationCategory() As Long` [R/W] property VATClassificationCategory
- `Public Property VatClassificationType() As Long` [R/W] property VATClassificationType
- `Public Property VatDate() As Date` [R/W] Sets or returns the date from which the tax rate for this VAT Group code applies. Field name: vatdate.
  - remarks: If the DocDate value (posting date) is later than the VatDate value,SAP Business One applies the latest tax rate, else it applies the tax rate defined for the period before the VatDate value. Relevant to sales and purchase documents only.
- `Public Property VATExemptionCause() As Long` [R/W] property VATExemptionCause
- `Public Property VatLine() As BoYesNoEnum` [R/W] Determines whether or not the transaction line refers to tax account (an account that is related to a tax group or stamp tax). Field name: VatLine.
- `Public Property VATRegNum() As String` [R] property VATRegNum
- `Public Property WTLiable() As BoYesNoEnum` [R/W] Indicates whether this journal entry line is liable for withholding tax. Field name: WTLiable
- `Public Property WTRow() As BoYesNoEnum` [R/W] Indicates whether this journal entry line represents withholding tax. Field name: WTLine

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
