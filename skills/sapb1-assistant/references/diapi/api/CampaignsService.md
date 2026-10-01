<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CampaignsService (Object)

The CampaignsService service enables you to add, look up, update, cancel, and remove campaigns. Source table: OCPN.

**Remarks:** Managing a promotional campaign typically involves the steps outlined below: - Creating and maintaining a TargetGroup - Creating a campaign using the Campaign Generation wizard To access the wizard, from the SAP Business One Main Menu, choose Business Partners --> Campaign Generation Wizard. - Managing the campaign data To access the Campaign window, from the SAP Business One Main Menu, choose Business Partners --> Campaign.

## Methods (9)
- `Public Function Add(ByVal pICampaign As Campaign) As CampaignParams` Adds a campaign.
  - param `pICampaign`: The data for the new campaign.
- `Public Sub Cancel(ByVal pICampaignParams As CampaignParams)` Cancels an existing campaign.
  - param `pICampaignParams`: The key of the campaign to be cancelled.
- `Public Sub Delete(ByVal pICampaignParams As CampaignParams)` Deletes an existing campaign.
  - param `pICampaignParams`: The key of the campaign to be deleted.
- `Public Function Get(ByVal pICampaignParams As CampaignParams) As Campaign` Retrieves a campaign. The campaign is specified by its key, which is contained in the CampaignParams object passed to the method.
  - param `pICampaignParams`: The key of the campaign to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As CampaignsServiceDataInterfaces) As Object` Creates an empty data structure for use with the CampaignsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CampaignsServiceDataInterfaces.md`
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
- `Public Function GetList() As CampaignsParams` Returns the CampaignsParams data collection that identifies all campaigns.
- `Public Sub Update(ByVal pICampaign As Campaign)` Updates an existing campaign.
  - param `pICampaign`: The data for the campaign to be updated. The Campaign object must contain the key of the object to be updated.
