<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TransactionCodesService (Object)

TransactionCodesService Class

## Methods (8)
- `Public Function Add(ByVal pITransactionCode As TransactionCode) As TransactionCodeParams` Add
  - param `pITransactionCode`: 
- `Public Sub Delete(ByVal pITransactionCodeParams As TransactionCodeParams)` Delete
  - param `pITransactionCodeParams`: 
- `Public Function Get(ByVal pITransactionCodeParams As TransactionCodeParams) As TransactionCode` Get
  - param `pITransactionCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TransactionCodesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TransactionCodesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As TransactionCodeParamsCollection` GetList
- `Public Sub Update(ByVal pITransactionCode As TransactionCode)` Update
  - param `pITransactionCode`:
