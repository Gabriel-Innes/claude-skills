<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Currencies (Object)

Currencies is a business object that represents the currency codes in the Administration module. This object enables you to: - Add a currency code. - Retrieve a currency code by its key. - Update a currency code. - Remove a currency code. - Save the object in XML format. Source table: OCRN.

**Remarks:** Mandatory fields in SAP Business One: Code and DocumentsCode. To display the form in the application: - Select Administration --> Setup --> Financials --> Currencies.

## Properties (20)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R/W] Sets or returns the currency code, for example, USD, EUR. Field name: CurrCode. Mandatory property. Length: 3 characters.
- `Public Property Decimals() As CurrenciesDecimalsEnum` [R/W] Sets or returns a value that specifies the decimal rounding type for the currency.
  - remarks: The settings affect the fields Price, Line Total, and Document Total in marketing documents.
- `Public Property DocumentsCode() As String` [R/W] Sets or returns the currency internatioanl code on printed documents (e.g. $, ?). Field name: DocCurrCod. Mandatory property. Length: 3 characters.
- `Public Property EnglishHundredthName() As String` [R/W] Sets or returns the English singular name of the decimal unit (e.g. Cent). Field name: F100Name. Length: 20 characters.
- `Public Property EnglishName() As String` [R/W] Sets or returns the English singular name of the currency (e.g. Canadian Dollar). Field name: FrgnName. Length: 20 characters.
- `Public Property HundredthName() As String` [R/W] Sets or returns the singular name of the decimal unit (e.g. Cent) on printed checks. Field name: Chk100Name. Length: 20 characters.
- `Public Property InternationalDescription() As String` [R/W] Sets or returns the international singular name of the currency on printed chacks (e.g. Canadian Dollar). Field name: ChkName. Length: 20 characters.
- `Public Property MaxIncomingAmtDiff() As Double` [R/W] property MaxIncomingAmtDiff
- `Public Property MaxIncomingAmtDiffPercent() As Double` [R/W] property MaxIncomingAmtDiffPercent
- `Public Property MaxOutgoingAmtDiff() As Double` [R/W] property MaxOutgoingAmtDiff
- `Public Property MaxOutgoingAmtDiffPercent() As Double` [R/W] property MaxOutgoingAmtDiffPercent
- `Public Property Name() As String` [R/W] Sets or returns the currency name (e.g. Canadian Dollar). Field name: CurrName. Length: 20 characters.
- `Public Property PluralEnglishHundredthName() As String` [R/W] Sets or returns the English plural name of the decimal unit (e.g. Cents). Applicable for cluster B only. Length: 20 characters.
- `Public Property PluralEnglishName() As String` [R/W] Sets or returns the English plural name of the currency (e.g. Canadian Dollars). Applicable for cluster B only. Length: 20 characters.
- `Public Property PluralHundredthName() As String` [R/W] Sets or returns the plural name of the decimal unit (e.g. Cents) on printed checks. Applicable for cluster B only. Length: 20 characters.
- `Public Property PluralInternationalDescription() As String` [R/W] Sets or returns the international plural name of the currency on printed chacks (e.g. Canadian Dollar). Applicable for cluster B only. Length: 20 characters.
- `Public Property Rounding() As RoundingSysEnum` [R/W] Sets or returns a valid value that determines the rounding method.
- `Public Property RoundingInPayment() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to round the total in payments.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a new currency rate.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Currency As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Currency`: Specifies the currency code (see Code property).
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
