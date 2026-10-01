<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProductTrees_Lines (Object)

ProductTrees_Lines is a child object of the ProductTrees object and it represents the line entries of each product tree. This object is part of the Inventory and Production module. Source table: ITT1.

**Remarks:** Mandatory fields in SAP Business One: ItemCode. To display the form in the application: - Select Production --> Define Bill of Materials.

## Properties (26)
- `Public Property AdditionalQuantity() As Double` [R/W] property AdditionalQuantity
- `Public Property ChildNum() As Long` [R] property ChildNum
- `Public Property Comment() As String` [R/W] Sets or returns comments for the item in the product tree line. Field name: Comment. Length: 254 characters.
- `Public Property Count() As Long` [R] Returns the total item rows.
  - remarks: When you add an item to the product tree, the Count value is incremented automatically.
- `Public Property Currency() As String` [R/W] Sets or returns the bill of materials currency. Field name: Currency. Length: 3 characters. Sets or returns the price currency used in the document row. Field name: Currency. Length: 3 characters.
  - remarks: You must define the currency strings before using this property. One business transaction may include more than one currency. In multiple currencies transaction, first call the GetCurrencyRate method to unify the total amount in different currencies into one currency. The value for multiple currencies is ##.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property InventoryUOM() As String` [R] Returns the Unit of Measurement for the item in the product tree line (for example: box, case, piece). Field name: Uom. Length: 5 characters.
  - remarks: The origin of the value is the Items object.
- `Public Property IssueMethod() As BoIssueMethod` [R/W] Sets or returns a valid value of BoIssueMethod that determines Specifies the methods for issuing items from the inventory: - Backflash (automatic) - Manual. Field name: IssueMthd.
- `Public Property ItemCode() As String` [R/W] Sets or returns the component item code. Field name: Code. Length: 254 characters. This is a foreign key to the Items object. Sets or returns the item code in the inventory. The item code must be unique. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property ItemName() As String` [R/W] property ItemName
- `Public Property ItemType() As ProductionItemType` [R/W] property ItemType
- `Public Property LineText() As String` [R/W] property LineText
- `Public Property ParentItem() As String` [R/W] Sets or returns the code of the parent item (product tree). Field name: Father. Length: 20 characters. This is a foreign key to the ProductTrees object.
  - remarks: The origin is the ProductTrees object.
- `Public Property Price() As Double` [R/W] Sets or returns the item price before taxation. Field name: Price.
- `Public Property PriceList() As Long` [R/W] Sets or returns the price list key of the item. Field name: PriceList. This is a foreign key to the PriceLists object.
  - remarks: The origin of the value is the PriceLists Object (OPLN table).
- `Public Property Project() As String` [R/W] The project that relates to the bill of materials. Field: Project. Length: 20 characters.
- `Public Property Quantity() As Double` [R/W] Sets or returns the items quantity in the bill of material. Field name: Quantity.
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VisualOrder() As Long` [R] property VisualOrder
- `Public Property Warehouse() As String` [R/W] Sets or returns the Warehouse identification key. Field name: Warehouse. Length: 8 characters. This is a foreign key to the Warehouses object.
- `Public Property WipAccount() As String` [R/W] property WipAccount

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: You cannot delete a line if it is the only line in the ProductTrees object.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ProductTrees oProdTree;

    // Delete Product Tree
    if(oProdTree.GetByKey("ProdTree") == true)
    {
        oProdTree.Items.SetCurrentLine(1);
        oProdTree.Items.Delete();
        oProdTree.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
