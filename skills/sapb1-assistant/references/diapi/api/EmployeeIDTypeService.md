<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeIDTypeService (Object)

EmployeeIDTypeService Class

## Methods (8)
- `Public Function Add(ByVal pIEmployeeIDType As EmployeeIDType) As EmployeeIDTypeParams` Add
  - param `pIEmployeeIDType`: 
- `Public Sub Delete(ByVal pIEmployeeIDTypeParams As EmployeeIDTypeParams)` Delete
  - param `pIEmployeeIDTypeParams`: 
- `Public Function Get(ByVal pIEmployeeIDTypeParams As EmployeeIDTypeParams) As EmployeeIDType` Get
  - param `pIEmployeeIDTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeeIDTypeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EmployeeIDTypeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EmployeeIDTypeParamsCollection` GetList
- `Public Sub Update(ByVal pIEmployeeIDType As EmployeeIDType)` Update
  - param `pIEmployeeIDType`:
