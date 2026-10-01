<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DepreciationTypePoolsService (Object)

Source table: ODPP.

## Methods (8)
- `Public Function Add(ByVal pIDepreciationTypePool As DepreciationTypePool) As DepreciationTypePoolParams` Add
  - param `pIDepreciationTypePool`: 
- `Public Sub Delete(ByVal pIDepreciationTypePoolParams As DepreciationTypePoolParams)` Delete
  - param `pIDepreciationTypePoolParams`: 
- `Public Function Get(ByVal pIDepreciationTypePoolParams As DepreciationTypePoolParams) As DepreciationTypePool` Get
  - param `pIDepreciationTypePoolParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As DepreciationTypePoolsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DepreciationTypePoolsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As DepreciationTypePoolParamsCollection` GetList
- `Public Sub Update(ByVal pIDepreciationTypePool As DepreciationTypePool)` Update
  - param `pIDepreciationTypePool`:
