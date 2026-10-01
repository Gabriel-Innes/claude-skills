<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# IndiaSacCodeService (Object)

IndiaSacCodeService Class

## Methods (8)
- `Public Function Add(ByVal pIIndiaSacCode As IndiaSacCode) As IndiaSacCodeParams` Add
  - param `pIIndiaSacCode`: 
- `Public Sub Delete(ByVal pIIndiaSacCodeParams As IndiaSacCodeParams)` Delete
  - param `pIIndiaSacCodeParams`: 
- `Public Function Get(ByVal pIIndiaSacCodeParams As IndiaSacCodeParams) As IndiaSacCode` Get
  - param `pIIndiaSacCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IndiaSacCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/IndiaSacCodeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As IndiaSacCodeParamsCollection` GetList
- `Public Sub Update(ByVal pIIndiaSacCode As IndiaSacCode)` Update
  - param `pIIndiaSacCode`:
