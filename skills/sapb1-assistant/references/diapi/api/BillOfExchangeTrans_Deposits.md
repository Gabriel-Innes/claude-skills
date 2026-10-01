<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BillOfExchangeTrans_Deposits (Object)

BillOfExchangeTrans_Deposits is a child object of the BillOfExchangeTransaction object and represents the deposits information for incoming payments. Source table: ODPS.

**Remarks:** Mandatory fields is SAP Business One: BankAccount (bank code), BankCountry, and BankDepositAccount. To display the form in the application: - Select Banking --> Bill of Exchange. - Select one of the Bill of Exchange sub-menus Management or Fund. Set your criteria and then click OK. The ODPS table also relates to Banking --> Deposits --> Deposit --> Bill of Exchange tab.

## Properties (7)
- `Public Property BankAccount() As String` [R/W] Sets or returns the bank code of the house bank for deposits. Field name: BanckAcct. Mandatory field is SAP Business One. Length: 30 characters.
- `Public Property BankBranch() As String` [R/W] Sets or returns the branch number of the house bank for deposits. Field name: DeposBrnch. Length: 50 characters.
- `Public Property BankCountry() As String` [R/W] Sets or returns the country of the of the house bank for deposits. Field name: BankCountr. Mandatory field is SAP Business One. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property BankDepositAccount() As String` [R/W] Sets or returns the account number of the house bank for deposits. Field name: BanckAcct. Mandatory field is SAP Business One. Length: 50 characters.
- `Public Property DepositNorm() As String` [R/W] Sets or returns the file format for presentation as defined for the banks for each country. Field name: DepostNorm. Length: 8 characters.
  - remarks: The file format for presentation in each country is as follows: - Italy: ABI-specification for CBI formats. - Spain: CSB 58, CSB 19, and CSB 32. - Portugal: PS2. - France: AFB .
- `Public Property PostingType() As BoDepositPostingTypes` [R/W] Sets or returns a valid value of BoDepositPostingTypes type that specifies the posting type for the deposit transaction (at the due date or before the due date). Field name: FinncPriod.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
