<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InternalReconciliation (Object)

InternalReconciliation Class

## Properties (8)
- `Public Property CancelAbs() As Long` [R] property CancelAbs
- `Public Property CardOrAccount() As CardOrAccountEnum` [R] property CardOrAccount
- `Public Property ElectronicProtocols() As ElectronicProtocolCollection` [R] property ElectronicProtocols
- `Public Property InternalReconciliationRows() As InternalReconciliationRows` [R] property InternalReconciliationRows
- `Public Property ReconDate() As Date` [R] property ReconDate
- `Public Property ReconNum() As Long` [R] property ReconNum
- `Public Property ReconType() As ReconTypeEnum` [R] property ReconType
- `Public Property Total() As Double` [R] property Total

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
