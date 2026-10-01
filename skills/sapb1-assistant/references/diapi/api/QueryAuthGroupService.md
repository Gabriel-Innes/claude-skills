<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# QueryAuthGroupService (Object)

QueryAuthGroupService Class

## Methods (8)
- `Public Function AddQueryAuthGroup(ByVal pIQueryAuthGroup As QueryAuthGroup) As QueryAuthGroup` AddQueryAuthGroup
  - param `pIQueryAuthGroup`: 
- `Public Function GetDataInterface(ByVal enumMSDI As QueryAuthGroupServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/QueryAuthGroupServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetQueryAuthGroup(ByVal pIQueryAuthGroupParams As QueryAuthGroupParams) As QueryAuthGroup` GetQueryAuthGroup
  - param `pIQueryAuthGroupParams`: 
- `Public Function GetQueryAuthGroupList() As QueryAuthGroupCollection` GetQueryAuthGroupList
- `Public Sub RemoveQueryAuthGroup(ByVal pIQueryAuthGroupParams As QueryAuthGroupParams)` RemoveQueryAuthGroup
  - param `pIQueryAuthGroupParams`: 
- `Public Sub UpdateQueryAuthGroup(ByVal pIQueryAuthGroup As QueryAuthGroup)` UpdateQueryAuthGroup
  - param `pIQueryAuthGroup`:
