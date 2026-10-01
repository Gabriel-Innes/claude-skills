<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BarCodesService (Object)

The BarCodesService service enables you to add, look up, update, and remove bar codes. Source table: OBCD.

**Remarks:** To access the Bar Codes window, from the SAP Business One Main Menu, choose Inventory --> Bar Codes.

## Methods (8)
- `Public Function Add(ByVal pIBarcode As BarCode) As BarCodeParams` Adds a bar code.
  - param `pIBarcode`: The data for the new bar code.
- `Public Sub Delete(ByVal pIBarcodeParams As BarCodeParams)` Deletes an existing bar code.
  - param `pIBarcodeParams`: The key of the bar code to be deleted.
- `Public Function Get(ByVal pIBarcodeParams As BarCodeParams) As BarCode` Retrieves a bar code. The bar code is specified by its key, which is contained in the BarCodeParams object passed to the method.
  - param `pIBarcodeParams`: The key of the bar code to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BarCodesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BarCodesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BarCodesServiceDataInterfaces.md`
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
- `Public Function GetList() As BarCodeParamsCollection` Returns the BarCodeParamsCollection data collection that identifies all bar codes.
- `Public Sub Update(ByVal pIBarcode As BarCode)` Updates an existing bar code.
  - param `pIBarcode`: The data for the bar code to be updated. The BarCode object must contain the key of the object to be updated.
