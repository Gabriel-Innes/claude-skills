<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InventoryOpeningBalancesService (Object)

InventoryOpeningBalancesService Class

## Methods (7)
- `Public Function Add(ByVal pIInventoryOpeningBalance As InventoryOpeningBalance) As InventoryOpeningBalanceParams` Add
  - param `pIInventoryOpeningBalance`: 
- `Public Function Get(ByVal pIInventoryOpeningBalanceParams As InventoryOpeningBalanceParams) As InventoryOpeningBalance` Get
  - param `pIInventoryOpeningBalanceParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As InventoryOpeningBalancesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/InventoryOpeningBalancesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As InventoryOpeningBalanceParamsCollection` GetList
- `Public Sub Update(ByVal pIInventoryOpeningBalance As InventoryOpeningBalance)` Update
  - param `pIInventoryOpeningBalance`:
