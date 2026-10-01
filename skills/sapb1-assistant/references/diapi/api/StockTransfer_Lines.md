<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# StockTransfer_Lines (Object)

StockTransfer_Lines is a child object of the StockTransfer object that represents the line entries of each stock transfer. Each line contains detailed information about the way items are transferred from one warehouse to the other. Source table: WTR1.

**Remarks:** Mandatory fields in SAP Business One: ItemCode and WarehouseCode. To display the form in the application: - Select Inventory --> Inventory Transactions --> Inventory Transfer.

## Properties (42)
- `Public Property BaseEntry() As Long` [R/W] Sets or returns the source Document ID. Field name: BaseEntry.
  - remarks: Use the BaseEntry, BaseLine, and BaseType properties to extract data from one document to another. For example, to extract data from a Quotation to an Order. To receive items from production or to issue items for production, you must specify the production order number (DocumentNumber) in the BaseEntry.
- `Public Property BaseLine() As Long` [R/W] Sets or returns the line number in the source document. Field name: BaseLine.
  - remarks: Use the BaseLine, BaseEntry, and BaseType properties to extract data from one document to another. For example, to extract data from a Quotation to an Order.
- `Public Property BaseType() As InvBaseDocTypeEnum` [R/W] Sets or returns a valid value of InvBaseDocTypeEnum that determines the document type. Field name: BaseType.
- `Public Property BatchNumbers() As BatchNumbers` [R] Returns the BatchNumbers child object.
- `Public Property BinAllocations() As StockTransferLinesBinAllocations` [R] The bin allocation of items or serial items or batch items.
- `Public Property CCDNumbers() As CCDNumbers` [R] property CCDNumbers
- `Public Property Count() As Long` [R] Returns the total rows in the table.
  - remarks: When you add a data row, the value of this property is incremented automatically.
- `Public Property Currency() As String` [R/W] Sets or returns the price currency used in the document row. Field name: Currency. Length: 3 characters.
  - remarks: You must define the currency strings before using this property. One business transaction may include more than one currency. In multiple currencies transaction, first call the GetCurrencyRate method to unify the total amount in different currencies into one currency. The value for multiple currencies is ##.
- `Public Property DiscountPercent() As Double` [R/W] Sets or returns the discount percentage of the item's Price. Field name: DiscPrcnt.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocEntry() As Long` [R] The internal ID of the document. Field name: DocEntry.
- `Public Property Factor() As Double` [R/W] Sets or returns the value of the first factor for calculating the item's quantity in the row. Field name: Factor1.
  - remarks: Example: A 1.20 m high fence is sold in square meters. To calculate the quantity on which the price is based, the system must multiply the sold length by the height of the fence. In this case, the length of the fence is multiplied by Factor1 and the height is multiplied by Factor2. The values of Factor1, Factor2, Factor3, Factor4 properties are used in purchase and sales documents. If the Quantity property is set, Factor 1, Factor 2, Factor 3, and Factor 4 properties are automatically set to 1 by default because the quantity overrides the factor fields. To set the factor fields, quantity must be empty.
- `Public Property Factor2() As Double` [R/W] Sets or returns the value of the first factor for calculating the item's quantity in the row. Field name: Factor2.
  - remarks: Example: A 1.20 m high fence is sold in square meters. To calculate the quantity on which the price is based, the system must multiply the sold length by the height of the fence. In this case, the length of the fence is multiplied by Factor1 and the height is multiplied by Factor2. The values of Factor1, Factor2, Factor3, Factor4 properties are used in purchase and sales documents. If the Quantity property is set, Factor 1, Factor 2, Factor 3, and Factor 4 properties are automatically set to 1 by default because the quantity overrides the factor fields. To set the factor fields, quantity must be empty.
- `Public Property Factor3() As Double` [R/W] Sets or returns the value of the first factor for calculating the item's quantity in the row. Field name: Factor3.
  - remarks: Example: A 1.20 m high fence is sold in square meters. To calculate the quantity on which the price is based, the system must multiply the sold length by the height of the fence. In this case, the length of the fence is multiplied by Factor1 and the height is multiplied by Factor2. The values of Factor1, Factor2, Factor3, Factor4 properties are used in purchase and sales documents. If the Quantity property is set, Factor 1, Factor 2, Factor 3, and Factor 4 properties are automatically set to 1 by default because the quantity overrides the factor fields. To set the factor fields, quantity must be empty.
- `Public Property Factor4() As Double` [R/W] Sets or returns the value of the first factor for calculating the item's quantity in the row. Field name: Factor4.
  - remarks: Example: A 1.20 m high fence is sold in square meters. To calculate the quantity on which the price is based, the system must multiply the sold length by the height of the fence. In this case, the length of the fence is multiplied by Factor1 and the height is multiplied by Factor2. The values of Factor1, Factor2, Factor3, Factor4 properties are used in purchase and sales documents. If the Quantity property is set, Factor 1, Factor 2, Factor 3, and Factor 4 properties are automatically set to 1 by default because the quantity overrides the factor fields. To set the factor fields, quantity must be empty.
- `Public Property FromWarehouseCode() As String` [R/W] The warehouse code from which the items are withdrawn. Field name: FromWhsCod. Length: 8 characters.
- `Public Property InventoryQuantity() As Double` [R/W] property InventoryQuantity
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. The item code must be unique. Mandatory property. Length: 20 characters. Field name: ItemCode.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property ItemDescription() As String` [R/W] Sets or returns the item name/description. Field name: Dscription. Length: 100 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number in the items list. Field name: LineNum.
- `Public Property LineStatus() As BoStatus` [R] property LineStatus
- `Public Property MeasureUnit() As String` [R/W] The measurement unit (e.g., inch, cm). Field name: unitMsr. Length: 20 characters.
- `Public Property Price() As Double` [R/W] Sets or returns the item price. Field name: Price.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code related to the stock transfer line. Field name: Project.
  - remarks: In SAP Business One, you can relate business transactions to projects. This can help you to create cost/income analyzes reports based on projects.
- `Public Property Quantity() As Double` [R/W] Sets or returns the quantity of the specified item. Field name: Quantity.
  - remarks: SAP Business One recalculates this value when modifying one or more of the factors.
- `Public Property Rate() As Double` [R/W] Sets or returns the currency exchange rate. Field name: Rate.
- `Public Property RemainingOpenInventoryQuantity() As Double` [R] property RemainingOpenInventoryQuantity
- `Public Property RemainingOpenQuantity() As Double` [R] property RemainingOpenQuantity
- `Public Property SerialNumber() As String` [R/W] Sets or returns the serial number of the item. Field: SerialNum. Length: 17 characters.
  - remarks: In SAP Business One, users can manage items by serial numbers so that providing additional information such as, items location in the warehouse, manufacturing date, warranty data, and so on. The work method is to enter serial numbers during stock entries for items that have a definition of serial numbers management, and to choose relevant serial numbers during sales or release documents.
- `Public Property SerialNumbers() As SerialNumbers` [R] Returns the SerialNumbers object.
- `Public Property UnitPrice() As Double` [R/W] Sets or returns this tax invoice raw unit price. Field name: UnitPrice.
- `Public Property UnitsOfMeasurment() As Double` [R/W] The number of items per measurement unit. The measurement unit is defined in the MeasureUnit property. Field name: NumPerMsr.
- `Public Property UoMCode() As String` [R] property UoMCode
- `Public Property UoMEntry() As Long` [R/W] property UoMEntry
- `Public Property UseBaseUnits() As BoYesNoEnum` [R/W] Indicates whether to use the base units as defined in SAP Business One. Field name: UseBaseUn.
  - remarks: In SAP Business One, users can define whether an item is sold or purchased in discrete units or in boxes, cases, and so on. For example, a 100 screws can be sold or purchased as one unit.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VendorNum() As String` [R/W] Sets or returns the vendor number that supplied this item. Field name: VendorNum. Length: 17 characters.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the warehouse code. Mandatory property. Length: 8 characters.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
