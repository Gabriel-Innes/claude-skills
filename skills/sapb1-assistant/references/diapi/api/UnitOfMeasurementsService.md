<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UnitOfMeasurementsService (Object)

The UnitOfMeasurementsService service enables you to add, look up, update, and remove unit of measurements. Source table: OUOM.

**Remarks:** To access the Units of Measurement - Setup window, choose Administration --> Setup --> Inventory --> Units of Measurement.

## Methods (8)
- `Public Function Add(ByVal pIUnitOfMeasurement As UnitOfMeasurement) As UnitOfMeasurementParams` Adds a UoM.
  - param `pIUnitOfMeasurement`: The data for the new UoM.
- `Public Sub Delete(ByVal pIUnitOfMeasurementParams As UnitOfMeasurementParams)` Deletes an existing UoM.
  - param `pIUnitOfMeasurementParams`: The key of the UoM to be deleted.
- `Public Function Get(ByVal pIUnitOfMeasurementParams As UnitOfMeasurementParams) As UnitOfMeasurement` Retrieves a UoM. The UoM is specified by its key, which is contained in the UnitOfMeasurementParams object passed to the method.
  - param `pIUnitOfMeasurementParams`: The key of the UoM to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As UnitOfMeasurementsServiceDataInterfaces) As Object` Creates an empty data structure for use with the UnitOfMeasurementsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/UnitOfMeasurementsServiceDataInterfaces.md`
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
- `Public Function GetList() As UnitOfMeasurementParamsCollection` Returns the UnitOfMeasurementParamsCollection data collection that identifies all UoMs.
- `Public Sub Update(ByVal pIUnitOfMeasurement As UnitOfMeasurement)` Updates an existing UoM.
  - param `pIUnitOfMeasurement`: The data for the UoM to be updated. The UnitOfMeasurement object must contain the key of the object to be updated.
