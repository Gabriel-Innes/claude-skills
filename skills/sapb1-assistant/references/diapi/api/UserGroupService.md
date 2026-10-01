<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserGroupService (Object)

UserGroupService Class

## Methods (8)
- `Public Function AddUserGroup(ByVal pIUserGroup As UserGroup) As UserGroupParams` AddUserGroup
  - param `pIUserGroup`: 
- `Public Sub DeleteUserGroup(ByVal pIUserGroupParams As UserGroupParams)` DeleteUserGroup
  - param `pIUserGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As UserGroupServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/UserGroupServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetUserGroup(ByVal pIUserGroupParams As UserGroupParams) As UserGroup` GetUserGroup
  - param `pIUserGroupParams`: 
- `Public Function GetUserGroupList() As UserGroupsParams` GetUserGroupList
- `Public Sub UpdateUserGroup(ByVal pIUserGroup As UserGroup)` UpdateUserGroup
  - param `pIUserGroup`:
