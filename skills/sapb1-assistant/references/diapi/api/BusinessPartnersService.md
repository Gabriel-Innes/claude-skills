<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BusinessPartnersService (Object)

The BusinessPartnersService enables to transfer credit or debit amounts from a specified opening balance account to one or more business partner accounts. This service creates a journal entry line. Mandatory properties: OpenBalanceAccount (OpenningBalanceAccount object) and Code (BPCode object). This object enables user to open Balanced Account. Source table: OCRD.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: Select Business Partners.

## Methods (4)
- `Public Sub CreateOpenBalance(ByVal pIOpenningBalanceAccount As OpenningBalanceAccount, ByVal pBPCodes As BPCodes)` Transfers credit or debit amounts from a specified opening balance account to one or more business partner accounts.
  - param `pIOpenningBalanceAccount`: Specifies the opening balance account.
  - param `pBPCodes`: Bpcodes is a collection of BPCode, a data structure related to the BusinessPartnersService.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oBusinessPartnersService As SAPbobsCOM.BusinessPartnersService

    Dim oOpenningBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oBpAccounts As SAPbobsCOM.BPCodes

    Dim oBpAccountFirst As SAPbobsCOM.BPCode

    Dim oBpAccountSecond As SAPbobsCOM.BPCode

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oBusinessPartnersService = oCmpSrv.GetBusinessService(ServiceTypes.BusinessPartnersService)

    'get Accounts Service Data Interface

    oOpenningBalanceAccount = oBusinessPartnersService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account code (account name = Common Stock (HO, USA, GA )) 'for the opening balance account

    oOpenningBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'set the details

    oOpenningBalanceAccount.Details = "Bp Accounts Opening Balance"

    'set the date

    oOpenningBalanceAccount.Date = Date.Today

    'get ref to Bp accounts

    oBpAccounts = oBusinessPartnersService.GetDataInterface(BusinessPartnersServiceDataInterfaces.bpsdiBPCodes)

    'add accounts that will be in credit or in debit

    'add first account

    oBpAccountFirst = oBpAccounts.Add

    'set the account code

    oBpAccountFirst.Code = "HU1006"

    'set credit amount

    oBpAccountFirst.Credit = 300

    'add second account

    oBpAccountSecond = oBpAccounts.Add

    'set the account code

    oBpAccountSecond.Code = "HU1007"

    'set credit amount

    oBpAccountSecond.Credit = 300

    'create the balance for the first and second accounts from the Opening Balance Account

    oBusinessPartnersService.CreateOpenBalance(oOpenningBalanceAccount,oBpAccounts)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As BusinessPartnersServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BusinessPartnersServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - example note: How to get an Openning Balance Account from an XML file
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oOpenBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oOpenBalanceAccountXmlFile As SAPbobsCOM.OpenningBalanceAccount

    Dim oBpAccounts As SAPbobsCOM.BPCodes

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oBusinessPartnersService = oCmpSrv.GetBusinessService(ServiceTypes.BusinessPartnersService)

    'get Accounts Service Data Interface

    oOpenBalanceAccount = oBusinessPartnersService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account code (account name = Common Stock (HO, USA, GA )) 'for the opening balance account

    oOpenBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'save data to xml file

    oOpenBalanceAccount.ToXMLFile("c:\OpenningBalanceAccount.xml")

    'create OpenBalanceAccount from xml file

    oOpenBalanceAccountXmlFile = oBusinessPartnersService.GetDataInterfaceFromXMLFile("c:\OpenningBalanceAccount.xml")
    ```
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
  - param `bstrXMLString`: XML string. Specifies an XML string.
  - example note: Shows how to get an Openning Balance Account from an XML string.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oOpenBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oOpenBalanceAccountXmlStr As SAPbobsCOM.OpenningBalanceAccount

    Dim sOpenBalanceAccountXmlStr As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oBusinessPartnersService = oCmpSrv.GetBusinessService(ServiceTypes.BusinessPartnersService)

    'get Accounts Service Data Interface

    oOpenBalanceAccount = oBusinessPartnersService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account code (account name = Common Stock (HO, USA, GA )) 'for the opening balance account

    oOpenBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'save data to xml string

    sOpenBalanceAccountXmlStr = oOpenBalanceAccount.ToXMLString

    'create OpenBalanceAccount from xml string

    oOpenBalanceAccountXmlStr = oBusinessPartnersService.GetDataInterfaceFromXMLString(sOpenBalanceAccountXmlStr)
    ```
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
