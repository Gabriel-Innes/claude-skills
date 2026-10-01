<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExportDeterminationService (Object)

ExportDeterminationService Class

## Methods (8)
- `Public Sub AddDetermination(ByVal pIExportDetermination As ExportDetermination)` AddDetermination
  - param `pIExportDetermination`: 
- `Public Sub DeleteDetermination(ByVal pIExportDeterminationParams As ExportDeterminationParams)` DeleteDetermination
  - param `pIExportDeterminationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExportDeterminationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ExportDeterminationServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDetermination(ByVal pIExportDeterminationParams As ExportDeterminationParams) As ExportDetermination` GetDetermination
  - param `pIExportDeterminationParams`: 
- `Public Function GetDeterminations(ByVal pIExportDeterminationsParams As ExportDeterminationsParams) As ExportDeterminationsCollection` GetDeterminations
  - param `pIExportDeterminationsParams`: 
- `Public Sub UpdateDetermination(ByVal pIExportDetermination As ExportDetermination)` UpdateDetermination
  - param `pIExportDetermination`:
