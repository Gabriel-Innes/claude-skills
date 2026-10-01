<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InventoryCountingsService (Object)

The InventoryCountingsService service enables you to add, look up, update, and close inventory counting transactions. Source table: OINC.

**Remarks:** To open the Inventory Counting window, from the SAP Business One Main Menu, choose Inventory --> Inventory Transactions --> Inventory Counting Transactions --> Inventory Counting.

## Methods (8)
- `Public Function Add(ByVal pIInventoryCounting As InventoryCounting) As InventoryCountingParams` Adds an inventory counting transaction.
  - param `pIInventoryCounting`: The data for the new inventory counting transaction.
- `Public Sub Close(ByVal pIInventoryCountingParams As InventoryCountingParams)` Closes an existing inventory counting transaction.
  - param `pIInventoryCountingParams`: The key of the inventory counting transaction to be closed.
- `Public Function Get(ByVal pIInventoryCountingParams As InventoryCountingParams) As InventoryCounting` Retrieves an inventory counting transaction. The inventory counting transaction is specified by its key, which is contained in the InventoryCountingParams object passed to the method.
  - param `pIInventoryCountingParams`: The key of the inventory counting transaction to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As InventoryCountingsServiceDataInterfaces) As Object` Creates an empty data structure for use with the InventoryCountingsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/InventoryCountingsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object. The path and name of the XML file with which to create the object.
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
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` The XML with which to create the object.
  - param `bstrXMLString`: The XML with which to create the object.
- `Public Function GetList() As InventoryCountingParamsCollection` Returns the InventoryCountingParamsCollection data collection that identifies all inventory counting transactions.
- `Public Sub Update(ByVal pIInventoryCounting As InventoryCounting)` Updates an existing inventory counting transaction.
  - param `pIInventoryCounting`: The data for the inventory counting transaction to be updated. The InventoryCounting object must contain the key of the object to be updated.
