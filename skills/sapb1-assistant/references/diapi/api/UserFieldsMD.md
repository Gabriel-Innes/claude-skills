<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserFieldsMD (Object)

UserFieldsMD is a business object that enables you to manage user-defined fields in user and system tables. This object enables you to: - Add a user-defined field. - Retrieve a user-defined field from the database by its key. - Remove a user-defined field. - Save the object in XML format. Source table: CUFD Mandatory properties: Name and TableName IMPORTANT: After creating a new user-defined field in .NET, you must release the object by executing the following line of code, where myObject is a reference to the UserFieldsMD object: System.Runtime.InteropServices.Marshal.ReleaseComObject(myObject);

**Remarks:** The DI API allows only one metadata object instance (with no other instances of any object type). This maintains data integrity by preventing any manipulation of a business object while modifying the object's properties. If you add a mandatory user-defined field, you must also define a default value; otherwise, the following message appears: "Invalid object name; cannot add field". Note: After adding a user-defined field, you can view it in the User-Defined Fields - Management window. To view the new user-defined field in the Settings window, you must restart the SAP Business One application. Before adding a user-defined field, check the application window and make sure there is an entry for the object to which you want to add a user-defined field. To display the form in the application: - From the main menu bar, select Tools --> Customization Tools --> User-Defined Fields - Management.

## Properties (15)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DefaultValue() As String` [R/W] Sets or returns the default value of the field. Field name: Dflt. Length: 254 characters.
  - remarks: Use the DefaultValue property in conjunction with the Value property of the ValidValuesMD object to determine the default value for the new field.
- `Public Property Description() As String` [R/W] Sets or returns the description of the field. Field name: Descr. Length: 80 characters.
- `Public Property EditSize() As Long` [R/W] Sets or returns the field maximum value entered by the user. This applies only when the Type property is set to db_Alpha or db_Numeric. Field name: EditSize.
- `Public Property FieldID() As Long` [R] Returns the unique identification key of the field in the meta data table. Field name: FieldID.
  - remarks: This value is also used with the GetByKey method.
- `Public Property LinkedSystemObject() As UDFLinkedSystemObjectTypesEnum` [R/W] Links to an existing system object of SAP Business One.
- `Public Property LinkedTable() As String` [R/W] Sets or returns a linked user table name, so that the user field will be used as a foreign key in the TableName. Field name: RTable. Length: 20 characters.
  - remarks: The values of the Size and Type properties must match the Size and Type values of the key field in the linked table. When using the LinkedTable property, do not set the DefaultValue and ValidValues properties. For the linked user tables do not use the @ sign in the LinkedTable name. This property is not supported by the Recordset object.
- `Public Property LinkedUDO() As String` [R/W] Links to a user-defined object (UDO) form of both Matrix style and Header Lines style. Field name: RelUDO. Length: 20 characters.
- `Public Property Mandatory() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not this User Field is mandatory in SAP Business One. Field name: Sys.
- `Public Property Name() As String` [R/W] Sets or returns the field name. Field name: AliasID. Length: 50 characters.
- `Public Property Size() As Long` [R/W] The actual size of the field. The value is automatically determined by the input of the EditSize property. Do not set any value in the Size property. Field name: SizeID.
  - remarks: Relevant when the Type property is set to db_Alpha or db_Numeric.
- `Public Property SubType() As BoFldSubTypes` [R/W] Returns or set the field sub-type, which specifies a specific format of the data type.
  - remarks: The following table describes the relations between the SAP Business One application data types and the DI API data types. Application DI API Type Structure Type SubType Alphanumeric Regular db_Alpha st_None Alphanumeric Address db_Alpha st_Address Alphanumeric Phone db_Alpha st_Phone Alphanumeric Text db_Memo st_None Numeric None db_Numeric st_None Date/Hour Date db_Date st_None Date/Hour Hour db_Date st_Time Units And Totals Rate db_Float st_Rate Units And Totals Sum db_Float st_Sum Units And Totals Price db_Float st_Price Units And Totals Quantity db_Float st_Quantity Units And Totals Percent db_Float st_Percentage Units And Totals Measure db_Float st_Measurement General Link db_Memo st_Link General Image db_Alpha st_Image
- `Public Property TableName() As String` [R/W] Sets or returns the name of the parent table that this field refers to. Length: 21 characters. Field name: TableID.
- `Public Property Type() As BoFieldTypes` [R/W] Sets or returns the data type, which describes the nature of the data, of the specified field . Field name: TypeID.
- `Public Property ValidValues() As ValidValuesMD` [R] Returns the ValidValuesMD object.
  - remarks: You can use this property to retrieve the valid values for the specified field.

## Methods (7)
- `Public Function Add() As Long` Adds a new user field to an exiting user table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal TableName As String, ByVal FieldID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `TableName`: Specifies the name of the user defined table. (use the symbol @ as a prefix to the name, see the TableName property of the UserTablesMD object).
  - param `FieldID`: Specifies the field identification key.
- `Public Function Remove() As Long` Removes a specified field from the table.
  - remarks: Warning: when removing a field, all it's content is lost.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
