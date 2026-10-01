<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# NFModelsService (Object)

NFModelsService Class

## Methods (8)
- `Public Function Add(ByVal pINFModel As NFModel) As NFModelParams` Add
  - param `pINFModel`: 
- `Public Sub Delete(ByVal pINFModelParams As NFModelParams)` Delete
  - param `pINFModelParams`: 
- `Public Function Get(ByVal pINFModelParams As NFModelParams) As NFModel` Get
  - param `pINFModelParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As NFModelsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/NFModelsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As NFModelsParams` GetList
- `Public Sub Update(ByVal pINFModel As NFModel)` Update
  - param `pINFModel`:
