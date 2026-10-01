<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CycleCountDeterminationSetup (Object)

This object enables setting up cycle count determination.

## Properties (9)
- `Public Property Alert() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to activate alert. Field name: Alert.
- `Public Property ChangeExistingItems() As BoYesNoEnum` [R/W] Changes existing items for cycle count determination. Field name: ChangeExist.
- `Public Property CycleCode() As Long` [R/W] Sets or returns the cycle code. Field name: CycleCode.
- `Public Property DestinationUser() As Long` [R/W] Sets or returns the destination user. Field name: DestUser. This is a foreign key to the Users object.
- `Public Property Entry() As Long` [R/W] If the CycleBy Property specified is a warehouse sublevel, the Entry property will be a foreign key to the WarehouseSublevelCode object. If the CycleBy Property specified is an item group, the Entry property will be a foreign key to the ItemGroups object. Field name: Entry.
- `Public Property ExcludeItemsWithZeroQuantity() As BoYesNoEnum` [R/W] Excludes items of zero quantity. Field name: ExcldZrQty.
  - remarks: This property is valid only when the CycleBy Property specified is a warehouse sublevel.
- `Public Property NextCountingDate() As Date` [R] Sets or returns the date of the upcoming inventory cycle. Field name: NextDate.
  - remarks: This property is valid only when the CycleBy Property specified is a warehouse sublevel.
- `Public Property Time() As Date` [R] Sets or returns the time of the upcoming inventory cycle. Field name: Time.
  - remarks: This property is valid only when the CycleBy Property specified is a warehouse sublevel.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the code of the warehouse where the item is stored. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
