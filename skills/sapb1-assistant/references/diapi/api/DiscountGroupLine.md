<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DiscountGroupLine (Object)

DiscountGroupLine Class

## Properties (8)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Discount() As Double` [R/W] property Discount
- `Public Property DiscountType() As DiscountGroupDiscountTypeEnum` [R] property DiscountType
- `Public Property FreeQuantity() As Double` [R/W] property FreeQuantity
- `Public Property MaximumFreeQuantity() As Double` [R/W] property MaximumFreeQuantity
- `Public Property ObjectCode() As String` [R/W] property ObjectCode
- `Public Property ObjectType() As DiscountGroupBaseObjectEnum` [R/W] property ObjectType
- `Public Property PaidQuantity() As Double` [R/W] property PaidQuantity

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
