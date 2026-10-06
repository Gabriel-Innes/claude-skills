<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# DAC-based OData metadata: type index

One row per EntityType / ComplexType. Open the entry with the `File`, `Line` and `Lines` columns (a line-range read of `api/<File>`), or grep `api/members-*.md` for `^<Type>\.`. A type with a BaseType lists only the fields it adds; its key and the rest of its fields are those of the base type (the entry says which type declares the key).

| Type | Kind | Label | Key | Fields | Navigation | BaseType | Entity sets | File | Line | Lines |
|---|---|---|---|---:|---:|---|---|---|---:|---:|
| PX.AI.Tools.DAC.AIToolDefinition | EntityType | AI Tool | ToolID | 2 | 1 |  | PX_AI_Tools_DAC_AIToolDefinition, AITool, AIToolDefinition | members-01.md | 3 | 9 |
| PX.AI.Tools.GI.DAC.AIGIToolDefinition | EntityType |  | ToolID | 3 | 3 |  | PX_AI_Tools_GI_DAC_AIGIToolDefinition | members-01.md | 13 | 11 |
| PX.AIStudio.DAC.LLMConnection | EntityType | Agent LLM Connection | ConnectionID | 13 | 6 |  | PX_AIStudio_DAC_LLMConnection, AgentLLMConnection, LLMConnection | members-01.md | 25 | 26 |
| PX.AIStudio.DAC.LLMConnectionParameter | EntityType | Agent LLM Connection Parameter | ConnectionID, ParameterID | 17 | 3 |  | PX_AIStudio_DAC_LLMConnectionParameter, AgentLLMConnectionParameter, LLMConnectionParameter | members-01.md | 52 | 27 |
| PX.AIStudio.DAC.LLMPrompt | EntityType | Agent | PromptID | 19 | 9 |  | PX_AIStudio_DAC_LLMPrompt, Agent, LLMPrompt | members-01.md | 80 | 35 |
| PX.AIStudio.DAC.LLMPromptSystemInstruction | EntityType | Agent System Instruction Assignment | PromptID, PromptInstructionID | 12 | 4 |  | PX_AIStudio_DAC_LLMPromptSystemInstruction, AgentSystemInstructionAssignment, LLMPromptSystemInstruction | members-01.md | 116 | 22 |
| PX.AIStudio.DAC.LLMPromptTesting | EntityType | Agent Testing | PromptID | 7 | 1 |  | PX_AIStudio_DAC_LLMPromptTesting, AgentTesting, LLMPromptTesting | members-01.md | 139 | 15 |
| PX.AIStudio.DAC.LLMPromptTestingLog | EntityType | Agent Testing Log | EventID, PromptID | 4 | 1 |  | PX_AIStudio_DAC_LLMPromptTestingLog, AgentTestingLog, LLMPromptTestingLog | members-01.md | 155 | 11 |
| PX.AIStudio.DAC.LLMPromptTool | EntityType | Agent Tool | AIToolDefinitionToolID, PromptID, ToolID | 18 | 4 |  | PX_AIStudio_DAC_LLMPromptTool, AgentTool, LLMPromptTool | members-01.md | 167 | 29 |
| PX.AIStudio.DAC.LLMPromptToolCBApiCurrent | EntityType | Agent Tool CB API Current | PromptID, ToolID | 5 | 3 |  | PX_AIStudio_DAC_LLMPromptToolCBApiCurrent, AgentToolCBAPICurrent, LLMPromptToolCBApiCurrent | members-01.md | 197 | 14 |
| PX.AIStudio.DAC.LLMProvider | EntityType | LLM Provider | ProviderID | 11 | 4 |  | PX_AIStudio_DAC_LLMProvider, LLMProvider | members-01.md | 212 | 22 |
| PX.AIStudio.DAC.LLMProviderParameter | EntityType | LLM Provider Parameter | ParameterID, ProviderID | 13 | 3 |  | PX_AIStudio_DAC_LLMProviderParameter, LLMProviderParameter | members-01.md | 235 | 22 |
| PX.AIStudio.DAC.LLMRequestHistory | EntityType | AI Automation History Record | RequestID | 21 | 2 |  | PX_AIStudio_DAC_LLMRequestHistory, AIAutomationHistoryRecord, LLMRequestHistory | members-01.md | 258 | 30 |
| PX.AIStudio.DAC.LLMSystemInstruction | EntityType | Agent System Instruction | InstructionID | 12 | 3 |  | PX_AIStudio_DAC_LLMSystemInstruction, AgentSystemInstruction, LLMSystemInstruction | members-01.md | 289 | 21 |
| PX.Api.ContractBased.UI.DAC.EntityEndpoint | EntityType |  | GateVersion, InterfaceName | 5 | 2 |  | PX_Api_ContractBased_UI_DAC_EntityEndpoint | members-01.md | 311 | 12 |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModel | EntityType |  | ModelID | 3 | 1 |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModel | members-01.md | 324 | 9 |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelField | EntityType |  | FieldName, ModelID | 4 | 0 |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelField | members-01.md | 334 | 9 |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping | EntityType |  | MappedFieldName, MappingID | 6 | 1 |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelFieldMapping | members-01.md | 344 | 12 |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping | EntityType |  | MappingID | 8 | 3 |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelMapping | members-01.md | 357 | 16 |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping | EntityType |  | MappingID, ScreenID, ViewName | 6 | 1 |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelScreenMapping | members-01.md | 374 | 12 |
| PX.Api.Mobile.MultiFactorAuth.DAC.MobileOtpSecret | EntityType |  | AccountID, ApplicationInstanceID | 3 | 0 |  | PX_Api_Mobile_MultiFactorAuth_DAC_MobileOtpSecret | members-01.md | 387 | 8 |
| PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode | EntityType |  | Code, UserId | 3 | 0 |  | PX_Api_Mobile_MultiFactorAuth_DAC_MultiFactorPersistentCode | members-01.md | 396 | 8 |
| PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCodeWithCompany | EntityType |  | Code, UserId | 1 | 0 | PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode | PX_Api_Mobile_MultiFactorAuth_DAC_MultiFactorPersistentCodeWithCompany | members-01.md | 405 | 7 |
| PX.Api.Mobile.PushNotifications.DAC.MobileDevice | EntityType |  | AccountID, ApplicationInstanceID | 13 | 0 |  | PX_Api_Mobile_PushNotifications_DAC_MobileDevice | members-01.md | 413 | 18 |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems | EntityType |  | NoteID, Owner | 16 | 2 |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceItems | members-01.md | 432 | 24 |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder | EntityType |  | ItemID, ItemOwner, ItemType, Owner | 16 | 2 |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceItemsOrder | members-01.md | 457 | 24 |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder | EntityType |  |  | 13 | 2 |  |  | members-01.md | 482 | 19 |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder | EntityType |  | DashboardID, Owner, WidgetID, WidgetOwner | 16 | 2 |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsOrder | members-01.md | 502 | 24 |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2 | EntityType |  | NoteID, Owner | 15 | 2 |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsV2 | members-01.md | 527 | 23 |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order | EntityType |  | DashboardID, Owner, WidgetID, WidgetOwner | 16 | 2 |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsV2Order | members-01.md | 551 | 24 |
| PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces | EntityType |  | Name | 15 | 2 |  | PX_Api_Mobile_Workspaces_MobileSiteMapWorkspaces | members-01.md | 576 | 23 |
| PX.Api.ModelContextProtocol.UI.DAC.McpServer | EntityType | MCP Server | Name | 7 | 0 |  | PX_Api_ModelContextProtocol_UI_DAC_McpServer, MCPServer | members-01.md | 600 | 14 |
| PX.Api.ModelContextProtocol.UI.DAC.McpServerTool | EntityType | MCP Tool | McpServerID, ToolID | 6 | 0 |  | PX_Api_ModelContextProtocol_UI_DAC_McpServerTool, MCPTool, McpServerTool | members-01.md | 615 | 12 |
| PX.Api.ModelContextProtocol.UI.DAC.McpServerToolProjection | EntityType | MCP Tool | McpServerID, ToolID | 2 | 0 | PX.Api.ModelContextProtocol.UI.DAC.McpServerTool | PX_Api_ModelContextProtocol_UI_DAC_McpServerToolProjection | members-01.md | 628 | 9 |
| PX.Api.OData.DAC.DeletedRecordResult | ComplexType |  |  | 2 | 0 |  |  | members-01.md | 638 | 5 |
| PX.Api.SYData | EntityType |  | LineNbr, MappingID | 20 | 3 |  | PX_Api_SYData | members-01.md | 644 | 29 |
| PX.Api.SYHistory | EntityType |  | MappingID, StatusDate | 12 | 1 |  | PX_Api_SYHistory | members-01.md | 674 | 19 |
| PX.Api.SYImportCondition | EntityType |  | LineNbr, MappingID | 19 | 3 |  | PX_Api_SYImportCondition | members-01.md | 694 | 28 |
| PX.Api.SYMapping | EntityType | Mapping | Name | 48 | 16 |  | PX_Api_SYMapping, Mapping, SYMapping | members-01.md | 723 | 71 |
| PX.Api.SYMappingActive | EntityType | Mapping | Name | 2 | 0 | PX.Api.SYMapping | PX_Api_SYMappingActive | members-01.md | 795 | 10 |
| PX.Api.SYMappingActiveFilter | EntityType | Mapping | Name | 0 | 0 | PX.Api.SYMappingActive | PX_Api_SYMappingActiveFilter | members-01.md | 806 | 6 |
| PX.Api.SYMappingCondition | EntityType |  | LineNbr, MappingID | 22 | 3 |  | PX_Api_SYMappingCondition | members-01.md | 813 | 31 |
| PX.Api.SYMappingField | EntityType |  | LineNbr, MappingID | 25 | 3 |  | PX_Api_SYMappingField | members-01.md | 845 | 34 |
| PX.Api.SYMappingFieldSimple | EntityType |  | LineNbr, MappingID | 1 | 0 | PX.Api.SYMappingField | PX_Api_SYMappingFieldSimple | members-01.md | 880 | 8 |
| PX.Api.SYProvider | EntityType | Provider | Name | 15 | 5 |  | PX_Api_SYProvider, Provider, SYProvider | members-01.md | 889 | 27 |
| PX.Api.SYProviderField | EntityType |  | Name, ObjectName, ProviderID | 20 | 3 |  | PX_Api_SYProviderField | members-01.md | 917 | 29 |
| PX.Api.SYProviderObject | EntityType | Provider Object | LineNbr, ProviderID | 17 | 5 |  | PX_Api_SYProviderObject, ProviderObject, SYProviderObject | members-01.md | 947 | 29 |
| PX.Api.SYServiceSchema | EntityType |  | ScreenID, ServiceID | 10 | 1 |  | PX_Api_SYServiceSchema | members-01.md | 977 | 17 |
| PX.Api.SYSubstitution | EntityType |  | SubstitutionID | 4 | 4 |  | PX_Api_SYSubstitution | members-01.md | 995 | 13 |
| PX.Api.SYSubstitutionValues | EntityType |  | SubstitutionID, ValueID | 5 | 1 |  | PX_Api_SYSubstitutionValues | members-01.md | 1009 | 11 |
| PX.Api.SYWebService | EntityType |  | ServiceID | 13 | 1 |  | PX_Api_SYWebService | members-01.md | 1021 | 20 |
| PX.Api.Webhooks.DAC.WebHook | EntityType |  | Name | 17 | 5 |  | PX_Api_Webhooks_DAC_WebHook | members-01.md | 1042 | 28 |
| PX.Api.Webhooks.WebHookRequest | EntityType |  | RequestID, WebHookID | 10 | 0 |  | PX_Api_Webhooks_WebHookRequest | members-01.md | 1071 | 15 |
| PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun | EntityType | GeneratorRun | RunId, UserId | 9 | 1 |  | PX_AutocompleteGenerator_UI_DAC_AutocompleteGeneratorRun, GeneratorRun, AutocompleteGeneratorRun | members-01.md | 1087 | 17 |
| PX.AutocompleteGenerator.UI.DAC.LastRunOfUser | EntityType | GeneratorRun | RunId, UserId | 0 | 0 | PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun | PX_AutocompleteGenerator_UI_DAC_LastRunOfUser | members-01.md | 1105 | 6 |
| PX.BusinessProcess.DAC.ActionExecution | EntityType | Action Execution | ExecutionID | 18 | 6 |  | PX_BusinessProcess_DAC_ActionExecution, ActionExecution | members-01.md | 1112 | 31 |
| PX.BusinessProcess.DAC.ActionExecutionMapping | EntityType | Action Execution Mapping | ExecutionID, LineNbr | 14 | 3 |  | PX_BusinessProcess_DAC_ActionExecutionMapping, ActionExecutionMapping | members-01.md | 1144 | 24 |
| PX.BusinessProcess.DAC.ActionExecutionParameter | EntityType | Action Execution Parameter | ExecutionID, LineNbr | 14 | 3 |  | PX_BusinessProcess_DAC_ActionExecutionParameter, ActionExecutionParameter | members-01.md | 1169 | 23 |
| PX.BusinessProcess.DAC.BPEvent | EntityType | Business Process Event | Name | 29 | 10 |  | PX_BusinessProcess_DAC_BPEvent, BusinessProcessEvent, BPEvent | members-01.md | 1193 | 46 |
| PX.BusinessProcess.DAC.BPEventHistory | EntityType | Business Process Event History | EventDefinitionID, EventID | 12 | 1 |  | PX_BusinessProcess_DAC_BPEventHistory, BusinessProcessEventHistory, BPEventHistory | members-01.md | 1240 | 20 |
| PX.BusinessProcess.DAC.BPEventSchedule | EntityType | Business Process Event Schedule | EventID, ScheduleID | 4 | 2 |  | PX_BusinessProcess_DAC_BPEventSchedule, BusinessProcessEventSchedule, BPEventSchedule | members-01.md | 1261 | 13 |
| PX.BusinessProcess.DAC.BPEventSetting | EntityType |  |  | 2 | 0 |  |  | members-01.md | 1275 | 6 |
| PX.BusinessProcess.DAC.BPEventSubscriber | EntityType | Business Process Event Subscriber | EventID, HandlerID, Type | 12 | 6 |  | PX_BusinessProcess_DAC_BPEventSubscriber, BusinessProcessEventSubscriber, BPEventSubscriber | members-01.md | 1282 | 25 |
| PX.BusinessProcess.DAC.BPEventTrackingField | EntityType | Business Process Tracked Field | EventID, FieldID | 6 | 1 |  | PX_BusinessProcess_DAC_BPEventTrackingField, BusinessProcessTrackedField, BPEventTrackingField | members-01.md | 1308 | 14 |
| PX.BusinessProcess.DAC.BPEventTriggerCondition | EntityType | Business Process Event Trigger Condition | EventID, OrderNbr | 14 | 1 |  | PX_BusinessProcess_DAC_BPEventTriggerCondition, BusinessProcessEventTriggerCondition, BPEventTriggerCondition | members-01.md | 1323 | 21 |
| PX.BusinessProcess.DAC.BPInquiryParameter | EntityType | Business Process Inquiry Parameter | EventID, Name | 7 | 1 |  | PX_BusinessProcess_DAC_BPInquiryParameter, BusinessProcessInquiryParameter, BPInquiryParameter | members-01.md | 1345 | 15 |
| PX.BusinessProcess.DAC.BPProcessedEventSubscribers | EntityType |  | Id | 4 | 0 |  | PX_BusinessProcess_DAC_BPProcessedEventSubscribers | members-01.md | 1361 | 9 |
| PX.BusinessProcess.DAC.DispatcherStatisticEventDetail | EntityType | DispatcherStatisticEventDetail | BusinessEventName, Id | 3 | 0 |  | PX_BusinessProcess_DAC_DispatcherStatisticEventDetail, DispatcherStatisticEventDetail | members-01.md | 1371 | 9 |
| PX.BusinessProcess.DAC.DispatcherStatus | EntityType |  | QueueType, WebsiteID | 16 | 0 |  | PX_BusinessProcess_DAC_DispatcherStatus | members-01.md | 1381 | 22 |
| PX.BusinessProcess.DAC.MobileNotification | EntityType | Mobile Notification | NotificationID | 22 | 7 |  | PX_BusinessProcess_DAC_MobileNotification, MobileNotification | members-01.md | 1404 | 36 |
| PX.BusinessProcess.DAC.QueueNotificationSettings | EntityType | Notification Settings | SettingID | 21 | 5 |  | PX_BusinessProcess_DAC_QueueNotificationSettings, NotificationSettings, QueueNotificationSettings | members-01.md | 1441 | 33 |
| PX.CloudServices.DAC.RecognizedRecord | EntityType | Recognized Record | EntityType, RefNbr | 30 | 3 |  | PX_CloudServices_DAC_RecognizedRecord, RecognizedRecord1 | members-01.md | 1475 | 40 |
| PX.CloudServices.DAC.RecognizedRecordProjection | EntityType | Recognized Record | EntityType, RefNbr | 4 | 0 | PX.CloudServices.DAC.RecognizedRecord | PX_CloudServices_DAC_RecognizedRecordProjection, RecognizedRecord, RecognizedRecordProjection | members-01.md | 1516 | 11 |
| PX.Commerce.Amazon.BCAmazonTaxMapping | EntityType | BCAmazonTaxMapping | BindingID, TaxMappingID | 15 | 5 |  | PX_Commerce_Amazon_BCAmazonTaxMapping, BCAmazonTaxMapping | members-01.md | 1528 | 26 |
| PX.Commerce.Amazon.BCBindingAmazon | EntityType | Amazon Settings | BindingID | 28 | 18 |  | PX_Commerce_Amazon_BCBindingAmazon, AmazonSettings, BCBindingAmazon | members-01.md | 1555 | 52 |
| PX.Commerce.BigCommerce.BCBindingBigCommerce | EntityType | BigCommerce Settings | BindingID | 20 | 4 |  | PX_Commerce_BigCommerce_BCBindingBigCommerce, BigCommerceSettings, BCBindingBigCommerce | members-01.md | 1608 | 30 |
| PX.Commerce.Core.BCBinding | EntityType | Connection Settings | BindingName, ConnectorType | 19 | 20 |  | PX_Commerce_Core_BCBinding, ConnectionSettings, BCBinding | members-01.md | 1639 | 46 |
| PX.Commerce.Core.BCEntitiesSyncStatistics | EntityType | Sync Entities Counts | BindingId, ConnectorType, EntityType | 6 | 9 |  | PX_Commerce_Core_BCEntitiesSyncStatistics, SyncEntitiesCounts, BCEntitiesSyncStatistics | members-01.md | 1686 | 21 |
| PX.Commerce.Core.BCEntity | EntityType | Sync Entity | BindingID, ConnectorType, EntityType | 29 | 8 |  | PX_Commerce_Core_BCEntity, SyncEntity, BCEntity | members-01.md | 1708 | 44 |
| PX.Commerce.Core.BCEntity2 | EntityType | Sync Entity With Counts | BindingID, ConnectorType, EntityType | 3 | 0 | PX.Commerce.Core.BCEntity | PX_Commerce_Core_BCEntity2, SyncEntityWithCounts, BCEntity2 | members-01.md | 1753 | 11 |
| PX.Commerce.Core.BCEntityExportFilter | EntityType | Entity Export Filter | BindingID, ConnectorType, EntityType, ExportFilterID | 23 | 3 |  | PX_Commerce_Core_BCEntityExportFilter, EntityExportFilter, BCEntityExportFilter | members-01.md | 1765 | 33 |
| PX.Commerce.Core.BCEntityExportMapping | EntityType | Entity Export Mapping | BindingID, ConnectorType, EntityType, ExportMappingID | 19 | 3 |  | PX_Commerce_Core_BCEntityExportMapping, EntityExportMapping, BCEntityExportMapping | members-01.md | 1799 | 29 |
| PX.Commerce.Core.BCEntityImportFilter | EntityType | Entity Import Filter | BindingID, ConnectorType, EntityType, ImportFilterID | 23 | 3 |  | PX_Commerce_Core_BCEntityImportFilter, EntityImportFilter, BCEntityImportFilter | members-01.md | 1829 | 33 |
| PX.Commerce.Core.BCEntityImportMapping | EntityType | Entity Import Mapping | BindingID, ConnectorType, EntityType, ImportMappingID | 19 | 3 |  | PX_Commerce_Core_BCEntityImportMapping, EntityImportMapping, BCEntityImportMapping | members-01.md | 1863 | 29 |
| PX.Commerce.Core.BCEntityStats | EntityType | Sync Entity Stats | BindingID, ConnectorType, EntityType | 8 | 2 |  | PX_Commerce_Core_BCEntityStats, SyncEntityStats, BCEntityStats | members-01.md | 1893 | 16 |
| PX.Commerce.Core.BCSyncDetail | EntityType | Sync Status Details | DetailID | 8 | 1 |  | PX_Commerce_Core_BCSyncDetail, SyncStatusDetails, BCSyncDetail | members-01.md | 1910 | 16 |
| PX.Commerce.Core.BCSyncStatus | EntityType | Sync History | SyncID | 33 | 8 |  | PX_Commerce_Core_BCSyncStatus, SyncHistory, BCSyncStatus | members-01.md | 1927 | 48 |
| PX.Commerce.Core.BCWebHook | EntityType | Web Hooks | BindingID, ConnectorType, Scope | 15 | 3 |  | PX_Commerce_Core_BCWebHook, WebHooks, BCWebHook | members-01.md | 1976 | 24 |
| PX.Commerce.Core.DispatcherStatisticCommerceDetail | EntityType | DispatcherStatisticCommerceDetail | Connector, Direction, Id | 4 | 0 |  | PX_Commerce_Core_DispatcherStatisticCommerceDetail, DispatcherStatisticCommerceDetail | members-01.md | 2001 | 10 |
| PX.Commerce.Objects.BCBindingExt | EntityType | Store Settings | BindingID | 53 | 22 |  | PX_Commerce_Objects_BCBindingExt, StoreSettings, BCBindingExt | members-01.md | 2012 | 81 |
| PX.Commerce.Objects.BCFeeMapping | EntityType | BCFeeMapping | BindingID, FeeMappingID | 9 | 3 |  | PX_Commerce_Objects_BCFeeMapping, BCFeeMapping | members-01.md | 2094 | 19 |
| PX.Commerce.Objects.BCInventoryFileUrls | EntityType | BC Inventory File Urls | FileID | 6 | 1 |  | PX_Commerce_Objects_BCInventoryFileUrls, BCInventoryFileUrls | members-01.md | 2114 | 14 |
| PX.Commerce.Objects.BCLocations | EntityType | Locations | BCLocationsID | 6 | 4 |  | PX_Commerce_Objects_BCLocations, Locations, BCLocations | members-01.md | 2129 | 16 |
| PX.Commerce.Objects.BCMatrixOptionsMapping | EntityType | Matrix Options Mapping | OptionMappingID | 18 | 6 |  | PX_Commerce_Objects_BCMatrixOptionsMapping, MatrixOptionsMapping, BCMatrixOptionsMapping | members-01.md | 2146 | 30 |
| PX.Commerce.Objects.BCPaymentMethods | EntityType | BCPaymentMethods | PaymentMappingID | 12 | 7 |  | PX_Commerce_Objects_BCPaymentMethods, BCPaymentMethods | members-01.md | 2177 | 25 |
| PX.Commerce.Objects.BCPaymentTermsMapping | EntityType | BCPaymentTermsMapping | BindingID, PaymentTermsMappingID | 7 | 2 |  | PX_Commerce_Objects_BCPaymentTermsMapping, BCPaymentTermsMapping | members-01.md | 2203 | 15 |
| PX.Commerce.Objects.BCShippingMappings | EntityType | BCShippingMappings | ShippingMappingID | 8 | 5 |  | PX_Commerce_Objects_BCShippingMappings, BCShippingMappings | members-01.md | 2219 | 19 |
| PX.Commerce.Objects.ExportBCLocations | EntityType | ExportLocations | BCLocationsID | 0 | 0 | PX.Commerce.Objects.BCLocations | PX_Commerce_Objects_ExportBCLocations, ExportLocations, ExportBCLocations | members-01.md | 2239 | 6 |
| PX.Commerce.Objects.ImportBCLocations | EntityType | ImportLocations | BCLocationsID | 0 | 0 | PX.Commerce.Objects.BCLocations | PX_Commerce_Objects_ImportBCLocations, ImportLocations, ImportBCLocations | members-01.md | 2246 | 6 |
| PX.Commerce.Objects.SOOrderRisks | EntityType | SO Order Risks | LineNbr, OrderNbr, OrderType | 8 | 1 |  | PX_Commerce_Objects_SOOrderRisks, SOOrderRisks | members-01.md | 2253 | 16 |
| PX.Commerce.Shopify.BCBindingShopify | EntityType | Shopify Settings | BindingID | 30 | 10 |  | PX_Commerce_Shopify_BCBindingShopify, ShopifySettings, BCBindingShopify | members-01.md | 2270 | 47 |
| PX.Commerce.Shopify.BCRoleAssignment | EntityType | Customer Contact Role Assignment | RoleAssignmentID | 13 | 2 |  | PX_Commerce_Shopify_BCRoleAssignment, CustomerContactRoleAssignment, BCRoleAssignment | members-01.md | 2318 | 22 |
| PX.CS.RMColumn | EntityType | Column | ColumnCode, ColumnSetCode | 33 | 4 |  | PX_CS_RMColumn, Column, RMColumn | members-01.md | 2341 | 44 |
| PX.CS.RMColumnHeader | EntityType |  | ColumnCode, ColumnSetCode, HeaderNbr | 20 | 3 |  | PX_CS_RMColumnHeader | members-01.md | 2386 | 29 |
| PX.CS.RMColumnSet | EntityType | Column Set | ColumnSetCode | 14 | 5 |  | PX_CS_RMColumnSet, ColumnSet, RMColumnSet | members-01.md | 2416 | 26 |
| PX.CS.RMDataSource | EntityType | Data Source | DataSourceID | 25 | 23 |  | PX_CS_RMDataSource, DataSource, RMDataSource | members-01.md | 2443 | 54 |
| PX.CS.RMReport | EntityType | Report | ReportCode | 58 | 10 |  | PX_CS_RMReport, Report, RMReport | members-01.md | 2498 | 75 |
| PX.CS.RMRow | EntityType | Row | RowNbr, RowSetCode | 37 | 4 |  | PX_CS_RMRow, Row, RMRow | members-01.md | 2574 | 48 |
| PX.CS.RMRowSet | EntityType | Row Set | RowSetCode | 13 | 4 |  | PX_CS_RMRowSet, RowSet, RMRowSet | members-01.md | 2623 | 24 |
| PX.CS.RMStyle | EntityType | Style | StyleID | 17 | 0 |  | PX_CS_RMStyle, Style, RMStyle | members-01.md | 2648 | 24 |
| PX.CS.RMUnit | EntityType | Unit | UnitCode, UnitSetCode | 18 | 6 |  | PX_CS_RMUnit, Unit, RMUnit | members-01.md | 2673 | 31 |
| PX.CS.RMUnitSet | EntityType | Unit Set | UnitSetCode | 12 | 4 |  | PX_CS_RMUnitSet, UnitSet, RMUnitSet | members-01.md | 2705 | 23 |
| PX.Dashboards.DAC.Dashboard | EntityType | Dashboard | Name | 20 | 6 |  | PX_Dashboards_DAC_Dashboard, Dashboard | members-01.md | 2729 | 33 |
| PX.Dashboards.DAC.DashboardParameter | EntityType | Dashboard Parameter | DashboardID, LineNbr | 21 | 3 |  | PX_Dashboards_DAC_DashboardParameter, DashboardParameter | members-01.md | 2763 | 31 |
| PX.Dashboards.DAC.DashboardParameterV2 | EntityType | Dashboard Parameter | DashboardID, LineNbr | 16 | 3 |  | PX_Dashboards_DAC_DashboardParameterV2, DashboardParameter1, DashboardParameterV2 | members-01.md | 2795 | 26 |
| PX.Dashboards.DAC.DashboardV2 | EntityType | Dashboard | Name | 17 | 6 |  | PX_Dashboards_DAC_DashboardV2, Dashboard1, DashboardV2 | members-01.md | 2822 | 30 |
| PX.Dashboards.DAC.Widget | EntityType | Widget | DashboardID, WidgetID | 23 | 4 |  | PX_Dashboards_DAC_Widget, Widget | members-01.md | 2853 | 34 |
| PX.Dashboards.DAC.WidgetParameterV2 | EntityType |  | DashboardID, DashboardParameterName, WidgetID | 12 | 4 |  | PX_Dashboards_DAC_WidgetParameterV2 | members-01.md | 2888 | 22 |
| PX.Dashboards.DAC.WidgetV2 | EntityType | Widget | DashboardID, WidgetID | 22 | 5 |  | PX_Dashboards_DAC_WidgetV2, Widget1, WidgetV2 | members-01.md | 2911 | 34 |
| PX.Dashboards.Widgets.WidgetPivotTable | EntityType |  | PivotTableID, ScreenID | 3 | 3 |  | PX_Dashboards_Widgets_WidgetPivotTable | members-01.md | 2946 | 11 |
| PX.Data.Archiving.DAC.ArchivalPolicy | EntityType | Archival Policy | TableName | 3 | 0 |  | PX_Data_Archiving_DAC_ArchivalPolicy, ArchivalPolicy | members-01.md | 2958 | 9 |
| PX.Data.Archiving.DAC.ArchivalSetup | EntityType | Archival Setup |  | 1 | 0 |  |  | members-01.md | 2968 | 6 |
| PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate | EntityType | Document Archival History | DateToArchive, ExecutionDate, TableName | 9 | 1 |  | PX_Data_Archiving_DAC_ArchivedDocumentBatchByDate, DocumentArchivalHistory, ArchivedDocumentBatchByDate | members-01.md | 2975 | 16 |
| PX.Data.DeletedRecordsTracking.DAC.ODataPreferences | EntityType | OData Preferences |  | 9 | 2 |  |  | members-01.md | 2992 | 16 |
| PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables | EntityType | Tables to Track Deleted Records | TableID | 6 | 1 |  | PX_Data_DeletedRecordsTracking_DAC_SMDeletedRecordsTrackingTables, TablestoTrackDeletedRecords, SMDeletedRecordsTrackingTables | members-01.md | 3009 | 14 |
| PX.Data.Descriptor.Attributes.SearchIndexEntityRank | EntityType |  |  | 2 | 0 |  |  | members-01.md | 3024 | 6 |
| PX.Data.FilterHeader | EntityType | Filter Header | FilterID, ScreenID, ViewName | 15 | 5 |  | PX_Data_FilterHeader, FilterHeader | members-01.md | 3031 | 27 |
| PX.Data.FilterRow | EntityType | Filter Row | FilterID, FilterRowNbr | 11 | 1 |  | PX_Data_FilterRow, FilterRow | members-01.md | 3059 | 18 |
| PX.Data.GenericInquiry.DAC.GIDataWarehouse | EntityType | Generic Inquiry Data Warehouse | DesignID | 15 | 3 |  | PX_Data_GenericInquiry_DAC_GIDataWarehouse, GenericInquiryDataWarehouse, GIDataWarehouse | members-01.md | 3078 | 25 |
| PX.Data.GridPreferences | EntityType |  |  | 0 | 0 |  |  | members-01.md | 3104 | 3 |
| PX.Data.Licensing.SM.SMLicenseCommerceTran | EntityType |  | Date, ScreenID | 5 | 0 |  | PX_Data_Licensing_SM_SMLicenseCommerceTran | members-01.md | 3108 | 10 |
| PX.Data.Licensing.SM.SMLicenseConstraints | EntityType |  | CompanyIdentifier, Date | 16 | 0 |  | PX_Data_Licensing_SM_SMLicenseConstraints | members-01.md | 3119 | 21 |
| PX.Data.Licensing.SM.SMLicenseERPTran | EntityType |  | Date, PrimaryItemType, ScreenID, TransactionType | 7 | 0 |  | PX_Data_Licensing_SM_SMLicenseERPTran | members-01.md | 3141 | 12 |
| PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction | EntityType | SMLicenseERPTranDetailsAction | ActionId | 6 | 1 |  | PX_Data_Licensing_SM_SMLicenseERPTranDetailsAction, SMLicenseERPTranDetailsAction | members-01.md | 3154 | 13 |
| PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc | EntityType | SMLicenseERPTranDetailsDoc | Id | 5 | 1 |  | PX_Data_Licensing_SM_SMLicenseERPTranDetailsDoc, SMLicenseERPTranDetailsDoc | members-01.md | 3168 | 12 |
| PX.Data.Licensing.SM.SMLicenseViolations | EntityType |  | Date, LimitType, TranType | 14 | 0 |  | PX_Data_Licensing_SM_SMLicenseViolations | members-01.md | 3181 | 20 |
| PX.Data.ListEntryPoint | EntityType | List as Entry Point | EntryScreenID | 9 | 4 |  | PX_Data_ListEntryPoint, ListasEntryPoint, ListEntryPoint | members-01.md | 3202 | 19 |
| PX.Data.Localization.SystemCollation | EntityType |  | CollationName, CollationNameCS, CollationNameCSLatin, CollationNameLatin, SqlDialect | 7 | 0 |  | PX_Data_Localization_SystemCollation | members-01.md | 3222 | 12 |
| PX.Data.Maintenance.GI.GIDesign | EntityType | Generic Inquiry | Name | 42 | 22 |  | PX_Data_Maintenance_GI_GIDesign, GenericInquiry, GIDesign | members-01.md | 3235 | 71 |
| PX.Data.Maintenance.GI.GIFilter | EntityType | Generic Inquiry Filter | DesignID, LineNbr | 24 | 3 |  | PX_Data_Maintenance_GI_GIFilter, GenericInquiryFilter, GIFilter | members-01.md | 3307 | 34 |
| PX.Data.Maintenance.GI.GIGroupBy | EntityType | Generic Inquiry Grouping | DesignID, LineNbr | 12 | 3 |  | PX_Data_Maintenance_GI_GIGroupBy, GenericInquiryGrouping, GIGroupBy | members-01.md | 3342 | 22 |
| PX.Data.Maintenance.GI.GIMassAction | EntityType | Generic Inquiry Mass Action | ActionName, DesignID, MassActionID | 4 | 1 |  | PX_Data_Maintenance_GI_GIMassAction, GenericInquiryMassAction, GIMassAction | members-01.md | 3365 | 11 |
| PX.Data.Maintenance.GI.GIMassUpdateField | EntityType | Generic Inquiry Mass Update Field | DesignID, FieldID, FieldName | 4 | 1 |  | PX_Data_Maintenance_GI_GIMassUpdateField, GenericInquiryMassUpdateField, GIMassUpdateField | members-01.md | 3377 | 11 |
| PX.Data.Maintenance.GI.GINavigationCondition | EntityType | Generic Inquiry Navigation Condition | DesignID, LineNbr, NavigationScreenLineNbr | 18 | 4 |  | PX_Data_Maintenance_GI_GINavigationCondition, GenericInquiryNavigationCondition, GINavigationCondition | members-01.md | 3389 | 28 |
| PX.Data.Maintenance.GI.GINavigationParameter | EntityType | Generic Inquiry Navigation Parameter | DesignID, LineNbr, NavigationScreenLineNbr | 12 | 4 |  | PX_Data_Maintenance_GI_GINavigationParameter, GenericInquiryNavigationParameter, GINavigationParameter | members-01.md | 3418 | 22 |
| PX.Data.Maintenance.GI.GINavigationScreen | EntityType | Generic Inquiry Navigation Screen | DesignID, LineNbr | 17 | 5 |  | PX_Data_Maintenance_GI_GINavigationScreen, GenericInquiryNavigationScreen, GINavigationScreen | members-01.md | 3441 | 29 |
| PX.Data.Maintenance.GI.GIOn | EntityType | Generic Inquiry Relation Dependencies | DesignID, LineNbr, RelationNbr | 17 | 4 |  | PX_Data_Maintenance_GI_GIOn, GenericInquiryRelationDependencies, GIOn | members-01.md | 3471 | 28 |
| PX.Data.Maintenance.GI.GIRecordDefault | EntityType | Generic Inquiry Default Record | DesignID, FieldName, RecDefID | 10 | 3 |  | PX_Data_Maintenance_GI_GIRecordDefault, GenericInquiryDefaultRecord, GIRecordDefault | members-01.md | 3500 | 19 |
| PX.Data.Maintenance.GI.GIRelation | EntityType | Generic Inquiry Relation | DesignID, LineNbr | 15 | 4 |  | PX_Data_Maintenance_GI_GIRelation, GenericInquiryRelation, GIRelation | members-01.md | 3520 | 26 |
| PX.Data.Maintenance.GI.GIResult | EntityType | Generic Inquiry Result | DesignID, LineNbr | 28 | 3 |  | PX_Data_Maintenance_GI_GIResult, GenericInquiryResult, GIResult | members-01.md | 3547 | 38 |
| PX.Data.Maintenance.GI.GISort | EntityType | Generic Inquiry Sorting | DesignID, LineNbr | 13 | 3 |  | PX_Data_Maintenance_GI_GISort, GenericInquirySorting, GISort | members-01.md | 3586 | 23 |
| PX.Data.Maintenance.GI.GITable | EntityType | Generic Inquiry Table | Alias, DesignID | 14 | 3 |  | PX_Data_Maintenance_GI_GITable, GenericInquiryTable, GITable | members-01.md | 3610 | 24 |
| PX.Data.Maintenance.GI.GIWhere | EntityType | Generic Inquiry Where Statement | DesignID, LineNbr | 19 | 3 |  | PX_Data_Maintenance_GI_GIWhere, GenericInquiryWhereStatement, GIWhere | members-01.md | 3635 | 29 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceChart | EntityType |  |  | 2 | 0 |  |  | members-01.md | 3665 | 6 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceSplit | EntityType |  |  | 2 | 0 |  |  | members-01.md | 3672 | 6 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary | EntityType |  | Date, InstallationID | 18 | 0 |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceDailyUsageSummary | members-01.md | 3679 | 23 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated | EntityType |  | ChartId, InstallationID, IntervalDateTime, Legend, SplitId | 6 | 0 |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceDayUsageAggregated | members-01.md | 3703 | 11 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceInstallation | EntityType |  | Id | 2 | 0 |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceInstallation | members-01.md | 3715 | 7 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits | EntityType |  | Date, InstallationID | 16 | 0 |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceParamLimits | members-01.md | 3723 | 22 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetails | EntityType |  | DayIndex, EncodedIDs, Legend | 4 | 0 |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetails | members-01.md | 3746 | 9 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsPacked | EntityType |  | ChartId, DayIndex, InstallationId, Legend, SplitId | 5 | 0 |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetailsPacked | members-01.md | 3756 | 10 |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp | EntityType |  | ChartId, InstallationID, IntervalDateTime, Legend, SplitId | 6 | 0 |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetailsTmp | members-01.md | 3767 | 11 |
| PX.Data.Maintenance.SM.DAC.SMLicenseStatistic | EntityType |  | Date | 14 | 0 |  | PX_Data_Maintenance_SM_DAC_SMLicenseStatistic | members-01.md | 3779 | 19 |
| PX.Data.Maintenance.SM.DAC.ThemeVariables | EntityType |  | EntityNoteID, Theme, VariableName | 4 | 0 |  | PX_Data_Maintenance_SM_DAC_ThemeVariables | members-01.md | 3799 | 9 |
| PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule | EntityType | Notification Schedule | NotificationID, ScheduleID | 4 | 2 |  | PX_Data_Maintenance_SM_SendRecurringNotifications_NotificationSchedule, NotificationSchedule | members-01.md | 3809 | 13 |
| PX.Data.Maintenance.TenantOperations.TenantOperationHistory | EntityType | Tenant Operation History | Id | 15 | 0 |  | PX_Data_Maintenance_TenantOperations_TenantOperationHistory, TenantOperationHistory | members-01.md | 3823 | 22 |
| PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion | EntityType | Tenant or Snapshot Deletion | SnapshotId, TenantId | 19 | 0 |  | PX_Data_Maintenance_TenantShapshotDeletion_DAC_TenantSnapshotDeletion, TenantorSnapshotDeletion, TenantSnapshotDeletion | members-01.md | 3846 | 26 |
| PX.Data.Note | EntityType | Note | NoteID | 7 | 0 |  | PX_Data_Note, Note | members-01.md | 3873 | 14 |
| PX.Data.NoteDoc | EntityType |  | FileID, NoteID | 5 | 0 |  | PX_Data_NoteDoc | members-01.md | 3888 | 11 |
| PX.Data.NoteDoc2 | EntityType |  | FileID, NoteID | 0 | 0 | PX.Data.NoteDoc | PX_Data_NoteDoc2 | members-01.md | 3900 | 5 |
| PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory | EntityType | Workflow Category | CategoryName, ScreenID | 10 | 0 |  | PX_Data_ProjectDefinition_Workflow_AUWorkflowCategory, WorkflowCategory, AUWorkflowCategory | members-01.md | 3906 | 16 |
| PX.Data.Reports.UserReport | EntityType |  | ReportFileName, Version | 12 | 2 |  | PX_Data_Reports_UserReport | members-01.md | 3923 | 19 |
| PX.Data.Reports.UserReportHeader | EntityType |  | ReportFileName, Version | 0 | 0 | PX.Data.Reports.UserReport | PX_Data_Reports_UserReportHeader | members-01.md | 3943 | 5 |
| PX.Data.RichTextEdit.RichFileRevision | EntityType |  | FileID, FileRevisionID | 0 | 0 | PX.SM.UploadFileRevision | PX_Data_RichTextEdit_RichFileRevision | members-01.md | 3949 | 5 |
| PX.Data.RichTextEdit.WikiPage2 | EntityType |  | PageID | 4 | 4 |  | PX_Data_RichTextEdit_WikiPage2 | members-01.md | 3955 | 13 |
| PX.Data.RichTextEdit.WikiPageParent | EntityType |  | PageID | 0 | 0 | PX.Data.RichTextEdit.WikiPage2 | PX_Data_RichTextEdit_WikiPageParent | members-01.md | 3969 | 5 |
| PX.Data.Search.SPWikiCategory | EntityType |  | CategoryID | 9 | 3 |  | PX_Data_Search_SPWikiCategory | members-01.md | 3975 | 17 |
| PX.Data.Search.SPWikiCategoryTags | EntityType |  | CategoryID, PageID | 11 | 3 |  | PX_Data_Search_SPWikiCategoryTags | members-01.md | 3993 | 19 |
| PX.Data.Search.SPWikiProduct | EntityType |  | ProductID | 9 | 3 |  | PX_Data_Search_SPWikiProduct | members-01.md | 4013 | 17 |
| PX.Data.Search.SPWikiProductTags | EntityType |  | PageID, ProductID | 11 | 3 |  | PX_Data_Search_SPWikiProductTags | members-01.md | 4031 | 19 |
| PX.Data.SearchIndex | EntityType | Search Index | NoteID | 7 | 0 |  | PX_Data_SearchIndex, SearchIndex | members-01.md | 4051 | 14 |
| PX.Data.Services.Implementations.FavoriteActionRecord | EntityType | Favorite Action | ActionName, IsPortal, ScreenID, UserID | 6 | 0 |  | PX_Data_Services_Implementations_FavoriteActionRecord, FavoriteAction, FavoriteActionRecord | members-01.md | 4066 | 12 |
| PX.Data.SystemColor | EntityType |  | ColorName | 3 | 0 |  | PX_Data_SystemColor | members-01.md | 4079 | 8 |
| PX.Data.Update.Company | EntityType |  |  | 0 | 2 |  |  | members-01.md | 4088 | 6 |
| PX.Data.Update.UPMeasureEndpoint | EntityType |  | EndpointID | 7 | 0 |  | PX_Data_Update_UPMeasureEndpoint | members-01.md | 4095 | 12 |
| PX.Data.Update.UPMeasureHistory | EntityType |  | EndpointID, MeasureID | 8 | 0 |  | PX_Data_Update_UPMeasureHistory | members-01.md | 4108 | 14 |
| PX.Data.Update.UPSelectedEndpoint | EntityType |  | EndpointID | 0 | 0 | PX.Data.Update.UPMeasureEndpoint | PX_Data_Update_UPSelectedEndpoint | members-01.md | 4123 | 5 |
| PX.Data.UserRecords.FavoriteRecords.FavoriteRecord | EntityType | Favorite Record | EntityType, IsPortal, RefNoteId, UserID | 7 | 0 |  | PX_Data_UserRecords_FavoriteRecords_FavoriteRecord, FavoriteRecord | members-01.md | 4129 | 13 |
| PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord | EntityType | Viewed Record | EntityType, IsPortal, RefNoteId, UserID | 9 | 0 |  | PX_Data_UserRecords_RecentlyVisitedRecords_VisitedRecord, ViewedRecord, VisitedRecord | members-01.md | 4143 | 15 |
| PX.Data.Wiki.Tags.RoleInTag | EntityType | Roles In Tag | Rolename, TagID | 9 | 4 |  | PX_Data_Wiki_Tags_RoleInTag, RolesInTag, RoleInTag | members-01.md | 4159 | 19 |
| PX.Data.Wiki.Tags.Tag | EntityType | Tag | TagID | 12 | 3 |  | PX_Data_Wiki_Tags_Tag, Tag | members-01.md | 4179 | 22 |
| PX.Data.Wiki.Tags.UploadFileTag | EntityType | File Tag | FileID, TagID | 8 | 2 |  | PX_Data_Wiki_Tags_UploadFileTag, FileTag, UploadFileTag | members-01.md | 4202 | 16 |
| PX.DataSync.HubSpot.HSEntitySetup | EntityType |  | EntityType | 20 | 4 |  | PX_DataSync_HubSpot_HSEntitySetup | members-01.md | 4219 | 30 |
| PX.DataSync.HubSpot.HSMarketingListMember | EntityType |  | MarketingListMemberID | 15 | 3 |  | PX_DataSync_HubSpot_HSMarketingListMember | members-01.md | 4250 | 23 |
| PX.DataSync.SendGrid.SMSendGridAccountsSettings | EntityType | SendGrid Accounts Settings | SendGridConnectionID | 4 | 19 | PX.DataSync.SendGrid.SMSendGridSettings | PX_DataSync_SendGrid_SMSendGridAccountsSettings, SendGridAccountsSettings, SMSendGridAccountsSettings | members-01.md | 4274 | 30 |
| PX.DataSync.SendGrid.SMSendGridRecipient | EntityType | SendGrid Recipients | Address, RefNoteID | 12 | 2 |  | PX_DataSync_SendGrid_SMSendGridRecipient, SendGridRecipients, SMSendGridRecipient | members-01.md | 4305 | 21 |
| PX.DataSync.SendGrid.SMSendGridSettings | EntityType | SendGrid Settings | SendGridConnectionID | 26 | 2 |  | PX_DataSync_SendGrid_SMSendGridSettings, SendGridSettings, SMSendGridSettings | members-01.md | 4327 | 35 |
| PX.DataSync.SendGrid.SMSendGridSuppressionGroup | EntityType | SendGrid Suppression Group | GroupID, SendGridConnectionID | 15 | 4 |  | PX_DataSync_SendGrid_SMSendGridSuppressionGroup, SendGridSuppressionGroup, SMSendGridSuppressionGroup | members-01.md | 4363 | 25 |
| PX.EP.EPLoginType | EntityType | Login Type | LoginTypeID, LoginTypeName | 20 | 5 |  | PX_EP_EPLoginType, LoginType, EPLoginType | members-01.md | 4389 | 32 |
| PX.EP.EPLoginTypeAllowsRole | EntityType | Login Type Allow Role | LoginTypeID, Rolename | 10 | 4 |  | PX_EP_EPLoginTypeAllowsRole, LoginTypeAllowRole, EPLoginTypeAllowsRole | members-01.md | 4422 | 20 |
| PX.EP.EPManagedLoginType | EntityType | Login Type Managed | LoginTypeID, ParentLoginTypeID | 9 | 4 |  | PX_EP_EPManagedLoginType, LoginTypeManaged, EPManagedLoginType | members-01.md | 4443 | 19 |
| PX.ESign.ESignAccount | EntityType | eSign Account | AccountCD | 29 | 4 |  | PX_ESign_ESignAccount, eSignAccount | members-01.md | 4463 | 40 |
| PX.ESign.ESignAccountUserRule | EntityType | eSign Account User Rule | AccountID, OwnerID | 9 | 3 |  | PX_ESign_ESignAccountUserRule, eSignAccountUserRule | members-01.md | 4504 | 18 |
| PX.ESign.ESignEnvelopeInfo | EntityType | eSign Request | EnvelopeInfoID | 36 | 5 |  | PX_ESign_ESignEnvelopeInfo, eSignRequest, ESignEnvelopeInfo | members-01.md | 4523 | 48 |
| PX.ESign.ESignRecipient | EntityType | eSign Recipient | RecipientID | 18 | 4 |  | PX_ESign_ESignRecipient, eSignRecipient | members-01.md | 4572 | 28 |
| PX.ExternalCarriersCommon.ShipEngineCarrierService | EntityType |  | CarrierPluginID, ServiceCode | 14 | 3 |  | PX_ExternalCarriersCommon_ShipEngineCarrierService | members-01.md | 4601 | 22 |
| PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData | EntityType | Opportunity Carrier Data | RefNoteID | 12 | 3 |  | PX_ExternalCarriersHelper_CROpportunityRevisionCarrierData, OpportunityCarrierData, CROpportunityRevisionCarrierData | members-01.md | 4624 | 21 |
| PX.ExternalCarriersHelper.InventoryItemCarrierData | EntityType | Inventory Item Carrier Data | InventoryID | 18 | 4 |  | PX_ExternalCarriersHelper_InventoryItemCarrierData, InventoryItemCarrierData | members-01.md | 4646 | 28 |
| PX.ExternalCarriersHelper.SETerritoriesMapping | EntityType |  | CarrierPluginID, CountryID, StateID | 12 | 5 |  | PX_ExternalCarriersHelper_SETerritoriesMapping | members-01.md | 4675 | 22 |
| PX.ExternalCarriersHelper.SOOrderCarrierData | EntityType | SO Order Carrier Data | OrderNbr, OrderType | 13 | 3 |  | PX_ExternalCarriersHelper_SOOrderCarrierData, SOOrderCarrierData | members-01.md | 4698 | 22 |
| PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates | EntityType | SOOrder Carrier Data for Shop for Rates | OrderNbr, OrderType | 6 | 1 |  | PX_ExternalCarriersHelper_SOOrderCarrierDataShopForRates, SOOrderCarrierDataforShopforRates, SOOrderCarrierDataShopForRates | members-01.md | 4721 | 13 |
| PX.ExternalCarriersHelper.SOOrderShopForRates | EntityType | SOOrder Data for Shop for Rates | OrderNbr, OrderType | 11 | 58 |  | PX_ExternalCarriersHelper_SOOrderShopForRates, SOOrderDataforShopforRates, SOOrderShopForRates | members-01.md | 4735 | 76 |
| PX.ExternalCarriersHelper.SOShipmentCarrierData | EntityType | SO Shipment Carrier Data | ShipmentNbr | 23 | 3 |  | PX_ExternalCarriersHelper_SOShipmentCarrierData, SOShipmentCarrierData | members-01.md | 4812 | 32 |
| PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates | EntityType | SOShipment Carrier Data for Shop for Rates | ShipmentNbr | 5 | 1 |  | PX_ExternalCarriersHelper_SOShipmentCarrierDataShopForRates, SOShipmentCarrierDataforShopforRates, SOShipmentCarrierDataShopForRates | members-01.md | 4845 | 12 |
| PX.ExternalCarriersHelper.SOShipmentShopForRates | EntityType | SOShipment Data for Shop for Rates | ShipmentNbr | 10 | 20 |  | PX_ExternalCarriersHelper_SOShipmentShopForRates, SOShipmentDataforShopforRates, SOShipmentShopForRates | members-01.md | 4858 | 37 |
| PX.FS.FSGPSTrackingHistory | EntityType |  | ExecutionDate, TrackingID | 6 | 0 |  | PX_FS_FSGPSTrackingHistory | members-01.md | 4896 | 11 |
| PX.FS.FSGPSTrackingRequest | EntityType |  | RequestID | 30 | 3 |  | PX_FS_FSGPSTrackingRequest | members-01.md | 4908 | 39 |
| PX.GIReports.Maintenance.DAC.GIReport | EntityType | Grouped Table | ReportID | 11 | 7 |  | PX_GIReports_Maintenance_DAC_GIReport, GroupedTable, GIReport | members-01.md | 4948 | 25 |
| PX.GIReports.Maintenance.DAC.GIReportGroup | EntityType | Grouped Table Groups | GroupID, ReportID | 19 | 6 |  | PX_GIReports_Maintenance_DAC_GIReportGroup, GroupedTableGroups, GIReportGroup | members-01.md | 4974 | 32 |
| PX.GIReports.Maintenance.DAC.GIReportGroupColumn | EntityType | Grouped Table Columns | GroupID, LineNbr, ReportID | 22 | 4 |  | PX_GIReports_Maintenance_DAC_GIReportGroupColumn, GroupedTableColumns, GIReportGroupColumn | members-01.md | 5007 | 33 |
| PX.GIReports.Maintenance.DAC.GIReportGroupGrouping | EntityType | Grouped Table Grouping | GroupID, LineNbr, ReportID | 15 | 4 |  | PX_GIReports_Maintenance_DAC_GIReportGroupGrouping, GroupedTableGrouping, GIReportGroupGrouping | members-01.md | 5041 | 26 |
| PX.GIReports.Maintenance.DAC.GIReportGroupSorting | EntityType | Grouped Table Sorting | GroupID, LineNbr, ReportID | 16 | 4 |  | PX_GIReports_Maintenance_DAC_GIReportGroupSorting, GroupedTableSorting, GIReportGroupSorting | members-01.md | 5068 | 27 |
| PX.Mail.Log.DAC.EmailLog | EntityType | Email Log | LogEntryID | 17 | 2 |  | PX_Mail_Log_DAC_EmailLog, EmailLog | members-01.md | 5096 | 25 |
| PX.ML.Chat.DAC.MLChatMessage | EntityType | MLChatMessage | MessageID | 10 | 0 |  | PX_ML_Chat_DAC_MLChatMessage, MLChatMessage | members-01.md | 5122 | 16 |
| PX.ML.Chat.DAC.MLChatMessageAttachment | EntityType | MLChatMessageAttachment | FileID, MessageID | 9 | 0 |  | PX_ML_Chat_DAC_MLChatMessageAttachment, MLChatMessageAttachment | members-01.md | 5139 | 15 |
| PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory | EntityType | MLAIAssistantUnitsConsumptionHistory | HistoryID | 7 | 0 |  | PX_ML_Chat_Licensing_DAC_MLAIAssistantUnitsConsumptionHistory, MLAIAssistantUnitsConsumptionHistory | members-01.md | 5155 | 13 |
| PX.ML.CrossSales.DAC.MLCrossSalesSetup | EntityType | MLCrossSalesSetup |  | 11 | 3 |  |  | members-01.md | 5169 | 19 |
| PX.MSGraph.DAC.SM.SMGraphPermission | EntityType | Graph Access Rights | AccessRight | 12 | 2 |  | PX_MSGraph_DAC_SM_SMGraphPermission, GraphAccessRights, SMGraphPermission | members-01.md | 5189 | 21 |
| PX.MSGraph.DAC.SM.SMGraphSetup | EntityType | Teams Preferences |  | 11 | 2 |  |  | members-01.md | 5211 | 18 |
| PX.MSTeams.DAC.SM.SMTeamsChannel | EntityType | Teams Channel | ChannelID | 9 | 2 |  | PX_MSTeams_DAC_SM_SMTeamsChannel, TeamsChannel, SMTeamsChannel | members-01.md | 5230 | 18 |
| PX.MSTeams.DAC.SM.SMTeamsMember | EntityType | Teams Member | MemberID | 19 | 2 |  | PX_MSTeams_DAC_SM_SMTeamsMember, TeamsMember, SMTeamsMember | members-01.md | 5249 | 28 |
| PX.MSTeams.DAC.SM.SMTeamsMemberMapping | EntityType | Teams Member Mapping | MemberID, TeamsID | 2 | 2 |  | PX_MSTeams_DAC_SM_SMTeamsMemberMapping, TeamsMemberMapping, SMTeamsMemberMapping | members-01.md | 5278 | 10 |
| PX.MSTeams.DAC.SM.SMTeamsNotification | EntityType | Teams Notification | NotificationID | 24 | 5 |  | PX_MSTeams_DAC_SM_SMTeamsNotification, TeamsNotification, SMTeamsNotification | members-01.md | 5289 | 36 |
| PX.MSTeams.DAC.SM.SMTeamsTeam | EntityType | Teams Team | TeamsID | 9 | 2 |  | PX_MSTeams_DAC_SM_SMTeamsTeam, TeamsTeam, SMTeamsTeam | members-01.md | 5326 | 18 |
| PX.OAuthClient.DAC.OAuthApplication | EntityType |  | ApplicationID | 9 | 4 |  | PX_OAuthClient_DAC_OAuthApplication | members-01.md | 5345 | 18 |
| PX.OAuthClient.DAC.OAuthResource | EntityType | Application Resource | ApplicationID, ResourceCD | 11 | 1 |  | PX_OAuthClient_DAC_OAuthResource, ApplicationResource, OAuthResource | members-01.md | 5364 | 19 |
| PX.OAuthClient.DAC.OAuthToken | EntityType |  | TokenID | 10 | 1 |  | PX_OAuthClient_DAC_OAuthToken | members-01.md | 5384 | 17 |
| PX.OAuthClient.DAC.ResourceRole | EntityType | Role | ApplicationName, Rolename | 1 | 0 | PX.SM.Roles | PX_OAuthClient_DAC_ResourceRole | members-01.md | 5402 | 9 |
| PX.Objects.AM.AMAPSMaintenanceSetup | EntityType | APS Maintenance Setup |  | 8 | 1 |  |  | members-01.md | 5412 | 14 |
| PX.Objects.AM.AMBatch | EntityType | AM Batch | BatNbr, DocType | 35 | 17 |  | PX_Objects_AM_AMBatch, AMBatch | members-01.md | 5427 | 59 |
| PX.Objects.AM.AMBatchCost | EntityType | AM Batch Cost | BatNbr, DocType | 27 | 12 |  | PX_Objects_AM_AMBatchCost, AMBatchCost | members-01.md | 5487 | 45 |
| PX.Objects.AM.AMBatchItemLotSerialAttributesHeader | EntityType | AMBatchItemLotSerialAttributesHeader | BatNbr, DocType, InventoryID, LotSerialNbr | 14 | 6 |  | PX_Objects_AM_AMBatchItemLotSerialAttributesHeader, AMBatchItemLotSerialAttributesHeader | members-01.md | 5533 | 27 |
| PX.Objects.AM.AMBomAttribute | EntityType | BOM Attributes | BOMID, LineNbr, RevisionID | 20 | 6 |  | PX_Objects_AM_AMBomAttribute, BOMAttributes, AMBomAttribute | members-01.md | 5561 | 32 |
| PX.Objects.AM.AMBomCost | EntityType | BOM Cost | BOMID, CuryID, RevisionID, SiteID, UserID | 43 | 6 |  | PX_Objects_AM_AMBomCost, BOMCost, AMBomCost | members-01.md | 5594 | 56 |
| PX.Objects.AM.AMBomCostHistory | EntityType | Cost Roll History | BOMID, CuryID, RevisionID, SiteID, StartDate | 41 | 6 |  | PX_Objects_AM_AMBomCostHistory, CostRollHistory, AMBomCostHistory | members-01.md | 5651 | 54 |
| PX.Objects.AM.AMBOMCurySettings | EntityType | BOM Currency Settings | BOMID, CuryID, LineID, LineType, OperationID, RevisionID | 17 | 3 |  | PX_Objects_AM_AMBOMCurySettings, BOMCurrencySettings, AMBOMCurySettings | members-01.md | 5706 | 26 |
| PX.Objects.AM.AMBomItem | EntityType | BOM Item | BOMID, RevisionID | 24 | 26 |  | PX_Objects_AM_AMBomItem, BOMItem, AMBomItem | members-01.md | 5733 | 57 |
| PX.Objects.AM.AMBomItem2 | EntityType | BOM Item | BOMID, RevisionID | 0 | 0 | PX.Objects.AM.AMBomItem | PX_Objects_AM_AMBomItem2, BOMItem1, AMBomItem2 | members-01.md | 5791 | 6 |
| PX.Objects.AM.AMBomItem3 | EntityType | BOM Item | BOMID, RevisionID | 8 | 2 |  | PX_Objects_AM_AMBomItem3, BOMItem2, AMBomItem3 | members-01.md | 5798 | 16 |
| PX.Objects.AM.AMBomItemActive | EntityType | BOM Item Active | BOMID, RevisionID | 0 | 0 | PX.Objects.AM.AMBomItem | PX_Objects_AM_AMBomItemActive, BOMItemActive, AMBomItemActive | members-01.md | 5815 | 6 |
| PX.Objects.AM.AMBomItemActive2 | EntityType | BOM Item Active 2 | BOMID, RevisionID | 0 | 0 | PX.Objects.AM.AMBomItem | PX_Objects_AM_AMBomItemActive2, BOMItemActive2, AMBomItemActive2 | members-01.md | 5822 | 6 |
| PX.Objects.AM.AMBomItemBomDefaults | EntityType | BOM Item BOM Default | BOMID, RevisionID | 11 | 0 |  | PX_Objects_AM_AMBomItemBomDefaults, BOMItemBOMDefault, AMBomItemBomDefaults | members-01.md | 5829 | 18 |
| PX.Objects.AM.AMBomMatl | EntityType | BOM Material | BOMID, CurrBOMID, CurrOperationID, CurrRevisionID, CuryID, CuryLineID, LineID, LineType, OperationID, RevisionID | 49 | 13 |  | PX_Objects_AM_AMBomMatl, BOMMaterial, AMBomMatl | members-01.md | 5848 | 69 |
| PX.Objects.AM.AMBomMatlCury | EntityType | AMBomMatlCurrency | BOMID, CuryID, LineID, LineType, OperationID, RevisionID | 17 | 2 |  | PX_Objects_AM_AMBomMatlCury, AMBomMatlCurrency, AMBomMatlCury | members-01.md | 5918 | 25 |
| PX.Objects.AM.AMBomOper | EntityType | BOM Operation | BOMID, OperationCD, RevisionID | 42 | 15 |  | PX_Objects_AM_AMBomOper, BOMOperation, AMBomOper | members-01.md | 5944 | 64 |
| PX.Objects.AM.AMBomOperCury | EntityType | AMBomOperCurrency | BOMID, CuryID, LineID, LineType, OperationID, RevisionID | 15 | 3 |  | PX_Objects_AM_AMBomOperCury, AMBomOperCurrency, AMBomOperCury | members-01.md | 6009 | 24 |
| PX.Objects.AM.AMBomOvhd | EntityType | BOM Overhead | BOMID, LineID, OperationID, RevisionID | 16 | 5 |  | PX_Objects_AM_AMBomOvhd, BOMOverhead, AMBomOvhd | members-01.md | 6034 | 28 |
| PX.Objects.AM.AMBomRef | EntityType | BOM Reference Designator | BOMID, LineID, MatlLineID, OperationID, RevisionID | 16 | 4 |  | PX_Objects_AM_AMBomRef, BOMReferenceDesignator, AMBomRef | members-01.md | 6063 | 27 |
| PX.Objects.AM.AMBomStep | EntityType | BOM Step | BOMID, LineID, OperationID, RevisionID | 16 | 4 |  | PX_Objects_AM_AMBomStep, BOMStep, AMBomStep | members-01.md | 6091 | 27 |
| PX.Objects.AM.AMBomTool | EntityType | BOM Tool | BOMID, LineID, OperationID, RevisionID | 18 | 6 |  | PX_Objects_AM_AMBomTool, BOMTool, AMBomTool | members-01.md | 6119 | 31 |
| PX.Objects.AM.AMBomToolCury | EntityType | AMBomToolCurrency | BOMID, CuryID, LineID, LineType, OperationID, RevisionID | 17 | 2 |  | PX_Objects_AM_AMBomToolCury, AMBomToolCurrency, AMBomToolCury | members-01.md | 6151 | 25 |
| PX.Objects.AM.AMBSetup | EntityType | BOM Preferences |  | 18 | 4 |  |  | members-01.md | 6177 | 27 |
| PX.Objects.AM.AMCalendarBreakTime | EntityType | Calendar Break Time | CalendarID, DayOfWeek, StartTime | 0 | 0 | PX.Objects.CS.CSCalendarBreakTime | PX_Objects_AM_AMCalendarBreakTime, CalendarBreakTime, AMCalendarBreakTime | members-01.md | 6205 | 6 |
| PX.Objects.AM.AMClockItem | EntityType | Clock Employee | EmployeeID | 31 | 19 |  | PX_Objects_AM_AMClockItem, ClockEmployee, AMClockItem | members-01.md | 6212 | 57 |
| PX.Objects.AM.AMClockItemSplit | EntityType | Clock Employee Split | EmployeeID, LineNbr, SplitLineNbr | 24 | 2 |  | PX_Objects_AM_AMClockItemSplit, ClockEmployeeSplit, AMClockItemSplit | members-01.md | 6270 | 33 |
| PX.Objects.AM.AMClockTran | EntityType | Clock Transaction | EmployeeID, LineNbr | 43 | 23 |  | PX_Objects_AM_AMClockTran, ClockTransaction, AMClockTran | members-01.md | 6304 | 73 |
| PX.Objects.AM.AMClockTranSplit | EntityType | Clock Transaction Split | EmployeeID, LineNbr, SplitLineNbr | 24 | 9 |  | PX_Objects_AM_AMClockTranSplit, ClockTransactionSplit, AMClockTranSplit | members-01.md | 6378 | 40 |
| PX.Objects.AM.AMConfigResultsAttribute | EntityType | Configuration Attribute Result | AttributeLineNbr, ConfigResultsID | 18 | 6 |  | PX_Objects_AM_AMConfigResultsAttribute, ConfigurationAttributeResult, AMConfigResultsAttribute | members-01.md | 6419 | 30 |
| PX.Objects.AM.AMConfigResultsFeature | EntityType | Configuration Feature Result | ConfigResultsID, FeatureLineNbr | 22 | 6 |  | PX_Objects_AM_AMConfigResultsFeature, ConfigurationFeatureResult, AMConfigResultsFeature | members-01.md | 6450 | 35 |
| PX.Objects.AM.AMConfigResultsOption | EntityType | Configuration Option Result | ConfigResultsID, FeatureLineNbr, OptionLineNbr | 36 | 9 |  | PX_Objects_AM_AMConfigResultsOption, ConfigurationOptionResult, AMConfigResultsOption | members-01.md | 6486 | 52 |
| PX.Objects.AM.AMConfigResultsRule | EntityType | Configuration Rule Result | ConfigResultsID, RuleLineNbr, RuleSource, RuleSourceLineNbr, RuleTarget, TargetLineNbr, TargetSubLineNbr | 23 | 4 |  | PX_Objects_AM_AMConfigResultsRule, ConfigurationRuleResult, AMConfigResultsRule | members-01.md | 6539 | 33 |
| PX.Objects.AM.AMConfiguration | EntityType | Configuration | ConfigurationID, Revision | 26 | 16 |  | PX_Objects_AM_AMConfiguration, Configuration, AMConfiguration | members-01.md | 6573 | 49 |
| PX.Objects.AM.AMConfigurationAttribute | EntityType | Configuration Attribute | ConfigurationID, LineNbr, Revision | 21 | 6 |  | PX_Objects_AM_AMConfigurationAttribute, ConfigurationAttribute, AMConfigurationAttribute | members-01.md | 6623 | 34 |
| PX.Objects.AM.AMConfigurationAttributeRule | EntityType | Configuration Attribute Rule | ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr | 19 | 6 |  | PX_Objects_AM_AMConfigurationAttributeRule, ConfigurationAttributeRule, AMConfigurationAttributeRule | members-01.md | 6658 | 31 |
| PX.Objects.AM.AMConfigurationFeature | EntityType | Configuration Feature | ConfigurationID, LineNbr, Revision | 24 | 10 |  | PX_Objects_AM_AMConfigurationFeature, ConfigurationFeature, AMConfigurationFeature | members-01.md | 6690 | 40 |
| PX.Objects.AM.AMConfigurationFeatureRule | EntityType | Configuration Feature Rule | ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr | 20 | 6 |  | PX_Objects_AM_AMConfigurationFeatureRule, ConfigurationFeatureRule, AMConfigurationFeatureRule | members-01.md | 6731 | 33 |
| PX.Objects.AM.AMConfigurationKeys | EntityType | Configuration Keys | ConfigResultsID | 35 | 15 |  | PX_Objects_AM_AMConfigurationKeys, ConfigurationKeys, AMConfigurationKeys | members-01.md | 6765 | 57 |
| PX.Objects.AM.AMConfigurationOption | EntityType | Configuration Option | ConfigFeatureLineNbr, ConfigurationID, LineNbr, Revision | 33 | 15 |  | PX_Objects_AM_AMConfigurationOption, ConfigurationOption, AMConfigurationOption | members-01.md | 6823 | 54 |
| PX.Objects.AM.AMConfigurationOptionCurySettings | EntityType | Config Option Currency Settings | ConfigFeatureLineNbr, ConfigurationID, CuryID, LineNbr, Revision | 13 | 4 |  | PX_Objects_AM_AMConfigurationOptionCurySettings, ConfigOptionCurrencySettings, AMConfigurationOptionCurySettings | members-01.md | 6878 | 23 |
| PX.Objects.AM.AMConfigurationResults | EntityType | Configuration Result | ConfigResultsID | 45 | 21 |  | PX_Objects_AM_AMConfigurationResults, ConfigurationResult, AMConfigurationResults | members-01.md | 6902 | 73 |
| PX.Objects.AM.AMConfigurationRule | EntityType | Configuration Rule | ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr | 19 | 7 |  | PX_Objects_AM_AMConfigurationRule, ConfigurationRule, AMConfigurationRule | members-01.md | 6976 | 32 |
| PX.Objects.AM.AMConfiguratorSetup | EntityType | Configurator Preferences |  | 14 | 2 |  |  | members-01.md | 7009 | 21 |
| PX.Objects.AM.AMDepartment | EntityType | AM Department | DepartmentID | 11 | 4 |  | PX_Objects_AM_AMDepartment, AMDepartment | members-01.md | 7031 | 22 |
| PX.Objects.AM.AMDisassembleBatch | EntityType | AM Disassemble | BatchNbr, DocType | 82 | 18 |  | PX_Objects_AM_AMDisassembleBatch, AMDisassemble, AMDisassembleBatch | members-01.md | 7054 | 107 |
| PX.Objects.AM.AMDisassembleBatchAttribute | EntityType | AM Disassemble Transaction Attribute | BatNbr, DocType, LineNbr, ProdAttributeLineNbr, TranLineNbr | 0 | 0 | PX.Objects.AM.AMMTranAttribute | PX_Objects_AM_AMDisassembleBatchAttribute, AMDisassembleTransactionAttribute, AMDisassembleBatchAttribute | members-01.md | 7162 | 6 |
| PX.Objects.AM.AMDisassembleBatchSplit | EntityType | AM Disassemble Batch Split | BatNbr, DocType, LineNbr, SplitLineNbr | 32 | 3 |  | PX_Objects_AM_AMDisassembleBatchSplit, AMDisassembleBatchSplit | members-01.md | 7169 | 42 |
| PX.Objects.AM.AMDisassembleTran | EntityType | AM Disassemble Transaction | BatNbr, DocType, LineNbr | 2 | 0 | PX.Objects.AM.AMMTran | PX_Objects_AM_AMDisassembleTran, AMDisassembleTransaction, AMDisassembleTran | members-01.md | 7212 | 9 |
| PX.Objects.AM.AMDisassembleTranSplit | EntityType | AM Disassemble Transaction Split | BatNbr, DocType, LineNbr, SplitLineNbr | 0 | 0 | PX.Objects.AM.AMMTranSplit | PX_Objects_AM_AMDisassembleTranSplit, AMDisassembleTransactionSplit, AMDisassembleTranSplit | members-01.md | 7222 | 6 |
| PX.Objects.AM.AMECOItem | EntityType | ECO Item | ECOID | 28 | 12 |  | PX_Objects_AM_AMECOItem, ECOItem, AMECOItem | members-01.md | 7229 | 47 |
| PX.Objects.AM.AMECOSetupApproval | EntityType | ECO Setup Approval | ApprovalID | 12 | 4 |  | PX_Objects_AM_AMECOSetupApproval, ECOSetupApproval, AMECOSetupApproval | members-01.md | 7277 | 23 |
| PX.Objects.AM.AMECRItem | EntityType | ECR Item | ECRID | 29 | 12 |  | PX_Objects_AM_AMECRItem, ECRItem, AMECRItem | members-01.md | 7301 | 48 |
| PX.Objects.AM.AMECRSetupApproval | EntityType | ECR Setup Approval | ApprovalID | 12 | 4 |  | PX_Objects_AM_AMECRSetupApproval, ECRSetupApproval, AMECRSetupApproval | members-01.md | 7350 | 23 |
| PX.Objects.AM.AMEstimateClass | EntityType | Estimate Class | EstimateClassID | 22 | 8 |  | PX_Objects_AM_AMEstimateClass, EstimateClass, AMEstimateClass | members-01.md | 7374 | 37 |
| PX.Objects.AM.AMEstimateHistory | EntityType | Estimate History | EstimateID, LineNbr | 11 | 4 |  | PX_Objects_AM_AMEstimateHistory, EstimateHistory, AMEstimateHistory | members-01.md | 7412 | 21 |
| PX.Objects.AM.AMEstimateItem | EntityType | Estimate Item | EstimateID, RevisionID | 94 | 24 |  | PX_Objects_AM_AMEstimateItem, EstimateItem, AMEstimateItem | members-01.md | 7434 | 125 |
| PX.Objects.AM.AMEstimateMatl | EntityType | Estimate Material | EstimateID, LineID, OperationID, RevisionID | 36 | 12 |  | PX_Objects_AM_AMEstimateMatl, EstimateMaterial, AMEstimateMatl | members-01.md | 7560 | 55 |
| PX.Objects.AM.AMEstimateOper | EntityType | Estimate Operations | EstimateID, OperationCD, RevisionID | 73 | 11 |  | PX_Objects_AM_AMEstimateOper, EstimateOperations, AMEstimateOper | members-01.md | 7616 | 91 |
| PX.Objects.AM.AMEstimateOvhd | EntityType | Estimate Overhead | EstimateID, LineID, OperationID, RevisionID | 21 | 5 |  | PX_Objects_AM_AMEstimateOvhd, EstimateOverhead, AMEstimateOvhd | members-01.md | 7708 | 33 |
| PX.Objects.AM.AMEstimatePriceBreak | EntityType | Estimate Price Break | EstimateID, LineNbr, RevisionID | 66 | 4 |  | PX_Objects_AM_AMEstimatePriceBreak, EstimatePriceBreak, AMEstimatePriceBreak | members-01.md | 7742 | 77 |
| PX.Objects.AM.AMEstimateReference | EntityType | Estimate Reference | EstimateID, RevisionID | 29 | 10 |  | PX_Objects_AM_AMEstimateReference, EstimateReference, AMEstimateReference | members-01.md | 7820 | 46 |
| PX.Objects.AM.AMEstimateSetup | EntityType | Estimate Preferences |  | 21 | 6 |  |  | members-01.md | 7867 | 32 |
| PX.Objects.AM.AMEstimateStep | EntityType | Estimate Step | EstimateID, LineID, OperationID, RevisionID | 15 | 4 |  | PX_Objects_AM_AMEstimateStep, EstimateStep, AMEstimateStep | members-01.md | 7900 | 26 |
| PX.Objects.AM.AMEstimateTool | EntityType | Estimate Tool | EstimateID, LineID, OperationID, RevisionID | 18 | 5 |  | PX_Objects_AM_AMEstimateTool, EstimateTool, AMEstimateTool | members-01.md | 7927 | 30 |
| PX.Objects.AM.AMFeature | EntityType | Feature | FeatureID | 17 | 5 |  | PX_Objects_AM_AMFeature, Feature, AMFeature | members-01.md | 7958 | 29 |
| PX.Objects.AM.AMFeatureAttribute | EntityType | Feature Attribute | FeatureID, LineNbr | 18 | 4 |  | PX_Objects_AM_AMFeatureAttribute, FeatureAttribute, AMFeatureAttribute | members-01.md | 7988 | 29 |
| PX.Objects.AM.AMFeatureOption | EntityType | Feature Option | FeatureID, LineNbr | 29 | 5 |  | PX_Objects_AM_AMFeatureOption, FeatureOption, AMFeatureOption | members-01.md | 8018 | 40 |
| PX.Objects.AM.AMFixedDemand | EntityType | AM Fixed Demand | PlanID | 28 | 5 | PX.Objects.IN.INItemPlan | PX_Objects_AM_AMFixedDemand, AMFixedDemand | members-01.md | 8059 | 41 |
| PX.Objects.AM.AMForecast | EntityType | Forecast | ForecastID | 20 | 12 |  | PX_Objects_AM_AMForecast, Forecast, AMForecast | members-01.md | 8101 | 39 |
| PX.Objects.AM.AMForecastPeriod | EntityType | Forecast Period | ForecastID, PeriodEnd, PeriodStart, TimePeriod | 11 | 3 |  | PX_Objects_AM_AMForecastPeriod, ForecastPeriod, AMForecastPeriod | members-01.md | 8141 | 20 |
| PX.Objects.AM.AMForecastStaging | EntityType | Forecast Staging | BeginDate, CustomerID, EndDate, InventoryID, SiteID, SubItemID, UserID | 23 | 10 |  | PX_Objects_AM_AMForecastStaging, ForecastStaging, AMForecastStaging | members-01.md | 8162 | 40 |
| PX.Objects.AM.AMLaborCode | EntityType | Labor Code | LaborCodeID | 12 | 8 |  | PX_Objects_AM_AMLaborCode, LaborCode, AMLaborCode | members-01.md | 8203 | 27 |
| PX.Objects.AM.AMMach | EntityType | Machine | MachID | 17 | 9 |  | PX_Objects_AM_AMMach, Machine, AMMach | members-01.md | 8231 | 33 |
| PX.Objects.AM.AMMachCurySettings | EntityType | Machine Currency Settings | CuryID, MachID | 10 | 4 |  | PX_Objects_AM_AMMachCurySettings, MachineCurrencySettings, AMMachCurySettings | members-01.md | 8265 | 20 |
| PX.Objects.AM.AMMachSchd | EntityType | Work Center Schedule | MachID, SchdDate | 19 | 5 |  | PX_Objects_AM_AMMachSchd, WorkCenterSchedule, AMMachSchd | members-01.md | 8286 | 31 |
| PX.Objects.AM.AMMachSchdDetail | EntityType | Machine Schedule Detail | RecordID | 23 | 5 |  | PX_Objects_AM_AMMachSchdDetail, MachineScheduleDetail, AMMachSchdDetail | members-01.md | 8318 | 35 |
| PX.Objects.AM.AMMPS | EntityType | Master Production Schedule | MPSID, MPSTypeID | 18 | 9 |  | PX_Objects_AM_AMMPS, MasterProductionSchedule, AMMPS | members-01.md | 8354 | 34 |
| PX.Objects.AM.AMMPSType | EntityType | Master Production Schedule Type | MPSTypeID | 13 | 5 |  | PX_Objects_AM_AMMPSType, MasterProductionScheduleType, AMMPSType | members-01.md | 8389 | 25 |
| PX.Objects.AM.AMMRPBucket | EntityType | Inventory Planning Buckets | BucketID | 12 | 5 |  | PX_Objects_AM_AMMRPBucket, InventoryPlanningBuckets, AMMRPBucket | members-01.md | 8415 | 24 |
| PX.Objects.AM.AMMRPBucketDetail | EntityType | Inventory Planning Bucket Detail | Bucket, BucketID | 11 | 3 |  | PX_Objects_AM_AMMRPBucketDetail, InventoryPlanningBucketDetail, AMMRPBucketDetail | members-01.md | 8440 | 20 |
| PX.Objects.AM.AMMRPBucketDetailInq | EntityType | Inventory Planning Bucket Detail Inquiry | Bucket, BucketID, InventoryID, SiteID, SubItemID | 21 | 6 |  | PX_Objects_AM_AMMRPBucketDetailInq, InventoryPlanningBucketDetailInquiry, AMMRPBucketDetailInq | members-01.md | 8461 | 33 |
| PX.Objects.AM.AMMRPBucketInq | EntityType | Inventory Planning Bucket Inquiry | BucketID, InventoryID, SiteID, SubItemID | 17 | 9 |  | PX_Objects_AM_AMMRPBucketInq, InventoryPlanningBucketInquiry, AMMRPBucketInq | members-01.md | 8495 | 32 |
| PX.Objects.AM.AMMTran | EntityType | AM Transaction | BatNbr, DocType, LineNbr | 76 | 40 |  | PX_Objects_AM_AMMTran, AMTransaction, AMMTran | members-01.md | 8528 | 123 |
| PX.Objects.AM.AMMTranAttribute | EntityType | Transaction Attributes | BatNbr, DocType, LineNbr, ProdAttributeLineNbr, TranLineNbr | 20 | 11 |  | PX_Objects_AM_AMMTranAttribute, TransactionAttributes, AMMTranAttribute | members-01.md | 8652 | 37 |
| PX.Objects.AM.AMMTranLotSerialNbrAll | EntityType | AM Transaction All Lot/Serial Nbr | BatNbr, DocType, LineNbr | 8 | 10 |  | PX_Objects_AM_AMMTranLotSerialNbrAll, AMTransactionAllLotSerialNbr, AMMTranLotSerialNbrAll | members-01.md | 8690 | 24 |
| PX.Objects.AM.AMMTranMoveByLotSerial | EntityType | AM Transaction by LotSerial | BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID, SiteID | 7 | 4 |  | PX_Objects_AM_AMMTranMoveByLotSerial, AMTransactionbyLotSerial, AMMTranMoveByLotSerial | members-01.md | 8715 | 17 |
| PX.Objects.AM.AMMTranSplit | EntityType | AM Transaction Split | BatNbr, DocType, LineNbr, SplitLineNbr | 33 | 13 |  | PX_Objects_AM_AMMTranSplit, AMTransactionSplit, AMMTranSplit | members-01.md | 8733 | 53 |
| PX.Objects.AM.AMOrderCrossRef | EntityType | Order Cross Reference | LineNbr, UserID | 29 | 7 |  | PX_Objects_AM_AMOrderCrossRef, OrderCrossReference, AMOrderCrossRef | members-01.md | 8787 | 43 |
| PX.Objects.AM.AMOrderType | EntityType | AM Order Types | OrderType | 38 | 46 |  | PX_Objects_AM_AMOrderType, AMOrderTypes, AMOrderType | members-01.md | 8831 | 91 |
| PX.Objects.AM.AMOrderTypeAttribute | EntityType | Order Type Attributes | LineNbr, OrderType | 15 | 4 |  | PX_Objects_AM_AMOrderTypeAttribute, OrderTypeAttributes, AMOrderTypeAttribute | members-01.md | 8923 | 25 |
| PX.Objects.AM.AMOverhead | EntityType | Overhead | OvhdID | 13 | 9 |  | PX_Objects_AM_AMOverhead, Overhead, AMOverhead | members-01.md | 8949 | 29 |
| PX.Objects.AM.AMOverheadCurySettings | EntityType | Overhead Currency Settings | CuryID, OvhdID | 10 | 4 |  | PX_Objects_AM_AMOverheadCurySettings, OverheadCurrencySettings, AMOverheadCurySettings | members-01.md | 8979 | 20 |
| PX.Objects.AM.AMProdAttribute | EntityType | Production Attributes | LineNbr, OrderType, ProdOrdID | 19 | 8 |  | PX_Objects_AM_AMProdAttribute, ProductionAttributes, AMProdAttribute | members-01.md | 9000 | 33 |
| PX.Objects.AM.AMProdEvnt | EntityType | Production Event | LineNbr, OrderType, ProdOrdID | 16 | 5 |  | PX_Objects_AM_AMProdEvnt, ProductionEvent, AMProdEvnt | members-01.md | 9034 | 28 |
| PX.Objects.AM.AMProdItem | EntityType | Production Item | OrderType, ProdOrdID | 92 | 72 |  | PX_Objects_AM_AMProdItem, ProductionItem, AMProdItem | members-01.md | 9063 | 171 |
| PX.Objects.AM.AMProdItemRelated | EntityType | Related Production Item | OrderType, ProdOrdID | 28 | 3 |  | PX_Objects_AM_AMProdItemRelated, RelatedProductionItem, AMProdItemRelated | members-01.md | 9235 | 38 |
| PX.Objects.AM.AMProdItemSplit | EntityType | Production Item Split | OrderType, ProdOrdID, SplitLineNbr | 35 | 12 |  | PX_Objects_AM_AMProdItemSplit, ProductionItemSplit, AMProdItemSplit | members-01.md | 9274 | 54 |
| PX.Objects.AM.AMProdItemSplitPreassign | EntityType | Prod Item Split Lot/Serial | LotSerialNbr, OrderType, ProdOrdID | 27 | 5 |  | PX_Objects_AM_AMProdItemSplitPreassign, ProdItemSplitLotSerial, AMProdItemSplitPreassign | members-01.md | 9329 | 39 |
| PX.Objects.AM.AMProdMatl | EntityType | Production Material | LineID, OperationID, OrderType, ProdOrdID | 69 | 20 |  | PX_Objects_AM_AMProdMatl, ProductionMaterial, AMProdMatl | members-01.md | 9369 | 96 |
| PX.Objects.AM.AMProdMatlLotSerial | EntityType | Production Material Lot/Serial Nbr. | LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID | 13 | 6 |  | PX_Objects_AM_AMProdMatlLotSerial, ProductionMaterialLotSerialNbr, AMProdMatlLotSerial | members-01.md | 9466 | 25 |
| PX.Objects.AM.AMProdMatlLotSerialAssigned | EntityType | Material Lot Serial Assigned | LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID | 20 | 0 |  | PX_Objects_AM_AMProdMatlLotSerialAssigned, MaterialLotSerialAssigned, AMProdMatlLotSerialAssigned | members-01.md | 9492 | 27 |
| PX.Objects.AM.AMProdMatlLotSerialUnassigned | EntityType | Material Lot Serial Unassigned | LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID | 21 | 0 |  | PX_Objects_AM_AMProdMatlLotSerialUnassigned, MaterialLotSerialUnassigned, AMProdMatlLotSerialUnassigned | members-01.md | 9520 | 28 |
| PX.Objects.AM.AMProdMatlSplit | EntityType | Production Material Split | LineID, OperationID, OrderType, ProdOrdID, SplitLineNbr | 50 | 17 |  | PX_Objects_AM_AMProdMatlSplit, ProductionMaterialSplit, AMProdMatlSplit | members-01.md | 9549 | 74 |
| PX.Objects.AM.AMProdNumber | EntityType | Production Number | OrderType, ProdOrdID | 10 | 5 |  | PX_Objects_AM_AMProdNumber, ProductionNumber, AMProdNumber | members-01.md | 9624 | 21 |
| PX.Objects.AM.AMProdOper | EntityType | Production Operation | OperationCD, OrderType, ProdOrdID | 117 | 30 |  | PX_Objects_AM_AMProdOper, ProductionOperation, AMProdOper | members-01.md | 9646 | 154 |
| PX.Objects.AM.AMProdOvhd | EntityType | Production Overhead | LineID, OperationID, OrderType, ProdOrdID | 26 | 6 |  | PX_Objects_AM_AMProdOvhd, ProductionOverhead, AMProdOvhd | members-01.md | 9801 | 39 |
| PX.Objects.AM.AMProdStep | EntityType | Production Step | LineID, OperationID, OrderType, ProdOrdID | 24 | 5 |  | PX_Objects_AM_AMProdStep, ProductionStep, AMProdStep | members-01.md | 9841 | 36 |
| PX.Objects.AM.AMProdTool | EntityType | Production Tool | LineID, OperationID, OrderType, ProdOrdID | 28 | 6 |  | PX_Objects_AM_AMProdTool, ProductionTool, AMProdTool | members-01.md | 9878 | 41 |
| PX.Objects.AM.AMProdTotal | EntityType | Production Totals | OrderType, ProdOrdID | 51 | 6 |  | PX_Objects_AM_AMProdTotal, ProductionTotals, AMProdTotal | members-01.md | 9920 | 64 |
| PX.Objects.AM.AMPSetup | EntityType | Production Preferences |  | 28 | 11 |  |  | members-01.md | 9985 | 44 |
| PX.Objects.AM.AMRPAuditHistory | EntityType | Inventory Planning Audit History | Recno | 8 | 1 |  | PX_Objects_AM_AMRPAuditHistory, InventoryPlanningAuditHistory, AMRPAuditHistory | members-01.md | 10030 | 15 |
| PX.Objects.AM.AMRPAuditTable | EntityType | Inventory Planning Audit | Recno | 8 | 1 |  | PX_Objects_AM_AMRPAuditTable, InventoryPlanningAudit, AMRPAuditTable | members-01.md | 10046 | 15 |
| PX.Objects.AM.AMRPDetail | EntityType | Inventory Planning Detail | RecordID | 36 | 21 |  | PX_Objects_AM_AMRPDetail, InventoryPlanningDetail, AMRPDetail | members-01.md | 10062 | 63 |
| PX.Objects.AM.AMRPDetailFP | EntityType | Inventory Planning First Pass Detail | RecordID | 45 | 15 |  | PX_Objects_AM_AMRPDetailFP, InventoryPlanningFirstPassDetail, AMRPDetailFP | members-01.md | 10126 | 67 |
| PX.Objects.AM.AMRPDetailPlan | EntityType | Inventory Planning Detail Plan | PlanID | 23 | 10 |  | PX_Objects_AM_AMRPDetailPlan, InventoryPlanningDetailPlan, AMRPDetailPlan | members-01.md | 10194 | 40 |
| PX.Objects.AM.AMRPExceptions | EntityType | Inventory Planning Exceptions | RecordID | 14 | 8 |  | PX_Objects_AM_AMRPExceptions, InventoryPlanningExceptions, AMRPExceptions | members-01.md | 10235 | 28 |
| PX.Objects.AM.AMRPHistory | EntityType | Inventory Planning History | ProcessID | 15 | 1 |  | PX_Objects_AM_AMRPHistory, InventoryPlanningHistory, AMRPHistory | members-01.md | 10264 | 22 |
| PX.Objects.AM.AMRPItemSite | EntityType | Inventory Planning Inventory | InventoryID, SiteID, SubItemID | 22 | 9 |  | PX_Objects_AM_AMRPItemSite, InventoryPlanningInventory, AMRPItemSite | members-01.md | 10287 | 37 |
| PX.Objects.AM.AMRPPlan | EntityType | MRP Plan | RecordID | 19 | 9 |  | PX_Objects_AM_AMRPPlan, MRPPlan, AMRPPlan | members-01.md | 10325 | 35 |
| PX.Objects.AM.AMRPSetup | EntityType | Inventory Planning Preferences |  | 23 | 4 |  |  | members-01.md | 10361 | 32 |
| PX.Objects.AM.AMScanSetup | EntityType | AM Scan Setup | BranchID | 20 | 2 |  | PX_Objects_AM_AMScanSetup, AMScanSetup | members-01.md | 10394 | 28 |
| PX.Objects.AM.AMScanUserSetup | EntityType | AM Scan User Setup | Mode, UserID | 6 | 0 |  | PX_Objects_AM_AMScanUserSetup, AMScanUserSetup | members-01.md | 10423 | 12 |
| PX.Objects.AM.AMSchdItem | EntityType | Schedule Item | OrderType, ProdOrdID, SchdID | 31 | 7 |  | PX_Objects_AM_AMSchdItem, ScheduleItem, AMSchdItem | members-01.md | 10436 | 45 |
| PX.Objects.AM.AMSchdOper | EntityType | Schedule Operation | LineNbr, OperationID, OrderType, ProdOrdID, SchdID | 37 | 8 |  | PX_Objects_AM_AMSchdOper, ScheduleOperation, AMSchdOper | members-01.md | 10482 | 52 |
| PX.Objects.AM.AMSchdOperDetail | EntityType | Scheduled Operation Details | RecordID | 20 | 6 |  | PX_Objects_AM_AMSchdOperDetail, ScheduledOperationDetails, AMSchdOperDetail | members-01.md | 10535 | 32 |
| PX.Objects.AM.AMShift | EntityType | Shift | ShiftCD, WcID | 16 | 8 |  | PX_Objects_AM_AMShift, Shift, AMShift | members-01.md | 10568 | 31 |
| PX.Objects.AM.AMSiteTransfer | EntityType | Warehouse Transfer | SiteID, TransferSiteID | 10 | 4 |  | PX_Objects_AM_AMSiteTransfer, WarehouseTransfer, AMSiteTransfer | members-01.md | 10600 | 20 |
| PX.Objects.AM.AMSubItemDefault | EntityType | Subitem Default | InventoryID, SiteID, SubItemID | 13 | 6 |  | PX_Objects_AM_AMSubItemDefault, SubitemDefault, AMSubItemDefault | members-01.md | 10621 | 25 |
| PX.Objects.AM.AMToolMst | EntityType | Tools | ToolID | 13 | 9 |  | PX_Objects_AM_AMToolMst, Tools, AMToolMst | members-01.md | 10647 | 29 |
| PX.Objects.AM.AMToolMstCurySettings | EntityType | Tools Currency Settings | CuryID, ToolID | 12 | 4 |  | PX_Objects_AM_AMToolMstCurySettings, ToolsCurrencySettings, AMToolMstCurySettings | members-01.md | 10677 | 22 |
| PX.Objects.AM.AMToolSchdDetail | EntityType | Tool Schedule Detail | RecordID | 26 | 4 |  | PX_Objects_AM_AMToolSchdDetail, ToolScheduleDetail, AMToolSchdDetail | members-01.md | 10700 | 37 |
| PX.Objects.AM.AMTranCost | EntityType | AM Transaction Cost | BatNbr, DocType, LineNbr | 49 | 18 |  | PX_Objects_AM_AMTranCost, AMTransactionCost, AMTranCost | members-01.md | 10738 | 74 |
| PX.Objects.AM.AMVendorShipLine | EntityType | Vendor Shipment Line | LineNbr, ShipmentNbr | 31 | 19 |  | PX_Objects_AM_AMVendorShipLine, VendorShipmentLine, AMVendorShipLine | members-01.md | 10813 | 57 |
| PX.Objects.AM.AMVendorShipLineSplit | EntityType | Vendor Shipment Line Split | LineNbr, ShipmentNbr, SplitLineNbr | 29 | 10 |  | PX_Objects_AM_AMVendorShipLineSplit, VendorShipmentLineSplit, AMVendorShipLineSplit | members-01.md | 10871 | 46 |
| PX.Objects.AM.AMVendorShipment | EntityType | Vendor Shipment | ShipmentNbr | 44 | 18 |  | PX_Objects_AM_AMVendorShipment, VendorShipment, AMVendorShipment | members-01.md | 10918 | 69 |
| PX.Objects.AM.AMVendorShipmentAddress | EntityType | Vendor Shipment Address | AddressID | 34 | 5 |  | PX_Objects_AM_AMVendorShipmentAddress, VendorShipmentAddress, AMVendorShipmentAddress | members-01.md | 10988 | 46 |
| PX.Objects.AM.AMVendorShipmentContact | EntityType | Vendor Shipment Contact | ContactID | 27 | 3 |  | PX_Objects_AM_AMVendorShipmentContact, VendorShipmentContact, AMVendorShipmentContact | members-01.md | 11035 | 37 |
| PX.Objects.AM.AMWC | EntityType | Work Center | WcID | 24 | 23 |  | PX_Objects_AM_AMWC, WorkCenter, AMWC | members-01.md | 11073 | 54 |
| PX.Objects.AM.AMWCCalendarPeriod | EntityType | Work Center Calendar Period | SequenceNbr, WcID | 20 | 3 |  | PX_Objects_AM_AMWCCalendarPeriod, WorkCenterCalendarPeriod, AMWCCalendarPeriod | members-01.md | 11128 | 30 |
| PX.Objects.AM.AMWCCury | EntityType | AMWCCurrency | CuryID, DetailID, WcID | 11 | 2 |  | PX_Objects_AM_AMWCCury, AMWCCurrency, AMWCCury | members-01.md | 11159 | 19 |
| PX.Objects.AM.AMWCCurySettings | EntityType | Work Center Currency Settings | CuryID, DetailID, WcID | 11 | 4 |  | PX_Objects_AM_AMWCCurySettings, WorkCenterCurrencySettings, AMWCCurySettings | members-01.md | 11179 | 21 |
| PX.Objects.AM.AMWCMach | EntityType | Work Center Machines | MachID, WcID | 13 | 7 |  | PX_Objects_AM_AMWCMach, WorkCenterMachines, AMWCMach | members-01.md | 11201 | 27 |
| PX.Objects.AM.AMWCMachCury | EntityType | AMWCMachCury | CuryID, DetailID, WcID | 11 | 2 |  | PX_Objects_AM_AMWCMachCury, AMWCMachCury | members-01.md | 11229 | 19 |
| PX.Objects.AM.AMWCOvhd | EntityType | Work Center Overheads | OvhdID, WcID | 12 | 4 |  | PX_Objects_AM_AMWCOvhd, WorkCenterOverheads, AMWCOvhd | members-01.md | 11249 | 23 |
| PX.Objects.AM.AMWCSchd | EntityType | Work Center Schedule | SchdDate, ShiftCD, WcID | 18 | 7 |  | PX_Objects_AM_AMWCSchd, WorkCenterSchedule1, AMWCSchd | members-01.md | 11273 | 32 |
| PX.Objects.AM.AMWCSchdDetail | EntityType | Work Center Schedule Detail | RecordID | 24 | 7 |  | PX_Objects_AM_AMWCSchdDetail, WorkCenterScheduleDetail, AMWCSchdDetail | members-01.md | 11306 | 38 |
| PX.Objects.AM.AMWCSubstitute | EntityType | Work Center Substitute | SiteID, WcID | 11 | 5 |  | PX_Objects_AM_AMWCSubstitute, WorkCenterSubstitute, AMWCSubstitute | members-01.md | 11345 | 22 |
| PX.Objects.AM.AMWrkMatl | EntityType | Material Work Temp | AutoNbr | 26 | 12 |  | PX_Objects_AM_AMWrkMatl, MaterialWorkTemp, AMWrkMatl | members-01.md | 11368 | 44 |
| PX.Objects.AM.BomInventoryItem | EntityType | BOM Inventory Item | InventoryCD | 0 | 0 | PX.Objects.IN.InventoryItem | PX_Objects_AM_BomInventoryItem, BOMInventoryItem | members-01.md | 11413 | 6 |
| PX.Objects.AM.BomWhereUsedDetail | EntityType | BOM Where Used Detail | BOMID, LineID, OperationID, RevisionID, Sequence | 49 | 0 |  | PX_Objects_AM_BomWhereUsedDetail, BOMWhereUsedDetail | members-01.md | 11420 | 56 |
| PX.Objects.AM.CacheExtensions.INItemPlanAMExtension | EntityType | AM Item Plan | InventoryID, PlanID | 3 | 3 |  | PX_Objects_AM_CacheExtensions_INItemPlanAMExtension, AMItemPlan, INItemPlanAMExtension | members-01.md | 11477 | 12 |
| PX.Objects.AM.PrintProductionOrders | EntityType | Print Production Orders | OrderType, ProdOrdID | 1 | 0 | PX.Objects.AM.AMProdItem | PX_Objects_AM_PrintProductionOrders, PrintProductionOrders | members-01.md | 11490 | 8 |
| PX.Objects.AM.ProdOperAdjusted | EntityType | Production Operation Adjusted | OperationID, OrderType, ProdOrdID | 28 | 0 |  | PX_Objects_AM_ProdOperAdjusted, ProductionOperationAdjusted, ProdOperAdjusted | members-01.md | 11499 | 35 |
| PX.Objects.AM.ProdOperMatl | EntityType | Production Operations & Materials | OperationCD, OrderType, ProdOrdID | 36 | 0 | PX.Objects.AM.AMProdOper | PX_Objects_AM_ProdOperMatl, ProductionOperationsMaterials, ProdOperMatl | members-01.md | 11535 | 44 |
| PX.Objects.AM.ProductionOrderBuildCapabilityMaterial | EntityType | Production Order Build Capability Material | ProdOrdID | 11 | 41 |  | PX_Objects_AM_ProductionOrderBuildCapabilityMaterial, ProductionOrderBuildCapabilityMaterial | members-01.md | 11580 | 58 |
| PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation | EntityType | Production Order Build Capability Material | ProdOrdID | 11 | 41 |  | PX_Objects_AM_ProductionOrderBuildCapabilityMaterialFirstOperation, ProductionOrderBuildCapabilityMaterial1, ProductionOrderBuildCapabilityMaterialFirstOperation | members-01.md | 11639 | 58 |
| PX.Objects.AM.ProductionReadinessByAllOperations | ComplexType |  |  | 4 | 0 |  |  | members-01.md | 11698 | 7 |
| PX.Objects.AM.ProductionReadinessByFirstOperation | ComplexType |  |  | 4 | 0 |  |  | members-01.md | 11706 | 7 |
| PX.Objects.AM.ProductionReadinessByProdItem | EntityType | Production Readiness By ProdItem | OrderType, ProdOrdID | 3 | 0 | PX.Objects.AM.AMProdItem | PX_Objects_AM_ProductionReadinessByProdItem, ProductionReadinessByProdItem | members-01.md | 11714 | 11 |
| PX.Objects.AM.SchedulerMachineOperation | EntityType | Machines event | CustomerID, OrderType, ProdOrdID | 41 | 2 |  | PX_Objects_AM_SchedulerMachineOperation, Machinesevent, SchedulerMachineOperation | members-01.md | 11726 | 50 |
| PX.Objects.AM.SchedulerMachineResource | EntityType | Machines resources | Id | 1 | 0 |  | PX_Objects_AM_SchedulerMachineResource, Machinesresources, SchedulerMachineResource | members-01.md | 11777 | 7 |
| PX.Objects.AM.SchedulerProductionOrder | EntityType | Production orders resources | CustomerID, Id, InventoryCD, OrderType, ProdOrdID | 65 | 5 |  | PX_Objects_AM_SchedulerProductionOrder, Productionordersresources, SchedulerProductionOrder | members-01.md | 11785 | 77 |
| PX.Objects.AM.SchedulerWCOperation | EntityType | Work centers operation | CustomerID, InventoryCD, OrderType, ProdOrdID | 64 | 5 |  | PX_Objects_AM_SchedulerWCOperation, Workcentersoperation, SchedulerWCOperation | members-01.md | 11863 | 76 |
| PX.Objects.AM.SchedulerWCResource | EntityType | Work centers resources | Id | 7 | 1 |  | PX_Objects_AM_SchedulerWCResource, Workcentersresources, SchedulerWCResource | members-01.md | 11940 | 15 |
| PX.Objects.AM.SelectedProdMatl | EntityType | Production Material | IsAllocated, LineID, OperationID, OrderType, ProdOrdID, SplitLineNbr | 61 | 10 |  | PX_Objects_AM_SelectedProdMatl, ProductionMaterial1, SelectedProdMatl | members-01.md | 11956 | 78 |
| PX.Objects.AM.SFK.AMClockTranUnapprovedSum | EntityType | Unapproved Clock Entries Sum | OperationID, OrderType, ProdOrdID | 4 | 0 |  | PX_Objects_AM_SFK_AMClockTranUnapprovedSum, UnapprovedClockEntriesSum, AMClockTranUnapprovedSum | members-01.md | 12035 | 10 |
| PX.Objects.AM.SFK.AMMTranScrap | EntityType | AM Transaction | BatNbr, DocType, LineNbr | 1 | 0 | PX.Objects.AM.AMMTran | PX_Objects_AM_SFK_AMMTranScrap, AMTransaction1, AMMTranScrap | members-01.md | 12046 | 9 |
| PX.Objects.AM.SFK.AMMTranSplitScrap | EntityType | AM Transaction Split | BatNbr, DocType, LineNbr, SplitLineNbr | 2 | 0 | PX.Objects.AM.AMMTranSplit | PX_Objects_AM_SFK_AMMTranSplitScrap, AMTransactionSplit1, AMMTranSplitScrap | members-01.md | 12056 | 10 |
| PX.Objects.AM.SFK.AMSFKRecentActivity | EntityType | SFK Recent Activity | RecordID | 12 | 6 |  | PX_Objects_AM_SFK_AMSFKRecentActivity, SFKRecentActivity, AMSFKRecentActivity | members-01.md | 12067 | 24 |
| PX.Objects.AM.SFK.OperationsInProgressProjection | EntityType | Operations In Progress View | EmployeeID, LineNbr | 25 | 3 |  | PX_Objects_AM_SFK_OperationsInProgressProjection, OperationsInProgressView, OperationsInProgressProjection | members-01.md | 12092 | 34 |
| PX.Objects.AM.SFK.OperationView | EntityType | Operation View | OperationID, OrderType, ProdOrdID | 9 | 0 |  | PX_Objects_AM_SFK_OperationView, OperationView | members-01.md | 12127 | 16 |
| PX.Objects.AM.SFK.SFKEmployeeProjection | EntityType | Shop Floor Employee | BAccountID | 10 | 61 |  | PX_Objects_AM_SFK_SFKEmployeeProjection, ShopFloorEmployee, SFKEmployeeProjection | members-01.md | 12144 | 77 |
| PX.Objects.AM.SFK.SFKIssueMaterialsFilter | EntityType | Production Operation Materials View | LineID, OperationID, OrderType, ProdOrdID | 36 | 5 |  | PX_Objects_AM_SFK_SFKIssueMaterialsFilter, ProductionOperationMaterialsView, SFKIssueMaterialsFilter | members-01.md | 12222 | 48 |
| PX.Objects.AM.SFK.SFKLotSerialNbrResult | EntityType | SFK Lot/Serial by Attributes | InventoryID, LocationID, LotSerialNbr, SiteID | 13 | 1 |  | PX_Objects_AM_SFK_SFKLotSerialNbrResult, SFKLotSerialbyAttributes, SFKLotSerialNbrResult | members-01.md | 12271 | 21 |
| PX.Objects.AM.SFK.SFKOperationFileProjection | EntityType | Operation file | FileID | 21 | 2 |  | PX_Objects_AM_SFK_SFKOperationFileProjection, Operationfile, SFKOperationFileProjection | members-01.md | 12293 | 30 |
| PX.Objects.AM.SFK.SFKOperationsByWCProjection | EntityType | Operations In Work Centers | OperationCD, OperationID, OrderType, ProdOrdID | 1 | 0 | PX.Objects.AM.SFK.SFKProdOperProjection | PX_Objects_AM_SFK_SFKOperationsByWCProjection, OperationsInWorkCenters, SFKOperationsByWCProjection | members-01.md | 12324 | 9 |
| PX.Objects.AM.SFK.SFKProdOperMaterialsProjection | EntityType | Production Operation Materials View | LineID, OperationID, OrderType, ProdOrdID | 35 | 9 |  | PX_Objects_AM_SFK_SFKProdOperMaterialsProjection, ProductionOperationMaterialsView1, SFKProdOperMaterialsProjection | members-01.md | 12334 | 51 |
| PX.Objects.AM.SFK.SFKProdOperProjection | EntityType | Production Operations View | OperationCD, OperationID, OrderType, ProdOrdID | 44 | 15 |  | PX_Objects_AM_SFK_SFKProdOperProjection, ProductionOperationsView, SFKProdOperProjection | members-01.md | 12386 | 66 |
| PX.Objects.AM.SFK.SFKProductionOrderProjection | EntityType | Production Order View | OrderType, ProdOrdID | 24 | 3 |  | PX_Objects_AM_SFK_SFKProductionOrderProjection, ProductionOrderView, SFKProductionOrderProjection | members-01.md | 12453 | 33 |
| PX.Objects.AM.SFK.SFKSubtractSplit | EntityType | SFK Subtract Lot/Serial | BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID | 12 | 0 |  | PX_Objects_AM_SFK_SFKSubtractSplit, SFKSubtractLotSerial, SFKSubtractSplit | members-01.md | 12487 | 19 |
| PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum | EntityType | Completed Quantities Summary | BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID | 10 | 0 |  | PX_Objects_AM_SFK_SFKTranSplitCompletedByLotSerialSum, CompletedQuantitiesSummary, SFKTranSplitCompletedByLotSerialSum | members-01.md | 12507 | 16 |
| PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum | EntityType | Scrap Quantities Summary | BatNbr, DocType, LotSerialNbr, OperationCD, OperationID, OrderType, ProdOrdID | 12 | 0 |  | PX_Objects_AM_SFK_SFKTranSplitScrapByLotSerialSum, ScrapQuantitiesSummary, SFKTranSplitScrapByLotSerialSum | members-01.md | 12524 | 18 |
| PX.Objects.AM.SubAssemblyProjection | EntityType | Sub-Assembly Projection | OrderType, ProdOrdID | 9 | 0 | PX.Objects.AM.AMProdItem | PX_Objects_AM_SubAssemblyProjection, SubAssemblyProjection | members-01.md | 12543 | 16 |
| PX.Objects.AP.AP1099Box | EntityType | AP 1099 Box | BoxCD, BoxNbr | 6 | 4 |  | PX_Objects_AP_AP1099Box, AP1099Box | members-01.md | 12560 | 17 |
| PX.Objects.AP.AP1099History | EntityType | AP 1099 History | BoxNbr, BranchID, FinYear, VendorID | 6 | 3 |  | PX_Objects_AP_AP1099History, AP1099History | members-01.md | 12578 | 15 |
| PX.Objects.AP.AP1099HistoryByPayer | ComplexType |  |  | 5 | 0 |  |  | members-01.md | 12594 | 8 |
| PX.Objects.AP.AP1099Year | EntityType | AP 1099 Year | FinYear, OrganizationID | 6 | 2 |  | PX_Objects_AP_AP1099Year, AP1099Year | members-01.md | 12603 | 14 |
| PX.Objects.AP.APAddItemSelected | EntityType |  | InventoryID | 17 | 6 |  | PX_Objects_AP_APAddItemSelected | members-01.md | 12618 | 29 |
| PX.Objects.AP.APAddress | EntityType | AP Address | AddressID | 36 | 6 |  | PX_Objects_AP_APAddress, APAddress | members-01.md | 12648 | 49 |
| PX.Objects.AP.APAdjust | EntityType | Adjust | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 91 | 25 |  | PX_Objects_AP_APAdjust, Adjust, APAdjust | members-01.md | 12698 | 123 |
| PX.Objects.AP.APAdjustedBalanceAtDate | EntityType | APAdjustedBalanceAtDate | DocType, RefNbr, SubmissionDate | 5 | 18 |  | PX_Objects_AP_APAdjustedBalanceAtDate, APAdjustedBalanceAtDate | members-01.md | 12822 | 30 |
| PX.Objects.AP.APAdjustingBalanceAtDate | EntityType | APAdjustingBalanceAtDate | DocType, RefNbr, SubmissionDate | 5 | 18 |  | PX_Objects_AP_APAdjustingBalanceAtDate, APAdjustingBalanceAtDate | members-01.md | 12853 | 30 |
| PX.Objects.AP.APAROrd | EntityType | APAROrd | Ord | 1 | 0 |  | PX_Objects_AP_APAROrd, APAROrd | members-01.md | 12884 | 7 |
| PX.Objects.AP.APCashRequirementsReport | EntityType | Cash Requirement | DocType, RefNbr | 34 | 26 |  | PX_Objects_AP_APCashRequirementsReport, CashRequirement, APCashRequirementsReport | members-01.md | 12892 | 67 |
| PX.Objects.AP.APContact | EntityType | AP Contact | ContactID | 27 | 6 |  | PX_Objects_AP_APContact, APContact | members-01.md | 12960 | 40 |
| PX.Objects.AP.APDiscount | EntityType | AP Discount | BAccountID, DiscountID | 17 | 12 |  | PX_Objects_AP_APDiscount, APDiscount | members-01.md | 13001 | 35 |
| PX.Objects.AP.APDiscountLocation | EntityType | AP Discount Location | DiscountID, DiscountSequenceID, VendorID | 10 | 5 |  | PX_Objects_AP_APDiscountLocation, APDiscountLocation | members-01.md | 13037 | 21 |
| PX.Objects.AP.APDiscountVendor | EntityType | AP Discount Vendor | DiscountID, DiscountSequenceID, VendorID | 10 | 5 |  | PX_Objects_AP_APDiscountVendor, APDiscountVendor | members-01.md | 13059 | 21 |
| PX.Objects.AP.APHistory | EntityType | AP History | AccountID, BranchID, FinPeriodID, SubID, VendorID | 54 | 6 |  | PX_Objects_AP_APHistory, APHistory | members-01.md | 13081 | 67 |
| PX.Objects.AP.APHistoryByPeriod | EntityType | AP History by Period | AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID | 7 | 2 |  | PX_Objects_AP_APHistoryByPeriod, APHistorybyPeriod | members-01.md | 13149 | 15 |
| PX.Objects.AP.APHistoryTran | ComplexType |  |  | 25 | 0 |  |  | members-01.md | 13165 | 28 |
| PX.Objects.AP.APInvoice | EntityType | AP document | DocType, RefNbr | 43 | 30 | PX.Objects.AP.APRegister | PX_Objects_AP_APInvoice, APdocument, APInvoice | members-01.md | 13194 | 81 |
| PX.Objects.AP.APInvoiceDiscountDetail | EntityType | AP Invoice Discount Detail | DocType, RecordID, RefNbr | 33 | 10 |  | PX_Objects_AP_APInvoiceDiscountDetail, APInvoiceDiscountDetail | members-01.md | 13276 | 50 |
| PX.Objects.AP.APInvoiceExt | EntityType | AP document | DocType, RefNbr | 16 | 5 | PX.Objects.AP.APInvoice | PX_Objects_AP_APInvoiceExt | members-01.md | 13327 | 29 |
| PX.Objects.AP.APInvoiceRetainageBalanceAtDate | EntityType | APInvoiceRetainageBalanceAtDate | DocType, RefNbr, SubmissionDate | 4 | 18 |  | PX_Objects_AP_APInvoiceRetainageBalanceAtDate, APInvoiceRetainageBalanceAtDate | members-01.md | 13357 | 28 |
| PX.Objects.AP.APLineTax | EntityType | AP Line Tax | LineNbr, RefNbr, TranType | 5 | 2 |  | PX_Objects_AP_APLineTax, APLineTax | members-01.md | 13386 | 13 |
| PX.Objects.AP.APNotification | EntityType | AP Notification | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_AP_APNotification, APNotification | members-01.md | 13400 | 6 |
| PX.Objects.AP.APPayment | EntityType | Payment | DocType, RefNbr | 66 | 17 | PX.Objects.AP.APRegister | PX_Objects_AP_APPayment, Payment, APPayment | members-01.md | 13407 | 91 |
| PX.Objects.AP.APPaymentChargeTran | EntityType | AP Financial Charge Transaction | DocType, LineNbr, RefNbr | 25 | 9 |  | PX_Objects_AP_APPaymentChargeTran, APFinancialChargeTransaction, APPaymentChargeTran | members-01.md | 13499 | 40 |
| PX.Objects.AP.APPayNotSelReport | EntityType | Bill For Approval | DocType, RefNbr | 32 | 31 |  | PX_Objects_AP_APPayNotSelReport, BillForApproval, APPayNotSelReport | members-01.md | 13540 | 70 |
| PX.Objects.AP.APPaySelReport | EntityType | Bill For Payment | DocType, RefNbr | 35 | 31 |  | PX_Objects_AP_APPaySelReport, BillForPayment, APPaySelReport | members-01.md | 13611 | 73 |
| PX.Objects.AP.APPriceWorksheet | EntityType | AP Price Worksheet | RefNbr | 18 | 3 |  | PX_Objects_AP_APPriceWorksheet, APPriceWorksheet | members-01.md | 13685 | 28 |
| PX.Objects.AP.APPriceWorksheetDetail | EntityType | AP Price Worksheet Detail | LineID, RefNbr | 23 | 11 |  | PX_Objects_AP_APPriceWorksheetDetail, APPriceWorksheetDetail | members-01.md | 13714 | 41 |
| PX.Objects.AP.APPrintCheckDetail | EntityType | Print Check Detail | AdjdDocType, AdjdRefNbr, AdjgDocType, AdjgRefNbr, Source | 30 | 3 |  | PX_Objects_AP_APPrintCheckDetail, PrintCheckDetail, APPrintCheckDetail | members-01.md | 13756 | 40 |
| PX.Objects.AP.APPrintCheckDetailWithAdjdDoc | EntityType | Print Check Detail with Paid Document | AdjgDocType, AdjgRefNbr, Source | 16 | 1 |  | PX_Objects_AP_APPrintCheckDetailWithAdjdDoc, PrintCheckDetailwithPaidDocument, APPrintCheckDetailWithAdjdDoc | members-01.md | 13797 | 24 |
| PX.Objects.AP.APRegister | EntityType | Document | DocType, RefNbr | 110 | 45 |  | PX_Objects_AP_APRegister, Document, APRegister | members-01.md | 13822 | 162 |
| PX.Objects.AP.APRegisterAccess | EntityType | Vendor | AcctCD | 4 | 11 | PX.Objects.AP.Vendor | PX_Objects_AP_APRegisterAccess | members-01.md | 13985 | 22 |
| PX.Objects.AP.APRegisterReport | EntityType | Document | DocType, RefNbr | 3 | 0 | PX.Objects.AP.APRegister | PX_Objects_AP_APRegisterReport, Document1, APRegisterReport | members-01.md | 14008 | 10 |
| PX.Objects.AP.APRegisterRetainage | EntityType | APRegister Retainage | OrigDocType, OrigRefNbr | 6 | 0 |  | PX_Objects_AP_APRegisterRetainage, APRegisterRetainage | members-01.md | 14019 | 13 |
| PX.Objects.AP.APRetainageInvoice | EntityType | Document | DocType, RefNbr | 0 | 0 | PX.Objects.AP.APRegister | PX_Objects_AP_APRetainageInvoice | members-01.md | 14033 | 6 |
| PX.Objects.AP.APSetup | EntityType | Accounts Payable Preferences |  | 50 | 10 |  |  | members-01.md | 14040 | 65 |
| PX.Objects.AP.APSetupApproval | EntityType | AP Approval Preferences | ApprovalID | 12 | 4 |  | PX_Objects_AP_APSetupApproval, APApprovalPreferences, APSetupApproval | members-01.md | 14106 | 22 |
| PX.Objects.AP.APTax | EntityType | AP Tax Detail | LineNbr, RefNbr, TaxID, TranType | 28 | 7 |  | PX_Objects_AP_APTax, APTaxDetail, APTax | members-01.md | 14129 | 42 |
| PX.Objects.AP.APTaxTran | EntityType | AP Tax Details | Module, RecordID | 9 | 0 | PX.Objects.TX.TaxTran | PX_Objects_AP_APTaxTran, APTaxDetails, APTaxTran | members-01.md | 14172 | 17 |
| PX.Objects.AP.APTran | EntityType | AP Transactions | LineNbr, RefNbr, TranType | 118 | 47 |  | PX_Objects_AP_APTran, APTransactions, APTran | members-01.md | 14190 | 172 |
| PX.Objects.AP.APTranPost | EntityType | AP Document transaction | DocType, ID, RefNbr | 32 | 11 |  | PX_Objects_AP_APTranPost, APDocumenttransaction, APTranPost | members-01.md | 14363 | 50 |
| PX.Objects.AP.APTranPostGL | EntityType | AP Document Post GL | DocType, ID, RefNbr | 42 | 10 |  | PX_Objects_AP_APTranPostGL, APDocumentPostGL, APTranPostGL | members-01.md | 14414 | 58 |
| PX.Objects.AP.APTranPostGLwithLines | EntityType | AP Document Post GL with Lines | DocType, Ord, RefNbr | 48 | 2 |  | PX_Objects_AP_APTranPostGLwithLines, APDocumentPostGLwithLines, APTranPostGLwithLines | members-01.md | 14473 | 57 |
| PX.Objects.AP.APTranRetainage | EntityType | AP Tran Retainage | OrigDocType, OrigLineNbr, OrigRefNbr | 5 | 0 |  | PX_Objects_AP_APTranRetainage, APTranRetainage | members-01.md | 14531 | 11 |
| PX.Objects.AP.APVendorPrice | EntityType | AP Vendor Price | RecordID | 18 | 8 |  | PX_Objects_AP_APVendorPrice, APVendorPrice | members-01.md | 14543 | 32 |
| PX.Objects.AP.BalancedAPDocument | EntityType | Document | DocType, RefNbr | 4 | 0 | PX.Objects.AP.APRegister | PX_Objects_AP_BalancedAPDocument | members-01.md | 14576 | 12 |
| PX.Objects.AP.BaseAPHistoryByPeriod | EntityType | Base AP History by Period | AccountID, BranchID, FinPeriodID, SubID, VendorID | 6 | 1 |  | PX_Objects_AP_BaseAPHistoryByPeriod, BaseAPHistorybyPeriod | members-01.md | 14589 | 13 |
| PX.Objects.AP.CalcAPTranGLwithLinesReport | EntityType | Aggrigate AP Document Post GL with Lines | AgingDate, DocType, OrigDocType, OrigRefNbr, ProjectID, RefNbr | 10 | 1 |  | PX_Objects_AP_CalcAPTranGLwithLinesReport, AggrigateAPDocumentPostGLwithLines, CalcAPTranGLwithLinesReport | members-01.md | 14603 | 17 |
| PX.Objects.AP.CuryAPHistory | EntityType | Currency AP History | AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID | 97 | 6 |  | PX_Objects_AP_CuryAPHistory, CurrencyAPHistory, CuryAPHistory | members-02.md | 3 | 110 |
| PX.Objects.AP.CuryAPHistoryTran | ComplexType |  |  | 35 | 0 |  |  | members-02.md | 114 | 38 |
| PX.Objects.AP.DAC.VendorPaymentMethod | EntityType | Update Vendor Payment Methods | AcctCD | 5 | 9 | PX.Objects.AP.Vendor | PX_Objects_AP_DAC_VendorPaymentMethod, UpdateVendorPaymentMethods, VendorPaymentMethod | members-02.md | 153 | 21 |
| PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice | EntityType | Recognized document | DocType, RefNbr | 33 | 0 | PX.Objects.AP.APInvoice | PX_Objects_AP_InvoiceRecognition_DAC_APRecognizedInvoice, Recognizeddocument, APRecognizedInvoice | members-02.md | 175 | 41 |
| PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain | EntityType | Excluded Email Domains | Name | 8 | 2 |  | PX_Objects_AP_InvoiceRecognition_DAC_ExcludedVendorDomain, ExcludedEmailDomains, ExcludedVendorDomain | members-02.md | 217 | 16 |
| PX.Objects.AP.InvoiceRecognition.DAC.RecognizedRecordSplit | EntityType | Recognized Document Split | RefNbr | 3 | 1 |  | PX_Objects_AP_InvoiceRecognition_DAC_RecognizedRecordSplit, RecognizedDocumentSplit, RecognizedRecordSplit | members-02.md | 234 | 11 |
| PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping | EntityType | Vendor Specified in Recognized Documents | Id | 11 | 3 |  | PX_Objects_AP_InvoiceRecognition_DAC_RecognizedVendorMapping, VendorSpecifiedinRecognizedDocuments, RecognizedVendorMapping | members-02.md | 246 | 20 |
| PX.Objects.AP.LocationAPAccountSub | EntityType | Location GL Accounts | BAccountID, LocationID | 9 | 7 |  | PX_Objects_AP_LocationAPAccountSub, LocationGLAccounts, LocationAPAccountSub | members-02.md | 267 | 22 |
| PX.Objects.AP.LocationAPPaymentInfo | EntityType | Location Payment Settings | BAccountID, LocationID | 16 | 6 |  | PX_Objects_AP_LocationAPPaymentInfo, LocationPaymentSettings, LocationAPPaymentInfo | members-02.md | 290 | 29 |
| PX.Objects.AP.MISC1099EFileProcessingInfoRaw | EntityType | AP 1099 History | BoxNbr, BranchID, FinYear, VendorID | 9 | 5 | PX.Objects.AP.AP1099History | PX_Objects_AP_MISC1099EFileProcessingInfoRaw | members-02.md | 320 | 22 |
| PX.Objects.AP.Overrides.APDocumentRelease.AP1099Hist | EntityType | AP 1099 History | BoxNbr, BranchID, FinYear, VendorID | 0 | 1 | PX.Objects.AP.AP1099History | PX_Objects_AP_Overrides_APDocumentRelease_AP1099Hist | members-02.md | 343 | 8 |
| PX.Objects.AP.Overrides.APDocumentRelease.AP1099Yr | EntityType | AP 1099 Year | FinYear, OrganizationID | 0 | 0 | PX.Objects.AP.AP1099Year | PX_Objects_AP_Overrides_APDocumentRelease_AP1099Yr | members-02.md | 352 | 6 |
| PX.Objects.AP.Overrides.APDocumentRelease.APHistory2 | EntityType | AP History | AccountID, BranchID, FinPeriodID, SubID, VendorID | 0 | 0 | PX.Objects.AP.APHistory | PX_Objects_AP_Overrides_APDocumentRelease_APHistory2 | members-02.md | 359 | 6 |
| PX.Objects.AP.Overrides.APDocumentRelease.CuryAPHistory2 | EntityType | Currency AP History | AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID | 0 | 0 | PX.Objects.AP.CuryAPHistory | PX_Objects_AP_Overrides_APDocumentRelease_CuryAPHistory2 | members-02.md | 366 | 6 |
| PX.Objects.AP.Overrides.ScheduleMaint.DocumentSelection | EntityType | Document | DocType, RefNbr | 0 | 0 | PX.Objects.AP.APRegister | PX_Objects_AP_Overrides_ScheduleMaint_DocumentSelection | members-02.md | 373 | 6 |
| PX.Objects.AP.PendingPPDVATAdjApp | EntityType | Applications Pending VAT Adjustment for Prompt Payment Discount | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 19 | 0 | PX.Objects.AP.APAdjust | PX_Objects_AP_PendingPPDVATAdjApp, ApplicationsPendingVATAdjustmentforPromptPaymentDiscount, PendingPPDVATAdjApp | members-02.md | 380 | 27 |
| PX.Objects.AP.Standalone.APQuickCheck | EntityType | Cash Purchase | DocType, RefNbr | 55 | 8 | PX.Objects.AP.APRegister | PX_Objects_AP_Standalone_APQuickCheck, CashPurchase, APQuickCheck | members-02.md | 408 | 71 |
| PX.Objects.AP.Vendor | EntityType | Vendor | AcctCD | 30 | 118 | PX.Objects.CR.BAccount | PX_Objects_AP_Vendor, Vendor | members-02.md | 480 | 156 |
| PX.Objects.AP.VendorClass | EntityType | Vendor Class | VendorClassID | 30 | 40 |  | PX_Objects_AP_VendorClass, VendorClass | members-02.md | 637 | 77 |
| PX.Objects.AP.VendorDiscountSequence | EntityType | Discount Sequence | DiscountID, DiscountSequenceID | 1 | 9 | PX.Objects.AR.DiscountSequence | PX_Objects_AP_VendorDiscountSequence | members-02.md | 715 | 17 |
| PX.Objects.AP.VendorPaymentMethodDetail | EntityType | Payment Type Detail | BAccountID, DetailID, LocationID, PaymentMethodID | 12 | 7 |  | PX_Objects_AP_VendorPaymentMethodDetail, PaymentTypeDetail, VendorPaymentMethodDetail | members-02.md | 733 | 25 |
| PX.Objects.AP.VendorR | EntityType | Vendor | AcctCD | 0 | 0 | PX.Objects.AP.Vendor | PX_Objects_AP_VendorR, Vendor1, VendorR | members-02.md | 759 | 6 |
| PX.Objects.AR.ARAddItemSelected | EntityType |  | InventoryID | 17 | 6 |  | PX_Objects_AR_ARAddItemSelected | members-02.md | 766 | 29 |
| PX.Objects.AR.ARAddress | EntityType | AR Address | AddressID | 37 | 8 |  | PX_Objects_AR_ARAddress, ARAddress | members-02.md | 796 | 52 |
| PX.Objects.AR.ARAdjust | EntityType | Applications | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 106 | 28 |  | PX_Objects_AR_ARAdjust, Applications, ARAdjust | members-02.md | 849 | 141 |
| PX.Objects.AR.ARAdjust2 | EntityType | Applications | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 1 | 0 | PX.Objects.AR.ARAdjust | PX_Objects_AR_ARAdjust2, Applications1, ARAdjust2 | members-02.md | 991 | 8 |
| PX.Objects.AR.ARAdjustedBalanceAtDate | EntityType | ARAdjustedBalanceAtDate | DocType, RefNbr, SubmissionDate | 5 | 20 |  | PX_Objects_AR_ARAdjustedBalanceAtDate, ARAdjustedBalanceAtDate | members-02.md | 1000 | 32 |
| PX.Objects.AR.ARAdjustingBalanceAtDate | EntityType | ARAdjustingBalanceAtDate | DocType, RefNbr, SubmissionDate | 5 | 20 |  | PX_Objects_AR_ARAdjustingBalanceAtDate, ARAdjustingBalanceAtDate | members-02.md | 1033 | 32 |
| PX.Objects.AR.ARAdjustReport | EntityType | Applications | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 4 | 0 | PX.Objects.AR.ARAdjust | PX_Objects_AR_ARAdjustReport, Applications2, ARAdjustReport | members-02.md | 1066 | 11 |
| PX.Objects.AR.ARBalances | EntityType | AR Balance | BranchID, CustomerID, CustomerLocationID | 26 | 5 |  | PX_Objects_AR_ARBalances, ARBalance, ARBalances | members-02.md | 1078 | 38 |
| PX.Objects.AR.ARBalancesByBaseCuryID | EntityType | AR Balance by Base Currency | BaseCuryID, CustomerID | 6 | 3 |  | PX_Objects_AR_ARBalancesByBaseCuryID, ARBalancebyBaseCurrency, ARBalancesByBaseCuryID | members-02.md | 1117 | 15 |
| PX.Objects.AR.ARBalancesSharedCredit | EntityType | AR Balance Shared Credit | SharedCreditCustomerID | 9 | 1 |  | PX_Objects_AR_ARBalancesSharedCredit, ARBalanceSharedCredit, ARBalancesSharedCredit | members-02.md | 1133 | 16 |
| PX.Objects.AR.ARContact | EntityType | AR Contact | ContactID | 28 | 7 |  | PX_Objects_AR_ARContact, ARContact | members-02.md | 1150 | 42 |
| PX.Objects.AR.ARDiscount | EntityType | AR Discount | DiscountID | 17 | 18 |  | PX_Objects_AR_ARDiscount, ARDiscount | members-02.md | 1193 | 41 |
| PX.Objects.AR.ARDunningCustomerClass | EntityType | AR Dunning Setup | CustomerClassID, DunningLetterLevel | 15 | 2 |  | PX_Objects_AR_ARDunningCustomerClass, ARDunningSetup, ARDunningCustomerClass | members-02.md | 1235 | 24 |
| PX.Objects.AR.ARDunningLetter | EntityType | Dunning Letter | DunningLetterID | 22 | 4 |  | PX_Objects_AR_ARDunningLetter, DunningLetter, ARDunningLetter | members-02.md | 1260 | 33 |
| PX.Objects.AR.ARDunningLetterDetail | EntityType | Dunning Letter Detail | DocType, DunningLetterID, RefNbr | 19 | 4 |  | PX_Objects_AR_ARDunningLetterDetail, DunningLetterDetail, ARDunningLetterDetail | members-02.md | 1294 | 30 |
| PX.Objects.AR.ARDunningLetterDetailReport | EntityType | Dunning Letter Detail | DocType, DunningLetterID, RefNbr | 1 | 0 | PX.Objects.AR.ARDunningLetterDetail | PX_Objects_AR_ARDunningLetterDetailReport, DunningLetterDetail1, ARDunningLetterDetailReport | members-02.md | 1325 | 8 |
| PX.Objects.AR.ARDunningSetup | EntityType | AR Dunning Setup | DunningLetterLevel | 14 | 2 |  | PX_Objects_AR_ARDunningSetup, ARDunningSetup1 | members-02.md | 1334 | 23 |
| PX.Objects.AR.ARFinCharge | EntityType | AR Financial Charge | FinChargeID | 24 | 11 |  | PX_Objects_AR_ARFinCharge, ARFinancialCharge, ARFinCharge | members-02.md | 1358 | 42 |
| PX.Objects.AR.ARFinChargePercent | EntityType | AR Financial Charge Percent | PercentID | 4 | 1 |  | PX_Objects_AR_ARFinChargePercent, ARFinancialChargePercent, ARFinChargePercent | members-02.md | 1401 | 11 |
| PX.Objects.AR.ARFinChargeTran | EntityType | AR Financial Charge Transaction | LineNbr, RefNbr, TranType | 8 | 1 |  | PX_Objects_AR_ARFinChargeTran, ARFinancialChargeTransaction, ARFinChargeTran | members-02.md | 1413 | 15 |
| PX.Objects.AR.ARHistory | EntityType | AR History | AccountID, BranchID, CustomerID, FinPeriodID, SubID | 62 | 5 |  | PX_Objects_AR_ARHistory, ARHistory | members-02.md | 1429 | 74 |
| PX.Objects.AR.ARHistoryByPeriod | EntityType | AR History by Period | AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID | 7 | 1 |  | PX_Objects_AR_ARHistoryByPeriod, ARHistorybyPeriod | members-02.md | 1504 | 14 |
| PX.Objects.AR.ARHistorySumCreditSales | ComplexType |  |  | 3 | 0 |  |  | members-02.md | 1519 | 6 |
| PX.Objects.AR.ARHistorySumForPeriod | EntityType | AR History Sum For Period | FinPeriodID | 5 | 0 |  | PX_Objects_AR_ARHistorySumForPeriod, ARHistorySumForPeriod | members-02.md | 1526 | 11 |
| PX.Objects.AR.ARHistoryTran | ComplexType |  |  | 27 | 0 |  |  | members-02.md | 1538 | 30 |
| PX.Objects.AR.ARInvoice | EntityType | AR Invoice/Memo | DocType, RefNbr | 113 | 37 | PX.Objects.AR.ARRegister | PX_Objects_AR_ARInvoice, ARInvoiceMemo, ARInvoice | members-02.md | 1569 | 158 |
| PX.Objects.AR.ARInvoiceDiscountDetail | EntityType | AR Invoice Discount Detail | DocType, RecordID, RefNbr | 31 | 9 |  | PX_Objects_AR_ARInvoiceDiscountDetail, ARInvoiceDiscountDetail | members-02.md | 1728 | 47 |
| PX.Objects.AR.ARInvoiceExt | EntityType | AR Invoice/Memo | DocType, RefNbr | 15 | 5 | PX.Objects.AR.ARInvoice | PX_Objects_AR_ARInvoiceExt | members-02.md | 1776 | 28 |
| PX.Objects.AR.ARInvoiceRetainageBalanceAtDate | EntityType | ARInvoiceRetainageBalanceAtDate | DocType, RefNbr, SubmissionDate | 4 | 20 |  | PX_Objects_AR_ARInvoiceRetainageBalanceAtDate, ARInvoiceRetainageBalanceAtDate | members-02.md | 1805 | 30 |
| PX.Objects.AR.ARNotification | EntityType | AR Notification | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_AR_ARNotification, ARNotification | members-02.md | 1836 | 6 |
| PX.Objects.AR.ARPayment | EntityType | AR Payment | DocType, RefNbr | 58 | 17 | PX.Objects.AR.ARRegister | PX_Objects_AR_ARPayment, ARPayment | members-02.md | 1843 | 83 |
| PX.Objects.AR.ARPaymentChargeTran | EntityType | AR Payment Charge Transaction | DocType, LineNbr, RefNbr | 26 | 13 |  | PX_Objects_AR_ARPaymentChargeTran, ARPaymentChargeTransaction, ARPaymentChargeTran | members-02.md | 1927 | 45 |
| PX.Objects.AR.ARPaymentInfo | EntityType | AR Payment | DocType, RefNbr | 3 | 0 | PX.Objects.AR.ARPayment | PX_Objects_AR_ARPaymentInfo | members-02.md | 1973 | 11 |
| PX.Objects.AR.ARPaymentTotals | EntityType | AR Payment Totals | DocType, RefNbr | 15 | 10 |  | PX_Objects_AR_ARPaymentTotals, ARPaymentTotals | members-02.md | 1985 | 31 |
| PX.Objects.AR.ARPriceClass | EntityType | AR Price Class | PriceClassID | 11 | 8 |  | PX_Objects_AR_ARPriceClass, ARPriceClass | members-02.md | 2017 | 26 |
| PX.Objects.AR.ARPriceWorksheet | EntityType | AR Price Worksheet | RefNbr | 23 | 3 |  | PX_Objects_AR_ARPriceWorksheet, ARPriceWorksheet | members-02.md | 2044 | 33 |
| PX.Objects.AR.ARPriceWorksheetDetail | EntityType | AR Price Worksheet Detail | LineID, RefNbr | 27 | 12 |  | PX_Objects_AR_ARPriceWorksheetDetail, ARPriceWorksheetDetail | members-02.md | 2078 | 46 |
| PX.Objects.AR.ARRegister | EntityType | AR Document | DocType, RefNbr | 111 | 42 |  | PX_Objects_AR_ARRegister, ARDocument, ARRegister | members-02.md | 2125 | 160 |
| PX.Objects.AR.ARRegisterAccess | EntityType | Customer | AcctCD | 4 | 10 | PX.Objects.AR.Customer | PX_Objects_AR_ARRegisterAccess | members-02.md | 2286 | 21 |
| PX.Objects.AR.ARRegisterCashSales | EntityType | ARRegister Cash Sales | DocType, RefNbr | 0 | 0 | PX.Objects.AR.ARRegisterSigned | PX_Objects_AR_ARRegisterCashSales, ARRegisterCashSales | members-02.md | 2308 | 6 |
| PX.Objects.AR.ARRegisterReport | EntityType | AR Document | DocType, RefNbr | 3 | 0 | PX.Objects.AR.ARRegister | PX_Objects_AR_ARRegisterReport, ARDocument1, ARRegisterReport | members-02.md | 2315 | 10 |
| PX.Objects.AR.ARRegisterSigned | EntityType | AR Document | DocType, RefNbr | 2 | 0 | PX.Objects.AR.ARRegister | PX_Objects_AR_ARRegisterSigned, ARDocument2, ARRegisterSigned | members-02.md | 2326 | 9 |
| PX.Objects.AR.ARRetainageInvoice | EntityType | AR Document | DocType, RefNbr | 0 | 0 | PX.Objects.AR.ARRegister | PX_Objects_AR_ARRetainageInvoice | members-02.md | 2336 | 6 |
| PX.Objects.AR.ARRetainageWithApplications | EntityType | AR Retainage documents with released/paid amount | DocType, RefNbr | 14 | 2 | PX.Objects.AR.ARRetainageInvoice | PX_Objects_AR_ARRetainageWithApplications, ARRetainagedocumentswithreleasedpaidamount, ARRetainageWithApplications | members-02.md | 2343 | 24 |
| PX.Objects.AR.ARSalesPerTran | EntityType | AR Salesperson Commission | AdjdDocType, AdjdRefNbr, AdjNbr, DocType, RefNbr, SalespersonID | 25 | 7 |  | PX_Objects_AR_ARSalesPerTran, ARSalespersonCommission, ARSalesPerTran | members-02.md | 2368 | 38 |
| PX.Objects.AR.ARSalesPrice | EntityType | AR Sales Price | RecordID | 38 | 10 |  | PX_Objects_AR_ARSalesPrice, ARSalesPrice | members-02.md | 2407 | 55 |
| PX.Objects.AR.ARSetup | EntityType | Account Receivable Preferences |  | 67 | 21 |  |  | members-02.md | 2463 | 93 |
| PX.Objects.AR.ARSetupApproval | EntityType |  | ApprovalID | 12 | 4 |  | PX_Objects_AR_ARSetupApproval | members-02.md | 2557 | 21 |
| PX.Objects.AR.ARShippingAddress | EntityType | AR Address | AddressID | 0 | 0 | PX.Objects.AR.ARAddress | PX_Objects_AR_ARShippingAddress, ARAddress1, ARShippingAddress | members-02.md | 2579 | 6 |
| PX.Objects.AR.ARShippingContact | EntityType | AR Contact | ContactID | 0 | 0 | PX.Objects.AR.ARContact | PX_Objects_AR_ARShippingContact, ARContact1, ARShippingContact | members-02.md | 2586 | 6 |
| PX.Objects.AR.ARSPCommissionPeriod | EntityType | AR Salesperson Commission Period | CommnPeriodID | 9 | 0 |  | PX_Objects_AR_ARSPCommissionPeriod, ARSalespersonCommissionPeriod, ARSPCommissionPeriod | members-02.md | 2593 | 16 |
| PX.Objects.AR.ARSPCommissionYear | EntityType | AR Salesperson Commission Year | Year | 3 | 0 |  | PX_Objects_AR_ARSPCommissionYear, ARSalespersonCommissionYear, ARSPCommissionYear | members-02.md | 2610 | 9 |
| PX.Objects.AR.ARSPCommnHistory | EntityType | AR Salesperson Commission History | BranchID, CommnPeriod, CustomerID, CustomerLocationID, SalesPersonID | 11 | 4 |  | PX_Objects_AR_ARSPCommnHistory, ARSalespersonCommissionHistory, ARSPCommnHistory | members-02.md | 2620 | 22 |
| PX.Objects.AR.ARStatement | EntityType | AR Statement | BranchID, CuryID, CustomerID, StatementDate | 51 | 10 |  | PX_Objects_AR_ARStatement, ARStatement | members-02.md | 2643 | 68 |
| PX.Objects.AR.ARStatementCycle | EntityType | Statement Cycle | StatementCycleId | 38 | 7 |  | PX_Objects_AR_ARStatementCycle, StatementCycle, ARStatementCycle | members-02.md | 2712 | 52 |
| PX.Objects.AR.ARStatementDetail | EntityType | AR Statement Detail | CuryID, CustomerID, DocType, RefNbr, RefNoteID, StatementDate | 23 | 5 |  | PX_Objects_AR_ARStatementDetail, ARStatementDetail | members-02.md | 2765 | 34 |
| PX.Objects.AR.ARStatementDetailInfo | EntityType | AR Statement Detail Info | AdjdDocType, AdjgDocType, AdjgRefNbr, DocType, RefNbr, RefNoteID, SourceDocType, SourceRefNbr, StatementDate | 73 | 9 |  | PX_Objects_AR_ARStatementDetailInfo, ARStatementDetailInfo | members-02.md | 2800 | 89 |
| PX.Objects.AR.ARTax | EntityType | AR Tax Detail | LineNbr, RefNbr, TaxID, TranType | 28 | 9 |  | PX_Objects_AR_ARTax, ARTaxDetail, ARTax | members-02.md | 2890 | 44 |
| PX.Objects.AR.ARTaxTran | EntityType | AR Tax | Module, RecordID | 9 | 0 | PX.Objects.TX.TaxTran | PX_Objects_AR_ARTaxTran, ARTax1, ARTaxTran | members-02.md | 2935 | 17 |
| PX.Objects.AR.ARTran | EntityType | AR Transactions | LineNbr, RefNbr, TranType | 145 | 54 |  | PX_Objects_AR_ARTran, ARTransactions, ARTran | members-02.md | 2953 | 206 |
| PX.Objects.AR.ARTranAccrueCost | EntityType |  | LineNbr, RefNbr, TranType | 13 | 16 |  | PX_Objects_AR_ARTranAccrueCost | members-02.md | 3160 | 35 |
| PX.Objects.AR.ARTranPost | EntityType | AR Document transaction | DocType, ID, RefNbr | 38 | 12 |  | PX_Objects_AR_ARTranPost, ARDocumenttransaction, ARTranPost | members-02.md | 3196 | 57 |
| PX.Objects.AR.ARTranPostGL | EntityType | AR Document Post GL | DocType, ID, RefNbr | 49 | 12 |  | PX_Objects_AR_ARTranPostGL, ARDocumentPostGL, ARTranPostGL | members-02.md | 3254 | 67 |
| PX.Objects.AR.BalancedARDocument | EntityType | AR Document | DocType, RefNbr | 4 | 0 | PX.Objects.AR.ARRegister | PX_Objects_AR_BalancedARDocument | members-02.md | 3322 | 12 |
| PX.Objects.AR.BaseARHistoryByPeriod | EntityType | Base AR History by Period | AccountID, BranchID, CustomerID, FinPeriodID, SubID | 6 | 0 |  | PX_Objects_AR_BaseARHistoryByPeriod, BaseARHistorybyPeriod | members-02.md | 3335 | 12 |
| PX.Objects.AR.CCProcTran | EntityType | Credit Card Processing Transaction | TranNbr | 40 | 8 |  | PX_Objects_AR_CCProcTran, CreditCardProcessingTransaction, CCProcTran | members-02.md | 3348 | 55 |
| PX.Objects.AR.CuryARHistory | EntityType | Currency AR History | AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID | 101 | 6 |  | PX_Objects_AR_CuryARHistory, CurrencyARHistory, CuryARHistory | members-02.md | 3404 | 114 |
| PX.Objects.AR.CuryARHistoryTran | ComplexType |  |  | 38 | 0 |  |  | members-02.md | 3519 | 41 |
| PX.Objects.AR.Customer | EntityType | Customer | AcctCD | 42 | 43 | PX.Objects.CR.BAccount | PX_Objects_AR_Customer, Customer | members-02.md | 3561 | 93 |
| PX.Objects.AR.CustomerClass | EntityType | Customer Class | CustomerClassID | 51 | 46 |  | PX_Objects_AR_CustomerClass, CustomerClass | members-02.md | 3655 | 104 |
| PX.Objects.AR.CustomerMaster | EntityType | Customer (alias) | BAccountID | 9 | 7 |  | PX_Objects_AR_CustomerMaster, Customeralias, CustomerMaster | members-02.md | 3760 | 22 |
| PX.Objects.AR.CustomerPaymentMethod | EntityType | Customer Payment Method | BAccountID, PMInstanceID | 31 | 20 |  | PX_Objects_AR_CustomerPaymentMethod, CustomerPaymentMethod | members-02.md | 3783 | 58 |
| PX.Objects.AR.CustomerPaymentMethodDetail | EntityType | Customer Payment Method Detail | DetailID, PaymentMethodID, PMInstanceID | 12 | 5 |  | PX_Objects_AR_CustomerPaymentMethodDetail, CustomerPaymentMethodDetail | members-02.md | 3842 | 23 |
| PX.Objects.AR.CustomerPaymentMethodInfo | EntityType | Customer Payment Method | PMInstanceID | 15 | 5 |  | PX_Objects_AR_CustomerPaymentMethodInfo, CustomerPaymentMethod1, CustomerPaymentMethodInfo | members-02.md | 3866 | 26 |
| PX.Objects.AR.CustomerSharedCredit | EntityType | Customer Shared Credit | BAccountID | 7 | 75 |  | PX_Objects_AR_CustomerSharedCredit, CustomerSharedCredit | members-02.md | 3893 | 88 |
| PX.Objects.AR.CustSalesPeople | EntityType | Customer Salespersons | BAccountID, LocationID, SalesPersonID | 12 | 7 |  | PX_Objects_AR_CustSalesPeople, CustomerSalespersons, CustSalesPeople | members-02.md | 3982 | 25 |
| PX.Objects.AR.DiscountBranch | EntityType | Discount for Branch | BranchID, DiscountID, DiscountSequenceID | 10 | 5 |  | PX_Objects_AR_DiscountBranch, DiscountforBranch, DiscountBranch | members-02.md | 4008 | 21 |
| PX.Objects.AR.DiscountCustomer | EntityType | Discount for Customer | CustomerID, DiscountID, DiscountSequenceID | 10 | 6 |  | PX_Objects_AR_DiscountCustomer, DiscountforCustomer, DiscountCustomer | members-02.md | 4030 | 22 |
| PX.Objects.AR.DiscountCustomerPriceClass | EntityType | Discount for Customer and Price Class | CustomerPriceClassID, DiscountID, DiscountSequenceID | 10 | 5 |  | PX_Objects_AR_DiscountCustomerPriceClass, DiscountforCustomerandPriceClass, DiscountCustomerPriceClass | members-02.md | 4053 | 21 |
| PX.Objects.AR.DiscountDetail | EntityType | Discount Breakpoint | DiscountDetailsID | 33 | 1 |  | PX_Objects_AR_DiscountDetail, DiscountBreakpoint, DiscountDetail | members-02.md | 4075 | 41 |
| PX.Objects.AR.DiscountInventoryPriceClass | EntityType | Discount for Inventory and Price Class | DiscountID, DiscountSequenceID, InventoryPriceClassID | 10 | 5 |  | PX_Objects_AR_DiscountInventoryPriceClass, DiscountforInventoryandPriceClass, DiscountInventoryPriceClass | members-02.md | 4117 | 21 |
| PX.Objects.AR.DiscountItem | EntityType | Discount Item | DiscountID, DiscountSequenceID, InventoryID | 13 | 6 |  | PX_Objects_AR_DiscountItem, DiscountItem | members-02.md | 4139 | 25 |
| PX.Objects.AR.DiscountSequence | EntityType | Discount Sequence | DiscountID, DiscountSequenceID | 25 | 23 |  | PX_Objects_AR_DiscountSequence, DiscountSequence | members-02.md | 4165 | 55 |
| PX.Objects.AR.DiscountSequenceDetail | EntityType | Discount Sequence Detail | DiscountDetailsID, IsLast | 27 | 3 |  | PX_Objects_AR_DiscountSequenceDetail, DiscountSequenceDetail | members-02.md | 4221 | 37 |
| PX.Objects.AR.DiscountSequenceDetail2 | EntityType | Discount Sequence Detail | DiscountDetailsID, IsLast | 0 | 0 | PX.Objects.AR.DiscountSequenceDetail | PX_Objects_AR_DiscountSequenceDetail2 | members-02.md | 4259 | 6 |
| PX.Objects.AR.DiscountSite | EntityType | Discount for Warehouse | DiscountID, DiscountSequenceID, SiteID | 10 | 5 |  | PX_Objects_AR_DiscountSite, DiscountforWarehouse, DiscountSite | members-02.md | 4266 | 21 |
| PX.Objects.AR.ExternalTransaction | EntityType | External Transaction | TransactionID | 40 | 12 |  | PX_Objects_AR_ExternalTransaction, ExternalTransaction | members-02.md | 4288 | 59 |
| PX.Objects.AR.FSCTNotification | EntityType | Default Notification setup | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_AR_FSCTNotification | members-02.md | 4348 | 6 |
| PX.Objects.AR.FSNotification | EntityType | Default Notification setup | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_AR_FSNotification | members-02.md | 4355 | 6 |
| PX.Objects.AR.Light.Customer | EntityType | Light version of Customer DAC for Statements Printing | AcctCD | 18 | 43 |  | PX_Objects_AR_Light_Customer, LightversionofCustomerDACforStatementsPrinting, Customer1 | members-02.md | 4362 | 68 |
| PX.Objects.AR.Override.BAccount | EntityType |  | BAccountID | 7 | 219 |  | PX_Objects_AR_Override_BAccount | members-02.md | 4431 | 232 |
| PX.Objects.AR.Override.Customer | EntityType |  | BAccountID | 7 | 96 |  | PX_Objects_AR_Override_Customer | members-02.md | 4664 | 109 |
| PX.Objects.AR.Overrides.ARDocumentRelease.ARHistory2 | EntityType | AR History | AccountID, BranchID, CustomerID, FinPeriodID, SubID | 0 | 0 | PX.Objects.AR.ARHistory | PX_Objects_AR_Overrides_ARDocumentRelease_ARHistory2 | members-02.md | 4774 | 6 |
| PX.Objects.AR.Overrides.ARDocumentRelease.CuryARHistory2 | EntityType | Currency AR History | AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID | 0 | 0 | PX.Objects.AR.CuryARHistory | PX_Objects_AR_Overrides_ARDocumentRelease_CuryARHistory2 | members-02.md | 4781 | 6 |
| PX.Objects.AR.Overrides.ScheduleMaint.DocumentSelection | EntityType | AR Document to Process | DocType, RefNbr | 0 | 0 | PX.Objects.AR.ARRegister | PX_Objects_AR_Overrides_ScheduleMaint_DocumentSelection, ARDocumenttoProcess, DocumentSelection | members-02.md | 4788 | 6 |
| PX.Objects.AR.PendingPPDARTaxAdjApp | EntityType | Pending PPD AR Tax Adj App | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 16 | 2 | PX.Objects.AR.ARAdjust | PX_Objects_AR_PendingPPDARTaxAdjApp, PendingPPDARTaxAdjApp | members-02.md | 4795 | 26 |
| PX.Objects.AR.SalesPerson | EntityType | Sales Person | SalesPersonCD | 14 | 22 |  | PX_Objects_AR_SalesPerson, SalesPerson | members-02.md | 4822 | 43 |
| PX.Objects.AR.Standalone.ARCashSale | EntityType | Cash Sale | DocType, RefNbr | 78 | 12 | PX.Objects.AR.ARRegister | PX_Objects_AR_Standalone_ARCashSale, CashSale, ARCashSale | members-02.md | 4866 | 98 |
| PX.Objects.CA.ACHPlugInParameter | EntityType | ACHPlugInParameter | ParameterID, PaymentMethodID, PlugInTypeName | 18 | 1 |  | PX_Objects_CA_ACHPlugInParameter, ACHPlugInParameter | members-02.md | 4965 | 26 |
| PX.Objects.CA.ACHPlugInParameter2 | EntityType | ACHPlugInParameter | ParameterID, PaymentMethodID, PlugInTypeName | 0 | 0 | PX.Objects.CA.ACHPlugInParameter | PX_Objects_CA_ACHPlugInParameter2, ACHPlugInParameter1, ACHPlugInParameter2 | members-02.md | 4992 | 6 |
| PX.Objects.CA.BankStatementHelpers.CATranExt | EntityType | CA Transaction | TranID | 8 | 0 | PX.Objects.CA.CATran | PX_Objects_CA_BankStatementHelpers_CATranExt | members-02.md | 4999 | 16 |
| PX.Objects.CA.CAAdj | EntityType | Cash Transactions | AdjRefNbr, AdjTranType | 74 | 19 |  | PX_Objects_CA_CAAdj, CashTransactions, CAAdj | members-02.md | 5016 | 100 |
| PX.Objects.CA.CABankChargeTax | EntityType | CABankChargeTax | BankTranID, LineNbr, MatchType, TaxID | 22 | 5 |  | PX_Objects_CA_CABankChargeTax, CABankChargeTax | members-02.md | 5117 | 33 |
| PX.Objects.CA.CABankFeed | EntityType | Bank Feed | BankFeedID | 43 | 10 |  | PX_Objects_CA_CABankFeed, BankFeed, CABankFeed | members-02.md | 5151 | 60 |
| PX.Objects.CA.CABankFeedAccountMapping | EntityType | Bank Feed Account Mapping | BankFeedAccountMapID | 16 | 5 |  | PX_Objects_CA_CABankFeedAccountMapping, BankFeedAccountMapping, CABankFeedAccountMapping | members-02.md | 5212 | 27 |
| PX.Objects.CA.CABankFeedCorpCard | EntityType | Bank Feed Corporate Cards | BankFeedID, LineNbr | 21 | 7 |  | PX_Objects_CA_CABankFeedCorpCard, BankFeedCorporateCards, CABankFeedCorpCard | members-02.md | 5240 | 35 |
| PX.Objects.CA.CABankFeedDetail | EntityType | Bank Feed Detail | BankFeedID, LineNbr | 31 | 7 |  | PX_Objects_CA_CABankFeedDetail, BankFeedDetail, CABankFeedDetail | members-02.md | 5276 | 45 |
| PX.Objects.CA.CABankFeedExpense | EntityType | Bank Feed Expense Items | BankFeedID, LineNbr | 16 | 4 |  | PX_Objects_CA_CABankFeedExpense, BankFeedExpenseItems, CABankFeedExpense | members-02.md | 5322 | 27 |
| PX.Objects.CA.CABankFeedFieldMapping | EntityType | CABankFeedFieldMapping | BankFeedID, LineNbr | 14 | 3 |  | PX_Objects_CA_CABankFeedFieldMapping, CABankFeedFieldMapping | members-02.md | 5350 | 24 |
| PX.Objects.CA.CABankTax | EntityType | CA Bank Tax Detail | BankTranID, BankTranType, LineNbr, TaxID | 22 | 5 |  | PX_Objects_CA_CABankTax, CABankTaxDetail, CABankTax | members-02.md | 5375 | 33 |
| PX.Objects.CA.CABankTaxTran | EntityType | CA Bank Tax Transaction | BankTranID, BankTranType, Module, RecordID, TaxID | 51 | 9 |  | PX_Objects_CA_CABankTaxTran, CABankTaxTransaction, CABankTaxTran | members-02.md | 5409 | 66 |
| PX.Objects.CA.CABankTaxTranMatch | EntityType | CABankTaxTranMatch | BankTranID, BankTranType, Module, RecordID, TaxID | 51 | 9 |  | PX_Objects_CA_CABankTaxTranMatch, CABankTaxTranMatch | members-02.md | 5476 | 66 |
| PX.Objects.CA.CABankTran | EntityType | Bank Transaction | TranID | 119 | 25 |  | PX_Objects_CA_CABankTran, BankTransaction, CABankTran | members-02.md | 5543 | 151 |
| PX.Objects.CA.CABankTranAdjustment | EntityType | Bank Transaction Adjustment | AdjNbr, TranID | 57 | 16 |  | PX_Objects_CA_CABankTranAdjustment, BankTransactionAdjustment, CABankTranAdjustment | members-02.md | 5695 | 80 |
| PX.Objects.CA.CABankTranBAccountMapping | EntityType | Bank Transaction Payee Business Account Mapping | MappingID | 11 | 4 |  | PX_Objects_CA_CABankTranBAccountMapping, BankTransactionPayeeBusinessAccountMapping, CABankTranBAccountMapping | members-02.md | 5776 | 21 |
| PX.Objects.CA.CABankTranDetail | EntityType | CA Bank Transaction Detail | BankTranID, BankTranType, LineNbr | 26 | 17 |  | PX_Objects_CA_CABankTranDetail, CABankTransactionDetail, CABankTranDetail | members-02.md | 5798 | 50 |
| PX.Objects.CA.CABankTranHeader | EntityType | Bank Statement | CashAccountID, RefNbr, TranType | 25 | 5 |  | PX_Objects_CA_CABankTranHeader, BankStatement, CABankTranHeader | members-02.md | 5849 | 37 |
| PX.Objects.CA.CABankTranMatch | EntityType | Bank Transaction Match | LineNbr, MatchType, TranID | 17 | 6 |  | PX_Objects_CA_CABankTranMatch, BankTransactionMatch, CABankTranMatch | members-02.md | 5887 | 29 |
| PX.Objects.CA.CABankTranMatch2 | EntityType | Bank Transaction Match | LineNbr, MatchType, TranID | 0 | 0 | PX.Objects.CA.CABankTranMatch | PX_Objects_CA_CABankTranMatch2 | members-02.md | 5917 | 6 |
| PX.Objects.CA.CABankTranRule | EntityType | CA Bank Transactions Rule | RuleID | 27 | 7 |  | PX_Objects_CA_CABankTranRule, CABankTransactionsRule, CABankTranRule | members-02.md | 5924 | 41 |
| PX.Objects.CA.CABankTranRulePopup | EntityType | CA Bank Transactions Rule | RuleID | 0 | 0 | PX.Objects.CA.CABankTranRule | PX_Objects_CA_CABankTranRulePopup | members-02.md | 5966 | 6 |
| PX.Objects.CA.CABatch | EntityType | CA Batch | BatchNbr | 40 | 11 |  | PX_Objects_CA_CABatch, CABatch | members-02.md | 5973 | 58 |
| PX.Objects.CA.CABatchDetail | EntityType | CA Batch Details | BatchNbr, OrigDocType, OrigLineNbr, OrigModule, OrigRefNbr | 12 | 4 |  | PX_Objects_CA_CABatchDetail, CABatchDetails, CABatchDetail | members-02.md | 6032 | 22 |
| PX.Objects.CA.CABatchDetailOrigDocAggregate | EntityType | Aggregated CA Batch Details | BatchNbr, OrigDocType, OrigLineNbr, OrigModule, OrigRefNbr | 0 | 0 | PX.Objects.CA.CABatchDetail | PX_Objects_CA_CABatchDetailOrigDocAggregate, AggregatedCABatchDetails, CABatchDetailOrigDocAggregate | members-02.md | 6055 | 6 |
| PX.Objects.CA.CACorpCard | EntityType | Corporate Card | CorpCardCD | 14 | 8 |  | PX_Objects_CA_CACorpCard, CorporateCard, CACorpCard | members-02.md | 6062 | 29 |
| PX.Objects.CA.CADailySummary | EntityType | CA Daily Summary | CashAccountID, TranDate | 10 | 1 |  | PX_Objects_CA_CADailySummary, CADailySummary | members-02.md | 6092 | 17 |
| PX.Objects.CA.CADeposit | EntityType | CA Deposit | RefNbr, TranType | 49 | 19 |  | PX_Objects_CA_CADeposit, CADeposit | members-02.md | 6110 | 75 |
| PX.Objects.CA.CADepositCharge | EntityType | CA Deposit Charge | LineNbr, RefNbr, TranType | 19 | 9 |  | PX_Objects_CA_CADepositCharge, CADepositCharge | members-02.md | 6186 | 34 |
| PX.Objects.CA.CADepositDetail | EntityType | CA Deposit Detail | LineNbr, RefNbr, TranType | 36 | 12 |  | PX_Objects_CA_CADepositDetail, CADepositDetail | members-02.md | 6221 | 55 |
| PX.Objects.CA.CAEntryType | EntityType | CA Entry Type | EntryTypeId | 15 | 21 |  | PX_Objects_CA_CAEntryType, CAEntryType | members-02.md | 6277 | 43 |
| PX.Objects.CA.CAExpense | EntityType | CAExpense | LineNbr, RefNbr | 50 | 16 |  | PX_Objects_CA_CAExpense, CAExpense | members-02.md | 6321 | 73 |
| PX.Objects.CA.CAExpenseTax | EntityType | CAExpenseTax | LineNbr, RefNbr, TaxID, TranType | 22 | 5 |  | PX_Objects_CA_CAExpenseTax, CAExpenseTax | members-02.md | 6395 | 34 |
| PX.Objects.CA.CAExpenseTaxTran | EntityType | CAExpenseTaxTran | Module, RecordID | 0 | 0 | PX.Objects.TX.TaxTran | PX_Objects_CA_CAExpenseTaxTran, CAExpenseTaxTran | members-02.md | 6430 | 6 |
| PX.Objects.CA.CARecon | EntityType | Reconciliation Statement | CashAccountID, ReconNbr | 44 | 9 |  | PX_Objects_CA_CARecon, ReconciliationStatement, CARecon | members-02.md | 6437 | 60 |
| PX.Objects.CA.CAReconByPeriod | EntityType | Reconciliation by Period | CashAccountID, FinPeriodID | 3 | 1 |  | PX_Objects_CA_CAReconByPeriod, ReconciliationbyPeriod, CAReconByPeriod | members-02.md | 6498 | 10 |
| PX.Objects.CA.CASetup | EntityType | Cash Management Preferences |  | 62 | 11 |  |  | members-02.md | 6509 | 78 |
| PX.Objects.CA.CASetupApproval | EntityType | CA Approval Preferences | ApprovalID | 12 | 5 |  | PX_Objects_CA_CASetupApproval, CAApprovalPreferences, CASetupApproval | members-02.md | 6588 | 23 |
| PX.Objects.CA.CashAccount | EntityType | Cash Account | CashAccountCD | 69 | 65 |  | PX_Objects_CA_CashAccount, CashAccount | members-02.md | 6612 | 141 |
| PX.Objects.CA.CashAccountCheck | EntityType | Cash Account Check | CashAccountID, CheckNbr, PaymentMethodID | 16 | 9 |  | PX_Objects_CA_CashAccountCheck, CashAccountCheck | members-02.md | 6754 | 31 |
| PX.Objects.CA.CashAccountDeposit | EntityType | Clearing Account | CashAccountID, DepositAcctID, PaymentMethodID | 5 | 4 |  | PX_Objects_CA_CashAccountDeposit, ClearingAccount, CashAccountDeposit | members-02.md | 6786 | 15 |
| PX.Objects.CA.CashAccountETDetail | EntityType | Entry Type for Cash Account | CashAccountID, EntryTypeID | 12 | 9 |  | PX_Objects_CA_CashAccountETDetail, EntryTypeforCashAccount, CashAccountETDetail | members-02.md | 6802 | 27 |
| PX.Objects.CA.CashAccountPaymentMethodDetail | EntityType | Remittance Settings | CashAccountID, DetailID, PaymentMethodID | 5 | 6 |  | PX_Objects_CA_CashAccountPaymentMethodDetail, RemittanceSettings, CashAccountPaymentMethodDetail | members-02.md | 6830 | 17 |
| PX.Objects.CA.CashForecastTran | EntityType | Cash Transactions | TranID | 15 | 4 |  | PX_Objects_CA_CashForecastTran, CashTransactions1, CashForecastTran | members-02.md | 6848 | 26 |
| PX.Objects.CA.CASplit | EntityType | CA Transaction Details | AdjRefNbr, AdjTranType, LineNbr | 30 | 17 |  | PX_Objects_CA_CASplit, CATransactionDetails, CASplit | members-02.md | 6875 | 54 |
| PX.Objects.CA.CASummaryOnReconDate | EntityType | Aggregated CA Daily Summary until Reconciliation Date | CashAccountID, ReconNbr | 7 | 3 |  | PX_Objects_CA_CASummaryOnReconDate, AggregatedCADailySummaryuntilReconciliationDate, CASummaryOnReconDate | members-02.md | 6930 | 16 |
| PX.Objects.CA.CATax | EntityType | CA Tax Detail | AdjRefNbr, AdjTranType, LineNbr, TaxID | 22 | 6 |  | PX_Objects_CA_CATax, CATaxDetail, CATax | members-02.md | 6947 | 35 |
| PX.Objects.CA.CATaxTran | EntityType | CA Tax Transaction | Module, RecordID | 0 | 0 | PX.Objects.TX.TaxTran | PX_Objects_CA_CATaxTran, CATaxTransaction, CATaxTran | members-02.md | 6983 | 6 |
| PX.Objects.CA.CATran | EntityType | CA Transaction | TranID | 53 | 28 |  | PX_Objects_CA_CATran, CATransaction, CATran | members-02.md | 6990 | 88 |
| PX.Objects.CA.CATransfer | EntityType | Transfer | TransferNbr | 49 | 19 |  | PX_Objects_CA_CATransfer, Transfer, CATransfer | members-02.md | 7079 | 75 |
| PX.Objects.CA.CCBatch | EntityType | CCBatch | BatchID | 43 | 9 |  | PX_Objects_CA_CCBatch, CCBatch | members-02.md | 7155 | 59 |
| PX.Objects.CA.CCBatchAdjustment | EntityType | CCBatchAdjustment | BatchID, ExternalID | 10 | 1 |  | PX_Objects_CA_CCBatchAdjustment, CCBatchAdjustment | members-02.md | 7215 | 18 |
| PX.Objects.CA.CCBatchStatistics | EntityType | CCBatchStatistics | BatchID, ProcCenterCardTypeCode | 22 | 3 |  | PX_Objects_CA_CCBatchStatistics, CCBatchStatistics | members-02.md | 7234 | 32 |
| PX.Objects.CA.CCBatchTransaction | EntityType | CCBatchTransaction | BatchID, PCTranNumber, SettlementStatus | 34 | 6 |  | PX_Objects_CA_CCBatchTransaction, CCBatchTransaction | members-02.md | 7267 | 47 |
| PX.Objects.CA.CCProcessingCenter | EntityType | Processing Center | ProcessingCenterID | 45 | 23 |  | PX_Objects_CA_CCProcessingCenter, ProcessingCenter, CCProcessingCenter | members-02.md | 7315 | 75 |
| PX.Objects.CA.CCProcessingCenterDetail | EntityType | Credit Card Processing Center Detail | DetailID, ProcessingCenterID | 15 | 3 |  | PX_Objects_CA_CCProcessingCenterDetail, CreditCardProcessingCenterDetail, CCProcessingCenterDetail | members-02.md | 7391 | 24 |
| PX.Objects.CA.CCProcessingCenterFeeType | EntityType | Fee Type for Credit Card Processing Center | EntryTypeID, FeeType, ProcessingCenterID | 10 | 4 |  | PX_Objects_CA_CCProcessingCenterFeeType, FeeTypeforCreditCardProcessingCenter, CCProcessingCenterFeeType | members-02.md | 7416 | 20 |
| PX.Objects.CA.CCProcessingCenterPmntMethod | EntityType | Payment Method for Credit Card Processing Center | PaymentMethodID, ProcessingCenterID | 6 | 5 |  | PX_Objects_CA_CCProcessingCenterPmntMethod, PaymentMethodforCreditCardProcessingCenter, CCProcessingCenterPmntMethod | members-02.md | 7437 | 17 |
| PX.Objects.CA.CCProcessingCenterPmntMethodBranch | EntityType | Overrides By Branch | BranchID, PaymentMethodID | 10 | 6 |  | PX_Objects_CA_CCProcessingCenterPmntMethodBranch, OverridesByBranch, CCProcessingCenterPmntMethodBranch | members-02.md | 7455 | 22 |
| PX.Objects.CA.CCSynchronizeCard | EntityType |  | RecordID | 21 | 7 |  | PX_Objects_CA_CCSynchronizeCard | members-02.md | 7478 | 34 |
| PX.Objects.CA.CustomerProcessingCenterID | EntityType | Customer Processing Center ID | InstanceID | 5 | 4 |  | PX_Objects_CA_CustomerProcessingCenterID, CustomerProcessingCenterID | members-02.md | 7513 | 15 |
| PX.Objects.CA.Light.APAdjust | EntityType |  | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 8 | 25 |  | PX_Objects_CA_Light_APAdjust | members-02.md | 7529 | 38 |
| PX.Objects.CA.Light.APInvoice | EntityType |  | DocType, RefNbr | 8 | 30 | PX.Objects.CA.Light.APRegister | PX_Objects_CA_Light_APInvoice | members-02.md | 7568 | 45 |
| PX.Objects.CA.Light.APPayment | EntityType | Document | DocType, RefNbr | 10 | 17 | PX.Objects.AP.APRegister | PX_Objects_CA_Light_APPayment | members-02.md | 7614 | 34 |
| PX.Objects.CA.Light.APRegister | EntityType |  | DocType, RefNbr | 22 | 45 |  | PX_Objects_CA_Light_APRegister | members-02.md | 7649 | 73 |
| PX.Objects.CA.Light.ARAdjust | EntityType |  | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 8 | 28 |  | PX_Objects_CA_Light_ARAdjust | members-02.md | 7723 | 41 |
| PX.Objects.CA.Light.ARInvoice | EntityType |  | DocType, RefNbr | 7 | 37 | PX.Objects.CA.Light.ARRegister | PX_Objects_CA_Light_ARInvoice | members-02.md | 7765 | 51 |
| PX.Objects.CA.Light.ARPayment | EntityType | AR Document | DocType, RefNbr | 13 | 17 | PX.Objects.AR.ARRegister | PX_Objects_CA_Light_ARPayment | members-02.md | 7817 | 37 |
| PX.Objects.CA.Light.ARRegister | EntityType |  | DocType, RefNbr | 27 | 42 |  | PX_Objects_CA_Light_ARRegister | members-02.md | 7855 | 75 |
| PX.Objects.CA.Light.BAccount | EntityType |  | AcctCD | 11 | 2 |  | PX_Objects_CA_Light_BAccount | members-02.md | 7931 | 19 |
| PX.Objects.CA.Light.CABankTranAdjustment | EntityType |  | AdjNbr, TranID | 7 | 16 |  | PX_Objects_CA_Light_CABankTranAdjustment | members-02.md | 7951 | 28 |
| PX.Objects.CA.Light.Customer | EntityType | Customer | AcctCD | 2 | 2 | PX.Objects.CA.Light.BAccount | PX_Objects_CA_Light_Customer, Customer2 | members-02.md | 7980 | 11 |
| PX.Objects.CA.Light.CustomerMaster | EntityType | Customer | AcctCD | 0 | 6 | PX.Objects.CA.Light.Customer | PX_Objects_CA_Light_CustomerMaster | members-02.md | 7992 | 13 |
| PX.Objects.CA.Light.Location | EntityType | Location | BAccountID, LocationCD | 4 | 139 |  | PX_Objects_CA_Light_Location, Location2 | members-02.md | 8006 | 149 |
| PX.Objects.CA.Light.Vendor | EntityType | Customer | AcctCD | 1 | 188 | PX.Objects.CA.Light.BAccount | PX_Objects_CA_Light_Vendor, Customer3, Vendor2 | members-02.md | 8156 | 196 |
| PX.Objects.CA.PaymentMethod | EntityType | Payment Method | PaymentMethodID | 49 | 50 |  | PX_Objects_CA_PaymentMethod, PaymentMethod | members-02.md | 8353 | 106 |
| PX.Objects.CA.PaymentMethodAccount | EntityType | Payment Method for Cash Account | CashAccountID, PaymentMethodID | 14 | 4 |  | PX_Objects_CA_PaymentMethodAccount, PaymentMethodforCashAccount, PaymentMethodAccount | members-02.md | 8460 | 24 |
| PX.Objects.CA.PaymentMethodDetail | EntityType | Payment Method Detail | DetailID, PaymentMethodID, UseFor | 28 | 7 |  | PX_Objects_CA_PaymentMethodDetail, PaymentMethodDetail | members-02.md | 8485 | 42 |
| PX.Objects.CC.CCPayLink | EntityType | Payment Link | PayLinkID | 30 | 5 |  | PX_Objects_CC_CCPayLink, PaymentLink, CCPayLink | members-02.md | 8528 | 42 |
| PX.Objects.CC.CCProcessingCenterBranch | EntityType | Payment Creation Settings | BranchID, ProcessingCenterID | 6 | 5 |  | PX_Objects_CC_CCProcessingCenterBranch, PaymentCreationSettings, CCProcessingCenterBranch | members-02.md | 8571 | 17 |
| PX.Objects.CC.CCProcessingCenterTerminal | EntityType | Processing Center Terminal | ProcessingCenterID, TerminalID | 13 | 5 |  | PX_Objects_CC_CCProcessingCenterTerminal, ProcessingCenterTerminal, CCProcessingCenterTerminal | members-02.md | 8589 | 24 |
| PX.Objects.CC.DefaultTerminal | EntityType | Default POS Terminal | BranchID, ProcessingCenterID, UserID | 4 | 0 |  | PX_Objects_CC_DefaultTerminal, DefaultPOSTerminal, DefaultTerminal | members-02.md | 8614 | 10 |
| PX.Objects.CM.APHistoryLastRevaluation | EntityType |  | AccountID, BranchID, CuryID, SubID, VendorID | 6 | 1 |  | PX_Objects_CM_APHistoryLastRevaluation | members-02.md | 8625 | 12 |
| PX.Objects.CM.ARHistoryLastRevaluation | EntityType |  | AccountID, BranchID, CuryID, CustomerID, SubID | 6 | 1 |  | PX_Objects_CM_ARHistoryLastRevaluation | members-02.md | 8638 | 12 |
| PX.Objects.CM.CMSetup | EntityType | Currency Management Preferences |  | 31 | 16 |  |  | members-02.md | 8651 | 52 |
| PX.Objects.CM.Currency | EntityType | Currency | CuryID | 24 | 132 |  | PX_Objects_CM_Currency, Currency | members-02.md | 8704 | 163 |
| PX.Objects.CM.CurrencyInfo | EntityType | Currency Info | CuryInfoID | 15 | 90 |  | PX_Objects_CM_CurrencyInfo, CurrencyInfo | members-02.md | 8868 | 112 |
| PX.Objects.CM.CurrencyList | EntityType | Currency | CuryID | 15 | 37 |  | PX_Objects_CM_CurrencyList, Currency1, CurrencyList | members-02.md | 8981 | 59 |
| PX.Objects.CM.CurrencyRate | EntityType | Currency Rate | CuryRateID | 17 | 7 |  | PX_Objects_CM_CurrencyRate, CurrencyRate | members-02.md | 9041 | 31 |
| PX.Objects.CM.CurrencyRate2 | EntityType | Effective Currency Rate | CuryRateID | 0 | 0 | PX.Objects.CM.CurrencyRate | PX_Objects_CM_CurrencyRate2, EffectiveCurrencyRate, CurrencyRate2 | members-02.md | 9073 | 6 |
| PX.Objects.CM.CurrencyRateByDate | EntityType | Currency Rate by Date | CuryRateID | 1 | 0 | PX.Objects.CM.CurrencyRate | PX_Objects_CM_CurrencyRateByDate, CurrencyRatebyDate | members-02.md | 9080 | 8 |
| PX.Objects.CM.CurrencyRateByDateForVendor | EntityType | Currency Rate by Date | CuryRateID | 1 | 0 | PX.Objects.CM.CurrencyRate | PX_Objects_CM_CurrencyRateByDateForVendor, CurrencyRatebyDate1, CurrencyRateByDateForVendor | members-02.md | 9089 | 8 |
| PX.Objects.CM.CurrencyRateType | EntityType | Currency Rate Type | CuryRateTypeID | 13 | 23 |  | PX_Objects_CM_CurrencyRateType, CurrencyRateType | members-02.md | 9098 | 43 |
| PX.Objects.CM.Extensions.Currency | EntityType | Currency | CuryID | 15 | 132 |  | PX_Objects_CM_Extensions_Currency, Currency2 | members-02.md | 9142 | 154 |
| PX.Objects.CM.Extensions.CurrencyInfo | EntityType | Currency Info | CuryInfoID | 15 | 90 |  | PX_Objects_CM_Extensions_CurrencyInfo, CurrencyInfo1 | members-02.md | 9297 | 112 |
| PX.Objects.CM.Extensions.CurrencyList | EntityType | Currency | CuryID | 15 | 37 |  | PX_Objects_CM_Extensions_CurrencyList, Currency3, CurrencyList1 | members-02.md | 9410 | 59 |
| PX.Objects.CM.Extensions.CurrencyRate | EntityType | Currency Rate | CuryRateID | 15 | 7 |  | PX_Objects_CM_Extensions_CurrencyRate, CurrencyRate1 | members-02.md | 9470 | 28 |
| PX.Objects.CM.Extensions.CurrencyRateType | EntityType | Currency Rate Type | CuryRateTypeID | 13 | 23 |  | PX_Objects_CM_Extensions_CurrencyRateType, CurrencyRateType1 | members-02.md | 9499 | 43 |
| PX.Objects.CM.RefreshRate | EntityType |  | CuryRateType, FromCuryID | 5 | 5 |  | PX_Objects_CM_RefreshRate | members-02.md | 9543 | 16 |
| PX.Objects.CM.RevaluedAPHistory | EntityType | Revalued AP History | AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID | 9 | 0 | PX.Objects.AP.CuryAPHistory | PX_Objects_CM_RevaluedAPHistory, RevaluedAPHistory | members-02.md | 9560 | 17 |
| PX.Objects.CM.RevaluedARHistory | EntityType | Revalued AR History | AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID | 9 | 0 | PX.Objects.AR.CuryARHistory | PX_Objects_CM_RevaluedARHistory, RevaluedARHistory | members-02.md | 9578 | 17 |
| PX.Objects.CM.RevaluedGLHistory | EntityType | GL History | AccountID, BranchID, FinPeriodID, LedgerID, SubID | 8 | 0 | PX.Objects.GL.GLHistory | PX_Objects_CM_RevaluedGLHistory | members-02.md | 9596 | 16 |
| PX.Objects.CM.TranslationHistory | EntityType | Translation History | ReferenceNbr | 23 | 8 |  | PX_Objects_CM_TranslationHistory, TranslationHistory | members-02.md | 9613 | 38 |
| PX.Objects.CM.TranslationHistoryDetails | EntityType | Translation History Detail | AccountID, BranchID, LineType, ReferenceNbr, SubID | 31 | 11 |  | PX_Objects_CM_TranslationHistoryDetails, TranslationHistoryDetail, TranslationHistoryDetails | members-02.md | 9652 | 49 |
| PX.Objects.CM.TranslDef | EntityType | Translation Definition | TranslDefId | 17 | 9 |  | PX_Objects_CM_TranslDef, TranslationDefinition, TranslDef | members-02.md | 9702 | 33 |
| PX.Objects.CM.TranslDefDet | EntityType | Translation Definition Detail | LineNbr, TranslDefId | 13 | 9 |  | PX_Objects_CM_TranslDefDet, TranslationDefinitionDetail, TranslDefDet | members-02.md | 9736 | 29 |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceAnswer | EntityType | Compliance Answer | AttributeID, RefNoteID | 1 | 0 | PX.Objects.CS.CSAnswers | PX_Objects_CN_Compliance_CL_DAC_ComplianceAnswer, ComplianceAnswer | members-02.md | 9766 | 8 |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute | EntityType | Compliance Attribute | AttributeId | 12 | 6 |  | PX_Objects_CN_Compliance_CL_DAC_ComplianceAttribute, ComplianceAttribute | members-02.md | 9775 | 25 |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType | EntityType | Compliance Attribute Type | ComplianceAttributeTypeID | 2 | 4 |  | PX_Objects_CN_Compliance_CL_DAC_ComplianceAttributeType, ComplianceAttributeType | members-02.md | 9801 | 12 |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument | EntityType | Compliance Document | ComplianceDocumentID | 77 | 20 |  | PX_Objects_CN_Compliance_CL_DAC_ComplianceDocument, ComplianceDocument | members-02.md | 9814 | 104 |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill | EntityType | Compliance Document Bill Reference | ComplianceDocumentID, DocType, LineNbr, RefNbr | 14 | 3 |  | PX_Objects_CN_Compliance_CL_DAC_ComplianceDocumentBill, ComplianceDocumentBillReference, ComplianceDocumentBill | members-02.md | 9919 | 24 |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference | EntityType | Compliance Document Reference | ComplianceDocumentReferenceId | 13 | 2 |  | PX_Objects_CN_Compliance_CL_DAC_ComplianceDocumentReference, ComplianceDocumentReference | members-02.md | 9944 | 22 |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceNotification | EntityType | Compliance Notification | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_CN_Compliance_CL_DAC_ComplianceNotification, ComplianceNotification | members-02.md | 9967 | 6 |
| PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup | EntityType | Compliance Preferences |  | 22 | 2 |  |  | members-02.md | 9974 | 29 |
| PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient | EntityType | Lien Waiver Recipient | ProjectId, VendorClassId | 13 | 4 |  | PX_Objects_CN_Compliance_PM_DAC_LienWaiverRecipient, LienWaiverRecipient | members-02.md | 10004 | 24 |
| PX.Objects.CN.CRM.CR.DAC.MultipleQuote | EntityType | Multiple Customers | MultipleQuoteID | 22 | 4 |  | PX_Objects_CN_CRM_CR_DAC_MultipleQuote, MultipleCustomers, MultipleQuote | members-02.md | 10029 | 33 |
| PX.Objects.CN.JointChecks.JointPayee | EntityType | Joint Payee | JointPayeeId | 26 | 5 |  | PX_Objects_CN_JointChecks_JointPayee, JointPayee | members-02.md | 10063 | 38 |
| PX.Objects.CN.JointChecks.JointPayeePayment | EntityType | Joint Payee Payment | JointPayeePaymentId | 20 | 5 |  | PX_Objects_CN_JointChecks_JointPayeePayment, JointPayeePayment | members-02.md | 10102 | 32 |
| PX.Objects.CN.PMReportProject | EntityType | PM Report Project | BaseType, ContractCD | 13 | 145 |  | PX_Objects_CN_PMReportProject, PMReportProject | members-02.md | 10135 | 164 |
| PX.Objects.CN.PMSubAuditReportChangeOrderLine | EntityType | PM Subcontract Audit Report Change Order Line | LineNbr, OrderNbr | 6 | 2 |  | PX_Objects_CN_PMSubAuditReportChangeOrderLine, PMSubcontractAuditReportChangeOrderLine, PMSubAuditReportChangeOrderLine | members-02.md | 10300 | 14 |
| PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract | EntityType | PM Subcontract Audit Report Retainage Not Linked to Subcontract | DocType, RefNbr | 2 | 18 |  | PX_Objects_CN_PMSubAuditReportRetainageNotLinkedToSubcontract, PMSubcontractAuditReportRetainageNotLinkedtoSubcontract, PMSubAuditReportRetainageNotLinkedToSubcontract | members-02.md | 10315 | 26 |
| PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontractGrouped | ComplexType |  |  | 2 | 0 |  |  | members-02.md | 10342 | 5 |
| PX.Objects.CN.PMSubAuditReportUnappliedPrepayments | EntityType | PM Subcontract Audit Report Unapplied Prepayments | PONbr, RefNbr | 8 | 6 |  | PX_Objects_CN_PMSubAuditReportUnappliedPrepayments, PMSubcontractAuditReportUnappliedPrepayments, PMSubAuditReportUnappliedPrepayments | members-02.md | 10348 | 20 |
| PX.Objects.CN.PMWipBudget | EntityType | PM WIP Budget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID | 18 | 7 |  | PX_Objects_CN_PMWipBudget, PMWIPBudget | members-02.md | 10369 | 31 |
| PX.Objects.CN.PMWipChangeOrder | EntityType | PM WIP Change Order | RefNbr | 10 | 9 |  | PX_Objects_CN_PMWipChangeOrder, PMWIPChangeOrder | members-02.md | 10401 | 25 |
| PX.Objects.CN.PMWipChangeOrderBudget | EntityType | PM WIP Change Order Budget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID, RefNbr | 12 | 8 |  | PX_Objects_CN_PMWipChangeOrderBudget, PMWIPChangeOrderBudget | members-02.md | 10427 | 26 |
| PX.Objects.CN.PMWipChangeOrderLine | EntityType | PM WIP Change Order Line | LineNbr, RefNbr | 11 | 10 |  | PX_Objects_CN_PMWipChangeOrderLine, PMWIPChangeOrderLine | members-02.md | 10454 | 27 |
| PX.Objects.CN.PMWipCommitment | EntityType | PM WIP Commitment | CommitmentID | 6 | 4 |  | PX_Objects_CN_PMWipCommitment, PMWIPCommitment | members-02.md | 10482 | 16 |
| PX.Objects.CN.PMWipCostProjection | EntityType | PM WIP Cost Projection | ProjectID | 5 | 7 |  | PX_Objects_CN_PMWipCostProjection, PMWIPCostProjection | members-02.md | 10499 | 18 |
| PX.Objects.CN.PMWipCostProjectionBudget | EntityType | PM WIP Cost Projection Budget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID | 19 | 7 |  | PX_Objects_CN_PMWipCostProjectionBudget, PMWIPCostProjectionBudget | members-02.md | 10518 | 32 |
| PX.Objects.CN.PMWipDetailTotalForecastHistory | ComplexType |  |  | 10 | 0 |  |  | members-02.md | 10551 | 13 |
| PX.Objects.CN.PMWipForecastHistory | EntityType | PM WIP Forecast History | AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID | 13 | 0 |  | PX_Objects_CN_PMWipForecastHistory, PMWIPForecastHistory | members-02.md | 10565 | 19 |
| PX.Objects.CN.PMWipTotalBudget | ComplexType |  |  | 11 | 0 |  |  | members-02.md | 10585 | 14 |
| PX.Objects.CN.PMWipTotalForecastHistory | ComplexType |  |  | 7 | 0 |  |  | members-02.md | 10600 | 10 |
| PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField | EntityType | ComplianceRequirementField | FieldID, RequirementID | 10 | 3 |  | PX_Objects_CN_Requirements_ComplianceRequirementFields_ComplianceRequirementField, ComplianceRequirementField | members-02.md | 10611 | 19 |
| PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance | EntityType | Vendor Document Requirement Compliance | ReqComplianceID | 26 | 8 |  | PX_Objects_CN_Requirements_DAC_VendorDocumentReqCompliance, VendorDocumentRequirementCompliance, VendorDocumentReqCompliance | members-02.md | 10631 | 41 |
| PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow | EntityType | Vendor Document Requirement Condition Row | LineNbr, RequirementID | 17 | 3 |  | PX_Objects_CN_Requirements_DAC_VendorDocumentReqConditionRow, VendorDocumentRequirementConditionRow, VendorDocumentReqConditionRow | members-02.md | 10673 | 27 |
| PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement | EntityType | Vendor Document Requirement | RequirementID | 17 | 7 |  | PX_Objects_CN_Requirements_DAC_VendorDocumentRequirement, VendorDocumentRequirement | members-02.md | 10701 | 31 |
| PX.Objects.CN.SCSetup | EntityType | Subcontract Preferences |  | 12 | 5 |  |  | members-02.md | 10733 | 22 |
| PX.Objects.CN.Subcontracts.SC.DAC.Subcontract | EntityType | Subcontract | OrderNbr, OrderType | 0 | 0 | PX.Objects.PO.POOrder | PX_Objects_CN_Subcontracts_SC_DAC_Subcontract, Subcontract | members-02.md | 10756 | 6 |
| PX.Objects.CN.Subcontracts.SC.DAC.SubcontractInventoryItem | EntityType | Subcontract Inventory Item | InventoryCD | 0 | 0 | PX.Objects.IN.InventoryItem | PX_Objects_CN_Subcontracts_SC_DAC_SubcontractInventoryItem, SubcontractInventoryItem | members-02.md | 10763 | 6 |
| PX.Objects.CN.Subcontracts.SC.DAC.SubcontractNotification | EntityType | Subcontract Notification | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_CN_Subcontracts_SC_DAC_SubcontractNotification, SubcontractNotification | members-02.md | 10770 | 6 |
| PX.Objects.Common.DAC.DropShipLink | EntityType | Drop-Ship Link | POLineNbr, POOrderNbr, POOrderType, SOLineNbr, SOOrderNbr, SOOrderType | 24 | 6 |  | PX_Objects_Common_DAC_DropShipLink, DropShipLink | members-02.md | 10777 | 36 |
| PX.Objects.Common.DAC.ReportParameters.BAccountNoMask | EntityType |  | AcctCD, BAccountID | 14 | 210 |  | PX_Objects_Common_DAC_ReportParameters_BAccountNoMask | members-02.md | 10814 | 229 |
| PX.Objects.CR.Address | EntityType | Address | AddressID | 39 | 22 |  | PX_Objects_CR_Address, Address | members-02.md | 11044 | 68 |
| PX.Objects.CR.BAccount | EntityType | Business Account | AcctCD | 43 | 219 |  | PX_Objects_CR_BAccount, BusinessAccount, BAccount | members-02.md | 11113 | 269 |
| PX.Objects.CR.BAccount2 | EntityType | Business Account | AcctCD | 0 | 0 | PX.Objects.CR.BAccount | PX_Objects_CR_BAccount2 | members-02.md | 11383 | 6 |
| PX.Objects.CR.BAccountParent | EntityType | Parent Business Account | AcctCD | 0 | 0 | PX.Objects.CR.BAccount | PX_Objects_CR_BAccountParent, ParentBusinessAccount, BAccountParent | members-02.md | 11390 | 6 |
| PX.Objects.CR.Building | EntityType |  | BranchID, BuildingCD | 11 | 4 |  | PX_Objects_CR_Building | members-02.md | 11397 | 20 |
| PX.Objects.CR.Contact | EntityType | Contact | ContactID | 66 | 116 |  | PX_Objects_CR_Contact, Contact | members-02.md | 11418 | 189 |
| PX.Objects.CR.Contact2 | EntityType | Contact | ContactID | 0 | 0 | PX.Objects.CR.Contact | PX_Objects_CR_Contact2, Contact1, Contact2 | members-02.md | 11608 | 6 |
| PX.Objects.CR.ContactAccount | EntityType | Contact | ContactID | 5 | 3 | PX.Objects.CR.Contact | PX_Objects_CR_ContactAccount | members-02.md | 11615 | 15 |
| PX.Objects.CR.ContactExtAddress | EntityType | Contact with Address | AddressID | 32 | 95 | PX.Objects.CR.Address | PX_Objects_CR_ContactExtAddress, ContactwithAddress, ContactExtAddress | members-02.md | 11631 | 135 |
| PX.Objects.CR.ContactNotification | EntityType | Contact Notification | NotificationID | 6 | 1 | PX.Objects.CS.NotificationRecipient | PX_Objects_CR_ContactNotification, ContactNotification | members-02.md | 11767 | 15 |
| PX.Objects.CR.CRActivity | EntityType | Activity | NoteID | 52 | 28 |  | PX_Objects_CR_CRActivity, Activity, CRActivity | members-02.md | 11783 | 87 |
| PX.Objects.CR.CRActivityStatistics | EntityType | Activity Statistics | NoteID | 11 | 1 |  | PX_Objects_CR_CRActivityStatistics, ActivityStatistics, CRActivityStatistics | members-02.md | 11871 | 18 |
| PX.Objects.CR.CRAddress | EntityType | Opportunity Address | AddressID | 36 | 9 |  | PX_Objects_CR_CRAddress, OpportunityAddress, CRAddress | members-02.md | 11890 | 52 |
| PX.Objects.CR.CRBillingAddress | EntityType | Bill-To Address | AddressID | 0 | 0 | PX.Objects.CR.CRAddress | PX_Objects_CR_CRBillingAddress, BillToAddress, CRBillingAddress | members-02.md | 11943 | 6 |
| PX.Objects.CR.CRBillingContact | EntityType | Bill-To Contact | ContactID | 0 | 0 | PX.Objects.CR.CRContact | PX_Objects_CR_CRBillingContact, BillToContact, CRBillingContact | members-02.md | 11950 | 6 |
| PX.Objects.CR.CRCampaign | EntityType | Campaign | CampaignID | 27 | 19 |  | PX_Objects_CR_CRCampaign, Campaign, CRCampaign | members-02.md | 11957 | 53 |
| PX.Objects.CR.CRCampaignMembers | EntityType | Campaign Members | CampaignID, ContactID | 15 | 5 |  | PX_Objects_CR_CRCampaignMembers, CampaignMembers, CRCampaignMembers | members-02.md | 12011 | 26 |
| PX.Objects.CR.CRCampaignToCRMarketingListLink | EntityType | CRCampaign To CRMarketingList Link | CampaignID, MarketingListID | 4 | 2 |  | PX_Objects_CR_CRCampaignToCRMarketingListLink, CRCampaignToCRMarketingListLink | members-02.md | 12038 | 12 |
| PX.Objects.CR.CRCampaignType | EntityType | Campaign Class | TypeID | 11 | 3 |  | PX_Objects_CR_CRCampaignType, CampaignClass, CRCampaignType | members-02.md | 12051 | 21 |
| PX.Objects.CR.CRCase | EntityType | Case | CaseCD | 50 | 17 |  | PX_Objects_CR_CRCase, Case, CRCase | members-02.md | 12073 | 74 |
| PX.Objects.CR.CRCaseClass | EntityType | Case Class | CaseClassID | 30 | 12 |  | PX_Objects_CR_CRCaseClass, CaseClass, CRCaseClass | members-02.md | 12148 | 49 |
| PX.Objects.CR.CRCaseClassLaborMatrix | EntityType | Case Class Labor | CaseClassID, EarningType | 10 | 5 |  | PX_Objects_CR_CRCaseClassLaborMatrix, CaseClassLabor, CRCaseClassLaborMatrix | members-02.md | 12198 | 21 |
| PX.Objects.CR.CRCaseCommitments | EntityType | Case Commitments | CaseCD | 9 | 1 |  | PX_Objects_CR_CRCaseCommitments, CaseCommitments, CRCaseCommitments | members-02.md | 12220 | 17 |
| PX.Objects.CR.CRCaseReference | EntityType | Case Reference | ChildCaseCD, ParentCaseCD | 10 | 3 |  | PX_Objects_CR_CRCaseReference, CaseReference, CRCaseReference | members-02.md | 12238 | 19 |
| PX.Objects.CR.CRClassSeverityTime | EntityType | Time Reaction By Severity | CaseClassID, Severity | 18 | 3 |  | PX_Objects_CR_CRClassSeverityTime, TimeReactionBySeverity, CRClassSeverityTime | members-02.md | 12258 | 27 |
| PX.Objects.CR.CRContact | EntityType | Opportunity Contact | ContactID | 33 | 7 |  | PX_Objects_CR_CRContact, OpportunityContact, CRContact | members-02.md | 12286 | 47 |
| PX.Objects.CR.CRContactClass | EntityType | Contact Class | ClassID | 19 | 13 |  | PX_Objects_CR_CRContactClass, ContactClass, CRContactClass | members-02.md | 12334 | 39 |
| PX.Objects.CR.CRCustomerClass | EntityType | Business Account Class | CRCustomerClassID | 17 | 10 |  | PX_Objects_CR_CRCustomerClass, BusinessAccountClass, CRCustomerClass | members-02.md | 12374 | 34 |
| PX.Objects.CR.CREmployee | EntityType | Employee | AcctCD | 3 | 0 | PX.Objects.CR.BAccount | PX_Objects_CR_CREmployee, Employee, CREmployee | members-02.md | 12409 | 10 |
| PX.Objects.CR.CRLead | EntityType | Lead | ContactID | 13 | 4 | PX.Objects.CR.Contact | PX_Objects_CR_CRLead, Lead, CRLead | members-02.md | 12420 | 24 |
| PX.Objects.CR.CRLeadClass | EntityType | Lead Class | ClassID | 21 | 11 |  | PX_Objects_CR_CRLeadClass, LeadClass, CRLeadClass | members-02.md | 12445 | 39 |
| PX.Objects.CR.CRLeadStatistics | EntityType | Lead Statistics | ContactID | 3 | 2 |  | PX_Objects_CR_CRLeadStatistics, LeadStatistics, CRLeadStatistics | members-02.md | 12485 | 11 |
| PX.Objects.CR.CRMarketingCategory | EntityType | Marketing Category | MarketingCategoryID | 11 | 8 |  | PX_Objects_CR_CRMarketingCategory, MarketingCategory, CRMarketingCategory | members-02.md | 12497 | 25 |
| PX.Objects.CR.CRMarketingList | EntityType | Marketing List | MailListCode | 21 | 10 |  | PX_Objects_CR_CRMarketingList, MarketingList, CRMarketingList | members-02.md | 12523 | 38 |
| PX.Objects.CR.CRMarketingListAlias | EntityType | Marketing List | MailListCode | 0 | 0 | PX.Objects.CR.CRMarketingList | PX_Objects_CR_CRMarketingListAlias, MarketingList1, CRMarketingListAlias | members-02.md | 12562 | 6 |
| PX.Objects.CR.CRMarketingListMember | EntityType | Marketing List Member | ContactID, MarketingListID | 13 | 4 |  | PX_Objects_CR_CRMarketingListMember, MarketingListMember, CRMarketingListMember | members-02.md | 12569 | 24 |
| PX.Objects.CR.CRMassMail | EntityType | Mass Emails | MassMailCD | 23 | 8 |  | PX_Objects_CR_CRMassMail, MassEmails, CRMassMail | members-02.md | 12594 | 38 |
| PX.Objects.CR.CRMassMailCampaign | EntityType | Mass Mail Campaign Member | CampaignID, MassMailID | 8 | 3 |  | PX_Objects_CR_CRMassMailCampaign, MassMailCampaignMember, CRMassMailCampaign | members-02.md | 12633 | 17 |
| PX.Objects.CR.CRMassMailMarketingList | EntityType | Mass Mail Marketing List Member | MailListID, MassMailID | 8 | 3 |  | PX_Objects_CR_CRMassMailMarketingList, MassMailMarketingListMember, CRMassMailMarketingList | members-02.md | 12651 | 17 |
| PX.Objects.CR.CRMassMailMember | EntityType | Mass Mail Members | ContactID, MassMailID | 8 | 4 |  | PX_Objects_CR_CRMassMailMember, MassMailMembers, CRMassMailMember | members-02.md | 12669 | 18 |
| PX.Objects.CR.CRMassMailMessage | EntityType | Mass Mail Message | MassMailID, MessageID | 2 | 1 |  | PX_Objects_CR_CRMassMailMessage, MassMailMessage, CRMassMailMessage | members-02.md | 12688 | 9 |
| PX.Objects.CR.CROpportunity | EntityType | Opportunity | OpportunityID | 112 | 36 |  | PX_Objects_CR_CROpportunity, Opportunity, CROpportunity | members-02.md | 12698 | 155 |
| PX.Objects.CR.CROpportunityClass | EntityType | Opportunity Class | CROpportunityClassID | 18 | 12 |  | PX_Objects_CR_CROpportunityClass, OpportunityClass, CROpportunityClass | members-02.md | 12854 | 37 |
| PX.Objects.CR.CROpportunityClassProbability | EntityType |  | ClassID, StageID | 9 | 4 |  | PX_Objects_CR_CROpportunityClassProbability | members-02.md | 12892 | 18 |
| PX.Objects.CR.CROpportunityDiscountDetail | EntityType | Opportunity Discount | QuoteID, RecordID | 27 | 6 |  | PX_Objects_CR_CROpportunityDiscountDetail, OpportunityDiscount, CROpportunityDiscountDetail | members-02.md | 12911 | 40 |
| PX.Objects.CR.CROpportunityProbability | EntityType | Opportunity Probability | StageCode | 14 | 3 |  | PX_Objects_CR_CROpportunityProbability, OpportunityProbability, CROpportunityProbability | members-02.md | 12952 | 24 |
| PX.Objects.CR.CROpportunityProducts | EntityType | Opportunity Products | LineNbr, QuoteID | 61 | 16 |  | PX_Objects_CR_CROpportunityProducts, OpportunityProducts, CROpportunityProducts | members-02.md | 12977 | 84 |
| PX.Objects.CR.CROpportunityTax | EntityType | CR Tax Detail | LineNbr, QuoteID, TaxID | 19 | 6 |  | PX_Objects_CR_CROpportunityTax, CRTaxDetail, CROpportunityTax | members-02.md | 13062 | 32 |
| PX.Objects.CR.CRPMSMEmail | EntityType | Activity | NoteID | 10 | 2 | PX.Objects.CR.CRActivity | PX_Objects_CR_CRPMSMEmail | members-02.md | 13095 | 19 |
| PX.Objects.CR.CRPMTimeActivity | EntityType | Activity | NoteID | 38 | 12 | PX.Objects.CR.CRActivity | PX_Objects_CR_CRPMTimeActivity | members-02.md | 13115 | 58 |
| PX.Objects.CR.CRQuote | EntityType | Sales Quote | QuoteNbr | 109 | 30 |  | PX_Objects_CR_CRQuote, SalesQuote, CRQuote | members-02.md | 13174 | 146 |
| PX.Objects.CR.CRRelation | EntityType | Relations | RelationID | 25 | 4 |  | PX_Objects_CR_CRRelation, Relations, CRRelation | members-02.md | 13321 | 36 |
| PX.Objects.CR.CRReminder | EntityType | Reminder | NoteID | 16 | 4 |  | PX_Objects_CR_CRReminder, Reminder, CRReminder | members-02.md | 13358 | 27 |
| PX.Objects.CR.CRSetup | EntityType | Customer Management Preferences |  | 30 | 20 |  |  | members-02.md | 13386 | 55 |
| PX.Objects.CR.CRShippingAddress | EntityType | Shipping Address | AddressID | 0 | 0 | PX.Objects.CR.CRAddress | PX_Objects_CR_CRShippingAddress, ShippingAddress, CRShippingAddress | members-02.md | 13442 | 6 |
| PX.Objects.CR.CRShippingContact | EntityType | Shipping Contact | ContactID | 0 | 0 | PX.Objects.CR.CRContact | PX_Objects_CR_CRShippingContact, ShippingContact, CRShippingContact | members-02.md | 13449 | 6 |
| PX.Objects.CR.CRSMEmail | EntityType | Email Activity | NoteID | 34 | 5 | PX.Objects.CR.CRActivity | PX_Objects_CR_CRSMEmail, EmailActivity, CRSMEmail | members-02.md | 13456 | 47 |
| PX.Objects.CR.CRSMTeamsActivity | EntityType | Teams Activity | NoteID | 14 | 2 | PX.Objects.CR.CRActivity | PX_Objects_CR_CRSMTeamsActivity, TeamsActivity, CRSMTeamsActivity | members-02.md | 13504 | 24 |
| PX.Objects.CR.CRTaxTran | EntityType |  | LineNbr, QuoteID, RecordID, TaxID | 24 | 5 |  | PX_Objects_CR_CRTaxTran | members-02.md | 13529 | 35 |
| PX.Objects.CR.CRUnsubscribedPreferences | EntityType | Marketing Unsubscribed Contact | MarketingCategoryID, RecipientContact | 11 | 3 |  | PX_Objects_CR_CRUnsubscribedPreferences, MarketingUnsubscribedContact, CRUnsubscribedPreferences | members-02.md | 13565 | 21 |
| PX.Objects.CR.CRValidationRules | EntityType | Duplicate Validation Rules | NoteID | 16 | 2 |  | PX_Objects_CR_CRValidationRules, DuplicateValidationRules, CRValidationRules | members-03.md | 3 | 25 |
| PX.Objects.CR.DAC.CRNotification | EntityType | CR Notification | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_CR_DAC_CRNotification, CRNotification | members-03.md | 29 | 6 |
| PX.Objects.CR.DAC.Standalone.CRCampaign | EntityType | Campaign Statistics | CampaignID | 14 | 19 |  | PX_Objects_CR_DAC_Standalone_CRCampaign, CampaignStatistics, CRCampaign1 | members-03.md | 36 | 40 |
| PX.Objects.CR.Inquiry.CRSMEmail | EntityType | Email Activity | NoteID | 0 | 0 | PX.Objects.CR.CRSMEmail | PX_Objects_CR_Inquiry_CRSMEmail, EmailActivity1, CRSMEmail1 | members-03.md | 77 | 6 |
| PX.Objects.CR.Location | EntityType | Location | BAccountID, LocationCD | 90 | 139 |  | PX_Objects_CR_Location, Location | members-03.md | 84 | 236 |
| PX.Objects.CR.LocationARAccountSub | EntityType | Location GL Accounts | BAccountID, LocationID | 3 | 3 |  | PX_Objects_CR_LocationARAccountSub, LocationGLAccounts1, LocationARAccountSub | members-03.md | 321 | 12 |
| PX.Objects.CR.LocationBranchSettings | EntityType | Location Settings for Current Branch | BAccountID, BranchID, LocationID | 10 | 4 |  | PX_Objects_CR_LocationBranchSettings, LocationSettingsforCurrentBranch, LocationBranchSettings | members-03.md | 334 | 20 |
| PX.Objects.CR.LocationExtAddress | EntityType | Location with Address | AddressID | 67 | 18 | PX.Objects.CR.Address | PX_Objects_CR_LocationExtAddress, LocationwithAddress, LocationExtAddress | members-03.md | 355 | 93 |
| PX.Objects.CR.PMCRActivity | EntityType | Activity | NoteID | 1 | 0 | PX.Objects.CR.CRPMTimeActivity | PX_Objects_CR_PMCRActivity | members-03.md | 449 | 9 |
| PX.Objects.CR.PMTimeActivity | EntityType | Time Activity | NoteID | 46 | 28 |  | PX_Objects_CR_PMTimeActivity, TimeActivity, PMTimeActivity | members-03.md | 459 | 81 |
| PX.Objects.CR.SMEmail | EntityType | System Email | NoteID | 38 | 7 |  | PX_Objects_CR_SMEmail, SystemEmail, SMEmail | members-03.md | 541 | 52 |
| PX.Objects.CR.SMTeamsActivity | EntityType | Teams Activity | NoteID | 16 | 3 |  | PX_Objects_CR_SMTeamsActivity, TeamsActivity1, SMTeamsActivity | members-03.md | 594 | 26 |
| PX.Objects.CR.Standalone.CRLead | EntityType | Lead | ContactID | 10 | 10 |  | PX_Objects_CR_Standalone_CRLead, Lead1, CRLead1 | members-03.md | 621 | 27 |
| PX.Objects.CR.Standalone.CROpportunity | EntityType |  | OpportunityID | 25 | 36 |  | PX_Objects_CR_Standalone_CROpportunity | members-03.md | 649 | 67 |
| PX.Objects.CR.Standalone.CROpportunityRevision | EntityType |  | NoteID | 94 | 23 |  | PX_Objects_CR_Standalone_CROpportunityRevision | members-03.md | 717 | 123 |
| PX.Objects.CR.Standalone.CRQuote | EntityType |  | QuoteID, QuoteNbr | 16 | 30 |  | PX_Objects_CR_Standalone_CRQuote | members-03.md | 841 | 52 |
| PX.Objects.CR.Standalone.Location | EntityType |  | BAccountID, LocationCD | 108 | 9 |  | PX_Objects_CR_Standalone_Location | members-03.md | 894 | 123 |
| PX.Objects.CS.AddressValidatorPlugin | EntityType | Address Verification Service | AddressValidatorPluginID | 13 | 6 |  | PX_Objects_CS_AddressValidatorPlugin, AddressVerificationService, AddressValidatorPlugin | members-03.md | 1018 | 26 |
| PX.Objects.CS.AddressValidatorPluginDetail | EntityType | Address Verification Service Details | AddressValidatorPluginID, SettingID | 14 | 3 |  | PX_Objects_CS_AddressValidatorPluginDetail, AddressVerificationServiceDetails, AddressValidatorPluginDetail | members-03.md | 1045 | 23 |
| PX.Objects.CS.ArmGLHistoryByPeriod | EntityType | GL History by Period | AccountID, BranchID, FinPeriodID, LedgerID, SubID | 8 | 5 |  | PX_Objects_CS_ArmGLHistoryByPeriod, GLHistorybyPeriod, ArmGLHistoryByPeriod | members-03.md | 1069 | 20 |
| PX.Objects.CS.ARTranAlias | EntityType |  | RefNbr, TranType | 2 | 6 |  | PX_Objects_CS_ARTranAlias | members-03.md | 1090 | 13 |
| PX.Objects.CS.Carrier | EntityType | Carrier | CarrierID | 28 | 30 |  | PX_Objects_CS_Carrier, Carrier | members-03.md | 1104 | 65 |
| PX.Objects.CS.CarrierPackage | EntityType | Carrier Package | BoxID, CarrierID | 10 | 4 |  | PX_Objects_CS_CarrierPackage, CarrierPackage | members-03.md | 1170 | 20 |
| PX.Objects.CS.CarrierPlugin | EntityType | Carrier Plugin | CarrierPluginID | 22 | 9 |  | PX_Objects_CS_CarrierPlugin, CarrierPlugin | members-03.md | 1191 | 38 |
| PX.Objects.CS.CarrierPluginCustomer | EntityType | Carrier Plugin Customer | CarrierPluginID, RecordID | 15 | 6 |  | PX_Objects_CS_CarrierPluginCustomer, CarrierPluginCustomer | members-03.md | 1230 | 27 |
| PX.Objects.CS.CarrierPluginDetail | EntityType | Carrier Plugin Detail | CarrierPluginID, DetailID | 14 | 3 |  | PX_Objects_CS_CarrierPluginDetail, CarrierPluginDetail | members-03.md | 1258 | 23 |
| PX.Objects.CS.CommonSetup | EntityType | Common Setup |  | 12 | 5 |  |  | members-03.md | 1282 | 22 |
| PX.Objects.CS.Country | EntityType | Country | CountryID | 22 | 44 |  | PX_Objects_CS_Country, Country | members-03.md | 1305 | 73 |
| PX.Objects.CS.CSAnswers | EntityType | Answers | AttributeID, RefNoteID | 7 | 3 |  | PX_Objects_CS_CSAnswers, Answers, CSAnswers | members-03.md | 1379 | 17 |
| PX.Objects.CS.CSAttribute | EntityType | Attribute | AttributeID | 19 | 18 |  | PX_Objects_CS_CSAttribute, Attribute, CSAttribute | members-03.md | 1397 | 44 |
| PX.Objects.CS.CSAttributeDetail | EntityType | Attribute Detail | AttributeID, ValueID | 15 | 4 |  | PX_Objects_CS_CSAttributeDetail, AttributeDetail, CSAttributeDetail | members-03.md | 1442 | 26 |
| PX.Objects.CS.CSAttributeGroup | EntityType | Attribute Group | AttributeID, EntityClassID, EntityType | 16 | 5 |  | PX_Objects_CS_CSAttributeGroup, AttributeGroup, CSAttributeGroup | members-03.md | 1469 | 28 |
| PX.Objects.CS.CSBox | EntityType | Box | BoxID | 17 | 6 |  | PX_Objects_CS_CSBox, Box, CSBox | members-03.md | 1498 | 29 |
| PX.Objects.CS.CSCalendar | EntityType | Calendar | CalendarID | 40 | 19 |  | PX_Objects_CS_CSCalendar, Calendar, CSCalendar | members-03.md | 1528 | 66 |
| PX.Objects.CS.CSCalendarBreakTime | EntityType | Calendar Break Time | CalendarID, DayOfWeek, StartTime | 10 | 2 |  | PX_Objects_CS_CSCalendarBreakTime, CalendarBreakTime1, CSCalendarBreakTime | members-03.md | 1595 | 18 |
| PX.Objects.CS.CSCalendarExceptions | EntityType | Calendar Exception | CalendarID, Date | 10 | 0 |  | PX_Objects_CS_CSCalendarExceptions, CalendarException, CSCalendarExceptions | members-03.md | 1614 | 16 |
| PX.Objects.CS.DAC.OrganizationBAccount | EntityType | Company | AcctCD | 2 | 0 | PX.Objects.CR.BAccount | PX_Objects_CS_DAC_OrganizationBAccount, Company, OrganizationBAccount | members-03.md | 1631 | 9 |
| PX.Objects.CS.DaylightShift | EntityType | Daylight Shift | TimeZone, Year | 8 | 0 |  | PX_Objects_CS_DaylightShift, DaylightShift | members-03.md | 1641 | 15 |
| PX.Objects.CS.Dimension | EntityType | Dimension | DimensionID | 18 | 6 |  | PX_Objects_CS_Dimension, Dimension | members-03.md | 1657 | 31 |
| PX.Objects.CS.Email.EMailSyncFolder | EntityType | EMailSyncFolder | FolderID, ItemType, SyncAccountNoteID | 7 | 0 |  | PX_Objects_CS_Email_EMailSyncFolder, EMailSyncFolder | members-03.md | 1689 | 13 |
| PX.Objects.CS.FeaturesSet | EntityType | Features Set | Status | 214 | 0 |  | PX_Objects_CS_FeaturesSet, FeaturesSet | members-03.md | 1703 | 221 |
| PX.Objects.CS.FOBPoint | EntityType | FOB Point | FOBPointID | 12 | 15 |  | PX_Objects_CS_FOBPoint, FOBPoint | members-03.md | 1925 | 34 |
| PX.Objects.CS.FreightRate | EntityType | Freight Rate | CarrierID, LineNbr | 13 | 4 |  | PX_Objects_CS_FreightRate, FreightRate | members-03.md | 1960 | 23 |
| PX.Objects.CS.NotificationRecipient | EntityType | Notification Recipient | NotificationID | 21 | 5 |  | PX_Objects_CS_NotificationRecipient, NotificationRecipient | members-03.md | 1984 | 33 |
| PX.Objects.CS.NotificationSetup | EntityType | Default Notification setup | SetupID | 18 | 12 |  | PX_Objects_CS_NotificationSetup, DefaultNotificationsetup, NotificationSetup | members-03.md | 2018 | 36 |
| PX.Objects.CS.NotificationSetupRecipient | EntityType | Default Notification Recipient | RecipientID | 17 | 3 |  | PX_Objects_CS_NotificationSetupRecipient, DefaultNotificationRecipient, NotificationSetupRecipient | members-03.md | 2055 | 27 |
| PX.Objects.CS.NotificationSetupUserOverride | EntityType | User's Notification Setup | SetupID, UserID | 12 | 6 |  | PX_Objects_CS_NotificationSetupUserOverride, UsersNotificationSetup, NotificationSetupUserOverride | members-03.md | 2083 | 25 |
| PX.Objects.CS.NotificationSource | EntityType | Notification Source | SetupID, SourceID | 18 | 7 |  | PX_Objects_CS_NotificationSource, NotificationSource | members-03.md | 2109 | 32 |
| PX.Objects.CS.Numbering | EntityType | Numbering Sequence | NumberingID | 13 | 41 |  | PX_Objects_CS_Numbering, NumberingSequence, Numbering | members-03.md | 2142 | 61 |
| PX.Objects.CS.NumberingSequence | EntityType | Numbering Sequence Detail | NumberingID, NumberingSEQ | 15 | 4 |  | PX_Objects_CS_NumberingSequence, NumberingSequenceDetail, NumberingSequence1 | members-03.md | 2204 | 25 |
| PX.Objects.CS.ReasonCode | EntityType | Reason Code | ReasonCodeID | 13 | 25 |  | PX_Objects_CS_ReasonCode, ReasonCode | members-03.md | 2230 | 45 |
| PX.Objects.CS.SalesTerritory | EntityType | Sales Territory | SalesTerritoryID | 13 | 15 |  | PX_Objects_CS_SalesTerritory, SalesTerritory | members-03.md | 2276 | 35 |
| PX.Objects.CS.Segment | EntityType | Segment | DimensionID, SegmentID | 25 | 5 |  | PX_Objects_CS_Segment, Segment | members-03.md | 2312 | 37 |
| PX.Objects.CS.SegmentValue | EntityType | Segment Value | DimensionID, SegmentID, Value | 16 | 4 |  | PX_Objects_CS_SegmentValue, SegmentValue | members-03.md | 2350 | 27 |
| PX.Objects.CS.ShippingZone | EntityType | Shipping Zone | ZoneID | 11 | 17 |  | PX_Objects_CS_ShippingZone, ShippingZone | members-03.md | 2378 | 34 |
| PX.Objects.CS.ShippingZoneLine | EntityType | Shipping Zone Line | LineNbr, ZoneID | 11 | 6 |  | PX_Objects_CS_ShippingZoneLine, ShippingZoneLine | members-03.md | 2413 | 23 |
| PX.Objects.CS.ShipTerms | EntityType | Shipping Terms | ShipTermsID | 13 | 18 |  | PX_Objects_CS_ShipTerms, ShippingTerms, ShipTerms | members-03.md | 2437 | 38 |
| PX.Objects.CS.ShipTermsDetail | EntityType | Shiping Terms Detail | LineNbr, ShipTermsID | 14 | 3 |  | PX_Objects_CS_ShipTermsDetail, ShipingTermsDetail, ShipTermsDetail | members-03.md | 2476 | 23 |
| PX.Objects.CS.State | EntityType | State | CountryID, StateID | 18 | 26 |  | PX_Objects_CS_State, State | members-03.md | 2500 | 51 |
| PX.Objects.CS.Terms | EntityType | Terms | TermsID | 25 | 35 |  | PX_Objects_CS_Terms, Terms | members-03.md | 2552 | 67 |
| PX.Objects.CS.TermsInstallments | EntityType | Terms Installments Detail | InstallmentNbr, TermsID | 10 | 3 |  | PX_Objects_CS_TermsInstallments, TermsInstallmentsDetail, TermsInstallments | members-03.md | 2620 | 19 |
| PX.Objects.CT.Contract | EntityType | Contract | BaseType, ContractCD | 119 | 49 |  | PX_Objects_CT_Contract, Contract | members-03.md | 2640 | 175 |
| PX.Objects.CT.ContractBillingSchedule | EntityType | Contract Billing Schedule | ContractID | 16 | 8 |  | PX_Objects_CT_ContractBillingSchedule, ContractBillingSchedule | members-03.md | 2816 | 30 |
| PX.Objects.CT.ContractBillingTrace | EntityType | Contract Billing Trace | ContractID, DocType, RecordID, RefNbr | 13 | 3 |  | PX_Objects_CT_ContractBillingTrace, ContractBillingTrace | members-03.md | 2847 | 22 |
| PX.Objects.CT.ContractDetail | EntityType | Contract Detail | ContractID, LineNbr | 69 | 7 |  | PX_Objects_CT_ContractDetail, ContractDetail | members-03.md | 2870 | 83 |
| PX.Objects.CT.ContractDetailAcum | EntityType | Contract Detail | ContractID, LineNbr | 0 | 0 | PX.Objects.CT.ContractDetail | PX_Objects_CT_ContractDetailAcum | members-03.md | 2954 | 6 |
| PX.Objects.CT.ContractItem | EntityType | Contract Item | ContractItemCD | 50 | 11 |  | PX_Objects_CT_ContractItem, ContractItem | members-03.md | 2961 | 68 |
| PX.Objects.CT.ContractRenewalHistory | EntityType | Contract Renewal History | ContractID, RevID | 28 | 5 |  | PX_Objects_CT_ContractRenewalHistory, ContractRenewalHistory | members-03.md | 3030 | 40 |
| PX.Objects.CT.ContractRevisionByPeriod | EntityType | Contract revision by period | ContractID, FinPeriodID | 11 | 2 |  | PX_Objects_CT_ContractRevisionByPeriod, Contractrevisionbyperiod | members-03.md | 3071 | 20 |
| PX.Objects.CT.ContractSLAMapping | EntityType | Contract SLA Mapping | ContractSLAMappingID | 11 | 3 |  | PX_Objects_CT_ContractSLAMapping, ContractSLAMapping | members-03.md | 3092 | 20 |
| PX.Objects.CT.ContractTemplate | EntityType | Contract Template | BaseType, ContractCD | 3 | 0 | PX.Objects.CT.Contract | PX_Objects_CT_ContractTemplate, ContractTemplate | members-03.md | 3113 | 11 |
| PX.Objects.CT.SelContractWatcher | EntityType |  | ContractID, EMail | 13 | 6 |  | PX_Objects_CT_SelContractWatcher | members-03.md | 3125 | 24 |
| PX.Objects.CT.Standalone.ContractDetail | EntityType |  | ContractDetailID, ContractID, RevID | 19 | 7 |  | PX_Objects_CT_Standalone_ContractDetail | members-03.md | 3150 | 32 |
| PX.Objects.DR.DRDeferredCode | EntityType | Deferral Code | DeferredCodeID | 25 | 12 |  | PX_Objects_DR_DRDeferredCode, DeferralCode, DRDeferredCode | members-03.md | 3183 | 44 |
| PX.Objects.DR.DRExpenseBalance | EntityType | DR Expense Balance | AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID | 24 | 6 |  | PX_Objects_DR_DRExpenseBalance, DRExpenseBalance | members-03.md | 3228 | 36 |
| PX.Objects.DR.DRExpenseBalance2 | EntityType | DR Expense Balance | AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID | 0 | 0 | PX.Objects.DR.DRExpenseBalance | PX_Objects_DR_DRExpenseBalance2 | members-03.md | 3265 | 6 |
| PX.Objects.DR.DRExpenseBalanceByPeriod | EntityType | DR Expense Balance by Period | AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID | 8 | 6 |  | PX_Objects_DR_DRExpenseBalanceByPeriod, DRExpenseBalancebyPeriod | members-03.md | 3272 | 20 |
| PX.Objects.DR.DRExpenseProjection | EntityType | DR Expense Projection | AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID | 14 | 6 |  | PX_Objects_DR_DRExpenseProjection, DRExpenseProjection | members-03.md | 3293 | 26 |
| PX.Objects.DR.DRRevenueBalance | EntityType | DR Revenue Balance | AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID | 24 | 6 |  | PX_Objects_DR_DRRevenueBalance, DRRevenueBalance | members-03.md | 3320 | 36 |
| PX.Objects.DR.DRRevenueBalance2 | EntityType | DR Revenue Balance | AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID | 0 | 0 | PX.Objects.DR.DRRevenueBalance | PX_Objects_DR_DRRevenueBalance2 | members-03.md | 3357 | 6 |
| PX.Objects.DR.DRRevenueBalanceByPeriod | EntityType | DR Revenue Balance by Period | AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID | 8 | 6 |  | PX_Objects_DR_DRRevenueBalanceByPeriod, DRRevenueBalancebyPeriod | members-03.md | 3364 | 20 |
| PX.Objects.DR.DRRevenueProjection | EntityType | DR Revenue Projection | AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID | 14 | 6 |  | PX_Objects_DR_DRRevenueProjection, DRRevenueProjection | members-03.md | 3385 | 26 |
| PX.Objects.DR.DRSchedule | EntityType | Deferral Schedule | ScheduleNbr | 43 | 17 |  | PX_Objects_DR_DRSchedule, DeferralSchedule, DRSchedule | members-03.md | 3412 | 67 |
| PX.Objects.DR.DRScheduleDetail | EntityType | Deferral Schedule Component | ComponentID, DetailLineNbr, ScheduleID | 54 | 16 |  | PX_Objects_DR_DRScheduleDetail, DeferralScheduleComponent, DRScheduleDetail | members-03.md | 3480 | 77 |
| PX.Objects.DR.DRScheduleTran | EntityType | DRScheduleTran | ComponentID, DetailLineNbr, LineNbr, ScheduleID | 25 | 9 |  | PX_Objects_DR_DRScheduleTran, DRScheduleTran | members-03.md | 3558 | 41 |
| PX.Objects.DR.DRScheduleTranLineLink | EntityType | DR Schedule Transaction Lines | ScheduleID | 6 | 7 |  | PX_Objects_DR_DRScheduleTranLineLink, DRScheduleTransactionLines, DRScheduleTranLineLink | members-03.md | 3600 | 19 |
| PX.Objects.DR.DRSetup | EntityType | Deferred Revenue Preferences |  | 3 | 3 |  |  | members-03.md | 3620 | 11 |
| PX.Objects.EP.ClockInClockOut.EPClockInTimerData | EntityType | Timer | TimerDataID | 27 | 2 |  | PX_Objects_EP_ClockInClockOut_EPClockInTimerData, Timer, EPClockInTimerData | members-03.md | 3632 | 36 |
| PX.Objects.EP.ClockInClockOut.EPTimeLog | EntityType | Time Log | TimeLogID | 21 | 3 |  | PX_Objects_EP_ClockInClockOut_EPTimeLog, TimeLog, EPTimeLog | members-03.md | 3669 | 30 |
| PX.Objects.EP.ClockInClockOut.EPTimeLogType | EntityType | Time Log Type | TimeLogTypeID | 10 | 3 |  | PX_Objects_EP_ClockInClockOut_EPTimeLogType, TimeLogType, EPTimeLogType | members-03.md | 3700 | 19 |
| PX.Objects.EP.ContractEx | EntityType | Contract | BaseType, ContractCD | 0 | 0 | PX.Objects.CT.Contract | PX_Objects_EP_ContractEx | members-03.md | 3720 | 6 |
| PX.Objects.EP.ContractExEx | EntityType | Contract | BaseType, ContractCD | 0 | 0 | PX.Objects.CT.Contract | PX_Objects_EP_ContractExEx | members-03.md | 3727 | 6 |
| PX.Objects.EP.DAC.EPEmployeeCorpCardLink | EntityType | Employee Corporate Card Reference | CorpCardID, EmployeeID | 2 | 3 |  | PX_Objects_EP_DAC_EPEmployeeCorpCardLink, EmployeeCorporateCardReference, EPEmployeeCorpCardLink | members-03.md | 3734 | 11 |
| PX.Objects.EP.DAC.EPExpenseClaimForCurrentUser | EntityType | Expense Claim | RefNbr | 0 | 0 | PX.Objects.EP.EPExpenseClaim | PX_Objects_EP_DAC_EPExpenseClaimForCurrentUser, ExpenseClaim1, EPExpenseClaimForCurrentUser | members-03.md | 3746 | 6 |
| PX.Objects.EP.DAC.EPRuleApprover | EntityType | Rule Approver | RuleApproverID | 10 | 5 |  | PX_Objects_EP_DAC_EPRuleApprover, RuleApprover, EPRuleApprover | members-03.md | 3753 | 21 |
| PX.Objects.EP.EPActivityApprove | EntityType | Time Activity | NoteID | 6 | 0 | PX.Objects.CR.PMTimeActivity | PX_Objects_EP_EPActivityApprove | members-03.md | 3775 | 14 |
| PX.Objects.EP.EPActivityApprove2 | EntityType | Mass Weekly Crew Time Entry | NoteID | 1 | 0 | PX.Objects.EP.EPActivityApprove | PX_Objects_EP_EPActivityApprove2, MassWeeklyCrewTimeEntry, EPActivityApprove2 | members-03.md | 3790 | 8 |
| PX.Objects.EP.EPActivityRelease | EntityType | Release Time Activity | NoteID | 1 | 0 | PX.Objects.EP.EPActivityApprove | PX_Objects_EP_EPActivityRelease, ReleaseTimeActivity, EPActivityRelease | members-03.md | 3799 | 8 |
| PX.Objects.EP.EPActivityType | EntityType | Activity Type | Type | 18 | 6 |  | PX_Objects_EP_EPActivityType, ActivityType, EPActivityType | members-03.md | 3808 | 31 |
| PX.Objects.EP.EPApproval | EntityType | Approval | ApprovalID | 41 | 12 |  | PX_Objects_EP_EPApproval, Approval, EPApproval | members-03.md | 3840 | 60 |
| PX.Objects.EP.EPAssignmentMap | EntityType | Assignment Map | AssignmentMapID | 15 | 30 |  | PX_Objects_EP_EPAssignmentMap, AssignmentMap, EPAssignmentMap | members-03.md | 3901 | 52 |
| PX.Objects.EP.EPAssignmentRoute | EntityType | Legacy Assignment Route | AssignmentRouteID | 21 | 9 |  | PX_Objects_EP_EPAssignmentRoute, LegacyAssignmentRoute, EPAssignmentRoute | members-03.md | 3954 | 37 |
| PX.Objects.EP.EPAssignmentRule | EntityType | Legacy Assignmnent Rule | AssignmentRuleID | 13 | 3 |  | PX_Objects_EP_EPAssignmentRule, LegacyAssignmnentRule, EPAssignmentRule | members-03.md | 3992 | 22 |
| PX.Objects.EP.EPAttendee | EntityType | Attendee | AttendeeID, EventNoteID | 14 | 4 |  | PX_Objects_EP_EPAttendee, Attendee, EPAttendee | members-03.md | 4015 | 24 |
| PX.Objects.EP.EPContractRate | EntityType | Contract Rates | RecordID | 13 | 5 |  | PX_Objects_EP_EPContractRate, ContractRates, EPContractRate | members-03.md | 4040 | 24 |
| PX.Objects.EP.EPCustomWeek | EntityType | Custom Week | WeekID | 18 | 2 |  | PX_Objects_EP_EPCustomWeek, CustomWeek, EPCustomWeek | members-03.md | 4065 | 27 |
| PX.Objects.EP.EPDepartment | EntityType | Department | DepartmentID | 9 | 8 |  | PX_Objects_EP_EPDepartment, Department, EPDepartment | members-03.md | 4093 | 23 |
| PX.Objects.EP.EPEarningType | EntityType | Earning Type | TypeCD | 13 | 35 |  | PX_Objects_EP_EPEarningType, EarningType, EPEarningType | members-03.md | 4117 | 54 |
| PX.Objects.EP.EPEmployee | EntityType | Employee | AcctCD | 13 | 26 | PX.Objects.AP.Vendor | PX_Objects_EP_EPEmployee, Employee1, EPEmployee | members-03.md | 4172 | 46 |
| PX.Objects.EP.EPEmployeeClass | EntityType | Employee Class | VendorClassID | 4 | 3 | PX.Objects.AP.VendorClass | PX_Objects_EP_EPEmployeeClass, EmployeeClass, EPEmployeeClass | members-03.md | 4219 | 14 |
| PX.Objects.EP.EPEmployeeClassLaborMatrix | EntityType | Employee Class Labor | EarningType, EmployeeID | 10 | 5 |  | PX_Objects_EP_EPEmployeeClassLaborMatrix, EmployeeClassLabor, EPEmployeeClassLaborMatrix | members-03.md | 4234 | 21 |
| PX.Objects.EP.EPEmployeeContract | EntityType | Employee Contract | ContractID, EmployeeID | 9 | 5 |  | PX_Objects_EP_EPEmployeeContract, EmployeeContract, EPEmployeeContract | members-03.md | 4256 | 20 |
| PX.Objects.EP.EPEmployeeEx | EntityType | Employee | AcctCD | 0 | 0 | PX.Objects.EP.EPEmployee | PX_Objects_EP_EPEmployeeEx | members-03.md | 4277 | 6 |
| PX.Objects.EP.EPEmployeePosition | EntityType | Employee Position | EmployeeID, LineNbr | 20 | 4 |  | PX_Objects_EP_EPEmployeePosition, EmployeePosition, EPEmployeePosition | members-03.md | 4284 | 31 |
| PX.Objects.EP.EPEquipment | EntityType | Equipment | EquipmentCD | 23 | 13 |  | PX_Objects_EP_EPEquipment, Equipment, EPEquipment | members-03.md | 4316 | 43 |
| PX.Objects.EP.EPEquipmentDetail | EntityType | Equipment Time Card Detail | LineNbr, TimeCardCD | 22 | 9 |  | PX_Objects_EP_EPEquipmentDetail, EquipmentTimeCardDetail, EPEquipmentDetail | members-03.md | 4360 | 38 |
| PX.Objects.EP.EPEquipmentRate | EntityType | Equipment Rate | EquipmentID, ProjectID | 15 | 4 |  | PX_Objects_EP_EPEquipmentRate, EquipmentRate, EPEquipmentRate | members-03.md | 4399 | 26 |
| PX.Objects.EP.EPEquipmentSummary | EntityType | Equipment Time Card Summary | LineNbr, TimeCardCD | 24 | 7 |  | PX_Objects_EP_EPEquipmentSummary, EquipmentTimeCardSummary, EPEquipmentSummary | members-03.md | 4426 | 38 |
| PX.Objects.EP.EPEquipmentTimeCard | EntityType | Equipment Time Card | TimeCardCD | 42 | 6 |  | PX_Objects_EP_EPEquipmentTimeCard, EquipmentTimeCard, EPEquipmentTimeCard | members-03.md | 4465 | 55 |
| PX.Objects.EP.EPEventCategory | EntityType | Event Category | CategoryID | 9 | 5 |  | PX_Objects_EP_EPEventCategory, EventCategory, EPEventCategory | members-03.md | 4521 | 20 |
| PX.Objects.EP.EPExpenseClaim | EntityType | Expense Claim | RefNbr | 49 | 19 |  | PX_Objects_EP_EPExpenseClaim, ExpenseClaim, EPExpenseClaim | members-03.md | 4542 | 75 |
| PX.Objects.EP.EPExpenseClaimDetails | EntityType | Expense Receipt | ClaimDetailCD | 103 | 37 |  | PX_Objects_EP_EPExpenseClaimDetails, ExpenseReceipt, EPExpenseClaimDetails | members-03.md | 4618 | 147 |
| PX.Objects.EP.EPPosition | EntityType | Position | PositionID | 9 | 7 |  | PX_Objects_EP_EPPosition, Position, EPPosition | members-03.md | 4766 | 22 |
| PX.Objects.EP.EPRule | EntityType | Assignment/Approval Rule | RuleID | 27 | 9 |  | PX_Objects_EP_EPRule, AssignmentApprovalRule, EPRule | members-03.md | 4789 | 43 |
| PX.Objects.EP.EPRuleCondition | EntityType | Assignment/Approval Rule Condition | RowNbr, RuleID | 21 | 3 |  | PX_Objects_EP_EPRuleCondition, AssignmentApprovalRuleCondition, EPRuleCondition | members-03.md | 4833 | 31 |
| PX.Objects.EP.EPRuleEmployeeCondition | EntityType | Assignment/Approval Rule Employee Condition | RowNbr, RuleID | 20 | 3 |  | PX_Objects_EP_EPRuleEmployeeCondition, AssignmentApprovalRuleEmployeeCondition, EPRuleEmployeeCondition | members-03.md | 4865 | 30 |
| PX.Objects.EP.EPRuleTree | EntityType | Assignment/Approval Rule | RuleID | 0 | 0 | PX.Objects.EP.EPRule | PX_Objects_EP_EPRuleTree | members-03.md | 4896 | 6 |
| PX.Objects.EP.EPSetup | EntityType | Time & Expenses Preferences |  | 67 | 27 |  |  | members-03.md | 4903 | 99 |
| PX.Objects.EP.EPShiftCode | EntityType | Shift Code | ShiftCD | 13 | 17 |  | PX_Objects_EP_EPShiftCode, ShiftCode, EPShiftCode | members-03.md | 5003 | 37 |
| PX.Objects.EP.EPShiftCodeRate | EntityType | Shift Code Rate | CuryID, EffectiveDate, ShiftID | 14 | 3 |  | PX_Objects_EP_EPShiftCodeRate, ShiftCodeRate, EPShiftCodeRate | members-03.md | 5041 | 23 |
| PX.Objects.EP.EPTax | EntityType | EP Tax Detail | ClaimDetailID, IsTipTax, TaxID | 22 | 5 |  | PX_Objects_EP_EPTax, EPTaxDetail, EPTax | members-03.md | 5065 | 34 |
| PX.Objects.EP.EPTaxAggregate | EntityType |  | RefNbr, TaxID | 17 | 5 |  | PX_Objects_EP_EPTaxAggregate | members-03.md | 5100 | 28 |
| PX.Objects.EP.EPTaxTran | EntityType |  | ClaimDetailID, IsTipTax, TaxID | 26 | 5 |  | PX_Objects_EP_EPTaxTran | members-03.md | 5129 | 37 |
| PX.Objects.EP.EPTimeActivitiesSummary | EntityType | Time Activities Summary | ContactID, Week, WorkgroupID | 24 | 6 |  | PX_Objects_EP_EPTimeActivitiesSummary, TimeActivitiesSummary, EPTimeActivitiesSummary | members-03.md | 5167 | 37 |
| PX.Objects.EP.EPTimeCard | EntityType | Employee Time Card | TimeCardCD | 82 | 11 |  | PX_Objects_EP_EPTimeCard, EmployeeTimeCard, EPTimeCard | members-03.md | 5205 | 100 |
| PX.Objects.EP.EPTimeCardEx | EntityType | Employee Time Card | TimeCardCD | 0 | 0 | PX.Objects.EP.EPTimeCard | PX_Objects_EP_EPTimeCardEx | members-03.md | 5306 | 6 |
| PX.Objects.EP.EPTimeCardItem | EntityType | Time Card Item | LineNbr, TimeCardCD | 87 | 9 |  | PX_Objects_EP_EPTimeCardItem, TimeCardItem, EPTimeCardItem | members-03.md | 5313 | 103 |
| PX.Objects.EP.EPTimeCardSummary | EntityType | Time Card Summary | LineNbr, TimeCardCD | 29 | 13 |  | PX_Objects_EP_EPTimeCardSummary, TimeCardSummary, EPTimeCardSummary | members-03.md | 5417 | 49 |
| PX.Objects.EP.EPView | EntityType | Activity View Status | ContactID, NoteID | 10 | 2 |  | PX_Objects_EP_EPView, ActivityViewStatus, EPView | members-03.md | 5467 | 18 |
| PX.Objects.EP.EPViewMy | EntityType | Activity View Status | ContactID, NoteID | 0 | 0 | PX.Objects.EP.EPView | PX_Objects_EP_EPViewMy, ActivityViewStatus1, EPViewMy | members-03.md | 5486 | 6 |
| PX.Objects.EP.EPWeeklyCrewTimeActivity | EntityType | Weekly Crew Time Activity | Week, WorkgroupID | 8 | 4 |  | PX_Objects_EP_EPWeeklyCrewTimeActivity, WeeklyCrewTimeActivity, EPWeeklyCrewTimeActivity | members-03.md | 5493 | 18 |
| PX.Objects.EP.EPWingman | EntityType | Delegate | RecordID | 13 | 6 |  | PX_Objects_EP_EPWingman, Delegate, EPWingman | members-03.md | 5512 | 25 |
| PX.Objects.EP.Standalone.EPEmployeeClass | EntityType |  | VendorClassID | 1 | 32 |  | PX_Objects_EP_Standalone_EPEmployeeClass | members-03.md | 5538 | 38 |
| PX.Objects.EP.TimecardWithTotals | EntityType |  | TimeCardCD | 19 | 8 |  | PX_Objects_EP_TimecardWithTotals | members-03.md | 5577 | 33 |
| PX.Objects.FA.DAC.FALocationHistoryByPeriod | EntityType | FA Location History by Period | AssetID, LastRevisionID | 4 | 15 |  | PX_Objects_FA_DAC_FALocationHistoryByPeriod, FALocationHistorybyPeriod | members-03.md | 5611 | 25 |
| PX.Objects.FA.FAAccrualTran | EntityType | FA Accrual Transaction | GLTranID | 41 | 10 |  | PX_Objects_FA_FAAccrualTran, FAAccrualTransaction, FAAccrualTran | members-03.md | 5637 | 58 |
| PX.Objects.FA.FAApplicableMethod | EntityType | FA Applicable Method | AssetID, BookID, StartPeriodID | 17 | 6 |  | PX_Objects_FA_FAApplicableMethod, FAApplicableMethod | members-03.md | 5696 | 30 |
| PX.Objects.FA.FABonus | EntityType | Bonus | BonusCD | 13 | 4 |  | PX_Objects_FA_FABonus, Bonus, FABonus | members-03.md | 5727 | 24 |
| PX.Objects.FA.FABonusDetails | EntityType | FA Bonus Details | BonusID, LineNbr | 13 | 3 |  | PX_Objects_FA_FABonusDetails, FABonusDetails | members-03.md | 5752 | 22 |
| PX.Objects.FA.FABook | EntityType | FA Book | BookCode | 13 | 13 |  | PX_Objects_FA_FABook, FABook | members-03.md | 5775 | 32 |
| PX.Objects.FA.FABookBalance | EntityType | FA Book Balance | AssetID, BookID | 59 | 8 |  | PX_Objects_FA_FABookBalance, FABookBalance | members-03.md | 5808 | 74 |
| PX.Objects.FA.FABookHistory | EntityType | FA Book History | AssetID, BookID, FinPeriodID | 52 | 4 |  | PX_Objects_FA_FABookHistory, FABookHistory | members-03.md | 5883 | 63 |
| PX.Objects.FA.FABookHistoryByPeriod | EntityType | FA Book History by Period | AssetID, BookID, FinPeriodID | 4 | 2 |  | PX_Objects_FA_FABookHistoryByPeriod, FABookHistorybyPeriod | members-03.md | 5947 | 12 |
| PX.Objects.FA.FABookHistoryRecon | EntityType | FA Book History for Reconciliation | AssetID, BookID | 6 | 2 |  | PX_Objects_FA_FABookHistoryRecon, FABookHistoryforReconciliation, FABookHistoryRecon | members-03.md | 5960 | 14 |
| PX.Objects.FA.FABookPeriod | EntityType | FA Book Period | BookID, FinPeriodID, OrganizationID | 21 | 5 |  | PX_Objects_FA_FABookPeriod, FABookPeriod | members-03.md | 5975 | 33 |
| PX.Objects.FA.FABookPeriodSetup | EntityType | FA Book Period Template | BookID, PeriodNbr | 14 | 4 |  | PX_Objects_FA_FABookPeriodSetup, FABookPeriodTemplate, FABookPeriodSetup | members-03.md | 6009 | 25 |
| PX.Objects.FA.FABookSettings | EntityType | FA Book Preferences | AssetID, BookID | 19 | 6 |  | PX_Objects_FA_FABookSettings, FABookPreferences, FABookSettings | members-03.md | 6035 | 31 |
| PX.Objects.FA.FABookYear | EntityType | FA Book Year | BookID, OrganizationID, Year | 14 | 5 |  | PX_Objects_FA_FABookYear, FABookYear | members-03.md | 6067 | 25 |
| PX.Objects.FA.FABookYearSetup | EntityType | Book Calendar | BookID | 21 | 4 |  | PX_Objects_FA_FABookYearSetup, BookCalendar, FABookYearSetup | members-03.md | 6093 | 32 |
| PX.Objects.FA.FAClass | EntityType | Asset Class | AssetCD | 0 | 0 | PX.Objects.FA.FixedAsset | PX_Objects_FA_FAClass, AssetClass, FAClass | members-03.md | 6126 | 6 |
| PX.Objects.FA.FAComponent | EntityType | FA Component | AssetCD | 0 | 0 | PX.Objects.FA.FixedAsset | PX_Objects_FA_FAComponent, FAComponent | members-03.md | 6133 | 6 |
| PX.Objects.FA.FADepreciationMethod | EntityType | Depreciation Method | MethodCD | 32 | 7 |  | PX_Objects_FA_FADepreciationMethod, DepreciationMethod, FADepreciationMethod | members-03.md | 6140 | 46 |
| PX.Objects.FA.FADepreciationMethodLines | EntityType | FA Depreciation Method Lines | MethodID, Year | 13 | 3 |  | PX_Objects_FA_FADepreciationMethodLines, FADepreciationMethodLines | members-03.md | 6187 | 23 |
| PX.Objects.FA.FADetails | EntityType | FA Details | AssetID | 61 | 8 |  | PX_Objects_FA_FADetails, FADetails | members-03.md | 6211 | 76 |
| PX.Objects.FA.FADetailsTransfer | EntityType | FA Details | AssetID | 1 | 0 | PX.Objects.FA.FADetails | PX_Objects_FA_FADetailsTransfer, FADetails1, FADetailsTransfer | members-03.md | 6288 | 8 |
| PX.Objects.FA.FADisposalMethod | EntityType | FA Disposal Method | DisposalMethodCD | 10 | 5 |  | PX_Objects_FA_FADisposalMethod, FADisposalMethod | members-03.md | 6297 | 21 |
| PX.Objects.FA.FAHistoryByPeriod | EntityType | FA History by Period | AssetID, BookID, FinPeriodID | 4 | 2 |  | PX_Objects_FA_FAHistoryByPeriod, FAHistorybyPeriod | members-03.md | 6319 | 12 |
| PX.Objects.FA.FALocationHistory | EntityType | FA Location History | AssetID, RevisionID | 22 | 20 |  | PX_Objects_FA_FALocationHistory, FALocationHistory | members-03.md | 6332 | 48 |
| PX.Objects.FA.FAOrganizationBook | EntityType | FA Book | BookCode | 5 | 0 | PX.Objects.FA.FABook | PX_Objects_FA_FAOrganizationBook | members-03.md | 6381 | 13 |
| PX.Objects.FA.FAProjectedGLTran | EntityType | FA transactions in GL representation | LineNbr, RefNbr | 6 | 6 |  | PX_Objects_FA_FAProjectedGLTran, FAtransactionsinGLrepresentation, FAProjectedGLTran | members-03.md | 6395 | 18 |
| PX.Objects.FA.FARegister | EntityType | Fixed Asset Transaction | RefNbr | 22 | 5 |  | PX_Objects_FA_FARegister, FixedAssetTransaction, FARegister | members-03.md | 6414 | 34 |
| PX.Objects.FA.FAService | EntityType | FA Service | AssetID, ServiceNumber | 18 | 8 |  | PX_Objects_FA_FAService, FAService | members-03.md | 6449 | 32 |
| PX.Objects.FA.FAServiceSchedule | EntityType | FA Service Schedule | ScheduleCD | 14 | 4 |  | PX_Objects_FA_FAServiceSchedule, FAServiceSchedule | members-03.md | 6482 | 24 |
| PX.Objects.FA.FASetup | EntityType | Fixed Assets Preferences |  | 30 | 10 |  |  | members-03.md | 6507 | 45 |
| PX.Objects.FA.FATran | EntityType | Fixed Asset Transaction | LineNbr, RefNbr | 40 | 14 |  | PX_Objects_FA_FATran, FixedAssetTransaction1, FATran | members-03.md | 6553 | 61 |
| PX.Objects.FA.FAType | EntityType | FA Type | AssetTypeID | 4 | 1 |  | PX_Objects_FA_FAType, FAType | members-03.md | 6615 | 11 |
| PX.Objects.FA.FAUsage | EntityType | FA Usage | AssetID, Number | 17 | 5 |  | PX_Objects_FA_FAUsage, FAUsage | members-03.md | 6627 | 28 |
| PX.Objects.FA.FAUsageSchedule | EntityType | FA Usage Schedule | ScheduleCD | 13 | 4 |  | PX_Objects_FA_FAUsageSchedule, FAUsageSchedule | members-03.md | 6656 | 23 |
| PX.Objects.FA.FixedAsset | EntityType | Fixed Asset | AssetCD | 39 | 43 |  | PX_Objects_FA_FixedAsset, FixedAsset | members-03.md | 6680 | 89 |
| PX.Objects.FA.Overrides.AssetProcess.FABookHist | EntityType | FA Book History | AssetID, BookID, FinPeriodID | 0 | 0 | PX.Objects.FA.FABookHistory | PX_Objects_FA_Overrides_AssetProcess_FABookHist | members-03.md | 6770 | 6 |
| PX.Objects.FA.SplitParams | EntityType | Fixed Asset | AssetCD | 5 | 0 | PX.Objects.FA.FixedAsset | PX_Objects_FA_SplitParams | members-03.md | 6777 | 13 |
| PX.Objects.FA.Standalone.FABookBalance | EntityType |  | AssetID, BookID | 4 | 8 |  | PX_Objects_FA_Standalone_FABookBalance | members-03.md | 6791 | 17 |
| PX.Objects.FA.Standalone.FADetails | EntityType | FA Details | AssetID | 38 | 8 |  | PX_Objects_FA_Standalone_FADetails, FADetails2 | members-03.md | 6809 | 53 |
| PX.Objects.FA.Transact | EntityType | Fixed Asset Transaction | LineNbr, RefNbr | 2 | 0 | PX.Objects.FA.FATran | PX_Objects_FA_Transact | members-03.md | 6863 | 10 |
| PX.Objects.FS.ActiveSchedule | EntityType |  | CustomerID, RefNbr | 3 | 0 | PX.Objects.FS.FSSchedule | PX_Objects_FS_ActiveSchedule | members-03.md | 6874 | 10 |
| PX.Objects.FS.AppointmentBoxComponentField | EntityType |  | ComponentType, FieldName, ObjectName | 0 | 0 | PX.Objects.FS.FSCalendarComponentField | PX_Objects_FS_AppointmentBoxComponentField | members-03.md | 6885 | 5 |
| PX.Objects.FS.AppointmentToPost | EntityType | Appointment | RefNbr, SrvOrdType | 29 | 12 | PX.Objects.FS.FSAppointment | PX_Objects_FS_AppointmentToPost | members-03.md | 6891 | 49 |
| PX.Objects.FS.BAccountLocation | EntityType |  | CustomerID, LocationID | 5 | 22 |  | PX_Objects_FS_BAccountLocation | members-03.md | 6941 | 32 |
| PX.Objects.FS.BAccountSelectorBase | EntityType | Business Account | AcctCD | 0 | 0 | PX.Objects.CR.BAccount | PX_Objects_FS_BAccountSelectorBase | members-03.md | 6974 | 6 |
| PX.Objects.FS.BAccountStaffMember | EntityType | Business Account | AcctCD | 0 | 0 | PX.Objects.FS.BAccountSelectorBase | PX_Objects_FS_BAccountStaffMember | members-03.md | 6981 | 6 |
| PX.Objects.FS.ContractPeriodToPost | EntityType |  | ContractPeriodID, ServiceContractID | 18 | 22 |  | PX_Objects_FS_ContractPeriodToPost | members-03.md | 6988 | 46 |
| PX.Objects.FS.ContractPostBatchDetail | EntityType |  | ContractPostBatchID, ContractPostDocID | 15 | 19 |  | PX_Objects_FS_ContractPostBatchDetail | members-03.md | 7035 | 40 |
| PX.Objects.FS.EPEmployeeFSRouteEmployee | EntityType | Employee | AcctCD | 3 | 1 | PX.Objects.EP.EPEmployee | PX_Objects_FS_EPEmployeeFSRouteEmployee | members-03.md | 7076 | 12 |
| PX.Objects.FS.FSAddress | EntityType | Field Service Address | AddressID | 38 | 9 |  | PX_Objects_FS_FSAddress, FieldServiceAddress, FSAddress | members-03.md | 7089 | 54 |
| PX.Objects.FS.FSAdjust | EntityType |  | AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr | 41 | 6 |  | PX_Objects_FS_FSAdjust | members-03.md | 7144 | 53 |
| PX.Objects.FS.FSAppointment | EntityType | Appointment | RefNbr, SrvOrdType | 160 | 43 |  | PX_Objects_FS_FSAppointment, Appointment, FSAppointment | members-03.md | 7198 | 210 |
| PX.Objects.FS.FSAppointmentDet | EntityType | Appointment Item Detail | LineNbr, RefNbr, SrvOrdType | 110 | 44 |  | PX_Objects_FS_FSAppointmentDet, AppointmentItemDetail, FSAppointmentDet | members-03.md | 7409 | 161 |
| PX.Objects.FS.FSAppointmentDiscountDetail | EntityType |  | EntityType, RefNbr, SrvOrdType | 0 | 0 | PX.Objects.FS.FSDiscountDetail | PX_Objects_FS_FSAppointmentDiscountDetail | members-03.md | 7571 | 5 |
| PX.Objects.FS.FSAppointmentEmployee | EntityType | FSAppointmentEmployee | LineNbr, RefNbr, SrvOrdType | 24 | 13 |  | PX_Objects_FS_FSAppointmentEmployee, FSAppointmentEmployee | members-03.md | 7577 | 44 |
| PX.Objects.FS.FSAppointmentFSServiceOrder | EntityType | Appointment | RefNbr, SrvOrdType | 40 | 12 | PX.Objects.FS.FSAppointment | PX_Objects_FS_FSAppointmentFSServiceOrder | members-03.md | 7622 | 59 |
| PX.Objects.FS.FSAppointmentInRoute | EntityType | Appointment | RefNbr, SrvOrdType | 7 | 3 | PX.Objects.FS.FSAppointment | PX_Objects_FS_FSAppointmentInRoute | members-03.md | 7682 | 17 |
| PX.Objects.FS.FSAppointmentLog | EntityType | Log | LogID | 3 | 0 | PX.Objects.FS.FSLog | PX_Objects_FS_FSAppointmentLog, Log, FSAppointmentLog | members-03.md | 7700 | 11 |
| PX.Objects.FS.FSAppointmentLogExtItemLine | EntityType | Log | LogID | 2 | 9 | PX.Objects.FS.FSAppointmentLog | PX_Objects_FS_FSAppointmentLogExtItemLine | members-03.md | 7712 | 18 |
| PX.Objects.FS.FSAppointmentResource | EntityType |  | RefNbr, SMEquipmentID, SrvOrdType | 14 | 5 |  | PX_Objects_FS_FSAppointmentResource | members-03.md | 7731 | 25 |
| PX.Objects.FS.FSAppointmentScheduleBoard | EntityType |  | RefNbr, SrvOrdType | 52 | 21 |  | PX_Objects_FS_FSAppointmentScheduleBoard | members-03.md | 7757 | 79 |
| PX.Objects.FS.FSAppointmentServiceEmployee | EntityType | Appointment Item Detail | LineNbr, RefNbr, SrvOrdType | 0 | 0 | PX.Objects.FS.FSAppointmentDet | PX_Objects_FS_FSAppointmentServiceEmployee | members-03.md | 7837 | 6 |
| PX.Objects.FS.FSAppointmentStaffDistinct | EntityType |  | BAccountID, RefNbr, SrvOrdType | 5 | 12 |  | PX_Objects_FS_FSAppointmentStaffDistinct | members-03.md | 7844 | 22 |
| PX.Objects.FS.FSAppointmentStaffExtItemLine | EntityType |  | LineNbr, RefNbr, SrvOrdType | 12 | 14 |  | PX_Objects_FS_FSAppointmentStaffExtItemLine | members-03.md | 7867 | 31 |
| PX.Objects.FS.FSAppointmentStaffMember | EntityType | Business Account | AcctCD | 4 | 3 | PX.Objects.FS.BAccountStaffMember | PX_Objects_FS_FSAppointmentStaffMember | members-03.md | 7899 | 14 |
| PX.Objects.FS.FSAppointmentStaffScheduleBoard | EntityType |  | RefNbr, SrvOrdType | 0 | 1 | PX.Objects.FS.FSAppointmentScheduleBoard | PX_Objects_FS_FSAppointmentStaffScheduleBoard | members-03.md | 7914 | 7 |
| PX.Objects.FS.FSAppointmentStatusColor | EntityType | Appointment Status Color | StatusID | 14 | 2 |  | PX_Objects_FS_FSAppointmentStatusColor, AppointmentStatusColor, FSAppointmentStatusColor | members-03.md | 7922 | 22 |
| PX.Objects.FS.FSAppointmentTax | EntityType | Appointment Tax | LineNbr, RefNbr, SrvOrdType, TaxID | 20 | 8 |  | PX_Objects_FS_FSAppointmentTax, AppointmentTax, FSAppointmentTax | members-03.md | 7945 | 35 |
| PX.Objects.FS.FSAppointmentTaxTran | EntityType | Appointment Tax Detail | RecordID, RefNbr, SrvOrdType, TaxID | 24 | 7 |  | PX_Objects_FS_FSAppointmentTaxTran, AppointmentTaxDetail, FSAppointmentTaxTran | members-03.md | 7981 | 38 |
| PX.Objects.FS.FSAppQuickProcessParams | EntityType |  | OrderType | 6 | 0 | PX.Objects.SO.SOQuickProcessParameters | PX_Objects_FS_FSAppQuickProcessParams | members-03.md | 8020 | 13 |
| PX.Objects.FS.FSApptLineSplit | EntityType | Appointment Lot/Serial Detail | ApptNbr, LineNbr, SplitLineNbr, SrvOrdType | 58 | 22 |  | PX_Objects_FS_FSApptLineSplit, AppointmentLotSerialDetail, FSApptLineSplit | members-03.md | 8034 | 87 |
| PX.Objects.FS.FSBillHistory | EntityType | Field Service Billing History | RecordID | 29 | 8 |  | PX_Objects_FS_FSBillHistory, FieldServiceBillingHistory, FSBillHistory | members-03.md | 8122 | 44 |
| PX.Objects.FS.FSBillingCycle | EntityType | Billing Cycle | BillingCycleCD | 19 | 8 |  | PX_Objects_FS_FSBillingCycle, BillingCycle, FSBillingCycle | members-03.md | 8167 | 34 |
| PX.Objects.FS.FSBLOCAddress | EntityType | Field Service Address | AddressID | 0 | 0 | PX.Objects.FS.FSAddress | PX_Objects_FS_FSBLOCAddress | members-03.md | 8202 | 6 |
| PX.Objects.FS.FSBLOCContact | EntityType | Field Service Contact | ContactID | 0 | 0 | PX.Objects.FS.FSContact | PX_Objects_FS_FSBLOCContact | members-03.md | 8209 | 6 |
| PX.Objects.FS.FSBranchLocation | EntityType | Branch Location | BranchLocationCD | 19 | 25 |  | PX_Objects_FS_FSBranchLocation, BranchLocation, FSBranchLocation | members-03.md | 8216 | 51 |
| PX.Objects.FS.FSCalendarComponentField | EntityType |  | ComponentType, FieldName, ObjectName | 14 | 2 |  | PX_Objects_FS_FSCalendarComponentField | members-03.md | 8268 | 22 |
| PX.Objects.FS.FSContact | EntityType | Field Service Contact | ContactID | 34 | 6 |  | PX_Objects_FS_FSContact, FieldServiceContact, FSContact | members-03.md | 8291 | 47 |
| PX.Objects.FS.FSContractAction | EntityType |  | RecordID | 20 | 5 |  | PX_Objects_FS_FSContractAction | members-03.md | 8339 | 30 |
| PX.Objects.FS.FSContractForecast | EntityType |  | ForecastID, ServiceContractID | 13 | 3 |  | PX_Objects_FS_FSContractForecast | members-03.md | 8370 | 21 |
| PX.Objects.FS.FSContractForecastDet | EntityType |  | ForecastID, LineNbr, ServiceContractID | 29 | 8 |  | PX_Objects_FS_FSContractForecastDet | members-03.md | 8392 | 42 |
| PX.Objects.FS.FSContractGenerationHistory | EntityType | Contract Generation History | ContractGenerationHistoryID | 16 | 3 |  | PX_Objects_FS_FSContractGenerationHistory, ContractGenerationHistory, FSContractGenerationHistory | members-03.md | 8435 | 25 |
| PX.Objects.FS.FSContractPeriod | EntityType |  | ContractPeriodID, ServiceContractID | 16 | 5 |  | PX_Objects_FS_FSContractPeriod | members-03.md | 8461 | 27 |
| PX.Objects.FS.FSContractPeriodDet | EntityType | Contract Period Detail | ContractPeriodDetID, ContractPeriodID | 33 | 11 |  | PX_Objects_FS_FSContractPeriodDet, ContractPeriodDetail, FSContractPeriodDet | members-03.md | 8489 | 51 |
| PX.Objects.FS.FSContractPostBatch | EntityType |  | ContractPostBatchNbr | 13 | 4 |  | PX_Objects_FS_FSContractPostBatch | members-03.md | 8541 | 22 |
| PX.Objects.FS.FSContractPostDet | EntityType |  | ContractPostDetID | 16 | 2 |  | PX_Objects_FS_FSContractPostDet | members-03.md | 8564 | 23 |
| PX.Objects.FS.FSContractPostDoc | EntityType |  | ContractPostDocID | 11 | 4 |  | PX_Objects_FS_FSContractPostDoc | members-03.md | 8588 | 20 |
| PX.Objects.FS.FSContractPostRegister | EntityType |  | ContractPeriodID, ServiceContractID | 6 | 0 |  | PX_Objects_FS_FSContractPostRegister | members-03.md | 8609 | 11 |
| PX.Objects.FS.FSContractSchedule | EntityType |  | CustomerID, RefNbr | 1 | 0 | PX.Objects.FS.FSSchedule | PX_Objects_FS_FSContractSchedule | members-03.md | 8621 | 8 |
| PX.Objects.FS.FSCreatedDoc | EntityType |  | RecordID | 9 | 1 |  | PX_Objects_FS_FSCreatedDoc | members-03.md | 8630 | 15 |
| PX.Objects.FS.FSCustomer | EntityType | Customer | AcctCD | 0 | 0 | PX.Objects.AR.Customer | PX_Objects_FS_FSCustomer | members-03.md | 8646 | 6 |
| PX.Objects.FS.FSCustomerBillingSetup | EntityType | FSCustomerBillingSetup | CBID | 17 | 6 |  | PX_Objects_FS_FSCustomerBillingSetup, FSCustomerBillingSetup | members-03.md | 8653 | 29 |
| PX.Objects.FS.FSCustomerClassBillingSetup | EntityType | FSCustomerClassBillingSetup | CBID, CustomerClassID | 14 | 5 |  | PX_Objects_FS_FSCustomerClassBillingSetup, FSCustomerClassBillingSetup | members-03.md | 8683 | 25 |
| PX.Objects.FS.FSDetailFSLogAction | EntityType |  | LineNbr, RefNbr, SrvOrdType | 11 | 10 |  | PX_Objects_FS_FSDetailFSLogAction | members-03.md | 8709 | 26 |
| PX.Objects.FS.FSDiscountDetail | EntityType |  | EntityType, RefNbr, SrvOrdType | 30 | 7 |  | PX_Objects_FS_FSDiscountDetail | members-03.md | 8736 | 43 |
| PX.Objects.FS.FSEmployeeSkill | EntityType |  | EmployeeID, SkillID | 11 | 5 |  | PX_Objects_FS_FSEmployeeSkill | members-03.md | 8780 | 22 |
| PX.Objects.FS.FSEquipment | EntityType | Equipment | RefNbr | 82 | 41 |  | PX_Objects_FS_FSEquipment, Equipment1, FSEquipment | members-03.md | 8803 | 130 |
| PX.Objects.FS.FSEquipmentComponent | EntityType | FSEquipmentComponent | LineNbr, SMEquipmentID | 37 | 20 |  | PX_Objects_FS_FSEquipmentComponent, FSEquipmentComponent | members-03.md | 8934 | 64 |
| PX.Objects.FS.FSEquipmentType | EntityType | Equipment Type | EquipmentTypeCD | 13 | 6 |  | PX_Objects_FS_FSEquipmentType, EquipmentType, FSEquipmentType | members-03.md | 8999 | 26 |
| PX.Objects.FS.FSGenerationLogError | EntityType | Generation Log Error | LogID | 15 | 3 |  | PX_Objects_FS_FSGenerationLogError, GenerationLogError, FSGenerationLogError | members-03.md | 9026 | 24 |
| PX.Objects.FS.FSGeoZone | EntityType | Service Area | GeoZoneCD | 13 | 8 |  | PX_Objects_FS_FSGeoZone, ServiceArea, FSGeoZone | members-03.md | 9051 | 28 |
| PX.Objects.FS.FSGeoZoneEmp | EntityType | Service Area - Employee | EmployeeID, GeoZoneID | 11 | 6 |  | PX_Objects_FS_FSGeoZoneEmp, ServiceAreaEmployee, FSGeoZoneEmp | members-03.md | 9080 | 24 |
| PX.Objects.FS.FSGeoZonePostalCode | EntityType | Service Area - Postal Code | GeoZoneID, PostalCode | 10 | 4 |  | PX_Objects_FS_FSGeoZonePostalCode, ServiceAreaPostalCode, FSGeoZonePostalCode | members-03.md | 9105 | 20 |
| PX.Objects.FS.FSGPSTrackingLocation | EntityType |  | RequestID | 1 | 0 | PX.FS.FSGPSTrackingRequest | PX_Objects_FS_FSGPSTrackingLocation | members-03.md | 9126 | 8 |
| PX.Objects.FS.FSLicense | EntityType | License | RefNbr | 17 | 6 |  | PX_Objects_FS_FSLicense, License, FSLicense | members-03.md | 9135 | 30 |
| PX.Objects.FS.FSLicenseType | EntityType | License Type | LicenseTypeCD | 13 | 5 |  | PX_Objects_FS_FSLicenseType, LicenseType, FSLicenseType | members-03.md | 9166 | 25 |
| PX.Objects.FS.FSLog | EntityType | Log | LogID | 46 | 16 |  | PX_Objects_FS_FSLog, Log1, FSLog | members-03.md | 9192 | 69 |
| PX.Objects.FS.FSManufacturer | EntityType | Manufacturer | ManufacturerCD | 19 | 7 |  | PX_Objects_FS_FSManufacturer, Manufacturer, FSManufacturer | members-03.md | 9262 | 33 |
| PX.Objects.FS.FSManufacturerModel | EntityType | Manufacturer Model | ManufacturerID, ManufacturerModelCD | 15 | 5 |  | PX_Objects_FS_FSManufacturerModel, ManufacturerModel, FSManufacturerModel | members-03.md | 9296 | 27 |
| PX.Objects.FS.FSMasterContract | EntityType |  | MasterContractCD | 14 | 5 |  | PX_Objects_FS_FSMasterContract | members-03.md | 9324 | 25 |
| PX.Objects.FS.FSModelComponent | EntityType | Model Warranty | ComponentID, ModelID | 23 | 7 |  | PX_Objects_FS_FSModelComponent, ModelWarranty, FSModelComponent | members-03.md | 9350 | 37 |
| PX.Objects.FS.FSModelTemplateComponent | EntityType | Model Template Component | ComponentCD, ModelTemplateID | 17 | 9 |  | PX_Objects_FS_FSModelTemplateComponent, ModelTemplateComponent, FSModelTemplateComponent | members-03.md | 9388 | 33 |
| PX.Objects.FS.FSPostBatch | EntityType | Field Service Billing Batch | BatchNbr | 17 | 5 |  | PX_Objects_FS_FSPostBatch, FieldServiceBillingBatch, FSPostBatch | members-03.md | 9422 | 28 |
| PX.Objects.FS.FSPostDet | EntityType |  | BatchID, PostDetID | 41 | 15 |  | PX_Objects_FS_FSPostDet | members-03.md | 9451 | 62 |
| PX.Objects.FS.FSPostDoc | EntityType |  | RecordID | 20 | 3 |  | PX_Objects_FS_FSPostDoc | members-03.md | 9514 | 29 |
| PX.Objects.FS.FSPostInfo | EntityType | FSPostInfo | PostID | 35 | 18 |  | PX_Objects_FS_FSPostInfo, FSPostInfo | members-03.md | 9544 | 60 |
| PX.Objects.FS.FSPostRegister | EntityType |  | EntityType, PostedTO, RefNbr, SrvOrdType | 9 | 0 |  | PX_Objects_FS_FSPostRegister | members-03.md | 9605 | 14 |
| PX.Objects.FS.FSProblem | EntityType | Problem | ProblemCD | 12 | 6 |  | PX_Objects_FS_FSProblem, Problem, FSProblem | members-03.md | 9620 | 25 |
| PX.Objects.FS.FSProcessIdentity | EntityType |  | ProcessID | 11 | 2 |  | PX_Objects_FS_FSProcessIdentity | members-03.md | 9646 | 18 |
| PX.Objects.FS.FSQuickProcessParameters | EntityType |  | SrvOrdType | 16 | 1 |  | PX_Objects_FS_FSQuickProcessParameters | members-03.md | 9665 | 23 |
| PX.Objects.FS.FSRoom | EntityType | Room | BranchLocationID, RecordID | 16 | 8 |  | PX_Objects_FS_FSRoom, Room, FSRoom | members-03.md | 9689 | 31 |
| PX.Objects.FS.FSRoute | EntityType | Route | RouteCD | 52 | 16 |  | PX_Objects_FS_FSRoute, Route, FSRoute | members-03.md | 9721 | 75 |
| PX.Objects.FS.FSRouteAppointmentForecasting | EntityType |  | ScheduleID, StartDate | 6 | 7 |  | PX_Objects_FS_FSRouteAppointmentForecasting | members-03.md | 9797 | 18 |
| PX.Objects.FS.FSRouteContractSchedule | EntityType |  | CustomerID, RefNbr | 1 | 0 | PX.Objects.FS.FSSchedule | PX_Objects_FS_FSRouteContractSchedule | members-03.md | 9816 | 8 |
| PX.Objects.FS.FSRouteContractScheduleFSServiceContract | EntityType |  | CustomerID, RefNbr | 3 | 1 | PX.Objects.FS.FSRouteContractSchedule | PX_Objects_FS_FSRouteContractScheduleFSServiceContract | members-03.md | 9825 | 10 |
| PX.Objects.FS.FSRouteDocument | EntityType | Route Document | RefNbr | 59 | 11 |  | PX_Objects_FS_FSRouteDocument, RouteDocument, FSRouteDocument | members-03.md | 9836 | 77 |
| PX.Objects.FS.FSRouteEmployee | EntityType |  | EmployeeID, RouteID | 10 | 4 |  | PX_Objects_FS_FSRouteEmployee | members-03.md | 9914 | 19 |
| PX.Objects.FS.FSRouteSetup | EntityType | Route Management Preferences |  | 16 | 4 |  |  | members-03.md | 9934 | 25 |
| PX.Objects.FS.FSSalesPrice | EntityType |  | InventoryID, ServiceContractID, UOM | 16 | 4 |  | PX_Objects_FS_FSSalesPrice | members-03.md | 9960 | 26 |
| PX.Objects.FS.FSSchedule | EntityType |  | CustomerID, RefNbr | 115 | 26 |  | PX_Objects_FS_FSSchedule | members-03.md | 9987 | 147 |
| PX.Objects.FS.FSScheduleDet | EntityType | FSScheduleDet | LineNbr, ScheduleID | 24 | 16 |  | PX_Objects_FS_FSScheduleDet, FSScheduleDet | members-03.md | 10135 | 47 |
| PX.Objects.FS.FSScheduleRoute | EntityType | FSScheduleRoute | ScheduleID | 29 | 11 |  | PX_Objects_FS_FSScheduleRoute, FSScheduleRoute | members-03.md | 10183 | 47 |
| PX.Objects.FS.FSServiceContract | EntityType | Service Contract | RefNbr | 53 | 32 |  | PX_Objects_FS_FSServiceContract, ServiceContract, FSServiceContract | members-03.md | 10231 | 92 |
| PX.Objects.FS.FSServiceEquipmentType | EntityType |  | EquipmentTypeID, ServiceID | 9 | 4 |  | PX_Objects_FS_FSServiceEquipmentType | members-03.md | 10324 | 18 |
| PX.Objects.FS.FSServiceInventoryItem | EntityType |  | InventoryID, ServiceID | 9 | 4 |  | PX_Objects_FS_FSServiceInventoryItem | members-03.md | 10343 | 18 |
| PX.Objects.FS.FSServiceLicenseType | EntityType | Service - License Type | LicenseTypeID, ServiceID | 9 | 4 |  | PX_Objects_FS_FSServiceLicenseType, ServiceLicenseType, FSServiceLicenseType | members-03.md | 10362 | 19 |
| PX.Objects.FS.FSServiceOrder | EntityType | Service Order | RefNbr, SrvOrdType | 174 | 56 |  | PX_Objects_FS_FSServiceOrder, ServiceOrder, FSServiceOrder | members-03.md | 10382 | 237 |
| PX.Objects.FS.FSServiceOrderDiscountDetail | EntityType |  | EntityType, RefNbr, SrvOrdType | 0 | 0 | PX.Objects.FS.FSDiscountDetail | PX_Objects_FS_FSServiceOrderDiscountDetail | members-03.md | 10620 | 5 |
| PX.Objects.FS.FSServiceOrderTax | EntityType | Service Order Tax | LineNbr, RefNbr, SrvOrdType, TaxID | 20 | 8 |  | PX_Objects_FS_FSServiceOrderTax, ServiceOrderTax, FSServiceOrderTax | members-03.md | 10626 | 35 |
| PX.Objects.FS.FSServiceOrderTaxTran | EntityType | Service Order Tax Detail | RecordID, RefNbr, SrvOrdType, TaxID | 24 | 7 |  | PX_Objects_FS_FSServiceOrderTaxTran, ServiceOrderTaxDetail, FSServiceOrderTaxTran | members-03.md | 10662 | 38 |
| PX.Objects.FS.FSServiceSkill | EntityType |  | ServiceID, SkillID | 9 | 4 |  | PX_Objects_FS_FSServiceSkill | members-03.md | 10701 | 18 |
| PX.Objects.FS.FSServiceTemplate | EntityType |  | ServiceTemplateCD | 13 | 5 |  | PX_Objects_FS_FSServiceTemplate | members-03.md | 10720 | 24 |
| PX.Objects.FS.FSServiceTemplateDet | EntityType | FSServiceTemplateDet | ServiceTemplateDetID, ServiceTemplateID | 14 | 5 |  | PX_Objects_FS_FSServiceTemplateDet, FSServiceTemplateDet | members-03.md | 10745 | 25 |
| PX.Objects.FS.FSServiceVehicleType | EntityType |  | ServiceID, VehicleTypeID | 10 | 4 |  | PX_Objects_FS_FSServiceVehicleType | members-03.md | 10771 | 19 |
| PX.Objects.FS.FSSetup | EntityType | Service Management Preferences |  | 70 | 5 |  |  | members-03.md | 10791 | 80 |
| PX.Objects.FS.FSShippingAddress | EntityType | Field Service Shipping Address | AddressID | 0 | 0 | PX.Objects.FS.FSAddress | PX_Objects_FS_FSShippingAddress, FieldServiceShippingAddress, FSShippingAddress | members-03.md | 10872 | 6 |
| PX.Objects.FS.FSShippingContact | EntityType | Field Service Shipping Contact | ContactID | 0 | 0 | PX.Objects.FS.FSContact | PX_Objects_FS_FSShippingContact, FieldServiceShippingContact, FSShippingContact | members-03.md | 10879 | 6 |
| PX.Objects.FS.FSSiteStatusSelected | EntityType |  | InventoryID | 42 | 8 |  | PX_Objects_FS_FSSiteStatusSelected | members-03.md | 10886 | 56 |
| PX.Objects.FS.FSSkill | EntityType | Skill | SkillCD | 14 | 6 |  | PX_Objects_FS_FSSkill, Skill, FSSkill | members-03.md | 10943 | 27 |
| PX.Objects.FS.FSSODet | EntityType | Service Order Item Detail | LineNbr, RefNbr, SrvOrdType | 116 | 48 |  | PX_Objects_FS_FSSODet, ServiceOrderItemDetail, FSSODet | members-03.md | 10971 | 171 |
| PX.Objects.FS.FSSODetEmployee | EntityType | Service Order Item Detail | LineNbr, RefNbr, SrvOrdType | 0 | 0 | PX.Objects.FS.FSSODet | PX_Objects_FS_FSSODetEmployee | members-03.md | 11143 | 6 |
| PX.Objects.FS.FSSODetFSSODetSplit | EntityType |  | LineNbr, RefNbr, SplitLineNbr, SrvOrdType | 11 | 13 |  | PX_Objects_FS_FSSODetFSSODetSplit | members-03.md | 11150 | 29 |
| PX.Objects.FS.FSSODetSplit | EntityType | Service Order Lot/Serial Detail | LineNbr, RefNbr, SplitLineNbr, SrvOrdType | 73 | 32 |  | PX_Objects_FS_FSSODetSplit, ServiceOrderLotSerialDetail, FSSODetSplit | members-03.md | 11180 | 112 |
| PX.Objects.FS.FSSOEmployee | EntityType | FSSOEmployee | LineNbr, RefNbr, SrvOrdType | 24 | 6 |  | PX_Objects_FS_FSSOEmployee, FSSOEmployee | members-03.md | 11293 | 37 |
| PX.Objects.FS.FSSOResource | EntityType | FSSOResource | RefNbr, SMEquipmentID, SrvOrdType | 13 | 5 |  | PX_Objects_FS_FSSOResource, FSSOResource | members-03.md | 11331 | 24 |
| PX.Objects.FS.FSSrvOrdQuickProcessParams | EntityType |  | OrderType | 7 | 0 | PX.Objects.SO.SOQuickProcessParameters | PX_Objects_FS_FSSrvOrdQuickProcessParams | members-03.md | 11356 | 14 |
| PX.Objects.FS.FSSrvOrdType | EntityType | Order Type | SrvOrdType | 78 | 49 |  | PX_Objects_FS_FSSrvOrdType, OrderType, FSSrvOrdType | members-03.md | 11371 | 134 |
| PX.Objects.FS.FSSrvOrdTypeProblem | EntityType |  | ProblemID, SrvOrdType | 9 | 4 |  | PX_Objects_FS_FSSrvOrdTypeProblem | members-03.md | 11506 | 18 |
| PX.Objects.FS.FSStaffSchedule | EntityType |  | CustomerID, RefNbr | 3 | 0 | PX.Objects.FS.FSSchedule | PX_Objects_FS_FSStaffSchedule | members-03.md | 11525 | 9 |
| PX.Objects.FS.FSTimeSlot | EntityType |  | TimeSlotID | 30 | 3 |  | PX_Objects_FS_FSTimeSlot | members-03.md | 11535 | 39 |
| PX.Objects.FS.FSVehicle | EntityType | Equipment | RefNbr | 1 | 0 | PX.Objects.FS.FSEquipment | PX_Objects_FS_FSVehicle | members-03.md | 11575 | 8 |
| PX.Objects.FS.FSVehicleType | EntityType | Vehicle Type | VehicleTypeCD | 13 | 6 |  | PX_Objects_FS_FSVehicleType, VehicleType, FSVehicleType | members-03.md | 11584 | 26 |
| PX.Objects.FS.FSWeekCodeDate | EntityType | Contracts/Routes calendar Week Code | WeekCodeDate | 16 | 2 |  | PX_Objects_FS_FSWeekCodeDate, ContractsRoutescalendarWeekCode, FSWeekCodeDate | members-03.md | 11611 | 24 |
| PX.Objects.FS.FSWFStage | EntityType | Order Stage | ParentWFStageID, WFID, WFStageCD | 23 | 6 |  | PX_Objects_FS_FSWFStage, OrderStage, FSWFStage | members-03.md | 11636 | 36 |
| PX.Objects.FS.FSWrkProcess | EntityType | FSWrkProcess | ProcessID | 22 | 10 |  | PX_Objects_FS_FSWrkProcess, FSWrkProcess | members-03.md | 11673 | 38 |
| PX.Objects.FS.InventoryPostingBatchDetail | EntityType |  | AppointmentRefNbr, BatchID, SrvOrdType | 3 | 4 | PX.Objects.FS.PostingBatchDetail | PX_Objects_FS_InventoryPostingBatchDetail | members-03.md | 11712 | 13 |
| PX.Objects.FS.LicenseTypeGridFilter | EntityType | License Type | LicenseTypeCD | 0 | 0 | PX.Objects.FS.FSLicenseType | PX_Objects_FS_LicenseTypeGridFilter | members-03.md | 11726 | 6 |
| PX.Objects.FS.POEnabledFSSODet | EntityType | Service Order Item Detail | LineNbr, RefNbr, SrvOrdType | 8 | 7 | PX.Objects.FS.FSSODet | PX_Objects_FS_POEnabledFSSODet | members-03.md | 11733 | 23 |
| PX.Objects.FS.PostingBatchDetail | EntityType |  | AppointmentRefNbr, BatchID, SrvOrdType | 43 | 22 |  | PX_Objects_FS_PostingBatchDetail | members-03.md | 11757 | 71 |
| PX.Objects.FS.RelatedServiceOrder | EntityType | Service Order | RefNbr, SrvOrdType | 0 | 0 | PX.Objects.FS.FSServiceOrder | PX_Objects_FS_RelatedServiceOrder | members-03.md | 11829 | 6 |
| PX.Objects.FS.RouteAppointmentInfo | EntityType | Appointment | RefNbr, SrvOrdType | 17 | 16 | PX.Objects.FS.FSAppointment | PX_Objects_FS_RouteAppointmentInfo | members-03.md | 11836 | 40 |
| PX.Objects.FS.SchedulerAppointment | EntityType | Appointment | RefNbr, SrvOrdType | 24 | 23 |  | PX_Objects_FS_SchedulerAppointment, Appointment1, SchedulerAppointment | members-03.md | 11877 | 54 |
| PX.Objects.FS.SchedulerEmployeeInventoryItem | EntityType | Employee Inventory Item | InventoryID | 4 | 265 |  | PX_Objects_FS_SchedulerEmployeeInventoryItem, EmployeeInventoryItem, SchedulerEmployeeInventoryItem | members-03.md | 11932 | 275 |
| PX.Objects.FS.SchedulerServiceOrder | EntityType | Service Order | BranchCD, BranchLocationCD, CustomerAcctCD, ProblemCD, ServiceContractRefNbr, SrvOrdType | 52 | 46 |  | PX_Objects_FS_SchedulerServiceOrder, ServiceOrder1, SchedulerServiceOrder | members-03.md | 12208 | 105 |
| PX.Objects.FS.ServiceOrderComponentField | EntityType |  | ComponentType, FieldName, ObjectName | 0 | 0 | PX.Objects.FS.FSCalendarComponentField | PX_Objects_FS_ServiceOrderComponentField | members-03.md | 12314 | 5 |
| PX.Objects.FS.ServiceOrderToPost | EntityType | Service Order | RefNbr, SrvOrdType | 23 | 9 | PX.Objects.FS.FSServiceOrder | PX_Objects_FS_ServiceOrderToPost | members-03.md | 12320 | 40 |
| PX.Objects.FS.SkillGridFilter | EntityType | Skill | SkillCD | 0 | 0 | PX.Objects.FS.FSSkill | PX_Objects_FS_SkillGridFilter | members-03.md | 12361 | 6 |
| PX.Objects.FS.SoldInventoryItem | EntityType |  | DocType, InvoiceLineNbr, InvoiceRefNbr, SOLineSplitNumber | 17 | 266 |  | PX_Objects_FS_SoldInventoryItem | members-03.md | 12368 | 288 |
| PX.Objects.FS.SOOrderTypeQuickProcess | EntityType | Order Type | OrderType | 0 | 0 | PX.Objects.SO.SOOrderType | PX_Objects_FS_SOOrderTypeQuickProcess | members-03.md | 12657 | 6 |
| PX.Objects.FS.UnassignedAppComponentField | EntityType |  | ComponentType, FieldName, ObjectName | 0 | 0 | PX.Objects.FS.FSCalendarComponentField | PX_Objects_FS_UnassignedAppComponentField | members-03.md | 12664 | 5 |
| PX.Objects.GDPR.SMPersonalDataLog | EntityType |  | LogID | 6 | 1 |  | PX_Objects_GDPR_SMPersonalDataLog | members-03.md | 12670 | 13 |
| PX.Objects.GL.Account | EntityType | GL Account | AccountCD | 36 | 176 |  | PX_Objects_GL_Account, GLAccount, Account | members-03.md | 12684 | 219 |
| PX.Objects.GL.AccountClass | EntityType | GL Account Class | AccountClassID | 12 | 4 |  | PX_Objects_GL_AccountClass, GLAccountClass, AccountClass | members-03.md | 12904 | 23 |
| PX.Objects.GL.AdjustedBranch | EntityType | Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_AdjustedBranch | members-03.md | 12928 | 6 |
| PX.Objects.GL.AdjustingBranch | EntityType | Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_AdjustingBranch | members-03.md | 12935 | 6 |
| PX.Objects.GL.ADL.Account | EntityType |  |  | 8 | 176 |  |  | members-03.md | 12942 | 188 |
| PX.Objects.GL.ADL.Batch | EntityType |  | BatchNbr, Module | 9 | 45 |  | PX_Objects_GL_ADL_Batch | members-03.md | 13131 | 60 |
| PX.Objects.GL.ADL.Sub | EntityType |  | SubCD | 4 | 165 |  | PX_Objects_GL_ADL_Sub | members-03.md | 13192 | 175 |
| PX.Objects.GL.Batch | EntityType | GL Batch | BatchNbr, Module | 56 | 45 |  | PX_Objects_GL_Batch, GLBatch, Batch | members-03.md | 13368 | 108 |
| PX.Objects.GL.BatchPostedForModule | EntityType | GL Batch | BatchNbr, Module | 0 | 0 | PX.Objects.GL.Batch | PX_Objects_GL_BatchPostedForModule | members-03.md | 13477 | 6 |
| PX.Objects.GL.BatchReport | EntityType | GL Batch | BatchNbr, Module | 0 | 0 | PX.Objects.GL.Batch | PX_Objects_GL_BatchReport | members-03.md | 13484 | 6 |
| PX.Objects.GL.Branch | EntityType | Branch | BranchCD | 34 | 221 |  | PX_Objects_GL_Branch, Branch | members-03.md | 13491 | 262 |
| PX.Objects.GL.BranchAcctMapFrom | EntityType | Branch Account Map From | BranchID, LineNbr | 6 | 7 |  | PX_Objects_GL_BranchAcctMapFrom, BranchAccountMapFrom, BranchAcctMapFrom | members-03.md | 13754 | 19 |
| PX.Objects.GL.BranchAcctMapTo | EntityType | Branch Account Map To | BranchID, LineNbr | 6 | 7 |  | PX_Objects_GL_BranchAcctMapTo, BranchAccountMapTo, BranchAcctMapTo | members-03.md | 13774 | 19 |
| PX.Objects.GL.CAExpenseBranch | EntityType | Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_CAExpenseBranch | members-03.md | 13794 | 6 |
| PX.Objects.GL.CashAccountBranch | EntityType | Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_CashAccountBranch | members-04.md | 3 | 6 |
| PX.Objects.GL.CASplitBranch | EntityType | Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_CASplitBranch | members-04.md | 10 | 6 |
| PX.Objects.GL.Company | EntityType | Company |  | 4 | 2 |  |  | members-04.md | 17 | 11 |
| PX.Objects.GL.CurrentBranch | EntityType | Current Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_CurrentBranch, CurrentBranch | members-04.md | 29 | 6 |
| PX.Objects.GL.DAC.Organization | EntityType | Company | OrganizationCD | 47 | 38 |  | PX_Objects_GL_DAC_Organization, Company2, Organization | members-04.md | 36 | 92 |
| PX.Objects.GL.DAC.OrganizationLedgerLink | EntityType |  | LedgerID, OrganizationID | 2 | 2 |  | PX_Objects_GL_DAC_OrganizationLedgerLink | members-04.md | 129 | 9 |
| PX.Objects.GL.DAC.Standalone.OrganizationAlias | EntityType | Company | OrganizationCD | 0 | 0 | PX.Objects.GL.DAC.Organization | PX_Objects_GL_DAC_Standalone_OrganizationAlias, Company3, OrganizationAlias | members-04.md | 139 | 6 |
| PX.Objects.GL.FinPeriods.MasterFinPeriod | EntityType |  | FinPeriodID | 30 | 6 |  | PX_Objects_GL_FinPeriods_MasterFinPeriod | members-04.md | 146 | 42 |
| PX.Objects.GL.FinPeriods.MasterFinYear | EntityType |  | Year | 16 | 4 |  | PX_Objects_GL_FinPeriods_MasterFinYear | members-04.md | 189 | 25 |
| PX.Objects.GL.FinPeriods.MasterPrevFinPeriodCurrent | ComplexType |  |  | 1 | 0 |  |  | members-04.md | 215 | 4 |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriod | EntityType |  | FinPeriodID, OrganizationID | 31 | 3 |  | PX_Objects_GL_FinPeriods_OrganizationFinPeriod | members-04.md | 220 | 40 |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodAlias | EntityType |  | FinPeriodID, OrganizationID | 0 | 0 | PX.Objects.GL.FinPeriods.OrganizationFinPeriod | PX_Objects_GL_FinPeriods_OrganizationFinPeriodAlias | members-04.md | 261 | 5 |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodCurrent | EntityType | Last FinPeriod Current | FinPeriodID, OrganizationID, PrevFinPeriodID | 4 | 1 |  | PX_Objects_GL_FinPeriods_OrganizationFinPeriodCurrent, LastFinPeriodCurrent, OrganizationFinPeriodCurrent | members-04.md | 267 | 11 |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodExt | EntityType | Last FinPeriod | FinPeriodID, OrganizationID, PrevFinPeriodID | 4 | 1 |  | PX_Objects_GL_FinPeriods_OrganizationFinPeriodExt, LastFinPeriod, OrganizationFinPeriodExt | members-04.md | 279 | 11 |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodMin | EntityType | Min FinPeriod Current | FinPeriodID, OrganizationID | 2 | 1 |  | PX_Objects_GL_FinPeriods_OrganizationFinPeriodMin, MinFinPeriodCurrent, OrganizationFinPeriodMin | members-04.md | 291 | 9 |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodStatus | EntityType |  | FinPeriodID, OrganizationID | 0 | 0 | PX.Objects.GL.FinPeriods.OrganizationFinPeriod | PX_Objects_GL_FinPeriods_OrganizationFinPeriodStatus | members-04.md | 301 | 5 |
| PX.Objects.GL.FinPeriods.OrganizationFinYear | EntityType | Company Financial Period | OrganizationID, Year | 14 | 3 |  | PX_Objects_GL_FinPeriods_OrganizationFinYear, CompanyFinancialPeriod, OrganizationFinYear | members-04.md | 307 | 23 |
| PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod | EntityType | Financial Period | FinPeriodID, OrganizationID | 32 | 5 |  | PX_Objects_GL_FinPeriods_TableDefinition_FinPeriod, FinancialPeriod, FinPeriod | members-04.md | 331 | 44 |
| PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod2 | EntityType | Financial Period | FinPeriodID, OrganizationID | 0 | 0 | PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod | PX_Objects_GL_FinPeriods_TableDefinition_FinPeriod2 | members-04.md | 376 | 6 |
| PX.Objects.GL.FinPeriods.TableDefinition.FinYear | EntityType |  | OrganizationID, Year | 18 | 4 |  | PX_Objects_GL_FinPeriods_TableDefinition_FinYear | members-04.md | 383 | 28 |
| PX.Objects.GL.FinPeriodSetup | EntityType | Financial Period Template | PeriodNbr | 15 | 2 |  | PX_Objects_GL_FinPeriodSetup, FinancialPeriodTemplate, FinPeriodSetup | members-04.md | 412 | 24 |
| PX.Objects.GL.FinYearSetup | EntityType | Financial Year |  | 19 | 2 |  |  | members-04.md | 437 | 26 |
| PX.Objects.GL.GLAllocation | EntityType | Allocation | GLAllocationID | 25 | 9 |  | PX_Objects_GL_GLAllocation, Allocation, GLAllocation | members-04.md | 464 | 41 |
| PX.Objects.GL.GLAllocationAccountHistory | EntityType | GL Allocation History for Account | AccountID, BatchNbr, BranchID, Module, SubID | 10 | 8 |  | PX_Objects_GL_GLAllocationAccountHistory, GLAllocationHistoryforAccount, GLAllocationAccountHistory | members-04.md | 506 | 24 |
| PX.Objects.GL.GLAllocationDestination | EntityType | GL Allocation Destination | GLAllocationID, LineID | 11 | 9 |  | PX_Objects_GL_GLAllocationDestination, GLAllocationDestination | members-04.md | 531 | 26 |
| PX.Objects.GL.GLAllocationHistory | EntityType | GL Allocation History | BatchNbr, GLAllocationID, Module | 3 | 3 |  | PX_Objects_GL_GLAllocationHistory, GLAllocationHistory | members-04.md | 558 | 12 |
| PX.Objects.GL.GLAllocationSource | EntityType | GL Allocation Source | GLAllocationID, LineID | 12 | 8 |  | PX_Objects_GL_GLAllocationSource, GLAllocationSource | members-04.md | 571 | 26 |
| PX.Objects.GL.GLBudget | EntityType | Budget | BranchID, FinYear, LedgerID | 10 | 4 |  | PX_Objects_GL_GLBudget, Budget, GLBudget | members-04.md | 598 | 20 |
| PX.Objects.GL.GLBudgetLine | EntityType | Budget Article | BranchID, FinYear, GroupID, LedgerID | 30 | 7 |  | PX_Objects_GL_GLBudgetLine, BudgetArticle, GLBudgetLine | members-04.md | 619 | 44 |
| PX.Objects.GL.GLBudgetLineDetail | EntityType | GL Budget Line Detail | BranchID, FinPeriodID, FinYear, GroupID, LedgerID | 15 | 7 |  | PX_Objects_GL_GLBudgetLineDetail, GLBudgetLineDetail | members-04.md | 664 | 28 |
| PX.Objects.GL.GLBudgetTree | EntityType | GL Budget Tree | GroupID | 17 | 6 |  | PX_Objects_GL_GLBudgetTree, GLBudgetTree | members-04.md | 693 | 30 |
| PX.Objects.GL.GLConsolAccount | EntityType | GL Consolidation Account | AccountCD | 2 | 1 |  | PX_Objects_GL_GLConsolAccount, GLConsolidationAccount, GLConsolAccount | members-04.md | 724 | 9 |
| PX.Objects.GL.GLConsolBranch | EntityType | GL Consolidation Branch | BranchCD, SetupID | 7 | 1 |  | PX_Objects_GL_GLConsolBranch, GLConsolidationBranch, GLConsolBranch | members-04.md | 734 | 15 |
| PX.Objects.GL.GLConsolData | EntityType | GL Consolidation Data | AccountCD, FinPeriodID, MappedValue | 6 | 0 |  | PX_Objects_GL_GLConsolData, GLConsolidationData, GLConsolData | members-04.md | 750 | 13 |
| PX.Objects.GL.GLConsolLedger | EntityType | GL Consolidation Ledger | LedgerCD, SetupID | 5 | 1 |  | PX_Objects_GL_GLConsolLedger, GLConsolidationLedger, GLConsolLedger | members-04.md | 764 | 12 |
| PX.Objects.GL.GLConsolLedger2 | EntityType |  | LedgerCD, SetupID | 3 | 1 |  | PX_Objects_GL_GLConsolLedger2 | members-04.md | 777 | 9 |
| PX.Objects.GL.GLConsolSetup | EntityType | GL Consolidation Setup | SetupID | 18 | 5 |  | PX_Objects_GL_GLConsolSetup, GLConsolidationSetup, GLConsolSetup | members-04.md | 787 | 29 |
| PX.Objects.GL.GLDocBatch | EntityType | GL Document Batch | BatchNbr, Module | 35 | 9 |  | PX_Objects_GL_GLDocBatch, GLDocumentBatch, GLDocBatch | members-04.md | 817 | 51 |
| PX.Objects.GL.GLHistory | EntityType | GL History | AccountID, BranchID, FinPeriodID, LedgerID, SubID | 41 | 5 |  | PX_Objects_GL_GLHistory, GLHistory | members-04.md | 869 | 53 |
| PX.Objects.GL.GLHistoryByCurrentPeriod | EntityType | GL History by Period | AccountID, BranchID, FinPeriodID, LedgerID, SubID | 7 | 4 |  | PX_Objects_GL_GLHistoryByCurrentPeriod, GLHistorybyPeriod1, GLHistoryByCurrentPeriod | members-04.md | 923 | 18 |
| PX.Objects.GL.GLHistoryByPeriod | EntityType | GL History by Period | AccountID, BranchID, FinPeriodID, LedgerID, SubID | 8 | 4 |  | PX_Objects_GL_GLHistoryByPeriod, GLHistorybyPeriod2 | members-04.md | 942 | 19 |
| PX.Objects.GL.GLHistoryByPeriodCurrent | EntityType | GL History by Period | AccountID, BranchID, FinPeriodID, LedgerID, SubID | 7 | 2 |  | PX_Objects_GL_GLHistoryByPeriodCurrent, GLHistorybyPeriod3, GLHistoryByPeriodCurrent | members-04.md | 962 | 16 |
| PX.Objects.GL.GLHistoryByPeriodMasterCurrent | EntityType | GL History by Period | AccountID, BranchID, FinPeriodID, LedgerID, SubID | 7 | 2 |  | PX_Objects_GL_GLHistoryByPeriodMasterCurrent, GLHistorybyPeriod4, GLHistoryByPeriodMasterCurrent | members-04.md | 979 | 16 |
| PX.Objects.GL.GLHistoryLastRevaluation | EntityType |  | AccountID, BranchID, LedgerID, SubID | 5 | 4 |  | PX_Objects_GL_GLHistoryLastRevaluation | members-04.md | 996 | 14 |
| PX.Objects.GL.GLHistorySummary | EntityType | GLHistory Summary | AccountID, BranchID, LedgerID, SubID | 4 | 4 |  | PX_Objects_GL_GLHistorySummary, GLHistorySummary | members-04.md | 1011 | 14 |
| PX.Objects.GL.GLSetup | EntityType | General Ledger Preferences |  | 28 | 11 |  |  | members-04.md | 1026 | 44 |
| PX.Objects.GL.GLSetupApproval | EntityType | GL Approval Preferences | ApprovalID | 12 | 4 |  | PX_Objects_GL_GLSetupApproval, GLApprovalPreferences, GLSetupApproval | members-04.md | 1071 | 22 |
| PX.Objects.GL.GLTax | EntityType | GL Tax Detail | BatchNbr, DetailType, LineNbr, Module, TaxID | 24 | 7 |  | PX_Objects_GL_GLTax, GLTaxDetail, GLTax | members-04.md | 1094 | 38 |
| PX.Objects.GL.GLTaxTran | EntityType | GL Tax Transaction | BatchNbr, DetailType, LineNbr, Module, TaxID | 0 | 0 | PX.Objects.GL.GLTax | PX_Objects_GL_GLTaxTran, GLTaxTransaction, GLTaxTran | members-04.md | 1133 | 6 |
| PX.Objects.GL.GLTran | EntityType | GL Transaction | BatchNbr, LineNbr, Module | 73 | 22 |  | PX_Objects_GL_GLTran, GLTransaction, GLTran | members-04.md | 1140 | 102 |
| PX.Objects.GL.GLTranCode | EntityType | GL Transaction Code | Module, TranType | 5 | 1 |  | PX_Objects_GL_GLTranCode, GLTransactionCode, GLTranCode | members-04.md | 1243 | 12 |
| PX.Objects.GL.GLTranDoc | EntityType | Journal Voucher | BatchNbr, LineNbr, Module | 88 | 43 |  | PX_Objects_GL_GLTranDoc, JournalVoucher, GLTranDoc | members-04.md | 1256 | 138 |
| PX.Objects.GL.GLTranR | EntityType | GL Transaction | BatchNbr, LineNbr, Module | 11 | 0 | PX.Objects.GL.GLTran | PX_Objects_GL_GLTranR | members-04.md | 1395 | 19 |
| PX.Objects.GL.GLTrialBalanceImportDetails | EntityType | Trial Balance Import Details | Line, MapNumber | 18 | 9 |  | PX_Objects_GL_GLTrialBalanceImportDetails, TrialBalanceImportDetails, GLTrialBalanceImportDetails | members-04.md | 1415 | 34 |
| PX.Objects.GL.GLTrialBalanceImportMap | EntityType | Trial Balance Import | Number | 27 | 6 |  | PX_Objects_GL_GLTrialBalanceImportMap, TrialBalanceImport, GLTrialBalanceImportMap | members-04.md | 1450 | 40 |
| PX.Objects.GL.INSiteTo | EntityType | Warehouse | SiteCD | 0 | 0 | PX.Objects.IN.INSite | PX_Objects_GL_INSiteTo | members-04.md | 1491 | 6 |
| PX.Objects.GL.INSiteToBranch | EntityType | Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_INSiteToBranch | members-04.md | 1498 | 6 |
| PX.Objects.GL.Ledger | EntityType | Ledger | LedgerCD | 19 | 30 |  | PX_Objects_GL_Ledger, Ledger | members-04.md | 1505 | 56 |
| PX.Objects.GL.Overrides.ScheduleMaint.BatchSelection | EntityType | Batch to Process | BatchNbr, Module | 0 | 0 | PX.Objects.GL.Batch | PX_Objects_GL_Overrides_ScheduleMaint_BatchSelection, BatchtoProcess, BatchSelection | members-04.md | 1562 | 6 |
| PX.Objects.GL.Overrides.ScheduleProcess.BatchNew | EntityType | GL Batch New | BatchNbr, Module | 1 | 0 | PX.Objects.GL.Batch | PX_Objects_GL_Overrides_ScheduleProcess_BatchNew, GLBatchNew, BatchNew | members-04.md | 1569 | 9 |
| PX.Objects.GL.Overrides.ScheduleProcess.GLTranNew | EntityType | GL Transaction | BatchNbr, LineNbr, Module | 3 | 0 | PX.Objects.GL.GLTran | PX_Objects_GL_Overrides_ScheduleProcess_GLTranNew | members-04.md | 1579 | 11 |
| PX.Objects.GL.ReclassBatch | EntityType | GL Batch | BatchNbr, Module | 0 | 0 | PX.Objects.GL.Batch | PX_Objects_GL_ReclassBatch | members-04.md | 1591 | 6 |
| PX.Objects.GL.Reclassification.Common.GLTranForReclassification | EntityType | GL Transaction | BatchNbr, LineNbr, Module | 11 | 0 | PX.Objects.GL.GLTran | PX_Objects_GL_Reclassification_Common_GLTranForReclassification | members-04.md | 1598 | 19 |
| PX.Objects.GL.Reclassification.UI.GLTranReclHist | EntityType | GL Transaction | BatchNbr, LineNbr, Module | 6 | 0 | PX.Objects.GL.GLTran | PX_Objects_GL_Reclassification_UI_GLTranReclHist | members-04.md | 1618 | 14 |
| PX.Objects.GL.ReclassifyingGLTranAggregate | EntityType |  | BatchNbr, LineNbr, Module | 7 | 2 |  | PX_Objects_GL_ReclassifyingGLTranAggregate | members-04.md | 1633 | 14 |
| PX.Objects.GL.Schedule | EntityType | Schedule | ScheduleID | 44 | 9 |  | PX_Objects_GL_Schedule, Schedule | members-04.md | 1648 | 60 |
| PX.Objects.GL.Standalone.LedgerAlias | EntityType | Ledger | LedgerCD | 0 | 0 | PX.Objects.GL.Ledger | PX_Objects_GL_Standalone_LedgerAlias, Ledger1, LedgerAlias | members-04.md | 1709 | 6 |
| PX.Objects.GL.Sub | EntityType | Subaccount | SubCD | 18 | 165 |  | PX_Objects_GL_Sub, Subaccount, Sub | members-04.md | 1716 | 190 |
| PX.Objects.GL.TranBranch | EntityType | Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_TranBranch | members-04.md | 1907 | 6 |
| PX.Objects.GL.TranINSite | EntityType | Warehouse | SiteCD | 0 | 0 | PX.Objects.IN.INSite | PX_Objects_GL_TranINSite | members-04.md | 1914 | 6 |
| PX.Objects.GL.TranINSiteBranch | EntityType | Branch | BranchCD | 0 | 0 | PX.Objects.GL.Branch | PX_Objects_GL_TranINSiteBranch | members-04.md | 1921 | 6 |
| PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial | EntityType | Adjustment Transactions grouped by SiteLotSerial | DocType, InventoryID, LotSerialNbr, RefNbr, SiteID | 8 | 7 |  | PX_Objects_IN_AffectedAvailability_AdjustmentTranBySiteLotSerial, AdjustmentTransactionsgroupedbySiteLotSerial, AdjustmentTranBySiteLotSerial | members-04.md | 1928 | 21 |
| PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus | EntityType | Adjustment Transactions grouped by SiteStatus | DocType, InventoryID, RefNbr, SiteID | 9 | 1 |  | PX_Objects_IN_AffectedAvailability_AdjustmentTranBySiteStatus, AdjustmentTransactionsgroupedbySiteStatus, AdjustmentTranBySiteStatus | members-04.md | 1950 | 16 |
| PX.Objects.IN.AffectedAvailability.Allocation | ComplexType |  |  | 13 | 0 |  |  | members-04.md | 1967 | 16 |
| PX.Objects.IN.DAC.INConversionHistory | EntityType | Inventory Conversion History | HistoryID | 7 | 1 |  | PX_Objects_IN_DAC_INConversionHistory, InventoryConversionHistory, INConversionHistory | members-04.md | 1984 | 14 |
| PX.Objects.IN.DAC.INItemClassSite | EntityType | Warehouse Item Class Details | ItemClassID, SiteID | 12 | 5 |  | PX_Objects_IN_DAC_INItemClassSite, WarehouseItemClassDetails, INItemClassSite | members-04.md | 1999 | 24 |
| PX.Objects.IN.DAC.INItemLotSerialAttributesHeader | EntityType | INItemLotSerialAttributesHeader | InventoryID, LotSerialNbr | 11 | 8 |  | PX_Objects_IN_DAC_INItemLotSerialAttributesHeader, INItemLotSerialAttributesHeader | members-04.md | 2024 | 26 |
| PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings | EntityType | INItemLotSerialAttributesHeaderCurySettings | CuryID, InventoryID, LotSerialNbr | 12 | 5 |  | PX_Objects_IN_DAC_INItemLotSerialAttributesHeaderCurySettings, INItemLotSerialAttributesHeaderCurySettings | members-04.md | 2051 | 23 |
| PX.Objects.IN.DAC.INRegisterCart | EntityType | Receipt Cart | CartID, DocType, RefNbr, SiteID | 11 | 6 |  | PX_Objects_IN_DAC_INRegisterCart, ReceiptCart, INRegisterCart | members-04.md | 2075 | 23 |
| PX.Objects.IN.DAC.INRegisterCartLine | EntityType | Receipt Cart Line | CartID, DocType, LineNbr, RefNbr, SiteID | 14 | 8 |  | PX_Objects_IN_DAC_INRegisterCartLine, ReceiptCartLine, INRegisterCartLine | members-04.md | 2099 | 28 |
| PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader | EntityType | INRegisterItemLotSerialAttributesHeader | DocType, InventoryID, LotSerialNbr, RefNbr | 14 | 6 |  | PX_Objects_IN_DAC_INRegisterItemLotSerialAttributesHeader, INRegisterItemLotSerialAttributesHeader | members-04.md | 2128 | 27 |
| PX.Objects.IN.DAC.INSetupApproval | EntityType | IN Approval | ApprovalID | 12 | 4 |  | PX_Objects_IN_DAC_INSetupApproval, INApproval, INSetupApproval | members-04.md | 2156 | 22 |
| PX.Objects.IN.DAC.INSitePlanningStrategy | EntityType | Warehouse Planning Strategy | PlanningStrategyID | 13 | 7 |  | PX_Objects_IN_DAC_INSitePlanningStrategy, WarehousePlanningStrategy, INSitePlanningStrategy | members-04.md | 2179 | 27 |
| PX.Objects.IN.DAC.INSitePlanningStrategyDetail | EntityType | Warehouse Planning Strategy Detail | LineNbr, PlanningStrategyID | 14 | 4 |  | PX_Objects_IN_DAC_INSitePlanningStrategyDetail, WarehousePlanningStrategyDetail, INSitePlanningStrategyDetail | members-04.md | 2207 | 25 |
| PX.Objects.IN.DAC.INSiteZone | EntityType | Warehouse Zone | ZoneID | 15 | 11 |  | PX_Objects_IN_DAC_INSiteZone, WarehouseZone, INSiteZone | members-04.md | 2233 | 33 |
| PX.Objects.IN.DAC.INTransferDemandLine | EntityType | Transfer Demand Line | RecordID | 31 | 13 |  | PX_Objects_IN_DAC_INTransferDemandLine, TransferDemandLine, INTransferDemandLine | members-04.md | 2267 | 51 |
| PX.Objects.IN.DAC.INTransferDemandPutAwaySplit | EntityType | Transfer Demand Put Away Split | SplitLineNbr, TransferDemandLineID | 18 | 9 |  | PX_Objects_IN_DAC_INTransferDemandPutAwaySplit, TransferDemandPutAwaySplit, INTransferDemandPutAwaySplit | members-04.md | 2319 | 34 |
| PX.Objects.IN.DAC.INTransferList | EntityType | Transfer List | ListNbr | 15 | 4 |  | PX_Objects_IN_DAC_INTransferList, TransferList, INTransferList | members-04.md | 2354 | 25 |
| PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected | EntityType | INItemLotSerialAttributesHeaderSelected | InventoryID, LocationID, LotSerialNbr, SiteID | 15 | 1 |  | PX_Objects_IN_DAC_Projections_INItemLotSerialAttributesHeaderSelected, INItemLotSerialAttributesHeaderSelected | members-04.md | 2380 | 23 |
| PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType | EntityType | IN Location Status by Cost Layer Type | CostLayerType, InventoryID, LocationID, SiteID, SubItemID | 23 | 0 |  | PX_Objects_IN_DAC_Projections_INLocationStatusByCostLayerType, INLocationStatusbyCostLayerType | members-04.md | 2404 | 29 |
| PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType | EntityType | IN Lot/Serial Cost Status by Cost Layer Type | CostLayerType, InventoryID, LotSerialNbr, SiteID, SubItemID | 9 | 4 |  | PX_Objects_IN_DAC_Projections_INLotSerialCostStatusByCostLayerType, INLotSerialCostStatusbyCostLayerType | members-04.md | 2434 | 20 |
| PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType | EntityType | IN Lot/Serial Status by Cost Layer Type | CostLayerType, InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID | 25 | 0 |  | PX_Objects_IN_DAC_Projections_INLotSerialStatusByCostLayerType, INLotSerialStatusbyCostLayerType | members-04.md | 2455 | 31 |
| PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType | EntityType | IN Site Cost Status by Cost Layer Type | CostLayerType, InventoryID, SiteID, SubItemID | 8 | 4 |  | PX_Objects_IN_DAC_Projections_INSiteCostStatusByCostLayerType, INSiteCostStatusbyCostLayerType | members-04.md | 2487 | 19 |
| PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType | EntityType | IN Site Status by Cost Layer Type | CostLayerType, InventoryID, SiteID, SubItemID | 23 | 0 |  | PX_Objects_IN_DAC_Projections_INSiteStatusByCostLayerType, INSiteStatusbyCostLayerType | members-04.md | 2507 | 29 |
| PX.Objects.IN.DAC.WarehouseReference | EntityType |  | PortalSetupID, SiteID | 9 | 3 |  | PX_Objects_IN_DAC_WarehouseReference | members-04.md | 2537 | 17 |
| PX.Objects.IN.GS1UOMSetup | EntityType | GS1 Unit Setup |  | 27 | 22 |  |  | members-04.md | 2555 | 54 |
| PX.Objects.IN.INABCCode | EntityType | IN ABC Code | ABCCodeID | 12 | 5 |  | PX_Objects_IN_INABCCode, INABCCode | members-04.md | 2610 | 23 |
| PX.Objects.IN.INAvailabilityScheme | EntityType | Availability Calculation Rule | AvailabilitySchemeID | 29 | 3 |  | PX_Objects_IN_INAvailabilityScheme, AvailabilityCalculationRule, INAvailabilityScheme | members-04.md | 2634 | 38 |
| PX.Objects.IN.INCart | EntityType | IN Cart | CartCD, SiteID | 15 | 14 |  | PX_Objects_IN_INCart, INCart | members-04.md | 2673 | 36 |
| PX.Objects.IN.INCartContentByLocation | EntityType | IN Cart Content by Location | InventoryID, LocationID, SiteID, SubItemID | 5 | 5 |  | PX_Objects_IN_INCartContentByLocation, INCartContentbyLocation | members-04.md | 2710 | 16 |
| PX.Objects.IN.INCartContentByLotSerial | EntityType | IN Cart Content by Lot/Serial Nbr. | InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID | 6 | 6 |  | PX_Objects_IN_INCartContentByLotSerial, INCartContentbyLotSerialNbr, INCartContentByLotSerial | members-04.md | 2727 | 18 |
| PX.Objects.IN.INCartSplit | EntityType | IN Cart Split | CartID, SiteID, SplitLineNbr | 14 | 14 |  | PX_Objects_IN_INCartSplit, INCartSplit | members-04.md | 2746 | 34 |
| PX.Objects.IN.INCategory | EntityType | Item Sales Category | CategoryID | 15 | 5 |  | PX_Objects_IN_INCategory, ItemSalesCategory, INCategory | members-04.md | 2781 | 27 |
| PX.Objects.IN.INComponent | EntityType | Deferred Revenue Components | ComponentID, InventoryID | 19 | 8 |  | PX_Objects_IN_INComponent, DeferredRevenueComponents, INComponent | members-04.md | 2809 | 33 |
| PX.Objects.IN.INComponentTran | EntityType | IN Component | DocType, LineNbr, RefNbr | 2 | 0 | PX.Objects.IN.INTran | PX_Objects_IN_INComponentTran, INComponent1, INComponentTran | members-04.md | 2843 | 9 |
| PX.Objects.IN.INComponentTranSplit | EntityType | IN Component Split | DocType, LineNbr, RefNbr, SplitLineNbr | 0 | 0 | PX.Objects.IN.INTranSplit | PX_Objects_IN_INComponentTranSplit, INComponentSplit, INComponentTranSplit | members-04.md | 2853 | 6 |
| PX.Objects.IN.INCostCenter | EntityType | IN Cost Center | CostCenterID | 10 | 16 |  | PX_Objects_IN_INCostCenter, INCostCenter | members-04.md | 2860 | 32 |
| PX.Objects.IN.INCostStatus | EntityType | IN Cost Status | CostID | 17 | 9 |  | PX_Objects_IN_INCostStatus, INCostStatus | members-04.md | 2893 | 33 |
| PX.Objects.IN.INCostStatusSummary | EntityType | IN Cost Status Summary | CostID | 0 | 0 | PX.Objects.IN.INCostStatus | PX_Objects_IN_INCostStatusSummary, INCostStatusSummary | members-04.md | 2927 | 6 |
| PX.Objects.IN.INCostStatusTransitLineSummary | EntityType | IN Cost Status | CostID | 0 | 0 | PX.Objects.IN.INCostStatus | PX_Objects_IN_INCostStatusTransitLineSummary | members-04.md | 2934 | 6 |
| PX.Objects.IN.INCostSubItemXRef | EntityType |  | CostSubItemID, SubItemID | 3 | 1 |  | PX_Objects_IN_INCostSubItemXRef | members-04.md | 2941 | 9 |
| PX.Objects.IN.INItemBox | EntityType | IN Item Box | BoxID, InventoryID | 15 | 5 |  | PX_Objects_IN_INItemBox, INItemBox | members-04.md | 2951 | 27 |
| PX.Objects.IN.INItemBoxEx | EntityType | IN Item Box | BoxID, InventoryID | 7 | 0 | PX.Objects.IN.INItemBox | PX_Objects_IN_INItemBoxEx | members-04.md | 2979 | 14 |
| PX.Objects.IN.INItemCategory | EntityType | Item Sales Category by Item | CategoryID, InventoryID | 7 | 3 |  | PX_Objects_IN_INItemCategory, ItemSalesCategorybyItem, INItemCategory | members-04.md | 2994 | 17 |
| PX.Objects.IN.INItemClass | EntityType | Item Class | ItemClassCD | 52 | 57 |  | PX_Objects_IN_INItemClass, ItemClass, INItemClass | members-04.md | 3012 | 116 |
| PX.Objects.IN.INItemClassCurySettings | EntityType | Item Class Currency Settings | CuryID, ItemClassID | 9 | 6 |  | PX_Objects_IN_INItemClassCurySettings, ItemClassCurrencySettings, INItemClassCurySettings | members-04.md | 3129 | 21 |
| PX.Objects.IN.INItemClassRep | EntityType | Item Class Replenishment | CuryID, ItemClassID, ReplenishmentClassID | 26 | 8 |  | PX_Objects_IN_INItemClassRep, ItemClassReplenishment, INItemClassRep | members-04.md | 3151 | 41 |
| PX.Objects.IN.INItemCost | EntityType | Item Cost Statistics | CuryID, InventoryID | 10 | 353 |  | PX_Objects_IN_INItemCost, ItemCostStatistics, INItemCost | members-04.md | 3193 | 369 |
| PX.Objects.IN.INItemCostHist | EntityType | IN Item Cost History | AccountID, CostSiteID, CostSubItemID, FinPeriodID, InventoryID, SubID | 87 | 6 |  | PX_Objects_IN_INItemCostHist, INItemCostHistory, INItemCostHist | members-04.md | 3563 | 99 |
| PX.Objects.IN.INItemCostHistByPeriod | EntityType | IN Item Cost History by Period | AccountID, CostSiteID, CostSubItemID, FinPeriodID, InventoryID, SubID | 7 | 5 |  | PX_Objects_IN_INItemCostHistByPeriod, INItemCostHistorybyPeriod, INItemCostHistByPeriod | members-04.md | 3663 | 18 |
| PX.Objects.IN.INItemLotSerial | EntityType | Lot/Serial by Item | InventoryID, LotSerialNbr | 19 | 7 |  | PX_Objects_IN_INItemLotSerial, LotSerialbyItem, INItemLotSerial | members-04.md | 3682 | 33 |
| PX.Objects.IN.INItemLotSerialAttribute | EntityType | Inventory Item Lot/Serial Attribute | AttributeID, InventoryID | 13 | 4 |  | PX_Objects_IN_INItemLotSerialAttribute, InventoryItemLotSerialAttribute, INItemLotSerialAttribute | members-04.md | 3716 | 24 |
| PX.Objects.IN.INItemPlan | EntityType | IN Item Plan | PlanID | 39 | 34 |  | PX_Objects_IN_INItemPlan, INItemPlan | members-04.md | 3741 | 80 |
| PX.Objects.IN.INItemRep | EntityType | Item Replenishment Settings | CuryID, InventoryID, ReplenishmentClassID | 29 | 9 |  | PX_Objects_IN_INItemRep, ItemReplenishmentSettings, INItemRep | members-04.md | 3822 | 45 |
| PX.Objects.IN.INItemSalesHist | EntityType | Item Sales History | CostSiteID, CostSubItemID, FinPeriodID, InventoryID | 41 | 2 |  | PX_Objects_IN_INItemSalesHist, ItemSalesHistory, INItemSalesHist | members-04.md | 3868 | 49 |
| PX.Objects.IN.INItemSite | EntityType | Item/Warehouse Settings | InventoryID, SiteID | 103 | 39 |  | PX_Objects_IN_INItemSite, ItemWarehouseSettings, INItemSite | members-04.md | 3918 | 149 |
| PX.Objects.IN.INItemSiteHist | EntityType | IN Item Site History | FinPeriodID, InventoryID, LocationID, SiteID, SubItemID | 35 | 5 |  | PX_Objects_IN_INItemSiteHist, INItemSiteHistory, INItemSiteHist | members-04.md | 4068 | 47 |
| PX.Objects.IN.INItemSiteHistByDay | EntityType | IN Item Site History by Day | Date, InventoryID, LocationID, SiteID, SubItemID | 6 | 0 |  | PX_Objects_IN_INItemSiteHistByDay, INItemSiteHistorybyDay, INItemSiteHistByDay | members-04.md | 4116 | 12 |
| PX.Objects.IN.INItemSiteHistByLastDayInPeriod | EntityType | IN Item Site History by Last Day In Period | FinPeriodID, InventoryID, LocationID, SiteID, SubItemID | 6 | 2 |  | PX_Objects_IN_INItemSiteHistByLastDayInPeriod, INItemSiteHistorybyLastDayInPeriod, INItemSiteHistByLastDayInPeriod | members-04.md | 4129 | 14 |
| PX.Objects.IN.INItemSiteHistByLatestSDate | EntityType | IN Item Site History by Latest SDate | InventoryID, LocationID, SiteID, SubItemID | 5 | 0 |  | PX_Objects_IN_INItemSiteHistByLatestSDate, INItemSiteHistorybyLatestSDate, INItemSiteHistByLatestSDate | members-04.md | 4144 | 11 |
| PX.Objects.IN.INItemSiteHistByPeriod | EntityType | IN Item Site History by Period | FinPeriodID, InventoryID, LocationID, SiteID, SubItemID | 6 | 0 |  | PX_Objects_IN_INItemSiteHistByPeriod, INItemSiteHistorybyPeriod, INItemSiteHistByPeriod | members-04.md | 4156 | 12 |
| PX.Objects.IN.INItemSiteHistDay | EntityType | IN Item Site History Day | InventoryID, LocationID, SDate, SiteID, SubItemID | 23 | 6 |  | PX_Objects_IN_INItemSiteHistDay, INItemSiteHistoryDay, INItemSiteHistDay | members-04.md | 4169 | 36 |
| PX.Objects.IN.INItemSiteReplenishment | EntityType | SubItem Replenishment Info | InventoryID, SiteID, SubItemID | 22 | 6 |  | PX_Objects_IN_INItemSiteReplenishment, SubItemReplenishmentInfo, INItemSiteReplenishment | members-04.md | 4206 | 35 |
| PX.Objects.IN.INItemStats | EntityType | IN Item Statistics | InventoryID, SiteID | 14 | 3 |  | PX_Objects_IN_INItemStats, INItemStatistics, INItemStats | members-04.md | 4242 | 24 |
| PX.Objects.IN.INItemXRef | EntityType | Cross-Reference | AlternateID, AlternateType, BAccountID, InventoryID, SubItemID | 16 | 6 |  | PX_Objects_IN_INItemXRef, CrossReference, INItemXRef | members-04.md | 4267 | 29 |
| PX.Objects.IN.INKitRegister | EntityType | IN Kit | DocType, RefNbr | 80 | 52 |  | PX_Objects_IN_INKitRegister, INKit, INKitRegister | members-04.md | 4297 | 139 |
| PX.Objects.IN.INKitSerialPart | EntityType |  | DocType, KitLineNbr, KitSplitLineNbr, PartLineNbr, PartSplitLineNbr, RefNbr | 13 | 4 |  | PX_Objects_IN_INKitSerialPart | members-04.md | 4437 | 22 |
| PX.Objects.IN.INKitSpecHdr | EntityType | Kit Specification | KitInventoryID, RevisionID | 16 | 9 |  | PX_Objects_IN_INKitSpecHdr, KitSpecification, INKitSpecHdr | members-04.md | 4460 | 32 |
| PX.Objects.IN.INKitSpecNonStkDet | EntityType | Non-Stock Component of Kit Specification | KitInventoryID, LineNbr, RevisionID | 17 | 6 |  | PX_Objects_IN_INKitSpecNonStkDet, NonStockComponentofKitSpecification, INKitSpecNonStkDet | members-04.md | 4493 | 30 |
| PX.Objects.IN.INKitSpecStkDet | EntityType | Stock Component of Kit Specification | KitInventoryID, LineNbr, RevisionID | 19 | 7 |  | PX_Objects_IN_INKitSpecStkDet, StockComponentofKitSpecification, INKitSpecStkDet | members-04.md | 4524 | 33 |
| PX.Objects.IN.INKitTranSplit | EntityType | IN Kit Split | DocType, LineNbr, RefNbr, SplitLineNbr | 27 | 12 |  | PX_Objects_IN_INKitTranSplit, INKitSplit, INKitTranSplit | members-04.md | 4558 | 46 |
| PX.Objects.IN.INLocation | EntityType | IN Location | LocationCD, SiteID | 28 | 78 |  | PX_Objects_IN_INLocation, INLocation | members-04.md | 4605 | 113 |
| PX.Objects.IN.INLocationCostStatus | EntityType |  | InventoryID, LocationID, SiteID, SubItemID | 8 | 4 |  | PX_Objects_IN_INLocationCostStatus | members-04.md | 4719 | 18 |
| PX.Objects.IN.INLocationStatus | EntityType | IN Location Status | InventoryID, LocationID, SiteID, SubItemID | 65 | 21 |  | PX_Objects_IN_INLocationStatus, INLocationStatus | members-04.md | 4738 | 93 |
| PX.Objects.IN.INLocationStatusByCostCenter | EntityType | IN Location Status by Cost Center | CostCenterID, InventoryID, LocationID, SiteID, SubItemID | 68 | 10 |  | PX_Objects_IN_INLocationStatusByCostCenter, INLocationStatusbyCostCenter | members-04.md | 4832 | 85 |
| PX.Objects.IN.INLotSerClass | EntityType | Lot/Serial Class | LotSerClassID | 21 | 8 |  | PX_Objects_IN_INLotSerClass, LotSerialClass, INLotSerClass | members-04.md | 4918 | 36 |
| PX.Objects.IN.INLotSerClassAttribute | EntityType | Lot/Serial Class Attribute | AttributeID, LotSerClassID | 12 | 4 |  | PX_Objects_IN_INLotSerClassAttribute, LotSerialClassAttribute, INLotSerClassAttribute | members-04.md | 4955 | 22 |
| PX.Objects.IN.INLotSerClassLotSerNumVal | EntityType | Auto-Incremental Value of a Lot/Serial Class | LotSerClassID | 9 | 3 |  | PX_Objects_IN_INLotSerClassLotSerNumVal, AutoIncrementalValueofaLotSerialClass, INLotSerClassLotSerNumVal | members-04.md | 4978 | 18 |
| PX.Objects.IN.INLotSerialStatus | EntityType | IN Lot/Serial Status | InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID | 68 | 19 |  | PX_Objects_IN_INLotSerialStatus, INLotSerialStatus | members-04.md | 4997 | 94 |
| PX.Objects.IN.INLotSerialStatusByCostCenter | EntityType | IN Lot/Serial Status by Cost Center | CostCenterID, InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID | 71 | 33 |  | PX_Objects_IN_INLotSerialStatusByCostCenter, INLotSerialStatusbyCostCenter | members-04.md | 5092 | 111 |
| PX.Objects.IN.INLotSerSegment | EntityType | Lot/Serial Segment | LotSerClassID, SegmentID | 11 | 3 |  | PX_Objects_IN_INLotSerSegment, LotSerialSegment, INLotSerSegment | members-04.md | 5204 | 20 |
| PX.Objects.IN.INMovementClass | EntityType | IN Movement Class | MovementClassID | 11 | 5 |  | PX_Objects_IN_INMovementClass, INMovementClass | members-04.md | 5225 | 22 |
| PX.Objects.IN.INNotification | EntityType | Default Notification setup | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_IN_INNotification | members-04.md | 5248 | 6 |
| PX.Objects.IN.INOverheadTran | EntityType | IN Overhead | DocType, LineNbr, RefNbr | 39 | 19 |  | PX_Objects_IN_INOverheadTran, INOverhead, INOverheadTran | members-04.md | 5255 | 64 |
| PX.Objects.IN.INPIClass | EntityType | Physical Inventory Type | PIClassID | 28 | 10 |  | PX_Objects_IN_INPIClass, PhysicalInventoryType, INPIClass | members-04.md | 5320 | 45 |
| PX.Objects.IN.INPIClassItem | EntityType | Physical Inventory Type by Item | InventoryID, PIClassID | 6 | 3 |  | PX_Objects_IN_INPIClassItem, PhysicalInventoryTypebyItem, INPIClassItem | members-04.md | 5366 | 15 |
| PX.Objects.IN.INPIClassItemClass | EntityType |  | ItemClassID, PIClassID | 9 | 4 |  | PX_Objects_IN_INPIClassItemClass | members-04.md | 5382 | 18 |
| PX.Objects.IN.INPIClassLocation | EntityType | Physical Inventory Type by Location | LocationID, PIClassID | 6 | 3 |  | PX_Objects_IN_INPIClassLocation, PhysicalInventoryTypebyLocation, INPIClassLocation | members-04.md | 5401 | 15 |
| PX.Objects.IN.INPICycle | EntityType | Physical Inventory Cycle | CycleID | 11 | 4 |  | PX_Objects_IN_INPICycle, PhysicalInventoryCycle, INPICycle | members-04.md | 5417 | 21 |
| PX.Objects.IN.INPIDetail | EntityType | IN Physical count Detail | LineNbr, PIID | 23 | 12 |  | PX_Objects_IN_INPIDetail, INPhysicalcountDetail, INPIDetail | members-04.md | 5439 | 42 |
| PX.Objects.IN.INPIHeader | EntityType | Physical Inventory Review | PIID | 25 | 14 |  | PX_Objects_IN_INPIHeader, PhysicalInventoryReview, INPIHeader | members-04.md | 5482 | 46 |
| PX.Objects.IN.INPIStatus | EntityType | Physical Inventory Status | LocRecordID, RecordID | 11 | 4 |  | PX_Objects_IN_INPIStatus, PhysicalInventoryStatus, INPIStatus | members-04.md | 5529 | 21 |
| PX.Objects.IN.INPIStatusItem | EntityType |  | RecordID | 12 | 5 |  | PX_Objects_IN_INPIStatusItem | members-04.md | 5551 | 22 |
| PX.Objects.IN.INPIStatusLoc | EntityType |  | RecordID | 11 | 6 |  | PX_Objects_IN_INPIStatusLoc | members-04.md | 5574 | 22 |
| PX.Objects.IN.INPlanType | EntityType | IN Item Plan Type | PlanType | 57 | 13 |  | PX_Objects_IN_INPlanType, INItemPlanType, INPlanType | members-04.md | 5597 | 77 |
| PX.Objects.IN.INPostClass | EntityType | Posting Class | PostClassID | 21 | 26 |  | PX_Objects_IN_INPostClass, PostingClass, INPostClass | members-04.md | 5675 | 54 |
| PX.Objects.IN.INPriceClass | EntityType | IN Item Price Class | PriceClassID | 11 | 8 |  | PX_Objects_IN_INPriceClass, INItemPriceClass, INPriceClass | members-04.md | 5730 | 26 |
| PX.Objects.IN.INRegister | EntityType | Receipt | DocType, RefNbr | 55 | 54 |  | PX_Objects_IN_INRegister, Receipt, INRegister | members-04.md | 5757 | 116 |
| PX.Objects.IN.INReplenishmentClass | EntityType | Replenishment Class | ReplenishmentClassID | 10 | 7 |  | PX_Objects_IN_INReplenishmentClass, ReplenishmentClass, INReplenishmentClass | members-04.md | 5874 | 23 |
| PX.Objects.IN.INReplenishmentItem | EntityType |  | InventoryID, SiteID | 63 | 2 | PX.Objects.IN.S.INItemSite | PX_Objects_IN_INReplenishmentItem | members-04.md | 5898 | 72 |
| PX.Objects.IN.INReplenishmentLine | EntityType | Replenishment Line | LineNbr, RefNbr | 24 | 18 |  | PX_Objects_IN_INReplenishmentLine, ReplenishmentLine, INReplenishmentLine | members-04.md | 5971 | 48 |
| PX.Objects.IN.INReplenishmentOrder | EntityType | Replenishment Order | RefNbr | 13 | 6 |  | PX_Objects_IN_INReplenishmentOrder, ReplenishmentOrder, INReplenishmentOrder | members-04.md | 6020 | 26 |
| PX.Objects.IN.INReplenishmentPolicy | EntityType | Replenishment Policy | ReplenishmentPolicyID | 12 | 7 |  | PX_Objects_IN_INReplenishmentPolicy, ReplenishmentPolicy, INReplenishmentPolicy | members-04.md | 6047 | 26 |
| PX.Objects.IN.INReplenishmentSeason | EntityType | Replenishment Seasonality | ReplenishmentPolicyID, SeasonID | 13 | 3 |  | PX_Objects_IN_INReplenishmentSeason, ReplenishmentSeasonality, INReplenishmentSeason | members-04.md | 6074 | 22 |
| PX.Objects.IN.INScanSetup | EntityType | IN Scan Setup | BranchID | 22 | 4 |  | PX_Objects_IN_INScanSetup, INScanSetup | members-04.md | 6097 | 32 |
| PX.Objects.IN.INScanUserSetup | EntityType | IN Scan User Setup | Mode, UserID | 12 | 5 |  | PX_Objects_IN_INScanUserSetup, INScanUserSetup | members-04.md | 6130 | 23 |
| PX.Objects.IN.INSetup | EntityType | IN Setup |  | 54 | 33 |  |  | members-04.md | 6154 | 92 |
| PX.Objects.IN.INSite | EntityType | Warehouse | SiteCD | 35 | 216 |  | PX_Objects_IN_INSite, Warehouse, INSite | members-04.md | 6247 | 258 |
| PX.Objects.IN.INSiteBuilding | EntityType | Warehouse Building | BuildingCD | 11 | 5 |  | PX_Objects_IN_INSiteBuilding, WarehouseBuilding, INSiteBuilding | members-04.md | 6506 | 22 |
| PX.Objects.IN.INSiteLotSerial | EntityType | Lot/Serial by Warehouse | InventoryID, LotSerialNbr, SiteID | 16 | 2 |  | PX_Objects_IN_INSiteLotSerial, LotSerialbyWarehouse, INSiteLotSerial | members-04.md | 6529 | 25 |
| PX.Objects.IN.INSiteStatus | EntityType | IN Site Status | InventoryID, SiteID, SubItemID | 64 | 18 |  | PX_Objects_IN_INSiteStatus, INSiteStatus | members-04.md | 6555 | 89 |
| PX.Objects.IN.INSiteStatusByCostCenter | EntityType | IN Site Status by Cost Center | CostCenterID, InventoryID, SiteID, SubItemID | 68 | 9 |  | PX_Objects_IN_INSiteStatusByCostCenter, INSiteStatusbyCostCenter | members-04.md | 6645 | 84 |
| PX.Objects.IN.INSiteStatusByCostCenterShort | EntityType | IN Site Status by Cost Center Short | CostCenterID, InventoryID, SiteID, SubItemID | 8 | 10 |  | PX_Objects_IN_INSiteStatusByCostCenterShort, INSiteStatusbyCostCenterShort | members-04.md | 6730 | 24 |
| PX.Objects.IN.INSiteStatusQtyAggregated | EntityType | Sum of Inventory Qtys by InventoryID with LastModifiedDateTime | InventoryID | 3 | 0 |  | PX_Objects_IN_INSiteStatusQtyAggregated, SumofInventoryQtysbyInventoryIDwithLastModifiedDateTime, INSiteStatusQtyAggregated | members-04.md | 6755 | 9 |
| PX.Objects.IN.INSiteStatusSelected | EntityType |  | InventoryID | 21 | 268 |  | PX_Objects_IN_INSiteStatusSelected | members-04.md | 6765 | 295 |
| PX.Objects.IN.INSiteStatusSummary | EntityType | IN Warehouse Status | InventoryID, SiteID | 5 | 3 |  | PX_Objects_IN_INSiteStatusSummary, INWarehouseStatus, INSiteStatusSummary | members-04.md | 7061 | 14 |
| PX.Objects.IN.INSubItem | EntityType | IN Sub Item | SubItemCD | 11 | 107 |  | PX_Objects_IN_INSubItem, INSubItem | members-04.md | 7076 | 125 |
| PX.Objects.IN.INSubItemRep | EntityType | Subitem Replenishment Settings | CuryID, InventoryID, ReplenishmentClassID, SubItemID | 16 | 7 |  | PX_Objects_IN_INSubItemRep, SubitemReplenishmentSettings, INSubItemRep | members-04.md | 7202 | 29 |
| PX.Objects.IN.INSubItemSegmentValue | EntityType | IN Subitem Segment Value | InventoryID, SegmentID, Value | 3 | 1 |  | PX_Objects_IN_INSubItemSegmentValue, INSubitemSegmentValue | members-04.md | 7232 | 10 |
| PX.Objects.IN.IntercompanyGoodsInTransitResult | EntityType | Intercompany Goods in Transit Result | LineNbr, POReceiptNbr, POReceiptType, ShipmentNbr | 24 | 6 |  | PX_Objects_IN_IntercompanyGoodsInTransitResult, IntercompanyGoodsinTransitResult | members-04.md | 7243 | 36 |
| PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult | EntityType | Intercompany Returned Goods in Transit Result | LineNbr, POReturnNbr | 24 | 9 |  | PX_Objects_IN_IntercompanyReturnedGoodsInTransitResult, IntercompanyReturnedGoodsinTransitResult | members-04.md | 7280 | 39 |
| PX.Objects.IN.INTote | EntityType | IN Tote | SiteID, ToteCD | 15 | 7 |  | PX_Objects_IN_INTote, INTote | members-04.md | 7320 | 29 |
| PX.Objects.IN.INTran | EntityType | IN Transaction | DocType, LineNbr, RefNbr | 88 | 54 |  | PX_Objects_IN_INTran, INTransaction, INTran | members-04.md | 7350 | 149 |
| PX.Objects.IN.INTranCost | EntityType | IN Transaction Cost | CostDocType, CostID, CostRefNbr, DocType, LineNbr, RefNbr | 34 | 12 |  | PX_Objects_IN_INTranCost, INTransactionCost, INTranCost | members-04.md | 7500 | 53 |
| PX.Objects.IN.INTranDetail | EntityType | IN Transaction Detail | DocType, LineNbr, RefNbr, SplitLineNbr, TranType | 18 | 5 |  | PX_Objects_IN_INTranDetail, INTransactionDetail, INTranDetail | members-04.md | 7554 | 30 |
| PX.Objects.IN.INTransfer | EntityType | Receipt | DocType, RefNbr | 0 | 0 | PX.Objects.IN.INRegister | PX_Objects_IN_INTransfer | members-04.md | 7585 | 6 |
| PX.Objects.IN.INTransferLocationStatus | EntityType |  | InventoryID, SubItemID, TransferNbr | 5 | 3 |  | PX_Objects_IN_INTransferLocationStatus | members-04.md | 7592 | 13 |
| PX.Objects.IN.INTransferStatus | EntityType |  | InventoryID, SubItemID, TransferNbr | 8 | 4 |  | PX_Objects_IN_INTransferStatus | members-04.md | 7606 | 18 |
| PX.Objects.IN.INTransitLine | EntityType | Transfer Line | TransferLineNbr, TransferNbr | 24 | 11 |  | PX_Objects_IN_INTransitLine, TransferLine, INTransitLine | members-04.md | 7625 | 42 |
| PX.Objects.IN.INTransitLineLotSerialStatus | EntityType |  | InventoryID, LotSerialNbr, SubItemID, TransferLineNbr, TransferNbr | 42 | 5 |  | PX_Objects_IN_INTransitLineLotSerialStatus | members-04.md | 7668 | 52 |
| PX.Objects.IN.INTransitLineStatus | EntityType |  | TransferLineNbr, TransferNbr | 18 | 5 |  | PX_Objects_IN_INTransitLineStatus | members-04.md | 7721 | 28 |
| PX.Objects.IN.INTranSplit | EntityType | IN Transaction Split | DocType, LineNbr, RefNbr, SplitLineNbr | 50 | 23 |  | PX_Objects_IN_INTranSplit, INTransactionSplit, INTranSplit | members-04.md | 7750 | 80 |
| PX.Objects.IN.INUnit | EntityType | Inventory Unit Conversions | FromUnit, InventoryID, ItemClassID, ToUnit, UnitType | 17 | 145 |  | PX_Objects_IN_INUnit, InventoryUnitConversions, INUnit | members-04.md | 7831 | 169 |
| PX.Objects.IN.INUpdateStdCostRecord | EntityType |  | CuryID, InventoryID | 11 | 2 |  | PX_Objects_IN_INUpdateStdCostRecord | members-04.md | 8001 | 18 |
| PX.Objects.IN.InventoryItem | EntityType | Inventory Item | InventoryCD | 111 | 314 |  | PX_Objects_IN_InventoryItem, InventoryItem | members-04.md | 8020 | 432 |
| PX.Objects.IN.InventoryItemCommon | EntityType | Inventory Item Common Fields Only | InventoryCD | 9 | 267 |  | PX_Objects_IN_InventoryItemCommon, InventoryItemCommonFieldsOnly, InventoryItemCommon | members-04.md | 8453 | 282 |
| PX.Objects.IN.InventoryItemCurySettings | EntityType | Inventory Item Currency Settings | CuryID, InventoryID | 17 | 17 |  | PX_Objects_IN_InventoryItemCurySettings, InventoryItemCurrencySettings, InventoryItemCurySettings | members-04.md | 8736 | 40 |
| PX.Objects.IN.InventoryItemLotSerNumVal | EntityType | Auto-Incremental Value of a Stock Item | InventoryID | 9 | 3 |  | PX_Objects_IN_InventoryItemLotSerNumVal, AutoIncrementalValueofaStockItem, InventoryItemLotSerNumVal | members-04.md | 8777 | 18 |
| PX.Objects.IN.InventoryTranSumEnqResult | ComplexType |  |  | 30 | 0 |  |  | members-04.md | 8796 | 33 |
| PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup | EntityType | Attribute Description Group | GroupID, TemplateID | 10 | 4 |  | PX_Objects_IN_Matrix_DAC_INAttributeDescriptionGroup, AttributeDescriptionGroup, INAttributeDescriptionGroup | members-04.md | 8830 | 20 |
| PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem | EntityType | Attribute Description Item | AttributeID, GroupID, TemplateID | 11 | 5 |  | PX_Objects_IN_Matrix_DAC_INAttributeDescriptionItem, AttributeDescriptionItem, INAttributeDescriptionItem | members-04.md | 8851 | 22 |
| PX.Objects.IN.Matrix.DAC.INMatrixExcludedData | EntityType | Data Excluded From Update of Matrix Items | FieldName, TableName, TemplateID, Type | 14 | 3 |  | PX_Objects_IN_Matrix_DAC_INMatrixExcludedData, DataExcludedFromUpdateofMatrixItems, INMatrixExcludedData | members-04.md | 8874 | 24 |
| PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule | EntityType | Matrix Generation Rule | LineNbr, ParentID, ParentType, Type | 20 | 7 |  | PX_Objects_IN_Matrix_DAC_INMatrixGenerationRule, MatrixGenerationRule, INMatrixGenerationRule | members-04.md | 8899 | 33 |
| PX.Objects.IN.Matrix.DAC.Projections.DescriptionGenerationRule | EntityType | Description Generation Rule | LineNbr, ParentID, ParentType, Type | 0 | 0 | PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule | PX_Objects_IN_Matrix_DAC_Projections_DescriptionGenerationRule, DescriptionGenerationRule | members-04.md | 8933 | 6 |
| PX.Objects.IN.Matrix.DAC.Projections.ExcludedAttribute | EntityType | Attribute Excluded From Update of Matrix Items | FieldName, TableName, TemplateID, Type | 0 | 0 | PX.Objects.IN.Matrix.DAC.INMatrixExcludedData | PX_Objects_IN_Matrix_DAC_Projections_ExcludedAttribute, AttributeExcludedFromUpdateofMatrixItems, ExcludedAttribute | members-04.md | 8940 | 6 |
| PX.Objects.IN.Matrix.DAC.Projections.ExcludedField | EntityType | Field Excluded From Update of Matrix Items | FieldName, TableName, TemplateID, Type | 0 | 0 | PX.Objects.IN.Matrix.DAC.INMatrixExcludedData | PX_Objects_IN_Matrix_DAC_Projections_ExcludedField, FieldExcludedFromUpdateofMatrixItems, ExcludedField | members-04.md | 8947 | 6 |
| PX.Objects.IN.Matrix.DAC.Projections.IDGenerationRule | EntityType | ID Generation Rule | LineNbr, ParentID, ParentType, Type | 0 | 0 | PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule | PX_Objects_IN_Matrix_DAC_Projections_IDGenerationRule, IDGenerationRule | members-04.md | 8954 | 6 |
| PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem | EntityType | Inventory Item with Attribute Values | InventoryCD | 6 | 0 | PX.Objects.IN.InventoryItem | PX_Objects_IN_Matrix_DAC_Unbound_MatrixInventoryItem, InventoryItemwithAttributeValues, MatrixInventoryItem | members-04.md | 8961 | 14 |
| PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback | EntityType | Related Item ML Feedback | InventoryID, RelatedInventoryID | 10 | 4 |  | PX_Objects_IN_RelatedItems_DAC_INRelatedInventoryUserFeedback, RelatedItemMLFeedback, INRelatedInventoryUserFeedback | members-04.md | 8976 | 20 |
| PX.Objects.IN.RelatedItems.INRelatedInventory | EntityType | Related Item | InventoryID, LineID | 27 | 5 |  | PX_Objects_IN_RelatedItems_INRelatedInventory, RelatedItem, INRelatedInventory | members-04.md | 8997 | 39 |
| PX.Objects.IN.RelatedItems.RelatedItem | EntityType | Related Item | InventoryID, LineID | 22 | 3 |  | PX_Objects_IN_RelatedItems_RelatedItem, RelatedItem1 | members-04.md | 9037 | 32 |
| PX.Objects.IN.RelatedItems.RelatedItemHistory | EntityType | Related Item History | LineID | 37 | 21 |  | PX_Objects_IN_RelatedItems_RelatedItemHistory, RelatedItemHistory | members-04.md | 9070 | 65 |
| PX.Objects.IN.S.INItemSite | EntityType |  | InventoryID, SiteID | 62 | 39 |  | PX_Objects_IN_S_INItemSite | members-04.md | 9136 | 107 |
| PX.Objects.IN.StoragePlace | EntityType | IN Storage Place | SiteID | 7 | 189 |  | PX_Objects_IN_StoragePlace, INStoragePlace, StoragePlace | members-04.md | 9244 | 202 |
| PX.Objects.IN.Turnover.INTurnoverCalc | EntityType | Turnover Calculation | BranchID, FromPeriodID, ToPeriodID | 17 | 6 |  | PX_Objects_IN_Turnover_INTurnoverCalc, TurnoverCalculation, INTurnoverCalc | members-04.md | 9447 | 30 |
| PX.Objects.IN.Turnover.INTurnoverCalcItem | EntityType | Turnover Calculation Item | BranchID, FromPeriodID, InventoryID, SiteID, ToPeriodID | 22 | 5 |  | PX_Objects_IN_Turnover_INTurnoverCalcItem, TurnoverCalculationItem, INTurnoverCalcItem | members-04.md | 9478 | 33 |
| PX.Objects.IN.Turnover.TurnoverCalcItem | EntityType | Turnover Calculation Item | BranchID, FromPeriodID, InventoryCD, SiteCD, ToPeriodID | 21 | 5 |  | PX_Objects_IN_Turnover_TurnoverCalcItem, TurnoverCalculationItem1, TurnoverCalcItem | members-04.md | 9512 | 32 |
| PX.Objects.IN.UnitOfMeasure | EntityType | Unit of Measure | Unit | 12 | 3 |  | PX_Objects_IN_UnitOfMeasure, UnitofMeasure | members-04.md | 9545 | 22 |
| PX.Objects.IN.WMSJob | EntityType | IN WMS Job | JobID | 19 | 5 |  | PX_Objects_IN_WMSJob, INWMSJob, WMSJob | members-04.md | 9568 | 31 |
| PX.Objects.Localizations.CA.APAdjustEFileRevision | EntityType | APAdjust EFileRevision | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, OrgBAccountID, Revision | 12 | 2 |  | PX_Objects_Localizations_CA_APAdjustEFileRevision, APAdjustEFileRevision | members-04.md | 9600 | 20 |
| PX.Objects.Localizations.CA.CanadianOrganizationSettings | EntityType | Canadian Organization Settings | OrgBAccountID | 3 | 1 |  | PX_Objects_Localizations_CA_CanadianOrganizationSettings, CanadianOrganizationSettings | members-04.md | 9621 | 10 |
| PX.Objects.Localizations.CA.CanadianVendor | EntityType | Canadian Vendor | VendorID | 8 | 1 |  | PX_Objects_Localizations_CA_CanadianVendor, CanadianVendor | members-04.md | 9632 | 15 |
| PX.Objects.Localizations.CA.T4AHistory | EntityType | T4A History | BoxNbr, BranchID, Revision, VendorID, Year | 7 | 0 |  | PX_Objects_Localizations_CA_T4AHistory, T4AHistory | members-04.md | 9648 | 13 |
| PX.Objects.Localizations.CA.T4AHistoryDetails | EntityType | T4A History Details | BoxNbr, BranchID, DocType, RefNbr, Revision, VendorID, Year | 9 | 0 |  | PX_Objects_Localizations_CA_T4AHistoryDetails, T4AHistoryDetails | members-04.md | 9662 | 15 |
| PX.Objects.Localizations.CA.T4AMasterTable | EntityType | T4A Master Table | OrgBAccountID, Revision, Year | 35 | 3 |  | PX_Objects_Localizations_CA_T4AMasterTable, T4AMasterTable | members-04.md | 9678 | 45 |
| PX.Objects.Localizations.CA.T4ASlip | EntityType | T4A Slip | BoxNbr, OrgBAccountID, Revision, VendorID, Year | 17 | 3 |  | PX_Objects_Localizations_CA_T4ASlip, T4ASlip | members-04.md | 9724 | 27 |
| PX.Objects.Localizations.CA.T5018EFileRow | EntityType | T5018 EFile Row | BAccountID, OrgBAccountID, Revision, Year | 12 | 1 |  | PX_Objects_Localizations_CA_T5018EFileRow, T5018EFileRow | members-04.md | 9752 | 19 |
| PX.Objects.Localizations.CA.T5018MasterTable | EntityType | T5018 Master Table | OrgBAccountID, Revision, Year | 32 | 4 |  | PX_Objects_Localizations_CA_T5018MasterTable, T5018MasterTable | members-04.md | 9772 | 43 |
| PX.Objects.Localizations.CA.T5018Transactions | EntityType | T5018Transactions | BranchID, DocDate, DocType, RefNbr, VendorID | 7 | 0 |  | PX_Objects_Localizations_CA_T5018Transactions, T5018Transactions | members-04.md | 9816 | 13 |
| PX.Objects.Localizations.CA.TaxRegistration | EntityType | Tax Registration | BAccountID, TaxID | 10 | 4 |  | PX_Objects_Localizations_CA_TaxRegistration, TaxRegistration | members-04.md | 9830 | 20 |
| PX.Objects.Localizations.GB.CISHistory | EntityType | CISHistory | BranchID, Revision, TaxPeriodID, VendorID | 17 | 3 |  | PX_Objects_Localizations_GB_CISHistory, CISHistory | members-04.md | 9851 | 26 |
| PX.Objects.Localizations.GB.CISHistoryDetails | EntityType | CISHistoryDetails | BranchID, DocType, RefNbr, Revision, TaxPeriodID, VendorID | 19 | 2 |  | PX_Objects_Localizations_GB_CISHistoryDetails, CISHistoryDetails | members-04.md | 9878 | 27 |
| PX.Objects.Localizations.GB.CISMasterTable | EntityType | CIS Master Table | OrgBAccountID, Revision, TaxPeriodID | 23 | 4 |  | PX_Objects_Localizations_GB_CISMasterTable, CISMasterTable | members-04.md | 9906 | 34 |
| PX.Objects.Localizations.GB.CISSubcontractor | EntityType | CIS Subcontractor | VendorID | 17 | 4 |  | PX_Objects_Localizations_GB_CISSubcontractor, CISSubcontractor | members-04.md | 9941 | 27 |
| PX.Objects.Localizations.GB.HMRC.DAC.BAccountMTDApplication | EntityType | MTD External Application | BAccountID | 2 | 0 |  | PX_Objects_Localizations_GB_HMRC_DAC_BAccountMTDApplication, MTDExternalApplication, BAccountMTDApplication | members-04.md | 9969 | 8 |
| PX.Objects.Localizations.GB.HMRCSubmission | EntityType | HMRC Submission | FormType, HMRCForm | 13 | 2 |  | PX_Objects_Localizations_GB_HMRCSubmission, HMRCSubmission | members-04.md | 9978 | 21 |
| PX.Objects.Localizations.GB.UKTaxReportingSettings | EntityType | UK Tax Reporting Settings | OrgBAccountID | 14 | 3 |  | PX_Objects_Localizations_GB_UKTaxReportingSettings, UKTaxReportingSettings | members-04.md | 10000 | 23 |
| PX.Objects.MN.DAC.Projections.MaterialMassProcessLine | EntityType | Material Line | LineNbr, SourceNoteID | 24 | 0 |  | PX_Objects_MN_DAC_Projections_MaterialMassProcessLine, MaterialLine, MaterialMassProcessLine | members-04.md | 10024 | 31 |
| PX.Objects.MN.MNMaterialList | EntityType | Material List | RefNbr | 16 | 13 |  | PX_Objects_MN_MNMaterialList, MaterialList, MNMaterialList | members-04.md | 10056 | 36 |
| PX.Objects.MN.MNMaterialListLine | EntityType | Material Line | LineNbr, MaterialListNoteID | 98 | 22 |  | PX_Objects_MN_MNMaterialListLine, MaterialLine1, MNMaterialListLine | members-04.md | 10093 | 127 |
| PX.Objects.MN.MNMaterialListLineSplit | EntityType | Material Line Split | LineNbr, MaterialListNoteID, SplitLineNbr | 57 | 15 |  | PX_Objects_MN_MNMaterialListLineSplit, MaterialLineSplit, MNMaterialListLineSplit | members-04.md | 10221 | 79 |
| PX.Objects.MN.MNMaterialListShipment | EntityType | Material List | MaterialListNoteID, ShipmentNoteID | 20 | 6 |  | PX_Objects_MN_MNMaterialListShipment, MaterialList1, MNMaterialListShipment | members-04.md | 10301 | 32 |
| PX.Objects.MN.MNMaterialListSiteStatusSelected | EntityType | Material Line Inventory Lookup Row | InventoryID | 33 | 4 |  | PX_Objects_MN_MNMaterialListSiteStatusSelected, MaterialLineInventoryLookupRow, MNMaterialListSiteStatusSelected | members-04.md | 10334 | 44 |
| PX.Objects.MN.POCreateExt.MNMaterialListLineProjection | EntityType | Material Line | LineNbr, MaterialListNoteID | 12 | 6 |  | PX_Objects_MN_POCreateExt_MNMaterialListLineProjection, MaterialLine2, MNMaterialListLineProjection | members-04.md | 10379 | 24 |
| PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection | EntityType | Material Line Split | LineNbr, MaterialListNoteID, SplitLineNbr | 10 | 2 |  | PX_Objects_MN_POCreateExt_MNMaterialListLineSplitProjection, MaterialLineSplit1, MNMaterialListLineSplitProjection | members-04.md | 10404 | 18 |
| PX.Objects.PJ.Common.DAC.ContactForCurrentProject | EntityType |  | ContactID | 10 | 107 |  | PX_Objects_PJ_Common_DAC_ContactForCurrentProject | members-04.md | 10423 | 122 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport | EntityType | Daily Field Report | DailyFieldReportCd | 46 | 20 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReport, DailyFieldReport | members-04.md | 10546 | 73 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder | EntityType | Daily Field Report Change Order | DailyFieldReportChangeOrderId | 3 | 2 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportChangeOrder, DailyFieldReportChangeOrder | members-04.md | 10620 | 11 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest | EntityType | Daily Field Report Change Request | DailyFieldReportChangeRequestId | 3 | 2 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportChangeRequest, DailyFieldReportChangeRequest | members-04.md | 10632 | 11 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration | EntityType | Daily Field Report Copy Configuration |  | 44 | 2 |  |  | members-04.md | 10644 | 51 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity | EntityType | Daily Field Report Employee Activity | DailyFieldReportId, EmployeeActivityId | 3 | 2 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEmployeeActivity, DailyFieldReportEmployeeActivity | members-04.md | 10696 | 11 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense | EntityType | Daily Field Report Employee Expenses | DailyFieldReportEmployeeExpenseId | 3 | 2 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEmployeeExpense, DailyFieldReportEmployeeExpenses, DailyFieldReportEmployeeExpense | members-04.md | 10708 | 11 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment | EntityType | Daily Field Report Equipment | DailyFieldReportId, EquipmentDetailLineNumber, EquipmentTimeCardCd | 4 | 3 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEquipment, DailyFieldReportEquipment | members-04.md | 10720 | 13 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory | EntityType | Daily Field Report History | DailyFieldReportHistoryId | 14 | 3 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportHistory, DailyFieldReportHistory | members-04.md | 10734 | 24 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote | EntityType | Daily Field Report Note | DailyFieldReportNoteId | 14 | 3 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportNote, DailyFieldReportNote | members-04.md | 10759 | 24 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog | EntityType | Daily Field Report Photo Log | DailyFieldReportPhotoLogId | 3 | 2 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportPhotoLog, DailyFieldReportPhotoLog | members-04.md | 10784 | 11 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet | EntityType | Daily Field Report Progress Worksheet | DailyFieldReportId, ProgressWorksheetId | 3 | 2 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProgressWorksheet, DailyFieldReportProgressWorksheet | members-04.md | 10796 | 11 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection | EntityType |  | DailyFieldReportCd | 2 | 14 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProjection | members-04.md | 10808 | 21 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue | EntityType | Daily Field Report Project Issue | DailyFieldReportProjectIssueId | 3 | 2 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProjectIssue, DailyFieldReportProjectIssue | members-04.md | 10830 | 11 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity | EntityType | Daily Field Report Subcontractor Activity | SubcontractorId | 22 | 5 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportSubcontractorActivity, DailyFieldReportSubcontractorActivity | members-04.md | 10842 | 34 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor | EntityType | Daily Field Report Visitor | DailyFieldReportVisitorId | 20 | 4 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportVisitor, DailyFieldReportVisitor | members-04.md | 10877 | 31 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather | EntityType | Daily Field Report Weather | DailyFieldReportWeatherId | 28 | 3 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportWeather, DailyFieldReportWeather | members-04.md | 10909 | 38 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection | EntityType | Daily Field Report Equipment | LineNbr, TimeCardCD | 7 | 4 | PX.Objects.EP.EPEquipmentDetail | PX_Objects_PJ_DailyFieldReports_PJ_DAC_EquipmentProjection, DailyFieldReportEquipment1, EquipmentProjection | members-04.md | 10948 | 18 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup | EntityType | Project Management Preferences - Weather Service Integration Settings |  | 9 | 2 |  |  | members-04.md | 10967 | 16 |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog | EntityType | Weather Processing Log | WeatherProcessingLogId | 17 | 2 |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_WeatherProcessingLog, WeatherProcessingLog | members-04.md | 10984 | 26 |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog | EntityType | Drawing Log | DrawingLogCd | 26 | 10 |  | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLog, DrawingLog | members-04.md | 11011 | 43 |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline | EntityType | Drawing Log Discipline | DrawingLogDisciplineId | 6 | 1 |  | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogDiscipline, DrawingLogDiscipline | members-04.md | 11055 | 14 |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogRevision | EntityType | Drawing Log Revision | DrawingLogId, DrawingLogRevisionId | 2 | 0 |  | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogRevision, DrawingLogRevision | members-04.md | 11070 | 8 |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup | EntityType | Drawing Log Preferences |  | 11 | 3 |  |  | members-04.md | 11079 | 19 |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus | EntityType | Drawing Log Status | StatusId | 4 | 1 |  | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogStatus, DrawingLogStatus | members-04.md | 11099 | 11 |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings | EntityType | Email Drawings | DrawingLogCd, RequestForInformationCd | 8 | 1 |  | PX_Objects_PJ_DrawingLogs_PJ_DAC_EmailDrawings, EmailDrawings | members-04.md | 11111 | 15 |
| PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo | EntityType | Photo | PhotoCd | 22 | 3 |  | PX_Objects_PJ_PhotoLogs_PJ_DAC_Photo, Photo | members-04.md | 11127 | 32 |
| PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog | EntityType | Photo Log | PhotoLogCd | 19 | 7 |  | PX_Objects_PJ_PhotoLogs_PJ_DAC_PhotoLog, PhotoLog | members-04.md | 11160 | 33 |
| PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup | EntityType | Photo Log Preferences |  | 12 | 4 |  |  | members-04.md | 11194 | 21 |
| PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus | EntityType | Photo Log Status | StatusId | 4 | 1 |  | PX_Objects_PJ_PhotoLogs_PJ_DAC_PhotoLogStatus, PhotoLogStatus | members-04.md | 11216 | 11 |
| PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass | EntityType | Project Management Class | ProjectManagementClassId | 16 | 4 |  | PX_Objects_PJ_ProjectManagement_PJ_DAC_ProjectManagementClass, ProjectManagementClass | members-04.md | 11228 | 27 |
| PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority | EntityType | Project Management Class Priority | PriorityId | 17 | 4 |  | PX_Objects_PJ_ProjectManagement_PJ_DAC_ProjectManagementClassPriority, ProjectManagementClassPriority | members-04.md | 11256 | 28 |
| PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup | EntityType | Project Management Preferences |  | 21 | 12 |  |  | members-04.md | 11285 | 38 |
| PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue | EntityType | Project Issue | ProjectIssueCd | 33 | 11 |  | PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssue, ProjectIssue | members-04.md | 11324 | 51 |
| PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueDrawingLog | EntityType | Project Issue Drawing Log | DrawingLogId, ProjectIssueId | 2 | 0 |  | PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssueDrawingLog, ProjectIssueDrawingLog | members-04.md | 11376 | 8 |
| PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueType | EntityType | Project Issue Type | ProjectIssueTypeId | 3 | 1 |  | PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssueType, ProjectIssueType | members-04.md | 11385 | 10 |
| PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation | EntityType | Request For Information | RequestForInformationCd | 42 | 14 |  | PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformation, RequestForInformation | members-04.md | 11396 | 63 |
| PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationAttachment | EntityType | Request For Information Attachment | FileID, RequestForInformationCd | 3 | 0 |  | PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationAttachment, RequestForInformationAttachment | members-04.md | 11460 | 9 |
| PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationDrawingLog | EntityType | Request For Information Drawing Log | DrawingLogId, RequestForInformationId | 2 | 0 |  | PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationDrawingLog, RequestForInformationDrawingLog | members-04.md | 11470 | 8 |
| PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation | EntityType | Request For Information Relation | RequestForInformationRelationId | 13 | 2 |  | PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationRelation, RequestForInformationRelation | members-04.md | 11479 | 22 |
| PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal | EntityType | Submittal | RevisionID, SubmittalID | 29 | 10 |  | PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittal, Submittal, PJSubmittal | members-04.md | 11502 | 46 |
| PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType | EntityType | Submittal Type | SubmittalTypeID | 10 | 3 |  | PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittalType, SubmittalType, PJSubmittalType | members-04.md | 11549 | 19 |
| PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem | EntityType | Submittal Workflow Item | LineNbr, RevisionID, SubmittalID | 23 | 4 |  | PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittalWorkflowItem, SubmittalWorkflowItem, PJSubmittalWorkflowItem | members-04.md | 11569 | 34 |
| PX.Objects.PM.DAC.PMItemCostStatusByCostCenter | EntityType | Item Cost Status by Cost Center | CostCenterID, InventoryID, SiteID | 5 | 11 |  | PX_Objects_PM_DAC_PMItemCostStatusByCostCenter, ItemCostStatusbyCostCenter, PMItemCostStatusByCostCenter | members-04.md | 11604 | 22 |
| PX.Objects.PM.DAC.PMReportRowsMultiplier | EntityType | Report Rows Multiplier | RecordID | 3 | 0 |  | PX_Objects_PM_DAC_PMReportRowsMultiplier, ReportRowsMultiplier, PMReportRowsMultiplier | members-04.md | 11627 | 10 |
| PX.Objects.PM.DAC.PMSelectedTag | EntityType | Project Selected Tag | TagID | 0 | 0 | PX.Data.Wiki.Tags.Tag | PX_Objects_PM_DAC_PMSelectedTag, ProjectSelectedTag, PMSelectedTag | members-04.md | 11638 | 6 |
| PX.Objects.PM.DAC.PMTagTemplate | EntityType | Project Tag Template | TemplateCD | 12 | 4 |  | PX_Objects_PM_DAC_PMTagTemplate, ProjectTagTemplate, PMTagTemplate | members-04.md | 11645 | 23 |
| PX.Objects.PM.DAC.PMTagTemplateItem | EntityType | Project Tag | TagID, TemplateID | 6 | 1 |  | PX_Objects_PM_DAC_PMTagTemplateItem, ProjectTag, PMTagTemplateItem | members-04.md | 11669 | 14 |
| PX.Objects.PM.DAC.Reports.PMRegister | EntityType | Project Register | Module, RefNbr | 5 | 1 |  | PX_Objects_PM_DAC_Reports_PMRegister, ProjectRegister, PMRegister | members-04.md | 11684 | 13 |
| PX.Objects.PM.Lite.PMBudget | EntityType | Budget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID | 15 | 10 |  | PX_Objects_PM_Lite_PMBudget, Budget1, PMBudget | members-04.md | 11698 | 31 |
| PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument | ComplexType |  |  | 12 | 0 |  |  | members-04.md | 11730 | 15 |
| PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList | EntityType | Material List | ProjectID | 5 | 1 |  | PX_Objects_PM_MaterialManagement_MaterialList_PMMaterialList, MaterialList2, PMMaterialList | members-04.md | 11746 | 12 |
| PX.Objects.PM.PMAccountGroup | EntityType | Account Group | GroupCD | 24 | 34 |  | PX_Objects_PM_PMAccountGroup, AccountGroup, PMAccountGroup | members-04.md | 11759 | 65 |
| PX.Objects.PM.PMAccountGroupRate | EntityType | PM Account Group Rate | AccountGroupID, RateCodeID, RateDefinitionID | 3 | 2 |  | PX_Objects_PM_PMAccountGroupRate, PMAccountGroupRate | members-04.md | 11825 | 11 |
| PX.Objects.PM.PMAccountTask | EntityType | PM Account Task | AccountID, ProjectID | 11 | 5 |  | PX_Objects_PM_PMAccountTask, PMAccountTask | members-04.md | 11837 | 23 |
| PX.Objects.PM.PMAddress | EntityType | PM Address | AddressID | 37 | 4 |  | PX_Objects_PM_PMAddress, PMAddress | members-04.md | 11861 | 48 |
| PX.Objects.PM.PMAllocation | EntityType | Allocation Rule | AllocationID | 12 | 5 |  | PX_Objects_PM_PMAllocation, AllocationRule, PMAllocation | members-04.md | 11910 | 24 |
| PX.Objects.PM.PMAllocationAuditTran | EntityType | PM Allocation Audit Transaction | AllocationID, SourceTranID, TranID | 3 | 0 |  | PX_Objects_PM_PMAllocationAuditTran, PMAllocationAuditTransaction, PMAllocationAuditTran | members-04.md | 11935 | 9 |
| PX.Objects.PM.PMAllocationDetail | EntityType | Allocation Rule Step | AllocationID, StepID | 55 | 20 |  | PX_Objects_PM_PMAllocationDetail, AllocationRuleStep, PMAllocationDetail | members-04.md | 11945 | 82 |
| PX.Objects.PM.PMAllocationSourceTran | EntityType | PM Allocation Source Transaction | AllocationID, StepID, TranID | 13 | 2 |  | PX_Objects_PM_PMAllocationSourceTran, PMAllocationSourceTransaction, PMAllocationSourceTran | members-04.md | 12028 | 21 |
| PX.Objects.PM.PMBilling | EntityType | Billing Rule | BillingID | 12 | 5 |  | PX_Objects_PM_PMBilling, BillingRule, PMBilling | members-04.md | 12050 | 24 |
| PX.Objects.PM.PMBillingAddress | EntityType | PM Billing Address | AddressID | 0 | 0 | PX.Objects.PM.PMAddress | PX_Objects_PM_PMBillingAddress, PMBillingAddress | members-04.md | 12075 | 6 |
| PX.Objects.PM.PMBillingContact | EntityType | PM Billing Contact | ContactID | 0 | 0 | PX.Objects.PM.PMContact | PX_Objects_PM_PMBillingContact, PMBillingContact | members-04.md | 12082 | 6 |
| PX.Objects.PM.PMBillingRecord | EntityType | Project Billing Record | BillingTag, ProjectID, RecordID | 10 | 2 |  | PX_Objects_PM_PMBillingRecord, ProjectBillingRecord, PMBillingRecord | members-04.md | 12089 | 19 |
| PX.Objects.PM.PMBillingRule | EntityType | Billing Rule Step | BillingID, StepID | 34 | 8 |  | PX_Objects_PM_PMBillingRule, BillingRuleStep, PMBillingRule | members-04.md | 12109 | 49 |
| PX.Objects.PM.PMBudget | EntityType | Project Budget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID | 79 | 10 |  | PX_Objects_PM_PMBudget, ProjectBudget, PMBudget1 | members-04.md | 12159 | 96 |
| PX.Objects.PM.PMBudgetedCostCode | EntityType | Budget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID | 7 | 7 |  | PX_Objects_PM_PMBudgetedCostCode, Budget2, PMBudgetedCostCode | members-04.md | 12256 | 20 |
| PX.Objects.PM.PMBudgetProduction | EntityType | Budget Production | AccountGroupID, CostCodeID, InventoryID, LineNbr, ProjectID, ProjectTaskID | 20 | 5 |  | PX_Objects_PM_PMBudgetProduction, BudgetProduction, PMBudgetProduction | members-04.md | 12277 | 32 |
| PX.Objects.PM.PMChangeOrder | EntityType | Change Order | RefNbr | 63 | 19 |  | PX_Objects_PM_PMChangeOrder, ChangeOrder, PMChangeOrder | members-04.md | 12310 | 89 |
| PX.Objects.PM.PMChangeOrderBudget | EntityType | Budget | LineNbr, RefNbr, Type | 34 | 13 |  | PX_Objects_PM_PMChangeOrderBudget, Budget3, PMChangeOrderBudget | members-04.md | 12400 | 54 |
| PX.Objects.PM.PMChangeOrderClass | EntityType | Change Order Class | ClassID | 16 | 4 |  | PX_Objects_PM_PMChangeOrderClass, ChangeOrderClass, PMChangeOrderClass | members-04.md | 12455 | 27 |
| PX.Objects.PM.PMChangeOrderCostBudget | EntityType | Budget | LineNbr, RefNbr, Type | 0 | 0 | PX.Objects.PM.PMChangeOrderBudget | PX_Objects_PM_PMChangeOrderCostBudget, Budget4, PMChangeOrderCostBudget | members-04.md | 12483 | 6 |
| PX.Objects.PM.PMChangeOrderLine | EntityType | Change Order Line | LineNbr, RefNbr | 29 | 18 |  | PX_Objects_PM_PMChangeOrderLine, ChangeOrderLine, PMChangeOrderLine | members-04.md | 12490 | 54 |
| PX.Objects.PM.PMChangeOrderRevenueBudget | EntityType | Budget | LineNbr, RefNbr, Type | 0 | 0 | PX.Objects.PM.PMChangeOrderBudget | PX_Objects_PM_PMChangeOrderRevenueBudget, Budget5, PMChangeOrderRevenueBudget | members-04.md | 12545 | 6 |
| PX.Objects.PM.PMChangeOrderTax | EntityType | PMChangeOrderTax | LineNbr, RefNbr, TaxID | 19 | 8 |  | PX_Objects_PM_PMChangeOrderTax, PMChangeOrderTax | members-04.md | 12552 | 34 |
| PX.Objects.PM.PMChangeOrderTaxTran | EntityType | PMChangeOrderTaxTran | RecordID, TaxID | 24 | 5 |  | PX_Objects_PM_PMChangeOrderTaxTran, PMChangeOrderTaxTran | members-04.md | 12587 | 36 |
| PX.Objects.PM.PMChangeRequest | EntityType | Change Request | RefNbr | 56 | 17 |  | PX_Objects_PM_PMChangeRequest, ChangeRequest, PMChangeRequest | members-04.md | 12624 | 80 |
| PX.Objects.PM.PMChangeRequestAudit | EntityType | Change Request Audit | RecordID | 11 | 2 |  | PX_Objects_PM_PMChangeRequestAudit, ChangeRequestAudit, PMChangeRequestAudit | members-04.md | 12705 | 19 |
| PX.Objects.PM.PMChangeRequestLine | EntityType | Change Request | LineNbr, RefNbr | 34 | 16 |  | PX_Objects_PM_PMChangeRequestLine, ChangeRequest1, PMChangeRequestLine | members-04.md | 12725 | 57 |
| PX.Objects.PM.PMChangeRequestLineTax | EntityType | Change Request Line Tax | LineNbr, RefNbr, TaxID, Type | 0 | 0 | PX.Objects.PM.PMChangeRequestTax | PX_Objects_PM_PMChangeRequestLineTax, ChangeRequestLineTax, PMChangeRequestLineTax | members-04.md | 12783 | 6 |
| PX.Objects.PM.PMChangeRequestLineTaxTran | EntityType | PChange Request Line Tax Tran | RecordID, TaxID | 0 | 0 | PX.Objects.PM.PMChangeRequestTaxTran | PX_Objects_PM_PMChangeRequestLineTaxTran, PChangeRequestLineTaxTran, PMChangeRequestLineTaxTran | members-04.md | 12790 | 6 |
| PX.Objects.PM.PMChangeRequestMarkup | EntityType | Markup | LineNbr, RefNbr | 20 | 7 |  | PX_Objects_PM_PMChangeRequestMarkup, Markup1, PMChangeRequestMarkup | members-04.md | 12797 | 34 |
| PX.Objects.PM.PMChangeRequestMarkupTax | EntityType | Change Request Markup Tax | LineNbr, RefNbr, TaxID, Type | 0 | 0 | PX.Objects.PM.PMChangeRequestTax | PX_Objects_PM_PMChangeRequestMarkupTax, ChangeRequestMarkupTax, PMChangeRequestMarkupTax | members-04.md | 12832 | 6 |
| PX.Objects.PM.PMChangeRequestMarkupTaxTran | EntityType | PChange Request Markup Tax Tran | RecordID, TaxID | 0 | 0 | PX.Objects.PM.PMChangeRequestTaxTran | PX_Objects_PM_PMChangeRequestMarkupTaxTran, PChangeRequestMarkupTaxTran, PMChangeRequestMarkupTaxTran | members-04.md | 12839 | 6 |
| PX.Objects.PM.PMChangeRequestTax | EntityType | Change Request Tax | LineNbr, RefNbr, TaxID, Type | 17 | 7 |  | PX_Objects_PM_PMChangeRequestTax, ChangeRequestTax, PMChangeRequestTax | members-04.md | 12846 | 31 |
| PX.Objects.PM.PMChangeRequestTaxTran | EntityType | PChange Request Tax Tran | RecordID, TaxID | 24 | 5 |  | PX_Objects_PM_PMChangeRequestTaxTran, PChangeRequestTaxTran, PMChangeRequestTaxTran | members-04.md | 12878 | 36 |
| PX.Objects.PM.PMChangeRequestTotalTaxTran | EntityType | PChange Request Total Tax Tran | RecordID, TaxID | 0 | 0 | PX.Objects.PM.PMChangeRequestTaxTran | PX_Objects_PM_PMChangeRequestTotalTaxTran, PChangeRequestTotalTaxTran, PMChangeRequestTotalTaxTran | members-04.md | 12915 | 6 |
| PX.Objects.PM.PMCommitment | EntityType | Commitment Record | CommitmentID | 27 | 10 |  | PX_Objects_PM_PMCommitment, CommitmentRecord, PMCommitment | members-04.md | 12922 | 44 |
| PX.Objects.PM.PMContact | EntityType | Project Contact | ContactID | 27 | 7 |  | PX_Objects_PM_PMContact, ProjectContact, PMContact | members-05.md | 3 | 41 |
| PX.Objects.PM.PMCostBudget | EntityType | Project Cost Budget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID | 0 | 0 | PX.Objects.PM.PMBudget | PX_Objects_PM_PMCostBudget, ProjectCostBudget, PMCostBudget | members-05.md | 45 | 6 |
| PX.Objects.PM.PMCostCode | EntityType | Cost Code | CostCodeCD | 15 | 57 |  | PX_Objects_PM_PMCostCode, CostCode, PMCostCode | members-05.md | 52 | 79 |
| PX.Objects.PM.PMCostProjection | EntityType | Cost Projection | ProjectID, RevisionID | 36 | 7 |  | PX_Objects_PM_PMCostProjection, CostProjection, PMCostProjection | members-05.md | 132 | 50 |
| PX.Objects.PM.PMCostProjectionByDate | EntityType | Cost Projection By Date | RefNbr | 74 | 8 |  | PX_Objects_PM_PMCostProjectionByDate, CostProjectionByDate, PMCostProjectionByDate | members-05.md | 183 | 89 |
| PX.Objects.PM.PMCostProjectionByDateLine | EntityType | Cost Projection By Date Line | LineNbr, RefNbr | 79 | 10 |  | PX_Objects_PM_PMCostProjectionByDateLine, CostProjectionByDateLine, PMCostProjectionByDateLine | members-05.md | 273 | 96 |
| PX.Objects.PM.PMCostProjectionClass | EntityType | Cost Projection Class | ClassID | 15 | 3 |  | PX_Objects_PM_PMCostProjectionClass, CostProjectionClass, PMCostProjectionClass | members-05.md | 370 | 25 |
| PX.Objects.PM.PMCostProjectionLine | EntityType | Cost Projection Line | LineNbr, ProjectID, RevisionID | 34 | 9 |  | PX_Objects_PM_PMCostProjectionLine, CostProjectionLine, PMCostProjectionLine | members-05.md | 396 | 50 |
| PX.Objects.PM.PMEmployeeRate | EntityType | PM Item Employee | EmployeeID, RateCodeID, RateDefinitionID | 3 | 2 |  | PX_Objects_PM_PMEmployeeRate, PMItemEmployee, PMEmployeeRate | members-05.md | 447 | 11 |
| PX.Objects.PM.PMForecast | EntityType | Budget Forecast | ProjectID, RevisionID | 13 | 4 |  | PX_Objects_PM_PMForecast, BudgetForecast, PMForecast | members-05.md | 459 | 24 |
| PX.Objects.PM.PMForecastDetail | EntityType | Budget Forecast Detail | AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID, RevisionID | 21 | 10 |  | PX_Objects_PM_PMForecastDetail, BudgetForecastDetail, PMForecastDetail | members-05.md | 484 | 38 |
| PX.Objects.PM.PMForecastHistory | EntityType | Budget Forecast History | AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID | 13 | 0 |  | PX_Objects_PM_PMForecastHistory, BudgetForecastHistory, PMForecastHistory | members-05.md | 523 | 19 |
| PX.Objects.PM.PMForecastProject | EntityType | Project | ContractID | 11 | 141 |  | PX_Objects_PM_PMForecastProject, Project1, PMForecastProject | members-05.md | 543 | 159 |
| PX.Objects.PM.PMHistory | EntityType | Project History | AccountGroupID, BranchID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID | 20 | 1 |  | PX_Objects_PM_PMHistory, ProjectHistory, PMHistory | members-05.md | 703 | 28 |
| PX.Objects.PM.PMHistoryByDate | EntityType | Project History By Date | AccountGroupID, CostCodeID, Date, InventoryID, PeriodID, ProjectID, ProjectTaskID | 21 | 6 |  | PX_Objects_PM_PMHistoryByDate, ProjectHistoryByDate, PMHistoryByDate | members-05.md | 732 | 34 |
| PX.Objects.PM.PMItemRate | EntityType | PM Item Rate | InventoryID, RateCodeID, RateDefinitionID | 3 | 2 |  | PX_Objects_PM_PMItemRate, PMItemRate | members-05.md | 767 | 11 |
| PX.Objects.PM.PMLaborCostRate | EntityType | Labor Cost Rates | RecordID | 25 | 10 |  | PX_Objects_PM_PMLaborCostRate, LaborCostRates, PMLaborCostRate | members-05.md | 779 | 42 |
| PX.Objects.PM.PMMarkup | EntityType | Markup | LineNbr, ProjectID | 17 | 8 |  | PX_Objects_PM_PMMarkup, Markup2, PMMarkup | members-05.md | 822 | 32 |
| PX.Objects.PM.PMPOHistoryByDate | EntityType | Project Commitment History | COLineNbr, CONbr, Date, POLineNbr, POOrderNbr, POOrderType, RecordType | 26 | 8 |  | PX_Objects_PM_PMPOHistoryByDate, ProjectCommitmentHistory, PMPOHistoryByDate | members-05.md | 855 | 40 |
| PX.Objects.PM.PMProfitHistoryByDate | EntityType | PMProfitHistoryByDate | AccountGroupID, ProjectID, TaskID | 10 | 2 |  | PX_Objects_PM_PMProfitHistoryByDate, PMProfitHistoryByDate | members-05.md | 896 | 18 |
| PX.Objects.PM.PMProforma | EntityType | Pro Forma Invoice | RefNbr, RevisionID | 64 | 19 |  | PX_Objects_PM_PMProforma, ProFormaInvoice, PMProforma | members-05.md | 915 | 90 |
| PX.Objects.PM.PMProformaLine | EntityType | Pro Forma Line | LineNbr, RefNbr, RevisionID | 56 | 18 |  | PX_Objects_PM_PMProformaLine, ProFormaLine, PMProformaLine | members-05.md | 1006 | 81 |
| PX.Objects.PM.PMProformaLineWithPrevious | EntityType | Pro Forma Line | LineNbr, RefNbr, RevisionID | 1 | 0 | PX.Objects.PM.PMProformaLine | PX_Objects_PM_PMProformaLineWithPrevious, ProFormaLine1, PMProformaLineWithPrevious | members-05.md | 1088 | 9 |
| PX.Objects.PM.PMProformaProgressLine | EntityType | Pro Forma Line | LineNbr, RefNbr, RevisionID | 0 | 0 | PX.Objects.PM.PMProformaLine | PX_Objects_PM_PMProformaProgressLine, ProFormaLine2, PMProformaProgressLine | members-05.md | 1098 | 6 |
| PX.Objects.PM.PMProformaRevision | EntityType | Pro Forma Invoice Revision | RefNbr, RevisionID | 12 | 6 |  | PX_Objects_PM_PMProformaRevision, ProFormaInvoiceRevision, PMProformaRevision | members-05.md | 1105 | 24 |
| PX.Objects.PM.PMProformaTransactLine | EntityType | Pro Forma Line | LineNbr, RefNbr, RevisionID | 7 | 0 | PX.Objects.PM.PMProformaLine | PX_Objects_PM_PMProformaTransactLine, ProFormaLine3, PMProformaTransactLine | members-05.md | 1130 | 15 |
| PX.Objects.PM.PMProgressLineTotal | EntityType | Pro Forma Line | AccountGroupID, ProjectID, RefNbr, TaskID | 12 | 6 |  | PX_Objects_PM_PMProgressLineTotal, ProFormaLine4, PMProgressLineTotal | members-05.md | 1146 | 24 |
| PX.Objects.PM.PMProgressWorksheet | EntityType | Progress Worksheet | RefNbr | 23 | 6 |  | PX_Objects_PM_PMProgressWorksheet, ProgressWorksheet, PMProgressWorksheet | members-05.md | 1171 | 36 |
| PX.Objects.PM.PMProgressWorksheetCostLine | EntityType | Progress Worksheet Cost Line | LineNbr, RefNbr | 0 | 0 | PX.Objects.PM.PMProgressWorksheetLine | PX_Objects_PM_PMProgressWorksheetCostLine, ProgressWorksheetCostLine, PMProgressWorksheetCostLine | members-05.md | 1208 | 6 |
| PX.Objects.PM.PMProgressWorksheetLine | EntityType | Progress Worksheet Line | LineNbr, RefNbr | 26 | 11 |  | PX_Objects_PM_PMProgressWorksheetLine, ProgressWorksheetLine, PMProgressWorksheetLine | members-05.md | 1215 | 44 |
| PX.Objects.PM.PMProgressWorksheetRevenueLine | EntityType | Progress Worksheet Revenue Line | LineNbr, RefNbr | 0 | 0 | PX.Objects.PM.PMProgressWorksheetLine | PX_Objects_PM_PMProgressWorksheetRevenueLine, ProgressWorksheetRevenueLine, PMProgressWorksheetRevenueLine | members-05.md | 1260 | 6 |
| PX.Objects.PM.PMProject | EntityType | Project | BaseType, ContractCD | 21 | 154 | PX.Objects.CT.Contract | PX_Objects_PM_PMProject, Project, PMProject | members-05.md | 1267 | 183 |
| PX.Objects.PM.PMProjectBudgetHistory | EntityType | Project Budget History | AccountGroupID, ChangeOrderRefNbr, CostCodeID, Date, InventoryID, ProjectID, TaskID | 19 | 9 |  | PX_Objects_PM_PMProjectBudgetHistory, ProjectBudgetHistory, PMProjectBudgetHistory | members-05.md | 1451 | 34 |
| PX.Objects.PM.PMProjectBudgetProfitHistory | EntityType | PMProjectBudgetProfitHistory | AccountGroupID, ProjectID, TaskID | 14 | 4 |  | PX_Objects_PM_PMProjectBudgetProfitHistory, PMProjectBudgetProfitHistory | members-05.md | 1486 | 24 |
| PX.Objects.PM.PMProjectContact | EntityType | Project Contact | ContactID, ProjectID | 15 | 6 |  | PX_Objects_PM_PMProjectContact, ProjectContact1, PMProjectContact | members-05.md | 1511 | 28 |
| PX.Objects.PM.PMProjectCostForecastTotal | EntityType | Contract Total | ProjectID | 8 | 1 |  | PX_Objects_PM_PMProjectCostForecastTotal, ContractTotal, PMProjectCostForecastTotal | members-05.md | 1540 | 16 |
| PX.Objects.PM.PMProjectCostSpread | EntityType | Project Monthly Cost Spread | RefNbr | 34 | 7 |  | PX_Objects_PM_PMProjectCostSpread, ProjectMonthlyCostSpread, PMProjectCostSpread | members-05.md | 1557 | 48 |
| PX.Objects.PM.PMProjectCostSpreadLine | EntityType | Project Monthly Cost Spread Line | LineNbr, RefNbr | 30 | 4 |  | PX_Objects_PM_PMProjectCostSpreadLine, ProjectMonthlyCostSpreadLine, PMProjectCostSpreadLine | members-05.md | 1606 | 41 |
| PX.Objects.PM.PMProjectGroup | EntityType | Project Group | ProjectGroupID | 14 | 3 |  | PX_Objects_PM_PMProjectGroup, ProjectGroup, PMProjectGroup | members-05.md | 1648 | 24 |
| PX.Objects.PM.PMProjectRate | EntityType | PM Project Rate | ProjectCD, RateCodeID, RateDefinitionID | 3 | 2 |  | PX_Objects_PM_PMProjectRate, PMProjectRate | members-05.md | 1673 | 11 |
| PX.Objects.PM.PMProjectRevenueTotal | EntityType | Contract Total | ProjectID | 9 | 1 |  | PX_Objects_PM_PMProjectRevenueTotal, ContractTotal1, PMProjectRevenueTotal | members-05.md | 1685 | 17 |
| PX.Objects.PM.PMProjectTemplate | EntityType | Project Template | ContractCD | 10 | 144 |  | PX_Objects_PM_PMProjectTemplate, ProjectTemplate, PMProjectTemplate | members-05.md | 1703 | 160 |
| PX.Objects.PM.PMProjectUnion | EntityType | Project Union Locals | ProjectID, UnionID | 3 | 2 |  | PX_Objects_PM_PMProjectUnion, ProjectUnionLocals, PMProjectUnion | members-05.md | 1864 | 11 |
| PX.Objects.PM.PMQuote | EntityType | Project Quote | QuoteNbr | 106 | 15 |  | PX_Objects_PM_PMQuote, ProjectQuote, PMQuote | members-05.md | 1876 | 128 |
| PX.Objects.PM.PMQuoteTask | EntityType | Project Task | QuoteID, TaskCD | 16 | 4 |  | PX_Objects_PM_PMQuoteTask, ProjectTask1, PMQuoteTask | members-05.md | 2005 | 27 |
| PX.Objects.PM.PMRate | EntityType | Rate | LineNbr, RateCodeID, RateDefinitionID | 15 | 3 |  | PX_Objects_PM_PMRate, Rate, PMRate | members-05.md | 2033 | 25 |
| PX.Objects.PM.PMRateDefinition | EntityType | Rate Lookup Rule | RateDefinitionID | 19 | 3 |  | PX_Objects_PM_PMRateDefinition, RateLookupRule, PMRateDefinition | members-05.md | 2059 | 29 |
| PX.Objects.PM.PMRateSequence | EntityType | Rate Lookup Rule Sequence | RateCodeID, RateTableID, RateTypeID, Sequence | 16 | 11 |  | PX_Objects_PM_PMRateSequence, RateLookupRuleSequence, PMRateSequence | members-05.md | 2089 | 34 |
| PX.Objects.PM.PMRateTable | EntityType | Rate Table Code | RateTableID | 11 | 5 |  | PX_Objects_PM_PMRateTable, RateTableCode, PMRateTable | members-05.md | 2124 | 23 |
| PX.Objects.PM.PMRateType | EntityType | Rate Type | RateTypeID | 11 | 5 |  | PX_Objects_PM_PMRateType, RateType, PMRateType | members-05.md | 2148 | 23 |
| PX.Objects.PM.PMRecurringItem | EntityType | Recurring Items | InventoryID, ProjectID, TaskID | 22 | 9 |  | PX_Objects_PM_PMRecurringItem, RecurringItems, PMRecurringItem | members-05.md | 2172 | 38 |
| PX.Objects.PM.PMRegister | EntityType | Project Register | Module, RefNbr | 25 | 1 |  | PX_Objects_PM_PMRegister, ProjectRegister1, PMRegister1 | members-05.md | 2211 | 33 |
| PX.Objects.PM.PMRetainageStep | EntityType | Retainage Step | LineNbr, ProjectID | 13 | 3 |  | PX_Objects_PM_PMRetainageStep, RetainageStep, PMRetainageStep | members-05.md | 2245 | 23 |
| PX.Objects.PM.PMRevenueBudget | EntityType | Project Revenue Budget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID | 4 | 0 | PX.Objects.PM.PMBudget | PX_Objects_PM_PMRevenueBudget, ProjectRevenueBudget, PMRevenueBudget | members-05.md | 2269 | 12 |
| PX.Objects.PM.PMRevenuePercentageCalculationRule | EntityType | Revenue Percentage Calculation Rule | RuleID | 15 | 4 |  | PX_Objects_PM_PMRevenuePercentageCalculationRule, RevenuePercentageCalculationRule, PMRevenuePercentageCalculationRule | members-05.md | 2282 | 26 |
| PX.Objects.PM.PMSetup | EntityType | Project Preferences |  | 58 | 50 |  |  | members-05.md | 2309 | 113 |
| PX.Objects.PM.PMShippingAddress | EntityType | PM Address | AddressID | 0 | 0 | PX.Objects.PM.PMAddress | PX_Objects_PM_PMShippingAddress, PMAddress1, PMShippingAddress | members-05.md | 2423 | 6 |
| PX.Objects.PM.PMShippingContact | EntityType | Project Contact | ContactID | 0 | 0 | PX.Objects.PM.PMContact | PX_Objects_PM_PMShippingContact, ProjectContact2, PMShippingContact | members-05.md | 2430 | 6 |
| PX.Objects.PM.PMSiteAddress | EntityType | PM Address | AddressID | 0 | 0 | PX.Objects.PM.PMAddress | PX_Objects_PM_PMSiteAddress, PMAddress2, PMSiteAddress | members-05.md | 2437 | 6 |
| PX.Objects.PM.PMTask | EntityType | Project Task | ProjectID, TaskCD | 51 | 126 |  | PX_Objects_PM_PMTask, ProjectTask, PMTask | members-05.md | 2444 | 184 |
| PX.Objects.PM.PMTaskRate | EntityType | PM Task Rate | RateCodeID, RateDefinitionID, TaskCD | 3 | 2 |  | PX_Objects_PM_PMTaskRate, PMTaskRate | members-05.md | 2629 | 11 |
| PX.Objects.PM.PMTaskTotal | EntityType | Task Total | ProjectID, TaskID | 14 | 0 |  | PX_Objects_PM_PMTaskTotal, TaskTotal, PMTaskTotal | members-05.md | 2641 | 21 |
| PX.Objects.PM.PMTax | EntityType | PM Tax Detail | LineNbr, RefNbr, RevisionID, TaxID | 22 | 6 |  | PX_Objects_PM_PMTax, PMTaxDetail, PMTax | members-05.md | 2663 | 35 |
| PX.Objects.PM.PMTaxTran | EntityType | PM Tax | LineNbr, RecordID, RefNbr, RevisionID, TaxID | 25 | 5 |  | PX_Objects_PM_PMTaxTran, PMTax1, PMTaxTran | members-05.md | 2699 | 36 |
| PX.Objects.PM.PMTran | EntityType | Project Transaction | TranID | 90 | 36 |  | PX_Objects_PM_PMTran, ProjectTransaction, PMTran | members-05.md | 2736 | 133 |
| PX.Objects.PM.PMTranConsolidated | ComplexType |  |  | 49 | 0 |  |  | members-05.md | 2870 | 52 |
| PX.Objects.PM.PMTransferRule | EntityType | Rollup Rule | TransferRuleID | 17 | 5 |  | PX_Objects_PM_PMTransferRule, RollupRule, PMTransferRule | members-05.md | 2923 | 29 |
| PX.Objects.PM.PMTransferRuleAccountGroupMap | EntityType | Rollup Rule Account Group Map | SourceAccountGroupID, TransferRuleID | 3 | 3 |  | PX_Objects_PM_PMTransferRuleAccountGroupMap, RollupRuleAccountGroupMap, PMTransferRuleAccountGroupMap | members-05.md | 2953 | 12 |
| PX.Objects.PM.PMTransferRuleCostCodeMap | EntityType | Rollup Rule Cost Code Map | SourceCostCodeID, TransferRuleID | 2 | 1 |  | PX_Objects_PM_PMTransferRuleCostCodeMap, RollupRuleCostCodeMap, PMTransferRuleCostCodeMap | members-05.md | 2966 | 9 |
| PX.Objects.PM.PMUnion | EntityType | Union Local | UnionID | 13 | 19 |  | PX_Objects_PM_PMUnion, UnionLocal, PMUnion | members-05.md | 2976 | 39 |
| PX.Objects.PM.PMWipAdjustment | EntityType | Project WIP Adjustment | RefNbr | 45 | 15 |  | PX_Objects_PM_PMWipAdjustment, ProjectWIPAdjustment, PMWipAdjustment | members-05.md | 3016 | 67 |
| PX.Objects.PM.PMWipAdjustmentLine | EntityType | Project WIP Adjustment Line | LineNbr, RefNbr | 70 | 13 |  | PX_Objects_PM_PMWipAdjustmentLine, ProjectWIPAdjustmentLine, PMWipAdjustmentLine | members-05.md | 3084 | 90 |
| PX.Objects.PM.PMWorkCode | EntityType | WorkCode | WorkCodeID | 12 | 17 |  | PX_Objects_PM_PMWorkCode, WorkCode, PMWorkCode | members-05.md | 3175 | 36 |
| PX.Objects.PM.PMWorkCodeCostCodeRange | EntityType | Workers' Compensation Code Cost Code Range | LineNbr, WorkCodeID | 10 | 5 |  | PX_Objects_PM_PMWorkCodeCostCodeRange, WorkersCompensationCodeCostCodeRange, PMWorkCodeCostCodeRange | members-05.md | 3212 | 21 |
| PX.Objects.PM.PMWorkCodeLaborItemSource | EntityType | Workers' Compensation Labor Item Source | LaborItemID, WorkCodeID | 8 | 4 |  | PX_Objects_PM_PMWorkCodeLaborItemSource, WorkersCompensationLaborItemSource, PMWorkCodeLaborItemSource | members-05.md | 3234 | 18 |
| PX.Objects.PM.PMWorkCodeProjectTaskSource | EntityType | Workers' Compensation Project Task Source | LineNbr, WorkCodeID | 8 | 6 |  | PX_Objects_PM_PMWorkCodeProjectTaskSource, WorkersCompensationProjectTaskSource, PMWorkCodeProjectTaskSource | members-05.md | 3253 | 20 |
| PX.Objects.PM.POLinePM | EntityType | PO Line | LineNbr, OrderNbr, OrderType | 37 | 22 |  | PX_Objects_PM_POLinePM, POLine, POLinePM | members-05.md | 3274 | 66 |
| PX.Objects.PM.POOrderPM | EntityType | Purchase Order | OrderNbr, OrderType | 4 | 47 |  | PX_Objects_PM_POOrderPM, PurchaseOrder1, POOrderPM | members-05.md | 3341 | 57 |
| PX.Objects.PM.Project.Cashflow.PMProjectAPDetails | ComplexType |  |  | 81 | 0 |  |  | members-05.md | 3399 | 84 |
| PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail | ComplexType |  |  | 68 | 0 |  |  | members-05.md | 3484 | 71 |
| PX.Objects.PM.Project.Cashflow.PMProjectARTranPost | ComplexType |  |  | 60 | 0 |  |  | members-05.md | 3556 | 63 |
| PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail | EntityType | Project AR History | DocType, ID, LineNbr, RefNbr, SourceLineNbr | 65 | 3 |  | PX_Objects_PM_Project_Cashflow_PMProjectARTranPostDetail, ProjectARHistory, PMProjectARTranPostDetail | members-05.md | 3620 | 75 |
| PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate | ComplexType |  |  | 39 | 0 |  |  | members-05.md | 3696 | 42 |
| PX.Objects.PM.ProjectAPTran | EntityType | AP Transactions | ProjectID, RefNbr, TranType | 5 | 4 |  | PX_Objects_PM_ProjectAPTran, APTransactions1, ProjectAPTran | members-05.md | 3739 | 15 |
| PX.Objects.PM.ProjectARTran | EntityType | AR Transactions | ProjectID, RefNbr, TranType | 5 | 7 |  | PX_Objects_PM_ProjectARTran, ARTransactions1, ProjectARTran | members-05.md | 3755 | 18 |
| PX.Objects.PM.ProjectCASplit | EntityType | CA Transaction Details | ProjectID, RefNbr, TranType | 3 | 1 |  | PX_Objects_PM_ProjectCASplit, CATransactionDetails1, ProjectCASplit | members-05.md | 3774 | 10 |
| PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile | EntityType | Linked File | FileID | 17 | 0 | PX.SM.UploadFileWithTags | PX_Objects_PM_ProjectFiles_FileEntryForms_PMLinkedFile, LinkedFile, PMLinkedFile | members-05.md | 3785 | 25 |
| PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity | EntityType | Project Entity | LinkedDocumentNoteID, LinkedEntityNoteID, ProjectID | 12 | 2 |  | PX_Objects_PM_ProjectFiles_ProjectEntities_PMProjectEntity, ProjectEntity, PMProjectEntity | members-05.md | 3811 | 21 |
| PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity | EntityType | Vendor Entity | BAccountID, LinkedDocumentNoteID, LinkedEntityNoteID | 12 | 2 |  | PX_Objects_PM_ProjectFiles_VendorEntities_PMVendorEntity, VendorEntity, PMVendorEntity | members-05.md | 3833 | 21 |
| PX.Objects.PM.ProjectGLTran | EntityType | GL Transaction | BatchNbr, Module, ProjectID | 3 | 2 |  | PX_Objects_PM_ProjectGLTran, GLTransaction1, ProjectGLTran | members-05.md | 3855 | 11 |
| PX.Objects.PM.ProjectINTran | EntityType | IN Transaction | DocType, ProjectID, RefNbr | 3 | 4 |  | PX_Objects_PM_ProjectINTran, INTransaction1, ProjectINTran | members-05.md | 3867 | 13 |
| PX.Objects.PM.ProjectParentChild.PMChildProject | EntityType | Child Project | BaseType, ContractCD | 0 | 0 | PX.Objects.PM.PMProject | PX_Objects_PM_ProjectParentChild_PMChildProject, ChildProject, PMChildProject | members-05.md | 3881 | 6 |
| PX.Objects.PM.ProjectParentChild.PMChildTask | EntityType | Child Task | ProjectID, TaskCD | 1 | 0 | PX.Objects.PM.PMTask | PX_Objects_PM_ProjectParentChild_PMChildTask, ChildTask, PMChildTask | members-05.md | 3888 | 8 |
| PX.Objects.PM.ProjectParentChild.PMParentProject | EntityType | Child Project | BaseType, ContractCD | 0 | 0 | PX.Objects.PM.PMProject | PX_Objects_PM_ProjectParentChild_PMParentProject, ChildProject1, PMParentProject | members-05.md | 3897 | 6 |
| PX.Objects.PM.ProjectPMTran | EntityType | Project Transaction | ProjectID, RefNbr, TranType | 5 | 5 |  | PX_Objects_PM_ProjectPMTran, ProjectTransaction1, ProjectPMTran | members-05.md | 3904 | 16 |
| PX.Objects.PMRole | EntityType | Project Role |  | 4 | 1 |  |  | members-05.md | 3921 | 10 |
| PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc | EntityType | Purchase Order to Accounts Payable Document Link | DocType, PONbr, POType, RefNbr | 13 | 24 |  | PX_Objects_PO_DAC_Projections_POBlanketOrderAPDoc, PurchaseOrdertoAccountsPayableDocumentLink, POBlanketOrderAPDoc | members-05.md | 3932 | 44 |
| PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder | EntityType | Purchase Blanket Order to Purchase Order Link | OrderNbr, OrderType, PONbr, POType | 10 | 2 |  | PX_Objects_PO_DAC_Projections_POBlanketOrderPOOrder, PurchaseBlanketOrdertoPurchaseOrderLink, POBlanketOrderPOOrder | members-05.md | 3977 | 19 |
| PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt | EntityType | Purchase Blanket Order to Purchase Receipt Link | OrderNbr, OrderType, PONbr, POType, ReceiptNbr, ReceiptType | 9 | 3 |  | PX_Objects_PO_DAC_Projections_POBlanketOrderPOReceipt, PurchaseBlanketOrdertoPurchaseReceiptLink, POBlanketOrderPOReceipt | members-05.md | 3997 | 18 |
| PX.Objects.PO.DAC.Projections.POReceiptLineAdd | EntityType | Purchase Receipt Line | LineNbr, ReceiptNbr, ReceiptType | 0 | 0 | PX.Objects.PO.POReceiptLineS | PX_Objects_PO_DAC_Projections_POReceiptLineAdd | members-05.md | 4016 | 6 |
| PX.Objects.PO.DropShipPOLine | EntityType | PO Drop-Ship Line | LineNbr, OrderNbr, OrderType | 12 | 18 |  | PX_Objects_PO_DropShipPOLine, PODropShipLine, DropShipPOLine | members-05.md | 4023 | 36 |
| PX.Objects.PO.INTransitLineStatusSO | EntityType |  | SOShipmentLineNbr, SOShipmentNbr | 18 | 5 |  | PX_Objects_PO_INTransitLineStatusSO | members-05.md | 4060 | 28 |
| PX.Objects.PO.LandedCostCode | EntityType | Landed Cost Code | LandedCostCodeID | 17 | 17 |  | PX_Objects_PO_LandedCostCode, LandedCostCode | members-05.md | 4089 | 41 |
| PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail | EntityType | Landed Costs Receipt | LCDocType, LCRefNbr, POReceiptNbr, POReceiptType | 18 | 7 | PX.Objects.PO.POLandedCostReceipt | PX_Objects_PO_LandedCosts_POReceiptLandedCostDetail, LandedCostsReceipt, POReceiptLandedCostDetail | members-05.md | 4131 | 33 |
| PX.Objects.PO.LandedCosts.POReceiptLineAdd | EntityType | Purchase Receipt Line | LineNbr, ReceiptNbr, ReceiptType | 33 | 23 |  | PX_Objects_PO_LandedCosts_POReceiptLineAdd, PurchaseReceiptLine, POReceiptLineAdd | members-05.md | 4165 | 62 |
| PX.Objects.PO.LinkLineOrder | EntityType |  | OrderLineNbr, OrderNbr, OrderType | 19 | 10 |  | PX_Objects_PO_LinkLineOrder | members-05.md | 4228 | 34 |
| PX.Objects.PO.LinkLineReceipt | EntityType |  | ReceiptLineNbr, ReceiptNbr, ReceiptType | 25 | 19 |  | PX_Objects_PO_LinkLineReceipt | members-05.md | 4263 | 49 |
| PX.Objects.PO.POAccrualDetail | EntityType | PO Accrual Detail | DocumentNoteID, LineNbr | 41 | 9 |  | PX_Objects_PO_POAccrualDetail, POAccrualDetail | members-05.md | 4313 | 56 |
| PX.Objects.PO.POAccrualInquiryResult | EntityType | Purchase Accrual Balance Result | DocumentNoteID, LineNbr | 41 | 9 |  | PX_Objects_PO_POAccrualInquiryResult, PurchaseAccrualBalanceResult, POAccrualInquiryResult | members-05.md | 4370 | 57 |
| PX.Objects.PO.POAccrualSplit | EntityType | PO Accrual Allocation | APDocType, APLineNbr, APRefNbr, POReceiptLineNbr, POReceiptNbr, POReceiptType | 24 | 7 |  | PX_Objects_PO_POAccrualSplit, POAccrualAllocation, POAccrualSplit | members-05.md | 4428 | 37 |
| PX.Objects.PO.POAccrualStatus | EntityType | PO Accrual Status | LineNbr, RefNoteID, Type | 55 | 20 |  | PX_Objects_PO_POAccrualStatus, POAccrualStatus | members-05.md | 4466 | 82 |
| PX.Objects.PO.POAddress | EntityType | PO Address | AddressID | 36 | 9 |  | PX_Objects_PO_POAddress, POAddress | members-05.md | 4549 | 52 |
| PX.Objects.PO.POAdjust | EntityType | Purchase Order Adjust | AdjdDocType, AdjdOrderNbr, AdjdOrderType, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | 31 | 9 |  | PX_Objects_PO_POAdjust, PurchaseOrderAdjust, POAdjust | members-05.md | 4602 | 47 |
| PX.Objects.PO.POCartReceipt | EntityType | Receipt Cart | CartID, SiteID | 6 | 4 |  | PX_Objects_PO_POCartReceipt, ReceiptCart1, POCartReceipt | members-05.md | 4650 | 16 |
| PX.Objects.PO.POContact | EntityType | PO Contact | ContactID | 27 | 6 |  | PX_Objects_PO_POContact, POContact | members-05.md | 4667 | 40 |
| PX.Objects.PO.POFixedDemand | EntityType | PO Fixed Demand | PlanID | 24 | 3 | PX.Objects.IN.INItemPlan | PX_Objects_PO_POFixedDemand, POFixedDemand | members-05.md | 4708 | 35 |
| PX.Objects.PO.POLandedCostDetail | EntityType | Landed Costs Detail | DocType, LineNbr, RefNbr | 28 | 17 |  | PX_Objects_PO_POLandedCostDetail, LandedCostsDetail, POLandedCostDetail | members-05.md | 4744 | 52 |
| PX.Objects.PO.POLandedCostDetailS | EntityType |  | DocType, LineNbr, RefNbr | 17 | 12 |  | PX_Objects_PO_POLandedCostDetailS | members-05.md | 4797 | 34 |
| PX.Objects.PO.POLandedCostDoc | EntityType | Landed Costs Document | DocType, RefNbr | 52 | 22 |  | PX_Objects_PO_POLandedCostDoc, LandedCostsDocument, POLandedCostDoc | members-05.md | 4832 | 81 |
| PX.Objects.PO.POLandedCostDocS | EntityType |  | DocType, RefNbr | 49 | 14 |  | PX_Objects_PO_POLandedCostDocS | members-05.md | 4914 | 68 |
| PX.Objects.PO.POLandedCostReceipt | EntityType | Landed Costs Receipt | LCDocType, LCRefNbr, POReceiptNbr, POReceiptType | 6 | 4 |  | PX_Objects_PO_POLandedCostReceipt, LandedCostsReceipt1, POLandedCostReceipt | members-05.md | 4983 | 17 |
| PX.Objects.PO.POLandedCostReceiptLine | EntityType | Landed Costs Receipt Line | DocType, LineNbr, RefNbr | 30 | 13 |  | PX_Objects_PO_POLandedCostReceiptLine, LandedCostsReceiptLine, POLandedCostReceiptLine | members-05.md | 5001 | 50 |
| PX.Objects.PO.POLandedCostTax | EntityType | Landed Costs Tax Detail | DocType, LineNbr, RefNbr, TaxID | 19 | 7 |  | PX_Objects_PO_POLandedCostTax, LandedCostsTaxDetail, POLandedCostTax | members-05.md | 5052 | 33 |
| PX.Objects.PO.POLandedCostTaxTran | EntityType | Landed Costs Tax | DocType, RecordID, RefNbr, TaxID | 24 | 7 |  | PX_Objects_PO_POLandedCostTaxTran, LandedCostsTax, POLandedCostTaxTran | members-05.md | 5086 | 38 |
| PX.Objects.PO.POLine | EntityType | PO Line | LineNbr, OrderNbr, OrderType | 134 | 42 |  | PX_Objects_PO_POLine, POLine1 | members-05.md | 5125 | 183 |
| PX.Objects.PO.POLineBillingRevision | EntityType | PO Line Billing Revision | APDocType, APRefNbr, OrderLineNbr, OrderNbr, OrderType | 24 | 1 |  | PX_Objects_PO_POLineBillingRevision, POLineBillingRevision | members-05.md | 5309 | 31 |
| PX.Objects.PO.POLineR | EntityType |  | LineNbr, OrderNbr, OrderType | 37 | 19 |  | PX_Objects_PO_POLineR | members-05.md | 5341 | 61 |
| PX.Objects.PO.POLineRS | EntityType | PO Line | LineNbr, OrderNbr, OrderType | 74 | 36 |  | PX_Objects_PO_POLineRS, POLine2, POLineRS | members-05.md | 5403 | 116 |
| PX.Objects.PO.POLineS | EntityType | PO Line | LineNbr, OrderNbr, OrderType | 63 | 32 |  | PX_Objects_PO_POLineS, POLine3, POLineS | members-05.md | 5520 | 101 |
| PX.Objects.PO.PONotification | EntityType | Default Notification setup | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_PO_PONotification | members-05.md | 5622 | 6 |
| PX.Objects.PO.POOrder | EntityType | Purchase Order | OrderNbr, OrderType | 140 | 75 |  | PX_Objects_PO_POOrder, PurchaseOrder, POOrder | members-05.md | 5629 | 222 |
| PX.Objects.PO.POOrderAPDoc | EntityType | Purchase Order to Accounts Payable Document Link | DocType, PONbr, POOrderType, RefNbr | 13 | 27 |  | PX_Objects_PO_POOrderAPDoc, PurchaseOrdertoAccountsPayableDocumentLink1, POOrderAPDoc | members-05.md | 5852 | 47 |
| PX.Objects.PO.POOrderDiscountDetail | EntityType | Purchase Order Discount Detail | OrderNbr, OrderType, RecordID | 29 | 8 |  | PX_Objects_PO_POOrderDiscountDetail, PurchaseOrderDiscountDetail, POOrderDiscountDetail | members-05.md | 5900 | 44 |
| PX.Objects.PO.POOrderPOReceipt | EntityType | Purchase Order to Purchase Receipt Link | PONbr, POType, ReceiptNbr, ReceiptType | 10 | 4 |  | PX_Objects_PO_POOrderPOReceipt, PurchaseOrdertoPurchaseReceiptLink, POOrderPOReceipt | members-05.md | 5945 | 21 |
| PX.Objects.PO.POOrderPrepayment | EntityType | PO Prepayment | APDocType, APRefNbr, OrderNbr, OrderType | 18 | 7 |  | PX_Objects_PO_POOrderPrepayment, POPrepayment, POOrderPrepayment | members-05.md | 5967 | 32 |
| PX.Objects.PO.POOrderReceipt | EntityType |  | PONbr, POType, ReceiptNbr, ReceiptType | 8 | 2 |  | PX_Objects_PO_POOrderReceipt | members-05.md | 6000 | 16 |
| PX.Objects.PO.POOrderReceiptLink | EntityType | Purchase Receipt to Purchase Order Link | PONbr, POType, ReceiptNbr, ReceiptType | 9 | 3 | PX.Objects.PO.POOrderReceipt | PX_Objects_PO_POOrderReceiptLink, PurchaseReceipttoPurchaseOrderLink, POOrderReceiptLink | members-05.md | 6017 | 19 |
| PX.Objects.PO.POOrderRS | EntityType | Purchase Order | OrderNbr, OrderType | 0 | 0 | PX.Objects.PO.POOrder | PX_Objects_PO_POOrderRS | members-05.md | 6037 | 6 |
| PX.Objects.PO.POReceipt | EntityType | Purchase Receipt | ReceiptNbr, ReceiptType | 68 | 57 |  | PX_Objects_PO_POReceipt, PurchaseReceipt, POReceipt | members-05.md | 6044 | 132 |
| PX.Objects.PO.POReceiptItemLotSerialAttributesHeader | EntityType | POReceiptItemLotSerialAttributesHeader | InventoryID, LotSerialNbr, ReceiptNbr, ReceiptType | 14 | 6 |  | PX_Objects_PO_POReceiptItemLotSerialAttributesHeader, POReceiptItemLotSerialAttributesHeader | members-05.md | 6177 | 27 |
| PX.Objects.PO.POReceiptLine | EntityType | Purchase Receipt Line | LineNbr, ReceiptNbr, ReceiptType | 105 | 51 |  | PX_Objects_PO_POReceiptLine, PurchaseReceiptLine1, POReceiptLine | members-05.md | 6205 | 163 |
| PX.Objects.PO.POReceiptLinePOReceipt | EntityType | Purchase Receipt Line | LineNbr, ReceiptNbr, ReceiptType | 15 | 37 |  | PX_Objects_PO_POReceiptLinePOReceipt, PurchaseReceiptLine2, POReceiptLinePOReceipt | members-05.md | 6369 | 58 |
| PX.Objects.PO.POReceiptLineS | EntityType | Purchase Receipt Line | LineNbr, ReceiptNbr, ReceiptType | 68 | 36 |  | PX_Objects_PO_POReceiptLineS, PurchaseReceiptLine3, POReceiptLineS | members-05.md | 6428 | 110 |
| PX.Objects.PO.POReceiptLineSplit | EntityType | Purchase Receipt Line Split | LineNbr, ReceiptNbr, ReceiptType, SplitLineNbr | 34 | 21 |  | PX_Objects_PO_POReceiptLineSplit, PurchaseReceiptLineSplit, POReceiptLineSplit | members-05.md | 6539 | 62 |
| PX.Objects.PO.POReceiptSplitToCartSplitLink | EntityType | Receipt Line Split To Cart Split Link | CartID, CartSplitLineNbr, ReceiptLineNbr, ReceiptNbr, ReceiptSplitLineNbr, ReceiptType, SiteID | 8 | 6 |  | PX_Objects_PO_POReceiptSplitToCartSplitLink, ReceiptLineSplitToCartSplitLink, POReceiptSplitToCartSplitLink | members-05.md | 6602 | 20 |
| PX.Objects.PO.POReceiptSplitToTransferSplitLink | EntityType | Receipt Line Split To Transfer Line Split Link | ReceiptLineNbr, ReceiptNbr, ReceiptSplitLineNbr, ReceiptType, TransferDocType, TransferLineNbr, TransferRefNbr, TransferSplitLineNbr | 9 | 6 |  | PX_Objects_PO_POReceiptSplitToTransferSplitLink, ReceiptLineSplitToTransferLineSplitLink, POReceiptSplitToTransferSplitLink | members-05.md | 6623 | 21 |
| PX.Objects.PO.POReceiptToShipmentLink | EntityType | Purchase Receipt to Shipment Link | ReceiptNbr, ReceiptType, SOOrderNbr, SOOrderType, SOShipmentNbr, SOShipmentType | 13 | 6 |  | PX_Objects_PO_POReceiptToShipmentLink, PurchaseReceipttoShipmentLink, POReceiptToShipmentLink | members-05.md | 6645 | 25 |
| PX.Objects.PO.POReceivePutAwaySetup | EntityType | Receive Put Away Setup | BranchID | 24 | 3 |  | PX_Objects_PO_POReceivePutAwaySetup, ReceivePutAwaySetup, POReceivePutAwaySetup | members-05.md | 6671 | 33 |
| PX.Objects.PO.POReceivePutAwayUserSetup | EntityType | Receive Put Away User Setup | UserID | 4 | 3 |  | PX_Objects_PO_POReceivePutAwayUserSetup, ReceivePutAwayUserSetup, POReceivePutAwayUserSetup | members-05.md | 6705 | 13 |
| PX.Objects.PO.PORemitAddress | EntityType | PO Remittance Address | AddressID | 0 | 0 | PX.Objects.PO.POAddress | PX_Objects_PO_PORemitAddress, PORemittanceAddress, PORemitAddress | members-05.md | 6719 | 6 |
| PX.Objects.PO.PORemitContact | EntityType | PO Remittance Contact | ContactID | 0 | 0 | PX.Objects.PO.POContact | PX_Objects_PO_PORemitContact, PORemittanceContact, PORemitContact | members-05.md | 6726 | 6 |
| PX.Objects.PO.POSetup | EntityType | Purchasing Preferences |  | 42 | 12 |  |  | members-05.md | 6733 | 59 |
| PX.Objects.PO.POSetupApproval | EntityType | PO Approval | ApprovalID | 12 | 4 |  | PX_Objects_PO_POSetupApproval, POApproval, POSetupApproval | members-05.md | 6793 | 22 |
| PX.Objects.PO.POShipAddress | EntityType | PO Shipping Address | AddressID | 0 | 0 | PX.Objects.PO.POAddress | PX_Objects_PO_POShipAddress, POShippingAddress, POShipAddress | members-05.md | 6816 | 6 |
| PX.Objects.PO.POShipContact | EntityType | PO Shipping Contact | ContactID | 0 | 0 | PX.Objects.PO.POContact | PX_Objects_PO_POShipContact, POShippingContact, POShipContact | members-05.md | 6823 | 6 |
| PX.Objects.PO.POSiteStatusSelected | EntityType |  | InventoryID | 37 | 4 |  | PX_Objects_PO_POSiteStatusSelected | members-05.md | 6830 | 47 |
| PX.Objects.PO.POTax | EntityType | PO Tax Detail | LineNbr, OrderNbr, OrderType, TaxID | 29 | 10 |  | PX_Objects_PO_POTax, POTaxDetail, POTax | members-05.md | 6878 | 46 |
| PX.Objects.PO.POTaxTran | EntityType | PO Tax | LineNbr, OrderNbr, OrderType, RecordID, TaxID | 30 | 9 |  | PX_Objects_PO_POTaxTran, POTax1, POTaxTran | members-05.md | 6925 | 45 |
| PX.Objects.PO.POTaxTranImported | EntityType | PO Tax | LineNbr, OrderNbr, OrderType, RecordID, TaxID | 0 | 0 | PX.Objects.PO.POTaxTran | PX_Objects_PO_POTaxTranImported | members-05.md | 6971 | 6 |
| PX.Objects.PO.POVendorInventory | EntityType | Inventory Item Vendor Details | RecordID | 28 | 11 |  | PX_Objects_PO_POVendorInventory, InventoryItemVendorDetails, POVendorInventory | members-05.md | 6978 | 46 |
| PX.Objects.PO.VendorLocation | EntityType | Vendor Location | BAccountID, LocationID | 8 | 6 |  | PX_Objects_PO_VendorLocation, VendorLocation | members-05.md | 7025 | 20 |
| PX.Objects.Portals.SP.DAC.SPARPayment | EntityType | Portal AR Payment | DocType, RefNbr | 0 | 0 | PX.Objects.AR.ARPayment | PX_Objects_Portals_SP_DAC_SPARPayment, PortalARPayment, SPARPayment | members-05.md | 7046 | 6 |
| PX.Objects.Portals.SP.DAC.SPARStatement | EntityType | Portal AR Statement | BranchID, StatementDate | 12 | 9 |  | PX_Objects_Portals_SP_DAC_SPARStatement, PortalARStatement, SPARStatement | members-05.md | 7053 | 28 |
| PX.Objects.Portals.SP.DAC.SPCRCase | EntityType | Portal Case | CaseCD | 1 | 0 | PX.Objects.CR.CRCase | PX_Objects_Portals_SP_DAC_SPCRCase, PortalCase, SPCRCase | members-05.md | 7082 | 9 |
| PX.Objects.Portals.SP.DAC.SPInventoryCartItem | EntityType | Products added to the shopping cart. | RecordID | 16 | 4 |  | PX_Objects_Portals_SP_DAC_SPInventoryCartItem, Productsaddedtotheshoppingcart, SPInventoryCartItem | members-05.md | 7092 | 27 |
| PX.Objects.Portals.SP.DAC.SPSOOrder | EntityType | Portal Sales Order | OrderNbr, OrderType | 0 | 0 | PX.Objects.SO.SOOrder | PX_Objects_Portals_SP_DAC_SPSOOrder, PortalSalesOrder, SPSOOrder | members-05.md | 7120 | 6 |
| PX.Objects.Portals.SPPortal | EntityType | Portal Configuration | PortalName | 48 | 19 |  | PX_Objects_Portals_SPPortal, PortalConfiguration, SPPortal | members-05.md | 7127 | 74 |
| PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent | EntityType | Vendor Portal Compliance Notification Event | NotificationEventID | 20 | 4 |  | PX_Objects_Portals_Vendor_Configuration_VPComplianceNotificationEvent, VendorPortalComplianceNotificationEvent, VPComplianceNotificationEvent | members-05.md | 7202 | 31 |
| PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent | EntityType | Vendor Portal Security Notification Event | NotificationEventID | 22 | 7 |  | PX_Objects_Portals_Vendor_Configuration_VPSecurityNotificationEvent, VendorPortalSecurityNotificationEvent, VPSecurityNotificationEvent | members-05.md | 7234 | 36 |
| PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity | EntityType | Recent Activity | ActivityID | 19 | 2 |  | PX_Objects_Portals_Vendor_Dashboard_RecentActivities_VPRecentActivity, RecentActivity, VPRecentActivity | members-05.md | 7271 | 28 |
| PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState | EntityType | User To Do State | EntityNoteID | 9 | 2 |  | PX_Objects_Portals_Vendor_Dashboard_ToDo_VPToDoState, UserToDoState, VPToDoState | members-05.md | 7300 | 17 |
| PX.Objects.PR.PRAcaAggregateGroupMember | EntityType | ACA Aggregate Group Member | MemberEin, OrgBAccountID, Year | 13 | 5 |  | PX_Objects_PR_PRAcaAggregateGroupMember, ACAAggregateGroupMember, PRAcaAggregateGroupMember | members-05.md | 7318 | 24 |
| PX.Objects.PR.PRAcaCompanyMonthlyInformation | EntityType | ACA Company Monthly Information | Month, OrgBAccountID, Year | 17 | 5 |  | PX_Objects_PR_PRAcaCompanyMonthlyInformation, ACACompanyMonthlyInformation, PRAcaCompanyMonthlyInformation | members-05.md | 7343 | 28 |
| PX.Objects.PR.PRAcaCompanyYearlyInformation | EntityType | ACA Company Yearly Information | OrgBAccountID, Year | 14 | 8 |  | PX_Objects_PR_PRAcaCompanyYearlyInformation, ACACompanyYearlyInformation, PRAcaCompanyYearlyInformation | members-05.md | 7372 | 29 |
| PX.Objects.PR.PRAcaDeductCoverageInfo | EntityType | ACA Deduction Code Coverage Information | CoverageType, DeductCodeID | 10 | 3 |  | PX_Objects_PR_PRAcaDeductCoverageInfo, ACADeductionCodeCoverageInformation, PRAcaDeductCoverageInfo | members-05.md | 7402 | 19 |
| PX.Objects.PR.PRAcaEmployeeMonthlyInformation | EntityType | ACA Employee Monthly Information | EmployeeID, Month, OrgBAccountID, Year | 18 | 6 |  | PX_Objects_PR_PRAcaEmployeeMonthlyInformation, ACAEmployeeMonthlyInformation, PRAcaEmployeeMonthlyInformation | members-05.md | 7422 | 30 |
| PX.Objects.PR.PRBandingRulePTOBank | EntityType | Banding Rules | RecordID | 16 | 4 |  | PX_Objects_PR_PRBandingRulePTOBank, BandingRules, PRBandingRulePTOBank | members-05.md | 7453 | 26 |
| PX.Objects.PR.PRBatch | EntityType | Batch | BatchNbr | 27 | 13 |  | PX_Objects_PR_PRBatch, Batch1, PRBatch | members-05.md | 7480 | 47 |
| PX.Objects.PR.PRBatchDeduct | EntityType | Batch Deduction | BatchNbr, CodeID | 10 | 4 |  | PX_Objects_PR_PRBatchDeduct, BatchDeduction, PRBatchDeduct | members-05.md | 7528 | 20 |
| PX.Objects.PR.PRBatchEmployee | EntityType | Batch Employee | BatchNbr, EmployeeID | 26 | 4 |  | PX_Objects_PR_PRBatchEmployee, BatchEmployee, PRBatchEmployee | members-05.md | 7549 | 37 |
| PX.Objects.PR.PRBatchOvertimeRule | EntityType | Batch Overtime Rule | BatchNbr, OvertimeRuleID | 11 | 4 |  | PX_Objects_PR_PRBatchOvertimeRule, BatchOvertimeRule, PRBatchOvertimeRule | members-05.md | 7587 | 22 |
| PX.Objects.PR.PRBenefitDetail | EntityType | Benefit Detail | RecordID | 23 | 19 |  | PX_Objects_PR_PRBenefitDetail, BenefitDetail, PRBenefitDetail | members-05.md | 7610 | 49 |
| PX.Objects.PR.PRCABatch | EntityType | CA Batch for Payroll | BatchNbr | 5 | 0 | PX.Objects.CA.CABatch | PX_Objects_PR_PRCABatch, CABatchforPayroll, PRCABatch | members-05.md | 7660 | 13 |
| PX.Objects.PR.PRCompanyTaxAttribute | EntityType | Company Tax Setting | SettingName | 34 | 5 |  | PX_Objects_PR_PRCompanyTaxAttribute, CompanyTaxSetting, PRCompanyTaxAttribute | members-05.md | 7674 | 46 |
| PX.Objects.PR.PRCRAPayrollAccount | EntityType | CRA Payroll Account | PayrollAccountID | 12 | 4 |  | PX_Objects_PR_PRCRAPayrollAccount, CRAPayrollAccount, PRCRAPayrollAccount | members-05.md | 7721 | 22 |
| PX.Objects.PR.PRDeductCode | EntityType | Deduction Code | CodeCD | 62 | 38 |  | PX_Objects_PR_PRDeductCode, DeductionCode, PRDeductCode | members-05.md | 7744 | 107 |
| PX.Objects.PR.PRDeductCodeBenefitIncreasingWage | EntityType | Deduct Code Benefit Increasing Wage | ApplicableBenefitCodeID, DeductCodeID | 10 | 4 |  | PX_Objects_PR_PRDeductCodeBenefitIncreasingWage, DeductCodeBenefitIncreasingWage, PRDeductCodeBenefitIncreasingWage | members-05.md | 7852 | 20 |
| PX.Objects.PR.PRDeductCodeDeductionDecreasingWage | EntityType | Deduct Code Deduction Decreasing Wage | ApplicableDeductionCodeID, DeductCodeID | 10 | 4 |  | PX_Objects_PR_PRDeductCodeDeductionDecreasingWage, DeductCodeDeductionDecreasingWage, PRDeductCodeDeductionDecreasingWage | members-05.md | 7873 | 20 |
| PX.Objects.PR.PRDeductCodeDetail | EntityType | Deduction Code Taxability | CodeID, TaxID | 9 | 4 |  | PX_Objects_PR_PRDeductCodeDetail, DeductionCodeTaxability, PRDeductCodeDetail | members-05.md | 7894 | 19 |
| PX.Objects.PR.PRDeductCodeEarningIncreasingWage | EntityType | Deduct Code Earning Increasing Wage | ApplicableTypeCD, DeductCodeID | 9 | 4 |  | PX_Objects_PR_PRDeductCodeEarningIncreasingWage, DeductCodeEarningIncreasingWage, PRDeductCodeEarningIncreasingWage | members-05.md | 7914 | 19 |
| PX.Objects.PR.PRDeductCodeTaxDecreasingWage | EntityType | Deduct Code Tax Decreasing Wage | ApplicableTaxID, DeductCodeID | 9 | 4 |  | PX_Objects_PR_PRDeductCodeTaxDecreasingWage, DeductCodeTaxDecreasingWage, PRDeductCodeTaxDecreasingWage | members-05.md | 7934 | 19 |
| PX.Objects.PR.PRDeductCodeTaxIncreasingWage | EntityType | Deduct Code Tax Increasing Wage | ApplicableTaxID, DeductCodeID | 9 | 4 |  | PX_Objects_PR_PRDeductCodeTaxIncreasingWage, DeductCodeTaxIncreasingWage, PRDeductCodeTaxIncreasingWage | members-05.md | 7954 | 19 |
| PX.Objects.PR.PRDeductionAndBenefitProjectPackage | EntityType | Deductions And Benefits Project Package | RecordID | 17 | 5 |  | PX_Objects_PR_PRDeductionAndBenefitProjectPackage, DeductionsAndBenefitsProjectPackage, PRDeductionAndBenefitProjectPackage | members-05.md | 7974 | 29 |
| PX.Objects.PR.PRDeductionAndBenefitUnionPackage | EntityType | Deductions And Benefits Union Package | RecordID | 16 | 5 |  | PX_Objects_PR_PRDeductionAndBenefitUnionPackage, DeductionsAndBenefitsUnionPackage, PRDeductionAndBenefitUnionPackage | members-05.md | 8004 | 27 |
| PX.Objects.PR.PRDeductionDetail | EntityType | Deduction Details | RecordID | 20 | 11 |  | PX_Objects_PR_PRDeductionDetail, DeductionDetails, PRDeductionDetail | members-05.md | 8032 | 38 |
| PX.Objects.PR.PRDeductionsReducingDisposableNet | EntityType | Deductions Reducing Disposable Net Income | ApplicableDeductionCodeID, DeductCodeID | 9 | 4 |  | PX_Objects_PR_PRDeductionsReducingDisposableNet, DeductionsReducingDisposableNetIncome, PRDeductionsReducingDisposableNet | members-05.md | 8071 | 19 |
| PX.Objects.PR.PRDirectDepositSplit | EntityType | Direct Deposit Split | DocType, LineNbr, RefNbr | 20 | 4 |  | PX_Objects_PR_PRDirectDepositSplit, DirectDepositSplit, PRDirectDepositSplit | members-05.md | 8091 | 30 |
| PX.Objects.PR.PREarningDetail | EntityType | Earning Detail | RecordID | 44 | 20 |  | PX_Objects_PR_PREarningDetail, EarningDetail, PREarningDetail | members-05.md | 8122 | 71 |
| PX.Objects.PR.PREarningTypeDetail | EntityType | Earning Type Detail | CountryID, TaxID, TypeCD | 10 | 6 |  | PX_Objects_PR_PREarningTypeDetail, EarningTypeDetail, PREarningTypeDetail | members-05.md | 8194 | 22 |
| PX.Objects.PR.PREIPremiumRate | EntityType | EI Premium Rates | RateID | 11 | 3 |  | PX_Objects_PR_PREIPremiumRate, EIPremiumRates, PREIPremiumRate | members-05.md | 8217 | 20 |
| PX.Objects.PR.PREmployee | EntityType | Payroll Employee | AcctCD | 36 | 26 | PX.Objects.EP.EPEmployee | PX_Objects_PR_PREmployee, PayrollEmployee, PREmployee | members-05.md | 8238 | 70 |
| PX.Objects.PR.PREmployeeAttribute | EntityType | Employee Setting | BAccountID, SettingName | 36 | 6 |  | PX_Objects_PR_PREmployeeAttribute, EmployeeSetting, PREmployeeAttribute | members-05.md | 8309 | 49 |
| PX.Objects.PR.PREmployeeClass | EntityType | Employee Payroll Class | EmployeeClassID | 28 | 11 |  | PX_Objects_PR_PREmployeeClass, EmployeePayrollClass, PREmployeeClass | members-05.md | 8359 | 46 |
| PX.Objects.PR.PREmployeeClassPTOBank | EntityType | Employee Class PTO Bank | RecordID | 23 | 4 |  | PX_Objects_PR_PREmployeeClassPTOBank, EmployeeClassPTOBank, PREmployeeClassPTOBank | members-05.md | 8406 | 34 |
| PX.Objects.PR.PREmployeeClassWorkLocation | EntityType | Employee Class Work Location | RecordID | 12 | 4 |  | PX_Objects_PR_PREmployeeClassWorkLocation, EmployeeClassWorkLocation, PREmployeeClassWorkLocation | members-05.md | 8441 | 23 |
| PX.Objects.PR.PREmployeeDeduct | EntityType | Employee Deduct | BAccountID, LineNbr | 36 | 6 |  | PX_Objects_PR_PREmployeeDeduct, EmployeeDeduct, PREmployeeDeduct | members-05.md | 8465 | 49 |
| PX.Objects.PR.PREmployeeDirectDeposit | EntityType | Employee Direct Deposit | BAccountID, LineNbr | 21 | 3 |  | PX_Objects_PR_PREmployeeDirectDeposit, EmployeeDirectDeposit, PREmployeeDirectDeposit | members-05.md | 8515 | 30 |
| PX.Objects.PR.PREmployeeEarning | EntityType | Employee Earning | BAccountID, LineNbr | 16 | 4 |  | PX_Objects_PR_PREmployeeEarning, EmployeeEarning, PREmployeeEarning | members-05.md | 8546 | 27 |
| PX.Objects.PR.PREmployeePTOBank | EntityType | Employee PTO Bank | BAccountID, BankID, StartDate | 28 | 4 |  | PX_Objects_PR_PREmployeePTOBank, EmployeePTOBank, PREmployeePTOBank | members-05.md | 8574 | 39 |
| PX.Objects.PR.PREmployeePTOHistory | EntityType | Employee PTO History | RecordID | 10 | 0 |  | PX_Objects_PR_PREmployeePTOHistory, EmployeePTOHistory, PREmployeePTOHistory | members-05.md | 8614 | 16 |
| PX.Objects.PR.PREmployeeTax | EntityType | Employee Tax | BAccountID, TaxID | 14 | 5 |  | PX_Objects_PR_PREmployeeTax, EmployeeTax, PREmployeeTax | members-05.md | 8631 | 26 |
| PX.Objects.PR.PREmployeeTaxAttribute | EntityType | Employee Tax Setting | BAccountID, SettingName, TaxID | 31 | 7 |  | PX_Objects_PR_PREmployeeTaxAttribute, EmployeeTaxSetting, PREmployeeTaxAttribute | members-05.md | 8658 | 45 |
| PX.Objects.PR.PREmployeeTaxForm | EntityType | Employee Tax Form | BatchID, EmployeeID, ProvinceOfEmployment | 15 | 4 |  | PX_Objects_PR_PREmployeeTaxForm, EmployeeTaxForm, PREmployeeTaxForm | members-05.md | 8704 | 26 |
| PX.Objects.PR.PREmployeeTaxFormData | EntityType | Employee Tax Form Data | BatchID, EmployeeID, FormFileType, ProvinceOfEmployment | 13 | 4 |  | PX_Objects_PR_PREmployeeTaxFormData, EmployeeTaxFormData, PREmployeeTaxFormData | members-05.md | 8731 | 24 |
| PX.Objects.PR.PREmployeeWorkLocation | EntityType | Employee Work Location | EmployeeID, LocationID | 11 | 4 |  | PX_Objects_PR_PREmployeeWorkLocation, EmployeeWorkLocation, PREmployeeWorkLocation | members-05.md | 8756 | 22 |
| PX.Objects.PR.PREntityCompanyTaxAttribute | EntityType | Entity Company Tax Attribute | EntityID, SettingName | 21 | 3 |  | PX_Objects_PR_PREntityCompanyTaxAttribute, EntityCompanyTaxAttribute, PREntityCompanyTaxAttribute | members-05.md | 8779 | 31 |
| PX.Objects.PR.PREntityTaxCodeAttribute | EntityType | Entity Tax Code Attribute | EntityID, SettingName, TaxID | 20 | 5 |  | PX_Objects_PR_PREntityTaxCodeAttribute, EntityTaxCodeAttribute, PREntityTaxCodeAttribute | members-05.md | 8811 | 32 |
| PX.Objects.PR.PRGovernmentSlip | EntityType | Government Slip | SlipName, Year | 11 | 3 |  | PX_Objects_PR_PRGovernmentSlip, GovernmentSlip, PRGovernmentSlip | members-05.md | 8844 | 20 |
| PX.Objects.PR.PRGovernmentSlipField | EntityType | Government Slip Field | FieldCode, Page, SlipName, Year | 23 | 3 |  | PX_Objects_PR_PRGovernmentSlipField, GovernmentSlipField, PRGovernmentSlipField | members-05.md | 8865 | 32 |
| PX.Objects.PR.PRLocation | EntityType | Location | LocationCD | 15 | 9 |  | PX_Objects_PR_PRLocation, Location1, PRLocation | members-05.md | 8898 | 31 |
| PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet | EntityType | Non-payable Benefits Increasing Disposable Net Income | ApplicableBenefitCodeID, DeductCodeID | 9 | 4 |  | PX_Objects_PR_PRNonPayableBenefitsIncreasingDisposableNet, NonpayableBenefitsIncreasingDisposableNetIncome, PRNonPayableBenefitsIncreasingDisposableNet | members-05.md | 8930 | 19 |
| PX.Objects.PR.PROvertimeRule | EntityType | Overtime Rule | OvertimeRuleID | 19 | 10 |  | PX_Objects_PR_PROvertimeRule, OvertimeRule, PROvertimeRule | members-05.md | 8950 | 36 |
| PX.Objects.PR.PRPayGroup | EntityType | Pay Group | PayGroupID | 14 | 28 |  | PX_Objects_PR_PRPayGroup, PayGroup, PRPayGroup | members-05.md | 8987 | 49 |
| PX.Objects.PR.PRPayGroupPeriod | EntityType | Pay Periods | FinPeriodID, PayGroupID | 23 | 7 |  | PX_Objects_PR_PRPayGroupPeriod, PayPeriods, PRPayGroupPeriod | members-05.md | 9037 | 37 |
| PX.Objects.PR.PRPayGroupPeriodSetup | EntityType | Pay Group Period Setup | PayGroupID, PeriodNbr | 14 | 3 |  | PX_Objects_PR_PRPayGroupPeriodSetup, PayGroupPeriodSetup, PRPayGroupPeriodSetup | members-05.md | 9075 | 24 |
| PX.Objects.PR.PRPayGroupYear | EntityType | Pay Group Year | PayGroupID, Year | 17 | 5 |  | PX_Objects_PR_PRPayGroupYear, PayGroupYear, PRPayGroupYear | members-05.md | 9100 | 29 |
| PX.Objects.PR.PRPayGroupYearSetup | EntityType | Pay Group Calendar | PayGroupID | 29 | 4 |  | PX_Objects_PR_PRPayGroupYearSetup, PayGroupCalendar, PRPayGroupYearSetup | members-05.md | 9130 | 40 |
| PX.Objects.PR.PRPayment | EntityType | Payment | DocType, RefNbr | 72 | 37 |  | PX_Objects_PR_PRPayment, Payment1, PRPayment | members-05.md | 9171 | 116 |
| PX.Objects.PR.PRPaymentBatchExportDetails | EntityType | Payment Batch Export Details | ExportHistoryLineNbr, LineNbr, PaymentBatchNbr | 17 | 7 |  | PX_Objects_PR_PRPaymentBatchExportDetails, PaymentBatchExportDetails, PRPaymentBatchExportDetails | members-05.md | 9288 | 30 |
| PX.Objects.PR.PRPaymentBatchExportHistory | EntityType | Payment Batch Export History | LineNbr, PaymentBatchNbr | 12 | 5 |  | PX_Objects_PR_PRPaymentBatchExportHistory, PaymentBatchExportHistory, PRPaymentBatchExportHistory | members-05.md | 9319 | 23 |
| PX.Objects.PR.PRPaymentDeduct | EntityType | Deduction Summary | CodeID, DocType, RefNbr, Source | 25 | 6 |  | PX_Objects_PR_PRPaymentDeduct, DeductionSummary, PRPaymentDeduct | members-05.md | 9343 | 38 |
| PX.Objects.PR.PRPaymentEarning | EntityType | Payment Earning | DocType, LocationID, RefNbr, TypeCD | 18 | 6 |  | PX_Objects_PR_PRPaymentEarning, PaymentEarning, PRPaymentEarning | members-05.md | 9382 | 31 |
| PX.Objects.PR.PRPaymentEarningAggregatedByCode | EntityType | Payment Earning Aggregated by Earning Type Code | DocType, RefNbr, TypeCD | 9 | 2 |  | PX_Objects_PR_PRPaymentEarningAggregatedByCode, PaymentEarningAggregatedbyEarningTypeCode, PRPaymentEarningAggregatedByCode | members-05.md | 9414 | 17 |
| PX.Objects.PR.PRPaymentFringeBenefit | EntityType | Payment Fringe Benefit | RecordID | 18 | 9 |  | PX_Objects_PR_PRPaymentFringeBenefit, PaymentFringeBenefit, PRPaymentFringeBenefit | members-05.md | 9432 | 34 |
| PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate | EntityType | Payment Fringe Benefit Decreasing Rate | RecordID | 19 | 9 |  | PX_Objects_PR_PRPaymentFringeBenefitDecreasingRate, PaymentFringeBenefitDecreasingRate, PRPaymentFringeBenefitDecreasingRate | members-05.md | 9467 | 35 |
| PX.Objects.PR.PRPaymentFringeEarningDecreasingRate | EntityType | Payment Fringe Earning Decreasing Rate | RecordID | 20 | 9 |  | PX_Objects_PR_PRPaymentFringeEarningDecreasingRate, PaymentFringeEarningDecreasingRate, PRPaymentFringeEarningDecreasingRate | members-05.md | 9503 | 36 |
| PX.Objects.PR.PRPaymentOvertimeRule | EntityType | Payment Overtime Rule | OvertimeRuleID, PaymentDocType, PaymentRefNbr | 12 | 4 |  | PX_Objects_PR_PRPaymentOvertimeRule, PaymentOvertimeRule, PRPaymentOvertimeRule | members-05.md | 9540 | 23 |
| PX.Objects.PR.PRPaymentProjectPackageDeduct | EntityType | Payment Project Package Deduction | RecordID | 24 | 6 |  | PX_Objects_PR_PRPaymentProjectPackageDeduct, PaymentProjectPackageDeduction, PRPaymentProjectPackageDeduct | members-05.md | 9564 | 37 |
| PX.Objects.PR.PRPaymentPTOBank | EntityType | Payment PTO Bank | BankID, DocType, EffectiveStartDate, RefNbr | 40 | 4 |  | PX_Objects_PR_PRPaymentPTOBank, PaymentPTOBank, PRPaymentPTOBank | members-05.md | 9602 | 51 |
| PX.Objects.PR.PRPaymentTax | EntityType | Payment Tax | DocType, RefNbr, TaxID | 20 | 6 |  | PX_Objects_PR_PRPaymentTax, PaymentTax, PRPaymentTax | members-05.md | 9654 | 33 |
| PX.Objects.PR.PRPaymentTaxApplicableAmounts | EntityType | Payment Tax Applicable Amounts | DocType, IsSupplemental, RefNbr, TaxID, WageTypeID | 14 | 4 |  | PX_Objects_PR_PRPaymentTaxApplicableAmounts, PaymentTaxApplicableAmounts, PRPaymentTaxApplicableAmounts | members-05.md | 9688 | 25 |
| PX.Objects.PR.PRPaymentTaxSplit | EntityType | Tax Splits | RecordID | 19 | 5 |  | PX_Objects_PR_PRPaymentTaxSplit, TaxSplits, PRPaymentTaxSplit | members-05.md | 9714 | 31 |
| PX.Objects.PR.PRPaymentUnionPackageDeduct | EntityType | Payment Union Package Deduction | RecordID | 25 | 6 |  | PX_Objects_PR_PRPaymentUnionPackageDeduct, PaymentUnionPackageDeduction, PRPaymentUnionPackageDeduct | members-05.md | 9746 | 38 |
| PX.Objects.PR.PRPaymentWCPremium | EntityType | Payment Work Compensation Premium | BranchID, ContribType, DeductCodeID, DocType, RefNbr, WorkCodeID | 26 | 6 |  | PX_Objects_PR_PRPaymentWCPremium, PaymentWorkCompensationPremium, PRPaymentWCPremium | members-05.md | 9785 | 39 |
| PX.Objects.PR.PRPeriodTaxApplicableAmounts | EntityType | Period Tax Applicable Amounts | EmployeeID, IsSupplemental, PeriodNbr, TaxID, WageTypeID, Year | 15 | 4 |  | PX_Objects_PR_PRPeriodTaxApplicableAmounts, PeriodTaxApplicableAmounts, PRPeriodTaxApplicableAmounts | members-05.md | 9825 | 25 |
| PX.Objects.PR.PRPeriodTaxes | EntityType | Period Taxes | EmployeeID, PeriodNbr, TaxID, Year | 16 | 5 |  | PX_Objects_PR_PRPeriodTaxes, PeriodTaxes, PRPeriodTaxes | members-05.md | 9851 | 27 |
| PX.Objects.PR.PRProjectFringeBenefitRate | EntityType | Project Fringe Benefit Rate | RecordID | 12 | 6 |  | PX_Objects_PR_PRProjectFringeBenefitRate, ProjectFringeBenefitRate, PRProjectFringeBenefitRate | members-05.md | 9879 | 24 |
| PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct | EntityType | Project Fringe Benefit Rate Reducing Deduction | DeductCodeID, ProjectID | 12 | 4 |  | PX_Objects_PR_PRProjectFringeBenefitRateReducingDeduct, ProjectFringeBenefitRateReducingDeduction, PRProjectFringeBenefitRateReducingDeduct | members-05.md | 9904 | 23 |
| PX.Objects.PR.PRPTOAdjustment | EntityType | PTO Adjustment | RefNbr, Type | 12 | 3 |  | PX_Objects_PR_PRPTOAdjustment, PTOAdjustment, PRPTOAdjustment | members-05.md | 9928 | 21 |
| PX.Objects.PR.PRPTOAdjustmentDetail | EntityType | PTO Adjustment Detail | BAccountID, BankID, RefNbr, Type | 20 | 6 |  | PX_Objects_PR_PRPTOAdjustmentDetail, PTOAdjustmentDetail, PRPTOAdjustmentDetail | members-05.md | 9950 | 32 |
| PX.Objects.PR.PRPTOBank | EntityType | PTO Bank | BankID | 26 | 16 |  | PX_Objects_PR_PRPTOBank, PTOBank, PRPTOBank | members-05.md | 9983 | 49 |
| PX.Objects.PR.PRPTOBankApplicableEarningType | EntityType | PTO Bank Applicable Earning Type | BankID, EarningTypeCD | 9 | 4 |  | PX_Objects_PR_PRPTOBankApplicableEarningType, PTOBankApplicableEarningType, PRPTOBankApplicableEarningType | members-05.md | 10033 | 19 |
| PX.Objects.PR.PRPTODetail | EntityType | PTO Detail | RecordID | 17 | 18 |  | PX_Objects_PR_PRPTODetail, PTODetail, PRPTODetail | members-05.md | 10053 | 41 |
| PX.Objects.PR.PRRecordOfEmployment | EntityType | Record Of Employment | RefNbr | 27 | 9 |  | PX_Objects_PR_PRRecordOfEmployment, RecordOfEmployment, PRRecordOfEmployment | members-05.md | 10095 | 43 |
| PX.Objects.PR.PRRegularTypeForOvertime | EntityType | Regular Type for Overtime | OvertimeTypeCD, RegularTypeCD | 9 | 4 |  | PX_Objects_PR_PRRegularTypeForOvertime, RegularTypeforOvertime, PRRegularTypeForOvertime | members-05.md | 10139 | 19 |
| PX.Objects.PR.PRROEInsurableEarningsByPayPeriod | EntityType | Insurable Earnings by Pay Period | PayPeriodID, RefNbr | 11 | 3 |  | PX_Objects_PR_PRROEInsurableEarningsByPayPeriod, InsurableEarningsbyPayPeriod, PRROEInsurableEarningsByPayPeriod | members-05.md | 10159 | 20 |
| PX.Objects.PR.PRROEOtherMonies | EntityType | Other Monies | LineNbr, RefNbr | 12 | 4 |  | PX_Objects_PR_PRROEOtherMonies, OtherMonies, PRROEOtherMonies | members-05.md | 10180 | 22 |
| PX.Objects.PR.PRROEStatutoryHolidayPay | EntityType | Statutory Holiday Pay | LineNbr, RefNbr | 11 | 3 |  | PX_Objects_PR_PRROEStatutoryHolidayPay, StatutoryHolidayPay, PRROEStatutoryHolidayPay | members-05.md | 10203 | 20 |
| PX.Objects.PR.PRSetup | EntityType | Payroll Preferences |  | 39 | 12 |  |  | members-05.md | 10224 | 56 |
| PX.Objects.PR.PRTaxCode | EntityType | Tax Code | TaxCD | 25 | 26 |  | PX_Objects_PR_PRTaxCode, TaxCode, PRTaxCode | members-05.md | 10281 | 58 |
| PX.Objects.PR.PRTaxCodeAttribute | EntityType | Tax Code Setting | SettingName, TaxID | 31 | 5 |  | PX_Objects_PR_PRTaxCodeAttribute, TaxCodeSetting, PRTaxCodeAttribute | members-05.md | 10340 | 43 |
| PX.Objects.PR.PRTaxDetail | EntityType | Tax Detail | RecordID | 24 | 20 |  | PX_Objects_PR_PRTaxDetail, TaxDetail, PRTaxDetail | members-05.md | 10384 | 51 |
| PX.Objects.PR.PRTaxFormBatch | EntityType | Tax Form Batch | BatchID | 20 | 5 |  | PX_Objects_PR_PRTaxFormBatch, TaxFormBatch, PRTaxFormBatch | members-05.md | 10436 | 32 |
| PX.Objects.PR.PRTaxRegistration | EntityType | Tax Registration | TaxRegistrationID | 9 | 2 |  | PX_Objects_PR_PRTaxRegistration, TaxRegistration1, PRTaxRegistration | members-05.md | 10469 | 18 |
| PX.Objects.PR.PRTaxRegistrationAttribute | EntityType | Tax Registration Attribute | SettingName, TaxID, TaxRegistrationID | 12 | 3 |  | PX_Objects_PR_PRTaxRegistrationAttribute, TaxRegistrationAttribute, PRTaxRegistrationAttribute | members-05.md | 10488 | 21 |
| PX.Objects.PR.PRTaxReportingAccount | EntityType | Tax Reporting Account | BAccountID | 14 | 4 |  | PX_Objects_PR_PRTaxReportingAccount, TaxReportingAccount, PRTaxReportingAccount | members-05.md | 10510 | 24 |
| PX.Objects.PR.PRTaxSettingAdditionalInformation | EntityType | Tax Setting Additional Information | CountryID, SettingName, State | 14 | 2 |  | PX_Objects_PR_PRTaxSettingAdditionalInformation, TaxSettingAdditionalInformation, PRTaxSettingAdditionalInformation | members-05.md | 10535 | 22 |
| PX.Objects.PR.PRTaxWebServiceData | EntityType | Tax Web Service Data | CountryID | 14 | 2 |  | PX_Objects_PR_PRTaxWebServiceData, TaxWebServiceData, PRTaxWebServiceData | members-05.md | 10558 | 22 |
| PX.Objects.PR.PRTransactionDateException | EntityType | Transaction Date Exception | RecordID | 12 | 3 |  | PX_Objects_PR_PRTransactionDateException, TransactionDateException, PRTransactionDateException | members-05.md | 10581 | 22 |
| PX.Objects.PR.PRWorkCompensationBenefitRate | EntityType | Work Compensation Benefit Rate | RecordID | 17 | 5 |  | PX_Objects_PR_PRWorkCompensationBenefitRate, WorkCompensationBenefitRate, PRWorkCompensationBenefitRate | members-05.md | 10604 | 29 |
| PX.Objects.PR.PRWorkCompensationMaximumInsurableWage | EntityType | Work Compensation Benefit Rate | DeductCodeID, EffectiveDate, WorkCodeID | 11 | 4 |  | PX_Objects_PR_PRWorkCompensationMaximumInsurableWage, WorkCompensationBenefitRate1, PRWorkCompensationMaximumInsurableWage | members-05.md | 10634 | 22 |
| PX.Objects.PR.PRYtdDeductions | EntityType | YTD Deductions | CodeID, EmployeeID, Year | 11 | 4 |  | PX_Objects_PR_PRYtdDeductions, YTDDeductions, PRYtdDeductions | members-05.md | 10657 | 21 |
| PX.Objects.PR.PRYtdEarnings | EntityType | YTD Earnings | EmployeeID, LocationID, Month, TypeCD, Year | 12 | 5 |  | PX_Objects_PR_PRYtdEarnings, YTDEarnings, PRYtdEarnings | members-05.md | 10679 | 23 |
| PX.Objects.PR.PRYtdTaxes | EntityType | YTD Taxes | EmployeeID, TaxID, Year | 13 | 5 |  | PX_Objects_PR_PRYtdTaxes, YTDTaxes, PRYtdTaxes | members-05.md | 10703 | 24 |
| PX.Objects.PR.Standalone.PRDeductCode | EntityType | Payroll Deduction and Benefit Code |  | 2 | 38 |  |  | members-05.md | 10728 | 45 |
| PX.Objects.PR.Standalone.PREarningType | EntityType | Payroll Earning Type | TypeCD | 1 | 0 |  | PX_Objects_PR_Standalone_PREarningType, PayrollEarningType, PREarningType | members-05.md | 10774 | 7 |
| PX.Objects.PR.Standalone.PREmployee | EntityType | Payroll Employee | BAccountID | 5 | 27 |  | PX_Objects_PR_Standalone_PREmployee, PayrollEmployee1, PREmployee1 | members-05.md | 10782 | 38 |
| PX.Objects.PR.Standalone.PREmployeeClass | EntityType | Payroll Employee Class | EmployeeClassID | 2 | 11 |  | PX_Objects_PR_Standalone_PREmployeeClass, PayrollEmployeeClass, PREmployeeClass1 | members-05.md | 10821 | 19 |
| PX.Objects.PR.Standalone.PRSetup | EntityType | Payroll Preferences |  | 6 | 12 |  |  | members-05.md | 10841 | 23 |
| PX.Objects.PR.Standalone.PRTaxCode | EntityType | Payroll Tax Code |  | 3 | 26 |  |  | members-05.md | 10865 | 34 |
| PX.Objects.RQ.DAC.RQBudgetLedger | EntityType | Budget Ledger | BudgetLedgerID | 12 | 4 |  | PX_Objects_RQ_DAC_RQBudgetLedger, BudgetLedger, RQBudgetLedger | members-05.md | 10900 | 23 |
| PX.Objects.RQ.RQBidding | EntityType |  | LineID | 23 | 7 |  | PX_Objects_RQ_RQBidding | members-05.md | 10924 | 36 |
| PX.Objects.RQ.RQBiddingVendor | EntityType | Bidding Vendor | LineID | 25 | 10 |  | PX_Objects_RQ_RQBiddingVendor, BiddingVendor, RQBiddingVendor | members-05.md | 10961 | 42 |
| PX.Objects.RQ.RQBudget | EntityType | Request Budget Line | ExpenseAcctID, ExpenseSubID | 17 | 2 |  | PX_Objects_RQ_RQBudget, RequestBudgetLine, RQBudget | members-05.md | 11004 | 26 |
| PX.Objects.RQ.RQInventoryItem | EntityType |  | InventoryCD | 6 | 264 |  | PX_Objects_RQ_RQInventoryItem | members-05.md | 11031 | 275 |
| PX.Objects.RQ.RQNotification | EntityType | Default Notification setup | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_RQ_RQNotification | members-05.md | 11307 | 6 |
| PX.Objects.RQ.RQRequest | EntityType | Request | OrderNbr | 48 | 16 |  | PX_Objects_RQ_RQRequest, Request, RQRequest | members-05.md | 11314 | 71 |
| PX.Objects.RQ.RQRequestClass | EntityType | Request Class | ReqClassID | 20 | 8 |  | PX_Objects_RQ_RQRequestClass, RequestClass, RQRequestClass | members-05.md | 11386 | 35 |
| PX.Objects.RQ.RQRequestClassItem | EntityType |  | LineID | 10 | 5 |  | PX_Objects_RQ_RQRequestClassItem | members-05.md | 11422 | 20 |
| PX.Objects.RQ.RQRequestLine | EntityType | Request Line | LineNbr, OrderNbr | 46 | 12 |  | PX_Objects_RQ_RQRequestLine, RequestLine, RQRequestLine | members-05.md | 11443 | 65 |
| PX.Objects.RQ.RQRequestLineOwned | EntityType | Request Line | LineNbr, OrderNbr | 7 | 4 | PX.Objects.RQ.RQRequestLine | PX_Objects_RQ_RQRequestLineOwned | members-05.md | 11509 | 18 |
| PX.Objects.RQ.RQRequestLineSelect | EntityType |  | LineNbr, OrderNbr | 19 | 3 |  | PX_Objects_RQ_RQRequestLineSelect | members-05.md | 11528 | 28 |
| PX.Objects.RQ.RQRequisition | EntityType | Requisition | ReqNbr | 52 | 27 |  | PX_Objects_RQ_RQRequisition, Requisition, RQRequisition | members-05.md | 11557 | 86 |
| PX.Objects.RQ.RQRequisitionContent | EntityType |  | LineNbr, OrderNbr, ReqLineNbr, ReqNbr | 16 | 5 |  | PX_Objects_RQ_RQRequisitionContent | members-05.md | 11644 | 27 |
| PX.Objects.RQ.RQRequisitionLine | EntityType | Requisition Line | LineNbr, ReqNbr | 55 | 13 |  | PX_Objects_RQ_RQRequisitionLine, RequisitionLine, RQRequisitionLine | members-05.md | 11672 | 75 |
| PX.Objects.RQ.RQRequisitionLineBidding | EntityType |  | LineNbr, ReqNbr | 16 | 4 |  | PX_Objects_RQ_RQRequisitionLineBidding | members-05.md | 11748 | 26 |
| PX.Objects.RQ.RQRequisitionLineReceived | EntityType | Requisition Line | LineNbr, ReqNbr | 3 | 0 | PX.Objects.RQ.RQRequisitionLine | PX_Objects_RQ_RQRequisitionLineReceived | members-05.md | 11775 | 11 |
| PX.Objects.RQ.RQRequisitionOrder | EntityType |  | OrderCategory, OrderNbr, OrderType, ReqNbr | 4 | 3 |  | PX_Objects_RQ_RQRequisitionOrder | members-05.md | 11787 | 12 |
| PX.Objects.RQ.RQSetup | EntityType | Requisition Preferences |  | 25 | 9 |  |  | members-05.md | 11800 | 39 |
| PX.Objects.RQ.RQSetupApproval | EntityType |  | ApprovalID | 12 | 4 |  | PX_Objects_RQ_RQSetupApproval | members-05.md | 11840 | 21 |
| PX.Objects.RQ.RQSiteStatusSelected | EntityType |  | InventoryID | 29 | 4 |  | PX_Objects_RQ_RQSiteStatusSelected | members-05.md | 11862 | 39 |
| PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice | EntityType | AR Transactions | LineNbr, RefNbr, TranType | 16 | 18 |  | PX_Objects_SO_DAC_Projections_ARTranForDirectInvoice, ARTransactions2, ARTranForDirectInvoice | members-05.md | 11902 | 40 |
| PX.Objects.SO.DAC.Projections.BlanketSOAdjust | EntityType | Blanket SO Adjustment | AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr, RecordID | 21 | 10 |  | PX_Objects_SO_DAC_Projections_BlanketSOAdjust, BlanketSOAdjustment, BlanketSOAdjust | members-05.md | 11943 | 37 |
| PX.Objects.SO.DAC.Projections.BlanketSOLine | EntityType | Blanket SO Line | LineNbr, OrderNbr, OrderType | 88 | 50 |  | PX_Objects_SO_DAC_Projections_BlanketSOLine, BlanketSOLine | members-05.md | 11981 | 145 |
| PX.Objects.SO.DAC.Projections.BlanketSOLineSplit | EntityType | Blanket SO Line Split | LineNbr, OrderNbr, OrderType, SplitLineNbr | 49 | 27 |  | PX_Objects_SO_DAC_Projections_BlanketSOLineSplit, BlanketSOLineSplit | members-05.md | 12127 | 83 |
| PX.Objects.SO.DAC.Projections.BlanketSOOrder | EntityType | Blanket Sales Order | OrderNbr, OrderType | 75 | 64 |  | PX_Objects_SO_DAC_Projections_BlanketSOOrder, BlanketSalesOrder, BlanketSOOrder | members-05.md | 12211 | 146 |
| PX.Objects.SO.DAC.Projections.BlanketSOOrderSite | EntityType | Blanket SO Order Site | OrderNbr, OrderType, SiteID | 8 | 9 |  | PX_Objects_SO_DAC_Projections_BlanketSOOrderSite, BlanketSOOrderSite | members-05.md | 12358 | 23 |
| PX.Objects.SO.DAC.Projections.InvoiceSplit | EntityType | Invoice Split | ARDocType, ARLineNbr, ARRefNbr, INDocType, INLineNbr, INRefNbr, INSplitLineNbr | 37 | 8 |  | PX_Objects_SO_DAC_Projections_InvoiceSplit, InvoiceSplit | members-05.md | 12382 | 52 |
| PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice | EntityType | Sales Order Line | LineNbr, OrderNbr, OrderType | 13 | 20 |  | PX_Objects_SO_DAC_Projections_SOLineForDirectInvoice, SalesOrderLine, SOLineForDirectInvoice | members-05.md | 12435 | 39 |
| PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult | EntityType | Credit Card Processing for Sales Result | DocType, RefNbr | 20 | 0 | PX.Objects.AR.ARPayment | PX_Objects_SO_DAC_Unbound_SOPaymentProcessResult, CreditCardProcessingforSalesResult, SOPaymentProcessResult | members-05.md | 12475 | 28 |
| PX.Objects.SO.DropShipSOLine | EntityType | SO Drop-Ship Line | LineNbr, OrderNbr, OrderType | 14 | 25 |  | PX_Objects_SO_DropShipSOLine, SODropShipLine, DropShipSOLine | members-05.md | 12504 | 45 |
| PX.Objects.SO.LocationOverrideEntry | ComplexType |  |  | 15 | 0 |  |  | members-05.md | 12550 | 18 |
| PX.Objects.SO.POLine3 | EntityType |  | LineNbr, OrderNbr, OrderType | 33 | 18 |  | PX_Objects_SO_POLine3 | members-05.md | 12569 | 57 |
| PX.Objects.SO.Report.SOShipLineSplitForPacking | EntityType | Shipment Line Split For Packing | LineNbr, ShipmentNbr, SplitLineNbr | 33 | 2 |  | PX_Objects_SO_Report_SOShipLineSplitForPacking, ShipmentLineSplitForPacking, SOShipLineSplitForPacking | members-05.md | 12627 | 42 |
| PX.Objects.SO.SalesAllocation | EntityType | Sales Allocation | LineNbr, OrderNbr, OrderType | 41 | 26 |  | PX_Objects_SO_SalesAllocation, SalesAllocation | members-05.md | 12670 | 74 |
| PX.Objects.SO.SOAddress | EntityType | SO Address | AddressID | 37 | 11 |  | PX_Objects_SO_SOAddress, SOAddress | members-05.md | 12745 | 55 |
| PX.Objects.SO.SOAdjust | EntityType | Sales Order Adjust | AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr, RecordID | 71 | 21 |  | PX_Objects_SO_SOAdjust, SalesOrderAdjust, SOAdjust | members-05.md | 12801 | 99 |
| PX.Objects.SO.SOBillingAddress | EntityType | Billing Address | AddressID | 0 | 0 | PX.Objects.SO.SOAddress | PX_Objects_SO_SOBillingAddress, BillingAddress, SOBillingAddress | members-05.md | 12901 | 6 |
| PX.Objects.SO.SOBillingContact | EntityType | Billing Contact | ContactID | 0 | 0 | PX.Objects.SO.SOContact | PX_Objects_SO_SOBillingContact, BillingContact, SOBillingContact | members-05.md | 12908 | 6 |
| PX.Objects.SO.SOBlanketOrderDisplayLink | EntityType | Blanket Order Display Link | BlanketNbr, BlanketType, OrderNbr, OrderType | 16 | 8 | PX.Objects.SO.SOBlanketOrderLink | PX_Objects_SO_SOBlanketOrderDisplayLink, BlanketOrderDisplayLink, SOBlanketOrderDisplayLink | members-05.md | 12915 | 32 |
| PX.Objects.SO.SOBlanketOrderLink | EntityType | Blanket Order Link | BlanketNbr, BlanketType, OrderNbr, OrderType | 18 | 8 |  | PX_Objects_SO_SOBlanketOrderLink, BlanketOrderLink, SOBlanketOrderLink | members-05.md | 12948 | 33 |
| PX.Objects.SO.SOCartShipment | EntityType | Shipment Cart | CartID, SiteID | 4 | 3 |  | PX_Objects_SO_SOCartShipment, ShipmentCart, SOCartShipment | members-05.md | 12982 | 13 |
| PX.Objects.SO.SOContact | EntityType | SO Contact | ContactID | 28 | 8 |  | PX_Objects_SO_SOContact, SOContact | members-05.md | 12996 | 43 |
| PX.Objects.SO.SOFreightDetail | EntityType | SO Freight Detail | DocType, OrderNbr, OrderType, RefNbr, ShipmentNbr, ShipmentType | 33 | 20 |  | PX_Objects_SO_SOFreightDetail, SOFreightDetail | members-05.md | 13040 | 60 |
| PX.Objects.SO.SOInvoice | EntityType | SO Invoice | DocType, RefNbr | 60 | 34 |  | PX_Objects_SO_SOInvoice, SOInvoice | members-05.md | 13101 | 101 |
| PX.Objects.SO.SOInvoiceSiteStatusSelected | EntityType | Invoice Inventory Lookup Row | InventoryID | 41 | 4 |  | PX_Objects_SO_SOInvoiceSiteStatusSelected, InvoiceInventoryLookupRow, SOInvoiceSiteStatusSelected | members-05.md | 13203 | 52 |
| PX.Objects.SO.SOLine | EntityType | Sales Order Line | LineNbr, OrderNbr, OrderType | 172 | 63 |  | PX_Objects_SO_SOLine, SalesOrderLine1, SOLine | members-05.md | 13256 | 242 |
| PX.Objects.SO.SOLine2 | EntityType |  | LineNbr, OrderNbr, OrderType | 62 | 31 |  | PX_Objects_SO_SOLine2 | members-06.md | 3 | 99 |
| PX.Objects.SO.SOLine4 | EntityType |  | LineNbr, OrderNbr, OrderType | 50 | 31 |  | PX_Objects_SO_SOLine4 | members-06.md | 103 | 87 |
| PX.Objects.SO.SOLineSplit | EntityType | Sales Order Line Split | LineNbr, OrderNbr, OrderType, SplitLineNbr | 82 | 34 |  | PX_Objects_SO_SOLineSplit, SalesOrderLineSplit, SOLineSplit | members-06.md | 191 | 123 |
| PX.Objects.SO.SOLineSplit2 | EntityType |  | LineNbr, OrderNbr, OrderType, SplitLineNbr | 31 | 14 |  | PX_Objects_SO_SOLineSplit2 | members-06.md | 315 | 50 |
| PX.Objects.SO.SOMiscLine2 | EntityType |  | LineNbr, OrderNbr, OrderType | 62 | 34 |  | PX_Objects_SO_SOMiscLine2 | members-06.md | 366 | 102 |
| PX.Objects.SO.SONotification | EntityType | Default Notification setup | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_SO_SONotification | members-06.md | 469 | 6 |
| PX.Objects.SO.SOOrchestrationPlan | EntityType | Orchestration Plan | PlanID | 14 | 6 |  | PX_Objects_SO_SOOrchestrationPlan, OrchestrationPlan, SOOrchestrationPlan | members-06.md | 476 | 26 |
| PX.Objects.SO.SOOrchestrationPlanLine | EntityType | Orchestration Plan Line | LineNbr, PlanID | 11 | 4 |  | PX_Objects_SO_SOOrchestrationPlanLine, OrchestrationPlanLine, SOOrchestrationPlanLine | members-06.md | 503 | 21 |
| PX.Objects.SO.SOOrder | EntityType | Sales Order | OrderNbr, OrderType | 285 | 98 |  | PX_Objects_SO_SOOrder, SalesOrder, SOOrder | members-06.md | 525 | 390 |
| PX.Objects.SO.SOOrderDiscountDetail | EntityType | Sales Order Discount Detail | OrderNbr, OrderType, RecordID | 32 | 9 |  | PX_Objects_SO_SOOrderDiscountDetail, SalesOrderDiscountDetail, SOOrderDiscountDetail | members-06.md | 916 | 48 |
| PX.Objects.SO.SOOrderProcessSelected | EntityType | Sales Order | OrderNbr, OrderType | 0 | 0 | PX.Objects.SO.SOOrder | PX_Objects_SO_SOOrderProcessSelected | members-06.md | 965 | 6 |
| PX.Objects.SO.SOOrderShipment | EntityType | Sales Order Shipment | OrderNbr, OrderType, ShippingRefNoteID | 45 | 28 |  | PX_Objects_SO_SOOrderShipment, SalesOrderShipment, SOOrderShipment | members-06.md | 972 | 80 |
| PX.Objects.SO.SOOrderSite | EntityType | SO Order Warehouse | OrderNbr, OrderType, SiteID | 14 | 8 |  | PX_Objects_SO_SOOrderSite, SOOrderWarehouse, SOOrderSite | members-06.md | 1053 | 28 |
| PX.Objects.SO.SOOrderSiteStatusSelected | EntityType | Sales Order Inventory Lookup Row | InventoryID | 46 | 4 |  | PX_Objects_SO_SOOrderSiteStatusSelected, SalesOrderInventoryLookupRow, SOOrderSiteStatusSelected | members-06.md | 1082 | 57 |
| PX.Objects.SO.SOOrderType | EntityType | Order Type | OrderType | 78 | 65 |  | PX_Objects_SO_SOOrderType, OrderType1, SOOrderType | members-06.md | 1140 | 150 |
| PX.Objects.SO.SOOrderTypeOperation | EntityType | SO Order Type Operation | Operation, OrderType | 16 | 14 |  | PX_Objects_SO_SOOrderTypeOperation, SOOrderTypeOperation | members-06.md | 1291 | 36 |
| PX.Objects.SO.SOPackageDetail | EntityType | SO Package Detail | LineNbr, ShipmentNbr | 32 | 6 |  | PX_Objects_SO_SOPackageDetail, SOPackageDetail | members-06.md | 1328 | 45 |
| PX.Objects.SO.SOPackageDetailEx | EntityType | SO Package Detail | LineNbr, ShipmentNbr | 15 | 0 | PX.Objects.SO.SOPackageDetail | PX_Objects_SO_SOPackageDetailEx | members-06.md | 1374 | 23 |
| PX.Objects.SO.SOPackageInfo | EntityType | SO Package Info | LineNbr, OrderNbr, OrderType | 25 | 7 |  | PX_Objects_SO_SOPackageInfo, SOPackageInfo | members-06.md | 1398 | 39 |
| PX.Objects.SO.SOPackageInfoEx | EntityType | SO Package Info | LineNbr, OrderNbr, OrderType | 4 | 0 | PX.Objects.SO.SOPackageInfo | PX_Objects_SO_SOPackageInfoEx | members-06.md | 1438 | 11 |
| PX.Objects.SO.SOPicker | EntityType | SO Picker | PickerNbr, WorksheetNbr | 17 | 15 |  | PX_Objects_SO_SOPicker, SOPicker | members-06.md | 1450 | 39 |
| PX.Objects.SO.SOPickerListEntry | EntityType | SO Picker List Entry | EntryNbr, PickerNbr, WorksheetNbr | 32 | 17 |  | PX_Objects_SO_SOPickerListEntry, SOPickerListEntry | members-06.md | 1490 | 56 |
| PX.Objects.SO.SOPickerToShipmentLink | EntityType | SO Picker to Shipment Link | PickerNbr, ShipmentNbr, SiteID, ToteID, WorksheetNbr | 12 | 7 |  | PX_Objects_SO_SOPickerToShipmentLink, SOPickertoShipmentLink | members-06.md | 1547 | 25 |
| PX.Objects.SO.SOPickingJob | EntityType | SO Picking Job | JobID | 6 | 3 | PX.Objects.IN.WMSJob | PX_Objects_SO_SOPickingJob, SOPickingJob | members-06.md | 1573 | 17 |
| PX.Objects.SO.SOPickingWorksheet | EntityType | SO Shipment Picking Worksheet | WorksheetNbr | 21 | 14 |  | PX_Objects_SO_SOPickingWorksheet, SOShipmentPickingWorksheet, SOPickingWorksheet | members-06.md | 1591 | 42 |
| PX.Objects.SO.SOPickingWorksheetLine | EntityType | SO Shipment Picking Worksheet Line | LineNbr, WorksheetNbr | 20 | 12 |  | PX_Objects_SO_SOPickingWorksheetLine, SOShipmentPickingWorksheetLine, SOPickingWorksheetLine | members-06.md | 1634 | 38 |
| PX.Objects.SO.SOPickingWorksheetLineSplit | EntityType | SO Shipment Picking Worksheet Line Split | LineNbr, SplitNbr, WorksheetNbr | 19 | 13 |  | PX_Objects_SO_SOPickingWorksheetLineSplit, SOShipmentPickingWorksheetLineSplit, SOPickingWorksheetLineSplit | members-06.md | 1673 | 38 |
| PX.Objects.SO.SOPickingWorksheetShipment | EntityType | SO Shipment Picking Worksheet Link | ShipmentNbr, WorksheetNbr | 19 | 4 |  | PX_Objects_SO_SOPickingWorksheetShipment, SOShipmentPickingWorksheetLink, SOPickingWorksheetShipment | members-06.md | 1712 | 29 |
| PX.Objects.SO.SOPickListEntryToCartSplitLink | EntityType | Pick List Entry To Cart Split Link | CartID, CartSplitLineNbr, EntryNbr, PickerNbr, SiteID, WorksheetNbr | 14 | 8 |  | PX_Objects_SO_SOPickListEntryToCartSplitLink, PickListEntryToCartSplitLink, SOPickListEntryToCartSplitLink | members-06.md | 1742 | 28 |
| PX.Objects.SO.SOPickPackShipSetup | EntityType | Pick Pack Ship Setup | BranchID | 30 | 3 |  | PX_Objects_SO_SOPickPackShipSetup, PickPackShipSetup, SOPickPackShipSetup | members-06.md | 1771 | 39 |
| PX.Objects.SO.SOPickPackShipUserSetup | EntityType | Pick Pack Ship User Setup | UserID | 6 | 2 |  | PX_Objects_SO_SOPickPackShipUserSetup, PickPackShipUserSetup, SOPickPackShipUserSetup | members-06.md | 1811 | 14 |
| PX.Objects.SO.SOQuickProcessParameters | EntityType |  | OrderType | 27 | 2 |  | PX_Objects_SO_SOQuickProcessParameters | members-06.md | 1826 | 35 |
| PX.Objects.SO.SOSalesPerTran | EntityType | SO Salesperson Commission | OrderNbr, OrderType, SalespersonID | 20 | 7 |  | PX_Objects_SO_SOSalesPerTran, SOSalespersonCommission, SOSalesPerTran | members-06.md | 1862 | 34 |
| PX.Objects.SO.SOSetup | EntityType | Sales Orders Preferences |  | 32 | 11 |  |  | members-06.md | 1897 | 48 |
| PX.Objects.SO.SOSetupApproval | EntityType | SO Approval | ApprovalID | 12 | 5 |  | PX_Objects_SO_SOSetupApproval, SOApproval, SOSetupApproval | members-06.md | 1946 | 23 |
| PX.Objects.SO.SOSetupCrossSellExcludedItemClasses | EntityType | SO Setup Cross Sell Excluded Item Classes | ItemClassID | 5 | 2 |  | PX_Objects_SO_SOSetupCrossSellExcludedItemClasses, SOSetupCrossSellExcludedItemClasses | members-06.md | 1970 | 13 |
| PX.Objects.SO.SOSetupCrossSellExcludedOrderType | EntityType | SO Setup Cross Sell Excluded Order Types | OrderType | 5 | 2 |  | PX_Objects_SO_SOSetupCrossSellExcludedOrderType, SOSetupCrossSellExcludedOrderTypes, SOSetupCrossSellExcludedOrderType | members-06.md | 1984 | 13 |
| PX.Objects.SO.SOSetupInvoiceApproval | EntityType | SO Invoice Approval | ApprovalID | 12 | 4 |  | PX_Objects_SO_SOSetupInvoiceApproval, SOInvoiceApproval, SOSetupInvoiceApproval | members-06.md | 1998 | 22 |
| PX.Objects.SO.SOShipLine | EntityType | Shipment Line | LineNbr, ShipmentNbr | 84 | 42 |  | PX_Objects_SO_SOShipLine, ShipmentLine, SOShipLine | members-06.md | 2021 | 133 |
| PX.Objects.SO.SOShipLineSplit | EntityType | Shipment Line Split | LineNbr, ShipmentNbr, SplitLineNbr | 46 | 27 |  | PX_Objects_SO_SOShipLineSplit, ShipmentLineSplit, SOShipLineSplit | members-06.md | 2155 | 80 |
| PX.Objects.SO.SOShipLineSplitPackage | EntityType | Shipment Package Detail | RecordID | 18 | 9 |  | PX_Objects_SO_SOShipLineSplitPackage, ShipmentPackageDetail, SOShipLineSplitPackage | members-06.md | 2236 | 33 |
| PX.Objects.SO.SOShipment | EntityType | Shipment | ShipmentNbr | 120 | 48 |  | PX_Objects_SO_SOShipment, Shipment, SOShipment | members-06.md | 2270 | 175 |
| PX.Objects.SO.SOShipmentAddress | EntityType | Shipment Address | AddressID | 0 | 0 | PX.Objects.SO.SOAddress | PX_Objects_SO_SOShipmentAddress, ShipmentAddress, SOShipmentAddress | members-06.md | 2446 | 6 |
| PX.Objects.SO.SOShipmentContact | EntityType | Shipment Contact | ContactID | 0 | 0 | PX.Objects.SO.SOContact | PX_Objects_SO_SOShipmentContact, ShipmentContact, SOShipmentContact | members-06.md | 2453 | 6 |
| PX.Objects.SO.SOShipmentDiscountDetail | EntityType | Shipment Discount Detail | OrderNbr, OrderType, RecordID, ShipmentNbr, Type | 23 | 8 |  | PX_Objects_SO_SOShipmentDiscountDetail, ShipmentDiscountDetail, SOShipmentDiscountDetail | members-06.md | 2460 | 38 |
| PX.Objects.SO.SOShipmentManifest | EntityType | SOShipmentManifest | ManifestNbr | 7 | 1 |  | PX_Objects_SO_SOShipmentManifest, SOShipmentManifest | members-06.md | 2499 | 15 |
| PX.Objects.SO.SOShipmentPlan | EntityType |  | OrderNbr, OrderType, PlanID | 18 | 76 |  | PX_Objects_SO_SOShipmentPlan | members-06.md | 2515 | 99 |
| PX.Objects.SO.SOShipmentProcessedByUser | EntityType | SO Shipment Processed by User | RecordID | 16 | 4 |  | PX_Objects_SO_SOShipmentProcessedByUser, SOShipmentProcessedbyUser | members-06.md | 2615 | 27 |
| PX.Objects.SO.SOShipmentSplitToCartSplitLink | EntityType | Shipment Line Split To Cart Split Link | CartID, CartSplitLineNbr, ShipmentLineNbr, ShipmentNbr, ShipmentSplitLineNbr, SiteID | 14 | 8 |  | PX_Objects_SO_SOShipmentSplitToCartSplitLink, ShipmentLineSplitToCartSplitLink, SOShipmentSplitToCartSplitLink | members-06.md | 2643 | 28 |
| PX.Objects.SO.SOShippingAddress | EntityType | Shipping Address | AddressID | 0 | 0 | PX.Objects.SO.SOAddress | PX_Objects_SO_SOShippingAddress, ShippingAddress1, SOShippingAddress | members-06.md | 2672 | 6 |
| PX.Objects.SO.SOShippingContact | EntityType | Shipping Contact | ContactID | 0 | 0 | PX.Objects.SO.SOContact | PX_Objects_SO_SOShippingContact, ShippingContact1, SOShippingContact | members-06.md | 2679 | 6 |
| PX.Objects.SO.SOTax | EntityType | SO Tax Detail | LineNbr, OrderNbr, OrderType, TaxID | 33 | 14 |  | PX_Objects_SO_SOTax, SOTaxDetail, SOTax | members-06.md | 2686 | 54 |
| PX.Objects.SO.SOTaxTran | EntityType | Sales Order Tax | LineNbr, OrderNbr, OrderType, RecordID, TaxID, TaxZoneID | 38 | 9 |  | PX_Objects_SO_SOTaxTran, SalesOrderTax, SOTaxTran | members-06.md | 2741 | 54 |
| PX.Objects.SO.SOTaxTranImported | EntityType | Sales Order Tax | LineNbr, OrderNbr, OrderType, RecordID, TaxID, TaxZoneID | 0 | 0 | PX.Objects.SO.SOTaxTran | PX_Objects_SO_SOTaxTranImported | members-06.md | 2796 | 6 |
| PX.Objects.SO.Standalone.SOOwner | EntityType | Employee | AcctCD | 0 | 0 | PX.Objects.EP.EPEmployee | PX_Objects_SO_Standalone_SOOwner, Employee2, SOOwner | members-06.md | 2803 | 6 |
| PX.Objects.SO.SupplyPOLine | EntityType | Supply PO Line | LineNbr, OrderNbr, OrderType | 39 | 23 |  | PX_Objects_SO_SupplyPOLine, SupplyPOLine | members-06.md | 2810 | 69 |
| PX.Objects.SO.Table.SOShipLineSplit | EntityType |  | LineNbr, ShipmentNbr, SplitLineNbr | 46 | 27 |  | PX_Objects_SO_Table_SOShipLineSplit | members-06.md | 2880 | 79 |
| PX.Objects.SV.DACUnbound.SVWorkHistoryItem | EntityType | Work History | NoteID, TicketNbr | 7 | 4 |  | PX_Objects_SV_DACUnbound_SVWorkHistoryItem, WorkHistory, SVWorkHistoryItem | members-06.md | 2960 | 17 |
| PX.Objects.SV.FSEmployeeSkill | EntityType | Staff Skill | EmployeeID, SkillID | 11 | 5 |  | PX_Objects_SV_FSEmployeeSkill, StaffSkill, FSEmployeeSkill | members-06.md | 2978 | 23 |
| PX.Objects.SV.FSGeoZone | EntityType | Service Area | GeoZoneCD | 13 | 8 |  | PX_Objects_SV_FSGeoZone, ServiceArea1, FSGeoZone1 | members-06.md | 3002 | 28 |
| PX.Objects.SV.FSGeoZonePostalCode | EntityType | Postal Code | GeoZoneID, PostalCode | 10 | 4 |  | PX_Objects_SV_FSGeoZonePostalCode, PostalCode, FSGeoZonePostalCode1 | members-06.md | 3031 | 20 |
| PX.Objects.SV.FSLicense | EntityType | Staff License | RefNbr | 18 | 6 |  | PX_Objects_SV_FSLicense, StaffLicense, FSLicense1 | members-06.md | 3052 | 31 |
| PX.Objects.SV.FSLicenseType | EntityType | License Type | LicenseTypeCD | 13 | 5 |  | PX_Objects_SV_FSLicenseType, LicenseType1, FSLicenseType1 | members-06.md | 3084 | 25 |
| PX.Objects.SV.FSSetup | EntityType | SV: Service Management Preferences |  | 47 | 10 |  |  | members-06.md | 3110 | 62 |
| PX.Objects.SV.FSSkill | EntityType | Skill | SkillCD | 14 | 6 |  | PX_Objects_SV_FSSkill, Skill1, FSSkill1 | members-06.md | 3173 | 27 |
| PX.Objects.SV.PMActivityTotal | EntityType | Activities Total | RefNoteId | 5 | 0 |  | PX_Objects_SV_PMActivityTotal, ActivitiesTotal, PMActivityTotal | members-06.md | 3201 | 11 |
| PX.Objects.SV.Reports.APRegister | EntityType |  | DocType, RefNbr | 5 | 45 |  | PX_Objects_SV_Reports_APRegister | members-06.md | 3213 | 56 |
| PX.Objects.SV.Reports.APRegisterServiceReport | EntityType |  | DocType, RefNbr | 0 | 0 | PX.Objects.SV.Reports.APRegister | PX_Objects_SV_Reports_APRegisterServiceReport | members-06.md | 3270 | 5 |
| PX.Objects.SV.Reports.APTran | EntityType |  | RefNbr, TranType | 3 | 47 |  | PX_Objects_SV_Reports_APTran | members-06.md | 3276 | 55 |
| PX.Objects.SV.Reports.APTran2 | EntityType |  | RefNbr, TranType | 0 | 0 | PX.Objects.SV.Reports.APTran | PX_Objects_SV_Reports_APTran2 | members-06.md | 3332 | 5 |
| PX.Objects.SV.Reports.ARRegister | EntityType |  | DocType, RefNbr | 5 | 42 |  | PX_Objects_SV_Reports_ARRegister | members-06.md | 3338 | 53 |
| PX.Objects.SV.Reports.ARRegisterServiceReport | EntityType |  | DocType, RefNbr | 0 | 0 | PX.Objects.SV.Reports.ARRegister | PX_Objects_SV_Reports_ARRegisterServiceReport | members-06.md | 3392 | 5 |
| PX.Objects.SV.Reports.ARTran | EntityType |  | RefNbr, TranType | 3 | 54 |  | PX_Objects_SV_Reports_ARTran | members-06.md | 3398 | 62 |
| PX.Objects.SV.Reports.ARTran2 | EntityType |  | RefNbr, TranType | 0 | 0 | PX.Objects.SV.Reports.ARTran | PX_Objects_SV_Reports_ARTran2 | members-06.md | 3461 | 5 |
| PX.Objects.SV.Reports.SVPrepaymentAdjust | EntityType |  | DocType, RefNbr | 0 | 0 | PX.Objects.SV.Reports.ARRegister | PX_Objects_SV_Reports_SVPrepaymentAdjust | members-06.md | 3467 | 5 |
| PX.Objects.SV.SVAccessibleCustomer | EntityType | Customer | BAccountID | 2 | 73 |  | PX_Objects_SV_SVAccessibleCustomer, Customer4, SVAccessibleCustomer | members-06.md | 3473 | 81 |
| PX.Objects.SV.SVAddress | EntityType | Address | AddressID | 24 | 6 |  | PX_Objects_SV_SVAddress, Address1, SVAddress | members-06.md | 3555 | 37 |
| PX.Objects.SV.SVAdjust | EntityType | Work Order Adjust | AdjdOrderNbr, AdjgDocType, AdjgRefNbr | 37 | 10 |  | PX_Objects_SV_SVAdjust, WorkOrderAdjust, SVAdjust | members-06.md | 3593 | 54 |
| PX.Objects.SV.SVContact | EntityType | Contact | ContactID | 27 | 2 |  | PX_Objects_SV_SVContact, Contact3, SVContact | members-06.md | 3648 | 36 |
| PX.Objects.SV.SVEmployeeLicense | EntityType | Staff License | RefNbr | 0 | 0 | PX.Objects.SV.FSLicense | PX_Objects_SV_SVEmployeeLicense, StaffLicense1, SVEmployeeLicense | members-06.md | 3685 | 6 |
| PX.Objects.SV.SVEmployeeServiceArea | EntityType | Staff Service Area | EmployeeID, GeoZoneID | 11 | 0 |  | PX_Objects_SV_SVEmployeeServiceArea, StaffServiceArea, SVEmployeeServiceArea | members-06.md | 3692 | 18 |
| PX.Objects.SV.SVEmployeeSkill | EntityType | Staff Skill | EmployeeID, SkillID | 0 | 0 | PX.Objects.SV.FSEmployeeSkill | PX_Objects_SV_SVEmployeeSkill, StaffSkill1, SVEmployeeSkill | members-06.md | 3711 | 6 |
| PX.Objects.SV.SVEvent | EntityType | Work Event | NoteID | 26 | 7 |  | PX_Objects_SV_SVEvent, WorkEvent, SVEvent | members-06.md | 3718 | 40 |
| PX.Objects.SV.SVEventLabor | EntityType | Work Task Workforce | EventNoteID, LineNbr | 17 | 4 |  | PX_Objects_SV_SVEventLabor, WorkTaskWorkforce, SVEventLabor | members-06.md | 3759 | 28 |
| PX.Objects.SV.SVEventProjection | EntityType | Work Event | NoteID | 11 | 4 |  | PX_Objects_SV_SVEventProjection, WorkEvent1, SVEventProjection | members-06.md | 3788 | 21 |
| PX.Objects.SV.SVEventStatusColor | EntityType | Work Event Status Color | StatusID | 12 | 2 |  | PX_Objects_SV_SVEventStatusColor, WorkEventStatusColor, SVEventStatusColor | members-06.md | 3810 | 20 |
| PX.Objects.SV.SVEventTask | EntityType | Work Event Task | EventNoteID, LineNbr | 14 | 4 |  | PX_Objects_SV_SVEventTask, WorkEventTask, SVEventTask | members-06.md | 3831 | 25 |
| PX.Objects.SV.SVInvoice | EntityType | Work Order Invoice | DocType, RefNbr | 12 | 5 |  | PX_Objects_SV_SVInvoice, WorkOrderInvoice, SVInvoice | members-06.md | 3857 | 24 |
| PX.Objects.SV.SVLicenseType | EntityType | License Type | LicenseTypeCD | 0 | 0 | PX.Objects.SV.FSLicenseType | PX_Objects_SV_SVLicenseType, LicenseType2, SVLicenseType | members-06.md | 3882 | 6 |
| PX.Objects.SV.SVMarkup | EntityType | Markup | MarkupID | 20 | 3 |  | PX_Objects_SV_SVMarkup, Markup, SVMarkup | members-06.md | 3889 | 30 |
| PX.Objects.SV.SVMyDayReport | EntityType | My Day Report | EmployeeID | 12 | 3 |  | PX_Objects_SV_SVMyDayReport, MyDayReport, SVMyDayReport | members-06.md | 3920 | 22 |
| PX.Objects.SV.SVNotification | EntityType | Default Notification setup | SetupID | 0 | 0 | PX.Objects.CS.NotificationSetup | PX_Objects_SV_SVNotification | members-06.md | 3943 | 6 |
| PX.Objects.SV.SVOrder | EntityType | Work Order | OrderNbr | 94 | 23 |  | PX_Objects_SV_SVOrder, WorkOrder, SVOrder | members-06.md | 3950 | 124 |
| PX.Objects.SV.SVOrderActual | EntityType | Work Order Actuals | LineNbr, OrderNbr | 57 | 19 |  | PX_Objects_SV_SVOrderActual, WorkOrderActuals, SVOrderActual | members-06.md | 4075 | 83 |
| PX.Objects.SV.SVOrderDetail | EntityType | Work Order Estimate | LineNbr, OrderNbr | 55 | 20 |  | PX_Objects_SV_SVOrderDetail, WorkOrderEstimate, SVOrderDetail | members-06.md | 4159 | 82 |
| PX.Objects.SV.SVOrderDiscountDetail | EntityType | Work Order Discount | OrderNbr, RecordID, Type | 27 | 8 |  | PX_Objects_SV_SVOrderDiscountDetail, WorkOrderDiscount, SVOrderDiscountDetail | members-06.md | 4242 | 42 |
| PX.Objects.SV.SVOrderGLAccount | EntityType | Work Order GL Accounts | BillingCategory, OrderNbr | 11 | 7 |  | PX_Objects_SV_SVOrderGLAccount, WorkOrderGLAccounts, SVOrderGLAccount | members-06.md | 4285 | 25 |
| PX.Objects.SV.SVOrderProjection | EntityType | Work Order | OrderNbr | 5 | 12 |  | PX_Objects_SV_SVOrderProjection, WorkOrder1, SVOrderProjection | members-06.md | 4311 | 23 |
| PX.Objects.SV.SVOrderTask | EntityType | Work Order Task | TaskID | 38 | 6 |  | PX_Objects_SV_SVOrderTask, WorkOrderTask, SVOrderTask | members-06.md | 4335 | 51 |
| PX.Objects.SV.SVOrderType | EntityType | Work Order Type | OrderType | 18 | 7 |  | PX_Objects_SV_SVOrderType, WorkOrderType, SVOrderType | members-06.md | 4387 | 32 |
| PX.Objects.SV.SVOrderTypeGLAccount | EntityType | Work Order Type GL Accounts | BillingCategory, OrderType | 11 | 7 |  | PX_Objects_SV_SVOrderTypeGLAccount, WorkOrderTypeGLAccounts, SVOrderTypeGLAccount | members-06.md | 4420 | 25 |
| PX.Objects.SV.SVOrderTypeTaskTemplate | EntityType | Task Templates tab | NoteID, OrderType | 12 | 4 |  | PX_Objects_SV_SVOrderTypeTaskTemplate, TaskTemplatestab, SVOrderTypeTaskTemplate | members-06.md | 4446 | 23 |
| PX.Objects.SV.SVPostalCode | EntityType | Postal Code | GeoZoneID, PostalCode | 0 | 0 | PX.Objects.SV.FSGeoZonePostalCode | PX_Objects_SV_SVPostalCode, PostalCode1, SVPostalCode | members-06.md | 4470 | 6 |
| PX.Objects.SV.SVResource | EntityType | Resource | ResourceClassID, ResourceNoteID | 10 | 6 |  | PX_Objects_SV_SVResource, Resource, SVResource | members-06.md | 4477 | 22 |
| PX.Objects.SV.SVResourceClass | EntityType | Resource Class | ResourceClassID | 11 | 6 |  | PX_Objects_SV_SVResourceClass, ResourceClass, SVResourceClass | members-06.md | 4500 | 24 |
| PX.Objects.SV.SVResourceClassProperty | EntityType | Resource Class Property | ClassPropertyID, ResourceClassID | 11 | 3 |  | PX_Objects_SV_SVResourceClassProperty, ResourceClassProperty, SVResourceClassProperty | members-06.md | 4525 | 20 |
| PX.Objects.SV.SVResourceProperty | EntityType | Resource Property | ClassPropertyID, PropertySourceID, ResourceNoteID, ResourceValue | 14 | 3 |  | PX_Objects_SV_SVResourceProperty, ResourceProperty, SVResourceProperty | members-06.md | 4546 | 23 |
| PX.Objects.SV.SVResourcePropertyMapping | EntityType | Resource Property Mapping | ClassPropertyID, ResourceClassID | 15 | 3 |  | PX_Objects_SV_SVResourcePropertyMapping, ResourcePropertyMapping, SVResourcePropertyMapping | members-06.md | 4570 | 24 |
| PX.Objects.SV.SVSchedulingSetup | EntityType | Scheduling Preferences |  | 19 | 3 |  |  | members-06.md | 4595 | 27 |
| PX.Objects.SV.SVServiceArea | EntityType | Service Area | GeoZoneCD | 0 | 0 | PX.Objects.SV.FSGeoZone | PX_Objects_SV_SVServiceArea, ServiceArea2, SVServiceArea | members-06.md | 4623 | 6 |
| PX.Objects.SV.SVServiceLocation | EntityType | Service Location | ServiceLocationID | 19 | 10 |  | PX_Objects_SV_SVServiceLocation, ServiceLocation, SVServiceLocation | members-06.md | 4630 | 36 |
| PX.Objects.SV.SVServiceLocationContact | EntityType | Service Location Contact | ServiceLocationContactID | 11 | 4 |  | PX_Objects_SV_SVServiceLocationContact, ServiceLocationContact, SVServiceLocationContact | members-06.md | 4667 | 21 |
| PX.Objects.SV.SVServiceLocationCustomer | EntityType | Service Location Customer | ServiceLocationCustomerID | 11 | 6 |  | PX_Objects_SV_SVServiceLocationCustomer, ServiceLocationCustomer, SVServiceLocationCustomer | members-06.md | 4689 | 23 |
| PX.Objects.SV.SVSetup | EntityType | Work Order Preferences |  | 20 | 8 |  |  | members-06.md | 4713 | 33 |
| PX.Objects.SV.SVSetupInvoiceApproval | EntityType | Work Order Invoice Approval | ApprovalID | 12 | 4 |  | PX_Objects_SV_SVSetupInvoiceApproval, WorkOrderInvoiceApproval, SVSetupInvoiceApproval | members-06.md | 4747 | 22 |
| PX.Objects.SV.SVSiteStatusSelected | EntityType |  | InventoryID | 20 | 5 |  | PX_Objects_SV_SVSiteStatusSelected | members-06.md | 4770 | 31 |
| PX.Objects.SV.SVSkill | EntityType | Skill | SkillCD | 0 | 0 | PX.Objects.SV.FSSkill | PX_Objects_SV_SVSkill, Skill2, SVSkill | members-06.md | 4802 | 6 |
| PX.Objects.SV.SVStagingWarehouse | EntityType | Staging Warehouse | BranchID | 9 | 5 |  | PX_Objects_SV_SVStagingWarehouse, StagingWarehouse, SVStagingWarehouse | members-06.md | 4809 | 21 |
| PX.Objects.SV.SVTax | EntityType | Work Order Tax Detail | LineNbr, OrderNbr, TaxID | 19 | 9 |  | PX_Objects_SV_SVTax, WorkOrderTaxDetail, SVTax | members-06.md | 4831 | 35 |
| PX.Objects.SV.SVTaxTran | EntityType | Work Order Tax | LineNbr, OrderNbr, RecordID, TaxID | 23 | 8 |  | PX_Objects_SV_SVTaxTran, WorkOrderTax, SVTaxTran | members-06.md | 4867 | 38 |
| PX.Objects.SV.SVTicket | EntityType | Work Ticket | TicketNbr | 29 | 7 |  | PX_Objects_SV_SVTicket, WorkTicket, SVTicket | members-06.md | 4906 | 43 |
| PX.Objects.SV.SVTicketDetail | EntityType | Work Ticket Detail | NoteID, TicketNbr | 25 | 8 |  | PX_Objects_SV_SVTicketDetail, WorkTicketDetail, SVTicketDetail | members-06.md | 4950 | 40 |
| PX.Objects.SV.SVTicketEmployeeGroup | ComplexType |  |  | 2 | 0 |  |  | members-06.md | 4991 | 5 |
| PX.Objects.SV.SVTicketLabor | EntityType | Ticket Labor Employee | EmployeeID, TicketNbr | 2 | 3 |  | PX_Objects_SV_SVTicketLabor, TicketLaborEmployee, SVTicketLabor | members-06.md | 4997 | 11 |
| PX.Objects.SV.SVVendorLicense | EntityType | Vendor License | LicenseID | 17 | 2 |  | PX_Objects_SV_SVVendorLicense, VendorLicense, SVVendorLicense | members-06.md | 5009 | 25 |
| PX.Objects.SV.SVVendorServiceArea | EntityType | Vendor Service Area | EmployeeID, GeoZoneID | 11 | 0 |  | PX_Objects_SV_SVVendorServiceArea, VendorServiceArea, SVVendorServiceArea | members-06.md | 5035 | 18 |
| PX.Objects.SV.SVVendorSkill | EntityType | Vendor Skill | EmployeeID, SkillID | 10 | 2 |  | PX_Objects_SV_SVVendorSkill, VendorSkill, SVVendorSkill | members-06.md | 5054 | 18 |
| PX.Objects.SV.SVWorkDetailsTicket | EntityType | Work Details | TicketNbr | 0 | 0 | PX.Objects.SV.SVTicket | PX_Objects_SV_SVWorkDetailsTicket, WorkDetails, SVWorkDetailsTicket | members-06.md | 5073 | 6 |
| PX.Objects.SV.SVWorkforceResource | EntityType | Workforce Resource | ResourceClassID, ResourceNoteID | 8 | 0 | PX.Objects.SV.SVResource | PX_Objects_SV_SVWorkforceResource, WorkforceResource, SVWorkforceResource | members-06.md | 5080 | 15 |
| PX.Objects.SV.SVWorkTask | EntityType | Work Task | TaskID | 30 | 8 |  | PX_Objects_SV_SVWorkTask, WorkTask, SVWorkTask | members-06.md | 5096 | 45 |
| PX.Objects.SV.SVWorkTaskAction | EntityType | Work Task Action | LineNbr, ParentNoteID | 14 | 3 |  | PX_Objects_SV_SVWorkTaskAction, WorkTaskAction, SVWorkTaskAction | members-06.md | 5142 | 23 |
| PX.Objects.SV.SVWorkTaskEvent | EntityType | Work Task Event | NoteID | 2 | 0 | PX.Objects.SV.SVEvent | PX_Objects_SV_SVWorkTaskEvent, WorkTaskEvent, SVWorkTaskEvent | members-06.md | 5166 | 10 |
| PX.Objects.SV.SVWorkTaskLabor | EntityType | Work Task Workforce | LineNbr, TaskID | 21 | 6 |  | PX_Objects_SV_SVWorkTaskLabor, WorkTaskWorkforce1, SVWorkTaskLabor | members-06.md | 5177 | 34 |
| PX.Objects.SV.SVWorkTaskResourceProperty | EntityType | Work Task Template Workforce | LineNbr, TaskID | 15 | 3 |  | PX_Objects_SV_SVWorkTaskResourceProperty, WorkTaskTemplateWorkforce, SVWorkTaskResourceProperty | members-06.md | 5212 | 25 |
| PX.Objects.SV.SVWorkTaskTemplate | EntityType | Work Task Template | TaskTemplateID | 17 | 7 |  | PX_Objects_SV_SVWorkTaskTemplate, WorkTaskTemplate, SVWorkTaskTemplate | members-06.md | 5238 | 30 |
| PX.Objects.SV.SVWorkTaskTemplateAction | EntityType | Checklist tab | LineNbr, TaskTemplateID | 12 | 3 |  | PX_Objects_SV_SVWorkTaskTemplateAction, Checklisttab, SVWorkTaskTemplateAction | members-06.md | 5269 | 21 |
| PX.Objects.SV.SVWorkTaskTemplateLabor | EntityType | Work Task Template Workforce | LineNbr, TaskTemplateID | 16 | 5 |  | PX_Objects_SV_SVWorkTaskTemplateLabor, WorkTaskTemplateWorkforce1, SVWorkTaskTemplateLabor | members-06.md | 5291 | 28 |
| PX.Objects.SV.SVWorkTaskTemplateResourceProperty | EntityType | Work Task Template Workforce | LineNbr, TaskTemplateID | 15 | 3 |  | PX_Objects_SV_SVWorkTaskTemplateResourceProperty, WorkTaskTemplateWorkforce2, SVWorkTaskTemplateResourceProperty | members-06.md | 5320 | 25 |
| PX.Objects.SV.SVWorkTaskTotal | EntityType | Time Widget | RefNoteId | 2 | 0 |  | PX_Objects_SV_SVWorkTaskTotal, TimeWidget, SVWorkTaskTotal | members-06.md | 5346 | 8 |
| PX.Objects.TX.DAC.TaxTranForReporting | EntityType | Tax Transaction | Module, RecordID | 2 | 0 | PX.Objects.TX.TaxTran | PX_Objects_TX_DAC_TaxTranForReporting | members-06.md | 5355 | 10 |
| PX.Objects.TX.SVATConversionHist | EntityType | SVAT Conversion History | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, Module, TaxID | 40 | 7 |  | PX_Objects_TX_SVATConversionHist, SVATConversionHistory, SVATConversionHist | members-06.md | 5366 | 53 |
| PX.Objects.TX.SVATConversionHistExt | EntityType | SVAT Conversion History | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, Module, TaxID | 8 | 1 | PX.Objects.TX.SVATConversionHist | PX_Objects_TX_SVATConversionHistExt | members-06.md | 5420 | 17 |
| PX.Objects.TX.Tax | EntityType | Tax | TaxID | 35 | 77 |  | PX_Objects_TX_Tax, Tax | members-06.md | 5438 | 119 |
| PX.Objects.TX.TaxAdjustment | EntityType | Tax Adjustment | DocType, RefNbr | 30 | 14 |  | PX_Objects_TX_TaxAdjustment, TaxAdjustment | members-06.md | 5558 | 51 |
| PX.Objects.TX.TaxBucket | EntityType | Tax Group | BucketID, VendorID | 11 | 6 |  | PX_Objects_TX_TaxBucket, TaxGroup, TaxBucket | members-06.md | 5610 | 23 |
| PX.Objects.TX.TaxBucketLine | EntityType | Tax Group Line | BucketID, LineNbr, TaxReportRevisionID, VendorID | 11 | 6 |  | PX_Objects_TX_TaxBucketLine, TaxGroupLine, TaxBucketLine | members-06.md | 5634 | 23 |
| PX.Objects.TX.TaxCategory | EntityType | Tax Category | TaxCategoryID | 12 | 44 |  | PX_Objects_TX_TaxCategory, TaxCategory | members-06.md | 5658 | 63 |
| PX.Objects.TX.TaxCategoryDet | EntityType | Tax Category Detail | TaxCategoryID, TaxID | 9 | 4 |  | PX_Objects_TX_TaxCategoryDet, TaxCategoryDetail, TaxCategoryDet | members-06.md | 5722 | 19 |
| PX.Objects.TX.TaxDetailByGLReport | EntityType | Tax Report Detail | Module, RecordID, RefNbr, TaxID, TranType | 18 | 6 |  | PX_Objects_TX_TaxDetailByGLReport, TaxReportDetail, TaxDetailByGLReport | members-06.md | 5742 | 30 |
| PX.Objects.TX.TaxDetailReport | EntityType | Tax Report Detail | LineNbr, Module, RecordID, RefNbr, TaxID, TranType | 20 | 6 |  | PX_Objects_TX_TaxDetailReport, TaxReportDetail1, TaxDetailReport | members-06.md | 5773 | 32 |
| PX.Objects.TX.TaxDetailReportCurrency | EntityType | Tax Detail Report Currency | LineNbr, Module, RecordID, RefNbr, TaxID, TranType | 22 | 6 |  | PX_Objects_TX_TaxDetailReportCurrency, TaxDetailReportCurrency | members-06.md | 5806 | 34 |
| PX.Objects.TX.TaxHistory | EntityType | Tax History | AccountID, BranchID, LineNbr, RevisionID, SubID, TaxID, TaxPeriodID, TaxReportRevisionID, VendorID | 15 | 5 |  | PX_Objects_TX_TaxHistory, TaxHistory | members-06.md | 5841 | 26 |
| PX.Objects.TX.TaxHistorySum | EntityType | Tax History Sum | BranchID, LineNbr, RevisionID, TaxPeriodID, TaxReportRevisionID, VendorID | 10 | 2 |  | PX_Objects_TX_TaxHistorySum, TaxHistorySum | members-06.md | 5868 | 18 |
| PX.Objects.TX.TaxPeriod | EntityType | Tax Period | OrganizationID, TaxPeriodID, VendorID | 11 | 7 |  | PX_Objects_TX_TaxPeriod, TaxPeriod | members-06.md | 5887 | 25 |
| PX.Objects.TX.TaxPeriodEffective | ComplexType |  |  | 6 | 0 |  |  | members-06.md | 5913 | 9 |
| PX.Objects.TX.TaxPeriodForReportShowing | EntityType |  | OrganizationID, TaxPeriodID, VendorID | 6 | 1 |  | PX_Objects_TX_TaxPeriodForReportShowing | members-06.md | 5923 | 13 |
| PX.Objects.TX.TaxPlugin | EntityType | Tax Plug-in | TaxPluginID | 14 | 5 |  | PX_Objects_TX_TaxPlugin, TaxPlugin | members-06.md | 5937 | 26 |
| PX.Objects.TX.TaxPluginDetail | EntityType | Tax Plug-in Details | SettingID, TaxPluginID | 14 | 3 |  | PX_Objects_TX_TaxPluginDetail, TaxPluginDetails, TaxPluginDetail | members-06.md | 5964 | 23 |
| PX.Objects.TX.TaxPluginMapping | EntityType | Tax Plug-in Mapping | BranchID, TaxPluginID | 11 | 4 |  | PX_Objects_TX_TaxPluginMapping, TaxPluginMapping | members-06.md | 5988 | 21 |
| PX.Objects.TX.TaxReport | EntityType | Tax Report | RevisionID, VendorID | 16 | 6 |  | PX_Objects_TX_TaxReport, TaxReport | members-06.md | 6010 | 29 |
| PX.Objects.TX.TaxReportLine | EntityType | Tax Report Line | LineNbr, TaxReportRevisionID, VendorID | 21 | 6 |  | PX_Objects_TX_TaxReportLine, TaxReportLine | members-06.md | 6040 | 34 |
| PX.Objects.TX.TaxReportSummary | EntityType | Tax Report Summary | BranchID, LineNbr, RevisionID | 11 | 0 |  | PX_Objects_TX_TaxReportSummary, TaxReportSummary | members-06.md | 6075 | 17 |
| PX.Objects.TX.TaxRev | EntityType | Tax Revision | RevisionID, TaxID | 20 | 5 |  | PX_Objects_TX_TaxRev, TaxRevision, TaxRev | members-06.md | 6093 | 31 |
| PX.Objects.TX.TaxTran | EntityType | Tax Transaction | Module, RecordID | 67 | 24 |  | PX_Objects_TX_TaxTran, TaxTransaction, TaxTran | members-06.md | 6125 | 98 |
| PX.Objects.TX.TaxTranReport | EntityType | Tax Transaction for Report | Module, RecordID | 2 | 0 | PX.Objects.TX.TaxTran | PX_Objects_TX_TaxTranReport, TaxTransactionforReport, TaxTranReport | members-06.md | 6224 | 10 |
| PX.Objects.TX.TaxYear | EntityType | Tax Year | OrganizationID, VendorID, Year | 9 | 4 |  | PX_Objects_TX_TaxYear, TaxYear | members-06.md | 6235 | 19 |
| PX.Objects.TX.TaxZone | EntityType | Tax Zone | TaxZoneID | 20 | 55 |  | PX_Objects_TX_TaxZone, TaxZone | members-06.md | 6255 | 82 |
| PX.Objects.TX.TaxZoneAddressMapping | EntityType | Tax Zone Address Mapping | CountryID, FromPostalCode, StateID, TaxZoneID | 14 | 5 |  | PX_Objects_TX_TaxZoneAddressMapping, TaxZoneAddressMapping | members-06.md | 6338 | 26 |
| PX.Objects.TX.TaxZoneDet | EntityType | Tax Zone Detail | TaxID, TaxZoneID | 9 | 4 |  | PX_Objects_TX_TaxZoneDet, TaxZoneDetail, TaxZoneDet | members-06.md | 6365 | 19 |
| PX.Objects.TX.TXImportFileData | EntityType |  | RecordID | 93 | 0 |  | PX_Objects_TX_TXImportFileData | members-06.md | 6385 | 98 |
| PX.Objects.TX.TXImportSettings | EntityType |  |  | 4 | 4 |  |  | members-06.md | 6484 | 12 |
| PX.Objects.TX.TXImportState | EntityType |  | StateCode | 9 | 4 |  | PX_Objects_TX_TXImportState | members-06.md | 6497 | 18 |
| PX.Objects.TX.TXImportZipFileData | EntityType |  | RecordID | 6 | 0 |  | PX_Objects_TX_TXImportZipFileData | members-06.md | 6516 | 11 |
| PX.Objects.TX.TXSetup | EntityType | Tax Preferences |  | 9 | 7 |  |  | members-06.md | 6528 | 21 |
| PX.Objects.WZ.PendingWZScenario | EntityType | Wizard Scenario | ScenarioID | 23 | 0 |  | PX_Objects_WZ_PendingWZScenario | members-06.md | 6550 | 30 |
| PX.Objects.WZ.WZSubTask | EntityType |  | TaskID | 27 | 0 |  | PX_Objects_WZ_WZSubTask | members-06.md | 6581 | 33 |
| PX.OidcClient.GraphExtensions.OidcUser | EntityType | External Identities | ProviderID, ProviderName, UserID | 6 | 1 |  | PX_OidcClient_GraphExtensions_OidcUser, ExternalIdentities, OidcUser | members-06.md | 6615 | 13 |
| PX.Olap.Maintenance.PivotField | EntityType | Pivot Field | PivotFieldID, PivotTableID, ScreenID | 32 | 5 |  | PX_Olap_Maintenance_PivotField, PivotField | members-06.md | 6629 | 44 |
| PX.Olap.Maintenance.PivotFieldPreferences | EntityType | Pivot Field Preferences | OwnerName, PivotFieldID, PivotTableID, ScreenID | 7 | 4 |  | PX_Olap_Maintenance_PivotFieldPreferences, PivotFieldPreferences | members-06.md | 6674 | 17 |
| PX.Olap.Maintenance.PivotTable | EntityType | Pivot Table | PivotTableID, ScreenID | 15 | 5 |  | PX_Olap_Maintenance_PivotTable, PivotTable | members-06.md | 6692 | 27 |
| PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment | EntityType | Avid Child Payment | ChildPaymentID, DocType, RefNbr | 18 | 3 |  | PX_PaymentProcessor_AvidXchange_DAC_PPAvidChildPayment, AvidChildPayment, PPAvidChildPayment | members-06.md | 6720 | 28 |
| PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount | EntityType | Avid Funding Account | ExternalPaymentProcessorID, RecordID | 19 | 4 |  | PX_PaymentProcessor_AvidXchange_DAC_PPAvidFundingAccount, AvidFundingAccount, PPAvidFundingAccount | members-06.md | 6749 | 30 |
| PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting | EntityType | Avid Processor Setting | ExternalPaymentProcessorID | 18 | 3 |  | PX_PaymentProcessor_AvidXchange_DAC_PPAvidSetting, AvidProcessorSetting, PPAvidSetting | members-06.md | 6780 | 28 |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomBill | EntityType | Payment Processor BILL Bills | DocType, ExternalPaymentProcessorID, OrganizationID, RefNbr | 12 | 6 |  | PX_PaymentProcessor_BillCom_DAC_PPBillcomBill, PaymentProcessorBILLBills, PPBillcomBill | members-06.md | 6809 | 24 |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount | EntityType | Payment Processor BILL Funding Accounts | ExternalAccountID, ExternalPaymentProcessorID, OrganizationID | 20 | 7 |  | PX_PaymentProcessor_BillCom_DAC_PPBillcomFundingAccount, PaymentProcessorBILLFundingAccounts, PPBillcomFundingAccount | members-06.md | 6834 | 34 |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser | EntityType | Payment Processor Account User | ExternalID, ExternalPaymentProcessorID, OrganizationID | 18 | 6 |  | PX_PaymentProcessor_BillCom_DAC_PPBillcomFundingAccountUser, PaymentProcessorAccountUser, PPBillcomFundingAccountUser | members-06.md | 6869 | 31 |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomUser | EntityType | Payment Processor BILL Users | ExternalPaymentProcessorID, OrganizationID, UserID | 17 | 6 |  | PX_PaymentProcessor_BillCom_DAC_PPBillcomUser, PaymentProcessorBILLUsers, PPBillcomUser | members-06.md | 6901 | 30 |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor | EntityType | Payment Processor BILL Vendors | BAccountID, ExternalPaymentProcessorID, LocationID, OrganizationID | 30 | 7 |  | PX_PaymentProcessor_BillCom_DAC_PPBillcomVendor, PaymentProcessorBILLVendors, PPBillcomVendor | members-06.md | 6932 | 44 |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation | EntityType | Payment Processor Vendors | BAccountID, ExternalPaymentProcessorID, LocationID, OrganizationID | 6 | 4 | PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor | PX_PaymentProcessor_BillCom_DAC_PPBillcomVendorLocation, PaymentProcessorVendors, PPBillcomVendorLocation | members-06.md | 6977 | 17 |
| PX.PaymentProcessor.BillCom.DAC.PPExternalSetting | EntityType | Payment Processor BILL Setting | ExternalPaymentProcessorID, OrganizationID | 20 | 10 |  | PX_PaymentProcessor_BillCom_DAC_PPExternalSetting, PaymentProcessorBILLSetting, PPExternalSetting | members-06.md | 6995 | 37 |
| PX.PaymentProcessor.ProcessorBase.DAC.APExternalPayment | EntityType | APExternalPayment | DocType, RefNbr | 3 | 0 | PX.Objects.AP.APPayment | PX_PaymentProcessor_ProcessorBase_DAC_APExternalPayment, APExternalPayment | members-06.md | 7033 | 10 |
| PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran | EntityType | External Payment Processor Transaction History | TranNbr | 25 | 3 |  | PX_PaymentProcessor_ProcessorBase_DAC_PPExternalTran, ExternalPaymentProcessorTransactionHistory, PPExternalTran | members-06.md | 7044 | 34 |
| PX.PaymentProcessorCommon.DAC.PPExternal | EntityType | External Payment Processor | ExternalPaymentProcessorID | 18 | 12 |  | PX_PaymentProcessorCommon_DAC_PPExternal, ExternalPaymentProcessor, PPExternal | members-06.md | 7079 | 37 |
| PX.PushNotifications.UI.DAC.DispatcherSettings | EntityType |  |  | 8 | 0 |  |  | members-06.md | 7117 | 12 |
| PX.PushNotifications.UI.DAC.DispatcherStatisticQueryDetail | EntityType | DispatcherStatisticQueryDetail | Field, Id, Query | 4 | 0 |  | PX_PushNotifications_UI_DAC_DispatcherStatisticQueryDetail, DispatcherStatisticQueryDetail | members-06.md | 7130 | 10 |
| PX.PushNotifications.UI.DAC.DispatcherStatistics | EntityType | DispatcherStatistics | Date, Hour, Id, Minute, QueueType, WebsiteId | 13 | 0 |  | PX_PushNotifications_UI_DAC_DispatcherStatistics, DispatcherStatistics | members-06.md | 7141 | 19 |
| PX.PushNotifications.UI.DAC.DispatcherStatisticSourceDetail | EntityType | DispatcherStatisticSourceDetail | Id, ScreenID, TableName | 4 | 0 |  | PX_PushNotifications_UI_DAC_DispatcherStatisticSourceDetail, DispatcherStatisticSourceDetail | members-06.md | 7161 | 10 |
| PX.PushNotifications.UI.DAC.DispatcherStatisticsPerHour | EntityType | DispatcherStatisticsPerHour | Date, Hour, Id, Minute, QueueType, WebsiteId | 0 | 0 | PX.PushNotifications.UI.DAC.DispatcherStatistics | PX_PushNotifications_UI_DAC_DispatcherStatisticsPerHour, DispatcherStatisticsPerHour | members-06.md | 7172 | 6 |
| PX.PushNotifications.UI.DAC.PushNotificationsErrors | EntityType |  | HookId, TransactionId | 6 | 0 |  | PX_PushNotifications_UI_DAC_PushNotificationsErrors | members-06.md | 7179 | 11 |
| PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend | EntityType | Push Notifications Failed To Send | HookId, Id, TransactionId | 9 | 1 |  | PX_PushNotifications_UI_DAC_PushNotificationsFailedToSend, PushNotificationsFailedToSend | members-06.md | 7191 | 17 |
| PX.PushNotifications.UI.DAC.PushNotificationsHook | EntityType | Push Notifications Hook | Name | 7 | 3 |  | PX_PushNotifications_UI_DAC_PushNotificationsHook, PushNotificationsHook | members-06.md | 7209 | 16 |
| PX.PushNotifications.UI.DAC.PushNotificationsSource | EntityType | Push Notifications Source | HookId, LineNbr | 11 | 3 |  | PX_PushNotifications_UI_DAC_PushNotificationsSource, PushNotificationsSource | members-06.md | 7226 | 20 |
| PX.PushNotifications.UI.DAC.PushNotificationsSourceGI | EntityType | Push Notifications Source | HookId, LineNbr | 0 | 0 | PX.PushNotifications.UI.DAC.PushNotificationsSource | PX_PushNotifications_UI_DAC_PushNotificationsSourceGI | members-06.md | 7247 | 6 |
| PX.PushNotifications.UI.DAC.PushNotificationsSourceIC | EntityType | Push Notifications Source | HookId, LineNbr | 0 | 0 | PX.PushNotifications.UI.DAC.PushNotificationsSource | PX_PushNotifications_UI_DAC_PushNotificationsSourceIC | members-06.md | 7254 | 6 |
| PX.PushNotifications.UI.DAC.PushNotificationsTrackingField | EntityType | Push Notification Tracked Field | FieldID, HookId, LineNbr, SourceType | 6 | 2 |  | PX_PushNotifications_UI_DAC_PushNotificationsTrackingField, PushNotificationTrackedField, PushNotificationsTrackingField | members-06.md | 7261 | 14 |
| PX.PushNotifications.UI.DAC.PushNotificationsTrackingFieldGI | EntityType | Push Notification Tracked Field | FieldID, HookId, LineNbr, SourceType | 0 | 0 | PX.PushNotifications.UI.DAC.PushNotificationsTrackingField | PX_PushNotifications_UI_DAC_PushNotificationsTrackingFieldGI, PushNotificationTrackedField1, PushNotificationsTrackingFieldGI | members-06.md | 7276 | 6 |
| PX.PushNotifications.UI.DAC.PushNotificationsTrackingFieldIC | EntityType | Push Notification Tracked Field | FieldID, HookId, LineNbr, SourceType | 0 | 0 | PX.PushNotifications.UI.DAC.PushNotificationsTrackingField | PX_PushNotifications_UI_DAC_PushNotificationsTrackingFieldIC, PushNotificationTrackedField2, PushNotificationsTrackingFieldIC | members-06.md | 7283 | 6 |
| PX.Salesforce.SFEntitySetup | EntityType |  | EntityType | 17 | 2 |  | PX_Salesforce_SFEntitySetup | members-06.md | 7290 | 25 |
| PX.Salesforce.SFSyncRecord | EntityType |  | SyncRecordID | 16 | 0 |  | PX_Salesforce_SFSyncRecord | members-06.md | 7316 | 22 |
| PX.ScreenPreferences.DAC.GridDataPresentation | EntityType |  | PresentationID | 19 | 2 |  | PX_ScreenPreferences_DAC_GridDataPresentation | members-06.md | 7339 | 27 |
| PX.SiteMap.DAC.SiteMap | EntityType | Site Map | NodeID | 4 | 0 | PX.SM.SiteMap | PX_SiteMap_DAC_SiteMap | members-06.md | 7367 | 12 |
| PX.SM.Alias.CustProject | EntityType |  | Name | 4 | 3 |  | PX_SM_Alias_CustProject | members-06.md | 7380 | 12 |
| PX.SM.AU.SMEmail | EntityType |  | NoteID | 34 | 7 |  | PX_SM_AU_SMEmail | members-06.md | 7393 | 47 |
| PX.SM.AUAction | EntityType |  | ActionName, MenuText, ScreenID | 14 | 2 |  | PX_SM_AUAction | members-06.md | 7441 | 21 |
| PX.SM.AUArchivingRule | EntityType | Archiving Rule | PrimaryType, ScreenID, TableType | 9 | 0 |  | PX_SM_AUArchivingRule, ArchivingRule, AUArchivingRule | members-06.md | 7463 | 15 |
| PX.SM.AUAuditField | EntityType |  | FieldName, ScreenID, TableName | 7 | 1 |  | PX_SM_AUAuditField | members-06.md | 7479 | 14 |
| PX.SM.AUAuditHistoryStatistics | EntityType | Audit History Statistics | TableName | 8 | 1 |  | PX_SM_AUAuditHistoryStatistics, AuditHistoryStatistics, AUAuditHistoryStatistics | members-06.md | 7494 | 16 |
| PX.SM.AUAuditHistoryStatisticsCalculationHistory | EntityType | Audit History Statistics Calculation History |  | 1 | 0 |  |  | members-06.md | 7511 | 6 |
| PX.SM.AUAuditSetup | EntityType |  | ScreenID | 12 | 3 |  | PX_SM_AUAuditSetup | members-06.md | 7518 | 21 |
| PX.SM.AUAuditTable | EntityType |  | ScreenID, TableName | 8 | 2 |  | PX_SM_AUAuditTable | members-06.md | 7540 | 16 |
| PX.SM.AUAuditValues | EntityType |  | BatchID, ChangeID | 1 | 0 | PX.SM.AuditHistory | PX_SM_AUAuditValues | members-06.md | 7557 | 8 |
| PX.SM.AUCombo | EntityType |  | FieldName, TableName, Value | 14 | 2 |  | PX_SM_AUCombo | members-06.md | 7566 | 21 |
| PX.SM.AUDefinition | EntityType |  | DefinitionID | 12 | 2 |  | PX_SM_AUDefinition | members-06.md | 7588 | 20 |
| PX.SM.AUDefinitionDetail | EntityType |  | DefinitionID, ScreenID | 14 | 2 |  | PX_SM_AUDefinitionDetail | members-06.md | 7609 | 22 |
| PX.SM.AuditHistory | EntityType |  | BatchID, ChangeID | 9 | 1 |  | PX_SM_AuditHistory | members-06.md | 7632 | 15 |
| PX.SM.AUNotification | EntityType |  | NotificationID, ScreenID | 32 | 9 |  | PX_SM_AUNotification | members-06.md | 7648 | 47 |
| PX.SM.AUNotificationField | EntityType |  | NotificationID, RowNbr, ScreenID | 14 | 3 |  | PX_SM_AUNotificationField | members-06.md | 7696 | 23 |
| PX.SM.AUNotificationFilter | EntityType |  | NotificationID, RowNbr, ScreenID | 22 | 3 |  | PX_SM_AUNotificationFilter | members-06.md | 7720 | 31 |
| PX.SM.AUNotificationHistory | EntityType |  | ExecutionDate, NotificationID, RefNoteID, ScreenID, Ticks | 36 | 2 |  | PX_SM_AUNotificationHistory | members-06.md | 7752 | 44 |
| PX.SM.AUNotificationParameter | EntityType |  | NotificationID, RowNbr, ScreenID | 15 | 3 |  | PX_SM_AUNotificationParameter | members-06.md | 7797 | 24 |
| PX.SM.AUNotificationTemplate | EntityType |  | ExecutionDate, NotificationID, RefNoteID, ScreenID | 13 | 1 |  | PX_SM_AUNotificationTemplate | members-06.md | 7822 | 20 |
| PX.SM.AUReportLink | EntityType | Report Link | RowNbr, ScheduleID, TemplateID | 3 | 1 |  | PX_SM_AUReportLink, ReportLink, AUReportLink | members-06.md | 7843 | 10 |
| PX.SM.AUSchedule | EntityType | Schedule | ScheduleID | 73 | 12 |  | PX_SM_AUSchedule, Schedule1, AUSchedule | members-06.md | 7854 | 92 |
| PX.SM.AUScheduleExecution | EntityType |  | ExecutionDate, ScheduleID | 11 | 1 |  | PX_SM_AUScheduleExecution | members-06.md | 7947 | 18 |
| PX.SM.AUScheduleFill | EntityType | Schedule Filter Values | RowNbr, ScheduleID | 16 | 4 |  | PX_SM_AUScheduleFill, ScheduleFilterValues, AUScheduleFill | members-06.md | 7966 | 27 |
| PX.SM.AUScheduleFilter | EntityType | Schedule Filter | RowNbr, ScheduleID | 20 | 4 |  | PX_SM_AUScheduleFilter, ScheduleFilter, AUScheduleFilter | members-06.md | 7994 | 31 |
| PX.SM.AUScheduleHistory | EntityType |  | ExecutionDate, RefNoteID, ScheduleID | 10 | 1 |  | PX_SM_AUScheduleHistory | members-06.md | 8026 | 17 |
| PX.SM.AUScheduleTemplate | EntityType |  | ScheduleID, TemplateID | 14 | 2 |  | PX_SM_AUScheduleTemplate | members-06.md | 8044 | 22 |
| PX.SM.AUScreenAction | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenAction | members-06.md | 8067 | 5 |
| PX.SM.AUScreenActionBaseState | EntityType |  | ActionName, ScreenID | 53 | 5 |  | PX_SM_AUScreenActionBaseState | members-06.md | 8073 | 63 |
| PX.SM.AUScreenActionProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenActionProp | members-06.md | 8137 | 5 |
| PX.SM.AUScreenActionState | EntityType |  | ActionName, ScreenID | 1 | 0 | PX.SM.AUScreenActionBaseState | PX_SM_AUScreenActionState | members-06.md | 8143 | 7 |
| PX.SM.AUScreenCondition | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenCondition | members-06.md | 8151 | 5 |
| PX.SM.AUScreenConditionFilter | EntityType |  | ConditionID, ProjectID, RowNbr, ScreenID | 20 | 3 |  | PX_SM_AUScreenConditionFilter | members-06.md | 8157 | 28 |
| PX.SM.AUScreenConditionLineState | EntityType |  | ConditionID, LineNbr, ScreenID | 12 | 1 |  | PX_SM_AUScreenConditionLineState | members-06.md | 8186 | 18 |
| PX.SM.AUScreenConditionState | EntityType |  | ConditionID, ScreenID | 11 | 1 |  | PX_SM_AUScreenConditionState | members-06.md | 8205 | 18 |
| PX.SM.AUScreenDefinition | EntityType |  | ProjectID, ScreenID | 18 | 3 |  | PX_SM_AUScreenDefinition | members-06.md | 8224 | 26 |
| PX.SM.AUScreenEvent | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 1 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenEvent | members-06.md | 8251 | 8 |
| PX.SM.AUScreenEventDef | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenEventDef | members-06.md | 8260 | 5 |
| PX.SM.AUScreenEventEndCondition | EntityType |  | ConditionID, ProjectID, RowNbr, ScreenID | 0 | 0 | PX.SM.AUScreenConditionFilter | PX_SM_AUScreenEventEndCondition | members-06.md | 8266 | 5 |
| PX.SM.AUScreenEventProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenEventProp | members-06.md | 8272 | 5 |
| PX.SM.AUScreenEventStartCondition | EntityType |  | ConditionID, ProjectID, RowNbr, ScreenID | 0 | 0 | PX.SM.AUScreenConditionFilter | PX_SM_AUScreenEventStartCondition | members-06.md | 8278 | 5 |
| PX.SM.AUScreenEventSubscriber | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 6 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenEventSubscriber | members-06.md | 8284 | 13 |
| PX.SM.AUScreenEventSubscriberDef | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenEventSubscriberDef | members-06.md | 8298 | 5 |
| PX.SM.AUScreenEventSubscriberExecCondition | EntityType |  | ConditionID, ProjectID, RowNbr, ScreenID | 0 | 0 | PX.SM.AUScreenConditionFilter | PX_SM_AUScreenEventSubscriberExecCondition | members-06.md | 8304 | 5 |
| PX.SM.AUScreenEventSubscriberProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenEventSubscriberProp | members-06.md | 8310 | 5 |
| PX.SM.AUScreenExtraAction | EntityType |  | ActionName, ScreenID | 16 | 0 |  | PX_SM_AUScreenExtraAction | members-06.md | 8316 | 21 |
| PX.SM.AUScreenFieldForm | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenFieldForm | members-06.md | 8338 | 5 |
| PX.SM.AUScreenFieldFormProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenFieldFormProp | members-06.md | 8344 | 5 |
| PX.SM.AUScreenFieldState | EntityType |  | FieldName, ScreenID, TableName | 25 | 0 |  | PX_SM_AUScreenFieldState | members-06.md | 8350 | 30 |
| PX.SM.AUScreenForm | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 3 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenForm | members-06.md | 8381 | 10 |
| PX.SM.AUScreenFormProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenFormProp | members-06.md | 8392 | 5 |
| PX.SM.AUScreenInquiry | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenInquiry | members-06.md | 8398 | 5 |
| PX.SM.AUScreenInquiryNavProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenInquiryNavProp | members-06.md | 8404 | 5 |
| PX.SM.AUScreenInquiryProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenInquiryProp | members-06.md | 8410 | 5 |
| PX.SM.AUScreenItem | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 19 | 7 |  | PX_SM_AUScreenItem | members-06.md | 8416 | 32 |
| PX.SM.AUScreenItemProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 19 | 3 |  | PX_SM_AUScreenItemProp | members-06.md | 8449 | 28 |
| PX.SM.AUScreenNavigationActionState | EntityType |  | ActionName, ScreenID | 6 | 0 | PX.SM.AUScreenActionBaseState | PX_SM_AUScreenNavigationActionState | members-06.md | 8478 | 12 |
| PX.SM.AUScreenNavigationParameterState | EntityType |  | ActionName, FieldName, ScreenID | 9 | 0 |  | PX_SM_AUScreenNavigationParameterState | members-06.md | 8491 | 14 |
| PX.SM.AUScreenPopup | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenPopup | members-06.md | 8506 | 5 |
| PX.SM.AUScreenPopupField | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenPopupField | members-06.md | 8512 | 5 |
| PX.SM.AUScreenPopupFieldProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenPopupFieldProp | members-06.md | 8518 | 5 |
| PX.SM.AUScreenPopupProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenPopupProp | members-06.md | 8524 | 5 |
| PX.SM.AUScreenReport | EntityType |  | ItemCD, ItemType, ParentID, ProjectID, ScreenID | 0 | 0 | PX.SM.AUScreenItem | PX_SM_AUScreenReport | members-06.md | 8530 | 5 |
| PX.SM.AUScreenReportProp | EntityType |  | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | 0 | 0 | PX.SM.AUScreenItemProp | PX_SM_AUScreenReportProp | members-06.md | 8536 | 5 |
| PX.SM.AUStep | EntityType |  | ScreenID, StepID | 27 | 7 |  | PX_SM_AUStep | members-06.md | 8542 | 40 |
| PX.SM.AUStepAction | EntityType |  | RowNbr, ScreenID, StepID | 37 | 6 |  | PX_SM_AUStepAction | members-06.md | 8583 | 49 |
| PX.SM.AUStepCombo | EntityType |  | FieldName, RowNbr, ScreenID, StepID, TableName | 16 | 3 |  | PX_SM_AUStepCombo | members-06.md | 8633 | 25 |
| PX.SM.AUStepField | EntityType |  | RowNbr, ScreenID, StepID | 23 | 3 |  | PX_SM_AUStepField | members-06.md | 8659 | 32 |
| PX.SM.AUStepFill | EntityType |  | ActionName, MenuText, RowNbr, ScreenID, StepID | 18 | 3 |  | PX_SM_AUStepFill | members-06.md | 8692 | 26 |
| PX.SM.AUStepFilter | EntityType |  | RowNbr, ScreenID, StepID | 21 | 3 |  | PX_SM_AUStepFilter | members-06.md | 8719 | 30 |
| PX.SM.AUTableDefinition | EntityType |  | ProjectID, TableName | 11 | 3 |  | PX_SM_AUTableDefinition | members-06.md | 8750 | 19 |
| PX.SM.AUTableExtension | EntityType |  | FieldName, ProjectID, TableName | 14 | 3 |  | PX_SM_AUTableExtension | members-06.md | 8770 | 23 |
| PX.SM.AUTableExtensionState | EntityType |  | FieldName, StateID, TableName | 24 | 0 |  | PX_SM_AUTableExtensionState | members-06.md | 8794 | 30 |
| PX.SM.AUTemplate | EntityType |  | TemplateID | 13 | 3 |  | PX_SM_AUTemplate | members-06.md | 8825 | 22 |
| PX.SM.AUTemplateData | EntityType |  | OrderId, TemplateId | 10 | 1 |  | PX_SM_AUTemplateData | members-06.md | 8848 | 17 |
| PX.SM.AUWorkflow | EntityType | Workflow | ScreenID, WorkflowGUID | 13 | 2 |  | PX_SM_AUWorkflow, Workflow, AUWorkflow | members-06.md | 8866 | 21 |
| PX.SM.AUWorkflowActionParam | EntityType | Workflow Action Parameter | ActionName, Parameter, ScreenID | 11 | 1 |  | PX_SM_AUWorkflowActionParam, WorkflowActionParameter, AUWorkflowActionParam | members-06.md | 8888 | 18 |
| PX.SM.AUWorkflowActionSequence | EntityType | Workflow Action Sequence | Condition, NextActionName, PrevActionName, ScreenID | 10 | 1 |  | PX_SM_AUWorkflowActionSequence, WorkflowActionSequence, AUWorkflowActionSequence | members-06.md | 8907 | 17 |
| PX.SM.AUWorkflowActionSequenceFormFieldValue | EntityType | Dialog Box Value | Condition, FieldName, NextActionName, PrevActionName, ScreenID | 11 | 0 |  | PX_SM_AUWorkflowActionSequenceFormFieldValue, DialogBoxValue, AUWorkflowActionSequenceFormFieldValue | members-06.md | 8925 | 17 |
| PX.SM.AUWorkflowActionUpdateField | EntityType | Workflow Action Field | ActionName, FieldName, ScreenID | 11 | 1 |  | PX_SM_AUWorkflowActionUpdateField, WorkflowActionField, AUWorkflowActionUpdateField | members-06.md | 8943 | 18 |
| PX.SM.AUWorkflowDefinition | EntityType | Workflow Definition | ScreenID | 13 | 1 |  | PX_SM_AUWorkflowDefinition, WorkflowDefinition, AUWorkflowDefinition | members-06.md | 8962 | 21 |
| PX.SM.AUWorkflowForm | EntityType |  | FormName, Screen | 10 | 0 |  | PX_SM_AUWorkflowForm | members-06.md | 8984 | 15 |
| PX.SM.AUWorkflowFormField | EntityType | Workflow Form Field | FieldName, FormName, Screen | 35 | 0 |  | PX_SM_AUWorkflowFormField, WorkflowFormField, AUWorkflowFormField | members-06.md | 9000 | 41 |
| PX.SM.AUWorkflowHandler | EntityType | Workflow Handler | HandlerName, ScreenID | 22 | 1 |  | PX_SM_AUWorkflowHandler, WorkflowHandler, AUWorkflowHandler | members-06.md | 9042 | 29 |
| PX.SM.AUWorkflowHandlerUpdateField | EntityType | Workflow Handler Field | FieldName, HandlerName, ScreenID | 8 | 1 |  | PX_SM_AUWorkflowHandlerUpdateField, WorkflowHandlerField, AUWorkflowHandlerUpdateField | members-06.md | 9072 | 15 |
| PX.SM.AUWorkflowOnEnterStateField | EntityType | Workflow Update Field On Enter State | FieldName, ScreenID, StateName, WorkflowGUID | 12 | 1 |  | PX_SM_AUWorkflowOnEnterStateField, WorkflowUpdateFieldOnEnterState, AUWorkflowOnEnterStateField | members-06.md | 9088 | 19 |
| PX.SM.AUWorkflowOnLeaveStateField | EntityType | Workflow Update Field On Leave State | FieldName, ScreenID, StateName, WorkflowGUID | 12 | 1 |  | PX_SM_AUWorkflowOnLeaveStateField, WorkflowUpdateFieldOnLeaveState, AUWorkflowOnLeaveStateField | members-06.md | 9108 | 19 |
| PX.SM.AUWorkflowState | EntityType | Workflow State | Identifier, ScreenID, WorkflowGUID | 21 | 8 |  | PX_SM_AUWorkflowState, WorkflowState, AUWorkflowState | members-06.md | 9128 | 35 |
| PX.SM.AUWorkflowStateAction | EntityType | State Action | ActionName, ScreenID, StateName, WorkflowGUID | 18 | 1 |  | PX_SM_AUWorkflowStateAction, StateAction, AUWorkflowStateAction | members-06.md | 9164 | 25 |
| PX.SM.AUWorkflowStateActionField | EntityType | Workflow Action Field | ActionName, FieldName, ScreenID | 11 | 1 |  | PX_SM_AUWorkflowStateActionField, WorkflowActionField1, AUWorkflowStateActionField | members-06.md | 9190 | 18 |
| PX.SM.AUWorkflowStateActionParam | EntityType | Workflow Action Parameter | ActionName, Parameter, ScreenID | 11 | 1 |  | PX_SM_AUWorkflowStateActionParam, WorkflowActionParameter1, AUWorkflowStateActionParam | members-06.md | 9209 | 18 |
| PX.SM.AUWorkflowStateEventHandler | EntityType | State Event Handler | HandlerName, ScreenID, StateName, WorkflowGUID | 8 | 1 |  | PX_SM_AUWorkflowStateEventHandler, StateEventHandler, AUWorkflowStateEventHandler | members-06.md | 9228 | 15 |
| PX.SM.AUWorkflowStateProperty | EntityType | State Property | FieldName, ObjectName, ScreenID, StateName, WorkflowGUID | 19 | 1 |  | PX_SM_AUWorkflowStateProperty, StateProperty, AUWorkflowStateProperty | members-06.md | 9244 | 26 |
| PX.SM.AUWorkflowStateStatusCondition | EntityType | State Status Condition | Condition, ScreenID, StateName, WorkflowGUID | 10 | 1 |  | PX_SM_AUWorkflowStateStatusCondition, StateStatusCondition, AUWorkflowStateStatusCondition | members-06.md | 9271 | 17 |
| PX.SM.AUWorkflowTransition | EntityType | Workflow Transition | ScreenID, TransitionID, WorkflowGUID | 23 | 2 |  | PX_SM_AUWorkflowTransition, WorkflowTransition, AUWorkflowTransition | members-06.md | 9289 | 31 |
| PX.SM.AUWorkflowTransitionField | EntityType | Transition Update Fields After | FieldName, ScreenID, TransitionID, WorkflowGUID | 12 | 1 |  | PX_SM_AUWorkflowTransitionField, TransitionUpdateFieldsAfter, AUWorkflowTransitionField | members-06.md | 9321 | 19 |
| PX.SM.BlobProviderSettings | EntityType |  | Name | 2 | 0 |  | PX_SM_BlobProviderSettings | members-06.md | 9341 | 7 |
| PX.SM.BlobStorageConfig | EntityType |  |  | 3 | 0 |  |  | members-06.md | 9349 | 7 |
| PX.SM.BPEventInProject | EntityType | Business Process Event | Name | 1 | 0 | PX.BusinessProcess.DAC.BPEvent | PX_SM_BPEventInProject | members-06.md | 9357 | 8 |
| PX.SM.Branch | EntityType |  | BranchCD, RoleName | 8 | 221 |  | PX_SM_Branch | members-06.md | 9366 | 235 |
| PX.SM.Certificate | EntityType | Certificate | Name | 4 | 6 |  | PX_SM_Certificate, Certificate | members-06.md | 9602 | 17 |
| PX.SM.CetrificateFile | EntityType | Certificate | Name | 1 | 0 | PX.SM.Certificate | PX_SM_CetrificateFile | members-06.md | 9620 | 8 |
| PX.SM.CompanyByTableSize | EntityType | Table Size | Company, TableName | 3 | 0 | PX.SM.TableSize | PX_SM_CompanyByTableSize | members-06.md | 9629 | 11 |
| PX.SM.CustMobileSiteMap | EntityType |  | ObjectID | 2 | 0 | PX.SM.CustObject | PX_SM_CustMobileSiteMap | members-06.md | 9641 | 9 |
| PX.SM.CustObject | EntityType |  | ObjectID | 19 | 2 |  | PX_SM_CustObject | members-06.md | 9651 | 27 |
| PX.SM.CustObjectMaint | EntityType |  | ObjectID | 8 | 0 | PX.SM.CustObject | PX_SM_CustObjectMaint | members-06.md | 9679 | 15 |
| PX.SM.CustProject | EntityType | Edit Project Items | Name | 21 | 3 |  | PX_SM_CustProject, EditProjectItems, CustProject | members-06.md | 9695 | 31 |
| PX.SM.CustScreen | EntityType |  | ObjectID | 2 | 0 | PX.SM.CustObject | PX_SM_CustScreen | members-06.md | 9727 | 9 |
| PX.SM.CustScreenConfiguration | EntityType |  | ObjectID | 2 | 0 | PX.SM.CustObject | PX_SM_CustScreenConfiguration | members-06.md | 9737 | 9 |
| PX.SM.CustUserFieldsObject | EntityType |  | ObjectID | 2 | 0 | PX.SM.CustObject | PX_SM_CustUserFieldsObject | members-06.md | 9747 | 9 |
| PX.SM.DashboardInProject | EntityType | Dashboard | Name | 1 | 0 | PX.Dashboards.DAC.Dashboard | PX_SM_DashboardInProject | members-06.md | 9757 | 8 |
| PX.SM.DashboardV2InProject | EntityType | Dashboard | Name | 1 | 0 | PX.Dashboards.DAC.DashboardV2 | PX_SM_DashboardV2InProject | members-06.md | 9766 | 8 |
| PX.SM.DateInfo | EntityType | Date Info | Date | 12 | 0 |  | PX_SM_DateInfo, DateInfo | members-06.md | 9775 | 19 |
| PX.SM.EMailAccount | EntityType | Email Account | EmailAccountID | 81 | 30 |  | PX_SM_EMailAccount, EmailAccount | members-06.md | 9795 | 118 |
| PX.SM.EMailAccountStatistics | EntityType | Email Account Statistics | EmailAccountID | 3 | 1 |  | PX_SM_EMailAccountStatistics, EmailAccountStatistics | members-06.md | 9914 | 10 |
| PX.SM.EMailSyncAccount | EntityType |  | EmployeeID, ServerID | 36 | 3 |  | PX_SM_EMailSyncAccount | members-06.md | 9925 | 45 |
| PX.SM.EMailSyncAccountPreferences | EntityType |  | EmployeeID, PolicyName | 4 | 2 |  | PX_SM_EMailSyncAccountPreferences | members-06.md | 9971 | 11 |
| PX.SM.EMailSyncLog | EntityType |  | EventID | 7 | 1 |  | PX_SM_EMailSyncLog | members-06.md | 9983 | 13 |
| PX.SM.EMailSyncPolicy | EntityType |  | PolicyName | 37 | 6 |  | PX_SM_EMailSyncPolicy | members-06.md | 9997 | 48 |
| PX.SM.EMailSyncReference | EntityType |  | Address, NoteID, ServerID | 7 | 1 |  | PX_SM_EMailSyncReference | members-06.md | 10046 | 13 |
| PX.SM.EMailSyncServer | EntityType |  | AccountCD | 21 | 5 |  | PX_SM_EMailSyncServer | members-06.md | 10060 | 31 |
| PX.SM.EntityEndpointInProject | EntityType |  | GateVersion, InterfaceName | 6 | 2 |  | PX_SM_EntityEndpointInProject | members-06.md | 10092 | 13 |
| PX.SM.EulaStatus | EntityType |  |  | 3 | 0 |  |  | members-06.md | 10106 | 7 |
| PX.SM.GiDesignInProject | EntityType | Generic Inquiry | Name | 1 | 0 | PX.Data.Maintenance.GI.GIDesign | PX_SM_GiDesignInProject | members-06.md | 10114 | 8 |
| PX.SM.Instance | EntityType | Application | InstallationID | 3 | 0 |  | PX_SM_Instance, Application, Instance | members-06.md | 10123 | 9 |
| PX.SM.KBFeedback | EntityType |  | FeedbackID | 14 | 2 |  | PX_SM_KBFeedback | members-06.md | 10133 | 22 |
| PX.SM.KBResponse | EntityType |  | ResponseID | 15 | 3 |  | PX_SM_KBResponse | members-06.md | 10156 | 23 |
| PX.SM.KBResponseMark | EntityType |  | Mark | 9 | 2 |  | PX_SM_KBResponseMark | members-06.md | 10180 | 16 |
| PX.SM.KBResponseSummary | EntityType |  | PageID | 12 | 3 |  | PX_SM_KBResponseSummary | members-06.md | 10197 | 20 |
| PX.SM.Licensing | EntityType |  |  | 7 | 0 |  |  | members-06.md | 10218 | 11 |
| PX.SM.Locale | EntityType | Locale | LocaleName | 10 | 19 |  | PX_SM_Locale, Locale | members-06.md | 10230 | 36 |
| PX.SM.LocaleFormat | EntityType | Custom Locale Format | FormatID | 11 | 1 |  | PX_SM_LocaleFormat, CustomLocaleFormat, LocaleFormat | members-06.md | 10267 | 18 |
| PX.SM.LoginTrace | EntityType | Login Trace | LoginTraceID | 10 | 2 |  | PX_SM_LoginTrace, LoginTrace | members-06.md | 10286 | 18 |
| PX.SM.MobileSiteMap | EntityType | Mobile Site Map | ScreenID, Type | 10 | 2 |  | PX_SM_MobileSiteMap, MobileSiteMap | members-06.md | 10305 | 18 |
| PX.SM.MobileSiteMapInProject | EntityType | Mobile Site Map | ScreenID, Type | 1 | 0 | PX.SM.MobileSiteMap | PX_SM_MobileSiteMapInProject | members-06.md | 10324 | 8 |
| PX.SM.MobileSiteMapWorkspacesInProject | EntityType |  | Name | 8 | 0 |  | PX_SM_MobileSiteMapWorkspacesInProject | members-06.md | 10333 | 13 |
| PX.SM.MUIScreenInProject | EntityType | Screen | IsPortal, NodeID, WorkspaceID | 1 | 0 | PX.Web.UI.Frameset.Model.DAC.MUIScreen | PX_SM_MUIScreenInProject | members-06.md | 10347 | 8 |
| PX.SM.MUITileInProject | EntityType | Tile | IsPortal, TileID | 1 | 0 | PX.Web.UI.Frameset.Model.DAC.MUITile | PX_SM_MUITileInProject | members-06.md | 10356 | 8 |
| PX.SM.Neighbour | EntityType |  | LeftEntityType, RightEntityType | 6 | 0 |  | PX_SM_Neighbour | members-06.md | 10365 | 11 |
| PX.SM.Notification | EntityType | Notification | NotificationID | 26 | 34 |  | PX_SM_Notification, Notification | members-06.md | 10377 | 67 |
| PX.SM.NotificationReport | EntityType | Notification Report | ReportID | 11 | 3 |  | PX_SM_NotificationReport, NotificationReport | members-06.md | 10445 | 21 |
| PX.SM.NotificationReportParameter | EntityType | Notification Report Parameter | Name, ReportID | 7 | 1 |  | PX_SM_NotificationReportParameter, NotificationReportParameter | members-06.md | 10467 | 15 |
| PX.SM.OAuthClient | EntityType |  | ClientID | 9 | 0 |  | PX_SM_OAuthClient | members-06.md | 10483 | 15 |
| PX.SM.PortalMap | EntityType | Portal Map | NodeID | 0 | 0 | PX.SM.SiteMap | PX_SM_PortalMap, PortalMap | members-06.md | 10499 | 6 |
| PX.SM.PreferencesEmail | EntityType |  |  | 25 | 11 |  |  | members-06.md | 10506 | 40 |
| PX.SM.PreferencesGeneral | EntityType | General Preferences |  | 47 | 5 |  |  | members-06.md | 10547 | 57 |
| PX.SM.PreferencesIdentityProvider | EntityType |  | InstanceKey, ProviderName | 6 | 0 |  | PX_SM_PreferencesIdentityProvider | members-06.md | 10605 | 11 |
| PX.SM.PreferencesSecurity | EntityType |  |  | 40 | 5 |  |  | members-06.md | 10617 | 49 |
| PX.SM.PushNotificationInProject | EntityType | Push Notifications Hook | Name | 1 | 0 | PX.PushNotifications.UI.DAC.PushNotificationsHook | PX_SM_PushNotificationInProject | members-06.md | 10667 | 8 |
| PX.SM.Reduced.UploadFile | EntityType |  | FileID | 2 | 4 |  | PX_SM_Reduced_UploadFile | members-06.md | 10676 | 11 |
| PX.SM.Reduced.WikiFileInPage | EntityType |  | PageID | 1 | 0 |  | PX_SM_Reduced_WikiFileInPage | members-06.md | 10688 | 6 |
| PX.SM.Reduced.WikiPage | EntityType |  | PageID | 1 | 7 |  | PX_SM_Reduced_WikiPage | members-06.md | 10695 | 13 |
| PX.SM.RelationDetail | EntityType | Relation Detail | GroupName | 0 | 0 | PX.SM.RelationGroup | PX_SM_RelationDetail, RelationDetail | members-06.md | 10709 | 6 |
| PX.SM.RelationGroup | EntityType | Relation Group | GroupName | 8 | 3 |  | PX_SM_RelationGroup, RelationGroup | members-06.md | 10716 | 18 |
| PX.SM.RelationHeader | EntityType | Relation Header | GroupName | 1 | 0 | PX.SM.RelationGroup | PX_SM_RelationHeader, RelationHeader | members-06.md | 10735 | 9 |
| PX.SM.ReportDefinitionInProject | EntityType | Report | ReportCode | 1 | 0 | PX.CS.RMReport | PX_SM_ReportDefinitionInProject | members-06.md | 10745 | 8 |
| PX.SM.ReportUsers | EntityType | User | Username | 1 | 0 | PX.SM.Users | PX_SM_ReportUsers | members-06.md | 10754 | 9 |
| PX.SM.RoleActiveDirectory | EntityType | Role Active Directory | GroupID, Role | 5 | 1 |  | PX_SM_RoleActiveDirectory, RoleActiveDirectory | members-06.md | 10764 | 13 |
| PX.SM.RoleClaims | EntityType | Role Claims | GroupID, Role | 2 | 1 |  | PX_SM_RoleClaims, RoleClaims | members-06.md | 10778 | 9 |
| PX.SM.Roles | EntityType | Role | ApplicationName, Rolename | 10 | 18 |  | PX_SM_Roles, Role, Roles | members-06.md | 10788 | 34 |
| PX.SM.RolesInCache | EntityType | Roles In Cache | ApplicationName, Cachetype, Rolename, ScreenID | 11 | 4 |  | PX_SM_RolesInCache, RolesInCache | members-06.md | 10823 | 21 |
| PX.SM.RolesInGraph | EntityType | Roles In Graph | ApplicationName, Rolename, ScreenID | 10 | 4 |  | PX_SM_RolesInGraph, RolesInGraph | members-06.md | 10845 | 20 |
| PX.SM.RolesInMember | EntityType | Roles In Member | ApplicationName, Cachetype, Membername, Rolename, ScreenID | 12 | 4 |  | PX_SM_RolesInMember, RolesInMember | members-06.md | 10866 | 22 |
| PX.SM.RowCodeFile | EntityType |  | ObjectID | 1 | 0 | PX.SM.CustObject | PX_SM_RowCodeFile | members-06.md | 10889 | 8 |
| PX.SM.RowMobileSiteMap | EntityType |  | ObjectID | 3 | 0 | PX.SM.CustObject | PX_SM_RowMobileSiteMap | members-06.md | 10898 | 10 |
| PX.SM.ScreensInUserField | EntityType |  | AttributeID, ScreenID, TypeValue | 19 | 0 |  | PX_SM_ScreensInUserField | members-06.md | 10909 | 25 |
| PX.SM.SelectedFilter | EntityType | Filter Header | FilterID, ScreenID, ViewName | 1 | 0 | PX.Data.FilterHeader | PX_SM_SelectedFilter | members-06.md | 10935 | 8 |
| PX.SM.SelectedImportScenario | EntityType | Mapping | Name | 1 | 0 | PX.Api.SYMapping | PX_SM_SelectedImportScenario | members-06.md | 10944 | 8 |
| PX.SM.SelectedLocale | EntityType | Locale | LocaleName | 0 | 0 | PX.SM.Locale | PX_SM_SelectedLocale | members-06.md | 10953 | 6 |
| PX.SM.SimpleWikiPage | EntityType |  | PageID | 0 | 0 | PX.SM.WikiPage | PX_SM_SimpleWikiPage | members-06.md | 10960 | 5 |
| PX.SM.SiteMap | EntityType | Site Map | NodeID | 16 | 34 |  | PX_SM_SiteMap, SiteMap | members-06.md | 10966 | 57 |
| PX.SM.SiteMapEx | EntityType | Site Map | NodeID | 1 | 0 | PX.SM.SiteMap | PX_SM_SiteMapEx | members-06.md | 11024 | 8 |
| PX.SM.SiteMapInProject | EntityType | Site Map | NodeID | 1 | 0 | PX.SM.SiteMap | PX_SM_SiteMapInProject | members-06.md | 11033 | 8 |
| PX.SM.SMCalendarSettings | EntityType | Calendar Settings | PKID | 11 | 2 |  | PX_SM_SMCalendarSettings, CalendarSettings, SMCalendarSettings | members-06.md | 11042 | 19 |
| PX.SM.SMPerformanceInfo | EntityType | Performance Info | RecordId | 45 | 2 |  | PX_SM_SMPerformanceInfo, PerformanceInfo, SMPerformanceInfo | members-06.md | 11062 | 54 |
| PX.SM.SMPerformanceInfoSQL | EntityType |  | ParentId, RecordId | 10 | 1 |  | PX_SM_SMPerformanceInfoSQL | members-06.md | 11117 | 16 |
| PX.SM.SMPerformanceInfoSQLText | EntityType | SQL Text Performance Info | RecordId | 5 | 0 |  | PX_SM_SMPerformanceInfoSQLText, SQLTextPerformanceInfo, SMPerformanceInfoSQLText | members-06.md | 11134 | 11 |
| PX.SM.SMPerformanceInfoSQLWithTables | EntityType | SQL With Tables Performance Info | ParentId, RecordId | 8 | 0 | PX.SM.SMPerformanceInfoSQL | PX_SM_SMPerformanceInfoSQLWithTables, SQLWithTablesPerformanceInfo, SMPerformanceInfoSQLWithTables | members-06.md | 11146 | 16 |
| PX.SM.SMPerformanceInfoStackTrace | EntityType | Stack Trace Performance Info | RecordId | 2 | 1 |  | PX_SM_SMPerformanceInfoStackTrace, StackTracePerformanceInfo, SMPerformanceInfoStackTrace | members-06.md | 11163 | 9 |
| PX.SM.SMPerformanceInfoTraceEvents | EntityType | Trace Events Performance Info | ParentId, RecordId | 13 | 3 |  | PX_SM_SMPerformanceInfoTraceEvents, TraceEventsPerformanceInfo, SMPerformanceInfoTraceEvents | members-06.md | 11173 | 22 |
| PX.SM.SMPerformanceInfoTraceMessages | EntityType | Trace Messages Performance Info | RecordId | 2 | 1 |  | PX_SM_SMPerformanceInfoTraceMessages, TraceMessagesPerformanceInfo, SMPerformanceInfoTraceMessages | members-06.md | 11196 | 9 |
| PX.SM.SMPerformanceInfoTraceWithMessages | EntityType | Trace Events Performance Info | ParentId, RecordId | 6 | 0 | PX.SM.SMPerformanceInfoTraceEvents | PX_SM_SMPerformanceInfoTraceWithMessages | members-06.md | 11206 | 14 |
| PX.SM.SMPrinter | EntityType | Printers | DeviceHubID, PrinterName | 17 | 9 |  | PX_SM_SMPrinter, Printers, SMPrinter | members-06.md | 11221 | 33 |
| PX.SM.SMPrintJob | EntityType | Print Job | JobID | 19 | 4 |  | PX_SM_SMPrintJob, PrintJob, SMPrintJob | members-06.md | 11255 | 30 |
| PX.SM.SMPrintJobParameter | EntityType | Print Job Parameter | JobID, ParameterName | 3 | 1 |  | PX_SM_SMPrintJobParameter, PrintJobParameter, SMPrintJobParameter | members-06.md | 11286 | 10 |
| PX.SM.SMScale | EntityType | Scale | DeviceHubID, ScaleID | 15 | 6 |  | PX_SM_SMScale, Scale, SMScale | members-06.md | 11297 | 28 |
| PX.SM.SMScanJob | EntityType | Scan Job | ScanJobID | 29 | 4 |  | PX_SM_SMScanJob, ScanJob, SMScanJob | members-06.md | 11326 | 40 |
| PX.SM.SMScanJobParameter | EntityType | Scan Job Parameters | LineNbr, ParameterName, ScanJobID | 5 | 1 |  | PX_SM_SMScanJobParameter, ScanJobParameters, SMScanJobParameter | members-06.md | 11367 | 12 |
| PX.SM.SMScanner | EntityType | Scanners | DeviceHubID, ScannerName | 20 | 4 |  | PX_SM_SMScanner, Scanners, SMScanner | members-06.md | 11380 | 30 |
| PX.SM.SpaceUsageCalculationHistory | EntityType | Space Usage Calculation History | PkID | 15 | 2 |  | PX_SM_SpaceUsageCalculationHistory, SpaceUsageCalculationHistory | members-06.md | 11411 | 24 |
| PX.SM.Standalone.EMailAccount | EntityType |  |  | 3 | 30 |  |  | members-06.md | 11436 | 37 |
| PX.SM.SyncTimeTag | EntityType |  | NoteID | 2 | 0 |  | PX_SM_SyncTimeTag | members-06.md | 11474 | 7 |
| PX.SM.TablesCompanySize | EntityType | Table Size | Company, TableName | 3 | 0 | PX.SM.TableSize | PX_SM_TablesCompanySize | members-06.md | 11482 | 11 |
| PX.SM.TableSize | EntityType | Table Size | Company, TableName | 8 | 0 |  | PX_SM_TableSize, TableSize | members-06.md | 11494 | 15 |
| PX.SM.TablesSnapshotSize | EntityType | Table Size | Company, TableName | 3 | 0 | PX.SM.TableSize | PX_SM_TablesSnapshotSize | members-06.md | 11510 | 11 |
| PX.SM.TaskTemplate | EntityType | Task Template | TaskTemplateID | 21 | 5 |  | PX_SM_TaskTemplate, TaskTemplate | members-06.md | 11522 | 33 |
| PX.SM.TaskTemplateSetting | EntityType | Task Template Setting | LineNbr, TaskTemplateID | 15 | 3 |  | PX_SM_TaskTemplateSetting, TaskTemplateSetting | members-06.md | 11556 | 25 |
| PX.SM.UPErrors | EntityType | Update Error | ErrorID, UpdateID | 7 | 0 |  | PX_SM_UPErrors, UpdateError, UPErrors | members-06.md | 11582 | 14 |
| PX.SM.UPHistory | EntityType | Update History | UpdateID | 4 | 0 |  | PX_SM_UPHistory, UpdateHistory, UPHistory | members-06.md | 11597 | 10 |
| PX.SM.UPHistoryComponents | EntityType | Update History Components | UpdateComponentID | 6 | 0 |  | PX_SM_UPHistoryComponents, UpdateHistoryComponents, UPHistoryComponents | members-06.md | 11608 | 12 |
| PX.SM.UploadAllowedFileTypes | EntityType |  | FileExt | 5 | 0 |  | PX_SM_UploadAllowedFileTypes | members-06.md | 11621 | 10 |
| PX.SM.UploadFile | EntityType |  | FileID | 36 | 4 |  | PX_SM_UploadFile | members-06.md | 11632 | 46 |
| PX.SM.UploadFileRevision | EntityType |  | FileID, FileRevisionID | 9 | 2 |  | PX_SM_UploadFileRevision | members-06.md | 11679 | 16 |
| PX.SM.UploadFileRevisionNoData | EntityType |  | FileID, FileRevisionID | 1 | 0 | PX.SM.UploadFileRevision | PX_SM_UploadFileRevisionNoData | members-06.md | 11696 | 8 |
| PX.SM.UploadFileWithData | EntityType |  | FileID, FileRevisionID | 8 | 2 |  | PX_SM_UploadFileWithData | members-06.md | 11705 | 16 |
| PX.SM.UploadFileWithIDSelector | EntityType | File | FileID | 5 | 4 | PX.SM.UploadFileWithTags | PX_SM_UploadFileWithIDSelector, File, UploadFileWithIDSelector | members-06.md | 11722 | 17 |
| PX.SM.UploadFileWithNoData | EntityType |  | FileID | 0 | 0 | PX.SM.UploadFile | PX_SM_UploadFileWithNoData | members-06.md | 11740 | 5 |
| PX.SM.UploadFileWithTags | EntityType |  | FileID | 1 | 0 | PX.SM.UploadFile | PX_SM_UploadFileWithTags | members-06.md | 11746 | 8 |
| PX.SM.UPLock | EntityType |  | DatabaseID | 4 | 0 |  | PX_SM_UPLock | members-06.md | 11755 | 9 |
| PX.SM.UPPackageTables | EntityType |  | ProjectID, TableName | 5 | 1 |  | PX_SM_UPPackageTables | members-06.md | 11765 | 11 |
| PX.SM.UPSetup | EntityType |  |  | 8 | 0 |  |  | members-06.md | 11777 | 12 |
| PX.SM.UPSnapshot | EntityType | Snapshot | SnapshotID | 25 | 3 |  | PX_SM_UPSnapshot, Snapshot, UPSnapshot | members-06.md | 11790 | 35 |
| PX.SM.UPSnapshotHistory | EntityType | Snapshot Restoration History | HistoryID | 9 | 2 |  | PX_SM_UPSnapshotHistory, SnapshotRestorationHistory, UPSnapshotHistory | members-06.md | 11826 | 18 |
| PX.SM.UPSnapshotSize | EntityType | Snapshot Size | SnapshotID | 2 | 0 | PX.SM.UPSnapshot | PX_SM_UPSnapshotSize, SnapshotSize, UPSnapshotSize | members-06.md | 11845 | 10 |
| PX.SM.UserFilter | EntityType |  | PKID, Username | 4 | 1 |  | PX_SM_UserFilter | members-06.md | 11856 | 10 |
| PX.SM.UserLocaleFormat | EntityType |  | LocaleName, UserID | 3 | 0 |  | PX_SM_UserLocaleFormat | members-06.md | 11867 | 8 |
| PX.SM.UserPreferences | EntityType | User Preferences and Email Settings | UserID | 25 | 12 |  | PX_SM_UserPreferences, UserPreferencesandEmailSettings, UserPreferences | members-06.md | 11876 | 44 |
| PX.SM.UserReportEx | EntityType |  | ReportFileName, Version | 1 | 0 | PX.Data.Reports.UserReport | PX_SM_UserReportEx | members-06.md | 11921 | 7 |
| PX.SM.Users | EntityType | User | Username | 62 | 1191 |  | PX_SM_Users, User, Users | members-06.md | 11929 | 1260 |
| PX.SM.UsersInRoles | EntityType | Users In Roles | ApplicationName, Rolename, Username | 14 | 4 |  | PX_SM_UsersInRoles, UsersInRoles | members-06.md | 13190 | 25 |
| PX.SM.Version | EntityType | Application Version |  | 6 | 0 |  |  | members-06.md | 13216 | 11 |
| PX.SM.Warden | EntityType |  | InstallationID, Key, Sub, Type | 7 | 0 |  | PX_SM_Warden | members-06.md | 13228 | 12 |
| PX.SM.WikiAccessRights | EntityType |  | ApplicationName, PageID, RoleName | 4 | 1 |  | PX_SM_WikiAccessRights | members-06.md | 13241 | 10 |
| PX.SM.WikiAccessRoles | EntityType |  | ApplicationName, PageID, RoleName | 2 | 0 | PX.SM.WikiAccessRights | PX_SM_WikiAccessRoles | members-06.md | 13252 | 9 |
| PX.SM.WikiArticle | EntityType |  | PageID | 0 | 2 | PX.SM.WikiPage | PX_SM_WikiArticle | members-06.md | 13262 | 8 |
| PX.SM.WikiArticleInProject | EntityType |  | PageID | 1 | 0 | PX.SM.WikiDescriptor | PX_SM_WikiArticleInProject | members-06.md | 13271 | 7 |
| PX.SM.WikiCss | EntityType |  | Name | 4 | 2 |  | PX_SM_WikiCss | members-06.md | 13279 | 11 |
| PX.SM.WikiDescriptor | EntityType |  | PageID | 19 | 3 | PX.SM.WikiPage | PX_SM_WikiDescriptor | members-06.md | 13291 | 29 |
| PX.SM.WikiDescriptorExt | EntityType |  | PageID | 7 | 0 | PX.SM.WikiDescriptorMaster | PX_SM_WikiDescriptorExt | members-06.md | 13321 | 14 |
| PX.SM.WikiDescriptorMaster | EntityType |  | PageID | 0 | 0 | PX.SM.WikiDescriptor | PX_SM_WikiDescriptorMaster | members-06.md | 13336 | 5 |
| PX.SM.WikiFileInPage | EntityType |  | FileID, Language, PageID, PageRevisionID | 5 | 0 |  | PX_SM_WikiFileInPage | members-06.md | 13342 | 11 |
| PX.SM.WikiNotificationTemplate | EntityType |  | PageID | 8 | 2 | PX.SM.WikiPage | PX_SM_WikiNotificationTemplate | members-06.md | 13354 | 16 |
| PX.SM.WikiPage | EntityType |  | PageID | 39 | 7 |  | PX_SM_WikiPage | members-06.md | 13371 | 52 |
| PX.SM.WikiPageCurrentLanguage | EntityType |  | Language, PageID | 0 | 0 | PX.SM.WikiPageLanguage | PX_SM_WikiPageCurrentLanguage | members-06.md | 13424 | 5 |
| PX.SM.WikiPageForReport | EntityType |  | PageID | 0 | 0 | PX.SM.WikiPage | PX_SM_WikiPageForReport | members-06.md | 13430 | 5 |
| PX.SM.WikiPageLanguage | EntityType |  | Language, PageID | 8 | 0 |  | PX_SM_WikiPageLanguage | members-06.md | 13436 | 13 |
| PX.SM.WikiPageLink | EntityType |  | Language, LinkID, PageID, PageRevisionID | 4 | 0 |  | PX_SM_WikiPageLink | members-06.md | 13450 | 9 |
| PX.SM.WikiPageMeta | EntityType |  | Name, PageID | 3 | 0 |  | PX_SM_WikiPageMeta | members-06.md | 13460 | 8 |
| PX.SM.WikiPagePath | EntityType |  | PageID | 1 | 0 | PX.SM.WikiPage | PX_SM_WikiPagePath | members-06.md | 13469 | 8 |
| PX.SM.WikiPageSimple | EntityType |  | PageID | 0 | 0 | PX.SM.WikiPage | PX_SM_WikiPageSimple | members-06.md | 13478 | 5 |
| PX.SM.WikiPageWithCurrentLanguage | EntityType |  | PageID | 11 | 6 |  | PX_SM_WikiPageWithCurrentLanguage | members-06.md | 13484 | 22 |
| PX.SM.WikiReadLanguage | EntityType |  | LocaleID, WikiID | 3 | 0 |  | PX_SM_WikiReadLanguage | members-06.md | 13507 | 9 |
| PX.SM.WikiRevision | EntityType |  | Language, PageID, PageRevisionID | 13 | 2 |  | PX_SM_WikiRevision | members-06.md | 13517 | 21 |
| PX.SM.WikiRevisionLocalized | EntityType |  | Language, PageID, PageRevisionID | 0 | 0 | PX.SM.WikiRevision | PX_SM_WikiRevisionLocalized | members-06.md | 13539 | 5 |
| PX.SM.WikiRevisionTag | EntityType |  | Language, PageID, PageRevisionID, TagID, WikiID | 5 | 1 |  | PX_SM_WikiRevisionTag | members-06.md | 13545 | 11 |
| PX.SM.WikiRevisionTagGrouped | EntityType |  | Language, PageID, PageRevisionID, TagID, WikiID | 0 | 0 | PX.SM.WikiRevisionTag | PX_SM_WikiRevisionTagGrouped | members-06.md | 13557 | 5 |
| PX.SM.WikiSitePage | EntityType |  | PageID | 7 | 1 | PX.SM.WikiPage | PX_SM_WikiSitePage | members-06.md | 13563 | 14 |
| PX.SM.WikiSitePath | EntityType |  | Number | 4 | 0 |  | PX_SM_WikiSitePath | members-06.md | 13578 | 10 |
| PX.SM.WikiTag | EntityType |  | Description, WikiID | 3 | 3 |  | PX_SM_WikiTag | members-06.md | 13589 | 11 |
| PX.SmsProvider.SM.DAC.SmsPlugin | EntityType | SMS Provider | Name | 12 | 3 |  | PX_SmsProvider_SM_DAC_SmsPlugin, SMSProvider, SmsPlugin | members-06.md | 13601 | 22 |
| PX.SmsProvider.SM.DAC.SmsPluginParameter | EntityType | Voice Plug-in Details | Name, PluginName | 13 | 2 |  | PX_SmsProvider_SM_DAC_SmsPluginParameter, VoicePluginDetails, SmsPluginParameter | members-06.md | 13624 | 21 |
| PX.SP.Alias.SPPortal | EntityType |  | PortalID | 8 | 19 |  | PX_SP_Alias_SPPortal | members-06.md | 13646 | 33 |
| PX.TM.EPCompanyTree | EntityType | Workgroup | Description | 14 | 74 |  | PX_TM_EPCompanyTree, Workgroup, EPCompanyTree | members-06.md | 13680 | 94 |
| PX.TM.EPCompanyTreeH | EntityType |  | ParentWGID, WorkGroupID | 5 | 0 |  | PX_TM_EPCompanyTreeH | members-06.md | 13775 | 10 |
| PX.TM.EPCompanyTreeMaster | EntityType | Workgroup | Description | 2 | 0 | PX.TM.EPCompanyTree | PX_TM_EPCompanyTreeMaster | members-06.md | 13786 | 10 |
| PX.TM.EPCompanyTreeMember | EntityType |  | ContactID, WorkGroupID | 12 | 4 |  | PX_TM_EPCompanyTreeMember | members-06.md | 13797 | 21 |
| PX.TokenLogin.SAGrantHistory | EntityType | Access Grant History | LogID | 4 | 0 |  | PX_TokenLogin_SAGrantHistory, AccessGrantHistory, SAGrantHistory | members-06.md | 13819 | 10 |
| PX.Web.UI.Frameset.Model.DAC.MUIArea | EntityType | Area | AreaID, IsPortal | 13 | 3 |  | PX_Web_UI_Frameset_Model_DAC_MUIArea, Area, MUIArea | members-06.md | 13830 | 22 |
| PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen | EntityType | Favorite Screen | IsPortal, NodeID, Username | 9 | 4 |  | PX_Web_UI_Frameset_Model_DAC_MUIFavoriteScreen, FavoriteScreen, MUIFavoriteScreen | members-06.md | 13853 | 19 |
| PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile | EntityType | Favorite Tile | IsPortal, TileID, Username | 9 | 4 |  | PX_Web_UI_Frameset_Model_DAC_MUIFavoriteTile, FavoriteTile, MUIFavoriteTile | members-06.md | 13873 | 19 |
| PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace | EntityType | Favorite Workspace | IsPortal, Username, WorkspaceID | 10 | 4 |  | PX_Web_UI_Frameset_Model_DAC_MUIFavoriteWorkspace, FavoriteWorkspace, MUIFavoriteWorkspace | members-06.md | 13893 | 20 |
| PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen | EntityType | Pinned Screen | IsPortal, NodeID, Username, WorkspaceID | 11 | 5 |  | PX_Web_UI_Frameset_Model_DAC_MUIPinnedScreen, PinnedScreen, MUIPinnedScreen | members-06.md | 13914 | 22 |
| PX.Web.UI.Frameset.Model.DAC.MUIScreen | EntityType | Screen | IsPortal, NodeID, WorkspaceID | 14 | 6 |  | PX_Web_UI_Frameset_Model_DAC_MUIScreen, Screen, MUIScreen | members-06.md | 13937 | 27 |
| PX.Web.UI.Frameset.Model.DAC.MUIScreenOrderHeader | EntityType |  | SubcategoryID, WorkspaceID | 3 | 0 |  | PX_Web_UI_Frameset_Model_DAC_MUIScreenOrderHeader | members-06.md | 13965 | 8 |
| PX.Web.UI.Frameset.Model.DAC.MUISubcategory | EntityType | Subcategory | IsPortal, SubcategoryID | 14 | 3 |  | PX_Web_UI_Frameset_Model_DAC_MUISubcategory, Subcategory, MUISubcategory | members-06.md | 13974 | 23 |
| PX.Web.UI.Frameset.Model.DAC.MUITile | EntityType | Tile | IsPortal, TileID | 14 | 5 |  | PX_Web_UI_Frameset_Model_DAC_MUITile, Tile, MUITile | members-06.md | 13998 | 25 |
| PX.Web.UI.Frameset.Model.DAC.MUITileOrderHeader | EntityType |  | WorkspaceID | 2 | 1 |  | PX_Web_UI_Frameset_Model_DAC_MUITileOrderHeader | members-06.md | 14024 | 8 |
| PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences | EntityType | User Preferences | Username | 8 | 3 |  | PX_Web_UI_Frameset_Model_DAC_MUIUserPreferences, UserPreferences1, MUIUserPreferences | members-06.md | 14033 | 17 |
| PX.Web.UI.Frameset.Model.DAC.MUIWorkspace | EntityType | Workspace | IsPortal, WorkspaceID | 16 | 6 |  | PX_Web_UI_Frameset_Model_DAC_MUIWorkspace, Workspace, MUIWorkspace | members-06.md | 14051 | 28 |
| PX.Web.UI.SMPageCache | EntityType |  |  | 0 | 0 |  |  | members-06.md | 14080 | 3 |
| ReconciliationTools.APGLDiscrepancyByDocumentEnqResult | EntityType | Vendor Details | DocType, RefNbr | 50 | 0 |  | ReconciliationTools_APGLDiscrepancyByDocumentEnqResult | members-06.md | 14084 | 57 |
| ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult | EntityType | Customer Details | DocType, RefNbr | 50 | 0 |  | ReconciliationTools_ARGLDiscrepancyByDocumentEnqResult | members-06.md | 14142 | 57 |
| ReconciliationTools.DiscrepancyByAccountEnqResult | EntityType | GL Transaction | BatchNbr, LineNbr, Module | 4 | 0 | PX.Objects.GL.GLTranR | ReconciliationTools_DiscrepancyByAccountEnqResult | members-06.md | 14200 | 12 |
