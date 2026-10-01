<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallProblemSubTypesService (Object)

ServiceCallProblemSubTypesService Class

## Methods (8)
- `Public Function AddServiceCallProblemSubType(ByVal pIServiceCallProblemSubType As ServiceCallProblemSubType) As ServiceCallProblemSubTypeParams` AddServiceCallProblemSubType
  - param `pIServiceCallProblemSubType`: 
- `Public Sub DeleteServiceCallProblemSubType(ByVal pIServiceCallProblemSubTypeParams As ServiceCallProblemSubTypeParams)` DeleteServiceCallProblemSubType
  - param `pIServiceCallProblemSubTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallProblemSubTypesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ServiceCallProblemSubTypesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetServiceCallProblemSubType(ByVal pIServiceCallProblemSubTypeParams As ServiceCallProblemSubTypeParams) As ServiceCallProblemSubType` GetServiceCallProblemSubType
  - param `pIServiceCallProblemSubTypeParams`: 
- `Public Function GetServiceCallProblemSubTypeList() As ServiceCallProblemSubTypeParamsCollection` GetServiceCallProblemSubTypeList
- `Public Sub UpdateServiceCallProblemSubType(ByVal pIServiceCallProblemSubType As ServiceCallProblemSubType)` UpdateServiceCallProblemSubType
  - param `pIServiceCallProblemSubType`:
