<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserQueries (Object)

The UserQueries object enables to define user queries in the Queries Manager. Source table: OUQR.

## Properties (14)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property EnableMenuEntry() As BoYesNoEnum` [R/W] Specify whether to display the query from the menu. Field name: MenuItem.
- `Public Property InternalKey() As Long` [R] Returns the user query code as assigned by the system when adding a new user query. Field name: IntrnalKey.
  - remarks: The combination of this property and the QueryCategory property determines the primary key of the user query.
- `Public Property MenuCaption() As String` [R/W] The caption of the menu. Field name: MenuCapt. Length: 254 characters.
- `Public Property MenuPosition() As Long` [R/W] Specify the position of the query in the menu. Field name: MenuPos.
- `Public Property MenuUniqueID() As String` [R/W] Specify the unique ID of the menu. Field name: MenuUid. Length: 32 characters.
- `Public Property ParentMenuID() As Long` [R/W] The ID of the parent menu, starts from 0. You can select the parent menu item from the menu navigaton tree structure. Field name: FatherMenu.
- `Public Property ProcedureAlias() As String` [R/W] property ProcedureAlias
- `Public Property ProcedureName() As String` [R/W] property ProcedureName
- `Public Property Query() As String` [R/W] Sets or returns the query content, for example, a SELECT statement for SQL databases. Field name: QString. Length: 64,000 characters.
- `Public Property QueryCategory() As Long` [R/W] Sets or returns the code of the query category (foreign key to QueryCategories). Mandatory property. Field name: QCategory.
  - remarks: The query category value must apply to the following restrictions: - The query category value must be defined in the QueryCategories object. - The query category value must be permited for the active user. - The query category value must not be -2 (system category).
- `Public Property QueryDescription() As String` [R/W] Sets or returns the query name. The value must be unique within the same category. Mandatory property. Field name: QName. Length: 100 characters.
- `Public Property QueryType() As UserQueryTypeEnum` [R/W] The type of the query. Field name: QType.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a user query to the User Queries library.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lInternalKey As Long, ByVal lQcategory As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lInternalKey`: InternalKey.
  - param `lQcategory`: QueryCategory.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
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
