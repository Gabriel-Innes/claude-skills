<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# QRCodeService (Object)

QRCodeService Class

## Methods (4)
- `Public Sub AddOrUpdateQRCode(ByVal pIQRCodeData As QRCodeData)` AddOrUpdateQRCode
  - param `pIQRCodeData`: 
- `Public Function GetDataInterface(ByVal enumMSDI As QRCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/QRCodeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`:
