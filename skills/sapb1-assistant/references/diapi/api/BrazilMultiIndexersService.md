<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BrazilMultiIndexersService (Object)

BrazilMultiIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilMultiIndexer As BrazilMultiIndexer) As BrazilMultiIndexerParams` Add
  - param `pIBrazilMultiIndexer`: 
- `Public Sub Delete(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams)` Delete
  - param `pIBrazilMultiIndexerParams`: 
- `Public Function Get(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams) As BrazilMultiIndexer` Get
  - param `pIBrazilMultiIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilMultiIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BrazilMultiIndexersServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetIndexerTypeList(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams) As BrazilMultiIndexersParams` GetIndexerTypeList
  - param `pIBrazilMultiIndexerParams`:
