<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DepositsService (Object)

The DepositsService service enables you to add, look up, update and cancel deposits for: - Cash - Checks - Credit card vouchers For Chile, France, Italy, Portugal, and Spain localizations, you can view deposited bills of exchange (BoE). Source table: ODPS.

**Remarks:** To access the Deposit window from the SAP Business One application, choose Banking --> Deposits --> Deposit.

## Methods (11)
- `Public Function AddDeposit(ByVal pIDeposit As Deposit) As DepositParams` Adds a deposit.
  - param `pIDeposit`: The data for the new deposit.
  - C# example (from SAP's help):
    ```csharp
    //Get company service
    CompanyService companyService = oCompany.GetCompanyService();

    //Get deposit service
    SAPbobsCOM.DepositService dpService = (SAPbobsCOM.DepositService)companyService.GetBusinessService(ServiceTypes.DepositService);

    //Deposit with Cash
    SAPbobsCOM.Deposit dpsAddCash = (SAPbobsCOM.Deposit)dpService.GetDataInterface(DepositServiceDataInterfaces.dsDeposit);
    //Specify the deposit type
    dpsAddCash.DepositType = BoDepositTypeEnum.dtCash;
    //Set deposit currency type
    dpsAddCash.DepositCurrency = "RMB";
    dpsAddCash.AllocationAccount = "100201";
    dpsAddCash.DepositAccount = "100101";
    dpsAddCash.TotalLC = 233.5;
    dpsAddCash.JournalRemarks = "Adding Deposit with Cash";

    //Add the deposit
    SAPbobsCOM.DepositParams dpsParamAddCash = dpService.AddDeposit(dpsAddCash);
    ```
- `Public Sub CancelCheckRow(ByVal pICancelCheckRowParams As CancelCheckRowParams)` Cancels a check that was received as an incoming payment together with the incoming payment document.
  - param `pICancelCheckRowParams`: The key of the check to be canceled.
- `Public Sub CancelCheckRowbyCurrentSystemDate(ByVal pICancelCheckRowParams As CancelCheckRowParams)` CancelCheckRowbyCurrentSystemDate
  - param `pICancelCheckRowParams`: 
- `Public Sub CancelDeposit(ByVal pIDepositParams As DepositParams)` Cancels an existing deposit.
  - param `pIDepositParams`: The key of the deposit to be canceled.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DepositsParams ParamsCancel = (SAPbobsCOM.DepositsParams)dpService.GetDepositList();

    if (ParamsCancel.Count > 0)
     {
         foreach (SAPbobsCOM.DepositParams paramC in ParamsCancel)
         {
             //Get the related deposit object
             SAPbobsCOM.Deposit dpsCancel = dpService.GetDeposit(paramC);

             //Cancel deposit
             dpService.CancelDeposit(paramC);

             //Cancel the first deposit
             break;
         }
     }
    ```
- `Public Sub CancelDepositbyCurrentSystemDate(ByVal pIDepositParams As DepositParams)` CancelDepositbyCurrentSystemDate
  - param `pIDepositParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As DepositsServiceDataInterfaces) As Object` Creates an empty data structure for use with the DepositsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DepositsServiceDataInterfaces.md`
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
- `Public Function GetDeposit(ByVal pIDepositParams As DepositParams) As Deposit` Retrieves a deposit. The deposit is specified by its key, which is contained in the DepositParams object passed to the method.
  - param `pIDepositParams`: The key of the deposit to retrieve.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DepositsParams dpsParamsGet = (SAPbobsCOM.DepositsParams)dpService.GetDepositList();
    if (dpsParamsGet.Count > 0)
    {
        //You can get the "DepositNumber" one by one.
        foreach (SAPbobsCOM.DepositParams dpsParamGet in dpsParamsGet)
        {
            int dpsNumber = dpsParamGet.DepositNumber;
            //Get Deposit
            SAPbobsCOM.Deposit dpsGet = dpService.GetDeposit(dpsParamGet);

           //Any operations as you like.
        }
    }
    ```
- `Public Function GetDepositList() As DepositsParams` Returns the DepositsParams data collection that identify all deposits.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DepositsParams dpsParamsGet = (SAPbobsCOM.DepositsParams)dpService.GetDepositList();
    if (dpsParamsGet.Count > 0)
    {
        //You can get the "DepositNumber" one by one.
        foreach (SAPbobsCOM.DepositParams dpsParamGet in dpsParamsGet)
        {
            int dpsNumber = dpsParamGet.DepositNumber;
            //Get Deposit
            SAPbobsCOM.Deposit dpsGet = dpService.GetDeposit(dpsParamGet);

           //Any operations as you like.
        }
    }
    ```
- `Public Sub UpdateDeposit(ByVal pIDeposit As Deposit)` Updates an existing deposit. The data for the deposit, including the key of the deposit to be updated, is contained in the Deposit object passed to the method. To update a deposit, you must first retrieve it using the GetDeposit method.
  - param `pIDeposit`: The data for the deposit to be updated. The Deposit object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    //Get an existing deposit object
    SAPbobsCOM.DepositsParams dpsParamsGetForUpdate = (SAPbobsCOM.DepositsParams)dpService.GetDepositList();

    if (dpsParamsGetForUpdate.Count > 0)
    {
        foreach (SAPbobsCOM.DepositParams dpsParamGetForUpdate in dpsParamsGetForUpdate)
        {
            //Get deposit
            SAPbobsCOM.Deposit dpsGetForUpdate = dpService.GetDeposit(dpsParamGetForUpdate);

            //Update deposit journal remarks
            dpsGetForUpdate.JournalRemarks = "Updating existing deposit";

            //Update the deposit
            dpService.UpdateDeposit(dpsGetForUpdate);

            //Change the first deposit only
            break;
         }
    }
    ```
