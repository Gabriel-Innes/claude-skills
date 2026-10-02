# Sage 200 Evolution table dictionary - Application metadata

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _atblAuthToken
PK: idToken
Columns (17):
  idToken int NOT NULL identity PK
  EmailAccountID int NULL
  cAccountName varchar(256) NULL
  cAccessToken varchar(max) NULL
  cTokenType varchar(64) NULL
  dTokenExpires datetime NULL
  cRefreshToken varchar(max) NULL
  cScope varchar(512) NULL
  _atblAuthToken_iBranchID int NULL
  _atblAuthToken_dCreatedDate datetime NULL
  _atblAuthToken_dModifiedDate datetime NULL
  _atblAuthToken_iCreatedBranchID int NULL
  _atblAuthToken_iModifiedBranchID int NULL
  _atblAuthToken_iCreatedAgentID int NULL
  _atblAuthToken_iModifiedAgentID int NULL
  _atblAuthToken_iChangeSetID int NULL
  _atblAuthToken_Checksum binary(20) NULL

## _atblBulkAuthToken
PK: idToken
Columns (17):
  idToken int NOT NULL identity PK
  BulkEmailAccountID int NULL
  cAccountName varchar(256) NULL
  cAccessToken varchar(max) NULL
  cTokenType varchar(64) NULL
  dTokenExpires datetime NULL
  cRefreshToken varchar(max) NULL
  cScope varchar(512) NULL
  _atblBulkAuthToken_iBranchID int NULL
  _atblBulkAuthToken_dCreatedDate datetime NULL
  _atblBulkAuthToken_dModifiedDate datetime NULL
  _atblBulkAuthToken_iCreatedBranchID int NULL
  _atblBulkAuthToken_iModifiedBranchID int NULL
  _atblBulkAuthToken_iCreatedAgentID int NULL
  _atblBulkAuthToken_iModifiedAgentID int NULL
  _atblBulkAuthToken_iChangeSetID int NULL
  _atblBulkAuthToken_Checksum binary(20) NULL

## _atblBulkEmailAccounts - AR Mail Merge
Alias: AR Mail Merge | Freedom Name:  | Record Identifier: 
Notes: Mail Merge. E-mail Accounts
PK: idBulkEmailAccount
Columns (17):
  idBulkEmailAccount int NOT NULL identity PK
  cEmailSettingName varchar(100) NOT NULL
  cFromEmail varchar(200) NULL
  cToEmail varchar(200) NULL
  cSMTPServer varchar(50) NULL
  iPortNumber int NULL
  cEmailUserName varchar(200) NULL
  cEmailPassword varchar(150) NULL
  bEmailRequiresSSL bit NOT NULL
  bEmailRequiresTLS bit NOT NULL default (0)
  bUseOAuth2 bit NOT NULL default (0)
  SMTPClientId varchar(256) NULL default ''
  SMTPClientSecret varchar(256) NULL default ''
  SMTPAuthUrl varchar(256) NULL default ''
  SMTPTokenUrl varchar(256) NULL default ''
  SMTPScope varchar(256) NULL default ''
  SMTPRedirectUrl varchar(256) NULL default ''

## _atblBulkEmailFilters - Bulk Email filters
Alias: Bulk Email filters | Freedom Name:  | Record Identifier: 
Notes: Mail Merge. E-mail filter Groups
PK: idBulkEmailFilter
Columns (9):
  idBulkEmailFilter int NOT NULL identity PK
  cEmailFilterName varchar(50) NOT NULL
  iFromCustomer varchar(20) NULL
  iToCustomer varchar(20) NULL
  cCustomerGroups varchar(max) NULL
  cAreas varchar(max) NULL
  cSalesReps varchar(max) NULL
  cCurrencies varchar(max) NULL
  cCustomerField varchar(150) NULL

## _atblBulkEmailHistory - Bul Email History
Alias: Bul Email History | Freedom Name:  | Record Identifier: 
Notes: Mail Merge. Bulk E-mail history
PK: idBulkEmailHistory
Columns (6):
  idBulkEmailHistory int NOT NULL identity PK
  iCustomerID int NOT NULL
  iBulkEmailTemplateID int NOT NULL
  cSentToEmailAddress varchar(50) NULL
  dTimeStamp datetime NOT NULL
  cMessage varchar(max) NOT NULL

## _atblBulkEmailHistoryDocuments - Bulk e-mail History Documents
Alias: Bulk e-mail History Documents | Freedom Name:  | Record Identifier: 
Notes: Mail merge. Bulk E-mail history documents
PK: idBulkEmailHistoryDocument
Columns (3):
  idBulkEmailHistoryDocument int NOT NULL identity PK
  iBulkEmailHistoryID int NOT NULL
  binDocument varbinary(max) NOT NULL

## _atblBulkEmailTemplateData - Bulk E-mail template data
Alias: Bulk E-mail template data | Freedom Name:  | Record Identifier: 
Notes: Mail Merge. Bulk E-mail Template data
PK: idBulkEmailTemplateData
Columns (3):
  idBulkEmailTemplateData int NOT NULL identity PK
  iBulkEmailTemplateID int NOT NULL
  binData varbinary(max) NOT NULL

## _atblBulkEmailTemplates - Bulk E-mail Templates
Alias: Bulk E-mail Templates | Freedom Name:  | Record Identifier: 
Notes: Mail Merge. Bulk E-Mail Templates
PK: idBulkEmailTemplate
Columns (10):
  idBulkEmailTemplate int NOT NULL identity PK
  cTemplateName varchar(50) NULL
  cTemplateDescription varchar(50) NULL
  cDefaultOutline varchar(100) NULL
  bAllowSendSameTemplate bit NOT NULL
  bCreateIncident bit NOT NULL
  iIncidentDefaultAgentID int NOT NULL
  iIncidentTypeID int NOT NULL
  iDueInDays int NOT NULL
  bCreateAsClosed bit NOT NULL

## _atblBulkEmailUDFFilters - BulkEMailUDFFilters
Alias: BulkEMailUDFFilters | Freedom Name:  | Record Identifier: 
Notes: Mail Merge. Bulk E-Mail UDF Filters
PK: idBulkEmailUDFFilter
Columns (7):
  idBulkEmailUDFFilter int NOT NULL identity PK
  iBulkEmailFilterID int NOT NULL
  cUDFTableName varchar(100) NOT NULL
  cUDFFieldName varchar(100) NOT NULL
  cValue varchar(100) NULL
  cToValue varchar(100) NULL
  iFieldType int NOT NULL

## _atblColumnLookups - Column Lookups
Alias: Column Lookups | Freedom Name:  | Record Identifier: 
Notes: Data Import. Lookups
PK: idColumnLookup
Columns (6):
  idColumnLookup int NOT NULL identity PK
  cTableName varchar(256) NOT NULL
  cColumnName varchar(256) NOT NULL
  cLookupTable varchar(256) NOT NULL
  cLookupColumn varchar(256) NOT NULL
  bIsValueLookup bit NOT NULL

## _atblColumnLookupValues - Column Lookup Values
Alias: Column Lookup Values | Freedom Name:  | Record Identifier: 
Notes: Data Import. Lookup Values
PK: idColumnLookupValue
Columns (4):
  idColumnLookupValue int NOT NULL identity PK
  iColumnLookupID int NOT NULL
  cLookupCode varchar(100) NOT NULL
  cValue varchar(100) NOT NULL

## _atblColumns - Columns
Alias: Columns | Freedom Name:  | Record Identifier: 
Notes: Data Import. Columns
PK: idColumn
Columns (6):
  idColumn int NOT NULL identity PK
  cTableName varchar(256) NOT NULL
  cColumnName varchar(256) NOT NULL
  iColumnSelectType int NOT NULL
  cDefaultValue varchar(1000) NOT NULL
  bSystemColumn bit NOT NULL

## _atblDocDefaults - Data Import Defaults
Alias: Data Import Defaults | Freedom Name:  | Record Identifier: 
Notes: Data Import Defaults
PK: idDocDefault
Columns (16):
  idDocDefault int NOT NULL identity PK
  bCreateIncident bit NOT NULL
  iIncidentDefaultAgentID int NULL
  iIncidentTypeID int NULL
  bIncidentAttachDocument bit NULL
  iImportFileType int NOT NULL
  cDelimiter varchar(5) NOT NULL
  cDateFormat varchar(20) NOT NULL
  cDateSeparator varchar(5) NOT NULL
  bUseShortDate bit NOT NULL
  cDocumentImportPath varchar(500) NOT NULL
  bSendEmail bit NOT NULL
  bEmailAttachDocument bit NULL
  iEmailAccountID int NOT NULL
  iHeaderCaptionType int NOT NULL
  cServerName varchar(200) NOT NULL

## _atblDocImportDocumentTemplates - Document Import Templates
Alias: Document Import Templates | Freedom Name:  | Record Identifier: 
Notes: Data Import. Table Templates
PK: idDocImportDocumentTemplate
Columns (3):
  idDocImportDocumentTemplate int NOT NULL identity PK
  cDescription varchar(100) NOT NULL
  cPrimaryTable varchar(100) NOT NULL

## _atblDocImportDocumentTemplateTables - Document Import Template Tables
Alias: Document Import Template Tables | Freedom Name:  | Record Identifier: 
Notes: Data Import. Table Template Relationships
PK: idDocumentTemplateTable
Columns (3):
  idDocumentTemplateTable int NOT NULL identity PK
  iDocumentTemplateID int NOT NULL
  cTableName varchar(256) NOT NULL

## _atblDocImportDocumentTypes - Document Import Document Types
Alias: Document Import Document Types | Freedom Name:  | Record Identifier: 
Notes: Data Import. document Types
PK: idDocImportDocumentTypes
Columns (4):
  idDocImportDocumentTypes int NOT NULL identity PK
  cDocumentType varchar(100) NOT NULL
  cFilePrefix varchar(50) NOT NULL
  iDocImportDocumentTemplateID int NOT NULL

## _atblDocImportFieldMappings - Import Field Mapping
Alias: Import Field Mapping | Freedom Name:  | Record Identifier: 
Notes: Data Import
PK: idDocImportFieldMapping
Columns (9):
  idDocImportFieldMapping int NOT NULL identity PK
  iDocImportDocumentTypeID int NOT NULL
  cTableName varchar(100) NOT NULL
  cFieldName varchar(100) NOT NULL
  iPosition int NOT NULL
  bImportCodeInstead bit NOT NULL
  bRequiredField bit NOT NULL
  cCaption varchar(100) NULL
  bCreate bit NULL

## _atblEmailAccounts - E-Mail Accounts
Alias: E-Mail Accounts | Freedom Name:  | Record Identifier: 
Notes: Data Import Export Module
PK: idEmailAccount
Columns (18):
  idEmailAccount int NOT NULL identity PK
  cEmailSettingName varchar(100) NOT NULL
  cFromEmail varchar(200) NULL
  cToEmail varchar(200) NULL
  cSMTPServer varchar(50) NULL
  iPortNumber int NULL
  cEmailUserName varchar(200) NULL
  cEmailPassword varchar(50) NULL
  bEmailRequiresSSL bit NOT NULL
  cDefaultOutline varchar(100) NULL
  bEmailRequiresTLS bit NOT NULL default (0)
  bUseOAuth2 bit NOT NULL default (0)
  SMTPClientId varchar(256) NULL default ''
  SMTPClientSecret varchar(256) NULL default ''
  SMTPAuthUrl varchar(256) NULL default ''
  SMTPTokenUrl varchar(256) NULL default ''
  SMTPScope varchar(256) NULL default ''
  SMTPRedirectUrl varchar(256) NULL default ''

## _atblExportDefaults - Export Defaults
Alias: Export Defaults | Freedom Name:  | Record Identifier: 
Notes: Export Utility
PK: idExportDefault
Columns (11):
  idExportDefault int NOT NULL identity PK
  iImportFileType int NOT NULL
  cDelimiter varchar(5) NOT NULL
  cDateFormat varchar(20) NOT NULL
  cDateSeparator varchar(5) NOT NULL
  bUseShortDate bit NOT NULL
  cDocumentExportPath varchar(500) NOT NULL
  bSendEmail bit NOT NULL
  bAppendDate bit NOT NULL
  iHeaderCaptionType int NOT NULL
  iEmailAccountID int NOT NULL

## _atblExportFieldMappings - Export Field Mappings
Alias: Export Field Mappings | Freedom Name:  | Record Identifier: 
Notes: Export Utility. Template field mappings
PK: idExportFieldMapping
Columns (6):
  idExportFieldMapping int NOT NULL identity PK
  iExportTemplateID int NOT NULL
  cTableName varchar(100) NOT NULL
  cFieldName varchar(100) NOT NULL
  iPosition int NOT NULL
  cCaption varchar(100) NULL

## _atblExportTemplates - Export Templates
Alias: Export Templates | Freedom Name:  | Record Identifier: 
Notes: Export Template Header
PK: idExportTemplate
Columns (21):
  idExportTemplate int NOT NULL identity PK
  cTemplateDescription varchar(100) NOT NULL
  cTableName varchar(258) NOT NULL
  cFilePrefix varchar(20) NOT NULL
  bAppendDateToFile bit NOT NULL
  bPlaceInSubFolder bit NOT NULL
  cSubFolderName varchar(128) NOT NULL
  bSendEmailAfterExport bit NOT NULL
  bAttachExportFileToEmail bit NOT NULL
  cSendEmailTo varchar(256) NOT NULL
  bCreateIncidentAfterExport bit NOT NULL
  bAttachExportFileToIncident bit NOT NULL
  iIncidentTypeID int NOT NULL
  iAssignedToAgentID int NOT NULL
  iExportType int NULL
  cColumnName varchar(128) NULL
  iLastExportedID int NULL
  dLastExportedDate datetime NULL
  bIncludeRowCounter bit NULL
  bCreateModifiedTrigger bit NULL
  cRowCounterCaption varchar(50) NULL

## _atblTableRelationships - Table Relationship
Alias: Table Relationship | Freedom Name:  | Record Identifier: 
Notes: Data Import. Table Relationships
PK: idTableRelationship
Columns (8):
  idTableRelationship int NOT NULL identity PK
  cPrimaryTable varchar(256) NOT NULL
  cPrimaryColumn varchar(256) NOT NULL
  cForeignTable varchar(256) NOT NULL
  cForeignColumn varchar(256) NOT NULL
  cCriteriaColumn varchar(1024) NOT NULL
  iCompareType varchar(1024) NOT NULL
  cCriteriaValues varchar(1024) NOT NULL

## _atblTables - Tables
Alias: Tables | Freedom Name:  | Record Identifier: 
Notes: Data Import Module. Tables
PK: idTable
Columns (4):
  idTable int NOT NULL identity PK
  cName varchar(256) NOT NULL
  cUserFreindlyTableName varchar(256) NOT NULL
  cCodeColumn varchar(256) NOT NULL
