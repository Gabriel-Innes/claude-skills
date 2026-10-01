<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MaterialRevaluation_lines (Object)

MaterialRevaluation_Lines is a child object of the MaterialRevaluation object representing the line entries of each transaction. Source table: MRV1.

## Properties (23)
- `Public Property ActualPrice() As Double` [R] Returns the current item price (item price before revaluation). Field name: RActPrice.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DebitCredit() As Double` [R/W] Sets or returns the amount of money to be recalculated on items.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocEntry() As Long` [R] Returns the document entry key that uniquely identifies the document. Field name: DocEntry.
- `Public Property FIFOLayers() As FIFOLayers` [R] The FIFO layers to be revalued. Relevant when the item's valuation method is FIFO.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. The item code must be unique. This is a foreign key to the Items object. Field name: ItemCode. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property ItemDescription() As String` [R] Sets or returns the item name/description. Field name: Dscription. Length: 100 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number in the list. Field name: LineNum.
- `Public Property OnHand() As Double` [R] Returns the number of available items in warehouse during the revaluation. Field name: ROnHand.
- `Public Property Price() As Double` [R/W] Sets or returns the item price before taxation. Field name: Price.
- `Public Property Project() As String` [R/W] The project to which the changed inventory value of the item is allocated. Field: Project. Length: 20 characters.
- `Public Property Quantity() As Double` [R/W] Sets or returns the number of items for recalculating their DebitCredit amount.
- `Public Property RevalAmountToStock() As Double` [R] Sets or returns the revaluation amount posted to the Stock Account. Field name: RToStock.
- `Public Property RevaluationDecrementAccount() As String` [R/W] Sets or returns the revaluation decrement account code. Field name: RDcrmAcct. Length: 15 characters.
- `Public Property RevaluationIncrementAccount() As String` [R/W] Sets or returns the revaluation increment account code. Field name: RIncmAcct. Length: 15 characters.
- `Public Property SNBLines() As SNBLines` [R] property SNBLines
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the warehouse code where the item is stored. Field name: WhsCode. Length: 8 characters. This is a foreign key to the Warehoses object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
