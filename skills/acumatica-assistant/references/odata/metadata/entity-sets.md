<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# DAC-based OData entity sets

One row per DAC that the container exposes. **Entity sets** are the names accepted after `/api/odata/dac/` (the generated `PX_Namespace_Class` name, the display-name alias and the class-name alias; a digit suffix means the alias collided with another DAC). **Non-filterable** fields are the `Cap.FilterRestrictions` `NonFilterableProperties` of the entity set, which the DAC-based OData interface refuses in both `$filter` and `$select`; **Filterable=false** means no field declared in the DAC itself may be used in `$filter` or `$select`.

| DAC | Label | Entity sets | Key | Non-filterable fields | Filterable=false |
|---|---|---|---|---|---|
| PX.AI.Tools.DAC.AIToolDefinition | AI Tool | PX_AI_Tools_DAC_AIToolDefinition, AITool, AIToolDefinition | ToolID |  |  |
| PX.AI.Tools.GI.DAC.AIGIToolDefinition |  | PX_AI_Tools_GI_DAC_AIGIToolDefinition | ToolID |  |  |
| PX.AIStudio.DAC.LLMConnection | Agent LLM Connection | PX_AIStudio_DAC_LLMConnection, AgentLLMConnection, LLMConnection | ConnectionID | DeletedDatabaseRecord |  |
| PX.AIStudio.DAC.LLMConnectionParameter | Agent LLM Connection Parameter | PX_AIStudio_DAC_LLMConnectionParameter, AgentLLMConnectionParameter, LLMConnectionParameter | ConnectionID, ParameterID | HasError, IsEditable |  |
| PX.AIStudio.DAC.LLMPrompt | Agent | PX_AIStudio_DAC_LLMPrompt, Agent, LLMPrompt | PromptID | State, NoteText |  |
| PX.AIStudio.DAC.LLMPromptSystemInstruction | Agent System Instruction Assignment | PX_AIStudio_DAC_LLMPromptSystemInstruction, AgentSystemInstructionAssignment, LLMPromptSystemInstruction | PromptID, PromptInstructionID |  |  |
| PX.AIStudio.DAC.LLMPromptTesting | Agent Testing | PX_AIStudio_DAC_LLMPromptTesting, AgentTesting, LLMPromptTesting | PromptID | ShowGIMaskingWarning, CacheType, GDPRProtectedFieldsWarning |  |
| PX.AIStudio.DAC.LLMPromptTestingLog | Agent Testing Log | PX_AIStudio_DAC_LLMPromptTestingLog, AgentTestingLog, LLMPromptTestingLog | EventID, PromptID |  |  |
| PX.AIStudio.DAC.LLMPromptTool | Agent Tool | PX_AIStudio_DAC_LLMPromptTool, AgentTool, LLMPromptTool | AIToolDefinitionToolID, PromptID, ToolID | NoteText |  |
| PX.AIStudio.DAC.LLMPromptToolCBApiCurrent | Agent Tool CB API Current | PX_AIStudio_DAC_LLMPromptToolCBApiCurrent, AgentToolCBAPICurrent, LLMPromptToolCBApiCurrent | PromptID, ToolID |  |  |
| PX.AIStudio.DAC.LLMProvider | LLM Provider | PX_AIStudio_DAC_LLMProvider, LLMProvider | ProviderID | DeletedDatabaseRecord |  |
| PX.AIStudio.DAC.LLMProviderParameter | LLM Provider Parameter | PX_AIStudio_DAC_LLMProviderParameter, LLMProviderParameter | ParameterID, ProviderID |  |  |
| PX.AIStudio.DAC.LLMRequestHistory | AI Automation History Record | PX_AIStudio_DAC_LLMRequestHistory, AIAutomationHistoryRecord, LLMRequestHistory | RequestID | Duration |  |
| PX.AIStudio.DAC.LLMSystemInstruction | Agent System Instruction | PX_AIStudio_DAC_LLMSystemInstruction, AgentSystemInstruction, LLMSystemInstruction | InstructionID |  |  |
| PX.Api.ContractBased.UI.DAC.EntityEndpoint |  | PX_Api_ContractBased_UI_DAC_EntityEndpoint | GateVersion, InterfaceName |  |  |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModel |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModel | ModelID |  |  |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelField |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelField | FieldName, ModelID |  |  |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelFieldMapping | MappedFieldName, MappingID |  |  |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelMapping | MappingID |  |  |
| PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping |  | PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelScreenMapping | MappingID, ScreenID, ViewName |  |  |
| PX.Api.Mobile.MultiFactorAuth.DAC.MobileOtpSecret |  | PX_Api_Mobile_MultiFactorAuth_DAC_MobileOtpSecret | AccountID, ApplicationInstanceID |  |  |
| PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode |  | PX_Api_Mobile_MultiFactorAuth_DAC_MultiFactorPersistentCode | Code, UserId |  |  |
| PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCodeWithCompany |  | PX_Api_Mobile_MultiFactorAuth_DAC_MultiFactorPersistentCodeWithCompany | Code, UserId |  |  |
| PX.Api.Mobile.PushNotifications.DAC.MobileDevice |  | PX_Api_Mobile_PushNotifications_DAC_MobileDevice | AccountID, ApplicationInstanceID |  |  |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceItems | NoteID, Owner | DisplayName, NoteText |  |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceItemsOrder | ItemID, ItemOwner, ItemType, Owner | NoteText |  |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsOrder | DashboardID, Owner, WidgetID, WidgetOwner | NoteText |  |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2 |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsV2 | NoteID, Owner | NoteText |  |
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsV2Order | DashboardID, Owner, WidgetID, WidgetOwner | NoteText |  |
| PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces |  | PX_Api_Mobile_Workspaces_MobileSiteMapWorkspaces | Name | NoteText |  |
| PX.Api.ModelContextProtocol.UI.DAC.McpServer | MCP Server | PX_Api_ModelContextProtocol_UI_DAC_McpServer, MCPServer | Name | Url |  |
| PX.Api.ModelContextProtocol.UI.DAC.McpServerTool | MCP Tool | PX_Api_ModelContextProtocol_UI_DAC_McpServerTool, MCPTool, McpServerTool | McpServerID, ToolID |  |  |
| PX.Api.ModelContextProtocol.UI.DAC.McpServerToolProjection | MCP Tool | PX_Api_ModelContextProtocol_UI_DAC_McpServerToolProjection | McpServerID, ToolID |  |  |
| PX.Api.SYData |  | PX_Api_SYData | LineNbr, MappingID | ExtRefNbr, CanAddSubstitutions, NoteText |  |
| PX.Api.SYHistory |  | PX_Api_SYHistory | MappingID, StatusDate | StatusDateToDisplay |  |
| PX.Api.SYImportCondition |  | PX_Api_SYImportCondition | LineNbr, MappingID | NoteText |  |
| PX.Api.SYMapping | Mapping | PX_Api_SYMapping, Mapping, SYMapping | Name | SitemapTitle, SitemapScreenId, NoteText, ShowCreatedByEventsTabExpr, WorkspaceID, SubcategoryID |  |
| PX.Api.SYMappingActive | Mapping | PX_Api_SYMappingActive | Name |  | yes |
| PX.Api.SYMappingActiveFilter | Mapping | PX_Api_SYMappingActiveFilter | Name |  |  |
| PX.Api.SYMappingCondition |  | PX_Api_SYMappingCondition | LineNbr, MappingID | ObjectNameHidden, FieldNameHidden, NoteText |  |
| PX.Api.SYMappingField |  | PX_Api_SYMappingField | LineNbr, MappingID | ObjectNameHidden, FieldNameHidden, FullFieldNameHidden, NoteText |  |
| PX.Api.SYMappingFieldSimple |  | PX_Api_SYMappingFieldSimple | LineNbr, MappingID |  | yes |
| PX.Api.SYProvider | Provider | PX_Api_SYProvider, Provider, SYProvider | Name | NoteText |  |
| PX.Api.SYProviderField |  | PX_Api_SYProviderField | Name, ObjectName, ProviderID | NoteText |  |
| PX.Api.SYProviderObject | Provider Object | PX_Api_SYProviderObject, ProviderObject, SYProviderObject | LineNbr, ProviderID | NoteText |  |
| PX.Api.SYServiceSchema |  | PX_Api_SYServiceSchema | ScreenID, ServiceID | Title, NoteText |  |
| PX.Api.SYSubstitution |  | PX_Api_SYSubstitution | SubstitutionID |  |  |
| PX.Api.SYSubstitutionValues |  | PX_Api_SYSubstitutionValues | SubstitutionID, ValueID |  |  |
| PX.Api.SYWebService |  | PX_Api_SYWebService | ServiceID | NoteText, CurSysVer |  |
| PX.Api.Webhooks.DAC.WebHook |  | PX_Api_Webhooks_DAC_WebHook | Name | NoteText, Url |  |
| PX.Api.Webhooks.WebHookRequest |  | PX_Api_Webhooks_WebHookRequest | RequestID, WebHookID |  |  |
| PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun | GeneratorRun | PX_AutocompleteGenerator_UI_DAC_AutocompleteGeneratorRun, GeneratorRun, AutocompleteGeneratorRun | RunId, UserId | SuccessString, NoteText |  |
| PX.AutocompleteGenerator.UI.DAC.LastRunOfUser | GeneratorRun | PX_AutocompleteGenerator_UI_DAC_LastRunOfUser | RunId, UserId |  |  |
| PX.BusinessProcess.DAC.ActionExecution | Action Execution | PX_BusinessProcess_DAC_ActionExecution, ActionExecution | ExecutionID | NoteText, ActionNameMethod, ShowCreatedByEventsTabExpr |  |
| PX.BusinessProcess.DAC.ActionExecutionMapping | Action Execution Mapping | PX_BusinessProcess_DAC_ActionExecutionMapping, ActionExecutionMapping | ExecutionID, LineNbr | DisplayFieldName |  |
| PX.BusinessProcess.DAC.ActionExecutionParameter | Action Execution Parameter | PX_BusinessProcess_DAC_ActionExecutionParameter, ActionExecutionParameter | ExecutionID, LineNbr |  |  |
| PX.BusinessProcess.DAC.BPEvent | Business Process Event | PX_BusinessProcess_DAC_BPEvent, BusinessProcessEvent, BPEvent | Name | ScreenIdValue, NoteText, ActionName2, GroupBy, IsGroupByOldValue, IsTriggerConditionsVisible |  |
| PX.BusinessProcess.DAC.BPEventHistory | Business Process Event History | PX_BusinessProcess_DAC_BPEventHistory, BusinessProcessEventHistory, BPEventHistory | EventDefinitionID, EventID | Source, CanBeResumed, LastRunStatus |  |
| PX.BusinessProcess.DAC.BPEventSchedule | Business Process Event Schedule | PX_BusinessProcess_DAC_BPEventSchedule, BusinessProcessEventSchedule, BPEventSchedule | EventID, ScheduleID | ScreenID |  |
| PX.BusinessProcess.DAC.BPEventSubscriber | Business Process Event Subscriber | PX_BusinessProcess_DAC_BPEventSubscriber, BusinessProcessEventSubscriber, BPEventSubscriber | EventID, HandlerID, Type | ScreenId, LastRunStatus, Status, ErrorText |  |
| PX.BusinessProcess.DAC.BPEventTrackingField | Business Process Tracked Field | PX_BusinessProcess_DAC_BPEventTrackingField, BusinessProcessTrackedField, BPEventTrackingField | EventID, FieldID | IsFromTriggerCondition, IsFromInsertOrDeleteTriggerCondition |  |
| PX.BusinessProcess.DAC.BPEventTriggerCondition | Business Process Event Trigger Condition | PX_BusinessProcess_DAC_BPEventTriggerCondition, BusinessProcessEventTriggerCondition, BPEventTriggerCondition | EventID, OrderNbr |  |  |
| PX.BusinessProcess.DAC.BPInquiryParameter | Business Process Inquiry Parameter | PX_BusinessProcess_DAC_BPInquiryParameter, BusinessProcessInquiryParameter, BPInquiryParameter | EventID, Name | DisplayName, DefaultValue, UseDefault |  |
| PX.BusinessProcess.DAC.BPProcessedEventSubscribers |  | PX_BusinessProcess_DAC_BPProcessedEventSubscribers | Id |  |  |
| PX.BusinessProcess.DAC.DispatcherStatisticEventDetail | DispatcherStatisticEventDetail | PX_BusinessProcess_DAC_DispatcherStatisticEventDetail, DispatcherStatisticEventDetail | BusinessEventName, Id |  |  |
| PX.BusinessProcess.DAC.DispatcherStatus |  | PX_BusinessProcess_DAC_DispatcherStatus | QueueType, WebsiteID | Order, PerformanceStatus, QueueSize, LastError, LastMessageProcessTime, LastFailedToCommitMessage, IsCurrentNode |  |
| PX.BusinessProcess.DAC.MobileNotification | Mobile Notification | PX_BusinessProcess_DAC_MobileNotification, MobileNotification | NotificationID | ScreenIdValue, NoteText, ShowSendByEventsTabExpr |  |
| PX.BusinessProcess.DAC.QueueNotificationSettings | Notification Settings | PX_BusinessProcess_DAC_QueueNotificationSettings, NotificationSettings, QueueNotificationSettings | SettingID | QueueMonitorScreenId, DeliveryTypeSms, DeliveryTypePush, NoteText |  |
| PX.CloudServices.DAC.RecognizedRecord | Recognized Record | PX_CloudServices_DAC_RecognizedRecord, RecognizedRecord1 | EntityType, RefNbr | NoteText, DeletedDatabaseRecord |  |
| PX.CloudServices.DAC.RecognizedRecordProjection | Recognized Record | PX_CloudServices_DAC_RecognizedRecordProjection, RecognizedRecord, RecognizedRecordProjection | EntityType, RefNbr |  |  |
| PX.Commerce.Amazon.BCAmazonTaxMapping | BCAmazonTaxMapping | PX_Commerce_Amazon_BCAmazonTaxMapping, BCAmazonTaxMapping | BindingID, TaxMappingID |  |  |
| PX.Commerce.Amazon.BCBindingAmazon | Amazon Settings | PX_Commerce_Amazon_BCBindingAmazon, AmazonSettings, BCBindingAmazon | BindingID |  |  |
| PX.Commerce.BigCommerce.BCBindingBigCommerce | BigCommerce Settings | PX_Commerce_BigCommerce_BCBindingBigCommerce, BigCommerceSettings, BCBindingBigCommerce | BindingID |  |  |
| PX.Commerce.Core.BCBinding | Connection Settings | PX_Commerce_Core_BCBinding, ConnectionSettings, BCBinding | BindingName, ConnectorType | AllowedStores, HasSyncStatuses |  |
| PX.Commerce.Core.BCEntitiesSyncStatistics | Sync Entities Counts | PX_Commerce_Core_BCEntitiesSyncStatistics, SyncEntitiesCounts, BCEntitiesSyncStatistics | BindingId, ConnectorType, EntityType |  |  |
| PX.Commerce.Core.BCEntity | Sync Entity | PX_Commerce_Core_BCEntity, SyncEntity, BCEntity | BindingID, ConnectorType, EntityType | IsFeatureEnabled, NoteText |  |
| PX.Commerce.Core.BCEntity2 | Sync Entity With Counts | PX_Commerce_Core_BCEntity2, SyncEntityWithCounts, BCEntity2 | BindingID, ConnectorType, EntityType |  | yes |
| PX.Commerce.Core.BCEntityExportFilter | Entity Export Filter | PX_Commerce_Core_BCEntityExportFilter, EntityExportFilter, BCEntityExportFilter | BindingID, ConnectorType, EntityType, ExportFilterID | NoteText |  |
| PX.Commerce.Core.BCEntityExportMapping | Entity Export Mapping | PX_Commerce_Core_BCEntityExportMapping, EntityExportMapping, BCEntityExportMapping | BindingID, ConnectorType, EntityType, ExportMappingID | NoteText |  |
| PX.Commerce.Core.BCEntityImportFilter | Entity Import Filter | PX_Commerce_Core_BCEntityImportFilter, EntityImportFilter, BCEntityImportFilter | BindingID, ConnectorType, EntityType, ImportFilterID | NoteText |  |
| PX.Commerce.Core.BCEntityImportMapping | Entity Import Mapping | PX_Commerce_Core_BCEntityImportMapping, EntityImportMapping, BCEntityImportMapping | BindingID, ConnectorType, EntityType, ImportMappingID | NoteText |  |
| PX.Commerce.Core.BCEntityStats | Sync Entity Stats | PX_Commerce_Core_BCEntityStats, SyncEntityStats, BCEntityStats | BindingID, ConnectorType, EntityType |  |  |
| PX.Commerce.Core.BCSyncDetail | Sync Status Details | PX_Commerce_Core_BCSyncDetail, SyncStatusDetails, BCSyncDetail | DetailID | Source |  |
| PX.Commerce.Core.BCSyncStatus | Sync History | PX_Commerce_Core_BCSyncStatus, SyncHistory, BCSyncStatus | SyncID | Selectable, Source, NoteText |  |
| PX.Commerce.Core.BCWebHook | Web Hooks | PX_Commerce_Core_BCWebHook, WebHooks, BCWebHook | BindingID, ConnectorType, Scope |  |  |
| PX.Commerce.Core.DispatcherStatisticCommerceDetail | DispatcherStatisticCommerceDetail | PX_Commerce_Core_DispatcherStatisticCommerceDetail, DispatcherStatisticCommerceDetail | Connector, Direction, Id |  |  |
| PX.Commerce.Objects.BCBindingExt | Store Settings | PX_Commerce_Objects_BCBindingExt, StoreSettings, BCBindingExt | BindingID |  |  |
| PX.Commerce.Objects.BCFeeMapping | BCFeeMapping | PX_Commerce_Objects_BCFeeMapping, BCFeeMapping | BindingID, FeeMappingID | EntryDescription, TransactionType, DefaultOffsetAccount |  |
| PX.Commerce.Objects.BCInventoryFileUrls | BC Inventory File Urls | PX_Commerce_Objects_BCInventoryFileUrls, BCInventoryFileUrls | FileID | NoteText |  |
| PX.Commerce.Objects.BCLocations | Locations | PX_Commerce_Objects_BCLocations, Locations, BCLocations | BCLocationsID |  |  |
| PX.Commerce.Objects.BCMatrixOptionsMapping | Matrix Options Mapping | PX_Commerce_Objects_BCMatrixOptionsMapping, MatrixOptionsMapping, BCMatrixOptionsMapping | OptionMappingID |  |  |
| PX.Commerce.Objects.BCPaymentMethods | BCPaymentMethods | PX_Commerce_Objects_BCPaymentMethods, BCPaymentMethods | PaymentMappingID |  |  |
| PX.Commerce.Objects.BCPaymentTermsMapping | BCPaymentTermsMapping | PX_Commerce_Objects_BCPaymentTermsMapping, BCPaymentTermsMapping | BindingID, PaymentTermsMappingID |  |  |
| PX.Commerce.Objects.BCShippingMappings | BCShippingMappings | PX_Commerce_Objects_BCShippingMappings, BCShippingMappings | ShippingMappingID |  |  |
| PX.Commerce.Objects.ExportBCLocations | ExportLocations | PX_Commerce_Objects_ExportBCLocations, ExportLocations, ExportBCLocations | BCLocationsID |  |  |
| PX.Commerce.Objects.ImportBCLocations | ImportLocations | PX_Commerce_Objects_ImportBCLocations, ImportLocations, ImportBCLocations | BCLocationsID |  |  |
| PX.Commerce.Objects.SOOrderRisks | SO Order Risks | PX_Commerce_Objects_SOOrderRisks, SOOrderRisks | LineNbr, OrderNbr, OrderType | NoteText |  |
| PX.Commerce.Shopify.BCBindingShopify | Shopify Settings | PX_Commerce_Shopify_BCBindingShopify, ShopifySettings, BCBindingShopify | BindingID | ApiCallLimit, ShopifyApiVersion |  |
| PX.Commerce.Shopify.BCRoleAssignment | Customer Contact Role Assignment | PX_Commerce_Shopify_BCRoleAssignment, CustomerContactRoleAssignment, BCRoleAssignment | RoleAssignmentID | NoteText |  |
| PX.CS.RMColumn | Column | PX_CS_RMColumn, Column, RMColumn | ColumnCode, ColumnSetCode | Preview, NoteText, StyleIDText |  |
| PX.CS.RMColumnHeader |  | PX_CS_RMColumnHeader | ColumnCode, ColumnSetCode, HeaderNbr | IsRowSet, SectionType, NoteText |  |
| PX.CS.RMColumnSet | Column Set | PX_CS_RMColumnSet, ColumnSet, RMColumnSet | ColumnSetCode | LastColumn, NoteText |  |
| PX.CS.RMDataSource | Data Source | PX_CS_RMDataSource, DataSource, RMDataSource | DataSourceID |  |  |
| PX.CS.RMReport | Report | PX_CS_RMReport, Report, RMReport | ReportCode | SitemapTitle, NoteText, SubCD, WorkspaceID, SubcategoryID |  |
| PX.CS.RMRow | Row | PX_CS_RMRow, Row, RMRow | RowNbr, RowSetCode | RowCodeRO, RMType, Preview, LineNbr, InCycle, DataVisible, DataSourceVisible, NoteText, StyleIDText |  |
| PX.CS.RMRowSet | Row Set | PX_CS_RMRowSet, RowSet, RMRowSet | RowSetCode | NoteText |  |
| PX.CS.RMStyle | Style | PX_CS_RMStyle, Style, RMStyle | StyleID | ColorRGBA, ColorRGB, BackColorRGBA, BackColorRGB, Bold, Italic, Underline, Strikeout, StyleIDText |  |
| PX.CS.RMUnit | Unit | PX_CS_RMUnit, Unit, RMUnit | UnitCode, UnitSetCode | TreeNodeID, CodeAndDescription, NoteText |  |
| PX.CS.RMUnitSet | Unit Set | PX_CS_RMUnitSet, UnitSet, RMUnitSet | UnitSetCode | NoteText |  |
| PX.Dashboards.DAC.Dashboard | Dashboard | PX_Dashboards_DAC_Dashboard, Dashboard | Name | SitemapTitle, NoteText, WorkspaceID, SubcategoryID |  |
| PX.Dashboards.DAC.DashboardParameter | Dashboard Parameter | PX_Dashboards_DAC_DashboardParameter, DashboardParameter | DashboardID, LineNbr | NoteText |  |
| PX.Dashboards.DAC.DashboardParameterV2 | Dashboard Parameter | PX_Dashboards_DAC_DashboardParameterV2, DashboardParameter1, DashboardParameterV2 | DashboardID, LineNbr | NoteText |  |
| PX.Dashboards.DAC.DashboardV2 | Dashboard | PX_Dashboards_DAC_DashboardV2, Dashboard1, DashboardV2 | Name | SitemapTitle, ScreenID, NoteText, WorkspaceID, SubcategoryID |  |
| PX.Dashboards.DAC.Widget | Widget | PX_Dashboards_DAC_Widget, Widget | DashboardID, WidgetID | IsMasterCopy, NoteText, WidgetName, SourceSetting |  |
| PX.Dashboards.DAC.WidgetParameterV2 |  | PX_Dashboards_DAC_WidgetParameterV2 | DashboardID, DashboardParameterName, WidgetID | NoteText |  |
| PX.Dashboards.DAC.WidgetV2 | Widget | PX_Dashboards_DAC_WidgetV2, Widget1, WidgetV2 | DashboardID, WidgetID | IsMasterCopy, NoteText, WidgetType, Source |  |
| PX.Dashboards.Widgets.WidgetPivotTable |  | PX_Dashboards_Widgets_WidgetPivotTable | PivotTableID, ScreenID |  |  |
| PX.Data.Archiving.DAC.ArchivalPolicy | Archival Policy | PX_Data_Archiving_DAC_ArchivalPolicy, ArchivalPolicy | TableName |  |  |
| PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate | Document Archival History | PX_Data_Archiving_DAC_ArchivedDocumentBatchByDate, DocumentArchivalHistory, ArchivedDocumentBatchByDate | DateToArchive, ExecutionDate, TableName |  |  |
| PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables | Tables to Track Deleted Records | PX_Data_DeletedRecordsTracking_DAC_SMDeletedRecordsTrackingTables, TablestoTrackDeletedRecords, SMDeletedRecordsTrackingTables | TableID | Description |  |
| PX.Data.FilterHeader | Filter Header | PX_Data_FilterHeader, FilterHeader | FilterID, ScreenID, ViewName | IsOwned, NoteText |  |
| PX.Data.FilterRow | Filter Row | PX_Data_FilterRow, FilterRow | FilterID, FilterRowNbr |  |  |
| PX.Data.GenericInquiry.DAC.GIDataWarehouse | Generic Inquiry Data Warehouse | PX_Data_GenericInquiry_DAC_GIDataWarehouse, GenericInquiryDataWarehouse, GIDataWarehouse | DesignID | UpdateScheduleExtended, WarningMessage, GIName, NoteText |  |
| PX.Data.Licensing.SM.SMLicenseCommerceTran |  | PX_Data_Licensing_SM_SMLicenseCommerceTran | Date, ScreenID |  |  |
| PX.Data.Licensing.SM.SMLicenseConstraints |  | PX_Data_Licensing_SM_SMLicenseConstraints | CompanyIdentifier, Date |  |  |
| PX.Data.Licensing.SM.SMLicenseERPTran |  | PX_Data_Licensing_SM_SMLicenseERPTran | Date, PrimaryItemType, ScreenID, TransactionType |  |  |
| PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction | SMLicenseERPTranDetailsAction | PX_Data_Licensing_SM_SMLicenseERPTranDetailsAction, SMLicenseERPTranDetailsAction | ActionId |  |  |
| PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc | SMLicenseERPTranDetailsDoc | PX_Data_Licensing_SM_SMLicenseERPTranDetailsDoc, SMLicenseERPTranDetailsDoc | Id |  |  |
| PX.Data.Licensing.SM.SMLicenseViolations |  | PX_Data_Licensing_SM_SMLicenseViolations | Date, LimitType, TranType | StatusUserFriendly, LimitTypeUserFriendly, TranTypeUserFriendly, OverchargeRate |  |
| PX.Data.ListEntryPoint | List as Entry Point | PX_Data_ListEntryPoint, ListasEntryPoint, ListEntryPoint | EntryScreenID |  |  |
| PX.Data.Localization.SystemCollation |  | PX_Data_Localization_SystemCollation | CollationName, CollationNameCS, CollationNameCSLatin, CollationNameLatin, SqlDialect |  |  |
| PX.Data.Maintenance.GI.GIDesign | Generic Inquiry | PX_Data_Maintenance_GI_GIDesign, GenericInquiry, GIDesign | Name | ReplacePrimaryScreen, NoteText, SitemapTitle, SitemapSelectorTitle, SitemapScreenID, DefaultSortOrder, DesignerMode, Query, IsDraft, AiAssistantGISyncStatus, WorkspaceID, SubcategoryID |  |
| PX.Data.Maintenance.GI.GIFilter | Generic Inquiry Filter | PX_Data_Maintenance_GI_GIFilter, GenericInquiryFilter, GIFilter | DesignID, LineNbr | NoteText |  |
| PX.Data.Maintenance.GI.GIGroupBy | Generic Inquiry Grouping | PX_Data_Maintenance_GI_GIGroupBy, GenericInquiryGrouping, GIGroupBy | DesignID, LineNbr | NoteText |  |
| PX.Data.Maintenance.GI.GIMassAction | Generic Inquiry Mass Action | PX_Data_Maintenance_GI_GIMassAction, GenericInquiryMassAction, GIMassAction | ActionName, DesignID, MassActionID |  |  |
| PX.Data.Maintenance.GI.GIMassUpdateField | Generic Inquiry Mass Update Field | PX_Data_Maintenance_GI_GIMassUpdateField, GenericInquiryMassUpdateField, GIMassUpdateField | DesignID, FieldID, FieldName |  |  |
| PX.Data.Maintenance.GI.GINavigationCondition | Generic Inquiry Navigation Condition | PX_Data_Maintenance_GI_GINavigationCondition, GenericInquiryNavigationCondition, GINavigationCondition | DesignID, LineNbr, NavigationScreenLineNbr |  |  |
| PX.Data.Maintenance.GI.GINavigationParameter | Generic Inquiry Navigation Parameter | PX_Data_Maintenance_GI_GINavigationParameter, GenericInquiryNavigationParameter, GINavigationParameter | DesignID, LineNbr, NavigationScreenLineNbr |  |  |
| PX.Data.Maintenance.GI.GINavigationScreen | Generic Inquiry Navigation Screen | PX_Data_Maintenance_GI_GINavigationScreen, GenericInquiryNavigationScreen, GINavigationScreen | DesignID, LineNbr | Title, NoteText |  |
| PX.Data.Maintenance.GI.GIOn | Generic Inquiry Relation Dependencies | PX_Data_Maintenance_GI_GIOn, GenericInquiryRelationDependencies, GIOn | DesignID, LineNbr, RelationNbr | NoteText |  |
| PX.Data.Maintenance.GI.GIRecordDefault | Generic Inquiry Default Record | PX_Data_Maintenance_GI_GIRecordDefault, GenericInquiryDefaultRecord, GIRecordDefault | DesignID, FieldName, RecDefID |  |  |
| PX.Data.Maintenance.GI.GIRelation | Generic Inquiry Relation | PX_Data_Maintenance_GI_GIRelation, GenericInquiryRelation, GIRelation | DesignID, LineNbr | IsAddRelatedTableAllowed, NoteText |  |
| PX.Data.Maintenance.GI.GIResult | Generic Inquiry Result | PX_Data_Maintenance_GI_GIResult, GenericInquiryResult, GIResult | DesignID, LineNbr | FieldName, NoteText |  |
| PX.Data.Maintenance.GI.GISort | Generic Inquiry Sorting | PX_Data_Maintenance_GI_GISort, GenericInquirySorting, GISort | DesignID, LineNbr | NoteText |  |
| PX.Data.Maintenance.GI.GITable | Generic Inquiry Table | PX_Data_Maintenance_GI_GITable, GenericInquiryTable, GITable | Alias, DesignID | Description, IsAddRelatedTableAllowed, NoteText |  |
| PX.Data.Maintenance.GI.GIWhere | Generic Inquiry Where Statement | PX_Data_Maintenance_GI_GIWhere, GenericInquiryWhereStatement, GIWhere | DesignID, LineNbr | NoteText |  |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceDailyUsageSummary | Date, InstallationID |  |  |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceDayUsageAggregated | ChartId, InstallationID, IntervalDateTime, Legend, SplitId |  |  |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceInstallation |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceInstallation | Id |  |  |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceParamLimits | Date, InstallationID | APISessions |  |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetails |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetails | DayIndex, EncodedIDs, Legend |  |  |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsPacked |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetailsPacked | ChartId, DayIndex, InstallationId, Legend, SplitId |  |  |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetailsTmp | ChartId, InstallationID, IntervalDateTime, Legend, SplitId |  |  |
| PX.Data.Maintenance.SM.DAC.SMLicenseStatistic |  | PX_Data_Maintenance_SM_DAC_SMLicenseStatistic | Date |  |  |
| PX.Data.Maintenance.SM.DAC.ThemeVariables |  | PX_Data_Maintenance_SM_DAC_ThemeVariables | EntityNoteID, Theme, VariableName |  |  |
| PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule | Notification Schedule | PX_Data_Maintenance_SM_SendRecurringNotifications_NotificationSchedule, NotificationSchedule | NotificationID, ScheduleID | ScheduleNoteID |  |
| PX.Data.Maintenance.TenantOperations.TenantOperationHistory | Tenant Operation History | PX_Data_Maintenance_TenantOperations_TenantOperationHistory, TenantOperationHistory | Id | SourceCompanyName, TargetCompanyName |  |
| PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion | Tenant or Snapshot Deletion | PX_Data_Maintenance_TenantShapshotDeletion_DAC_TenantSnapshotDeletion, TenantorSnapshotDeletion, TenantSnapshotDeletion | SnapshotId, TenantId | NoteText, Type, SizeMB, SnapshotName, Description, Visibility, CreatedOn, Version, ExportMode, SourceCompany, TenantName, Status |  |
| PX.Data.Note | Note | PX_Data_Note, Note | NoteID | EntityName |  |
| PX.Data.NoteDoc |  | PX_Data_NoteDoc | FileID, NoteID | EntityType, EntityName, EntityRowValues |  |
| PX.Data.NoteDoc2 |  | PX_Data_NoteDoc2 | FileID, NoteID |  |  |
| PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory | Workflow Category | PX_Data_ProjectDefinition_Workflow_AUWorkflowCategory, WorkflowCategory, AUWorkflowCategory | CategoryName, ScreenID |  |  |
| PX.Data.Reports.UserReport |  | PX_Data_Reports_UserReport | ReportFileName, Version |  |  |
| PX.Data.Reports.UserReportHeader |  | PX_Data_Reports_UserReportHeader | ReportFileName, Version |  |  |
| PX.Data.RichTextEdit.RichFileRevision |  | PX_Data_RichTextEdit_RichFileRevision | FileID, FileRevisionID |  |  |
| PX.Data.RichTextEdit.WikiPage2 |  | PX_Data_RichTextEdit_WikiPage2 | PageID |  |  |
| PX.Data.RichTextEdit.WikiPageParent |  | PX_Data_RichTextEdit_WikiPageParent | PageID |  |  |
| PX.Data.Search.SPWikiCategory |  | PX_Data_Search_SPWikiCategory | CategoryID |  |  |
| PX.Data.Search.SPWikiCategoryTags |  | PX_Data_Search_SPWikiCategoryTags | CategoryID, PageID |  |  |
| PX.Data.Search.SPWikiProduct |  | PX_Data_Search_SPWikiProduct | ProductID |  |  |
| PX.Data.Search.SPWikiProductTags |  | PX_Data_Search_SPWikiProductTags | PageID, ProductID |  |  |
| PX.Data.SearchIndex | Search Index | PX_Data_SearchIndex, SearchIndex | NoteID | Top |  |
| PX.Data.Services.Implementations.FavoriteActionRecord | Favorite Action | PX_Data_Services_Implementations_FavoriteActionRecord, FavoriteAction, FavoriteActionRecord | ActionName, IsPortal, ScreenID, UserID |  |  |
| PX.Data.SystemColor |  | PX_Data_SystemColor | ColorName |  |  |
| PX.Data.Update.UPMeasureEndpoint |  | PX_Data_Update_UPMeasureEndpoint | EndpointID |  |  |
| PX.Data.Update.UPMeasureHistory |  | PX_Data_Update_UPMeasureHistory | EndpointID, MeasureID | DateOnly, TimeOnly |  |
| PX.Data.Update.UPSelectedEndpoint |  | PX_Data_Update_UPSelectedEndpoint | EndpointID |  |  |
| PX.Data.UserRecords.FavoriteRecords.FavoriteRecord | Favorite Record | PX_Data_UserRecords_FavoriteRecords_FavoriteRecord, FavoriteRecord | EntityType, IsPortal, RefNoteId, UserID |  |  |
| PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord | Viewed Record | PX_Data_UserRecords_RecentlyVisitedRecords_VisitedRecord, ViewedRecord, VisitedRecord | EntityType, IsPortal, RefNoteId, UserID |  |  |
| PX.Data.Wiki.Tags.RoleInTag | Roles In Tag | PX_Data_Wiki_Tags_RoleInTag, RolesInTag, RoleInTag | Rolename, TagID |  |  |
| PX.Data.Wiki.Tags.Tag | Tag | PX_Data_Wiki_Tags_Tag, Tag | TagID | NoteText |  |
| PX.Data.Wiki.Tags.UploadFileTag | File Tag | PX_Data_Wiki_Tags_UploadFileTag, FileTag, UploadFileTag | FileID, TagID |  |  |
| PX.DataSync.HubSpot.HSEntitySetup |  | PX_DataSync_HubSpot_HSEntitySetup | EntityType | SyncProcessStatus, NoteText |  |
| PX.DataSync.HubSpot.HSMarketingListMember |  | PX_DataSync_HubSpot_HSMarketingListMember | MarketingListMemberID |  |  |
| PX.DataSync.SendGrid.SMSendGridAccountsSettings | SendGrid Accounts Settings | PX_DataSync_SendGrid_SMSendGridAccountsSettings, SendGridAccountsSettings, SMSendGridAccountsSettings | SendGridConnectionID |  |  |
| PX.DataSync.SendGrid.SMSendGridRecipient | SendGrid Recipients | PX_DataSync_SendGrid_SMSendGridRecipient, SendGridRecipients, SMSendGridRecipient | Address, RefNoteID | Name |  |
| PX.DataSync.SendGrid.SMSendGridSettings | SendGrid Settings | PX_DataSync_SendGrid_SMSendGridSettings, SendGridSettings, SMSendGridSettings | SendGridConnectionID | SendGridApiUrl, EnableWebhooks |  |
| PX.DataSync.SendGrid.SMSendGridSuppressionGroup | SendGrid Suppression Group | PX_DataSync_SendGrid_SMSendGridSuppressionGroup, SendGridSuppressionGroup, SMSendGridSuppressionGroup | GroupID, SendGridConnectionID |  |  |
| PX.EP.EPLoginType | Login Type | PX_EP_EPLoginType, LoginType, EPLoginType | LoginTypeID, LoginTypeName | IsExternal |  |
| PX.EP.EPLoginTypeAllowsRole | Login Type Allow Role | PX_EP_EPLoginTypeAllowsRole, LoginTypeAllowRole, EPLoginTypeAllowsRole | LoginTypeID, Rolename |  |  |
| PX.EP.EPManagedLoginType | Login Type Managed | PX_EP_EPManagedLoginType, LoginTypeManaged, EPManagedLoginType | LoginTypeID, ParentLoginTypeID |  |  |
| PX.ESign.ESignAccount | eSign Account | PX_ESign_ESignAccount, eSignAccount | AccountCD | ConnectionStatus |  |
| PX.ESign.ESignAccountUserRule | eSign Account User Rule | PX_ESign_ESignAccountUserRule, eSignAccountUserRule | AccountID, OwnerID |  |  |
| PX.ESign.ESignEnvelopeInfo | eSign Request | PX_ESign_ESignEnvelopeInfo, eSignRequest, ESignEnvelopeInfo | EnvelopeInfoID | IsSendAvailable, IsDeleteAvailable, IsRemindAvailable, IsVoidAvailable |  |
| PX.ESign.ESignRecipient | eSign Recipient | PX_ESign_ESignRecipient, eSignRecipient | RecipientID |  |  |
| PX.ExternalCarriersCommon.ShipEngineCarrierService |  | PX_ExternalCarriersCommon_ShipEngineCarrierService | CarrierPluginID, ServiceCode |  |  |
| PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData | Opportunity Carrier Data | PX_ExternalCarriersHelper_CROpportunityRevisionCarrierData, OpportunityCarrierData, CROpportunityRevisionCarrierData | RefNoteID |  |  |
| PX.ExternalCarriersHelper.InventoryItemCarrierData | Inventory Item Carrier Data | PX_ExternalCarriersHelper_InventoryItemCarrierData, InventoryItemCarrierData | InventoryID |  |  |
| PX.ExternalCarriersHelper.SETerritoriesMapping |  | PX_ExternalCarriersHelper_SETerritoriesMapping | CarrierPluginID, CountryID, StateID |  |  |
| PX.ExternalCarriersHelper.SOOrderCarrierData | SO Order Carrier Data | PX_ExternalCarriersHelper_SOOrderCarrierData, SOOrderCarrierData | OrderNbr, OrderType |  |  |
| PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates | SOOrder Carrier Data for Shop for Rates | PX_ExternalCarriersHelper_SOOrderCarrierDataShopForRates, SOOrderCarrierDataforShopforRates, SOOrderCarrierDataShopForRates | OrderNbr, OrderType |  |  |
| PX.ExternalCarriersHelper.SOOrderShopForRates | SOOrder Data for Shop for Rates | PX_ExternalCarriersHelper_SOOrderShopForRates, SOOrderDataforShopforRates, SOOrderShopForRates | OrderNbr, OrderType | CarrierPluginID, ShipViaSelectedFromDocument |  |
| PX.ExternalCarriersHelper.SOShipmentCarrierData | SO Shipment Carrier Data | PX_ExternalCarriersHelper_SOShipmentCarrierData, SOShipmentCarrierData | ShipmentNbr |  |  |
| PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates | SOShipment Carrier Data for Shop for Rates | PX_ExternalCarriersHelper_SOShipmentCarrierDataShopForRates, SOShipmentCarrierDataforShopforRates, SOShipmentCarrierDataShopForRates | ShipmentNbr |  |  |
| PX.ExternalCarriersHelper.SOShipmentShopForRates | SOShipment Data for Shop for Rates | PX_ExternalCarriersHelper_SOShipmentShopForRates, SOShipmentDataforShopforRates, SOShipmentShopForRates | ShipmentNbr | CarrierPluginID, ShipViaSelectedFromDocument |  |
| PX.FS.FSGPSTrackingHistory |  | PX_FS_FSGPSTrackingHistory | ExecutionDate, TrackingID |  |  |
| PX.FS.FSGPSTrackingRequest |  | PX_FS_FSGPSTrackingRequest | RequestID | NoteText |  |
| PX.GIReports.Maintenance.DAC.GIReport | Grouped Table | PX_GIReports_Maintenance_DAC_GIReport, GroupedTable, GIReport | ReportID | NoteText |  |
| PX.GIReports.Maintenance.DAC.GIReportGroup | Grouped Table Groups | PX_GIReports_Maintenance_DAC_GIReportGroup, GroupedTableGroups, GIReportGroup | GroupID, ReportID | IsDetail, IsTotal, NoteText |  |
| PX.GIReports.Maintenance.DAC.GIReportGroupColumn | Grouped Table Columns | PX_GIReports_Maintenance_DAC_GIReportGroupColumn, GroupedTableColumns, GIReportGroupColumn | GroupID, LineNbr, ReportID | NoteText |  |
| PX.GIReports.Maintenance.DAC.GIReportGroupGrouping | Grouped Table Grouping | PX_GIReports_Maintenance_DAC_GIReportGroupGrouping, GroupedTableGrouping, GIReportGroupGrouping | GroupID, LineNbr, ReportID | NoteText |  |
| PX.GIReports.Maintenance.DAC.GIReportGroupSorting | Grouped Table Sorting | PX_GIReports_Maintenance_DAC_GIReportGroupSorting, GroupedTableSorting, GIReportGroupSorting | GroupID, LineNbr, ReportID | NoteText |  |
| PX.Mail.Log.DAC.EmailLog | Email Log | PX_Mail_Log_DAC_EmailLog, EmailLog | LogEntryID |  |  |
| PX.ML.Chat.DAC.MLChatMessage | MLChatMessage | PX_ML_Chat_DAC_MLChatMessage, MLChatMessage | MessageID |  |  |
| PX.ML.Chat.DAC.MLChatMessageAttachment | MLChatMessageAttachment | PX_ML_Chat_DAC_MLChatMessageAttachment, MLChatMessageAttachment | FileID, MessageID |  |  |
| PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory | MLAIAssistantUnitsConsumptionHistory | PX_ML_Chat_Licensing_DAC_MLAIAssistantUnitsConsumptionHistory, MLAIAssistantUnitsConsumptionHistory | HistoryID |  |  |
| PX.MSGraph.DAC.SM.SMGraphPermission | Graph Access Rights | PX_MSGraph_DAC_SM_SMGraphPermission, GraphAccessRights, SMGraphPermission | AccessRight | Description, ApplicableFor, AdminConsent |  |
| PX.MSTeams.DAC.SM.SMTeamsChannel | Teams Channel | PX_MSTeams_DAC_SM_SMTeamsChannel, TeamsChannel, SMTeamsChannel | ChannelID | IsNotificationConfigured, TeamPhoto |  |
| PX.MSTeams.DAC.SM.SMTeamsMember | Teams Member | PX_MSTeams_DAC_SM_SMTeamsMember, TeamsMember, SMTeamsMember | MemberID | NoteText, TeamsStatus, GraphTeamsStatus, TeamPhoto, TeamsRedirectType |  |
| PX.MSTeams.DAC.SM.SMTeamsMemberMapping | Teams Member Mapping | PX_MSTeams_DAC_SM_SMTeamsMemberMapping, TeamsMemberMapping, SMTeamsMemberMapping | MemberID, TeamsID |  |  |
| PX.MSTeams.DAC.SM.SMTeamsNotification | Teams Notification | PX_MSTeams_DAC_SM_SMTeamsNotification, TeamsNotification, SMTeamsNotification | NotificationID | NoteText, ShowReportTabExpr, ShowSendByEventsTabExpr |  |
| PX.MSTeams.DAC.SM.SMTeamsTeam | Teams Team | PX_MSTeams_DAC_SM_SMTeamsTeam, TeamsTeam, SMTeamsTeam | TeamsID | NoteText, TeamPhoto |  |
| PX.OAuthClient.DAC.OAuthApplication |  | PX_OAuthClient_DAC_OAuthApplication | ApplicationID |  |  |
| PX.OAuthClient.DAC.OAuthResource | Application Resource | PX_OAuthClient_DAC_OAuthResource, ApplicationResource, OAuthResource | ApplicationID, ResourceCD | SitemapTitle, SitemapSelectorTitle, SitemapScreenID, WorkspaceID, SubcategoryID |  |
| PX.OAuthClient.DAC.OAuthToken |  | PX_OAuthClient_DAC_OAuthToken | TokenID | NoteText, UtcNow, ExpiresOn |  |
| PX.OAuthClient.DAC.ResourceRole | Role | PX_OAuthClient_DAC_ResourceRole | ApplicationName, Rolename |  | yes |
| PX.Objects.AM.AMBatch | AM Batch | PX_Objects_AM_AMBatch, AMBatch | BatNbr, DocType | NoteText, EditableBatch, DeletableBatch |  |
| PX.Objects.AM.AMBatchCost | AM Batch Cost | PX_Objects_AM_AMBatchCost, AMBatchCost | BatNbr, DocType |  |  |
| PX.Objects.AM.AMBatchItemLotSerialAttributesHeader | AMBatchItemLotSerialAttributesHeader | PX_Objects_AM_AMBatchItemLotSerialAttributesHeader, AMBatchItemLotSerialAttributesHeader | BatNbr, DocType, InventoryID, LotSerialNbr | NoteText |  |
| PX.Objects.AM.AMBomAttribute | BOM Attributes | PX_Objects_AM_AMBomAttribute, BOMAttributes, AMBomAttribute | BOMID, LineNbr, RevisionID |  |  |
| PX.Objects.AM.AMBomCost | BOM Cost | PX_Objects_AM_AMBomCost, BOMCost, AMBomCost | BOMID, CuryID, RevisionID, SiteID, UserID | DirectCost |  |
| PX.Objects.AM.AMBomCostHistory | Cost Roll History | PX_Objects_AM_AMBomCostHistory, CostRollHistory, AMBomCostHistory | BOMID, CuryID, RevisionID, SiteID, StartDate | DirectCost |  |
| PX.Objects.AM.AMBOMCurySettings | BOM Currency Settings | PX_Objects_AM_AMBOMCurySettings, BOMCurrencySettings, AMBOMCurySettings | BOMID, CuryID, LineID, LineType, OperationID, RevisionID |  |  |
| PX.Objects.AM.AMBomItem | BOM Item | PX_Objects_AM_AMBomItem, BOMItem, AMBomItem | BOMID, RevisionID | NoteText, Rejected |  |
| PX.Objects.AM.AMBomItem2 | BOM Item | PX_Objects_AM_AMBomItem2, BOMItem1, AMBomItem2 | BOMID, RevisionID |  |  |
| PX.Objects.AM.AMBomItem3 | BOM Item | PX_Objects_AM_AMBomItem3, BOMItem2, AMBomItem3 | BOMID, RevisionID |  |  |
| PX.Objects.AM.AMBomItemActive | BOM Item Active | PX_Objects_AM_AMBomItemActive, BOMItemActive, AMBomItemActive | BOMID, RevisionID |  |  |
| PX.Objects.AM.AMBomItemActive2 | BOM Item Active 2 | PX_Objects_AM_AMBomItemActive2, BOMItemActive2, AMBomItemActive2 | BOMID, RevisionID |  |  |
| PX.Objects.AM.AMBomItemBomDefaults | BOM Item BOM Default | PX_Objects_AM_AMBomItemBomDefaults, BOMItemBOMDefault, AMBomItemBomDefaults | BOMID, RevisionID | IsItemDefaultBOM, IsItemSiteDefaultBOM, IsDefaultBOM |  |
| PX.Objects.AM.AMBomMatl | BOM Material | PX_Objects_AM_AMBomMatl, BOMMaterial, AMBomMatl | BOMID, CurrBOMID, CurrOperationID, CurrRevisionID, CuryID, CuryLineID, LineID, LineType, OperationID, RevisionID | NoteText, LineNbr, PlanCost, OriginalTreeNodeID |  |
| PX.Objects.AM.AMBomMatlCury | AMBomMatlCurrency | PX_Objects_AM_AMBomMatlCury, AMBomMatlCurrency, AMBomMatlCury | BOMID, CuryID, LineID, LineType, OperationID, RevisionID |  |  |
| PX.Objects.AM.AMBomOper | BOM Operation | PX_Objects_AM_AMBomOper, BOMOperation, AMBomOper | BOMID, OperationCD, RevisionID | NoteText, SetupTimeRaw, RunUnitTimeRaw, MachineUnitTimeRaw, QueueTimeRaw, FinishTimeRaw, MoveTimeRaw, NewOperationCD, OriginalTreeNodeID |  |
| PX.Objects.AM.AMBomOperCury | AMBomOperCurrency | PX_Objects_AM_AMBomOperCury, AMBomOperCurrency, AMBomOperCury | BOMID, CuryID, LineID, LineType, OperationID, RevisionID |  |  |
| PX.Objects.AM.AMBomOvhd | BOM Overhead | PX_Objects_AM_AMBomOvhd, BOMOverhead, AMBomOvhd | BOMID, LineID, OperationID, RevisionID | NoteText |  |
| PX.Objects.AM.AMBomRef | BOM Reference Designator | PX_Objects_AM_AMBomRef, BOMReferenceDesignator, AMBomRef | BOMID, LineID, MatlLineID, OperationID, RevisionID | NoteText |  |
| PX.Objects.AM.AMBomStep | BOM Step | PX_Objects_AM_AMBomStep, BOMStep, AMBomStep | BOMID, LineID, OperationID, RevisionID | NoteText |  |
| PX.Objects.AM.AMBomTool | BOM Tool | PX_Objects_AM_AMBomTool, BOMTool, AMBomTool | BOMID, LineID, OperationID, RevisionID | NoteText |  |
| PX.Objects.AM.AMBomToolCury | AMBomToolCurrency | PX_Objects_AM_AMBomToolCury, AMBomToolCurrency, AMBomToolCury | BOMID, CuryID, LineID, LineType, OperationID, RevisionID |  |  |
| PX.Objects.AM.AMCalendarBreakTime | Calendar Break Time | PX_Objects_AM_AMCalendarBreakTime, CalendarBreakTime, AMCalendarBreakTime | CalendarID, DayOfWeek, StartTime |  |  |
| PX.Objects.AM.AMClockItem | Clock Employee | PX_Objects_AM_AMClockItem, ClockEmployee, AMClockItem | EmployeeID | LaborTime, NoteText, IsClockedIn |  |
| PX.Objects.AM.AMClockItemSplit | Clock Employee Split | PX_Objects_AM_AMClockItemSplit, ClockEmployeeSplit, AMClockItemSplit | EmployeeID, LineNbr, SplitLineNbr | LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.AM.AMClockTran | Clock Transaction | PX_Objects_AM_AMClockTran, ClockTransaction, AMClockTran | EmployeeID, LineNbr | NoteText, IsStockItem, LaborTimeSeconds, Duration |  |
| PX.Objects.AM.AMClockTranSplit | Clock Transaction Split | PX_Objects_AM_AMClockTranSplit, ClockTransactionSplit, AMClockTranSplit | EmployeeID, LineNbr, SplitLineNbr | LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.AM.AMConfigResultsAttribute | Configuration Attribute Result | PX_Objects_AM_AMConfigResultsAttribute, ConfigurationAttributeResult, AMConfigResultsAttribute | AttributeLineNbr, ConfigResultsID |  |  |
| PX.Objects.AM.AMConfigResultsFeature | Configuration Feature Result | PX_Objects_AM_AMConfigResultsFeature, ConfigurationFeatureResult, AMConfigResultsFeature | ConfigResultsID, FeatureLineNbr | MinMaxSelection, MinLotMaxQty |  |
| PX.Objects.AM.AMConfigResultsOption | Configuration Option Result | PX_Objects_AM_AMConfigResultsOption, ConfigurationOptionResult, AMConfigResultsOption | ConfigResultsID, FeatureLineNbr, OptionLineNbr | ActualQty, IsRemovable, MinLotMaxQty |  |
| PX.Objects.AM.AMConfigResultsRule | Configuration Rule Result | PX_Objects_AM_AMConfigResultsRule, ConfigurationRuleResult, AMConfigResultsRule | ConfigResultsID, RuleLineNbr, RuleSource, RuleSourceLineNbr, RuleTarget, TargetLineNbr, TargetSubLineNbr |  |  |
| PX.Objects.AM.AMConfiguration | Configuration | PX_Objects_AM_AMConfiguration, Configuration, AMConfiguration | ConfigurationID, Revision | NoteText |  |
| PX.Objects.AM.AMConfigurationAttribute | Configuration Attribute | PX_Objects_AM_AMConfigurationAttribute, ConfigurationAttribute, AMConfigurationAttribute | ConfigurationID, LineNbr, Revision | IsFormula |  |
| PX.Objects.AM.AMConfigurationAttributeRule | Configuration Attribute Rule | PX_Objects_AM_AMConfigurationAttributeRule, ConfigurationAttributeRule, AMConfigurationAttributeRule | ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr |  |  |
| PX.Objects.AM.AMConfigurationFeature | Configuration Feature | PX_Objects_AM_AMConfigurationFeature, ConfigurationFeature, AMConfigurationFeature | ConfigurationID, LineNbr, Revision |  |  |
| PX.Objects.AM.AMConfigurationFeatureRule | Configuration Feature Rule | PX_Objects_AM_AMConfigurationFeatureRule, ConfigurationFeatureRule, AMConfigurationFeatureRule | ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr | SourceOptionLineNbr |  |
| PX.Objects.AM.AMConfigurationKeys | Configuration Keys | PX_Objects_AM_AMConfigurationKeys, ConfigurationKeys, AMConfigurationKeys | ConfigResultsID | SupplementalPriceTotal, CuryRate, CuryViewState |  |
| PX.Objects.AM.AMConfigurationOption | Configuration Option | PX_Objects_AM_AMConfigurationOption, ConfigurationOption, AMConfigurationOption | ConfigFeatureLineNbr, ConfigurationID, LineNbr, Revision |  |  |
| PX.Objects.AM.AMConfigurationOptionCurySettings | Config Option Currency Settings | PX_Objects_AM_AMConfigurationOptionCurySettings, ConfigOptionCurrencySettings, AMConfigurationOptionCurySettings | ConfigFeatureLineNbr, ConfigurationID, CuryID, LineNbr, Revision |  |  |
| PX.Objects.AM.AMConfigurationResults | Configuration Result | PX_Objects_AM_AMConfigurationResults, ConfigurationResult, AMConfigurationResults | ConfigResultsID | IsConfigurationTesting, SupplementalPriceTotal, DisplayPrice, UserOptionsError, IsSalesReferenced, IsOpportunityReferenced, IsProductionReferenced, CuryRate, CuryViewState |  |
| PX.Objects.AM.AMConfigurationRule | Configuration Rule | PX_Objects_AM_AMConfigurationRule, ConfigurationRule, AMConfigurationRule | ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr |  |  |
| PX.Objects.AM.AMDepartment | AM Department | PX_Objects_AM_AMDepartment, AMDepartment | DepartmentID | NoteText |  |
| PX.Objects.AM.AMDisassembleBatch | AM Disassemble | PX_Objects_AM_AMDisassembleBatch, AMDisassemble, AMDisassembleBatch | BatchNbr, DocType | BatNbr, IsStockItem, EditableBatch |  |
| PX.Objects.AM.AMDisassembleBatchAttribute | AM Disassemble Transaction Attribute | PX_Objects_AM_AMDisassembleBatchAttribute, AMDisassembleTransactionAttribute, AMDisassembleBatchAttribute | BatNbr, DocType, LineNbr, ProdAttributeLineNbr, TranLineNbr |  |  |
| PX.Objects.AM.AMDisassembleBatchSplit | AM Disassemble Batch Split | PX_Objects_AM_AMDisassembleBatchSplit, AMDisassembleBatchSplit | BatNbr, DocType, LineNbr, SplitLineNbr | CostSubItemID, CostSiteID, LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.AM.AMDisassembleTran | AM Disassemble Transaction | PX_Objects_AM_AMDisassembleTran, AMDisassembleTransaction, AMDisassembleTran | BatNbr, DocType, LineNbr |  |  |
| PX.Objects.AM.AMDisassembleTranSplit | AM Disassemble Transaction Split | PX_Objects_AM_AMDisassembleTranSplit, AMDisassembleTransactionSplit, AMDisassembleTranSplit | BatNbr, DocType, LineNbr, SplitLineNbr |  |  |
| PX.Objects.AM.AMECOItem | ECO Item | PX_Objects_AM_AMECOItem, ECOItem, AMECOItem | ECOID | ID, NoteText, Rejected |  |
| PX.Objects.AM.AMECOSetupApproval | ECO Setup Approval | PX_Objects_AM_AMECOSetupApproval, ECOSetupApproval, AMECOSetupApproval | ApprovalID | NonExistence |  |
| PX.Objects.AM.AMECRItem | ECR Item | PX_Objects_AM_AMECRItem, ECRItem, AMECRItem | ECRID | ID, NoteText, Rejected |  |
| PX.Objects.AM.AMECRSetupApproval | ECR Setup Approval | PX_Objects_AM_AMECRSetupApproval, ECRSetupApproval, AMECRSetupApproval | ApprovalID | NonExistence |  |
| PX.Objects.AM.AMEstimateClass | Estimate Class | PX_Objects_AM_AMEstimateClass, EstimateClass, AMEstimateClass | EstimateClassID | NoteText |  |
| PX.Objects.AM.AMEstimateHistory | Estimate History | PX_Objects_AM_AMEstimateHistory, EstimateHistory, AMEstimateHistory | EstimateID, LineNbr |  |  |
| PX.Objects.AM.AMEstimateItem | Estimate Item | PX_Objects_AM_AMEstimateItem, EstimateItem, AMEstimateItem | EstimateID, RevisionID | ExtCostDisplay, NoteText, DescriptionAsPlainText, IsPrimary, CuryRate, CuryViewState |  |
| PX.Objects.AM.AMEstimateMatl | Estimate Material | PX_Objects_AM_AMEstimateMatl, EstimateMaterial, AMEstimateMatl | EstimateID, LineID, OperationID, RevisionID | LineNbr, NoteText, QtyReqWithScrap, BaseOrderQty |  |
| PX.Objects.AM.AMEstimateOper | Estimate Operations | PX_Objects_AM_AMEstimateOper, EstimateOperations, AMEstimateOper | EstimateID, OperationCD, RevisionID | WcID, RunUnitsPerHour, MachineUnitsPerHour, NoteText, SetupTimeRaw, RunUnitTimeRaw, MachineUnitTimeRaw, QueueTimeRaw, FinishTimeRaw, MoveTimeRaw |  |
| PX.Objects.AM.AMEstimateOvhd | Estimate Overhead | PX_Objects_AM_AMEstimateOvhd, EstimateOverhead, AMEstimateOvhd | EstimateID, LineID, OperationID, RevisionID | NoteText |  |
| PX.Objects.AM.AMEstimatePriceBreak | Estimate Price Break | PX_Objects_AM_AMEstimatePriceBreak, EstimatePriceBreak, AMEstimatePriceBreak | EstimateID, LineNbr, RevisionID | IsPrimary, NoteText, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.AM.AMEstimateReference | Estimate Reference | PX_Objects_AM_AMEstimateReference, EstimateReference, AMEstimateReference | EstimateID, RevisionID | QuoteNbrLink, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.AM.AMEstimateStep | Estimate Step | PX_Objects_AM_AMEstimateStep, EstimateStep, AMEstimateStep | EstimateID, LineID, OperationID, RevisionID | NoteText |  |
| PX.Objects.AM.AMEstimateTool | Estimate Tool | PX_Objects_AM_AMEstimateTool, EstimateTool, AMEstimateTool | EstimateID, LineID, OperationID, RevisionID | NoteText |  |
| PX.Objects.AM.AMFeature | Feature | PX_Objects_AM_AMFeature, Feature, AMFeature | FeatureID | NoteText |  |
| PX.Objects.AM.AMFeatureAttribute | Feature Attribute | PX_Objects_AM_AMFeatureAttribute, FeatureAttribute, AMFeatureAttribute | FeatureID, LineNbr | IsFormula |  |
| PX.Objects.AM.AMFeatureOption | Feature Option | PX_Objects_AM_AMFeatureOption, FeatureOption, AMFeatureOption | FeatureID, LineNbr |  |  |
| PX.Objects.AM.AMFixedDemand | AM Fixed Demand | PX_Objects_AM_AMFixedDemand, AMFixedDemand | PlanID | OrderQty, AddLeadTimeDays, NoteText, DemandDocumentType, DemandDocumentID, DemandProjectID, DemandTaskID, DemandCostCodeID, DemandInventorySource, MLProvisioningDocCreationDate, DemandCustomerID, DemandCustomerAcctName, DemandLocationID, CreateSubAssemblyOrders |  |
| PX.Objects.AM.AMForecast | Forecast | PX_Objects_AM_AMForecast, Forecast, AMForecast | ForecastID | NoteText |  |
| PX.Objects.AM.AMForecastPeriod | Forecast Period | PX_Objects_AM_AMForecastPeriod, ForecastPeriod, AMForecastPeriod | ForecastID, PeriodEnd, PeriodStart, TimePeriod |  |  |
| PX.Objects.AM.AMForecastStaging | Forecast Staging | PX_Objects_AM_AMForecastStaging, ForecastStaging, AMForecastStaging | BeginDate, CustomerID, EndDate, InventoryID, SiteID, SubItemID, UserID | ChangeUnits, PercentChange, CustomerID2 |  |
| PX.Objects.AM.AMLaborCode | Labor Code | PX_Objects_AM_AMLaborCode, LaborCode, AMLaborCode | LaborCodeID | NoteText |  |
| PX.Objects.AM.AMMach | Machine | PX_Objects_AM_AMMach, Machine, AMMach | MachID | NoteText |  |
| PX.Objects.AM.AMMachCurySettings | Machine Currency Settings | PX_Objects_AM_AMMachCurySettings, MachineCurrencySettings, AMMachCurySettings | CuryID, MachID |  |  |
| PX.Objects.AM.AMMachSchd | Work Center Schedule | PX_Objects_AM_AMMachSchd, WorkCenterSchedule, AMMachSchd | MachID, SchdDate | ResourceID |  |
| PX.Objects.AM.AMMachSchdDetail | Machine Schedule Detail | PX_Objects_AM_AMMachSchdDetail, MachineScheduleDetail, AMMachSchdDetail | RecordID | ResourceID, StartTimeString, EndTimeString |  |
| PX.Objects.AM.AMMPS | Master Production Schedule | PX_Objects_AM_AMMPS, MasterProductionSchedule, AMMPS | MPSID, MPSTypeID | NoteText |  |
| PX.Objects.AM.AMMPSType | Master Production Schedule Type | PX_Objects_AM_AMMPSType, MasterProductionScheduleType, AMMPSType | MPSTypeID | NoteText |  |
| PX.Objects.AM.AMMRPBucket | Inventory Planning Buckets | PX_Objects_AM_AMMRPBucket, InventoryPlanningBuckets, AMMRPBucket | BucketID | NoteText |  |
| PX.Objects.AM.AMMRPBucketDetail | Inventory Planning Bucket Detail | PX_Objects_AM_AMMRPBucketDetail, InventoryPlanningBucketDetail, AMMRPBucketDetail | Bucket, BucketID |  |  |
| PX.Objects.AM.AMMRPBucketDetailInq | Inventory Planning Bucket Detail Inquiry | PX_Objects_AM_AMMRPBucketDetailInq, InventoryPlanningBucketDetailInquiry, AMMRPBucketDetailInq | Bucket, BucketID, InventoryID, SiteID, SubItemID |  |  |
| PX.Objects.AM.AMMRPBucketInq | Inventory Planning Bucket Inquiry | PX_Objects_AM_AMMRPBucketInq, InventoryPlanningBucketInquiry, AMMRPBucketInq | BucketID, InventoryID, SiteID, SubItemID |  |  |
| PX.Objects.AM.AMMTran | AM Transaction | PX_Objects_AM_AMMTran, AMTransaction, AMMTran | BatNbr, DocType, LineNbr | LaborTimeRaw, NoteText, HasReference, IsStockItem, TranTypeChanged |  |
| PX.Objects.AM.AMMTranAttribute | Transaction Attributes | PX_Objects_AM_AMMTranAttribute, TransactionAttributes, AMMTranAttribute | BatNbr, DocType, LineNbr, ProdAttributeLineNbr, TranLineNbr |  |  |
| PX.Objects.AM.AMMTranLotSerialNbrAll | AM Transaction All Lot/Serial Nbr | PX_Objects_AM_AMMTranLotSerialNbrAll, AMTransactionAllLotSerialNbr, AMMTranLotSerialNbrAll | BatNbr, DocType, LineNbr |  |  |
| PX.Objects.AM.AMMTranMoveByLotSerial | AM Transaction by LotSerial | PX_Objects_AM_AMMTranMoveByLotSerial, AMTransactionbyLotSerial, AMMTranMoveByLotSerial | BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID, SiteID |  |  |
| PX.Objects.AM.AMMTranSplit | AM Transaction Split | PX_Objects_AM_AMMTranSplit, AMTransactionSplit, AMMTranSplit | BatNbr, DocType, LineNbr, SplitLineNbr | CostSubItemID, CostSiteID, LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.AM.AMOrderCrossRef | Order Cross Reference | PX_Objects_AM_AMOrderCrossRef, OrderCrossReference, AMOrderCrossRef | LineNbr, UserID | DmdDetGroupedRecNbrs, CreateSubAssemblyOrders, Action |  |
| PX.Objects.AM.AMOrderType | AM Order Types | PX_Objects_AM_AMOrderType, AMOrderTypes, AMOrderType | OrderType | NoteText |  |
| PX.Objects.AM.AMOrderTypeAttribute | Order Type Attributes | PX_Objects_AM_AMOrderTypeAttribute, OrderTypeAttributes, AMOrderTypeAttribute | LineNbr, OrderType |  |  |
| PX.Objects.AM.AMOverhead | Overhead | PX_Objects_AM_AMOverhead, Overhead, AMOverhead | OvhdID | NoteText |  |
| PX.Objects.AM.AMOverheadCurySettings | Overhead Currency Settings | PX_Objects_AM_AMOverheadCurySettings, OverheadCurrencySettings, AMOverheadCurySettings | CuryID, OvhdID |  |  |
| PX.Objects.AM.AMProdAttribute | Production Attributes | PX_Objects_AM_AMProdAttribute, ProductionAttributes, AMProdAttribute | LineNbr, OrderType, ProdOrdID |  |  |
| PX.Objects.AM.AMProdEvnt | Production Event | PX_Objects_AM_AMProdEvnt, ProductionEvent, AMProdEvnt | LineNbr, OrderType, ProdOrdID | CreatedByScreenIDTitle |  |
| PX.Objects.AM.AMProdItem | Production Item | PX_Objects_AM_AMProdItem, ProductionItem, AMProdItem | OrderType, ProdOrdID | BaseQtyRemaining, QtyRemaining, IsConfigurable, NoteText, TranDate, WIPBalance, BuildProductionBom, Reschedule, LineQtyAvail, LineQtyHardAvail |  |
| PX.Objects.AM.AMProdItemRelated | Related Production Item | PX_Objects_AM_AMProdItemRelated, RelatedProductionItem, AMProdItemRelated | OrderType, ProdOrdID | RelationType, QtyRemaining |  |
| PX.Objects.AM.AMProdItemSplit | Production Item Split | PX_Objects_AM_AMProdItemSplit, ProductionItemSplit, AMProdItemSplit | OrderType, ProdOrdID, SplitLineNbr | CostSubItemID, CostSiteID, LotSerClassID, AssignedNbr, ProjectID, TaskID, BaseQtyRemaining, QtyRemaining |  |
| PX.Objects.AM.AMProdItemSplitPreassign | Prod Item Split Lot/Serial | PX_Objects_AM_AMProdItemSplitPreassign, ProdItemSplitLotSerial, AMProdItemSplitPreassign | LotSerialNbr, OrderType, ProdOrdID | QtyRemaining |  |
| PX.Objects.AM.AMProdMatl | Production Material | PX_Objects_AM_AMProdMatl, ProductionMaterial, AMProdMatl | LineID, OperationID, OrderType, ProdOrdID | BaseOperTotalQty, QtyReqWithScrap, NoteText, LineNbr, IsByproduct, IsFixedMaterial, QtyRemaining, BaseQtyRemaining, PlanCost, UpdateProject, POLinkEnable, ProdLinkEnable, LineQtyAvail, LineQtyHardAvail |  |
| PX.Objects.AM.AMProdMatlLotSerial | Production Material Lot/Serial Nbr. | PX_Objects_AM_AMProdMatlLotSerial, ProductionMaterialLotSerialNbr, AMProdMatlLotSerial | LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID |  |  |
| PX.Objects.AM.AMProdMatlLotSerialAssigned | Material Lot Serial Assigned | PX_Objects_AM_AMProdMatlLotSerialAssigned, MaterialLotSerialAssigned, AMProdMatlLotSerialAssigned | LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID | QtyRequired |  |
| PX.Objects.AM.AMProdMatlLotSerialUnassigned | Material Lot Serial Unassigned | PX_Objects_AM_AMProdMatlLotSerialUnassigned, MaterialLotSerialUnassigned, AMProdMatlLotSerialUnassigned | LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID | QtyRequired, QtyToAllocate |  |
| PX.Objects.AM.AMProdMatlSplit | Production Material Split | PX_Objects_AM_AMProdMatlSplit, ProductionMaterialSplit, AMProdMatlSplit | LineID, OperationID, OrderType, ProdOrdID, SplitLineNbr | AssignedNbr, LotSerClassID, ProjectID, TaskID, CostSubItemID, CostSiteID |  |
| PX.Objects.AM.AMProdNumber | Production Number | PX_Objects_AM_AMProdNumber, ProductionNumber, AMProdNumber | OrderType, ProdOrdID |  |  |
| PX.Objects.AM.AMProdOper | Production Operation | PX_Objects_AM_AMProdOper, ProductionOperation, AMProdOper | OperationCD, OrderType, ProdOrdID | QtyRemaining, BaseQtyRemaining, NoteText, PlanTotal, WIPTotal, HasActualCost, VarianceLabor, VarianceLaborTime, VarianceMachine, VarianceMaterial, VarianceTool, VarianceFixedOverhead, VarianceVariableOverhead, VarianceSubcontract, VarianceTotal, WIPBalance, ActualLaborTimeRaw, ActualMachineTimeRaw, PlanLaborTimeRaw, PlanMachineTimeRaw, VarianceLaborTimeRaw, SetupTimeRaw, RunUnitTimeRaw, MachineUnitTimeRaw, QueueTimeRaw, FinishTimeRaw, MoveTimeRaw, ShipRemainingQty, BaseShipRemainingQty, AtVendorQuantity, BaseAtVendorQuantity |  |
| PX.Objects.AM.AMProdOvhd | Production Overhead | PX_Objects_AM_AMProdOvhd, ProductionOverhead, AMProdOvhd | LineID, OperationID, OrderType, ProdOrdID | NoteText |  |
| PX.Objects.AM.AMProdStep | Production Step | PX_Objects_AM_AMProdStep, ProductionStep, AMProdStep | LineID, OperationID, OrderType, ProdOrdID | NoteText |  |
| PX.Objects.AM.AMProdTool | Production Tool | PX_Objects_AM_AMProdTool, ProductionTool, AMProdTool | LineID, OperationID, OrderType, ProdOrdID | NoteText |  |
| PX.Objects.AM.AMProdTotal | Production Totals | PX_Objects_AM_AMProdTotal, ProductionTotals, AMProdTotal | OrderType, ProdOrdID | PlanTotal, PlanUnitCost, QtyComplete, WIPTotal, WIPComp, VarianceLabor, VarianceLaborTime, VarianceMachine, VarianceMaterial, VarianceTool, VarianceFixedOverhead, VarianceVariableOverhead, VarianceSubcontract, QtyRemaining, VarianceTotal, WIPBalance, NoteText, ActualLaborTimeRaw, PlanLaborTimeRaw, VarianceLaborTimeRaw |  |
| PX.Objects.AM.AMRPAuditHistory | Inventory Planning Audit History | PX_Objects_AM_AMRPAuditHistory, InventoryPlanningAuditHistory, AMRPAuditHistory | Recno |  |  |
| PX.Objects.AM.AMRPAuditTable | Inventory Planning Audit | PX_Objects_AM_AMRPAuditTable, InventoryPlanningAudit, AMRPAuditTable | Recno |  |  |
| PX.Objects.AM.AMRPDetail | Inventory Planning Detail | PX_Objects_AM_AMRPDetail, InventoryPlanningDetail, AMRPDetail | RecordID |  |  |
| PX.Objects.AM.AMRPDetailFP | Inventory Planning First Pass Detail | PX_Objects_AM_AMRPDetailFP, InventoryPlanningFirstPassDetail, AMRPDetailFP | RecordID | SiteSequence, ParentSchdNoteID, ProjectedOnHandQty, ConsolidatedStockingQty, ConsolidatedStockingOriginalQty |  |
| PX.Objects.AM.AMRPDetailPlan | Inventory Planning Detail Plan | PX_Objects_AM_AMRPDetailPlan, InventoryPlanningDetailPlan, AMRPDetailPlan | PlanID | RefNbr, OrigRefNoteID, Type |  |
| PX.Objects.AM.AMRPExceptions | Inventory Planning Exceptions | PX_Objects_AM_AMRPExceptions, InventoryPlanningExceptions, AMRPExceptions | RecordID |  |  |
| PX.Objects.AM.AMRPHistory | Inventory Planning History | PX_Objects_AM_AMRPHistory, InventoryPlanningHistory, AMRPHistory | ProcessID |  |  |
| PX.Objects.AM.AMRPItemSite | Inventory Planning Inventory | PX_Objects_AM_AMRPItemSite, InventoryPlanningInventory, AMRPItemSite | InventoryID, SiteID, SubItemID |  |  |
| PX.Objects.AM.AMRPPlan | MRP Plan | PX_Objects_AM_AMRPPlan, MRPPlan, AMRPPlan | RecordID | QtyOnHand |  |
| PX.Objects.AM.AMScanSetup | AM Scan Setup | PX_Objects_AM_AMScanSetup, AMScanSetup | BranchID |  |  |
| PX.Objects.AM.AMScanUserSetup | AM Scan User Setup | PX_Objects_AM_AMScanUserSetup, AMScanUserSetup | Mode, UserID |  |  |
| PX.Objects.AM.AMSchdItem | Schedule Item | PX_Objects_AM_AMSchdItem, ScheduleItem, AMSchdItem | OrderType, ProdOrdID, SchdID | QtyRemaining, NoteText, OrigConstDate, OrigSchedulingMethod |  |
| PX.Objects.AM.AMSchdOper | Schedule Operation | PX_Objects_AM_AMSchdOper, ScheduleOperation, AMSchdOper | LineNbr, OperationID, OrderType, ProdOrdID, SchdID | QtyRemaining, TotalPlanTime |  |
| PX.Objects.AM.AMSchdOperDetail | Scheduled Operation Details | PX_Objects_AM_AMSchdOperDetail, ScheduledOperationDetails, AMSchdOperDetail | RecordID |  |  |
| PX.Objects.AM.AMShift | Shift | PX_Objects_AM_AMShift, Shift, AMShift | ShiftCD, WcID | NoteText |  |
| PX.Objects.AM.AMSiteTransfer | Warehouse Transfer | PX_Objects_AM_AMSiteTransfer, WarehouseTransfer, AMSiteTransfer | SiteID, TransferSiteID |  |  |
| PX.Objects.AM.AMSubItemDefault | Subitem Default | PX_Objects_AM_AMSubItemDefault, SubitemDefault, AMSubItemDefault | InventoryID, SiteID, SubItemID |  |  |
| PX.Objects.AM.AMToolMst | Tools | PX_Objects_AM_AMToolMst, Tools, AMToolMst | ToolID | NoteText |  |
| PX.Objects.AM.AMToolMstCurySettings | Tools Currency Settings | PX_Objects_AM_AMToolMstCurySettings, ToolsCurrencySettings, AMToolMstCurySettings | CuryID, ToolID |  |  |
| PX.Objects.AM.AMToolSchdDetail | Tool Schedule Detail | PX_Objects_AM_AMToolSchdDetail, ToolScheduleDetail, AMToolSchdDetail | RecordID | ResourceID, StartTimeString, EndTimeString, NoteText |  |
| PX.Objects.AM.AMTranCost | AM Transaction Cost | PX_Objects_AM_AMTranCost, AMTransactionCost, AMTranCost | BatNbr, DocType, LineNbr | LaborTimeRaw |  |
| PX.Objects.AM.AMVendorShipLine | Vendor Shipment Line | PX_Objects_AM_AMVendorShipLine, VendorShipmentLine, AMVendorShipLine | LineNbr, ShipmentNbr | NoteText, UpdateProject |  |
| PX.Objects.AM.AMVendorShipLineSplit | Vendor Shipment Line Split | PX_Objects_AM_AMVendorShipLineSplit, VendorShipmentLineSplit, AMVendorShipLineSplit | LineNbr, ShipmentNbr, SplitLineNbr | LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.AM.AMVendorShipment | Vendor Shipment | PX_Objects_AM_AMVendorShipment, VendorShipment, AMVendorShipment | ShipmentNbr | NoteText, CuryRate, CuryViewState |  |
| PX.Objects.AM.AMVendorShipmentAddress | Vendor Shipment Address | PX_Objects_AM_AMVendorShipmentAddress, VendorShipmentAddress, AMVendorShipmentAddress | AddressID | OverrideAddress |  |
| PX.Objects.AM.AMVendorShipmentContact | Vendor Shipment Contact | PX_Objects_AM_AMVendorShipmentContact, VendorShipmentContact, AMVendorShipmentContact | ContactID | OverrideContact |  |
| PX.Objects.AM.AMWC | Work Center | PX_Objects_AM_AMWC, WorkCenter, AMWC | WcID | NoteText |  |
| PX.Objects.AM.AMWCCalendarPeriod | Work Center Calendar Period | PX_Objects_AM_AMWCCalendarPeriod, WorkCenterCalendarPeriod, AMWCCalendarPeriod | SequenceNbr, WcID | ShiftPriority |  |
| PX.Objects.AM.AMWCCury | AMWCCurrency | PX_Objects_AM_AMWCCury, AMWCCurrency, AMWCCury | CuryID, DetailID, WcID |  |  |
| PX.Objects.AM.AMWCCurySettings | Work Center Currency Settings | PX_Objects_AM_AMWCCurySettings, WorkCenterCurrencySettings, AMWCCurySettings | CuryID, DetailID, WcID |  |  |
| PX.Objects.AM.AMWCMach | Work Center Machines | PX_Objects_AM_AMWCMach, WorkCenterMachines, AMWCMach | MachID, WcID | NoteText |  |
| PX.Objects.AM.AMWCMachCury | AMWCMachCury | PX_Objects_AM_AMWCMachCury, AMWCMachCury | CuryID, DetailID, WcID |  |  |
| PX.Objects.AM.AMWCOvhd | Work Center Overheads | PX_Objects_AM_AMWCOvhd, WorkCenterOverheads, AMWCOvhd | OvhdID, WcID | NoteText |  |
| PX.Objects.AM.AMWCSchd | Work Center Schedule | PX_Objects_AM_AMWCSchd, WorkCenterSchedule1, AMWCSchd | SchdDate, ShiftCD, WcID | ResourceID |  |
| PX.Objects.AM.AMWCSchdDetail | Work Center Schedule Detail | PX_Objects_AM_AMWCSchdDetail, WorkCenterScheduleDetail, AMWCSchdDetail | RecordID | ResourceID |  |
| PX.Objects.AM.AMWCSubstitute | Work Center Substitute | PX_Objects_AM_AMWCSubstitute, WorkCenterSubstitute, AMWCSubstitute | SiteID, WcID |  |  |
| PX.Objects.AM.AMWrkMatl | Material Work Temp | PX_Objects_AM_AMWrkMatl, MaterialWorkTemp, AMWrkMatl | AutoNbr |  |  |
| PX.Objects.AM.BomInventoryItem | BOM Inventory Item | PX_Objects_AM_BomInventoryItem, BOMInventoryItem | InventoryCD |  |  |
| PX.Objects.AM.BomWhereUsedDetail | BOM Where Used Detail | PX_Objects_AM_BomWhereUsedDetail, BOMWhereUsedDetail | BOMID, LineID, OperationID, RevisionID, Sequence | NoteText, LineNbr, PlanCost, OriginalTreeNodeID, Level, QtyRequired, ItemClassID, Source, Description, ParentDescription, ParentItemClassID, Sequence, BOMStatus, EffStartDate, EffEndDate |  |
| PX.Objects.AM.CacheExtensions.INItemPlanAMExtension | AM Item Plan | PX_Objects_AM_CacheExtensions_INItemPlanAMExtension, AMItemPlan, INItemPlanAMExtension | InventoryID, PlanID |  |  |
| PX.Objects.AM.PrintProductionOrders | Print Production Orders | PX_Objects_AM_PrintProductionOrders, PrintProductionOrders | OrderType, ProdOrdID |  |  |
| PX.Objects.AM.ProdOperAdjusted | Production Operation Adjusted | PX_Objects_AM_ProdOperAdjusted, ProductionOperationAdjusted, ProdOperAdjusted | OperationID, OrderType, ProdOrdID | StatusIDAdjusted |  |
| PX.Objects.AM.ProdOperMatl | Production Operations & Materials | PX_Objects_AM_ProdOperMatl, ProductionOperationsMaterials, ProdOperMatl | OperationCD, OrderType, ProdOrdID |  | yes |
| PX.Objects.AM.ProductionOrderBuildCapabilityMaterial | Production Order Build Capability Material | PX_Objects_AM_ProductionOrderBuildCapabilityMaterial, ProductionOrderBuildCapabilityMaterial | ProdOrdID |  |  |
| PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation | Production Order Build Capability Material | PX_Objects_AM_ProductionOrderBuildCapabilityMaterialFirstOperation, ProductionOrderBuildCapabilityMaterial1, ProductionOrderBuildCapabilityMaterialFirstOperation | ProdOrdID |  |  |
| PX.Objects.AM.ProductionReadinessByProdItem | Production Readiness By ProdItem | PX_Objects_AM_ProductionReadinessByProdItem, ProductionReadinessByProdItem | OrderType, ProdOrdID | QtyReadyToProd |  |
| PX.Objects.AM.SchedulerMachineOperation | Machines event | PX_Objects_AM_SchedulerMachineOperation, Machinesevent, SchedulerMachineOperation | CustomerID, OrderType, ProdOrdID | OperationStart, OperationEnd, Schedulable |  |
| PX.Objects.AM.SchedulerMachineResource | Machines resources | PX_Objects_AM_SchedulerMachineResource, Machinesresources, SchedulerMachineResource | Id |  |  |
| PX.Objects.AM.SchedulerProductionOrder | Production orders resources | PX_Objects_AM_SchedulerProductionOrder, Productionordersresources, SchedulerProductionOrder | CustomerID, Id, InventoryCD, OrderType, ProdOrdID | IsLate, IsOnTime, IsEarly, ShippingDescr, Schedulable, IsEventExpanded, LackOfMaterials, Id, ChildMinStartDate, ChildMaxEndDate, ProductID, ParentID, IsProduct, IsChild |  |
| PX.Objects.AM.SchedulerWCOperation | Work centers operation | PX_Objects_AM_SchedulerWCOperation, Workcentersoperation, SchedulerWCOperation | CustomerID, InventoryCD, OrderType, ProdOrdID | ResourceId, Schedulable, OperationStart, OperationEnd, IsOnTime, IsEarly, IsLate, LackOfMaterials, ShippingDescr |  |
| PX.Objects.AM.SchedulerWCResource | Work centers resources | PX_Objects_AM_SchedulerWCResource, Workcentersresources, SchedulerWCResource | Id | Id, ShiftCode, ResourceDetails |  |
| PX.Objects.AM.SelectedProdMatl | Production Material | PX_Objects_AM_SelectedProdMatl, ProductionMaterial1, SelectedProdMatl | IsAllocated, LineID, OperationID, OrderType, ProdOrdID, SplitLineNbr | QtyAlloc, QtyShort, IsByproduct2, RequiredDate, IsVisible |  |
| PX.Objects.AM.SFK.AMClockTranUnapprovedSum | Unapproved Clock Entries Sum | PX_Objects_AM_SFK_AMClockTranUnapprovedSum, UnapprovedClockEntriesSum, AMClockTranUnapprovedSum | OperationID, OrderType, ProdOrdID |  |  |
| PX.Objects.AM.SFK.AMMTranScrap | AM Transaction | PX_Objects_AM_SFK_AMMTranScrap, AMTransaction1, AMMTranScrap | BatNbr, DocType, LineNbr |  | yes |
| PX.Objects.AM.SFK.AMMTranSplitScrap | AM Transaction Split | PX_Objects_AM_SFK_AMMTranSplitScrap, AMTransactionSplit1, AMMTranSplitScrap | BatNbr, DocType, LineNbr, SplitLineNbr |  | yes |
| PX.Objects.AM.SFK.AMSFKRecentActivity | SFK Recent Activity | PX_Objects_AM_SFK_AMSFKRecentActivity, SFKRecentActivity, AMSFKRecentActivity | RecordID |  |  |
| PX.Objects.AM.SFK.OperationsInProgressProjection | Operations In Progress View | PX_Objects_AM_SFK_OperationsInProgressProjection, OperationsInProgressView, OperationsInProgressProjection | EmployeeID, LineNbr |  |  |
| PX.Objects.AM.SFK.OperationView | Operation View | PX_Objects_AM_SFK_OperationView, OperationView | OperationID, OrderType, ProdOrdID | WcWithDescr, OperationWithDescr |  |
| PX.Objects.AM.SFK.SFKEmployeeProjection | Shop Floor Employee | PX_Objects_AM_SFK_SFKEmployeeProjection, ShopFloorEmployee, SFKEmployeeProjection | BAccountID |  |  |
| PX.Objects.AM.SFK.SFKIssueMaterialsFilter | Production Operation Materials View | PX_Objects_AM_SFK_SFKIssueMaterialsFilter, ProductionOperationMaterialsView, SFKIssueMaterialsFilter | LineID, OperationID, OrderType, ProdOrdID | Info, QtyRemaining, QtyToIssue, SelectedQtyToIssue, AddedQtyToIssue, QtyOnHand, QtyAvailableForIssue, OpenContext, IsReturn, IsAdditionalMaterial, EffectiveCostCenterID, IsByproduct |  |
| PX.Objects.AM.SFK.SFKLotSerialNbrResult | SFK Lot/Serial by Attributes | PX_Objects_AM_SFK_SFKLotSerialNbrResult, SFKLotSerialbyAttributes, SFKLotSerialNbrResult | InventoryID, LocationID, LotSerialNbr, SiteID | QtySelected |  |
| PX.Objects.AM.SFK.SFKOperationFileProjection | Operation file | PX_Objects_AM_SFK_SFKOperationFileProjection, Operationfile, SFKOperationFileProjection | FileID | ViewURL |  |
| PX.Objects.AM.SFK.SFKOperationsByWCProjection | Operations In Work Centers | PX_Objects_AM_SFK_SFKOperationsByWCProjection, OperationsInWorkCenters, SFKOperationsByWCProjection | OperationCD, OperationID, OrderType, ProdOrdID |  | yes |
| PX.Objects.AM.SFK.SFKProdOperMaterialsProjection | Production Operation Materials View | PX_Objects_AM_SFK_SFKProdOperMaterialsProjection, ProductionOperationMaterialsView1, SFKProdOperMaterialsProjection | LineID, OperationID, OrderType, ProdOrdID | IsRowDisabled, Info, QtyRemaining, BaseQtyRemaining, QtyToIssue, QtyOnHand, QtyAvailableForIssue, TotalIssuedQty |  |
| PX.Objects.AM.SFK.SFKProdOperProjection | Production Operations View | PX_Objects_AM_SFK_SFKProdOperProjection, ProductionOperationsView, SFKProdOperProjection | OperationCD, OperationID, OrderType, ProdOrdID | OperatorName, ActualLaborTime, ActiveClockStartTime, RequiresLotSerialAttributes, ShowLinkOnOrder, ShowLinkOnOper |  |
| PX.Objects.AM.SFK.SFKProductionOrderProjection | Production Order View | PX_Objects_AM_SFK_SFKProductionOrderProjection, ProductionOrderView, SFKProductionOrderProjection | OrderType, ProdOrdID |  |  |
| PX.Objects.AM.SFK.SFKSubtractSplit | SFK Subtract Lot/Serial | PX_Objects_AM_SFK_SFKSubtractSplit, SFKSubtractLotSerial, SFKSubtractSplit | BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID | ReportedQty, BaseReportedQty, QtyToSubtract, BaseQtyToSubtract |  |
| PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum | Completed Quantities Summary | PX_Objects_AM_SFK_SFKTranSplitCompletedByLotSerialSum, CompletedQuantitiesSummary, SFKTranSplitCompletedByLotSerialSum | BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID |  |  |
| PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum | Scrap Quantities Summary | PX_Objects_AM_SFK_SFKTranSplitScrapByLotSerialSum, ScrapQuantitiesSummary, SFKTranSplitScrapByLotSerialSum | BatNbr, DocType, LotSerialNbr, OperationCD, OperationID, OrderType, ProdOrdID |  |  |
| PX.Objects.AM.SubAssemblyProjection | Sub-Assembly Projection | PX_Objects_AM_SubAssemblyProjection, SubAssemblyProjection | OrderType, ProdOrdID |  |  |
| PX.Objects.AP.AP1099Box | AP 1099 Box | PX_Objects_AP_AP1099Box, AP1099Box | BoxCD, BoxNbr | OldAccountID |  |
| PX.Objects.AP.AP1099History | AP 1099 History | PX_Objects_AP_AP1099History, AP1099History | BoxNbr, BranchID, FinYear, VendorID |  |  |
| PX.Objects.AP.AP1099Year | AP 1099 Year | PX_Objects_AP_AP1099Year, AP1099Year | FinYear, OrganizationID |  |  |
| PX.Objects.AP.APAddItemSelected |  | PX_Objects_AP_APAddItemSelected | InventoryID | CuryID, CuryInfoID, CuryUnitPrice, CuryRate, CuryViewState |  |
| PX.Objects.AP.APAddress | AP Address | PX_Objects_AP_APAddress, APAddress | AddressID | OverrideAddress |  |
| PX.Objects.AP.APAdjust | Adjust | PX_Objects_AP_APAdjust, Adjust, APAdjust | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | SeparateCheck, PrintAdjgDocType, AdjdCuryID, PrintAdjdDocType, CuryRGOLAmt, DisplayRGOLAmt, NoteText, CuryOrigDocAmt, OrigDocAmt, CuryDocBal, CuryAdjustedDocBal, AdjustedDocBal, DocBal, CuryDiscBal, CuryAdjustedDiscBal, DiscBal, CuryWhTaxBal, CuryAdjustedWhTaxBal, WhTaxBal, VoidAppl, AdjType, PPDVATAdjDescription, DisplayDocType, DisplayRefNbr, DisplayDocDate, DisplayDocDesc, DisplayCuryID, DisplayCuryInfoID, DisplayFinPeriodID, DisplayStatus, DisplayCuryAmt, DisplayCuryDiscAmt, DisplayCuryPPDAmt, DisplayCuryWhTaxAmt |  |
| PX.Objects.AP.APAdjustedBalanceAtDate | APAdjustedBalanceAtDate | PX_Objects_AP_APAdjustedBalanceAtDate, APAdjustedBalanceAtDate | DocType, RefNbr, SubmissionDate | CuryLineTotal |  |
| PX.Objects.AP.APAdjustingBalanceAtDate | APAdjustingBalanceAtDate | PX_Objects_AP_APAdjustingBalanceAtDate, APAdjustingBalanceAtDate | DocType, RefNbr, SubmissionDate | CuryLineTotal |  |
| PX.Objects.AP.APAROrd | APAROrd | PX_Objects_AP_APAROrd, APAROrd | Ord |  |  |
| PX.Objects.AP.APCashRequirementsReport | Cash Requirement | PX_Objects_AP_APCashRequirementsReport, CashRequirement, APCashRequirementsReport | DocType, RefNbr | PrintDocType, CuryPayOrigDocAmt, CuryPayDocBal, CuryPayDiscBal, SignBalance |  |
| PX.Objects.AP.APContact | AP Contact | PX_Objects_AP_APContact, APContact | ContactID | OverrideContact |  |
| PX.Objects.AP.APDiscount | AP Discount | PX_Objects_AP_APDiscount, APDiscount | BAccountID, DiscountID |  |  |
| PX.Objects.AP.APDiscountLocation | AP Discount Location | PX_Objects_AP_APDiscountLocation, APDiscountLocation | DiscountID, DiscountSequenceID, VendorID |  |  |
| PX.Objects.AP.APDiscountVendor | AP Discount Vendor | PX_Objects_AP_APDiscountVendor, APDiscountVendor | DiscountID, DiscountSequenceID, VendorID |  |  |
| PX.Objects.AP.APHistory | AP History | PX_Objects_AP_APHistory, APHistory | AccountID, BranchID, FinPeriodID, SubID, VendorID | FinFlag, PtdCrAdjustments, PtdDrAdjustments, PtdPurchases, PtdPayments, PtdDiscTaken, PtdWhTax, PtdRGOL, YtdBalance, BegBalance, PtdDeposits, YtdDeposits, PtdRetainageWithheld, YtdRetainageWithheld, PtdRetainageReleased, YtdRetainageReleased |  |
| PX.Objects.AP.APHistoryByPeriod | AP History by Period | PX_Objects_AP_APHistoryByPeriod, APHistorybyPeriod | AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID |  |  |
| PX.Objects.AP.APInvoice | AP document | PX_Objects_AP_APInvoice, APdocument, APInvoice | DocType, RefNbr | PaymentInfoLocationID, ExternalTaxesImportInProgress, DrCr, LCEnabled, HasWithHoldTax, HasUseTax, DetailExtPriceTotal, CuryDetailExtPriceTotal, CuryOrderDiscTotal, OrderDiscTotal, SetWarningOnDiscount |  |
| PX.Objects.AP.APInvoiceDiscountDetail | AP Invoice Discount Detail | PX_Objects_AP_APInvoiceDiscountDetail, APInvoiceDiscountDetail | DocType, RecordID, RefNbr | IsOrigDocDiscount |  |
| PX.Objects.AP.APInvoiceExt | AP document | PX_Objects_AP_APInvoiceExt | DocType, RefNbr | LineNbr, DisplayProjectID, CuryRetainageBal, RetainageBal, RetainageReleasePct, CuryRetainageReleasedAmt, RetainageReleasedAmt, CuryRetainageUnreleasedCalcAmt, RetainageUnreleasedCalcAmt |  |
| PX.Objects.AP.APInvoiceRetainageBalanceAtDate | APInvoiceRetainageBalanceAtDate | PX_Objects_AP_APInvoiceRetainageBalanceAtDate, APInvoiceRetainageBalanceAtDate | DocType, RefNbr, SubmissionDate |  |  |
| PX.Objects.AP.APLineTax | AP Line Tax | PX_Objects_AP_APLineTax, APLineTax | LineNbr, RefNbr, TranType |  |  |
| PX.Objects.AP.APNotification | AP Notification | PX_Objects_AP_APNotification, APNotification | SetupID |  |  |
| PX.Objects.AP.APPayment | Payment | PX_Objects_AP_APPayment, Payment, APPayment | DocType, RefNbr | CuryUnappliedBal, UnappliedBal, CuryApplAmt, ApplAmt, BatchPaymentRefNbr, IsPrintingProcess, IsReleaseCheckProcess, VoidAppl, CanHaveBalance, DrCr, AmountToWords, DepositDate, CuryPOApplAmt, POApplAmt, CuryPOUnreleasedApplAmt, POUnreleasedApplAmt, CuryPOFullApplAmt, POFullApplAmt, IsRequestPrepayment, PaymentCannotbeVoidedMessage, RemittanceInformationMessage, IsExternalPayment |  |
| PX.Objects.AP.APPaymentChargeTran | AP Financial Charge Transaction | PX_Objects_AP_APPaymentChargeTran, APFinancialChargeTransaction, APPaymentChargeTran | DocType, LineNbr, RefNbr |  |  |
| PX.Objects.AP.APPayNotSelReport | Bill For Approval | PX_Objects_AP_APPayNotSelReport, BillForApproval, APPayNotSelReport | DocType, RefNbr | PrintDocType, CuryPayDocBal, CuryPayDiscBal, SignBalance |  |
| PX.Objects.AP.APPaySelReport | Bill For Payment | PX_Objects_AP_APPaySelReport, BillForPayment, APPaySelReport | DocType, RefNbr | PrintDocType, CuryPayOrigDocAmt, CuryPayDocBal, CuryPayDiscBal, SignBalance |  |
| PX.Objects.AP.APPriceWorksheet | AP Price Worksheet | PX_Objects_AP_APPriceWorksheet, APPriceWorksheet | RefNbr | NoteText |  |
| PX.Objects.AP.APPriceWorksheetDetail | AP Price Worksheet Detail | PX_Objects_AP_APPriceWorksheetDetail, APPriceWorksheetDetail | LineID, RefNbr | RestrictInventoryByAlternateID, NoteText |  |
| PX.Objects.AP.APPrintCheckDetail | Print Check Detail | PX_Objects_AP_APPrintCheckDetail, PrintCheckDetail, APPrintCheckDetail | AdjdDocType, AdjdRefNbr, AdjgDocType, AdjgRefNbr, Source | AdjgCuryID, CuryRate, CuryViewState, AdjdCuryID |  |
| PX.Objects.AP.APPrintCheckDetailWithAdjdDoc | Print Check Detail with Paid Document | PX_Objects_AP_APPrintCheckDetailWithAdjdDoc, PrintCheckDetailwithPaidDocument, APPrintCheckDetailWithAdjdDoc | AdjgDocType, AdjgRefNbr, Source | AdjdPrintDocType |  |
| PX.Objects.AP.APRegister | Document | PX_Objects_AP_APRegister, Document, APRegister | DocType, RefNbr | HiddenKey, InternalDocType, PrintDocType, DocDisc, CuryDocDisc, DocClass, ReleasedToVerify, NoteText, ReleasedOrPrebooked, WorkgroupID, OwnerID, RetainageUnpaidTotal, RetainagePaidTotal, CuryDiscountedDocTotal, DiscountedDocTotal, CuryDiscountedTaxableTotal, DiscountedTaxableTotal, CuryDiscountedPrice, DiscountedPrice, CuryRate, DeletedDatabaseRecord |  |
| PX.Objects.AP.APRegisterAccess | Vendor | PX_Objects_AP_APRegisterAccess | AcctCD |  |  |
| PX.Objects.AP.APRegisterReport | Document | PX_Objects_AP_APRegisterReport, Document1, APRegisterReport | DocType, RefNbr |  |  |
| PX.Objects.AP.APRegisterRetainage | APRegister Retainage | PX_Objects_AP_APRegisterRetainage, APRegisterRetainage | OrigDocType, OrigRefNbr | DocBalSigned, OrigDocAmtSigned |  |
| PX.Objects.AP.APRetainageInvoice | Document | PX_Objects_AP_APRetainageInvoice | DocType, RefNbr |  |  |
| PX.Objects.AP.APSetupApproval | AP Approval Preferences | PX_Objects_AP_APSetupApproval, APApprovalPreferences, APSetupApproval | ApprovalID |  |  |
| PX.Objects.AP.APTax | AP Tax Detail | PX_Objects_AP_APTax, APTaxDetail, APTax | LineNbr, RefNbr, TaxID, TranType | NonDeductibleTaxRate, CuryTaxDiscountAmt, TaxDiscountAmt |  |
| PX.Objects.AP.APTaxTran | AP Tax Details | PX_Objects_AP_APTaxTran, APTaxDetails, APTaxTran | Module, RecordID | CuryTaxableDiscountAmt, TaxableDiscountAmt, CuryDiscountedTaxableAmt, DiscountedTaxableAmt, CuryDiscountedPrice, DiscountedPrice |  |
| PX.Objects.AP.APTran | AP Transactions | PX_Objects_AP_APTran, APTransactions, APTran | LineNbr, RefNbr, TranType | SuppliedByVendorID, AllowControlAccountForModule, RequiresTerms, FreezeManualDisc, SkipDisc, ReleasedToVerify, CalculateDiscountsOnImport, NoteText, ClassID, Custodian, SignedQty, SignedCuryTranAmt, SignedTranAmt, ProjectReclassified |  |
| PX.Objects.AP.APTranPost | AP Document transaction | PX_Objects_AP_APTranPost, APDocumenttransaction, APTranPost | DocType, ID, RefNbr | IsVoidPrepayment |  |
| PX.Objects.AP.APTranPostGL | AP Document Post GL | PX_Objects_AP_APTranPostGL, APDocumentPostGL, APTranPostGL | DocType, ID, RefNbr |  |  |
| PX.Objects.AP.APTranPostGLwithLines | AP Document Post GL with Lines | PX_Objects_AP_APTranPostGLwithLines, APDocumentPostGLwithLines, APTranPostGLwithLines | DocType, Ord, RefNbr | PrintDocType, CuryDebitAPAmt, DebitAPAmt, CuryCreditAPAmt, CreditAPAmt, CuryTurnDiscAmt, TurnDiscAmt, CuryTurnWHTaxAmt, TurnWHTaxAmt, TurnRGOLAmt |  |
| PX.Objects.AP.APTranRetainage | AP Tran Retainage | PX_Objects_AP_APTranRetainage, APTranRetainage | OrigDocType, OrigLineNbr, OrigRefNbr |  |  |
| PX.Objects.AP.APVendorPrice | AP Vendor Price | PX_Objects_AP_APVendorPrice, APVendorPrice | RecordID |  |  |
| PX.Objects.AP.BalancedAPDocument | Document | PX_Objects_AP_BalancedAPDocument | DocType, RefNbr | VendorRefNbr |  |
| PX.Objects.AP.BaseAPHistoryByPeriod | Base AP History by Period | PX_Objects_AP_BaseAPHistoryByPeriod, BaseAPHistorybyPeriod | AccountID, BranchID, FinPeriodID, SubID, VendorID |  |  |
| PX.Objects.AP.CalcAPTranGLwithLinesReport | Aggrigate AP Document Post GL with Lines | PX_Objects_AP_CalcAPTranGLwithLinesReport, AggrigateAPDocumentPostGLwithLines, CalcAPTranGLwithLinesReport | AgingDate, DocType, OrigDocType, OrigRefNbr, ProjectID, RefNbr |  |  |
| PX.Objects.AP.CuryAPHistory | Currency AP History | PX_Objects_AP_CuryAPHistory, CurrencyAPHistory, CuryAPHistory | AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID | FinFlag, PtdCrAdjustments, PtdDrAdjustments, PtdPurchases, PtdPayments, PtdDiscTaken, PtdWhTax, PtdRGOL, YtdBalance, BegBalance, PtdDeposits, YtdDeposits, CuryPtdCrAdjustments, CuryPtdDrAdjustments, CuryPtdPurchases, CuryPtdPayments, CuryPtdDiscTaken, CuryPtdWhTax, CuryYtdBalance, CuryBegBalance, CuryPtdDeposits, CuryYtdDeposits, PtdRetainageWithheld, YtdRetainageWithheld, CuryPtdRetainageWithheld, CuryYtdRetainageWithheld, PtdRetainageReleased, YtdRetainageReleased, CuryPtdRetainageReleased, CuryYtdRetainageReleased |  |
| PX.Objects.AP.DAC.VendorPaymentMethod | Update Vendor Payment Methods | PX_Objects_AP_DAC_VendorPaymentMethod, UpdateVendorPaymentMethods, VendorPaymentMethod | AcctCD |  |  |
| PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice | Recognized document | PX_Objects_AP_InvoiceRecognition_DAC_APRecognizedInvoice, Recognizeddocument, APRecognizedInvoice | DocType, RefNbr | IsRedirect, RecognitionStatus, AllowFiles, AllowFilesMsg, AllowUploadFile, FileID, RecognizedDataJson, VendorTermIndex, VendorName, VendorSearchError, IsDataLoaded |  |
| PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain | Excluded Email Domains | PX_Objects_AP_InvoiceRecognition_DAC_ExcludedVendorDomain, ExcludedEmailDomains, ExcludedVendorDomain | Name |  |  |
| PX.Objects.AP.InvoiceRecognition.DAC.RecognizedRecordSplit | Recognized Document Split | PX_Objects_AP_InvoiceRecognition_DAC_RecognizedRecordSplit, RecognizedDocumentSplit, RecognizedRecordSplit | RefNbr | SplitStatus |  |
| PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping | Vendor Specified in Recognized Documents | PX_Objects_AP_InvoiceRecognition_DAC_RecognizedVendorMapping, VendorSpecifiedinRecognizedDocuments, RecognizedVendorMapping | Id |  |  |
| PX.Objects.AP.LocationAPAccountSub | Location GL Accounts | PX_Objects_AP_LocationAPAccountSub, LocationGLAccounts, LocationAPAccountSub | BAccountID, LocationID |  |  |
| PX.Objects.AP.LocationAPPaymentInfo | Location Payment Settings | PX_Objects_AP_LocationAPPaymentInfo, LocationPaymentSettings, LocationAPPaymentInfo | BAccountID, LocationID | OverrideRemitAddress, IsRemitAddressSameAsMain, OverrideRemitContact, IsRemitContactSameAsMain |  |
| PX.Objects.AP.MISC1099EFileProcessingInfoRaw | AP 1099 History | PX_Objects_AP_MISC1099EFileProcessingInfoRaw | BoxNbr, BranchID, FinYear, VendorID | PayerBAccountID |  |
| PX.Objects.AP.Overrides.APDocumentRelease.AP1099Hist | AP 1099 History | PX_Objects_AP_Overrides_APDocumentRelease_AP1099Hist | BoxNbr, BranchID, FinYear, VendorID |  |  |
| PX.Objects.AP.Overrides.APDocumentRelease.AP1099Yr | AP 1099 Year | PX_Objects_AP_Overrides_APDocumentRelease_AP1099Yr | FinYear, OrganizationID |  |  |
| PX.Objects.AP.Overrides.APDocumentRelease.APHistory2 | AP History | PX_Objects_AP_Overrides_APDocumentRelease_APHistory2 | AccountID, BranchID, FinPeriodID, SubID, VendorID |  |  |
| PX.Objects.AP.Overrides.APDocumentRelease.CuryAPHistory2 | Currency AP History | PX_Objects_AP_Overrides_APDocumentRelease_CuryAPHistory2 | AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID |  |  |
| PX.Objects.AP.Overrides.ScheduleMaint.DocumentSelection | Document | PX_Objects_AP_Overrides_ScheduleMaint_DocumentSelection | DocType, RefNbr |  |  |
| PX.Objects.AP.PendingPPDVATAdjApp | Applications Pending VAT Adjustment for Prompt Payment Discount | PX_Objects_AP_PendingPPDVATAdjApp, ApplicationsPendingVATAdjustmentforPromptPaymentDiscount, PendingPPDVATAdjApp | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | Index |  |
| PX.Objects.AP.Standalone.APQuickCheck | Cash Purchase | PX_Objects_AP_Standalone_APQuickCheck, CashPurchase, APQuickCheck | DocType, RefNbr | VoidAppl, IsPrintingProcess, IsReleaseCheckProcess, DepositDate, HasWithHoldTax, HasUseTax |  |
| PX.Objects.AP.Vendor | Vendor | PX_Objects_AP_Vendor, Vendor | AcctCD | Hold, Included |  |
| PX.Objects.AP.VendorClass | Vendor Class | PX_Objects_AP_VendorClass, VendorClass | VendorClassID | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.AP.VendorDiscountSequence | Discount Sequence | PX_Objects_AP_VendorDiscountSequence | DiscountID, DiscountSequenceID |  |  |
| PX.Objects.AP.VendorPaymentMethodDetail | Payment Type Detail | PX_Objects_AP_VendorPaymentMethodDetail, PaymentTypeDetail, VendorPaymentMethodDetail | BAccountID, DetailID, LocationID, PaymentMethodID |  |  |
| PX.Objects.AP.VendorR | Vendor | PX_Objects_AP_VendorR, Vendor1, VendorR | AcctCD |  |  |
| PX.Objects.AR.ARAddItemSelected |  | PX_Objects_AR_ARAddItemSelected | InventoryID | CuryID, CuryInfoID, CuryUnitPrice, CuryRate, CuryViewState |  |
| PX.Objects.AR.ARAddress | AR Address | PX_Objects_AR_ARAddress, ARAddress | AddressID | OverrideAddress |  |
| PX.Objects.AR.ARAdjust | Applications | PX_Objects_AR_ARAdjust, Applications, ARAdjust | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | AdjType, PrintAdjgDocType, AdjdCuryID, PrintAdjdDocType, HistoryAdjdDocType, DisplayDocType, CuryRGOLAmt, DisplayRGOLAmt, NoteText, CuryOrigDocAmt, OrigDocAmt, CuryDocBal, CuryAdjustedDocBal, AdjustedDocBal, DocBal, CuryDiscBal, CuryAdjustedDiscBal, DiscBal, CuryWOBal, CuryAdjustedWOBal, WOBal, VoidAppl, ReverseGainLoss, PPDVATAdjDescription, DisplayRefNbr, DisplayBranchID, DisplayCustomerID, DisplayDocDate, DisplayDocDesc, DisplayCuryID, DisplayFinPeriodID, DisplayStatus, DisplayCuryInfoID, DisplayAdjAmt, DisplayCuryAmt, DisplayCuryPPDAmt, DisplayCuryWOAmt, DisplayProcStatus |  |
| PX.Objects.AR.ARAdjust2 | Applications | PX_Objects_AR_ARAdjust2, Applications1, ARAdjust2 | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr |  |  |
| PX.Objects.AR.ARAdjustedBalanceAtDate | ARAdjustedBalanceAtDate | PX_Objects_AR_ARAdjustedBalanceAtDate, ARAdjustedBalanceAtDate | DocType, RefNbr, SubmissionDate | CuryLineTotal |  |
| PX.Objects.AR.ARAdjustingBalanceAtDate | ARAdjustingBalanceAtDate | PX_Objects_AR_ARAdjustingBalanceAtDate, ARAdjustingBalanceAtDate | DocType, RefNbr, SubmissionDate | CuryLineTotal |  |
| PX.Objects.AR.ARAdjustReport | Applications | PX_Objects_AR_ARAdjustReport, Applications2, ARAdjustReport | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr |  |  |
| PX.Objects.AR.ARBalances | AR Balance | PX_Objects_AR_ARBalances, ARBalance, ARBalances | BranchID, CustomerID, CustomerLocationID | DatesUpdated |  |
| PX.Objects.AR.ARBalancesByBaseCuryID | AR Balance by Base Currency | PX_Objects_AR_ARBalancesByBaseCuryID, ARBalancebyBaseCurrency, ARBalancesByBaseCuryID | BaseCuryID, CustomerID |  |  |
| PX.Objects.AR.ARBalancesSharedCredit | AR Balance Shared Credit | PX_Objects_AR_ARBalancesSharedCredit, ARBalanceSharedCredit, ARBalancesSharedCredit | SharedCreditCustomerID |  |  |
| PX.Objects.AR.ARContact | AR Contact | PX_Objects_AR_ARContact, ARContact | ContactID | OverrideContact |  |
| PX.Objects.AR.ARDiscount | AR Discount | PX_Objects_AR_ARDiscount, ARDiscount | DiscountID |  |  |
| PX.Objects.AR.ARDunningCustomerClass | AR Dunning Setup | PX_Objects_AR_ARDunningCustomerClass, ARDunningSetup, ARDunningCustomerClass | CustomerClassID, DunningLetterLevel | NoteText |  |
| PX.Objects.AR.ARDunningLetter | Dunning Letter | PX_Objects_AR_ARDunningLetter, DunningLetter, ARDunningLetter | DunningLetterID | Status, DetailsCount, CuryID, NoteText |  |
| PX.Objects.AR.ARDunningLetterDetail | Dunning Letter Detail | PX_Objects_AR_ARDunningLetterDetail, DunningLetterDetail, ARDunningLetterDetail | DocType, DunningLetterID, RefNbr | PrintDocType |  |
| PX.Objects.AR.ARDunningLetterDetailReport | Dunning Letter Detail | PX_Objects_AR_ARDunningLetterDetailReport, DunningLetterDetail1, ARDunningLetterDetailReport | DocType, DunningLetterID, RefNbr |  |  |
| PX.Objects.AR.ARDunningSetup | AR Dunning Setup | PX_Objects_AR_ARDunningSetup, ARDunningSetup1 | DunningLetterLevel | NoteText |  |
| PX.Objects.AR.ARFinCharge | AR Financial Charge | PX_Objects_AR_ARFinCharge, ARFinancialCharge, ARFinCharge | FinChargeID | LineThreshold, FixedAmount, ChargingMethod, NoteText |  |
| PX.Objects.AR.ARFinChargePercent | AR Financial Charge Percent | PX_Objects_AR_ARFinChargePercent, ARFinancialChargePercent, ARFinChargePercent | PercentID |  |  |
| PX.Objects.AR.ARFinChargeTran | AR Financial Charge Transaction | PX_Objects_AR_ARFinChargeTran, ARFinancialChargeTransaction, ARFinChargeTran | LineNbr, RefNbr, TranType |  |  |
| PX.Objects.AR.ARHistory | AR History | PX_Objects_AR_ARHistory, ARHistory | AccountID, BranchID, CustomerID, FinPeriodID, SubID | FinFlag, PtdCrAdjustments, PtdDrAdjustments, PtdSales, PtdPayments, PtdDiscounts, YtdBalance, BegBalance, PtdCOGS, PtdRGOL, PtdFinCharges, PtdDeposits, YtdDeposits, PtdItemDiscounts, PtdRetainageWithheld, YtdRetainageWithheld, PtdRetainageReleased, YtdRetainageReleased |  |
| PX.Objects.AR.ARHistoryByPeriod | AR History by Period | PX_Objects_AR_ARHistoryByPeriod, ARHistorybyPeriod | AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID |  |  |
| PX.Objects.AR.ARHistorySumForPeriod | AR History Sum For Period | PX_Objects_AR_ARHistorySumForPeriod, ARHistorySumForPeriod | FinPeriodID |  |  |
| PX.Objects.AR.ARInvoice | AR Invoice/Memo | PX_Objects_AR_ARInvoice, ARInvoiceMemo, ARInvoice | DocType, RefNbr | ExternalTaxesImportInProgress, DrCr, CuryUnreleasedPaymentAmt, UnreleasedPaymentAmt, CuryCCAuthorizedAmt, CCAuthorizedAmt, CuryPaidAmt, PaidAmt, CuryApplicationBalance, ApplicationBalance, LastFinChargeDate, LastPaymentDate, CuryWhTaxBal, WhTaxBal, Hidden, HiddenOrderType, HiddenOrderNbr, HiddenByShipment, HiddenShipmentType, HiddenShipmentNbr, ApplyPaymentWhenTaxAvailable, DeferPriceDiscountRecalculation, IsPriceAndDiscountsValid, CorrectionDocType, CorrectionRefNbr, IsUnderCancellation, IsLoadApplications |  |
| PX.Objects.AR.ARInvoiceDiscountDetail | AR Invoice Discount Detail | PX_Objects_AR_ARInvoiceDiscountDetail, ARInvoiceDiscountDetail | DocType, RecordID, RefNbr | IsOrigDocDiscount |  |
| PX.Objects.AR.ARInvoiceExt | AR Invoice/Memo | PX_Objects_AR_ARInvoiceExt | DocType, RefNbr | DisplayProjectID, CuryRetainageBal, RetainageBal, RetainageReleasePct, CuryRetainageReleasedAmt, RetainageReleasedAmt, CuryRetainageUnreleasedCalcAmt, RetainageUnreleasedCalcAmt |  |
| PX.Objects.AR.ARInvoiceRetainageBalanceAtDate | ARInvoiceRetainageBalanceAtDate | PX_Objects_AR_ARInvoiceRetainageBalanceAtDate, ARInvoiceRetainageBalanceAtDate | DocType, RefNbr, SubmissionDate |  |  |
| PX.Objects.AR.ARNotification | AR Notification | PX_Objects_AR_ARNotification, ARNotification | SetupID |  |  |
| PX.Objects.AR.ARPayment | AR Payment | PX_Objects_AR_ARPayment, ARPayment | DocType, RefNbr | NewCard, NewAccount, UpdateNextNumber, CuryUnappliedBal, UnappliedBal, CuryApplAmt, CurySOApplAmt, SOApplAmt, ApplAmt, CuryWOAmt, WOAmt, VoidAppl, CanHaveBalance, DrCr, SaveAccount, DepositDate, NeedTaskValidation, PostponeReleasedFlag, PostponeVoidedFlag, OrigReleased |  |
| PX.Objects.AR.ARPaymentChargeTran | AR Payment Charge Transaction | PX_Objects_AR_ARPaymentChargeTran, ARPaymentChargeTransaction, ARPaymentChargeTran | DocType, LineNbr, RefNbr |  |  |
| PX.Objects.AR.ARPaymentInfo | AR Payment | PX_Objects_AR_ARPaymentInfo | DocType, RefNbr |  | yes |
| PX.Objects.AR.ARPaymentTotals | AR Payment Totals | PX_Objects_AR_ARPaymentTotals, ARPaymentTotals | DocType, RefNbr |  |  |
| PX.Objects.AR.ARPriceClass | AR Price Class | PX_Objects_AR_ARPriceClass, ARPriceClass | PriceClassID | NoteText |  |
| PX.Objects.AR.ARPriceWorksheet | AR Price Worksheet | PX_Objects_AR_ARPriceWorksheet, ARPriceWorksheet | RefNbr | NoteText |  |
| PX.Objects.AR.ARPriceWorksheetDetail | AR Price Worksheet Detail | PX_Objects_AR_ARPriceWorksheetDetail, ARPriceWorksheetDetail | LineID, RefNbr | TaxCategoryID, RestrictInventoryByAlternateID |  |
| PX.Objects.AR.ARRegister | AR Document | PX_Objects_AR_ARRegister, ARDocument, ARRegister | DocType, RefNbr | InternalDocType, PrintDocType, DocDisc, CuryDocDisc, DocClass, ReleasedToVerify, FromSchedule, SelfVoidingDoc, NoteText, CuryDiscountedDocTotal, DiscountedDocTotal, CuryDiscountedTaxableTotal, DiscountedTaxableTotal, CuryDiscountedPrice, DiscountedPrice, RetainagePaidTotal, PostponePendingPaymentFlag, CuryRate, DeletedDatabaseRecord |  |
| PX.Objects.AR.ARRegisterAccess | Customer | PX_Objects_AR_ARRegisterAccess | AcctCD |  |  |
| PX.Objects.AR.ARRegisterCashSales | ARRegister Cash Sales | PX_Objects_AR_ARRegisterCashSales, ARRegisterCashSales | DocType, RefNbr |  |  |
| PX.Objects.AR.ARRegisterReport | AR Document | PX_Objects_AR_ARRegisterReport, ARDocument1, ARRegisterReport | DocType, RefNbr |  |  |
| PX.Objects.AR.ARRegisterSigned | AR Document | PX_Objects_AR_ARRegisterSigned, ARDocument2, ARRegisterSigned | DocType, RefNbr |  |  |
| PX.Objects.AR.ARRetainageInvoice | AR Document | PX_Objects_AR_ARRetainageInvoice | DocType, RefNbr |  |  |
| PX.Objects.AR.ARRetainageWithApplications | AR Retainage documents with released/paid amount | PX_Objects_AR_ARRetainageWithApplications, ARRetainagedocumentswithreleasedpaidamount, ARRetainageWithApplications | DocType, RefNbr | CuryRetainageReleasedAmt, CuryRetainagePaidAmt |  |
| PX.Objects.AR.ARSalesPerTran | AR Salesperson Commission | PX_Objects_AR_ARSalesPerTran, ARSalespersonCommission, ARSalesPerTran | AdjdDocType, AdjdRefNbr, AdjNbr, DocType, RefNbr, SalespersonID |  |  |
| PX.Objects.AR.ARSalesPrice | AR Sales Price | PX_Objects_AR_ARSalesPrice, ARSalesPrice | RecordID | PriceCode, CustomerCD, Description, TaxCategoryID, InventoryCD, NoteText, ItemStatus, ItemClassID, PriceClassID, PriceWorkgroupID, PriceManagerID |  |
| PX.Objects.AR.ARSetupApproval |  | PX_Objects_AR_ARSetupApproval | ApprovalID |  |  |
| PX.Objects.AR.ARShippingAddress | AR Address | PX_Objects_AR_ARShippingAddress, ARAddress1, ARShippingAddress | AddressID |  |  |
| PX.Objects.AR.ARShippingContact | AR Contact | PX_Objects_AR_ARShippingContact, ARContact1, ARShippingContact | ContactID |  |  |
| PX.Objects.AR.ARSPCommissionPeriod | AR Salesperson Commission Period | PX_Objects_AR_ARSPCommissionPeriod, ARSalespersonCommissionPeriod, ARSPCommissionPeriod | CommnPeriodID | StartDateUI, EndDateUI |  |
| PX.Objects.AR.ARSPCommissionYear | AR Salesperson Commission Year | PX_Objects_AR_ARSPCommissionYear, ARSalespersonCommissionYear, ARSPCommissionYear | Year |  |  |
| PX.Objects.AR.ARSPCommnHistory | AR Salesperson Commission History | PX_Objects_AR_ARSPCommnHistory, ARSalespersonCommissionHistory, ARSPCommnHistory | BranchID, CommnPeriod, CustomerID, CustomerLocationID, SalesPersonID | Type |  |
| PX.Objects.AR.ARStatement | AR Statement | PX_Objects_AR_ARStatement, ARStatement | BranchID, CuryID, CustomerID, StatementDate | Processed, NoteText, IsParentCustomerStatement |  |
| PX.Objects.AR.ARStatementCycle | Statement Cycle | PX_Objects_AR_ARStatementCycle, StatementCycle, ARStatementCycle | StatementCycleId | NextStmtDate, Bucket01LowerInclusiveBound, Bucket02LowerInclusiveBound, Bucket03LowerInclusiveBound, Bucket04LowerExclusiveBound, NoteText |  |
| PX.Objects.AR.ARStatementDetail | AR Statement Detail | PX_Objects_AR_ARStatementDetail, ARStatementDetail | CuryID, CustomerID, DocType, RefNbr, RefNoteID, StatementDate |  |  |
| PX.Objects.AR.ARStatementDetailInfo | AR Statement Detail Info | PX_Objects_AR_ARStatementDetailInfo, ARStatementDetailInfo | AdjdDocType, AdjgDocType, AdjgRefNbr, DocType, RefNbr, RefNoteID, SourceDocType, SourceRefNbr, StatementDate | PrintDocType, DocExtRefNbr, CuryOrigDocAmtSigned, OrigDocAmtSigned, CuryInitDocBalSigned, InitDocBalSigned, CuryDocBalanceSigned, DocBalanceSigned, IsOrphanApplication, IsInterCurrencyApplication, IsInterBranchApplication, IsInterCustomerApplication, IsInterStatementApplication, AdjgRefNbr, AdjdDocType, AdjdRefNbr, AdjdCuryID, AdjgCuryID, SignBalanceDelta |  |
| PX.Objects.AR.ARTax | AR Tax Detail | PX_Objects_AR_ARTax, ARTaxDetail, ARTax | LineNbr, RefNbr, TaxID, TranType | NonDeductibleTaxRate, CuryTaxDiscountAmt, TaxDiscountAmt |  |
| PX.Objects.AR.ARTaxTran | AR Tax | PX_Objects_AR_ARTaxTran, ARTax1, ARTaxTran | Module, RecordID | CuryTaxableDiscountAmt, TaxableDiscountAmt, CuryDiscountedTaxableAmt, DiscountedTaxableAmt, CuryDiscountedPrice, DiscountedPrice |  |
| PX.Objects.AR.ARTran | AR Transactions | PX_Objects_AR_ARTran, ARTransactions, ARTran | LineNbr, RefNbr, TranType | IsFree, CalculateDiscountsOnImport, CostBasisNull, CuryInventoryID, ReleasedToVerify, AllowControlAccountForModule, NoteText, RequireINUpdate, FreezeManualDisc, RequiresTerms, ItemHasResidual, UnassignedQty |  |
| PX.Objects.AR.ARTranAccrueCost |  | PX_Objects_AR_ARTranAccrueCost | LineNbr, RefNbr, TranType | IsStockItem |  |
| PX.Objects.AR.ARTranPost | AR Document transaction | PX_Objects_AR_ARTranPost, ARDocumenttransaction, ARTranPost | DocType, ID, RefNbr | IsVoidPrepayment |  |
| PX.Objects.AR.ARTranPostGL | AR Document Post GL | PX_Objects_AR_ARTranPostGL, ARDocumentPostGL, ARTranPostGL | DocType, ID, RefNbr |  |  |
| PX.Objects.AR.BalancedARDocument | AR Document | PX_Objects_AR_BalancedARDocument | DocType, RefNbr | CustomerRefNbr |  |
| PX.Objects.AR.BaseARHistoryByPeriod | Base AR History by Period | PX_Objects_AR_BaseARHistoryByPeriod, BaseARHistorybyPeriod | AccountID, BranchID, CustomerID, FinPeriodID, SubID |  |  |
| PX.Objects.AR.CCProcTran | Credit Card Processing Transaction | PX_Objects_AR_CCProcTran, CreditCardProcessingTransaction, CCProcTran | TranNbr | FundHoldExpDate, PCTranApiNumber, CommerceTranNumber, TerminalID, MaskedCardNumber, DeletedDatabaseRecord |  |
| PX.Objects.AR.CuryARHistory | Currency AR History | PX_Objects_AR_CuryARHistory, CurrencyARHistory, CuryARHistory | AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID | FinFlag, PtdCrAdjustments, PtdDrAdjustments, PtdSales, PtdPayments, PtdDiscounts, YtdBalance, BegBalance, PtdCOGS, PtdRGOL, PtdFinCharges, PtdDeposits, YtdDeposits, PtdItemDiscounts, CuryPtdCrAdjustments, CuryPtdDrAdjustments, CuryPtdSales, CuryPtdPayments, CuryPtdDiscounts, CuryPtdFinCharges, CuryYtdBalance, CuryBegBalance, CuryPtdDeposits, CuryYtdDeposits, PtdRetainageWithheld, YtdRetainageWithheld, CuryPtdRetainageWithheld, CuryYtdRetainageWithheld, PtdRetainageReleased, YtdRetainageReleased, CuryPtdRetainageReleased, CuryYtdRetainageReleased |  |
| PX.Objects.AR.Customer | Customer | PX_Objects_AR_Customer, Customer | AcctCD | OverrideBillAddress, IsBillSameAsMain, OverrideBillContact, IsBillContSameAsMain, Included, SharedCreditChild, StatementChild |  |
| PX.Objects.AR.CustomerClass | Customer Class | PX_Objects_AR_CustomerClass, CustomerClass | CustomerClassID | NoteText |  |
| PX.Objects.AR.CustomerMaster | Customer (alias) | PX_Objects_AR_CustomerMaster, Customeralias, CustomerMaster | BAccountID |  |  |
| PX.Objects.AR.CustomerPaymentMethod | Customer Payment Method | PX_Objects_AR_CustomerPaymentMethod, CustomerPaymentMethod | BAccountID, PMInstanceID | NoteText, DisplayCardType, HasBillingInfo, IsBillAddressSameAsMain, IsBillContactSameAsMain, DeletedDatabaseRecord |  |
| PX.Objects.AR.CustomerPaymentMethodDetail | Customer Payment Method Detail | PX_Objects_AR_CustomerPaymentMethodDetail, CustomerPaymentMethodDetail | DetailID, PaymentMethodID, PMInstanceID |  |  |
| PX.Objects.AR.CustomerPaymentMethodInfo | Customer Payment Method | PX_Objects_AR_CustomerPaymentMethodInfo, CustomerPaymentMethod1, CustomerPaymentMethodInfo | PMInstanceID |  |  |
| PX.Objects.AR.CustomerSharedCredit | Customer Shared Credit | PX_Objects_AR_CustomerSharedCredit, CustomerSharedCredit | BAccountID |  |  |
| PX.Objects.AR.CustSalesPeople | Customer Salespersons | PX_Objects_AR_CustSalesPeople, CustomerSalespersons, CustSalesPeople | BAccountID, LocationID, SalesPersonID |  |  |
| PX.Objects.AR.DiscountBranch | Discount for Branch | PX_Objects_AR_DiscountBranch, DiscountforBranch, DiscountBranch | BranchID, DiscountID, DiscountSequenceID |  |  |
| PX.Objects.AR.DiscountCustomer | Discount for Customer | PX_Objects_AR_DiscountCustomer, DiscountforCustomer, DiscountCustomer | CustomerID, DiscountID, DiscountSequenceID |  |  |
| PX.Objects.AR.DiscountCustomerPriceClass | Discount for Customer and Price Class | PX_Objects_AR_DiscountCustomerPriceClass, DiscountforCustomerandPriceClass, DiscountCustomerPriceClass | CustomerPriceClassID, DiscountID, DiscountSequenceID |  |  |
| PX.Objects.AR.DiscountDetail | Discount Breakpoint | PX_Objects_AR_DiscountDetail, DiscountBreakpoint, DiscountDetail | DiscountDetailsID | DiscountPercent, LastDiscountPercent, PendingDiscountPercent |  |
| PX.Objects.AR.DiscountInventoryPriceClass | Discount for Inventory and Price Class | PX_Objects_AR_DiscountInventoryPriceClass, DiscountforInventoryandPriceClass, DiscountInventoryPriceClass | DiscountID, DiscountSequenceID, InventoryPriceClassID |  |  |
| PX.Objects.AR.DiscountItem | Discount Item | PX_Objects_AR_DiscountItem, DiscountItem | DiscountID, DiscountSequenceID, InventoryID |  |  |
| PX.Objects.AR.DiscountSequence | Discount Sequence | PX_Objects_AR_DiscountSequence, DiscountSequence | DiscountID, DiscountSequenceID | ShowFreeItem, NoteText |  |
| PX.Objects.AR.DiscountSequenceDetail | Discount Sequence Detail | PX_Objects_AR_DiscountSequenceDetail, DiscountSequenceDetail | DiscountDetailsID, IsLast | DiscountPercent, PendingDiscountPercent |  |
| PX.Objects.AR.DiscountSequenceDetail2 | Discount Sequence Detail | PX_Objects_AR_DiscountSequenceDetail2 | DiscountDetailsID, IsLast |  |  |
| PX.Objects.AR.DiscountSite | Discount for Warehouse | PX_Objects_AR_DiscountSite, DiscountforWarehouse, DiscountSite | DiscountID, DiscountSequenceID, SiteID |  |  |
| PX.Objects.AR.ExternalTransaction | External Transaction | PX_Objects_AR_ExternalTransaction, ExternalTransaction | TransactionID | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.AR.FSCTNotification | Default Notification setup | PX_Objects_AR_FSCTNotification | SetupID |  |  |
| PX.Objects.AR.FSNotification | Default Notification setup | PX_Objects_AR_FSNotification | SetupID |  |  |
| PX.Objects.AR.Light.Customer | Light version of Customer DAC for Statements Printing | PX_Objects_AR_Light_Customer, LightversionofCustomerDACforStatementsPrinting, Customer1 | AcctCD | DeletedDatabaseRecord |  |
| PX.Objects.AR.Override.BAccount |  | PX_Objects_AR_Override_BAccount | BAccountID | DeletedDatabaseRecord |  |
| PX.Objects.AR.Override.Customer |  | PX_Objects_AR_Override_Customer | BAccountID | DeletedDatabaseRecord |  |
| PX.Objects.AR.Overrides.ARDocumentRelease.ARHistory2 | AR History | PX_Objects_AR_Overrides_ARDocumentRelease_ARHistory2 | AccountID, BranchID, CustomerID, FinPeriodID, SubID |  |  |
| PX.Objects.AR.Overrides.ARDocumentRelease.CuryARHistory2 | Currency AR History | PX_Objects_AR_Overrides_ARDocumentRelease_CuryARHistory2 | AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID |  |  |
| PX.Objects.AR.Overrides.ScheduleMaint.DocumentSelection | AR Document to Process | PX_Objects_AR_Overrides_ScheduleMaint_DocumentSelection, ARDocumenttoProcess, DocumentSelection | DocType, RefNbr |  |  |
| PX.Objects.AR.PendingPPDARTaxAdjApp | Pending PPD AR Tax Adj App | PX_Objects_AR_PendingPPDARTaxAdjApp, PendingPPDARTaxAdjApp | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | Index |  |
| PX.Objects.AR.SalesPerson | Sales Person | PX_Objects_AR_SalesPerson, SalesPerson | SalesPersonCD | NoteText |  |
| PX.Objects.AR.Standalone.ARCashSale | Cash Sale | PX_Objects_AR_Standalone_ARCashSale, CashSale, ARCashSale | DocType, RefNbr | DetailExtLineTotal, CuryDetailExtPriceTotal, DepositDate, VoidAppl |  |
| PX.Objects.CA.ACHPlugInParameter | ACHPlugInParameter | PX_Objects_CA_ACHPlugInParameter, ACHPlugInParameter | ParameterID, PaymentMethodID, PlugInTypeName | DetailMapping, ExportScenarioMapping, DataElementSize |  |
| PX.Objects.CA.ACHPlugInParameter2 | ACHPlugInParameter | PX_Objects_CA_ACHPlugInParameter2, ACHPlugInParameter1, ACHPlugInParameter2 | ParameterID, PaymentMethodID, PlugInTypeName |  |  |
| PX.Objects.CA.BankStatementHelpers.CATranExt | CA Transaction | PX_Objects_CA_BankStatementHelpers_CATranExt | TranID |  | yes |
| PX.Objects.CA.CAAdj | Cash Transactions | PX_Objects_CA_CAAdj, CashTransactions, CAAdj | AdjRefNbr, AdjTranType | ReverseCount, WorkgroupID, OwnerID, NoteText, HasWithHoldTax, HasUseTax, DepositDate, FormCaptionDescription, CuryRate, DeletedDatabaseRecord |  |
| PX.Objects.CA.CABankChargeTax | CABankChargeTax | PX_Objects_CA_CABankChargeTax, CABankChargeTax | BankTranID, LineNbr, MatchType, TaxID |  |  |
| PX.Objects.CA.CABankFeed | Bank Feed | PX_Objects_CA_CABankFeed, BankFeed, CABankFeed | BankFeedID | IsTestFeed, StatementImportSource, NoteText |  |
| PX.Objects.CA.CABankFeedAccountMapping | Bank Feed Account Mapping | PX_Objects_CA_CABankFeedAccountMapping, BankFeedAccountMapping, CABankFeedAccountMapping | BankFeedAccountMapID |  |  |
| PX.Objects.CA.CABankFeedCorpCard | Bank Feed Corporate Cards | PX_Objects_CA_CABankFeedCorpCard, BankFeedCorporateCards, CABankFeedCorpCard | BankFeedID, LineNbr | CardNumber, CardName, EmployeeName, NoteText |  |
| PX.Objects.CA.CABankFeedDetail | Bank Feed Detail | PX_Objects_CA_CABankFeedDetail, BankFeedDetail, CABankFeedDetail | BankFeedID, LineNbr | ImportStartDate, NoteText |  |
| PX.Objects.CA.CABankFeedExpense | Bank Feed Expense Items | PX_Objects_CA_CABankFeedExpense, BankFeedExpenseItems, CABankFeedExpense | BankFeedID, LineNbr | NoteText |  |
| PX.Objects.CA.CABankFeedFieldMapping | CABankFeedFieldMapping | PX_Objects_CA_CABankFeedFieldMapping, CABankFeedFieldMapping | BankFeedID, LineNbr | NoteText |  |
| PX.Objects.CA.CABankTax | CA Bank Tax Detail | PX_Objects_CA_CABankTax, CABankTaxDetail, CABankTax | BankTranID, BankTranType, LineNbr, TaxID |  |  |
| PX.Objects.CA.CABankTaxTran | CA Bank Tax Transaction | PX_Objects_CA_CABankTaxTran, CABankTaxTransaction, CABankTaxTran | BankTranID, BankTranType, Module, RecordID, TaxID |  |  |
| PX.Objects.CA.CABankTaxTranMatch | CABankTaxTranMatch | PX_Objects_CA_CABankTaxTranMatch, CABankTaxTranMatch | BankTranID, BankTranType, Module, RecordID, TaxID |  |  |
| PX.Objects.CA.CABankTran | Bank Transaction | PX_Objects_CA_CABankTran, BankTransaction, CABankTran | TranID | RuleApplied, ApplyRuleEnabled, MatchedToExisting, MatchedToInvoice, MatchedToExpenseReceipt, Status, CuryDebitAmt, CuryCreditAmt, CuryTotalAmt, CuryTotalAmtCopy, CuryTotalAmtDisplay, CuryUnappliedBal, CuryApplAmtMatchToInvoice, CuryApplAmtMatchToPayment, CuryUnappliedBalMatch, CuryUnappliedBalMatchToInvoice, CuryUnappliedBalMatchToPayment, DocType, PayeeBAccountIDCopy, PaymentMethodIDCopy, PMInstanceIDCopy, CountMatches, CountInvoiceMatches, CountExpenseReceiptDetailMatches, MatchStatsInfo, AcctName, PayeeBAccountID1, PayeeLocationID1, PaymentMethodID1, InvoiceInfo1, EntryTypeID1, OrigModule1, CuryWOAmt, WOAmt, SortOrder, NoteText, Cleared, ClearDate, CuryRate |  |
| PX.Objects.CA.CABankTranAdjustment | Bank Transaction Adjustment | PX_Objects_CA_CABankTranAdjustment, BankTransactionAdjustment, CABankTranAdjustment | AdjNbr, TranID | SeparateCheck, AdjdCuryID, PrintAdjdDocType, CuryDocBal, CuryAdjustedDocBal, DocBal, CuryDiscBal, CuryAdjustedDiscBal, DiscBal, CuryWhTaxBal, CuryAdjustedWhTaxBal, WhTaxBal, CuryAdjdWOAmt, AdjgWOAmt, NoteText |  |
| PX.Objects.CA.CABankTranBAccountMapping | Bank Transaction Payee Business Account Mapping | PX_Objects_CA_CABankTranBAccountMapping, BankTransactionPayeeBusinessAccountMapping, CABankTranBAccountMapping | MappingID |  |  |
| PX.Objects.CA.CABankTranDetail | CA Bank Transaction Detail | PX_Objects_CA_CABankTranDetail, CABankTransactionDetail, CABankTranDetail | BankTranID, BankTranType, LineNbr | NoteText |  |
| PX.Objects.CA.CABankTranHeader | Bank Statement | PX_Objects_CA_CABankTranHeader, BankStatement, CABankTranHeader | CashAccountID, RefNbr, TranType | CuryDetailsEndBalance, NoteText |  |
| PX.Objects.CA.CABankTranMatch | Bank Transaction Match | PX_Objects_CA_CABankTranMatch, BankTransactionMatch, CABankTranMatch | LineNbr, MatchType, TranID |  |  |
| PX.Objects.CA.CABankTranMatch2 | Bank Transaction Match | PX_Objects_CA_CABankTranMatch2 | LineNbr, MatchType, TranID |  |  |
| PX.Objects.CA.CABankTranRule | CA Bank Transactions Rule | PX_Objects_CA_CABankTranRule, CABankTransactionsRule, CABankTranRule | RuleID | CuryMinTranAmt, NoteText |  |
| PX.Objects.CA.CABankTranRulePopup | CA Bank Transactions Rule | PX_Objects_CA_CABankTranRulePopup | RuleID |  |  |
| PX.Objects.CA.CABatch | CA Batch | PX_Objects_CA_CABatch, CABatch | BatchNbr | Status, NoteText, Total, FormCaptionDescription, DeletedDatabaseRecord |  |
| PX.Objects.CA.CABatchDetail | CA Batch Details | PX_Objects_CA_CABatchDetail, CABatchDetails, CABatchDetail | BatchNbr, OrigDocType, OrigLineNbr, OrigModule, OrigRefNbr |  |  |
| PX.Objects.CA.CABatchDetailOrigDocAggregate | Aggregated CA Batch Details | PX_Objects_CA_CABatchDetailOrigDocAggregate, AggregatedCABatchDetails, CABatchDetailOrigDocAggregate | BatchNbr, OrigDocType, OrigLineNbr, OrigModule, OrigRefNbr |  |  |
| PX.Objects.CA.CACorpCard | Corporate Card | PX_Objects_CA_CACorpCard, CorporateCard, CACorpCard | CorpCardCD | NoteText |  |
| PX.Objects.CA.CADailySummary | CA Daily Summary | PX_Objects_CA_CADailySummary, CADailySummary | CashAccountID, TranDate |  |  |
| PX.Objects.CA.CADeposit | CA Deposit | PX_Objects_CA_CADeposit, CADeposit | RefNbr, TranType | NoteText, ChargeMult, FormCaptionDescription, IsManual, AdjustmentCounter, CuryRate, DeletedDatabaseRecord |  |
| PX.Objects.CA.CADepositCharge | CA Deposit Charge | PX_Objects_CA_CADepositCharge, CADepositCharge | LineNbr, RefNbr, TranType |  |  |
| PX.Objects.CA.CADepositDetail | CA Deposit Detail | PX_Objects_CA_CADepositDetail, CADepositDetail | LineNbr, RefNbr, TranType | ChargeEntryTypeID, SourceDrCr, CuryChargeTotal, ChargeTotal, CuryConsolidateChargeTotal, ConsolidateChargeTotal, DepositAfter, CuryOrigAmtSigned, OrigAmtSigned |  |
| PX.Objects.CA.CAEntryType | CA Entry Type | PX_Objects_CA_CAEntryType, CAEntryType | EntryTypeId | DeletedDatabaseRecord |  |
| PX.Objects.CA.CAExpense | CAExpense | PX_Objects_CA_CAExpense, CAExpense | LineNbr, RefNbr | AdjCuryRate, HasWithHoldTax, HasUseTax, NoteText |  |
| PX.Objects.CA.CAExpenseTax | CAExpenseTax | PX_Objects_CA_CAExpenseTax, CAExpenseTax | LineNbr, RefNbr, TaxID, TranType | NonDeductibleTaxRate |  |
| PX.Objects.CA.CAExpenseTaxTran | CAExpenseTaxTran | PX_Objects_CA_CAExpenseTaxTran, CAExpenseTaxTran | Module, RecordID |  |  |
| PX.Objects.CA.CARecon | Reconciliation Statement | PX_Objects_CA_CARecon, ReconciliationStatement, CARecon | CashAccountID, ReconNbr | LoadDocumentsTill, IsUserLoadDocumentsTill, CuryReconciledTurnover, ReconciledTurnover, WorkgroupID, OwnerID, NoteText, CuryRate, CuryViewState, DeletedDatabaseRecord |  |
| PX.Objects.CA.CAReconByPeriod | Reconciliation by Period | PX_Objects_CA_CAReconByPeriod, ReconciliationbyPeriod, CAReconByPeriod | CashAccountID, FinPeriodID |  |  |
| PX.Objects.CA.CASetupApproval | CA Approval Preferences | PX_Objects_CA_CASetupApproval, CAApprovalPreferences, CASetupApproval | ApprovalID |  |  |
| PX.Objects.CA.CashAccount | Cash Account | PX_Objects_CA_CashAccount, CashAccount | CashAccountCD | AllowOverrideCury, AllowOverrideRate, PTInstancesAllowed, AcctSettingsAllowed, RefNbrComparePercent, DateComparePercent, PayeeComparePercent, ExpenseReceiptRefNbrComparePercent, ExpenseReceiptDateComparePercent, ExpenseReceiptAmountComparePercent, RatioInRelevanceCalculationLabel, InvoiceRefNbrComparePercent, InvoiceDateComparePercent, InvoicePayeeComparePercent, NoteText |  |
| PX.Objects.CA.CashAccountCheck | Cash Account Check | PX_Objects_CA_CashAccountCheck, CashAccountCheck | CashAccountID, CheckNbr, PaymentMethodID |  |  |
| PX.Objects.CA.CashAccountDeposit | Clearing Account | PX_Objects_CA_CashAccountDeposit, ClearingAccount, CashAccountDeposit | CashAccountID, DepositAcctID, PaymentMethodID |  |  |
| PX.Objects.CA.CashAccountETDetail | Entry Type for Cash Account | PX_Objects_CA_CashAccountETDetail, EntryTypeforCashAccount, CashAccountETDetail | CashAccountID, EntryTypeID |  |  |
| PX.Objects.CA.CashAccountPaymentMethodDetail | Remittance Settings | PX_Objects_CA_CashAccountPaymentMethodDetail, RemittanceSettings, CashAccountPaymentMethodDetail | CashAccountID, DetailID, PaymentMethodID |  |  |
| PX.Objects.CA.CashForecastTran | Cash Transactions | PX_Objects_CA_CashForecastTran, CashTransactions1, CashForecastTran | TranID | NoteText |  |
| PX.Objects.CA.CASplit | CA Transaction Details | PX_Objects_CA_CASplit, CATransactionDetails, CASplit | AdjRefNbr, AdjTranType, LineNbr | ReclassificationProhibited, NoteText |  |
| PX.Objects.CA.CASummaryOnReconDate | Aggregated CA Daily Summary until Reconciliation Date | PX_Objects_CA_CASummaryOnReconDate, AggregatedCADailySummaryuntilReconciliationDate, CASummaryOnReconDate | CashAccountID, ReconNbr |  |  |
| PX.Objects.CA.CATax | CA Tax Detail | PX_Objects_CA_CATax, CATaxDetail, CATax | AdjRefNbr, AdjTranType, LineNbr, TaxID | NonDeductibleTaxRate |  |
| PX.Objects.CA.CATaxTran | CA Tax Transaction | PX_Objects_CA_CATaxTran, CATaxTransaction, CATaxTran | Module, RecordID |  |  |
| PX.Objects.CA.CATran | CA Transaction | PX_Objects_CA_CATran, CATransaction, CATran | TranID | BegBal, EndBal, DayDesc, ReferenceName, Status, CuryDebitAmt, CuryCreditAmt, CuryClearedDebitAmt, CuryClearedCreditAmt, NoteText |  |
| PX.Objects.CA.CATransfer | Transfer | PX_Objects_CA_CATransfer, Transfer, CATransfer | TransferNbr | ReverseCount, NoteText, CashBalanceIn, CashBalanceOut, InGLBalance, OutGLBalance, BaseCuryID, TotalExpenses, CuryRate, OutCuryRate, DeletedDatabaseRecord |  |
| PX.Objects.CA.CCBatch | CCBatch | PX_Objects_CA_CCBatch, CCBatch | BatchID | SettlementTime, ExcludedCount, Description, NoteText |  |
| PX.Objects.CA.CCBatchAdjustment | CCBatchAdjustment | PX_Objects_CA_CCBatchAdjustment, CCBatchAdjustment | BatchID, ExternalID | AdjustmentTime |  |
| PX.Objects.CA.CCBatchStatistics | CCBatchStatistics | PX_Objects_CA_CCBatchStatistics, CCBatchStatistics | BatchID, ProcCenterCardTypeCode | DisplayCardType, NoteText |  |
| PX.Objects.CA.CCBatchTransaction | CCBatchTransaction | PX_Objects_CA_CCBatchTransaction, CCBatchTransaction | BatchID, PCTranNumber, SettlementStatus | SelectedToHide, SelectedToUnhide, DisplayCardType, NoteText |  |
| PX.Objects.CA.CCProcessingCenter | Processing Center | PX_Objects_CA_CCProcessingCenter, ProcessingCenter, CCProcessingCenter | ProcessingCenterID | NeedsExpDateUpdate, LastSettlementDate, NoteText |  |
| PX.Objects.CA.CCProcessingCenterDetail | Credit Card Processing Center Detail | PX_Objects_CA_CCProcessingCenterDetail, CreditCardProcessingCenterDetail, CCProcessingCenterDetail | DetailID, ProcessingCenterID |  |  |
| PX.Objects.CA.CCProcessingCenterFeeType | Fee Type for Credit Card Processing Center | PX_Objects_CA_CCProcessingCenterFeeType, FeeTypeforCreditCardProcessingCenter, CCProcessingCenterFeeType | EntryTypeID, FeeType, ProcessingCenterID |  |  |
| PX.Objects.CA.CCProcessingCenterPmntMethod | Payment Method for Credit Card Processing Center | PX_Objects_CA_CCProcessingCenterPmntMethod, PaymentMethodforCreditCardProcessingCenter, CCProcessingCenterPmntMethod | PaymentMethodID, ProcessingCenterID |  |  |
| PX.Objects.CA.CCProcessingCenterPmntMethodBranch | Overrides By Branch | PX_Objects_CA_CCProcessingCenterPmntMethodBranch, OverridesByBranch, CCProcessingCenterPmntMethodBranch | BranchID, PaymentMethodID |  |  |
| PX.Objects.CA.CCSynchronizeCard |  | PX_Objects_CA_CCSynchronizeCard | RecordID | NoteText |  |
| PX.Objects.CA.CustomerProcessingCenterID | Customer Processing Center ID | PX_Objects_CA_CustomerProcessingCenterID, CustomerProcessingCenterID | InstanceID |  |  |
| PX.Objects.CA.Light.APAdjust |  | PX_Objects_CA_Light_APAdjust | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr |  |  |
| PX.Objects.CA.Light.APInvoice |  | PX_Objects_CA_Light_APInvoice | DocType, RefNbr | DrCr |  |
| PX.Objects.CA.Light.APPayment | Document | PX_Objects_CA_Light_APPayment | DocType, RefNbr |  |  |
| PX.Objects.CA.Light.APRegister |  | PX_Objects_CA_Light_APRegister | DocType, RefNbr | DeletedDatabaseRecord |  |
| PX.Objects.CA.Light.ARAdjust |  | PX_Objects_CA_Light_ARAdjust | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr |  |  |
| PX.Objects.CA.Light.ARInvoice |  | PX_Objects_CA_Light_ARInvoice | DocType, RefNbr | DrCr |  |
| PX.Objects.CA.Light.ARPayment | AR Document | PX_Objects_CA_Light_ARPayment | DocType, RefNbr |  |  |
| PX.Objects.CA.Light.ARRegister |  | PX_Objects_CA_Light_ARRegister | DocType, RefNbr | DeletedDatabaseRecord |  |
| PX.Objects.CA.Light.BAccount |  | PX_Objects_CA_Light_BAccount | AcctCD | DeletedDatabaseRecord |  |
| PX.Objects.CA.Light.CABankTranAdjustment |  | PX_Objects_CA_Light_CABankTranAdjustment | AdjNbr, TranID |  |  |
| PX.Objects.CA.Light.Customer | Customer | PX_Objects_CA_Light_Customer, Customer2 | AcctCD |  |  |
| PX.Objects.CA.Light.CustomerMaster | Customer | PX_Objects_CA_Light_CustomerMaster | AcctCD |  |  |
| PX.Objects.CA.Light.Location | Location | PX_Objects_CA_Light_Location, Location2 | BAccountID, LocationCD |  |  |
| PX.Objects.CA.Light.Vendor | Customer | PX_Objects_CA_Light_Vendor, Customer3, Vendor2 | AcctCD |  |  |
| PX.Objects.CA.PaymentMethod | Payment Method | PX_Objects_CA_PaymentMethod, PaymentMethod | PaymentMethodID | NoteText, IsAccountNumberRequired, PrintOrExport, HasProcessingCenters, IsUsingPlugin, ExternalPaymentProcessorType, NeedAccountFilter, DeletedDatabaseRecord |  |
| PX.Objects.CA.PaymentMethodAccount | Payment Method for Cash Account | PX_Objects_CA_PaymentMethodAccount, PaymentMethodforCashAccount, PaymentMethodAccount | CashAccountID, PaymentMethodID |  |  |
| PX.Objects.CA.PaymentMethodDetail | Payment Method Detail | PX_Objects_CA_PaymentMethodDetail, PaymentMethodDetail | DetailID, PaymentMethodID, UseFor | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.CC.CCPayLink | Payment Link | PX_Objects_CC_CCPayLink, PaymentLink, CCPayLink | PayLinkID | NoteText |  |
| PX.Objects.CC.CCProcessingCenterBranch | Payment Creation Settings | PX_Objects_CC_CCProcessingCenterBranch, PaymentCreationSettings, CCProcessingCenterBranch | BranchID, ProcessingCenterID |  |  |
| PX.Objects.CC.CCProcessingCenterTerminal | Processing Center Terminal | PX_Objects_CC_CCProcessingCenterTerminal, ProcessingCenterTerminal, CCProcessingCenterTerminal | ProcessingCenterID, TerminalID |  |  |
| PX.Objects.CC.DefaultTerminal | Default POS Terminal | PX_Objects_CC_DefaultTerminal, DefaultPOSTerminal, DefaultTerminal | BranchID, ProcessingCenterID, UserID |  |  |
| PX.Objects.CM.APHistoryLastRevaluation |  | PX_Objects_CM_APHistoryLastRevaluation | AccountID, BranchID, CuryID, SubID, VendorID |  |  |
| PX.Objects.CM.ARHistoryLastRevaluation |  | PX_Objects_CM_ARHistoryLastRevaluation | AccountID, BranchID, CuryID, CustomerID, SubID |  |  |
| PX.Objects.CM.Currency | Currency | PX_Objects_CM_Currency, Currency | CuryID | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.CM.CurrencyInfo | Currency Info | PX_Objects_CM_CurrencyInfo, CurrencyInfo | CuryInfoID | DisplayCuryID, SampleCuryRate, SampleRecipRate, CuryPrecision, BasePrecision |  |
| PX.Objects.CM.CurrencyList | Currency | PX_Objects_CM_CurrencyList, Currency1, CurrencyList | CuryID | DeletedDatabaseRecord |  |
| PX.Objects.CM.CurrencyRate | Currency Rate | PX_Objects_CM_CurrencyRate, CurrencyRate | CuryRateID | NoteText |  |
| PX.Objects.CM.CurrencyRate2 | Effective Currency Rate | PX_Objects_CM_CurrencyRate2, EffectiveCurrencyRate, CurrencyRate2 | CuryRateID |  |  |
| PX.Objects.CM.CurrencyRateByDate | Currency Rate by Date | PX_Objects_CM_CurrencyRateByDate, CurrencyRatebyDate | CuryRateID |  |  |
| PX.Objects.CM.CurrencyRateByDateForVendor | Currency Rate by Date | PX_Objects_CM_CurrencyRateByDateForVendor, CurrencyRatebyDate1, CurrencyRateByDateForVendor | CuryRateID |  |  |
| PX.Objects.CM.CurrencyRateType | Currency Rate Type | PX_Objects_CM_CurrencyRateType, CurrencyRateType | CuryRateTypeID | DeletedDatabaseRecord |  |
| PX.Objects.CM.Extensions.Currency | Currency | PX_Objects_CM_Extensions_Currency, Currency2 | CuryID | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.CM.Extensions.CurrencyInfo | Currency Info | PX_Objects_CM_Extensions_CurrencyInfo, CurrencyInfo1 | CuryInfoID | DisplayCuryID, SampleCuryRate, SampleRecipRate, CuryPrecision, BasePrecision |  |
| PX.Objects.CM.Extensions.CurrencyList | Currency | PX_Objects_CM_Extensions_CurrencyList, Currency3, CurrencyList1 | CuryID | DeletedDatabaseRecord |  |
| PX.Objects.CM.Extensions.CurrencyRate | Currency Rate | PX_Objects_CM_Extensions_CurrencyRate, CurrencyRate1 | CuryRateID |  |  |
| PX.Objects.CM.Extensions.CurrencyRateType | Currency Rate Type | PX_Objects_CM_Extensions_CurrencyRateType, CurrencyRateType1 | CuryRateTypeID | DeletedDatabaseRecord |  |
| PX.Objects.CM.RefreshRate |  | PX_Objects_CM_RefreshRate | CuryRateType, FromCuryID | OnlineRateAdjustment |  |
| PX.Objects.CM.RevaluedAPHistory | Revalued AP History | PX_Objects_CM_RevaluedAPHistory, RevaluedAPHistory | AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID |  | yes |
| PX.Objects.CM.RevaluedARHistory | Revalued AR History | PX_Objects_CM_RevaluedARHistory, RevaluedARHistory | AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID |  | yes |
| PX.Objects.CM.RevaluedGLHistory | GL History | PX_Objects_CM_RevaluedGLHistory | AccountID, BranchID, FinPeriodID, LedgerID, SubID |  | yes |
| PX.Objects.CM.TranslationHistory | Translation History | PX_Objects_CM_TranslationHistory, TranslationHistory | ReferenceNbr | NoteText |  |
| PX.Objects.CM.TranslationHistoryDetails | Translation History Detail | PX_Objects_CM_TranslationHistoryDetails, TranslationHistoryDetail, TranslationHistoryDetails | AccountID, BranchID, LineType, ReferenceNbr, SubID | NoteText |  |
| PX.Objects.CM.TranslDef | Translation Definition | PX_Objects_CM_TranslDef, TranslationDefinition, TranslDef | TranslDefId | NoteText, SourceCuryID, DestCuryID |  |
| PX.Objects.CM.TranslDefDet | Translation Definition Detail | PX_Objects_CM_TranslDefDet, TranslationDefinitionDetail, TranslDefDet | LineNbr, TranslDefId | NoteText |  |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceAnswer | Compliance Answer | PX_Objects_CN_Compliance_CL_DAC_ComplianceAnswer, ComplianceAnswer | AttributeID, RefNoteID |  |  |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute | Compliance Attribute | PX_Objects_CN_Compliance_CL_DAC_ComplianceAttribute, ComplianceAttribute | AttributeId | NoteText |  |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType | Compliance Attribute Type | PX_Objects_CN_Compliance_CL_DAC_ComplianceAttributeType, ComplianceAttributeType | ComplianceAttributeTypeID |  |  |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument | Compliance Document | PX_Objects_CN_Compliance_CL_DAC_ComplianceDocument, ComplianceDocument | ComplianceDocumentID | IsExpired, NoteText, SkipInit, NewClassID |  |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill | Compliance Document Bill Reference | PX_Objects_CN_Compliance_CL_DAC_ComplianceDocumentBill, ComplianceDocumentBillReference, ComplianceDocumentBill | ComplianceDocumentID, DocType, LineNbr, RefNbr | NoteText |  |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference | Compliance Document Reference | PX_Objects_CN_Compliance_CL_DAC_ComplianceDocumentReference, ComplianceDocumentReference | ComplianceDocumentReferenceId | NoteText |  |
| PX.Objects.CN.Compliance.CL.DAC.ComplianceNotification | Compliance Notification | PX_Objects_CN_Compliance_CL_DAC_ComplianceNotification, ComplianceNotification | SetupID |  |  |
| PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient | Lien Waiver Recipient | PX_Objects_CN_Compliance_PM_DAC_LienWaiverRecipient, LienWaiverRecipient | ProjectId, VendorClassId | NoteText |  |
| PX.Objects.CN.CRM.CR.DAC.MultipleQuote | Multiple Customers | PX_Objects_CN_CRM_CR_DAC_MultipleQuote, MultipleCustomers, MultipleQuote | MultipleQuoteID | Tstamp, CreatedByScreenId, CreatedDateTime, LastModifiedByScreenId, LastModifiedDateTime, NoteID, NoteText, GrossMarginAbsolute, GrossMarginPercentage, FinalGrossMarginAbsolute, FinalGrossMarginPercentage |  |
| PX.Objects.CN.JointChecks.JointPayee | Joint Payee | PX_Objects_CN_JointChecks_JointPayee, JointPayee | JointPayeeId | BillLineAmount, CanDelete, NoteText |  |
| PX.Objects.CN.JointChecks.JointPayeePayment | Joint Payee Payment | PX_Objects_CN_JointChecks_JointPayeePayment, JointPayeePayment | JointPayeePaymentId | BillLineNumber, NoteText |  |
| PX.Objects.CN.PMReportProject | PM Report Project | PX_Objects_CN_PMReportProject, PMReportProject | BaseType, ContractCD |  |  |
| PX.Objects.CN.PMSubAuditReportChangeOrderLine | PM Subcontract Audit Report Change Order Line | PX_Objects_CN_PMSubAuditReportChangeOrderLine, PMSubcontractAuditReportChangeOrderLine, PMSubAuditReportChangeOrderLine | LineNbr, OrderNbr |  |  |
| PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract | PM Subcontract Audit Report Retainage Not Linked to Subcontract | PX_Objects_CN_PMSubAuditReportRetainageNotLinkedToSubcontract, PMSubcontractAuditReportRetainageNotLinkedtoSubcontract, PMSubAuditReportRetainageNotLinkedToSubcontract | DocType, RefNbr |  |  |
| PX.Objects.CN.PMSubAuditReportUnappliedPrepayments | PM Subcontract Audit Report Unapplied Prepayments | PX_Objects_CN_PMSubAuditReportUnappliedPrepayments, PMSubcontractAuditReportUnappliedPrepayments, PMSubAuditReportUnappliedPrepayments | PONbr, RefNbr |  |  |
| PX.Objects.CN.PMWipBudget | PM WIP Budget | PX_Objects_CN_PMWipBudget, PMWIPBudget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID |  |  |
| PX.Objects.CN.PMWipChangeOrder | PM WIP Change Order | PX_Objects_CN_PMWipChangeOrder, PMWIPChangeOrder | RefNbr |  |  |
| PX.Objects.CN.PMWipChangeOrderBudget | PM WIP Change Order Budget | PX_Objects_CN_PMWipChangeOrderBudget, PMWIPChangeOrderBudget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID, RefNbr |  |  |
| PX.Objects.CN.PMWipChangeOrderLine | PM WIP Change Order Line | PX_Objects_CN_PMWipChangeOrderLine, PMWIPChangeOrderLine | LineNbr, RefNbr |  |  |
| PX.Objects.CN.PMWipCommitment | PM WIP Commitment | PX_Objects_CN_PMWipCommitment, PMWIPCommitment | CommitmentID |  |  |
| PX.Objects.CN.PMWipCostProjection | PM WIP Cost Projection | PX_Objects_CN_PMWipCostProjection, PMWIPCostProjection | ProjectID |  |  |
| PX.Objects.CN.PMWipCostProjectionBudget | PM WIP Cost Projection Budget | PX_Objects_CN_PMWipCostProjectionBudget, PMWIPCostProjectionBudget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID |  |  |
| PX.Objects.CN.PMWipForecastHistory | PM WIP Forecast History | PX_Objects_CN_PMWipForecastHistory, PMWIPForecastHistory | AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID |  |  |
| PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField | ComplianceRequirementField | PX_Objects_CN_Requirements_ComplianceRequirementFields_ComplianceRequirementField, ComplianceRequirementField | FieldID, RequirementID |  |  |
| PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance | Vendor Document Requirement Compliance | PX_Objects_CN_Requirements_DAC_VendorDocumentReqCompliance, VendorDocumentRequirementCompliance, VendorDocumentReqCompliance | ReqComplianceID | ComplianceDocumentDisplayName, ExpirationWarningText, ComplianceLimitText, IsExpired, StatusWithExpiration, ProjectCD, RelatedTo |  |
| PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow | Vendor Document Requirement Condition Row | PX_Objects_CN_Requirements_DAC_VendorDocumentReqConditionRow, VendorDocumentRequirementConditionRow, VendorDocumentReqConditionRow | LineNbr, RequirementID | ConditionName |  |
| PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement | Vendor Document Requirement | PX_Objects_CN_Requirements_DAC_VendorDocumentRequirement, VendorDocumentRequirement | RequirementID | NoteText |  |
| PX.Objects.CN.Subcontracts.SC.DAC.Subcontract | Subcontract | PX_Objects_CN_Subcontracts_SC_DAC_Subcontract, Subcontract | OrderNbr, OrderType |  |  |
| PX.Objects.CN.Subcontracts.SC.DAC.SubcontractInventoryItem | Subcontract Inventory Item | PX_Objects_CN_Subcontracts_SC_DAC_SubcontractInventoryItem, SubcontractInventoryItem | InventoryCD |  |  |
| PX.Objects.CN.Subcontracts.SC.DAC.SubcontractNotification | Subcontract Notification | PX_Objects_CN_Subcontracts_SC_DAC_SubcontractNotification, SubcontractNotification | SetupID |  |  |
| PX.Objects.Common.DAC.DropShipLink | Drop-Ship Link | PX_Objects_Common_DAC_DropShipLink, DropShipLink | POLineNbr, POOrderNbr, POOrderType, SOLineNbr, SOOrderNbr, SOOrderType |  |  |
| PX.Objects.Common.DAC.ReportParameters.BAccountNoMask |  | PX_Objects_Common_DAC_ReportParameters_BAccountNoMask | AcctCD, BAccountID |  |  |
| PX.Objects.CR.Address | Address | PX_Objects_CR_Address, Address | AddressID | NoteText |  |
| PX.Objects.CR.BAccount | Business Account | PX_Objects_CR_BAccount, BusinessAccount, BAccount | AcctCD | NoteText, NotePopupText, ViewInCrm, HSEntityTypeID, EntityTypeID, Secured, DeletedDatabaseRecord |  |
| PX.Objects.CR.BAccount2 | Business Account | PX_Objects_CR_BAccount2 | AcctCD |  |  |
| PX.Objects.CR.BAccountParent | Parent Business Account | PX_Objects_CR_BAccountParent, ParentBusinessAccount, BAccountParent | AcctCD |  |  |
| PX.Objects.CR.Building |  | PX_Objects_CR_Building | BranchID, BuildingCD |  |  |
| PX.Objects.CR.Contact | Contact | PX_Objects_CR_Contact, Contact | ContactID | IsAddressSameAsMain, OverrideAddress, IsPrimary, NoteText, IsNotEmployee, HSEntityTypeID, EntityTypeID, CanBeMadePrimary, IsAddedAsExt |  |
| PX.Objects.CR.Contact2 | Contact | PX_Objects_CR_Contact2, Contact1, Contact2 | ContactID |  |  |
| PX.Objects.CR.ContactAccount | Contact | PX_Objects_CR_ContactAccount | ContactID |  |  |
| PX.Objects.CR.ContactExtAddress | Contact with Address | PX_Objects_CR_ContactExtAddress, ContactwithAddress, ContactExtAddress | AddressID | IsDefault, IsAddressSameAsMain |  |
| PX.Objects.CR.ContactNotification | Contact Notification | PX_Objects_CR_ContactNotification, ContactNotification | NotificationID | EntityDescription |  |
| PX.Objects.CR.CRActivity | Activity | PX_Objects_CR_CRActivity, Activity, CRActivity | NoteID | NoteText, Source, ClassIcon, ClassInfo, PriorityIcon, IsOverdue, IsCompleteIcon, DayOfWeek, SelectorDescription, EntityDescription, IsPinned |  |
| PX.Objects.CR.CRActivityStatistics | Activity Statistics | PX_Objects_CR_CRActivityStatistics, ActivityStatistics, CRActivityStatistics | NoteID |  |  |
| PX.Objects.CR.CRAddress | Opportunity Address | PX_Objects_CR_CRAddress, OpportunityAddress, CRAddress | AddressID | OverrideAddress |  |
| PX.Objects.CR.CRBillingAddress | Bill-To Address | PX_Objects_CR_CRBillingAddress, BillToAddress, CRBillingAddress | AddressID |  |  |
| PX.Objects.CR.CRBillingContact | Bill-To Contact | PX_Objects_CR_CRBillingContact, BillToContact, CRBillingContact | ContactID |  |  |
| PX.Objects.CR.CRCampaign | Campaign | PX_Objects_CR_CRCampaign, Campaign, CRCampaign | CampaignID | DescriptionAsPlainText, SendFilter, NoteText |  |
| PX.Objects.CR.CRCampaignMembers | Campaign Members | PX_Objects_CR_CRCampaignMembers, CampaignMembers, CRCampaignMembers | CampaignID, ContactID |  |  |
| PX.Objects.CR.CRCampaignToCRMarketingListLink | CRCampaign To CRMarketingList Link | PX_Objects_CR_CRCampaignToCRMarketingListLink, CRCampaignToCRMarketingListLink | CampaignID, MarketingListID |  |  |
| PX.Objects.CR.CRCampaignType | Campaign Class | PX_Objects_CR_CRCampaignType, CampaignClass, CRCampaignType | TypeID | NoteText |  |
| PX.Objects.CR.CRCase | Case | PX_Objects_CR_CRCase, Case, CRCase | CaseCD | DescriptionAsPlainText, SLAETA, LastActivity, LastModified, TimeSpentInt, OvertimeSpentInt, TimeBillableInt, OvertimeBillableInt, TimeResolutionMinutes, Age, NoteText, EntityTypeID, DeletedDatabaseRecord |  |
| PX.Objects.CR.CRCaseClass | Case Class | PX_Objects_CR_CRCaseClass, CaseClass, CRCaseClass | CaseClassID | NoteText |  |
| PX.Objects.CR.CRCaseClassLaborMatrix | Case Class Labor | PX_Objects_CR_CRCaseClassLaborMatrix, CaseClassLabor, CRCaseClassLaborMatrix | CaseClassID, EarningType |  |  |
| PX.Objects.CR.CRCaseCommitments | Case Commitments | PX_Objects_CR_CRCaseCommitments, CaseCommitments, CRCaseCommitments | CaseCD | HeaderInitialResponseDueDateTime, HeaderResolutionDueDateTime, HeaderResponseDueDateTime |  |
| PX.Objects.CR.CRCaseReference | Case Reference | PX_Objects_CR_CRCaseReference, CaseReference, CRCaseReference | ChildCaseCD, ParentCaseCD |  |  |
| PX.Objects.CR.CRClassSeverityTime | Time Reaction By Severity | PX_Objects_CR_CRClassSeverityTime, TimeReactionBySeverity, CRClassSeverityTime | CaseClassID, Severity |  |  |
| PX.Objects.CR.CRContact | Opportunity Contact | PX_Objects_CR_CRContact, OpportunityContact, CRContact | ContactID | OverrideContact |  |
| PX.Objects.CR.CRContactClass | Contact Class | PX_Objects_CR_CRContactClass, ContactClass, CRContactClass | ClassID | NoteText |  |
| PX.Objects.CR.CRCustomerClass | Business Account Class | PX_Objects_CR_CRCustomerClass, BusinessAccountClass, CRCustomerClass | CRCustomerClassID | NoteText |  |
| PX.Objects.CR.CREmployee | Employee | PX_Objects_CR_CREmployee, Employee, CREmployee | AcctCD |  |  |
| PX.Objects.CR.CRLead | Lead | PX_Objects_CR_CRLead, Lead, CRLead | ContactID |  |  |
| PX.Objects.CR.CRLeadClass | Lead Class | PX_Objects_CR_CRLeadClass, LeadClass, CRLeadClass | ClassID | NoteText |  |
| PX.Objects.CR.CRLeadStatistics | Lead Statistics | PX_Objects_CR_CRLeadStatistics, LeadStatistics, CRLeadStatistics | ContactID |  |  |
| PX.Objects.CR.CRMarketingCategory | Marketing Category | PX_Objects_CR_CRMarketingCategory, MarketingCategory, CRMarketingCategory | MarketingCategoryID |  |  |
| PX.Objects.CR.CRMarketingList | Marketing List | PX_Objects_CR_CRMarketingList, MarketingList, CRMarketingList | MailListCode | NoteText, HSEntityTypeID |  |
| PX.Objects.CR.CRMarketingListAlias | Marketing List | PX_Objects_CR_CRMarketingListAlias, MarketingList1, CRMarketingListAlias | MailListCode |  |  |
| PX.Objects.CR.CRMarketingListMember | Marketing List Member | PX_Objects_CR_CRMarketingListMember, MarketingListMember, CRMarketingListMember | ContactID, MarketingListID | IsVirtual, Type |  |
| PX.Objects.CR.CRMassMail | Mass Emails | PX_Objects_CR_CRMassMail, MassEmails, CRMassMail | MassMailCD | SourceType, NoteText |  |
| PX.Objects.CR.CRMassMailCampaign | Mass Mail Campaign Member | PX_Objects_CR_CRMassMailCampaign, MassMailCampaignMember, CRMassMailCampaign | CampaignID, MassMailID |  |  |
| PX.Objects.CR.CRMassMailMarketingList | Mass Mail Marketing List Member | PX_Objects_CR_CRMassMailMarketingList, MassMailMarketingListMember, CRMassMailMarketingList | MailListID, MassMailID |  |  |
| PX.Objects.CR.CRMassMailMember | Mass Mail Members | PX_Objects_CR_CRMassMailMember, MassMailMembers, CRMassMailMember | ContactID, MassMailID |  |  |
| PX.Objects.CR.CRMassMailMessage | Mass Mail Message | PX_Objects_CR_CRMassMailMessage, MassMailMessage, CRMassMailMessage | MassMailID, MessageID |  |  |
| PX.Objects.CR.CROpportunity | Opportunity | PX_Objects_CR_CROpportunity, Opportunity, CROpportunity | OpportunityID | AllowOverrideBillingContactAddress, CuryWgtAmount, NoteText, PrimaryQuoteNbr, SuggestRelatedItems, CuryRate, EntityTypeID |  |
| PX.Objects.CR.CROpportunityClass | Opportunity Class | PX_Objects_CR_CROpportunityClass, OpportunityClass, CROpportunityClass | CROpportunityClassID | NoteText |  |
| PX.Objects.CR.CROpportunityClassProbability |  | PX_Objects_CR_CROpportunityClassProbability | ClassID, StageID |  |  |
| PX.Objects.CR.CROpportunityDiscountDetail | Opportunity Discount | PX_Objects_CR_CROpportunityDiscountDetail, OpportunityDiscount, CROpportunityDiscountDetail | QuoteID, RecordID | IsOrigDocDiscount |  |
| PX.Objects.CR.CROpportunityProbability | Opportunity Probability | PX_Objects_CR_CROpportunityProbability, OpportunityProbability, CROpportunityProbability | StageCode | IsActive, NoteText |  |
| PX.Objects.CR.CROpportunityProducts | Opportunity Products | PX_Objects_CR_CROpportunityProducts, OpportunityProducts, CROpportunityProducts | LineNbr, QuoteID | CalculateDiscountsOnImport, TextForProductsGrid, PreferredVendorID, NoteText, StockItemType |  |
| PX.Objects.CR.CROpportunityTax | CR Tax Detail | PX_Objects_CR_CROpportunityTax, CRTaxDetail, CROpportunityTax | LineNbr, QuoteID, TaxID | NonDeductibleTaxRate, ExpenseAmt |  |
| PX.Objects.CR.CRPMSMEmail | Activity | PX_Objects_CR_CRPMSMEmail | NoteID |  |  |
| PX.Objects.CR.CRPMTimeActivity | Activity | PX_Objects_CR_CRPMTimeActivity | NoteID | ARDocType, ARRefNbr, ChildKey |  |
| PX.Objects.CR.CRQuote | Sales Quote | PX_Objects_CR_CRQuote, SalesQuote, CRQuote | QuoteNbr | IsPrimary, AllowOverrideBillingContactAddress, Hold, IsSetupApprovalRequired, IsDisabled, TextForProductsGrid, CuryWgtAmount, NoteText, SuggestRelatedItems, CuryRate |  |
| PX.Objects.CR.CRRelation | Relations | PX_Objects_CR_CRRelation, Relations, CRRelation | RelationID | EntityCD, Name, ContactName, Email, Status, Description, OwnerID, DocumentDate |  |
| PX.Objects.CR.CRReminder | Reminder | PX_Objects_CR_CRReminder, Reminder, CRReminder | NoteID | IsReminderOn, ReminderIcon, NoteText |  |
| PX.Objects.CR.CRShippingAddress | Shipping Address | PX_Objects_CR_CRShippingAddress, ShippingAddress, CRShippingAddress | AddressID |  |  |
| PX.Objects.CR.CRShippingContact | Shipping Contact | PX_Objects_CR_CRShippingContact, ShippingContact, CRShippingContact | ContactID |  |  |
| PX.Objects.CR.CRSMEmail | Email Activity | PX_Objects_CR_CRSMEmail, EmailActivity, CRSMEmail | NoteID | DocumentSource, ClearedBody |  |
| PX.Objects.CR.CRSMTeamsActivity | Teams Activity | PX_Objects_CR_CRSMTeamsActivity, TeamsActivity, CRSMTeamsActivity | NoteID | DocumentSource |  |
| PX.Objects.CR.CRTaxTran |  | PX_Objects_CR_CRTaxTran | LineNbr, QuoteID, RecordID, TaxID | TaxRate, NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt, TaxZoneID |  |
| PX.Objects.CR.CRUnsubscribedPreferences | Marketing Unsubscribed Contact | PX_Objects_CR_CRUnsubscribedPreferences, MarketingUnsubscribedContact, CRUnsubscribedPreferences | MarketingCategoryID, RecipientContact | CategoryChannel |  |
| PX.Objects.CR.CRValidationRules | Duplicate Validation Rules | PX_Objects_CR_CRValidationRules, DuplicateValidationRules, CRValidationRules | NoteID | NoteText |  |
| PX.Objects.CR.DAC.CRNotification | CR Notification | PX_Objects_CR_DAC_CRNotification, CRNotification | SetupID |  |  |
| PX.Objects.CR.DAC.Standalone.CRCampaign | Campaign Statistics | PX_Objects_CR_DAC_Standalone_CRCampaign, CampaignStatistics, CRCampaign1 | CampaignID | NoteText |  |
| PX.Objects.CR.Inquiry.CRSMEmail | Email Activity | PX_Objects_CR_Inquiry_CRSMEmail, EmailActivity1, CRSMEmail1 | NoteID |  |  |
| PX.Objects.CR.Location | Location | PX_Objects_CR_Location, Location | BAccountID, LocationCD | NoteText, IsARAccountSameAsMain, OverrideRemitAddress, IsRemitAddressSameAsMain, OverrideRemitContact, IsRemitContactSameAsMain, IsAPAccountSameAsMain, IsAPPaymentInfoSameAsMain, IsAddressSameAsMain, OverrideAddress, IsContactSameAsMain, OverrideContact |  |
| PX.Objects.CR.LocationARAccountSub | Location GL Accounts | PX_Objects_CR_LocationARAccountSub, LocationGLAccounts1, LocationARAccountSub | BAccountID, LocationID |  |  |
| PX.Objects.CR.LocationBranchSettings | Location Settings for Current Branch | PX_Objects_CR_LocationBranchSettings, LocationSettingsforCurrentBranch, LocationBranchSettings | BAccountID, BranchID, LocationID |  |  |
| PX.Objects.CR.LocationExtAddress | Location with Address | PX_Objects_CR_LocationExtAddress, LocationwithAddress, LocationExtAddress | AddressID | IsARAccountSameAsMain, IsAPAccountSameAsMain, IsAddressSameAsMain, IsContactSameAsMain |  |
| PX.Objects.CR.PMCRActivity | Activity | PX_Objects_CR_PMCRActivity | NoteID |  | yes |
| PX.Objects.CR.PMTimeActivity | Time Activity | PX_Objects_CR_PMTimeActivity, TimeActivity, PMTimeActivity | NoteID | NoteText, DayOfWeek, ARDocType, ARRefNbr, NeedToBeDeleted, IsActivityExists, ReportedOnDate, TimeLogID, DeletedDatabaseRecord |  |
| PX.Objects.CR.SMEmail | System Email | PX_Objects_CR_SMEmail, SystemEmail, SMEmail | NoteID | NoteText, RedException, Source, DeletedDatabaseRecord |  |
| PX.Objects.CR.SMTeamsActivity | Teams Activity | PX_Objects_CR_SMTeamsActivity, TeamsActivity1, SMTeamsActivity | NoteID | NoteText |  |
| PX.Objects.CR.Standalone.CRLead | Lead | PX_Objects_CR_Standalone_CRLead, Lead1, CRLead1 | ContactID | DeletedDatabaseRecord |  |
| PX.Objects.CR.Standalone.CROpportunity |  | PX_Objects_CR_Standalone_CROpportunity | OpportunityID | NoteText |  |
| PX.Objects.CR.Standalone.CROpportunityRevision |  | PX_Objects_CR_Standalone_CROpportunityRevision | NoteID | NoteText, CuryWgtAmount, QuoteStatus, CuryRate, CuryViewState |  |
| PX.Objects.CR.Standalone.CRQuote |  | PX_Objects_CR_Standalone_CRQuote | QuoteID, QuoteNbr | NoteText |  |
| PX.Objects.CR.Standalone.Location |  | PX_Objects_CR_Standalone_Location | BAccountID, LocationCD | OverrideAddress, IsAddressSameAsMain, OverrideContact, IsContactSameAsMain, NoteText, IsDefault, IsARAccountSameAsMain, OverrideRemitAddress, IsRemitAddressSameAsMain, OverrideRemitContact, IsRemitContactSameAsMain, IsAPAccountSameAsMain, IsAPPaymentInfoSameAsMain |  |
| PX.Objects.CS.AddressValidatorPlugin | Address Verification Service | PX_Objects_CS_AddressValidatorPlugin, AddressVerificationService, AddressValidatorPlugin | AddressValidatorPluginID | NoteText |  |
| PX.Objects.CS.AddressValidatorPluginDetail | Address Verification Service Details | PX_Objects_CS_AddressValidatorPluginDetail, AddressVerificationServiceDetails, AddressValidatorPluginDetail | AddressValidatorPluginID, SettingID |  |  |
| PX.Objects.CS.ArmGLHistoryByPeriod | GL History by Period | PX_Objects_CS_ArmGLHistoryByPeriod, GLHistorybyPeriod, ArmGLHistoryByPeriod | AccountID, BranchID, FinPeriodID, LedgerID, SubID | FinYear |  |
| PX.Objects.CS.ARTranAlias |  | PX_Objects_CS_ARTranAlias | RefNbr, TranType |  |  |
| PX.Objects.CS.Carrier | Carrier | PX_Objects_CS_Carrier, Carrier | CarrierID | NoteText |  |
| PX.Objects.CS.CarrierPackage | Carrier Package | PX_Objects_CS_CarrierPackage, CarrierPackage | BoxID, CarrierID |  |  |
| PX.Objects.CS.CarrierPlugin | Carrier Plugin | PX_Objects_CS_CarrierPlugin, CarrierPlugin | CarrierPluginID | KilogramUOM, PoundUOM, CentimeterUOM, InchUOM, NoteText |  |
| PX.Objects.CS.CarrierPluginCustomer | Carrier Plugin Customer | PX_Objects_CS_CarrierPluginCustomer, CarrierPluginCustomer | CarrierPluginID, RecordID |  |  |
| PX.Objects.CS.CarrierPluginDetail | Carrier Plugin Detail | PX_Objects_CS_CarrierPluginDetail, CarrierPluginDetail | CarrierPluginID, DetailID |  |  |
| PX.Objects.CS.Country | Country | PX_Objects_CS_Country, Country | CountryID | NoteText |  |
| PX.Objects.CS.CSAnswers | Answers | PX_Objects_CS_CSAnswers, Answers, CSAnswers | AttributeID, RefNoteID | IsRequired, Order, NotInClass |  |
| PX.Objects.CS.CSAttribute | Attribute | PX_Objects_CS_CSAttribute, Attribute, CSAttribute | AttributeID | NoteText |  |
| PX.Objects.CS.CSAttributeDetail | Attribute Detail | PX_Objects_CS_CSAttributeDetail, AttributeDetail, CSAttributeDetail | AttributeID, ValueID | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.CS.CSAttributeGroup | Attribute Group | PX_Objects_CS_CSAttributeGroup, AttributeGroup, CSAttributeGroup | AttributeID, EntityClassID, EntityType | Description, ControlType |  |
| PX.Objects.CS.CSBox | Box | PX_Objects_CS_CSBox, Box, CSBox | BoxID |  |  |
| PX.Objects.CS.CSCalendar | Calendar | PX_Objects_CS_CSCalendar, Calendar, CSCalendar | CalendarID | SunWorkTime, MonWorkTime, TueWorkTime, WedWorkTime, ThuWorkTime, FriWorkTime, SatWorkTime |  |
| PX.Objects.CS.CSCalendarBreakTime | Calendar Break Time | PX_Objects_CS_CSCalendarBreakTime, CalendarBreakTime1, CSCalendarBreakTime | CalendarID, DayOfWeek, StartTime |  |  |
| PX.Objects.CS.CSCalendarExceptions | Calendar Exception | PX_Objects_CS_CSCalendarExceptions, CalendarException, CSCalendarExceptions | CalendarID, Date |  |  |
| PX.Objects.CS.DAC.OrganizationBAccount | Company | PX_Objects_CS_DAC_OrganizationBAccount, Company, OrganizationBAccount | AcctCD |  |  |
| PX.Objects.CS.DaylightShift | Daylight Shift | PX_Objects_CS_DaylightShift, DaylightShift | TimeZone, Year | TimeZoneDescription, OriginalShift |  |
| PX.Objects.CS.Dimension | Dimension | PX_Objects_CS_Dimension, Dimension | DimensionID | MaxLength |  |
| PX.Objects.CS.Email.EMailSyncFolder | EMailSyncFolder | PX_Objects_CS_Email_EMailSyncFolder, EMailSyncFolder | FolderID, ItemType, SyncAccountNoteID |  |  |
| PX.Objects.CS.FeaturesSet | Features Set | PX_Objects_CS_FeaturesSet, FeaturesSet | Status | LicenseID |  |
| PX.Objects.CS.FOBPoint | FOB Point | PX_Objects_CS_FOBPoint, FOBPoint | FOBPointID | NoteText |  |
| PX.Objects.CS.FreightRate | Freight Rate | PX_Objects_CS_FreightRate, FreightRate | CarrierID, LineNbr |  |  |
| PX.Objects.CS.NotificationRecipient | Notification Recipient | PX_Objects_CS_NotificationRecipient, NotificationRecipient | NotificationID | OriginalContactID, Hidden, Email, OrderID |  |
| PX.Objects.CS.NotificationSetup | Default Notification setup | PX_Objects_CS_NotificationSetup, DefaultNotificationsetup, NotificationSetup | SetupID |  |  |
| PX.Objects.CS.NotificationSetupRecipient | Default Notification Recipient | PX_Objects_CS_NotificationSetupRecipient, DefaultNotificationRecipient, NotificationSetupRecipient | RecipientID | OriginalContactID, Hidden, Email |  |
| PX.Objects.CS.NotificationSetupUserOverride | User's Notification Setup | PX_Objects_CS_NotificationSetupUserOverride, UsersNotificationSetup, NotificationSetupUserOverride | SetupID, UserID | ReportID |  |
| PX.Objects.CS.NotificationSource | Notification Source | PX_Objects_CS_NotificationSource, NotificationSource | SetupID, SourceID | OverrideSource |  |
| PX.Objects.CS.Numbering | Numbering Sequence | PX_Objects_CS_Numbering, NumberingSequence, Numbering | NumberingID | NoteText |  |
| PX.Objects.CS.NumberingSequence | Numbering Sequence Detail | PX_Objects_CS_NumberingSequence, NumberingSequenceDetail, NumberingSequence1 | NumberingID, NumberingSEQ |  |  |
| PX.Objects.CS.ReasonCode | Reason Code | PX_Objects_CS_ReasonCode, ReasonCode | ReasonCodeID | NoteText |  |
| PX.Objects.CS.SalesTerritory | Sales Territory | PX_Objects_CS_SalesTerritory, SalesTerritory | SalesTerritoryID | NoteText |  |
| PX.Objects.CS.Segment | Segment | PX_Objects_CS_Segment, Segment | DimensionID, SegmentID | Inherited, IsOverrideForUI |  |
| PX.Objects.CS.SegmentValue | Segment Value | PX_Objects_CS_SegmentValue, SegmentValue | DimensionID, SegmentID, Value | Included, Secured |  |
| PX.Objects.CS.ShippingZone | Shipping Zone | PX_Objects_CS_ShippingZone, ShippingZone | ZoneID |  |  |
| PX.Objects.CS.ShippingZoneLine | Shipping Zone Line | PX_Objects_CS_ShippingZoneLine, ShippingZoneLine | LineNbr, ZoneID |  |  |
| PX.Objects.CS.ShipTerms | Shipping Terms | PX_Objects_CS_ShipTerms, ShippingTerms, ShipTerms | ShipTermsID | NoteText |  |
| PX.Objects.CS.ShipTermsDetail | Shiping Terms Detail | PX_Objects_CS_ShipTermsDetail, ShipingTermsDetail, ShipTermsDetail | LineNbr, ShipTermsID |  |  |
| PX.Objects.CS.State | State | PX_Objects_CS_State, State | CountryID, StateID | NoteText |  |
| PX.Objects.CS.Terms | Terms | PX_Objects_CS_Terms, Terms | TermsID | NoteText |  |
| PX.Objects.CS.TermsInstallments | Terms Installments Detail | PX_Objects_CS_TermsInstallments, TermsInstallmentsDetail, TermsInstallments | InstallmentNbr, TermsID |  |  |
| PX.Objects.CT.Contract | Contract | PX_Objects_CT_Contract, Contract | BaseType, ContractCD | ContractInfo, Balance, StrIsTemplate, WorkgroupID, PendingSetup, PendingRecurring, PendingRenewal, TotalPending, CurrentSetup, CurrentRecurring, CurrentRenewal, TotalsCalculated, TotalRecurring, TotalUsage, TotalDue, NoteText, DaysBeforeExpiration, Days, Min, ClassID, Secured, DeletedDatabaseRecord |  |
| PX.Objects.CT.ContractBillingSchedule | Contract Billing Schedule | PX_Objects_CT_ContractBillingSchedule, ContractBillingSchedule | ContractID |  |  |
| PX.Objects.CT.ContractBillingTrace | Contract Billing Trace | PX_Objects_CT_ContractBillingTrace, ContractBillingTrace | ContractID, DocType, RecordID, RefNbr |  |  |
| PX.Objects.CT.ContractDetail | Contract Detail | PX_Objects_CT_ContractDetail, ContractDetail | ContractID, LineNbr | Change, Deposit, RecurringIncluded, RecurringUsed, RecurringUsedTotal, BaseDiscountAmt, RecurringDiscountAmt, RenewalDiscountAmt, BasePriceVal, BasePriceEditable, RenewalPriceVal, RenewalPriceEditable, FixedRecurringPriceVal, FixedRecurringPriceEditable, UsagePriceVal, UsagePriceEditable, NoteText, WarningAmountForDeposit |  |
| PX.Objects.CT.ContractDetailAcum | Contract Detail | PX_Objects_CT_ContractDetailAcum | ContractID, LineNbr |  |  |
| PX.Objects.CT.ContractItem | Contract Item | PX_Objects_CT_ContractItem, ContractItem | ContractItemCD | RecurringTypeForDeposits, UOMForDeposits, BaseItemCurySettingsID, BasePriceVal, RenewalItemCurySettingsID, RenewalPriceVal, RecurringItemCurySettingsID, FixedRecurringPriceVal, UsagePriceVal, NoteText |  |
| PX.Objects.CT.ContractRenewalHistory | Contract Renewal History | PX_Objects_CT_ContractRenewalHistory, ContractRenewalHistory | ContractID, RevID | Date |  |
| PX.Objects.CT.ContractRevisionByPeriod | Contract revision by period | PX_Objects_CT_ContractRevisionByPeriod, Contractrevisionbyperiod | ContractID, FinPeriodID | NewCount |  |
| PX.Objects.CT.ContractSLAMapping | Contract SLA Mapping | PX_Objects_CT_ContractSLAMapping, ContractSLAMapping | ContractSLAMappingID |  |  |
| PX.Objects.CT.ContractTemplate | Contract Template | PX_Objects_CT_ContractTemplate, ContractTemplate | BaseType, ContractCD | ContractStrID |  |
| PX.Objects.CT.SelContractWatcher |  | PX_Objects_CT_SelContractWatcher | ContractID, EMail |  |  |
| PX.Objects.CT.Standalone.ContractDetail |  | PX_Objects_CT_Standalone_ContractDetail | ContractDetailID, ContractID, RevID | BasePriceVal, FixedRecurringPriceVal |  |
| PX.Objects.DR.DRDeferredCode | Deferral Code | PX_Objects_DR_DRDeferredCode, DeferralCode, DRDeferredCode | DeferredCodeID | Periods, NoteText |  |
| PX.Objects.DR.DRExpenseBalance | DR Expense Balance | PX_Objects_DR_DRExpenseBalance, DRExpenseBalance | AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID |  |  |
| PX.Objects.DR.DRExpenseBalance2 | DR Expense Balance | PX_Objects_DR_DRExpenseBalance2 | AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID |  |  |
| PX.Objects.DR.DRExpenseBalanceByPeriod | DR Expense Balance by Period | PX_Objects_DR_DRExpenseBalanceByPeriod, DRExpenseBalancebyPeriod | AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID |  |  |
| PX.Objects.DR.DRExpenseProjection | DR Expense Projection | PX_Objects_DR_DRExpenseProjection, DRExpenseProjection | AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID |  |  |
| PX.Objects.DR.DRRevenueBalance | DR Revenue Balance | PX_Objects_DR_DRRevenueBalance, DRRevenueBalance | AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID |  |  |
| PX.Objects.DR.DRRevenueBalance2 | DR Revenue Balance | PX_Objects_DR_DRRevenueBalance2 | AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID |  |  |
| PX.Objects.DR.DRRevenueBalanceByPeriod | DR Revenue Balance by Period | PX_Objects_DR_DRRevenueBalanceByPeriod, DRRevenueBalancebyPeriod | AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID |  |  |
| PX.Objects.DR.DRRevenueProjection | DR Revenue Projection | PX_Objects_DR_DRRevenueProjection, DRRevenueProjection | AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID |  |  |
| PX.Objects.DR.DRSchedule | Deferral Schedule | PX_Objects_DR_DRSchedule, DeferralSchedule, DRSchedule | ScheduleNbr | DocumentType, BAccountType, OrigLineAmt, CuryNetTranPrice, NetTranPrice, ComponentsTotal, DefTotal, DocumentTypeEx, Status, IsPoolVisible, IsRecalculated, IsSuspense, NoteText, CuryRate, CuryViewState |  |
| PX.Objects.DR.DRScheduleDetail | Deferral Schedule Component | PX_Objects_DR_DRScheduleDetail, DeferralScheduleComponent, DRScheduleDetail | ComponentID, DetailLineNbr, ScheduleID | ParentInventoryID, ReceiptNbr, PONbr, AllowControlAccountForModule, DefTotal, DocumentType, BAccountType, DefCodeType, AllocationWeightResidual, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.DR.DRScheduleTran | DRScheduleTran | PX_Objects_DR_DRScheduleTran, DRScheduleTran | ComponentID, DetailLineNbr, LineNbr, ScheduleID | ReceiptNbr, PONbr, AllowControlAccountForModule |  |
| PX.Objects.DR.DRScheduleTranLineLink | DR Schedule Transaction Lines | PX_Objects_DR_DRScheduleTranLineLink, DRScheduleTransactionLines, DRScheduleTranLineLink | ScheduleID |  |  |
| PX.Objects.EP.ClockInClockOut.EPClockInTimerData | Timer | PX_Objects_EP_ClockInClockOut_EPClockInTimerData, Timer, EPClockInTimerData | TimerDataID | NoteText, Status, EntityName, DocumentDescr, StartDateUTC, TimerDisplay, IsClockIn, IsPause, IsStart, IsStop |  |
| PX.Objects.EP.ClockInClockOut.EPTimeLog | Time Log | PX_Objects_EP_ClockInClockOut_EPTimeLog, TimeLog, EPTimeLog | TimeLogID |  |  |
| PX.Objects.EP.ClockInClockOut.EPTimeLogType | Time Log Type | PX_Objects_EP_ClockInClockOut_EPTimeLogType, TimeLogType, EPTimeLogType | TimeLogTypeID |  |  |
| PX.Objects.EP.ContractEx | Contract | PX_Objects_EP_ContractEx | BaseType, ContractCD |  |  |
| PX.Objects.EP.ContractExEx | Contract | PX_Objects_EP_ContractExEx | BaseType, ContractCD |  |  |
| PX.Objects.EP.DAC.EPEmployeeCorpCardLink | Employee Corporate Card Reference | PX_Objects_EP_DAC_EPEmployeeCorpCardLink, EmployeeCorporateCardReference, EPEmployeeCorpCardLink | CorpCardID, EmployeeID |  |  |
| PX.Objects.EP.DAC.EPExpenseClaimForCurrentUser | Expense Claim | PX_Objects_EP_DAC_EPExpenseClaimForCurrentUser, ExpenseClaim1, EPExpenseClaimForCurrentUser | RefNbr |  |  |
| PX.Objects.EP.DAC.EPRuleApprover | Rule Approver | PX_Objects_EP_DAC_EPRuleApprover, RuleApprover, EPRuleApprover | RuleApproverID |  |  |
| PX.Objects.EP.EPActivityApprove | Time Activity | PX_Objects_EP_EPActivityApprove | NoteID |  | yes |
| PX.Objects.EP.EPActivityApprove2 | Mass Weekly Crew Time Entry | PX_Objects_EP_EPActivityApprove2, MassWeeklyCrewTimeEntry, EPActivityApprove2 | NoteID |  |  |
| PX.Objects.EP.EPActivityRelease | Release Time Activity | PX_Objects_EP_EPActivityRelease, ReleaseTimeActivity, EPActivityRelease | NoteID |  |  |
| PX.Objects.EP.EPActivityType | Activity Type | PX_Objects_EP_EPActivityType, ActivityType, EPActivityType | Type | NoteText |  |
| PX.Objects.EP.EPApproval | Approval | PX_Objects_EP_EPApproval, Approval, EPApproval | ApprovalID | NoteText, DocType |  |
| PX.Objects.EP.EPAssignmentMap | Assignment Map | PX_Objects_EP_EPAssignmentMap, AssignmentMap, EPAssignmentMap | AssignmentMapID | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.EP.EPAssignmentRoute | Legacy Assignment Route | PX_Objects_EP_EPAssignmentRoute, LegacyAssignmentRoute, EPAssignmentRoute | AssignmentRouteID | Icon |  |
| PX.Objects.EP.EPAssignmentRule | Legacy Assignmnent Rule | PX_Objects_EP_EPAssignmentRule, LegacyAssignmnentRule, EPAssignmentRule | AssignmentRuleID |  |  |
| PX.Objects.EP.EPAttendee | Attendee | PX_Objects_EP_EPAttendee, Attendee, EPAttendee | AttendeeID, EventNoteID |  |  |
| PX.Objects.EP.EPContractRate | Contract Rates | PX_Objects_EP_EPContractRate, ContractRates, EPContractRate | RecordID |  |  |
| PX.Objects.EP.EPCustomWeek | Custom Week | PX_Objects_EP_EPCustomWeek, CustomWeek, EPCustomWeek | WeekID | FullNumber, Description, ShortDescription, EntityDescription |  |
| PX.Objects.EP.EPDepartment | Department | PX_Objects_EP_EPDepartment, Department, EPDepartment | DepartmentID |  |  |
| PX.Objects.EP.EPEarningType | Earning Type | PX_Objects_EP_EPEarningType, EarningType, EPEarningType | TypeCD |  |  |
| PX.Objects.EP.EPEmployee | Employee | PX_Objects_EP_EPEmployee, Employee1, EPEmployee | AcctCD |  |  |
| PX.Objects.EP.EPEmployeeClass | Employee Class | PX_Objects_EP_EPEmployeeClass, EmployeeClass, EPEmployeeClass | VendorClassID |  |  |
| PX.Objects.EP.EPEmployeeClassLaborMatrix | Employee Class Labor | PX_Objects_EP_EPEmployeeClassLaborMatrix, EmployeeClassLabor, EPEmployeeClassLaborMatrix | EarningType, EmployeeID |  |  |
| PX.Objects.EP.EPEmployeeContract | Employee Contract | PX_Objects_EP_EPEmployeeContract, EmployeeContract, EPEmployeeContract | ContractID, EmployeeID |  |  |
| PX.Objects.EP.EPEmployeeEx | Employee | PX_Objects_EP_EPEmployeeEx | AcctCD |  |  |
| PX.Objects.EP.EPEmployeePosition | Employee Position | PX_Objects_EP_EPEmployeePosition, EmployeePosition, EPEmployeePosition | EmployeeID, LineNbr | NoteText |  |
| PX.Objects.EP.EPEquipment | Equipment | PX_Objects_EP_EPEquipment, Equipment, EPEquipment | EquipmentCD | ClassID, NoteText |  |
| PX.Objects.EP.EPEquipmentDetail | Equipment Time Card Detail | PX_Objects_EP_EPEquipmentDetail, EquipmentTimeCardDetail, EPEquipmentDetail | LineNbr, TimeCardCD | NoteText |  |
| PX.Objects.EP.EPEquipmentRate | Equipment Rate | PX_Objects_EP_EPEquipmentRate, EquipmentRate, EPEquipmentRate | EquipmentID, ProjectID | NoteText |  |
| PX.Objects.EP.EPEquipmentSummary | Equipment Time Card Summary | PX_Objects_EP_EPEquipmentSummary, EquipmentTimeCardSummary, EPEquipmentSummary | LineNbr, TimeCardCD | TimeSpent, NoteText, LabourClassCalc |  |
| PX.Objects.EP.EPEquipmentTimeCard | Equipment Time Card | PX_Objects_EP_EPEquipmentTimeCard, EquipmentTimeCard, EPEquipmentTimeCard | TimeCardCD | WorkgroupID, OwnerID, NoteText, WeekStartDate, WeekDescription, WeekShortDescription, TimeSetupCalc, TimeRunCalc, TimeSuspendCalc, TimeTotalCalc, TimeBillableSetupCalc, TimeBillableRunCalc, TimeBillableSuspendCalc, TimeBillableTotalCalc, TimecardType, SunTotal, MonTotal, TueTotal, WedTotal, ThuTotal, FriTotal, SatTotal, WeekTotal |  |
| PX.Objects.EP.EPEventCategory | Event Category | PX_Objects_EP_EPEventCategory, EventCategory, EPEventCategory | CategoryID |  |  |
| PX.Objects.EP.EPExpenseClaim | Expense Claim | PX_Objects_EP_EPExpenseClaim, ExpenseClaim, EPExpenseClaim | RefNbr | ReleasedToVerify, HasWithHoldTax, HasUseTax, NoteText, CuryLineTotal, LineTotal, OwnerID, FormCaptionDescription, CuryRate, CuryViewState |  |
| PX.Objects.EP.EPExpenseClaimDetails | Expense Receipt | PX_Objects_EP_EPExpenseClaimDetails, ExpenseReceipt, EPExpenseClaimDetails | ClaimDetailCD | RefNbrNotFiltered, CuryTaxTipTotal, TaxTipTotal, HasWithHoldTax, HasUseTax, CuryNetAmount, NetAmount, StatusClaim, HoldClaim, NoteText, DailyFieldReportId, CuryRate, CuryViewState, ClaimCuryID |  |
| PX.Objects.EP.EPPosition | Position | PX_Objects_EP_EPPosition, Position, EPPosition | PositionID |  |  |
| PX.Objects.EP.EPRule | Assignment/Approval Rule | PX_Objects_EP_EPRule, AssignmentApprovalRule, EPRule | RuleID | NoteText, StepName, Icon |  |
| PX.Objects.EP.EPRuleCondition | Assignment/Approval Rule Condition | PX_Objects_EP_EPRuleCondition, AssignmentApprovalRuleCondition, EPRuleCondition | RowNbr, RuleID | IsField, UiNoteID |  |
| PX.Objects.EP.EPRuleEmployeeCondition | Assignment/Approval Rule Employee Condition | PX_Objects_EP_EPRuleEmployeeCondition, AssignmentApprovalRuleEmployeeCondition, EPRuleEmployeeCondition | RowNbr, RuleID | UiNoteID |  |
| PX.Objects.EP.EPRuleTree | Assignment/Approval Rule | PX_Objects_EP_EPRuleTree | RuleID |  |  |
| PX.Objects.EP.EPShiftCode | Shift Code | PX_Objects_EP_EPShiftCode, ShiftCode, EPShiftCode | ShiftCD | NoteText |  |
| PX.Objects.EP.EPShiftCodeRate | Shift Code Rate | PX_Objects_EP_EPShiftCodeRate, ShiftCodeRate, EPShiftCodeRate | CuryID, EffectiveDate, ShiftID |  |  |
| PX.Objects.EP.EPTax | EP Tax Detail | PX_Objects_EP_EPTax, EPTaxDetail, EPTax | ClaimDetailID, IsTipTax, TaxID | NonDeductibleTaxRate, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.EP.EPTaxAggregate |  | PX_Objects_EP_EPTaxAggregate | RefNbr, TaxID | NonDeductibleTaxRate |  |
| PX.Objects.EP.EPTaxTran |  | PX_Objects_EP_EPTaxTran | ClaimDetailID, IsTipTax, TaxID | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.EP.EPTimeActivitiesSummary | Time Activities Summary | PX_Objects_EP_EPTimeActivitiesSummary, TimeActivitiesSummary, EPTimeActivitiesSummary | ContactID, Week, WorkgroupID | IsWithoutActivities |  |
| PX.Objects.EP.EPTimeCard | Employee Time Card | PX_Objects_EP_EPTimeCard, EmployeeTimeCard, EPTimeCard | TimeCardCD | WorkgroupID, OwnerID, TotalTimeSpent, TotalTimeBillable, FormCaptionDescription, NoteText, WeekStartDate, WeekEndDate, WeekDescription, WeekShortDescription, TimeSpentCalc, OvertimeSpentCalc, TotalSpentCalc, TimeBillableCalc, OvertimeBillableCalc, TotalBillableCalc, TimecardType, BillingRateCalc, SunTotal, MonTotal, TueTotal, WedTotal, ThuTotal, FriTotal, SatTotal, Day1Total, Day2Total, Day3Total, Day4Total, Day5Total, Day6Total, Day7Total, Day8Total, Day9Total, Day10Total, Day11Total, Day12Total, Day13Total, Day14Total, Day15Total, Day16Total, Day17Total, Day18Total, Day19Total, Day20Total, Day21Total, Day22Total, Day23Total, Day24Total, Day25Total, Day26Total, Day27Total, Day28Total, Day29Total, Day30Total, Day31Total, WeekTotal |  |
| PX.Objects.EP.EPTimeCardEx | Employee Time Card | PX_Objects_EP_EPTimeCardEx | TimeCardCD |  |  |
| PX.Objects.EP.EPTimeCardItem | Time Card Item | PX_Objects_EP_EPTimeCardItem, TimeCardItem, EPTimeCardItem | LineNbr, TimeCardCD | Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13, Day14, Day15, Day16, Day17, Day18, Day19, Day20, Day21, Day22, Day23, Day24, Day25, Day26, Day27, Day28, Day29, Day30, Day31, DayName1, DayName2, DayName3, DayName4, DayName5, DayName6, DayName7, DayName8, DayName9, DayName10, DayName11, DayName12, DayName13, DayName14, DayName15, DayName16, DayName17, DayName18, DayName19, DayName20, DayName21, DayName22, DayName23, DayName24, DayName25, DayName26, DayName27, DayName28, DayName29, DayName30, DayName31, NoteText |  |
| PX.Objects.EP.EPTimeCardSummary | Time Card Summary | PX_Objects_EP_EPTimeCardSummary, TimeCardSummary, EPTimeCardSummary | LineNbr, TimeCardCD | EmployeeID, NoteText, EmployeeRate |  |
| PX.Objects.EP.EPView | Activity View Status | PX_Objects_EP_EPView, ActivityViewStatus, EPView | ContactID, NoteID |  |  |
| PX.Objects.EP.EPViewMy | Activity View Status | PX_Objects_EP_EPViewMy, ActivityViewStatus1, EPViewMy | ContactID, NoteID |  |  |
| PX.Objects.EP.EPWeeklyCrewTimeActivity | Weekly Crew Time Activity | PX_Objects_EP_EPWeeklyCrewTimeActivity, WeeklyCrewTimeActivity, EPWeeklyCrewTimeActivity | Week, WorkgroupID |  |  |
| PX.Objects.EP.EPWingman | Delegate | PX_Objects_EP_EPWingman, Delegate, EPWingman | RecordID |  |  |
| PX.Objects.EP.Standalone.EPEmployeeClass |  | PX_Objects_EP_Standalone_EPEmployeeClass | VendorClassID |  |  |
| PX.Objects.EP.TimecardWithTotals |  | PX_Objects_EP_TimecardWithTotals | TimeCardCD | WeekStartDate |  |
| PX.Objects.FA.DAC.FALocationHistoryByPeriod | FA Location History by Period | PX_Objects_FA_DAC_FALocationHistoryByPeriod, FALocationHistorybyPeriod | AssetID, LastRevisionID |  |  |
| PX.Objects.FA.FAAccrualTran | FA Accrual Transaction | PX_Objects_FA_FAAccrualTran, FAAccrualTransaction, FAAccrualTran | GLTranID | SelectedQty, SelectedAmt, ClassID, EmployeeID, Department, Component |  |
| PX.Objects.FA.FAApplicableMethod | FA Applicable Method | PX_Objects_FA_FAApplicableMethod, FAApplicableMethod | AssetID, BookID, StartPeriodID | AveragingConvention, IsOriginal |  |
| PX.Objects.FA.FABonus | Bonus | PX_Objects_FA_FABonus, Bonus, FABonus | BonusCD | NoteText |  |
| PX.Objects.FA.FABonusDetails | FA Bonus Details | PX_Objects_FA_FABonusDetails, FABonusDetails | BonusID, LineNbr |  |  |
| PX.Objects.FA.FABook | FA Book | PX_Objects_FA_FABook, FABook | BookCode |  |  |
| PX.Objects.FA.FABookBalance | FA Book Balance | PX_Objects_FA_FABookBalance, FABookBalance | AssetID, BookID | DeprFromYear, DeprToYear, DisposalAmount, AllowChangeDeprFromPeriod, NoteText |  |
| PX.Objects.FA.FABookHistory | FA Book History | PX_Objects_FA_FABookHistory, FABookHistory | AssetID, BookID, FinPeriodID | Reopen |  |
| PX.Objects.FA.FABookHistoryByPeriod | FA Book History by Period | PX_Objects_FA_FABookHistoryByPeriod, FABookHistorybyPeriod | AssetID, BookID, FinPeriodID |  |  |
| PX.Objects.FA.FABookHistoryRecon | FA Book History for Reconciliation | PX_Objects_FA_FABookHistoryRecon, FABookHistoryforReconciliation, FABookHistoryRecon | AssetID, BookID |  |  |
| PX.Objects.FA.FABookPeriod | FA Book Period | PX_Objects_FA_FABookPeriod, FABookPeriod | BookID, FinPeriodID, OrganizationID | StartDateUI, EndDateUI |  |
| PX.Objects.FA.FABookPeriodSetup | FA Book Period Template | PX_Objects_FA_FABookPeriodSetup, FABookPeriodTemplate, FABookPeriodSetup | BookID, PeriodNbr | StartDateUI, EndDateUI |  |
| PX.Objects.FA.FABookSettings | FA Book Preferences | PX_Objects_FA_FABookSettings, FABookPreferences, FABookSettings | AssetID, BookID |  |  |
| PX.Objects.FA.FABookYear | FA Book Year | PX_Objects_FA_FABookYear, FABookYear | BookID, OrganizationID, Year |  |  |
| PX.Objects.FA.FABookYearSetup | Book Calendar | PX_Objects_FA_FABookYearSetup, BookCalendar, FABookYearSetup | BookID | NoteText, BelongsToNextYear |  |
| PX.Objects.FA.FAClass | Asset Class | PX_Objects_FA_FAClass, AssetClass, FAClass | AssetCD |  |  |
| PX.Objects.FA.FAComponent | FA Component | PX_Objects_FA_FAComponent, FAComponent | AssetCD |  |  |
| PX.Objects.FA.FADepreciationMethod | Depreciation Method | PX_Objects_FA_FADepreciationMethod, DepreciationMethod, FADepreciationMethod | MethodCD | DisplayTotalPercents, DepreciationPeriodsInYear, DepreciationStartDate, DepreciationStopDate, BookID, Source, NoteText |  |
| PX.Objects.FA.FADepreciationMethodLines | FA Depreciation Method Lines | PX_Objects_FA_FADepreciationMethodLines, FADepreciationMethodLines | MethodID, Year | DisplayRatioPerYear, NoteText |  |
| PX.Objects.FA.FADetails | FA Details | PX_Objects_FA_FADetails, FADetails | AssetID | TransferPeriod, BaseCuryID, DisplayDisposalDate, DisplayDisposalPeriodID, DisplayDisposalMethodID, DisplaySaleAmount |  |
| PX.Objects.FA.FADetailsTransfer | FA Details | PX_Objects_FA_FADetailsTransfer, FADetails1, FADetailsTransfer | AssetID |  |  |
| PX.Objects.FA.FADisposalMethod | FA Disposal Method | PX_Objects_FA_FADisposalMethod, FADisposalMethod | DisposalMethodCD |  |  |
| PX.Objects.FA.FAHistoryByPeriod | FA History by Period | PX_Objects_FA_FAHistoryByPeriod, FAHistorybyPeriod | AssetID, BookID, FinPeriodID |  |  |
| PX.Objects.FA.FALocationHistory | FA Location History | PX_Objects_FA_FALocationHistory, FALocationHistory | AssetID, RevisionID |  |  |
| PX.Objects.FA.FAOrganizationBook | FA Book | PX_Objects_FA_FAOrganizationBook | BookCode | OrganizationID, FirstCalendarYear, LastCalendarYear |  |
| PX.Objects.FA.FAProjectedGLTran | FA transactions in GL representation | PX_Objects_FA_FAProjectedGLTran, FAtransactionsinGLrepresentation, FAProjectedGLTran | LineNbr, RefNbr |  |  |
| PX.Objects.FA.FARegister | Fixed Asset Transaction | PX_Objects_FA_FARegister, FixedAssetTransaction, FARegister | RefNbr | NoteText, TranAmt |  |
| PX.Objects.FA.FAService | FA Service | PX_Objects_FA_FAService, FAService | AssetID, ServiceNumber |  |  |
| PX.Objects.FA.FAServiceSchedule | FA Service Schedule | PX_Objects_FA_FAServiceSchedule, FAServiceSchedule | ScheduleCD |  |  |
| PX.Objects.FA.FATran | Fixed Asset Transaction | PX_Objects_FA_FATran, FixedAssetTransaction1, FATran | LineNbr, RefNbr | ReceiptDate, DeprFromDate, ClassID, TargetAssetID, EmployeeID, Department, NewAsset, Component, NoteText, AssetCD, Depreciable |  |
| PX.Objects.FA.FAType | FA Type | PX_Objects_FA_FAType, FAType | AssetTypeID |  |  |
| PX.Objects.FA.FAUsage | FA Usage | PX_Objects_FA_FAUsage, FAUsage | AssetID, Number |  |  |
| PX.Objects.FA.FAUsageSchedule | FA Usage Schedule | PX_Objects_FA_FAUsageSchedule, FAUsageSchedule | ScheduleCD |  |  |
| PX.Objects.FA.FixedAsset | Fixed Asset | PX_Objects_FA_FixedAsset, FixedAsset | AssetCD | NoteText, DisposalAmt, SalvageAmtAfterSplit |  |
| PX.Objects.FA.Overrides.AssetProcess.FABookHist | FA Book History | PX_Objects_FA_Overrides_AssetProcess_FABookHist | AssetID, BookID, FinPeriodID |  |  |
| PX.Objects.FA.SplitParams | Fixed Asset | PX_Objects_FA_SplitParams | AssetCD |  | yes |
| PX.Objects.FA.Standalone.FABookBalance |  | PX_Objects_FA_Standalone_FABookBalance | AssetID, BookID |  |  |
| PX.Objects.FA.Standalone.FADetails | FA Details | PX_Objects_FA_Standalone_FADetails, FADetails2 | AssetID | DisplayDisposalDate, DisplayDisposalPeriodID, DisplayDisposalMethodID, DisplaySaleAmount |  |
| PX.Objects.FA.Transact | Fixed Asset Transaction | PX_Objects_FA_Transact | LineNbr, RefNbr |  | yes |
| PX.Objects.FS.ActiveSchedule |  | PX_Objects_FS_ActiveSchedule | CustomerID, RefNbr |  | yes |
| PX.Objects.FS.AppointmentBoxComponentField |  | PX_Objects_FS_AppointmentBoxComponentField | ComponentType, FieldName, ObjectName |  |  |
| PX.Objects.FS.AppointmentToPost | Appointment | PX_Objects_FS_AppointmentToPost | RefNbr, SrvOrdType | RowIndex, GroupKey, BatchID, ErrorFlag |  |
| PX.Objects.FS.BAccountLocation |  | PX_Objects_FS_BAccountLocation | CustomerID, LocationID |  |  |
| PX.Objects.FS.BAccountSelectorBase | Business Account | PX_Objects_FS_BAccountSelectorBase | AcctCD |  |  |
| PX.Objects.FS.BAccountStaffMember | Business Account | PX_Objects_FS_BAccountStaffMember | AcctCD |  |  |
| PX.Objects.FS.ContractPeriodToPost |  | PX_Objects_FS_ContractPeriodToPost | ContractPeriodID, ServiceContractID | ContractPostBatchID, BillingPeriod |  |
| PX.Objects.FS.ContractPostBatchDetail |  | PX_Objects_FS_ContractPostBatchDetail | ContractPostBatchID, ContractPostDocID | ContractRefNbr, CustomerContractNbr, AcctName |  |
| PX.Objects.FS.EPEmployeeFSRouteEmployee | Employee | PX_Objects_FS_EPEmployeeFSRouteEmployee | AcctCD | MemDriverName |  |
| PX.Objects.FS.FSAddress | Field Service Address | PX_Objects_FS_FSAddress, FieldServiceAddress, FSAddress | AddressID | OverrideAddress, FullAddress |  |
| PX.Objects.FS.FSAdjust |  | PX_Objects_FS_FSAdjust | AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr | CuryAdjgDiscAmt, CuryAdjdDiscAmt, AdjDiscAmt, CuryDocBal, DocBal, NoteText, SOCuryCompletedBillableTotal, AdjdOrigCuryID, CuryRate, CuryViewState, AdjdCuryID |  |
| PX.Objects.FS.FSAppointment | Appointment | PX_Objects_FS_FSAppointment, Appointment, FSAppointment | RefNbr, SrvOrdType | SrvOrdTypeCode, BillCustomerID, UserConfirmedUnclosing, StartActionRunning, PauseActionRunning, ResumeActionRunning, CompleteActionRunning, CloseActionRunning, UnCloseActionRunning, CancelActionRunning, ReopenActionRunning, ReloadServiceOrderRelated, AreActualFieldsActive, EffDocDate, NoteText, ProfitPercent, ProfitMarginPercent, CuryLineDocDiscountTotal, DocDisc, CuryDocDisc, SkipExternalTaxCalculation, AppCompletedBillableTotal, IntTravelInProcess, isBeingCloned, ScheduledDuration, ActualDuration, ScheduledDateBegin, IsRouteAppoinment, IsPrepaymentEnable, IsReassigned, ActualDurationTotalReport, AppointmentRefReport, IsCalledFromQuickProcess, IsPosted, TravelCanBeStarted, TravelCanBeCompleted, MustUpdateServiceOrder, FormCaptionDescription, IsINReleaseProcess, TrackTimeChanged, CuryActualBillableTotal, ActualBillableTotal, EditActionRunning, CuryRate |  |
| PX.Objects.FS.FSAppointmentDet | Appointment Item Detail | PX_Objects_FS_FSAppointmentDet, AppointmentItemDetail, FSAppointmentDet | LineNbr, RefNbr, SrvOrdType | SOLineType, UIStatus, AreActualFieldsActive, Qty, NoteText, CuryExtPrice, CuryLineAmt, SkipCostCodeValidation, InventoryIDReport, CanChangeMarkForPO, EnableUnlinkPO, TabOrigin, LinkedDisplayRefNbr, InventoryCD, Operation, TranType, InvtMult, LocationID, TaskID, IsLotSerialRequired, INOpenQty |  |
| PX.Objects.FS.FSAppointmentDiscountDetail |  | PX_Objects_FS_FSAppointmentDiscountDetail | EntityType, RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSAppointmentEmployee | FSAppointmentEmployee | PX_Objects_FS_FSAppointmentEmployee, FSAppointmentEmployee | LineNbr, RefNbr, SrvOrdType | NoteText, SkipCostCodeValidation, IsStaffCalendar |  |
| PX.Objects.FS.FSAppointmentFSServiceOrder | Appointment | PX_Objects_FS_FSAppointmentFSServiceOrder | RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSAppointmentInRoute | Appointment | PX_Objects_FS_FSAppointmentInRoute | RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSAppointmentLog | Log | PX_Objects_FS_FSAppointmentLog, Log, FSAppointmentLog | LogID |  | yes |
| PX.Objects.FS.FSAppointmentLogExtItemLine | Log | PX_Objects_FS_FSAppointmentLogExtItemLine | LogID |  |  |
| PX.Objects.FS.FSAppointmentResource |  | PX_Objects_FS_FSAppointmentResource | RefNbr, SMEquipmentID, SrvOrdType | SMEquipmentIDReport |  |
| PX.Objects.FS.FSAppointmentScheduleBoard |  | PX_Objects_FS_FSAppointmentScheduleBoard | RefNbr, SrvOrdType | RoomDesc, FirstServiceDesc, StatusUI, CustomID, CustomDateID, CustomRoomID, AppointmentCustomID, CustomDateTimeStart, CustomDateTimeEnd, EmployeeID, OldEmployeeID, EmployeeList, EmployeeCount, ServiceCount, ServiceList, CanDeleteAppointment, MemRefNbr, MemAcctName, OpenAppointmentScreenOnError, IsPosted, Resizable, Draggable |  |
| PX.Objects.FS.FSAppointmentServiceEmployee | Appointment Item Detail | PX_Objects_FS_FSAppointmentServiceEmployee | LineNbr, RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSAppointmentStaffDistinct |  | PX_Objects_FS_FSAppointmentStaffDistinct | BAccountID, RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSAppointmentStaffExtItemLine |  | PX_Objects_FS_FSAppointmentStaffExtItemLine | LineNbr, RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSAppointmentStaffMember | Business Account | PX_Objects_FS_FSAppointmentStaffMember | AcctCD |  |  |
| PX.Objects.FS.FSAppointmentStaffScheduleBoard |  | PX_Objects_FS_FSAppointmentStaffScheduleBoard | RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSAppointmentStatusColor | Appointment Status Color | PX_Objects_FS_FSAppointmentStatusColor, AppointmentStatusColor, FSAppointmentStatusColor | StatusID |  |  |
| PX.Objects.FS.FSAppointmentTax | Appointment Tax | PX_Objects_FS_FSAppointmentTax, AppointmentTax, FSAppointmentTax | LineNbr, RefNbr, SrvOrdType, TaxID | NonDeductibleTaxRate, ExpenseAmt |  |
| PX.Objects.FS.FSAppointmentTaxTran | Appointment Tax Detail | PX_Objects_FS_FSAppointmentTaxTran, AppointmentTaxDetail, FSAppointmentTaxTran | RecordID, RefNbr, SrvOrdType, TaxID | NonDeductibleTaxRate, ExpenseAmt, TaxZoneID |  |
| PX.Objects.FS.FSAppQuickProcessParams |  | PX_Objects_FS_FSAppQuickProcessParams | OrderType |  | yes |
| PX.Objects.FS.FSApptLineSplit | Appointment Lot/Serial Detail | PX_Objects_FS_FSApptLineSplit, AppointmentLotSerialDetail, FSApptLineSplit | ApptNbr, LineNbr, SplitLineNbr, SrvOrdType | TranType, LastLotSerialNbr, LotSerClassID, AssignedNbr, ProjectID, TaskID, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.FS.FSBillHistory | Field Service Billing History | PX_Objects_FS_FSBillHistory, FieldServiceBillingHistory, FSBillHistory | RecordID | ChildDocLink, ParentDocLink, ChildDocDesc, ChildDocDate, ChildDocStatus, IsChildDocDeleted, ChildAmount, ServiceContractPeriodID, ContractPeriodStatus, RelatedDocument |  |
| PX.Objects.FS.FSBillingCycle | Billing Cycle | PX_Objects_FS_FSBillingCycle, BillingCycle, FSBillingCycle | BillingCycleCD | NoteText |  |
| PX.Objects.FS.FSBLOCAddress | Field Service Address | PX_Objects_FS_FSBLOCAddress | AddressID |  |  |
| PX.Objects.FS.FSBLOCContact | Field Service Contact | PX_Objects_FS_FSBLOCContact | ContactID |  |  |
| PX.Objects.FS.FSBranchLocation | Branch Location | PX_Objects_FS_FSBranchLocation, BranchLocation, FSBranchLocation | BranchLocationCD | NoteText, RoomFeatureEnabled, DeletedDatabaseRecord |  |
| PX.Objects.FS.FSCalendarComponentField |  | PX_Objects_FS_FSCalendarComponentField | ComponentType, FieldName, ObjectName | LineNbr |  |
| PX.Objects.FS.FSContact | Field Service Contact | PX_Objects_FS_FSContact, FieldServiceContact, FSContact | ContactID | OverrideContact |  |
| PX.Objects.FS.FSContractAction |  | PX_Objects_FS_FSContractAction | RecordID |  |  |
| PX.Objects.FS.FSContractForecast |  | PX_Objects_FS_FSContractForecast | ForecastID, ServiceContractID |  |  |
| PX.Objects.FS.FSContractForecastDet |  | PX_Objects_FS_FSContractForecastDet | ForecastID, LineNbr, ServiceContractID |  |  |
| PX.Objects.FS.FSContractGenerationHistory | Contract Generation History | PX_Objects_FS_FSContractGenerationHistory, ContractGenerationHistory, FSContractGenerationHistory | ContractGenerationHistoryID |  |  |
| PX.Objects.FS.FSContractPeriod |  | PX_Objects_FS_FSContractPeriod | ContractPeriodID, ServiceContractID | BillingPeriod |  |
| PX.Objects.FS.FSContractPeriodDet | Contract Period Detail | PX_Objects_FS_FSContractPeriodDet, ContractPeriodDetail, FSContractPeriodDet | ContractPeriodDetID, ContractPeriodID | ScheduledQty, ScheduledTime, SkipCostCodeValidation, Amount, RemainingAmount, UsedAmount, ScheduledAmount |  |
| PX.Objects.FS.FSContractPostBatch |  | PX_Objects_FS_FSContractPostBatch | ContractPostBatchNbr |  |  |
| PX.Objects.FS.FSContractPostDet |  | PX_Objects_FS_FSContractPostDet | ContractPostDetID |  |  |
| PX.Objects.FS.FSContractPostDoc |  | PX_Objects_FS_FSContractPostDoc | ContractPostDocID |  |  |
| PX.Objects.FS.FSContractPostRegister |  | PX_Objects_FS_FSContractPostRegister | ContractPeriodID, ServiceContractID |  |  |
| PX.Objects.FS.FSContractSchedule |  | PX_Objects_FS_FSContractSchedule | CustomerID, RefNbr |  | yes |
| PX.Objects.FS.FSCreatedDoc |  | PX_Objects_FS_FSCreatedDoc | RecordID |  |  |
| PX.Objects.FS.FSCustomer | Customer | PX_Objects_FS_FSCustomer | AcctCD |  |  |
| PX.Objects.FS.FSCustomerBillingSetup | FSCustomerBillingSetup | PX_Objects_FS_FSCustomerBillingSetup, FSCustomerBillingSetup | CBID |  |  |
| PX.Objects.FS.FSCustomerClassBillingSetup | FSCustomerClassBillingSetup | PX_Objects_FS_FSCustomerClassBillingSetup, FSCustomerClassBillingSetup | CBID, CustomerClassID |  |  |
| PX.Objects.FS.FSDetailFSLogAction |  | PX_Objects_FS_FSDetailFSLogAction | LineNbr, RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSDiscountDetail |  | PX_Objects_FS_FSDiscountDetail | EntityType, RefNbr, SrvOrdType | IsOrigDocDiscount |  |
| PX.Objects.FS.FSEmployeeSkill |  | PX_Objects_FS_FSEmployeeSkill | EmployeeID, SkillID | NoteText |  |
| PX.Objects.FS.FSEquipment | Equipment | PX_Objects_FS_FSEquipment, Equipment1, FSEquipment | RefNbr | NoteText, MemDescription, MemReplacedEquipment, MemDescrVehicle, MemDescrAdditionalVehicle1, ReportSMEquipmentID, FixedAssetCD, DeletedDatabaseRecord |  |
| PX.Objects.FS.FSEquipmentComponent | FSEquipmentComponent | PX_Objects_FS_FSEquipmentComponent, FSEquipmentComponent | LineNbr, SMEquipmentID | NoteText |  |
| PX.Objects.FS.FSEquipmentType | Equipment Type | PX_Objects_FS_FSEquipmentType, EquipmentType, FSEquipmentType | EquipmentTypeCD | NoteText |  |
| PX.Objects.FS.FSGenerationLogError | Generation Log Error | PX_Objects_FS_FSGenerationLogError, GenerationLogError, FSGenerationLogError | LogID |  |  |
| PX.Objects.FS.FSGeoZone | Service Area | PX_Objects_FS_FSGeoZone, ServiceArea, FSGeoZone | GeoZoneCD | NoteText |  |
| PX.Objects.FS.FSGeoZoneEmp | Service Area - Employee | PX_Objects_FS_FSGeoZoneEmp, ServiceAreaEmployee, FSGeoZoneEmp | EmployeeID, GeoZoneID | NoteText |  |
| PX.Objects.FS.FSGeoZonePostalCode | Service Area - Postal Code | PX_Objects_FS_FSGeoZonePostalCode, ServiceAreaPostalCode, FSGeoZonePostalCode | GeoZoneID, PostalCode |  |  |
| PX.Objects.FS.FSGPSTrackingLocation |  | PX_Objects_FS_FSGPSTrackingLocation | RequestID |  | yes |
| PX.Objects.FS.FSLicense | License | PX_Objects_FS_FSLicense, License, FSLicense | RefNbr | NoteText |  |
| PX.Objects.FS.FSLicenseType | License Type | PX_Objects_FS_FSLicenseType, LicenseType, FSLicenseType | LicenseTypeCD | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.FS.FSLog | Log | PX_Objects_FS_FSLog, Log1, FSLog | LogID | BillableTimeDurationInt, NoteText, SkipCostCodeValidation, TimeDurationReport |  |
| PX.Objects.FS.FSManufacturer | Manufacturer | PX_Objects_FS_FSManufacturer, Manufacturer, FSManufacturer | ManufacturerCD | LocationID, NoteText, ManufacturerGICD, DeletedDatabaseRecord |  |
| PX.Objects.FS.FSManufacturerModel | Manufacturer Model | PX_Objects_FS_FSManufacturerModel, ManufacturerModel, FSManufacturerModel | ManufacturerID, ManufacturerModelCD | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.FS.FSMasterContract |  | PX_Objects_FS_FSMasterContract | MasterContractCD | NoteText |  |
| PX.Objects.FS.FSModelComponent | Model Warranty | PX_Objects_FS_FSModelComponent, ModelWarranty, FSModelComponent | ComponentID, ModelID | NoteText |  |
| PX.Objects.FS.FSModelTemplateComponent | Model Template Component | PX_Objects_FS_FSModelTemplateComponent, ModelTemplateComponent, FSModelTemplateComponent | ComponentCD, ModelTemplateID | NoteText |  |
| PX.Objects.FS.FSPostBatch | Field Service Billing Batch | PX_Objects_FS_FSPostBatch, FieldServiceBillingBatch, FSPostBatch | BatchNbr |  |  |
| PX.Objects.FS.FSPostDet |  | PX_Objects_FS_FSPostDet | BatchID, PostDetID | PostDocType, PostDocReferenceNbr, INPostDocReferenceNbr, InvoiceRefNbr, InvoiceDocType, InvoiceReferenceNbr, BatchNbr |  |
| PX.Objects.FS.FSPostDoc |  | PX_Objects_FS_FSPostDoc | RecordID | InvtMult |  |
| PX.Objects.FS.FSPostInfo | FSPostInfo | PX_Objects_FS_FSPostInfo, FSPostInfo | PostID | DeletedDatabaseRecord |  |
| PX.Objects.FS.FSPostRegister |  | PX_Objects_FS_FSPostRegister | EntityType, PostedTO, RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSProblem | Problem | PX_Objects_FS_FSProblem, Problem, FSProblem | ProblemCD | NoteText |  |
| PX.Objects.FS.FSProcessIdentity |  | PX_Objects_FS_FSProcessIdentity | ProcessID |  |  |
| PX.Objects.FS.FSQuickProcessParameters |  | PX_Objects_FS_FSQuickProcessParameters | SrvOrdType | GenerateInvoice |  |
| PX.Objects.FS.FSRoom | Room | PX_Objects_FS_FSRoom, Room, FSRoom | BranchLocationID, RecordID | NoteText, CustomRoomID, FormCaptionDescription |  |
| PX.Objects.FS.FSRoute | Route | PX_Objects_FS_FSRoute, Route, FSRoute | RouteCD | NoteText, BeginBranchCD, EndBranchCD, BeginBranchLocationCD, EndBranchLocationCD, MemRouteName, MemRoute, MemRouteDescription |  |
| PX.Objects.FS.FSRouteAppointmentForecasting |  | PX_Objects_FS_FSRouteAppointmentForecasting | ScheduleID, StartDate |  |  |
| PX.Objects.FS.FSRouteContractSchedule |  | PX_Objects_FS_FSRouteContractSchedule | CustomerID, RefNbr |  | yes |
| PX.Objects.FS.FSRouteContractScheduleFSServiceContract |  | PX_Objects_FS_FSRouteContractScheduleFSServiceContract | CustomerID, RefNbr |  |  |
| PX.Objects.FS.FSRouteDocument | Route Document | PX_Objects_FS_FSRouteDocument, RouteDocument, FSRouteDocument | RefNbr | NoteText, FormCaptionDescription, RouteNumberingID, MemActualDuration, MemBusinessDateTime, GPSLatitudeLongitude, MustRecalculateStats, MemAdditionalDriverName, ApproximateValuesLabel |  |
| PX.Objects.FS.FSRouteEmployee |  | PX_Objects_FS_FSRouteEmployee | EmployeeID, RouteID |  |  |
| PX.Objects.FS.FSSalesPrice |  | PX_Objects_FS_FSSalesPrice | InventoryID, ServiceContractID, UOM | NoteText |  |
| PX.Objects.FS.FSSchedule |  | PX_Objects_FS_FSSchedule | CustomerID, RefNbr | NoteText, YearlyLabel, MonthlyLabel, WeeklyLabel, DailyLabel, SrvOrdTypeMessage, ContractDescr, ReportScheduleID, OrigScheduleRefNbr, OrigServiceContractRefNbr, BillCustomerID |  |
| PX.Objects.FS.FSScheduleDet | FSScheduleDet | PX_Objects_FS_FSScheduleDet, FSScheduleDet | LineNbr, ScheduleID | NoteText, SkipCostCodeValidation |  |
| PX.Objects.FS.FSScheduleRoute | FSScheduleRoute | PX_Objects_FS_FSScheduleRoute, FSScheduleRoute | ScheduleID | NoteText |  |
| PX.Objects.FS.FSServiceContract | Service Contract | PX_Objects_FS_FSServiceContract, ServiceContract, FSServiceContract | RefNbr | ClassID, NoteText, ReportServiceContractID, HasSchedule, HasProcessedSchedule, HasForecast, ShowInvoicesTab, UsageBillingCycleID, FormCaptionDescription, OrigServiceContractRefNbr, EmailNotificationCD, DeletedDatabaseRecord |  |
| PX.Objects.FS.FSServiceEquipmentType |  | PX_Objects_FS_FSServiceEquipmentType | EquipmentTypeID, ServiceID |  |  |
| PX.Objects.FS.FSServiceInventoryItem |  | PX_Objects_FS_FSServiceInventoryItem | InventoryID, ServiceID |  |  |
| PX.Objects.FS.FSServiceLicenseType | Service - License Type | PX_Objects_FS_FSServiceLicenseType, ServiceLicenseType, FSServiceLicenseType | LicenseTypeID, ServiceID |  |  |
| PX.Objects.FS.FSServiceOrder | Service Order | PX_Objects_FS_FSServiceOrder, ServiceOrder, FSServiceOrder | RefNbr, SrvOrdType | UserConfirmedClosing, UserConfirmedUnclosing, ProcessReopenAction, ProcessCompleteAction, CompleteAppointments, ProcessCloseAction, CloseAppointments, ProcessCancelAction, CancelAppointments, CompleteActionRunning, CancelActionRunning, ReopenActionRunning, CloseActionRunning, UnCloseActionRunning, NoteText, CuryAppointmentTaxTotal, AppointmentTaxTotal, CuryAppointmentDocTotal, AppointmentDocTotal, CuryEffectiveBillableLineTotal, EffectiveBillableLineTotal, CuryEffectiveLogBillableTranAmountTotal, EffectiveLogBillableTranAmountTotal, CuryEffectiveBillableTaxTotal, EffectiveBillableTaxTotal, CuryEffectiveBillableDocTotal, EffectiveBillableDocTotal, CuryShortLabelEffectiveBillableDocTotal, ShortLabelEffectiveBillableDocTotal, CuryEffectiveCostTotal, EffectiveCostTotal, SOCuryUnpaidBalanace, SOUnpaidBalanace, SOCuryBillableUnpaidBalanace, SOBillableUnpaidBalanace, SOPrepaymentReceived, SOPrepaymentRemaining, SOPrepaymentApplied, ReportLocationID, AppointmentsCompletedCntr, AppointmentsCompletedOrClosedCntr, MemRefNbr, MemAcctName, IsPrepaymentEnable, ShowInvoicesTab, SourceReferenceNbr, CanCreatePurchaseOrder, SLARemaining, CustomerDisplayName, ContactName, ContactPhone, ContactEmail, AssignedEmployeeDisplayName, ServicesRemaining, ServicesCount, BranchLocationDesc, TreeID, Text, Leaf, CustomOrderDate, SkipExternalTaxCalculation, CuryLineDocDiscountTotal, CuryDocDisc, DocDisc, ProfitPercent, ProfitMarginPercent, IsCalledFromQuickProcess, FormCaptionDescription, IsINReleaseProcess, CuryEstimatedBillableTotal, EstimatedBillableTotal, CuryRate |  |
| PX.Objects.FS.FSServiceOrderDiscountDetail |  | PX_Objects_FS_FSServiceOrderDiscountDetail | EntityType, RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSServiceOrderTax | Service Order Tax | PX_Objects_FS_FSServiceOrderTax, ServiceOrderTax, FSServiceOrderTax | LineNbr, RefNbr, SrvOrdType, TaxID | NonDeductibleTaxRate, ExpenseAmt |  |
| PX.Objects.FS.FSServiceOrderTaxTran | Service Order Tax Detail | PX_Objects_FS_FSServiceOrderTaxTran, ServiceOrderTaxDetail, FSServiceOrderTaxTran | RecordID, RefNbr, SrvOrdType, TaxID | NonDeductibleTaxRate, ExpenseAmt, TaxZoneID |  |
| PX.Objects.FS.FSServiceSkill |  | PX_Objects_FS_FSServiceSkill | ServiceID, SkillID |  |  |
| PX.Objects.FS.FSServiceTemplate |  | PX_Objects_FS_FSServiceTemplate | ServiceTemplateCD | NoteText |  |
| PX.Objects.FS.FSServiceTemplateDet | FSServiceTemplateDet | PX_Objects_FS_FSServiceTemplateDet, FSServiceTemplateDet | ServiceTemplateDetID, ServiceTemplateID |  |  |
| PX.Objects.FS.FSServiceVehicleType |  | PX_Objects_FS_FSServiceVehicleType | ServiceID, VehicleTypeID |  |  |
| PX.Objects.FS.FSShippingAddress | Field Service Shipping Address | PX_Objects_FS_FSShippingAddress, FieldServiceShippingAddress, FSShippingAddress | AddressID |  |  |
| PX.Objects.FS.FSShippingContact | Field Service Shipping Contact | PX_Objects_FS_FSShippingContact, FieldServiceShippingContact, FSShippingContact | ContactID |  |  |
| PX.Objects.FS.FSSiteStatusSelected |  | PX_Objects_FS_FSSiteStatusSelected | InventoryID | CuryID, CuryInfoID, QtySelected, DurationSelected, CuryUnitPrice, DropShipCuryUnitPrice, CuryRate, CuryViewState |  |
| PX.Objects.FS.FSSkill | Skill | PX_Objects_FS_FSSkill, Skill, FSSkill | SkillCD | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.FS.FSSODet | Service Order Item Detail | PX_Objects_FS_FSSODet, ServiceOrderItemDetail, FSSODet | LineNbr, RefNbr, SrvOrdType | Behavior, TranType, SOLineType, IsStockItem, IsKit, OrderQty, BaseOrderQty, DeductQty, BaseDeductQty, RequireShipping, RequireAllocation, RequireLocation, LineQtyAvail, LineQtyHardAvail, NoteText, EnableUnlinkPO, CuryExtPrice, CuryLineAmt, SkipCostCodeValidation, EstimatedDurationReport, TabOrigin, SkipUnitPriceCalc, AlreadyCalculatedUnitPrice, IsTravelItem, EnableStaffID, InventoryIDReport, LinkedDisplayRefNbr |  |
| PX.Objects.FS.FSSODetEmployee | Service Order Item Detail | PX_Objects_FS_FSSODetEmployee | LineNbr, RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSSODetFSSODetSplit |  | PX_Objects_FS_FSSODetFSSODetSplit | LineNbr, RefNbr, SplitLineNbr, SrvOrdType |  |  |
| PX.Objects.FS.FSSODetSplit | Service Order Lot/Serial Detail | PX_Objects_FS_FSSODetSplit, ServiceOrderLotSerialDetail, FSSODetSplit | LineNbr, RefNbr, SplitLineNbr, SrvOrdType | IsMergeable, LotSerClassID, AssignedNbr, UnreceivedQty, BaseUnreceivedQty, OpenQty, BaseOpenQty, TranType, RequireShipping, RequireAllocation, RequireLocation, ProjectID, TaskID, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.FS.FSSOEmployee | FSSOEmployee | PX_Objects_FS_FSSOEmployee, FSSOEmployee | LineNbr, RefNbr, SrvOrdType | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.FS.FSSOResource | FSSOResource | PX_Objects_FS_FSSOResource, FSSOResource | RefNbr, SMEquipmentID, SrvOrdType |  |  |
| PX.Objects.FS.FSSrvOrdQuickProcessParams |  | PX_Objects_FS_FSSrvOrdQuickProcessParams | OrderType |  | yes |
| PX.Objects.FS.FSSrvOrdType | Order Type | PX_Objects_FS_FSSrvOrdType, OrderType, FSSrvOrdType | SrvOrdType | NoteText, ShowQuickProcessTab, PostToSOSIPM, AllowInventoryItems |  |
| PX.Objects.FS.FSSrvOrdTypeProblem |  | PX_Objects_FS_FSSrvOrdTypeProblem | ProblemID, SrvOrdType |  |  |
| PX.Objects.FS.FSStaffSchedule |  | PX_Objects_FS_FSStaffSchedule | CustomerID, RefNbr |  |  |
| PX.Objects.FS.FSTimeSlot |  | PX_Objects_FS_FSTimeSlot | TimeSlotID | CustomID, CustomDateID, WrkEmployeeScheduleID, BranchLocationDesc, BranchLocationCD, CustomDateTimeStart, CustomDateTimeEnd, NoteText |  |
| PX.Objects.FS.FSVehicle | Equipment | PX_Objects_FS_FSVehicle | RefNbr |  |  |
| PX.Objects.FS.FSVehicleType | Vehicle Type | PX_Objects_FS_FSVehicleType, VehicleType, FSVehicleType | VehicleTypeCD | NoteText, VehicleTypeGICD |  |
| PX.Objects.FS.FSWeekCodeDate | Contracts/Routes calendar Week Code | PX_Objects_FS_FSWeekCodeDate, ContractsRoutescalendarWeekCode, FSWeekCodeDate | WeekCodeDate |  |  |
| PX.Objects.FS.FSWFStage | Order Stage | PX_Objects_FS_FSWFStage, OrderStage, FSWFStage | ParentWFStageID, WFID, WFStageCD | NoteText |  |
| PX.Objects.FS.FSWrkProcess | FSWrkProcess | PX_Objects_FS_FSWrkProcess, FSWrkProcess | ProcessID |  |  |
| PX.Objects.FS.InventoryPostingBatchDetail |  | PX_Objects_FS_InventoryPostingBatchDetail | AppointmentRefNbr, BatchID, SrvOrdType |  |  |
| PX.Objects.FS.LicenseTypeGridFilter | License Type | PX_Objects_FS_LicenseTypeGridFilter | LicenseTypeCD |  |  |
| PX.Objects.FS.POEnabledFSSODet | Service Order Item Detail | PX_Objects_FS_POEnabledFSSODet | LineNbr, RefNbr, SrvOrdType | PONbrCreated |  |
| PX.Objects.FS.PostingBatchDetail |  | PX_Objects_FS_PostingBatchDetail | AppointmentRefNbr, BatchID, SrvOrdType | SOPosted, SOOrderType, SOOrderNbr, SOLineNbr, ARPosted, ARDocType, ARRefNbr, ARLineNbr, APPosted, APDocType, APRefNbr, APLineNbr, INPosted, INDocType, INRefNbr, INLineNbr, SOInvPosted, SOInvDocType, SOInvRefNbr, SOInvLineNbr, PMPosted, PMDocType, PMRefNbr, PMTranID, AcctName, InvoiceRefNbr |  |
| PX.Objects.FS.RelatedServiceOrder | Service Order | PX_Objects_FS_RelatedServiceOrder | RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.RouteAppointmentInfo | Appointment | PX_Objects_FS_RouteAppointmentInfo | RefNbr, SrvOrdType |  |  |
| PX.Objects.FS.SchedulerAppointment | Appointment | PX_Objects_FS_SchedulerAppointment, Appointment1, SchedulerAppointment | RefNbr, SrvOrdType | Locked |  |
| PX.Objects.FS.SchedulerEmployeeInventoryItem | Employee Inventory Item | PX_Objects_FS_SchedulerEmployeeInventoryItem, EmployeeInventoryItem, SchedulerEmployeeInventoryItem | InventoryID |  |  |
| PX.Objects.FS.SchedulerServiceOrder | Service Order | PX_Objects_FS_SchedulerServiceOrder, ServiceOrder1, SchedulerServiceOrder | BranchCD, BranchLocationCD, CustomerAcctCD, ProblemCD, ServiceContractRefNbr, SrvOrdType | FullAddress |  |
| PX.Objects.FS.ServiceOrderComponentField |  | PX_Objects_FS_ServiceOrderComponentField | ComponentType, FieldName, ObjectName |  |  |
| PX.Objects.FS.ServiceOrderToPost | Service Order | PX_Objects_FS_ServiceOrderToPost | RefNbr, SrvOrdType | AppointmentID, RowIndex, GroupKey, BatchID, ErrorFlag |  |
| PX.Objects.FS.SkillGridFilter | Skill | PX_Objects_FS_SkillGridFilter | SkillCD |  |  |
| PX.Objects.FS.SoldInventoryItem |  | PX_Objects_FS_SoldInventoryItem | DocType, InvoiceLineNbr, InvoiceRefNbr, SOLineSplitNumber |  |  |
| PX.Objects.FS.SOOrderTypeQuickProcess | Order Type | PX_Objects_FS_SOOrderTypeQuickProcess | OrderType |  |  |
| PX.Objects.FS.UnassignedAppComponentField |  | PX_Objects_FS_UnassignedAppComponentField | ComponentType, FieldName, ObjectName |  |  |
| PX.Objects.GDPR.SMPersonalDataLog |  | PX_Objects_GDPR_SMPersonalDataLog | LogID | UIKey |  |
| PX.Objects.GL.Account | GL Account | PX_Objects_GL_Account, GLAccount, Account | AccountCD | NoteText, TypeTotal, ReadableActive, TransactionsForGivenCurrencyExists, Included, Secured, DeletedDatabaseRecord |  |
| PX.Objects.GL.AccountClass | GL Account Class | PX_Objects_GL_AccountClass, GLAccountClass, AccountClass | AccountClassID | NoteText |  |
| PX.Objects.GL.AdjustedBranch | Branch | PX_Objects_GL_AdjustedBranch | BranchCD |  |  |
| PX.Objects.GL.AdjustingBranch | Branch | PX_Objects_GL_AdjustingBranch | BranchCD |  |  |
| PX.Objects.GL.ADL.Batch |  | PX_Objects_GL_ADL_Batch | BatchNbr, Module | DeletedDatabaseRecord |  |
| PX.Objects.GL.ADL.Sub |  | PX_Objects_GL_ADL_Sub | SubCD | Secured, DeletedDatabaseRecord |  |
| PX.Objects.GL.Batch | GL Batch | PX_Objects_GL_Batch, GLBatch, Batch | BatchNbr, Module | NoteText, ReverseCount, HasRamainingAmount, ReleasedToVerify, PostedToVerify, ApproverID, ApproverWorkgroupID, CuryRate, CuryViewState, DeletedDatabaseRecord |  |
| PX.Objects.GL.BatchPostedForModule | GL Batch | PX_Objects_GL_BatchPostedForModule | BatchNbr, Module |  |  |
| PX.Objects.GL.BatchReport | GL Batch | PX_Objects_GL_BatchReport | BatchNbr, Module |  |  |
| PX.Objects.GL.Branch | Branch | PX_Objects_GL_Branch, Branch | BranchCD | BranchOrOrganizationLogoNameReport, LedgerCD, Included, Secured, DeletedDatabaseRecord |  |
| PX.Objects.GL.BranchAcctMapFrom | Branch Account Map From | PX_Objects_GL_BranchAcctMapFrom, BranchAccountMapFrom, BranchAcctMapFrom | BranchID, LineNbr |  |  |
| PX.Objects.GL.BranchAcctMapTo | Branch Account Map To | PX_Objects_GL_BranchAcctMapTo, BranchAccountMapTo, BranchAcctMapTo | BranchID, LineNbr |  |  |
| PX.Objects.GL.CAExpenseBranch | Branch | PX_Objects_GL_CAExpenseBranch | BranchCD |  |  |
| PX.Objects.GL.CashAccountBranch | Branch | PX_Objects_GL_CashAccountBranch | BranchCD |  |  |
| PX.Objects.GL.CASplitBranch | Branch | PX_Objects_GL_CASplitBranch | BranchCD |  |  |
| PX.Objects.GL.CurrentBranch | Current Branch | PX_Objects_GL_CurrentBranch, CurrentBranch | BranchCD |  |  |
| PX.Objects.GL.DAC.Organization | Company | PX_Objects_GL_DAC_Organization, Company2, Organization | OrganizationCD | ActualLedgerCD, PrimaryColor, BackgroundColor, LogoNameGetter, LogoNameReportGetter, Included, NoteText, Secured, DeletedDatabaseRecord |  |
| PX.Objects.GL.DAC.OrganizationLedgerLink |  | PX_Objects_GL_DAC_OrganizationLedgerLink | LedgerID, OrganizationID |  |  |
| PX.Objects.GL.DAC.Standalone.OrganizationAlias | Company | PX_Objects_GL_DAC_Standalone_OrganizationAlias, Company3, OrganizationAlias | OrganizationCD |  |  |
| PX.Objects.GL.FinPeriods.MasterFinPeriod |  | PX_Objects_GL_FinPeriods_MasterFinPeriod | FinPeriodID | StartDateUI, EndDateUI, Length, IsAdjustment |  |
| PX.Objects.GL.FinPeriods.MasterFinYear |  | PX_Objects_GL_FinPeriods_MasterFinYear | Year |  |  |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriod |  | PX_Objects_GL_FinPeriods_OrganizationFinPeriod | FinPeriodID, OrganizationID | StartDateUI, EndDateUI, Length, IsAdjustment |  |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodAlias |  | PX_Objects_GL_FinPeriods_OrganizationFinPeriodAlias | FinPeriodID, OrganizationID |  |  |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodCurrent | Last FinPeriod Current | PX_Objects_GL_FinPeriods_OrganizationFinPeriodCurrent, LastFinPeriodCurrent, OrganizationFinPeriodCurrent | FinPeriodID, OrganizationID, PrevFinPeriodID |  |  |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodExt | Last FinPeriod | PX_Objects_GL_FinPeriods_OrganizationFinPeriodExt, LastFinPeriod, OrganizationFinPeriodExt | FinPeriodID, OrganizationID, PrevFinPeriodID |  |  |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodMin | Min FinPeriod Current | PX_Objects_GL_FinPeriods_OrganizationFinPeriodMin, MinFinPeriodCurrent, OrganizationFinPeriodMin | FinPeriodID, OrganizationID |  |  |
| PX.Objects.GL.FinPeriods.OrganizationFinPeriodStatus |  | PX_Objects_GL_FinPeriods_OrganizationFinPeriodStatus | FinPeriodID, OrganizationID |  |  |
| PX.Objects.GL.FinPeriods.OrganizationFinYear | Company Financial Period | PX_Objects_GL_FinPeriods_OrganizationFinYear, CompanyFinancialPeriod, OrganizationFinYear | OrganizationID, Year |  |  |
| PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod | Financial Period | PX_Objects_GL_FinPeriods_TableDefinition_FinPeriod, FinancialPeriod, FinPeriod | FinPeriodID, OrganizationID | StartDateUI, EndDateUI, Length, NoteText |  |
| PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod2 | Financial Period | PX_Objects_GL_FinPeriods_TableDefinition_FinPeriod2 | FinPeriodID, OrganizationID |  |  |
| PX.Objects.GL.FinPeriods.TableDefinition.FinYear |  | PX_Objects_GL_FinPeriods_TableDefinition_FinYear | OrganizationID, Year | NoteText |  |
| PX.Objects.GL.FinPeriodSetup | Financial Period Template | PX_Objects_GL_FinPeriodSetup, FinancialPeriodTemplate, FinPeriodSetup | PeriodNbr | StartDateUI, EndDateUI, NoteText |  |
| PX.Objects.GL.GLAllocation | Allocation | PX_Objects_GL_GLAllocation, Allocation, GLAllocation | GLAllocationID | OrganizationID, AllocLedgerBalanceType, AllocLedgerBaseCuryID, NoteText |  |
| PX.Objects.GL.GLAllocationAccountHistory | GL Allocation History for Account | PX_Objects_GL_GLAllocationAccountHistory, GLAllocationHistoryforAccount, GLAllocationAccountHistory | AccountID, BatchNbr, BranchID, Module, SubID |  |  |
| PX.Objects.GL.GLAllocationDestination | GL Allocation Destination | PX_Objects_GL_GLAllocationDestination, GLAllocationDestination | GLAllocationID, LineID |  |  |
| PX.Objects.GL.GLAllocationHistory | GL Allocation History | PX_Objects_GL_GLAllocationHistory, GLAllocationHistory | BatchNbr, GLAllocationID, Module |  |  |
| PX.Objects.GL.GLAllocationSource | GL Allocation Source | PX_Objects_GL_GLAllocationSource, GLAllocationSource | GLAllocationID, LineID |  |  |
| PX.Objects.GL.GLBudget | Budget | PX_Objects_GL_GLBudget, Budget, GLBudget | BranchID, FinYear, LedgerID |  |  |
| PX.Objects.GL.GLBudgetLine | Budget Article | PX_Objects_GL_GLBudgetLine, BudgetArticle, GLBudgetLine | BranchID, FinYear, GroupID, LedgerID | Comparison, NoteText, SortOrder, IsRolledUp, Secured |  |
| PX.Objects.GL.GLBudgetLineDetail | GL Budget Line Detail | PX_Objects_GL_GLBudgetLineDetail, GLBudgetLineDetail | BranchID, FinPeriodID, FinYear, GroupID, LedgerID |  |  |
| PX.Objects.GL.GLBudgetTree | GL Budget Tree | PX_Objects_GL_GLBudgetTree, GLBudgetTree | GroupID | Secured, Included |  |
| PX.Objects.GL.GLConsolAccount | GL Consolidation Account | PX_Objects_GL_GLConsolAccount, GLConsolidationAccount, GLConsolAccount | AccountCD |  |  |
| PX.Objects.GL.GLConsolBranch | GL Consolidation Branch | PX_Objects_GL_GLConsolBranch, GLConsolidationBranch, GLConsolBranch | BranchCD, SetupID | DisplayName |  |
| PX.Objects.GL.GLConsolData | GL Consolidation Data | PX_Objects_GL_GLConsolData, GLConsolidationData, GLConsolData | AccountCD, FinPeriodID, MappedValue | FinPeriodID |  |
| PX.Objects.GL.GLConsolLedger | GL Consolidation Ledger | PX_Objects_GL_GLConsolLedger, GLConsolidationLedger, GLConsolLedger | LedgerCD, SetupID |  |  |
| PX.Objects.GL.GLConsolLedger2 |  | PX_Objects_GL_GLConsolLedger2 | LedgerCD, SetupID |  |  |
| PX.Objects.GL.GLConsolSetup | GL Consolidation Setup | PX_Objects_GL_GLConsolSetup, GLConsolidationSetup, GLConsolSetup | SetupID |  |  |
| PX.Objects.GL.GLDocBatch | GL Document Batch | PX_Objects_GL_GLDocBatch, GLDocumentBatch, GLDocBatch | BatchNbr, Module | NoteText, CuryRate, CuryViewState |  |
| PX.Objects.GL.GLHistory | GL History | PX_Objects_GL_GLHistory, GLHistory | AccountID, BranchID, FinPeriodID, LedgerID, SubID | FinFlag, REFlag, PtdCredit, PtdDebit, YtdBalance, BegBalance, PtdRevalued, CuryPtdCredit, CuryPtdDebit, CuryYtdBalance, CuryBegBalance |  |
| PX.Objects.GL.GLHistoryByCurrentPeriod | GL History by Period | PX_Objects_GL_GLHistoryByCurrentPeriod, GLHistorybyPeriod1, GLHistoryByCurrentPeriod | AccountID, BranchID, FinPeriodID, LedgerID, SubID | FinYear |  |
| PX.Objects.GL.GLHistoryByPeriod | GL History by Period | PX_Objects_GL_GLHistoryByPeriod, GLHistorybyPeriod2 | AccountID, BranchID, FinPeriodID, LedgerID, SubID | FinYear |  |
| PX.Objects.GL.GLHistoryByPeriodCurrent | GL History by Period | PX_Objects_GL_GLHistoryByPeriodCurrent, GLHistorybyPeriod3, GLHistoryByPeriodCurrent | AccountID, BranchID, FinPeriodID, LedgerID, SubID | FinYear |  |
| PX.Objects.GL.GLHistoryByPeriodMasterCurrent | GL History by Period | PX_Objects_GL_GLHistoryByPeriodMasterCurrent, GLHistorybyPeriod4, GLHistoryByPeriodMasterCurrent | AccountID, BranchID, FinPeriodID, LedgerID, SubID | FinYear |  |
| PX.Objects.GL.GLHistoryLastRevaluation |  | PX_Objects_GL_GLHistoryLastRevaluation | AccountID, BranchID, LedgerID, SubID |  |  |
| PX.Objects.GL.GLHistorySummary | GLHistory Summary | PX_Objects_GL_GLHistorySummary, GLHistorySummary | AccountID, BranchID, LedgerID, SubID |  |  |
| PX.Objects.GL.GLSetupApproval | GL Approval Preferences | PX_Objects_GL_GLSetupApproval, GLApprovalPreferences, GLSetupApproval | ApprovalID |  |  |
| PX.Objects.GL.GLTax | GL Tax Detail | PX_Objects_GL_GLTax, GLTaxDetail, GLTax | BatchNbr, DetailType, LineNbr, Module, TaxID | NonDeductibleTaxRate, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.GL.GLTaxTran | GL Tax Transaction | PX_Objects_GL_GLTaxTran, GLTaxTransaction, GLTaxTran | BatchNbr, DetailType, LineNbr, Module, TaxID |  |  |
| PX.Objects.GL.GLTran | GL Transaction | PX_Objects_GL_GLTran, GLTransaction, GLTran | BatchNbr, LineNbr, Module | IncludedInReclassHistory, ZeroPost, PostYear, TranYear, NextPostYear, NextTranYear, LedgerBalanceType, AccountRequireUnits, NoteText, SkipNormalizeAmounts, MLFinPeriodID, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.GL.GLTranCode | GL Transaction Code | PX_Objects_GL_GLTranCode, GLTransactionCode, GLTranCode | Module, TranType |  |  |
| PX.Objects.GL.GLTranDoc | Journal Voucher | PX_Objects_GL_GLTranDoc, JournalVoucher, GLTranDoc | BatchNbr, LineNbr, Module | ImportRefNbr, LedgerBalanceType, NoteText, CuryBalanceAmt, GroupTranID, CashAccountID, CuryDocTotal, DocTotal, CuryTaxTotal, CuryUnappliedBal, UnappliedBal, CuryDiscBal, DiscBal, CuryWhTaxBal, WhTaxBal, NeedsDebitCashAccount, IsARCustomerCashAccount, NeedsCreditCashAccount, NeedTaskValidation, CuryRate, CuryViewState |  |
| PX.Objects.GL.GLTranR | GL Transaction | PX_Objects_GL_GLTranR | BatchNbr, LineNbr, Module | BegBalance, EndBalance, CuryBegBalance, CuryEndBalance, SignBegBalance, SignEndBalance, SignCuryBegBalance, SignCuryEndBalance, Type, BatchType |  |
| PX.Objects.GL.GLTrialBalanceImportDetails | Trial Balance Import Details | PX_Objects_GL_GLTrialBalanceImportDetails, TrialBalanceImportDetails, GLTrialBalanceImportDetails | Line, MapNumber | Description, AccountType, AccountCuryID |  |
| PX.Objects.GL.GLTrialBalanceImportMap | Trial Balance Import | PX_Objects_GL_GLTrialBalanceImportMap, TrialBalanceImport, GLTrialBalanceImportMap | Number | OrganizationID, IsEditable, NoteText |  |
| PX.Objects.GL.INSiteTo | Warehouse | PX_Objects_GL_INSiteTo | SiteCD |  |  |
| PX.Objects.GL.INSiteToBranch | Branch | PX_Objects_GL_INSiteToBranch | BranchCD |  |  |
| PX.Objects.GL.Ledger | Ledger | PX_Objects_GL_Ledger, Ledger | LedgerCD | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.GL.Overrides.ScheduleMaint.BatchSelection | Batch to Process | PX_Objects_GL_Overrides_ScheduleMaint_BatchSelection, BatchtoProcess, BatchSelection | BatchNbr, Module |  |  |
| PX.Objects.GL.Overrides.ScheduleProcess.BatchNew | GL Batch New | PX_Objects_GL_Overrides_ScheduleProcess_BatchNew, GLBatchNew, BatchNew | BatchNbr, Module |  | yes |
| PX.Objects.GL.Overrides.ScheduleProcess.GLTranNew | GL Transaction | PX_Objects_GL_Overrides_ScheduleProcess_GLTranNew | BatchNbr, LineNbr, Module | RefBatchNbr |  |
| PX.Objects.GL.ReclassBatch | GL Batch | PX_Objects_GL_ReclassBatch | BatchNbr, Module |  |  |
| PX.Objects.GL.Reclassification.Common.GLTranForReclassification | GL Transaction | PX_Objects_GL_Reclassification_Common_GLTranForReclassification | BatchNbr, LineNbr, Module |  | yes |
| PX.Objects.GL.Reclassification.UI.GLTranReclHist | GL Transaction | PX_Objects_GL_Reclassification_UI_GLTranReclHist | BatchNbr, LineNbr, Module |  | yes |
| PX.Objects.GL.ReclassifyingGLTranAggregate |  | PX_Objects_GL_ReclassifyingGLTranAggregate | BatchNbr, LineNbr, Module |  |  |
| PX.Objects.GL.Schedule | Schedule | PX_Objects_GL_Schedule, Schedule | ScheduleID | FormScheduleType, NoteText, Days, Weeks, Months, Periods |  |
| PX.Objects.GL.Standalone.LedgerAlias | Ledger | PX_Objects_GL_Standalone_LedgerAlias, Ledger1, LedgerAlias | LedgerCD |  |  |
| PX.Objects.GL.Sub | Subaccount | PX_Objects_GL_Sub, Subaccount, Sub | SubCD | NoteText, Included, Secured, DeletedDatabaseRecord |  |
| PX.Objects.GL.TranBranch | Branch | PX_Objects_GL_TranBranch | BranchCD |  |  |
| PX.Objects.GL.TranINSite | Warehouse | PX_Objects_GL_TranINSite | SiteCD |  |  |
| PX.Objects.GL.TranINSiteBranch | Branch | PX_Objects_GL_TranINSiteBranch | BranchCD |  |  |
| PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial | Adjustment Transactions grouped by SiteLotSerial | PX_Objects_IN_AffectedAvailability_AdjustmentTranBySiteLotSerial, AdjustmentTransactionsgroupedbySiteLotSerial, AdjustmentTranBySiteLotSerial | DocType, InventoryID, LotSerialNbr, RefNbr, SiteID |  |  |
| PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus | Adjustment Transactions grouped by SiteStatus | PX_Objects_IN_AffectedAvailability_AdjustmentTranBySiteStatus, AdjustmentTransactionsgroupedbySiteStatus, AdjustmentTranBySiteStatus | DocType, InventoryID, RefNbr, SiteID |  |  |
| PX.Objects.IN.DAC.INConversionHistory | Inventory Conversion History | PX_Objects_IN_DAC_INConversionHistory, InventoryConversionHistory, INConversionHistory | HistoryID |  |  |
| PX.Objects.IN.DAC.INItemClassSite | Warehouse Item Class Details | PX_Objects_IN_DAC_INItemClassSite, WarehouseItemClassDetails, INItemClassSite | ItemClassID, SiteID | NoteText |  |
| PX.Objects.IN.DAC.INItemLotSerialAttributesHeader | INItemLotSerialAttributesHeader | PX_Objects_IN_DAC_INItemLotSerialAttributesHeader, INItemLotSerialAttributesHeader | InventoryID, LotSerialNbr | NoteText |  |
| PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings | INItemLotSerialAttributesHeaderCurySettings | PX_Objects_IN_DAC_INItemLotSerialAttributesHeaderCurySettings, INItemLotSerialAttributesHeaderCurySettings | CuryID, InventoryID, LotSerialNbr |  |  |
| PX.Objects.IN.DAC.INRegisterCart | Receipt Cart | PX_Objects_IN_DAC_INRegisterCart, ReceiptCart, INRegisterCart | CartID, DocType, RefNbr, SiteID |  |  |
| PX.Objects.IN.DAC.INRegisterCartLine | Receipt Cart Line | PX_Objects_IN_DAC_INRegisterCartLine, ReceiptCartLine, INRegisterCartLine | CartID, DocType, LineNbr, RefNbr, SiteID |  |  |
| PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader | INRegisterItemLotSerialAttributesHeader | PX_Objects_IN_DAC_INRegisterItemLotSerialAttributesHeader, INRegisterItemLotSerialAttributesHeader | DocType, InventoryID, LotSerialNbr, RefNbr | NoteText |  |
| PX.Objects.IN.DAC.INSetupApproval | IN Approval | PX_Objects_IN_DAC_INSetupApproval, INApproval, INSetupApproval | ApprovalID |  |  |
| PX.Objects.IN.DAC.INSitePlanningStrategy | Warehouse Planning Strategy | PX_Objects_IN_DAC_INSitePlanningStrategy, WarehousePlanningStrategy, INSitePlanningStrategy | PlanningStrategyID | NoteText |  |
| PX.Objects.IN.DAC.INSitePlanningStrategyDetail | Warehouse Planning Strategy Detail | PX_Objects_IN_DAC_INSitePlanningStrategyDetail, WarehousePlanningStrategyDetail, INSitePlanningStrategyDetail | LineNbr, PlanningStrategyID | NoteText |  |
| PX.Objects.IN.DAC.INSiteZone | Warehouse Zone | PX_Objects_IN_DAC_INSiteZone, WarehouseZone, INSiteZone | ZoneID | NoteText |  |
| PX.Objects.IN.DAC.INTransferDemandLine | Transfer Demand Line | PX_Objects_IN_DAC_INTransferDemandLine, TransferDemandLine, INTransferDemandLine | RecordID | InventoryDescr, UnitOfHandling, BaseUOM, NoteText |  |
| PX.Objects.IN.DAC.INTransferDemandPutAwaySplit | Transfer Demand Put Away Split | PX_Objects_IN_DAC_INTransferDemandPutAwaySplit, TransferDemandPutAwaySplit, INTransferDemandPutAwaySplit | SplitLineNbr, TransferDemandLineID | NoteText |  |
| PX.Objects.IN.DAC.INTransferList | Transfer List | PX_Objects_IN_DAC_INTransferList, TransferList, INTransferList | ListNbr |  |  |
| PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected | INItemLotSerialAttributesHeaderSelected | PX_Objects_IN_DAC_Projections_INItemLotSerialAttributesHeaderSelected, INItemLotSerialAttributesHeaderSelected | InventoryID, LocationID, LotSerialNbr, SiteID | QtySelected |  |
| PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType | IN Location Status by Cost Layer Type | PX_Objects_IN_DAC_Projections_INLocationStatusByCostLayerType, INLocationStatusbyCostLayerType | CostLayerType, InventoryID, LocationID, SiteID, SubItemID |  |  |
| PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType | IN Lot/Serial Cost Status by Cost Layer Type | PX_Objects_IN_DAC_Projections_INLotSerialCostStatusByCostLayerType, INLotSerialCostStatusbyCostLayerType | CostLayerType, InventoryID, LotSerialNbr, SiteID, SubItemID | UnitCost |  |
| PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType | IN Lot/Serial Status by Cost Layer Type | PX_Objects_IN_DAC_Projections_INLotSerialStatusByCostLayerType, INLotSerialStatusbyCostLayerType | CostLayerType, InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID |  |  |
| PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType | IN Site Cost Status by Cost Layer Type | PX_Objects_IN_DAC_Projections_INSiteCostStatusByCostLayerType, INSiteCostStatusbyCostLayerType | CostLayerType, InventoryID, SiteID, SubItemID | UnitCost |  |
| PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType | IN Site Status by Cost Layer Type | PX_Objects_IN_DAC_Projections_INSiteStatusByCostLayerType, INSiteStatusbyCostLayerType | CostLayerType, InventoryID, SiteID, SubItemID |  |  |
| PX.Objects.IN.DAC.WarehouseReference |  | PX_Objects_IN_DAC_WarehouseReference | PortalSetupID, SiteID |  |  |
| PX.Objects.IN.INABCCode | IN ABC Code | PX_Objects_IN_INABCCode, INABCCode | ABCCodeID |  |  |
| PX.Objects.IN.INAvailabilityScheme | Availability Calculation Rule | PX_Objects_IN_INAvailabilityScheme, AvailabilityCalculationRule, INAvailabilityScheme | AvailabilitySchemeID |  |  |
| PX.Objects.IN.INCart | IN Cart | PX_Objects_IN_INCart, INCart | CartCD, SiteID | NoteText |  |
| PX.Objects.IN.INCartContentByLocation | IN Cart Content by Location | PX_Objects_IN_INCartContentByLocation, INCartContentbyLocation | InventoryID, LocationID, SiteID, SubItemID |  |  |
| PX.Objects.IN.INCartContentByLotSerial | IN Cart Content by Lot/Serial Nbr. | PX_Objects_IN_INCartContentByLotSerial, INCartContentbyLotSerialNbr, INCartContentByLotSerial | InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID |  |  |
| PX.Objects.IN.INCartSplit | IN Cart Split | PX_Objects_IN_INCartSplit, INCartSplit | CartID, SiteID, SplitLineNbr |  |  |
| PX.Objects.IN.INCategory | Item Sales Category | PX_Objects_IN_INCategory, ItemSalesCategory, INCategory | CategoryID | TempChildID, TempParentID, NoteText |  |
| PX.Objects.IN.INComponent | Deferred Revenue Components | PX_Objects_IN_INComponent, DeferredRevenueComponents, INComponent | ComponentID, InventoryID |  |  |
| PX.Objects.IN.INComponentTran | IN Component | PX_Objects_IN_INComponentTran, INComponent1, INComponentTran | DocType, LineNbr, RefNbr |  |  |
| PX.Objects.IN.INComponentTranSplit | IN Component Split | PX_Objects_IN_INComponentTranSplit, INComponentSplit, INComponentTranSplit | DocType, LineNbr, RefNbr, SplitLineNbr |  |  |
| PX.Objects.IN.INCostCenter | IN Cost Center | PX_Objects_IN_INCostCenter, INCostCenter | CostCenterID |  |  |
| PX.Objects.IN.INCostStatus | IN Cost Status | PX_Objects_IN_INCostStatus, INCostStatus | CostID | OrigQtyOnHand, OverrideOrigQty, PositiveTranQty |  |
| PX.Objects.IN.INCostStatusSummary | IN Cost Status Summary | PX_Objects_IN_INCostStatusSummary, INCostStatusSummary | CostID |  |  |
| PX.Objects.IN.INCostStatusTransitLineSummary | IN Cost Status | PX_Objects_IN_INCostStatusTransitLineSummary | CostID |  |  |
| PX.Objects.IN.INCostSubItemXRef |  | PX_Objects_IN_INCostSubItemXRef | CostSubItemID, SubItemID |  |  |
| PX.Objects.IN.INItemBox | IN Item Box | PX_Objects_IN_INItemBox, INItemBox | BoxID, InventoryID | MaxQty, NoteText |  |
| PX.Objects.IN.INItemBoxEx | IN Item Box | PX_Objects_IN_INItemBoxEx | BoxID, InventoryID |  |  |
| PX.Objects.IN.INItemCategory | Item Sales Category by Item | PX_Objects_IN_INItemCategory, ItemSalesCategorybyItem, INItemCategory | CategoryID, InventoryID | CategorySelected |  |
| PX.Objects.IN.INItemClass | Item Class | PX_Objects_IN_INItemClass, ItemClass, INItemClass | ItemClassCD | ParentItemClassID, NoteText, Included, ItemClassStrID, ItemClassCDWildcard, SampleID, SampleDescription, Secured, DeletedDatabaseRecord |  |
| PX.Objects.IN.INItemClassCurySettings | Item Class Currency Settings | PX_Objects_IN_INItemClassCurySettings, ItemClassCurrencySettings, INItemClassCurySettings | CuryID, ItemClassID |  |  |
| PX.Objects.IN.INItemClassRep | Item Class Replenishment | PX_Objects_IN_INItemClassRep, ItemClassReplenishment, INItemClassRep | CuryID, ItemClassID, ReplenishmentClassID | ServiceLevelPct |  |
| PX.Objects.IN.INItemCost | Item Cost Statistics | PX_Objects_IN_INItemCost, ItemCostStatistics, INItemCost | CuryID, InventoryID |  |  |
| PX.Objects.IN.INItemCostHist | IN Item Cost History | PX_Objects_IN_INItemCostHist, INItemCostHistory, INItemCostHist | AccountID, CostSiteID, CostSubItemID, FinPeriodID, InventoryID, SubID |  |  |
| PX.Objects.IN.INItemCostHistByPeriod | IN Item Cost History by Period | PX_Objects_IN_INItemCostHistByPeriod, INItemCostHistorybyPeriod, INItemCostHistByPeriod | AccountID, CostSiteID, CostSubItemID, FinPeriodID, InventoryID, SubID |  |  |
| PX.Objects.IN.INItemLotSerial | Lot/Serial by Item | PX_Objects_IN_INItemLotSerial, LotSerialbyItem, INItemLotSerial | InventoryID, LotSerialNbr | UpdateExpireDate, NoteText |  |
| PX.Objects.IN.INItemLotSerialAttribute | Inventory Item Lot/Serial Attribute | PX_Objects_IN_INItemLotSerialAttribute, InventoryItemLotSerialAttribute, INItemLotSerialAttribute | AttributeID, InventoryID | LotSerialNbr |  |
| PX.Objects.IN.INItemPlan | IN Item Plan | PX_Objects_IN_INItemPlan, INItemPlan | PlanID | Active, IsTempLotSerial, IsSkippedWhenBackOrdered, IsTemporary |  |
| PX.Objects.IN.INItemRep | Item Replenishment Settings | PX_Objects_IN_INItemRep, ItemReplenishmentSettings, INItemRep | CuryID, InventoryID, ReplenishmentClassID | ServiceLevelPct |  |
| PX.Objects.IN.INItemSalesHist | Item Sales History | PX_Objects_IN_INItemSalesHist, ItemSalesHistory, INItemSalesHist | CostSiteID, CostSubItemID, FinPeriodID, InventoryID |  |  |
| PX.Objects.IN.INItemSite | Item/Warehouse Settings | PX_Objects_IN_INItemSite, ItemWarehouseSettings, INItemSite | InventoryID, SiteID | LastCostDate, IsDefault, NoteText, ServiceLevelPct, DemandPerDaySTDEV, LeadTimeSTDEV |  |
| PX.Objects.IN.INItemSiteHist | IN Item Site History | PX_Objects_IN_INItemSiteHist, INItemSiteHistory, INItemSiteHist | FinPeriodID, InventoryID, LocationID, SiteID, SubItemID | LastActivityPeriod |  |
| PX.Objects.IN.INItemSiteHistByDay | IN Item Site History by Day | PX_Objects_IN_INItemSiteHistByDay, INItemSiteHistorybyDay, INItemSiteHistByDay | Date, InventoryID, LocationID, SiteID, SubItemID |  |  |
| PX.Objects.IN.INItemSiteHistByLastDayInPeriod | IN Item Site History by Last Day In Period | PX_Objects_IN_INItemSiteHistByLastDayInPeriod, INItemSiteHistorybyLastDayInPeriod, INItemSiteHistByLastDayInPeriod | FinPeriodID, InventoryID, LocationID, SiteID, SubItemID |  |  |
| PX.Objects.IN.INItemSiteHistByLatestSDate | IN Item Site History by Latest SDate | PX_Objects_IN_INItemSiteHistByLatestSDate, INItemSiteHistorybyLatestSDate, INItemSiteHistByLatestSDate | InventoryID, LocationID, SiteID, SubItemID |  |  |
| PX.Objects.IN.INItemSiteHistByPeriod | IN Item Site History by Period | PX_Objects_IN_INItemSiteHistByPeriod, INItemSiteHistorybyPeriod, INItemSiteHistByPeriod | FinPeriodID, InventoryID, LocationID, SiteID, SubItemID |  |  |
| PX.Objects.IN.INItemSiteHistDay | IN Item Site History Day | PX_Objects_IN_INItemSiteHistDay, INItemSiteHistoryDay, INItemSiteHistDay | InventoryID, LocationID, SDate, SiteID, SubItemID | QtyIn, QtyOut |  |
| PX.Objects.IN.INItemSiteReplenishment | SubItem Replenishment Info | PX_Objects_IN_INItemSiteReplenishment, SubItemReplenishmentInfo, INItemSiteReplenishment | InventoryID, SiteID, SubItemID | DemandPerDaySTDEV |  |
| PX.Objects.IN.INItemStats | IN Item Statistics | PX_Objects_IN_INItemStats, INItemStatistics, INItemStats | InventoryID, SiteID | QtyReceived, CostReceived |  |
| PX.Objects.IN.INItemXRef | Cross-Reference | PX_Objects_IN_INItemXRef, CrossReference, INItemXRef | AlternateID, AlternateType, BAccountID, InventoryID, SubItemID | NoteText |  |
| PX.Objects.IN.INKitRegister | IN Kit | PX_Objects_IN_INKitRegister, INKit, INKitRegister | DocType, RefNbr | TotalCostStock, TotalCostNonStock, LotSerTrack |  |
| PX.Objects.IN.INKitSerialPart |  | PX_Objects_IN_INKitSerialPart | DocType, KitLineNbr, KitSplitLineNbr, PartLineNbr, PartSplitLineNbr, RefNbr |  |  |
| PX.Objects.IN.INKitSpecHdr | Kit Specification | PX_Objects_IN_INKitSpecHdr, KitSpecification, INKitSpecHdr | KitInventoryID, RevisionID | NoteText |  |
| PX.Objects.IN.INKitSpecNonStkDet | Non-Stock Component of Kit Specification | PX_Objects_IN_INKitSpecNonStkDet, NonStockComponentofKitSpecification, INKitSpecNonStkDet | KitInventoryID, LineNbr, RevisionID | BaseDfltCompQty |  |
| PX.Objects.IN.INKitSpecStkDet | Stock Component of Kit Specification | PX_Objects_IN_INKitSpecStkDet, StockComponentofKitSpecification, INKitSpecStkDet | KitInventoryID, LineNbr, RevisionID | BaseDfltCompQty |  |
| PX.Objects.IN.INKitTranSplit | IN Kit Split | PX_Objects_IN_INKitTranSplit, INKitSplit, INKitTranSplit | DocType, LineNbr, RefNbr, SplitLineNbr | LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.IN.INLocation | IN Location | PX_Objects_IN_INLocation, INLocation | LocationCD, SiteID | NoteText |  |
| PX.Objects.IN.INLocationCostStatus |  | PX_Objects_IN_INLocationCostStatus | InventoryID, LocationID, SiteID, SubItemID | UnitCost |  |
| PX.Objects.IN.INLocationStatus | IN Location Status | PX_Objects_IN_INLocationStatus, INLocationStatus | InventoryID, LocationID, SiteID, SubItemID | Active, QtyNotAvail, QtyExpired |  |
| PX.Objects.IN.INLocationStatusByCostCenter | IN Location Status by Cost Center | PX_Objects_IN_INLocationStatusByCostCenter, INLocationStatusbyCostCenter | CostCenterID, InventoryID, LocationID, SiteID, SubItemID | Active, QtyNotAvail, QtyExpired |  |
| PX.Objects.IN.INLotSerClass | Lot/Serial Class | PX_Objects_IN_INLotSerClass, LotSerialClass, INLotSerClass | LotSerClassID | IsManualAssignRequired, NoteText |  |
| PX.Objects.IN.INLotSerClassAttribute | Lot/Serial Class Attribute | PX_Objects_IN_INLotSerClassAttribute, LotSerialClassAttribute, INLotSerClassAttribute | AttributeID, LotSerClassID |  |  |
| PX.Objects.IN.INLotSerClassLotSerNumVal | Auto-Incremental Value of a Lot/Serial Class | PX_Objects_IN_INLotSerClassLotSerNumVal, AutoIncrementalValueofaLotSerialClass, INLotSerClassLotSerNumVal | LotSerClassID |  |  |
| PX.Objects.IN.INLotSerialStatus | IN Lot/Serial Status | PX_Objects_IN_INLotSerialStatus, INLotSerialStatus | InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID | QtyNotAvail, QtyExpired |  |
| PX.Objects.IN.INLotSerialStatusByCostCenter | IN Lot/Serial Status by Cost Center | PX_Objects_IN_INLotSerialStatusByCostCenter, INLotSerialStatusbyCostCenter | CostCenterID, InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID | QtyNotAvail, QtyExpired |  |
| PX.Objects.IN.INLotSerSegment | Lot/Serial Segment | PX_Objects_IN_INLotSerSegment, LotSerialSegment, INLotSerSegment | LotSerClassID, SegmentID |  |  |
| PX.Objects.IN.INMovementClass | IN Movement Class | PX_Objects_IN_INMovementClass, INMovementClass | MovementClassID |  |  |
| PX.Objects.IN.INNotification | Default Notification setup | PX_Objects_IN_INNotification | SetupID |  |  |
| PX.Objects.IN.INOverheadTran | IN Overhead | PX_Objects_IN_INOverheadTran, INOverhead, INOverheadTran | DocType, LineNbr, RefNbr |  |  |
| PX.Objects.IN.INPIClass | Physical Inventory Type | PX_Objects_IN_INPIClass, PhysicalInventoryType, INPIClass | PIClassID | ByABCFrequency, ByMovementClassFrequency, ByCycleFrequency |  |
| PX.Objects.IN.INPIClassItem | Physical Inventory Type by Item | PX_Objects_IN_INPIClassItem, PhysicalInventoryTypebyItem, INPIClassItem | InventoryID, PIClassID |  |  |
| PX.Objects.IN.INPIClassItemClass |  | PX_Objects_IN_INPIClassItemClass | ItemClassID, PIClassID |  |  |
| PX.Objects.IN.INPIClassLocation | Physical Inventory Type by Location | PX_Objects_IN_INPIClassLocation, PhysicalInventoryTypebyLocation, INPIClassLocation | LocationID, PIClassID |  |  |
| PX.Objects.IN.INPICycle | Physical Inventory Cycle | PX_Objects_IN_INPICycle, PhysicalInventoryCycle, INPICycle | CycleID |  |  |
| PX.Objects.IN.INPIDetail | IN Physical count Detail | PX_Objects_IN_INPIDetail, INPhysicalcountDetail, INPIDetail | LineNbr, PIID | NoteText |  |
| PX.Objects.IN.INPIHeader | Physical Inventory Review | PX_Objects_IN_INPIHeader, PhysicalInventoryReview, INPIHeader | PIID | NoteText |  |
| PX.Objects.IN.INPIStatus | Physical Inventory Status | PX_Objects_IN_INPIStatus, PhysicalInventoryStatus, INPIStatus | LocRecordID, RecordID |  |  |
| PX.Objects.IN.INPIStatusItem |  | PX_Objects_IN_INPIStatusItem | RecordID |  |  |
| PX.Objects.IN.INPIStatusLoc |  | PX_Objects_IN_INPIStatusLoc | RecordID |  |  |
| PX.Objects.IN.INPlanType | IN Item Plan Type | PX_Objects_IN_INPlanType, INItemPlanType, INPlanType | PlanType | LocalizedDescr, DeleteOperation |  |
| PX.Objects.IN.INPostClass | Posting Class | PX_Objects_IN_INPostClass, PostingClass, INPostClass | PostClassID | NoteText |  |
| PX.Objects.IN.INPriceClass | IN Item Price Class | PX_Objects_IN_INPriceClass, INItemPriceClass, INPriceClass | PriceClassID | NoteText |  |
| PX.Objects.IN.INRegister | Receipt | PX_Objects_IN_INRegister, Receipt, INRegister | DocType, RefNbr | SrcDocType, SrcRefNbr, ReleasedToVerify, NoteText |  |
| PX.Objects.IN.INReplenishmentClass | Replenishment Class | PX_Objects_IN_INReplenishmentClass, ReplenishmentClass, INReplenishmentClass | ReplenishmentClassID |  |  |
| PX.Objects.IN.INReplenishmentItem |  | PX_Objects_IN_INReplenishmentItem | InventoryID, SiteID | QtyProcess, QtyProcessRounded |  |
| PX.Objects.IN.INReplenishmentLine | Replenishment Line | PX_Objects_IN_INReplenishmentLine, ReplenishmentLine, INReplenishmentLine | LineNbr, RefNbr |  |  |
| PX.Objects.IN.INReplenishmentOrder | Replenishment Order | PX_Objects_IN_INReplenishmentOrder, ReplenishmentOrder, INReplenishmentOrder | RefNbr | NoteText |  |
| PX.Objects.IN.INReplenishmentPolicy | Replenishment Policy | PX_Objects_IN_INReplenishmentPolicy, ReplenishmentPolicy, INReplenishmentPolicy | ReplenishmentPolicyID | NoteText |  |
| PX.Objects.IN.INReplenishmentSeason | Replenishment Seasonality | PX_Objects_IN_INReplenishmentSeason, ReplenishmentSeasonality, INReplenishmentSeason | ReplenishmentPolicyID, SeasonID |  |  |
| PX.Objects.IN.INScanSetup | IN Scan Setup | PX_Objects_IN_INScanSetup, INScanSetup | BranchID |  |  |
| PX.Objects.IN.INScanUserSetup | IN Scan User Setup | PX_Objects_IN_INScanUserSetup, INScanUserSetup | Mode, UserID |  |  |
| PX.Objects.IN.INSite | Warehouse | PX_Objects_IN_INSite, Warehouse, INSite | SiteCD | ReceiptLocationIDOverride, ShipLocationIDOverride, NoteText, Included, DiscAcctID, DiscSubID, FreightAcctID, FreightSubID, MiscAcctID, MiscSubID, Secured |  |
| PX.Objects.IN.INSiteBuilding | Warehouse Building | PX_Objects_IN_INSiteBuilding, WarehouseBuilding, INSiteBuilding | BuildingCD |  |  |
| PX.Objects.IN.INSiteLotSerial | Lot/Serial by Warehouse | PX_Objects_IN_INSiteLotSerial, LotSerialbyWarehouse, INSiteLotSerial | InventoryID, LotSerialNbr, SiteID | UpdateExpireDate |  |
| PX.Objects.IN.INSiteStatus | IN Site Status | PX_Objects_IN_INSiteStatus, INSiteStatus | InventoryID, SiteID, SubItemID | QtyExpired |  |
| PX.Objects.IN.INSiteStatusByCostCenter | IN Site Status by Cost Center | PX_Objects_IN_INSiteStatusByCostCenter, INSiteStatusbyCostCenter | CostCenterID, InventoryID, SiteID, SubItemID | Active, QtyExpired |  |
| PX.Objects.IN.INSiteStatusByCostCenterShort | IN Site Status by Cost Center Short | PX_Objects_IN_INSiteStatusByCostCenterShort, INSiteStatusbyCostCenterShort | CostCenterID, InventoryID, SiteID, SubItemID |  |  |
| PX.Objects.IN.INSiteStatusQtyAggregated | Sum of Inventory Qtys by InventoryID with LastModifiedDateTime | PX_Objects_IN_INSiteStatusQtyAggregated, SumofInventoryQtysbyInventoryIDwithLastModifiedDateTime, INSiteStatusQtyAggregated | InventoryID |  |  |
| PX.Objects.IN.INSiteStatusSelected |  | PX_Objects_IN_INSiteStatusSelected | InventoryID | QtySelected, Rank |  |
| PX.Objects.IN.INSiteStatusSummary | IN Warehouse Status | PX_Objects_IN_INSiteStatusSummary, INWarehouseStatus, INSiteStatusSummary | InventoryID, SiteID |  |  |
| PX.Objects.IN.INSubItem | IN Sub Item | PX_Objects_IN_INSubItem, INSubItem | SubItemCD | Secured |  |
| PX.Objects.IN.INSubItemRep | Subitem Replenishment Settings | PX_Objects_IN_INSubItemRep, SubitemReplenishmentSettings, INSubItemRep | CuryID, InventoryID, ReplenishmentClassID, SubItemID |  |  |
| PX.Objects.IN.INSubItemSegmentValue | IN Subitem Segment Value | PX_Objects_IN_INSubItemSegmentValue, INSubitemSegmentValue | InventoryID, SegmentID, Value |  |  |
| PX.Objects.IN.IntercompanyGoodsInTransitResult | Intercompany Goods in Transit Result | PX_Objects_IN_IntercompanyGoodsInTransitResult, IntercompanyGoodsinTransitResult | LineNbr, POReceiptNbr, POReceiptType, ShipmentNbr |  |  |
| PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult | Intercompany Returned Goods in Transit Result | PX_Objects_IN_IntercompanyReturnedGoodsInTransitResult, IntercompanyReturnedGoodsinTransitResult | LineNbr, POReturnNbr |  |  |
| PX.Objects.IN.INTote | IN Tote | PX_Objects_IN_INTote, INTote | SiteID, ToteCD | NoteText |  |
| PX.Objects.IN.INTran | IN Transaction | PX_Objects_IN_INTran, INTransaction, INTran | DocType, LineNbr, RefNbr | OverrideUnitCost, AvgCost, CostedQty, OrigTranCost, OrigTranAmt, ReceiptedBaseQty, INTransitBaseQty, ReceiptedQty, INTransitQty, NoteText, SalesMult |  |
| PX.Objects.IN.INTranCost | IN Transaction Cost | PX_Objects_IN_INTranCost, INTransactionCost, INTranCost | CostDocType, CostID, CostRefNbr, DocType, LineNbr, RefNbr | TranAmt, QtyOnHand, UnitCost, TotalCost |  |
| PX.Objects.IN.INTranDetail | IN Transaction Detail | PX_Objects_IN_INTranDetail, INTransactionDetail, INTranDetail | DocType, LineNbr, RefNbr, SplitLineNbr, TranType | TranCost |  |
| PX.Objects.IN.INTransfer | Receipt | PX_Objects_IN_INTransfer | DocType, RefNbr |  |  |
| PX.Objects.IN.INTransferLocationStatus |  | PX_Objects_IN_INTransferLocationStatus | InventoryID, SubItemID, TransferNbr |  |  |
| PX.Objects.IN.INTransferStatus |  | PX_Objects_IN_INTransferStatus | InventoryID, SubItemID, TransferNbr | UnitCost |  |
| PX.Objects.IN.INTransitLine | Transfer Line | PX_Objects_IN_INTransitLine, TransferLine, INTransitLine | TransferLineNbr, TransferNbr | NoteText |  |
| PX.Objects.IN.INTransitLineLotSerialStatus |  | PX_Objects_IN_INTransitLineLotSerialStatus | InventoryID, LotSerialNbr, SubItemID, TransferLineNbr, TransferNbr |  |  |
| PX.Objects.IN.INTransitLineStatus |  | PX_Objects_IN_INTransitLineStatus | TransferLineNbr, TransferNbr |  |  |
| PX.Objects.IN.INTranSplit | IN Transaction Split | PX_Objects_IN_INTranSplit, INTransactionSplit, INTranSplit | DocType, LineNbr, RefNbr, SplitLineNbr | ValMethod, FromSiteID, FromLocationID, LotSerClassID, AssignedNbr, SkipCostUpdate, SkipQtyValidation, ProjectID, TaskID |  |
| PX.Objects.IN.INUnit | Inventory Unit Conversions | PX_Objects_IN_INUnit, InventoryUnitConversions, INUnit | FromUnit, InventoryID, ItemClassID, ToUnit, UnitType | SampleToUnit |  |
| PX.Objects.IN.INUpdateStdCostRecord |  | PX_Objects_IN_INUpdateStdCostRecord | CuryID, InventoryID |  |  |
| PX.Objects.IN.InventoryItem | Inventory Item | PX_Objects_IN_InventoryItem, InventoryItem | InventoryCD | IsConversionMode, ExpenseAccrualAcctID, ExpenseAccrualSubID, ExpenseAcctID, ExpenseSubID, NegQty, TotalPercentage, NoteText, NotePopupText, Included, HasChild, SampleID, SampleDescription, UpdateOnlySelected, DiscAcctID, DiscSubID, EntityTypeID, Secured, DeletedDatabaseRecord |  |
| PX.Objects.IN.InventoryItemCommon | Inventory Item Common Fields Only | PX_Objects_IN_InventoryItemCommon, InventoryItemCommonFieldsOnly, InventoryItemCommon | InventoryCD |  |  |
| PX.Objects.IN.InventoryItemCurySettings | Inventory Item Currency Settings | PX_Objects_IN_InventoryItemCurySettings, InventoryItemCurrencySettings, InventoryItemCurySettings | CuryID, InventoryID |  |  |
| PX.Objects.IN.InventoryItemLotSerNumVal | Auto-Incremental Value of a Stock Item | PX_Objects_IN_InventoryItemLotSerNumVal, AutoIncrementalValueofaStockItem, InventoryItemLotSerNumVal | InventoryID |  |  |
| PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup | Attribute Description Group | PX_Objects_IN_Matrix_DAC_INAttributeDescriptionGroup, AttributeDescriptionGroup, INAttributeDescriptionGroup | GroupID, TemplateID |  |  |
| PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem | Attribute Description Item | PX_Objects_IN_Matrix_DAC_INAttributeDescriptionItem, AttributeDescriptionItem, INAttributeDescriptionItem | AttributeID, GroupID, TemplateID |  |  |
| PX.Objects.IN.Matrix.DAC.INMatrixExcludedData | Data Excluded From Update of Matrix Items | PX_Objects_IN_Matrix_DAC_INMatrixExcludedData, DataExcludedFromUpdateofMatrixItems, INMatrixExcludedData | FieldName, TableName, TemplateID, Type | NoteText |  |
| PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule | Matrix Generation Rule | PX_Objects_IN_Matrix_DAC_INMatrixGenerationRule, MatrixGenerationRule, INMatrixGenerationRule | LineNbr, ParentID, ParentType, Type |  |  |
| PX.Objects.IN.Matrix.DAC.Projections.DescriptionGenerationRule | Description Generation Rule | PX_Objects_IN_Matrix_DAC_Projections_DescriptionGenerationRule, DescriptionGenerationRule | LineNbr, ParentID, ParentType, Type |  |  |
| PX.Objects.IN.Matrix.DAC.Projections.ExcludedAttribute | Attribute Excluded From Update of Matrix Items | PX_Objects_IN_Matrix_DAC_Projections_ExcludedAttribute, AttributeExcludedFromUpdateofMatrixItems, ExcludedAttribute | FieldName, TableName, TemplateID, Type |  |  |
| PX.Objects.IN.Matrix.DAC.Projections.ExcludedField | Field Excluded From Update of Matrix Items | PX_Objects_IN_Matrix_DAC_Projections_ExcludedField, FieldExcludedFromUpdateofMatrixItems, ExcludedField | FieldName, TableName, TemplateID, Type |  |  |
| PX.Objects.IN.Matrix.DAC.Projections.IDGenerationRule | ID Generation Rule | PX_Objects_IN_Matrix_DAC_Projections_IDGenerationRule, IDGenerationRule | LineNbr, ParentID, ParentType, Type |  |  |
| PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem | Inventory Item with Attribute Values | PX_Objects_IN_Matrix_DAC_Unbound_MatrixInventoryItem, InventoryItemwithAttributeValues, MatrixInventoryItem | InventoryCD |  | yes |
| PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback | Related Item ML Feedback | PX_Objects_IN_RelatedItems_DAC_INRelatedInventoryUserFeedback, RelatedItemMLFeedback, INRelatedInventoryUserFeedback | InventoryID, RelatedInventoryID |  |  |
| PX.Objects.IN.RelatedItems.INRelatedInventory | Related Item | PX_Objects_IN_RelatedItems_INRelatedInventory, RelatedItem, INRelatedInventory | InventoryID, LineID | Desc, NoteText, NotePopupText |  |
| PX.Objects.IN.RelatedItems.RelatedItem | Related Item | PX_Objects_IN_RelatedItems_RelatedItem, RelatedItem1 | InventoryID, LineID | Desc, QtySelected, CuryUnitPrice, CuryExtPrice, PriceDiff |  |
| PX.Objects.IN.RelatedItems.RelatedItemHistory | Related Item History | PX_Objects_IN_RelatedItems_RelatedItemHistory, RelatedItemHistory | LineID | OriginalInventoryDesc, RelatedInventoryDesc |  |
| PX.Objects.IN.S.INItemSite |  | PX_Objects_IN_S_INItemSite | InventoryID, SiteID | IsDefault, NoteText |  |
| PX.Objects.IN.StoragePlace | IN Storage Place | PX_Objects_IN_StoragePlace, INStoragePlace, StoragePlace | SiteID |  |  |
| PX.Objects.IN.Turnover.INTurnoverCalc | Turnover Calculation | PX_Objects_IN_Turnover_INTurnoverCalc, TurnoverCalculation, INTurnoverCalc | BranchID, FromPeriodID, ToPeriodID | NoteText |  |
| PX.Objects.IN.Turnover.INTurnoverCalcItem | Turnover Calculation Item | PX_Objects_IN_Turnover_INTurnoverCalcItem, TurnoverCalculationItem, INTurnoverCalcItem | BranchID, FromPeriodID, InventoryID, SiteID, ToPeriodID |  |  |
| PX.Objects.IN.Turnover.TurnoverCalcItem | Turnover Calculation Item | PX_Objects_IN_Turnover_TurnoverCalcItem, TurnoverCalculationItem1, TurnoverCalcItem | BranchID, FromPeriodID, InventoryCD, SiteCD, ToPeriodID |  |  |
| PX.Objects.IN.UnitOfMeasure | Unit of Measure | PX_Objects_IN_UnitOfMeasure, UnitofMeasure | Unit | NoteText |  |
| PX.Objects.IN.WMSJob | IN WMS Job | PX_Objects_IN_WMSJob, INWMSJob, WMSJob | JobID | NoteText |  |
| PX.Objects.Localizations.CA.APAdjustEFileRevision | APAdjust EFileRevision | PX_Objects_Localizations_CA_APAdjustEFileRevision, APAdjustEFileRevision | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, OrgBAccountID, Revision |  |  |
| PX.Objects.Localizations.CA.CanadianOrganizationSettings | Canadian Organization Settings | PX_Objects_Localizations_CA_CanadianOrganizationSettings, CanadianOrganizationSettings | OrgBAccountID |  |  |
| PX.Objects.Localizations.CA.CanadianVendor | Canadian Vendor | PX_Objects_Localizations_CA_CanadianVendor, CanadianVendor | VendorID |  |  |
| PX.Objects.Localizations.CA.T4AHistory | T4A History | PX_Objects_Localizations_CA_T4AHistory, T4AHistory | BoxNbr, BranchID, Revision, VendorID, Year |  |  |
| PX.Objects.Localizations.CA.T4AHistoryDetails | T4A History Details | PX_Objects_Localizations_CA_T4AHistoryDetails, T4AHistoryDetails | BoxNbr, BranchID, DocType, RefNbr, Revision, VendorID, Year |  |  |
| PX.Objects.Localizations.CA.T4AMasterTable | T4A Master Table | PX_Objects_Localizations_CA_T4AMasterTable, T4AMasterTable | OrgBAccountID, Revision, Year | FromDate, ToDate, NoteText, ProgramNumber, TransmitterRepID, AcctName, AddressLine1, AddressLine2, City, Province, Country, PostalCode, Name, AreaCode, Phone, ExtensionNbr, Email, SecondEmail, Language, FilingType |  |
| PX.Objects.Localizations.CA.T4ASlip | T4A Slip | PX_Objects_Localizations_CA_T4ASlip, T4ASlip | BoxNbr, OrgBAccountID, Revision, VendorID, Year | NoteText |  |
| PX.Objects.Localizations.CA.T5018EFileRow | T5018 EFile Row | PX_Objects_Localizations_CA_T5018EFileRow, T5018EFileRow | BAccountID, OrgBAccountID, Revision, Year |  |  |
| PX.Objects.Localizations.CA.T5018MasterTable | T5018 Master Table | PX_Objects_Localizations_CA_T5018MasterTable, T5018MasterTable | OrgBAccountID, Revision, Year | NoteText |  |
| PX.Objects.Localizations.CA.T5018Transactions | T5018Transactions | PX_Objects_Localizations_CA_T5018Transactions, T5018Transactions | BranchID, DocDate, DocType, RefNbr, VendorID |  |  |
| PX.Objects.Localizations.CA.TaxRegistration | Tax Registration | PX_Objects_Localizations_CA_TaxRegistration, TaxRegistration | BAccountID, TaxID |  |  |
| PX.Objects.Localizations.GB.CISHistory | CISHistory | PX_Objects_Localizations_GB_CISHistory, CISHistory | BranchID, Revision, TaxPeriodID, VendorID |  |  |
| PX.Objects.Localizations.GB.CISHistoryDetails | CISHistoryDetails | PX_Objects_Localizations_GB_CISHistoryDetails, CISHistoryDetails | BranchID, DocType, RefNbr, Revision, TaxPeriodID, VendorID |  |  |
| PX.Objects.Localizations.GB.CISMasterTable | CIS Master Table | PX_Objects_Localizations_GB_CISMasterTable, CISMasterTable | OrgBAccountID, Revision, TaxPeriodID | NilReturnIndicatorDeclaration, NoteText |  |
| PX.Objects.Localizations.GB.CISSubcontractor | CIS Subcontractor | PX_Objects_Localizations_GB_CISSubcontractor, CISSubcontractor | VendorID |  |  |
| PX.Objects.Localizations.GB.HMRC.DAC.BAccountMTDApplication | MTD External Application | PX_Objects_Localizations_GB_HMRC_DAC_BAccountMTDApplication, MTDExternalApplication, BAccountMTDApplication | BAccountID |  |  |
| PX.Objects.Localizations.GB.HMRCSubmission | HMRC Submission | PX_Objects_Localizations_GB_HMRCSubmission, HMRCSubmission | FormType, HMRCForm |  |  |
| PX.Objects.Localizations.GB.UKTaxReportingSettings | UK Tax Reporting Settings | PX_Objects_Localizations_GB_UKTaxReportingSettings, UKTaxReportingSettings | OrgBAccountID |  |  |
| PX.Objects.MN.DAC.Projections.MaterialMassProcessLine | Material Line | PX_Objects_MN_DAC_Projections_MaterialMassProcessLine, MaterialLine, MaterialMassProcessLine | LineNbr, SourceNoteID | SourceNoteDisplayID, QtyAvailableForDispatch |  |
| PX.Objects.MN.MNMaterialList | Material List | PX_Objects_MN_MNMaterialList, MaterialList, MNMaterialList | RefNbr | NoteText |  |
| PX.Objects.MN.MNMaterialListLine | Material Line | PX_Objects_MN_MNMaterialListLine, MaterialLine1, MNMaterialListLine | LineNbr, MaterialListNoteID | TranType, QtyAvailableForDispatch, IsKit, LineQtyAvail, LineQtyHardAvail, NoteText |  |
| PX.Objects.MN.MNMaterialListLineSplit | Material Line Split | PX_Objects_MN_MNMaterialListLineSplit, MaterialLineSplit, MNMaterialListLineSplit | LineNbr, MaterialListNoteID, SplitLineNbr | TranType, LotSerClassID, AssignedNbr, UnreceivedQty, BaseUnreceivedQty, OpenQty, BaseOpenQty, ProjectID, TaskID, PlanType, POCreate |  |
| PX.Objects.MN.MNMaterialListShipment | Material List | PX_Objects_MN_MNMaterialListShipment, MaterialList1, MNMaterialListShipment | MaterialListNoteID, ShipmentNoteID |  |  |
| PX.Objects.MN.MNMaterialListSiteStatusSelected | Material Line Inventory Lookup Row | PX_Objects_MN_MNMaterialListSiteStatusSelected, MaterialLineInventoryLookupRow, MNMaterialListSiteStatusSelected | InventoryID | QtySelected, Rank |  |
| PX.Objects.MN.POCreateExt.MNMaterialListLineProjection | Material Line | PX_Objects_MN_POCreateExt_MNMaterialListLineProjection, MaterialLine2, MNMaterialListLineProjection | LineNbr, MaterialListNoteID |  |  |
| PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection | Material Line Split | PX_Objects_MN_POCreateExt_MNMaterialListLineSplitProjection, MaterialLineSplit1, MNMaterialListLineSplitProjection | LineNbr, MaterialListNoteID, SplitLineNbr |  |  |
| PX.Objects.PJ.Common.DAC.ContactForCurrentProject |  | PX_Objects_PJ_Common_DAC_ContactForCurrentProject | ContactID |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport | Daily Field Report | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReport, DailyFieldReport | DailyFieldReportCd | NoteText, WorkgroupID, OwnerID, TemperatureLevel, Humidity, Icon, TimeObserved, TimeActivitiesTimeBillableTotal, TimeActivitiesTimeSpentTotal, DeletedDatabaseRecord |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder | Daily Field Report Change Order | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportChangeOrder, DailyFieldReportChangeOrder | DailyFieldReportChangeOrderId |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest | Daily Field Report Change Request | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportChangeRequest, DailyFieldReportChangeRequest | DailyFieldReportChangeRequestId |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity | Daily Field Report Employee Activity | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEmployeeActivity, DailyFieldReportEmployeeActivity | DailyFieldReportId, EmployeeActivityId |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense | Daily Field Report Employee Expenses | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEmployeeExpense, DailyFieldReportEmployeeExpenses, DailyFieldReportEmployeeExpense | DailyFieldReportEmployeeExpenseId |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment | Daily Field Report Equipment | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEquipment, DailyFieldReportEquipment | DailyFieldReportId, EquipmentDetailLineNumber, EquipmentTimeCardCd |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory | Daily Field Report History | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportHistory, DailyFieldReportHistory | DailyFieldReportHistoryId | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote | Daily Field Report Note | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportNote, DailyFieldReportNote | DailyFieldReportNoteId | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog | Daily Field Report Photo Log | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportPhotoLog, DailyFieldReportPhotoLog | DailyFieldReportPhotoLogId |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet | Daily Field Report Progress Worksheet | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProgressWorksheet, DailyFieldReportProgressWorksheet | DailyFieldReportId, ProgressWorksheetId |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection |  | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProjection | DailyFieldReportCd |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue | Daily Field Report Project Issue | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProjectIssue, DailyFieldReportProjectIssue | DailyFieldReportProjectIssueId |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity | Daily Field Report Subcontractor Activity | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportSubcontractorActivity, DailyFieldReportSubcontractorActivity | SubcontractorId | VendorName, ProjectID, NoteText, DeletedDatabaseRecord |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor | Daily Field Report Visitor | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportVisitor, DailyFieldReportVisitor | DailyFieldReportVisitorId | NoteText |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather | Daily Field Report Weather | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportWeather, DailyFieldReportWeather | DailyFieldReportWeatherId | TemperatureLevelMobile, PrecipitationAmountMobile, WindSpeedMobile, NoteText |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection | Daily Field Report Equipment | PX_Objects_PJ_DailyFieldReports_PJ_DAC_EquipmentProjection, DailyFieldReportEquipment1, EquipmentProjection | LineNbr, TimeCardCD |  |  |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog | Weather Processing Log | PX_Objects_PJ_DailyFieldReports_PJ_DAC_WeatherProcessingLog, WeatherProcessingLog | WeatherProcessingLogId | NoteText |  |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog | Drawing Log | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLog, DrawingLog | DrawingLogCd | SelectorStatusId, UsrDrawingLogClassId, NoteText, DeletedDatabaseRecord |  |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline | Drawing Log Discipline | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogDiscipline, DrawingLogDiscipline | DrawingLogDisciplineId | LineNbr |  |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogRevision | Drawing Log Revision | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogRevision, DrawingLogRevision | DrawingLogId, DrawingLogRevisionId |  |  |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus | Drawing Log Status | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogStatus, DrawingLogStatus | StatusId |  |  |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings | Email Drawings | PX_Objects_PJ_DrawingLogs_PJ_DAC_EmailDrawings, EmailDrawings | DrawingLogCd, RequestForInformationCd |  |  |
| PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo | Photo | PX_Objects_PJ_PhotoLogs_PJ_DAC_Photo, Photo | PhotoCd | ImageUrl, NoteText, Tstamp, CreatedByScreenId, CreatedDateTime, LastModifiedById, LastModifiedByScreenId, LastModifiedDateTime, UsrPhotoClassId, Tags, DeletedDatabaseRecord |  |
| PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog | Photo Log | PX_Objects_PJ_PhotoLogs_PJ_DAC_PhotoLog, PhotoLog | PhotoLogCd | SelectorStatusId, NoteText, DailyFieldReportId, FormCaptionDescription, PhotoLogClassID, DeletedDatabaseRecord |  |
| PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus | Photo Log Status | PX_Objects_PJ_PhotoLogs_PJ_DAC_PhotoLogStatus, PhotoLogStatus | StatusId |  |  |
| PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass | Project Management Class | PX_Objects_PJ_ProjectManagement_PJ_DAC_ProjectManagementClass, ProjectManagementClass | ProjectManagementClassId | NoteText |  |
| PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority | Project Management Class Priority | PX_Objects_PJ_ProjectManagement_PJ_DAC_ProjectManagementClassPriority, ProjectManagementClassPriority | PriorityId | NoteText |  |
| PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue | Project Issue | PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssue, ProjectIssue | ProjectIssueCd | MajorStatus, NoteText, PriorityIcon, DailyFieldReportId, DeletedDatabaseRecord |  |
| PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueDrawingLog | Project Issue Drawing Log | PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssueDrawingLog, ProjectIssueDrawingLog | DrawingLogId, ProjectIssueId |  |  |
| PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueType | Project Issue Type | PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssueType, ProjectIssueType | ProjectIssueTypeId |  |  |
| PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation | Request For Information | PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformation, RequestForInformation | RequestForInformationCd | NoteText, IsScheduleImpactFormatted, IsCostImpactFormatted, DesignChangeFormatted, DeletedDatabaseRecord |  |
| PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationAttachment | Request For Information Attachment | PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationAttachment, RequestForInformationAttachment | FileID, RequestForInformationCd |  |  |
| PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationDrawingLog | Request For Information Drawing Log | PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationDrawingLog, RequestForInformationDrawingLog | DrawingLogId, RequestForInformationId |  |  |
| PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation | Request For Information Relation | PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationRelation, RequestForInformationRelation | RequestForInformationRelationId | BusinessAccountCd, BusinessAccountName, ContactName, ContactEmail |  |
| PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal | Submittal | PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittal, Submittal, PJSubmittal | RevisionID, SubmittalID | DaysOverdue, WorkgroupID, FormCaptionDescription, NoteText |  |
| PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType | Submittal Type | PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittalType, SubmittalType, PJSubmittalType | SubmittalTypeID |  |  |
| PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem | Submittal Workflow Item | PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittalWorkflowItem, SubmittalWorkflowItem, PJSubmittalWorkflowItem | LineNbr, RevisionID, SubmittalID | CanDelete, NoteText |  |
| PX.Objects.PM.DAC.PMItemCostStatusByCostCenter | Item Cost Status by Cost Center | PX_Objects_PM_DAC_PMItemCostStatusByCostCenter, ItemCostStatusbyCostCenter, PMItemCostStatusByCostCenter | CostCenterID, InventoryID, SiteID |  |  |
| PX.Objects.PM.DAC.PMReportRowsMultiplier | Report Rows Multiplier | PX_Objects_PM_DAC_PMReportRowsMultiplier, ReportRowsMultiplier, PMReportRowsMultiplier | RecordID | RecordID |  |
| PX.Objects.PM.DAC.PMSelectedTag | Project Selected Tag | PX_Objects_PM_DAC_PMSelectedTag, ProjectSelectedTag, PMSelectedTag | TagID |  |  |
| PX.Objects.PM.DAC.PMTagTemplate | Project Tag Template | PX_Objects_PM_DAC_PMTagTemplate, ProjectTagTemplate, PMTagTemplate | TemplateCD | NoteText |  |
| PX.Objects.PM.DAC.PMTagTemplateItem | Project Tag | PX_Objects_PM_DAC_PMTagTemplateItem, ProjectTag, PMTagTemplateItem | TagID, TemplateID | TagCD, Description |  |
| PX.Objects.PM.DAC.Reports.PMRegister | Project Register | PX_Objects_PM_DAC_Reports_PMRegister, ProjectRegister, PMRegister | Module, RefNbr | NoteText |  |
| PX.Objects.PM.Lite.PMBudget | Budget | PX_Objects_PM_Lite_PMBudget, Budget1, PMBudget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID |  |  |
| PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList | Material List | PX_Objects_PM_MaterialManagement_MaterialList_PMMaterialList, MaterialList2, PMMaterialList | ProjectID |  |  |
| PX.Objects.PM.PMAccountGroup | Account Group | PX_Objects_PM_PMAccountGroup, AccountGroup, PMAccountGroup | GroupCD | Included, ClassID, NoteText, Secured |  |
| PX.Objects.PM.PMAccountGroupRate | PM Account Group Rate | PX_Objects_PM_PMAccountGroupRate, PMAccountGroupRate | AccountGroupID, RateCodeID, RateDefinitionID |  |  |
| PX.Objects.PM.PMAccountTask | PM Account Task | PX_Objects_PM_PMAccountTask, PMAccountTask | AccountID, ProjectID | NoteText |  |
| PX.Objects.PM.PMAddress | PM Address | PX_Objects_PM_PMAddress, PMAddress | AddressID | BAccountID, OverrideAddress |  |
| PX.Objects.PM.PMAllocation | Allocation Rule | PX_Objects_PM_PMAllocation, AllocationRule, PMAllocation | AllocationID | NoteText |  |
| PX.Objects.PM.PMAllocationAuditTran | PM Allocation Audit Transaction | PX_Objects_PM_PMAllocationAuditTran, PMAllocationAuditTransaction, PMAllocationAuditTran | AllocationID, SourceTranID, TranID |  |  |
| PX.Objects.PM.PMAllocationDetail | Allocation Rule Step | PX_Objects_PM_PMAllocationDetail, AllocationRuleStep, PMAllocationDetail | AllocationID, StepID | FullDetail, Allocation, AllocationText, NoteText |  |
| PX.Objects.PM.PMAllocationSourceTran | PM Allocation Source Transaction | PX_Objects_PM_PMAllocationSourceTran, PMAllocationSourceTransaction, PMAllocationSourceTran | AllocationID, StepID, TranID |  |  |
| PX.Objects.PM.PMBilling | Billing Rule | PX_Objects_PM_PMBilling, BillingRule, PMBilling | BillingID | NoteText |  |
| PX.Objects.PM.PMBillingAddress | PM Billing Address | PX_Objects_PM_PMBillingAddress, PMBillingAddress | AddressID |  |  |
| PX.Objects.PM.PMBillingContact | PM Billing Contact | PX_Objects_PM_PMBillingContact, PMBillingContact | ContactID |  |  |
| PX.Objects.PM.PMBillingRecord | Project Billing Record | PX_Objects_PM_PMBillingRecord, ProjectBillingRecord, PMBillingRecord | BillingTag, ProjectID, RecordID | SortOrder, RecordNumber |  |
| PX.Objects.PM.PMBillingRule | Billing Rule Step | PX_Objects_PM_PMBillingRule, BillingRuleStep, PMBillingRule | BillingID, StepID | BranchSourceBudget, IncludeZeroAmount, NoteText |  |
| PX.Objects.PM.PMBudget | Project Budget | PX_Objects_PM_PMBudget, ProjectBudget, PMBudget1 | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID | RevenueTaskIDApiEndPoint, CuryActualPlusOpenCommittedAmount, ActualPlusOpenCommittedAmount, CuryVarianceAmount, VarianceAmount, Performance, SortOrder, NoteText, CuryRate |  |
| PX.Objects.PM.PMBudgetedCostCode | Budget | PX_Objects_PM_PMBudgetedCostCode, Budget2, PMBudgetedCostCode | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID |  |  |
| PX.Objects.PM.PMBudgetProduction | Budget Production | PX_Objects_PM_PMBudgetProduction, BudgetProduction, PMBudgetProduction | AccountGroupID, CostCodeID, InventoryID, LineNbr, ProjectID, ProjectTaskID | NoteText |  |
| PX.Objects.PM.PMChangeOrder | Change Order | PX_Objects_PM_PMChangeOrder, ChangeOrder, PMChangeOrder | RefNbr | ChangeOrderTaskCD, DescriptionAsPlainText, ReversingRefNbr, RevenueChangeTotal, GrossMarginAmount, GrossMarginPct, CuryInfoID, IsCostVisible, IsRevenueVisible, IsDetailsVisible, IsChangeRequestVisible, FormCaptionDescription, NoteText, DailyFieldReportId |  |
| PX.Objects.PM.PMChangeOrderBudget | Budget | PX_Objects_PM_PMChangeOrderBudget, Budget3, PMChangeOrderBudget | LineNbr, RefNbr, Type | RevisedQty, RevisedAmount, PreviouslyApprovedQty, PreviouslyApprovedAmount, CommittedCOQty, CommittedCOAmount, OtherDraftRevisedAmount, TotalPotentialRevisedAmount, NoteText |  |
| PX.Objects.PM.PMChangeOrderClass | Change Order Class | PX_Objects_PM_PMChangeOrderClass, ChangeOrderClass, PMChangeOrderClass | ClassID | IncrementsProjectNumber, NoteText |  |
| PX.Objects.PM.PMChangeOrderCostBudget | Budget | PX_Objects_PM_PMChangeOrderCostBudget, Budget4, PMChangeOrderCostBudget | LineNbr, RefNbr, Type |  |  |
| PX.Objects.PM.PMChangeOrderLine | Change Order Line | PX_Objects_PM_PMChangeOrderLine, ChangeOrderLine, PMChangeOrderLine | LineNbr, RefNbr | PotentialRevisedQty, PotentialRevisedAmount, NoteText |  |
| PX.Objects.PM.PMChangeOrderRevenueBudget | Budget | PX_Objects_PM_PMChangeOrderRevenueBudget, Budget5, PMChangeOrderRevenueBudget | LineNbr, RefNbr, Type |  |  |
| PX.Objects.PM.PMChangeOrderTax | PMChangeOrderTax | PX_Objects_PM_PMChangeOrderTax, PMChangeOrderTax | LineNbr, RefNbr, TaxID | NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt |  |
| PX.Objects.PM.PMChangeOrderTaxTran | PMChangeOrderTaxTran | PX_Objects_PM_PMChangeOrderTaxTran, PMChangeOrderTaxTran | RecordID, TaxID | NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.PM.PMChangeRequest | Change Request | PX_Objects_PM_PMChangeRequest, ChangeRequest, PMChangeRequest | RefNbr | ChangeRequestTaskCD, DescriptionAsPlainText, GrossMarginPct, FormCaptionDescription, CuryInfoID, ChangeRequestTaxTotal, ChangeRequestTotal, NoteText, DailyFieldReportId |  |
| PX.Objects.PM.PMChangeRequestAudit | Change Request Audit | PX_Objects_PM_PMChangeRequestAudit, ChangeRequestAudit, PMChangeRequestAudit | RecordID |  |  |
| PX.Objects.PM.PMChangeRequestLine | Change Request | PX_Objects_PM_PMChangeRequestLine, ChangeRequest1, PMChangeRequestLine | LineNbr, RefNbr | NoteText |  |
| PX.Objects.PM.PMChangeRequestLineTax | Change Request Line Tax | PX_Objects_PM_PMChangeRequestLineTax, ChangeRequestLineTax, PMChangeRequestLineTax | LineNbr, RefNbr, TaxID, Type |  |  |
| PX.Objects.PM.PMChangeRequestLineTaxTran | PChange Request Line Tax Tran | PX_Objects_PM_PMChangeRequestLineTaxTran, PChangeRequestLineTaxTran, PMChangeRequestLineTaxTran | RecordID, TaxID |  |  |
| PX.Objects.PM.PMChangeRequestMarkup | Markup | PX_Objects_PM_PMChangeRequestMarkup, Markup1, PMChangeRequestMarkup | LineNbr, RefNbr | ProjectID, NoteText |  |
| PX.Objects.PM.PMChangeRequestMarkupTax | Change Request Markup Tax | PX_Objects_PM_PMChangeRequestMarkupTax, ChangeRequestMarkupTax, PMChangeRequestMarkupTax | LineNbr, RefNbr, TaxID, Type |  |  |
| PX.Objects.PM.PMChangeRequestMarkupTaxTran | PChange Request Markup Tax Tran | PX_Objects_PM_PMChangeRequestMarkupTaxTran, PChangeRequestMarkupTaxTran, PMChangeRequestMarkupTaxTran | RecordID, TaxID |  |  |
| PX.Objects.PM.PMChangeRequestTax | Change Request Tax | PX_Objects_PM_PMChangeRequestTax, ChangeRequestTax, PMChangeRequestTax | LineNbr, RefNbr, TaxID, Type | NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt |  |
| PX.Objects.PM.PMChangeRequestTaxTran | PChange Request Tax Tran | PX_Objects_PM_PMChangeRequestTaxTran, PChangeRequestTaxTran, PMChangeRequestTaxTran | RecordID, TaxID | NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.PM.PMChangeRequestTotalTaxTran | PChange Request Total Tax Tran | PX_Objects_PM_PMChangeRequestTotalTaxTran, PChangeRequestTotalTaxTran, PMChangeRequestTotalTaxTran | RecordID, TaxID |  |  |
| PX.Objects.PM.PMCommitment | Commitment Record | PX_Objects_PM_PMCommitment, CommitmentRecord, PMCommitment | CommitmentID | CommittedVarianceQty, CommittedVarianceAmount, NoteText |  |
| PX.Objects.PM.PMContact | Project Contact | PX_Objects_PM_PMContact, ProjectContact, PMContact | ContactID | OverrideContact |  |
| PX.Objects.PM.PMCostBudget | Project Cost Budget | PX_Objects_PM_PMCostBudget, ProjectCostBudget, PMCostBudget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID |  |  |
| PX.Objects.PM.PMCostCode | Cost Code | PX_Objects_PM_PMCostCode, CostCode, PMCostCode | CostCodeCD | IsProjectOverride, NoteText |  |
| PX.Objects.PM.PMCostProjection | Cost Projection | PX_Objects_PM_PMCostProjection, CostProjection, PMCostProjection | ProjectID, RevisionID | FormCaptionDescription, NoteText |  |
| PX.Objects.PM.PMCostProjectionByDate | Cost Projection By Date | PX_Objects_PM_PMCostProjectionByDate, CostProjectionByDate, PMCostProjectionByDate | RefNbr | CuryCompletedAmountTotal, CompletedAmountTotal, CompletedPctTotal, CuryBudgetBacklogAmountTotal, BudgetBacklogAmountTotal, CuryRevenueBudgetBacklogAmountTotal, RevenueBudgetBacklogAmountTotal, CuryExpectedAmountTotal, ExpectedAmountTotal, CuryRevenueExpectedAmountTotal, RevenueExpectedAmountTotal, PerformanceTotal, AnticipatedPerformanceTotal, CuryOverbillingAmountTotal, OverbillingAmountTotal, ProjectedMarginTotal, CompletedQtyPctTotal, NoteText |  |
| PX.Objects.PM.PMCostProjectionByDateLine | Cost Projection By Date Line | PX_Objects_PM_PMCostProjectionByDateLine, CostProjectionByDateLine, PMCostProjectionByDateLine | LineNbr, RefNbr | CuryCompletedAmount, CompletedAmount, CuryBudgetBacklogAmount, BudgetBacklogAmount, Performance, AnticipatedPerformance, AnticipatedQty, CuryAnticipatedUnitRate, AnticipatedUnitRate, QtyPerformance, AnticipatedQtyPerformance, ProjectedQtyVariance, CuryProjectedCostVariance, ProjectedCostVariance, IsHeader, NoteText |  |
| PX.Objects.PM.PMCostProjectionClass | Cost Projection Class | PX_Objects_PM_PMCostProjectionClass, CostProjectionClass, PMCostProjectionClass | ClassID | NoteText |  |
| PX.Objects.PM.PMCostProjectionLine | Cost Projection Line | PX_Objects_PM_PMCostProjectionLine, CostProjectionLine, PMCostProjectionLine | LineNbr, ProjectID, RevisionID | CompletedQuantity, CompletedAmount, QuantityToComplete, AmountToComplete, NoteText |  |
| PX.Objects.PM.PMEmployeeRate | PM Item Employee | PX_Objects_PM_PMEmployeeRate, PMItemEmployee, PMEmployeeRate | EmployeeID, RateCodeID, RateDefinitionID |  |  |
| PX.Objects.PM.PMForecast | Budget Forecast | PX_Objects_PM_PMForecast, BudgetForecast, PMForecast | ProjectID, RevisionID | FormCaptionDescription, NoteText |  |
| PX.Objects.PM.PMForecastDetail | Budget Forecast Detail | PX_Objects_PM_PMForecastDetail, BudgetForecastDetail, PMForecastDetail | AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID, RevisionID | NoteText |  |
| PX.Objects.PM.PMForecastHistory | Budget Forecast History | PX_Objects_PM_PMForecastHistory, BudgetForecastHistory, PMForecastHistory | AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID |  |  |
| PX.Objects.PM.PMForecastProject | Project | PX_Objects_PM_PMForecastProject, Project1, PMForecastProject | ContractID | TotalBudgetedCompletedAmount, TotalBudgetedAmountToComplete, TotalBudgetedGrossProfit, TotalProjectedGrossProfit |  |
| PX.Objects.PM.PMHistory | Project History | PX_Objects_PM_PMHistory, ProjectHistory, PMHistory | AccountGroupID, BranchID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID | BranchID |  |
| PX.Objects.PM.PMHistoryByDate | Project History By Date | PX_Objects_PM_PMHistoryByDate, ProjectHistoryByDate, PMHistoryByDate | AccountGroupID, CostCodeID, Date, InventoryID, PeriodID, ProjectID, ProjectTaskID | GroupID |  |
| PX.Objects.PM.PMItemRate | PM Item Rate | PX_Objects_PM_PMItemRate, PMItemRate | InventoryID, RateCodeID, RateDefinitionID |  |  |
| PX.Objects.PM.PMLaborCostRate | Labor Cost Rates | PX_Objects_PM_PMLaborCostRate, LaborCostRates, PMLaborCostRate | RecordID | UOM, NoteText |  |
| PX.Objects.PM.PMMarkup | Markup | PX_Objects_PM_PMMarkup, Markup2, PMMarkup | LineNbr, ProjectID | NoteText |  |
| PX.Objects.PM.PMPOHistoryByDate | Project Commitment History | PX_Objects_PM_PMPOHistoryByDate, ProjectCommitmentHistory, PMPOHistoryByDate | COLineNbr, CONbr, Date, POLineNbr, POOrderNbr, POOrderType, RecordType |  |  |
| PX.Objects.PM.PMProfitHistoryByDate | PMProfitHistoryByDate | PX_Objects_PM_PMProfitHistoryByDate, PMProfitHistoryByDate | AccountGroupID, ProjectID, TaskID |  |  |
| PX.Objects.PM.PMProforma | Pro Forma Invoice | PX_Objects_PM_PMProforma, ProFormaInvoice, PMProforma | RefNbr, RevisionID | CuryTaxTotalWithRetainage, ARInvoiceRefName, NoteText, CuryRate |  |
| PX.Objects.PM.PMProformaLine | Pro Forma Line | PX_Objects_PM_PMProformaLine, ProFormaLine, PMProformaLine | LineNbr, RefNbr, RevisionID | CompletedPct, CurrentInvoicedPct, NoteText |  |
| PX.Objects.PM.PMProformaLineWithPrevious | Pro Forma Line | PX_Objects_PM_PMProformaLineWithPrevious, ProFormaLine1, PMProformaLineWithPrevious | LineNbr, RefNbr, RevisionID |  | yes |
| PX.Objects.PM.PMProformaProgressLine | Pro Forma Line | PX_Objects_PM_PMProformaProgressLine, ProFormaLine2, PMProformaProgressLine | LineNbr, RefNbr, RevisionID |  |  |
| PX.Objects.PM.PMProformaRevision | Pro Forma Invoice Revision | PX_Objects_PM_PMProformaRevision, ProFormaInvoiceRevision, PMProformaRevision | RefNbr, RevisionID |  |  |
| PX.Objects.PM.PMProformaTransactLine | Pro Forma Line | PX_Objects_PM_PMProformaTransactLine, ProFormaLine3, PMProformaTransactLine | LineNbr, RefNbr, RevisionID | CuryMaxAmount, MaxAmount, CuryAvailableAmount, AvailableAmount, CuryOverflowAmount, OverflowAmount |  |
| PX.Objects.PM.PMProgressLineTotal | Pro Forma Line | PX_Objects_PM_PMProgressLineTotal, ProFormaLine4, PMProgressLineTotal | AccountGroupID, ProjectID, RefNbr, TaskID |  |  |
| PX.Objects.PM.PMProgressWorksheet | Progress Worksheet | PX_Objects_PM_PMProgressWorksheet, ProgressWorksheet, PMProgressWorksheet | RefNbr | HiddenRefNbr, HiddenStatus, NoteText |  |
| PX.Objects.PM.PMProgressWorksheetCostLine | Progress Worksheet Cost Line | PX_Objects_PM_PMProgressWorksheetCostLine, ProgressWorksheetCostLine, PMProgressWorksheetCostLine | LineNbr, RefNbr |  |  |
| PX.Objects.PM.PMProgressWorksheetLine | Progress Worksheet Line | PX_Objects_PM_PMProgressWorksheetLine, ProgressWorksheetLine, PMProgressWorksheetLine | LineNbr, RefNbr | Description, UOM, PreviouslyCompletedQuantity, PriorPeriodQuantity, CurrentPeriodQuantity, TotalCompletedQuantity, CompletedPercentTotalQuantity, TotalBudgetedQuantity, NoteText |  |
| PX.Objects.PM.PMProgressWorksheetRevenueLine | Progress Worksheet Revenue Line | PX_Objects_PM_PMProgressWorksheetRevenueLine, ProgressWorksheetRevenueLine, PMProgressWorksheetRevenueLine | LineNbr, RefNbr |  |  |
| PX.Objects.PM.PMProject | Project | PX_Objects_PM_PMProject, Project, PMProject | BaseType, ContractCD | ProjectType, Included, CapAmount, CuryRate |  |
| PX.Objects.PM.PMProjectBudgetHistory | Project Budget History | PX_Objects_PM_PMProjectBudgetHistory, ProjectBudgetHistory, PMProjectBudgetHistory | AccountGroupID, ChangeOrderRefNbr, CostCodeID, Date, InventoryID, ProjectID, TaskID |  |  |
| PX.Objects.PM.PMProjectBudgetProfitHistory | PMProjectBudgetProfitHistory | PX_Objects_PM_PMProjectBudgetProfitHistory, PMProjectBudgetProfitHistory | AccountGroupID, ProjectID, TaskID |  |  |
| PX.Objects.PM.PMProjectContact | Project Contact | PX_Objects_PM_PMProjectContact, ProjectContact1, PMProjectContact | ContactID, ProjectID | NoteText |  |
| PX.Objects.PM.PMProjectCostForecastTotal | Contract Total | PX_Objects_PM_PMProjectCostForecastTotal, ContractTotal, PMProjectCostForecastTotal | ProjectID | CompletedAmount |  |
| PX.Objects.PM.PMProjectCostSpread | Project Monthly Cost Spread | PX_Objects_PM_PMProjectCostSpread, ProjectMonthlyCostSpread, PMProjectCostSpread | RefNbr | CurrentPeriod, NoteText |  |
| PX.Objects.PM.PMProjectCostSpreadLine | Project Monthly Cost Spread Line | PX_Objects_PM_PMProjectCostSpreadLine, ProjectMonthlyCostSpreadLine, PMProjectCostSpreadLine | LineNbr, RefNbr | Period, VariancePTD, Variance, CostToCompletePTD, CostToComplete, EffectiveWeight, IsPastPeriod, IsCurrentPeriod, IsHeader, NoteText |  |
| PX.Objects.PM.PMProjectGroup | Project Group | PX_Objects_PM_PMProjectGroup, ProjectGroup, PMProjectGroup | ProjectGroupID | Included, NoteText, Secured |  |
| PX.Objects.PM.PMProjectRate | PM Project Rate | PX_Objects_PM_PMProjectRate, PMProjectRate | ProjectCD, RateCodeID, RateDefinitionID |  |  |
| PX.Objects.PM.PMProjectRevenueTotal | Contract Total | PX_Objects_PM_PMProjectRevenueTotal, ContractTotal1, PMProjectRevenueTotal | ProjectID | ContractCompletedPct, ContractCompletedWithCOPct |  |
| PX.Objects.PM.PMProjectTemplate | Project Template | PX_Objects_PM_PMProjectTemplate, ProjectTemplate, PMProjectTemplate | ContractCD |  |  |
| PX.Objects.PM.PMProjectUnion | Project Union Locals | PX_Objects_PM_PMProjectUnion, ProjectUnionLocals, PMProjectUnion | ProjectID, UnionID |  |  |
| PX.Objects.PM.PMQuote | Project Quote | PX_Objects_PM_PMQuote, ProjectQuote, PMQuote | QuoteNbr | Hold, SubmitCancelled, IsSetupApprovalRequired, IsDisabled, IsFirstQuote, GrossMarginAmount, CuryGrossMarginAmount, GrossMarginPct, QuoteTotal, CuryQuoteTotal, TextForProductsGrid, CuryWgtAmount, ClassID, FormCaptionDescription, SuggestRelatedItems, CuryRate |  |
| PX.Objects.PM.PMQuoteTask | Project Task | PX_Objects_PM_PMQuoteTask, ProjectTask1, PMQuoteTask | QuoteID, TaskCD | NoteText |  |
| PX.Objects.PM.PMRate | Rate | PX_Objects_PM_PMRate, Rate, PMRate | LineNbr, RateCodeID, RateDefinitionID | NoteText |  |
| PX.Objects.PM.PMRateDefinition | Rate Lookup Rule | PX_Objects_PM_PMRateDefinition, RateLookupRule, PMRateDefinition | RateDefinitionID | NoteText |  |
| PX.Objects.PM.PMRateSequence | Rate Lookup Rule Sequence | PX_Objects_PM_PMRateSequence, RateLookupRuleSequence, PMRateSequence | RateCodeID, RateTableID, RateTypeID, Sequence | NoteText |  |
| PX.Objects.PM.PMRateTable | Rate Table Code | PX_Objects_PM_PMRateTable, RateTableCode, PMRateTable | RateTableID | NoteText |  |
| PX.Objects.PM.PMRateType | Rate Type | PX_Objects_PM_PMRateType, RateType, PMRateType | RateTypeID | NoteText |  |
| PX.Objects.PM.PMRecurringItem | Recurring Items | PX_Objects_PM_PMRecurringItem, RecurringItems, PMRecurringItem | InventoryID, ProjectID, TaskID | NoteText |  |
| PX.Objects.PM.PMRegister | Project Register | PX_Objects_PM_PMRegister, ProjectRegister1, PMRegister1 | Module, RefNbr | NoteText, IsBaseCury |  |
| PX.Objects.PM.PMRetainageStep | Retainage Step | PX_Objects_PM_PMRetainageStep, RetainageStep, PMRetainageStep | LineNbr, ProjectID | NoteText |  |
| PX.Objects.PM.PMRevenueBudget | Project Revenue Budget | PX_Objects_PM_PMRevenueBudget, ProjectRevenueBudget, PMRevenueBudget | AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID |  | yes |
| PX.Objects.PM.PMRevenuePercentageCalculationRule | Revenue Percentage Calculation Rule | PX_Objects_PM_PMRevenuePercentageCalculationRule, RevenuePercentageCalculationRule, PMRevenuePercentageCalculationRule | RuleID | NoteText |  |
| PX.Objects.PM.PMShippingAddress | PM Address | PX_Objects_PM_PMShippingAddress, PMAddress1, PMShippingAddress | AddressID |  |  |
| PX.Objects.PM.PMShippingContact | Project Contact | PX_Objects_PM_PMShippingContact, ProjectContact2, PMShippingContact | ContactID |  |  |
| PX.Objects.PM.PMSiteAddress | PM Address | PX_Objects_PM_PMSiteAddress, PMAddress2, PMSiteAddress | AddressID |  |  |
| PX.Objects.PM.PMTask | Project Task | PX_Objects_PM_PMTask, ProjectTask, PMTask | ProjectID, TaskCD | FormCaptionDescription, ClassID, TemplateID, NoteText |  |
| PX.Objects.PM.PMTaskRate | PM Task Rate | PX_Objects_PM_PMTaskRate, PMTaskRate | RateCodeID, RateDefinitionID, TaskCD |  |  |
| PX.Objects.PM.PMTaskTotal | Task Total | PX_Objects_PM_PMTaskTotal, TaskTotal, PMTaskTotal | ProjectID, TaskID | CuryMargin, Margin, MarginPct |  |
| PX.Objects.PM.PMTax | PM Tax Detail | PX_Objects_PM_PMTax, PMTaxDetail, PMTax | LineNbr, RefNbr, RevisionID, TaxID | NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt |  |
| PX.Objects.PM.PMTaxTran | PM Tax | PX_Objects_PM_PMTaxTran, PMTax1, PMTaxTran | LineNbr, RecordID, RefNbr, RevisionID, TaxID |  |  |
| PX.Objects.PM.PMTran | Project Transaction | PX_Objects_PM_PMTran, ProjectTransaction, PMTran | TranID | TranIDDisplay, SourceModule, NonProject, BaseType, InvoicedDescription, TranCuryAmountCopy, IsFree, Proportion, Skip, Prefix, NoteText, IsInverted, IsCreditPair, CreatedByCurrentAllocation, CuryRate |  |
| PX.Objects.PM.PMTransferRule | Rollup Rule | PX_Objects_PM_PMTransferRule, RollupRule, PMTransferRule | TransferRuleID | NoteText |  |
| PX.Objects.PM.PMTransferRuleAccountGroupMap | Rollup Rule Account Group Map | PX_Objects_PM_PMTransferRuleAccountGroupMap, RollupRuleAccountGroupMap, PMTransferRuleAccountGroupMap | SourceAccountGroupID, TransferRuleID |  |  |
| PX.Objects.PM.PMTransferRuleCostCodeMap | Rollup Rule Cost Code Map | PX_Objects_PM_PMTransferRuleCostCodeMap, RollupRuleCostCodeMap, PMTransferRuleCostCodeMap | SourceCostCodeID, TransferRuleID |  |  |
| PX.Objects.PM.PMUnion | Union Local | PX_Objects_PM_PMUnion, UnionLocal, PMUnion | UnionID | NoteText |  |
| PX.Objects.PM.PMWipAdjustment | Project WIP Adjustment | PX_Objects_PM_PMWipAdjustment, ProjectWIPAdjustment, PMWipAdjustment | RefNbr | CuryTotalAmount, TotalAmount, CuryTotalAdjustmentAmount, TotalAdjustmentAmount, NoteText, CuryRate |  |
| PX.Objects.PM.PMWipAdjustmentLine | Project WIP Adjustment Line | PX_Objects_PM_PMWipAdjustmentLine, ProjectWIPAdjustmentLine, PMWipAdjustmentLine | LineNbr, RefNbr | CuryBudgetedRevenueChangeOrderAmount, BudgetedRevenueChangeOrderAmount, CuryBudgetedCostChangeOrderAmount, BudgetedCostChangeOrderAmount, CuryRevisedCommitmentAmount, RevisedCommitmentAmount, BudgetUsedPct, CuryGrossProfitAmount, GrossProfitAmount, MarginPct, CuryRevenueBacklogAmount, RevenueBacklogAmount, CuryGrossProfitBacklogAmount, GrossProfitBacklogAmount, CuryRemainingContractgAmount, RemainingContractgAmount, NoteText |  |
| PX.Objects.PM.PMWorkCode | WorkCode | PX_Objects_PM_PMWorkCode, WorkCode, PMWorkCode | WorkCodeID | NoteText |  |
| PX.Objects.PM.PMWorkCodeCostCodeRange | Workers' Compensation Code Cost Code Range | PX_Objects_PM_PMWorkCodeCostCodeRange, WorkersCompensationCodeCostCodeRange, PMWorkCodeCostCodeRange | LineNbr, WorkCodeID |  |  |
| PX.Objects.PM.PMWorkCodeLaborItemSource | Workers' Compensation Labor Item Source | PX_Objects_PM_PMWorkCodeLaborItemSource, WorkersCompensationLaborItemSource, PMWorkCodeLaborItemSource | LaborItemID, WorkCodeID |  |  |
| PX.Objects.PM.PMWorkCodeProjectTaskSource | Workers' Compensation Project Task Source | PX_Objects_PM_PMWorkCodeProjectTaskSource, WorkersCompensationProjectTaskSource, PMWorkCodeProjectTaskSource | LineNbr, WorkCodeID |  |  |
| PX.Objects.PM.POLinePM | PO Line | PX_Objects_PM_POLinePM, POLine, POLinePM | LineNbr, OrderNbr, OrderType | LineAmount, CalcOpenQty, CalcCuryOpenAmt |  |
| PX.Objects.PM.POOrderPM | Purchase Order | PX_Objects_PM_POOrderPM, PurchaseOrder1, POOrderPM | OrderNbr, OrderType |  |  |
| PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail | Project AR History | PX_Objects_PM_Project_Cashflow_PMProjectARTranPostDetail, ProjectARHistory, PMProjectARTranPostDetail | DocType, ID, LineNbr, RefNbr, SourceLineNbr | CuryRate, CuryViewState |  |
| PX.Objects.PM.ProjectAPTran | AP Transactions | PX_Objects_PM_ProjectAPTran, APTransactions1, ProjectAPTran | ProjectID, RefNbr, TranType |  |  |
| PX.Objects.PM.ProjectARTran | AR Transactions | PX_Objects_PM_ProjectARTran, ARTransactions1, ProjectARTran | ProjectID, RefNbr, TranType |  |  |
| PX.Objects.PM.ProjectCASplit | CA Transaction Details | PX_Objects_PM_ProjectCASplit, CATransactionDetails1, ProjectCASplit | ProjectID, RefNbr, TranType |  |  |
| PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile | Linked File | PX_Objects_PM_ProjectFiles_FileEntryForms_PMLinkedFile, LinkedFile, PMLinkedFile | FileID |  | yes |
| PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity | Project Entity | PX_Objects_PM_ProjectFiles_ProjectEntities_PMProjectEntity, ProjectEntity, PMProjectEntity | LinkedDocumentNoteID, LinkedEntityNoteID, ProjectID | LinkedDocumentNumber |  |
| PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity | Vendor Entity | PX_Objects_PM_ProjectFiles_VendorEntities_PMVendorEntity, VendorEntity, PMVendorEntity | BAccountID, LinkedDocumentNoteID, LinkedEntityNoteID | LinkedDocumentNumber |  |
| PX.Objects.PM.ProjectGLTran | GL Transaction | PX_Objects_PM_ProjectGLTran, GLTransaction1, ProjectGLTran | BatchNbr, Module, ProjectID |  |  |
| PX.Objects.PM.ProjectINTran | IN Transaction | PX_Objects_PM_ProjectINTran, INTransaction1, ProjectINTran | DocType, ProjectID, RefNbr |  |  |
| PX.Objects.PM.ProjectParentChild.PMChildProject | Child Project | PX_Objects_PM_ProjectParentChild_PMChildProject, ChildProject, PMChildProject | BaseType, ContractCD |  |  |
| PX.Objects.PM.ProjectParentChild.PMChildTask | Child Task | PX_Objects_PM_ProjectParentChild_PMChildTask, ChildTask, PMChildTask | ProjectID, TaskCD |  |  |
| PX.Objects.PM.ProjectParentChild.PMParentProject | Child Project | PX_Objects_PM_ProjectParentChild_PMParentProject, ChildProject1, PMParentProject | BaseType, ContractCD |  |  |
| PX.Objects.PM.ProjectPMTran | Project Transaction | PX_Objects_PM_ProjectPMTran, ProjectTransaction1, ProjectPMTran | ProjectID, RefNbr, TranType |  |  |
| PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc | Purchase Order to Accounts Payable Document Link | PX_Objects_PO_DAC_Projections_POBlanketOrderAPDoc, PurchaseOrdertoAccountsPayableDocumentLink, POBlanketOrderAPDoc | DocType, PONbr, POType, RefNbr | TotalAmt, StatusText |  |
| PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder | Purchase Blanket Order to Purchase Order Link | PX_Objects_PO_DAC_Projections_POBlanketOrderPOOrder, PurchaseBlanketOrdertoPurchaseOrderLink, POBlanketOrderPOOrder | OrderNbr, OrderType, PONbr, POType | NoteText, StatusText |  |
| PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt | Purchase Blanket Order to Purchase Receipt Link | PX_Objects_PO_DAC_Projections_POBlanketOrderPOReceipt, PurchaseBlanketOrdertoPurchaseReceiptLink, POBlanketOrderPOReceipt | OrderNbr, OrderType, PONbr, POType, ReceiptNbr, ReceiptType |  |  |
| PX.Objects.PO.DAC.Projections.POReceiptLineAdd | Purchase Receipt Line | PX_Objects_PO_DAC_Projections_POReceiptLineAdd | LineNbr, ReceiptNbr, ReceiptType |  |  |
| PX.Objects.PO.DropShipPOLine | PO Drop-Ship Line | PX_Objects_PO_DropShipPOLine, PODropShipLine, DropShipPOLine | LineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.PO.INTransitLineStatusSO |  | PX_Objects_PO_INTransitLineStatusSO | SOShipmentLineNbr, SOShipmentNbr |  |  |
| PX.Objects.PO.LandedCostCode | Landed Cost Code | PX_Objects_PO_LandedCostCode, LandedCostCode | LandedCostCodeID | NoteText |  |
| PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail | Landed Costs Receipt | PX_Objects_PO_LandedCosts_POReceiptLandedCostDetail, LandedCostsReceipt, POReceiptLandedCostDetail | LCDocType, LCRefNbr, POReceiptNbr, POReceiptType | CuryLineAmt |  |
| PX.Objects.PO.LandedCosts.POReceiptLineAdd | Purchase Receipt Line | PX_Objects_PO_LandedCosts_POReceiptLineAdd, PurchaseReceiptLine, POReceiptLineAdd | LineNbr, ReceiptNbr, ReceiptType |  |  |
| PX.Objects.PO.LinkLineOrder |  | PX_Objects_PO_LinkLineOrder | OrderLineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.PO.LinkLineReceipt |  | PX_Objects_PO_LinkLineReceipt | ReceiptLineNbr, ReceiptNbr, ReceiptType |  |  |
| PX.Objects.PO.POAccrualDetail | PO Accrual Detail | PX_Objects_PO_POAccrualDetail, POAccrualDetail | DocumentNoteID, LineNbr |  |  |
| PX.Objects.PO.POAccrualInquiryResult | Purchase Accrual Balance Result | PX_Objects_PO_POAccrualInquiryResult, PurchaseAccrualBalanceResult, POAccrualInquiryResult | DocumentNoteID, LineNbr | NoteText, DocumentType, DocumentNbr, VendorName, UnbilledAmt, NotAdjustedAmt, NotReceivedAmt, NotInvoicedAmt, AccrualAmt |  |
| PX.Objects.PO.POAccrualSplit | PO Accrual Allocation | PX_Objects_PO_POAccrualSplit, POAccrualAllocation, POAccrualSplit | APDocType, APLineNbr, APRefNbr, POReceiptLineNbr, POReceiptNbr, POReceiptType |  |  |
| PX.Objects.PO.POAccrualStatus | PO Accrual Status | PX_Objects_PO_POAccrualStatus, POAccrualStatus | LineNbr, RefNoteID, Type | IsAccountAffected, UOM |  |
| PX.Objects.PO.POAddress | PO Address | PX_Objects_PO_POAddress, POAddress | AddressID | OverrideAddress |  |
| PX.Objects.PO.POAdjust | Purchase Order Adjust | PX_Objects_PO_POAdjust, PurchaseOrderAdjust, POAdjust | AdjdDocType, AdjdOrderNbr, AdjdOrderType, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr | ForceDelete, NoteText |  |
| PX.Objects.PO.POCartReceipt | Receipt Cart | PX_Objects_PO_POCartReceipt, ReceiptCart1, POCartReceipt | CartID, SiteID |  |  |
| PX.Objects.PO.POContact | PO Contact | PX_Objects_PO_POContact, POContact | ContactID | OverrideContact |  |
| PX.Objects.PO.POFixedDemand | PO Fixed Demand | PX_Objects_PO_POFixedDemand, POFixedDemand | PlanID | LocalizedPlanDescr, SourceSiteDescr, OrderQty, NoteText, AddLeadTimeDays, EffPrice, ExtWeight, ExtVolume, ExtCost, DemandProjectID, CuryID, SorterString, SalesBranchID, SalesCustomerID, IsSpecialOrder |  |
| PX.Objects.PO.POLandedCostDetail | Landed Costs Detail | PX_Objects_PO_POLandedCostDetail, LandedCostsDetail, POLandedCostDetail | DocType, LineNbr, RefNbr | NoteText |  |
| PX.Objects.PO.POLandedCostDetailS |  | PX_Objects_PO_POLandedCostDetailS | DocType, LineNbr, RefNbr |  |  |
| PX.Objects.PO.POLandedCostDoc | Landed Costs Document | PX_Objects_PO_POLandedCostDoc, LandedCostsDocument, POLandedCostDoc | DocType, RefNbr | NoteText, CuryRate |  |
| PX.Objects.PO.POLandedCostDocS |  | PX_Objects_PO_POLandedCostDocS | DocType, RefNbr |  |  |
| PX.Objects.PO.POLandedCostReceipt | Landed Costs Receipt | PX_Objects_PO_POLandedCostReceipt, LandedCostsReceipt1, POLandedCostReceipt | LCDocType, LCRefNbr, POReceiptNbr, POReceiptType | LineCntr |  |
| PX.Objects.PO.POLandedCostReceiptLine | Landed Costs Receipt Line | PX_Objects_PO_POLandedCostReceiptLine, LandedCostsReceiptLine, POLandedCostReceiptLine | DocType, LineNbr, RefNbr | POReceiptBaseCuryID |  |
| PX.Objects.PO.POLandedCostTax | Landed Costs Tax Detail | PX_Objects_PO_POLandedCostTax, LandedCostsTaxDetail, POLandedCostTax | DocType, LineNbr, RefNbr, TaxID | NonDeductibleTaxRate, ExpenseAmt |  |
| PX.Objects.PO.POLandedCostTaxTran | Landed Costs Tax | PX_Objects_PO_POLandedCostTaxTran, LandedCostsTax, POLandedCostTaxTran | DocType, RecordID, RefNbr, TaxID | NonDeductibleTaxRate |  |
| PX.Objects.PO.POLine | PO Line | PX_Objects_PO_POLine, POLine1 | LineNbr, OrderNbr, OrderType | ClearPlanID, VendorLocationID, ShipToBAccountID, ShipToLocationID, CalculateDiscountsOnImport, NoteText, ItemRequiresTerms, SOOrderStatus, SOOrderType, SOOrderNbr, SOLineNbr, LeftToReceiveQty, LeftToReceiveBaseQty, NonOrderedQty, DisplayReqPrepaidQty, IsKit, OrderedQtyAltered, OverridenUOM, OverridenQty, BaseOverridenQty, CuryReceivedCost, ViewDemandEnabled |  |
| PX.Objects.PO.POLineBillingRevision | PO Line Billing Revision | PX_Objects_PO_POLineBillingRevision, POLineBillingRevision | APDocType, APRefNbr, OrderLineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.PO.POLineR |  | PX_Objects_PO_POLineR | LineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.PO.POLineRS | PO Line | PX_Objects_PO_POLineRS, POLine2, POLineRS | LineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.PO.POLineS | PO Line | PX_Objects_PO_POLineS, POLine3, POLineS | LineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.PO.PONotification | Default Notification setup | PX_Objects_PO_PONotification | SetupID |  |  |
| PX.Objects.PO.POOrder | Purchase Order | PX_Objects_PO_POOrder, PurchaseOrder, POOrder | OrderNbr, OrderType | OverrideCurrency, Rejected, RequestApproval, ExternalTaxesImportInProgress, NoteText, SiteIdErrorMessage, EmployeeID, WorkgroupID, PrintedExt, EmailedExt, UpdateVendorCost, POAccrualType, LinesStatusUpdated, IntercompanySOCancelled, IntercompanySOWithEmptyInventory, CuryRate |  |
| PX.Objects.PO.POOrderAPDoc | Purchase Order to Accounts Payable Document Link | PX_Objects_PO_POOrderAPDoc, PurchaseOrdertoAccountsPayableDocumentLink1, POOrderAPDoc | DocType, PONbr, POOrderType, RefNbr | TotalAmt, StatusText |  |
| PX.Objects.PO.POOrderDiscountDetail | Purchase Order Discount Detail | PX_Objects_PO_POOrderDiscountDetail, PurchaseOrderDiscountDetail, POOrderDiscountDetail | OrderNbr, OrderType, RecordID | IsOrigDocDiscount |  |
| PX.Objects.PO.POOrderPOReceipt | Purchase Order to Purchase Receipt Link | PX_Objects_PO_POOrderPOReceipt, PurchaseOrdertoPurchaseReceiptLink, POOrderPOReceipt | PONbr, POType, ReceiptNbr, ReceiptType | StatusText, NoteText |  |
| PX.Objects.PO.POOrderPrepayment | PO Prepayment | PX_Objects_PO_POOrderPrepayment, POPrepayment, POOrderPrepayment | APDocType, APRefNbr, OrderNbr, OrderType | StatusText |  |
| PX.Objects.PO.POOrderReceipt |  | PX_Objects_PO_POOrderReceipt | PONbr, POType, ReceiptNbr, ReceiptType | NoteText |  |
| PX.Objects.PO.POOrderReceiptLink | Purchase Receipt to Purchase Order Link | PX_Objects_PO_POOrderReceiptLink, PurchaseReceipttoPurchaseOrderLink, POOrderReceiptLink | PONbr, POType, ReceiptNbr, ReceiptType |  |  |
| PX.Objects.PO.POOrderRS | Purchase Order | PX_Objects_PO_POOrderRS | OrderNbr, OrderType |  |  |
| PX.Objects.PO.POReceipt | Purchase Receipt | PX_Objects_PO_POReceipt, PurchaseReceipt, POReceipt | ReceiptNbr, ReceiptType | NoteText, CuryControlTotal, InventoryDocType, InventoryRefNbr, ShowPurchaseOrdersTab, ShowPutAwayHistoryTab, ShowLandedCostsTab, IntercompanySOCancelled, DropshipFieldsSet, CorrectionReceiptNbr, ReversalInvtDocType, ReversalInvtRefNbr, CuryRate, DailyFieldReportId |  |
| PX.Objects.PO.POReceiptItemLotSerialAttributesHeader | POReceiptItemLotSerialAttributesHeader | PX_Objects_PO_POReceiptItemLotSerialAttributesHeader, POReceiptItemLotSerialAttributesHeader | InventoryID, LotSerialNbr, ReceiptNbr, ReceiptType | NoteText |  |
| PX.Objects.PO.POReceiptLine | Purchase Receipt Line | PX_Objects_PO_POReceiptLine, PurchaseReceiptLine1, POReceiptLine | LineNbr, ReceiptNbr, ReceiptType | TranType, AllowComplete, AllowOpen, NoteText, OrigOrderQty, OpenOrderQty, ReturnedQty, IsKit, IsLSEntryBlocked, CuryLineAmt, AllowResetCorrectionLine |  |
| PX.Objects.PO.POReceiptLinePOReceipt | Purchase Receipt Line | PX_Objects_PO_POReceiptLinePOReceipt, PurchaseReceiptLine2, POReceiptLinePOReceipt | LineNbr, ReceiptNbr, ReceiptType |  |  |
| PX.Objects.PO.POReceiptLineS | Purchase Receipt Line | PX_Objects_PO_POReceiptLineS, PurchaseReceiptLine3, POReceiptLineS | LineNbr, ReceiptNbr, ReceiptType |  |  |
| PX.Objects.PO.POReceiptLineSplit | Purchase Receipt Line Split | PX_Objects_PO_POReceiptLineSplit, PurchaseReceiptLineSplit, POReceiptLineSplit | LineNbr, ReceiptNbr, ReceiptType, SplitLineNbr | TranType, LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.PO.POReceiptSplitToCartSplitLink | Receipt Line Split To Cart Split Link | PX_Objects_PO_POReceiptSplitToCartSplitLink, ReceiptLineSplitToCartSplitLink, POReceiptSplitToCartSplitLink | CartID, CartSplitLineNbr, ReceiptLineNbr, ReceiptNbr, ReceiptSplitLineNbr, ReceiptType, SiteID |  |  |
| PX.Objects.PO.POReceiptSplitToTransferSplitLink | Receipt Line Split To Transfer Line Split Link | PX_Objects_PO_POReceiptSplitToTransferSplitLink, ReceiptLineSplitToTransferLineSplitLink, POReceiptSplitToTransferSplitLink | ReceiptLineNbr, ReceiptNbr, ReceiptSplitLineNbr, ReceiptType, TransferDocType, TransferLineNbr, TransferRefNbr, TransferSplitLineNbr |  |  |
| PX.Objects.PO.POReceiptToShipmentLink | Purchase Receipt to Shipment Link | PX_Objects_PO_POReceiptToShipmentLink, PurchaseReceipttoShipmentLink, POReceiptToShipmentLink | ReceiptNbr, ReceiptType, SOOrderNbr, SOOrderType, SOShipmentNbr, SOShipmentType |  |  |
| PX.Objects.PO.POReceivePutAwaySetup | Receive Put Away Setup | PX_Objects_PO_POReceivePutAwaySetup, ReceivePutAwaySetup, POReceivePutAwaySetup | BranchID |  |  |
| PX.Objects.PO.POReceivePutAwayUserSetup | Receive Put Away User Setup | PX_Objects_PO_POReceivePutAwayUserSetup, ReceivePutAwayUserSetup, POReceivePutAwayUserSetup | UserID |  |  |
| PX.Objects.PO.PORemitAddress | PO Remittance Address | PX_Objects_PO_PORemitAddress, PORemittanceAddress, PORemitAddress | AddressID |  |  |
| PX.Objects.PO.PORemitContact | PO Remittance Contact | PX_Objects_PO_PORemitContact, PORemittanceContact, PORemitContact | ContactID |  |  |
| PX.Objects.PO.POSetupApproval | PO Approval | PX_Objects_PO_POSetupApproval, POApproval, POSetupApproval | ApprovalID |  |  |
| PX.Objects.PO.POShipAddress | PO Shipping Address | PX_Objects_PO_POShipAddress, POShippingAddress, POShipAddress | AddressID |  |  |
| PX.Objects.PO.POShipContact | PO Shipping Contact | PX_Objects_PO_POShipContact, POShippingContact, POShipContact | ContactID |  |  |
| PX.Objects.PO.POSiteStatusSelected |  | PX_Objects_PO_POSiteStatusSelected | InventoryID | QtySelected, Rank |  |
| PX.Objects.PO.POTax | PO Tax Detail | PX_Objects_PO_POTax, POTaxDetail, POTax | LineNbr, OrderNbr, OrderType, TaxID | NonDeductibleTaxRate |  |
| PX.Objects.PO.POTaxTran | PO Tax | PX_Objects_PO_POTaxTran, POTax1, POTaxTran | LineNbr, OrderNbr, OrderType, RecordID, TaxID |  |  |
| PX.Objects.PO.POTaxTranImported | PO Tax | PX_Objects_PO_POTaxTranImported | LineNbr, OrderNbr, OrderType, RecordID, TaxID |  |  |
| PX.Objects.PO.POVendorInventory | Inventory Item Vendor Details | PX_Objects_PO_POVendorInventory, InventoryItemVendorDetails, POVendorInventory | RecordID | IsDefault, NoteText |  |
| PX.Objects.PO.VendorLocation | Vendor Location | PX_Objects_PO_VendorLocation, VendorLocation | BAccountID, LocationID |  |  |
| PX.Objects.Portals.SP.DAC.SPARPayment | Portal AR Payment | PX_Objects_Portals_SP_DAC_SPARPayment, PortalARPayment, SPARPayment | DocType, RefNbr |  |  |
| PX.Objects.Portals.SP.DAC.SPARStatement | Portal AR Statement | PX_Objects_Portals_SP_DAC_SPARStatement, PortalARStatement, SPARStatement | BranchID, StatementDate | StatementDateText |  |
| PX.Objects.Portals.SP.DAC.SPCRCase | Portal Case | PX_Objects_Portals_SP_DAC_SPCRCase, PortalCase, SPCRCase | CaseCD |  | yes |
| PX.Objects.Portals.SP.DAC.SPInventoryCartItem | Products added to the shopping cart. | PX_Objects_Portals_SP_DAC_SPInventoryCartItem, Productsaddedtotheshoppingcart, SPInventoryCartItem | RecordID | SiteIDList, UOMList, RemoveFromCart |  |
| PX.Objects.Portals.SP.DAC.SPSOOrder | Portal Sales Order | PX_Objects_Portals_SP_DAC_SPSOOrder, PortalSalesOrder, SPSOOrder | OrderNbr, OrderType |  |  |
| PX.Objects.Portals.SPPortal | Portal Configuration | PX_Objects_Portals_SPPortal, PortalConfiguration, SPPortal | PortalName | VisibleWarehouses, VisiblePaymentMethods, PrimaryColor, BackgroundColor, NoteText |  |
| PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent | Vendor Portal Compliance Notification Event | PX_Objects_Portals_Vendor_Configuration_VPComplianceNotificationEvent, VendorPortalComplianceNotificationEvent, VPComplianceNotificationEvent | NotificationEventID | NoteText |  |
| PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent | Vendor Portal Security Notification Event | PX_Objects_Portals_Vendor_Configuration_VPSecurityNotificationEvent, VendorPortalSecurityNotificationEvent, VPSecurityNotificationEvent | NotificationEventID | NoteText |  |
| PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity | Recent Activity | PX_Objects_Portals_Vendor_Dashboard_RecentActivities_VPRecentActivity, RecentActivity, VPRecentActivity | ActivityID | StatusIcon, TimeAgo |  |
| PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState | User To Do State | PX_Objects_Portals_Vendor_Dashboard_ToDo_VPToDoState, UserToDoState, VPToDoState | EntityNoteID |  |  |
| PX.Objects.PR.PRAcaAggregateGroupMember | ACA Aggregate Group Member | PX_Objects_PR_PRAcaAggregateGroupMember, ACAAggregateGroupMember, PRAcaAggregateGroupMember | MemberEin, OrgBAccountID, Year |  |  |
| PX.Objects.PR.PRAcaCompanyMonthlyInformation | ACA Company Monthly Information | PX_Objects_PR_PRAcaCompanyMonthlyInformation, ACACompanyMonthlyInformation, PRAcaCompanyMonthlyInformation | Month, OrgBAccountID, Year |  |  |
| PX.Objects.PR.PRAcaCompanyYearlyInformation | ACA Company Yearly Information | PX_Objects_PR_PRAcaCompanyYearlyInformation, ACACompanyYearlyInformation, PRAcaCompanyYearlyInformation | OrgBAccountID, Year | Ein, HeaderDescription |  |
| PX.Objects.PR.PRAcaDeductCoverageInfo | ACA Deduction Code Coverage Information | PX_Objects_PR_PRAcaDeductCoverageInfo, ACADeductionCodeCoverageInformation, PRAcaDeductCoverageInfo | CoverageType, DeductCodeID |  |  |
| PX.Objects.PR.PRAcaEmployeeMonthlyInformation | ACA Employee Monthly Information | PX_Objects_PR_PRAcaEmployeeMonthlyInformation, ACAEmployeeMonthlyInformation, PRAcaEmployeeMonthlyInformation | EmployeeID, Month, OrgBAccountID, Year |  |  |
| PX.Objects.PR.PRBandingRulePTOBank | Banding Rules | PX_Objects_PR_PRBandingRulePTOBank, BandingRules, PRBandingRulePTOBank | RecordID |  |  |
| PX.Objects.PR.PRBatch | Batch | PX_Objects_PR_PRBatch, Batch1, PRBatch | BatchNbr | IsWeeklyOrBiWeeklyPeriod, NoteText, HeaderDescription |  |
| PX.Objects.PR.PRBatchDeduct | Batch Deduction | PX_Objects_PR_PRBatchDeduct, BatchDeduction, PRBatchDeduct | BatchNbr, CodeID |  |  |
| PX.Objects.PR.PRBatchEmployee | Batch Employee | PX_Objects_PR_PRBatchEmployee, BatchEmployee, PRBatchEmployee | BatchNbr, EmployeeID | BatchStatus, PaymentRefNbr, PaymentDocAndRef, VoidPaymentDocAndRef, HasNegativeHoursEarnings |  |
| PX.Objects.PR.PRBatchOvertimeRule | Batch Overtime Rule | PX_Objects_PR_PRBatchOvertimeRule, BatchOvertimeRule, PRBatchOvertimeRule | BatchNbr, OvertimeRuleID | RuleType |  |
| PX.Objects.PR.PRBenefitDetail | Benefit Detail | PX_Objects_PR_PRBenefitDetail, BenefitDetail, PRBenefitDetail | RecordID | IsPayableBenefit, PaymentCountryID |  |
| PX.Objects.PR.PRCABatch | CA Batch for Payroll | PX_Objects_PR_PRCABatch, CABatchforPayroll, PRCABatch | BatchNbr | BatchTotal, HeaderDescription |  |
| PX.Objects.PR.PRCompanyTaxAttribute | Company Tax Setting | PX_Objects_PR_PRCompanyTaxAttribute, CompanyTaxSetting, PRCompanyTaxAttribute | SettingName | Description, AllowOverride, UseDefault, UsedForGovernmentReporting, NoteText, ErrorLevel, SettingLevelEnabled, FEINDisplaySetting, IsTaxAgency |  |
| PX.Objects.PR.PRCRAPayrollAccount | CRA Payroll Account | PX_Objects_PR_PRCRAPayrollAccount, CRAPayrollAccount, PRCRAPayrollAccount | PayrollAccountID |  |  |
| PX.Objects.PR.PRDeductCode | Deduction Code | PX_Objects_PR_PRDeductCode, DeductionCode, PRDeductCode | CodeCD | ShowApplicableWageTab, ShowGarnishmentNetIncomeTab, AssociatedSource, ShowUSTaxSettingsTab, ShowCANTaxSettingsTab, NoteText |  |
| PX.Objects.PR.PRDeductCodeBenefitIncreasingWage | Deduct Code Benefit Increasing Wage | PX_Objects_PR_PRDeductCodeBenefitIncreasingWage, DeductCodeBenefitIncreasingWage, PRDeductCodeBenefitIncreasingWage | ApplicableBenefitCodeID, DeductCodeID |  |  |
| PX.Objects.PR.PRDeductCodeDeductionDecreasingWage | Deduct Code Deduction Decreasing Wage | PX_Objects_PR_PRDeductCodeDeductionDecreasingWage, DeductCodeDeductionDecreasingWage, PRDeductCodeDeductionDecreasingWage | ApplicableDeductionCodeID, DeductCodeID |  |  |
| PX.Objects.PR.PRDeductCodeDetail | Deduction Code Taxability | PX_Objects_PR_PRDeductCodeDetail, DeductionCodeTaxability, PRDeductCodeDetail | CodeID, TaxID |  |  |
| PX.Objects.PR.PRDeductCodeEarningIncreasingWage | Deduct Code Earning Increasing Wage | PX_Objects_PR_PRDeductCodeEarningIncreasingWage, DeductCodeEarningIncreasingWage, PRDeductCodeEarningIncreasingWage | ApplicableTypeCD, DeductCodeID |  |  |
| PX.Objects.PR.PRDeductCodeTaxDecreasingWage | Deduct Code Tax Decreasing Wage | PX_Objects_PR_PRDeductCodeTaxDecreasingWage, DeductCodeTaxDecreasingWage, PRDeductCodeTaxDecreasingWage | ApplicableTaxID, DeductCodeID |  |  |
| PX.Objects.PR.PRDeductCodeTaxIncreasingWage | Deduct Code Tax Increasing Wage | PX_Objects_PR_PRDeductCodeTaxIncreasingWage, DeductCodeTaxIncreasingWage, PRDeductCodeTaxIncreasingWage | ApplicableTaxID, DeductCodeID |  |  |
| PX.Objects.PR.PRDeductionAndBenefitProjectPackage | Deductions And Benefits Project Package | PX_Objects_PR_PRDeductionAndBenefitProjectPackage, DeductionsAndBenefitsProjectPackage, PRDeductionAndBenefitProjectPackage | RecordID | CountryUS |  |
| PX.Objects.PR.PRDeductionAndBenefitUnionPackage | Deductions And Benefits Union Package | PX_Objects_PR_PRDeductionAndBenefitUnionPackage, DeductionsAndBenefitsUnionPackage, PRDeductionAndBenefitUnionPackage | RecordID |  |  |
| PX.Objects.PR.PRDeductionDetail | Deduction Details | PX_Objects_PR_PRDeductionDetail, DeductionDetails, PRDeductionDetail | RecordID | PaymentCountryID |  |
| PX.Objects.PR.PRDeductionsReducingDisposableNet | Deductions Reducing Disposable Net Income | PX_Objects_PR_PRDeductionsReducingDisposableNet, DeductionsReducingDisposableNetIncome, PRDeductionsReducingDisposableNet | ApplicableDeductionCodeID, DeductCodeID |  |  |
| PX.Objects.PR.PRDirectDepositSplit | Direct Deposit Split | PX_Objects_PR_PRDirectDepositSplit, DirectDepositSplit, PRDirectDepositSplit | DocType, LineNbr, RefNbr |  |  |
| PX.Objects.PR.PREarningDetail | Earning Detail | PX_Objects_PR_PREarningDetail, EarningDetail, PREarningDetail | RecordID | ExcelRecordID, SortingRecordID, AllowCopy, IsOvertime, IsPiecework, IsAmountBased, PTODisbursementWithFinancialTransaction, PTODisbursementWithAverageRate |  |
| PX.Objects.PR.PREarningTypeDetail | Earning Type Detail | PX_Objects_PR_PREarningTypeDetail, EarningTypeDetail, PREarningTypeDetail | CountryID, TaxID, TypeCD |  |  |
| PX.Objects.PR.PREIPremiumRate | EI Premium Rates | PX_Objects_PR_PREIPremiumRate, EIPremiumRates, PREIPremiumRate | RateID |  |  |
| PX.Objects.PR.PREmployee | Payroll Employee | PX_Objects_PR_PREmployee, PayrollEmployee, PREmployee | AcctCD | HoursPerWeek |  |
| PX.Objects.PR.PREmployeeAttribute | Employee Setting | PX_Objects_PR_PREmployeeAttribute, EmployeeSetting, PREmployeeAttribute | BAccountID, SettingName | SettingLevel, Description, UseDefault, AllowOverride, IsFederal, SortOrder, Required, UsedForGovernmentReporting, CompanyNotes, NoteText, ErrorLevel, IsEmployeeSpecific, FEINDisplaySetting, IsTaxAgency, MaskedValue |  |
| PX.Objects.PR.PREmployeeClass | Employee Payroll Class | PX_Objects_PR_PREmployeeClass, EmployeePayrollClass, PREmployeeClass | EmployeeClassID | HoursPerWeek, HoursPerYear, NoteText |  |
| PX.Objects.PR.PREmployeeClassPTOBank | Employee Class PTO Bank | PX_Objects_PR_PREmployeeClassPTOBank, EmployeeClassPTOBank, PREmployeeClassPTOBank | RecordID | CreateFinancialTransaction |  |
| PX.Objects.PR.PREmployeeClassWorkLocation | Employee Class Work Location | PX_Objects_PR_PREmployeeClassWorkLocation, EmployeeClassWorkLocation, PREmployeeClassWorkLocation | RecordID | EmployeeClassCountryID |  |
| PX.Objects.PR.PREmployeeDeduct | Employee Deduct | PX_Objects_PR_PREmployeeDeduct, EmployeeDeduct, PREmployeeDeduct | BAccountID, LineNbr | ContribType, CntCalcType, DedCalcType, IsGarnishment, EmployeeCountryID |  |
| PX.Objects.PR.PREmployeeDirectDeposit | Employee Direct Deposit | PX_Objects_PR_PREmployeeDirectDeposit, EmployeeDirectDeposit, PREmployeeDirectDeposit | BAccountID, LineNbr |  |  |
| PX.Objects.PR.PREmployeeEarning | Employee Earning | PX_Objects_PR_PREmployeeEarning, EmployeeEarning, PREmployeeEarning | BAccountID, LineNbr | IsPiecework |  |
| PX.Objects.PR.PREmployeePTOBank | Employee PTO Bank | PX_Objects_PR_PREmployeePTOBank, EmployeePTOBank, PREmployeePTOBank | BAccountID, BankID, StartDate | CreateFinancialTransaction, AllowViewAvailablePTOPaidHours |  |
| PX.Objects.PR.PREmployeePTOHistory | Employee PTO History | PX_Objects_PR_PREmployeePTOHistory, EmployeePTOHistory, PREmployeePTOHistory | RecordID |  |  |
| PX.Objects.PR.PREmployeeTax | Employee Tax | PX_Objects_PR_PREmployeeTax, EmployeeTax, PREmployeeTax | BAccountID, TaxID | State, EmployeeCountryID, ErrorLevel |  |
| PX.Objects.PR.PREmployeeTaxAttribute | Employee Tax Setting | PX_Objects_PR_PREmployeeTaxAttribute, EmployeeTaxSetting, PREmployeeTaxAttribute | BAccountID, SettingName, TaxID | Description, IsEncryptionRequired, IsEncrypted, UseDefault, AllowOverride, SortOrder, Required, State, CompanyNotes, NoteText, ErrorLevel, IsEmployeeSpecific, FEINDisplaySetting, IsTaxAgency |  |
| PX.Objects.PR.PREmployeeTaxForm | Employee Tax Form | PX_Objects_PR_PREmployeeTaxForm, EmployeeTaxForm, PREmployeeTaxForm | BatchID, EmployeeID, ProvinceOfEmployment | NotPublished, PublishedFrom, DeletedDatabaseRecord |  |
| PX.Objects.PR.PREmployeeTaxFormData | Employee Tax Form Data | PX_Objects_PR_PREmployeeTaxFormData, EmployeeTaxFormData, PREmployeeTaxFormData | BatchID, EmployeeID, FormFileType, ProvinceOfEmployment | DeletedDatabaseRecord |  |
| PX.Objects.PR.PREmployeeWorkLocation | Employee Work Location | PX_Objects_PR_PREmployeeWorkLocation, EmployeeWorkLocation, PREmployeeWorkLocation | EmployeeID, LocationID | EmployeeCountryID |  |
| PX.Objects.PR.PREntityCompanyTaxAttribute | Entity Company Tax Attribute | PX_Objects_PR_PREntityCompanyTaxAttribute, EntityCompanyTaxAttribute, PREntityCompanyTaxAttribute | EntityID, SettingName | OrganizationCD, OrganizationName, BranchCD, BranchName, EmployeeCD, EmployeeName, Branch, Company |  |
| PX.Objects.PR.PREntityTaxCodeAttribute | Entity Tax Code Attribute | PX_Objects_PR_PREntityTaxCodeAttribute, EntityTaxCodeAttribute, PREntityTaxCodeAttribute | EntityID, SettingName, TaxID | OrganizationCD, OrganizationName, BranchCD, BranchName, EmployeeCD, EmployeeName, Branch, Company |  |
| PX.Objects.PR.PRGovernmentSlip | Government Slip | PX_Objects_PR_PRGovernmentSlip, GovernmentSlip, PRGovernmentSlip | SlipName, Year |  |  |
| PX.Objects.PR.PRGovernmentSlipField | Government Slip Field | PX_Objects_PR_PRGovernmentSlipField, GovernmentSlipField, PRGovernmentSlipField | FieldCode, Page, SlipName, Year |  |  |
| PX.Objects.PR.PRLocation | Location | PX_Objects_PR_PRLocation, Location1, PRLocation | LocationCD | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet | Non-payable Benefits Increasing Disposable Net Income | PX_Objects_PR_PRNonPayableBenefitsIncreasingDisposableNet, NonpayableBenefitsIncreasingDisposableNetIncome, PRNonPayableBenefitsIncreasingDisposableNet | ApplicableBenefitCodeID, DeductCodeID |  |  |
| PX.Objects.PR.PROvertimeRule | Overtime Rule | PX_Objects_PR_PROvertimeRule, OvertimeRule, PROvertimeRule | OvertimeRuleID | OvertimeMultiplier |  |
| PX.Objects.PR.PRPayGroup | Pay Group | PX_Objects_PR_PRPayGroup, PayGroup, PRPayGroup | PayGroupID | IsPayGroupIDFilled, NoteText |  |
| PX.Objects.PR.PRPayGroupPeriod | Pay Periods | PX_Objects_PR_PRPayGroupPeriod, PayPeriods, PRPayGroupPeriod | FinPeriodID, PayGroupID | PeriodNbrAsInt, EndDateUI |  |
| PX.Objects.PR.PRPayGroupPeriodSetup | Pay Group Period Setup | PX_Objects_PR_PRPayGroupPeriodSetup, PayGroupPeriodSetup, PRPayGroupPeriodSetup | PayGroupID, PeriodNbr | EndDateUI |  |
| PX.Objects.PR.PRPayGroupYear | Pay Group Year | PX_Objects_PR_PRPayGroupYear, PayGroupYear, PRPayGroupYear | PayGroupID, Year | HeaderDescription |  |
| PX.Objects.PR.PRPayGroupYearSetup | Pay Group Calendar | PX_Objects_PR_PRPayGroupYearSetup, PayGroupCalendar, PRPayGroupYearSetup | PayGroupID | NoteText, IsWeeklyOrBiWeeklyPeriod, AdjustToPeriodStart, HasAdjustmentPeriod, BelongsToNextYear |  |
| PX.Objects.PR.PRPayment | Payment | PX_Objects_PR_PRPayment, Payment1, PRPayment | DocType, RefNbr | ReleasedToVerify, IsWeeklyOrBiWeeklyPeriod, OrganizationID, DrCr, AverageRate, ExemptFromOvertimeRules, PaymentDocAndRef, IsPrintChecksPaymentMethod, NetAmountToWords, ShowROETab, NoteText, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.PR.PRPaymentBatchExportDetails | Payment Batch Export Details | PX_Objects_PR_PRPaymentBatchExportDetails, PaymentBatchExportDetails, PRPaymentBatchExportDetails | ExportHistoryLineNbr, LineNbr, PaymentBatchNbr |  |  |
| PX.Objects.PR.PRPaymentBatchExportHistory | Payment Batch Export History | PX_Objects_PR_PRPaymentBatchExportHistory, PaymentBatchExportHistory, PRPaymentBatchExportHistory | LineNbr, PaymentBatchNbr |  |  |
| PX.Objects.PR.PRPaymentDeduct | Deduction Summary | PX_Objects_PR_PRPaymentDeduct, DeductionSummary, PRPaymentDeduct | CodeID, DocType, RefNbr, Source | NoFinancialTransaction, PaymentCountryID |  |
| PX.Objects.PR.PRPaymentEarning | Payment Earning | PX_Objects_PR_PRPaymentEarning, PaymentEarning, PRPaymentEarning | DocType, LocationID, RefNbr, TypeCD | RoundedHours |  |
| PX.Objects.PR.PRPaymentEarningAggregatedByCode | Payment Earning Aggregated by Earning Type Code | PX_Objects_PR_PRPaymentEarningAggregatedByCode, PaymentEarningAggregatedbyEarningTypeCode, PRPaymentEarningAggregatedByCode | DocType, RefNbr, TypeCD |  |  |
| PX.Objects.PR.PRPaymentFringeBenefit | Payment Fringe Benefit | PX_Objects_PR_PRPaymentFringeBenefit, PaymentFringeBenefit, PRPaymentFringeBenefit | RecordID | CalculatedFringeRate |  |
| PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate | Payment Fringe Benefit Decreasing Rate | PX_Objects_PR_PRPaymentFringeBenefitDecreasingRate, PaymentFringeBenefitDecreasingRate, PRPaymentFringeBenefitDecreasingRate | RecordID | AnnualizationException, CountryUS |  |
| PX.Objects.PR.PRPaymentFringeEarningDecreasingRate | Payment Fringe Earning Decreasing Rate | PX_Objects_PR_PRPaymentFringeEarningDecreasingRate, PaymentFringeEarningDecreasingRate, PRPaymentFringeEarningDecreasingRate | RecordID | AnnualizationException |  |
| PX.Objects.PR.PRPaymentOvertimeRule | Payment Overtime Rule | PX_Objects_PR_PRPaymentOvertimeRule, PaymentOvertimeRule, PRPaymentOvertimeRule | OvertimeRuleID, PaymentDocType, PaymentRefNbr | RuleType |  |
| PX.Objects.PR.PRPaymentProjectPackageDeduct | Payment Project Package Deduction | PX_Objects_PR_PRPaymentProjectPackageDeduct, PaymentProjectPackageDeduction, PRPaymentProjectPackageDeduct | RecordID | WageBaseHours, WageBaseAmount, DeductionCalcType, BenefitCalcType, CountryUS |  |
| PX.Objects.PR.PRPaymentPTOBank | Payment PTO Bank | PX_Objects_PR_PRPaymentPTOBank, PaymentPTOBank, PRPaymentPTOBank | BankID, DocType, EffectiveStartDate, RefNbr | EarningTypeCD, EffectiveCoefficient, TotalAccrual, TotalDisbursement, CreateFinancialTransaction, CalculationFormula |  |
| PX.Objects.PR.PRPaymentTax | Payment Tax | PX_Objects_PR_PRPaymentTax, PaymentTax, PRPaymentTax | DocType, RefNbr, TaxID | PaymentCountryID |  |
| PX.Objects.PR.PRPaymentTaxApplicableAmounts | Payment Tax Applicable Amounts | PX_Objects_PR_PRPaymentTaxApplicableAmounts, PaymentTaxApplicableAmounts, PRPaymentTaxApplicableAmounts | DocType, IsSupplemental, RefNbr, TaxID, WageTypeID | PaymentCountryID |  |
| PX.Objects.PR.PRPaymentTaxSplit | Tax Splits | PX_Objects_PR_PRPaymentTaxSplit, TaxSplits, PRPaymentTaxSplit | RecordID | CountryID |  |
| PX.Objects.PR.PRPaymentUnionPackageDeduct | Payment Union Package Deduction | PX_Objects_PR_PRPaymentUnionPackageDeduct, PaymentUnionPackageDeduction, PRPaymentUnionPackageDeduct | RecordID | WageBaseHours, WageBaseAmount, DeductionCalcType, BenefitCalcType, PaymentCountryID |  |
| PX.Objects.PR.PRPaymentWCPremium | Payment Work Compensation Premium | PX_Objects_PR_PRPaymentWCPremium, PaymentWorkCompensationPremium, PRPaymentWCPremium | BranchID, ContribType, DeductCodeID, DocType, RefNbr, WorkCodeID | WageBaseAmount, WageBaseHours, DeductionCalcType, BenefitCalcType, PaymentCountryID |  |
| PX.Objects.PR.PRPeriodTaxApplicableAmounts | Period Tax Applicable Amounts | PX_Objects_PR_PRPeriodTaxApplicableAmounts, PeriodTaxApplicableAmounts, PRPeriodTaxApplicableAmounts | EmployeeID, IsSupplemental, PeriodNbr, TaxID, WageTypeID, Year |  |  |
| PX.Objects.PR.PRPeriodTaxes | Period Taxes | PX_Objects_PR_PRPeriodTaxes, PeriodTaxes, PRPeriodTaxes | EmployeeID, PeriodNbr, TaxID, Year |  |  |
| PX.Objects.PR.PRProjectFringeBenefitRate | Project Fringe Benefit Rate | PX_Objects_PR_PRProjectFringeBenefitRate, ProjectFringeBenefitRate, PRProjectFringeBenefitRate | RecordID |  |  |
| PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct | Project Fringe Benefit Rate Reducing Deduction | PX_Objects_PR_PRProjectFringeBenefitRateReducingDeduct, ProjectFringeBenefitRateReducingDeduction, PRProjectFringeBenefitRateReducingDeduct | DeductCodeID, ProjectID | CountryUS |  |
| PX.Objects.PR.PRPTOAdjustment | PTO Adjustment | PX_Objects_PR_PRPTOAdjustment, PTOAdjustment, PRPTOAdjustment | RefNbr, Type |  |  |
| PX.Objects.PR.PRPTOAdjustmentDetail | PTO Adjustment Detail | PX_Objects_PR_PRPTOAdjustmentDetail, PTOAdjustmentDetail, PRPTOAdjustmentDetail | BAccountID, BankID, RefNbr, Type |  |  |
| PX.Objects.PR.PRPTOBank | PTO Bank | PX_Objects_PR_PRPTOBank, PTOBank, PRPTOBank | BankID | StartDateMonth, StartDateDay, PTOYearStartDate, IsPercentageBased |  |
| PX.Objects.PR.PRPTOBankApplicableEarningType | PTO Bank Applicable Earning Type | PX_Objects_PR_PRPTOBankApplicableEarningType, PTOBankApplicableEarningType, PRPTOBankApplicableEarningType | BankID, EarningTypeCD |  |  |
| PX.Objects.PR.PRPTODetail | PTO Detail | PX_Objects_PR_PRPTODetail, PTODetail, PRPTODetail | RecordID |  |  |
| PX.Objects.PR.PRRecordOfEmployment | Record Of Employment | PX_Objects_PR_PRRecordOfEmployment, RecordOfEmployment, PRRecordOfEmployment | RefNbr | NoteText |  |
| PX.Objects.PR.PRRegularTypeForOvertime | Regular Type for Overtime | PX_Objects_PR_PRRegularTypeForOvertime, RegularTypeforOvertime, PRRegularTypeForOvertime | OvertimeTypeCD, RegularTypeCD |  |  |
| PX.Objects.PR.PRROEInsurableEarningsByPayPeriod | Insurable Earnings by Pay Period | PX_Objects_PR_PRROEInsurableEarningsByPayPeriod, InsurableEarningsbyPayPeriod, PRROEInsurableEarningsByPayPeriod | PayPeriodID, RefNbr |  |  |
| PX.Objects.PR.PRROEOtherMonies | Other Monies | PX_Objects_PR_PRROEOtherMonies, OtherMonies, PRROEOtherMonies | LineNbr, RefNbr |  |  |
| PX.Objects.PR.PRROEStatutoryHolidayPay | Statutory Holiday Pay | PX_Objects_PR_PRROEStatutoryHolidayPay, StatutoryHolidayPay, PRROEStatutoryHolidayPay | LineNbr, RefNbr |  |  |
| PX.Objects.PR.PRTaxCode | Tax Code | PX_Objects_PR_PRTaxCode, TaxCode, PRTaxCode | TaxCD | NoteText, ErrorLevel |  |
| PX.Objects.PR.PRTaxCodeAttribute | Tax Code Setting | PX_Objects_PR_PRTaxCodeAttribute, TaxCodeSetting, PRTaxCodeAttribute | SettingName, TaxID | Description, IsEncryptionRequired, IsEncrypted, AllowOverride, UseDefault, State, NoteText, ErrorLevel, SettingLevelEnabled, IsEmployeeSpecific |  |
| PX.Objects.PR.PRTaxDetail | Tax Detail | PX_Objects_PR_PRTaxDetail, TaxDetail, PRTaxDetail | RecordID | AmountErrorMessage |  |
| PX.Objects.PR.PRTaxFormBatch | Tax Form Batch | PX_Objects_PR_PRTaxFormBatch, TaxFormBatch, PRTaxFormBatch | BatchID | OrgBAccountIDDynamicLabel, DeletedDatabaseRecord |  |
| PX.Objects.PR.PRTaxRegistration | Tax Registration | PX_Objects_PR_PRTaxRegistration, TaxRegistration1, PRTaxRegistration | TaxRegistrationID | Entities |  |
| PX.Objects.PR.PRTaxRegistrationAttribute | Tax Registration Attribute | PX_Objects_PR_PRTaxRegistrationAttribute, TaxRegistrationAttribute, PRTaxRegistrationAttribute | SettingName, TaxID, TaxRegistrationID |  |  |
| PX.Objects.PR.PRTaxReportingAccount | Tax Reporting Account | PX_Objects_PR_PRTaxReportingAccount, TaxReportingAccount, PRTaxReportingAccount | BAccountID |  |  |
| PX.Objects.PR.PRTaxSettingAdditionalInformation | Tax Setting Additional Information | PX_Objects_PR_PRTaxSettingAdditionalInformation, TaxSettingAdditionalInformation, PRTaxSettingAdditionalInformation | CountryID, SettingName, State |  |  |
| PX.Objects.PR.PRTaxWebServiceData | Tax Web Service Data | PX_Objects_PR_PRTaxWebServiceData, TaxWebServiceData, PRTaxWebServiceData | CountryID |  |  |
| PX.Objects.PR.PRTransactionDateException | Transaction Date Exception | PX_Objects_PR_PRTransactionDateException, TransactionDateException, PRTransactionDateException | RecordID | DayOfWeek |  |
| PX.Objects.PR.PRWorkCompensationBenefitRate | Work Compensation Benefit Rate | PX_Objects_PR_PRWorkCompensationBenefitRate, WorkCompensationBenefitRate, PRWorkCompensationBenefitRate | RecordID | IsActive, ContribType, DeductionCalcType, WorkCodeCountryID, DeductCodeCountryID |  |
| PX.Objects.PR.PRWorkCompensationMaximumInsurableWage | Work Compensation Benefit Rate | PX_Objects_PR_PRWorkCompensationMaximumInsurableWage, WorkCompensationBenefitRate1, PRWorkCompensationMaximumInsurableWage | DeductCodeID, EffectiveDate, WorkCodeID | WorkCodeCountryID |  |
| PX.Objects.PR.PRYtdDeductions | YTD Deductions | PX_Objects_PR_PRYtdDeductions, YTDDeductions, PRYtdDeductions | CodeID, EmployeeID, Year |  |  |
| PX.Objects.PR.PRYtdEarnings | YTD Earnings | PX_Objects_PR_PRYtdEarnings, YTDEarnings, PRYtdEarnings | EmployeeID, LocationID, Month, TypeCD, Year |  |  |
| PX.Objects.PR.PRYtdTaxes | YTD Taxes | PX_Objects_PR_PRYtdTaxes, YTDTaxes, PRYtdTaxes | EmployeeID, TaxID, Year |  |  |
| PX.Objects.PR.Standalone.PREarningType | Payroll Earning Type | PX_Objects_PR_Standalone_PREarningType, PayrollEarningType, PREarningType | TypeCD |  |  |
| PX.Objects.PR.Standalone.PREmployee | Payroll Employee | PX_Objects_PR_Standalone_PREmployee, PayrollEmployee1, PREmployee1 | BAccountID |  |  |
| PX.Objects.PR.Standalone.PREmployeeClass | Payroll Employee Class | PX_Objects_PR_Standalone_PREmployeeClass, PayrollEmployeeClass, PREmployeeClass1 | EmployeeClassID |  |  |
| PX.Objects.RQ.DAC.RQBudgetLedger | Budget Ledger | PX_Objects_RQ_DAC_RQBudgetLedger, BudgetLedger, RQBudgetLedger | BudgetLedgerID | OrganizationName, BaseCuryID, LedgerName |  |
| PX.Objects.RQ.RQBidding |  | PX_Objects_RQ_RQBidding | LineID | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.RQ.RQBiddingVendor | Bidding Vendor | PX_Objects_RQ_RQBiddingVendor, BiddingVendor, RQBiddingVendor | LineID | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.RQ.RQBudget | Request Budget Line | PX_Objects_RQ_RQBudget, RequestBudgetLine, RQBudget | ExpenseAcctID, ExpenseSubID | DocRequestAmt, CuryDocRequestAmt, BudgetAmt, UsageAmt |  |
| PX.Objects.RQ.RQInventoryItem |  | PX_Objects_RQ_RQInventoryItem | InventoryCD |  |  |
| PX.Objects.RQ.RQNotification | Default Notification setup | PX_Objects_RQ_RQNotification | SetupID |  |  |
| PX.Objects.RQ.RQRequest | Request | PX_Objects_RQ_RQRequest, Request, RQRequest | OrderNbr | Rejected, NoteText, VendorHidden, CustomerRequest, BudgetValidation, ApprovalWorkgroupID, ApprovalOwnerID, SiteIdErrorMessage, CuryRate, CuryViewState |  |
| PX.Objects.RQ.RQRequestClass | Request Class | PX_Objects_RQ_RQRequestClass, RequestClass, RQRequestClass | ReqClassID | NoteText |  |
| PX.Objects.RQ.RQRequestClassItem |  | PX_Objects_RQ_RQRequestClassItem | LineID |  |  |
| PX.Objects.RQ.RQRequestLine | Request Line | PX_Objects_RQ_RQRequestLine, RequestLine, RQRequestLine | LineNbr, OrderNbr | IssueStatus, NoteText, Updatable, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.RQ.RQRequestLineOwned | Request Line | PX_Objects_RQ_RQRequestLineOwned | LineNbr, OrderNbr |  |  |
| PX.Objects.RQ.RQRequestLineSelect |  | PX_Objects_RQ_RQRequestLineSelect | LineNbr, OrderNbr | SelectQty, BaseSelectQty |  |
| PX.Objects.RQ.RQRequisition | Requisition | PX_Objects_RQ_RQRequisition, Requisition, RQRequisition | ReqNbr | Rejected, NoteText, ApprovalWorkgroupID, ApprovalOwnerID, SiteIdErrorMessage, VendorRequestSent, SkipValidateWithVendorCuryOrRate, CuryRate, CuryViewState |  |
| PX.Objects.RQ.RQRequisitionContent |  | PX_Objects_RQ_RQRequisitionContent | LineNbr, OrderNbr, ReqLineNbr, ReqNbr | RecalcOnly |  |
| PX.Objects.RQ.RQRequisitionLine | Requisition Line | PX_Objects_RQ_RQRequisitionLine, RequisitionLine, RQRequisitionLine | LineNbr, ReqNbr | LineSource, NoteText, Availability, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.RQ.RQRequisitionLineBidding |  | PX_Objects_RQ_RQRequisitionLineBidding | LineNbr, ReqNbr | QuoteNumber, QuoteQty, CuryQuoteUnitCost, QuoteUnitCost, CuryQuoteExtCost, QuoteExtCost, MinQty |  |
| PX.Objects.RQ.RQRequisitionLineReceived | Requisition Line | PX_Objects_RQ_RQRequisitionLineReceived | LineNbr, ReqNbr | Status |  |
| PX.Objects.RQ.RQRequisitionOrder |  | PX_Objects_RQ_RQRequisitionOrder | OrderCategory, OrderNbr, OrderType, ReqNbr |  |  |
| PX.Objects.RQ.RQSetupApproval |  | PX_Objects_RQ_RQSetupApproval | ApprovalID |  |  |
| PX.Objects.RQ.RQSiteStatusSelected |  | PX_Objects_RQ_RQSiteStatusSelected | InventoryID | QtySelected, Rank |  |
| PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice | AR Transactions | PX_Objects_SO_DAC_Projections_ARTranForDirectInvoice, ARTransactions2, ARTranForDirectInvoice | LineNbr, RefNbr, TranType |  |  |
| PX.Objects.SO.DAC.Projections.BlanketSOAdjust | Blanket SO Adjustment | PX_Objects_SO_DAC_Projections_BlanketSOAdjust, BlanketSOAdjustment, BlanketSOAdjust | AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr, RecordID |  |  |
| PX.Objects.SO.DAC.Projections.BlanketSOLine | Blanket SO Line | PX_Objects_SO_DAC_Projections_BlanketSOLine, BlanketSOLine | LineNbr, OrderNbr, OrderType | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.DAC.Projections.BlanketSOLineSplit | Blanket SO Line Split | PX_Objects_SO_DAC_Projections_BlanketSOLineSplit, BlanketSOLineSplit | LineNbr, OrderNbr, OrderType, SplitLineNbr | BaseUnreceivedQty |  |
| PX.Objects.SO.DAC.Projections.BlanketSOOrder | Blanket Sales Order | PX_Objects_SO_DAC_Projections_BlanketSOOrder, BlanketSalesOrder, BlanketSOOrder | OrderNbr, OrderType | ShipmentCntrUpdated, CuryRate, CuryViewState |  |
| PX.Objects.SO.DAC.Projections.BlanketSOOrderSite | Blanket SO Order Site | PX_Objects_SO_DAC_Projections_BlanketSOOrderSite, BlanketSOOrderSite | OrderNbr, OrderType, SiteID |  |  |
| PX.Objects.SO.DAC.Projections.InvoiceSplit | Invoice Split | PX_Objects_SO_DAC_Projections_InvoiceSplit, InvoiceSplit | ARDocType, ARLineNbr, ARRefNbr, INDocType, INLineNbr, INRefNbr, INSplitLineNbr | QtyAvailForReturn, QtyReturned, QtyToReturn, SerialIsOnHand, SerialIsAlreadyReceived, SerialIsAlreadyReceivedRef, AutoCreateIssueLine |  |
| PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice | Sales Order Line | PX_Objects_SO_DAC_Projections_SOLineForDirectInvoice, SalesOrderLine, SOLineForDirectInvoice | LineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult | Credit Card Processing for Sales Result | PX_Objects_SO_DAC_Unbound_SOPaymentProcessResult, CreditCardProcessingforSalesResult, SOPaymentProcessResult | DocType, RefNbr |  | yes |
| PX.Objects.SO.DropShipSOLine | SO Drop-Ship Line | PX_Objects_SO_DropShipSOLine, SODropShipLine, DropShipSOLine | LineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.SO.POLine3 |  | PX_Objects_SO_POLine3 | LineNbr, OrderNbr, OrderType | VendorRefNbr, SOOrderType, SOOrderNbr, SOOrderLineNbr, LinkedToCurrentSOLine, DemandQty |  |
| PX.Objects.SO.Report.SOShipLineSplitForPacking | Shipment Line Split For Packing | PX_Objects_SO_Report_SOShipLineSplitForPacking, ShipmentLineSplitForPacking, SOShipLineSplitForPacking | LineNbr, ShipmentNbr, SplitLineNbr | TranType, LastLotSerialNbr, LotSerClassID, AssignedNbr |  |
| PX.Objects.SO.SalesAllocation | Sales Allocation | PX_Objects_SO_SalesAllocation, SalesAllocation | LineNbr, OrderNbr, OrderType | QtyHardAvail, QtyToAllocate, QtyToDeallocate, BufferedQty, BufferedTime, IsExtraAllocation |  |
| PX.Objects.SO.SOAddress | SO Address | PX_Objects_SO_SOAddress, SOAddress | AddressID | OverrideAddress |  |
| PX.Objects.SO.SOAdjust | Sales Order Adjust | PX_Objects_SO_SOAdjust, SalesOrderAdjust, SOAdjust | AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr, RecordID | CuryAdjgDiscAmt, CuryAdjdDiscAmt, AdjDiscAmt, CuryDocBal, CuryInitialDocBal, CuryInitialDiscBal, CuryInitialWBal, DocBal, RefTranExtNbr, ExternalRef, Authorize, Capture, Refund, NoteText, IsBalanceRecalculationRequired, NewCard, SaveCard |  |
| PX.Objects.SO.SOBillingAddress | Billing Address | PX_Objects_SO_SOBillingAddress, BillingAddress, SOBillingAddress | AddressID |  |  |
| PX.Objects.SO.SOBillingContact | Billing Contact | PX_Objects_SO_SOBillingContact, BillingContact, SOBillingContact | ContactID |  |  |
| PX.Objects.SO.SOBlanketOrderDisplayLink | Blanket Order Display Link | PX_Objects_SO_SOBlanketOrderDisplayLink, BlanketOrderDisplayLink, SOBlanketOrderDisplayLink | BlanketNbr, BlanketType, OrderNbr, OrderType | DisplayShippingRefNoteID |  |
| PX.Objects.SO.SOBlanketOrderLink | Blanket Order Link | PX_Objects_SO_SOBlanketOrderLink, BlanketOrderLink, SOBlanketOrderLink | BlanketNbr, BlanketType, OrderNbr, OrderType | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOCartShipment | Shipment Cart | PX_Objects_SO_SOCartShipment, ShipmentCart, SOCartShipment | CartID, SiteID |  |  |
| PX.Objects.SO.SOContact | SO Contact | PX_Objects_SO_SOContact, SOContact | ContactID | OverrideContact |  |
| PX.Objects.SO.SOFreightDetail | SO Freight Detail | PX_Objects_SO_SOFreightDetail, SOFreightDetail | DocType, OrderNbr, OrderType, RefNbr, ShipmentNbr, ShipmentType | NoteText |  |
| PX.Objects.SO.SOInvoice | SO Invoice | PX_Objects_SO_SOInvoice, SOInvoice | DocType, RefNbr | NoteText, ARPaymentPMInstanceID, ARPaymentPaymentMethodID, ARPaymentCashAccountID, ARPaymentExtRefNbr, ARPaymentCleared, ARPaymentClearDate, ARPaymentCATranID, ARPaymentDepositAsBatch, SuggestRelatedItems |  |
| PX.Objects.SO.SOInvoiceSiteStatusSelected | Invoice Inventory Lookup Row | PX_Objects_SO_SOInvoiceSiteStatusSelected, InvoiceInventoryLookupRow, SOInvoiceSiteStatusSelected | InventoryID | CuryID, CuryInfoID, QtySelected, CuryUnitPrice, DropShipCuryUnitPrice, Rank, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOLine | Sales Order Line | PX_Objects_SO_SOLine, SalesOrderLine1, SOLine | LineNbr, OrderNbr, OrderType | IsBeingCopied, IsKit, TranType, PlanType, RequireReasonCode, RequireShipping, RequireAllocation, RequireLocation, LineQtyAvail, LineQtyHardAvail, CalculateDiscountsOnImport, FreezeManualDisc, SkipDisc, AvgCost, NoteText, OrigIsSpecialOrder, POOrderStatus, POOrderType, POOrderNbr, POLineNbr, POLinkActive, IsPOLinkAllowed, ItemRequiresTerms, ItemHasResidual, IsCut, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOLine2 |  | PX_Objects_SO_SOLine2 | LineNbr, OrderNbr, OrderType | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOLine4 |  | PX_Objects_SO_SOLine4 | LineNbr, OrderNbr, OrderType | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOLineSplit | Sales Order Line Split | PX_Objects_SO_SOLineSplit, SalesOrderLineSplit, SOLineSplit | LineNbr, OrderNbr, OrderType, SplitLineNbr | RequireShipping, RequireAllocation, RequireLocation, IsMergeable, LotSerClassID, AssignedNbr, UnreceivedQty, BaseUnreceivedQty, OpenQty, BaseOpenQty, TranType, PlanType, ProjectID, TaskID |  |
| PX.Objects.SO.SOLineSplit2 |  | PX_Objects_SO_SOLineSplit2 | LineNbr, OrderNbr, OrderType, SplitLineNbr |  |  |
| PX.Objects.SO.SOMiscLine2 |  | PX_Objects_SO_SOMiscLine2 | LineNbr, OrderNbr, OrderType | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SONotification | Default Notification setup | PX_Objects_SO_SONotification | SetupID |  |  |
| PX.Objects.SO.SOOrchestrationPlan | Orchestration Plan | PX_Objects_SO_SOOrchestrationPlan, OrchestrationPlan, SOOrchestrationPlan | PlanID |  |  |
| PX.Objects.SO.SOOrchestrationPlanLine | Orchestration Plan Line | PX_Objects_SO_SOOrchestrationPlanLine, OrchestrationPlanLine, SOOrchestrationPlanLine | LineNbr, PlanID |  |  |
| PX.Objects.SO.SOOrder | Sales Order | PX_Objects_SO_SOOrder, SalesOrder, SOOrder | OrderNbr, OrderType | IsInvoiceOrder, DontApprove, Rejected, ShipmentDeleted, BackOrdered, NoteText, WillCall, EmployeeID, CuryTermsDiscAmt, TermsDiscAmt, DestinationSiteIdErrorMessage, ActiveOperationsCntr, DefaultTranType, UpdateNextNumber, ExternalTaxesImportInProgress, CuryDocBal, DocBal, DeferPriceDiscountRecalculation, IsPriceAndDiscountsValid, ForceCompleteOrder, ArePaymentsApplicable, IsFullyPaid, AllowsRequiredPrepayment, IsIntercompany, SuggestRelatedItems, IsCreditMemoOrder, IsRMAOrder, IsMixedOrder, IsTransferOrder, IsDebitMemoOrder, IsNoAROrder, IsCashSaleOrder, IsPaymentInfoEnabled, IsUserInvoiceNumbering, IsFreightAvailable, ShowDiscountsTab, ShowShipmentsTab, ShowOrdersTab, IsOrchestrationAllowed, KeepOrchestrationStatus, IsBeingCopied, ExtCarrierPlugIn, ExtCarrierServiceMethod, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOOrderDiscountDetail | Sales Order Discount Detail | PX_Objects_SO_SOOrderDiscountDetail, SalesOrderDiscountDetail, SOOrderDiscountDetail | OrderNbr, OrderType, RecordID | IsOrigDocDiscount, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOOrderProcessSelected | Sales Order | PX_Objects_SO_SOOrderProcessSelected | OrderNbr, OrderType |  |  |
| PX.Objects.SO.SOOrderShipment | Sales Order Shipment | PX_Objects_SO_SOOrderShipment, SalesOrderShipment, SOOrderShipment | OrderNbr, OrderType, ShippingRefNoteID | DisplayShippingRefNoteID, HasDetailDeleted, IsPartialInvoiceConstraintViolated, HasUnhandledErrors, NoteText, BillShipmentSeparately |  |
| PX.Objects.SO.SOOrderSite | SO Order Warehouse | PX_Objects_SO_SOOrderSite, SOOrderWarehouse, SOOrderSite | OrderNbr, OrderType, SiteID |  |  |
| PX.Objects.SO.SOOrderSiteStatusSelected | Sales Order Inventory Lookup Row | PX_Objects_SO_SOOrderSiteStatusSelected, SalesOrderInventoryLookupRow, SOOrderSiteStatusSelected | InventoryID | CuryID, CuryInfoID, QtySelected, CuryUnitPrice, DropShipCuryUnitPrice, Rank, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOOrderType | Order Type | PX_Objects_SO_SOOrderType, OrderType1, SOOrderType | OrderType | UserInvoiceNumbering, NoteText |  |
| PX.Objects.SO.SOOrderTypeOperation | SO Order Type Operation | PX_Objects_SO_SOOrderTypeOperation, SOOrderTypeOperation | Operation, OrderType |  |  |
| PX.Objects.SO.SOPackageDetail | SO Package Detail | PX_Objects_SO_SOPackageDetail, SOPackageDetail | LineNbr, ShipmentNbr | WeightUOM, NoteText, AllowOverrideDimension |  |
| PX.Objects.SO.SOPackageDetailEx | SO Package Detail | PX_Objects_SO_SOPackageDetailEx | LineNbr, ShipmentNbr | NetWeight |  |
| PX.Objects.SO.SOPackageInfo | SO Package Info | PX_Objects_SO_SOPackageInfo, SOPackageInfo | LineNbr, OrderNbr, OrderType | WeightUOM, AllowOverrideDimension |  |
| PX.Objects.SO.SOPackageInfoEx | SO Package Info | PX_Objects_SO_SOPackageInfoEx | LineNbr, OrderNbr, OrderType |  |  |
| PX.Objects.SO.SOPicker | SO Picker | PX_Objects_SO_SOPicker, SOPicker | PickerNbr, WorksheetNbr | PickListNbr |  |
| PX.Objects.SO.SOPickerListEntry | SO Picker List Entry | PX_Objects_SO_SOPickerListEntry, SOPickerListEntry | EntryNbr, PickerNbr, WorksheetNbr | MatchingLocationID, MatchingLotSerialNbr |  |
| PX.Objects.SO.SOPickerToShipmentLink | SO Picker to Shipment Link | PX_Objects_SO_SOPickerToShipmentLink, SOPickertoShipmentLink | PickerNbr, ShipmentNbr, SiteID, ToteID, WorksheetNbr |  |  |
| PX.Objects.SO.SOPickingJob | SO Picking Job | PX_Objects_SO_SOPickingJob, SOPickingJob | JobID | PickListNbr |  |
| PX.Objects.SO.SOPickingWorksheet | SO Shipment Picking Worksheet | PX_Objects_SO_SOPickingWorksheet, SOShipmentPickingWorksheet, SOPickingWorksheet | WorksheetNbr | NoteText |  |
| PX.Objects.SO.SOPickingWorksheetLine | SO Shipment Picking Worksheet Line | PX_Objects_SO_SOPickingWorksheetLine, SOShipmentPickingWorksheetLine, SOPickingWorksheetLine | LineNbr, WorksheetNbr |  |  |
| PX.Objects.SO.SOPickingWorksheetLineSplit | SO Shipment Picking Worksheet Line Split | PX_Objects_SO_SOPickingWorksheetLineSplit, SOShipmentPickingWorksheetLineSplit, SOPickingWorksheetLineSplit | LineNbr, SplitNbr, WorksheetNbr |  |  |
| PX.Objects.SO.SOPickingWorksheetShipment | SO Shipment Picking Worksheet Link | PX_Objects_SO_SOPickingWorksheetShipment, SOShipmentPickingWorksheetLink, SOPickingWorksheetShipment | ShipmentNbr, WorksheetNbr |  |  |
| PX.Objects.SO.SOPickListEntryToCartSplitLink | Pick List Entry To Cart Split Link | PX_Objects_SO_SOPickListEntryToCartSplitLink, PickListEntryToCartSplitLink, SOPickListEntryToCartSplitLink | CartID, CartSplitLineNbr, EntryNbr, PickerNbr, SiteID, WorksheetNbr |  |  |
| PX.Objects.SO.SOPickPackShipSetup | Pick Pack Ship Setup | PX_Objects_SO_SOPickPackShipSetup, PickPackShipSetup, SOPickPackShipSetup | BranchID |  |  |
| PX.Objects.SO.SOPickPackShipUserSetup | Pick Pack Ship User Setup | PX_Objects_SO_SOPickPackShipUserSetup, PickPackShipUserSetup, SOPickPackShipUserSetup | UserID |  |  |
| PX.Objects.SO.SOQuickProcessParameters |  | PX_Objects_SO_SOQuickProcessParameters | OrderType | AvailabilityStatus, GreenStatus, YellowStatus, RedStatus, AvailabilityMessage, AvailabilityStatusMessage, SkipByDateMsg, HideWhenNothingToPrint, ShipDateMode, ShipDate, Today, Tomorrow |  |
| PX.Objects.SO.SOSalesPerTran | SO Salesperson Commission | PX_Objects_SO_SOSalesPerTran, SOSalespersonCommission, SOSalesPerTran | OrderNbr, OrderType, SalespersonID | CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOSetupApproval | SO Approval | PX_Objects_SO_SOSetupApproval, SOApproval, SOSetupApproval | ApprovalID |  |  |
| PX.Objects.SO.SOSetupCrossSellExcludedItemClasses | SO Setup Cross Sell Excluded Item Classes | PX_Objects_SO_SOSetupCrossSellExcludedItemClasses, SOSetupCrossSellExcludedItemClasses | ItemClassID |  |  |
| PX.Objects.SO.SOSetupCrossSellExcludedOrderType | SO Setup Cross Sell Excluded Order Types | PX_Objects_SO_SOSetupCrossSellExcludedOrderType, SOSetupCrossSellExcludedOrderTypes, SOSetupCrossSellExcludedOrderType | OrderType |  |  |
| PX.Objects.SO.SOSetupInvoiceApproval | SO Invoice Approval | PX_Objects_SO_SOSetupInvoiceApproval, SOInvoiceApproval, SOSetupInvoiceApproval | ApprovalID |  |  |
| PX.Objects.SO.SOShipLine | Shipment Line | PX_Objects_SO_SOShipLine, ShipmentLine, SOShipLine | LineNbr, ShipmentNbr | TranType, OriginalShippedQty, OpenOrderQty, LineAmt, KeepManualFreight, NoteText |  |
| PX.Objects.SO.SOShipLineSplit | Shipment Line Split | PX_Objects_SO_SOShipLineSplit, ShipmentLineSplit, SOShipLineSplit | LineNbr, ShipmentNbr, SplitLineNbr | TranType, LastLotSerialNbr, LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.SO.SOShipLineSplitPackage | Shipment Package Detail | PX_Objects_SO_SOShipLineSplitPackage, ShipmentPackageDetail, SOShipLineSplitPackage | RecordID |  |  |
| PX.Objects.SO.SOShipment | Shipment | PX_Objects_SO_SOShipment, Shipment, SOShipment | ShipmentNbr | SiteBranchID, WillCall, NoteText, ConfirmedToVerify, BillingInOrders, RecalcPackagesReason, IsPackageContentDeleted, Hidden, BillSeparately, CreateARDoc, ShopForRatesErrorMessage, Excluded, ShipViaUpdateFromShopForRate, OrigDocumentNoteID, InvtDocType, InvtRefNbr, IsMaterialRelated, HasDeliverySettings, ExtCarrierServiceMethod, ShipperCountry, PJExternalStatus, ExtCarrierPlugIn, ExtIsExternalCarrierPlugIn, ExtUseScenario, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOShipmentAddress | Shipment Address | PX_Objects_SO_SOShipmentAddress, ShipmentAddress, SOShipmentAddress | AddressID |  |  |
| PX.Objects.SO.SOShipmentContact | Shipment Contact | PX_Objects_SO_SOShipmentContact, ShipmentContact, SOShipmentContact | ContactID |  |  |
| PX.Objects.SO.SOShipmentDiscountDetail | Shipment Discount Detail | PX_Objects_SO_SOShipmentDiscountDetail, ShipmentDiscountDetail, SOShipmentDiscountDetail | OrderNbr, OrderType, RecordID, ShipmentNbr, Type | IsOrigDocDiscount |  |
| PX.Objects.SO.SOShipmentManifest | SOShipmentManifest | PX_Objects_SO_SOShipmentManifest, SOShipmentManifest | ManifestNbr | NoteText |  |
| PX.Objects.SO.SOShipmentPlan |  | PX_Objects_SO_SOShipmentPlan | OrderNbr, OrderType, PlanID |  |  |
| PX.Objects.SO.SOShipmentProcessedByUser | SO Shipment Processed by User | PX_Objects_SO_SOShipmentProcessedByUser, SOShipmentProcessedbyUser | RecordID | PickListNbr |  |
| PX.Objects.SO.SOShipmentSplitToCartSplitLink | Shipment Line Split To Cart Split Link | PX_Objects_SO_SOShipmentSplitToCartSplitLink, ShipmentLineSplitToCartSplitLink, SOShipmentSplitToCartSplitLink | CartID, CartSplitLineNbr, ShipmentLineNbr, ShipmentNbr, ShipmentSplitLineNbr, SiteID |  |  |
| PX.Objects.SO.SOShippingAddress | Shipping Address | PX_Objects_SO_SOShippingAddress, ShippingAddress1, SOShippingAddress | AddressID |  |  |
| PX.Objects.SO.SOShippingContact | Shipping Contact | PX_Objects_SO_SOShippingContact, ShippingContact1, SOShippingContact | ContactID |  |  |
| PX.Objects.SO.SOTax | SO Tax Detail | PX_Objects_SO_SOTax, SOTaxDetail, SOTax | LineNbr, OrderNbr, OrderType, TaxID | NonDeductibleTaxRate, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOTaxTran | Sales Order Tax | PX_Objects_SO_SOTaxTran, SalesOrderTax, SOTaxTran | LineNbr, OrderNbr, OrderType, RecordID, TaxID, TaxZoneID | NonDeductibleTaxRate, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SO.SOTaxTranImported | Sales Order Tax | PX_Objects_SO_SOTaxTranImported | LineNbr, OrderNbr, OrderType, RecordID, TaxID, TaxZoneID |  |  |
| PX.Objects.SO.Standalone.SOOwner | Employee | PX_Objects_SO_Standalone_SOOwner, Employee2, SOOwner | AcctCD |  |  |
| PX.Objects.SO.SupplyPOLine | Supply PO Line | PX_Objects_SO_SupplyPOLine, SupplyPOLine | LineNbr, OrderNbr, OrderType | BaseDemandQty |  |
| PX.Objects.SO.Table.SOShipLineSplit |  | PX_Objects_SO_Table_SOShipLineSplit | LineNbr, ShipmentNbr, SplitLineNbr | TranType, LastLotSerialNbr, LotSerClassID, AssignedNbr, ProjectID, TaskID |  |
| PX.Objects.SV.DACUnbound.SVWorkHistoryItem | Work History | PX_Objects_SV_DACUnbound_SVWorkHistoryItem, WorkHistory, SVWorkHistoryItem | NoteID, TicketNbr |  |  |
| PX.Objects.SV.FSEmployeeSkill | Staff Skill | PX_Objects_SV_FSEmployeeSkill, StaffSkill, FSEmployeeSkill | EmployeeID, SkillID | NoteText |  |
| PX.Objects.SV.FSGeoZone | Service Area | PX_Objects_SV_FSGeoZone, ServiceArea1, FSGeoZone1 | GeoZoneCD | NoteText |  |
| PX.Objects.SV.FSGeoZonePostalCode | Postal Code | PX_Objects_SV_FSGeoZonePostalCode, PostalCode, FSGeoZonePostalCode1 | GeoZoneID, PostalCode |  |  |
| PX.Objects.SV.FSLicense | Staff License | PX_Objects_SV_FSLicense, StaffLicense, FSLicense1 | RefNbr | NoteText |  |
| PX.Objects.SV.FSLicenseType | License Type | PX_Objects_SV_FSLicenseType, LicenseType1, FSLicenseType1 | LicenseTypeCD | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.SV.FSSkill | Skill | PX_Objects_SV_FSSkill, Skill1, FSSkill1 | SkillCD | NoteText, DeletedDatabaseRecord |  |
| PX.Objects.SV.PMActivityTotal | Activities Total | PX_Objects_SV_PMActivityTotal, ActivitiesTotal, PMActivityTotal | RefNoteId |  |  |
| PX.Objects.SV.Reports.APRegister |  | PX_Objects_SV_Reports_APRegister | DocType, RefNbr | DeletedDatabaseRecord |  |
| PX.Objects.SV.Reports.APRegisterServiceReport |  | PX_Objects_SV_Reports_APRegisterServiceReport | DocType, RefNbr |  |  |
| PX.Objects.SV.Reports.APTran |  | PX_Objects_SV_Reports_APTran | RefNbr, TranType |  |  |
| PX.Objects.SV.Reports.APTran2 |  | PX_Objects_SV_Reports_APTran2 | RefNbr, TranType |  |  |
| PX.Objects.SV.Reports.ARRegister |  | PX_Objects_SV_Reports_ARRegister | DocType, RefNbr | DeletedDatabaseRecord |  |
| PX.Objects.SV.Reports.ARRegisterServiceReport |  | PX_Objects_SV_Reports_ARRegisterServiceReport | DocType, RefNbr |  |  |
| PX.Objects.SV.Reports.ARTran |  | PX_Objects_SV_Reports_ARTran | RefNbr, TranType |  |  |
| PX.Objects.SV.Reports.ARTran2 |  | PX_Objects_SV_Reports_ARTran2 | RefNbr, TranType |  |  |
| PX.Objects.SV.Reports.SVPrepaymentAdjust |  | PX_Objects_SV_Reports_SVPrepaymentAdjust | DocType, RefNbr |  |  |
| PX.Objects.SV.SVAccessibleCustomer | Customer | PX_Objects_SV_SVAccessibleCustomer, Customer4, SVAccessibleCustomer | BAccountID |  |  |
| PX.Objects.SV.SVAddress | Address | PX_Objects_SV_SVAddress, Address1, SVAddress | AddressID | OverrideAddress |  |
| PX.Objects.SV.SVAdjust | Work Order Adjust | PX_Objects_SV_SVAdjust, WorkOrderAdjust, SVAdjust | AdjdOrderNbr, AdjgDocType, AdjgRefNbr | CuryAdjgDiscAmt, CuryAdjdDiscAmt, AdjDiscAmt, CuryDocBal, DocBal, CuryInitialDocBal, CuryInitialDiscBal, CuryInitialWBal, NoteText |  |
| PX.Objects.SV.SVContact | Contact | PX_Objects_SV_SVContact, Contact3, SVContact | ContactID | OverrideContact |  |
| PX.Objects.SV.SVEmployeeLicense | Staff License | PX_Objects_SV_SVEmployeeLicense, StaffLicense1, SVEmployeeLicense | RefNbr |  |  |
| PX.Objects.SV.SVEmployeeServiceArea | Staff Service Area | PX_Objects_SV_SVEmployeeServiceArea, StaffServiceArea, SVEmployeeServiceArea | EmployeeID, GeoZoneID | NoteText |  |
| PX.Objects.SV.SVEmployeeSkill | Staff Skill | PX_Objects_SV_SVEmployeeSkill, StaffSkill1, SVEmployeeSkill | EmployeeID, SkillID |  |  |
| PX.Objects.SV.SVEvent | Work Event | PX_Objects_SV_SVEvent, WorkEvent, SVEvent | NoteID | Location, NoteText |  |
| PX.Objects.SV.SVEventLabor | Work Task Workforce | PX_Objects_SV_SVEventLabor, WorkTaskWorkforce, SVEventLabor | EventNoteID, LineNbr | DatafeedRemoveEnabled, NoteText |  |
| PX.Objects.SV.SVEventProjection | Work Event | PX_Objects_SV_SVEventProjection, WorkEvent1, SVEventProjection | NoteID |  |  |
| PX.Objects.SV.SVEventStatusColor | Work Event Status Color | PX_Objects_SV_SVEventStatusColor, WorkEventStatusColor, SVEventStatusColor | StatusID |  |  |
| PX.Objects.SV.SVEventTask | Work Event Task | PX_Objects_SV_SVEventTask, WorkEventTask, SVEventTask | EventNoteID, LineNbr | NoteText, DatafeedRemoveEnabled |  |
| PX.Objects.SV.SVInvoice | Work Order Invoice | PX_Objects_SV_SVInvoice, WorkOrderInvoice, SVInvoice | DocType, RefNbr | NoteText |  |
| PX.Objects.SV.SVLicenseType | License Type | PX_Objects_SV_SVLicenseType, LicenseType2, SVLicenseType | LicenseTypeCD |  |  |
| PX.Objects.SV.SVMarkup | Markup | PX_Objects_SV_SVMarkup, Markup, SVMarkup | MarkupID | NoteText |  |
| PX.Objects.SV.SVMyDayReport | My Day Report | PX_Objects_SV_SVMyDayReport, MyDayReport, SVMyDayReport | EmployeeID | Updated, NoteText |  |
| PX.Objects.SV.SVNotification | Default Notification setup | PX_Objects_SV_SVNotification | SetupID |  |  |
| PX.Objects.SV.SVOrder | Work Order | PX_Objects_SV_SVOrder, WorkOrder, SVOrder | OrderNbr | LocationAddress, IsExpanded, CuryDocumentDiscountTotal, DocumentDiscountTotal, ReplaceTasksAfterSave, CuryDocBal, DocBal, NoteText, CuryRate |  |
| PX.Objects.SV.SVOrderActual | Work Order Actuals | PX_Objects_SV_SVOrderActual, WorkOrderActuals, SVOrderActual | LineNbr, OrderNbr | StkItem, ProfitMarginPercent, NoteText |  |
| PX.Objects.SV.SVOrderDetail | Work Order Estimate | PX_Objects_SV_SVOrderDetail, WorkOrderEstimate, SVOrderDetail | LineNbr, OrderNbr | FreezeManualDisc, SkipDisc, StkItem, NoteText |  |
| PX.Objects.SV.SVOrderDiscountDetail | Work Order Discount | PX_Objects_SV_SVOrderDiscountDetail, WorkOrderDiscount, SVOrderDiscountDetail | OrderNbr, RecordID, Type | IsOrigDocDiscount |  |
| PX.Objects.SV.SVOrderGLAccount | Work Order GL Accounts | PX_Objects_SV_SVOrderGLAccount, WorkOrderGLAccounts, SVOrderGLAccount | BillingCategory, OrderNbr | SalesAcctCD, ExpenseAcctCD |  |
| PX.Objects.SV.SVOrderProjection | Work Order | PX_Objects_SV_SVOrderProjection, WorkOrder1, SVOrderProjection | OrderNbr |  |  |
| PX.Objects.SV.SVOrderTask | Work Order Task | PX_Objects_SV_SVOrderTask, WorkOrderTask, SVOrderTask | TaskID | SourceEventNoteID, Workforce, HasMoreEvents, EventStartDate, EventEndDate, EventDuration, EventStatus, EventSummary, EventCount, EventBandColor, DatafeedRemoveEnabled |  |
| PX.Objects.SV.SVOrderType | Work Order Type | PX_Objects_SV_SVOrderType, WorkOrderType, SVOrderType | OrderType | TotalEstDuration, NoteText |  |
| PX.Objects.SV.SVOrderTypeGLAccount | Work Order Type GL Accounts | PX_Objects_SV_SVOrderTypeGLAccount, WorkOrderTypeGLAccounts, SVOrderTypeGLAccount | BillingCategory, OrderType | SalesAcctCD, ExpenseAcctCD |  |
| PX.Objects.SV.SVOrderTypeTaskTemplate | Task Templates tab | PX_Objects_SV_SVOrderTypeTaskTemplate, TaskTemplatestab, SVOrderTypeTaskTemplate | NoteID, OrderType | NoteText |  |
| PX.Objects.SV.SVPostalCode | Postal Code | PX_Objects_SV_SVPostalCode, PostalCode1, SVPostalCode | GeoZoneID, PostalCode |  |  |
| PX.Objects.SV.SVResource | Resource | PX_Objects_SV_SVResource, Resource, SVResource | ResourceClassID, ResourceNoteID |  |  |
| PX.Objects.SV.SVResourceClass | Resource Class | PX_Objects_SV_SVResourceClass, ResourceClass, SVResourceClass | ResourceClassID | NoteText |  |
| PX.Objects.SV.SVResourceClassProperty | Resource Class Property | PX_Objects_SV_SVResourceClassProperty, ResourceClassProperty, SVResourceClassProperty | ClassPropertyID, ResourceClassID |  |  |
| PX.Objects.SV.SVResourceProperty | Resource Property | PX_Objects_SV_SVResourceProperty, ResourceProperty, SVResourceProperty | ClassPropertyID, PropertySourceID, ResourceNoteID, ResourceValue |  |  |
| PX.Objects.SV.SVResourcePropertyMapping | Resource Property Mapping | PX_Objects_SV_SVResourcePropertyMapping, ResourcePropertyMapping, SVResourcePropertyMapping | ClassPropertyID, ResourceClassID |  |  |
| PX.Objects.SV.SVServiceArea | Service Area | PX_Objects_SV_SVServiceArea, ServiceArea2, SVServiceArea | GeoZoneCD |  |  |
| PX.Objects.SV.SVServiceLocation | Service Location | PX_Objects_SV_SVServiceLocation, ServiceLocation, SVServiceLocation | ServiceLocationID | TaxRegistrationID, NoteText |  |
| PX.Objects.SV.SVServiceLocationContact | Service Location Contact | PX_Objects_SV_SVServiceLocationContact, ServiceLocationContact, SVServiceLocationContact | ServiceLocationContactID |  |  |
| PX.Objects.SV.SVServiceLocationCustomer | Service Location Customer | PX_Objects_SV_SVServiceLocationCustomer, ServiceLocationCustomer, SVServiceLocationCustomer | ServiceLocationCustomerID |  |  |
| PX.Objects.SV.SVSetupInvoiceApproval | Work Order Invoice Approval | PX_Objects_SV_SVSetupInvoiceApproval, WorkOrderInvoiceApproval, SVSetupInvoiceApproval | ApprovalID |  |  |
| PX.Objects.SV.SVSiteStatusSelected |  | PX_Objects_SV_SVSiteStatusSelected | InventoryID | CuryID, CuryInfoID, CuryUnitPrice, QtySelected, CuryRate, CuryViewState |  |
| PX.Objects.SV.SVSkill | Skill | PX_Objects_SV_SVSkill, Skill2, SVSkill | SkillCD |  |  |
| PX.Objects.SV.SVStagingWarehouse | Staging Warehouse | PX_Objects_SV_SVStagingWarehouse, StagingWarehouse, SVStagingWarehouse | BranchID | BranchCuryID |  |
| PX.Objects.SV.SVTax | Work Order Tax Detail | PX_Objects_SV_SVTax, WorkOrderTaxDetail, SVTax | LineNbr, OrderNbr, TaxID | NonDeductibleTaxRate, ExpenseAmt |  |
| PX.Objects.SV.SVTaxTran | Work Order Tax | PX_Objects_SV_SVTaxTran, WorkOrderTax, SVTaxTran | LineNbr, OrderNbr, RecordID, TaxID | TaxRate, NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt, TaxZoneID, IsTaxInclusive |  |
| PX.Objects.SV.SVTicket | Work Ticket | PX_Objects_SV_SVTicket, WorkTicket, SVTicket | TicketNbr | NoteText, BranchID, CuryRate, CuryViewState |  |
| PX.Objects.SV.SVTicketDetail | Work Ticket Detail | PX_Objects_SV_SVTicketDetail, WorkTicketDetail, SVTicketDetail | NoteID, TicketNbr | EmployeeName, IsCorrectionLocked, NoteText, CuryID, CuryRate, CuryViewState |  |
| PX.Objects.SV.SVTicketLabor | Ticket Labor Employee | PX_Objects_SV_SVTicketLabor, TicketLaborEmployee, SVTicketLabor | EmployeeID, TicketNbr |  |  |
| PX.Objects.SV.SVVendorLicense | Vendor License | PX_Objects_SV_SVVendorLicense, VendorLicense, SVVendorLicense | LicenseID |  |  |
| PX.Objects.SV.SVVendorServiceArea | Vendor Service Area | PX_Objects_SV_SVVendorServiceArea, VendorServiceArea, SVVendorServiceArea | EmployeeID, GeoZoneID | NoteText |  |
| PX.Objects.SV.SVVendorSkill | Vendor Skill | PX_Objects_SV_SVVendorSkill, VendorSkill, SVVendorSkill | EmployeeID, SkillID |  |  |
| PX.Objects.SV.SVWorkDetailsTicket | Work Details | PX_Objects_SV_SVWorkDetailsTicket, WorkDetails, SVWorkDetailsTicket | TicketNbr |  |  |
| PX.Objects.SV.SVWorkforceResource | Workforce Resource | PX_Objects_SV_SVWorkforceResource, WorkforceResource, SVWorkforceResource | ResourceClassID, ResourceNoteID |  |  |
| PX.Objects.SV.SVWorkTask | Work Task | PX_Objects_SV_SVWorkTask, WorkTask, SVWorkTask | TaskID | NoteText, SourceEventNoteID |  |
| PX.Objects.SV.SVWorkTaskAction | Work Task Action | PX_Objects_SV_SVWorkTaskAction, WorkTaskAction, SVWorkTaskAction | LineNbr, ParentNoteID |  |  |
| PX.Objects.SV.SVWorkTaskEvent | Work Task Event | PX_Objects_SV_SVWorkTaskEvent, WorkTaskEvent, SVWorkTaskEvent | NoteID | BandColor |  |
| PX.Objects.SV.SVWorkTaskLabor | Work Task Workforce | PX_Objects_SV_SVWorkTaskLabor, WorkTaskWorkforce1, SVWorkTaskLabor | LineNbr, TaskID | DatafeedRemoveEnabled, NoteText |  |
| PX.Objects.SV.SVWorkTaskResourceProperty | Work Task Template Workforce | PX_Objects_SV_SVWorkTaskResourceProperty, WorkTaskTemplateWorkforce, SVWorkTaskResourceProperty | LineNbr, TaskID | ResourceClassPropertyName, DatafeedRemoveEnabled |  |
| PX.Objects.SV.SVWorkTaskTemplate | Work Task Template | PX_Objects_SV_SVWorkTaskTemplate, WorkTaskTemplate, SVWorkTaskTemplate | TaskTemplateID |  |  |
| PX.Objects.SV.SVWorkTaskTemplateAction | Checklist tab | PX_Objects_SV_SVWorkTaskTemplateAction, Checklisttab, SVWorkTaskTemplateAction | LineNbr, TaskTemplateID |  |  |
| PX.Objects.SV.SVWorkTaskTemplateLabor | Work Task Template Workforce | PX_Objects_SV_SVWorkTaskTemplateLabor, WorkTaskTemplateWorkforce1, SVWorkTaskTemplateLabor | LineNbr, TaskTemplateID | NoteText |  |
| PX.Objects.SV.SVWorkTaskTemplateResourceProperty | Work Task Template Workforce | PX_Objects_SV_SVWorkTaskTemplateResourceProperty, WorkTaskTemplateWorkforce2, SVWorkTaskTemplateResourceProperty | LineNbr, TaskTemplateID | ResourceClassDescription, ResourceClassPropertyName |  |
| PX.Objects.SV.SVWorkTaskTotal | Time Widget | PX_Objects_SV_SVWorkTaskTotal, TimeWidget, SVWorkTaskTotal | RefNoteId |  |  |
| PX.Objects.TX.DAC.TaxTranForReporting | Tax Transaction | PX_Objects_TX_DAC_TaxTranForReporting | Module, RecordID | Sign |  |
| PX.Objects.TX.SVATConversionHist | SVAT Conversion History | PX_Objects_TX_SVATConversionHist, SVATConversionHistory, SVATConversionHist | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, Module, TaxID |  |  |
| PX.Objects.TX.SVATConversionHistExt | SVAT Conversion History | PX_Objects_TX_SVATConversionHistExt | AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, Module, TaxID | DisplayDocType |  |
| PX.Objects.TX.Tax | Tax | PX_Objects_TX_Tax, Tax | TaxID | NoteText |  |
| PX.Objects.TX.TaxAdjustment | Tax Adjustment | PX_Objects_TX_TaxAdjustment, TaxAdjustment | DocType, RefNbr | NoteText, CuryRate |  |
| PX.Objects.TX.TaxBucket | Tax Group | PX_Objects_TX_TaxBucket, TaxGroup, TaxBucket | BucketID, VendorID |  |  |
| PX.Objects.TX.TaxBucketLine | Tax Group Line | PX_Objects_TX_TaxBucketLine, TaxGroupLine, TaxBucketLine | BucketID, LineNbr, TaxReportRevisionID, VendorID |  |  |
| PX.Objects.TX.TaxCategory | Tax Category | PX_Objects_TX_TaxCategory, TaxCategory | TaxCategoryID | NoteText |  |
| PX.Objects.TX.TaxCategoryDet | Tax Category Detail | PX_Objects_TX_TaxCategoryDet, TaxCategoryDetail, TaxCategoryDet | TaxCategoryID, TaxID |  |  |
| PX.Objects.TX.TaxDetailByGLReport | Tax Report Detail | PX_Objects_TX_TaxDetailByGLReport, TaxReportDetail, TaxDetailByGLReport | Module, RecordID, RefNbr, TaxID, TranType |  |  |
| PX.Objects.TX.TaxDetailReport | Tax Report Detail | PX_Objects_TX_TaxDetailReport, TaxReportDetail1, TaxDetailReport | LineNbr, Module, RecordID, RefNbr, TaxID, TranType |  |  |
| PX.Objects.TX.TaxDetailReportCurrency | Tax Detail Report Currency | PX_Objects_TX_TaxDetailReportCurrency, TaxDetailReportCurrency | LineNbr, Module, RecordID, RefNbr, TaxID, TranType |  |  |
| PX.Objects.TX.TaxHistory | Tax History | PX_Objects_TX_TaxHistory, TaxHistory | AccountID, BranchID, LineNbr, RevisionID, SubID, TaxID, TaxPeriodID, TaxReportRevisionID, VendorID |  |  |
| PX.Objects.TX.TaxHistorySum | Tax History Sum | PX_Objects_TX_TaxHistorySum, TaxHistorySum | BranchID, LineNbr, RevisionID, TaxPeriodID, TaxReportRevisionID, VendorID |  |  |
| PX.Objects.TX.TaxPeriod | Tax Period | PX_Objects_TX_TaxPeriod, TaxPeriod | OrganizationID, TaxPeriodID, VendorID | StartDateUI, EndDateUI |  |
| PX.Objects.TX.TaxPeriodForReportShowing |  | PX_Objects_TX_TaxPeriodForReportShowing | OrganizationID, TaxPeriodID, VendorID | RevisionID |  |
| PX.Objects.TX.TaxPlugin | Tax Plug-in | PX_Objects_TX_TaxPlugin, TaxPlugin | TaxPluginID | NoteText |  |
| PX.Objects.TX.TaxPluginDetail | Tax Plug-in Details | PX_Objects_TX_TaxPluginDetail, TaxPluginDetails, TaxPluginDetail | SettingID, TaxPluginID |  |  |
| PX.Objects.TX.TaxPluginMapping | Tax Plug-in Mapping | PX_Objects_TX_TaxPluginMapping, TaxPluginMapping | BranchID, TaxPluginID |  |  |
| PX.Objects.TX.TaxReport | Tax Report | PX_Objects_TX_TaxReport, TaxReport | RevisionID, VendorID | ShowNoTemp, NoteText, NotePopupText |  |
| PX.Objects.TX.TaxReportLine | Tax Report Line | PX_Objects_TX_TaxReportLine, TaxReportLine | LineNbr, TaxReportRevisionID, VendorID | BucketSum |  |
| PX.Objects.TX.TaxReportSummary | Tax Report Summary | PX_Objects_TX_TaxReportSummary, TaxReportSummary | BranchID, LineNbr, RevisionID |  |  |
| PX.Objects.TX.TaxRev | Tax Revision | PX_Objects_TX_TaxRev, TaxRevision, TaxRev | RevisionID, TaxID |  |  |
| PX.Objects.TX.TaxTran | Tax Transaction | PX_Objects_TX_TaxTran, TaxTransaction, TaxTran | Module, RecordID | CuryEffDate |  |
| PX.Objects.TX.TaxTranReport | Tax Transaction for Report | PX_Objects_TX_TaxTranReport, TaxTransactionforReport, TaxTranReport | Module, RecordID | Sign |  |
| PX.Objects.TX.TaxYear | Tax Year | PX_Objects_TX_TaxYear, TaxYear | OrganizationID, VendorID, Year |  |  |
| PX.Objects.TX.TaxZone | Tax Zone | PX_Objects_TX_TaxZone, TaxZone | TaxZoneID | ShowTaxTabExpr, NoteText |  |
| PX.Objects.TX.TaxZoneAddressMapping | Tax Zone Address Mapping | PX_Objects_TX_TaxZoneAddressMapping, TaxZoneAddressMapping | CountryID, FromPostalCode, StateID, TaxZoneID | Description |  |
| PX.Objects.TX.TaxZoneDet | Tax Zone Detail | PX_Objects_TX_TaxZoneDet, TaxZoneDetail, TaxZoneDet | TaxID, TaxZoneID |  |  |
| PX.Objects.TX.TXImportFileData |  | PX_Objects_TX_TXImportFileData | RecordID |  |  |
| PX.Objects.TX.TXImportState |  | PX_Objects_TX_TXImportState | StateCode |  |  |
| PX.Objects.TX.TXImportZipFileData |  | PX_Objects_TX_TXImportZipFileData | RecordID |  |  |
| PX.Objects.WZ.PendingWZScenario | Wizard Scenario | PX_Objects_WZ_PendingWZScenario | ScenarioID | WorkgroupID, OwnerID, TasksCompleted |  |
| PX.Objects.WZ.WZSubTask |  | PX_Objects_WZ_WZSubTask | TaskID | Order, Offset, NoteText |  |
| PX.OidcClient.GraphExtensions.OidcUser | External Identities | PX_OidcClient_GraphExtensions_OidcUser, ExternalIdentities, OidcUser | ProviderID, ProviderName, UserID |  |  |
| PX.Olap.Maintenance.PivotField | Pivot Field | PX_Olap_Maintenance_PivotField, PivotField | PivotFieldID, PivotTableID, ScreenID | FieldName, NoteText, Cumulative, DatePartMode, Mode, SegmentNumber |  |
| PX.Olap.Maintenance.PivotFieldPreferences | Pivot Field Preferences | PX_Olap_Maintenance_PivotFieldPreferences, PivotFieldPreferences | OwnerName, PivotFieldID, PivotTableID, ScreenID |  |  |
| PX.Olap.Maintenance.PivotTable | Pivot Table | PX_Olap_Maintenance_PivotTable, PivotTable | PivotTableID, ScreenID | SitemapTitle, NoteText, WorkspaceID, SubcategoryID |  |
| PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment | Avid Child Payment | PX_PaymentProcessor_AvidXchange_DAC_PPAvidChildPayment, AvidChildPayment, PPAvidChildPayment | ChildPaymentID, DocType, RefNbr | ProofOfPayment |  |
| PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount | Avid Funding Account | PX_PaymentProcessor_AvidXchange_DAC_PPAvidFundingAccount, AvidFundingAccount, PPAvidFundingAccount | ExternalPaymentProcessorID, RecordID | CanBeOnboarded, NoteText |  |
| PX.PaymentProcessor.AvidXchange.DAC.PPAvidSetting | Avid Processor Setting | PX_PaymentProcessor_AvidXchange_DAC_PPAvidSetting, AvidProcessorSetting, PPAvidSetting | ExternalPaymentProcessorID | NoteText |  |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomBill | Payment Processor BILL Bills | PX_PaymentProcessor_BillCom_DAC_PPBillcomBill, PaymentProcessorBILLBills, PPBillcomBill | DocType, ExternalPaymentProcessorID, OrganizationID, RefNbr |  |  |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount | Payment Processor BILL Funding Accounts | PX_PaymentProcessor_BillCom_DAC_PPBillcomFundingAccount, PaymentProcessorBILLFundingAccounts, PPBillcomFundingAccount | ExternalAccountID, ExternalPaymentProcessorID, OrganizationID | CanBeDisabled, NoteText |  |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser | Payment Processor Account User | PX_PaymentProcessor_BillCom_DAC_PPBillcomFundingAccountUser, PaymentProcessorAccountUser, PPBillcomFundingAccountUser | ExternalID, ExternalPaymentProcessorID, OrganizationID | ExternalAccountStatus, Status, CanBeDisabled, NoteText |  |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomUser | Payment Processor BILL Users | PX_PaymentProcessor_BillCom_DAC_PPBillcomUser, PaymentProcessorBILLUsers, PPBillcomUser | ExternalPaymentProcessorID, OrganizationID, UserID | CanBeOnboarded, CanBeEnabled, CanBeDisabled, NoteText |  |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor | Payment Processor BILL Vendors | PX_PaymentProcessor_BillCom_DAC_PPBillcomVendor, PaymentProcessorBILLVendors, PPBillcomVendor | BAccountID, ExternalPaymentProcessorID, LocationID, OrganizationID | NetworkType, RemittanceInformationMessage, IsUSVendor, IsUSDtoUSD, IsUSDtoFC, IsFCtoFC, IsFCtoUSD |  |
| PX.PaymentProcessor.BillCom.DAC.PPBillcomVendorLocation | Payment Processor Vendors | PX_PaymentProcessor_BillCom_DAC_PPBillcomVendorLocation, PaymentProcessorVendors, PPBillcomVendorLocation | BAccountID, ExternalPaymentProcessorID, LocationID, OrganizationID |  |  |
| PX.PaymentProcessor.BillCom.DAC.PPExternalSetting | Payment Processor BILL Setting | PX_PaymentProcessor_BillCom_DAC_PPExternalSetting, PaymentProcessorBILLSetting, PPExternalSetting | ExternalPaymentProcessorID, OrganizationID | CanBeOnboarded, CanSubscribe, CanUnSubscribe, NoteText |  |
| PX.PaymentProcessor.ProcessorBase.DAC.APExternalPayment | APExternalPayment | PX_PaymentProcessor_ProcessorBase_DAC_APExternalPayment, APExternalPayment | DocType, RefNbr |  |  |
| PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran | External Payment Processor Transaction History | PX_PaymentProcessor_ProcessorBase_DAC_PPExternalTran, ExternalPaymentProcessorTransactionHistory, PPExternalTran | TranNbr |  |  |
| PX.PaymentProcessorCommon.DAC.PPExternal | External Payment Processor | PX_PaymentProcessorCommon_DAC_PPExternal, ExternalPaymentProcessor, PPExternal | ExternalPaymentProcessorID | DisclaimerMessage, NoteText |  |
| PX.PushNotifications.UI.DAC.DispatcherStatisticQueryDetail | DispatcherStatisticQueryDetail | PX_PushNotifications_UI_DAC_DispatcherStatisticQueryDetail, DispatcherStatisticQueryDetail | Field, Id, Query |  |  |
| PX.PushNotifications.UI.DAC.DispatcherStatistics | DispatcherStatistics | PX_PushNotifications_UI_DAC_DispatcherStatistics, DispatcherStatistics | Date, Hour, Id, Minute, QueueType, WebsiteId |  |  |
| PX.PushNotifications.UI.DAC.DispatcherStatisticSourceDetail | DispatcherStatisticSourceDetail | PX_PushNotifications_UI_DAC_DispatcherStatisticSourceDetail, DispatcherStatisticSourceDetail | Id, ScreenID, TableName |  |  |
| PX.PushNotifications.UI.DAC.DispatcherStatisticsPerHour | DispatcherStatisticsPerHour | PX_PushNotifications_UI_DAC_DispatcherStatisticsPerHour, DispatcherStatisticsPerHour | Date, Hour, Id, Minute, QueueType, WebsiteId |  |  |
| PX.PushNotifications.UI.DAC.PushNotificationsErrors |  | PX_PushNotifications_UI_DAC_PushNotificationsErrors | HookId, TransactionId |  |  |
| PX.PushNotifications.UI.DAC.PushNotificationsFailedToSend | Push Notifications Failed To Send | PX_PushNotifications_UI_DAC_PushNotificationsFailedToSend, PushNotificationsFailedToSend | HookId, Id, TransactionId | DateTimeStamp |  |
| PX.PushNotifications.UI.DAC.PushNotificationsHook | Push Notifications Hook | PX_PushNotifications_UI_DAC_PushNotificationsHook, PushNotificationsHook | Name |  |  |
| PX.PushNotifications.UI.DAC.PushNotificationsSource | Push Notifications Source | PX_PushNotifications_UI_DAC_PushNotificationsSource, PushNotificationsSource | HookId, LineNbr |  |  |
| PX.PushNotifications.UI.DAC.PushNotificationsSourceGI | Push Notifications Source | PX_PushNotifications_UI_DAC_PushNotificationsSourceGI | HookId, LineNbr |  |  |
| PX.PushNotifications.UI.DAC.PushNotificationsSourceIC | Push Notifications Source | PX_PushNotifications_UI_DAC_PushNotificationsSourceIC | HookId, LineNbr |  |  |
| PX.PushNotifications.UI.DAC.PushNotificationsTrackingField | Push Notification Tracked Field | PX_PushNotifications_UI_DAC_PushNotificationsTrackingField, PushNotificationTrackedField, PushNotificationsTrackingField | FieldID, HookId, LineNbr, SourceType |  |  |
| PX.PushNotifications.UI.DAC.PushNotificationsTrackingFieldGI | Push Notification Tracked Field | PX_PushNotifications_UI_DAC_PushNotificationsTrackingFieldGI, PushNotificationTrackedField1, PushNotificationsTrackingFieldGI | FieldID, HookId, LineNbr, SourceType |  |  |
| PX.PushNotifications.UI.DAC.PushNotificationsTrackingFieldIC | Push Notification Tracked Field | PX_PushNotifications_UI_DAC_PushNotificationsTrackingFieldIC, PushNotificationTrackedField2, PushNotificationsTrackingFieldIC | FieldID, HookId, LineNbr, SourceType |  |  |
| PX.Salesforce.SFEntitySetup |  | PX_Salesforce_SFEntitySetup | EntityType | LastNotification, LastNotificationTime, NoteText |  |
| PX.Salesforce.SFSyncRecord |  | PX_Salesforce_SFSyncRecord | SyncRecordID | DisplayName, DeletedDatabaseRecord |  |
| PX.ScreenPreferences.DAC.GridDataPresentation |  | PX_ScreenPreferences_DAC_GridDataPresentation | PresentationID | NoteText |  |
| PX.SiteMap.DAC.SiteMap | Site Map | PX_SiteMap_DAC_SiteMap | NodeID | Workspaces, Category, External |  |
| PX.SM.Alias.CustProject |  | PX_SM_Alias_CustProject | Name |  |  |
| PX.SM.AU.SMEmail |  | PX_SM_AU_SMEmail | NoteID | NoteText, DeletedDatabaseRecord |  |
| PX.SM.AUAction |  | PX_SM_AUAction | ActionName, MenuText, ScreenID |  |  |
| PX.SM.AUArchivingRule | Archiving Rule | PX_SM_AUArchivingRule, ArchivingRule, AUArchivingRule | PrimaryType, ScreenID, TableType |  |  |
| PX.SM.AUAuditField |  | PX_SM_AUAuditField | FieldName, ScreenID, TableName | IsInserted, FieldType, FieldDisplayName |  |
| PX.SM.AUAuditHistoryStatistics | Audit History Statistics | PX_SM_AUAuditHistoryStatistics, AuditHistoryStatistics, AUAuditHistoryStatistics | TableName | NoteText |  |
| PX.SM.AUAuditSetup |  | PX_SM_AUAuditSetup | ScreenID | ScreenName, VirtualScreenID |  |
| PX.SM.AUAuditTable |  | PX_SM_AUAuditTable | ScreenID, TableName | IsInserted, TableDisplayName |  |
| PX.SM.AUAuditValues |  | PX_SM_AUAuditValues | BatchID, ChangeID |  | yes |
| PX.SM.AUCombo |  | PX_SM_AUCombo | FieldName, TableName, Value |  |  |
| PX.SM.AUDefinition |  | PX_SM_AUDefinition | DefinitionID | NoteText |  |
| PX.SM.AUDefinitionDetail |  | PX_SM_AUDefinitionDetail | DefinitionID, ScreenID | NoteText |  |
| PX.SM.AuditHistory |  | PX_SM_AuditHistory | BatchID, ChangeID |  |  |
| PX.SM.AUNotification |  | PX_SM_AUNotification | NotificationID, ScreenID | NoteText, DeletedDatabaseRecord |  |
| PX.SM.AUNotificationField |  | PX_SM_AUNotificationField | NotificationID, RowNbr, ScreenID | NoteText |  |
| PX.SM.AUNotificationFilter |  | PX_SM_AUNotificationFilter | NotificationID, RowNbr, ScreenID | NoteText |  |
| PX.SM.AUNotificationHistory |  | PX_SM_AUNotificationHistory | ExecutionDate, NotificationID, RefNoteID, ScreenID, Ticks | Ticks, BodyVirtual |  |
| PX.SM.AUNotificationParameter |  | PX_SM_AUNotificationParameter | NotificationID, RowNbr, ScreenID | NoteText |  |
| PX.SM.AUNotificationTemplate |  | PX_SM_AUNotificationTemplate | ExecutionDate, NotificationID, RefNoteID, ScreenID | Ticks |  |
| PX.SM.AUReportLink | Report Link | PX_SM_AUReportLink, ReportLink, AUReportLink | RowNbr, ScheduleID, TemplateID |  |  |
| PX.SM.AUSchedule | Schedule | PX_SM_AUSchedule, Schedule1, AUSchedule | ScheduleID | DailyLabel, WeeklyLabel, MonthlyLabel, PeriodLabel, LastRunStatus, NoteText, ShowEventsTabExpr, ShowConditionsTabExpr, ShowEmailNotificationsTabExpr, CreatedFromBusinessEvent, NextRunDateTime, IsCreatedFromNotification, DeletedDatabaseRecord |  |
| PX.SM.AUScheduleExecution |  | PX_SM_AUScheduleExecution | ExecutionDate, ScheduleID | ExecutionDateToDisplay, Status, Result |  |
| PX.SM.AUScheduleFill | Schedule Filter Values | PX_SM_AUScheduleFill, ScheduleFilterValues, AUScheduleFill | RowNbr, ScheduleID | NoteText |  |
| PX.SM.AUScheduleFilter | Schedule Filter | PX_SM_AUScheduleFilter, ScheduleFilter, AUScheduleFilter | RowNbr, ScheduleID | NoteText |  |
| PX.SM.AUScheduleHistory |  | PX_SM_AUScheduleHistory | ExecutionDate, RefNoteID, ScheduleID | ExecutionDateToDisplay, ExecutionStatus, Ticks |  |
| PX.SM.AUScheduleTemplate |  | PX_SM_AUScheduleTemplate | ScheduleID, TemplateID | NoteText |  |
| PX.SM.AUScreenAction |  | PX_SM_AUScreenAction | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenActionBaseState |  | PX_SM_AUScreenActionBaseState | ActionName, ScreenID |  |  |
| PX.SM.AUScreenActionProp |  | PX_SM_AUScreenActionProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenActionState |  | PX_SM_AUScreenActionState | ActionName, ScreenID |  |  |
| PX.SM.AUScreenCondition |  | PX_SM_AUScreenCondition | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenConditionFilter |  | PX_SM_AUScreenConditionFilter | ConditionID, ProjectID, RowNbr, ScreenID |  |  |
| PX.SM.AUScreenConditionLineState |  | PX_SM_AUScreenConditionLineState | ConditionID, LineNbr, ScreenID |  |  |
| PX.SM.AUScreenConditionState |  | PX_SM_AUScreenConditionState | ConditionID, ScreenID | Order, IsSystem, Expression, CalcStatus |  |
| PX.SM.AUScreenDefinition |  | PX_SM_AUScreenDefinition | ProjectID, ScreenID |  |  |
| PX.SM.AUScreenEvent |  | PX_SM_AUScreenEvent | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  | yes |
| PX.SM.AUScreenEventDef |  | PX_SM_AUScreenEventDef | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenEventEndCondition |  | PX_SM_AUScreenEventEndCondition | ConditionID, ProjectID, RowNbr, ScreenID |  |  |
| PX.SM.AUScreenEventProp |  | PX_SM_AUScreenEventProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenEventStartCondition |  | PX_SM_AUScreenEventStartCondition | ConditionID, ProjectID, RowNbr, ScreenID |  |  |
| PX.SM.AUScreenEventSubscriber |  | PX_SM_AUScreenEventSubscriber | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  | yes |
| PX.SM.AUScreenEventSubscriberDef |  | PX_SM_AUScreenEventSubscriberDef | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenEventSubscriberExecCondition |  | PX_SM_AUScreenEventSubscriberExecCondition | ConditionID, ProjectID, RowNbr, ScreenID |  |  |
| PX.SM.AUScreenEventSubscriberProp |  | PX_SM_AUScreenEventSubscriberProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenExtraAction |  | PX_SM_AUScreenExtraAction | ActionName, ScreenID |  |  |
| PX.SM.AUScreenFieldForm |  | PX_SM_AUScreenFieldForm | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenFieldFormProp |  | PX_SM_AUScreenFieldFormProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenFieldState |  | PX_SM_AUScreenFieldState | FieldName, ScreenID, TableName |  |  |
| PX.SM.AUScreenForm |  | PX_SM_AUScreenForm | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  | yes |
| PX.SM.AUScreenFormProp |  | PX_SM_AUScreenFormProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenInquiry |  | PX_SM_AUScreenInquiry | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenInquiryNavProp |  | PX_SM_AUScreenInquiryNavProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenInquiryProp |  | PX_SM_AUScreenInquiryProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenItem |  | PX_SM_AUScreenItem | ItemCD, ItemType, ParentID, ProjectID, ScreenID | Inherit, SortOrder |  |
| PX.SM.AUScreenItemProp |  | PX_SM_AUScreenItemProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID | PropertyName, OriginalValue, OverrideValue, Inherit, SortOrder |  |
| PX.SM.AUScreenNavigationActionState |  | PX_SM_AUScreenNavigationActionState | ActionName, ScreenID |  |  |
| PX.SM.AUScreenNavigationParameterState |  | PX_SM_AUScreenNavigationParameterState | ActionName, FieldName, ScreenID |  |  |
| PX.SM.AUScreenPopup |  | PX_SM_AUScreenPopup | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenPopupField |  | PX_SM_AUScreenPopupField | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenPopupFieldProp |  | PX_SM_AUScreenPopupFieldProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenPopupProp |  | PX_SM_AUScreenPopupProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUScreenReport |  | PX_SM_AUScreenReport | ItemCD, ItemType, ParentID, ProjectID, ScreenID |  |  |
| PX.SM.AUScreenReportProp |  | PX_SM_AUScreenReportProp | ItemID, ProjectID, PropertyID, PropertyType, ScreenID |  |  |
| PX.SM.AUStep |  | PX_SM_AUStep | ScreenID, StepID | ActionName, MenuText, FieldTableName, FieldOrigTableName, FieldName, NoteText |  |
| PX.SM.AUStepAction |  | PX_SM_AUStepAction | RowNbr, ScreenID, StepID | MenuIcon, RetryCntr, NoteText |  |
| PX.SM.AUStepCombo |  | PX_SM_AUStepCombo | FieldName, RowNbr, ScreenID, StepID, TableName | IsExplicit, Description |  |
| PX.SM.AUStepField |  | PX_SM_AUStepField | RowNbr, ScreenID, StepID | NoteText |  |
| PX.SM.AUStepFill |  | PX_SM_AUStepFill | ActionName, MenuText, RowNbr, ScreenID, StepID |  |  |
| PX.SM.AUStepFilter |  | PX_SM_AUStepFilter | RowNbr, ScreenID, StepID | NoteText |  |
| PX.SM.AUTableDefinition |  | PX_SM_AUTableDefinition | ProjectID, TableName |  |  |
| PX.SM.AUTableExtension |  | PX_SM_AUTableExtension | FieldName, ProjectID, TableName | Inherit, SortOrder |  |
| PX.SM.AUTableExtensionState |  | PX_SM_AUTableExtensionState | FieldName, StateID, TableName | ComboValues, ComboXml, DefaultValue, DefaultXml, Selector, SelectorXml |  |
| PX.SM.AUTemplate |  | PX_SM_AUTemplate | TemplateID | Graph, NoteText |  |
| PX.SM.AUTemplateData |  | PX_SM_AUTemplateData | OrderId, TemplateId | View, RowType |  |
| PX.SM.AUWorkflow | Workflow | PX_SM_AUWorkflow, Workflow, AUWorkflow | ScreenID, WorkflowGUID |  |  |
| PX.SM.AUWorkflowActionParam | Workflow Action Parameter | PX_SM_AUWorkflowActionParam, WorkflowActionParameter, AUWorkflowActionParam | ActionName, Parameter, ScreenID |  |  |
| PX.SM.AUWorkflowActionSequence | Workflow Action Sequence | PX_SM_AUWorkflowActionSequence, WorkflowActionSequence, AUWorkflowActionSequence | Condition, NextActionName, PrevActionName, ScreenID |  |  |
| PX.SM.AUWorkflowActionSequenceFormFieldValue | Dialog Box Value | PX_SM_AUWorkflowActionSequenceFormFieldValue, DialogBoxValue, AUWorkflowActionSequenceFormFieldValue | Condition, FieldName, NextActionName, PrevActionName, ScreenID |  |  |
| PX.SM.AUWorkflowActionUpdateField | Workflow Action Field | PX_SM_AUWorkflowActionUpdateField, WorkflowActionField, AUWorkflowActionUpdateField | ActionName, FieldName, ScreenID |  |  |
| PX.SM.AUWorkflowDefinition | Workflow Definition | PX_SM_AUWorkflowDefinition, WorkflowDefinition, AUWorkflowDefinition | ScreenID | AllowWorkflowCustomization |  |
| PX.SM.AUWorkflowForm |  | PX_SM_AUWorkflowForm | FormName, Screen |  |  |
| PX.SM.AUWorkflowFormField | Workflow Form Field | PX_SM_AUWorkflowFormField, WorkflowFormField, AUWorkflowFormField | FieldName, FormName, Screen |  |  |
| PX.SM.AUWorkflowHandler | Workflow Handler | PX_SM_AUWorkflowHandler, WorkflowHandler, AUWorkflowHandler | HandlerName, ScreenID |  |  |
| PX.SM.AUWorkflowHandlerUpdateField | Workflow Handler Field | PX_SM_AUWorkflowHandlerUpdateField, WorkflowHandlerField, AUWorkflowHandlerUpdateField | FieldName, HandlerName, ScreenID |  |  |
| PX.SM.AUWorkflowOnEnterStateField | Workflow Update Field On Enter State | PX_SM_AUWorkflowOnEnterStateField, WorkflowUpdateFieldOnEnterState, AUWorkflowOnEnterStateField | FieldName, ScreenID, StateName, WorkflowGUID |  |  |
| PX.SM.AUWorkflowOnLeaveStateField | Workflow Update Field On Leave State | PX_SM_AUWorkflowOnLeaveStateField, WorkflowUpdateFieldOnLeaveState, AUWorkflowOnLeaveStateField | FieldName, ScreenID, StateName, WorkflowGUID |  |  |
| PX.SM.AUWorkflowState | Workflow State | PX_SM_AUWorkflowState, WorkflowState, AUWorkflowState | Identifier, ScreenID, WorkflowGUID |  |  |
| PX.SM.AUWorkflowStateAction | State Action | PX_SM_AUWorkflowStateAction, StateAction, AUWorkflowStateAction | ActionName, ScreenID, StateName, WorkflowGUID |  |  |
| PX.SM.AUWorkflowStateActionField | Workflow Action Field | PX_SM_AUWorkflowStateActionField, WorkflowActionField1, AUWorkflowStateActionField | ActionName, FieldName, ScreenID |  |  |
| PX.SM.AUWorkflowStateActionParam | Workflow Action Parameter | PX_SM_AUWorkflowStateActionParam, WorkflowActionParameter1, AUWorkflowStateActionParam | ActionName, Parameter, ScreenID |  |  |
| PX.SM.AUWorkflowStateEventHandler | State Event Handler | PX_SM_AUWorkflowStateEventHandler, StateEventHandler, AUWorkflowStateEventHandler | HandlerName, ScreenID, StateName, WorkflowGUID |  |  |
| PX.SM.AUWorkflowStateProperty | State Property | PX_SM_AUWorkflowStateProperty, StateProperty, AUWorkflowStateProperty | FieldName, ObjectName, ScreenID, StateName, WorkflowGUID |  |  |
| PX.SM.AUWorkflowStateStatusCondition | State Status Condition | PX_SM_AUWorkflowStateStatusCondition, StateStatusCondition, AUWorkflowStateStatusCondition | Condition, ScreenID, StateName, WorkflowGUID |  |  |
| PX.SM.AUWorkflowTransition | Workflow Transition | PX_SM_AUWorkflowTransition, WorkflowTransition, AUWorkflowTransition | ScreenID, TransitionID, WorkflowGUID |  |  |
| PX.SM.AUWorkflowTransitionField | Transition Update Fields After | PX_SM_AUWorkflowTransitionField, TransitionUpdateFieldsAfter, AUWorkflowTransitionField | FieldName, ScreenID, TransitionID, WorkflowGUID |  |  |
| PX.SM.BlobProviderSettings |  | PX_SM_BlobProviderSettings | Name |  |  |
| PX.SM.BPEventInProject | Business Process Event | PX_SM_BPEventInProject | Name |  |  |
| PX.SM.Branch |  | PX_SM_Branch | BranchCD, RoleName | DeletedDatabaseRecord |  |
| PX.SM.Certificate | Certificate | PX_SM_Certificate, Certificate | Name | NoteText |  |
| PX.SM.CetrificateFile | Certificate | PX_SM_CetrificateFile | Name |  |  |
| PX.SM.CompanyByTableSize | Table Size | PX_SM_CompanyByTableSize | Company, TableName |  | yes |
| PX.SM.CustMobileSiteMap |  | PX_SM_CustMobileSiteMap | ObjectID |  | yes |
| PX.SM.CustObject |  | PX_SM_CustObject | ObjectID | ObjectName, NoteText, IsThirdParty, AccessRightsMergeRule, ScreenId, IsReadOnly |  |
| PX.SM.CustObjectMaint |  | PX_SM_CustObjectMaint | ObjectID | ShortName, UserFriendlyType, CustType, Priority |  |
| PX.SM.CustProject | Edit Project Items | PX_SM_CustProject, EditProjectItems, CustProject | Name | Initials, NoteText, ScreenNames, IsPublished, UpdateSnapshot |  |
| PX.SM.CustScreen |  | PX_SM_CustScreen | ObjectID |  | yes |
| PX.SM.CustScreenConfiguration |  | PX_SM_CustScreenConfiguration | ObjectID |  | yes |
| PX.SM.CustUserFieldsObject |  | PX_SM_CustUserFieldsObject | ObjectID |  | yes |
| PX.SM.DashboardInProject | Dashboard | PX_SM_DashboardInProject | Name |  |  |
| PX.SM.DashboardV2InProject | Dashboard | PX_SM_DashboardV2InProject | Name |  |  |
| PX.SM.DateInfo | Date Info | PX_SM_DateInfo, DateInfo | Date | MonthName, MonthInCalendar, QuarterInCalendar, DayInWeek, DayOfWeekName, WeekEnding |  |
| PX.SM.EMailAccount | Email Account | PX_SM_EMailAccount, EmailAccount | EmailAccountID | IsOfPluginType, PasswordIsDecrypted, OutcomingAuthenticationRequest, OutcomingAuthenticationDifferent, SupportReceiving, SupportSending, Included, InboxCount, OutboxCount, NoteText, CanUpdatePassword, CanSignIn, CanSignOut, Secured |  |
| PX.SM.EMailAccountStatistics | Email Account Statistics | PX_SM_EMailAccountStatistics, EmailAccountStatistics | EmailAccountID |  |  |
| PX.SM.EMailSyncAccount |  | PX_SM_EMailSyncAccount | EmployeeID, ServerID | SyncAccount, TimeZone, IsVitrual, IsContactsReset, IsEmailsReset, IsTasksReset, IsEventsReset, NoteText |  |
| PX.SM.EMailSyncAccountPreferences |  | PX_SM_EMailSyncAccountPreferences | EmployeeID, PolicyName |  |  |
| PX.SM.EMailSyncLog |  | PX_SM_EMailSyncLog | EventID |  |  |
| PX.SM.EMailSyncPolicy |  | PX_SM_EMailSyncPolicy | PolicyName |  |  |
| PX.SM.EMailSyncReference |  | PX_SM_EMailSyncReference | Address, NoteID, ServerID |  |  |
| PX.SM.EMailSyncServer |  | PX_SM_EMailSyncServer | AccountCD |  |  |
| PX.SM.EntityEndpointInProject |  | PX_SM_EntityEndpointInProject | GateVersion, InterfaceName |  |  |
| PX.SM.GiDesignInProject | Generic Inquiry | PX_SM_GiDesignInProject | Name |  |  |
| PX.SM.Instance | Application | PX_SM_Instance, Application, Instance | InstallationID |  |  |
| PX.SM.KBFeedback |  | PX_SM_KBFeedback | FeedbackID | PageID |  |
| PX.SM.KBResponse |  | PX_SM_KBResponse | ResponseID |  |  |
| PX.SM.KBResponseMark |  | PX_SM_KBResponseMark | Mark |  |  |
| PX.SM.KBResponseSummary |  | PX_SM_KBResponseSummary | PageID |  |  |
| PX.SM.Locale | Locale | PX_SM_Locale, Locale | LocaleName | CultureReadableName |  |
| PX.SM.LocaleFormat | Custom Locale Format | PX_SM_LocaleFormat, CustomLocaleFormat, LocaleFormat | FormatID |  |  |
| PX.SM.LoginTrace | Login Trace | PX_SM_LoginTrace, LoginTrace | LoginTraceID |  |  |
| PX.SM.MobileSiteMap | Mobile Site Map | PX_SM_MobileSiteMap, MobileSiteMap | ScreenID, Type |  |  |
| PX.SM.MobileSiteMapInProject | Mobile Site Map | PX_SM_MobileSiteMapInProject | ScreenID, Type |  |  |
| PX.SM.MobileSiteMapWorkspacesInProject |  | PX_SM_MobileSiteMapWorkspacesInProject | Name |  |  |
| PX.SM.MUIScreenInProject | Screen | PX_SM_MUIScreenInProject | IsPortal, NodeID, WorkspaceID |  |  |
| PX.SM.MUITileInProject | Tile | PX_SM_MUITileInProject | IsPortal, TileID |  |  |
| PX.SM.Neighbour |  | PX_SM_Neighbour | LeftEntityType, RightEntityType |  |  |
| PX.SM.Notification | Notification | PX_SM_Notification, Notification | NotificationID | NoteText, CreatedFromReport |  |
| PX.SM.NotificationReport | Notification Report | PX_SM_NotificationReport, NotificationReport | ReportID | Title, PassData |  |
| PX.SM.NotificationReportParameter | Notification Report Parameter | PX_SM_NotificationReportParameter, NotificationReportParameter | Name, ReportID | IsOverride, FromDB, ScreenID |  |
| PX.SM.OAuthClient |  | PX_SM_OAuthClient | ClientID | FullClientID |  |
| PX.SM.PortalMap | Portal Map | PX_SM_PortalMap, PortalMap | NodeID |  |  |
| PX.SM.PreferencesIdentityProvider |  | PX_SM_PreferencesIdentityProvider | InstanceKey, ProviderName |  |  |
| PX.SM.PushNotificationInProject | Push Notifications Hook | PX_SM_PushNotificationInProject | Name |  |  |
| PX.SM.Reduced.UploadFile |  | PX_SM_Reduced_UploadFile | FileID |  |  |
| PX.SM.Reduced.WikiFileInPage |  | PX_SM_Reduced_WikiFileInPage | PageID |  |  |
| PX.SM.Reduced.WikiPage |  | PX_SM_Reduced_WikiPage | PageID |  |  |
| PX.SM.RelationDetail | Relation Detail | PX_SM_RelationDetail, RelationDetail | GroupName |  |  |
| PX.SM.RelationGroup | Relation Group | PX_SM_RelationGroup, RelationGroup | GroupName | Included |  |
| PX.SM.RelationHeader | Relation Header | PX_SM_RelationHeader, RelationHeader | GroupName |  | yes |
| PX.SM.ReportDefinitionInProject | Report | PX_SM_ReportDefinitionInProject | ReportCode |  |  |
| PX.SM.ReportUsers | User | PX_SM_ReportUsers | Username |  | yes |
| PX.SM.RoleActiveDirectory | Role Active Directory | PX_SM_RoleActiveDirectory, RoleActiveDirectory | GroupID, Role | GroupName, GroupDomain, GroupDescription |  |
| PX.SM.RoleClaims | Role Claims | PX_SM_RoleClaims, RoleClaims | GroupID, Role |  |  |
| PX.SM.Roles | Role | PX_SM_Roles, Role, Roles | ApplicationName, Rolename |  |  |
| PX.SM.RolesInCache | Roles In Cache | PX_SM_RolesInCache, RolesInCache | ApplicationName, Cachetype, Rolename, ScreenID |  |  |
| PX.SM.RolesInGraph | Roles In Graph | PX_SM_RolesInGraph, RolesInGraph | ApplicationName, Rolename, ScreenID |  |  |
| PX.SM.RolesInMember | Roles In Member | PX_SM_RolesInMember, RolesInMember | ApplicationName, Cachetype, Membername, Rolename, ScreenID |  |  |
| PX.SM.RowCodeFile |  | PX_SM_RowCodeFile | ObjectID |  | yes |
| PX.SM.RowMobileSiteMap |  | PX_SM_RowMobileSiteMap | ObjectID |  | yes |
| PX.SM.ScreensInUserField |  | PX_SM_ScreensInUserField | AttributeID, ScreenID, TypeValue | NoteText, TypeValueDesc |  |
| PX.SM.SelectedFilter | Filter Header | PX_SM_SelectedFilter | FilterID, ScreenID, ViewName |  |  |
| PX.SM.SelectedImportScenario | Mapping | PX_SM_SelectedImportScenario | Name |  |  |
| PX.SM.SelectedLocale | Locale | PX_SM_SelectedLocale | LocaleName |  |  |
| PX.SM.SimpleWikiPage |  | PX_SM_SimpleWikiPage | PageID |  |  |
| PX.SM.SiteMap | Site Map | PX_SM_SiteMap, SiteMap | NodeID | Graphtype, WorkspaceNames |  |
| PX.SM.SiteMapEx | Site Map | PX_SM_SiteMapEx | NodeID |  |  |
| PX.SM.SiteMapInProject | Site Map | PX_SM_SiteMapInProject | NodeID |  |  |
| PX.SM.SMCalendarSettings | Calendar Settings | PX_SM_SMCalendarSettings, CalendarSettings, SMCalendarSettings | PKID |  |  |
| PX.SM.SMPerformanceInfo | Performance Info | PX_SM_SMPerformanceInfo, PerformanceInfo, SMPerformanceInfo | RecordId | UrlToScreen, IsPinned, ID, NoteText |  |
| PX.SM.SMPerformanceInfoSQL |  | PX_SM_SMPerformanceInfoSQL | ParentId, RecordId |  |  |
| PX.SM.SMPerformanceInfoSQLText | SQL Text Performance Info | PX_SM_SMPerformanceInfoSQLText, SQLTextPerformanceInfo, SMPerformanceInfoSQLText | RecordId |  |  |
| PX.SM.SMPerformanceInfoSQLWithTables | SQL With Tables Performance Info | PX_SM_SMPerformanceInfoSQLWithTables, SQLWithTablesPerformanceInfo, SMPerformanceInfoSQLWithTables | ParentId, RecordId | SQLWithStackTrace, SQLWithParams, ShortParams |  |
| PX.SM.SMPerformanceInfoStackTrace | Stack Trace Performance Info | PX_SM_SMPerformanceInfoStackTrace, StackTracePerformanceInfo, SMPerformanceInfoStackTrace | RecordId |  |  |
| PX.SM.SMPerformanceInfoTraceEvents | Trace Events Performance Info | PX_SM_SMPerformanceInfoTraceEvents, TraceEventsPerformanceInfo, SMPerformanceInfoTraceEvents | ParentId, RecordId |  |  |
| PX.SM.SMPerformanceInfoTraceMessages | Trace Messages Performance Info | PX_SM_SMPerformanceInfoTraceMessages, TraceMessagesPerformanceInfo, SMPerformanceInfoTraceMessages | RecordId |  |  |
| PX.SM.SMPerformanceInfoTraceWithMessages | Trace Events Performance Info | PX_SM_SMPerformanceInfoTraceWithMessages | ParentId, RecordId | MessageWithStackTrace, ShortMessage, HttpMethod, HttpStatusCode |  |
| PX.SM.SMPrinter | Printers | PX_SM_SMPrinter, Printers, SMPrinter | DeviceHubID, PrinterName | NoteText, Included, Secured |  |
| PX.SM.SMPrintJob | Print Job | PX_SM_SMPrintJob, PrintJob, SMPrintJob | JobID | NoteText |  |
| PX.SM.SMPrintJobParameter | Print Job Parameter | PX_SM_SMPrintJobParameter, PrintJobParameter, SMPrintJobParameter | JobID, ParameterName |  |  |
| PX.SM.SMScale | Scale | PX_SM_SMScale, Scale, SMScale | DeviceHubID, ScaleID | CompanyUOM, CompanyLastWeight |  |
| PX.SM.SMScanJob | Scan Job | PX_SM_SMScanJob, ScanJob, SMScanJob | ScanJobID | PaperSourceList, PixelTypeList, ResolutionList, FileTypeList, RequestingUserName |  |
| PX.SM.SMScanJobParameter | Scan Job Parameters | PX_SM_SMScanJobParameter, ScanJobParameters, SMScanJobParameter | LineNbr, ParameterName, ScanJobID |  |  |
| PX.SM.SMScanner | Scanners | PX_SM_SMScanner, Scanners, SMScanner | DeviceHubID, ScannerName |  |  |
| PX.SM.SpaceUsageCalculationHistory | Space Usage Calculation History | PX_SM_SpaceUsageCalculationHistory, SpaceUsageCalculationHistory | PkID | UsedTotal, FreeSpace, CurrentStatus |  |
| PX.SM.SyncTimeTag |  | PX_SM_SyncTimeTag | NoteID |  |  |
| PX.SM.TablesCompanySize | Table Size | PX_SM_TablesCompanySize | Company, TableName |  | yes |
| PX.SM.TableSize | Table Size | PX_SM_TableSize, TableSize | Company, TableName | FullSizeByCompanyMB |  |
| PX.SM.TablesSnapshotSize | Table Size | PX_SM_TablesSnapshotSize | Company, TableName |  | yes |
| PX.SM.TaskTemplate | Task Template | PX_SM_TaskTemplate, TaskTemplate | TaskTemplateID | NameForDescription, NoteText, ShowCreatedByEventsTabExpr |  |
| PX.SM.TaskTemplateSetting | Task Template Setting | PX_SM_TaskTemplateSetting, TaskTemplateSetting | LineNbr, TaskTemplateID | NoteText |  |
| PX.SM.UPErrors | Update Error | PX_SM_UPErrors, UpdateError, UPErrors | ErrorID, UpdateID | Details |  |
| PX.SM.UPHistory | Update History | PX_SM_UPHistory, UpdateHistory, UPHistory | UpdateID |  |  |
| PX.SM.UPHistoryComponents | Update History Components | PX_SM_UPHistoryComponents, UpdateHistoryComponents, UPHistoryComponents | UpdateComponentID |  |  |
| PX.SM.UploadAllowedFileTypes |  | PX_SM_UploadAllowedFileTypes | FileExt |  |  |
| PX.SM.UploadFile |  | PX_SM_UploadFile | FileID | Comment, FileRevisionID, OriginalName, Size, RevisionDate, Extansion, LastExportDate, NoteText |  |
| PX.SM.UploadFileRevision |  | PX_SM_UploadFileRevision | FileID, FileRevisionID |  |  |
| PX.SM.UploadFileRevisionNoData |  | PX_SM_UploadFileRevisionNoData | FileID, FileRevisionID |  | yes |
| PX.SM.UploadFileWithData |  | PX_SM_UploadFileWithData | FileID, FileRevisionID | ContentID |  |
| PX.SM.UploadFileWithIDSelector | File | PX_SM_UploadFileWithIDSelector, File, UploadFileWithIDSelector | FileID |  | yes |
| PX.SM.UploadFileWithNoData |  | PX_SM_UploadFileWithNoData | FileID |  |  |
| PX.SM.UploadFileWithTags |  | PX_SM_UploadFileWithTags | FileID |  | yes |
| PX.SM.UPLock |  | PX_SM_UPLock | DatabaseID |  |  |
| PX.SM.UPPackageTables |  | PX_SM_UPPackageTables | ProjectID, TableName |  |  |
| PX.SM.UPSnapshot | Snapshot | PX_SM_UPSnapshot, Snapshot, UPSnapshot | SnapshotID | Prepared, SizePrepared, Size, NoteText, DeletedDatabaseRecord |  |
| PX.SM.UPSnapshotHistory | Snapshot Restoration History | PX_SM_UPSnapshotHistory, SnapshotRestorationHistory, UPSnapshotHistory | HistoryID | UserID |  |
| PX.SM.UPSnapshotSize | Snapshot Size | PX_SM_UPSnapshotSize, SnapshotSize, UPSnapshotSize | SnapshotID |  | yes |
| PX.SM.UserFilter |  | PX_SM_UserFilter | PKID, Username |  |  |
| PX.SM.UserLocaleFormat |  | PX_SM_UserLocaleFormat | LocaleName, UserID |  |  |
| PX.SM.UserPreferences | User Preferences and Email Settings | PX_SM_UserPreferences, UserPreferencesandEmailSettings, UserPreferences | UserID | NoteText |  |
| PX.SM.UserReportEx |  | PX_SM_UserReportEx | ReportFileName, Version |  |  |
| PX.SM.Users | User | PX_SM_Users, User, Users | Username | Domain, DisplayName, IsADUser, ContactID, GeneratePassword, OldPassword, NewPassword, ConfirmPassword, RecoveryLink, TwoFactorCode, IsLockedOut, State, Included, ActivationID, NoteText, EntityTypeID, chkServiceManagement, IsUserUpdated, IsUserDisable, DeletedDatabaseRecord |  |
| PX.SM.UsersInRoles | Users In Roles | PX_SM_UsersInRoles, UsersInRoles | ApplicationName, Rolename, Username | Inherited, DisplayName, State, Domain, Comment |  |
| PX.SM.Warden |  | PX_SM_Warden | InstallationID, Key, Sub, Type |  |  |
| PX.SM.WikiAccessRights |  | PX_SM_WikiAccessRights | ApplicationName, PageID, RoleName |  |  |
| PX.SM.WikiAccessRoles |  | PX_SM_WikiAccessRoles | ApplicationName, PageID, RoleName |  | yes |
| PX.SM.WikiArticle |  | PX_SM_WikiArticle | PageID |  |  |
| PX.SM.WikiArticleInProject |  | PX_SM_WikiArticleInProject | PageID |  |  |
| PX.SM.WikiCss |  | PX_SM_WikiCss | Name |  |  |
| PX.SM.WikiDescriptor |  | PX_SM_WikiDescriptor | PageID | SitemapParent, SitemapTitle, WikiTitle, WikiDescription |  |
| PX.SM.WikiDescriptorExt |  | PX_SM_WikiDescriptorExt | PageID | RootPageName, HeaderPageName, FooterPageName |  |
| PX.SM.WikiDescriptorMaster |  | PX_SM_WikiDescriptorMaster | PageID |  |  |
| PX.SM.WikiFileInPage |  | PX_SM_WikiFileInPage | FileID, Language, PageID, PageRevisionID | IsLatest |  |
| PX.SM.WikiNotificationTemplate |  | PX_SM_WikiNotificationTemplate | PageID |  |  |
| PX.SM.WikiPage |  | PX_SM_WikiPage | PageID | Title, Summary, Keywords, NoteText, Language, PageRevisionID, PageRevisionDateTime, PageRevisionCreatedByID, PublishedDateTime, Content, ContentHtml, OldStatusID, Hold, AllowApprove, Approved, Rejected, AccessRights, ParentAccessRights, VisibleisHtml |  |
| PX.SM.WikiPageCurrentLanguage |  | PX_SM_WikiPageCurrentLanguage | Language, PageID |  |  |
| PX.SM.WikiPageForReport |  | PX_SM_WikiPageForReport | PageID |  |  |
| PX.SM.WikiPageLanguage |  | PX_SM_WikiPageLanguage | Language, PageID |  |  |
| PX.SM.WikiPageLink |  | PX_SM_WikiPageLink | Language, LinkID, PageID, PageRevisionID |  |  |
| PX.SM.WikiPageMeta |  | PX_SM_WikiPageMeta | Name, PageID |  |  |
| PX.SM.WikiPagePath |  | PX_SM_WikiPagePath | PageID |  | yes |
| PX.SM.WikiPageSimple |  | PX_SM_WikiPageSimple | PageID |  |  |
| PX.SM.WikiPageWithCurrentLanguage |  | PX_SM_WikiPageWithCurrentLanguage | PageID |  |  |
| PX.SM.WikiReadLanguage |  | PX_SM_WikiReadLanguage | LocaleID, WikiID | Language |  |
| PX.SM.WikiRevision |  | PX_SM_WikiRevision | Language, PageID, PageRevisionID | Published, SelectedDest |  |
| PX.SM.WikiRevisionLocalized |  | PX_SM_WikiRevisionLocalized | Language, PageID, PageRevisionID |  |  |
| PX.SM.WikiRevisionTag |  | PX_SM_WikiRevisionTag | Language, PageID, PageRevisionID, TagID, WikiID |  |  |
| PX.SM.WikiRevisionTagGrouped |  | PX_SM_WikiRevisionTagGrouped | Language, PageID, PageRevisionID, TagID, WikiID |  |  |
| PX.SM.WikiSitePage |  | PX_SM_WikiSitePage | PageID |  |  |
| PX.SM.WikiSitePath |  | PX_SM_WikiSitePath | Number | PageName |  |
| PX.SM.WikiTag |  | PX_SM_WikiTag | Description, WikiID |  |  |
| PX.SmsProvider.SM.DAC.SmsPlugin | SMS Provider | PX_SmsProvider_SM_DAC_SmsPlugin, SMSProvider, SmsPlugin | Name | NoteText |  |
| PX.SmsProvider.SM.DAC.SmsPluginParameter | Voice Plug-in Details | PX_SmsProvider_SM_DAC_SmsPluginParameter, VoicePluginDetails, SmsPluginParameter | Name, PluginName |  |  |
| PX.SP.Alias.SPPortal |  | PX_SP_Alias_SPPortal | PortalID | NoteText |  |
| PX.TM.EPCompanyTree | Workgroup | PX_TM_EPCompanyTree, Workgroup, EPCompanyTree | Description |  |  |
| PX.TM.EPCompanyTreeH |  | PX_TM_EPCompanyTreeH | ParentWGID, WorkGroupID |  |  |
| PX.TM.EPCompanyTreeMaster | Workgroup | PX_TM_EPCompanyTreeMaster | Description |  | yes |
| PX.TM.EPCompanyTreeMember |  | PX_TM_EPCompanyTreeMember | ContactID, WorkGroupID |  |  |
| PX.TokenLogin.SAGrantHistory | Access Grant History | PX_TokenLogin_SAGrantHistory, AccessGrantHistory, SAGrantHistory | LogID |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUIArea | Area | PX_Web_UI_Frameset_Model_DAC_MUIArea, Area, MUIArea | AreaID, IsPortal |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen | Favorite Screen | PX_Web_UI_Frameset_Model_DAC_MUIFavoriteScreen, FavoriteScreen, MUIFavoriteScreen | IsPortal, NodeID, Username |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile | Favorite Tile | PX_Web_UI_Frameset_Model_DAC_MUIFavoriteTile, FavoriteTile, MUIFavoriteTile | IsPortal, TileID, Username |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace | Favorite Workspace | PX_Web_UI_Frameset_Model_DAC_MUIFavoriteWorkspace, FavoriteWorkspace, MUIFavoriteWorkspace | IsPortal, Username, WorkspaceID |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen | Pinned Screen | PX_Web_UI_Frameset_Model_DAC_MUIPinnedScreen, PinnedScreen, MUIPinnedScreen | IsPortal, NodeID, Username, WorkspaceID |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUIScreen | Screen | PX_Web_UI_Frameset_Model_DAC_MUIScreen, Screen, MUIScreen | IsPortal, NodeID, WorkspaceID | ScreenID, Url, Title |  |
| PX.Web.UI.Frameset.Model.DAC.MUIScreenOrderHeader |  | PX_Web_UI_Frameset_Model_DAC_MUIScreenOrderHeader | SubcategoryID, WorkspaceID |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUISubcategory | Subcategory | PX_Web_UI_Frameset_Model_DAC_MUISubcategory, Subcategory, MUISubcategory | IsPortal, SubcategoryID |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUITile | Tile | PX_Web_UI_Frameset_Model_DAC_MUITile, Tile, MUITile | IsPortal, TileID |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUITileOrderHeader |  | PX_Web_UI_Frameset_Model_DAC_MUITileOrderHeader | WorkspaceID |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences | User Preferences | PX_Web_UI_Frameset_Model_DAC_MUIUserPreferences, UserPreferences1, MUIUserPreferences | Username |  |  |
| PX.Web.UI.Frameset.Model.DAC.MUIWorkspace | Workspace | PX_Web_UI_Frameset_Model_DAC_MUIWorkspace, Workspace, MUIWorkspace | IsPortal, WorkspaceID |  |  |
| ReconciliationTools.APGLDiscrepancyByDocumentEnqResult | Vendor Details | ReconciliationTools_APGLDiscrepancyByDocumentEnqResult | DocType, RefNbr | NoteText, CuryBegBalance, BegBalance, GLTurnover, XXTurnover, Discrepancy, CuryRate, CuryViewState |  |
| ReconciliationTools.ARGLDiscrepancyByDocumentEnqResult | Customer Details | ReconciliationTools_ARGLDiscrepancyByDocumentEnqResult | DocType, RefNbr | NoteText, SignBalance, GLTurnover, XXTurnover, Discrepancy, CuryRate, CuryViewState |  |
| ReconciliationTools.DiscrepancyByAccountEnqResult | GL Transaction | ReconciliationTools_DiscrepancyByAccountEnqResult | BatchNbr, LineNbr, Module |  | yes |

## Singletons

Setup-style DACs exposed as a single record (`GET .../api/odata/dac/<Name>` returns one object, not a `value` array).

| DAC | Label | Singleton names |
|---|---|---|
| PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder |  | PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspacesOrder |
| PX.BusinessProcess.DAC.BPEventSetting |  | PX_BusinessProcess_DAC_BPEventSetting |
| PX.Data.Archiving.DAC.ArchivalSetup | Archival Setup | PX_Data_Archiving_DAC_ArchivalSetup, ArchivalSetup |
| PX.Data.DeletedRecordsTracking.DAC.ODataPreferences | OData Preferences | PX_Data_DeletedRecordsTracking_DAC_ODataPreferences, ODataPreferences |
| PX.Data.Descriptor.Attributes.SearchIndexEntityRank |  | PX_Data_Descriptor_Attributes_SearchIndexEntityRank |
| PX.Data.GridPreferences |  | PX_Data_GridPreferences |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceChart |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_Mappings_SMLicenseResourceChart |
| PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceSplit |  | PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_Mappings_SMLicenseResourceSplit |
| PX.Data.Update.Company |  | PX_Data_Update_Company |
| PX.ML.CrossSales.DAC.MLCrossSalesSetup | MLCrossSalesSetup | PX_ML_CrossSales_DAC_MLCrossSalesSetup, MLCrossSalesSetup |
| PX.MSGraph.DAC.SM.SMGraphSetup | Teams Preferences | PX_MSGraph_DAC_SM_SMGraphSetup, TeamsPreferences, SMGraphSetup |
| PX.Objects.AM.AMAPSMaintenanceSetup | APS Maintenance Setup | PX_Objects_AM_AMAPSMaintenanceSetup, APSMaintenanceSetup, AMAPSMaintenanceSetup |
| PX.Objects.AM.AMBSetup | BOM Preferences | PX_Objects_AM_AMBSetup, BOMPreferences, AMBSetup |
| PX.Objects.AM.AMConfiguratorSetup | Configurator Preferences | PX_Objects_AM_AMConfiguratorSetup, ConfiguratorPreferences, AMConfiguratorSetup |
| PX.Objects.AM.AMEstimateSetup | Estimate Preferences | PX_Objects_AM_AMEstimateSetup, EstimatePreferences, AMEstimateSetup |
| PX.Objects.AM.AMPSetup | Production Preferences | PX_Objects_AM_AMPSetup, ProductionPreferences, AMPSetup |
| PX.Objects.AM.AMRPSetup | Inventory Planning Preferences | PX_Objects_AM_AMRPSetup, InventoryPlanningPreferences, AMRPSetup |
| PX.Objects.AP.APSetup | Accounts Payable Preferences | PX_Objects_AP_APSetup, AccountsPayablePreferences, APSetup |
| PX.Objects.AR.ARSetup | Account Receivable Preferences | PX_Objects_AR_ARSetup, AccountReceivablePreferences, ARSetup |
| PX.Objects.CA.CASetup | Cash Management Preferences | PX_Objects_CA_CASetup, CashManagementPreferences, CASetup |
| PX.Objects.CM.CMSetup | Currency Management Preferences | PX_Objects_CM_CMSetup, CurrencyManagementPreferences, CMSetup |
| PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup | Compliance Preferences | PX_Objects_CN_Compliance_CL_DAC_LienWaiverSetup, CompliancePreferences, LienWaiverSetup |
| PX.Objects.CN.SCSetup | Subcontract Preferences | PX_Objects_CN_SCSetup, SubcontractPreferences, SCSetup |
| PX.Objects.CR.CRSetup | Customer Management Preferences | PX_Objects_CR_CRSetup, CustomerManagementPreferences, CRSetup |
| PX.Objects.CS.CommonSetup | Common Setup | PX_Objects_CS_CommonSetup, CommonSetup |
| PX.Objects.DR.DRSetup | Deferred Revenue Preferences | PX_Objects_DR_DRSetup, DeferredRevenuePreferences, DRSetup |
| PX.Objects.EP.EPSetup | Time & Expenses Preferences | PX_Objects_EP_EPSetup, TimeExpensesPreferences, EPSetup |
| PX.Objects.FA.FASetup | Fixed Assets Preferences | PX_Objects_FA_FASetup, FixedAssetsPreferences, FASetup |
| PX.Objects.FS.FSRouteSetup | Route Management Preferences | PX_Objects_FS_FSRouteSetup, RouteManagementPreferences, FSRouteSetup |
| PX.Objects.FS.FSSetup | Service Management Preferences | PX_Objects_FS_FSSetup, ServiceManagementPreferences, FSSetup |
| PX.Objects.GL.ADL.Account |  | PX_Objects_GL_ADL_Account |
| PX.Objects.GL.Company | Company | PX_Objects_GL_Company, Company1 |
| PX.Objects.GL.FinYearSetup | Financial Year | PX_Objects_GL_FinYearSetup, FinancialYear, FinYearSetup |
| PX.Objects.GL.GLSetup | General Ledger Preferences | PX_Objects_GL_GLSetup, GeneralLedgerPreferences, GLSetup |
| PX.Objects.IN.GS1UOMSetup | GS1 Unit Setup | PX_Objects_IN_GS1UOMSetup, GS1UnitSetup, GS1UOMSetup |
| PX.Objects.IN.INSetup | IN Setup | PX_Objects_IN_INSetup, INSetup |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration | Daily Field Report Copy Configuration | PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportCopyConfiguration, DailyFieldReportCopyConfiguration |
| PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup | Project Management Preferences - Weather Service Integration Settings | PX_Objects_PJ_DailyFieldReports_PJ_DAC_WeatherIntegrationSetup, ProjectManagementPreferencesWeatherServiceIntegrationSettings, WeatherIntegrationSetup |
| PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup | Drawing Log Preferences | PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogSetup, DrawingLogPreferences, DrawingLogSetup |
| PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup | Photo Log Preferences | PX_Objects_PJ_PhotoLogs_PJ_DAC_PhotoLogSetup, PhotoLogPreferences, PhotoLogSetup |
| PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup | Project Management Preferences | PX_Objects_PJ_ProjectManagement_PJ_DAC_ProjectManagementSetup, ProjectManagementPreferences, ProjectManagementSetup |
| PX.Objects.PM.PMSetup | Project Preferences | PX_Objects_PM_PMSetup, ProjectPreferences, PMSetup |
| PX.Objects.PMRole | Project Role | PX_Objects_PMRole, ProjectRole, PMRole |
| PX.Objects.PO.POSetup | Purchasing Preferences | PX_Objects_PO_POSetup, PurchasingPreferences, POSetup |
| PX.Objects.PR.PRSetup | Payroll Preferences | PX_Objects_PR_PRSetup, PayrollPreferences, PRSetup |
| PX.Objects.PR.Standalone.PRDeductCode | Payroll Deduction and Benefit Code | PX_Objects_PR_Standalone_PRDeductCode, PayrollDeductionandBenefitCode, PRDeductCode1 |
| PX.Objects.PR.Standalone.PRSetup | Payroll Preferences | PX_Objects_PR_Standalone_PRSetup, PayrollPreferences1, PRSetup1 |
| PX.Objects.PR.Standalone.PRTaxCode | Payroll Tax Code | PX_Objects_PR_Standalone_PRTaxCode, PayrollTaxCode, PRTaxCode1 |
| PX.Objects.RQ.RQSetup | Requisition Preferences | PX_Objects_RQ_RQSetup, RequisitionPreferences, RQSetup |
| PX.Objects.SO.SOSetup | Sales Orders Preferences | PX_Objects_SO_SOSetup, SalesOrdersPreferences, SOSetup |
| PX.Objects.SV.FSSetup | SV: Service Management Preferences | PX_Objects_SV_FSSetup, SVServiceManagementPreferences, FSSetup1 |
| PX.Objects.SV.SVSchedulingSetup | Scheduling Preferences | PX_Objects_SV_SVSchedulingSetup, SchedulingPreferences, SVSchedulingSetup |
| PX.Objects.SV.SVSetup | Work Order Preferences | PX_Objects_SV_SVSetup, WorkOrderPreferences, SVSetup |
| PX.Objects.TX.TXImportSettings |  | PX_Objects_TX_TXImportSettings |
| PX.Objects.TX.TXSetup | Tax Preferences | PX_Objects_TX_TXSetup, TaxPreferences, TXSetup |
| PX.PushNotifications.UI.DAC.DispatcherSettings |  | PX_PushNotifications_UI_DAC_DispatcherSettings |
| PX.SM.AUAuditHistoryStatisticsCalculationHistory | Audit History Statistics Calculation History | PX_SM_AUAuditHistoryStatisticsCalculationHistory, AuditHistoryStatisticsCalculationHistory, AUAuditHistoryStatisticsCalculationHistory |
| PX.SM.BlobStorageConfig |  | PX_SM_BlobStorageConfig |
| PX.SM.EulaStatus |  | PX_SM_EulaStatus |
| PX.SM.Licensing |  | PX_SM_Licensing |
| PX.SM.PreferencesEmail |  | PX_SM_PreferencesEmail |
| PX.SM.PreferencesGeneral | General Preferences | PX_SM_PreferencesGeneral, GeneralPreferences, PreferencesGeneral |
| PX.SM.PreferencesSecurity |  | PX_SM_PreferencesSecurity |
| PX.SM.Standalone.EMailAccount |  | PX_SM_Standalone_EMailAccount |
| PX.SM.UPSetup |  | PX_SM_UPSetup |
| PX.SM.Version | Application Version | PX_SM_Version, ApplicationVersion, Version |
| PX.Web.UI.SMPageCache |  | PX_Web_UI_SMPageCache |
