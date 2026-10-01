<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmailGroupsService (Object)

EmailGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIEmailGroup As EmailGroup) As EmailGroupParams` Add
  - param `pIEmailGroup`: 
- `Public Sub Delete(ByVal pIEmailGroupParams As EmailGroupParams)` Delete
  - param `pIEmailGroupParams`: 
- `Public Function Get(ByVal pIEmailGroupParams As EmailGroupParams) As EmailGroup` Get
  - param `pIEmailGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmailGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EmailGroupsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EmailGroupParamsCollection` GetList
- `Public Sub Update(ByVal pIEmailGroup As EmailGroup)` Update
  - param `pIEmailGroup`:
