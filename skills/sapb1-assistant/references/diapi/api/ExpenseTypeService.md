<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExpenseTypeService (Object)

ExpenseTypeService Class

## Methods (6)
- `Public Function Add(ByVal pIExpenseTypeData As ExpenseTypeData) As ExpenseTypeParams` Add
  - param `pIExpenseTypeData`: 
- `Public Function Get(ByVal pIExpenseTypeParams As ExpenseTypeParams) As ExpenseTypeData` Get
  - param `pIExpenseTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExpenseTypeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ExpenseTypeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pIExpenseTypeData As ExpenseTypeData)` Update
  - param `pIExpenseTypeData`:
