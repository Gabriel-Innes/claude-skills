<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BrazilStringIndexersService (Object)

BrazilStringIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilStringIndexer As BrazilStringIndexer) As BrazilStringIndexerParams` Add
  - param `pIBrazilStringIndexer`: 
- `Public Sub Delete(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams)` Delete
  - param `pIBrazilStringIndexerParams`: 
- `Public Function Get(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams) As BrazilStringIndexer` Get
  - param `pIBrazilStringIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilStringIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BrazilStringIndexersServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetIndexerTypeList(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams) As BrazilStringIndexersParams` GetIndexerTypeList
  - param `pIBrazilStringIndexerParams`:
