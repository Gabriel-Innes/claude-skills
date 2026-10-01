<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PackagesTypes (Object)

PackagesTypes is a business object that represents the list of package types for deliveries in the Inventory and Production module. This object enables you to: - Add a package type. - Retrieve a package type. - Update a package type. - Remove a package type. - Save the object in XML format. Source table: OPKG.

**Remarks:** From the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Package Types.

## Properties (22)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the package type code (key). Field name: PkgCode.
- `Public Property Height1() As Double` [R/W] The height for the unit. Field name: Height1.
- `Public Property Height1Unit() As Long` [R/W] The height UoM. Field name: Hght1Unit.
- `Public Property Height2() As Double` [R/W] The height for the unit. Field name: Height2.
- `Public Property Height2Unit() As Long` [R/W] The height UoM. Field name: Hght2Unit.
- `Public Property Length1() As Double` [R/W] The length for the unit. Field name: Length1.
- `Public Property Length1Unit() As Long` [R/W] The length UoM. Field name: Len1Unit.
- `Public Property Length2() As Double` [R/W] The length for the unit. Field name: Length2.
- `Public Property Length2Unit() As Long` [R/W] The length UoM. Field name: Len2Unit.
- `Public Property Type() As String` [R/W] Sets or returns the package type name. Field name: PkgType. Mandatory property. Length: 30 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Volume() As Double` [R/W] The volume for the unit. Field name: Volume.
- `Public Property VolumeUnit() As Long` [R/W] The volume UoM. Field name: VolUnit.
- `Public Property Weight1() As Double` [R/W] The weight for the unit. Field name: Weight1.
- `Public Property Weight1Unit() As Long` [R/W] The weight UoM. Field name: WghtUnit.
- `Public Property Weight2() As Double` [R/W] The weight for the unit. Field name: Weight2.
- `Public Property Weight2Unit() As Long` [R/W] The weight UoM. Field name: Wght2Unit.
- `Public Property Width1() As Double` [R/W] The width for the unit. Field name: Width1.
- `Public Property Width1Unit() As Long` [R/W] The width UoM. Field name: Wdth1Unit.
- `Public Property Width2() As Double` [R/W] The width for the unit. Field name: Width2.
- `Public Property Width2Unit() As Long` [R/W] The width UoM. Field name: Wdth2Unit.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: Package type code (Code).
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
