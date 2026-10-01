<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TrackingNotesService (Object)

TrackingNotesService Class

## Methods (8)
- `Public Function Add(ByVal pITrackingNote As TrackingNote) As TrackingNoteParams` Add
  - param `pITrackingNote`: 
- `Public Sub Delete(ByVal pITrackingNoteParams As TrackingNoteParams)` Delete
  - param `pITrackingNoteParams`: 
- `Public Function Get(ByVal pITrackingNoteParams As TrackingNoteParams) As TrackingNote` Get
  - param `pITrackingNoteParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TrackingNotesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TrackingNotesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As TrackingNoteParamsCollection` GetList
- `Public Sub Update(ByVal pITrackingNote As TrackingNote)` Update
  - param `pITrackingNote`:
