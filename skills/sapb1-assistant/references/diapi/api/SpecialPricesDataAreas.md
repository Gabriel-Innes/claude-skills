<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SpecialPricesDataAreas (Object)

SpecialPricesDataAreas is a child object of SpecialPrices object and represents special prices that are valid only for specified periods such as, holidays and season sales. Source table: SPP1.

**Remarks:** To display the form in the application: - Select Inventory --> Price Lists --> Special Prices --> Special Prices for Business Partners. - Double-click a line number in the Special Prices for Business Partners table.

## Properties (13)
- `Public Property AutoUpdate() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the price is updated automatically when the discount or price list number are modified. Field name: AutoUpdt.
  - remarks: Default value - tYES, SAP Business One calculates the SpecialPrice according to the Discount and the PriceListNo. If you set to tNO, SAP Business One ignores the Discount and PriceListNo properties and you must set the SpecialPrice property.
- `Public Property BPCode() As String` [R] Returns the identification code of the business partner for whom the special price applies. The BPCode returns from the CardCode property of the SpecialPrices object. Field name: CardCode. Length: 15 characters. This is a foreign key to the SpecialPrices object.
- `Public Property Count() As Long` [R] Returns the total rows in the table, that is the total number of records in the object.
- `Public Property DateFrom() As Date` [R/W] Sets or returns the start date of the special price. Field name: FromDate.
- `Public Property Dateto() As Date` [R/W] Sets or returns the end date of the special price. Field name: ToDate.
  - remarks: If you do not set the end date, then the period for the special price is not limited.
- `Public Property Discount() As Double` [R/W] Sets or returns the discount percentage for an item for the specified period. Field name: Discount.
- `Public Property ItemNo() As String` [R] Returns the item code in the inventory for which the special price applies. The ItemNo returns from the ItemCode property of the SpecialPrices object. Field name: ItemCode. This is a foreign key to the SpecialPrices object. Length: 20 characters.
- `Public Property PriceCurrency() As String` [R/W] Sets or returns the currency of the special price. The currency must match to the currency in the specified price list. Field name: Currency. Length: 3 characters.
- `Public Property PriceListNo() As Long` [R/W] Sets or returns the price list number. Field name: ListNum. This is a foreign key to the PriceLists object.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (0-based). Field name: LINENUM.
- `Public Property SpecialPrice() As Double` [R/W] Sets or returns the special price after discount. Field name: Price.
  - remarks: If you don’t have authorization to view the price, this property will return 0 with the nil="true" attribute in the exported xml file: <Price nil="true">0.000000</Price>.
- `Public Property SpecialPricesQuantityAreas() As SpecialPricesQuantityAreas` [R] Returns the SpecialPricesQuantityAreas child object.
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
