<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# OccurrenceCodesService (Object)

OccurrenceCodesService Class

## Methods (8)
- `Public Function Add(ByVal pIOccurenceCode As OccurenceCode) As OccurenceCodeParams` Add
  - param `pIOccurenceCode`: 
- `Public Sub Delete(ByVal pIOccurenceCodeParams As OccurenceCodeParams)` Delete
  - param `pIOccurenceCodeParams`: 
- `Public Function Get(ByVal pIOccurenceCodeParams As OccurenceCodeParams) As OccurenceCode` Get
  - param `pIOccurenceCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As OccurrenceCodesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/OccurrenceCodesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As OccurenceCodeParamsCollection` GetList
- `Public Sub Update(ByVal pIOccurenceCode As OccurenceCode)` Update
  - param `pIOccurenceCode`:
