<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MobileAppService (Object)

MobileAppService Class

## Methods (17)
- `Public Function GetCurrentServerDateTime() As MobileServerDateTime` GetCurrentServerDateTime
- `Public Function GetDataInterface(ByVal enumMSDI As MobileAppServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/MobileAppServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDppChangeParams(ByVal pDppChangeParams As DppChangeParams) As DppChangeParams` GetDppChangeParams
  - param `pDppChangeParams`: 
- `Public Function GetEmployeeFullNames(ByVal pEmployeeFullNamesParamsCollection As EmployeeFullNamesParamsCollection) As EmployeeFullNamesParamsCollection` GetFullEmployeeNames
  - param `pEmployeeFullNamesParamsCollection`: 
- `Public Function GetSalesAppSetting(ByVal pSalesAppSettingParams As SalesAppSettingParams) As SalesAppSetting` GetSalesAppSetting
  - param `pSalesAppSettingParams`: 
- `Public Function GetServiceAppReport(ByVal pServiceAppReportParams As ServiceAppReportParams) As ServiceAppReport` GetServiceAppReport
  - param `pServiceAppReportParams`: 
- `Public Function GetServiceAppReportContent(ByVal pServiceAppReportParams As ServiceAppReportParams) As ServiceAppReportContent` GetServiceAppReportContent
  - param `pServiceAppReportParams`: 
- `Public Function GetTechnicianSchedulings(ByVal pITechnicianSchedulingsParams As TechnicianSchedulingsParams) As TechnicianSchedulingsCollection` GetTechnicianSchedulings
  - param `pITechnicianSchedulingsParams`: 
- `Public Function GetTechnicianSettings(ByVal pTechnicianSettingsParams As TechnicianSettingsParams) As TechnicianSettings` GetTechnicianSettings
  - param `pTechnicianSettingsParams`: 
- `Public Function GetTechnicianSettingsGroup(ByVal pTechnicianSettingsGroupParams As TechnicianSettingsGroupParams) As TechnicianSettingsGroup` GetTechnicianSettingsGroup
  - param `pTechnicianSettingsGroupParams`: 
- `Public Sub UpdateSalesAppSetting(ByVal pSalesAppSetting As SalesAppSetting)` UpdateSalesAppSetting
  - param `pSalesAppSetting`: 
- `Public Sub UpdateServiceAppReport(ByVal pServiceAppReport As ServiceAppReport)` UpdateServiceAppReport
  - param `pServiceAppReport`: 
- `Public Sub UpdateServiceAppReportContent(ByVal pServiceAppReportParams As ServiceAppReportParams, ByVal pServiceAppReportContent As ServiceAppReportContent)` UpdateServiceAppReportContent
  - param `pServiceAppReportParams`: 
  - param `pServiceAppReportContent`: 
- `Public Sub UpdateTechnicianSettings(ByVal ppTechnicianSettings As TechnicianSettings)` UpdateTechnicianSettings
  - param `ppTechnicianSettings`: 
- `Public Sub UpdateTechnicianSettingsGroup(ByVal pTechnicianSettingsGroup As TechnicianSettingsGroup)` UpdateTechnicianSettingsGroup
  - param `pTechnicianSettingsGroup`:
