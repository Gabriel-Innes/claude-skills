<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CashFlowLineItem (Object)

CashFlowLineItem Class

## Properties (6)
- `Public Property ActiveLineItem() As BoYesNoEnum` [R] property ActiveLineItem
- `Public Property Drawer() As Long` [R] property Drawer
- `Public Property Level() As Long` [R] property Level
- `Public Property LineItemID() As Long` [R] property LineItemID
- `Public Property LineItemName() As String` [R] property LineItemName
- `Public Property ParentArticle() As Long` [R] property ParentArticle

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
