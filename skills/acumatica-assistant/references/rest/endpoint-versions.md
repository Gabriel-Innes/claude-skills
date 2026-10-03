<!-- source: Acumatica Integration Development Guide, "Configuring the REST API > Contract Versions" and "Comparison of System Endpoints", "Basic Requests > Retrieve the Acumatica ERP Version, Enabled Features, and Endpoints"; URLs in INDEX.md | version: Acumatica ERP 2026 R2 (guide edition 2026-09-30) | verified: 2026-10-03 -->

# System endpoint versions and contract versions

## 1. Contract versions

(*Contract Versions*.)

- Acumatica ERP 2026 R2 supports **Contract Versions 4 and 5**. Contract Version 1 is unsupported since 2018 R2;
  Contract Versions 2 and 3 are unsupported since **2023 R2**.
- Custom endpoints created from scratch get Contract Version 5; an endpoint extension inherits the base
  endpoint's contract version.

| Characteristic | Contract Version 4 | Contract Version 5 |
|---|---|---|
| Query syntax | OData 3.0; nested fields and expansions as slash paths | OData 4.01; `$select`/`$expand` of a nested entity nested in parentheses inside `$expand` |
| Elements outside the endpoint definition (custom fields) | supported | supported |
| Drop-down selected value | plain value | `{"id": ..., "description": ...}`; requests and filters use the ID |
| Drop-down field types | one type, no string/integer or single/multi distinction | `StringSingleSelectValue`, `IntSingleSelectValue`, `StringMultiSelectValue` (array) |
| Filtering multi-select fields defined in the endpoint | `any()`/`all()` not supported | `any()`/`all()` supported |
| Retrieving custom fields | `$custom` | inside `$select` |
| OpenAPI nullability | `value` nullable, wrapper not marked nullable | wrappers and metadata properties explicitly nullable |

## 2. System endpoints compared by the 2026 R2 guide

(*Comparison of System Endpoints*; the page compares each `Default` version with its predecessor.)

| Endpoint | Contract Version | Release the version number corresponds to |
|---|---|---|
| `Default/26.200.001` | **5** | 2026 R2 |
| `Default/25.200.001` | 4 | 2025 R2 |
| `Default/24.200.001` | 4 | 2024 R2 |
| `Default/23.200.001` | 4 | 2023 R2 |
| `Default/22.200.001` | 4 | 2022 R2 |
| `Default/20.200.001` | 4 | 2020 R2 |

The release mapping follows Acumatica's `YY.R00.001` numbering (R1 = `100`, R2 = `200`) as the guide uses it
(for example "Version 26.200.001 and Contract Version 5 to access Acumatica ERP 2026 R2"). The guide's
`GET /entity` example also lists an `eCommerce` endpoint at `20.200.001` and `22.200.001`, and the examples use a
`MANUFACTURING/26.200.001` endpoint. An instance may carry more or fewer system endpoints than this table
(older ones, or ones removed as obsolete): **always confirm with `GET <instance URL>/entity`** on the client's
instance, which lists every endpoint with its `href`.

## 3. What changed between system endpoint versions

The guide's comparison page lists every new, renamed, retyped and removed entity, field and action per step.
The lists below keep the **entities** and the renames/removals that break code; the per-field additions (several
hundred rows, mostly new fields on existing entities) are on the page: open it when a field is missing on an older
endpoint.

### Default/26.200.001 vs 25.200.001 (Contract Version 5 vs 4)

- New entities: `BankStatement`, `CashPurchase`, `ChangeRequest`, `FileTags`, `InvoiceMemoPrintForm`, `MyDayReport`,
  `ProjectMaterials`, `ServiceLocation`, `TagTemplates`, `UploadedFiles`, `WorkEvent`, `WorkOrder`, `WorkTask`,
  `WorkTicket`.
- Renamed fields: `ContactDuplicateDetail.LastModifiedDate`, `DuplicateDetail.LastModifiedDate`,
  `SalesOrder.LastModified`, `SalesOrderDetail.LastModifiedDate` all became `LastModifiedDateTime`.
- Retyped fields (the contract-version change): 163 string single-select fields `StringValue` to
  `StringSingleSelectValue`; 30 integer single-select (including time-span) fields to `IntSingleSelectValue`;
  43 date-without-time fields `DateTimeValue` to `DateOnlyValue`; `CompensationDetail.LastModifiedDateTime`
  `StringValue` to `DateTimeValue`.
