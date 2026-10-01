<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BlanketAgreementsService (Object)

The BlanketAgreementsService service enables you to add, look up, cancel, and update blanket agreements. Source table: OOAT.

**Remarks:** To open the blanket agreement window, choose Business Partners -> Blanket Agreement. To display the available blanket agreements, choose Business Partners -> Business Partner Reports -> Blanket Agreements List.

## Methods (9)
- `Public Function AddBlanketAgreement(ByVal pIBlanketAgreement As BlanketAgreement) As BlanketAgreementParams` Adds a blanket agreement.
  - param `pIBlanketAgreement`: The data for the new blanket agreement.
- `Public Sub CancelBlanketAgreement(ByVal pIBlanketAgreementParams As BlanketAgreementParams)` Cancels an existing blanket agreement.
  - param `pIBlanketAgreementParams`: The key of the blanket agreement to be cancelled.
- `Public Function GetBlanketAgreement(ByVal pIBlanketAgreementParams As BlanketAgreementParams) As BlanketAgreement` Retrieves a blanket agreement. The blanket agreement is specified by its key, which is contained in the BlanketAgreementParams object passed to the method.
  - param `pIBlanketAgreementParams`: The key of the blanket agreement to retrieve.
- `Public Function GetBlanketAgreementList() As BlanketAgreementsParams` Returns the BlanketAgreementsParams data collection that identifies all blanket agreements.
- `Public Function GetDataInterface(ByVal enumMSDI As BlanketAgreementsServiceDataInterfaces) As Object` Creates an empty data structure for use with the BlanketAgreementsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BlanketAgreementsServiceDataInterfaces.md`
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
- `Public Function GetRelatedDocuments(ByVal pIBlanketAgreementParams As BlanketAgreementParams) As BlanketAgreementsDocuments` Retrieves the related documents of a blanket agreement.
  - param `pIBlanketAgreementParams`: The key of the blanket agreement to retrieve.
- `Public Sub UpdateBlanketAgreement(ByVal pIBlanketAgreement As BlanketAgreement)` Updates an existing blanket agreement. The data for the blanket agreement, including the key of the blanket agreement to be updated, is contained in the BlanketAgreement object passed to the method. To update a blanket agreement, you must first retrieve it using the GetBlanketAgreement method.
  - param `pIBlanketAgreement`: The key of the blanket agreement to be updated.
