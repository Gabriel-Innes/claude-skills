<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ResourceCapacitiesService (Object)

ResourceCapacitiesService Class

## Methods (8)
- `Public Function Add(ByVal pIResourceCapacity As ResourceCapacity) As ResourceCapacityParams` Add
  - param `pIResourceCapacity`: 
- `Public Function Get(ByVal pIResourceCapacityParams As ResourceCapacityParams) As ResourceCapacity` Get
  - param `pIResourceCapacityParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ResourceCapacitiesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ResourceCapacitiesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As ResourceCapacityParamsCollection` GetList
- `Public Function GetListWithFilter(ByVal pIResourceCapacityWithFilterParams As ResourceCapacityWithFilterParams) As ResourceCapacityParamsCollection` GetListWithFilter
  - param `pIResourceCapacityWithFilterParams`: 
- `Public Sub Update(ByVal pIResourceCapacity As ResourceCapacity)` Update
  - param `pIResourceCapacity`:
