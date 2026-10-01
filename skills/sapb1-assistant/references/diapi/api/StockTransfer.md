<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# StockTransfer (Object)

StockTransfer is a business object that represents items to transfer from one warehouse to another. This object is part of the Inventory and Production module. Source tables: OWTR (ODRF for drafts)

**Remarks:** To display the form in the application: - Select Inventory --> Inventory Transactions --> Inventory Transfer.

## Properties (56)
- `Public Property Address() As String` [R/W] Sets or returns the customer address where the items are shipped to as a consignment. Field name: Address. Length: 254 characters.
- `Public Property ATDocumentType() As String` [R/W] property ATDocumentType
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property AuthorizationCode() As String` [R/W] property AuthorizationCode
- `Public Property AuthorizationStatus() As StockTransferAuthorizationStatusEnum` [R] Returns the status of the authorization for this payment. Field name: wddStatus.
- `Public Property BPLID() As Long` [R] property BPLID
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the code of the business partner who receives the items. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CardName() As String` [R/W] Sets or returns the name of the business partner who receives the items as a consignment. Field name: CardName. Length: 100 characters.
- `Public Property Comments() As String` [R/W] Sets or returns the remarks for the stock transfer. Field name: Comments. Length: 254 characters.
- `Public Property ContactPerson() As Long` [R/W] Sets or returns the code of the contact person. Field name: CntctCode. This is a foreign key to the ContactEmployees object.
- `Public Property CreationDate() As Date` [R] Returns the creation date of the stock transfer. Field name: CreateDate.
  - remarks: This property is internal in SAP Business One.
- `Public Property DocDate() As Date` [R/W] Sets or returns the posting date for the stock transfer. Field name: DocDate.
  - remarks: Default: current date.
- `Public Property DocEntry() As Long` [R] Returns the document entry key that identifies the stock transfer. Field name: DocEntry.
- `Public Property DocNum() As Long` [R] Returns the document number of the stock transfer. Field name: DocNum.
  - remarks: SAP Business One assigns automatically a consecutive number.
- `Public Property DocObjectCode() As BoObjectTypes` [R/W] Indicates that the object is a stock transfer. When creating a stock transfer draft, set this property to BoObjectTypes.oStockTransfer. Field name: ObjType
  - remarks: Set this property only when creating a stock transfer draft.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim draft As SAPbobsCOM.StockTransfer

    draft = oCompany.GetBusinessObject(BoObjectType.oStockTransferDraft)

    draft.DocObjectCode = BoObjectType.oStockTransfer

    ' ... set other properties

    draft.Add
    ```
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oDraft As SAPbobsCOM.StockTransfer

    Set oDraft = vCmp.GetBusinessObject(oStockTransferDraft)

    Dim oStockTransfer As SAPbobsCOM.StockTransfer

    oCompany.XmlExportType = xet_ExportImportMode

    oCompany.XMLAsString = False

    ' Get the draft to convert and save to file

    oDraft.GetByKey (3)

    oDraft.SaveXML ("c:\drafts.xml")

    ' ... change the object code from 179 (stock transfer draft) to 67 (stock transfer)

    ' ... in the XML file

    ' Create stock transfer

    Set oStockTransfer = oCompany.GetBusinessObjectFromXML("c:\drafts.xml", 0)

    oStockTransfer.Add
    ```
- `Public Property DocumentReferences() As Document_DocumentReferences` [R] property DocumentReferences
- `Public Property DocumentStatus() As BoStatus` [R] property DocumentStatus
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date for the document. Field name: DocDueDate.
- `Public Property EDocExportFormat() As Long` [R/W] property EDocExportFormat
- `Public Property ElecCommMessage() As String` [R] property ElecCommMessage
- `Public Property ElecCommStatus() As ElecCommStatusEnum` [R/W] property ElecCommStatus
- `Public Property ElectronicProtocols() As ElectronicProtocols` [R] property ElectronicProtocols
- `Public Property EndDeliveryDate() As Date` [R/W] property EndDeliveryDate
- `Public Property EndDeliveryTime() As Date` [R/W] property EndDeliveryTime
- `Public Property FinancialPeriod() As Long` [R] Returns the financial period. Field name: FinncPriod. This is a foreign key to the FinancePeriod object.
- `Public Property FolioNumber() As Long` [R/W] Sets or returns the reference number in a stock transfer. Country-specific field for Mexico and Chile. Field name: FolioNum.
- `Public Property FolioNumberFrom() As Long` [R/W] property FolioNumberFrom
- `Public Property FolioNumberTo() As Long` [R/W] property FolioNumberTo
- `Public Property FolioPrefixString() As String` [R/W] Sets or returns the prefix for the FolioNumber. Country-specific field for Mexico and Chile. Field name: FolioPref. Length: 2 characters.
- `Public Property FromWarehouse() As String` [R/W] Sets or returns the warehouse code from which the items are withdrawn. Field name: Filler. Length: 8 characters. This is a foreign key to the Warehouses object.
  - remarks: SAP Business One proposes the default warehouse.
- `Public Property JournalMemo() As String` [R/W] Sets or returns the journal entry details. Field name: JrnlMemo. Length: 50 characters.
- `Public Property LastPageFolioNumber() As Long` [R] Folio number of the last page of the marketing document in the Chile localization. Field name: LPgFolioN.
- `Public Property Letter() As FolioLetterEnum` [R/W] property Letter
- `Public Property Lines() As StockTransfer_Lines` [R] Returns the StockTransfer_Lines child object.
- `Public Property PointOfIssueCode() As String` [R/W] property PointOfIssueCode
- `Public Property PriceList() As Long` [R/W] Sets or returns the price list for the items. Field name: GroupNum. This is a foreign key to the PriceLists object.
- `Public Property Printed() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the stock transfer document was printed. Field name: Printed.
- `Public Property Reference1() As String` [R/W] Sets or returns the first reference code of the stock transfer. Field name: Ref1. Length: 11 characters.
- `Public Property Reference2() As String` [R/W] Sets or returns the second reference code of the stock transfer. Field name: Ref2. Length: 11 characters.
- `Public Property SalesPersonCode() As Long` [R/W] Sets or returns the sales person code. Field name: SlpCode. This is a foreign key to the SalesPersons object.
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property ShipToCode() As String` [R/W] property ShipToCode
- `Public Property StartDeliveryDate() As Date` [R/W] property StartDeliveryDate
- `Public Property StartDeliveryTime() As Date` [R/W] property StartDeliveryTime
- `Public Property StockTransfer_ApprovalRequests() As StockTransfer_ApprovalRequests` [R] Returns the StockTransfer_ApprovalRequests object.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the tax date for the document. Field name: TaxDate.
- `Public Property TaxExtension() As StockTransfer_TaxExtension` [R] Returns the stock tranfer tax extension child object.
- `Public Property ToWarehouse() As String` [R/W] The receiving warehouse for the transferred item. Field name: ToWhsCode. Length: 8 characters.
- `Public Property TransNum() As Long` [R] Returns the transaction code that SAP Business One creates for the stock transfer. Field: TransId.
- `Public Property UpdateDate() As Date` [R] Returns the date when the stock transfer document was last updated.
  - remarks: Internal property in SAP Business One.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VATRegNum() As String` [R] property VATRegNum
- `Public Property VehiclePlate() As String` [R/W] property VehiclePlate

## Methods (12)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Cancels a record from the object table. Supported from release 2005 SP1. Cancels a record from the object table.
- `Public Function Close() As Long` Not supported.
- `Public Function GetApprovalTemplates() As Long` Gets the related approval template.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal AbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `AbsEntry`: Specifies the document entry key that identifies the stock transfer (see DocEntry property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function HandleApprovalRequest() As Long` method HandleApprovalRequest
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Function SaveDraftToDocument() As Long` Converts an approved draft document to a valid document.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
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
