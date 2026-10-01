<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DynamicSystemStrings (Object)

The DynamicSystemStrings object enables to modify the field name and format in the interface to match the terms used in your company. For example, in the Business Partners Master Data form, you can modify the field name 'Code' to 'BP Number' (format: bold). Source table: SDIS.

**Remarks:** Mandatory properties: FormID and ItemID. The combination of these properties specify the primary key of the required field for modification. In case the ItemID specifies a table, set also the ColumnID, otherwise the system sets the value -1. To display the form in the application: - Open a form, e.g. an A/R Invoice. - Hold down the Ctrl key and double-click the field name.

## Properties (8)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ColumnID() As String` [R/W] Sets or returns the column identification key. Field name: ColumnId. Mandatory property for Table fields. The default value is -1 (Title field). Length: 10 characters.
  - remarks: The entered value must be a valid column ID (the system does not validate the entered value). To display the column ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property FormID() As String` [R/W] Sets or returns the form identification key. Field name: FormID. Mandatory property. Length: 20 characters.
  - remarks: The entered value must be a valid form ID (the system does not validate the entered value). To display the form ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property IsBold() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not the new name of the field appears bold. Field name: IsBold.
- `Public Property IsItalics() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not the new name of the field appears italic. Field name: IsItalic.
- `Public Property ItemID() As String` [R/W] Sets or returns the ID of the field or the table in a form (primary key with FormID). Field name: ItemId. Mandatory property. Length: 10 characters.
  - remarks: The entered value must be a valid item ID (the system does not validate the entered value). In case the ItemID specifies a table, set also the ColumnID, otherwise the system sets the value -1. To display the item ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property ItemString() As String` [R/W] Sets or returns the new name for the specified field. Field name: ItemString. Length: 64 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Applies a new modification to a field name.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrFormId As String, ByVal bstrItemNum As String, ByVal bstrColNum As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrFormId`: 
  - param `bstrItemNum`: 
  - param `bstrColNum`: 
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
