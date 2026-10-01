<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RetornoCodesService (Object)

RetornoCodesService Class

## Methods (8)
- `Public Function Add(ByVal pIRetornoCode As RetornoCode) As RetornoCodeParams` Add
  - param `pIRetornoCode`: 
- `Public Sub Delete(ByVal pIRetornoCodeParams As RetornoCodeParams)` Delete
  - param `pIRetornoCodeParams`: 
- `Public Function Get(ByVal pIRetornoCodeParams As RetornoCodeParams) As RetornoCode` Get
  - param `pIRetornoCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As RetornoCodesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/RetornoCodesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As RetornoCodeParamsCollection` GetList
- `Public Sub Update(ByVal pIRetornoCode As RetornoCode)` Update
  - param `pIRetornoCode`:
