<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ActivitySubjectService (Object)

ActivitySubjectService Class

## Methods (8)
- `Public Function AddActivitySubject(ByVal pIActivitySubject As ActivitySubject) As ActivitySubjectParams` AddActivitySubject
  - param `pIActivitySubject`: 
- `Public Function GetActivitySubject(ByVal pIActivitySubjectParams As ActivitySubjectParams) As ActivitySubject` GetActivitySubject
  - param `pIActivitySubjectParams`: 
- `Public Function GetActivitySubjectList() As ActivitySubjectsParams` GetActivitySubjectList
- `Public Function GetDataInterface(ByVal enumMSDI As ActivitySubjectServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ActivitySubjectServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetListByTypeCode(ByVal pIActivitySubject As ActivitySubject) As ActivitySubjectsParams` GetListByTypeCode
  - param `pIActivitySubject`: 
- `Public Sub UpdateActivitySubject(ByVal pIActivitySubject As ActivitySubject)` UpdateActivitySubject
  - param `pIActivitySubject`:
