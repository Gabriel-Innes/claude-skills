<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProjectManagementTimeSheetService (Object)

ProjectManagementTimeSheetService Class

## Methods (7)
- `Public Function AddTimeSheet(ByVal pIPM_TimeSheetData As PM_TimeSheetData) As PM_TimeSheetParams` AddTimeSheet
  - param `pIPM_TimeSheetData`: 
- `Public Sub DeleteTimeSheet(ByVal pIPM_TimeSheetParams As PM_TimeSheetParams)` DeleteTimeSheet
  - param `pIPM_TimeSheetParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ProjectManagementTimeSheetServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ProjectManagementTimeSheetServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTimeSheet(ByVal pIPM_TimeSheetParams As PM_TimeSheetParams) As PM_TimeSheetData` GetTimeSheet
  - param `pIPM_TimeSheetParams`: 
- `Public Sub UpdateTimeSheet(ByVal pIPM_TimeSheetData As PM_TimeSheetData)` UpdateTimeSheet
  - param `pIPM_TimeSheetData`:
