<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EDFProtocolParameter (Object)

EDFProtocolParameter Class

## Properties (6)
- `Public Property BranchID() As Long` [R] property BranchID
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R] property Code
- `Public Property ParameterID() As Long` [R] property ParameterID
- `Public Property ParamName() As String` [R] property ParamName
- `Public Property ParamParameters() As String` [R] property ParamParameters
- `Public Property ParamValue() As String` [R] property ParamValue

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
