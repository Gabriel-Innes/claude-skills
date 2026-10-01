<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# CompanyService (Object)

The CompanyService enables to manage the company administration data. This includes the following tables: - Administration data - OADM (AdminInfo object). - Company data - CINF (CompanyInfo object). - Posting Periods - OACT (ChartOfAccounts object). - Finance Periods - OFPR (FinancePeriods object). You can also retrieve the status of the application features, whether these features are blocked or not, according to the installation type and localization (see GetFeaturesStatus method).

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method.

## Methods (30)
- `Public Function CreatePeriod(ByVal pIPeriodCategory As PeriodCategory) As PeriodCategoryParams` Returns the PeriodCategoryParams Identification Key (PeriodCategory Key) based on the PeriodCategory data structure.
  - param `pIPeriodCategory`: PeriodCategory data structure input.
  - example note: The following is a VB.NET sample that creates new period categories and returns its parameters.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oPeriodCategory As PeriodCategory

    'get period category

    oPeriodCategory =     oCompanyService.GetDataInterface(CompanyServiceDataInterfaces.csdiPeriodCategory)

    'set period code

    oPeriodCategory.PeriodCategory = "My Period Code"

    'set period name

    oPeriodCategory.PeriodName = "My Period Name"

    'set the period type can be year,quater,month or day

    '(e.g. spt_Year=0,spt_quater=1,spt_month=2,spt_days)

    oPeriodCategory.SubPeriodType = BoSubPeriodTypeEnum.spt_Year

    'set the beginning of Financial Year

    oPeriodCategory.BeginningofFinancialYear ="2008-01-01"

    oCompanyService.CreatePeriod(oPeriodCategory)
    ```
- `Public Function CreatePeriodWithFinanceParams(ByVal pIPeriodCategory As PeriodCategory, ByVal pIFinancePeriodParams As FinancePeriodParams) As PeriodCategoryParams` Returns a PeriodCategoryParams Identification Key, extended with finance parameters derived by the FinancePeriodParams identification key (system number, period indicator).
  - param `pIPeriodCategory`: PeriodCategory data structure input.
  - param `pIFinancePeriodParams`: FinancePeriodParams identification key (system number, period indicator) input.
- `Public Function GetAdminInfo() As AdminInfo` Returns the AdminInfo data structure.
  - example note: The following is a VB.NET sample that retrieves the administration information.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim oCompanyAdminInfo As AdminInfo

    Dim sAddress As String

    'get company service

    oCompanyService = oCompany.GetCompanyService

    'get admin info

    oCompanyAdminInfo = oCompanyService.GetAdminInfo

    'set company name

    oCompanyAdminInfo.CompanyName ="My Company"

    'set Company color

    'Sets the number of the background color for active windows

    '(e.g Red=8,Orange=7)

    oCompanyAdminInfo.CompanyColor = 8

    'set phone number

    oCompanyAdminInfo.PhoneNumber1 ="6666666"

    'set email

    oCompanyAdminInfo.EMail ="MyMail@mail.com"

    'update the admin info

    oCompanyService.UpdateAdminInfo(oCompanyAdminInfo)
    ```
- `Public Function GetAdvancedGLAccount(ByVal pIAdvancedGLAccountParams As AdvancedGLAccountParams) As AdvancedGLAccountReturnParams` method GetAdvancedGLAccount
  - param `pIAdvancedGLAccountParams`: 
- `Public Function GetBlob(ByVal pIBlobParams As BlobParams) As Blob` Gets the contents of a blob field in the SAP Business One database. NOTE: If you want to save a blob field to a file, we recommend that you use the SaveBlobToFile method.
  - param `pIBlobParams`: The database table and its blob field, the key of the record whose blob field is to be retrieved, and the path to the file where the blob field contents are to be saved.
  - C# example (from SAP's help):
    ```csharp
    string blobNewFilePath = @"C:\myblobfile.zip";

    SAPbobsCOM.CompanyService oCompanyService = oCompany.GetCompanyService();

    // Specify a table and blob field
    SAPbobsCOM.BlobParams oBlobParams;
    oBlobParams = (SAPbobsCOM.BlobParams)oCompanyService.GetDataInterface(SAPbobsCOM.CompanyServiceDataInterfaces.csdiBlobParams);
    oBlobParams.Table = "RDOC";
    oBlobParams.Field = "Template";

    // Specify key name and key value of a record to update
    SAPbobsCOM.BlobTableKeySegment oKeySegment;
    oKeySegment = oBlobParams.BlobTableKeySegments.Add();
    oKeySegment.Name = "DocCode";
    oKeySegment.Value = "ACT10001";

    SAPbobsCOM.Blob oBlob;
    oBlob = (SAPbobsCOM.Blob)oCompanyService.GetDataInterface(SAPbobsCOM.CompanyServiceDataInterfaces.csdiBlob);

    // Get contents of a blob field
    oBlob = oCompanyService.GetBlob(oBlobParams);

    // Convert Base64 string to binary
    byte[] buf;
    buf = Convert.FromBase64String(oBlob.Content);

    // Write blob file to file system
    FileStream oFile = new FileStream(blobNewFilePath, FileMode.Create, FileAccess.Write);
    oFile.Write(buf, 0, buf.Length);
    oFile.Close();
    oFile.Dispose();
    ```
- `Public Function GetBusinessService(ByVal enumServiceType As ServiceTypes) As Object` Creates a specified business service. Use this method for all types of services
  - param `enumServiceType`: one of the enumeration's values (see the enum file)
  - enum: `ServiceTypes` in `../enums/enums-03.md`
- `Public Function GetCompanyInfo() As CompanyInfo` Returns the CompanyInfo data structure.
  - example note: The following is a VB.NET sample that retrieves the company information.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCompanyInfo As CompanyInfo

    Dim oCompanyService As SAPbobsCOM.CompanyService

    'get company service

    oCompanyService = oCompany.GetCompanyService

    'Get company info

    oCompanyInfo = oCompanyService.GetCompanyInfo

    'Set the Auto Create Customer Equipment Card (1=yes ,0=No)

    oCompanyInfo.AutoCreateCustomerEqCard = BoYesNoEnum.tYES

    'Set Block Stock Negative Quantity(1=yes ,0=No)

    oCompanyInfo.BlockStockNegativeQuantity = = BoYesNoEnum.tYES

    'Update the company info

    oCompanyService.UpdateCompanyInfo(oCompanyInfo)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As CompanyServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CompanyServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - example note: Shows how to get Company Admin Info from an XML file.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim oCompanyAdminInfo As AdminInfo

    Dim oCompanyAdminInfoXmlFile As AdminInfo

    'get company service

    oCompanyService = oCompany.GetCompanyService

    'get admin info

    oCompanyAdminInfo = oCompanyService.GetAdminInfo

    'save data to xml file

    oCompanyAdminInfo.ToXMLFile("C:\CompanyAdminInfo.xml")

    'create CompanyAdminInfo from xml file

    oCompanyAdminInfoXmlFile = oCompanyService.GetDataInterfaceFromXMLFile("C:\CompanyAdminInfo.xml")
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: XML string.
  - example note: Shows how to get Company Admin Info from an XML string.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim oCompanyAdminInfo As AdminInfo

    Dim oCompanyAdminInfoXmlStr As AdminInfo

    Dim sCompanyAdminInfoXmlStr As String

    'get company service

    oCompanyService = oCompany.GetCompanyService

    'get admin info

    oCompanyAdminInfo = oCompanyService.GetAdminInfo

    'save data to xml string

    sCompanyAdminInfoXmlStr = oCompanyAdminInfo.ToXMLString()

    'create CompanyAdminInfo from xml string

    oCompanyAdminInfoXmlStr = oCompanyService.GetDataInterfaceFromXMLString(sCompanyAdminInfoXmlStr)
    ```
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim oFinancePeriodParams As FinancePeriodParams

    'get company service

    oCompanyService = oCompany.GetCompanyService

    'create finance period data structure

    oFinancePeriodParams = oCompanyService.GetDataInterface(CompanyServiceDataInterfaces.csdiFinancePeriodParams)

    'fill the code of the finance period

    oFinancePeriodParams.AbsoluteEntry = 13

    'remove finance period

    oCompanyService.RemoveFinancePeriod(oFinancePeriodParams)
    ```
- `Public Function GetFeaturesStatus() As FeatureStatusCollection` Returns the FeatureStatusCollection. A feature status can be either blocked or not.
- `Public Function GetFinancePeriod(ByVal pIFinancePeriodParams As FinancePeriodParams) As FinancePeriod` Returns a FinancePeriod data structure according to the specified finance period key parameters.
  - param `pIFinancePeriodParams`: Finance period key parameters input.
- `Public Function GetFinancePeriods(ByVal pIPeriodCategoryParams As PeriodCategoryParams) As FinancePeriods` Returns the FinancePeriods collection according to the specified period category key parameters.
  - param `pIPeriodCategoryParams`: Period category key parameters.
- `Public Function GetGeneralService(ByVal sServiceCode As String) As GeneralService` Returns an instance of GeneralService for the specified user-defined object (UDO). The GeneralService instance can be used to add, retrieve and delete rows of the main table and child tables linked to the specified UDO.
  - param `sServiceCode`: The name of the UDO for which to create an instance of the GeneralService service.
- `Public Function GetItemPrice(ByVal pIItemPriceParams As ItemPriceParams) As ItemPriceReturnParams` Returns the ItemPriceReturnParams.
  - param `pIItemPriceParams`: 
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim params As SAPbobsCOM.ItemPriceParams

    Dim rtnParams As SAPbobsCOM.ItemPriceReturnParams

    Try

          params = vCmp.GetCompanyService.GetDataInterface(CompanyServiceDataInterfaces.csdiItemPriceParams)

          params.CardCode = "C001"

          params.ItemCode = "I002"

          params.UoMEntry = 1

          params.UoMQuantity = 2

          params.InventoryQuantity=6

          params.Currency = "EUR"

          params.Date = "01.13.2013"

          params.PriceList = 1

          params.BlanketAgreementNumber = 2

          params.BlanketAgreementLine = 1

          rtnParams = vCmp.GetCompanyService.GetDataInterface(CompanyServiceDataInterfaces.csdiItemPriceReturnParams)

          rtnParams = vCmp.GetCompanyService().GetItemPrice(params)

           RCurrency = rtnParams.Currency

           RPrice = rtnParams.Price

           RDiscount = rtnParams.Discount

         Catch ex As System.Exception

              ...

         End Try
    ```
- `Public Function GetPathAdmin() As PathAdmin` Returns an object for setting and getting directory paths for storing various files.
- `Public Function GetPeriod(ByVal pIPeriodCategoryParams As PeriodCategoryParams) As PeriodCategory` Returns the PeriodCategory data structure according to the specified period category key parameters.
  - param `pIPeriodCategoryParams`: Period category key parameters input.
  - example note: The following is a VB.NET sample that retrieves the period categories by its parameters.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim oPeriodCategoryColl As PeriodCategoryParamsCollection

    Dim oPerCategory As PeriodCategory

    Dim oFinancePeriods As FinancePeriods

    Dim oFinancePeriod As FinancePeriod

    Dim i As Integer

    Dim j As Integer

    'get company service

    oCompanyService = oCompany.GetCompanyService

    'get Period Category Collection

    oPeriodCategoryColl = oCompanyService.GetPeriods

    'print all periods

    For i = 0 To oPeriodCategoryColl.Count - 1

       'get period category

        oPerCategory = oCompanyService.GetPeriod(oPeriodCategoryColl.Item(i))

        'print period category name

        Debug.WriteLine(oPerCategory.PeriodName)

        'get all finance periods (if the sub period isn't a year then it

        'has more than one finance period, for example sub period month has 12 finance periods)

        oFinancePeriods = oCompanyService.GetFinancePeriods(oPeriodCategoryColl.Item(i))

        For j = 0 To oFinancePeriods.Count - 1

            'get finance period

            oFinancePeriod = oFinancePeriods.Item(j)

            'print the period name

            Debug.WriteLine(oFinancePeriod.PeriodName)

        Next j

    Next i
    ```
- `Public Function GetPeriods() As PeriodCategoryParamsCollection` Returns the PeriodCategoryParamsCollection.
- `Public Function GetServiceMetaData(ByVal ServiceCode As ServiceTypes) As String` GetServiceMetaData
  - param `ServiceCode`: one of the enumeration's values (see the enum file)
  - enum: `ServiceTypes` in `../enums/enums-03.md`
- `Public Function IsUserLicensed(ByVal bstrUserName As String, ByVal bstrLicType As String) As Boolean` IsUserLicensed
  - param `bstrUserName`: 
  - param `bstrLicType`: 
- `Public Sub LoadBlobFromFile(ByVal pIBlobParams As BlobParams)` Loads a file into a blob field in the SAP Business One database.
  - param `pIBlobParams`: The database table and its blob field, the key of the record whose blob field is to be set, and the path to the file to be uploaded to the blob field.
  - C# example (from SAP's help):
    ```csharp
    string blobFile = @"C:\0.gif.zip";
    SAPbobsCOM.CompanyService oCompanyService = MainModule.oCompany.GetCompanyService();

    // Specify the table and field to which to load the blob field
    BlobParams oBlobParams = (BlobParams)oCompanyService.GetDataInterface(SAPbobsCOM.CompanyServiceDataInterfaces.csdiBlobParams);
    oBlobParams.Table = "RDOC";
    oBlobParams.Field = "Template";

    // Specify the file to load into the DB
    string blobNewFilePath = @"C:\myblobfile1.zip";
    oBlobParams.FileName = blobNewFilePath;

    // Specify the key field and key of the record whose blob field Is to be set
    BlobTableKeySegment oKeySegment = oBlobParams.BlobTableKeySegments.Add();
    oKeySegment.Name = "DocCode";
    oKeySegment.Value = "ACT10001";

    // Load file into DB field
    oCompanyService.LoadBlobFromFile(oBlobParams);
    ```
- `Public Function RoundDecimal(ByVal pIDecimalData As DecimalData) As RoundedData` Rounds data to a specified number of decimal places or to a whole number if no decimal places are specified.
  - param `pIDecimalData`: The data to be rounded.
  - remarks: - Tax rounding is not supported for China, Japan, and Korea. - Rounding for budget amounts and price list amounts is not supported.
- `Public Sub SaveBlobToFile(ByVal pIBlobParams As BlobParams)` Saves to a file the contents of a blob field in the SAP Business One database.
  - param `pIBlobParams`: The database table and its blob field, the key of the record whose blob field is to be saved to a file, and the path of the file to be saved with the contents of the blob field.
  - C# example (from SAP's help):
    ```csharp
    // Specify the table and blob field
    BlobParams oBlobParams = (SAPbobsCOM.BlobParams)oCompanyService.GetDataInterface(SAPbobsCOM.CompanyServiceDataInterfaces.csdiBlobParams);
    oBlobParams.Table = "RDOC";
    oBlobParams.Field = "Template";

    // Specify the file name to which to write the blob
    string blobNewFilePath = @"C:\myblobfile.zip";
    oBlobParams.FileName = blobNewFilePath;

    // Specify the key field and value of the row from which to get the blob
    BlobTableKeySegment oKeySegment;
    oKeySegment = oBlobParams.BlobTableKeySegments.Add();
    oKeySegment.Name = "DocCode";
    oKeySegment.Value = "ACT10001";

    // Save the blob to the file
    oCompanyService.SaveBlobToFile(oBlobParams);
    ```
- `Public Sub SetBlob(ByVal pIBlobParams As BlobParams, ByVal pIBlob As Blob)` Sets a blob field in the SAP Business One database. NOTE: If you want to load a blob field to a file, we recommend that you use the LoadBlobFromFile method.
  - param `pIBlobParams`: The database table, blob field, and records whose blob field is to be set
  - param `pIBlob`: The blob content
  - C# example (from SAP's help):
    ```csharp
    string blobFilePath = @"C:\myblobfile.zip";

    SAPbobsCOM.CompanyService oCompanyService = _company.GetCompanyService();

    // Specify a table and blob field
    BlobParams oBlobParams = (BlobParams)oCompanyService.GetDataInterface(SAPbobsCOM.CompanyServiceDataInterfaces.csdiBlobParams);
    oBlobParams.Table = "RDOC";
    oBlobParams.Field = "Template";

    // Specify key name and key value of a record to update
    BlobTableKeySegment oKeySegment = oBlobParams.BlobTableKeySegments.Add();
    oKeySegment.Name = "DocCode";
    oKeySegment.Value = "ACT10001";

    Blob oBlob = (Blob)oCompanyService.GetDataInterface(CompanyServiceDataInterfaces.csdiBlob);

    // Put blob file into memory buffer
    FileStream oFile = new FileStream(blobFilePath, System.IO.FileMode.Open);
    int fileSize = (int)oFile.Length;
    byte[] buf = new byte[fileSize];
    oFile.Read(buf, 0, fileSize);
    oFile.Close();

    // Convert memory buffer to Base64 string
    string blobStr = Convert.ToBase64String(buf, 0, fileSize);

    // Set Base64 string to Blob object
    oBlob.Content = blobStr;

    try
    {
        // Upload Blob to B1 company database
        oCompanyService.SetBlob(oBlobParams, oBlob);
    }
    catch (System.Exception ex)
    {
        string errmsg = ex.Message;
    }
    ```
- `Public Sub UpdateAdminInfo(ByVal pIAdminInfo As AdminInfo)` Updates the AdminInfo data.
  - param `pIAdminInfo`: AdminInfo data input.
- `Public Sub UpdateCompanyInfo(ByVal pICompanyInfo As CompanyInfo)` Updates the CompanyInfo data.
  - param `pICompanyInfo`: CompanyInfo data input.
- `Public Sub UpdateFinancePeriod(ByVal pIFinancePeriod As FinancePeriod)` Updates the FinancePeriod data.
  - param `pIFinancePeriod`: FinancePeriod data input.
  - example note: Shows how to update a Finance Period
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim oPeriodCategoryColl As PeriodCategoryParamsCollection

    Dim oPerCategory As PeriodCategoryParams

    Dim oFinancePeriods As FinancePeriods

    Dim oFinancePeriod As FinancePeriod

    'get company service

    oCompanyService = oCompany.GetCompanyService

    'get period category Collection

    oPeriodCategoryColl = oCompanyService.GetPeriods

    'get period category params

    oPerCategory = oPeriodCategoryColl.Item(1)

    'get all finance periods (if the sub period isn't a year then it

    'has more than one finance period for example sub period month has 12 finance

    'periods)

    oFinancePeriods = oCompanyService.GetFinancePeriods(oPerCategory)

    'get the first finance period

    oFinancePeriod = oFinancePeriods.Item(0)

    'update the period name

    oFinancePeriod.PeriodName = "MyFinancePeriod"

    'update finance period

    oCompanyService.UpdateFinancePeriod(oFinancePeriod)
    ```
- `Public Sub UpdatePathAdmin(ByVal pIPathAdmin As PathAdmin)` Updates the paths for storing various files.
  - param `pIPathAdmin`: The updated data.
- `Public Sub UpdatePeriod(ByVal pIPeriodCategory As PeriodCategory)` Updates the PeriodCategory data.
  - param `pIPeriodCategory`: PeriodCategory data input.
  - example note: shows how to update a Period Category
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
          Dim oCompanyService As SAPbobsCOM.CompanyService

            Dim oPeriodCategoryColl As PeriodCategoryParamsCollection

            Dim oPerCategory As PeriodCategory

            'get company service

            oCompanyService = oCompany.GetCompanyService

            'get period category Collection

            oPeriodCategoryColl = oCompanyService.GetPeriods

            'get period category

            oPerCategory = oCompanyService.GetPeriod(oPeriodCategoryColl.Item(0))

            'set the Default Customer For A/R Invoice And Payment

            oPerCategory.InvoicePaymentBP = "C20000"

            'update period category

            oCompanyService.UpdatePeriod(oPerCategory)
    ```
- `Public Sub UpdateUserLicense(ByVal pIUserLicenseParams As UserLicenseParams)` Assigns an SAP Business One license to a user, or removes a license from a user.
  - param `pIUserLicenseParams`: The user and the license type to assign to the user or remove from the user.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Try

        Dim oCompanyService As SAPbobsCOM.CompanyService

        oCompanyService = oCompany.GetCompanyService

        Dim oUserLicenseParam As SAPbobsCOM.UserLicenseParams

        ' Set parameters

        oUserLicenseParam = oCompanyService.GetDataInterface(SAPbobsCOM.CompanyServiceDataInterfaces.csdiUserLicenseParams)

        oUserLicenseParam.UserName = "manager"

        oUserLicenseParam.LicenseKeyType = SAPbobsCOM.LicenseKeyTypeEnum.lktdIdirect

        oUserLicenseParam.LicenseUpdateType = SAPbobsCOM.LicenseUpdateTypeEnum.ultAssign

        ' Update user's license

        oCompanyService.UpdateUserLicense(oUserLicenseParam)

    Catch ex As Exception

        MsgBox(ex.ToString)

    End Try
    ```

# ContactEmployeeBlockSendingMarketingContents (Object)

Block sending marketing contnet to the contact employee.

## Properties (3)
- `Public Property Choose() As BoYesNoEnum` [R/W] Choose to block sending marketing contnet to the contact employee.
- `Public Property CommunicationMediaId() As Long` [R/W] Communication media code. Field name: CommCode. Length: 50 characters.
- `Public Property ContactEmployeeAbsEntry() As Long` [R/W] The contact employee code. Field name: CntctCode. Length: 11 characters.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ContactEmployees (Object)

ContactEmployees is a business object that represents the contact employees in the Business Partners module. This object enables you to add contact information of employees to the Business Partners master record. Source table: OCPR.

**Remarks:** Mandatory fields in SAP Business One: Name. To display the form in the application: - Select Business Partners --> Business Partner Master Data --> Contact Persons tab.

## Properties (36)
- `Public Property Active() As BoYesNoEnum` [R/W] Indicates whether or not the contact person for a particular business partner is available for selection in transactions.
- `Public Property Address() As String` [R/W] Sets or returns the employee address. Field name: Address. Length: 100 characters.
- `Public Property BlockSendingMarketingContent() As BoYesNoEnum` [R/W] Specifies whether or not to block sending marketing contnet to the contact employee. Field name: BlockComm. Length: 1 character.
- `Public Property CardCode() As String` [R] Returns the business partner identification number. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CityOfBirth() As String` [R/W] Sets or returns the city of birth of the employee. Field name: BirthCity. Length: 100 characters.
- `Public Property ConnectedAddressName() As String` [R/W] Description of the connected address. Field name: CnnectAddr. Length: 50 characters.
- `Public Property ConnectedAddressType() As BoAddressType` [R/W] Type of the connected address: B stands for bill to or pay to address; S stands for ship to address. Field name: CnAddrType.
- `Public Property ContactEmployeeBlockSendingMarketingContents() As ContactEmployeeBlockSendingMarketingContents` [R] Returns the ContactEmployeeBlockSendingMarketingContents object.
- `Public Property Count() As Long` [R] Returns the number of contact employees included in the object.
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property CreateTime() As Date` [R] property CreateTime
- `Public Property DateOfBirth() As Date` [R/W] Sets or returns the employee birth date. Field name: BirthDate.
- `Public Property E_Mail() As String` [R/W] Sets or returns the e-mail address of the contact employee. Field name: E_MailL. Length: 100 characters.
- `Public Property EmailGroupCode() As String` [R/W] property EmailGroupCode
- `Public Property Fax() As String` [R/W] Sets or returns the fax number of the contact employee. Field name: Fax. Length: 50 characters.
- `Public Property FirstName() As String` [R/W] property FirstName
- `Public Property ForeignCountry() As String` [R/W] Field name: Frgncntry. Length: 3 characters.
  - remarks: For the Italy localization only, field "Stato Estero".
- `Public Property Gender() As BoGenderTypes` [R/W] Sets or returns a valid value of BoGenderTypes that specifies the employee gender. Field name: Gender.
- `Public Property InternalCode() As Long` [R] Returns the internal code of the contact employee. Field name: CntctCode.
- `Public Property LastName() As String` [R/W] property LastName
- `Public Property MiddleName() As String` [R/W] property MiddleName
- `Public Property MobilePhone() As String` [R/W] Sets or returns the employee mobile phone number. Field name: Cellolar. Length: 50 characters.
- `Public Property Name() As String` [R/W] Sets or returns the employee name. Field name: Name. Mandatory property. Length: 50 characters.
- `Public Property Pager() As String` [R/W] Sets or returns the pager number of the employee. Field name: Pager. Length: 30 characters.
- `Public Property Password() As String` [R/W] Sets or returns the employee access password to e-commerce applications. Field name: Password. Length: 8 characters.
  - remarks: This property is used for B2C and B2B systems.
- `Public Property Phone1() As String` [R/W] Sets or returns the primary phone number of the employee. Field name: Tel1. Length: 50 characters.
- `Public Property Phone2() As String` [R/W] Sets or returns the secondary phone number of the employee. Field name: Tel2. Length: 50 characters.
- `Public Property PlaceOfBirth() As String` [R/W] Sets or returns the country of birth of the employee. Field name: BirthPlace. Length: 100 characters.
- `Public Property Position() As String` [R/W] Sets or returns the employee position in the company. Field name: Position. Length: 90 characters.
- `Public Property Profession() As String` [R/W] Sets or returns the employee profession. Field name: Profession. Length: 50 characters.
- `Public Property Remarks1() As String` [R/W] Sets or returns remarks for the employee. Field name: Notes1. Length: 100 characters.
- `Public Property Remarks2() As String` [R/W] Sets or returns secondary remarks for the employee. Field name: Notes2. Length: 100 characters.
- `Public Property Title() As String` [R/W] Sets or returns the Contact Employee's Title. Field name: Title. Field name: Title. Length: 10 characters.
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Date` [R] property UpdateTime
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new contact employee.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: To save the information to the database, use the BusinessPartners object, Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: If you delete the default contact employee, the first contact employee in the remaining list becomes the default.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.BusinessPartners oBP;

    // Delete contact employee
    if (oBP.GetByKey("BP1") == true)
    {
        oBP.ContactEmployees.SetCurrentLine(0);
        oBP.ContactEmployees.Delete();
        oBP.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Contacts (Object)

Contacts is a business object that represents the activities with customers and vendors in the Business Partners module. This object enables you to: - Add an activity. - Retrieve an activity by its key. - Update an activity. - Save the object in XML format. Source table: OCLG.

**Remarks:** Mandatory fields in SAP Business One: CardCode (only if the activity is not personal) and ContactPersonCode. To display the form in the application: - Select Business Partners --> Activities. Auto-complete of the Activity Schedule Properties (new for release 2005) The schedule of the activity must be specified at the database level, therefore the system completes automatically the values of the properties that are related to the activity schedule. These properties include: - Start time - combination of StartDate and StartTime. - Duration - combination of Duration and DurationType. - End time - combination of EndDuedate and EndTime. When adding or updating an activity, there are five scenarios for the auto-complete operation according to the specified values: 1. If no value is specified (when adding only), then the system sets the following default values: - Start time - the current time when adding the activity. - Duration - 15 minutes (0 minute when upgrading the system to release 2005). - End time - the system calculates the values as follows: End time = Start time + Duration. 2. If all three values are specified (when adding or updating), then the system checks their validity, and if there is an error the system issues an error message (-5002 - invalid object). 3. If two values are specified (or modified when updating), then the system calculates (or recalculates) the remaining value as follows: - Start time and End time are specified - the system calculates the Duration. - Start time and Duration are specified - the system calculates the End time. - Duration and End time are specified - when adding, the system sets Start time to default and recalculates the Duration. When updating, the Start time remains the same and the system recalculates the Duration. 4. If one value is specified (when adding only), then the system calculates the remaining values as follows: - Start time is specified - the system sets the Duration to default and calculates the End time. - Duration is specified - the system sets the Start time to default and calculates the End time. - End time is specified - the system sets the Start time to default and calculates the Duration. 5. If one value is modified (when updating only), then the system recalculates the remaining value as follows: - Start time is specified - the system recalculates the End time (for release 2005) or the Duration (for release 2004). - Duration is specified - the system recalculates the End time. - End time is specified - the system recalculates the Duration.

## Properties (48)
- `Public Property Activity() As BoActivities` [R/W] Sets or returns a valid value of BoActivities type that specifies activity with the business partner. Field name: Action.
- `Public Property ActivityType() As Long` [R/W] Sets or returns the type of the activity. Field name: CntctType. This is a foreign key to the ActivityTypes object.
  - remarks: You can add new activity types to the list using the ActivityTypes object.
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Mandatory field in SAP Business One only if the activity is not personal . Length: 15 characters. This is a foreign key to the BusinessPartners object.
  - remarks: Mandatory property. SAP Business One validates the CardCode, and if not valid, returns an error code.
- `Public Property City() As String` [R/W] Sets or returns the city where the Activity (Meeting type only) with the business partner takes place. Field name: city. Length: 100 characters.
- `Public Property Closed() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the activity is closed and no further processing is required. Field name: Closed.
  - remarks: You can use the CloseDate property to find out the closing date.
- `Public Property CloseDate() As Date` [R/W] Sets or returns the closing date of the activity. Field name: CloseDate.
  - remarks: In case the end-user does not enter a value, the system completes automatically the closing date.
- `Public Property ContactCode() As Long` [R] Returns the identification key of the activity. Field name: CntctCode.
- `Public Property ContactDate() As Date` [R/W] Sets or returns the contact date. Field name: CntctDate.
- `Public Property ContactPersonCode() As Long` [R/W] Sets or returns the internal code for the contact person. Field name: CntctCode. Mandatory property. This is a foreign key to the ContactEmployees object.
- `Public Property ContactTime() As Date` [R/W] Sets or returns the activity time. Field name: CntctTime.
  - remarks: In case the end-user does not enter a value, the system completes automatically the contact time.
- `Public Property Country() As String` [R/W] Sets or returns the country where the Activity (Meeting type only) with the business partner takes place. Field name: country. Length: 3 characters. This is a foreign key to the Countries table (OCRY).
- `Public Property Details() As String` [R/W] Sets or returns the details for the next action. Field name: Details. Length: 60 characters.
- `Public Property DocEntry() As String` [R/W] Sets or returns the document entry key. Field name: DocEntry. Length: 20 characters.
  - remarks: You can use this key to reference a document.
- `Public Property DocNum() As String` [R] Returns the number of the linked document. Field name: DocNum. Length: 20 characters.
- `Public Property DocType() As Long` [R/W] Sets or returns the type of the document, such as invoice or purchase order, that is linked to the activity. Field name: DocType.
- `Public Property DocTypeEx() As String` [R/W] The document type that is linked to the activity. This property replaces the DocType property (integer). Length: 20 characters. Field name: DocNum.
  - remarks: The valid values are: '13' - 'A/R Invoice' '14' - 'A/R Credit Memo' '15' - 'Delivery' '16' - 'Return' '17' - 'Sales Order' '18' - 'A/P Invoice' '19' - 'A/P Credit Memo' '20' - 'Goods Receipt PO' '21' - 'Goods Return' '22' - 'Purchase order' '23' - 'Sales Quotation' '24' - 'Incoming Payment' '25' - 'Deposit' '30' - 'Journal Entry' '46' - 'Outgoing Payment' '57' - 'Checks for Payment' '59' - 'Goods Receipt' '60' - 'Goods Issue' '1250000001' - 'Stock Transfer Request' '67' - 'Stock Transfer' '68' - 'Work Order' '69' - 'Landed Costs' '132' - 'Correction Invoice' '162' - 'Material Revaluation' '202' - 'Production Order' '203' - 'AR Down Payment' '204' - 'AP Down Payment' '140000009' - 'Outgoing Excise Invoice' '140000010' - 'Incoming Excise Invoice' '-1' - '' '0' - '' '4' - 'Items' '163' - 'AP Correction Invoice' '164' - 'AP Correction Invoice Reversal' '165' - 'AR Correction Invoice' '166' - 'AR Correction Invoice Reversal' '1320000012' - 'Campaign' '540000006' - 'Purchase Quotation' '1250000025' - 'Blanket Agreements' '1470000113' - 'Purchase Request' '112' - 'Document Drafts' '140' - 'Payment Drafts' '123' - 'Checks for Payment Drafts' '254000065' - 'Self Invoice' '254000066' - 'Self Credit Note' '234000031' - 'Return Request' '234000032' - 'Goods Return Request' '1250000026' - 'Sales Blanket Agreement' '1250000027' - 'Purchase Blanket Agreement'
- `Public Property Duration() As Double` [R/W] Sets or returns the amount of time scheduled for the activity. Field name: Duration.
  - remarks: The duration value specifies the number of minutes, hours, or days according to the DurationType. The duration value must be equal or greater than 0. In case the start time (days + hours) and end time (days + hours) are specified, then the system recalculates the duration time.
- `Public Property DurationType() As BoDurations` [R/W] Sets or returns a valid value of BoDurations type that specifies the duration type for the activity (minutes, hours, or days). Field name: DurType.
- `Public Property EndDuedate() As Date` [R/W] Sets or returns the due date for completing the activity. Field name: endDate.
  - remarks: The end date must be later than the start date.
- `Public Property EndTime() As Date` [R/W] Sets or returns the end time (hh:mm) of the activity. Field name: ENDTime.
  - remarks: The end time must be later than the start time.
- `Public Property Fax() As String` [R/W] Sets or returns the fax number of the contact person. Field name: Fax. Length: 50 characters.
- `Public Property HandledBy() As Long` [R/W] Sets or returns the name or title of the person who is responsible for entering the activity details. Field name: AttendUser. This is a foreign key to the Users object.
- `Public Property Inactiveflag() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the the activity is inactive. Field name: inactive.
- `Public Property Location() As Long` [R/W] Sets or returns the code for the activity location. Field name: Location. This is a foreign key to the ActivityLocations object.
  - remarks: You can add new locations to the list using the ActivityLocations object.
- `Public Property Notes() As String` [R/W] Sets or returns a memo type string that specifies remarks regarding the activity. Field name: Notes. Length: 16 characters.
- `Public Property ParentobjectId() As Long` [R] Returns the source object ID of the activity: - For Service Call object type: ServiceCallID. - For Sales Opportunity object type: SequentialNo. Field name: parentId.
- `Public Property Parentobjecttype() As String` [R] Returns the source object type of the activity: Sales Opportunity or Service Call. Field name: parentType. Length: 20 characters.
- `Public Property Personalflag() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether the the activity is personal or business. If business, you must set the business partner details (CardCode). Field name: personal.
- `Public Property Phone() As String` [R/W] Sets or returns the phone number of the contact person. Field name: Tel. Length: 50 characters.
- `Public Property PreviousActivity() As Long` [R/W] Sets or returns the previous activity number (ContactCode) related to the current activity. Field name: prevActvty.
- `Public Property Priority() As BoMsgPriorities` [R/W] Sets or returns a valid value of BoMsgPriorities type that specifies the priority of the activity (low, normal, or high). Field name: Priority.
- `Public Property Recontact() As Date` [R/W] Sets or returns the date for the next activity. Field name: Recontact.
- `Public Property Reminder() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not SAP Business One will send a reminder message to the user mailbox ('user' means the current SAP Business One user). Field name: Reminder.
- `Public Property ReminderPeriod() As Double` [R/W] Sets or returns the duration for sending the reminder message. Field name: RemTime.
- `Public Property ReminderType() As BoDurations` [R/W] Sets or returns a valid value of BoDurations type that specifies the duration types: minutes or hours. Field name: RemType.
- `Public Property Room() As String` [R/W] Sets or returns the room where the Activity (Meeting type only) with the business partner takes place. Field name: room. Length: 50 characters.
- `Public Property SalesEmployee() As Long` [R/W] Sets or returns the code of the sales employee who is responsible for the activity. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property StartDate() As Date` [R/W] Sets or returns the start date of the activity. Field name: Recontact.
- `Public Property StartTime() As Date` [R/W] Sets or returns the start time (hh:mm) of the activity. Field name: BeginTime.
- `Public Property State() As String` [R/W] Sets or returns the code of the state where the Activity (Meeting type only) with the business partner takes place. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST).
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Status() As Long` [R/W] Sets or returns the status of the Activity (Task type only) as defined in ActivityStatus object. Field name: status. This is a foreign key to the ActivityStatus object.
- `Public Property Street() As String` [R/W] Sets or returns the street where the Activity (Meeting type only) with the business partner takes place. Field name: street. Length: 100 characters.
- `Public Property Subject() As String` [R/W] Sets or returns the subject of the activity. Field name: CntctSbjct.
- `Public Property Tentativeflag() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the activity is tentative. Field name: tentative.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a new activity with a business partner.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ContactCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ContactCode`: Specifies the identification key of the activity (see ContactCode property).
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

# ContractTemplates (Object)

ContractTemplates is a business object that represents the contract templates in the Service module. This object enables you to: - Add a contract template. - Retrieve a contract template by its key. - Update a contract template. - Remove a contract template. - Save the object in XML format. Source table: OCTT.

**Remarks:** Mandatory field in SAP Business One: TemplateName. To display the form in the application: - Select Administration --> Setup --> Service --> Contract Templates.

## Properties (42)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ContractType() As BoContractTypes` [R/W] Sets or returns a valid value of BoContractTypes that specifies the service contract types for the contract template. Field name: CntrctType.
- `Public Property Description() As String` [R/W] Sets or returns the description of the contract template. Field name: Remark. Length: 16 characters.
- `Public Property DurationOfCoverage() As Long` [R/W] Sets or returns the duration of the service contract coverage in the contract template. Field name: Duration.
- `Public Property FridayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Fridays to the contract template coverage. Field name: FriEnabled.
- `Public Property FridayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Fridays. Field name: FriEnd.
- `Public Property FridayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Fridays. Field name: FriStart.
- `Public Property IncludeHolidays() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include holidays to the contract template coverage. Field name: InclHldays.
- `Public Property IncludeLabor() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include technician's work to the contract template coverage. Field name: InclWork.
- `Public Property IncludeParts() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include replacement parts (items) to the contract template coverage. Field name: InclParts.
- `Public Property IncludeTravel() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include travel to the contract template coverage. Field name: InclTravel.
- `Public Property MondayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Mondays to the contract template coverage. Field name: MonEnabled.
- `Public Property MondayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Mondays. Field name: MonEnd.
- `Public Property MondayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Mondays. Field name: MonStart.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks for the contract template. Field name: Descriptio. Length: 64,000 characters.
- `Public Property RemindBeforeRenewal() As Long` [R/W] Sets or returns the number of days, weeks, or months for the alert to appear prior to the termination of the contract. To enable this reminder, set the TemplateIsRenewal property to tYES. Field name: Renewal.
- `Public Property RemindUnit() As BoRemindUnits` [R/W] Sets or returns a valid value of BoRemindUnits type that specifies the units (days, weeks, or months) for the RemindBeforeRenewal property. Field name: RemindUnit.
- `Public Property ResolutionTime() As Long` [R/W] Sets or returns the maximum time, in hours or days, to resolve the service call. Field name: ResponsVal.
- `Public Property ResolutionUnit() As BoResolutionUnits` [R/W] Sets or returns a valid value of BoResolutionUnits type that specifies the units, hours or days, for the ResolutionTime property. Field name: ResponsUnt.
- `Public Property ResponseUnit() As BoResponseUnit` [R/W] Sets or returns a valid value of BoResponseUnit type that specifies the units, hours or days, for the ResponseValue property. Field name: ResponseU.
- `Public Property ResponseValue() As Long` [R/W] Sets or returns the maximum time, in hours or days, to respond to a service call. Field name: ResponseV.
- `Public Property SaturdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Saturdays to the contract template coverage. Field name: SatEnabled.
- `Public Property SaturdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Saturdays. Field name: SatEnd.
- `Public Property SaturdayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Saturdays. Field name: SatStart.
- `Public Property SundayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Sundays to the contract template coverage. Field name: SunEnabled.
- `Public Property SundayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Sundays. Field name: SunEnd.
- `Public Property SundayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Sundays. Field name: SunStrart.
- `Public Property TemplateIsDeleted() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the contract template is expired. Field name: TmpltName.
- `Public Property TemplateIsRenewal() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to renew the service contract. Field name: Renewal.
- `Public Property TemplateName() As String` [R/W] Sets or returns the name for the contract template. Field name: TmpltName. Mandatory field in SAP Business One. Length: 20 characters.
- `Public Property ThursdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Thursdays to the contract template coverage. Field name: ThuEnabled.
- `Public Property ThursdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Thursdays. Field name: ThuEnd.
- `Public Property ThursdayStart() As Date` [R/W] Sets or returns the beginning working hour of the company on Thursdays. Field name: ThuStart.
- `Public Property TuesdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Tuesdays to the contract template coverage. Field name: ThuEnabled.
- `Public Property TuesdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Tuesdays. Field name: ThuEnd.
- `Public Property TuesdayStart() As Date` [R/W] Sets or returns the beginning working hour of the company on Tuesdays. Field name: ThuStart.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WednesdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Wednesdays to the contract template coverage. Field name: WedEnabled.
- `Public Property WednesdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Wednesdays. Field name: WedEnd.
- `Public Property WednesdayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Wednesdays. Field name: WedStart.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal TemplateName As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `TemplateName`: Specifies the template name.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
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

# CostCenterType (Object)

Represents a cost center type. Source table: OCCT.

## Properties (3)
- `Public Property CostCenterTypeCode() As String` [R/W] The code of the cost center type. Field name: CctCode. Length: 8 characters.
- `Public Property CostCenterTypeName() As String` [R/W] The name of the cost center type. Field name: CctName. Length: 30 characters.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

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

# CostCenterTypeParams (Object)

Holds the key of a cost center type. This object is used to pass keys to and retrieve keys from CostCenterTypesService methods. Source table: OCCT.

## Properties (1)
- `Public Property CostCenterTypeCode() As String` [R/W] The key for a specific cost center type. Field name: CctCode.

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

# CostCenterTypes (Collection)

A collection of CostCenterType objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As CostCenterType` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As CostCenterType` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# CostCenterTypesParams (Collection)

A collection of CostCenterTypeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As CostCenterTypeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As CostCenterTypeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# CostCenterTypesService (Object)

A cost center type is for selection by future reports and analyses. The CostCenterTypesService service enables you to add, look up, update, and remove cost center types. Source table: OCCT.

**Remarks:** To define cost center types, from the SAP Business One Main Menu, choose Financials --> Cost Accounting --> Cost Centers, in the Cost Center Type field, select Define New to open the Cost Center Type – Setup window.

## Methods (8)
- `Public Function AddCostCenterType(ByVal pICostCenterType As CostCenterType) As CostCenterTypeParams` Adds a cost center type.
  - param `pICostCenterType`: The data for the new cost center type.
- `Public Sub DeleteCostCenterType(ByVal pICostCenterTypeParams As CostCenterTypeParams)` Deletes an existing cost center type.
  - param `pICostCenterTypeParams`: The key of the cost center type to be deleted.
- `Public Function GetCostCenterType(ByVal pICostCenterTypeParams As CostCenterTypeParams) As CostCenterType` Retrieves a cost center type. The cost center type is specified by its key, which is contained in the CostCenterTypeParams object passed to the method.
  - param `pICostCenterTypeParams`: The key of the cost center type to retrieve.
- `Public Function GetCostCenterTypeList() As CostCenterTypesParams` Returns the CostCenterTypesParams data collection that identify all cost center types.
- `Public Function GetDataInterface(ByVal enumMSDI As CostCenterTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the CostCenterTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CostCenterTypesServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Sub UpdateCostCenterType(ByVal pICostCenterType As CostCenterType)` Updates an existing cost center type. The data for the cost center type, including the key of the cost center type to be updated, is contained in the CostCenterType object passed to the method. To update a cost center type, you must first retrieve it using the GetCostCenterType method.
  - param `pICostCenterType`: The data for the cost center type to be updated. The CostCenterType object must contain the key of the object to be updated.

# CostElement (Object)

CostElement Class

## Properties (3)
- `Public Property Code() As String` [R/W] property Code
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

# CostElementParams (Object)

CostElementParams Class

## Properties (2)
- `Public Property Code() As String` [R/W] property Code
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

# CostElementService (Object)

CostElementService Class

## Methods (8)
- `Public Function AddCostElement(ByVal pICostElement As CostElement) As CostElementParams` AddCostElement
  - param `pICostElement`: 
- `Public Sub DeleteCostElement(ByVal pICostElementParams As CostElementParams)` DeleteCostElement
  - param `pICostElementParams`: 
- `Public Function GetCostElement(ByVal pICostElementParams As CostElementParams) As CostElement` GetCostElement
  - param `pICostElementParams`: 
- `Public Function GetCostElementList() As CostElementsParams` GetCostElementList
- `Public Function GetDataInterface(ByVal enumMSDI As CostElementServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CostElementServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub UpdateCostElement(ByVal pICostElement As CostElement)` UpdateCostElement
  - param `pICostElement`: 

# CostElementsParams (Collection)

CostElementsParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As CostElementParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As CostElementParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# CountriesParams (Collection)

A data collection of CountryParams identification properties.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of instances in the collection.

## Methods (5)
- `Public Function Add() As CountryParams` Adds a new CountryParams instance.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As CountryParams` Returns a CountryParams instance by a specified index.
  - param `vtIndex`: Specifies the index of the CountryParams instance to retrieve.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# CountriesService (Object)

The CountriesService manages the setting of each country in SAP Business One. For example, country code, country name and address format. Source table: OCRY.

**Remarks:** To access countries in the application: Choose Administration > Setup > Business Partners > Countries/Regions.

**Example:**
- C# example (from SAP's help):
  ```csharp
  CompanyService cmpService = oCmpy.GetCompanyService();
  Country cty = (Country)countryService.GetDataInterface(CountriesServiceDataInterfaces.csCountry);
  cty.Code = "XP";
  cty.Name = "XP Name";
  cty.ISOAlpha2Code = "XC";
  cty.ISOAlpha3Code = "XCC";
  cty.ISONumeric = "002";
  CountryParams cp = countryService.AddCountry(cty);
  ```

## Methods (8)
- `Public Function AddCountry(ByVal pICountry As Country) As CountryParams` Adds a Country as specified in the Country data structure.
  - param `pICountry`: The data for the new country.
- `Public Sub DeleteCountry(ByVal pICountryParams As CountryParams)` Deletes the country as specified in CountryParams object.
  - param `pICountryParams`: CountryParams
- `Public Function GetCountry(ByVal pICountryParams As CountryParams) As Country` Returns an instance of the Country data structure.
  - param `pICountryParams`: CountryParams
- `Public Function GetCountryList() As CountriesParams` Returns a collection of CountryParams.
- `Public Function GetDataInterface(ByVal enumMSDI As CountriesServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CountriesServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: 
- `Public Sub UpdateCountry(ByVal pICountry As Country)` Update the specified Country with the updated data.
  - param `pICountry`: The data for the country to be updated.

# Country (Object)

A data structure object holding properties for the CountriesService object. Source table: OCRY.

## Properties (19)
- `Public Property AddressFormat() As Long` [R/W] Sets or returns the postal address format used by the country. The postal address format must be already presented in the Address Formats table (foreign key to OADF). Field name: AddrFormat.
- `Public Property BankAccountDigits() As Long` [R/W] Sets or returns the number of digits for the bank account number. Used for bank account validation. If greater than zero, it determines how many digits or characters has a valid bank account number for the specific country. If zero, the number of digits is not validated for bank account numbers for the specific country. Field name: BnkActDgts.
- `Public Property BankBranchDigits() As Long` [R/W] Sets or returns the number of digits for the bank branch number. Used for bank account validation. If greater than zero, it determines how many digits or characters has a valid bank branch number for the specific country. If zero, the number of digits is not validated for bank branch numbers for the specific country. Field name: BnkBchDgts.
- `Public Property BankCodeDigits() As Long` [R/W] Sets or returns the number of digits for the bank code. Used for bank account validation. If greater than zero, it determines how many digits or characters has a valid bank branch number for the specific country. If zero, the number of digits is not validated for bank branch numbers for the specific country. Field name: BnkCodDgts.
- `Public Property BankControlKeyDigits() As Long` [R/W] Sets or returns the number of digits for the bank control key. Used for bank account validation. If greater than zero, it determines how many digits or characters has a valid bank control key for the specific country. If zero, the number of digits is not validated for bank control key numbers for the specific country. Field name: BnkCtKDgts.
- `Public Property Blacklisted() As BoYesNoEnum` [R/W] property Blacklisted
- `Public Property Code() As String` [R/W] Sets or returns the country code. Field name: code. Character length: 3.
- `Public Property CodeForReports() As String` [R/W] Sets or returns the country code for the reports. Field name: ReportCode. Character length: 3.
- `Public Property DomesticAccountValidation() As DomesticBankAccountValidationEnum` [R/W] Sets or returns a valid value for special validation of specific countries' bank accounts. If set to one of the valid values, it activates a country specific bank account number validation algorithm. The algorithms usually performs additional validations that are more complex than simple number of digits checks. These algorithms are currently available for certain countries in SAP Business One. If empty or XX, not country specific bank account number validation is performed.
- `Public Property EAEU() As BoYesNoEnum` [R/W] property EAEU
- `Public Property EU() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether or not the country is a member of the European Union.
- `Public Property IbanValidation() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether or not to perform IBAN validation for the specified country.
- `Public Property ISOAlpha2Code() As String` [R/W] 2 character ISO country code. Field name: ISO2Code. Length: 2.
- `Public Property ISOAlpha3Code() As String` [R/W] 3 character ISO country code. Field name: ISO3Code. Length: 3.
- `Public Property ISONumeric() As String` [R/W] 3 numeric ISO country code. Field name: ISONumeric. Length: 3.
- `Public Property Name() As String` [R/W] Sets or returns the name of the country. Field name: Name. Character length: 100.
- `Public Property NumberOfDigitsForTaxID() As Long` [R/W] Sets or returns the number of digits of a valid Tax ID in the specified country. Field name: TaxIdDigts.
- `Public Property UICCountryCode() As String` [R/W] UIC country code. Field name: UICCode. Length: 3.
- `Public Property UserFields() As Fields` [R] Get User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data. Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# CountryParams (Object)

This object holds identification properties for the CountriesService object. Source table: OCRY.

## Properties (2)
- `Public Property Code() As String` [R/W] Sets or returns the country code. Field name: code. Character length: 3.
- `Public Property Name() As String` [R] Returns the name of the country. Field name: Name. Character length: 100.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data. Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path. Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# CreditCardPayments (Object)

The CreditCardPayments object enables to define dates for incoming payments from the credit card company. Source table: OCDT.

**Remarks:** Mandatory fields in SAP Business One: DueDateCode. To display the form in the application: - Select Administration --> Setup --> Banking --> Credit Card Payment.

## Properties (23)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DueDateCode() As String` [R/W] Sets or returns the code of the credit card due date payments. Field name: Code. Mandatory property. Length: 8 characters.
- `Public Property DueDateName() As String` [R/W] Sets or returns the name of the credit card due date payments. Field name: Name. Length: 30 characters.
- `Public Property DueDatesType() As DueDateTypesEnum` [R/W] Determines whether the payment due dates are based on ddtAfterTimePeriod (after number of days and months) or ddtByDates (voucher date of receipt). Field name: TERM_TYPE.
  - remarks: If you set ddtAfterTimePeriod (default), then you must set the PaymentAfterDays (PaymentAfterMonths is not mandatory). If you set ddtByDates, then you must set the due dates for payment from day 1 to day 31 of the month. You can split the month period to maximum four periods. The payment day must be within the period. For example: Voucher Date of Receipt Payment On Day FromDay1 = 1, ToDay1 = 7, PaymentDate1 = 10, (NoofMonths1 is not mandatory). FromDay2 = 8, ToDay2 = 15, PaymentDate2 = 20, (NoofMonths2 is not mandatory). FromDay3 = 16, ToDay3 = 23, PaymentDate3 = 25, (NoofMonths3 is not mandatory). FromDay4 = 24, ToDay4 = 31, PaymentDate4 = 30, (NoofMonths4 is not mandatory).
- `Public Property FromDay1() As Long` [R/W] Sets or returns the beginning day of the first period of voucher receipt. Field name: Day_From1.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property FromDay2() As Long` [R/W] Sets or returns the begining day of the second period of voucher receipt. Field name: Day_From2.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property FromDay3() As Long` [R/W] Sets or returns the begining day of the third period of voucher receipt. Field name: Day_From3.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property FromDay4() As Long` [R/W] Sets or returns the begining day of the fourth period of voucher receipt. Field name: Day_From4.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property NoOfMonths1() As Long` [R/W] Sets or returns the number of months to add to PaymentDay1. Field name: Pay_Month1.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property NoOfMonths2() As Long` [R/W] Sets or returns the number of months to add to PaymentDay2. Field name: Pay_Month2.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property NoOfMonths3() As Long` [R/W] Sets or returns the number of months to add to PaymentDay3. Field name: Pay_Month3.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property NoOfMonths4() As Long` [R/W] Sets or returns the number of months to add to PaymentDay4. Field name: Pay_Month4.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property PaymentAfterDays() As Long` [R/W] Sets or returns the number of days for payment after the voucher receipt. Field name: After_Days.
  - remarks: Applicable when DueDatesType is set to ddtAfterTimePeriod.
- `Public Property PaymentAfterMonths() As Long` [R/W] Sets or returns the number of months to add to PaymentAfterDays. Field name: After_Mnth.
  - remarks: Applicable when DueDatesType is set to ddtAfterTimePeriod.
- `Public Property PaymentDay1() As Long` [R/W] Sets or returns the payment day in the first payment period. For example, if the first payment period is from day 1 to day 7, the payment day can be 1 - 7. Field name: Pay_Day1.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property PaymentDay2() As Long` [R/W] Sets or returns the payment day in the second payment period. For example, if the first payment period is from day 8 to day 15, the payment day can be 8 - 15. Field name: Pay_Day2.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property PaymentDay3() As Long` [R/W] Sets or returns the payment day in the third payment period. Field name: Pay_Day3. For example, if the first payment period is from day 16 to day 24, the payment day can be 16 - 24.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property PaymentDay4() As Long` [R/W] Sets or returns the payment day in the forth payment period. Field name: Pay_Day4. For example, if the first payment period is from day 25 to day 31, the payment day can be 25 - 31.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property ToDay1() As Long` [R/W] Sets or returns the ending day of the first period of voucher receipt. Field name: Day_To1.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property ToDay2() As Long` [R/W] Sets or returns the ending day of the second period of voucher receipt. Field name: Day_To2.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property ToDay3() As Long` [R/W] Sets or returns the ending day of the third period of voucher receipt. Field name: Day_To3.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property ToDay4() As Long` [R/W] Sets or returns the ending day of the fourth period of voucher receipt. Field name: Day_To4.
  - remarks: Applicable when DueDatesType is set to ddtByDates.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a credit card due date payments definition.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrCode`: DueDateCode.
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

# CreditCards (Object)

The CreditCards object enables to define credit cards that the company can use for incoming and outgoing payments. Source table: OCRC.

**Remarks:** Mandatory fields in SAP Business One: CreditCardName and GLAccount. To display the form in the application: - Select Administration --> Setup --> Banking --> Credit Cards.

## Properties (8)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CompanyID() As String` [R/W] Sets or returns the company number at the credit card company. Field name: CompanyId. Length: 20 characters.
- `Public Property CountryCode() As String` [R/W] property CountryCode
- `Public Property CreditCardCode() As Long` [R] Returns the credit card code as assigned by the application when defining a new credit card. Field name: CreditCard.
- `Public Property CreditCardName() As String` [R/W] Sets or returns the credit card name (credit card company). Field name: CardName. Mandatory property. Length: 30 characters.
- `Public Property GLAccount() As String` [R/W] Sets or returns the G/L account (from the ChartOfAccounts object) assigned to transactions made with the credit card. Field name: AcctCode. Mandatory property. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property Telephone() As String` [R/W] Sets or returns the phone number of the credit card company. Field name: Phone. Length: 50 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a new credit card definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCardCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCardCode`: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
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

# CreditLine (Object)

Represents the deposits for credit card vouchers. Source table: OCRH.

## Properties (12)
- `Public Property AbsId() As Long` [R/W] The key of the credit card payment. Field name: AbsId. Length: 11 characters.
- `Public Property CreditCard() As Long` [R] The credit card. Field name: CreditCard.
- `Public Property CreditCurrency() As String` [R] The currency of the credit card voucher. Field name: CreditCurr.
- `Public Property Customer() As String` [R] The code of the customer. Field name: CardCode.
- `Public Property Deposited() As BoYesNoEnum` [R] Indicates whether the credit card voucher is paid or not. Field name: Deposited.
- `Public Property NumOfPayments() As Long` [R] The number of the payment. Field name: NumOfPmnts.
- `Public Property PayDate() As Date` [R] The date of the payment. Field name: PayDate.
- `Public Property PaymentMethodCode() As Long` [R] The code of the payment method. Field name: CrTypeCode.
- `Public Property Reference() As String` [R] The transaction reference. Field name: TransRef.
- `Public Property Total() As Double` [R] The amount of the credit card payment. Field name: CreditSum.
- `Public Property Transferred() As BoYesNoEnum` [R] Indicates whether the deposit of the credit card voucher is transferred to the next year or not. Field name: Transfered.
- `Public Property VoucherNumber() As String` [R] The number of the credit card voucher. Field name: VoucherNum.

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

# CreditLineParams (Object)

Holds the key of a credit card payment. This object is used to pass keys to and retrieve keys from CreditLinesService methods.

## Properties (1)
- `Public Property AbsId() As Long` [R/W] The key of the credit card payment. Field name: AbsId. Length: 11 characters.

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

# CreditLines (Collection)

A data collection of CreditLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As CreditLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As CreditLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# CreditLinesParams (Collection)

A data collection of CreditLineParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As CreditLineParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As CreditLineParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# CreditLinesService (Object)

The CreditLinesService service enables you to get deposits for credit card vouchers. Source table: OCRH.

**Remarks:** To view details on a deposited credit card voucher, from SAP Business One, choose Banking --> Deposits --> Deposit --> Credit Card.

## Methods (5)
- `Public Function GetCreditLine(ByVal pICreditLineParams As CreditLineParams) As CreditLine` Retrieves a deposit for a credit card voucher. The credit card voucher is specified by its key, which is contained in the CreditLineParams object passed to the method.
  - param `pICreditLineParams`: The key of the credit card voucher to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As CreditLinesServiceDataInterfaces) As Object` Creates an empty data structure for use with the CreditLinesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CreditLinesServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetValidCreditLineList() As CreditLinesParams` Returns the CreditLinesParams data collection that identify all deposits of credit card vouchers.

# CreditPaymentMethods (Object)

The CreditPaymentMethods object enables to define payment methods by credit cards. Source table: OCRP.

**Remarks:** The methods for credit card payments are used by the Payments_CreditCards object. Mandatory field in SAP Business One: Name. To display the form in the application: - Select Administration --> Setup --> Banking --> Credit Card Payment Methods.

## Properties (10)
- `Public Property AssignedtoCreditCard() As Long` [R/W] Sets or returns the foreign key of the credit card assigned to the payment method. Field name: CreditCard. This is a foreign key to the CreditCards object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property InstallmentPaymentsPossible() As InstallmentPaymentsPossiblityEnum` [R/W] Sets or returns a valid value that defines the options for installments available for the payment method. Field name: InstalMent.
- `Public Property MaxQtyWithoutApproval() As Double` [R/W] Sets or returns the maximum amount of incoming and outgoing payments without the approval of the credit card company. Field name: MaxValid.
  - remarks: The system issues a warning if the value of credit card transactions does not match the maximum amount with approval.
- `Public Property MinimumCreditAmount() As Double` [R/W] Sets or returns the minimum amount for credit vouchers. Field name: MinCredit.
  - remarks: The system issues a warning if the value of credit card transactions does not match the minimum amount of credit vouchers.
- `Public Property MinimumPaymentAmount() As Double` [R/W] Sets or returns the minimum amount for incoming and outgoing payments. Field name: MinToPay.
  - remarks: The system issues a warning if the value of credit card transactions does not match the minimum amount of payment.
- `Public Property Name() As String` [R/W] Sets or returns the name of the credit payment method. Field name: CrTypeName. Mandatory property. Length: 30 characters.
  - remarks: The Name clearly identifies the payment method in documents (such as Visa Regular).
- `Public Property PaymentCode() As String` [R/W] Sets or returns the foreign key of the credit card payment due dates. Field name: DueTerms. This is a foreign key to the CreditCardPayments object.
- `Public Property PaymentMethodCode() As Long` [R] Returns the payment method code as assigned by the system when adding the payment method definition. Field name: CrTypeCode.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a credit card payment method.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: PaymentMethodCode.
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

# Currencies (Object)

Currencies is a business object that represents the currency codes in the Administration module. This object enables you to: - Add a currency code. - Retrieve a currency code by its key. - Update a currency code. - Remove a currency code. - Save the object in XML format. Source table: OCRN.

**Remarks:** Mandatory fields in SAP Business One: Code and DocumentsCode. To display the form in the application: - Select Administration --> Setup --> Financials --> Currencies.

## Properties (20)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R/W] Sets or returns the currency code, for example, USD, EUR. Field name: CurrCode. Mandatory property. Length: 3 characters.
- `Public Property Decimals() As CurrenciesDecimalsEnum` [R/W] Sets or returns a value that specifies the decimal rounding type for the currency.
  - remarks: The settings affect the fields Price, Line Total, and Document Total in marketing documents.
- `Public Property DocumentsCode() As String` [R/W] Sets or returns the currency internatioanl code on printed documents (e.g. $, ?). Field name: DocCurrCod. Mandatory property. Length: 3 characters.
- `Public Property EnglishHundredthName() As String` [R/W] Sets or returns the English singular name of the decimal unit (e.g. Cent). Field name: F100Name. Length: 20 characters.
- `Public Property EnglishName() As String` [R/W] Sets or returns the English singular name of the currency (e.g. Canadian Dollar). Field name: FrgnName. Length: 20 characters.
- `Public Property HundredthName() As String` [R/W] Sets or returns the singular name of the decimal unit (e.g. Cent) on printed checks. Field name: Chk100Name. Length: 20 characters.
- `Public Property InternationalDescription() As String` [R/W] Sets or returns the international singular name of the currency on printed chacks (e.g. Canadian Dollar). Field name: ChkName. Length: 20 characters.
- `Public Property MaxIncomingAmtDiff() As Double` [R/W] property MaxIncomingAmtDiff
- `Public Property MaxIncomingAmtDiffPercent() As Double` [R/W] property MaxIncomingAmtDiffPercent
- `Public Property MaxOutgoingAmtDiff() As Double` [R/W] property MaxOutgoingAmtDiff
- `Public Property MaxOutgoingAmtDiffPercent() As Double` [R/W] property MaxOutgoingAmtDiffPercent
- `Public Property Name() As String` [R/W] Sets or returns the currency name (e.g. Canadian Dollar). Field name: CurrName. Length: 20 characters.
- `Public Property PluralEnglishHundredthName() As String` [R/W] Sets or returns the English plural name of the decimal unit (e.g. Cents). Applicable for cluster B only. Length: 20 characters.
- `Public Property PluralEnglishName() As String` [R/W] Sets or returns the English plural name of the currency (e.g. Canadian Dollars). Applicable for cluster B only. Length: 20 characters.
- `Public Property PluralHundredthName() As String` [R/W] Sets or returns the plural name of the decimal unit (e.g. Cents) on printed checks. Applicable for cluster B only. Length: 20 characters.
- `Public Property PluralInternationalDescription() As String` [R/W] Sets or returns the international plural name of the currency on printed chacks (e.g. Canadian Dollar). Applicable for cluster B only. Length: 20 characters.
- `Public Property Rounding() As RoundingSysEnum` [R/W] Sets or returns a valid value that determines the rounding method.
- `Public Property RoundingInPayment() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to round the total in payments.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a new currency rate.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Currency As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Currency`: Specifies the currency code (see Code property).
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

# CurrencyRestrictions (Object)

The CurrencyRestrictions is a child object of the WizardPaymentMethods object. This object enables to allow or restrict currencies in the payment method. Source table: PYM1.

**Remarks:** To display the form in the application: - Select Administration -->Setup -->Banking -->Payment Methods. - Click the [...] button near the Currency Restriction field. The CurrencyRestrictions object is applicable when the CurrencyRestriction property of the WizardPaymentMethods object is set to tYES.

## Properties (6)
- `Public Property Choose() As BoYesNoEnum` [R/W] Determines whether to allow (Y) or to restrict (N) the currency in the payment method. Field name: Choose.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property CurrencyCode() As String` [R/W] Sets or returns the currency code as defined through the Currencies object. Field name: CurrCode. This is a foreign key to the Currencies object. Length: 3 characters.
- `Public Property CurrencyName() As String` [R] Returns the currency name as defined through the Currencies object. Field name: CurrName. Length: 20 characters.
- `Public Property PaymentMethodCode() As String` [R] Returns the payment method code as defined in the WizardPaymentMethods object. Field name: PymCode. This is a foreign key to the WizardPaymentMethods object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# CustomerEquipmentCards (Object)

CustomerEquipmentCards is a business object that represents the customer equipment cards in the Services module. This object enables you to: - Add a customer equipment card. - Retrieve a customer equipment card by its key. - Update a customer equipment card. - Remove a customer equipment card. - Save the object in XML format. Source table: OINS.

**Remarks:** Mandatory fields in SAP Business One: ManufacturerSerialNum or InternalSerialNum (according to the definition of Unique Number in the General Settings in SAP Business One - SriUniqFld field in OADM table), ItemCode, and CustomerCode. To display the form in the application: - Select Service --> Customer Equipment Card.

## Properties (37)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the Attachment File as assigned by SAP Business One when adding an attachment file. Field name: AtcEntry. This is a foreign key to the Territories object. Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Block() As String` [R/W] Sets or returns the block name in the address where the service is provided. Field name: block. Length: 100 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the additional address details, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters.
- `Public Property BusinessPartners() As CustomerEquipmentCards_BusinessPartners` [R] property BusinessPartners
- `Public Property City() As String` [R/W] Sets or returns the city name in the address where the service is provided. Field name: city. Length: 100 characters.
- `Public Property ContactEmployeeCode() As Long` [R/W] Sets or returns the code of the contact person. Field name: contactCod. This is a foreign key to the ContactEmployees object.
- `Public Property ContactPhone() As String` [R] Returns the phone number of the contact person. Field name: cntctPhone. Length: 50 characters.
- `Public Property CountryCode() As String` [R/W] Sets or returns the country code in the address where the service is provided. Field name: country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county name in the address where the service is provided. Field name: county. Length: 100 characters.
- `Public Property CustomerCode() As String` [R/W] Sets or returns the customer code. Field name: customer. Mandatory field in SAP Business One. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CustomerName() As String` [R/W] Sets or returns the customer name. Field name: custmrName. Length: 100 characters.
- `Public Property DefaultTechnician() As Long` [R/W] Sets or returns the default technician for this customer equipment card as defined in the technicians table. Field name: technician. This is a foreign key to the EmployeesInfo object.
- `Public Property Defaultterritory() As Long` [R/W] Sets or returns the default territory for this customer equipment card as defined in the territories table. Field name: territory. This is a foreign key to the Territories object.
- `Public Property DeliveryCode() As Long` [R/W] Sets or returns the code of the delivery note document. Field name: delivery. This is a foreign key to the Documents object.
- `Public Property DeliveryDate() As Date` [R] Returns the delivery date of the item. Field name: dlvryDate.
- `Public Property DeliveryNumber() As Long` [R] Returns the number of the delivery note document. Field name: deliveryNo.
- `Public Property DirectCustomerCode() As String` [R/W] Sets or returns the code of the customer that bought the item. Field name: directCsmr. Length: 15 characters.
- `Public Property DirectCustomerName() As String` [R/W] Sets or returns the name of the customer that bought the item. Field name: custmrName. Length: 100 characters.
- `Public Property EquipmentCardNum() As Long` [R] Returns the equipment card ID. Field name: insID.
- `Public Property InstallLocation() As String` [R/W] Sets or returns the location where the item is installed. Field name: instLction. Length: 254 characters.
- `Public Property InternalSerialNum() As String` [R/W] Sets or returns the unique internal serial number of the item. Field name: internalSN. Mandatory field in SAP Business One in one of the following cases: - If you do not set the ManufacturerSerialNum property. - From version 2004, if the definition of Unique Number in General Settings in SAP Business One is Serial Number. Length: 32 characters.
- `Public Property InvoiceCode() As Long` [R/W] Sets or returns the invoice code. Field name: invoice. This is a foreign key to the Documents object.
- `Public Property InvoiceNumber() As Long` [R] Returns the invoice number. Field name: invoiceNum.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code. Field name: itemCode. Mandatory field in SAP Business One. Length: 20 characters.Items
- `Public Property ItemDescription() As String` [R/W] Sets or returns the item description. Field name: itemName. Length: 100 characters.
- `Public Property ManufacturerSerialNum() As String` [R/W] Sets or returns the unique manufacturer serial number of the item. Field name: manufSN. Mandatory field in SAP Business One in one of the following cases: - If you do not set the InternalSerialNum property. - From version 2004, if the definition of Unique Number in General Settings in SAP Business One is Man. Serial No. Length: 32 characters.
- `Public Property ReplacedBySN() As Long` [R/W] Sets or returns the S/N of the replacement equipment (Replaced By S/N) that replaced the equipment of the Replace S/N equipment card. This enables concatenation of replacement equipments. Field name: repByIns. This is a foreign key to the CustomerEquipmentCards object.
- `Public Property ReplaceSN() As Long` [R/W] Sets or returns the S/N of the replacement equipment (Replace S/N) that replaced the equipment of the current equipment card. Field name: replcIns. This is a foreign key to the CustomerEquipmentCards object.
- `Public Property ServiceBPType() As BoEquipmentBPType` [R/W] Sets or returns the service BP type, whether your company provides support services to its customers, or receives support services from your vendors. Field name: BPType.
- `Public Property StateCode() As String` [R/W] Sets or returns the state code where the service is provided. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property StatusOfSerialNumber() As BoSerialNumberStatus` [R/W] Sets or returns a valid value of BoSerialNumberStatus type that specifies the current location of the equipment, for example at the customer premises, in the lab, and so on. Field name: status.
- `Public Property Street() As String` [R/W] Sets or returns the street name in the address where the service is provided. Field name: Street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] Sets or returns the street number in the address where the service is provided. Field name: Street No. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code in the address where the service is provided. Field name: zip. Length: 20 characters.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal EquipmentCardNum As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `EquipmentCardNum`: Specifies the equipment card number in the database.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
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

# CustomerEquipmentCards_BusinessPartners (Object)

Items_PreferredVendors Class

## Properties (3)
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property Count() As Long` [R] property Count
- `Public Property UserFields() As UserFields` [R] Get User Fields

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# CustomsDeclaration (Object)

A data structure related with the CustomsDeclarationService holding the information about a Cargo Customs Declaration (CCD). Source table: OCCD.

## Properties (10)
- `Public Property CCDNum() As String` [R/W] Sets or returns the unique CCD number. Field name: CCDNum.
- `Public Property CustomsBroker() As String` [R/W] Sets or returns the customs broker (a valid business partner code from the OCRD table). Field name: CustBroker.
- `Public Property CustomsTerminal() As String` [R/W] Sets or returns the customs terminal (a valid business partner code from the OCRD table). Field name: CustTerm.
- `Public Property Date() As Date` [R/W] Sets or returns the date of declaration. Field name: Date.
- `Public Property DocDate() As Date` [R/W] Sets or returns the import or export document date. Field name: DocDate.
- `Public Property DocNum() As String` [R/W] Sets or returns the import or export document number. Field name: DocNum.
- `Public Property PaymentKey() As String` [R/W] Sets or returns the payment key. Field name: PayKey.
- `Public Property SupplyDate() As Date` [R/W] Sets or returns the supply agreement date. Field name: SupDate.
- `Public Property SupplyNum() As String` [R/W] Sets or returns the supply agreement number. Field name: SupNum.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# CustomsDeclarationParams (Object)

A data structure holding identification properties for the CustomsDeclarationService.

## Properties (1)
- `Public Property CCDNum() As String` [R/W] Sets or returns the unique CCD number.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# CustomsDeclarationService (Object)

The CustomsDeclarationService enables to manage the Cargo Customs Declarations (CCD). The service enables to add, update, get and delete CCDs. Mandatory properties: CCDNum (primary key). Source table: OCCD.

## Methods (7)
- `Public Function AddCustomsDeclaration(ByVal pICustomsDeclaration As CustomsDeclaration) As CustomsDeclarationParams` Defines a new CCD entry.
  - param `pICustomsDeclaration`: The data for the new customs declaration.
- `Public Sub DeleteCustomsDeclaration(ByVal pICustomsDeclarationParams As CustomsDeclarationParams)` Deletes an existing CCD entry specified in CustomsDeclarationParams.
  - param `pICustomsDeclarationParams`: The key of the customs declaration to be deleted.
- `Public Function GetCustomsDeclaration(ByVal pICustomsDeclarationParams As CustomsDeclarationParams) As CustomsDeclaration` Retrieves information about an existing CCD entry specified in CustomsDeclarationParams.
  - param `pICustomsDeclarationParams`: The key of the customs declaration to be retrieved.
- `Public Function GetDataInterface(ByVal enumMSDI As CustomsDeclarationServiceDataInterfaces) As Object` Creates an empty data interface. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CustomsDeclarationServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface from XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Retrieves the Data Interface from XML string.
  - param `bstrXMLString`: 
- `Public Sub UpdateCustomsDeclaration(ByVal pICustomsDeclaration As CustomsDeclaration)` Updates an existing CCD entry.
  - param `pICustomsDeclaration`: The data for the customs declaration to be updated.
