<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MultiLanguageTranslations (Object)

The MultiLanguageTranslation object enables to translate alphanumeric data of specified fields in master data objects (such as, BusinessPartners and Items) to foreign languages and then print documents in the translated language. This functionality is used by companies that trade with foreign business partners that require docouments in their language. Source table: OMLT.

**Remarks:** Prerequisites: - Set MultiLanguageSupportEnable (AdminInfo) to tYES. - Set the UserLanguages object with the required foreign language. - Set LanguageCode (BusinessPartners) to the requied foreign language. To display the form in the application: - Open a master data window (e.g. Business Partner Master Data). - From the menu bar, select View --> Translatable Fields. A globe icon appears next to fields that can be translated. - Click a field for translation and then from the menu bar, select Goto --> Translate.

## Properties (7)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property FieldAlias() As String` [R/W] Sets or returns the field name for which the translation in user language applies. Field name: FieldAlias. Length: 10 characters.
- `Public Property Numerator() As Long` [R] Returns the key (numerator) of the translated field value as assigned by the system when adding a translation to a field value. Field name: TranEntry.
- `Public Property PrimaryKeyofobject() As String` [R/W] Sets or returns the primary key of the object for which the translation in user language applies. For example: CardCode value of a business partner; ItemCode value of an item. Field name: PK. Length: 254 characters.
- `Public Property TableName() As String` [R/W] Sets or returns the table name (e.g. OCRD and OITM) for which the translation in user language applies. Field name: TableName. Length: 20 characters.
- `Public Property TranslationsInUserLanguages() As TranslationsInUserLanguages` [R] Returns the TranslationsInUserLanguages child object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` method Add
  - remarks: Adds a translation for a specified field.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: Numerator.
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
