<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExternalReconciliationsService (Object)

The ExternalReconciliationsService service enables you to add, look up, and cancel external reconciliations. Source table: OMTH.

**Remarks:** To perform external reconciliations, choose Banking --> Bank Statements and External Reconciliations --> Reconciliation. In the External Reconciliation – Selection Criteria window, select either the Manual or Automatic radio button, specify the selection criteria, and choose the Reconcile button.

**Example:**
- C# example (from SAP's help):
  ```csharp
  //Get business service.

  SAPbobsCOM.CompanyService oCompanyService = Cmpy.GetCompanyService();

  SAPbobsCOM.ExternalReconciliationsService ExtReconSvc =
                          (SAPbobsCOM.ExternalReconciliationsService)oCompanyService.GetBusinessService
  (SAPbobsCOM.ServiceTypes.ExternalReconciliationsService);

  SAPbobsCOM.ExternalReconciliation ExtReconciliation =
                          (SAPbobsCOM.ExternalReconciliation)ExtReconSvc.GetDataInterface(SAPbobsCOM.ExternalReconciliationsServiceDataInterfaces.ersExternalReconciliations);

  ExtReconciliation.ReconciliationAccountType = SAPbobsCOM.ReconciliationAccountTypeEnum.rat_BusinessPartner; // default is GL Account

  //Reconcile object.
  SAPbobsCOM. ReconciliationJournalEntryLine jeLine1 = (SAPbobsCOM. ReconciliationJournalEntryLine)ExtReconciliation.ReconciliationJournalEntryLines.Add();
  jeLine1.TransactionNumber = "1";
  jeLine1.LineNumber = 1;

  SAPbobsCOM.ReconciliationJournalEntryLine jeLine2 = (SAPbobsCOM. ReconciliationJournalEntryLine)ExtReconciliation.ReconciliationJournalEntryLines.Add();
   jeLine2.TransactionNumber = "2";
  jeLine2.LineNumber = 2;

  SAPbobsCOM.ReconciliationBankStatementLine bstLine1 = (SAPbobsCOM. ReconciliationBankStatementLine)ExtReconciliation. ReconciliationBankStatementLines.Add();
  bstLine1.BankStatementAccountCode = "C1";
  bstLine1.Sequence = 1;

  SAPbobsCOM. ReconciliationBankStatementLine bstLine2 = (SAPbobsCOM. ReconciliationBankStatementLine)ExtReconciliation. ReconciliationBankStatementLines.Add();
  bstLine2.BankStatementAccountCode = " C1";
  bstLine2.Sequence = 2;

  ExtReconSvc.Reconcile(ExtReconciliation);

  //Get object.
  SAPbobsCOM.ExternalReconciliationParams ExtReconParam =
                          (SAPbobsCOM.ExternalReconciliationParams)ExtReconSvc.GetDataInterface(SAPbobsCOM.ExternalReconciliationsServiceDataInterfaces.ersExternalReconciliationParams);
  ExtReconParam.AccountCode = "100012";
  ExtReconParam.ReconciliationNo = "2";
  ExtReconciliation = ExtReconSvc.GetReconciliation(ExtReconParam);

  //Get Reconcile List.
  SAPbobsCOM.ExternalReconciliationsParamsCollection ExtReconsParamsCollection = (SAPbobsCOM. ExternalReconciliationsParamsCollection)ExtReconSvc.GetDataInterface(SAPbobsCOM.ExternalReconciliationsServiceDataInterfaces.ersExternalReconciliationsParamsCollection);

  SAPbobsCOM.ExternalReconciliationFilterParams ExtReconFilteredParams =
                          (SAPbobsCOM.ExternalReconciliationFilterParams)ExtReconSvc.GetDataInterface(SAPbobsCOM.ExternalReconciliationsServiceDataInterfaces.ersExternalReconciliationFilterParams);
  ExtReconFilteredParams.ReconciliationAccountType = SAPbobsCOM.ReconciliationAccountTypeEnum.rat_GLAccount;//"G/L Account"
  ExtReconFilteredParams.AccountCodeFrom = "11200000-01-001-01";
  ExtReconFilteredParams.AccountCodeTo = "12400000-01-001-01";
  ExtReconFilteredParams.ReconciliationDateFrom = "05/03/11";
  ExtReconFilteredParams.ReconciliationDateTo = "06/03/11";
  ExtReconFilteredParams.ReconciliationNoFrom = 1;
  ExtReconFilteredParams.ReconciliationNoTo = 2;
  ExtReconsParamsCollection = ExtReconSvc.GetReconciliationList(ExtReconFilteredParams);

  //Cancel reconciliations.
  foreach (SAPbobsCOM.ExternalReconciliationParams ExtReconParam in ExtReconsParamsCollection)
  {
              ExtReconSvc.CancelReconciliation(ExtReconParam);
    }
  ```

## Methods (7)
- `Public Sub CancelReconciliation(ByVal pIExternalReconciliationParams As ExternalReconciliationParams)` Cancels an external reconciliation.
  - param `pIExternalReconciliationParams`: The key of the external reconciliation to be canceled.
- `Public Function GetDataInterface(ByVal enumMSDI As ExternalReconciliationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ExternalReconciliationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ExternalReconciliationsServiceDataInterfaces.md`
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
- `Public Function GetReconciliation(ByVal pIExternalReconciliationParams As ExternalReconciliationParams) As ExternalReconciliation` Retrieves an external reconciliation.
  - param `pIExternalReconciliationParams`: The key of the external reconciliation to be retrieved.
- `Public Function GetReconciliationList(ByVal pIExternalReconciliationFilterParams As ExternalReconciliationFilterParams) As ExternalReconciliationsParamsCollection` Returns the ExternalReconciliationsParamsCollection data collection that identifies all external reconciliations.
  - param `pIExternalReconciliationFilterParams`: The key of the external reconciliation to be retrieved.
- `Public Sub Reconcile(ByVal pIExternalReconciliation As ExternalReconciliation)` Performs an external reconciliation.
  - param `pIExternalReconciliation`: The data for the external reconciliations.
