<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
