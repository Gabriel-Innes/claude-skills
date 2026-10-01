<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DunningTermsService (Object)

The DunningTermsService service enables you to add, look up and remove dunning terms for defining when to send out dunning terms for delinquent balances. Each business partner can be assigned to one dunning term, which defines when to send dunning letters to that partner. Source table: ODUT

**Remarks:** SAP Business One maintains a template list of up to 10 dunning levels; in the DI API, this list is managed by the DunningLetters object. In the application, a new dunning term automatically contains this list of dunning levels, but the dunning levels in the dunning terms can be changed. In the DI API, if no lines are specified for a new dunning term in the AddDunningTerm method, then the template list of dunning levels is automatically added to the dunning term. To see the list of dunning terms, select Administration --> Setup --> Business partners --> Dunning Terms.

## Methods (8)
- `Public Function AddDunningTerm(ByVal pIDunningTerm As DunningTerm) As DunningTermParams` Adds a dunning term.
  - param `pIDunningTerm`: The data for the new dunning term.
  - returns: Contains the key (TermCode) of the new dunning term.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DunningTermsService dts = globals_Renamed.oCompany.GetCompanyService().GetBusinessService(ServiceTypes.DunningTermsService) as DunningTermsService;
    SAPbobsCOM.DunningTerm dt = dts.GetDataInterface(DunningTermsServiceDataInterfaces.dtsDunningTerm) as SAPbobsCOM.DunningTerm;

    string code = "Code" + DateTime.Now.Minute.ToString() + DateTime.Now.Second.ToString();
    dt.Code = code;
    dt.Name = "myName";
    dt.ApplyHighestLetterTemplate = BoYesNoEnum.tNO;
    dt.CalculateInterestMethod = CalculateInterestMethodEnum.cimOnRemainingAmount;
    dt.DaysInMonth = 28;
    dt.DaysInYear = 350;
    dt.GroupingMethod = GroupingMethodEnum.gmPerBP;
    dt.IncludeInterest = BoYesNoEnum.tYES;
    dt.ExchangeRateSelect = ExchangeRateSelectEnum.ierCurrentRate;
    dt.LetterFee = 12;
    dt.LetterFeeCurrency = "USD";
    dt.MinimumBalance = 13;
    dt.MinimumBalanceCurrency = "CAN";
    dt.YearlyInterestRate = 25;

    SAPbobsCOM.DunningTermLine dtl = dt.DunningTermLines.Add();
    dtl.CalculateInterest = BoYesNoEnum.tYES;
    dtl.Effectiveafter = "12";
    dtl.LetterFee = 20;
    dtl.LetterFeeCurrency = "USD";
    dtl.LetterFormat = dltDunningLetter2;
    dtl.MininumBalance = 14;
    dtl.MininumBalanceCurrency = "USD";

    dtl = dt.DunningTermLines.Add();
    dtl.CalculateInterest = BoYesNoEnum.tYES;
    dtl.Effectiveafter = "15";
    dtl.LetterFee = 20;
    dtl.LetterFeeCurrency = "CAN";
    dtl.LetterFormat = dltDunningLetter3;
    dtl.MininumBalance = 14;
    dtl.MininumBalanceCurrency = "USD";

    try
    {
        DunningTermParams dtp = dts.AddDunningTerm(dt);
    }
    catch(Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
    ```
- `Public Sub DeleteDunningTerm(ByVal pIDunningTermParams As DunningTermParams)` Deletes an existing dunning term. The dunning term is specified by its key (TermCode), which is contained in the DunningTermParams object passed to the method.
  - param `pIDunningTermParams`: The key of the dunning term to be deleted.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DunningTermsService dts = globals_Renamed.oCompany.GetCompanyService().GetBusinessService(ServiceTypes.DunningTermsService) as DunningTermsService;
    SAPbobsCOM.DunningTermParams dtp = dts.GetDataInterface(DunningTermsServiceDataInterfaces.dtsDunningTermParams) as DunningTermParams;
    dtp.Code = "Code5327";

    try
    {
        dts.DeleteDunningTerm(dtp);
    }
    catch (Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As DunningTermsServiceDataInterfaces) As Object` Creates an empty data structure for use with the DunningTermsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DunningTermsServiceDataInterfaces.md`
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
- `Public Function GetDunningTerm(ByVal pIDunningTermParams As DunningTermParams) As DunningTerm` Retrieves a dunning term. The dunning term is specified by its key (TermCode), which is contained in the DunningTermParams object passed to the method.
  - param `pIDunningTermParams`: The key of the dunning term to retrieve.
  - returns: The dunning term with the specified key.
- `Public Function GetDunningTermList() As DunningTermsParams` Retrieves the keys and names of all the dunning terms.
  - C# example (from SAP's help):
    ```csharp
    DunningTermsService dts = globals_Renamed.oCompany.GetCompanyService().GetBusinessService(ServiceTypes.DunningTermsService) as DunningTermsService;
    DunningTermsParams dtps = dts.GetDunningTermList();
    int length = dtps.Count;
    for (int i=0; i<length; i++)
    {
         Console.WriteLine(dtps.Item(i).Code);
    }
    ```
- `Public Sub UpdateDunningTerm(ByVal pIDunningTerm As DunningTerm)` Updates an existing dunning term. The data for the dunning term, including the key of the dunning term to be updated, is contained in the DunningTerm object passed to the method. To update a dunning term, you must first retrieve it using the GetDunningTerm method.
  - param `pIDunningTerm`: The data for the dunning term to be updated. The DunningTerm object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DunningTermsService dts = globals_Renamed.oCompany.GetCompanyService().GetBusinessService(ServiceTypes.DunningTermsService) as DunningTermsService;
    SAPbobsCOM.DunningTermParams dtp = dts.GetDataInterface(DunningTermsServiceDataInterfaces.dtsDunningTermParams) as DunningTermParams;

    dtp.Code = "Code5327";
    SAPbobsCOM.DunningTerm dt = dts.GetDunningTerm(dtp);

    string code;
    string name;
    code = dt.Code;
    name = dt.Name;
    SAPbobsCOM.BoYesNoEnum applyHighestLetter = dt.ApplyHighestLetterTemplate;
    SAPbobsCOM.CalculateInterestMethodEnum calculateInterestMethod = dt.CalculateInterestMethod;
    dt.DaysInMonth = 28;
    dt.DaysInYear = 30;
    SAPbobsCOM.GroupingMethodEnum groupMethod = dt.GroupingMethod;
    SAPbobsCOM.BoYesNoEnum includeInterest = dt.IncludeInterest;
    SAPbobsCOM.ExchangeRateSelectEnum exchangeRateSelect = dt.ExchangeRateSelect;
    double letterFee = dt.LetterFee;
    string currency = dt.LetterFeeCurrency;
    double minBalance = dt.MinimumBalance;
    string minCurrency = dt.MinimumBalanceCurrency;
    double interestRate = dt.YearlyInterestRate;

    int count = dt.DunningTermLines.Count;
    SAPbobsCOM.DunningTermLine dtl = dt.DunningTermLines.Item(0);
    SAPbobsCOM.DunningTermLine dtl2 = dt.DunningTermLines.Item(1);
    dtl2.CalculateInterest = BoYesNoEnum.tNO;

    try
    {
        dts.UpdateDunningTerm(dt);
    }
    catch (Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
    ```
