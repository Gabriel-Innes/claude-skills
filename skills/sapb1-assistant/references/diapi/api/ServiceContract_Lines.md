<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceContract_Lines (Object)

ServiceContract_Lines is a child object of the ServiceContracts object that represents the line entries of each service contract. This object is part of the Service module. Source table: CTR1.

**Remarks:** To display the form in the application: - Select Service --> Service Contract. - Select the Items tab.

## Properties (12)
- `Public Property Count() As Long` [R] Returns the total data rows in the table.
  - remarks: When you add a new item or item group, the value of this property is incremented automatically.
- `Public Property EndDate() As Date` [R/W] Sets or returns the end date of the service contract for a specified item group. Field name: EndDate.
  - remarks: SAP Business One automatically sets the service contract end date for the specified item group.
- `Public Property InternalSerialNum() As String` [R/W] Sets or returns the unique internal serial number of the item. Field name: InternalSN. Length: 32 characters.
  - remarks: In SAP Business One, if you set the value of ManufacturerSerialNum, the value of the internal serial number is set automatically, and vice versa.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property ItemGroup() As Long` [R/W] Sets or returns the code of the item group. Field name: ItemGroup. This is a foreign key to the ItemGroups object.
- `Public Property ItemGroupName() As String` [R] Returns the name of the ItemGroup. Field name: ItmGrpName. Length: 20 characters.
- `Public Property ItemName() As String` [R/W] Sets or returns the item name. Field name: ItemName. Length: 200 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number. Field name: Line.
- `Public Property ManufacturerSerialNum() As String` [R/W] Sets or returns the unique manufacturer serial number of the item. Field name: ManufSN. Length: 32 characters.
  - remarks: In SAP Business One, if you set the value of InternalSerialNum, the value of the manufacturer serial number is set automatically, and vice versa.
- `Public Property StartDate() As Date` [R/W] Sets or returns the start date of the service contract for a specified item group. Field name: StartDate.
  - remarks: SAP Business One automatically sets the service contract start date for the specified item group.
- `Public Property TerminationDate() As Date` [R/W] Sets or returns the termination date of the service contract. Field name: TermDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
