<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlternativeItemsService (Object)

This service manages alternative items in SAP Business One (add, delete, get by key, and update). Source table: OALI.

**Remarks:** To access Alternative Items in the application, choose Inventory > Item Management > Alternative Items.

## Methods (7)
- `Public Function AddItem(ByVal pIOriginalItem As OriginalItem) As OriginalItemParams` Adds an alternative item specified in the data structure OriginalItem (ItemCode and ItemName).
  - param `pIOriginalItem`: Specifies the alternative item data structure you want to add.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    ' Alternative Items Code Sample

    ' This sample assumes you have SBODemo_US database installed

    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim AltItemsService As SAPbobsCOM.AlternativeItemsService

    Dim OriItem As SAPbobsCOM.OriginalItem

    Dim OriItemParams As SAPbobsCOM.OriginalItemParams

    Dim AltItem As SAPbobsCOM.AlternativeItem

    oCompanyService = oCompany.GetCompanyService

    AltItemsService = oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.AlternativeItemsService)

    OriItem = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItem)

    OriItemParams = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItemParams)

    'Add 2 Alternative Items to Item A00003

    OriItem.ItemCode = "A00003" ' This item has no Alternative Items

    ' Adding first Alternative Item

    OriItem.AlternativeItems.Add()

    AltItem = OriItem.AlternativeItems.Item(0)

    AltItem.AlternativeItemCode = "A00001"

    AltItem.MatchFactor = 200

    ' Adding second Alternative Item

    OriItem.AlternativeItems.Add()

    AltItem = OriItem.AlternativeItems.Item(1)

    AltItem.AlternativeItemCode = "A00002"

    AltItem.MatchFactor = 400

    ' Adding the new Alternative Items

    OriItemParams = AltItemsService.AddItem(OriItem)
    ```
- `Public Sub DeleteItem(ByVal pIOriginalItemParams As OriginalItemParams)` Deletes the alternative item specified in data structure OriginalItemParams (ItemCode and ItemName).
  - param `pIOriginalItemParams`: Specifies the alternative item data structure you want to delete.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    ' Alternative Items Code Sample

    ' This sample assumes you have SBODemo_US database installed

    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim AltItemsService As SAPbobsCOM.AlternativeItemsService

    Dim OriItem As SAPbobsCOM.OriginalItem

    Dim OriItemParams As SAPbobsCOM.OriginalItemParams

    Dim AltItem As SAPbobsCOM.AlternativeItem

    oCompanyService = oCompany.GetCompanyService

    AltItemsService = oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.AlternativeItemsService)

    OriItem = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItem)

    OriItemParams = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItemParams)

    'Delete Alternative Item

    OriItemParams.ItemCode = "A00001"

    AltItemsService.DeleteItem(OriItemParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As AlternativeItemsServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AlternativeItemsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: Specifies the XML string.
- `Public Function GetItem(ByVal pIOriginalItemParams As OriginalItemParams) As OriginalItem` Returns an instance of the data structure OriginalItem.
  - param `pIOriginalItemParams`: Specifies the properties of the data structure you want to get (ItemName and ItemCode).
- `Public Sub UpdateItem(ByVal pIOriginalItem As OriginalItem)` Replaces an alternative item with the specified OriginalItem data structure.
  - param `pIOriginalItem`: Specifies the data structure (ItemCode and ItemName) that will replace the alternative item.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    ' Alternative Items Code Sample

    ' This sample assumes you have SBODemo_US database installed

    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim AltItemsService As SAPbobsCOM.AlternativeItemsService

    Dim OriItem As SAPbobsCOM.OriginalItem

    Dim OriItemParams As SAPbobsCOM.OriginalItemParams

    Dim AltItem As SAPbobsCOM.AlternativeItem

    oCompanyService = oCompany.GetCompanyService

    AltItemsService = oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.AlternativeItemsService)

    OriItem = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItem)

    OriItemParams = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItemParams)

    'Update Alternative Item

    OriItemParams.ItemCode = "A00001"

    OriItem = AltItemsService.GetItem(OriItemParams)

    'Getting the first alternative item

    AltItem = OriItem.AlternativeItems.Item(0)

    'Updating Alternative Item A00004 to have match factor 400

    AltItem.AlternativeItemCode = "A00004"

    AltItem.MatchFactor = 300

    AltItemsService.UpdateItem(OriItem)
    ```
