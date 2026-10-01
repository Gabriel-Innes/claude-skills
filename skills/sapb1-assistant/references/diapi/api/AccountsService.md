<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
  - enum: `../enums/AccountsServiceDataInterfaces.md`
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
