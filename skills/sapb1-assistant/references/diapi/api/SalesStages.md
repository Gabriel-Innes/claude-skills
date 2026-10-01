<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesStages (Object)

The SalesStages object enables defining sales stages and their probability percentage. For example: Lead, Meeting, Quotation, Negotiation, and Order. These definitions are used as default values for the SalesOpportunities object. Source table: OOST.

**Remarks:** Mandatory fields in SAP Business One: Name and Stageno. To display the form in the application: - Select Administration -->Setup -->Sales Opportunities -->Sales Stages.

## Properties (9)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Cancelled() As BoYesNoEnum` [R/W] Returns whether or not the sales stage is cancelled. Field name: Canceled.
  - remarks: In the Sales Opportunities form, stages that are cancelled cannot be selected.
- `Public Property ClosingPercentage() As Double` [R/W] Sets or returns the probability percentage to complete the sales stage successfuly. Field name: CloPrcnt.
  - remarks: The value must not be negative.
- `Public Property IsPurchasing() As BoYesNoEnum` [R/W] property IsPurchasing
- `Public Property IsSales() As BoYesNoEnum` [R/W] property IsSales
- `Public Property Name() As String` [R/W] Sets or returns the stage name. Mandatory property. Field name: Descript. Langth: 30 characters.
- `Public Property SequenceNo() As Long` [R] Returns the primary identification key of the sales stage as assigned by the system when adding a new sales stage (numerator). Property type Read-only property " --> Field name: Num.
- `Public Property Stageno() As Long` [R/W] Sets or returns the stage identification number. Mandatory property. Field name: StepId.
  - remarks: The stage number must be a unique and not a negative number.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a sales stage definition.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lNum As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lNum`: SequenceNo.
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
