<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# POSDailySummaryService (Object)

POSDailySummaryService Class

## Methods (7)
- `Public Function Add(ByVal pIPOSDailySummary As POSDailySummary) As POSDailySummaryParams` Add
  - param `pIPOSDailySummary`: 
- `Public Sub Delete(ByVal pIPOSDailySummaryParams As POSDailySummaryParams)` Delete
  - param `pIPOSDailySummaryParams`: 
- `Public Function Get(ByVal pIPOSDailySummaryParams As POSDailySummaryParams) As POSDailySummary` Get
  - param `pIPOSDailySummaryParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As POSDailySummaryServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/POSDailySummaryServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pIPOSDailySummary As POSDailySummary)` Update
  - param `pIPOSDailySummary`:
