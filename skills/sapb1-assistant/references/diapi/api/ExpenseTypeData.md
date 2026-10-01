<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExpenseTypeData (Object)

ExpenseTypeData Class

## Properties (5)
- `Public Property ExpenseAccount() As String` [R/W] property ExpenseAccount
- `Public Property ExpenseName() As String` [R/W] property ExpenseName
- `Public Property ExpenseType() As String` [R/W] property ExpenseType
- `Public Property PaidByCompany() As BoYesNoEnum` [R/W] property PaidByCompany
- `Public Property VatGroup() As String` [R/W] property VatGroup

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
