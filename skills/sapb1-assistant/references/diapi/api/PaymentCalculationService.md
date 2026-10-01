<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PaymentCalculationService (Object)

PaymentCalculationService Class

## Methods (4)
- `Public Function GetDataInterface(ByVal enumMSDI As PaymentCalculationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/PaymentCalculationServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetPaymentAmount(ByVal pIPaymentBPCode As PaymentBPCode, ByVal pIPaymentInvoiceEntries As PaymentInvoiceEntries) As PaymentAmountParamsCollection` GetPaymentAmount
  - param `pIPaymentBPCode`: 
  - param `pIPaymentInvoiceEntries`:
