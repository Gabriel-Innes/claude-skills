<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CycleCountDeterminationParams (Object)

CycleCountDeterminationParams Class

## Properties (2)
- `Public Property CycleBy() As Long` [R] Specifies the warehouse sublevel or item group for cycle counting. Field name: CycleBy.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the warehouse code where the item is stored. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
