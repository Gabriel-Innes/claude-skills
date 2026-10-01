<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserObjectsMD (Object)

The UserObjectsMD object represents the registration data settings, such as table name and supported services, of a user defined object. This object enables you to: - Add a user define object. - Retrieve a user define object by its key. - Update a user define object . - Remove a user define object from the database. - Save the object in XML format. - Specify the menu location of the UDO. Source table: OUDO. IMPORTANT: After creating a new UDO in .NET, you must release the object by executing the following line of code, where myObject is a reference to the UserObjectsMD object: System.Runtime.InteropServices.Marshal.ReleaseComObject(myObject);

**Remarks:** Mandatory fields in SAP Business One: Code and TableName. To activate the registration wizard in the application: - Select Tools > User Defined Object > User Defined Object Registration. For more information, see the User Defined Object documentation.

**Example:**
- C# example (from SAP's help):
  ```csharp
  // Updating a UDO to have a Menu item.
  UserObjectsMD udo = cmp.GetBusinessObject(BoObjectTypes.oUserObjectsMD) as UserObjectsMD;

  // Get UDO
  udo.GetByKey("MyUDO");

  // Set UDO to have a menu
  udo.MenuItem = BoYesNoEnum.tYES;
  udo.MenuCaption = "My UDO menu";

  // Set father and position of menu item.
  udo.FatherMenuID = 43535; // Business Partners menu UID
  udo.Position = 1;

  // Set UDO menu UID
  udo.MenuUID = "mn_MyUDO";

  // Update UDO to have the new menu item
  udo.Update();
  ```

## Properties (32)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CanApprove() As BoYesNoEnum` [R/W] Indicates whether the UDO uses the Approve service, which enables a UDO record to be a request and to be approved by the specified workflow template. Field name: CanApprove
- `Public Property CanArchive() As BoYesNoEnum` [R/W] Indicates that the UDO records can be archived. The OnCanArchive virtual method in the implementation DLL for the UDO can specify conditions to limit which records are archived.
  - remarks: Only relevant for document UDOs. If this property is set to Yes, then you must supply a business logic implementation (DLL) with the UDO. Refer to the ExtensionName property.
- `Public Property CanCancel() As BoYesNoEnum` [R/W] Indicates whether the UDO uses the Cancel service, which enables users to cancel a UDO record. Field name: CanCancel
- `Public Property CanClose() As BoYesNoEnum` [R/W] Indicates whether the UDO uses the Close service, which enables a user to close a UDO record without creating a posting in accounting. Field name: CanClose
- `Public Property CanCreateDefaultForm() As BoYesNoEnum` [R/W] Indicates whether the UDO uses the Default Form service, which creates a default form that has an ordinary table with selected fields. Field name: CanDefForm
  - remarks: Set tYES if you do not use a User Form.
- `Public Property CanDelete() As BoYesNoEnum` [R/W] Indicates whether the UDO uses the Delete service, which enables a user to delete records from Master Data type objects. Field name: CanDelete
- `Public Property CanFind() As BoYesNoEnum` [R/W] Indicates whether the UDO uses the Find service, which enables the Choose from list dialog box in the application (Find Form). Field name: CanFind
- `Public Property CanLog() As BoYesNoEnum` [R/W] Indicates whether the UDO uses the History Log service, which creates a history log table in the database. Field name: CanLog
- `Public Property CanYearTransfer() As BoYesNoEnum` [R/W] Indicates whether the UDO uses the Year Transfer service, which enables the copying of the user tables to a new database. Field name: CanYrTrnsf
- `Public Property ChildTables() As UserObjectMD_ChildTables` [R] Returns the UserObjectMD_ChildTables child tables.
- `Public Property Code() As String` [R/W] Sets or returns the Object Unique ID. The Unique ID is the primary key of the user defined object and its child objects. Length: 20 characters (must include at least one alphabetical character). Field name: Code.
  - remarks: You must include your name identifier in the object ID.
- `Public Property EnableEnhancedForm() As BoYesNoEnum` [R/W] Creates the UDO enhanced form (UDO form with header-line style). Field name: CanNewForm.
- `Public Property EnhancedFormColumns() As UserObjectMD_EnhancedFormColumns` [R] Returns the UserObjectMD_EnhancedFormColumns child object.
- `Public Property ExtensionName() As String` [R/W] Sets or returns the name and full path of your business logic implementation (DLL). Length: 254 characters. Field name: ExtName.
- `Public Property FatherMenuID() As Long` [R/W] The menu ID of the UDO menu's father menu. Field name: FatherMenuID. Length: 11 characters.
- `Public Property FindColumns() As UserObjectMD_FindColumns` [R] Returns the UserObjectMD_FindColumns child object.
- `Public Property FormColumns() As UserObjectMD_FormColumns` [R] Returns the UserObjectMD_FormColumns child object.
- `Public Property FormSRF() As String` [R/W] The *.srf file of the UDO enhanced form (UDO form with header-line style). Field name: NewFormSrf. Length: 16 characters.
- `Public Property LogTableName() As String` [R/W] Sets or returns the log table name. This table maintains a history log of all actions related to the main user table. Length: 19 characters. Field name: LogTable.
  - remarks: If you select the History Log service, then set a history log table name starting with "A" followed by the object's User Table name. Notes: - If you unregister a user defined object that is registered to the history log service, the related history log table is deleted from the database. - If you unregister the history log service while updating a user defined object, the history log table is not deleted (only unregistered).
- `Public Property ManageSeries() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the user defined object can use the Manage Series service. This service enables document numbering. Field name: MngSeries.
- `Public Property MenuCaption() As String` [R/W] The caption of the UDO menu that appears on the SAP Business One main menu. Field name: MenuCapt. Length: 256 characters.
- `Public Property MenuItem() As BoYesNoEnum` [R/W] Specifies whether to add a UDO menu into the SAP Business One main menu. Field name: MenuItem.
- `Public Property MenuUID() As String` [R/W] The UID of the UDO menu. Field name: MenuUid. Length: 32 characters.
- `Public Property Name() As String` [R/W] Sets or returns the the object name that must include your name identifier. Length: 100 characters. Field name: Name.
- `Public Property ObjectType() As BoUDOObjType` [R/W] Sets or returns a valid value of BoUDOObjType type that specifies the object type, Master Data or Document. Field name: TYPE.
- `Public Property OverwriteDllfile() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to overwrite existing Dll file with new Dll file. Field name: OvrWrtDll.
  - remarks: The property is used to modify the User Object.
- `Public Property Position() As Long` [R/W] The position of the UDO menu under its father menu. Field name: Position. Length: 6 characters.
- `Public Property RebuildEnhancedForm() As BoYesNoEnum` [R/W] If needed, rebuild the UDO enhanced form (UDO form with header-line style). Field name: IsRebuild.
- `Public Property TableName() As String` [R/W] Sets or returns the the main User Table related to the user defined object. Length: 19 characters. Field name: TableName.
  - remarks: You can set only a user table of the selected ObjectType (Master Data object type or Document object type).
- `Public Property TemplateID() As String` [R/W] The ID of the workflow template for an approval UDO record. Field name: TemplateID. Length: 11 characters.
- `Public Property UseUniqueFormType() As BoYesNoEnum` [R/W] Indicates whether every child form of a parent UDO gets a unique ID. If false, all child forms share the same ID.

## Methods (6)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal Code As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Code`: 
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: 
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
