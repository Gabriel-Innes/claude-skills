<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PostingTemplatesLine (Object)

PostingTemplatesLine Class

## Properties (21)
- `Public Property AccountCode() As String` [R/W] property AccountCode
- `Public Property AccountName() As String` [R/W] property AccountName
- `Public Property ControlAccount() As String` [R/W] property ControlAccount
- `Public Property CostElementCode() As String` [R] property CostElementCode
- `Public Property CostingCode1() As String` [R/W] property CostingCode1
- `Public Property CostingCode2() As String` [R/W] property CostingCode2
- `Public Property CostingCode3() As String` [R/W] property CostingCode3
- `Public Property CostingCode4() As String` [R/W] property CostingCode4
- `Public Property CostingCode5() As String` [R/W] property CostingCode5
- `Public Property Credit() As Double` [R/W] property Credit
- `Public Property Debit() As Double` [R/W] property Debit
- `Public Property DistributionRule() As String` [R/W] property DistributionRule
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ProjectCode() As String` [R/W] property ProjectCode
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property TaxGroup() As String` [R/W] property TaxGroup
- `Public Property TaxPostingAccount() As BoTaxPostingAccountTypeEnum` [R/W] property TaxPostingAccount
- `Public Property TrtCode() As String` [R] property TrtCode
- `Public Property VatLine() As BoYesNoEnum` [R/W] property VatLine
- `Public Property WTaxLiable() As BoYesNoEnum` [R/W] property WTaxLiable
- `Public Property WTaxLine() As BoYesNoEnum` [R/W] property WTaxLine

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
