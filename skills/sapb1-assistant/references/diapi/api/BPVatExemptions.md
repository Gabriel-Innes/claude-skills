<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPVatExemptions (Object)

BPVatExemptions Class

## Properties (4)
- `Public Property AbsoluteEntry() As Long` [R] property AbsoluteEntry
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property BPVatExemptionsLines() As BPVatExemptionsLines` [R] property BPVatExemptionsLines
- `Public Property Remarks() As String` [R/W] property Remarks

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
