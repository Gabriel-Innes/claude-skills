<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WTDCode (Object)

WTDCode Class

## Properties (18)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property BaseAmountPrct() As Double` [R/W] property BaseAmountPrct
- `Public Property BaseType() As WithholdingTaxCodeBaseTypeEnum` [R/W] property BaseType
- `Public Property CalculateInAutomaticCM() As BoYesNoEnum` [R/W] property CalculateInAutomaticCM
- `Public Property Category() As WithholdingTaxCodeCategoryEnum` [R/W] property Category
- `Public Property FormulaId() As Long` [R/W] property FormulaID
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property MinAmount() As Double` [R/W] property MinAmount
- `Public Property OfficialCode() As String` [R/W] property OfficialCode
- `Public Property SlidingScaleProgressiveTax() As BoYesNoEnum` [R/W] property SlidingScaleProgressiveTax
- `Public Property Type() As Long` [R/W] property Type
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property WTaxCode() As String` [R/W] property WTaxCode
- `Public Property WTaxName() As String` [R/W] property WTaxName
- `Public Property WTDBPCollection() As WTDBPCollection` [R] property WTDBPCollection
- `Public Property WTDEffectiveDateCollection() As WTDEffectiveDateCollection` [R] property WTDEffectiveDateCollection
- `Public Property WTDFreightCollection() As WTDFreightCollection` [R] property WTDFreightCollection
- `Public Property WTDItemCollection() As WTDItemCollection` [R] property WTDItemCollection

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
