<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BrazilNumericIndexersService (Object)

BrazilNumericIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilNumericIndexer As BrazilNumericIndexer) As BrazilNumericIndexerParams` Add
  - param `pIBrazilNumericIndexer`: 
- `Public Sub Delete(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams)` Delete
  - param `pIBrazilNumericIndexerParams`: 
- `Public Function Get(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams) As BrazilNumericIndexer` Get
  - param `pIBrazilNumericIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilNumericIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BrazilNumericIndexersServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetIndexerTypeList(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams) As BrazilNumericIndexersParams` GetIndexerTypeList
  - param `pIBrazilNumericIndexerParams`:
