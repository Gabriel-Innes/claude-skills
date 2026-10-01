<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DunningLetters (Object)

Represents a list of dunning levels that is used as a template when creating a new dunning term. You can define up to 10 dunning levels, and relate each level to a dunning letter format. This object enables you to: - Add a dunning level. - Retrieve a dunning level by its key. - Update a dunning level. - Remove a dunning level. - Save the object in XML format. This object manages a list of dunning levels. This list is a template when creating a new dunning term, and the template list does not directly affect business partners or the dunning letters functionality. Dunning terms can be assigned to business partners and are managed by the DunningTermsService. Source table: ODUN.

**Remarks:** Mandatory fields: RowNumber, LetterFormat and Effectiveafter. To display the form in the application: - Select Administration --> Setup --> Business Partners --> Dunning Levels.

## Properties (10)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CalcInterest() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to calculate interest on a delinquent debt. Field name: CalcIntert.
- `Public Property Effectiveafter() As String` [R/W] Sets or returns the overdue number of days. Field name: EffctAftr. Mandatory in SAP Business One. Length: 3 characters.
  - remarks: The value of each level relates to the preceding level. For example, If you set this property to 30 days for level 1 and 40 days for level 2, then SAP Business One will send the first dunning letter 30 days after the payment due date, and then will send the second dunning letter 40 days after the first dunning letter date.
- `Public Property FeeCurrency() As String` [R/W] Sets or returns the currency of the dunning letter fee. Field name: FeeCurr. Length: 3 characters.
- `Public Property Feeperletter() As Double` [R/W] Sets or returns the fee for each dunning letter sent to the business partner. Field name: LetterFee.
- `Public Property LetterFormat() As String` [R/W] Sets or returns the letter format to relate to the dunning level. Field name: LetrFormat. Mandatory in SAP Business One. Length: 8 characters.
- `Public Property MinimumBalance() As Double` [R/W] Sets or returns the minimum balance of the debt. SAP Business One will send a dunning letter only for a debt balance higher than this minimum amount. Field name: MinBalance.
- `Public Property MinimumBalanceCurrency() As String` [R/W] Sets or returns the currency of MinimumBalance. Field name: MinBlnCurr. Length: 3 characters.
- `Public Property RowNumber() As Long` [R/W] Sets or returns the dunning level number, which is used as an identification key. Field name: LineNum. Mandatory in SAP Business One.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Dunning level number (RowNumber).
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
