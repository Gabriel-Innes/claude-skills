<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ActivityRecipientListsService (Object)

ActivityRecipientListsService Class

## Methods (8)
- `Public Function Add(ByVal pIActivityRecipientList As ActivityRecipientList) As ActivityRecipientListParams` Add
  - param `pIActivityRecipientList`: 
- `Public Sub Delete(ByVal pIActivityRecipientListParams As ActivityRecipientListParams)` Delete
  - param `pIActivityRecipientListParams`: 
- `Public Function Get(ByVal pIActivityRecipientListParams As ActivityRecipientListParams) As ActivityRecipientList` Get
  - param `pIActivityRecipientListParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ActivityRecipientListsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ActivityRecipientListsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As ActivityRecipientListParamsCollection` GetList
- `Public Sub Update(ByVal pIActivityRecipientList As ActivityRecipientList)` Update
  - param `pIActivityRecipientList`:
