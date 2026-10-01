<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
