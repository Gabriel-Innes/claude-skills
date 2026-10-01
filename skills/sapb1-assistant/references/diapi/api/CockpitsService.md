<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CockpitsService (Object)

The CockpitsService service enables you to add, look up, update, and remove cockpits. Source table: OCPT.

**Remarks:** Note: - If you log on to an SAP Business One company with the cockpit enabled, and you connect to the same company via DI-API, the changes you make to the cockpits via DI-API are lost after you exit the SAP Business One application. It does not affect add/delete operations, only the update operations of the existing cockpits. You can update the cockpits successfully via DI-API without running the SAP Business One application that connects to the same company database. - If you make changes via DI-API to the database tables, the GUI of the SAP Business One application does not get updated immediately. To see the changes you have made via DI-API, re-open the Cockpit Management window. To open the Cockpit Management window, from the SAP Business One menu bar, choose Tools --> Cockpit --> Cockpit Management. Changes via DI-API are also available when you log on again to the company, or restart the SAP Business One application and connect to the company.

## Methods (11)
- `Public Function AddCockpit(ByVal pICockpit As Cockpit) As CockpitParams` Adds a cockpit.
  - param `pICockpit`: The data for the new cockpit.
  - returns: Contains the key (AbsEntry) of the new cockpit.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Cockpit cptAdd = (SAPbobsCOM.Cockpit)cockService.GetDataInterface(CockpitsServiceDataInterfaces.csCockpit);

    cptAdd.Name = "Name";
    cptAdd.Description = "Description";

    SAPbobsCOM.CockpitParams cockParamAdd = cockService.AddCockpit(cptAdd);
    ```
- `Public Sub DeleteCockpit(ByVal pICockpitParams As CockpitParams)` Deletes an existing cockpit.
  - param `pICockpitParams`: The key of the cockpit to be deleted.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CockpitsParams cockParamsDelete = cockService.GetCockpitList();

    if (cockParamsDelete.Count > 0)
    {
          //Delete the first one.
          SAPbobsCOM.CockpitParams cockParamDelete = cockParamsDelete.Item(0);
          cockService.DeleteCockpit(cockParamDelete);
    }
    ```
- `Public Function GetCockpit(ByVal pICockpitParams As CockpitParams) As Cockpit` Retrieves a specific cockpit.
  - param `pICockpitParams`: The key of the cockpit to retrieve.
  - returns: The cockpit with the specified key.
- `Public Function GetCockpitList() As CockpitsParams` Retrieves the keys and names of all the cockpits.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CockpitsParams cockParams = cockService.GetCockpitList();
    if (cockParams.Count > 0)
    {
         foreach (SAPbobsCOM.CockpitParams cockParam in cockParams)
         {
               SAPbobsCOM.Cockpit cpt = cockService.GetCockpit(cockParam);
         }
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As CockpitsServiceDataInterfaces) As Object` Creates an empty data structure for use with the CockpitsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CockpitsServiceDataInterfaces.md`
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
- `Public Function GetTemplateCockpitList() As CockpitsParams` GetTemplateCockpitList
- `Public Function GetUserCockpitList() As CockpitsParams` GetUserCockpitList
- `Public Sub PublishCockpit(ByVal pICockpit As Cockpit)` PublishCockpit
  - param `pICockpit`: 
- `Public Sub UpdateCockpit(ByVal pICockpit As Cockpit)` Updates an existing cockpit.
  - param `pICockpit`: The data for the cockpit to be updated. The Cockpit object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CockpitsParams cockParamsUpdate = cockService.GetCockpitList();

    if (cockParamsUpdate.Count > 0)
    {
          //Update the first one.
          SAPbobsCOM.CockpitParams cockParamUpdate = cockParamsUpdate.Item(0);
          SAPbobsCOM.Cockpit cptUpdate = cockService.GetCockpit(cockParamUpdate);
          cptUpdate.Description = "The updated description.";

          cockService.UpdateCockpit(cptUpdate);
    }
    ```
