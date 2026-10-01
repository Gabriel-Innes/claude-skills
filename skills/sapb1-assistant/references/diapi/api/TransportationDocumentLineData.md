<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TransportationDocumentLineData (Object)

TransportationDocumentLineData Class

## Properties (8)
- `Public Property DocLineNumber() As Long` [R/W] property DocLineNumber
- `Public Property DocNumber() As Long` [R/W] property DocNumber
- `Public Property DocOrderNum() As Long` [R/W] property DocOrderNum
- `Public Property DocType() As DocumentObjectTypeEnum` [R/W] property DocType
- `Public Property ItemCode() As String` [R] property ItemCode
- `Public Property LineId() As Long` [R] property LineID
- `Public Property TranspDocNumber() As Long` [R] property TranspDocNumber
- `Public Property TransportedQuantity() As Double` [R/W] property TransportedQuantity

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
