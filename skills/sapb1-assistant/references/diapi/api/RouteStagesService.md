<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RouteStagesService (Object)

RouteStagesService Class

## Methods (8)
- `Public Function Add(ByVal pIRouteStage As RouteStage) As RouteStageParams` Add
  - param `pIRouteStage`: 
- `Public Sub Delete(ByVal pIRouteStageParams As RouteStageParams)` Delete
  - param `pIRouteStageParams`: 
- `Public Function Get(ByVal pIRouteStageParams As RouteStageParams) As RouteStage` Get
  - param `pIRouteStageParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As RouteStagesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/RouteStagesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As RouteStageParamsCollection` GetList
- `Public Sub Update(ByVal pIRouteStage As RouteStage)` Update
  - param `pIRouteStage`:
