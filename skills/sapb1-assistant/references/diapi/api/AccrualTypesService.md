<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AccrualTypesService (Object)

An accrual type is a set of conditions used to represent the differences between cost accounting and financial accounting. The AccrualTypesService service enables you to add, look up, update, and remove accrual types. Source table: OACR.

**Remarks:** Accrual types are defined only for use in the cost accounting reconciliation report. They do not affect other reports. To define accrual types, in the SAP Business One application, choose Financials --> Cost Accounting --> Accrual Type.

## Methods (8)
- `Public Function AddAccrualType(ByVal pIAccrualType As AccrualType) As AccrualTypeParams` Adds an accrual type.
  - param `pIAccrualType`: The data for the new accrual type.
- `Public Sub DeleteAccrualType(ByVal pIAccrualTypeParams As AccrualTypeParams)` Deletes an existing accrual type.
  - param `pIAccrualTypeParams`: The key of the accrual type to be deleted.
- `Public Function GetAccrualType(ByVal pIAccrualTypeParams As AccrualTypeParams) As AccrualType` Retrieves an accrual type. The accrual type is specified by its key, which is contained in the AccrualTypeParams object passed to the method.
  - param `pIAccrualTypeParams`: The key of the accrual type to retrieve.
- `Public Function GetAccrualTypeList() As AccrualTypesParams` Returns the AccrualTypesParams data collection that identify all accrual types.
- `Public Function GetDataInterface(ByVal enumMSDI As AccrualTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the AccrualTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AccrualTypesServiceDataInterfaces.md`
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
- `Public Sub UpdateAccrualType(ByVal pIAccrualType As AccrualType)` Updates an existing accrual type. The data for the accrual type, including the key of the accrual type to be updated, is contained in the AccrualType object passed to the method. To update an accrual type, you must first retrieve it using the GetAccrualType method.
  - param `pIAccrualType`: The data for the accrual type to be updated. The AccrualType object must contain the key of the object to be updated.