- Removed: every `*.Subitem` / `*.DefaultSubitem` field on inventory, sales, purchase, kit, physical-inventory,
  shipment, service-order and opportunity entities; `AppDetails.Subitem`; `Lead.LastIncomingActivity` /
  `LastOutgoingActivity` (use `Lead.LeadActivityStatistics.*`); `SalesInvoice.LastModifiedDate` (use
  `LastModifiedDateTime`); `SalesInvoiceApplicationInvoice.DocumentType` (use `DocType`);
  `SalesOrder.UsrExternalOrderOriginal` (use `ExternalOrderOriginal`); `StockItem.LastModified` and
  `TemplateItems.LastModified` (use `LastModifiedDateTime`); `StockItem.UseOnEntry`;
  `DeductionOrBenefitTaxDetailCA.Benefitincreasestaxablewage` / `Deductiondecreasestaxablewage` (use
  `TaxSettingsCA.ImpactonTaxableWage`, which has the **opposite** logic); `TaxAndReportingCA.SupplementalIncome`
  (use `TaxAndReportingCA.WageType`).
- Notable new fields: `Address.AddressLine3` (all address-bearing entities), `Customer.LegalName`,
  `Vendor.LegalName`, `SalesOrder.ExternalQuoteNbr` / `ExternalQuoteStatus`, `SalesOrderDetail.OrigOrderNbr` /
  `OrigOrderType`, `SalesOrderPayment.NewCard` / `PaymentNoteID`, `Payment.CCProcessingStatus`,
  `TransferOrderDetail.OrderNumber` / `OrderType` / `OrderLineNbr` / `ShipmentNumber` / `RecivedQty`, CRM
  `CreatedByID` / `CreatedDateTime` / `LastModifiedByID` / `SalesTerritoryID` / `OverrideSalesTerritory` on
  BusinessAccount, Contact, Lead, Opportunity, Case; AI fields on Activity, Email, Case, Opportunity.

### Default/25.200.001 vs 24.200.001 (both Contract Version 4)

- New entities: `BillRetainageDocument`, `CompanyTree`.
- New fields: structured address parts (`BuildingName`, `BuildingNumber`, `Department`, `DistrictName`, `Floor`,
  `PostBox`, `Room`, `StreetName`, `SubDepartment`, `TownLocationName`, `UnitNumber`) on `Address`,
  `ProjectAddress`, `SalesInvoiceAddress`, `SrvOrdAddress`, `SubcontractVendorAddressInfo`; `Bill.RetainageDocuments`;
  `CreditCardTransactionDetail.CommerceTranNbr`; `Email.Type`; `Employee.CompanyTreeInfo`; `TimeEntry.TimeZone`.
- Removed: `BusinessAccountMainContact.LanguageOrLocale` (use `BusinessAccount.LocaleName`); `Event.EndDate` /
  `EndTime` (use `EndDateTime`); `ReminderDetail.RemindAtDate` / `RemindAtTime` (use `RemindAtDateTime`);
  `TaxCodeSetting.UseDefault`, `TaxSettingDetail.UseDefault`; `TimeEntry.Time` (never mapped).

### Default/24.200.001 vs 23.200.001 (both Contract Version 4)

- New entities: `AmazonStore`, `CashTransaction`, `CashTransactionDetail`, `SalesInvoiceAddress`,
  `SalesInvoiceDocContact`.
- New fields include `AttributeValue.IsActive`, `BillDetail.LCNbr` / `LCType` / `LCLineNbr`,
  `InventoryReceiptDetail.ReasonCode`, `NonStockItem.IsAKit`, `SalesInvoice.BillToAddress` / `ShipToAddress` /
  `*Contact` / `*Override` / `TaxCalcMode` / `ExternalRef` / `CreatedDate` / `LastModifiedDate`,
  `SalesInvoiceDetail.Account` / `SubAccount` / `ExternalRef` / `ManualPrice` / `NoteID`,
  `SalesOrder.RecalculatePricesDiscounts`, `Shipment.UnlimitedPackages`, `StockItem.LastModifiedDateTime`,
  `TemplateItems.LastModifiedDateTime`, `TransferOrderDetailAllocation.ExpirationDate`.

### Default/23.200.001 vs 22.200.001 (both Contract Version 4)

- New entities: `BCRoleAssignment`, `OrderRisks`, `PaymentCharge`, `ProjectAddress`, `ProjectRetainage`,
  `Subcontract`, `SubcontractDetail`, `SubcontractTaxDetail`, `SubcontractVendorAddressInfo`,
  `SubcontractVendorContactInfo`.
- New fields/actions include `Bill.ReleaseRetainage`, `Bill.IsTaxValid`, `BusinessAccount.CreateContactFromBusinessAccount`,
  `Contact.CreateAccountFromContact`, `Customer.CreateContactFromCustomer`, `Customer.CustomerKind` / `Email` /
  `PrimaryContactID`, `CustomerLocation.Default` / `Status`, `Payment.Charges` / `IsCCPayment`,
  `SalesOrder.Branch` / `MaxRiskScore` / `OrderRisks` / `Relations`, `Vendor.CreateContactFromVendor`,
  `Warehouse.NonStockPickingLocationID` / `UseItemDefaultLocationForPicking`, many `LastModifiedDateTime` fields,
  `Project.ProjectProperties.*` (cost/revenue tax zones, currencies, rate type, inventory tracking mode).
- Changed: parameters of `Lead.ConvertLeadToBAccount` / `ConvertLeadToContact` / `ConvertLeadToOpportunity`,
  `Opportunity.CreateContactFromOpportunity` / `CreateAccountFromOpportunity`; `Project.ProjectManager` mapping.
- Renamed: `StorageDetailsInquiry.StorageDetail.Site*` and `StorageDetailsByLocationInquiry.*` fields to
  `Qty*` / `WarehouseID` / `LastModifiedDate*` names.
- Removed entities: `SubItemStockItem`, `TrialBalance`, `TrialBalanceDetail`; removed fields
  `Project.BillingAndAllocationSettings.Retainage` (use `Project.Retainage`), `StockItem.SubItems`.

### Default/22.200.001 vs 20.200.001 (both Contract Version 4)

- New entities: the whole **Payroll** family (`DeductionBenefitCode`, `EarningTypeCode`, `EmployeePayrollClass`,
  `EmployeePayrollSettings`, `PayGroup`, `PayPeriod`, `PayrollBatch`, `PayrollUnionLocal`, `PayrollWCCCode`,
  `PTOBank`, `WorkLocation`, `WorkCalendar`, `LaborRate`, their detail entities), commerce stores
  (`BigCommerceStores`, `ShopifyStore`), `InventoryIssue` (+ detail/allocation), `InventoryQuantityAvailable`,
  `MatrixItems`, `TemplateItems`, `SalesTerritory` (+ `CountryDetail`, `StateDetail`), `PurchasingDetail`,
  `SettingsForPR`, `CalendarSettings`, `InventoryFileUrls`.
- New fields/actions include project lifecycle actions (`Project.ActivateProject` / `CancelProject` /
  `CompleteProject` / `HoldProject` / `SuspendProject`, `ProjectTask.*`, `ProjectTemplate.*`,
  `ChangeOrder.HoldChangeOrder` / `RemoveChangeOrderFromHold`, `ProFormaInvoice.HoldProFormaInvoice` /
  `RemoveProFormaInvoiceFromHold`), `Payment.VoidCardPayment` / `AppliedToOrders` / `OrigTransaction` /
  `ExternalRef`, e-commerce item fields (`StockItem.Visibility` / `Availability` / `ExportToExternal` /
  `CustomURL` / `PageTitle` / `MetaDescription` / `SearchKeywords` / `FileURLs`, same on `NonStockItem`),
  `SalesOrder.ExternalOrderOrigin` / `ExternalOrderSource` / `ExternalRefundRef` / `PaymentRef` /
  `WillCall` / `TaxCalcMode` / `DisableAutomaticTaxCalculation`, `SalesOrder.Details.*` purchasing and
  invoice links, `Shipment.Packages.*` dimensions, `ItemWarehouse` reorder settings, `Customer.CreditLimit` /
  `TaxExemptionNumber` / `IsGuestCustomer`.
- Renamed: `ItemWarehouse.OverrideServiceLevelOverride` to `OverrideServiceLevel`; `LaborCostRate.EmployeeID` /
  `ProjectID` / `ProjectTaskID` / `UnionLocalID` to `Employee` / `Project` / `ProjectTask` / `UnionLocal`;
  `ProjectTask.Attribute` to `Attributes`; `SalesOrder.ShippingSettings.Freight` and `Shipment.FreightAmount` to
  `FreightPrice`.
- Removed: `AllocationRule`, `CommonTask`, `ProjectBilling`, `ProjectBillingDetails`, `ProjectBillingRules`;
  `LaborCostRate.*` scalar fields (use `LaborCostRate.Results`); `SalesOrder.Details.PurchasingSettings`;
  `SalesOrder.Relations`; `SalesOrder.SalesOrderAddInvoice`; several `ChangeOrder.RevenueBudget.*` fields.
