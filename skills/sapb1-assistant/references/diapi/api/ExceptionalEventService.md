<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExceptionalEventService (Object)

Source table: OEPE.

**Remarks:** For the Italy localization only. Navigation path: Business Partner Master Data → Accounting → Tax, select the checkbox Subject to Withholding Tax and go to the field Exceptional Event.

## Methods (8)
- `Public Function AddExceptionalEvent(ByVal pIExceptionalEvent As ExceptionalEvent) As ExceptionalEventParams` AddExceptionalEvent
  - param `pIExceptionalEvent`: 
- `Public Sub DeleteExceptionalEvent(ByVal pIExceptionalEventParams As ExceptionalEventParams)` DeleteExceptionalEvent
  - param `pIExceptionalEventParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExceptionalEventServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ExceptionalEventServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetExceptionalEvent(ByVal pIExceptionalEventParams As ExceptionalEventParams) As ExceptionalEvent` GetExceptionalEvent
  - param `pIExceptionalEventParams`: 
- `Public Function GetExceptionalEventList() As ExceptionalEventsParams` GetExceptionalEventList
- `Public Sub UpdateExceptionalEvent(ByVal pIExceptionalEvent As ExceptionalEvent)` UpdateExceptionalEvent
  - param `pIExceptionalEvent`:
