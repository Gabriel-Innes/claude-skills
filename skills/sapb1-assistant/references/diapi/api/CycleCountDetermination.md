<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CycleCountDetermination (Object)

CycleCountDetermination Class

## Properties (3)
- `Public Property CycleBy() As CycleCountDeterminationCycleByEnum` [R/W] Specifies the warehouse sublevel or item group for cycle counting. Field name: CycleBy.
  - remarks: You may not update both the CycleBy Property and CycleCountDeterminationSetup of the same transaction. This means that when updating these two settings in one transaction, the CycleCountDeterminationSetup changes will (by default) be ignored and the CycleBy Property changes will take effect.
- `Public Property CycleCountDeterminationSetupCollection() As CycleCountDeterminationSetupCollection` [R] property CycleCountDeterminationSetupCollection
- `Public Property WarehouseCode() As String` [R/W] The code of a warehouse. Field name: WhsCode.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
