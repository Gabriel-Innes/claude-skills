<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FixedAssetItemsService (Object)

The FixedAssetItemsService service enables you to look up and update the end balance of an asset. Source table: OFDV, OFEV.

## Methods (6)
- `Public Function GetAssetEndBalance(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams) As FixedAssetEndBalance` GetAssetEndBalance
  - param `pIFixedAssetValuesParams`: 
- `Public Function GetAssetValuesList(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams) As FixedAssetValuesParamsCollection` GetAssetValuesList
  - param `pIFixedAssetValuesParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As FixedAssetItemsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/FixedAssetItemsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub UpdateAssetEndBalance(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams, ByVal pIFixedAssetEndBalance As FixedAssetEndBalance)` UpdateAssetEndBalance
  - param `pIFixedAssetValuesParams`: 
  - param `pIFixedAssetEndBalance`:
