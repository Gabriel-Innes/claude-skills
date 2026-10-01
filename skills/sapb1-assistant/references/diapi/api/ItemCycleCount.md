<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ItemCycleCount (Object)

ItemCycleCount object hold the information when an item will go through cycle counting. Each Item has a few Warehouses and each Warehouse has one ItemCycleCount. Source table: ITW1

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim oItem As Items

  Dim oWhareHouse As ItemWarehouseInfo

  oItem = oCompany.GetBusinessObject(BoObjectTypes.oItems)

  'get item

  oItem.GetByKey("X0003")

  'get warehouse

  oWhareHouse = oItem.WhsInfo

  'set an existind cycle count (e.g CycleCode=1 : CycleName:"Weekly on Tuesday" ,OCYC table)

  oWhareHouse.ItemCycleCount.CycleCode = 1

  'set alert

  oWhareHouse.ItemCycleCount.Alert = BoYesNoEnum.tYES

  'set user

  oWhareHouse.ItemCycleCount.DestinationUser = 1

  'update item with new Cycle Count

  oItem.Update()
  ```

## Properties (8)
- `Public Property Alert() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to activate alert. Field name: Alert.
- `Public Property AlertTime() As Date` [R/W] Sets or returns the Alert Time. Field name: Time.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
- `Public Property CycleCode() As Long` [R/W] Sets or returns the Cycle Code. Field name: CycleCode. This is a foreign key to the OCYC object.
- `Public Property DestinationUser() As Long` [R/W] Sets or returns the alert destination user. Field name: DestUser. This is a foreign key to the Users object.
- `Public Property NextCountingDate() As Date` [R/W] Returns the next counting date for this item. Field name: NextDate.
- `Public Property UserFields() As UserFields` [R] Returns the user signature. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property WarehouseCode() As String` [R/W] Returns the warehouse code. Field name: WhsCode. This is a foreign key to the Warehouses object.
