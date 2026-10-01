<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BankStatementsService (Object)

This service manages bank statements drafts that can be posted in SAP Business One. The service lets you add, update, delete, get, and get list of bank statements. Source tables: OBNH, OBNK, BNK1.

**Remarks:** Country-specific: Austria, Belgium, Czech Republic, Germany, Denmark, Finland, France, Netherlands, Norway, and Sweden. In new 2006 A installations, the BankStatements service is activated by default. When upgrading to 2006 A, the service is disabled. To activate it: in Administration > System Initialization > Company Details, choose the Basic Initialization tab and select Install Bank Statement Process. You will not be able to use thise service if it is not activated. When the BankStatement service is activated, you can use both this service and the BankPages object (without account that are in the accounts list of House Bank).

## Methods (8)
- `Public Function AddBankStatement(ByVal pIBankStatement As BankStatement) As BankStatementParams` Adds a bank statement row.
  - param `pIBankStatement`: Specifies the properties of the bank statement you want to add.
  - remarks: The bank statement is added as a draft document.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Sub AddBankStatement()

            Dim oBnkStSrv As SAPbobsCOM.BankStatementsService

            Dim oCmpSrv As SAPbobsCOM.CompanyService

            Dim oBankStatement As SAPbobsCOM.BankStatement

            Dim oBnkStRow As SAPbobsCOM.BankStatementRow

            Dim MultiPayment As SAPbobsCOM.MultiplePayment

            oCmpSrv = oCompany.GetCompanyService ' Assume oCompany is the DI company Object

            'Get Bank Statement Service

            oBnkStSrv = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.BankStatementsService)

            oBankStatement = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatement)

            oBankStatement.BankAccountKey = 1

            'Add Row to Bank Statement

            oBnkStRow = oBankStatement.BankStatementRows.Add()

            oBnkStRow.ExternalCode = "E1"

            'Add Payment to Bank Statement row

            MultiPayment = oBnkStRow.MultiplePayments.Add()

            MultiPayment.AmountFC = 20

            MultiPayment.IsDebit = SAPbobsCOM.BoYesNoEnum.tYES

            'Add Bank Statement

            oBnkStSrv.AddBankStatement(oBankStatement)

    End Sub
    ```
- `Public Sub DeleteBankStatement(ByVal pIBankStatementParams As BankStatementParams)` Deletes the specified bank statement row.
  - param `pIBankStatementParams`: Specifies the number of the statement you want to delet.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub DeleteBankStatement()

            Dim oBnkStSrv As SAPbobsCOM.BankStatementsService

            Dim oCmpSrv As SAPbobsCOM.CompanyService

            Dim oBankStmParm As SAPbobsCOM.BankStatementParams

            oCmpSrv = oCompany.GetCompanyService ' Assume oCompany is the DI company Object

            'Get Bank Statement Service

            oBnkStSrv = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.BankStatementsService)

            oBankStmParm = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatementParams)

            oBankStmParm.InternalNumber = 2

            'Delete Bank Statement

            oBnkStSrv.DeleteBankStatement(oBankStmParm)

    End Sub
    ```
- `Public Function GetBankStatement(ByVal pIBankStatementParams As BankStatementParams) As BankStatement` Returns an instance of BankStatement object according to the specified number.
  - param `pIBankStatementParams`: Specifies the number of the statement you want to get.
- `Public Function GetBankStatementList(ByVal pIBankStatementsFilter As BankStatementsFilter) As BankStatementsParams` Returns a collection of bank statement rows by a specified filter. The filter is defined in BankStatementsFilter object.
  - param `pIBankStatementsFilter`: Specifies a filter to the bank statements you want to get.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub GetBankStatementList()

            Dim oBnkStSrv As SAPbobsCOM.BankStatementsService

            Dim oCmpSrv As SAPbobsCOM.CompanyService

            Dim Filter As SAPbobsCOM.IBankStatementsFilter

            Dim Params As SAPbobsCOM.IBankStatementsParams

            oCmpSrv = oCompany.GetCompanyService ' Assume oCompany is the DI company Object

            'Get Bank Statement Service

            oBnkStSrv = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.BankStatementsService)

            'Set Bank Statement Filter

            Filter = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatementsFilter)

            Filter.Bank = "10000000"

            Filter.Account = "111"

            Filter.Country = "DE"

            Params = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatementsParams)

            'Get Bank Statement List

            Params = oBnkStSrv.GetBankStatementList(Filter)

    End Sub
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As BankStatementsServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BankStatementsServiceDataInterfaces.md`
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
- `Public Sub UpdateBankStatement(ByVal pIBankStatement As BankStatement)` Updates an existing bank statement.
  - param `pIBankStatement`: Specifies the properties you want to update.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Sub UpdateBankStatement()

          Dim oBnkStSrv As SAPbobsCOM.BankStatementsService

          Dim oCmpSrv As SAPbobsCOM.CompanyService

          Dim oBankStatement As SAPbobsCOM.IBankStatement

          Dim oBankStmParm As SAPbobsCOM.BankStatementParams

          oCmpSrv = oCompany.GetCompanyService ' Assume oCompany is the DI company Object

          'Get Bank Statement Service

          oBnkStSrv = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.BankStatementsService)

          oBankStmParm = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatementParams)

          oBankStmParm.InternalNumber = 1

          'Get Bank Statement

          oBankStatement = oBnkStSrv.GetBankStatement(oBankStmParm)

          'Change the Bank Statement Currency to USD

          oBankStatement.Currency = "USD"

          'Update Bank Statement

          oBnkStSrv.UpdateBankStatement(oBankStatement)

    End Sub
    ```
