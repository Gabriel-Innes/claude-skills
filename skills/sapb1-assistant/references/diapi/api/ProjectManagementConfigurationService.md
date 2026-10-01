<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProjectManagementConfigurationService (Object)

ProjectManagementConfigurationService Class

## Methods (27)
- `Public Sub AddActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)` AddActivities
  - param `pIPMC_ActivityCollection`: 
- `Public Sub AddAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)` AddAreas
  - param `pIPMC_AreaCollection`: 
- `Public Sub AddPriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)` AddPriorities
  - param `pIPMC_PriorityCollection`: 
- `Public Sub AddStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)` AddStageTypes
  - param `pIPMC_StageTypeCollection`: 
- `Public Sub AddSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)` AddSubprojectTypes
  - param `pIPMC_SubprojectTypesCollection`: 
- `Public Sub AddTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)` AddTasks
  - param `pIPMC_TaskCollection`: 
- `Public Sub DeleteActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)` DeleteActivities
  - param `pIPMC_ActivityCollection`: 
- `Public Sub DeleteAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)` DeleteAreas
  - param `pIPMC_AreaCollection`: 
- `Public Sub DeletePriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)` DeletePriorities
  - param `pIPMC_PriorityCollection`: 
- `Public Sub DeleteStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)` DeleteStageTypes
  - param `pIPMC_StageTypeCollection`: 
- `Public Sub DeleteSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)` DeleteSubprojectTypes
  - param `pIPMC_SubprojectTypesCollection`: 
- `Public Sub DeleteTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)` DeleteTasks
  - param `pIPMC_TaskCollection`: 
- `Public Function GetActivities() As PMC_ActivityCollection` GetActivities
- `Public Function GetAreas() As PMC_AreaCollection` GetAreas
- `Public Function GetDataInterface(ByVal enumMSDI As ProjectManagementConfigurationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ProjectManagementConfigurationServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetPriorities() As PMC_PriorityCollection` GetPriorities
- `Public Function GetStageTypes() As PMC_StageTypeCollection` GetStageTypes
- `Public Function GetSubprojectTypes() As PMC_SubprojectTypesCollection` GetSubprojectTypes
- `Public Function GetTasks() As PMC_TaskCollection` GetTasks
- `Public Sub UpdateActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)` UpdateActivities
  - param `pIPMC_ActivityCollection`: 
- `Public Sub UpdateAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)` UpdateAreas
  - param `pIPMC_AreaCollection`: 
- `Public Sub UpdatePriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)` UpdatePriorities
  - param `pIPMC_PriorityCollection`: 
- `Public Sub UpdateStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)` UpdateStageTypes
  - param `pIPMC_StageTypeCollection`: 
- `Public Sub UpdateSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)` UpdateSubprojectTypes
  - param `pIPMC_SubprojectTypesCollection`: 
- `Public Sub UpdateTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)` UpdateTasks
  - param `pIPMC_TaskCollection`:
