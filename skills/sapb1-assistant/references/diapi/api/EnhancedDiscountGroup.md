<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EnhancedDiscountGroup (Object)

EnhancedDiscountGroup Class

## Properties (8)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property DiscountGroupLineCollection() As DiscountGroupLineCollection` [R] property DiscountGroupLineCollection
- `Public Property DiscountRelations() As DiscountGroupRelationsEnum` [R/W] property DiscountRelations
- `Public Property ObjectCode() As String` [R/W] property ObjectCode
- `Public Property Type() As DiscountGroupTypeEnum` [R/W] property Type
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidTo() As Date` [R/W] property ValidTo

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
