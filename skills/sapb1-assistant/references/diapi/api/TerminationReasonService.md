<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TerminationReasonService (Object)

TerminationReasonService Class

## Methods (8)
- `Public Function Add(ByVal pITerminationReason As TerminationReason) As TerminationReasonParams` Add
  - param `pITerminationReason`: 
- `Public Sub Delete(ByVal pITerminationReasonParams As TerminationReasonParams)` Delete
  - param `pITerminationReasonParams`: 
- `Public Function Get(ByVal pITerminationReasonParams As TerminationReasonParams) As TerminationReason` Get
  - param `pITerminationReasonParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TerminationReasonServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TerminationReasonServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As TerminationReasonParamsCollection` GetList
- `Public Sub Update(ByVal pITerminationReason As TerminationReason)` Update
  - param `pITerminationReason`:
