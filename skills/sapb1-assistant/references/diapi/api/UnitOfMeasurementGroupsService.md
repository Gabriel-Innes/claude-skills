<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UnitOfMeasurementGroupsService (Object)

The UnitOfMeasurementGroupsService service enables you to add, look up, update, and remove unit of measurement groups. Source table: OUGP.

**Remarks:** From the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Unit of Measurement Groups. In the Unit of Measurement - Setup window, enter a group name and its description. Choose Group Definition to open the Unit of Measurement Groups – <Group> – Setup window.

## Methods (8)
- `Public Function Add(ByVal pIUnitOfMeasurementGroup As UnitOfMeasurementGroup) As UnitOfMeasurementGroupParams` Adds a UoM group.
  - param `pIUnitOfMeasurementGroup`: The data for the new UoM group.
- `Public Sub Delete(ByVal pIUnitOfMeasurementGroupParams As UnitOfMeasurementGroupParams)` Deletes an existing UoM group.
  - param `pIUnitOfMeasurementGroupParams`: The key of the UoM group to be deleted.
- `Public Function Get(ByVal pIUnitOfMeasurementGroupParams As UnitOfMeasurementGroupParams) As UnitOfMeasurementGroup` Retrieves a UoM group. The UoM group is specified by its key, which is contained in the UnitOfMeasurementGroupParams object passed to the method.
  - param `pIUnitOfMeasurementGroupParams`: The key of the UoM group to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As UnitOfMeasurementGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the UnitOfMeasurementGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/UnitOfMeasurementGroupsServiceDataInterfaces.md`
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
- `Public Function GetList() As UnitOfMeasurementGroupParamsCollection` Returns the UnitOfMeasurementGroupParamsCollection data collection that identifies all UoM groups.
- `Public Sub Update(ByVal pIUnitOfMeasurementGroup As UnitOfMeasurementGroup)` Updates an existing UoM group.
  - param `pIUnitOfMeasurementGroup`: The data for the UoM group to be updated. The UnitOfMeasurementGroup object must contain the key of the object to be updated.
