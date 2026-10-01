<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Deposit (Object)

Represents the deposits for received checks, credit card vouchers, and cash. Source table: ODPS.

## Properties (49)
- `Public Property AbsEntry() As Long` [R] The internal key of a specific deposit. Field name: AbsEntry.
- `Public Property AllocationAccount() As String` [R/W] The Cash on Hand account from which the deposit is defined. Field name: AllocAcct. Length: 15 characters.
  - remarks: The account is defined in Administration --> Setup --> Financials --> G/L Account Determination --> Sales. If required, you can specify another account.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property Bank() As String` [R/W] The name of the bank in which the deposit was made. Field name: DpsBank. Length: 30 characters.
- `Public Property BankAccountNum() As String` [R/W] The bank account number of the deposit. Field name: DeposAcct. Length: 50 characters.
- `Public Property BankBranch() As String` [R/W] The branch of the bank in which the deposit was made. Field name: DeposBrnch. Length: 50 characters.
- `Public Property BankReference() As String` [R/W] The reference assigned to the deposit by the bank. Field name: Ref2. Length: 11 characters.
- `Public Property BOEs() As BOELines` [R] Returns the BOELines object which support bills of exchange deposit on line level.
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property CheckDepositType() As BoCheckDepositTypeEnum` [R/W] property CheckDepositType
- `Public Property Checks() As CheckLines` [R] Returns the CheckLines object which support checks deposit on line level.
- `Public Property Commission() As Double` [R/W] The amount of commission to be paid in credit card deposit type. Field name: Comission.
- `Public Property CommissionAccount() As String` [R/W] The account used for commission payment in credit card deposit type. Field name: ComissAct. Length: 15 characters.
- `Public Property CommissionCurrency() As String` [R/W] property CommissionCurrency
- `Public Property CommissionDate() As Date` [R/W] The due date for the commission entry in the transaction. Field name: ComissDate.
- `Public Property CommissionFC() As Double` [R] property CommissionFC
- `Public Property CommissionSC() As Double` [R] property CommissionSC
- `Public Property Credits() As CreditLines` [R] Returns the CreditLines object which support credit cards deposit on line level.
- `Public Property DepositAccount() As String` [R/W] The G/L account if you perform the deposit to a bank account. Field name: BanckAcct. Length: 15 characters.
- `Public Property DepositAccountType() As BoDepositAccountTypeEnum` [R/W] The type of the deposit account: bank account or business partner. Field name: IsCard.
- `Public Property DepositCurrency() As String` [R/W] The currency of the deposit. Field name: DeposCurr.
  - remarks: Once a currency is selected, only checks/credit card vouchers/cash of this currency may be deposited.
- `Public Property DepositDate() As Date` [R/W] The date of the deposit. Field name: DeposDate.
- `Public Property DepositNumber() As Long` [R] The deposit number according to the selected numbering series. Field name: DeposNum.
- `Public Property DepositorName() As String` [R/W] The name of the person who made the deposit. Field name: DpostorNam. Length: 30 characters.
- `Public Property DepositType() As BoDepositTypeEnum` [R/W] The type of the deposit. Field name: DeposType.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for the commission. Field name: OcrCode. Length: 8 characters.
  - remarks: If you define the distribution rule here, it appears in the Distr. Rule field for the corresponding journal entry row. If you leave this field empty, the default distribution rule for the commission G/L account appears in the Distr. Rule field for the corresponding journal entry row.
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocRate() As Double` [R/W] The payment rate. Field name: DocRate.
- `Public Property IncomeTaxAccount() As String` [R/W] property IncomeTaxAccount
- `Public Property IncomeTaxAmount() As Double` [R/W] property IncomeTaxAmount
- `Public Property IncomeTaxAmountFC() As Double` [R] property IncomeTaxAmountFC
- `Public Property IncomeTaxAmountSC() As Double` [R] property IncomeTaxAmountSC
- `Public Property JournalRemarks() As String` [R/W] The remarks relevant to the journal entry created by the deposit. Field name: Memo. Length: 250 characters.
- `Public Property Project() As String` [R/W] The project to which the commission is allocated. Field: Project. Length: 20 characters.
- `Public Property ReconcileAfterDeposit() As BoYesNoEnum` [R/W] Specifies whether to perform reconciliation of the amounts deposited automatically. Field name: ReconAfter.
  - remarks: Only for checks and credit cards.
- `Public Property Series() As Long` [R/W] The numbering series you want to use for the deposit number. Field name: Series.
- `Public Property TaxAccount() As String` [R/W] The tax account, if you need to pay tax for the commission charges in credit card deposit type. Field name: VatAct. Length: 15 characters.
- `Public Property TaxAmount() As Double` [R/W] The tax amount, if you need to pay tax for the commission charges in credit card deposit type. Field name: VatTotal.
- `Public Property TaxAmountFC() As Double` [R] property TaxAmountFC
- `Public Property TaxAmountSC() As Double` [R] property TaxAmountSC
- `Public Property TaxCode() As String` [R/W] The tax code, if you need to pay tax for the commission charges in credit card deposit type. Field name: CommisVat. Length: 8 characters.
  - remarks: Country-specific fields for Europe.
- `Public Property TotalFC() As Double` [R] The total amount of the deposit in foreign currency. Field name: FcTotal.
- `Public Property TotalLC() As Double` [R/W] The total amount of the deposit in local currency. Field name: LocTotal.
- `Public Property TotalSC() As Double` [R] The total amount of the deposit in system currency. Field name: SysTotal.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property VoucherAccount() As String` [R/W] The credit card vouchers to be deposited. The details are from the incoming payment documents relating to the displayed vouchers. Field name: CrdBankAct. Length: 15 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
