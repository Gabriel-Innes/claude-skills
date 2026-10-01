<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPVatExemptionsService (Object)

BPVatExemptionsService Class

## Methods (8)
- `Public Function Add(ByVal pIBPVatExemptions As BPVatExemptions) As BPVatExemptionsParams` Add
  - param `pIBPVatExemptions`: 
- `Public Sub Delete(ByVal pIBPVatExemptionsParams As BPVatExemptionsParams)` Delete
  - param `pIBPVatExemptionsParams`: 
- `Public Function Get(ByVal pIBPVatExemptionsParams As BPVatExemptionsParams) As BPVatExemptions` Get
  - param `pIBPVatExemptionsParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BPVatExemptionsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BPVatExemptionsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As BPVatExemptionsParamsCollection` GetList
- `Public Sub Update(ByVal pIBPVatExemptions As BPVatExemptions)` Update
  - param `pIBPVatExemptions`:
