<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProductionOrders_Lines (Object)

The ProductionOrders_Lines is a child object of the ProductionOrders object. Each line represents a component (item) of the product. Source table: WOR1.

**Remarks:** To display the form in the application: - Select Production --> Production Orders.

## Properties (32)
- `Public Property AdditionalQuantity() As Double` [R/W] The value is copied from the Additional Qty field in the Bill of Materials window; however, you can change it manually in the production order. Field name: AdditQty.
  - remarks: Only components of the Manual issue method can have zero Base Qty and the Additional Quantity larger than zero. The additional quantity for by-products is always zero.
- `Public Property BaseQuantity() As Double` [R/W] Sets or returns the quantity of the items required for manufacturing a single product. The default value is retrieved from the Quantity property (ProductTrees object). Field name: BaseQty.
  - remarks: The Base Quantity value of a resource component cannot be less than zero.
- `Public Property BatchNumbers() As BatchNumbers` [R] property BatchNumbers
- `Public Property Count() As Long` [R] Returns the total number of records in the table. Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocumentAbsoluteEntry() As Long` [R] Returns the production order number (AbsoluteEntry).
- `Public Property EndDate() As Date` [R/W] The latest date by which a component needs to be used in the production process. Field: EndDate.
- `Public Property IssuedQuantity() As Double` [R] Sets or returns the total items quantity already issued for the production order. That is, BaseQuantity multiplied by PlannedQuantity (ProductionOrders object). Field name: IssuedQty.
- `Public Property ItemName() As String` [R/W] property ItemName
- `Public Property ItemNo() As String` [R/W] Sets or returns the item code in the inventory. Length: 20 characters. Field name: ItemCode. This is a foreign key to the Items object.
- `Public Property ItemType() As ProductionItemType` [R/W] The type of the production item. Field name: ItemType.
- `Public Property LineNumber() As Long` [R] Returns the current row number in the list. Field name: LineNum.
- `Public Property LineText() As String` [R/W] Add text in the line. Field name: LineText. Length: 16 characters.
  - remarks: The text is added automatically from the corresponding line in the Bill of Materials window associated with the parent item.
- `Public Property LocationCode() As Long` [R/W] The location for the items in this line of the production order. Field name: LocCode This is a foreign key to the WarehouseLocations object.
- `Public Property PlannedQuantity() As Double` [R/W] Sets or returns the total items quantity planned to be issued for the production order. For each component line, the value of this field is calculated according to the following formula: (Planned Quantity of the parent * Base Qty of the component) + Additional Qty of the component. Field name: PlannedQty.
- `Public Property ProductionOrderIssueType() As BoIssueMethod` [R/W] Determines the method for issuing the components of the product from the inventory, whether Manual or Backflash(automatic). Field name: IssueType.
  - remarks: Manual - The user issues individual components of a parent item manually. For example, serial or batch-controlled items must be issued manually. Backflash - The system issues the components of a parent item automatically to the production order according to the parent item completion status (ProductionOrderStatus).
- `Public Property Project() As String` [R/W] The project that relates to the components of the product. Field: Project. Length: 20 characters.
- `Public Property RequiredDays() As Double` [R] The number of days required for a specific Resource to complete the Planned Quantity of a particular route stage. This field will be automatically calculated for a production order that has at least one route stage, one resource line, and whose Routing Date Calculation field is either Start Date Forwards or End Date Backwards. Field: ReqDays.
- `Public Property ResourceAllocation() As ResourceAllocationEnum` [R/W] Determines how the resource allocation will occur, for a production order that has route stages. Field name: ResAlloc.
- `Public Property SerialNumbers() As SerialNumbers` [R] property SerialNumbers
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property StartDate() As Date` [R/W] The earliest date on which the component is needed in the production process. Field name: StartDate.
- `Public Property UoMCode() As String` [R] The unique code for the UoM. Field name: UomCode. Length: 20 characters.
- `Public Property UoMEntry() As Long` [R] The internal key of the UoM. Field name: UomEntry.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VisualOrder() As Long` [R] Returns the visual order number. The value for the first row is null, and from the second row the number starts from 1. Field name: VisOrder.
- `Public Property Warehouse() As String` [R/W] Sets or returns the warehouse identification key from which the items are issued. Field name: wareHouse. Length: 8 characters.
- `Public Property WipAccount() As String` [R/W] If the production order lines are populated with components from a BOM, the account defined in the WIP Account field of the BOM for the relevant component populates this field. If theWIP Account field for the relevant component is blank in the BOM, this account is blank, too. You can manually update the account in this field before the production order closure. The value of this field is then copied into the Account Code field of the issue for production. Field name: WipActCode.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: You cannot delete a line if it is the only line in the ProductionOrders object.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ProductionOrders oProdOrder;

    // Delete production order line
    if(oProdOrder.GetByKey(0) == true)
    {
        oProdOrder.Lines.SetCurrentLine(0);
        oProdOrder.Lines.Delete();
        oProdOrder.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
