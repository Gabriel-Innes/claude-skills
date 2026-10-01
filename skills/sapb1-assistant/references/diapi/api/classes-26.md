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

# UserPermission (Object)

UserPermission is a business object that enables to set the authorization of a specified user to a UserPermissionTree. Source table: USR3.

**Remarks:** To display the form in the application: - Select Administration --> System Initialization --> Authorization --> General Authorization. See example of Authorizations Tree.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total rows in the table.
- `Public Property Permission() As BoPermission` [R/W] Sets or returns a valid value of BoPermission type that specifies the permission type assigned to the user. The available options are according to the setting of Options property. Field name: Permission.
- `Public Property PermissionID() As String` [R/W] Sets or returns the identification key of the user permission in the tree, for which the permission is set. Length: 20 characters. Field name: PermId. This is a foreign key to the UserPermissionTree object, not exposed through the DI API).
- `Public Property UserCode() As Long` [R] Returns the user code.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# UserPermissionForms (Object)

UserPermissionForms is a child object of UserPermissionTree object and enables to add a user permission to a collection of forms. Source table: UPT1.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total forms in the collection (rows).
- `Public Property DisplayOrder() As Long` [R/W] Sets or returns the display order of the user permission form in the collection (starts from 1). Field name: VisOrder.
- `Public Property FormType() As String` [R/W] Sets or returns the form ID (primary key) linked to the user permission. Length: 20 characters. Field name: FormId.
  - remarks: To display the form ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property PermissionID() As String` [R] Returns the identification key of the user permission tree as defined in UserPermissionTree object. Length: 20 characters. Field name: PermId. This is a foreign key to the UserPermissionTree object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# UserPermissionTree (Object)

UserPermissionTree is a business object that represents the User Authorization Form. This object enables to manage user authorization for new forms (which their FormType property is defined in UserPermissionForms object). After adding a user permission tree to the Authorizations tree, you can set the UserPermission object. This object enables you to: - Add a user permission tree to the Authorizations tree. - Retrieve a user permission tree by its key. - Update a user permission tree. - Remove a user permission tree from the Authorizations tree. - Save the object in XML format. Source table: OUPT.

**Remarks:** Mandatory field in SAP Business One: PermissionId. To display the form in the application: - Select Administration --> System Initialization --> Authorization --> User Authorization Form. See example of User Authorization Form. To manage user authorization for forms that are not forms, set the mUserPermission.IsItem = tYES and create the logic to support the item permission.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  [Visual Basic]

  Dim RetVal As Long

  Dim ErrCode As Long

  Dim ErrMsg As String

  Dim mUserPermission As SAPbobsCOM.UserPermissionTree

  Set mUserPermission = oCompany.GetBusinessObject(oUserPermissionTree)

  '//Mandatory field, which is the key of the object.

  '//The partner namespace must be included as a prefix followed by _

  mUserPermission.PermissionId = "SM_MathClass"

  '//The Name value that will be displayed in the General Authorization Tree

  mUserPermission.Name = "SM_MathClass"

  '//The permission that this object can get

  mUserPermission.Options = bou_FullReadNone

  '//In case the level is one, there Is no need to set the FatherID parameter.

  mUserPermission.Levels = 1

  RetVal = UserPermission.Add

  oCompany.GetLastError RetVal, ErrMsg

  '//In case this permission object has a son permission object
  ```
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  [Visual Basic]

  Dim RetVal As Long

  Dim ErrCode As Long

  Dim ErrMsg As String

  Dim mUserPermission As SAPbobsCOM.UserPermissionTree

  Set mUserPermission = oCompany.GetBusinessObject(oUserPermissionTree)

  mUserPermission.PermissionId = "SM_MathClassSon"

  mUserPermission.Name = "SM_MathClassExam"

  mUserPermission.Options = bou_FullNone

  '//For level 2 and up you must set the object's father unique ID

  mUserPermission.Levels = 2

  mUserPermission.FatherID = "SM_MathClass"

  '//this object manages forms

  mUserPermission.UserPermissionForm.FormType = "GL_MathClass"

  RetVal = mUserPermission.Add

  oCompany.GetLastError RetVal, ErrMsg

  [Visual Basic]

  Dim RetVal As Long

  Dim ErrCode As Long

  Dim ErrMsg As String

  Dim mUser As SAPbobsCOM.Users

  Set mUser = oCompany.GetBusinessObject(oUsers)

  '//The user unique ID is 2

  RetVal = mUser.GetByKey(2)

  '//Setting a new sub object for the User that hold the user permission for the user permission object

  mUser.UserPermission.PermissionId = "SM_MathClassSon"

  '//Seting full permission for User 2 to manage SM_MathClassSon sub object

  mUsers.UserPermission.Permission = boper_Full

  RetVal = mUsers.Update

  oCompany.GetLastError RetVal, ErrMsg
  ```
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim RetVal As Long

  Dim ErrCode As Long

  Dim ErrMsg As String

  Dim mUser As SAPbobsCOM.Users

  Set mUser = oCompany.GetBusinessObject(oUsers)

  '//The user unique ID is 2

  RetVal = mUser.GetByKey(2)

  '//Setting a new sub object for the User that hold the user permission for the user permission object

  mUser.UserPermission.PermissionId = "SM_MathClassSon"

  '//Seting full permission for User 2 to manage SM_MathClassSon sub object

  mUsers.UserPermission.Permission = boper_Full

  RetVal = mUsers.Update

  oCompany.GetLastError RetVal, ErrMsg
  ```

## Properties (11)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DisplayOrder() As Long` [R] Returns the display order of the user permission form in the tree (starts from 1). Field name: VisOrder.
- `Public Property IsItem() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the user permission relates to an item in the form, for example, button, secondary form, and menu item. Field name: IsItem.
  - remarks: Default: tNO. tNO - the user permission relates to a form. tYES - the user permission relates to an item in the form.
- `Public Property Levels() As Long` [R] Returns the level (1 to 5) of the user permission in the tree. For parent user permissions, assign level 1. For child user permissions, assign level greater than 1. Field name: Levels.
  - remarks: level is 1. Child user permission level is greater than 1.
- `Public Property Name() As String` [R/W] Sets or returns the name of the user permission. This name will appear in the General Authorization Tree. Field name: Name. Length: 40 characters.
- `Public Property Options() As BoUPTOptions` [R/W] Sets or returns a valid value of BoUPTOptions type that specifies the user permission options. Field name: Options.
- `Public Property ParentID() As String` [R/W] Sets or returns the identification key of the parent user permission. Mandatory field for child permission in a tree. Length: 20 characters. Field name: FathId.
- `Public Property PermissionID() As String` [R/W] Sets or returns the identification key of the user permission. Mandatory property. Length: 20 characters. Field name: AbsId.
  - remarks: When you add a user permission item to the General Authorization Tree, you must include in the permission ID a prefix with the partner's name space in the following format: XYZ_Unique ID (where: XYZ is the partner's name space).
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserPermissionForms() As UserPermissionForms` [R] Returns the UserPermissionForms child object.
- `Public Property UserSignature() As Long` [R/W] Returns the ID code of the user who enters the user permission tree details. This user ID code is defined in the Users object. Field name: UserSign. This is a foreign key to the Users object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal PermissionID As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `PermissionID`: Identification key of the user permission tree (PermissionId).
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

# UserQueries (Object)

The UserQueries object enables to define user queries in the Queries Manager. Source table: OUQR.

## Properties (14)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property EnableMenuEntry() As BoYesNoEnum` [R/W] Specify whether to display the query from the menu. Field name: MenuItem.
- `Public Property InternalKey() As Long` [R] Returns the user query code as assigned by the system when adding a new user query. Field name: IntrnalKey.
  - remarks: The combination of this property and the QueryCategory property determines the primary key of the user query.
- `Public Property MenuCaption() As String` [R/W] The caption of the menu. Field name: MenuCapt. Length: 254 characters.
- `Public Property MenuPosition() As Long` [R/W] Specify the position of the query in the menu. Field name: MenuPos.
- `Public Property MenuUniqueID() As String` [R/W] Specify the unique ID of the menu. Field name: MenuUid. Length: 32 characters.
- `Public Property ParentMenuID() As Long` [R/W] The ID of the parent menu, starts from 0. You can select the parent menu item from the menu navigaton tree structure. Field name: FatherMenu.
- `Public Property ProcedureAlias() As String` [R/W] property ProcedureAlias
- `Public Property ProcedureName() As String` [R/W] property ProcedureName
- `Public Property Query() As String` [R/W] Sets or returns the query content, for example, a SELECT statement for SQL databases. Field name: QString. Length: 64,000 characters.
- `Public Property QueryCategory() As Long` [R/W] Sets or returns the code of the query category (foreign key to QueryCategories). Mandatory property. Field name: QCategory.
  - remarks: The query category value must apply to the following restrictions: - The query category value must be defined in the QueryCategories object. - The query category value must be permited for the active user. - The query category value must not be -2 (system category).
- `Public Property QueryDescription() As String` [R/W] Sets or returns the query name. The value must be unique within the same category. Mandatory property. Field name: QName. Length: 100 characters.
- `Public Property QueryType() As UserQueryTypeEnum` [R/W] The type of the query. Field name: QType.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a user query to the User Queries library.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lInternalKey As Long, ByVal lQcategory As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lInternalKey`: InternalKey.
  - param `lQcategory`: QueryCategory.
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

# Users (Object)

Users is a business object that represents the users table of the SAP Business One application. The users table includes the users list, login details, and authorizations. This object enables you to: - Add users to the users list. - Retrieve user's details by its key. - Update user's details. - Remove users from the users list. - Save the object in XML format. Source table: OUSR.

**Remarks:** Mandatory fields in SAP Business One: UserCode and UserPassword. To display the form in the application: - Select Administration --> Setup --> General --> Users.

## Properties (30)
- `Public Property Branch() As Long` [R/W] Sets or returns the user's branch code. Field name: Branch. This is a foreign key to the Branches table (OUBR - not exposed through the DI API).
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CashLimit() As BoYesNoEnum` [R/W] Indicates whether to set the maximum cash amount a regular user is authorized to enter in an incoming payment (Payment Means window, Cash tab). Field name: CashLimit.
- `Public Property Defaults() As String` [R/W] Sets or returns the users group code. Length: 8 characters. Field name: DfltsGroup. This is a foreign key to the UserDefaultGroups object , which provides the default values related to the users group.
- `Public Property Department() As Long` [R/W] Sets or returns the user's department code. Field name: Department. This is a foreign key to the Departments table (OUDP), which is exposed via the DepartmentsService object.
- `Public Property eMail() As String` [R/W] Sets or returns the user's e-mail that can be used by the system for sending messages to the user. Field name: E_Mail. Length: 100 characters.
- `Public Property FaxNumber() As String` [R/W] Sets or returns the user's fax number that can be used by the system for sending messages to the user. Field name: Fax. Length: 50 characters.
- `Public Property Group() As BoUserGroup` [R] Returns a valid value that determines whether the user group status is Regular or Deleted. Field name: GROUPS.
- `Public Property InternalKey() As Long` [R] Returns the internal key identifier of a user. This is a serial number assigned by the system used as a reference for other documents in the system. Field name: INTERNAL_K.
- `Public Property LanguageCode() As BoSuppLangs` [R/W] property LanguageCode
- `Public Property LastLoginTime() As Date` [R] The time at which the user last logged on to SAP Business One. Field name: LstLoginT.
- `Public Property LastLogoutDate() As Date` [R] The date on which the user last logged off from SAP Business One. Field name: LstLogoutD.
- `Public Property LastLogoutTime() As Date` [R] The time at which the user last logged off from SAP Business One. Field name: LstLogoutT.
- `Public Property LastPasswordChangedBy() As String` [R] The user who last changed the password. Field name: LstPwdChB.
- `Public Property LastPasswordChangeTime() As Date` [R] The time at which the password was last changed. Field name: LstPwdChT.
- `Public Property Locked() As BoYesNoEnum` [R/W] Returns a valid value that determines whether the user status is Locked or or not. Field name: Locked.
- `Public Property MaxCashAmtForIncmngPayts() As Double` [R/W] Sets the maximum cash amount a regular user is authorized to enter in an incoming payment (Payment Means window, Cash tab). Field name: MaxCashSum.
- `Public Property MaxDiscountGeneral() As Double` [R/W] Sets the maximum discount (in percentage) relevant to all discounts, except for sales and purchase documents, including: - Business partner master data - Payment terms - Discount in goods issue, goods receipt, and inventory transfer - Special price Field name: Discount.
- `Public Property MaxDiscountPurchase() As Double` [R/W] Sets the maximum discount (in percentage) for purchase documents. Field name: PurchDisc.
- `Public Property MaxDiscountSales() As Double` [R/W] Sets the maximum discount (in percentage) for sales documents. Field name: SalesDisc.
- `Public Property MobilePhoneNumber() As String` [R/W] Sets or returns the user's mobile phone number that can be used by the system for sending SMS messages to the user. Field name: PortNum. Length: 50 characters.
- `Public Property Superuser() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the user is a super-user. Super-users have automatic authorizations to all objects and are authorized to perform all functions in the system. Authorizations for super-users cannot be reduced or changed. However, super-users can deny super-user rights from other super-users in the system. Field name: SUPERUSER.
- `Public Property UserActionRecord() As UserActionRecord` [R] To display a list of actions and details related to a specific user's access activity in SAP Business One.
- `Public Property UserBranchAssignment() As UserBranchAssignment` [R] property UserBranchAssignment
- `Public Property UserCode() As String` [R/W] Sets or returns the unique user code for log on to the system. Length: 8 characters (case-sensitive). Mandatory property. Field name: USER_CODE.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserGroupByUser() As UserGroupByUser` [R] property UserGroupByUser
- `Public Property UserName() As String` [R/W] Sets or returns the user name used for information only and not for reference. The user name can be non unique. Field name: U_Name. Length: 155 characters.
- `Public Property UserPassword() As String` [R/W] Sets or returns the password for log on to the system. The password must be unique. Length: 4 to 8 characters (case-sensitive). Mandatory property. Field name: PASSWORD.
- `Public Property UserPermission() As UserPermission` [R] Returns the UserPermission child object.

## Methods (9)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal InternalKey As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `InternalKey`: Internal key identifier (read only) of a user that is provided by the system and used as a reference for other documents in the system.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a user from the users list.
  - remarks: Before using the Remove method, you must get the required table using the GetByKey method.
- `Public Function RemoveUserAndLicense() As Long` method RemoveUserAndLicense
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

# UserTable (Object)

The UserTable object represents records of a user-defined table.

**Example:**
- example note: This sample shows how to do the following: - Add a user table. - Add a UDF to the user table. - Add a record to the new table. When adding a user table, two fields are created: Code (primary key) and Name. Both are mandatory.
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim ret As Long

  Private Sub Add_Table_Click()

      Dim oUserTablesMD As SAPbobsCOM.UserTablesMD

      Set oUserTablesMD = oCompany.GetBusinessObject(oUserTables)

      '**************************************************

      ' When adding user tables or fields, use a prefix

      ' identifying your partner name space. This will

      ' prevent collisions from different partner add-ons

      '

      ' SAP's name space prefix is "BE_"

      '**************************************************

      'Set the two mandatory fields

      oUserTablesMD.TableName = "T1"

      oUserTablesMD.TableDescription = "Table1"

      'Add the table (which contains 2 default, mandatory fields, 'Code' and 'Name')

      ret = oUserTablesMD.Add

      If ret <> 0 Then

          oCompany.GetLastError ret, Str

          MsgBox Str

      Else

          MsgBox "Table: " & oUserTablesMD.TableName & " was added successfully"

      End If

  End Sub

  Private Sub Add_UDF_Click()

      Dim oUserFieldsMD As SAPbobsCOM.UserFieldsMD

      Set oUserFieldsMD = oCompany.GetBusinessObject(oUserFields)

      oUserFieldsMD.TableName = "T1"

      oUserFieldsMD.Name = "AlbUDF"

      oUserFieldsMD.Description = "Albert UDF"

      'Add the field to the table

      lRetCode = oUserFieldsMD.Add

      If lRetCode <> 0 Then

          oCompany.GetLastError ret, Str

          MsgBox Str

      Else

          MsgBox "Field: '" & oUserFieldsMD.Name & "' was added successfuly to " & oUserFieldsMD.TableName & " Table"

      End If

  End Sub

  Private Sub Add_Data_Click()

      Dim oUserTable As SAPbobsCOM.UserTable

      Set oUserTable = oCompany.UserTables.Item(1)

      'Set default, mandatory fields

      oUserTable.Code = "A"

      oUserTable.Name = "Albert"

      'Set user field

      oUserTable.UserFields.Fields.Item("U_AlbUDF").Value = "1"

      oUserTable.Add

      If ret <> 0 Then

          oCompany.GetLastError ret, Str

          MsgBox Str

      Else

          MsgBox "Value to field: '" & oUserTable.UserFields.Fields.Item("U_AlbUDF").Name & "' was updated successfuly to " & oUserTable.TableName & " Table"

      End If

  End Sub
  ```

## Properties (6)
- `Public Property ArchiveDate() As Date` [R/W] property ArchiveDate
- `Public Property Code() As String` [R/W] Sets or returns the key value for the current record.
- `Public Property Name() As String` [R/W] Sets or returns the value of this record.
- `Public Property TableDescription() As String` [R] Sets or returns the description of the user defined table.
- `Public Property TableName() As String` [R] Sets or returns the name of the user defined table.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Key As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Key`: The key as defined in the Code property.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record from the table.
  - remarks: Before using the Remove method, you must get the required table using the GetByKey method.
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

# UserTables (Collection)

UserTables is a collection of UserTable objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of tables in the collection.

## Methods (1)
- `Public Function Item(ByVal Index As Variant) As UserTable` The Item method retrieves a user table specified by its index.
  - param `Index`: User table number.

# UserTablesMD (Object)

The UserTablesMD object enables to manage user defined tables as follows: - Add a user table. - Retrieve a user table from the database by its TableName. - Remove a user table. - Save the object in XML format. Source table: OUTB. IMPORTANT: After creating a new user-defined table in .NET, you must release the object by executing the following line of code, where myObject is a reference to the UserTablesMD object: System.Runtime.InteropServices.Marshal.ReleaseComObject(myObject);

**Remarks:** DI API allows only one metadata object instance (with no other instances of any object type). This maintains data integrity by preventing any manipulation of a business object while modifying the object's properties. To display the form in the application: - From the main menu bar, select Tools --> Manage User Fields. - Click User Tables.

## Properties (7)
- `Public Property Archivable() As BoYesNoEnum` [R/W] property Archivable
- `Public Property ArchiveDateField() As String` [R/W] property ArchiveDateField
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DisplayMenu() As BoYesNoEnum` [R/W] Determines whether to display the user-defined table as a submenu in the SAP Business One client, or a tile in the Web Client. Field name: DisplyMenu.
- `Public Property TableDescription() As String` [R/W] A string that describes the name and functionality of the table. Field name: Descr. Length: 30 characters.
- `Public Property TableName() As String` [R/W] Sets or returns the name for the user defined table. Field name: TableName. Length: 19 characters.
  - remarks: When adding a user table, SAP Business One automatically adds the symbol @ as a prefix to the table name. For example, if you add a table named ABC, the resulting table name is @ABC. When referring to a user-defined table, you must use the name including the prefix @. When adding a user table and assigning it a TableName, the DI API creates the table with an upper case name. By default, Microsoft SQL Server is not case sensitive. If it is configured to be case sensitive, make sure to specify the table name in upper-case when using the DoQuery method of the Recordset object.
- `Public Property TableType() As BoUTBTableType` [R/W] Sets or returns a valid value of BoUTBTableType type that specifies the type of the user table. Field name: ObjectType.
  - remarks: For each user table type, SAP Business One provides a default table. You can add user fields to the default user fields but not remove them. For a user defined object, do not use the table type 'No object'.

## Methods (7)
- `Public Function Add() As Long` Adds a new table to the User-Defined Tables collection. The new table includes two columns by default: Code and Name, where the Code column is the primary key of the specific user table.
  - remarks: When adding a user table, SAP Business One automatically adds the symbol @ as a prefix to the table name. For example, if you add a table named ABC, the resulting table name is @ABC. When referring to a user-defined table, you must use the name including the prefix @. When adding a user table and assigning it a TableName, the DI API creates the table with an upper case name. By default, Microsoft SQL Server is not case sensitive. If it is configured to be case sensitive, make sure to specify the table name in upper-case when using the DoQuery method of the Recordset object.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal TableName As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `TableName`: Specifies the name of the user defined table (use the symbol @ as a prefix to the name, see the TableName property of the UserTablesMD object).
- `Public Function Remove() As Long` Deletes a specified table.
  - remarks: Before using the Remove method, you must get the required table using the GetByKey method. Warning: Removing a table deletes all its content.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.

# UserValidValues (Object)

UserValidValues is an object related to the FormattedSearches object. It enables to define valid values for the field specified by the FormattedSearches object. Source table: CUVV.

**Remarks:** This object is relevant for fields that their search Action is set to bofsaValidValues. To display the form in the application: - Open a document and click any field. - From the menu bar, select Tools --> Search Function --> Define. - In the Define Formatted Search form, select the Search in Existing Values option. - Click the [...] button. The Define Field Values form opens.

## Properties (3)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property FieldValue() As String` [R/W] Sets or returns the valid value of the field that is specified in the Index property of the FormattedSearches object. Field name: Value. Length: 254 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ValidValue (Object)

The ValidValue object represents a single valid value element of a specified user field.

## Properties (2)
- `Public Property Description() As String` [R] Returns the description of the valid value. Length: 254 characters.
- `Public Property Value() As String` [R] Returns the valid value. Length: 254 characters.

# ValidValues (Collection)

ValidValues is a collection of ValidValue objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ValidValue objects in the collection.

## Methods (1)
- `Public Function Item(ByVal Index As Variant) As ValidValue` Returns a ValidValue object by its index.
  - param `Index`: Specifies the object index.

# ValidValuesMD (Object)

ValidValuesMD enables you to add valid values to a specified user defined field (UserFieldsMD). Source table: UFD1.

**Remarks:** To display the form in the application: - From the main menu bar, select Tools --> Manage User Fields. - Click User Tables.

## Properties (3)
- `Public Property Count() As Long` [R] Retrieves the number of the valid values in the collection.
- `Public Property Description() As String` [R/W] Sets or returns the description of the valid value. Field name: Descr. Length: 254 characters.
- `Public Property Value() As String` [R/W] Sets or returns the valid value. Field name: FldValue. Length: 254 characters.

## Methods (3)
- `Public Sub Add()` Adds a new valid value to the collection.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.UserFieldsMD oUFMD;

    // Delete valid value
    if(oUFMD.GetByKey("@MyObj", 0) == true)
    {
        oUFMD.ValidValues.SetCurrentLine(0);
        oUFMD.ValidValues.Delete();
        oUFMD.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ValueMappingCommunicationData (Object)

ValueMappingCommunicationData Class

## Properties (10)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property CommunicationType() As VMCommunicationTypeEnum` [R/W] property CommunicationType
- `Public Property EndDate() As Date` [R/W] property EndDate
- `Public Property EndTime() As Long` [R/W] property EndTime
- `Public Property Message() As String` [R/W] property Message
- `Public Property ObjectID() As Long` [R/W] property ObjectId
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property StartTime() As Long` [R/W] property StartTime
- `Public Property Status() As VMCommunicationStatusEnum` [R/W] property Status
- `Public Property ThirdPartySystemId() As Long` [R/W] property ThirdPartySystemId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ValueMappingCommunicationParams (Object)

ValueMappingCommunicationParams Class

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ValueMappingCommunicationService (Object)

ValueMappingCommunicationService Class

## Methods (6)
- `Public Function AddVMCommunicationObject(ByVal pIValueMappingCommunicationData As ValueMappingCommunicationData) As ValueMappingCommunicationParams` AddVMCommunicationObject
  - param `pIValueMappingCommunicationData`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ValueMappingCommunicationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ValueMappingCommunicationServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetVMCommunicationObject(ByVal pIValueMappingCommunicationParams As ValueMappingCommunicationParams) As ValueMappingCommunicationData` GetVMCommunicationObject
  - param `pIValueMappingCommunicationParams`: 
- `Public Sub UpdateVMCommunicationObject(ByVal pIValueMappingCommunicationData As ValueMappingCommunicationData)` UpdateVMCommunicationObject
  - param `pIValueMappingCommunicationData`: 

# ValueMappingParams (Object)

ValueMappingParams Class

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ValueMappingService (Object)

ValueMappingService Class

## Methods (10)
- `Public Function AddVMObject(ByVal pIVM_B1ValuesData As VM_B1ValuesData) As ValueMappingParams` AddVMObject
  - param `pIVM_B1ValuesData`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ValueMappingServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ValueMappingServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetMappedB1Value(ByVal pIVM_B1ValuesData As VM_B1ValuesData) As VM_B1ValuesCollection` GetMappedB1Value
  - param `pIVM_B1ValuesData`: 
- `Public Function GetThirdPartyValuesForB1Value(ByVal pIVM_B1ValuesData As VM_B1ValuesData) As VM_ThirdPartyValuesCollection` GetThirdPartyValuesForB1Value
  - param `pIVM_B1ValuesData`: 
- `Public Function GetVMObject(ByVal pIValueMappingParams As ValueMappingParams) As VM_B1ValuesData` GetVMObject
  - param `pIValueMappingParams`: 
- `Public Sub RemoveMappedValue(ByVal pIVM_ThirdPartyValuesData As VM_ThirdPartyValuesData)` RemoveMappedValue
  - param `pIVM_ThirdPartyValuesData`: 
- `Public Sub RemoveVMObject(ByVal pIValueMappingParams As ValueMappingParams)` RemoveVMObject
  - param `pIValueMappingParams`: 
- `Public Sub UpdateVMObject(ByVal pIVM_B1ValuesData As VM_B1ValuesData)` UpdateVMObject
  - param `pIVM_B1ValuesData`: 

# VatGroups (Object)

The VatGroups object enables to define tax groups that can be assigned to business partners and items in sales and purchase documents. Source table: OVTG.

**Remarks:** Country-specific for Europe. Mandatory properties: Code and Effectivefrom (VatGroups_Lines). To display the form in the application: - Select Administration --> Setup --> Financials --> Tax --> Tax Groups.

## Properties (31)
- `Public Property AcquisitionReverse() As BoYesNoEnum` [R/W] Determines whether or not the VAT group is related to Acquisition/Reverse. Field name: AcqstnRvrs.
  - remarks: Applicable for purchase documents (the value of Category is bovcInputTax)
- `Public Property AcquisitionReverseCorrespondingTaxCode() As String` [R/W] property AcquisitionReverseCorrespondingTaxCode
- `Public Property AcquisitionTax() As String` [R/W] Sets or returns the G/L account for acquisition tax posting. Field name: AcqsTax. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT). Applicable for purchase documents (the value of Category is bovcInputTax)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CashDiscountAccount() As String` [R/W] property CashDiscountAccount
- `Public Property Category() As BoVatCategoryEnum` [R/W] Determines whether the tax group applies to sales documents (output tax) or to purchase documents (input tax). Field name: Category.
- `Public Property Code() As String` [R/W] Sets or returns a tax group code (primary key). Field name: Code. Length: 8 characters.
- `Public Property Correction() As BoYesNoEnum` [R/W] Determines whether or not the tax group is a correction tax group. Field name: Correction.
  - remarks: Country-specific for Portugal.
- `Public Property DeferredTaxAcc() As String` [R/W] Sets or returns the G/L account for deferred tax postings. Field name: DeferrAcc. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT).
- `Public Property DownPaymentTaxOffsetAccount() As String` [R/W] property DownPaymentTaxOffsetAccount
- `Public Property EBooksVatCategory() As Long` [R/W] property EBooksVatCategory
- `Public Property EqualizationTaxAccount() As String` [R/W] The G/L account for equalization tax. Field name: EquAccount
  - remarks: For Spain only.
- `Public Property EU() As BoYesNoEnum` [R/W] Determines whether or not the tax group applies to European Union countries. Field name: IsEC.
  - remarks: Applicable for sales documents (the value of Category is bovcOutputTax).
- `Public Property ExcludedTaxSummary() As BoYesNoEnum` [R/W] property ExcludedTaxSummary
- `Public Property GoodsShipment() As String` [R/W] Sets or returns the goods shipment indicator, which appears in the EU Sales Report. This property is applicable when TriangularDeal is not set. Field name: GoddsShip. Length: 1 numeric character.
  - remarks: The value of this property is a foreign key to the OGSP table, which is not exposed through the DI API.
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property Name() As String` [R/W] Sets or returns a tax group name. Field name: Name. Length: 50 characters.
- `Public Property NonDeduct() As Double` [R/W] Sets or returns the non-deductable tax percentange. Field name: NonDedct.
  - remarks: Applicable for purchase documents (the value of Category is bovcInputTax) and when the value of AcquisitionReverse is tNO.
- `Public Property NonDeductAcc() As String` [R/W] Sets or returns the G/L account for non-deductable tax postings. Field name: NonDedAcc. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT). Applicable for purchase documents (the value of Category is bovcInputTax) and when the value of AcquisitionReverse is tNO.
- `Public Property Report349Code() As Report349CodeListEnum` [R/W] property Report349Code
- `Public Property ServiceSupply() As String` [R/W] Sets or returns the service supply indicator, which appears in the EU Sales Report. This property is applicable when TriangularDeal and GoodsShipment is not set. If you put a value in either TriangularDeal or GoodsShipment, it will cause the deletion of the value in ServiceSupply. Field name: ServSupply. Length: 1 numeric character.
- `Public Property StandardTaxCode() As String` [R/W] property StandardTaxCode
- `Public Property TaxAccount() As String` [R/W] Sets or returns the G/L account for the tax group. Field name: Account. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT).
- `Public Property TaxRegion() As VatGroupsTaxRegionEnum` [R/W] property TaxRegion
- `Public Property TaxTypeBlackList() As TaxTypeBlackListEnum` [R/W] property TaxTypeBlackList
- `Public Property TriangularDeal() As String` [R/W] Sets or returns the triangular deal indicator, which enables to identify delivery of goods as part of triangular deals in the EU sales report. This property is applicable when GoodsShipment is not set. Field name: Indicator. Length: 1 numeric character.
  - remarks: Deliveries of goods as part of triangular deals must be listed separately in the EU sales report. The end-user must identify these deliveries as such when entering the line item. This indicator causes the transaction to be identified as a triangular deal in the EU sales report. The value of this property is a foreign key to the OIND table, which is not exposed through the DI API.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatCorrection() As String` [R/W] Sets or returns the tax group code (foreign key) that is used as a correction tax group. Field name: VatCrctn. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: Country-specific for Portugal.
- `Public Property VATDeductibleAccount() As String` [R/W] property VATDeductibleAccount
- `Public Property VatGroups_Lines() As VatGroups_Lines` [R] Returns the VatGroups_Lines child object.
- `Public Property VATInRevenueAccount() As String` [R/W] property VATInRevenueAccount

## Methods (7)
- `Public Function Add() As Long` Adds a tax group definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal bstrGroupCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrGroupCode`: Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
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

# VatGroups_Lines (Object)

VatGroups_Lines is a child object of the VatGroups_Lines object. It enables to define the tax percentage and the effective from date for the tax group. Source table: VTG1.

**Remarks:** Country-specific for Europe. Mandatory property: Effectivefrom. To display the form in the application: - Select Administration --> Setup --> Financials --> Tax --> Tax Groups. - Click the Tax Definition button.

## Properties (6)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DatevCode() As Long` [R/W] property DatevCode
- `Public Property Effectivefrom() As Date` [R/W] Sets or returns the date from which the tax group's percentage is effective. Mandatory property. Field name: EffecDate.
- `Public Property EqualizationTax() As Double` [R/W] Sets or returns the equalization tax percentage. Field name: EquVatPr.
  - remarks: Country-specific for Spain and Portugal.
- `Public Property Rate() As Double` [R/W] Sets or returns the percentage of the tax group. Field name: Rate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# VM_B1ValuesCollection (Collection)

VM_B1ValuesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As VM_B1ValuesData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As VM_B1ValuesData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# VM_B1ValuesData (Object)

VM_B1ValuesData Class

## Properties (4)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property ObjectAbsEntry() As String` [R/W] property ObjectAbsEntry
- `Public Property ObjectID() As Long` [R/W] property ObjectId
- `Public Property VM_ThirdPartyValuesCollection() As VM_ThirdPartyValuesCollection` [R] property VM_ThirdPartyValuesCollection

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# VM_ThirdPartyValuesCollection (Collection)

VM_ThirdPartyValuesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As VM_ThirdPartyValuesData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As VM_ThirdPartyValuesData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# VM_ThirdPartyValuesData (Object)

VM_ThirdPartyValuesData Class

## Properties (4)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property LineId() As Long` [R] property LineId
- `Public Property ThirdPartySystemId() As Long` [R/W] property ThirdPartySystemId
- `Public Property ThirdPartyValue() As String` [R/W] property ThirdPartyValue

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WarehouseLocations (Object)

The WarehouseLocations object enables to define geographical locations for warehouses. Source table: OLCT.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Inventory --> Warehouses. - From the Location field select Define New. Defining few locations for a warehouse is required when the warehouse includes few areas, where each area can be concidered as a separate warehouse, with the same address as the main warehouse.

## Properties (34)
- `Public Property AssesseeType() As String` [R/W] Sets or returns the assessee type in the location definition. Applicable for cluster B only. Field name: AsseType.
- `Public Property Block() As String` [R/W] Sets or returns the block name in the location definition. Applicable for cluster B only. Field name: Block.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the building in the location definition. Applicable for cluster B only. Field name: Building.
- `Public Property CECommissionerate() As String` [R/W] Sets or returns the C.E. commissionerate in the location definition. Applicable for cluster B only. Field name: CeComRate.
- `Public Property CEDivision() As String` [R/W] Sets or returns the C.E division in the location definition. Applicable for cluster B only. Field name: CeDivision.
- `Public Property CERange() As String` [R/W] Sets or returns the C.E range in the location definition. Applicable for cluster B only. Field name: CeRange.
- `Public Property CERegisterNumber() As String` [R/W] Sets or returns the C.E Register number in the location definition. Applicable for cluster B only. Field name: CeRegNo.
- `Public Property City() As String` [R/W] Sets or returns the city in the location definition. Applicable for cluster B only. Field name: City.
- `Public Property Code() As Long` [R] Returns the warehouse location code (primary key) in the Location definition. Field name: Code.
- `Public Property CompanyType() As String` [R/W] Sets or returns the company type in the location definition. Applicable for cluster B only. Field name: CompType.
- `Public Property Country() As String` [R/W] Sets or returns the country in the location definition. Applicable for cluster B only. Field name: Country.
- `Public Property County() As String` [R/W] Sets or returns the county in the location definition. Applicable for cluster B only. Field name: County.
- `Public Property CSTNumber() As String` [R/W] Sets or returns the CST number in the location definition. Applicable for cluster B only. Field name: CstNo.
- `Public Property EccNumber() As String` [R/W] Sets or returns the E.C.C number in the location definition. Applicable for cluster B only. Field name: EccNo.
- `Public Property ExemptionNumber() As String` [R/W] Sets or returns the exempt number in the location definition. Applicable for cluster B only. Field name: EccNo.
- `Public Property GSTIN() As String` [R/W] property GSTIN
- `Public Property GSTISD() As String` [R/W] property GSTISD
- `Public Property GSTTDS() As String` [R/W] property GSTTDS
- `Public Property GstType() As BoGSTRegnTypeEnum` [R/W] property GstType
- `Public Property Jurisdiction() As String` [R/W] Sets or returns the jurisdiction in the location definition. Applicable for cluster B only. Field name: Jurisd.
- `Public Property LSTVATNumber() As String` [R/W] Sets or returns the LST/VAT number in the location definition. Applicable for cluster B only. Field name: LstVatNo.
- `Public Property ManufacturerCode() As String` [R/W] Sets or returns the manufacture code in the location definition. Applicable for cluster B only. Field name: ManuCode.
- `Public Property Name() As String` [R/W] Sets or returns the name of the geographical location for warehouses. Field name: Location. Length: 100 characters.
- `Public Property NatureOfBusiness() As String` [R/W] Sets or returns the nature of business in the location definition. Applicable for cluster B only. Field name: NatOfBiz.
- `Public Property PANNumber() As String` [R/W] Sets or returns the PAN number in the location definition. Applicable for cluster B only. Field name: PanNo.
- `Public Property RegistrationType() As String` [R] Returns the registration type in the location definition. Applicable for cluster B only. Field name: RegType.
- `Public Property ServiceTaxNumber() As String` [R/W] Sets or returns the Service Tax Number in the location definition. Applicable for cluster B only. Field name: ServTaxNo.
- `Public Property State() As String` [R/W] Sets or returns the state in the location definition. Applicable for cluster B only. Field name: State.
- `Public Property Street() As String` [R/W] Sets or returns the street in the location definition. Applicable for cluster B only. Field name: Street.
- `Public Property TANNumber() As String` [R/W] Sets or returns the TAN number in the location definition. Applicable for cluster B only. Field name: TanNo.
- `Public Property TINNumber() As String` [R/W] Sets or returns the T.I.N number in the location definition. Applicable for cluster B only. Field name: TinNo.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code in the location definition. Applicable for cluster B only. Field name: ZipCode.

## Methods (6)
- `Public Function Add() As Long` Adds a warehouse location definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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

# Warehouses (Object)

Warehouses is a business object that represents the warehouses information in the Inventory module. This object enables you to: - Add a warehouse. - Retrieve a warehouse by its key. - Update a warehouse details. - Remove a warehouse. - Save the object in XML format. Source table: OWHS.

**Remarks:** Mandatory field in SAP Business One: WarehouseCode. To display the form in the application: - Select Administration --> Setup --> Inventory --> Warehouses. The warehouse definition includes: - Warehouse type - Warehouse address - G/L accounts, which are defined in ChartOfAccounts, used in Item Master Data - Inventory Data in case GLMethod property is set to WH.

## Properties (92)
- `Public Property AddressName2() As String` [R/W] property AddressName2
- `Public Property AddressName3() As String` [R/W] property AddressName3
- `Public Property AddressType() As String` [R/W] property AddressType
- `Public Property AllowUseTax() As BoYesNoEnum` [R/W] Determines whether or not to Allow Use Tax for items in marketing documents. Field name: UseTax.
  - remarks: Country-specific for US and Canada.
- `Public Property AutoAllocOnIssue() As BoDocWhsAutoIssueMethod` [R/W] The method by which items in bin locations are issued. Field name: AutoIssMtd.
- `Public Property AutoAllocOnReceipt() As AutoAllocOnReceiptMethodEnum` [R/W] property AutoAllocOnReceipt
- `Public Property BinLocCodeSeparator() As String` [R/W] The separator of bin location codes. Field name: BinSeptor. Length: 5 characters.
- `Public Property Block() As String` [R/W] Sets or returns the block subcomponent of the warehouse address. Field name: Block. Length: 100 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the additional address details of the warehouse, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters. Building
- `Public Property BusinessPlaceID() As Long` [R/W] Returns the business place ID related to the warehouse. Field name: BPLid.
- `Public Property City() As String` [R/W] Sets or returns the city subcomponent of the warehouse address. Field name: City. Length: 100 characters.
- `Public Property CostInflationAccount() As String` [R/W] Sets or returns the G/L account associated with Cost Inflation. Field name: CostRvlAct. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property CostInflationOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Cost Inflation Offset. Field name: CstOffsAct. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property CostOfGoodsSold() As String` [R/W] Sets or returns the G/L account associated with Cost of Good Sold in continues stock system. Field name: SaleCostAc. Length: 15 characters.
- `Public Property Country() As String` [R/W] Sets or returns the country code subcomponent of the warehouse address. Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county subcomponent of the warehouse address. Field name: County. Length: 100 characters.
- `Public Property DecreaseGLAccount() As String` [R/W] Sets or returns the G/L account associated with Decrease G/L Account. Field name: DecresGlAc. Length: 15 characters.
- `Public Property DecreasingAccount() As String` [R/W] Sets or returns the G/L account associated with decreased stock transactions (inventory offset). Field name: DecreasAc. Length: 15 characters.
- `Public Property DefaultBin() As Long` [R/W] The default bin location in the warehouse for receiving items. Field name: DftBinAbs.
- `Public Property DefaultBinEnforced() As BoYesNoEnum` [R/W] Indicates whether to enforce the use of the default bin location during receipt of items to the warehouse. That is, when you receive an item to the warehouse, you must place it in the default bin location. Field name: DftBinEnfd.
- `Public Property DropShip() As BoYesNoEnum` [R/W] Determines whether or not to the warehouse type is virtual (no address) or real (with address). Field name: DropShip.
  - remarks: When set to Y, the warehouse is virtual and shipments to this warehouse are shipped automatically to the purchaser Ship To address. In addition, the warehouse does not participate in the Material Requirement Planning (MRP). When set to N, the warehouse is real and shipments to this warehouse are shipped to the warehouse address. In addition, the warehouse can participate in the Material Requirement Planning (MRP).
- `Public Property EnableBinLocations() As BoYesNoEnum` [R/W] Enables bin locations for the warehouse. Field name: BinActivat.
- `Public Property EnableReceivingBinLocations() As BoYesNoEnum` [R/W] Enables receiving bin locations for a warehouse. Field name: RecBinEnab.
- `Public Property EUExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with EU Expenses Account. Field name: EUExpensAc. Field name: ExpensesAc. Length: 15 characters.
- `Public Property EUPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with EU Purchase Credit Acc.. Field name: APCMEUAct. Field name: APCMEUAct. Length: 15 characters
- `Public Property EURevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with EU Revenues. Field name: EURevenuAc. Length: 15 characters.
- `Public Property ExchangeRateDifferencesAccount() As String` [R/W] Sets or returns the G/L account associated with Exchange Rate Differences between purchase delivery notes and A/P invoices. Field name: ExchangeAc. Length: 15 characters.
- `Public Property Excisable() As BoYesNoEnum` [R/W] Sets or returns the Excisable in Warehouses Definition. Applicable for cluster B only (country-specific for India). Field name: Excisable.
- `Public Property ExemptedCredits() As String` [R/W] Sets or returns the G/L account associated with Exempted Credits account. Field name: ARCMExpAct. Length: 15 characters.
- `Public Property ExemptRevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Exempted Revenues. Field name: ExmptIncom). Length: 15 characters.
- `Public Property ExpenseAccount() As String` [R/W] Sets or returns the G/L account associated with Expense Account. Field name: ExpensesAc. Length: 15 characters.
- `Public Property ExpenseOffsetingAct() As String` [R/W] Sets or returns the G/L account associated with Expense Offset Account. Field name: ExpOfstAct. Length: 15 characters.
  - remarks: This is a foreign key to the ChartOfAccounts Object.
- `Public Property ExpensesClearingAccount() As String` [R/W] Sets or returns the G/L account associated with Expenses clearing Account. Field name: ExpClrAct. Length: 15 characters.
  - remarks: This is a foreign key to the ChartOfAccounts Object.
- `Public Property External() As BoYesNoEnum` [R/W] property External
- `Public Property FederalTaxID() As String` [R/W] Sets or returns the Federal Tax ID related to the warehouse. Field name: FedTaxID. Length: 32 characters.
- `Public Property ForeignExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with Foreign Expenses account. Field name: FrExpensAc. Length: 15 characters.
- `Public Property ForeignPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with Foreign Purchase Credit Account. Field name: APCMFrnAct. Length: 15 characters.
- `Public Property ForeignRevenuesAcc() As String` [R/W] Sets or returns the G/L account associated with Sales Revenue - Foreign Account. Field name: FrRevenuAc. Length: 15 characters.
- `Public Property GlobalLocationNumber() As String` [R/W] property GlobalLocationNumber
- `Public Property GoodsClearingAcc() As String` [R/W] Sets or returns the G/L account associated with closing a purchase delivery note. Field name: BalanceAcc. Length: 15 characters.
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property IncreaseGLAccount() As String` [R/W] Sets or returns the G/L account associated to Increase G/L Account. Field name: IncresGlAc. Length: 15 characters.
- `Public Property IncreasingAcc() As String` [R/W] Sets or returns the G/L account associated to increased stock transactions (inventory offset). Field name: IncresGlAc. Length: 15 characters.
- `Public Property InternalKey() As Long` [R] Returns the internal key of the warehouse as assigned by SAP Business One when adding a warehouse. Field name: IntrnalKey.
- `Public Property InventoryOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to an inventory account used within production transactions and for change of value of the inventory account during the production process. Field name: StockOffst. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property LegalText() As String` [R/W] Legal Text defined on the warehouse level. Field name: LegalText. Length: 250 characters.
- `Public Property Location() As Long` [R/W] Sets or returns the code of the geographical area inside the warehouse. The locations can be defined through the WarehouseLocations object. Field name: location.
- `Public Property ManageSerialAndBatchNumbers() As BoYesNoEnum` [R/W] property ManageSerialAndBatchNumbers
- `Public Property NegativeInventoryAdjustmentAccount() As String` [R/W] Sets or returns the negative stock adjustment Account. Field name: NegStckAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property Nettable() As BoYesNoEnum` [R/W] property Nettable
  - remarks: Determines whether or not the warehouse participates in the Material Requirement Planning (MRP). Field name: Nettable.
- `Public Property PriceDifferencesAccount() As String` [R/W] Sets or returns the G/L account associated with Price Differences Account. Field name: PriceDifAc. Length: 15 characters.
- `Public Property PurchaseAccount() As String` [R/W] Sets or returns the G/L account associated with Purchases. Field name: PurchaseAc. Length: 15 characters.
- `Public Property PurchaseBalanceAccount() As String` [R/W] property PurchaseBalanceAccount
- `Public Property PurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with Purchase Credit Account. Field name: APCMAct. Length: 15 characters.
- `Public Property PurchaseOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Offsetting. Field name: PurchOfsAc. Length: 15 characters.
- `Public Property PurchaseReturningAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Returning account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property ReceiveUpToMaxQuantity() As BoYesNoEnum` [R/W] property ReceiveUpToMaxQuantity
- `Public Property ReceiveUpToMaxWeight() As BoYesNoEnum` [R/W] property ReceiveUpToMaxWeight
- `Public Property ReceiveUpToMethod() As ReceivingUpToMethodEnum` [R/W] property ReceiveUpToMethod
- `Public Property ReceivingBinLocationsBy() As ReceivingBinLocationsMethodEnum` [R/W] The method by which items are received at receiving bin locations. Field name: RecItemsBy.
- `Public Property RestrictReceiptToEmptyBinLocation() As BoYesNoEnum` [R/W] property RestrictReceiptToEmptyBinLocation
- `Public Property ReturningAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Returning Account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property RevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Revenues Account. Field name: RevenuesAc. Length: 15 characters.
- `Public Property SalesCreditAcc() As String` [R/W] Sets or returns the G/L account associated with Sales Credit EU Account. Field name: ARCMEUAct. Length: 15 characters.
- `Public Property SalesCreditEUAcc() As String` [R/W] Sets or returns the G/L account associated with Sales Credit EU Account. Field name: ARCMEUAct . Length: 15 characters.
- `Public Property SalesCreditForeignAcc() As String` [R/W] Sets or returns the G/L account associated withSales Credit EU Account. Field name: ARCMFrnAct . Length: 15 characters.
- `Public Property ShippedGoodsAccount() As String` [R/W] Sets or returns the G/L account associated with Shipping Goods Account. Field name: ShpdGdsAct. Length: 15 characters.
  - remarks: This is a foreign key to ChartOfAccounts Object.
- `Public Property Shipper() As String` [R/W] property Shipper
- `Public Property State() As String` [R/W] Sets or returns the state code of the sub-component of the warehouse address. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property StockAccount() As String` [R/W] Sets or returns the G/L account associated to stock in continues stock system. Length: 15 characters. Field name: BalInvntAc.
- `Public Property StockInflationAdjustAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Inflation Adjust. Length: 15 characters. Field name: IncreasAc.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property StockInflationOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Inflation Offset. Field name: DecreasAc. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property StockInTransitAccount() As String` [R/W] The stock in transit G/L account for this warehouse. Field name: StkInTnAct
- `Public Property Storekeeper() As Long` [R/W] property Storekeeper
- `Public Property Street() As String` [R/W] Sets or returns the street subcomponent of the warehouse address. Field name: street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] property StreetNo
- `Public Property TaxGroup() As String` [R/W] Sets or returns the sales tax code as defined in SalesTaxCodes object. Field name: VatGroup. Length: 8 characters.
- `Public Property TaxOffice() As String` [R/W] property TaxOffice
- `Public Property TransfersAcc() As String` [R/W] Sets or returns the G/L account associated with Stock Transfers. Field name: TransferAc. Length: 15 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object. Field name: userSign2.
- `Public Property VarianceAccount() As String` [R/W] Sets or returns the G/L account associated with Variance Account. Field name: VarianceAc. Length: 15 characters.
- `Public Property VATInRevenueAccount() As String` [R/W] Sets or returns the G/L account associated with VAT in Revenues. Field name: VatRevAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the Warehouse identification key. Mandatory field. Field name: WhsCode. Length: 8 characters.
- `Public Property WarehouseName() As String` [R/W] Sets or returns the warehouse name. Field name: WhsName. Length: 100 characters.
- `Public Property WHIncomingCenvatAccount() As String` [R/W] Sets or returns the Incoming CENVAT Account (WH) for Account Setting in Warehouses Definition. Applicable for cluster B only (country-specific for India). Field name: WhICenAct.
- `Public Property WHOutgoingCenvatAccount() As String` [R/W] Sets or returns the Outgoing CENVAT Account (WH) for Account Setting in Warehouse Definition. Applicable for cluster B only (country-specific for India). Field name: WhOCenAct.
- `Public Property WHShipToName() As String` [R/W] Sets or returns the Ship-to Name (WH) in Warehouses Definition. Applicable for cluster B only (country-specific for India). Field name: WhShipTo.
- `Public Property WIPMaterialAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP). Field name: WipAcct. Length: 15 characters.
  - remarks: Work In Prog account is used for posting transactions such as, transferring row material from the warehouse to the production floor.
- `Public Property WIPMaterialVarianceAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP) differences. That is, the account for posting differences between the value of the row material (before production) and the value of the complete product (after production). Field name: WipVarAcct. Length: 15 characters.
- `Public Property WipOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to a WIP (work in progress) account used within production transactions and for change of value of the WIP account during the production process. Field name: WipOffset. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property ZipCode() As String` [R/W] Sets or returns the Zip Code of the warehouse address. Field name: ZipCode. Length: 20 characters.

## Methods (7)
- `Public Function Add() As Long` Adds a new record to the Warehouses table. Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Retrieves the XML schema of the data structure. Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal WhsCode As String) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database. Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `WhsCode`: Warehouse code as a string (WarehouseCode).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key you can use the DataBrowser object. To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Removes a specified field from the table. Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Warning: when removing a field, all it's content is lost. You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data. Saves the object data to XML formatted data.
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
  - returns: Determines weather the update succeeded or failed. If the method succeeds, it returns 0. Otherwise, it returns an error code. Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Updates the object data in the company database. Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# WarehouseSublevelCode (Object)

You can set up different codes for each warehouse sublevel. Source table: OBSL.

## Properties (4)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As String` [R/W] The code for the warehouse sublevel. Field name: SLCode. Length: 50 characters.
- `Public Property Description() As String` [R/W] The description of the warehouse sublevel code. Field name: Descr. Length: 50 characters.
- `Public Property WarehouseSublevel() As Long` [R/W] The warehouse sublevel for which you want to define the codes. Field name: FldAbs.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WarehouseSublevelCodeCollectionParams (Collection)

A collection of WarehouseSublevelCodeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As WarehouseSublevelCodeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As WarehouseSublevelCodeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WarehouseSublevelCodeParams (Object)

Holds the key to an existing warehouse sublevel code. This object is used to pass keys to and retrieve keys from WarehouseSublevelCodesService methods.

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property Code() As String` [R/W] The code for the warehouse sublevel. Field name: SLCode. Length: 50 characters.
- `Public Property WarehouseSublevel() As Long` [R/W] The warehouse sublevel for which you want to define the codes. Field name: FldAbs.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WarehouseSublevelCodesService (Object)

The WarehouseSublevelCodesService service enables you to add, look up, update, and remove warehouse sublevel codes. Source table: OBSL.

**Remarks:** To access the Warehouse Sublevel Codes - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Bin Locations --> Warehouse Sublevel Codes.

## Methods (8)
- `Public Function Add(ByVal pIWarehouseSublevelCode As WarehouseSublevelCode) As WarehouseSublevelCodeParams` Adds a warehouse sublevel code.
  - param `pIWarehouseSublevelCode`: The data for the new warehouse sublevel code.
- `Public Sub Delete(ByVal pIWarehouseSublevelCodeParams As WarehouseSublevelCodeParams)` Deletes an existing warehouse sublevel code.
  - param `pIWarehouseSublevelCodeParams`: The key of the warehouse sublevel code to be deleted.
- `Public Function Get(ByVal pIWarehouseSublevelCodeParams As WarehouseSublevelCodeParams) As WarehouseSublevelCode` The warehouse sublevel code is specified by its key, which is contained in the WarehouseSublevelCodeParams object passed to the method.
  - param `pIWarehouseSublevelCodeParams`: The key of the warehouse sublevel code to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As WarehouseSublevelCodesServiceDataInterfaces) As Object` Creates an empty data structure for use with the WarehouseSublevelCodesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `WarehouseSublevelCodesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetList() As WarehouseSublevelCodeCollectionParams` Returns the WarehouseSublevelCodeCollectionParams data collection that identifies all warehouse sublevel codes.
- `Public Sub Update(ByVal pIWarehouseSublevelCode As WarehouseSublevelCode)` Updates an existing warehouse sublevel code.
  - param `pIWarehouseSublevelCode`: The data for the warehouse sublevel code to be updated. The WarehouseSublevelCode object must contain the key of the object to be updated.

# WeightMeasures (Object)

The WeightMeasures object enables to define the weight measure units that are used for item records. Source table: OWGT.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Inventory --> Weight UoM.

## Properties (6)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property UnitCode() As Long` [R] Returns the weight unit code (primary key). Field name: UnitCode.
- `Public Property UnitDisplay() As String` [R/W] Sets or returns the displayed name of the weight unit (for example, kg). Field name: UnitDisply. Length: 2 characters.
- `Public Property UnitName() As String` [R/W] Sets or returns the unit name (for example, Kilogram). Field name: UnitName. Length: 20 characters.
- `Public Property UnitWeightinmg() As Double` [R/W] Sets or returns the weight in miligrams. For example: 1,000,000 mg for Kg measure unit or 28,300 mg for Oz measure unit. Field name: WightInMG.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a weight unit of measure definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lUnitCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lUnitCode`: UnitCode.
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

# WIPMapping (Object)

WIPMapping Class

## Properties (4)
- `Public Property AbsoluteEntry() As Long` [R] property AbsoluteEntry
- `Public Property AccountFrom() As String` [R/W] property AccountFrom
- `Public Property AccountTo() As String` [R/W] property AccountTo
- `Public Property LineNumber() As Long` [R] property LineNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WIPMappingCollection (Collection)

WIPMappingCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As WIPMapping` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As WIPMapping` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WithholdingTaxCertificates (Object)

WithholdingTaxCertificates Class

## Properties (16)
- `Public Property Certificate() As String` [R/W] property Certificate
- `Public Property Count() As Long` [R] property Count
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property Number() As Long` [R/W] property Number
- `Public Property PeriodIndicator() As String` [R] property PeriodIndicator
- `Public Property POICode() As String` [R/W] property POICode
- `Public Property POICodeRef() As String` [R/W] property POICodeRef
- `Public Property Series() As Long` [R/W] property Series
- `Public Property SumAccumulatedAmount() As Double` [R] property SumAccumulatedAmount
- `Public Property SumBaseAmount() As Double` [R] property SumBaseAmount
- `Public Property SumDocTotal() As Double` [R] property SumDocTotal
- `Public Property SumPerceptAmount() As Double` [R] property SumPerceptAmount
- `Public Property SumVATAmount() As Double` [R] property SumVATAmount
- `Public Property WhtAbsId() As Long` [R/W] property WhtAbsId
- `Public Property WTaxType() As String` [R] property WTaxType
- `Public Property WTGroups() As WTGroups` [R] property WithholdingCertificateWTC1

## Methods (2)
- `Public Sub Add()` method Add
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# WithholdingTaxCodes (Object)

The WithholdingTaxCodes object enables to define the system withholding tax codes that can be applied to business partners, payments, and documents. Source table: OWHT.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Financials --> Tax --> Withholding Tax. Mandatory properties (for India): APCessAccount, APHSCAccount, APSurchargeAccount, APTDSAccount, ARCessAccount, ARHSCAccount, ARSurchargeAccount, ARTDSAccount, Assessee, Location, ReturnType, Section

## Properties (59)
- `Public Property Account() As String` [R/W] Sets or returns the G/L account for withholding tax postings. Field name: Account. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT).
- `Public Property APCessAccount() As String` [R/W] An A/P cess account associated with this withholding tax code. Field name: ApCessAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property APCessGSTAccount() As String` [R/W] property APCessGSTAccount
- `Public Property APCessInterimAccount() As String` [R/W] An A/P cess interim account associated with this withholding tax code. Field name: ApCesInAcc Length: 15 characters.
- `Public Property APCGSTAccount() As String` [R/W] property APCGSTAccount
- `Public Property APHSCAccount() As String` [R/W] An A/P HSC account associated with this withholding tax code. Field name: ApHscAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property APHSCInterimAccount() As String` [R/W] An A/P HSC interim account associated with this withholding tax code. Field name: ApHscInAcc Length: 15 characters.
- `Public Property APIGSTAccount() As String` [R/W] property APIGSTAccount
- `Public Property APSGSTAccount() As String` [R/W] property APSGSTAccount
- `Public Property APSurchargeAccount() As String` [R/W] An A/P surcharge account associated with this withholding tax code. Field name: ApSurAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property APSurchargeInterimAccount() As String` [R/W] An A/P surcharge interim account associated with this withholding tax code. Field name: ApSurInAcc Length: 15 characters.
- `Public Property APTCSInterimAccount() As String` [R/W] An A/P TCS interim account associated with this withholding tax code. Field name: ApTcsInAcc Length: 15 characters.
- `Public Property APTDSAccount() As String` [R/W] An A/P TDS account associated with this withholding tax code. Field name: ApTdsAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property APUTGSTAccount() As String` [R/W] property APUTGSTAccount
- `Public Property ARCessAccount() As String` [R/W] An A/R cess account associated with this withholding tax code. Field name: ArCessAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property ARCessGSTAccount() As String` [R/W] property ARCessGSTAccount
- `Public Property ARCessInterimAccount() As String` [R/W] An A/R cess interim account associated with this withholding tax code. Field name: ArCesInAcc Length: 15 characters.
- `Public Property ARCGSTAccount() As String` [R/W] property ARCGSTAccount
- `Public Property ARHSCAccount() As String` [R/W] An A/R HSC account associated with this withholding tax code. Field name: ArHscAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property ARHSCInterimAccount() As String` [R/W] An A/R HSC interim account associated with this withholding tax code. Field name: ArHscInAcc Length: 15 characters.
- `Public Property ARIGSTAccount() As String` [R/W] property ARIGSTAccount
- `Public Property ARSGSTAccount() As String` [R/W] property ARSGSTAccount
- `Public Property ARSurchargeAccount() As String` [R/W] An A/R surcharge account associated with this withholding tax code. Field name: ArSurAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property ARSurchargeInterimAccount() As String` [R/W] An A/R surcharge interim account associated with this withholding tax code. Field name: ArSurInAcc Length: 15 characters.
- `Public Property ARTCSInterimAccount() As String` [R/W] An A/R TCS interim account associated with this withholding tax code. Field name: ArTcsInAcc Length: 15 characters.
- `Public Property ARTDSAccount() As String` [R/W] An A/R TDS account associated with this withholding tax code. Field name: ArTdsAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property ARUTGSTAccount() As String` [R/W] property ARUTGSTAccount
- `Public Property Assessee() As Long` [R/W] An assessee associated with this withholding tax code. Field name: Assessee This is a foreign key to the ONOA (Nature of Assessee) table.
  - remarks: For India only.
- `Public Property BaseAmount() As Double` [R/W] Specifies the percentage of the base amount that is subject to withholding. Default value is 100%. Field name: PrctBsAmnt.
- `Public Property BaseType() As WithholdingTaxCodeBaseTypeEnum` [R/W] Sets or returns the base amount type on which to calculate withholding tax (Gross, Net, or VAT). Field name: BaseType.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Category() As WithholdingTaxCodeCategoryEnum` [R/W] Determines when the withholding tax code is posted: upon payment or upon invoice. Field name: Category.
- `Public Property Concessional() As BoYesNoEnum` [R/W] Indicates whether concession rates are applied. Field name: Concess.
  - remarks: For India only.
- `Public Property CSTCodeIncomingID() As Long` [R/W] property CSTCodeIncomingID
- `Public Property CSTCodeOutgoingID() As Long` [R/W] property CSTCodeOutgoingID
- `Public Property Currency() As String` [R/W] property Currency
- `Public Property EBooksWTaxCategory() As Long` [R/W] property EBooksWTaxCategory
- `Public Property Effectivefrom() As Date` [R] property EffectiveFrom
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property IsProgressiveTax() As BoYesNoEnum` [R/W] property IsProgressiveTax
- `Public Property Lines() As WithholdingTaxCodes_Lines` [R] Returns the WithholdingTaxCodes_Lines child object.
- `Public Property Location() As Long` [R/W] The location associated with this withholding tax code. Field name: Location This is a foreign key to the WarehouseLocations object.
  - remarks: For India only.
- `Public Property MinimumTaxableAmount() As Double` [R/W] property MinimumTaxableAmount
- `Public Property NatureOfCalculationBaseCode() As String` [R/W] property NatureOfCalculationBaseCode
- `Public Property NonDeductThreshold() As BoYesNoEnum` [R/W] Apply tax exemption after threshold. Field name: NoDedThrsh.
- `Public Property OfficialCode() As String` [R/W] Sets or returns the code for the withholding tax declaration report. Field name: OffclCode. Length: 4 characters.
- `Public Property Rate() As Double` [R] property Rate
- `Public Property ReturnType() As ReturnTypeEnum` [R/W] The return type associated with this witholding tax code. Field name: ReturnType
  - remarks: For India only.
- `Public Property RoundingType() As RoundingTypeEnum` [R/W] Determines the rounding type - Truncated AU or Commercial Values - for the withholding tax calculation. Field name: RoundType.
  - remarks: Country-specific for Australia and New Zealand.
- `Public Property Section() As Long` [R/W] A section associated with this witholding tax code. Field name: Section. This is a foreign key to the Section object.
  - remarks: For India only.
- `Public Property Surcharge() As Double` [R/W] A threshold limit for surcharges for this witholding tax code. Field name: Surcharge.
  - remarks: For India only.
- `Public Property TdsType() As TdsTypeEnum` [R/W] property TdsType
- `Public Property Threshold() As Double` [R/W] A threshold limit for this witholding tax code. Field name: Threshold.
  - remarks: For India only.
- `Public Property TransactonThreshold() As Double` [R/W] property TransactonThreshold
- `Public Property TypeID() As Long` [R/W] property TypeID
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WithholdingType() As WithholdingTypeEnum` [R/W] Determines whether the withholding tax code relates to VAT Withholding or Income Tax Withholding. Field name: Type.
  - remarks: Country-specific for Mexico and Chile.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code (primary key). Field name: WTCode. Length: 4 characters.
- `Public Property WTName() As String` [R/W] Sets or returns the withholding tax name. Field name: WTName. Length: 50 characters.

## Methods (7)
- `Public Function Add() As Long` Adds a withholding tax code definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrWtCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrWtCode`: WTCode.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You cannot delete a withholding tax code that is in use. You must use the GetByKey method to retrieve a valid object.
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
  - remarks: If the withholding tax code is in use, than only the eight A/R and A/P account fields can be updated. Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# WithholdingTaxCodes_Lines (Object)

WithholdingTaxCodes_Lines is a child object of the WithholdingTaxCodes object. It enables to define the tax percentage and the effective from date for the withholding tax code. Source table: WHT1.

**Remarks:** Mandatory property: Effectivefrom Mandatory properties (for India): CessRate, HSCRate, SurchargeRate, TDSRate To display the form in the application: - Select Administration --> Setup --> Financials --> Tax --> Withholding Tax. - Choose the Tax Definition button.

## Properties (22)
- `Public Property CessGSTRate() As Double` [R/W] property CessGSTRate
- `Public Property CessRate() As Double` [R/W] The cess rate.
- `Public Property CGSTRate() As Double` [R/W] property CGSTRate
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property Currency() As String` [R/W] Fixed amount currency. Field name: Currency. Length: 3 characters.
- `Public Property Effectivefrom() As Date` [R/W] Sets or returns the date from which the withholding tax percentage is effective. Mandatory property. Field name: EffecDate.
- `Public Property FixedAmount() As Double` [R/W] Fixed amount. Field name: FixedAmnt.
- `Public Property HSCRate() As Double` [R/W] The HSC rate.
  - remarks: For India only.
- `Public Property IGSTRate() As Double` [R/W] property IGSTRate
- `Public Property ITRNonCompliantRate() As Double` [R/W] TDS ITR noncompliance rate. Field name: ItrNCRate.
  - remarks: For India only.
- `Public Property LineNum() As Long` [R] The ID (line number) of the withholding tax line. Field name: LineNum
- `Public Property PANNonCompliantRate() As Double` [R/W] TDS PAN noncompliance rate. Field name: PanNCRate.
  - remarks: For India only.
- `Public Property ProgressiveTaxLines() As WithholdingTaxCodes_ProgressiveTax_Lines` [R] property ProgressiveTaxLines
- `Public Property Rate() As Double` [R/W] Sets or returns the percentage of the withholding tax. Field name: Rate.
- `Public Property SGSTRate() As Double` [R/W] property SGSTRate
- `Public Property SurchargeRate() As Double` [R/W] The surcharge rate.
  - remarks: For India only.
- `Public Property TDSRate() As Double` [R/W] The TDS rate. Field name: TdsRate.
  - remarks: For India only.
- `Public Property UoMCode() As String` [R] UoM code. Field name: UoMCode. Length: 20 characters.
- `Public Property UoMEntry() As Long` [R/W] UoM entry. Field name: UomEntry.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UTGSTRate() As Double` [R/W] property UTGSTRate
- `Public Property ValueRangeLines() As WithholdingTaxCodes_ValueRange_Lines` [R] property ValueRangeLines

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# WithholdingTaxCodes_ProgressiveTax_Lines (Object)

WithHoldingTaxCodes_ProgressiveTax_Lines Class

## Properties (5)
- `Public Property Count() As Long` [R] property Count
- `Public Property MaxAmount() As Double` [R/W] property MaxAmount
- `Public Property MinAmount() As Double` [R/W] property MinAmount
- `Public Property TaxRate() As Double` [R/W] property TaxRate
- `Public Property UserFields() As UserFields` [R] Get User Fields

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# WithholdingTaxCodes_ValueRange_Lines (Object)

WithHoldingTaxCodes_ValueRange_Lines Class

## Properties (5)
- `Public Property Count() As Long` [R] property Count
- `Public Property Rate() As Double` [R/W] property Rate
- `Public Property UserFields() As UserFields` [R] Get User Fields
- `Public Property ValueFrom() As Double` [R/W] property ValueFrom
- `Public Property WTaxToBeDeductible() As Double` [R/W] property WTaxToBeDeductible

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 
