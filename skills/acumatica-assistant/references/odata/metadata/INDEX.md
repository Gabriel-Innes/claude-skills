<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# DAC-based OData metadata snapshot

Compiled from `GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata` of a clean **Acumatica ERP 2026 R2** instance by `scripts/build_odata_metadata_ref.py`. It is the OData v4 CSDL of the DAC-based interface, not a tenant's generic-inquiry (`/api/odata/gi`) metadata and not the contract-based REST API's `swagger.json`.

| Path | Covers |
|---|---|
| `entity-sets.md` | One row per DAC: the entity-set names accepted in the URL, key fields, non-filterable fields, `Filterable=false`; plus singletons |
| `api/INDEX.md` | One row per EntityType / ComplexType: label, key, counts, base type, entity sets, and the bundle file + line range of its entry |
| `api/members-NN.md` | The entries: a heading per type, then `Type.Field : Edm.Type [key] [required] "Display name"` and `Type.Nav -> Target (LocalField=TargetField)` lines |
| `enums.md` | `Enum.Member = Value` lines |

## How to read it

- **Which DAC / which URL name?** grep `entity-sets.md` for the class name, the display name (`| Sales Order |`) or the URL alias.
- **Fields of a DAC**: grep `api/members-*.md` for `^PX\.Objects\.SO\.SOOrder\.` (one line per field and navigation property), or take `File` / `Line` / `Lines` from `api/INDEX.md` and read that range. A DAC with a `BaseType` (for example `PX.Objects.AR.Customer : PX.Objects.CR.BAccount`) lists only the fields it adds; read the base type's entry for the rest, including the key.
- **Which DACs have a field named X?** grep `api/members-*.md` for `\.X : `.
- **Joins**: a navigation line `A.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)` means `$expand=BAccountByCustomerID` and that `A.CustomerID` equals `BAccount.BAccountID`; `A.SOLineCollection -> Collection(PX.Objects.SO.SOLine)` is a detail collection.
- Field lines carry the field's UI display name in quotes when the metadata has one (the `Org.OData.Core.V1.Description` annotation), which is how a user's wording ("Customer Order Nbr.") maps to a field (`CustomerOrderNbr`).

## Counts

- schemas: 211
- entity_types: 2265
- complex_types: 25
- fields: 42288
- fields_with_display_name: 26342
- navigation_properties: 23576
- entity_sets: 5108
- dacs_with_entity_sets: 2198
- singletons: 158
- dacs_with_non_filterable_fields: 1074
- dacs_filterable_false: 56
- enum_members: 6
- excluded_types: 0
- member_bundles: 6

## Edm types used

`Edm.String` (14031), `Edm.Decimal` (7120), `Edm.Int32` (6144), `Edm.Boolean` (5305), `Edm.DateTimeOffset` (3899), `Edm.Guid` (3736), `Edm.Binary` (1167), `Edm.Int16` (438), `Edm.Int64` (366), `Edm.Byte` (42), `Edm.Double` (31), `Edm.Single` (5), `Collection(Edm.String)` (3), `PX.SM.CustObjectTypes` (1)

## Scope and limits

- One clean instance, one release. A customer's instance adds customization and user-defined fields, extension DACs and custom namespaces, and may lack modules (Manufacturing, Payroll, Field Service, Construction ...) whose DACs are listed here. Absence here is not proof of absence there, and presence here is not proof of presence there: confirm on the client's `/api/odata/dac/$metadata`.
- The DAC-based interface exposes DACs, not forms. A DAC's fields are the database-backed and unbound fields the server publishes; the metadata does not say which fields are populated for a given record type.
- Navigation property names are generated (`<Target>By<LocalField>` for lookups, `<Detail>Collection` for details); the referential constraint in parentheses is the join the server uses.
- `Edm.Decimal` fields are declared with `Scale="Variable"`; `Edm.Binary` is used for `tstamp`; no `MaxLength` or `Precision` facets are published.
- The `px.GetDeletedRecords()` function documented for removed-record tracking is not declared in this metadata; its result shape is the `PX.Api.OData.DAC.DeletedRecordResult` complex type (`RefNoteID`, `DeleteDate`).
- Namespaces: Default, PX.AI.Tools.DAC, PX.AI.Tools.GI.DAC, PX.AIStudio.DAC, PX.Api, PX.Api.ContractBased.UI.DAC, PX.Api.Mobile.ImageRecognition.DAC, PX.Api.Mobile.MultiFactorAuth.DAC, PX.Api.Mobile.PushNotifications.DAC, PX.Api.Mobile.Workspaces, PX.Api.Mobile.Workspaces.DAC, PX.Api.ModelContextProtocol.UI.DAC, PX.Api.OData.DAC, PX.Api.Webhooks, PX.Api.Webhooks.DAC, PX.AutocompleteGenerator.UI.DAC, PX.BusinessProcess.DAC, PX.CS, PX.CloudServices.DAC, PX.Commerce.Amazon, PX.Commerce.BigCommerce, PX.Commerce.Core, PX.Commerce.Objects, PX.Commerce.Shopify, PX.Dashboards.DAC, PX.Dashboards.Widgets, PX.Data, PX.Data.Archiving.DAC, PX.Data.DeletedRecordsTracking.DAC, PX.Data.Descriptor.Attributes, PX.Data.GenericInquiry.DAC, PX.Data.Licensing.SM, PX.Data.Localization, PX.Data.Maintenance.GI, PX.Data.Maintenance.SM.DAC, PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring, PX.Data.Maintenance.SM.DAC.LicenseResourceMonitoring.Mappings, PX.Data.Maintenance.SM.SendRecurringNotifications, PX.Data.Maintenance.TenantOperations, PX.Data.Maintenance.TenantShapshotDeletion.DAC, PX.Data.ProjectDefinition.Workflow, PX.Data.Reports, PX.Data.RichTextEdit, PX.Data.Search, PX.Data.Services.Implementations, PX.Data.Update, PX.Data.UserRecords.FavoriteRecords, PX.Data.UserRecords.RecentlyVisitedRecords, PX.Data.Wiki.Tags, PX.DataSync.HubSpot, PX.DataSync.SendGrid, PX.EP, PX.ESign, PX.ExternalCarriersCommon, PX.ExternalCarriersHelper, PX.FS, PX.GIReports.Maintenance.DAC, PX.ML.Chat.DAC, PX.ML.Chat.Licensing.DAC, PX.ML.CrossSales.DAC, PX.MSGraph.DAC.SM, PX.MSTeams.DAC.SM, PX.Mail.Log.DAC, PX.OAuthClient.DAC, PX.Objects, PX.Objects.AM, PX.Objects.AM.CacheExtensions, PX.Objects.AM.SFK, PX.Objects.AP, PX.Objects.AP.DAC, PX.Objects.AP.InvoiceRecognition.DAC, PX.Objects.AP.Overrides.APDocumentRelease, PX.Objects.AP.Overrides.ScheduleMaint, PX.Objects.AP.Standalone, PX.Objects.AR, PX.Objects.AR.Light, PX.Objects.AR.Override, PX.Objects.AR.Overrides.ARDocumentRelease, PX.Objects.AR.Overrides.ScheduleMaint, PX.Objects.AR.Standalone, PX.Objects.CA, PX.Objects.CA.BankStatementHelpers, PX.Objects.CA.Light, PX.Objects.CC, PX.Objects.CM, PX.Objects.CM.Extensions, PX.Objects.CN, PX.Objects.CN.CRM.CR.DAC, PX.Objects.CN.Compliance.CL.DAC, PX.Objects.CN.Compliance.PM.DAC, PX.Objects.CN.JointChecks, PX.Objects.CN.Requirements.ComplianceRequirementFields, PX.Objects.CN.Requirements.DAC, PX.Objects.CN.Subcontracts.SC.DAC, PX.Objects.CR, PX.Objects.CR.DAC, PX.Objects.CR.DAC.Standalone, PX.Objects.CR.Inquiry, PX.Objects.CR.Standalone, PX.Objects.CS, PX.Objects.CS.DAC, PX.Objects.CS.Email, PX.Objects.CT, PX.Objects.CT.Standalone, PX.Objects.Common.DAC, PX.Objects.Common.DAC.ReportParameters, PX.Objects.DR, PX.Objects.EP, PX.Objects.EP.ClockInClockOut, PX.Objects.EP.DAC, PX.Objects.EP.Standalone, PX.Objects.FA, PX.Objects.FA.DAC, PX.Objects.FA.Overrides.AssetProcess, PX.Objects.FA.Standalone, PX.Objects.FS, PX.Objects.GDPR, PX.Objects.GL, PX.Objects.GL.ADL, PX.Objects.GL.DAC, PX.Objects.GL.DAC.Standalone, PX.Objects.GL.FinPeriods, PX.Objects.GL.FinPeriods.TableDefinition, PX.Objects.GL.Overrides.ScheduleMaint, PX.Objects.GL.Overrides.ScheduleProcess, PX.Objects.GL.Reclassification.Common, PX.Objects.GL.Reclassification.UI, PX.Objects.GL.Standalone, PX.Objects.IN, PX.Objects.IN.AffectedAvailability, PX.Objects.IN.DAC, PX.Objects.IN.DAC.Projections, PX.Objects.IN.Matrix.DAC, PX.Objects.IN.Matrix.DAC.Projections, PX.Objects.IN.Matrix.DAC.Unbound, PX.Objects.IN.RelatedItems, PX.Objects.IN.RelatedItems.DAC, PX.Objects.IN.S, PX.Objects.IN.Turnover, PX.Objects.Localizations.CA, PX.Objects.Localizations.GB, PX.Objects.Localizations.GB.HMRC.DAC, PX.Objects.MN, PX.Objects.MN.DAC.Projections, PX.Objects.MN.POCreateExt, PX.Objects.PJ.Common.DAC, PX.Objects.PJ.DailyFieldReports.PJ.DAC, PX.Objects.PJ.DrawingLogs.PJ.DAC, PX.Objects.PJ.PhotoLogs.PJ.DAC, PX.Objects.PJ.ProjectManagement.PJ.DAC, PX.Objects.PJ.ProjectsIssue.PJ.DAC, PX.Objects.PJ.RequestsForInformation.PJ.DAC, PX.Objects.PJ.Submittals.PJ.DAC, PX.Objects.PM, PX.Objects.PM.DAC, PX.Objects.PM.DAC.Reports, PX.Objects.PM.Lite, PX.Objects.PM.MaterialManagement.MaterialList, PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments, PX.Objects.PM.Project.Cashflow, PX.Objects.PM.Project.Cashflow.Projections, PX.Objects.PM.ProjectFiles.FileEntryForms, PX.Objects.PM.ProjectFiles.ProjectEntities, PX.Objects.PM.ProjectFiles.VendorEntities, PX.Objects.PM.ProjectParentChild, PX.Objects.PO, PX.Objects.PO.DAC.Projections, PX.Objects.PO.LandedCosts, PX.Objects.PR, PX.Objects.PR.Standalone, PX.Objects.Portals, PX.Objects.Portals.SP.DAC, PX.Objects.Portals.Vendor.Configuration, PX.Objects.Portals.Vendor.Dashboard.RecentActivities, PX.Objects.Portals.Vendor.Dashboard.ToDo, PX.Objects.RQ, PX.Objects.RQ.DAC, PX.Objects.SO, PX.Objects.SO.DAC.Projections, PX.Objects.SO.DAC.Unbound, PX.Objects.SO.Report, PX.Objects.SO.Standalone, PX.Objects.SO.Table, PX.Objects.SV, PX.Objects.SV.DACUnbound, PX.Objects.SV.Reports, PX.Objects.TX, PX.Objects.TX.DAC, PX.Objects.WZ, PX.OidcClient.GraphExtensions, PX.Olap.Maintenance, PX.PaymentProcessor.AvidXchange.DAC, PX.PaymentProcessor.BillCom.DAC, PX.PaymentProcessor.ProcessorBase.DAC, PX.PaymentProcessorCommon.DAC, PX.PushNotifications.UI.DAC, PX.SM, PX.SM.AU, PX.SM.Alias, PX.SM.Reduced, PX.SM.Standalone, PX.SP.Alias, PX.Salesforce, PX.ScreenPreferences.DAC, PX.SiteMap.DAC, PX.SmsProvider.SM.DAC, PX.TM, PX.TokenLogin, PX.Web.UI, PX.Web.UI.Frameset.Model.DAC, ReconciliationTools.
