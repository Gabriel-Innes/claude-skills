<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ElectronicCommunicationActionsService (Object)

ElectronicCommunicationActionsService Class

## Methods (11)
- `Public Function AddEcmAction(ByVal pIEcmAction As EcmAction) As EcmAction` AddEcmAction
  - param `pIEcmAction`: 
- `Public Function AddEcmActionLog(ByVal pIEcmActionLog As EcmActionLog) As EcmActionLog` AddEcmActionLog
  - param `pIEcmActionLog`: 
- `Public Sub DeleteEcmAction(ByVal pIEcmAction As EcmAction)` DeleteEcmAction
  - param `pIEcmAction`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ElectronicCommunicationActionsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ElectronicCommunicationActionsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetEcmAction(ByVal pIEcmActionParams As EcmActionParams) As EcmAction` GetEcmAction
  - param `pIEcmActionParams`: 
- `Public Function GetEcmActionByDoc(ByVal pIEcmActionDocParams As EcmActionDocParams) As EcmAction` GetEcmActionByDoc
  - param `pIEcmActionDocParams`: 
- `Public Function GetEcmActionLog(ByVal pIEcmActionLogParams As EcmActionLogParams) As EcmActionLog` GetEcmActionLog
  - param `pIEcmActionLogParams`: 
- `Public Function GetEcmActionLogList(ByVal pIEcmAction As EcmAction) As EcmActionLogCollection` GetEcmActionLogList
  - param `pIEcmAction`: 
- `Public Sub UpdateEcmAction(ByVal pIEcmAction As EcmAction)` UpdateEcmAction
  - param `pIEcmAction`:
