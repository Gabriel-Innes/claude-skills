<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DeductionTaxHierarchies (Object)

The DeductionTaxHierarchies object enables to define taxation levels to withhold from payments to vendors. This object is part of the Business Partners module. Source table: ODDT.

**Remarks:** Country-specific for Israel. Mandatory properties: BPCode, HierarchyCode, ValidFrom, and ValidUntil. To display the form in the application: - Select Business Partners -->Business Partner Master Data -->Accounting tab -->Tax tab. - Click the Hierarchies button.

## Properties (12)
- `Public Property AbsEntry() As Long` [R] Returns ABS_ENTRY, the Primery key to the Withholding Tax Deduction Hierarchy (ODDT) table. Field name: ABS_ENTRY.
- `Public Property BPCode() As String` [R/W] Sets or returns the business partner identification key in SAP Business One. Field name: CardCode. Mandatory property. Length: 15 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DeductionPercent() As Double` [R/W] property DeductionPercent
- `Public Property HierarchyCode() As String` [R/W] Sets or returns the hierarchy code. Field name: DateFrom. Mandatory property. Length: 10 characters. TrcCode
- `Public Property HierarchyName() As String` [R/W] Sets or returns the hierarchy name. Field name: DateFrom. Length: 30 characters. TrcName
- `Public Property LastUpdated() As Date` [R] property LastUpdated
- `Public Property Lines() As DeductionTaxHierarchies_Lines` [R] Returns the DeductionTaxHierarchies_Lines child object.
- `Public Property MaximumTotal() As Double` [R/W] property MaximumTotal
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ValidFrom() As Date` [R/W] Sets or returns the validity start date of the withholding tax deduction certificate. Field name: DateFrom.
  - remarks: SAP Business One does not enable overlapping periods.
- `Public Property ValidUntil() As Date` [R/W] Sets or returns the validity end date of the withholding tax deduction certificate. Field name: DateTo.
  - remarks: SAP Business One does not enable overlapping periods.

## Methods (6)
- `Public Function Add() As Long` Adds a taxation level definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: Numerator.
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
