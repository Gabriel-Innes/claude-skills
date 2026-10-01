<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ElectronicCommunicationActionService (Object)

ElectronicCommunicationActionService Class

## Methods (8)
- `Public Sub ConfirmSuccessOfCommunication(ByVal pIECMCodeParams As ECMCodeParams)` ConfirmSuccessOfCommunication
  - param `pIECMCodeParams`: 
- `Public Function GetAction(ByVal pIECMCodeParams As ECMCodeParams) As ECMActionStatusData` GetAction
  - param `pIECMCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ElectronicCommunicationActionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ElectronicCommunicationActionServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub ReportErrorAndContinue(ByVal pIECMCodeParams As ECMCodeParams)` ReportErrorAndContinue
  - param `pIECMCodeParams`: 
- `Public Sub ReportErrorAndStop(ByVal pIECMCodeParams As ECMCodeParams)` ReportErrorAndStop
  - param `pIECMCodeParams`: 
- `Public Sub UpdateAction(ByVal pActionStatusData As ECMActionStatusData)` UpdateAction
  - param `pActionStatusData`:
