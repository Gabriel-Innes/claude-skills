<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
  - enum: `../enums/AccountCategoryServiceDataInterfaces.md`
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
