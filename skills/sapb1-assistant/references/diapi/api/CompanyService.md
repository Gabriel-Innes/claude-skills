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
  - enum: `../enums/ServiceTypes.md`
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
  - enum: `../enums/CompanyServiceDataInterfaces.md`
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
  - enum: `../enums/ServiceTypes.md`
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
