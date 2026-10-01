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

# State (Object)

Represents a state that can be included, for example, in an address for a business partner. Source table: OCST All properties are mandatory.

**Remarks:** Each state is assigned to a specific country.

## Properties (5)
- `Public Property Code() As String` [R/W] The short name of the state. Field name: Code
  - remarks: Must contain at least one non-space character.
- `Public Property Country() As String` [R/W] The country to which this state is assigned. This is a foreign key to the Country object. Field name: Country
- `Public Property GSTCode() As String` [R/W] property GSTCode
- `Public Property IsUnionTerritory() As BoYesNoEnum` [R/W] property IsUnionTerritory
- `Public Property Name() As String` [R/W] The display name for the state. Field name: Name
  - remarks: Must contain at least one non-space character.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# StateParams (Object)

Holds the key and name to an existing state. This object is used to pass keys to and retrieve keys from StatesService methods.

## Properties (3)
- `Public Property Code() As String` [R/W] The short name of a specific state. Field name: Code
  - remarks: Must contain at least one non-space character.
- `Public Property Country() As String` [R/W] The country to which a specific state is assigned. Field name: Country
- `Public Property Name() As String` [R] The name of a specific state. Field name: Name
  - remarks: Must contain at least one non-space character.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# StatesParams (Collection)

A collection of StateParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As StateParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As StateParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# StatesService (Object)

The StatesService service enables you to add, look up and remove states in the states master data table. States are assigned to business partners and other objects as part of the address information. Each state is associated with a specific country. To see the list of states, select Administration --> System Initialization --> Company Details --> General tab --> Local Language tab --> State combobox --> Define new Source table: OCST

## Methods (8)
- `Public Function AddState(ByVal pIState As State) As StateParams` Adds a state.
  - param `pIState`: The data for the new state.
  - returns: Contains the key (Code, Country) of the new state.
  - C# example (from SAP's help):
    ```csharp
    // Get states service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    StatesService oStatesService = (StatesService)oCompanyService.GetBusinessService(ServiceTypes.StatesService);

    // Add a State
    SAPbobsCOM.State oState = (SAPbobsCOM.State)oStatesService.GetDataInterface
        (StatesServiceDataInterfaces.ssState);

    oState.Code = "Z1";
    oState.Country = "US";
    oState.Name = "ZZ4";

    oStatesService.AddState(oState);
    ```
- `Public Sub DeleteState(ByVal pIStateParams As StateParams)` Deletes an existing state. The state is specified by its key (Code, Country), which is contained in the StateParams object passed to the method.
  - param `pIStateParams`: The key of the state to be deleted.
  - C# example (from SAP's help):
    ```csharp
    // Get states service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    StatesService oStatesService = (StatesService)oCompanyService.GetBusinessService(ServiceTypes.StatesService);

    // Delete a state
    SAPbobsCOM.StateParams oStateParams = (SAPbobsCOM.StateParams)oStatesService.GetDataInterface
        (StatesServiceDataInterfaces.ssStateParams);

    oStateParams.Code = "ZZ1";
    oStateParams.Country = "US";

    oStatesService.DeleteState(oStateParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As StatesServiceDataInterfaces) As Object` Creates an empty data structure for use with the StatesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `StatesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
- `Public Function GetState(ByVal pIStateParams As StateParams) As State` Retrieves a state. The state is specified by its key (Code, Country), which is contained in the StateParams object passed to the method.
  - param `pIStateParams`: The key of the state to retrieve.
  - returns: The state with the specified key.
- `Public Function GetStateList() As StatesParams` Retrieves the keys and names of all the states.
  - C# example (from SAP's help):
    ```csharp
    // Get states service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    StatesService oStatesService = (StatesService)oCompanyService.GetBusinessService(ServiceTypes.StatesService);

    // Get list of states
    SAPbobsCOM.StatesParams oStatesList = oStatesService.GetStateList();
    ```
- `Public Sub UpdateState(ByVal pIState As State)` Updates an existing state. The data for the state, including the key of the state to be updated, is contained in the State passed to the method. To update a state, you must first retrieve it using the GetState method.
  - param `pIState`: The data for the state to be updated. The State object must contain the key (Code, Country) of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    // Get states service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    StatesService oStatesService = (StatesService)oCompanyService.GetBusinessService(ServiceTypes.StatesService);

    // Update a State
    SAPbobsCOM.StateParams oStateParams = (SAPbobsCOM.StateParams)oStatesService.GetDataInterface
        (StatesServiceDataInterfaces.ssStateParams);

    oStateParams.Code = "ZZ1";
    oStateParams.Country = "US";

    SAPbobsCOM.State oState = oStatesService.GetState(oStateParams);
    oState.Name = "ZZ9";

    oStatesService.UpdateState(oState);
    ```

# StockTaking (Object)

This function is abandoned in SAP Business One 9.0. If you use this object, an ATL Error occurs. StockTaking is a business object that is used to take items from a warehouse, or to put items into a warehouse. Source table: OITW.

**Remarks:** Mandatory fields in SAP Business One: ItemCode and WarehouseCode. To display the form in the application: - Select Inventory --> Inventory Transactions --> Beginning quantities and cycle counting. - In Stock Posting tab select your warehouse and then click OK.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Counted() As Double` [R/W] Sets or returns the number of items in stock to take. Field name: Counted.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the warehouse code. Field name: WhsCode. Length: 8 characters. This is a foreign key to the Warehouses object.

## Methods (5)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrItemCode As String, ByVal bstrWhsCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrItemCode`: ItemCode.
  - param `bstrWhsCode`: WarehouseCode.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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

# StockTransfer_ApprovalRequests (Object)

StockTransfer_ApprovalRequests is a child object of the StockTransfer object. You can set the remarks field of the approval request. Source table: OWDDV.

## Properties (5)
- `Public Property ActiveForUpdate() As BoYesNoEnum` [R] property ActiveForUpdate
- `Public Property ApprovalTemplatesID() As Long` [R] The ID of the approval template. Field: WtmCode.
- `Public Property ApprovalTemplatesName() As String` [R] property ApprovalTemplatesName
- `Public Property Count() As Long` [R] property Count
- `Public Property Remarks() As String` [R/W] Remarks made by the originator that are included with the approval request. Field: Remarks. Length: 100 characters.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

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

# StockTransfer_TaxExtension (Object)

StockTransfer_TaxExtension is a child object of the StockTransfer object. It represents the tax extension of stock tranfers. Applicable for cluster B only (country-specific for India). Source table: WTR12.

## Properties (4)
- `Public Property FormNumber() As String` [R/W] Sets or returns the form number used for the transaction category in Warehouse Transfer. Field name: FormNo.
- `Public Property SupportVAT() As BoYesNoEnum` [R/W] Sets or returns a valid value to identify Stock transfers created for Sales Tax purposes in Warehouse Transfer. Field name: Vat.
- `Public Property TransactionCategory() As String` [R/W] Sets or returns the transaction category. This property is a foreign key of Transaction Category table (OTNC - not exposed through the DI API). Field name: TransCat.
  - remarks: Dealer has to issue declarations in which form printed and supplied by the Sales Tax authorities in Warehouse Transfer.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

# StockTransferLinesBinAllocations (Object)

StockTransferLinesBinAllocations is a child object of the StockTransfer_Lines object that represents the bin allocation of items or serial items or batch items. Source table: INV19.

## Properties (7)
- `Public Property AllowNegativeQuantity() As BoYesNoEnum` [R/W] Indicates whether to allow enter negative quantity. Field name: AllowNeg.
- `Public Property BaseLineNumber() As Long` [R/W] property BaseLineNumber
- `Public Property BinAbsEntry() As Long` [R/W] The internal number of the bin location. Field name: BinAbs.
- `Public Property BinActionType() As BinActionTypeEnum` [R/W] The type of the bin action. Field name: BinActTyp.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property Quantity() As Double` [R/W] The quantity allocated to the bin location. Field name: Quantity.
- `Public Property SerialAndBatchNumbersBaseLine() As Long` [R/W] The internal number of the serial and batch numbers master data. Field name: SnBMDAbs.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# TargetGroup (Object)

A target group is a list of prospects. You can create a target group and then define a promotional campaign for targeting this group. You can add prospects either from existing customers and leads or from an external Microsoft Excel file. Source table: OTTG.

## Properties (4)
- `Public Property TargetGroupCode() As String` [R/W] The code of the target group. Field name: TargetCode. Length: 20 characters.
- `Public Property TargetGroupName() As String` [R/W] The name of the target group. Field name: TargetName. Length: 20 characters.
- `Public Property TargetGroupsDetails() As TargetGroupsDetails` [R] The detailed information of the potential customers or leads for the target group.
- `Public Property TargetGroupType() As TargetGroupTypeEnum` [R/W] property TargetGroupType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TargetGroupParams (Object)

Holds the key to an existing target group. This object is used to pass keys to and retrieve keys from TargetGroupsService methods.

## Properties (2)
- `Public Property TargetGroupCode() As String` [R/W] The code of the target group. Field name: TargetCode. Length: 20 characters.
- `Public Property TargetGroupName() As String` [R/W] The name of the target group. Field name: TargetName. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TargetGroupsDetail (Object)

The detailed information of the potential customers or leads for the target group. This is a child object of the TargetGroup object. Source table: TTG1.

## Properties (22)
- `Public Property ActiveStatus() As TargetGroupsDetailStatusEnum` [R] The status of the business partner. Field name: validFor.
- `Public Property Address() As String` [R] The address of the contact person. Field name: Address.
- `Public Property Block() As String` [R/W] The block of the contact person. Field name: Block. Length: 100 characters.
- `Public Property Building() As String` [R/W] The building/floor/room of the contact person. Field name: Building. Length: 16 characters.
- `Public Property BusinessPartnerCode() As String` [R/W] The code of the business partner. Field name: CardCode. Length: 15 characters.
- `Public Property BusinessPartnerName() As String` [R/W] The name of the business partner. Field name: CardName. Length: 100 characters.
- `Public Property City() As String` [R/W] The city of the contact person. Field name: City. Length: 100 characters.
- `Public Property ContactPerson() As String` [R/W] The default contact person of the business partner. Field name: CntctPrsn. Length: 50 characters.
- `Public Property Country() As String` [R/W] The country of the contact person. Field name: Country. Length: 3 characters.
- `Public Property County() As String` [R/W] The county of the contact person. Field name: County. Length: 100 characters.
- `Public Property E_Mail() As String` [R/W] The E-mail of the contact person. Field name: E_Mail. Length: 100 characters.
- `Public Property Fax() As String` [R/W] The fax number of the contact person. Field name: Fax. Length: 50 characters.
- `Public Property GroupCode() As String` [R] The group code of the business partner. Field name: GroupCode. Length: 20 characters.
- `Public Property Industry() As String` [R] The industry of the business partner. Field name: Industry. Length: 16 characters.
- `Public Property MobilePhone() As String` [R/W] The mobile phone of the contact person. Field name: Cellolar. Length: 50 characters.
- `Public Property Position() As String` [R/W] The position of the contact person. Field name: Position. Length: 90 characters.
- `Public Property State() As String` [R/W] The state of the contact person. Field name: State. Length: 3 characters.
- `Public Property Street() As String` [R/W] The street of the contact person. Field name: Street. Length: 100 characters.
- `Public Property TargetGroupCode() As String` [R] The code of the target group. Field name: TargetCode.
- `Public Property Telephone() As String` [R/W] The telephone number of the contact person. Field name: Telephone. Length: 50 characters.
- `Public Property Title() As String` [R/W] The title of the contact person. Field name: Title. Length: 10 characters.
- `Public Property ZipCode() As String` [R/W] The zipcode of the contact person. Field name: ZipCode. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TargetGroupsDetails (Collection)

A collection of TargetGroupsDetail objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As TargetGroupsDetail` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As TargetGroupsDetail` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TargetGroupsParams (Collection)

A collection of TargetGroupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As TargetGroupParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As TargetGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TargetGroupsService (Object)

The TargetGroupsService service enables you to add, look up, update, and remove target groups. Source table: OTTG.

**Remarks:** To create a target group, proceed as follows: From the SAP Business One Main Menu, choose Administration --> Set Up --> Business Partners --> Target Group. In the Target Group – Set Up window, specify the Target Group Code and the Target Group Name for the new group and choose Update. In the # column, double-click the gray sequence number area corresponding to the target group you created in step 2. The Target Group Details window appears.

## Methods (8)
- `Public Function Add(ByVal pITargetGroup As TargetGroup) As TargetGroupParams` Adds a target group.
  - param `pITargetGroup`: The data for the new target group.
- `Public Sub Delete(ByVal pITargetGroupParams As TargetGroupParams)` Deletes an existing target group.
  - param `pITargetGroupParams`: The key of the target group to be deleted.
- `Public Function Get(ByVal pITargetGroupParams As TargetGroupParams) As TargetGroup` Retrieves a target group. The target group is specified by its key, which is contained in the TargetGroupParams object passed to the method.
  - param `pITargetGroupParams`: The key of the target group to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As TargetGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the TargetGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TargetGroupsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As TargetGroupsParams` Returns the TargetGroupsParams data collection that identifies all target groups.
- `Public Sub Update(ByVal pITargetGroup As TargetGroup)` Updates an existing target group.
  - param `pITargetGroup`: The data for the target group to be updated. The TargetGroup object must contain the key of the object to be updated.

# TaxCodeDetermination (Object)

Represents the tax code determination rules according to which the application proposes tax codes in sales and purchasing document lines. Source table: OTCX.

**Remarks:** Relevant for all localizations except Brazil, India, Israel, and Puerto Rico.

## Properties (38)
- `Public Property BusinessArea() As BoBusinessAreaEnum` [R/W] The business area, for which the tax code determination rule is relevant, for example, sales, purchasing, or both. Mandatory property. Field name: BusArea.
- `Public Property Condition1() As BoTCDConditionEnum` [R/W] The condition based upon which the tax code is determined. If you select more than one condition, all conditions must be met for the tax code determination rule to be applied. Mandatory property. Field name: Cond1.
- `Public Property Condition2() As BoTCDConditionEnum` [R/W] The second condition based upon which the tax code is determined. Field name: Cond2.
- `Public Property Condition3() As BoTCDConditionEnum` [R/W] The third condition based upon which the tax code is determined. Field name: Cond3.
- `Public Property Condition4() As BoTCDConditionEnum` [R/W] The fourth condition based upon which the tax code is determined. Field name: Cond4.
- `Public Property Condition5() As BoTCDConditionEnum` [R/W] The fifth condition based upon which the tax code is determined. Field name: Cond5.
- `Public Property Description() As String` [R/W] The additional explanation for the tax code determination rule. Field name: Descr. Length: 250 characters.
- `Public Property DocEntry() As Long` [R] The internal key of the document. Field name: DocEntry.
- `Public Property DocumentType() As BoTCDDocumentTypeEnum` [R/W] The type of document, for which the tax code determination rule is relevant, for example, item, service, or both. Mandatory property. Field name: DocType.
- `Public Property FreightHeaderTax() As String` [R/W] The tax code for freight charges in sales or purchasing document headers. Field name: FrHdrTax.
  - remarks: In the SAP Business One application, this field is available only if you have selected Manage Freight in Documents on the General tab of the Document Settings window (Administration --> System Initialization --> Document Settings).
- `Public Property FreightRowTax() As String` [R/W] The tax code for freight charges in sales or purchasing document lines. Field name: FrLnTax.
- `Public Property LineNumber() As Long` [R/W] Sets or returns the row number within the hierarchy of tax code determination rules. When determining the tax code proposal in a sales or purchasing document, the application works its way through the rules, starting at the highest position. Field name: LineNum.
- `Public Property MoneyValue1() As Double` [R/W] The monetary value for condition 1. Field name: MnyVal1.
- `Public Property MoneyValue2() As Double` [R/W] The monetary value for condition 2. Field name: MnyVal2.
- `Public Property MoneyValue3() As Double` [R/W] The monetary value for condition 3. Field name: MnyVal3.
- `Public Property MoneyValue4() As Double` [R/W] The monetary value for condition 4. Field name: MnyVal4.
- `Public Property MoneyValue5() As Double` [R/W] The monetary value for condition 5. Field name: MnyVal5.
- `Public Property NumberValue1() As Long` [R/W] The numeric value for condition 1. Field name: NumVal1.
- `Public Property NumberValue2() As Long` [R/W] The numeric value for condition 2. Field name: NumVal2.
- `Public Property NumberValue3() As Long` [R/W] The numeric value for condition 3. Field name: NumVal3.
- `Public Property NumberValue4() As Long` [R/W] The numeric value for condition 4. Field name: NumVal4.
- `Public Property NumberValue5() As Long` [R/W] The numeric value for condition 5. Field name: NumVal5.
- `Public Property StringValue1() As String` [R/W] The string value for condition 1. Field name: StrVal1.
- `Public Property StringValue2() As String` [R/W] The string value for condition 2. Field name: StrVal2.
- `Public Property StringValue3() As String` [R/W] The string value for condition 3. Field name: StrVal3.
- `Public Property StringValue4() As String` [R/W] The string value for condition 4. Field name: StrVal4.
- `Public Property StringValue5() As String` [R/W] The string value for condition 5. Field name: StrVal5.
- `Public Property TaxCode() As String` [R/W] The tax code that is proposed in sales or purchasing documents, if the tax code determination rule applies. You can use one of the tax codes defined in the application or create a new one. Field name: LnTaxCode. Length: 8 characters.
- `Public Property UDFAlias1() As String` [R/W] The alias of the user-defined field for condition 1. Field name: UDFAlias1.
- `Public Property UDFAlias2() As String` [R/W] The alias of the user-defined field for condition 2. Field name: UDFAlias2.
- `Public Property UDFAlias3() As String` [R/W] The alias of the user-defined field for condition 3. Field name: UDFAlias3.
- `Public Property UDFAlias4() As String` [R/W] The alias of the user-defined field for condition 4. Field name: UDFAlias4.
- `Public Property UDFAlias5() As String` [R/W] The alias of the user-defined field for condition 5. Field name: UDFAlias5.
- `Public Property UDFTable1() As String` [R/W] The title of the user-defined field for condition 1. Field name: UdfTable1.
  - remarks: To see details of the user-defined field in SAP Business One application, choose Tools --> Customization Tools --> User-Defined Fields - Management.
- `Public Property UDFTable2() As String` [R/W] The title of the user-defined field for condition 2. Field name: UdfTable2.
- `Public Property UDFTable3() As String` [R/W] The title of the user-defined field for condition 3. Field name: UdfTable3.
- `Public Property UDFTable4() As String` [R/W] The title of the user-defined field for condition 4. Field name: UdfTable4.
- `Public Property UDFTable5() As String` [R/W] The title of the user-defined field for condition 5. Field name: UdfTable5.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TaxCodeDeterminationParams (Object)

Holds the key to an existing tax code determination rule. This object is used to pass keys to and retrieve keys from TaxCodeDeterminationsService methods.

## Properties (1)
- `Public Property DocEntry() As Long` [R/W] Returns the document entry key that identifies the tax code determination rule. Field name: DocEntry.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TaxCodeDeterminationsParams (Collection)

A collection of TaxCodeDeterminationParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As TaxCodeDeterminationParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As TaxCodeDeterminationParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TaxCodeDeterminationsService (Object)

The TaxCodeDeterminationsService service enables you to add, look up, update, and remove tax code determination rules. For all localizations except Brazil, India, Israel and Puerto Rico, you can set up tax code determination rules that take precedence over the tax information in the business partner or item master data, and in G/L account determination. Source table: OTCX.

**Remarks:** To see the list of tax code determination rules, choose Administration --> Setup --> Financials --> Tax --> Tax Code Determination.

## Methods (8)
- `Public Function AddTaxCodeDetermination(ByVal pITaxCodeDetermination As TaxCodeDetermination) As TaxCodeDeterminationParams` Adds a tax code determination rule.
  - param `pITaxCodeDetermination`: The data for the new tax code determination rule.
- `Public Sub DeleteTaxCodeDetermination(ByVal pITaxCodeDeterminationParams As TaxCodeDeterminationParams)` Deletes an existing tax code determination rule.
  - param `pITaxCodeDeterminationParams`: The key of the tax code determination rule to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As TaxCodeDeterminationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the TaxCodeDeterminationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TaxCodeDeterminationsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetTaxCodeDetermination(ByVal pITaxCodeDeterminationParams As TaxCodeDeterminationParams) As TaxCodeDetermination` Retrieves a tax code determination rule. The tax code determination rule is specified by its key, which is contained in the TaxCodeDeterminationParams object passed to the method.
  - param `pITaxCodeDeterminationParams`: The key of the tax code determination rule to retrieve.
- `Public Function GetTaxCodeDeterminationList() As TaxCodeDeterminationsParams` Returns the TaxCodeDeterminationsParams data collection that identifies all tax code determination rules.
- `Public Sub UpdateTaxCodeDetermination(ByVal pITaxCodeDetermination As TaxCodeDetermination)` Updates an existing tax code determination rule. The data for the tax code determination rule, including the key of the tax code determination rule to be updated, is contained in the TaxCodeDetermination object passed to the method. To update a tax code determination rule, you must first retrieve it using the GetTaxCodeDetermination method.
  - param `pITaxCodeDetermination`: The data for the tax code determination rule to be updated. The TaxCodeDetermination object must contain the key of the object to be updated.

# TaxCodeDeterminationsTCDParams (Collection)

Legal Text on Tax Code Determination - Setup form.

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TaxCodeDeterminationTCDParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TaxCodeDeterminationTCDParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationsTCDService (Object)

TaxCodeDeterminationsTCDService Class

## Methods (6)
- `Public Function GetDataInterface(ByVal enumMSDI As TaxCodeDeterminationsTCDServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TaxCodeDeterminationsTCDServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTaxCodeDeterminationTCD(ByVal pITaxCodeDeterminationTCDParams As TaxCodeDeterminationTCDParams) As TaxCodeDeterminationTCD` GetTaxCodeDeterminationTCD
  - param `pITaxCodeDeterminationTCDParams`: 
- `Public Function GetTaxCodeDeterminationTCDList() As TaxCodeDeterminationsTCDParams` GetTaxCodeDeterminationTCDList
- `Public Sub UpdateTaxCodeDeterminationTCD(ByVal pITaxCodeDeterminationTCD As TaxCodeDeterminationTCD)` UpdateTaxCodeDeterminationTCD
  - param `pITaxCodeDeterminationTCD`: 

# TaxCodeDeterminationTCD (Object)

TaxCodeDeterminationTCD Class

## Properties (7)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property DefaultPurchase() As String` [R/W] property DefaultPurchase
- `Public Property DefaultSales() As String` [R/W] property DefaultSales
- `Public Property DefaultSalesAndPurchaseByUsages() As TaxCodeDeterminationTCDByUsages` [R] property DefaultSalesAndPurchaseByUsages
- `Public Property DefaultSalesAndPurchaseWTs() As TaxCodeDeterminationTCDDefaultWTs` [R] property DefaultSalesAndPurchaseWTs
- `Public Property KeyFields() As TaxCodeDeterminationTCDKeyFields` [R] property KeyFields
- `Public Property Type() As TaxCodeDeterminationTCDTypeEnum` [R] property Type

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDByUsage (Object)

TaxCodeDeterminationTCDByUsage Class

## Properties (6)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property FreightTaxCode() As String` [R/W] property FreightTaxCode
- `Public Property PurchaseTaxCode() As String` [R/W] property PurchaseTaxCode
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property Type() As TaxCodeDeterminationTCDByUsageTypeEnum` [R/W] property Type
- `Public Property UsageCode() As Long` [R/W] property UsageCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDByUsages (Collection)

TaxCodeDeterminationTCDByUsages Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As TaxCodeDeterminationTCDByUsage` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TaxCodeDeterminationTCDByUsage` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDDefaultWT (Object)

TaxCodeDeterminationTCDDefaultWT Class

## Properties (3)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property Type() As TaxCodeDeterminationTCDDefaultWTTypeEnum` [R/W] property Type
- `Public Property WTCode() As String` [R/W] property WTCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDDefaultWTs (Collection)

TaxCodeDeterminationTCDDefaultWTs Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As TaxCodeDeterminationTCDDefaultWT` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TaxCodeDeterminationTCDDefaultWT` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDKeyField (Object)

TaxCodeDeterminationTCDKeyField Class

## Properties (17)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property Description() As String` [R/W] property Description
- `Public Property KeyField1() As Long` [R/W] property KeyField1
- `Public Property KeyField2() As Long` [R/W] property KeyField2
- `Public Property KeyField3() As Long` [R/W] property KeyField3
- `Public Property KeyField4() As Long` [R/W] property KeyField4
- `Public Property LegalText() As String` [R/W] Legal text defined on the Tax Code Determination - Setup window. Field name: LegalText. Length: 250 characters.
- `Public Property Priority() As Long` [R/W] property Priority
- `Public Property UDFAlias1() As String` [R/W] property UDFAlias1
- `Public Property UDFAlias2() As String` [R/W] property UDFAlias2
- `Public Property UDFAlias3() As String` [R/W] property UDFAlias3
- `Public Property UDFAlias4() As String` [R/W] property UDFAlias4
- `Public Property UDFTable1() As String` [R/W] property UDFTable1
- `Public Property UDFTable2() As String` [R/W] property UDFTable2
- `Public Property UDFTable3() As String` [R/W] property UDFTable3
- `Public Property UDFTable4() As String` [R/W] property UDFTable4
- `Public Property Values() As TaxCodeDeterminationTCDValues` [R] property Values

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDKeyFields (Collection)

TaxCodeDeterminationTCDKeyFields Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As TaxCodeDeterminationTCDKeyField` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TaxCodeDeterminationTCDKeyField` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDParams (Object)

TaxCodeDeterminationTCDParams Class

## Properties (1)
- `Public Property AbsId() As Long` [R/W] property AbsId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDPeriod (Object)

TaxCodeDeterminationTCDPeriod Class

## Properties (5)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property ByUsages() As TaxCodeDeterminationTCDByUsages` [R] property ByUsages
- `Public Property EffectFrom() As Date` [R/W] property EffectFrom
- `Public Property EffectTo() As Date` [R/W] property EffectTo
- `Public Property TaxCode() As String` [R/W] property TaxCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDPeriods (Collection)

TaxCodeDeterminationTCDPeriods Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As TaxCodeDeterminationTCDPeriod` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TaxCodeDeterminationTCDPeriod` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDValue (Object)

TaxCodeDeterminationTCDValue Class

## Properties (8)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property DefaultWTs() As TaxCodeDeterminationTCDDefaultWTs` [R] property DefaultWTs
- `Public Property DispOrder() As Long` [R/W] property DispOrder
- `Public Property Periods() As TaxCodeDeterminationTCDPeriods` [R] property Periods
- `Public Property Value1() As String` [R/W] property Value1
- `Public Property Value2() As String` [R/W] property Value2
- `Public Property Value3() As String` [R/W] property Value3
- `Public Property Value4() As String` [R/W] property Value4

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxCodeDeterminationTCDValues (Collection)

TaxCodeDeterminationTCDValues Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As TaxCodeDeterminationTCDValue` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TaxCodeDeterminationTCDValue` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxDefinitions (Object)

A set of tax rates for different time periods for a particular sales tax jurisdiction. Source table: STA1

**Remarks:** For the United States and Canada only.

## Properties (3)
- `Public Property Effectivefrom() As Date` [R/W] The date from which the tax rate in the Rate property is in effect. This value must be unique within the TaxDefinitions collection. Field name: EfctDate
- `Public Property Rate() As Double` [R/W] The tax rate for the period starting from the date specified in the Effectivefrom property. Field name: Rate
- `Public Property UserFields() As UserFields` [R] property UserFields

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

# TaxExtension (Object)

TaxExtension is a child object of the Documents object. It stores fiscal IDs of marketing documents. Every marketing document has a set of fiscal IDs. The TaxExtension object is applicable for cluster B (country-specific for Brazil and India). Source tables: CPI12, CPV12, CSI12, CSV12, DLN12, DRF12, IGE12, IGN12, INV12, PCH12, PDN12, POR12, QUT12, RDN12, RDR12, RIN12, RPC12, RPD12, and WTR12.

**Remarks:** To display the form in the application: - Select a marketing document. - Select the Tax tab. - Click the Fiscal IDs button.

## Properties (58)
- `Public Property BillOfEntryDate() As Date` [R/W] property BillOfEntryDate
- `Public Property BillOfEntryNo() As String` [R/W] property BillOfEntryNo
- `Public Property BlockB() As String` [R/W] Sets or returns the block of the bill-to address.
- `Public Property BlockS() As String` [R/W] Sets or returns the block of the ship-to address.
- `Public Property BoEValue() As Double` [R/W] property BoEValue
- `Public Property Brand() As String` [R/W] Sets or returns the brand fiscal Id. Field name: Brand. Length: 20 characters.
- `Public Property BuildingB() As String` [R/W] Sets or returns the Building of the bill-to address.
- `Public Property BuildingS() As String` [R/W] Sets or returns the Building of the ship-to address. Field name: Building.
- `Public Property Carrier() As String` [R/W] Sets or returns the carrier code. Field name: Carrier. Length: 15 characters.
- `Public Property CityB() As String` [R/W] Sets or returns the Building of the bill-to address.
- `Public Property CityS() As String` [R/W] Sets or returns the City of the ship-to address.
- `Public Property ClaimRefund() As BoYesNoEnum` [R/W] property ClaimRefund
- `Public Property CountryB() As String` [R/W] Sets or returns the Country of the bill-to address.
- `Public Property CountryS() As String` [R/W] Sets or returns the Country of the ship-to address.
- `Public Property County() As String` [R/W] Sets or returns the county code. Field name: County. Length: 7 characters.
- `Public Property CountyB() As String` [R/W] Sets or returns the County of the bill-to address.
- `Public Property CountyS() As String` [R/W] Sets or returns the County of the Ship-to address.
- `Public Property DifferentialOfTaxRate() As Long` [R/W] property DifferentialOfTaxRate
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property GlobalLocationNumberB() As String` [R/W] property GlobalLocationNumberB
- `Public Property GlobalLocationNumberS() As String` [R/W] property GlobalLocationNumberS
- `Public Property GrossWeight() As Double` [R/W] Sets or returns the gross weight.
- `Public Property ImportOrExport() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether the Sales Tax Invoice is for import or export. Applicable for cluster B (country-specific for India). Field name: ImpOrExp (INV12).
- `Public Property ImportOrExportType() As ImportOrExportTypeEnum` [R/W] property ImportOrExportType
- `Public Property Incoterms() As String` [R/W] Sets or returns the Internationally Accepted Commerce terms. Field name: Incoterms. Length: 3 characters.
- `Public Property IsIGSTAccount() As BoYesNoEnum` [R/W] property IsIGSTAccount
- `Public Property MainUsage() As Long` [R/W] property MainUsage
- `Public Property NetWeight() As Double` [R/W] Sets or returns the net weight. Field name: NetWeight.
- `Public Property NFRef() As String` [R/W] Sets or returns the NF reference. Field name: NfRef.
- `Public Property OriginalBillOfEntryDate() As Date` [R/W] property OriginalBillOfEntryDate
- `Public Property OriginalBillOfEntryNo() As String` [R/W] property OriginalBillOfEntryNo
- `Public Property PackDescription() As String` [R/W] Sets or returns the pack description. Field name: PackDesc.
- `Public Property PackQuantity() As Long` [R/W] Sets or returns the quantity of packs. Field name: QoP.
- `Public Property PortCode() As String` [R/W] property PortCode
- `Public Property ShipUnitNo() As Long` [R/W] Sets or returns the number of shipping unit. Field name: NoSU.
- `Public Property State() As String` [R/W] Sets or returns the state code. Field name: State. Length: 3 characters.
- `Public Property StateB() As String` [R/W] Sets or returns the Building of the bill-to address.
- `Public Property StateS() As String` [R/W] Sets or returns the State of the bill-to address.
- `Public Property StreetB() As String` [R/W] Sets or returns the Street of the bill-to address.
- `Public Property StreetS() As String` [R/W] Sets or returns the Street of the Ship-to address.
- `Public Property TaxId0() As String` [R/W] Sets or returns the CNPJ code (country-specific to Brazil). Field name: TaxId0. Length: 100 characters.
- `Public Property TaxId1() As String` [R/W] Sets or returns the I.E. (country-specific to Brazil). Field name: TaxId1. Length: 100 characters.
- `Public Property TaxId12() As String` [R/W] Tax ID 12. Field name: TaxId12. Length: 50 characters.
- `Public Property TaxId13() As String` [R/W] Deductee Ref. No. in India. Field name: TaxId13. Length: 100 characters.
- `Public Property TaxId14() As String` [R/W] ITR Filing. Field name: TaxId14. Length: 250 characters.
- `Public Property TaxId2() As String` [R/W] Sets or returns the I.E.S.T (country-specific to Brazil). Field name: TaxId2. Length: 100 characters.
- `Public Property TaxId3() As String` [R/W] Sets or returns the I.M. (country-specific to Brazil). Field name: TaxId3. Length: 100 characters.
- `Public Property TaxId4() As String` [R/W] Sets or returns the CPF code (country-specific to Brazil). Field name: TaxId4. Length: 100 characters.
- `Public Property TaxId5() As String` [R/W] Sets or returns the Foreigner ID (country-specific to Brazil). Field name: TaxId5. Length: 100 characters.
- `Public Property TaxId6() As String` [R/W] Sets or returns the Foreigner description (country-specific to Brazil). Field name: TaxId6. Length: 100 characters.
- `Public Property TaxId7() As String` [R/W] Sets or returns the INSS Inscription (country-specific to Brazil). Field name: TaxId7. Length: 100 characters.
- `Public Property TaxId8() As String` [R/W] Sets or returns the Suframa (country-specific to Brazil). Field name: TaxId8. Length: 100 characters.
- `Public Property TaxId9() As String` [R/W] Reserved. Field name: TaxId9. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Vehicle() As String` [R/W] Sets or returns the vehicle ID. Field name: Vehicle. Length: 10 characters.
- `Public Property VehicleState() As String` [R/W] Sets or returns the state of the vehicle ID. Field name: VidState. Length: 3 characters.
- `Public Property ZipCodeB() As String` [R/W] Sets or returns the Zip Code of the bill-to address.
- `Public Property ZipCodeS() As String` [R/W] Sets or returns the Zip Code part of the Ship-to address.

# TaxInvoice_DocumentReferences (Object)

TaxInvoice_DocumentReferences Class

## Properties (10)
- `Public Property CardCode() As String` [R/W] property CardCode
- `Public Property Count() As Long` [R] property Count
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExternalReferencedDocNumber
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ReferencedDocEntry() As Long` [R/W] property ReferencedDocEntry
- `Public Property ReferencedDocNumber() As Long` [R] property ReferencedDocNumber
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property ReferencedObjectType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# TaxInvoice_Lines (Object)

TaxInvoice_Lines is a child object of the TaxInvoices object that represents the line entries of each tax invoice document. Source table: TSI1 for sales invoices, TPI1 for purchase invoices, or TXD1 for journal entry.

**Remarks:** Country-specific for Russia.

## Properties (6)
- `Public Property BaseEntry() As Long` [R] Returns the key of the source document. Field name: BaseEntry.
- `Public Property BaseType() As BoTaxInvoiceTypes` [R] Returns a valid value of BoTaxInvoiceTypes type that specifies the type of the base document: Invoice, Payment, or Journal Entry. Field name: DocType.
- `Public Property Count() As Long` [R] Returns the total data rows in the table.
- `Public Property LineNum() As Long` [R] Returns the row number. Field name: LineNum.
- `Public Property Reference() As Long` [R/W] Sets or returns the key of the referenced document. Field name: RefEntry1.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0. Specifies the row number. The count starts from 0.

# TaxInvoice_LinkedDownPayments (Object)

Link to tax invoices from down payments for Russia localization. The whole "Linked Down Payments" subobject is read-only, meaning it is completed automatically during the adding of Tax Invoices (no matter if via UI or DI) and user can read the values via DI API using this subobject (LinkedDownPayments). Source table: TSI4 for A/R tax invoices, TPI4 for A/P tax invoices.

**Remarks:** Sales - A/R -> A/R Tax Invoice -> option Down Payments Purchasing - A/P -> A/P Tax Invoice -> option Down Payments

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.TaxInvoices taxInvoice = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oSalesTaxInvoice) as SAPbobsCOM.TaxInvoices;
                  taxInvoice.GetByKey(1);
                  SAPbobsCOM.TaxInvoice_LinkedDownPayments taxInvoiceDPMs = taxInvoice.LinkedDownPayments;
                  if (taxInvoiceDPMs.Count < 1)
                  {
                      Console.WriteLine(""no linked down payments found"");
                  }
                  else
                  {
                      Console.WriteLine(""count: "" + taxInvoiceDPMs.Count);
                      for (int line = 0; line < taxInvoiceDPMs.Count; line++)
                      {
                          taxInvoiceDPMs.SetCurrentLine(line);
                          Console.WriteLine(""line "" + (line + 1) + "":"");
                          Console.WriteLine("" DocEntry: "" + taxInvoiceDPMs.DocEntry);
                          Console.WriteLine("" LineNum: "" + taxInvoiceDPMs.LineNum);
                          Console.WriteLine("" DownPaymentType: "" + taxInvoiceDPMs.DownPaymentType);
                          Console.WriteLine("" DownPaymentEntry: "" + taxInvoiceDPMs.DownPaymentEntry;
                          Console.WriteLine("" DownPaymentNum: "" + taxInvoiceDPMs.DownPaymentNum);
                          Console.WriteLine("" PaymentType: "" + taxInvoiceDPMs.PaymentType);
                          Console.WriteLine("" PaymentEntry: "" + taxInvoiceDPMs.PaymentEntry;
                          Console.WriteLine("" PaymentNum: "" + taxInvoiceDPMs.PaymentNum);
                          Console.WriteLine("" PaymentTaxDate: "" + taxInvoiceDPMs.PaymentTaxDate);
                          Console.WriteLine("" TransferDate: "" + taxInvoiceDPMs.TransferDate);
                          Console.WriteLine("" TransferReference: "" + taxInvoiceDPMs.TransferReference;
                          Console.WriteLine("" AmountToDraw: "" + taxInvoiceDPMs.AmountToDraw);
                          Console.WriteLine("" AmountToDrawFC: "" + taxInvoiceDPMs.AmountToDrawFC);
                          Console.WriteLine("" AmountToDrawSC: "" + taxInvoiceDPMs.AmountToDrawSC);
                          Console.WriteLine("" DocCurrency: "" + taxInvoiceDPMs.DocCurrency);
                      }
                  }
  ```

## Properties (22)
- `Public Property AmountToDraw() As Double` [R] The amount of the down payment that is used. Field name: DrawnSum.
- `Public Property AmountToDrawFC() As Double` [R] The amount of the down payment that is used in foreign currency. Field name: DrawnSumFc.
- `Public Property AmountToDrawSC() As Double` [R] The amount of the down payment that is used in system currency. Field name: DrawnSumSc.
- `Public Property Count() As Long` [R] Number of records in a LinkedDownPayments collection.
- `Public Property DocCurrency() As String` [R] Document currency code (руб, EUR). Field name: DocCur.
- `Public Property DocEntry() As Long` [R] Absolute ID of the current Tax Invoice. Field name: DocEntry.
- `Public Property DownPaymentEntry() As Long` [R] Down payment entry. (203: A/R Down Payment, 204: A/P Down Payment); on UI just the Document Number is visible with link arrow to DPM called "Down Payment No." Field name: DpmDocEntr.
- `Public Property DownPaymentNum() As Long` [R] Down payment number. (203: A/R Down Payment, 204: A/P Down Payment); on UI just the Document Number is visible with link arrow to DPM called "Down Payment No." Field name: DpmDocNum.
- `Public Property DownPaymentType() As Long` [R] Down payment object type. (203: A/R Down Payment, 204: A/P Down Payment); on UI just the Document Number is visible with link arrow to DPM called "Down Payment No." Field name: DpmObjType.
- `Public Property GrossAmountToDraw() As Double` [R] The gross amount of the down payment that is used. Field name: Gross.
- `Public Property GrossAmountToDrawFC() As Double` [R] The gross amount of the down payment that is used in foreign currency. Field name: GrossFc.
- `Public Property GrossAmountToDrawSC() As Double` [R] The gross amount of the down payment that is used in system currency. Field name: GrossSc.
- `Public Property LineNum() As Long` [R] Line number in a LinkedDownPayments collection. Field name: LineNum.
- `Public Property PaymentEntry() As Long` [R] Payment entry. (24: Incoming Payment, 46: Outgoing Payment); on UI just the Document Number is visible with link arrow to Payment called "Payment No." Field name: PmnDocEntr.
- `Public Property PaymentNum() As Long` [R] Payment number. (24: Incoming Payment, 46: Outgoing Payment); on UI just the Document Number is visible with link arrow to Payment called "Payment No." Field name: PmnDocNum.
- `Public Property PaymentTaxDate() As Date` [R] Date of payment. Field name: PmnTaxDate.
- `Public Property PaymentType() As Long` [R] Type of payment object. (24: Incoming Payment, 46: Outgoing Payment); on UI just the Document Number is visible with link arrow to Payment called "Payment No." Field name: PmnObjType.
- `Public Property Tax() As Double` [R] Tax amount. Field name: Vat.
- `Public Property TaxFC() As Double` [R] Tax amount in foreign currency. Field name: VatFc.
- `Public Property TaxSC() As Double` [R] Tax amount in system currency. Field name: VatSc.
- `Public Property TransferDate() As Date` [R] Date of transfer. Copied from the payment of the linked DPM, when using Bank Transfer payment method. Field name: TrsfrDate.
- `Public Property TransferReference() As String` [R] Reference of transfer. Copied from the payment of the linked DPM, when using Bank Transfer payment method. Field name: TrsfrRef.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# TaxInvoice_OperationCodes (Object)

TaxInvoice_OperationCodes is a child object of the TaxInvoices object that represents the operation codes of the tax invoice document.

## Properties (5)
- `Public Property BaseEntry() As Long` [R] Document key of tax invoice. Same as DocEntry of TaxInvoices object.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property LineNum() As Long` [R/W] Obsolete. Do not use anymore.
- `Public Property OpCode() As Long` [R/W] The operation code.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# TaxInvoiceReport (Object)

TaxInvoiceReport Class

## Properties (16)
- `Public Property BaseAmount() As Double` [R] property BaseAmount
- `Public Property BPCode() As String` [R] property BPCode
- `Public Property BPName() As String` [R] property BPName
- `Public Property BusinessPlace() As Long` [R] property BusinessPlace
- `Public Property Canceled() As String` [R] property Canceled
- `Public Property Date() As Date` [R] property Date
- `Public Property ETaxNo() As String` [R/W] property ETaxNo
- `Public Property ETaxWebSite() As Long` [R/W] property ETaxWebSite
- `Public Property NTSApproval() As TaxInvoiceReportNTSApprovedEnum` [R/W] property NTSApproval
- `Public Property NTSApprovalNo() As String` [R/W] property NTSApprovalNo
- `Public Property OriginalNTSApprovalNo() As String` [R/W] property OriginalNTSApprovalNo
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property ReportType() As Long` [R] property ReportType
- `Public Property TaxAmount() As Double` [R] property TaxAmount
- `Public Property TaxInvoiceReportLineCollection() As TaxInvoiceReportLineCollection` [R] property TaxInvoiceReportLineCollection
- `Public Property TaxInvoiceReportNumber() As String` [R] property TaxInvoiceReportNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxInvoiceReportLine (Object)

TaxInvoiceReportLine Class

## Properties (18)
- `Public Property BaseAmount() As Double` [R] property BaseAmount
- `Public Property BPCode() As String` [R] property BPCode
- `Public Property BPName() As String` [R] property BPName
- `Public Property BusinessPlace() As Long` [R] property BusinessPlace
- `Public Property Currency() As String` [R] property Currency
- `Public Property DocumentDate() As Date` [R] property DocumentDate
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property DocumentType() As Long` [R] property DocumentType
- `Public Property ItemDescription() As String` [R] property ItemDescription
- `Public Property ItemNo() As String` [R] property ItemNo
- `Public Property ItemPrice() As Double` [R] property ItemPrice
- `Public Property ItemQuantity() As Double` [R] property ItemQuantity
- `Public Property Legacy() As String` [R] property Legacy
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property LineType() As TaxInvoiceReportLineTypeEnum` [R] property LineType
- `Public Property TaxAmount() As Double` [R] property TaxAmount
- `Public Property TaxCode() As String` [R] property TaxCode
- `Public Property TaxInvoiceReportNumber() As String` [R] property TaxInvoiceReportNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxInvoiceReportLineCollection (Collection)

TaxInvoiceReportLineCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TaxInvoiceReportLine` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TaxInvoiceReportLine` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxInvoiceReportParams (Object)

TaxInvoiceReportParams Class

## Properties (1)
- `Public Property TaxInvoiceReportNumber() As String` [R/W] property TaxInvoiceReportNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxInvoiceReportService (Object)

TaxInvoiceReportService Class

## Methods (6)
- `Public Sub CancelTaxInvoiceReport(ByVal pITaxInvoiceReportParams As TaxInvoiceReportParams)` CancelTaxInvoiceReport
  - param `pITaxInvoiceReportParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TaxInvoiceReportServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TaxInvoiceReportServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTaxInvoiceReport(ByVal pITaxInvoiceReportParams As TaxInvoiceReportParams) As TaxInvoiceReport` GetTaxInvoiceReport
  - param `pITaxInvoiceReportParams`: 
- `Public Sub UpdateTaxInvoiceReport(ByVal pITaxInvoiceReport As TaxInvoiceReport)` UpdateTaxInvoiceReport
  - param `pITaxInvoiceReport`: 

# TaxInvoices (Object)

TaxInvoices is a business object that represents the header data of a Tax Invoice document. Source table: OTSI for sales invoices, OTPI for purchase invoices, or OTXD for journal entry according to the DocType valid value.

**Remarks:** Country-specific for Russia.

## Properties (36)
- `Public Property Address() As String` [R/W] Sets or returns the Bill To address. Field name: Address. Length: 254 characters.
- `Public Property Address2() As String` [R/W] Sets or returns the alternative Ship To address. Field name: Address2. Length: 254 characters.
- `Public Property AlterationRevision() As Long` [R/W] property AlterationRevision
- `Public Property BPLID() As Long` [R] property BPLID
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object. Returns the DataBrowser object.
- `Public Property CancelDate() As Date` [R] Returns the Cancel Date of the tax invoice . Field name: CancelDate. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner Customer Code. Field name: CardCode. This is a foreign key to the BusinessPartners object. Mandatory field in SAP Business One. Length: 15 characters.
- `Public Property Comments() As String` [R/W] Sets or returns the Remarks regarding the tax invoice document. Field name: Comments. Length: 254 characters.
- `Public Property ContactPersonCode() As Long` [R/W] Sets or returns the contact person code. Field name: CntctCode. This is a foreign key to the ContactEmployees object.
  - remarks: The contact employee codes are defined through the ContactEmployees object (foreign key linked to OCPR table).
- `Public Property CreationDate() As Date` [R] Returns the creation date of the tax invoice document. Field name: CreateDate.
- `Public Property CurrencySource() As BoCurrencySources` [R/W] Sets or returns a valid value of BoCurrencySources type that specifies the currency source: - L - local - S - system - C - customer (business partner, default) Field name: CurSource.
- `Public Property CustomerOrVendorName() As String` [R/W] Sets or returns a string that specifies the business partner's full name. Field name: CardName. Length: 100 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
  - remarks: The default value is retrieved from CardName property of the BusinessPartners object.
- `Public Property CustomerOrVendorRefNo() As String` [R/W] Sets or returns a string that specifies the business partner's Reference number. Field name: NumAtCard. Length: 16 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property DocCurrency() As String` [R/W] Sets or returns the currency used in this document. Field name: DocCur. Length: 3 characters.
- `Public Property DocDate() As Date` [R/W] Sets or returns the document posting date. Field name: DocDate.
- `Public Property DocDueDate() As Date` [R/W] Sets or returns the document value date. Field name: DocDueDate.
- `Public Property DocEntry() As Long` [R] Returns the document key. Field name: DocEntry.
- `Public Property DocNum() As Long` [R] Returns the document number. Field name: DocNum.
- `Public Property DocType() As BoTaxInvoiceTypes` [R/W] Sets or returns a valid value of BoTaxInvoiceTypes that specifies the document type of the tax invoice. Field name: DocType.
- `Public Property DocumentReferences() As TaxInvoice_DocumentReferences` [R] Returns TaxInvoice_DocumentReferences child object.
- `Public Property DocumentTotal() As Double` [R] Sets or returns the Document Total value in document currency. Field name: DocTotal.
  - remarks: The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property Lines() As TaxInvoice_Lines` [R] Returns TaxInvoice_Lines child object.
- `Public Property LinkedDownPayments() As TaxInvoice_LinkedDownPayments` [R] Returns TaxInvoice_LinkedDownPayments child object.
- `Public Property OperationCodes() As TaxInvoice_OperationCodes` [R] Returns TaxInvoice_OperationCodes child object.
- `Public Property PaymentRefDate() As Date` [R/W] Sets or returns the Payment Ref. Date. Field name: PayRefDate. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property PaymentRefNo() As String` [R/W] Sets or returns a string that specifies the the payment document number. Field name: PayRefNo. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property Printed() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not this tax invoice document was printed. Field name: Printed.
- `Public Property Segment() As Long` [R] Returns the segment number of the tax invoice document. Field name: Segment.
  - remarks: Default: 0.
- `Public Property Series() As Long` [R/W] Returns the auto-numbering series that generated the document number. Field name: Series.
  - remarks: Default: 0.
- `Public Property ShipToCode() As String` [R/W] Sets or returns the Ship To address name. Field name: ShipToCode. Length: 50 characters.
  - remarks: For sales documents, the value is retrieved from the business partner record. This address name can be updated only for open sales documents. For purchase documents, the value is retrieved from the company record.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the document VAT date. Field name: VatDate.
- `Public Property TaxTotal() As Double` [R] Returns a double integer that specifies the Tax Total amount in document currency. Field name: VatSum.
  - remarks: The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property UpdateDate() As Date` [R] Returns the document last update date. Field name: UpdateDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VATRegNum() As String` [R] property VATRegNum

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database. Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
  - example note: The following sample shows how to add an invoice (with lines) document to the database. Use this sample as a basis for all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub AddInvoice_Click()

        Dim RetVal As Long

        Dim ErrCode As Long

        Dim ErrMsg As String

        'Create the Documents object

        Dim vInvoice    As SAPbobsCOM.Documents

        Set vInvoice = vCmp.GetBusinessObject(oInvoices)

        'Set values to the fields

        vInvoice.Series = 0

        vInvoice.CardCode = "BP234"

        vInvoice.HandWritten = tNO

        vInvoice.PaymentGroupCode = "-1"

        vInvoice.DocDate = "21/8/2003"

        vInvoice.DocTotal = 264.6

        'Invoice Lines - Set values to the first line

        vInvoice.Lines.ItemCode = "A00023"

        vInvoice.Lines.ItemDescription = "Banana"

        vInvoice.Lines.PriceAfterVAT = 2.36

        vInvoice.Lines.Quantity = 50

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Invoice Lines - Set values to the second line

        vInvoice.Lines.Add

        vInvoice.Lines.ItemCode = " A00033"

        vInvoice.Lines.ItemDescription = "Orange"

        vInvoice.Lines.PriceAfterVAT = 118

        vInvoice.Lines.Quantity = 1

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Add the Invoice

        RetVal = vInvoice.Add

       'Check the result

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox ErrCode & " " & ErrMsg

        End If

     End Sub
    ```
- `Public Function Cancel() As Long` Cancels a record from the object table. Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal DocEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from SAP Business One database. Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `DocEntry`: Document key (DocEntry).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data. Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data. Saves the object data to XML formatted data.
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
- `Public Function Update() As Long` Updates the object data in the SAP Business One company database. Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# TaxJurisdictions (Object)

Represents the tax amount of a document. Source table: PCH4. TaxJurisdictions is a child object of the following existing objects: - Document_Lines object (Source table: PCH1) - Document_LinesAdditionalExpenses object (Source table: PCH2) - DocumentsAdditionalExpenses object (Source table: PCH3)

**Example:**
- C# example (from SAP's help):
  ```csharp
  oc.CardCode = "C20000";
              doc.DocDate = DateTime.Today;
              doc.DocDueDate = DateTime.Today;
              doc.Lines.ItemCode = "A00001";
              doc.Lines.Quantity = 2;
              doc.Lines.UnitPrice = 100;
              doc.Lines.TaxCode = "1101-001";

             // Set Line Freight External Tax
              doc.Lines.Expenses.ExpenseCode = 2;
              doc.Lines.Expenses.LineTotal = 100;
              doc.Lines.Expenses.TaxCode = "1101-005";
              doc.Lines.Expenses.TaxJurisdictions.Add();
              doc.Lines.Expenses.TaxJurisdictions.SetCurrentLine(0);
              doc.Lines.Expenses.TaxJurisdictions.JurisdictionCode = "IC18BT01";
              doc.Lines.Expenses.TaxJurisdictions.JurisdictionType = 10;
              doc.Lines.Expenses.TaxJurisdictions.ExternalCalcTaxAmount = 20;
              doc.Lines.Expenses.TaxJurisdictions.ExternalCalcTaxRate = 6;

              doc.Lines.Expenses.TaxJurisdictions.Add();
              doc.Lines.Expenses.TaxJurisdictions.SetCurrentLine(1);
              doc.Lines.Expenses.TaxJurisdictions.JurisdictionCode = "IP15BT01";
              doc.Lines.Expenses.TaxJurisdictions.JurisdictionType = 16;
              doc.Lines.Expenses.TaxJurisdictions.ExternalCalcTaxAmount = 50;
              doc.Lines.Expenses.TaxJurisdictions.ExternalCalcTaxRate = 2;
              doc.Add();
  ```

## Properties (15)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalCalcTaxAmount() As Double` [R/W] The external calculated tax amount, in local currency. Field name: ExtTaxSum.
- `Public Property ExternalCalcTaxAmountFC() As Double` [R/W] Returns the external calculated tax amount, in foreign currency. Field name: ExtTaxSumF.
- `Public Property ExternalCalcTaxAmountSC() As Double` [R] Returns the external calculated tax amount, in system currency. Field name: ExtTaxSumS.
- `Public Property ExternalCalcTaxRate() As Double` [R/W] External calculated tax rate. Field: ExtTaxRate.
- `Public Property JurisdictionCode() As String` [R/W] The jurisdiction tax code. Field: StaCode. Length: 8 characters.
- `Public Property JurisdictionType() As Long` [R/W] The type of the jurisdiction tax code. Field: staType.
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property RowSequence() As Long` [R] property RowSequence
- `Public Property TaxAmount() As Double` [R/W] The tax amount, in local currency, calculated for the transaction. You can manually adjust the tax amount according to the business need. Field name: TaxSum.
- `Public Property TaxAmountFC() As Double` [R] Returns the tax amount, in foreign currency, calculated for the transaction. Field name: TaxSumFrgn.
- `Public Property TaxAmountSC() As Double` [R] Returns the total tax amount, in system currency, calculated for the transaction. Field name: TaxSumSys.
- `Public Property TaxRate() As Double` [R] The rate of the jurisdiction tax. Field: TaxRate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# TaxReplStateSubData (Object)

Tax replacement state subscription data. In Brazil companies associate state code with IEST code. Source table: OTRSS.

**Remarks:** Administration -> System Initialization -> Company Details -> Localization Fields tab.

## Properties (2)
- `Public Property IEST() As String` [R/W] Brazil IEST code. Field name: IEST. Length: 14 characters.
- `Public Property State() As String` [R/W] Brazil state code. Field name: State. Length: 3 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TaxReplStateSubParams (Object)

Holds the key to existing tax replacement state subscription data. This object is used to pass keys to and retrieve keys from TaxReplStateSubService methods.

## Properties (1)
- `Public Property State() As String` [R/W] Brazil state code. Field name: State. Length: 3 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TaxReplStateSubService (Object)

The TaxReplStateSubService service enables you to add, look up, update, and remove tax replacement state subscription. Source table: OTRSS.

**Remarks:** Administration -> System Initialization -> Company Details -> Localization Fields tab.

## Methods (7)
- `Public Function Add(ByVal pITaxReplStateSubData As TaxReplStateSubData) As TaxReplStateSubParams` Adds tax replacement state subscription data.
  - param `pITaxReplStateSubData`: The tax replacement state subscription data.
- `Public Sub Delete(ByVal pITaxReplStateSubParams As TaxReplStateSubParams)` Deletes existing tax replacement state subscription data.
  - param `pITaxReplStateSubParams`: The key of the tax replacement state subscription data to be deleted.
- `Public Function GetByParams(ByVal pITaxReplStateSubParams As TaxReplStateSubParams) As TaxReplStateSubData` Retrieves tax replacement state subscription data. The tax replacement state subscription data is specified by its key, which is contained in the TaxReplStateSubParams object passed to the method.
  - param `pITaxReplStateSubParams`: The key of the tax replacement state subscription data to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As TaxReplStateSubServiceDataInterfaces) As Object` Creates an empty data structure for use with the TaxReplStateSubService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TaxReplStateSubServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Sub Update(ByVal pITaxReplStateSubData As TaxReplStateSubData)` Updates existing tax replacement state subscription data.
  - param `pITaxReplStateSubData`: The tax replacement state subscription data to be updated. The TaxReplStateSubData object must contain the key of the object to be updated.

# TaxReportAccount (Object)

TaxReportAccount is a data structure related to the TaxReportsService. Source table: VTR5.

## Properties (1)
- `Public Property Code() As String` [R/W] Sets or returns the tax report group object code. Field name: ObjectCode.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportAccounts (Collection)

TaxReportAccounts is a Data Collection of TaxReportAccount data structures. Source table: VTR5.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportAccount data structures in the TaxReportAccounts data collection.

## Methods (5)
- `Public Function Add() As TaxReportAccount` Adds a new TaxReportAccount to the TaxReportAccounts data collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportAccount` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportBusinessPartner (Object)

TaxReportBusinessPartner is a data structure related to the TaxReportsService.

## Properties (1)
- `Public Property Code() As String` [R/W] Sets or returns the tax report business partner code. Field name: ObjectCode.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportBusinessPartners (Collection)

TaxReportBusinessPartners is a Data Collection of TaxReportBusinessPartner data structures. Source table: VTR4. Remark: VTR4 is a virtual table and not exposed in the database reference files.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportBusinessPartner data structures in the TaxReportBusinessPartners data collection.

## Methods (5)
- `Public Function Add() As TaxReportBusinessPartner` Adds a new TaxReportBusinessPartner to the TaxReportBusinessPartners data collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportBusinessPartner` Returns reference to existing TaxReportBusinessPartner in the collection by its index.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportDocument (Object)

TaxReportDocument is a data structure related to the TaxReportsService. Source table: VTR2.

## Properties (3)
- `Public Property DocumentType() As TaxReportFilterDocumentType` [R/W] Sets or returns a valid value that determines Document Type . Field name: ObjectCode.
- `Public Property FromNumber() As Long` [R/W] Sets or returns the from document number. Field name: FromDocNo.
- `Public Property ToNumber() As Long` [R/W] Sets or returns the to document number. Field name: ToDocNo.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportDocuments (Collection)

TaxReportDocuments is a Data Collection of TaxReportDocument data structures. Source table: VTR2.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportDocument data structures in the TaxReportDocuments data collection.

## Methods (5)
- `Public Function Add() As TaxReportDocument` Adds a new TaxReportDocument to the TaxReportDocuments data collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportDocument` Returns reference to existing TaxReportDocument item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
