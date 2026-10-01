<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WorkOrders (Object)

WorkOrders is a business object that represents the work orders in the Inventory and Production module. This object is applicable only if work orders are already exist in the Company database. From release 2005, this object is replaced by the ProductionOrders object. Source table: OWKO.

**Remarks:** To display the form in the application (release 2004 only): - Select Production --> Work Order.

## Properties (26)
- `Public Property ActiveAccountCode() As String` [R/W] This property is not supported in this object. Supported only in WorkOrder_Lines.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Canceled() As BoYesNoEnum` [R] Determines whether or not the work order was canceled. Field name: Canceled.
- `Public Property Comment() As String` [R/W] Sets or returns remarks to the work order. Field name: Memo. Length: 254 characters.
- `Public Property ContactPerson() As Long` [R/W] Sets or returns the code of the contact person. Field name: CntctCode. This is a foreign key to the ContactEmployees object.
- `Public Property CustomerRefNo() As String` [R/W] Sets or returns the customer reference number related to the work order. Field name: NumInCustm. Length: 16 characters.
- `Public Property ExpectedCompletionDate() As Date` [R/W] Sets or returns the expected date for the product completion. Field name: ExpFinishD.
- `Public Property FinancialPeriod() As Long` [R] Returns the financial period. Field name: FinncPriod. This is a foreign key to the FinancePeriod object.
- `Public Property GenerationTime() As Date` [R/W] Sets or returns the generation time of the work order. Field name: DocTime.
- `Public Property InstructionNumber() As Long` [R] Returns the instruction number. That is the work order serial number, which is incremented automatically when adding a work order. Field name: SerialNum.
- `Public Property JournalRemarks() As String` [R/W] Sets or returns the journal remarks, of the G/L account, for the work order. Field name: JrnlMemo. Length: 50 characters.
  - remarks: The journal remark is copied to the accounting document when you set the work order Status to Work Completed.
- `Public Property Lines() As WorkOrder_Lines` [R] Returns the WorkOrder_Lines child object.
- `Public Property OrderDate() As Date` [R/W] Sets or returns the date for the work order. Field name: OrderDate.
  - remarks: SAP Business One suggest the current date as order date.
- `Public Property OrdererCode() As String` [R/W] Sets or returns the Contact code of the customer that ordered the work. Field name: CntctCode. Length: 11 characters.
- `Public Property OrdererName() As String` [R/W] Sets or returns the customer name as defined in the business partners master data. Field name: CustomName. Length: 100 characters.
- `Public Property OrderNum() As Long` [R] Returns the work order unique number (primary key) as assigned by SAP Business One. Field name: OrderNum.
- `Public Property OrderTotal() As Double` [R] Returns the total price of all the items specified in the work order. Field name: TotalOrder.
- `Public Property PriceListNum() As Long` [R/W] Sets or returns the number of the price list for a specified item. Field name: PriceList. This is a foreign key to the PriceLists object.
- `Public Property ReceiverName() As String` [R/W] Sets or returns the name of the employee that receives the production instructions. Field name: FinishUser. Length: 8 characters.
  - remarks: This property uses the internal key of the user. For Anonymous use the value -1.
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
- `Public Property Status() As BoWorkOrderStat` [R/W] Sets or returns a valid value of BoWorkOrderStat type that specifies the status of the work order. Field name: Status.
- `Public Property TotalCurrency() As String` [R] Returns the currency of the total price. Field name: TotalCurr. Length: 3 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WorkFinishDate() As Date` [R/W] Sets or returns the date for completing the product. Field name: FinishDate.
- `Public Property WorkStartDate() As Date` [R/W] Sets or returns the date for starting the production. Field name: ProdctDate.
- `Public Property WorkSum() As Double` [R/W] Not supported in this object. Supported only in WorkOrder_Lines. Field name: ActWorkSum.

## Methods (7)
- `Public Function Add() As Long` Adds a new workorder.
- `Public Function Cancel() As Long` Cancel a record from the object table. Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal WkoKey As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `WkoKey`: Specifies the work order identification key (OrderNum).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to an XML file.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
