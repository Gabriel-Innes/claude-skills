<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InternalReconciliationRow (Object)

InternalReconciliationRow Class

## Properties (9)
- `Public Property CashDiscount() As Double` [R] property CashDiscount
- `Public Property CreditOrDebit() As CreditOrDebitEnum` [R] property CreditOrDebit
- `Public Property LineSeq() As Long` [R] property LineSeq
- `Public Property ReconcileAmount() As Double` [R] property ReconcileAmount
- `Public Property ShortName() As String` [R] property ShortName
- `Public Property SrcObjAbs() As Long` [R] property SrcObjAbs
- `Public Property SrcObjTyp() As String` [R] property SrcObjTyp
- `Public Property TransId() As Long` [R] property TransId
- `Public Property TransRowId() As Long` [R] property TransRowId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
