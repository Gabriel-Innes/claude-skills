<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MaterialRevaluationSNBParams (Object)

MaterialRevaluationSNBParams Class

## Properties (8)
- `Public Property AdmissionDate() As Date` [R] property AdmissionDate
- `Public Property DebitCredit() As Double` [R/W] property DebitCredit
- `Public Property ExpirationDate() As Date` [R] property ExpirationDate
- `Public Property LotNumber() As String` [R] property LotNumber
- `Public Property ManufactureNumber() As String` [R] property ManufactureNumber
- `Public Property NewCost() As Double` [R/W] property NewCost
- `Public Property SnbAbsEntry() As Long` [R/W] property SnbAbsEntry
- `Public Property SystemNumber() As Long` [R] property SystemNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
