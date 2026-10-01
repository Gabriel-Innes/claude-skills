<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BusinessPartnerPropertiesService (Object)

The BusinessPartnerPropertiesService service enables you to update and look up business partner properties in the business partner properties master data table. There are 64 properties. You can set the name of each property, and assign each property to a business partner as a flag. To see the list of properties, select Select Administration --> Setup --> Business Partners --> Business Partner Properties. Source table: OCQG

## Methods (6)
- `Public Function GetBusinessPartnerProperty(ByVal pIBusinessPartnerPropertyParams As BusinessPartnerPropertyParams) As BusinessPartnerProperty` Retrieves a business partner property. The business partner property is specified by its key (GroupCode), which is contained in the BusinessPartnerPropertyParams object passed to the method.
  - param `pIBusinessPartnerPropertyParams`: The key of the business partner property to retrieve.
  - returns: The business partner property with the specified key.
- `Public Function GetBusinessPartnerPropertyList() As BusinessPartnerPropertiesParams` Retrieves the keys and names of all the business partner properties.
  - C# example (from SAP's help):
    ```csharp
    try
    {
         BusinessPartnerPropertiesParams getParams;
         getParams = oBPPropSrv.GetBusinessPartnerPropertyList();

         String resultSet = "";

         foreach (BusinessPartnerPropertyParams record in getParams)
         {
              resultSet = resultSet + record.PropertyCode + "\t" + record.PropertyName + "\n";
         }
         Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As BusinessPartnerPropertiesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BusinessPartnerPropertiesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BusinessPartnerPropertiesServiceDataInterfaces.md`
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
- `Public Sub UpdateBusinessPartnerProperty(ByVal pIBusinessPartnerProperty As BusinessPartnerProperty)` Updates an existing business partner property. The data for the business partner property, including the key of the business partner property to be updated, is contained in the BusinessPartnerProperty object passed to the method. To update a business partner property, you must first retrieve it using the GetBusinessPartnerProperty method.
  - param `pIBusinessPartnerProperty`: The data for the business partner property to be updated. The BusinessPartnerProperty object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    try
    {
         oBPPropSrv = (BusinessPartnerPropertiesService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.BusinessPartnerPropertiesService));
         BusinessPartnerPropertyParams getLine;
         BusinessPartnerProperty updateLine;

         getLine = (BusinessPartnerPropertyParams)oBPPropSrv.GetDataInterface(BusinessPartnerPropertiesServiceDataInterfaces.bppsBusinessPartnerPropertyParams);

         // update
         getLine.PropertyCode = 5;
         updateLine = oBPPropSrv.GetBusinessPartnerProperty(getLine);
         updateLine.PropertyName = "New Value";
         oBPPropSrv.UpdateBusinessPartnerProperty(updateLine);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
