<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ResourceGroupsService (Object)

ResourceGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIResourceGroup As ResourceGroup) As ResourceGroupParams` Add
  - param `pIResourceGroup`: 
- `Public Sub Delete(ByVal pIResourceGroupParams As ResourceGroupParams)` Delete
  - param `pIResourceGroupParams`: 
- `Public Function Get(ByVal pIResourceGroupParams As ResourceGroupParams) As ResourceGroup` Get
  - param `pIResourceGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ResourceGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ResourceGroupsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As ResourceGroupParamsCollection` GetList
- `Public Sub Update(ByVal pIResourceGroup As ResourceGroup)` Update
  - param `pIResourceGroup`:
