<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ImportDeterminationService (Object)

ImportDeterminationService Class

## Methods (8)
- `Public Sub AddDetermination(ByVal pIImportDetermination As ImportDetermination)` AddDetermination
  - param `pIImportDetermination`: 
- `Public Sub DeleteDetermination(ByVal pIImportDeterminationParams As ImportDeterminationParams)` DeleteDetermination
  - param `pIImportDeterminationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ImportDeterminationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ImportDeterminationServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDetermination(ByVal pIImportDeterminationParams As ImportDeterminationParams) As ImportDetermination` GetDetermination
  - param `pIImportDeterminationParams`: 
- `Public Function GetDeterminations(ByVal pIImportDeterminationsParams As ImportDeterminationsParams) As ImportDeterminationsCollection` GetDeterminations
  - param `pIImportDeterminationsParams`: 
- `Public Sub UpdateDetermination(ByVal pIImportDetermination As ImportDetermination)` UpdateDetermination
  - param `pIImportDetermination`:
