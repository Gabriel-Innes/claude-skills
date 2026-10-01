<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# KnowledgeBaseSolutions (Object)

KnowledgeBaseSolutions is a business object that represents the knowledge base solutions in the Service module. This object enables you to: - Add a solution to the knowledge base. - Retrieve a solution from the knowledge base by its key. - Update a solution in the knowledge base. - Remove a solution from the knowledge base. - Save the object in XML format. Source table: OSLT.

**Remarks:** Mandatory field in SAP Business One: Solution. To display the form in the application: - Select Service --> Knowledgebase Solutions.

## Properties (16)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry. Field name: AtcEntry. Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Cause() As String` [R/W] Sets or returns the origin of the problem. Field name: Cause. Length: 254 characters.
- `Public Property CreatedBy() As Long` [R] Returns the name or title of the employee who created the solution. Field name: CreatedBy. This is a foreign key to the Users object.
- `Public Property CreationDate() As Date` [R] Returns the creation date of the solution. Field name: DateCreate.
  - remarks: This property is internal in SAP Business One.
- `Public Property Description() As String` [R/W] Sets or returns a memo type string that specifies additional details for the problem cause. Field name: Descriptio. Length: 64,000 characters.
- `Public Property ItemCode() As String` [R/W] Sets or returns the code (unique) of the item used for solving the problem. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property LastUpdateDate() As Date` [R] Returns the last date when the solution was updated. Field name: DateUpdate.
- `Public Property LastUpdatedBy() As Long` [R] Returns the name or title of the employee who last updated the solution in the knowledge base. Field name: UpdateBy. This is a foreign key to the Users object.
- `Public Property Owner() As Long` [R] Returns the name or title of the employee who is the owner of solution in the knowledge base. Field name: UpdateBy. This is a foreign key to the Users object.
- `Public Property Solution() As String` [R/W] Sets or returns the description of the solution to the problem. Field name: Subject. Length: 254 characters.
  - remarks: Mandatory property.
- `Public Property SolutionCode() As Long` [R] Returns the solution number. Field name: SltCode.
- `Public Property Status() As Long` [R/W] Sets or returns the status of the solution (for example: published, internal, or review). Field name: StatusNum. This is a foreign key to the Service Call Solution Statuses table (OSST), not exposed through the DI API).
- `Public Property Symptom() As String` [R/W] Sets or returns the indications of the problem. Length: 254 characters. Field name: Symptom.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal SolutionCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `SolutionCode`: Specifies the identification code of the knowledge base solution in the database.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
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
