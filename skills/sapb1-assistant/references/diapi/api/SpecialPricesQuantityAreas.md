<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SpecialPricesQuantityAreas (Object)

SpecialPricesQuantityAreas is a child object of SpecialPricesDataAreas object and represents special prices that are valid only for specified quantities and above. Source table: SPP2.

**Remarks:** To display the form in the application: - Select Inventory --> Price Lists --> Special Prices --> Special Prices for Business Partners. - Double-click a line number in the Special Prices for Business Partners table. - Double-click a line number in the Special Prices for Periods table.

## Properties (11)
- `Public Property BPCode() As String` [R] Returns the identification code of the business partner for whom the special price applies. The BPCode returns from the CardCode property of the SpecialPrices object. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartnersService object.
- `Public Property Count() As Long` [R] Returns the total rows in the table, that is the total number of records in the object.
- `Public Property Discountin() As Double` [R/W] Sets or returns the discount percentage for an item for the specified quantity. Field name: Discount.
- `Public Property ItemNo() As String` [R] Returns the item code in the inventory for which the special price applies. The ItemNo returns from the ItemCode property of the SpecialPrices object. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property PriceCurrency() As String` [R/W] Sets or returns the currency of the special price. The currency must match to the currency in the specified price list. Field name: Currency. Length: 3 characters.
- `Public Property Quantity() As Double` [R/W] Sets or returns the items quantity for which the special price applies. Field name: Amount.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (0-based). Field name: SPP2LNum.
- `Public Property SPDARowNumber() As Long` [R] Returns the row number in the SpecialPricesDataAreas object (RowNumber) for which the special price for quantity applies.
- `Public Property SpecialPrice() As Double` [R/W] Sets or returns the special price after the discount, which is based on quantities. Field name: Price.
- `Public Property UoMEntry() As Long` [R/W] property UoMEntry
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

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
