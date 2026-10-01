<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesPersons (Object)

The SalesPersons object enables to define sales employees and their commision percentage. Source table: OSLP.

**Remarks:** Mandatory fields in SAP Business One: SalesEmployeeName. To display the form in the application: - Select Administration -->Setup -->General -->Sales Employees.

## Properties (14)
- `Public Property Active() As BoYesNoEnum` [R/W] Determines whether the sales employee is active or not. Field name: Active.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CommissionForSalesEmployee() As Double` [R/W] Sets or returns the commission percentage for the sales employee. Field name: Commission.
  - remarks: Applicable when SetCommissionbySE (AdminInfo object) is set to tYes.
- `Public Property CommissionGroup() As Long` [R/W] Sets or returns commission group code, which is relevant to the sales employee. This is a foreign key to the CommissionGroups object. Sets or returns the commission percentage for the sales employee. Field name: GroupCode. This is a foreign key to the CommissionGroups object.
  - remarks: Applicable when SetCommissionbySE (AdminInfo object) is set to tYes.
- `Public Property eMail() As String` [R/W] Sets or returns the Email of the sales employee. Length: 100 characters. Field name: Email.
- `Public Property EmployeeID() As Long` [R] Returns the employee ID code. Field name: EmpID. This is a foreign key to the EmployeesInfo object.
- `Public Property Fax() As String` [R/W] Sets or returns the fax number of the sales employee. Length: 50 characters. Field name: Fax.
- `Public Property Locked() As BoYesNoEnum` [R] Returns whether or not the sales person definition is locked for update. Field name: Locked.
  - remarks: tYes - the record is locked. The record -1 -No Sales Employee- is locked by the system. tNo - the record is available for update. All the records starting from 1 are available for update.
- `Public Property Mobile() As String` [R/W] Sets or returns the mobile number of the sales employee. Length: 50 characters. Field name: Mobil.
- `Public Property Remarks() As String` [R/W] Sets or returns the remarks related to the sales employee. Length: 50 characters. Field name: Memo.
- `Public Property SalesEmployeeCode() As Long` [R] Returns the primary key of the sales employee as assigned by the system. Field name: SlpCode.
  - remarks: This property is a system numerator available from number 1. The default value is -1 that means No Sales Employee. You can set another default value for a specific user or users group by the SalesEmployee (UserDefaultGroups).
- `Public Property SalesEmployeeName() As String` [R/W] Sets or returns the name of the sales employee. Mandatory property. Field name: SlpName. Length: 155 characters.
- `Public Property Telephone() As String` [R/W] Sets or returns the telephone number of the sales employee. Length: 50 characters. Field name: Telephone.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a sales person employee.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lSlpCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lSlpCode`: SalesEmployeeCode.
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
