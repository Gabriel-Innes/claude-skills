<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RecurringPostingsService (Object)

RecurringPostingsService Class

## Methods (8)
- `Public Function Add(ByVal pIRecurringPostings As RecurringPostings) As RecurringPostingsParams` Add
  - param `pIRecurringPostings`: 
- `Public Sub Delete(ByVal pIRecurringPostingsParams As RecurringPostingsParams)` Delete
  - param `pIRecurringPostingsParams`: 
- `Public Function Get(ByVal pIRecurringPostingsParams As RecurringPostingsParams) As RecurringPostings` Get
  - param `pIRecurringPostingsParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As RecurringPostingsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/RecurringPostingsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As RecurringPostingsParamsCollection` GetList
- `Public Sub Update(ByVal pIRecurringPostings As RecurringPostings)` Update
  - param `pIRecurringPostings`:
