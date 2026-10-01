<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PaymentReasonCodeService (Object)

Source table: OPTR.

**Remarks:** For the Italy localization only. Navigation path 1: Administration → Setup → Financial → Tax → Withholding Tax, and go to the column Payment Reason Code. Navigation path 2: Business Partner Master Data → Accounting → Tax, select the checkbox Subject to Withholding Tax, choose the browser button next to the Specific WTax Amounts Setup field, and go to the column Payment Reason Code.

## Methods (7)
- `Public Function AddPaymentReasonCode(ByVal pIPaymentReasonCode As PaymentReasonCode) As PaymentReasonCodeParams` AddPaymentReasonCode
  - param `pIPaymentReasonCode`: 
- `Public Sub DeletePaymentReasonCode(ByVal pIPaymentReasonCodeParams As PaymentReasonCodeParams)` DeletePaymentReasonCode
  - param `pIPaymentReasonCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As PaymentReasonCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/PaymentReasonCodeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetPaymentReasonCode(ByVal pIPaymentReasonCodeParams As PaymentReasonCodeParams) As PaymentReasonCode` GetPaymentReasonCode
  - param `pIPaymentReasonCodeParams`: 
- `Public Function GetPaymentReasonCodeList() As PaymentReasonCodesParams` GetPaymentReasonCodeList
