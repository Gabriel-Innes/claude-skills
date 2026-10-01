<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AttributeGroupsService (Object)

AttributeGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIAttributeGroup As AttributeGroup) As AttributeGroupParams` Add
  - param `pIAttributeGroup`: 
- `Public Sub Delete(ByVal pIAttributeGroupParams As AttributeGroupParams)` Delete
  - param `pIAttributeGroupParams`: 
- `Public Function Get(ByVal pIAttributeGroupParams As AttributeGroupParams) As AttributeGroup` Get
  - param `pIAttributeGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As AttributeGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AttributeGroupsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As AttributeGroupParamsCollection` GetList
- `Public Sub Update(ByVal pIAttributeGroup As AttributeGroup)` Update
  - param `pIAttributeGroup`:
