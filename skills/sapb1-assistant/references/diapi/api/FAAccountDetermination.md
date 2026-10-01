<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FAAccountDetermination (Object)

Account determination enables the system to automatically determine the relevant general ledger accounts for a fixed asset when an asset transaction takes place. SAP Business One lets you define multiple account determination sets. For each asset, you can apply more than one set of G/L accounts, so that the asset value and transactions can be posted to more than one accounting area at the same time. Source table: OADT.

## Properties (21)
- `Public Property AccumulatedOrdinaryDepr() As String` [R/W] The account on the liability side for the accumulated value of ordinary, planned depreciation. This account is the offsetting account for ordinary, planned depreciation. Field name: OrdDprAcc. Length: 15 characters.
- `Public Property AccumulatedSpecialDepr() As String` [R/W] The account for the accumulated special depreciation of fixed assets. Field name: SpDprAcc. Length: 15 characters.
- `Public Property AccumulatedUnplannedDepr() As String` [R/W] The account for the accumulated unplanned depreciation of fixed assets. Field name: UnpDprAcc. Length: 15 characters.
- `Public Property AssetBalanceSheetAccount() As String` [R/W] The account for the acquisition and production costs of fixed assets. Field name: BalanceAct. Length: 15 characters.
- `Public Property ClearingAccountAcquisition() As String` [R/W] The clearing account for the acquisition and production costs of the fixed assets. Field name: ClrAcqAct. Length: 15 characters.
- `Public Property Code() As String` [R/W] The unique code for the set of G/L accounts you are defining. Field name: Code. Length: 15 characters.
- `Public Property Description() As String` [R/W] The description for the set of G/L accounts you are defining. Field name: Descr. Length: 100 characters.
- `Public Property LeavewithExpenseNBVGross() As String` [R/W] The expense account for recording the net book value of an asset during retirement. When an asset with the gross posting method retires with losses, the account records the net book value of the asset during retirement. Field name: ReNBVeAct. Length: 15 characters.
- `Public Property LeavewithRevenueNBVGross() As String` [R/W] The revenue account for recording the net book value of an asset during retirement. When an asset with the gross posting method retires with profits, the account records the net book value of the asset during retirement. Field name: ReNBVrAct. Length: 15 characters.
- `Public Property OrdinaryDepreciation() As String` [R/W] The expense account for the ordinary, planned, annual depreciation of fixed assets. Field name: OrdDprAct. Length: 15 characters.
- `Public Property RetirementwithExpenseNet() As String` [R/W] The account to which the net losses resulting from asset sales are posted. Field name: ReExpNAct. Length: 15 characters.
- `Public Property RetirementwithRevenueNet() As String` [R/W] The account to which the net profits gained from asset sales are posted. Field name: ReRevNAct. Length: 15 characters.
- `Public Property RevaluationAccount() As String` [R/W] Revaluation account for fixed assets. Field name: RevAct. Length: 15 characters.
- `Public Property RevaluationLossAcct() As String` [R/W] Revaluation loss account for fixed assets. Field name: RevLossAct. Length: 15 characters.
- `Public Property RevaluationReserveAccount() As String` [R/W] The account to which the increase in the asset's value, as a result of revaluation, is posted. Field name: RevResvAct. Length: 15 characters.
- `Public Property RevaluationReserveClearing() As String` [R/W] The clearing account to which the increase in the asset's value as a result of revaluation is posted temporarily when an asset is sold. Field name: RevResvClr. Length: 15 characters.
- `Public Property RevenueAccountforRetirement() As String` [R/W] The account for the revenue resulting from asset retirement. Field name: RevReAct. Length: 15 characters.
- `Public Property RevenueClearingAccount() As String` [R/W] The clearing account for the revenue resulting from asset sales. Field name: ClearAccRe. Length: 15 characters.
- `Public Property RevenuefromAssetSalesNet() As String` [R/W] The account for the net revenues from asset sales before tax. This account is the offsetting account for the revenue account from asset sales that is specified for sales from the customer account. The net book value and the profits or losses are posted to this account when a sale is made. Field name: SaRevNAct. Length: 15 characters.
- `Public Property SpecialDepreciation() As String` [R/W] The expense account for the special depreciation of fixed assets. Field name: SpDprAct. Length: 15 characters.
- `Public Property UnplannedDepreciation() As String` [R/W] The expense account for the unplanned annual depreciation of fixed assets. Field name: UnpDprAct. Length: 15 characters.

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
