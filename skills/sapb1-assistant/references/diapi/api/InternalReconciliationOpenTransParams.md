<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InternalReconciliationOpenTransParams (Object)

InternalReconciliationOpenTransParams Class

## Properties (7)
- `Public Property AccountNo() As String` [R/W] property AccountNo
- `Public Property CardOrAccount() As CardOrAccountEnum` [R/W] property CardOrAccount
- `Public Property DateType() As ReconSelectDateTypeEnum` [R/W] property DateType
- `Public Property FromDate() As Date` [R/W] property FromDate
- `Public Property InternalReconciliationBPs() As InternalReconciliationBPs` [R] property InternalReconciliationBPs
- `Public Property ReconDate() As Date` [R/W] property ReconDate
- `Public Property ToDate() As Date` [R/W] property ToDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
