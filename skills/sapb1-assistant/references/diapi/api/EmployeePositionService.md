<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeePositionService (Object)

EmployeePositionService Class

## Methods (8)
- `Public Function Add(ByVal pIEmployeePosition As EmployeePosition) As EmployeePositionParams` Add
  - param `pIEmployeePosition`: 
- `Public Sub Delete(ByVal pIEmployeePositionParams As EmployeePositionParams)` Delete
  - param `pIEmployeePositionParams`: 
- `Public Function Get(ByVal pIEmployeePositionParams As EmployeePositionParams) As EmployeePosition` Get
  - param `pIEmployeePositionParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeePositionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EmployeePositionServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EmployeePositionParamsCollection` GetList
- `Public Sub Update(ByVal pIEmployeePosition As EmployeePosition)` Update
  - param `pIEmployeePosition`:
