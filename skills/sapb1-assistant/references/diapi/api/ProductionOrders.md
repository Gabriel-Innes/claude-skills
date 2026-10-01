<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProductionOrders (Object)

The ProductionOrders object supports the creation and maintenance of production orders. This object replaces the WorkOrders object of release 2004. During upgrade to 2005, SAP Business One creates production orders based on the data of the existing work orders (OWKO, WKO1). Therefore, you must upgrade add-ons that use the WorkOrders object to use the ProductionOrders object. After the upgrade process work orders can be displayed only but cannot be maintained. Source table: OWOR.

**Remarks:** Mandatory properties for creating a new production order: ItemNo and DueDate. To display the form in the application: - Select Production --> Production Orders.

## Properties (45)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the production order as assigned by SAP Business One when adding one. Field name: DocEntry. Length: 11 characters.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ClosingDate() As Date` [R/W] Returns the date when the production order status is changed to Closed. Field name: CloseDate.
- `Public Property CompletedQuantity() As Double` [R] Returns the total quantity of the completed products that were received from production. Field name: CmpltQty.
  - remarks: The system calculates the total quantity by summing the Quantity of each transaction in IGN1 with the valid value botrntComplete (TransactionType).
- `Public Property CreationDate() As Date` [R] Returns the date of creation of the Production Order. Field name: CreateDate.
- `Public Property CustomerCode() As String` [R/W] Sets or returns the customer code, which is the card code in the business partner master data. Mandatory field in SAP Business One. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
  - remarks: During upgrade, this property retrieves the value from CustomerRefNo (WorkOrders).
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocumentNumber() As Long` [R] Returns the production order number, which is a sequential number, assigned by the system. Field name: DocNum. Length: 11 characters.
  - remarks: During upgrade, the system sets the next available number for the selected series. If the work order includes few rows, then each row is added as a separate production order. The system copies the work order number (OrderNum) to the production order remarks field.
- `Public Property DocumentReferences() As ProductionOrders_DocumentReferences` [R] property DocumentReferences
- `Public Property DueDate() As Date` [R/W] Sets or returns the planned completion date of the production order. The DueDate can be modified (read-write) while the ProductionOrderStatus is either Planned or Released (read-only when the status is Closed). Mandatory for creating a new production order. Field name: DueDate.
  - remarks: During upgrade, if ExpectedCompletionDate (WorkOrders) exists, the system copies it as is to DueDate, otherwise, the system sets the DueDate with the value of PostingDate.
- `Public Property InventoryUOM() As String` [R] Returns the inventory Unit of Measurement for the product (for example: box, case, piece). Field name: Uom. Length: 20 characters
- `Public Property ItemNo() As String` [R/W] Sets or returns the key of the product. Mandatory for creating a new production order. Field name: ItemCode. Length: 20 characters. This is a foreign key to the ProductTrees object.
- `Public Property JournalRemarks() As String` [R/W] Sets or returns the journal remarks for the G/L account that is related to the production order. Field name: JrnlMemo. Length: 50 characters.
- `Public Property Lines() As ProductionOrders_Lines` [R] Returns the ProductionOrders_Lines child object.
- `Public Property PlannedQuantity() As Double` [R/W] Sets or returns the planned quantity of the completed product. Field name: PlannedQty.
  - remarks: When upgrading SAP Business One from release 2004 to 2005, the value of the PlannedQuantity property will be as follows: If the 'Quantity' field in the work order is positive, the system will create a 'Standard' production order type, and the planned quantity will be similar to the work order quantity.If the 'Quantity' field in the work is negative, the system will create a 'Disassembly' production order type, and the planned quantity will be the same as the WO quantity without the minus sign (i.e. -9 will be 9 and order type= disassembly)
- `Public Property PostingDate() As Date` [R/W] Sets or returns the order date of the product. Field name: PostDate.
- `Public Property Printed() As BoYesNoEnum` [R] Returns a valid value that determines wether to use a printed copy or an original . Field name: Printed.
- `Public Property Priority() As Long` [R/W] The degree of importance of a production order, indicated by integer numbers. The default value is 100. You can manually change the number here. The smaller the number, the more important the production order. Field name: Priority.
- `Public Property ProductDescription() As String` [R/W] The descritpion of the product. Field name: ProdName. Length: 100 characters.
- `Public Property ProductionOrderOrigin() As BoProductionOrderOriginEnum` [R/W] Sets or returns the origin type of the production order (Manual, MRP, or Sales Order). Field name: OriginType.
- `Public Property ProductionOrderOriginEntry() As Long` [R/W] Sets or returns the key number of sales order that is linked to the production order. Field name: OriginAbs.
- `Public Property ProductionOrderOriginNumber() As Long` [R] The sales order number that is linked to the production order. Field name: OriginNum.
  - remarks: Only open sales order can be linked to a production order.
- `Public Property ProductionOrderStatus() As BoProductionOrderStatusEnum` [R/W] Sets or returns the status of the production order (Planned, Released, Closed, or Cancelled). Field name: Sets or returns the status of the production order (Planned, Released, Closed, or Cancelled)..
- `Public Property ProductionOrderType() As BoProductionOrderTypeEnum` [R/W] Set or returns the production order type (Standard, Special, or Disassembly). Field name: Type.
- `Public Property Project() As String` [R/W] The project that relates to the components of the product. Field: Project. Length: 20 characters.
- `Public Property RejectedQuantity() As Double` [R] Returns the total quantity of the rejected products that were received from production. Field name: RjctQty.
  - remarks: The system calculates the total quantity by summing the Quantity of each transaction in IGN1 with the valid value botrntReject (TransactionType).
- `Public Property ReleaseDate() As Date` [R] Returns the date when the production order status is changed to Released. Field name: RlsDate.
- `Public Property Remarks() As String` [R/W] Sets or returns remarks related to the production order. Field name: Comments. Length: 254 characters.
  - remarks: When upgrading SAP Business One from release 2004 to 2005, the value of the Remarks property will include the following information: - 'Series - ZZZ' (where: ZZZ is the series description) - 'WO No. XXX' (where: XXX is the old work order number) - 'Ref. No. YYY' (where: YYY is information from Customer Ref. No.) - WO Remarks. Example: 'Series - Primary, WO No. 213. Very important order' in the example, no data were in the ref. no. field'
- `Public Property RoutingDateCalculation() As ResourceAllocationEnum` [R/W] Determines how the resource allocation will occur. Field name: RouDatCalc.
- `Public Property SalesOrderLines() As ProductionOrders_SalesOrderLines` [R] Returns the ProductionOrders_SalesOrderLines object.
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property Series() As Long` [R/W] Sets or returns the key of the series that determines the production order number (DocumentNumber). Field name: Series.
  - remarks: During upgrade, this property retrieves the value from Series (WorkOrders).
- `Public Property Stages() As ProductionOrders_Stages` [R] Returns the ProductionOrders_Stages child object.
- `Public Property StartDate() As Date` [R/W] The start date of the production. You can change it manually, which may affect Due Date. Field name: StartDate.
- `Public Property TransactionNumber() As Long` [R] Returns the transaction code that SAP Business One creates for the production order. Field name: TransId. This is a foreign key to the JournalEntries object.
- `Public Property UoMEntry() As Long` [R] The internal key of the UoM. Field name: UomEntry.
- `Public Property UpdateAllocation() As BoUpdateAllocationEnum` [R/W] property UpdateAllocation
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who manages the production order. Field name: UserSign.
- `Public Property Warehouse() As String` [R/W] Sets or returns the identification key of the warehouse that will receive the completed product. Length: 8 characters. Field name: Warehouse. This is a foreign key to the Warehouses object.

## Methods (7)
- `Public Function Add() As Long` Adds a new record to the table.
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: For vesrions prior to 2007 A, use DocumentNumber property. From version 2007 A, use AbsoluteEntry property. Historically the GetByKey method for production order got the DocumentNumber property Field name: DocNum) as an input, different from any other document that got the DocEntry as an input. Starting from SAP Business One 2007 A release the GetByKey for production order gets as an input the AbsoluteEntry property Field name: DocEntry), like any other document.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
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
