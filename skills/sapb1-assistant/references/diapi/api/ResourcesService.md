<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ResourcesService (Object)

The ResourcesService service enables you to add, look up, update, and delete resources in SAP Business One. Source table: ORSC.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.CompanyService oCS = (SAPbobsCOM.CompanyService)oCompany.GetCompanyService();
  SAPbobsCOM.ResourcesService srvResources = (SAPbobsCOM.ResourcesService)oCS.GetBusinessService(SAPbobsCOM.ServiceTypes.ResourcesService);
  SAPbobsCOM.Resource res = (SAPbobsCOM.Resource)srvResources.GetDataInterface(SAPbobsCOM.ResourcesServiceDataInterfaces.rsdiResource);

  res.VisCode = "r1";
  SAPbobsCOM.ResourceWarehouse Whs = res.Warehouses.Add();
  Whs.Warehouse = "01";

  SAPbobsCOM.ResourceDailyCapacity DC = res.DailyCapacities.Add();
  DC.Weekday = SAPbobsCOM.ResourceDailyCapacityWeekdayEnum.rdcwFirst;
  DC.Factor1 = 1;

  SAPbobsCOM.ResourceParams ret = srvResources.Add(res);
  ```
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.ResourceParams par = (SAPbobsCOM.ResourceParams)srvResources.GetDataInterface(SAPbobsCOM.ResourcesServiceDataInterfaces.rsdiResourceParams);
  par.Code = ret.Code; //"r1";
  SAPbobsCOM.Resource res2 = srvResources.Get(par);
  res2.Name = "name";
  srvResources.Update(res2);
  ```

## Methods (9)
- `Public Function Add(ByVal pIResource As Resource) As ResourceParams` Adds a new resource.
  - param `pIResource`: The data for the new resource.
- `Public Sub CreateLinkedItem(ByVal pIResourceParams As ResourceParams)` Creates a non-inventory item that links to the resource.
  - param `pIResourceParams`: The key of the resource to be linked.
  - remarks: By linking resources to non-inventory items, you can purchase and sell these resources in AP/AR order documents (via the existing non-inventory item functionality). This is especially helpful for service-based businesses.
- `Public Sub Delete(ByVal pIResourceParams As ResourceParams)` Deletes an existing resource.
  - param `pIResourceParams`: The key of the resource to be deleted.
- `Public Function Get(ByVal pIResourceParams As ResourceParams) As Resource` Retrieves a resource. The resource is specified by its key, which is contained in the ResourceParams object passed to the method.
  - param `pIResourceParams`: The key of the resource to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As ResourcesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ResourcesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ResourcesServiceDataInterfaces.md`
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
- `Public Function GetList() As ResourceParamsCollection` Returns the ResourceParamsCollection data collection that identify all resources.
- `Public Sub Update(ByVal pIResource As Resource)` Updates an existing resource. The data for the resource, including the key of the resource to be updated, is contained in the Resource object passed to the method. To update a resource, you must first retrieve it using the Get method.
  - param `pIResource`: The data for the resource to be updated. The Resource object must contain the key of the object to be updated.
