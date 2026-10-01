<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BrazilBeverageIndexersService (Object)

BrazilBeverageIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilBeverageIndexer As BrazilBeverageIndexer) As BrazilBeverageIndexerParams` Add
  - param `pIBrazilBeverageIndexer`: 
- `Public Sub Delete(ByVal pIBrazilBeverageIndexerParams As BrazilBeverageIndexerParams)` Delete
  - param `pIBrazilBeverageIndexerParams`: 
- `Public Function Get(ByVal pIBrazilBeverageIndexerParams As BrazilBeverageIndexerParams) As BrazilBeverageIndexer` Get
  - param `pIBrazilBeverageIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilBeverageIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BrazilBeverageIndexersServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As BrazilBeverageIndexersParams` GetList
