<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BankChargesAllocationCodesService (Object)

The BankChargesAllocationCodesService service enables you to add, look up, update, and remove allocation codes for bank charges. Source table: OBCA.

**Remarks:** To see the list of codes for the allocation of bank charges, from SAP Business One, choose Administration --> Setup --> Banking --> Bank Charges Allocation Codes.

## Methods (9)
- `Public Function AddBankChargesAllocationCode(ByVal pIBankChargesAllocationCode As BankChargesAllocationCode) As BankChargesAllocationCodeParams` Adds a bank charges allocation code.
  - param `pIBankChargesAllocationCode`: The data for the bank charges allocation code.
- `Public Sub DeleteBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams)` Deletes an existing bank charges allocation code.
  - param `pIBankChargesAllocationCodeParams`: The key of the bank charges allocation code to be deleted.
- `Public Function GetBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams) As BankChargesAllocationCode` Retrieves a bank charges allocation code. The bank charges allocation code is specified by its key, which is contained in the BankChargesAllocationCodeParams object passed to the method.
  - param `pIBankChargesAllocationCodeParams`: The key of the bank charges allocation code to retrieve.
- `Public Function GetBankChargesAllocationCodeList() As BankChargesAllocationCodesParams` Returns the BankChargesAllocationCodesParams data collection that identify all bank charges allocation codes.
- `Public Function GetDataInterface(ByVal enumMSDI As BankChargesAllocationCodesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BankChargesAllocationCodesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BankChargesAllocationCodesServiceDataInterfaces.md`
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
- `Public Sub SetDefaultBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams)` Sets the default bank charges allocation code.
  - param `pIBankChargesAllocationCodeParams`: The key of the bank charges allocation code.
  - C# example (from SAP's help):
    ```csharp
    void SetDefaultCode ()
            {
                Try
                {
                    CompanyService oCompSrv = MyCompany.GetCompanyService();
                    BankChargesAllocationCodesService oBCACodeSrv = (BankChargesAllocationCodesService)(oCompSrv.GetBusinessService(ServiceTypes.BankChargesAllocationCodesService));
                    BCACodeParams defaultCode;
                    defaultCode = (BCACodeParams)oBCACodeSrv.GetDataInterface(BankChargesAllocationCodesServiceDataInterfaces.bcacsBCACodeParams);
                    defaultCode.Code = "1";
                    oBCACodeSrv. SetDefaultBankChargesAllocationCode(defaultCode);
                }
                Catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString());
                }
    }
    ```
- `Public Sub UpdateBankChargesAllocationCode(ByVal pIBankChargesAllocationCode As BankChargesAllocationCode)` Updates an existing bank charges allocation code. The data for the bank charges allocation code, including the key of the bank charges allocation code to be updated, is contained in the BankChargesAllocationCode object passed to the method. To update a bank charges allocation code, you must first retrieve it using the GetBankChargesAllocationCode method.
  - param `pIBankChargesAllocationCode`: The data for the bank charges allocation code to be updated. The BankChargesAllocationCode object must contain the key of the object to be updated.
