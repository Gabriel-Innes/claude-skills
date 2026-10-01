<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPVatExemptionsLine (Object)

BPVatExemptionsLine Class

## Properties (15)
- `Public Property AbsoluteEntry() As Long` [R] property AbsoluteEntry
- `Public Property ApplyAllItems() As BoYesNoEnum` [R/W] property ApplyAllItems
- `Public Property AuthoritiesName() As String` [R/W] property AuthoritiesName
- `Public Property ExemptionDocNum() As String` [R/W] property ExemptionDocNum
- `Public Property ExemptionType() As Long` [R/W] property ExemptionType
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property IssueTime() As Date` [R/W] property IssueTime
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property ItemDescription() As String` [R] property ItemDescription
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidTo() As Date` [R/W] property ValidTo
- `Public Property VATRate() As Double` [R/W] property VATRate
- `Public Property VisualOrder() As Long` [R] property VisualOrder

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
