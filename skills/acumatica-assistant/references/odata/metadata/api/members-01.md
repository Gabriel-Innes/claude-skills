<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# PX.AI.Tools.DAC.AIToolDefinition (EntityType)

Label: "AI Tool"
Key: ToolID
Entity sets: PX_AI_Tools_DAC_AIToolDefinition, AITool, AIToolDefinition

PX.AI.Tools.DAC.AIToolDefinition.ToolID : Edm.Guid [key]
PX.AI.Tools.DAC.AIToolDefinition.ToolType : Edm.String "Type"
PX.AI.Tools.DAC.AIToolDefinition.AIGIToolDefinitionCollection -> Collection(PX.AI.Tools.GI.DAC.AIGIToolDefinition)

# PX.AI.Tools.GI.DAC.AIGIToolDefinition (EntityType)

Key: ToolID
Entity sets: PX_AI_Tools_GI_DAC_AIGIToolDefinition

PX.AI.Tools.GI.DAC.AIGIToolDefinition.ToolID : Edm.Guid [key]
PX.AI.Tools.GI.DAC.AIGIToolDefinition.ScreenID : Edm.String "Generic Inquiry"
PX.AI.Tools.GI.DAC.AIGIToolDefinition.FilterID : Edm.Guid "Shared Filter to Apply"
PX.AI.Tools.GI.DAC.AIGIToolDefinition.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.AI.Tools.GI.DAC.AIGIToolDefinition.FilterHeaderByFilterID -> PX.Data.FilterHeader (FilterID=FilterID)
PX.AI.Tools.GI.DAC.AIGIToolDefinition.AIToolDefinitionByToolID -> PX.AI.Tools.DAC.AIToolDefinition (ToolID=ToolID)

# PX.AIStudio.DAC.LLMConnection (EntityType)

Label: "Agent LLM Connection"
Key: ConnectionID
Entity sets: PX_AIStudio_DAC_LLMConnection, AgentLLMConnection, LLMConnection
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.AIStudio.DAC.LLMConnection.ConnectionID : Edm.String [key] "Connection ID"
PX.AIStudio.DAC.LLMConnection.Name : Edm.String "Connection Name"
PX.AIStudio.DAC.LLMConnection.ProviderID : Edm.String "LLM Provider"
PX.AIStudio.DAC.LLMConnection.Status : Edm.String "Status"
PX.AIStudio.DAC.LLMConnection.StatusMessage : Edm.String "Status Message"
PX.AIStudio.DAC.LLMConnection.CreatedByID : Edm.Guid "Created By"
PX.AIStudio.DAC.LLMConnection.CreatedByScreenID : Edm.String
PX.AIStudio.DAC.LLMConnection.CreatedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMConnection.LastModifiedByID : Edm.Guid "Last Modified By"
PX.AIStudio.DAC.LLMConnection.LastModifiedByScreenID : Edm.String
PX.AIStudio.DAC.LLMConnection.LastModifiedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMConnection.tstamp : Edm.Binary
PX.AIStudio.DAC.LLMConnection.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.AIStudio.DAC.LLMConnection.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.AIStudio.DAC.LLMConnection.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.AIStudio.DAC.LLMConnection.LLMProviderByProviderID -> PX.AIStudio.DAC.LLMProvider (ProviderID=ProviderID)
PX.AIStudio.DAC.LLMConnection.LLMConnectionParameterCollection -> Collection(PX.AIStudio.DAC.LLMConnectionParameter)
PX.AIStudio.DAC.LLMConnection.LLMPromptCollection -> Collection(PX.AIStudio.DAC.LLMPrompt)
PX.AIStudio.DAC.LLMConnection.LLMRequestHistoryCollection -> Collection(PX.AIStudio.DAC.LLMRequestHistory)

# PX.AIStudio.DAC.LLMConnectionParameter (EntityType)

Label: "Agent LLM Connection Parameter"
Key: ConnectionID, ParameterID
Entity sets: PX_AIStudio_DAC_LLMConnectionParameter, AgentLLMConnectionParameter, LLMConnectionParameter
Non-filterable, non-selectable: HasError, IsEditable

PX.AIStudio.DAC.LLMConnectionParameter.ConnectionID : Edm.String [key]
PX.AIStudio.DAC.LLMConnectionParameter.ParameterID : Edm.String [key] "Parameter ID"
PX.AIStudio.DAC.LLMConnectionParameter.IsCustom : Edm.Boolean [required] "Custom Parameter"
PX.AIStudio.DAC.LLMConnectionParameter.Name : Edm.String "Parameter"
PX.AIStudio.DAC.LLMConnectionParameter.Type : Edm.String "Type"
PX.AIStudio.DAC.LLMConnectionParameter.IsEncrypted : Edm.Boolean [required] "Encrypted"
PX.AIStudio.DAC.LLMConnectionParameter.IsHeader : Edm.Boolean [required] "Header"
PX.AIStudio.DAC.LLMConnectionParameter.Value : Edm.String "Value"
PX.AIStudio.DAC.LLMConnectionParameter.HasError : Edm.Boolean
PX.AIStudio.DAC.LLMConnectionParameter.IsEditable : Edm.Boolean
PX.AIStudio.DAC.LLMConnectionParameter.CreatedByID : Edm.Guid "Created By"
PX.AIStudio.DAC.LLMConnectionParameter.CreatedByScreenID : Edm.String
PX.AIStudio.DAC.LLMConnectionParameter.CreatedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMConnectionParameter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.AIStudio.DAC.LLMConnectionParameter.LastModifiedByScreenID : Edm.String
PX.AIStudio.DAC.LLMConnectionParameter.LastModifiedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMConnectionParameter.tstamp : Edm.Binary
PX.AIStudio.DAC.LLMConnectionParameter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.AIStudio.DAC.LLMConnectionParameter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.AIStudio.DAC.LLMConnectionParameter.LLMConnectionByConnectionID -> PX.AIStudio.DAC.LLMConnection (ConnectionID=ConnectionID)

# PX.AIStudio.DAC.LLMPrompt (EntityType)

Label: "Agent"
Key: PromptID
Entity sets: PX_AIStudio_DAC_LLMPrompt, Agent, LLMPrompt
Non-filterable, non-selectable: State, NoteText

PX.AIStudio.DAC.LLMPrompt.PromptID : Edm.String [key] "Agent ID"
PX.AIStudio.DAC.LLMPrompt.IsActive : Edm.Boolean [required] "Active"
PX.AIStudio.DAC.LLMPrompt.Name : Edm.String "Agent Name"
PX.AIStudio.DAC.LLMPrompt.Description : Edm.String "Description"
PX.AIStudio.DAC.LLMPrompt.ConnectionID : Edm.String "Agent LLM Connection"
PX.AIStudio.DAC.LLMPrompt.ScreenID : Edm.String "Target Form"
PX.AIStudio.DAC.LLMPrompt.ActionName : Edm.String "Button Name"
PX.AIStudio.DAC.LLMPrompt.PromptInstruction : Edm.String "Agent Instructions"
PX.AIStudio.DAC.LLMPrompt.Type : Edm.String "Type"
PX.AIStudio.DAC.LLMPrompt.State : Edm.String "State"
PX.AIStudio.DAC.LLMPrompt.NoteID : Edm.Guid
PX.AIStudio.DAC.LLMPrompt.NoteText : Edm.String "Note Text"
PX.AIStudio.DAC.LLMPrompt.CreatedByID : Edm.Guid "Created By"
PX.AIStudio.DAC.LLMPrompt.CreatedByScreenID : Edm.String
PX.AIStudio.DAC.LLMPrompt.CreatedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMPrompt.LastModifiedByID : Edm.Guid "Last Modified By"
PX.AIStudio.DAC.LLMPrompt.LastModifiedByScreenID : Edm.String
PX.AIStudio.DAC.LLMPrompt.LastModifiedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMPrompt.tstamp : Edm.Binary
PX.AIStudio.DAC.LLMPrompt.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.AIStudio.DAC.LLMPrompt.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.AIStudio.DAC.LLMPrompt.LLMConnectionByConnectionID -> PX.AIStudio.DAC.LLMConnection (ConnectionID=ConnectionID)
PX.AIStudio.DAC.LLMPrompt.LLMPromptSystemInstructionCollection -> Collection(PX.AIStudio.DAC.LLMPromptSystemInstruction)
PX.AIStudio.DAC.LLMPrompt.LLMPromptToolCollection -> Collection(PX.AIStudio.DAC.LLMPromptTool)
PX.AIStudio.DAC.LLMPrompt.LLMRequestHistoryCollection -> Collection(PX.AIStudio.DAC.LLMRequestHistory)
PX.AIStudio.DAC.LLMPrompt.LLMPromptTestingCollection -> Collection(PX.AIStudio.DAC.LLMPromptTesting)
PX.AIStudio.DAC.LLMPrompt.LLMPromptTestingLogCollection -> Collection(PX.AIStudio.DAC.LLMPromptTestingLog)
PX.AIStudio.DAC.LLMPrompt.LLMPromptToolCBApiCurrentCollection -> Collection(PX.AIStudio.DAC.LLMPromptToolCBApiCurrent)

# PX.AIStudio.DAC.LLMPromptSystemInstruction (EntityType)

Label: "Agent System Instruction Assignment"
Key: PromptID, PromptInstructionID
Entity sets: PX_AIStudio_DAC_LLMPromptSystemInstruction, AgentSystemInstructionAssignment, LLMPromptSystemInstruction

PX.AIStudio.DAC.LLMPromptSystemInstruction.PromptID : Edm.String [key] "Agent ID"
PX.AIStudio.DAC.LLMPromptSystemInstruction.PromptInstructionID : Edm.Guid [key] "Agent Instruction ID"
PX.AIStudio.DAC.LLMPromptSystemInstruction.InstructionID : Edm.String "Instruction Name"
PX.AIStudio.DAC.LLMPromptSystemInstruction.Description : Edm.String "Description"
PX.AIStudio.DAC.LLMPromptSystemInstruction.Instruction : Edm.String "Instruction"
PX.AIStudio.DAC.LLMPromptSystemInstruction.CreatedByID : Edm.Guid "Created By"
PX.AIStudio.DAC.LLMPromptSystemInstruction.CreatedByScreenID : Edm.String
PX.AIStudio.DAC.LLMPromptSystemInstruction.CreatedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMPromptSystemInstruction.LastModifiedByID : Edm.Guid "Last Modified By"
PX.AIStudio.DAC.LLMPromptSystemInstruction.LastModifiedByScreenID : Edm.String
PX.AIStudio.DAC.LLMPromptSystemInstruction.LastModifiedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMPromptSystemInstruction.TStamp : Edm.Binary
PX.AIStudio.DAC.LLMPromptSystemInstruction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.AIStudio.DAC.LLMPromptSystemInstruction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.AIStudio.DAC.LLMPromptSystemInstruction.LLMPromptByPromptID -> PX.AIStudio.DAC.LLMPrompt (PromptID=PromptID)
PX.AIStudio.DAC.LLMPromptSystemInstruction.LLMSystemInstructionByInstructionID -> PX.AIStudio.DAC.LLMSystemInstruction (InstructionID=InstructionID)

# PX.AIStudio.DAC.LLMPromptTesting (EntityType)

Label: "Agent Testing"
Key: PromptID
Entity sets: PX_AIStudio_DAC_LLMPromptTesting, AgentTesting, LLMPromptTesting
Non-filterable, non-selectable: ShowGIMaskingWarning, CacheType, GDPRProtectedFieldsWarning

PX.AIStudio.DAC.LLMPromptTesting.PromptID : Edm.String [key] "Agent ID"
PX.AIStudio.DAC.LLMPromptTesting.LastTestDateTime : Edm.DateTimeOffset "Last Tested On"
PX.AIStudio.DAC.LLMPromptTesting.ExampleID : Edm.Guid "Example Record"
PX.AIStudio.DAC.LLMPromptTesting.FileName : Edm.String "File"
PX.AIStudio.DAC.LLMPromptTesting.ShowGIMaskingWarning : Edm.Boolean "Show Warning About Generic Inquiry Masking"
PX.AIStudio.DAC.LLMPromptTesting.CacheType : Edm.String
PX.AIStudio.DAC.LLMPromptTesting.GDPRProtectedFieldsWarning : Edm.String "GDPR Protected Fields Warning"
PX.AIStudio.DAC.LLMPromptTesting.LLMPromptByPromptID -> PX.AIStudio.DAC.LLMPrompt (PromptID=PromptID)

# PX.AIStudio.DAC.LLMPromptTestingLog (EntityType)

Label: "Agent Testing Log"
Key: EventID, PromptID
Entity sets: PX_AIStudio_DAC_LLMPromptTestingLog, AgentTestingLog, LLMPromptTestingLog

PX.AIStudio.DAC.LLMPromptTestingLog.PromptID : Edm.String [key] "Agent ID"
PX.AIStudio.DAC.LLMPromptTestingLog.EventID : Edm.Int32 [key] "Event ID"
PX.AIStudio.DAC.LLMPromptTestingLog.LogType : Edm.String "Log Type"
PX.AIStudio.DAC.LLMPromptTestingLog.RawJson : Edm.String "Raw JSON"
PX.AIStudio.DAC.LLMPromptTestingLog.LLMPromptByPromptID -> PX.AIStudio.DAC.LLMPrompt (PromptID=PromptID)

# PX.AIStudio.DAC.LLMPromptTool (EntityType)

Label: "Agent Tool"
Key: AIToolDefinitionToolID, PromptID, ToolID
Entity sets: PX_AIStudio_DAC_LLMPromptTool, AgentTool, LLMPromptTool
Non-filterable, non-selectable: NoteText

PX.AIStudio.DAC.LLMPromptTool.PromptID : Edm.String [key] "Agent ID"
PX.AIStudio.DAC.LLMPromptTool.ToolID : Edm.Guid [key] "Tool ID"
PX.AIStudio.DAC.LLMPromptTool.IsActive : Edm.Boolean [required] "Active"
PX.AIStudio.DAC.LLMPromptTool.ToolName : Edm.String "Tool Name"
PX.AIStudio.DAC.LLMPromptTool.ToolDescription : Edm.String "Tool Description"
PX.AIStudio.DAC.LLMPromptTool.SortOrder : Edm.Int32 [required]
PX.AIStudio.DAC.LLMPromptTool.NoteID : Edm.Guid
PX.AIStudio.DAC.LLMPromptTool.NoteText : Edm.String "Note Text"
PX.AIStudio.DAC.LLMPromptTool.CreatedByID : Edm.Guid "Created By"
PX.AIStudio.DAC.LLMPromptTool.CreatedByScreenID : Edm.String
PX.AIStudio.DAC.LLMPromptTool.CreatedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMPromptTool.LastModifiedByID : Edm.Guid "Last Modified By"
PX.AIStudio.DAC.LLMPromptTool.LastModifiedByScreenID : Edm.String
PX.AIStudio.DAC.LLMPromptTool.LastModifiedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMPromptTool.TStamp : Edm.Binary
PX.AIStudio.DAC.LLMPromptTool.AIToolDefinitionToolID : Edm.Guid [key] "Tool ID"
PX.AIStudio.DAC.LLMPromptTool.ToolType : Edm.String "Tool Type"
PX.AIStudio.DAC.LLMPromptTool.MaskedFields : Edm.String "Masked Fields"
PX.AIStudio.DAC.LLMPromptTool.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.AIStudio.DAC.LLMPromptTool.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.AIStudio.DAC.LLMPromptTool.LLMPromptByPromptID -> PX.AIStudio.DAC.LLMPrompt (PromptID=PromptID)
PX.AIStudio.DAC.LLMPromptTool.LLMPromptToolCBApiCurrentCollection -> Collection(PX.AIStudio.DAC.LLMPromptToolCBApiCurrent)

# PX.AIStudio.DAC.LLMPromptToolCBApiCurrent (EntityType)

Label: "Agent Tool CB API Current"
Key: PromptID, ToolID
Entity sets: PX_AIStudio_DAC_LLMPromptToolCBApiCurrent, AgentToolCBAPICurrent, LLMPromptToolCBApiCurrent

PX.AIStudio.DAC.LLMPromptToolCBApiCurrent.PromptID : Edm.String [key] "Agent ID"
PX.AIStudio.DAC.LLMPromptToolCBApiCurrent.ToolID : Edm.Guid [key] "Tool ID"
PX.AIStudio.DAC.LLMPromptToolCBApiCurrent.EndpointName : Edm.String "Endpoint Name"
PX.AIStudio.DAC.LLMPromptToolCBApiCurrent.EndpointVersion : Edm.String "Version"
PX.AIStudio.DAC.LLMPromptToolCBApiCurrent.Entity : Edm.String "Entity"
PX.AIStudio.DAC.LLMPromptToolCBApiCurrent.LLMPromptByPromptID -> PX.AIStudio.DAC.LLMPrompt (PromptID=PromptID)
PX.AIStudio.DAC.LLMPromptToolCBApiCurrent.LLMPromptToolByToolID -> PX.AIStudio.DAC.LLMPromptTool (PromptID=PromptID, ToolID=ToolID)
PX.AIStudio.DAC.LLMPromptToolCBApiCurrent.EntityEndpointByEndpointName -> PX.Api.ContractBased.UI.DAC.EntityEndpoint (EndpointName=InterfaceName)

# PX.AIStudio.DAC.LLMProvider (EntityType)

Label: "LLM Provider"
Key: ProviderID
Entity sets: PX_AIStudio_DAC_LLMProvider, LLMProvider
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.AIStudio.DAC.LLMProvider.ProviderID : Edm.String [key] "LLM Provider ID"
PX.AIStudio.DAC.LLMProvider.IsActive : Edm.Boolean [required] "Active"
PX.AIStudio.DAC.LLMProvider.Name : Edm.String "LLM Provider Name"
PX.AIStudio.DAC.LLMProvider.CreatedByID : Edm.Guid "Created By"
PX.AIStudio.DAC.LLMProvider.CreatedByScreenID : Edm.String
PX.AIStudio.DAC.LLMProvider.CreatedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMProvider.LastModifiedByID : Edm.Guid "Last Modified By"
PX.AIStudio.DAC.LLMProvider.LastModifiedByScreenID : Edm.String
PX.AIStudio.DAC.LLMProvider.LastModifiedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMProvider.tstamp : Edm.Binary
PX.AIStudio.DAC.LLMProvider.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.AIStudio.DAC.LLMProvider.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.AIStudio.DAC.LLMProvider.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.AIStudio.DAC.LLMProvider.LLMConnectionCollection -> Collection(PX.AIStudio.DAC.LLMConnection)
PX.AIStudio.DAC.LLMProvider.LLMProviderParameterCollection -> Collection(PX.AIStudio.DAC.LLMProviderParameter)

# PX.AIStudio.DAC.LLMProviderParameter (EntityType)

Label: "LLM Provider Parameter"
Key: ParameterID, ProviderID
Entity sets: PX_AIStudio_DAC_LLMProviderParameter, LLMProviderParameter

PX.AIStudio.DAC.LLMProviderParameter.ProviderID : Edm.String [key] "LLM Provider"
PX.AIStudio.DAC.LLMProviderParameter.ParameterID : Edm.String [key] "Connection Parameter ID"
PX.AIStudio.DAC.LLMProviderParameter.Name : Edm.String "Parameter"
PX.AIStudio.DAC.LLMProviderParameter.Type : Edm.String "Type"
PX.AIStudio.DAC.LLMProviderParameter.IsEncrypted : Edm.Boolean "Encrypted"
PX.AIStudio.DAC.LLMProviderParameter.IsHeader : Edm.Boolean "Header"
PX.AIStudio.DAC.LLMProviderParameter.CreatedByID : Edm.Guid "Created By"
PX.AIStudio.DAC.LLMProviderParameter.CreatedByScreenID : Edm.String
PX.AIStudio.DAC.LLMProviderParameter.CreatedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMProviderParameter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.AIStudio.DAC.LLMProviderParameter.LastModifiedByScreenID : Edm.String
PX.AIStudio.DAC.LLMProviderParameter.LastModifiedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMProviderParameter.tstamp : Edm.Binary
PX.AIStudio.DAC.LLMProviderParameter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.AIStudio.DAC.LLMProviderParameter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.AIStudio.DAC.LLMProviderParameter.LLMProviderByProviderID -> PX.AIStudio.DAC.LLMProvider (ProviderID=ProviderID)

# PX.AIStudio.DAC.LLMRequestHistory (EntityType)

Label: "AI Automation History Record"
Key: RequestID
Entity sets: PX_AIStudio_DAC_LLMRequestHistory, AIAutomationHistoryRecord, LLMRequestHistory
Non-filterable, non-selectable: Duration

PX.AIStudio.DAC.LLMRequestHistory.RequestID : Edm.Guid [key] "Request ID"
PX.AIStudio.DAC.LLMRequestHistory.RequestGroupID : Edm.Guid "Request Group ID"
PX.AIStudio.DAC.LLMRequestHistory.Attempt : Edm.Int32 "Attempt Number"
PX.AIStudio.DAC.LLMRequestHistory.ProviderName : Edm.String "LLM Provider Name"
PX.AIStudio.DAC.LLMRequestHistory.ConnectionID : Edm.String "Connection ID"
PX.AIStudio.DAC.LLMRequestHistory.ConnectionName : Edm.String "Connection Name"
PX.AIStudio.DAC.LLMRequestHistory.PromptID : Edm.String "Agent ID"
PX.AIStudio.DAC.LLMRequestHistory.Type : Edm.String "Type"
PX.AIStudio.DAC.LLMRequestHistory.ScreenID : Edm.String "Form"
PX.AIStudio.DAC.LLMRequestHistory.User : Edm.String "User"
PX.AIStudio.DAC.LLMRequestHistory.Status : Edm.String "Status"
PX.AIStudio.DAC.LLMRequestHistory.ErrorMessage : Edm.String "Error Message"
PX.AIStudio.DAC.LLMRequestHistory.InputTokens : Edm.Int64 "Input Tokens"
PX.AIStudio.DAC.LLMRequestHistory.OutputTokens : Edm.Int64 "Output Tokens"
PX.AIStudio.DAC.LLMRequestHistory.ProviderInputTokens : Edm.Int64 "Provider's Input Tokens"
PX.AIStudio.DAC.LLMRequestHistory.ProviderOutputTokens : Edm.Int64 "Provider's Output Tokens"
PX.AIStudio.DAC.LLMRequestHistory.ProviderTotalTokens : Edm.Int64 "Provider's Total Tokens"
PX.AIStudio.DAC.LLMRequestHistory.TotalTokens : Edm.Int64 "Total Tokens"
PX.AIStudio.DAC.LLMRequestHistory.RequestTime : Edm.DateTimeOffset "Requested On"
PX.AIStudio.DAC.LLMRequestHistory.ResponseTime : Edm.DateTimeOffset "Received On"
PX.AIStudio.DAC.LLMRequestHistory.Duration : Edm.Int32 "Duration (Sec)"
PX.AIStudio.DAC.LLMRequestHistory.LLMConnectionByConnectionID -> PX.AIStudio.DAC.LLMConnection (ConnectionID=ConnectionID)
PX.AIStudio.DAC.LLMRequestHistory.LLMPromptByPromptID -> PX.AIStudio.DAC.LLMPrompt (PromptID=PromptID)

# PX.AIStudio.DAC.LLMSystemInstruction (EntityType)

Label: "Agent System Instruction"
Key: InstructionID
Entity sets: PX_AIStudio_DAC_LLMSystemInstruction, AgentSystemInstruction, LLMSystemInstruction

PX.AIStudio.DAC.LLMSystemInstruction.InstructionID : Edm.String [key] "Instruction Name"
PX.AIStudio.DAC.LLMSystemInstruction.Description : Edm.String "Description"
PX.AIStudio.DAC.LLMSystemInstruction.IsActive : Edm.Boolean [required] "Active"
PX.AIStudio.DAC.LLMSystemInstruction.IsDefault : Edm.Boolean [required] "Default"
PX.AIStudio.DAC.LLMSystemInstruction.Instruction : Edm.String "Instruction"
PX.AIStudio.DAC.LLMSystemInstruction.CreatedByID : Edm.Guid "Created By"
PX.AIStudio.DAC.LLMSystemInstruction.CreatedByScreenID : Edm.String
PX.AIStudio.DAC.LLMSystemInstruction.CreatedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMSystemInstruction.LastModifiedByID : Edm.Guid "Last Modified By"
PX.AIStudio.DAC.LLMSystemInstruction.LastModifiedByScreenID : Edm.String
PX.AIStudio.DAC.LLMSystemInstruction.LastModifiedDateTime : Edm.DateTimeOffset
PX.AIStudio.DAC.LLMSystemInstruction.tstamp : Edm.Binary
PX.AIStudio.DAC.LLMSystemInstruction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.AIStudio.DAC.LLMSystemInstruction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.AIStudio.DAC.LLMSystemInstruction.LLMPromptSystemInstructionCollection -> Collection(PX.AIStudio.DAC.LLMPromptSystemInstruction)

# PX.Api.ContractBased.UI.DAC.EntityEndpoint (EntityType)

Key: GateVersion, InterfaceName
Entity sets: PX_Api_ContractBased_UI_DAC_EntityEndpoint

PX.Api.ContractBased.UI.DAC.EntityEndpoint.InterfaceName : Edm.String [key required] "Endpoint Name"
PX.Api.ContractBased.UI.DAC.EntityEndpoint.GateVersion : Edm.String [key] "Endpoint Version"
PX.Api.ContractBased.UI.DAC.EntityEndpoint.ExtendsVersion : Edm.String "Base Endpoint Version"
PX.Api.ContractBased.UI.DAC.EntityEndpoint.ExtendsName : Edm.String "Base Endpoint Name"
PX.Api.ContractBased.UI.DAC.EntityEndpoint.SystemContractVersion : Edm.Int32 [required] "System Contract"
PX.Api.ContractBased.UI.DAC.EntityEndpoint.BCBindingCollection -> Collection(PX.Commerce.Core.BCBinding)
PX.Api.ContractBased.UI.DAC.EntityEndpoint.LLMPromptToolCBApiCurrentCollection -> Collection(PX.AIStudio.DAC.LLMPromptToolCBApiCurrent)

# PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModel (EntityType)

Key: ModelID
Entity sets: PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModel

PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModel.ModelID : Edm.Int32 [key]
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModel.ModelName : Edm.String
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModel.ModelCD : Edm.String "Recognition Model"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModel.ImageRecognitionModelMappingCollection -> Collection(PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping)

# PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelField (EntityType)

Key: FieldName, ModelID
Entity sets: PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelField

PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelField.ModelID : Edm.Int32 [key]
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelField.FieldName : Edm.String [key]
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelField.IsVirtual : Edm.Boolean
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelField.FieldType : Edm.String

# PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping (EntityType)

Key: MappedFieldName, MappingID
Entity sets: PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelFieldMapping

PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping.MappingID : Edm.Guid [key]
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping.FieldName : Edm.String "Target Field Name"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping.ViewName : Edm.String "Target View Name"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping.MappedFieldName : Edm.String [key] "Source Field Name"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping.Active : Edm.Boolean [required]
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping.ImageRecognitionModelMappingByMappingID -> PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping (MappingID=MappingID)

# PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping (EntityType)

Key: MappingID
Entity sets: PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelMapping

PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.MappingID : Edm.Guid [key] "Mapping"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.ModelID : Edm.Int32 "Recognition Model"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.ActionName : Edm.String "Action Name"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.ScreenID : Edm.String "Target Screen ID"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.Active : Edm.Boolean [required] "Active"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.ForceEnabled : Edm.Boolean [required] "Enabled if feature is turned off"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.MappingCD : Edm.String "Mapping"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.ImageRecognitionModelByModelID -> PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModel (ModelID=ModelID)
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.ImageRecognitionModelFieldMappingCollection -> Collection(PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelFieldMapping)
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping.ImageRecognitionModelScreenMappingCollection -> Collection(PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping)

# PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping (EntityType)

Key: MappingID, ScreenID, ViewName
Entity sets: PX_Api_Mobile_ImageRecognition_DAC_ImageRecognitionModelScreenMapping

PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping.MappingID : Edm.Guid [key]
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping.ViewName : Edm.String [key] "View Name"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping.Action : Edm.String
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping.Active : Edm.Boolean [required]
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping.ScreenID : Edm.String [key] "Target Screen ID"
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelScreenMapping.ImageRecognitionModelMappingByMappingID -> PX.Api.Mobile.ImageRecognition.DAC.ImageRecognitionModelMapping (MappingID=MappingID)

# PX.Api.Mobile.MultiFactorAuth.DAC.MobileOtpSecret (EntityType)

Key: AccountID, ApplicationInstanceID
Entity sets: PX_Api_Mobile_MultiFactorAuth_DAC_MobileOtpSecret

PX.Api.Mobile.MultiFactorAuth.DAC.MobileOtpSecret.ApplicationInstanceID : Edm.String [key] "Mobile Application ID"
PX.Api.Mobile.MultiFactorAuth.DAC.MobileOtpSecret.AccountID : Edm.Guid [key]
PX.Api.Mobile.MultiFactorAuth.DAC.MobileOtpSecret.OtpSecret : Edm.Binary "OTP Secret"

# PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode (EntityType)

Key: Code, UserId
Entity sets: PX_Api_Mobile_MultiFactorAuth_DAC_MultiFactorPersistentCode

PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode.UserId : Edm.Guid [key] "User ID"
PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode.Code : Edm.String [key] "Access Code"
PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode.ValidTo : Edm.DateTimeOffset "Valid To"

# PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCodeWithCompany (EntityType)

BaseType: PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode
Key: Code, UserId (inherited from PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCode)
Entity sets: PX_Api_Mobile_MultiFactorAuth_DAC_MultiFactorPersistentCodeWithCompany

PX.Api.Mobile.MultiFactorAuth.DAC.MultiFactorPersistentCodeWithCompany.CompanyID : Edm.Int32 "CompanyId"

# PX.Api.Mobile.PushNotifications.DAC.MobileDevice (EntityType)

Key: AccountID, ApplicationInstanceID
Entity sets: PX_Api_Mobile_PushNotifications_DAC_MobileDevice

PX.Api.Mobile.PushNotifications.DAC.MobileDevice.ApplicationInstanceID : Edm.String [key] "Mobile Application ID"
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.AccountID : Edm.Guid [key]
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.Service : Edm.String
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.RegistrationToken : Edm.String
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.DeviceName : Edm.String "Device Name"
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.DeviceModel : Edm.String "Device Model"
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.DeviceOS : Edm.String "OS Version"
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.ExpiredToken : Edm.Boolean "Token Expired"
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.IsConfirmation : Edm.Boolean "Send Confirmation Push"
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.UserID : Edm.Guid
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.AccountApplicationInstanceID : Edm.String "Mobile Application ID"
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.AccountAccountID : Edm.Guid
PX.Api.Mobile.PushNotifications.DAC.MobileDevice.Enabled : Edm.Boolean "Turn on Notifications"

# PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems (EntityType)

Key: NoteID, Owner
Entity sets: PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceItems
Non-filterable, non-selectable: DisplayName, NoteText

PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.WorkspaceOwner : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.WorkspaceName : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.ItemID : Edm.String "Item Name"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.ItemType : Edm.String "Item Type"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.DisplayName : Edm.String "Display Name"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.IsActive : Edm.Boolean [required] "Visible"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.SortOrder : Edm.Int32 [required] "SortOrder"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.Owner : Edm.String [key required]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.NoteID : Edm.Guid [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.NoteText : Edm.String "Note Text"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.CreatedByID : Edm.Guid "Created By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.CreatedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.CreatedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.LastModifiedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItems.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder (EntityType)

Key: ItemID, ItemOwner, ItemType, Owner
Entity sets: PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceItemsOrder
Non-filterable, non-selectable: NoteText

PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.WorkspaceOwner : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.WorkspaceName : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.ItemID : Edm.String [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.ItemType : Edm.String [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.IsActive : Edm.Boolean
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.ItemOwner : Edm.String [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.Owner : Edm.String [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.SortOrder : Edm.Int32 [required] "SortOrder"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.NoteID : Edm.Guid
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.NoteText : Edm.String "Note Text"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.CreatedByID : Edm.Guid "Created By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.CreatedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.CreatedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.LastModifiedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceItemsOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder (EntityType)

Singletons: PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspacesOrder

PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.WorkspaceOwner : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.WorkspaceName : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.Owner : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.SortOrder : Edm.Int32 [required] "SortOrder"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.IsActive : Edm.Boolean
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.NoteID : Edm.Guid
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.NoteText : Edm.String "Note Text"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.CreatedByID : Edm.Guid "Created By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.CreatedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.CreatedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.LastModifiedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspacesOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder (EntityType)

Key: DashboardID, Owner, WidgetID, WidgetOwner
Entity sets: PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsOrder
Non-filterable, non-selectable: NoteText

PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.WorkspaceOwner : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.WorkspaceName : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.DashboardID : Edm.Int32 [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.WidgetID : Edm.Int32 [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.IsActive : Edm.Boolean
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.WidgetOwner : Edm.String [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.Owner : Edm.String [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.SortOrder : Edm.Int32 [required] "SortOrder"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.NoteID : Edm.Guid
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.NoteText : Edm.String "Note Text"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.CreatedByID : Edm.Guid "Created By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.CreatedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.CreatedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.LastModifiedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2 (EntityType)

Key: NoteID, Owner
Entity sets: PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsV2
Non-filterable, non-selectable: NoteText

PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.WorkspaceOwner : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.WorkspaceName : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.DashboardID : Edm.Guid "Dashboard"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.WidgetID : Edm.Guid "Widget"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.IsActive : Edm.Boolean [required] "Visible"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.SortOrder : Edm.Int32 [required] "SortOrder"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.Owner : Edm.String [key required]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.NoteID : Edm.Guid [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.NoteText : Edm.String "Note Text"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.CreatedByID : Edm.Guid "Created By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.CreatedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.CreatedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.LastModifiedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order (EntityType)

Key: DashboardID, Owner, WidgetID, WidgetOwner
Entity sets: PX_Api_Mobile_Workspaces_DAC_MobileSiteMapWorkspaceWidgetsV2Order
Non-filterable, non-selectable: NoteText

PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.WorkspaceOwner : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.WorkspaceName : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.DashboardID : Edm.Guid [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.WidgetID : Edm.Guid [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.IsActive : Edm.Boolean
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.WidgetOwner : Edm.String [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.Owner : Edm.String [key]
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.SortOrder : Edm.Int32 [required] "SortOrder"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.NoteID : Edm.Guid
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.NoteText : Edm.String "Note Text"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.CreatedByID : Edm.Guid "Created By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.CreatedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.CreatedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.LastModifiedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.Mobile.Workspaces.DAC.MobileSiteMapWorkspaceWidgetsV2Order.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces (EntityType)

Key: Name
Entity sets: PX_Api_Mobile_Workspaces_MobileSiteMapWorkspaces
Non-filterable, non-selectable: NoteText

PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.MobileWorkspaceID : Edm.Guid "MobileWorkspaceID"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.Owner : Edm.String
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.Name : Edm.String [key] "Workspace ID"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.DisplayName : Edm.String "Display Name"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.SortOrder : Edm.Int32 [required] "SortOrder"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.IsActive : Edm.Boolean [required] "Visible"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.Icon : Edm.String "Icon"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.NoteID : Edm.Guid
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.NoteText : Edm.String "Note Text"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.CreatedByID : Edm.Guid "Created By"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.CreatedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.CreatedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.LastModifiedByScreenID : Edm.String
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.Mobile.Workspaces.MobileSiteMapWorkspaces.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Api.ModelContextProtocol.UI.DAC.McpServer (EntityType)

Label: "MCP Server"
Key: Name
Entity sets: PX_Api_ModelContextProtocol_UI_DAC_McpServer, MCPServer
Non-filterable, non-selectable: Url

PX.Api.ModelContextProtocol.UI.DAC.McpServer.McpServerID : Edm.Guid
PX.Api.ModelContextProtocol.UI.DAC.McpServer.Name : Edm.String [key] "Server Name"
PX.Api.ModelContextProtocol.UI.DAC.McpServer.Title : Edm.String "Server Title"
PX.Api.ModelContextProtocol.UI.DAC.McpServer.Url : Edm.String "URL"
PX.Api.ModelContextProtocol.UI.DAC.McpServer.Instructions : Edm.String "Instructions"
PX.Api.ModelContextProtocol.UI.DAC.McpServer.Active : Edm.Boolean [required] "Active"
PX.Api.ModelContextProtocol.UI.DAC.McpServer.ToolCounter : Edm.Int32 [required]

# PX.Api.ModelContextProtocol.UI.DAC.McpServerTool (EntityType)

Label: "MCP Tool"
Key: McpServerID, ToolID
Entity sets: PX_Api_ModelContextProtocol_UI_DAC_McpServerTool, MCPTool, McpServerTool

PX.Api.ModelContextProtocol.UI.DAC.McpServerTool.McpServerID : Edm.Guid [key] "MCP Server"
PX.Api.ModelContextProtocol.UI.DAC.McpServerTool.ToolID : Edm.Guid [key] "Tool Type"
PX.Api.ModelContextProtocol.UI.DAC.McpServerTool.Active : Edm.Boolean [required] "Active"
PX.Api.ModelContextProtocol.UI.DAC.McpServerTool.Name : Edm.String "Tool Name"
PX.Api.ModelContextProtocol.UI.DAC.McpServerTool.Title : Edm.String "Tool Title"
PX.Api.ModelContextProtocol.UI.DAC.McpServerTool.Order : Edm.Int32

# PX.Api.ModelContextProtocol.UI.DAC.McpServerToolProjection (EntityType)

Label: "MCP Tool"
BaseType: PX.Api.ModelContextProtocol.UI.DAC.McpServerTool
Key: McpServerID, ToolID (inherited from PX.Api.ModelContextProtocol.UI.DAC.McpServerTool)
Entity sets: PX_Api_ModelContextProtocol_UI_DAC_McpServerToolProjection

PX.Api.ModelContextProtocol.UI.DAC.McpServerToolProjection.AIToolDefinitionToolID : Edm.Guid "Tool ID"
PX.Api.ModelContextProtocol.UI.DAC.McpServerToolProjection.ToolType : Edm.String "Tool Type"

# PX.Api.OData.DAC.DeletedRecordResult (ComplexType)


PX.Api.OData.DAC.DeletedRecordResult.RefNoteID : Edm.Guid
PX.Api.OData.DAC.DeletedRecordResult.DeleteDate : Edm.DateTimeOffset

# PX.Api.SYData (EntityType)

Key: LineNbr, MappingID
Entity sets: PX_Api_SYData
Non-filterable, non-selectable: ExtRefNbr, CanAddSubstitutions, NoteText

PX.Api.SYData.MappingID : Edm.Guid [key]
PX.Api.SYData.LineNbr : Edm.Int32 [key] "Number"
PX.Api.SYData.IsActive : Edm.Boolean [required] "Active"
PX.Api.SYData.IsProcessed : Edm.Boolean [required] "Processed"
PX.Api.SYData.ErrorMessage : Edm.String "Error"
PX.Api.SYData.FieldErrors : Edm.String
PX.Api.SYData.FieldExceptions : Edm.String
PX.Api.SYData.FieldValues : Edm.String
PX.Api.SYData.Keys : Edm.String
PX.Api.SYData.ExtRefNbr : Edm.String
PX.Api.SYData.CanAddSubstitutions : Edm.Boolean
PX.Api.SYData.NoteID : Edm.Guid
PX.Api.SYData.NoteText : Edm.String "Note Text"
PX.Api.SYData.CreatedByID : Edm.Guid "Created By"
PX.Api.SYData.CreatedByScreenID : Edm.String
PX.Api.SYData.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.SYData.LastModifiedByScreenID : Edm.String
PX.Api.SYData.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.SYData.TStamp : Edm.Binary
PX.Api.SYData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.SYData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.SYData.SYMappingByMappingID -> PX.Api.SYMapping (MappingID=MappingID)

# PX.Api.SYHistory (EntityType)

Key: MappingID, StatusDate
Entity sets: PX_Api_SYHistory
Non-filterable, non-selectable: StatusDateToDisplay

PX.Api.SYHistory.MappingID : Edm.Guid [key]
PX.Api.SYHistory.StatusDate : Edm.DateTimeOffset [key] "Status Date"
PX.Api.SYHistory.Status : Edm.String "Status"
PX.Api.SYHistory.NbrRecords : Edm.Int32 "Number of Records"
PX.Api.SYHistory.ImportTimeStamp : Edm.String "Version"
PX.Api.SYHistory.ExportTimeStamp : Edm.DateTimeOffset "Version"
PX.Api.SYHistory.ExportTimeStampUtc : Edm.DateTimeOffset "UTC Time Stamp"
PX.Api.SYHistory.Description : Edm.String "Description"
PX.Api.SYHistory.CreatedByID : Edm.Guid "Created By"
PX.Api.SYHistory.CreatedByScreenID : Edm.String
PX.Api.SYHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYHistory.StatusDateToDisplay : Edm.DateTimeOffset "Status Date"
PX.Api.SYHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Api.SYImportCondition (EntityType)

Key: LineNbr, MappingID
Entity sets: PX_Api_SYImportCondition
Non-filterable, non-selectable: NoteText

PX.Api.SYImportCondition.MappingID : Edm.Guid [key]
PX.Api.SYImportCondition.LineNbr : Edm.Int16 [key]
PX.Api.SYImportCondition.IsActive : Edm.Boolean [required] "Active"
PX.Api.SYImportCondition.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.Api.SYImportCondition.FieldName : Edm.String "Field Name"
PX.Api.SYImportCondition.Condition : Edm.Int32 [required] "Condition"
PX.Api.SYImportCondition.Value : Edm.String "Value"
PX.Api.SYImportCondition.Value2 : Edm.String "Value 2"
PX.Api.SYImportCondition.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.Api.SYImportCondition.Operator : Edm.Int32 [required] "Operator"
PX.Api.SYImportCondition.NoteID : Edm.Guid
PX.Api.SYImportCondition.NoteText : Edm.String "Note Text"
PX.Api.SYImportCondition.CreatedByID : Edm.Guid "Created By"
PX.Api.SYImportCondition.CreatedByScreenID : Edm.String
PX.Api.SYImportCondition.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYImportCondition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.SYImportCondition.LastModifiedByScreenID : Edm.String
PX.Api.SYImportCondition.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.SYImportCondition.TStamp : Edm.Binary
PX.Api.SYImportCondition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.SYImportCondition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.SYImportCondition.SYMappingByMappingID -> PX.Api.SYMapping (MappingID=MappingID)

# PX.Api.SYMapping (EntityType)

Label: "Mapping"
Key: Name
Entity sets: PX_Api_SYMapping, Mapping, SYMapping
Non-filterable, non-selectable: SitemapTitle, SitemapScreenId, NoteText, ShowCreatedByEventsTabExpr, WorkspaceID, SubcategoryID

PX.Api.SYMapping.IsSimpleMapping : Edm.Boolean "Simple Scenario"
PX.Api.SYMapping.MappingID : Edm.Guid "Mapping ID"
PX.Api.SYMapping.IsActive : Edm.Boolean [required] "Active"
PX.Api.SYMapping.Name : Edm.String [key] "Name"
PX.Api.SYMapping.SitemapTitle : Edm.String "Site Map Title"
PX.Api.SYMapping.SitemapScreenId : Edm.String "Site Map ScreenID"
PX.Api.SYMapping.InverseMappingID : Edm.Guid "Inverse Mapping ID"
PX.Api.SYMapping.ScreenID : Edm.String "Screen Name"
PX.Api.SYMapping.MappingType : Edm.String
PX.Api.SYMapping.RepeatingData : Edm.Byte [required] "Detail Export Mode"
PX.Api.SYMapping.GraphName : Edm.String
PX.Api.SYMapping.ViewName : Edm.String
PX.Api.SYMapping.GridViewName : Edm.String
PX.Api.SYMapping.ProviderID : Edm.Guid "Provider"
PX.Api.SYMapping.ProviderObject : Edm.String "Provider Object"
PX.Api.SYMapping.SyncType : Edm.String "Sync Type"
PX.Api.SYMapping.Status : Edm.String "Status"
PX.Api.SYMapping.FieldCntr : Edm.Int16 [required]
PX.Api.SYMapping.FieldOrderCntr : Edm.Int16 [required]
PX.Api.SYMapping.DataCntr : Edm.Int32 [required]
PX.Api.SYMapping.ImportConditionCntr : Edm.Int16 [required]
PX.Api.SYMapping.ConditionCntr : Edm.Int16 [required]
PX.Api.SYMapping.NbrRecords : Edm.Int32 [required] "Number of Records"
PX.Api.SYMapping.PreparedOn : Edm.DateTimeOffset "Prepared On"
PX.Api.SYMapping.CompletedOn : Edm.DateTimeOffset "Completed On"
PX.Api.SYMapping.ImportTimeStamp : Edm.String
PX.Api.SYMapping.ExportTimeStamp : Edm.DateTimeOffset
PX.Api.SYMapping.ExportTimeStampUtc : Edm.DateTimeOffset
PX.Api.SYMapping.NoteID : Edm.Guid
PX.Api.SYMapping.NoteText : Edm.String "Note Text"
PX.Api.SYMapping.FormatLocale : Edm.String "Format Locale"
PX.Api.SYMapping.IsExportOnlyMappingFields : Edm.Boolean [required] "Export Only Mapped Fields"
PX.Api.SYMapping.CreatedByID : Edm.Guid "Created By"
PX.Api.SYMapping.CreatedByScreenID : Edm.String
PX.Api.SYMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.SYMapping.LastModifiedByScreenID : Edm.String
PX.Api.SYMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.SYMapping.TStamp : Edm.Binary
PX.Api.SYMapping.ProcessInParallel : Edm.Boolean [required] "Parallel Processing"
PX.Api.SYMapping.BreakOnError : Edm.Boolean [required] "Break on Error"
PX.Api.SYMapping.BreakOnTarget : Edm.Boolean [required] "Break on Incorrect Target"
PX.Api.SYMapping.SkipHeaders : Edm.Boolean [required] "Skip Headers"
PX.Api.SYMapping.SitemapID : Edm.Guid
PX.Api.SYMapping.DiscardResult : Edm.Boolean [required] "Discard Previous Result"
PX.Api.SYMapping.ShowCreatedByEventsTabExpr : Edm.Boolean "ShowCreatedByEventsTabExpr"
PX.Api.SYMapping.WorkspaceID : Edm.Guid "Workspace"
PX.Api.SYMapping.SubcategoryID : Edm.Guid "Category"
PX.Api.SYMapping.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Api.SYMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.SYMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.SYMapping.SYMappingByMappingID -> PX.Api.SYMapping (MappingID=InverseMappingID)
PX.Api.SYMapping.SYProviderByProviderID -> PX.Api.SYProvider (ProviderID=ProviderID)
PX.Api.SYMapping.SYProviderObjectByProviderID -> PX.Api.SYProviderObject (ProviderObject=Name, ProviderID=ProviderID)
PX.Api.SYMapping.LocaleByFormatLocale -> PX.SM.Locale (FormatLocale=LocaleName)
PX.Api.SYMapping.SYMappingCollection -> Collection(PX.Api.SYMapping)
PX.Api.SYMapping.SYMappingFieldCollection -> Collection(PX.Api.SYMappingField)
PX.Api.SYMapping.PaymentMethodCollection -> Collection(PX.Objects.CA.PaymentMethod)
PX.Api.SYMapping.SYDataCollection -> Collection(PX.Api.SYData)
PX.Api.SYMapping.SYImportConditionCollection -> Collection(PX.Api.SYImportCondition)
PX.Api.SYMapping.SYMappingConditionCollection -> Collection(PX.Api.SYMappingCondition)
PX.Api.SYMapping.HSEntitySetupCollection -> Collection(PX.DataSync.HubSpot.HSEntitySetup)
PX.Api.SYMapping.BPEventSubscriberCollection -> Collection(PX.BusinessProcess.DAC.BPEventSubscriber)
PX.Api.SYMapping.SFEntitySetupCollection -> Collection(PX.Salesforce.SFEntitySetup)

# PX.Api.SYMappingActive (EntityType)

Label: "Mapping"
BaseType: PX.Api.SYMapping
Key: Name (inherited from PX.Api.SYMapping)
Entity sets: PX_Api_SYMappingActive
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Api.SYMappingActive.ScreenDescription : Edm.String "Screen Name"
PX.Api.SYMappingActive.BatchSize : Edm.Int32 "Batch Size"

# PX.Api.SYMappingActiveFilter (EntityType)

Label: "Mapping"
BaseType: PX.Api.SYMappingActive
Key: Name (inherited from PX.Api.SYMapping)
Entity sets: PX_Api_SYMappingActiveFilter

# PX.Api.SYMappingCondition (EntityType)

Key: LineNbr, MappingID
Entity sets: PX_Api_SYMappingCondition
Non-filterable, non-selectable: ObjectNameHidden, FieldNameHidden, NoteText

PX.Api.SYMappingCondition.MappingID : Edm.Guid [key]
PX.Api.SYMappingCondition.LineNbr : Edm.Int16 [key]
PX.Api.SYMappingCondition.IsActive : Edm.Boolean [required] "Active"
PX.Api.SYMappingCondition.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.Api.SYMappingCondition.ObjectName : Edm.String "Target Object"
PX.Api.SYMappingCondition.ObjectNameHidden : Edm.String "Native Object Name"
PX.Api.SYMappingCondition.FieldName : Edm.String "Field Name"
PX.Api.SYMappingCondition.FieldNameHidden : Edm.String "Native Field Name"
PX.Api.SYMappingCondition.Condition : Edm.Int32 [required] "Condition"
PX.Api.SYMappingCondition.Value : Edm.String "Value"
PX.Api.SYMappingCondition.Value2 : Edm.String "Value 2"
PX.Api.SYMappingCondition.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.Api.SYMappingCondition.Operator : Edm.Int32 [required] "Operator"
PX.Api.SYMappingCondition.NoteID : Edm.Guid
PX.Api.SYMappingCondition.NoteText : Edm.String "Note Text"
PX.Api.SYMappingCondition.CreatedByID : Edm.Guid "Created By"
PX.Api.SYMappingCondition.CreatedByScreenID : Edm.String
PX.Api.SYMappingCondition.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYMappingCondition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.SYMappingCondition.LastModifiedByScreenID : Edm.String
PX.Api.SYMappingCondition.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.SYMappingCondition.TStamp : Edm.Binary
PX.Api.SYMappingCondition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.SYMappingCondition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.SYMappingCondition.SYMappingByMappingID -> PX.Api.SYMapping (MappingID=MappingID)

# PX.Api.SYMappingField (EntityType)

Key: LineNbr, MappingID
Entity sets: PX_Api_SYMappingField
Non-filterable, non-selectable: ObjectNameHidden, FieldNameHidden, FullFieldNameHidden, NoteText

PX.Api.SYMappingField.MappingID : Edm.Guid [key]
PX.Api.SYMappingField.LineNbr : Edm.Int16 [key]
PX.Api.SYMappingField.IsActive : Edm.Boolean [required] "Active"
PX.Api.SYMappingField.IsVisible : Edm.Boolean [required] "Is Visible"
PX.Api.SYMappingField.ParentLineNbr : Edm.Int16
PX.Api.SYMappingField.OrderNumber : Edm.Int32
PX.Api.SYMappingField.ObjectName : Edm.String "Target Object"
PX.Api.SYMappingField.ObjectNameHidden : Edm.String "Native Object Name"
PX.Api.SYMappingField.FieldName : Edm.String "Field or Action"
PX.Api.SYMappingField.FieldNameHidden : Edm.String "Internal Name"
PX.Api.SYMappingField.FullFieldNameHidden : Edm.String "Internal Name"
PX.Api.SYMappingField.Value : Edm.String "Source Field or Value"
PX.Api.SYMappingField.NeedCommit : Edm.Boolean [required] "Commit"
PX.Api.SYMappingField.NeedSearch : Edm.Boolean "Search"
PX.Api.SYMappingField.IgnoreError : Edm.Boolean [required] "Ignore Error"
PX.Api.SYMappingField.ExecuteActionBehavior : Edm.String "Execute Action"
PX.Api.SYMappingField.NoteID : Edm.Guid
PX.Api.SYMappingField.NoteText : Edm.String "Note Text"
PX.Api.SYMappingField.CreatedByID : Edm.Guid "Created By"
PX.Api.SYMappingField.CreatedByScreenID : Edm.String
PX.Api.SYMappingField.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYMappingField.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.SYMappingField.LastModifiedByScreenID : Edm.String
PX.Api.SYMappingField.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.SYMappingField.TStamp : Edm.Binary
PX.Api.SYMappingField.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.SYMappingField.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.SYMappingField.SYMappingByMappingID -> PX.Api.SYMapping (MappingID=MappingID)

# PX.Api.SYMappingFieldSimple (EntityType)

BaseType: PX.Api.SYMappingField
Key: LineNbr, MappingID (inherited from PX.Api.SYMappingField)
Entity sets: PX_Api_SYMappingFieldSimple
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Api.SYMappingFieldSimple.IsKey : Edm.Boolean "Key"

# PX.Api.SYProvider (EntityType)

Label: "Provider"
Key: Name
Entity sets: PX_Api_SYProvider, Provider, SYProvider
Non-filterable, non-selectable: NoteText

PX.Api.SYProvider.ProviderID : Edm.Guid
PX.Api.SYProvider.Name : Edm.String [key] "Name"
PX.Api.SYProvider.IsActive : Edm.Boolean [required] "Active"
PX.Api.SYProvider.ProviderType : Edm.String "Provider Type"
PX.Api.SYProvider.ObjectCntr : Edm.Int16 [required]
PX.Api.SYProvider.ParameterCntr : Edm.Int16 [required]
PX.Api.SYProvider.NoteID : Edm.Guid
PX.Api.SYProvider.NoteText : Edm.String "Note Text"
PX.Api.SYProvider.CreatedByID : Edm.Guid "Created By"
PX.Api.SYProvider.CreatedByScreenID : Edm.String
PX.Api.SYProvider.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYProvider.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.SYProvider.LastModifiedByScreenID : Edm.String
PX.Api.SYProvider.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.SYProvider.TStamp : Edm.Binary
PX.Api.SYProvider.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.SYProvider.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.SYProvider.SYMappingCollection -> Collection(PX.Api.SYMapping)
PX.Api.SYProvider.SYProviderObjectCollection -> Collection(PX.Api.SYProviderObject)
PX.Api.SYProvider.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)

# PX.Api.SYProviderField (EntityType)

Key: Name, ObjectName, ProviderID
Entity sets: PX_Api_SYProviderField
Non-filterable, non-selectable: NoteText

PX.Api.SYProviderField.ProviderID : Edm.Guid [key]
PX.Api.SYProviderField.ObjectName : Edm.String [key]
PX.Api.SYProviderField.LineNbr : Edm.Int16
PX.Api.SYProviderField.IsActive : Edm.Boolean [required] "Active"
PX.Api.SYProviderField.Name : Edm.String [key] "Field"
PX.Api.SYProviderField.DisplayName : Edm.String "Description"
PX.Api.SYProviderField.Command : Edm.String "Command"
PX.Api.SYProviderField.IsKey : Edm.Boolean [required] "Key"
PX.Api.SYProviderField.DataType : Edm.String "Data Type"
PX.Api.SYProviderField.DataLength : Edm.Int32 "Data Length"
PX.Api.SYProviderField.IsCustom : Edm.Boolean [required]
PX.Api.SYProviderField.NoteID : Edm.Guid
PX.Api.SYProviderField.NoteText : Edm.String "Note Text"
PX.Api.SYProviderField.CreatedByID : Edm.Guid "Created By"
PX.Api.SYProviderField.CreatedByScreenID : Edm.String
PX.Api.SYProviderField.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYProviderField.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.SYProviderField.LastModifiedByScreenID : Edm.String
PX.Api.SYProviderField.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.SYProviderField.TStamp : Edm.Binary
PX.Api.SYProviderField.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.SYProviderField.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.SYProviderField.SYProviderObjectByObjectName -> PX.Api.SYProviderObject (ProviderID=ProviderID, ObjectName=Name)

# PX.Api.SYProviderObject (EntityType)

Label: "Provider Object"
Key: LineNbr, ProviderID
Entity sets: PX_Api_SYProviderObject, ProviderObject, SYProviderObject
Non-filterable, non-selectable: NoteText

PX.Api.SYProviderObject.ProviderID : Edm.Guid [key]
PX.Api.SYProviderObject.LineNbr : Edm.Int16 [key]
PX.Api.SYProviderObject.IsActive : Edm.Boolean [required] "Active"
PX.Api.SYProviderObject.Name : Edm.String "Object"
PX.Api.SYProviderObject.DisplayName : Edm.String "Description"
PX.Api.SYProviderObject.Command : Edm.String "Command"
PX.Api.SYProviderObject.FieldCntr : Edm.Int16 [required]
PX.Api.SYProviderObject.IsCustom : Edm.Boolean [required]
PX.Api.SYProviderObject.NoteID : Edm.Guid
PX.Api.SYProviderObject.NoteText : Edm.String "Note Text"
PX.Api.SYProviderObject.CreatedByID : Edm.Guid "Created By"
PX.Api.SYProviderObject.CreatedByScreenID : Edm.String
PX.Api.SYProviderObject.CreatedDateTime : Edm.DateTimeOffset
PX.Api.SYProviderObject.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.SYProviderObject.LastModifiedByScreenID : Edm.String
PX.Api.SYProviderObject.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.SYProviderObject.TStamp : Edm.Binary
PX.Api.SYProviderObject.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.SYProviderObject.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.SYProviderObject.SYProviderByProviderID -> PX.Api.SYProvider (ProviderID=ProviderID)
PX.Api.SYProviderObject.SYMappingCollection -> Collection(PX.Api.SYMapping)
PX.Api.SYProviderObject.SYProviderFieldCollection -> Collection(PX.Api.SYProviderField)

# PX.Api.SYServiceSchema (EntityType)

Key: ScreenID, ServiceID
Entity sets: PX_Api_SYServiceSchema
Non-filterable, non-selectable: Title, NoteText

PX.Api.SYServiceSchema.ServiceID : Edm.String [key]
PX.Api.SYServiceSchema.ScreenID : Edm.String [key] "Screen ID"
PX.Api.SYServiceSchema.IsIncluded : Edm.Boolean [required] "Active"
PX.Api.SYServiceSchema.IsGenerated : Edm.Boolean [required] "Generated"
PX.Api.SYServiceSchema.IsImport : Edm.Boolean "Import"
PX.Api.SYServiceSchema.IsExport : Edm.Boolean "Export"
PX.Api.SYServiceSchema.IsSubmit : Edm.Boolean "Submit"
PX.Api.SYServiceSchema.Title : Edm.String "Title"
PX.Api.SYServiceSchema.NoteID : Edm.Guid
PX.Api.SYServiceSchema.NoteText : Edm.String "Note Text"
PX.Api.SYServiceSchema.SYWebServiceByServiceID -> PX.Api.SYWebService (ServiceID=ServiceID)

# PX.Api.SYSubstitution (EntityType)

Key: SubstitutionID
Entity sets: PX_Api_SYSubstitution

PX.Api.SYSubstitution.SubstitutionID : Edm.String [key] "Substitution List"
PX.Api.SYSubstitution.TableName : Edm.String "Table Name"
PX.Api.SYSubstitution.FieldName : Edm.String "Field Name"
PX.Api.SYSubstitution.TStamp : Edm.Binary
PX.Api.SYSubstitution.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Api.SYSubstitution.BCBindingBigCommerceCollection -> Collection(PX.Commerce.BigCommerce.BCBindingBigCommerce)
PX.Api.SYSubstitution.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Api.SYSubstitution.SYSubstitutionValuesCollection -> Collection(PX.Api.SYSubstitutionValues)

# PX.Api.SYSubstitutionValues (EntityType)

Key: SubstitutionID, ValueID
Entity sets: PX_Api_SYSubstitutionValues

PX.Api.SYSubstitutionValues.SubstitutionID : Edm.String [key]
PX.Api.SYSubstitutionValues.ValueID : Edm.Int64 [key]
PX.Api.SYSubstitutionValues.OriginalValue : Edm.String "Original Value"
PX.Api.SYSubstitutionValues.SubstitutedValue : Edm.String "Substitution Value"
PX.Api.SYSubstitutionValues.TStamp : Edm.Binary
PX.Api.SYSubstitutionValues.SYSubstitutionBySubstitutionID -> PX.Api.SYSubstitution (SubstitutionID=SubstitutionID)

# PX.Api.SYWebService (EntityType)

Key: ServiceID
Entity sets: PX_Api_SYWebService
Non-filterable, non-selectable: NoteText, CurSysVer

PX.Api.SYWebService.ServiceID : Edm.String [key] "Service ID"
PX.Api.SYWebService.Description : Edm.String "Description"
PX.Api.SYWebService.IncludeUntyped : Edm.Boolean [required] "Include Untyped"
PX.Api.SYWebService.DateGenerated : Edm.DateTimeOffset "System Time"
PX.Api.SYWebService.SysVerWhenGenerated : Edm.String "System Version"
PX.Api.SYWebService.IsGenerated : Edm.Boolean [required] "Is Generated"
PX.Api.SYWebService.WSDL : Edm.String "WSDL"
PX.Api.SYWebService.IsImport : Edm.Boolean [required] "Import"
PX.Api.SYWebService.IsExport : Edm.Boolean [required] "Export"
PX.Api.SYWebService.IsSubmit : Edm.Boolean [required] "Submit"
PX.Api.SYWebService.NoteID : Edm.Guid
PX.Api.SYWebService.NoteText : Edm.String "Note Text"
PX.Api.SYWebService.CurSysVer : Edm.String "Current System Version"
PX.Api.SYWebService.SYServiceSchemaCollection -> Collection(PX.Api.SYServiceSchema)

# PX.Api.Webhooks.DAC.WebHook (EntityType)

Key: Name
Entity sets: PX_Api_Webhooks_DAC_WebHook
Non-filterable, non-selectable: NoteText, Url

PX.Api.Webhooks.DAC.WebHook.WebHookID : Edm.Guid
PX.Api.Webhooks.DAC.WebHook.Name : Edm.String [key] "Webhook Name"
PX.Api.Webhooks.DAC.WebHook.Handler : Edm.String "Implementation Class"
PX.Api.Webhooks.DAC.WebHook.IsActive : Edm.Boolean [required] "Active"
PX.Api.Webhooks.DAC.WebHook.IsSystem : Edm.Boolean [required] "Predefined"
PX.Api.Webhooks.DAC.WebHook.RequestLogLevel : Edm.Byte [required] "Requests to Keep"
PX.Api.Webhooks.DAC.WebHook.RequestRetainCount : Edm.Int16 [required] "Maximum Number of Requests in History"
PX.Api.Webhooks.DAC.WebHook.CreatedByID : Edm.Guid "Created By"
PX.Api.Webhooks.DAC.WebHook.CreatedByScreenID : Edm.String
PX.Api.Webhooks.DAC.WebHook.CreatedDateTime : Edm.DateTimeOffset
PX.Api.Webhooks.DAC.WebHook.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Api.Webhooks.DAC.WebHook.LastModifiedByScreenID : Edm.String
PX.Api.Webhooks.DAC.WebHook.LastModifiedDateTime : Edm.DateTimeOffset
PX.Api.Webhooks.DAC.WebHook.TStamp : Edm.Binary
PX.Api.Webhooks.DAC.WebHook.NoteID : Edm.Guid
PX.Api.Webhooks.DAC.WebHook.NoteText : Edm.String "Note Text"
PX.Api.Webhooks.DAC.WebHook.Url : Edm.String "URL"
PX.Api.Webhooks.DAC.WebHook.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Api.Webhooks.DAC.WebHook.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Api.Webhooks.DAC.WebHook.SMSendGridSettingsCollection -> Collection(PX.DataSync.SendGrid.SMSendGridSettings)
PX.Api.Webhooks.DAC.WebHook.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Api.Webhooks.DAC.WebHook.PPExternalSettingCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPExternalSetting)

# PX.Api.Webhooks.WebHookRequest (EntityType)

Key: RequestID, WebHookID
Entity sets: PX_Api_Webhooks_WebHookRequest

PX.Api.Webhooks.WebHookRequest.WebHookID : Edm.Guid [key]
PX.Api.Webhooks.WebHookRequest.RequestID : Edm.Int64 [key]
PX.Api.Webhooks.WebHookRequest.Type : Edm.String "Request"
PX.Api.Webhooks.WebHookRequest.Request : Edm.String "Request"
PX.Api.Webhooks.WebHookRequest.Response : Edm.String "Response"
PX.Api.Webhooks.WebHookRequest.ResponseStatus : Edm.Int32 "Response Status"
PX.Api.Webhooks.WebHookRequest.ProcessingTime : Edm.Int32 "Processing Time (ms)"
PX.Api.Webhooks.WebHookRequest.ReceiveDate : Edm.DateTimeOffset "Date"
PX.Api.Webhooks.WebHookRequest.ReceivedFrom : Edm.String "Received From"
PX.Api.Webhooks.WebHookRequest.Error : Edm.String "Error"

# PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun (EntityType)

Label: "GeneratorRun"
Key: RunId, UserId
Entity sets: PX_AutocompleteGenerator_UI_DAC_AutocompleteGeneratorRun, GeneratorRun, AutocompleteGeneratorRun
Non-filterable, non-selectable: SuccessString, NoteText

PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.RunId : Edm.Guid [key] "Run Identifier"
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.UserId : Edm.Guid [key] "User"
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.Model : Edm.String "Model"
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.Logs : Edm.String "Logs"
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.Success : Edm.Boolean "Generation Result"
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.SuccessString : Edm.String "Generation Result"
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.CreatedDateTime : Edm.DateTimeOffset "Last Generated On"
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.NoteID : Edm.Guid
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.NoteText : Edm.String "Note Text"
PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun.UsersByUserId -> PX.SM.Users (UserId=PKID)

# PX.AutocompleteGenerator.UI.DAC.LastRunOfUser (EntityType)

Label: "GeneratorRun"
BaseType: PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun
Key: RunId, UserId (inherited from PX.AutocompleteGenerator.UI.DAC.AutocompleteGeneratorRun)
Entity sets: PX_AutocompleteGenerator_UI_DAC_LastRunOfUser

# PX.BusinessProcess.DAC.ActionExecution (EntityType)

Label: "Action Execution"
Key: ExecutionID
Entity sets: PX_BusinessProcess_DAC_ActionExecution, ActionExecution
Non-filterable, non-selectable: NoteText, ActionNameMethod, ShowCreatedByEventsTabExpr

PX.BusinessProcess.DAC.ActionExecution.ExecutionID : Edm.Guid [key] "Subscriber ID"
PX.BusinessProcess.DAC.ActionExecution.Name : Edm.String "Subscriber Name"
PX.BusinessProcess.DAC.ActionExecution.ActionScreenID : Edm.String "Action Screen ID"
PX.BusinessProcess.DAC.ActionExecution.ScreenID : Edm.String "Event Screen ID"
PX.BusinessProcess.DAC.ActionExecution.ActionName : Edm.String "Action Name"
PX.BusinessProcess.DAC.ActionExecution.MappingCntr : Edm.Int16 [required]
PX.BusinessProcess.DAC.ActionExecution.ParameterCntr : Edm.Int16 [required]
PX.BusinessProcess.DAC.ActionExecution.NoteID : Edm.Guid
PX.BusinessProcess.DAC.ActionExecution.NoteText : Edm.String "Note Text"
PX.BusinessProcess.DAC.ActionExecution.CreatedByID : Edm.Guid "Created By"
PX.BusinessProcess.DAC.ActionExecution.CreatedByScreenID : Edm.String
PX.BusinessProcess.DAC.ActionExecution.CreatedDateTime : Edm.DateTimeOffset
PX.BusinessProcess.DAC.ActionExecution.LastModifiedByID : Edm.Guid "Last Modified By"
PX.BusinessProcess.DAC.ActionExecution.LastModifiedByScreenID : Edm.String
PX.BusinessProcess.DAC.ActionExecution.LastModifiedDateTime : Edm.DateTimeOffset
PX.BusinessProcess.DAC.ActionExecution.tstamp : Edm.Binary
PX.BusinessProcess.DAC.ActionExecution.ActionNameMethod : Edm.String "Action Name"
PX.BusinessProcess.DAC.ActionExecution.ShowCreatedByEventsTabExpr : Edm.Boolean "ShowCreatedByEventsTabExpr"
PX.BusinessProcess.DAC.ActionExecution.SiteMapByActionScreenID -> PX.SM.SiteMap (ActionScreenID=ScreenID)
PX.BusinessProcess.DAC.ActionExecution.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.BusinessProcess.DAC.ActionExecution.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.BusinessProcess.DAC.ActionExecution.ActionExecutionMappingCollection -> Collection(PX.BusinessProcess.DAC.ActionExecutionMapping)
PX.BusinessProcess.DAC.ActionExecution.ActionExecutionParameterCollection -> Collection(PX.BusinessProcess.DAC.ActionExecutionParameter)
PX.BusinessProcess.DAC.ActionExecution.BPEventSubscriberCollection -> Collection(PX.BusinessProcess.DAC.BPEventSubscriber)

# PX.BusinessProcess.DAC.ActionExecutionMapping (EntityType)

Label: "Action Execution Mapping"
Key: ExecutionID, LineNbr
Entity sets: PX_BusinessProcess_DAC_ActionExecutionMapping, ActionExecutionMapping
Non-filterable, non-selectable: DisplayFieldName

PX.BusinessProcess.DAC.ActionExecutionMapping.ExecutionID : Edm.Guid [key]
PX.BusinessProcess.DAC.ActionExecutionMapping.LineNbr : Edm.Int16 [key required]
PX.BusinessProcess.DAC.ActionExecutionMapping.FieldName : Edm.String "Screen Key Field"
PX.BusinessProcess.DAC.ActionExecutionMapping.FromSchema : Edm.Boolean [required] "From Schema"
PX.BusinessProcess.DAC.ActionExecutionMapping.Value : Edm.String "Value"
PX.BusinessProcess.DAC.ActionExecutionMapping.DataType : Edm.Int32
PX.BusinessProcess.DAC.ActionExecutionMapping.CreatedByID : Edm.Guid "Created By"
PX.BusinessProcess.DAC.ActionExecutionMapping.CreatedByScreenID : Edm.String
PX.BusinessProcess.DAC.ActionExecutionMapping.CreatedDateTime : Edm.DateTimeOffset
PX.BusinessProcess.DAC.ActionExecutionMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.BusinessProcess.DAC.ActionExecutionMapping.LastModifiedByScreenID : Edm.String
PX.BusinessProcess.DAC.ActionExecutionMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.BusinessProcess.DAC.ActionExecutionMapping.tstamp : Edm.Binary
PX.BusinessProcess.DAC.ActionExecutionMapping.DisplayFieldName : Edm.String "Screen Key Field"
PX.BusinessProcess.DAC.ActionExecutionMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.BusinessProcess.DAC.ActionExecutionMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.BusinessProcess.DAC.ActionExecutionMapping.ActionExecutionByExecutionID -> PX.BusinessProcess.DAC.ActionExecution (ExecutionID=ExecutionID)

# PX.BusinessProcess.DAC.ActionExecutionParameter (EntityType)

Label: "Action Execution Parameter"
Key: ExecutionID, LineNbr
Entity sets: PX_BusinessProcess_DAC_ActionExecutionParameter, ActionExecutionParameter

PX.BusinessProcess.DAC.ActionExecutionParameter.ExecutionID : Edm.Guid [key]
PX.BusinessProcess.DAC.ActionExecutionParameter.LineNbr : Edm.Int16 [key required]
PX.BusinessProcess.DAC.ActionExecutionParameter.ObjectName : Edm.String "Object Name"
PX.BusinessProcess.DAC.ActionExecutionParameter.FieldName : Edm.String "Field"
PX.BusinessProcess.DAC.ActionExecutionParameter.FromSchema : Edm.Boolean [required] "From Schema"
PX.BusinessProcess.DAC.ActionExecutionParameter.Value : Edm.String "Value"
PX.BusinessProcess.DAC.ActionExecutionParameter.DataType : Edm.Int32
PX.BusinessProcess.DAC.ActionExecutionParameter.CreatedByID : Edm.Guid "Created By"
PX.BusinessProcess.DAC.ActionExecutionParameter.CreatedByScreenID : Edm.String
PX.BusinessProcess.DAC.ActionExecutionParameter.CreatedDateTime : Edm.DateTimeOffset
PX.BusinessProcess.DAC.ActionExecutionParameter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.BusinessProcess.DAC.ActionExecutionParameter.LastModifiedByScreenID : Edm.String
PX.BusinessProcess.DAC.ActionExecutionParameter.LastModifiedDateTime : Edm.DateTimeOffset
PX.BusinessProcess.DAC.ActionExecutionParameter.tstamp : Edm.Binary
PX.BusinessProcess.DAC.ActionExecutionParameter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.BusinessProcess.DAC.ActionExecutionParameter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.BusinessProcess.DAC.ActionExecutionParameter.ActionExecutionByExecutionID -> PX.BusinessProcess.DAC.ActionExecution (ExecutionID=ExecutionID)

# PX.BusinessProcess.DAC.BPEvent (EntityType)

Label: "Business Process Event"
Key: Name
Entity sets: PX_BusinessProcess_DAC_BPEvent, BusinessProcessEvent, BPEvent
Non-filterable, non-selectable: ScreenIdValue, NoteText, ActionName2, GroupBy, IsGroupByOldValue, IsTriggerConditionsVisible

PX.BusinessProcess.DAC.BPEvent.EventID : Edm.Guid
PX.BusinessProcess.DAC.BPEvent.Name : Edm.String [key] "Event ID"
PX.BusinessProcess.DAC.BPEvent.Description : Edm.String "Description"
PX.BusinessProcess.DAC.BPEvent.ScreenID : Edm.String "Screen Name"
PX.BusinessProcess.DAC.BPEvent.ViewName : Edm.String
PX.BusinessProcess.DAC.BPEvent.RowProcessingType : Edm.Byte [required] "Raise Event"
PX.BusinessProcess.DAC.BPEvent.ScreenIdValue : Edm.String "Screen ID"
PX.BusinessProcess.DAC.BPEvent.Active : Edm.Boolean [required] "Active"
PX.BusinessProcess.DAC.BPEvent.FilterID : Edm.Guid "Shared Filter to Apply"
PX.BusinessProcess.DAC.BPEvent.NoteID : Edm.Guid
PX.BusinessProcess.DAC.BPEvent.NoteText : Edm.String "Note Text"
PX.BusinessProcess.DAC.BPEvent.Type : Edm.Byte [required] "Type"
PX.BusinessProcess.DAC.BPEvent.RunSynchronously : Edm.Boolean [required] "Process Synchronously"
PX.BusinessProcess.DAC.BPEvent.ActionName : Edm.String "Action Name"
PX.BusinessProcess.DAC.BPEvent.ActionName2 : Edm.String "Action Name"
PX.BusinessProcess.DAC.BPEvent.ShowMassAction : Edm.Boolean [required] "Add Action to Process All"
PX.BusinessProcess.DAC.BPEvent.GroupBy : Edm.String "Group Records By"
PX.BusinessProcess.DAC.BPEvent.GroupingField : Edm.String
PX.BusinessProcess.DAC.BPEvent.GroupingTable : Edm.String
PX.BusinessProcess.DAC.BPEvent.IsGroupByNew : Edm.Boolean [required]
PX.BusinessProcess.DAC.BPEvent.IsGroupByOldValue : Edm.Boolean "Use Previous Value"
PX.BusinessProcess.DAC.BPEvent.TrackAllFields : Edm.Boolean "Track All Fields"
PX.BusinessProcess.DAC.BPEvent.CreatedByID : Edm.Guid "Created By"
PX.BusinessProcess.DAC.BPEvent.CreatedByScreenID : Edm.String "Created by Screen ID"
PX.BusinessProcess.DAC.BPEvent.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.BusinessProcess.DAC.BPEvent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.BusinessProcess.DAC.BPEvent.LastModifiedByScreenID : Edm.String "Last Modified by Screen ID"
PX.BusinessProcess.DAC.BPEvent.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.BusinessProcess.DAC.BPEvent.IsTriggerConditionsVisible : Edm.Boolean "IsTriggerConditionsVisible"
PX.BusinessProcess.DAC.BPEvent.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.BusinessProcess.DAC.BPEvent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.BusinessProcess.DAC.BPEvent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.BusinessProcess.DAC.BPEvent.FilterHeaderByFilterID -> PX.Data.FilterHeader (FilterID=FilterID)
PX.BusinessProcess.DAC.BPEvent.BPEventSubscriberCollection -> Collection(PX.BusinessProcess.DAC.BPEventSubscriber)
PX.BusinessProcess.DAC.BPEvent.BPEventScheduleCollection -> Collection(PX.BusinessProcess.DAC.BPEventSchedule)
PX.BusinessProcess.DAC.BPEvent.BPEventHistoryCollection -> Collection(PX.BusinessProcess.DAC.BPEventHistory)
PX.BusinessProcess.DAC.BPEvent.BPEventTrackingFieldCollection -> Collection(PX.BusinessProcess.DAC.BPEventTrackingField)
PX.BusinessProcess.DAC.BPEvent.BPEventTriggerConditionCollection -> Collection(PX.BusinessProcess.DAC.BPEventTriggerCondition)
PX.BusinessProcess.DAC.BPEvent.BPInquiryParameterCollection -> Collection(PX.BusinessProcess.DAC.BPInquiryParameter)

# PX.BusinessProcess.DAC.BPEventHistory (EntityType)

Label: "Business Process Event History"
Key: EventDefinitionID, EventID
Entity sets: PX_BusinessProcess_DAC_BPEventHistory, BusinessProcessEventHistory, BPEventHistory
Non-filterable, non-selectable: Source, CanBeResumed, LastRunStatus

PX.BusinessProcess.DAC.BPEventHistory.EventID : Edm.Guid [key] "Event ID"
PX.BusinessProcess.DAC.BPEventHistory.EventDefinitionID : Edm.Guid [key] "Event Definition ID"
PX.BusinessProcess.DAC.BPEventHistory.RefNoteID : Edm.Guid
PX.BusinessProcess.DAC.BPEventHistory.RefEntityType : Edm.String
PX.BusinessProcess.DAC.BPEventHistory.Source : Edm.String "Related Entity"
PX.BusinessProcess.DAC.BPEventHistory.Payload : Edm.String "Payload"
PX.BusinessProcess.DAC.BPEventHistory.CreatedDateTime : Edm.DateTimeOffset "Triggered At"
PX.BusinessProcess.DAC.BPEventHistory.LastModifiedDateTime : Edm.DateTimeOffset "Processed At"
PX.BusinessProcess.DAC.BPEventHistory.ErrorText : Edm.String "Execution Result"
PX.BusinessProcess.DAC.BPEventHistory.Status : Edm.Byte "Status Description"
PX.BusinessProcess.DAC.BPEventHistory.CanBeResumed : Edm.Boolean "CanBeResumed"
PX.BusinessProcess.DAC.BPEventHistory.LastRunStatus : Edm.String "Status"
PX.BusinessProcess.DAC.BPEventHistory.BPEventByEventDefinitionID -> PX.BusinessProcess.DAC.BPEvent (EventDefinitionID=EventID)

# PX.BusinessProcess.DAC.BPEventSchedule (EntityType)

Label: "Business Process Event Schedule"
Key: EventID, ScheduleID
Entity sets: PX_BusinessProcess_DAC_BPEventSchedule, BusinessProcessEventSchedule, BPEventSchedule
Non-filterable, non-selectable: ScreenID

PX.BusinessProcess.DAC.BPEventSchedule.EventID : Edm.Guid [key] "Event ID"
PX.BusinessProcess.DAC.BPEventSchedule.ScheduleID : Edm.Int32 [key] "Schedule ID"
PX.BusinessProcess.DAC.BPEventSchedule.ScreenID : Edm.String "ScreenID"
PX.BusinessProcess.DAC.BPEventSchedule.Active : Edm.Boolean [required] "Active"
PX.BusinessProcess.DAC.BPEventSchedule.AUScheduleByScheduleID -> PX.SM.AUSchedule (ScheduleID=ScheduleID)
PX.BusinessProcess.DAC.BPEventSchedule.BPEventByEventID -> PX.BusinessProcess.DAC.BPEvent (EventID=EventID)

# PX.BusinessProcess.DAC.BPEventSetting (EntityType)

Singletons: PX_BusinessProcess_DAC_BPEventSetting

PX.BusinessProcess.DAC.BPEventSetting.HistoryRetainCount : Edm.Int16 "Days"
PX.BusinessProcess.DAC.BPEventSetting.DeleteHistoryAutomatically : Edm.Boolean [required] "Delete History Automatically After:"

# PX.BusinessProcess.DAC.BPEventSubscriber (EntityType)

Label: "Business Process Event Subscriber"
Key: EventID, HandlerID, Type
Entity sets: PX_BusinessProcess_DAC_BPEventSubscriber, BusinessProcessEventSubscriber, BPEventSubscriber
Non-filterable, non-selectable: ScreenId, LastRunStatus, Status, ErrorText

PX.BusinessProcess.DAC.BPEventSubscriber.EventID : Edm.Guid [key] "Event ID"
PX.BusinessProcess.DAC.BPEventSubscriber.HandlerID : Edm.Guid [key] "Subscriber ID"
PX.BusinessProcess.DAC.BPEventSubscriber.Active : Edm.Boolean [required] "Active"
PX.BusinessProcess.DAC.BPEventSubscriber.OpenAfterProcessing : Edm.Boolean [required] "Open After Processing"
PX.BusinessProcess.DAC.BPEventSubscriber.OrderNbr : Edm.Int16 "Sequence"
PX.BusinessProcess.DAC.BPEventSubscriber.Type : Edm.String [key required] "Type"
PX.BusinessProcess.DAC.BPEventSubscriber.StopOnError : Edm.Boolean [required] "Stop on Error"
PX.BusinessProcess.DAC.BPEventSubscriber.IsProcessSingleLine : Edm.Boolean [required] "Execute per Line"
PX.BusinessProcess.DAC.BPEventSubscriber.ScreenId : Edm.String "ScreenId"
PX.BusinessProcess.DAC.BPEventSubscriber.LastRunStatus : Edm.String "Status"
PX.BusinessProcess.DAC.BPEventSubscriber.Status : Edm.Int32 "Status"
PX.BusinessProcess.DAC.BPEventSubscriber.ErrorText : Edm.String "Error Text"
PX.BusinessProcess.DAC.BPEventSubscriber.NotificationByHandlerID -> PX.SM.Notification (HandlerID=NoteID)
PX.BusinessProcess.DAC.BPEventSubscriber.ActionExecutionByHandlerID -> PX.BusinessProcess.DAC.ActionExecution (HandlerID=ExecutionID)
PX.BusinessProcess.DAC.BPEventSubscriber.SYMappingByHandlerID -> PX.Api.SYMapping (HandlerID=MappingID)
PX.BusinessProcess.DAC.BPEventSubscriber.TaskTemplateByHandlerID -> PX.SM.TaskTemplate (HandlerID=NoteID)
PX.BusinessProcess.DAC.BPEventSubscriber.BPEventByEventID -> PX.BusinessProcess.DAC.BPEvent (EventID=EventID)
PX.BusinessProcess.DAC.BPEventSubscriber.MobileNotificationByHandlerID -> PX.BusinessProcess.DAC.MobileNotification (HandlerID=NoteID)

# PX.BusinessProcess.DAC.BPEventTrackingField (EntityType)

Label: "Business Process Tracked Field"
Key: EventID, FieldID
Entity sets: PX_BusinessProcess_DAC_BPEventTrackingField, BusinessProcessTrackedField, BPEventTrackingField
Non-filterable, non-selectable: IsFromTriggerCondition, IsFromInsertOrDeleteTriggerCondition

PX.BusinessProcess.DAC.BPEventTrackingField.EventID : Edm.Guid [key]
PX.BusinessProcess.DAC.BPEventTrackingField.FieldID : Edm.Int32 [key]
PX.BusinessProcess.DAC.BPEventTrackingField.TableName : Edm.String "Table Name"
PX.BusinessProcess.DAC.BPEventTrackingField.FieldName : Edm.String "Field Name"
PX.BusinessProcess.DAC.BPEventTrackingField.IsFromTriggerCondition : Edm.Boolean
PX.BusinessProcess.DAC.BPEventTrackingField.IsFromInsertOrDeleteTriggerCondition : Edm.Boolean
PX.BusinessProcess.DAC.BPEventTrackingField.BPEventByEventID -> PX.BusinessProcess.DAC.BPEvent (EventID=EventID)

# PX.BusinessProcess.DAC.BPEventTriggerCondition (EntityType)

Label: "Business Process Event Trigger Condition"
Key: EventID, OrderNbr
Entity sets: PX_BusinessProcess_DAC_BPEventTriggerCondition, BusinessProcessEventTriggerCondition, BPEventTriggerCondition

PX.BusinessProcess.DAC.BPEventTriggerCondition.EventID : Edm.Guid [key] "Event ID"
PX.BusinessProcess.DAC.BPEventTriggerCondition.OrderNbr : Edm.Int16 [key] "Order Number"
PX.BusinessProcess.DAC.BPEventTriggerCondition.TableName : Edm.String "Table Name"
PX.BusinessProcess.DAC.BPEventTriggerCondition.Operation : Edm.Byte "Operation"
PX.BusinessProcess.DAC.BPEventTriggerCondition.Active : Edm.Boolean [required] "Active"
PX.BusinessProcess.DAC.BPEventTriggerCondition.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.BusinessProcess.DAC.BPEventTriggerCondition.FieldName : Edm.String "Field Name"
PX.BusinessProcess.DAC.BPEventTriggerCondition.Condition : Edm.Byte "Condition"
PX.BusinessProcess.DAC.BPEventTriggerCondition.IsFromSchema : Edm.Boolean [required] "From Schema"
PX.BusinessProcess.DAC.BPEventTriggerCondition.Value : Edm.String "Value 1"
PX.BusinessProcess.DAC.BPEventTriggerCondition.Value2 : Edm.String "Value 2"
PX.BusinessProcess.DAC.BPEventTriggerCondition.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.BusinessProcess.DAC.BPEventTriggerCondition.Operator : Edm.Int32 [required] "Operator"
PX.BusinessProcess.DAC.BPEventTriggerCondition.DataType : Edm.Int32
PX.BusinessProcess.DAC.BPEventTriggerCondition.BPEventByEventID -> PX.BusinessProcess.DAC.BPEvent (EventID=EventID)

# PX.BusinessProcess.DAC.BPInquiryParameter (EntityType)

Label: "Business Process Inquiry Parameter"
Key: EventID, Name
Entity sets: PX_BusinessProcess_DAC_BPInquiryParameter, BusinessProcessInquiryParameter, BPInquiryParameter
Non-filterable, non-selectable: DisplayName, DefaultValue, UseDefault

PX.BusinessProcess.DAC.BPInquiryParameter.EventID : Edm.Guid [key] "Event ID"
PX.BusinessProcess.DAC.BPInquiryParameter.Name : Edm.String [key]
PX.BusinessProcess.DAC.BPInquiryParameter.DisplayName : Edm.String "Display Name"
PX.BusinessProcess.DAC.BPInquiryParameter.FieldType : Edm.Int32 [required]
PX.BusinessProcess.DAC.BPInquiryParameter.DefaultValue : Edm.String
PX.BusinessProcess.DAC.BPInquiryParameter.Value : Edm.String "Value"
PX.BusinessProcess.DAC.BPInquiryParameter.UseDefault : Edm.Boolean "Use Default Value"
PX.BusinessProcess.DAC.BPInquiryParameter.BPEventByEventID -> PX.BusinessProcess.DAC.BPEvent (EventID=EventID)

# PX.BusinessProcess.DAC.BPProcessedEventSubscribers (EntityType)

Key: Id
Entity sets: PX_BusinessProcess_DAC_BPProcessedEventSubscribers

PX.BusinessProcess.DAC.BPProcessedEventSubscribers.Id : Edm.Guid [key]
PX.BusinessProcess.DAC.BPProcessedEventSubscribers.ProcessedSubscribers : Edm.String
PX.BusinessProcess.DAC.BPProcessedEventSubscribers.WorkflowInstance : Edm.String
PX.BusinessProcess.DAC.BPProcessedEventSubscribers.LastModifiedDateTime : Edm.DateTimeOffset "Processed Date"

# PX.BusinessProcess.DAC.DispatcherStatisticEventDetail (EntityType)

Label: "DispatcherStatisticEventDetail"
Key: BusinessEventName, Id
Entity sets: PX_BusinessProcess_DAC_DispatcherStatisticEventDetail, DispatcherStatisticEventDetail

PX.BusinessProcess.DAC.DispatcherStatisticEventDetail.Id : Edm.Guid [key] "ID"
PX.BusinessProcess.DAC.DispatcherStatisticEventDetail.BusinessEventName : Edm.String [key] "Event Name"
PX.BusinessProcess.DAC.DispatcherStatisticEventDetail.Count : Edm.Int32 [required] "Messages"

# PX.BusinessProcess.DAC.DispatcherStatus (EntityType)

Key: QueueType, WebsiteID
Entity sets: PX_BusinessProcess_DAC_DispatcherStatus
Non-filterable, non-selectable: Order, PerformanceStatus, QueueSize, LastError, LastMessageProcessTime, LastFailedToCommitMessage, IsCurrentNode

PX.BusinessProcess.DAC.DispatcherStatus.WebsiteID : Edm.String [key] "Node ID"
PX.BusinessProcess.DAC.DispatcherStatus.QueueType : Edm.String [key] "Queue Type"
PX.BusinessProcess.DAC.DispatcherStatus.Order : Edm.Int32
PX.BusinessProcess.DAC.DispatcherStatus.QueueName : Edm.String "Queue Name"
PX.BusinessProcess.DAC.DispatcherStatus.Status : Edm.Int32 "Status"
PX.BusinessProcess.DAC.DispatcherStatus.HasFailedToCommitMessage : Edm.Boolean [required]
PX.BusinessProcess.DAC.DispatcherStatus.PerformanceStatus : Edm.Int32 "Processing Performance"
PX.BusinessProcess.DAC.DispatcherStatus.QueueCount : Edm.Int32 "Messages"
PX.BusinessProcess.DAC.DispatcherStatus.CurrentSize : Edm.Int64
PX.BusinessProcess.DAC.DispatcherStatus.MaxSize : Edm.Int64
PX.BusinessProcess.DAC.DispatcherStatus.QueueSize : Edm.String "Queue Size (KB)"
PX.BusinessProcess.DAC.DispatcherStatus.LastReportDateTime : Edm.DateTimeOffset "Last Response"
PX.BusinessProcess.DAC.DispatcherStatus.LastError : Edm.String
PX.BusinessProcess.DAC.DispatcherStatus.LastMessageProcessTime : Edm.Int64
PX.BusinessProcess.DAC.DispatcherStatus.LastFailedToCommitMessage : Edm.String
PX.BusinessProcess.DAC.DispatcherStatus.IsCurrentNode : Edm.Boolean "Current Node"

# PX.BusinessProcess.DAC.MobileNotification (EntityType)

Label: "Mobile Notification"
Key: NotificationID
Entity sets: PX_BusinessProcess_DAC_MobileNotification, MobileNotification
Non-filterable, non-selectable: ScreenIdValue, NoteText, ShowSendByEventsTabExpr

PX.BusinessProcess.DAC.MobileNotification.NotificationID : Edm.Int32 [key] "Notification ID"
PX.BusinessProcess.DAC.MobileNotification.Name : Edm.String "Description"
PX.BusinessProcess.DAC.MobileNotification.NTo : Edm.String "To"
PX.BusinessProcess.DAC.MobileNotification.Subject : Edm.String "Title"
PX.BusinessProcess.DAC.MobileNotification.ScreenID : Edm.String "Screen"
PX.BusinessProcess.DAC.MobileNotification.ScreenIdValue : Edm.String "Screen ID"
PX.BusinessProcess.DAC.MobileNotification.Body : Edm.String "Message"
PX.BusinessProcess.DAC.MobileNotification.LocaleName : Edm.String "Locale"
PX.BusinessProcess.DAC.MobileNotification.NoteID : Edm.Guid
PX.BusinessProcess.DAC.MobileNotification.NoteText : Edm.String "Note Text"
PX.BusinessProcess.DAC.MobileNotification.CreatedByID : Edm.Guid "Created By"
PX.BusinessProcess.DAC.MobileNotification.CreatedByScreenID : Edm.String
PX.BusinessProcess.DAC.MobileNotification.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.BusinessProcess.DAC.MobileNotification.LastModifiedByID : Edm.Guid "Last Modified By"
PX.BusinessProcess.DAC.MobileNotification.LastModifiedByScreenID : Edm.String
PX.BusinessProcess.DAC.MobileNotification.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.BusinessProcess.DAC.MobileNotification.tstamp : Edm.Binary
PX.BusinessProcess.DAC.MobileNotification.DestinationScreenID : Edm.String "Destination Screen ID"
PX.BusinessProcess.DAC.MobileNotification.DestinationEntityID : Edm.String "Destination Entity ID"
PX.BusinessProcess.DAC.MobileNotification.DeliveryType : Edm.Byte [required] "Delivery Method"
PX.BusinessProcess.DAC.MobileNotification.NFrom : Edm.Guid "From"
PX.BusinessProcess.DAC.MobileNotification.ShowSendByEventsTabExpr : Edm.Boolean "ShowSendByEventsTabExpr"
PX.BusinessProcess.DAC.MobileNotification.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.BusinessProcess.DAC.MobileNotification.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.BusinessProcess.DAC.MobileNotification.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.BusinessProcess.DAC.MobileNotification.SmsPluginByNfrom -> PX.SmsProvider.SM.DAC.SmsPlugin
PX.BusinessProcess.DAC.MobileNotification.LocaleByLocaleName -> PX.SM.Locale (LocaleName=LocaleName)
PX.BusinessProcess.DAC.MobileNotification.QueueNotificationSettingsCollection -> Collection(PX.BusinessProcess.DAC.QueueNotificationSettings)
PX.BusinessProcess.DAC.MobileNotification.BPEventSubscriberCollection -> Collection(PX.BusinessProcess.DAC.BPEventSubscriber)

# PX.BusinessProcess.DAC.QueueNotificationSettings (EntityType)

Label: "Notification Settings"
Key: SettingID
Entity sets: PX_BusinessProcess_DAC_QueueNotificationSettings, NotificationSettings, QueueNotificationSettings
Non-filterable, non-selectable: QueueMonitorScreenId, DeliveryTypeSms, DeliveryTypePush, NoteText

PX.BusinessProcess.DAC.QueueNotificationSettings.SettingID : Edm.Guid [key]
PX.BusinessProcess.DAC.QueueNotificationSettings.QueueType : Edm.String
PX.BusinessProcess.DAC.QueueNotificationSettings.IsEmailActive : Edm.Boolean [required] "Send Notifications By Email"
PX.BusinessProcess.DAC.QueueNotificationSettings.IsMobileSmsActive : Edm.Boolean [required] "Send Notifications By SMS"
PX.BusinessProcess.DAC.QueueNotificationSettings.IsMobilePushActive : Edm.Boolean [required] "Send Notifications By Push"
PX.BusinessProcess.DAC.QueueNotificationSettings.EmailNotificationID : Edm.Guid "Template"
PX.BusinessProcess.DAC.QueueNotificationSettings.MobileSmsNotificationID : Edm.Guid "Template"
PX.BusinessProcess.DAC.QueueNotificationSettings.MobilePushNotificationID : Edm.Guid "Template"
PX.BusinessProcess.DAC.QueueNotificationSettings.FillThreshold : Edm.Byte "Notification Threshold (% of Maximum Queue Size)"
PX.BusinessProcess.DAC.QueueNotificationSettings.QueueMonitorScreenId : Edm.String
PX.BusinessProcess.DAC.QueueNotificationSettings.DeliveryTypeSms : Edm.Byte
PX.BusinessProcess.DAC.QueueNotificationSettings.DeliveryTypePush : Edm.Byte
PX.BusinessProcess.DAC.QueueNotificationSettings.NoteID : Edm.Guid
PX.BusinessProcess.DAC.QueueNotificationSettings.NoteText : Edm.String "Note Text"
PX.BusinessProcess.DAC.QueueNotificationSettings.CreatedByID : Edm.Guid "Created By"
PX.BusinessProcess.DAC.QueueNotificationSettings.CreatedByScreenID : Edm.String
PX.BusinessProcess.DAC.QueueNotificationSettings.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.BusinessProcess.DAC.QueueNotificationSettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.BusinessProcess.DAC.QueueNotificationSettings.LastModifiedByScreenID : Edm.String
PX.BusinessProcess.DAC.QueueNotificationSettings.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.BusinessProcess.DAC.QueueNotificationSettings.tstamp : Edm.Binary
PX.BusinessProcess.DAC.QueueNotificationSettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.BusinessProcess.DAC.QueueNotificationSettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.BusinessProcess.DAC.QueueNotificationSettings.NotificationByEmailNotificationID -> PX.SM.Notification (EmailNotificationID=NoteID)
PX.BusinessProcess.DAC.QueueNotificationSettings.MobileNotificationByMobileSmsNotificationID -> PX.BusinessProcess.DAC.MobileNotification (MobileSmsNotificationID=NoteID)
PX.BusinessProcess.DAC.QueueNotificationSettings.MobileNotificationByMobilePushNotificationID -> PX.BusinessProcess.DAC.MobileNotification (MobilePushNotificationID=NoteID)

# PX.CloudServices.DAC.RecognizedRecord (EntityType)

Label: "Recognized Record"
Key: EntityType, RefNbr
Entity sets: PX_CloudServices_DAC_RecognizedRecord, RecognizedRecord1
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.CloudServices.DAC.RecognizedRecord.EntityType : Edm.String [key] "Entity Type"
PX.CloudServices.DAC.RecognizedRecord.RefNbr : Edm.Guid [key] "Ref. Nbr."
PX.CloudServices.DAC.RecognizedRecord.FileHash : Edm.Binary "File Hash"
PX.CloudServices.DAC.RecognizedRecord.Status : Edm.String "Status"
PX.CloudServices.DAC.RecognizedRecord.RecognitionStarted : Edm.Boolean [required] "Recognition Started"
PX.CloudServices.DAC.RecognizedRecord.RecognitionResult : Edm.String "Recognition Result"
PX.CloudServices.DAC.RecognizedRecord.RecognitionFeedback : Edm.String "Recognition Feedback"
PX.CloudServices.DAC.RecognizedRecord.DocumentLink : Edm.Guid "Document Link"
PX.CloudServices.DAC.RecognizedRecord.DuplicateLink : Edm.Guid "Duplicate Link"
PX.CloudServices.DAC.RecognizedRecord.MailFrom : Edm.String "From"
PX.CloudServices.DAC.RecognizedRecord.Subject : Edm.String "Summary"
PX.CloudServices.DAC.RecognizedRecord.MessageID : Edm.String "Message ID"
PX.CloudServices.DAC.RecognizedRecord.Owner : Edm.Int32 "Owner"
PX.CloudServices.DAC.RecognizedRecord.CustomInfo : Edm.String "Custom Info"
PX.CloudServices.DAC.RecognizedRecord.ErrorMessage : Edm.String "Error Message"
PX.CloudServices.DAC.RecognizedRecord.NoteID : Edm.Guid
PX.CloudServices.DAC.RecognizedRecord.NoteText : Edm.String "Note Text"
PX.CloudServices.DAC.RecognizedRecord.CreatedByID : Edm.Guid "Created By"
PX.CloudServices.DAC.RecognizedRecord.CreatedByScreenID : Edm.String
PX.CloudServices.DAC.RecognizedRecord.CreatedDateTime : Edm.DateTimeOffset
PX.CloudServices.DAC.RecognizedRecord.LastModifiedByID : Edm.Guid "Last Modified By"
PX.CloudServices.DAC.RecognizedRecord.LastModifiedByScreenID : Edm.String
PX.CloudServices.DAC.RecognizedRecord.LastModifiedDateTime : Edm.DateTimeOffset
PX.CloudServices.DAC.RecognizedRecord.TStamp : Edm.Binary
PX.CloudServices.DAC.RecognizedRecord.ResultUrl : Edm.String
PX.CloudServices.DAC.RecognizedRecord.CloudTenantId : Edm.Guid "CloudTenantId"
PX.CloudServices.DAC.RecognizedRecord.ModelName : Edm.String "ModelName"
PX.CloudServices.DAC.RecognizedRecord.CloudFileId : Edm.Guid "CloudFileId"
PX.CloudServices.DAC.RecognizedRecord.PageCount : Edm.Int32 "PageCount"
PX.CloudServices.DAC.RecognizedRecord.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.CloudServices.DAC.RecognizedRecord.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CloudServices.DAC.RecognizedRecord.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CloudServices.DAC.RecognizedRecord.RecognizedRecordSplitCollection -> Collection(PX.Objects.AP.InvoiceRecognition.DAC.RecognizedRecordSplit)

# PX.CloudServices.DAC.RecognizedRecordProjection (EntityType)

Label: "Recognized Record"
BaseType: PX.CloudServices.DAC.RecognizedRecord
Key: EntityType, RefNbr (inherited from PX.CloudServices.DAC.RecognizedRecord)
Entity sets: PX_CloudServices_DAC_RecognizedRecordProjection, RecognizedRecord, RecognizedRecordProjection

PX.CloudServices.DAC.RecognizedRecordProjection.APRefNbr : Edm.String
PX.CloudServices.DAC.RecognizedRecordProjection.EPRefNbr : Edm.String
PX.CloudServices.DAC.RecognizedRecordProjection.CNRefNbr : Edm.Int32
PX.CloudServices.DAC.RecognizedRecordProjection.LDRefNbr : Edm.Int32

# PX.Commerce.Amazon.BCAmazonTaxMapping (EntityType)

Label: "BCAmazonTaxMapping"
Key: BindingID, TaxMappingID
Entity sets: PX_Commerce_Amazon_BCAmazonTaxMapping, BCAmazonTaxMapping

PX.Commerce.Amazon.BCAmazonTaxMapping.BindingID : Edm.Int32 [key]
PX.Commerce.Amazon.BCAmazonTaxMapping.TaxMappingID : Edm.Int32 [key]
PX.Commerce.Amazon.BCAmazonTaxMapping.Active : Edm.Boolean [required] "Active"
PX.Commerce.Amazon.BCAmazonTaxMapping.IsDefault : Edm.Boolean [required] "Default"
PX.Commerce.Amazon.BCAmazonTaxMapping.TaxZoneID : Edm.String "Tax Zone"
PX.Commerce.Amazon.BCAmazonTaxMapping.TaxID : Edm.String "Tax ID"
PX.Commerce.Amazon.BCAmazonTaxMapping.TaxZoneBasedOn : Edm.String "Tax Zone Is Based On"
PX.Commerce.Amazon.BCAmazonTaxMapping.CountryID : Edm.String "Country"
PX.Commerce.Amazon.BCAmazonTaxMapping.Tstamp : Edm.Binary
PX.Commerce.Amazon.BCAmazonTaxMapping.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Amazon.BCAmazonTaxMapping.CreatedByScreenID : Edm.String "Created At"
PX.Commerce.Amazon.BCAmazonTaxMapping.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Commerce.Amazon.BCAmazonTaxMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Amazon.BCAmazonTaxMapping.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Commerce.Amazon.BCAmazonTaxMapping.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Commerce.Amazon.BCAmazonTaxMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Amazon.BCAmazonTaxMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Amazon.BCAmazonTaxMapping.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Commerce.Amazon.BCAmazonTaxMapping.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Commerce.Amazon.BCAmazonTaxMapping.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)

# PX.Commerce.Amazon.BCBindingAmazon (EntityType)

Label: "Amazon Settings"
Key: BindingID
Entity sets: PX_Commerce_Amazon_BCBindingAmazon, AmazonSettings, BCBindingAmazon

PX.Commerce.Amazon.BCBindingAmazon.BindingID : Edm.Int32 [key] "Store"
PX.Commerce.Amazon.BCBindingAmazon.SellerPartnerId : Edm.String "Seller Partner ID"
PX.Commerce.Amazon.BCBindingAmazon.Region : Edm.String "Region"
PX.Commerce.Amazon.BCBindingAmazon.Marketplace : Edm.String "Marketplace"
PX.Commerce.Amazon.BCBindingAmazon.RefreshToken : Edm.String "Refresh Token"
PX.Commerce.Amazon.BCBindingAmazon.SellerFulfilledOrderType : Edm.String "Seller-Fulfilled Order Type"
PX.Commerce.Amazon.BCBindingAmazon.AmazonFulfilledOrderType : Edm.String "Marketplace-Fulfilled Order Type"
PX.Commerce.Amazon.BCBindingAmazon.ShipViaCodesToCarriers : Edm.String "Ship Via Codes to Carriers"
PX.Commerce.Amazon.BCBindingAmazon.ShipViaCodesToCarrierServices : Edm.String "Ship Via Codes to Carrier Services"
PX.Commerce.Amazon.BCBindingAmazon.Warehouse : Edm.Int32 "Marketplace Warehouse"
PX.Commerce.Amazon.BCBindingAmazon.LocationID : Edm.Int32 "Marketplace Warehouse Location"
PX.Commerce.Amazon.BCBindingAmazon.ReleaseInvoices : Edm.Boolean "Release Invoices"
PX.Commerce.Amazon.BCBindingAmazon.ShippingPriceItem : Edm.Int32 "Shipping Price Item"
PX.Commerce.Amazon.BCBindingAmazon.SellerReturnOrderType : Edm.String "Seller-Fulfilled Return Type"
PX.Commerce.Amazon.BCBindingAmazon.AmazonReturnOrderType : Edm.String "Marketplace-Fulfilled Return Type"
PX.Commerce.Amazon.BCBindingAmazon.EarliestShipmentDate : Edm.DateTimeOffset "Earliest Shipment Date"
PX.Commerce.Amazon.BCBindingAmazon.TransferOrderType : Edm.String "Order Type for Import"
PX.Commerce.Amazon.BCBindingAmazon.SourceWarehouse : Edm.Int32 "Source Warehouse"
PX.Commerce.Amazon.BCBindingAmazon.CarriersToShipViaCodes : Edm.String "Ship-Via Codes to Carriers"
PX.Commerce.Amazon.BCBindingAmazon.ReturnChargeItem : Edm.Int32 "Charge Item"
PX.Commerce.Amazon.BCBindingAmazon.SettlementReportStartDate : Edm.DateTimeOffset "Earliest Report Date"
PX.Commerce.Amazon.BCBindingAmazon.tstamp : Edm.Binary
PX.Commerce.Amazon.BCBindingAmazon.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Amazon.BCBindingAmazon.CreatedByScreenID : Edm.String "Created At"
PX.Commerce.Amazon.BCBindingAmazon.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Commerce.Amazon.BCBindingAmazon.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Amazon.BCBindingAmazon.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Commerce.Amazon.BCBindingAmazon.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Commerce.Amazon.BCBindingAmazon.InventoryItemByShippingPriceItem -> PX.Objects.IN.InventoryItem (ShippingPriceItem=InventoryID)
PX.Commerce.Amazon.BCBindingAmazon.InventoryItemByReturnChargeItem -> PX.Objects.IN.InventoryItem (ReturnChargeItem=InventoryID)
PX.Commerce.Amazon.BCBindingAmazon.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Amazon.BCBindingAmazon.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Amazon.BCBindingAmazon.SOOrderTypeBySellerFulfilledOrderType -> PX.Objects.SO.SOOrderType (SellerFulfilledOrderType=OrderType)
PX.Commerce.Amazon.BCBindingAmazon.SOOrderTypeByAmazonFulfilledOrderType -> PX.Objects.SO.SOOrderType (AmazonFulfilledOrderType=OrderType)
PX.Commerce.Amazon.BCBindingAmazon.SOOrderTypeBySellerReturnOrderType -> PX.Objects.SO.SOOrderType (SellerReturnOrderType=OrderType)
PX.Commerce.Amazon.BCBindingAmazon.SOOrderTypeByAmazonReturnOrderType -> PX.Objects.SO.SOOrderType (AmazonReturnOrderType=OrderType)
PX.Commerce.Amazon.BCBindingAmazon.SOOrderTypeByTransferOrderType -> PX.Objects.SO.SOOrderType (TransferOrderType=OrderType)
PX.Commerce.Amazon.BCBindingAmazon.INLocationByWarehouse -> PX.Objects.IN.INLocation (LocationID=LocationID, Warehouse=SiteID)
PX.Commerce.Amazon.BCBindingAmazon.INSiteByWarehouse -> PX.Objects.IN.INSite (Warehouse=SiteID)
PX.Commerce.Amazon.BCBindingAmazon.INSiteBySourceWarehouse -> PX.Objects.IN.INSite (SourceWarehouse=SiteID)
PX.Commerce.Amazon.BCBindingAmazon.AccountByShippingAccount -> PX.Objects.GL.Account
PX.Commerce.Amazon.BCBindingAmazon.SubByShippingSubAccount -> PX.Objects.GL.Sub
PX.Commerce.Amazon.BCBindingAmazon.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)
PX.Commerce.Amazon.BCBindingAmazon.SYSubstitutionByShipViaCodesToCarriers -> PX.Api.SYSubstitution (ShipViaCodesToCarriers=SubstitutionID)
PX.Commerce.Amazon.BCBindingAmazon.SYSubstitutionByShipViaCodesToCarrierServices -> PX.Api.SYSubstitution (ShipViaCodesToCarrierServices=SubstitutionID)
PX.Commerce.Amazon.BCBindingAmazon.SYSubstitutionByCarriersToShipViaCodes -> PX.Api.SYSubstitution (CarriersToShipViaCodes=SubstitutionID)

# PX.Commerce.BigCommerce.BCBindingBigCommerce (EntityType)

Label: "BigCommerce Settings"
Key: BindingID
Entity sets: PX_Commerce_BigCommerce_BCBindingBigCommerce, BigCommerceSettings, BCBindingBigCommerce

PX.Commerce.BigCommerce.BCBindingBigCommerce.BindingID : Edm.Int32 [key] "Store"
PX.Commerce.BigCommerce.BCBindingBigCommerce.StoreBaseUrl : Edm.String "API Path"
PX.Commerce.BigCommerce.BCBindingBigCommerce.StoreXAuthClient : Edm.String "Client ID"
PX.Commerce.BigCommerce.BCBindingBigCommerce.StoreXAuthToken : Edm.String "Access Token"
PX.Commerce.BigCommerce.BCBindingBigCommerce.StoreWDAVServerUrl : Edm.String "WebDAV Path"
PX.Commerce.BigCommerce.BCBindingBigCommerce.StoreWDAVClientUser : Edm.String "WebDAV Username"
PX.Commerce.BigCommerce.BCBindingBigCommerce.StoreWDAVClientPass : Edm.String "WebDAV Password"
PX.Commerce.BigCommerce.BCBindingBigCommerce.StoreAdminUrl : Edm.String "Store Admin URL"
PX.Commerce.BigCommerce.BCBindingBigCommerce.DefaultLocationID : Edm.Int32 "Default Location ID"
PX.Commerce.BigCommerce.BCBindingBigCommerce.DefaultLocationName : Edm.String "Default Location"
PX.Commerce.BigCommerce.BCBindingBigCommerce.tstamp : Edm.Binary
PX.Commerce.BigCommerce.BCBindingBigCommerce.CreatedByID : Edm.Guid "Created By"
PX.Commerce.BigCommerce.BCBindingBigCommerce.CreatedByScreenID : Edm.String "Created At"
PX.Commerce.BigCommerce.BCBindingBigCommerce.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Commerce.BigCommerce.BCBindingBigCommerce.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.BigCommerce.BCBindingBigCommerce.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Commerce.BigCommerce.BCBindingBigCommerce.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Commerce.BigCommerce.BCBindingBigCommerce.ImportCompanyUsersAsCustomers : Edm.Boolean [required] "Import Company Users as Customers"
PX.Commerce.BigCommerce.BCBindingBigCommerce.SynchronizeOnlyDefaultCompanyAddress : Edm.Boolean [required] "Synchronize only Default Company Address"
PX.Commerce.BigCommerce.BCBindingBigCommerce.B2BPaymentMethodsSubstitutionListID : Edm.String "B2B Payment Methods"
PX.Commerce.BigCommerce.BCBindingBigCommerce.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.BigCommerce.BCBindingBigCommerce.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.BigCommerce.BCBindingBigCommerce.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)
PX.Commerce.BigCommerce.BCBindingBigCommerce.SYSubstitutionByB2BPaymentMethodsSubstitutionListID -> PX.Api.SYSubstitution (B2BPaymentMethodsSubstitutionListID=SubstitutionID)

# PX.Commerce.Core.BCBinding (EntityType)

Label: "Connection Settings"
Key: BindingName, ConnectorType
Entity sets: PX_Commerce_Core_BCBinding, ConnectionSettings, BCBinding
Non-filterable, non-selectable: AllowedStores, HasSyncStatuses

PX.Commerce.Core.BCBinding.ConnectorType : Edm.String [key] "Connector"
PX.Commerce.Core.BCBinding.BindingID : Edm.Int32 "Store ID"
PX.Commerce.Core.BCBinding.BindingName : Edm.String [key] "Store Name"
PX.Commerce.Core.BCBinding.BindingDescription : Edm.String "Store Description"
PX.Commerce.Core.BCBinding.IsActive : Edm.Boolean "Active"
PX.Commerce.Core.BCBinding.IsDefault : Edm.Boolean "Default"
PX.Commerce.Core.BCBinding.LocaleName : Edm.String "Locale"
PX.Commerce.Core.BCBinding.AllowedStores : Edm.Int32 "Max. Number of Stores"
PX.Commerce.Core.BCBinding.WebServicesEndpoint : Edm.String "Endpoint Name"
PX.Commerce.Core.BCBinding.WebServiceVersion : Edm.String "Endpoint Version"
PX.Commerce.Core.BCBinding.BindingAdministrator : Edm.Guid "Administrator"
PX.Commerce.Core.BCBinding.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Core.BCBinding.CreatedByScreenID : Edm.String
PX.Commerce.Core.BCBinding.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Commerce.Core.BCBinding.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Core.BCBinding.LastModifiedByScreenID : Edm.String
PX.Commerce.Core.BCBinding.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Commerce.Core.BCBinding.Tstamp : Edm.Binary "Tstamp"
PX.Commerce.Core.BCBinding.HasSyncStatuses : Edm.Boolean
PX.Commerce.Core.BCBinding.BranchByBranchID -> PX.Objects.GL.Branch
PX.Commerce.Core.BCBinding.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Core.BCBinding.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Core.BCBinding.UsersByBindingAdministrator -> PX.SM.Users (BindingAdministrator=PKID)
PX.Commerce.Core.BCBinding.EntityEndpointByWebServicesEndpoint -> PX.Api.ContractBased.UI.DAC.EntityEndpoint (WebServicesEndpoint=InterfaceName)
PX.Commerce.Core.BCBinding.LocaleByLocaleName -> PX.SM.Locale (LocaleName=LocaleName)
PX.Commerce.Core.BCBinding.BCSyncStatusCollection -> Collection(PX.Commerce.Core.BCSyncStatus)
PX.Commerce.Core.BCBinding.BCLocationsCollection -> Collection(PX.Commerce.Objects.BCLocations)
PX.Commerce.Core.BCBinding.BCAmazonTaxMappingCollection -> Collection(PX.Commerce.Amazon.BCAmazonTaxMapping)
PX.Commerce.Core.BCBinding.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Commerce.Core.BCBinding.BCBindingBigCommerceCollection -> Collection(PX.Commerce.BigCommerce.BCBindingBigCommerce)
PX.Commerce.Core.BCBinding.BCWebHookCollection -> Collection(PX.Commerce.Core.BCWebHook)
PX.Commerce.Core.BCBinding.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Commerce.Core.BCBinding.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Commerce.Core.BCBinding.BCPaymentMethodsCollection -> Collection(PX.Commerce.Objects.BCPaymentMethods)
PX.Commerce.Core.BCBinding.BCPaymentTermsMappingCollection -> Collection(PX.Commerce.Objects.BCPaymentTermsMapping)
PX.Commerce.Core.BCBinding.BCShippingMappingsCollection -> Collection(PX.Commerce.Objects.BCShippingMappings)
PX.Commerce.Core.BCBinding.BCEntityCollection -> Collection(PX.Commerce.Core.BCEntity)
PX.Commerce.Core.BCBinding.BCFeeMappingCollection -> Collection(PX.Commerce.Objects.BCFeeMapping)
PX.Commerce.Core.BCBinding.BCEntityStatsCollection -> Collection(PX.Commerce.Core.BCEntityStats)

# PX.Commerce.Core.BCEntitiesSyncStatistics (EntityType)

Label: "Sync Entities Counts"
Key: BindingId, ConnectorType, EntityType
Entity sets: PX_Commerce_Core_BCEntitiesSyncStatistics, SyncEntitiesCounts, BCEntitiesSyncStatistics

PX.Commerce.Core.BCEntitiesSyncStatistics.ConnectorType : Edm.String [key]
PX.Commerce.Core.BCEntitiesSyncStatistics.BindingId : Edm.Int32 [key]
PX.Commerce.Core.BCEntitiesSyncStatistics.EntityType : Edm.String [key]
PX.Commerce.Core.BCEntitiesSyncStatistics.PendingSyncCount : Edm.Int32
PX.Commerce.Core.BCEntitiesSyncStatistics.SyncedCount : Edm.Int32
PX.Commerce.Core.BCEntitiesSyncStatistics.TotalCount : Edm.Int32
PX.Commerce.Core.BCEntitiesSyncStatistics.BCEntityByEntityType -> PX.Commerce.Core.BCEntity (ConnectorType=ConnectorType, BindingId=BindingID, EntityType=EntityType)
PX.Commerce.Core.BCEntitiesSyncStatistics.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (ConnectorType=ConnectorType)
PX.Commerce.Core.BCEntitiesSyncStatistics.BCSyncStatusCollection -> Collection(PX.Commerce.Core.BCSyncStatus)
PX.Commerce.Core.BCEntitiesSyncStatistics.BCEntityExportFilterCollection -> Collection(PX.Commerce.Core.BCEntityExportFilter)
PX.Commerce.Core.BCEntitiesSyncStatistics.BCEntityExportMappingCollection -> Collection(PX.Commerce.Core.BCEntityExportMapping)
PX.Commerce.Core.BCEntitiesSyncStatistics.BCEntityImportFilterCollection -> Collection(PX.Commerce.Core.BCEntityImportFilter)
PX.Commerce.Core.BCEntitiesSyncStatistics.BCEntityImportMappingCollection -> Collection(PX.Commerce.Core.BCEntityImportMapping)
PX.Commerce.Core.BCEntitiesSyncStatistics.BCEntitiesSyncStatisticsCollection -> Collection(PX.Commerce.Core.BCEntitiesSyncStatistics)
PX.Commerce.Core.BCEntitiesSyncStatistics.BCEntityStatsCollection -> Collection(PX.Commerce.Core.BCEntityStats)

# PX.Commerce.Core.BCEntity (EntityType)

Label: "Sync Entity"
Key: BindingID, ConnectorType, EntityType
Entity sets: PX_Commerce_Core_BCEntity, SyncEntity, BCEntity
Non-filterable, non-selectable: IsFeatureEnabled, NoteText

PX.Commerce.Core.BCEntity.ConnectorType : Edm.String [key] "Connector"
PX.Commerce.Core.BCEntity.BindingID : Edm.Int32 [key] "Store"
PX.Commerce.Core.BCEntity.EntityType : Edm.String [key] "Entity"
PX.Commerce.Core.BCEntity.IsActive : Edm.Boolean [required] "Active"
PX.Commerce.Core.BCEntity.IsFeatureEnabled : Edm.Boolean
PX.Commerce.Core.BCEntity.Direction : Edm.String "Sync Direction"
PX.Commerce.Core.BCEntity.PrimarySystem : Edm.String "Primary System"
PX.Commerce.Core.BCEntity.AutoMergeDuplicates : Edm.Boolean "Merge Duplicate"
PX.Commerce.Core.BCEntity.ParallelProcessing : Edm.Boolean "Parallel Processing"
PX.Commerce.Core.BCEntity.MaxAttemptCount : Edm.Int32 "Max. Failed Attempts"
PX.Commerce.Core.BCEntity.SyncSortOrder : Edm.Int32 "Sync Order"
PX.Commerce.Core.BCEntity.RealTimeMode : Edm.String "Real-Time Mode"
PX.Commerce.Core.BCEntity.ExportRealTimeStatus : Edm.String "Real-Time Export"
PX.Commerce.Core.BCEntity.ImportRealTimeStatus : Edm.String "Real-Time Import"
PX.Commerce.Core.BCEntity.RealTimeStartDateTime : Edm.DateTimeOffset "Real-Time Start Date"
PX.Commerce.Core.BCEntity.RealTimeBaseURL : Edm.String "Real-Time Webhook URL"
PX.Commerce.Core.BCEntity.ImportMappingLineCntr : Edm.Int32 [required]
PX.Commerce.Core.BCEntity.ExportMappingLineCntr : Edm.Int32 [required]
PX.Commerce.Core.BCEntity.ImportFilterLineCntr : Edm.Int32 [required]
PX.Commerce.Core.BCEntity.ExportFilterLineCntr : Edm.Int32 [required]
PX.Commerce.Core.BCEntity.NoteID : Edm.Guid "NoteID"
PX.Commerce.Core.BCEntity.NoteText : Edm.String "Note Text"
PX.Commerce.Core.BCEntity.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Core.BCEntity.CreatedByScreenID : Edm.String
PX.Commerce.Core.BCEntity.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Commerce.Core.BCEntity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Core.BCEntity.LastModifiedByScreenID : Edm.String
PX.Commerce.Core.BCEntity.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Commerce.Core.BCEntity.Tstamp : Edm.Binary "Time Stamp"
PX.Commerce.Core.BCEntity.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (ConnectorType=ConnectorType, BindingID=BindingID)
PX.Commerce.Core.BCEntity.BCSyncStatusCollection -> Collection(PX.Commerce.Core.BCSyncStatus)
PX.Commerce.Core.BCEntity.BCEntityExportFilterCollection -> Collection(PX.Commerce.Core.BCEntityExportFilter)
PX.Commerce.Core.BCEntity.BCEntityExportMappingCollection -> Collection(PX.Commerce.Core.BCEntityExportMapping)
PX.Commerce.Core.BCEntity.BCEntityImportFilterCollection -> Collection(PX.Commerce.Core.BCEntityImportFilter)
PX.Commerce.Core.BCEntity.BCEntityImportMappingCollection -> Collection(PX.Commerce.Core.BCEntityImportMapping)
PX.Commerce.Core.BCEntity.BCEntitiesSyncStatisticsCollection -> Collection(PX.Commerce.Core.BCEntitiesSyncStatistics)
PX.Commerce.Core.BCEntity.BCEntityStatsCollection -> Collection(PX.Commerce.Core.BCEntityStats)

# PX.Commerce.Core.BCEntity2 (EntityType)

Label: "Sync Entity With Counts"
BaseType: PX.Commerce.Core.BCEntity
Key: BindingID, ConnectorType, EntityType (inherited from PX.Commerce.Core.BCEntity)
Entity sets: PX_Commerce_Core_BCEntity2, SyncEntityWithCounts, BCEntity2
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Commerce.Core.BCEntity2.TotalRecords : Edm.Int32 "Total Records"
PX.Commerce.Core.BCEntity2.PreparedRecords : Edm.Int32 "Ready to Process"
PX.Commerce.Core.BCEntity2.ProcessedRecords : Edm.Int32 "Processed Records"

# PX.Commerce.Core.BCEntityExportFilter (EntityType)

Label: "Entity Export Filter"
Key: BindingID, ConnectorType, EntityType, ExportFilterID
Entity sets: PX_Commerce_Core_BCEntityExportFilter, EntityExportFilter, BCEntityExportFilter
Non-filterable, non-selectable: NoteText

PX.Commerce.Core.BCEntityExportFilter.ConnectorType : Edm.String [key]
PX.Commerce.Core.BCEntityExportFilter.BindingID : Edm.Int32 [key]
PX.Commerce.Core.BCEntityExportFilter.EntityType : Edm.String [key]
PX.Commerce.Core.BCEntityExportFilter.ExportFilterID : Edm.Int32 [key]
PX.Commerce.Core.BCEntityExportFilter.SortOrder : Edm.Int32 "Line Nbr."
PX.Commerce.Core.BCEntityExportFilter.IsActive : Edm.Boolean [required] "Active"
PX.Commerce.Core.BCEntityExportFilter.OpenBrackets : Edm.Int32 [required] "Opening Brackets"
PX.Commerce.Core.BCEntityExportFilter.FieldName : Edm.String "Field Name"
PX.Commerce.Core.BCEntityExportFilter.Condition : Edm.Int32 [required] "Condition"
PX.Commerce.Core.BCEntityExportFilter.IsRelative : Edm.Boolean [required] "Is Relative"
PX.Commerce.Core.BCEntityExportFilter.Value : Edm.String "Value"
PX.Commerce.Core.BCEntityExportFilter.Value2 : Edm.String "Value 2"
PX.Commerce.Core.BCEntityExportFilter.CloseBrackets : Edm.Int32 [required] "Closing Brackets"
PX.Commerce.Core.BCEntityExportFilter.Operator : Edm.Int32 [required] "Operator"
PX.Commerce.Core.BCEntityExportFilter.NoteID : Edm.Guid
PX.Commerce.Core.BCEntityExportFilter.NoteText : Edm.String "Note Text"
PX.Commerce.Core.BCEntityExportFilter.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Core.BCEntityExportFilter.CreatedByScreenID : Edm.String
PX.Commerce.Core.BCEntityExportFilter.CreatedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCEntityExportFilter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Core.BCEntityExportFilter.LastModifiedByScreenID : Edm.String
PX.Commerce.Core.BCEntityExportFilter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCEntityExportFilter.TStamp : Edm.Binary
PX.Commerce.Core.BCEntityExportFilter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Core.BCEntityExportFilter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Core.BCEntityExportFilter.BCEntityByEntityType -> PX.Commerce.Core.BCEntity (ConnectorType=ConnectorType, BindingID=BindingID, EntityType=EntityType)

# PX.Commerce.Core.BCEntityExportMapping (EntityType)

Label: "Entity Export Mapping"
Key: BindingID, ConnectorType, EntityType, ExportMappingID
Entity sets: PX_Commerce_Core_BCEntityExportMapping, EntityExportMapping, BCEntityExportMapping
Non-filterable, non-selectable: NoteText

PX.Commerce.Core.BCEntityExportMapping.ConnectorType : Edm.String [key]
PX.Commerce.Core.BCEntityExportMapping.BindingID : Edm.Int32 [key]
PX.Commerce.Core.BCEntityExportMapping.EntityType : Edm.String [key]
PX.Commerce.Core.BCEntityExportMapping.ExportMappingID : Edm.Int32 [key]
PX.Commerce.Core.BCEntityExportMapping.SortOrder : Edm.Int32 "Line Nbr."
PX.Commerce.Core.BCEntityExportMapping.IsActive : Edm.Boolean [required] "Active"
PX.Commerce.Core.BCEntityExportMapping.TargetObject : Edm.String "External Object"
PX.Commerce.Core.BCEntityExportMapping.TargetField : Edm.String "External Field"
PX.Commerce.Core.BCEntityExportMapping.SourceObject : Edm.String "ERP Object"
PX.Commerce.Core.BCEntityExportMapping.SourceField : Edm.String "ERP Field / Value"
PX.Commerce.Core.BCEntityExportMapping.NoteID : Edm.Guid "NoteID"
PX.Commerce.Core.BCEntityExportMapping.NoteText : Edm.String "Note Text"
PX.Commerce.Core.BCEntityExportMapping.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Core.BCEntityExportMapping.CreatedByScreenID : Edm.String
PX.Commerce.Core.BCEntityExportMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCEntityExportMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Core.BCEntityExportMapping.LastModifiedByScreenID : Edm.String
PX.Commerce.Core.BCEntityExportMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCEntityExportMapping.Tstamp : Edm.Binary
PX.Commerce.Core.BCEntityExportMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Core.BCEntityExportMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Core.BCEntityExportMapping.BCEntityByEntityType -> PX.Commerce.Core.BCEntity (ConnectorType=ConnectorType, BindingID=BindingID, EntityType=EntityType)

# PX.Commerce.Core.BCEntityImportFilter (EntityType)

Label: "Entity Import Filter"
Key: BindingID, ConnectorType, EntityType, ImportFilterID
Entity sets: PX_Commerce_Core_BCEntityImportFilter, EntityImportFilter, BCEntityImportFilter
Non-filterable, non-selectable: NoteText

PX.Commerce.Core.BCEntityImportFilter.ConnectorType : Edm.String [key]
PX.Commerce.Core.BCEntityImportFilter.BindingID : Edm.Int32 [key]
PX.Commerce.Core.BCEntityImportFilter.EntityType : Edm.String [key]
PX.Commerce.Core.BCEntityImportFilter.ImportFilterID : Edm.Int32 [key]
PX.Commerce.Core.BCEntityImportFilter.SortOrder : Edm.Int32 "Line Nbr."
PX.Commerce.Core.BCEntityImportFilter.IsActive : Edm.Boolean [required] "Active"
PX.Commerce.Core.BCEntityImportFilter.OpenBrackets : Edm.Int32 [required] "Opening Brackets"
PX.Commerce.Core.BCEntityImportFilter.FieldName : Edm.String "Field Name"
PX.Commerce.Core.BCEntityImportFilter.Condition : Edm.Int32 [required] "Condition"
PX.Commerce.Core.BCEntityImportFilter.IsRelative : Edm.Boolean [required] "Is Relative"
PX.Commerce.Core.BCEntityImportFilter.Value : Edm.String "Value"
PX.Commerce.Core.BCEntityImportFilter.Value2 : Edm.String "Value 2"
PX.Commerce.Core.BCEntityImportFilter.CloseBrackets : Edm.Int32 [required] "Closing Brackets"
PX.Commerce.Core.BCEntityImportFilter.Operator : Edm.Int32 [required] "Operator"
PX.Commerce.Core.BCEntityImportFilter.NoteID : Edm.Guid
PX.Commerce.Core.BCEntityImportFilter.NoteText : Edm.String "Note Text"
PX.Commerce.Core.BCEntityImportFilter.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Core.BCEntityImportFilter.CreatedByScreenID : Edm.String
PX.Commerce.Core.BCEntityImportFilter.CreatedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCEntityImportFilter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Core.BCEntityImportFilter.LastModifiedByScreenID : Edm.String
PX.Commerce.Core.BCEntityImportFilter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCEntityImportFilter.TStamp : Edm.Binary
PX.Commerce.Core.BCEntityImportFilter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Core.BCEntityImportFilter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Core.BCEntityImportFilter.BCEntityByEntityType -> PX.Commerce.Core.BCEntity (ConnectorType=ConnectorType, BindingID=BindingID, EntityType=EntityType)

# PX.Commerce.Core.BCEntityImportMapping (EntityType)

Label: "Entity Import Mapping"
Key: BindingID, ConnectorType, EntityType, ImportMappingID
Entity sets: PX_Commerce_Core_BCEntityImportMapping, EntityImportMapping, BCEntityImportMapping
Non-filterable, non-selectable: NoteText

PX.Commerce.Core.BCEntityImportMapping.ConnectorType : Edm.String [key]
PX.Commerce.Core.BCEntityImportMapping.BindingID : Edm.Int32 [key]
PX.Commerce.Core.BCEntityImportMapping.EntityType : Edm.String [key]
PX.Commerce.Core.BCEntityImportMapping.ImportMappingID : Edm.Int32 [key]
PX.Commerce.Core.BCEntityImportMapping.SortOrder : Edm.Int32 "Line Nbr."
PX.Commerce.Core.BCEntityImportMapping.IsActive : Edm.Boolean [required] "Active"
PX.Commerce.Core.BCEntityImportMapping.TargetObject : Edm.String "ERP Object"
PX.Commerce.Core.BCEntityImportMapping.TargetField : Edm.String "ERP Field"
PX.Commerce.Core.BCEntityImportMapping.SourceObject : Edm.String "External Object"
PX.Commerce.Core.BCEntityImportMapping.SourceField : Edm.String "External Field / Value"
PX.Commerce.Core.BCEntityImportMapping.NoteID : Edm.Guid "NoteID"
PX.Commerce.Core.BCEntityImportMapping.NoteText : Edm.String "Note Text"
PX.Commerce.Core.BCEntityImportMapping.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Core.BCEntityImportMapping.CreatedByScreenID : Edm.String
PX.Commerce.Core.BCEntityImportMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCEntityImportMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Core.BCEntityImportMapping.LastModifiedByScreenID : Edm.String
PX.Commerce.Core.BCEntityImportMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCEntityImportMapping.Tstamp : Edm.Binary
PX.Commerce.Core.BCEntityImportMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Core.BCEntityImportMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Core.BCEntityImportMapping.BCEntityByEntityType -> PX.Commerce.Core.BCEntity (ConnectorType=ConnectorType, BindingID=BindingID, EntityType=EntityType)

# PX.Commerce.Core.BCEntityStats (EntityType)

Label: "Sync Entity Stats"
Key: BindingID, ConnectorType, EntityType
Entity sets: PX_Commerce_Core_BCEntityStats, SyncEntityStats, BCEntityStats

PX.Commerce.Core.BCEntityStats.ConnectorType : Edm.String [key] "Connector"
PX.Commerce.Core.BCEntityStats.BindingID : Edm.Int32 [key] "Binding"
PX.Commerce.Core.BCEntityStats.EntityType : Edm.String [key] "Entity"
PX.Commerce.Core.BCEntityStats.LastReconciliationImportDateTime : Edm.DateTimeOffset "Last Reconciliation Import"
PX.Commerce.Core.BCEntityStats.LastReconciliationExportDateTime : Edm.DateTimeOffset "Last Reconciliation Export"
PX.Commerce.Core.BCEntityStats.LastIncrementalImportDateTime : Edm.DateTimeOffset "Last Incremental Import"
PX.Commerce.Core.BCEntityStats.LastIncrementalExportDateTime : Edm.DateTimeOffset "Last Incremental Export"
PX.Commerce.Core.BCEntityStats.LastErrorMessage : Edm.String "Last Error"
PX.Commerce.Core.BCEntityStats.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (ConnectorType=ConnectorType, BindingID=BindingID)
PX.Commerce.Core.BCEntityStats.BCEntityByEntityType -> PX.Commerce.Core.BCEntity (ConnectorType=ConnectorType, BindingID=BindingID, EntityType=EntityType)

# PX.Commerce.Core.BCSyncDetail (EntityType)

Label: "Sync Status Details"
Key: DetailID
Entity sets: PX_Commerce_Core_BCSyncDetail, SyncStatusDetails, BCSyncDetail
Non-filterable, non-selectable: Source

PX.Commerce.Core.BCSyncDetail.SyncID : Edm.Int32 "Sync ID"
PX.Commerce.Core.BCSyncDetail.EntityType : Edm.String "Entity Type"
PX.Commerce.Core.BCSyncDetail.DetailID : Edm.Int32 [key] "Detail ID"
PX.Commerce.Core.BCSyncDetail.LocalID : Edm.Guid "Ref. Note ID"
PX.Commerce.Core.BCSyncDetail.Source : Edm.String "ERP ID"
PX.Commerce.Core.BCSyncDetail.ExternID : Edm.String "External ID"
PX.Commerce.Core.BCSyncDetail.RefNoteID : Edm.Guid "RefNoteID"
PX.Commerce.Core.BCSyncDetail.IsHidden : Edm.Boolean
PX.Commerce.Core.BCSyncDetail.BCSyncStatusBySyncID -> PX.Commerce.Core.BCSyncStatus (SyncID=SyncID)

# PX.Commerce.Core.BCSyncStatus (EntityType)

Label: "Sync History"
Key: SyncID
Entity sets: PX_Commerce_Core_BCSyncStatus, SyncHistory, BCSyncStatus
Non-filterable, non-selectable: Selectable, Source, NoteText

PX.Commerce.Core.BCSyncStatus.Selectable : Edm.Boolean
PX.Commerce.Core.BCSyncStatus.SyncID : Edm.Int32 [key] "Sync Record ID"
PX.Commerce.Core.BCSyncStatus.ConnectorType : Edm.String "Connector"
PX.Commerce.Core.BCSyncStatus.BindingID : Edm.Int32 "Store"
PX.Commerce.Core.BCSyncStatus.EntityType : Edm.String "Entity"
PX.Commerce.Core.BCSyncStatus.LocalID : Edm.Guid "Ref. Note ID"
PX.Commerce.Core.BCSyncStatus.Source : Edm.String "ERP ID"
PX.Commerce.Core.BCSyncStatus.LocalTS : Edm.DateTimeOffset "Last Locally Modified"
PX.Commerce.Core.BCSyncStatus.LocalCreatedTS : Edm.DateTimeOffset "Created Date (ERP)"
PX.Commerce.Core.BCSyncStatus.ExternID : Edm.String "External ID"
PX.Commerce.Core.BCSyncStatus.ExternDescription : Edm.String "External Description"
PX.Commerce.Core.BCSyncStatus.ExternTS : Edm.DateTimeOffset "Last Externally  Modified"
PX.Commerce.Core.BCSyncStatus.ExternCreatedTS : Edm.DateTimeOffset "Created Date (External)"
PX.Commerce.Core.BCSyncStatus.ExternHash : Edm.String "External Hash"
PX.Commerce.Core.BCSyncStatus.PendingSync : Edm.Boolean [required] "Ready to Process"
PX.Commerce.Core.BCSyncStatus.LastErrorMessage : Edm.String "Last Message"
PX.Commerce.Core.BCSyncStatus.LastOperation : Edm.String "Last Operation"
PX.Commerce.Core.BCSyncStatus.LastOperationTS : Edm.DateTimeOffset "Last Attempt"
PX.Commerce.Core.BCSyncStatus.Deleted : Edm.Boolean "Deleted"
PX.Commerce.Core.BCSyncStatus.SyncInProcess : Edm.Boolean "Sync in Process"
PX.Commerce.Core.BCSyncStatus.AttemptCount : Edm.Int32 "Attempts Count"
PX.Commerce.Core.BCSyncStatus.ParentSyncID : Edm.Int32 "Sync Record ID"
PX.Commerce.Core.BCSyncStatus.Status : Edm.String "Status"
PX.Commerce.Core.BCSyncStatus.SortOrder : Edm.Int32
PX.Commerce.Core.BCSyncStatus.NoteID : Edm.Guid
PX.Commerce.Core.BCSyncStatus.NoteText : Edm.String "Note Text"
PX.Commerce.Core.BCSyncStatus.Tstamp : Edm.Binary
PX.Commerce.Core.BCSyncStatus.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Core.BCSyncStatus.CreatedByScreenID : Edm.String
PX.Commerce.Core.BCSyncStatus.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Commerce.Core.BCSyncStatus.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Core.BCSyncStatus.LastModifiedByScreenID : Edm.String
PX.Commerce.Core.BCSyncStatus.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Commerce.Core.BCSyncStatus.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Core.BCSyncStatus.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Core.BCSyncStatus.BCBindingByConnectorType -> PX.Commerce.Core.BCBinding (BindingID=BindingID, ConnectorType=ConnectorType)
PX.Commerce.Core.BCSyncStatus.BCSyncStatusBySyncID -> PX.Commerce.Core.BCSyncStatus (SyncID=ParentSyncID)
PX.Commerce.Core.BCSyncStatus.BCEntityByEntityType -> PX.Commerce.Core.BCEntity (ConnectorType=ConnectorType, BindingID=BindingID, EntityType=EntityType)
PX.Commerce.Core.BCSyncStatus.BCSyncStatusCollection -> Collection(PX.Commerce.Core.BCSyncStatus)
PX.Commerce.Core.BCSyncStatus.BCMatrixOptionsMappingCollection -> Collection(PX.Commerce.Objects.BCMatrixOptionsMapping)
PX.Commerce.Core.BCSyncStatus.BCSyncDetailCollection -> Collection(PX.Commerce.Core.BCSyncDetail)

# PX.Commerce.Core.BCWebHook (EntityType)

Label: "Web Hooks"
Key: BindingID, ConnectorType, Scope
Entity sets: PX_Commerce_Core_BCWebHook, WebHooks, BCWebHook

PX.Commerce.Core.BCWebHook.ConnectorType : Edm.String [key] "Connector"
PX.Commerce.Core.BCWebHook.BindingID : Edm.Int32 [key] "Store"
PX.Commerce.Core.BCWebHook.Scope : Edm.String [key] "Scope"
PX.Commerce.Core.BCWebHook.Destination : Edm.String "Destination"
PX.Commerce.Core.BCWebHook.HookRef : Edm.Int64 "Webhook ID"
PX.Commerce.Core.BCWebHook.StoreHash : Edm.String "Store Hash"
PX.Commerce.Core.BCWebHook.ValidationHash : Edm.String "Validation Hash"
PX.Commerce.Core.BCWebHook.IsActive : Edm.Boolean [required] "Is Active"
PX.Commerce.Core.BCWebHook.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Core.BCWebHook.CreatedByScreenID : Edm.String
PX.Commerce.Core.BCWebHook.CreatedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCWebHook.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Core.BCWebHook.LastModifiedByScreenID : Edm.String
PX.Commerce.Core.BCWebHook.LastModifiedDateTime : Edm.DateTimeOffset
PX.Commerce.Core.BCWebHook.Tstamp : Edm.Binary
PX.Commerce.Core.BCWebHook.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Core.BCWebHook.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Core.BCWebHook.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (ConnectorType=ConnectorType, BindingID=BindingID)

# PX.Commerce.Core.DispatcherStatisticCommerceDetail (EntityType)

Label: "DispatcherStatisticCommerceDetail"
Key: Connector, Direction, Id
Entity sets: PX_Commerce_Core_DispatcherStatisticCommerceDetail, DispatcherStatisticCommerceDetail

PX.Commerce.Core.DispatcherStatisticCommerceDetail.Id : Edm.Guid [key] "ID"
PX.Commerce.Core.DispatcherStatisticCommerceDetail.Connector : Edm.String [key] "Connector"
PX.Commerce.Core.DispatcherStatisticCommerceDetail.Direction : Edm.String [key] "Direction"
PX.Commerce.Core.DispatcherStatisticCommerceDetail.Count : Edm.Int32 [required] "Messages"

# PX.Commerce.Objects.BCBindingExt (EntityType)

Label: "Store Settings"
Key: BindingID
Entity sets: PX_Commerce_Objects_BCBindingExt, StoreSettings, BCBindingExt

PX.Commerce.Objects.BCBindingExt.BindingID : Edm.Int32 [key] "Store"
PX.Commerce.Objects.BCBindingExt.DefaultStoreCurrency : Edm.String "Default Currency"
PX.Commerce.Objects.BCBindingExt.StoreTimeZone : Edm.String "Store Time Zone"
PX.Commerce.Objects.BCBindingExt.SupportedCurrencies : Edm.String "Supported Currencies"
PX.Commerce.Objects.BCBindingExt.CustomerNumberingID : Edm.String "Customer Numbering Sequence"
PX.Commerce.Objects.BCBindingExt.LocationNumberingID : Edm.String "Location Numbering Sequence"
PX.Commerce.Objects.BCBindingExt.InventoryNumberingID : Edm.String "Inventory Numbering Sequence"
PX.Commerce.Objects.BCBindingExt.CustomerTemplate : Edm.String "Customer Numbering Template"
PX.Commerce.Objects.BCBindingExt.LocationTemplate : Edm.String "Location Numbering Template"
PX.Commerce.Objects.BCBindingExt.InventoryTemplate : Edm.String "Inventory Numbering Template"
PX.Commerce.Objects.BCBindingExt.CustomerClassID : Edm.String "Customer Class"
PX.Commerce.Objects.BCBindingExt.GuestCustomerID : Edm.Int32 "Generic Guest Customer"
PX.Commerce.Objects.BCBindingExt.MultipleGuestAccounts : Edm.Boolean [required] "Use Multiple Guest Accounts"
PX.Commerce.Objects.BCBindingExt.StockItemClassID : Edm.Int32 "Item Class for Stock Items"
PX.Commerce.Objects.BCBindingExt.NonStockItemClassID : Edm.Int32 "Item Class for Non-Stock Items"
PX.Commerce.Objects.BCBindingExt.StockSalesCategoriesIDs : Edm.String "Default Stock Categories"
PX.Commerce.Objects.BCBindingExt.NonStockSalesCategoriesIDs : Edm.String "Default Non-Stock Categories"
PX.Commerce.Objects.BCBindingExt.RelatedItems : Edm.String "Related Items"
PX.Commerce.Objects.BCBindingExt.Visibility : Edm.String "Default Visibility"
PX.Commerce.Objects.BCBindingExt.ProductItemClassSubstitutionListID : Edm.String "Substitution List for Item Classes"
PX.Commerce.Objects.BCBindingExt.Availability : Edm.String "Default Availability"
PX.Commerce.Objects.BCBindingExt.NotAvailMode : Edm.String "When Qty Unavailable"
PX.Commerce.Objects.BCBindingExt.AvailabilityCalcRule : Edm.String "Availability Mode"
PX.Commerce.Objects.BCBindingExt.WarehouseMode : Edm.String "Warehouse Mode"
PX.Commerce.Objects.BCBindingExt.OrderType : Edm.String "Order Type for Import"
PX.Commerce.Objects.BCBindingExt.OtherSalesOrderTypes : Edm.String "Order Types for Export"
PX.Commerce.Objects.BCBindingExt.ReturnOrderType : Edm.String "Return Order Type"
PX.Commerce.Objects.BCBindingExt.OrderTimeZone : Edm.String "Order Time Zone"
PX.Commerce.Objects.BCBindingExt.GiftCertificateItemID : Edm.Int32 "Gift Certificate Item"
PX.Commerce.Objects.BCBindingExt.GiftWrappingItemID : Edm.Int32 "Gift Wrapping Item"
PX.Commerce.Objects.BCBindingExt.RefundAmountItemID : Edm.Int32 "Refund Amount Item"
PX.Commerce.Objects.BCBindingExt.ReasonCode : Edm.String "Refund Reason Code"
PX.Commerce.Objects.BCBindingExt.PostDiscounts : Edm.String "Show Discounts As"
PX.Commerce.Objects.BCBindingExt.ImportOrderRisks : Edm.Boolean [required] "Import Order Risks"
PX.Commerce.Objects.BCBindingExt.HoldOnRiskStatus : Edm.String "Hold on Risk Status"
PX.Commerce.Objects.BCBindingExt.SyncOrderNbrToStore : Edm.Boolean "Tag Ext. Order with ERP Order Nbr."
PX.Commerce.Objects.BCBindingExt.SyncOrdersFrom : Edm.DateTimeOffset "Earliest Order Date"
PX.Commerce.Objects.BCBindingExt.AllowOrderEdit : Edm.Boolean "Allow Adding Items to Processed Orders"
PX.Commerce.Objects.BCBindingExt.UsePaymentCurrencyForOrderImport : Edm.Boolean [required] "Use Payment Currency Instead of Store Currency"
PX.Commerce.Objects.BCBindingExt.TaxSynchronization : Edm.Boolean "Tax Synchronization"
PX.Commerce.Objects.BCBindingExt.DefaultTaxZoneID : Edm.String "Default Tax Zone"
PX.Commerce.Objects.BCBindingExt.UseAsPrimaryTaxZone : Edm.Boolean "Use as Primary Tax Zone"
PX.Commerce.Objects.BCBindingExt.TaxSubstitutionListID : Edm.String "Taxes"
PX.Commerce.Objects.BCBindingExt.TaxCategorySubstitutionListID : Edm.String "Tax Categories"
PX.Commerce.Objects.BCBindingExt.ShippingCarrierListID : Edm.String "Shipping Carriers"
PX.Commerce.Objects.BCBindingExt.PaymentTermsListID : Edm.String "Payment Terms"
PX.Commerce.Objects.BCBindingExt.tstamp : Edm.Binary
PX.Commerce.Objects.BCBindingExt.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Objects.BCBindingExt.CreatedByScreenID : Edm.String "Created At"
PX.Commerce.Objects.BCBindingExt.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Commerce.Objects.BCBindingExt.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Objects.BCBindingExt.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Commerce.Objects.BCBindingExt.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Commerce.Objects.BCBindingExt.CustomerByGuestCustomerID -> PX.Objects.AR.Customer (GuestCustomerID=BAccountID)
PX.Commerce.Objects.BCBindingExt.InventoryItemByGiftCertificateItemID -> PX.Objects.IN.InventoryItem (GiftCertificateItemID=InventoryID)
PX.Commerce.Objects.BCBindingExt.InventoryItemByGiftWrappingItemID -> PX.Objects.IN.InventoryItem (GiftWrappingItemID=InventoryID)
PX.Commerce.Objects.BCBindingExt.InventoryItemByRefundAmountItemID -> PX.Objects.IN.InventoryItem (RefundAmountItemID=InventoryID)
PX.Commerce.Objects.BCBindingExt.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Objects.BCBindingExt.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Objects.BCBindingExt.TaxZoneByDefaultTaxZoneID -> PX.Objects.TX.TaxZone (DefaultTaxZoneID=TaxZoneID)
PX.Commerce.Objects.BCBindingExt.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Commerce.Objects.BCBindingExt.SOOrderTypeByReturnorderType -> PX.Objects.SO.SOOrderType
PX.Commerce.Objects.BCBindingExt.NumberingByCustomerNumberingID -> PX.Objects.CS.Numbering (CustomerNumberingID=NumberingID)
PX.Commerce.Objects.BCBindingExt.NumberingByLocationNumberingID -> PX.Objects.CS.Numbering (LocationNumberingID=NumberingID)
PX.Commerce.Objects.BCBindingExt.NumberingByInventoryNumberingID -> PX.Objects.CS.Numbering (InventoryNumberingID=NumberingID)
PX.Commerce.Objects.BCBindingExt.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Commerce.Objects.BCBindingExt.INItemClassByNonStockItemClassID -> PX.Objects.IN.INItemClass (NonStockItemClassID=ItemClassID)
PX.Commerce.Objects.BCBindingExt.INItemClassByStockItemClassID -> PX.Objects.IN.INItemClass (StockItemClassID=ItemClassID)
PX.Commerce.Objects.BCBindingExt.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass (CustomerClassID=CustomerClassID)
PX.Commerce.Objects.BCBindingExt.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)
PX.Commerce.Objects.BCBindingExt.SYSubstitutionByProductItemClassSubstitutionListID -> PX.Api.SYSubstitution (ProductItemClassSubstitutionListID=SubstitutionID)
PX.Commerce.Objects.BCBindingExt.SYSubstitutionByTaxSubstitutionListID -> PX.Api.SYSubstitution (TaxSubstitutionListID=SubstitutionID)
PX.Commerce.Objects.BCBindingExt.SYSubstitutionByTaxCategorySubstitutionListID -> PX.Api.SYSubstitution (TaxCategorySubstitutionListID=SubstitutionID)
PX.Commerce.Objects.BCBindingExt.SYSubstitutionByShippingCarrierListID -> PX.Api.SYSubstitution (ShippingCarrierListID=SubstitutionID)
PX.Commerce.Objects.BCBindingExt.SYSubstitutionByPaymentTermsListID -> PX.Api.SYSubstitution (PaymentTermsListID=SubstitutionID)

# PX.Commerce.Objects.BCFeeMapping (EntityType)

Label: "BCFeeMapping"
Key: BindingID, FeeMappingID
Entity sets: PX_Commerce_Objects_BCFeeMapping, BCFeeMapping
Non-filterable, non-selectable: EntryDescription, TransactionType, DefaultOffsetAccount

PX.Commerce.Objects.BCFeeMapping.BindingID : Edm.Int32 [key]
PX.Commerce.Objects.BCFeeMapping.FeeMappingID : Edm.Int32 [key]
PX.Commerce.Objects.BCFeeMapping.PaymentMappingID : Edm.Int32
PX.Commerce.Objects.BCFeeMapping.FeeType : Edm.String "Fee Type"
PX.Commerce.Objects.BCFeeMapping.EntryTypeID : Edm.String "ERP Entry Type"
PX.Commerce.Objects.BCFeeMapping.EntryDescription : Edm.String "Entry Type Description"
PX.Commerce.Objects.BCFeeMapping.TransactionType : Edm.String "Transaction Type"
PX.Commerce.Objects.BCFeeMapping.DefaultOffsetAccount : Edm.Int32 "Default Offset Account"
PX.Commerce.Objects.BCFeeMapping.Active : Edm.Boolean [required] "Active"
PX.Commerce.Objects.BCFeeMapping.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Commerce.Objects.BCFeeMapping.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)
PX.Commerce.Objects.BCFeeMapping.BCPaymentMethodsByPaymentMappingID -> PX.Commerce.Objects.BCPaymentMethods (PaymentMappingID=PaymentMappingID)

# PX.Commerce.Objects.BCInventoryFileUrls (EntityType)

Label: "BC Inventory File Urls"
Key: FileID
Entity sets: PX_Commerce_Objects_BCInventoryFileUrls, BCInventoryFileUrls
Non-filterable, non-selectable: NoteText

PX.Commerce.Objects.BCInventoryFileUrls.FileID : Edm.Int32 [key]
PX.Commerce.Objects.BCInventoryFileUrls.InventoryID : Edm.Int32
PX.Commerce.Objects.BCInventoryFileUrls.FileURL : Edm.String "URL"
PX.Commerce.Objects.BCInventoryFileUrls.FileType : Edm.String "Type"
PX.Commerce.Objects.BCInventoryFileUrls.NoteID : Edm.Guid
PX.Commerce.Objects.BCInventoryFileUrls.NoteText : Edm.String "Note Text"
PX.Commerce.Objects.BCInventoryFileUrls.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)

# PX.Commerce.Objects.BCLocations (EntityType)

Label: "Locations"
Key: BCLocationsID
Entity sets: PX_Commerce_Objects_BCLocations, Locations, BCLocations

PX.Commerce.Objects.BCLocations.BCLocationsID : Edm.Int32 [key]
PX.Commerce.Objects.BCLocations.BindingID : Edm.Int32 "Store"
PX.Commerce.Objects.BCLocations.SiteID : Edm.Int32 "Warehouse"
PX.Commerce.Objects.BCLocations.LocationID : Edm.Int32 "Location ID"
PX.Commerce.Objects.BCLocations.ExternalLocationID : Edm.String "External Location ID"
PX.Commerce.Objects.BCLocations.MappingDirection : Edm.String "Mapping Direction"
PX.Commerce.Objects.BCLocations.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Commerce.Objects.BCLocations.INLocationBySiteID -> PX.Objects.IN.INLocation (LocationID=LocationID, SiteID=SiteID)
PX.Commerce.Objects.BCLocations.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Commerce.Objects.BCLocations.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)

# PX.Commerce.Objects.BCMatrixOptionsMapping (EntityType)

Label: "Matrix Options Mapping"
Key: OptionMappingID
Entity sets: PX_Commerce_Objects_BCMatrixOptionsMapping, MatrixOptionsMapping, BCMatrixOptionsMapping

PX.Commerce.Objects.BCMatrixOptionsMapping.OptionMappingID : Edm.Int32 [key]
PX.Commerce.Objects.BCMatrixOptionsMapping.SyncID : Edm.Int32 "Sync ID"
PX.Commerce.Objects.BCMatrixOptionsMapping.ExternID : Edm.String "External ID"
PX.Commerce.Objects.BCMatrixOptionsMapping.ItemClassID : Edm.Int32 "ERP Item Class"
PX.Commerce.Objects.BCMatrixOptionsMapping.ExternalOptionID : Edm.String
PX.Commerce.Objects.BCMatrixOptionsMapping.ExternalOptionSortOrder : Edm.Int32
PX.Commerce.Objects.BCMatrixOptionsMapping.ExternalOptionName : Edm.String "External Option"
PX.Commerce.Objects.BCMatrixOptionsMapping.ExternalOptionValue : Edm.String "External Option Value"
PX.Commerce.Objects.BCMatrixOptionsMapping.ExternalOptionValueID : Edm.String
PX.Commerce.Objects.BCMatrixOptionsMapping.MappedAttributeID : Edm.String "ERP Attribute"
PX.Commerce.Objects.BCMatrixOptionsMapping.MappedValue : Edm.String "ERP Attribute Value"
PX.Commerce.Objects.BCMatrixOptionsMapping.BindingID : Edm.Int32
PX.Commerce.Objects.BCMatrixOptionsMapping.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Objects.BCMatrixOptionsMapping.CreatedByScreenID : Edm.String
PX.Commerce.Objects.BCMatrixOptionsMapping.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Commerce.Objects.BCMatrixOptionsMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Objects.BCMatrixOptionsMapping.LastModifiedByScreenID : Edm.String
PX.Commerce.Objects.BCMatrixOptionsMapping.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Commerce.Objects.BCMatrixOptionsMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Objects.BCMatrixOptionsMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Objects.BCMatrixOptionsMapping.CSAttributeDetailByMappedValue -> PX.Objects.CS.CSAttributeDetail (MappedValue=ValueID)
PX.Commerce.Objects.BCMatrixOptionsMapping.CSAttributeGroupByMappedAttributeID -> PX.Objects.CS.CSAttributeGroup (MappedAttributeID=AttributeID)
PX.Commerce.Objects.BCMatrixOptionsMapping.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Commerce.Objects.BCMatrixOptionsMapping.BCSyncStatusBySyncID -> PX.Commerce.Core.BCSyncStatus (SyncID=SyncID)

# PX.Commerce.Objects.BCPaymentMethods (EntityType)

Label: "BCPaymentMethods"
Key: PaymentMappingID
Entity sets: PX_Commerce_Objects_BCPaymentMethods, BCPaymentMethods

PX.Commerce.Objects.BCPaymentMethods.BindingID : Edm.Int32 "Store"
PX.Commerce.Objects.BCPaymentMethods.PaymentMappingID : Edm.Int32 [key]
PX.Commerce.Objects.BCPaymentMethods.StorePaymentMethod : Edm.String "Store Payment Method"
PX.Commerce.Objects.BCPaymentMethods.StoreCurrency : Edm.String "Store Currency"
PX.Commerce.Objects.BCPaymentMethods.StoreOrderPaymentMethod : Edm.String "Store Order Payment Method"
PX.Commerce.Objects.BCPaymentMethods.PaymentMethodID : Edm.String "ERP Payment Method"
PX.Commerce.Objects.BCPaymentMethods.CashAccountID : Edm.Int32 "Cash Account"
PX.Commerce.Objects.BCPaymentMethods.ProcessingCenterID : Edm.String "Proc. Center ID"
PX.Commerce.Objects.BCPaymentMethods.ReleasePayments : Edm.Boolean [required] "Release Payments and Refunds"
PX.Commerce.Objects.BCPaymentMethods.Active : Edm.Boolean [required] "Active"
PX.Commerce.Objects.BCPaymentMethods.ProcessRefunds : Edm.Boolean [required] "Process Refunds"
PX.Commerce.Objects.BCPaymentMethods.CreatePaymentFromOrder : Edm.Boolean [required] "Create Payment from Order"
PX.Commerce.Objects.BCPaymentMethods.CurrencyByStoreCurrency -> PX.Objects.CM.Currency (StoreCurrency=CuryID)
PX.Commerce.Objects.BCPaymentMethods.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Commerce.Objects.BCPaymentMethods.CashAccountByStoreCurrency -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID, StoreCurrency=CuryID)
PX.Commerce.Objects.BCPaymentMethods.CCProcessingCenterByCashAccountID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Commerce.Objects.BCPaymentMethods.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Commerce.Objects.BCPaymentMethods.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)
PX.Commerce.Objects.BCPaymentMethods.BCFeeMappingCollection -> Collection(PX.Commerce.Objects.BCFeeMapping)

# PX.Commerce.Objects.BCPaymentTermsMapping (EntityType)

Label: "BCPaymentTermsMapping"
Key: BindingID, PaymentTermsMappingID
Entity sets: PX_Commerce_Objects_BCPaymentTermsMapping, BCPaymentTermsMapping

PX.Commerce.Objects.BCPaymentTermsMapping.BindingID : Edm.Int32 [key]
PX.Commerce.Objects.BCPaymentTermsMapping.PaymentTermsMappingID : Edm.Int32 [key]
PX.Commerce.Objects.BCPaymentTermsMapping.ExternPaymentTermsID : Edm.String "Payment Terms ID"
PX.Commerce.Objects.BCPaymentTermsMapping.PaymentTermsName : Edm.String "Payment Terms Name"
PX.Commerce.Objects.BCPaymentTermsMapping.PaymentTermsType : Edm.String "Payment Terms Type"
PX.Commerce.Objects.BCPaymentTermsMapping.TermsID : Edm.String "ERP Credit Terms"
PX.Commerce.Objects.BCPaymentTermsMapping.Active : Edm.Boolean [required]
PX.Commerce.Objects.BCPaymentTermsMapping.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Commerce.Objects.BCPaymentTermsMapping.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)

# PX.Commerce.Objects.BCShippingMappings (EntityType)

Label: "BCShippingMappings"
Key: ShippingMappingID
Entity sets: PX_Commerce_Objects_BCShippingMappings, BCShippingMappings

PX.Commerce.Objects.BCShippingMappings.ShippingMappingID : Edm.Int32 [key]
PX.Commerce.Objects.BCShippingMappings.BindingID : Edm.Int32 "Store"
PX.Commerce.Objects.BCShippingMappings.ShippingZone : Edm.String "Store Shipping Zone"
PX.Commerce.Objects.BCShippingMappings.ShippingMethod : Edm.String "Store Shipping Method"
PX.Commerce.Objects.BCShippingMappings.CarrierID : Edm.String "Ship Via"
PX.Commerce.Objects.BCShippingMappings.ZoneID : Edm.String "Shipping Zone"
PX.Commerce.Objects.BCShippingMappings.ShipTermsID : Edm.String "Shipping Terms"
PX.Commerce.Objects.BCShippingMappings.Active : Edm.Boolean [required] "Active"
PX.Commerce.Objects.BCShippingMappings.CarrierByCarrierID -> PX.Objects.CS.Carrier (CarrierID=CarrierID)
PX.Commerce.Objects.BCShippingMappings.ShippingZoneByZoneID -> PX.Objects.CS.ShippingZone (ZoneID=ZoneID)
PX.Commerce.Objects.BCShippingMappings.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Commerce.Objects.BCShippingMappings.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)
PX.Commerce.Objects.BCShippingMappings.BCBindingByZoneID -> PX.Commerce.Core.BCBinding (ZoneID=BindingID)

# PX.Commerce.Objects.ExportBCLocations (EntityType)

Label: "ExportLocations"
BaseType: PX.Commerce.Objects.BCLocations
Key: BCLocationsID (inherited from PX.Commerce.Objects.BCLocations)
Entity sets: PX_Commerce_Objects_ExportBCLocations, ExportLocations, ExportBCLocations

# PX.Commerce.Objects.ImportBCLocations (EntityType)

Label: "ImportLocations"
BaseType: PX.Commerce.Objects.BCLocations
Key: BCLocationsID (inherited from PX.Commerce.Objects.BCLocations)
Entity sets: PX_Commerce_Objects_ImportBCLocations, ImportLocations, ImportBCLocations

# PX.Commerce.Objects.SOOrderRisks (EntityType)

Label: "SO Order Risks"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Commerce_Objects_SOOrderRisks, SOOrderRisks
Non-filterable, non-selectable: NoteText

PX.Commerce.Objects.SOOrderRisks.OrderType : Edm.String [key]
PX.Commerce.Objects.SOOrderRisks.OrderNbr : Edm.String [key]
PX.Commerce.Objects.SOOrderRisks.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Commerce.Objects.SOOrderRisks.NoteID : Edm.Guid
PX.Commerce.Objects.SOOrderRisks.NoteText : Edm.String "Note Text"
PX.Commerce.Objects.SOOrderRisks.Recommendation : Edm.String "Risk Level"
PX.Commerce.Objects.SOOrderRisks.Message : Edm.String "Message"
PX.Commerce.Objects.SOOrderRisks.Score : Edm.Decimal "Score %"
PX.Commerce.Objects.SOOrderRisks.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)

# PX.Commerce.Shopify.BCBindingShopify (EntityType)

Label: "Shopify Settings"
Key: BindingID
Entity sets: PX_Commerce_Shopify_BCBindingShopify, ShopifySettings, BCBindingShopify
Non-filterable, non-selectable: ApiCallLimit, ShopifyApiVersion

PX.Commerce.Shopify.BCBindingShopify.BindingID : Edm.Int32 [key] "Store"
PX.Commerce.Shopify.BCBindingShopify.ShopifyApiBaseUrl : Edm.String "Store Admin URL"
PX.Commerce.Shopify.BCBindingShopify.ShopifyAccessToken : Edm.String "API Access Token"
PX.Commerce.Shopify.BCBindingShopify.StoreSharedSecret : Edm.String "API Secret Key"
PX.Commerce.Shopify.BCBindingShopify.ShopifyStoreUrl : Edm.String "Store URL"
PX.Commerce.Shopify.BCBindingShopify.ShopifyStorePlan : Edm.String "Store Plan"
PX.Commerce.Shopify.BCBindingShopify.ApiCallLimit : Edm.Int32
PX.Commerce.Shopify.BCBindingShopify.ApiDelaySeconds : Edm.Int32
PX.Commerce.Shopify.BCBindingShopify.ShopifyApiVersion : Edm.String "API Version"
PX.Commerce.Shopify.BCBindingShopify.ShopifyPOS : Edm.Boolean "Import POS Orders"
PX.Commerce.Shopify.BCBindingShopify.POSDirectOrderType : Edm.String "Order Type for Import"
PX.Commerce.Shopify.BCBindingShopify.POSShippingOrderType : Edm.String "Order Type for Import"
PX.Commerce.Shopify.BCBindingShopify.POSDirectExchangeOrderType : Edm.String "Order Type for Exchange"
PX.Commerce.Shopify.BCBindingShopify.POSShippingExchangeOrderType : Edm.String "Order Type for Exchange"
PX.Commerce.Shopify.BCBindingShopify.OnlineExchangeOrderType : Edm.String "Exchange Order Type"
PX.Commerce.Shopify.BCBindingShopify.ReturnFeesItemID : Edm.Int32 "Return Fee Item"
PX.Commerce.Shopify.BCBindingShopify.CombineCategoriesToTags : Edm.String "Sales Category Export"
PX.Commerce.Shopify.BCBindingShopify.MandatoryExportPaymentTerms : Edm.Boolean "Always Export Credit Terms"
PX.Commerce.Shopify.BCBindingShopify.UpdateTermsOnProcessedOrder : Edm.Boolean [required] "Update Terms on Processed Orders"
PX.Commerce.Shopify.BCBindingShopify.ImportCompanyContactsAsCustomers : Edm.Boolean [required] "Import Company Contacts as Customers"
PX.Commerce.Shopify.BCBindingShopify.tstamp : Edm.Binary
PX.Commerce.Shopify.BCBindingShopify.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Shopify.BCBindingShopify.CreatedByScreenID : Edm.String "Created At"
PX.Commerce.Shopify.BCBindingShopify.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Commerce.Shopify.BCBindingShopify.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Shopify.BCBindingShopify.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Commerce.Shopify.BCBindingShopify.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Commerce.Shopify.BCBindingShopify.QuoteOrderType : Edm.String "Quote Order Type for Import"
PX.Commerce.Shopify.BCBindingShopify.ExportQuoteOrderTypes : Edm.String "Quote Order Type for Export"
PX.Commerce.Shopify.BCBindingShopify.EarliestQuoteOrderDate : Edm.DateTimeOffset "Earliest Date for Quote Order Sync"
PX.Commerce.Shopify.BCBindingShopify.InventoryItemByReturnFeesItemID -> PX.Objects.IN.InventoryItem (ReturnFeesItemID=InventoryID)
PX.Commerce.Shopify.BCBindingShopify.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Commerce.Shopify.BCBindingShopify.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Commerce.Shopify.BCBindingShopify.SOOrderTypeByPOSDirectOrderType -> PX.Objects.SO.SOOrderType (POSDirectOrderType=OrderType)
PX.Commerce.Shopify.BCBindingShopify.SOOrderTypeByPOSShippingOrderType -> PX.Objects.SO.SOOrderType (POSShippingOrderType=OrderType)
PX.Commerce.Shopify.BCBindingShopify.SOOrderTypeByPOSDirectExchangeOrderType -> PX.Objects.SO.SOOrderType (POSDirectExchangeOrderType=OrderType)
PX.Commerce.Shopify.BCBindingShopify.SOOrderTypeByPOSShippingExchangeOrderType -> PX.Objects.SO.SOOrderType (POSShippingExchangeOrderType=OrderType)
PX.Commerce.Shopify.BCBindingShopify.SOOrderTypeByOnlineExchangeOrderType -> PX.Objects.SO.SOOrderType (OnlineExchangeOrderType=OrderType)
PX.Commerce.Shopify.BCBindingShopify.SOOrderTypeByQuoteOrderType -> PX.Objects.SO.SOOrderType (QuoteOrderType=OrderType)
PX.Commerce.Shopify.BCBindingShopify.BCBindingByBindingID -> PX.Commerce.Core.BCBinding (BindingID=BindingID)

# PX.Commerce.Shopify.BCRoleAssignment (EntityType)

Label: "Customer Contact Role Assignment"
Key: RoleAssignmentID
Entity sets: PX_Commerce_Shopify_BCRoleAssignment, CustomerContactRoleAssignment, BCRoleAssignment
Non-filterable, non-selectable: NoteText

PX.Commerce.Shopify.BCRoleAssignment.BAccountID : Edm.Int32
PX.Commerce.Shopify.BCRoleAssignment.RoleAssignmentID : Edm.Int32 [key]
PX.Commerce.Shopify.BCRoleAssignment.NoteID : Edm.Guid
PX.Commerce.Shopify.BCRoleAssignment.NoteText : Edm.String "Note Text"
PX.Commerce.Shopify.BCRoleAssignment.ContactID : Edm.Int32 "Contact"
PX.Commerce.Shopify.BCRoleAssignment.Role : Edm.String "Role"
PX.Commerce.Shopify.BCRoleAssignment.CreatedByID : Edm.Guid "Created By"
PX.Commerce.Shopify.BCRoleAssignment.CreatedByScreenID : Edm.String
PX.Commerce.Shopify.BCRoleAssignment.CreatedDateTime : Edm.DateTimeOffset
PX.Commerce.Shopify.BCRoleAssignment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Commerce.Shopify.BCRoleAssignment.LastModifiedByScreenID : Edm.String
PX.Commerce.Shopify.BCRoleAssignment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Commerce.Shopify.BCRoleAssignment.Tstamp : Edm.Binary
PX.Commerce.Shopify.BCRoleAssignment.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Commerce.Shopify.BCRoleAssignment.LocationByLocationID -> PX.Objects.CR.Location

# PX.CS.RMColumn (EntityType)

Label: "Column"
Key: ColumnCode, ColumnSetCode
Entity sets: PX_CS_RMColumn, Column, RMColumn
Non-filterable, non-selectable: Preview, NoteText, StyleIDText

PX.CS.RMColumn.ColumnSetCode : Edm.String [key] "ColumnSetCode"
PX.CS.RMColumn.ColumnCode : Edm.String [key] "Code"
PX.CS.RMColumn.Description : Edm.String "Description"
PX.CS.RMColumn.ColumnType : Edm.Int16 [required] "Type"
PX.CS.RMColumn.CellEvalOrder : Edm.Int16 [required] "Cell Evaluation Order"
PX.CS.RMColumn.CellFormatOrder : Edm.Int16 [required] "Cell Format Order"
PX.CS.RMColumn.Formula : Edm.String "Value"
PX.CS.RMColumn.Rounding : Edm.Int16 [required] "Rounding"
PX.CS.RMColumn.Format : Edm.String "Format"
PX.CS.RMColumn.Width : Edm.Int32 [required] "Width"
PX.CS.RMColumn.AutoHeight : Edm.Boolean [required] "Auto Height"
PX.CS.RMColumn.ExtraSpace : Edm.Int32 [required] "Extra Space"
PX.CS.RMColumn.SuppressEmpty : Edm.Boolean [required] "Suppress Empty"
PX.CS.RMColumn.HideZero : Edm.Boolean [required] "Hide Zero"
PX.CS.RMColumn.SuppressLine : Edm.Boolean [required] "Suppress Line"
PX.CS.RMColumn.GroupID : Edm.String "Printing Group"
PX.CS.RMColumn.UnitGroupID : Edm.String "Unit Group"
PX.CS.RMColumn.PrintControl : Edm.Int16 [required] "Printing Control"
PX.CS.RMColumn.VisibleFormula : Edm.String "Visible Formula"
PX.CS.RMColumn.PageBreak : Edm.Boolean [required] "Page Break"
PX.CS.RMColumn.StyleID : Edm.Int32 "Style"
PX.CS.RMColumn.DataSourceID : Edm.Int32 "Data Source"
PX.CS.RMColumn.Preview : Edm.String "Data Summary"
PX.CS.RMColumn.NoteID : Edm.Guid
PX.CS.RMColumn.NoteText : Edm.String "Note Text"
PX.CS.RMColumn.CreatedByID : Edm.Guid "CreatedByID"
PX.CS.RMColumn.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.CS.RMColumn.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.CS.RMColumn.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.CS.RMColumn.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.CS.RMColumn.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.CS.RMColumn.tstamp : Edm.Binary
PX.CS.RMColumn.StyleIDText : Edm.String
PX.CS.RMColumn.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CS.RMColumn.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CS.RMColumn.RMColumnSetByColumnSetCode -> PX.CS.RMColumnSet (ColumnSetCode=ColumnSetCode)
PX.CS.RMColumn.RMDataSourceByDataSourceID -> PX.CS.RMDataSource (DataSourceID=DataSourceID)

# PX.CS.RMColumnHeader (EntityType)

Key: ColumnCode, ColumnSetCode, HeaderNbr
Entity sets: PX_CS_RMColumnHeader
Non-filterable, non-selectable: IsRowSet, SectionType, NoteText

PX.CS.RMColumnHeader.ColumnSetCode : Edm.String [key] "ColumnSetCode"
PX.CS.RMColumnHeader.ColumnCode : Edm.String [key] "ColumnCode"
PX.CS.RMColumnHeader.HeaderNbr : Edm.Int16 [key] "HeaderNbr"
PX.CS.RMColumnHeader.Formula : Edm.String "Formula"
PX.CS.RMColumnHeader.StartColumn : Edm.String "Column Range"
PX.CS.RMColumnHeader.EndColumn : Edm.String "End Column"
PX.CS.RMColumnHeader.Height : Edm.Int32 [required] "Height"
PX.CS.RMColumnHeader.GroupID : Edm.String "Printing Group"
PX.CS.RMColumnHeader.StyleID : Edm.Int32 "StyleID"
PX.CS.RMColumnHeader.IsRowSet : Edm.Boolean
PX.CS.RMColumnHeader.SectionType : Edm.String "Section Type"
PX.CS.RMColumnHeader.NoteID : Edm.Guid
PX.CS.RMColumnHeader.NoteText : Edm.String "Note Text"
PX.CS.RMColumnHeader.CreatedByID : Edm.Guid "CreatedByID"
PX.CS.RMColumnHeader.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.CS.RMColumnHeader.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.CS.RMColumnHeader.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.CS.RMColumnHeader.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.CS.RMColumnHeader.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.CS.RMColumnHeader.tstamp : Edm.Binary
PX.CS.RMColumnHeader.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CS.RMColumnHeader.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CS.RMColumnHeader.RMColumnSetByColumnSetCode -> PX.CS.RMColumnSet (ColumnSetCode=ColumnSetCode)

# PX.CS.RMColumnSet (EntityType)

Label: "Column Set"
Key: ColumnSetCode
Entity sets: PX_CS_RMColumnSet, ColumnSet, RMColumnSet
Non-filterable, non-selectable: LastColumn, NoteText

PX.CS.RMColumnSet.ColumnSetCode : Edm.String [key] "Code"
PX.CS.RMColumnSet.Description : Edm.String "Description"
PX.CS.RMColumnSet.Type : Edm.String "Type"
PX.CS.RMColumnSet.LastColumn : Edm.String
PX.CS.RMColumnSet.HeaderCntr : Edm.Int16 [required]
PX.CS.RMColumnSet.NoteID : Edm.Guid
PX.CS.RMColumnSet.NoteText : Edm.String "Note Text"
PX.CS.RMColumnSet.CreatedByID : Edm.Guid "Created By"
PX.CS.RMColumnSet.CreatedByScreenID : Edm.String
PX.CS.RMColumnSet.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.CS.RMColumnSet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.CS.RMColumnSet.LastModifiedByScreenID : Edm.String
PX.CS.RMColumnSet.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.CS.RMColumnSet.tstamp : Edm.Binary
PX.CS.RMColumnSet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CS.RMColumnSet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CS.RMColumnSet.RMReportCollection -> Collection(PX.CS.RMReport)
PX.CS.RMColumnSet.RMColumnCollection -> Collection(PX.CS.RMColumn)
PX.CS.RMColumnSet.RMColumnHeaderCollection -> Collection(PX.CS.RMColumnHeader)

# PX.CS.RMDataSource (EntityType)

Label: "Data Source"
Key: DataSourceID
Entity sets: PX_CS_RMDataSource, DataSource, RMDataSource

PX.CS.RMDataSource.DataSourceID : Edm.Int32 [key] "DataSourceID"
PX.CS.RMDataSource.Expand : Edm.String "Expand"
PX.CS.RMDataSource.RowDescription : Edm.String "Row Description"
PX.CS.RMDataSource.AmountType : Edm.Int16 [required] "Amount Type"
PX.CS.RMDataSource.UseMasterCalendar : Edm.Boolean [required] "Use Master Calendar"
PX.CS.RMDataSource.LedgerID : Edm.Int32 "Ledger"
PX.CS.RMDataSource.StartAccount : Edm.String "Start Account"
PX.CS.RMDataSource.StartSub : Edm.String "Start Sub."
PX.CS.RMDataSource.StartPeriod : Edm.String "Start Period"
PX.CS.RMDataSource.EndPeriod : Edm.String "End Period"
PX.CS.RMDataSource.AccountClassID : Edm.String "Account Class"
PX.CS.RMDataSource.EndAccount : Edm.String "End Account"
PX.CS.RMDataSource.EndSub : Edm.String "End Sub."
PX.CS.RMDataSource.StartPeriodYearOffset : Edm.Int16 "Offset (Year, Period)"
PX.CS.RMDataSource.StartPeriodOffset : Edm.Int16
PX.CS.RMDataSource.EndPeriodYearOffset : Edm.Int16 "Offset (Year, Period)"
PX.CS.RMDataSource.EndPeriodOffset : Edm.Int16
PX.CS.RMDataSource.StartAccountGroup : Edm.String "Start Account Group"
PX.CS.RMDataSource.StartProject : Edm.String "Start Project"
PX.CS.RMDataSource.StartProjectTask : Edm.String "Start Task"
PX.CS.RMDataSource.StartInventory : Edm.String "Start Inventory"
PX.CS.RMDataSource.EndAccountGroup : Edm.String "End Account Group"
PX.CS.RMDataSource.EndProject : Edm.String "End Project"
PX.CS.RMDataSource.EndProjectTask : Edm.String "End Task"
PX.CS.RMDataSource.EndInventory : Edm.String "End Inventory"
PX.CS.RMDataSource.PMProjectByStartProject -> PX.Objects.PM.PMProject (StartProject=ContractCD)
PX.CS.RMDataSource.PMProjectByEndProject -> PX.Objects.PM.PMProject (EndProject=ContractCD)
PX.CS.RMDataSource.PMTaskByStartProjectTask -> PX.Objects.PM.PMTask (StartProjectTask=TaskCD)
PX.CS.RMDataSource.PMTaskByEndProjectTask -> PX.Objects.PM.PMTask (EndProjectTask=TaskCD)
PX.CS.RMDataSource.InventoryItemByStartInventory -> PX.Objects.IN.InventoryItem (StartInventory=InventoryCD)
PX.CS.RMDataSource.InventoryItemByEndInventory -> PX.Objects.IN.InventoryItem (EndInventory=InventoryCD)
PX.CS.RMDataSource.PMAccountGroupByStartAccountGroup -> PX.Objects.PM.PMAccountGroup (StartAccountGroup=GroupCD)
PX.CS.RMDataSource.PMAccountGroupByEndAccountGroup -> PX.Objects.PM.PMAccountGroup (EndAccountGroup=GroupCD)
PX.CS.RMDataSource.BranchByStartBranch -> PX.Objects.GL.Branch
PX.CS.RMDataSource.BranchByEndBranch -> PX.Objects.GL.Branch
PX.CS.RMDataSource.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization
PX.CS.RMDataSource.AccountByStartAccount -> PX.Objects.GL.Account (StartAccount=AccountCD)
PX.CS.RMDataSource.AccountByEndAccount -> PX.Objects.GL.Account (EndAccount=AccountCD)
PX.CS.RMDataSource.AccountClassByAccountClassID -> PX.Objects.GL.AccountClass (AccountClassID=AccountClassID)
PX.CS.RMDataSource.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.CS.RMDataSource.SubByStartSub -> PX.Objects.GL.Sub (StartSub=SubCD)
PX.CS.RMDataSource.SubByEndSub -> PX.Objects.GL.Sub (EndSub=SubCD)
PX.CS.RMDataSource.FinPeriodByStartPeriod -> PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod (StartPeriod=FinPeriodID)
PX.CS.RMDataSource.FinPeriodByEndPeriod -> PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod (EndPeriod=FinPeriodID)
PX.CS.RMDataSource.RMReportCollection -> Collection(PX.CS.RMReport)
PX.CS.RMDataSource.RMColumnCollection -> Collection(PX.CS.RMColumn)
PX.CS.RMDataSource.RMRowCollection -> Collection(PX.CS.RMRow)
PX.CS.RMDataSource.RMUnitCollection -> Collection(PX.CS.RMUnit)

# PX.CS.RMReport (EntityType)

Label: "Report"
Key: ReportCode
Entity sets: PX_CS_RMReport, Report, RMReport
Non-filterable, non-selectable: SitemapTitle, NoteText, SubCD, WorkspaceID, SubcategoryID

PX.CS.RMReport.ReportCode : Edm.String [key] "Code"
PX.CS.RMReport.Description : Edm.String "Description"
PX.CS.RMReport.ReportUID : Edm.Guid
PX.CS.RMReport.Type : Edm.String "Type"
PX.CS.RMReport.RowSetCode : Edm.String "Row Set"
PX.CS.RMReport.ColumnSetCode : Edm.String "Column Set"
PX.CS.RMReport.UnitSetCode : Edm.String "Unit Set"
PX.CS.RMReport.StartUnitCode : Edm.String "Start Unit"
PX.CS.RMReport.Landscape : Edm.Boolean [required] "Landscape"
PX.CS.RMReport.ApplyRestrictionGroups : Edm.Boolean [required] "Apply Restriction Groups"
PX.CS.RMReport.PaperKind : Edm.Int16 "Paper Kind"
PX.CS.RMReport.StyleID : Edm.Int32
PX.CS.RMReport.DataSourceID : Edm.Int32
PX.CS.RMReport.SitemapTitle : Edm.String "Title"
PX.CS.RMReport.MarginLeft : Edm.Double "Left"
PX.CS.RMReport.MarginLeftType : Edm.Int16 "Margin Left Type"
PX.CS.RMReport.MarginRight : Edm.Double "Right"
PX.CS.RMReport.MarginRightType : Edm.Int16 "Margin Right Type"
PX.CS.RMReport.MarginTop : Edm.Double "Top"
PX.CS.RMReport.MarginTopType : Edm.Int16 "Margin Top Type"
PX.CS.RMReport.MarginBottom : Edm.Double "Bottom"
PX.CS.RMReport.MarginBottomType : Edm.Int16 "Margin Bottom Type"
PX.CS.RMReport.Width : Edm.Double "Width"
PX.CS.RMReport.WidthType : Edm.Int16 "Width Type"
PX.CS.RMReport.Height : Edm.Double "Height"
PX.CS.RMReport.HeightType : Edm.Int16 "Height Type"
PX.CS.RMReport.NoteID : Edm.Guid
PX.CS.RMReport.NoteText : Edm.String "Note Text"
PX.CS.RMReport.CreatedByID : Edm.Guid "Created By"
PX.CS.RMReport.CreatedByScreenID : Edm.String
PX.CS.RMReport.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.CS.RMReport.LastModifiedByID : Edm.Guid "Last Modified By"
PX.CS.RMReport.LastModifiedByScreenID : Edm.String
PX.CS.RMReport.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.CS.RMReport.tstamp : Edm.Binary
PX.CS.RMReport.RequestOrganizationID : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestUseMasterCalendar : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestLedgerID : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestAccountClassID : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestStartAccount : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestEndAccount : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestStartSub : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestEndSub : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestStartBranch : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestEndBranch : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestStartAccountGroup : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestEndAccountGroup : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestStartProject : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestEndProject : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestStartProjectTask : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestEndProjectTask : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestStartInventory : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestEndInventory : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestStartPeriod : Edm.Boolean [required] "Request"
PX.CS.RMReport.RequestEndPeriod : Edm.Int16 [required] "Default"
PX.CS.RMReport.SubCD : Edm.String
PX.CS.RMReport.WorkspaceID : Edm.Guid "Workspace"
PX.CS.RMReport.SubcategoryID : Edm.Guid "Category"
PX.CS.RMReport.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CS.RMReport.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CS.RMReport.RMColumnSetByColumnSetCode -> PX.CS.RMColumnSet (ColumnSetCode=ColumnSetCode)
PX.CS.RMReport.RMColumnSetByType -> PX.CS.RMColumnSet (ColumnSetCode=ColumnSetCode, Type=Type)
PX.CS.RMReport.RMRowSetByRowSetCode -> PX.CS.RMRowSet (RowSetCode=RowSetCode)
PX.CS.RMReport.RMRowSetByType -> PX.CS.RMRowSet (RowSetCode=RowSetCode, Type=Type)
PX.CS.RMReport.RMUnitByUnitSetCode -> PX.CS.RMUnit (StartUnitCode=UnitCode, UnitSetCode=UnitSetCode)
PX.CS.RMReport.RMUnitSetByUnitSetCode -> PX.CS.RMUnitSet (UnitSetCode=UnitSetCode)
PX.CS.RMReport.RMUnitSetByType -> PX.CS.RMUnitSet (UnitSetCode=UnitSetCode, Type=Type)
PX.CS.RMReport.RMDataSourceByDataSourceID -> PX.CS.RMDataSource (DataSourceID=DataSourceID)

# PX.CS.RMRow (EntityType)

Label: "Row"
Key: RowNbr, RowSetCode
Entity sets: PX_CS_RMRow, Row, RMRow
Non-filterable, non-selectable: RowCodeRO, RMType, Preview, LineNbr, InCycle, DataVisible, DataSourceVisible, NoteText, StyleIDText

PX.CS.RMRow.RowSetCode : Edm.String [key]
PX.CS.RMRow.RowNbr : Edm.Int16 [key]
PX.CS.RMRow.RowCode : Edm.String "Code"
PX.CS.RMRow.RowCodeRO : Edm.String "Row"
PX.CS.RMRow.Description : Edm.String "Description"
PX.CS.RMRow.RowType : Edm.Int16 [required] "Type"
PX.CS.RMRow.Formula : Edm.String "Value"
PX.CS.RMRow.Format : Edm.String "Format"
PX.CS.RMRow.SuppressEmpty : Edm.Boolean [required] "Suppress Empty"
PX.CS.RMRow.HideZero : Edm.Boolean [required] "Hide Zero"
PX.CS.RMRow.Height : Edm.Int32 [required] "Height"
PX.CS.RMRow.Indent : Edm.Int32 [required] "Indent"
PX.CS.RMRow.LineStyle : Edm.Int16 [required] "Line Style"
PX.CS.RMRow.LinkedRowCode : Edm.String "Linked Row"
PX.CS.RMRow.BaseRowCode : Edm.String "Base Row"
PX.CS.RMRow.ColumnGroupID : Edm.String "Column Group"
PX.CS.RMRow.UnitGroupID : Edm.String "Unit Group"
PX.CS.RMRow.PrintControl : Edm.Int16 [required] "Printing Control"
PX.CS.RMRow.PageBreak : Edm.Boolean [required] "Page Break"
PX.CS.RMRow.StyleID : Edm.Int32 "Style"
PX.CS.RMRow.DataSourceID : Edm.Int32 "Data Source"
PX.CS.RMRow.RMType : Edm.String "RMType"
PX.CS.RMRow.Preview : Edm.String "Data Summary"
PX.CS.RMRow.LineNbr : Edm.Int32
PX.CS.RMRow.InCycle : Edm.Boolean
PX.CS.RMRow.DataVisible : Edm.Boolean
PX.CS.RMRow.DataSourceVisible : Edm.Boolean
PX.CS.RMRow.NoteID : Edm.Guid
PX.CS.RMRow.NoteText : Edm.String "Note Text"
PX.CS.RMRow.CreatedByID : Edm.Guid "Created By"
PX.CS.RMRow.CreatedByScreenID : Edm.String
PX.CS.RMRow.CreatedDateTime : Edm.DateTimeOffset
PX.CS.RMRow.LastModifiedByID : Edm.Guid "Last Modified By"
PX.CS.RMRow.LastModifiedByScreenID : Edm.String
PX.CS.RMRow.LastModifiedDateTime : Edm.DateTimeOffset
PX.CS.RMRow.tstamp : Edm.Binary
PX.CS.RMRow.StyleIDText : Edm.String
PX.CS.RMRow.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CS.RMRow.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CS.RMRow.RMRowSetByRowSetCode -> PX.CS.RMRowSet (RowSetCode=RowSetCode)
PX.CS.RMRow.RMDataSourceByDataSourceID -> PX.CS.RMDataSource (DataSourceID=DataSourceID)

# PX.CS.RMRowSet (EntityType)

Label: "Row Set"
Key: RowSetCode
Entity sets: PX_CS_RMRowSet, RowSet, RMRowSet
Non-filterable, non-selectable: NoteText

PX.CS.RMRowSet.RowSetCode : Edm.String [key] "Code"
PX.CS.RMRowSet.Description : Edm.String "Description"
PX.CS.RMRowSet.Type : Edm.String "Type"
PX.CS.RMRowSet.RowCntr : Edm.Int16 [required]
PX.CS.RMRowSet.NoteID : Edm.Guid
PX.CS.RMRowSet.NoteText : Edm.String "Note Text"
PX.CS.RMRowSet.CreatedByID : Edm.Guid "Created By"
PX.CS.RMRowSet.CreatedByScreenID : Edm.String
PX.CS.RMRowSet.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.CS.RMRowSet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.CS.RMRowSet.LastModifiedByScreenID : Edm.String
PX.CS.RMRowSet.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.CS.RMRowSet.tstamp : Edm.Binary
PX.CS.RMRowSet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CS.RMRowSet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CS.RMRowSet.RMReportCollection -> Collection(PX.CS.RMReport)
PX.CS.RMRowSet.RMRowCollection -> Collection(PX.CS.RMRow)

# PX.CS.RMStyle (EntityType)

Label: "Style"
Key: StyleID
Entity sets: PX_CS_RMStyle, Style, RMStyle
Non-filterable, non-selectable: ColorRGBA, ColorRGB, BackColorRGBA, BackColorRGB, Bold, Italic, Underline, Strikeout, StyleIDText

PX.CS.RMStyle.StyleID : Edm.Int32 [key] "StyleID"
PX.CS.RMStyle.Color : Edm.String "Color"
PX.CS.RMStyle.BackColor : Edm.String "Backgr. Color"
PX.CS.RMStyle.ColorRGBA : Edm.String "Color"
PX.CS.RMStyle.ColorRGB : Edm.String "Color"
PX.CS.RMStyle.BackColorRGBA : Edm.String "Backgr. Color"
PX.CS.RMStyle.BackColorRGB : Edm.String "Backgr. Color"
PX.CS.RMStyle.Bold : Edm.Boolean "Bold"
PX.CS.RMStyle.Italic : Edm.Boolean "Italic"
PX.CS.RMStyle.Underline : Edm.Boolean "Underline"
PX.CS.RMStyle.Strikeout : Edm.Boolean "Strikethrough"
PX.CS.RMStyle.TextAlign : Edm.Int16 "Text Align"
PX.CS.RMStyle.FontName : Edm.String "Font"
PX.CS.RMStyle.FontSize : Edm.Double "Font Size"
PX.CS.RMStyle.FontSizeType : Edm.Int16 "Size Type"
PX.CS.RMStyle.FontStyle : Edm.Int16 "Font Style"
PX.CS.RMStyle.StyleIDText : Edm.String

# PX.CS.RMUnit (EntityType)

Label: "Unit"
Key: UnitCode, UnitSetCode
Entity sets: PX_CS_RMUnit, Unit, RMUnit
Non-filterable, non-selectable: TreeNodeID, CodeAndDescription, NoteText

PX.CS.RMUnit.UnitSetCode : Edm.String [key] "Unit Set"
PX.CS.RMUnit.UnitCode : Edm.String [key] "Code"
PX.CS.RMUnit.TreeNodeID : Edm.String
PX.CS.RMUnit.CodeAndDescription : Edm.String
PX.CS.RMUnit.ParentCode : Edm.String "ParentCode"
PX.CS.RMUnit.Description : Edm.String "Description"
PX.CS.RMUnit.Formula : Edm.String "Value"
PX.CS.RMUnit.GroupID : Edm.String "Printing Group"
PX.CS.RMUnit.DataSourceID : Edm.Int32 "Data Source"
PX.CS.RMUnit.NoteID : Edm.Guid
PX.CS.RMUnit.NoteText : Edm.String "Note Text"
PX.CS.RMUnit.CreatedByID : Edm.Guid "Created By"
PX.CS.RMUnit.CreatedByScreenID : Edm.String
PX.CS.RMUnit.CreatedDateTime : Edm.DateTimeOffset
PX.CS.RMUnit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.CS.RMUnit.LastModifiedByScreenID : Edm.String
PX.CS.RMUnit.LastModifiedDateTime : Edm.DateTimeOffset
PX.CS.RMUnit.tstamp : Edm.Binary
PX.CS.RMUnit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CS.RMUnit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CS.RMUnit.RMUnitSetByUnitSetCode -> PX.CS.RMUnitSet (UnitSetCode=UnitSetCode)
PX.CS.RMUnit.RMUnitSetByParentCode -> PX.CS.RMUnitSet (ParentCode=UnitSetCode)
PX.CS.RMUnit.RMDataSourceByDataSourceID -> PX.CS.RMDataSource (DataSourceID=DataSourceID)
PX.CS.RMUnit.RMReportCollection -> Collection(PX.CS.RMReport)

# PX.CS.RMUnitSet (EntityType)

Label: "Unit Set"
Key: UnitSetCode
Entity sets: PX_CS_RMUnitSet, UnitSet, RMUnitSet
Non-filterable, non-selectable: NoteText

PX.CS.RMUnitSet.UnitSetCode : Edm.String [key] "Code"
PX.CS.RMUnitSet.Description : Edm.String "Description"
PX.CS.RMUnitSet.Type : Edm.String "Type"
PX.CS.RMUnitSet.NoteID : Edm.Guid
PX.CS.RMUnitSet.NoteText : Edm.String "Note Text"
PX.CS.RMUnitSet.CreatedByID : Edm.Guid "Created By"
PX.CS.RMUnitSet.CreatedByScreenID : Edm.String
PX.CS.RMUnitSet.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.CS.RMUnitSet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.CS.RMUnitSet.LastModifiedByScreenID : Edm.String
PX.CS.RMUnitSet.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.CS.RMUnitSet.tstamp : Edm.Binary
PX.CS.RMUnitSet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.CS.RMUnitSet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.CS.RMUnitSet.RMReportCollection -> Collection(PX.CS.RMReport)
PX.CS.RMUnitSet.RMUnitCollection -> Collection(PX.CS.RMUnit)

# PX.Dashboards.DAC.Dashboard (EntityType)

Label: "Dashboard"
Key: Name
Entity sets: PX_Dashboards_DAC_Dashboard, Dashboard
Non-filterable, non-selectable: SitemapTitle, NoteText, WorkspaceID, SubcategoryID

PX.Dashboards.DAC.Dashboard.DashboardID : Edm.Int32 "Dashboard ID"
PX.Dashboards.DAC.Dashboard.Name : Edm.String [key] "Name"
PX.Dashboards.DAC.Dashboard.SitemapTitle : Edm.String "Site Map Title"
PX.Dashboards.DAC.Dashboard.ScreenID : Edm.String "Site Map Location"
PX.Dashboards.DAC.Dashboard.NoteID : Edm.Guid
PX.Dashboards.DAC.Dashboard.NoteText : Edm.String "Note Text"
PX.Dashboards.DAC.Dashboard.DefaultOwnerRole : Edm.String "Owner Role"
PX.Dashboards.DAC.Dashboard.AllowCopy : Edm.Boolean [required] "Allow Users to Personalize"
PX.Dashboards.DAC.Dashboard.Workspace1Size : Edm.Int32 [required]
PX.Dashboards.DAC.Dashboard.Workspace2Size : Edm.Int32 [required]
PX.Dashboards.DAC.Dashboard.IsPortal : Edm.Boolean
PX.Dashboards.DAC.Dashboard.ExposeViaMobile : Edm.Boolean [required] "Expose to the Mobile Application"
PX.Dashboards.DAC.Dashboard.CreatedByID : Edm.Guid "Created By"
PX.Dashboards.DAC.Dashboard.CreatedByScreenID : Edm.String
PX.Dashboards.DAC.Dashboard.CreatedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.Dashboard.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Dashboards.DAC.Dashboard.LastModifiedByScreenID : Edm.String
PX.Dashboards.DAC.Dashboard.LastModifiedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.Dashboard.WorkspaceID : Edm.Guid "Workspace"
PX.Dashboards.DAC.Dashboard.SubcategoryID : Edm.Guid "Category"
PX.Dashboards.DAC.Dashboard.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Dashboards.DAC.Dashboard.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Dashboards.DAC.Dashboard.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Dashboards.DAC.Dashboard.RolesByDefaultOwnerRole -> PX.SM.Roles (DefaultOwnerRole=Rolename)
PX.Dashboards.DAC.Dashboard.DashboardParameterCollection -> Collection(PX.Dashboards.DAC.DashboardParameter)
PX.Dashboards.DAC.Dashboard.WidgetCollection -> Collection(PX.Dashboards.DAC.Widget)

# PX.Dashboards.DAC.DashboardParameter (EntityType)

Label: "Dashboard Parameter"
Key: DashboardID, LineNbr
Entity sets: PX_Dashboards_DAC_DashboardParameter, DashboardParameter
Non-filterable, non-selectable: NoteText

PX.Dashboards.DAC.DashboardParameter.DashboardID : Edm.Int32 [key]
PX.Dashboards.DAC.DashboardParameter.LineNbr : Edm.Int32 [key]
PX.Dashboards.DAC.DashboardParameter.Name : Edm.String "Name"
PX.Dashboards.DAC.DashboardParameter.IsActive : Edm.Boolean [required] "Active"
PX.Dashboards.DAC.DashboardParameter.Required : Edm.Boolean [required] "Is Required"
PX.Dashboards.DAC.DashboardParameter.ObjectName : Edm.String "Schema Object"
PX.Dashboards.DAC.DashboardParameter.FieldName : Edm.String "Schema Field"
PX.Dashboards.DAC.DashboardParameter.DisplayName : Edm.String "Display Name"
PX.Dashboards.DAC.DashboardParameter.IsExpression : Edm.Boolean [required] "From Schema"
PX.Dashboards.DAC.DashboardParameter.DefaultValue : Edm.String "Default Value"
PX.Dashboards.DAC.DashboardParameter.Size : Edm.String "Control Size"
PX.Dashboards.DAC.DashboardParameter.LabelSize : Edm.String "Label Size"
PX.Dashboards.DAC.DashboardParameter.ColSpan : Edm.Int32 [required] "Column Span"
PX.Dashboards.DAC.DashboardParameter.NoteID : Edm.Guid
PX.Dashboards.DAC.DashboardParameter.NoteText : Edm.String "Note Text"
PX.Dashboards.DAC.DashboardParameter.CreatedByID : Edm.Guid "Created By"
PX.Dashboards.DAC.DashboardParameter.CreatedByScreenID : Edm.String
PX.Dashboards.DAC.DashboardParameter.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Dashboards.DAC.DashboardParameter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Dashboards.DAC.DashboardParameter.LastModifiedByScreenID : Edm.String
PX.Dashboards.DAC.DashboardParameter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.DashboardParameter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Dashboards.DAC.DashboardParameter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Dashboards.DAC.DashboardParameter.DashboardByDashboardID -> PX.Dashboards.DAC.Dashboard (DashboardID=DashboardID)

# PX.Dashboards.DAC.DashboardParameterV2 (EntityType)

Label: "Dashboard Parameter"
Key: DashboardID, LineNbr
Entity sets: PX_Dashboards_DAC_DashboardParameterV2, DashboardParameter1, DashboardParameterV2
Non-filterable, non-selectable: NoteText

PX.Dashboards.DAC.DashboardParameterV2.DashboardID : Edm.Guid [key]
PX.Dashboards.DAC.DashboardParameterV2.LineNbr : Edm.Int32 [key]
PX.Dashboards.DAC.DashboardParameterV2.Name : Edm.String "Name"
PX.Dashboards.DAC.DashboardParameterV2.IsActive : Edm.Boolean [required] "Active"
PX.Dashboards.DAC.DashboardParameterV2.Required : Edm.Boolean [required] "Is Required"
PX.Dashboards.DAC.DashboardParameterV2.ObjectName : Edm.String "Schema Object"
PX.Dashboards.DAC.DashboardParameterV2.FieldName : Edm.String "Schema Field"
PX.Dashboards.DAC.DashboardParameterV2.DisplayName : Edm.String "Display Name"
PX.Dashboards.DAC.DashboardParameterV2.NoteID : Edm.Guid
PX.Dashboards.DAC.DashboardParameterV2.NoteText : Edm.String "Note Text"
PX.Dashboards.DAC.DashboardParameterV2.CreatedByID : Edm.Guid "Created By"
PX.Dashboards.DAC.DashboardParameterV2.CreatedByScreenID : Edm.String
PX.Dashboards.DAC.DashboardParameterV2.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Dashboards.DAC.DashboardParameterV2.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Dashboards.DAC.DashboardParameterV2.LastModifiedByScreenID : Edm.String
PX.Dashboards.DAC.DashboardParameterV2.LastModifiedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.DashboardParameterV2.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Dashboards.DAC.DashboardParameterV2.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Dashboards.DAC.DashboardParameterV2.DashboardV2ByDashboardID -> PX.Dashboards.DAC.DashboardV2 (DashboardID=DashboardID)

# PX.Dashboards.DAC.DashboardV2 (EntityType)

Label: "Dashboard"
Key: Name
Entity sets: PX_Dashboards_DAC_DashboardV2, Dashboard1, DashboardV2
Non-filterable, non-selectable: SitemapTitle, ScreenID, NoteText, WorkspaceID, SubcategoryID

PX.Dashboards.DAC.DashboardV2.DashboardID : Edm.Guid "Dashboard ID"
PX.Dashboards.DAC.DashboardV2.Name : Edm.String [key] "Name"
PX.Dashboards.DAC.DashboardV2.SitemapTitle : Edm.String "Site Map Title"
PX.Dashboards.DAC.DashboardV2.ScreenID : Edm.String "Site Map Location"
PX.Dashboards.DAC.DashboardV2.NoteID : Edm.Guid
PX.Dashboards.DAC.DashboardV2.NoteText : Edm.String "Note Text"
PX.Dashboards.DAC.DashboardV2.DefaultOwnerRole : Edm.String "Owner Role"
PX.Dashboards.DAC.DashboardV2.AllowCopy : Edm.Boolean [required] "Allow Users to Personalize"
PX.Dashboards.DAC.DashboardV2.ExposeViaMobile : Edm.Boolean [required] "Expose to the Mobile Application"
PX.Dashboards.DAC.DashboardV2.CreatedByID : Edm.Guid "Created By"
PX.Dashboards.DAC.DashboardV2.CreatedByScreenID : Edm.String
PX.Dashboards.DAC.DashboardV2.CreatedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.DashboardV2.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Dashboards.DAC.DashboardV2.LastModifiedByScreenID : Edm.String
PX.Dashboards.DAC.DashboardV2.LastModifiedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.DashboardV2.WorkspaceID : Edm.Guid "Workspace"
PX.Dashboards.DAC.DashboardV2.SubcategoryID : Edm.Guid "Category"
PX.Dashboards.DAC.DashboardV2.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Dashboards.DAC.DashboardV2.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Dashboards.DAC.DashboardV2.RolesByDefaultOwnerRole -> PX.SM.Roles (DefaultOwnerRole=Rolename)
PX.Dashboards.DAC.DashboardV2.DashboardParameterV2Collection -> Collection(PX.Dashboards.DAC.DashboardParameterV2)
PX.Dashboards.DAC.DashboardV2.WidgetParameterV2Collection -> Collection(PX.Dashboards.DAC.WidgetParameterV2)
PX.Dashboards.DAC.DashboardV2.WidgetV2Collection -> Collection(PX.Dashboards.DAC.WidgetV2)

# PX.Dashboards.DAC.Widget (EntityType)

Label: "Widget"
Key: DashboardID, WidgetID
Entity sets: PX_Dashboards_DAC_Widget, Widget
Non-filterable, non-selectable: IsMasterCopy, NoteText, WidgetName, SourceSetting

PX.Dashboards.DAC.Widget.DashboardID : Edm.Int32 [key]
PX.Dashboards.DAC.Widget.WidgetID : Edm.Int32 [key]
PX.Dashboards.DAC.Widget.OwnerName : Edm.String "Owner Name"
PX.Dashboards.DAC.Widget.Caption : Edm.String "Caption"
PX.Dashboards.DAC.Widget.Column : Edm.Int32 "Column"
PX.Dashboards.DAC.Widget.Row : Edm.Int32 "Row"
PX.Dashboards.DAC.Widget.Workspace : Edm.Int32 [required] "Workspace"
PX.Dashboards.DAC.Widget.Width : Edm.Int32 "Width"
PX.Dashboards.DAC.Widget.Height : Edm.Int32 "Height"
PX.Dashboards.DAC.Widget.Type : Edm.String "Widget Class"
PX.Dashboards.DAC.Widget.Settings : Edm.String "Settings"
PX.Dashboards.DAC.Widget.IsMasterCopy : Edm.Boolean
PX.Dashboards.DAC.Widget.CreatedByID : Edm.Guid "Created By"
PX.Dashboards.DAC.Widget.CreatedByScreenID : Edm.String
PX.Dashboards.DAC.Widget.CreatedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.Widget.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Dashboards.DAC.Widget.LastModifiedByScreenID : Edm.String
PX.Dashboards.DAC.Widget.LastModifiedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.Widget.NoteID : Edm.Guid
PX.Dashboards.DAC.Widget.NoteText : Edm.String "Note Text"
PX.Dashboards.DAC.Widget.IsActive : Edm.Boolean [required] "Active"
PX.Dashboards.DAC.Widget.WidgetName : Edm.String "Widget Type"
PX.Dashboards.DAC.Widget.SourceSetting : Edm.String "Source"
PX.Dashboards.DAC.Widget.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Dashboards.DAC.Widget.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Dashboards.DAC.Widget.UsersByOwnerName -> PX.SM.Users (OwnerName=Username)
PX.Dashboards.DAC.Widget.DashboardByDashboardID -> PX.Dashboards.DAC.Dashboard (DashboardID=DashboardID)

# PX.Dashboards.DAC.WidgetParameterV2 (EntityType)

Key: DashboardID, DashboardParameterName, WidgetID
Entity sets: PX_Dashboards_DAC_WidgetParameterV2
Non-filterable, non-selectable: NoteText

PX.Dashboards.DAC.WidgetParameterV2.DashboardID : Edm.Guid [key]
PX.Dashboards.DAC.WidgetParameterV2.WidgetID : Edm.Guid [key]
PX.Dashboards.DAC.WidgetParameterV2.DashboardParameterName : Edm.String [key] "Dashboard"
PX.Dashboards.DAC.WidgetParameterV2.WidgetParameterName : Edm.String "Widget"
PX.Dashboards.DAC.WidgetParameterV2.NoteID : Edm.Guid
PX.Dashboards.DAC.WidgetParameterV2.NoteText : Edm.String "Note Text"
PX.Dashboards.DAC.WidgetParameterV2.CreatedByID : Edm.Guid "Created By"
PX.Dashboards.DAC.WidgetParameterV2.CreatedByScreenID : Edm.String
PX.Dashboards.DAC.WidgetParameterV2.CreatedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.WidgetParameterV2.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Dashboards.DAC.WidgetParameterV2.LastModifiedByScreenID : Edm.String
PX.Dashboards.DAC.WidgetParameterV2.LastModifiedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.WidgetParameterV2.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Dashboards.DAC.WidgetParameterV2.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Dashboards.DAC.WidgetParameterV2.DashboardV2ByDashboardID -> PX.Dashboards.DAC.DashboardV2 (DashboardID=DashboardID)
PX.Dashboards.DAC.WidgetParameterV2.WidgetV2ByWidgetID -> PX.Dashboards.DAC.WidgetV2 (DashboardID=DashboardID, WidgetID=WidgetID)

# PX.Dashboards.DAC.WidgetV2 (EntityType)

Label: "Widget"
Key: DashboardID, WidgetID
Entity sets: PX_Dashboards_DAC_WidgetV2, Widget1, WidgetV2
Non-filterable, non-selectable: IsMasterCopy, NoteText, WidgetType, Source

PX.Dashboards.DAC.WidgetV2.DashboardID : Edm.Guid [key]
PX.Dashboards.DAC.WidgetV2.WidgetID : Edm.Guid [key]
PX.Dashboards.DAC.WidgetV2.OwnerName : Edm.String "Owner Name"
PX.Dashboards.DAC.WidgetV2.Caption : Edm.String "Caption"
PX.Dashboards.DAC.WidgetV2.Column : Edm.Int32 "Column"
PX.Dashboards.DAC.WidgetV2.Row : Edm.Int32 "Row"
PX.Dashboards.DAC.WidgetV2.Width : Edm.Int32 "Width"
PX.Dashboards.DAC.WidgetV2.Height : Edm.Int32 "Height"
PX.Dashboards.DAC.WidgetV2.Type : Edm.String "Widget Class"
PX.Dashboards.DAC.WidgetV2.Settings : Edm.String "Settings"
PX.Dashboards.DAC.WidgetV2.IsMasterCopy : Edm.Boolean
PX.Dashboards.DAC.WidgetV2.CreatedByID : Edm.Guid "Created By"
PX.Dashboards.DAC.WidgetV2.CreatedByScreenID : Edm.String
PX.Dashboards.DAC.WidgetV2.CreatedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.WidgetV2.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Dashboards.DAC.WidgetV2.LastModifiedByScreenID : Edm.String
PX.Dashboards.DAC.WidgetV2.LastModifiedDateTime : Edm.DateTimeOffset
PX.Dashboards.DAC.WidgetV2.NoteID : Edm.Guid
PX.Dashboards.DAC.WidgetV2.NoteText : Edm.String "Note Text"
PX.Dashboards.DAC.WidgetV2.IsActive : Edm.Boolean [required] "Active"
PX.Dashboards.DAC.WidgetV2.WidgetType : Edm.String "Widget Type"
PX.Dashboards.DAC.WidgetV2.Source : Edm.String "Source"
PX.Dashboards.DAC.WidgetV2.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Dashboards.DAC.WidgetV2.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Dashboards.DAC.WidgetV2.UsersByOwnerName -> PX.SM.Users (OwnerName=Username)
PX.Dashboards.DAC.WidgetV2.DashboardV2ByDashboardID -> PX.Dashboards.DAC.DashboardV2 (DashboardID=DashboardID)
PX.Dashboards.DAC.WidgetV2.WidgetParameterV2Collection -> Collection(PX.Dashboards.DAC.WidgetParameterV2)

# PX.Dashboards.Widgets.WidgetPivotTable (EntityType)

Key: PivotTableID, ScreenID
Entity sets: PX_Dashboards_Widgets_WidgetPivotTable

PX.Dashboards.Widgets.WidgetPivotTable.ScreenID : Edm.String [key] "Screen ID"
PX.Dashboards.Widgets.WidgetPivotTable.PivotTableID : Edm.Int32 [key] "Pivot Table ID"
PX.Dashboards.Widgets.WidgetPivotTable.Name : Edm.String "Name"
PX.Dashboards.Widgets.WidgetPivotTable.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Dashboards.Widgets.WidgetPivotTable.PivotFieldCollection -> Collection(PX.Olap.Maintenance.PivotField)
PX.Dashboards.Widgets.WidgetPivotTable.PivotFieldPreferencesCollection -> Collection(PX.Olap.Maintenance.PivotFieldPreferences)

# PX.Data.Archiving.DAC.ArchivalPolicy (EntityType)

Label: "Archival Policy"
Key: TableName
Entity sets: PX_Data_Archiving_DAC_ArchivalPolicy, ArchivalPolicy

PX.Data.Archiving.DAC.ArchivalPolicy.TableName : Edm.String [key] "Entity Name"
PX.Data.Archiving.DAC.ArchivalPolicy.TypeName : Edm.String
PX.Data.Archiving.DAC.ArchivalPolicy.RetentionPeriodInMonths : Edm.Int32 [required] "Retention Period (Months)"

# PX.Data.Archiving.DAC.ArchivalSetup (EntityType)

Label: "Archival Setup"
Singletons: PX_Data_Archiving_DAC_ArchivalSetup, ArchivalSetup

PX.Data.Archiving.DAC.ArchivalSetup.ArchivingProcessDurationLimitInHours : Edm.Int32 [required] "Archiving Process Duration (Hours)"

# PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate (EntityType)

Label: "Document Archival History"
Key: DateToArchive, ExecutionDate, TableName
Entity sets: PX_Data_Archiving_DAC_ArchivedDocumentBatchByDate, DocumentArchivalHistory, ArchivedDocumentBatchByDate

PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.DateToArchive : Edm.DateTimeOffset [key] "Ready-to-Archive Date"
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.ExecutionDate : Edm.DateTimeOffset [key]
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.TableName : Edm.String [key]
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.TypeName : Edm.String
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.ExecutionTimeInSeconds : Edm.Int32 "Duration"
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.ArchivedRowsCount : Edm.Int32
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.CreatedByID : Edm.Guid "Created By"
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.CreatedDateTime : Edm.DateTimeOffset
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.tstamp : Edm.Binary
PX.Data.Archiving.DAC.ArchivedDocumentBatchByDate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Data.DeletedRecordsTracking.DAC.ODataPreferences (EntityType)

Label: "OData Preferences"
Singletons: PX_Data_DeletedRecordsTracking_DAC_ODataPreferences, ODataPreferences

PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.DaysRetentionHistoryDeletedRecords : Edm.Int32 [required] "Days to Keep Records"
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.NoteID : Edm.Guid
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.NoteText : Edm.String "Note Text"
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.CreatedByID : Edm.Guid "Created By"
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.CreatedByScreenID : Edm.String
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.CreatedDateTime : Edm.DateTimeOffset
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.LastModifiedByScreenID : Edm.String
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.DeletedRecordsTracking.DAC.ODataPreferences.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables (EntityType)

Label: "Tables to Track Deleted Records"
Key: TableID
Entity sets: PX_Data_DeletedRecordsTracking_DAC_SMDeletedRecordsTrackingTables, TablestoTrackDeletedRecords, SMDeletedRecordsTrackingTables
Non-filterable, non-selectable: Description

PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables.TableID : Edm.Guid [key]
PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables.TableName : Edm.String "Table"
PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables.Description : Edm.String "Description"
PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables.CreatedDateTime : Edm.DateTimeOffset "Added On"
PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables.CreatedByID : Edm.Guid "Created By"
PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables.CreatedByScreenID : Edm.String
PX.Data.DeletedRecordsTracking.DAC.SMDeletedRecordsTrackingTables.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Data.Descriptor.Attributes.SearchIndexEntityRank (EntityType)

Singletons: PX_Data_Descriptor_Attributes_SearchIndexEntityRank

PX.Data.Descriptor.Attributes.SearchIndexEntityRank.EntityType : Edm.String
PX.Data.Descriptor.Attributes.SearchIndexEntityRank.EntityRank : Edm.Int16

# PX.Data.FilterHeader (EntityType)

Label: "Filter Header"
Key: FilterID, ScreenID, ViewName
Entity sets: PX_Data_FilterHeader, FilterHeader
Non-filterable, non-selectable: IsOwned, NoteText

PX.Data.FilterHeader.FilterID : Edm.Guid [key] "ID"
PX.Data.FilterHeader.UserName : Edm.String "UserName"
PX.Data.FilterHeader.ScreenID : Edm.String [key] "ScreenID"
PX.Data.FilterHeader.ViewName : Edm.String [key] "View"
PX.Data.FilterHeader.FilterName : Edm.String "Name"
PX.Data.FilterHeader.IsDefault : Edm.Boolean [required] "Is Default"
PX.Data.FilterHeader.IsShared : Edm.Boolean [required] "Is Shared"
PX.Data.FilterHeader.IsShortcut : Edm.Boolean [required] "Is Shortcut"
PX.Data.FilterHeader.IsSystem : Edm.Boolean [required] "IsSystem"
PX.Data.FilterHeader.IsHidden : Edm.Boolean "Is Hidden"
PX.Data.FilterHeader.FilterOrder : Edm.Int64 "Filter Order"
PX.Data.FilterHeader.IsOwned : Edm.Boolean "IsOwned"
PX.Data.FilterHeader.NoteID : Edm.Guid
PX.Data.FilterHeader.NoteText : Edm.String "Note Text"
PX.Data.FilterHeader.RefNoteID : Edm.Guid
PX.Data.FilterHeader.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.Data.FilterHeader.BPEventCollection -> Collection(PX.BusinessProcess.DAC.BPEvent)
PX.Data.FilterHeader.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Data.FilterHeader.AIGIToolDefinitionCollection -> Collection(PX.AI.Tools.GI.DAC.AIGIToolDefinition)
PX.Data.FilterHeader.FilterRowCollection -> Collection(PX.Data.FilterRow)

# PX.Data.FilterRow (EntityType)

Label: "Filter Row"
Key: FilterID, FilterRowNbr
Entity sets: PX_Data_FilterRow, FilterRow

PX.Data.FilterRow.IsUsed : Edm.Boolean [required] "Active"
PX.Data.FilterRow.FilterID : Edm.Guid [key] "FilterID"
PX.Data.FilterRow.FilterRowNbr : Edm.Int16 [key] "FilterRowNbr"
PX.Data.FilterRow.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.Data.FilterRow.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.Data.FilterRow.DataField : Edm.String "Property"
PX.Data.FilterRow.Condition : Edm.Byte "Condition"
PX.Data.FilterRow.ValueSt : Edm.String "Value"
PX.Data.FilterRow.ValueSt2 : Edm.String "Value2"
PX.Data.FilterRow.Operator : Edm.Int32 [required] "Operator"
PX.Data.FilterRow.FilterType : Edm.Byte [required]
PX.Data.FilterRow.FilterHeaderByFilterID -> PX.Data.FilterHeader (FilterID=FilterID)

# PX.Data.GenericInquiry.DAC.GIDataWarehouse (EntityType)

Label: "Generic Inquiry Data Warehouse"
Key: DesignID
Entity sets: PX_Data_GenericInquiry_DAC_GIDataWarehouse, GenericInquiryDataWarehouse, GIDataWarehouse
Non-filterable, non-selectable: UpdateScheduleExtended, WarningMessage, GIName, NoteText

PX.Data.GenericInquiry.DAC.GIDataWarehouse.DesignID : Edm.Guid [key]
PX.Data.GenericInquiry.DAC.GIDataWarehouse.TableName : Edm.String
PX.Data.GenericInquiry.DAC.GIDataWarehouse.UpdateFrequency : Edm.Int32 [required] "Update Schedule"
PX.Data.GenericInquiry.DAC.GIDataWarehouse.UpdateFrequencyInMinutes : Edm.Int32 "Frequency"
PX.Data.GenericInquiry.DAC.GIDataWarehouse.UpdateScheduleExtended : Edm.String "Frequency"
PX.Data.GenericInquiry.DAC.GIDataWarehouse.WarningMessage : Edm.String
PX.Data.GenericInquiry.DAC.GIDataWarehouse.GIName : Edm.String "Inquiry Title"
PX.Data.GenericInquiry.DAC.GIDataWarehouse.NoteID : Edm.Guid
PX.Data.GenericInquiry.DAC.GIDataWarehouse.NoteText : Edm.String "Note Text"
PX.Data.GenericInquiry.DAC.GIDataWarehouse.CreatedByID : Edm.Guid "Created By"
PX.Data.GenericInquiry.DAC.GIDataWarehouse.CreatedByScreenID : Edm.String
PX.Data.GenericInquiry.DAC.GIDataWarehouse.CreatedDateTime : Edm.DateTimeOffset
PX.Data.GenericInquiry.DAC.GIDataWarehouse.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.GenericInquiry.DAC.GIDataWarehouse.LastModifiedByScreenID : Edm.String
PX.Data.GenericInquiry.DAC.GIDataWarehouse.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.GenericInquiry.DAC.GIDataWarehouse.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.GenericInquiry.DAC.GIDataWarehouse.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.GenericInquiry.DAC.GIDataWarehouse.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.GridPreferences (EntityType)

Singletons: PX_Data_GridPreferences

# PX.Data.Licensing.SM.SMLicenseCommerceTran (EntityType)

Key: Date, ScreenID
Entity sets: PX_Data_Licensing_SM_SMLicenseCommerceTran

PX.Data.Licensing.SM.SMLicenseCommerceTran.InstallationID : Edm.String "InstallationID"
PX.Data.Licensing.SM.SMLicenseCommerceTran.Date : Edm.DateTimeOffset [key] "Date"
PX.Data.Licensing.SM.SMLicenseCommerceTran.ScreenID : Edm.String [key required] "ScreenID"
PX.Data.Licensing.SM.SMLicenseCommerceTran.Count : Edm.Int32 [required] "Count"
PX.Data.Licensing.SM.SMLicenseCommerceTran.Signature : Edm.String "Signature"

# PX.Data.Licensing.SM.SMLicenseConstraints (EntityType)

Key: CompanyIdentifier, Date
Entity sets: PX_Data_Licensing_SM_SMLicenseConstraints

PX.Data.Licensing.SM.SMLicenseConstraints.InstallationID : Edm.String "InstallationID"
PX.Data.Licensing.SM.SMLicenseConstraints.Date : Edm.DateTimeOffset [key] "Date"
PX.Data.Licensing.SM.SMLicenseConstraints.CompanyIdentifier : Edm.Int32 [key required] "CompanyIdentifier"
PX.Data.Licensing.SM.SMLicenseConstraints.FixedAssets : Edm.Int32 "FixedAssets"
PX.Data.Licensing.SM.SMLicenseConstraints.InventoryItems : Edm.Int32 "InventoryItems"
PX.Data.Licensing.SM.SMLicenseConstraints.BAccount : Edm.Int32 "BAccount"
PX.Data.Licensing.SM.SMLicenseConstraints.PayrollEmployees : Edm.Int32 "PayrollEmployees"
PX.Data.Licensing.SM.SMLicenseConstraints.FSStaffVehicles : Edm.Int32 "FSStaffVehicles"
PX.Data.Licensing.SM.SMLicenseConstraints.FSAppointments : Edm.Int32 "FSAppointments"
PX.Data.Licensing.SM.SMLicenseConstraints.ExpenseReceiptsRecognized : Edm.Int32 "ExpenseReceiptsRecognized"
PX.Data.Licensing.SM.SMLicenseConstraints.BusinessCardsRecognized : Edm.Int32 "BusinessCardsRecognized"
PX.Data.Licensing.SM.SMLicenseConstraints.DocumentsRecognized : Edm.Int32 "APDocumentsRecognized"
PX.Data.Licensing.SM.SMLicenseConstraints.BankFeedAccounts : Edm.Int32 "BankFeedAccounts"
PX.Data.Licensing.SM.SMLicenseConstraints.Violation : Edm.Int32
PX.Data.Licensing.SM.SMLicenseConstraints.Signature : Edm.String "Signature"
PX.Data.Licensing.SM.SMLicenseConstraints.AiAssistantTokensProcessed : Edm.Int32 "AI Units"

# PX.Data.Licensing.SM.SMLicenseERPTran (EntityType)

Key: Date, PrimaryItemType, ScreenID, TransactionType
Entity sets: PX_Data_Licensing_SM_SMLicenseERPTran

PX.Data.Licensing.SM.SMLicenseERPTran.InstallationID : Edm.String "InstallationID"
PX.Data.Licensing.SM.SMLicenseERPTran.Date : Edm.DateTimeOffset [key] "Date"
PX.Data.Licensing.SM.SMLicenseERPTran.ScreenID : Edm.String [key required] "ScreenID"
PX.Data.Licensing.SM.SMLicenseERPTran.TransactionType : Edm.String [key required] "Transaction Source"
PX.Data.Licensing.SM.SMLicenseERPTran.Count : Edm.Int32 [required] "Count"
PX.Data.Licensing.SM.SMLicenseERPTran.Signature : Edm.String "Signature"
PX.Data.Licensing.SM.SMLicenseERPTran.PrimaryItemType : Edm.String [key required] "PrimaryItemType"

# PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction (EntityType)

Label: "SMLicenseERPTranDetailsAction"
Key: ActionId
Entity sets: PX_Data_Licensing_SM_SMLicenseERPTranDetailsAction, SMLicenseERPTranDetailsAction

PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction.ActionId : Edm.Guid [key]
PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction.Date : Edm.DateTimeOffset "Registered At"
PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction.ScreenID : Edm.String "Screen ID"
PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction.ActionName : Edm.String "Action"
PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction.TransactionType : Edm.String "Action Type"
PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction.TranCount : Edm.Int32 "Number of Transactions"
PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction.SMLicenseERPTranDetailsDocCollection -> Collection(PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc)

# PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc (EntityType)

Label: "SMLicenseERPTranDetailsDoc"
Key: Id
Entity sets: PX_Data_Licensing_SM_SMLicenseERPTranDetailsDoc, SMLicenseERPTranDetailsDoc

PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc.Id : Edm.Guid [key]
PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc.ActionId : Edm.Guid
PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc.TranDocKeys : Edm.String
PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc.TranDocScreen : Edm.String
PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc.TranDocItemType : Edm.String
PX.Data.Licensing.SM.SMLicenseERPTranDetailsDoc.SMLicenseERPTranDetailsActionByActionId -> PX.Data.Licensing.SM.SMLicenseERPTranDetailsAction (ActionId=ActionId)

# PX.Data.Licensing.SM.SMLicenseViolations (EntityType)

Key: Date, LimitType, TranType
Entity sets: PX_Data_Licensing_SM_SMLicenseViolations
Non-filterable, non-selectable: StatusUserFriendly, LimitTypeUserFriendly, TranTypeUserFriendly, OverchargeRate

PX.Data.Licensing.SM.SMLicenseViolations.InstallationID : Edm.String "InstallationID"
PX.Data.Licensing.SM.SMLicenseViolations.Status : Edm.String "Status"
PX.Data.Licensing.SM.SMLicenseViolations.StatusUserFriendly : Edm.String "Status"
PX.Data.Licensing.SM.SMLicenseViolations.Date : Edm.DateTimeOffset [key] "Date"
PX.Data.Licensing.SM.SMLicenseViolations.LimitType : Edm.String [key required] "LimitType"
PX.Data.Licensing.SM.SMLicenseViolations.LimitTypeUserFriendly : Edm.String "Limit Type"
PX.Data.Licensing.SM.SMLicenseViolations.TranType : Edm.String [key required] "TranType"
PX.Data.Licensing.SM.SMLicenseViolations.TranTypeUserFriendly : Edm.String "Data Type"
PX.Data.Licensing.SM.SMLicenseViolations.TranCount : Edm.Int32 [required] "Transaction Count"
PX.Data.Licensing.SM.SMLicenseViolations.Limit : Edm.Int32 [required] "License Limit"
PX.Data.Licensing.SM.SMLicenseViolations.OverchargeRate : Edm.Int32 "% of Overcharge"
PX.Data.Licensing.SM.SMLicenseViolations.CloseDate : Edm.DateTimeOffset "Dismissed On"
PX.Data.Licensing.SM.SMLicenseViolations.Reason : Edm.String "Comment"
PX.Data.Licensing.SM.SMLicenseViolations.Signature : Edm.String "Signature"

# PX.Data.ListEntryPoint (EntityType)

Label: "List as Entry Point"
Key: EntryScreenID
Entity sets: PX_Data_ListEntryPoint, ListasEntryPoint, ListEntryPoint

PX.Data.ListEntryPoint.EntryScreenID : Edm.String [key] "Entry Screen ID"
PX.Data.ListEntryPoint.ListScreenID : Edm.String "Substitute Screen ID"
PX.Data.ListEntryPoint.IsActive : Edm.Boolean [required] "Active"
PX.Data.ListEntryPoint.CreatedByID : Edm.Guid "Created By"
PX.Data.ListEntryPoint.CreatedByScreenID : Edm.String
PX.Data.ListEntryPoint.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Data.ListEntryPoint.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.ListEntryPoint.LastModifiedByScreenID : Edm.String
PX.Data.ListEntryPoint.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Data.ListEntryPoint.SiteMapByEntryScreenID -> PX.SM.SiteMap (EntryScreenID=ScreenID)
PX.Data.ListEntryPoint.SiteMapByListScreenID -> PX.SM.SiteMap (ListScreenID=ScreenID)
PX.Data.ListEntryPoint.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.ListEntryPoint.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Data.Localization.SystemCollation (EntityType)

Key: CollationName, CollationNameCS, CollationNameCSLatin, CollationNameLatin, SqlDialect
Entity sets: PX_Data_Localization_SystemCollation

PX.Data.Localization.SystemCollation.CollationName : Edm.String [key]
PX.Data.Localization.SystemCollation.CollationNameCS : Edm.String [key]
PX.Data.Localization.SystemCollation.CollationNameLatin : Edm.String [key]
PX.Data.Localization.SystemCollation.CollationNameCSLatin : Edm.String [key]
PX.Data.Localization.SystemCollation.SqlDialect : Edm.String [key]
PX.Data.Localization.SystemCollation.LocaleName : Edm.String
PX.Data.Localization.SystemCollation.Priority : Edm.Int32

# PX.Data.Maintenance.GI.GIDesign (EntityType)

Label: "Generic Inquiry"
Key: Name
Entity sets: PX_Data_Maintenance_GI_GIDesign, GenericInquiry, GIDesign
Non-filterable, non-selectable: ReplacePrimaryScreen, NoteText, SitemapTitle, SitemapSelectorTitle, SitemapScreenID, DefaultSortOrder, DesignerMode, Query, IsDraft, AiAssistantGISyncStatus, WorkspaceID, SubcategoryID

PX.Data.Maintenance.GI.GIDesign.DesignID : Edm.Guid
PX.Data.Maintenance.GI.GIDesign.Name : Edm.String [key] "Inquiry Title"
PX.Data.Maintenance.GI.GIDesign.SelectTop : Edm.Int32 "Select Top"
PX.Data.Maintenance.GI.GIDesign.FilterColCount : Edm.Int32 "Arrange Parameters in"
PX.Data.Maintenance.GI.GIDesign.PageSize : Edm.Int32 "Records per Page"
PX.Data.Maintenance.GI.GIDesign.ExportTop : Edm.Int32 "Export Top"
PX.Data.Maintenance.GI.GIDesign.PrimaryScreenID : Edm.String "Entry Screen"
PX.Data.Maintenance.GI.GIDesign.ReplacePrimaryScreen : Edm.Boolean "Replace Entry Screen with this Inquiry in Menu"
PX.Data.Maintenance.GI.GIDesign.NewRecordCreationEnabled : Edm.Boolean [required] "Enable New Record Creation"
PX.Data.Maintenance.GI.GIDesign.MassDeleteEnabled : Edm.Boolean [required] "Enable Mass Record Deletion"
PX.Data.Maintenance.GI.GIDesign.AutoConfirmDelete : Edm.Boolean [required] "Auto-Confirm Custom Delete Confirmations"
PX.Data.Maintenance.GI.GIDesign.MassRecordsUpdateEnabled : Edm.Boolean [required] "Enable Mass Record Update"
PX.Data.Maintenance.GI.GIDesign.MassActionsOnRecordsEnabled : Edm.Boolean [required] "Enable Mass Actions on Records"
PX.Data.Maintenance.GI.GIDesign.ExposeViaOData : Edm.Boolean [required] "Expose via OData"
PX.Data.Maintenance.GI.GIDesign.ExposeViaMobile : Edm.Boolean [required] "Expose to the Mobile Application"
PX.Data.Maintenance.GI.GIDesign.UseDataWarehouse : Edm.Boolean [required] "Store Result in Data Warehouse"
PX.Data.Maintenance.GI.GIDesign.NotesAndFilesTable : Edm.String "Attach Notes To"
PX.Data.Maintenance.GI.GIDesign.RowStyleFormula : Edm.String "Row Style"
PX.Data.Maintenance.GI.GIDesign.ShowDeletedRecords : Edm.Boolean [required] "Show Deleted Records"
PX.Data.Maintenance.GI.GIDesign.ShowArchivedRecords : Edm.Boolean [required] "Show Archived Records"
PX.Data.Maintenance.GI.GIDesign.DisableCountsAndTotals : Edm.Boolean [required] "Disable Record Counts and Totals"
PX.Data.Maintenance.GI.GIDesign.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GIDesign.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GIDesign.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GIDesign.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIDesign.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GIDesign.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GIDesign.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIDesign.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GIDesign.SitemapTitle : Edm.String "Site Map Title"
PX.Data.Maintenance.GI.GIDesign.SitemapSelectorTitle : Edm.String "Site Map Title"
PX.Data.Maintenance.GI.GIDesign.SitemapScreenID : Edm.String "Screen ID"
PX.Data.Maintenance.GI.GIDesign.DefaultSortOrder : Edm.String "Default Sort Order"
PX.Data.Maintenance.GI.GIDesign.ODataFunctionName : Edm.String "OData Function Name"
PX.Data.Maintenance.GI.GIDesign.DesignerMode : Edm.String "Mode"
PX.Data.Maintenance.GI.GIDesign.Query : Edm.String "Query"
PX.Data.Maintenance.GI.GIDesign.IsDraft : Edm.Boolean
PX.Data.Maintenance.GI.GIDesign.ExposeToAiAssistant : Edm.Boolean "Expose to AI Assistant"
PX.Data.Maintenance.GI.GIDesign.AiAssistantGISyncStatus : Edm.String "Status"
PX.Data.Maintenance.GI.GIDesign.AiDescription : Edm.String "Description for AI"
PX.Data.Maintenance.GI.GIDesign.WorkspaceID : Edm.Guid "Workspace"
PX.Data.Maintenance.GI.GIDesign.SubcategoryID : Edm.Guid "Category"
PX.Data.Maintenance.GI.GIDesign.SiteMapByPrimaryScreenID -> PX.SM.SiteMap (PrimaryScreenID=ScreenID)
PX.Data.Maintenance.GI.GIDesign.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GIDesign.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GIDesign.CRMarketingListCollection -> Collection(PX.Objects.CR.CRMarketingList)
PX.Data.Maintenance.GI.GIDesign.PushNotificationsSourceCollection -> Collection(PX.PushNotifications.UI.DAC.PushNotificationsSource)
PX.Data.Maintenance.GI.GIDesign.GIFilterCollection -> Collection(PX.Data.Maintenance.GI.GIFilter)
PX.Data.Maintenance.GI.GIDesign.GIGroupByCollection -> Collection(PX.Data.Maintenance.GI.GIGroupBy)
PX.Data.Maintenance.GI.GIDesign.GINavigationScreenCollection -> Collection(PX.Data.Maintenance.GI.GINavigationScreen)
PX.Data.Maintenance.GI.GIDesign.GINavigationParameterCollection -> Collection(PX.Data.Maintenance.GI.GINavigationParameter)
PX.Data.Maintenance.GI.GIDesign.GINavigationConditionCollection -> Collection(PX.Data.Maintenance.GI.GINavigationCondition)
PX.Data.Maintenance.GI.GIDesign.GIRecordDefaultCollection -> Collection(PX.Data.Maintenance.GI.GIRecordDefault)
PX.Data.Maintenance.GI.GIDesign.GIRelationCollection -> Collection(PX.Data.Maintenance.GI.GIRelation)
PX.Data.Maintenance.GI.GIDesign.GIOnCollection -> Collection(PX.Data.Maintenance.GI.GIOn)
PX.Data.Maintenance.GI.GIDesign.GIResultCollection -> Collection(PX.Data.Maintenance.GI.GIResult)
PX.Data.Maintenance.GI.GIDesign.GISortCollection -> Collection(PX.Data.Maintenance.GI.GISort)
PX.Data.Maintenance.GI.GIDesign.GITableCollection -> Collection(PX.Data.Maintenance.GI.GITable)
PX.Data.Maintenance.GI.GIDesign.GIWhereCollection -> Collection(PX.Data.Maintenance.GI.GIWhere)
PX.Data.Maintenance.GI.GIDesign.GIDataWarehouseCollection -> Collection(PX.Data.GenericInquiry.DAC.GIDataWarehouse)
PX.Data.Maintenance.GI.GIDesign.GIReportCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReport)
PX.Data.Maintenance.GI.GIDesign.GIMassActionCollection -> Collection(PX.Data.Maintenance.GI.GIMassAction)
PX.Data.Maintenance.GI.GIDesign.GIMassUpdateFieldCollection -> Collection(PX.Data.Maintenance.GI.GIMassUpdateField)
PX.Data.Maintenance.GI.GIDesign.MLCrossSalesSetupCollection -> Collection(PX.ML.CrossSales.DAC.MLCrossSalesSetup)

# PX.Data.Maintenance.GI.GIFilter (EntityType)

Label: "Generic Inquiry Filter"
Key: DesignID, LineNbr
Entity sets: PX_Data_Maintenance_GI_GIFilter, GenericInquiryFilter, GIFilter
Non-filterable, non-selectable: NoteText

PX.Data.Maintenance.GI.GIFilter.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIFilter.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GIFilter.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GIFilter.Name : Edm.String "Name"
PX.Data.Maintenance.GI.GIFilter.FieldName : Edm.String "Schema Field"
PX.Data.Maintenance.GI.GIFilter.DataType : Edm.String "Type"
PX.Data.Maintenance.GI.GIFilter.DisplayName : Edm.String "Display Name"
PX.Data.Maintenance.GI.GIFilter.AvailableValues : Edm.String "Available Values"
PX.Data.Maintenance.GI.GIFilter.IsExpression : Edm.Boolean [required] "From Schema"
PX.Data.Maintenance.GI.GIFilter.DefaultValue : Edm.String "Default Value"
PX.Data.Maintenance.GI.GIFilter.ColSpan : Edm.Int32 [required] "Column Span"
PX.Data.Maintenance.GI.GIFilter.Required : Edm.Boolean [required] "Is Required"
PX.Data.Maintenance.GI.GIFilter.Hidden : Edm.Boolean "Hidden"
PX.Data.Maintenance.GI.GIFilter.Size : Edm.String "Control Size"
PX.Data.Maintenance.GI.GIFilter.LabelSize : Edm.String "Label Size"
PX.Data.Maintenance.GI.GIFilter.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GIFilter.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GIFilter.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GIFilter.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIFilter.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GIFilter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GIFilter.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIFilter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GIFilter.AiDescription : Edm.String "Description for AI"
PX.Data.Maintenance.GI.GIFilter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GIFilter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GIFilter.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GIGroupBy (EntityType)

Label: "Generic Inquiry Grouping"
Key: DesignID, LineNbr
Entity sets: PX_Data_Maintenance_GI_GIGroupBy, GenericInquiryGrouping, GIGroupBy
Non-filterable, non-selectable: NoteText

PX.Data.Maintenance.GI.GIGroupBy.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIGroupBy.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GIGroupBy.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GIGroupBy.DataFieldName : Edm.String "Data Field"
PX.Data.Maintenance.GI.GIGroupBy.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GIGroupBy.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GIGroupBy.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GIGroupBy.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIGroupBy.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GIGroupBy.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GIGroupBy.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIGroupBy.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GIGroupBy.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GIGroupBy.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GIGroupBy.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GIMassAction (EntityType)

Label: "Generic Inquiry Mass Action"
Key: ActionName, DesignID, MassActionID
Entity sets: PX_Data_Maintenance_GI_GIMassAction, GenericInquiryMassAction, GIMassAction

PX.Data.Maintenance.GI.GIMassAction.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIMassAction.MassActionID : Edm.Int32 [key] "Mass Action ID"
PX.Data.Maintenance.GI.GIMassAction.ActionName : Edm.String [key] "Action"
PX.Data.Maintenance.GI.GIMassAction.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GIMassAction.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GIMassUpdateField (EntityType)

Label: "Generic Inquiry Mass Update Field"
Key: DesignID, FieldID, FieldName
Entity sets: PX_Data_Maintenance_GI_GIMassUpdateField, GenericInquiryMassUpdateField, GIMassUpdateField

PX.Data.Maintenance.GI.GIMassUpdateField.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIMassUpdateField.FieldID : Edm.Int32 [key] "Mass Update Field ID"
PX.Data.Maintenance.GI.GIMassUpdateField.FieldName : Edm.String [key] "Field Name"
PX.Data.Maintenance.GI.GIMassUpdateField.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GIMassUpdateField.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GINavigationCondition (EntityType)

Label: "Generic Inquiry Navigation Condition"
Key: DesignID, LineNbr, NavigationScreenLineNbr
Entity sets: PX_Data_Maintenance_GI_GINavigationCondition, GenericInquiryNavigationCondition, GINavigationCondition

PX.Data.Maintenance.GI.GINavigationCondition.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GINavigationCondition.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GINavigationCondition.NavigationScreenLineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GINavigationCondition.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GINavigationCondition.DataField : Edm.String "Data Field"
PX.Data.Maintenance.GI.GINavigationCondition.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.Data.Maintenance.GI.GINavigationCondition.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.Data.Maintenance.GI.GINavigationCondition.Condition : Edm.String "Condition"
PX.Data.Maintenance.GI.GINavigationCondition.IsExpression : Edm.Boolean [required] "From Schema"
PX.Data.Maintenance.GI.GINavigationCondition.ValueSt : Edm.String "Value"
PX.Data.Maintenance.GI.GINavigationCondition.ValueSt2 : Edm.String "Value 2"
PX.Data.Maintenance.GI.GINavigationCondition.Operator : Edm.String "Operator"
PX.Data.Maintenance.GI.GINavigationCondition.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GINavigationCondition.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GINavigationCondition.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GINavigationCondition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GINavigationCondition.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GINavigationCondition.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GINavigationCondition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GINavigationCondition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GINavigationCondition.GINavigationScreenByNavigationScreenLineNbr -> PX.Data.Maintenance.GI.GINavigationScreen (DesignID=DesignID, NavigationScreenLineNbr=LineNbr)
PX.Data.Maintenance.GI.GINavigationCondition.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GINavigationParameter (EntityType)

Label: "Generic Inquiry Navigation Parameter"
Key: DesignID, LineNbr, NavigationScreenLineNbr
Entity sets: PX_Data_Maintenance_GI_GINavigationParameter, GenericInquiryNavigationParameter, GINavigationParameter

PX.Data.Maintenance.GI.GINavigationParameter.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GINavigationParameter.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GINavigationParameter.NavigationScreenLineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GINavigationParameter.FieldName : Edm.String "Field"
PX.Data.Maintenance.GI.GINavigationParameter.ParameterName : Edm.String "Parameter"
PX.Data.Maintenance.GI.GINavigationParameter.IsExpression : Edm.Boolean [required] "From Schema"
PX.Data.Maintenance.GI.GINavigationParameter.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GINavigationParameter.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GINavigationParameter.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GINavigationParameter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GINavigationParameter.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GINavigationParameter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GINavigationParameter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GINavigationParameter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GINavigationParameter.GINavigationScreenByNavigationScreenLineNbr -> PX.Data.Maintenance.GI.GINavigationScreen (DesignID=DesignID, NavigationScreenLineNbr=LineNbr)
PX.Data.Maintenance.GI.GINavigationParameter.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GINavigationScreen (EntityType)

Label: "Generic Inquiry Navigation Screen"
Key: DesignID, LineNbr
Entity sets: PX_Data_Maintenance_GI_GINavigationScreen, GenericInquiryNavigationScreen, GINavigationScreen
Non-filterable, non-selectable: Title, NoteText

PX.Data.Maintenance.GI.GINavigationScreen.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GINavigationScreen.Link : Edm.String "Link"
PX.Data.Maintenance.GI.GINavigationScreen.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GINavigationScreen.SortOrder : Edm.Int32 "Sort Order"
PX.Data.Maintenance.GI.GINavigationScreen.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GINavigationScreen.Title : Edm.String "Title"
PX.Data.Maintenance.GI.GINavigationScreen.WindowMode : Edm.String "Window Mode"
PX.Data.Maintenance.GI.GINavigationScreen.Icon : Edm.String "Icon"
PX.Data.Maintenance.GI.GINavigationScreen.CustomTitle : Edm.String "Custom Title"
PX.Data.Maintenance.GI.GINavigationScreen.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GINavigationScreen.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GINavigationScreen.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GINavigationScreen.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GINavigationScreen.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GINavigationScreen.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GINavigationScreen.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GINavigationScreen.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GINavigationScreen.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GINavigationScreen.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GINavigationScreen.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)
PX.Data.Maintenance.GI.GINavigationScreen.GINavigationParameterCollection -> Collection(PX.Data.Maintenance.GI.GINavigationParameter)
PX.Data.Maintenance.GI.GINavigationScreen.GINavigationConditionCollection -> Collection(PX.Data.Maintenance.GI.GINavigationCondition)

# PX.Data.Maintenance.GI.GIOn (EntityType)

Label: "Generic Inquiry Relation Dependencies"
Key: DesignID, LineNbr, RelationNbr
Entity sets: PX_Data_Maintenance_GI_GIOn, GenericInquiryRelationDependencies, GIOn
Non-filterable, non-selectable: NoteText

PX.Data.Maintenance.GI.GIOn.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIOn.RelationNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GIOn.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GIOn.OpenBrackets : Edm.String "Brackets"
PX.Data.Maintenance.GI.GIOn.ParentField : Edm.String "Parent Field"
PX.Data.Maintenance.GI.GIOn.Condition : Edm.String "Condition"
PX.Data.Maintenance.GI.GIOn.ChildField : Edm.String "Child Field"
PX.Data.Maintenance.GI.GIOn.CloseBrackets : Edm.String "Brackets"
PX.Data.Maintenance.GI.GIOn.Operation : Edm.String "Operator"
PX.Data.Maintenance.GI.GIOn.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GIOn.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GIOn.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GIOn.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIOn.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GIOn.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GIOn.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIOn.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GIOn.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GIOn.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GIOn.GIRelationByRelationNbr -> PX.Data.Maintenance.GI.GIRelation (DesignID=DesignID, RelationNbr=LineNbr)
PX.Data.Maintenance.GI.GIOn.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GIRecordDefault (EntityType)

Label: "Generic Inquiry Default Record"
Key: DesignID, FieldName, RecDefID
Entity sets: PX_Data_Maintenance_GI_GIRecordDefault, GenericInquiryDefaultRecord, GIRecordDefault

PX.Data.Maintenance.GI.GIRecordDefault.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIRecordDefault.RecDefID : Edm.Int32 [key] "Default ID"
PX.Data.Maintenance.GI.GIRecordDefault.FieldName : Edm.String [key] "Field"
PX.Data.Maintenance.GI.GIRecordDefault.Value : Edm.String "Value"
PX.Data.Maintenance.GI.GIRecordDefault.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GIRecordDefault.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIRecordDefault.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GIRecordDefault.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GIRecordDefault.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIRecordDefault.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GIRecordDefault.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GIRecordDefault.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GIRecordDefault.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GIRelation (EntityType)

Label: "Generic Inquiry Relation"
Key: DesignID, LineNbr
Entity sets: PX_Data_Maintenance_GI_GIRelation, GenericInquiryRelation, GIRelation
Non-filterable, non-selectable: IsAddRelatedTableAllowed, NoteText

PX.Data.Maintenance.GI.GIRelation.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIRelation.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Data.Maintenance.GI.GIRelation.ParentTable : Edm.String "Parent Table"
PX.Data.Maintenance.GI.GIRelation.ChildTable : Edm.String "Child Table"
PX.Data.Maintenance.GI.GIRelation.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GIRelation.JoinType : Edm.String "Join Type"
PX.Data.Maintenance.GI.GIRelation.IsAddRelatedTableAllowed : Edm.Boolean
PX.Data.Maintenance.GI.GIRelation.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GIRelation.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GIRelation.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GIRelation.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIRelation.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GIRelation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GIRelation.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIRelation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GIRelation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GIRelation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GIRelation.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)
PX.Data.Maintenance.GI.GIRelation.GIOnCollection -> Collection(PX.Data.Maintenance.GI.GIOn)

# PX.Data.Maintenance.GI.GIResult (EntityType)

Label: "Generic Inquiry Result"
Key: DesignID, LineNbr
Entity sets: PX_Data_Maintenance_GI_GIResult, GenericInquiryResult, GIResult
Non-filterable, non-selectable: FieldName, NoteText

PX.Data.Maintenance.GI.GIResult.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIResult.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GIResult.SortOrder : Edm.Int32 "Sort Order"
PX.Data.Maintenance.GI.GIResult.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GIResult.ObjectName : Edm.String "Object"
PX.Data.Maintenance.GI.GIResult.Field : Edm.String "Data Field"
PX.Data.Maintenance.GI.GIResult.FieldName : Edm.String
PX.Data.Maintenance.GI.GIResult.SchemaField : Edm.String "Schema Field"
PX.Data.Maintenance.GI.GIResult.Caption : Edm.String "Caption"
PX.Data.Maintenance.GI.GIResult.StyleFormula : Edm.String "Style"
PX.Data.Maintenance.GI.GIResult.Width : Edm.Int32 "Width (px)"
PX.Data.Maintenance.GI.GIResult.IsVisible : Edm.Boolean [required] "Visible"
PX.Data.Maintenance.GI.GIResult.DefaultNav : Edm.Boolean [required] "Default Navigation"
PX.Data.Maintenance.GI.GIResult.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GIResult.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GIResult.RowID : Edm.Guid
PX.Data.Maintenance.GI.GIResult.AggregateFunction : Edm.String "Aggregate Function"
PX.Data.Maintenance.GI.GIResult.TotalAggregateFunction : Edm.String "Total Aggregate Function"
PX.Data.Maintenance.GI.GIResult.NavigationNbr : Edm.Int32 "Navigate To"
PX.Data.Maintenance.GI.GIResult.QuickFilter : Edm.Boolean [required] "Quick Filter"
PX.Data.Maintenance.GI.GIResult.FastFilter : Edm.Boolean [required] "Use in Quick Search"
PX.Data.Maintenance.GI.GIResult.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GIResult.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIResult.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GIResult.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GIResult.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIResult.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GIResult.AiDescription : Edm.String "Description for AI"
PX.Data.Maintenance.GI.GIResult.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GIResult.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GIResult.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GISort (EntityType)

Label: "Generic Inquiry Sorting"
Key: DesignID, LineNbr
Entity sets: PX_Data_Maintenance_GI_GISort, GenericInquirySorting, GISort
Non-filterable, non-selectable: NoteText

PX.Data.Maintenance.GI.GISort.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GISort.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GISort.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GISort.DataFieldName : Edm.String "Data Field"
PX.Data.Maintenance.GI.GISort.SortOrder : Edm.String "Sort Order"
PX.Data.Maintenance.GI.GISort.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GISort.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GISort.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GISort.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GISort.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GISort.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GISort.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GISort.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GISort.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GISort.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GISort.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GITable (EntityType)

Label: "Generic Inquiry Table"
Key: Alias, DesignID
Entity sets: PX_Data_Maintenance_GI_GITable, GenericInquiryTable, GITable
Non-filterable, non-selectable: Description, IsAddRelatedTableAllowed, NoteText

PX.Data.Maintenance.GI.GITable.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GITable.Alias : Edm.String [key] "Alias"
PX.Data.Maintenance.GI.GITable.Name : Edm.String "Source Name"
PX.Data.Maintenance.GI.GITable.Description : Edm.String "Description"
PX.Data.Maintenance.GI.GITable.Type : Edm.Int32 "Type"
PX.Data.Maintenance.GI.GITable.IsAddRelatedTableAllowed : Edm.Boolean
PX.Data.Maintenance.GI.GITable.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GITable.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GITable.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GITable.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GITable.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GITable.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GITable.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GITable.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GITable.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GITable.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GITable.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.GI.GIWhere (EntityType)

Label: "Generic Inquiry Where Statement"
Key: DesignID, LineNbr
Entity sets: PX_Data_Maintenance_GI_GIWhere, GenericInquiryWhereStatement, GIWhere
Non-filterable, non-selectable: NoteText

PX.Data.Maintenance.GI.GIWhere.DesignID : Edm.Guid [key]
PX.Data.Maintenance.GI.GIWhere.LineNbr : Edm.Int32 [key]
PX.Data.Maintenance.GI.GIWhere.IsActive : Edm.Boolean [required] "Active"
PX.Data.Maintenance.GI.GIWhere.OpenBrackets : Edm.String "Brackets"
PX.Data.Maintenance.GI.GIWhere.DataFieldName : Edm.String "Data Field"
PX.Data.Maintenance.GI.GIWhere.Condition : Edm.String "Condition"
PX.Data.Maintenance.GI.GIWhere.IsExpression : Edm.Boolean [required] "From Schema"
PX.Data.Maintenance.GI.GIWhere.Value1 : Edm.String "Value 1"
PX.Data.Maintenance.GI.GIWhere.Value2 : Edm.String "Value 2"
PX.Data.Maintenance.GI.GIWhere.CloseBrackets : Edm.String "Brackets"
PX.Data.Maintenance.GI.GIWhere.Operation : Edm.String "Operator"
PX.Data.Maintenance.GI.GIWhere.NoteID : Edm.Guid
PX.Data.Maintenance.GI.GIWhere.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.GI.GIWhere.CreatedByID : Edm.Guid "Created By"
PX.Data.Maintenance.GI.GIWhere.CreatedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIWhere.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.Data.Maintenance.GI.GIWhere.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Maintenance.GI.GIWhere.LastModifiedByScreenID : Edm.String
PX.Data.Maintenance.GI.GIWhere.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Maintenance.GI.GIWhere.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Maintenance.GI.GIWhere.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Maintenance.GI.GIWhere.GIDesignByDesignID -> PX.Data.Maintenance.GI.GIDesign (DesignID=DesignID)

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceChart (EntityType)

Singletons: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_Mappings_SMLicenseResourceChart

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceChart.Id : Edm.Byte
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceChart.Name : Edm.String

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceSplit (EntityType)

Singletons: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_Mappings_SMLicenseResourceSplit

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceSplit.Id : Edm.Byte
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings.SMLicenseResourceSplit.Name : Edm.String

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary (EntityType)

Key: Date, InstallationID
Entity sets: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceDailyUsageSummary

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.InstallationID : Edm.String [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.Date : Edm.DateTimeOffset [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.CalendarThrottling : Edm.Boolean
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.CalendarReducedPerformance : Edm.Boolean
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.ExcessiveConsumption : Edm.Boolean
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.ElevatedConsumption : Edm.Boolean
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileCPUDayMaxUsage : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileSQLDayMaxUsage : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileMemoryDayMaxUsage : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileCPUCumulative : Edm.Int64
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileSQLCumulative : Edm.Int64
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileMemoryAverage : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileMonthlyCTV : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileMonthlyETV : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileApiSessionsMax : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.TileApiRequestsPerMinMax : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.ApiExcessiveConsumption : Edm.Boolean
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDailyUsageSummary.ApiSignificantThrottling : Edm.Boolean

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated (EntityType)

Key: ChartId, InstallationID, IntervalDateTime, Legend, SplitId
Entity sets: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceDayUsageAggregated

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated.InstallationID : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated.IntervalDateTime : Edm.DateTimeOffset [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated.ChartId : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated.SplitId : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated.Legend : Edm.String [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceDayUsageAggregated.Value : Edm.Int32

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceInstallation (EntityType)

Key: Id
Entity sets: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceInstallation

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceInstallation.Id : Edm.Int32 [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceInstallation.Name : Edm.String

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits (EntityType)

Key: Date, InstallationID
Entity sets: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceParamLimits
Non-filterable, non-selectable: APISessions

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.InstallationID : Edm.String [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.Date : Edm.DateTimeOffset [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.LicenceKey : Edm.String
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.PeakAPIRequests : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.CPUHardLimit : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.SQLHardLimit : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.MemoryMaxUsage : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.CPUCumulative : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.SQLCumulative : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.MemoryAverage : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.CTVMonthly : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.CTVDaily : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.ERPTranMonthly : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.ERPTranDaily : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.ApiProcessingCores : Edm.Int32
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceParamLimits.APISessions : Edm.Int32

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetails (EntityType)

Key: DayIndex, EncodedIDs, Legend
Entity sets: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetails

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetails.EncodedIDs : Edm.Int16 [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetails.Legend : Edm.String [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetails.DayIndex : Edm.Int16 [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetails.Scale : Edm.Byte

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsPacked (EntityType)

Key: ChartId, DayIndex, InstallationId, Legend, SplitId
Entity sets: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetailsPacked

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsPacked.InstallationId : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsPacked.DayIndex : Edm.Int16 [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsPacked.ChartId : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsPacked.SplitId : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsPacked.Legend : Edm.String [key]

# PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp (EntityType)

Key: ChartId, InstallationID, IntervalDateTime, Legend, SplitId
Entity sets: PX_Data_Maintenance_SM_DAC_LicenseResourceMonitoring_SMLicenseResourceUsageDetailsTmp

PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp.InstallationID : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp.IntervalDateTime : Edm.DateTimeOffset [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp.ChartId : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp.SplitId : Edm.Byte [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp.Legend : Edm.String [key]
PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.SMLicenseResourceUsageDetailsTmp.Value : Edm.Int32

# PX.Data.Maintenance.SM.DAC.SMLicenseStatistic (EntityType)

Key: Date
Entity sets: PX_Data_Maintenance_SM_DAC_SMLicenseStatistic

PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.InstallationID : Edm.String
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.Date : Edm.DateTimeOffset [key]
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.MonthYear : Edm.DateTimeOffset
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.CommerceTranCount : Edm.Int32
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.ERPTranCount : Edm.Int32
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.MaxAPIRate : Edm.Int32 "Peak Number of Web Services API Requests per Minute"
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.TotalAPIRequestsCount : Edm.Int32 "Total Number of Web Services API Requests"
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.RejectedAPICount : Edm.Int32 "Nbr. of Declined Web Services API Requests"
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.RejectedAPILoginCount : Edm.Int32 "Number of Declined API Login Requests"
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.ThrottledAPIConcurrencyCount : Edm.Int32 "Number of Delayed Web Services API Requests Due to License Concurrent Limit"
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.ThrottledAPICount : Edm.Int32 "Number of Delayed Web Services API Requests Due to License per Minute Limit"
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.ThrottledAPIHighFreqCount : Edm.Int32 "Number of Delayed Web Services API Requests Due to ApiPauseThreshold"
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.LoadDay : Edm.Int32 "Data Load Mode"
PX.Data.Maintenance.SM.DAC.SMLicenseStatistic.Signature : Edm.String

# PX.Data.Maintenance.SM.DAC.ThemeVariables (EntityType)

Key: EntityNoteID, Theme, VariableName
Entity sets: PX_Data_Maintenance_SM_DAC_ThemeVariables

PX.Data.Maintenance.SM.DAC.ThemeVariables.EntityNoteID : Edm.Guid [key]
PX.Data.Maintenance.SM.DAC.ThemeVariables.Theme : Edm.String [key]
PX.Data.Maintenance.SM.DAC.ThemeVariables.VariableName : Edm.String [key]
PX.Data.Maintenance.SM.DAC.ThemeVariables.Value : Edm.String

# PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule (EntityType)

Label: "Notification Schedule"
Key: NotificationID, ScheduleID
Entity sets: PX_Data_Maintenance_SM_SendRecurringNotifications_NotificationSchedule, NotificationSchedule
Non-filterable, non-selectable: ScheduleNoteID

PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule.NotificationID : Edm.Int32 [key] "Notification ID"
PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule.ScheduleID : Edm.Int32 [key] "Schedule ID"
PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule.IsActive : Edm.Boolean "Active"
PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule.ScheduleNoteID : Edm.Guid
PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule.NotificationByNotificationID -> PX.SM.Notification (NotificationID=NotificationID)
PX.Data.Maintenance.SM.SendRecurringNotifications.NotificationSchedule.AUScheduleByScheduleID -> PX.SM.AUSchedule (ScheduleID=ScheduleID)

# PX.Data.Maintenance.TenantOperations.TenantOperationHistory (EntityType)

Label: "Tenant Operation History"
Key: Id
Entity sets: PX_Data_Maintenance_TenantOperations_TenantOperationHistory, TenantOperationHistory
Non-filterable, non-selectable: SourceCompanyName, TargetCompanyName

PX.Data.Maintenance.TenantOperations.TenantOperationHistory.Id : Edm.Guid [key] "ID"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.Operation : Edm.String "Operation"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.Status : Edm.String "Status"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.CommandsTotal : Edm.Int32
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.CommandsExecuted : Edm.Int32
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.SnapshotName : Edm.String "Snapshot Name"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.ExportMode : Edm.String "Export Mode"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.SourceCompany : Edm.Int32 "Source Tenant"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.SourceCompanyName : Edm.String "Source Tenant"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.TargetCompany : Edm.Int32 "Target Tenant"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.TargetCompanyName : Edm.String "Target Tenant"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.OperationStarted : Edm.DateTimeOffset "Operation Started"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.OperationCompleted : Edm.DateTimeOffset "Operation Completed"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.Error : Edm.String "Message"
PX.Data.Maintenance.TenantOperations.TenantOperationHistory.Progress : Edm.Decimal "Progress"

# PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion (EntityType)

Label: "Tenant or Snapshot Deletion"
Key: SnapshotId, TenantId
Entity sets: PX_Data_Maintenance_TenantShapshotDeletion_DAC_TenantSnapshotDeletion, TenantorSnapshotDeletion, TenantSnapshotDeletion
Non-filterable, non-selectable: NoteText, Type, SizeMB, SnapshotName, Description, Visibility, CreatedOn, Version, ExportMode, SourceCompany, TenantName, Status

PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.Id : Edm.Guid "ID"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.TenantId : Edm.Int32 [key] "Tenant ID"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.SnapshotId : Edm.Guid [key] "Snapshot ID"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.DeletionStatus : Edm.String "Deletion Status"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.DeletionProgress : Edm.String "Deletion Progress"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.DeletionHeartbeat : Edm.DateTimeOffset "Deletion Heartbeat"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.NoteID : Edm.Guid
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.NoteText : Edm.String "Note Text"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.Type : Edm.Int32 "Type"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.SizeMB : Edm.Decimal "Size on Disk (MB)"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.SnapshotName : Edm.String "Snapshot Name"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.Description : Edm.String "Description"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.Visibility : Edm.String "Visibility"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.CreatedOn : Edm.DateTimeOffset "Created On"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.Version : Edm.String "Version"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.ExportMode : Edm.String "Export Mode"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.SourceCompany : Edm.Int32
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.TenantName : Edm.String "Tenant Name"
PX.Data.Maintenance.TenantShapshotDeletion.DAC.TenantSnapshotDeletion.Status : Edm.String "Status"

# PX.Data.Note (EntityType)

Label: "Note"
Key: NoteID
Entity sets: PX_Data_Note, Note
Non-filterable, non-selectable: EntityName

PX.Data.Note.NoteID : Edm.Guid [key] "NoteID"
PX.Data.Note.NoteText : Edm.String "NoteText"
PX.Data.Note.EntityType : Edm.String "EntityType"
PX.Data.Note.GraphType : Edm.String
PX.Data.Note.ExternalKey : Edm.String "ExternalKey"
PX.Data.Note.NotePopupText : Edm.String "NoteText"
PX.Data.Note.EntityName : Edm.String "EntityName"

# PX.Data.NoteDoc (EntityType)

Key: FileID, NoteID
Entity sets: PX_Data_NoteDoc
Non-filterable, non-selectable: EntityType, EntityName, EntityRowValues

PX.Data.NoteDoc.NoteID : Edm.Guid [key]
PX.Data.NoteDoc.FileID : Edm.Guid [key]
PX.Data.NoteDoc.EntityType : Edm.String
PX.Data.NoteDoc.EntityName : Edm.String "Entity"
PX.Data.NoteDoc.EntityRowValues : Edm.String "Row Values"

# PX.Data.NoteDoc2 (EntityType)

BaseType: PX.Data.NoteDoc
Key: FileID, NoteID (inherited from PX.Data.NoteDoc)
Entity sets: PX_Data_NoteDoc2

# PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory (EntityType)

Label: "Workflow Category"
Key: CategoryName, ScreenID
Entity sets: PX_Data_ProjectDefinition_Workflow_AUWorkflowCategory, WorkflowCategory, AUWorkflowCategory

PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.IsActive : Edm.Boolean "Active"
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.IsSystem : Edm.Boolean "System"
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.ScreenID : Edm.String [key] "Screen"
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.CategoryName : Edm.String [key] "Action Name"
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.DisplayName : Edm.String "Display Name"
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.Placement : Edm.Byte
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.After : Edm.String
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.PlacementCustomized : Edm.Boolean
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.AfterCustomized : Edm.Boolean
PX.Data.ProjectDefinition.Workflow.AUWorkflowCategory.DisplayNameCustomized : Edm.Boolean

# PX.Data.Reports.UserReport (EntityType)

Key: ReportFileName, Version
Entity sets: PX_Data_Reports_UserReport

PX.Data.Reports.UserReport.ReportFileName : Edm.String [key] "ReportFileName"
PX.Data.Reports.UserReport.Version : Edm.Int32 [key] "Version"
PX.Data.Reports.UserReport.Description : Edm.String "Description"
PX.Data.Reports.UserReport.DateCreated : Edm.DateTimeOffset "Created"
PX.Data.Reports.UserReport.IsActive : Edm.Boolean "Active"
PX.Data.Reports.UserReport.Xml : Edm.String "Xml"
PX.Data.Reports.UserReport.CreatedByID : Edm.Guid "Created By"
PX.Data.Reports.UserReport.CreatedByScreenID : Edm.String
PX.Data.Reports.UserReport.CreatedDateTime : Edm.DateTimeOffset
PX.Data.Reports.UserReport.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Reports.UserReport.LastModifiedByScreenID : Edm.String
PX.Data.Reports.UserReport.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Reports.UserReport.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Reports.UserReport.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Data.Reports.UserReportHeader (EntityType)

BaseType: PX.Data.Reports.UserReport
Key: ReportFileName, Version (inherited from PX.Data.Reports.UserReport)
Entity sets: PX_Data_Reports_UserReportHeader

# PX.Data.RichTextEdit.RichFileRevision (EntityType)

BaseType: PX.SM.UploadFileRevision
Key: FileID, FileRevisionID (inherited from PX.SM.UploadFileRevision)
Entity sets: PX_Data_RichTextEdit_RichFileRevision

# PX.Data.RichTextEdit.WikiPage2 (EntityType)

Key: PageID
Entity sets: PX_Data_RichTextEdit_WikiPage2

PX.Data.RichTextEdit.WikiPage2.PageID : Edm.Guid [key] "PageID"
PX.Data.RichTextEdit.WikiPage2.Title : Edm.String "Name"
PX.Data.RichTextEdit.WikiPage2.ParentUID : Edm.Guid "Parent Folder"
PX.Data.RichTextEdit.WikiPage2.CreatedDateTime : Edm.DateTimeOffset "Created at"
PX.Data.RichTextEdit.WikiPage2.WikiArticleCollection -> Collection(PX.SM.WikiArticle)
PX.Data.RichTextEdit.WikiPage2.PreferencesGeneralCollection -> Collection(PX.SM.PreferencesGeneral)
PX.Data.RichTextEdit.WikiPage2.KBResponseCollection -> Collection(PX.SM.KBResponse)
PX.Data.RichTextEdit.WikiPage2.KBResponseSummaryCollection -> Collection(PX.SM.KBResponseSummary)

# PX.Data.RichTextEdit.WikiPageParent (EntityType)

BaseType: PX.Data.RichTextEdit.WikiPage2
Key: PageID (inherited from PX.Data.RichTextEdit.WikiPage2)
Entity sets: PX_Data_RichTextEdit_WikiPageParent

# PX.Data.Search.SPWikiCategory (EntityType)

Key: CategoryID
Entity sets: PX_Data_Search_SPWikiCategory

PX.Data.Search.SPWikiCategory.CategoryID : Edm.String [key] "Category ID"
PX.Data.Search.SPWikiCategory.Description : Edm.String "Category Name"
PX.Data.Search.SPWikiCategory.tstamp : Edm.Binary
PX.Data.Search.SPWikiCategory.CreatedByID : Edm.Guid "Created By"
PX.Data.Search.SPWikiCategory.CreatedByScreenID : Edm.String
PX.Data.Search.SPWikiCategory.CreatedDateTime : Edm.DateTimeOffset
PX.Data.Search.SPWikiCategory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Search.SPWikiCategory.LastModifiedByScreenID : Edm.String
PX.Data.Search.SPWikiCategory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Search.SPWikiCategory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Search.SPWikiCategory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Search.SPWikiCategory.SPWikiCategoryTagsCollection -> Collection(PX.Data.Search.SPWikiCategoryTags)

# PX.Data.Search.SPWikiCategoryTags (EntityType)

Key: CategoryID, PageID
Entity sets: PX_Data_Search_SPWikiCategoryTags

PX.Data.Search.SPWikiCategoryTags.CategoryID : Edm.String [key] "Category ID"
PX.Data.Search.SPWikiCategoryTags.PageID : Edm.Guid [key] "PageID"
PX.Data.Search.SPWikiCategoryTags.PageName : Edm.String "Article ID"
PX.Data.Search.SPWikiCategoryTags.PageTitle : Edm.String "Name"
PX.Data.Search.SPWikiCategoryTags.tstamp : Edm.Binary
PX.Data.Search.SPWikiCategoryTags.CreatedByID : Edm.Guid "Created By"
PX.Data.Search.SPWikiCategoryTags.CreatedByScreenID : Edm.String
PX.Data.Search.SPWikiCategoryTags.CreatedDateTime : Edm.DateTimeOffset
PX.Data.Search.SPWikiCategoryTags.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Search.SPWikiCategoryTags.LastModifiedByScreenID : Edm.String
PX.Data.Search.SPWikiCategoryTags.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Search.SPWikiCategoryTags.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Search.SPWikiCategoryTags.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Search.SPWikiCategoryTags.SPWikiCategoryByCategoryID -> PX.Data.Search.SPWikiCategory (CategoryID=CategoryID)

# PX.Data.Search.SPWikiProduct (EntityType)

Key: ProductID
Entity sets: PX_Data_Search_SPWikiProduct

PX.Data.Search.SPWikiProduct.ProductID : Edm.String [key] "Product ID"
PX.Data.Search.SPWikiProduct.Description : Edm.String "Product Name"
PX.Data.Search.SPWikiProduct.tstamp : Edm.Binary
PX.Data.Search.SPWikiProduct.CreatedByID : Edm.Guid "Created By"
PX.Data.Search.SPWikiProduct.CreatedByScreenID : Edm.String
PX.Data.Search.SPWikiProduct.CreatedDateTime : Edm.DateTimeOffset
PX.Data.Search.SPWikiProduct.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Search.SPWikiProduct.LastModifiedByScreenID : Edm.String
PX.Data.Search.SPWikiProduct.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Search.SPWikiProduct.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Search.SPWikiProduct.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Search.SPWikiProduct.SPWikiProductTagsCollection -> Collection(PX.Data.Search.SPWikiProductTags)

# PX.Data.Search.SPWikiProductTags (EntityType)

Key: PageID, ProductID
Entity sets: PX_Data_Search_SPWikiProductTags

PX.Data.Search.SPWikiProductTags.ProductID : Edm.String [key] "Product ID"
PX.Data.Search.SPWikiProductTags.PageID : Edm.Guid [key] "PageID"
PX.Data.Search.SPWikiProductTags.PageName : Edm.String "Article ID"
PX.Data.Search.SPWikiProductTags.PageTitle : Edm.String "Name"
PX.Data.Search.SPWikiProductTags.tstamp : Edm.Binary
PX.Data.Search.SPWikiProductTags.CreatedByID : Edm.Guid "Created By"
PX.Data.Search.SPWikiProductTags.CreatedByScreenID : Edm.String
PX.Data.Search.SPWikiProductTags.CreatedDateTime : Edm.DateTimeOffset
PX.Data.Search.SPWikiProductTags.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Search.SPWikiProductTags.LastModifiedByScreenID : Edm.String
PX.Data.Search.SPWikiProductTags.LastModifiedDateTime : Edm.DateTimeOffset
PX.Data.Search.SPWikiProductTags.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Search.SPWikiProductTags.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Search.SPWikiProductTags.SPWikiProductByProductID -> PX.Data.Search.SPWikiProduct (ProductID=ProductID)

# PX.Data.SearchIndex (EntityType)

Label: "Search Index"
Key: NoteID
Entity sets: PX_Data_SearchIndex, SearchIndex
Non-filterable, non-selectable: Top

PX.Data.SearchIndex.NoteID : Edm.Guid [key]
PX.Data.SearchIndex.IndexID : Edm.Guid
PX.Data.SearchIndex.Category : Edm.Int32
PX.Data.SearchIndex.Content : Edm.String
PX.Data.SearchIndex.EntityType : Edm.String
PX.Data.SearchIndex.tstamp : Edm.Binary
PX.Data.SearchIndex.Top : Edm.Int32

# PX.Data.Services.Implementations.FavoriteActionRecord (EntityType)

Label: "Favorite Action"
Key: ActionName, IsPortal, ScreenID, UserID
Entity sets: PX_Data_Services_Implementations_FavoriteActionRecord, FavoriteAction, FavoriteActionRecord

PX.Data.Services.Implementations.FavoriteActionRecord.IsPortal : Edm.Boolean [key]
PX.Data.Services.Implementations.FavoriteActionRecord.ScreenID : Edm.String [key]
PX.Data.Services.Implementations.FavoriteActionRecord.ActionName : Edm.String [key] "Action Name"
PX.Data.Services.Implementations.FavoriteActionRecord.UserID : Edm.Guid [key] "User ID"
PX.Data.Services.Implementations.FavoriteActionRecord.CreatedByScreenID : Edm.String
PX.Data.Services.Implementations.FavoriteActionRecord.CreatedDateTime : Edm.DateTimeOffset "Created On"

# PX.Data.SystemColor (EntityType)

Key: ColorName
Entity sets: PX_Data_SystemColor

PX.Data.SystemColor.ColorID : Edm.Int32
PX.Data.SystemColor.ColorName : Edm.String [key] "Name"
PX.Data.SystemColor.ColorValue : Edm.Int32 "RGB"

# PX.Data.Update.Company (EntityType)

Singletons: PX_Data_Update_Company

PX.Data.Update.Company.CurrencyByBaseCuryID -> PX.Objects.CM.Currency
PX.Data.Update.Company.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList

# PX.Data.Update.UPMeasureEndpoint (EntityType)

Key: EndpointID
Entity sets: PX_Data_Update_UPMeasureEndpoint

PX.Data.Update.UPMeasureEndpoint.EndpointID : Edm.String [key] "Session ID"
PX.Data.Update.UPMeasureEndpoint.Url : Edm.String "Destination URL"
PX.Data.Update.UPMeasureEndpoint.Login : Edm.String "User Name"
PX.Data.Update.UPMeasureEndpoint.Password : Edm.String "Password"
PX.Data.Update.UPMeasureEndpoint.Screen : Edm.String "Form Name"
PX.Data.Update.UPMeasureEndpoint.Action : Edm.String "Operation"
PX.Data.Update.UPMeasureEndpoint.Count : Edm.Int32 [required] "Measurements"

# PX.Data.Update.UPMeasureHistory (EntityType)

Key: EndpointID, MeasureID
Entity sets: PX_Data_Update_UPMeasureHistory
Non-filterable, non-selectable: DateOnly, TimeOnly

PX.Data.Update.UPMeasureHistory.EndpointID : Edm.String [key] "Endpoint ID"
PX.Data.Update.UPMeasureHistory.MeasureID : Edm.Int32 [key] "Measure ID"
PX.Data.Update.UPMeasureHistory.Date : Edm.DateTimeOffset "Date"
PX.Data.Update.UPMeasureHistory.NetworkTime : Edm.Int32 "Response Time, ms"
PX.Data.Update.UPMeasureHistory.OperationTime : Edm.Int32 "Operation Time, ms"
PX.Data.Update.UPMeasureHistory.UsersCount : Edm.Int32 "User Count"
PX.Data.Update.UPMeasureHistory.DateOnly : Edm.DateTimeOffset "Date"
PX.Data.Update.UPMeasureHistory.TimeOnly : Edm.Int32 "Time"

# PX.Data.Update.UPSelectedEndpoint (EntityType)

BaseType: PX.Data.Update.UPMeasureEndpoint
Key: EndpointID (inherited from PX.Data.Update.UPMeasureEndpoint)
Entity sets: PX_Data_Update_UPSelectedEndpoint

# PX.Data.UserRecords.FavoriteRecords.FavoriteRecord (EntityType)

Label: "Favorite Record"
Key: EntityType, IsPortal, RefNoteId, UserID
Entity sets: PX_Data_UserRecords_FavoriteRecords_FavoriteRecord, FavoriteRecord

PX.Data.UserRecords.FavoriteRecords.FavoriteRecord.IsPortal : Edm.Boolean [key]
PX.Data.UserRecords.FavoriteRecords.FavoriteRecord.RefNoteId : Edm.Guid [key] "Record Note ID"
PX.Data.UserRecords.FavoriteRecords.FavoriteRecord.EntityType : Edm.String [key]
PX.Data.UserRecords.FavoriteRecords.FavoriteRecord.UserID : Edm.Guid [key] "User ID"
PX.Data.UserRecords.FavoriteRecords.FavoriteRecord.RecordContent : Edm.String
PX.Data.UserRecords.FavoriteRecords.FavoriteRecord.CreatedByScreenID : Edm.String
PX.Data.UserRecords.FavoriteRecords.FavoriteRecord.CreatedDateTime : Edm.DateTimeOffset "Created On"

# PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord (EntityType)

Label: "Viewed Record"
Key: EntityType, IsPortal, RefNoteId, UserID
Entity sets: PX_Data_UserRecords_RecentlyVisitedRecords_VisitedRecord, ViewedRecord, VisitedRecord

PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.IsPortal : Edm.Boolean [key]
PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.UserID : Edm.Guid [key] "User ID"
PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.RefNoteId : Edm.Guid [key] "Record Note ID"
PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.EntityType : Edm.String [key]
PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.VisitCount : Edm.Int32 "Visit Count"
PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.RecordContent : Edm.String
PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.CreatedByScreenID : Edm.String
PX.Data.UserRecords.RecentlyVisitedRecords.VisitedRecord.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"

# PX.Data.Wiki.Tags.RoleInTag (EntityType)

Label: "Roles In Tag"
Key: Rolename, TagID
Entity sets: PX_Data_Wiki_Tags_RoleInTag, RolesInTag, RoleInTag

PX.Data.Wiki.Tags.RoleInTag.TagID : Edm.Guid [key]
PX.Data.Wiki.Tags.RoleInTag.Rolename : Edm.String [key]
PX.Data.Wiki.Tags.RoleInTag.AccessRights : Edm.Int16 [required]
PX.Data.Wiki.Tags.RoleInTag.CreatedByID : Edm.Guid "Created By"
PX.Data.Wiki.Tags.RoleInTag.CreatedByScreenID : Edm.String
PX.Data.Wiki.Tags.RoleInTag.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Data.Wiki.Tags.RoleInTag.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Wiki.Tags.RoleInTag.LastModifiedByScreenID : Edm.String
PX.Data.Wiki.Tags.RoleInTag.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Data.Wiki.Tags.RoleInTag.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Wiki.Tags.RoleInTag.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Wiki.Tags.RoleInTag.RolesByRolename -> PX.SM.Roles (Rolename=Rolename)
PX.Data.Wiki.Tags.RoleInTag.TagByTagID -> PX.Data.Wiki.Tags.Tag (TagID=TagID)

# PX.Data.Wiki.Tags.Tag (EntityType)

Label: "Tag"
Key: TagID
Entity sets: PX_Data_Wiki_Tags_Tag, Tag
Non-filterable, non-selectable: NoteText

PX.Data.Wiki.Tags.Tag.TagID : Edm.Guid [key]
PX.Data.Wiki.Tags.Tag.TagCD : Edm.String "Tag Name"
PX.Data.Wiki.Tags.Tag.Description : Edm.String "Description"
PX.Data.Wiki.Tags.Tag.NoteID : Edm.Guid
PX.Data.Wiki.Tags.Tag.NoteText : Edm.String "Note Text"
PX.Data.Wiki.Tags.Tag.tstamp : Edm.Binary
PX.Data.Wiki.Tags.Tag.CreatedByID : Edm.Guid "Created By"
PX.Data.Wiki.Tags.Tag.CreatedByScreenID : Edm.String
PX.Data.Wiki.Tags.Tag.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Data.Wiki.Tags.Tag.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Wiki.Tags.Tag.LastModifiedByScreenID : Edm.String
PX.Data.Wiki.Tags.Tag.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Data.Wiki.Tags.Tag.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Wiki.Tags.Tag.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Data.Wiki.Tags.Tag.RoleInTagCollection -> Collection(PX.Data.Wiki.Tags.RoleInTag)

# PX.Data.Wiki.Tags.UploadFileTag (EntityType)

Label: "File Tag"
Key: FileID, TagID
Entity sets: PX_Data_Wiki_Tags_UploadFileTag, FileTag, UploadFileTag

PX.Data.Wiki.Tags.UploadFileTag.FileID : Edm.Guid [key] "File ID"
PX.Data.Wiki.Tags.UploadFileTag.TagID : Edm.Guid [key]
PX.Data.Wiki.Tags.UploadFileTag.CreatedByID : Edm.Guid "Created By"
PX.Data.Wiki.Tags.UploadFileTag.CreatedByScreenID : Edm.String
PX.Data.Wiki.Tags.UploadFileTag.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Data.Wiki.Tags.UploadFileTag.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Data.Wiki.Tags.UploadFileTag.LastModifiedByScreenID : Edm.String
PX.Data.Wiki.Tags.UploadFileTag.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Data.Wiki.Tags.UploadFileTag.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Data.Wiki.Tags.UploadFileTag.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.DataSync.HubSpot.HSEntitySetup (EntityType)

Key: EntityType
Entity sets: PX_DataSync_HubSpot_HSEntitySetup
Non-filterable, non-selectable: SyncProcessStatus, NoteText

PX.DataSync.HubSpot.HSEntitySetup.EntityType : Edm.Int32 [key] "Entity"
PX.DataSync.HubSpot.HSEntitySetup.ImportScenario : Edm.Guid "Import Scenario"
PX.DataSync.HubSpot.HSEntitySetup.ExportScenario : Edm.Guid "Export Scenario"
PX.DataSync.HubSpot.HSEntitySetup.SyncProcessStatus : Edm.Int32 "Status"
PX.DataSync.HubSpot.HSEntitySetup.MasterSource : Edm.Int32 "Master Source"
PX.DataSync.HubSpot.HSEntitySetup.LastRealTimeDateTime : Edm.DateTimeOffset "Latest RealTime Attempt"
PX.DataSync.HubSpot.HSEntitySetup.LastFullSyncDateTime : Edm.DateTimeOffset "Latest Full Data Resync Attempt"
PX.DataSync.HubSpot.HSEntitySetup.LastMissedSyncDateTime : Edm.DateTimeOffset "Latest Failed & Missed Data Resync Attempt"
PX.DataSync.HubSpot.HSEntitySetup.MaxAttemptCount : Edm.Int32 [required] "Number of Attempts"
PX.DataSync.HubSpot.HSEntitySetup.PoolingPeriod : Edm.Int32 [required] "Polling Period, sec"
PX.DataSync.HubSpot.HSEntitySetup.SyncSortOrder : Edm.Int32 [required] "Sync Order"
PX.DataSync.HubSpot.HSEntitySetup.LegacyAPI : Edm.Boolean [required] "Legacy API"
PX.DataSync.HubSpot.HSEntitySetup.NoteID : Edm.Guid "NoteID"
PX.DataSync.HubSpot.HSEntitySetup.NoteText : Edm.String "Note Text"
PX.DataSync.HubSpot.HSEntitySetup.CreatedByID : Edm.Guid "Created By"
PX.DataSync.HubSpot.HSEntitySetup.CreatedByScreenID : Edm.String
PX.DataSync.HubSpot.HSEntitySetup.CreatedDateTime : Edm.DateTimeOffset "Created Date"
PX.DataSync.HubSpot.HSEntitySetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.DataSync.HubSpot.HSEntitySetup.LastModifiedByScreenID : Edm.String
PX.DataSync.HubSpot.HSEntitySetup.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date"
PX.DataSync.HubSpot.HSEntitySetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.DataSync.HubSpot.HSEntitySetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.DataSync.HubSpot.HSEntitySetup.SYMappingByImportScenario -> PX.Api.SYMapping (ImportScenario=MappingID)
PX.DataSync.HubSpot.HSEntitySetup.SYMappingByExportScenario -> PX.Api.SYMapping (ExportScenario=MappingID)

# PX.DataSync.HubSpot.HSMarketingListMember (EntityType)

Key: MarketingListMemberID
Entity sets: PX_DataSync_HubSpot_HSMarketingListMember

PX.DataSync.HubSpot.HSMarketingListMember.MarketingListMemberID : Edm.Int32 [key] "ID"
PX.DataSync.HubSpot.HSMarketingListMember.MarketingListID : Edm.Int32 "Marketing List ID"
PX.DataSync.HubSpot.HSMarketingListMember.LocalID : Edm.Int32 "Document"
PX.DataSync.HubSpot.HSMarketingListMember.LocalNoteID : Edm.Guid
PX.DataSync.HubSpot.HSMarketingListMember.IsSubscribed : Edm.Boolean "Subscribed"
PX.DataSync.HubSpot.HSMarketingListMember.RemoteID : Edm.Int64 "Remote ID"
PX.DataSync.HubSpot.HSMarketingListMember.RemoteName : Edm.String "Ext. Ref."
PX.DataSync.HubSpot.HSMarketingListMember.Error : Edm.String "Error"
PX.DataSync.HubSpot.HSMarketingListMember.MembershipSyncStatus : Edm.Int32 "Membership Sync Status"
PX.DataSync.HubSpot.HSMarketingListMember.CreatedByID : Edm.Guid "Created By"
PX.DataSync.HubSpot.HSMarketingListMember.CreatedByScreenID : Edm.String
PX.DataSync.HubSpot.HSMarketingListMember.CreatedDateTime : Edm.DateTimeOffset "Created Date"
PX.DataSync.HubSpot.HSMarketingListMember.LastModifiedByID : Edm.Guid "Last Modified By"
PX.DataSync.HubSpot.HSMarketingListMember.LastModifiedByScreenID : Edm.String
PX.DataSync.HubSpot.HSMarketingListMember.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date"
PX.DataSync.HubSpot.HSMarketingListMember.ContactByLocalID -> PX.Objects.CR.Contact (LocalID=ContactID)
PX.DataSync.HubSpot.HSMarketingListMember.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.DataSync.HubSpot.HSMarketingListMember.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.DataSync.SendGrid.SMSendGridAccountsSettings (EntityType)

Label: "SendGrid Accounts Settings"
BaseType: PX.DataSync.SendGrid.SMSendGridSettings
Key: SendGridConnectionID (inherited from PX.DataSync.SendGrid.SMSendGridSettings)
Entity sets: PX_DataSync_SendGrid_SMSendGridAccountsSettings, SendGridAccountsSettings, SMSendGridAccountsSettings

PX.DataSync.SendGrid.SMSendGridAccountsSettings.EmailAccountID : Edm.Int32 "Email Address"
PX.DataSync.SendGrid.SMSendGridAccountsSettings.EmailAccountName : Edm.String "Account Name"
PX.DataSync.SendGrid.SMSendGridAccountsSettings.EmailAccountAddress : Edm.String "Email Address"
PX.DataSync.SendGrid.SMSendGridAccountsSettings.IsEmailAccountActive : Edm.Boolean "Active"
PX.DataSync.SendGrid.SMSendGridAccountsSettings.NotificationByResponseNotificationID -> PX.SM.Notification
PX.DataSync.SendGrid.SMSendGridAccountsSettings.NotificationByConfirmReceiptNotificationID -> PX.SM.Notification
PX.DataSync.SendGrid.SMSendGridAccountsSettings.WikiNotificationTemplateCollection -> Collection(PX.SM.WikiNotificationTemplate)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.CRContactClassCollection -> Collection(PX.Objects.CR.CRContactClass)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.CRCustomerClassCollection -> Collection(PX.Objects.CR.CRCustomerClass)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.CRLeadClassCollection -> Collection(PX.Objects.CR.CRLeadClass)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.CROpportunityClassCollection -> Collection(PX.Objects.CR.CROpportunityClass)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.NotificationCollection -> Collection(PX.SM.Notification)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.PreferencesEmailCollection -> Collection(PX.SM.PreferencesEmail)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.SMEmailCollection -> Collection(PX.Objects.CR.SMEmail)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.NotificationSourceCollection -> Collection(PX.Objects.CS.NotificationSource)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.CRMassMailCollection -> Collection(PX.Objects.CR.CRMassMail)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.EMailSyncAccountCollection -> Collection(PX.SM.EMailSyncAccount)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.EMailAccountStatisticsCollection -> Collection(PX.SM.EMailAccountStatistics)
PX.DataSync.SendGrid.SMSendGridAccountsSettings.EmailLogCollection -> Collection(PX.Mail.Log.DAC.EmailLog)

# PX.DataSync.SendGrid.SMSendGridRecipient (EntityType)

Label: "SendGrid Recipients"
Key: Address, RefNoteID
Entity sets: PX_DataSync_SendGrid_SMSendGridRecipient, SendGridRecipients, SMSendGridRecipient
Non-filterable, non-selectable: Name

PX.DataSync.SendGrid.SMSendGridRecipient.RefNoteID : Edm.Guid [key] "Email Note ID"
PX.DataSync.SendGrid.SMSendGridRecipient.Address : Edm.String [key] "Email Address"
PX.DataSync.SendGrid.SMSendGridRecipient.Name : Edm.String "Name"
PX.DataSync.SendGrid.SMSendGridRecipient.Status : Edm.Int32 "Delivery Status"
PX.DataSync.SendGrid.SMSendGridRecipient.OpenedCount : Edm.Int32 [required] "Opened"
PX.DataSync.SendGrid.SMSendGridRecipient.ClickedCount : Edm.Int32 [required] "Clicked"
PX.DataSync.SendGrid.SMSendGridRecipient.ReportedAsSpamCount : Edm.Int32 [required] "Reported as Spam"
PX.DataSync.SendGrid.SMSendGridRecipient.OptedOutCount : Edm.Int32 [required] "Opted Out"
PX.DataSync.SendGrid.SMSendGridRecipient.MailServiceReply : Edm.String "Mail Service Reply"
PX.DataSync.SendGrid.SMSendGridRecipient.SendGridMessageId : Edm.String "SendGrid Message ID"
PX.DataSync.SendGrid.SMSendGridRecipient.SendGridTimestamp : Edm.DateTimeOffset "SendGrid Timestamp"
PX.DataSync.SendGrid.SMSendGridRecipient.LastModifiedDateTime : Edm.DateTimeOffset "Last Event Received On"
PX.DataSync.SendGrid.SMSendGridRecipient.CRSMEmailByRefNoteID -> PX.Objects.CR.CRSMEmail (RefNoteID=NoteID)
PX.DataSync.SendGrid.SMSendGridRecipient.SMEmailByRefNoteID -> PX.Objects.CR.SMEmail (RefNoteID=RefNoteID)

# PX.DataSync.SendGrid.SMSendGridSettings (EntityType)

Label: "SendGrid Settings"
Key: SendGridConnectionID
Entity sets: PX_DataSync_SendGrid_SMSendGridSettings, SendGridSettings, SMSendGridSettings
Non-filterable, non-selectable: SendGridApiUrl, EnableWebhooks

PX.DataSync.SendGrid.SMSendGridSettings.SendGridConnectionID : Edm.Guid [key] "SendGrid Connection"
PX.DataSync.SendGrid.SMSendGridSettings.Description : Edm.String "Description"
PX.DataSync.SendGrid.SMSendGridSettings.IsActive : Edm.Boolean [required] "Active"
PX.DataSync.SendGrid.SMSendGridSettings.IsInitialized : Edm.Boolean [required] "Initialized"
PX.DataSync.SendGrid.SMSendGridSettings.SendGridApiUrl : Edm.String "SendGrid API URL"
PX.DataSync.SendGrid.SMSendGridSettings.ApiKey : Edm.String "API Key"
PX.DataSync.SendGrid.SMSendGridSettings.ApiKeyScopes : Edm.String
PX.DataSync.SendGrid.SMSendGridSettings.ApiKeyName : Edm.String "API Key Name"
PX.DataSync.SendGrid.SMSendGridSettings.PublicKey : Edm.String "Public Key"
PX.DataSync.SendGrid.SMSendGridSettings.Categories : Edm.String "Email Categories"
PX.DataSync.SendGrid.SMSendGridSettings.TrackEmailOpens : Edm.Boolean [required] "TrackEmailOpens"
PX.DataSync.SendGrid.SMSendGridSettings.TrackClicksInEmail : Edm.Boolean [required] "TrackClicksInEmail"
PX.DataSync.SendGrid.SMSendGridSettings.EnableWebhooks : Edm.Boolean "Receive SendGrid events via webhooks"
PX.DataSync.SendGrid.SMSendGridSettings.WebhookID : Edm.Guid "Webhook ID"
PX.DataSync.SendGrid.SMSendGridSettings.WebhookUrl : Edm.String "URL of the webhook registered in Acumatica ERP"
PX.DataSync.SendGrid.SMSendGridSettings.ProcessedEvent : Edm.Boolean [required] "ProcessedEvent"
PX.DataSync.SendGrid.SMSendGridSettings.DeferredEvent : Edm.Boolean [required] "DeferredEvent"
PX.DataSync.SendGrid.SMSendGridSettings.DeliveredEvent : Edm.Boolean [required] "DeliveredEvent"
PX.DataSync.SendGrid.SMSendGridSettings.DroppedEvent : Edm.Boolean [required] "DroppedEvent"
PX.DataSync.SendGrid.SMSendGridSettings.BouncedEvent : Edm.Boolean [required] "BouncedEvent"
PX.DataSync.SendGrid.SMSendGridSettings.OpenEvent : Edm.Boolean [required] "OpenEvent"
PX.DataSync.SendGrid.SMSendGridSettings.ClickEvent : Edm.Boolean [required] "ClickEvent"
PX.DataSync.SendGrid.SMSendGridSettings.SpamReportEvent : Edm.Boolean [required] "SpamReportEvent"
PX.DataSync.SendGrid.SMSendGridSettings.UnsubscribeEvent : Edm.Boolean [required] "UnsubscribeEvent"
PX.DataSync.SendGrid.SMSendGridSettings.GroupUnsubscribeEvent : Edm.Boolean [required] "Group Unsubscribes"
PX.DataSync.SendGrid.SMSendGridSettings.GroupResubscribeEvent : Edm.Boolean [required] "Group Resubscribes"
PX.DataSync.SendGrid.SMSendGridSettings.WebHookByWebhookID -> PX.Api.Webhooks.DAC.WebHook (WebhookID=WebHookID)
PX.DataSync.SendGrid.SMSendGridSettings.SMSendGridSuppressionGroupCollection -> Collection(PX.DataSync.SendGrid.SMSendGridSuppressionGroup)

# PX.DataSync.SendGrid.SMSendGridSuppressionGroup (EntityType)

Label: "SendGrid Suppression Group"
Key: GroupID, SendGridConnectionID
Entity sets: PX_DataSync_SendGrid_SMSendGridSuppressionGroup, SendGridSuppressionGroup, SMSendGridSuppressionGroup

PX.DataSync.SendGrid.SMSendGridSuppressionGroup.SendGridConnectionID : Edm.Guid [key] "SendGrid Connection"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.GroupID : Edm.Int32 [key] "Unsubscribe Group ID"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.GroupName : Edm.String "Unsubscribe Group Name"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.MarketingCategoryID : Edm.String "Mapped Marketing Category"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.IsActive : Edm.Boolean [required] "Mapping is Active"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.SyncStatus : Edm.String "Sync Status"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.LastSyncedDate : Edm.DateTimeOffset "Last Synced Date"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.SyncError : Edm.String "Sync Failed"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.CreatedByID : Edm.Guid "Created By"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.CreatedByScreenID : Edm.String
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.CreatedDateTime : Edm.DateTimeOffset
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.LastModifiedByScreenID : Edm.String
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.LastModifiedDateTime : Edm.DateTimeOffset
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.tstamp : Edm.Binary
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.CRMarketingCategoryByMarketingCategoryID -> PX.Objects.CR.CRMarketingCategory (MarketingCategoryID=MarketingCategoryID)
PX.DataSync.SendGrid.SMSendGridSuppressionGroup.SMSendGridSettingsBySendGridConnectionID -> PX.DataSync.SendGrid.SMSendGridSettings (SendGridConnectionID=SendGridConnectionID)

# PX.EP.EPLoginType (EntityType)

Label: "Login Type"
Key: LoginTypeID, LoginTypeName
Entity sets: PX_EP_EPLoginType, LoginType, EPLoginType
Non-filterable, non-selectable: IsExternal

PX.EP.EPLoginType.LoginTypeID : Edm.Int32 [key]
PX.EP.EPLoginType.LoginTypeName : Edm.String [key] "User Type"
PX.EP.EPLoginType.Entity : Edm.String "Linked Entity"
PX.EP.EPLoginType.Description : Edm.String "Description"
PX.EP.EPLoginType.IsExternal : Edm.Boolean
PX.EP.EPLoginType.EmailAsLogin : Edm.Boolean [required] "Use Email as Username"
PX.EP.EPLoginType.ResetPasswordOnLogin : Edm.Boolean [required] "Reset Password on First Sign-In"
PX.EP.EPLoginType.RequireLoginActivation : Edm.Boolean [required] "Require Username Activation"
PX.EP.EPLoginType.AllowedLoginType : Edm.String "Allowed Login Type"
PX.EP.EPLoginType.AllowedSessions : Edm.Int32 "Allowed Concurrent Sign-Ins"
PX.EP.EPLoginType.DisableTwoFactorAuth : Edm.Boolean "Turn Off Two-Factor Authentication"
PX.EP.EPLoginType.AllowThisTypeForContacts : Edm.Boolean [required] "Allow Selection of This Type on Contacts Form"
PX.EP.EPLoginType.AllowThisTypeForEmployees : Edm.Boolean [required] "Allow Selection of This Type on Employees Form"
PX.EP.EPLoginType.tstamp : Edm.Binary
PX.EP.EPLoginType.CreatedByID : Edm.Guid "Created By"
PX.EP.EPLoginType.CreatedByScreenID : Edm.String
PX.EP.EPLoginType.CreatedDateTime : Edm.DateTimeOffset
PX.EP.EPLoginType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.EP.EPLoginType.LastModifiedByScreenID : Edm.String
PX.EP.EPLoginType.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.EP.EPLoginType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.EP.EPLoginType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.EP.EPLoginType.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.EP.EPLoginType.EPLoginTypeAllowsRoleCollection -> Collection(PX.EP.EPLoginTypeAllowsRole)
PX.EP.EPLoginType.EPManagedLoginTypeCollection -> Collection(PX.EP.EPManagedLoginType)

# PX.EP.EPLoginTypeAllowsRole (EntityType)

Label: "Login Type Allow Role"
Key: LoginTypeID, Rolename
Entity sets: PX_EP_EPLoginTypeAllowsRole, LoginTypeAllowRole, EPLoginTypeAllowsRole

PX.EP.EPLoginTypeAllowsRole.IsDefault : Edm.Boolean "Assigned by Default"
PX.EP.EPLoginTypeAllowsRole.LoginTypeID : Edm.Int32 [key] "User Type"
PX.EP.EPLoginTypeAllowsRole.Rolename : Edm.String [key] "Role Name"
PX.EP.EPLoginTypeAllowsRole.tstamp : Edm.Binary
PX.EP.EPLoginTypeAllowsRole.CreatedByID : Edm.Guid "Created By"
PX.EP.EPLoginTypeAllowsRole.CreatedByScreenID : Edm.String
PX.EP.EPLoginTypeAllowsRole.CreatedDateTime : Edm.DateTimeOffset
PX.EP.EPLoginTypeAllowsRole.LastModifiedByID : Edm.Guid "Last Modified By"
PX.EP.EPLoginTypeAllowsRole.LastModifiedByScreenID : Edm.String
PX.EP.EPLoginTypeAllowsRole.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.EP.EPLoginTypeAllowsRole.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.EP.EPLoginTypeAllowsRole.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.EP.EPLoginTypeAllowsRole.EPLoginTypeByLoginTypeID -> PX.EP.EPLoginType (LoginTypeID=LoginTypeID)
PX.EP.EPLoginTypeAllowsRole.RolesByRolename -> PX.SM.Roles (Rolename=Rolename)

# PX.EP.EPManagedLoginType (EntityType)

Label: "Login Type Managed"
Key: LoginTypeID, ParentLoginTypeID
Entity sets: PX_EP_EPManagedLoginType, LoginTypeManaged, EPManagedLoginType

PX.EP.EPManagedLoginType.LoginTypeID : Edm.Int32 [key] "User Type"
PX.EP.EPManagedLoginType.ParentLoginTypeID : Edm.Int32 [key] "Parent User Type"
PX.EP.EPManagedLoginType.tstamp : Edm.Binary
PX.EP.EPManagedLoginType.CreatedByID : Edm.Guid "Created By"
PX.EP.EPManagedLoginType.CreatedByScreenID : Edm.String
PX.EP.EPManagedLoginType.CreatedDateTime : Edm.DateTimeOffset
PX.EP.EPManagedLoginType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.EP.EPManagedLoginType.LastModifiedByScreenID : Edm.String
PX.EP.EPManagedLoginType.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.EP.EPManagedLoginType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.EP.EPManagedLoginType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.EP.EPManagedLoginType.EPLoginTypeByLoginTypeID -> PX.EP.EPLoginType (LoginTypeID=LoginTypeID)
PX.EP.EPManagedLoginType.EPLoginTypeByParentLoginTypeID -> PX.EP.EPLoginType (ParentLoginTypeID=LoginTypeID)

# PX.ESign.ESignAccount (EntityType)

Label: "eSign Account"
Key: AccountCD
Entity sets: PX_ESign_ESignAccount, eSignAccount
Non-filterable, non-selectable: ConnectionStatus

PX.ESign.ESignAccount.AccountID : Edm.Int32
PX.ESign.ESignAccount.AccountCD : Edm.String [key] "eSign Account"
PX.ESign.ESignAccount.Type : Edm.String "Type"
PX.ESign.ESignAccount.IsActive : Edm.Boolean [required] "Active"
PX.ESign.ESignAccount.OwnerID : Edm.Guid "Employee"
PX.ESign.ESignAccount.ClientID : Edm.String "Client ID"
PX.ESign.ESignAccount.ClientSecret : Edm.String "Client Secret"
PX.ESign.ESignAccount.ApiUrl : Edm.String "API URL"
PX.ESign.ESignAccount.ApiAccessPoint : Edm.String
PX.ESign.ESignAccount.AccessToken : Edm.String
PX.ESign.ESignAccount.RefreshToken : Edm.String
PX.ESign.ESignAccount.IsConnected : Edm.Boolean [required]
PX.ESign.ESignAccount.ConnectionStatus : Edm.String "Status"
PX.ESign.ESignAccount.ProviderType : Edm.String "Provider"
PX.ESign.ESignAccount.SendReminders : Edm.Boolean [required] "Send Automatic Reminders"
PX.ESign.ESignAccount.ReminderType : Edm.String "Reminder Frequency"
PX.ESign.ESignAccount.ExpiredDays : Edm.Int32 [required] "Expiration Period in Days"
PX.ESign.ESignAccount.WarnDays : Edm.Int32 [required] "Days Before Expiration Warning"
PX.ESign.ESignAccount.FirstReminderDay : Edm.Int32 [required] "Days Before First Reminder"
PX.ESign.ESignAccount.ReminderFrequency : Edm.Int32 [required] "Days Between Reminders"
PX.ESign.ESignAccount.IsTestApi : Edm.Boolean [required] "Use Test API"
PX.ESign.ESignAccount.ProviderAccountID : Edm.String
PX.ESign.ESignAccount.CreatedByID : Edm.Guid "Created By"
PX.ESign.ESignAccount.CreatedByScreenID : Edm.String
PX.ESign.ESignAccount.CreatedDateTime : Edm.DateTimeOffset
PX.ESign.ESignAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ESign.ESignAccount.LastModifiedByScreenID : Edm.String
PX.ESign.ESignAccount.LastModifiedDateTime : Edm.DateTimeOffset
PX.ESign.ESignAccount.Tstamp : Edm.Binary
PX.ESign.ESignAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ESign.ESignAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ESign.ESignAccount.ESignAccountUserRuleCollection -> Collection(PX.ESign.ESignAccountUserRule)
PX.ESign.ESignAccount.ESignEnvelopeInfoCollection -> Collection(PX.ESign.ESignEnvelopeInfo)

# PX.ESign.ESignAccountUserRule (EntityType)

Label: "eSign Account User Rule"
Key: AccountID, OwnerID
Entity sets: PX_ESign_ESignAccountUserRule, eSignAccountUserRule

PX.ESign.ESignAccountUserRule.AccountID : Edm.Int32 [key]
PX.ESign.ESignAccountUserRule.OwnerID : Edm.Guid [key] "Employee ID"
PX.ESign.ESignAccountUserRule.CreatedByID : Edm.Guid "Created By"
PX.ESign.ESignAccountUserRule.CreatedByScreenID : Edm.String
PX.ESign.ESignAccountUserRule.CreatedDateTime : Edm.DateTimeOffset
PX.ESign.ESignAccountUserRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ESign.ESignAccountUserRule.LastModifiedByScreenID : Edm.String
PX.ESign.ESignAccountUserRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.ESign.ESignAccountUserRule.Tstamp : Edm.Binary
PX.ESign.ESignAccountUserRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ESign.ESignAccountUserRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ESign.ESignAccountUserRule.ESignAccountByAccountID -> PX.ESign.ESignAccount (AccountID=AccountID)

# PX.ESign.ESignEnvelopeInfo (EntityType)

Label: "eSign Request"
Key: EnvelopeInfoID
Entity sets: PX_ESign_ESignEnvelopeInfo, eSignRequest, ESignEnvelopeInfo
Non-filterable, non-selectable: IsSendAvailable, IsDeleteAvailable, IsRemindAvailable, IsVoidAvailable

PX.ESign.ESignEnvelopeInfo.EnvelopeInfoID : Edm.Int32 [key]
PX.ESign.ESignEnvelopeInfo.FileID : Edm.Guid
PX.ESign.ESignEnvelopeInfo.FileRevisionID : Edm.Int32
PX.ESign.ESignEnvelopeInfo.EnvelopeID : Edm.String
PX.ESign.ESignEnvelopeInfo.ReviewUrl : Edm.String
PX.ESign.ESignEnvelopeInfo.LastStatus : Edm.String "eSign Status"
PX.ESign.ESignEnvelopeInfo.AcumaticaEnvelopeStatus : Edm.String "eSign Status"
PX.ESign.ESignEnvelopeInfo.ActivityDate : Edm.DateTimeOffset "Status Updated On"
PX.ESign.ESignEnvelopeInfo.ESignAccountID : Edm.Int32 "eSign Account"
PX.ESign.ESignEnvelopeInfo.Theme : Edm.String "Subject"
PX.ESign.ESignEnvelopeInfo.MessageBody : Edm.String "Message"
PX.ESign.ESignEnvelopeInfo.IsOrder : Edm.Boolean [required] "Apply Signing Order"
PX.ESign.ESignEnvelopeInfo.ReminderType : Edm.String "Reminder Frequency"
PX.ESign.ESignEnvelopeInfo.SendReminders : Edm.Boolean "Send Automatic Reminders"
PX.ESign.ESignEnvelopeInfo.ExpiredDays : Edm.Int32 "Expiration Period in Days"
PX.ESign.ESignEnvelopeInfo.WarnDays : Edm.Int32 "Days Before Expiration Warning"
PX.ESign.ESignEnvelopeInfo.FirstReminderDay : Edm.Int32 "Days Before First Reminder"
PX.ESign.ESignEnvelopeInfo.ReminderFrequency : Edm.Int32 "Days Between Reminders"
PX.ESign.ESignEnvelopeInfo.IsFinalVersion : Edm.Boolean [required]
PX.ESign.ESignEnvelopeInfo.CompletedFileID : Edm.Guid
PX.ESign.ESignEnvelopeInfo.CompletedFileName : Edm.String "eSigned Version"
PX.ESign.ESignEnvelopeInfo.SendDate : Edm.DateTimeOffset "eSign Sent Date"
PX.ESign.ESignEnvelopeInfo.ExpirationDate : Edm.DateTimeOffset "Expires On"
PX.ESign.ESignEnvelopeInfo.ProviderType : Edm.String "Provider"
PX.ESign.ESignEnvelopeInfo.VoidReason : Edm.String "Recall Reason"
PX.ESign.ESignEnvelopeInfo.CreatedByID : Edm.Guid "Created By"
PX.ESign.ESignEnvelopeInfo.CreatedByScreenID : Edm.String
PX.ESign.ESignEnvelopeInfo.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.ESign.ESignEnvelopeInfo.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ESign.ESignEnvelopeInfo.LastModifiedByScreenID : Edm.String
PX.ESign.ESignEnvelopeInfo.LastModifiedDateTime : Edm.DateTimeOffset
PX.ESign.ESignEnvelopeInfo.Tstamp : Edm.Binary
PX.ESign.ESignEnvelopeInfo.IsSendAvailable : Edm.Boolean
PX.ESign.ESignEnvelopeInfo.IsDeleteAvailable : Edm.Boolean
PX.ESign.ESignEnvelopeInfo.IsRemindAvailable : Edm.Boolean
PX.ESign.ESignEnvelopeInfo.IsVoidAvailable : Edm.Boolean
PX.ESign.ESignEnvelopeInfo.UploadFileRevisionByFileRevisionID -> PX.SM.UploadFileRevision (FileID=FileID, FileRevisionID=FileRevisionID)
PX.ESign.ESignEnvelopeInfo.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ESign.ESignEnvelopeInfo.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ESign.ESignEnvelopeInfo.ESignAccountByESignAccountID -> PX.ESign.ESignAccount (ESignAccountID=AccountID)
PX.ESign.ESignEnvelopeInfo.ESignRecipientCollection -> Collection(PX.ESign.ESignRecipient)

# PX.ESign.ESignRecipient (EntityType)

Label: "eSign Recipient"
Key: RecipientID
Entity sets: PX_ESign_ESignRecipient, eSignRecipient

PX.ESign.ESignRecipient.RecipientID : Edm.Int32 [key]
PX.ESign.ESignRecipient.EnvelopeInfoID : Edm.Int32
PX.ESign.ESignRecipient.Email : Edm.String "Email Address"
PX.ESign.ESignRecipient.Name : Edm.String "Name"
PX.ESign.ESignRecipient.Position : Edm.Int32 "Signing Order"
PX.ESign.ESignRecipient.CustomMessage : Edm.String "Personal Message"
PX.ESign.ESignRecipient.Type : Edm.String "Recipient Role"
PX.ESign.ESignRecipient.Status : Edm.String "Recipient Status"
PX.ESign.ESignRecipient.SignedDateTime : Edm.DateTimeOffset "Signed On"
PX.ESign.ESignRecipient.DeliveredDateTime : Edm.DateTimeOffset "Delivered On"
PX.ESign.ESignRecipient.IPAddress : Edm.String "IP Address"
PX.ESign.ESignRecipient.CreatedByID : Edm.Guid "Created By"
PX.ESign.ESignRecipient.CreatedByScreenID : Edm.String
PX.ESign.ESignRecipient.CreatedDateTime : Edm.DateTimeOffset
PX.ESign.ESignRecipient.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ESign.ESignRecipient.LastModifiedByScreenID : Edm.String
PX.ESign.ESignRecipient.LastModifiedDateTime : Edm.DateTimeOffset
PX.ESign.ESignRecipient.Tstamp : Edm.Binary
PX.ESign.ESignRecipient.ContactByEmail -> PX.Objects.CR.Contact (Email=EMail)
PX.ESign.ESignRecipient.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ESign.ESignRecipient.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ESign.ESignRecipient.ESignEnvelopeInfoByEnvelopeInfoID -> PX.ESign.ESignEnvelopeInfo (EnvelopeInfoID=EnvelopeInfoID)

# PX.ExternalCarriersCommon.ShipEngineCarrierService (EntityType)

Key: CarrierPluginID, ServiceCode
Entity sets: PX_ExternalCarriersCommon_ShipEngineCarrierService

PX.ExternalCarriersCommon.ShipEngineCarrierService.CarrierPluginID : Edm.String [key]
PX.ExternalCarriersCommon.ShipEngineCarrierService.ServiceCode : Edm.String [key] "Service Code"
PX.ExternalCarriersCommon.ShipEngineCarrierService.ServiceName : Edm.String "Service Name"
PX.ExternalCarriersCommon.ShipEngineCarrierService.Domestic : Edm.Boolean [required] "Domestic"
PX.ExternalCarriersCommon.ShipEngineCarrierService.International : Edm.Boolean [required] "International"
PX.ExternalCarriersCommon.ShipEngineCarrierService.IsMultiPackageSupported : Edm.Boolean [required] "Supports Multiple Packages"
PX.ExternalCarriersCommon.ShipEngineCarrierService.IsSystemDefined : Edm.Boolean [required] "Provider-Defined"
PX.ExternalCarriersCommon.ShipEngineCarrierService.CreatedByID : Edm.Guid "Created By"
PX.ExternalCarriersCommon.ShipEngineCarrierService.CreatedByScreenID : Edm.String
PX.ExternalCarriersCommon.ShipEngineCarrierService.CreatedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersCommon.ShipEngineCarrierService.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ExternalCarriersCommon.ShipEngineCarrierService.LastModifiedByScreenID : Edm.String
PX.ExternalCarriersCommon.ShipEngineCarrierService.LastModifiedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersCommon.ShipEngineCarrierService.tstamp : Edm.Binary
PX.ExternalCarriersCommon.ShipEngineCarrierService.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ExternalCarriersCommon.ShipEngineCarrierService.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ExternalCarriersCommon.ShipEngineCarrierService.CarrierPluginByCarrierPluginID -> PX.Objects.CS.CarrierPlugin (CarrierPluginID=CarrierPluginID)

# PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData (EntityType)

Label: "Opportunity Carrier Data"
Key: RefNoteID
Entity sets: PX_ExternalCarriersHelper_CROpportunityRevisionCarrierData, OpportunityCarrierData, CROpportunityRevisionCarrierData

PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.RefNoteID : Edm.Guid [key]
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.LiftGate : Edm.Boolean [required] "Lift Gate"
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.AdditionalHandling : Edm.Boolean [required] "Additional Handling"
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.InsideDelivery : Edm.Boolean [required] "Inside Delivery"
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.LimitedAccess : Edm.Boolean [required] "Limited Access"
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.CreatedByID : Edm.Guid "Created By"
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.CreatedByScreenID : Edm.String
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.CreatedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.LastModifiedByScreenID : Edm.String
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.LastModifiedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.tstamp : Edm.Binary
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData.CROpportunityRevisionByRefNoteID -> PX.Objects.CR.Standalone.CROpportunityRevision (RefNoteID=NoteID)

# PX.ExternalCarriersHelper.InventoryItemCarrierData (EntityType)

Label: "Inventory Item Carrier Data"
Key: InventoryID
Entity sets: PX_ExternalCarriersHelper_InventoryItemCarrierData, InventoryItemCarrierData

PX.ExternalCarriersHelper.InventoryItemCarrierData.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.ExternalCarriersHelper.InventoryItemCarrierData.PacejetCommodityCode : Edm.String "Commodity Name"
PX.ExternalCarriersHelper.InventoryItemCarrierData.LinearUOM : Edm.String "Linear UOM"
PX.ExternalCarriersHelper.InventoryItemCarrierData.SelfPack : Edm.Boolean "Manufacturer's Packaging"
PX.ExternalCarriersHelper.InventoryItemCarrierData.Length : Edm.Decimal "Length"
PX.ExternalCarriersHelper.InventoryItemCarrierData.Height : Edm.Decimal "Height"
PX.ExternalCarriersHelper.InventoryItemCarrierData.Width : Edm.Decimal "Width"
PX.ExternalCarriersHelper.InventoryItemCarrierData.NMFCCode : Edm.String "Product Code"
PX.ExternalCarriersHelper.InventoryItemCarrierData.NMFCSubCode : Edm.String "Product Subcode"
PX.ExternalCarriersHelper.InventoryItemCarrierData.HazardousCode : Edm.String "Hazardous Material Code"
PX.ExternalCarriersHelper.InventoryItemCarrierData.PacejetTariffCode : Edm.String "Tariff Code Group"
PX.ExternalCarriersHelper.InventoryItemCarrierData.CreatedByID : Edm.Guid "Created By"
PX.ExternalCarriersHelper.InventoryItemCarrierData.CreatedByScreenID : Edm.String
PX.ExternalCarriersHelper.InventoryItemCarrierData.CreatedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.InventoryItemCarrierData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ExternalCarriersHelper.InventoryItemCarrierData.LastModifiedByScreenID : Edm.String
PX.ExternalCarriersHelper.InventoryItemCarrierData.LastModifiedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.InventoryItemCarrierData.tstamp : Edm.Binary
PX.ExternalCarriersHelper.InventoryItemCarrierData.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.ExternalCarriersHelper.InventoryItemCarrierData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ExternalCarriersHelper.InventoryItemCarrierData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ExternalCarriersHelper.InventoryItemCarrierData.INUnitByLinearUOM -> PX.Objects.IN.INUnit (LinearUOM=FromUnit)

# PX.ExternalCarriersHelper.SETerritoriesMapping (EntityType)

Key: CarrierPluginID, CountryID, StateID
Entity sets: PX_ExternalCarriersHelper_SETerritoriesMapping

PX.ExternalCarriersHelper.SETerritoriesMapping.CarrierPluginID : Edm.String [key]
PX.ExternalCarriersHelper.SETerritoriesMapping.CountryID : Edm.String [key] "Country"
PX.ExternalCarriersHelper.SETerritoriesMapping.StateID : Edm.String [key] "State"
PX.ExternalCarriersHelper.SETerritoriesMapping.StateName : Edm.String "State (For Carrier)"
PX.ExternalCarriersHelper.SETerritoriesMapping.CountryName : Edm.String "Country (For Carrier)"
PX.ExternalCarriersHelper.SETerritoriesMapping.CreatedByID : Edm.Guid "Created By"
PX.ExternalCarriersHelper.SETerritoriesMapping.CreatedByScreenID : Edm.String
PX.ExternalCarriersHelper.SETerritoriesMapping.CreatedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.SETerritoriesMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ExternalCarriersHelper.SETerritoriesMapping.LastModifiedByScreenID : Edm.String
PX.ExternalCarriersHelper.SETerritoriesMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.SETerritoriesMapping.tstamp : Edm.Binary
PX.ExternalCarriersHelper.SETerritoriesMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ExternalCarriersHelper.SETerritoriesMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ExternalCarriersHelper.SETerritoriesMapping.CarrierPluginByCarrierPluginID -> PX.Objects.CS.CarrierPlugin (CarrierPluginID=CarrierPluginID)
PX.ExternalCarriersHelper.SETerritoriesMapping.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.ExternalCarriersHelper.SETerritoriesMapping.StateByCountryID -> PX.Objects.CS.State (StateID=StateID, CountryID=CountryID)

# PX.ExternalCarriersHelper.SOOrderCarrierData (EntityType)

Label: "SO Order Carrier Data"
Key: OrderNbr, OrderType
Entity sets: PX_ExternalCarriersHelper_SOOrderCarrierData, SOOrderCarrierData

PX.ExternalCarriersHelper.SOOrderCarrierData.OrderType : Edm.String [key] "Order Type"
PX.ExternalCarriersHelper.SOOrderCarrierData.OrderNbr : Edm.String [key] "Order Nbr."
PX.ExternalCarriersHelper.SOOrderCarrierData.LiftGate : Edm.Boolean "Liftgate"
PX.ExternalCarriersHelper.SOOrderCarrierData.AdditionalHandling : Edm.Boolean "Additional Handling"
PX.ExternalCarriersHelper.SOOrderCarrierData.InsideDelivery : Edm.Boolean "Inside Delivery"
PX.ExternalCarriersHelper.SOOrderCarrierData.LimitedAccess : Edm.Boolean "Limited Access"
PX.ExternalCarriersHelper.SOOrderCarrierData.CreatedByID : Edm.Guid "Created By"
PX.ExternalCarriersHelper.SOOrderCarrierData.CreatedByScreenID : Edm.String
PX.ExternalCarriersHelper.SOOrderCarrierData.CreatedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.SOOrderCarrierData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ExternalCarriersHelper.SOOrderCarrierData.LastModifiedByScreenID : Edm.String
PX.ExternalCarriersHelper.SOOrderCarrierData.LastModifiedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.SOOrderCarrierData.tstamp : Edm.Binary
PX.ExternalCarriersHelper.SOOrderCarrierData.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.ExternalCarriersHelper.SOOrderCarrierData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ExternalCarriersHelper.SOOrderCarrierData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates (EntityType)

Label: "SOOrder Carrier Data for Shop for Rates"
Key: OrderNbr, OrderType
Entity sets: PX_ExternalCarriersHelper_SOOrderCarrierDataShopForRates, SOOrderCarrierDataforShopforRates, SOOrderCarrierDataShopForRates

PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates.OrderType : Edm.String [key]
PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates.OrderNbr : Edm.String [key]
PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates.InsideDelivery : Edm.Boolean "Inside Delivery"
PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates.AdditionalHandling : Edm.Boolean "Additional Handling"
PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates.LiftGate : Edm.Boolean "Liftgate"
PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates.LimitedAccess : Edm.Boolean "Limited Access"
PX.ExternalCarriersHelper.SOOrderCarrierDataShopForRates.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)

# PX.ExternalCarriersHelper.SOOrderShopForRates (EntityType)

Label: "SOOrder Data for Shop for Rates"
Key: OrderNbr, OrderType
Entity sets: PX_ExternalCarriersHelper_SOOrderShopForRates, SOOrderDataforShopforRates, SOOrderShopForRates
Non-filterable, non-selectable: CarrierPluginID, ShipViaSelectedFromDocument

PX.ExternalCarriersHelper.SOOrderShopForRates.OrderType : Edm.String [key]
PX.ExternalCarriersHelper.SOOrderShopForRates.OrderNbr : Edm.String [key]
PX.ExternalCarriersHelper.SOOrderShopForRates.RequestDate : Edm.DateTimeOffset "Requested On"
PX.ExternalCarriersHelper.SOOrderShopForRates.ShipDate : Edm.DateTimeOffset "Ship On"
PX.ExternalCarriersHelper.SOOrderShopForRates.Resedential : Edm.Boolean "Residential Delivery"
PX.ExternalCarriersHelper.SOOrderShopForRates.SaturdayDelivery : Edm.Boolean "Saturday Delivery"
PX.ExternalCarriersHelper.SOOrderShopForRates.Insurance : Edm.Boolean "Insurance"
PX.ExternalCarriersHelper.SOOrderShopForRates.UseCustomerAccount : Edm.Boolean "Use Customer's Account"
PX.ExternalCarriersHelper.SOOrderShopForRates.GroundCollect : Edm.Boolean "Ground Collect"
PX.ExternalCarriersHelper.SOOrderShopForRates.CarrierPluginID : Edm.String "Carrier"
PX.ExternalCarriersHelper.SOOrderShopForRates.ShipViaSelectedFromDocument : Edm.String
PX.ExternalCarriersHelper.SOOrderShopForRates.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOOrderTypeByOrigOrderType -> PX.Objects.SO.SOOrderType
PX.ExternalCarriersHelper.SOOrderShopForRates.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOBlanketOrderLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderLink)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.ExternalCarriersHelper.SOOrderShopForRates.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.ExternalCarriersHelper.SOOrderShopForRates.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.ExternalCarriersHelper.SOOrderShopForRates.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.ExternalCarriersHelper.SOOrderShopForRates.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.ExternalCarriersHelper.SOOrderShopForRates.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.ExternalCarriersHelper.SOOrderShopForRates.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.ExternalCarriersHelper.SOOrderShopForRates.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.ExternalCarriersHelper.SOOrderShopForRates.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.ExternalCarriersHelper.SOOrderShopForRates.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.ExternalCarriersHelper.SOOrderShopForRates.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.ExternalCarriersHelper.SOOrderShopForRates.CCPayLinkCollection -> Collection(PX.Objects.CC.CCPayLink)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOOrderSiteCollection -> Collection(PX.Objects.SO.SOOrderSite)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.ExternalCarriersHelper.SOOrderShopForRates.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.ExternalCarriersHelper.SOOrderShopForRates.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.ExternalCarriersHelper.SOOrderShopForRates.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.ExternalCarriersHelper.SOOrderShopForRates.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.ExternalCarriersHelper.SOOrderShopForRates.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.ExternalCarriersHelper.SOOrderShopForRates.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.ExternalCarriersHelper.SOOrderShopForRates.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOOrderCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.SOOrderCarrierData)
PX.ExternalCarriersHelper.SOOrderShopForRates.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.ExternalCarriersHelper.SOOrderShopForRates.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.ExternalCarriersHelper.SOOrderShopForRates.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.ExternalCarriersHelper.SOOrderShopForRates.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.ExternalCarriersHelper.SOOrderShopForRates.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.ExternalCarriersHelper.SOOrderShopForRates.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.ExternalCarriersHelper.SOOrderShopForRates.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)
PX.ExternalCarriersHelper.SOOrderShopForRates.DropShipSOLineCollection -> Collection(PX.Objects.SO.DropShipSOLine)
PX.ExternalCarriersHelper.SOOrderShopForRates.RQRequisitionOrderCollection -> Collection(PX.Objects.RQ.RQRequisitionOrder)
PX.ExternalCarriersHelper.SOOrderShopForRates.DropShipPOLineCollection -> Collection(PX.Objects.PO.DropShipPOLine)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.ExternalCarriersHelper.SOOrderShopForRates.SalesAllocationCollection -> Collection(PX.Objects.SO.SalesAllocation)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOLine2Collection -> Collection(PX.Objects.SO.SOLine2)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOLine4Collection -> Collection(PX.Objects.SO.SOLine4)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOMiscLine2Collection -> Collection(PX.Objects.SO.SOMiscLine2)
PX.ExternalCarriersHelper.SOOrderShopForRates.BlanketSOLineSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOLineSplit)
PX.ExternalCarriersHelper.SOOrderShopForRates.IntercompanyReturnedGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult)
PX.ExternalCarriersHelper.SOOrderShopForRates.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.ExternalCarriersHelper.SOOrderShopForRates.SOOrderRisksCollection -> Collection(PX.Commerce.Objects.SOOrderRisks)
PX.ExternalCarriersHelper.SOOrderShopForRates.AMConfigurationKeysCollection -> Collection(PX.Objects.AM.AMConfigurationKeys)
PX.ExternalCarriersHelper.SOOrderShopForRates.SchedulerMachineOperationCollection -> Collection(PX.Objects.AM.SchedulerMachineOperation)

# PX.ExternalCarriersHelper.SOShipmentCarrierData (EntityType)

Label: "SO Shipment Carrier Data"
Key: ShipmentNbr
Entity sets: PX_ExternalCarriersHelper_SOShipmentCarrierData, SOShipmentCarrierData

PX.ExternalCarriersHelper.SOShipmentCarrierData.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.ExternalCarriersHelper.SOShipmentCarrierData.ExternalStatus : Edm.String "Pacejet Status"
PX.ExternalCarriersHelper.SOShipmentCarrierData.MasterTrackingNumber : Edm.String "Master Tracking Number"
PX.ExternalCarriersHelper.SOShipmentCarrierData.AdditionalHandling : Edm.Boolean "Additional Handling"
PX.ExternalCarriersHelper.SOShipmentCarrierData.EmailNotification : Edm.Boolean "Email Notifications"
PX.ExternalCarriersHelper.SOShipmentCarrierData.HazardousMaterials : Edm.Boolean "Hazardous Materials"
PX.ExternalCarriersHelper.SOShipmentCarrierData.InsideDelivery : Edm.Boolean "Inside Delivery"
PX.ExternalCarriersHelper.SOShipmentCarrierData.LiftGate : Edm.Boolean "Liftgate"
PX.ExternalCarriersHelper.SOShipmentCarrierData.LimitedAccess : Edm.Boolean "Limited Access"
PX.ExternalCarriersHelper.SOShipmentCarrierData.PrintReturnLabel : Edm.Boolean "Preprint Return Label"
PX.ExternalCarriersHelper.SOShipmentCarrierData.DeliveryInstructions : Edm.String "Delivery Instructions"
PX.ExternalCarriersHelper.SOShipmentCarrierData.ProBillNbr : Edm.String "Pro Bill Nbr."
PX.ExternalCarriersHelper.SOShipmentCarrierData.BillOfLadingNbr : Edm.String "Bill of Lading Nbr."
PX.ExternalCarriersHelper.SOShipmentCarrierData.DeliveryDate : Edm.DateTimeOffset "Delivery Date"
PX.ExternalCarriersHelper.SOShipmentCarrierData.DeliveryTime : Edm.Int32 "Delivery Time"
PX.ExternalCarriersHelper.SOShipmentCarrierData.PacejetWorkstationID : Edm.String "Pacejet Workstation ID"
PX.ExternalCarriersHelper.SOShipmentCarrierData.CreatedByID : Edm.Guid "Created By"
PX.ExternalCarriersHelper.SOShipmentCarrierData.CreatedByScreenID : Edm.String
PX.ExternalCarriersHelper.SOShipmentCarrierData.CreatedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.SOShipmentCarrierData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.ExternalCarriersHelper.SOShipmentCarrierData.LastModifiedByScreenID : Edm.String
PX.ExternalCarriersHelper.SOShipmentCarrierData.LastModifiedDateTime : Edm.DateTimeOffset
PX.ExternalCarriersHelper.SOShipmentCarrierData.tstamp : Edm.Binary
PX.ExternalCarriersHelper.SOShipmentCarrierData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.ExternalCarriersHelper.SOShipmentCarrierData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.ExternalCarriersHelper.SOShipmentCarrierData.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)

# PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates (EntityType)

Label: "SOShipment Carrier Data for Shop for Rates"
Key: ShipmentNbr
Entity sets: PX_ExternalCarriersHelper_SOShipmentCarrierDataShopForRates, SOShipmentCarrierDataforShopforRates, SOShipmentCarrierDataShopForRates

PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates.ShipmentNbr : Edm.String [key]
PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates.InsideDelivery : Edm.Boolean "Inside Delivery"
PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates.AdditionalHandling : Edm.Boolean "Additional Handling"
PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates.LiftGate : Edm.Boolean "Liftgate"
PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates.LimitedAccess : Edm.Boolean "Limited Access"
PX.ExternalCarriersHelper.SOShipmentCarrierDataShopForRates.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)

# PX.ExternalCarriersHelper.SOShipmentShopForRates (EntityType)

Label: "SOShipment Data for Shop for Rates"
Key: ShipmentNbr
Entity sets: PX_ExternalCarriersHelper_SOShipmentShopForRates, SOShipmentDataforShopforRates, SOShipmentShopForRates
Non-filterable, non-selectable: CarrierPluginID, ShipViaSelectedFromDocument

PX.ExternalCarriersHelper.SOShipmentShopForRates.ShipmentNbr : Edm.String [key]
PX.ExternalCarriersHelper.SOShipmentShopForRates.ShipDate : Edm.DateTimeOffset "Ship On"
PX.ExternalCarriersHelper.SOShipmentShopForRates.RequestDate : Edm.DateTimeOffset "Requested On"
PX.ExternalCarriersHelper.SOShipmentShopForRates.Resedential : Edm.Boolean "Residential Delivery"
PX.ExternalCarriersHelper.SOShipmentShopForRates.SaturdayDelivery : Edm.Boolean "Saturday Delivery"
PX.ExternalCarriersHelper.SOShipmentShopForRates.Insurance : Edm.Boolean "Insurance"
PX.ExternalCarriersHelper.SOShipmentShopForRates.GroundCollect : Edm.Boolean "Ground Collect"
PX.ExternalCarriersHelper.SOShipmentShopForRates.UseCustomerAccount : Edm.Boolean "Use Customer's Account"
PX.ExternalCarriersHelper.SOShipmentShopForRates.CarrierPluginID : Edm.String "Carrier"
PX.ExternalCarriersHelper.SOShipmentShopForRates.ShipViaSelectedFromDocument : Edm.String
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.ExternalCarriersHelper.SOShipmentShopForRates.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOPickerToShipmentLinkCollection -> Collection(PX.Objects.SO.SOPickerToShipmentLink)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOPickingWorksheetCollection -> Collection(PX.Objects.SO.SOPickingWorksheet)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOPickingWorksheetShipmentCollection -> Collection(PX.Objects.SO.SOPickingWorksheetShipment)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)
PX.ExternalCarriersHelper.SOShipmentShopForRates.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOShipmentCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.SOShipmentCarrierData)
PX.ExternalCarriersHelper.SOShipmentShopForRates.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOShipmentProcessedByUserCollection -> Collection(PX.Objects.SO.SOShipmentProcessedByUser)
PX.ExternalCarriersHelper.SOShipmentShopForRates.IntercompanyReturnedGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult)
PX.ExternalCarriersHelper.SOShipmentShopForRates.SOCartShipmentCollection -> Collection(PX.Objects.SO.SOCartShipment)
PX.ExternalCarriersHelper.SOShipmentShopForRates.IntercompanyGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyGoodsInTransitResult)

# PX.FS.FSGPSTrackingHistory (EntityType)

Key: ExecutionDate, TrackingID
Entity sets: PX_FS_FSGPSTrackingHistory

PX.FS.FSGPSTrackingHistory.TrackingID : Edm.Guid [key] "Tracking ID"
PX.FS.FSGPSTrackingHistory.ExecutionDate : Edm.DateTimeOffset [key] "Execution Date"
PX.FS.FSGPSTrackingHistory.Latitude : Edm.Decimal [required] "Latitude"
PX.FS.FSGPSTrackingHistory.Longitude : Edm.Decimal [required] "Longitude"
PX.FS.FSGPSTrackingHistory.Altitude : Edm.Decimal [required] "Altitude"
PX.FS.FSGPSTrackingHistory.CreatedDateTime : Edm.DateTimeOffset

# PX.FS.FSGPSTrackingRequest (EntityType)

Key: RequestID
Entity sets: PX_FS_FSGPSTrackingRequest
Non-filterable, non-selectable: NoteText

PX.FS.FSGPSTrackingRequest.RequestID : Edm.Guid [key] "Request ID"
PX.FS.FSGPSTrackingRequest.Description : Edm.String "Description"
PX.FS.FSGPSTrackingRequest.IsActive : Edm.Boolean [required] "Is Active"
PX.FS.FSGPSTrackingRequest.TrackingID : Edm.Guid "Tracking ID"
PX.FS.FSGPSTrackingRequest.UserName : Edm.String "User Name"
PX.FS.FSGPSTrackingRequest.DeviceID : Edm.String "Device ID"
PX.FS.FSGPSTrackingRequest.DeviceName : Edm.String "Device Name"
PX.FS.FSGPSTrackingRequest.TimeZoneID : Edm.String "Time Zone"
PX.FS.FSGPSTrackingRequest.WeeklyOnDay1 : Edm.Boolean [required] "Sunday"
PX.FS.FSGPSTrackingRequest.WeeklyOnDay2 : Edm.Boolean [required] "Monday"
PX.FS.FSGPSTrackingRequest.WeeklyOnDay3 : Edm.Boolean [required] "Tuesday"
PX.FS.FSGPSTrackingRequest.WeeklyOnDay4 : Edm.Boolean [required] "Wednesday"
PX.FS.FSGPSTrackingRequest.WeeklyOnDay5 : Edm.Boolean [required] "Thursday"
PX.FS.FSGPSTrackingRequest.WeeklyOnDay6 : Edm.Boolean [required] "Friday"
PX.FS.FSGPSTrackingRequest.WeeklyOnDay7 : Edm.Boolean [required] "Saturday"
PX.FS.FSGPSTrackingRequest.StartDate : Edm.DateTimeOffset "Starts On (Date)"
PX.FS.FSGPSTrackingRequest.EndDate : Edm.DateTimeOffset "Expires On (Date)"
PX.FS.FSGPSTrackingRequest.StartTime : Edm.DateTimeOffset "Starts On (Time)"
PX.FS.FSGPSTrackingRequest.EndTime : Edm.DateTimeOffset "Expires On (Time)"
PX.FS.FSGPSTrackingRequest.Interval : Edm.Int16 [required] "Interval"
PX.FS.FSGPSTrackingRequest.Distance : Edm.Int16 [required] "Distance"
PX.FS.FSGPSTrackingRequest.NoteID : Edm.Guid
PX.FS.FSGPSTrackingRequest.NoteText : Edm.String "Note Text"
PX.FS.FSGPSTrackingRequest.CreatedByID : Edm.Guid "Created By"
PX.FS.FSGPSTrackingRequest.CreatedByScreenID : Edm.String
PX.FS.FSGPSTrackingRequest.CreatedDateTime : Edm.DateTimeOffset
PX.FS.FSGPSTrackingRequest.LastModifiedByID : Edm.Guid "Last Modified By"
PX.FS.FSGPSTrackingRequest.LastModifiedByScreenID : Edm.String
PX.FS.FSGPSTrackingRequest.LastModifiedDateTime : Edm.DateTimeOffset
PX.FS.FSGPSTrackingRequest.TStamp : Edm.Binary
PX.FS.FSGPSTrackingRequest.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.FS.FSGPSTrackingRequest.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.FS.FSGPSTrackingRequest.UsersByUserName -> PX.SM.Users (UserName=Username)

# PX.GIReports.Maintenance.DAC.GIReport (EntityType)

Label: "Grouped Table"
Key: ReportID
Entity sets: PX_GIReports_Maintenance_DAC_GIReport, GroupedTable, GIReport
Non-filterable, non-selectable: NoteText

PX.GIReports.Maintenance.DAC.GIReport.ReportID : Edm.Guid [key]
PX.GIReports.Maintenance.DAC.GIReport.GIDesignID : Edm.Guid "GI Design ID"
PX.GIReports.Maintenance.DAC.GIReport.CreatedByID : Edm.Guid "Created By"
PX.GIReports.Maintenance.DAC.GIReport.CreatedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReport.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.GIReports.Maintenance.DAC.GIReport.LastModifiedByID : Edm.Guid "Last Modified By"
PX.GIReports.Maintenance.DAC.GIReport.LastModifiedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReport.LastModifiedDateTime : Edm.DateTimeOffset
PX.GIReports.Maintenance.DAC.GIReport.NoteID : Edm.Guid
PX.GIReports.Maintenance.DAC.GIReport.NoteText : Edm.String "Note Text"
PX.GIReports.Maintenance.DAC.GIReport.tstamp : Edm.Binary
PX.GIReports.Maintenance.DAC.GIReport.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReport.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReport.GIDesignByGiDesignID -> PX.Data.Maintenance.GI.GIDesign
PX.GIReports.Maintenance.DAC.GIReport.GIReportGroupCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroup)
PX.GIReports.Maintenance.DAC.GIReport.GIReportGroupColumnCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupColumn)
PX.GIReports.Maintenance.DAC.GIReport.GIReportGroupGroupingCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupGrouping)
PX.GIReports.Maintenance.DAC.GIReport.GIReportGroupSortingCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupSorting)

# PX.GIReports.Maintenance.DAC.GIReportGroup (EntityType)

Label: "Grouped Table Groups"
Key: GroupID, ReportID
Entity sets: PX_GIReports_Maintenance_DAC_GIReportGroup, GroupedTableGroups, GIReportGroup
Non-filterable, non-selectable: IsDetail, IsTotal, NoteText

PX.GIReports.Maintenance.DAC.GIReportGroup.ReportID : Edm.Guid [key] "Report ID"
PX.GIReports.Maintenance.DAC.GIReportGroup.GroupID : Edm.Int32 [key] "Group ID"
PX.GIReports.Maintenance.DAC.GIReportGroup.SortOrder : Edm.Int32 "SortOrder"
PX.GIReports.Maintenance.DAC.GIReportGroup.Name : Edm.String "Group Name"
PX.GIReports.Maintenance.DAC.GIReportGroup.IsActive : Edm.Boolean [required] "Active"
PX.GIReports.Maintenance.DAC.GIReportGroup.VisibleCondition : Edm.String "Visibility Condition"
PX.GIReports.Maintenance.DAC.GIReportGroup.CollapseByDefault : Edm.Boolean [required] "Collapse By Default"
PX.GIReports.Maintenance.DAC.GIReportGroup.ShowColumnCaptions : Edm.Boolean [required] "Show Column Captions"
PX.GIReports.Maintenance.DAC.GIReportGroup.IsDetail : Edm.Boolean
PX.GIReports.Maintenance.DAC.GIReportGroup.IsTotal : Edm.Boolean
PX.GIReports.Maintenance.DAC.GIReportGroup.CreatedByID : Edm.Guid "Created By"
PX.GIReports.Maintenance.DAC.GIReportGroup.CreatedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReportGroup.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.GIReports.Maintenance.DAC.GIReportGroup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.GIReports.Maintenance.DAC.GIReportGroup.LastModifiedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReportGroup.LastModifiedDateTime : Edm.DateTimeOffset
PX.GIReports.Maintenance.DAC.GIReportGroup.NoteID : Edm.Guid
PX.GIReports.Maintenance.DAC.GIReportGroup.NoteText : Edm.String "Note Text"
PX.GIReports.Maintenance.DAC.GIReportGroup.tstamp : Edm.Binary
PX.GIReports.Maintenance.DAC.GIReportGroup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReportGroup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReportGroup.GIReportByReportID -> PX.GIReports.Maintenance.DAC.GIReport (ReportID=ReportID)
PX.GIReports.Maintenance.DAC.GIReportGroup.GIReportGroupColumnCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupColumn)
PX.GIReports.Maintenance.DAC.GIReportGroup.GIReportGroupGroupingCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupGrouping)
PX.GIReports.Maintenance.DAC.GIReportGroup.GIReportGroupSortingCollection -> Collection(PX.GIReports.Maintenance.DAC.GIReportGroupSorting)

# PX.GIReports.Maintenance.DAC.GIReportGroupColumn (EntityType)

Label: "Grouped Table Columns"
Key: GroupID, LineNbr, ReportID
Entity sets: PX_GIReports_Maintenance_DAC_GIReportGroupColumn, GroupedTableColumns, GIReportGroupColumn
Non-filterable, non-selectable: NoteText

PX.GIReports.Maintenance.DAC.GIReportGroupColumn.ReportID : Edm.Guid [key] "Report ID"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.GroupID : Edm.Int32 [key] "Group ID"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.LineNbr : Edm.Int32 [key]
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.SortOrder : Edm.Int32 "SortOrder"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.IsActive : Edm.Boolean [required] "Active"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.DataSource : Edm.String "Data Source"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.Aggregate : Edm.String "Aggregate"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.Caption : Edm.String "Caption"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.Width : Edm.Int32 "Width (px)"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.IsVisible : Edm.Boolean [required] "Visible"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.Format : Edm.String "Format"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.Span : Edm.Int32 "Span"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.TextAlign : Edm.Int16 "Text Alignment"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.CreatedByID : Edm.Guid "Created By"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.CreatedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.LastModifiedByID : Edm.Guid "Last Modified By"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.LastModifiedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.LastModifiedDateTime : Edm.DateTimeOffset
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.NoteID : Edm.Guid
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.NoteText : Edm.String "Note Text"
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.tstamp : Edm.Binary
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.GIReportByReportID -> PX.GIReports.Maintenance.DAC.GIReport (ReportID=ReportID)
PX.GIReports.Maintenance.DAC.GIReportGroupColumn.GIReportGroupByGroupID -> PX.GIReports.Maintenance.DAC.GIReportGroup (ReportID=ReportID, GroupID=GroupID)

# PX.GIReports.Maintenance.DAC.GIReportGroupGrouping (EntityType)

Label: "Grouped Table Grouping"
Key: GroupID, LineNbr, ReportID
Entity sets: PX_GIReports_Maintenance_DAC_GIReportGroupGrouping, GroupedTableGrouping, GIReportGroupGrouping
Non-filterable, non-selectable: NoteText

PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.ReportID : Edm.Guid [key] "Report ID"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.GroupID : Edm.Int32 [key] "Group ID"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.LineNbr : Edm.Int32 [key]
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.SortOrder : Edm.Int32 "SortOrder"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.DataFieldName : Edm.String "Data Source"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.IsActive : Edm.Boolean [required] "Active"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.CreatedByID : Edm.Guid "Created By"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.CreatedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.LastModifiedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.LastModifiedDateTime : Edm.DateTimeOffset
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.NoteID : Edm.Guid
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.NoteText : Edm.String "Note Text"
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.tstamp : Edm.Binary
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.GIReportByReportID -> PX.GIReports.Maintenance.DAC.GIReport (ReportID=ReportID)
PX.GIReports.Maintenance.DAC.GIReportGroupGrouping.GIReportGroupByGroupID -> PX.GIReports.Maintenance.DAC.GIReportGroup (ReportID=ReportID, GroupID=GroupID)

# PX.GIReports.Maintenance.DAC.GIReportGroupSorting (EntityType)

Label: "Grouped Table Sorting"
Key: GroupID, LineNbr, ReportID
Entity sets: PX_GIReports_Maintenance_DAC_GIReportGroupSorting, GroupedTableSorting, GIReportGroupSorting
Non-filterable, non-selectable: NoteText

PX.GIReports.Maintenance.DAC.GIReportGroupSorting.ReportID : Edm.Guid [key] "Report ID"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.GroupID : Edm.Int32 [key] "Group ID"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.LineNbr : Edm.Int32 [key]
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.SortOrder : Edm.Int32 "SortOrder"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.DataFieldName : Edm.String "Data Source"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.Sorting : Edm.String "Sort Order"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.IsActive : Edm.Boolean [required] "Active"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.CreatedByID : Edm.Guid "Created By"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.CreatedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.CreatedDateTime : Edm.DateTimeOffset "Creation Date"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.LastModifiedByID : Edm.Guid "Last Modified By"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.LastModifiedByScreenID : Edm.String
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.LastModifiedDateTime : Edm.DateTimeOffset
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.NoteID : Edm.Guid
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.NoteText : Edm.String "Note Text"
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.tstamp : Edm.Binary
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.GIReportByReportID -> PX.GIReports.Maintenance.DAC.GIReport (ReportID=ReportID)
PX.GIReports.Maintenance.DAC.GIReportGroupSorting.GIReportGroupByGroupID -> PX.GIReports.Maintenance.DAC.GIReportGroup (ReportID=ReportID, GroupID=GroupID)

# PX.Mail.Log.DAC.EmailLog (EntityType)

Label: "Email Log"
Key: LogEntryID
Entity sets: PX_Mail_Log_DAC_EmailLog, EmailLog

PX.Mail.Log.DAC.EmailLog.LogEntryID : Edm.Guid [key] "Log Entry ID"
PX.Mail.Log.DAC.EmailLog.LogEntryDateTime : Edm.DateTimeOffset [required] "Log Entry Date"
PX.Mail.Log.DAC.EmailLog.LogLevel : Edm.Int32 [required] "Level"
PX.Mail.Log.DAC.EmailLog.EMailAccountID : Edm.Int32 "Email Account"
PX.Mail.Log.DAC.EmailLog.RefNoteID : Edm.Guid "Email"
PX.Mail.Log.DAC.EmailLog.ExtServiceType : Edm.String "Ext. Service"
PX.Mail.Log.DAC.EmailLog.ExtServiceID : Edm.String "Ext. ID"
PX.Mail.Log.DAC.EmailLog.Operation : Edm.String "Operation"
PX.Mail.Log.DAC.EmailLog.Message : Edm.String "Message"
PX.Mail.Log.DAC.EmailLog.Exception : Edm.String "Exception"
PX.Mail.Log.DAC.EmailLog.EmailMessageID : Edm.String "Message-ID"
PX.Mail.Log.DAC.EmailLog.EmailDateTime : Edm.DateTimeOffset "Date"
PX.Mail.Log.DAC.EmailLog.EmailFrom : Edm.String "From"
PX.Mail.Log.DAC.EmailLog.EmailSender : Edm.String "Sender"
PX.Mail.Log.DAC.EmailLog.EmailTo : Edm.String "To"
PX.Mail.Log.DAC.EmailLog.EmailCc : Edm.String "CC"
PX.Mail.Log.DAC.EmailLog.EmailBcc : Edm.String "BCC"
PX.Mail.Log.DAC.EmailLog.EMailAccountByEMailAccountID -> PX.SM.EMailAccount (EMailAccountID=EmailAccountID)
PX.Mail.Log.DAC.EmailLog.SMEmailByRefNoteID -> PX.Objects.CR.SMEmail (RefNoteID=RefNoteID)

# PX.ML.Chat.DAC.MLChatMessage (EntityType)

Label: "MLChatMessage"
Key: MessageID
Entity sets: PX_ML_Chat_DAC_MLChatMessage, MLChatMessage

PX.ML.Chat.DAC.MLChatMessage.ThreadID : Edm.Int64 "Thread ID"
PX.ML.Chat.DAC.MLChatMessage.MessageID : Edm.Int64 [key] "Message ID"
PX.ML.Chat.DAC.MLChatMessage.CorrelationID : Edm.Guid
PX.ML.Chat.DAC.MLChatMessage.Sender : Edm.String "Sender"
PX.ML.Chat.DAC.MLChatMessage.Receiver : Edm.String "Receiver"
PX.ML.Chat.DAC.MLChatMessage.DateTime : Edm.DateTimeOffset "Message Creation Date"
PX.ML.Chat.DAC.MLChatMessage.TextMessage : Edm.String "Message Text"
PX.ML.Chat.DAC.MLChatMessage.MessageData : Edm.String "Message Data"
PX.ML.Chat.DAC.MLChatMessage.IsSent : Edm.Int32 "Message Status"
PX.ML.Chat.DAC.MLChatMessage.Feedback : Edm.Boolean "Feedback"

# PX.ML.Chat.DAC.MLChatMessageAttachment (EntityType)

Label: "MLChatMessageAttachment"
Key: FileID, MessageID
Entity sets: PX_ML_Chat_DAC_MLChatMessageAttachment, MLChatMessageAttachment

PX.ML.Chat.DAC.MLChatMessageAttachment.ThreadID : Edm.Int64 "Thread ID"
PX.ML.Chat.DAC.MLChatMessageAttachment.MessageID : Edm.Int64 [key] "Message ID"
PX.ML.Chat.DAC.MLChatMessageAttachment.FileID : Edm.Guid [key] "File ID"
PX.ML.Chat.DAC.MLChatMessageAttachment.FileName : Edm.String "File Name"
PX.ML.Chat.DAC.MLChatMessageAttachment.CloudFileID : Edm.String "Cloud File ID"
PX.ML.Chat.DAC.MLChatMessageAttachment.ServiceKey : Edm.String
PX.ML.Chat.DAC.MLChatMessageAttachment.UploadStatus : Edm.Int32 "Uploading Status"
PX.ML.Chat.DAC.MLChatMessageAttachment.UploadedDateTime : Edm.DateTimeOffset "Uploaded At"
PX.ML.Chat.DAC.MLChatMessageAttachment.CreatedDateTime : Edm.DateTimeOffset

# PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory (EntityType)

Label: "MLAIAssistantUnitsConsumptionHistory"
Key: HistoryID
Entity sets: PX_ML_Chat_Licensing_DAC_MLAIAssistantUnitsConsumptionHistory, MLAIAssistantUnitsConsumptionHistory

PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory.HistoryID : Edm.Int64 [key]
PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory.UserID : Edm.String "User Name"
PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory.RecipientType : Edm.Byte "Recipient Type"
PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory.MessageID : Edm.Int64 "Message ID"
PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory.CorrelationID : Edm.Guid "Prompt Correlation ID"
PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory.Date : Edm.DateTimeOffset "Date"
PX.ML.Chat.Licensing.DAC.MLAIAssistantUnitsConsumptionHistory.AIUnits : Edm.Int32 "AI Units"

# PX.ML.CrossSales.DAC.MLCrossSalesSetup (EntityType)

Label: "MLCrossSalesSetup"
Singletons: PX_ML_CrossSales_DAC_MLCrossSalesSetup, MLCrossSalesSetup

PX.ML.CrossSales.DAC.MLCrossSalesSetup.ReCalculationPeriod : Edm.Int32 "Frequency"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.ItemsGIID : Edm.Guid "Generic Inquiry with Transactions"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.FeedBackGIID : Edm.Guid "Generic Inquiry with Feedback"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.DataPeriodForAnalysis : Edm.String "Data Period for Analysis"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.MinRelevanceScore : Edm.Decimal
PX.ML.CrossSales.DAC.MLCrossSalesSetup.MinRelevanceScorePercent : Edm.Decimal "Min. Relevance Score (%)"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.MaxNumberOfSuggestions : Edm.Int32 "Max. Number of Suggestions"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.AddRelationsAsActive : Edm.Boolean [required] "Add Relations as Active"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.GeneratedSuggestionNotification : Edm.Int32 "Generated Suggestion Notification"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.NoteID : Edm.Guid
PX.ML.CrossSales.DAC.MLCrossSalesSetup.NoteText : Edm.String "Note Text"
PX.ML.CrossSales.DAC.MLCrossSalesSetup.GIDesignByItemsGIID -> PX.Data.Maintenance.GI.GIDesign (ItemsGIID=DesignID)
PX.ML.CrossSales.DAC.MLCrossSalesSetup.GIDesignByFeedBackGIID -> PX.Data.Maintenance.GI.GIDesign (FeedBackGIID=DesignID)
PX.ML.CrossSales.DAC.MLCrossSalesSetup.NotificationByGeneratedSuggestionNotification -> PX.SM.Notification (GeneratedSuggestionNotification=NotificationID)

# PX.MSGraph.DAC.SM.SMGraphPermission (EntityType)

Label: "Graph Access Rights"
Key: AccessRight
Entity sets: PX_MSGraph_DAC_SM_SMGraphPermission, GraphAccessRights, SMGraphPermission
Non-filterable, non-selectable: Description, ApplicableFor, AdminConsent

PX.MSGraph.DAC.SM.SMGraphPermission.AccessRight : Edm.String [key] "Permission"
PX.MSGraph.DAC.SM.SMGraphPermission.Enabled : Edm.Boolean [required] "Enabled"
PX.MSGraph.DAC.SM.SMGraphPermission.Tstamp : Edm.Binary "Tstamp"
PX.MSGraph.DAC.SM.SMGraphPermission.CreatedByID : Edm.Guid "Created By"
PX.MSGraph.DAC.SM.SMGraphPermission.CreatedByScreenID : Edm.String
PX.MSGraph.DAC.SM.SMGraphPermission.CreatedDateTime : Edm.DateTimeOffset
PX.MSGraph.DAC.SM.SMGraphPermission.LastModifiedByID : Edm.Guid "Last Modified By"
PX.MSGraph.DAC.SM.SMGraphPermission.LastModifiedByScreenID : Edm.String
PX.MSGraph.DAC.SM.SMGraphPermission.LastModifiedDateTime : Edm.DateTimeOffset
PX.MSGraph.DAC.SM.SMGraphPermission.Description : Edm.String "Description"
PX.MSGraph.DAC.SM.SMGraphPermission.ApplicableFor : Edm.String "Applicable For"
PX.MSGraph.DAC.SM.SMGraphPermission.AdminConsent : Edm.Boolean "Admin Consent"
PX.MSGraph.DAC.SM.SMGraphPermission.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.MSGraph.DAC.SM.SMGraphPermission.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.MSGraph.DAC.SM.SMGraphSetup (EntityType)

Label: "Teams Preferences"
Singletons: PX_MSGraph_DAC_SM_SMGraphSetup, TeamsPreferences, SMGraphSetup

PX.MSGraph.DAC.SM.SMGraphSetup.TenantID : Edm.Guid "Tenant ID"
PX.MSGraph.DAC.SM.SMGraphSetup.ClientID : Edm.String "Client ID"
PX.MSGraph.DAC.SM.SMGraphSetup.ClientSecret : Edm.String "Client Secret"
PX.MSGraph.DAC.SM.SMGraphSetup.Timeout : Edm.Int32 "User Inactivity Timeout (Sec)"
PX.MSGraph.DAC.SM.SMGraphSetup.CreatedByID : Edm.Guid "Created By"
PX.MSGraph.DAC.SM.SMGraphSetup.CreatedByScreenID : Edm.String
PX.MSGraph.DAC.SM.SMGraphSetup.CreatedDateTime : Edm.DateTimeOffset
PX.MSGraph.DAC.SM.SMGraphSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.MSGraph.DAC.SM.SMGraphSetup.LastModifiedByScreenID : Edm.String
PX.MSGraph.DAC.SM.SMGraphSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.MSGraph.DAC.SM.SMGraphSetup.Tstamp : Edm.Binary
PX.MSGraph.DAC.SM.SMGraphSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.MSGraph.DAC.SM.SMGraphSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.MSTeams.DAC.SM.SMTeamsChannel (EntityType)

Label: "Teams Channel"
Key: ChannelID
Entity sets: PX_MSTeams_DAC_SM_SMTeamsChannel, TeamsChannel, SMTeamsChannel
Non-filterable, non-selectable: IsNotificationConfigured, TeamPhoto

PX.MSTeams.DAC.SM.SMTeamsChannel.TeamsID : Edm.Guid "Team"
PX.MSTeams.DAC.SM.SMTeamsChannel.Active : Edm.Boolean [required] "Active"
PX.MSTeams.DAC.SM.SMTeamsChannel.ChannelID : Edm.String [key] "Channel"
PX.MSTeams.DAC.SM.SMTeamsChannel.DisplayName : Edm.String "Channel"
PX.MSTeams.DAC.SM.SMTeamsChannel.Description : Edm.String "Description"
PX.MSTeams.DAC.SM.SMTeamsChannel.TeamChannel : Edm.String "Team Channel"
PX.MSTeams.DAC.SM.SMTeamsChannel.NotificationUrl : Edm.String "Incoming Webhook URL"
PX.MSTeams.DAC.SM.SMTeamsChannel.IsNotificationConfigured : Edm.Boolean
PX.MSTeams.DAC.SM.SMTeamsChannel.TeamPhoto : Edm.String "Picture"
PX.MSTeams.DAC.SM.SMTeamsChannel.SMTeamsTeamByTeamsID -> PX.MSTeams.DAC.SM.SMTeamsTeam (TeamsID=TeamsID)
PX.MSTeams.DAC.SM.SMTeamsChannel.SMTeamsNotificationCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsNotification)

# PX.MSTeams.DAC.SM.SMTeamsMember (EntityType)

Label: "Teams Member"
Key: MemberID
Entity sets: PX_MSTeams_DAC_SM_SMTeamsMember, TeamsMember, SMTeamsMember
Non-filterable, non-selectable: NoteText, TeamsStatus, GraphTeamsStatus, TeamPhoto, TeamsRedirectType

PX.MSTeams.DAC.SM.SMTeamsMember.MemberID : Edm.Guid [key]
PX.MSTeams.DAC.SM.SMTeamsMember.Active : Edm.Boolean [required] "Active"
PX.MSTeams.DAC.SM.SMTeamsMember.ContactID : Edm.Int32 "Acumatica ERP Contact/Employee"
PX.MSTeams.DAC.SM.SMTeamsMember.DisplayName : Edm.String "Teams Member"
PX.MSTeams.DAC.SM.SMTeamsMember.GivenName : Edm.String "First Name"
PX.MSTeams.DAC.SM.SMTeamsMember.SurName : Edm.String "First Name"
PX.MSTeams.DAC.SM.SMTeamsMember.CompanyName : Edm.String "Company"
PX.MSTeams.DAC.SM.SMTeamsMember.JobTitle : Edm.String "Title"
PX.MSTeams.DAC.SM.SMTeamsMember.MobilePhone : Edm.String "Phone"
PX.MSTeams.DAC.SM.SMTeamsMember.UserPrincipalName : Edm.String "Teams ID"
PX.MSTeams.DAC.SM.SMTeamsMember.Email : Edm.String "Email"
PX.MSTeams.DAC.SM.SMTeamsMember.PhotoFileName : Edm.String
PX.MSTeams.DAC.SM.SMTeamsMember.ThumbnailFileID : Edm.Guid
PX.MSTeams.DAC.SM.SMTeamsMember.Noteid : Edm.Guid
PX.MSTeams.DAC.SM.SMTeamsMember.NoteText : Edm.String "Note Text"
PX.MSTeams.DAC.SM.SMTeamsMember.TeamsStatus : Edm.String "Status"
PX.MSTeams.DAC.SM.SMTeamsMember.GraphTeamsStatus : Edm.String "GraphTeamsStatus"
PX.MSTeams.DAC.SM.SMTeamsMember.TeamPhoto : Edm.String "Picture"
PX.MSTeams.DAC.SM.SMTeamsMember.TeamsRedirectType : Edm.String
PX.MSTeams.DAC.SM.SMTeamsMember.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.MSTeams.DAC.SM.SMTeamsMember.SMTeamsMemberMappingCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsMemberMapping)

# PX.MSTeams.DAC.SM.SMTeamsMemberMapping (EntityType)

Label: "Teams Member Mapping"
Key: MemberID, TeamsID
Entity sets: PX_MSTeams_DAC_SM_SMTeamsMemberMapping, TeamsMemberMapping, SMTeamsMemberMapping

PX.MSTeams.DAC.SM.SMTeamsMemberMapping.TeamsID : Edm.Guid [key] "Team"
PX.MSTeams.DAC.SM.SMTeamsMemberMapping.MemberID : Edm.Guid [key] "Member"
PX.MSTeams.DAC.SM.SMTeamsMemberMapping.SMTeamsMemberByMemberID -> PX.MSTeams.DAC.SM.SMTeamsMember (MemberID=MemberID)
PX.MSTeams.DAC.SM.SMTeamsMemberMapping.SMTeamsTeamByTeamsID -> PX.MSTeams.DAC.SM.SMTeamsTeam (TeamsID=TeamsID)

# PX.MSTeams.DAC.SM.SMTeamsNotification (EntityType)

Label: "Teams Notification"
Key: NotificationID
Entity sets: PX_MSTeams_DAC_SM_SMTeamsNotification, TeamsNotification, SMTeamsNotification
Non-filterable, non-selectable: NoteText, ShowReportTabExpr, ShowSendByEventsTabExpr

PX.MSTeams.DAC.SM.SMTeamsNotification.NotificationID : Edm.Int32 [key] "Notification ID"
PX.MSTeams.DAC.SM.SMTeamsNotification.Name : Edm.String "Description"
PX.MSTeams.DAC.SM.SMTeamsNotification.ChannelID : Edm.String "Teams Channel"
PX.MSTeams.DAC.SM.SMTeamsNotification.Subject : Edm.String "Subject"
PX.MSTeams.DAC.SM.SMTeamsNotification.ScreenID : Edm.String "Screen"
PX.MSTeams.DAC.SM.SMTeamsNotification.Body : Edm.String "Body"
PX.MSTeams.DAC.SM.SMTeamsNotification.LocaleName : Edm.String "Locale"
PX.MSTeams.DAC.SM.SMTeamsNotification.NoteID : Edm.Guid
PX.MSTeams.DAC.SM.SMTeamsNotification.NoteText : Edm.String "Note Text"
PX.MSTeams.DAC.SM.SMTeamsNotification.CreatedByID : Edm.Guid "Created By"
PX.MSTeams.DAC.SM.SMTeamsNotification.CreatedByScreenID : Edm.String
PX.MSTeams.DAC.SM.SMTeamsNotification.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.MSTeams.DAC.SM.SMTeamsNotification.LastModifiedByID : Edm.Guid "Last Modified By"
PX.MSTeams.DAC.SM.SMTeamsNotification.LastModifiedByScreenID : Edm.String
PX.MSTeams.DAC.SM.SMTeamsNotification.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.MSTeams.DAC.SM.SMTeamsNotification.tstamp : Edm.Binary
PX.MSTeams.DAC.SM.SMTeamsNotification.BAccountID : Edm.String "Link to Account"
PX.MSTeams.DAC.SM.SMTeamsNotification.ContactID : Edm.String "Link to Contact"
PX.MSTeams.DAC.SM.SMTeamsNotification.RefNoteID : Edm.String "Link to Entity"
PX.MSTeams.DAC.SM.SMTeamsNotification.ReportAction : Edm.String "Attach Report Opened by Action"
PX.MSTeams.DAC.SM.SMTeamsNotification.AttachActivity : Edm.Boolean [required] "Attach Activity"
PX.MSTeams.DAC.SM.SMTeamsNotification.NotificationUrl : Edm.String
PX.MSTeams.DAC.SM.SMTeamsNotification.ShowReportTabExpr : Edm.Boolean "ShowReportTabExpr"
PX.MSTeams.DAC.SM.SMTeamsNotification.ShowSendByEventsTabExpr : Edm.Boolean "ShowSendByEventsTabExpr"
PX.MSTeams.DAC.SM.SMTeamsNotification.SiteMapByScreenID -> PX.SM.SiteMap (ScreenID=ScreenID)
PX.MSTeams.DAC.SM.SMTeamsNotification.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.MSTeams.DAC.SM.SMTeamsNotification.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.MSTeams.DAC.SM.SMTeamsNotification.SMTeamsChannelByChannelID -> PX.MSTeams.DAC.SM.SMTeamsChannel (ChannelID=ChannelID)
PX.MSTeams.DAC.SM.SMTeamsNotification.LocaleByLocaleName -> PX.SM.Locale (LocaleName=LocaleName)

# PX.MSTeams.DAC.SM.SMTeamsTeam (EntityType)

Label: "Teams Team"
Key: TeamsID
Entity sets: PX_MSTeams_DAC_SM_SMTeamsTeam, TeamsTeam, SMTeamsTeam
Non-filterable, non-selectable: NoteText, TeamPhoto

PX.MSTeams.DAC.SM.SMTeamsTeam.TeamsID : Edm.Guid [key] "Team"
PX.MSTeams.DAC.SM.SMTeamsTeam.Active : Edm.Boolean [required] "Active"
PX.MSTeams.DAC.SM.SMTeamsTeam.DisplayName : Edm.String "Team"
PX.MSTeams.DAC.SM.SMTeamsTeam.Description : Edm.String "Description"
PX.MSTeams.DAC.SM.SMTeamsTeam.PhotoFileName : Edm.String
PX.MSTeams.DAC.SM.SMTeamsTeam.ThumbnailFileID : Edm.Guid
PX.MSTeams.DAC.SM.SMTeamsTeam.Noteid : Edm.Guid
PX.MSTeams.DAC.SM.SMTeamsTeam.NoteText : Edm.String "Note Text"
PX.MSTeams.DAC.SM.SMTeamsTeam.TeamPhoto : Edm.String "Picture"
PX.MSTeams.DAC.SM.SMTeamsTeam.SMTeamsMemberMappingCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsMemberMapping)
PX.MSTeams.DAC.SM.SMTeamsTeam.SMTeamsChannelCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsChannel)

# PX.OAuthClient.DAC.OAuthApplication (EntityType)

Key: ApplicationID
Entity sets: PX_OAuthClient_DAC_OAuthApplication

PX.OAuthClient.DAC.OAuthApplication.ApplicationID : Edm.Int32 [key] "Application ID"
PX.OAuthClient.DAC.OAuthApplication.Type : Edm.String "Type"
PX.OAuthClient.DAC.OAuthApplication.ApplicationName : Edm.String "Application Name"
PX.OAuthClient.DAC.OAuthApplication.ClientID : Edm.String "Client ID"
PX.OAuthClient.DAC.OAuthApplication.ClientSecret : Edm.String "Client Secret"
PX.OAuthClient.DAC.OAuthApplication.IsSystem : Edm.Boolean [required] "Predefined"
PX.OAuthClient.DAC.OAuthApplication.AuthorizationEndpoint : Edm.String "Authorization Endpoint"
PX.OAuthClient.DAC.OAuthApplication.TokenEndpoint : Edm.String "Token Endpoint"
PX.OAuthClient.DAC.OAuthApplication.CustomClient : Edm.String
PX.OAuthClient.DAC.OAuthApplication.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.OAuthClient.DAC.OAuthApplication.OAuthResourceCollection -> Collection(PX.OAuthClient.DAC.OAuthResource)
PX.OAuthClient.DAC.OAuthApplication.EMailSyncServerCollection -> Collection(PX.SM.EMailSyncServer)
PX.OAuthClient.DAC.OAuthApplication.OAuthTokenCollection -> Collection(PX.OAuthClient.DAC.OAuthToken)

# PX.OAuthClient.DAC.OAuthResource (EntityType)

Label: "Application Resource"
Key: ApplicationID, ResourceCD
Entity sets: PX_OAuthClient_DAC_OAuthResource, ApplicationResource, OAuthResource
Non-filterable, non-selectable: SitemapTitle, SitemapSelectorTitle, SitemapScreenID, WorkspaceID, SubcategoryID

PX.OAuthClient.DAC.OAuthResource.ApplicationID : Edm.Int32 [key] "Application ID"
PX.OAuthClient.DAC.OAuthResource.ResourceID : Edm.Guid "ResourceID"
PX.OAuthClient.DAC.OAuthResource.ResourceCD : Edm.Int32 [key] "Resource ID"
PX.OAuthClient.DAC.OAuthResource.ResourceName : Edm.String "External Name"
PX.OAuthClient.DAC.OAuthResource.ResourceUrl : Edm.String "Resource URL"
PX.OAuthClient.DAC.OAuthResource.ResourceExtensionData : Edm.String
PX.OAuthClient.DAC.OAuthResource.SitemapTitle : Edm.String "Site Map Title"
PX.OAuthClient.DAC.OAuthResource.SitemapSelectorTitle : Edm.String "Site Map Title"
PX.OAuthClient.DAC.OAuthResource.SitemapScreenID : Edm.String "Screen ID"
PX.OAuthClient.DAC.OAuthResource.WorkspaceID : Edm.Guid "Workspace"
PX.OAuthClient.DAC.OAuthResource.SubcategoryID : Edm.Guid "Category"
PX.OAuthClient.DAC.OAuthResource.OAuthApplicationByApplicationID -> PX.OAuthClient.DAC.OAuthApplication (ApplicationID=ApplicationID)

# PX.OAuthClient.DAC.OAuthToken (EntityType)

Key: TokenID
Entity sets: PX_OAuthClient_DAC_OAuthToken
Non-filterable, non-selectable: NoteText, UtcNow, ExpiresOn

PX.OAuthClient.DAC.OAuthToken.ApplicationID : Edm.Int32 "Application ID"
PX.OAuthClient.DAC.OAuthToken.TokenID : Edm.Int32 [key] "Token ID"
PX.OAuthClient.DAC.OAuthToken.RefreshToken : Edm.String "RefreshToken"
PX.OAuthClient.DAC.OAuthToken.AccessToken : Edm.String "AccessToken"
PX.OAuthClient.DAC.OAuthToken.UtcExpiredOn : Edm.DateTimeOffset "Expires On (UTC)"
PX.OAuthClient.DAC.OAuthToken.Bearer : Edm.String "Bearer"
PX.OAuthClient.DAC.OAuthToken.NoteID : Edm.Guid
PX.OAuthClient.DAC.OAuthToken.NoteText : Edm.String "Note Text"
PX.OAuthClient.DAC.OAuthToken.UtcNow : Edm.DateTimeOffset "Now Date"
PX.OAuthClient.DAC.OAuthToken.ExpiresOn : Edm.DateTimeOffset "Expires On"
PX.OAuthClient.DAC.OAuthToken.OAuthApplicationByApplicationID -> PX.OAuthClient.DAC.OAuthApplication (ApplicationID=ApplicationID)

# PX.OAuthClient.DAC.ResourceRole (EntityType)

Label: "Role"
BaseType: PX.SM.Roles
Key: ApplicationName, Rolename (inherited from PX.SM.Roles)
Entity sets: PX_OAuthClient_DAC_ResourceRole
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.OAuthClient.DAC.ResourceRole.AccessRights : Edm.Int32 "Access Rights"

# PX.Objects.AM.AMAPSMaintenanceSetup (EntityType)

Label: "APS Maintenance Setup"
Singletons: PX_Objects_AM_AMAPSMaintenanceSetup, APSMaintenanceSetup, AMAPSMaintenanceSetup

PX.Objects.AM.AMAPSMaintenanceSetup.WorkCenterCalendarProcessLastRunDateTime : Edm.DateTimeOffset "Work Center Calendar Process Last Run Date Time"
PX.Objects.AM.AMAPSMaintenanceSetup.WorkCenterCalendarProcessLastRunByID : Edm.Guid "Work Center Calendar Process Last Run By"
PX.Objects.AM.AMAPSMaintenanceSetup.HistoryCleanupProcessLastRunDateTime : Edm.DateTimeOffset "History Cleanup Process Last Run Date Time"
PX.Objects.AM.AMAPSMaintenanceSetup.HistoryCleanupProcessLastRunByID : Edm.Guid "History Cleanup Process Last Run By"
PX.Objects.AM.AMAPSMaintenanceSetup.WorkCalendarProcessLastRunByID : Edm.Guid "Work Calendar Process Last Run By"
PX.Objects.AM.AMAPSMaintenanceSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMAPSMaintenanceSetup.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMAPSMaintenanceSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMAPSMaintenanceSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.AM.AMBatch (EntityType)

Label: "AM Batch"
Key: BatNbr, DocType
Entity sets: PX_Objects_AM_AMBatch, AMBatch
Non-filterable, non-selectable: NoteText, EditableBatch, DeletableBatch

PX.Objects.AM.AMBatch.DocType : Edm.String [key] "Document Type"
PX.Objects.AM.AMBatch.BatNbr : Edm.String [key] "Batch Nbr."
PX.Objects.AM.AMBatch.FinPeriodID : Edm.String "Post Period"
PX.Objects.AM.AMBatch.Status : Edm.String "Status"
PX.Objects.AM.AMBatch.Hold : Edm.Boolean "Hold"
PX.Objects.AM.AMBatch.ControlAmount : Edm.Decimal [required] "Control Amount"
PX.Objects.AM.AMBatch.ControlQty : Edm.Decimal [required] "Control Qty."
PX.Objects.AM.AMBatch.ControlCost : Edm.Decimal [required] "Control Cost"
PX.Objects.AM.AMBatch.TranDate : Edm.DateTimeOffset "Date"
PX.Objects.AM.AMBatch.NoteID : Edm.Guid
PX.Objects.AM.AMBatch.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBatch.OrigBatNbr : Edm.String "Orig. Batch Nbr."
PX.Objects.AM.AMBatch.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.AM.AMBatch.INRefNbr : Edm.String "IN Reference Nbr."
PX.Objects.AM.AMBatch.MaterialBatNbr : Edm.String "Material Batch Nbr."
PX.Objects.AM.AMBatch.GLBatchNbr : Edm.String "GL Batch Nbr."
PX.Objects.AM.AMBatch.TranPeriodID : Edm.String
PX.Objects.AM.AMBatch.Released : Edm.Boolean [required] "Released"
PX.Objects.AM.AMBatch.TotalAmount : Edm.Decimal [required] "Total Amount"
PX.Objects.AM.AMBatch.TotalQty : Edm.Decimal [required] "Total Qty."
PX.Objects.AM.AMBatch.TotalCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMBatch.tstamp : Edm.Binary
PX.Objects.AM.AMBatch.LineCntr : Edm.Int32 [required]
PX.Objects.AM.AMBatch.RefLineNbr : Edm.Int32 "Ref Line Nbr."
PX.Objects.AM.AMBatch.TranDesc : Edm.String "Description"
PX.Objects.AM.AMBatch.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBatch.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBatch.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBatch.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBatch.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBatch.EditableBatch : Edm.Boolean "Editable Batch"
PX.Objects.AM.AMBatch.DeletableBatch : Edm.Boolean
PX.Objects.AM.AMBatch.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.AM.AMBatch.IsLegacy : Edm.Boolean [required] "Legacy"
PX.Objects.AM.AMBatch.BatchByGLBatchNbr -> PX.Objects.GL.Batch (GLBatchNbr=BatchNbr)
PX.Objects.AM.AMBatch.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMBatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBatch.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr)
PX.Objects.AM.AMBatch.INRegisterByINRefNbr -> PX.Objects.IN.INRegister (INRefNbr=RefNbr)
PX.Objects.AM.AMBatch.AMBatchByOrigBatNbr -> PX.Objects.AM.AMBatch (OrigDocType=DocType, OrigBatNbr=BatNbr)
PX.Objects.AM.AMBatch.AMBatchByOrigDocType -> PX.Objects.AM.AMBatch (OrigBatNbr=BatNbr, OrigDocType=DocType)
PX.Objects.AM.AMBatch.AMBatchByMaterialBatNbr -> PX.Objects.AM.AMBatch (MaterialBatNbr=BatNbr)
PX.Objects.AM.AMBatch.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMBatch.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.AMBatch.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.AM.AMBatch.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.AM.AMBatch.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.AM.AMBatch.AMProdEvntCollection -> Collection(PX.Objects.AM.AMProdEvnt)
PX.Objects.AM.AMBatch.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.AM.AMBatch.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)

# PX.Objects.AM.AMBatchCost (EntityType)

Label: "AM Batch Cost"
Key: BatNbr, DocType
Entity sets: PX_Objects_AM_AMBatchCost, AMBatchCost

PX.Objects.AM.AMBatchCost.DocType : Edm.String [key] "Document Type"
PX.Objects.AM.AMBatchCost.BatNbr : Edm.String [key] "Batch Nbr."
PX.Objects.AM.AMBatchCost.FinPeriodID : Edm.String "Post Period"
PX.Objects.AM.AMBatchCost.Status : Edm.String "Status"
PX.Objects.AM.AMBatchCost.Hold : Edm.Boolean "Hold"
PX.Objects.AM.AMBatchCost.ControlAmount : Edm.Decimal "Control Amount"
PX.Objects.AM.AMBatchCost.ControlQty : Edm.Decimal "Control Qty."
PX.Objects.AM.AMBatchCost.ControlCost : Edm.Decimal "Control Cost"
PX.Objects.AM.AMBatchCost.TranDate : Edm.DateTimeOffset "Date"
PX.Objects.AM.AMBatchCost.NoteID : Edm.Guid
PX.Objects.AM.AMBatchCost.OrigBatNbr : Edm.String "Orig Batch Nbr"
PX.Objects.AM.AMBatchCost.OrigDocType : Edm.String "Orig Doc Type"
PX.Objects.AM.AMBatchCost.TranPeriodID : Edm.String
PX.Objects.AM.AMBatchCost.Released : Edm.Boolean "Released"
PX.Objects.AM.AMBatchCost.TotalAmount : Edm.Decimal "Total Amount"
PX.Objects.AM.AMBatchCost.TotalQty : Edm.Decimal "Total Qty."
PX.Objects.AM.AMBatchCost.TotalCost : Edm.Decimal "Total Cost"
PX.Objects.AM.AMBatchCost.tstamp : Edm.Binary
PX.Objects.AM.AMBatchCost.LineCntr : Edm.Int32
PX.Objects.AM.AMBatchCost.TranDesc : Edm.String "Description"
PX.Objects.AM.AMBatchCost.IsLegacy : Edm.Boolean "Legacy"
PX.Objects.AM.AMBatchCost.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBatchCost.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBatchCost.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBatchCost.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBatchCost.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBatchCost.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBatchCost.AMBatchByOrigBatNbr -> PX.Objects.AM.AMBatch (OrigDocType=DocType, OrigBatNbr=BatNbr)
PX.Objects.AM.AMBatchCost.AMBatchByOrigDocType -> PX.Objects.AM.AMBatch (OrigBatNbr=BatNbr, OrigDocType=DocType)
PX.Objects.AM.AMBatchCost.AMBatchByMaterialBatNbr -> PX.Objects.AM.AMBatch
PX.Objects.AM.AMBatchCost.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.AM.AMBatchCost.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMBatchCost.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.AMBatchCost.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.AM.AMBatchCost.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.AM.AMBatchCost.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.AM.AMBatchCost.AMProdEvntCollection -> Collection(PX.Objects.AM.AMProdEvnt)
PX.Objects.AM.AMBatchCost.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.AM.AMBatchCost.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)

# PX.Objects.AM.AMBatchItemLotSerialAttributesHeader (EntityType)

Label: "AMBatchItemLotSerialAttributesHeader"
Key: BatNbr, DocType, InventoryID, LotSerialNbr
Entity sets: PX_Objects_AM_AMBatchItemLotSerialAttributesHeader, AMBatchItemLotSerialAttributesHeader
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.DocType : Edm.String [key] "Document Type"
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.BatNbr : Edm.String [key] "Batch Nbr."
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.InventoryID : Edm.Int32 [key]
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.MfgLotSerialNbr : Edm.String "Manufacturer Lot/Serial Nbr."
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.NoteID : Edm.Guid
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.tstamp : Edm.Binary
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.AMBatchByBatNbr -> PX.Objects.AM.AMBatch (DocType=DocType, BatNbr=BatNbr)
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.INItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.IN.DAC.INItemLotSerialAttributesHeader (InventoryID=InventoryID, LotSerialNbr=LotSerialNbr)
PX.Objects.AM.AMBatchItemLotSerialAttributesHeader.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)

# PX.Objects.AM.AMBomAttribute (EntityType)

Label: "BOM Attributes"
Key: BOMID, LineNbr, RevisionID
Entity sets: PX_Objects_AM_AMBomAttribute, BOMAttributes, AMBomAttribute

PX.Objects.AM.AMBomAttribute.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomAttribute.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomAttribute.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMBomAttribute.Level : Edm.Int32 [required] "Level"
PX.Objects.AM.AMBomAttribute.AttributeID : Edm.String "Attribute ID"
PX.Objects.AM.AMBomAttribute.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMBomAttribute.Label : Edm.String "Label"
PX.Objects.AM.AMBomAttribute.Descr : Edm.String "Description"
PX.Objects.AM.AMBomAttribute.Enabled : Edm.Boolean [required] "Enabled"
PX.Objects.AM.AMBomAttribute.TransactionRequired : Edm.Boolean [required] "Transaction Required"
PX.Objects.AM.AMBomAttribute.Value : Edm.String "Value"
PX.Objects.AM.AMBomAttribute.OrderFunction : Edm.Int32 [required] "Order Function"
PX.Objects.AM.AMBomAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomAttribute.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomAttribute.RowStatus : Edm.Int32 "Change Status"
PX.Objects.AM.AMBomAttribute.tstamp : Edm.Binary
PX.Objects.AM.AMBomAttribute.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBomAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.AM.AMBomAttribute.AMBomOperByOperationID -> PX.Objects.AM.AMBomOper (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID)
PX.Objects.AM.AMBomAttribute.AMBomOperByRevisionID -> PX.Objects.AM.AMBomOper (OperationID=OperationID, BOMID=BOMID, RevisionID=RevisionID)

# PX.Objects.AM.AMBomCost (EntityType)

Label: "BOM Cost"
Key: BOMID, CuryID, RevisionID, SiteID, UserID
Entity sets: PX_Objects_AM_AMBomCost, BOMCost, AMBomCost
Non-filterable, non-selectable: DirectCost

PX.Objects.AM.AMBomCost.MatlManufacturedCost : Edm.Decimal [required] "Manufactured Material"
PX.Objects.AM.AMBomCost.MatlNonManufacturedCost : Edm.Decimal [required] "Purchase Material"
PX.Objects.AM.AMBomCost.MatlCost : Edm.Decimal [required] "Material"
PX.Objects.AM.AMBomCost.FLaborCost : Edm.Decimal [required] "Fixed Labor"
PX.Objects.AM.AMBomCost.VLaborCost : Edm.Decimal [required] "Variable Labor"
PX.Objects.AM.AMBomCost.MachCost : Edm.Decimal [required] "Machine"
PX.Objects.AM.AMBomCost.OutsideCost : Edm.Decimal [required] "Outside"
PX.Objects.AM.AMBomCost.DirectCost : Edm.Decimal [required] "Direct"
PX.Objects.AM.AMBomCost.FOvdCost : Edm.Decimal [required] "Fixed Overhead"
PX.Objects.AM.AMBomCost.VOvdCost : Edm.Decimal [required] "Variable Overhead"
PX.Objects.AM.AMBomCost.SubcontractMaterialCost : Edm.Decimal [required] "Subcontract"
PX.Objects.AM.AMBomCost.ReferenceMaterialCost : Edm.Decimal [required] "Ref. Material"
PX.Objects.AM.AMBomCost.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMBomCost.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMBomCost.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomCost.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomCost.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMBomCost.UserID : Edm.Guid [key] "User ID"
PX.Objects.AM.AMBomCost.tstamp : Edm.Binary
PX.Objects.AM.AMBomCost.ToolCost : Edm.Decimal [required] "Tools"
PX.Objects.AM.AMBomCost.LotSize : Edm.Decimal [required] "Lot Size"
PX.Objects.AM.AMBomCost.TotalCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMBomCost.MultiLevelProcess : Edm.Boolean [required] "Multi Level"
PX.Objects.AM.AMBomCost.Level : Edm.Int32 [required] "Level"
PX.Objects.AM.AMBomCost.IsDefaultBom : Edm.Boolean [required] "Default BOM"
PX.Objects.AM.AMBomCost.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomCost.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomCost.FixedLaborTime : Edm.Int32 [required] "Fixed Labor Time"
PX.Objects.AM.AMBomCost.VariableLaborTime : Edm.Int32 [required] "Variable Labor Time"
PX.Objects.AM.AMBomCost.MachineTime : Edm.Int32 [required] "Machine Time"
PX.Objects.AM.AMBomCost.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMBomCost.StdCost : Edm.Decimal [required] "Current Standard Cost"
PX.Objects.AM.AMBomCost.PendingStdCost : Edm.Decimal [required] "Pending Standard Cost"
PX.Objects.AM.AMBomCost.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMBomCost.ReplenishmentSource : Edm.String "Source"
PX.Objects.AM.AMBomCost.ValMethod : Edm.String "Valuation Method"
PX.Objects.AM.AMBomCost.HasPendingProcessed : Edm.Boolean [required] "Pending Processed"
PX.Objects.AM.AMBomCost.HasMaterialProcessed : Edm.Boolean [required] "Material Processed"
PX.Objects.AM.AMBomCost.HasArchiveProcessed : Edm.Boolean [required] "Archive Processed"
PX.Objects.AM.AMBomCost.LastCost : Edm.Decimal [required] "Last Cost"
PX.Objects.AM.AMBomCost.AvgCost : Edm.Decimal [required] "Average Cost"
PX.Objects.AM.AMBomCost.MinCost : Edm.Decimal [required] "Min. Cost"
PX.Objects.AM.AMBomCost.MaxCost : Edm.Decimal [required] "Max. Cost"
PX.Objects.AM.AMBomCost.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMBomCost.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomCost.AMBomItemByBOMID -> PX.Objects.AM.AMBomItem (RevisionID=RevisionID, BOMID=BOMID)
PX.Objects.AM.AMBomCost.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMBomCost.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMBomCost.INSubItemBySubItemID -> PX.Objects.IN.INSubItem

# PX.Objects.AM.AMBomCostHistory (EntityType)

Label: "Cost Roll History"
Key: BOMID, CuryID, RevisionID, SiteID, StartDate
Entity sets: PX_Objects_AM_AMBomCostHistory, CostRollHistory, AMBomCostHistory
Non-filterable, non-selectable: DirectCost

PX.Objects.AM.AMBomCostHistory.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomCostHistory.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomCostHistory.StartDate : Edm.DateTimeOffset [key] "Start Date"
PX.Objects.AM.AMBomCostHistory.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.AMBomCostHistory.MatlManufacturedCost : Edm.Decimal [required] "Manufactured Material"
PX.Objects.AM.AMBomCostHistory.MatlNonManufacturedCost : Edm.Decimal [required] "Purchase Material"
PX.Objects.AM.AMBomCostHistory.MatlCost : Edm.Decimal [required] "Material"
PX.Objects.AM.AMBomCostHistory.FLaborCost : Edm.Decimal [required] "Fixed Labor"
PX.Objects.AM.AMBomCostHistory.VLaborCost : Edm.Decimal [required] "Variable Labor"
PX.Objects.AM.AMBomCostHistory.MachCost : Edm.Decimal [required] "Machine"
PX.Objects.AM.AMBomCostHistory.OutsideCost : Edm.Decimal [required] "Outside"
PX.Objects.AM.AMBomCostHistory.DirectCost : Edm.Decimal [required] "Direct"
PX.Objects.AM.AMBomCostHistory.FOvdCost : Edm.Decimal [required] "Fixed Overhead"
PX.Objects.AM.AMBomCostHistory.VOvdCost : Edm.Decimal [required] "Variable Overhead"
PX.Objects.AM.AMBomCostHistory.SubcontractMaterialCost : Edm.Decimal [required] "Subcontract"
PX.Objects.AM.AMBomCostHistory.ReferenceMaterialCost : Edm.Decimal [required] "Ref. Material"
PX.Objects.AM.AMBomCostHistory.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMBomCostHistory.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMBomCostHistory.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMBomCostHistory.tstamp : Edm.Binary
PX.Objects.AM.AMBomCostHistory.ToolCost : Edm.Decimal [required] "Tools"
PX.Objects.AM.AMBomCostHistory.LotSize : Edm.Decimal [required] "Lot Size"
PX.Objects.AM.AMBomCostHistory.TotalCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMBomCostHistory.MultiLevelProcess : Edm.Boolean [required] "Multi Level"
PX.Objects.AM.AMBomCostHistory.Level : Edm.Int32 [required] "Level"
PX.Objects.AM.AMBomCostHistory.IsDefaultBom : Edm.Boolean [required] "Default BOM"
PX.Objects.AM.AMBomCostHistory.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomCostHistory.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Objects.AM.AMBomCostHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomCostHistory.FixedLaborTime : Edm.Int32 [required] "Fixed Labor Time"
PX.Objects.AM.AMBomCostHistory.VariableLaborTime : Edm.Int32 [required] "Variable Labor Time"
PX.Objects.AM.AMBomCostHistory.MachineTime : Edm.Int32 [required] "Machine Time"
PX.Objects.AM.AMBomCostHistory.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMBomCostHistory.StdCost : Edm.Decimal [required] "Current Cost"
PX.Objects.AM.AMBomCostHistory.PendingStdCost : Edm.Decimal [required] "Pending Cost"
PX.Objects.AM.AMBomCostHistory.LastModifiedDateTime : Edm.DateTimeOffset "Last Updated Date Time"
PX.Objects.AM.AMBomCostHistory.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMBomCostHistory.LastCost : Edm.Decimal [required] "Last Cost"
PX.Objects.AM.AMBomCostHistory.AvgCost : Edm.Decimal [required] "Average Cost"
PX.Objects.AM.AMBomCostHistory.MinCost : Edm.Decimal [required] "Min. Cost"
PX.Objects.AM.AMBomCostHistory.MaxCost : Edm.Decimal [required] "Max. Cost"
PX.Objects.AM.AMBomCostHistory.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMBomCostHistory.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomCostHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomCostHistory.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMBomCostHistory.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMBomCostHistory.INSubItemBySubItemID -> PX.Objects.IN.INSubItem

# PX.Objects.AM.AMBOMCurySettings (EntityType)

Label: "BOM Currency Settings"
Key: BOMID, CuryID, LineID, LineType, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBOMCurySettings, BOMCurrencySettings, AMBOMCurySettings

PX.Objects.AM.AMBOMCurySettings.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBOMCurySettings.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBOMCurySettings.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBOMCurySettings.LineID : Edm.Int32 [key] "LineID"
PX.Objects.AM.AMBOMCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMBOMCurySettings.LineType : Edm.String [key] "Line Type"
PX.Objects.AM.AMBOMCurySettings.LocationID : Edm.Int32 "Location ID"
PX.Objects.AM.AMBOMCurySettings.VendorID : Edm.Int32 "Vendor ID"
PX.Objects.AM.AMBOMCurySettings.VendorLocationID : Edm.Int32 "Vendor Location ID"
PX.Objects.AM.AMBOMCurySettings.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMBOMCurySettings.tstamp : Edm.Binary
PX.Objects.AM.AMBOMCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBOMCurySettings.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBOMCurySettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBOMCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBOMCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBOMCurySettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBOMCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBOMCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBOMCurySettings.INSiteBySiteID -> PX.Objects.IN.INSite

# PX.Objects.AM.AMBomItem (EntityType)

Label: "BOM Item"
Key: BOMID, RevisionID
Entity sets: PX_Objects_AM_AMBomItem, BOMItem, AMBomItem
Non-filterable, non-selectable: NoteText, Rejected

PX.Objects.AM.AMBomItem.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomItem.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomItem.Descr : Edm.String "Description"
PX.Objects.AM.AMBomItem.EffStartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.AMBomItem.EffEndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.AMBomItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMBomItem.NoteID : Edm.Guid
PX.Objects.AM.AMBomItem.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBomItem.LineCntrAttribute : Edm.Int32 [required]
PX.Objects.AM.AMBomItem.LineCntrOperation : Edm.Int32 [required] "Operation Line Cntr"
PX.Objects.AM.AMBomItem.tstamp : Edm.Binary
PX.Objects.AM.AMBomItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomItem.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomItem.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomItem.Status : Edm.String "Status"
PX.Objects.AM.AMBomItem.OwnerID : Edm.Int32 "Owner"
PX.Objects.AM.AMBomItem.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.AM.AMBomItem.Hold : Edm.Boolean "Hold"
PX.Objects.AM.AMBomItem.Approved : Edm.Boolean [required] "Approved"
PX.Objects.AM.AMBomItem.Rejected : Edm.Boolean
PX.Objects.AM.AMBomItem.IsProcessMFG : Edm.Boolean [required] "Process Manufacturing"
PX.Objects.AM.AMBomItem.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.AM.AMBomItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMBomItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBomItem.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.AM.AMBomItem.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMBomItem.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMBomItem.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.AM.AMBomItem.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.Objects.AM.AMBomItem.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.AM.AMBomItem.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.AM.AMBomItem.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.AM.AMBomItem.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.AM.AMBomItem.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.AM.AMBomItem.AMBomAttributeCollection -> Collection(PX.Objects.AM.AMBomAttribute)
PX.Objects.AM.AMBomItem.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.AM.AMBomItem.AMBomOvhdCollection -> Collection(PX.Objects.AM.AMBomOvhd)
PX.Objects.AM.AMBomItem.AMBomRefCollection -> Collection(PX.Objects.AM.AMBomRef)
PX.Objects.AM.AMBomItem.AMBomStepCollection -> Collection(PX.Objects.AM.AMBomStep)
PX.Objects.AM.AMBomItem.AMBomToolCollection -> Collection(PX.Objects.AM.AMBomTool)
PX.Objects.AM.AMBomItem.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.AM.AMBomItem.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.AM.AMBomItem.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.AM.AMBomItem.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.AM.AMBomItem.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.AM.AMBomItem.AMBomItem3Collection -> Collection(PX.Objects.AM.AMBomItem3)

# PX.Objects.AM.AMBomItem2 (EntityType)

Label: "BOM Item"
BaseType: PX.Objects.AM.AMBomItem
Key: BOMID, RevisionID (inherited from PX.Objects.AM.AMBomItem)
Entity sets: PX_Objects_AM_AMBomItem2, BOMItem1, AMBomItem2

# PX.Objects.AM.AMBomItem3 (EntityType)

Label: "BOM Item"
Key: BOMID, RevisionID
Entity sets: PX_Objects_AM_AMBomItem3, BOMItem2, AMBomItem3

PX.Objects.AM.AMBomItem3.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomItem3.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomItem3.Descr : Edm.String "Description"
PX.Objects.AM.AMBomItem3.EffStartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.AMBomItem3.EffEndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.AMBomItem3.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMBomItem3.Status : Edm.String "Status"
PX.Objects.AM.AMBomItem3.Hold : Edm.Boolean "Hold"
PX.Objects.AM.AMBomItem3.AMBomItemByBOMID -> PX.Objects.AM.AMBomItem (BOMID=BOMID)
PX.Objects.AM.AMBomItem3.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (RevisionID=RevisionID)

# PX.Objects.AM.AMBomItemActive (EntityType)

Label: "BOM Item Active"
BaseType: PX.Objects.AM.AMBomItem
Key: BOMID, RevisionID (inherited from PX.Objects.AM.AMBomItem)
Entity sets: PX_Objects_AM_AMBomItemActive, BOMItemActive, AMBomItemActive

# PX.Objects.AM.AMBomItemActive2 (EntityType)

Label: "BOM Item Active 2"
BaseType: PX.Objects.AM.AMBomItem
Key: BOMID, RevisionID (inherited from PX.Objects.AM.AMBomItem)
Entity sets: PX_Objects_AM_AMBomItemActive2, BOMItemActive2, AMBomItemActive2

# PX.Objects.AM.AMBomItemBomDefaults (EntityType)

Label: "BOM Item BOM Default"
Key: BOMID, RevisionID
Entity sets: PX_Objects_AM_AMBomItemBomDefaults, BOMItemBOMDefault, AMBomItemBomDefaults
Non-filterable, non-selectable: IsItemDefaultBOM, IsItemSiteDefaultBOM, IsDefaultBOM

PX.Objects.AM.AMBomItemBomDefaults.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomItemBomDefaults.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomItemBomDefaults.ItemBOMID : Edm.String "Item Default BOM ID"
PX.Objects.AM.AMBomItemBomDefaults.ItemPlanningBOMID : Edm.String "Item Planning BOM ID"
PX.Objects.AM.AMBomItemBomDefaults.ItemSiteBOMID : Edm.String "Site Default BOM ID"
PX.Objects.AM.AMBomItemBomDefaults.ItemSitePlanningBOMID : Edm.String "Site Planning BOM ID"
PX.Objects.AM.AMBomItemBomDefaults.IsItemDefaultBOM : Edm.Boolean "Item Default BOM"
PX.Objects.AM.AMBomItemBomDefaults.IsItemSiteDefaultBOM : Edm.Boolean "Site Default BOM"
PX.Objects.AM.AMBomItemBomDefaults.IsDefaultBOM : Edm.Boolean "Default BOM"
PX.Objects.AM.AMBomItemBomDefaults.ItemReplenishmentSource : Edm.String "Replenishment Source"
PX.Objects.AM.AMBomItemBomDefaults.ItemSiteReplenishmentSource : Edm.String "Replenishment Source"

# PX.Objects.AM.AMBomMatl (EntityType)

Label: "BOM Material"
Key: BOMID, CurrBOMID, CurrOperationID, CurrRevisionID, CuryID, CuryLineID, LineID, LineType, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBomMatl, BOMMaterial, AMBomMatl
Non-filterable, non-selectable: NoteText, LineNbr, PlanCost, OriginalTreeNodeID

PX.Objects.AM.AMBomMatl.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomMatl.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomMatl.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBomMatl.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMBomMatl.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMBomMatl.Descr : Edm.String "Description"
PX.Objects.AM.AMBomMatl.QtyReq : Edm.Decimal [required] "Required Qty."
PX.Objects.AM.AMBomMatl.UOM : Edm.String "UOM"
PX.Objects.AM.AMBomMatl.BaseQty : Edm.Decimal [required] "Base Qty."
PX.Objects.AM.AMBomMatl.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMBomMatl.MaterialType : Edm.Int32 [required] "Material Type"
PX.Objects.AM.AMBomMatl.PhantomRouting : Edm.Int32 [required] "Phantom Routing"
PX.Objects.AM.AMBomMatl.BFlush : Edm.Boolean [required] "Backflush Materials"
PX.Objects.AM.AMBomMatl.CompBOMID : Edm.String "Comp BOM ID"
PX.Objects.AM.AMBomMatl.CompBOMRevisionID : Edm.String "Comp BOM Revision"
PX.Objects.AM.AMBomMatl.ScrapFactor : Edm.Decimal [required] "Scrap Factor"
PX.Objects.AM.AMBomMatl.BubbleNbr : Edm.String "Bubble Nbr"
PX.Objects.AM.AMBomMatl.EffDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AM.AMBomMatl.ExpDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AM.AMBomMatl.NoteID : Edm.Guid
PX.Objects.AM.AMBomMatl.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBomMatl.tstamp : Edm.Binary
PX.Objects.AM.AMBomMatl.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomMatl.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomMatl.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomMatl.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomMatl.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomMatl.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomMatl.LineNbr : Edm.Int32 "Line Nbr. 2"
PX.Objects.AM.AMBomMatl.SortOrder : Edm.Int32 "Line Order"
PX.Objects.AM.AMBomMatl.BatchSize : Edm.Decimal [required] "Batch Size"
PX.Objects.AM.AMBomMatl.PlanCost : Edm.Decimal "Planned Cost"
PX.Objects.AM.AMBomMatl.LineCntrRef : Edm.Int32 [required]
PX.Objects.AM.AMBomMatl.RowStatus : Edm.Int32 "Change Status"
PX.Objects.AM.AMBomMatl.SubcontractSource : Edm.Int32 [required] "Subcontract Source"
PX.Objects.AM.AMBomMatl.IsStockItem : Edm.Boolean [required] "Stock"
PX.Objects.AM.AMBomMatl.OriginalTreeNodeID : Edm.String "Original Tree Node"
PX.Objects.AM.AMBomMatl.CurrBOMID : Edm.String [key] "CurrBOMID"
PX.Objects.AM.AMBomMatl.CurrRevisionID : Edm.String [key] "CurrRevisionID"
PX.Objects.AM.AMBomMatl.CurrOperationID : Edm.Int32 [key] "CurrOperationID"
PX.Objects.AM.AMBomMatl.CuryLineID : Edm.Int32 [key] "CuryLineID"
PX.Objects.AM.AMBomMatl.CuryID : Edm.String [key] "CuryID"
PX.Objects.AM.AMBomMatl.LineType : Edm.String [key] "LineType"
PX.Objects.AM.AMBomMatl.CuryCreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomMatl.CuryCreatedByScreenID : Edm.String
PX.Objects.AM.AMBomMatl.CuryCreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomMatl.CuryLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomMatl.CuryLastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomMatl.CuryLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomMatl.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMBomMatl.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomMatl.AMBomItemByCompBOMID -> PX.Objects.AM.AMBomItem (CompBOMID=BOMID)
PX.Objects.AM.AMBomMatl.AMBomItemByCompBOMRevisionID -> PX.Objects.AM.AMBomItem (CompBOMID=BOMID, CompBOMRevisionID=RevisionID)
PX.Objects.AM.AMBomMatl.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomMatl.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBomMatl.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMBomMatl.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMBomMatl.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMBomMatl.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMBomMatl.AMBomOperByOperationID -> PX.Objects.AM.AMBomOper (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID)
PX.Objects.AM.AMBomMatl.AMBomRefCollection -> Collection(PX.Objects.AM.AMBomRef)
PX.Objects.AM.AMBomMatl.AMBomMatlCuryCollection -> Collection(PX.Objects.AM.AMBomMatlCury)

# PX.Objects.AM.AMBomMatlCury (EntityType)

Label: "AMBomMatlCurrency"
Key: BOMID, CuryID, LineID, LineType, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBomMatlCury, AMBomMatlCurrency, AMBomMatlCury

PX.Objects.AM.AMBomMatlCury.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomMatlCury.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomMatlCury.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBomMatlCury.LineID : Edm.Int32 [key] "LineID"
PX.Objects.AM.AMBomMatlCury.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMBomMatlCury.LineType : Edm.String [key] "Line Type"
PX.Objects.AM.AMBomMatlCury.LocationID : Edm.Int32 "Location ID"
PX.Objects.AM.AMBomMatlCury.VendorID : Edm.Int32 "Vendor ID"
PX.Objects.AM.AMBomMatlCury.VendorLocationID : Edm.Int32 "Vendor Location ID"
PX.Objects.AM.AMBomMatlCury.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMBomMatlCury.tstamp : Edm.Binary
PX.Objects.AM.AMBomMatlCury.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomMatlCury.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomMatlCury.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomMatlCury.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomMatlCury.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomMatlCury.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomMatlCury.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMBomMatlCury.AMBomMatlByLineID -> PX.Objects.AM.AMBomMatl (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID, LineID=LineID)

# PX.Objects.AM.AMBomOper (EntityType)

Label: "BOM Operation"
Key: BOMID, OperationCD, RevisionID
Entity sets: PX_Objects_AM_AMBomOper, BOMOperation, AMBomOper
Non-filterable, non-selectable: NoteText, SetupTimeRaw, RunUnitTimeRaw, MachineUnitTimeRaw, QueueTimeRaw, FinishTimeRaw, MoveTimeRaw, NewOperationCD, OriginalTreeNodeID

PX.Objects.AM.AMBomOper.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomOper.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomOper.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMBomOper.OperationCD : Edm.String [key] "Operation ID"
PX.Objects.AM.AMBomOper.Descr : Edm.String "Oper Desc"
PX.Objects.AM.AMBomOper.WcID : Edm.String "Work Center"
PX.Objects.AM.AMBomOper.SetupTime : Edm.Int32 [required] "Setup Time"
PX.Objects.AM.AMBomOper.RunUnitTime : Edm.Int32 [required] "Run Time"
PX.Objects.AM.AMBomOper.RunUnits : Edm.Decimal [required] "Run Units"
PX.Objects.AM.AMBomOper.MachineUnitTime : Edm.Int32 [required] "Machine Time"
PX.Objects.AM.AMBomOper.MachineUnits : Edm.Decimal [required] "Machine Units"
PX.Objects.AM.AMBomOper.QueueTime : Edm.Int32 [required] "Queue Time"
PX.Objects.AM.AMBomOper.FinishTime : Edm.Int32 [required] "Finish Time"
PX.Objects.AM.AMBomOper.BFlush : Edm.Boolean [required] "Backflush Labor"
PX.Objects.AM.AMBomOper.LineCntrMatl : Edm.Int32 [required]
PX.Objects.AM.AMBomOper.LineCntrOvhd : Edm.Int32 [required]
PX.Objects.AM.AMBomOper.LineCntrStep : Edm.Int32 [required]
PX.Objects.AM.AMBomOper.LineCntrTool : Edm.Int32 [required]
PX.Objects.AM.AMBomOper.NoteID : Edm.Guid
PX.Objects.AM.AMBomOper.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBomOper.tstamp : Edm.Binary
PX.Objects.AM.AMBomOper.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomOper.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomOper.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomOper.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomOper.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomOper.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomOper.ScrapAction : Edm.Int32 [required] "Scrap Action"
PX.Objects.AM.AMBomOper.RowStatus : Edm.Int32 "Change Status"
PX.Objects.AM.AMBomOper.MoveTime : Edm.Int32 [required] "Move Time"
PX.Objects.AM.AMBomOper.ControlPoint : Edm.Boolean "Control Point"
PX.Objects.AM.AMBomOper.SetupTimeRaw : Edm.Int32 "SetupTimeRaw"
PX.Objects.AM.AMBomOper.RunUnitTimeRaw : Edm.Int32 "RunUnitTimeRaw"
PX.Objects.AM.AMBomOper.MachineUnitTimeRaw : Edm.Int32 "MachineUnitTimeRaw"
PX.Objects.AM.AMBomOper.QueueTimeRaw : Edm.Int32 "QueueTimeRaw"
PX.Objects.AM.AMBomOper.FinishTimeRaw : Edm.Int32 "FinishTimeRaw"
PX.Objects.AM.AMBomOper.MoveTimeRaw : Edm.Int32 "MoveTimeRaw"
PX.Objects.AM.AMBomOper.OutsideProcess : Edm.Boolean [required] "Outside Process"
PX.Objects.AM.AMBomOper.DropShippedToVendor : Edm.Boolean [required] "Drop Shipped to Vendor"
PX.Objects.AM.AMBomOper.VendorID : Edm.Int32 "Vendor"
PX.Objects.AM.AMBomOper.NewOperationCD : Edm.String "New Operation ID"
PX.Objects.AM.AMBomOper.OriginalTreeNodeID : Edm.String "Original Tree Node"
PX.Objects.AM.AMBomOper.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AM.AMBomOper.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomOper.AMBomItemByBOMID -> PX.Objects.AM.AMBomItem (BOMID=BOMID)
PX.Objects.AM.AMBomOper.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomOper.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBomOper.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.AM.AMBomOper.LocationByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.AM.AMBomOper.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)
PX.Objects.AM.AMBomOper.AMBomAttributeCollection -> Collection(PX.Objects.AM.AMBomAttribute)
PX.Objects.AM.AMBomOper.AMBomOvhdCollection -> Collection(PX.Objects.AM.AMBomOvhd)
PX.Objects.AM.AMBomOper.AMBomStepCollection -> Collection(PX.Objects.AM.AMBomStep)
PX.Objects.AM.AMBomOper.AMBomToolCollection -> Collection(PX.Objects.AM.AMBomTool)
PX.Objects.AM.AMBomOper.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.AM.AMBomOper.AMBomOperCuryCollection -> Collection(PX.Objects.AM.AMBomOperCury)
PX.Objects.AM.AMBomOper.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)

# PX.Objects.AM.AMBomOperCury (EntityType)

Label: "AMBomOperCurrency"
Key: BOMID, CuryID, LineID, LineType, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBomOperCury, AMBomOperCurrency, AMBomOperCury

PX.Objects.AM.AMBomOperCury.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomOperCury.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomOperCury.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBomOperCury.LineID : Edm.Int32 [key] "LineID"
PX.Objects.AM.AMBomOperCury.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMBomOperCury.LineType : Edm.String [key] "Line Type"
PX.Objects.AM.AMBomOperCury.LocationID : Edm.Int32 "Location ID"
PX.Objects.AM.AMBomOperCury.VendorID : Edm.Int32 "Vendor"
PX.Objects.AM.AMBomOperCury.tstamp : Edm.Binary
PX.Objects.AM.AMBomOperCury.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomOperCury.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomOperCury.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomOperCury.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomOperCury.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomOperCury.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomOperCury.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMBomOperCury.LocationByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.AM.AMBomOperCury.AMBomOperByOperationID -> PX.Objects.AM.AMBomOper (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID)

# PX.Objects.AM.AMBomOvhd (EntityType)

Label: "BOM Overhead"
Key: BOMID, LineID, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBomOvhd, BOMOverhead, AMBomOvhd
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMBomOvhd.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomOvhd.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomOvhd.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBomOvhd.LineID : Edm.Int32 [key] "LineID"
PX.Objects.AM.AMBomOvhd.NoteID : Edm.Guid
PX.Objects.AM.AMBomOvhd.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBomOvhd.OFactor : Edm.Decimal [required] "Factor"
PX.Objects.AM.AMBomOvhd.OvhdID : Edm.String "Overhead ID"
PX.Objects.AM.AMBomOvhd.tstamp : Edm.Binary
PX.Objects.AM.AMBomOvhd.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomOvhd.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomOvhd.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomOvhd.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomOvhd.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomOvhd.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomOvhd.RowStatus : Edm.Int32 "Change Status"
PX.Objects.AM.AMBomOvhd.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomOvhd.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomOvhd.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBomOvhd.AMBomOperByOperationID -> PX.Objects.AM.AMBomOper (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID)
PX.Objects.AM.AMBomOvhd.AMOverheadByOvhdID -> PX.Objects.AM.AMOverhead (OvhdID=OvhdID)

# PX.Objects.AM.AMBomRef (EntityType)

Label: "BOM Reference Designator"
Key: BOMID, LineID, MatlLineID, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBomRef, BOMReferenceDesignator, AMBomRef
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMBomRef.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomRef.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomRef.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBomRef.MatlLineID : Edm.Int32 [key] "Material Line ID"
PX.Objects.AM.AMBomRef.LineID : Edm.Int32 [key] "Line ID"
PX.Objects.AM.AMBomRef.Descr : Edm.String "Description"
PX.Objects.AM.AMBomRef.NoteID : Edm.Guid
PX.Objects.AM.AMBomRef.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBomRef.RefDes : Edm.String "Ref Des"
PX.Objects.AM.AMBomRef.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomRef.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomRef.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomRef.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomRef.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomRef.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomRef.RowStatus : Edm.Int32 "Change Status"
PX.Objects.AM.AMBomRef.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomRef.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomRef.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBomRef.AMBomMatlByMatlLineID -> PX.Objects.AM.AMBomMatl (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID, MatlLineID=LineID)

# PX.Objects.AM.AMBomStep (EntityType)

Label: "BOM Step"
Key: BOMID, LineID, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBomStep, BOMStep, AMBomStep
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMBomStep.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomStep.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomStep.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBomStep.Descr : Edm.String "Description"
PX.Objects.AM.AMBomStep.LineID : Edm.Int32 [key] "LineID"
PX.Objects.AM.AMBomStep.NoteID : Edm.Guid
PX.Objects.AM.AMBomStep.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBomStep.tstamp : Edm.Binary
PX.Objects.AM.AMBomStep.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomStep.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomStep.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomStep.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomStep.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomStep.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomStep.RowStatus : Edm.Int32 "Change Status"
PX.Objects.AM.AMBomStep.SortOrder : Edm.Int32 "Line Order"
PX.Objects.AM.AMBomStep.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomStep.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomStep.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBomStep.AMBomOperByOperationID -> PX.Objects.AM.AMBomOper (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID)

# PX.Objects.AM.AMBomTool (EntityType)

Label: "BOM Tool"
Key: BOMID, LineID, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBomTool, BOMTool, AMBomTool
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMBomTool.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomTool.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomTool.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBomTool.ToolID : Edm.String "Tool ID"
PX.Objects.AM.AMBomTool.Descr : Edm.String "Description"
PX.Objects.AM.AMBomTool.LineID : Edm.Int32 [key] "Line ID"
PX.Objects.AM.AMBomTool.NoteID : Edm.Guid
PX.Objects.AM.AMBomTool.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMBomTool.QtyReq : Edm.Decimal [required] "Required Qty."
PX.Objects.AM.AMBomTool.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMBomTool.tstamp : Edm.Binary
PX.Objects.AM.AMBomTool.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomTool.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomTool.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomTool.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomTool.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomTool.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomTool.RowStatus : Edm.Int32 "Change Status"
PX.Objects.AM.AMBomTool.AMBomItemByRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, RevisionID=RevisionID)
PX.Objects.AM.AMBomTool.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMBomTool.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMBomTool.AMBomOperByOperationID -> PX.Objects.AM.AMBomOper (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID)
PX.Objects.AM.AMBomTool.AMToolMstByToolID -> PX.Objects.AM.AMToolMst (ToolID=ToolID)
PX.Objects.AM.AMBomTool.AMBomToolCuryCollection -> Collection(PX.Objects.AM.AMBomToolCury)

# PX.Objects.AM.AMBomToolCury (EntityType)

Label: "AMBomToolCurrency"
Key: BOMID, CuryID, LineID, LineType, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMBomToolCury, AMBomToolCurrency, AMBomToolCury

PX.Objects.AM.AMBomToolCury.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.AMBomToolCury.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMBomToolCury.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMBomToolCury.LineID : Edm.Int32 [key] "LineID"
PX.Objects.AM.AMBomToolCury.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMBomToolCury.LineType : Edm.String [key] "Line Type"
PX.Objects.AM.AMBomToolCury.LocationID : Edm.Int32 "Location ID"
PX.Objects.AM.AMBomToolCury.VendorID : Edm.Int32 "Vendor ID"
PX.Objects.AM.AMBomToolCury.VendorLocationID : Edm.Int32 "Vendor Location ID"
PX.Objects.AM.AMBomToolCury.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMBomToolCury.tstamp : Edm.Binary
PX.Objects.AM.AMBomToolCury.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMBomToolCury.CreatedByScreenID : Edm.String
PX.Objects.AM.AMBomToolCury.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomToolCury.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMBomToolCury.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMBomToolCury.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMBomToolCury.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMBomToolCury.AMBomToolByLineID -> PX.Objects.AM.AMBomTool (BOMID=BOMID, RevisionID=RevisionID, OperationID=OperationID, LineID=LineID)

# PX.Objects.AM.AMBSetup (EntityType)

Label: "BOM Preferences"
Singletons: PX_Objects_AM_AMBSetup, BOMPreferences, AMBSetup

PX.Objects.AM.AMBSetup.BOMNumberingID : Edm.String "BOM Numbering Sequence"
PX.Objects.AM.AMBSetup.DuplicateItemOnBOM : Edm.String "Duplicates on BOM"
PX.Objects.AM.AMBSetup.DuplicateItemOnOper : Edm.String "Duplicates on Operation"
PX.Objects.AM.AMBSetup.LastLowLevelCompletedDateTime : Edm.DateTimeOffset "Last Low Level Completed At"
PX.Objects.AM.AMBSetup.LastMaxLowLevel : Edm.Int32 "Last Max Low Level"
PX.Objects.AM.AMBSetup.WcID : Edm.String "Default Work Center"
PX.Objects.AM.AMBSetup.tstamp : Edm.Binary
PX.Objects.AM.AMBSetup.OperationTimeFormat : Edm.Int32 [required] "Operation Time Format"
PX.Objects.AM.AMBSetup.ProductionTimeFormat : Edm.Int32 [required] "Total Time Format"
PX.Objects.AM.AMBSetup.DefaultRevisionID : Edm.String "Default Revision"
PX.Objects.AM.AMBSetup.ECRRequestApproval : Edm.Boolean [required] "Require ECR Approval"
PX.Objects.AM.AMBSetup.ECORequestApproval : Edm.Boolean [required] "Require ECO Approval"
PX.Objects.AM.AMBSetup.AllowArchiveWithoutUpdatePending : Edm.Boolean [required] "Allow Archive without Updating Pending Costs"
PX.Objects.AM.AMBSetup.AutoArchiveWhenUpdatePending : Edm.Boolean [required] "Allow Archive when Updating Pending Costs"
PX.Objects.AM.AMBSetup.BOMHoldRevisionsOnEntry : Edm.Boolean [required] "Hold BOM Revisions on Entry"
PX.Objects.AM.AMBSetup.DefaultMoveTime : Edm.Int32 [required] "Default Move Time"
PX.Objects.AM.AMBSetup.DefaultQueueTime : Edm.Int32 [required] "Default Queue Time"
PX.Objects.AM.AMBSetup.DefaultFinishTime : Edm.Int32 [required] "Default Finish Time"
PX.Objects.AM.AMBSetup.NumberingByBOMNumberingID -> PX.Objects.CS.Numbering (BOMNumberingID=NumberingID)
PX.Objects.AM.AMBSetup.NumberingByECRNumberingID -> PX.Objects.CS.Numbering
PX.Objects.AM.AMBSetup.NumberingByECONumberingID -> PX.Objects.CS.Numbering
PX.Objects.AM.AMBSetup.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)

# PX.Objects.AM.AMCalendarBreakTime (EntityType)

Label: "Calendar Break Time"
BaseType: PX.Objects.CS.CSCalendarBreakTime
Key: CalendarID, DayOfWeek, StartTime (inherited from PX.Objects.CS.CSCalendarBreakTime)
Entity sets: PX_Objects_AM_AMCalendarBreakTime, CalendarBreakTime, AMCalendarBreakTime

# PX.Objects.AM.AMClockItem (EntityType)

Label: "Clock Employee"
Key: EmployeeID
Entity sets: PX_Objects_AM_AMClockItem, ClockEmployee, AMClockItem
Non-filterable, non-selectable: LaborTime, NoteText, IsClockedIn

PX.Objects.AM.AMClockItem.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.AM.AMClockItem.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMClockItem.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMClockItem.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMClockItem.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMClockItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMClockItem.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.AM.AMClockItem.Qty : Edm.Decimal "Quantity"
PX.Objects.AM.AMClockItem.UOM : Edm.String "UOM"
PX.Objects.AM.AMClockItem.BaseQty : Edm.Decimal [required] "Base Qty."
PX.Objects.AM.AMClockItem.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.AMClockItem.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.AMClockItem.LaborTime : Edm.Int32 "Duration"
PX.Objects.AM.AMClockItem.LastOper : Edm.Boolean [required] "Is Last Oper"
PX.Objects.AM.AMClockItem.LotSerCntr : Edm.Int32 [required] "LotSerCntr"
PX.Objects.AM.AMClockItem.NoteID : Edm.Guid
PX.Objects.AM.AMClockItem.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMClockItem.ShiftCD : Edm.String "Shift"
PX.Objects.AM.AMClockItem.tstamp : Edm.Binary
PX.Objects.AM.AMClockItem.InvtMult : Edm.Int16 [required] "Multiplier"
PX.Objects.AM.AMClockItem.TranDesc : Edm.String "Tran Description"
PX.Objects.AM.AMClockItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMClockItem.CreatedByScreenID : Edm.String
PX.Objects.AM.AMClockItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMClockItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMClockItem.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMClockItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMClockItem.LineCntr : Edm.Int32 [required]
PX.Objects.AM.AMClockItem.UnassignedQty : Edm.Decimal [required]
PX.Objects.AM.AMClockItem.IsClockedIn : Edm.Boolean "Is Clocked In"
PX.Objects.AM.AMClockItem.CostCenterID : Edm.Int32 "Cost Center"
PX.Objects.AM.AMClockItem.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AM.AMClockItem.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.AM.AMClockItem.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AM.AMClockItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMClockItem.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMClockItem.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMClockItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMClockItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMClockItem.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMClockItem.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMClockItem.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMClockItem.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMClockItem.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMClockItem.EPShiftCodeByShiftCD -> PX.Objects.EP.EPShiftCode (ShiftCD=ShiftCD)
PX.Objects.AM.AMClockItem.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMClockItem.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMClockItem.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.AM.AMClockItem.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.AM.AMClockItem.AMClockItemSplitCollection -> Collection(PX.Objects.AM.AMClockItemSplit)

# PX.Objects.AM.AMClockItemSplit (EntityType)

Label: "Clock Employee Split"
Key: EmployeeID, LineNbr, SplitLineNbr
Entity sets: PX_Objects_AM_AMClockItemSplit, ClockEmployeeSplit, AMClockItemSplit
Non-filterable, non-selectable: LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.AM.AMClockItemSplit.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.AM.AMClockItemSplit.TranType : Edm.String
PX.Objects.AM.AMClockItemSplit.LineNbr : Edm.Int32 [key]
PX.Objects.AM.AMClockItemSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.AM.AMClockItemSplit.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.AM.AMClockItemSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMClockItemSplit.LotSerClassID : Edm.String
PX.Objects.AM.AMClockItemSplit.AssignedNbr : Edm.String
PX.Objects.AM.AMClockItemSplit.InvtMult : Edm.Int16
PX.Objects.AM.AMClockItemSplit.Released : Edm.Boolean
PX.Objects.AM.AMClockItemSplit.UOM : Edm.String "UOM"
PX.Objects.AM.AMClockItemSplit.Qty : Edm.Decimal "Quantity"
PX.Objects.AM.AMClockItemSplit.BaseQty : Edm.Decimal
PX.Objects.AM.AMClockItemSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMClockItemSplit.CreatedByScreenID : Edm.String
PX.Objects.AM.AMClockItemSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMClockItemSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMClockItemSplit.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMClockItemSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMClockItemSplit.tstamp : Edm.Binary
PX.Objects.AM.AMClockItemSplit.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.AMClockItemSplit.TaskID : Edm.Int32 "Task"
PX.Objects.AM.AMClockItemSplit.IsStockItem : Edm.Boolean "Stock Item"
PX.Objects.AM.AMClockItemSplit.IsAllocated : Edm.Boolean "Allocated"
PX.Objects.AM.AMClockItemSplit.AMClockItemByEmployeeID -> PX.Objects.AM.AMClockItem (EmployeeID=EmployeeID)
PX.Objects.AM.AMClockItemSplit.AMClockTranByEmployeeID -> PX.Objects.AM.AMClockTran (LineNbr=LineNbr, EmployeeID=EmployeeID)

# PX.Objects.AM.AMClockTran (EntityType)

Label: "Clock Transaction"
Key: EmployeeID, LineNbr
Entity sets: PX_Objects_AM_AMClockTran, ClockTransaction, AMClockTran
Non-filterable, non-selectable: NoteText, IsStockItem, LaborTimeSeconds, Duration

PX.Objects.AM.AMClockTran.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.AM.AMClockTran.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMClockTran.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMClockTran.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMClockTran.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMClockTran.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMClockTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMClockTran.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.AM.AMClockTran.Qty : Edm.Decimal "Quantity"
PX.Objects.AM.AMClockTran.UOM : Edm.String "UOM"
PX.Objects.AM.AMClockTran.BaseQty : Edm.Decimal [required] "Base Qty."
PX.Objects.AM.AMClockTran.Closeflg : Edm.Boolean [required] "Approved"
PX.Objects.AM.AMClockTran.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.AMClockTran.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.AMClockTran.LaborTime : Edm.Int32 "Labor Time"
PX.Objects.AM.AMClockTran.LastOper : Edm.Boolean [required] "Is Last Oper"
PX.Objects.AM.AMClockTran.LotSerCntr : Edm.Int32 [required] "LotSerCntr"
PX.Objects.AM.AMClockTran.NoteID : Edm.Guid
PX.Objects.AM.AMClockTran.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMClockTran.ShiftCD : Edm.String "Shift"
PX.Objects.AM.AMClockTran.tstamp : Edm.Binary
PX.Objects.AM.AMClockTran.InvtMult : Edm.Int16 [required] "Multiplier"
PX.Objects.AM.AMClockTran.TranDesc : Edm.String "Tran Description"
PX.Objects.AM.AMClockTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMClockTran.CreatedByScreenID : Edm.String
PX.Objects.AM.AMClockTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMClockTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMClockTran.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMClockTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMClockTran.UnassignedQty : Edm.Decimal
PX.Objects.AM.AMClockTran.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.AM.AMClockTran.Status : Edm.String "Status"
PX.Objects.AM.AMClockTran.IsLotSerialPreassigned : Edm.Boolean "Lot/Serial Nbr. Preassigned"
PX.Objects.AM.AMClockTran.BaseQtyScrapped : Edm.Decimal "Scrapped Base Qty."
PX.Objects.AM.AMClockTran.QtyScrapped : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.AMClockTran.ReasonCodeID : Edm.String "Reason Code"
PX.Objects.AM.AMClockTran.ScrapAction : Edm.Int32 "Scrap Action"
PX.Objects.AM.AMClockTran.FinPeriodID : Edm.String "Post Period"
PX.Objects.AM.AMClockTran.WcID : Edm.String "Work Center"
PX.Objects.AM.AMClockTran.AllowMultiClockEntry : Edm.Boolean "Multiple Entries Allowed"
PX.Objects.AM.AMClockTran.LaborTimeSeconds : Edm.Int32 "Labor Time Seconds"
PX.Objects.AM.AMClockTran.Duration : Edm.Int32 "Duration"
PX.Objects.AM.AMClockTran.CostCenterID : Edm.Int32 "Cost Center ID"
PX.Objects.AM.AMClockTran.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AM.AMClockTran.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.AM.AMClockTran.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AM.AMClockTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMClockTran.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMClockTran.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMClockTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMClockTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMClockTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMClockTran.ReasonCodeByReasonCodeID -> PX.Objects.CS.ReasonCode (ReasonCodeID=ReasonCodeID)
PX.Objects.AM.AMClockTran.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMClockTran.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMClockTran.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMClockTran.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMClockTran.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMClockTran.EPShiftCodeByShiftCD -> PX.Objects.EP.EPShiftCode (ShiftCD=ShiftCD)
PX.Objects.AM.AMClockTran.AMClockItemByEmployeeID -> PX.Objects.AM.AMClockItem (EmployeeID=EmployeeID)
PX.Objects.AM.AMClockTran.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMClockTran.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMClockTran.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMClockTran.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)
PX.Objects.AM.AMClockTran.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.AM.AMClockTran.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)

# PX.Objects.AM.AMClockTranSplit (EntityType)

Label: "Clock Transaction Split"
Key: EmployeeID, LineNbr, SplitLineNbr
Entity sets: PX_Objects_AM_AMClockTranSplit, ClockTransactionSplit, AMClockTranSplit
Non-filterable, non-selectable: LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.AM.AMClockTranSplit.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.AM.AMClockTranSplit.TranType : Edm.String
PX.Objects.AM.AMClockTranSplit.LineNbr : Edm.Int32 [key]
PX.Objects.AM.AMClockTranSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.AM.AMClockTranSplit.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.AM.AMClockTranSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMClockTranSplit.LotSerClassID : Edm.String
PX.Objects.AM.AMClockTranSplit.AssignedNbr : Edm.String
PX.Objects.AM.AMClockTranSplit.InvtMult : Edm.Int16
PX.Objects.AM.AMClockTranSplit.Released : Edm.Boolean [required]
PX.Objects.AM.AMClockTranSplit.UOM : Edm.String "UOM"
PX.Objects.AM.AMClockTranSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMClockTranSplit.BaseQty : Edm.Decimal
PX.Objects.AM.AMClockTranSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMClockTranSplit.CreatedByScreenID : Edm.String
PX.Objects.AM.AMClockTranSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMClockTranSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMClockTranSplit.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMClockTranSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMClockTranSplit.tstamp : Edm.Binary
PX.Objects.AM.AMClockTranSplit.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.AMClockTranSplit.TaskID : Edm.Int32 "Task"
PX.Objects.AM.AMClockTranSplit.IsStockItem : Edm.Boolean "Stock Item"
PX.Objects.AM.AMClockTranSplit.IsAllocated : Edm.Boolean [required] "Allocated"
PX.Objects.AM.AMClockTranSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMClockTranSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMClockTranSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMClockTranSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMClockTranSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMClockTranSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMClockTranSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMClockTranSplit.AMClockTranByEmployeeID -> PX.Objects.AM.AMClockTran (LineNbr=LineNbr, EmployeeID=EmployeeID)
PX.Objects.AM.AMClockTranSplit.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID)

# PX.Objects.AM.AMConfigResultsAttribute (EntityType)

Label: "Configuration Attribute Result"
Key: AttributeLineNbr, ConfigResultsID
Entity sets: PX_Objects_AM_AMConfigResultsAttribute, ConfigurationAttributeResult, AMConfigResultsAttribute

PX.Objects.AM.AMConfigResultsAttribute.ConfigResultsID : Edm.Int32 [key] "Config Results ID"
PX.Objects.AM.AMConfigResultsAttribute.ConfigurationID : Edm.String "Configuration ID"
PX.Objects.AM.AMConfigResultsAttribute.Revision : Edm.String "Revision"
PX.Objects.AM.AMConfigResultsAttribute.AttributeLineNbr : Edm.Int32 [key] "Attribute Line Nbr"
PX.Objects.AM.AMConfigResultsAttribute.AttributeID : Edm.String "Attribute ID"
PX.Objects.AM.AMConfigResultsAttribute.Parent : Edm.String "Parent"
PX.Objects.AM.AMConfigResultsAttribute.Value : Edm.String "Value"
PX.Objects.AM.AMConfigResultsAttribute.Enabled : Edm.Boolean [required] "Enabled"
PX.Objects.AM.AMConfigResultsAttribute.Required : Edm.Boolean [required] "Required"
PX.Objects.AM.AMConfigResultsAttribute.Visible : Edm.Boolean [required] "Visible"
PX.Objects.AM.AMConfigResultsAttribute.RuleValid : Edm.Boolean [required]
PX.Objects.AM.AMConfigResultsAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigResultsAttribute.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigResultsAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigResultsAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigResultsAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigResultsAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigResultsAttribute.tstamp : Edm.Binary
PX.Objects.AM.AMConfigResultsAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigResultsAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigResultsAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.AM.AMConfigResultsAttribute.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigResultsAttribute.AMConfigurationAttributeByAttributeLineNbr -> PX.Objects.AM.AMConfigurationAttribute (ConfigurationID=ConfigurationID, Revision=Revision, AttributeLineNbr=LineNbr)
PX.Objects.AM.AMConfigResultsAttribute.AMConfigurationResultsByConfigResultsID -> PX.Objects.AM.AMConfigurationResults (ConfigResultsID=ConfigResultsID)

# PX.Objects.AM.AMConfigResultsFeature (EntityType)

Label: "Configuration Feature Result"
Key: ConfigResultsID, FeatureLineNbr
Entity sets: PX_Objects_AM_AMConfigResultsFeature, ConfigurationFeatureResult, AMConfigResultsFeature
Non-filterable, non-selectable: MinMaxSelection, MinLotMaxQty

PX.Objects.AM.AMConfigResultsFeature.ConfigResultsID : Edm.Int32 [key] "Config Results ID"
PX.Objects.AM.AMConfigResultsFeature.FeatureLineNbr : Edm.Int32 [key] "Feature Line Nbr"
PX.Objects.AM.AMConfigResultsFeature.ConfigurationID : Edm.String "Configuration ID"
PX.Objects.AM.AMConfigResultsFeature.Revision : Edm.String "Revision"
PX.Objects.AM.AMConfigResultsFeature.TotalQty : Edm.Decimal "Total Qty."
PX.Objects.AM.AMConfigResultsFeature.Required : Edm.Boolean [required] "Required"
PX.Objects.AM.AMConfigResultsFeature.Completed : Edm.Boolean [required] "Completed"
PX.Objects.AM.AMConfigResultsFeature.RuleValid : Edm.Boolean [required]
PX.Objects.AM.AMConfigResultsFeature.MinSelection : Edm.Int32 "Min Selection"
PX.Objects.AM.AMConfigResultsFeature.MaxSelection : Edm.Int32 "Max Selection"
PX.Objects.AM.AMConfigResultsFeature.MinQty : Edm.Decimal "Min. Qty."
PX.Objects.AM.AMConfigResultsFeature.MaxQty : Edm.Decimal "Max. Qty."
PX.Objects.AM.AMConfigResultsFeature.LotQty : Edm.Decimal "Lot Qty."
PX.Objects.AM.AMConfigResultsFeature.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigResultsFeature.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigResultsFeature.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigResultsFeature.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigResultsFeature.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigResultsFeature.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigResultsFeature.tstamp : Edm.Binary
PX.Objects.AM.AMConfigResultsFeature.MinMaxSelection : Edm.String "Min/Max Selection"
PX.Objects.AM.AMConfigResultsFeature.MinLotMaxQty : Edm.String "Min./Lot/Max. Qty."
PX.Objects.AM.AMConfigResultsFeature.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigResultsFeature.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigResultsFeature.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigResultsFeature.AMConfigurationFeatureByFeatureLineNbr -> PX.Objects.AM.AMConfigurationFeature (ConfigurationID=ConfigurationID, Revision=Revision, FeatureLineNbr=LineNbr)
PX.Objects.AM.AMConfigResultsFeature.AMConfigurationResultsByConfigResultsID -> PX.Objects.AM.AMConfigurationResults (ConfigResultsID=ConfigResultsID)
PX.Objects.AM.AMConfigResultsFeature.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)

# PX.Objects.AM.AMConfigResultsOption (EntityType)

Label: "Configuration Option Result"
Key: ConfigResultsID, FeatureLineNbr, OptionLineNbr
Entity sets: PX_Objects_AM_AMConfigResultsOption, ConfigurationOptionResult, AMConfigResultsOption
Non-filterable, non-selectable: ActualQty, IsRemovable, MinLotMaxQty

PX.Objects.AM.AMConfigResultsOption.ConfigResultsID : Edm.Int32 [key] "Config Results ID"
PX.Objects.AM.AMConfigResultsOption.ConfigurationID : Edm.String "Configuration ID"
PX.Objects.AM.AMConfigResultsOption.Revision : Edm.String "Revision"
PX.Objects.AM.AMConfigResultsOption.FeatureLineNbr : Edm.Int32 [key] "Feature Line Nbr"
PX.Objects.AM.AMConfigResultsOption.OptionLineNbr : Edm.Int32 [key required] "Option Line Nbr"
PX.Objects.AM.AMConfigResultsOption.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMConfigResultsOption.UOM : Edm.String "UOM"
PX.Objects.AM.AMConfigResultsOption.Qty : Edm.Decimal "Qty"
PX.Objects.AM.AMConfigResultsOption.ActualQty : Edm.Decimal
PX.Objects.AM.AMConfigResultsOption.CuryInfoID : Edm.Int64
PX.Objects.AM.AMConfigResultsOption.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.AM.AMConfigResultsOption.UnitPrice : Edm.Decimal
PX.Objects.AM.AMConfigResultsOption.CuryExtPrice : Edm.Decimal "Cfg. Ext. Price"
PX.Objects.AM.AMConfigResultsOption.ExtPrice : Edm.Decimal "Cfg Ext Price"
PX.Objects.AM.AMConfigResultsOption.Available : Edm.Boolean [required] "Available"
PX.Objects.AM.AMConfigResultsOption.Included : Edm.Boolean [required] "Included"
PX.Objects.AM.AMConfigResultsOption.FixedInclude : Edm.Boolean [required] "Fixed Include"
PX.Objects.AM.AMConfigResultsOption.ManualInclude : Edm.Boolean [required] "Manual Include"
PX.Objects.AM.AMConfigResultsOption.IsRemovable : Edm.Boolean "Is Removable"
PX.Objects.AM.AMConfigResultsOption.Required : Edm.Boolean [required] "Required"
PX.Objects.AM.AMConfigResultsOption.RuleValid : Edm.Boolean [required]
PX.Objects.AM.AMConfigResultsOption.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigResultsOption.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigResultsOption.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigResultsOption.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigResultsOption.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigResultsOption.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigResultsOption.tstamp : Edm.Binary
PX.Objects.AM.AMConfigResultsOption.QtyRequired : Edm.Decimal "Required Qty."
PX.Objects.AM.AMConfigResultsOption.MinQty : Edm.Decimal "Min. Qty."
PX.Objects.AM.AMConfigResultsOption.MaxQty : Edm.Decimal "Max. Qty."
PX.Objects.AM.AMConfigResultsOption.LotQty : Edm.Decimal "Lot Qty."
PX.Objects.AM.AMConfigResultsOption.ScrapFactor : Edm.Decimal "Scrap Factor"
PX.Objects.AM.AMConfigResultsOption.PriceFactor : Edm.Decimal "Price Factor"
PX.Objects.AM.AMConfigResultsOption.MaterialType : Edm.Int32 [required] "Material Type"
PX.Objects.AM.AMConfigResultsOption.MinLotMaxQty : Edm.String "Min./Lot/Max. Qty."
PX.Objects.AM.AMConfigResultsOption.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMConfigResultsOption.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigResultsOption.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigResultsOption.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMConfigResultsOption.AMConfigResultsFeatureByFeatureLineNbr -> PX.Objects.AM.AMConfigResultsFeature (ConfigResultsID=ConfigResultsID, FeatureLineNbr=FeatureLineNbr)
PX.Objects.AM.AMConfigResultsOption.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigResultsOption.AMConfigurationFeatureByFeatureLineNbr -> PX.Objects.AM.AMConfigurationFeature (ConfigurationID=ConfigurationID, Revision=Revision, FeatureLineNbr=LineNbr)
PX.Objects.AM.AMConfigResultsOption.AMConfigurationOptionByOptionLineNbr -> PX.Objects.AM.AMConfigurationOption (ConfigurationID=ConfigurationID, Revision=Revision, FeatureLineNbr=ConfigFeatureLineNbr, OptionLineNbr=LineNbr)
PX.Objects.AM.AMConfigResultsOption.AMConfigurationResultsByConfigResultsID -> PX.Objects.AM.AMConfigurationResults (ConfigResultsID=ConfigResultsID)

# PX.Objects.AM.AMConfigResultsRule (EntityType)

Label: "Configuration Rule Result"
Key: ConfigResultsID, RuleLineNbr, RuleSource, RuleSourceLineNbr, RuleTarget, TargetLineNbr, TargetSubLineNbr
Entity sets: PX_Objects_AM_AMConfigResultsRule, ConfigurationRuleResult, AMConfigResultsRule

PX.Objects.AM.AMConfigResultsRule.ConfigResultsID : Edm.Int32 [key] "Config Results ID"
PX.Objects.AM.AMConfigResultsRule.ConfigurationID : Edm.String "Configuration ID"
PX.Objects.AM.AMConfigResultsRule.Revision : Edm.String "Revision"
PX.Objects.AM.AMConfigResultsRule.RuleTarget : Edm.String [key] "Rule Target"
PX.Objects.AM.AMConfigResultsRule.TargetLineNbr : Edm.Int32 [key] "Target Line Nbr."
PX.Objects.AM.AMConfigResultsRule.TargetSubLineNbr : Edm.Int32 [key] "Target Sub-Line Nbr."
PX.Objects.AM.AMConfigResultsRule.RuleSource : Edm.String [key] "Rule Source"
PX.Objects.AM.AMConfigResultsRule.RuleSourceLineNbr : Edm.Int32 [key] "Rule Source Line Nbr."
PX.Objects.AM.AMConfigResultsRule.RuleLineNbr : Edm.Int32 [key] "Rule Line Nbr."
PX.Objects.AM.AMConfigResultsRule.RuleType : Edm.String "Rule Type"
PX.Objects.AM.AMConfigResultsRule.IsSoftRule : Edm.Boolean
PX.Objects.AM.AMConfigResultsRule.RuleValid : Edm.Boolean [required]
PX.Objects.AM.AMConfigResultsRule.Condition : Edm.String "Condition"
PX.Objects.AM.AMConfigResultsRule.CalcValue : Edm.String "Value"
PX.Objects.AM.AMConfigResultsRule.CalcValue1 : Edm.String "Value 1"
PX.Objects.AM.AMConfigResultsRule.CalcValue2 : Edm.String "Value 2"
PX.Objects.AM.AMConfigResultsRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigResultsRule.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigResultsRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigResultsRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigResultsRule.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigResultsRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigResultsRule.tstamp : Edm.Binary
PX.Objects.AM.AMConfigResultsRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigResultsRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigResultsRule.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigResultsRule.AMConfigurationResultsByConfigResultsID -> PX.Objects.AM.AMConfigurationResults (ConfigResultsID=ConfigResultsID)

# PX.Objects.AM.AMConfiguration (EntityType)

Label: "Configuration"
Key: ConfigurationID, Revision
Entity sets: PX_Objects_AM_AMConfiguration, Configuration, AMConfiguration
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMConfiguration.ConfigurationID : Edm.String [key] "Configuration ID"
PX.Objects.AM.AMConfiguration.Revision : Edm.String [key] "Revision"
PX.Objects.AM.AMConfiguration.Status : Edm.String "Status"
PX.Objects.AM.AMConfiguration.Descr : Edm.String "Description"
PX.Objects.AM.AMConfiguration.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMConfiguration.BOMRevisionID : Edm.String "BOM Revision"
PX.Objects.AM.AMConfiguration.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMConfiguration.PriceRollup : Edm.String "Rollup"
PX.Objects.AM.AMConfiguration.PriceCalc : Edm.String "Calculate"
PX.Objects.AM.AMConfiguration.KeyFormat : Edm.String "Format"
PX.Objects.AM.AMConfiguration.KeyEquation : Edm.String "Formula"
PX.Objects.AM.AMConfiguration.KeyNumberingID : Edm.String "Number Sequence"
PX.Objects.AM.AMConfiguration.KeyDescription : Edm.String "Key Description"
PX.Objects.AM.AMConfiguration.TranDescription : Edm.String "Tran Description"
PX.Objects.AM.AMConfiguration.LineCntrFeature : Edm.Int32 [required]
PX.Objects.AM.AMConfiguration.LineCntrAttribute : Edm.Int32 [required]
PX.Objects.AM.AMConfiguration.IsCompletionRequired : Edm.Boolean "Completion Required Before Production"
PX.Objects.AM.AMConfiguration.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfiguration.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfiguration.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfiguration.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfiguration.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfiguration.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfiguration.NoteID : Edm.Guid
PX.Objects.AM.AMConfiguration.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMConfiguration.tstamp : Edm.Binary
PX.Objects.AM.AMConfiguration.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMConfiguration.AMBomItemByBOMRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, BOMRevisionID=RevisionID)
PX.Objects.AM.AMConfiguration.AMBomItemByBOMID -> PX.Objects.AM.AMBomItem (BOMID=BOMID)
PX.Objects.AM.AMConfiguration.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfiguration.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfiguration.NumberingByKeyNumberingID -> PX.Objects.CS.Numbering (KeyNumberingID=NumberingID)
PX.Objects.AM.AMConfiguration.AMConfigResultsAttributeCollection -> Collection(PX.Objects.AM.AMConfigResultsAttribute)
PX.Objects.AM.AMConfiguration.AMConfigResultsFeatureCollection -> Collection(PX.Objects.AM.AMConfigResultsFeature)
PX.Objects.AM.AMConfiguration.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.AM.AMConfiguration.AMConfigResultsRuleCollection -> Collection(PX.Objects.AM.AMConfigResultsRule)
PX.Objects.AM.AMConfiguration.AMConfigurationAttributeCollection -> Collection(PX.Objects.AM.AMConfigurationAttribute)
PX.Objects.AM.AMConfiguration.AMConfigurationFeatureCollection -> Collection(PX.Objects.AM.AMConfigurationFeature)
PX.Objects.AM.AMConfiguration.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.AM.AMConfiguration.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.AM.AMConfiguration.AMConfigurationRuleCollection -> Collection(PX.Objects.AM.AMConfigurationRule)
PX.Objects.AM.AMConfiguration.AMConfigurationKeysCollection -> Collection(PX.Objects.AM.AMConfigurationKeys)

# PX.Objects.AM.AMConfigurationAttribute (EntityType)

Label: "Configuration Attribute"
Key: ConfigurationID, LineNbr, Revision
Entity sets: PX_Objects_AM_AMConfigurationAttribute, ConfigurationAttribute, AMConfigurationAttribute
Non-filterable, non-selectable: IsFormula

PX.Objects.AM.AMConfigurationAttribute.ConfigurationID : Edm.String [key] "Configuration ID"
PX.Objects.AM.AMConfigurationAttribute.Revision : Edm.String [key] "Revision"
PX.Objects.AM.AMConfigurationAttribute.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.AM.AMConfigurationAttribute.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.AM.AMConfigurationAttribute.AttributeID : Edm.String "Attribute ID"
PX.Objects.AM.AMConfigurationAttribute.Label : Edm.String "Label"
PX.Objects.AM.AMConfigurationAttribute.Variable : Edm.String "Variable"
PX.Objects.AM.AMConfigurationAttribute.Descr : Edm.String "Description"
PX.Objects.AM.AMConfigurationAttribute.IsFormula : Edm.Boolean "Is Formula"
PX.Objects.AM.AMConfigurationAttribute.Enabled : Edm.Boolean [required] "Enabled"
PX.Objects.AM.AMConfigurationAttribute.Required : Edm.Boolean [required] "Required"
PX.Objects.AM.AMConfigurationAttribute.Visible : Edm.Boolean [required] "Visible"
PX.Objects.AM.AMConfigurationAttribute.Value : Edm.String "Default Value"
PX.Objects.AM.AMConfigurationAttribute.LineCntrRule : Edm.Int32 [required]
PX.Objects.AM.AMConfigurationAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationAttribute.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigurationAttribute.tstamp : Edm.Binary
PX.Objects.AM.AMConfigurationAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigurationAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigurationAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.AM.AMConfigurationAttribute.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationAttribute.AMConfigResultsAttributeCollection -> Collection(PX.Objects.AM.AMConfigResultsAttribute)
PX.Objects.AM.AMConfigurationAttribute.AMConfigurationAttributeRuleCollection -> Collection(PX.Objects.AM.AMConfigurationAttributeRule)

# PX.Objects.AM.AMConfigurationAttributeRule (EntityType)

Label: "Configuration Attribute Rule"
Key: ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr
Entity sets: PX_Objects_AM_AMConfigurationAttributeRule, ConfigurationAttributeRule, AMConfigurationAttributeRule

PX.Objects.AM.AMConfigurationAttributeRule.ConfigurationID : Edm.String [key] "ConfigurationID"
PX.Objects.AM.AMConfigurationAttributeRule.Revision : Edm.String [key] "Revision"
PX.Objects.AM.AMConfigurationAttributeRule.RuleSource : Edm.String [key] "Rule Source"
PX.Objects.AM.AMConfigurationAttributeRule.SourceLineNbr : Edm.Int32 [key] "SourceLineNbr"
PX.Objects.AM.AMConfigurationAttributeRule.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.AM.AMConfigurationAttributeRule.RuleType : Edm.String "Rule"
PX.Objects.AM.AMConfigurationAttributeRule.Condition : Edm.String "Condition"
PX.Objects.AM.AMConfigurationAttributeRule.IsExpression : Edm.Boolean "From Schema"
PX.Objects.AM.AMConfigurationAttributeRule.Value1 : Edm.String "Value 1"
PX.Objects.AM.AMConfigurationAttributeRule.Value2 : Edm.String "Value 2"
PX.Objects.AM.AMConfigurationAttributeRule.TargetFeatureLineNbr : Edm.Int32 "Target Feature"
PX.Objects.AM.AMConfigurationAttributeRule.TargetOptionLineNbr : Edm.Int32 "Target Option"
PX.Objects.AM.AMConfigurationAttributeRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationAttributeRule.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationAttributeRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationAttributeRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationAttributeRule.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationAttributeRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigurationAttributeRule.tstamp : Edm.Binary
PX.Objects.AM.AMConfigurationAttributeRule.AMConfigurationAttributeBySourceLineNbr -> PX.Objects.AM.AMConfigurationAttribute (ConfigurationID=ConfigurationID, Revision=Revision, SourceLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationAttributeRule.AMConfigurationFeatureByRevision -> PX.Objects.AM.AMConfigurationFeature (TargetFeatureLineNbr=LineNbr, ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationAttributeRule.AMConfigurationOptionByTargetFeatureLineNbr -> PX.Objects.AM.AMConfigurationOption (TargetOptionLineNbr=LineNbr, ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=ConfigFeatureLineNbr)
PX.Objects.AM.AMConfigurationAttributeRule.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationAttributeRule.AMConfigurationFeatureByTargetFeatureLineNbr -> PX.Objects.AM.AMConfigurationFeature (ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationAttributeRule.AMConfigurationOptionByTargetOptionLineNbr -> PX.Objects.AM.AMConfigurationOption (ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=ConfigFeatureLineNbr, TargetOptionLineNbr=LineNbr)

# PX.Objects.AM.AMConfigurationFeature (EntityType)

Label: "Configuration Feature"
Key: ConfigurationID, LineNbr, Revision
Entity sets: PX_Objects_AM_AMConfigurationFeature, ConfigurationFeature, AMConfigurationFeature

PX.Objects.AM.AMConfigurationFeature.ConfigurationID : Edm.String [key] "Configuration ID"
PX.Objects.AM.AMConfigurationFeature.Revision : Edm.String [key] "Revision"
PX.Objects.AM.AMConfigurationFeature.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.AM.AMConfigurationFeature.FeatureID : Edm.String "Feature ID"
PX.Objects.AM.AMConfigurationFeature.Label : Edm.String "Label"
PX.Objects.AM.AMConfigurationFeature.Descr : Edm.String "Description"
PX.Objects.AM.AMConfigurationFeature.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.AM.AMConfigurationFeature.MinSelection : Edm.String "Min Selection"
PX.Objects.AM.AMConfigurationFeature.MaxSelection : Edm.String "Max Selection"
PX.Objects.AM.AMConfigurationFeature.MinQty : Edm.String "Min. Qty."
PX.Objects.AM.AMConfigurationFeature.MaxQty : Edm.String "Max. Qty."
PX.Objects.AM.AMConfigurationFeature.LotQty : Edm.String "Lot Qty."
PX.Objects.AM.AMConfigurationFeature.Visible : Edm.Boolean [required] "Visible"
PX.Objects.AM.AMConfigurationFeature.ResultsCopy : Edm.Boolean [required] "Results Copy"
PX.Objects.AM.AMConfigurationFeature.LineCntrOption : Edm.Int32 [required]
PX.Objects.AM.AMConfigurationFeature.LineCntrRule : Edm.Int32 [required]
PX.Objects.AM.AMConfigurationFeature.PrintResults : Edm.Boolean [required] "Print Results"
PX.Objects.AM.AMConfigurationFeature.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationFeature.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationFeature.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationFeature.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationFeature.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationFeature.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigurationFeature.tstamp : Edm.Binary
PX.Objects.AM.AMConfigurationFeature.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigurationFeature.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigurationFeature.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationFeature.AMFeatureByFeatureID -> PX.Objects.AM.AMFeature (FeatureID=FeatureID)
PX.Objects.AM.AMConfigurationFeature.AMConfigResultsFeatureCollection -> Collection(PX.Objects.AM.AMConfigResultsFeature)
PX.Objects.AM.AMConfigurationFeature.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.AM.AMConfigurationFeature.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.AM.AMConfigurationFeature.AMConfigurationRuleCollection -> Collection(PX.Objects.AM.AMConfigurationRule)
PX.Objects.AM.AMConfigurationFeature.AMConfigurationAttributeRuleCollection -> Collection(PX.Objects.AM.AMConfigurationAttributeRule)
PX.Objects.AM.AMConfigurationFeature.AMConfigurationFeatureRuleCollection -> Collection(PX.Objects.AM.AMConfigurationFeatureRule)

# PX.Objects.AM.AMConfigurationFeatureRule (EntityType)

Label: "Configuration Feature Rule"
Key: ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr
Entity sets: PX_Objects_AM_AMConfigurationFeatureRule, ConfigurationFeatureRule, AMConfigurationFeatureRule
Non-filterable, non-selectable: SourceOptionLineNbr

PX.Objects.AM.AMConfigurationFeatureRule.ConfigurationID : Edm.String [key] "ConfigurationID"
PX.Objects.AM.AMConfigurationFeatureRule.Revision : Edm.String [key] "Revision"
PX.Objects.AM.AMConfigurationFeatureRule.RuleSource : Edm.String [key] "Rule Source"
PX.Objects.AM.AMConfigurationFeatureRule.SourceLineNbr : Edm.Int32 [key] "SourceLineNbr"
PX.Objects.AM.AMConfigurationFeatureRule.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.AM.AMConfigurationFeatureRule.RuleType : Edm.String "Rule"
PX.Objects.AM.AMConfigurationFeatureRule.Condition : Edm.String "Condition"
PX.Objects.AM.AMConfigurationFeatureRule.IsExpression : Edm.Boolean "From Schema"
PX.Objects.AM.AMConfigurationFeatureRule.SourceOptionLineNbr : Edm.Int32 "Source Option"
PX.Objects.AM.AMConfigurationFeatureRule.Value1 : Edm.String "Value1"
PX.Objects.AM.AMConfigurationFeatureRule.Value2 : Edm.String "Value2"
PX.Objects.AM.AMConfigurationFeatureRule.TargetFeatureLineNbr : Edm.Int32 "Target Feature"
PX.Objects.AM.AMConfigurationFeatureRule.TargetOptionLineNbr : Edm.Int32 "Target Option"
PX.Objects.AM.AMConfigurationFeatureRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationFeatureRule.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationFeatureRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationFeatureRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationFeatureRule.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationFeatureRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigurationFeatureRule.tstamp : Edm.Binary
PX.Objects.AM.AMConfigurationFeatureRule.AMConfigurationFeatureBySourceLineNbr -> PX.Objects.AM.AMConfigurationFeature (ConfigurationID=ConfigurationID, Revision=Revision, SourceLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationFeatureRule.AMConfigurationFeatureByRevision -> PX.Objects.AM.AMConfigurationFeature (TargetFeatureLineNbr=LineNbr, ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationFeatureRule.AMConfigurationOptionByTargetFeatureLineNbr -> PX.Objects.AM.AMConfigurationOption (TargetOptionLineNbr=LineNbr, ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=ConfigFeatureLineNbr)
PX.Objects.AM.AMConfigurationFeatureRule.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationFeatureRule.AMConfigurationFeatureByTargetFeatureLineNbr -> PX.Objects.AM.AMConfigurationFeature (ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationFeatureRule.AMConfigurationOptionByTargetOptionLineNbr -> PX.Objects.AM.AMConfigurationOption (ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=ConfigFeatureLineNbr, TargetOptionLineNbr=LineNbr)

# PX.Objects.AM.AMConfigurationKeys (EntityType)

Label: "Configuration Keys"
Key: ConfigResultsID
Entity sets: PX_Objects_AM_AMConfigurationKeys, ConfigurationKeys, AMConfigurationKeys
Non-filterable, non-selectable: SupplementalPriceTotal, CuryRate, CuryViewState

PX.Objects.AM.AMConfigurationKeys.ConfigResultsID : Edm.Int32 [key] "Config Results ID"
PX.Objects.AM.AMConfigurationKeys.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMConfigurationKeys.ConfigurationID : Edm.String "Configuration ID"
PX.Objects.AM.AMConfigurationKeys.Revision : Edm.String "Conf. Revision"
PX.Objects.AM.AMConfigurationKeys.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AM.AMConfigurationKeys.CustomerID : Edm.Int32 "Customer"
PX.Objects.AM.AMConfigurationKeys.UOM : Edm.String "UOM"
PX.Objects.AM.AMConfigurationKeys.Qty : Edm.Decimal "Qty"
PX.Objects.AM.AMConfigurationKeys.CuryID : Edm.String "Currency"
PX.Objects.AM.AMConfigurationKeys.CuryInfoID : Edm.Int64
PX.Objects.AM.AMConfigurationKeys.CuryOptionPriceTotal : Edm.Decimal "Option price Total"
PX.Objects.AM.AMConfigurationKeys.OptionPriceTotal : Edm.Decimal
PX.Objects.AM.AMConfigurationKeys.CurySupplementalPriceTotal : Edm.Decimal "Option price Total"
PX.Objects.AM.AMConfigurationKeys.SupplementalPriceTotal : Edm.Decimal
PX.Objects.AM.AMConfigurationKeys.CuryBOMPriceTotal : Edm.Decimal "BOM Price Total"
PX.Objects.AM.AMConfigurationKeys.BOMPriceTotal : Edm.Decimal
PX.Objects.AM.AMConfigurationKeys.CuryFixedPriceTotal : Edm.Decimal "Fixed Price Total"
PX.Objects.AM.AMConfigurationKeys.FixedPriceTotal : Edm.Decimal
PX.Objects.AM.AMConfigurationKeys.Completed : Edm.Boolean "Completed"
PX.Objects.AM.AMConfigurationKeys.Closed : Edm.Boolean "Closed"
PX.Objects.AM.AMConfigurationKeys.ProdOrderType : Edm.String "Prod Order Type"
PX.Objects.AM.AMConfigurationKeys.ProdOrderNbr : Edm.String "Prod Order Nbr"
PX.Objects.AM.AMConfigurationKeys.OrdLineRef : Edm.Int32 "SO Line Nbr."
PX.Objects.AM.AMConfigurationKeys.OrdTypeRef : Edm.String "SO Order Type"
PX.Objects.AM.AMConfigurationKeys.OrdNbrRef : Edm.String "SO Order Nbr"
PX.Objects.AM.AMConfigurationKeys.OpportunityQuoteID : Edm.Guid "Opportunity Quote ID"
PX.Objects.AM.AMConfigurationKeys.OpportunityLineNbr : Edm.Int32 "Opportunity Line Nbr"
PX.Objects.AM.AMConfigurationKeys.CreatedDateTime : Edm.DateTimeOffset "Config. Date"
PX.Objects.AM.AMConfigurationKeys.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationKeys.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationKeys.KeyID : Edm.String "Config. Key"
PX.Objects.AM.AMConfigurationKeys.KeyDescription : Edm.String "Key Description"
PX.Objects.AM.AMConfigurationKeys.TranDescription : Edm.String "Tran Description"
PX.Objects.AM.AMConfigurationKeys.CuryRate : Edm.Decimal
PX.Objects.AM.AMConfigurationKeys.CuryViewState : Edm.Boolean
PX.Objects.AM.AMConfigurationKeys.SOOrderByOrdNbrRef -> PX.Objects.SO.SOOrder (OrdNbrRef=OrderNbr)
PX.Objects.AM.AMConfigurationKeys.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AM.AMConfigurationKeys.AMConfigurationByConfigurationID -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID)
PX.Objects.AM.AMConfigurationKeys.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (Revision=Revision)
PX.Objects.AM.AMConfigurationKeys.CROpportunityProductsByOpportunityLineNbr -> PX.Objects.CR.CROpportunityProducts (OpportunityQuoteID=QuoteID, OpportunityLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationKeys.SOLineByOrdLineRef -> PX.Objects.SO.SOLine (OrdTypeRef=OrderType, OrdNbrRef=OrderNbr, OrdLineRef=LineNbr)
PX.Objects.AM.AMConfigurationKeys.AMConfigurationByInventoryID -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, InventoryID=InventoryID)
PX.Objects.AM.AMConfigurationKeys.AMProdItemByProdOrderNbr -> PX.Objects.AM.AMProdItem (ProdOrderType=OrderType, ProdOrderNbr=ProdOrdID)
PX.Objects.AM.AMConfigurationKeys.CROpportunityByOpportunityQuoteID -> PX.Objects.CR.CROpportunity (OpportunityQuoteID=QuoteNoteID)
PX.Objects.AM.AMConfigurationKeys.AMConfigurationKeysByConfigurationID -> PX.Objects.AM.AMConfigurationKeys (KeyID=KeyID, ConfigurationID=ConfigurationID)
PX.Objects.AM.AMConfigurationKeys.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.AM.AMConfigurationKeys.AMConfigResultsAttributeCollection -> Collection(PX.Objects.AM.AMConfigResultsAttribute)
PX.Objects.AM.AMConfigurationKeys.AMConfigResultsFeatureCollection -> Collection(PX.Objects.AM.AMConfigResultsFeature)
PX.Objects.AM.AMConfigurationKeys.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.AM.AMConfigurationKeys.AMConfigResultsRuleCollection -> Collection(PX.Objects.AM.AMConfigResultsRule)

# PX.Objects.AM.AMConfigurationOption (EntityType)

Label: "Configuration Option"
Key: ConfigFeatureLineNbr, ConfigurationID, LineNbr, Revision
Entity sets: PX_Objects_AM_AMConfigurationOption, ConfigurationOption, AMConfigurationOption

PX.Objects.AM.AMConfigurationOption.ConfigurationID : Edm.String [key] "Configuration ID"
PX.Objects.AM.AMConfigurationOption.Revision : Edm.String [key] "Revision"
PX.Objects.AM.AMConfigurationOption.ConfigFeatureLineNbr : Edm.Int32 [key] "Feature Line Nbr"
PX.Objects.AM.AMConfigurationOption.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.AM.AMConfigurationOption.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.AM.AMConfigurationOption.Label : Edm.String "Label"
PX.Objects.AM.AMConfigurationOption.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMConfigurationOption.Descr : Edm.String "Description"
PX.Objects.AM.AMConfigurationOption.FixedInclude : Edm.Boolean [required] "Fixed Include"
PX.Objects.AM.AMConfigurationOption.QtyEnabled : Edm.Boolean [required] "Enabled Qty."
PX.Objects.AM.AMConfigurationOption.QtyRequired : Edm.String "Required Qty."
PX.Objects.AM.AMConfigurationOption.UOM : Edm.String "UOM"
PX.Objects.AM.AMConfigurationOption.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMConfigurationOption.MinQty : Edm.String "Min. Qty."
PX.Objects.AM.AMConfigurationOption.MaxQty : Edm.String "Max. Qty."
PX.Objects.AM.AMConfigurationOption.LotQty : Edm.String "Lot Qty."
PX.Objects.AM.AMConfigurationOption.ScrapFactor : Edm.String "Scrap Factor"
PX.Objects.AM.AMConfigurationOption.MaterialType : Edm.Int32 "Material Type"
PX.Objects.AM.AMConfigurationOption.PhantomRouting : Edm.Int32 [required] "Phantom Routing"
PX.Objects.AM.AMConfigurationOption.PriceFactor : Edm.String "Price Factor"
PX.Objects.AM.AMConfigurationOption.ResultsCopy : Edm.Boolean [required] "Results Copy"
PX.Objects.AM.AMConfigurationOption.BFlush : Edm.Boolean [required] "Backflush"
PX.Objects.AM.AMConfigurationOption.QtyRoundUp : Edm.Boolean [required] "Round Qty. Up"
PX.Objects.AM.AMConfigurationOption.BatchSize : Edm.Decimal [required] "Batch Size"
PX.Objects.AM.AMConfigurationOption.SubcontractSource : Edm.Int32 [required] "Subcontract Source"
PX.Objects.AM.AMConfigurationOption.PrintResults : Edm.Boolean [required] "Print Results"
PX.Objects.AM.AMConfigurationOption.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationOption.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationOption.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationOption.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationOption.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationOption.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigurationOption.tstamp : Edm.Binary
PX.Objects.AM.AMConfigurationOption.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMConfigurationOption.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigurationOption.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigurationOption.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMConfigurationOption.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMConfigurationOption.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMConfigurationOption.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMConfigurationOption.AMBomOperByOperationID -> PX.Objects.AM.AMBomOper (OperationID=OperationID)
PX.Objects.AM.AMConfigurationOption.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationOption.AMConfigurationFeatureByConfigFeatureLineNbr -> PX.Objects.AM.AMConfigurationFeature (ConfigurationID=ConfigurationID, Revision=Revision, ConfigFeatureLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationOption.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.AM.AMConfigurationOption.AMConfigurationOptionCurySettingsCollection -> Collection(PX.Objects.AM.AMConfigurationOptionCurySettings)
PX.Objects.AM.AMConfigurationOption.AMConfigurationRuleCollection -> Collection(PX.Objects.AM.AMConfigurationRule)
PX.Objects.AM.AMConfigurationOption.AMConfigurationAttributeRuleCollection -> Collection(PX.Objects.AM.AMConfigurationAttributeRule)
PX.Objects.AM.AMConfigurationOption.AMConfigurationFeatureRuleCollection -> Collection(PX.Objects.AM.AMConfigurationFeatureRule)

# PX.Objects.AM.AMConfigurationOptionCurySettings (EntityType)

Label: "Config Option Currency Settings"
Key: ConfigFeatureLineNbr, ConfigurationID, CuryID, LineNbr, Revision
Entity sets: PX_Objects_AM_AMConfigurationOptionCurySettings, ConfigOptionCurrencySettings, AMConfigurationOptionCurySettings

PX.Objects.AM.AMConfigurationOptionCurySettings.ConfigurationID : Edm.String [key] "Configuration ID"
PX.Objects.AM.AMConfigurationOptionCurySettings.Revision : Edm.String [key] "Revision"
PX.Objects.AM.AMConfigurationOptionCurySettings.ConfigFeatureLineNbr : Edm.Int32 [key] "Feature Line Nbr"
PX.Objects.AM.AMConfigurationOptionCurySettings.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.AM.AMConfigurationOptionCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMConfigurationOptionCurySettings.LocationID : Edm.Int32 "Location ID"
PX.Objects.AM.AMConfigurationOptionCurySettings.tstamp : Edm.Binary
PX.Objects.AM.AMConfigurationOptionCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationOptionCurySettings.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationOptionCurySettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationOptionCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigurationOptionCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationOptionCurySettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationOptionCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigurationOptionCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigurationOptionCurySettings.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMConfigurationOptionCurySettings.AMConfigurationOptionByLineNbr -> PX.Objects.AM.AMConfigurationOption (ConfigurationID=ConfigurationID, Revision=Revision, ConfigFeatureLineNbr=ConfigFeatureLineNbr, LineNbr=LineNbr)

# PX.Objects.AM.AMConfigurationResults (EntityType)

Label: "Configuration Result"
Key: ConfigResultsID
Entity sets: PX_Objects_AM_AMConfigurationResults, ConfigurationResult, AMConfigurationResults
Non-filterable, non-selectable: IsConfigurationTesting, SupplementalPriceTotal, DisplayPrice, UserOptionsError, IsSalesReferenced, IsOpportunityReferenced, IsProductionReferenced, CuryRate, CuryViewState

PX.Objects.AM.AMConfigurationResults.ConfigResultsID : Edm.Int32 [key] "Config Results ID"
PX.Objects.AM.AMConfigurationResults.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMConfigurationResults.ConfigurationID : Edm.String "Configuration ID"
PX.Objects.AM.AMConfigurationResults.IsConfigurationTesting : Edm.Boolean "Test Configuration"
PX.Objects.AM.AMConfigurationResults.Revision : Edm.String "Conf. Revision"
PX.Objects.AM.AMConfigurationResults.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AM.AMConfigurationResults.CustomerID : Edm.Int32 "Customer"
PX.Objects.AM.AMConfigurationResults.UOM : Edm.String "UOM"
PX.Objects.AM.AMConfigurationResults.Qty : Edm.Decimal "Qty"
PX.Objects.AM.AMConfigurationResults.CuryID : Edm.String "Currency"
PX.Objects.AM.AMConfigurationResults.CuryInfoID : Edm.Int64
PX.Objects.AM.AMConfigurationResults.CuryOptionPriceTotal : Edm.Decimal [required] "Option price Total"
PX.Objects.AM.AMConfigurationResults.OptionPriceTotal : Edm.Decimal [required]
PX.Objects.AM.AMConfigurationResults.CurySupplementalPriceTotal : Edm.Decimal [required] "Option price Total"
PX.Objects.AM.AMConfigurationResults.SupplementalPriceTotal : Edm.Decimal [required]
PX.Objects.AM.AMConfigurationResults.CuryBOMPriceTotal : Edm.Decimal [required] "BOM Price Total"
PX.Objects.AM.AMConfigurationResults.BOMPriceTotal : Edm.Decimal [required]
PX.Objects.AM.AMConfigurationResults.CuryFixedPriceTotal : Edm.Decimal [required] "Parent Price"
PX.Objects.AM.AMConfigurationResults.FixedPriceTotal : Edm.Decimal [required]
PX.Objects.AM.AMConfigurationResults.DisplayPrice : Edm.Decimal "Price"
PX.Objects.AM.AMConfigurationResults.Completed : Edm.Boolean [required] "Completed"
PX.Objects.AM.AMConfigurationResults.Closed : Edm.Boolean [required] "Closed"
PX.Objects.AM.AMConfigurationResults.ProdOrderType : Edm.String "Prod Order Type"
PX.Objects.AM.AMConfigurationResults.ProdOrderNbr : Edm.String "Prod Order Nbr"
PX.Objects.AM.AMConfigurationResults.OrdLineRef : Edm.Int32 "SO Line Nbr."
PX.Objects.AM.AMConfigurationResults.OrdTypeRef : Edm.String "SO Order Type"
PX.Objects.AM.AMConfigurationResults.OrdNbrRef : Edm.String "SO Order Nbr"
PX.Objects.AM.AMConfigurationResults.OpportunityQuoteID : Edm.Guid "Opportunity Quote ID"
PX.Objects.AM.AMConfigurationResults.OpportunityLineNbr : Edm.Int32 "Opportunity Line Nbr"
PX.Objects.AM.AMConfigurationResults.CreatedDateTime : Edm.DateTimeOffset "Config. Date"
PX.Objects.AM.AMConfigurationResults.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationResults.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationResults.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationResults.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationResults.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigurationResults.tstamp : Edm.Binary
PX.Objects.AM.AMConfigurationResults.KeyID : Edm.String "Config. Key"
PX.Objects.AM.AMConfigurationResults.KeyDescription : Edm.String "Key Description"
PX.Objects.AM.AMConfigurationResults.TranDescription : Edm.String "Tran Description"
PX.Objects.AM.AMConfigurationResults.UserOptionsError : Edm.String "Options Tab Error"
PX.Objects.AM.AMConfigurationResults.IsSalesReferenced : Edm.Boolean
PX.Objects.AM.AMConfigurationResults.IsOpportunityReferenced : Edm.Boolean
PX.Objects.AM.AMConfigurationResults.IsProductionReferenced : Edm.Boolean
PX.Objects.AM.AMConfigurationResults.CuryRate : Edm.Decimal
PX.Objects.AM.AMConfigurationResults.CuryViewState : Edm.Boolean
PX.Objects.AM.AMConfigurationResults.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AM.AMConfigurationResults.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AM.AMConfigurationResults.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMConfigurationResults.SOOrderByOrdNbrRef -> PX.Objects.SO.SOOrder (OrdTypeRef=OrderType, OrdNbrRef=OrderNbr)
PX.Objects.AM.AMConfigurationResults.CROpportunityProductsByOpportunityLineNbr -> PX.Objects.CR.CROpportunityProducts (OpportunityQuoteID=QuoteID, OpportunityLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationResults.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigurationResults.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigurationResults.SOLineByOrdLineRef -> PX.Objects.SO.SOLine (OrdTypeRef=OrderType, OrdNbrRef=OrderNbr, OrdLineRef=LineNbr)
PX.Objects.AM.AMConfigurationResults.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMConfigurationResults.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AM.AMConfigurationResults.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.AM.AMConfigurationResults.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationResults.AMConfigurationByInventoryID -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, InventoryID=InventoryID)
PX.Objects.AM.AMConfigurationResults.AMConfigurationByConfigurationID -> PX.Objects.AM.AMConfiguration (Revision=Revision, ConfigurationID=ConfigurationID)
PX.Objects.AM.AMConfigurationResults.AMProdItemByProdOrderNbr -> PX.Objects.AM.AMProdItem (ProdOrderType=OrderType, ProdOrderNbr=ProdOrdID)
PX.Objects.AM.AMConfigurationResults.CROpportunityByOpportunityQuoteID -> PX.Objects.CR.CROpportunity (OpportunityQuoteID=QuoteNoteID)
PX.Objects.AM.AMConfigurationResults.AMConfigurationKeysByConfigurationID -> PX.Objects.AM.AMConfigurationKeys (KeyID=KeyID, ConfigurationID=ConfigurationID)
PX.Objects.AM.AMConfigurationResults.AMConfigResultsAttributeCollection -> Collection(PX.Objects.AM.AMConfigResultsAttribute)
PX.Objects.AM.AMConfigurationResults.AMConfigResultsFeatureCollection -> Collection(PX.Objects.AM.AMConfigResultsFeature)
PX.Objects.AM.AMConfigurationResults.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.AM.AMConfigurationResults.AMConfigResultsRuleCollection -> Collection(PX.Objects.AM.AMConfigResultsRule)

# PX.Objects.AM.AMConfigurationRule (EntityType)

Label: "Configuration Rule"
Key: ConfigurationID, LineNbr, Revision, RuleSource, SourceLineNbr
Entity sets: PX_Objects_AM_AMConfigurationRule, ConfigurationRule, AMConfigurationRule

PX.Objects.AM.AMConfigurationRule.ConfigurationID : Edm.String [key] "Configuration ID"
PX.Objects.AM.AMConfigurationRule.Revision : Edm.String [key] "Revision"
PX.Objects.AM.AMConfigurationRule.RuleSource : Edm.String [key] "Rule Source"
PX.Objects.AM.AMConfigurationRule.SourceLineNbr : Edm.Int32 [key] "Source Line Nbr"
PX.Objects.AM.AMConfigurationRule.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.AM.AMConfigurationRule.RuleType : Edm.String "Rule"
PX.Objects.AM.AMConfigurationRule.Condition : Edm.String "Condition"
PX.Objects.AM.AMConfigurationRule.IsExpression : Edm.Boolean "From Schema"
PX.Objects.AM.AMConfigurationRule.Value1 : Edm.String "Value 1"
PX.Objects.AM.AMConfigurationRule.Value2 : Edm.String "Value 2"
PX.Objects.AM.AMConfigurationRule.TargetFeatureLineNbr : Edm.Int32 "Target Feature"
PX.Objects.AM.AMConfigurationRule.TargetOptionLineNbr : Edm.Int32 "Target Option"
PX.Objects.AM.AMConfigurationRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationRule.CreatedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMConfigurationRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMConfigurationRule.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMConfigurationRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMConfigurationRule.tstamp : Edm.Binary
PX.Objects.AM.AMConfigurationRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMConfigurationRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMConfigurationRule.AMConfigurationByRevision -> PX.Objects.AM.AMConfiguration (ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationRule.AMConfigurationFeatureByTargetFeatureLineNbr -> PX.Objects.AM.AMConfigurationFeature (ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationRule.AMConfigurationFeatureByRevision -> PX.Objects.AM.AMConfigurationFeature (TargetFeatureLineNbr=LineNbr, ConfigurationID=ConfigurationID, Revision=Revision)
PX.Objects.AM.AMConfigurationRule.AMConfigurationOptionByTargetOptionLineNbr -> PX.Objects.AM.AMConfigurationOption (ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=ConfigFeatureLineNbr, TargetOptionLineNbr=LineNbr)
PX.Objects.AM.AMConfigurationRule.AMConfigurationOptionByTargetFeatureLineNbr -> PX.Objects.AM.AMConfigurationOption (TargetOptionLineNbr=LineNbr, ConfigurationID=ConfigurationID, Revision=Revision, TargetFeatureLineNbr=ConfigFeatureLineNbr)

# PX.Objects.AM.AMConfiguratorSetup (EntityType)

Label: "Configurator Preferences"
Singletons: PX_Objects_AM_AMConfiguratorSetup, ConfiguratorPreferences, AMConfiguratorSetup

PX.Objects.AM.AMConfiguratorSetup.ConfigNumberingID : Edm.String "Config Numbering Sequence"
PX.Objects.AM.AMConfiguratorSetup.DefaultsNumberingID : Edm.String "Defaults Numbering Sequence"
PX.Objects.AM.AMConfiguratorSetup.DfltRevisionNbr : Edm.String "Default Revision"
PX.Objects.AM.AMConfiguratorSetup.ConfigKeyFormat : Edm.String "Config Key Format"
PX.Objects.AM.AMConfiguratorSetup.DefaultKeyNumberingID : Edm.String "Default Key Number Sequence"
PX.Objects.AM.AMConfiguratorSetup.HidePriceDetails : Edm.Boolean [required] "Hide Price Details"
PX.Objects.AM.AMConfiguratorSetup.Rollup : Edm.String "Rollup"
PX.Objects.AM.AMConfiguratorSetup.AllowRollupOverride : Edm.Boolean [required] "Override Default on Configuration"
PX.Objects.AM.AMConfiguratorSetup.Calculate : Edm.String "Calculate"
PX.Objects.AM.AMConfiguratorSetup.AllowCalculateOverride : Edm.Boolean [required] "Override Default on Configuration"
PX.Objects.AM.AMConfiguratorSetup.EnableDiscount : Edm.Boolean [required] "Enable Discount"
PX.Objects.AM.AMConfiguratorSetup.EnablePrice : Edm.Boolean [required] "Enable Price"
PX.Objects.AM.AMConfiguratorSetup.IsCompletionRequired : Edm.Boolean [required] "Completion Required Before Production"
PX.Objects.AM.AMConfiguratorSetup.tstamp : Edm.Binary
PX.Objects.AM.AMConfiguratorSetup.NumberingByConfigNumberingID -> PX.Objects.CS.Numbering (ConfigNumberingID=NumberingID)
PX.Objects.AM.AMConfiguratorSetup.NumberingByDefaultKeyNumberingID -> PX.Objects.CS.Numbering (DefaultKeyNumberingID=NumberingID)

# PX.Objects.AM.AMDepartment (EntityType)

Label: "AM Department"
Key: DepartmentID
Entity sets: PX_Objects_AM_AMDepartment, AMDepartment
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMDepartment.DepartmentID : Edm.String [key] "Manufacturing Department ID"
PX.Objects.AM.AMDepartment.Descr : Edm.String "Description"
PX.Objects.AM.AMDepartment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMDepartment.CreatedByScreenID : Edm.String
PX.Objects.AM.AMDepartment.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMDepartment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMDepartment.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMDepartment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMDepartment.NoteID : Edm.Guid
PX.Objects.AM.AMDepartment.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMDepartment.tstamp : Edm.Binary
PX.Objects.AM.AMDepartment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMDepartment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMDepartment.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMDepartment.AMWCCollection -> Collection(PX.Objects.AM.AMWC)

# PX.Objects.AM.AMDisassembleBatch (EntityType)

Label: "AM Disassemble"
Key: BatchNbr, DocType
Entity sets: PX_Objects_AM_AMDisassembleBatch, AMDisassemble, AMDisassembleBatch
Non-filterable, non-selectable: BatNbr, IsStockItem, EditableBatch

PX.Objects.AM.AMDisassembleBatch.DocType : Edm.String [key] "Document Type"
PX.Objects.AM.AMDisassembleBatch.BatchNbr : Edm.String [key] "Batch Nbr."
PX.Objects.AM.AMDisassembleBatch.BatNbr : Edm.String "Bat Nbr"
PX.Objects.AM.AMDisassembleBatch.Released : Edm.Boolean "Released"
PX.Objects.AM.AMDisassembleBatch.Hold : Edm.Boolean "Hold"
PX.Objects.AM.AMDisassembleBatch.LineCntr : Edm.Int32
PX.Objects.AM.AMDisassembleBatch.RefLineNbr : Edm.Int32 "Ref Line Nbr."
PX.Objects.AM.AMDisassembleBatch.Status : Edm.String "Status"
PX.Objects.AM.AMDisassembleBatch.Date : Edm.DateTimeOffset "Date"
PX.Objects.AM.AMDisassembleBatch.TranDesc : Edm.String "Description"
PX.Objects.AM.AMDisassembleBatch.FinPeriodID : Edm.String "Post Period"
PX.Objects.AM.AMDisassembleBatch.TranPeriodID : Edm.String
PX.Objects.AM.AMDisassembleBatch.ControlAmount : Edm.Decimal "Control Amount"
PX.Objects.AM.AMDisassembleBatch.ControlQty : Edm.Decimal "Control Qty."
PX.Objects.AM.AMDisassembleBatch.ControlCost : Edm.Decimal "Control Cost"
PX.Objects.AM.AMDisassembleBatch.TotalAmount : Edm.Decimal "Total Amount"
PX.Objects.AM.AMDisassembleBatch.TotalQty : Edm.Decimal "Total Qty."
PX.Objects.AM.AMDisassembleBatch.TotalCost : Edm.Decimal "Total Cost"
PX.Objects.AM.AMDisassembleBatch.NoteID : Edm.Guid
PX.Objects.AM.AMDisassembleBatch.OrigBatNbr : Edm.String "Orig Batch Nbr"
PX.Objects.AM.AMDisassembleBatch.OrigDocType : Edm.String "Orig Doc Type"
PX.Objects.AM.AMDisassembleBatch.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMDisassembleBatch.CreatedByScreenID : Edm.String
PX.Objects.AM.AMDisassembleBatch.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMDisassembleBatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMDisassembleBatch.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMDisassembleBatch.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMDisassembleBatch.tstamp : Edm.Binary
PX.Objects.AM.AMDisassembleBatch.TranBranchID : Edm.Int32
PX.Objects.AM.AMDisassembleBatch.TranDocType : Edm.String
PX.Objects.AM.AMDisassembleBatch.TranBatchNbr : Edm.String
PX.Objects.AM.AMDisassembleBatch.LineNbr : Edm.Int32
PX.Objects.AM.AMDisassembleBatch.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMDisassembleBatch.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMDisassembleBatch.TranDate : Edm.DateTimeOffset
PX.Objects.AM.AMDisassembleBatch.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMDisassembleBatch.TranAmt : Edm.Decimal "Ext. Cost"
PX.Objects.AM.AMDisassembleBatch.TranFinPeriodID : Edm.String
PX.Objects.AM.AMDisassembleBatch.TranTranPeriodID : Edm.String
PX.Objects.AM.AMDisassembleBatch.Closeflg : Edm.Boolean "Complete"
PX.Objects.AM.AMDisassembleBatch.TranNoteID : Edm.Guid
PX.Objects.AM.AMDisassembleBatch.TranReleased : Edm.Boolean "Tran. Released"
PX.Objects.AM.AMDisassembleBatch.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMDisassembleBatch.Description : Edm.String "Description"
PX.Objects.AM.AMDisassembleBatch.UOM : Edm.String "UOM"
PX.Objects.AM.AMDisassembleBatch.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMDisassembleBatch.Qty : Edm.Decimal "Quantity"
PX.Objects.AM.AMDisassembleBatch.BaseQty : Edm.Decimal
PX.Objects.AM.AMDisassembleBatch.InvtMult : Edm.Int16 "Batch Multiplier"
PX.Objects.AM.AMDisassembleBatch.UnassignedQty : Edm.Decimal
PX.Objects.AM.AMDisassembleBatch.MatlLineId : Edm.Int32 "Material Line ID"
PX.Objects.AM.AMDisassembleBatch.WIPAcctID : Edm.Int32 "WIP Account"
PX.Objects.AM.AMDisassembleBatch.WIPSubID : Edm.Int32 "WIP Subaccount"
PX.Objects.AM.AMDisassembleBatch.ExtCost : Edm.Decimal
PX.Objects.AM.AMDisassembleBatch.GLBatNbr : Edm.String "GL Batch Nbr"
PX.Objects.AM.AMDisassembleBatch.GLLineNbr : Edm.Int32 "GL Batch Line Nbr"
PX.Objects.AM.AMDisassembleBatch.INDocType : Edm.String "IN Doc Type"
PX.Objects.AM.AMDisassembleBatch.INBatNbr : Edm.String "IN Ref Nbr"
PX.Objects.AM.AMDisassembleBatch.INLineNbr : Edm.Int32 "IN Line Nbr"
PX.Objects.AM.AMDisassembleBatch.TranOverride : Edm.Boolean "Override"
PX.Objects.AM.AMDisassembleBatch.TranOrigDocType : Edm.String "Orig Doc Type"
PX.Objects.AM.AMDisassembleBatch.TranOrigBatNbr : Edm.String "Orig Batch Nbr"
PX.Objects.AM.AMDisassembleBatch.OrigLineNbr : Edm.Int32 "Orig Line Nbr."
PX.Objects.AM.AMDisassembleBatch.TranCreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMDisassembleBatch.TranCreatedByScreenID : Edm.String
PX.Objects.AM.AMDisassembleBatch.TranCreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMDisassembleBatch.TranLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMDisassembleBatch.TranLastModifiedByScreenID : Edm.String
PX.Objects.AM.AMDisassembleBatch.TranLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMDisassembleBatch.TranTstamp : Edm.Binary
PX.Objects.AM.AMDisassembleBatch.LotSerCntr : Edm.Int32 "Lot Serial Cntr"
PX.Objects.AM.AMDisassembleBatch.InventorySource : Edm.String
PX.Objects.AM.AMDisassembleBatch.LineCntrAttribute : Edm.Int32 "Line Cntr Attribute"
PX.Objects.AM.AMDisassembleBatch.QtyScrapped : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.AMDisassembleBatch.BaseQtyScrapped : Edm.Decimal "Scrapped Base Qty."
PX.Objects.AM.AMDisassembleBatch.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMDisassembleBatch.LastOper : Edm.Boolean "Last Oper"
PX.Objects.AM.AMDisassembleBatch.IsByproduct : Edm.Boolean "By-product"
PX.Objects.AM.AMDisassembleBatch.IsScrap : Edm.Boolean "Scrapped"
PX.Objects.AM.AMDisassembleBatch.CostCenterID : Edm.Int32
PX.Objects.AM.AMDisassembleBatch.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.AM.AMDisassembleBatch.EditableBatch : Edm.Boolean "Editable Batch"
PX.Objects.AM.AMDisassembleBatch.BatchByGLBatNbr -> PX.Objects.GL.Batch (GLBatNbr=BatchNbr)
PX.Objects.AM.AMDisassembleBatch.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMDisassembleBatch.INRegisterByINDocType -> PX.Objects.IN.INRegister (INBatNbr=RefNbr, INDocType=DocType)
PX.Objects.AM.AMDisassembleBatch.AMBatchByDocType -> PX.Objects.AM.AMBatch (BatchNbr=BatNbr, DocType=DocType)
PX.Objects.AM.AMDisassembleBatch.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMDisassembleBatch.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMDisassembleBatch.AMBatchByOrigBatNbr -> PX.Objects.AM.AMBatch (OrigDocType=DocType, OrigBatNbr=BatNbr)
PX.Objects.AM.AMDisassembleBatch.AMBatchByOrigDocType -> PX.Objects.AM.AMBatch (OrigBatNbr=BatNbr, OrigDocType=DocType)
PX.Objects.AM.AMDisassembleBatch.AMBatchByMaterialBatNbr -> PX.Objects.AM.AMBatch
PX.Objects.AM.AMDisassembleBatch.INTranByINLineNbr -> PX.Objects.IN.INTran (INDocType=DocType, INBatNbr=RefNbr, INLineNbr=LineNbr)
PX.Objects.AM.AMDisassembleBatch.INRegisterByINBatNbr -> PX.Objects.IN.INRegister (INDocType=DocType, INBatNbr=RefNbr)
PX.Objects.AM.AMDisassembleBatch.AccountByWIPAcctID -> PX.Objects.GL.Account (WIPAcctID=AccountID)
PX.Objects.AM.AMDisassembleBatch.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMDisassembleBatch.SubByWIPSubID -> PX.Objects.GL.Sub (WIPSubID=SubID)
PX.Objects.AM.AMDisassembleBatch.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMDisassembleBatch.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMDisassembleBatch.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.AMDisassembleBatch.AMDisassembleBatchSplitCollection -> Collection(PX.Objects.AM.AMDisassembleBatchSplit)

# PX.Objects.AM.AMDisassembleBatchAttribute (EntityType)

Label: "AM Disassemble Transaction Attribute"
BaseType: PX.Objects.AM.AMMTranAttribute
Key: BatNbr, DocType, LineNbr, ProdAttributeLineNbr, TranLineNbr (inherited from PX.Objects.AM.AMMTranAttribute)
Entity sets: PX_Objects_AM_AMDisassembleBatchAttribute, AMDisassembleTransactionAttribute, AMDisassembleBatchAttribute

# PX.Objects.AM.AMDisassembleBatchSplit (EntityType)

Label: "AM Disassemble Batch Split"
Key: BatNbr, DocType, LineNbr, SplitLineNbr
Entity sets: PX_Objects_AM_AMDisassembleBatchSplit, AMDisassembleBatchSplit
Non-filterable, non-selectable: CostSubItemID, CostSiteID, LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.AM.AMDisassembleBatchSplit.TranType : Edm.String
PX.Objects.AM.AMDisassembleBatchSplit.DocType : Edm.String [key]
PX.Objects.AM.AMDisassembleBatchSplit.BatNbr : Edm.String [key]
PX.Objects.AM.AMDisassembleBatchSplit.LineNbr : Edm.Int32 [key]
PX.Objects.AM.AMDisassembleBatchSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.AM.AMDisassembleBatchSplit.TranDate : Edm.DateTimeOffset
PX.Objects.AM.AMDisassembleBatchSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMDisassembleBatchSplit.CostSubItemID : Edm.Int32
PX.Objects.AM.AMDisassembleBatchSplit.CostSiteID : Edm.Int32
PX.Objects.AM.AMDisassembleBatchSplit.LotSerClassID : Edm.String
PX.Objects.AM.AMDisassembleBatchSplit.AssignedNbr : Edm.String
PX.Objects.AM.AMDisassembleBatchSplit.InvtMult : Edm.Int16
PX.Objects.AM.AMDisassembleBatchSplit.Released : Edm.Boolean
PX.Objects.AM.AMDisassembleBatchSplit.UOM : Edm.String "UOM"
PX.Objects.AM.AMDisassembleBatchSplit.Qty : Edm.Decimal "Quantity"
PX.Objects.AM.AMDisassembleBatchSplit.BaseQty : Edm.Decimal
PX.Objects.AM.AMDisassembleBatchSplit.PlanID : Edm.Int64
PX.Objects.AM.AMDisassembleBatchSplit.OrigSource : Edm.String
PX.Objects.AM.AMDisassembleBatchSplit.OrigBatNbr : Edm.String
PX.Objects.AM.AMDisassembleBatchSplit.OrigLineNbr : Edm.Int32
PX.Objects.AM.AMDisassembleBatchSplit.OrigSplitLineNbr : Edm.Int32
PX.Objects.AM.AMDisassembleBatchSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMDisassembleBatchSplit.CreatedByScreenID : Edm.String
PX.Objects.AM.AMDisassembleBatchSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMDisassembleBatchSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMDisassembleBatchSplit.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMDisassembleBatchSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMDisassembleBatchSplit.tstamp : Edm.Binary
PX.Objects.AM.AMDisassembleBatchSplit.CostCenterID : Edm.Int32
PX.Objects.AM.AMDisassembleBatchSplit.IsStockItem : Edm.Boolean "Stock Item"
PX.Objects.AM.AMDisassembleBatchSplit.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.AMDisassembleBatchSplit.TaskID : Edm.Int32 "Task"
PX.Objects.AM.AMDisassembleBatchSplit.AMDisassembleBatchByLineNbr -> PX.Objects.AM.AMDisassembleBatch (DocType=DocType, BatNbr=BatchNbr, LineNbr=RefLineNbr)
PX.Objects.AM.AMDisassembleBatchSplit.AMMTranByLineNbr -> PX.Objects.AM.AMMTran (DocType=DocType, BatNbr=BatNbr, LineNbr=LineNbr)
PX.Objects.AM.AMDisassembleBatchSplit.AMBatchByBatNbr -> PX.Objects.AM.AMBatch (DocType=DocType, BatNbr=BatNbr)

# PX.Objects.AM.AMDisassembleTran (EntityType)

Label: "AM Disassemble Transaction"
BaseType: PX.Objects.AM.AMMTran
Key: BatNbr, DocType, LineNbr (inherited from PX.Objects.AM.AMMTran)
Entity sets: PX_Objects_AM_AMDisassembleTran, AMDisassembleTransaction, AMDisassembleTran

PX.Objects.AM.AMDisassembleTran.BranchID : Edm.Int32
PX.Objects.AM.AMDisassembleTran.ParentLotSerialNbr : Edm.String "Parent Lot/Serial Nbr."

# PX.Objects.AM.AMDisassembleTranSplit (EntityType)

Label: "AM Disassemble Transaction Split"
BaseType: PX.Objects.AM.AMMTranSplit
Key: BatNbr, DocType, LineNbr, SplitLineNbr (inherited from PX.Objects.AM.AMMTranSplit)
Entity sets: PX_Objects_AM_AMDisassembleTranSplit, AMDisassembleTransactionSplit, AMDisassembleTranSplit

# PX.Objects.AM.AMECOItem (EntityType)

Label: "ECO Item"
Key: ECOID
Entity sets: PX_Objects_AM_AMECOItem, ECOItem, AMECOItem
Non-filterable, non-selectable: ID, NoteText, Rejected

PX.Objects.AM.AMECOItem.ECOID : Edm.String [key] "ECO ID"
PX.Objects.AM.AMECOItem.ID : Edm.String "ID"
PX.Objects.AM.AMECOItem.RevisionID : Edm.String "Revision"
PX.Objects.AM.AMECOItem.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMECOItem.BOMRevisionID : Edm.String "BOM Revision"
PX.Objects.AM.AMECOItem.Descr : Edm.String "Description"
PX.Objects.AM.AMECOItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMECOItem.NoteID : Edm.Guid
PX.Objects.AM.AMECOItem.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMECOItem.LineCntrAttribute : Edm.Int32 [required]
PX.Objects.AM.AMECOItem.LineCntrOperation : Edm.Int32 [required] "Operation Line Cntr"
PX.Objects.AM.AMECOItem.tstamp : Edm.Binary
PX.Objects.AM.AMECOItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMECOItem.CreatedByScreenID : Edm.String
PX.Objects.AM.AMECOItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMECOItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMECOItem.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMECOItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMECOItem.Status : Edm.String "Status"
PX.Objects.AM.AMECOItem.OwnerID : Edm.Int32 "Owner"
PX.Objects.AM.AMECOItem.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.AM.AMECOItem.Hold : Edm.Boolean [required] "Hold"
PX.Objects.AM.AMECOItem.Approved : Edm.Boolean [required] "Approved"
PX.Objects.AM.AMECOItem.Rejected : Edm.Boolean
PX.Objects.AM.AMECOItem.Requestor : Edm.Int32 "Requestor"
PX.Objects.AM.AMECOItem.Priority : Edm.Int32 [required] "Priority"
PX.Objects.AM.AMECOItem.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AM.AMECOItem.RequestDate : Edm.DateTimeOffset "Request Date"
PX.Objects.AM.AMECOItem.EPEmployeeByOwnerID -> PX.Objects.EP.EPEmployee (OwnerID=BAccountID)
PX.Objects.AM.AMECOItem.VendorByRequestor -> PX.Objects.AP.Vendor (Requestor=BAccountID)
PX.Objects.AM.AMECOItem.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.AM.AMECOItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMECOItem.AMBomItemByBOMRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, BOMRevisionID=RevisionID)
PX.Objects.AM.AMECOItem.AMBomItemByBOMID -> PX.Objects.AM.AMBomItem (BOMID=BOMID)
PX.Objects.AM.AMECOItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMECOItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMECOItem.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.AM.AMECOItem.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMECOItem.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMECOItem.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)

# PX.Objects.AM.AMECOSetupApproval (EntityType)

Label: "ECO Setup Approval"
Key: ApprovalID
Entity sets: PX_Objects_AM_AMECOSetupApproval, ECOSetupApproval, AMECOSetupApproval
Non-filterable, non-selectable: NonExistence

PX.Objects.AM.AMECOSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.AM.AMECOSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.AM.AMECOSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.AM.AMECOSetupApproval.tstamp : Edm.Binary
PX.Objects.AM.AMECOSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMECOSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.AM.AMECOSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMECOSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMECOSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMECOSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMECOSetupApproval.NonExistence : Edm.Boolean
PX.Objects.AM.AMECOSetupApproval.IsActive : Edm.Boolean
PX.Objects.AM.AMECOSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMECOSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMECOSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.AM.AMECOSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.AM.AMECRItem (EntityType)

Label: "ECR Item"
Key: ECRID
Entity sets: PX_Objects_AM_AMECRItem, ECRItem, AMECRItem
Non-filterable, non-selectable: ID, NoteText, Rejected

PX.Objects.AM.AMECRItem.ECRID : Edm.String [key] "ECR ID"
PX.Objects.AM.AMECRItem.ID : Edm.String "ID"
PX.Objects.AM.AMECRItem.RevisionID : Edm.String "Revision"
PX.Objects.AM.AMECRItem.ECOID : Edm.String "ECO ID"
PX.Objects.AM.AMECRItem.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMECRItem.BOMRevisionID : Edm.String "BOM Revision"
PX.Objects.AM.AMECRItem.Descr : Edm.String "Description"
PX.Objects.AM.AMECRItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMECRItem.NoteID : Edm.Guid
PX.Objects.AM.AMECRItem.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMECRItem.LineCntrAttribute : Edm.Int32 [required]
PX.Objects.AM.AMECRItem.LineCntrOperation : Edm.Int32 [required] "Operation Line Cntr"
PX.Objects.AM.AMECRItem.tstamp : Edm.Binary
PX.Objects.AM.AMECRItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMECRItem.CreatedByScreenID : Edm.String
PX.Objects.AM.AMECRItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMECRItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMECRItem.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMECRItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMECRItem.Status : Edm.String "Status"
PX.Objects.AM.AMECRItem.OwnerID : Edm.Int32 "Owner"
PX.Objects.AM.AMECRItem.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.AM.AMECRItem.Hold : Edm.Boolean [required] "Hold"
PX.Objects.AM.AMECRItem.Approved : Edm.Boolean [required] "Approved"
PX.Objects.AM.AMECRItem.Rejected : Edm.Boolean
PX.Objects.AM.AMECRItem.Requestor : Edm.Int32 "Requestor"
PX.Objects.AM.AMECRItem.Priority : Edm.Int32 [required] "Priority"
PX.Objects.AM.AMECRItem.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AM.AMECRItem.RequestDate : Edm.DateTimeOffset "Request Date"
PX.Objects.AM.AMECRItem.EPEmployeeByOwnerID -> PX.Objects.EP.EPEmployee (OwnerID=BAccountID)
PX.Objects.AM.AMECRItem.VendorByRequestor -> PX.Objects.AP.Vendor (Requestor=BAccountID)
PX.Objects.AM.AMECRItem.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.AM.AMECRItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMECRItem.AMBomItemByBOMRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, BOMRevisionID=RevisionID)
PX.Objects.AM.AMECRItem.AMBomItemByBOMID -> PX.Objects.AM.AMBomItem (BOMID=BOMID)
PX.Objects.AM.AMECRItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMECRItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMECRItem.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.AM.AMECRItem.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMECRItem.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMECRItem.AMECOItemByECOID -> PX.Objects.AM.AMECOItem (ECOID=ECOID)

# PX.Objects.AM.AMECRSetupApproval (EntityType)

Label: "ECR Setup Approval"
Key: ApprovalID
Entity sets: PX_Objects_AM_AMECRSetupApproval, ECRSetupApproval, AMECRSetupApproval
Non-filterable, non-selectable: NonExistence

PX.Objects.AM.AMECRSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.AM.AMECRSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.AM.AMECRSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.AM.AMECRSetupApproval.tstamp : Edm.Binary
PX.Objects.AM.AMECRSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMECRSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.AM.AMECRSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMECRSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMECRSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMECRSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMECRSetupApproval.NonExistence : Edm.Boolean
PX.Objects.AM.AMECRSetupApproval.IsActive : Edm.Boolean
PX.Objects.AM.AMECRSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMECRSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMECRSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.AM.AMECRSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.AM.AMEstimateClass (EntityType)

Label: "Estimate Class"
Key: EstimateClassID
Entity sets: PX_Objects_AM_AMEstimateClass, EstimateClass, AMEstimateClass
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMEstimateClass.EstimateClassID : Edm.String [key] "Class ID"
PX.Objects.AM.AMEstimateClass.Description : Edm.String "Description"
PX.Objects.AM.AMEstimateClass.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMEstimateClass.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.AM.AMEstimateClass.EngineerID : Edm.Int32 "Engineer"
PX.Objects.AM.AMEstimateClass.LeadTime : Edm.Int32 [required] "Lead Time (Days)"
PX.Objects.AM.AMEstimateClass.OrderQty : Edm.Decimal [required] "Order Qty."
PX.Objects.AM.AMEstimateClass.LaborMarkupPct : Edm.Decimal [required] "Labor Markup (%)"
PX.Objects.AM.AMEstimateClass.MachineMarkupPct : Edm.Decimal [required] "Machine Markup (%)"
PX.Objects.AM.AMEstimateClass.MaterialMarkupPct : Edm.Decimal [required] "Material Markup (%)"
PX.Objects.AM.AMEstimateClass.ToolMarkupPct : Edm.Decimal [required] "Tool Markup (%)"
PX.Objects.AM.AMEstimateClass.OverheadMarkupPct : Edm.Decimal [required] "Overhead Markup (%)"
PX.Objects.AM.AMEstimateClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateClass.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateClass.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateClass.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateClass.NoteID : Edm.Guid
PX.Objects.AM.AMEstimateClass.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMEstimateClass.SubcontractMarkupPct : Edm.Decimal [required] "Subcontract Markup (%)"
PX.Objects.AM.AMEstimateClass.EPEmployeeByEngineerID -> PX.Objects.EP.EPEmployee (EngineerID=BAccountID)
PX.Objects.AM.AMEstimateClass.ContactByEngineerID -> PX.Objects.CR.Contact (EngineerID=ContactID)
PX.Objects.AM.AMEstimateClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateClass.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.AM.AMEstimateClass.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMEstimateClass.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.AM.AMEstimateClass.AMEstimateSetupCollection -> Collection(PX.Objects.AM.AMEstimateSetup)

# PX.Objects.AM.AMEstimateHistory (EntityType)

Label: "Estimate History"
Key: EstimateID, LineNbr
Entity sets: PX_Objects_AM_AMEstimateHistory, EstimateHistory, AMEstimateHistory

PX.Objects.AM.AMEstimateHistory.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimateHistory.LineNbr : Edm.Int32 [key] "History Line Number"
PX.Objects.AM.AMEstimateHistory.RevisionID : Edm.String "Revision"
PX.Objects.AM.AMEstimateHistory.Description : Edm.String "Description"
PX.Objects.AM.AMEstimateHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateHistory.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateHistory.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.AM.AMEstimateHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateHistory.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateHistory.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateHistory.AMEstimateItemByRevisionID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID, RevisionID=RevisionID)
PX.Objects.AM.AMEstimateHistory.AMEstimateItemByEstimateID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID)

# PX.Objects.AM.AMEstimateItem (EntityType)

Label: "Estimate Item"
Key: EstimateID, RevisionID
Entity sets: PX_Objects_AM_AMEstimateItem, EstimateItem, AMEstimateItem
Non-filterable, non-selectable: ExtCostDisplay, NoteText, DescriptionAsPlainText, IsPrimary, CuryRate, CuryViewState

PX.Objects.AM.AMEstimateItem.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimateItem.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMEstimateItem.InventoryID : Edm.Int32
PX.Objects.AM.AMEstimateItem.InventoryCD : Edm.String "Inventory ID"
PX.Objects.AM.AMEstimateItem.IsNonInventory : Edm.Boolean [required] "Non-Inventory"
PX.Objects.AM.AMEstimateItem.ItemDesc : Edm.String "Item Description"
PX.Objects.AM.AMEstimateItem.EstimateClassID : Edm.String "Estimate Class"
PX.Objects.AM.AMEstimateItem.RevisionDate : Edm.DateTimeOffset "Revision Date"
PX.Objects.AM.AMEstimateItem.FixedLaborOverride : Edm.Boolean [required] "Override Fixed Labor Cost"
PX.Objects.AM.AMEstimateItem.FixedLaborCalcCost : Edm.Decimal [required] "Fix Labor Calc"
PX.Objects.AM.AMEstimateItem.FixedLaborCost : Edm.Decimal [required] "Fixed Labor Cost"
PX.Objects.AM.AMEstimateItem.VariableLaborOverride : Edm.Boolean [required] "Override Var. Labor Cost"
PX.Objects.AM.AMEstimateItem.VariableLaborCalcCost : Edm.Decimal [required] "Var Labor Calc"
PX.Objects.AM.AMEstimateItem.VariableLaborCost : Edm.Decimal [required] "Var. Labor Cost"
PX.Objects.AM.AMEstimateItem.MachineOverride : Edm.Boolean [required] "Override Machine Cost"
PX.Objects.AM.AMEstimateItem.MachineCalcCost : Edm.Decimal [required] "Machine Cost Calc"
PX.Objects.AM.AMEstimateItem.MachineCost : Edm.Decimal [required] "Machine Cost"
PX.Objects.AM.AMEstimateItem.MaterialOverride : Edm.Boolean [required] "Override Material Cost"
PX.Objects.AM.AMEstimateItem.MaterialCalcCost : Edm.Decimal [required] "Material Cost Calc"
PX.Objects.AM.AMEstimateItem.MaterialCost : Edm.Decimal [required] "Material Cost"
PX.Objects.AM.AMEstimateItem.ToolOverride : Edm.Boolean [required] "Override Tool Cost"
PX.Objects.AM.AMEstimateItem.ToolCalcCost : Edm.Decimal [required] "Tool Cost Calc"
PX.Objects.AM.AMEstimateItem.ToolCost : Edm.Decimal [required] "Tool Cost"
PX.Objects.AM.AMEstimateItem.FixedOverheadOverride : Edm.Boolean [required] "Override Fixed Overhead Cost"
PX.Objects.AM.AMEstimateItem.FixedOverheadCalcCost : Edm.Decimal [required] "Fix Overhead Calc Cost"
PX.Objects.AM.AMEstimateItem.FixedOverheadCost : Edm.Decimal [required] "Fixed Overhead Cost"
PX.Objects.AM.AMEstimateItem.VariableOverheadOverride : Edm.Boolean [required] "Override Var. Overhead Cost"
PX.Objects.AM.AMEstimateItem.VariableOverheadCalcCost : Edm.Decimal [required] "Var Overhead Cost Calc"
PX.Objects.AM.AMEstimateItem.VariableOverheadCost : Edm.Decimal [required] "Var. Overhead Cost"
PX.Objects.AM.AMEstimateItem.SubcontractOverride : Edm.Boolean [required] "Override Subcontract Cost"
PX.Objects.AM.AMEstimateItem.SubcontractCalcCost : Edm.Decimal [required] "Subcontract Cost Calc"
PX.Objects.AM.AMEstimateItem.SubcontractCost : Edm.Decimal [required] "Subcontract Cost"
PX.Objects.AM.AMEstimateItem.ReferenceMaterialCost : Edm.Decimal [required] "Ref. Material Cost"
PX.Objects.AM.AMEstimateItem.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMEstimateItem.OwnerID : Edm.Int32 "Owner"
PX.Objects.AM.AMEstimateItem.EngineerID : Edm.Int32 "Engineer"
PX.Objects.AM.AMEstimateItem.RequestDate : Edm.DateTimeOffset "Request Date"
PX.Objects.AM.AMEstimateItem.PromiseDate : Edm.DateTimeOffset "Promise Date"
PX.Objects.AM.AMEstimateItem.LeadTime : Edm.Int32 [required] "Lead Time (Days)"
PX.Objects.AM.AMEstimateItem.LeadTimeOverride : Edm.Boolean [required] "Override Lead Time"
PX.Objects.AM.AMEstimateItem.OrderQty : Edm.Decimal [required] "Order Qty."
PX.Objects.AM.AMEstimateItem.BaseOrderQty : Edm.Decimal [required] "Base Order Qty."
PX.Objects.AM.AMEstimateItem.UOM : Edm.String "UOM"
PX.Objects.AM.AMEstimateItem.CuryID : Edm.String "Currency"
PX.Objects.AM.AMEstimateItem.CuryInfoID : Edm.Int64
PX.Objects.AM.AMEstimateItem.ExtCostDisplay : Edm.Decimal "Total Cost"
PX.Objects.AM.AMEstimateItem.ExtCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMEstimateItem.CuryExtCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMEstimateItem.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMEstimateItem.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMEstimateItem.LaborMarkupPct : Edm.Decimal [required] "Labor Markup (%)"
PX.Objects.AM.AMEstimateItem.MachineMarkupPct : Edm.Decimal [required] "Machine Markup (%)"
PX.Objects.AM.AMEstimateItem.MaterialMarkupPct : Edm.Decimal [required] "Material Markup (%)"
PX.Objects.AM.AMEstimateItem.ToolMarkupPct : Edm.Decimal [required] "Tool Markup (%)"
PX.Objects.AM.AMEstimateItem.OverheadMarkupPct : Edm.Decimal [required] "Overhead Markup (%)"
PX.Objects.AM.AMEstimateItem.SubcontractMarkupPct : Edm.Decimal [required] "Subcontract Markup (%)"
PX.Objects.AM.AMEstimateItem.MarkupPct : Edm.Decimal [required] "Overall Markup (%)"
PX.Objects.AM.AMEstimateItem.CuryExtPrice : Edm.Decimal [required] "Total Price"
PX.Objects.AM.AMEstimateItem.ExtPrice : Edm.Decimal [required] "Total Price"
PX.Objects.AM.AMEstimateItem.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.AM.AMEstimateItem.UnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.AM.AMEstimateItem.PriceOverride : Edm.Boolean [required] "Override Unit Price"
PX.Objects.AM.AMEstimateItem.NoteID : Edm.Guid
PX.Objects.AM.AMEstimateItem.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMEstimateItem.ImageURL : Edm.String
PX.Objects.AM.AMEstimateItem.Body : Edm.String "Description"
PX.Objects.AM.AMEstimateItem.DescriptionAsPlainText : Edm.String "DescriptionAsPlainText"
PX.Objects.AM.AMEstimateItem.LineCntrOper : Edm.Int32 [required]
PX.Objects.AM.AMEstimateItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateItem.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateItem.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateItem.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateItem.PrimaryRevisionID : Edm.String "Primary Revision"
PX.Objects.AM.AMEstimateItem.QuoteSource : Edm.Int32 "Quote Source"
PX.Objects.AM.AMEstimateItem.EstimateStatus : Edm.Int32 "Status"
PX.Objects.AM.AMEstimateItem.IsLockedByQuote : Edm.Boolean "Locked by Quote"
PX.Objects.AM.AMEstimateItem.LineCntrHistory : Edm.Int32 "History Line Cntr"
PX.Objects.AM.AMEstimateItem.PCreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateItem.PCreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateItem.PCreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateItem.PLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateItem.PLastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateItem.PLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateItem.IsPrimary : Edm.Boolean "Primary"
PX.Objects.AM.AMEstimateItem.LineCntrPriceBreak : Edm.Int32 [required] "LineCntrPriceBreak"
PX.Objects.AM.AMEstimateItem.HasPriceBreak : Edm.Boolean [required] "Price Breaks"
PX.Objects.AM.AMEstimateItem.MarkupPctOverride : Edm.Boolean [required] "Override Overall Markup (%)"
PX.Objects.AM.AMEstimateItem.PriceBreakPrimaryLineNbr : Edm.Int32 "PriceBreakPrimaryLineNbr"
PX.Objects.AM.AMEstimateItem.RoundUpUnitPrice : Edm.Boolean [required] "Round Unit Prices"
PX.Objects.AM.AMEstimateItem.CuryRate : Edm.Decimal
PX.Objects.AM.AMEstimateItem.CuryViewState : Edm.Boolean
PX.Objects.AM.AMEstimateItem.EPEmployeeByEngineerID -> PX.Objects.EP.EPEmployee (EngineerID=BAccountID)
PX.Objects.AM.AMEstimateItem.EPEmployeeByOwnerID -> PX.Objects.EP.EPEmployee (OwnerID=BAccountID)
PX.Objects.AM.AMEstimateItem.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.AM.AMEstimateItem.ContactByEngineerID -> PX.Objects.CR.Contact (EngineerID=ContactID)
PX.Objects.AM.AMEstimateItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMEstimateItem.InventoryItemByInventoryCD -> PX.Objects.IN.InventoryItem (InventoryCD=InventoryCD)
PX.Objects.AM.AMEstimateItem.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMEstimateItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateItem.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMEstimateItem.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMEstimateItem.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMEstimateItem.INUnitByUOM -> PX.Objects.IN.INUnit (UOM=FromUnit)
PX.Objects.AM.AMEstimateItem.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AM.AMEstimateItem.AMEstimateClassByEstimateClassID -> PX.Objects.AM.AMEstimateClass (EstimateClassID=EstimateClassID)
PX.Objects.AM.AMEstimateItem.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.AM.AMEstimateItem.AMEstimateHistoryCollection -> Collection(PX.Objects.AM.AMEstimateHistory)
PX.Objects.AM.AMEstimateItem.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.AM.AMEstimateItem.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.Objects.AM.AMEstimateItem.AMEstimateOvhdCollection -> Collection(PX.Objects.AM.AMEstimateOvhd)
PX.Objects.AM.AMEstimateItem.AMEstimatePriceBreakCollection -> Collection(PX.Objects.AM.AMEstimatePriceBreak)
PX.Objects.AM.AMEstimateItem.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.AM.AMEstimateItem.AMEstimateStepCollection -> Collection(PX.Objects.AM.AMEstimateStep)
PX.Objects.AM.AMEstimateItem.AMEstimateToolCollection -> Collection(PX.Objects.AM.AMEstimateTool)

# PX.Objects.AM.AMEstimateMatl (EntityType)

Label: "Estimate Material"
Key: EstimateID, LineID, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMEstimateMatl, EstimateMaterial, AMEstimateMatl
Non-filterable, non-selectable: LineNbr, NoteText, QtyReqWithScrap, BaseOrderQty

PX.Objects.AM.AMEstimateMatl.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimateMatl.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMEstimateMatl.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMEstimateMatl.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMEstimateMatl.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMEstimateMatl.InventoryCD : Edm.String "Inventory ID"
PX.Objects.AM.AMEstimateMatl.IsNonInventory : Edm.Boolean [required] "Non-Inventory"
PX.Objects.AM.AMEstimateMatl.ItemDesc : Edm.String "Description"
PX.Objects.AM.AMEstimateMatl.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMEstimateMatl.BackFlush : Edm.Boolean [required] "Backflush Materials"
PX.Objects.AM.AMEstimateMatl.QtyReq : Edm.Decimal [required] "Required Qty."
PX.Objects.AM.AMEstimateMatl.BaseQtyReq : Edm.Decimal [required] "Required Base Qty."
PX.Objects.AM.AMEstimateMatl.UOM : Edm.String "UOM"
PX.Objects.AM.AMEstimateMatl.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMEstimateMatl.MaterialType : Edm.Int32 [required] "Material Type"
PX.Objects.AM.AMEstimateMatl.PhantomRouting : Edm.Int32 [required] "Phantom Routing"
PX.Objects.AM.AMEstimateMatl.ScrapFactor : Edm.Decimal [required] "Scrap Factor"
PX.Objects.AM.AMEstimateMatl.MaterialOperCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMEstimateMatl.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateMatl.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateMatl.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateMatl.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateMatl.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateMatl.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateMatl.LineNbr : Edm.Int32 "Line Nbr. 2"
PX.Objects.AM.AMEstimateMatl.SortOrder : Edm.Int32 "Line Order"
PX.Objects.AM.AMEstimateMatl.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateMatl.NoteID : Edm.Guid
PX.Objects.AM.AMEstimateMatl.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMEstimateMatl.QtyRoundUp : Edm.Boolean [required] "Round Qty. Up"
PX.Objects.AM.AMEstimateMatl.BatchSize : Edm.Decimal [required] "Batch Size"
PX.Objects.AM.AMEstimateMatl.QtyReqWithScrap : Edm.Decimal "Required Qty. with Scrap"
PX.Objects.AM.AMEstimateMatl.TotalQtyRequired : Edm.Decimal [required] "Total Required"
PX.Objects.AM.AMEstimateMatl.BaseTotalQtyRequired : Edm.Decimal [required] "Base Total Required"
PX.Objects.AM.AMEstimateMatl.SubcontractSource : Edm.Int32 [required] "Subcontract Source"
PX.Objects.AM.AMEstimateMatl.BaseOrderQty : Edm.Decimal "Base Order Qty."
PX.Objects.AM.AMEstimateMatl.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMEstimateMatl.InventoryItemByInventoryCD -> PX.Objects.IN.InventoryItem (InventoryCD=InventoryCD)
PX.Objects.AM.AMEstimateMatl.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateMatl.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateMatl.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMEstimateMatl.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMEstimateMatl.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMEstimateMatl.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMEstimateMatl.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMEstimateMatl.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMEstimateMatl.AMEstimateOperByOperationID -> PX.Objects.AM.AMEstimateOper (EstimateID=EstimateID, RevisionID=RevisionID, OperationID=OperationID)
PX.Objects.AM.AMEstimateMatl.AMEstimateItemByRevisionID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID, RevisionID=RevisionID)

# PX.Objects.AM.AMEstimateOper (EntityType)

Label: "Estimate Operations"
Key: EstimateID, OperationCD, RevisionID
Entity sets: PX_Objects_AM_AMEstimateOper, EstimateOperations, AMEstimateOper
Non-filterable, non-selectable: WcID, RunUnitsPerHour, MachineUnitsPerHour, NoteText, SetupTimeRaw, RunUnitTimeRaw, MachineUnitTimeRaw, QueueTimeRaw, FinishTimeRaw, MoveTimeRaw

PX.Objects.AM.AMEstimateOper.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimateOper.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMEstimateOper.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMEstimateOper.OperationCD : Edm.String [key] "Operation ID"
PX.Objects.AM.AMEstimateOper.BaseOrderQty : Edm.Decimal "Base Order Qty."
PX.Objects.AM.AMEstimateOper.WorkCenterID : Edm.String "Work Center"
PX.Objects.AM.AMEstimateOper.WcID : Edm.String "Work Center"
PX.Objects.AM.AMEstimateOper.WorkCenterStdCost : Edm.Decimal [required] "Work Center Standard Cost"
PX.Objects.AM.AMEstimateOper.MachineStdCost : Edm.Decimal [required] "Machine StdCost"
PX.Objects.AM.AMEstimateOper.LineCntrMatl : Edm.Int32 [required]
PX.Objects.AM.AMEstimateOper.LineCntrOvhd : Edm.Int32 [required]
PX.Objects.AM.AMEstimateOper.LineCntrTool : Edm.Int32 [required]
PX.Objects.AM.AMEstimateOper.Description : Edm.String "Operation Desc"
PX.Objects.AM.AMEstimateOper.SetupTime : Edm.Int32 [required] "Setup Time"
PX.Objects.AM.AMEstimateOper.RunUnitTime : Edm.Int32 [required] "Run Time"
PX.Objects.AM.AMEstimateOper.RunUnits : Edm.Decimal [required] "Run Units"
PX.Objects.AM.AMEstimateOper.RunUnitsPerHour : Edm.Decimal "Units Per Hour"
PX.Objects.AM.AMEstimateOper.RunTimeHours : Edm.Decimal [required] "Run Time Hours"
PX.Objects.AM.AMEstimateOper.MachineUnitTime : Edm.Int32 [required] "Machine Time"
PX.Objects.AM.AMEstimateOper.MachineUnits : Edm.Decimal [required] "Machine Units"
PX.Objects.AM.AMEstimateOper.MachineUnitsPerHour : Edm.Decimal "Machine Units Per Hour"
PX.Objects.AM.AMEstimateOper.MachineTimeHours : Edm.Decimal [required] "Machine Time Hours"
PX.Objects.AM.AMEstimateOper.QueueTime : Edm.Int32 [required] "Queue Time"
PX.Objects.AM.AMEstimateOper.FinishTime : Edm.Int32 [required] "Finish Time"
PX.Objects.AM.AMEstimateOper.BackFlushLabor : Edm.Boolean [required] "Backflush Labor"
PX.Objects.AM.AMEstimateOper.FixedLaborOverride : Edm.Boolean [required] "Override Fixed Labor Cost"
PX.Objects.AM.AMEstimateOper.FixedLaborCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.FixedLaborCost : Edm.Decimal [required] "Fixed Labor Cost"
PX.Objects.AM.AMEstimateOper.VariableLaborOverride : Edm.Boolean [required] "Override Var. Labor Cost"
PX.Objects.AM.AMEstimateOper.VariableLaborCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.VariableLaborCost : Edm.Decimal [required] "Var. Labor Cost"
PX.Objects.AM.AMEstimateOper.MachineOverride : Edm.Boolean [required] "Override Machine Cost"
PX.Objects.AM.AMEstimateOper.MachineCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.MachineCost : Edm.Decimal [required] "Machine Cost"
PX.Objects.AM.AMEstimateOper.MaterialOverride : Edm.Boolean [required] "Override Material Cost"
PX.Objects.AM.AMEstimateOper.MaterialCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.MaterialCost : Edm.Decimal [required] "Material Cost"
PX.Objects.AM.AMEstimateOper.ToolOverride : Edm.Boolean [required] "Override Tool Cost"
PX.Objects.AM.AMEstimateOper.ToolUnitCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.ToolCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.ToolCost : Edm.Decimal [required] "Tool Cost"
PX.Objects.AM.AMEstimateOper.FixedOverheadOverride : Edm.Boolean [required] "Override Fixed Overhead Cost"
PX.Objects.AM.AMEstimateOper.FixedOverheadCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.FixedOverheadCost : Edm.Decimal [required] "Fixed Overhead Cost"
PX.Objects.AM.AMEstimateOper.VariableOverheadOverride : Edm.Boolean [required] "Override Var. Overhead Cost"
PX.Objects.AM.AMEstimateOper.VariableOverheadCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.VariableOverheadCost : Edm.Decimal [required] "Var. Overhead Cost"
PX.Objects.AM.AMEstimateOper.SubcontractOverride : Edm.Boolean [required] "Override Subcontract Cost"
PX.Objects.AM.AMEstimateOper.SubcontractCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOper.SubcontractCost : Edm.Decimal [required] "Subcontract Cost"
PX.Objects.AM.AMEstimateOper.ReferenceMaterialCost : Edm.Decimal [required] "Ref. Material Cost"
PX.Objects.AM.AMEstimateOper.ExtCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMEstimateOper.NoteID : Edm.Guid
PX.Objects.AM.AMEstimateOper.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMEstimateOper.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateOper.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateOper.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateOper.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateOper.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateOper.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateOper.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateOper.LineCntrStep : Edm.Int32 [required]
PX.Objects.AM.AMEstimateOper.ControlPoint : Edm.Boolean "Control Point"
PX.Objects.AM.AMEstimateOper.MoveTime : Edm.Int32 [required] "Move Time"
PX.Objects.AM.AMEstimateOper.SetupTimeRaw : Edm.Int32 "SetupTimeRaw"
PX.Objects.AM.AMEstimateOper.RunUnitTimeRaw : Edm.Int32 "RunUnitTimeRaw"
PX.Objects.AM.AMEstimateOper.MachineUnitTimeRaw : Edm.Int32 "MachineUnitTimeRaw"
PX.Objects.AM.AMEstimateOper.QueueTimeRaw : Edm.Int32 "QueueTimeRaw"
PX.Objects.AM.AMEstimateOper.FinishTimeRaw : Edm.Int32 "FinishTimeRaw"
PX.Objects.AM.AMEstimateOper.MoveTimeRaw : Edm.Int32 "MoveTimeRaw"
PX.Objects.AM.AMEstimateOper.OutsideProcess : Edm.Boolean [required] "Outside Process"
PX.Objects.AM.AMEstimateOper.DropShippedToVendor : Edm.Boolean [required] "Drop Shipped to Vendor"
PX.Objects.AM.AMEstimateOper.VendorID : Edm.Int32 "Vendor"
PX.Objects.AM.AMEstimateOper.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AM.AMEstimateOper.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateOper.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateOper.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.AM.AMEstimateOper.LocationByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.AM.AMEstimateOper.AMWCByWorkCenterID -> PX.Objects.AM.AMWC (WorkCenterID=WcID)
PX.Objects.AM.AMEstimateOper.AMEstimateItemByRevisionID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID, RevisionID=RevisionID)
PX.Objects.AM.AMEstimateOper.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.AM.AMEstimateOper.AMEstimateOvhdCollection -> Collection(PX.Objects.AM.AMEstimateOvhd)
PX.Objects.AM.AMEstimateOper.AMEstimateStepCollection -> Collection(PX.Objects.AM.AMEstimateStep)
PX.Objects.AM.AMEstimateOper.AMEstimateToolCollection -> Collection(PX.Objects.AM.AMEstimateTool)

# PX.Objects.AM.AMEstimateOvhd (EntityType)

Label: "Estimate Overhead"
Key: EstimateID, LineID, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMEstimateOvhd, EstimateOverhead, AMEstimateOvhd
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMEstimateOvhd.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimateOvhd.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMEstimateOvhd.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMEstimateOvhd.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMEstimateOvhd.OvhdID : Edm.String "Overhead ID"
PX.Objects.AM.AMEstimateOvhd.OvhdType : Edm.String "Type"
PX.Objects.AM.AMEstimateOvhd.Description : Edm.String "Description"
PX.Objects.AM.AMEstimateOvhd.OverheadCostRate : Edm.Decimal "Overhead Cost Rate"
PX.Objects.AM.AMEstimateOvhd.OFactor : Edm.Decimal [required] "Factor"
PX.Objects.AM.AMEstimateOvhd.FixedOvhdOperCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOvhd.VariableOvhdOperCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateOvhd.WCFlag : Edm.Boolean [required] "WC Flag"
PX.Objects.AM.AMEstimateOvhd.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateOvhd.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateOvhd.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateOvhd.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateOvhd.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateOvhd.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateOvhd.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateOvhd.NoteID : Edm.Guid
PX.Objects.AM.AMEstimateOvhd.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMEstimateOvhd.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateOvhd.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateOvhd.AMEstimateOperByOperationID -> PX.Objects.AM.AMEstimateOper (EstimateID=EstimateID, RevisionID=RevisionID, OperationID=OperationID)
PX.Objects.AM.AMEstimateOvhd.AMOverheadByOvhdID -> PX.Objects.AM.AMOverhead (OvhdID=OvhdID)
PX.Objects.AM.AMEstimateOvhd.AMEstimateItemByRevisionID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID, RevisionID=RevisionID)

# PX.Objects.AM.AMEstimatePriceBreak (EntityType)

Label: "Estimate Price Break"
Key: EstimateID, LineNbr, RevisionID
Entity sets: PX_Objects_AM_AMEstimatePriceBreak, EstimatePriceBreak, AMEstimatePriceBreak
Non-filterable, non-selectable: IsPrimary, NoteText, CuryID, CuryRate, CuryViewState

PX.Objects.AM.AMEstimatePriceBreak.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimatePriceBreak.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMEstimatePriceBreak.LineNbr : Edm.Int32 [key]
PX.Objects.AM.AMEstimatePriceBreak.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMEstimatePriceBreak.CuryInfoID : Edm.Int64
PX.Objects.AM.AMEstimatePriceBreak.IsPrimary : Edm.Boolean "Primary"
PX.Objects.AM.AMEstimatePriceBreak.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.AM.AMEstimatePriceBreak.BaseOrderQty : Edm.Decimal [required]
PX.Objects.AM.AMEstimatePriceBreak.UOM : Edm.String "UOM"
PX.Objects.AM.AMEstimatePriceBreak.LeadTime : Edm.Int32 "Lead Time (Days)"
PX.Objects.AM.AMEstimatePriceBreak.LeadTimeOverride : Edm.Boolean "Override Lead Time"
PX.Objects.AM.AMEstimatePriceBreak.FixedLaborCost : Edm.Decimal [required] "Fixed Labor Cost"
PX.Objects.AM.AMEstimatePriceBreak.FixedLaborCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimatePriceBreak.FixedLaborOverride : Edm.Boolean "Override Fixed Labor Cost"
PX.Objects.AM.AMEstimatePriceBreak.VariableLaborOverride : Edm.Boolean "Override Var. Labor Cost"
PX.Objects.AM.AMEstimatePriceBreak.VariableLaborCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimatePriceBreak.VariableLaborCost : Edm.Decimal [required] "Var. Labor Cost"
PX.Objects.AM.AMEstimatePriceBreak.MachineOverride : Edm.Boolean "Override Machine Cost"
PX.Objects.AM.AMEstimatePriceBreak.MachineCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimatePriceBreak.MachineCost : Edm.Decimal [required] "Machine Cost"
PX.Objects.AM.AMEstimatePriceBreak.MaterialOverride : Edm.Boolean "Override Material Cost"
PX.Objects.AM.AMEstimatePriceBreak.MaterialCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimatePriceBreak.MaterialCost : Edm.Decimal [required] "Material Cost"
PX.Objects.AM.AMEstimatePriceBreak.SubcontractOverride : Edm.Boolean "Override Subcontract Cost"
PX.Objects.AM.AMEstimatePriceBreak.SubcontractCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimatePriceBreak.SubcontractCost : Edm.Decimal [required] "Subcontract Cost"
PX.Objects.AM.AMEstimatePriceBreak.ReferenceMaterialCost : Edm.Decimal [required] "Ref. Material Cost"
PX.Objects.AM.AMEstimatePriceBreak.ToolOverride : Edm.Boolean "Override Tool Cost"
PX.Objects.AM.AMEstimatePriceBreak.ToolCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimatePriceBreak.ToolCost : Edm.Decimal [required] "Tool Cost"
PX.Objects.AM.AMEstimatePriceBreak.FixedOverheadOverride : Edm.Boolean "Override Fixed Overhead Cost"
PX.Objects.AM.AMEstimatePriceBreak.FixedOverheadCalcCost : Edm.Decimal [required] "Fix Overhead Calc Cost"
PX.Objects.AM.AMEstimatePriceBreak.FixedOverheadCost : Edm.Decimal [required] "Fixed Overhead Cost"
PX.Objects.AM.AMEstimatePriceBreak.VariableOverheadOverride : Edm.Boolean "Override Var. Overhead Cost"
PX.Objects.AM.AMEstimatePriceBreak.VariableOverheadCalcCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimatePriceBreak.VariableOverheadCost : Edm.Decimal [required] "Var. Overhead Cost"
PX.Objects.AM.AMEstimatePriceBreak.ExtCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMEstimatePriceBreak.CuryExtCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMEstimatePriceBreak.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMEstimatePriceBreak.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMEstimatePriceBreak.LaborMarkupPct : Edm.Decimal "Labor Markup (%)"
PX.Objects.AM.AMEstimatePriceBreak.MachineMarkupPct : Edm.Decimal "Machine Markup (%)"
PX.Objects.AM.AMEstimatePriceBreak.MaterialMarkupPct : Edm.Decimal "Material Markup (%)"
PX.Objects.AM.AMEstimatePriceBreak.ToolMarkupPct : Edm.Decimal "Tool Markup (%)"
PX.Objects.AM.AMEstimatePriceBreak.OverheadMarkupPct : Edm.Decimal "Overhead Markup (%)"
PX.Objects.AM.AMEstimatePriceBreak.SubcontractMarkupPct : Edm.Decimal "Subcontract Markup (%)"
PX.Objects.AM.AMEstimatePriceBreak.MarkupPct : Edm.Decimal "Overall Markup (%)"
PX.Objects.AM.AMEstimatePriceBreak.MarkupPctOverride : Edm.Boolean "Override Overall Markup (%)"
PX.Objects.AM.AMEstimatePriceBreak.CuryExtPrice : Edm.Decimal [required] "Total Price"
PX.Objects.AM.AMEstimatePriceBreak.ExtPrice : Edm.Decimal [required] "Total Price"
PX.Objects.AM.AMEstimatePriceBreak.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.AM.AMEstimatePriceBreak.UnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.AM.AMEstimatePriceBreak.PriceOverride : Edm.Boolean "Override Unit Price"
PX.Objects.AM.AMEstimatePriceBreak.Print : Edm.Boolean [required] "Print"
PX.Objects.AM.AMEstimatePriceBreak.NoteID : Edm.Guid
PX.Objects.AM.AMEstimatePriceBreak.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMEstimatePriceBreak.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimatePriceBreak.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimatePriceBreak.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimatePriceBreak.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimatePriceBreak.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimatePriceBreak.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimatePriceBreak.tstamp : Edm.Binary
PX.Objects.AM.AMEstimatePriceBreak.CuryID : Edm.String "Currency"
PX.Objects.AM.AMEstimatePriceBreak.CuryRate : Edm.Decimal
PX.Objects.AM.AMEstimatePriceBreak.CuryViewState : Edm.Boolean
PX.Objects.AM.AMEstimatePriceBreak.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimatePriceBreak.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimatePriceBreak.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMEstimatePriceBreak.AMEstimateItemByRevisionID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID, RevisionID=RevisionID)

# PX.Objects.AM.AMEstimateReference (EntityType)

Label: "Estimate Reference"
Key: EstimateID, RevisionID
Entity sets: PX_Objects_AM_AMEstimateReference, EstimateReference, AMEstimateReference
Non-filterable, non-selectable: QuoteNbrLink, CuryID, CuryRate, CuryViewState

PX.Objects.AM.AMEstimateReference.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimateReference.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMEstimateReference.CuryInfoID : Edm.Int64
PX.Objects.AM.AMEstimateReference.OpportunityID : Edm.String "Opportunity ID"
PX.Objects.AM.AMEstimateReference.OpportunityQuoteID : Edm.Guid "Opportunity Quote ID"
PX.Objects.AM.AMEstimateReference.QuoteType : Edm.String "Quote Type"
PX.Objects.AM.AMEstimateReference.QuoteNbr : Edm.String "Quote Nbr"
PX.Objects.AM.AMEstimateReference.QuoteNbrLink : Edm.String "Quote Nbr"
PX.Objects.AM.AMEstimateReference.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMEstimateReference.OrderNbr : Edm.String "Order Nbr"
PX.Objects.AM.AMEstimateReference.TaxLineNbr : Edm.Int32 "Tax Line Nbr."
PX.Objects.AM.AMEstimateReference.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.AM.AMEstimateReference.OrderQty : Edm.Decimal [required] "Order Qty."
PX.Objects.AM.AMEstimateReference.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.AM.AMEstimateReference.UnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.AM.AMEstimateReference.CuryExtPrice : Edm.Decimal [required] "Total Price"
PX.Objects.AM.AMEstimateReference.ExtPrice : Edm.Decimal [required] "Total Price"
PX.Objects.AM.AMEstimateReference.BAccountID : Edm.Int32 "Customer"
PX.Objects.AM.AMEstimateReference.ExternalRefNbr : Edm.String "Ext. Ref. Nbr."
PX.Objects.AM.AMEstimateReference.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateReference.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateReference.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateReference.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateReference.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateReference.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateReference.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateReference.CuryID : Edm.String "Currency"
PX.Objects.AM.AMEstimateReference.CuryRate : Edm.Decimal
PX.Objects.AM.AMEstimateReference.CuryViewState : Edm.Boolean
PX.Objects.AM.AMEstimateReference.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AM.AMEstimateReference.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AM.AMEstimateReference.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AM.AMEstimateReference.SOOrderByOrderType -> PX.Objects.SO.SOOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.AM.AMEstimateReference.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateReference.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateReference.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.AM.AMEstimateReference.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.AM.AMEstimateReference.CROpportunityByOpportunityID -> PX.Objects.CR.CROpportunity (OpportunityID=OpportunityID)
PX.Objects.AM.AMEstimateReference.AMEstimateItemByRevisionID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID, RevisionID=RevisionID)

# PX.Objects.AM.AMEstimateSetup (EntityType)

Label: "Estimate Preferences"
Singletons: PX_Objects_AM_AMEstimateSetup, EstimatePreferences, AMEstimateSetup

PX.Objects.AM.AMEstimateSetup.EstimateNumberingID : Edm.String "Estimate Number Sequence"
PX.Objects.AM.AMEstimateSetup.DefaultRevisionID : Edm.String "Default Revision"
PX.Objects.AM.AMEstimateSetup.AutoNumberRevisionID : Edm.Boolean [required] "Auto Number Revisions"
PX.Objects.AM.AMEstimateSetup.DefaultEstimateClassID : Edm.String "Default Estimate Class"
PX.Objects.AM.AMEstimateSetup.DefaultWorkCenterID : Edm.String "Default Work Center"
PX.Objects.AM.AMEstimateSetup.DefaultOrderType : Edm.String "Default Prod. Order Type"
PX.Objects.AM.AMEstimateSetup.NewRevisionIsPrimary : Edm.Boolean [required] "New Revision Is Primary"
PX.Objects.AM.AMEstimateSetup.CopyEstimateNotes : Edm.Boolean [required] "Copy Estimate Notes"
PX.Objects.AM.AMEstimateSetup.CopyEstimateFiles : Edm.Boolean [required] "Copy Estimate Files"
PX.Objects.AM.AMEstimateSetup.CopyOperationNotes : Edm.Boolean [required] "Copy Operation Notes"
PX.Objects.AM.AMEstimateSetup.CopyOperationFiles : Edm.Boolean [required] "Copy Operation Files"
PX.Objects.AM.AMEstimateSetup.InventoryIDOverride : Edm.Boolean [required] "Override Inventory ID"
PX.Objects.AM.AMEstimateSetup.UpdateAllRevisions : Edm.Boolean [required] "Update All Revisions"
PX.Objects.AM.AMEstimateSetup.UpdatePriceInfo : Edm.Boolean [required] "Update Price Info"
PX.Objects.AM.AMEstimateSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateSetup.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateSetup.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateSetup.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateSetup.NumberingByEstimateNumberingID -> PX.Objects.CS.Numbering (EstimateNumberingID=NumberingID)
PX.Objects.AM.AMEstimateSetup.AMEstimateClassByDefaultEstimateClassID -> PX.Objects.AM.AMEstimateClass (DefaultEstimateClassID=EstimateClassID)
PX.Objects.AM.AMEstimateSetup.AMOrderTypeByDefaultOrderType -> PX.Objects.AM.AMOrderType (DefaultOrderType=OrderType)
PX.Objects.AM.AMEstimateSetup.AMWCByDefaultWorkCenterID -> PX.Objects.AM.AMWC (DefaultWorkCenterID=WcID)

# PX.Objects.AM.AMEstimateStep (EntityType)

Label: "Estimate Step"
Key: EstimateID, LineID, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMEstimateStep, EstimateStep, AMEstimateStep
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMEstimateStep.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimateStep.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMEstimateStep.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMEstimateStep.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMEstimateStep.Description : Edm.String "Description"
PX.Objects.AM.AMEstimateStep.SortOrder : Edm.Int32 "Line Order"
PX.Objects.AM.AMEstimateStep.NoteID : Edm.Guid
PX.Objects.AM.AMEstimateStep.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMEstimateStep.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateStep.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateStep.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateStep.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateStep.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateStep.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateStep.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateStep.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateStep.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateStep.AMEstimateOperByOperationID -> PX.Objects.AM.AMEstimateOper (EstimateID=EstimateID, RevisionID=RevisionID, OperationID=OperationID)
PX.Objects.AM.AMEstimateStep.AMEstimateItemByRevisionID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID, RevisionID=RevisionID)

# PX.Objects.AM.AMEstimateTool (EntityType)

Label: "Estimate Tool"
Key: EstimateID, LineID, OperationID, RevisionID
Entity sets: PX_Objects_AM_AMEstimateTool, EstimateTool, AMEstimateTool
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMEstimateTool.EstimateID : Edm.String [key] "Estimate ID"
PX.Objects.AM.AMEstimateTool.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.AMEstimateTool.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMEstimateTool.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMEstimateTool.QtyReq : Edm.Decimal [required] "Required Qty."
PX.Objects.AM.AMEstimateTool.ToolID : Edm.String "Tool ID"
PX.Objects.AM.AMEstimateTool.Description : Edm.String "Description"
PX.Objects.AM.AMEstimateTool.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMEstimateTool.ToolOperCost : Edm.Decimal [required]
PX.Objects.AM.AMEstimateTool.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMEstimateTool.CreatedByScreenID : Edm.String
PX.Objects.AM.AMEstimateTool.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateTool.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMEstimateTool.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMEstimateTool.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMEstimateTool.tstamp : Edm.Binary
PX.Objects.AM.AMEstimateTool.NoteID : Edm.Guid
PX.Objects.AM.AMEstimateTool.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMEstimateTool.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMEstimateTool.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMEstimateTool.AMEstimateOperByOperationID -> PX.Objects.AM.AMEstimateOper (EstimateID=EstimateID, RevisionID=RevisionID, OperationID=OperationID)
PX.Objects.AM.AMEstimateTool.AMToolMstByToolID -> PX.Objects.AM.AMToolMst (ToolID=ToolID)
PX.Objects.AM.AMEstimateTool.AMEstimateItemByRevisionID -> PX.Objects.AM.AMEstimateItem (EstimateID=EstimateID, RevisionID=RevisionID)

# PX.Objects.AM.AMFeature (EntityType)

Label: "Feature"
Key: FeatureID
Entity sets: PX_Objects_AM_AMFeature, Feature, AMFeature
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMFeature.FeatureID : Edm.String [key] "Feature ID"
PX.Objects.AM.AMFeature.Descr : Edm.String "Description"
PX.Objects.AM.AMFeature.ActiveFlg : Edm.Boolean [required] "Active"
PX.Objects.AM.AMFeature.AllowNonInventoryOptions : Edm.Boolean [required] "Allow Non-Inventory Options"
PX.Objects.AM.AMFeature.DisplayOptionAttributes : Edm.Boolean [required] "Display Option Attributes"
PX.Objects.AM.AMFeature.LineCntrAttribute : Edm.Int32 [required]
PX.Objects.AM.AMFeature.LineCntrOption : Edm.Int32 [required]
PX.Objects.AM.AMFeature.PrintResults : Edm.Boolean [required] "Print Results"
PX.Objects.AM.AMFeature.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMFeature.CreatedByScreenID : Edm.String
PX.Objects.AM.AMFeature.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMFeature.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMFeature.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMFeature.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMFeature.NoteID : Edm.Guid
PX.Objects.AM.AMFeature.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMFeature.tstamp : Edm.Binary
PX.Objects.AM.AMFeature.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMFeature.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMFeature.AMConfigurationFeatureCollection -> Collection(PX.Objects.AM.AMConfigurationFeature)
PX.Objects.AM.AMFeature.AMFeatureAttributeCollection -> Collection(PX.Objects.AM.AMFeatureAttribute)
PX.Objects.AM.AMFeature.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)

# PX.Objects.AM.AMFeatureAttribute (EntityType)

Label: "Feature Attribute"
Key: FeatureID, LineNbr
Entity sets: PX_Objects_AM_AMFeatureAttribute, FeatureAttribute, AMFeatureAttribute
Non-filterable, non-selectable: IsFormula

PX.Objects.AM.AMFeatureAttribute.FeatureID : Edm.String [key] "Feature ID"
PX.Objects.AM.AMFeatureAttribute.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMFeatureAttribute.AttributeID : Edm.String "Attribute ID"
PX.Objects.AM.AMFeatureAttribute.Label : Edm.String "Label"
PX.Objects.AM.AMFeatureAttribute.Descr : Edm.String "Description"
PX.Objects.AM.AMFeatureAttribute.IsFormula : Edm.Boolean "Is Formula"
PX.Objects.AM.AMFeatureAttribute.Enabled : Edm.Boolean [required] "Enabled"
PX.Objects.AM.AMFeatureAttribute.Required : Edm.Boolean [required] "Required"
PX.Objects.AM.AMFeatureAttribute.Visible : Edm.Boolean [required] "Visible"
PX.Objects.AM.AMFeatureAttribute.Value : Edm.String "Default Value"
PX.Objects.AM.AMFeatureAttribute.Variable : Edm.String "Variable"
PX.Objects.AM.AMFeatureAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMFeatureAttribute.CreatedByScreenID : Edm.String
PX.Objects.AM.AMFeatureAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMFeatureAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMFeatureAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMFeatureAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMFeatureAttribute.tstamp : Edm.Binary
PX.Objects.AM.AMFeatureAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMFeatureAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMFeatureAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.AM.AMFeatureAttribute.AMFeatureByFeatureID -> PX.Objects.AM.AMFeature (FeatureID=FeatureID)

# PX.Objects.AM.AMFeatureOption (EntityType)

Label: "Feature Option"
Key: FeatureID, LineNbr
Entity sets: PX_Objects_AM_AMFeatureOption, FeatureOption, AMFeatureOption

PX.Objects.AM.AMFeatureOption.FeatureID : Edm.String [key] "Feature ID"
PX.Objects.AM.AMFeatureOption.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMFeatureOption.Label : Edm.String "Label"
PX.Objects.AM.AMFeatureOption.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMFeatureOption.Descr : Edm.String "Description"
PX.Objects.AM.AMFeatureOption.FixedInclude : Edm.Boolean [required] "Fixed Include"
PX.Objects.AM.AMFeatureOption.QtyEnabled : Edm.Boolean [required] "Enabled Qty."
PX.Objects.AM.AMFeatureOption.QtyRequired : Edm.String "Required Qty."
PX.Objects.AM.AMFeatureOption.UOM : Edm.String "UOM"
PX.Objects.AM.AMFeatureOption.MinQty : Edm.String "Min. Qty."
PX.Objects.AM.AMFeatureOption.MaxQty : Edm.String "Max. Qty."
PX.Objects.AM.AMFeatureOption.LotQty : Edm.String "Lot Qty."
PX.Objects.AM.AMFeatureOption.ScrapFactor : Edm.String "Scrap Factor"
PX.Objects.AM.AMFeatureOption.MaterialType : Edm.Int32 "Material Type"
PX.Objects.AM.AMFeatureOption.PhantomRouting : Edm.Int32 [required] "Phantom Routing"
PX.Objects.AM.AMFeatureOption.PriceFactor : Edm.String "Price Factor"
PX.Objects.AM.AMFeatureOption.ResultsCopy : Edm.Boolean [required] "Results Copy"
PX.Objects.AM.AMFeatureOption.BFlush : Edm.Boolean [required] "Backflush"
PX.Objects.AM.AMFeatureOption.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMFeatureOption.CreatedByScreenID : Edm.String
PX.Objects.AM.AMFeatureOption.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMFeatureOption.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMFeatureOption.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMFeatureOption.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMFeatureOption.tstamp : Edm.Binary
PX.Objects.AM.AMFeatureOption.QtyRoundUp : Edm.Boolean [required] "Round Qty. Up"
PX.Objects.AM.AMFeatureOption.BatchSize : Edm.Decimal [required] "Batch Size"
PX.Objects.AM.AMFeatureOption.SubcontractSource : Edm.Int32 [required] "Subcontract Source"
PX.Objects.AM.AMFeatureOption.PrintResults : Edm.Boolean [required] "Print Results"
PX.Objects.AM.AMFeatureOption.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMFeatureOption.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMFeatureOption.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMFeatureOption.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMFeatureOption.AMFeatureByFeatureID -> PX.Objects.AM.AMFeature (FeatureID=FeatureID)

# PX.Objects.AM.AMFixedDemand (EntityType)

Label: "AM Fixed Demand"
BaseType: PX.Objects.IN.INItemPlan
Key: PlanID (inherited from PX.Objects.IN.INItemPlan)
Entity sets: PX_Objects_AM_AMFixedDemand, AMFixedDemand
Non-filterable, non-selectable: OrderQty, AddLeadTimeDays, NoteText, DemandDocumentType, DemandDocumentID, DemandProjectID, DemandTaskID, DemandCostCodeID, DemandInventorySource, MLProvisioningDocCreationDate, DemandCustomerID, DemandCustomerAcctName, DemandLocationID, CreateSubAssemblyOrders

PX.Objects.AM.AMFixedDemand.UnitMultDiv : Edm.String
PX.Objects.AM.AMFixedDemand.UnitRate : Edm.Decimal
PX.Objects.AM.AMFixedDemand.PlanUnitQty : Edm.Decimal
PX.Objects.AM.AMFixedDemand.OrderQty : Edm.Decimal "Quantity"
PX.Objects.AM.AMFixedDemand.AddLeadTimeDays : Edm.Int16 "Add. Lead Time (Days)"
PX.Objects.AM.AMFixedDemand.AlternateID : Edm.String "Alternate ID"
PX.Objects.AM.AMFixedDemand.SOOrderType : Edm.String "SO Order Type"
PX.Objects.AM.AMFixedDemand.SOOrderNbr : Edm.String "SO Order Nbr."
PX.Objects.AM.AMFixedDemand.SOLineNbr : Edm.Int32 "Line Nbr."
PX.Objects.AM.AMFixedDemand.AMOrderType : Edm.String "Prod. Order Type"
PX.Objects.AM.AMFixedDemand.AMProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMFixedDemand.AMOperationID : Edm.Int32 "Prod. Operation ID"
PX.Objects.AM.AMFixedDemand.AMLineID : Edm.Int32 "Prod. LineID"
PX.Objects.AM.AMFixedDemand.AMProdCreate : Edm.Boolean
PX.Objects.AM.AMFixedDemand.Descr : Edm.String "Description"
PX.Objects.AM.AMFixedDemand.NoteID : Edm.Guid
PX.Objects.AM.AMFixedDemand.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMFixedDemand.DemandDocumentType : Edm.String "Document Type"
PX.Objects.AM.AMFixedDemand.DemandDocumentID : Edm.String "Document"
PX.Objects.AM.AMFixedDemand.DemandProjectID : Edm.Int32
PX.Objects.AM.AMFixedDemand.DemandTaskID : Edm.Int32
PX.Objects.AM.AMFixedDemand.DemandCostCodeID : Edm.Int32
PX.Objects.AM.AMFixedDemand.DemandInventorySource : Edm.String
PX.Objects.AM.AMFixedDemand.MLProvisioningDocCreationDate : Edm.DateTimeOffset
PX.Objects.AM.AMFixedDemand.DemandCustomerID : Edm.Int32 "Customer"
PX.Objects.AM.AMFixedDemand.DemandCustomerAcctName : Edm.String "Customer Name"
PX.Objects.AM.AMFixedDemand.DemandLocationID : Edm.Int32 "Customer Location"
PX.Objects.AM.AMFixedDemand.CreateSubAssemblyOrders : Edm.Boolean "Generate Orders for Subassemblies"
PX.Objects.AM.AMFixedDemand.AMProdOperByAMProdOrdID -> PX.Objects.AM.AMProdOper (AMOperationID=OperationID, AMOrderType=OrderType, AMProdOrdID=ProdOrdID)
PX.Objects.AM.AMFixedDemand.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.AM.AMFixedDemand.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.AM.AMFixedDemand.AMOrderTypeByAMOrderType -> PX.Objects.AM.AMOrderType (AMOrderType=OrderType)
PX.Objects.AM.AMFixedDemand.AMProdItemByAMOrderType -> PX.Objects.AM.AMProdItem (AMProdOrdID=ProdOrdID, AMOrderType=OrderType)

# PX.Objects.AM.AMForecast (EntityType)

Label: "Forecast"
Key: ForecastID
Entity sets: PX_Objects_AM_AMForecast, Forecast, AMForecast
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMForecast.ForecastID : Edm.String [key] "Forecast ID"
PX.Objects.AM.AMForecast.ActiveFlg : Edm.Boolean [required] "Active"
PX.Objects.AM.AMForecast.Interval : Edm.String "Interval"
PX.Objects.AM.AMForecast.BeginDate : Edm.DateTimeOffset "Begin Date"
PX.Objects.AM.AMForecast.CustomerID : Edm.Int32 "Customer"
PX.Objects.AM.AMForecast.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.AMForecast.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMForecast.NoteID : Edm.Guid
PX.Objects.AM.AMForecast.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMForecast.BaseQty : Edm.Decimal
PX.Objects.AM.AMForecast.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMForecast.UOM : Edm.String "UOM"
PX.Objects.AM.AMForecast.Dependent : Edm.Boolean [required] "Dependent"
PX.Objects.AM.AMForecast.tstamp : Edm.Binary
PX.Objects.AM.AMForecast.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMForecast.CreatedByScreenID : Edm.String
PX.Objects.AM.AMForecast.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMForecast.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMForecast.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMForecast.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMForecast.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AM.AMForecast.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AM.AMForecast.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMForecast.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMForecast.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMForecast.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMForecast.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMForecast.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMForecast.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMForecast.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.AM.AMForecast.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.AM.AMForecast.AMForecastPeriodCollection -> Collection(PX.Objects.AM.AMForecastPeriod)

# PX.Objects.AM.AMForecastPeriod (EntityType)

Label: "Forecast Period"
Key: ForecastID, PeriodEnd, PeriodStart, TimePeriod
Entity sets: PX_Objects_AM_AMForecastPeriod, ForecastPeriod, AMForecastPeriod

PX.Objects.AM.AMForecastPeriod.ForecastID : Edm.String [key] "Forecast ID"
PX.Objects.AM.AMForecastPeriod.PeriodStart : Edm.DateTimeOffset [key] "Start Date"
PX.Objects.AM.AMForecastPeriod.PeriodEnd : Edm.DateTimeOffset [key] "End Date"
PX.Objects.AM.AMForecastPeriod.TimePeriod : Edm.String [key] "Time Period"
PX.Objects.AM.AMForecastPeriod.tstamp : Edm.Binary
PX.Objects.AM.AMForecastPeriod.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMForecastPeriod.CreatedByScreenID : Edm.String
PX.Objects.AM.AMForecastPeriod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMForecastPeriod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMForecastPeriod.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMForecastPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMForecastPeriod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMForecastPeriod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMForecastPeriod.AMForecastByForecastID -> PX.Objects.AM.AMForecast (ForecastID=ForecastID)

# PX.Objects.AM.AMForecastStaging (EntityType)

Label: "Forecast Staging"
Key: BeginDate, CustomerID, EndDate, InventoryID, SiteID, SubItemID, UserID
Entity sets: PX_Objects_AM_AMForecastStaging, ForecastStaging, AMForecastStaging
Non-filterable, non-selectable: ChangeUnits, PercentChange, CustomerID2

PX.Objects.AM.AMForecastStaging.BeginDate : Edm.DateTimeOffset [key] "Begin Date"
PX.Objects.AM.AMForecastStaging.EndDate : Edm.DateTimeOffset [key] "End Date"
PX.Objects.AM.AMForecastStaging.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AM.AMForecastStaging.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.AM.AMForecastStaging.ForecastQty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMForecastStaging.UOM : Edm.String "UOM"
PX.Objects.AM.AMForecastStaging.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMForecastStaging.ChangeUnits : Edm.Decimal "Change in Units"
PX.Objects.AM.AMForecastStaging.PercentChange : Edm.Decimal "Percent Change"
PX.Objects.AM.AMForecastStaging.Seasonality : Edm.String "Seasonality"
PX.Objects.AM.AMForecastStaging.CustomerID : Edm.Int32 [key required] "CustomerID"
PX.Objects.AM.AMForecastStaging.Dependent : Edm.Boolean [required] "Dependent"
PX.Objects.AM.AMForecastStaging.UserID : Edm.Guid [key]
PX.Objects.AM.AMForecastStaging.LastYearBaseQty : Edm.Decimal [required] "Last Year Base"
PX.Objects.AM.AMForecastStaging.LastYearSalesQty : Edm.Decimal [required] "Last Year"
PX.Objects.AM.AMForecastStaging.tstamp : Edm.Binary
PX.Objects.AM.AMForecastStaging.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMForecastStaging.CreatedByScreenID : Edm.String
PX.Objects.AM.AMForecastStaging.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMForecastStaging.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMForecastStaging.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMForecastStaging.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMForecastStaging.CustomerID2 : Edm.Int32 "Customer"
PX.Objects.AM.AMForecastStaging.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AM.AMForecastStaging.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMForecastStaging.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMForecastStaging.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMForecastStaging.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMForecastStaging.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMForecastStaging.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.AM.AMForecastStaging.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMForecastStaging.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.AM.AMForecastStaging.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)

# PX.Objects.AM.AMLaborCode (EntityType)

Label: "Labor Code"
Key: LaborCodeID
Entity sets: PX_Objects_AM_AMLaborCode, LaborCode, AMLaborCode
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMLaborCode.LaborType : Edm.String "Type"
PX.Objects.AM.AMLaborCode.LaborCodeID : Edm.String [key] "Labor Code"
PX.Objects.AM.AMLaborCode.Descr : Edm.String "Description"
PX.Objects.AM.AMLaborCode.NoteID : Edm.Guid
PX.Objects.AM.AMLaborCode.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMLaborCode.tstamp : Edm.Binary
PX.Objects.AM.AMLaborCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMLaborCode.CreatedByScreenID : Edm.String
PX.Objects.AM.AMLaborCode.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMLaborCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMLaborCode.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMLaborCode.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMLaborCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMLaborCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMLaborCode.AccountByLaborAccountID -> PX.Objects.GL.Account
PX.Objects.AM.AMLaborCode.AccountByOverheadAccountID -> PX.Objects.GL.Account
PX.Objects.AM.AMLaborCode.SubByLaborSubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMLaborCode.SubByOverheadSubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMLaborCode.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.AMLaborCode.AMShiftCollection -> Collection(PX.Objects.AM.AMShift)

# PX.Objects.AM.AMMach (EntityType)

Label: "Machine"
Key: MachID
Entity sets: PX_Objects_AM_AMMach, Machine, AMMach
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMMach.MachID : Edm.String [key] "Machine ID"
PX.Objects.AM.AMMach.Descr : Edm.String "Description"
PX.Objects.AM.AMMach.ActiveFlg : Edm.Boolean [required] "Active"
PX.Objects.AM.AMMach.DownFlg : Edm.Boolean [required] "Down"
PX.Objects.AM.AMMach.AssetID : Edm.String "Asset ID"
PX.Objects.AM.AMMach.CalendarID : Edm.String "Calendar ID"
PX.Objects.AM.AMMach.MachEff : Edm.Decimal [required] "Efficiency"
PX.Objects.AM.AMMach.ActRunTime : Edm.Decimal [required] "Actual Run Time"
PX.Objects.AM.AMMach.NoteID : Edm.Guid
PX.Objects.AM.AMMach.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMMach.tstamp : Edm.Binary
PX.Objects.AM.AMMach.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMach.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMach.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMach.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMach.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMach.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMach.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMach.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMach.AccountByMachAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMMach.SubByMachSubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMMach.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.AM.AMMach.AMMachSchdCollection -> Collection(PX.Objects.AM.AMMachSchd)
PX.Objects.AM.AMMach.AMMachCurySettingsCollection -> Collection(PX.Objects.AM.AMMachCurySettings)
PX.Objects.AM.AMMach.AMMachSchdDetailCollection -> Collection(PX.Objects.AM.AMMachSchdDetail)
PX.Objects.AM.AMMach.AMWCMachCollection -> Collection(PX.Objects.AM.AMWCMach)

# PX.Objects.AM.AMMachCurySettings (EntityType)

Label: "Machine Currency Settings"
Key: CuryID, MachID
Entity sets: PX_Objects_AM_AMMachCurySettings, MachineCurrencySettings, AMMachCurySettings

PX.Objects.AM.AMMachCurySettings.MachID : Edm.String [key] "Machine ID"
PX.Objects.AM.AMMachCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMMachCurySettings.StdCost : Edm.Decimal [required] "Standard Cost"
PX.Objects.AM.AMMachCurySettings.tstamp : Edm.Binary
PX.Objects.AM.AMMachCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMachCurySettings.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMachCurySettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMachCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMachCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMachCurySettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMachCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMachCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMachCurySettings.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMMachCurySettings.AMMachByMachID -> PX.Objects.AM.AMMach (MachID=MachID)

# PX.Objects.AM.AMMachSchd (EntityType)

Label: "Work Center Schedule"
Key: MachID, SchdDate
Entity sets: PX_Objects_AM_AMMachSchd, WorkCenterSchedule, AMMachSchd
Non-filterable, non-selectable: ResourceID

PX.Objects.AM.AMMachSchd.ResourceID : Edm.String "Resource ID"
PX.Objects.AM.AMMachSchd.MachID : Edm.String [key] "Machine ID"
PX.Objects.AM.AMMachSchd.SchdDate : Edm.DateTimeOffset [key] "Schedule Date"
PX.Objects.AM.AMMachSchd.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.AMMachSchd.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.AMMachSchd.WorkTime : Edm.Int32 [required] "Work Time"
PX.Objects.AM.AMMachSchd.TotalBlocks : Edm.Int32 [required] "Total Blocks"
PX.Objects.AM.AMMachSchd.SchdTime : Edm.Int32 [required] "Schedule Time"
PX.Objects.AM.AMMachSchd.PlanBlocks : Edm.Int32 [required] "Plan Blocks"
PX.Objects.AM.AMMachSchd.SchdBlocks : Edm.Int32 [required] "Scheduled Blocks"
PX.Objects.AM.AMMachSchd.AvailableBlocks : Edm.Int32 [required] "Available Blocks"
PX.Objects.AM.AMMachSchd.ExceptionDate : Edm.Boolean [required] "Exception Date"
PX.Objects.AM.AMMachSchd.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMachSchd.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMachSchd.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMachSchd.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMachSchd.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMachSchd.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMachSchd.tstamp : Edm.Binary
PX.Objects.AM.AMMachSchd.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMachSchd.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMachSchd.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMMachSchd.AMMachByMachID -> PX.Objects.AM.AMMach (MachID=MachID)
PX.Objects.AM.AMMachSchd.AMMachSchdDetailCollection -> Collection(PX.Objects.AM.AMMachSchdDetail)

# PX.Objects.AM.AMMachSchdDetail (EntityType)

Label: "Machine Schedule Detail"
Key: RecordID
Entity sets: PX_Objects_AM_AMMachSchdDetail, MachineScheduleDetail, AMMachSchdDetail
Non-filterable, non-selectable: ResourceID, StartTimeString, EndTimeString

PX.Objects.AM.AMMachSchdDetail.ResourceID : Edm.String "Resource ID"
PX.Objects.AM.AMMachSchdDetail.RecordID : Edm.Int64 [key] "Record ID"
PX.Objects.AM.AMMachSchdDetail.MachID : Edm.String "Machine ID"
PX.Objects.AM.AMMachSchdDetail.SchdKey : Edm.Guid "Schedule Key"
PX.Objects.AM.AMMachSchdDetail.SchdDate : Edm.DateTimeOffset "Schedule Date"
PX.Objects.AM.AMMachSchdDetail.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.AMMachSchdDetail.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.AMMachSchdDetail.StartTimeString : Edm.String "Start Time"
PX.Objects.AM.AMMachSchdDetail.EndTimeString : Edm.String "End Time"
PX.Objects.AM.AMMachSchdDetail.OrderByDate : Edm.DateTimeOffset "Order By Date Time"
PX.Objects.AM.AMMachSchdDetail.Description : Edm.String "Description"
PX.Objects.AM.AMMachSchdDetail.RunTimeBase : Edm.Int32 [required] "Run Time Without Efficiency"
PX.Objects.AM.AMMachSchdDetail.RunTime : Edm.Int32 [required] "Run Time"
PX.Objects.AM.AMMachSchdDetail.PlanBlocks : Edm.Int32 [required] "Plan Blocks"
PX.Objects.AM.AMMachSchdDetail.SchdBlocks : Edm.Int32 [required] "Scheduled Blocks"
PX.Objects.AM.AMMachSchdDetail.IsBreak : Edm.Boolean [required] "Down"
PX.Objects.AM.AMMachSchdDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMachSchdDetail.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMachSchdDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMachSchdDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMachSchdDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMachSchdDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMachSchdDetail.tstamp : Edm.Binary
PX.Objects.AM.AMMachSchdDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMachSchdDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMachSchdDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMMachSchdDetail.AMMachByMachID -> PX.Objects.AM.AMMach (MachID=MachID)
PX.Objects.AM.AMMachSchdDetail.AMMachSchdBySchdDate -> PX.Objects.AM.AMMachSchd (MachID=MachID, SchdDate=SchdDate)

# PX.Objects.AM.AMMPS (EntityType)

Label: "Master Production Schedule"
Key: MPSID, MPSTypeID
Entity sets: PX_Objects_AM_AMMPS, MasterProductionSchedule, AMMPS
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMMPS.MPSTypeID : Edm.String [key] "Type"
PX.Objects.AM.AMMPS.MPSID : Edm.String [key] "MPS ID"
PX.Objects.AM.AMMPS.ActiveFlg : Edm.Boolean [required] "Active"
PX.Objects.AM.AMMPS.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMMPS.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMMPS.PlanDate : Edm.DateTimeOffset "Plan Date"
PX.Objects.AM.AMMPS.BaseQty : Edm.Decimal
PX.Objects.AM.AMMPS.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMMPS.UOM : Edm.String "UOM"
PX.Objects.AM.AMMPS.NoteID : Edm.Guid
PX.Objects.AM.AMMPS.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMMPS.tstamp : Edm.Binary
PX.Objects.AM.AMMPS.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMPS.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMPS.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMPS.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMPS.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMPS.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMPS.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMMPS.AMBomItemBySubItemID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, InventoryID=InventoryID)
PX.Objects.AM.AMMPS.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMMPS.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMPS.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMPS.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMMPS.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMMPS.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMMPS.AMMPSTypeByMPSTypeID -> PX.Objects.AM.AMMPSType (MPSTypeID=MPSTypeID)

# PX.Objects.AM.AMMPSType (EntityType)

Label: "Master Production Schedule Type"
Key: MPSTypeID
Entity sets: PX_Objects_AM_AMMPSType, MasterProductionScheduleType, AMMPSType
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMMPSType.Dependent : Edm.Boolean [required] "Dependent"
PX.Objects.AM.AMMPSType.Descr : Edm.String "Description"
PX.Objects.AM.AMMPSType.MPSNumberingID : Edm.String "Numbering Sequence"
PX.Objects.AM.AMMPSType.MPSTypeID : Edm.String [key] "Type ID"
PX.Objects.AM.AMMPSType.NoteID : Edm.Guid
PX.Objects.AM.AMMPSType.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMMPSType.tstamp : Edm.Binary
PX.Objects.AM.AMMPSType.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMPSType.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMPSType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMPSType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMPSType.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMPSType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMPSType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMPSType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMPSType.NumberingByMpsNumberingID -> PX.Objects.CS.Numbering
PX.Objects.AM.AMMPSType.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.AM.AMMPSType.AMRPSetupCollection -> Collection(PX.Objects.AM.AMRPSetup)

# PX.Objects.AM.AMMRPBucket (EntityType)

Label: "Inventory Planning Buckets"
Key: BucketID
Entity sets: PX_Objects_AM_AMMRPBucket, InventoryPlanningBuckets, AMMRPBucket
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMMRPBucket.BucketID : Edm.String [key] "Bucket ID"
PX.Objects.AM.AMMRPBucket.Descr : Edm.String "Description"
PX.Objects.AM.AMMRPBucket.ActiveFlg : Edm.Boolean [required] "Active"
PX.Objects.AM.AMMRPBucket.NoteID : Edm.Guid
PX.Objects.AM.AMMRPBucket.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMMRPBucket.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMRPBucket.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMRPBucket.CreatedDateTime : Edm.DateTimeOffset "MRP Bucket Date"
PX.Objects.AM.AMMRPBucket.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMRPBucket.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMRPBucket.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMRPBucket.tstamp : Edm.Binary
PX.Objects.AM.AMMRPBucket.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMRPBucket.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMRPBucket.AMMRPBucketDetailCollection -> Collection(PX.Objects.AM.AMMRPBucketDetail)
PX.Objects.AM.AMMRPBucket.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.AM.AMMRPBucket.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)

# PX.Objects.AM.AMMRPBucketDetail (EntityType)

Label: "Inventory Planning Bucket Detail"
Key: Bucket, BucketID
Entity sets: PX_Objects_AM_AMMRPBucketDetail, InventoryPlanningBucketDetail, AMMRPBucketDetail

PX.Objects.AM.AMMRPBucketDetail.BucketID : Edm.String [key] "Bucket ID"
PX.Objects.AM.AMMRPBucketDetail.Bucket : Edm.Int32 [key] "Bucket"
PX.Objects.AM.AMMRPBucketDetail.Value : Edm.Int32 [required] "Value"
PX.Objects.AM.AMMRPBucketDetail.Interval : Edm.Int32 [required] "Interval"
PX.Objects.AM.AMMRPBucketDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMRPBucketDetail.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMRPBucketDetail.CreatedDateTime : Edm.DateTimeOffset "MRP Bucket Date"
PX.Objects.AM.AMMRPBucketDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMRPBucketDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMRPBucketDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMRPBucketDetail.tstamp : Edm.Binary
PX.Objects.AM.AMMRPBucketDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMRPBucketDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMRPBucketDetail.AMMRPBucketByBucketID -> PX.Objects.AM.AMMRPBucket (BucketID=BucketID)

# PX.Objects.AM.AMMRPBucketDetailInq (EntityType)

Label: "Inventory Planning Bucket Detail Inquiry"
Key: Bucket, BucketID, InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_AM_AMMRPBucketDetailInq, InventoryPlanningBucketDetailInquiry, AMMRPBucketDetailInq

PX.Objects.AM.AMMRPBucketDetailInq.BucketID : Edm.String [key] "Bucket ID"
PX.Objects.AM.AMMRPBucketDetailInq.Bucket : Edm.Int32 [key] "Bucket"
PX.Objects.AM.AMMRPBucketDetailInq.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AM.AMMRPBucketDetailInq.SubItemID : Edm.Int32 [key] "SubItem"
PX.Objects.AM.AMMRPBucketDetailInq.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMMRPBucketDetailInq.FromDate : Edm.DateTimeOffset "From Date"
PX.Objects.AM.AMMRPBucketDetailInq.ToDate : Edm.DateTimeOffset "To Date"
PX.Objects.AM.AMMRPBucketDetailInq.BeginQty : Edm.Decimal [required] "Start Qty."
PX.Objects.AM.AMMRPBucketDetailInq.ActualSupply : Edm.Decimal [required] "Actual Supply"
PX.Objects.AM.AMMRPBucketDetailInq.ActualDemand : Edm.Decimal [required] "Actual Demand"
PX.Objects.AM.AMMRPBucketDetailInq.NetQty : Edm.Decimal [required] "Net Qty."
PX.Objects.AM.AMMRPBucketDetailInq.PlannedSupply : Edm.Decimal [required] "Planned Supply"
PX.Objects.AM.AMMRPBucketDetailInq.PlannedDemand : Edm.Decimal [required] "Planned Demand"
PX.Objects.AM.AMMRPBucketDetailInq.EndQty : Edm.Decimal [required] "End Qty."
PX.Objects.AM.AMMRPBucketDetailInq.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMRPBucketDetailInq.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMRPBucketDetailInq.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMRPBucketDetailInq.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMRPBucketDetailInq.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMRPBucketDetailInq.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMRPBucketDetailInq.tstamp : Edm.Binary
PX.Objects.AM.AMMRPBucketDetailInq.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMMRPBucketDetailInq.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMRPBucketDetailInq.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMRPBucketDetailInq.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMMRPBucketDetailInq.AMMRPBucketByBucketID -> PX.Objects.AM.AMMRPBucket (BucketID=BucketID)
PX.Objects.AM.AMMRPBucketDetailInq.AMMRPBucketInqBySiteID -> PX.Objects.AM.AMMRPBucketInq (BucketID=BucketID, InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID)

# PX.Objects.AM.AMMRPBucketInq (EntityType)

Label: "Inventory Planning Bucket Inquiry"
Key: BucketID, InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_AM_AMMRPBucketInq, InventoryPlanningBucketInquiry, AMMRPBucketInq

PX.Objects.AM.AMMRPBucketInq.BucketID : Edm.String [key] "Bucket ID"
PX.Objects.AM.AMMRPBucketInq.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AM.AMMRPBucketInq.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.AM.AMMRPBucketInq.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMMRPBucketInq.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.AM.AMMRPBucketInq.ProductManagerID : Edm.Int32 "Product Mgr."
PX.Objects.AM.AMMRPBucketInq.SafetyStock : Edm.Decimal "Safety Stock"
PX.Objects.AM.AMMRPBucketInq.ReplenishmentSource : Edm.String "Rep. Source"
PX.Objects.AM.AMMRPBucketInq.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.AM.AMMRPBucketInq.LeadTime : Edm.Int32 [required] "Lead Time"
PX.Objects.AM.AMMRPBucketInq.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMRPBucketInq.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMRPBucketInq.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMRPBucketInq.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMRPBucketInq.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMRPBucketInq.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMRPBucketInq.tstamp : Edm.Binary
PX.Objects.AM.AMMRPBucketInq.BAccountByPreferredVendorID -> PX.Objects.CR.BAccount (PreferredVendorID=BAccountID)
PX.Objects.AM.AMMRPBucketInq.ContactByProductManagerID -> PX.Objects.CR.Contact (ProductManagerID=ContactID)
PX.Objects.AM.AMMRPBucketInq.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMMRPBucketInq.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMRPBucketInq.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMRPBucketInq.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMMRPBucketInq.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.AM.AMMRPBucketInq.AMMRPBucketByBucketID -> PX.Objects.AM.AMMRPBucket (BucketID=BucketID)
PX.Objects.AM.AMMRPBucketInq.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)

# PX.Objects.AM.AMMTran (EntityType)

Label: "AM Transaction"
Key: BatNbr, DocType, LineNbr
Entity sets: PX_Objects_AM_AMMTran, AMTransaction, AMMTran
Non-filterable, non-selectable: LaborTimeRaw, NoteText, HasReference, IsStockItem, TranTypeChanged

PX.Objects.AM.AMMTran.DocType : Edm.String [key]
PX.Objects.AM.AMMTran.BatNbr : Edm.String [key] "Batch Nbr."
PX.Objects.AM.AMMTran.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMMTran.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMMTran.LaborType : Edm.String "Labor Type"
PX.Objects.AM.AMMTran.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMMTran.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMMTran.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMMTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMMTran.LaborCodeID : Edm.String "Labor Code"
PX.Objects.AM.AMMTran.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.AM.AMMTran.Qty : Edm.Decimal "Quantity"
PX.Objects.AM.AMMTran.QtyScrapped : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.AMMTran.UOM : Edm.String "UOM"
PX.Objects.AM.AMMTran.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMMTran.TranAmt : Edm.Decimal [required] "Ext. Cost"
PX.Objects.AM.AMMTran.BaseQty : Edm.Decimal "Base Qty."
PX.Objects.AM.AMMTran.BaseQtyScrapped : Edm.Decimal "Scrapped Base Qty."
PX.Objects.AM.AMMTran.Closeflg : Edm.Boolean "Complete"
PX.Objects.AM.AMMTran.EmployeeID : Edm.Int32 "Employee ID"
PX.Objects.AM.AMMTran.ExtCost : Edm.Decimal [required] "Labor Amount"
PX.Objects.AM.AMMTran.GLModule : Edm.String "GL Module"
PX.Objects.AM.AMMTran.GLBatNbr : Edm.String "GL Batch Nbr"
PX.Objects.AM.AMMTran.GLLineNbr : Edm.Int32 "GL Batch Line Nbr"
PX.Objects.AM.AMMTran.INDocType : Edm.String "IN Doc Type"
PX.Objects.AM.AMMTran.INBatNbr : Edm.String "IN Ref Nbr"
PX.Objects.AM.AMMTran.INLineNbr : Edm.Int32 "IN Line Nbr"
PX.Objects.AM.AMMTran.ReceiptNbr : Edm.String "Receipt Nbr."
PX.Objects.AM.AMMTran.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.AMMTran.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.AMMTran.LaborTime : Edm.Int32 "Labor Time"
PX.Objects.AM.AMMTran.LaborTimeRaw : Edm.Int32 "LaborTimeRaw"
PX.Objects.AM.AMMTran.LaborRate : Edm.Decimal "Labor Rate"
PX.Objects.AM.AMMTran.LastOper : Edm.Boolean [required] "Is Last Oper"
PX.Objects.AM.AMMTran.LotSerCntr : Edm.Int32 "LotSerCntr"
PX.Objects.AM.AMMTran.MatlLineId : Edm.Int32 "Material Line ID"
PX.Objects.AM.AMMTran.NoteID : Edm.Guid
PX.Objects.AM.AMMTran.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMMTran.FinPeriodID : Edm.String
PX.Objects.AM.AMMTran.TranPeriodID : Edm.String
PX.Objects.AM.AMMTran.Released : Edm.Boolean [required] "Released"
PX.Objects.AM.AMMTran.ShiftCD : Edm.String "Shift"
PX.Objects.AM.AMMTran.WIPAcctID : Edm.Int32 "WIP Account"
PX.Objects.AM.AMMTran.WIPSubID : Edm.Int32 "WIP Subaccount"
PX.Objects.AM.AMMTran.tstamp : Edm.Binary
PX.Objects.AM.AMMTran.UnassignedQty : Edm.Decimal
PX.Objects.AM.AMMTran.InvtMult : Edm.Int16 [required] "Multiplier"
PX.Objects.AM.AMMTran.TranDesc : Edm.String "Tran Description"
PX.Objects.AM.AMMTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMTran.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMTran.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMTran.HasReference : Edm.Boolean
PX.Objects.AM.AMMTran.OrigDocType : Edm.String "Orig Doc Type"
PX.Objects.AM.AMMTran.OrigBatNbr : Edm.String "Orig Batch Nbr"
PX.Objects.AM.AMMTran.OrigLineNbr : Edm.Int32 "Orig Line Nbr."
PX.Objects.AM.AMMTran.IsByproduct : Edm.Boolean "By-product"
PX.Objects.AM.AMMTran.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.AM.AMMTran.CostCenterID : Edm.Int32
PX.Objects.AM.AMMTran.TimeCardStatus : Edm.Int32 "Time Card Status"
PX.Objects.AM.AMMTran.LineCntrAttribute : Edm.Int32 "LineCntrAttribute"
PX.Objects.AM.AMMTran.ScrapAction : Edm.Int32 "Scrap Action"
PX.Objects.AM.AMMTran.ReasonCodeID : Edm.String "Reason Code"
PX.Objects.AM.AMMTran.IsScrap : Edm.Boolean "Scrapped"
PX.Objects.AM.AMMTran.TranOverride : Edm.Boolean [required] "Override"
PX.Objects.AM.AMMTran.SubcontractSource : Edm.Int32 "Subcontract Source"
PX.Objects.AM.AMMTran.ReferenceCostID : Edm.String "Ref. Cost ID"
PX.Objects.AM.AMMTran.CostRefNoteID : Edm.Guid "Cost Ref Note ID"
PX.Objects.AM.AMMTran.TranTypeChanged : Edm.Boolean
PX.Objects.AM.AMMTran.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.AM.AMMTran.POReceiptLineNbr : Edm.Int32
PX.Objects.AM.AMMTran.IsSplitUnitCost : Edm.Boolean "Is Split Unit Cost"
PX.Objects.AM.AMMTran.IsGLEntry : Edm.Boolean "Is GL Entry"
PX.Objects.AM.AMMTran.IsWIPDebit : Edm.Boolean "WIP Is Debit"
PX.Objects.AM.AMMTran.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AM.AMMTran.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.AM.AMMTran.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.AM.AMMTran.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AM.AMMTran.INTranByINLineNbr -> PX.Objects.IN.INTran (INDocType=DocType, INBatNbr=RefNbr, INLineNbr=LineNbr)
PX.Objects.AM.AMMTran.BatchByGLBatNbr -> PX.Objects.GL.Batch (GLBatNbr=BatchNbr)
PX.Objects.AM.AMMTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMMTran.AMMTranByOrigLineNbr -> PX.Objects.AM.AMMTran (OrigDocType=DocType, OrigBatNbr=BatNbr, OrigLineNbr=LineNbr)
PX.Objects.AM.AMMTran.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMMTran.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMMTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMMTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMTran.ReasonCodeByReasonCodeID -> PX.Objects.CS.ReasonCode (ReasonCodeID=ReasonCodeID)
PX.Objects.AM.AMMTran.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMMTran.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMMTran.INRegisterByINBatNbr -> PX.Objects.IN.INRegister (INDocType=DocType, INBatNbr=RefNbr)
PX.Objects.AM.AMMTran.INRegisterByINDocType -> PX.Objects.IN.INRegister (INBatNbr=RefNbr, INDocType=DocType)
PX.Objects.AM.AMMTran.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMMTran.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMMTran.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMMTran.AccountByWIPAcctID -> PX.Objects.GL.Account (WIPAcctID=AccountID)
PX.Objects.AM.AMMTran.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMMTran.SubByWIPSubID -> PX.Objects.GL.Sub (WIPSubID=SubID)
PX.Objects.AM.AMMTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMMTran.EPShiftCodeByShiftCD -> PX.Objects.EP.EPShiftCode (ShiftCD=ShiftCD)
PX.Objects.AM.AMMTran.AMBatchByBatNbr -> PX.Objects.AM.AMBatch (DocType=DocType, BatNbr=BatNbr)
PX.Objects.AM.AMMTran.AMBatchByOrigBatNbr -> PX.Objects.AM.AMBatch (OrigBatNbr=BatNbr)
PX.Objects.AM.AMMTran.AMLaborCodeByLaborCodeID -> PX.Objects.AM.AMLaborCode (LaborCodeID=LaborCodeID)
PX.Objects.AM.AMMTran.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMMTran.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMMTran.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMMTran.AMProdMatlByMatlLineId -> PX.Objects.AM.AMProdMatl (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID, MatlLineId=LineID)
PX.Objects.AM.AMMTran.AMProdMatlBySubItemID -> PX.Objects.AM.AMProdMatl (MatlLineId=LineID, OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID, InventoryID=InventoryID)
PX.Objects.AM.AMMTran.AMDisassembleBatchByBatNbr -> PX.Objects.AM.AMDisassembleBatch (DocType=DocType, BatNbr=BatchNbr)
PX.Objects.AM.AMMTran.INCostStatusByLocationID -> PX.Objects.IN.INCostStatus (ReceiptNbr=ReceiptNbr, InventoryID=InventoryID)
PX.Objects.AM.AMMTran.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.AM.AMMTran.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.AM.AMMTran.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMMTran.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)

# PX.Objects.AM.AMMTranAttribute (EntityType)

Label: "Transaction Attributes"
Key: BatNbr, DocType, LineNbr, ProdAttributeLineNbr, TranLineNbr
Entity sets: PX_Objects_AM_AMMTranAttribute, TransactionAttributes, AMMTranAttribute

PX.Objects.AM.AMMTranAttribute.DocType : Edm.String [key] "Doc Type"
PX.Objects.AM.AMMTranAttribute.BatNbr : Edm.String [key] "Batch Nbr."
PX.Objects.AM.AMMTranAttribute.TranLineNbr : Edm.Int32 [key] "Tran Line Nbr."
PX.Objects.AM.AMMTranAttribute.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMMTranAttribute.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMMTranAttribute.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMMTranAttribute.ProdAttributeLineNbr : Edm.Int32 [key] "Production Line Nbr."
PX.Objects.AM.AMMTranAttribute.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMMTranAttribute.AttributeID : Edm.String "Attribute ID"
PX.Objects.AM.AMMTranAttribute.Label : Edm.String "Attribute"
PX.Objects.AM.AMMTranAttribute.Descr : Edm.String "Description"
PX.Objects.AM.AMMTranAttribute.TransactionRequired : Edm.Boolean "Required"
PX.Objects.AM.AMMTranAttribute.Value : Edm.String "Value"
PX.Objects.AM.AMMTranAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMTranAttribute.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMTranAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMTranAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMTranAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMTranAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMTranAttribute.tstamp : Edm.Binary
PX.Objects.AM.AMMTranAttribute.AMMTranByTranLineNbr -> PX.Objects.AM.AMMTran (DocType=DocType, BatNbr=BatNbr, TranLineNbr=LineNbr)
PX.Objects.AM.AMMTranAttribute.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMMTranAttribute.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMMTranAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMTranAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMTranAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.AM.AMMTranAttribute.AMBatchByBatNbr -> PX.Objects.AM.AMBatch (DocType=DocType, BatNbr=BatNbr)
PX.Objects.AM.AMMTranAttribute.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMMTranAttribute.AMProdAttributeByProdAttributeLineNbr -> PX.Objects.AM.AMProdAttribute (OrderType=OrderType, ProdOrdID=ProdOrdID, ProdAttributeLineNbr=LineNbr)
PX.Objects.AM.AMMTranAttribute.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMMTranAttribute.AMDisassembleBatchByTranLineNbr -> PX.Objects.AM.AMDisassembleBatch (DocType=DocType, BatNbr=BatchNbr, TranLineNbr=LineNbr)

# PX.Objects.AM.AMMTranLotSerialNbrAll (EntityType)

Label: "AM Transaction All Lot/Serial Nbr"
Key: BatNbr, DocType, LineNbr
Entity sets: PX_Objects_AM_AMMTranLotSerialNbrAll, AMTransactionAllLotSerialNbr, AMMTranLotSerialNbrAll

PX.Objects.AM.AMMTranLotSerialNbrAll.DocType : Edm.String [key]
PX.Objects.AM.AMMTranLotSerialNbrAll.BatNbr : Edm.String [key]
PX.Objects.AM.AMMTranLotSerialNbrAll.LineNbr : Edm.Int32 [key]
PX.Objects.AM.AMMTranLotSerialNbrAll.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMMTranLotSerialNbrAll.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMMTranLotSerialNbrAll.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMMTranLotSerialNbrAll.MatlLineId : Edm.Int32
PX.Objects.AM.AMMTranLotSerialNbrAll.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMMTranLotSerialNbrAll.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMMTranLotSerialNbrAll.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMMTranLotSerialNbrAll.INItemLotSerialByLotSerialNbr -> PX.Objects.IN.INItemLotSerial
PX.Objects.AM.AMMTranLotSerialNbrAll.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMMTranLotSerialNbrAll.AMBatchByBatNbr -> PX.Objects.AM.AMBatch (DocType=DocType, BatNbr=BatNbr)
PX.Objects.AM.AMMTranLotSerialNbrAll.AMBatchByOrigBatNbr -> PX.Objects.AM.AMBatch
PX.Objects.AM.AMMTranLotSerialNbrAll.AMDisassembleBatchByBatNbr -> PX.Objects.AM.AMDisassembleBatch (DocType=DocType, BatNbr=BatchNbr)
PX.Objects.AM.AMMTranLotSerialNbrAll.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.AM.AMMTranLotSerialNbrAll.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMMTranLotSerialNbrAll.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)

# PX.Objects.AM.AMMTranMoveByLotSerial (EntityType)

Label: "AM Transaction by LotSerial"
Key: BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID, SiteID
Entity sets: PX_Objects_AM_AMMTranMoveByLotSerial, AMTransactionbyLotSerial, AMMTranMoveByLotSerial

PX.Objects.AM.AMMTranMoveByLotSerial.DocType : Edm.String [key]
PX.Objects.AM.AMMTranMoveByLotSerial.BatNbr : Edm.String [key]
PX.Objects.AM.AMMTranMoveByLotSerial.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMMTranMoveByLotSerial.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.AMMTranMoveByLotSerial.BaseQty : Edm.Decimal "Base Quantity"
PX.Objects.AM.AMMTranMoveByLotSerial.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMMTranMoveByLotSerial.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMMTranMoveByLotSerial.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMMTranMoveByLotSerial.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMMTranMoveByLotSerial.AMMTranByLineNbr -> PX.Objects.AM.AMMTran (DocType=DocType, BatNbr=BatNbr)
PX.Objects.AM.AMMTranMoveByLotSerial.AMBatchByBatNbr -> PX.Objects.AM.AMBatch (DocType=DocType, BatNbr=BatNbr)

# PX.Objects.AM.AMMTranSplit (EntityType)

Label: "AM Transaction Split"
Key: BatNbr, DocType, LineNbr, SplitLineNbr
Entity sets: PX_Objects_AM_AMMTranSplit, AMTransactionSplit, AMMTranSplit
Non-filterable, non-selectable: CostSubItemID, CostSiteID, LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.AM.AMMTranSplit.TranType : Edm.String
PX.Objects.AM.AMMTranSplit.DocType : Edm.String [key]
PX.Objects.AM.AMMTranSplit.BatNbr : Edm.String [key]
PX.Objects.AM.AMMTranSplit.LineNbr : Edm.Int32 [key]
PX.Objects.AM.AMMTranSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.AM.AMMTranSplit.TranDate : Edm.DateTimeOffset "Date"
PX.Objects.AM.AMMTranSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMMTranSplit.CostSubItemID : Edm.Int32
PX.Objects.AM.AMMTranSplit.CostSiteID : Edm.Int32
PX.Objects.AM.AMMTranSplit.LotSerClassID : Edm.String
PX.Objects.AM.AMMTranSplit.AssignedNbr : Edm.String
PX.Objects.AM.AMMTranSplit.InvtMult : Edm.Int16
PX.Objects.AM.AMMTranSplit.Released : Edm.Boolean [required]
PX.Objects.AM.AMMTranSplit.UOM : Edm.String "UOM"
PX.Objects.AM.AMMTranSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMMTranSplit.BaseQty : Edm.Decimal
PX.Objects.AM.AMMTranSplit.PlanID : Edm.Int64
PX.Objects.AM.AMMTranSplit.OrigSource : Edm.String
PX.Objects.AM.AMMTranSplit.OrigBatNbr : Edm.String
PX.Objects.AM.AMMTranSplit.OrigLineNbr : Edm.Int32
PX.Objects.AM.AMMTranSplit.OrigSplitLineNbr : Edm.Int32
PX.Objects.AM.AMMTranSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMMTranSplit.CreatedByScreenID : Edm.String
PX.Objects.AM.AMMTranSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMTranSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMMTranSplit.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMMTranSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMMTranSplit.tstamp : Edm.Binary
PX.Objects.AM.AMMTranSplit.IsStockItem : Edm.Boolean "Stock Item"
PX.Objects.AM.AMMTranSplit.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.AMMTranSplit.TaskID : Edm.Int32 "Task"
PX.Objects.AM.AMMTranSplit.CostCenterID : Edm.Int32
PX.Objects.AM.AMMTranSplit.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMMTranSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMMTranSplit.AMMTranByLineNbr -> PX.Objects.AM.AMMTran (DocType=DocType, BatNbr=BatNbr, LineNbr=LineNbr)
PX.Objects.AM.AMMTranSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMMTranSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMMTranSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMMTranSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMMTranSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMMTranSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMMTranSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMMTranSplit.AMBatchByBatNbr -> PX.Objects.AM.AMBatch (DocType=DocType, BatNbr=BatNbr)
PX.Objects.AM.AMMTranSplit.AMBatchItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.AM.AMBatchItemLotSerialAttributesHeader (DocType=DocType, BatNbr=BatNbr, InventoryID=InventoryID)
PX.Objects.AM.AMMTranSplit.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID)
PX.Objects.AM.AMMTranSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)

# PX.Objects.AM.AMOrderCrossRef (EntityType)

Label: "Order Cross Reference"
Key: LineNbr, UserID
Entity sets: PX_Objects_AM_AMOrderCrossRef, OrderCrossReference, AMOrderCrossRef
Non-filterable, non-selectable: DmdDetGroupedRecNbrs, CreateSubAssemblyOrders, Action

PX.Objects.AM.AMOrderCrossRef.ProcessSource : Edm.Int32 "Process Source"
PX.Objects.AM.AMOrderCrossRef.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMOrderCrossRef.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMOrderCrossRef.DmdDetRecNbr : Edm.Int32 [required] "Demand Detail Rec Nbr"
PX.Objects.AM.AMOrderCrossRef.DmdDetGroupedRecNbrs : Edm.String "Demand Detail Group Rec Nbrs"
PX.Objects.AM.AMOrderCrossRef.ExplodeBOM : Edm.Boolean [required] "Explode BOM"
PX.Objects.AM.AMOrderCrossRef.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMOrderCrossRef.ParentOrderType : Edm.String "Order Type"
PX.Objects.AM.AMOrderCrossRef.ParentProdOrdID : Edm.String "Parent Production Order Nbr"
PX.Objects.AM.AMOrderCrossRef.PlanDate : Edm.DateTimeOffset "Plan Date"
PX.Objects.AM.AMOrderCrossRef.BaseQty : Edm.Decimal "Base Qty."
PX.Objects.AM.AMOrderCrossRef.Qty : Edm.Decimal "Quantity"
PX.Objects.AM.AMOrderCrossRef.Released : Edm.Boolean [required]
PX.Objects.AM.AMOrderCrossRef.ReferenceOrderType : Edm.String "Reference Order Type"
PX.Objects.AM.AMOrderCrossRef.ReferenceNbr : Edm.String "Reference Nbr"
PX.Objects.AM.AMOrderCrossRef.ReferenceType : Edm.String "Reference Type"
PX.Objects.AM.AMOrderCrossRef.ReferenceLineNbr : Edm.Int32 "Refference Line Nbr"
PX.Objects.AM.AMOrderCrossRef.Source : Edm.String "Source"
PX.Objects.AM.AMOrderCrossRef.UOM : Edm.String "UOM"
PX.Objects.AM.AMOrderCrossRef.VendorID : Edm.Int32 "Vendor"
PX.Objects.AM.AMOrderCrossRef.GroupNumber : Edm.Int32 "Group Nbr."
PX.Objects.AM.AMOrderCrossRef.CustomerID : Edm.Int32 "Customer"
PX.Objects.AM.AMOrderCrossRef.UserID : Edm.Guid [key] "User ID"
PX.Objects.AM.AMOrderCrossRef.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMOrderCrossRef.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMOrderCrossRef.ManualNumbering : Edm.Boolean [required]
PX.Objects.AM.AMOrderCrossRef.tstamp : Edm.Binary
PX.Objects.AM.AMOrderCrossRef.CreateSubAssemblyOrders : Edm.Boolean "Generate Orders for Subassemblies"
PX.Objects.AM.AMOrderCrossRef.Action : Edm.String "Action"
PX.Objects.AM.AMOrderCrossRef.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AM.AMOrderCrossRef.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AM.AMOrderCrossRef.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMOrderCrossRef.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMOrderCrossRef.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMOrderCrossRef.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMOrderCrossRef.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)

# PX.Objects.AM.AMOrderType (EntityType)

Label: "AM Order Types"
Key: OrderType
Entity sets: PX_Objects_AM_AMOrderType, AMOrderTypes, AMOrderType
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMOrderType.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMOrderType.Active : Edm.Boolean [required] "Active"
PX.Objects.AM.AMOrderType.Descr : Edm.String "Description"
PX.Objects.AM.AMOrderType.Function : Edm.Int32 [required] "Function"
PX.Objects.AM.AMOrderType.ProdNumberingID : Edm.String "Order Numbering Sequence"
PX.Objects.AM.AMOrderType.CopyNotesItem : Edm.Boolean [required] "Item/Header"
PX.Objects.AM.AMOrderType.CopyNotesOper : Edm.Boolean [required] "Operation"
PX.Objects.AM.AMOrderType.CopyNotesMatl : Edm.Boolean [required] "Material"
PX.Objects.AM.AMOrderType.CopyNotesStep : Edm.Boolean [required] "Step"
PX.Objects.AM.AMOrderType.CopyNotesTool : Edm.Boolean [required] "Tool"
PX.Objects.AM.AMOrderType.CopyNotesOvhd : Edm.Boolean [required] "Overhead"
PX.Objects.AM.AMOrderType.DefaultCostMethod : Edm.Int32 [required] "Costing Method"
PX.Objects.AM.AMOrderType.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMOrderType.CreatedByScreenID : Edm.String
PX.Objects.AM.AMOrderType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMOrderType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMOrderType.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMOrderType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMOrderType.tstamp : Edm.Binary
PX.Objects.AM.AMOrderType.NoteID : Edm.Guid
PX.Objects.AM.AMOrderType.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMOrderType.UnderIssueMaterial : Edm.String "Under Issue Material"
PX.Objects.AM.AMOrderType.MoveCompletedOrders : Edm.String "Move on Completed Operations"
PX.Objects.AM.AMOrderType.OverCompleteOrders : Edm.String "Excess Qty. for Orders"
PX.Objects.AM.AMOrderType.ExceedQtyOperations : Edm.String "Excess Qty. for Operations"
PX.Objects.AM.AMOrderType.ScrapSource : Edm.Int32 [required] "Scrap Source"
PX.Objects.AM.AMOrderType.OverIssueMaterial : Edm.String "Over Issue Material"
PX.Objects.AM.AMOrderType.IncludeUnreleasedOverIssueMaterial : Edm.Boolean [required] "Include Unreleased Batch Qty."
PX.Objects.AM.AMOrderType.BackflushUnderIssueMaterial : Edm.String "Under Issue Backflush Material"
PX.Objects.AM.AMOrderType.IssueMaterialOnTheFly : Edm.String "Issue Material Not On Order"
PX.Objects.AM.AMOrderType.ExcludeFromMRP : Edm.Boolean [required] "Exclude from MRP"
PX.Objects.AM.AMOrderType.DefaultOperationMoveQty : Edm.Boolean [required] "Default Operation Move Qty."
PX.Objects.AM.AMOrderType.ProductionReportID : Edm.String "Print Production Report ID"
PX.Objects.AM.AMOrderType.SubstituteWorkCenters : Edm.Boolean [required] "Substitute Work Centers"
PX.Objects.AM.AMOrderType.LineCntrAttribute : Edm.Int32 [required]
PX.Objects.AM.AMOrderType.AutoBackwardReporting : Edm.Boolean [required] "Automatic Backward Reporting"
PX.Objects.AM.AMOrderType.IsProcessMFG : Edm.Boolean [required] "Process Manufacturing"
PX.Objects.AM.AMOrderType.AddSubassemblySuffix : Edm.Boolean "Add Suffix for Production Subassemblies"
PX.Objects.AM.AMOrderType.SiteMapByProductionReportID -> PX.SM.SiteMap (ProductionReportID=ScreenID)
PX.Objects.AM.AMOrderType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMOrderType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMOrderType.NumberingByProdNumberingID -> PX.Objects.CS.Numbering (ProdNumberingID=NumberingID)
PX.Objects.AM.AMOrderType.INLocationByScrapSiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMOrderType.INLocationByScrapLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMOrderType.INSiteByScrapSiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMOrderType.AccountByWIPAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMOrderType.AccountByWIPVarianceAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMOrderType.SubByWIPSubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMOrderType.SubByWIPVarianceSubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMOrderType.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.AM.AMOrderType.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.AM.AMOrderType.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMOrderType.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.AMOrderType.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.AM.AMOrderType.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.AM.AMOrderType.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.AM.AMOrderType.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.AM.AMOrderType.AMEstimateSetupCollection -> Collection(PX.Objects.AM.AMEstimateSetup)
PX.Objects.AM.AMOrderType.AMOrderTypeAttributeCollection -> Collection(PX.Objects.AM.AMOrderTypeAttribute)
PX.Objects.AM.AMOrderType.AMProdAttributeCollection -> Collection(PX.Objects.AM.AMProdAttribute)
PX.Objects.AM.AMOrderType.AMProdEvntCollection -> Collection(PX.Objects.AM.AMProdEvnt)
PX.Objects.AM.AMOrderType.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.AM.AMOrderType.AMProdMatlLotSerialCollection -> Collection(PX.Objects.AM.AMProdMatlLotSerial)
PX.Objects.AM.AMOrderType.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.AM.AMOrderType.AMProdNumberCollection -> Collection(PX.Objects.AM.AMProdNumber)
PX.Objects.AM.AMOrderType.AMProdOvhdCollection -> Collection(PX.Objects.AM.AMProdOvhd)
PX.Objects.AM.AMOrderType.AMProdStepCollection -> Collection(PX.Objects.AM.AMProdStep)
PX.Objects.AM.AMOrderType.AMProdToolCollection -> Collection(PX.Objects.AM.AMProdTool)
PX.Objects.AM.AMOrderType.AMProdTotalCollection -> Collection(PX.Objects.AM.AMProdTotal)
PX.Objects.AM.AMOrderType.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.AM.AMOrderType.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.Objects.AM.AMOrderType.AMSchdOperDetailCollection -> Collection(PX.Objects.AM.AMSchdOperDetail)
PX.Objects.AM.AMOrderType.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.AM.AMOrderType.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.AM.AMOrderType.AMSFKRecentActivityCollection -> Collection(PX.Objects.AM.SFK.AMSFKRecentActivity)
PX.Objects.AM.AMOrderType.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)
PX.Objects.AM.AMOrderType.SelectedProdMatlCollection -> Collection(PX.Objects.AM.SelectedProdMatl)
PX.Objects.AM.AMOrderType.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)
PX.Objects.AM.AMOrderType.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.AM.AMOrderType.AMPSetupCollection -> Collection(PX.Objects.AM.AMPSetup)
PX.Objects.AM.AMOrderType.AMRPSetupCollection -> Collection(PX.Objects.AM.AMRPSetup)
PX.Objects.AM.AMOrderType.AMMTranMoveByLotSerialCollection -> Collection(PX.Objects.AM.AMMTranMoveByLotSerial)
PX.Objects.AM.AMOrderType.AMMTranLotSerialNbrAllCollection -> Collection(PX.Objects.AM.AMMTranLotSerialNbrAll)
PX.Objects.AM.AMOrderType.AMProdItemSplitPreassignCollection -> Collection(PX.Objects.AM.AMProdItemSplitPreassign)

# PX.Objects.AM.AMOrderTypeAttribute (EntityType)

Label: "Order Type Attributes"
Key: LineNbr, OrderType
Entity sets: PX_Objects_AM_AMOrderTypeAttribute, OrderTypeAttributes, AMOrderTypeAttribute

PX.Objects.AM.AMOrderTypeAttribute.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMOrderTypeAttribute.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.AM.AMOrderTypeAttribute.AttributeID : Edm.String "Attribute ID"
PX.Objects.AM.AMOrderTypeAttribute.Label : Edm.String "Label"
PX.Objects.AM.AMOrderTypeAttribute.Descr : Edm.String "Description"
PX.Objects.AM.AMOrderTypeAttribute.Enabled : Edm.Boolean [required] "Enabled"
PX.Objects.AM.AMOrderTypeAttribute.TransactionRequired : Edm.Boolean [required] "Transaction Required"
PX.Objects.AM.AMOrderTypeAttribute.Value : Edm.String "Value"
PX.Objects.AM.AMOrderTypeAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMOrderTypeAttribute.CreatedByScreenID : Edm.String
PX.Objects.AM.AMOrderTypeAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMOrderTypeAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMOrderTypeAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMOrderTypeAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMOrderTypeAttribute.tstamp : Edm.Binary
PX.Objects.AM.AMOrderTypeAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMOrderTypeAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMOrderTypeAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.AM.AMOrderTypeAttribute.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)

# PX.Objects.AM.AMOverhead (EntityType)

Label: "Overhead"
Key: OvhdID
Entity sets: PX_Objects_AM_AMOverhead, Overhead, AMOverhead
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMOverhead.OvhdID : Edm.String [key] "Overhead ID"
PX.Objects.AM.AMOverhead.CostRate : Edm.Decimal [required] "Cost Rate"
PX.Objects.AM.AMOverhead.Descr : Edm.String "Description"
PX.Objects.AM.AMOverhead.NoteID : Edm.Guid
PX.Objects.AM.AMOverhead.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMOverhead.OvhdType : Edm.String "Type"
PX.Objects.AM.AMOverhead.tstamp : Edm.Binary
PX.Objects.AM.AMOverhead.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMOverhead.CreatedByScreenID : Edm.String
PX.Objects.AM.AMOverhead.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMOverhead.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMOverhead.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMOverhead.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMOverhead.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMOverhead.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMOverhead.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMOverhead.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMOverhead.AMBomOvhdCollection -> Collection(PX.Objects.AM.AMBomOvhd)
PX.Objects.AM.AMOverhead.AMEstimateOvhdCollection -> Collection(PX.Objects.AM.AMEstimateOvhd)
PX.Objects.AM.AMOverhead.AMOverheadCurySettingsCollection -> Collection(PX.Objects.AM.AMOverheadCurySettings)
PX.Objects.AM.AMOverhead.AMProdOvhdCollection -> Collection(PX.Objects.AM.AMProdOvhd)
PX.Objects.AM.AMOverhead.AMWCOvhdCollection -> Collection(PX.Objects.AM.AMWCOvhd)

# PX.Objects.AM.AMOverheadCurySettings (EntityType)

Label: "Overhead Currency Settings"
Key: CuryID, OvhdID
Entity sets: PX_Objects_AM_AMOverheadCurySettings, OverheadCurrencySettings, AMOverheadCurySettings

PX.Objects.AM.AMOverheadCurySettings.OvhdID : Edm.String [key] "Overhead ID"
PX.Objects.AM.AMOverheadCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMOverheadCurySettings.CostRate : Edm.Decimal [required] "Cost Rate"
PX.Objects.AM.AMOverheadCurySettings.tstamp : Edm.Binary
PX.Objects.AM.AMOverheadCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMOverheadCurySettings.CreatedByScreenID : Edm.String
PX.Objects.AM.AMOverheadCurySettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMOverheadCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMOverheadCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMOverheadCurySettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMOverheadCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMOverheadCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMOverheadCurySettings.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMOverheadCurySettings.AMOverheadByOvhdID -> PX.Objects.AM.AMOverhead (OvhdID=OvhdID)

# PX.Objects.AM.AMProdAttribute (EntityType)

Label: "Production Attributes"
Key: LineNbr, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdAttribute, ProductionAttributes, AMProdAttribute

PX.Objects.AM.AMProdAttribute.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdAttribute.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdAttribute.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMProdAttribute.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMProdAttribute.Level : Edm.Int32 [required] "Level"
PX.Objects.AM.AMProdAttribute.Source : Edm.Int32 [required] "Source"
PX.Objects.AM.AMProdAttribute.AttributeID : Edm.String "Attribute ID"
PX.Objects.AM.AMProdAttribute.Label : Edm.String "Label"
PX.Objects.AM.AMProdAttribute.Descr : Edm.String "Description"
PX.Objects.AM.AMProdAttribute.Enabled : Edm.Boolean [required] "Enabled"
PX.Objects.AM.AMProdAttribute.TransactionRequired : Edm.Boolean [required] "Transaction Required"
PX.Objects.AM.AMProdAttribute.Value : Edm.String "Value"
PX.Objects.AM.AMProdAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdAttribute.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdAttribute.tstamp : Edm.Binary
PX.Objects.AM.AMProdAttribute.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMProdAttribute.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.AM.AMProdAttribute.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdAttribute.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdAttribute.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)

# PX.Objects.AM.AMProdEvnt (EntityType)

Label: "Production Event"
Key: LineNbr, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdEvnt, ProductionEvent, AMProdEvnt
Non-filterable, non-selectable: CreatedByScreenIDTitle

PX.Objects.AM.AMProdEvnt.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdEvnt.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdEvnt.LineNbr : Edm.Int32 [key] "Event Line Number"
PX.Objects.AM.AMProdEvnt.Description : Edm.String "Description"
PX.Objects.AM.AMProdEvnt.EventType : Edm.Int32 [required] "Type"
PX.Objects.AM.AMProdEvnt.RefBatNbr : Edm.String "Batch Nbr."
PX.Objects.AM.AMProdEvnt.RefDocType : Edm.String "Doc Type"
PX.Objects.AM.AMProdEvnt.RefNoteID : Edm.Guid "Related Document"
PX.Objects.AM.AMProdEvnt.tstamp : Edm.Binary
PX.Objects.AM.AMProdEvnt.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdEvnt.CreatedByScreenID : Edm.String "Created Screen ID"
PX.Objects.AM.AMProdEvnt.CreatedByScreenIDTitle : Edm.String "Created Screen"
PX.Objects.AM.AMProdEvnt.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.AM.AMProdEvnt.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdEvnt.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdEvnt.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdEvnt.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdEvnt.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdEvnt.AMBatchByRefDocType -> PX.Objects.AM.AMBatch (RefBatNbr=BatNbr, RefDocType=DocType)
PX.Objects.AM.AMProdEvnt.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdEvnt.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)

# PX.Objects.AM.AMProdItem (EntityType)

Label: "Production Item"
Key: OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdItem, ProductionItem, AMProdItem
Non-filterable, non-selectable: BaseQtyRemaining, QtyRemaining, IsConfigurable, NoteText, TranDate, WIPBalance, BuildProductionBom, Reschedule, LineQtyAvail, LineQtyHardAvail

PX.Objects.AM.AMProdItem.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdItem.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdItem.Function : Edm.Int32 [required] "Function"
PX.Objects.AM.AMProdItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMProdItem.ProdDate : Edm.DateTimeOffset "Order Date"
PX.Objects.AM.AMProdItem.StatusID : Edm.String "Status"
PX.Objects.AM.AMProdItem.QtytoProd : Edm.Decimal [required] "Qty. to Produce"
PX.Objects.AM.AMProdItem.BaseQtytoProd : Edm.Decimal [required] "Base Qty. to Produce"
PX.Objects.AM.AMProdItem.UOM : Edm.String "UOM"
PX.Objects.AM.AMProdItem.QtyComplete : Edm.Decimal [required] "Completed Qty."
PX.Objects.AM.AMProdItem.BaseQtyComplete : Edm.Decimal [required] "Completed Base Qty."
PX.Objects.AM.AMProdItem.BaseQtyRemaining : Edm.Decimal "Remaining Base Qty."
PX.Objects.AM.AMProdItem.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMProdItem.QtyScrapped : Edm.Decimal [required] "Scrapped Qty."
PX.Objects.AM.AMProdItem.BaseQtyScrapped : Edm.Decimal [required]
PX.Objects.AM.AMProdItem.SchedulingMethod : Edm.String "Scheduling Method"
PX.Objects.AM.AMProdItem.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.AMProdItem.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.AMProdItem.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AM.AMProdItem.DueDateDiff : Edm.Int32 "Due Date Diff."
PX.Objects.AM.AMProdItem.ConstDate : Edm.DateTimeOffset "Constraint"
PX.Objects.AM.AMProdItem.Hold : Edm.Boolean [required] "Hold"
PX.Objects.AM.AMProdItem.Released : Edm.Boolean [required] "Released"
PX.Objects.AM.AMProdItem.HasTransactions : Edm.Boolean [required] "HasTransactions"
PX.Objects.AM.AMProdItem.Completed : Edm.Boolean [required] "Completed"
PX.Objects.AM.AMProdItem.Closed : Edm.Boolean [required] "Closed"
PX.Objects.AM.AMProdItem.Canceled : Edm.Boolean [required] "Canceled"
PX.Objects.AM.AMProdItem.IsOpen : Edm.Boolean [required] "IsOpen"
PX.Objects.AM.AMProdItem.FMLTime : Edm.Boolean "Use Fixed Mfg Lead Times for Order Dates"
PX.Objects.AM.AMProdItem.FMLTMRPOrdorOP : Edm.Boolean "Use Order Start Date for MRP"
PX.Objects.AM.AMProdItem.SchPriority : Edm.Int16 [required] "Dispatch Priority"
PX.Objects.AM.AMProdItem.SplitLineCntr : Edm.Int32 [required]
PX.Objects.AM.AMProdItem.DetailSource : Edm.Int32 [required] "Source"
PX.Objects.AM.AMProdItem.IsConfigurable : Edm.Boolean "Is Configurable"
PX.Objects.AM.AMProdItem.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMProdItem.BOMRevisionID : Edm.String "BOM Revision"
PX.Objects.AM.AMProdItem.BOMEffDate : Edm.DateTimeOffset "Source Date"
PX.Objects.AM.AMProdItem.CustomerID : Edm.Int32 "Customer"
PX.Objects.AM.AMProdItem.Descr : Edm.String "Order Description"
PX.Objects.AM.AMProdItem.NoteID : Edm.Guid
PX.Objects.AM.AMProdItem.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMProdItem.OrdLineRef : Edm.Int32 "SO Line Nbr."
PX.Objects.AM.AMProdItem.OrdTypeRef : Edm.String "Sales Order Type"
PX.Objects.AM.AMProdItem.OrdNbr : Edm.String "Sales Order Nbr."
PX.Objects.AM.AMProdItem.ParentOrderType : Edm.String "Parent Order Type"
PX.Objects.AM.AMProdItem.ParentOrdID : Edm.String "Parent Production Nbr."
PX.Objects.AM.AMProdItem.PerClose : Edm.String "Period Closed"
PX.Objects.AM.AMProdItem.PerEnt : Edm.String "Entered Period"
PX.Objects.AM.AMProdItem.ProductOrderType : Edm.String "Product Order Type"
PX.Objects.AM.AMProdItem.ProductOrdID : Edm.String "Product Production Nbr."
PX.Objects.AM.AMProdItem.RelDate : Edm.DateTimeOffset "Release Date"
PX.Objects.AM.AMProdItem.WIPComp : Edm.Decimal [required] "MFG to Inventory"
PX.Objects.AM.AMProdItem.WIPTotal : Edm.Decimal [required] "WIP Total"
PX.Objects.AM.AMProdItem.tstamp : Edm.Binary
PX.Objects.AM.AMProdItem.InvtMult : Edm.Int16 [required]
PX.Objects.AM.AMProdItem.UnassignedQty : Edm.Decimal [required]
PX.Objects.AM.AMProdItem.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMProdItem.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.AM.AMProdItem.WIPBalance : Edm.Decimal "WIP Balance"
PX.Objects.AM.AMProdItem.FirmSchedule : Edm.Boolean [required] "Firm Schedule"
PX.Objects.AM.AMProdItem.CostMethod : Edm.Int32 "Costing Method"
PX.Objects.AM.AMProdItem.LineCntrAttribute : Edm.Int32 [required]
PX.Objects.AM.AMProdItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdItem.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdItem.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdItem.FirstOperationID : Edm.Int32 "First Operation ID"
PX.Objects.AM.AMProdItem.LastOperationID : Edm.Int32 "Last Operation ID"
PX.Objects.AM.AMProdItem.BuildProductionBom : Edm.Boolean
PX.Objects.AM.AMProdItem.Reschedule : Edm.Boolean
PX.Objects.AM.AMProdItem.EstimateRevisionID : Edm.String "Estimate Revision"
PX.Objects.AM.AMProdItem.ProductWorkgroupID : Edm.Int32 "Product Workgroup"
PX.Objects.AM.AMProdItem.ProductManagerID : Edm.Int32 "Product Manager"
PX.Objects.AM.AMProdItem.ScrapOverride : Edm.Boolean [required] "Scrap Override"
PX.Objects.AM.AMProdItem.SourceOrderType : Edm.String "Source Order Type"
PX.Objects.AM.AMProdItem.SourceProductionNbr : Edm.String "Source Production Nbr"
PX.Objects.AM.AMProdItem.ExcludeFromMRP : Edm.Boolean "Exclude from MRP"
PX.Objects.AM.AMProdItem.IsReportPrinted : Edm.Boolean [required] "Report Printed"
PX.Objects.AM.AMProdItem.SupplyType : Edm.Int32 [required] "Supply Type"
PX.Objects.AM.AMProdItem.UpdateProject : Edm.Boolean "Update Project"
PX.Objects.AM.AMProdItem.LineCntrOperation : Edm.Int32 [required] "Operation Line Cntr"
PX.Objects.AM.AMProdItem.LineCntrEvnt : Edm.Int32 [required] "Event Line Cntr"
PX.Objects.AM.AMProdItem.DemandPlanID : Edm.Int64 "Demand Plan ID"
PX.Objects.AM.AMProdItem.Locked : Edm.Boolean [required] "Locked"
PX.Objects.AM.AMProdItem.AutoBackwardReporting : Edm.Boolean [required] "Automatic Backward Reporting"
PX.Objects.AM.AMProdItem.IsProcessMFG : Edm.Boolean [required] "Process Manufacturing"
PX.Objects.AM.AMProdItem.LineQtyAvail : Edm.Decimal
PX.Objects.AM.AMProdItem.LineQtyHardAvail : Edm.Decimal
PX.Objects.AM.AMProdItem.CostCenterID : Edm.Int32 [required]
PX.Objects.AM.AMProdItem.IsOnTimeOverhead : Edm.Boolean [required] "On-Time Overhead"
PX.Objects.AM.AMProdItem.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AM.AMProdItem.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AM.AMProdItem.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AM.AMProdItem.ContactByProductManagerID -> PX.Objects.CR.Contact (ProductManagerID=ContactID)
PX.Objects.AM.AMProdItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMProdItem.AMBomItemByBOMRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, BOMRevisionID=RevisionID)
PX.Objects.AM.AMProdItem.AMBomItemBySubItemID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, InventoryID=InventoryID)
PX.Objects.AM.AMProdItem.AMBomItemByBOMID -> PX.Objects.AM.AMBomItem (BOMRevisionID=RevisionID, BOMID=BOMID)
PX.Objects.AM.AMProdItem.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (FirstOperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdItem.SOOrderByOrdTypeRef -> PX.Objects.SO.SOOrder (OrdNbr=OrderNbr, OrdTypeRef=OrderType)
PX.Objects.AM.AMProdItem.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMProdItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdItem.EPCompanyTreeByProductWorkgroupID -> PX.TM.EPCompanyTree (ProductWorkgroupID=WorkGroupID)
PX.Objects.AM.AMProdItem.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMProdItem.INLocationByScrapSiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMProdItem.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMProdItem.INLocationByScrapLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMProdItem.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMProdItem.INSiteByScrapSiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMProdItem.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMProdItem.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMProdItem.AccountByWIPAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMProdItem.AccountByWIPVarianceAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMProdItem.SubByWIPSubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMProdItem.SubByWIPVarianceSubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMProdItem.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.AM.AMProdItem.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.AM.AMProdItem.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdItem.AMOrderTypeByParentOrderType -> PX.Objects.AM.AMOrderType (ParentOrderType=OrderType)
PX.Objects.AM.AMProdItem.AMOrderTypeByProductOrderType -> PX.Objects.AM.AMOrderType (ProductOrderType=OrderType)
PX.Objects.AM.AMProdItem.AMOrderTypeBySourceOrderType -> PX.Objects.AM.AMOrderType (SourceOrderType=OrderType)
PX.Objects.AM.AMProdItem.AMProdItemByParentOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ParentOrdID, ParentOrderType=OrderType)
PX.Objects.AM.AMProdItem.AMProdItemByProductOrderType -> PX.Objects.AM.AMProdItem (ProductOrdID=ProdOrdID, ProductOrderType=OrderType)
PX.Objects.AM.AMProdItem.AMProdItemBySourceOrderType -> PX.Objects.AM.AMProdItem (SourceProductionNbr=ProdOrdID, SourceOrderType=OrderType)
PX.Objects.AM.AMProdItem.AMEstimateItemByEstimateID -> PX.Objects.AM.AMEstimateItem
PX.Objects.AM.AMProdItem.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.AM.AMProdItem.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.AM.AMProdItem.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.AM.AMProdItem.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMProdItem.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.AMProdItem.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.AM.AMProdItem.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.AM.AMProdItem.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.AM.AMProdItem.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.AM.AMProdItem.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.AM.AMProdItem.AMProdAttributeCollection -> Collection(PX.Objects.AM.AMProdAttribute)
PX.Objects.AM.AMProdItem.AMProdEvntCollection -> Collection(PX.Objects.AM.AMProdEvnt)
PX.Objects.AM.AMProdItem.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.AM.AMProdItem.AMProdMatlLotSerialCollection -> Collection(PX.Objects.AM.AMProdMatlLotSerial)
PX.Objects.AM.AMProdItem.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.AM.AMProdItem.AMProdNumberCollection -> Collection(PX.Objects.AM.AMProdNumber)
PX.Objects.AM.AMProdItem.AMProdOvhdCollection -> Collection(PX.Objects.AM.AMProdOvhd)
PX.Objects.AM.AMProdItem.AMProdStepCollection -> Collection(PX.Objects.AM.AMProdStep)
PX.Objects.AM.AMProdItem.AMProdToolCollection -> Collection(PX.Objects.AM.AMProdTool)
PX.Objects.AM.AMProdItem.AMProdTotalCollection -> Collection(PX.Objects.AM.AMProdTotal)
PX.Objects.AM.AMProdItem.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.AM.AMProdItem.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.Objects.AM.AMProdItem.AMSchdOperDetailCollection -> Collection(PX.Objects.AM.AMSchdOperDetail)
PX.Objects.AM.AMProdItem.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.AM.AMProdItem.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.AM.AMProdItem.AMSFKRecentActivityCollection -> Collection(PX.Objects.AM.SFK.AMSFKRecentActivity)
PX.Objects.AM.AMProdItem.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.Objects.AM.AMProdItem.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)
PX.Objects.AM.AMProdItem.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.AM.AMProdItem.SelectedProdMatlCollection -> Collection(PX.Objects.AM.SelectedProdMatl)
PX.Objects.AM.AMProdItem.SchedulerMachineOperationCollection -> Collection(PX.Objects.AM.SchedulerMachineOperation)
PX.Objects.AM.AMProdItem.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)
PX.Objects.AM.AMProdItem.AMMTranMoveByLotSerialCollection -> Collection(PX.Objects.AM.AMMTranMoveByLotSerial)
PX.Objects.AM.AMProdItem.AMMTranLotSerialNbrAllCollection -> Collection(PX.Objects.AM.AMMTranLotSerialNbrAll)
PX.Objects.AM.AMProdItem.AMProdItemSplitPreassignCollection -> Collection(PX.Objects.AM.AMProdItemSplitPreassign)
PX.Objects.AM.AMProdItem.AMProdItemRelatedCollection -> Collection(PX.Objects.AM.AMProdItemRelated)

# PX.Objects.AM.AMProdItemRelated (EntityType)

Label: "Related Production Item"
Key: OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdItemRelated, RelatedProductionItem, AMProdItemRelated
Non-filterable, non-selectable: RelationType, QtyRemaining

PX.Objects.AM.AMProdItemRelated.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdItemRelated.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdItemRelated.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMProdItemRelated.SiteID : Edm.Int32 "Warehouse"
PX.Objects.AM.AMProdItemRelated.ParentOrderType : Edm.String "Parent Order Type"
PX.Objects.AM.AMProdItemRelated.ParentOrdID : Edm.String "Parent Order"
PX.Objects.AM.AMProdItemRelated.ProductOrderType : Edm.String "Product Order Type"
PX.Objects.AM.AMProdItemRelated.ProductOrdID : Edm.String "Product Order"
PX.Objects.AM.AMProdItemRelated.RelationType : Edm.String "Relationship Type"
PX.Objects.AM.AMProdItemRelated.SupplyType : Edm.Int32
PX.Objects.AM.AMProdItemRelated.StatusID : Edm.String "Status"
PX.Objects.AM.AMProdItemRelated.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.AMProdItemRelated.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.AMProdItemRelated.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AM.AMProdItemRelated.DueDateDiff : Edm.Int32 "Due Date Diff."
PX.Objects.AM.AMProdItemRelated.UOM : Edm.String "UOM"
PX.Objects.AM.AMProdItemRelated.QtytoProd : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.AMProdItemRelated.BaseQtytoProd : Edm.Decimal "Base Qty. to Produce"
PX.Objects.AM.AMProdItemRelated.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMProdItemRelated.QtyComplete : Edm.Decimal "Completed Qty."
PX.Objects.AM.AMProdItemRelated.BaseQtyComplete : Edm.Decimal "Completed Base Qty."
PX.Objects.AM.AMProdItemRelated.QtyScrapped : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.AMProdItemRelated.BaseQtyScrapped : Edm.Decimal
PX.Objects.AM.AMProdItemRelated.Hold : Edm.Boolean
PX.Objects.AM.AMProdItemRelated.Released : Edm.Boolean
PX.Objects.AM.AMProdItemRelated.LineCntrEvnt : Edm.Int32 "Event Line Cntr"
PX.Objects.AM.AMProdItemRelated.DemandPlanID : Edm.Int64
PX.Objects.AM.AMProdItemRelated.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMProdItemRelated.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMProdItemRelated.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMProdItemRelated.INSiteByScrapSiteID -> PX.Objects.IN.INSite

# PX.Objects.AM.AMProdItemSplit (EntityType)

Label: "Production Item Split"
Key: OrderType, ProdOrdID, SplitLineNbr
Entity sets: PX_Objects_AM_AMProdItemSplit, ProductionItemSplit, AMProdItemSplit
Non-filterable, non-selectable: CostSubItemID, CostSiteID, LotSerClassID, AssignedNbr, ProjectID, TaskID, BaseQtyRemaining, QtyRemaining

PX.Objects.AM.AMProdItemSplit.TranType : Edm.String
PX.Objects.AM.AMProdItemSplit.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdItemSplit.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdItemSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.AM.AMProdItemSplit.TranDate : Edm.DateTimeOffset
PX.Objects.AM.AMProdItemSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMProdItemSplit.CostSubItemID : Edm.Int32
PX.Objects.AM.AMProdItemSplit.CostSiteID : Edm.Int32
PX.Objects.AM.AMProdItemSplit.LotSerClassID : Edm.String
PX.Objects.AM.AMProdItemSplit.AssignedNbr : Edm.String
PX.Objects.AM.AMProdItemSplit.InvtMult : Edm.Int16
PX.Objects.AM.AMProdItemSplit.UOM : Edm.String "UOM"
PX.Objects.AM.AMProdItemSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMProdItemSplit.BaseQty : Edm.Decimal
PX.Objects.AM.AMProdItemSplit.PlanID : Edm.Int64 "Plan ID"
PX.Objects.AM.AMProdItemSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdItemSplit.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdItemSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdItemSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdItemSplit.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdItemSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdItemSplit.tstamp : Edm.Binary
PX.Objects.AM.AMProdItemSplit.IsStockItem : Edm.Boolean [required]
PX.Objects.AM.AMProdItemSplit.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.AMProdItemSplit.TaskID : Edm.Int32 "Task"
PX.Objects.AM.AMProdItemSplit.StatusID : Edm.String "Status"
PX.Objects.AM.AMProdItemSplit.IsAllocated : Edm.Boolean [required] "Allocated"
PX.Objects.AM.AMProdItemSplit.QtyComplete : Edm.Decimal [required] "Complete Qty."
PX.Objects.AM.AMProdItemSplit.BaseQtyComplete : Edm.Decimal [required]
PX.Objects.AM.AMProdItemSplit.QtyScrapped : Edm.Decimal [required] "Scrapped Qty."
PX.Objects.AM.AMProdItemSplit.BaseQtyScrapped : Edm.Decimal [required]
PX.Objects.AM.AMProdItemSplit.BaseQtyRemaining : Edm.Decimal "Remaining Base Qty."
PX.Objects.AM.AMProdItemSplit.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMProdItemSplit.IsMaterialLinked : Edm.Boolean [required] "Material Linked"
PX.Objects.AM.AMProdItemSplit.CostCenterID : Edm.Int32 [required]
PX.Objects.AM.AMProdItemSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMProdItemSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.AM.AMProdItemSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdItemSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdItemSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMProdItemSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMProdItemSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMProdItemSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMProdItemSplit.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdItemSplit.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdItemSplit.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.AM.AMProdItemSplit.AMProdItemSplitPreassignCollection -> Collection(PX.Objects.AM.AMProdItemSplitPreassign)

# PX.Objects.AM.AMProdItemSplitPreassign (EntityType)

Label: "Prod Item Split Lot/Serial"
Key: LotSerialNbr, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdItemSplitPreassign, ProdItemSplitLotSerial, AMProdItemSplitPreassign
Non-filterable, non-selectable: QtyRemaining

PX.Objects.AM.AMProdItemSplitPreassign.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdItemSplitPreassign.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdItemSplitPreassign.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.AMProdItemSplitPreassign.SplitLineNbr : Edm.Int32
PX.Objects.AM.AMProdItemSplitPreassign.TranType : Edm.String
PX.Objects.AM.AMProdItemSplitPreassign.TranDate : Edm.DateTimeOffset
PX.Objects.AM.AMProdItemSplitPreassign.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMProdItemSplitPreassign.UOM : Edm.String "UOM"
PX.Objects.AM.AMProdItemSplitPreassign.LocationID : Edm.Int32
PX.Objects.AM.AMProdItemSplitPreassign.Qty : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.AMProdItemSplitPreassign.BaseQty : Edm.Decimal
PX.Objects.AM.AMProdItemSplitPreassign.QtyComplete : Edm.Decimal "Complete Qty."
PX.Objects.AM.AMProdItemSplitPreassign.BaseQtyComplete : Edm.Decimal
PX.Objects.AM.AMProdItemSplitPreassign.QtyScrapped : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.AMProdItemSplitPreassign.BaseQtyScrapped : Edm.Decimal
PX.Objects.AM.AMProdItemSplitPreassign.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMProdItemSplitPreassign.StatusID : Edm.String "Status"
PX.Objects.AM.AMProdItemSplitPreassign.PreassignLotSerial : Edm.Boolean "Allow Preassigning Lot/Serial Numbers"
PX.Objects.AM.AMProdItemSplitPreassign.ParentLotSerialRequired : Edm.String "Require Parent Lot/Serial Number"
PX.Objects.AM.AMProdItemSplitPreassign.Function : Edm.Int32 "Function"
PX.Objects.AM.AMProdItemSplitPreassign.Hold : Edm.Boolean "Hold"
PX.Objects.AM.AMProdItemSplitPreassign.BaseCuryID : Edm.String "BaseCuryID"
PX.Objects.AM.AMProdItemSplitPreassign.Released : Edm.Boolean "Released"
PX.Objects.AM.AMProdItemSplitPreassign.HasTransactions : Edm.Boolean "HasTransactions"
PX.Objects.AM.AMProdItemSplitPreassign.Closed : Edm.Boolean "Closed"
PX.Objects.AM.AMProdItemSplitPreassign.Canceled : Edm.Boolean "Canceled"
PX.Objects.AM.AMProdItemSplitPreassign.Locked : Edm.Boolean "Locked"
PX.Objects.AM.AMProdItemSplitPreassign.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdItemSplitPreassign.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMProdItemSplitPreassign.AMProdItemSplitByProdOrdID -> PX.Objects.AM.AMProdItemSplit (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdItemSplitPreassign.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.AM.AMProdItemSplitPreassign.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)

# PX.Objects.AM.AMProdMatl (EntityType)

Label: "Production Material"
Key: LineID, OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdMatl, ProductionMaterial, AMProdMatl
Non-filterable, non-selectable: BaseOperTotalQty, QtyReqWithScrap, NoteText, LineNbr, IsByproduct, IsFixedMaterial, QtyRemaining, BaseQtyRemaining, PlanCost, UpdateProject, POLinkEnable, ProdLinkEnable, LineQtyAvail, LineQtyHardAvail

PX.Objects.AM.AMProdMatl.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdMatl.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdMatl.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMProdMatl.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMProdMatl.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMProdMatl.Descr : Edm.String "Description"
PX.Objects.AM.AMProdMatl.BaseOperTotalQty : Edm.Decimal "Base Order Qty."
PX.Objects.AM.AMProdMatl.QtyReq : Edm.Decimal [required] "Required Qty."
PX.Objects.AM.AMProdMatl.QtyReqWithScrap : Edm.Decimal "Required Qty. with Scrap"
PX.Objects.AM.AMProdMatl.UOM : Edm.String "UOM"
PX.Objects.AM.AMProdMatl.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMProdMatl.BFlush : Edm.Boolean [required] "Backflush Materials"
PX.Objects.AM.AMProdMatl.CompBOMID : Edm.String "Comp. BOM ID"
PX.Objects.AM.AMProdMatl.CompBOMRevisionID : Edm.String "Comp. BOM Revision"
PX.Objects.AM.AMProdMatl.ScrapFactor : Edm.Decimal [required] "Scrap Factor"
PX.Objects.AM.AMProdMatl.QtyActual : Edm.Decimal [required] "Actual Qty."
PX.Objects.AM.AMProdMatl.TotActCost : Edm.Decimal [required] "Total Actual Cost"
PX.Objects.AM.AMProdMatl.MaterialType : Edm.Int32 "Material Type"
PX.Objects.AM.AMProdMatl.StatusID : Edm.String "Material Status"
PX.Objects.AM.AMProdMatl.BaseQtyActual : Edm.Decimal [required] "Actual Base Qty."
PX.Objects.AM.AMProdMatl.NoteID : Edm.Guid
PX.Objects.AM.AMProdMatl.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMProdMatl.PhtmBOMID : Edm.String "Phantom BOM ID"
PX.Objects.AM.AMProdMatl.PhtmBOMRevisionID : Edm.String "Phantom BOM Revision"
PX.Objects.AM.AMProdMatl.PhtmBOMLineRef : Edm.Int32 "Phantom BOM Ref. Line Nbr."
PX.Objects.AM.AMProdMatl.PhtmBOMOperationID : Edm.Int32 "Phantom Operation ID"
PX.Objects.AM.AMProdMatl.PhtmLevel : Edm.Int32 "Phantom Level"
PX.Objects.AM.AMProdMatl.PhtmMatlBOMID : Edm.String "Phantom Matl BOM ID"
PX.Objects.AM.AMProdMatl.PhtmMatlRevisionID : Edm.String "Phantom Matl Revision"
PX.Objects.AM.AMProdMatl.PhtmMatlLineRef : Edm.Int32 "Phantom Material Line Nbr."
PX.Objects.AM.AMProdMatl.PhtmMatlOperationID : Edm.Int32 "Phantom Material Operation ID"
PX.Objects.AM.AMProdMatl.PhantomRouting : Edm.Int32 "Phantom Routing"
PX.Objects.AM.AMProdMatl.tstamp : Edm.Binary
PX.Objects.AM.AMProdMatl.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdMatl.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdMatl.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatl.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdMatl.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdMatl.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatl.LineNbr : Edm.Int32 "Line Nbr"
PX.Objects.AM.AMProdMatl.SortOrder : Edm.Int32 "Line Order"
PX.Objects.AM.AMProdMatl.QtyRoundUp : Edm.Boolean [required] "Round Qty. Up"
PX.Objects.AM.AMProdMatl.BatchSize : Edm.Decimal [required] "Batch Size"
PX.Objects.AM.AMProdMatl.IsByproduct : Edm.Boolean "By-product"
PX.Objects.AM.AMProdMatl.IsStockItem : Edm.Boolean [required] "Is stock"
PX.Objects.AM.AMProdMatl.IsFixedMaterial : Edm.Boolean "Fixed Material"
PX.Objects.AM.AMProdMatl.TotalQtyRequired : Edm.Decimal [required] "Total Required"
PX.Objects.AM.AMProdMatl.BaseTotalQtyRequired : Edm.Decimal [required] "Base Total Required"
PX.Objects.AM.AMProdMatl.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMProdMatl.BaseQtyRemaining : Edm.Decimal "Remaining Base Qty."
PX.Objects.AM.AMProdMatl.PlanCost : Edm.Decimal "Planned Cost"
PX.Objects.AM.AMProdMatl.SplitLineCntr : Edm.Int32 [required]
PX.Objects.AM.AMProdMatl.WarehouseOverride : Edm.Boolean [required] "Warehouse Override"
PX.Objects.AM.AMProdMatl.UnassignedQty : Edm.Decimal [required]
PX.Objects.AM.AMProdMatl.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMProdMatl.TranDate : Edm.DateTimeOffset "Tran Date"
PX.Objects.AM.AMProdMatl.InvtMult : Edm.Int16 [required]
PX.Objects.AM.AMProdMatl.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.AMProdMatl.TaskID : Edm.Int32 "Task"
PX.Objects.AM.AMProdMatl.UpdateProject : Edm.Boolean
PX.Objects.AM.AMProdMatl.CostCenterID : Edm.Int32
PX.Objects.AM.AMProdMatl.POCreate : Edm.Boolean "Mark for PO"
PX.Objects.AM.AMProdMatl.POLinkEnable : Edm.Boolean
PX.Objects.AM.AMProdMatl.ProdCreate : Edm.Boolean "Mark for Production"
PX.Objects.AM.AMProdMatl.ProdLinkEnable : Edm.Boolean
PX.Objects.AM.AMProdMatl.VendorID : Edm.Int32 "Vendor"
PX.Objects.AM.AMProdMatl.SubcontractSource : Edm.Int32 [required] "Subcontract Source"
PX.Objects.AM.AMProdMatl.LineQtyAvail : Edm.Decimal
PX.Objects.AM.AMProdMatl.LineQtyHardAvail : Edm.Decimal
PX.Objects.AM.AMProdMatl.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AM.AMProdMatl.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMProdMatl.AMBomItemByInventoryID -> PX.Objects.AM.AMBomItem (CompBOMID=BOMID, InventoryID=InventoryID)
PX.Objects.AM.AMProdMatl.AMBomItemByCompBOMID -> PX.Objects.AM.AMBomItem (CompBOMRevisionID=RevisionID, CompBOMID=BOMID)
PX.Objects.AM.AMProdMatl.AMBomItemByCompBOMRevisionID -> PX.Objects.AM.AMBomItem (CompBOMID=BOMID, CompBOMRevisionID=RevisionID)
PX.Objects.AM.AMProdMatl.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMProdMatl.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdMatl.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdMatl.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMProdMatl.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMProdMatl.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMProdMatl.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMProdMatl.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMProdMatl.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdMatl.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdMatl.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.AM.AMProdMatl.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.AMProdMatl.AMProdMatlLotSerialCollection -> Collection(PX.Objects.AM.AMProdMatlLotSerial)
PX.Objects.AM.AMProdMatl.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.AM.AMProdMatl.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)

# PX.Objects.AM.AMProdMatlLotSerial (EntityType)

Label: "Production Material Lot/Serial Nbr."
Key: LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID
Entity sets: PX_Objects_AM_AMProdMatlLotSerial, ProductionMaterialLotSerialNbr, AMProdMatlLotSerial

PX.Objects.AM.AMProdMatlLotSerial.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdMatlLotSerial.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdMatlLotSerial.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMProdMatlLotSerial.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMProdMatlLotSerial.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.AMProdMatlLotSerial.ParentLotSerialNbr : Edm.String [key required] "Parent Lot/Serial Nbr."
PX.Objects.AM.AMProdMatlLotSerial.QtyIssued : Edm.Decimal [required] "Issued Qty."
PX.Objects.AM.AMProdMatlLotSerial.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdMatlLotSerial.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdMatlLotSerial.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatlLotSerial.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdMatlLotSerial.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdMatlLotSerial.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatlLotSerial.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMProdMatlLotSerial.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdMatlLotSerial.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdMatlLotSerial.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdMatlLotSerial.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdMatlLotSerial.AMProdMatlByLineID -> PX.Objects.AM.AMProdMatl (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID, LineID=LineID)

# PX.Objects.AM.AMProdMatlLotSerialAssigned (EntityType)

Label: "Material Lot Serial Assigned"
Key: LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID
Entity sets: PX_Objects_AM_AMProdMatlLotSerialAssigned, MaterialLotSerialAssigned, AMProdMatlLotSerialAssigned
Non-filterable, non-selectable: QtyRequired

PX.Objects.AM.AMProdMatlLotSerialAssigned.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdMatlLotSerialAssigned.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdMatlLotSerialAssigned.OperationID : Edm.Int32 [key]
PX.Objects.AM.AMProdMatlLotSerialAssigned.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMProdMatlLotSerialAssigned.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMProdMatlLotSerialAssigned.Descr : Edm.String "Description"
PX.Objects.AM.AMProdMatlLotSerialAssigned.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.AMProdMatlLotSerialAssigned.ParentLotSerialNbr : Edm.String [key] "Parent Lot/Serial Nbr."
PX.Objects.AM.AMProdMatlLotSerialAssigned.QtyIssued : Edm.Decimal "Allocated Qty."
PX.Objects.AM.AMProdMatlLotSerialAssigned.BaseUnit : Edm.String "UOM"
PX.Objects.AM.AMProdMatlLotSerialAssigned.BatchSize : Edm.Decimal "Batch Size"
PX.Objects.AM.AMProdMatlLotSerialAssigned.QtyReq : Edm.Decimal "Required Qty."
PX.Objects.AM.AMProdMatlLotSerialAssigned.ScrapFactor : Edm.Decimal "Scrap Factor"
PX.Objects.AM.AMProdMatlLotSerialAssigned.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdMatlLotSerialAssigned.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdMatlLotSerialAssigned.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatlLotSerialAssigned.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdMatlLotSerialAssigned.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdMatlLotSerialAssigned.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatlLotSerialAssigned.QtyRequired : Edm.Decimal "Required Qty."

# PX.Objects.AM.AMProdMatlLotSerialUnassigned (EntityType)

Label: "Material Lot Serial Unassigned"
Key: LineID, LotSerialNbr, OperationID, OrderType, ParentLotSerialNbr, ProdOrdID
Entity sets: PX_Objects_AM_AMProdMatlLotSerialUnassigned, MaterialLotSerialUnassigned, AMProdMatlLotSerialUnassigned
Non-filterable, non-selectable: QtyRequired, QtyToAllocate

PX.Objects.AM.AMProdMatlLotSerialUnassigned.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdMatlLotSerialUnassigned.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdMatlLotSerialUnassigned.OperationID : Edm.Int32 [key]
PX.Objects.AM.AMProdMatlLotSerialUnassigned.LineID : Edm.Int32 [key]
PX.Objects.AM.AMProdMatlLotSerialUnassigned.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMProdMatlLotSerialUnassigned.Descr : Edm.String "Description"
PX.Objects.AM.AMProdMatlLotSerialUnassigned.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.AMProdMatlLotSerialUnassigned.ParentLotSerialNbr : Edm.String [key] "Parent Lot/Serial Nbr."
PX.Objects.AM.AMProdMatlLotSerialUnassigned.QtyIssued : Edm.Decimal "Unallocated Qty."
PX.Objects.AM.AMProdMatlLotSerialUnassigned.BaseUnit : Edm.String "UOM"
PX.Objects.AM.AMProdMatlLotSerialUnassigned.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdMatlLotSerialUnassigned.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdMatlLotSerialUnassigned.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatlLotSerialUnassigned.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdMatlLotSerialUnassigned.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdMatlLotSerialUnassigned.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatlLotSerialUnassigned.BatchSize : Edm.Decimal "Batch Size"
PX.Objects.AM.AMProdMatlLotSerialUnassigned.QtyReq : Edm.Decimal "Required Qty."
PX.Objects.AM.AMProdMatlLotSerialUnassigned.ScrapFactor : Edm.Decimal "Scrap Factor"
PX.Objects.AM.AMProdMatlLotSerialUnassigned.QtyRequired : Edm.Decimal "Required Qty."
PX.Objects.AM.AMProdMatlLotSerialUnassigned.QtyToAllocate : Edm.Decimal "Qty. to Allocate"

# PX.Objects.AM.AMProdMatlSplit (EntityType)

Label: "Production Material Split"
Key: LineID, OperationID, OrderType, ProdOrdID, SplitLineNbr
Entity sets: PX_Objects_AM_AMProdMatlSplit, ProductionMaterialSplit, AMProdMatlSplit
Non-filterable, non-selectable: AssignedNbr, LotSerClassID, ProjectID, TaskID, CostSubItemID, CostSiteID

PX.Objects.AM.AMProdMatlSplit.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdMatlSplit.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdMatlSplit.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMProdMatlSplit.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMProdMatlSplit.SplitLineNbr : Edm.Int32 [key] "Allocation ID"
PX.Objects.AM.AMProdMatlSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMProdMatlSplit.UOM : Edm.String "UOM"
PX.Objects.AM.AMProdMatlSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMProdMatlSplit.BaseQty : Edm.Decimal
PX.Objects.AM.AMProdMatlSplit.PlanID : Edm.Int64 "Plan ID"
PX.Objects.AM.AMProdMatlSplit.AssignedNbr : Edm.String
PX.Objects.AM.AMProdMatlSplit.LotSerClassID : Edm.String
PX.Objects.AM.AMProdMatlSplit.IsStockItem : Edm.Boolean "Stock Item"
PX.Objects.AM.AMProdMatlSplit.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMProdMatlSplit.TranDate : Edm.DateTimeOffset "Allocation Date"
PX.Objects.AM.AMProdMatlSplit.InvtMult : Edm.Int16 [required]
PX.Objects.AM.AMProdMatlSplit.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.AMProdMatlSplit.TaskID : Edm.Int32 "Task"
PX.Objects.AM.AMProdMatlSplit.IsAllocated : Edm.Boolean [required] "Allocated"
PX.Objects.AM.AMProdMatlSplit.CostSubItemID : Edm.Int32
PX.Objects.AM.AMProdMatlSplit.CostSiteID : Edm.Int32
PX.Objects.AM.AMProdMatlSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdMatlSplit.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdMatlSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatlSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdMatlSplit.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdMatlSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdMatlSplit.tstamp : Edm.Binary
PX.Objects.AM.AMProdMatlSplit.QtyComplete : Edm.Decimal "Completed Qty."
PX.Objects.AM.AMProdMatlSplit.BaseQtyComplete : Edm.Decimal
PX.Objects.AM.AMProdMatlSplit.Completed : Edm.Boolean "Completed"
PX.Objects.AM.AMProdMatlSplit.ParentSplitLineNbr : Edm.Int32 "Parent Allocation ID"
PX.Objects.AM.AMProdMatlSplit.RefNoteID : Edm.Guid "Related Document"
PX.Objects.AM.AMProdMatlSplit.QtyReceived : Edm.Decimal "Received Qty."
PX.Objects.AM.AMProdMatlSplit.BaseQtyReceived : Edm.Decimal
PX.Objects.AM.AMProdMatlSplit.POCreate : Edm.Boolean "Mark for PO"
PX.Objects.AM.AMProdMatlSplit.POCompleted : Edm.Boolean
PX.Objects.AM.AMProdMatlSplit.POCancelled : Edm.Boolean
PX.Objects.AM.AMProdMatlSplit.POOrderType : Edm.String "PO Type"
PX.Objects.AM.AMProdMatlSplit.POOrderNbr : Edm.String "PO Order Nbr."
PX.Objects.AM.AMProdMatlSplit.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.AM.AMProdMatlSplit.POReceiptType : Edm.String "PO Receipt Type"
PX.Objects.AM.AMProdMatlSplit.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.AM.AMProdMatlSplit.AMOrderType : Edm.String "Sub. Assy. Order Type"
PX.Objects.AM.AMProdMatlSplit.AMProdOrdID : Edm.String "Sub. Assy. Production Nbr."
PX.Objects.AM.AMProdMatlSplit.ProdCreate : Edm.Boolean "Mark for Production"
PX.Objects.AM.AMProdMatlSplit.AMDocType : Edm.String "AM Document Type"
PX.Objects.AM.AMProdMatlSplit.AMBatNbr : Edm.String "AM Batch Nbr"
PX.Objects.AM.AMProdMatlSplit.VendorID : Edm.Int32
PX.Objects.AM.AMProdMatlSplit.CostCenterID : Edm.Int32
PX.Objects.AM.AMProdMatlSplit.POOrderByPOOrderType -> PX.Objects.PO.POOrder (POOrderNbr=OrderNbr, POOrderType=OrderType)
PX.Objects.AM.AMProdMatlSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMProdMatlSplit.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMProdMatlSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.AM.AMProdMatlSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdMatlSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdMatlSplit.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.AM.AMProdMatlSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMProdMatlSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMProdMatlSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMProdMatlSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMProdMatlSplit.AMBatchByAMDocType -> PX.Objects.AM.AMBatch (AMBatNbr=BatNbr, AMDocType=DocType)
PX.Objects.AM.AMProdMatlSplit.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdMatlSplit.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdMatlSplit.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMProdMatlSplit.AMProdMatlByLineID -> PX.Objects.AM.AMProdMatl (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID, LineID=LineID)
PX.Objects.AM.AMProdMatlSplit.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)

# PX.Objects.AM.AMProdNumber (EntityType)

Label: "Production Number"
Key: OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdNumber, ProductionNumber, AMProdNumber

PX.Objects.AM.AMProdNumber.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdNumber.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdNumber.ChildOrderCntr : Edm.Int32
PX.Objects.AM.AMProdNumber.tstamp : Edm.Binary
PX.Objects.AM.AMProdNumber.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdNumber.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdNumber.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdNumber.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdNumber.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdNumber.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdNumber.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdNumber.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdNumber.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdNumber.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdNumber.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)

# PX.Objects.AM.AMProdOper (EntityType)

Label: "Production Operation"
Key: OperationCD, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdOper, ProductionOperation, AMProdOper
Non-filterable, non-selectable: QtyRemaining, BaseQtyRemaining, NoteText, PlanTotal, WIPTotal, HasActualCost, VarianceLabor, VarianceLaborTime, VarianceMachine, VarianceMaterial, VarianceTool, VarianceFixedOverhead, VarianceVariableOverhead, VarianceSubcontract, VarianceTotal, WIPBalance, ActualLaborTimeRaw, ActualMachineTimeRaw, PlanLaborTimeRaw, PlanMachineTimeRaw, VarianceLaborTimeRaw, SetupTimeRaw, RunUnitTimeRaw, MachineUnitTimeRaw, QueueTimeRaw, FinishTimeRaw, MoveTimeRaw, ShipRemainingQty, BaseShipRemainingQty, AtVendorQuantity, BaseAtVendorQuantity

PX.Objects.AM.AMProdOper.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdOper.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdOper.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMProdOper.OperationCD : Edm.String [key] "Operation ID"
PX.Objects.AM.AMProdOper.Descr : Edm.String "Operation Description"
PX.Objects.AM.AMProdOper.WcID : Edm.String "Work Center"
PX.Objects.AM.AMProdOper.SetupTime : Edm.Int32 [required] "Setup Time"
PX.Objects.AM.AMProdOper.RunUnitTime : Edm.Int32 [required] "Run Time"
PX.Objects.AM.AMProdOper.RunUnits : Edm.Decimal [required] "Run Units"
PX.Objects.AM.AMProdOper.MachineUnitTime : Edm.Int32 [required] "Machine Time"
PX.Objects.AM.AMProdOper.MachineUnits : Edm.Decimal [required] "Machine Units"
PX.Objects.AM.AMProdOper.QueueTime : Edm.Int32 [required] "Queue Time"
PX.Objects.AM.AMProdOper.FinishTime : Edm.Int32 [required] "Finish Time"
PX.Objects.AM.AMProdOper.MoveTime : Edm.Int32 [required] "Move Time"
PX.Objects.AM.AMProdOper.StatusID : Edm.String "Status"
PX.Objects.AM.AMProdOper.BFlush : Edm.Boolean [required] "Backflush Labor"
PX.Objects.AM.AMProdOper.QtytoProd : Edm.Decimal [required] "Qty. to Produce"
PX.Objects.AM.AMProdOper.BaseQtytoProd : Edm.Decimal [required] "Base Qty. to Produce"
PX.Objects.AM.AMProdOper.QtyComplete : Edm.Decimal [required] "Completed Qty."
PX.Objects.AM.AMProdOper.BaseQtyComplete : Edm.Decimal [required] "Completed Base Qty."
PX.Objects.AM.AMProdOper.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMProdOper.BaseQtyRemaining : Edm.Decimal "Remaining Base Qty."
PX.Objects.AM.AMProdOper.QtyScrapped : Edm.Decimal [required] "Scrapped Qty."
PX.Objects.AM.AMProdOper.BaseQtyScrapped : Edm.Decimal [required] "Scrapped Base Qty."
PX.Objects.AM.AMProdOper.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.AMProdOper.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.AMProdOper.ActEndDate : Edm.DateTimeOffset "Actual End Date"
PX.Objects.AM.AMProdOper.LineCntrMatl : Edm.Int32 [required]
PX.Objects.AM.AMProdOper.LineCntrOvhd : Edm.Int32 [required]
PX.Objects.AM.AMProdOper.LineCntrStep : Edm.Int32 [required]
PX.Objects.AM.AMProdOper.LineCntrTool : Edm.Int32 [required]
PX.Objects.AM.AMProdOper.ActStartDate : Edm.DateTimeOffset "Actual Start Date"
PX.Objects.AM.AMProdOper.NoteID : Edm.Guid
PX.Objects.AM.AMProdOper.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMProdOper.PhtmBOMID : Edm.String "Phantom BOM ID"
PX.Objects.AM.AMProdOper.PhtmBOMRevisionID : Edm.String "Phantom BOM Revision"
PX.Objects.AM.AMProdOper.PhtmBOMLineRef : Edm.Int32 "Phantom BOM Ref. Line Nbr."
PX.Objects.AM.AMProdOper.PhtmBOMOperationID : Edm.Int32 "Phantom Operation ID"
PX.Objects.AM.AMProdOper.PhtmLevel : Edm.Int32 "Phantom Level"
PX.Objects.AM.AMProdOper.PhtmMatlBOMID : Edm.String "Phantom Material BOM ID"
PX.Objects.AM.AMProdOper.PhtmMatlRevisionID : Edm.String "Phantom Material Revision"
PX.Objects.AM.AMProdOper.PhtmMatlLineRef : Edm.Int32 "Phantom Material Line Nbr."
PX.Objects.AM.AMProdOper.PhtmMatlOperationID : Edm.Int32 "Phantom Material Operation ID"
PX.Objects.AM.AMProdOper.PhtmPriorLevelQty : Edm.Decimal "Phantom Prior Level Qty."
PX.Objects.AM.AMProdOper.FirmSchedule : Edm.Boolean [required] "Firm Schedule"
PX.Objects.AM.AMProdOper.ControlPoint : Edm.Boolean "Control Point"
PX.Objects.AM.AMProdOper.PlanLabor : Edm.Decimal [required] "Labor"
PX.Objects.AM.AMProdOper.PlanLaborTime : Edm.Int32 [required] "Labor Time"
PX.Objects.AM.AMProdOper.PlanMachine : Edm.Decimal [required] "Machine"
PX.Objects.AM.AMProdOper.PlanMachineTime : Edm.Int32 [required] "Plan Machine Time"
PX.Objects.AM.AMProdOper.PlanMaterial : Edm.Decimal [required] "Material"
PX.Objects.AM.AMProdOper.PlanTool : Edm.Decimal [required] "Tool"
PX.Objects.AM.AMProdOper.PlanFixedOverhead : Edm.Decimal [required] "Fixed Overhead"
PX.Objects.AM.AMProdOper.PlanVariableOverhead : Edm.Decimal [required] "Variable Overhead"
PX.Objects.AM.AMProdOper.PlanSubcontract : Edm.Decimal [required] "Subcontract"
PX.Objects.AM.AMProdOper.PlanQtyToProduce : Edm.Decimal [required] "Plan Qty."
PX.Objects.AM.AMProdOper.PlanTotal : Edm.Decimal "Planned Total"
PX.Objects.AM.AMProdOper.PlanCostDate : Edm.DateTimeOffset "Plan Cost Date"
PX.Objects.AM.AMProdOper.PlanReferenceMaterial : Edm.Decimal [required] "Ref. Material"
PX.Objects.AM.AMProdOper.ActualLabor : Edm.Decimal [required] "Labor"
PX.Objects.AM.AMProdOper.ActualLaborTime : Edm.Int32 [required] "Labor Time"
PX.Objects.AM.AMProdOper.ActualMachine : Edm.Decimal [required] "Machine"
PX.Objects.AM.AMProdOper.ActualMachineTime : Edm.Int32 [required] "Actual Machine Time"
PX.Objects.AM.AMProdOper.ActualMaterial : Edm.Decimal [required] "Material"
PX.Objects.AM.AMProdOper.ActualTool : Edm.Decimal [required] "Tool"
PX.Objects.AM.AMProdOper.ActualFixedOverhead : Edm.Decimal [required] "Fixed Overhead"
PX.Objects.AM.AMProdOper.ActualVariableOverhead : Edm.Decimal [required] "Variable Overhead"
PX.Objects.AM.AMProdOper.ActualSubcontract : Edm.Decimal [required] "Subcontract"
PX.Objects.AM.AMProdOper.ScrapAmount : Edm.Decimal [required] "Scrap"
PX.Objects.AM.AMProdOper.WIPAdjustment : Edm.Decimal [required] "Adjustments"
PX.Objects.AM.AMProdOper.WIPTotal : Edm.Decimal "WIP Total"
PX.Objects.AM.AMProdOper.WIPComp : Edm.Decimal [required] "MFG to Inventory"
PX.Objects.AM.AMProdOper.HasActualCost : Edm.Boolean "Has Actual cost"
PX.Objects.AM.AMProdOper.VarianceLabor : Edm.Decimal "Labor"
PX.Objects.AM.AMProdOper.VarianceLaborTime : Edm.Int32 "Labor Time"
PX.Objects.AM.AMProdOper.VarianceMachine : Edm.Decimal "Machine"
PX.Objects.AM.AMProdOper.VarianceMaterial : Edm.Decimal "Material"
PX.Objects.AM.AMProdOper.VarianceTool : Edm.Decimal "Tool"
PX.Objects.AM.AMProdOper.VarianceFixedOverhead : Edm.Decimal "Fixed Overhead"
PX.Objects.AM.AMProdOper.VarianceVariableOverhead : Edm.Decimal "Variable Overhead"
PX.Objects.AM.AMProdOper.VarianceSubcontract : Edm.Decimal "Subcontract"
PX.Objects.AM.AMProdOper.VarianceTotal : Edm.Decimal "Total Variance"
PX.Objects.AM.AMProdOper.WIPBalance : Edm.Decimal "WIP Balance"
PX.Objects.AM.AMProdOper.tstamp : Edm.Binary
PX.Objects.AM.AMProdOper.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdOper.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdOper.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdOper.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdOper.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdOper.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdOper.TotalQty : Edm.Decimal [required] "Total Qty."
PX.Objects.AM.AMProdOper.BaseTotalQty : Edm.Decimal [required] "Base Total Qty."
PX.Objects.AM.AMProdOper.ScrapAction : Edm.Int32 [required] "Scrap Action"
PX.Objects.AM.AMProdOper.ActualLaborTimeRaw : Edm.Int32 "ActualLaborTimeRaw"
PX.Objects.AM.AMProdOper.ActualMachineTimeRaw : Edm.Int32 "ActualMachineTimeRaw"
PX.Objects.AM.AMProdOper.PlanLaborTimeRaw : Edm.Int32 "PlanLaborTimeRaw"
PX.Objects.AM.AMProdOper.PlanMachineTimeRaw : Edm.Int32 "PlanMachineTimeRaw"
PX.Objects.AM.AMProdOper.VarianceLaborTimeRaw : Edm.Int32 "VarianceLaborTimeRaw"
PX.Objects.AM.AMProdOper.SetupTimeRaw : Edm.Int32 "SetupTimeRaw"
PX.Objects.AM.AMProdOper.RunUnitTimeRaw : Edm.Int32 "RunUnitTimeRaw"
PX.Objects.AM.AMProdOper.MachineUnitTimeRaw : Edm.Int32 "MachineUnitTimeRaw"
PX.Objects.AM.AMProdOper.QueueTimeRaw : Edm.Int32 "QueueTimeRaw"
PX.Objects.AM.AMProdOper.FinishTimeRaw : Edm.Int32 "FinishTimeRaw"
PX.Objects.AM.AMProdOper.MoveTimeRaw : Edm.Int32 "MoveTimeRaw"
PX.Objects.AM.AMProdOper.OutsideProcess : Edm.Boolean [required] "Outside Process"
PX.Objects.AM.AMProdOper.DropShippedToVendor : Edm.Boolean [required] "Drop Shipped to Vendor"
PX.Objects.AM.AMProdOper.VendorID : Edm.Int32 "Vendor"
PX.Objects.AM.AMProdOper.POOrderNbr : Edm.String "PO Order Nbr."
PX.Objects.AM.AMProdOper.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.AM.AMProdOper.ShippedQuantity : Edm.Decimal [required] "Shipped Quantity"
PX.Objects.AM.AMProdOper.BaseShippedQuantity : Edm.Decimal [required] "Base Shipped Quantity"
PX.Objects.AM.AMProdOper.ShipRemainingQty : Edm.Decimal "Ship Remaining Qty."
PX.Objects.AM.AMProdOper.BaseShipRemainingQty : Edm.Decimal "Base Ship Remaining Qty."
PX.Objects.AM.AMProdOper.AtVendorQuantity : Edm.Decimal "At Vendor Quantity"
PX.Objects.AM.AMProdOper.BaseAtVendorQuantity : Edm.Decimal "Base At Vendor Quantity"
PX.Objects.AM.AMProdOper.BaseMaterialQty : Edm.Decimal [required] "Base Total Qty."
PX.Objects.AM.AMProdOper.AutoReportQty : Edm.Boolean "Auto-Report Qty."
PX.Objects.AM.AMProdOper.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AM.AMProdOper.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdOper.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdOper.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.AM.AMProdOper.LocationByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.AM.AMProdOper.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdOper.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdOper.AMProdTotalByProdOrdID -> PX.Objects.AM.AMProdTotal (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdOper.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)
PX.Objects.AM.AMProdOper.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.AM.AMProdOper.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.AM.AMProdOper.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMProdOper.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.AMProdOper.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.AM.AMProdOper.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.AM.AMProdOper.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.AM.AMProdOper.AMProdAttributeCollection -> Collection(PX.Objects.AM.AMProdAttribute)
PX.Objects.AM.AMProdOper.AMProdMatlLotSerialCollection -> Collection(PX.Objects.AM.AMProdMatlLotSerial)
PX.Objects.AM.AMProdOper.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.AM.AMProdOper.AMProdOvhdCollection -> Collection(PX.Objects.AM.AMProdOvhd)
PX.Objects.AM.AMProdOper.AMProdStepCollection -> Collection(PX.Objects.AM.AMProdStep)
PX.Objects.AM.AMProdOper.AMProdToolCollection -> Collection(PX.Objects.AM.AMProdTool)
PX.Objects.AM.AMProdOper.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.Objects.AM.AMProdOper.AMSchdOperDetailCollection -> Collection(PX.Objects.AM.AMSchdOperDetail)
PX.Objects.AM.AMProdOper.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.AM.AMProdOper.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.AM.AMProdOper.AMSFKRecentActivityCollection -> Collection(PX.Objects.AM.SFK.AMSFKRecentActivity)
PX.Objects.AM.AMProdOper.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.AM.AMProdOper.SelectedProdMatlCollection -> Collection(PX.Objects.AM.SelectedProdMatl)
PX.Objects.AM.AMProdOper.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)

# PX.Objects.AM.AMProdOvhd (EntityType)

Label: "Production Overhead"
Key: LineID, OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdOvhd, ProductionOverhead, AMProdOvhd
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMProdOvhd.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdOvhd.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdOvhd.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMProdOvhd.LineID : Edm.Int32 [key] "Line ID"
PX.Objects.AM.AMProdOvhd.OvhdID : Edm.String "Overhead ID"
PX.Objects.AM.AMProdOvhd.OFactor : Edm.Decimal [required] "Factor"
PX.Objects.AM.AMProdOvhd.TotActCost : Edm.Decimal [required] "Total Actual Cost"
PX.Objects.AM.AMProdOvhd.NoteID : Edm.Guid
PX.Objects.AM.AMProdOvhd.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMProdOvhd.PhtmBOMID : Edm.String "Phantom BOM ID"
PX.Objects.AM.AMProdOvhd.PhtmBOMRevisionID : Edm.String "Phantom BOM Revision"
PX.Objects.AM.AMProdOvhd.PhtmBOMLineRef : Edm.Int32 "Phantom BOM Ref. Line Nbr."
PX.Objects.AM.AMProdOvhd.PhtmBOMOperationID : Edm.Int32 "Phantom Operation ID"
PX.Objects.AM.AMProdOvhd.PhtmLevel : Edm.Int32 "Phantom Level"
PX.Objects.AM.AMProdOvhd.PhtmMatlBOMID : Edm.String "Phantom Material BOM ID"
PX.Objects.AM.AMProdOvhd.PhtmMatlRevisionID : Edm.String "Phantom Material Revision"
PX.Objects.AM.AMProdOvhd.PhtmMatlLineRef : Edm.Int32 "Phantom Material Line Nbr."
PX.Objects.AM.AMProdOvhd.PhtmMatlOperationID : Edm.Int32 "Phantom Material Operation ID"
PX.Objects.AM.AMProdOvhd.WCFlag : Edm.Boolean [required] "WC Flag"
PX.Objects.AM.AMProdOvhd.tstamp : Edm.Binary
PX.Objects.AM.AMProdOvhd.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdOvhd.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdOvhd.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdOvhd.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdOvhd.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdOvhd.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdOvhd.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMProdOvhd.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdOvhd.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdOvhd.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdOvhd.AMOverheadByOvhdID -> PX.Objects.AM.AMOverhead (OvhdID=OvhdID)
PX.Objects.AM.AMProdOvhd.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)

# PX.Objects.AM.AMProdStep (EntityType)

Label: "Production Step"
Key: LineID, OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdStep, ProductionStep, AMProdStep
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMProdStep.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdStep.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdStep.Descr : Edm.String "Description"
PX.Objects.AM.AMProdStep.LineID : Edm.Int32 [key] "LineID"
PX.Objects.AM.AMProdStep.NoteID : Edm.Guid
PX.Objects.AM.AMProdStep.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMProdStep.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMProdStep.PhtmBOMID : Edm.String "Phantom BOM ID"
PX.Objects.AM.AMProdStep.PhtmBOMRevisionID : Edm.String "Phantom BOM Revision"
PX.Objects.AM.AMProdStep.PhtmBOMLineRef : Edm.Int32 "Phantom BOM Ref. Line Nbr."
PX.Objects.AM.AMProdStep.PhtmBOMOperationID : Edm.Int32 "Phantom Operation ID"
PX.Objects.AM.AMProdStep.PhtmLevel : Edm.Int32 "Phantom Level"
PX.Objects.AM.AMProdStep.PhtmMatlBOMID : Edm.String "Phantom Material BOM ID"
PX.Objects.AM.AMProdStep.PhtmMatlRevisionID : Edm.String "Phantom Material Revision"
PX.Objects.AM.AMProdStep.PhtmMatlLineRef : Edm.Int32 "Phantom Material Line Nbr."
PX.Objects.AM.AMProdStep.PhtmMatlOperationID : Edm.Int32 "Phantom Material Operation ID"
PX.Objects.AM.AMProdStep.tstamp : Edm.Binary
PX.Objects.AM.AMProdStep.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdStep.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdStep.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdStep.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdStep.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdStep.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdStep.SortOrder : Edm.Int32 "Line Order"
PX.Objects.AM.AMProdStep.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMProdStep.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdStep.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdStep.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdStep.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)

# PX.Objects.AM.AMProdTool (EntityType)

Label: "Production Tool"
Key: LineID, OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdTool, ProductionTool, AMProdTool
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMProdTool.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdTool.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdTool.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMProdTool.LineID : Edm.Int32 [key] "LineID"
PX.Objects.AM.AMProdTool.ToolID : Edm.String "Tool ID"
PX.Objects.AM.AMProdTool.Descr : Edm.String "Description"
PX.Objects.AM.AMProdTool.QtyReq : Edm.Decimal [required] "Required Qty."
PX.Objects.AM.AMProdTool.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMProdTool.TotActCost : Edm.Decimal [required] "Total Actual Cost"
PX.Objects.AM.AMProdTool.NoteID : Edm.Guid
PX.Objects.AM.AMProdTool.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMProdTool.PhtmBOMID : Edm.String "Phantom BOM ID"
PX.Objects.AM.AMProdTool.PhtmBOMRevisionID : Edm.String "Phantom BOM Revision"
PX.Objects.AM.AMProdTool.PhtmBOMLineRef : Edm.Int32 "Phantom BOM Ref. Line Nbr."
PX.Objects.AM.AMProdTool.PhtmBOMOperationID : Edm.Int32 "Phantom Operation ID"
PX.Objects.AM.AMProdTool.PhtmLevel : Edm.Int32 "Phantom Level"
PX.Objects.AM.AMProdTool.PhtmMatlBOMID : Edm.String "Phantom Material BOM ID"
PX.Objects.AM.AMProdTool.PhtmMatlRevisionID : Edm.String "Phantom Material Revision"
PX.Objects.AM.AMProdTool.PhtmMatlLineRef : Edm.Int32 "Phantom Material Line Nbr."
PX.Objects.AM.AMProdTool.PhtmMatlOperationID : Edm.Int32 "Phantom Material Operation ID"
PX.Objects.AM.AMProdTool.TotActUses : Edm.Decimal [required] "Total Actual Uses"
PX.Objects.AM.AMProdTool.tstamp : Edm.Binary
PX.Objects.AM.AMProdTool.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdTool.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdTool.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdTool.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdTool.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdTool.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdTool.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMProdTool.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdTool.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdTool.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdTool.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdTool.AMToolMstByToolID -> PX.Objects.AM.AMToolMst (ToolID=ToolID)

# PX.Objects.AM.AMProdTotal (EntityType)

Label: "Production Totals"
Key: OrderType, ProdOrdID
Entity sets: PX_Objects_AM_AMProdTotal, ProductionTotals, AMProdTotal
Non-filterable, non-selectable: PlanTotal, PlanUnitCost, QtyComplete, WIPTotal, WIPComp, VarianceLabor, VarianceLaborTime, VarianceMachine, VarianceMaterial, VarianceTool, VarianceFixedOverhead, VarianceVariableOverhead, VarianceSubcontract, QtyRemaining, VarianceTotal, WIPBalance, NoteText, ActualLaborTimeRaw, PlanLaborTimeRaw, VarianceLaborTimeRaw

PX.Objects.AM.AMProdTotal.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMProdTotal.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMProdTotal.PlanLabor : Edm.Decimal [required] "Labor"
PX.Objects.AM.AMProdTotal.PlanLaborTime : Edm.Int32 [required] "Labor Time"
PX.Objects.AM.AMProdTotal.PlanMachine : Edm.Decimal [required] "Machine"
PX.Objects.AM.AMProdTotal.PlanMaterial : Edm.Decimal [required] "Material"
PX.Objects.AM.AMProdTotal.PlanTool : Edm.Decimal [required] "Tool"
PX.Objects.AM.AMProdTotal.PlanFixedOverhead : Edm.Decimal [required] "Fixed Overhead"
PX.Objects.AM.AMProdTotal.PlanVariableOverhead : Edm.Decimal [required] "Variable Overhead"
PX.Objects.AM.AMProdTotal.PlanSubcontract : Edm.Decimal [required] "Subcontract"
PX.Objects.AM.AMProdTotal.PlanQtyToProduce : Edm.Decimal [required] "Qty. to Produce"
PX.Objects.AM.AMProdTotal.PlanTotal : Edm.Decimal "Plan Total"
PX.Objects.AM.AMProdTotal.PlanUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.AMProdTotal.PlanCostDate : Edm.DateTimeOffset "Plan Cost Date"
PX.Objects.AM.AMProdTotal.PlanReferenceMaterial : Edm.Decimal [required] "Ref. Material"
PX.Objects.AM.AMProdTotal.ActualLabor : Edm.Decimal [required] "Labor"
PX.Objects.AM.AMProdTotal.ActualLaborTime : Edm.Int32 [required] "Labor Time"
PX.Objects.AM.AMProdTotal.ActualMachine : Edm.Decimal [required] "Machine"
PX.Objects.AM.AMProdTotal.ActualMaterial : Edm.Decimal [required] "Material"
PX.Objects.AM.AMProdTotal.ActualTool : Edm.Decimal [required] "Tool"
PX.Objects.AM.AMProdTotal.ActualFixedOverhead : Edm.Decimal [required] "Fixed Overhead"
PX.Objects.AM.AMProdTotal.ActualVariableOverhead : Edm.Decimal [required] "Variable Overhead"
PX.Objects.AM.AMProdTotal.ActualSubcontract : Edm.Decimal [required] "Subcontract"
PX.Objects.AM.AMProdTotal.WIPAdjustment : Edm.Decimal [required] "Adjustments"
PX.Objects.AM.AMProdTotal.QtyComplete : Edm.Decimal "Completed Qty."
PX.Objects.AM.AMProdTotal.WIPTotal : Edm.Decimal "WIP Total"
PX.Objects.AM.AMProdTotal.WIPComp : Edm.Decimal "MFG to Inventory"
PX.Objects.AM.AMProdTotal.VarianceLabor : Edm.Decimal "Labor"
PX.Objects.AM.AMProdTotal.VarianceLaborTime : Edm.Int32 "Labor Time"
PX.Objects.AM.AMProdTotal.VarianceMachine : Edm.Decimal "Machine"
PX.Objects.AM.AMProdTotal.VarianceMaterial : Edm.Decimal "Material"
PX.Objects.AM.AMProdTotal.VarianceTool : Edm.Decimal "Tool"
PX.Objects.AM.AMProdTotal.VarianceFixedOverhead : Edm.Decimal "Fixed Overhead"
PX.Objects.AM.AMProdTotal.VarianceVariableOverhead : Edm.Decimal "Variable Overhead"
PX.Objects.AM.AMProdTotal.VarianceSubcontract : Edm.Decimal "Subcontract"
PX.Objects.AM.AMProdTotal.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMProdTotal.VarianceTotal : Edm.Decimal "Total Variance"
PX.Objects.AM.AMProdTotal.WIPBalance : Edm.Decimal "WIP Balance"
PX.Objects.AM.AMProdTotal.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMProdTotal.CreatedByScreenID : Edm.String
PX.Objects.AM.AMProdTotal.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdTotal.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMProdTotal.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMProdTotal.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMProdTotal.tstamp : Edm.Binary
PX.Objects.AM.AMProdTotal.NoteID : Edm.Guid
PX.Objects.AM.AMProdTotal.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMProdTotal.ScrapAmount : Edm.Decimal [required] "Scrap"
PX.Objects.AM.AMProdTotal.ActualLaborTimeRaw : Edm.Int32 "ActualLaborTimeRaw"
PX.Objects.AM.AMProdTotal.PlanLaborTimeRaw : Edm.Int32 "PlanLaborTimeRaw"
PX.Objects.AM.AMProdTotal.VarianceLaborTimeRaw : Edm.Int32 "VarianceLaborTimeRaw"
PX.Objects.AM.AMProdTotal.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMProdTotal.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMProdTotal.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMProdTotal.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMProdTotal.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMProdTotal.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)

# PX.Objects.AM.AMPSetup (EntityType)

Label: "Production Preferences"
Singletons: PX_Objects_AM_AMPSetup, ProductionPreferences, AMPSetup

PX.Objects.AM.AMPSetup.MoveNumberingID : Edm.String "Move Numbering Sequence"
PX.Objects.AM.AMPSetup.LaborNumberingID : Edm.String "Labor Numbering Sequence"
PX.Objects.AM.AMPSetup.MaterialNumberingID : Edm.String "Material Numbering Sequence"
PX.Objects.AM.AMPSetup.WipAdjustNumberingID : Edm.String "WIP Adjustment Numbering Sequence"
PX.Objects.AM.AMPSetup.ProdCostNumberingID : Edm.String "Cost Numbering Sequence"
PX.Objects.AM.AMPSetup.DfltLbrRate : Edm.String "Use Labor Rate"
PX.Objects.AM.AMPSetup.FMLTime : Edm.Boolean [required] "Use Fixed Manufacturing Times"
PX.Objects.AM.AMPSetup.FMLTMRPOrdorOP : Edm.Boolean [required] "Use Order Start Date for MRP"
PX.Objects.AM.AMPSetup.InclScrap : Edm.Boolean [required] "Include Scrap in Completions"
PX.Objects.AM.AMPSetup.UseShiftCrewSize : Edm.Boolean [required] "Use Shift Crew Size"
PX.Objects.AM.AMPSetup.IncludeFinishTimeInCapacity : Edm.Boolean [required] "Consume Capacity for Finish Time"
PX.Objects.AM.AMPSetup.IncludeQueueTimeInCapacity : Edm.Boolean [required] "Consume Capacity for Queue Time"
PX.Objects.AM.AMPSetup.FixMfgCalendarID : Edm.String "Fixed Mfg. Calendar ID"
PX.Objects.AM.AMPSetup.tstamp : Edm.Binary
PX.Objects.AM.AMPSetup.SummPost : Edm.Boolean [required] "Post Summary on Updating GL"
PX.Objects.AM.AMPSetup.HoldEntry : Edm.Boolean [required] "Hold Documents on Entry"
PX.Objects.AM.AMPSetup.RequireControlTotal : Edm.Boolean [required] "Validate Document Totals on Entry"
PX.Objects.AM.AMPSetup.FMLTimeUnits : Edm.Int32 "Fixed Mfg. Units"
PX.Objects.AM.AMPSetup.DefaultEmployee : Edm.Boolean [required] "Insert Current User's Employee ID"
PX.Objects.AM.AMPSetup.DefaultOrderType : Edm.String "Default Order Type"
PX.Objects.AM.AMPSetup.CTPOrderType : Edm.String "Capable to Promise Order Type"
PX.Objects.AM.AMPSetup.DisassemblyNumberingID : Edm.String "Disassembly Numbering Sequence"
PX.Objects.AM.AMPSetup.DefaultDisassembleOrderType : Edm.String "Default Disassembly Order Type"
PX.Objects.AM.AMPSetup.VendorShipmentNumberingID : Edm.String "Vendor Shipment Numbering Sequence"
PX.Objects.AM.AMPSetup.HoldShipmentsOnEntry : Edm.Boolean [required] "Hold Shipments on Entry"
PX.Objects.AM.AMPSetup.ValidateShipmentTotalOnConfirm : Edm.Boolean [required] "Validate Shipment Total on Confirmation"
PX.Objects.AM.AMPSetup.RestrictClockCurrentUser : Edm.Boolean [required] "Restrict Clock Entry to Current User"
PX.Objects.AM.AMPSetup.LockWorkflowEnabled : Edm.Boolean [required] "Lock Production Orders Before Closing"
PX.Objects.AM.AMPSetup.NumberingByMoveNumberingID -> PX.Objects.CS.Numbering (MoveNumberingID=NumberingID)
PX.Objects.AM.AMPSetup.NumberingByLaborNumberingID -> PX.Objects.CS.Numbering (LaborNumberingID=NumberingID)
PX.Objects.AM.AMPSetup.NumberingByMaterialNumberingID -> PX.Objects.CS.Numbering (MaterialNumberingID=NumberingID)
PX.Objects.AM.AMPSetup.NumberingByWipAdjustNumberingID -> PX.Objects.CS.Numbering (WipAdjustNumberingID=NumberingID)
PX.Objects.AM.AMPSetup.NumberingByProdCostNumberingID -> PX.Objects.CS.Numbering (ProdCostNumberingID=NumberingID)
PX.Objects.AM.AMPSetup.NumberingByDisassemblyNumberingID -> PX.Objects.CS.Numbering (DisassemblyNumberingID=NumberingID)
PX.Objects.AM.AMPSetup.NumberingByVendorShipmentNumberingID -> PX.Objects.CS.Numbering (VendorShipmentNumberingID=NumberingID)
PX.Objects.AM.AMPSetup.AMOrderTypeByDefaultOrderType -> PX.Objects.AM.AMOrderType (DefaultOrderType=OrderType)
PX.Objects.AM.AMPSetup.AMOrderTypeByCTPOrderType -> PX.Objects.AM.AMOrderType (CTPOrderType=OrderType)
PX.Objects.AM.AMPSetup.AMOrderTypeByDefaultDisassembleOrderType -> PX.Objects.AM.AMOrderType (DefaultDisassembleOrderType=OrderType)
PX.Objects.AM.AMPSetup.CSCalendarByFixMfgCalendarID -> PX.Objects.CS.CSCalendar (FixMfgCalendarID=CalendarID)

# PX.Objects.AM.AMRPAuditHistory (EntityType)

Label: "Inventory Planning Audit History"
Key: Recno
Entity sets: PX_Objects_AM_AMRPAuditHistory, InventoryPlanningAuditHistory, AMRPAuditHistory

PX.Objects.AM.AMRPAuditHistory.Recno : Edm.Int32 [key] "Recno"
PX.Objects.AM.AMRPAuditHistory.MsgText : Edm.String "Message"
PX.Objects.AM.AMRPAuditHistory.MsgType : Edm.Int32 [required] "Message Type"
PX.Objects.AM.AMRPAuditHistory.ProcessID : Edm.Guid "Process ID"
PX.Objects.AM.AMRPAuditHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMRPAuditHistory.CreatedByScreenID : Edm.String "Created By (Screen ID)"
PX.Objects.AM.AMRPAuditHistory.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.AM.AMRPAuditHistory.tstamp : Edm.Binary
PX.Objects.AM.AMRPAuditHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Objects.AM.AMRPAuditTable (EntityType)

Label: "Inventory Planning Audit"
Key: Recno
Entity sets: PX_Objects_AM_AMRPAuditTable, InventoryPlanningAudit, AMRPAuditTable

PX.Objects.AM.AMRPAuditTable.Recno : Edm.Int32 [key] "Recno"
PX.Objects.AM.AMRPAuditTable.MsgText : Edm.String "Message"
PX.Objects.AM.AMRPAuditTable.MsgType : Edm.Int32 [required] "Message Type"
PX.Objects.AM.AMRPAuditTable.ProcessID : Edm.Guid "Process ID"
PX.Objects.AM.AMRPAuditTable.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMRPAuditTable.CreatedByScreenID : Edm.String "Created Screen ID"
PX.Objects.AM.AMRPAuditTable.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.AM.AMRPAuditTable.tstamp : Edm.Binary
PX.Objects.AM.AMRPAuditTable.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Objects.AM.AMRPDetail (EntityType)

Label: "Inventory Planning Detail"
Key: RecordID
Entity sets: PX_Objects_AM_AMRPDetail, InventoryPlanningDetail, AMRPDetail

PX.Objects.AM.AMRPDetail.RecordID : Edm.Int32 [key] "Record ID"
PX.Objects.AM.AMRPDetail.ActionDate : Edm.DateTimeOffset "Action Date"
PX.Objects.AM.AMRPDetail.ActionLeadTime : Edm.Int32 [required] "Action Lead Time"
PX.Objects.AM.AMRPDetail.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMRPDetail.BOMRevisionID : Edm.String "BOM Revision"
PX.Objects.AM.AMRPDetail.BOMLevel : Edm.Int32 [required] "BOM Level"
PX.Objects.AM.AMRPDetail.DetailFPRecordID : Edm.Int32 "Detail FP ID"
PX.Objects.AM.AMRPDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMRPDetail.IsSub : Edm.Boolean [required] "Is Sub"
PX.Objects.AM.AMRPDetail.ParentInventoryID : Edm.Int32 "Parent Inventory ID"
PX.Objects.AM.AMRPDetail.ProductInventoryID : Edm.Int32 "Product Inventory ID"
PX.Objects.AM.AMRPDetail.PromiseDate : Edm.DateTimeOffset "Promise Date"
PX.Objects.AM.AMRPDetail.RefType : Edm.String "Reference Type"
PX.Objects.AM.AMRPDetail.SDFlag : Edm.String "SD Flag"
PX.Objects.AM.AMRPDetail.ReplenishmentSource : Edm.String "Source"
PX.Objects.AM.AMRPDetail.BaseQty : Edm.Decimal [required] "Base Qty."
PX.Objects.AM.AMRPDetail.BaseUOM : Edm.String "Base UOM"
PX.Objects.AM.AMRPDetail.Type : Edm.String "Type"
PX.Objects.AM.AMRPDetail.ProductManagerID : Edm.Int32 "Product Manager ID"
PX.Objects.AM.AMRPDetail.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.AM.AMRPDetail.Processed : Edm.Boolean [required] "Processed"
PX.Objects.AM.AMRPDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMRPDetail.CreatedByScreenID : Edm.String
PX.Objects.AM.AMRPDetail.CreatedDateTime : Edm.DateTimeOffset "Inventory Planning Date"
PX.Objects.AM.AMRPDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMRPDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMRPDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMRPDetail.tstamp : Edm.Binary
PX.Objects.AM.AMRPDetail.RefNbr : Edm.String "Related Document"
PX.Objects.AM.AMRPDetail.ParentRefNbr : Edm.String "Related Parent Document"
PX.Objects.AM.AMRPDetail.ProductRefNbr : Edm.String "Related Product Document"
PX.Objects.AM.AMRPDetail.RefNoteID : Edm.Guid "Related Document ID"
PX.Objects.AM.AMRPDetail.ParentRefNoteID : Edm.Guid "Related Parent Document ID"
PX.Objects.AM.AMRPDetail.ProductRefNoteID : Edm.Guid "Related Product Document ID"
PX.Objects.AM.AMRPDetail.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMRPDetail.PlannedRefNbr : Edm.String "Generated Supply Document"
PX.Objects.AM.AMRPDetail.EPEmployeeByProductManagerID -> PX.Objects.EP.EPEmployee (ProductManagerID=BAccountID)
PX.Objects.AM.AMRPDetail.VendorByPreferredVendorID -> PX.Objects.AP.Vendor (PreferredVendorID=BAccountID)
PX.Objects.AM.AMRPDetail.BAccountByPreferredVendorID -> PX.Objects.CR.BAccount (PreferredVendorID=BAccountID)
PX.Objects.AM.AMRPDetail.ContactByProductManagerID -> PX.Objects.CR.Contact (ProductManagerID=ContactID)
PX.Objects.AM.AMRPDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMRPDetail.InventoryItemByParentInventoryID -> PX.Objects.IN.InventoryItem (ParentInventoryID=InventoryID)
PX.Objects.AM.AMRPDetail.InventoryItemByProductInventoryID -> PX.Objects.IN.InventoryItem (ProductInventoryID=InventoryID)
PX.Objects.AM.AMRPDetail.AMBomItemByBOMRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, BOMRevisionID=RevisionID)
PX.Objects.AM.AMRPDetail.AMBomItemByBOMID -> PX.Objects.AM.AMBomItem (BOMRevisionID=RevisionID, BOMID=BOMID)
PX.Objects.AM.AMRPDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMRPDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMRPDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMRPDetail.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMRPDetail.INKitSpecHdrByKitRevisionID -> PX.Objects.IN.INKitSpecHdr
PX.Objects.AM.AMRPDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPDetail.INSiteByTransferSiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPDetail.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMRPDetail.INSubItemByParentSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMRPDetail.INSubItemByProductSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMRPDetail.INUnitByInventoryID -> PX.Objects.IN.INUnit (BaseUOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMRPDetail.AMRPDetailFPByDetailFPRecordID -> PX.Objects.AM.AMRPDetailFP (DetailFPRecordID=RecordID)

# PX.Objects.AM.AMRPDetailFP (EntityType)

Label: "Inventory Planning First Pass Detail"
Key: RecordID
Entity sets: PX_Objects_AM_AMRPDetailFP, InventoryPlanningFirstPassDetail, AMRPDetailFP
Non-filterable, non-selectable: SiteSequence, ParentSchdNoteID, ProjectedOnHandQty, ConsolidatedStockingQty, ConsolidatedStockingOriginalQty

PX.Objects.AM.AMRPDetailFP.RecordID : Edm.Int32 [key] "Record ID"
PX.Objects.AM.AMRPDetailFP.BOMID : Edm.String "BOM ID"
PX.Objects.AM.AMRPDetailFP.BOMRevisionID : Edm.String "BOM Revision"
PX.Objects.AM.AMRPDetailFP.OrderQtyConsumed : Edm.Decimal [required] "Consumed Forecast Qty."
PX.Objects.AM.AMRPDetailFP.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMRPDetailFP.SubItemID : Edm.Int32 "Subitem"
PX.Objects.AM.AMRPDetailFP.LowLevel : Edm.Int32 [required] "Low Level"
PX.Objects.AM.AMRPDetailFP.PlanDate : Edm.DateTimeOffset "Plan Date"
PX.Objects.AM.AMRPDetailFP.OriginalQty : Edm.Decimal [required] "Original Stock Qty."
PX.Objects.AM.AMRPDetailFP.Qty : Edm.Decimal [required] "Stock Qty."
PX.Objects.AM.AMRPDetailFP.ParentInventoryID : Edm.Int32 "Parent Inventory ID"
PX.Objects.AM.AMRPDetailFP.ParentSubItemID : Edm.Int32 "Parent Subitem"
PX.Objects.AM.AMRPDetailFP.ProductInventoryID : Edm.Int32 "Product Inventory ID"
PX.Objects.AM.AMRPDetailFP.ProductSubItemID : Edm.Int32 "Product Subitem"
PX.Objects.AM.AMRPDetailFP.Processed : Edm.Boolean [required] "Processed"
PX.Objects.AM.AMRPDetailFP.OnHoldStatus : Edm.Int32 [required] "On hold status"
PX.Objects.AM.AMRPDetailFP.RefType : Edm.String "Ref Type"
PX.Objects.AM.AMRPDetailFP.RequiredDate : Edm.DateTimeOffset "Required Date"
PX.Objects.AM.AMRPDetailFP.SDFlag : Edm.String "SD Flag"
PX.Objects.AM.AMRPDetailFP.SuppliedQty : Edm.Decimal [required] "Supplied Qty."
PX.Objects.AM.AMRPDetailFP.Type : Edm.String "Type"
PX.Objects.AM.AMRPDetailFP.tstamp : Edm.Binary
PX.Objects.AM.AMRPDetailFP.PlanID : Edm.Int64
PX.Objects.AM.AMRPDetailFP.PlanType : Edm.String "Plan Type"
PX.Objects.AM.AMRPDetailFP.VendorID : Edm.Int32
PX.Objects.AM.AMRPDetailFP.VendorLocationID : Edm.Int32
PX.Objects.AM.AMRPDetailFP.SupplyPlanID : Edm.Int64
PX.Objects.AM.AMRPDetailFP.DemandPlanID : Edm.Int64
PX.Objects.AM.AMRPDetailFP.BAccountID : Edm.Int32
PX.Objects.AM.AMRPDetailFP.RefNbr : Edm.String "Ref Nbr"
PX.Objects.AM.AMRPDetailFP.ParentRefNbr : Edm.String "Parent Reference Nbr."
PX.Objects.AM.AMRPDetailFP.ProductRefNbr : Edm.String "Product Reference Nbr."
PX.Objects.AM.AMRPDetailFP.RefNoteID : Edm.Guid "Related Document ID"
PX.Objects.AM.AMRPDetailFP.ParentRefNoteID : Edm.Guid "Related Parent Document ID"
PX.Objects.AM.AMRPDetailFP.ProductRefNoteID : Edm.Guid "Related Product Document ID"
PX.Objects.AM.AMRPDetailFP.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMRPDetailFP.ConsolidatedRecordID : Edm.Int32 "Consolidated Record"
PX.Objects.AM.AMRPDetailFP.ConsolidatedSafetyQty : Edm.Decimal "Consolidated Safety Qty."
PX.Objects.AM.AMRPDetailFP.SiteSequence : Edm.Int32 "Warehouse Sequence"
PX.Objects.AM.AMRPDetailFP.ParentSchdNoteID : Edm.Guid "Parent Schedule ID"
PX.Objects.AM.AMRPDetailFP.ProjectedOnHandQty : Edm.Decimal "Projected On-Hand Qty."
PX.Objects.AM.AMRPDetailFP.ConsolidatedStockingQty : Edm.Decimal
PX.Objects.AM.AMRPDetailFP.ConsolidatedStockingOriginalQty : Edm.Decimal
PX.Objects.AM.AMRPDetailFP.PureOnHandQty : Edm.Decimal
PX.Objects.AM.AMRPDetailFP.AvoidDeleteExceptionFlg : Edm.Boolean
PX.Objects.AM.AMRPDetailFP.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AM.AMRPDetailFP.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AM.AMRPDetailFP.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMRPDetailFP.InventoryItemByParentInventoryID -> PX.Objects.IN.InventoryItem (ParentInventoryID=InventoryID)
PX.Objects.AM.AMRPDetailFP.InventoryItemByProductInventoryID -> PX.Objects.IN.InventoryItem (ProductInventoryID=InventoryID)
PX.Objects.AM.AMRPDetailFP.AMBomItemByBOMRevisionID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, BOMRevisionID=RevisionID)
PX.Objects.AM.AMRPDetailFP.INItemPlanBySupplyPlanID -> PX.Objects.IN.INItemPlan (SupplyPlanID=PlanID)
PX.Objects.AM.AMRPDetailFP.INItemPlanByDemandPlanID -> PX.Objects.IN.INItemPlan (DemandPlanID=PlanID)
PX.Objects.AM.AMRPDetailFP.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.AM.AMRPDetailFP.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMRPDetailFP.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMRPDetailFP.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPDetailFP.INSiteByTransferSiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPDetailFP.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID, VendorLocationID=LocationID)
PX.Objects.AM.AMRPDetailFP.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)

# PX.Objects.AM.AMRPDetailPlan (EntityType)

Label: "Inventory Planning Detail Plan"
Key: PlanID
Entity sets: PX_Objects_AM_AMRPDetailPlan, InventoryPlanningDetailPlan, AMRPDetailPlan
Non-filterable, non-selectable: RefNbr, OrigRefNoteID, Type

PX.Objects.AM.AMRPDetailPlan.PlanID : Edm.Int64 [key]
PX.Objects.AM.AMRPDetailPlan.FPRecordID : Edm.Int32 "FP Record ID"
PX.Objects.AM.AMRPDetailPlan.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMRPDetailPlan.SubItemID : Edm.Int32 "Subitem"
PX.Objects.AM.AMRPDetailPlan.PlanDate : Edm.DateTimeOffset "Plan Date"
PX.Objects.AM.AMRPDetailPlan.PlanType : Edm.String "Plan Type"
PX.Objects.AM.AMRPDetailPlan.Qty : Edm.Decimal [required] "Stock Qty."
PX.Objects.AM.AMRPDetailPlan.Processed : Edm.Boolean [required] "Processed"
PX.Objects.AM.AMRPDetailPlan.LowLevel : Edm.Int32 [required] "Low Level"
PX.Objects.AM.AMRPDetailPlan.OnHoldStatus : Edm.Int32 [required] "On hold status"
PX.Objects.AM.AMRPDetailPlan.RefType : Edm.String "Ref Type"
PX.Objects.AM.AMRPDetailPlan.SDFlag : Edm.String "SD Flag"
PX.Objects.AM.AMRPDetailPlan.SupplyPlanID : Edm.Int64
PX.Objects.AM.AMRPDetailPlan.DemandPlanID : Edm.Int64
PX.Objects.AM.AMRPDetailPlan.BAccountID : Edm.Int32
PX.Objects.AM.AMRPDetailPlan.RefNoteID : Edm.Guid
PX.Objects.AM.AMRPDetailPlan.ParentInventoryID : Edm.Int32 "Parent Inventory ID"
PX.Objects.AM.AMRPDetailPlan.ParentSubItemID : Edm.Int32 "Parent Subitem"
PX.Objects.AM.AMRPDetailPlan.tstamp : Edm.Binary
PX.Objects.AM.AMRPDetailPlan.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMRPDetailPlan.RefNbr : Edm.String "Ref Nbr"
PX.Objects.AM.AMRPDetailPlan.OrigRefNoteID : Edm.Guid
PX.Objects.AM.AMRPDetailPlan.Type : Edm.String
PX.Objects.AM.AMRPDetailPlan.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AM.AMRPDetailPlan.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMRPDetailPlan.InventoryItemByParentInventoryID -> PX.Objects.IN.InventoryItem (ParentInventoryID=InventoryID)
PX.Objects.AM.AMRPDetailPlan.INItemPlanBySupplyPlanID -> PX.Objects.IN.INItemPlan (SupplyPlanID=PlanID)
PX.Objects.AM.AMRPDetailPlan.INItemPlanByDemandPlanID -> PX.Objects.IN.INItemPlan (DemandPlanID=PlanID)
PX.Objects.AM.AMRPDetailPlan.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.AM.AMRPDetailPlan.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMRPDetailPlan.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMRPDetailPlan.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPDetailPlan.INSiteByTransferSiteID -> PX.Objects.IN.INSite

# PX.Objects.AM.AMRPExceptions (EntityType)

Label: "Inventory Planning Exceptions"
Key: RecordID
Entity sets: PX_Objects_AM_AMRPExceptions, InventoryPlanningExceptions, AMRPExceptions

PX.Objects.AM.AMRPExceptions.RecordID : Edm.Int32 [key] "Record ID"
PX.Objects.AM.AMRPExceptions.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMRPExceptions.Type : Edm.String "Type"
PX.Objects.AM.AMRPExceptions.RefType : Edm.String "Ref. Type"
PX.Objects.AM.AMRPExceptions.RefNbr : Edm.String "Related Document"
PX.Objects.AM.AMRPExceptions.RefNoteID : Edm.Guid "Related Document ID"
PX.Objects.AM.AMRPExceptions.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMRPExceptions.PromiseDate : Edm.DateTimeOffset "Promise Date"
PX.Objects.AM.AMRPExceptions.RequiredDate : Edm.DateTimeOffset "Required Date"
PX.Objects.AM.AMRPExceptions.SupplyQty : Edm.Decimal [required] "Supply Qty."
PX.Objects.AM.AMRPExceptions.ProductManagerID : Edm.Int32 "Product Manager ID"
PX.Objects.AM.AMRPExceptions.tstamp : Edm.Binary
PX.Objects.AM.AMRPExceptions.QtyToReduce : Edm.Decimal "Qty. to Reduce"
PX.Objects.AM.AMRPExceptions.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.AMRPExceptions.EPEmployeeByProductManagerID -> PX.Objects.EP.EPEmployee (ProductManagerID=BAccountID)
PX.Objects.AM.AMRPExceptions.ContactByProductManagerID -> PX.Objects.CR.Contact (ProductManagerID=ContactID)
PX.Objects.AM.AMRPExceptions.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMRPExceptions.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMRPExceptions.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.AMRPExceptions.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPExceptions.INSiteBySupplySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPExceptions.INSubItemBySubItemID -> PX.Objects.IN.INSubItem

# PX.Objects.AM.AMRPHistory (EntityType)

Label: "Inventory Planning History"
Key: ProcessID
Entity sets: PX_Objects_AM_AMRPHistory, InventoryPlanningHistory, AMRPHistory

PX.Objects.AM.AMRPHistory.ProcessID : Edm.Guid [key] "Process ID"
PX.Objects.AM.AMRPHistory.StartDateTime : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.AMRPHistory.EndDateTime : Edm.DateTimeOffset "End Date"
PX.Objects.AM.AMRPHistory.Duration : Edm.Int32 [required] "Duration"
PX.Objects.AM.AMRPHistory.HasError : Edm.Boolean [required] "Has Errors"
PX.Objects.AM.AMRPHistory.CountAMRPDetailPlan : Edm.Int32 [required] "Detail Plan Count"
PX.Objects.AM.AMRPHistory.CountAMRPDetailFP : Edm.Int32 [required] "First Pass Detail Count"
PX.Objects.AM.AMRPHistory.CountAMRPDetail : Edm.Int32 [required] "Detail Count"
PX.Objects.AM.AMRPHistory.CountAMRPExceptions : Edm.Int32 [required] "Exceptions Count"
PX.Objects.AM.AMRPHistory.CountAMRPPlan : Edm.Int32 [required] "Plan Count"
PX.Objects.AM.AMRPHistory.CountAMRPItemSite : Edm.Int32 [required] "Inventory Count"
PX.Objects.AM.AMRPHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMRPHistory.CreatedByScreenID : Edm.String
PX.Objects.AM.AMRPHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMRPHistory.Tstamp : Edm.Binary "Tstamp"
PX.Objects.AM.AMRPHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Objects.AM.AMRPItemSite (EntityType)

Label: "Inventory Planning Inventory"
Key: InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_AM_AMRPItemSite, InventoryPlanningInventory, AMRPItemSite

PX.Objects.AM.AMRPItemSite.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AM.AMRPItemSite.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMRPItemSite.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.AM.AMRPItemSite.LeadTime : Edm.Int32 [required] "Lead Time"
PX.Objects.AM.AMRPItemSite.PreferredVendorID : Edm.Int32 "Preferred Vendor"
PX.Objects.AM.AMRPItemSite.ProductManagerID : Edm.Int32 "Product Manager"
PX.Objects.AM.AMRPItemSite.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.AM.AMRPItemSite.ReorderPoint : Edm.Decimal "Reorder Point"
PX.Objects.AM.AMRPItemSite.ReplenishmentSource : Edm.String "Replenishment Source"
PX.Objects.AM.AMRPItemSite.SafetyStock : Edm.Decimal "Safety Stock"
PX.Objects.AM.AMRPItemSite.LotSize : Edm.Decimal "Lot Size"
PX.Objects.AM.AMRPItemSite.MaxOrdQty : Edm.Decimal "Max. Order Qty."
PX.Objects.AM.AMRPItemSite.MinOrdQty : Edm.Decimal "Min. Order Qty."
PX.Objects.AM.AMRPItemSite.TransferLeadTime : Edm.Int32 [required]
PX.Objects.AM.AMRPItemSite.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMRPItemSite.CreatedByScreenID : Edm.String
PX.Objects.AM.AMRPItemSite.CreatedDateTime : Edm.DateTimeOffset "MRP Bucket Date"
PX.Objects.AM.AMRPItemSite.tstamp : Edm.Binary
PX.Objects.AM.AMRPItemSite.AMGroupWindow : Edm.Int32 "Days of Supply"
PX.Objects.AM.AMRPItemSite.StockMethod : Edm.String "Stocking Method"
PX.Objects.AM.AMRPItemSite.MaxQty : Edm.Decimal "Max Qty."
PX.Objects.AM.AMRPItemSite.EOQ : Edm.Decimal "EOQ"
PX.Objects.AM.AMRPItemSite.EPEmployeeByProductManagerID -> PX.Objects.EP.EPEmployee (ProductManagerID=BAccountID)
PX.Objects.AM.AMRPItemSite.VendorByPreferredVendorID -> PX.Objects.AP.Vendor (PreferredVendorID=BAccountID)
PX.Objects.AM.AMRPItemSite.BAccountByPreferredVendorID -> PX.Objects.CR.BAccount (PreferredVendorID=BAccountID)
PX.Objects.AM.AMRPItemSite.ContactByProductManagerID -> PX.Objects.CR.Contact (ProductManagerID=ContactID)
PX.Objects.AM.AMRPItemSite.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMRPItemSite.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMRPItemSite.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMRPItemSite.INSiteByReplenishmentSiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPItemSite.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.AM.AMRPPlan (EntityType)

Label: "MRP Plan"
Key: RecordID
Entity sets: PX_Objects_AM_AMRPPlan, MRPPlan, AMRPPlan
Non-filterable, non-selectable: QtyOnHand

PX.Objects.AM.AMRPPlan.ActionDate : Edm.DateTimeOffset "Action Date"
PX.Objects.AM.AMRPPlan.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMRPPlan.RecordID : Edm.Int32 [key]
PX.Objects.AM.AMRPPlan.ParentInventoryID : Edm.Int32 "Parent Inventory ID"
PX.Objects.AM.AMRPPlan.ProductInventoryID : Edm.Int32 "Product Inventory ID"
PX.Objects.AM.AMRPPlan.PromiseDate : Edm.DateTimeOffset "Promise Date"
PX.Objects.AM.AMRPPlan.BaseQty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMRPPlan.RefType : Edm.String "Reference Type"
PX.Objects.AM.AMRPPlan.SDflag : Edm.String "SD Flag"
PX.Objects.AM.AMRPPlan.Type : Edm.String "Type"
PX.Objects.AM.AMRPPlan.UOM : Edm.String "UOM"
PX.Objects.AM.AMRPPlan.Tstamp : Edm.Binary
PX.Objects.AM.AMRPPlan.RefNbr : Edm.String "Related Document"
PX.Objects.AM.AMRPPlan.RefNoteID : Edm.Guid "Related Document ID"
PX.Objects.AM.AMRPPlan.IsPlan : Edm.Boolean [required] "Plan"
PX.Objects.AM.AMRPPlan.QtyOnHand : Edm.Decimal "Projected On-Hand Qty."
PX.Objects.AM.AMRPPlan.ProductRefNbr : Edm.String "Related Product Document"
PX.Objects.AM.AMRPPlan.ProductRefNoteID : Edm.Guid "Related Product Document ID"
PX.Objects.AM.AMRPPlan.ConsolidationID : Edm.String "Consolidation ID"
PX.Objects.AM.AMRPPlan.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMRPPlan.InventoryItemByParentInventoryID -> PX.Objects.IN.InventoryItem (ParentInventoryID=InventoryID)
PX.Objects.AM.AMRPPlan.InventoryItemByProductInventoryID -> PX.Objects.IN.InventoryItem (ProductInventoryID=InventoryID)
PX.Objects.AM.AMRPPlan.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMRPPlan.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMRPPlan.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMRPPlan.INSubItemByParentSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMRPPlan.INSubItemByProductSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMRPPlan.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.AM.AMRPSetup (EntityType)

Label: "Inventory Planning Preferences"
Singletons: PX_Objects_AM_AMRPSetup, InventoryPlanningPreferences, AMRPSetup

PX.Objects.AM.AMRPSetup.IncludeOnHoldSalesOrder : Edm.Boolean [required] "Include On-Hold Sales Orders"
PX.Objects.AM.AMRPSetup.IncludeOnHoldPurchaseOrder : Edm.Boolean [required] "Include On-Hold Purchase Orders"
PX.Objects.AM.AMRPSetup.IncludeOnHoldProductionOrder : Edm.Boolean [required] "Include On-Hold Production Orders"
PX.Objects.AM.AMRPSetup.ExceptionDaysBefore : Edm.Int32 [required] "Days Before"
PX.Objects.AM.AMRPSetup.ExceptionDaysAfter : Edm.Int32 [required] "Days After"
PX.Objects.AM.AMRPSetup.ForecastPlanHorizon : Edm.Int32 [required] "Demand Time Fence"
PX.Objects.AM.AMRPSetup.ForecastNumberingID : Edm.String "Numbering Sequence"
PX.Objects.AM.AMRPSetup.PurchaseCalendarID : Edm.String "Purchase Calendar ID"
PX.Objects.AM.AMRPSetup.UseFixMfgLeadTime : Edm.Boolean [required] "Use Fixed Manufacturing Times"
PX.Objects.AM.AMRPSetup.MPSFence : Edm.Int32 [required] "MPS Time Fence"
PX.Objects.AM.AMRPSetup.DefaultMPSTypeID : Edm.String "Default Type"
PX.Objects.AM.AMRPSetup.GracePeriod : Edm.Int32 [required] "Grace Period"
PX.Objects.AM.AMRPSetup.StockingMethod : Edm.Int32 [required] "Stocking Method"
PX.Objects.AM.AMRPSetup.tstamp : Edm.Binary
PX.Objects.AM.AMRPSetup.PlanOrderType : Edm.String "Plan Order Type"
PX.Objects.AM.AMRPSetup.LastMrpRegenCompletedByID : Edm.Guid "Last Regen Completed By"
PX.Objects.AM.AMRPSetup.LastMrpRegenCompletedDateTime : Edm.DateTimeOffset "Last Regen Completed At"
PX.Objects.AM.AMRPSetup.UseDaysSupplytoConsolidateOrders : Edm.Boolean [required] "Use Days of Supply to Consolidate Orders"
PX.Objects.AM.AMRPSetup.UseLongTermConsolidationBucket : Edm.Boolean [required] "Use Long-Term Consolidation Bucket"
PX.Objects.AM.AMRPSetup.ConsolidateAfterDays : Edm.Int32 [required] "Consolidate After (Days)"
PX.Objects.AM.AMRPSetup.BucketDays : Edm.Int32 [required] "Bucket (Days)"
PX.Objects.AM.AMRPSetup.IncludeExpiredBlanketSalesOrders : Edm.Boolean [required] "Include Expired Blanket Sales Orders"
PX.Objects.AM.AMRPSetup.AMPlanningHorizon : Edm.Int32 [required] "Planning Horizon"
PX.Objects.AM.AMRPSetup.NumberingByForecastNumberingID -> PX.Objects.CS.Numbering (ForecastNumberingID=NumberingID)
PX.Objects.AM.AMRPSetup.AMMPSTypeByDefaultMPSTypeID -> PX.Objects.AM.AMMPSType (DefaultMPSTypeID=MPSTypeID)
PX.Objects.AM.AMRPSetup.AMOrderTypeByPlanOrderType -> PX.Objects.AM.AMOrderType (PlanOrderType=OrderType)
PX.Objects.AM.AMRPSetup.CSCalendarByPurchaseCalendarID -> PX.Objects.CS.CSCalendar (PurchaseCalendarID=CalendarID)

# PX.Objects.AM.AMScanSetup (EntityType)

Label: "AM Scan Setup"
Key: BranchID
Entity sets: PX_Objects_AM_AMScanSetup, AMScanSetup

PX.Objects.AM.AMScanSetup.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.AM.AMScanSetup.ExplicitLineConfirmation : Edm.Boolean [required] "Use Explicit Line Confirmation"
PX.Objects.AM.AMScanSetup.QtyEnterModeInMove : Edm.String "Quantity Input Mode in Move"
PX.Objects.AM.AMScanSetup.QtyEnterModeInLabor : Edm.String "Quantity Input Mode in Labor"
PX.Objects.AM.AMScanSetup.QtyEnterModeInMaterials : Edm.String "Quantity Input Mode in Materials"
PX.Objects.AM.AMScanSetup.UseRemainingQtyInMove : Edm.Boolean [required] "Use Remaining Quantity in Move"
PX.Objects.AM.AMScanSetup.UseRemainingQtyInMaterials : Edm.Boolean [required] "Use Remaining Quantity in Materials"
PX.Objects.AM.AMScanSetup.UseDefaultOrderType : Edm.Boolean [required] "Use Default Order Type"
PX.Objects.AM.AMScanSetup.RequestLocationForEachItemInMove : Edm.Boolean [required] "Request Location for Each Item in Move/Labor"
PX.Objects.AM.AMScanSetup.RequestLocationForEachItemInMaterials : Edm.Boolean [required] "Request Location for Each Item in Materials"
PX.Objects.AM.AMScanSetup.DefaultWarehouse : Edm.Boolean [required] "Insert Default Warehouse from User Profile"
PX.Objects.AM.AMScanSetup.DefaultLotSerialNumber : Edm.Boolean [required] "Use Default Auto-Generated Lot/Serial Nbr."
PX.Objects.AM.AMScanSetup.DefaultExpireDate : Edm.Boolean [required] "Use Default Expiration Date"
PX.Objects.AM.AMScanSetup.tstamp : Edm.Binary
PX.Objects.AM.AMScanSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMScanSetup.CreatedByScreenID : Edm.String
PX.Objects.AM.AMScanSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMScanSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMScanSetup.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMScanSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMScanSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMScanSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.AM.AMScanUserSetup (EntityType)

Label: "AM Scan User Setup"
Key: Mode, UserID
Entity sets: PX_Objects_AM_AMScanUserSetup, AMScanUserSetup

PX.Objects.AM.AMScanUserSetup.UserID : Edm.Guid [key] "User"
PX.Objects.AM.AMScanUserSetup.IsOverridden : Edm.Boolean [required] "Is Overridden"
PX.Objects.AM.AMScanUserSetup.Mode : Edm.String [key] "Mode"
PX.Objects.AM.AMScanUserSetup.DefaultWarehouse : Edm.Boolean [required] "Default Warehouse from User Profile"
PX.Objects.AM.AMScanUserSetup.DefaultLotSerialNumber : Edm.Boolean [required] "Use Default Auto-Generated Lot/Serial Nbr."
PX.Objects.AM.AMScanUserSetup.DefaultExpireDate : Edm.Boolean [required] "Use Default Expiration Date"

# PX.Objects.AM.AMSchdItem (EntityType)

Label: "Schedule Item"
Key: OrderType, ProdOrdID, SchdID
Entity sets: PX_Objects_AM_AMSchdItem, ScheduleItem, AMSchdItem
Non-filterable, non-selectable: QtyRemaining, NoteText, OrigConstDate, OrigSchedulingMethod

PX.Objects.AM.AMSchdItem.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMSchdItem.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMSchdItem.IsPlan : Edm.Boolean [required] "Is Plan"
PX.Objects.AM.AMSchdItem.IsMRP : Edm.Boolean [required] "Is MRP"
PX.Objects.AM.AMSchdItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMSchdItem.SchdID : Edm.Int32 [key required] "Schedule ID"
PX.Objects.AM.AMSchdItem.ConstDate : Edm.DateTimeOffset "Constraint"
PX.Objects.AM.AMSchdItem.EndDate : Edm.DateTimeOffset [required] "End Date"
PX.Objects.AM.AMSchdItem.QtyComplete : Edm.Decimal [required] "Completed Qty."
PX.Objects.AM.AMSchdItem.QtyScrapped : Edm.Decimal [required] "Scrapped Qty."
PX.Objects.AM.AMSchdItem.QtytoProd : Edm.Decimal [required] "Qty. to Produce"
PX.Objects.AM.AMSchdItem.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMSchdItem.SchedulingMethod : Edm.String "Scheduling Method"
PX.Objects.AM.AMSchdItem.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.AM.AMSchdItem.SchPriority : Edm.Int16 [required] "Dispatch Priority"
PX.Objects.AM.AMSchdItem.FirmSchedule : Edm.Boolean [required] "Firm Schedule"
PX.Objects.AM.AMSchdItem.MRPPlanID : Edm.Int64
PX.Objects.AM.AMSchdItem.NoteID : Edm.Guid
PX.Objects.AM.AMSchdItem.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMSchdItem.RefNoteID : Edm.Guid
PX.Objects.AM.AMSchdItem.ParentOrderType : Edm.String "Parent Order Type"
PX.Objects.AM.AMSchdItem.ParentOrdID : Edm.String "Parent Production Nbr."
PX.Objects.AM.AMSchdItem.OrigConstDate : Edm.DateTimeOffset "Original Constraint Date"
PX.Objects.AM.AMSchdItem.OrigSchedulingMethod : Edm.String "Original Scheduling Method"
PX.Objects.AM.AMSchdItem.tstamp : Edm.Binary
PX.Objects.AM.AMSchdItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMSchdItem.CreatedByScreenID : Edm.String
PX.Objects.AM.AMSchdItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSchdItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMSchdItem.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMSchdItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSchdItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMSchdItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMSchdItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMSchdItem.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMSchdItem.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMSchdItem.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMSchdItem.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)

# PX.Objects.AM.AMSchdOper (EntityType)

Label: "Schedule Operation"
Key: LineNbr, OperationID, OrderType, ProdOrdID, SchdID
Entity sets: PX_Objects_AM_AMSchdOper, ScheduleOperation, AMSchdOper
Non-filterable, non-selectable: QtyRemaining, TotalPlanTime

PX.Objects.AM.AMSchdOper.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.AMSchdOper.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.AMSchdOper.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.AMSchdOper.SchdID : Edm.Int32 [key required] "Schd ID"
PX.Objects.AM.AMSchdOper.LineNbr : Edm.Int32 [key required] "Line Nbr"
PX.Objects.AM.AMSchdOper.SortOrder : Edm.Int32 [required] "Line Order"
PX.Objects.AM.AMSchdOper.IsPlan : Edm.Boolean [required] "Is Plan"
PX.Objects.AM.AMSchdOper.IsMRP : Edm.Boolean [required] "Is MRP"
PX.Objects.AM.AMSchdOper.ConstDate : Edm.DateTimeOffset "Constraint"
PX.Objects.AM.AMSchdOper.EndDate : Edm.DateTimeOffset [required] "End Date"
PX.Objects.AM.AMSchdOper.MachID : Edm.String "Machine ID"
PX.Objects.AM.AMSchdOper.QueueTime : Edm.Int32 [required] "Queue Time"
PX.Objects.AM.AMSchdOper.SetupTime : Edm.Int32 [required] "Setup Time"
PX.Objects.AM.AMSchdOper.FinishTime : Edm.Int32 [required] "Finish Time"
PX.Objects.AM.AMSchdOper.MoveTime : Edm.Int32 [required] "Move Time"
PX.Objects.AM.AMSchdOper.RunTimeBase : Edm.Int32 [required] "Run Time Without Efficiency"
PX.Objects.AM.AMSchdOper.RunTime : Edm.Int32 [required] "Run Time"
PX.Objects.AM.AMSchdOper.QtyComplete : Edm.Decimal [required] "QtyComplete"
PX.Objects.AM.AMSchdOper.QtyScrapped : Edm.Decimal [required] "QtyScrapped"
PX.Objects.AM.AMSchdOper.QtytoProd : Edm.Decimal [required] "Qty. to Produce"
PX.Objects.AM.AMSchdOper.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMSchdOper.SchedulingMethod : Edm.String "Scheduling Method"
PX.Objects.AM.AMSchdOper.FirmSchedule : Edm.Boolean [required] "Firm Schedule"
PX.Objects.AM.AMSchdOper.SiteID : Edm.Int32 [required] "SiteID"
PX.Objects.AM.AMSchdOper.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.AM.AMSchdOper.TotalPlanTime : Edm.Int32 [required] "Total Plan Time"
PX.Objects.AM.AMSchdOper.WcID : Edm.String "Work Center"
PX.Objects.AM.AMSchdOper.tstamp : Edm.Binary
PX.Objects.AM.AMSchdOper.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMSchdOper.CreatedByScreenID : Edm.String
PX.Objects.AM.AMSchdOper.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSchdOper.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMSchdOper.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMSchdOper.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSchdOper.QueueStartDate : Edm.DateTimeOffset [required] "Queue Start Date"
PX.Objects.AM.AMSchdOper.MoveEndDate : Edm.DateTimeOffset [required] "Move End Date"
PX.Objects.AM.AMSchdOper.StatusID : Edm.String "Status"
PX.Objects.AM.AMSchdOper.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMSchdOper.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMSchdOper.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMSchdOper.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMSchdOper.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMSchdOper.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMSchdOper.AMSchdItemBySchdID -> PX.Objects.AM.AMSchdItem (OrderType=OrderType, ProdOrdID=ProdOrdID, SchdID=SchdID)
PX.Objects.AM.AMSchdOper.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)

# PX.Objects.AM.AMSchdOperDetail (EntityType)

Label: "Scheduled Operation Details"
Key: RecordID
Entity sets: PX_Objects_AM_AMSchdOperDetail, ScheduledOperationDetails, AMSchdOperDetail

PX.Objects.AM.AMSchdOperDetail.RecordID : Edm.Int64 [key] "Record ID"
PX.Objects.AM.AMSchdOperDetail.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMSchdOperDetail.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMSchdOperDetail.IsPlan : Edm.Boolean [required] "Is Plan"
PX.Objects.AM.AMSchdOperDetail.IsMRP : Edm.Boolean [required] "Is MRP"
PX.Objects.AM.AMSchdOperDetail.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMSchdOperDetail.SchdDate : Edm.DateTimeOffset "Schedule Date"
PX.Objects.AM.AMSchdOperDetail.RunTimeBase : Edm.Int32 [required] "Run Time Without Efficiency"
PX.Objects.AM.AMSchdOperDetail.RunTime : Edm.Int32 [required] "Run Time"
PX.Objects.AM.AMSchdOperDetail.FirmSchedule : Edm.Boolean [required] "Firm Schedule"
PX.Objects.AM.AMSchdOperDetail.SchdQty : Edm.Decimal [required] "Schedule Qty."
PX.Objects.AM.AMSchdOperDetail.Chain : Edm.Int32 [required] "Chain"
PX.Objects.AM.AMSchdOperDetail.SchdKey : Edm.Guid "Schedule Key"
PX.Objects.AM.AMSchdOperDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMSchdOperDetail.CreatedByScreenID : Edm.String
PX.Objects.AM.AMSchdOperDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSchdOperDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMSchdOperDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMSchdOperDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSchdOperDetail.tstamp : Edm.Binary
PX.Objects.AM.AMSchdOperDetail.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMSchdOperDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMSchdOperDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMSchdOperDetail.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMSchdOperDetail.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMSchdOperDetail.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)

# PX.Objects.AM.AMShift (EntityType)

Label: "Shift"
Key: ShiftCD, WcID
Entity sets: PX_Objects_AM_AMShift, Shift, AMShift
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMShift.ShiftCD : Edm.String [key] "Shift"
PX.Objects.AM.AMShift.CrewSize : Edm.Decimal [required] "Crew Size"
PX.Objects.AM.AMShift.MachNbr : Edm.Decimal [required] "Machines"
PX.Objects.AM.AMShift.ShftEff : Edm.Decimal [required] "Efficiency"
PX.Objects.AM.AMShift.CalendarID : Edm.String "Calendar ID"
PX.Objects.AM.AMShift.LaborCodeID : Edm.String "Labor Code"
PX.Objects.AM.AMShift.NoteID : Edm.Guid
PX.Objects.AM.AMShift.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMShift.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMShift.tstamp : Edm.Binary
PX.Objects.AM.AMShift.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMShift.CreatedByScreenID : Edm.String
PX.Objects.AM.AMShift.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMShift.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMShift.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMShift.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMShift.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMShift.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMShift.EPShiftCodeByShiftCD -> PX.Objects.EP.EPShiftCode (ShiftCD=ShiftCD)
PX.Objects.AM.AMShift.AMLaborCodeByLaborCodeID -> PX.Objects.AM.AMLaborCode (LaborCodeID=LaborCodeID)
PX.Objects.AM.AMShift.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)
PX.Objects.AM.AMShift.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.AM.AMShift.AMWCSchdCollection -> Collection(PX.Objects.AM.AMWCSchd)
PX.Objects.AM.AMShift.AMWCSchdDetailCollection -> Collection(PX.Objects.AM.AMWCSchdDetail)

# PX.Objects.AM.AMSiteTransfer (EntityType)

Label: "Warehouse Transfer"
Key: SiteID, TransferSiteID
Entity sets: PX_Objects_AM_AMSiteTransfer, WarehouseTransfer, AMSiteTransfer

PX.Objects.AM.AMSiteTransfer.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMSiteTransfer.TransferSiteID : Edm.Int32 [key] "Replenishment Warehouse"
PX.Objects.AM.AMSiteTransfer.TransferLeadTime : Edm.Int32 [required] "Transfer Lead Time (Days)"
PX.Objects.AM.AMSiteTransfer.tstamp : Edm.Binary
PX.Objects.AM.AMSiteTransfer.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMSiteTransfer.CreatedByScreenID : Edm.String
PX.Objects.AM.AMSiteTransfer.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSiteTransfer.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMSiteTransfer.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMSiteTransfer.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSiteTransfer.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMSiteTransfer.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMSiteTransfer.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMSiteTransfer.INSiteByTransferSiteID -> PX.Objects.IN.INSite (TransferSiteID=SiteID)

# PX.Objects.AM.AMSubItemDefault (EntityType)

Label: "Subitem Default"
Key: InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_AM_AMSubItemDefault, SubitemDefault, AMSubItemDefault

PX.Objects.AM.AMSubItemDefault.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMSubItemDefault.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AM.AMSubItemDefault.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.AM.AMSubItemDefault.IsItemDefault : Edm.Boolean [required] "Default"
PX.Objects.AM.AMSubItemDefault.BOMID : Edm.String "Default BOM ID"
PX.Objects.AM.AMSubItemDefault.PlanningBOMID : Edm.String "Planning BOM ID"
PX.Objects.AM.AMSubItemDefault.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMSubItemDefault.CreatedByScreenID : Edm.String
PX.Objects.AM.AMSubItemDefault.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSubItemDefault.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMSubItemDefault.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMSubItemDefault.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMSubItemDefault.tstamp : Edm.Binary
PX.Objects.AM.AMSubItemDefault.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMSubItemDefault.AMBomItemBySubItemID -> PX.Objects.AM.AMBomItem (BOMID=BOMID, InventoryID=InventoryID)
PX.Objects.AM.AMSubItemDefault.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMSubItemDefault.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMSubItemDefault.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMSubItemDefault.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.AM.AMToolMst (EntityType)

Label: "Tools"
Key: ToolID
Entity sets: PX_Objects_AM_AMToolMst, Tools, AMToolMst
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMToolMst.ToolID : Edm.String [key] "Tool ID"
PX.Objects.AM.AMToolMst.Descr : Edm.String "Description"
PX.Objects.AM.AMToolMst.Active : Edm.Boolean [required] "Active"
PX.Objects.AM.AMToolMst.ActualUses : Edm.Decimal [required] "Total Uses"
PX.Objects.AM.AMToolMst.NoteID : Edm.Guid
PX.Objects.AM.AMToolMst.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMToolMst.tstamp : Edm.Binary
PX.Objects.AM.AMToolMst.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMToolMst.CreatedByScreenID : Edm.String
PX.Objects.AM.AMToolMst.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMToolMst.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMToolMst.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMToolMst.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMToolMst.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMToolMst.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMToolMst.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMToolMst.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMToolMst.AMBomToolCollection -> Collection(PX.Objects.AM.AMBomTool)
PX.Objects.AM.AMToolMst.AMEstimateToolCollection -> Collection(PX.Objects.AM.AMEstimateTool)
PX.Objects.AM.AMToolMst.AMProdToolCollection -> Collection(PX.Objects.AM.AMProdTool)
PX.Objects.AM.AMToolMst.AMToolMstCurySettingsCollection -> Collection(PX.Objects.AM.AMToolMstCurySettings)
PX.Objects.AM.AMToolMst.AMToolSchdDetailCollection -> Collection(PX.Objects.AM.AMToolSchdDetail)

# PX.Objects.AM.AMToolMstCurySettings (EntityType)

Label: "Tools Currency Settings"
Key: CuryID, ToolID
Entity sets: PX_Objects_AM_AMToolMstCurySettings, ToolsCurrencySettings, AMToolMstCurySettings

PX.Objects.AM.AMToolMstCurySettings.ToolID : Edm.String [key] "Tool ID"
PX.Objects.AM.AMToolMstCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMToolMstCurySettings.ActualCost : Edm.Decimal [required] "Consumed Cost"
PX.Objects.AM.AMToolMstCurySettings.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.AM.AMToolMstCurySettings.TotalCost : Edm.Decimal [required] "Total Cost"
PX.Objects.AM.AMToolMstCurySettings.tstamp : Edm.Binary
PX.Objects.AM.AMToolMstCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMToolMstCurySettings.CreatedByScreenID : Edm.String
PX.Objects.AM.AMToolMstCurySettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMToolMstCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMToolMstCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMToolMstCurySettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMToolMstCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMToolMstCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMToolMstCurySettings.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMToolMstCurySettings.AMToolMstByToolID -> PX.Objects.AM.AMToolMst (ToolID=ToolID)

# PX.Objects.AM.AMToolSchdDetail (EntityType)

Label: "Tool Schedule Detail"
Key: RecordID
Entity sets: PX_Objects_AM_AMToolSchdDetail, ToolScheduleDetail, AMToolSchdDetail
Non-filterable, non-selectable: ResourceID, StartTimeString, EndTimeString, NoteText

PX.Objects.AM.AMToolSchdDetail.ResourceID : Edm.String "Resource ID"
PX.Objects.AM.AMToolSchdDetail.RecordID : Edm.Int64 [key] "Record ID"
PX.Objects.AM.AMToolSchdDetail.ToolID : Edm.String "Tool ID"
PX.Objects.AM.AMToolSchdDetail.SchdDate : Edm.DateTimeOffset "Schedule Date"
PX.Objects.AM.AMToolSchdDetail.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.AMToolSchdDetail.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.AMToolSchdDetail.StartTimeString : Edm.String "Start Time"
PX.Objects.AM.AMToolSchdDetail.EndTimeString : Edm.String "End Time"
PX.Objects.AM.AMToolSchdDetail.OrderByDate : Edm.DateTimeOffset "Order By Date Time"
PX.Objects.AM.AMToolSchdDetail.Description : Edm.String "Description"
PX.Objects.AM.AMToolSchdDetail.PlanQty : Edm.Int32 [required] "Plan Qty."
PX.Objects.AM.AMToolSchdDetail.SchdQty : Edm.Int32 [required] "Schedule Qty."
PX.Objects.AM.AMToolSchdDetail.ProdToolNoteID : Edm.Guid
PX.Objects.AM.AMToolSchdDetail.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMToolSchdDetail.IsBreak : Edm.Boolean [required] "Down Time"
PX.Objects.AM.AMToolSchdDetail.RunTimeBase : Edm.Int32 [required] "Run Time Without Efficiency"
PX.Objects.AM.AMToolSchdDetail.RunTime : Edm.Int32 [required] "Run Time"
PX.Objects.AM.AMToolSchdDetail.SchdBlocks : Edm.Int32 [required] "Scheduled Blocks"
PX.Objects.AM.AMToolSchdDetail.SchdKey : Edm.Guid "Schedule Key"
PX.Objects.AM.AMToolSchdDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMToolSchdDetail.CreatedByScreenID : Edm.String
PX.Objects.AM.AMToolSchdDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMToolSchdDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMToolSchdDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMToolSchdDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMToolSchdDetail.tstamp : Edm.Binary
PX.Objects.AM.AMToolSchdDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMToolSchdDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMToolSchdDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMToolSchdDetail.AMToolMstByToolID -> PX.Objects.AM.AMToolMst (ToolID=ToolID)

# PX.Objects.AM.AMTranCost (EntityType)

Label: "AM Transaction Cost"
Key: BatNbr, DocType, LineNbr
Entity sets: PX_Objects_AM_AMTranCost, AMTransactionCost, AMTranCost
Non-filterable, non-selectable: LaborTimeRaw

PX.Objects.AM.AMTranCost.DocType : Edm.String [key]
PX.Objects.AM.AMTranCost.BatNbr : Edm.String [key] "Batch Nbr."
PX.Objects.AM.AMTranCost.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMTranCost.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMTranCost.LaborType : Edm.String "Labor Type"
PX.Objects.AM.AMTranCost.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMTranCost.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMTranCost.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMTranCost.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMTranCost.LaborCodeID : Edm.String "Labor Code"
PX.Objects.AM.AMTranCost.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.AM.AMTranCost.Qty : Edm.Decimal "Quantity"
PX.Objects.AM.AMTranCost.BaseQty : Edm.Decimal "Base Qty."
PX.Objects.AM.AMTranCost.QtyScrapped : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.AMTranCost.BaseQtyScrapped : Edm.Decimal "Scrapped Base Qty."
PX.Objects.AM.AMTranCost.TranAmt : Edm.Decimal "Ext. Cost"
PX.Objects.AM.AMTranCost.EmployeeID : Edm.Int32 "Employee ID"
PX.Objects.AM.AMTranCost.ExtCost : Edm.Decimal "Labor Amount"
PX.Objects.AM.AMTranCost.GLModule : Edm.String "GL Module"
PX.Objects.AM.AMTranCost.GLBatNbr : Edm.String "GL Batch Nbr"
PX.Objects.AM.AMTranCost.GLLineNbr : Edm.Int32 "GL Batch Line Nbr"
PX.Objects.AM.AMTranCost.LaborTime : Edm.Int32 "Labor Time"
PX.Objects.AM.AMTranCost.LaborTimeRaw : Edm.Int32 "LaborTimeRaw"
PX.Objects.AM.AMTranCost.FinPeriodID : Edm.String
PX.Objects.AM.AMTranCost.TranPeriodID : Edm.String
PX.Objects.AM.AMTranCost.Released : Edm.Boolean "Released"
PX.Objects.AM.AMTranCost.WIPAcctID : Edm.Int32 "WIP Account"
PX.Objects.AM.AMTranCost.WIPSubID : Edm.Int32 "WIP Subaccount"
PX.Objects.AM.AMTranCost.tstamp : Edm.Binary
PX.Objects.AM.AMTranCost.TranDesc : Edm.String "Tran Description"
PX.Objects.AM.AMTranCost.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMTranCost.CreatedByScreenID : Edm.String
PX.Objects.AM.AMTranCost.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMTranCost.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMTranCost.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMTranCost.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMTranCost.OrigDocType : Edm.String "Orig Doc Type"
PX.Objects.AM.AMTranCost.OrigBatNbr : Edm.String "Orig Batch Nbr"
PX.Objects.AM.AMTranCost.OrigLineNbr : Edm.Int32 "Orig Line Nbr."
PX.Objects.AM.AMTranCost.ReasonCodeID : Edm.String "Reason Code"
PX.Objects.AM.AMTranCost.ReferenceCostID : Edm.String "Ref. Cost ID"
PX.Objects.AM.AMTranCost.CostRefNoteID : Edm.Guid "Cost Ref Note ID"
PX.Objects.AM.AMTranCost.InvtMult : Edm.Int16 "Multiplier"
PX.Objects.AM.AMTranCost.LastOper : Edm.Boolean "Is Last Oper"
PX.Objects.AM.AMTranCost.TranOverride : Edm.Boolean "Override"
PX.Objects.AM.AMTranCost.NoteID : Edm.Guid
PX.Objects.AM.AMTranCost.InventorySource : Edm.String "Inventory Source"
PX.Objects.AM.AMTranCost.IsGLEntry : Edm.Boolean "Is GL Entry"
PX.Objects.AM.AMTranCost.IsWIPDebit : Edm.Boolean "WIP Is Debit"
PX.Objects.AM.AMTranCost.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.AM.AMTranCost.BatchByGLBatNbr -> PX.Objects.GL.Batch (GLBatNbr=BatchNbr)
PX.Objects.AM.AMTranCost.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMTranCost.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMTranCost.AMBatchCostByBatNbr -> PX.Objects.AM.AMBatchCost (DocType=DocType, BatNbr=BatNbr)
PX.Objects.AM.AMTranCost.AMMTranByOrigLineNbr -> PX.Objects.AM.AMMTran (OrigDocType=DocType, OrigBatNbr=BatNbr, OrigLineNbr=LineNbr)
PX.Objects.AM.AMTranCost.ReasonCodeByReasonCodeID -> PX.Objects.CS.ReasonCode (ReasonCodeID=ReasonCodeID)
PX.Objects.AM.AMTranCost.AccountByWIPAcctID -> PX.Objects.GL.Account (WIPAcctID=AccountID)
PX.Objects.AM.AMTranCost.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMTranCost.SubByWIPSubID -> PX.Objects.GL.Sub (WIPSubID=SubID)
PX.Objects.AM.AMTranCost.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMTranCost.AMBatchByBatNbr -> PX.Objects.AM.AMBatch (DocType=DocType, BatNbr=BatNbr)
PX.Objects.AM.AMTranCost.AMBatchByOrigBatNbr -> PX.Objects.AM.AMBatch (OrigBatNbr=BatNbr)
PX.Objects.AM.AMTranCost.AMLaborCodeByLaborCodeID -> PX.Objects.AM.AMLaborCode (LaborCodeID=LaborCodeID)
PX.Objects.AM.AMTranCost.AMDisassembleBatchByBatNbr -> PX.Objects.AM.AMDisassembleBatch (DocType=DocType, BatNbr=BatchNbr)
PX.Objects.AM.AMTranCost.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.AM.AMTranCost.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.AMTranCost.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)

# PX.Objects.AM.AMVendorShipLine (EntityType)

Label: "Vendor Shipment Line"
Key: LineNbr, ShipmentNbr
Entity sets: PX_Objects_AM_AMVendorShipLine, VendorShipmentLine, AMVendorShipLine
Non-filterable, non-selectable: NoteText, UpdateProject

PX.Objects.AM.AMVendorShipLine.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.AM.AMVendorShipLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMVendorShipLine.LineType : Edm.String "Type"
PX.Objects.AM.AMVendorShipLine.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMVendorShipLine.TranType : Edm.String "Tran. Type"
PX.Objects.AM.AMVendorShipLine.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMVendorShipLine.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMVendorShipLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMVendorShipLine.UOM : Edm.String "UOM"
PX.Objects.AM.AMVendorShipLine.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMVendorShipLine.BaseQty : Edm.Decimal [required] "Base Qty."
PX.Objects.AM.AMVendorShipLine.LotSerCntr : Edm.Int32 [required] "LotSerCntr"
PX.Objects.AM.AMVendorShipLine.NoteID : Edm.Guid
PX.Objects.AM.AMVendorShipLine.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMVendorShipLine.tstamp : Edm.Binary
PX.Objects.AM.AMVendorShipLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMVendorShipLine.CreatedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMVendorShipLine.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipLine.UnassignedQty : Edm.Decimal [required]
PX.Objects.AM.AMVendorShipLine.TranDate : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipLine.InvtMult : Edm.Int16 [required] "Multiplier"
PX.Objects.AM.AMVendorShipLine.CostCenterID : Edm.Int32
PX.Objects.AM.AMVendorShipLine.UpdateProject : Edm.Boolean
PX.Objects.AM.AMVendorShipLine.Released : Edm.Boolean [required] "Released"
PX.Objects.AM.AMVendorShipLine.MatlLineID : Edm.Int32 "Material Line Nbr."
PX.Objects.AM.AMVendorShipLine.POOrderNbr : Edm.String "PO Order Nbr."
PX.Objects.AM.AMVendorShipLine.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.AM.AMVendorShipLine.TranDesc : Edm.String "Tran Description"
PX.Objects.AM.AMVendorShipLine.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AM.AMVendorShipLine.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AM.AMVendorShipLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMVendorShipLine.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMVendorShipLine.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMVendorShipLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMVendorShipLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMVendorShipLine.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMVendorShipLine.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMVendorShipLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMVendorShipLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMVendorShipLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMVendorShipLine.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMVendorShipLine.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMVendorShipLine.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)
PX.Objects.AM.AMVendorShipLine.AMProdMatlBySubItemID -> PX.Objects.AM.AMProdMatl (MatlLineID=LineID, OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID, InventoryID=InventoryID)
PX.Objects.AM.AMVendorShipLine.AMVendorShipmentByShipmentNbr -> PX.Objects.AM.AMVendorShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.AM.AMVendorShipLine.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.AM.AMVendorShipLine.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)

# PX.Objects.AM.AMVendorShipLineSplit (EntityType)

Label: "Vendor Shipment Line Split"
Key: LineNbr, ShipmentNbr, SplitLineNbr
Entity sets: PX_Objects_AM_AMVendorShipLineSplit, VendorShipmentLineSplit, AMVendorShipLineSplit
Non-filterable, non-selectable: LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.AM.AMVendorShipLineSplit.ShipmentNbr : Edm.String [key]
PX.Objects.AM.AMVendorShipLineSplit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.AMVendorShipLineSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.AM.AMVendorShipLineSplit.InvtMult : Edm.Int16
PX.Objects.AM.AMVendorShipLineSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMVendorShipLineSplit.IsStockItem : Edm.Boolean
PX.Objects.AM.AMVendorShipLineSplit.IsComponentItem : Edm.Boolean
PX.Objects.AM.AMVendorShipLineSplit.TranType : Edm.String
PX.Objects.AM.AMVendorShipLineSplit.TranDate : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipLineSplit.PlanID : Edm.Int64
PX.Objects.AM.AMVendorShipLineSplit.LotSerClassID : Edm.String
PX.Objects.AM.AMVendorShipLineSplit.AssignedNbr : Edm.String
PX.Objects.AM.AMVendorShipLineSplit.UOM : Edm.String "UOM"
PX.Objects.AM.AMVendorShipLineSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.AM.AMVendorShipLineSplit.BaseQty : Edm.Decimal
PX.Objects.AM.AMVendorShipLineSplit.ShipDate : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipLineSplit.Confirmed : Edm.Boolean "Confirmed"
PX.Objects.AM.AMVendorShipLineSplit.Released : Edm.Boolean "Released"
PX.Objects.AM.AMVendorShipLineSplit.IsUnassigned : Edm.Boolean [required]
PX.Objects.AM.AMVendorShipLineSplit.ProjectID : Edm.Int32
PX.Objects.AM.AMVendorShipLineSplit.TaskID : Edm.Int32
PX.Objects.AM.AMVendorShipLineSplit.CostCenterID : Edm.Int32
PX.Objects.AM.AMVendorShipLineSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMVendorShipLineSplit.CreatedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipLineSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMVendorShipLineSplit.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipLineSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipLineSplit.tstamp : Edm.Binary
PX.Objects.AM.AMVendorShipLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMVendorShipLineSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMVendorShipLineSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMVendorShipLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMVendorShipLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMVendorShipLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMVendorShipLineSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMVendorShipLineSplit.AMVendorShipLineByLineNbr -> PX.Objects.AM.AMVendorShipLine (ShipmentNbr=ShipmentNbr, LineNbr=LineNbr)
PX.Objects.AM.AMVendorShipLineSplit.AMVendorShipmentByShipmentNbr -> PX.Objects.AM.AMVendorShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.AM.AMVendorShipLineSplit.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID)

# PX.Objects.AM.AMVendorShipment (EntityType)

Label: "Vendor Shipment"
Key: ShipmentNbr
Entity sets: PX_Objects_AM_AMVendorShipment, VendorShipment, AMVendorShipment
Non-filterable, non-selectable: NoteText, CuryRate, CuryViewState

PX.Objects.AM.AMVendorShipment.ShipmentNbr : Edm.String [key] "Shipment ID"
PX.Objects.AM.AMVendorShipment.ShipmentType : Edm.String "Type"
PX.Objects.AM.AMVendorShipment.Status : Edm.String "Status"
PX.Objects.AM.AMVendorShipment.Hold : Edm.Boolean "Hold"
PX.Objects.AM.AMVendorShipment.ShipmentDate : Edm.DateTimeOffset "Shipment Date"
PX.Objects.AM.AMVendorShipment.VendorID : Edm.Int32 "Vendor"
PX.Objects.AM.AMVendorShipment.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.AM.AMVendorShipment.EmployeeID : Edm.Int32 "Owner"
PX.Objects.AM.AMVendorShipment.ShipAddressID : Edm.Int32 "ShipAddressID"
PX.Objects.AM.AMVendorShipment.ShipContactID : Edm.Int32 "ShipContactID"
PX.Objects.AM.AMVendorShipment.ShipDestType : Edm.String "Shipping Destination Type"
PX.Objects.AM.AMVendorShipment.ShipmentQty : Edm.Decimal [required] "Shipped Quantity"
PX.Objects.AM.AMVendorShipment.ControlQty : Edm.Decimal [required] "Control Quantity"
PX.Objects.AM.AMVendorShipment.LineCntr : Edm.Int32 [required]
PX.Objects.AM.AMVendorShipment.Released : Edm.Boolean [required] "Released"
PX.Objects.AM.AMVendorShipment.NoteID : Edm.Guid
PX.Objects.AM.AMVendorShipment.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMVendorShipment.tstamp : Edm.Binary
PX.Objects.AM.AMVendorShipment.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMVendorShipment.CreatedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMVendorShipment.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipment.BatNbr : Edm.String "Batch Nbr"
PX.Objects.AM.AMVendorShipment.ShipVia : Edm.String "Ship Via"
PX.Objects.AM.AMVendorShipment.FOBPoint : Edm.String "FOB Point"
PX.Objects.AM.AMVendorShipment.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.AM.AMVendorShipment.ShipZoneID : Edm.String "Shipping Zone ID"
PX.Objects.AM.AMVendorShipment.Residential : Edm.Boolean [required] "Residential Delivery"
PX.Objects.AM.AMVendorShipment.SaturdayDelivery : Edm.Boolean [required] "Saturday Delivery"
PX.Objects.AM.AMVendorShipment.Insurance : Edm.Boolean [required] "Insurance"
PX.Objects.AM.AMVendorShipment.GroundCollect : Edm.Boolean [required] "Ground Collect"
PX.Objects.AM.AMVendorShipment.CuryID : Edm.String "Freight Currency"
PX.Objects.AM.AMVendorShipment.CuryInfoID : Edm.Int64
PX.Objects.AM.AMVendorShipment.FreightCost : Edm.Decimal "Freight Cost"
PX.Objects.AM.AMVendorShipment.CuryFreightCost : Edm.Decimal [required] "Freight Cost"
PX.Objects.AM.AMVendorShipment.OverrideFreightAmount : Edm.Boolean [required] "Override Freight Price"
PX.Objects.AM.AMVendorShipment.OrderCntr : Edm.Int32
PX.Objects.AM.AMVendorShipment.FreightAmountSource : Edm.String "Invoice Freight Price Based On"
PX.Objects.AM.AMVendorShipment.FreightAmt : Edm.Decimal "Freight Price"
PX.Objects.AM.AMVendorShipment.CuryFreightAmt : Edm.Decimal [required] "Freight Price"
PX.Objects.AM.AMVendorShipment.CuryRate : Edm.Decimal
PX.Objects.AM.AMVendorShipment.CuryViewState : Edm.Boolean
PX.Objects.AM.AMVendorShipment.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.AM.AMVendorShipment.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AM.AMVendorShipment.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AM.AMVendorShipment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMVendorShipment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMVendorShipment.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.AM.AMVendorShipment.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.AM.AMVendorShipment.FOBPointByFOBPoint -> PX.Objects.CS.FOBPoint (FOBPoint=FOBPointID)
PX.Objects.AM.AMVendorShipment.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.AM.AMVendorShipment.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.AM.AMVendorShipment.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMVendorShipment.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AM.AMVendorShipment.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.AM.AMVendorShipment.LocationByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.AM.AMVendorShipment.AMVendorShipmentAddressByShipAddressID -> PX.Objects.AM.AMVendorShipmentAddress (ShipAddressID=AddressID)
PX.Objects.AM.AMVendorShipment.AMVendorShipmentContactByShipContactID -> PX.Objects.AM.AMVendorShipmentContact (ShipContactID=ContactID)
PX.Objects.AM.AMVendorShipment.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.AM.AMVendorShipment.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)

# PX.Objects.AM.AMVendorShipmentAddress (EntityType)

Label: "Vendor Shipment Address"
Key: AddressID
Entity sets: PX_Objects_AM_AMVendorShipmentAddress, VendorShipmentAddress, AMVendorShipmentAddress
Non-filterable, non-selectable: OverrideAddress

PX.Objects.AM.AMVendorShipmentAddress.AddressID : Edm.Int32 [key]
PX.Objects.AM.AMVendorShipmentAddress.BAccountID : Edm.Int32
PX.Objects.AM.AMVendorShipmentAddress.BAccountAddressID : Edm.Int32
PX.Objects.AM.AMVendorShipmentAddress.IsDefaultAddress : Edm.Boolean [required] "Is Default Address"
PX.Objects.AM.AMVendorShipmentAddress.OverrideAddress : Edm.Boolean "Override"
PX.Objects.AM.AMVendorShipmentAddress.RevisionID : Edm.Int32 "RevisionID"
PX.Objects.AM.AMVendorShipmentAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.AM.AMVendorShipmentAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.AM.AMVendorShipmentAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.AM.AMVendorShipmentAddress.City : Edm.String "City"
PX.Objects.AM.AMVendorShipmentAddress.CountryID : Edm.String "Country"
PX.Objects.AM.AMVendorShipmentAddress.State : Edm.String "State"
PX.Objects.AM.AMVendorShipmentAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.AM.AMVendorShipmentAddress.Department : Edm.String "Department"
PX.Objects.AM.AMVendorShipmentAddress.SubDepartment : Edm.String "Subdepartment"
PX.Objects.AM.AMVendorShipmentAddress.StreetName : Edm.String "Street Name"
PX.Objects.AM.AMVendorShipmentAddress.BuildingNumber : Edm.String "Building Number"
PX.Objects.AM.AMVendorShipmentAddress.BuildingName : Edm.String "Building Name"
PX.Objects.AM.AMVendorShipmentAddress.Floor : Edm.String "Floor"
PX.Objects.AM.AMVendorShipmentAddress.UnitNumber : Edm.String "Unit Number"
PX.Objects.AM.AMVendorShipmentAddress.PostBox : Edm.String "Post Box"
PX.Objects.AM.AMVendorShipmentAddress.Room : Edm.String "Room"
PX.Objects.AM.AMVendorShipmentAddress.TownLocationName : Edm.String "Town Location Name"
PX.Objects.AM.AMVendorShipmentAddress.DistrictName : Edm.String "District Name"
PX.Objects.AM.AMVendorShipmentAddress.AddressType : Edm.String "Address Type"
PX.Objects.AM.AMVendorShipmentAddress.CareOf : Edm.String "Care Of"
PX.Objects.AM.AMVendorShipmentAddress.NoteID : Edm.Guid
PX.Objects.AM.AMVendorShipmentAddress.tstamp : Edm.Binary
PX.Objects.AM.AMVendorShipmentAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMVendorShipmentAddress.CreatedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipmentAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipmentAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMVendorShipmentAddress.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipmentAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMVendorShipmentAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMVendorShipmentAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMVendorShipmentAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.AM.AMVendorShipmentAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.AM.AMVendorShipmentAddress.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)

# PX.Objects.AM.AMVendorShipmentContact (EntityType)

Label: "Vendor Shipment Contact"
Key: ContactID
Entity sets: PX_Objects_AM_AMVendorShipmentContact, VendorShipmentContact, AMVendorShipmentContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.AM.AMVendorShipmentContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.AM.AMVendorShipmentContact.BAccountID : Edm.Int32
PX.Objects.AM.AMVendorShipmentContact.BAccountContactID : Edm.Int32
PX.Objects.AM.AMVendorShipmentContact.IsDefaultContact : Edm.Boolean [required] "Default Customer Contact"
PX.Objects.AM.AMVendorShipmentContact.OverrideContact : Edm.Boolean "Override Contact"
PX.Objects.AM.AMVendorShipmentContact.RevisionID : Edm.Int32 "RevisionID"
PX.Objects.AM.AMVendorShipmentContact.Title : Edm.String "Title"
PX.Objects.AM.AMVendorShipmentContact.Salutation : Edm.String "Job Title"
PX.Objects.AM.AMVendorShipmentContact.Attention : Edm.String "Attention"
PX.Objects.AM.AMVendorShipmentContact.FullName : Edm.String "Account Name"
PX.Objects.AM.AMVendorShipmentContact.Email : Edm.String "Email"
PX.Objects.AM.AMVendorShipmentContact.Fax : Edm.String "Fax"
PX.Objects.AM.AMVendorShipmentContact.FaxType : Edm.String "Fax"
PX.Objects.AM.AMVendorShipmentContact.Phone1 : Edm.String "Phone 1"
PX.Objects.AM.AMVendorShipmentContact.Phone1Type : Edm.String "Phone 1"
PX.Objects.AM.AMVendorShipmentContact.Phone2 : Edm.String "Phone 2"
PX.Objects.AM.AMVendorShipmentContact.Phone2Type : Edm.String "Phone 2"
PX.Objects.AM.AMVendorShipmentContact.Phone3 : Edm.String "Phone 3"
PX.Objects.AM.AMVendorShipmentContact.Phone3Type : Edm.String "Phone 3"
PX.Objects.AM.AMVendorShipmentContact.NoteID : Edm.Guid
PX.Objects.AM.AMVendorShipmentContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMVendorShipmentContact.CreatedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipmentContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AM.AMVendorShipmentContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMVendorShipmentContact.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMVendorShipmentContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AM.AMVendorShipmentContact.tstamp : Edm.Binary
PX.Objects.AM.AMVendorShipmentContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMVendorShipmentContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMVendorShipmentContact.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)

# PX.Objects.AM.AMWC (EntityType)

Label: "Work Center"
Key: WcID
Entity sets: PX_Objects_AM_AMWC, WorkCenter, AMWC
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMWC.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWC.ActiveFlg : Edm.Boolean [required] "Active"
PX.Objects.AM.AMWC.BflushLbr : Edm.Boolean [required] "Backflush Labor"
PX.Objects.AM.AMWC.BflushMatl : Edm.Boolean [required] "Backflush Materials"
PX.Objects.AM.AMWC.Descr : Edm.String "Description"
PX.Objects.AM.AMWC.NoteID : Edm.Guid
PX.Objects.AM.AMWC.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMWC.DepartmentID : Edm.String "Manufacturing Department ID"
PX.Objects.AM.AMWC.OutsideFlg : Edm.Boolean [required] "Outside Process"
PX.Objects.AM.AMWC.StdCost : Edm.Decimal [required] "Standard Cost"
PX.Objects.AM.AMWC.WcBasis : Edm.String "Basis for Capacity"
PX.Objects.AM.AMWC.DefaultQueueTime : Edm.Int32 [required] "Default Queue Time"
PX.Objects.AM.AMWC.DefaultFinishTime : Edm.Int32 [required] "Default Finish Time"
PX.Objects.AM.AMWC.DefaultMoveTime : Edm.Int32 [required] "Default Move Time"
PX.Objects.AM.AMWC.tstamp : Edm.Binary
PX.Objects.AM.AMWC.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWC.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWC.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWC.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWC.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWC.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWC.ScrapAction : Edm.Int32 [required] "Scrap Action Default"
PX.Objects.AM.AMWC.AllowMultiClockEntry : Edm.Boolean [required] "Allow Clock Entry for Multiple Production Orders"
PX.Objects.AM.AMWC.ControlPoint : Edm.Boolean [required] "Control Point"
PX.Objects.AM.AMWC.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMWC.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMWC.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMWC.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMWC.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMWC.AMDepartmentByDepartmentID -> PX.Objects.AM.AMDepartment (DepartmentID=DepartmentID)
PX.Objects.AM.AMWC.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.AM.AMWC.AMWCSchdCollection -> Collection(PX.Objects.AM.AMWCSchd)
PX.Objects.AM.AMWC.AMWCSchdDetailCollection -> Collection(PX.Objects.AM.AMWCSchdDetail)
PX.Objects.AM.AMWC.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.Objects.AM.AMWC.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.AM.AMWC.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.Objects.AM.AMWC.AMEstimateSetupCollection -> Collection(PX.Objects.AM.AMEstimateSetup)
PX.Objects.AM.AMWC.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.Objects.AM.AMWC.AMShiftCollection -> Collection(PX.Objects.AM.AMShift)
PX.Objects.AM.AMWC.AMWCCalendarPeriodCollection -> Collection(PX.Objects.AM.AMWCCalendarPeriod)
PX.Objects.AM.AMWC.AMWCCurySettingsCollection -> Collection(PX.Objects.AM.AMWCCurySettings)
PX.Objects.AM.AMWC.AMWCMachCollection -> Collection(PX.Objects.AM.AMWCMach)
PX.Objects.AM.AMWC.AMWCOvhdCollection -> Collection(PX.Objects.AM.AMWCOvhd)
PX.Objects.AM.AMWC.AMWCSubstituteCollection -> Collection(PX.Objects.AM.AMWCSubstitute)
PX.Objects.AM.AMWC.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.Objects.AM.AMWC.AMWCCuryCollection -> Collection(PX.Objects.AM.AMWCCury)
PX.Objects.AM.AMWC.AMBSetupCollection -> Collection(PX.Objects.AM.AMBSetup)

# PX.Objects.AM.AMWCCalendarPeriod (EntityType)

Label: "Work Center Calendar Period"
Key: SequenceNbr, WcID
Entity sets: PX_Objects_AM_AMWCCalendarPeriod, WorkCenterCalendarPeriod, AMWCCalendarPeriod
Non-filterable, non-selectable: ShiftPriority

PX.Objects.AM.AMWCCalendarPeriod.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWCCalendarPeriod.SequenceNbr : Edm.Int32 [key]
PX.Objects.AM.AMWCCalendarPeriod.DayOfWeek : Edm.Int32 [required]
PX.Objects.AM.AMWCCalendarPeriod.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.AMWCCalendarPeriod.EndTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCCalendarPeriod.Efficiency : Edm.Decimal [required]
PX.Objects.AM.AMWCCalendarPeriod.CrewSize : Edm.Decimal [required]
PX.Objects.AM.AMWCCalendarPeriod.CapacityMinutes : Edm.Int32 [required]
PX.Objects.AM.AMWCCalendarPeriod.PeriodType : Edm.String
PX.Objects.AM.AMWCCalendarPeriod.ShiftCD : Edm.String
PX.Objects.AM.AMWCCalendarPeriod.CalendarID : Edm.String
PX.Objects.AM.AMWCCalendarPeriod.Date : Edm.DateTimeOffset
PX.Objects.AM.AMWCCalendarPeriod.ShiftPriority : Edm.Int32
PX.Objects.AM.AMWCCalendarPeriod.tstamp : Edm.Binary
PX.Objects.AM.AMWCCalendarPeriod.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCCalendarPeriod.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCCalendarPeriod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCCalendarPeriod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCCalendarPeriod.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCCalendarPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCCalendarPeriod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMWCCalendarPeriod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMWCCalendarPeriod.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)

# PX.Objects.AM.AMWCCury (EntityType)

Label: "AMWCCurrency"
Key: CuryID, DetailID, WcID
Entity sets: PX_Objects_AM_AMWCCury, AMWCCurrency, AMWCCury

PX.Objects.AM.AMWCCury.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWCCury.DetailID : Edm.String [key] "Detail"
PX.Objects.AM.AMWCCury.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMWCCury.StdCost : Edm.Decimal "Standard Cost"
PX.Objects.AM.AMWCCury.tstamp : Edm.Binary
PX.Objects.AM.AMWCCury.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCCury.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCCury.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCCury.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCCury.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCCury.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCCury.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMWCCury.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)

# PX.Objects.AM.AMWCCurySettings (EntityType)

Label: "Work Center Currency Settings"
Key: CuryID, DetailID, WcID
Entity sets: PX_Objects_AM_AMWCCurySettings, WorkCenterCurrencySettings, AMWCCurySettings

PX.Objects.AM.AMWCCurySettings.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWCCurySettings.DetailID : Edm.String [key] "Detail"
PX.Objects.AM.AMWCCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMWCCurySettings.StdCost : Edm.Decimal [required] "Standard Cost"
PX.Objects.AM.AMWCCurySettings.tstamp : Edm.Binary
PX.Objects.AM.AMWCCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCCurySettings.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCCurySettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCCurySettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMWCCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMWCCurySettings.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMWCCurySettings.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)

# PX.Objects.AM.AMWCMach (EntityType)

Label: "Work Center Machines"
Key: MachID, WcID
Entity sets: PX_Objects_AM_AMWCMach, WorkCenterMachines, AMWCMach
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMWCMach.MachID : Edm.String [key] "Machine ID"
PX.Objects.AM.AMWCMach.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWCMach.NoteID : Edm.Guid
PX.Objects.AM.AMWCMach.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMWCMach.StdCost : Edm.Decimal [required] "Standard Cost"
PX.Objects.AM.AMWCMach.MachineOverride : Edm.Boolean [required] "Machine Override"
PX.Objects.AM.AMWCMach.tstamp : Edm.Binary
PX.Objects.AM.AMWCMach.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCMach.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCMach.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCMach.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCMach.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCMach.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCMach.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMWCMach.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMWCMach.AccountByMachAcctID -> PX.Objects.GL.Account
PX.Objects.AM.AMWCMach.SubByMachSubID -> PX.Objects.GL.Sub
PX.Objects.AM.AMWCMach.AMMachByMachID -> PX.Objects.AM.AMMach (MachID=MachID)
PX.Objects.AM.AMWCMach.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)
PX.Objects.AM.AMWCMach.AMWCMachCuryCollection -> Collection(PX.Objects.AM.AMWCMachCury)

# PX.Objects.AM.AMWCMachCury (EntityType)

Label: "AMWCMachCury"
Key: CuryID, DetailID, WcID
Entity sets: PX_Objects_AM_AMWCMachCury, AMWCMachCury

PX.Objects.AM.AMWCMachCury.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWCMachCury.DetailID : Edm.String [key] "Detail"
PX.Objects.AM.AMWCMachCury.CuryID : Edm.String [key] "Currency"
PX.Objects.AM.AMWCMachCury.StdCost : Edm.Decimal "Standard Cost"
PX.Objects.AM.AMWCMachCury.tstamp : Edm.Binary
PX.Objects.AM.AMWCMachCury.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCMachCury.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCMachCury.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCMachCury.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCMachCury.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCMachCury.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCMachCury.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AM.AMWCMachCury.AMWCMachByWcID -> PX.Objects.AM.AMWCMach (DetailID=MachID, WcID=WcID)

# PX.Objects.AM.AMWCOvhd (EntityType)

Label: "Work Center Overheads"
Key: OvhdID, WcID
Entity sets: PX_Objects_AM_AMWCOvhd, WorkCenterOverheads, AMWCOvhd
Non-filterable, non-selectable: NoteText

PX.Objects.AM.AMWCOvhd.NoteID : Edm.Guid
PX.Objects.AM.AMWCOvhd.NoteText : Edm.String "Note Text"
PX.Objects.AM.AMWCOvhd.OFactor : Edm.Decimal [required] "Factor"
PX.Objects.AM.AMWCOvhd.OvhdID : Edm.String [key] "Overhead ID"
PX.Objects.AM.AMWCOvhd.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWCOvhd.tstamp : Edm.Binary
PX.Objects.AM.AMWCOvhd.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCOvhd.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCOvhd.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCOvhd.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCOvhd.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCOvhd.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCOvhd.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMWCOvhd.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMWCOvhd.AMOverheadByOvhdID -> PX.Objects.AM.AMOverhead (OvhdID=OvhdID)
PX.Objects.AM.AMWCOvhd.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)

# PX.Objects.AM.AMWCSchd (EntityType)

Label: "Work Center Schedule"
Key: SchdDate, ShiftCD, WcID
Entity sets: PX_Objects_AM_AMWCSchd, WorkCenterSchedule1, AMWCSchd
Non-filterable, non-selectable: ResourceID

PX.Objects.AM.AMWCSchd.ResourceID : Edm.String "Resource ID"
PX.Objects.AM.AMWCSchd.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWCSchd.ShiftCD : Edm.String [key] "Shift"
PX.Objects.AM.AMWCSchd.SchdDate : Edm.DateTimeOffset [key] "Schedule Date"
PX.Objects.AM.AMWCSchd.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.AMWCSchd.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.AMWCSchd.WorkTime : Edm.Int32 [required] "Work Time"
PX.Objects.AM.AMWCSchd.TotalBlocks : Edm.Int32 [required] "Total Blocks"
PX.Objects.AM.AMWCSchd.SchdTime : Edm.Int32 [required] "Schedule Time"
PX.Objects.AM.AMWCSchd.PlanBlocks : Edm.Int32 [required] "Plan Blocks"
PX.Objects.AM.AMWCSchd.ExceptionDate : Edm.Boolean [required] "Exception Date"
PX.Objects.AM.AMWCSchd.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCSchd.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCSchd.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCSchd.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCSchd.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCSchd.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCSchd.tstamp : Edm.Binary
PX.Objects.AM.AMWCSchd.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMWCSchd.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMWCSchd.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMWCSchd.EPShiftCodeByShiftCD -> PX.Objects.EP.EPShiftCode (ShiftCD=ShiftCD)
PX.Objects.AM.AMWCSchd.AMShiftByShiftCD -> PX.Objects.AM.AMShift (WcID=ShiftCD, ShiftCD=WcID)
PX.Objects.AM.AMWCSchd.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)
PX.Objects.AM.AMWCSchd.AMWCSchdDetailCollection -> Collection(PX.Objects.AM.AMWCSchdDetail)

# PX.Objects.AM.AMWCSchdDetail (EntityType)

Label: "Work Center Schedule Detail"
Key: RecordID
Entity sets: PX_Objects_AM_AMWCSchdDetail, WorkCenterScheduleDetail, AMWCSchdDetail
Non-filterable, non-selectable: ResourceID

PX.Objects.AM.AMWCSchdDetail.ResourceID : Edm.String "Resource ID"
PX.Objects.AM.AMWCSchdDetail.ResourceSize : Edm.Decimal [required] "Resource Size"
PX.Objects.AM.AMWCSchdDetail.RecordID : Edm.Int64 [key] "Record ID"
PX.Objects.AM.AMWCSchdDetail.SchdKey : Edm.Guid "Schedule Key"
PX.Objects.AM.AMWCSchdDetail.WcID : Edm.String "Work Center"
PX.Objects.AM.AMWCSchdDetail.ShiftCD : Edm.String "Shift"
PX.Objects.AM.AMWCSchdDetail.SchdDate : Edm.DateTimeOffset "Schedule Date"
PX.Objects.AM.AMWCSchdDetail.OrderByDate : Edm.DateTimeOffset "Order By Date Time"
PX.Objects.AM.AMWCSchdDetail.Description : Edm.String "Description"
PX.Objects.AM.AMWCSchdDetail.QueueTime : Edm.Int32 [required] "Queue Time"
PX.Objects.AM.AMWCSchdDetail.FinishTime : Edm.Int32 [required] "Finish Time"
PX.Objects.AM.AMWCSchdDetail.MoveTime : Edm.Int32 [required] "Move Time"
PX.Objects.AM.AMWCSchdDetail.RunTimeBase : Edm.Int32 [required] "Run Time Without Efficiency"
PX.Objects.AM.AMWCSchdDetail.RunTime : Edm.Int32 [required] "Run Time"
PX.Objects.AM.AMWCSchdDetail.SchdTime : Edm.Int32 [required] "Schedule Time"
PX.Objects.AM.AMWCSchdDetail.PlanBlocks : Edm.Int32 [required] "Plan Blocks"
PX.Objects.AM.AMWCSchdDetail.IsBreak : Edm.Boolean [required] "Break"
PX.Objects.AM.AMWCSchdDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCSchdDetail.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCSchdDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCSchdDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCSchdDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCSchdDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCSchdDetail.tstamp : Edm.Binary
PX.Objects.AM.AMWCSchdDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMWCSchdDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMWCSchdDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMWCSchdDetail.EPShiftCodeByShiftCD -> PX.Objects.EP.EPShiftCode (ShiftCD=ShiftCD)
PX.Objects.AM.AMWCSchdDetail.AMShiftByShiftCD -> PX.Objects.AM.AMShift (WcID=ShiftCD, ShiftCD=WcID)
PX.Objects.AM.AMWCSchdDetail.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)
PX.Objects.AM.AMWCSchdDetail.AMWCSchdBySchdDate -> PX.Objects.AM.AMWCSchd (WcID=WcID, ShiftCD=ShiftCD, SchdDate=SchdDate)

# PX.Objects.AM.AMWCSubstitute (EntityType)

Label: "Work Center Substitute"
Key: SiteID, WcID
Entity sets: PX_Objects_AM_AMWCSubstitute, WorkCenterSubstitute, AMWCSubstitute

PX.Objects.AM.AMWCSubstitute.WcID : Edm.String [key] "Work Center"
PX.Objects.AM.AMWCSubstitute.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.AMWCSubstitute.SubstituteWcID : Edm.String "Substitute Work Center"
PX.Objects.AM.AMWCSubstitute.UpdateOperDesc : Edm.Boolean [required] "Update Operation Description"
PX.Objects.AM.AMWCSubstitute.tstamp : Edm.Binary
PX.Objects.AM.AMWCSubstitute.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.AMWCSubstitute.CreatedByScreenID : Edm.String
PX.Objects.AM.AMWCSubstitute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCSubstitute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.AMWCSubstitute.LastModifiedByScreenID : Edm.String
PX.Objects.AM.AMWCSubstitute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.AMWCSubstitute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.AMWCSubstitute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AM.AMWCSubstitute.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.AMWCSubstitute.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)
PX.Objects.AM.AMWCSubstitute.AMWCBySubstituteWcID -> PX.Objects.AM.AMWC (SubstituteWcID=WcID)

# PX.Objects.AM.AMWrkMatl (EntityType)

Label: "Material Work Temp"
Key: AutoNbr
Entity sets: PX_Objects_AM_AMWrkMatl, MaterialWorkTemp, AMWrkMatl

PX.Objects.AM.AMWrkMatl.AutoNbr : Edm.Int32 [key] "AutoNbr"
PX.Objects.AM.AMWrkMatl.BFlush : Edm.Boolean [required] "BFlush"
PX.Objects.AM.AMWrkMatl.Descr : Edm.String "Descr"
PX.Objects.AM.AMWrkMatl.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.AMWrkMatl.LineID : Edm.Int32 [required] "Line ID"
PX.Objects.AM.AMWrkMatl.MatlQty : Edm.Decimal [required] "Release Qty."
PX.Objects.AM.AMWrkMatl.BaseMatlQty : Edm.Decimal [required] "Release Base Qty."
PX.Objects.AM.AMWrkMatl.OrderType : Edm.String "Order Type"
PX.Objects.AM.AMWrkMatl.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.AMWrkMatl.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.AMWrkMatl.OperationCD : Edm.String "Operation ID"
PX.Objects.AM.AMWrkMatl.QtyAvail : Edm.Decimal [required] "Available Qty."
PX.Objects.AM.AMWrkMatl.BaseQtyAvail : Edm.Decimal [required] "Available Qty."
PX.Objects.AM.AMWrkMatl.QtyReq : Edm.Decimal [required] "Required Qty."
PX.Objects.AM.AMWrkMatl.BaseQtyReq : Edm.Decimal [required] "Required Base Qty"
PX.Objects.AM.AMWrkMatl.UOM : Edm.String "UOM"
PX.Objects.AM.AMWrkMatl.UserID : Edm.Guid "Created By"
PX.Objects.AM.AMWrkMatl.IsByproduct : Edm.Boolean [required] "By-product"
PX.Objects.AM.AMWrkMatl.UnreleasedBatchQty : Edm.Decimal "Unreleased Batch Qty."
PX.Objects.AM.AMWrkMatl.BaseUnreleasedBatchQty : Edm.Decimal "Unreleased Batch Base Qty."
PX.Objects.AM.AMWrkMatl.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.AMWrkMatl.BaseQtyRemaining : Edm.Decimal "Remaining Base Qty."
PX.Objects.AM.AMWrkMatl.OverIssueMaterial : Edm.String "Over Issue Material"
PX.Objects.AM.AMWrkMatl.tstamp : Edm.Binary
PX.Objects.AM.AMWrkMatl.SubcontractSource : Edm.Int32 "Subcontract Source"
PX.Objects.AM.AMWrkMatl.CostCenterID : Edm.Int32
PX.Objects.AM.AMWrkMatl.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AM.AMWrkMatl.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.AM.AMWrkMatl.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.AMWrkMatl.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.AMWrkMatl.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.AM.AMWrkMatl.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.AMWrkMatl.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.AMWrkMatl.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AM.AMWrkMatl.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.AMWrkMatl.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.AMWrkMatl.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.AMWrkMatl.AMProdItemByOrderType -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID, OrderType=OrderType)

# PX.Objects.AM.BomInventoryItem (EntityType)

Label: "BOM Inventory Item"
BaseType: PX.Objects.IN.InventoryItem
Key: InventoryCD (inherited from PX.Objects.IN.InventoryItem)
Entity sets: PX_Objects_AM_BomInventoryItem, BOMInventoryItem

# PX.Objects.AM.BomWhereUsedDetail (EntityType)

Label: "BOM Where Used Detail"
Key: BOMID, LineID, OperationID, RevisionID, Sequence
Entity sets: PX_Objects_AM_BomWhereUsedDetail, BOMWhereUsedDetail
Non-filterable, non-selectable: NoteText, LineNbr, PlanCost, OriginalTreeNodeID, Level, QtyRequired, ItemClassID, Source, Description, ParentDescription, ParentItemClassID, Sequence, BOMStatus, EffStartDate, EffEndDate

PX.Objects.AM.BomWhereUsedDetail.BOMID : Edm.String [key] "BOM ID"
PX.Objects.AM.BomWhereUsedDetail.RevisionID : Edm.String [key] "Revision"
PX.Objects.AM.BomWhereUsedDetail.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.BomWhereUsedDetail.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.BomWhereUsedDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.BomWhereUsedDetail.Descr : Edm.String "Description"
PX.Objects.AM.BomWhereUsedDetail.QtyReq : Edm.Decimal "Required Qty."
PX.Objects.AM.BomWhereUsedDetail.UOM : Edm.String "UOM"
PX.Objects.AM.BomWhereUsedDetail.BaseQty : Edm.Decimal "Base Qty"
PX.Objects.AM.BomWhereUsedDetail.MaterialType : Edm.Int32 "Material Type"
PX.Objects.AM.BomWhereUsedDetail.PhantomRouting : Edm.Int32 "Phantom Routing"
PX.Objects.AM.BomWhereUsedDetail.BFlush : Edm.Boolean "Backflush Materials"
PX.Objects.AM.BomWhereUsedDetail.CompBOMRevisionID : Edm.String "Comp. BOM Revision"
PX.Objects.AM.BomWhereUsedDetail.ScrapFactor : Edm.Decimal "Scrap Factor"
PX.Objects.AM.BomWhereUsedDetail.BubbleNbr : Edm.String "Bubble Nbr."
PX.Objects.AM.BomWhereUsedDetail.EffDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AM.BomWhereUsedDetail.ExpDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AM.BomWhereUsedDetail.NoteID : Edm.Guid
PX.Objects.AM.BomWhereUsedDetail.NoteText : Edm.String "Note Text"
PX.Objects.AM.BomWhereUsedDetail.tstamp : Edm.Binary
PX.Objects.AM.BomWhereUsedDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.BomWhereUsedDetail.CreatedByScreenID : Edm.String
PX.Objects.AM.BomWhereUsedDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AM.BomWhereUsedDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AM.BomWhereUsedDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AM.BomWhereUsedDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AM.BomWhereUsedDetail.LineNbr : Edm.Int32 "Line Nbr. 2"
PX.Objects.AM.BomWhereUsedDetail.SortOrder : Edm.Int32 "Line Order"
PX.Objects.AM.BomWhereUsedDetail.BatchSize : Edm.Decimal "Batch Size"
PX.Objects.AM.BomWhereUsedDetail.PlanCost : Edm.Decimal "Planned Cost"
PX.Objects.AM.BomWhereUsedDetail.LineCntrRef : Edm.Int32
PX.Objects.AM.BomWhereUsedDetail.RowStatus : Edm.Int32 "Change Status"
PX.Objects.AM.BomWhereUsedDetail.SubcontractSource : Edm.Int32 "Subcontract Source"
PX.Objects.AM.BomWhereUsedDetail.IsStockItem : Edm.Boolean "Stock"
PX.Objects.AM.BomWhereUsedDetail.OriginalTreeNodeID : Edm.String "Original Tree Node"
PX.Objects.AM.BomWhereUsedDetail.UnitCost : Edm.Decimal
PX.Objects.AM.BomWhereUsedDetail.Level : Edm.Int32 "Level"
PX.Objects.AM.BomWhereUsedDetail.ParentInventoryID : Edm.Int32 "Parent Inventory ID"
PX.Objects.AM.BomWhereUsedDetail.QtyRequired : Edm.Decimal "Required Qty."
PX.Objects.AM.BomWhereUsedDetail.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.BomWhereUsedDetail.Source : Edm.String
PX.Objects.AM.BomWhereUsedDetail.Description : Edm.String "Description"
PX.Objects.AM.BomWhereUsedDetail.ParentDescription : Edm.String "Parent Desc."
PX.Objects.AM.BomWhereUsedDetail.ParentItemClassID : Edm.Int32 "Parent Item Class"
PX.Objects.AM.BomWhereUsedDetail.Sequence : Edm.Int32 [key] "Sequence"
PX.Objects.AM.BomWhereUsedDetail.CompBOMID : Edm.String "Comp. BOM ID"
PX.Objects.AM.BomWhereUsedDetail.BOMStatus : Edm.String "Revision Status"
PX.Objects.AM.BomWhereUsedDetail.EffStartDate : Edm.DateTimeOffset "Revision Start Date"
PX.Objects.AM.BomWhereUsedDetail.EffEndDate : Edm.DateTimeOffset "Revision End Date"

# PX.Objects.AM.CacheExtensions.INItemPlanAMExtension (EntityType)

Label: "AM Item Plan"
Key: InventoryID, PlanID
Entity sets: PX_Objects_AM_CacheExtensions_INItemPlanAMExtension, AMItemPlan, INItemPlanAMExtension

PX.Objects.AM.CacheExtensions.INItemPlanAMExtension.PlanID : Edm.Int64 [key]
PX.Objects.AM.CacheExtensions.INItemPlanAMExtension.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AM.CacheExtensions.INItemPlanAMExtension.AMSoftSupplyPlanID : Edm.Int64
PX.Objects.AM.CacheExtensions.INItemPlanAMExtension.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.CacheExtensions.INItemPlanAMExtension.INItemPlanByInventoryID -> PX.Objects.IN.INItemPlan (PlanID=PlanID, InventoryID=InventoryID)
PX.Objects.AM.CacheExtensions.INItemPlanAMExtension.INSiteBySiteID -> PX.Objects.IN.INSite

# PX.Objects.AM.PrintProductionOrders (EntityType)

Label: "Print Production Orders"
BaseType: PX.Objects.AM.AMProdItem
Key: OrderType, ProdOrdID (inherited from PX.Objects.AM.AMProdItem)
Entity sets: PX_Objects_AM_PrintProductionOrders, PrintProductionOrders

PX.Objects.AM.PrintProductionOrders.ProductionReportID : Edm.String "Print Production Report ID"

# PX.Objects.AM.ProdOperAdjusted (EntityType)

Label: "Production Operation Adjusted"
Key: OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_ProdOperAdjusted, ProductionOperationAdjusted, ProdOperAdjusted
Non-filterable, non-selectable: StatusIDAdjusted

PX.Objects.AM.ProdOperAdjusted.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.ProdOperAdjusted.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.ProdOperAdjusted.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.ProdOperAdjusted.OperationCD : Edm.String "Operation ID"
PX.Objects.AM.ProdOperAdjusted.Descr : Edm.String "Operation Description"
PX.Objects.AM.ProdOperAdjusted.WcID : Edm.String "Work Center"
PX.Objects.AM.ProdOperAdjusted.StatusID : Edm.String "Status"
PX.Objects.AM.ProdOperAdjusted.QtytoProd : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.ProdOperAdjusted.QtytoProdAdjusted : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.ProdOperAdjusted.BaseQtytoProd : Edm.Decimal "Base Qty. to Produce"
PX.Objects.AM.ProdOperAdjusted.BaseQtytoProdAdjusted : Edm.Decimal "Base Qty. to Produce"
PX.Objects.AM.ProdOperAdjusted.QtyComplete : Edm.Decimal "Completed Qty."
PX.Objects.AM.ProdOperAdjusted.QtyCompleteAdjusted : Edm.Decimal "Completed Qty."
PX.Objects.AM.ProdOperAdjusted.BaseQtyComplete : Edm.Decimal "Completed Base Qty."
PX.Objects.AM.ProdOperAdjusted.BaseQtyCompleteAdjusted : Edm.Decimal "Completed Base Qty."
PX.Objects.AM.ProdOperAdjusted.QtyScrapped : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.ProdOperAdjusted.QtyScrappedAdjusted : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.ProdOperAdjusted.BaseQtyScrapped : Edm.Decimal "Scrapped Base Qty."
PX.Objects.AM.ProdOperAdjusted.BaseQtyScrappedAdjusted : Edm.Decimal "Scrapped Base Qty."
PX.Objects.AM.ProdOperAdjusted.TotalQty : Edm.Decimal "Total Qty."
PX.Objects.AM.ProdOperAdjusted.TotalQtyAdjusted : Edm.Decimal "Total Qty."
PX.Objects.AM.ProdOperAdjusted.BaseTotalQty : Edm.Decimal "Base Total Qty."
PX.Objects.AM.ProdOperAdjusted.BaseTotalQtyAdjusted : Edm.Decimal "Base Total Qty."
PX.Objects.AM.ProdOperAdjusted.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.ProdOperAdjusted.QtyRemainingAdjusted : Edm.Decimal "Remaining Qty."
PX.Objects.AM.ProdOperAdjusted.BaseQtyRemaining : Edm.Decimal "Remaining Base Qty."
PX.Objects.AM.ProdOperAdjusted.BaseQtyRemainingAdjusted : Edm.Decimal "Remaining Base Qty."
PX.Objects.AM.ProdOperAdjusted.StatusIDAdjusted : Edm.String "Status"

# PX.Objects.AM.ProdOperMatl (EntityType)

Label: "Production Operations & Materials"
BaseType: PX.Objects.AM.AMProdOper
Key: OperationCD, OrderType, ProdOrdID (inherited from PX.Objects.AM.AMProdOper)
Entity sets: PX_Objects_AM_ProdOperMatl, ProductionOperationsMaterials, ProdOperMatl
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.AM.ProdOperMatl.OperUOM : Edm.String "UOM"
PX.Objects.AM.ProdOperMatl.OperationEventCD : Edm.String "OperationEventCD"
PX.Objects.AM.ProdOperMatl.OperMatlLineID : Edm.Int32 "OperMatlLineID"
PX.Objects.AM.ProdOperMatl.LackOfMaterials : Edm.Boolean "Lack Of Materials"
PX.Objects.AM.ProdOperMatl.POPromiseDate : Edm.DateTimeOffset "Promised On"
PX.Objects.AM.ProdOperMatl.MaterialID : Edm.Int32 "Material ID"
PX.Objects.AM.ProdOperMatl.MaterialCD : Edm.String "MaterialCD"
PX.Objects.AM.ProdOperMatl.MatlDescr : Edm.String "Description"
PX.Objects.AM.ProdOperMatl.ReceivedDescr : Edm.String "ReceivedDescr"
PX.Objects.AM.ProdOperMatl.IssuedDescr : Edm.String "IssuedDescr"
PX.Objects.AM.ProdOperMatl.MaterialScheduledStart : Edm.DateTimeOffset "Material Scheduled Start"
PX.Objects.AM.ProdOperMatl.MaterialScheduledEnd : Edm.DateTimeOffset "Material Scheduled End"
PX.Objects.AM.ProdOperMatl.RequiredMaterialQty : Edm.Decimal "Required Material Qty."
PX.Objects.AM.ProdOperMatl.IssuedMaterialQty : Edm.Decimal "Issued Material Qty."
PX.Objects.AM.ProdOperMatl.RemainingMaterialQty : Edm.Decimal "Remaining Material Qty."
PX.Objects.AM.ProdOperMatl.MaterialUOM : Edm.String "Material UOM"
PX.Objects.AM.ProdOperMatl.IsMatlPOLinked : Edm.Boolean "IsMatlPOLinked"
PX.Objects.AM.ProdOperMatl.MatlPOOrderType : Edm.String "MatlPOOrderType"
PX.Objects.AM.ProdOperMatl.MatlPOOrderNbr : Edm.String "Purchase Order"
PX.Objects.AM.ProdOperMatl.MatlPOPromiseDate : Edm.DateTimeOffset "Promised On"
PX.Objects.AM.ProdOperMatl.MatlPOOrderQty : Edm.Decimal "Order Qty."
PX.Objects.AM.ProdOperMatl.MatlPOOpenQty : Edm.Decimal "Open Qty."
PX.Objects.AM.ProdOperMatl.MatlPOLineDescr : Edm.String "Line Desc."
PX.Objects.AM.ProdOperMatl.MatlPOUOM : Edm.String "UOM"
PX.Objects.AM.ProdOperMatl.MatlPOVendorID : Edm.Int32 "Vendor"
PX.Objects.AM.ProdOperMatl.MaterialType : Edm.Int32 "Material Type"
PX.Objects.AM.ProdOperMatl.MatlSubcontractSource : Edm.Int32 "Subcontract Source"
PX.Objects.AM.ProdOperMatl.MaterialMarkFor : Edm.Int32 "Mark For"
PX.Objects.AM.ProdOperMatl.SupplyOrderType : Edm.String "SupplyOrderType"
PX.Objects.AM.ProdOperMatl.SupplyProdOrdID : Edm.String "SupplyProdOrdID"
PX.Objects.AM.ProdOperMatl.IsMatlRegularStockWBom : Edm.Boolean "IsMatlRegularStockWBom"
PX.Objects.AM.ProdOperMatl.IsMatlRegularStockWOBom : Edm.Boolean "IsMatlRegularStockWOBom"
PX.Objects.AM.ProdOperMatl.IsMatlSubCWBomMFG : Edm.Boolean "IsMatlSubCWBomMFG"
PX.Objects.AM.ProdOperMatl.IsMatlSubCWOBomMFG : Edm.Boolean "IsMatlSubCWOBomMFG"
PX.Objects.AM.ProdOperMatl.IsMatlRegularNS : Edm.Boolean "IsMatlRegularNS"
PX.Objects.AM.ProdOperMatl.IsMatlSubCNS : Edm.Boolean "IsMatlSubCNS"

# PX.Objects.AM.ProductionOrderBuildCapabilityMaterial (EntityType)

Label: "Production Order Build Capability Material"
Key: ProdOrdID
Entity sets: PX_Objects_AM_ProductionOrderBuildCapabilityMaterial, ProductionOrderBuildCapabilityMaterial

PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.OrderType : Edm.String "Order Type"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.QtyReq : Edm.Decimal "Required Qty."
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.UOM : Edm.String "UOM"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.QtyToProd : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.CostCenterID : Edm.Int32
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.TaskID : Edm.Int32 "Task"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.MaxQtyToProdNonCalcMatl : Edm.Decimal "Max Qty. to Produce"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.MaxQtyToProd : Edm.Decimal "Max Qty. to Produce"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMOrderTypeByParentOrderType -> PX.Objects.AM.AMOrderType
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMOrderTypeByProductOrderType -> PX.Objects.AM.AMOrderType
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMOrderTypeBySourceOrderType -> PX.Objects.AM.AMOrderType
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdAttributeCollection -> Collection(PX.Objects.AM.AMProdAttribute)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdEvntCollection -> Collection(PX.Objects.AM.AMProdEvnt)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdMatlLotSerialCollection -> Collection(PX.Objects.AM.AMProdMatlLotSerial)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdNumberCollection -> Collection(PX.Objects.AM.AMProdNumber)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdOvhdCollection -> Collection(PX.Objects.AM.AMProdOvhd)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdStepCollection -> Collection(PX.Objects.AM.AMProdStep)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdToolCollection -> Collection(PX.Objects.AM.AMProdTool)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdTotalCollection -> Collection(PX.Objects.AM.AMProdTotal)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMSchdOperDetailCollection -> Collection(PX.Objects.AM.AMSchdOperDetail)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMSFKRecentActivityCollection -> Collection(PX.Objects.AM.SFK.AMSFKRecentActivity)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.SelectedProdMatlCollection -> Collection(PX.Objects.AM.SelectedProdMatl)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.SchedulerMachineOperationCollection -> Collection(PX.Objects.AM.SchedulerMachineOperation)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMMTranMoveByLotSerialCollection -> Collection(PX.Objects.AM.AMMTranMoveByLotSerial)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMMTranLotSerialNbrAllCollection -> Collection(PX.Objects.AM.AMMTranLotSerialNbrAll)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdItemSplitPreassignCollection -> Collection(PX.Objects.AM.AMProdItemSplitPreassign)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterial.AMProdItemRelatedCollection -> Collection(PX.Objects.AM.AMProdItemRelated)

# PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation (EntityType)

Label: "Production Order Build Capability Material"
Key: ProdOrdID
Entity sets: PX_Objects_AM_ProductionOrderBuildCapabilityMaterialFirstOperation, ProductionOrderBuildCapabilityMaterial1, ProductionOrderBuildCapabilityMaterialFirstOperation

PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.OrderType : Edm.String "Order Type"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.QtyReq : Edm.Decimal "Required Qty."
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.UOM : Edm.String "UOM"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.QtyToProd : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.CostCenterID : Edm.Int32
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.TaskID : Edm.Int32 "Task"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.MaxQtyToProdNonCalcMatl : Edm.Decimal "Max Qty. to Produce"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.MaxQtyToProd : Edm.Decimal "Max Qty. to Produce"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMOrderTypeByParentOrderType -> PX.Objects.AM.AMOrderType
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMOrderTypeByProductOrderType -> PX.Objects.AM.AMOrderType
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMOrderTypeBySourceOrderType -> PX.Objects.AM.AMOrderType
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdAttributeCollection -> Collection(PX.Objects.AM.AMProdAttribute)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdEvntCollection -> Collection(PX.Objects.AM.AMProdEvnt)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdMatlLotSerialCollection -> Collection(PX.Objects.AM.AMProdMatlLotSerial)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdNumberCollection -> Collection(PX.Objects.AM.AMProdNumber)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdOvhdCollection -> Collection(PX.Objects.AM.AMProdOvhd)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdStepCollection -> Collection(PX.Objects.AM.AMProdStep)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdToolCollection -> Collection(PX.Objects.AM.AMProdTool)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdTotalCollection -> Collection(PX.Objects.AM.AMProdTotal)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMSchdOperDetailCollection -> Collection(PX.Objects.AM.AMSchdOperDetail)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMSFKRecentActivityCollection -> Collection(PX.Objects.AM.SFK.AMSFKRecentActivity)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.SelectedProdMatlCollection -> Collection(PX.Objects.AM.SelectedProdMatl)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.SchedulerMachineOperationCollection -> Collection(PX.Objects.AM.SchedulerMachineOperation)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMMTranMoveByLotSerialCollection -> Collection(PX.Objects.AM.AMMTranMoveByLotSerial)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMMTranLotSerialNbrAllCollection -> Collection(PX.Objects.AM.AMMTranLotSerialNbrAll)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdItemSplitPreassignCollection -> Collection(PX.Objects.AM.AMProdItemSplitPreassign)
PX.Objects.AM.ProductionOrderBuildCapabilityMaterialFirstOperation.AMProdItemRelatedCollection -> Collection(PX.Objects.AM.AMProdItemRelated)

# PX.Objects.AM.ProductionReadinessByAllOperations (ComplexType)


PX.Objects.AM.ProductionReadinessByAllOperations.OrderType : Edm.String
PX.Objects.AM.ProductionReadinessByAllOperations.ProdOrdID : Edm.String
PX.Objects.AM.ProductionReadinessByAllOperations.MaxQtyToProd : Edm.Decimal
PX.Objects.AM.ProductionReadinessByAllOperations.MaxQtyToProdNonCalcMatl : Edm.Decimal

# PX.Objects.AM.ProductionReadinessByFirstOperation (ComplexType)


PX.Objects.AM.ProductionReadinessByFirstOperation.OrderType : Edm.String
PX.Objects.AM.ProductionReadinessByFirstOperation.ProdOrdID : Edm.String
PX.Objects.AM.ProductionReadinessByFirstOperation.MaxQtyToProd : Edm.Decimal
PX.Objects.AM.ProductionReadinessByFirstOperation.MaxQtyToProdNonCalcMatl : Edm.Decimal

# PX.Objects.AM.ProductionReadinessByProdItem (EntityType)

Label: "Production Readiness By ProdItem"
BaseType: PX.Objects.AM.AMProdItem
Key: OrderType, ProdOrdID (inherited from PX.Objects.AM.AMProdItem)
Entity sets: PX_Objects_AM_ProductionReadinessByProdItem, ProductionReadinessByProdItem
Non-filterable, non-selectable: QtyReadyToProd

PX.Objects.AM.ProductionReadinessByProdItem.ReadinessToProd : Edm.String "Readiness to Produce"
PX.Objects.AM.ProductionReadinessByProdItem.MaxQtyToProd : Edm.Decimal "Max Qty. to Produce"
PX.Objects.AM.ProductionReadinessByProdItem.QtyReadyToProd : Edm.Decimal "Qty. Ready to Produce"

# PX.Objects.AM.SchedulerMachineOperation (EntityType)

Label: "Machines event"
Key: CustomerID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SchedulerMachineOperation, Machinesevent, SchedulerMachineOperation
Non-filterable, non-selectable: OperationStart, OperationEnd, Schedulable

PX.Objects.AM.SchedulerMachineOperation.OrderType : Edm.String [key] "Type"
PX.Objects.AM.SchedulerMachineOperation.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SchedulerMachineOperation.OperationID : Edm.Int32 "OperationID"
PX.Objects.AM.SchedulerMachineOperation.OperationDescr : Edm.String "Description"
PX.Objects.AM.SchedulerMachineOperation.Name : Edm.String "Name"
PX.Objects.AM.SchedulerMachineOperation.SchdID : Edm.Int32 "Schedule ID"
PX.Objects.AM.SchedulerMachineOperation.SchdItemNoteID : Edm.Guid
PX.Objects.AM.SchedulerMachineOperation.ScheduleStatus : Edm.String "Schedule Status"
PX.Objects.AM.SchedulerMachineOperation.Closed : Edm.Boolean
PX.Objects.AM.SchedulerMachineOperation.Canceled : Edm.Boolean
PX.Objects.AM.SchedulerMachineOperation.Completed : Edm.Boolean
PX.Objects.AM.SchedulerMachineOperation.Locked : Edm.Boolean "Locked"
PX.Objects.AM.SchedulerMachineOperation.Hold : Edm.Boolean "Hold"
PX.Objects.AM.SchedulerMachineOperation.LastOperationID : Edm.Int32
PX.Objects.AM.SchedulerMachineOperation.ReadOnly : Edm.Boolean "Read Only"
PX.Objects.AM.SchedulerMachineOperation.StatusID : Edm.String "Production Order Status"
PX.Objects.AM.SchedulerMachineOperation.CustomerID : Edm.Int32 [key] "Customer ID"
PX.Objects.AM.SchedulerMachineOperation.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.SchedulerMachineOperation.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.SchedulerMachineOperation.SoOrderType : Edm.String "SO Order Type"
PX.Objects.AM.SchedulerMachineOperation.SoOrderNumber : Edm.String "SO Order Nbr."
PX.Objects.AM.SchedulerMachineOperation.Descr : Edm.String "Production Order Description"
PX.Objects.AM.SchedulerMachineOperation.CustomerName : Edm.String "Customer Name"
PX.Objects.AM.SchedulerMachineOperation.QtytoProd : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.SchedulerMachineOperation.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.SchedulerMachineOperation.Uom : Edm.String "UOM"
PX.Objects.AM.SchedulerMachineOperation.RequestedOn : Edm.DateTimeOffset "Requested On"
PX.Objects.AM.SchedulerMachineOperation.Function : Edm.Int32 "Function"
PX.Objects.AM.SchedulerMachineOperation.BaseCuryID : Edm.String
PX.Objects.AM.SchedulerMachineOperation.OperationStart : Edm.DateTimeOffset "Operation Start Time"
PX.Objects.AM.SchedulerMachineOperation.OperationEnd : Edm.DateTimeOffset "Operation End Time"
PX.Objects.AM.SchedulerMachineOperation.OperationStatus : Edm.String "Operation Status"
PX.Objects.AM.SchedulerMachineOperation.Id : Edm.Int64 "Id"
PX.Objects.AM.SchedulerMachineOperation.ResourceId : Edm.String "ResourceId"
PX.Objects.AM.SchedulerMachineOperation.SchdDate : Edm.DateTimeOffset "Schedule Date"
PX.Objects.AM.SchedulerMachineOperation.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.SchedulerMachineOperation.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.SchedulerMachineOperation.Schedulable : Edm.Boolean "Schedulable"
PX.Objects.AM.SchedulerMachineOperation.FirmSchedule : Edm.Boolean "Firm Schedule"
PX.Objects.AM.SchedulerMachineOperation.ProductOrderType : Edm.String "Product Order Type"
PX.Objects.AM.SchedulerMachineOperation.ProductOrdID : Edm.String "Product Order"
PX.Objects.AM.SchedulerMachineOperation.SOOrderBySoOrderNumber -> PX.Objects.SO.SOOrder (SoOrderNumber=OrderNbr)
PX.Objects.AM.SchedulerMachineOperation.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID)

# PX.Objects.AM.SchedulerMachineResource (EntityType)

Label: "Machines resources"
Key: Id
Entity sets: PX_Objects_AM_SchedulerMachineResource, Machinesresources, SchedulerMachineResource

PX.Objects.AM.SchedulerMachineResource.Id : Edm.String [key] "Machine"

# PX.Objects.AM.SchedulerProductionOrder (EntityType)

Label: "Production orders resources"
Key: CustomerID, Id, InventoryCD, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SchedulerProductionOrder, Productionordersresources, SchedulerProductionOrder
Non-filterable, non-selectable: IsLate, IsOnTime, IsEarly, ShippingDescr, Schedulable, IsEventExpanded, LackOfMaterials, Id, ChildMinStartDate, ChildMaxEndDate, ProductID, ParentID, IsProduct, IsChild

PX.Objects.AM.SchedulerProductionOrder.OrderType : Edm.String [key] "Type"
PX.Objects.AM.SchedulerProductionOrder.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SchedulerProductionOrder.SchdID : Edm.Int32 "Schedule ID"
PX.Objects.AM.SchedulerProductionOrder.SchdItemNoteID : Edm.Guid
PX.Objects.AM.SchedulerProductionOrder.OrdDescr : Edm.String "Production Order Description"
PX.Objects.AM.SchedulerProductionOrder.ScheduleStatus : Edm.String "Schedule Status"
PX.Objects.AM.SchedulerProductionOrder.Released : Edm.Boolean "Released"
PX.Objects.AM.SchedulerProductionOrder.Closed : Edm.Boolean
PX.Objects.AM.SchedulerProductionOrder.Canceled : Edm.Boolean
PX.Objects.AM.SchedulerProductionOrder.Completed : Edm.Boolean
PX.Objects.AM.SchedulerProductionOrder.Locked : Edm.Boolean "Locked"
PX.Objects.AM.SchedulerProductionOrder.IsLate : Edm.Boolean "Production order will be late"
PX.Objects.AM.SchedulerProductionOrder.IsOnTime : Edm.Boolean "Production order due same day"
PX.Objects.AM.SchedulerProductionOrder.IsEarly : Edm.Boolean "Production order will be early"
PX.Objects.AM.SchedulerProductionOrder.ShippingDescr : Edm.String
PX.Objects.AM.SchedulerProductionOrder.LastOperationID : Edm.Int32
PX.Objects.AM.SchedulerProductionOrder.ReadOnly : Edm.Boolean "Read Only"
PX.Objects.AM.SchedulerProductionOrder.Schedulable : Edm.Boolean "Schedulable"
PX.Objects.AM.SchedulerProductionOrder.Hold : Edm.Boolean "Hold"
PX.Objects.AM.SchedulerProductionOrder.StatusID : Edm.String "Production Order Status"
PX.Objects.AM.SchedulerProductionOrder.InventoryCD : Edm.String [key] "Inventory ID"
PX.Objects.AM.SchedulerProductionOrder.CustomerID : Edm.Int32 [key] "Customer ID"
PX.Objects.AM.SchedulerProductionOrder.CustomerName : Edm.String "Customer Name"
PX.Objects.AM.SchedulerProductionOrder.ProductWorkgroupID : Edm.Int32 "Product Workgroup"
PX.Objects.AM.SchedulerProductionOrder.WorkgroupDescr : Edm.String "Product Workgroup"
PX.Objects.AM.SchedulerProductionOrder.ProductManagerID : Edm.Int32 "Product Manager"
PX.Objects.AM.SchedulerProductionOrder.ProductManager : Edm.String "Product Manager"
PX.Objects.AM.SchedulerProductionOrder.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.SchedulerProductionOrder.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.SchedulerProductionOrder.FilterableStartDate : Edm.DateTimeOffset
PX.Objects.AM.SchedulerProductionOrder.FilterableEndDate : Edm.DateTimeOffset
PX.Objects.AM.SchedulerProductionOrder.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.AM.SchedulerProductionOrder.SoOrderType : Edm.String "SO Order Type"
PX.Objects.AM.SchedulerProductionOrder.SoOrderNumber : Edm.String "SO Order Nbr."
PX.Objects.AM.SchedulerProductionOrder.IsEventExpanded : Edm.Boolean
PX.Objects.AM.SchedulerProductionOrder.Descr : Edm.String "Production Order Description"
PX.Objects.AM.SchedulerProductionOrder.SchPriority : Edm.Int16 "Dispatch Priority"
PX.Objects.AM.SchedulerProductionOrder.ConstDate : Edm.DateTimeOffset "Constraint"
PX.Objects.AM.SchedulerProductionOrder.FirmSchedule : Edm.Boolean "Firm Schedule"
PX.Objects.AM.SchedulerProductionOrder.OrdTypeDescr : Edm.String "Order Type Description"
PX.Objects.AM.SchedulerProductionOrder.QtytoProd : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.SchedulerProductionOrder.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.SchedulerProductionOrder.Uom : Edm.String "UOM"
PX.Objects.AM.SchedulerProductionOrder.RequestedOn : Edm.DateTimeOffset "Requested On"
PX.Objects.AM.SchedulerProductionOrder.TotalCost : Edm.Decimal "WIP Total"
PX.Objects.AM.SchedulerProductionOrder.SchedulingMethod : Edm.String "Scheduling Method"
PX.Objects.AM.SchedulerProductionOrder.Function : Edm.Int32 "Function"
PX.Objects.AM.SchedulerProductionOrder.LackOfMaterials : Edm.Boolean "Lack Of Materials"
PX.Objects.AM.SchedulerProductionOrder.BaseCuryID : Edm.String
PX.Objects.AM.SchedulerProductionOrder.ProductOrderType : Edm.String "Product Order Type"
PX.Objects.AM.SchedulerProductionOrder.ProductOrdID : Edm.String "Product Order"
PX.Objects.AM.SchedulerProductionOrder.ParentOrderType : Edm.String "Parent Order Type"
PX.Objects.AM.SchedulerProductionOrder.ParentOrdID : Edm.String "Parent Order"
PX.Objects.AM.SchedulerProductionOrder.ParentOrdOperID : Edm.Int32
PX.Objects.AM.SchedulerProductionOrder.DueDateDiff : Edm.Int32 "Due Date Diff."
PX.Objects.AM.SchedulerProductionOrder.Id : Edm.String [key] "ID"
PX.Objects.AM.SchedulerProductionOrder.CalcedStartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.SchedulerProductionOrder.CalcedEndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.SchedulerProductionOrder.ChildMinStartDate : Edm.DateTimeOffset "Child Order Min. Start Date"
PX.Objects.AM.SchedulerProductionOrder.ChildMaxEndDate : Edm.DateTimeOffset "Child Order Max. Start Date"
PX.Objects.AM.SchedulerProductionOrder.ProductID : Edm.String "Product ID"
PX.Objects.AM.SchedulerProductionOrder.ParentID : Edm.String "Product ID"
PX.Objects.AM.SchedulerProductionOrder.IsProduct : Edm.Boolean
PX.Objects.AM.SchedulerProductionOrder.IsChild : Edm.Boolean
PX.Objects.AM.SchedulerProductionOrder.ProductScheduleStatus : Edm.String "Product Order Schedule Status"
PX.Objects.AM.SchedulerProductionOrder.SOOrderBySoOrderNumber -> PX.Objects.SO.SOOrder (SoOrderNumber=OrderNbr)
PX.Objects.AM.SchedulerProductionOrder.EPCompanyTreeByProductWorkgroupID -> PX.TM.EPCompanyTree (ProductWorkgroupID=WorkGroupID)
PX.Objects.AM.SchedulerProductionOrder.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.SchedulerProductionOrder.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID)
PX.Objects.AM.SchedulerProductionOrder.AMProdItemByParentOrdID -> PX.Objects.AM.AMProdItem (ParentOrdID=ProdOrdID)

# PX.Objects.AM.SchedulerWCOperation (EntityType)

Label: "Work centers operation"
Key: CustomerID, InventoryCD, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SchedulerWCOperation, Workcentersoperation, SchedulerWCOperation
Non-filterable, non-selectable: ResourceId, Schedulable, OperationStart, OperationEnd, IsOnTime, IsEarly, IsLate, LackOfMaterials, ShippingDescr

PX.Objects.AM.SchedulerWCOperation.Id : Edm.Int64 "Id"
PX.Objects.AM.SchedulerWCOperation.WcID : Edm.String "Work Center"
PX.Objects.AM.SchedulerWCOperation.Shift : Edm.String "Shift"
PX.Objects.AM.SchedulerWCOperation.ResourceId : Edm.String "ResourceId"
PX.Objects.AM.SchedulerWCOperation.OrderType : Edm.String [key] "Type"
PX.Objects.AM.SchedulerWCOperation.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SchedulerWCOperation.OperationID : Edm.Int32 "OperationID"
PX.Objects.AM.SchedulerWCOperation.OperationDescr : Edm.String "Description"
PX.Objects.AM.SchedulerWCOperation.Name : Edm.String "Name"
PX.Objects.AM.SchedulerWCOperation.SchdID : Edm.Int32 "Schedule ID"
PX.Objects.AM.SchedulerWCOperation.SchdItemNoteID : Edm.Guid
PX.Objects.AM.SchedulerWCOperation.ScheduleStatus : Edm.String "Schedule Status"
PX.Objects.AM.SchedulerWCOperation.Closed : Edm.Boolean
PX.Objects.AM.SchedulerWCOperation.Canceled : Edm.Boolean
PX.Objects.AM.SchedulerWCOperation.Completed : Edm.Boolean
PX.Objects.AM.SchedulerWCOperation.Locked : Edm.Boolean "Locked"
PX.Objects.AM.SchedulerWCOperation.Hold : Edm.Boolean "Hold"
PX.Objects.AM.SchedulerWCOperation.LastOperationID : Edm.Int32
PX.Objects.AM.SchedulerWCOperation.ReadOnly : Edm.Boolean "Read Only"
PX.Objects.AM.SchedulerWCOperation.Schedulable : Edm.Boolean "Schedulable"
PX.Objects.AM.SchedulerWCOperation.StatusID : Edm.String "Production Order Status"
PX.Objects.AM.SchedulerWCOperation.InventoryCD : Edm.String [key] "Inventory ID"
PX.Objects.AM.SchedulerWCOperation.CustomerID : Edm.Int32 [key] "Customer ID"
PX.Objects.AM.SchedulerWCOperation.ProductWorkgroupID : Edm.Int32 "Product Workgroup"
PX.Objects.AM.SchedulerWCOperation.ProductManagerID : Edm.Int32 "Product Manager"
PX.Objects.AM.SchedulerWCOperation.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.AM.SchedulerWCOperation.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.AM.SchedulerWCOperation.FilterableStartDate : Edm.DateTimeOffset
PX.Objects.AM.SchedulerWCOperation.FilterableEndDate : Edm.DateTimeOffset
PX.Objects.AM.SchedulerWCOperation.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.AM.SchedulerWCOperation.SoOrderType : Edm.String "SO Order Type"
PX.Objects.AM.SchedulerWCOperation.SoOrderNumber : Edm.String "SO Order Nbr."
PX.Objects.AM.SchedulerWCOperation.Descr : Edm.String "Production Order Description"
PX.Objects.AM.SchedulerWCOperation.SchPriority : Edm.Int16 "Dispatch Priority"
PX.Objects.AM.SchedulerWCOperation.ConstDate : Edm.DateTimeOffset "Constraint"
PX.Objects.AM.SchedulerWCOperation.FirmSchedule : Edm.Boolean "Firm Schedule"
PX.Objects.AM.SchedulerWCOperation.OrdTypeDescr : Edm.String "Order Type Description"
PX.Objects.AM.SchedulerWCOperation.CustomerName : Edm.String "Customer Name"
PX.Objects.AM.SchedulerWCOperation.WorkgroupDescr : Edm.String "Product Workgroup"
PX.Objects.AM.SchedulerWCOperation.ProductManager : Edm.String "Product Manager"
PX.Objects.AM.SchedulerWCOperation.QtytoProd : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.SchedulerWCOperation.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.SchedulerWCOperation.Uom : Edm.String "UOM"
PX.Objects.AM.SchedulerWCOperation.RequestedOn : Edm.DateTimeOffset "Requested On"
PX.Objects.AM.SchedulerWCOperation.TotalCost : Edm.Decimal "WIP Total"
PX.Objects.AM.SchedulerWCOperation.SchedulingMethod : Edm.String "Scheduling Method"
PX.Objects.AM.SchedulerWCOperation.Function : Edm.Int32 "Function"
PX.Objects.AM.SchedulerWCOperation.BaseCuryID : Edm.String
PX.Objects.AM.SchedulerWCOperation.ProductOrderType : Edm.String "Product Order Type"
PX.Objects.AM.SchedulerWCOperation.ProductOrdID : Edm.String "Product Order"
PX.Objects.AM.SchedulerWCOperation.ParentOrderType : Edm.String "Parent Order Type"
PX.Objects.AM.SchedulerWCOperation.ParentOrdID : Edm.String "Parent Order"
PX.Objects.AM.SchedulerWCOperation.ParentOrdOperID : Edm.Int32
PX.Objects.AM.SchedulerWCOperation.OperationStart : Edm.DateTimeOffset "Operation Start Time"
PX.Objects.AM.SchedulerWCOperation.OperationEnd : Edm.DateTimeOffset "Operation End Time"
PX.Objects.AM.SchedulerWCOperation.OperationStatus : Edm.String "Operation Status"
PX.Objects.AM.SchedulerWCOperation.SchdDate : Edm.DateTimeOffset "SchdDate"
PX.Objects.AM.SchedulerWCOperation.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.AM.SchedulerWCOperation.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.AM.SchedulerWCOperation.IsOnTime : Edm.Boolean "Production order due same day"
PX.Objects.AM.SchedulerWCOperation.IsEarly : Edm.Boolean "Production order will be early"
PX.Objects.AM.SchedulerWCOperation.IsLate : Edm.Boolean "Production order will be late"
PX.Objects.AM.SchedulerWCOperation.LackOfMaterials : Edm.Boolean "Lack Of Materials"
PX.Objects.AM.SchedulerWCOperation.ShippingDescr : Edm.String
PX.Objects.AM.SchedulerWCOperation.SOOrderBySoOrderNumber -> PX.Objects.SO.SOOrder (SoOrderNumber=OrderNbr)
PX.Objects.AM.SchedulerWCOperation.EPCompanyTreeByProductWorkgroupID -> PX.TM.EPCompanyTree (ProductWorkgroupID=WorkGroupID)
PX.Objects.AM.SchedulerWCOperation.EPShiftCodeByShift -> PX.Objects.EP.EPShiftCode (Shift=ShiftCD)
PX.Objects.AM.SchedulerWCOperation.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (ProdOrdID=ProdOrdID)
PX.Objects.AM.SchedulerWCOperation.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)

# PX.Objects.AM.SchedulerWCResource (EntityType)

Label: "Work centers resources"
Key: Id
Entity sets: PX_Objects_AM_SchedulerWCResource, Workcentersresources, SchedulerWCResource
Non-filterable, non-selectable: Id, ShiftCode, ResourceDetails

PX.Objects.AM.SchedulerWCResource.Id : Edm.String [key] "Id"
PX.Objects.AM.SchedulerWCResource.ShiftCode : Edm.String "Shift Code"
PX.Objects.AM.SchedulerWCResource.WcID : Edm.String "Work Center"
PX.Objects.AM.SchedulerWCResource.Shift : Edm.String "Shift"
PX.Objects.AM.SchedulerWCResource.CrewSize : Edm.Decimal "Crew Size"
PX.Objects.AM.SchedulerWCResource.Machines : Edm.Decimal "Machines"
PX.Objects.AM.SchedulerWCResource.ResourceDetails : Edm.String "Crew Size"
PX.Objects.AM.SchedulerWCResource.AMWCByWcID -> PX.Objects.AM.AMWC (WcID=WcID)

# PX.Objects.AM.SelectedProdMatl (EntityType)

Label: "Production Material"
Key: IsAllocated, LineID, OperationID, OrderType, ProdOrdID, SplitLineNbr
Entity sets: PX_Objects_AM_SelectedProdMatl, ProductionMaterial1, SelectedProdMatl
Non-filterable, non-selectable: QtyAlloc, QtyShort, IsByproduct2, RequiredDate, IsVisible

PX.Objects.AM.SelectedProdMatl.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SelectedProdMatl.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SelectedProdMatl.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.SelectedProdMatl.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.AM.SelectedProdMatl.SortOrder : Edm.Int32 "Line Order"
PX.Objects.AM.SelectedProdMatl.Descr : Edm.String "Description"
PX.Objects.AM.SelectedProdMatl.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.SelectedProdMatl.LocationID : Edm.Int32
PX.Objects.AM.SelectedProdMatl.QtyReq : Edm.Decimal "Required Qty."
PX.Objects.AM.SelectedProdMatl.QtyActual : Edm.Decimal "Actual Qty."
PX.Objects.AM.SelectedProdMatl.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.SelectedProdMatl.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AM.SelectedProdMatl.UOM : Edm.String "UOM"
PX.Objects.AM.SelectedProdMatl.BatchSize : Edm.Decimal "Batch Size"
PX.Objects.AM.SelectedProdMatl.OperStartDate : Edm.DateTimeOffset
PX.Objects.AM.SelectedProdMatl.ProdItemStartDate : Edm.DateTimeOffset
PX.Objects.AM.SelectedProdMatl.UpdateProject : Edm.Boolean
PX.Objects.AM.SelectedProdMatl.Function : Edm.Int32
PX.Objects.AM.SelectedProdMatl.FMLTMRPOrdorOP : Edm.Boolean
PX.Objects.AM.SelectedProdMatl.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.AM.SelectedProdMatl.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.AM.SelectedProdMatl.IsAllocated : Edm.Boolean [key] "Allocated"
PX.Objects.AM.SelectedProdMatl.POCreate : Edm.Boolean "Mark for PO"
PX.Objects.AM.SelectedProdMatl.ProdCreate : Edm.Boolean "Mark for Production"
PX.Objects.AM.SelectedProdMatl.SplitQty : Edm.Decimal "Quantity"
PX.Objects.AM.SelectedProdMatl.QtyAlloc : Edm.Decimal "Quantity"
PX.Objects.AM.SelectedProdMatl.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.AM.SelectedProdMatl.QtyAvail : Edm.Decimal "Available Qty."
PX.Objects.AM.SelectedProdMatl.QtyHardAvail : Edm.Decimal "Qty. Hard Available"
PX.Objects.AM.SelectedProdMatl.QtyShort : Edm.Decimal "Shortage Qty."
PX.Objects.AM.SelectedProdMatl.IsByproduct2 : Edm.Boolean "By-product"
PX.Objects.AM.SelectedProdMatl.RequiredDate : Edm.DateTimeOffset "Required Date"
PX.Objects.AM.SelectedProdMatl.TotalQtyRequired : Edm.Decimal "Total Required"
PX.Objects.AM.SelectedProdMatl.BaseTotalQtyRequired : Edm.Decimal "Base Total Required"
PX.Objects.AM.SelectedProdMatl.QtyProductionSupplyPrepared : Edm.Decimal "Prepared Production Supply Qty."
PX.Objects.AM.SelectedProdMatl.QtyProductionSupply : Edm.Decimal "Qty. Production Supply"
PX.Objects.AM.SelectedProdMatl.QtyProductionDemandPrepared : Edm.Decimal "Prepared Production Demand Qty."
PX.Objects.AM.SelectedProdMatl.QtyProductionDemand : Edm.Decimal "Production Demand Qty."
PX.Objects.AM.SelectedProdMatl.ItemCuryID : Edm.String
PX.Objects.AM.SelectedProdMatl.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.AM.SelectedProdMatl.TranDate : Edm.DateTimeOffset "Tran Date"
PX.Objects.AM.SelectedProdMatl.SplitLineCntr : Edm.Int32
PX.Objects.AM.SelectedProdMatl.MaterialType : Edm.Int32 "Material Type"
PX.Objects.AM.SelectedProdMatl.SubcontractSource : Edm.Int32 "Subcontract Source"
PX.Objects.AM.SelectedProdMatl.ReplenishmentSourceSiteID : Edm.Int32 "Replenishment Warehouse"
PX.Objects.AM.SelectedProdMatl.StatusID : Edm.String "Material Status"
PX.Objects.AM.SelectedProdMatl.ProjectID : Edm.Int32 "Project"
PX.Objects.AM.SelectedProdMatl.TaskID : Edm.Int32 "Task"
PX.Objects.AM.SelectedProdMatl.CostCenterID : Edm.Int32
PX.Objects.AM.SelectedProdMatl.SplitLineNbr : Edm.Int32 [key] "Split Line Nbr."
PX.Objects.AM.SelectedProdMatl.ReplenishmentSource : Edm.String "Replenishment Source"
PX.Objects.AM.SelectedProdMatl.QtyAvailPjct : Edm.Decimal
PX.Objects.AM.SelectedProdMatl.QtyHardAvailPjct : Edm.Decimal
PX.Objects.AM.SelectedProdMatl.QtyHardAvailAtLoc : Edm.Decimal
PX.Objects.AM.SelectedProdMatl.QtyHardAvailLocSum : Edm.Decimal
PX.Objects.AM.SelectedProdMatl.AccountingMode : Edm.String
PX.Objects.AM.SelectedProdMatl.POOrderNbr : Edm.String "PO Order Nbr."
PX.Objects.AM.SelectedProdMatl.AMOrderType : Edm.String "Sub. Assy. Order Type"
PX.Objects.AM.SelectedProdMatl.AMProdOrdID : Edm.String "Sub. Assy. Production Nbr."
PX.Objects.AM.SelectedProdMatl.PlanID : Edm.Int64 "Plan ID"
PX.Objects.AM.SelectedProdMatl.IsVisible : Edm.Boolean
PX.Objects.AM.SelectedProdMatl.POOrderByPOOrderNbr -> PX.Objects.PO.POOrder (POOrderNbr=OrderNbr)
PX.Objects.AM.SelectedProdMatl.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.SelectedProdMatl.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.SelectedProdMatl.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AM.SelectedProdMatl.AMOrderTypeByAMOrderType -> PX.Objects.AM.AMOrderType (AMOrderType=OrderType)
PX.Objects.AM.SelectedProdMatl.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.SelectedProdMatl.AMProdItemByAMOrderType -> PX.Objects.AM.AMProdItem (AMProdOrdID=ProdOrdID, AMOrderType=OrderType)
PX.Objects.AM.SelectedProdMatl.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.AM.SelectedProdMatl.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.SelectedProdMatl.INSiteByReplenishmentSourceSiteID -> PX.Objects.IN.INSite (ReplenishmentSourceSiteID=SiteID)

# PX.Objects.AM.SFK.AMClockTranUnapprovedSum (EntityType)

Label: "Unapproved Clock Entries Sum"
Key: OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_AMClockTranUnapprovedSum, UnapprovedClockEntriesSum, AMClockTranUnapprovedSum

PX.Objects.AM.SFK.AMClockTranUnapprovedSum.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.AMClockTranUnapprovedSum.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.AMClockTranUnapprovedSum.OperationID : Edm.Int32 [key]
PX.Objects.AM.SFK.AMClockTranUnapprovedSum.TotalLaborTime : Edm.Int64

# PX.Objects.AM.SFK.AMMTranScrap (EntityType)

Label: "AM Transaction"
BaseType: PX.Objects.AM.AMMTran
Key: BatNbr, DocType, LineNbr (inherited from PX.Objects.AM.AMMTran)
Entity sets: PX_Objects_AM_SFK_AMMTranScrap, AMTransaction1, AMMTranScrap
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.AM.SFK.AMMTranScrap.UnassignedQtyWarning : Edm.String

# PX.Objects.AM.SFK.AMMTranSplitScrap (EntityType)

Label: "AM Transaction Split"
BaseType: PX.Objects.AM.AMMTranSplit
Key: BatNbr, DocType, LineNbr, SplitLineNbr (inherited from PX.Objects.AM.AMMTranSplit)
Entity sets: PX_Objects_AM_SFK_AMMTranSplitScrap, AMTransactionSplit1, AMMTranSplitScrap
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.AM.SFK.AMMTranSplitScrap.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.SFK.AMMTranSplitScrap.RemoveLine : Edm.String "Remove"

# PX.Objects.AM.SFK.AMSFKRecentActivity (EntityType)

Label: "SFK Recent Activity"
Key: RecordID
Entity sets: PX_Objects_AM_SFK_AMSFKRecentActivity, SFKRecentActivity, AMSFKRecentActivity

PX.Objects.AM.SFK.AMSFKRecentActivity.RecordID : Edm.Int32 [key] "Record ID"
PX.Objects.AM.SFK.AMSFKRecentActivity.EmployeeID : Edm.Int32 "Employee"
PX.Objects.AM.SFK.AMSFKRecentActivity.ActionType : Edm.String "Action"
PX.Objects.AM.SFK.AMSFKRecentActivity.ActionDetails : Edm.String "Details"
PX.Objects.AM.SFK.AMSFKRecentActivity.OrderType : Edm.String "Order Type"
PX.Objects.AM.SFK.AMSFKRecentActivity.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.SFK.AMSFKRecentActivity.OperationID : Edm.Int32 "Operation ID"
PX.Objects.AM.SFK.AMSFKRecentActivity.CreatedDateTimeDaysFromNow : Edm.Int32 "Created Date Days"
PX.Objects.AM.SFK.AMSFKRecentActivity.CreatedByID : Edm.Guid "Created By"
PX.Objects.AM.SFK.AMSFKRecentActivity.CreatedByScreenID : Edm.String
PX.Objects.AM.SFK.AMSFKRecentActivity.CreatedDateTime : Edm.DateTimeOffset "Date and Time"
PX.Objects.AM.SFK.AMSFKRecentActivity.Tstamp : Edm.Binary
PX.Objects.AM.SFK.AMSFKRecentActivity.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.AM.SFK.AMSFKRecentActivity.AMProdOperByOperationID -> PX.Objects.AM.AMProdOper (OrderType=OrderType, ProdOrdID=ProdOrdID, OperationID=OperationID)
PX.Objects.AM.SFK.AMSFKRecentActivity.AMProdOperByProdOrdID -> PX.Objects.AM.AMProdOper (OperationID=OperationID, OrderType=OrderType, ProdOrdID=ProdOrdID)
PX.Objects.AM.SFK.AMSFKRecentActivity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AM.SFK.AMSFKRecentActivity.AMOrderTypeByOrderType -> PX.Objects.AM.AMOrderType (OrderType=OrderType)
PX.Objects.AM.SFK.AMSFKRecentActivity.AMProdItemByProdOrdID -> PX.Objects.AM.AMProdItem (OrderType=OrderType, ProdOrdID=ProdOrdID)

# PX.Objects.AM.SFK.OperationsInProgressProjection (EntityType)

Label: "Operations In Progress View"
Key: EmployeeID, LineNbr
Entity sets: PX_Objects_AM_SFK_OperationsInProgressProjection, OperationsInProgressView, OperationsInProgressProjection

PX.Objects.AM.SFK.OperationsInProgressProjection.EmployeeID : Edm.Int32 [key]
PX.Objects.AM.SFK.OperationsInProgressProjection.LineNbr : Edm.Int32 [key]
PX.Objects.AM.SFK.OperationsInProgressProjection.AcctName : Edm.String "Employee"
PX.Objects.AM.SFK.OperationsInProgressProjection.OrderType : Edm.String "Order Type"
PX.Objects.AM.SFK.OperationsInProgressProjection.ProdOrdID : Edm.String "Production Nbr."
PX.Objects.AM.SFK.OperationsInProgressProjection.OperationID : Edm.Int32
PX.Objects.AM.SFK.OperationsInProgressProjection.WcID : Edm.String "Work Center"
PX.Objects.AM.SFK.OperationsInProgressProjection.WCDescription : Edm.String "Work Center Description"
PX.Objects.AM.SFK.OperationsInProgressProjection.OperationCD : Edm.String "Operation"
PX.Objects.AM.SFK.OperationsInProgressProjection.OperationDescription : Edm.String "Operation Description"
PX.Objects.AM.SFK.OperationsInProgressProjection.SetupTime : Edm.Int32
PX.Objects.AM.SFK.OperationsInProgressProjection.RunUnitTime : Edm.Int32
PX.Objects.AM.SFK.OperationsInProgressProjection.RunUnits : Edm.Decimal
PX.Objects.AM.SFK.OperationsInProgressProjection.QtytoProd : Edm.Decimal
PX.Objects.AM.SFK.OperationsInProgressProjection.PlannedLaborTime : Edm.Int32 "Planned Labor Time"
PX.Objects.AM.SFK.OperationsInProgressProjection.ActualLaborTime : Edm.Int32
PX.Objects.AM.SFK.OperationsInProgressProjection.UnapprovedLaborTime : Edm.Int64
PX.Objects.AM.SFK.OperationsInProgressProjection.FinishTime : Edm.Int32 "Finish Time"
PX.Objects.AM.SFK.OperationsInProgressProjection.StartTime : Edm.DateTimeOffset
PX.Objects.AM.SFK.OperationsInProgressProjection.EndTime : Edm.DateTimeOffset
PX.Objects.AM.SFK.OperationsInProgressProjection.RemainingTime : Edm.Int32 "Remaining Time"
PX.Objects.AM.SFK.OperationsInProgressProjection.QtyComplete : Edm.Decimal "Completed Qty."
PX.Objects.AM.SFK.OperationsInProgressProjection.QtyRemaining : Edm.Decimal "Remaining Qty."
PX.Objects.AM.SFK.OperationsInProgressProjection.QueueTime : Edm.Int32 "Queue Time"
PX.Objects.AM.SFK.OperationsInProgressProjection.MoveTime : Edm.Int32 "Move Time"
PX.Objects.AM.SFK.OperationsInProgressProjection.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.AM.SFK.OperationsInProgressProjection.AMClockItemByEmployeeID -> PX.Objects.AM.AMClockItem (EmployeeID=EmployeeID)
PX.Objects.AM.SFK.OperationsInProgressProjection.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)

# PX.Objects.AM.SFK.OperationView (EntityType)

Label: "Operation View"
Key: OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_OperationView, OperationView
Non-filterable, non-selectable: WcWithDescr, OperationWithDescr

PX.Objects.AM.SFK.OperationView.WcWithDescr : Edm.String "Work Center"
PX.Objects.AM.SFK.OperationView.OperationWithDescr : Edm.String "Operation"
PX.Objects.AM.SFK.OperationView.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.OperationView.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.OperationView.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.SFK.OperationView.OperationCD : Edm.String "Operation ID"
PX.Objects.AM.SFK.OperationView.Descr : Edm.String
PX.Objects.AM.SFK.OperationView.WcID : Edm.String "Work Center"
PX.Objects.AM.SFK.OperationView.WcDescr : Edm.String

# PX.Objects.AM.SFK.SFKEmployeeProjection (EntityType)

Label: "Shop Floor Employee"
Key: BAccountID
Entity sets: PX_Objects_AM_SFK_SFKEmployeeProjection, ShopFloorEmployee, SFKEmployeeProjection

PX.Objects.AM.SFK.SFKEmployeeProjection.BAccountID : Edm.Int32 [key]
PX.Objects.AM.SFK.SFKEmployeeProjection.AcctCD : Edm.String "Employee ID"
PX.Objects.AM.SFK.SFKEmployeeProjection.AcctName : Edm.String "Employee Name"
PX.Objects.AM.SFK.SFKEmployeeProjection.FirstName : Edm.String "First Name"
PX.Objects.AM.SFK.SFKEmployeeProjection.LastName : Edm.String "Last Name"
PX.Objects.AM.SFK.SFKEmployeeProjection.Username : Edm.String "Username"
PX.Objects.AM.SFK.SFKEmployeeProjection.DefContactID : Edm.Int32
PX.Objects.AM.SFK.SFKEmployeeProjection.VStatus : Edm.String
PX.Objects.AM.SFK.SFKEmployeeProjection.ParentBAccountID : Edm.Int32
PX.Objects.AM.SFK.SFKEmployeeProjection.AMShopFloorShiftCD : Edm.String
PX.Objects.AM.SFK.SFKEmployeeProjection.BAccountByParentBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID)
PX.Objects.AM.SFK.SFKEmployeeProjection.BAccountByCOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.AM.SFK.SFKEmployeeProjection.BAccountByBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID, BAccountID=BAccountID)
PX.Objects.AM.SFK.SFKEmployeeProjection.ContactByPrimaryContactID -> PX.Objects.CR.Contact
PX.Objects.AM.SFK.SFKEmployeeProjection.ContactByDefContactID -> PX.Objects.CR.Contact (DefContactID=ContactID)
PX.Objects.AM.SFK.SFKEmployeeProjection.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.AM.SFK.SFKEmployeeProjection.ContactByParentBAccountID -> PX.Objects.CR.Contact (DefContactID=ContactID, ParentBAccountID=BAccountID)
PX.Objects.AM.SFK.SFKEmployeeProjection.BranchByParentBAccountID -> PX.Objects.GL.Branch (ParentBAccountID=BAccountID)
PX.Objects.AM.SFK.SFKEmployeeProjection.EPShiftCodeByShiftID -> PX.Objects.EP.EPShiftCode
PX.Objects.AM.SFK.SFKEmployeeProjection.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.AM.SFK.SFKEmployeeProjection.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.AM.SFK.SFKEmployeeProjection.EPTimeCardCollection -> Collection(PX.Objects.EP.EPTimeCard)
PX.Objects.AM.SFK.SFKEmployeeProjection.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.AM.SFK.SFKEmployeeProjection.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.AM.SFK.SFKEmployeeProjection.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AM.SFK.SFKEmployeeProjection.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.AM.SFK.SFKEmployeeProjection.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.Objects.AM.SFK.SFKEmployeeProjection.EPTimeLogCollection -> Collection(PX.Objects.EP.ClockInClockOut.EPTimeLog)
PX.Objects.AM.SFK.SFKEmployeeProjection.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.AM.SFK.SFKEmployeeProjection.TimecardWithTotalsCollection -> Collection(PX.Objects.EP.TimecardWithTotals)
PX.Objects.AM.SFK.SFKEmployeeProjection.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.AM.SFK.SFKEmployeeProjection.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.AM.SFK.SFKEmployeeProjection.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.AM.SFK.SFKEmployeeProjection.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.AM.SFK.SFKEmployeeProjection.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.AM.SFK.SFKEmployeeProjection.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.AM.SFK.SFKEmployeeProjection.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.AM.SFK.SFKEmployeeProjection.FSLicenseCollection -> Collection(PX.Objects.SV.FSLicense)
PX.Objects.AM.SFK.SFKEmployeeProjection.FSEmployeeSkillCollection -> Collection(PX.Objects.SV.FSEmployeeSkill)
PX.Objects.AM.SFK.SFKEmployeeProjection.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.AM.SFK.SFKEmployeeProjection.EPWingmanCollection -> Collection(PX.Objects.EP.EPWingman)
PX.Objects.AM.SFK.SFKEmployeeProjection.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.AM.SFK.SFKEmployeeProjection.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.AM.SFK.SFKEmployeeProjection.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.AM.SFK.SFKEmployeeProjection.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.AM.SFK.SFKEmployeeProjection.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.AM.SFK.SFKEmployeeProjection.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.AM.SFK.SFKEmployeeProjection.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.AM.SFK.SFKEmployeeProjection.AMEstimateClassCollection -> Collection(PX.Objects.AM.AMEstimateClass)
PX.Objects.AM.SFK.SFKEmployeeProjection.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.AM.SFK.SFKEmployeeProjection.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.AM.SFK.SFKEmployeeProjection.FSGeoZoneEmpCollection -> Collection(PX.Objects.FS.FSGeoZoneEmp)
PX.Objects.AM.SFK.SFKEmployeeProjection.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.AM.SFK.SFKEmployeeProjection.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.AM.SFK.SFKEmployeeProjection.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.AM.SFK.SFKEmployeeProjection.EPEmployeeCorpCardLinkCollection -> Collection(PX.Objects.EP.DAC.EPEmployeeCorpCardLink)
PX.Objects.AM.SFK.SFKEmployeeProjection.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.AM.SFK.SFKEmployeeProjection.PMEmployeeRateCollection -> Collection(PX.Objects.PM.PMEmployeeRate)
PX.Objects.AM.SFK.SFKEmployeeProjection.FSGPSTrackingRequestCollection -> Collection(PX.FS.FSGPSTrackingRequest)
PX.Objects.AM.SFK.SFKEmployeeProjection.MUIFavoriteScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteScreen)
PX.Objects.AM.SFK.SFKEmployeeProjection.MUIFavoriteTileCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteTile)
PX.Objects.AM.SFK.SFKEmployeeProjection.MUIFavoriteWorkspaceCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIFavoriteWorkspace)
PX.Objects.AM.SFK.SFKEmployeeProjection.MUIPinnedScreenCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIPinnedScreen)
PX.Objects.AM.SFK.SFKEmployeeProjection.MUIUserPreferencesCollection -> Collection(PX.Web.UI.Frameset.Model.DAC.MUIUserPreferences)
PX.Objects.AM.SFK.SFKEmployeeProjection.UsersInRolesCollection -> Collection(PX.SM.UsersInRoles)
PX.Objects.AM.SFK.SFKEmployeeProjection.WidgetCollection -> Collection(PX.Dashboards.DAC.Widget)
PX.Objects.AM.SFK.SFKEmployeeProjection.WidgetV2Collection -> Collection(PX.Dashboards.DAC.WidgetV2)
PX.Objects.AM.SFK.SFKEmployeeProjection.GridDataPresentationCollection -> Collection(PX.ScreenPreferences.DAC.GridDataPresentation)
PX.Objects.AM.SFK.SFKEmployeeProjection.LoginTraceCollection -> Collection(PX.SM.LoginTrace)
PX.Objects.AM.SFK.SFKEmployeeProjection.PivotFieldPreferencesCollection -> Collection(PX.Olap.Maintenance.PivotFieldPreferences)
PX.Objects.AM.SFK.SFKEmployeeProjection.UserFilterCollection -> Collection(PX.SM.UserFilter)

# PX.Objects.AM.SFK.SFKIssueMaterialsFilter (EntityType)

Label: "Production Operation Materials View"
Key: LineID, OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_SFKIssueMaterialsFilter, ProductionOperationMaterialsView, SFKIssueMaterialsFilter
Non-filterable, non-selectable: Info, QtyRemaining, QtyToIssue, SelectedQtyToIssue, AddedQtyToIssue, QtyOnHand, QtyAvailableForIssue, OpenContext, IsReturn, IsAdditionalMaterial, EffectiveCostCenterID, IsByproduct

PX.Objects.AM.SFK.SFKIssueMaterialsFilter.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.LineID : Edm.Int32 [key]
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.Info : Edm.String
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.StkItem : Edm.Boolean
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.InventoryCD : Edm.String "Inventory ID"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.ImageUrl : Edm.String "Image"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.NoteID : Edm.Guid "NoteID"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.Descr : Edm.String "Description"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.UOM : Edm.String "UOM"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.TotalQtyRequired : Edm.Decimal "Total Required Qty."
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.BaseTotalQtyRequired : Edm.Decimal
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.QtyActual : Edm.Decimal "Qty. Actual"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.QtyRemaining : Edm.Decimal "Total Remaining Qty."
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.LotSerTrack : Edm.String "Tracking Method"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.QtyToIssue : Edm.Decimal "Total Qty. to Issue"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.SelectedQtyToIssue : Edm.Decimal "Selected Qty."
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.AddedQtyToIssue : Edm.Decimal "Added Qty."
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.QtyAvailableForIssue : Edm.Decimal "Qty. Available for Issue"
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.AutoNextNbr : Edm.Boolean
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.LotSerAssign : Edm.String
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.OpenContext : Edm.String
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.IsReturn : Edm.Boolean
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.IsAdditionalMaterial : Edm.Boolean
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.EffectiveCostCenterID : Edm.Int32
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.SiteID : Edm.Int32
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.LocationID : Edm.Int32
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.SubItemID : Edm.Int32
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.StatusID : Edm.String
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.SortOrder : Edm.Int32
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.IsByproduct : Edm.Boolean
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.MaterialType : Edm.Int32
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.BFlush : Edm.Boolean
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.AM.SFK.SFKIssueMaterialsFilter.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.AM.SFK.SFKLotSerialNbrResult (EntityType)

Label: "SFK Lot/Serial by Attributes"
Key: InventoryID, LocationID, LotSerialNbr, SiteID
Entity sets: PX_Objects_AM_SFK_SFKLotSerialNbrResult, SFKLotSerialbyAttributes, SFKLotSerialNbrResult
Non-filterable, non-selectable: QtySelected

PX.Objects.AM.SFK.SFKLotSerialNbrResult.LotSerClassID : Edm.String
PX.Objects.AM.SFK.SFKLotSerialNbrResult.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AM.SFK.SFKLotSerialNbrResult.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.SFK.SFKLotSerialNbrResult.MfgLotSerialNbr : Edm.String "Manufacturer Lot/Serial Nbr."
PX.Objects.AM.SFK.SFKLotSerialNbrResult.Descr : Edm.String "Description"
PX.Objects.AM.SFK.SFKLotSerialNbrResult.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AM.SFK.SFKLotSerialNbrResult.LocationID : Edm.Int32 [key]
PX.Objects.AM.SFK.SFKLotSerialNbrResult.LocationCD : Edm.String "Location"
PX.Objects.AM.SFK.SFKLotSerialNbrResult.BaseUnit : Edm.String "Base UOM"
PX.Objects.AM.SFK.SFKLotSerialNbrResult.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.AM.SFK.SFKLotSerialNbrResult.QtyAvail : Edm.Decimal "Qty. Available for Issue"
PX.Objects.AM.SFK.SFKLotSerialNbrResult.QtySelected : Edm.Decimal "Selected Qty."
PX.Objects.AM.SFK.SFKLotSerialNbrResult.NoteID : Edm.Guid
PX.Objects.AM.SFK.SFKLotSerialNbrResult.INLotSerClassByLotSerClassID -> PX.Objects.IN.INLotSerClass (LotSerClassID=LotSerClassID)

# PX.Objects.AM.SFK.SFKOperationFileProjection (EntityType)

Label: "Operation file"
Key: FileID
Entity sets: PX_Objects_AM_SFK_SFKOperationFileProjection, Operationfile, SFKOperationFileProjection
Non-filterable, non-selectable: ViewURL

PX.Objects.AM.SFK.SFKOperationFileProjection.FileID : Edm.Guid [key] "File ID"
PX.Objects.AM.SFK.SFKOperationFileProjection.NoteID : Edm.Guid "Note ID"
PX.Objects.AM.SFK.SFKOperationFileProjection.Name : Edm.String "File Name"
PX.Objects.AM.SFK.SFKOperationFileProjection.ViewURL : Edm.String "View"
PX.Objects.AM.SFK.SFKOperationFileProjection.Comment : Edm.String "Comment"
PX.Objects.AM.SFK.SFKOperationFileProjection.RevisionDate : Edm.DateTimeOffset "Last Modified"
PX.Objects.AM.SFK.SFKOperationFileProjection.Source : Edm.String "Source"
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdItemOrderType : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdItemProdOrdID : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdOperOrderType : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdOperProdOrdID : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdOperOperationID : Edm.Int32
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdMatlOrderType : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdMatlProdOrdID : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdMatlOperationID : Edm.Int32
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdStepOrderType : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdStepProdOrdID : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdStepOperationID : Edm.Int32
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdToolOrderType : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdToolProdOrdID : Edm.String
PX.Objects.AM.SFK.SFKOperationFileProjection.ProdToolOperationID : Edm.Int32
PX.Objects.AM.SFK.SFKOperationFileProjection.UploadFileWithIDSelectorByName -> PX.SM.UploadFileWithIDSelector (Name=FileID)
PX.Objects.AM.SFK.SFKOperationFileProjection.UploadFileWithIDSelectorCollection -> Collection(PX.SM.UploadFileWithIDSelector)

# PX.Objects.AM.SFK.SFKOperationsByWCProjection (EntityType)

Label: "Operations In Work Centers"
BaseType: PX.Objects.AM.SFK.SFKProdOperProjection
Key: OperationCD, OperationID, OrderType, ProdOrdID (inherited from PX.Objects.AM.SFK.SFKProdOperProjection)
Entity sets: PX_Objects_AM_SFK_SFKOperationsByWCProjection, OperationsInWorkCenters, SFKOperationsByWCProjection
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.AM.SFK.SFKOperationsByWCProjection.IsCurrentEmployeeClocked : Edm.Boolean

# PX.Objects.AM.SFK.SFKProdOperMaterialsProjection (EntityType)

Label: "Production Operation Materials View"
Key: LineID, OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_SFKProdOperMaterialsProjection, ProductionOperationMaterialsView1, SFKProdOperMaterialsProjection
Non-filterable, non-selectable: IsRowDisabled, Info, QtyRemaining, BaseQtyRemaining, QtyToIssue, QtyOnHand, QtyAvailableForIssue, TotalIssuedQty

PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.LineID : Edm.Int32 [key]
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.IsRowDisabled : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.Info : Edm.String
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.InventoryID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.InventoryCD : Edm.String "Inventory ID"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.Descr : Edm.String "Description"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.UOM : Edm.String "UOM"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.TotalQtyRequired : Edm.Decimal "Total Required Qty."
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.BaseTotalQtyRequired : Edm.Decimal
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.BatchSize : Edm.Decimal "Batch Size"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.QtyActual : Edm.Decimal "Qty. Actual"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.BaseQtyActual : Edm.Decimal "Actual Base Qty."
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.QtyRemaining : Edm.Decimal "Total Remaining Qty."
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.BaseQtyRemaining : Edm.Decimal "Total Remaining Qty."
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.SubcontractSource : Edm.Int32 "Subcontract Source"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.CostCenterID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.QtyToIssue : Edm.Decimal "Qty. to Issue"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.QtyAvailableForIssue : Edm.Decimal "Qty. Available for Issue"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.TotalIssuedQty : Edm.Decimal "Total Issued Qty."
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.SiteID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.LocationID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.SubItemID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.SortOrder : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.IsByproduct : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.MaterialType : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.StkItem : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.ItemStatus : Edm.String "Item Status"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.StatusID : Edm.String "Material Status"
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.BFlush : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.ProjectID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.TaskID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.INLocationBySiteID -> PX.Objects.IN.INLocation (LocationID=LocationID, SiteID=SiteID)
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.INLocationByLocationID -> PX.Objects.IN.INLocation (SiteID=SiteID, LocationID=LocationID)
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.AM.SFK.SFKProdOperMaterialsProjection.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.AM.SFK.SFKProdOperProjection (EntityType)

Label: "Production Operations View"
Key: OperationCD, OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_SFKProdOperProjection, ProductionOperationsView, SFKProdOperProjection
Non-filterable, non-selectable: OperatorName, ActualLaborTime, ActiveClockStartTime, RequiresLotSerialAttributes, ShowLinkOnOrder, ShowLinkOnOper

PX.Objects.AM.SFK.SFKProdOperProjection.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.SFKProdOperProjection.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.SFKProdOperProjection.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.SFK.SFKProdOperProjection.OperationCD : Edm.String [key] "Operation"
PX.Objects.AM.SFK.SFKProdOperProjection.Descr : Edm.String "Operation Description"
PX.Objects.AM.SFK.SFKProdOperProjection.StatusID : Edm.String "Status"
PX.Objects.AM.SFK.SFKProdOperProjection.WcID : Edm.String "Work Center"
PX.Objects.AM.SFK.SFKProdOperProjection.WcDescr : Edm.String "Work Center Description"
PX.Objects.AM.SFK.SFKProdOperProjection.QtytoProdAdjusted : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.SFK.SFKProdOperProjection.PlanQtyToProduce : Edm.Decimal "Plan Qty."
PX.Objects.AM.SFK.SFKProdOperProjection.QtyCompleteAdjusted : Edm.Decimal "Completed Qty."
PX.Objects.AM.SFK.SFKProdOperProjection.BaseQtyCompleteAdjusted : Edm.Decimal "Completed Qty."
PX.Objects.AM.SFK.SFKProdOperProjection.QtyRemainingAdjusted : Edm.Decimal "Remaining Qty."
PX.Objects.AM.SFK.SFKProdOperProjection.QtyScrappedAdjusted : Edm.Decimal "Scrapped Qty."
PX.Objects.AM.SFK.SFKProdOperProjection.UOM : Edm.String "UOM"
PX.Objects.AM.SFK.SFKProdOperProjection.BaseUnit : Edm.String "UOM"
PX.Objects.AM.SFK.SFKProdOperProjection.ValMethod : Edm.String "Valuation Method"
PX.Objects.AM.SFK.SFKProdOperProjection.OperatorName : Edm.String "Operator"
PX.Objects.AM.SFK.SFKProdOperProjection.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AM.SFK.SFKProdOperProjection.WcWithDescr : Edm.String "Work Center"
PX.Objects.AM.SFK.SFKProdOperProjection.OperationWithDescr : Edm.String "Operation"
PX.Objects.AM.SFK.SFKProdOperProjection.IsOpen : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.StartDate : Edm.DateTimeOffset
PX.Objects.AM.SFK.SFKProdOperProjection.EndDate : Edm.DateTimeOffset
PX.Objects.AM.SFK.SFKProdOperProjection.PlanLaborTime : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperProjection.ActualLaborTime : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperProjection.ActiveClockStartTime : Edm.DateTimeOffset
PX.Objects.AM.SFK.SFKProdOperProjection.BFlush : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.PreassignLotSerial : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.ParentLotSerialRequired : Edm.String
PX.Objects.AM.SFK.SFKProdOperProjection.IsLastOperation : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.InventoryID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperProjection.SubItemID : Edm.Int32
PX.Objects.AM.SFK.SFKProdOperProjection.InventoryCD : Edm.String "Inventory ID"
PX.Objects.AM.SFK.SFKProdOperProjection.InventoryDescr : Edm.String "Inventory Description"
PX.Objects.AM.SFK.SFKProdOperProjection.LotSerTrackExpiration : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.LotSerAssign : Edm.String
PX.Objects.AM.SFK.SFKProdOperProjection.LotSerTrack : Edm.String
PX.Objects.AM.SFK.SFKProdOperProjection.LSAutoNextNbr : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.OutsideProcess : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.ScrapAction : Edm.Int32 "Scrap Action"
PX.Objects.AM.SFK.SFKProdOperProjection.RequiresLotSerialAttributes : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.ShowLinkOnOrder : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.ShowLinkOnOper : Edm.Boolean
PX.Objects.AM.SFK.SFKProdOperProjection.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AM.SFK.SFKProdOperProjection.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.SFK.SFKProdOperProjection.INLocationByScrapSiteID -> PX.Objects.IN.INLocation
PX.Objects.AM.SFK.SFKProdOperProjection.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.SFK.SFKProdOperProjection.INLocationByScrapLocationID -> PX.Objects.IN.INLocation
PX.Objects.AM.SFK.SFKProdOperProjection.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AM.SFK.SFKProdOperProjection.INSiteByScrapSiteID -> PX.Objects.IN.INSite
PX.Objects.AM.SFK.SFKProdOperProjection.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.AM.SFK.SFKProdOperProjection.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AM.SFK.SFKProdOperProjection.INUnitByBaseUnit -> PX.Objects.IN.INUnit (BaseUnit=FromUnit)
PX.Objects.AM.SFK.SFKProdOperProjection.INUnitByWeightUOM -> PX.Objects.IN.INUnit
PX.Objects.AM.SFK.SFKProdOperProjection.INUnitByVolumeUOM -> PX.Objects.IN.INUnit
PX.Objects.AM.SFK.SFKProdOperProjection.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.AM.SFK.SFKProdOperProjection.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.AM.SFK.SFKProdOperProjection.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.AM.SFK.SFKProductionOrderProjection (EntityType)

Label: "Production Order View"
Key: OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_SFKProductionOrderProjection, ProductionOrderView, SFKProductionOrderProjection

PX.Objects.AM.SFK.SFKProductionOrderProjection.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.SFKProductionOrderProjection.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.SFKProductionOrderProjection.CustomerIDDescr : Edm.String "Customer"
PX.Objects.AM.SFK.SFKProductionOrderProjection.InventoryIDWithDescr : Edm.String "Inventory ID"
PX.Objects.AM.SFK.SFKProductionOrderProjection.QtytoProd : Edm.Decimal "Qty. to Produce"
PX.Objects.AM.SFK.SFKProductionOrderProjection.UOM : Edm.String "UOM"
PX.Objects.AM.SFK.SFKProductionOrderProjection.StatusID : Edm.String "Status"
PX.Objects.AM.SFK.SFKProductionOrderProjection.IsOpen : Edm.Boolean
PX.Objects.AM.SFK.SFKProductionOrderProjection.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AM.SFK.SFKProductionOrderProjection.LastOperationID : Edm.Int32
PX.Objects.AM.SFK.SFKProductionOrderProjection.Descr : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.StartDate : Edm.DateTimeOffset
PX.Objects.AM.SFK.SFKProductionOrderProjection.EndDate : Edm.DateTimeOffset
PX.Objects.AM.SFK.SFKProductionOrderProjection.CostMethod : Edm.Int32
PX.Objects.AM.SFK.SFKProductionOrderProjection.OrderTypeDescr : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.Function : Edm.Int32
PX.Objects.AM.SFK.SFKProductionOrderProjection.ExceedQtyOperations : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.CustomerAcctCD : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.CustomerAcctName : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.InventoryCD : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.InventoryDescr : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.LotSerTrack : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.LotSerAssign : Edm.String
PX.Objects.AM.SFK.SFKProductionOrderProjection.AutoNextNbr : Edm.Boolean
PX.Objects.AM.SFK.SFKProductionOrderProjection.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.AM.SFK.SFKProductionOrderProjection.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.AM.SFK.SFKProductionOrderProjection.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.AM.SFK.SFKSubtractSplit (EntityType)

Label: "SFK Subtract Lot/Serial"
Key: BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_SFKSubtractSplit, SFKSubtractLotSerial, SFKSubtractSplit
Non-filterable, non-selectable: ReportedQty, BaseReportedQty, QtyToSubtract, BaseQtyToSubtract

PX.Objects.AM.SFK.SFKSubtractSplit.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.SFKSubtractSplit.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.SFKSubtractSplit.DocType : Edm.String [key]
PX.Objects.AM.SFK.SFKSubtractSplit.BatNbr : Edm.String [key]
PX.Objects.AM.SFK.SFKSubtractSplit.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.SFK.SFKSubtractSplit.InventoryID : Edm.Int32
PX.Objects.AM.SFK.SFKSubtractSplit.UOM : Edm.String "UOM"
PX.Objects.AM.SFK.SFKSubtractSplit.ReportedQty : Edm.Decimal "Reported Lot Qty."
PX.Objects.AM.SFK.SFKSubtractSplit.BaseReportedQty : Edm.Decimal
PX.Objects.AM.SFK.SFKSubtractSplit.NoteID : Edm.Guid
PX.Objects.AM.SFK.SFKSubtractSplit.QtyToSubtract : Edm.Decimal "Qty. to Subtract"
PX.Objects.AM.SFK.SFKSubtractSplit.BaseQtyToSubtract : Edm.Decimal

# PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum (EntityType)

Label: "Completed Quantities Summary"
Key: BatNbr, DocType, LotSerialNbr, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_SFKTranSplitCompletedByLotSerialSum, CompletedQuantitiesSummary, SFKTranSplitCompletedByLotSerialSum

PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.DocType : Edm.String [key]
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.BatNbr : Edm.String [key]
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.CompletedQty : Edm.Decimal "Completed Qty."
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.BaseCompletedQty : Edm.Decimal
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.InventoryID : Edm.Int32
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.UOM : Edm.String "UOM"
PX.Objects.AM.SFK.SFKTranSplitCompletedByLotSerialSum.NoteID : Edm.Guid

# PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum (EntityType)

Label: "Scrap Quantities Summary"
Key: BatNbr, DocType, LotSerialNbr, OperationCD, OperationID, OrderType, ProdOrdID
Entity sets: PX_Objects_AM_SFK_SFKTranSplitScrapByLotSerialSum, ScrapQuantitiesSummary, SFKTranSplitScrapByLotSerialSum

PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.OrderType : Edm.String [key] "Order Type"
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.ProdOrdID : Edm.String [key] "Production Nbr."
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.OperationID : Edm.Int32 [key] "Operation ID"
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.DocType : Edm.String [key]
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.BatNbr : Edm.String [key]
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.OperationCD : Edm.String [key] "Operation"
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.ScrappedQty : Edm.Decimal "Scrap Qty."
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.BaseScrappedQty : Edm.Decimal
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.InventoryID : Edm.Int32
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.UOM : Edm.String "UOM"
PX.Objects.AM.SFK.SFKTranSplitScrapByLotSerialSum.NoteID : Edm.Guid

# PX.Objects.AM.SubAssemblyProjection (EntityType)

Label: "Sub-Assembly Projection"
BaseType: PX.Objects.AM.AMProdItem
Key: OrderType, ProdOrdID (inherited from PX.Objects.AM.AMProdItem)
Entity sets: PX_Objects_AM_SubAssemblyProjection, SubAssemblyProjection

PX.Objects.AM.SubAssemblyProjection.ParentOperationID : Edm.Int32 "Parent Operation"
PX.Objects.AM.SubAssemblyProjection.ParentLineID : Edm.Int32
PX.Objects.AM.SubAssemblyProjection.SplitLineNbr : Edm.Int32
PX.Objects.AM.SubAssemblyProjection.SchdOperationID : Edm.Int32
PX.Objects.AM.SubAssemblyProjection.SchdID : Edm.Int32
PX.Objects.AM.SubAssemblyProjection.SchdLineNbr : Edm.Int32
PX.Objects.AM.SubAssemblyProjection.SchdOperStartDate : Edm.DateTimeOffset
PX.Objects.AM.SubAssemblyProjection.SchdOperEndDate : Edm.DateTimeOffset
PX.Objects.AM.SubAssemblyProjection.SchdWcID : Edm.String

# PX.Objects.AP.AP1099Box (EntityType)

Label: "AP 1099 Box"
Key: BoxCD, BoxNbr
Entity sets: PX_Objects_AP_AP1099Box, AP1099Box
Non-filterable, non-selectable: OldAccountID

PX.Objects.AP.AP1099Box.BoxNbr : Edm.Int16 [key] "1099 Box"
PX.Objects.AP.AP1099Box.BoxCD : Edm.String [key] "1099 Box"
PX.Objects.AP.AP1099Box.Descr : Edm.String "Description"
PX.Objects.AP.AP1099Box.MinReportAmt : Edm.Decimal [required] "Minimum Report Amount"
PX.Objects.AP.AP1099Box.OldAccountID : Edm.Int32
PX.Objects.AP.AP1099Box.tstamp : Edm.Binary
PX.Objects.AP.AP1099Box.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.AP.AP1099Box.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.AP1099Box.AP1099HistoryCollection -> Collection(PX.Objects.AP.AP1099History)
PX.Objects.AP.AP1099Box.AP1099HistCollection -> Collection(PX.Objects.AP.Overrides.APDocumentRelease.AP1099Hist)

# PX.Objects.AP.AP1099History (EntityType)

Label: "AP 1099 History"
Key: BoxNbr, BranchID, FinYear, VendorID
Entity sets: PX_Objects_AP_AP1099History, AP1099History

PX.Objects.AP.AP1099History.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.AP.AP1099History.VendorID : Edm.Int32 [key]
PX.Objects.AP.AP1099History.FinYear : Edm.String [key]
PX.Objects.AP.AP1099History.BoxNbr : Edm.Int16 [key]
PX.Objects.AP.AP1099History.HistAmt : Edm.Decimal [required] "Amount"
PX.Objects.AP.AP1099History.tstamp : Edm.Binary
PX.Objects.AP.AP1099History.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.AP1099History.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AP.AP1099History.AP1099BoxByBoxNbr -> PX.Objects.AP.AP1099Box (BoxNbr=BoxNbr)

# PX.Objects.AP.AP1099HistoryByPayer (ComplexType)


PX.Objects.AP.AP1099HistoryByPayer.BAccountID : Edm.Int32
PX.Objects.AP.AP1099HistoryByPayer.VendorID : Edm.Int32
PX.Objects.AP.AP1099HistoryByPayer.FinYear : Edm.String
PX.Objects.AP.AP1099HistoryByPayer.BoxNbr : Edm.Int16
PX.Objects.AP.AP1099HistoryByPayer.HistAmt : Edm.Decimal

# PX.Objects.AP.AP1099Year (EntityType)

Label: "AP 1099 Year"
Key: FinYear, OrganizationID
Entity sets: PX_Objects_AP_AP1099Year, AP1099Year

PX.Objects.AP.AP1099Year.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.AP.AP1099Year.FinYear : Edm.String [key] "1099 Year"
PX.Objects.AP.AP1099Year.StartDate : Edm.String
PX.Objects.AP.AP1099Year.EndDate : Edm.String
PX.Objects.AP.AP1099Year.Status : Edm.String "Status"
PX.Objects.AP.AP1099Year.tstamp : Edm.Binary
PX.Objects.AP.AP1099Year.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.AP.AP1099Year.AP1099HistCollection -> Collection(PX.Objects.AP.Overrides.APDocumentRelease.AP1099Hist)

# PX.Objects.AP.APAddItemSelected (EntityType)

Key: InventoryID
Entity sets: PX_Objects_AP_APAddItemSelected
Non-filterable, non-selectable: CuryID, CuryInfoID, CuryUnitPrice, CuryRate, CuryViewState

PX.Objects.AP.APAddItemSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AP.APAddItemSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.AP.APAddItemSelected.Descr : Edm.String "Description"
PX.Objects.AP.APAddItemSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.AP.APAddItemSelected.ItemClassCD : Edm.String
PX.Objects.AP.APAddItemSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.AP.APAddItemSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.AP.APAddItemSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.AP.APAddItemSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.AP.APAddItemSelected.CuryID : Edm.String "Currency"
PX.Objects.AP.APAddItemSelected.CuryInfoID : Edm.Int64
PX.Objects.AP.APAddItemSelected.CuryUnitPrice : Edm.Decimal "Last Unit Price"
PX.Objects.AP.APAddItemSelected.ProductWorkgroupID : Edm.Int32 "Product Workgroup"
PX.Objects.AP.APAddItemSelected.ProductManagerID : Edm.Int32 "Product Manager"
PX.Objects.AP.APAddItemSelected.NoteID : Edm.Guid
PX.Objects.AP.APAddItemSelected.CuryRate : Edm.Decimal
PX.Objects.AP.APAddItemSelected.CuryViewState : Edm.Boolean
PX.Objects.AP.APAddItemSelected.EPCompanyTreeByProductWorkgroupID -> PX.TM.EPCompanyTree (ProductWorkgroupID=WorkGroupID)
PX.Objects.AP.APAddItemSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AP.APAddItemSelected.EPCompanyTreeByPriceWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.AP.APAddItemSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.AP.APAddItemSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.AP.APAddItemSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.AP.APAddress (EntityType)

Label: "AP Address"
Key: AddressID
Entity sets: PX_Objects_AP_APAddress, APAddress
Non-filterable, non-selectable: OverrideAddress

PX.Objects.AP.APAddress.AddressID : Edm.Int32 [key] "Address ID"
PX.Objects.AP.APAddress.VendorID : Edm.Int32
PX.Objects.AP.APAddress.VendorAddressID : Edm.Int32
PX.Objects.AP.APAddress.IsDefaultAddress : Edm.Boolean [required] "Vendor Default"
PX.Objects.AP.APAddress.OverrideAddress : Edm.Boolean "Override Address"
PX.Objects.AP.APAddress.RevisionID : Edm.Int32 [required]
PX.Objects.AP.APAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.AP.APAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.AP.APAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.AP.APAddress.City : Edm.String "City"
PX.Objects.AP.APAddress.CountryID : Edm.String "Country"
PX.Objects.AP.APAddress.State : Edm.String "State"
PX.Objects.AP.APAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.AP.APAddress.Department : Edm.String "Department"
PX.Objects.AP.APAddress.SubDepartment : Edm.String "Subdepartment"
PX.Objects.AP.APAddress.StreetName : Edm.String "Street Name"
PX.Objects.AP.APAddress.BuildingNumber : Edm.String "Building Number"
PX.Objects.AP.APAddress.BuildingName : Edm.String "Building Name"
PX.Objects.AP.APAddress.Floor : Edm.String "Floor"
PX.Objects.AP.APAddress.UnitNumber : Edm.String "Unit Number"
PX.Objects.AP.APAddress.PostBox : Edm.String "Post Box"
PX.Objects.AP.APAddress.Room : Edm.String "Room"
PX.Objects.AP.APAddress.TownLocationName : Edm.String "Town Location Name"
PX.Objects.AP.APAddress.DistrictName : Edm.String "District Name"
PX.Objects.AP.APAddress.AddressType : Edm.String "Address Type"
PX.Objects.AP.APAddress.CareOf : Edm.String "Care Of"
PX.Objects.AP.APAddress.NoteID : Edm.Guid
PX.Objects.AP.APAddress.tstamp : Edm.Binary
PX.Objects.AP.APAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APAddress.CreatedByScreenID : Edm.String
PX.Objects.AP.APAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APAddress.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APAddress.Latitude : Edm.Decimal "Latitude"
PX.Objects.AP.APAddress.Longitude : Edm.Decimal "Longitude"
PX.Objects.AP.APAddress.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APAddress.AddressByVendorAddressID -> PX.Objects.CR.Address (VendorAddressID=AddressID)
PX.Objects.AP.APAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.AP.APAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)

# PX.Objects.AP.APAdjust (EntityType)

Label: "Adjust"
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr
Entity sets: PX_Objects_AP_APAdjust, Adjust, APAdjust
Non-filterable, non-selectable: SeparateCheck, PrintAdjgDocType, AdjdCuryID, PrintAdjdDocType, CuryRGOLAmt, DisplayRGOLAmt, NoteText, CuryOrigDocAmt, OrigDocAmt, CuryDocBal, CuryAdjustedDocBal, AdjustedDocBal, DocBal, CuryDiscBal, CuryAdjustedDiscBal, DiscBal, CuryWhTaxBal, CuryAdjustedWhTaxBal, WhTaxBal, VoidAppl, AdjType, PPDVATAdjDescription, DisplayDocType, DisplayRefNbr, DisplayDocDate, DisplayDocDesc, DisplayCuryID, DisplayCuryInfoID, DisplayFinPeriodID, DisplayStatus, DisplayCuryAmt, DisplayCuryDiscAmt, DisplayCuryPPDAmt, DisplayCuryWhTaxAmt

PX.Objects.AP.APAdjust.SeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.AP.APAdjust.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APAdjust.AdjgDocType : Edm.String [key] "AdjgDocType"
PX.Objects.AP.APAdjust.PrintAdjgDocType : Edm.String "Type"
PX.Objects.AP.APAdjust.AdjgRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APAdjust.AdjgBranchID : Edm.Int32 "Branch"
PX.Objects.AP.APAdjust.AdjdCuryInfoID : Edm.Int64
PX.Objects.AP.APAdjust.AdjdCuryID : Edm.String "Currency"
PX.Objects.AP.APAdjust.AdjdDocType : Edm.String [key required] "Document Type"
PX.Objects.AP.APAdjust.PrintAdjdDocType : Edm.String "Type"
PX.Objects.AP.APAdjust.AdjdRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APAdjust.AdjdLineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AP.APAdjust.AdjNbr : Edm.Int32 [key] "Adjustment Nbr."
PX.Objects.AP.APAdjust.CashAccountID : Edm.Int32
PX.Objects.AP.APAdjust.PaymentMethodID : Edm.String
PX.Objects.AP.APAdjust.StubNbr : Edm.String "Check Number"
PX.Objects.AP.APAdjust.AdjBatchNbr : Edm.String "Batch Number"
PX.Objects.AP.APAdjust.VoidAdjNbr : Edm.Int32
PX.Objects.AP.APAdjust.AdjdOrigCuryInfoID : Edm.Int64
PX.Objects.AP.APAdjust.AdjgCuryInfoID : Edm.Int64
PX.Objects.AP.APAdjust.AdjgDocDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.AP.APAdjust.AdjgFinPeriodID : Edm.String "Application Period"
PX.Objects.AP.APAdjust.AdjgTranPeriodID : Edm.String "Post Period"
PX.Objects.AP.APAdjust.AdjdDocDate : Edm.DateTimeOffset "Date"
PX.Objects.AP.APAdjust.AdjdFinPeriodID : Edm.String "Post Period"
PX.Objects.AP.APAdjust.AdjdTranPeriodID : Edm.String
PX.Objects.AP.APAdjust.CuryAdjgDiscAmt : Edm.Decimal "Cash Discount Taken in Payment Currency"
PX.Objects.AP.APAdjust.CuryAdjgWhTaxAmt : Edm.Decimal [required] "With. Tax in Payment Currency"
PX.Objects.AP.APAdjust.CuryAdjgAmt : Edm.Decimal "Amount Paid in Payment Currency"
PX.Objects.AP.APAdjust.AdjDiscAmt : Edm.Decimal
PX.Objects.AP.APAdjust.CuryAdjdDiscAmt : Edm.Decimal
PX.Objects.AP.APAdjust.AdjWhTaxAmt : Edm.Decimal [required] "Withholding Tax Amount"
PX.Objects.AP.APAdjust.CuryAdjdWhTaxAmt : Edm.Decimal [required] "With. Tax"
PX.Objects.AP.APAdjust.AdjAmt : Edm.Decimal "Amount"
PX.Objects.AP.APAdjust.CuryAdjdAmt : Edm.Decimal "Amount Paid"
PX.Objects.AP.APAdjust.CuryRGOLAmt : Edm.Decimal "RGOL Amount"
PX.Objects.AP.APAdjust.DisplayRGOLAmt : Edm.Decimal
PX.Objects.AP.APAdjust.RGOLAmt : Edm.Decimal
PX.Objects.AP.APAdjust.Released : Edm.Boolean [required] "Released"
PX.Objects.AP.APAdjust.Hold : Edm.Boolean [required]
PX.Objects.AP.APAdjust.Voided : Edm.Boolean [required]
PX.Objects.AP.APAdjust.tstamp : Edm.Binary
PX.Objects.AP.APAdjust.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APAdjust.CreatedByScreenID : Edm.String
PX.Objects.AP.APAdjust.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APAdjust.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APAdjust.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APAdjust.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APAdjust.NoteID : Edm.Guid
PX.Objects.AP.APAdjust.NoteText : Edm.String "Note Text"
PX.Objects.AP.APAdjust.InvoiceID : Edm.Guid
PX.Objects.AP.APAdjust.PaymentID : Edm.Guid
PX.Objects.AP.APAdjust.MemoID : Edm.Guid
PX.Objects.AP.APAdjust.CuryOrigDocAmt : Edm.Decimal
PX.Objects.AP.APAdjust.OrigDocAmt : Edm.Decimal
PX.Objects.AP.APAdjust.CuryDocBal : Edm.Decimal "Balance"
PX.Objects.AP.APAdjust.CuryAdjustedDocBal : Edm.Decimal "Balance"
PX.Objects.AP.APAdjust.AdjustedDocBal : Edm.Decimal
PX.Objects.AP.APAdjust.DocBal : Edm.Decimal
PX.Objects.AP.APAdjust.CuryDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.AP.APAdjust.CuryAdjustedDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.AP.APAdjust.DiscBal : Edm.Decimal
PX.Objects.AP.APAdjust.CuryWhTaxBal : Edm.Decimal "With. Tax Balance"
PX.Objects.AP.APAdjust.CuryAdjustedWhTaxBal : Edm.Decimal "With. Tax Balance"
PX.Objects.AP.APAdjust.WhTaxBal : Edm.Decimal
PX.Objects.AP.APAdjust.VoidAppl : Edm.Boolean "Void Application"
PX.Objects.AP.APAdjust.TaxInvoiceNbr : Edm.String "Tax Doc. Nbr"
PX.Objects.AP.APAdjust.AdjType : Edm.String
PX.Objects.AP.APAdjust.JointPayeeID : Edm.Int32
PX.Objects.AP.APAdjust.IsMigratedRecord : Edm.Boolean
PX.Objects.AP.APAdjust.IsInitialApplication : Edm.Boolean [required]
PX.Objects.AP.APAdjust.PendingPPD : Edm.Boolean [required] "Subject to Tax Adjustment"
PX.Objects.AP.APAdjust.PPDVATAdjRefNbr : Edm.String
PX.Objects.AP.APAdjust.PPDVATAdjDocType : Edm.String
PX.Objects.AP.APAdjust.PPDVATAdjDescription : Edm.String "Tax Adjustment"
PX.Objects.AP.APAdjust.AdjdHasPPDTaxes : Edm.Boolean
PX.Objects.AP.APAdjust.AdjPPDAmt : Edm.Decimal
PX.Objects.AP.APAdjust.CuryAdjdPPDAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AP.APAdjust.CuryAdjgPPDAmt : Edm.Decimal "Cash Discount Taken in Payment Currency"
PX.Objects.AP.APAdjust.DisplayDocType : Edm.String "Doc. Type"
PX.Objects.AP.APAdjust.DisplayRefNbr : Edm.String "Reference Nbr."
PX.Objects.AP.APAdjust.DisplayDocDate : Edm.DateTimeOffset "Date"
PX.Objects.AP.APAdjust.DisplayDocDesc : Edm.String "Description"
PX.Objects.AP.APAdjust.DisplayCuryID : Edm.String "Currency"
PX.Objects.AP.APAdjust.DisplayCuryInfoID : Edm.Int64
PX.Objects.AP.APAdjust.DisplayFinPeriodID : Edm.String "Post Period"
PX.Objects.AP.APAdjust.DisplayStatus : Edm.String "Status"
PX.Objects.AP.APAdjust.DisplayCuryAmt : Edm.Decimal "Amount Paid"
PX.Objects.AP.APAdjust.DisplayCuryDiscAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AP.APAdjust.DisplayCuryPPDAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AP.APAdjust.DisplayCuryWhTaxAmt : Edm.Decimal "With. Tax"
PX.Objects.AP.APAdjust.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APAdjust.APInvoiceByAdjdRefNbr -> PX.Objects.AP.APInvoice (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.AP.APAdjust.APInvoiceByAdjdDocType -> PX.Objects.AP.APInvoice (AdjdRefNbr=RefNbr, AdjdDocType=DocType)
PX.Objects.AP.APAdjust.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APAdjust.BatchByAdjBatchNbr -> PX.Objects.GL.Batch (AdjBatchNbr=BatchNbr)
PX.Objects.AP.APAdjust.APRegisterByAdjgRefNbr -> PX.Objects.AP.APRegister (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.AP.APAdjust.APRegisterByAdjdRefNbr -> PX.Objects.AP.APRegister (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.AP.APAdjust.APRegisterByPPDVATAdjRefNbr -> PX.Objects.AP.APRegister (PPDVATAdjRefNbr=RefNbr)
PX.Objects.AP.APAdjust.APRegisterByAdjdDocType -> PX.Objects.AP.APRegister (AdjdRefNbr=RefNbr, AdjdDocType=DocType)
PX.Objects.AP.APAdjust.APRegisterByAdjgDocType -> PX.Objects.AP.APRegister (AdjgRefNbr=RefNbr, AdjgDocType=DocType)
PX.Objects.AP.APAdjust.BranchByAdjgBranchID -> PX.Objects.GL.Branch (AdjgBranchID=BranchID)
PX.Objects.AP.APAdjust.BranchByAdjdBranchID -> PX.Objects.GL.Branch
PX.Objects.AP.APAdjust.CurrencyInfoByAdjgCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjgCuryInfoID=CuryInfoID)
PX.Objects.AP.APAdjust.CurrencyInfoByAdjdCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdCuryInfoID=CuryInfoID)
PX.Objects.AP.APAdjust.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APAdjust.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APAdjust.AccountByAdjdWhTaxAcctID -> PX.Objects.GL.Account
PX.Objects.AP.APAdjust.AccountByAdjdAPAcct -> PX.Objects.GL.Account
PX.Objects.AP.APAdjust.SubByAdjdWhTaxSubID -> PX.Objects.GL.Sub
PX.Objects.AP.APAdjust.SubByAdjdAPSub -> PX.Objects.GL.Sub
PX.Objects.AP.APAdjust.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.AP.APAdjust.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AP.APAdjust.APTranByAdjdRefNbr -> PX.Objects.AP.APTran (AdjdLineNbr=LineNbr, AdjdDocType=TranType, AdjdRefNbr=RefNbr)
PX.Objects.AP.APAdjust.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.AP.APAdjust.APAdjustEFileRevisionCollection -> Collection(PX.Objects.Localizations.CA.APAdjustEFileRevision)

# PX.Objects.AP.APAdjustedBalanceAtDate (EntityType)

Label: "APAdjustedBalanceAtDate"
Key: DocType, RefNbr, SubmissionDate
Entity sets: PX_Objects_AP_APAdjustedBalanceAtDate, APAdjustedBalanceAtDate
Non-filterable, non-selectable: CuryLineTotal

PX.Objects.AP.APAdjustedBalanceAtDate.DocType : Edm.String [key]
PX.Objects.AP.APAdjustedBalanceAtDate.RefNbr : Edm.String [key]
PX.Objects.AP.APAdjustedBalanceAtDate.SubmissionDate : Edm.DateTimeOffset [key]
PX.Objects.AP.APAdjustedBalanceAtDate.LineTotal : Edm.Decimal
PX.Objects.AP.APAdjustedBalanceAtDate.CuryLineTotal : Edm.Decimal
PX.Objects.AP.APAdjustedBalanceAtDate.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.AP.APAdjustedBalanceAtDate.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AP.APAdjustedBalanceAtDate.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AP.APAdjustedBalanceAtDate.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.APAdjustedBalanceAtDate.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.AP.APAdjustedBalanceAtDate.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.AP.APAdjustedBalanceAtDate.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.AP.APAdjustedBalanceAtDate.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.AP.APAdjustedBalanceAtDate.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.AP.APAdjustedBalanceAtDate.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AP.APAdjustedBalanceAtDate.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.AP.APAdjustedBalanceAtDate.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.AP.APAdjustedBalanceAtDate.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.AP.APAdjustedBalanceAtDate.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.AP.APAdjustedBalanceAtDate.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.AP.APAdjustedBalanceAtDate.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.AP.APAdjustedBalanceAtDate.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.AP.APAdjustedBalanceAtDate.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.AP.APAdjustingBalanceAtDate (EntityType)

Label: "APAdjustingBalanceAtDate"
Key: DocType, RefNbr, SubmissionDate
Entity sets: PX_Objects_AP_APAdjustingBalanceAtDate, APAdjustingBalanceAtDate
Non-filterable, non-selectable: CuryLineTotal

PX.Objects.AP.APAdjustingBalanceAtDate.DocType : Edm.String [key]
PX.Objects.AP.APAdjustingBalanceAtDate.RefNbr : Edm.String [key]
PX.Objects.AP.APAdjustingBalanceAtDate.SubmissionDate : Edm.DateTimeOffset [key]
PX.Objects.AP.APAdjustingBalanceAtDate.LineTotal : Edm.Decimal
PX.Objects.AP.APAdjustingBalanceAtDate.CuryLineTotal : Edm.Decimal
PX.Objects.AP.APAdjustingBalanceAtDate.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.AP.APAdjustingBalanceAtDate.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AP.APAdjustingBalanceAtDate.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AP.APAdjustingBalanceAtDate.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.APAdjustingBalanceAtDate.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.AP.APAdjustingBalanceAtDate.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.AP.APAdjustingBalanceAtDate.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.AP.APAdjustingBalanceAtDate.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.AP.APAdjustingBalanceAtDate.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.AP.APAdjustingBalanceAtDate.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AP.APAdjustingBalanceAtDate.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.AP.APAdjustingBalanceAtDate.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.AP.APAdjustingBalanceAtDate.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.AP.APAdjustingBalanceAtDate.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.AP.APAdjustingBalanceAtDate.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.AP.APAdjustingBalanceAtDate.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.AP.APAdjustingBalanceAtDate.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.AP.APAdjustingBalanceAtDate.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.AP.APAROrd (EntityType)

Label: "APAROrd"
Key: Ord
Entity sets: PX_Objects_AP_APAROrd, APAROrd

PX.Objects.AP.APAROrd.Ord : Edm.Int16 [key]

# PX.Objects.AP.APCashRequirementsReport (EntityType)

Label: "Cash Requirement"
Key: DocType, RefNbr
Entity sets: PX_Objects_AP_APCashRequirementsReport, CashRequirement, APCashRequirementsReport
Non-filterable, non-selectable: PrintDocType, CuryPayOrigDocAmt, CuryPayDocBal, CuryPayDiscBal, SignBalance

PX.Objects.AP.APCashRequirementsReport.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APCashRequirementsReport.PayTypeID : Edm.String "Payment Method"
PX.Objects.AP.APCashRequirementsReport.TermsID : Edm.String
PX.Objects.AP.APCashRequirementsReport.DocType : Edm.String [key]
PX.Objects.AP.APCashRequirementsReport.PrintDocType : Edm.String "Type"
PX.Objects.AP.APCashRequirementsReport.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APCashRequirementsReport.InvoiceNbr : Edm.String "Vendor Ref."
PX.Objects.AP.APCashRequirementsReport.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AP.APCashRequirementsReport.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.AP.APCashRequirementsReport.PayDate : Edm.DateTimeOffset
PX.Objects.AP.APCashRequirementsReport.PaySel : Edm.Boolean "Approved for Payment"
PX.Objects.AP.APCashRequirementsReport.EstPayDate : Edm.DateTimeOffset "Estimated Pay Date"
PX.Objects.AP.APCashRequirementsReport.DocDesc : Edm.String
PX.Objects.AP.APCashRequirementsReport.CuryInfoID : Edm.Int64
PX.Objects.AP.APCashRequirementsReport.CuryRateType : Edm.String
PX.Objects.AP.APCashRequirementsReport.BaseCuryID : Edm.String
PX.Objects.AP.APCashRequirementsReport.CashCuryID : Edm.String "Cash Account Currency"
PX.Objects.AP.APCashRequirementsReport.DocCuryID : Edm.String "Document Currency"
PX.Objects.AP.APCashRequirementsReport.OrigCuryMultDiv : Edm.String
PX.Objects.AP.APCashRequirementsReport.OrigCuryRate : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.CuryOrigDocAmt : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.OrigDocAmt : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.CuryDocBal : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.DocBal : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.CuryDiscBal : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.DiscBal : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.CuryPayOrigDocAmt : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.PayOrigDocAmt : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.CuryPayDocBal : Edm.Decimal "Balance"
PX.Objects.AP.APCashRequirementsReport.PayDocBal : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.CuryPayDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.AP.APCashRequirementsReport.PayDiscBal : Edm.Decimal
PX.Objects.AP.APCashRequirementsReport.SignBalance : Edm.Decimal "SignBalance"
PX.Objects.AP.APCashRequirementsReport.InvoicePayTypeID : Edm.String "Payment Method"
PX.Objects.AP.APCashRequirementsReport.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AP.APCashRequirementsReport.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APCashRequirementsReport.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AP.APCashRequirementsReport.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.AP.APCashRequirementsReport.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.APCashRequirementsReport.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.AP.APCashRequirementsReport.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AP.APCashRequirementsReport.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AP.APCashRequirementsReport.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AP.APCashRequirementsReport.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.AP.APCashRequirementsReport.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.AP.APCashRequirementsReport.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.AP.APCashRequirementsReport.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.AP.APCashRequirementsReport.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.AP.APCashRequirementsReport.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.AP.APCashRequirementsReport.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.AP.APCashRequirementsReport.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.Objects.AP.APCashRequirementsReport.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.AP.APCashRequirementsReport.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.AP.APCashRequirementsReport.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.AP.APCashRequirementsReport.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.AP.APCashRequirementsReport.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.AP.APCashRequirementsReport.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.AP.APCashRequirementsReport.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.AP.APCashRequirementsReport.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.AP.APCashRequirementsReport.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)

# PX.Objects.AP.APContact (EntityType)

Label: "AP Contact"
Key: ContactID
Entity sets: PX_Objects_AP_APContact, APContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.AP.APContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.AP.APContact.VendorID : Edm.Int32
PX.Objects.AP.APContact.VendorContactID : Edm.Int32
PX.Objects.AP.APContact.IsDefaultContact : Edm.Boolean [required] "Default Vendor Contact"
PX.Objects.AP.APContact.OverrideContact : Edm.Boolean "Override Contact"
PX.Objects.AP.APContact.RevisionID : Edm.Int32 [required]
PX.Objects.AP.APContact.Title : Edm.String "Title"
PX.Objects.AP.APContact.Salutation : Edm.String "Job Title"
PX.Objects.AP.APContact.Attention : Edm.String "Attention"
PX.Objects.AP.APContact.FullName : Edm.String "Account Name"
PX.Objects.AP.APContact.Email : Edm.String "Email"
PX.Objects.AP.APContact.Fax : Edm.String "Fax"
PX.Objects.AP.APContact.FaxType : Edm.String "Fax"
PX.Objects.AP.APContact.Phone1 : Edm.String "Phone 1"
PX.Objects.AP.APContact.Phone1Type : Edm.String "Phone 1"
PX.Objects.AP.APContact.Phone2 : Edm.String "Phone 2"
PX.Objects.AP.APContact.Phone2Type : Edm.String "Phone 2"
PX.Objects.AP.APContact.Phone3 : Edm.String "Phone 3"
PX.Objects.AP.APContact.Phone3Type : Edm.String "Phone 3"
PX.Objects.AP.APContact.NoteID : Edm.Guid
PX.Objects.AP.APContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APContact.CreatedByScreenID : Edm.String
PX.Objects.AP.APContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AP.APContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APContact.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AP.APContact.tstamp : Edm.Binary
PX.Objects.AP.APContact.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APContact.ContactByVendorContactID -> PX.Objects.CR.Contact (VendorContactID=ContactID)
PX.Objects.AP.APContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APContact.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.AP.APContact.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)

# PX.Objects.AP.APDiscount (EntityType)

Label: "AP Discount"
Key: BAccountID, DiscountID
Entity sets: PX_Objects_AP_APDiscount, APDiscount

PX.Objects.AP.APDiscount.BAccountID : Edm.Int32 [key]
PX.Objects.AP.APDiscount.DiscountID : Edm.String [key] "Discount Code"
PX.Objects.AP.APDiscount.Description : Edm.String "Description"
PX.Objects.AP.APDiscount.Type : Edm.String "Discount Type"
PX.Objects.AP.APDiscount.ApplicableTo : Edm.String "Applicable To"
PX.Objects.AP.APDiscount.IsManual : Edm.Boolean [required] "Manual"
PX.Objects.AP.APDiscount.ExcludeFromDiscountableAmt : Edm.Boolean [required] "Exclude from Discountable Amount"
PX.Objects.AP.APDiscount.SkipDocumentDiscounts : Edm.Boolean [required] "Skip Document Discounts"
PX.Objects.AP.APDiscount.IsAutoNumber : Edm.Boolean [required] "Auto-Numbering"
PX.Objects.AP.APDiscount.LastNumber : Edm.String "Last Number"
PX.Objects.AP.APDiscount.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APDiscount.CreatedByScreenID : Edm.String
PX.Objects.AP.APDiscount.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AP.APDiscount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APDiscount.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APDiscount.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AP.APDiscount.tstamp : Edm.Binary
PX.Objects.AP.APDiscount.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.AP.APDiscount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APDiscount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APDiscount.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.AP.APDiscount.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.Objects.AP.APDiscount.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.APDiscount.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.AP.APDiscount.APDiscountVendorCollection -> Collection(PX.Objects.AP.APDiscountVendor)
PX.Objects.AP.APDiscount.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.AP.APDiscount.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.AP.APDiscount.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.AP.APDiscount.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.AP.APDiscountLocation (EntityType)

Label: "AP Discount Location"
Key: DiscountID, DiscountSequenceID, VendorID
Entity sets: PX_Objects_AP_APDiscountLocation, APDiscountLocation

PX.Objects.AP.APDiscountLocation.DiscountID : Edm.String [key] "DiscountID"
PX.Objects.AP.APDiscountLocation.DiscountSequenceID : Edm.String [key] "DiscountSequenceID"
PX.Objects.AP.APDiscountLocation.VendorID : Edm.Int32 [key]
PX.Objects.AP.APDiscountLocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APDiscountLocation.CreatedByScreenID : Edm.String
PX.Objects.AP.APDiscountLocation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APDiscountLocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APDiscountLocation.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APDiscountLocation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APDiscountLocation.tstamp : Edm.Binary
PX.Objects.AP.APDiscountLocation.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APDiscountLocation.VendorDiscountSequenceByDiscountSequenceID -> PX.Objects.AP.VendorDiscountSequence (VendorID=VendorID, DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AP.APDiscountLocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APDiscountLocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APDiscountLocation.LocationByLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)

# PX.Objects.AP.APDiscountVendor (EntityType)

Label: "AP Discount Vendor"
Key: DiscountID, DiscountSequenceID, VendorID
Entity sets: PX_Objects_AP_APDiscountVendor, APDiscountVendor

PX.Objects.AP.APDiscountVendor.DiscountID : Edm.String [key]
PX.Objects.AP.APDiscountVendor.DiscountSequenceID : Edm.String [key]
PX.Objects.AP.APDiscountVendor.VendorID : Edm.Int32 [key]
PX.Objects.AP.APDiscountVendor.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APDiscountVendor.CreatedByScreenID : Edm.String
PX.Objects.AP.APDiscountVendor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APDiscountVendor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APDiscountVendor.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APDiscountVendor.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APDiscountVendor.tstamp : Edm.Binary
PX.Objects.AP.APDiscountVendor.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APDiscountVendor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APDiscountVendor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APDiscountVendor.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)
PX.Objects.AP.APDiscountVendor.APDiscountByDiscountID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID)

# PX.Objects.AP.APHistory (EntityType)

Label: "AP History"
Key: AccountID, BranchID, FinPeriodID, SubID, VendorID
Entity sets: PX_Objects_AP_APHistory, APHistory
Non-filterable, non-selectable: FinFlag, PtdCrAdjustments, PtdDrAdjustments, PtdPurchases, PtdPayments, PtdDiscTaken, PtdWhTax, PtdRGOL, YtdBalance, BegBalance, PtdDeposits, YtdDeposits, PtdRetainageWithheld, YtdRetainageWithheld, PtdRetainageReleased, YtdRetainageReleased

PX.Objects.AP.APHistory.BranchID : Edm.Int32 [key]
PX.Objects.AP.APHistory.AccountID : Edm.Int32 [key]
PX.Objects.AP.APHistory.SubID : Edm.Int32 [key]
PX.Objects.AP.APHistory.FinPeriodID : Edm.String [key]
PX.Objects.AP.APHistory.VendorID : Edm.Int32 [key] "Vendor ID"
PX.Objects.AP.APHistory.DetDeleted : Edm.Boolean [required]
PX.Objects.AP.APHistory.FinBegBalance : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdPurchases : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdPayments : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdDiscTaken : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdWhTax : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdRGOL : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinYtdBalance : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdDeposits : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinYtdDeposits : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinPtdRevalued : Edm.Decimal [required] "PTD Revalued Amount"
PX.Objects.AP.APHistory.TranBegBalance : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdPurchases : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdPayments : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdDiscTaken : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdWhTax : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdRGOL : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranYtdBalance : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdDeposits : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranYtdDeposits : Edm.Decimal [required]
PX.Objects.AP.APHistory.tstamp : Edm.Binary
PX.Objects.AP.APHistory.FinFlag : Edm.Boolean
PX.Objects.AP.APHistory.PtdCrAdjustments : Edm.Decimal
PX.Objects.AP.APHistory.PtdDrAdjustments : Edm.Decimal
PX.Objects.AP.APHistory.PtdPurchases : Edm.Decimal
PX.Objects.AP.APHistory.PtdPayments : Edm.Decimal
PX.Objects.AP.APHistory.PtdDiscTaken : Edm.Decimal
PX.Objects.AP.APHistory.PtdWhTax : Edm.Decimal
PX.Objects.AP.APHistory.PtdRGOL : Edm.Decimal
PX.Objects.AP.APHistory.YtdBalance : Edm.Decimal
PX.Objects.AP.APHistory.BegBalance : Edm.Decimal
PX.Objects.AP.APHistory.PtdDeposits : Edm.Decimal
PX.Objects.AP.APHistory.YtdDeposits : Edm.Decimal
PX.Objects.AP.APHistory.FinPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.APHistory.PtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.APHistory.YtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.APHistory.FinPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.APHistory.FinYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.APHistory.TranYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.APHistory.PtdRetainageReleased : Edm.Decimal
PX.Objects.AP.APHistory.YtdRetainageReleased : Edm.Decimal
PX.Objects.AP.APHistory.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APHistory.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APHistory.CustomerByVendorID -> PX.Objects.AR.Customer (VendorID=BAccountID)
PX.Objects.AP.APHistory.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AP.APHistory.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.AP.APHistory.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.AP.APHistoryByPeriod (EntityType)

Label: "AP History by Period"
Key: AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID
Entity sets: PX_Objects_AP_APHistoryByPeriod, APHistorybyPeriod

PX.Objects.AP.APHistoryByPeriod.BranchID : Edm.Int32 [key]
PX.Objects.AP.APHistoryByPeriod.VendorID : Edm.Int32 [key] "Vendor"
PX.Objects.AP.APHistoryByPeriod.AccountID : Edm.Int32 [key] "Account"
PX.Objects.AP.APHistoryByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.AP.APHistoryByPeriod.CuryID : Edm.String [key]
PX.Objects.AP.APHistoryByPeriod.LastActivityPeriod : Edm.String
PX.Objects.AP.APHistoryByPeriod.FinPeriodID : Edm.String [key]
PX.Objects.AP.APHistoryByPeriod.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AP.APHistoryByPeriod.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)

# PX.Objects.AP.APHistoryTran (ComplexType)


PX.Objects.AP.APHistoryTran.ID : Edm.Int32
PX.Objects.AP.APHistoryTran.DocType : Edm.String
PX.Objects.AP.APHistoryTran.RefNbr : Edm.String
PX.Objects.AP.APHistoryTran.LineNbr : Edm.Int32
PX.Objects.AP.APHistoryTran.SourceDocType : Edm.String
PX.Objects.AP.APHistoryTran.SourceRefNbr : Edm.String
PX.Objects.AP.APHistoryTran.CuryInfoID : Edm.Int64
PX.Objects.AP.APHistoryTran.VendorID : Edm.Int32
PX.Objects.AP.APHistoryTran.FinPeriodID : Edm.String
PX.Objects.AP.APHistoryTran.TranPeriodID : Edm.String
PX.Objects.AP.APHistoryTran.BatchNbr : Edm.String
PX.Objects.AP.APHistoryTran.Type : Edm.String
PX.Objects.AP.APHistoryTran.TranType : Edm.String
PX.Objects.AP.APHistoryTran.TranRefNbr : Edm.String
PX.Objects.AP.APHistoryTran.IsMigratedRecord : Edm.Boolean
PX.Objects.AP.APHistoryTran.PtdPurchases : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdPayments : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdDrAdjustments : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdCrAdjustments : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdDiscTaken : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdWhTax : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdRGOL : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdDeposits : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.APHistoryTran.PtdRetainageReleased : Edm.Decimal

# PX.Objects.AP.APInvoice (EntityType)

Label: "AP document"
BaseType: PX.Objects.AP.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_APInvoice, APdocument, APInvoice
Non-filterable, non-selectable: PaymentInfoLocationID, ExternalTaxesImportInProgress, DrCr, LCEnabled, HasWithHoldTax, HasUseTax, DetailExtPriceTotal, CuryDetailExtPriceTotal, CuryOrderDiscTotal, OrderDiscTotal, SetWarningOnDiscount

PX.Objects.AP.APInvoice.PaymentInfoLocationID : Edm.Int32
PX.Objects.AP.APInvoice.TermsID : Edm.String "Terms"
PX.Objects.AP.APInvoice.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AP.APInvoice.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.AP.APInvoice.MasterRefNbr : Edm.String
PX.Objects.AP.APInvoice.InstallmentNbr : Edm.Int16
PX.Objects.AP.APInvoice.InstallmentCntr : Edm.Int16 "Number of Installments"
PX.Objects.AP.APInvoice.InvoiceNbr : Edm.String "Vendor Ref."
PX.Objects.AP.APInvoice.InvoiceDate : Edm.DateTimeOffset [required] "Vendor Ref. Date"
PX.Objects.AP.APInvoice.TaxZoneID : Edm.String "Vendor Tax Zone"
PX.Objects.AP.APInvoice.ExternalTaxesImportInProgress : Edm.Boolean
PX.Objects.AP.APInvoice.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.AP.APInvoice.TaxTotal : Edm.Decimal [required]
PX.Objects.AP.APInvoice.CuryLineTotal : Edm.Decimal [required] "Detail Total"
PX.Objects.AP.APInvoice.LineTotal : Edm.Decimal [required]
PX.Objects.AP.APInvoice.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.AP.APInvoice.TaxAmt : Edm.Decimal [required]
PX.Objects.AP.APInvoice.CuryVatExemptTotal : Edm.Decimal [required] "Tax Exempt Total"
PX.Objects.AP.APInvoice.VatExemptTotal : Edm.Decimal [required]
PX.Objects.AP.APInvoice.CuryVatTaxableTotal : Edm.Decimal [required] "Taxable Total"
PX.Objects.AP.APInvoice.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.AP.APInvoice.DrCr : Edm.String
PX.Objects.AP.APInvoice.SeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.AP.APInvoice.PaySel : Edm.Boolean "Approved for Payment"
PX.Objects.AP.APInvoice.PayDate : Edm.DateTimeOffset "Pay Date"
PX.Objects.AP.APInvoice.PayTypeID : Edm.String "Payment Method"
PX.Objects.AP.APInvoice.EstPayDate : Edm.DateTimeOffset
PX.Objects.AP.APInvoice.LCEnabled : Edm.Boolean "LCEnabled"
PX.Objects.AP.APInvoice.HasWithHoldTax : Edm.Boolean
PX.Objects.AP.APInvoice.HasUseTax : Edm.Boolean
PX.Objects.AP.APInvoice.IsTaxDocument : Edm.Boolean
PX.Objects.AP.APInvoice.CuryLineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.AP.APInvoice.LineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.AP.APInvoice.DetailExtPriceTotal : Edm.Decimal
PX.Objects.AP.APInvoice.CuryDetailExtPriceTotal : Edm.Decimal "Detail Total"
PX.Objects.AP.APInvoice.CuryOrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.AP.APInvoice.OrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.AP.APInvoice.SetWarningOnDiscount : Edm.Boolean
PX.Objects.AP.APInvoice.ManualEntry : Edm.Boolean
PX.Objects.AP.APInvoice.DisableAutomaticDiscountCalculation : Edm.Boolean [required] "Disable Automatic Discount Update"
PX.Objects.AP.APInvoice.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.AP.APInvoice.EntityUsageType : Edm.String "Tax Exemption Type"
PX.Objects.AP.APInvoice.Reclassified : Edm.Boolean [required]
PX.Objects.AP.APInvoice.VendorBySuppliedByVendorID -> PX.Objects.AP.Vendor
PX.Objects.AP.APInvoice.ARInvoiceByIntercompanyInvoiceNoteID -> PX.Objects.AR.ARInvoice
PX.Objects.AP.APInvoice.BAccountBySuppliedByVendorID -> PX.Objects.CR.BAccount
PX.Objects.AP.APInvoice.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AP.APInvoice.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.AP.APInvoice.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AP.APInvoice.AccountByPrebookAcctID -> PX.Objects.GL.Account
PX.Objects.AP.APInvoice.SubByPrebookSubID -> PX.Objects.GL.Sub
PX.Objects.AP.APInvoice.CashAccountByPayAccountID -> PX.Objects.CA.CashAccount
PX.Objects.AP.APInvoice.CashAccountByBranchID -> PX.Objects.CA.CashAccount
PX.Objects.AP.APInvoice.PaymentMethodByPayTypeID -> PX.Objects.CA.PaymentMethod (PayTypeID=PaymentMethodID)
PX.Objects.AP.APInvoice.LocationBySuppliedByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.AP.APInvoice.LocationBySuppliedByVendorID -> PX.Objects.CR.Location
PX.Objects.AP.APInvoice.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.AP.APInvoice.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AP.APInvoice.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AP.APInvoice.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.AP.APInvoice.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.AP.APInvoice.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.AP.APInvoice.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.AP.APInvoice.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.AP.APInvoice.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.AP.APInvoice.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.AP.APInvoice.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.Objects.AP.APInvoice.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.AP.APInvoice.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.AP.APInvoice.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.AP.APInvoice.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.AP.APInvoice.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.AP.APInvoice.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)

# PX.Objects.AP.APInvoiceDiscountDetail (EntityType)

Label: "AP Invoice Discount Detail"
Key: DocType, RecordID, RefNbr
Entity sets: PX_Objects_AP_APInvoiceDiscountDetail, APInvoiceDiscountDetail
Non-filterable, non-selectable: IsOrigDocDiscount

PX.Objects.AP.APInvoiceDiscountDetail.DocType : Edm.String [key] "Type"
PX.Objects.AP.APInvoiceDiscountDetail.RecordID : Edm.Int32 [key]
PX.Objects.AP.APInvoiceDiscountDetail.LineNbr : Edm.Int32
PX.Objects.AP.APInvoiceDiscountDetail.SkipDiscount : Edm.Boolean [required] "Skip Discount"
PX.Objects.AP.APInvoiceDiscountDetail.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APInvoiceDiscountDetail.DiscountID : Edm.String "Discount Code"
PX.Objects.AP.APInvoiceDiscountDetail.DiscountSequenceID : Edm.String "Sequence ID"
PX.Objects.AP.APInvoiceDiscountDetail.Type : Edm.String "Type"
PX.Objects.AP.APInvoiceDiscountDetail.CuryInfoID : Edm.Int64
PX.Objects.AP.APInvoiceDiscountDetail.DiscountableAmt : Edm.Decimal
PX.Objects.AP.APInvoiceDiscountDetail.CuryDiscountableAmt : Edm.Decimal "Discountable Amt."
PX.Objects.AP.APInvoiceDiscountDetail.DiscountableQty : Edm.Decimal "Discountable Qty."
PX.Objects.AP.APInvoiceDiscountDetail.DiscountAmt : Edm.Decimal
PX.Objects.AP.APInvoiceDiscountDetail.CuryDiscountAmt : Edm.Decimal "Discount Amt."
PX.Objects.AP.APInvoiceDiscountDetail.DiscountPct : Edm.Decimal "Discount Percent"
PX.Objects.AP.APInvoiceDiscountDetail.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.AP.APInvoiceDiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.AP.APInvoiceDiscountDetail.IsManual : Edm.Boolean [required] "Manual Discount"
PX.Objects.AP.APInvoiceDiscountDetail.IsOrigDocDiscount : Edm.Boolean
PX.Objects.AP.APInvoiceDiscountDetail.ExtDiscCode : Edm.String "External Discount Code"
PX.Objects.AP.APInvoiceDiscountDetail.Description : Edm.String "Description"
PX.Objects.AP.APInvoiceDiscountDetail.OrderType : Edm.String "Order Type"
PX.Objects.AP.APInvoiceDiscountDetail.OrderNbr : Edm.String "PO Order Nbr."
PX.Objects.AP.APInvoiceDiscountDetail.ReceiptType : Edm.String "Receipt Type"
PX.Objects.AP.APInvoiceDiscountDetail.ReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.AP.APInvoiceDiscountDetail.tstamp : Edm.Binary
PX.Objects.AP.APInvoiceDiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APInvoiceDiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.AP.APInvoiceDiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APInvoiceDiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APInvoiceDiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APInvoiceDiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APInvoiceDiscountDetail.RetainedDiscountAmt : Edm.Decimal [required]
PX.Objects.AP.APInvoiceDiscountDetail.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr)
PX.Objects.AP.APInvoiceDiscountDetail.VendorDiscountSequenceByDiscountSequenceID -> PX.Objects.AP.VendorDiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AP.APInvoiceDiscountDetail.VendorDiscountSequenceByDiscountID -> PX.Objects.AP.VendorDiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)
PX.Objects.AP.APInvoiceDiscountDetail.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APInvoiceDiscountDetail.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.AP.APInvoiceDiscountDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APInvoiceDiscountDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APInvoiceDiscountDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APInvoiceDiscountDetail.POReceiptByReceiptType -> PX.Objects.PO.POReceipt (ReceiptNbr=ReceiptNbr, ReceiptType=ReceiptType)
PX.Objects.AP.APInvoiceDiscountDetail.APDiscountByDiscountID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID)

# PX.Objects.AP.APInvoiceExt (EntityType)

Label: "AP document"
BaseType: PX.Objects.AP.APInvoice
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_APInvoiceExt
Non-filterable, non-selectable: LineNbr, DisplayProjectID, CuryRetainageBal, RetainageBal, RetainageReleasePct, CuryRetainageReleasedAmt, RetainageReleasedAmt, CuryRetainageUnreleasedCalcAmt, RetainageUnreleasedCalcAmt

PX.Objects.AP.APInvoiceExt.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.AP.APInvoiceExt.DisplayProjectID : Edm.Int32 "Project"
PX.Objects.AP.APInvoiceExt.CuryRetainageBal : Edm.Decimal
PX.Objects.AP.APInvoiceExt.RetainageBal : Edm.Decimal
PX.Objects.AP.APInvoiceExt.RetainageReleasePct : Edm.Decimal "Percent to Release"
PX.Objects.AP.APInvoiceExt.CuryRetainageReleasedAmt : Edm.Decimal "Retainage to Release"
PX.Objects.AP.APInvoiceExt.RetainageReleasedAmt : Edm.Decimal
PX.Objects.AP.APInvoiceExt.CuryRetainageUnreleasedCalcAmt : Edm.Decimal "Unreleased Retainage"
PX.Objects.AP.APInvoiceExt.RetainageUnreleasedCalcAmt : Edm.Decimal
PX.Objects.AP.APInvoiceExt.APTranLineNbr : Edm.Int32
PX.Objects.AP.APInvoiceExt.APTranCuryOrigRetainageAmt : Edm.Decimal
PX.Objects.AP.APInvoiceExt.APTranOrigRetainageAmt : Edm.Decimal
PX.Objects.AP.APInvoiceExt.APTranCuryRetainageBal : Edm.Decimal
PX.Objects.AP.APInvoiceExt.APTranRetainageBal : Edm.Decimal
PX.Objects.AP.APInvoiceExt.APTranCuryOrigTranAmt : Edm.Decimal
PX.Objects.AP.APInvoiceExt.APTranOrigTranAmt : Edm.Decimal
PX.Objects.AP.APInvoiceExt.PMProjectByAPTranProjectID -> PX.Objects.PM.PMProject
PX.Objects.AP.APInvoiceExt.PMTaskByAPTranTaskID -> PX.Objects.PM.PMTask
PX.Objects.AP.APInvoiceExt.InventoryItemByAPTranInventoryID -> PX.Objects.IN.InventoryItem
PX.Objects.AP.APInvoiceExt.PMCostCodeByAPTranCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.AP.APInvoiceExt.AccountByAPTranAccountID -> PX.Objects.GL.Account

# PX.Objects.AP.APInvoiceRetainageBalanceAtDate (EntityType)

Label: "APInvoiceRetainageBalanceAtDate"
Key: DocType, RefNbr, SubmissionDate
Entity sets: PX_Objects_AP_APInvoiceRetainageBalanceAtDate, APInvoiceRetainageBalanceAtDate

PX.Objects.AP.APInvoiceRetainageBalanceAtDate.DocType : Edm.String [key]
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.RefNbr : Edm.String [key]
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.SubmissionDate : Edm.DateTimeOffset [key]
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.LineTotal : Edm.Decimal
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.AP.APInvoiceRetainageBalanceAtDate.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.AP.APLineTax (EntityType)

Label: "AP Line Tax"
Key: LineNbr, RefNbr, TranType
Entity sets: PX_Objects_AP_APLineTax, APLineTax

PX.Objects.AP.APLineTax.TranType : Edm.String [key]
PX.Objects.AP.APLineTax.RefNbr : Edm.String [key]
PX.Objects.AP.APLineTax.LineNbr : Edm.Int32 [key]
PX.Objects.AP.APLineTax.TaxType : Edm.String
PX.Objects.AP.APLineTax.TaxAmt : Edm.Decimal
PX.Objects.AP.APLineTax.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APLineTax.APTranByLineNbr -> PX.Objects.AP.APTran (TranType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)

# PX.Objects.AP.APNotification (EntityType)

Label: "AP Notification"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_AP_APNotification, APNotification

# PX.Objects.AP.APPayment (EntityType)

Label: "Payment"
BaseType: PX.Objects.AP.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_APPayment, Payment, APPayment
Non-filterable, non-selectable: CuryUnappliedBal, UnappliedBal, CuryApplAmt, ApplAmt, BatchPaymentRefNbr, IsPrintingProcess, IsReleaseCheckProcess, VoidAppl, CanHaveBalance, DrCr, AmountToWords, DepositDate, CuryPOApplAmt, POApplAmt, CuryPOUnreleasedApplAmt, POUnreleasedApplAmt, CuryPOFullApplAmt, POFullApplAmt, IsRequestPrepayment, PaymentCannotbeVoidedMessage, RemittanceInformationMessage, IsExternalPayment

PX.Objects.AP.APPayment.RemitAddressID : Edm.Int32
PX.Objects.AP.APPayment.RemitContactID : Edm.Int32 "Remittance Contact"
PX.Objects.AP.APPayment.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AP.APPayment.JointPayeeID : Edm.Int32
PX.Objects.AP.APPayment.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.AP.APPayment.AdjDate : Edm.DateTimeOffset "Application Date"
PX.Objects.AP.APPayment.AdjFinPeriodID : Edm.String "Application Period"
PX.Objects.AP.APPayment.AdjTranPeriodID : Edm.String
PX.Objects.AP.APPayment.StubCntr : Edm.Int32 [required]
PX.Objects.AP.APPayment.BillCntr : Edm.Int32 [required]
PX.Objects.AP.APPayment.ChargeCntr : Edm.Int32 [required]
PX.Objects.AP.APPayment.CuryUnappliedBal : Edm.Decimal "Unapplied Balance"
PX.Objects.AP.APPayment.UnappliedBal : Edm.Decimal
PX.Objects.AP.APPayment.CuryApplAmt : Edm.Decimal "Application Amount"
PX.Objects.AP.APPayment.ApplAmt : Edm.Decimal
PX.Objects.AP.APPayment.Cleared : Edm.Boolean [required] "Cleared"
PX.Objects.AP.APPayment.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.AP.APPayment.PrintCheck : Edm.Boolean "Print Check"
PX.Objects.AP.APPayment.BatchPaymentRefNbr : Edm.String
PX.Objects.AP.APPayment.IsPrintingProcess : Edm.Boolean
PX.Objects.AP.APPayment.IsReleaseCheckProcess : Edm.Boolean
PX.Objects.AP.APPayment.VoidAppl : Edm.Boolean "Void Application"
PX.Objects.AP.APPayment.CanHaveBalance : Edm.Boolean "Can Have Balance"
PX.Objects.AP.APPayment.DrCr : Edm.String
PX.Objects.AP.APPayment.CATranID : Edm.Int64
PX.Objects.AP.APPayment.AmountToWords : Edm.String
PX.Objects.AP.APPayment.CuryOrigTaxDiscAmt : Edm.Decimal [required]
PX.Objects.AP.APPayment.OrigTaxDiscAmt : Edm.Decimal [required]
PX.Objects.AP.APPayment.DepositAsBatch : Edm.Boolean [required] "Batch Deposit"
PX.Objects.AP.APPayment.DepositAfter : Edm.DateTimeOffset "Deposit After"
PX.Objects.AP.APPayment.Deposited : Edm.Boolean [required] "Deposited"
PX.Objects.AP.APPayment.DepositDate : Edm.DateTimeOffset "Batch Deposit Date"
PX.Objects.AP.APPayment.DepositType : Edm.String "DepositType"
PX.Objects.AP.APPayment.DepositNbr : Edm.String "Batch Deposit Nbr."
PX.Objects.AP.APPayment.CuryPOApplAmt : Edm.Decimal "Applied to Order"
PX.Objects.AP.APPayment.POApplAmt : Edm.Decimal
PX.Objects.AP.APPayment.CuryPOUnreleasedApplAmt : Edm.Decimal
PX.Objects.AP.APPayment.POUnreleasedApplAmt : Edm.Decimal
PX.Objects.AP.APPayment.CuryPOFullApplAmt : Edm.Decimal
PX.Objects.AP.APPayment.POFullApplAmt : Edm.Decimal
PX.Objects.AP.APPayment.IsRequestPrepayment : Edm.Boolean
PX.Objects.AP.APPayment.ExternalPaymentID : Edm.String "External Payment ID"
PX.Objects.AP.APPayment.ExternalPaymentStatus : Edm.String "Processing Status"
PX.Objects.AP.APPayment.ExternalOrganizationID : Edm.String "External Organization ID"
PX.Objects.AP.APPayment.ExternalPaymentCanceled : Edm.Boolean [required]
PX.Objects.AP.APPayment.ExternalPaymentIsVoidable : Edm.Boolean [required]
PX.Objects.AP.APPayment.ExternalPaymentIsFinalState : Edm.Boolean [required]
PX.Objects.AP.APPayment.ExternalPaymentUpdateTime : Edm.DateTimeOffset "Updated On"
PX.Objects.AP.APPayment.ExternalPaymentDisbursementType : Edm.String "Disbursement Method"
PX.Objects.AP.APPayment.ExternalPaymentSentDate : Edm.DateTimeOffset "Sent On"
PX.Objects.AP.APPayment.ExternalPaymentCheckNbr : Edm.String "Check Number"
PX.Objects.AP.APPayment.ExternalPaymentCardNbr : Edm.String "Card Number"
PX.Objects.AP.APPayment.ExternalPaymentTraceNbr : Edm.String "Trace Number"
PX.Objects.AP.APPayment.ExternalPaymentBatchNbr : Edm.String "Batch Number"
PX.Objects.AP.APPayment.PaymentCannotbeVoidedMessage : Edm.String "PaymentCannotbeVoidedMessage"
PX.Objects.AP.APPayment.ExternalCheckDeliveryMethod : Edm.String "Fast Delivery Method"
PX.Objects.AP.APPayment.ExternalCheckPayFaster : Edm.Boolean [required] "Pay Faster"
PX.Objects.AP.APPayment.ExternalRateExpiryDate : Edm.DateTimeOffset "Rate Expires On"
PX.Objects.AP.APPayment.ExternalRate : Edm.Decimal "External Exch. Rate"
PX.Objects.AP.APPayment.ExternalRateCuryID : Edm.String "Disbursement Currency"
PX.Objects.AP.APPayment.ExternalPaymentPaidAmount : Edm.Decimal "Disb. Amount"
PX.Objects.AP.APPayment.ExternalRateBatchId : Edm.Int32 "External Rate Batch ID"
PX.Objects.AP.APPayment.RemittanceInformationMessage : Edm.String "RemittanceInformationMessage"
PX.Objects.AP.APPayment.IsExternalPayment : Edm.Boolean
PX.Objects.AP.APPayment.ExternalPaymentHasChild : Edm.Boolean [required]
PX.Objects.AP.APPayment.ExternalPaymentClearedDate : Edm.DateTimeOffset "Cleared Date"
PX.Objects.AP.APPayment.CATranByCATranID -> PX.Objects.CA.CATran (CATranID=TranID)
PX.Objects.AP.APPayment.ContactByRemitContactID -> PX.Objects.CR.Contact (RemitContactID=ContactID)
PX.Objects.AP.APPayment.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AP.APPayment.AddressByRemitAddressID -> PX.Objects.CR.Address (RemitAddressID=AddressID)
PX.Objects.AP.APPayment.CADepositByDepositType -> PX.Objects.CA.CADeposit (DepositNbr=RefNbr, DepositType=TranType)
PX.Objects.AP.APPayment.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.AP.APPayment.CashAccountByBranchID -> PX.Objects.CA.CashAccount
PX.Objects.AP.APPayment.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AP.APPayment.APContactByRemitContactID -> PX.Objects.AP.APContact (RemitContactID=ContactID)
PX.Objects.AP.APPayment.CABatchDetailCollection -> Collection(PX.Objects.CA.CABatchDetail)
PX.Objects.AP.APPayment.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.AP.APPayment.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AP.APPayment.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.AP.APPayment.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.Objects.AP.APPayment.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.AP.APPayment.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.AP.APPayment.APPrintCheckDetailCollection -> Collection(PX.Objects.AP.APPrintCheckDetail)

# PX.Objects.AP.APPaymentChargeTran (EntityType)

Label: "AP Financial Charge Transaction"
Key: DocType, LineNbr, RefNbr
Entity sets: PX_Objects_AP_APPaymentChargeTran, APFinancialChargeTransaction, APPaymentChargeTran

PX.Objects.AP.APPaymentChargeTran.DocType : Edm.String [key] "DocType"
PX.Objects.AP.APPaymentChargeTran.RefNbr : Edm.String [key]
PX.Objects.AP.APPaymentChargeTran.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AP.APPaymentChargeTran.CashAccountID : Edm.Int32 "Cash Account ID"
PX.Objects.AP.APPaymentChargeTran.DrCr : Edm.String "Disb./Receipt"
PX.Objects.AP.APPaymentChargeTran.ExtRefNbr : Edm.String "ExtRefNbr"
PX.Objects.AP.APPaymentChargeTran.EntryTypeID : Edm.String "Entry Type"
PX.Objects.AP.APPaymentChargeTran.TranDate : Edm.DateTimeOffset "TranDate"
PX.Objects.AP.APPaymentChargeTran.FinPeriodID : Edm.String "FinPeriodID"
PX.Objects.AP.APPaymentChargeTran.TranPeriodID : Edm.String "TranPeriodID"
PX.Objects.AP.APPaymentChargeTran.TranDesc : Edm.String "Description"
PX.Objects.AP.APPaymentChargeTran.CuryInfoID : Edm.Int64
PX.Objects.AP.APPaymentChargeTran.CashTranID : Edm.Int64
PX.Objects.AP.APPaymentChargeTran.CuryTranAmt : Edm.Decimal [required] "Amount"
PX.Objects.AP.APPaymentChargeTran.TranAmt : Edm.Decimal [required]
PX.Objects.AP.APPaymentChargeTran.Released : Edm.Boolean [required] "Released"
PX.Objects.AP.APPaymentChargeTran.Cleared : Edm.Boolean [required] "Cleared"
PX.Objects.AP.APPaymentChargeTran.ClearDate : Edm.DateTimeOffset "ClearDate"
PX.Objects.AP.APPaymentChargeTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APPaymentChargeTran.CreatedByScreenID : Edm.String
PX.Objects.AP.APPaymentChargeTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APPaymentChargeTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APPaymentChargeTran.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APPaymentChargeTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APPaymentChargeTran.tstamp : Edm.Binary
PX.Objects.AP.APPaymentChargeTran.CATranByCashTranID -> PX.Objects.CA.CATran (CashTranID=TranID)
PX.Objects.AP.APPaymentChargeTran.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APPaymentChargeTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APPaymentChargeTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APPaymentChargeTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APPaymentChargeTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.AP.APPaymentChargeTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AP.APPaymentChargeTran.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.AP.APPaymentChargeTran.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)

# PX.Objects.AP.APPayNotSelReport (EntityType)

Label: "Bill For Approval"
Key: DocType, RefNbr
Entity sets: PX_Objects_AP_APPayNotSelReport, BillForApproval, APPayNotSelReport
Non-filterable, non-selectable: PrintDocType, CuryPayDocBal, CuryPayDiscBal, SignBalance

PX.Objects.AP.APPayNotSelReport.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APPayNotSelReport.PayTypeID : Edm.String "Payment Method"
PX.Objects.AP.APPayNotSelReport.TermsID : Edm.String
PX.Objects.AP.APPayNotSelReport.DocType : Edm.String [key]
PX.Objects.AP.APPayNotSelReport.PrintDocType : Edm.String "Type"
PX.Objects.AP.APPayNotSelReport.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APPayNotSelReport.InvoiceNbr : Edm.String "Vendor Ref."
PX.Objects.AP.APPayNotSelReport.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AP.APPayNotSelReport.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.AP.APPayNotSelReport.PayDate : Edm.DateTimeOffset
PX.Objects.AP.APPayNotSelReport.PaySel : Edm.Boolean
PX.Objects.AP.APPayNotSelReport.CuryInfoID : Edm.Int64
PX.Objects.AP.APPayNotSelReport.BaseCuryID : Edm.String
PX.Objects.AP.APPayNotSelReport.CuryRateType : Edm.String
PX.Objects.AP.APPayNotSelReport.CashCuryID : Edm.String "Cash Account Currency"
PX.Objects.AP.APPayNotSelReport.DocCuryID : Edm.String "Document Currency"
PX.Objects.AP.APPayNotSelReport.OrigCuryMultDiv : Edm.String
PX.Objects.AP.APPayNotSelReport.OrigCuryRate : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.CuryOrigDocAmt : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.OrigDocAmt : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.CuryDocBal : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.DocBal : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.CuryDiscBal : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.DiscBal : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.CuryPayOrigDocAmt : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.PayOrigDocAmt : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.CuryPayDocBal : Edm.Decimal "Balance"
PX.Objects.AP.APPayNotSelReport.PayDocBal : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.CuryPayDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.AP.APPayNotSelReport.PayDiscBal : Edm.Decimal
PX.Objects.AP.APPayNotSelReport.SignBalance : Edm.Decimal "SignBalance"
PX.Objects.AP.APPayNotSelReport.SuppliedByVendorID : Edm.Int32
PX.Objects.AP.APPayNotSelReport.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APPayNotSelReport.VendorBySuppliedByVendorID -> PX.Objects.AP.Vendor (SuppliedByVendorID=BAccountID)
PX.Objects.AP.APPayNotSelReport.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APPayNotSelReport.BAccountBySuppliedByVendorID -> PX.Objects.CR.BAccount (SuppliedByVendorID=BAccountID)
PX.Objects.AP.APPayNotSelReport.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AP.APPayNotSelReport.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APPayNotSelReport.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AP.APPayNotSelReport.PaymentMethodByPayTypeID -> PX.Objects.CA.PaymentMethod (PayTypeID=PaymentMethodID)
PX.Objects.AP.APPayNotSelReport.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.AP.APPayNotSelReport.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.APPayNotSelReport.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.AP.APPayNotSelReport.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AP.APPayNotSelReport.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AP.APPayNotSelReport.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AP.APPayNotSelReport.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.AP.APPayNotSelReport.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.AP.APPayNotSelReport.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.AP.APPayNotSelReport.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.AP.APPayNotSelReport.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.AP.APPayNotSelReport.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.AP.APPayNotSelReport.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.AP.APPayNotSelReport.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.Objects.AP.APPayNotSelReport.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.AP.APPayNotSelReport.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.AP.APPayNotSelReport.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.AP.APPayNotSelReport.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.AP.APPayNotSelReport.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.AP.APPayNotSelReport.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.AP.APPayNotSelReport.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.AP.APPayNotSelReport.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.AP.APPayNotSelReport.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)

# PX.Objects.AP.APPaySelReport (EntityType)

Label: "Bill For Payment"
Key: DocType, RefNbr
Entity sets: PX_Objects_AP_APPaySelReport, BillForPayment, APPaySelReport
Non-filterable, non-selectable: PrintDocType, CuryPayOrigDocAmt, CuryPayDocBal, CuryPayDiscBal, SignBalance

PX.Objects.AP.APPaySelReport.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APPaySelReport.PayTypeID : Edm.String "Payment Method"
PX.Objects.AP.APPaySelReport.TermsID : Edm.String "Terms"
PX.Objects.AP.APPaySelReport.DocType : Edm.String [key] "Document Type"
PX.Objects.AP.APPaySelReport.PrintDocType : Edm.String "Type"
PX.Objects.AP.APPaySelReport.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APPaySelReport.PayNbr : Edm.String "Payment Nbr."
PX.Objects.AP.APPaySelReport.SeparateCheck : Edm.Boolean "Separate Check"
PX.Objects.AP.APPaySelReport.InvoiceNbr : Edm.String "Vendor Ref."
PX.Objects.AP.APPaySelReport.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AP.APPaySelReport.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.AP.APPaySelReport.PayDate : Edm.DateTimeOffset "Pay Date"
PX.Objects.AP.APPaySelReport.PaySel : Edm.Boolean "Selected"
PX.Objects.AP.APPaySelReport.CuryInfoID : Edm.Int64 "Currency Info"
PX.Objects.AP.APPaySelReport.BaseCuryID : Edm.String "Base Currency ID"
PX.Objects.AP.APPaySelReport.CuryRateType : Edm.String
PX.Objects.AP.APPaySelReport.CashCuryID : Edm.String "Cash Account Currency"
PX.Objects.AP.APPaySelReport.DocCuryID : Edm.String "Document Currency"
PX.Objects.AP.APPaySelReport.OrigCuryMultDiv : Edm.String
PX.Objects.AP.APPaySelReport.OrigCuryRate : Edm.Decimal
PX.Objects.AP.APPaySelReport.CuryOrigDocAmt : Edm.Decimal "Amount"
PX.Objects.AP.APPaySelReport.OrigDocAmt : Edm.Decimal
PX.Objects.AP.APPaySelReport.CuryDocBal : Edm.Decimal
PX.Objects.AP.APPaySelReport.DocBal : Edm.Decimal
PX.Objects.AP.APPaySelReport.CuryDiscBal : Edm.Decimal
PX.Objects.AP.APPaySelReport.DiscBal : Edm.Decimal
PX.Objects.AP.APPaySelReport.CuryPayOrigDocAmt : Edm.Decimal
PX.Objects.AP.APPaySelReport.PayOrigDocAmt : Edm.Decimal
PX.Objects.AP.APPaySelReport.CuryPayDocBal : Edm.Decimal "Balance"
PX.Objects.AP.APPaySelReport.PayDocBal : Edm.Decimal
PX.Objects.AP.APPaySelReport.CuryPayDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.AP.APPaySelReport.PayDiscBal : Edm.Decimal
PX.Objects.AP.APPaySelReport.SignBalance : Edm.Decimal "SignBalance"
PX.Objects.AP.APPaySelReport.SuppliedByVendorID : Edm.Int32
PX.Objects.AP.APPaySelReport.HasMultipleProjects : Edm.Boolean
PX.Objects.AP.APPaySelReport.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APPaySelReport.VendorBySuppliedByVendorID -> PX.Objects.AP.Vendor (SuppliedByVendorID=BAccountID)
PX.Objects.AP.APPaySelReport.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APPaySelReport.BAccountBySuppliedByVendorID -> PX.Objects.CR.BAccount (SuppliedByVendorID=BAccountID)
PX.Objects.AP.APPaySelReport.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AP.APPaySelReport.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APPaySelReport.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AP.APPaySelReport.PaymentMethodByPayTypeID -> PX.Objects.CA.PaymentMethod (PayTypeID=PaymentMethodID)
PX.Objects.AP.APPaySelReport.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.AP.APPaySelReport.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.APPaySelReport.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.AP.APPaySelReport.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AP.APPaySelReport.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AP.APPaySelReport.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AP.APPaySelReport.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.AP.APPaySelReport.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.AP.APPaySelReport.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.AP.APPaySelReport.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.AP.APPaySelReport.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.AP.APPaySelReport.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.AP.APPaySelReport.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.AP.APPaySelReport.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.Objects.AP.APPaySelReport.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.AP.APPaySelReport.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.AP.APPaySelReport.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.AP.APPaySelReport.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.AP.APPaySelReport.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.AP.APPaySelReport.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.AP.APPaySelReport.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.AP.APPaySelReport.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.AP.APPaySelReport.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)

# PX.Objects.AP.APPriceWorksheet (EntityType)

Label: "AP Price Worksheet"
Key: RefNbr
Entity sets: PX_Objects_AP_APPriceWorksheet, APPriceWorksheet
Non-filterable, non-selectable: NoteText

PX.Objects.AP.APPriceWorksheet.Status : Edm.String "Status"
PX.Objects.AP.APPriceWorksheet.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APPriceWorksheet.Hold : Edm.Boolean [required] "Hold"
PX.Objects.AP.APPriceWorksheet.Approved : Edm.Boolean [required] "Approved"
PX.Objects.AP.APPriceWorksheet.Descr : Edm.String "Description"
PX.Objects.AP.APPriceWorksheet.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AP.APPriceWorksheet.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AP.APPriceWorksheet.IsPromotional : Edm.Boolean [required] "Promotional"
PX.Objects.AP.APPriceWorksheet.OverwriteOverlapping : Edm.Boolean [required] "Overwrite Overlapping Prices"
PX.Objects.AP.APPriceWorksheet.NoteID : Edm.Guid
PX.Objects.AP.APPriceWorksheet.NoteText : Edm.String "Note Text"
PX.Objects.AP.APPriceWorksheet.tstamp : Edm.Binary
PX.Objects.AP.APPriceWorksheet.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APPriceWorksheet.CreatedByScreenID : Edm.String
PX.Objects.AP.APPriceWorksheet.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AP.APPriceWorksheet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APPriceWorksheet.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APPriceWorksheet.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AP.APPriceWorksheet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APPriceWorksheet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APPriceWorksheet.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)

# PX.Objects.AP.APPriceWorksheetDetail (EntityType)

Label: "AP Price Worksheet Detail"
Key: LineID, RefNbr
Entity sets: PX_Objects_AP_APPriceWorksheetDetail, APPriceWorksheetDetail
Non-filterable, non-selectable: RestrictInventoryByAlternateID, NoteText

PX.Objects.AP.APPriceWorksheetDetail.LineID : Edm.Int32 [key]
PX.Objects.AP.APPriceWorksheetDetail.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APPriceWorksheetDetail.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APPriceWorksheetDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AP.APPriceWorksheetDetail.InventoryCD : Edm.String
PX.Objects.AP.APPriceWorksheetDetail.AlternateID : Edm.String "Alternate ID"
PX.Objects.AP.APPriceWorksheetDetail.Description : Edm.String "Description"
PX.Objects.AP.APPriceWorksheetDetail.UOM : Edm.String "UOM"
PX.Objects.AP.APPriceWorksheetDetail.BreakQty : Edm.Decimal [required] "Break Qty."
PX.Objects.AP.APPriceWorksheetDetail.CurrentPrice : Edm.Decimal "Source Price"
PX.Objects.AP.APPriceWorksheetDetail.PendingPrice : Edm.Decimal "Pending Price"
PX.Objects.AP.APPriceWorksheetDetail.CuryID : Edm.String "Currency"
PX.Objects.AP.APPriceWorksheetDetail.TaxID : Edm.String "Tax"
PX.Objects.AP.APPriceWorksheetDetail.tstamp : Edm.Binary
PX.Objects.AP.APPriceWorksheetDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APPriceWorksheetDetail.CreatedByScreenID : Edm.String
PX.Objects.AP.APPriceWorksheetDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APPriceWorksheetDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APPriceWorksheetDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APPriceWorksheetDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APPriceWorksheetDetail.RestrictInventoryByAlternateID : Edm.Boolean
PX.Objects.AP.APPriceWorksheetDetail.NoteID : Edm.Guid
PX.Objects.AP.APPriceWorksheetDetail.NoteText : Edm.String "Note Text"
PX.Objects.AP.APPriceWorksheetDetail.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APPriceWorksheetDetail.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APPriceWorksheetDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AP.APPriceWorksheetDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APPriceWorksheetDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APPriceWorksheetDetail.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.AP.APPriceWorksheetDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AP.APPriceWorksheetDetail.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AP.APPriceWorksheetDetail.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AP.APPriceWorksheetDetail.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AP.APPriceWorksheetDetail.APPriceWorksheetByRefNbr -> PX.Objects.AP.APPriceWorksheet (RefNbr=RefNbr)

# PX.Objects.AP.APPrintCheckDetail (EntityType)

Label: "Print Check Detail"
Key: AdjdDocType, AdjdRefNbr, AdjgDocType, AdjgRefNbr, Source
Entity sets: PX_Objects_AP_APPrintCheckDetail, PrintCheckDetail, APPrintCheckDetail
Non-filterable, non-selectable: AdjgCuryID, CuryRate, CuryViewState, AdjdCuryID

PX.Objects.AP.APPrintCheckDetail.AdjgDocType : Edm.String [key]
PX.Objects.AP.APPrintCheckDetail.AdjgRefNbr : Edm.String [key]
PX.Objects.AP.APPrintCheckDetail.Source : Edm.String [key]
PX.Objects.AP.APPrintCheckDetail.AdjdDocType : Edm.String [key]
PX.Objects.AP.APPrintCheckDetail.AdjdRefNbr : Edm.String [key]
PX.Objects.AP.APPrintCheckDetail.StubNbr : Edm.String
PX.Objects.AP.APPrintCheckDetail.CashAccountID : Edm.Int32
PX.Objects.AP.APPrintCheckDetail.PaymentMethodID : Edm.String
PX.Objects.AP.APPrintCheckDetail.AdjgCuryInfoID : Edm.Int64
PX.Objects.AP.APPrintCheckDetail.AdjdCuryInfoID : Edm.Int64
PX.Objects.AP.APPrintCheckDetail.CuryOutstandingBalance : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.OutstandingBalance : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.OutstandingBalanceDate : Edm.DateTimeOffset
PX.Objects.AP.APPrintCheckDetail.CuryAdjgAmt : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.AdjgAmt : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.CuryAdjgDiscAmt : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.AdjgDiscAmt : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.CuryExtraDocBal : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.ExtraDocBal : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APPrintCheckDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APPrintCheckDetail.CreatedByScreenID : Edm.String
PX.Objects.AP.APPrintCheckDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APPrintCheckDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APPrintCheckDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APPrintCheckDetail.tstamp : Edm.Binary
PX.Objects.AP.APPrintCheckDetail.AdjgCuryID : Edm.String "Currency"
PX.Objects.AP.APPrintCheckDetail.CuryRate : Edm.Decimal
PX.Objects.AP.APPrintCheckDetail.CuryViewState : Edm.Boolean
PX.Objects.AP.APPrintCheckDetail.AdjdCuryID : Edm.String "Currency"
PX.Objects.AP.APPrintCheckDetail.APPaymentByAdjgRefNbr -> PX.Objects.AP.APPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.AP.APPrintCheckDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APPrintCheckDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.AP.APPrintCheckDetailWithAdjdDoc (EntityType)

Label: "Print Check Detail with Paid Document"
Key: AdjgDocType, AdjgRefNbr, Source
Entity sets: PX_Objects_AP_APPrintCheckDetailWithAdjdDoc, PrintCheckDetailwithPaidDocument, APPrintCheckDetailWithAdjdDoc
Non-filterable, non-selectable: AdjdPrintDocType

PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjgDocType : Edm.String [key] "Type"
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjgRefNbr : Edm.String [key]
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.CuryAdjgAmt : Edm.Decimal
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.CuryAdjgDiscAmt : Edm.Decimal
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.StubNbr : Edm.String
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdRefNbr : Edm.String
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdDocType : Edm.String
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdPrintDocType : Edm.String "Type"
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdDocNbr : Edm.String
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdDocDate : Edm.DateTimeOffset
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdInvtMult : Edm.Int16
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdCuryOrigDocAmt : Edm.Decimal
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdCuryDocBal : Edm.Decimal
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.AdjdSuppliedByVendorID : Edm.Int32
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.Source : Edm.String [key]
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.OrderBy : Edm.Int16
PX.Objects.AP.APPrintCheckDetailWithAdjdDoc.APPaymentByAdjgRefNbr -> PX.Objects.AP.APPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)

# PX.Objects.AP.APRegister (EntityType)

Label: "Document"
Key: DocType, RefNbr
Entity sets: PX_Objects_AP_APRegister, Document, APRegister
Non-filterable, non-selectable: HiddenKey, InternalDocType, PrintDocType, DocDisc, CuryDocDisc, DocClass, ReleasedToVerify, NoteText, ReleasedOrPrebooked, WorkgroupID, OwnerID, RetainageUnpaidTotal, RetainagePaidTotal, CuryDiscountedDocTotal, DiscountedDocTotal, CuryDiscountedTaxableTotal, DiscountedTaxableTotal, CuryDiscountedPrice, DiscountedPrice, CuryRate, DeletedDatabaseRecord

PX.Objects.AP.APRegister.DocType : Edm.String [key] "Type"
PX.Objects.AP.APRegister.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APRegister.HiddenKey : Edm.String
PX.Objects.AP.APRegister.InternalDocType : Edm.String "Document Type (Internal)"
PX.Objects.AP.APRegister.PrintDocType : Edm.String "Type"
PX.Objects.AP.APRegister.OrigModule : Edm.String "Source"
PX.Objects.AP.APRegister.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AP.APRegister.OrigDocDate : Edm.DateTimeOffset
PX.Objects.AP.APRegister.TranPeriodID : Edm.String "Master Period"
PX.Objects.AP.APRegister.FinPeriodID : Edm.String "Post Period"
PX.Objects.AP.APRegister.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APRegister.CuryID : Edm.String "Currency"
PX.Objects.AP.APRegister.LineCntr : Edm.Int32 [required]
PX.Objects.AP.APRegister.AdjCntr : Edm.Int32 [required]
PX.Objects.AP.APRegister.CuryInfoID : Edm.Int64
PX.Objects.AP.APRegister.CuryOrigDocAmt : Edm.Decimal [required] "Amount"
PX.Objects.AP.APRegister.OrigDocAmt : Edm.Decimal [required] "Amount"
PX.Objects.AP.APRegister.CuryDocBal : Edm.Decimal [required] "Balance"
PX.Objects.AP.APRegister.DocBal : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryInitDocBal : Edm.Decimal [required] "Balance"
PX.Objects.AP.APRegister.InitDocBal : Edm.Decimal [required]
PX.Objects.AP.APRegister.DisplayCuryInitDocBal : Edm.Decimal "Migrated Balance"
PX.Objects.AP.APRegister.DiscTot : Edm.Decimal
PX.Objects.AP.APRegister.CuryDiscTot : Edm.Decimal "Discount Total"
PX.Objects.AP.APRegister.DocDisc : Edm.Decimal
PX.Objects.AP.APRegister.CuryDocDisc : Edm.Decimal "Document Discount"
PX.Objects.AP.APRegister.CuryOrigDiscAmt : Edm.Decimal [required] "Cash Discount"
PX.Objects.AP.APRegister.OrigDiscAmt : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryDiscTaken : Edm.Decimal [required]
PX.Objects.AP.APRegister.DiscTaken : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryDiscBal : Edm.Decimal [required] "Cash Discount Balance"
PX.Objects.AP.APRegister.DiscBal : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryOrigWhTaxAmt : Edm.Decimal [required] "With. Tax"
PX.Objects.AP.APRegister.OrigWhTaxAmt : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryWhTaxBal : Edm.Decimal [required]
PX.Objects.AP.APRegister.WhTaxBal : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryTaxWheld : Edm.Decimal [required]
PX.Objects.AP.APRegister.TaxWheld : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryChargeAmt : Edm.Decimal [required] "Finance Charges"
PX.Objects.AP.APRegister.ChargeAmt : Edm.Decimal [required]
PX.Objects.AP.APRegister.DocDesc : Edm.String "Description"
PX.Objects.AP.APRegister.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APRegister.CreatedByScreenID : Edm.String
PX.Objects.AP.APRegister.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AP.APRegister.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APRegister.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APRegister.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AP.APRegister.tstamp : Edm.Binary
PX.Objects.AP.APRegister.DocClass : Edm.String
PX.Objects.AP.APRegister.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.AP.APRegister.PrebookBatchNbr : Edm.String "Pre-Releasing Batch Nbr."
PX.Objects.AP.APRegister.VoidBatchNbr : Edm.String "Void Batch Nbr."
PX.Objects.AP.APRegister.Released : Edm.Boolean [required] "Released"
PX.Objects.AP.APRegister.ReleasedToVerify : Edm.Boolean
PX.Objects.AP.APRegister.OpenDoc : Edm.Boolean [required] "Open"
PX.Objects.AP.APRegister.Hold : Edm.Boolean [required] "Hold"
PX.Objects.AP.APRegister.Scheduled : Edm.Boolean [required]
PX.Objects.AP.APRegister.Voided : Edm.Boolean [required] "Void"
PX.Objects.AP.APRegister.Printed : Edm.Boolean [required]
PX.Objects.AP.APRegister.Prebooked : Edm.Boolean [required] "Prebooked"
PX.Objects.AP.APRegister.Approved : Edm.Boolean [required]
PX.Objects.AP.APRegister.Rejected : Edm.Boolean [required]
PX.Objects.AP.APRegister.DontApprove : Edm.Boolean
PX.Objects.AP.APRegister.NoteID : Edm.Guid
PX.Objects.AP.APRegister.NoteText : Edm.String "Note Text"
PX.Objects.AP.APRegister.RefNoteID : Edm.Guid
PX.Objects.AP.APRegister.ClosedDate : Edm.DateTimeOffset "Closed Date"
PX.Objects.AP.APRegister.ClosedFinPeriodID : Edm.String "Closed Period"
PX.Objects.AP.APRegister.ClosedTranPeriodID : Edm.String "Closed Master Period"
PX.Objects.AP.APRegister.RGOLAmt : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryRoundDiff : Edm.Decimal [required] "Rounding Diff."
PX.Objects.AP.APRegister.RoundDiff : Edm.Decimal [required]
PX.Objects.AP.APRegister.CuryTaxRoundDiff : Edm.Decimal [required] "Rounding Diff."
PX.Objects.AP.APRegister.TaxRoundDiff : Edm.Decimal [required]
PX.Objects.AP.APRegister.Status : Edm.String "Status"
PX.Objects.AP.APRegister.ScheduleID : Edm.String
PX.Objects.AP.APRegister.ImpRefNbr : Edm.String
PX.Objects.AP.APRegister.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.AP.APRegister.IsTaxPosted : Edm.Boolean [required] "Tax has been posted to the external tax provider"
PX.Objects.AP.APRegister.IsTaxSaved : Edm.Boolean [required] "Tax has been saved in the external tax provider"
PX.Objects.AP.APRegister.NonTaxable : Edm.Boolean [required] "Non-Taxable"
PX.Objects.AP.APRegister.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.AP.APRegister.OrigRefNbr : Edm.String "Orig. Ref. Nbr."
PX.Objects.AP.APRegister.ReleasedOrPrebooked : Edm.Boolean
PX.Objects.AP.APRegister.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.AP.APRegister.EmployeeWorkgroupID : Edm.Int32 "Workgroup ID"
PX.Objects.AP.APRegister.EmployeeID : Edm.Int32 "Owner"
PX.Objects.AP.APRegister.WorkgroupID : Edm.Int32 "Approval Workgroup ID"
PX.Objects.AP.APRegister.OwnerID : Edm.Int32 "Approver"
PX.Objects.AP.APRegister.IsMigratedRecord : Edm.Boolean
PX.Objects.AP.APRegister.HasMultipleProjects : Edm.Boolean [required]
PX.Objects.AP.APRegister.CuryLineRetainageTotal : Edm.Decimal [required]
PX.Objects.AP.APRegister.LineRetainageTotal : Edm.Decimal [required]
PX.Objects.AP.APRegister.RetainedTaxTotal : Edm.Decimal [required]
PX.Objects.AP.APRegister.RetainedDiscTotal : Edm.Decimal [required]
PX.Objects.AP.APRegister.RetainageUnpaidTotal : Edm.Decimal
PX.Objects.AP.APRegister.RetainagePaidTotal : Edm.Decimal
PX.Objects.AP.APRegister.PendingPayment : Edm.Boolean [required]
PX.Objects.AP.APRegister.CuryDiscountedDocTotal : Edm.Decimal "Discounted Doc. Total"
PX.Objects.AP.APRegister.DiscountedDocTotal : Edm.Decimal
PX.Objects.AP.APRegister.CuryDiscountedTaxableTotal : Edm.Decimal "Discounted Taxable Total"
PX.Objects.AP.APRegister.DiscountedTaxableTotal : Edm.Decimal
PX.Objects.AP.APRegister.CuryDiscountedPrice : Edm.Decimal "Tax on Discounted Price"
PX.Objects.AP.APRegister.DiscountedPrice : Edm.Decimal
PX.Objects.AP.APRegister.HasPPDTaxes : Edm.Boolean [required]
PX.Objects.AP.APRegister.PendingPPD : Edm.Boolean [required]
PX.Objects.AP.APRegister.IsExpectedPPVValid : Edm.Boolean [required]
PX.Objects.AP.APRegister.PendingProcessing : Edm.Boolean [required]
PX.Objects.AP.APRegister.CuryRate : Edm.Decimal
PX.Objects.AP.APRegister.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AP.APRegister.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AP.APRegister.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.AP.APRegister.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APRegister.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APRegister.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.AP.APRegister.BatchByPrebookBatchNbr -> PX.Objects.GL.Batch (PrebookBatchNbr=BatchNbr)
PX.Objects.AP.APRegister.BatchByVoidBatchNbr -> PX.Objects.GL.Batch (VoidBatchNbr=BatchNbr)
PX.Objects.AP.APRegister.ContactByEmployeeID -> PX.Objects.CR.Contact (EmployeeID=ContactID)
PX.Objects.AP.APRegister.APRegisterByRefNbr -> PX.Objects.AP.APRegister (OrigDocType=DocType, RefNbr=OrigRefNbr)
PX.Objects.AP.APRegister.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AP.APRegister.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APRegister.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APRegister.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APRegister.EPCompanyTreeByEmployeeWorkgroupID -> PX.TM.EPCompanyTree (EmployeeWorkgroupID=WorkGroupID)
PX.Objects.AP.APRegister.INRegisterByTaxCostINAdjRefNbr -> PX.Objects.IN.INRegister
PX.Objects.AP.APRegister.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AP.APRegister.AccountByAPAccountID -> PX.Objects.GL.Account
PX.Objects.AP.APRegister.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.AP.APRegister.AccountByPrepaymentAccountID -> PX.Objects.GL.Account
PX.Objects.AP.APRegister.ScheduleByScheduleID -> PX.Objects.GL.Schedule (ScheduleID=ScheduleID)
PX.Objects.AP.APRegister.SubByAPSubID -> PX.Objects.GL.Sub
PX.Objects.AP.APRegister.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.AP.APRegister.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.AP.APRegister.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.AP.APRegister.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.AP.APRegister.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.AP.APRegister.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AP.APRegister.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AP.APRegister.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AP.APRegister.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.AP.APRegister.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.AP.APRegister.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.AP.APRegister.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.AP.APRegister.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.AP.APRegister.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.AP.APRegister.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AP.APRegister.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.AP.APRegister.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.AP.APRegister.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.AP.APRegister.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.AP.APRegister.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.AP.APRegister.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.AP.APRegister.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.AP.APRegister.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.AP.APRegister.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.AP.APRegisterAccess (EntityType)

Label: "Vendor"
BaseType: PX.Objects.AP.Vendor
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_AP_APRegisterAccess

PX.Objects.AP.APRegisterAccess.DocType : Edm.String
PX.Objects.AP.APRegisterAccess.RefNbr : Edm.String
PX.Objects.AP.APRegisterAccess.Scheduled : Edm.Boolean
PX.Objects.AP.APRegisterAccess.ScheduleID : Edm.String
PX.Objects.AP.APRegisterAccess.ScheduleByScheduleID -> PX.Objects.GL.Schedule (ScheduleID=ScheduleID)
PX.Objects.AP.APRegisterAccess.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.AP.APRegisterAccess.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AP.APRegisterAccess.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.AP.APRegisterAccess.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.AP.APRegisterAccess.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.AP.APRegisterAccess.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.AP.APRegisterAccess.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.AP.APRegisterAccess.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.AP.APRegisterAccess.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.AP.APRegisterAccess.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.AP.APRegisterReport (EntityType)

Label: "Document"
BaseType: PX.Objects.AP.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_APRegisterReport, Document1, APRegisterReport

PX.Objects.AP.APRegisterReport.SignBalance : Edm.Decimal
PX.Objects.AP.APRegisterReport.SignAmount : Edm.Decimal
PX.Objects.AP.APRegisterReport.SignReleasedRetainage : Edm.Decimal

# PX.Objects.AP.APRegisterRetainage (EntityType)

Label: "APRegister Retainage"
Key: OrigDocType, OrigRefNbr
Entity sets: PX_Objects_AP_APRegisterRetainage, APRegisterRetainage
Non-filterable, non-selectable: DocBalSigned, OrigDocAmtSigned

PX.Objects.AP.APRegisterRetainage.OrigDocType : Edm.String [key]
PX.Objects.AP.APRegisterRetainage.OrigRefNbr : Edm.String [key]
PX.Objects.AP.APRegisterRetainage.DocBalSigned : Edm.Decimal
PX.Objects.AP.APRegisterRetainage.DocBal : Edm.Decimal
PX.Objects.AP.APRegisterRetainage.OrigDocAmtSigned : Edm.Decimal
PX.Objects.AP.APRegisterRetainage.OrigDocAmt : Edm.Decimal

# PX.Objects.AP.APRetainageInvoice (EntityType)

Label: "Document"
BaseType: PX.Objects.AP.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_APRetainageInvoice

# PX.Objects.AP.APSetup (EntityType)

Label: "Accounts Payable Preferences"
Singletons: PX_Objects_AP_APSetup, AccountsPayablePreferences, APSetup

PX.Objects.AP.APSetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.AP.APSetup.DfltVendorClassID : Edm.String "Default Vendor Class ID"
PX.Objects.AP.APSetup.PerRetainTran : Edm.Int16 [required] "Keep Transactions for"
PX.Objects.AP.APSetup.PerRetainHist : Edm.Int16 [required] "Periods to Retain History"
PX.Objects.AP.APSetup.InvoiceNumberingID : Edm.String "Bill Numbering Sequence"
PX.Objects.AP.APSetup.PastDue00 : Edm.Int16 [required] "Aging Period 1"
PX.Objects.AP.APSetup.PastDue01 : Edm.Int16 [required] "Aging Period 2"
PX.Objects.AP.APSetup.PastDue02 : Edm.Int16 [required] "Aging Period 3"
PX.Objects.AP.APSetup.CheckNumberingID : Edm.String "Payment Numbering Sequence"
PX.Objects.AP.APSetup.CreditAdjNumberingID : Edm.String "Credit Adjustment Numbering Sequence"
PX.Objects.AP.APSetup.DebitAdjNumberingID : Edm.String "Debit Adjustment Numbering Sequence"
PX.Objects.AP.APSetup.PriceWSNumberingID : Edm.String "Price Worksheet Numbering Sequence"
PX.Objects.AP.APSetup.PrepaymentInvoiceNumberingID : Edm.String "Prepayment Invoice Numbering Sequence"
PX.Objects.AP.APSetup.DefaultTranDesc : Edm.String "Default Transaction Description"
PX.Objects.AP.APSetup.AutoPost : Edm.Boolean [required] "Automatically Post on Release"
PX.Objects.AP.APSetup.TransactionPosting : Edm.String "Transaction Posting"
PX.Objects.AP.APSetup.DataInconsistencyHandlingMode : Edm.String "Extra Data Validation"
PX.Objects.AP.APSetup.tstamp : Edm.Binary
PX.Objects.AP.APSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APSetup.CreatedByScreenID : Edm.String
PX.Objects.AP.APSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APSetup.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APSetup.SummaryPost : Edm.Boolean "Post Summary on Updating GL"
PX.Objects.AP.APSetup.RequireApprovePayments : Edm.Boolean [required] "Require Approval of Bills Prior to Payment"
PX.Objects.AP.APSetup.RequireControlTotal : Edm.Boolean [required] "Validate Document Totals on Entry"
PX.Objects.AP.APSetup.RequireControlTaxTotal : Edm.Boolean [required] "Validate Tax Totals on Entry"
PX.Objects.AP.APSetup.HoldEntry : Edm.Boolean [required] "Hold Documents on Entry"
PX.Objects.AP.APSetup.EarlyChecks : Edm.Boolean [required] "Enable Early Payments"
PX.Objects.AP.APSetup.RequireVendorRef : Edm.Boolean [required] "Require Vendor Reference"
PX.Objects.AP.APSetup.PaymentLeadTime : Edm.Int16 [required] "Payment Lead Time"
PX.Objects.AP.APSetup.InvoicePrecision : Edm.Decimal [required] "Rounding Precision"
PX.Objects.AP.APSetup.InvoiceRounding : Edm.String "Rounding Rule for Bills"
PX.Objects.AP.APSetup.RaiseErrorOnDoubleInvoiceNbr : Edm.Boolean [required] "Raise an Error on Duplicate Vendor Reference Number"
PX.Objects.AP.APSetup.LoadVendorsPricesUsingAlternateID : Edm.Boolean [required] "Load Vendor Prices by Alternate ID"
PX.Objects.AP.APSetup.VendorPriceUpdate : Edm.String "Vendor Price Update"
PX.Objects.AP.APSetup.ApplyQuantityDiscountBy : Edm.String "Apply Quantity Discounts To"
PX.Objects.AP.APSetup.RetentionType : Edm.String "Retention Type"
PX.Objects.AP.APSetup.NumberOfMonths : Edm.Int32 "Number of Months"
PX.Objects.AP.APSetup.SuggestPaymentAmount : Edm.Boolean [required] "Set Zero Payment Amount to Application Amount"
PX.Objects.AP.APSetup.MigrationMode : Edm.Boolean [required] "Activate Migration Mode"
PX.Objects.AP.APSetup.RequireSingleProjectPerDocument : Edm.Boolean [required]
PX.Objects.AP.APSetup.TermsInDebitAdjustments : Edm.Boolean [required] "Use Credit Terms in Debit Adjustments"
PX.Objects.AP.APSetup.PPDDebitAdjustmentDescr : Edm.String "Tax Adjustment Description"
PX.Objects.AP.APSetup.NoteID : Edm.Guid
PX.Objects.AP.APSetup.NoteText : Edm.String "Note Text"
PX.Objects.AP.APSetup.PrintDirectSalesOn : Edm.String "Report Direct Sales On"
PX.Objects.AP.APSetup.IRISRowsPerCSVFile : Edm.Int32 [required] "Rows per CSV File"
PX.Objects.AP.APSetup.ReclassifyInvoices : Edm.Boolean [required] "Allow Bill Reclassification"
PX.Objects.AP.APSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APSetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.AP.APSetup.NumberingByInvoiceNumberingID -> PX.Objects.CS.Numbering (InvoiceNumberingID=NumberingID)
PX.Objects.AP.APSetup.NumberingByDebitAdjNumberingID -> PX.Objects.CS.Numbering (DebitAdjNumberingID=NumberingID)
PX.Objects.AP.APSetup.NumberingByCreditAdjNumberingID -> PX.Objects.CS.Numbering (CreditAdjNumberingID=NumberingID)
PX.Objects.AP.APSetup.NumberingByCheckNumberingID -> PX.Objects.CS.Numbering (CheckNumberingID=NumberingID)
PX.Objects.AP.APSetup.NumberingByPriceWSNumberingID -> PX.Objects.CS.Numbering (PriceWSNumberingID=NumberingID)
PX.Objects.AP.APSetup.NumberingByPrepaymentInvoiceNumberingID -> PX.Objects.CS.Numbering (PrepaymentInvoiceNumberingID=NumberingID)
PX.Objects.AP.APSetup.VendorClassByDfltVendorClassID -> PX.Objects.AP.VendorClass (DfltVendorClassID=VendorClassID)

# PX.Objects.AP.APSetupApproval (EntityType)

Label: "AP Approval Preferences"
Key: ApprovalID
Entity sets: PX_Objects_AP_APSetupApproval, APApprovalPreferences, APSetupApproval

PX.Objects.AP.APSetupApproval.DocType : Edm.String "Type"
PX.Objects.AP.APSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.AP.APSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.AP.APSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.AP.APSetupApproval.tstamp : Edm.Binary
PX.Objects.AP.APSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.AP.APSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APSetupApproval.IsActive : Edm.Boolean [required] "Active"
PX.Objects.AP.APSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.AP.APSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.AP.APTax (EntityType)

Label: "AP Tax Detail"
Key: LineNbr, RefNbr, TaxID, TranType
Entity sets: PX_Objects_AP_APTax, APTaxDetail, APTax
Non-filterable, non-selectable: NonDeductibleTaxRate, CuryTaxDiscountAmt, TaxDiscountAmt

PX.Objects.AP.APTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.AP.APTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.AP.APTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.AP.APTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APTax.CreatedByScreenID : Edm.String
PX.Objects.AP.APTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APTax.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APTax.TranType : Edm.String [key] "Tran. Type"
PX.Objects.AP.APTax.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AP.APTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.AP.APTax.CuryInfoID : Edm.Int64
PX.Objects.AP.APTax.CuryOrigTaxableAmt : Edm.Decimal
PX.Objects.AP.APTax.OrigTaxableAmt : Edm.Decimal
PX.Objects.AP.APTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.AP.APTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.AP.APTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.AP.APTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.AP.APTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.AP.APTax.CuryTaxableDiscountAmt : Edm.Decimal [required]
PX.Objects.AP.APTax.TaxableDiscountAmt : Edm.Decimal [required]
PX.Objects.AP.APTax.CuryTaxDiscountAmt : Edm.Decimal
PX.Objects.AP.APTax.TaxDiscountAmt : Edm.Decimal
PX.Objects.AP.APTax.RetainedTaxableAmt : Edm.Decimal [required] "Retained Taxable Amount"
PX.Objects.AP.APTax.RetainedTaxAmt : Edm.Decimal [required] "Retained Tax"
PX.Objects.AP.APTax.tstamp : Edm.Binary
PX.Objects.AP.APTax.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.AP.APTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.AP.APTax.APTranByLineNbr -> PX.Objects.AP.APTran (TranType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)

# PX.Objects.AP.APTaxTran (EntityType)

Label: "AP Tax Details"
BaseType: PX.Objects.TX.TaxTran
Key: Module, RecordID (inherited from PX.Objects.TX.TaxTran)
Entity sets: PX_Objects_AP_APTaxTran, APTaxDetails, APTaxTran
Non-filterable, non-selectable: CuryTaxableDiscountAmt, TaxableDiscountAmt, CuryDiscountedTaxableAmt, DiscountedTaxableAmt, CuryDiscountedPrice, DiscountedPrice

PX.Objects.AP.APTaxTran.BranchID : Edm.Int32 "Branch"
PX.Objects.AP.APTaxTran.CuryTaxableDiscountAmt : Edm.Decimal
PX.Objects.AP.APTaxTran.TaxableDiscountAmt : Edm.Decimal
PX.Objects.AP.APTaxTran.CuryTaxDiscountAmt : Edm.Decimal
PX.Objects.AP.APTaxTran.TaxDiscountAmt : Edm.Decimal
PX.Objects.AP.APTaxTran.CuryDiscountedTaxableAmt : Edm.Decimal "Discounted Taxable Amount"
PX.Objects.AP.APTaxTran.DiscountedTaxableAmt : Edm.Decimal
PX.Objects.AP.APTaxTran.CuryDiscountedPrice : Edm.Decimal "Tax on Discounted Price"
PX.Objects.AP.APTaxTran.DiscountedPrice : Edm.Decimal

# PX.Objects.AP.APTran (EntityType)

Label: "AP Transactions"
Key: LineNbr, RefNbr, TranType
Entity sets: PX_Objects_AP_APTran, APTransactions, APTran
Non-filterable, non-selectable: SuppliedByVendorID, AllowControlAccountForModule, RequiresTerms, FreezeManualDisc, SkipDisc, ReleasedToVerify, CalculateDiscountsOnImport, NoteText, ClassID, Custodian, SignedQty, SignedCuryTranAmt, SignedTranAmt, ProjectReclassified

PX.Objects.AP.APTran.BranchID : Edm.Int32 "Branch"
PX.Objects.AP.APTran.TranType : Edm.String [key] "Tran. Type"
PX.Objects.AP.APTran.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AP.APTran.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AP.APTran.SortOrder : Edm.Int32 "Line Nbr."
PX.Objects.AP.APTran.TranID : Edm.Int32
PX.Objects.AP.APTran.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APTran.SuppliedByVendorID : Edm.Int32
PX.Objects.AP.APTran.LineType : Edm.String
PX.Objects.AP.APTran.POOrderType : Edm.String "PO Type"
PX.Objects.AP.APTran.PONbr : Edm.String "PO Number"
PX.Objects.AP.APTran.POLineNbr : Edm.Int32 "PO Line"
PX.Objects.AP.APTran.LCDocType : Edm.String "LC Type"
PX.Objects.AP.APTran.LCRefNbr : Edm.String "LC Number"
PX.Objects.AP.APTran.LCLineNbr : Edm.Int32 "LC Line"
PX.Objects.AP.APTran.ReceiptType : Edm.String "PO Receipt Type"
PX.Objects.AP.APTran.ReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.AP.APTran.ReceiptLineNbr : Edm.Int32 "PO Receipt Line"
PX.Objects.AP.APTran.IsStockItem : Edm.Boolean
PX.Objects.AP.APTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AP.APTran.AccrueCost : Edm.Boolean "Accrue Cost"
PX.Objects.AP.APTran.AllowControlAccountForModule : Edm.String
PX.Objects.AP.APTran.Box1099 : Edm.Int16 "1099 Box"
PX.Objects.AP.APTran.TaxID : Edm.String "Tax ID"
PX.Objects.AP.APTran.DeferredCode : Edm.String "Deferral Code"
PX.Objects.AP.APTran.DRTermStartDate : Edm.DateTimeOffset "Term Start Date"
PX.Objects.AP.APTran.DRTermEndDate : Edm.DateTimeOffset "Term End Date"
PX.Objects.AP.APTran.RequiresTerms : Edm.Boolean
PX.Objects.AP.APTran.CuryInfoID : Edm.Int64
PX.Objects.AP.APTran.SiteID : Edm.Int32
PX.Objects.AP.APTran.UOM : Edm.String "UOM"
PX.Objects.AP.APTran.Qty : Edm.Decimal "Quantity"
PX.Objects.AP.APTran.BaseQty : Edm.Decimal "Base Qty."
PX.Objects.AP.APTran.CuryUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.AP.APTran.UnitCost : Edm.Decimal
PX.Objects.AP.APTran.CuryLineAmt : Edm.Decimal "Ext. Cost"
PX.Objects.AP.APTran.LineAmt : Edm.Decimal
PX.Objects.AP.APTran.ManualDisc : Edm.Boolean "Manual Discount"
PX.Objects.AP.APTran.FreezeManualDisc : Edm.Boolean
PX.Objects.AP.APTran.SkipDisc : Edm.Boolean
PX.Objects.AP.APTran.AutomaticDiscountsDisabled : Edm.Boolean [required]
PX.Objects.AP.APTran.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.AP.APTran.DiscAmt : Edm.Decimal
PX.Objects.AP.APTran.CuryDiscCost : Edm.Decimal "Disc. Unit Cost"
PX.Objects.AP.APTran.DiscCost : Edm.Decimal
PX.Objects.AP.APTran.PrepaymentPct : Edm.Decimal [required] "Prepayment Percent"
PX.Objects.AP.APTran.CuryPrepaymentAmt : Edm.Decimal [required] "Prepayment Amount"
PX.Objects.AP.APTran.PrepaymentAmt : Edm.Decimal [required]
PX.Objects.AP.APTran.RetainagePct : Edm.Decimal [required] "RetainagePct"
PX.Objects.AP.APTran.CuryRetainageAmt : Edm.Decimal [required] "CuryRetainageAmt"
PX.Objects.AP.APTran.RetainageAmt : Edm.Decimal [required]
PX.Objects.AP.APTran.CuryTranAmt : Edm.Decimal "Amount"
PX.Objects.AP.APTran.TranAmt : Edm.Decimal "Amount"
PX.Objects.AP.APTran.TaxableAmt : Edm.Decimal
PX.Objects.AP.APTran.TaxAmt : Edm.Decimal
PX.Objects.AP.APTran.OrigTaxableAmt : Edm.Decimal [required]
PX.Objects.AP.APTran.OrigTaxAmt : Edm.Decimal [required]
PX.Objects.AP.APTran.RetainedTaxableAmt : Edm.Decimal [required]
PX.Objects.AP.APTran.RetainedTaxAmt : Edm.Decimal [required]
PX.Objects.AP.APTran.CashDiscBal : Edm.Decimal [required]
PX.Objects.AP.APTran.OrigRetainageAmt : Edm.Decimal [required]
PX.Objects.AP.APTran.RetainageBal : Edm.Decimal [required]
PX.Objects.AP.APTran.OrigTranAmt : Edm.Decimal [required]
PX.Objects.AP.APTran.TranBal : Edm.Decimal [required] "Balance"
PX.Objects.AP.APTran.ExpenseAmt : Edm.Decimal
PX.Objects.AP.APTran.CuryExpenseAmt : Edm.Decimal
PX.Objects.AP.APTran.ManualPrice : Edm.Boolean "Manual Cost"
PX.Objects.AP.APTran.OrigLineNbr : Edm.Int32
PX.Objects.AP.APTran.OrigGroupDiscountRate : Edm.Decimal [required]
PX.Objects.AP.APTran.OrigDocumentDiscountRate : Edm.Decimal [required]
PX.Objects.AP.APTran.GroupDiscountRate : Edm.Decimal
PX.Objects.AP.APTran.DocumentDiscountRate : Edm.Decimal [required]
PX.Objects.AP.APTran.TranClass : Edm.String
PX.Objects.AP.APTran.DrCr : Edm.String
PX.Objects.AP.APTran.TranDate : Edm.DateTimeOffset "Document Date"
PX.Objects.AP.APTran.FinPeriodID : Edm.String
PX.Objects.AP.APTran.TranPeriodID : Edm.String
PX.Objects.AP.APTran.TranDesc : Edm.String "Transaction Descr."
PX.Objects.AP.APTran.ReleasedToVerify : Edm.Boolean
PX.Objects.AP.APTran.Released : Edm.Boolean [required] "Released"
PX.Objects.AP.APTran.ExpectedPPVAmount : Edm.Decimal [required] "Estimated PPV Amount"
PX.Objects.AP.APTran.POPPVAmt : Edm.Decimal [required] "PO PPV Amount"
PX.Objects.AP.APTran.PPVDocType : Edm.String "PPV Doc. Type"
PX.Objects.AP.APTran.PPVRefNbr : Edm.String "PPV Ref. Nbr."
PX.Objects.AP.APTran.POAccrualType : Edm.String "Billing Based On"
PX.Objects.AP.APTran.POAccrualRefNoteID : Edm.Guid
PX.Objects.AP.APTran.POAccrualLineNbr : Edm.Int32
PX.Objects.AP.APTran.UnreceivedQty : Edm.Decimal
PX.Objects.AP.APTran.BaseUnreceivedQty : Edm.Decimal
PX.Objects.AP.APTran.DefScheduleID : Edm.Int32 "Original Deferral Schedule"
PX.Objects.AP.APTran.Date : Edm.DateTimeOffset "Expense Date"
PX.Objects.AP.APTran.LandedCostCodeID : Edm.String "Landed Cost Code"
PX.Objects.AP.APTran.CalculateDiscountsOnImport : Edm.Boolean "Calculate automatic discounts on import"
PX.Objects.AP.APTran.DiscPct : Edm.Decimal "Discount Percent"
PX.Objects.AP.APTran.DiscountID : Edm.String "Discount Code"
PX.Objects.AP.APTran.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.AP.APTran.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.AP.APTran.IsDirectTaxLine : Edm.Boolean [required]
PX.Objects.AP.APTran.tstamp : Edm.Binary
PX.Objects.AP.APTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APTran.CreatedByScreenID : Edm.String
PX.Objects.AP.APTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APTran.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APTran.NoteID : Edm.Guid
PX.Objects.AP.APTran.NoteText : Edm.String "Note Text"
PX.Objects.AP.APTran.ClassID : Edm.Int32 "Asset Class"
PX.Objects.AP.APTran.Custodian : Edm.Guid "Custodian"
PX.Objects.AP.APTran.EmployeeID : Edm.Int32
PX.Objects.AP.APTran.SignedQty : Edm.Decimal
PX.Objects.AP.APTran.SignedCuryTranAmt : Edm.Decimal
PX.Objects.AP.APTran.SignedTranAmt : Edm.Decimal
PX.Objects.AP.APTran.DropshipExpenseRecording : Edm.String
PX.Objects.AP.APTran.ProjectCuryInfoID : Edm.Int64
PX.Objects.AP.APTran.Reclassified : Edm.Boolean [required]
PX.Objects.AP.APTran.ProjectReclassified : Edm.Boolean
PX.Objects.AP.APTran.PrevPOLineNbr : Edm.Int32
PX.Objects.AP.APTran.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AP.APTran.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APTran.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTran.POLineByPOLineNbr -> PX.Objects.PO.POLine (POOrderType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.AP.APTran.POOrderByPONbr -> PX.Objects.PO.POOrder (POOrderType=OrderType, PONbr=OrderNbr)
PX.Objects.AP.APTran.POOrderByPOOrderType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POOrderType=OrderType)
PX.Objects.AP.APTran.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AP.APTran.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.AP.APTran.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APTran.APPaymentByRefNbr -> PX.Objects.AP.APPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTran.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AP.APTran.DRDeferredCodeByDeferredCode -> PX.Objects.DR.DRDeferredCode (DeferredCode=DeferredCodeID)
PX.Objects.AP.APTran.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AP.APTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.AP.APTran.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.AP.APTran.LandedCostCodeByLandedCostCodeID -> PX.Objects.PO.LandedCostCode (LandedCostCodeID=LandedCostCodeID)
PX.Objects.AP.APTran.POLandedCostDetailByLCLineNbr -> PX.Objects.PO.POLandedCostDetail (LCDocType=DocType, LCRefNbr=RefNbr, LCLineNbr=LineNbr)
PX.Objects.AP.APTran.POLandedCostDetailByLCRefNbr -> PX.Objects.PO.POLandedCostDetail (LCDocType=DocType, LCRefNbr=RefNbr, LCRefNbr=LineNbr)
PX.Objects.AP.APTran.POLandedCostDocByLCRefNbr -> PX.Objects.PO.POLandedCostDoc (LCDocType=DocType, LCRefNbr=RefNbr)
PX.Objects.AP.APTran.POLandedCostDocByLCDocType -> PX.Objects.PO.POLandedCostDoc (LCRefNbr=RefNbr, LCDocType=DocType)
PX.Objects.AP.APTran.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.AP.APTran.POReceiptByReceiptType -> PX.Objects.PO.POReceipt (ReceiptNbr=ReceiptNbr, ReceiptType=ReceiptType)
PX.Objects.AP.APTran.POReceiptLineByReceiptLineNbr -> PX.Objects.PO.POReceiptLine (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr, ReceiptLineNbr=LineNbr)
PX.Objects.AP.APTran.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.AP.APTran.DRScheduleByTranType -> PX.Objects.DR.DRSchedule (DefScheduleID=ScheduleID, TranType=DocType)
PX.Objects.AP.APTran.INRegisterByPPVDocType -> PX.Objects.IN.INRegister (PPVRefNbr=RefNbr, PPVDocType=DocType)
PX.Objects.AP.APTran.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AP.APTran.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AP.APTran.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AP.APTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.AP.APTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AP.APTran.APDiscountByVendorID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID, VendorID=BAccountID)
PX.Objects.AP.APTran.AP1099BoxByBox1099 -> PX.Objects.AP.AP1099Box (Box1099=BoxNbr)
PX.Objects.AP.APTran.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AP.APTran.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AP.APTran.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.AP.APTran.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.AP.APTran.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AP.APTran.JointPayeeCollection -> Collection(PX.Objects.CN.JointChecks.JointPayee)
PX.Objects.AP.APTran.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.AP.APTran.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.AP.APTran.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.AP.APTran.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.AP.APTranPost (EntityType)

Label: "AP Document transaction"
Key: DocType, ID, RefNbr
Entity sets: PX_Objects_AP_APTranPost, APDocumenttransaction, APTranPost
Non-filterable, non-selectable: IsVoidPrepayment

PX.Objects.AP.APTranPost.BranchID : Edm.Int32 "Branch"
PX.Objects.AP.APTranPost.DocType : Edm.String [key] "Doc. Type"
PX.Objects.AP.APTranPost.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.AP.APTranPost.ID : Edm.Int32 [key]
PX.Objects.AP.APTranPost.RefNoteID : Edm.Guid
PX.Objects.AP.APTranPost.SourceDocType : Edm.String "Source Doc. Type"
PX.Objects.AP.APTranPost.SourceRefNbr : Edm.String "Source Ref. Nbr."
PX.Objects.AP.APTranPost.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AP.APTranPost.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APTranPost.FinPeriodID : Edm.String "Application Period"
PX.Objects.AP.APTranPost.TranPeriodID : Edm.String
PX.Objects.AP.APTranPost.CuryInfoID : Edm.Int64
PX.Objects.AP.APTranPost.BatchNbr : Edm.String "Batch Number"
PX.Objects.AP.APTranPost.CuryAmt : Edm.Decimal "Amount"
PX.Objects.AP.APTranPost.CuryPPDAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AP.APTranPost.CuryDiscAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AP.APTranPost.CuryRetainageAmt : Edm.Decimal
PX.Objects.AP.APTranPost.CuryWhTaxAmt : Edm.Decimal [required] "With. Tax"
PX.Objects.AP.APTranPost.Amt : Edm.Decimal
PX.Objects.AP.APTranPost.PPDAmt : Edm.Decimal
PX.Objects.AP.APTranPost.DiscAmt : Edm.Decimal
PX.Objects.AP.APTranPost.RetainageAmt : Edm.Decimal
PX.Objects.AP.APTranPost.WhTaxAmt : Edm.Decimal [required]
PX.Objects.AP.APTranPost.RGOLAmt : Edm.Decimal
PX.Objects.AP.APTranPost.IsMigratedRecord : Edm.Boolean
PX.Objects.AP.APTranPost.Type : Edm.String "Transaction type"
PX.Objects.AP.APTranPost.TranType : Edm.String "Tran. Type"
PX.Objects.AP.APTranPost.TranRefNbr : Edm.String "Tran. Ref. Nbr."
PX.Objects.AP.APTranPost.BalanceSign : Edm.Int16
PX.Objects.AP.APTranPost.GLSign : Edm.Int16
PX.Objects.AP.APTranPost.IsVoidPrepayment : Edm.Boolean
PX.Objects.AP.APTranPost.TranClass : Edm.String
PX.Objects.AP.APTranPost.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APTranPost.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTranPost.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APTranPost.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.AP.APTranPost.APPaymentByRefNbr -> PX.Objects.AP.APPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTranPost.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTranPost.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AP.APTranPost.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APTranPost.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.AP.APTranPost.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AP.APTranPost.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.AP.APTranPostGL (EntityType)

Label: "AP Document Post GL"
Key: DocType, ID, RefNbr
Entity sets: PX_Objects_AP_APTranPostGL, APDocumentPostGL, APTranPostGL

PX.Objects.AP.APTranPostGL.DocType : Edm.String [key] "Doc. Type"
PX.Objects.AP.APTranPostGL.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.AP.APTranPostGL.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.AP.APTranPostGL.ID : Edm.Int32 [key]
PX.Objects.AP.APTranPostGL.SourceDocType : Edm.String "Source Doc. Type"
PX.Objects.AP.APTranPostGL.SourceRefNbr : Edm.String "Source Ref. Nbr."
PX.Objects.AP.APTranPostGL.CuryID : Edm.String
PX.Objects.AP.APTranPostGL.CuryInfoID : Edm.Int64
PX.Objects.AP.APTranPostGL.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APTranPostGL.FinPeriodID : Edm.String "Application Period"
PX.Objects.AP.APTranPostGL.TranPeriodID : Edm.String
PX.Objects.AP.APTranPostGL.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AP.APTranPostGL.BalanceSign : Edm.Int16
PX.Objects.AP.APTranPostGL.BatchNbr : Edm.String "Batch Number"
PX.Objects.AP.APTranPostGL.Type : Edm.String
PX.Objects.AP.APTranPostGL.TranClass : Edm.String
PX.Objects.AP.APTranPostGL.TranType : Edm.String
PX.Objects.AP.APTranPostGL.TranRefNbr : Edm.String
PX.Objects.AP.APTranPostGL.ReferenceID : Edm.Int32
PX.Objects.AP.APTranPostGL.RefNoteID : Edm.Guid
PX.Objects.AP.APTranPostGL.IsMigratedRecord : Edm.Boolean
PX.Objects.AP.APTranPostGL.CuryBalanceAmt : Edm.Decimal "Balance"
PX.Objects.AP.APTranPostGL.BalanceAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.CuryDebitAPAmt : Edm.Decimal "Debit AP Amt."
PX.Objects.AP.APTranPostGL.DebitAPAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.CuryCreditAPAmt : Edm.Decimal "Credit AP Amt."
PX.Objects.AP.APTranPostGL.CreditAPAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.CuryTurnDiscAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.TurnDiscAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.CuryTurnWHTaxAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.TurnWHTaxAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.CuryTurnRetainageAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.TurnRetainageAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.CuryRetainageReleasedAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.RetainageReleasedAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.CuryRetainageUnreleasedAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.RetainageUnreleasedAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.TurnRGOLAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.RGOLAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.CuryTurnAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.TurnAmt : Edm.Decimal
PX.Objects.AP.APTranPostGL.GLSign : Edm.Int16
PX.Objects.AP.APTranPostGL.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APTranPostGL.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTranPostGL.APPaymentByRefNbr -> PX.Objects.AP.APPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTranPostGL.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTranPostGL.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AP.APTranPostGL.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AP.APTranPostGL.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.AP.APTranPostGL.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AP.APTranPostGL.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTranPostGL.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)

# PX.Objects.AP.APTranPostGLwithLines (EntityType)

Label: "AP Document Post GL with Lines"
Key: DocType, Ord, RefNbr
Entity sets: PX_Objects_AP_APTranPostGLwithLines, APDocumentPostGLwithLines, APTranPostGLwithLines
Non-filterable, non-selectable: PrintDocType, CuryDebitAPAmt, DebitAPAmt, CuryCreditAPAmt, CreditAPAmt, CuryTurnDiscAmt, TurnDiscAmt, CuryTurnWHTaxAmt, TurnWHTaxAmt, TurnRGOLAmt

PX.Objects.AP.APTranPostGLwithLines.DocType : Edm.String [key] "Doc. Type"
PX.Objects.AP.APTranPostGLwithLines.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.AP.APTranPostGLwithLines.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.AP.APTranPostGLwithLines.OrigRefNbr : Edm.String "Orig. Ref. Nbr."
PX.Objects.AP.APTranPostGLwithLines.TranType : Edm.String
PX.Objects.AP.APTranPostGLwithLines.Ord : Edm.Int16 [key]
PX.Objects.AP.APTranPostGLwithLines.PrintDocType : Edm.String "Type"
PX.Objects.AP.APTranPostGLwithLines.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.AP.APTranPostGLwithLines.ID : Edm.Int32
PX.Objects.AP.APTranPostGLwithLines.ProjectID : Edm.Int32
PX.Objects.AP.APTranPostGLwithLines.Released : Edm.Boolean
PX.Objects.AP.APTranPostGLwithLines.OpenDoc : Edm.Boolean
PX.Objects.AP.APTranPostGLwithLines.Prebooked : Edm.Boolean
PX.Objects.AP.APTranPostGLwithLines.Voided : Edm.Boolean
PX.Objects.AP.APTranPostGLwithLines.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APTranPostGLwithLines.ClosedFinPeriodID : Edm.String
PX.Objects.AP.APTranPostGLwithLines.ClosedTranPeriodID : Edm.String
PX.Objects.AP.APTranPostGLwithLines.SourceDocType : Edm.String "Source Doc. Type"
PX.Objects.AP.APTranPostGLwithLines.SourceRefNbr : Edm.String "Source Ref. Nbr."
PX.Objects.AP.APTranPostGLwithLines.CuryID : Edm.String
PX.Objects.AP.APTranPostGLwithLines.CuryInfoID : Edm.Int64
PX.Objects.AP.APTranPostGLwithLines.FinPeriodID : Edm.String "Application Period"
PX.Objects.AP.APTranPostGLwithLines.TranPeriodID : Edm.String
PX.Objects.AP.APTranPostGLwithLines.APRegisterTranPeriodID : Edm.String
PX.Objects.AP.APTranPostGLwithLines.APRegisterDocDate : Edm.DateTimeOffset "Date"
PX.Objects.AP.APTranPostGLwithLines.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AP.APTranPostGLwithLines.ClosedDate : Edm.DateTimeOffset
PX.Objects.AP.APTranPostGLwithLines.BalanceSign : Edm.Int16
PX.Objects.AP.APTranPostGLwithLines.Type : Edm.String
PX.Objects.AP.APTranPostGLwithLines.TranClass : Edm.String
PX.Objects.AP.APTranPostGLwithLines.TranRefNbr : Edm.String
PX.Objects.AP.APTranPostGLwithLines.ReferenceID : Edm.Int32
PX.Objects.AP.APTranPostGLwithLines.RefNoteID : Edm.Guid
PX.Objects.AP.APTranPostGLwithLines.IsMigratedRecord : Edm.Boolean
PX.Objects.AP.APTranPostGLwithLines.PaymentsByLinesAllowed : Edm.Boolean
PX.Objects.AP.APTranPostGLwithLines.OrigBalanceAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.BalanceAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.CuryDebitAPAmt : Edm.Decimal "Debit AP Amt."
PX.Objects.AP.APTranPostGLwithLines.DebitAPAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.CuryCreditAPAmt : Edm.Decimal "Credit AP Amt."
PX.Objects.AP.APTranPostGLwithLines.CreditAPAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.CuryTurnDiscAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.TurnDiscAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.CuryTurnWHTaxAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.TurnWHTaxAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.TurnRGOLAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.RGOLAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.ReleasedRetainageAmt : Edm.Decimal
PX.Objects.AP.APTranPostGLwithLines.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AP.APTranPostGLwithLines.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)

# PX.Objects.AP.APTranRetainage (EntityType)

Label: "AP Tran Retainage"
Key: OrigDocType, OrigLineNbr, OrigRefNbr
Entity sets: PX_Objects_AP_APTranRetainage, APTranRetainage

PX.Objects.AP.APTranRetainage.OrigDocType : Edm.String [key]
PX.Objects.AP.APTranRetainage.OrigRefNbr : Edm.String [key]
PX.Objects.AP.APTranRetainage.OrigLineNbr : Edm.Int32 [key]
PX.Objects.AP.APTranRetainage.TranBalSigned : Edm.Decimal
PX.Objects.AP.APTranRetainage.OrigTranAmtSigned : Edm.Decimal

# PX.Objects.AP.APVendorPrice (EntityType)

Label: "AP Vendor Price"
Key: RecordID
Entity sets: PX_Objects_AP_APVendorPrice, APVendorPrice

PX.Objects.AP.APVendorPrice.RecordID : Edm.Int32 [key]
PX.Objects.AP.APVendorPrice.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.APVendorPrice.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AP.APVendorPrice.AlternateID : Edm.String "Alternate ID"
PX.Objects.AP.APVendorPrice.CuryID : Edm.String "Currency"
PX.Objects.AP.APVendorPrice.UOM : Edm.String "UOM"
PX.Objects.AP.APVendorPrice.IsPromotionalPrice : Edm.Boolean "Promotional"
PX.Objects.AP.APVendorPrice.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AP.APVendorPrice.SalesPrice : Edm.Decimal "Price"
PX.Objects.AP.APVendorPrice.BreakQty : Edm.Decimal [required] "Break Qty."
PX.Objects.AP.APVendorPrice.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AP.APVendorPrice.tstamp : Edm.Binary
PX.Objects.AP.APVendorPrice.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.APVendorPrice.CreatedByScreenID : Edm.String
PX.Objects.AP.APVendorPrice.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APVendorPrice.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.APVendorPrice.LastModifiedByScreenID : Edm.String
PX.Objects.AP.APVendorPrice.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.APVendorPrice.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.APVendorPrice.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.APVendorPrice.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AP.APVendorPrice.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.APVendorPrice.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.APVendorPrice.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AP.APVendorPrice.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AP.APVendorPrice.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)

# PX.Objects.AP.BalancedAPDocument (EntityType)

Label: "Document"
BaseType: PX.Objects.AP.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_BalancedAPDocument
Non-filterable, non-selectable: VendorRefNbr

PX.Objects.AP.BalancedAPDocument.InvoiceNbr : Edm.String
PX.Objects.AP.BalancedAPDocument.ExtRefNbr : Edm.String
PX.Objects.AP.BalancedAPDocument.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.AP.BalancedAPDocument.PrintCheck : Edm.Boolean

# PX.Objects.AP.BaseAPHistoryByPeriod (EntityType)

Label: "Base AP History by Period"
Key: AccountID, BranchID, FinPeriodID, SubID, VendorID
Entity sets: PX_Objects_AP_BaseAPHistoryByPeriod, BaseAPHistorybyPeriod

PX.Objects.AP.BaseAPHistoryByPeriod.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.AP.BaseAPHistoryByPeriod.VendorID : Edm.Int32 [key] "Vendor"
PX.Objects.AP.BaseAPHistoryByPeriod.AccountID : Edm.Int32 [key] "Account"
PX.Objects.AP.BaseAPHistoryByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.AP.BaseAPHistoryByPeriod.LastActivityPeriod : Edm.String "Last Activity Period"
PX.Objects.AP.BaseAPHistoryByPeriod.FinPeriodID : Edm.String [key] "Post Period"
PX.Objects.AP.BaseAPHistoryByPeriod.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)

# PX.Objects.AP.CalcAPTranGLwithLinesReport (EntityType)

Label: "Aggrigate AP Document Post GL with Lines"
Key: AgingDate, DocType, OrigDocType, OrigRefNbr, ProjectID, RefNbr
Entity sets: PX_Objects_AP_CalcAPTranGLwithLinesReport, AggrigateAPDocumentPostGLwithLines, CalcAPTranGLwithLinesReport

PX.Objects.AP.CalcAPTranGLwithLinesReport.ProjectID : Edm.Int32 [key]
PX.Objects.AP.CalcAPTranGLwithLinesReport.DocType : Edm.String [key] "Doc. Type"
PX.Objects.AP.CalcAPTranGLwithLinesReport.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.AP.CalcAPTranGLwithLinesReport.OrigDocType : Edm.String [key] "Orig Doc. Type"
PX.Objects.AP.CalcAPTranGLwithLinesReport.OrigRefNbr : Edm.String [key] "Orig Ref. Nbr."
PX.Objects.AP.CalcAPTranGLwithLinesReport.AgingDate : Edm.DateTimeOffset [key]
PX.Objects.AP.CalcAPTranGLwithLinesReport.OrigBalanceAmt : Edm.Decimal
PX.Objects.AP.CalcAPTranGLwithLinesReport.BalanceAmt : Edm.Decimal
PX.Objects.AP.CalcAPTranGLwithLinesReport.OrigRetainageAmt : Edm.Decimal
PX.Objects.AP.CalcAPTranGLwithLinesReport.ReleasedRetainageAmt : Edm.Decimal
PX.Objects.AP.CalcAPTranGLwithLinesReport.APRegisterByRefNbr -> PX.Objects.AP.APRegister (DocType=DocType, RefNbr=RefNbr)
