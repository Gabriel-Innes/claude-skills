<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InternalReconciliationsService (Object)

InternalReconciliationsService Class

## Methods (9)
- `Public Function Add(ByVal pIInternalReconciliationOpenTrans As InternalReconciliationOpenTrans) As InternalReconciliationParams` Add
  - param `pIInternalReconciliationOpenTrans`: 
- `Public Sub Cancel(ByVal pIInternalReconciliationParams As InternalReconciliationParams)` Cancel
  - param `pIInternalReconciliationParams`: 
- `Public Function Get(ByVal pIInternalReconciliationParams As InternalReconciliationParams) As InternalReconciliation` Get
  - param `pIInternalReconciliationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As InternalReconciliationsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/InternalReconciliationsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetOpenTransactions(ByVal pInternalReconciliationOpenTransParams As InternalReconciliationOpenTransParams) As InternalReconciliationOpenTrans` GetOpenTransactions
  - param `pInternalReconciliationOpenTransParams`: 
- `Public Sub RequestApproveCancellation(ByVal pIInternalReconciliationParams As InternalReconciliationParams)` RequestApproveCancellation
  - param `pIInternalReconciliationParams`: 
- `Public Sub Update(ByVal pIInternalReconciliation As InternalReconciliation)` Update
  - param `pIInternalReconciliation`:
