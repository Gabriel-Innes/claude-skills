<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DistributionRulesService (Object)

The DistributionRulesService service enables you to add, look up and remove distribution rules for spreading a specific expense, account, journal entry, or other entity among profit centers. To see the list of distribution rules, select Financials --> Cost Accounting --> Distribution Rules. You can also select Financials --> Cost Accounting --> Profit Centers, and then click Open Table to see a list of all profit centers and distribution rules. Source table: OOCR

## Methods (8)
- `Public Function AddDistributionRule(ByVal pIDistributionRule As DistributionRule) As DistributionRuleParams` Adds a distribution rule.
  - param `pIDistributionRule`: The data for the new distribution rule.
  - returns: Contains the key (OcrCode) of the new distribution rule.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oCmpSrv = oCompany.GetCompanyService()

    Dim oDLservice As SAPbobsCOM.DistributionRulesService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.DistributionRulesService)

    Dim oDL As SAPbobsCOM.DistributionRule

    ' Add distribution rule

    oDL = oDLservice.GetDataInterface(SAPbobsCOM.DistributionRulesServiceDataInterfaces.drsDistributionRule)

    oDL.FactorCode = "1"

    oDL.FactorDescription = "Desc 1"

    oDL.InWhichDimension = 1

    oDL.TotalFactor = 40

    oDL.DistributionRuleLines.Add()

    oDL.DistributionRuleLines.Item(0).CenterCode = "1"

    oDL.DistributionRuleLines.Item(0).TotalInCenter = "10"

    oDL.DistributionRuleLines.Add()

    oDL.DistributionRuleLines.Item(1).CenterCode = "2"

    oDL.DistributionRuleLines.Item(1).TotalInCenter = "30"

    Try

        oDLservice.AddDistributionRule(oDL)

    Catch ex As Exception

        MsgBox(ex.Message)

    End Try
    ```
- `Public Sub DeleteDistributionRule(ByVal pIDistributionRuleParams As DistributionRuleParams)` Deletes an existing distribution rule. The distribution rule is specified by its key (OcrCode), which is contained in the DistributionRuleParams object passed to the method.
  - param `pIDistributionRuleParams`: The key of the distribution rule to be deleted.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oCmpSrv = oCompany.GetCompanyService()

    Dim oDLservice As SAPbobsCOM.DistributionRulesService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.DistributionRulesService)

    Dim oDL As SAPbobsCOM.DistributionRule

    Dim oDLParams As SAPbobsCOM.IDistributionRuleParams

    ' Get distribution rule

    oDLParams = oDLservice.GetDataInterface(SAPbobsCOM.DistributionRulesServiceDataInterfaces.drsDistributionRuleParams)

    oDLParams.FactorCode = "1"

    Try

        oDL = oDLservice.GetDistributionRule(oDLParams)

    Catch ex As Exception

        MsgBox(ex.Message)

    End Try

    ' Delete distribution rule

    Try

        oDLservice.DeleteDistributionRule(oDL)

    Catch ex As Exception

        MsgBox(ex.Message)

    End Try
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As DistributionRulesServiceDataInterfaces) As Object` Creates an empty data structure for use with the DistributionRulesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DistributionRulesServiceDataInterfaces.md`
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
- `Public Function GetDistributionRule(ByVal pIDistributionRuleParams As DistributionRuleParams) As DistributionRule` Retrieves a distribution rule. The distribution rule is specified by its key (OcrCode), which is contained in the DistributionRuleParams object passed to the method.
  - param `pIDistributionRuleParams`: The key of the distribution rule to retrieve.
  - returns: The distribution rule with the specified key.
- `Public Function GetDistributionRuleList() As DistributionRulesParams` Retrieves the keys and names of all the distribution rules.
- `Public Sub UpdateDistributionRule(ByVal pIDistributionRule As DistributionRule)` Updates an existing distribution rule. The data for the distribution rule, including the key of the distribution rule to be updated, is contained in the DistributionRule object passed to the method. To update a distribution rule, you must first retrieve it using the GetDistributionRule method.
  - param `pIDistributionRule`: The data for the distribution rule to be updated. The DistributionRule object must contain the key of the object to be updated.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oCmpSrv = oCompany.GetCompanyService()

    Dim oDLservice As SAPbobsCOM.DistributionRulesService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.DistributionRulesService)

    Dim oDL As SAPbobsCOM.DistributionRule

    Dim oDLParams As SAPbobsCOM.IDistributionRuleParams

    ' Get distribution rule

    oDLParams = oDLservice.GetDataInterface(SAPbobsCOM.DistributionRulesServiceDataInterfaces.drsDistributionRuleParams)

    oDLParams.FactorCode = "1"

    Try

        oDL = oDLservice.GetDistributionRule(oDLParams)

    Catch ex As Exception

        MsgBox(ex.Message)

    End Try

    ' Update distribution rule

    oDL = oDLservice.GetDataInterface(SAPbobsCOM.DistributionRulesServiceDataInterfaces.drsDistributionRule)

    oDL.FactorCode = "1"

    oDL.FactorDescription = "Desc 1"

    oDL.InWhichDimension = 1

    oDL.TotalFactor = 40

    oDL.DistributionRuleLines.Add()

    oDL.DistributionRuleLines.Item(0).CenterCode = "1"

    oDL.DistributionRuleLines.Item(0).TotalInCenter = "10"

    oDL.DistributionRuleLines.Add()

    oDL.DistributionRuleLines.Item(1).CenterCode = "2"

    oDL.DistributionRuleLines.Item(1).TotalInCenter = "30"

    Try

        oDLservice.UpdateDistributionRule(oDL)

    Catch ex As Exception

        MsgBox(ex.Message)

    End Try
    ```
