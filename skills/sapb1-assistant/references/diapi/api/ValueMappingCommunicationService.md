<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ValueMappingCommunicationService (Object)

ValueMappingCommunicationService Class

## Methods (6)
- `Public Function AddVMCommunicationObject(ByVal pIValueMappingCommunicationData As ValueMappingCommunicationData) As ValueMappingCommunicationParams` AddVMCommunicationObject
  - param `pIValueMappingCommunicationData`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ValueMappingCommunicationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ValueMappingCommunicationServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetVMCommunicationObject(ByVal pIValueMappingCommunicationParams As ValueMappingCommunicationParams) As ValueMappingCommunicationData` GetVMCommunicationObject
  - param `pIValueMappingCommunicationParams`: 
- `Public Sub UpdateVMCommunicationObject(ByVal pIValueMappingCommunicationData As ValueMappingCommunicationData)` UpdateVMCommunicationObject
  - param `pIValueMappingCommunicationData`:
