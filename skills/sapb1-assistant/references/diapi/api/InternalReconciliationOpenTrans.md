<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InternalReconciliationOpenTrans (Object)

InternalReconciliationOpenTrans Class

## Properties (5)
- `Public Property BPLID() As Long` [R/W] property BPLId
- `Public Property CardOrAccount() As CardOrAccountEnum` [R/W] property CardOrAccount
- `Public Property ElectronicProtocols() As ElectronicProtocolCollection` [R] property ElectronicProtocols
- `Public Property InternalReconciliationOpenTransRows() As InternalReconciliationOpenTransRows` [R] property InternalReconciliationOpenTransRows
- `Public Property ReconDate() As Date` [R/W] property ReconDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
