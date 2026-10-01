<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BusinessPartnerGroups (Object)

BusinessPartnerGroups represents the setup of customer and vendor Groups. Used for classifing business partners according to groups, such as, sector or size. Source table: OCRG.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Business Partners --> Customer Groups (or Vendor Groups).

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the group code of the current Business Partner Group. Field name: GroupCode.
- `Public Property Name() As String` [R/W] Sets or returns the name of current Business Partner Groups. Field name: GroupName. Length: 20 characters.
- `Public Property Type() As BoBusinessPartnerGroupTypes` [R/W] Sets or returns a valid value of BoBusinessPartnerGroupTypes that determines wether current group is a Customer Group or a Vendor Group. Field name: GroupType.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the OCRG table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal lGroupCode As Long) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database.
  - param `lGroupCode`: Specifies the required object's properties according to object's absolute key in Company database.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
