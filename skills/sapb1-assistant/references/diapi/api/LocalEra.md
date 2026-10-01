<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# LocalEra (Object)

LocalEra is a business object that represents the Local Era. Local Era is a type of calendar system that co-existent in some countries (such as, Japan) with the Gregorian calendar. This object enables you to: - Browse the Local Era table for mapping to or from the Gregorian calendar (Browser). - Retrieve details about the Local Era by its key (Code). - Retrieve the Local Era details from XML data. - Save the object to a file as XML data. - Save the object as XML formatted data. Source table: OJPE.

**Remarks:** Country-specific for Japan. To display the form in the application: - Select Administration --> Setup --> Define Local Era.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R] Returns the Local Era code. Field name: Code. Length: 1 character.
- `Public Property EraName() As String` [R] Returns the Local Era name. Field name: EraName. Length: 20 characters.
- `Public Property StartDate() As Date` [R] Returns the start date of the Local Era calendar. Field name: StartDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (4)
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrCode`: Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` method SaveXML
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
