<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Items_Prices (Object)

Items_Prices is a child object of the Items object that represents the items' prices in the Inventory and Production module. This object enables you to specify prices for various price lists. Source table: ITM1

**Remarks:** Mandatory fields in SAP Business One: Price and PriceList. To display the form in the application: - Select Inventory --> Item Master Data. - Select a Price List, and set a price.

**Example:**
- example note: The sample prints the pricelist of the Item and updates the price of the Item in the current price list.
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
         Dim lErrCode As Long

          Dim sErrMsg As String

          Dim bRetVal As Boolean

          Dim oItems As SAPbobsCOM.Items

          Dim oItemPrice As SAPbobsCOM.Items_Prices

          Dim i As Integer

          'Retrieve Items object

          oItems = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oItems)

          'Retrieve specific item

          bRetVal = oItems.GetByKey("X0004")

          'Check errors

          If Not bRetVal Then

              oCompany.GetLastError(lErrCode, sErrMsg)

              MsgBox("Failed to Retrieve the record " & lErrCode & " " & sErrMsg)

              Exit Sub

          End If

          'get item price object

          oItemPrice = oItems.PriceList

          'print price lists names and prices

          For i = 0 To oItemPrice.Count - 1

              oItemPrice.SetCurrentLine(i)

              'print price list name

              Debug.WriteLine(oItemPrice.PriceListName())

              'print the items price

              Debug.WriteLine(oItemPrice.Price())

          Next

          'change the price of the item in the last price list

          oItemPrice.Price = 600

          'save changes

          oItems.Update()
  ```

## Properties (13)
- `Public Property AdditionalCurrency1() As String` [R/W] property AdditionalCurrency1
- `Public Property AdditionalCurrency2() As String` [R/W] property AdditionalCurrency2
- `Public Property AdditionalPrice1() As Double` [R/W] property AdditionalPrice1
- `Public Property AdditionalPrice2() As Double` [R/W] property AdditionalPrice2
- `Public Property BasePriceList() As Long` [R/W] property BasePriceList
- `Public Property Count() As Long` [R] Returns the number of prices for the current item.
  - remarks: When you add a new price, the value is increased automatically.
- `Public Property Currency() As String` [R/W] Sets or returns the price currency used in the document row. Field name: Currency. Length: 3 characters.
  - remarks: You must define the currency strings before using this property. One business transaction may include more than one currency. In multiple currencies transaction, first call the GetCurrencyRate method to unify the total amount in different currencies into one currency. The value for multiple currencies is ##.
- `Public Property Factor() As Double` [R/W] property Factor
- `Public Property Price() As Double` [R/W] Sets or returns the item price before taxation. Mandatory property.
- `Public Property PriceList() As Long` [R] Returns the price list index for the item.
- `Public Property PriceListName() As String` [R] Returns the price list name. Length: 32 characters.
- `Public Property UoMPrices() As UoMPrices` [R] property UoMPrices
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
