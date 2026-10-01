<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ResourcePropertiesService (Object)

ResourcePropertiesService Class

## Methods (6)
- `Public Function Get(ByVal pIResourcePropertyParams As ResourcePropertyParams) As ResourceProperty` Get
  - param `pIResourcePropertyParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ResourcePropertiesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ResourcePropertiesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As ResourcePropertyParamsCollection` GetList
- `Public Sub Update(ByVal pIResourceProperty As ResourceProperty)` Update
  - param `pIResourceProperty`:
