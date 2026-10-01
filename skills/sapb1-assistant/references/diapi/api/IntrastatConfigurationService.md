<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# IntrastatConfigurationService (Object)

IntrastatConfigurationService Class

## Methods (8)
- `Public Function Add(ByVal pIIntrastatConfiguration As IntrastatConfiguration) As IntrastatConfigurationParams` Add
  - param `pIIntrastatConfiguration`: 
- `Public Sub Delete(ByVal pIIntrastatConfigurationParams As IntrastatConfigurationParams)` Delete
  - param `pIIntrastatConfigurationParams`: 
- `Public Function Get(ByVal pIIntrastatConfigurationParams As IntrastatConfigurationParams) As IntrastatConfiguration` Get
  - param `pIIntrastatConfigurationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IntrastatConfigurationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/IntrastatConfigurationServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As IntrastatConfigurationCollectionParams` GetList
- `Public Sub Update(ByVal pIIntrastatConfiguration As IntrastatConfiguration)` Update
  - param `pIIntrastatConfiguration`:
