<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# NotaFiscalCST (Object)

Represents CST codes for Nota Fiscal documents. Source table: OTSC

**Remarks:** For Brazil only. To display the form in the application: - Select Administration > Definitions > Financials > Tax > Nota Fiscal > Define CST Code.

## Properties (7)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R/W] The CST code. Field name: CODE Length: 4 characters
- `Public Property CSTCodeOutgoing() As String` [R/W] The corresponding outgoing CST code for this CST (incoming) code. The size of the value can be one of the following: 2 characters, if the TaxCategory field is IPI (-4), PIS (-8), or COFINS (-9) 4 characters, if the TaxCategory field is ICMS (-6) 20 characters, if the TaxCategory field is set to any other value Field name: CodeOut
- `Public Property DescriptionOutgoing() As String` [R/W] A description for the outgoing CST code specified in the CSTCodeOutgoing property. Field name: OutDesc
- `Public Property Situation() As String` [R/W] The description or tributary situation. Field name: Situation Length: 16 characters
- `Public Property TaxCategory() As Long` [R/W] The tax category for the CST code. Field name: Category This field is a foreign key to the ONFT table.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal ID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ID`: CST ID.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
