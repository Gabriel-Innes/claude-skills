<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WitholdingTaxDefinitionService (Object)

WitholdingTaxDefinitionService Class

## Methods (7)
- `Public Function AddWTDCode(ByVal pIWTDCode As WTDCode) As WTDCodeParamsCollection` AddWTDCode
  - param `pIWTDCode`: 
- `Public Sub Delete(ByVal pIWTDCodeParamsCollection As WTDCodeParamsCollection)` Delete
  - param `pIWTDCodeParamsCollection`: 
- `Public Function Get(ByVal pIWTDCodeParams As WTDCodeParams) As WTDCode` Get
  - param `pIWTDCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As WitholdingTaxDefinitionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/WitholdingTaxDefinitionServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub UpdateWTDCode(ByVal pIWTDCode As WTDCode)` UpdateWTDCode
  - param `pIWTDCode`:
