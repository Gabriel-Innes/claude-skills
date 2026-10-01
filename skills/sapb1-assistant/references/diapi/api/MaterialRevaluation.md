<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MaterialRevaluation (Object)

MaterialRevaluation is a business object that enables you to update the items' price (average price or standard price only), revaluate the stock, and create journal entries accordingly. This object applies only to companies that manage their stock using Continuous Stock system. This object enables you to: - Add a material revaluation. - Retrieve a material revaluation by its key. - Update a material revaluation. - Save the object in XML format. Source table: OMRV.

## Properties (25)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] property CardCode
- `Public Property CardName() As String` [R/W] property CardName
- `Public Property Comments() As String` [R/W] Sets or returns comments for the document. Field name: Comments. Length: 254 characters.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property CreationDate() As Date` [R] Returns the creation date of the document. Field name: CreateDate.
  - remarks: This property is internal in SAP Business One.
- `Public Property DataSource() As String` [R] Not used. Field name: DataSource.
- `Public Property DocDate() As Date` [R/W] Sets or returns the document posting date. Field name: DocDate.
  - remarks: The default is the current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocEntry() As Long` [R] Returns the document entry key that uniquely identifies the document. Field name: DocEntry.
- `Public Property DocNum() As Long` [R] Sets or returns the number of the document. Field name: DocNum.
  - remarks: and also verify Relevant to sales documents only. In case the value of the HandWritten property is tNO and you add a sales document, SAP Business One automatically assigns the next available number to the document, in accordance with the document numbering system defined during system configuration. When saving the document as a draft, this number is stored for the document draft only. So that the number of the draft is still available in the system for other new documents. The system may assign this number to a new document of the same type. When saving the draft as a document, SAP Business One assigns a new available number. In case the value of the HandWritten property is tYES, set a value (greater than 0) to the DocNum property and also set the Series property to -1.
- `Public Property DocTime() As Date` [R] Sets or returns the document creation time. Field name: DocTime.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocumentReferences() As MaterialRevaluationDocumentReferences` [R] property DocumentReferences
- `Public Property InflationRevaluation() As BoYesNoEnum` [R/W] Specify whether to record inflation as the reason for this revaluation. You can then filter out inflation-based revaluations in the inventory valuation simulation report. Field: InflaReval.
  - remarks: It is a requirement of IFRS not to include inflation-based revaluations in inventory valuation.
- `Public Property JournalMemo() As String` [R/W] Sets or returns the journal entry remarks that is copied later to the accounting document. Field name: JrnlMemo. Length: 50 characters.
  - remarks: SAP Business One, by default, automatically enters the document type and the business partner number. When using the system's default template for printing, the remark is not printed on the associated document. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Lines() As MaterialRevaluation_lines` [R] Returns the MaterialRevaluation_lines child object.
- `Public Property Reference1() As String` [R] P>Sets or returns the first reference code of the document. Field name: Ref1. Length: 11 characters.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Reference2() As String` [R/W] Sets or returns the second reference code of the document. Field name: Ref2. Length: 11 characters.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property RevalType() As String` [R/W] Sets or returns the revaluation type: price change or material debit/credit. Field name: RevalType. Length: 1 character.
- `Public Property RevaluationExpenseAccount() As String` [R/W] Sets or returns the revaluation expense account code. Field name: RExpnAcct. Length: 15 characters.
- `Public Property RevaluationIncomeAccount() As String` [R/W] Sets or returns the revaluation income account code. Field name: RIncmAcct. Length: 15 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TransNum() As Long` [R] Returns the transaction number that SAP Business One creates for the document. Field name: TransId. This is a foreign key to the JournalEntries object.
- `Public Property UpdateDate() As Date` [R] Returns the date when the material revaluation was last updated. Field name: UpdateDate.
  - remarks: Internal property in SAP Business One.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who created the document. Field name: UserSign.

## Methods (9)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
- `Public Function Cancel() As Long` Not supported.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal AbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `AbsEntry`: Specifies the document entry key (see DocEntry property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Save object as XML document
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
