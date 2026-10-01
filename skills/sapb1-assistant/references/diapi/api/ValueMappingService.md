<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ValueMappingService (Object)

ValueMappingService Class

## Methods (10)
- `Public Function AddVMObject(ByVal pIVM_B1ValuesData As VM_B1ValuesData) As ValueMappingParams` AddVMObject
  - param `pIVM_B1ValuesData`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ValueMappingServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ValueMappingServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetMappedB1Value(ByVal pIVM_B1ValuesData As VM_B1ValuesData) As VM_B1ValuesCollection` GetMappedB1Value
  - param `pIVM_B1ValuesData`: 
- `Public Function GetThirdPartyValuesForB1Value(ByVal pIVM_B1ValuesData As VM_B1ValuesData) As VM_ThirdPartyValuesCollection` GetThirdPartyValuesForB1Value
  - param `pIVM_B1ValuesData`: 
- `Public Function GetVMObject(ByVal pIValueMappingParams As ValueMappingParams) As VM_B1ValuesData` GetVMObject
  - param `pIValueMappingParams`: 
- `Public Sub RemoveMappedValue(ByVal pIVM_ThirdPartyValuesData As VM_ThirdPartyValuesData)` RemoveMappedValue
  - param `pIVM_ThirdPartyValuesData`: 
- `Public Sub RemoveVMObject(ByVal pIValueMappingParams As ValueMappingParams)` RemoveVMObject
  - param `pIValueMappingParams`: 
- `Public Sub UpdateVMObject(ByVal pIVM_B1ValuesData As VM_B1ValuesData)` UpdateVMObject
  - param `pIVM_B1ValuesData`:
