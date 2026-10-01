<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# POSDailySummary (Object)

POSDailySummary Class

## Properties (11)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property COFINSTotal() As Double` [R/W] property COFINSTotal
- `Public Property CounterPosition() As Long` [R/W] property CounterPosition
- `Public Property Date() As Date` [R/W] property Date
- `Public Property EquipmentNo() As String` [R/W] property EquipmentNo
- `Public Property GrossSales() As Double` [R/W] property GrossSales
- `Public Property OperationCounter() As Long` [R/W] property OperationCounter
- `Public Property PISTotal() As Double` [R/W] property PISTotal
- `Public Property POSTotalizerCollection() As POSTotalizerCollection` [R] property POSTotalizerCollection
- `Public Property ResetCounterPosition() As Long` [R/W] property ResetCounterPosition
- `Public Property Total() As Double` [R/W] property Total

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
