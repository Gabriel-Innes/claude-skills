<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# AccountCategoriesParams (Collection)

A data collection of AccountCategoryParams.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of AccountCategoryParams instances in the collection.

## Methods (5)
- `Public Function Add() As AccountCategoryParams` Adds a new AccountCategoryParams object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As AccountCategoryParams` Returns a reference to a specified AccountCategoryParams object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AccountCategory (Object)

A data structure object related to the AccountCategoryService service. Source table: OACG.

## Properties (3)
- `Public Property CategoryCode() As Long` [R] Sets or returns a value specifying the category ID number. Field name: AbsID
- `Public Property CategoryName() As String` [R/W] Sets or returns a string specifying the account category name. Field name: Name.
- `Public Property CategorySource() As AccountCategorySourceEnum` [R/W] Sets or returns a valid value specifying the account category source: Balance Sheet or Profit and Loss. Supports the creation of the Cash Flow report. Field name: source.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AccountCategoryParams (Object)

Holds identification parameters for the AccountCategoryService (CategoryCode, CategoryName).

## Properties (2)
- `Public Property CategoryCode() As Long` [R/W] Sets or returns a value specifying the category ID number. Field name: AbsID
- `Public Property CategoryName() As String` [R] Sets or returns a string specifying the account category name. Field name: Name.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AccountCategoryService (Object)

This service allows you to manage account categories (add, delete, get by key, get list, and update) for use with the Copy Express add-on. Source table: OACG.

**Remarks:** Country-specific for US and Canada. System categories cannot be deleted or updated.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  'Company Service

  Dim oCompanyService As SAPbobsCOM.CompanyService

  'Account Category Service

  Dim AccCatService As SAPbobsCOM.AccountCategoryService

  'Get Company Service

  oCompanyService = oCompany.GetCompanyService

  'Get Category Service

  AccCatService = oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.AccountCategoryService)

  'Account Category Objects

  Dim AccCat, NewAcctCat As SAPbobsCOM.AccountCategory

  'Account Category Parameters

  Dim AccCatParams, NewAccCatParams As SAPbobsCOM.AccountCategoryParams

  'Get Account Category

  AccCatParams = AccCatService.GetDataInterface(SAPbobsCOM.AccountCategoryServiceDataInterfaces.acsAccountCategoryParams)

  AccCat = AccCatService.GetDataInterface(SAPbobsCOM.AccountCategoryServiceDataInterfaces.acsAccountCategory)

  AccCatParams.CategoryCode = 10

  AccCat = AccCatService.GetCategory(AccCatParams)

  'Get Account Category List

  Dim CategoryList As SAPbobsCOM.AccountCategoriesParams

  CategoryList = AccCatService.GetCategoryList

  'Add New Account Category

  NewAcctCat = AccCatService.GetDataInterface(SAPbobsCOM.AccountCategoryServiceDataInterfaces.acsAccountCategory)

  NewAcctCat.CategoryName = "New Account Category"

  NewAcctCat.CategorySource = SAPbobsCOM.AccountCategorySourceEnum.acsBalanceSheet

  NewAccCatParams = AccCatService.AddCategory(NewAcctCat)
  ```

## Methods (8)
- `Public Function AddCategory(ByVal pIAccountCategory As AccountCategory) As AccountCategoryParams` Adds an account category.
  - param `pIAccountCategory`: Specifies an AccountCategory object holding the properties of the category you want to add.
- `Public Sub DeleteCategory(ByVal pIAccountCategoryParams As AccountCategoryParams)` Deletes a category from the Balance Sheet or Profit and Loss report.
  - param `pIAccountCategoryParams`: Specifies an AccountCategoryParams object holding the name and code of the category you want to delete.
- `Public Function GetCategory(ByVal pIAccountCategoryParams As AccountCategoryParams) As AccountCategory` Returns an instance of AccountCategory object according to the specified AccountCatgoryParams object (CategoryCode, CategoryName).
  - param `pIAccountCategoryParams`: Specifies an AccountCategoryParams object holding Name and Code of the category you want to get.
- `Public Function GetCategoryList() As AccountCategoriesParams` Returns an AccountCategoriesParams collection holding all existing instances of AccountCategory object in the collection.
- `Public Function GetDataInterface(ByVal enumMSDI As AccountCategoryServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AccountCategoryServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - example note: Shows how to get an Openning Balance Account from an XML file.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As CompanyService

    Dim oAccountsService As AccountsService

    Dim oOpenBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oOpenBalanceAccountFrmFile As SAPbobsCOM.OpenningBalanceAccount

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oAccountsService = oCmpSrv.GetBusinessService(ServiceTypes.AccountsService)

    'get OpenBalanceAccount Data Interface

    oOpenBalanceAccount = oAccountsService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account number for the opening balance account

    oOpenBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'save data to xml file

    oOpenBalanceAccount.ToXMLFile("c:\MyAccount.xml")

    'create OpenBalanceAccount from xml file

    oOpenBalanceAccountFrmFile = oAccountsService.GetDataInterfaceFromXMLFile("c:\MyAccount.xml")
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: Specifies an XML string.
  - example note: Show to get an Openning Balance Account from an XML string.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As CompanyService

    Dim oAccountsService As AccountsService

    Dim oOpenBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oOpenBalanceAccountXmlStr As SAPbobsCOM.OpenningBalanceAccount

    Dim sOpenBalanceAccountXmlStr As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oAccountsService = oCmpSrv.GetBusinessService(ServiceTypes.AccountsService)

    'get OpenBalanceAccount Data Interface

    oOpenBalanceAccount = oAccountsService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account number for the opening balance account

    oOpenBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'save data to xml string

    sOpenBalanceAccountXmlStr = oOpenBalanceAccount.ToXMLString

    'create OpenBalanceAccount from xml string

    oOpenBalanceAccountXmlStr = oAccountsService.GetDataInterfaceFromXMLString(sOpenBalanceAccountXmlStr)
    ```
- `Public Sub UpdateCategory(ByVal pIAccountCategory As AccountCategory)` Replaces an instance of AccountCategory object with a new one.
  - param `pIAccountCategory`: Specifies the AccountCategory object you want to update.

# AccountSegmentationCategories (Object)

The AccountSegmentationCategories object represents the categories for each of the account segments in the Financials module. This object enables you to: - Add an account category to a segment. - Retrieve an account segment category by its key. - Update an account segment category. - Save the object in XML format. Source table: OASC.

**Remarks:** Applicable only when the EnableAccountSegmentation property of the CompanyInfo object is set to Y. Account segmentation is used mainly in USA. To display the form in the application: - Select Administration --> Setup -->Financials -->Account Segmentation. - Double-click the number on the left of the account segmentation name.

## Properties (6)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R/W] Sets or returns the code of the account segmentation category. Field name: Code. Length: 20 characters.
  - remarks: The length of the Code value must be according to the specified Size (maximum 20 characters). The characters type (alphanumeric or numeric) must be according to the specified Type (both properties are part of the AccountSegmentations object).
- `Public Property Name() As String` [R/W] Sets or returns the full name of the account segmentation category. Field name: Name. Length: 100 characters.
- `Public Property SegmentID() As Long` [R/W] Sets or returns the ID number of the account segmentation. This is a foreign key to the Numerator property of the AccountSegmentations object. Field name: SegmentId.
- `Public Property ShortName() As String` [R/W] Sets or returns the short name of the account segmentation category. Field name: ShortName. Length: 10 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds an account segment category.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lSegmentId As Long, ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lSegmentId`: Specifies the required SegmentID.
  - param `bstrCode`: Specifies the required Code.
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

# AccountSegmentations (Object)

The AccountSegmentations object represents the account segments in the Financials module. The default segments are: Division, Region, and Department. When creating a new company, before defining any accounts, this object enables you to: - Add up to 10 segments. - Retrieve a segment by its key. - Update a segment. - Save the object in XML format. After creating an account with segments, you can modify only the segment Name. Source table: OASG.

**Remarks:** Applicable only when the EnableAccountSegmentation property of the CompanyInfo object is set to Y. Account segmentation is used mainly in USA. To display the form in the application: - Select Administration --> Setup -->Financials -->Account Segmentation.

## Properties (7)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Categories() As AcctSegmnt_Categories` [R] The category of the account segmentation.
- `Public Property Name() As String` [R/W] Sets or returns the name of the account segmentation. Field name: Name. Length: 100 characters.
- `Public Property Numerator() As Long` [R] Returns the identification key of the account segmentation as assigned by SAP Business One when adding an account segmentation. Field name: AbsId.
- `Public Property Size() As Long` [R/W] Sets or returns the number of characters assigned for the account segment. Field name: Size.
  - remarks: The characters can be alphanumeric or numeric according to the Type property setting.
- `Public Property Type() As AccountSegmentationTypeEnum` [R/W] Sets or returns a valid value that determines wether or not the account segment is alphanumeric or numeric. Field name: Type.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds an account segment (up to 10).
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsID`: Specifies the required Numerator.
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

# AccountsService (Object)

The AccountsService enables to transfer credit or debit amounts from a specified opening balance account to one or more G/L accounts. This service creates a journal entry lines. Mandatory properties: - OpenBalanceAccount (OpenningBalanceAccount object) - Code (GLAccount object).

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method.

## Methods (4)
- `Public Sub CreateOpenBalance(ByVal pIOpenningBalanceAccount As OpenningBalanceAccount, ByVal pGLAccounts As GLAccounts)` Transfers credit or debit amounts from a specified opening balance account to one or more G/L accounts.
  - param `pIOpenningBalanceAccount`: Specifies the openning balance account.
  - param `pGLAccounts`: Specifies the G/L accounts collection.
  - example note: The following is a VB.NET sample that creates openning balances for two G/L accounts.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oAccountsService As SAPbobsCOM.AccountsService

    Dim oOpenningBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oGLAccounts As SAPbobsCOM.GLAccounts

    Dim oGLAccountFirst As SAPbobsCOM.GLAccount

    Dim oGLAccountSecond As SAPbobsCOM.GLAccount

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get accounts service

    oAccountsService = oCmpSrv.GetBusinessService(ServiceTypes.AccountsService)

    'get Accounts Service Data Interface

    oOpenningBalanceAccount = oAccountsService.GetDataInterface(AccountsServiceDataInterfaces.a sdiOpenningBalanceAccount)

    'set the account code(account name = Common Stock (HO, USA, GA ))

    'for the openning balance account

    oOpenningBalanceAccount.OpenBalanceAccount="_SYS00000000078"

    'set the details

    oOpenningBalanceAccount.Details = "G/L Accounts Opening Balance"

    'set the date

    oOpenningBalanceAccount.Date = Date.Today

    'get ref to GlAccounts

    oGLAccounts = oAccountsService.GetDataInterface(AccountsServiceDataInterfaces.a sdiGLAccounts)

    'add accounts that will be in credit or in debit

    'add first account

    oGLAccountFirst = oGLAccounts.Add

    'set the account code

    '(account name = "Sales Revenues - Services (HO, USA, GA )"

    oGLAccountFirst.Code ="_SYS00000000083"

    'set credit amount

    oGLAccountFirst.Credit = 300

    'add second account

    oGLAccountSecond = oGLAccounts.Add

    'set the account code

    '(account name = Sales Revenues - Foreign (HO, USA, GA ))

    oGLAccountSecond.Code ="_SYS00000000082"

    'set credit amount

    oGLAccountSecond.Credit = 300

    'create the balance for the first and second accounts from the Openning 'Balance Account

    oAccountsService.CreateOpenBalance(oOpenningBalanceAccount,    oGLAccounts)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As AccountsServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AccountsServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - example note: Shows how to get an Openning Balance Account from an XML file.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As CompanyService

    Dim oAccountsService As AccountsService

    Dim oOpenBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oOpenBalanceAccountFrmFile As SAPbobsCOM.OpenningBalanceAccount

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oAccountsService = oCmpSrv.GetBusinessService(ServiceTypes.AccountsService)

    'get OpenBalanceAccount Data Interface

    oOpenBalanceAccount = oAccountsService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account number for the opening balance account

    oOpenBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'save data to xml file

    oOpenBalanceAccount.ToXMLFile("c:\MyAccount.xml")

    'create OpenBalanceAccount from xml file

    oOpenBalanceAccountFrmFile = oAccountsService.GetDataInterfaceFromXMLFile("c:\MyAccount.xml")
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: Specifies an XML string.
  - example note: Show to get an Openning Balance Account from an XML string.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As CompanyService

    Dim oAccountsService As AccountsService

    Dim oOpenBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oOpenBalanceAccountXmlStr As SAPbobsCOM.OpenningBalanceAccount

    Dim sOpenBalanceAccountXmlStr As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oAccountsService = oCmpSrv.GetBusinessService(ServiceTypes.AccountsService)

    'get OpenBalanceAccount Data Interface

    oOpenBalanceAccount = oAccountsService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account number for the opening balance account

    oOpenBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'save data to xml string

    sOpenBalanceAccountXmlStr = oOpenBalanceAccount.ToXMLString

    'create OpenBalanceAccount from xml string

    oOpenBalanceAccountXmlStr = oAccountsService.GetDataInterfaceFromXMLString(sOpenBalanceAccountXmlStr)
    ```

# AccrualType (Object)

Represents an accrual type. Source table: OACR.

## Properties (6)
- `Public Property CalculationAccount() As String` [R/W] The cost accounting calculation account for the accrual type. Field name: CalcAcct. Length: 15 characters.
  - remarks: Amounts posted to this account appear in both the Financial Accounting and the Cost Accounting P/L sections of the cost accounting reconciliation report.
- `Public Property Code() As String` [R/W] The code of the accrual type. Field name: Code. Length: 8 characters.
- `Public Property InterimAccount() As String` [R/W] The cost accounting interim account for the accrual type. Field name: InterimAct. Length: 15 characters.
  - remarks: Amounts posted to this account appear in both the Financial Accounting and the Cost Accounting Correction sections of the cost accounting reconciliation report.
- `Public Property Name() As String` [R/W] The name of the accrual type. Field name: Name. Length: 30 characters.
- `Public Property PostingAccount() As String` [R/W] The cost accounting posting account for the accrual type. Field name: PostingAct. Length: 15 characters.
  - remarks: Amounts posted to this account appear in both the Financial Accounting and the Cost Accounting Correction sections of the cost accounting reconciliation report.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AccrualTypeParams (Object)

Holds the key of an accrual type. This object is used to pass keys to and retrieve keys from AccrualTypesService methods. Source table: OACR.

## Properties (1)
- `Public Property Code() As String` [R/W] The key for a specific accrual type. Field name: Code.

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

# AccrualTypes (Collection)

A collection of AccrualType objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AccrualType` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AccrualType` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AccrualTypesParams (Collection)

A collection of AccrualTypeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AccrualTypeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AccrualTypeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AccrualTypesService (Object)

An accrual type is a set of conditions used to represent the differences between cost accounting and financial accounting. The AccrualTypesService service enables you to add, look up, update, and remove accrual types. Source table: OACR.

**Remarks:** Accrual types are defined only for use in the cost accounting reconciliation report. They do not affect other reports. To define accrual types, in the SAP Business One application, choose Financials --> Cost Accounting --> Accrual Type.

## Methods (8)
- `Public Function AddAccrualType(ByVal pIAccrualType As AccrualType) As AccrualTypeParams` Adds an accrual type.
  - param `pIAccrualType`: The data for the new accrual type.
- `Public Sub DeleteAccrualType(ByVal pIAccrualTypeParams As AccrualTypeParams)` Deletes an existing accrual type.
  - param `pIAccrualTypeParams`: The key of the accrual type to be deleted.
- `Public Function GetAccrualType(ByVal pIAccrualTypeParams As AccrualTypeParams) As AccrualType` Retrieves an accrual type. The accrual type is specified by its key, which is contained in the AccrualTypeParams object passed to the method.
  - param `pIAccrualTypeParams`: The key of the accrual type to retrieve.
- `Public Function GetAccrualTypeList() As AccrualTypesParams` Returns the AccrualTypesParams data collection that identify all accrual types.
- `Public Function GetDataInterface(ByVal enumMSDI As AccrualTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the AccrualTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AccrualTypesServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Sub UpdateAccrualType(ByVal pIAccrualType As AccrualType)` Updates an existing accrual type. The data for the accrual type, including the key of the accrual type to be updated, is contained in the AccrualType object passed to the method. To update an accrual type, you must first retrieve it using the GetAccrualType method.
  - param `pIAccrualType`: The data for the accrual type to be updated. The AccrualType object must contain the key of the object to be updated.

# AcctSegmnt_Categories (Object)

The category of the account segmentation. Source table: OASC.

## Properties (4)
- `Public Property Code() As String` [R/W] The code of the segment. Field name: Code. Length: 20 characters.
  - remarks: You can use the digit 0 in a segment code. For example, if the segment size is 3, you can enter values such as 000 or 001.
- `Public Property Name() As String` [R/W] The name of the segment. Field name: Name. Length: 100 characters.
- `Public Property SegmentID() As Long` [R/W] The ID of the segment. Field name: SegmentId.
- `Public Property ShortName() As String` [R/W] The short name of the segment. SAP Business One uses this short name when creating automatic names for your G/L accounts. Field name: ShortName. Length: 10 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ActivitiesParams (Collection)

A collection of ActivityParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ActivityParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ActivityParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ActivitiesService (Object)

The ActivitiesService service enables you to add, look up, remove, and update single activities and recurring activities. Source table: OCLG.

**Remarks:** To display the form in the application, choose Business Partners --> Activities.

## Methods (13)
- `Public Function AddActivity(ByVal pIActivity As Activity) As ActivityParams` Adds a new activity.
  - param `pIActivity`: The data for the new activity.
  - C# example (from SAP's help):
    ```csharp
    ActivitiesService oActSrv = (ActivitiesService)oCmpSrv.GetBusinessService(ServiceTypes.ActivitiesService);
    Activity oAct = (Activity)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivity);
    ActivityParams oParams;
    oAct.CardCode = "C001";
    oAct.ContactDate = DateTime.Parse("15/01/2010");
    oAct.Activity = BoActivities.cn_Conversation;
    oAct.Notes = "Discuss next year's financial plan";
    oParams = oActSrv.AddActivity(oAct);
    long singleActCode = oParams.ActivityCode;
    ```
  - C# example (from SAP's help):
    ```csharp
    oAct = (Activity)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivity);
    oAct.CardCode = "C002";
    oAct.ContactDate = DateTime.Parse("16/01/2010");
    oAct.Activity = BoActivities.cn_Meeting;
    oAct.Notes = "Monthly team meeting";
    oAct.StartDate = DateTime.Parse("18/02/2010");
    oAct.StartTime = DateTime.Parse("16:30:00");
    oAct.EndDate = DateTime.Parse("18/12/2010");
    oAct.EndTime = DateTime.Parse("17:30:00");
    oAct.RecurrencePattern = RecurrencePatternEnum.rpMonthly;
    oAct.EndType = EndTypeEnum.etByCounter;
    oAct.MaxOccurrence = 10;
    oAct.Interval = 1;
    oAct.RepeatOption = RepeatOptionEnum.roByDate;
    oParams = oActSrv.AddActivity(oAct);
    long seriesActCode = oParams.ActivityCode;
    ```
- `Public Sub DeleteActivity(ByVal pIActivityParams As ActivityParams)` Deletes an existing activity.
  - param `pIActivityParams`: The key of the activity to be deleted.
- `Public Sub DeleteSingleInstanceFromSeries(ByVal pIActivityInstanceParams As ActivityInstanceParams)` Deletes a single instance from an existing recurring activity series.
  - param `pIActivityInstanceParams`: The key of the activity instance to be deleted.
  - C# example (from SAP's help):
    ```csharp
    oInstanceParams.ActivityCode = seriesActCode;
    oInstanceParams.InstanceDate = DateTime.Parse("18/04/2010");
    oActSrv.DeleteSingleInstanceFromSeries(oParams);
    ```
- `Public Function GetActivity(ByVal pIActivityParams As ActivityParams) As Activity` Retrieves an activity. The activity is specified by its key, which is contained in the ActivityParams object passed to the method.
  - param `pIActivityParams`: The key of the activity to retrieve.
- `Public Function GetActivityList() As ActivitiesParams` Returns the ActivitiesParams data collection that identify all activities.
- `Public Function GetDataInterface(ByVal enumMSDI As ActivitiesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ActivitiesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ActivitiesServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetListByAttendUser(ByVal pIActivity As Activity) As ActivitiesParams` GetListByAttendUser
  - param `pIActivity`: 
- `Public Function GetSingleInstanceFromSeries(ByVal pIActivityInstanceParams As ActivityInstanceParams) As Activity` Retrieves a single instance from a recurring activity series. The activity instance is specified by its key, which is contained in the ActivityInstanceParams object passed to the method.
  - param `pIActivityInstanceParams`: The key of the activity instance to retrieve.
- `Public Function GetTopNActivityInstances(ByVal pActivityInstancesListParams As ActivityInstancesListParams) As ActivityInstancesParams` Retrieves the top N activity instances.
  - param `pActivityInstancesListParams`: The key of the activity instance list to retrieve.
- `Public Sub UpdateActivity(ByVal pIActivity As Activity)` Updates an existing activity. The data for the activity, including the key of the activity to be updated, is contained in the Activity object passed to the method. To update an activity, you must first retrieve it using the GetActivity method.
  - param `pIActivity`: The data for the activity to be updated. The Activity object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    //Get a single activity or a modified activity from a series
    oParams = (ActivityParams)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivityParams);
    oParams.ActivityCode = singleActCode;
    Activity oGet = oActSrv.GetActivity(oParams);
    oGet.Notes = "Discuss next year's financial plan and training plan";

    //update a single activity, or an already modified activity from a series
    oActSrv.UpdateActivity(oGet);
    ```
  - C# example (from SAP's help):
    ```csharp
    //Get an activity series
    oParams = (ActivityParams)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivityParams);
    oParams.ActivityCode = seriesActCode;
    oGet = oActSrv.GetActivity(oParams);
    oGet.StartTime = DateTime.Parse("16:00:00");

    //Update the whole series
    oActSrv.UpdateActivity(oGet);
    ```
- `Public Function UpdateSingleInstanceInSeries(ByVal pIActivity As Activity) As ActivityParams` Updates an existing single instance from a recurring activity series. The data for the activity, including the key of the activity to be updated, is contained in the Activity object passed to the method. To update an activity instance, you must first retrieve it using the GetSingleInstanceFromSeries method.
  - param `pIActivity`: The data for the single activity instance to be updated. The Activity object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    //Get a single instance from a series
    ActivityInstancesParams oInstanceParams = (ActivityInstancesParams)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivityInstancesParams);
    oInstanceParams.ActivityCode = seriesActCode;
    oInstanceParams.InstanceDate = DateTime.Parse("18/03/2010");
    oGet = oActSrv.GetSingleInstanceFromSeries(oParams);
    oGet.StartTime = DateTime.Parse("15:30:00");

    //Update a single activity from a series
    oActSrv.UpdateSingleInstanceInSeries(oGet);
    ```

# Activity (Object)

Activities refer to interactions you have with business partners, such as phone calls, meetings, tasks, and so on. All activities are automatically recorded in your calendar and in activity reports. In phone calls, meetings, and tasks, you can use recurring activities. Source table: OCLG.

## Properties (74)
- `Public Property Activity() As BoActivities` [R/W] Sets or returns a valid value of BoActivities type that specifies an activity with the business partner. Field name: Action.
- `Public Property ActivityCheckIns() As ActivityCheckInCollection` [R] property ActivityCheckIns
- `Public Property ActivityCode() As Long` [R] The code of the activity. Field name: ClgCode.
- `Public Property ActivityDate() As Date` [R/W] The contact date. Field name: CntctDate.
- `Public Property ActivityRecipients() As ActivityMultipleRecipientCollection` [R] The activity recipients when you select the Multiple Recipients option.
- `Public Property ActivityTime() As Date` [R/W] The activity time. Field name: CntctTime.
- `Public Property ActivityType() As Long` [R/W] The type of the activity. Field name: CntctType. This is a foreign key to the ActivityTypes object.
  - remarks: You can add new activity types to the list using the ActivityTypes object.
- `Public Property AddressName() As String` [R/W] The name of the address. Field name: AddrName. Length: 50 characters.
- `Public Property AddressType() As BoAddressType` [R/W] The type of the address. Field name: AddrType.
- `Public Property AttachmentEntry() As Long` [R/W] The identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to an alert message. Field name: AtcEntry.
- `Public Property BelongedSeriesNum() As Long` [R] The activity number of the series. Modified occurrence uses this field to link with the recurring series. Field name: SeriesNum.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Mandatory field in SAP Business One only if the activity is not personal. Length: 15 characters. This is a foreign key to the BusinessPartners object.
  - remarks: Mandatory property. SAP Business One validates the CardCode, and if not valid, returns an error code.
- `Public Property City() As String` [R/W] The city in which the activity (Meeting type only) with the business partner takes place. Field name: city. Length: 100 characters.
- `Public Property Closed() As BoYesNoEnum` [R/W] Specifies whether or not the activity is closed and no further processing is required. Field name: Closed.
  - remarks: You can use the CloseDate property to find out the closing date.
- `Public Property CloseDate() As Date` [R/W] The closing date of the activity. Field name: CloseDate.
  - remarks: In case the end user does not enter a value, the system completes the closing date automatically.
- `Public Property ContactPersonCode() As Long` [R/W] The internal code for the contact person. Field name: CntctCode. Mandatory property. This is a foreign key to the ContactEmployees object.
- `Public Property Country() As String` [R/W] The country in which the activity (Meeting type only) with the business partner takes place. Field name: country. Length: 3 characters. This is a foreign key to the Countries table (OCRY).
- `Public Property Details() As String` [R/W] The details for the next action. Field name: Details. Length: 60 characters.
- `Public Property DocEntry() As String` [R/W] The document entry key. Field name: DocEntry. Length: 20 characters.
  - remarks: You can use this key to reference a document.
- `Public Property DocNum() As String` [R] The number of the linked document. Field name: DocNum. Length: 20 characters.
- `Public Property DocType() As String` [R/W] The type of the document, such as invoice or purchase order, that is linked to the activity. Field name: DocType.
- `Public Property DocTypeEx() As String` [R/W] The document type that is linked to the activity. This property replaces the DocType property (integer). Length: 20 characters. Field name: DocNum.
  - remarks: The valid values are: '13' - 'A/R Invoice' '14' - 'A/R Credit Memo' '15' - 'Delivery' '16' - 'Return' '17' - 'Sales Order' '18' - 'A/P Invoice' '19' - 'A/P Credit Memo' '20' - 'Goods Receipt PO' '21' - 'Goods Return' '22' - 'Purchase order' '23' - 'Sales Quotation' '24' - 'Incoming Payment' '25' - 'Deposit' '30' - 'Journal Entry' '46' - 'Outgoing Payment' '57' - 'Checks for Payment' '59' - 'Goods Receipt' '60' - 'Goods Issue' '1250000001' - 'Stock Transfer Request' '67' - 'Stock Transfer' '68' - 'Work Order' '69' - 'Landed Costs' '132' - 'Correction Invoice' '162' - 'Material Revaluation' '202' - 'Production Order' '203' - 'AR Down Payment' '204' - 'AP Down Payment' '140000009' - 'Outgoing Excise Invoice' '140000010' - 'Incoming Excise Invoice' '-1' - '' '0' - '' '4' - 'Items' '163' - 'AP Correction Invoice' '164' - 'AP Correction Invoice Reversal' '165' - 'AR Correction Invoice' '166' - 'AR Correction Invoice Reversal' '1320000012' - 'Campaign' '540000006' - 'Purchase Quotation' '1250000025' - 'Blanket Agreements' '1470000113' - 'Purchase Request' '112' - 'Document Drafts' '140' - 'Payment Drafts' '123' - 'Checks for Payment Drafts' '254000065' - 'Self Invoice' '254000066' - 'Self Credit Note' '234000031' - 'Return Request' '234000032' - 'Goods Return Request' '1250000026' - 'Sales Blanket Agreement' '1250000027' - 'Purchase Blanket Agreement'
- `Public Property Duration() As Double` [R/W] The amount of time scheduled for the activity. Field name: Duration.
  - remarks: The duration value specifies the number of minutes, hours, or days according to the DurationType. The duration value must be equal to or greater than 0. In case the start time (days + hours) and end time (days + hours) are specified, then the system recalculates the duration time.
- `Public Property DurationType() As BoDurations` [R/W] Sets or returns a valid value of BoDurations type that specifies the duration type for the activity (minutes, hours, or days). Field name: DurType.
- `Public Property EndDuedate() As Date` [R/W] The due date for completing the activity. Field name: endDate.
  - remarks: The end date must be later than the start date.
- `Public Property EndTime() As Date` [R/W] The end time (hh:mm) of the activity. Field name: ENDTime.
  - remarks: The end time must be later than the start time.
- `Public Property endType() As EndTypeEnum` [R/W] The end type of the recurring activity. It is only available for Phone Call, Meeting, or Task, when the value of the recurrence pattern is not None. Field name: EndType.
- `Public Property Fax() As String` [R/W] The fax number of the contact person. Field name: Fax. Length: 20 characters.
- `Public Property Friday() As BoYesNoEnum` [R/W] Defines whether the recurring activity occurs on Friday. Used in a weekly pattern. Field name: Friday.
- `Public Property HandledBy() As Long` [R/W] The name or title of the person who is responsible for entering the activity details. Field name: AttendUser. This is a foreign key to the Users object.
- `Public Property HandledByEmployee() As Long` [R/W] The employee who handles the activity. Field name: AttendEmpl.
- `Public Property HandledByRecipientList() As Long` [R/W] property HandledByRecipientList
- `Public Property Inactiveflag() As BoYesNoEnum` [R/W] Specifies whether or not the activity is inactive. Field name: inactive.
- `Public Property Interval() As Long` [R/W] The frequency for the recurring activity. It is only available for Phone Call, Meeting, or Task, when the value of the recurrence pattern is not None. Field name: Interval.
- `Public Property IsRemoved() As BoYesNoEnum` [R] Indicates whether an occurrence is removed from the recurring series. Field name: IsRemoved.
- `Public Property Location() As Long` [R/W] The code for the activity location. Field name: Location. This is a foreign key to the ActivityLocations object.
  - remarks: You can add new locations to the list using the ActivityLocations object.
- `Public Property MaxOccurrence() As Long` [R/W] The recurring activity ends after a certain number of occurrences. Field name: MaxOccur.
- `Public Property Monday() As BoYesNoEnum` [R/W] Defines whether the recurring activity occurs on Monday. Used in a weekly pattern. Field name: Monday.
- `Public Property Notes() As String` [R/W] Sets or returns a memo type string that specifies remarks regarding the activity. Field name: Notes. Length: 16 characters.
- `Public Property Office365EventId() As String` [R/W] Office 365 Event ID. Field name: Of365EvtId. Length: 200 characters.
- `Public Property ParentobjectId() As Long` [R] The source object ID of the activity: - For Service Call object type: ServiceCallID. - For Sales Opportunity object type: SequentialNo. Field name: parentId.
- `Public Property Parentobjecttype() As String` [R] The source object type of the activity: Sales Opportunity or Service Call. Field name: parentType. Length: 20 characters.
- `Public Property Personalflag() As BoYesNoEnum` [R/W] Specifies whether the activity is personal or business. If business, you must set the business partner details (CardCode). Field name: personal.
- `Public Property Phone() As String` [R/W] The phone number of the contact person. Field name: Tel. Length: 50 characters.
- `Public Property PreviousActivity() As Long` [R/W] The previous activity code related to the current activity. Field name: prevActvty.
- `Public Property Priority() As BoMsgPriorities` [R/W] Sets or returns a valid value of BoMsgPriorities type that specifies the priority of the activity (low, normal, or high). Field name: Priority.
- `Public Property RecurrenceDayInMonth() As Long` [R/W] For monthly activities, specify the days when the activity recurs. Field name: DayInMonth.
- `Public Property RecurrenceDayOfWeek() As RecurrenceDayOfWeekEnum` [R/W] For monthly activities, specify the days when the activity recurs. Field name: DayOfWeek.
- `Public Property RecurrenceMonth() As Long` [R/W] Specify the month when the activity recurs. Field name: Month.
- `Public Property RecurrencePattern() As RecurrencePatternEnum` [R/W] Used for setting recurring activities. It is only available for Phone Call, Meeting, or Task. Field name: RecurPat.
- `Public Property RecurrenceSequenceSpecifier() As RecurrenceSequenceSpecifierEnum` [R/W] The recurrence week in a month. Field name: Week.
- `Public Property Reminder() As BoYesNoEnum` [R/W] Specifies whether or not SAP Business One sends a reminder message to the user mailbox ('user' means the current SAP Business One user). Field name: Reminder.
- `Public Property ReminderPeriod() As Double` [R/W] The duration for sending the reminder message. Field name: RemTime.
- `Public Property ReminderType() As BoDurations` [R/W] Specifies the duration type: minutes or hours. Field name: RemType.
- `Public Property RepeatOption() As RepeatOptionEnum` [R/W] For each occurrence, specifies the date on which the recurring activity is to take place. It is only available for Phone Call, Meeting, or Task, when the value of the recurrence pattern is not None. Field name: SubOption.
- `Public Property Room() As String` [R/W] The room in which the activity (Meeting type only) with the business partner takes place. Field name: room. Length: 50 characters.
- `Public Property SalesEmployee() As Long` [R/W] The code of the sales employee who is responsible for the activity. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property SalesOpportunityId() As Long` [R/W] The ID of the sales opportunity. Field name: OprId.
- `Public Property SalesOpportunityLine() As Long` [R/W] The row number of the sales opportunity. Field name: OprLine.
- `Public Property Saturday() As BoYesNoEnum` [R/W] Defines whether the recurring activity occurs on Saturday. Used in a weekly pattern. Field name: Saturday.
- `Public Property SeriesEndDate() As Date` [R/W] The end date of the series for the recurring activity. Field name: SeEndDate.
- `Public Property SeriesStartDate() As Date` [R] The start date of the series for the recurring activity. Field name: SeStartDate.
- `Public Property StartDate() As Date` [R/W] The start date of the activity. Field name: Recontact.
- `Public Property StartTime() As Date` [R/W] The start time (hh:mm) of the activity. Field name: BeginTime.
- `Public Property State() As String` [R/W] The code of the state where the activity (Meeting type only) with the business partner takes place. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST).
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Status() As Long` [R/W] The status of the activity (Task type only) as defined in ActivityStatus object. Field name: status. This is a foreign key to the ActivityStatus object.
- `Public Property Street() As String` [R/W] The street part of the address at which the activity (Meeting type only) with the business partner takes place. Field name: street. Length: 100 characters.
- `Public Property Subject() As Long` [R/W] The subject of the activity. Field name: CntctSbjct.
- `Public Property Sunday() As BoYesNoEnum` [R/W] Defines whether the recurring activity occurs on Sunday. Used in a weekly pattern. Field name: Sunday.
- `Public Property Tentativeflag() As BoYesNoEnum` [R/W] Specifies whether or not the activity is tentative. Field name: tentative.
- `Public Property Thursday() As BoYesNoEnum` [R/W] Defines whether the recurring activity occurs on Thursday. Used in a weekly pattern. Field name: Thursday.
- `Public Property Tuesday() As BoYesNoEnum` [R/W] Defines whether the recurring activity occurs on Tuesday. Used in a weekly pattern. Field name: Tuesday.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property Wednesday() As BoYesNoEnum` [R/W] Defines whether the recurring activity occurs on Wednesday. Used in a weekly pattern. Field name: Wednesday.

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

# ActivityCheckIn (Object)

ActivityCheckIn Class

## Properties (8)
- `Public Property Date() As Date` [R] property Date
- `Public Property HandledBy() As Long` [R] property HandledBy
- `Public Property HandledByEmployee() As Long` [R] property HandledByEmployee
- `Public Property Latitude() As String` [R/W] property Latitude
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property Location() As String` [R/W] property Location
- `Public Property Longitude() As String` [R/W] property Longitude
- `Public Property Time() As Date` [R] property Time

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivityCheckInCollection (Collection)

ActivityCheckInCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ActivityCheckIn` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ActivityCheckIn` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivityInstanceParams (Object)

Holds the key and date of an instance in a recurring activity. This object is used to pass keys to and retrieve keys from ActivitiesService methods. Source table: OCLG.

## Properties (2)
- `Public Property ActivityCode() As Long` [R/W] The key for a specific activity. Field name: ClgCode.
- `Public Property InstanceDate() As Date` [R/W] The date for the instance in the recurring activity. Field name: Recontact.

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

# ActivityInstancesListParams (Object)

You can get the top N activity instances from certain date.

**Remarks:** You can use this object for the To-Do list in SAP Business One mobile solution.

## Properties (2)
- `Public Property InstanceCount() As Long` [R/W] The number of activity instances.
- `Public Property StartDate() As Date` [R/W] The start date for the activity instances.

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

# ActivityInstancesParams (Collection)

A collection of ActivityInstanceParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ActivityInstanceParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ActivityInstanceParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ActivityLocations (Object)

ActivityLocations is a business object that represents activity locations in the Business Partners module. This object enables you to: - Add a location for an activity (for example, meeting room, address name, and so on). - Retrieve an activity location by its key. - Update an activity location. - Save the object in XML format. Source table: OCLO.

**Remarks:** To display the form in the application: - Select Business Partners --> Activities. - In the Location text box of the General tab, select Define New.

## Properties (4)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the key of the activity location. Field name: Code.
  - remarks: SAP Business One assigns a sequential number, starting from 1, for each location that you add.
- `Public Property Name() As String` [R/W] Sets or returns the Sets or returns the location name. Field name: Name. Length: 50 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a new location to the Activity Locations table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Specifies the Activity location Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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

# ActivityMultipleRecipient (Object)

List of the recipients when you select the Multiple Recipients option. Source table: CLG2.

**Remarks:** To display the form in the application: - Select Business Partners --> Activities. - In the Assigned To dropdown list, select the Multiple Recipients option.

## Properties (3)
- `Public Property LineNumber() As Long` [R] Row number of the recipient. Field name: LineNum.
- `Public Property RecipientCode() As String` [R/W] Code of the recipient. Field name: ObjCode. Length: 50 characters.
- `Public Property RecipientType() As ActivityRecipientObjTypeEnum` [R/W] Type of the recipient. Field name: ObjType.

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

# ActivityMultipleRecipientCollection (Collection)

Properties of the recipients when you select the Multiple Recipients option. Source table: CLG2.

**Remarks:** To display the form in the application: - Select Business Partners --> Activities. - In the Assigned To dropdown list, select the Multiple Recipients option.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As ActivityMultipleRecipient` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ActivityMultipleRecipient` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ActivityParams (Object)

Holds the key of an activity. This object is used to pass keys to and retrieve keys from ActivitiesService methods. Source table: OCLG.

## Properties (24)
- `Public Property Activity() As BoActivities` [R] property Activity
- `Public Property ActivityCode() As Long` [R/W] The key for a specific activity. Field name: ClgCode.
- `Public Property CardCode() As String` [R] property CardCode
- `Public Property City() As String` [R] property City
- `Public Property Closed() As BoYesNoEnum` [R] property Closed
- `Public Property Country() As String` [R] property Country
- `Public Property Details() As String` [R] property Details
- `Public Property DocEntry() As String` [R] property DocEntry
- `Public Property DocNum() As String` [R] property DocNum
- `Public Property DocType() As String` [R] property DocType
- `Public Property EndDuedate() As Date` [R] property EndDueDate
- `Public Property EndTime() As Date` [R] property EndTime
- `Public Property HandledBy() As Long` [R] property HandledBy
- `Public Property Inactiveflag() As BoYesNoEnum` [R] property InactiveFlag
- `Public Property Notes() As String` [R] property Notes
- `Public Property Priority() As BoMsgPriorities` [R] property Priority
- `Public Property Room() As String` [R] property Room
- `Public Property SalesOpportunityId() As Long` [R] property SalesOpportunityId
- `Public Property SalesOpportunityLine() As Long` [R] property SalesOpportunityLine
- `Public Property StartDate() As Date` [R] property StartDate
- `Public Property StartTime() As Date` [R] property StartTime
- `Public Property State() As String` [R] property State
- `Public Property Street() As String` [R] property Street
- `Public Property Tentativeflag() As BoYesNoEnum` [R] property TentativeFlag

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

# ActivityRecipient (Object)

ActivityRecipient Class

## Properties (3)
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property RecipientCode() As String` [R/W] property RecipientCode
- `Public Property RecipientType() As RecipientTypeEnum` [R/W] property RecipientType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivityRecipientCollection (Collection)

ActivityRecipientCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As ActivityRecipient` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ActivityRecipient` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivityRecipientList (Object)

ActivityRecipientList Class

## Properties (5)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property ActivityRecipientCollection() As ActivityRecipientCollection` [R] property ActivityRecipientCollection
- `Public Property Code() As Long` [R] property Code
- `Public Property IsMultiple() As BoYesNoEnum` [R] property IsMultiple
- `Public Property Name() As String` [R/W] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivityRecipientListParams (Object)

ActivityRecipientParams Class

## Properties (4)
- `Public Property Active() As BoYesNoEnum` [R] property Active
- `Public Property Code() As Long` [R/W] property Code
- `Public Property IsMultiple() As BoYesNoEnum` [R] property IsMultiple
- `Public Property Name() As String` [R] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivityRecipientListParamsCollection (Collection)

ActivityRecipientParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ActivityRecipientListParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ActivityRecipientListParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivityRecipientListsService (Object)

ActivityRecipientListsService Class

## Methods (8)
- `Public Function Add(ByVal pIActivityRecipientList As ActivityRecipientList) As ActivityRecipientListParams` Add
  - param `pIActivityRecipientList`: 
- `Public Sub Delete(ByVal pIActivityRecipientListParams As ActivityRecipientListParams)` Delete
  - param `pIActivityRecipientListParams`: 
- `Public Function Get(ByVal pIActivityRecipientListParams As ActivityRecipientListParams) As ActivityRecipientList` Get
  - param `pIActivityRecipientListParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ActivityRecipientListsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ActivityRecipientListsServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As ActivityRecipientListParamsCollection` GetList
- `Public Sub Update(ByVal pIActivityRecipientList As ActivityRecipientList)` Update
  - param `pIActivityRecipientList`: 

# ActivityStatus (Object)

ActivityStatus is a business object that enables to define statuses for Task type activities in the Business Partners module. This object enables you to: - Add a status to the statuses list. - Retrieve a status by its key. - Update a status of the statuses list. - Save the object in XML format. Source table: OCLA.

**Remarks:** To display the form in the application: - Select Business Partners --> Activities. - From the Activity box, select Task. - From the Status box in the General tab, select Define New.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property StatusDescription() As String` [R/W] Sets or returns the task status description. Field name: descriptio. Length: 254 characters.
- `Public Property StatusId() As Long` [R] Returns the status ID of the task. Field name: statusID.
- `Public Property StatusName() As String` [R/W] Sets or returns the task status name. Field name: name. Length: 30 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ActivityID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ActivityID`: StatusID.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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

# ActivitySubject (Object)

ActivitySubject Class

## Properties (4)
- `Public Property ActivityType() As Long` [R/W] property ActivityType
- `Public Property Code() As Long` [R] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property IsActive() As BoYesNoEnum` [R/W] property IsActive

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivitySubjectParams (Object)

ActivitySubjectParams Class

## Properties (2)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property Description() As String` [R] property Description

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivitySubjectService (Object)

ActivitySubjectService Class

## Methods (8)
- `Public Function AddActivitySubject(ByVal pIActivitySubject As ActivitySubject) As ActivitySubjectParams` AddActivitySubject
  - param `pIActivitySubject`: 
- `Public Function GetActivitySubject(ByVal pIActivitySubjectParams As ActivitySubjectParams) As ActivitySubject` GetActivitySubject
  - param `pIActivitySubjectParams`: 
- `Public Function GetActivitySubjectList() As ActivitySubjectsParams` GetActivitySubjectList
- `Public Function GetDataInterface(ByVal enumMSDI As ActivitySubjectServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ActivitySubjectServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetListByTypeCode(ByVal pIActivitySubject As ActivitySubject) As ActivitySubjectsParams` GetListByTypeCode
  - param `pIActivitySubject`: 
- `Public Sub UpdateActivitySubject(ByVal pIActivitySubject As ActivitySubject)` UpdateActivitySubject
  - param `pIActivitySubject`: 

# ActivitySubjectsParams (Collection)

ActivitySubjectsParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ActivitySubjectParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ActivitySubjectParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ActivityTypes (Object)

ActivityTypes is a business object that represents activity types in the Business Partners module. This object enables you to: - Add a type for an activity. - Retrieve an activity type by its key. - Update an activity type. - Save the object in XML format. Source table: OCLT.

**Remarks:** To display the form in the application: - Select Business Partners --> Activities. - In the Type text box of the Activity master data, select Define New.

## Properties (5)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the key of the activity type. Field name: Code.
  - remarks: SAP Business One assigns a sequential number, starting from 1, for each type that you add.
- `Public Property Name() As String` [R/W] Sets or returns the activity type. Field name: Name. Length: 20 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a new type to the Activity Types table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Activity type Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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

# AdditionalExpenses (Object)

AdditionalExpenses is a business object that represents the additional expenses defined in the Administration module. These definitions are used by the Marketing Documents and Receipts. This object enables to calculate additional costs connected with a document, such as delivery changes and deposit tax. This object enables you to: - Add an additional expense. - Retrieve an additional expense by its key. - Update an additional expense. - Save the object in XML format. Source table: OEXD.

**Remarks:** To display the form in the application: - Select Administration --> System Initialization --> Document Settings. - In the General tab, select Manage Expenses In Documents. - Click Define Expenses.

## Properties (30)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DistributionMethod() As BoAeDistMthd` [R/W] Sets or returns a valid value of BoAeDistMthd type that specifies the distribution method of the additional expenses. Field name: DistrbMthd
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DrawingMethod() As DrawingMethodEnum` [R/W] The calculation method for freight per row. The calculation method is relevant when you copy rows from a base document to a target document. Field name: BaseMethod
- `Public Property ExpensCode() As Long` [R] Returns the unique ID (primary key) of the additional expense. SAP Business One assigns a sequential number when adding an additional expense. Field name: ExpnsCode
- `Public Property ExpenseAccount() As String` [R/W] Sets or returns the expense account number. You can set only accounts that are defined as Expenses type in Chart of Accounts. Field name: ExpnsAcct Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property ExpenseExemptedAccount() As String` [R/W] Sets or returns the expense exempted account. Field name: ExpnsExAct Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property FixedAmountExpenses() As Double` [R/W] Sets or returns the fixed amount of the expense. Field name: ExpFixSum
- `Public Property FixedAmountRevenues() As Double` [R/W] Sets or returns the fixed revenue amount of the expense. Field name: RevFixSum
- `Public Property FreightOffsetAccount() As String` [R/W] Sets or returns the freight offset account. Field name: ExpOfstAc Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property FreightType() As FreightTypeEnum` [R/W] Indicates the type of freight expense. Field name: ExpnsType
- `Public Property FreightTypeForBollo() As FreightTypeForBolloEnum` [R/W] property FreightTypeForBollo
- `Public Property GrossFreight() As BoYesNoEnum` [R/W] property GrossFreight
- `Public Property Includein1099() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include the expense in the 1099 form. Field name: In1099
- `Public Property InputVATGroup() As String` [R/W] Sets or returns the input VAT group. Field name: VatGroupi Length: 8 characters This is a foreign key to the VatGroups object.
- `Public Property LastPurchasePrice() As BoYesNoEnum` [R/W] Indicates whether to update the last purchase price list after adding an A/P invoice that includes a freight amount per row. Field name: LstPchPrce
- `Public Property Name() As String` [R/W] Sets or returns the expense name. Field name: ExpnsName Length: 20 characters
- `Public Property OutputVATGroup() As String` [R/W] Sets or returns the output VAT group. Field name: VatGroupo Length: 8 characters This is a foreign key to the VatGroups object.
- `Public Property Project() As String` [R/W] The project that relates to the freight. Field: Project. Length: 20 characters.
- `Public Property RevenuesAccount() As String` [R/W] Sets or returns the revenues account. You can set only accounts that are defined as Revenues type in Chart of Accounts. Field name: RevAcct Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property RevenuesExemptedAccount() As String` [R/W] Sets or returns the revenues exempted account. Field name: RevExmAcct Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property SACCode() As String` [R/W] property SACCode
- `Public Property Stock() As BoYesNoEnum` [R/W] Indicates whether to add the freight amount, either in the row level or the total level, to the item's cost when working with perpetual inventory. Field name: Stock
- `Public Property TaxLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the additional expense is VAT liable. Field name: TaxLiable
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WTLiable() As String` [R] Returns the whether or not the additional expense is subject to withholding tax. Field name: TaxLiable Length: 1 character

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ExpnsCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ExpnsCode`: Specifies the code of the additional expense.
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

# AddressExtension (Object)

The Bill To and Ship To address for a marketing document. Source table: INV12

**Example:**
- C# example (from SAP's help):
  ```csharp
  // Get Invoice document
  m_Doc = (SAPbobsCOM.Documents)m_Company.GetBusinessObject(BoObjectTypes.oInvoices);
  m_Doc.GetByKey(4);

  // Get the address sub object from the document object
  m_AddrExtension = (AddressExtension)m_Doc.AddressExtension;

  // Set bill to address properties
  m_AddrExtension.BillToBlock = "BillToBlockU";
  m_AddrExtension.BillToBuilding = "BillToBuildingU";
  m_AddrExtension.BillToCity = "BillToCityU";
  m_AddrExtension.BillToCountry = "BCU";
  m_AddrExtension.BillToCounty = "BUt";
  m_AddrExtension.BillToState = "BSU";
  m_AddrExtension.BillToStreet = "BillToStreetU";
  m_AddrExtension.BillToStreetNo = "BillToStreetNoU";
  m_AddrExtension.BillToZipCode = "BillToZipCodeU";
  m_AddrExtension.BillToAddressType = "BillToAddressTypeU";

  // Set ship to address properties
  m_AddrExtension.ShipToBlock = "ShipToBlockU";
  m_AddrExtension.ShipToBuilding = "ShipToBuildingU";
  m_AddrExtension.ShipToCity = "ShipToCityU";
  m_AddrExtension.ShipToCountry = "SCU";
  m_AddrExtension.ShipToCounty = "SUt";
  m_AddrExtension.ShipToState = "SUt";
  m_AddrExtension.ShipToStreet = "ShipToStreetU";
  m_AddrExtension.ShipToStreetNo = "ShipToStreetNoU";
  m_AddrExtension.ShipToZipCode = "ShipToZipCodeU";

  // Update the document
  m_Doc.Update();
  ```

## Properties (60)
- `Public Property BillToAddress2() As String` [R/W] property BillToAddress2
- `Public Property BillToAddress3() As String` [R/W] property BillToAddress3
- `Public Property BillToAddressType() As String` [R/W] The address type for the Bill To address. For Brazil only. Field name: AddrTypeB
- `Public Property BillToBlock() As String` [R/W] The block of the Bill To address. Field name: BlockB
- `Public Property BillToBuilding() As String` [R/W] The building of the Bill To address. Field name: BuildingB
- `Public Property BillToCity() As String` [R/W] The city of the Bill To address. Field name: CityB
- `Public Property BillToCountry() As String` [R/W] The country of the Bill To address. Field name: CountryB
  - remarks: Enter the 2- or 3-character country code; a list is available in the Code field of the OCRY table.
- `Public Property BillToCounty() As String` [R/W] The county of the Bill To address. Field name: CountyB
- `Public Property BillToGlobalLocationNumber() As String` [R/W] property BillToGlobalLocationNumber
- `Public Property BillToState() As String` [R/W] The state of the Bill To address. Field name: StateB
- `Public Property BillToStreet() As String` [R/W] The street of the Bill To address. Field name: StreetB
- `Public Property BillToStreetNo() As String` [R/W] The street number of the Bill To address. Field name: StreetNoB
- `Public Property BillToZipCode() As String` [R/W] The zip code of the Bill To address. Field name: ZipCodeB
- `Public Property DeliveryPlaceBlock() As String` [R/W] Delivery Place Block. Field name: BlckDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceBP() As String` [R/W] Delivery Place BP. Field name: BPDelivryP. Length: 15 characters.
- `Public Property DeliveryPlaceBuilding() As String` [R/W] Delivery Place Building. Field name: BldDlvryP. Length: 16 characters.
- `Public Property DeliveryPlaceCity() As String` [R/W] Delivery Place City. Field name: CityDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceCNPJ() As String` [R/W] Delivery Place CNPJ. Field name: CNPJDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceCountry() As String` [R/W] Delivery Place Country. Field name: CtryDlvryP. Length: 3 characters.
- `Public Property DeliveryPlaceCounty() As String` [R/W] Delivery Place County. Field name: CntyDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceCPF() As String` [R/W] Delivery Place CPF. Field name: CPFDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceDepartureDate() As String` [R/W] Delivery Place Departure Date. Field name: DpDtDlvryP. Length: 8 characters.
- `Public Property DeliveryPlaceEMail() As String` [R/W] Delivery Place E-Mail. Field name: MailDlvryP. Length: 100 characters.
- `Public Property DeliveryPlacePhone() As String` [R/W] Delivery Place Phone. Field name: FoneDlvryP. Length: 50 characters.
- `Public Property DeliveryPlaceState() As String` [R/W] Delivery Place State. Field name: StatDlvryP. Length: 3 characters.
- `Public Property DeliveryPlaceStreet() As String` [R/W] Delivery Place Street. Field name: StrtDlvryP. Length: 100 characters.
- `Public Property DeliveryPlaceStreetNo() As String` [R/W] Delivery Place Street Number. Field name: StrNoDlvrP. Length: 100 characters.
- `Public Property DeliveryPlaceZip() As String` [R/W] Delivery Place Zip Code. Field name: ZipDlvryP. Length: 20 characters.
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property GoodsIssuePlaceBlock() As String` [R/W] Goods Issue Place Block. Field name: BlockGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceBP() As String` [R/W] Goods Issue Place BP. Field name: BPGdsIssP. Length: 15 characters.
- `Public Property GoodsIssuePlaceBuilding() As String` [R/W] Goods Issue Place Building. Field name: BldngGIP. Length: 16 characters.
- `Public Property GoodsIssuePlaceCity() As String` [R/W] Goods Issue Place City. Field name: CityGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceCNPJ() As String` [R/W] Goods Issue Place CNPJ. Field name: CNPJGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceCountry() As String` [R/W] Goods Issue Place Country. Field name: CountryGIP. Length: 3 characters.
- `Public Property GoodsIssuePlaceCounty() As String` [R/W] Goods Issue Place County. Field name: CountyGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceCPF() As String` [R/W] Goods Issue Place CPF. Field name: CPFGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceDepartureDate() As String` [R/W] Goods Issue Place Departure Date. Field name: DptDateGIP. Length: 8 characters.
- `Public Property GoodsIssuePlaceEMail() As String` [R/W] Goods Issue Place E-Mail. Field name: EMailGIP. Length: 100 characters.
- `Public Property GoodsIssuePlacePhone() As String` [R/W] Goods Issue Place Telephone. Field name: PhoneGIP. Length: 50 characters.
- `Public Property GoodsIssuePlaceState() As String` [R/W] Goods Issue Place State. Field name: StateGIP. Length: 3 characters.
- `Public Property GoodsIssuePlaceStreet() As String` [R/W] Goods Issue Place Street. Field name: StreetGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceStreetNo() As String` [R/W] Goods Issue Place Street Number. Field name: StrtNoGIP. Length: 100 characters.
- `Public Property GoodsIssuePlaceZip() As String` [R/W] Goods Issue Place Zip Code. Field name: ZipGIP. Length: 20 characters.
- `Public Property PlaceOfSupply() As String` [R/W] property PlaceOfSupply
- `Public Property PurchasePlaceOfSupply() As String` [R/W] property PurchasePlaceOfSupply
- `Public Property ShipToAddress2() As String` [R/W] property ShipToAddress2
- `Public Property ShipToAddress3() As String` [R/W] property ShipToAddress3
- `Public Property ShipToAddressType() As String` [R/W] The address type for the Ship To address. For Brazil only. Field name: AddrTypeS
- `Public Property ShipToBlock() As String` [R/W] The block of the Ship To address. Field name: BlockS
- `Public Property ShipToBuilding() As String` [R/W] The building of the Ship To address. Field name: BuildingS
- `Public Property ShipToCity() As String` [R/W] The city of the Ship To address. Field name: CityS
- `Public Property ShipToCountry() As String` [R/W] The country of the Ship To address. Field name: CountryS
  - remarks: Enter the 2- or 3-character country code; a list is available in the Code field of the OCRY table.
- `Public Property ShipToCounty() As String` [R/W] The county of the Ship To address. Field name: CountyS
- `Public Property ShipToGlobalLocationNumber() As String` [R/W] property ShipToGlobalLocationNumber
- `Public Property ShipToState() As String` [R/W] The state of the Ship To address. Field name: StateS
- `Public Property ShipToStreet() As String` [R/W] The street of the Ship To address. Field name: StreetS
- `Public Property ShipToStreetNo() As String` [R/W] The street number of the Ship To address. Field name: StreetNoS
- `Public Property ShipToZipCode() As String` [R/W] The zip code of the Ship To address. Field name: ZipCodeS
- `Public Property UserFields() As UserFields` [R] property UserFields

# AddressFormat (Object)

The address formats for business partners. Source table: OADF.

## Properties (3)
- `Public Property Code() As Long` [R] The code for the address format. Field name: Code.
- `Public Property Format() As String` [R/W] The address format. Field name: Format. Length: 100 characters.
- `Public Property Name() As String` [R/W] The name for the address format. Field name: Name. Length: 50 characters.

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

# AddressFormatParams (Object)

Holds the key of an address format. This object is used to pass keys to and retrieve keys from AddressService methods.

## Properties (2)
- `Public Property Code() As Long` [R/W] The code for the address format. Field name: Code.
- `Public Property Name() As String` [R] The name for the address format. Field name: Name. Length: 50 characters.

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

# AddressFormatParamsCollection (Collection)

A collection of AddressFormatParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AddressFormatParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AddressFormatParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AddressParams (Object)

Holds the key of an address. This object is used to pass keys to and retrieve keys from AddressService methods. Source table: SCL7.

## Properties (14)
- `Public Property Address2() As String` [R/W] The Address Name 2. Field name: Address2S. Length: 50 characters.
- `Public Property Address3() As String` [R/W] The Address Name 3. Field name: Address3S. Length: 50 characters.
- `Public Property AddressType() As String` [R/W] The address type. Field name: AddrTypeS. Length: 100 characters.
- `Public Property Block() As String` [R/W] The block. Field name: BlockS. Length: 100 characters.
- `Public Property Building() As String` [R/W] The building/floor/room. Field name: BuildingS.
- `Public Property City() As String` [R/W] The city. Field name: CityS. Length: 100 characters.
- `Public Property Country() As String` [R/W] The country. Field name: CountryS. Length: 3 characters.
- `Public Property County() As String` [R/W] The county. Field name: CountyS. Length: 100 characters.
- `Public Property GlobalLocationNumber() As String` [R/W] The global location number. Field name: GlbLocNumS. Length: 50 characters.
- `Public Property State() As String` [R/W] The state. Field name: StateS. Length: 3 characters.
- `Public Property Street() As String` [R/W] The street. Field name: StreetS. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] The street number. Field name: StreetNoS. Length: 100 characters.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property ZipCode() As String` [R/W] The zip code. Field name: ZipCodeS. Length: 20 characters.

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

# AddressReturnParams (Object)

Holds the key of a full address. This object is used to pass keys to and retrieve keys from AddressService methods.

## Properties (1)
- `Public Property FullAddress() As String` [R] Retrieves the full address for a business partner.

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

# AddressService (Object)

The AddressService service enables you to retrieve Address Format and full address. Source table: OADF.

**Remarks:** From the SAP Business One Main Menu, choose Administration → Setup → Business Partners → Address Formats, create a new Address Formats.

**Example:**
- C# example (from SAP's help):
  ```csharp
              oCompany.StartTransaction();
              CompanyService cs = oCompany.GetCompanyService();

              SAPbobsCOM.AddressService addrService = (SAPbobsCOM.AddressService)cs.GetBusinessService(SAPbobsCOM.ServiceTypes.AddressService);
              SAPbobsCOM.AddressParams addrParam = (SAPbobsCOM.AddressParams)addrService.GetDataInterface(AddressServiceDataInterfaces.asAddressParams);
              SAPbobsCOM.AddressReturnParams addrRetParam = (SAPbobsCOM.AddressReturnParams)addrService.GetDataInterface(AddressServiceDataInterfaces.asAddressReturnParams);
              SAPbobsCOM.AddressFormatParams addrFormatParam = (SAPbobsCOM.AddressFormatParams)addrService.GetDataInterface(AddressServiceDataInterfaces.asAddressFormatParams);

              //GetAddressFormat
              addrFormatParam.Code = 16;
              SAPbobsCOM.AddressFormat addrFormat = addrService.GetAddressFormat(addrFormatParam);
              MessageBox.Show(addrFormat.Format);
              if (!string.IsNullOrEmpty(addrFormat.Format))
              {
                  MessageBox.Show("created!");
                  oCompany.EndTransaction(SAPbobsCOM.BoWfTransOpt.wf_Commit);
              }

              //GetFullAddress
              addrParam.Country = "CN";
              addrParam.City = "Shanghai";
              addrParam.Street = "Chenhui";
              addrParam.Block = "1001";

              addrRetParam = addrService.GetFullAddress(addrParam);

              MessageBox.Show(addrRetParam.FullAddress);
              if (!string.IsNullOrEmpty(addrRetParam.FullAddress))
              {
                  MessageBox.Show("created!");
                  oCompany.EndTransaction(SAPbobsCOM.BoWfTransOpt.wf_Commit);
              }
  ```

## Methods (5)
- `Public Function GetAddressFormat(ByVal pIAddressFormatParams As AddressFormatParams) As AddressFormat` Retrieves an address format. The address format is specified by its key, which is contained in the AddressFormatParams object passed to the method.
  - param `pIAddressFormatParams`: The key of the address format to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As AddressServiceDataInterfaces) As Object` AddressService data interfaces. Creates an empty data structure for use with the GeneralService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AddressServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetFullAddress(ByVal pIAddressParams As AddressParams) As AddressReturnParams` Retrieves a full address. The full address is specified by its key, which is contained in the AddressReturnParams object passed to the method.
  - param `pIAddressParams`: The key of the full address to retrieve.
