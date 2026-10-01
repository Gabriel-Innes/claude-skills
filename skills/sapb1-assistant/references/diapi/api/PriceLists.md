<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PriceLists (Object)

PriceLists is a business object that represents the management of price lists in the Inventory module. A price list is used by Items_Prices object to set the item prices. An item can have several prices, with each based on a different price list, for example, purchase price list, sales price list, distributor price list, and so on. This object enables you to: - Add a price list. - Retrieve a price list by its key. - Update a price list. - Delete a price list. - Save the object in XML format. Source table: OPLN.

**Remarks:** To display the form in the application: - Select Inventory --> Price Lists --> Price Lists.

## Properties (19)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property BasePriceList() As Long` [R/W] Sets or returns the base price list on which the price list (PriceListName) is based. Field name: BASE_NUM.
  - remarks: The base price lists are defined in the ASHP table which is not exposed through the DI API.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DefaultAdditionalCurrency1() As String` [R/W] property DefaultAdditionalCurrency1
- `Public Property DefaultAdditionalCurrency2() As String` [R/W] property DefaultAdditionalCurrency2
- `Public Property DefaultPrimeCurrency() As String` [R/W] property DefaultPrimeCurrency
- `Public Property Factor() As Double` [R/W] Sets or returns the factor for calculating prices of items based on the specified price list. Field name: Factor.
  - remarks: An item price (that is based on PriceListName) equals to the item price (that is based on BasePriceList) multiplied by the Factor.
- `Public Property FixedAmount() As Double` [R/W] property FixedAmount
- `Public Property GroupNum() As BoPriceListGroupNum` [R/W] Sets or returns a valid value of BoPriceListGroupNum type that specifies the group number to which the price list is related. Field name: GroupCode.
  - remarks: In SAP Business One, in General Authorization, you can set the access rights of a user to a price list group for modifying price lists.
- `Public Property IsGrossPrice() As BoYesNoEnum` [R/W] property IsGrossPrice
- `Public Property PriceListName() As String` [R/W] property PriceListName
  - remarks: Sets or returns the price list name (or description). Length: 32 characters. Field name: ListName.
- `Public Property PriceListNo() As Long` [R] Returns the price list unique ID. SAP Business One assigns a sequential number for each price list. Field name: ListNum.
- `Public Property RoundingFormatDecimalPart() As String` [R/W] property RoundingFormatDecimalPart
- `Public Property RoundingFormatIntegerPart() As String` [R/W] property RoundingFormatIntegerPart
- `Public Property RoundingMethod() As BoRoundingMethod` [R/W] Sets or returns a valid value of BoRoundingMethod type that specifies the rounding method of the item price calculation. Field name: RoundSys.
- `Public Property RoundingRule() As BoRoundingRule` [R/W] property RoundingRule
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidTo() As Date` [R/W] property ValidTo

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal QueueID As String) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database. Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `QueueID`: Price list unique ID (PriceListNo).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You cannot delete a price list if it is: - The base price list of another price list. - Associated with a business partner. - Associated with a product tree (ProductTrees) record. - Associated with a payment term type (PaymentTermsTypes) record. You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
