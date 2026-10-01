<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Company (Object)

Company is the primary DI API object that represents a single SAP Business One company database. This object enables you to connect to the company database and to create business objects to use with the company database.

**Remarks:** The Company object is the only object of the DI API that you can create directly (for example, with New in Visual Basic). You can then use the Company object to create all other DI API objects. To enable your add-on to support the side-by-side model, see Versions Compatibility.

## Properties (28)
- `Public Property AddonIdentifier() As String` [R/W] Sets or returns a string identifier that your add-on must use to connect to SAP Business One database.
  - remarks: You can generate the string identifier through SAP Business One application only (Administration > License > Add-on Identifier Generator).
- `Public Property Application(ByVal RHS As Object) As Object` [W] To connect with SAP Business One, you can set this property to a SAPbouiCOM.Application object, and then call the Connect method without specifying any other connection properties -- the properties are taken from the UI API Application object.
  - remarks: Creating a connection with this property is only relevant when an instance of the SAP Business One application on the same machine is open and connected to a company.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Private WithEvents SBO_Application As SAPbouiCOM.Application

    Dim oSboGuiApi As SAPbouiCOM.SboGuiApi

    Dim sConnectionString As String

    Dim oApplication As SAPbouiCOM.Application

    Dim oCompany As SAPbobsCOM.Company

    Dim nResult As Long

    oSboGuiApi = New SAPbouiCOM.SboGuiApi

    ' The connection string is passed to the add-on as a command line argument

    sConnectionString = Environment.GetCommandLineArgs.GetValue(1)

    ' Set an add-on identifier (this identifier is for development license)

    oSboGuiApi.AddonIdentifier = "4CC5B8A4E0213A68489E38CB4052855EE8678CD237F64D1C11C22707A54DBD2D5D5F6E4050A09B9F9FB80FAC44F6"

    ' Connect to a running SBO Application

    oSboGuiApi.Connect(sConnectionString)

    ' Get an initialized application object

    oApplication = oSboGuiApi.GetApplication()

    oCompany = New SAPbobsCOM.Company

    ' Set UI Application object to Company object

    oCompany.Application = oApplication

    ' Connect to current B1 company

    nResult = oCompany.Connect
    ```
- `Public Property AttachMentPath() As String` [R] Returns the path to all the company's saved mail attachments and all contact related files.
  - remarks: Specify the directory of the attachments such as, customer web pages.
- `Public Property BitMapPath() As String` [R] Returns the path to all the picture files of the company, which are related to the Picture property of Items object, Picture property of BusinessPartners object, and documents.
- `Public Property CompanyDB() As String` [R/W] Sets or returns the name of the company SQL database .
  - remarks: Use this property to specify the database name to which you want to connect. You must set this property before you use the Connect method to establish a connection to the database. This database must be a SAP Business One database that is compatible with the SAP Business One server database (SBO-Common).
- `Public Property CompanyName() As String` [R] Returns the company name as defined in the database.
  - remarks: After establishing a connection, this property contains the company name that is specified in the database.
- `Public Property Connected() As Boolean` [R] Returns a Boolean value that specifies whether or not the Company object is connected to the database.
  - remarks: You can use this property to check if the operation of the Connect or Disconnect methods was successful.
- `Public Property DbPassword() As String` [R/W] Sets or returns the password for establishing a connection to the database server. The field is not mandatory, as the database credentials are stored in the System Landscape Directory (SLD) server and you can use these values instead.
  - remarks: When you retrieve the value of the DbPassword field, ****** is returned. If you set a value to the DbUserName field, then that value is returned when you get a value from this field. If you connected without providing a database user name (relying on the credentials stored in the license server), then an empty string is returned.
- `Public Property DbServerType() As BoDataServerTypes` [R/W] The database type.
- `Public Property DbUserName() As String` [R/W] Sets or returns the user name for establishing a connection to the database server. The field is not mandatory, as the database credentials are stored in the System Landscape Directory (SLD) server and you can use these values instead.
  - remarks: If you set a value to the DbUserName field, then that value is returned when you get a value from this field. If you connected without providing a database user name (relying on the credentials stored in the license server), then an empty string is returned.
- `Public Property DTCTransactionObject() As Unknown` [R/W] This interface supports Distributed Transactions for MS-SQL database that are controlled by MS-DTC engine (Microsoft Distributed Transaction Coordinator). DTC is a system service that coordinates transactions so that work can be committed as an atomic transaction even if it spans multiple resource managers on multiple computers, regardless of failures. This interface is applicable for the following environment: - MS-SQL database server - C/C++ interface - ODBC connection type - DI API only (and not by DI Server)
  - remarks: Usage - Create a distributed transaction object externally to the application using the DTC interface. GetDTCInterface (&g_pTransactionDispenser); g_pTransactionDispenser-> BeginTransaction(NULL, ISOLATIONLEVEL_ISOLATED, ISOFLAG_RETAIN_DONTCARE, NULL, (::ITransaction**)&g_pTransaction); - The DI COM module receives a handle to a live transaction that is created by the MS-DTC. ICompanyPtr pCmp; pCmp->put_DTCTransactionObject (g_pTransaction); - The DI performs a validation of the transaction object by verifying its Isolation Level. After the validation succeeds, the DB module is notified that the current transaction is an outside object and managed externally. - The transaction process is performed as usual, and the change in the flow is transparent to the user. During a DTC Transaction, do not call StartTransaction() and EndTransaction(), otherwise the system returns an error. - To end the DTC transaction, assign a NULL value to the DTC Transaction handle: pCmp->put_DTCTransactionObject (NULL); - To get the current DTC handle that is set in SAP Business One, call: IUnknown* ptr = NULL; HRESULT hr = pCmp ->get_DTCTransactionObject(&ptr); - To check whether a DTC Transaction is set, call: bool isDTCSet; pCmp->IsDTCTransactionObjectSet(&isDTCSet); Notes - In case an operation fails during a DTC transaction, SAP Business One performs a rollback, which forces other systems under the same distributed transaction to rollback. - The DTC transaction scope (the Begin/End user transaction equivalent) is determined by the calls to put_DTCTransactionObject (). As long as there is a transaction object set, every operation is performed under this transaction context. It is the Client's responsibility to make sure a valid DTC transaction is assigned, and to assign NULL value when the DTC transaction ends. - StartTransaction() and EndTransaction() must not be called during a DTC Transaction. - put_DTCTransactionObject () must not be called during a live user transaction.
- `Public Property ExcelDocsPath() As String` [R] Returns the path to the Microsoft Excel documents exported from the SAP Business One application.
- `Public Property InTransaction() As Boolean` [R] Returns a Boolean value that specifies whether or not the transaction is active.
  - remarks: In case the add-on is not connected to the database, SAP Business One returns exception Not Connected (exception number: -106).
- `Public Property language() As BoSuppLangs` [R/W] Sets or returns the resource language of the object.
  - remarks: If you do not specify a language, the system automatically selects the first language that it finds. If the language you specified is not supported by SAP Business One, the Connect method will fail when trying to establish connection with the SAP Business One server.
- `Public Property LicenseServer() As String` [R/W] Deprecated in DI API 9.2 PL05. Please use SLDServer instead. The DI API will continue to support this property for backward compatibility. The license server name and port for connecting to the company database. The value is in the format myServer:30000. If no value is given, the default license server and port are used. If a server is given but no port is given, 30000 is used for the port.
  - remarks: Previously, the default license for all clients was stored in the SLIC table of the SBO-COMMON database. From release 8.8, the default license file is stored in the b1-local-machine.xml file, which is located by default in c:\Program Files\SAP\SAP Business One DI API\Conf.
- `Public Property MinimalSupportedVersion() As Long` [R] Returns the minimal version of the Company database that the Add-on supports.
  - remarks: For example, an Add-on that its minimal supported version is 6.5 can connect only to a Company database of version 6.5 and up.
- `Public Property Password() As String` [R/W] Sets or returns the SAP Business One password issued to the user.
  - remarks: The password corresponds to the user name the in SAP Business One application.
- `Public Property SecurityCode() As String` [R/W] property SecurityCode
- `Public Property Server() As String` [R/W] Sets or returns the SQL server to which the object connects.
  - remarks: Before establishing a connection with the database, you must specify the SQL server that you want to use. This server must be installed with the SBO-Common database.
- `Public Property SLDServer() As String` [R/W] Set the System Landscape Directory (SLD) server address to connect to the company database and to retrieve the real license address from the SLD server.
  - remarks: As of SAP Business One 9.2 PL05, License Servere will register its URL into the SLD Server.
- `Public Property UserName() As String` [R/W] Sets or returns the user ID, which is used for log on to the SAP Business One application.
  - remarks: This is the user name used for log on to the system (not the user name to access the database server). The UserName property must correspond to the Password property. In the SAP Business One application, a user is specific to the server (Server) and company database (CompanyDB).
- `Public Property UserSignature() As Long` [R] Returns the identification key of the active user who operates the system.
- `Public Property UserTables() As UserTables` [R] Returns the UserTables object, which is the interface to the tables defined by the user. This object allows you to access to the user tables as if they were regular business objects.
- `Public Property UseTrusted() As Boolean` [R/W] Sets or returns a Boolean value that specifies whether the Company object uses NT authentication, or the internal SQL Server user ObsCommon, to establish a connection with the SQL Server.
  - remarks: Set this property to FALSE to log on using ObsCommon. Set this property to TRUE to log on using the current NT user.
- `Public Property Version() As Long` [R] Returns the version of the Company database.
  - remarks: The version of the Company database always equals to the versions of the OBServer.dll and SBOcommon database. The version is stored in the CINF table of the Company database and also in the SINF table of the SBO Common database. The OBServer.dll can be found in the user temporary folder after connecting to the company database. To view its version, open the file properties dialog box and click the Version tab. See also Versions Compatibility.
- `Public Property WordDocsPath() As String` [R] Returns the path to the Microsoft Word documents exported from the SAP Business One application. This directory also contains Microsoft Word templates, which are used for exporting data to Word documents.
- `Public Property XMLAsString() As Boolean` [R/W] Sets or returns a Boolean value that determines whether the XML data will be saved as a file or transferred as a string.
  - remarks: The default value is False - XML as files. This setting is compatible with older versions of the DI API.
- `Public Property XmlExportType() As BoXmlExportTypes` [R/W] Sets or returns a valid value of BoXmlExportTypes that specifies the types for exporting data from the database to XML format.
  - remarks: The default setting is xet_AllNodes (0). This setting supports older DI API versions but cannot be read using the ReadXml method. To use ReadXML method later, set the XmlExportType to xet_ExportImportMode (3).

## Methods (28)
- `Public Function AuthenticateUser(ByVal bstrUserName As String, ByVal bstrPassword As String) As AuthenticateUserResultsEnum` Checks whether a pair of username and password exist and match in the current SAP Business One company . Note: this method is for superuser only.
  - param `bstrUserName`: The username to be tested.
  - param `bstrPassword`: The password to be tested.
- `Public Function ChangePassword(ByVal NewPassword As String) As Long` Changes the password of the actual user connected to SAP Business One. The system verifies whether the new password complies to the company password policy and if not, the system returns an error.
  - param `NewPassword`: Specifies the new password.
- `Public Function Connect() As Long` Connects to the SAP Business One company database.
  - returns: 0 if the method succeeds; otherwise, an error code. You can retrieve the last error code and its description with the method GetLastError.
  - remarks: Before calling this method, set proper values to the following properties: Server, CompanyDB, UserName Password, DbUserName, DbPassword, UseTrusted, and AddonIdentifier. From version 8.8, you can connect without supplying database credentials. The new security mechanism stores the database credentials in the System Landscape Directory (SLD) server. Related Tasks - To retrieve a list of company databases for a specific server, use the GetCompanyList method. - To check if the connection to the database is successful, use the Connected property.
- `Public Sub Disconnect()` Disconnects an active connection with the company database.
  - remarks: Use this method to disconnect the channel between the database and the client. Before disconnecting from the company database, you can use the Connected property to check whether or not the connection is active.
- `Public Sub EndTransaction(ByVal endType As BoWfTransOpt)` Ends a global transaction that started with the StartTransaction method.
  - param `endType`: one of the enumeration's values (see the enum file)
  - remarks: You can only use the StartTransaction and EndTransaction methods when the connection with the database is active. If an exception occurs when you call EndTransaction, the changes are not committed. To correct this: - Troubleshoot and fix the exception. - Call StartTransaction. - Resubmit the changes (by calling the Add, Update, and Delete methods). - Call EndTransaction.
  - enum: `../enums/BoWfTransOpt.md`
- `Public Function GetBusinessObject(ByVal Object As BoObjectTypes) As Object` Creates a new business object.
  - param `Object`: one of the enumeration's values (see the enum file)
  - returns: The GetBusinessObject method returns the object type specified in the method's parameter. The returned object is empty and contains only the default values specified in the company database.
  - remarks: You can use this method to create business objects such as, BusinessPartners, Items, and so on. Then, to use the created object (to call methods such as, Add, Update, GetByKey, and so on) you must set the appropriate values to the object's properties (including the mandatory properties). To load an existing object from an XML file, call the GetBusinessObjectFromXML method. To release an object after using it, use the code line: Set object = Nothing
  - enum: `../enums/BoObjectTypes.md`
- `Public Function GetBusinessObjectFromXML(ByVal FileName As String, ByVal Index As Long) As Object` Creates a new business object based on a valid XML file.
  - param `FileName`: Specifies the full path and file name of the XML file that contains the business object data.
  - param `Index`: Specifies the offset of the object within the file when using an XML file that contains more than one business object. Otherwise, set the value 0.
  - remarks: You can use this method to create business objects such as, BusinessPartners, Items, and so on. To create an empty object instead of an existing one from an XML file, you can use the GetBusinessObject method. To release an object after using it, use the code line: Set vbps = Nothing To obtain the number of business objects included in the XML file, use the GetXMLelementCount method. For more information and a sample, see Exchanging Data Using the DI API XML Capabilities and Loading Data from XML.
- `Public Function GetBusinessObjectXmlSchema(ByVal Object As BoObjectTypes) As String` Retrieves the XML schema that is used by the object to validate the input XML files.
  - param `Object`: one of the enumeration's values (see the enum file)
  - remarks: Schemes use a dynamic cache mechanism so that when the first specified schema is called, the schema is created and updated dynamically with the user fields related to the object. For more information, see Exchanging Data Using the DI API XML Capabilities.
  - enum: `../enums/BoObjectTypes.md`
- `Public Function GetCompanyDate() As Date` Get Company DATE
- `Public Function GetCompanyList() As Recordset` Retrieves a list of the company databases located on the specified server.
  - returns: This method returns a Recordset object that contains a list of available companies on the server. The list includes the following four fields: - dbName - represents the database name. - cmpName - represents the company name. - versStr - represents the version number of the company database. - dbUser - represents the database owner.
  - remarks: This method is commonly used at start-up phase, when you are not sure which company databases exist on the server. Alternatively, you can use this method to allow users to choose the company database. Before using this method, you must set the correct value to the Server property. After retrieving the company databases list, you can use the Connect method to set up a connection with a specific company database.
- `Public Function GetCompanyService() As CompanyService` Creates a new CompanyService.
- `Public Function GetCompanyTime() As String` Get Company Time
- `Public Function GetContextCookie() As String` Creates a cookie that consists of the current DI API session for Sign-on Procedure.
- `Public Function GetDBServerDate() As Date` method GetDBServerDate
- `Public Function GetDBServerTime() As String` method GetDBServerTime
- `Public Sub GetLastError(ByRef errCode As Long, ByRef errMsg As String)` Retrieves the error code and message for the last error for any object tied to the Company object.
  - param `errCode`: The error code. If no error occurred, the code is 0.
  - param `errMsg`: The error message. If no error occurred, the message is an empty string. When applicable, the message also contains the application error code, for example, 10001090 - Posting period missing. More information about the error with this code can be found in the application help, accessible in the application via the Help --> Documentation --> Online Help. In the help, you can search for the error code or you can navigate to SAP Business One --> Message Documentation.
  - remarks: You must call this method immediately after the API call that caused the error. The error information is lost when you call other methods. If an error is associated with a system error, a description of the system error is included. Error Codes Code (errCode) Description (errMsg) 0 (Empty string - no error was found) -103 Connection to the company database has failed. -104 Connection to the license database has failed. -105 The observer.dll init has failed. -106 You are not connected to a company. -107 Wrong username and/or password. -108 Error reading company definitions. -109 Error copying dll to temp directory. -110 Error opening observer.dll. -111 Connection to SBO-Common has failed. -112 Error extracting dll from cab. -113 Error creating temporary dll folder. -114 No server defined. -115 No database defined. -116 Already connected to a company database. -117 Language is not supported. -118 Exceeded the number of max concurrent users. -1001 The field is to small to accept the data -1002 Invalid row. -1103 Object not supported. -1104 Invalid XML file. -1105 Invalid index. -1106 Invalid field name. -1107 Wrong object state. -1108 The transaction is already active. -1109 There is no active transaction in progress. -1110 Invalid user entered. -1111 Invalid file name. -1112 Could not save the XML file. -1113 Function not implemented. -1114 XML validation failed. -1115 No XML schema was found to support this object. -1120 Ref count for this object is higher then 0. -1130 Invalid edit state. -2000 SQL native error. -2050 No query string entered. -2051 No value found. -2052 No records found. -2053 Invalid object. -2054 Either BOF or EOF have been reached. -2055 The value entered is invalid. -3000 The logged on user does not have permission to use this object. -3001 You do not have a permission to view this fields data. -8004 Company connection is dead. -8005 Server connection is dead. -8006 Error opening language resource. -8007 License failure. -8008 Error initializing the DB layer. -8009 Too many users connected. -8010 No valid license is present. -8011 Error initializing Business objects layer. -8012 Company version mismatch. -8013 Error initializing the application environment. -8014 Invalid command. -8015 Missing parameter. . -8016 Unsupported object. -8017 Invalid command for this object. -8018 Internal permission error. -8019 Dll is not initialized. -8020 Language init error. -8021 Timeout encountered. -8022 Init error. -8023 Wrong user or password.
- `Public Function GetLastErrorCode() As Long` Retrieves the last error code issued by any object related to the Company object.
  - remarks: You can use this method, instead of GetLastError, for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Function GetLastErrorContext() As String` method GetLastErrorContext
- `Public Function GetLastErrorDescription() As String` Retrieves the description of the last error issued by any object related to the Company object.
  - remarks: You can use this method, instead of GetLastError, for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub GetNewObjectCode(ByRef ObjectCode As String)` Retrieves the key of the last added record.
  - param `ObjectCode`: Gets the key of the last object that you have created.
  - remarks: After you create a new object such as, BusinessPartners and Items objects, you can use this method to retrieve the object key. If no new object is found, the method returns an empty string in the ObjectCode parameter. You can use this method, for example, to create a payment based on an invoice: - Create invoice. - Get the key for identifying the invoice (Invoices property of the Payments object). - Create the payment.
- `Public Function GetNewObjectKey() As String` Retrieves the key of the last added record.
  - remarks: You can use this method, instead of GetNewObjectCode, for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Function GetNewObjectType() As String` Gets the last added object type.
  - remarks: After the global flag EnableApprovalProcedureInDI is turned on, we strongly recommend that you call this method each time you add any document or payment to make sure that your Documents(Payments) have been added as Document(Payment) or Draft(PaymentDraft).
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    ' Preconditions: Approval template should be set in order to make every invoice pass approval process.
    Dim dockey As String = String.Empty
    Dim docType As String = String.Empty
    Dim oInv As SAPbobsCOM.Documents = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oInvoices)

    oInv.CardCode = "BP1"
    oInv.DocDate = Date.Today

    oInv.Lines.ItemCode = "Item1"
    oInv.Lines.Quantity = 2
    oInv.Lines.Price = 5
    oInv.Lines.TaxCode = "tx001"

    ' This call must be done after all properties were filled
    ' User can change remark if they need

    ' Fill Approval Request sub object
    oInv.GetApprovalTemplates()
    oInv.Document_ApprovalRequests.Remarks = "Some Remarks for approval"

    Dim ret As Integer
    'Invoice was added as draft
    ret = oInv.Add()

    If ret = 0 Then
        'Get new added object key and type
        dockey = oCompany.GetNewObjectKey()
        docType = oCompany.GetNewObjectType()
    End If
    ```
- `Public Function GetRegisteredServersList() As Recordset` Retrieves a list of servers registered with the System Landscape Directory (SLD) server. Use this method when creating a window for logging into SAP Business One. Create a dropdown list of servers and allow the user to select the server to which to connect.
  - C# example (from SAP's help):
    ```csharp
    Company oCompany = new SAPbobsCOM.Company();
    oCompany.SLDServer = "myServer:40000";

    Recordset oRecordset = oCompany.GetRegisteredServersList();

    while (!oRecordset.EoF)
    {
        Console.WriteLine(oRecordset.Fields.Item(0).Value.ToString());
        oRecordset.MoveNext();
    }
    ```
- `Public Function GetXMLelementCount(ByVal FileName As String) As Long` Retrieves the number of business objects described in an XML file.
  - param `FileName`: Specifies the full path and file name of the XML file containing the Business objects.
  - remarks: Use this method find out how many business objects are described in the XML file when using the method GetBusinessObjectFromXML, and you want to . For more information, see Exchanging Data Using the DI API XML Capabilities.
- `Public Function GetXMLobjectType(ByVal FileName As String, ByVal Index As Long) As BoObjectTypes` Retrieves the type of business object described in an XML file on a specific offset specified by the Index parameter.
  - param `FileName`: Specifies the full path and file name of the XML file containing the Business objects.
  - param `Index`: Specifies the offset of the Business object within the file, when using an XML file containing more the one Business object. Otherwise, you can enter the value 0.
  - remarks: Before using the GetXMLobjectType method, use the GetXMLelementCount to find out the number of business objects described in the XML file.
- `Public Function IsDTCTransactionObjectSet() As Boolean` Checks whether or not the DTCTransactionObject is set.
- `Public Function SetSboLoginContext(ByVal conStr As String) As Long` Decodes the encrypted connection information received from the UI API -- based on the cookie created by the GetContextCookie method -- and then sets the connection information for log on to the Company database. See Sign-on Procedure.
  - param `conStr`: Specifies the connection information string.
- `Public Sub StartTransaction()` Starts a transaction, allowing you to perform data operations on several business objects. Use the EndTransaction method to end the transaction and free locked records, allowing other users to access them.
  - remarks: Use this method when you want to perform data operations on several business objects: - If the operations succeed, either commit the transaction to save the data in the database, or roll back to discard the changes. - If one of the operations fail, the DI API rolls back the transaction, which discards the changes. After a failed DI API call in the transaction, you must immediately exit the transaction (see the example below).
  - example note: When working with transactions, make sure to check the return code when executing SAP Business One APIs and, if an error occurs, immediately exit the transaction. If a call fails, SAP Business One automatically ends the transaction with a rollback (of all actions up to that point); if you do not exit the transaction code, all subsequent code is still executed even though an error occurred.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        int errorCode = 0;
        bool findItem = false;
        string errorMessage = string.Empty;
        SAPbobsCOM.Company company = new SAPbobsCOM.Company();

        company.Server = "PVGD50059267A";//mandatory property
        //mandatory property in release 8.8 and afterwards. Before release 8.8, dst_MSSQL (SQL Server 2000) is the default value.
        company.DbServerType = SAPbobsCOM.BoDataServerTypes.dst_MSSQL2005;
        company.CompanyDB = "2009";//mandatory property
        company.UserName = "manager";//mandatory property
        company.Password = "1234";//mandatory property

        company.DbUserName = "sa"; //optional in release 8.8 and afterwards
        company.DbPassword = "sasa"; //optional in release 8.8 and afterwards
        company.UseTrusted = false; //optional in release 8.8 and afterwards
        company.language = SAPbobsCOM.BoSuppLangs.ln_English; //optional
        //Optional, default value is from DI configuration file in release 8.8 and afterwards
        company.SLDServer = "PVGD50059267A:40000";
        errorCode = company.Connect();
        if (errorCode != 0)
        {
            //You can also use GetLastError to get the error code and error message at the same time.
            errorMessage = company.GetLastErrorDescription();
            MessageBox.Show("Fail to conect to SAP Business One. " + "Error Code: " + errorCode.ToString() + " Error Message: " + errorMessage);
            return;
        }

        company.StartTransaction();
        SAPbobsCOM.Items item = company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oItems) as SAPbobsCOM.Items;
        findItem = item.GetByKey("itemcode");
        if (!findItem)
        {
            MessageBox.Show("Can not find the item.");
            return;
        }
        item.BarCode = "1234567";
        errorCode = item.Update();
        if (errorCode != 0)
        {
            company.GetLastError(out errorCode, out errorMessage);
            MessageBox.Show("Fail to update item master data. " + "Error Code: " + errorCode.ToString() + " Error Message: " + errorMessage);
            //transaction started has been rolled back by SAP Business One automaticly. Just return the code and do your error handling.
            return;
        }

        // Get predefined text service
        SAPbobsCOM.CompanyService companyService = company.GetCompanyService();
        SAPbobsCOM.PredefinedTextsService textService = companyService.GetBusinessService(SAPbobsCOM.ServiceTypes.PredefinedTextsService) as SAPbobsCOM.PredefinedTextsService;

        // Add predefined text
        SAPbobsCOM.PredefinedText text = textService.GetDataInterface(SAPbobsCOM.PredefinedTextsServiceDataInterfaces.ptsPredefinedText) as SAPbobsCOM.PredefinedText;
        text.TextCode = "text code";
        text.Text = "test content";
        try
        {
            SAPbobsCOM.PredefinedTextParams param = textService.AddPredefinedText(text);
        }
        catch (System.Runtime.InteropServices.COMException ex)
        {
            MessageBox.Show(ex.ErrorCode.ToString());
            MessageBox.Show(ex.Message);
            //transaction started has been rolled back by SAP Business One automaticly. Just return the code and do your error handling.
            return;
        }

        company.EndTransaction(SAPbobsCOM.BoWfTransOpt.wf_Commit);
        company.Disconnect();
    }
    catch (Exception ex)
    {
        // ... unexpected error
    }
    ```

## Events (1)
- `Public Event ProgressIndicator(ByVal MaxValue As Long, ByVal CurrentValue As Long)` Progress indicator for long process execution. To be supported in future releases.
