<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
