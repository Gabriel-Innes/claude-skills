<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AssetDepreciationGroupsService (Object)

AssetDepreciationGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIAssetDepreciationGroup As AssetDepreciationGroup) As AssetDepreciationGroupParams` Add
  - param `pIAssetDepreciationGroup`: 
- `Public Sub Delete(ByVal pIAssetDepreciationGroupParams As AssetDepreciationGroupParams)` Delete
  - param `pIAssetDepreciationGroupParams`: 
- `Public Function Get(ByVal pIAssetDepreciationGroupParams As AssetDepreciationGroupParams) As AssetDepreciationGroup` Get
  - param `pIAssetDepreciationGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As AssetDepreciationGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AssetDepreciationGroupsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As AssetDepreciationGroupParamsCollection` GetList
- `Public Sub Update(ByVal pIAssetDepreciationGroup As AssetDepreciationGroup)` Update
  - param `pIAssetDepreciationGroup`:
