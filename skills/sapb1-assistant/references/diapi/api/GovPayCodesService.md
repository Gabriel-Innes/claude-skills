<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# GovPayCodesService (Object)

GovPayCodesService Class

## Methods (8)
- `Public Function Add(ByVal pIGovPayCode As GovPayCode) As GovPayCodeParams` Add
  - param `pIGovPayCode`: 
- `Public Sub Delete(ByVal pIGovPayCodeParams As GovPayCodeParams)` Delete
  - param `pIGovPayCodeParams`: 
- `Public Function Get(ByVal pIGovPayCodeParams As GovPayCodeParams) As GovPayCode` Get
  - param `pIGovPayCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As GovPayCodesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/GovPayCodesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As GovPayCodeParamsCollection` GetList
- `Public Sub Update(ByVal pIGovPayCode As GovPayCode)` Update
  - param `pIGovPayCode`:
