<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Attachments2 (Object)

The Attachments2 object enables to copy files from a source folder to the Attachments folder that is defined through the application. Files stored in the Attachments folder can be associated by the AttachmentEntry property of the following objects: Contacts, ContractTemplates, CustomerEquipmentCards, EmployeeInfo, KnowledgeBaseSolutions, Messages, Message, SalesOpportunities, and ServiceContracts. This object replaces the Attachment and Attachments objects. Source table: OATC.

**Remarks:** The Attachments Path must be defined in the application before using this object. This path is stored in the AttachePath field of the OADP table, which is not exposed through the DI API. Mandatory property: Lines. You must set the Attachments2_Lines child object whith the following properties: SourcePath, FileName, and FileExtension. To define the Attachments Path in the application: - Select Administration -->System Initialization -->General Settings -->Path tab.

## Properties (4)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the attachment file as assigned by SAP Business One when adding an attachment file. Field name: AbsEntry.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Lines() As Attachments2_Lines` [R] Returns the Attachments2_Lines child object (mandatory).
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds attachment files that are specified by the Attachments2_Lines child object.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsoluteEntry As Long) As Boolean` Determines wether or not the object identified by its AbsoluteEntry exists. If the object exists, the method gets it.
  - param `lAbsoluteEntry`: Specifies the AbsoluteEntry of the object you want to get.
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
