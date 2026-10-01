<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MobileAddOnSettingService (Object)

MobileAddOnSettingService Class

## Methods (8)
- `Public Function AddMobileAddOnSetting(ByVal pIMobileAddOnSetting As MobileAddOnSetting) As MobileAddOnSettingParams` AddMobileAddOnSetting
  - param `pIMobileAddOnSetting`: 
- `Public Sub DeleteMobileAddOnSetting(ByVal pIMobileAddOnSettingParams As MobileAddOnSettingParams)` DeleteMobileAddOnSetting
  - param `pIMobileAddOnSettingParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As MobileAddOnSettingServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/MobileAddOnSettingServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetMobileAddOnSetting(ByVal pIMobileAddOnSettingParams As MobileAddOnSettingParams) As MobileAddOnSetting` GetMobileAddOnSetting
  - param `pIMobileAddOnSettingParams`: 
- `Public Function GetMobileAddOnSettingList() As MobileAddOnSettingParamsCollection` GetMobileAddOnSettingList
- `Public Sub UpdateMobileAddOnSetting(ByVal pIMobileAddOnSetting As MobileAddOnSetting)` UpdateMobileAddOnSetting
  - param `pIMobileAddOnSetting`:
