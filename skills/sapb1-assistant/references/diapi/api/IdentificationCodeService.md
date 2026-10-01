<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# IdentificationCodeService (Object)

IdentificationCodeService Class

## Methods (8)
- `Public Function Add(ByVal pIIdentificationCode As IdentificationCode) As IdentificationCodeParams` Add
  - param `pIIdentificationCode`: 
- `Public Function GetByParams(ByVal pIIdentificationCodeParams As IdentificationCodeParams) As IdentificationCode` GetByParams
  - param `pIIdentificationCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IdentificationCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/IdentificationCodeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As IdentificationCodes` GetList
- `Public Sub Remove(ByVal pIIdentificationCodeParams As IdentificationCodeParams)` Remove
  - param `pIIdentificationCodeParams`: 
- `Public Sub Update(ByVal pIIdentificationCode As IdentificationCode)` Update
  - param `pIIdentificationCode`:
