<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AssetDocumentService (Object)

The AssetDocumentService service enables you to add, look up, update, cancel, and remove asset documents. Source table: OACQ.

**Remarks:** From the SAP Business One Main Menu, choose Financials --> Fixed Assets.

**Example:**
- C# example (from SAP's help):
  ```csharp
  AssetDocumentService AssetService = (AssetDocumentService)m_oCompanyService.GetBusinessService(ServiceTypes.AssetCapitalizationService);
  AssetDocument AssetDocument = AssetService.GetDataInterface(AssetDocumentServiceDataInterfaces.adsAssetDocument);
  AssetDocumentLine line = AssetDocument.AssetDocumentLineCollection.Add();
  AssetDocumentAreaJournal journalEn = AssetDocument.AssetDocumentAreaJournalCollection.Add();

  AssetDocument.AssetValueDate = New DateTime(2013, 8, 1);
  line.AssetNumber = "FA01";
  line.TotalLC = 15000;
  journalEn.DepreciationArea = "DA_test";
  journalEn.JournalRemarks = "Remark_test";

  AssetService.Add(AssetDocument);
  ```
- C# example (from SAP's help):
  ```csharp
  AssetDocumentService AssetService = (AssetDocumentService)m_oCompanyService.GetBusinessService(ServiceTypes.AssetCapitalizationService);
  AssetDocumentParams faDocumentParams = (AssetDocumentParams)AssetService.GetDataInterface(AssetDocumentServiceDataInterfaces.adsAssetDocumentParams);
  faDocumentParams.Code = 1;
  AssetDocument AssetDocument = AssetService.Get(faDocumentParams);

  AssetDocument.AssetDocumentLineCollection.Item(0).Remarks = "Test1";
  AssetDocument.Remarks = "Test2";

  AssetService.Update(AssetDocument);
  ```
- C# example (from SAP's help):
  ```csharp
  AssetDocumentService AssetService = (AssetDocumentService)m_oCompanyService.GetBusinessService(ServiceTypes.AssetCapitalizationService);
  AssetDocumentParams faDocumentParams = AssetService.GetDataInterface(AssetDocumentServiceDataInterfaces.adsAssetDocumentParams);

  faDocumentParams.Code = 1;
  faDocumentParams.CancellationOption = ClosingOptionEnum.coBySpecifiedDate;
  faDocumentParams.CancellationDate = new DateTime(2013, 10, 1);
  AssetService.Cancel(faDocumentParams);
  ```

## Methods (9)
- `Public Function Add(ByVal pIAssetDocument As AssetDocument) As AssetDocumentParams` Adds an asset document.
  - param `pIAssetDocument`: The data for the new asset document.
- `Public Sub Cancel(ByVal pIAssetDocumentParams As AssetDocumentParams)` Cancels an existing asset document.
  - param `pIAssetDocumentParams`: The key of the asset document to be cancelled.
- `Public Sub Delete(ByVal pIAssetDocumentParams As AssetDocumentParams)` Deletes an existing asset document.
  - param `pIAssetDocumentParams`: The key of the asset document to be deleted.
- `Public Function Get(ByVal pIAssetDocumentParams As AssetDocumentParams) As AssetDocument` Retrieves an asset document. The asset document is specified by its key, which is contained in the AssetDocumentParams object passed to the method.
  - param `pIAssetDocumentParams`: The key of the asset document to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As AssetDocumentServiceDataInterfaces) As Object` Creates an empty data structure for use with the AssetDocumentService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AssetDocumentServiceDataInterfaces.md`
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
- `Public Function GetList() As AssetDocumentParamsCollection` Returns the AssetDocumentParamsCollection data collection that identifies all asset documents.
- `Public Sub Update(ByVal pIAssetDocument As AssetDocument)` Updates an existing asset document. The data for the asset document, including the key of the asset document to be updated, is contained in the AssetDocument object passed to the method. To update an asset document, you must first retrieve it using the Get method.
  - param `pIAssetDocument`: The data for the asset document to be updated. The AssetDocument object must contain the key of the object to be updated.
