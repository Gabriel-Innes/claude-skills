<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BrazilFuelIndexersService (Object)

BrazilFuelIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilFuelIndexer As BrazilFuelIndexer) As BrazilFuelIndexerParams` Add
  - param `pIBrazilFuelIndexer`: 
- `Public Sub Delete(ByVal pIBrazilFuelIndexerParams As BrazilFuelIndexerParams)` Delete
  - param `pIBrazilFuelIndexerParams`: 
- `Public Function Get(ByVal pIBrazilFuelIndexerParams As BrazilFuelIndexerParams) As BrazilFuelIndexer` Get
  - param `pIBrazilFuelIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilFuelIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BrazilFuelIndexersServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As BrazilFuelIndexersParams` GetList
