<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeStatusService (Object)

EmployeeStatusService Class

## Methods (8)
- `Public Function Add(ByVal pIEmployeeStatus As EmployeeStatus) As EmployeeStatusParams` Add
  - param `pIEmployeeStatus`: 
- `Public Sub Delete(ByVal pIEmployeeStatusParams As EmployeeStatusParams)` Delete
  - param `pIEmployeeStatusParams`: 
- `Public Function Get(ByVal pIEmployeeStatusParams As EmployeeStatusParams) As EmployeeStatus` Get
  - param `pIEmployeeStatusParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeeStatusServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EmployeeStatusServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EmployeeStatusParamsCollection` GetList
- `Public Sub Update(ByVal pIEmployeeStatus As EmployeeStatus)` Update
  - param `pIEmployeeStatus`:
