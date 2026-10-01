<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Banks (Object)

The Banks object enables to define banks, which can be used by the HouseBankAccounts and BPBankAccounts objects. Source table: ODSC.

**Remarks:** Mandatory fields in SAP Business One: BankCode and CountryCode. To display the form in the application: - Select Administration -->Setup -->Banking -->Banks.

## Properties (13)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the bank as assigned by the system when adding a new entry. Field name: AbsoluteEntry.
- `Public Property AccountforOutgoingChecks() As String` [R] Returns the bank account number for outgoing checks. Field name: DfltAcct. Length: 50 characters.
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code. Field name: BankCode. Mandatory property. Length: 30 characters.
- `Public Property BankName() As String` [R/W] Sets or returns bank name. Field name: BankName. Length: 32 characters.
- `Public Property BranchforOutgoingChecks() As String` [R] Returns the bank branch for outgoing checks. Field name: DfltBranch. Length: 50 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CountryCode() As String` [R/W] Sets or returns the country code of the bank (for example: DE). Field name: CountryCod. Length: 3 characters. Mandatory property.
  - remarks: You can set only the country codes that are defined in the Countries table (OCRY - not exposed through the DI API).
- `Public Property DefaultBankAccountKey() As Long` [R/W] Sets or returns the identification key of the default house bank account. Field name: DfltActKey. This is a foreign key to the HouseBankAccounts object.
  - remarks: Bank accounts are defined through the HouseBankAccounts object. The bank account is identified by the AbsoluteEntry.
- `Public Property IBAN() As String` [R/W] Sets or returns the International Bank Account Number (IBAN). Field name: IBAN. Length: 50 characters.
- `Public Property NextCheckNumber() As Long` [R] Returns the number of the next check for payment as specified in the NextCheckNo property of the HouseBankAccounts object. Field name: NextNum.
- `Public Property PostOffice() As BoYesNoEnum` [R/W] Determines whether or not the bank is also a post office. Field name: PostOffice.
- `Public Property SwiftNo() As String` [R/W] Sets or returns the swift number for international payments by wire transfer. Field name: SwiftNum. Length: 50 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a new record of banks table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: 
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
