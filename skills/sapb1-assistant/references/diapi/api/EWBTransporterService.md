<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EWBTransporterService (Object)

EWBTransporterService Class

## Methods (8)
- `Public Function AddTransporter(ByVal pIEWBTransporter As EWBTransporter) As EWBTransporterParams` AddTransporter
  - param `pIEWBTransporter`: 
- `Public Sub DeleteTransporter(ByVal pIEWBTransporterParams As EWBTransporterParams)` DeleteTransporter
  - param `pIEWBTransporterParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EWBTransporterServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EWBTransporterServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetEWBTransporterList() As EWBTransporterParamsCollection` GetEWBTransporterList
- `Public Function GetTransporter(ByVal pIEWBTransporterParams As EWBTransporterParams) As EWBTransporter` GetTransporter
  - param `pIEWBTransporterParams`: 
- `Public Sub UpdateTransporter(ByVal pIEWBTransporter As EWBTransporter)` UpdateTransporter
  - param `pIEWBTransporter`:
