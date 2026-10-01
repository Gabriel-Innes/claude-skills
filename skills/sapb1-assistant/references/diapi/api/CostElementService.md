<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CostElementService (Object)

CostElementService Class

## Methods (8)
- `Public Function AddCostElement(ByVal pICostElement As CostElement) As CostElementParams` AddCostElement
  - param `pICostElement`: 
- `Public Sub DeleteCostElement(ByVal pICostElementParams As CostElementParams)` DeleteCostElement
  - param `pICostElementParams`: 
- `Public Function GetCostElement(ByVal pICostElementParams As CostElementParams) As CostElement` GetCostElement
  - param `pICostElementParams`: 
- `Public Function GetCostElementList() As CostElementsParams` GetCostElementList
- `Public Function GetDataInterface(ByVal enumMSDI As CostElementServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CostElementServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub UpdateCostElement(ByVal pICostElement As CostElement)` UpdateCostElement
  - param `pICostElement`:
