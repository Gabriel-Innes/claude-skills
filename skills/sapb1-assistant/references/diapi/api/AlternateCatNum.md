<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlternateCatNum (Object)

AlternateCatNum is a business object that represents the alternative catalog numbers in the Business Partners module. This object enables you to: - Add an alternative catalog number. - Retrieve an alternative catalog number by its key. - Update an alternative catalog number. - Save the object in XML format. Source table: OSCN.

**Remarks:** Customers or vendors usually maintain their own catalog numbers for items. You can define and use these catalog numbers instead of the item numbers. Mandatory fields in SAP Business One: CardCode, ItemCode, and Substitute. To display the form in the application: - Select Inventory --> Item Management --> Batches --> Define Business Partner Catalog Numbers.

## Properties (8)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners Object
  - remarks: Mandatory property. SAP Business One validates the CardCode, and if not valid, returns an error code.
- `Public Property Description() As String` [R/W] BP Catalog description. Field name: Descriptio. Length: 200 characters.
- `Public Property DisplayBPCatalogNumber() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to display business partner catalog number. Field name: ShowSCN.
- `Public Property IsDefault() As BoYesNoEnum` [R/W] The default Business Partner Catalog Number for each combination of Business Partner and Item Code. Field name: IsDefault.
  - C# example (from SAP's help):
    ```csharp
    AlternateCatNum cat = (AlternateCatNum)oCompany.GetBusinessObject(BoObjectTypes.oAlternateCatNum);
    bool res = cat.GetByKey(""I001"", ""C001"", ""sss"");
    if(res)
    cat.IsDefault = BoYesNoEnum.tYES;
    ```
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. The item code must be unique. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property Substitute() As String` [R/W] Sets or returns the substitute catalog number. Field name: Substitute. Length: 20 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ItemCode As String, ByVal CardCode As String, ByVal Substitute As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ItemCode`: Specifies the item key in the database.
  - param `CardCode`: Specifies the card key in the database. Specifies the identification key of the business object (CardCode).
  - param `Substitute`: Specifies the key of the replacement item in the database.
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
