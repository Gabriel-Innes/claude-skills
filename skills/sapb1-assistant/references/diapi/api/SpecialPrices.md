<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SpecialPrices (Object)

Represents a discount for a specific item in a specific price list. The discount can apply to a specific business partner or for all business partners. - Specific Partners: To view discounts for specific business partners, select Inventory --> Price Lists --> Special Prices --> Special Prices for Business Partners. - All Business Partners: To view discounts for all business partners, select Inventory --> Price Lists --> Period and Volume Discounts. In previous versions, this was called Hierarchies and Expansions. For a specific business partner, the item and business partner must be unique; for all business partners, the item and price list must be unique. Source table: OSPP Mandatory fields: ItemCode

**Remarks:** For marketing documents, the system checks for special prices in the following order: - Special prices (this object) for the specified business partner - Discount groups (DiscountGroups) for the specified business partner and item - Special prices (this object) for all business partners If no special prices are found, the price is set by the default price list for the business partner.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  'Call the object

  Dim vSP As SAPbobsCOM.SpecialPrices

  Set vSP = vCompany.GetBusinessObject(oSpecialPrices)

  'set object's properties

  vSP.CardCode = "D10002"

  vSP.Currency = "Eur"

  vSP.DiscountPercent = 30.3

  vSP.ItemCode = "A00001"

  vSP.Price = 355.3

  vSP.PriceListNum = 0

  'Call the Add method

  Call vSP.Add
  ```
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim oSpp As SAPbobsCOM.SpecialPrices

  oSpp = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oSpecialPrices)

  oSpp.PriceListNum = 4

  oSpp.ItemCode = "I0001"

  oSpp.Price = 33.033

  oSpp.SpecialPricesDataAreas.PriceListNo = 4

  oSpp.SpecialPricesDataAreas.DateFrom = #10/20/2007 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Dateto = #11/20/2007 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Discount = 5

  oSpp.SpecialPricesDataAreas.Add()

  oSpp.SpecialPricesDataAreas.PriceListNo = 4

  oSpp.SpecialPricesDataAreas.DateFrom = #11/21/2007 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Dateto = #11/30/2007 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Discount = 6

  oSpp.SpecialPricesDataAreas.Add()

  oSpp.SpecialPricesDataAreas.PriceListNo = 4

  oSpp.SpecialPricesDataAreas.DateFrom = #12/21/2008 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Dateto = #12/30/2008 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.SpecialPrice = 28.808

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.Quantity = 101

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.SpecialPrice = 25.012

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.Add()

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.Quantity = 401

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.SpecialPrice = 24.98

  Dim retV As Integer = oSpp.Add()
  ```

## Properties (14)
- `Public Property AutoUpdate() As BoYesNoEnum` [R/W] Specifies whether to change the special price when the price list is updated. Field name: AutoUpdt.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner to which this discount applies. If blank, the discount applies to all business partners. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property Currency() As String` [R/W] Sets or returns the currency of the discount. The currency must match the currency of the specified price list. Field name: Currency. Length: 3 characters.
- `Public Property DiscountPercent() As Double` [R/W] Sets or returns the discount percentage. This property is date-dependent. Field name: Discount.
  - remarks: SAP Business One calculates the special price (Price property) on the basis of the specified price list (PriceListNum property) and discount percentage (DiscountPercent property). If you change the discount percentage, the price is automatically modified and vice versa.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code to which this discount applies. The item code must be unique. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
  - remarks: This property is mandatory.
- `Public Property Price() As Double` [R/W] Sets or returns the special price of the item. Field name: Price.
  - remarks: SAP Business One calculates the special price (Price property) on the basis of the specified price list (PriceListNum property) and discount percentage (DiscountPercent property). If you change the discount percentage, the price is automatically modified and vice versa. If you don’t have authorization to view the price, this property will return 0 with the nil="true" attribute in the exported xml file: <Price nil="true">0.000000</Price>.
- `Public Property PriceListNum() As Long` [R/W] Sets or returns the price list. Field name: ListNum. This is a foreign key to the PriceLists object.
  - remarks: The price list is used to calculate the special price. If you do not set a price list, then the special price (Price property) is not calculated on the basis of a price list. Instead, you must set the special price manually.
- `Public Property SourcePrice() As SourceCurrencyEnum` [R/W] property SourcePrice
- `Public Property SpecialPricesDataAreas() As SpecialPricesDataAreas` [R] Returns the SpecialPricesDataAreas child object.
- `Public Property UserFields() As UserFields` [R] property UserFields
- `Public Property Valid() As BoYesNoEnum` [R/W] property Valid
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidTo() As Date` [R/W] property ValidTo

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ItemCode As String, ByVal CardCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ItemCode`: The key of the item whose discounts are to be retrieved. This is a foreign key to the Items object.
  - param `CardCode`: The key of the business partner whose discounts are to be retrieved. This is a foreign key to the BusinessPartners object. Specifies the identification key of the business object (CardCode).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function GetByKeyDiscounts(ByVal ItemCode As String, ByVal PriceListNum As Long) As Boolean` Retrieves the discounts for a specific item that apply to all business partners. To retrieve discounts for a specific business partner, use the GetByKey method.
  - param `ItemCode`: The key of the item whose discounts are to be retrieved. This is a foreign key to the Items object.
  - param `PriceListNum`: The key of the price list whose discounts are to be retrieved. This is a foreign key to the PriceLists object.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oSppDel As SAPbobsCOM.SpecialPrices

    oSppDel = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oSpecialPrices)

    Dim bret As Boolean = oSppDel.GetByKeyDiscounts("I0001", "Code1")
    ```
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
