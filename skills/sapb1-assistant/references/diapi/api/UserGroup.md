<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserGroup (Object)

UserGroup Class

## Properties (7)
- `Public Property DueDate() As Date` [R/W] property DueDate
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property TPLId() As Long` [R/W] property TPLId
- `Public Property UserGroupDec() As String` [R/W] property UserGroupDec
- `Public Property UserGroupId() As Long` [R] property UserGroupId
- `Public Property UserGroupName() As String` [R/W] property UserGroupName
- `Public Property UserGroupType() As UserGroupCategoryEnum` [R/W] property UserGroupType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
