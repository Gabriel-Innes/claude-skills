<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# NotaFiscalUsage (Object)

Represents a usage for specifying tax codes for Nota Fiscal documents. Source table: OUSG

**Remarks:** To display the form in the application: - In any marketing document's row, click Usage dropdown list , and click Define New.

## Properties (13)
- `Public Property Adjustment() As BoYesNoEnum` [R/W] Adjustment. Field name: Adjustment.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Description() As String` [R/W] property Description
- `Public Property ID() As Long` [R] The ID for the usage. Field name: ID
- `Public Property IncomingImportCFOPCode() As String` [R/W] property IncomingImportCFOPCode
- `Public Property IncomingInStateCFOPCode() As String` [R/W] property IncomingInStateCFOPCode
- `Public Property IncomingOutStateCFOPCode() As String` [R/W] property IncomingOutStateCFOPCode
- `Public Property OutgoingExportCFOPCode() As String` [R/W] property OutgoingExportCFOPCode
- `Public Property OutgoingInStateCFOPCode() As String` [R/W] property OutgoingInStateCFOPCode
- `Public Property OutgoingOutStateCFOPCode() As String` [R/W] property OutgoingOutStateCFOPCode
- `Public Property ThirdParty() As BoYesNoEnum` [R/W] property ThirdParty
- `Public Property Usage() As String` [R/W] The usage name. Field name: Usage Length: 20 characters
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal ID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ID`: Usage ID.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
