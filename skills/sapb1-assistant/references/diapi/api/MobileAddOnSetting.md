<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MobileAddOnSetting (Object)

MobileAddOnSetting Class

## Properties (11)
- `Public Property B1MobileApp() As BoYesNoEnum` [R/W] property B1MobileApp
- `Public Property B1SalesApp() As BoYesNoEnum` [R/W] property B1SalesApp
- `Public Property B1ServiceApp() As BoYesNoEnum` [R/W] property B1ServiceApp
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property Enable() As BoYesNoEnum` [R/W] property Enable
- `Public Property LogonMethod() As LogonMethodEnum` [R/W] property LogonMethod
- `Public Property Provider() As String` [R/W] property Provider
- `Public Property Type() As MobileAddonSettingTypeEnum` [R/W] property Type
- `Public Property Url() As String` [R/W] property Url
- `Public Property ViewStyle() As ViewStyleTypeEnum` [R/W] property ViewStyle

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
