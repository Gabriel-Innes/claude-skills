<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# PX.Objects.GL.CashAccountBranch (EntityType)

Label: "Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_CashAccountBranch

# PX.Objects.GL.CASplitBranch (EntityType)

Label: "Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_CASplitBranch

# PX.Objects.GL.Company (EntityType)

Label: "Company"
Singletons: PX_Objects_GL_Company, Company1

PX.Objects.GL.Company.CompanyCD : Edm.String "Company"
PX.Objects.GL.Company.BaseCuryID : Edm.String "Base Currency ID"
PX.Objects.GL.Company.PhoneMask : Edm.String "Phone Mask"
PX.Objects.GL.Company.tstamp : Edm.Binary
PX.Objects.GL.Company.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.GL.Company.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)

# PX.Objects.GL.CurrentBranch (EntityType)

Label: "Current Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_CurrentBranch, CurrentBranch

# PX.Objects.GL.DAC.Organization (EntityType)

Label: "Company"
Key: OrganizationCD
Entity sets: PX_Objects_GL_DAC_Organization, Company2, Organization
Non-filterable, non-selectable: ActualLedgerCD, PrimaryColor, BackgroundColor, LogoNameGetter, LogoNameReportGetter, Included, NoteText, Secured, DeletedDatabaseRecord

PX.Objects.GL.DAC.Organization.OrganizationID : Edm.Int32
PX.Objects.GL.DAC.Organization.OrganizationCD : Edm.String [key] "Company ID"
PX.Objects.GL.DAC.Organization.OrganizationType : Edm.String "Company Type"
PX.Objects.GL.DAC.Organization.FileTaxesByBranches : Edm.Boolean [required] "File Taxes by Branch"
PX.Objects.GL.DAC.Organization.BaseCuryID : Edm.String "Base Currency ID"
PX.Objects.GL.DAC.Organization.ActualLedgerID : Edm.Int32
PX.Objects.GL.DAC.Organization.ActualLedgerCD : Edm.String
PX.Objects.GL.DAC.Organization.Status : Edm.String "Status"
PX.Objects.GL.DAC.Organization.OrganizationName : Edm.String "Company Name"
PX.Objects.GL.DAC.Organization.RoleName : Edm.String "Access Role"
PX.Objects.GL.DAC.Organization.PhoneMask : Edm.String "Phone Mask"
PX.Objects.GL.DAC.Organization.CountryID : Edm.String "Default Country"
PX.Objects.GL.DAC.Organization.OrganizationLocalizationCode : Edm.String "Localization"
PX.Objects.GL.DAC.Organization.CashDiscountBase : Edm.String "Cash Discount Base"
PX.Objects.GL.DAC.Organization.CarrierFacility : Edm.String "Carrier Facility"
PX.Objects.GL.DAC.Organization.OverrideThemeVariables : Edm.Boolean [required] "Override Colors for the Selected Company"
PX.Objects.GL.DAC.Organization.PrimaryColor : Edm.String "Primary Color"
PX.Objects.GL.DAC.Organization.BackgroundColor : Edm.String "Background Color"
PX.Objects.GL.DAC.Organization.BAccountID : Edm.Int32 "BAccountID"
PX.Objects.GL.DAC.Organization.LogoName : Edm.String "Logo File"
PX.Objects.GL.DAC.Organization.LogoNameGetter : Edm.String "Logo File"
PX.Objects.GL.DAC.Organization.LogoNameReport : Edm.String "Report Logo File"
PX.Objects.GL.DAC.Organization.LogoNameReportGetter : Edm.String "Logo File"
PX.Objects.GL.DAC.Organization.TCC : Edm.String "Transmitter Control Code (TCC)"
PX.Objects.GL.DAC.Organization.ForeignEntity : Edm.Boolean "Foreign Entity"
PX.Objects.GL.DAC.Organization.CFSFiler : Edm.Boolean "Combined Federal/State Filer"
PX.Objects.GL.DAC.Organization.FirstName : Edm.String "First Name"
PX.Objects.GL.DAC.Organization.MiddleName : Edm.String "Middle Name"
PX.Objects.GL.DAC.Organization.LastName : Edm.String "Last Name"
PX.Objects.GL.DAC.Organization.CTelNumber : Edm.String "Phone Number"
PX.Objects.GL.DAC.Organization.PhoneType1099 : Edm.String "Phone Number Type"
PX.Objects.GL.DAC.Organization.CEmail : Edm.String "Contact E-mail"
PX.Objects.GL.DAC.Organization.NameControl : Edm.String "Name Control"
PX.Objects.GL.DAC.Organization.Reporting1099 : Edm.Boolean [required] "1099-MISC Reporting Entity"
PX.Objects.GL.DAC.Organization.Reporting1099ByBranches : Edm.Boolean [required] "File 1099-MISC by Branch"
PX.Objects.GL.DAC.Organization.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.DAC.Organization.CreatedByScreenID : Edm.String
PX.Objects.GL.DAC.Organization.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.GL.DAC.Organization.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.DAC.Organization.LastModifiedByScreenID : Edm.String
PX.Objects.GL.DAC.Organization.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.GL.DAC.Organization.tstamp : Edm.Binary
PX.Objects.GL.DAC.Organization.Included : Edm.Boolean "Included"
PX.Objects.GL.DAC.Organization.NoteID : Edm.Guid
PX.Objects.GL.DAC.Organization.NoteText : Edm.String "Note Text"
PX.Objects.GL.DAC.Organization.Secured : Edm.Boolean "Secured"
PX.Objects.GL.DAC.Organization.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.DAC.Organization.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.GL.DAC.Organization.BranchByDunningFeeBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.DAC.Organization.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.DAC.Organization.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.DAC.Organization.RolesByRoleName -> PX.SM.Roles (RoleName=Rolename)
PX.Objects.GL.DAC.Organization.SMPrinterByDefaultPrinterID -> PX.SM.SMPrinter
PX.Objects.GL.DAC.Organization.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.GL.DAC.Organization.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)
PX.Objects.GL.DAC.Organization.LedgerByActualLedgerID -> PX.Objects.GL.Ledger (ActualLedgerID=LedgerID)
PX.Objects.GL.DAC.Organization.LedgerCollection -> Collection(PX.Objects.GL.Ledger)
PX.Objects.GL.DAC.Organization.FinPeriodCollection -> Collection(PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod)
PX.Objects.GL.DAC.Organization.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.Objects.GL.DAC.Organization.FABookPeriodCollection -> Collection(PX.Objects.FA.FABookPeriod)
PX.Objects.GL.DAC.Organization.FABookYearCollection -> Collection(PX.Objects.FA.FABookYear)
PX.Objects.GL.DAC.Organization.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.GL.DAC.Organization.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.GL.DAC.Organization.MISC1099EFileProcessingInfoRawCollection -> Collection(PX.Objects.AP.MISC1099EFileProcessingInfoRaw)
PX.Objects.GL.DAC.Organization.TaxYearCollection -> Collection(PX.Objects.TX.TaxYear)
PX.Objects.GL.DAC.Organization.TaxPeriodCollection -> Collection(PX.Objects.TX.TaxPeriod)
PX.Objects.GL.DAC.Organization.RQBudgetLedgerCollection -> Collection(PX.Objects.RQ.DAC.RQBudgetLedger)
PX.Objects.GL.DAC.Organization.FinYearCollection -> Collection(PX.Objects.GL.FinPeriods.TableDefinition.FinYear)
PX.Objects.GL.DAC.Organization.T4AMasterTableCollection -> Collection(PX.Objects.Localizations.CA.T4AMasterTable)
PX.Objects.GL.DAC.Organization.PRAcaAggregateGroupMemberCollection -> Collection(PX.Objects.PR.PRAcaAggregateGroupMember)
PX.Objects.GL.DAC.Organization.PRAcaCompanyMonthlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyMonthlyInformation)
PX.Objects.GL.DAC.Organization.PRAcaCompanyYearlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyYearlyInformation)
PX.Objects.GL.DAC.Organization.PRAcaEmployeeMonthlyInformationCollection -> Collection(PX.Objects.PR.PRAcaEmployeeMonthlyInformation)
PX.Objects.GL.DAC.Organization.PRPayGroupPeriodCollection -> Collection(PX.Objects.PR.PRPayGroupPeriod)
PX.Objects.GL.DAC.Organization.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.GL.DAC.Organization.PPBillcomFundingAccountCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount)
PX.Objects.GL.DAC.Organization.PPBillcomFundingAccountUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccountUser)
PX.Objects.GL.DAC.Organization.PPBillcomUserCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomUser)
PX.Objects.GL.DAC.Organization.PPExternalSettingCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPExternalSetting)
PX.Objects.GL.DAC.Organization.OrganizationFinPeriodCollection -> Collection(PX.Objects.GL.FinPeriods.OrganizationFinPeriod)
PX.Objects.GL.DAC.Organization.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.GL.DAC.Organization.OrganizationFinYearCollection -> Collection(PX.Objects.GL.FinPeriods.OrganizationFinYear)
PX.Objects.GL.DAC.Organization.OrganizationLedgerLinkCollection -> Collection(PX.Objects.GL.DAC.OrganizationLedgerLink)
PX.Objects.GL.DAC.Organization.AP1099YearCollection -> Collection(PX.Objects.AP.AP1099Year)
PX.Objects.GL.DAC.Organization.AP1099YrCollection -> Collection(PX.Objects.AP.Overrides.APDocumentRelease.AP1099Yr)

# PX.Objects.GL.DAC.OrganizationLedgerLink (EntityType)

Key: LedgerID, OrganizationID
Entity sets: PX_Objects_GL_DAC_OrganizationLedgerLink

PX.Objects.GL.DAC.OrganizationLedgerLink.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.GL.DAC.OrganizationLedgerLink.LedgerID : Edm.Int32 [key] "Ledger"
PX.Objects.GL.DAC.OrganizationLedgerLink.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.GL.DAC.OrganizationLedgerLink.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)

# PX.Objects.GL.DAC.Standalone.OrganizationAlias (EntityType)

Label: "Company"
BaseType: PX.Objects.GL.DAC.Organization
Key: OrganizationCD (inherited from PX.Objects.GL.DAC.Organization)
Entity sets: PX_Objects_GL_DAC_Standalone_OrganizationAlias, Company3, OrganizationAlias

# PX.Objects.GL.FinPeriods.MasterFinPeriod (EntityType)

Key: FinPeriodID
Entity sets: PX_Objects_GL_FinPeriods_MasterFinPeriod
Non-filterable, non-selectable: StartDateUI, EndDateUI, Length, IsAdjustment

PX.Objects.GL.FinPeriods.MasterFinPeriod.FinPeriodID : Edm.String [key] "Financial Period ID"
PX.Objects.GL.FinPeriods.MasterFinPeriod.OrganizationID : Edm.Int32
PX.Objects.GL.FinPeriods.MasterFinPeriod.FinYear : Edm.String
PX.Objects.GL.FinPeriods.MasterFinPeriod.Descr : Edm.String "Description"
PX.Objects.GL.FinPeriods.MasterFinPeriod.PeriodNbr : Edm.String
PX.Objects.GL.FinPeriods.MasterFinPeriod.Status : Edm.String "Status"
PX.Objects.GL.FinPeriods.MasterFinPeriod.Active : Edm.Boolean "Active"
PX.Objects.GL.FinPeriods.MasterFinPeriod.Closed : Edm.Boolean "Closed in GL"
PX.Objects.GL.FinPeriods.MasterFinPeriod.APClosed : Edm.Boolean "Closed in AP"
PX.Objects.GL.FinPeriods.MasterFinPeriod.ARClosed : Edm.Boolean "Closed in AR"
PX.Objects.GL.FinPeriods.MasterFinPeriod.INClosed : Edm.Boolean "Closed in IN"
PX.Objects.GL.FinPeriods.MasterFinPeriod.CAClosed : Edm.Boolean "Closed in CA"
PX.Objects.GL.FinPeriods.MasterFinPeriod.FAClosed : Edm.Boolean "Closed in FA"
PX.Objects.GL.FinPeriods.MasterFinPeriod.StartDateUI : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriods.MasterFinPeriod.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.GL.FinPeriods.MasterFinPeriod.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriods.MasterFinPeriod.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.GL.FinPeriods.MasterFinPeriod.Custom : Edm.Boolean
PX.Objects.GL.FinPeriods.MasterFinPeriod.DateLocked : Edm.Boolean "Date Locked"
PX.Objects.GL.FinPeriods.MasterFinPeriod.FinDate : Edm.DateTimeOffset "Fin. Date"
PX.Objects.GL.FinPeriods.MasterFinPeriod.Length : Edm.Int32 "Length (Days)"
PX.Objects.GL.FinPeriods.MasterFinPeriod.IsAdjustment : Edm.Boolean "Adjustment Period"
PX.Objects.GL.FinPeriods.MasterFinPeriod.tstamp : Edm.Binary
PX.Objects.GL.FinPeriods.MasterFinPeriod.NoteID : Edm.Guid
PX.Objects.GL.FinPeriods.MasterFinPeriod.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.FinPeriods.MasterFinPeriod.CreatedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.MasterFinPeriod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.MasterFinPeriod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.FinPeriods.MasterFinPeriod.LastModifiedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.MasterFinPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.MasterFinPeriod.MasterFinYearByFinYear -> PX.Objects.GL.FinPeriods.MasterFinYear (FinYear=Year)
PX.Objects.GL.FinPeriods.MasterFinPeriod.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.GL.FinPeriods.MasterFinPeriod.FinYearByFinYear -> PX.Objects.GL.FinPeriods.TableDefinition.FinYear (OrganizationID=OrganizationID, FinYear=Year)
PX.Objects.GL.FinPeriods.MasterFinPeriod.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.GL.FinPeriods.MasterFinPeriod.PMHistoryCollection -> Collection(PX.Objects.PM.PMHistory)
PX.Objects.GL.FinPeriods.MasterFinPeriod.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.GL.FinPeriods.MasterFinYear (EntityType)

Key: Year
Entity sets: PX_Objects_GL_FinPeriods_MasterFinYear

PX.Objects.GL.FinPeriods.MasterFinYear.Year : Edm.String [key] "Financial Year"
PX.Objects.GL.FinPeriods.MasterFinYear.OrganizationID : Edm.Int32
PX.Objects.GL.FinPeriods.MasterFinYear.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriods.MasterFinYear.EndDate : Edm.DateTimeOffset "EndDate"
PX.Objects.GL.FinPeriods.MasterFinYear.FinPeriods : Edm.Int16 "Number of Periods"
PX.Objects.GL.FinPeriods.MasterFinYear.CustomPeriods : Edm.Boolean "User-Defined Periods"
PX.Objects.GL.FinPeriods.MasterFinYear.BegFinYearHist : Edm.DateTimeOffset "Financial Year Starts On"
PX.Objects.GL.FinPeriods.MasterFinYear.PeriodsStartDateHist : Edm.DateTimeOffset "Periods Start Date"
PX.Objects.GL.FinPeriods.MasterFinYear.NoteID : Edm.Guid
PX.Objects.GL.FinPeriods.MasterFinYear.tstamp : Edm.Binary
PX.Objects.GL.FinPeriods.MasterFinYear.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.FinPeriods.MasterFinYear.CreatedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.MasterFinYear.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.MasterFinYear.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.FinPeriods.MasterFinYear.LastModifiedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.MasterFinYear.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.MasterFinYear.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.GL.FinPeriods.MasterFinYear.OrganizationFinYearCollection -> Collection(PX.Objects.GL.FinPeriods.OrganizationFinYear)
PX.Objects.GL.FinPeriods.MasterFinYear.MasterFinPeriodCollection -> Collection(PX.Objects.GL.FinPeriods.MasterFinPeriod)
PX.Objects.GL.FinPeriods.MasterFinYear.FinPeriodCollection -> Collection(PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod)

# PX.Objects.GL.FinPeriods.MasterPrevFinPeriodCurrent (ComplexType)


PX.Objects.GL.FinPeriods.MasterPrevFinPeriodCurrent.PrevFinPeriodID : Edm.String

# PX.Objects.GL.FinPeriods.OrganizationFinPeriod (EntityType)

Key: FinPeriodID, OrganizationID
Entity sets: PX_Objects_GL_FinPeriods_OrganizationFinPeriod
Non-filterable, non-selectable: StartDateUI, EndDateUI, Length, IsAdjustment

PX.Objects.GL.FinPeriods.OrganizationFinPeriod.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.FinPeriodID : Edm.String [key] "Financial Period ID"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.MasterFinPeriodID : Edm.String "Master Calendar Period ID"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.FinYear : Edm.String "FinYear"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.Descr : Edm.String "Description"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.PeriodNbr : Edm.String
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.Status : Edm.String "Status"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.Active : Edm.Boolean "Active"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.Closed : Edm.Boolean "Closed in GL"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.APClosed : Edm.Boolean "Closed in AP"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.ARClosed : Edm.Boolean "Closed in AR"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.INClosed : Edm.Boolean "Closed in IN"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.CAClosed : Edm.Boolean "Closed in CA"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.FAClosed : Edm.Boolean "Closed in FA"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.StartDateUI : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.EndDate : Edm.DateTimeOffset "EndDate"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.Custom : Edm.Boolean
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.DateLocked : Edm.Boolean "Date Locked"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.FinDate : Edm.DateTimeOffset "FinDate"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.Length : Edm.Int32 "Length (Days)"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.IsAdjustment : Edm.Boolean "Adjustment Period"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.NoteID : Edm.Guid
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.tstamp : Edm.Binary
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.CreatedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.LastModifiedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.OrganizationFinYearByFinYear -> PX.Objects.GL.FinPeriods.OrganizationFinYear (OrganizationID=OrganizationID, FinYear=Year)
PX.Objects.GL.FinPeriods.OrganizationFinPeriod.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.GL.FinPeriods.OrganizationFinPeriodAlias (EntityType)

BaseType: PX.Objects.GL.FinPeriods.OrganizationFinPeriod
Key: FinPeriodID, OrganizationID (inherited from PX.Objects.GL.FinPeriods.OrganizationFinPeriod)
Entity sets: PX_Objects_GL_FinPeriods_OrganizationFinPeriodAlias

# PX.Objects.GL.FinPeriods.OrganizationFinPeriodCurrent (EntityType)

Label: "Last FinPeriod Current"
Key: FinPeriodID, OrganizationID, PrevFinPeriodID
Entity sets: PX_Objects_GL_FinPeriods_OrganizationFinPeriodCurrent, LastFinPeriodCurrent, OrganizationFinPeriodCurrent

PX.Objects.GL.FinPeriods.OrganizationFinPeriodCurrent.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.GL.FinPeriods.OrganizationFinPeriodCurrent.FinPeriodID : Edm.String [key] "Financial Period ID"
PX.Objects.GL.FinPeriods.OrganizationFinPeriodCurrent.MasterFinPeriodID : Edm.String "Master Calendar Period ID"
PX.Objects.GL.FinPeriods.OrganizationFinPeriodCurrent.PrevFinPeriodID : Edm.String [key]
PX.Objects.GL.FinPeriods.OrganizationFinPeriodCurrent.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.GL.FinPeriods.OrganizationFinPeriodExt (EntityType)

Label: "Last FinPeriod"
Key: FinPeriodID, OrganizationID, PrevFinPeriodID
Entity sets: PX_Objects_GL_FinPeriods_OrganizationFinPeriodExt, LastFinPeriod, OrganizationFinPeriodExt

PX.Objects.GL.FinPeriods.OrganizationFinPeriodExt.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.GL.FinPeriods.OrganizationFinPeriodExt.FinPeriodID : Edm.String [key] "Financial Period ID"
PX.Objects.GL.FinPeriods.OrganizationFinPeriodExt.MasterFinPeriodID : Edm.String "Master Calendar Period ID"
PX.Objects.GL.FinPeriods.OrganizationFinPeriodExt.PrevFinPeriodID : Edm.String [key]
PX.Objects.GL.FinPeriods.OrganizationFinPeriodExt.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.GL.FinPeriods.OrganizationFinPeriodMin (EntityType)

Label: "Min FinPeriod Current"
Key: FinPeriodID, OrganizationID
Entity sets: PX_Objects_GL_FinPeriods_OrganizationFinPeriodMin, MinFinPeriodCurrent, OrganizationFinPeriodMin

PX.Objects.GL.FinPeriods.OrganizationFinPeriodMin.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.GL.FinPeriods.OrganizationFinPeriodMin.FinPeriodID : Edm.String [key] "Financial Period ID"
PX.Objects.GL.FinPeriods.OrganizationFinPeriodMin.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.GL.FinPeriods.OrganizationFinPeriodStatus (EntityType)

BaseType: PX.Objects.GL.FinPeriods.OrganizationFinPeriod
Key: FinPeriodID, OrganizationID (inherited from PX.Objects.GL.FinPeriods.OrganizationFinPeriod)
Entity sets: PX_Objects_GL_FinPeriods_OrganizationFinPeriodStatus

# PX.Objects.GL.FinPeriods.OrganizationFinYear (EntityType)

Label: "Company Financial Period"
Key: OrganizationID, Year
Entity sets: PX_Objects_GL_FinPeriods_OrganizationFinYear, CompanyFinancialPeriod, OrganizationFinYear

PX.Objects.GL.FinPeriods.OrganizationFinYear.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.GL.FinPeriods.OrganizationFinYear.Year : Edm.String [key] "Financial Year"
PX.Objects.GL.FinPeriods.OrganizationFinYear.StartMasterFinPeriodID : Edm.String "Start Master Period ID"
PX.Objects.GL.FinPeriods.OrganizationFinYear.FinPeriods : Edm.Int16 "Number of Periods"
PX.Objects.GL.FinPeriods.OrganizationFinYear.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriods.OrganizationFinYear.EndDate : Edm.DateTimeOffset "EndDate"
PX.Objects.GL.FinPeriods.OrganizationFinYear.NoteID : Edm.Guid
PX.Objects.GL.FinPeriods.OrganizationFinYear.tstamp : Edm.Binary
PX.Objects.GL.FinPeriods.OrganizationFinYear.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.FinPeriods.OrganizationFinYear.CreatedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.OrganizationFinYear.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.OrganizationFinYear.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.FinPeriods.OrganizationFinYear.LastModifiedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.OrganizationFinYear.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.OrganizationFinYear.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.GL.FinPeriods.OrganizationFinYear.MasterFinYearByYear -> PX.Objects.GL.FinPeriods.MasterFinYear (Year=Year)
PX.Objects.GL.FinPeriods.OrganizationFinYear.OrganizationFinPeriodCollection -> Collection(PX.Objects.GL.FinPeriods.OrganizationFinPeriod)

# PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod (EntityType)

Label: "Financial Period"
Key: FinPeriodID, OrganizationID
Entity sets: PX_Objects_GL_FinPeriods_TableDefinition_FinPeriod, FinancialPeriod, FinPeriod
Non-filterable, non-selectable: StartDateUI, EndDateUI, Length, NoteText

PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.OrganizationID : Edm.Int32 [key]
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.FinPeriodID : Edm.String [key] "Financial Period ID"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.MasterFinPeriodID : Edm.String
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.FinYear : Edm.String
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.Descr : Edm.String "Description"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.PeriodNbr : Edm.String
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.Status : Edm.String "Status"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.Active : Edm.Boolean "Active"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.Closed : Edm.Boolean "Closed in GL"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.APClosed : Edm.Boolean [required] "Closed in AP"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.ARClosed : Edm.Boolean [required] "Closed in AR"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.INClosed : Edm.Boolean [required] "Closed in IN"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.CAClosed : Edm.Boolean [required] "Closed in CA"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.FAClosed : Edm.Boolean [required] "Closed in FA"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.StartDateUI : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.EndDate : Edm.DateTimeOffset "EndDate"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.DateLocked : Edm.Boolean "Date Locked"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.Custom : Edm.Boolean
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.FinDate : Edm.DateTimeOffset "Fin. Date"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.Length : Edm.Int32 "Length (Days)"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.IsAdjustment : Edm.Boolean "Adjustment Period"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.tstamp : Edm.Binary
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.NoteID : Edm.Guid
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.NoteText : Edm.String "Note Text"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.CreatedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.LastModifiedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.FinYearByFinYear -> PX.Objects.GL.FinPeriods.TableDefinition.FinYear (OrganizationID=OrganizationID, FinYear=Year)
PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod2 (EntityType)

Label: "Financial Period"
BaseType: PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod
Key: FinPeriodID, OrganizationID (inherited from PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod)
Entity sets: PX_Objects_GL_FinPeriods_TableDefinition_FinPeriod2

# PX.Objects.GL.FinPeriods.TableDefinition.FinYear (EntityType)

Key: OrganizationID, Year
Entity sets: PX_Objects_GL_FinPeriods_TableDefinition_FinYear
Non-filterable, non-selectable: NoteText

PX.Objects.GL.FinPeriods.TableDefinition.FinYear.OrganizationID : Edm.Int32 [key] "Company"
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.Year : Edm.String [key required] "Year"
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.StartDate : Edm.DateTimeOffset [required]
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.EndDate : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.FinPeriods : Edm.Int16 [required]
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.CustomPeriods : Edm.Boolean
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.BegFinYearHist : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.PeriodsStartDateHist : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.StartMasterFinPeriodID : Edm.String
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.NoteID : Edm.Guid
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.NoteText : Edm.String "Note Text"
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.tstamp : Edm.Binary
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.CreatedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.LastModifiedByScreenID : Edm.String
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.GL.FinPeriods.TableDefinition.FinYear.FinPeriodCollection -> Collection(PX.Objects.GL.FinPeriods.TableDefinition.FinPeriod)

# PX.Objects.GL.FinPeriodSetup (EntityType)

Label: "Financial Period Template"
Key: PeriodNbr
Entity sets: PX_Objects_GL_FinPeriodSetup, FinancialPeriodTemplate, FinPeriodSetup
Non-filterable, non-selectable: StartDateUI, EndDateUI, NoteText

PX.Objects.GL.FinPeriodSetup.PeriodNbr : Edm.String [key] "Period Nbr."
PX.Objects.GL.FinPeriodSetup.StartDateUI : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriodSetup.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.GL.FinPeriodSetup.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.FinPeriodSetup.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.GL.FinPeriodSetup.Descr : Edm.String "Description"
PX.Objects.GL.FinPeriodSetup.tstamp : Edm.Binary
PX.Objects.GL.FinPeriodSetup.NoteID : Edm.Guid
PX.Objects.GL.FinPeriodSetup.NoteText : Edm.String "Note Text"
PX.Objects.GL.FinPeriodSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.FinPeriodSetup.CreatedByScreenID : Edm.String
PX.Objects.GL.FinPeriodSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriodSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.FinPeriodSetup.LastModifiedByScreenID : Edm.String
PX.Objects.GL.FinPeriodSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinPeriodSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.FinPeriodSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.GL.FinYearSetup (EntityType)

Label: "Financial Year"
Singletons: PX_Objects_GL_FinYearSetup, FinancialYear, FinYearSetup

PX.Objects.GL.FinYearSetup.FirstFinYear : Edm.String "First Financial Year"
PX.Objects.GL.FinYearSetup.BegFinYear : Edm.DateTimeOffset "Financial Year Starts On"
PX.Objects.GL.FinYearSetup.FinPeriods : Edm.Int16 [required] "Number of Financial Periods"
PX.Objects.GL.FinYearSetup.PeriodLength : Edm.Int16 "Length of Financial Period (days)"
PX.Objects.GL.FinYearSetup.PeriodType : Edm.String "Period Type"
PX.Objects.GL.FinYearSetup.UserDefined : Edm.Boolean "User-Defined Periods"
PX.Objects.GL.FinYearSetup.PeriodsStartDate : Edm.DateTimeOffset "First Period Start Date"
PX.Objects.GL.FinYearSetup.HasAdjustmentPeriod : Edm.Boolean [required] "Has Adjustment Period"
PX.Objects.GL.FinYearSetup.EndYearCalcMethod : Edm.String "Year End Calculation Method"
PX.Objects.GL.FinYearSetup.EndYearDayOfWeek : Edm.Int32 [required] "Periods Start Day of Week"
PX.Objects.GL.FinYearSetup.YearLastDayOfWeek : Edm.Int32 "Day of Week"
PX.Objects.GL.FinYearSetup.tstamp : Edm.Binary
PX.Objects.GL.FinYearSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.FinYearSetup.CreatedByScreenID : Edm.String
PX.Objects.GL.FinYearSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinYearSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.FinYearSetup.LastModifiedByScreenID : Edm.String
PX.Objects.GL.FinYearSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.FinYearSetup.BelongsToNextYear : Edm.Boolean "Belongs to Next Year"
PX.Objects.GL.FinYearSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.FinYearSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.GL.GLAllocation (EntityType)

Label: "Allocation"
Key: GLAllocationID
Entity sets: PX_Objects_GL_GLAllocation, Allocation, GLAllocation
Non-filterable, non-selectable: OrganizationID, AllocLedgerBalanceType, AllocLedgerBaseCuryID, NoteText

PX.Objects.GL.GLAllocation.GLAllocationID : Edm.String [key] "Allocation ID"
PX.Objects.GL.GLAllocation.Descr : Edm.String "Description"
PX.Objects.GL.GLAllocation.Active : Edm.Boolean [required] "Active"
PX.Objects.GL.GLAllocation.StartFinPeriodID : Edm.String "Start Period"
PX.Objects.GL.GLAllocation.EndFinPeriodID : Edm.String "End Period"
PX.Objects.GL.GLAllocation.Recurring : Edm.Boolean [required] "Recurring"
PX.Objects.GL.GLAllocation.AllocMethod : Edm.String "Distribution Method"
PX.Objects.GL.GLAllocation.OrganizationID : Edm.Int32
PX.Objects.GL.GLAllocation.AllocLedgerID : Edm.Int32 "Allocation Ledger"
PX.Objects.GL.GLAllocation.AllocLedgerBalanceType : Edm.String "AllocLedgerBalanceType"
PX.Objects.GL.GLAllocation.AllocLedgerBaseCuryID : Edm.String "AllocLedgerBaseCuryID"
PX.Objects.GL.GLAllocation.SourceLedgerID : Edm.Int32 "Source Ledger"
PX.Objects.GL.GLAllocation.BasisLederID : Edm.Int32 "Base Ledger"
PX.Objects.GL.GLAllocation.SortOrder : Edm.Int16 [required] "Sort Order"
PX.Objects.GL.GLAllocation.NoteID : Edm.Guid
PX.Objects.GL.GLAllocation.NoteText : Edm.String "Note Text"
PX.Objects.GL.GLAllocation.LastRevisionOn : Edm.DateTimeOffset "Last Revision Date"
PX.Objects.GL.GLAllocation.AllocCollectMethod : Edm.String "Allocation Method"
PX.Objects.GL.GLAllocation.AllocateSeparately : Edm.Boolean [required] "Allocate Source Accounts Separately"
PX.Objects.GL.GLAllocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLAllocation.CreatedByScreenID : Edm.String
PX.Objects.GL.GLAllocation.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.GL.GLAllocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLAllocation.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLAllocation.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.GL.GLAllocation.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.GLAllocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLAllocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLAllocation.LedgerByAllocLedgerID -> PX.Objects.GL.Ledger (AllocLedgerID=LedgerID)
PX.Objects.GL.GLAllocation.LedgerBySourceLedgerID -> PX.Objects.GL.Ledger (SourceLedgerID=LedgerID)
PX.Objects.GL.GLAllocation.LedgerByBasisLederID -> PX.Objects.GL.Ledger (BasisLederID=LedgerID)
PX.Objects.GL.GLAllocation.GLAllocationDestinationCollection -> Collection(PX.Objects.GL.GLAllocationDestination)
PX.Objects.GL.GLAllocation.GLAllocationSourceCollection -> Collection(PX.Objects.GL.GLAllocationSource)
PX.Objects.GL.GLAllocation.GLAllocationHistoryCollection -> Collection(PX.Objects.GL.GLAllocationHistory)

# PX.Objects.GL.GLAllocationAccountHistory (EntityType)

Label: "GL Allocation History for Account"
Key: AccountID, BatchNbr, BranchID, Module, SubID
Entity sets: PX_Objects_GL_GLAllocationAccountHistory, GLAllocationHistoryforAccount, GLAllocationAccountHistory

PX.Objects.GL.GLAllocationAccountHistory.Module : Edm.String [key]
PX.Objects.GL.GLAllocationAccountHistory.BatchNbr : Edm.String [key]
PX.Objects.GL.GLAllocationAccountHistory.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.GL.GLAllocationAccountHistory.AccountID : Edm.Int32 [key]
PX.Objects.GL.GLAllocationAccountHistory.SubID : Edm.Int32 [key]
PX.Objects.GL.GLAllocationAccountHistory.AllocatedAmount : Edm.Decimal [required]
PX.Objects.GL.GLAllocationAccountHistory.PriorPeriodsAllocAmount : Edm.Decimal [required]
PX.Objects.GL.GLAllocationAccountHistory.ContrAccontID : Edm.Int32
PX.Objects.GL.GLAllocationAccountHistory.ContrSubID : Edm.Int32
PX.Objects.GL.GLAllocationAccountHistory.SourceLedgerID : Edm.Int32
PX.Objects.GL.GLAllocationAccountHistory.BatchByBatchNbr -> PX.Objects.GL.Batch (Module=Module, BatchNbr=BatchNbr)
PX.Objects.GL.GLAllocationAccountHistory.BatchByModule -> PX.Objects.GL.Batch (BatchNbr=BatchNbr, Module=Module)
PX.Objects.GL.GLAllocationAccountHistory.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLAllocationAccountHistory.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.GL.GLAllocationAccountHistory.AccountByContrAccontID -> PX.Objects.GL.Account (ContrAccontID=AccountID)
PX.Objects.GL.GLAllocationAccountHistory.LedgerBySourceLedgerID -> PX.Objects.GL.Ledger (SourceLedgerID=LedgerID)
PX.Objects.GL.GLAllocationAccountHistory.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)
PX.Objects.GL.GLAllocationAccountHistory.SubByContrSubID -> PX.Objects.GL.Sub (ContrSubID=SubID)

# PX.Objects.GL.GLAllocationDestination (EntityType)

Label: "GL Allocation Destination"
Key: GLAllocationID, LineID
Entity sets: PX_Objects_GL_GLAllocationDestination, GLAllocationDestination

PX.Objects.GL.GLAllocationDestination.GLAllocationID : Edm.String [key] "Allocation ID"
PX.Objects.GL.GLAllocationDestination.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.GL.GLAllocationDestination.AccountCD : Edm.String "Account"
PX.Objects.GL.GLAllocationDestination.BasisAccountCD : Edm.String "Base Account"
PX.Objects.GL.GLAllocationDestination.Weight : Edm.Decimal "Weight/Percent"
PX.Objects.GL.GLAllocationDestination.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLAllocationDestination.CreatedByScreenID : Edm.String
PX.Objects.GL.GLAllocationDestination.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLAllocationDestination.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLAllocationDestination.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLAllocationDestination.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLAllocationDestination.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.GLAllocationDestination.BranchByBasisBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.GLAllocationDestination.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLAllocationDestination.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLAllocationDestination.AccountByAccountCD -> PX.Objects.GL.Account (AccountCD=AccountCD)
PX.Objects.GL.GLAllocationDestination.AccountByBasisAccountCD -> PX.Objects.GL.Account (BasisAccountCD=AccountCD)
PX.Objects.GL.GLAllocationDestination.GLAllocationByGLAllocationID -> PX.Objects.GL.GLAllocation (GLAllocationID=GLAllocationID)
PX.Objects.GL.GLAllocationDestination.SubBySubCD -> PX.Objects.GL.Sub
PX.Objects.GL.GLAllocationDestination.SubByBasisSubCD -> PX.Objects.GL.Sub

# PX.Objects.GL.GLAllocationHistory (EntityType)

Label: "GL Allocation History"
Key: BatchNbr, GLAllocationID, Module
Entity sets: PX_Objects_GL_GLAllocationHistory, GLAllocationHistory

PX.Objects.GL.GLAllocationHistory.GLAllocationID : Edm.String [key]
PX.Objects.GL.GLAllocationHistory.Module : Edm.String [key]
PX.Objects.GL.GLAllocationHistory.BatchNbr : Edm.String [key]
PX.Objects.GL.GLAllocationHistory.BatchByBatchNbr -> PX.Objects.GL.Batch (Module=Module, BatchNbr=BatchNbr)
PX.Objects.GL.GLAllocationHistory.BatchByModule -> PX.Objects.GL.Batch (BatchNbr=BatchNbr, Module=Module)
PX.Objects.GL.GLAllocationHistory.GLAllocationByGLAllocationID -> PX.Objects.GL.GLAllocation (GLAllocationID=GLAllocationID)

# PX.Objects.GL.GLAllocationSource (EntityType)

Label: "GL Allocation Source"
Key: GLAllocationID, LineID
Entity sets: PX_Objects_GL_GLAllocationSource, GLAllocationSource

PX.Objects.GL.GLAllocationSource.GLAllocationID : Edm.String [key] "Allocation ID"
PX.Objects.GL.GLAllocationSource.LineID : Edm.Int32 [key] "Line Nbr."
PX.Objects.GL.GLAllocationSource.AccountCD : Edm.String "Account"
PX.Objects.GL.GLAllocationSource.PercentLimitType : Edm.String "Percent Limit Type"
PX.Objects.GL.GLAllocationSource.LimitAmount : Edm.Decimal "Amount Limit"
PX.Objects.GL.GLAllocationSource.LimitPercent : Edm.Decimal "Percentage Limit"
PX.Objects.GL.GLAllocationSource.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLAllocationSource.CreatedByScreenID : Edm.String
PX.Objects.GL.GLAllocationSource.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLAllocationSource.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLAllocationSource.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLAllocationSource.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLAllocationSource.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.GLAllocationSource.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLAllocationSource.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLAllocationSource.AccountByAccountCD -> PX.Objects.GL.Account (AccountCD=AccountCD)
PX.Objects.GL.GLAllocationSource.AccountByContrAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLAllocationSource.GLAllocationByGLAllocationID -> PX.Objects.GL.GLAllocation (GLAllocationID=GLAllocationID)
PX.Objects.GL.GLAllocationSource.SubBySubCD -> PX.Objects.GL.Sub
PX.Objects.GL.GLAllocationSource.SubByContrSubID -> PX.Objects.GL.Sub

# PX.Objects.GL.GLBudget (EntityType)

Label: "Budget"
Key: BranchID, FinYear, LedgerID
Entity sets: PX_Objects_GL_GLBudget, Budget, GLBudget

PX.Objects.GL.GLBudget.BranchID : Edm.Int32 [key]
PX.Objects.GL.GLBudget.LedgerID : Edm.Int32 [key]
PX.Objects.GL.GLBudget.FinYear : Edm.String [key]
PX.Objects.GL.GLBudget.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLBudget.CreatedByScreenID : Edm.String
PX.Objects.GL.GLBudget.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLBudget.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLBudget.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLBudget.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLBudget.tstamp : Edm.Binary
PX.Objects.GL.GLBudget.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLBudget.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLBudget.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLBudget.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)

# PX.Objects.GL.GLBudgetLine (EntityType)

Label: "Budget Article"
Key: BranchID, FinYear, GroupID, LedgerID
Entity sets: PX_Objects_GL_GLBudgetLine, BudgetArticle, GLBudgetLine
Non-filterable, non-selectable: Comparison, NoteText, SortOrder, IsRolledUp, Secured

PX.Objects.GL.GLBudgetLine.GroupID : Edm.Guid [key] "GroupID"
PX.Objects.GL.GLBudgetLine.ParentGroupID : Edm.Guid "ParentGroupID"
PX.Objects.GL.GLBudgetLine.Rollup : Edm.Boolean [required] "Rollup"
PX.Objects.GL.GLBudgetLine.IsGroup : Edm.Boolean [required] "Node"
PX.Objects.GL.GLBudgetLine.IsPreloaded : Edm.Boolean [required] "Preloaded"
PX.Objects.GL.GLBudgetLine.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.GL.GLBudgetLine.LedgerID : Edm.Int32 [key] "LedgerID"
PX.Objects.GL.GLBudgetLine.FinYear : Edm.String [key] "Financial Year"
PX.Objects.GL.GLBudgetLine.Description : Edm.String "Description"
PX.Objects.GL.GLBudgetLine.Amount : Edm.Decimal [required] "Amount"
PX.Objects.GL.GLBudgetLine.AllocatedAmount : Edm.Decimal [required] "Distributed Amount"
PX.Objects.GL.GLBudgetLine.ReleasedAmount : Edm.Decimal [required] "Released Amount"
PX.Objects.GL.GLBudgetLine.AccountMask : Edm.String "Account Mask"
PX.Objects.GL.GLBudgetLine.SubMask : Edm.String "Subaccount Mask"
PX.Objects.GL.GLBudgetLine.Released : Edm.Boolean [required] "Released"
PX.Objects.GL.GLBudgetLine.WasReleased : Edm.Boolean [required]
PX.Objects.GL.GLBudgetLine.Comparison : Edm.Boolean
PX.Objects.GL.GLBudgetLine.NoteID : Edm.Guid
PX.Objects.GL.GLBudgetLine.NoteText : Edm.String "Note Text"
PX.Objects.GL.GLBudgetLine.tstamp : Edm.Binary
PX.Objects.GL.GLBudgetLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLBudgetLine.CreatedByScreenID : Edm.String
PX.Objects.GL.GLBudgetLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLBudgetLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLBudgetLine.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLBudgetLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLBudgetLine.TreeSortOrder : Edm.Int32 "TreeSortOrder"
PX.Objects.GL.GLBudgetLine.SortOrder : Edm.Int32
PX.Objects.GL.GLBudgetLine.IsRolledUp : Edm.Boolean
PX.Objects.GL.GLBudgetLine.Secured : Edm.Boolean "Secured"
PX.Objects.GL.GLBudgetLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLBudgetLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLBudgetLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLBudgetLine.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLBudgetLine.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLBudgetLine.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.GL.GLBudgetLine.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)

# PX.Objects.GL.GLBudgetLineDetail (EntityType)

Label: "GL Budget Line Detail"
Key: BranchID, FinPeriodID, FinYear, GroupID, LedgerID
Entity sets: PX_Objects_GL_GLBudgetLineDetail, GLBudgetLineDetail

PX.Objects.GL.GLBudgetLineDetail.BranchID : Edm.Int32 [key]
PX.Objects.GL.GLBudgetLineDetail.LedgerID : Edm.Int32 [key]
PX.Objects.GL.GLBudgetLineDetail.FinYear : Edm.String [key]
PX.Objects.GL.GLBudgetLineDetail.GroupID : Edm.Guid [key] "GroupID"
PX.Objects.GL.GLBudgetLineDetail.AccountID : Edm.Int32
PX.Objects.GL.GLBudgetLineDetail.FinPeriodID : Edm.String [key]
PX.Objects.GL.GLBudgetLineDetail.Amount : Edm.Decimal [required] "Budget Amount"
PX.Objects.GL.GLBudgetLineDetail.ReleasedAmount : Edm.Decimal [required] "Released Amount"
PX.Objects.GL.GLBudgetLineDetail.tstamp : Edm.Binary
PX.Objects.GL.GLBudgetLineDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLBudgetLineDetail.CreatedByScreenID : Edm.String
PX.Objects.GL.GLBudgetLineDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLBudgetLineDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLBudgetLineDetail.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLBudgetLineDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLBudgetLineDetail.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLBudgetLineDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLBudgetLineDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLBudgetLineDetail.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.GL.GLBudgetLineDetail.GLBudgetLineByGroupID -> PX.Objects.GL.GLBudgetLine (GroupID=GroupID)
PX.Objects.GL.GLBudgetLineDetail.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLBudgetLineDetail.SubBySubID -> PX.Objects.GL.Sub

# PX.Objects.GL.GLBudgetTree (EntityType)

Label: "GL Budget Tree"
Key: GroupID
Entity sets: PX_Objects_GL_GLBudgetTree, GLBudgetTree
Non-filterable, non-selectable: Secured, Included

PX.Objects.GL.GLBudgetTree.GroupID : Edm.Guid [key] "GroupID"
PX.Objects.GL.GLBudgetTree.ParentGroupID : Edm.Guid "ParentGroupID"
PX.Objects.GL.GLBudgetTree.SortOrder : Edm.Int32 [required] "Sort Order"
PX.Objects.GL.GLBudgetTree.IsGroup : Edm.Boolean [required] "Node"
PX.Objects.GL.GLBudgetTree.Rollup : Edm.Boolean [required] "Rollup"
PX.Objects.GL.GLBudgetTree.Description : Edm.String "Description"
PX.Objects.GL.GLBudgetTree.AccountMask : Edm.String "Account Mask"
PX.Objects.GL.GLBudgetTree.SubMask : Edm.String "Subaccount Mask"
PX.Objects.GL.GLBudgetTree.Secured : Edm.Boolean "Secured"
PX.Objects.GL.GLBudgetTree.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLBudgetTree.CreatedByScreenID : Edm.String
PX.Objects.GL.GLBudgetTree.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLBudgetTree.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLBudgetTree.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLBudgetTree.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLBudgetTree.TStamp : Edm.Binary
PX.Objects.GL.GLBudgetTree.Included : Edm.Boolean "Included"
PX.Objects.GL.GLBudgetTree.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLBudgetTree.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLBudgetTree.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLBudgetTree.GLBudgetTreeByParentGroupID -> PX.Objects.GL.GLBudgetTree (ParentGroupID=GroupID)
PX.Objects.GL.GLBudgetTree.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.GL.GLBudgetTree.GLBudgetTreeCollection -> Collection(PX.Objects.GL.GLBudgetTree)

# PX.Objects.GL.GLConsolAccount (EntityType)

Label: "GL Consolidation Account"
Key: AccountCD
Entity sets: PX_Objects_GL_GLConsolAccount, GLConsolidationAccount, GLConsolAccount

PX.Objects.GL.GLConsolAccount.AccountCD : Edm.String [key] "Account"
PX.Objects.GL.GLConsolAccount.Description : Edm.String
PX.Objects.GL.GLConsolAccount.AccountCollection -> Collection(PX.Objects.GL.Account)

# PX.Objects.GL.GLConsolBranch (EntityType)

Label: "GL Consolidation Branch"
Key: BranchCD, SetupID
Entity sets: PX_Objects_GL_GLConsolBranch, GLConsolidationBranch, GLConsolBranch
Non-filterable, non-selectable: DisplayName

PX.Objects.GL.GLConsolBranch.SetupID : Edm.Int32 [key]
PX.Objects.GL.GLConsolBranch.BranchCD : Edm.String [key] "Branch"
PX.Objects.GL.GLConsolBranch.OrganizationCD : Edm.String "Company"
PX.Objects.GL.GLConsolBranch.LedgerCD : Edm.String "Ledger"
PX.Objects.GL.GLConsolBranch.Description : Edm.String "Name"
PX.Objects.GL.GLConsolBranch.IsOrganization : Edm.Boolean [required]
PX.Objects.GL.GLConsolBranch.DisplayName : Edm.String "Company/Branch"
PX.Objects.GL.GLConsolBranch.GLConsolSetupCollection -> Collection(PX.Objects.GL.GLConsolSetup)

# PX.Objects.GL.GLConsolData (EntityType)

Label: "GL Consolidation Data"
Key: AccountCD, FinPeriodID, MappedValue
Entity sets: PX_Objects_GL_GLConsolData, GLConsolidationData, GLConsolData
Non-filterable, non-selectable: FinPeriodID

PX.Objects.GL.GLConsolData.AccountCD : Edm.String [key] "Account"
PX.Objects.GL.GLConsolData.MappedValue : Edm.String [key] "Mapped Sub."
PX.Objects.GL.GLConsolData.FinPeriodID : Edm.String [key] "Fin. Period"
PX.Objects.GL.GLConsolData.ConsolAmtCredit : Edm.Decimal "Credit Amount"
PX.Objects.GL.GLConsolData.ConsolAmtDebit : Edm.Decimal "Debit Amount"
PX.Objects.GL.GLConsolData.MappedValueLength : Edm.Int32 "Mapped Sub. Length"

# PX.Objects.GL.GLConsolLedger (EntityType)

Label: "GL Consolidation Ledger"
Key: LedgerCD, SetupID
Entity sets: PX_Objects_GL_GLConsolLedger, GLConsolidationLedger, GLConsolLedger

PX.Objects.GL.GLConsolLedger.SetupID : Edm.Int32 [key]
PX.Objects.GL.GLConsolLedger.LedgerCD : Edm.String [key] "Ledger"
PX.Objects.GL.GLConsolLedger.PostInterCompany : Edm.Boolean "Generates Inter-Branch Transactions"
PX.Objects.GL.GLConsolLedger.BalanceType : Edm.String "Balance Type"
PX.Objects.GL.GLConsolLedger.Description : Edm.String "Description"
PX.Objects.GL.GLConsolLedger.GLConsolSetupCollection -> Collection(PX.Objects.GL.GLConsolSetup)

# PX.Objects.GL.GLConsolLedger2 (EntityType)

Key: LedgerCD, SetupID
Entity sets: PX_Objects_GL_GLConsolLedger2

PX.Objects.GL.GLConsolLedger2.SetupID : Edm.Int32 [key]
PX.Objects.GL.GLConsolLedger2.LedgerCD : Edm.String [key]
PX.Objects.GL.GLConsolLedger2.BalanceType : Edm.String
PX.Objects.GL.GLConsolLedger2.GLConsolSetupCollection -> Collection(PX.Objects.GL.GLConsolSetup)

# PX.Objects.GL.GLConsolSetup (EntityType)

Label: "GL Consolidation Setup"
Key: SetupID
Entity sets: PX_Objects_GL_GLConsolSetup, GLConsolidationSetup, GLConsolSetup

PX.Objects.GL.GLConsolSetup.SetupID : Edm.Int32 [key]
PX.Objects.GL.GLConsolSetup.IsActive : Edm.Boolean [required] "Active"
PX.Objects.GL.GLConsolSetup.LedgerId : Edm.Int32 "Consolidation Ledger"
PX.Objects.GL.GLConsolSetup.SegmentValue : Edm.String "Consolidation Segment Value"
PX.Objects.GL.GLConsolSetup.Description : Edm.String "Consolidation Unit"
PX.Objects.GL.GLConsolSetup.Login : Edm.String "Username"
PX.Objects.GL.GLConsolSetup.Password : Edm.String "Password"
PX.Objects.GL.GLConsolSetup.Url : Edm.String "URL"
PX.Objects.GL.GLConsolSetup.SourceLedgerCD : Edm.String "Source Ledger"
PX.Objects.GL.GLConsolSetup.SourceBranchCD : Edm.String "Source Company/Branch"
PX.Objects.GL.GLConsolSetup.PasteFlag : Edm.Boolean "Paste Segment Value"
PX.Objects.GL.GLConsolSetup.LastPostPeriod : Edm.String "Last Post Period"
PX.Objects.GL.GLConsolSetup.StartPeriod : Edm.String "Start Period"
PX.Objects.GL.GLConsolSetup.EndPeriod : Edm.String "End Period"
PX.Objects.GL.GLConsolSetup.LastConsDate : Edm.DateTimeOffset "Last Consolidation Date"
PX.Objects.GL.GLConsolSetup.BypassAccountSubValidation : Edm.Boolean [required] "Bypass Account/Sub Validation"
PX.Objects.GL.GLConsolSetup.HttpClientTimeout : Edm.Int32
PX.Objects.GL.GLConsolSetup.ProcessTimeLimit : Edm.Int32 [required] "Process Time Limit"
PX.Objects.GL.GLConsolSetup.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.GLConsolSetup.SegmentValueBySegmentValue -> PX.Objects.CS.SegmentValue (SegmentValue=Value)
PX.Objects.GL.GLConsolSetup.LedgerByLedgerId -> PX.Objects.GL.Ledger (LedgerId=LedgerID)
PX.Objects.GL.GLConsolSetup.GLConsolLedgerBySetupID -> PX.Objects.GL.GLConsolLedger (SourceLedgerCD=LedgerCD, SetupID=SetupID)
PX.Objects.GL.GLConsolSetup.GLConsolBranchBySetupID -> PX.Objects.GL.GLConsolBranch (SourceBranchCD=BranchCD, SetupID=SetupID)

# PX.Objects.GL.GLDocBatch (EntityType)

Label: "GL Document Batch"
Key: BatchNbr, Module
Entity sets: PX_Objects_GL_GLDocBatch, GLDocumentBatch, GLDocBatch
Non-filterable, non-selectable: NoteText, CuryRate, CuryViewState

PX.Objects.GL.GLDocBatch.Module : Edm.String [key required] "Module"
PX.Objects.GL.GLDocBatch.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.GL.GLDocBatch.LedgerID : Edm.Int32 "Ledger"
PX.Objects.GL.GLDocBatch.DateEntered : Edm.DateTimeOffset "Transaction Date"
PX.Objects.GL.GLDocBatch.FinPeriodID : Edm.String "Post Period"
PX.Objects.GL.GLDocBatch.BatchType : Edm.String "Type"
PX.Objects.GL.GLDocBatch.Status : Edm.String "Status"
PX.Objects.GL.GLDocBatch.CuryDebitTotal : Edm.Decimal "Debit Total"
PX.Objects.GL.GLDocBatch.CuryCreditTotal : Edm.Decimal "Credit Total"
PX.Objects.GL.GLDocBatch.CuryControlTotal : Edm.Decimal "Control Total"
PX.Objects.GL.GLDocBatch.DebitTotal : Edm.Decimal
PX.Objects.GL.GLDocBatch.CreditTotal : Edm.Decimal
PX.Objects.GL.GLDocBatch.ControlTotal : Edm.Decimal "Control Total"
PX.Objects.GL.GLDocBatch.CuryInfoID : Edm.Int64
PX.Objects.GL.GLDocBatch.OrigModule : Edm.String
PX.Objects.GL.GLDocBatch.OrigBatchNbr : Edm.String "Orig. Batch Number"
PX.Objects.GL.GLDocBatch.Released : Edm.Boolean
PX.Objects.GL.GLDocBatch.Posted : Edm.Boolean
PX.Objects.GL.GLDocBatch.TranPeriodID : Edm.String
PX.Objects.GL.GLDocBatch.LineCntr : Edm.Int32 [required]
PX.Objects.GL.GLDocBatch.CuryID : Edm.String "Currency"
PX.Objects.GL.GLDocBatch.NoteID : Edm.Guid
PX.Objects.GL.GLDocBatch.NoteText : Edm.String "Note Text"
PX.Objects.GL.GLDocBatch.tstamp : Edm.Binary
PX.Objects.GL.GLDocBatch.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLDocBatch.CreatedByScreenID : Edm.String
PX.Objects.GL.GLDocBatch.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.GL.GLDocBatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLDocBatch.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLDocBatch.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.GL.GLDocBatch.Hold : Edm.Boolean [required] "Hold"
PX.Objects.GL.GLDocBatch.Voided : Edm.Boolean [required]
PX.Objects.GL.GLDocBatch.Description : Edm.String "Description"
PX.Objects.GL.GLDocBatch.CuryRate : Edm.Decimal
PX.Objects.GL.GLDocBatch.CuryViewState : Edm.Boolean
PX.Objects.GL.GLDocBatch.BatchByOrigBatchNbr -> PX.Objects.GL.Batch (OrigModule=Module, OrigBatchNbr=BatchNbr)
PX.Objects.GL.GLDocBatch.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.GLDocBatch.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.GL.GLDocBatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLDocBatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLDocBatch.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.GL.GLDocBatch.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLDocBatch.GLTaxCollection -> Collection(PX.Objects.GL.GLTax)
PX.Objects.GL.GLDocBatch.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)

# PX.Objects.GL.GLHistory (EntityType)

Label: "GL History"
Key: AccountID, BranchID, FinPeriodID, LedgerID, SubID
Entity sets: PX_Objects_GL_GLHistory, GLHistory
Non-filterable, non-selectable: FinFlag, REFlag, PtdCredit, PtdDebit, YtdBalance, BegBalance, PtdRevalued, CuryPtdCredit, CuryPtdDebit, CuryYtdBalance, CuryBegBalance

PX.Objects.GL.GLHistory.LedgerID : Edm.Int32 [key] "Ledger"
PX.Objects.GL.GLHistory.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.GL.GLHistory.AccountID : Edm.Int32 [key] "Account"
PX.Objects.GL.GLHistory.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.GL.GLHistory.BalanceType : Edm.String "Balance Type"
PX.Objects.GL.GLHistory.CuryID : Edm.String
PX.Objects.GL.GLHistory.FinPtdCredit : Edm.Decimal [required] "Fin. PTD Credit"
PX.Objects.GL.GLHistory.FinPtdDebit : Edm.Decimal [required] "Fin. PTD Debit"
PX.Objects.GL.GLHistory.FinYtdBalance : Edm.Decimal [required] "Fin. YTD Balance"
PX.Objects.GL.GLHistory.FinBegBalance : Edm.Decimal [required] "Fin. Begining Balance"
PX.Objects.GL.GLHistory.FinPtdRevalued : Edm.Decimal [required]
PX.Objects.GL.GLHistory.TranPtdCredit : Edm.Decimal [required]
PX.Objects.GL.GLHistory.TranPtdDebit : Edm.Decimal [required]
PX.Objects.GL.GLHistory.TranYtdBalance : Edm.Decimal [required]
PX.Objects.GL.GLHistory.TranBegBalance : Edm.Decimal [required]
PX.Objects.GL.GLHistory.CuryFinPtdCredit : Edm.Decimal [required]
PX.Objects.GL.GLHistory.CuryFinPtdDebit : Edm.Decimal [required]
PX.Objects.GL.GLHistory.CuryFinYtdBalance : Edm.Decimal [required] "CuryFinYtdBalance"
PX.Objects.GL.GLHistory.CuryFinBegBalance : Edm.Decimal [required] "CuryFinBegBalance"
PX.Objects.GL.GLHistory.CuryTranPtdCredit : Edm.Decimal [required]
PX.Objects.GL.GLHistory.CuryTranPtdDebit : Edm.Decimal [required]
PX.Objects.GL.GLHistory.CuryTranYtdBalance : Edm.Decimal [required]
PX.Objects.GL.GLHistory.CuryTranBegBalance : Edm.Decimal [required]
PX.Objects.GL.GLHistory.FinFlag : Edm.Boolean
PX.Objects.GL.GLHistory.REFlag : Edm.Boolean
PX.Objects.GL.GLHistory.PtdCredit : Edm.Decimal
PX.Objects.GL.GLHistory.PtdDebit : Edm.Decimal
PX.Objects.GL.GLHistory.YtdBalance : Edm.Decimal
PX.Objects.GL.GLHistory.BegBalance : Edm.Decimal
PX.Objects.GL.GLHistory.PtdRevalued : Edm.Decimal
PX.Objects.GL.GLHistory.CuryPtdCredit : Edm.Decimal
PX.Objects.GL.GLHistory.CuryPtdDebit : Edm.Decimal
PX.Objects.GL.GLHistory.CuryYtdBalance : Edm.Decimal
PX.Objects.GL.GLHistory.CuryBegBalance : Edm.Decimal
PX.Objects.GL.GLHistory.tstamp : Edm.Binary
PX.Objects.GL.GLHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLHistory.FinPeriodID : Edm.String [key] "Financial Period"
PX.Objects.GL.GLHistory.FinYear : Edm.String
PX.Objects.GL.GLHistory.DetDeleted : Edm.Boolean [required]
PX.Objects.GL.GLHistory.AllocPtdBalance : Edm.Decimal [required]
PX.Objects.GL.GLHistory.AllocBegBalance : Edm.Decimal [required]
PX.Objects.GL.GLHistory.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLHistory.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.GL.GLHistory.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.GL.GLHistory.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLHistory.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.GL.GLHistoryByCurrentPeriod (EntityType)

Label: "GL History by Period"
Key: AccountID, BranchID, FinPeriodID, LedgerID, SubID
Entity sets: PX_Objects_GL_GLHistoryByCurrentPeriod, GLHistorybyPeriod1, GLHistoryByCurrentPeriod
Non-filterable, non-selectable: FinYear

PX.Objects.GL.GLHistoryByCurrentPeriod.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.GL.GLHistoryByCurrentPeriod.LedgerID : Edm.Int32 [key] "Ledger"
PX.Objects.GL.GLHistoryByCurrentPeriod.AccountID : Edm.Int32 [key] "Account"
PX.Objects.GL.GLHistoryByCurrentPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.GL.GLHistoryByCurrentPeriod.LastActivityPeriod : Edm.String "Last Activity Period"
PX.Objects.GL.GLHistoryByCurrentPeriod.FinPeriodID : Edm.String [key] "Financial Period"
PX.Objects.GL.GLHistoryByCurrentPeriod.FinYear : Edm.String
PX.Objects.GL.GLHistoryByCurrentPeriod.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLHistoryByCurrentPeriod.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.GL.GLHistoryByCurrentPeriod.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLHistoryByCurrentPeriod.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.GL.GLHistoryByPeriod (EntityType)

Label: "GL History by Period"
Key: AccountID, BranchID, FinPeriodID, LedgerID, SubID
Entity sets: PX_Objects_GL_GLHistoryByPeriod, GLHistorybyPeriod2
Non-filterable, non-selectable: FinYear

PX.Objects.GL.GLHistoryByPeriod.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.GL.GLHistoryByPeriod.LedgerID : Edm.Int32 [key] "Ledger"
PX.Objects.GL.GLHistoryByPeriod.AccountID : Edm.Int32 [key] "Account"
PX.Objects.GL.GLHistoryByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.GL.GLHistoryByPeriod.LastActivityPeriod : Edm.String "Last Activity Period"
PX.Objects.GL.GLHistoryByPeriod.FinPeriodID : Edm.String [key] "Financial Period"
PX.Objects.GL.GLHistoryByPeriod.FinYear : Edm.String
PX.Objects.GL.GLHistoryByPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLHistoryByPeriod.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLHistoryByPeriod.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.GL.GLHistoryByPeriod.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLHistoryByPeriod.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.GL.GLHistoryByPeriodCurrent (EntityType)

Label: "GL History by Period"
Key: AccountID, BranchID, FinPeriodID, LedgerID, SubID
Entity sets: PX_Objects_GL_GLHistoryByPeriodCurrent, GLHistorybyPeriod3, GLHistoryByPeriodCurrent
Non-filterable, non-selectable: FinYear

PX.Objects.GL.GLHistoryByPeriodCurrent.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.GL.GLHistoryByPeriodCurrent.LedgerID : Edm.Int32 [key] "Ledger"
PX.Objects.GL.GLHistoryByPeriodCurrent.AccountID : Edm.Int32 [key] "Account"
PX.Objects.GL.GLHistoryByPeriodCurrent.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.GL.GLHistoryByPeriodCurrent.LastActivityPeriod : Edm.String "Last Activity Period"
PX.Objects.GL.GLHistoryByPeriodCurrent.FinPeriodID : Edm.String [key] "Financial Period"
PX.Objects.GL.GLHistoryByPeriodCurrent.FinYear : Edm.String
PX.Objects.GL.GLHistoryByPeriodCurrent.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLHistoryByPeriodCurrent.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)

# PX.Objects.GL.GLHistoryByPeriodMasterCurrent (EntityType)

Label: "GL History by Period"
Key: AccountID, BranchID, FinPeriodID, LedgerID, SubID
Entity sets: PX_Objects_GL_GLHistoryByPeriodMasterCurrent, GLHistorybyPeriod4, GLHistoryByPeriodMasterCurrent
Non-filterable, non-selectable: FinYear

PX.Objects.GL.GLHistoryByPeriodMasterCurrent.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.GL.GLHistoryByPeriodMasterCurrent.LedgerID : Edm.Int32 [key] "Ledger"
PX.Objects.GL.GLHistoryByPeriodMasterCurrent.AccountID : Edm.Int32 [key] "Account"
PX.Objects.GL.GLHistoryByPeriodMasterCurrent.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.GL.GLHistoryByPeriodMasterCurrent.LastActivityPeriod : Edm.String "Last Activity Period"
PX.Objects.GL.GLHistoryByPeriodMasterCurrent.FinPeriodID : Edm.String [key] "Financial Period"
PX.Objects.GL.GLHistoryByPeriodMasterCurrent.FinYear : Edm.String
PX.Objects.GL.GLHistoryByPeriodMasterCurrent.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLHistoryByPeriodMasterCurrent.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)

# PX.Objects.GL.GLHistoryLastRevaluation (EntityType)

Key: AccountID, BranchID, LedgerID, SubID
Entity sets: PX_Objects_GL_GLHistoryLastRevaluation

PX.Objects.GL.GLHistoryLastRevaluation.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.GL.GLHistoryLastRevaluation.LedgerID : Edm.Int32 [key] "Ledger"
PX.Objects.GL.GLHistoryLastRevaluation.AccountID : Edm.Int32 [key] "Account"
PX.Objects.GL.GLHistoryLastRevaluation.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.GL.GLHistoryLastRevaluation.LastActivityPeriod : Edm.String "Last Activity Period"
PX.Objects.GL.GLHistoryLastRevaluation.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLHistoryLastRevaluation.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.GL.GLHistoryLastRevaluation.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLHistoryLastRevaluation.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.GL.GLHistorySummary (EntityType)

Label: "GLHistory Summary"
Key: AccountID, BranchID, LedgerID, SubID
Entity sets: PX_Objects_GL_GLHistorySummary, GLHistorySummary

PX.Objects.GL.GLHistorySummary.LedgerID : Edm.Int32 [key]
PX.Objects.GL.GLHistorySummary.BranchID : Edm.Int32 [key]
PX.Objects.GL.GLHistorySummary.AccountID : Edm.Int32 [key]
PX.Objects.GL.GLHistorySummary.SubID : Edm.Int32 [key]
PX.Objects.GL.GLHistorySummary.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLHistorySummary.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.GL.GLHistorySummary.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLHistorySummary.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.GL.GLSetup (EntityType)

Label: "General Ledger Preferences"
Singletons: PX_Objects_GL_GLSetup, GeneralLedgerPreferences, GLSetup

PX.Objects.GL.GLSetup.AutoRevOption : Edm.String "Generate Reversing Entries"
PX.Objects.GL.GLSetup.AutoRevEntry : Edm.Boolean [required] "Create Negative Entries on Reversal"
PX.Objects.GL.GLSetup.AutoPostOption : Edm.Boolean [required] "Automatically Post on Release"
PX.Objects.GL.GLSetup.COAOrder : Edm.Int16 [required] "Chart of Accounts Order"
PX.Objects.GL.GLSetup.RequireControlTotal : Edm.Boolean [required] "Validate Batch Control Totals on Entry"
PX.Objects.GL.GLSetup.RequireRefNbrForTaxEntry : Edm.Boolean [required] "Require Ref. Numbers for GL Documents with Taxes"
PX.Objects.GL.GLSetup.PostClosedPeriods : Edm.Boolean [required] "Allow Posting to Closed Periods"
PX.Objects.GL.GLSetup.RestrictAccessToClosedPeriods : Edm.Boolean [required] "Restrict Access to Closed Periods"
PX.Objects.GL.GLSetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.GL.GLSetup.DocBatchNumberingID : Edm.String "Document Batch Numbering Sequence"
PX.Objects.GL.GLSetup.TBImportNumberingID : Edm.String "Import Numbering Sequence"
PX.Objects.GL.GLSetup.AllocationNumberingID : Edm.String "Allocation Numbering Sequence"
PX.Objects.GL.GLSetup.ScheduleNumberingID : Edm.String "Schedule Numbering Sequence"
PX.Objects.GL.GLSetup.tstamp : Edm.Binary
PX.Objects.GL.GLSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLSetup.CreatedByScreenID : Edm.String
PX.Objects.GL.GLSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLSetup.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLSetup.HoldEntry : Edm.Boolean [required] "Hold Batches on Entry"
PX.Objects.GL.GLSetup.VouchersHoldEntry : Edm.Boolean [required] "Hold Vouchers on Entry"
PX.Objects.GL.GLSetup.ConsolSegmentId : Edm.Int16 "Consolidation Segment Number"
PX.Objects.GL.GLSetup.PerRetainTran : Edm.Int16 [required] "Keep Transactions for"
PX.Objects.GL.GLSetup.TrialBalanceSign : Edm.String "Sign of the Trial Balance"
PX.Objects.GL.GLSetup.ReuseRefNbrsInVouchers : Edm.Boolean [required] "Reuse Ref. Numbers in Journal Vouchers"
PX.Objects.GL.GLSetup.ConsolidatedPosting : Edm.Boolean [required] "Generate Consolidated Batches"
PX.Objects.GL.GLSetup.AutoReleaseReclassBatch : Edm.Boolean [required] "Automatically Release Reclassification Batches"
PX.Objects.GL.GLSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLSetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.GL.GLSetup.NumberingByDocBatchNumberingID -> PX.Objects.CS.Numbering (DocBatchNumberingID=NumberingID)
PX.Objects.GL.GLSetup.NumberingByTBImportNumberingID -> PX.Objects.CS.Numbering (TBImportNumberingID=NumberingID)
PX.Objects.GL.GLSetup.NumberingByAllocationNumberingID -> PX.Objects.CS.Numbering (AllocationNumberingID=NumberingID)
PX.Objects.GL.GLSetup.NumberingByScheduleNumberingID -> PX.Objects.CS.Numbering (ScheduleNumberingID=NumberingID)
PX.Objects.GL.GLSetup.SegmentByConsolSegmentId -> PX.Objects.CS.Segment (ConsolSegmentId=SegmentID)
PX.Objects.GL.GLSetup.AccountByYtdNetIncAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLSetup.AccountByRetEarnAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLSetup.SubByDefaultSubID -> PX.Objects.GL.Sub

# PX.Objects.GL.GLSetupApproval (EntityType)

Label: "GL Approval Preferences"
Key: ApprovalID
Entity sets: PX_Objects_GL_GLSetupApproval, GLApprovalPreferences, GLSetupApproval

PX.Objects.GL.GLSetupApproval.BatchType : Edm.String "Type"
PX.Objects.GL.GLSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.GL.GLSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.GL.GLSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.GL.GLSetupApproval.IsActive : Edm.Boolean [required] "Active"
PX.Objects.GL.GLSetupApproval.tstamp : Edm.Binary
PX.Objects.GL.GLSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.GL.GLSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.GL.GLSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.GL.GLTax (EntityType)

Label: "GL Tax Detail"
Key: BatchNbr, DetailType, LineNbr, Module, TaxID
Entity sets: PX_Objects_GL_GLTax, GLTaxDetail, GLTax
Non-filterable, non-selectable: NonDeductibleTaxRate, CuryID, CuryRate, CuryViewState

PX.Objects.GL.GLTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.GL.GLTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.GL.GLTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.GL.GLTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLTax.CreatedByScreenID : Edm.String
PX.Objects.GL.GLTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLTax.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLTax.Module : Edm.String [key] "Module"
PX.Objects.GL.GLTax.BatchNbr : Edm.String [key] "Reference Nbr."
PX.Objects.GL.GLTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.GL.GLTax.DetailType : Edm.Int16 [key required] "Tax Detail Type"
PX.Objects.GL.GLTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.GL.GLTax.CuryInfoID : Edm.Int64
PX.Objects.GL.GLTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.GL.GLTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.GL.GLTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.GL.GLTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.GL.GLTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.GL.GLTax.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.GL.GLTax.CuryID : Edm.String "Currency"
PX.Objects.GL.GLTax.CuryRate : Edm.Decimal
PX.Objects.GL.GLTax.CuryViewState : Edm.Boolean
PX.Objects.GL.GLTax.GLTranDocByLineNbr -> PX.Objects.GL.GLTranDoc (Module=Module, BatchNbr=BatchNbr, LineNbr=LineNbr)
PX.Objects.GL.GLTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.GL.GLTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.GL.GLTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.GL.GLTax.GLDocBatchByBatchNbr -> PX.Objects.GL.GLDocBatch (Module=Module, BatchNbr=BatchNbr)

# PX.Objects.GL.GLTaxTran (EntityType)

Label: "GL Tax Transaction"
BaseType: PX.Objects.GL.GLTax
Key: BatchNbr, DetailType, LineNbr, Module, TaxID (inherited from PX.Objects.GL.GLTax)
Entity sets: PX_Objects_GL_GLTaxTran, GLTaxTransaction, GLTaxTran

# PX.Objects.GL.GLTran (EntityType)

Label: "GL Transaction"
Key: BatchNbr, LineNbr, Module
Entity sets: PX_Objects_GL_GLTran, GLTransaction, GLTran
Non-filterable, non-selectable: IncludedInReclassHistory, ZeroPost, PostYear, TranYear, NextPostYear, NextTranYear, LedgerBalanceType, AccountRequireUnits, NoteText, SkipNormalizeAmounts, MLFinPeriodID, CuryID, CuryRate, CuryViewState

PX.Objects.GL.GLTran.IncludedInReclassHistory : Edm.Boolean "Included in Reclass. History"
PX.Objects.GL.GLTran.BranchID : Edm.Int32 "Branch"
PX.Objects.GL.GLTran.Module : Edm.String [key] "Module"
PX.Objects.GL.GLTran.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.GL.GLTran.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.GL.GLTran.LedgerID : Edm.Int32
PX.Objects.GL.GLTran.ProjectID : Edm.Int32 "Project"
PX.Objects.GL.GLTran.IsNonPM : Edm.Boolean [required]
PX.Objects.GL.GLTran.RefNbr : Edm.String "Ref. Number"
PX.Objects.GL.GLTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.GL.GLTran.UOM : Edm.String "UOM"
PX.Objects.GL.GLTran.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.GL.GLTran.DebitAmt : Edm.Decimal
PX.Objects.GL.GLTran.CreditAmt : Edm.Decimal
PX.Objects.GL.GLTran.CuryInfoID : Edm.Int64
PX.Objects.GL.GLTran.CuryDebitAmt : Edm.Decimal "Debit Amount"
PX.Objects.GL.GLTran.CuryCreditAmt : Edm.Decimal "Credit Amount"
PX.Objects.GL.GLTran.Released : Edm.Boolean
PX.Objects.GL.GLTran.Posted : Edm.Boolean
PX.Objects.GL.GLTran.IsInterCompany : Edm.Boolean [required]
PX.Objects.GL.GLTran.SummPost : Edm.Boolean [required]
PX.Objects.GL.GLTran.ZeroPost : Edm.Boolean
PX.Objects.GL.GLTran.OrigModule : Edm.String "Orig. Module"
PX.Objects.GL.GLTran.OrigBatchNbr : Edm.String "Orig. Batch Nbr."
PX.Objects.GL.GLTran.OrigLineNbr : Edm.Int32 "Orig. Line Nbr."
PX.Objects.GL.GLTran.TranID : Edm.Int32
PX.Objects.GL.GLTran.TranType : Edm.String
PX.Objects.GL.GLTran.TranClass : Edm.String
PX.Objects.GL.GLTran.TranDesc : Edm.String "Transaction Description"
PX.Objects.GL.GLTran.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.GL.GLTran.TranLineNbr : Edm.Int32
PX.Objects.GL.GLTran.ReferenceID : Edm.Int32 "Customer/Vendor"
PX.Objects.GL.GLTran.FinPeriodID : Edm.String "Period ID"
PX.Objects.GL.GLTran.TranPeriodID : Edm.String "Master Period ID"
PX.Objects.GL.GLTran.PostYear : Edm.String
PX.Objects.GL.GLTran.TranYear : Edm.String
PX.Objects.GL.GLTran.NextPostYear : Edm.String
PX.Objects.GL.GLTran.NextTranYear : Edm.String
PX.Objects.GL.GLTran.CATranID : Edm.Int64 "CATranID"
PX.Objects.GL.GLTran.OrigPMTranID : Edm.Int64
PX.Objects.GL.GLTran.LedgerBalanceType : Edm.String
PX.Objects.GL.GLTran.AccountRequireUnits : Edm.Boolean
PX.Objects.GL.GLTran.TaxID : Edm.String "Tax ID"
PX.Objects.GL.GLTran.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.GL.GLTran.NoteID : Edm.Guid
PX.Objects.GL.GLTran.NoteText : Edm.String "Note Text"
PX.Objects.GL.GLTran.ReclassificationProhibited : Edm.Boolean [required]
PX.Objects.GL.GLTran.ReclassBatchModule : Edm.String "Reclass. Batch Module"
PX.Objects.GL.GLTran.ReclassBatchNbr : Edm.String "Reclass. Batch Number"
PX.Objects.GL.GLTran.IsReclassReverse : Edm.Boolean [required]
PX.Objects.GL.GLTran.ReclassType : Edm.String "Reclassification Type"
PX.Objects.GL.GLTran.CuryReclassRemainingAmt : Edm.Decimal [required] "Remaining Reclass. Amount"
PX.Objects.GL.GLTran.ReclassRemainingAmt : Edm.Decimal [required]
PX.Objects.GL.GLTran.Reclassified : Edm.Boolean [required]
PX.Objects.GL.GLTran.ReclassOrigTranDate : Edm.DateTimeOffset
PX.Objects.GL.GLTran.ReclassSourceTranModule : Edm.String
PX.Objects.GL.GLTran.ReclassSourceTranBatchNbr : Edm.String
PX.Objects.GL.GLTran.ReclassSourceTranLineNbr : Edm.Int32
PX.Objects.GL.GLTran.ReclassSeqNbr : Edm.Int32 "Reclass. Sequence Nbr."
PX.Objects.GL.GLTran.ReclassTotalCount : Edm.Int32
PX.Objects.GL.GLTran.ReclassReleasedCount : Edm.Int32
PX.Objects.GL.GLTran.tstamp : Edm.Binary
PX.Objects.GL.GLTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLTran.CreatedByScreenID : Edm.String
PX.Objects.GL.GLTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLTran.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLTran.SkipNormalizeAmounts : Edm.Boolean
PX.Objects.GL.GLTran.MLFinPeriodID : Edm.String
PX.Objects.GL.GLTran.CuryID : Edm.String "Currency"
PX.Objects.GL.GLTran.CuryRate : Edm.Decimal
PX.Objects.GL.GLTran.CuryViewState : Edm.Boolean
PX.Objects.GL.GLTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.GL.GLTran.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.GL.GLTran.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.GL.GLTran.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.GL.GLTran.BatchByBatchNbr -> PX.Objects.GL.Batch (Module=Module, BatchNbr=BatchNbr)
PX.Objects.GL.GLTran.CATranByCATranID -> PX.Objects.CA.CATran (CATranID=TranID)
PX.Objects.GL.GLTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.GL.GLTran.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.GL.GLTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLTran.TaxBySubID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.GL.GLTran.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.GL.GLTran.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.GL.GLTran.INUnitByUOM -> PX.Objects.IN.INUnit (UOM=FromUnit)
PX.Objects.GL.GLTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLTran.AccountByOrigAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLTran.GLTranByOrigLineNbr -> PX.Objects.GL.GLTran (OrigModule=Module, OrigBatchNbr=BatchNbr, OrigLineNbr=LineNbr)
PX.Objects.GL.GLTran.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.GL.GLTran.SubByOrigSubID -> PX.Objects.GL.Sub
PX.Objects.GL.GLTran.GLTranCollection -> Collection(PX.Objects.GL.GLTran)

# PX.Objects.GL.GLTranCode (EntityType)

Label: "GL Transaction Code"
Key: Module, TranType
Entity sets: PX_Objects_GL_GLTranCode, GLTransactionCode, GLTranCode

PX.Objects.GL.GLTranCode.Module : Edm.String [key] "Module"
PX.Objects.GL.GLTranCode.TranType : Edm.String [key] "Module Tran. Type"
PX.Objects.GL.GLTranCode.TranCode : Edm.String "Unique Tran. Code"
PX.Objects.GL.GLTranCode.Descr : Edm.String "Description"
PX.Objects.GL.GLTranCode.Active : Edm.Boolean [required] "Active"
PX.Objects.GL.GLTranCode.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)

# PX.Objects.GL.GLTranDoc (EntityType)

Label: "Journal Voucher"
Key: BatchNbr, LineNbr, Module
Entity sets: PX_Objects_GL_GLTranDoc, JournalVoucher, GLTranDoc
Non-filterable, non-selectable: ImportRefNbr, LedgerBalanceType, NoteText, CuryBalanceAmt, GroupTranID, CashAccountID, CuryDocTotal, DocTotal, CuryTaxTotal, CuryUnappliedBal, UnappliedBal, CuryDiscBal, DiscBal, CuryWhTaxBal, WhTaxBal, NeedsDebitCashAccount, IsARCustomerCashAccount, NeedsCreditCashAccount, NeedTaskValidation, CuryRate, CuryViewState

PX.Objects.GL.GLTranDoc.BranchID : Edm.Int32 "Branch"
PX.Objects.GL.GLTranDoc.Module : Edm.String [key] "Batch Module"
PX.Objects.GL.GLTranDoc.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.GL.GLTranDoc.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.GL.GLTranDoc.ImportRefNbr : Edm.String
PX.Objects.GL.GLTranDoc.LedgerID : Edm.Int32
PX.Objects.GL.GLTranDoc.ParentLineNbr : Edm.Int32 "Parent Line Nbr."
PX.Objects.GL.GLTranDoc.Split : Edm.Boolean [required] "Split"
PX.Objects.GL.GLTranDoc.CuryID : Edm.String "Currency"
PX.Objects.GL.GLTranDoc.TranCode : Edm.String "Tran. Code"
PX.Objects.GL.GLTranDoc.TranModule : Edm.String "Tran. Module"
PX.Objects.GL.GLTranDoc.TranType : Edm.String "Type"
PX.Objects.GL.GLTranDoc.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.GL.GLTranDoc.BAccountID : Edm.Int32 "Customer/Vendor"
PX.Objects.GL.GLTranDoc.ProjectID : Edm.Int32 "Project"
PX.Objects.GL.GLTranDoc.EntryTypeID : Edm.String "Entry Type ID"
PX.Objects.GL.GLTranDoc.CADrCr : Edm.String
PX.Objects.GL.GLTranDoc.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.GL.GLTranDoc.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.GL.GLTranDoc.RefNbr : Edm.String "Ref. Number"
PX.Objects.GL.GLTranDoc.DocCreated : Edm.Boolean [required] "Doc. Created"
PX.Objects.GL.GLTranDoc.ExtRefNbr : Edm.String "Ext. Ref.Number"
PX.Objects.GL.GLTranDoc.TranAmt : Edm.Decimal
PX.Objects.GL.GLTranDoc.TranTotal : Edm.Decimal
PX.Objects.GL.GLTranDoc.CuryInfoID : Edm.Int64
PX.Objects.GL.GLTranDoc.CuryTranTotal : Edm.Decimal "Total Amount"
PX.Objects.GL.GLTranDoc.CuryTranAmt : Edm.Decimal "Subtotal Amount"
PX.Objects.GL.GLTranDoc.Released : Edm.Boolean "Released"
PX.Objects.GL.GLTranDoc.TranClass : Edm.String
PX.Objects.GL.GLTranDoc.TranDesc : Edm.String "Transaction Description"
PX.Objects.GL.GLTranDoc.TranLineNbr : Edm.Int32
PX.Objects.GL.GLTranDoc.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.GL.GLTranDoc.TranPeriodID : Edm.String
PX.Objects.GL.GLTranDoc.FinPeriodID : Edm.String
PX.Objects.GL.GLTranDoc.PMTranID : Edm.Int64
PX.Objects.GL.GLTranDoc.LedgerBalanceType : Edm.String
PX.Objects.GL.GLTranDoc.TermsID : Edm.String "Terms"
PX.Objects.GL.GLTranDoc.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.GL.GLTranDoc.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.GL.GLTranDoc.CuryDiscAmt : Edm.Decimal "Cash Discount"
PX.Objects.GL.GLTranDoc.DiscAmt : Edm.Decimal
PX.Objects.GL.GLTranDoc.NoteID : Edm.Guid
PX.Objects.GL.GLTranDoc.NoteText : Edm.String "Note Text"
PX.Objects.GL.GLTranDoc.tstamp : Edm.Binary
PX.Objects.GL.GLTranDoc.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLTranDoc.CreatedByScreenID : Edm.String
PX.Objects.GL.GLTranDoc.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLTranDoc.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLTranDoc.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLTranDoc.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.GLTranDoc.CuryBalanceAmt : Edm.Decimal "Tran Amount"
PX.Objects.GL.GLTranDoc.GroupTranID : Edm.Int32 "GroupTranID"
PX.Objects.GL.GLTranDoc.CashAccountID : Edm.Int32
PX.Objects.GL.GLTranDoc.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.GL.GLTranDoc.TaxID : Edm.String "Tax ID"
PX.Objects.GL.GLTranDoc.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.GL.GLTranDoc.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.GL.GLTranDoc.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.GL.GLTranDoc.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.GL.GLTranDoc.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.GL.GLTranDoc.CuryInclTaxAmt : Edm.Decimal "Included Tax Amount"
PX.Objects.GL.GLTranDoc.InclTaxAmt : Edm.Decimal "Included Tax Amount"
PX.Objects.GL.GLTranDoc.CuryOrigWhTaxAmt : Edm.Decimal [required] "With. Tax"
PX.Objects.GL.GLTranDoc.OrigWhTaxAmt : Edm.Decimal [required]
PX.Objects.GL.GLTranDoc.CuryDocTotal : Edm.Decimal "Doc Total"
PX.Objects.GL.GLTranDoc.DocTotal : Edm.Decimal
PX.Objects.GL.GLTranDoc.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.GL.GLTranDoc.CuryApplAmt : Edm.Decimal "Application Amount"
PX.Objects.GL.GLTranDoc.ApplAmt : Edm.Decimal
PX.Objects.GL.GLTranDoc.CuryDiscTaken : Edm.Decimal
PX.Objects.GL.GLTranDoc.DiscTaken : Edm.Decimal
PX.Objects.GL.GLTranDoc.CuryTaxWheld : Edm.Decimal
PX.Objects.GL.GLTranDoc.TaxWheld : Edm.Decimal
PX.Objects.GL.GLTranDoc.ApplCount : Edm.Int32 [required]
PX.Objects.GL.GLTranDoc.CuryUnappliedBal : Edm.Decimal "Unapplied Balance"
PX.Objects.GL.GLTranDoc.UnappliedBal : Edm.Decimal
PX.Objects.GL.GLTranDoc.CuryDiscBal : Edm.Decimal "Disc. Balance"
PX.Objects.GL.GLTranDoc.DiscBal : Edm.Decimal
PX.Objects.GL.GLTranDoc.CuryWhTaxBal : Edm.Decimal "Wh. Tax Balance"
PX.Objects.GL.GLTranDoc.WhTaxBal : Edm.Decimal
PX.Objects.GL.GLTranDoc.NeedsDebitCashAccount : Edm.Boolean
PX.Objects.GL.GLTranDoc.IsARCustomerCashAccount : Edm.Boolean
PX.Objects.GL.GLTranDoc.NeedsCreditCashAccount : Edm.Boolean
PX.Objects.GL.GLTranDoc.NeedTaskValidation : Edm.Boolean
PX.Objects.GL.GLTranDoc.DebitCashAccountID : Edm.Int32
PX.Objects.GL.GLTranDoc.CreditCashAccountID : Edm.Int32
PX.Objects.GL.GLTranDoc.CuryRate : Edm.Decimal
PX.Objects.GL.GLTranDoc.CuryViewState : Edm.Boolean
PX.Objects.GL.GLTranDoc.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.GL.GLTranDoc.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.GL.GLTranDoc.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.GL.GLTranDoc.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.GL.GLTranDoc.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.GL.GLTranDoc.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.GL.GLTranDoc.BatchByRefNbr -> PX.Objects.GL.Batch (TranModule=Module, RefNbr=BatchNbr)
PX.Objects.GL.GLTranDoc.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.GL.GLTranDoc.APPaymentByRefNbr -> PX.Objects.AP.APPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.GL.GLTranDoc.GLTranDocByParentLineNbr -> PX.Objects.GL.GLTranDoc (ParentLineNbr=LineNbr)
PX.Objects.GL.GLTranDoc.PMTranByPMTranID -> PX.Objects.PM.PMTran (PMTranID=TranID)
PX.Objects.GL.GLTranDoc.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.GLTranDoc.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.GL.GLTranDoc.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLTranDoc.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLTranDoc.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.GL.GLTranDoc.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.GL.GLTranDoc.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.GL.GLTranDoc.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.GL.GLTranDoc.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.GL.GLTranDoc.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.GL.GLTranDoc.AccountByDebitAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLTranDoc.AccountByCreditAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLTranDoc.GLDocBatchByBatchNbr -> PX.Objects.GL.GLDocBatch (Module=Module, BatchNbr=BatchNbr)
PX.Objects.GL.GLTranDoc.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLTranDoc.SubByDebitAccountID -> PX.Objects.GL.Sub
PX.Objects.GL.GLTranDoc.SubByCreditAccountID -> PX.Objects.GL.Sub
PX.Objects.GL.GLTranDoc.SubByDebitSubID -> PX.Objects.GL.Sub
PX.Objects.GL.GLTranDoc.SubByCreditSubID -> PX.Objects.GL.Sub
PX.Objects.GL.GLTranDoc.CAAdjByRefNbr -> PX.Objects.CA.CAAdj (TranType=AdjTranType, RefNbr=AdjRefNbr)
PX.Objects.GL.GLTranDoc.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.GL.GLTranDoc.CAEntryTypeByTranModule -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId, TranModule=Module)
PX.Objects.GL.GLTranDoc.CashAccountByDebitCashAccountID -> PX.Objects.CA.CashAccount (DebitCashAccountID=CashAccountID)
PX.Objects.GL.GLTranDoc.CashAccountByCreditCashAccountID -> PX.Objects.CA.CashAccount (CreditCashAccountID=CashAccountID)
PX.Objects.GL.GLTranDoc.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.GL.GLTranDoc.LocationByLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.GL.GLTranDoc.LocationByBAccountID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.GL.GLTranDoc.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.GL.GLTranDoc.CustomerPaymentMethodByPaymentMethodID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID, BAccountID=BAccountID, PaymentMethodID=PaymentMethodID)
PX.Objects.GL.GLTranDoc.GLTranCodeByTranType -> PX.Objects.GL.GLTranCode (TranModule=Module, TranType=TranType)
PX.Objects.GL.GLTranDoc.GLTranCodeByTranCode -> PX.Objects.GL.GLTranCode (TranCode=TranCode)
PX.Objects.GL.GLTranDoc.GLTaxCollection -> Collection(PX.Objects.GL.GLTax)
PX.Objects.GL.GLTranDoc.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)

# PX.Objects.GL.GLTranR (EntityType)

Label: "GL Transaction"
BaseType: PX.Objects.GL.GLTran
Key: BatchNbr, LineNbr, Module (inherited from PX.Objects.GL.GLTran)
Entity sets: PX_Objects_GL_GLTranR
Non-filterable, non-selectable: BegBalance, EndBalance, CuryBegBalance, CuryEndBalance, SignBegBalance, SignEndBalance, SignCuryBegBalance, SignCuryEndBalance, Type, BatchType

PX.Objects.GL.GLTranR.BatchDescription : Edm.String "Batch Description"
PX.Objects.GL.GLTranR.BegBalance : Edm.Decimal "Beg. Balance"
PX.Objects.GL.GLTranR.EndBalance : Edm.Decimal "Ending Balance"
PX.Objects.GL.GLTranR.CuryBegBalance : Edm.Decimal "Curr. Beg. Balance"
PX.Objects.GL.GLTranR.CuryEndBalance : Edm.Decimal "Curr. Ending Balance"
PX.Objects.GL.GLTranR.SignBegBalance : Edm.Decimal "Beg. Balance"
PX.Objects.GL.GLTranR.SignEndBalance : Edm.Decimal "Ending Balance"
PX.Objects.GL.GLTranR.SignCuryBegBalance : Edm.Decimal "Curr. Beg. Balance"
PX.Objects.GL.GLTranR.SignCuryEndBalance : Edm.Decimal "Curr. Ending Balance"
PX.Objects.GL.GLTranR.Type : Edm.String
PX.Objects.GL.GLTranR.BatchType : Edm.String

# PX.Objects.GL.GLTrialBalanceImportDetails (EntityType)

Label: "Trial Balance Import Details"
Key: Line, MapNumber
Entity sets: PX_Objects_GL_GLTrialBalanceImportDetails, TrialBalanceImportDetails, GLTrialBalanceImportDetails
Non-filterable, non-selectable: Description, AccountType, AccountCuryID

PX.Objects.GL.GLTrialBalanceImportDetails.MapNumber : Edm.String [key] "MapNumber"
PX.Objects.GL.GLTrialBalanceImportDetails.Line : Edm.Int32 [key] "Line"
PX.Objects.GL.GLTrialBalanceImportDetails.ImportBranchCDError : Edm.String "ImportBranchCDError"
PX.Objects.GL.GLTrialBalanceImportDetails.ImportAccountCDError : Edm.String "ImportAccountCDError"
PX.Objects.GL.GLTrialBalanceImportDetails.ImportSubAccountCDError : Edm.String "ImportSubAccountCDError"
PX.Objects.GL.GLTrialBalanceImportDetails.Status : Edm.Int32 [required] "Status"
PX.Objects.GL.GLTrialBalanceImportDetails.YtdBalance : Edm.Decimal "YTD Balance"
PX.Objects.GL.GLTrialBalanceImportDetails.CuryYtdBalance : Edm.Decimal "Currency YTD Balance"
PX.Objects.GL.GLTrialBalanceImportDetails.Description : Edm.String "Description"
PX.Objects.GL.GLTrialBalanceImportDetails.AccountType : Edm.String "Type"
PX.Objects.GL.GLTrialBalanceImportDetails.AccountCuryID : Edm.String
PX.Objects.GL.GLTrialBalanceImportDetails.tstamp : Edm.Binary
PX.Objects.GL.GLTrialBalanceImportDetails.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.GL.GLTrialBalanceImportDetails.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.GL.GLTrialBalanceImportDetails.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.GL.GLTrialBalanceImportDetails.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.GL.GLTrialBalanceImportDetails.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.GL.GLTrialBalanceImportDetails.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.GL.GLTrialBalanceImportDetails.BranchByImportBranchCD -> PX.Objects.GL.Branch
PX.Objects.GL.GLTrialBalanceImportDetails.BranchByMapBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.GLTrialBalanceImportDetails.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLTrialBalanceImportDetails.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLTrialBalanceImportDetails.AccountByImportAccountCD -> PX.Objects.GL.Account
PX.Objects.GL.GLTrialBalanceImportDetails.AccountByMapAccountID -> PX.Objects.GL.Account
PX.Objects.GL.GLTrialBalanceImportDetails.GLTrialBalanceImportMapByMapNumber -> PX.Objects.GL.GLTrialBalanceImportMap (MapNumber=Number)
PX.Objects.GL.GLTrialBalanceImportDetails.SubByImportSubAccountCD -> PX.Objects.GL.Sub
PX.Objects.GL.GLTrialBalanceImportDetails.SubByMapSubAccountID -> PX.Objects.GL.Sub

# PX.Objects.GL.GLTrialBalanceImportMap (EntityType)

Label: "Trial Balance Import"
Key: Number
Entity sets: PX_Objects_GL_GLTrialBalanceImportMap, TrialBalanceImport, GLTrialBalanceImportMap
Non-filterable, non-selectable: OrganizationID, IsEditable, NoteText

PX.Objects.GL.GLTrialBalanceImportMap.Number : Edm.String [key] "Import Number"
PX.Objects.GL.GLTrialBalanceImportMap.OrganizationID : Edm.Int32
PX.Objects.GL.GLTrialBalanceImportMap.BatchNbr : Edm.String "Batch Number"
PX.Objects.GL.GLTrialBalanceImportMap.ImportDate : Edm.DateTimeOffset "Import Date"
PX.Objects.GL.GLTrialBalanceImportMap.FinPeriodID : Edm.String "Period"
PX.Objects.GL.GLTrialBalanceImportMap.Description : Edm.String "Description"
PX.Objects.GL.GLTrialBalanceImportMap.LedgerID : Edm.Int32 "Ledger"
PX.Objects.GL.GLTrialBalanceImportMap.IsHold : Edm.Boolean [required] "Hold"
PX.Objects.GL.GLTrialBalanceImportMap.Status : Edm.String "Status"
PX.Objects.GL.GLTrialBalanceImportMap.IsEditable : Edm.Boolean
PX.Objects.GL.GLTrialBalanceImportMap.CreditTotalBalance : Edm.Decimal [required] "Credit Total"
PX.Objects.GL.GLTrialBalanceImportMap.DebitTotalBalance : Edm.Decimal [required] "Debit Total"
PX.Objects.GL.GLTrialBalanceImportMap.LiabilityTotal : Edm.Decimal [required] "Liability Total"
PX.Objects.GL.GLTrialBalanceImportMap.IncomeTotal : Edm.Decimal [required] "Income Total"
PX.Objects.GL.GLTrialBalanceImportMap.AssetTotal : Edm.Decimal [required] "Asset Total"
PX.Objects.GL.GLTrialBalanceImportMap.ExpenseTotal : Edm.Decimal [required] "Expense Total"
PX.Objects.GL.GLTrialBalanceImportMap.TotalBalance : Edm.Decimal [required] "Control Total"
PX.Objects.GL.GLTrialBalanceImportMap.LineCntr : Edm.Int32
PX.Objects.GL.GLTrialBalanceImportMap.NoteID : Edm.Guid
PX.Objects.GL.GLTrialBalanceImportMap.NoteText : Edm.String "Note Text"
PX.Objects.GL.GLTrialBalanceImportMap.tstamp : Edm.Binary
PX.Objects.GL.GLTrialBalanceImportMap.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.GLTrialBalanceImportMap.CreatedByScreenID : Edm.String
PX.Objects.GL.GLTrialBalanceImportMap.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.GL.GLTrialBalanceImportMap.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.GLTrialBalanceImportMap.LastModifiedByScreenID : Edm.String
PX.Objects.GL.GLTrialBalanceImportMap.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.GL.GLTrialBalanceImportMap.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.GL.GLTrialBalanceImportMap.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.GL.GLTrialBalanceImportMap.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.GLTrialBalanceImportMap.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.GLTrialBalanceImportMap.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.GLTrialBalanceImportMap.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)

# PX.Objects.GL.INSiteTo (EntityType)

Label: "Warehouse"
BaseType: PX.Objects.IN.INSite
Key: SiteCD (inherited from PX.Objects.IN.INSite)
Entity sets: PX_Objects_GL_INSiteTo

# PX.Objects.GL.INSiteToBranch (EntityType)

Label: "Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_INSiteToBranch

# PX.Objects.GL.Ledger (EntityType)

Label: "Ledger"
Key: LedgerCD
Entity sets: PX_Objects_GL_Ledger, Ledger
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.GL.Ledger.LedgerID : Edm.Int32 "Ledger ID"
PX.Objects.GL.Ledger.LedgerCD : Edm.String [key] "Ledger ID"
PX.Objects.GL.Ledger.OrganizationID : Edm.Int32
PX.Objects.GL.Ledger.BaseCuryID : Edm.String "Currency"
PX.Objects.GL.Ledger.Descr : Edm.String "Description"
PX.Objects.GL.Ledger.BalanceType : Edm.String "Type"
PX.Objects.GL.Ledger.DefBranchID : Edm.Int32
PX.Objects.GL.Ledger.PostInterCompany : Edm.Boolean [required] "Branch Accounting"
PX.Objects.GL.Ledger.ConsolAllowed : Edm.Boolean [required] "Consolidation Source"
PX.Objects.GL.Ledger.tstamp : Edm.Binary
PX.Objects.GL.Ledger.NoteID : Edm.Guid
PX.Objects.GL.Ledger.NoteText : Edm.String "Note Text"
PX.Objects.GL.Ledger.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.Ledger.CreatedByScreenID : Edm.String
PX.Objects.GL.Ledger.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.GL.Ledger.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.Ledger.LastModifiedByScreenID : Edm.String
PX.Objects.GL.Ledger.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.GL.Ledger.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.Ledger.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.Ledger.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.Ledger.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.GL.Ledger.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.GL.Ledger.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.GL.Ledger.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.GL.Ledger.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.GL.Ledger.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.Objects.GL.Ledger.GLAllocationCollection -> Collection(PX.Objects.GL.GLAllocation)
PX.Objects.GL.Ledger.GLBudgetLineCollection -> Collection(PX.Objects.GL.GLBudgetLine)
PX.Objects.GL.Ledger.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.GL.Ledger.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.GL.Ledger.RQBudgetLedgerCollection -> Collection(PX.Objects.RQ.DAC.RQBudgetLedger)
PX.Objects.GL.Ledger.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.Objects.GL.Ledger.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.GL.Ledger.TranslDefCollection -> Collection(PX.Objects.CM.TranslDef)
PX.Objects.GL.Ledger.GLBudgetCollection -> Collection(PX.Objects.GL.GLBudget)
PX.Objects.GL.Ledger.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)
PX.Objects.GL.Ledger.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.GL.Ledger.GLTrialBalanceImportMapCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportMap)
PX.Objects.GL.Ledger.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.GL.Ledger.ArmGLHistoryByPeriodCollection -> Collection(PX.Objects.CS.ArmGLHistoryByPeriod)
PX.Objects.GL.Ledger.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.Objects.GL.Ledger.GLConsolSetupCollection -> Collection(PX.Objects.GL.GLConsolSetup)
PX.Objects.GL.Ledger.GLHistoryByPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByPeriod)
PX.Objects.GL.Ledger.GLHistoryByCurrentPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByCurrentPeriod)
PX.Objects.GL.Ledger.GLHistoryByPeriodCurrentCollection -> Collection(PX.Objects.GL.GLHistoryByPeriodCurrent)
PX.Objects.GL.Ledger.GLHistoryByPeriodMasterCurrentCollection -> Collection(PX.Objects.GL.GLHistoryByPeriodMasterCurrent)
PX.Objects.GL.Ledger.GLHistoryLastRevaluationCollection -> Collection(PX.Objects.GL.GLHistoryLastRevaluation)
PX.Objects.GL.Ledger.OrganizationLedgerLinkCollection -> Collection(PX.Objects.GL.DAC.OrganizationLedgerLink)

# PX.Objects.GL.Overrides.ScheduleMaint.BatchSelection (EntityType)

Label: "Batch to Process"
BaseType: PX.Objects.GL.Batch
Key: BatchNbr, Module (inherited from PX.Objects.GL.Batch)
Entity sets: PX_Objects_GL_Overrides_ScheduleMaint_BatchSelection, BatchtoProcess, BatchSelection

# PX.Objects.GL.Overrides.ScheduleProcess.BatchNew (EntityType)

Label: "GL Batch New"
BaseType: PX.Objects.GL.Batch
Key: BatchNbr, Module (inherited from PX.Objects.GL.Batch)
Entity sets: PX_Objects_GL_Overrides_ScheduleProcess_BatchNew, GLBatchNew, BatchNew
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.GL.Overrides.ScheduleProcess.BatchNew.RefBatchNbr : Edm.String

# PX.Objects.GL.Overrides.ScheduleProcess.GLTranNew (EntityType)

Label: "GL Transaction"
BaseType: PX.Objects.GL.GLTran
Key: BatchNbr, LineNbr, Module (inherited from PX.Objects.GL.GLTran)
Entity sets: PX_Objects_GL_Overrides_ScheduleProcess_GLTranNew
Non-filterable, non-selectable: RefBatchNbr

PX.Objects.GL.Overrides.ScheduleProcess.GLTranNew.RefBatchNbr : Edm.String
PX.Objects.GL.Overrides.ScheduleProcess.GLTranNew.AccountID : Edm.Int32
PX.Objects.GL.Overrides.ScheduleProcess.GLTranNew.SubID : Edm.Int32

# PX.Objects.GL.ReclassBatch (EntityType)

Label: "GL Batch"
BaseType: PX.Objects.GL.Batch
Key: BatchNbr, Module (inherited from PX.Objects.GL.Batch)
Entity sets: PX_Objects_GL_ReclassBatch

# PX.Objects.GL.Reclassification.Common.GLTranForReclassification (EntityType)

Label: "GL Transaction"
BaseType: PX.Objects.GL.GLTran
Key: BatchNbr, LineNbr, Module (inherited from PX.Objects.GL.GLTran)
Entity sets: PX_Objects_GL_Reclassification_Common_GLTranForReclassification
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.GL.Reclassification.Common.GLTranForReclassification.SplittedIcon : Edm.String
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.NewBranchID : Edm.Int32 "To Branch"
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.NewTranDate : Edm.DateTimeOffset "New Tran. Date"
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.NewFinPeriodID : Edm.String
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.NewTranDesc : Edm.String "New Transaction Description"
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.NewProjectID : Edm.Int32 "To Project"
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.CuryNewAmt : Edm.Decimal "New Amount"
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.NewAmt : Edm.Decimal
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.SortOrder : Edm.Int32
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.SourceCuryDebitAmt : Edm.Decimal
PX.Objects.GL.Reclassification.Common.GLTranForReclassification.SourceCuryCreditAmt : Edm.Decimal

# PX.Objects.GL.Reclassification.UI.GLTranReclHist (EntityType)

Label: "GL Transaction"
BaseType: PX.Objects.GL.GLTran
Key: BatchNbr, LineNbr, Module (inherited from PX.Objects.GL.GLTran)
Entity sets: PX_Objects_GL_Reclassification_UI_GLTranReclHist
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.GL.Reclassification.UI.GLTranReclHist.SplitIcon : Edm.String
PX.Objects.GL.Reclassification.UI.GLTranReclHist.ActionDesc : Edm.String "Action"
PX.Objects.GL.Reclassification.UI.GLTranReclHist.SortOrder : Edm.Int32
PX.Objects.GL.Reclassification.UI.GLTranReclHist.IsParent : Edm.Boolean
PX.Objects.GL.Reclassification.UI.GLTranReclHist.IsSplited : Edm.Boolean
PX.Objects.GL.Reclassification.UI.GLTranReclHist.IsCurrent : Edm.Boolean

# PX.Objects.GL.ReclassifyingGLTranAggregate (EntityType)

Key: BatchNbr, LineNbr, Module
Entity sets: PX_Objects_GL_ReclassifyingGLTranAggregate

PX.Objects.GL.ReclassifyingGLTranAggregate.Module : Edm.String [key]
PX.Objects.GL.ReclassifyingGLTranAggregate.BatchNbr : Edm.String [key]
PX.Objects.GL.ReclassifyingGLTranAggregate.LineNbr : Edm.Int32 [key]
PX.Objects.GL.ReclassifyingGLTranAggregate.DebitAmt : Edm.Decimal
PX.Objects.GL.ReclassifyingGLTranAggregate.CreditAmt : Edm.Decimal
PX.Objects.GL.ReclassifyingGLTranAggregate.CuryDebitAmt : Edm.Decimal
PX.Objects.GL.ReclassifyingGLTranAggregate.CuryCreditAmt : Edm.Decimal
PX.Objects.GL.ReclassifyingGLTranAggregate.BatchByBatchNbr -> PX.Objects.GL.Batch (Module=Module, BatchNbr=BatchNbr)
PX.Objects.GL.ReclassifyingGLTranAggregate.GLTranCollection -> Collection(PX.Objects.GL.GLTran)

# PX.Objects.GL.Schedule (EntityType)

Label: "Schedule"
Key: ScheduleID
Entity sets: PX_Objects_GL_Schedule, Schedule
Non-filterable, non-selectable: FormScheduleType, NoteText, Days, Weeks, Months, Periods

PX.Objects.GL.Schedule.ScheduleID : Edm.String [key] "Schedule ID"
PX.Objects.GL.Schedule.ScheduleName : Edm.String "Description"
PX.Objects.GL.Schedule.Active : Edm.Boolean "Active"
PX.Objects.GL.Schedule.ScheduleType : Edm.String "Schedule Type"
PX.Objects.GL.Schedule.FormScheduleType : Edm.String "Frequency"
PX.Objects.GL.Schedule.DailyFrequency : Edm.Int16 "Every"
PX.Objects.GL.Schedule.WeeklyFrequency : Edm.Int16 "Every"
PX.Objects.GL.Schedule.WeeklyOnDay1 : Edm.Boolean "Sunday"
PX.Objects.GL.Schedule.WeeklyOnDay2 : Edm.Boolean "Monday"
PX.Objects.GL.Schedule.WeeklyOnDay3 : Edm.Boolean "Tuesday"
PX.Objects.GL.Schedule.WeeklyOnDay4 : Edm.Boolean "Wednesday"
PX.Objects.GL.Schedule.WeeklyOnDay5 : Edm.Boolean "Thursday"
PX.Objects.GL.Schedule.WeeklyOnDay6 : Edm.Boolean "Friday"
PX.Objects.GL.Schedule.WeeklyOnDay7 : Edm.Boolean "Saturday"
PX.Objects.GL.Schedule.MonthlyFrequency : Edm.Int16 "Every"
PX.Objects.GL.Schedule.MonthlyDaySel : Edm.String "Recurrence"
PX.Objects.GL.Schedule.MonthlyOnDay : Edm.Int16 "On Day"
PX.Objects.GL.Schedule.MonthlyOnWeek : Edm.Int16 "On the"
PX.Objects.GL.Schedule.MonthlyOnDayOfWeek : Edm.Int16 "Day of Week"
PX.Objects.GL.Schedule.PeriodFrequency : Edm.Int16 "Every"
PX.Objects.GL.Schedule.PeriodDateSel : Edm.String "Recurrence"
PX.Objects.GL.Schedule.PeriodFixedDay : Edm.Int16 "Fixed Day of the Period"
PX.Objects.GL.Schedule.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.GL.Schedule.NoEndDate : Edm.Boolean "Never Expires"
PX.Objects.GL.Schedule.EndDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.GL.Schedule.NoRunLimit : Edm.Boolean "No Limit"
PX.Objects.GL.Schedule.RunLimit : Edm.Int16 "Execution Limit (Times)"
PX.Objects.GL.Schedule.RunCntr : Edm.Int16 "Executed (Times)"
PX.Objects.GL.Schedule.NextRunDate : Edm.DateTimeOffset "Next Execution"
PX.Objects.GL.Schedule.LastRunDate : Edm.DateTimeOffset "Last Executed"
PX.Objects.GL.Schedule.NoteID : Edm.Guid
PX.Objects.GL.Schedule.NoteText : Edm.String "Note Text"
PX.Objects.GL.Schedule.tstamp : Edm.Binary
PX.Objects.GL.Schedule.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.Schedule.CreatedByScreenID : Edm.String
PX.Objects.GL.Schedule.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.GL.Schedule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.Schedule.LastModifiedByScreenID : Edm.String
PX.Objects.GL.Schedule.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.GL.Schedule.Module : Edm.String
PX.Objects.GL.Schedule.Days : Edm.String "Days"
PX.Objects.GL.Schedule.Weeks : Edm.String "Weeks"
PX.Objects.GL.Schedule.Months : Edm.String "Months"
PX.Objects.GL.Schedule.Periods : Edm.String "Periods"
PX.Objects.GL.Schedule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.Schedule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.Schedule.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.GL.Schedule.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.GL.Schedule.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.GL.Schedule.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.GL.Schedule.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.GL.Schedule.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.GL.Schedule.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)

# PX.Objects.GL.Standalone.LedgerAlias (EntityType)

Label: "Ledger"
BaseType: PX.Objects.GL.Ledger
Key: LedgerCD (inherited from PX.Objects.GL.Ledger)
Entity sets: PX_Objects_GL_Standalone_LedgerAlias, Ledger1, LedgerAlias

# PX.Objects.GL.Sub (EntityType)

Label: "Subaccount"
Key: SubCD
Entity sets: PX_Objects_GL_Sub, Subaccount, Sub
Non-filterable, non-selectable: NoteText, Included, Secured, DeletedDatabaseRecord

PX.Objects.GL.Sub.SubID : Edm.Int32 "Sub. ID"
PX.Objects.GL.Sub.SubCD : Edm.String [key] "Subaccount"
PX.Objects.GL.Sub.Active : Edm.Boolean [required] "Active"
PX.Objects.GL.Sub.Description : Edm.String "Description"
PX.Objects.GL.Sub.ConsoSubID : Edm.Int32 "Consolidation Subaccount ID"
PX.Objects.GL.Sub.ConsoSubCode : Edm.String "Consolidation Subaccount Code"
PX.Objects.GL.Sub.NoteID : Edm.Guid
PX.Objects.GL.Sub.NoteText : Edm.String "Note Text"
PX.Objects.GL.Sub.tstamp : Edm.Binary
PX.Objects.GL.Sub.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.Sub.CreatedByScreenID : Edm.String
PX.Objects.GL.Sub.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.Sub.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.Sub.LastModifiedByScreenID : Edm.String
PX.Objects.GL.Sub.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.Sub.Included : Edm.Boolean "Included"
PX.Objects.GL.Sub.Secured : Edm.Boolean "Secured"
PX.Objects.GL.Sub.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.Sub.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.Sub.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.Sub.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.GL.Sub.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.GL.Sub.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.GL.Sub.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.GL.Sub.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.GL.Sub.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.GL.Sub.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.GL.Sub.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.GL.Sub.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.GL.Sub.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.GL.Sub.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.GL.Sub.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.GL.Sub.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.GL.Sub.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.GL.Sub.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.GL.Sub.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.GL.Sub.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.GL.Sub.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.GL.Sub.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.GL.Sub.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.GL.Sub.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.GL.Sub.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.GL.Sub.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.GL.Sub.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.GL.Sub.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.GL.Sub.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.GL.Sub.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.GL.Sub.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.GL.Sub.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.GL.Sub.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.GL.Sub.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.GL.Sub.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.GL.Sub.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.GL.Sub.DRDeferredCodeCollection -> Collection(PX.Objects.DR.DRDeferredCode)
PX.Objects.GL.Sub.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.GL.Sub.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.Objects.GL.Sub.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.GL.Sub.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.GL.Sub.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.GL.Sub.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.GL.Sub.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.GL.Sub.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.GL.Sub.SOOrderTypeCollection -> Collection(PX.Objects.SO.SOOrderType)
PX.Objects.GL.Sub.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.GL.Sub.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.GL.Sub.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.GL.Sub.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.GL.Sub.CurrencyCollection -> Collection(PX.Objects.CM.Currency)
PX.Objects.GL.Sub.GLBudgetLineCollection -> Collection(PX.Objects.GL.GLBudgetLine)
PX.Objects.GL.Sub.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.GL.Sub.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.GL.Sub.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.GL.Sub.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.GL.Sub.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.GL.Sub.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.GL.Sub.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.GL.Sub.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.GL.Sub.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.GL.Sub.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.GL.Sub.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.GL.Sub.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.GL.Sub.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.GL.Sub.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.GL.Sub.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.GL.Sub.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.GL.Sub.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.GL.Sub.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.GL.Sub.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.GL.Sub.TXImportStateCollection -> Collection(PX.Objects.TX.TXImportState)
PX.Objects.GL.Sub.TXSetupCollection -> Collection(PX.Objects.TX.TXSetup)
PX.Objects.GL.Sub.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.GL.Sub.RQRequestClassCollection -> Collection(PX.Objects.RQ.RQRequestClass)
PX.Objects.GL.Sub.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.GL.Sub.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.GL.Sub.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.GL.Sub.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.GL.Sub.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.GL.Sub.POSetupCollection -> Collection(PX.Objects.PO.POSetup)
PX.Objects.GL.Sub.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.GL.Sub.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.Objects.GL.Sub.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.GL.Sub.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.GL.Sub.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.GL.Sub.FADisposalMethodCollection -> Collection(PX.Objects.FA.FADisposalMethod)
PX.Objects.GL.Sub.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.GL.Sub.FASetupCollection -> Collection(PX.Objects.FA.FASetup)
PX.Objects.GL.Sub.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.GL.Sub.CarrierCollection -> Collection(PX.Objects.CS.Carrier)
PX.Objects.GL.Sub.ReasonCodeCollection -> Collection(PX.Objects.CS.ReasonCode)
PX.Objects.GL.Sub.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.GL.Sub.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.Objects.GL.Sub.INPostClassCollection -> Collection(PX.Objects.IN.INPostClass)
PX.Objects.GL.Sub.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.GL.Sub.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.GL.Sub.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.GL.Sub.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.Objects.GL.Sub.GLAllocationDestinationCollection -> Collection(PX.Objects.GL.GLAllocationDestination)
PX.Objects.GL.Sub.GLAllocationSourceCollection -> Collection(PX.Objects.GL.GLAllocationSource)
PX.Objects.GL.Sub.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)
PX.Objects.GL.Sub.GLBudgetTreeCollection -> Collection(PX.Objects.GL.GLBudgetTree)
PX.Objects.GL.Sub.GLSetupCollection -> Collection(PX.Objects.GL.GLSetup)
PX.Objects.GL.Sub.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.GL.Sub.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.GL.Sub.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.GL.Sub.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.GL.Sub.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.GL.Sub.CASetupCollection -> Collection(PX.Objects.CA.CASetup)
PX.Objects.GL.Sub.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.Objects.GL.Sub.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.GL.Sub.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.GL.Sub.ARFinChargeCollection -> Collection(PX.Objects.AR.ARFinCharge)
PX.Objects.GL.Sub.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.GL.Sub.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.GL.Sub.SalesPersonCollection -> Collection(PX.Objects.AR.SalesPerson)
PX.Objects.GL.Sub.EPDepartmentCollection -> Collection(PX.Objects.EP.EPDepartment)
PX.Objects.GL.Sub.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.GL.Sub.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.GL.Sub.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.GL.Sub.AMLaborCodeCollection -> Collection(PX.Objects.AM.AMLaborCode)
PX.Objects.GL.Sub.AMMachCollection -> Collection(PX.Objects.AM.AMMach)
PX.Objects.GL.Sub.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.Objects.GL.Sub.AMOverheadCollection -> Collection(PX.Objects.AM.AMOverhead)
PX.Objects.GL.Sub.AMToolMstCollection -> Collection(PX.Objects.AM.AMToolMst)
PX.Objects.GL.Sub.AMWCMachCollection -> Collection(PX.Objects.AM.AMWCMach)
PX.Objects.GL.Sub.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.GL.Sub.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.GL.Sub.PRPayGroupCollection -> Collection(PX.Objects.PR.PRPayGroup)
PX.Objects.GL.Sub.PRPTOBankCollection -> Collection(PX.Objects.PR.PRPTOBank)
PX.Objects.GL.Sub.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.GL.Sub.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.GL.Sub.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.GL.Sub.SVOrderGLAccountCollection -> Collection(PX.Objects.SV.SVOrderGLAccount)
PX.Objects.GL.Sub.SVOrderTypeGLAccountCollection -> Collection(PX.Objects.SV.SVOrderTypeGLAccount)
PX.Objects.GL.Sub.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.GL.Sub.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.GL.Sub.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.GL.Sub.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.GL.Sub.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.GL.Sub.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.GL.Sub.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.Objects.GL.Sub.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.GL.Sub.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.GL.Sub.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.GL.Sub.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.GL.Sub.ArmGLHistoryByPeriodCollection -> Collection(PX.Objects.CS.ArmGLHistoryByPeriod)
PX.Objects.GL.Sub.BranchAcctMapFromCollection -> Collection(PX.Objects.GL.BranchAcctMapFrom)
PX.Objects.GL.Sub.BranchAcctMapToCollection -> Collection(PX.Objects.GL.BranchAcctMapTo)
PX.Objects.GL.Sub.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.Objects.GL.Sub.GLHistoryByPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByPeriod)
PX.Objects.GL.Sub.GLHistoryByCurrentPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByCurrentPeriod)
PX.Objects.GL.Sub.GLHistoryLastRevaluationCollection -> Collection(PX.Objects.GL.GLHistoryLastRevaluation)
PX.Objects.GL.Sub.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.GL.Sub.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.GL.Sub.LocationARAccountSubCollection -> Collection(PX.Objects.CR.LocationARAccountSub)
PX.Objects.GL.Sub.LocationAPAccountSubCollection -> Collection(PX.Objects.AP.LocationAPAccountSub)
PX.Objects.GL.Sub.DRSetupCollection -> Collection(PX.Objects.DR.DRSetup)
PX.Objects.GL.Sub.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.GL.Sub.INUpdateStdCostRecordCollection -> Collection(PX.Objects.IN.INUpdateStdCostRecord)
PX.Objects.GL.Sub.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.GL.Sub.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.GL.Sub.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.GL.Sub.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.GL.Sub.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.GL.TranBranch (EntityType)

Label: "Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_TranBranch

# PX.Objects.GL.TranINSite (EntityType)

Label: "Warehouse"
BaseType: PX.Objects.IN.INSite
Key: SiteCD (inherited from PX.Objects.IN.INSite)
Entity sets: PX_Objects_GL_TranINSite

# PX.Objects.GL.TranINSiteBranch (EntityType)

Label: "Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_TranINSiteBranch

# PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial (EntityType)

Label: "Adjustment Transactions grouped by SiteLotSerial"
Key: DocType, InventoryID, LotSerialNbr, RefNbr, SiteID
Entity sets: PX_Objects_IN_AffectedAvailability_AdjustmentTranBySiteLotSerial, AdjustmentTransactionsgroupedbySiteLotSerial, AdjustmentTranBySiteLotSerial

PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.DocType : Edm.String [key]
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.RefNbr : Edm.String [key]
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.LotSerialNbr : Edm.String [key]
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.BaseUnit : Edm.String
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.QtyHardAvail : Edm.Decimal
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.QtyAdjusted : Edm.Decimal
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.INRegisterByRefNbr -> PX.Objects.IN.INRegister (RefNbr=RefNbr)
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.INKitRegisterByRefNbr -> PX.Objects.IN.INKitRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.INUnitByBaseUnit -> PX.Objects.IN.INUnit (BaseUnit=FromUnit)
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.INUnitByInventoryID -> PX.Objects.IN.INUnit (InventoryID=InventoryID)
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.INUnitByWeightUOM -> PX.Objects.IN.INUnit
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.INUnitByVolumeUOM -> PX.Objects.IN.INUnit
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)

# PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus (EntityType)

Label: "Adjustment Transactions grouped by SiteStatus"
Key: DocType, InventoryID, RefNbr, SiteID
Entity sets: PX_Objects_IN_AffectedAvailability_AdjustmentTranBySiteStatus, AdjustmentTransactionsgroupedbySiteStatus, AdjustmentTranBySiteStatus

PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.DocType : Edm.String [key]
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.RefNbr : Edm.String [key]
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.Released : Edm.Boolean
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.BaseUnit : Edm.String
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.QtyHardAvail : Edm.Decimal
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.QtyAdjusted : Edm.Decimal
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.LSQtyToDeallocate : Edm.Decimal
PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus.INRegisterByRefNbr -> PX.Objects.IN.INRegister (RefNbr=RefNbr)

# PX.Objects.IN.AffectedAvailability.Allocation (ComplexType)


PX.Objects.IN.AffectedAvailability.Allocation.PlanID : Edm.Int64
PX.Objects.IN.AffectedAvailability.Allocation.DocType : Edm.String
PX.Objects.IN.AffectedAvailability.Allocation.RefNoteID : Edm.Guid
PX.Objects.IN.AffectedAvailability.Allocation.RefEntityType : Edm.String
PX.Objects.IN.AffectedAvailability.Allocation.LineNbr : Edm.Int32
PX.Objects.IN.AffectedAvailability.Allocation.InventoryID : Edm.Int32
PX.Objects.IN.AffectedAvailability.Allocation.LotSerialNbr : Edm.String
PX.Objects.IN.AffectedAvailability.Allocation.AllocatedQty : Edm.Decimal
PX.Objects.IN.AffectedAvailability.Allocation.Status : Edm.String
PX.Objects.IN.AffectedAvailability.Allocation.OwnerID : Edm.Int32
PX.Objects.IN.AffectedAvailability.Allocation.CustomerID : Edm.Int32
PX.Objects.IN.AffectedAvailability.Allocation.Date : Edm.DateTimeOffset
PX.Objects.IN.AffectedAvailability.Allocation.RequestedDate : Edm.DateTimeOffset

# PX.Objects.IN.DAC.INConversionHistory (EntityType)

Label: "Inventory Conversion History"
Key: HistoryID
Entity sets: PX_Objects_IN_DAC_INConversionHistory, InventoryConversionHistory, INConversionHistory

PX.Objects.IN.DAC.INConversionHistory.HistoryID : Edm.Int32 [key]
PX.Objects.IN.DAC.INConversionHistory.InventoryID : Edm.Int32
PX.Objects.IN.DAC.INConversionHistory.IsStockItem : Edm.Boolean
PX.Objects.IN.DAC.INConversionHistory.StartedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INConversionHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INConversionHistory.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INConversionHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INConversionHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Objects.IN.DAC.INItemClassSite (EntityType)

Label: "Warehouse Item Class Details"
Key: ItemClassID, SiteID
Entity sets: PX_Objects_IN_DAC_INItemClassSite, WarehouseItemClassDetails, INItemClassSite
Non-filterable, non-selectable: NoteText

PX.Objects.IN.DAC.INItemClassSite.ItemClassID : Edm.Int32 [key] "Item Class"
PX.Objects.IN.DAC.INItemClassSite.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.DAC.INItemClassSite.PlanningStrategyID : Edm.String "Picking Strategy"
PX.Objects.IN.DAC.INItemClassSite.NoteID : Edm.Guid
PX.Objects.IN.DAC.INItemClassSite.NoteText : Edm.String "Note Text"
PX.Objects.IN.DAC.INItemClassSite.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INItemClassSite.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INItemClassSite.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INItemClassSite.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INItemClassSite.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INItemClassSite.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INItemClassSite.tstamp : Edm.Binary
PX.Objects.IN.DAC.INItemClassSite.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INItemClassSite.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INItemClassSite.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.DAC.INItemClassSite.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.DAC.INItemClassSite.INSitePlanningStrategyByPlanningStrategyID -> PX.Objects.IN.DAC.INSitePlanningStrategy (PlanningStrategyID=PlanningStrategyID)

# PX.Objects.IN.DAC.INItemLotSerialAttributesHeader (EntityType)

Label: "INItemLotSerialAttributesHeader"
Key: InventoryID, LotSerialNbr
Entity sets: PX_Objects_IN_DAC_INItemLotSerialAttributesHeader, INItemLotSerialAttributesHeader
Non-filterable, non-selectable: NoteText

PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.MfgLotSerialNbr : Edm.String "Manufacturer Lot/Serial Nbr."
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.Descr : Edm.String "Description"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.ImageUrl : Edm.String "Image"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.Body : Edm.String "Content"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.NoteID : Edm.Guid
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.NoteText : Edm.String "Note Text"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.tstamp : Edm.Binary
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.INItemLotSerialByLotSerialNbr -> PX.Objects.IN.INItemLotSerial (InventoryID=InventoryID, LotSerialNbr=LotSerialNbr)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeader.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)

# PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings (EntityType)

Label: "INItemLotSerialAttributesHeaderCurySettings"
Key: CuryID, InventoryID, LotSerialNbr
Entity sets: PX_Objects_IN_DAC_INItemLotSerialAttributesHeaderCurySettings, INItemLotSerialAttributesHeaderCurySettings

PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.SalesPrice : Edm.Decimal "Sales Price"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.RecPrice : Edm.Decimal "MSRP"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.tstamp : Edm.Binary
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings.INItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.IN.DAC.INItemLotSerialAttributesHeader (InventoryID=InventoryID, LotSerialNbr=LotSerialNbr)

# PX.Objects.IN.DAC.INRegisterCart (EntityType)

Label: "Receipt Cart"
Key: CartID, DocType, RefNbr, SiteID
Entity sets: PX_Objects_IN_DAC_INRegisterCart, ReceiptCart, INRegisterCart

PX.Objects.IN.DAC.INRegisterCart.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.DAC.INRegisterCart.CartID : Edm.Int32 [key]
PX.Objects.IN.DAC.INRegisterCart.DocType : Edm.String [key] "Document Type"
PX.Objects.IN.DAC.INRegisterCart.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.IN.DAC.INRegisterCart.tstamp : Edm.Binary
PX.Objects.IN.DAC.INRegisterCart.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INRegisterCart.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INRegisterCart.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INRegisterCart.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INRegisterCart.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INRegisterCart.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INRegisterCart.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INRegisterCart.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INRegisterCart.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.IN.DAC.INRegisterCart.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.DAC.INRegisterCart.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.DAC.INRegisterCart.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)

# PX.Objects.IN.DAC.INRegisterCartLine (EntityType)

Label: "Receipt Cart Line"
Key: CartID, DocType, LineNbr, RefNbr, SiteID
Entity sets: PX_Objects_IN_DAC_INRegisterCartLine, ReceiptCartLine, INRegisterCartLine

PX.Objects.IN.DAC.INRegisterCartLine.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.DAC.INRegisterCartLine.CartID : Edm.Int32 [key]
PX.Objects.IN.DAC.INRegisterCartLine.DocType : Edm.String [key] "Document Type"
PX.Objects.IN.DAC.INRegisterCartLine.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.IN.DAC.INRegisterCartLine.CartSplitLineNbr : Edm.Int32
PX.Objects.IN.DAC.INRegisterCartLine.LineNbr : Edm.Int32 [key]
PX.Objects.IN.DAC.INRegisterCartLine.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.IN.DAC.INRegisterCartLine.tstamp : Edm.Binary
PX.Objects.IN.DAC.INRegisterCartLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INRegisterCartLine.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INRegisterCartLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INRegisterCartLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INRegisterCartLine.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INRegisterCartLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INRegisterCartLine.INTranByLineNbr -> PX.Objects.IN.INTran (DocType=DocType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.IN.DAC.INRegisterCartLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INRegisterCartLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INRegisterCartLine.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.IN.DAC.INRegisterCartLine.INCartSplitByCartSplitLineNbr -> PX.Objects.IN.INCartSplit (SiteID=SiteID, CartID=CartID, CartSplitLineNbr=SplitLineNbr)
PX.Objects.IN.DAC.INRegisterCartLine.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.DAC.INRegisterCartLine.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.DAC.INRegisterCartLine.INRegisterCartByRefNbr -> PX.Objects.IN.DAC.INRegisterCart (SiteID=SiteID, CartID=CartID, DocType=DocType, RefNbr=RefNbr)

# PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader (EntityType)

Label: "INRegisterItemLotSerialAttributesHeader"
Key: DocType, InventoryID, LotSerialNbr, RefNbr
Entity sets: PX_Objects_IN_DAC_INRegisterItemLotSerialAttributesHeader, INRegisterItemLotSerialAttributesHeader
Non-filterable, non-selectable: NoteText

PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.DocType : Edm.String [key] "Document Type"
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.InventoryID : Edm.Int32 [key]
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.MfgLotSerialNbr : Edm.String "Manufacturer Lot/Serial Nbr."
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.NoteID : Edm.Guid
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.NoteText : Edm.String "Note Text"
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.tstamp : Edm.Binary
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.INItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.IN.DAC.INItemLotSerialAttributesHeader (InventoryID=InventoryID, LotSerialNbr=LotSerialNbr)
PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)

# PX.Objects.IN.DAC.INSetupApproval (EntityType)

Label: "IN Approval"
Key: ApprovalID
Entity sets: PX_Objects_IN_DAC_INSetupApproval, INApproval, INSetupApproval

PX.Objects.IN.DAC.INSetupApproval.IsActive : Edm.Boolean [required] "Active"
PX.Objects.IN.DAC.INSetupApproval.DocType : Edm.String "Document Type"
PX.Objects.IN.DAC.INSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.IN.DAC.INSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.IN.DAC.INSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.IN.DAC.INSetupApproval.tstamp : Edm.Binary
PX.Objects.IN.DAC.INSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.IN.DAC.INSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.IN.DAC.INSitePlanningStrategy (EntityType)

Label: "Warehouse Planning Strategy"
Key: PlanningStrategyID
Entity sets: PX_Objects_IN_DAC_INSitePlanningStrategy, WarehousePlanningStrategy, INSitePlanningStrategy
Non-filterable, non-selectable: NoteText

PX.Objects.IN.DAC.INSitePlanningStrategy.PlanningStrategyID : Edm.String [key] "Picking Strategy"
PX.Objects.IN.DAC.INSitePlanningStrategy.Descr : Edm.String "Description"
PX.Objects.IN.DAC.INSitePlanningStrategy.Active : Edm.Boolean [required] "Active"
PX.Objects.IN.DAC.INSitePlanningStrategy.DetailLineCntr : Edm.Int32 [required]
PX.Objects.IN.DAC.INSitePlanningStrategy.NoteID : Edm.Guid
PX.Objects.IN.DAC.INSitePlanningStrategy.NoteText : Edm.String "Note Text"
PX.Objects.IN.DAC.INSitePlanningStrategy.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INSitePlanningStrategy.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INSitePlanningStrategy.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INSitePlanningStrategy.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INSitePlanningStrategy.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INSitePlanningStrategy.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INSitePlanningStrategy.tstamp : Edm.Binary
PX.Objects.IN.DAC.INSitePlanningStrategy.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INSitePlanningStrategy.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INSitePlanningStrategy.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.DAC.INSitePlanningStrategy.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.DAC.INSitePlanningStrategy.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.IN.DAC.INSitePlanningStrategy.INItemClassSiteCollection -> Collection(PX.Objects.IN.DAC.INItemClassSite)
PX.Objects.IN.DAC.INSitePlanningStrategy.INSitePlanningStrategyDetailCollection -> Collection(PX.Objects.IN.DAC.INSitePlanningStrategyDetail)

# PX.Objects.IN.DAC.INSitePlanningStrategyDetail (EntityType)

Label: "Warehouse Planning Strategy Detail"
Key: LineNbr, PlanningStrategyID
Entity sets: PX_Objects_IN_DAC_INSitePlanningStrategyDetail, WarehousePlanningStrategyDetail, INSitePlanningStrategyDetail
Non-filterable, non-selectable: NoteText

PX.Objects.IN.DAC.INSitePlanningStrategyDetail.PlanningStrategyID : Edm.String [key]
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.UnitOfHandling : Edm.String "Unit of Handling"
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.ZoneID : Edm.Int32 "Warehouse Zone"
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.SortOrder : Edm.Int32 "Priority"
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.NoteID : Edm.Guid
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.NoteText : Edm.String "Note Text"
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.tstamp : Edm.Binary
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.INSitePlanningStrategyByPlanningStrategyID -> PX.Objects.IN.DAC.INSitePlanningStrategy (PlanningStrategyID=PlanningStrategyID)
PX.Objects.IN.DAC.INSitePlanningStrategyDetail.INSiteZoneByZoneID -> PX.Objects.IN.DAC.INSiteZone (ZoneID=ZoneID)

# PX.Objects.IN.DAC.INSiteZone (EntityType)

Label: "Warehouse Zone"
Key: ZoneID
Entity sets: PX_Objects_IN_DAC_INSiteZone, WarehouseZone, INSiteZone
Non-filterable, non-selectable: NoteText

PX.Objects.IN.DAC.INSiteZone.SiteID : Edm.Int32
PX.Objects.IN.DAC.INSiteZone.ZoneID : Edm.Int32 [key] "ZoneID"
PX.Objects.IN.DAC.INSiteZone.Name : Edm.String "Zone"
PX.Objects.IN.DAC.INSiteZone.Descr : Edm.String "Description"
PX.Objects.IN.DAC.INSiteZone.ParentID : Edm.Int32 "Parent Zone"
PX.Objects.IN.DAC.INSiteZone.SortOrder : Edm.Int32
PX.Objects.IN.DAC.INSiteZone.NoteID : Edm.Guid
PX.Objects.IN.DAC.INSiteZone.NoteText : Edm.String "Note Text"
PX.Objects.IN.DAC.INSiteZone.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INSiteZone.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INSiteZone.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INSiteZone.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INSiteZone.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INSiteZone.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INSiteZone.tstamp : Edm.Binary
PX.Objects.IN.DAC.INSiteZone.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INSiteZone.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INSiteZone.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.DAC.INSiteZone.INSiteZoneByZoneID -> PX.Objects.IN.DAC.INSiteZone (ZoneID=ParentID)
PX.Objects.IN.DAC.INSiteZone.INSiteZoneCollection -> Collection(PX.Objects.IN.DAC.INSiteZone)
PX.Objects.IN.DAC.INSiteZone.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.DAC.INSiteZone.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.DAC.INSiteZone.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.IN.DAC.INSiteZone.INSitePlanningStrategyDetailCollection -> Collection(PX.Objects.IN.DAC.INSitePlanningStrategyDetail)
PX.Objects.IN.DAC.INSiteZone.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.DAC.INSiteZone.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)

# PX.Objects.IN.DAC.INTransferDemandLine (EntityType)

Label: "Transfer Demand Line"
Key: RecordID
Entity sets: PX_Objects_IN_DAC_INTransferDemandLine, TransferDemandLine, INTransferDemandLine
Non-filterable, non-selectable: InventoryDescr, UnitOfHandling, BaseUOM, NoteText

PX.Objects.IN.DAC.INTransferDemandLine.RecordID : Edm.Guid [key] "RecordID"
PX.Objects.IN.DAC.INTransferDemandLine.OperationType : Edm.String "Operation Type"
PX.Objects.IN.DAC.INTransferDemandLine.CreationDate : Edm.DateTimeOffset "Creation Date"
PX.Objects.IN.DAC.INTransferDemandLine.ExecutionDate : Edm.DateTimeOffset "Execution Date"
PX.Objects.IN.DAC.INTransferDemandLine.SourceZoneID : Edm.Int32 "Source Zone"
PX.Objects.IN.DAC.INTransferDemandLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.DAC.INTransferDemandLine.InventoryDescr : Edm.String "Description"
PX.Objects.IN.DAC.INTransferDemandLine.LotSerialNbr : Edm.String "Lot/Serial Nbr."
PX.Objects.IN.DAC.INTransferDemandLine.UOM : Edm.String "UOM"
PX.Objects.IN.DAC.INTransferDemandLine.UnitOfHandling : Edm.String "Unit of Handling"
PX.Objects.IN.DAC.INTransferDemandLine.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.IN.DAC.INTransferDemandLine.BaseQty : Edm.Decimal [required] "Qty. in Base UOM"
PX.Objects.IN.DAC.INTransferDemandLine.BaseUOM : Edm.String "Base UOM"
PX.Objects.IN.DAC.INTransferDemandLine.PickedQty : Edm.Decimal [required] "Picked Qty."
PX.Objects.IN.DAC.INTransferDemandLine.BasePickedQty : Edm.Decimal [required] "Picked Qty. in Base UOM"
PX.Objects.IN.DAC.INTransferDemandLine.MovedQty : Edm.Decimal [required] "Moved Qty."
PX.Objects.IN.DAC.INTransferDemandLine.BaseMovedQty : Edm.Decimal [required] "Moved Qty. in Base UOM"
PX.Objects.IN.DAC.INTransferDemandLine.DestinationZoneID : Edm.Int32 "Destination Zone"
PX.Objects.IN.DAC.INTransferDemandLine.Status : Edm.String "Status"
PX.Objects.IN.DAC.INTransferDemandLine.TransferListNbr : Edm.String "Transfer List"
PX.Objects.IN.DAC.INTransferDemandLine.UserID : Edm.Guid "User"
PX.Objects.IN.DAC.INTransferDemandLine.PlanID : Edm.Int64
PX.Objects.IN.DAC.INTransferDemandLine.NoteID : Edm.Guid
PX.Objects.IN.DAC.INTransferDemandLine.NoteText : Edm.String "Note Text"
PX.Objects.IN.DAC.INTransferDemandLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INTransferDemandLine.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INTransferDemandLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INTransferDemandLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INTransferDemandLine.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INTransferDemandLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INTransferDemandLine.tstamp : Edm.Binary
PX.Objects.IN.DAC.INTransferDemandLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.DAC.INTransferDemandLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INTransferDemandLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INTransferDemandLine.INLocationBySourceLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.DAC.INTransferDemandLine.INLocationByDestinationLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.DAC.INTransferDemandLine.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.DAC.INTransferDemandLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.DAC.INTransferDemandLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.IN.DAC.INTransferDemandLine.INSiteZoneBySourceZoneID -> PX.Objects.IN.DAC.INSiteZone (SourceZoneID=ZoneID)
PX.Objects.IN.DAC.INTransferDemandLine.INSiteZoneByDestinationZoneID -> PX.Objects.IN.DAC.INSiteZone (DestinationZoneID=ZoneID)
PX.Objects.IN.DAC.INTransferDemandLine.INSiteZoneBySiteID -> PX.Objects.IN.DAC.INSiteZone (SourceZoneID=ZoneID)
PX.Objects.IN.DAC.INTransferDemandLine.INTransferListByTransferListNbr -> PX.Objects.IN.DAC.INTransferList (TransferListNbr=ListNbr)
PX.Objects.IN.DAC.INTransferDemandLine.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)

# PX.Objects.IN.DAC.INTransferDemandPutAwaySplit (EntityType)

Label: "Transfer Demand Put Away Split"
Key: SplitLineNbr, TransferDemandLineID
Entity sets: PX_Objects_IN_DAC_INTransferDemandPutAwaySplit, TransferDemandPutAwaySplit, INTransferDemandPutAwaySplit
Non-filterable, non-selectable: NoteText

PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.TransferDemandLineID : Edm.Guid [key]
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.SplitLineNbr : Edm.Int32 [key] "Split Line Number"
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.DestinationZoneID : Edm.Int32 "Destination Zone"
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.UOM : Edm.String "UOM"
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.MovedQty : Edm.Decimal [required] "Moved Qty."
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.BaseMovedQty : Edm.Decimal [required] "Moved Qty. in Base UOM"
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.LotSerialNbr : Edm.String "Lot/Serial Nbr."
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.PlanID : Edm.Int64
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.NoteID : Edm.Guid
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.NoteText : Edm.String "Note Text"
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.tstamp : Edm.Binary
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.INLocationByDestinationLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.INSiteZoneByDestinationZoneID -> PX.Objects.IN.DAC.INSiteZone (DestinationZoneID=ZoneID)
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.INSiteZoneBySiteID -> PX.Objects.IN.DAC.INSiteZone (DestinationZoneID=ZoneID)
PX.Objects.IN.DAC.INTransferDemandPutAwaySplit.INTransferDemandLineByTransferDemandLineID -> PX.Objects.IN.DAC.INTransferDemandLine (TransferDemandLineID=RecordID)

# PX.Objects.IN.DAC.INTransferList (EntityType)

Label: "Transfer List"
Key: ListNbr
Entity sets: PX_Objects_IN_DAC_INTransferList, TransferList, INTransferList

PX.Objects.IN.DAC.INTransferList.ListNbr : Edm.String [key] "List Nbr."
PX.Objects.IN.DAC.INTransferList.Status : Edm.String "Status"
PX.Objects.IN.DAC.INTransferList.CreationDate : Edm.DateTimeOffset "Creation Date"
PX.Objects.IN.DAC.INTransferList.TransferType : Edm.String "Transfer Type"
PX.Objects.IN.DAC.INTransferList.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.IN.DAC.INTransferList.CompletionDate : Edm.DateTimeOffset "Completion Date"
PX.Objects.IN.DAC.INTransferList.TransferNbr : Edm.String "Transfer Nbr."
PX.Objects.IN.DAC.INTransferList.UserID : Edm.Guid "User"
PX.Objects.IN.DAC.INTransferList.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.INTransferList.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.INTransferList.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INTransferList.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.INTransferList.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.INTransferList.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.INTransferList.tstamp : Edm.Binary
PX.Objects.IN.DAC.INTransferList.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.INTransferList.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.INTransferList.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.DAC.INTransferList.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)

# PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected (EntityType)

Label: "INItemLotSerialAttributesHeaderSelected"
Key: InventoryID, LocationID, LotSerialNbr, SiteID
Entity sets: PX_Objects_IN_DAC_Projections_INItemLotSerialAttributesHeaderSelected, INItemLotSerialAttributesHeaderSelected
Non-filterable, non-selectable: QtySelected

PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.LotSerClassID : Edm.String
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.MfgLotSerialNbr : Edm.String "Manufacturer Lot/Serial Nbr."
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.Descr : Edm.String "Description"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.LocationID : Edm.Int32 [key]
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.LocationCD : Edm.String "Location"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.QtyHardAvail : Edm.Decimal "Qty. Available For Shipping"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.ExpireDate : Edm.DateTimeOffset
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.NoteID : Edm.Guid
PX.Objects.IN.DAC.Projections.INItemLotSerialAttributesHeaderSelected.INLotSerClassByLotSerClassID -> PX.Objects.IN.INLotSerClass (LotSerClassID=LotSerClassID)

# PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType (EntityType)

Label: "IN Location Status by Cost Layer Type"
Key: CostLayerType, InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_DAC_Projections_INLocationStatusByCostLayerType, INLocationStatusbyCostLayerType

PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.CostLayerType : Edm.String [key] "Cost Layer Type"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyOnHand : Edm.Decimal
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyHardAvail : Edm.Decimal "Qty. Hard Available"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyActual : Edm.Decimal "Qty. Available for Issue"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyInTransit : Edm.Decimal "Qty. In-Transit"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyInTransitToSO : Edm.Decimal "Qty. In Transit to SO"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyPOPrepared : Edm.Decimal "Qty. PO Prepared"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyPOOrders : Edm.Decimal "Qty. Purchase Orders"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyPOReceipts : Edm.Decimal "Qty. Purchase Receipts"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtySOBackOrdered : Edm.Decimal "Qty. SO Backordered"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtySOPrepared : Edm.Decimal "Qty. SO Prepared"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtySOBooked : Edm.Decimal "Qty. SO Booked"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtySOShipped : Edm.Decimal "Qty. SO Shipped"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtySOShipping : Edm.Decimal "Qty. SO Shipping"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyINIssues : Edm.Decimal "Qty On Inventory Issues"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyINReceipts : Edm.Decimal "Qty On Inventory Receipts"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyINAssemblyDemand : Edm.Decimal "Qty Demanded by Kit Assembly"
PX.Objects.IN.DAC.Projections.INLocationStatusByCostLayerType.QtyINAssemblySupply : Edm.Decimal "Qty On Kit Assembly"

# PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType (EntityType)

Label: "IN Lot/Serial Cost Status by Cost Layer Type"
Key: CostLayerType, InventoryID, LotSerialNbr, SiteID, SubItemID
Entity sets: PX_Objects_IN_DAC_Projections_INLotSerialCostStatusByCostLayerType, INLotSerialCostStatusbyCostLayerType
Non-filterable, non-selectable: UnitCost

PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.InventoryID : Edm.Int32 [key]
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.SubItemID : Edm.Int32 [key]
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.SiteID : Edm.Int32 [key]
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.LotSerialNbr : Edm.String [key] "Lot/Serial Number"
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.CostLayerType : Edm.String [key]
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.QtyOnHand : Edm.Decimal
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.TotalCost : Edm.Decimal
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.DecPlPrcCst : Edm.Int16
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.UnitCost : Edm.Decimal
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.INSiteByCostSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.DAC.Projections.INLotSerialCostStatusByCostLayerType.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType (EntityType)

Label: "IN Lot/Serial Status by Cost Layer Type"
Key: CostLayerType, InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID
Entity sets: PX_Objects_IN_DAC_Projections_INLotSerialStatusByCostLayerType, INLotSerialStatusbyCostLayerType

PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.CostLayerType : Edm.String [key] "Cost Layer Type"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.ExpireDate : Edm.DateTimeOffset "Expiry Date"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyOnHand : Edm.Decimal
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyHardAvail : Edm.Decimal "Qty. Hard Available"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyActual : Edm.Decimal "Qty. Available for Issue"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyInTransit : Edm.Decimal "Qty. In-Transit"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyInTransitToSO : Edm.Decimal "Qty. In Transit to SO"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyPOPrepared : Edm.Decimal "Qty. PO Prepared"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyPOOrders : Edm.Decimal "Qty. Purchase Orders"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyPOReceipts : Edm.Decimal "Qty. Purchase Receipts"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtySOBackOrdered : Edm.Decimal "Qty. SO Backordered"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtySOPrepared : Edm.Decimal "Qty. SO Prepared"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtySOBooked : Edm.Decimal "Qty. SO Booked"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtySOShipped : Edm.Decimal "Qty. SO Shipped"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtySOShipping : Edm.Decimal "Qty. SO Shipping"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyINIssues : Edm.Decimal "Qty On Inventory Issues"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyINReceipts : Edm.Decimal "Qty On Inventory Receipts"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyINAssemblyDemand : Edm.Decimal "Qty Demanded by Kit Assembly"
PX.Objects.IN.DAC.Projections.INLotSerialStatusByCostLayerType.QtyINAssemblySupply : Edm.Decimal "Qty On Kit Assembly"

# PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType (EntityType)

Label: "IN Site Cost Status by Cost Layer Type"
Key: CostLayerType, InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_IN_DAC_Projections_INSiteCostStatusByCostLayerType, INSiteCostStatusbyCostLayerType
Non-filterable, non-selectable: UnitCost

PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.InventoryID : Edm.Int32 [key]
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.SubItemID : Edm.Int32 [key]
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.SiteID : Edm.Int32 [key]
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.CostLayerType : Edm.String [key]
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.QtyOnHand : Edm.Decimal
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.TotalCost : Edm.Decimal
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.DecPlPrcCst : Edm.Int16
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.UnitCost : Edm.Decimal
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.INSiteByCostSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.DAC.Projections.INSiteCostStatusByCostLayerType.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType (EntityType)

Label: "IN Site Status by Cost Layer Type"
Key: CostLayerType, InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_IN_DAC_Projections_INSiteStatusByCostLayerType, INSiteStatusbyCostLayerType

PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.CostLayerType : Edm.String [key] "Cost Layer Type"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyOnHand : Edm.Decimal
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyNotAvail : Edm.Decimal "Qty. Not Available"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyHardAvail : Edm.Decimal "Qty. Hard Available"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyActual : Edm.Decimal "Qty. Available for Issue"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyInTransit : Edm.Decimal "Qty. In-Transit"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyInTransitToSO : Edm.Decimal "Qty. In Transit to SO"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyPOPrepared : Edm.Decimal "Qty. PO Prepared"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyPOOrders : Edm.Decimal "Qty. Purchase Orders"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyPOReceipts : Edm.Decimal "Qty. Purchase Receipts"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtySOBackOrdered : Edm.Decimal "Qty. SO Backordered"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtySOPrepared : Edm.Decimal "Qty. SO Prepared"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtySOBooked : Edm.Decimal "Qty. SO Booked"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtySOShipped : Edm.Decimal "Qty. SO Shipped"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtySOShipping : Edm.Decimal "Qty. SO Shipping"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyINIssues : Edm.Decimal "Qty On Inventory Issues"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyINReceipts : Edm.Decimal "Qty On Inventory Receipts"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyINAssemblyDemand : Edm.Decimal "Qty Demanded by Kit Assembly"
PX.Objects.IN.DAC.Projections.INSiteStatusByCostLayerType.QtyINAssemblySupply : Edm.Decimal "Qty On Kit Assembly"

# PX.Objects.IN.DAC.WarehouseReference (EntityType)

Key: PortalSetupID, SiteID
Entity sets: PX_Objects_IN_DAC_WarehouseReference

PX.Objects.IN.DAC.WarehouseReference.SiteID : Edm.Int32 [key] "SiteID"
PX.Objects.IN.DAC.WarehouseReference.PortalSetupID : Edm.String [key] "PortalSetupID"
PX.Objects.IN.DAC.WarehouseReference.tstamp : Edm.Binary
PX.Objects.IN.DAC.WarehouseReference.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.DAC.WarehouseReference.CreatedByScreenID : Edm.String
PX.Objects.IN.DAC.WarehouseReference.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.WarehouseReference.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.DAC.WarehouseReference.LastModifiedByScreenID : Edm.String
PX.Objects.IN.DAC.WarehouseReference.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.DAC.WarehouseReference.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.DAC.WarehouseReference.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.DAC.WarehouseReference.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.IN.GS1UOMSetup (EntityType)

Label: "GS1 Unit Setup"
Singletons: PX_Objects_IN_GS1UOMSetup, GS1UnitSetup, GS1UOMSetup

PX.Objects.IN.GS1UOMSetup.Kilogram : Edm.String "Kilogram"
PX.Objects.IN.GS1UOMSetup.Pound : Edm.String "Pound"
PX.Objects.IN.GS1UOMSetup.Ounce : Edm.String "Ounce"
PX.Objects.IN.GS1UOMSetup.TroyOunce : Edm.String "Troy Ounce"
PX.Objects.IN.GS1UOMSetup.Metre : Edm.String "Metre"
PX.Objects.IN.GS1UOMSetup.Inch : Edm.String "Inch"
PX.Objects.IN.GS1UOMSetup.Foot : Edm.String "Foot"
PX.Objects.IN.GS1UOMSetup.Yard : Edm.String "Yard"
PX.Objects.IN.GS1UOMSetup.SqrMetre : Edm.String "Square Metre"
PX.Objects.IN.GS1UOMSetup.SqrInch : Edm.String "Square Inch"
PX.Objects.IN.GS1UOMSetup.SqrFoot : Edm.String "Square Foot"
PX.Objects.IN.GS1UOMSetup.SqrYard : Edm.String "Square Yard"
PX.Objects.IN.GS1UOMSetup.CubicMetre : Edm.String "Cubic Metre"
PX.Objects.IN.GS1UOMSetup.CubicInch : Edm.String "Cubic Inch"
PX.Objects.IN.GS1UOMSetup.CubicFoot : Edm.String "Cubic Foot"
PX.Objects.IN.GS1UOMSetup.CubicYard : Edm.String "Cubic Yard"
PX.Objects.IN.GS1UOMSetup.Litre : Edm.String "Litre"
PX.Objects.IN.GS1UOMSetup.Quart : Edm.String "Quart"
PX.Objects.IN.GS1UOMSetup.GallonUS : Edm.String "Gallon U.S."
PX.Objects.IN.GS1UOMSetup.KilogramPerSqrMetre : Edm.String "Kilogram per Square Metre"
PX.Objects.IN.GS1UOMSetup.tstamp : Edm.Binary
PX.Objects.IN.GS1UOMSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.GS1UOMSetup.CreatedByScreenID : Edm.String
PX.Objects.IN.GS1UOMSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.GS1UOMSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.GS1UOMSetup.LastModifiedByScreenID : Edm.String
PX.Objects.IN.GS1UOMSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.GS1UOMSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.GS1UOMSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.GS1UOMSetup.INUnitByKilogram -> PX.Objects.IN.INUnit (Kilogram=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByPound -> PX.Objects.IN.INUnit (Pound=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByOunce -> PX.Objects.IN.INUnit (Ounce=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByTroyOunce -> PX.Objects.IN.INUnit (TroyOunce=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByMetre -> PX.Objects.IN.INUnit (Metre=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByInch -> PX.Objects.IN.INUnit (Inch=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByFoot -> PX.Objects.IN.INUnit (Foot=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByYard -> PX.Objects.IN.INUnit (Yard=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitBySqrMetre -> PX.Objects.IN.INUnit (SqrMetre=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitBySqrInch -> PX.Objects.IN.INUnit (SqrInch=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitBySqrFoot -> PX.Objects.IN.INUnit (SqrFoot=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitBySqrYard -> PX.Objects.IN.INUnit (SqrYard=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByCubicMetre -> PX.Objects.IN.INUnit (CubicMetre=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByCubicInch -> PX.Objects.IN.INUnit (CubicInch=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByCubicFoot -> PX.Objects.IN.INUnit (CubicFoot=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByCubicYard -> PX.Objects.IN.INUnit (CubicYard=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByLitre -> PX.Objects.IN.INUnit (Litre=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByQuart -> PX.Objects.IN.INUnit (Quart=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByGallonUS -> PX.Objects.IN.INUnit (GallonUS=FromUnit)
PX.Objects.IN.GS1UOMSetup.INUnitByKilogramPerSqrMetre -> PX.Objects.IN.INUnit (KilogramPerSqrMetre=FromUnit)

# PX.Objects.IN.INABCCode (EntityType)

Label: "IN ABC Code"
Key: ABCCodeID
Entity sets: PX_Objects_IN_INABCCode, INABCCode

PX.Objects.IN.INABCCode.ABCCodeID : Edm.String [key] "ABC Code"
PX.Objects.IN.INABCCode.Descr : Edm.String "Description"
PX.Objects.IN.INABCCode.CountsPerYear : Edm.Int16 "Counts Per Year"
PX.Objects.IN.INABCCode.MaxCountInaccuracyPct : Edm.Decimal "Max. Count Inaccuracy %"
PX.Objects.IN.INABCCode.ABCPct : Edm.Decimal "ABC Code %"
PX.Objects.IN.INABCCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INABCCode.CreatedByScreenID : Edm.String
PX.Objects.IN.INABCCode.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INABCCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INABCCode.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INABCCode.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INABCCode.tstamp : Edm.Binary
PX.Objects.IN.INABCCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INABCCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INABCCode.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INABCCode.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INABCCode.INPIClassCollection -> Collection(PX.Objects.IN.INPIClass)

# PX.Objects.IN.INAvailabilityScheme (EntityType)

Label: "Availability Calculation Rule"
Key: AvailabilitySchemeID
Entity sets: PX_Objects_IN_INAvailabilityScheme, AvailabilityCalculationRule, INAvailabilityScheme

PX.Objects.IN.INAvailabilityScheme.AvailabilitySchemeID : Edm.String [key] "Availability Calculation Rule"
PX.Objects.IN.INAvailabilityScheme.Description : Edm.String "Description"
PX.Objects.IN.INAvailabilityScheme.InclQtySOReverse : Edm.Boolean [required] "Include Qty. on Sales Returns"
PX.Objects.IN.INAvailabilityScheme.InclQtySOBackOrdered : Edm.Boolean [required] "Deduct Qty. on Back Orders"
PX.Objects.IN.INAvailabilityScheme.InclQtySOPrepared : Edm.Boolean [required] "Deduct Qty. on Sales Prepared"
PX.Objects.IN.INAvailabilityScheme.InclQtySOBooked : Edm.Boolean [required] "Deduct Qty. on Sales Orders"
PX.Objects.IN.INAvailabilityScheme.InclQtySOShipped : Edm.Boolean [required] "Deduct Qty. Shipped"
PX.Objects.IN.INAvailabilityScheme.InclQtySOShipping : Edm.Boolean [required] "Deduct Qty. Allocated"
PX.Objects.IN.INAvailabilityScheme.InclQtyInTransit : Edm.Boolean "Include Qty. in Transit"
PX.Objects.IN.INAvailabilityScheme.InclQtyPOReceipts : Edm.Boolean "Include Qty. on PO Receipts"
PX.Objects.IN.INAvailabilityScheme.InclQtyPOPrepared : Edm.Boolean [required] "Include Qty. on Purchase Prepared"
PX.Objects.IN.INAvailabilityScheme.InclQtyPOOrders : Edm.Boolean "Include Qty. on Purchase Orders"
PX.Objects.IN.INAvailabilityScheme.InclQtyFixedSOPO : Edm.Boolean [required] "Include Qty. of Purchase for SO and SO to Purchase"
PX.Objects.IN.INAvailabilityScheme.InclQtyINIssues : Edm.Boolean [required] "Deduct Qty. on Issues"
PX.Objects.IN.INAvailabilityScheme.InclQtyINReceipts : Edm.Boolean "Include Qty. on Receipts"
PX.Objects.IN.INAvailabilityScheme.InclQtyINAssemblyDemand : Edm.Boolean [required] "Deduct Qty. of Kit Assembly Demand"
PX.Objects.IN.INAvailabilityScheme.InclQtyINAssemblySupply : Edm.Boolean "Include Qty. of Kit Assembly Supply"
PX.Objects.IN.INAvailabilityScheme.InclQtyProductionSupplyPrepared : Edm.Boolean [required] "Include Qty. of Production Supply Prepared"
PX.Objects.IN.INAvailabilityScheme.InclQtyProductionSupply : Edm.Boolean "Include Qty. of Production Supply"
PX.Objects.IN.INAvailabilityScheme.InclQtyProductionDemandPrepared : Edm.Boolean [required] "Deduct Qty. on Production Demand Prepared"
PX.Objects.IN.INAvailabilityScheme.InclQtyProductionDemand : Edm.Boolean "Deduct Qty. on Production Demand"
PX.Objects.IN.INAvailabilityScheme.InclQtyProductionAllocated : Edm.Boolean "Deduct Qty. on Production Allocated"
PX.Objects.IN.INAvailabilityScheme.tstamp : Edm.Binary
PX.Objects.IN.INAvailabilityScheme.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INAvailabilityScheme.CreatedByScreenID : Edm.String
PX.Objects.IN.INAvailabilityScheme.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INAvailabilityScheme.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INAvailabilityScheme.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INAvailabilityScheme.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INAvailabilityScheme.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INAvailabilityScheme.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INAvailabilityScheme.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)

# PX.Objects.IN.INCart (EntityType)

Label: "IN Cart"
Key: CartCD, SiteID
Entity sets: PX_Objects_IN_INCart, INCart
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INCart.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INCart.CartID : Edm.Int32 "CartID"
PX.Objects.IN.INCart.CartCD : Edm.String [key] "Cart ID"
PX.Objects.IN.INCart.Descr : Edm.String "Description"
PX.Objects.IN.INCart.Active : Edm.Boolean [required] "Active"
PX.Objects.IN.INCart.AssignedNbrOfTotes : Edm.Int32 [required] "Assigned Number of Totes"
PX.Objects.IN.INCart.NoteID : Edm.Guid
PX.Objects.IN.INCart.NoteText : Edm.String "Note Text"
PX.Objects.IN.INCart.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INCart.CreatedByScreenID : Edm.String
PX.Objects.IN.INCart.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INCart.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INCart.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INCart.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INCart.tstamp : Edm.Binary
PX.Objects.IN.INCart.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INCart.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INCart.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INCart.SOPickerCollection -> Collection(PX.Objects.SO.SOPicker)
PX.Objects.IN.INCart.SOPickListEntryToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOPickListEntryToCartSplitLink)
PX.Objects.IN.INCart.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)
PX.Objects.IN.INCart.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.INCart.INToteCollection -> Collection(PX.Objects.IN.INTote)
PX.Objects.IN.INCart.INRegisterCartCollection -> Collection(PX.Objects.IN.DAC.INRegisterCart)
PX.Objects.IN.INCart.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.Objects.IN.INCart.SOCartShipmentCollection -> Collection(PX.Objects.SO.SOCartShipment)
PX.Objects.IN.INCart.POCartReceiptCollection -> Collection(PX.Objects.PO.POCartReceipt)
PX.Objects.IN.INCart.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.IN.INCart.StoragePlaceCollection -> Collection(PX.Objects.IN.StoragePlace)

# PX.Objects.IN.INCartContentByLocation (EntityType)

Label: "IN Cart Content by Location"
Key: InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INCartContentByLocation, INCartContentbyLocation

PX.Objects.IN.INCartContentByLocation.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INCartContentByLocation.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INCartContentByLocation.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INCartContentByLocation.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INCartContentByLocation.BaseQty : Edm.Decimal
PX.Objects.IN.INCartContentByLocation.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INCartContentByLocation.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INCartContentByLocation.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INCartContentByLocation.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INCartContentByLocation.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID, LocationID=LocationID)

# PX.Objects.IN.INCartContentByLotSerial (EntityType)

Label: "IN Cart Content by Lot/Serial Nbr."
Key: InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID
Entity sets: PX_Objects_IN_INCartContentByLotSerial, INCartContentbyLotSerialNbr, INCartContentByLotSerial

PX.Objects.IN.INCartContentByLotSerial.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INCartContentByLotSerial.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INCartContentByLotSerial.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INCartContentByLotSerial.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INCartContentByLotSerial.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.INCartContentByLotSerial.BaseQty : Edm.Decimal
PX.Objects.IN.INCartContentByLotSerial.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INCartContentByLotSerial.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INCartContentByLotSerial.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INCartContentByLotSerial.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INCartContentByLotSerial.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID, LocationID=LocationID)
PX.Objects.IN.INCartContentByLotSerial.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID, LocationID=LocationID, LotSerialNbr=LotSerialNbr)

# PX.Objects.IN.INCartSplit (EntityType)

Label: "IN Cart Split"
Key: CartID, SiteID, SplitLineNbr
Entity sets: PX_Objects_IN_INCartSplit, INCartSplit

PX.Objects.IN.INCartSplit.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INCartSplit.CartID : Edm.Int32 [key] "Cart ID"
PX.Objects.IN.INCartSplit.SplitLineNbr : Edm.Int32 [key] "Split Line Number"
PX.Objects.IN.INCartSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INCartSplit.UOM : Edm.String "UOM"
PX.Objects.IN.INCartSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.IN.INCartSplit.BaseQty : Edm.Decimal [required]
PX.Objects.IN.INCartSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INCartSplit.CreatedByScreenID : Edm.String
PX.Objects.IN.INCartSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INCartSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INCartSplit.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INCartSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INCartSplit.tstamp : Edm.Binary
PX.Objects.IN.INCartSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INCartSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INCartSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INCartSplit.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.IN.INCartSplit.INLocationByFromLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INCartSplit.INLocationByToLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INCartSplit.INLocationBySiteID -> PX.Objects.IN.INLocation (SiteID=SiteID)
PX.Objects.IN.INCartSplit.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INCartSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INCartSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.IN.INCartSplit.SOPickListEntryToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOPickListEntryToCartSplitLink)
PX.Objects.IN.INCartSplit.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)
PX.Objects.IN.INCartSplit.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.Objects.IN.INCartSplit.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)

# PX.Objects.IN.INCategory (EntityType)

Label: "Item Sales Category"
Key: CategoryID
Entity sets: PX_Objects_IN_INCategory, ItemSalesCategory, INCategory
Non-filterable, non-selectable: TempChildID, TempParentID, NoteText

PX.Objects.IN.INCategory.CategoryID : Edm.Int32 [key] "Category ID"
PX.Objects.IN.INCategory.Description : Edm.String "Description"
PX.Objects.IN.INCategory.ParentID : Edm.Int32 [required] "Parent Category"
PX.Objects.IN.INCategory.TempChildID : Edm.Int32
PX.Objects.IN.INCategory.TempParentID : Edm.Int32
PX.Objects.IN.INCategory.NoteID : Edm.Guid
PX.Objects.IN.INCategory.NoteText : Edm.String "Note Text"
PX.Objects.IN.INCategory.SortOrder : Edm.Int32
PX.Objects.IN.INCategory.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INCategory.CreatedByScreenID : Edm.String
PX.Objects.IN.INCategory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INCategory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INCategory.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INCategory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INCategory.tstamp : Edm.Binary
PX.Objects.IN.INCategory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INCategory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INCategory.INCategoryByParentID -> PX.Objects.IN.INCategory (ParentID=CategoryID)
PX.Objects.IN.INCategory.INCategoryCollection -> Collection(PX.Objects.IN.INCategory)
PX.Objects.IN.INCategory.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)

# PX.Objects.IN.INComponent (EntityType)

Label: "Deferred Revenue Components"
Key: ComponentID, InventoryID
Entity sets: PX_Objects_IN_INComponent, DeferredRevenueComponents, INComponent

PX.Objects.IN.INComponent.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INComponent.ComponentID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INComponent.DeferredCode : Edm.String "Deferral Code"
PX.Objects.IN.INComponent.DefaultTerm : Edm.Decimal [required] "Default Term"
PX.Objects.IN.INComponent.DefaultTermUOM : Edm.String "Default Term UOM"
PX.Objects.IN.INComponent.OverrideDefaultTerm : Edm.Boolean [required] "Override Default Term"
PX.Objects.IN.INComponent.Percentage : Edm.Decimal [required] "Percentage"
PX.Objects.IN.INComponent.UOM : Edm.String "UOM"
PX.Objects.IN.INComponent.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.IN.INComponent.FixedAmt : Edm.Decimal "Fixed Amount"
PX.Objects.IN.INComponent.AmtOption : Edm.String "Allocation Method"
PX.Objects.IN.INComponent.AmtOptionASC606 : Edm.String "Allocation Method"
PX.Objects.IN.INComponent.tstamp : Edm.Binary
PX.Objects.IN.INComponent.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INComponent.CreatedByScreenID : Edm.String
PX.Objects.IN.INComponent.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INComponent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INComponent.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INComponent.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INComponent.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INComponent.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.IN.INComponent.DRDeferredCodeByDeferredCode -> PX.Objects.DR.DRDeferredCode (DeferredCode=DeferredCodeID)
PX.Objects.IN.INComponent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INComponent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INComponent.INUnitByComponentID -> PX.Objects.IN.INUnit (UOM=FromUnit, ComponentID=InventoryID)
PX.Objects.IN.INComponent.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INComponent.SubBySalesSubID -> PX.Objects.GL.Sub

# PX.Objects.IN.INComponentTran (EntityType)

Label: "IN Component"
BaseType: PX.Objects.IN.INTran
Key: DocType, LineNbr, RefNbr (inherited from PX.Objects.IN.INTran)
Entity sets: PX_Objects_IN_INComponentTran, INComponent1, INComponentTran

PX.Objects.IN.INComponentTran.ProjectID : Edm.Int32
PX.Objects.IN.INComponentTran.SiteID : Edm.Int32

# PX.Objects.IN.INComponentTranSplit (EntityType)

Label: "IN Component Split"
BaseType: PX.Objects.IN.INTranSplit
Key: DocType, LineNbr, RefNbr, SplitLineNbr (inherited from PX.Objects.IN.INTranSplit)
Entity sets: PX_Objects_IN_INComponentTranSplit, INComponentSplit, INComponentTranSplit

# PX.Objects.IN.INCostCenter (EntityType)

Label: "IN Cost Center"
Key: CostCenterID
Entity sets: PX_Objects_IN_INCostCenter, INCostCenter

PX.Objects.IN.INCostCenter.CostCenterID : Edm.Int32 [key]
PX.Objects.IN.INCostCenter.CostCenterCD : Edm.String "Cost Center ID"
PX.Objects.IN.INCostCenter.CostLayerType : Edm.String
PX.Objects.IN.INCostCenter.SOOrderType : Edm.String "Sales Order Type"
PX.Objects.IN.INCostCenter.SOOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.IN.INCostCenter.SOOrderLineNbr : Edm.Int32 "Sales Order Line Nbr."
PX.Objects.IN.INCostCenter.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INCostCenter.CreatedByScreenID : Edm.String
PX.Objects.IN.INCostCenter.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INCostCenter.tstamp : Edm.Binary
PX.Objects.IN.INCostCenter.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.IN.INCostCenter.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.IN.INCostCenter.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.IN.INCostCenter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INCostCenter.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOOrderLineNbr=LineNbr)
PX.Objects.IN.INCostCenter.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INCostCenter.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.INCostCenter.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INCostCenter.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.INCostCenter.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INCostCenter.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.INCostCenter.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.INCostCenter.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INCostCenter.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INCostCenter.INSiteStatusSelectedCollection -> Collection(PX.Objects.IN.INSiteStatusSelected)
PX.Objects.IN.INCostCenter.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)

# PX.Objects.IN.INCostStatus (EntityType)

Label: "IN Cost Status"
Key: CostID
Entity sets: PX_Objects_IN_INCostStatus, INCostStatus
Non-filterable, non-selectable: OrigQtyOnHand, OverrideOrigQty, PositiveTranQty

PX.Objects.IN.INCostStatus.CostID : Edm.Int64 [key]
PX.Objects.IN.INCostStatus.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INCostStatus.CostSiteID : Edm.Int32 "Cost Site"
PX.Objects.IN.INCostStatus.CostLayerType : Edm.String
PX.Objects.IN.INCostStatus.LayerType : Edm.String
PX.Objects.IN.INCostStatus.ValMethod : Edm.String
PX.Objects.IN.INCostStatus.ReceiptNbr : Edm.String "Receipt Nbr."
PX.Objects.IN.INCostStatus.ReceiptDate : Edm.DateTimeOffset "Receipt Date"
PX.Objects.IN.INCostStatus.LotSerialNbr : Edm.String "Lot/Serial Number"
PX.Objects.IN.INCostStatus.OrigQty : Edm.Decimal [required]
PX.Objects.IN.INCostStatus.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INCostStatus.OrigQtyOnHand : Edm.Decimal
PX.Objects.IN.INCostStatus.OverrideOrigQty : Edm.Boolean
PX.Objects.IN.INCostStatus.PositiveTranQty : Edm.Decimal
PX.Objects.IN.INCostStatus.UnitCost : Edm.Decimal [required]
PX.Objects.IN.INCostStatus.TotalCost : Edm.Decimal [required] "Total Cost"
PX.Objects.IN.INCostStatus.tstamp : Edm.Binary
PX.Objects.IN.INCostStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INCostStatus.INItemSiteByCostSiteID -> PX.Objects.IN.INItemSite (InventoryID=InventoryID, CostSiteID=SiteID)
PX.Objects.IN.INCostStatus.INSiteByCostSiteID -> PX.Objects.IN.INSite (CostSiteID=SiteID)
PX.Objects.IN.INCostStatus.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INCostStatus.INSubItemByCostSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INCostStatus.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.IN.INCostStatus.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.IN.INCostStatus.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INCostStatus.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)

# PX.Objects.IN.INCostStatusSummary (EntityType)

Label: "IN Cost Status Summary"
BaseType: PX.Objects.IN.INCostStatus
Key: CostID (inherited from PX.Objects.IN.INCostStatus)
Entity sets: PX_Objects_IN_INCostStatusSummary, INCostStatusSummary

# PX.Objects.IN.INCostStatusTransitLineSummary (EntityType)

Label: "IN Cost Status"
BaseType: PX.Objects.IN.INCostStatus
Key: CostID (inherited from PX.Objects.IN.INCostStatus)
Entity sets: PX_Objects_IN_INCostStatusTransitLineSummary

# PX.Objects.IN.INCostSubItemXRef (EntityType)

Key: CostSubItemID, SubItemID
Entity sets: PX_Objects_IN_INCostSubItemXRef

PX.Objects.IN.INCostSubItemXRef.SubItemID : Edm.Int32 [key]
PX.Objects.IN.INCostSubItemXRef.CostSubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INCostSubItemXRef.tstamp : Edm.Binary
PX.Objects.IN.INCostSubItemXRef.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.IN.INItemBox (EntityType)

Label: "IN Item Box"
Key: BoxID, InventoryID
Entity sets: PX_Objects_IN_INItemBox, INItemBox
Non-filterable, non-selectable: MaxQty, NoteText

PX.Objects.IN.INItemBox.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INItemBox.BoxID : Edm.String [key] "Box ID"
PX.Objects.IN.INItemBox.UOM : Edm.String "UOM"
PX.Objects.IN.INItemBox.Qty : Edm.Decimal [required] "Qty."
PX.Objects.IN.INItemBox.BaseQty : Edm.Decimal [required]
PX.Objects.IN.INItemBox.MaxQty : Edm.Decimal "Max. Qty"
PX.Objects.IN.INItemBox.NoteID : Edm.Guid
PX.Objects.IN.INItemBox.NoteText : Edm.String "Note Text"
PX.Objects.IN.INItemBox.tstamp : Edm.Binary
PX.Objects.IN.INItemBox.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemBox.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemBox.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemBox.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemBox.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemBox.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemBox.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemBox.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemBox.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemBox.CSBoxByBoxID -> PX.Objects.CS.CSBox (BoxID=BoxID)
PX.Objects.IN.INItemBox.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.IN.INItemBoxEx (EntityType)

Label: "IN Item Box"
BaseType: PX.Objects.IN.INItemBox
Key: BoxID, InventoryID (inherited from PX.Objects.IN.INItemBox)
Entity sets: PX_Objects_IN_INItemBoxEx

PX.Objects.IN.INItemBoxEx.Description : Edm.String "Description"
PX.Objects.IN.INItemBoxEx.MaxWeight : Edm.Decimal "Max. Weight"
PX.Objects.IN.INItemBoxEx.BoxWeight : Edm.Decimal "Box Weight"
PX.Objects.IN.INItemBoxEx.MaxVolume : Edm.Decimal "Max Volume"
PX.Objects.IN.INItemBoxEx.Length : Edm.Decimal "Length"
PX.Objects.IN.INItemBoxEx.Width : Edm.Decimal "Width"
PX.Objects.IN.INItemBoxEx.Height : Edm.Decimal "Height"

# PX.Objects.IN.INItemCategory (EntityType)

Label: "Item Sales Category by Item"
Key: CategoryID, InventoryID
Entity sets: PX_Objects_IN_INItemCategory, ItemSalesCategorybyItem, INItemCategory
Non-filterable, non-selectable: CategorySelected

PX.Objects.IN.INItemCategory.CategoryID : Edm.Int32 [key] "Category"
PX.Objects.IN.INItemCategory.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemCategory.CategorySelected : Edm.Boolean "Category Selected"
PX.Objects.IN.INItemCategory.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemCategory.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemCategory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemCategory.tstamp : Edm.Binary
PX.Objects.IN.INItemCategory.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemCategory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemCategory.INCategoryByCategoryID -> PX.Objects.IN.INCategory (CategoryID=CategoryID)

# PX.Objects.IN.INItemClass (EntityType)

Label: "Item Class"
Key: ItemClassCD
Entity sets: PX_Objects_IN_INItemClass, ItemClass, INItemClass
Non-filterable, non-selectable: ParentItemClassID, NoteText, Included, ItemClassStrID, ItemClassCDWildcard, SampleID, SampleDescription, Secured, DeletedDatabaseRecord

PX.Objects.IN.INItemClass.ItemClassID : Edm.Int32 "ItemClassID"
PX.Objects.IN.INItemClass.ItemClassCD : Edm.String [key] "Class ID"
PX.Objects.IN.INItemClass.Descr : Edm.String "Description"
PX.Objects.IN.INItemClass.StkItem : Edm.Boolean "Stock Item"
PX.Objects.IN.INItemClass.ParentItemClassID : Edm.Int32
PX.Objects.IN.INItemClass.NegQty : Edm.Boolean [required] "Allow Negative Quantity"
PX.Objects.IN.INItemClass.AvailabilitySchemeID : Edm.String "Availability Calculation Rule"
PX.Objects.IN.INItemClass.ValMethod : Edm.String "Valuation Method"
PX.Objects.IN.INItemClass.BaseUnit : Edm.String "Base Unit"
PX.Objects.IN.INItemClass.SalesUnit : Edm.String "Sales Unit"
PX.Objects.IN.INItemClass.PurchaseUnit : Edm.String "Purchase Unit"
PX.Objects.IN.INItemClass.DecimalBaseUnit : Edm.Boolean [required] "Divisible Unit"
PX.Objects.IN.INItemClass.DecimalSalesUnit : Edm.Boolean [required] "Divisible Unit"
PX.Objects.IN.INItemClass.DecimalPurchaseUnit : Edm.Boolean [required] "Divisible Unit"
PX.Objects.IN.INItemClass.PostClassID : Edm.String "Posting Class"
PX.Objects.IN.INItemClass.LotSerClassID : Edm.String "Lot/Serial Class"
PX.Objects.IN.INItemClass.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.IN.INItemClass.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.IN.INItemClass.DeferredCode : Edm.String "Deferral Code"
PX.Objects.IN.INItemClass.ItemType : Edm.String "Item Type"
PX.Objects.IN.INItemClass.PriceClassID : Edm.String "Price Class"
PX.Objects.IN.INItemClass.PriceWorkgroupID : Edm.Int32 "Price Workgroup"
PX.Objects.IN.INItemClass.PriceManagerID : Edm.Int32 "Price Manager"
PX.Objects.IN.INItemClass.MinGrossProfitPct : Edm.Decimal [required] "Min. Markup %"
PX.Objects.IN.INItemClass.MarkupPct : Edm.Decimal "Markup %"
PX.Objects.IN.INItemClass.NoteID : Edm.Guid
PX.Objects.IN.INItemClass.NoteText : Edm.String "Note Text"
PX.Objects.IN.INItemClass.DemandCalculation : Edm.String "Demand Calculation"
PX.Objects.IN.INItemClass.CommodityCodeType : Edm.String "Commodity Code Type"
PX.Objects.IN.INItemClass.HSTariffCode : Edm.String "Commodity Code"
PX.Objects.IN.INItemClass.UndershipThreshold : Edm.Decimal [required] "Undership Threshold (%)"
PX.Objects.IN.INItemClass.OvershipThreshold : Edm.Decimal [required] "Overship Threshold (%)"
PX.Objects.IN.INItemClass.CountryOfOrigin : Edm.String "Country Of Origin"
PX.Objects.IN.INItemClass.PostToExpenseAccount : Edm.String "Post Cost to Expenses On"
PX.Objects.IN.INItemClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemClass.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemClass.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemClass.tstamp : Edm.Binary
PX.Objects.IN.INItemClass.GroupMask : Edm.Binary
PX.Objects.IN.INItemClass.Included : Edm.Boolean "Included"
PX.Objects.IN.INItemClass.ItemClassStrID : Edm.String "ItemClassStrID"
PX.Objects.IN.INItemClass.ItemClassCDWildcard : Edm.String "ItemClassCDWildcard"
PX.Objects.IN.INItemClass.SampleID : Edm.String
PX.Objects.IN.INItemClass.SampleDescription : Edm.String
PX.Objects.IN.INItemClass.ReplenishmentSource : Edm.String "Source"
PX.Objects.IN.INItemClass.GenerationRuleCntr : Edm.Int32 [required]
PX.Objects.IN.INItemClass.ExportToExternal : Edm.Boolean "Export to External System"
PX.Objects.IN.INItemClass.Secured : Edm.Boolean "Secured"
PX.Objects.IN.INItemClass.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.IN.INItemClass.EPEmployeeByPriceManagerID -> PX.Objects.EP.EPEmployee (PriceManagerID=BAccountID)
PX.Objects.IN.INItemClass.ContactByPriceManagerID -> PX.Objects.CR.Contact (PriceManagerID=ContactID)
PX.Objects.IN.INItemClass.DRDeferredCodeByDeferredCode -> PX.Objects.DR.DRDeferredCode (DeferredCode=DeferredCodeID)
PX.Objects.IN.INItemClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemClass.EPCompanyTreeByPriceWorkgroupID -> PX.TM.EPCompanyTree (PriceWorkgroupID=WorkGroupID)
PX.Objects.IN.INItemClass.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.IN.INItemClass.CountryByCountryOfOrigin -> PX.Objects.CS.Country (CountryOfOrigin=CountryID)
PX.Objects.IN.INItemClass.CSAttributeGroupByDefaultColumnMatrixAttributeID -> PX.Objects.CS.CSAttributeGroup
PX.Objects.IN.INItemClass.CSAttributeGroupByDefaultRowMatrixAttributeID -> PX.Objects.CS.CSAttributeGroup
PX.Objects.IN.INItemClass.INAvailabilitySchemeByAvailabilitySchemeID -> PX.Objects.IN.INAvailabilityScheme (AvailabilitySchemeID=AvailabilitySchemeID)
PX.Objects.IN.INItemClass.INAvailabilitySchemeByAtpAvailabilitySchemeID -> PX.Objects.IN.INAvailabilityScheme
PX.Objects.IN.INItemClass.INLotSerClassByLotSerClassID -> PX.Objects.IN.INLotSerClass (LotSerClassID=LotSerClassID)
PX.Objects.IN.INItemClass.INPostClassByPostClassID -> PX.Objects.IN.INPostClass (PostClassID=PostClassID)
PX.Objects.IN.INItemClass.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.IN.INItemClass.INUnitByBaseUnit -> PX.Objects.IN.INUnit (BaseUnit=FromUnit)
PX.Objects.IN.INItemClass.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)
PX.Objects.IN.INItemClass.INReplenishmentItemCollection -> Collection(PX.Objects.IN.INReplenishmentItem)
PX.Objects.IN.INItemClass.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INItemClass.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.IN.INItemClass.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.IN.INItemClass.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.IN.INItemClass.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.INItemClass.SOOrderSiteStatusSelectedCollection -> Collection(PX.Objects.SO.SOOrderSiteStatusSelected)
PX.Objects.IN.INItemClass.SOSetupCrossSellExcludedItemClassesCollection -> Collection(PX.Objects.SO.SOSetupCrossSellExcludedItemClasses)
PX.Objects.IN.INItemClass.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.Objects.IN.INItemClass.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.IN.INItemClass.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.IN.INItemClass.INPIClassItemClassCollection -> Collection(PX.Objects.IN.INPIClassItemClass)
PX.Objects.IN.INItemClass.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.IN.INItemClass.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.IN.INItemClass.INItemClassSiteCollection -> Collection(PX.Objects.IN.DAC.INItemClassSite)
PX.Objects.IN.INItemClass.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.IN.INItemClass.BCMatrixOptionsMappingCollection -> Collection(PX.Commerce.Objects.BCMatrixOptionsMapping)
PX.Objects.IN.INItemClass.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.IN.INItemClass.AMEstimateClassCollection -> Collection(PX.Objects.AM.AMEstimateClass)
PX.Objects.IN.INItemClass.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.INItemClass.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.INItemClass.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.IN.INItemClass.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.IN.INItemClass.FSModelTemplateComponentCollection -> Collection(PX.Objects.FS.FSModelTemplateComponent)
PX.Objects.IN.INItemClass.ARAddItemSelectedCollection -> Collection(PX.Objects.AR.ARAddItemSelected)
PX.Objects.IN.INItemClass.APAddItemSelectedCollection -> Collection(PX.Objects.AP.APAddItemSelected)
PX.Objects.IN.INItemClass.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.IN.INItemClass.SelectedProdMatlCollection -> Collection(PX.Objects.AM.SelectedProdMatl)
PX.Objects.IN.INItemClass.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.IN.INItemClass.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.IN.INItemClass.SoldInventoryItemCollection -> Collection(PX.Objects.FS.SoldInventoryItem)
PX.Objects.IN.INItemClass.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.INItemClass.INSiteStatusSelectedCollection -> Collection(PX.Objects.IN.INSiteStatusSelected)
PX.Objects.IN.INItemClass.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.IN.INItemClass.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)
PX.Objects.IN.INItemClass.SOInvoiceSiteStatusSelectedCollection -> Collection(PX.Objects.SO.SOInvoiceSiteStatusSelected)
PX.Objects.IN.INItemClass.RQInventoryItemCollection -> Collection(PX.Objects.RQ.RQInventoryItem)
PX.Objects.IN.INItemClass.RQSiteStatusSelectedCollection -> Collection(PX.Objects.RQ.RQSiteStatusSelected)
PX.Objects.IN.INItemClass.POSiteStatusSelectedCollection -> Collection(PX.Objects.PO.POSiteStatusSelected)
PX.Objects.IN.INItemClass.MNMaterialListSiteStatusSelectedCollection -> Collection(PX.Objects.MN.MNMaterialListSiteStatusSelected)

# PX.Objects.IN.INItemClassCurySettings (EntityType)

Label: "Item Class Currency Settings"
Key: CuryID, ItemClassID
Entity sets: PX_Objects_IN_INItemClassCurySettings, ItemClassCurrencySettings, INItemClassCurySettings

PX.Objects.IN.INItemClassCurySettings.ItemClassID : Edm.Int32 [key] "Item Class"
PX.Objects.IN.INItemClassCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.IN.INItemClassCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemClassCurySettings.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemClassCurySettings.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INItemClassCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemClassCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemClassCurySettings.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INItemClassCurySettings.tstamp : Edm.Binary
PX.Objects.IN.INItemClassCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemClassCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemClassCurySettings.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.INItemClassCurySettings.INSiteByDfltSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INItemClassCurySettings.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.IN.INItemClassCurySettings.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)

# PX.Objects.IN.INItemClassRep (EntityType)

Label: "Item Class Replenishment"
Key: CuryID, ItemClassID, ReplenishmentClassID
Entity sets: PX_Objects_IN_INItemClassRep, ItemClassReplenishment, INItemClassRep
Non-filterable, non-selectable: ServiceLevelPct

PX.Objects.IN.INItemClassRep.ItemClassID : Edm.Int32 [key] "Class ID"
PX.Objects.IN.INItemClassRep.CuryID : Edm.String [key] "Currency"
PX.Objects.IN.INItemClassRep.ReplenishmentClassID : Edm.String [key] "Replenishment Class ID"
PX.Objects.IN.INItemClassRep.ReplenishmentMethod : Edm.String "Method"
PX.Objects.IN.INItemClassRep.ReplenishmentSource : Edm.String "Source"
PX.Objects.IN.INItemClassRep.ReplenishmentPolicyID : Edm.String "Seasonality"
PX.Objects.IN.INItemClassRep.TransferLeadTime : Edm.Int16 [required] "Transfer Lead Time"
PX.Objects.IN.INItemClassRep.TransferERQ : Edm.Decimal "Transfer ERQ"
PX.Objects.IN.INItemClassRep.ServiceLevel : Edm.Decimal "Service Level"
PX.Objects.IN.INItemClassRep.ServiceLevelPct : Edm.Decimal "Service Level (%)"
PX.Objects.IN.INItemClassRep.ForecastModelType : Edm.String "Demand Forecast Model"
PX.Objects.IN.INItemClassRep.ForecastPeriodType : Edm.String "Forecast Period Type"
PX.Objects.IN.INItemClassRep.HistoryDepth : Edm.Int32 [required] "Periods to Analyze"
PX.Objects.IN.INItemClassRep.ESSmoothingConstantL : Edm.Decimal "Level Smoothing Constant"
PX.Objects.IN.INItemClassRep.ESSmoothingConstantT : Edm.Decimal "Trend Smoothing Constant"
PX.Objects.IN.INItemClassRep.ESSmoothingConstantS : Edm.Decimal "Seasonality Smoothing Constant"
PX.Objects.IN.INItemClassRep.AutoFitModel : Edm.Boolean [required] "Auto Fit Model"
PX.Objects.IN.INItemClassRep.LaunchDate : Edm.DateTimeOffset "Launch Date"
PX.Objects.IN.INItemClassRep.TerminationDate : Edm.DateTimeOffset "Termination Date"
PX.Objects.IN.INItemClassRep.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemClassRep.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemClassRep.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemClassRep.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemClassRep.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemClassRep.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemClassRep.tstamp : Edm.Binary
PX.Objects.IN.INItemClassRep.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemClassRep.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemClassRep.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.INItemClassRep.INReplenishmentClassByReplenishmentClassID -> PX.Objects.IN.INReplenishmentClass (ReplenishmentClassID=ReplenishmentClassID)
PX.Objects.IN.INItemClassRep.INReplenishmentPolicyByReplenishmentPolicyID -> PX.Objects.IN.INReplenishmentPolicy (ReplenishmentPolicyID=ReplenishmentPolicyID)
PX.Objects.IN.INItemClassRep.INSiteByReplenishmentSourceSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INItemClassRep.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.IN.INItemClassRep.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)

# PX.Objects.IN.INItemCost (EntityType)

Label: "Item Cost Statistics"
Key: CuryID, InventoryID
Entity sets: PX_Objects_IN_INItemCost, ItemCostStatistics, INItemCost

PX.Objects.IN.INItemCost.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INItemCost.CuryID : Edm.String [key]
PX.Objects.IN.INItemCost.LastCost : Edm.Decimal [required] "Last Cost"
PX.Objects.IN.INItemCost.LastCostDate : Edm.DateTimeOffset
PX.Objects.IN.INItemCost.TotalCost : Edm.Decimal [required]
PX.Objects.IN.INItemCost.QtyOnHand : Edm.Decimal [required]
PX.Objects.IN.INItemCost.AvgCost : Edm.Decimal "Average Cost"
PX.Objects.IN.INItemCost.MinCost : Edm.Decimal [required] "Min. Cost"
PX.Objects.IN.INItemCost.MaxCost : Edm.Decimal [required] "Max. Cost"
PX.Objects.IN.INItemCost.TranUnitCost : Edm.Decimal
PX.Objects.IN.INItemCost.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemCost.InventoryItemCurySettingsByCuryID -> PX.Objects.IN.InventoryItemCurySettings (InventoryID=InventoryID, CuryID=CuryID)
PX.Objects.IN.INItemCost.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.IN.INItemCost.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.IN.INItemCost.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.IN.INItemCost.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.IN.INItemCost.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.IN.INItemCost.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.IN.INItemCost.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.IN.INItemCost.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.IN.INItemCost.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.IN.INItemCost.FSAppointmentLogExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentLogExtItemLine)
PX.Objects.IN.INItemCost.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.IN.INItemCost.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.IN.INItemCost.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.IN.INItemCost.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.IN.INItemCost.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.INItemCost.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.INItemCost.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.IN.INItemCost.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.IN.INItemCost.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.IN.INItemCost.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.IN.INItemCost.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.IN.INItemCost.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.IN.INItemCost.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INItemCost.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INItemCost.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INItemCost.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.INItemCost.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.IN.INItemCost.INMatrixExcludedDataCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
PX.Objects.IN.INItemCost.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.IN.INItemCost.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.Objects.IN.INItemCost.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.IN.INItemCost.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.IN.INItemCost.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.IN.INItemCost.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.IN.INItemCost.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.INItemCost.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.IN.INItemCost.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INItemCost.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.INItemCost.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INItemCost.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.IN.INItemCost.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.INItemCost.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.INItemCost.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INItemCost.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.IN.INItemCost.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.IN.INItemCost.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.IN.INItemCost.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INItemCost.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.IN.INItemCost.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.INItemCost.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.IN.INItemCost.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.IN.INItemCost.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.IN.INItemCost.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INItemCost.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.IN.INItemCost.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.IN.INItemCost.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.IN.INItemCost.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.IN.INItemCost.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INItemCost.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.IN.INItemCost.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.IN.INItemCost.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.IN.INItemCost.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.Objects.IN.INItemCost.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.IN.INItemCost.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.IN.INItemCost.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.IN.INItemCost.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.IN.INItemCost.InventoryPostingBatchDetailCollection -> Collection(PX.Objects.FS.InventoryPostingBatchDetail)
PX.Objects.IN.INItemCost.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.IN.INItemCost.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.INItemCost.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.INItemCost.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.INItemCost.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.INItemCost.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INItemCost.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.IN.INItemCost.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INItemCost.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.INItemCost.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.INItemCost.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INItemCost.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INItemCost.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.IN.INItemCost.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.IN.INItemCost.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.Objects.IN.INItemCost.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.IN.INItemCost.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.IN.INItemCost.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.IN.INItemCost.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.IN.INItemCost.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.IN.INItemCost.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INItemCost.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.IN.INItemCost.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.IN.INItemCost.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.IN.INItemCost.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.IN.INItemCost.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.IN.INItemCost.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.IN.INItemCost.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.IN.INItemCost.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.IN.INItemCost.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.Objects.IN.INItemCost.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.INItemCost.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.INItemCost.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.IN.INItemCost.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.IN.INItemCost.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.IN.INItemCost.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.INItemCost.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)
PX.Objects.IN.INItemCost.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.Objects.IN.INItemCost.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.IN.INItemCost.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.IN.INItemCost.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.Objects.IN.INItemCost.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.IN.INItemCost.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.IN.INItemCost.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.IN.INItemCost.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.Objects.IN.INItemCost.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.INItemCost.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.IN.INItemCost.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.INItemCost.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.IN.INItemCost.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.INItemCost.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.IN.INItemCost.InventoryItemLotSerNumValCollection -> Collection(PX.Objects.IN.InventoryItemLotSerNumVal)
PX.Objects.IN.INItemCost.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.IN.INItemCost.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.IN.INItemCost.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.IN.INItemCost.INRelatedInventoryUserFeedbackCollection -> Collection(PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback)
PX.Objects.IN.INItemCost.INAttributeDescriptionGroupCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup)
PX.Objects.IN.INItemCost.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.Objects.IN.INItemCost.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.IN.INItemCost.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.IN.INItemCost.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.INItemCost.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.IN.INItemCost.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)
PX.Objects.IN.INItemCost.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.Objects.IN.INItemCost.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.IN.INItemCost.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.IN.INItemCost.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.IN.INItemCost.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.Objects.IN.INItemCost.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.IN.INItemCost.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.IN.INItemCost.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.IN.INItemCost.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.IN.INItemCost.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.IN.INItemCost.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.IN.INItemCost.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.Objects.IN.INItemCost.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.Objects.IN.INItemCost.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.IN.INItemCost.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.IN.INItemCost.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.IN.INItemCost.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.IN.INItemCost.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.IN.INItemCost.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.IN.INItemCost.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.IN.INItemCost.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Objects.IN.INItemCost.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.Objects.IN.INItemCost.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.IN.INItemCost.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.IN.INItemCost.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.INItemCost.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.INItemCost.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.INItemCost.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.IN.INItemCost.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.IN.INItemCost.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.IN.INItemCost.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.IN.INItemCost.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.IN.INItemCost.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.IN.INItemCost.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.INItemCost.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.Objects.IN.INItemCost.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.IN.INItemCost.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.IN.INItemCost.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.IN.INItemCost.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.IN.INItemCost.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.IN.INItemCost.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.INItemCost.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.INItemCost.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.INItemCost.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.IN.INItemCost.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.IN.INItemCost.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.IN.INItemCost.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.INItemCost.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.INItemCost.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.INItemCost.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.IN.INItemCost.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INItemCost.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.IN.INItemCost.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.IN.INItemCost.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.IN.INItemCost.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.IN.INItemCost.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.Objects.IN.INItemCost.FSServiceInventoryItemCollection -> Collection(PX.Objects.FS.FSServiceInventoryItem)
PX.Objects.IN.INItemCost.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)
PX.Objects.IN.INItemCost.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)
PX.Objects.IN.INItemCost.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.Objects.IN.INItemCost.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)
PX.Objects.IN.INItemCost.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INItemCost.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.IN.INItemCost.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.IN.INItemCost.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.IN.INItemCost.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.IN.INItemCost.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.IN.INItemCost.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.IN.INItemCost.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.IN.INItemCost.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.IN.INItemCost.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.IN.INItemCost.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.IN.INItemCost.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.INItemCost.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.IN.INItemCost.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.IN.INItemCost.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.IN.INItemCost.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.IN.INItemCost.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INItemCost.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.IN.INItemCost.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.IN.INItemCost.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.IN.INItemCost.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.IN.INItemCost.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.IN.INItemCost.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.IN.INItemCost.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.IN.INItemCost.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.IN.INItemCost.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.IN.INItemCost.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.IN.INItemCost.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.IN.INItemCost.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.IN.INItemCost.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.INItemCost.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.IN.INItemCost.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.IN.INItemCost.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.INItemCost.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.IN.INItemCost.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.IN.INItemCost.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.IN.INItemCost.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.IN.INItemCost.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.IN.INItemCost.POLineRCollection -> Collection(PX.Objects.PO.POLineR)
PX.Objects.IN.INItemCost.PMItemRateCollection -> Collection(PX.Objects.PM.PMItemRate)
PX.Objects.IN.INItemCost.PMProjectARTranPostDetailCollection -> Collection(PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail)
PX.Objects.IN.INItemCost.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.INItemCost.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.INItemCost.INItemLotSerialCollection -> Collection(PX.Objects.IN.INItemLotSerial)
PX.Objects.IN.INItemCost.INItemSalesHistCollection -> Collection(PX.Objects.IN.INItemSalesHist)
PX.Objects.IN.INItemCost.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.IN.INItemCost.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.IN.INItemCost.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.IN.INItemCost.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.IN.INItemCost.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.INItemCost.INSubItemSegmentValueCollection -> Collection(PX.Objects.IN.INSubItemSegmentValue)
PX.Objects.IN.INItemCost.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INItemCost.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.INItemCost.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.INItemCost.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.IN.INItemCost.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.INItemCost.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.INItemCost.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.IN.INItemCost.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.INItemCost.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.IN.INItemCost.RelatedItemCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItem)
PX.Objects.IN.INItemCost.INItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeader)
PX.Objects.IN.INItemCost.BCInventoryFileUrlsCollection -> Collection(PX.Commerce.Objects.BCInventoryFileUrls)
PX.Objects.IN.INItemCost.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.IN.INItemCost.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.INItemCost.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.IN.INItemCost.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.IN.INItemCost.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.IN.INItemCost.SchedulerEmployeeInventoryItemCollection -> Collection(PX.Objects.FS.SchedulerEmployeeInventoryItem)
PX.Objects.IN.INItemCost.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)
PX.Objects.IN.INItemCost.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.IN.INItemCost.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.IN.INItemCost.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.IN.INItemCost.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)
PX.Objects.IN.INItemCost.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.IN.INItemCost.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.IN.INItemCost.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.IN.INItemCost.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.IN.INItemCost.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.IN.INItemCost.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.IN.INItemCost.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.IN.INItemCost.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.IN.INItemCost.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.IN.INItemCost.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.IN.INItemCost.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.IN.INItemCost.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.IN.INItemCost.CurrencyRateCollection -> Collection(PX.Objects.CM.CurrencyRate)
PX.Objects.IN.INItemCost.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.IN.INItemCost.LedgerCollection -> Collection(PX.Objects.GL.Ledger)
PX.Objects.IN.INItemCost.CABankTranRuleCollection -> Collection(PX.Objects.CA.CABankTranRule)
PX.Objects.IN.INItemCost.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.IN.INItemCost.CRCustomerClassCollection -> Collection(PX.Objects.CR.CRCustomerClass)
PX.Objects.IN.INItemCost.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.IN.INItemCost.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.IN.INItemCost.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.IN.INItemCost.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.IN.INItemCost.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.IN.INItemCost.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.IN.INItemCost.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.IN.INItemCost.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.IN.INItemCost.SVTicketCollection -> Collection(PX.Objects.SV.SVTicket)
PX.Objects.IN.INItemCost.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.IN.INItemCost.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.IN.INItemCost.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.IN.INItemCost.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.IN.INItemCost.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.IN.INItemCost.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.IN.INItemCost.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.IN.INItemCost.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.IN.INItemCost.CurrencyInfoCollection -> Collection(PX.Objects.CM.CurrencyInfo)
PX.Objects.IN.INItemCost.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.IN.INItemCost.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.IN.INItemCost.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.IN.INItemCost.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.IN.INItemCost.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.IN.INItemCost.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.Objects.IN.INItemCost.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.IN.INItemCost.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.Objects.IN.INItemCost.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.IN.INItemCost.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.IN.INItemCost.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.IN.INItemCost.CABankTranHeaderCollection -> Collection(PX.Objects.CA.CABankTranHeader)
PX.Objects.IN.INItemCost.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.IN.INItemCost.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.IN.INItemCost.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.IN.INItemCost.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.Objects.IN.INItemCost.CashForecastTranCollection -> Collection(PX.Objects.CA.CashForecastTran)
PX.Objects.IN.INItemCost.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.IN.INItemCost.CCBatchCollection -> Collection(PX.Objects.CA.CCBatch)
PX.Objects.IN.INItemCost.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.IN.INItemCost.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.IN.INItemCost.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.Objects.IN.INItemCost.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.IN.INItemCost.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.IN.INItemCost.FSSalesPriceCollection -> Collection(PX.Objects.FS.FSSalesPrice)
PX.Objects.IN.INItemCost.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.IN.INItemCost.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.IN.INItemCost.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.IN.INItemCost.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.IN.INItemCost.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.IN.INItemCost.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.IN.INItemCost.AMConfigurationKeysCollection -> Collection(PX.Objects.AM.AMConfigurationKeys)
PX.Objects.IN.INItemCost.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.IN.INItemCost.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.IN.INItemCost.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.IN.INItemCost.CompanyCollection -> Collection(PX.Objects.GL.Company)
PX.Objects.IN.INItemCost.RQBudgetCollection -> Collection(PX.Objects.RQ.RQBudget)
PX.Objects.IN.INItemCost.RQRequestLineSelectCollection -> Collection(PX.Objects.RQ.RQRequestLineSelect)
PX.Objects.IN.INItemCost.BCPaymentMethodsCollection -> Collection(PX.Commerce.Objects.BCPaymentMethods)
PX.Objects.IN.INItemCost.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.IN.INItemCost.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.IN.INItemCost.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.IN.INItemCost.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.IN.INItemCost.PendingPPDARTaxAdjAppCollection -> Collection(PX.Objects.AR.PendingPPDARTaxAdjApp)
PX.Objects.IN.INItemCost.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.IN.INItemCost.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.IN.INItemCost.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.IN.INItemCost.POLinePMCollection -> Collection(PX.Objects.PM.POLinePM)
PX.Objects.IN.INItemCost.POOrderPMCollection -> Collection(PX.Objects.PM.POOrderPM)
PX.Objects.IN.INItemCost.VendorLocationCollection -> Collection(PX.Objects.PO.VendorLocation)

# PX.Objects.IN.INItemCostHist (EntityType)

Label: "IN Item Cost History"
Key: AccountID, CostSiteID, CostSubItemID, FinPeriodID, InventoryID, SubID
Entity sets: PX_Objects_IN_INItemCostHist, INItemCostHistory, INItemCostHist

PX.Objects.IN.INItemCostHist.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemCostHist.CostSubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemCostHist.CostSiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemCostHist.AccountID : Edm.Int32 [key]
PX.Objects.IN.INItemCostHist.SubID : Edm.Int32 [key]
PX.Objects.IN.INItemCostHist.FinPeriodID : Edm.String [key] "Fin. Period"
PX.Objects.IN.INItemCostHist.FinPtdCostIssued : Edm.Decimal [required] "Issued"
PX.Objects.IN.INItemCostHist.FinPtdCostReceived : Edm.Decimal [required] "Received"
PX.Objects.IN.INItemCostHist.FinBegCost : Edm.Decimal [required] "Beginning Cost"
PX.Objects.IN.INItemCostHist.FinYtdCost : Edm.Decimal [required] "Ending Cost"
PX.Objects.IN.INItemCostHist.FinPtdQtyIssued : Edm.Decimal [required] "Qty. Issued"
PX.Objects.IN.INItemCostHist.FinPtdQtyReceived : Edm.Decimal [required] "Qty. Received"
PX.Objects.IN.INItemCostHist.FinBegQty : Edm.Decimal [required] "Beginning Qty."
PX.Objects.IN.INItemCostHist.FinYtdQty : Edm.Decimal [required] "Ending Qty."
PX.Objects.IN.INItemCostHist.FinPtdCOGS : Edm.Decimal [required] "COGS"
PX.Objects.IN.INItemCostHist.FinPtdCOGSCredits : Edm.Decimal [required] "Credit Memos"
PX.Objects.IN.INItemCostHist.FinPtdCOGSDropShips : Edm.Decimal [required] "Drop ships"
PX.Objects.IN.INItemCostHist.FinPtdCostTransferIn : Edm.Decimal [required] "Transfer In"
PX.Objects.IN.INItemCostHist.FinPtdCostTransferOut : Edm.Decimal [required] "Transfer out"
PX.Objects.IN.INItemCostHist.FinPtdCostAssemblyIn : Edm.Decimal [required] "Assembly In"
PX.Objects.IN.INItemCostHist.FinPtdCostAssemblyOut : Edm.Decimal [required] "Assembly Out"
PX.Objects.IN.INItemCostHist.FinPtdCostAMAssemblyIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdCostAMAssemblyOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdCostAMAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdCostAMAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdCostAdjusted : Edm.Decimal "Adjusted"
PX.Objects.IN.INItemCostHist.FinPtdCostAdjustedZero : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdCostAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdCostAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdQtySales : Edm.Decimal [required] "Qty. Sales"
PX.Objects.IN.INItemCostHist.FinPtdQtyCreditMemos : Edm.Decimal [required] "Qty. Credit Memos"
PX.Objects.IN.INItemCostHist.FinPtdQtyDropShipSales : Edm.Decimal [required] "Qty. Drop ship Sales"
PX.Objects.IN.INItemCostHist.FinPtdQtyTransferIn : Edm.Decimal [required] "Qty. Transfer In"
PX.Objects.IN.INItemCostHist.FinPtdQtyTransferOut : Edm.Decimal [required] "Qty. Transfer Out"
PX.Objects.IN.INItemCostHist.FinPtdQtyAssemblyIn : Edm.Decimal [required] "Qty. Assembly In"
PX.Objects.IN.INItemCostHist.FinPtdQtyAssemblyOut : Edm.Decimal [required] "Qty. Assembly Out"
PX.Objects.IN.INItemCostHist.FinPtdQtyAMAssemblyIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdQtyAMAssemblyOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdQtyAMAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdQtyAMAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdQtyAdjusted : Edm.Decimal "Qty. Adjusted"
PX.Objects.IN.INItemCostHist.FinPtdQtyAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdQtyAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.FinPtdSales : Edm.Decimal [required] "Sales"
PX.Objects.IN.INItemCostHist.FinPtdCreditMemos : Edm.Decimal [required] "Credit Memos"
PX.Objects.IN.INItemCostHist.FinPtdDropShipSales : Edm.Decimal [required] "Drop ship Sales"
PX.Objects.IN.INItemCostHist.TranPtdCostReceived : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostIssued : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyReceived : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyIssued : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCOGS : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCOGSCredits : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCOGSDropShips : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostTransferIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostTransferOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAssemblyIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAssemblyOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAMAssemblyIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAMAssemblyOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAMAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAMAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAdjusted : Edm.Decimal
PX.Objects.IN.INItemCostHist.TranPtdCostAdjustedZero : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCostAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtySales : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyTransferIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyTransferOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyAssemblyIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyAssemblyOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyAMAssemblyIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyAMAssemblyOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyAMAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyAMAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyAdjusted : Edm.Decimal
PX.Objects.IN.INItemCostHist.TranPtdQtyAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdQtyAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdSales : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranPtdDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranBegCost : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranYtdCost : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranBegQty : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.TranYtdQty : Edm.Decimal [required]
PX.Objects.IN.INItemCostHist.tstamp : Edm.Binary
PX.Objects.IN.INItemCostHist.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemCostHist.INSiteByCostSiteID -> PX.Objects.IN.INSite (CostSiteID=SiteID)
PX.Objects.IN.INItemCostHist.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INItemCostHist.INSubItemByCostSubItemID -> PX.Objects.IN.INSubItem (CostSubItemID=SubItemID)
PX.Objects.IN.INItemCostHist.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.IN.INItemCostHist.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.IN.INItemCostHistByPeriod (EntityType)

Label: "IN Item Cost History by Period"
Key: AccountID, CostSiteID, CostSubItemID, FinPeriodID, InventoryID, SubID
Entity sets: PX_Objects_IN_INItemCostHistByPeriod, INItemCostHistorybyPeriod, INItemCostHistByPeriod

PX.Objects.IN.INItemCostHistByPeriod.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemCostHistByPeriod.CostSubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemCostHistByPeriod.CostSiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemCostHistByPeriod.AccountID : Edm.Int32 [key] "Account"
PX.Objects.IN.INItemCostHistByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.IN.INItemCostHistByPeriod.LastActivityPeriod : Edm.String
PX.Objects.IN.INItemCostHistByPeriod.FinPeriodID : Edm.String [key] "Fin. Period"
PX.Objects.IN.INItemCostHistByPeriod.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemCostHistByPeriod.INSiteByCostSiteID -> PX.Objects.IN.INSite (CostSiteID=SiteID)
PX.Objects.IN.INItemCostHistByPeriod.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INItemCostHistByPeriod.INSubItemByCostSubItemID -> PX.Objects.IN.INSubItem (CostSubItemID=SubItemID)
PX.Objects.IN.INItemCostHistByPeriod.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.IN.INItemLotSerial (EntityType)

Label: "Lot/Serial by Item"
Key: InventoryID, LotSerialNbr
Entity sets: PX_Objects_IN_INItemLotSerial, LotSerialbyItem, INItemLotSerial
Non-filterable, non-selectable: UpdateExpireDate, NoteText

PX.Objects.IN.INItemLotSerial.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemLotSerial.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.INItemLotSerial.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INItemLotSerial.QtyAvail : Edm.Decimal [required] "Qty. Available"
PX.Objects.IN.INItemLotSerial.QtyHardAvail : Edm.Decimal [required] "Qty. Hard Available"
PX.Objects.IN.INItemLotSerial.QtyActual : Edm.Decimal [required] "Qty. Available for Issue"
PX.Objects.IN.INItemLotSerial.QtyInTransit : Edm.Decimal [required]
PX.Objects.IN.INItemLotSerial.QtyOrig : Edm.Decimal
PX.Objects.IN.INItemLotSerial.QtyOnReceipt : Edm.Decimal [required]
PX.Objects.IN.INItemLotSerial.Preassigned : Edm.Boolean [required] "Pre-Assigned"
PX.Objects.IN.INItemLotSerial.ExpireDate : Edm.DateTimeOffset "Expiry Date"
PX.Objects.IN.INItemLotSerial.UpdateExpireDate : Edm.Boolean
PX.Objects.IN.INItemLotSerial.LotSerTrack : Edm.String
PX.Objects.IN.INItemLotSerial.LotSerAssign : Edm.String
PX.Objects.IN.INItemLotSerial.tstamp : Edm.Binary
PX.Objects.IN.INItemLotSerial.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemLotSerial.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INItemLotSerial.NoteID : Edm.Guid
PX.Objects.IN.INItemLotSerial.NoteText : Edm.String "Note Text"
PX.Objects.IN.INItemLotSerial.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemLotSerial.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INItemLotSerial.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.INItemLotSerial.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INItemLotSerial.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.INItemLotSerial.INItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeader)
PX.Objects.IN.INItemLotSerial.AMMTranLotSerialNbrAllCollection -> Collection(PX.Objects.AM.AMMTranLotSerialNbrAll)

# PX.Objects.IN.INItemLotSerialAttribute (EntityType)

Label: "Inventory Item Lot/Serial Attribute"
Key: AttributeID, InventoryID
Entity sets: PX_Objects_IN_INItemLotSerialAttribute, InventoryItemLotSerialAttribute, INItemLotSerialAttribute
Non-filterable, non-selectable: LotSerialNbr

PX.Objects.IN.INItemLotSerialAttribute.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INItemLotSerialAttribute.AttributeID : Edm.String [key] "Attribute ID"
PX.Objects.IN.INItemLotSerialAttribute.SortOrder : Edm.Int16 "Sort Order"
PX.Objects.IN.INItemLotSerialAttribute.Required : Edm.Boolean [required] "Required"
PX.Objects.IN.INItemLotSerialAttribute.IsActive : Edm.Boolean [required] "Active"
PX.Objects.IN.INItemLotSerialAttribute.LotSerialNbr : Edm.String
PX.Objects.IN.INItemLotSerialAttribute.tstamp : Edm.Binary
PX.Objects.IN.INItemLotSerialAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemLotSerialAttribute.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemLotSerialAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemLotSerialAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemLotSerialAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemLotSerialAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemLotSerialAttribute.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemLotSerialAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemLotSerialAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemLotSerialAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)

# PX.Objects.IN.INItemPlan (EntityType)

Label: "IN Item Plan"
Key: PlanID
Entity sets: PX_Objects_IN_INItemPlan, INItemPlan
Non-filterable, non-selectable: Active, IsTempLotSerial, IsSkippedWhenBackOrdered, IsTemporary

PX.Objects.IN.INItemPlan.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INItemPlan.PlanDate : Edm.DateTimeOffset "Planned On"
PX.Objects.IN.INItemPlan.PlanID : Edm.Int64 [key]
PX.Objects.IN.INItemPlan.FixedSource : Edm.String "Fixed Source"
PX.Objects.IN.INItemPlan.Active : Edm.Boolean "Active"
PX.Objects.IN.INItemPlan.PlanType : Edm.String "Plan Type"
PX.Objects.IN.INItemPlan.ExcludePlanLevel : Edm.Int32
PX.Objects.IN.INItemPlan.OrigPlanID : Edm.Int64
PX.Objects.IN.INItemPlan.OrigPlanType : Edm.String "Orig. Plan Type"
PX.Objects.IN.INItemPlan.OrigNoteID : Edm.Guid
PX.Objects.IN.INItemPlan.OrigPlanLevel : Edm.Int32
PX.Objects.IN.INItemPlan.IgnoreOrigPlan : Edm.Boolean [required]
PX.Objects.IN.INItemPlan.ProjectID : Edm.Int32
PX.Objects.IN.INItemPlan.TaskID : Edm.Int32
PX.Objects.IN.INItemPlan.IsTempLotSerial : Edm.Boolean
PX.Objects.IN.INItemPlan.VendorID : Edm.Int32
PX.Objects.IN.INItemPlan.VendorLocationID : Edm.Int32
PX.Objects.IN.INItemPlan.SupplyPlanID : Edm.Int64
PX.Objects.IN.INItemPlan.DemandPlanID : Edm.Int64
PX.Objects.IN.INItemPlan.OrigUOM : Edm.String
PX.Objects.IN.INItemPlan.UOM : Edm.String
PX.Objects.IN.INItemPlan.PlanQty : Edm.Decimal [required] "Planned Qty."
PX.Objects.IN.INItemPlan.RefNoteID : Edm.Guid
PX.Objects.IN.INItemPlan.Hold : Edm.Boolean "On Hold"
PX.Objects.IN.INItemPlan.Reverse : Edm.Boolean [required] "Reverse"
PX.Objects.IN.INItemPlan.IsSkippedWhenBackOrdered : Edm.Boolean
PX.Objects.IN.INItemPlan.tstamp : Edm.Binary
PX.Objects.IN.INItemPlan.BAccountID : Edm.Int32
PX.Objects.IN.INItemPlan.IsTemporary : Edm.Boolean
PX.Objects.IN.INItemPlan.RefEntityType : Edm.String
PX.Objects.IN.INItemPlan.CostCenterID : Edm.Int32 [required]
PX.Objects.IN.INItemPlan.CostLayerType : Edm.String
PX.Objects.IN.INItemPlan.KitInventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INItemPlan.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemPlan.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemPlan.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemPlan.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemPlan.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemPlan.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemPlan.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.IN.INItemPlan.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.IN.INItemPlan.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.IN.INItemPlan.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemPlan.InventoryItemByKitInventoryID -> PX.Objects.IN.InventoryItem (KitInventoryID=InventoryID)
PX.Objects.IN.INItemPlan.INItemPlanBySupplyPlanID -> PX.Objects.IN.INItemPlan (SupplyPlanID=PlanID)
PX.Objects.IN.INItemPlan.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=DemandPlanID)
PX.Objects.IN.INItemPlan.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemPlan.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemPlan.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INItemPlan.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.INItemPlan.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INItemPlan.INSiteBySourceSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INItemPlan.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INItemPlan.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID, VendorLocationID=LocationID)
PX.Objects.IN.INItemPlan.LocationByVendorID -> PX.Objects.CR.Location (VendorLocationID=LocationID, VendorID=BAccountID)
PX.Objects.IN.INItemPlan.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.IN.INItemPlan.INPlanTypeByPlanType -> PX.Objects.IN.INPlanType (PlanType=PlanType)
PX.Objects.IN.INItemPlan.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.IN.INItemPlan.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.INItemPlan.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.IN.INItemPlan.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.IN.INItemPlan.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.INItemPlan.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INItemPlan.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INItemPlan.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INItemPlan.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INItemPlan.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.INItemPlan.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.INItemPlan.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.INItemPlan.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INItemPlan.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INItemPlan.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.IN.INItemPlan.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)

# PX.Objects.IN.INItemRep (EntityType)

Label: "Item Replenishment Settings"
Key: CuryID, InventoryID, ReplenishmentClassID
Entity sets: PX_Objects_IN_INItemRep, ItemReplenishmentSettings, INItemRep
Non-filterable, non-selectable: ServiceLevelPct

PX.Objects.IN.INItemRep.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemRep.CuryID : Edm.String [key] "Currency"
PX.Objects.IN.INItemRep.ReplenishmentClassID : Edm.String [key] "Repl. Class"
PX.Objects.IN.INItemRep.ReplenishmentSource : Edm.String "Source"
PX.Objects.IN.INItemRep.ReplenishmentMethod : Edm.String "Method"
PX.Objects.IN.INItemRep.ReplenishmentPolicyID : Edm.String "Seasonality"
PX.Objects.IN.INItemRep.MaxShelfLife : Edm.Int32 [required] "Max. Shelf Life (Days)"
PX.Objects.IN.INItemRep.LaunchDate : Edm.DateTimeOffset "Launch Date"
PX.Objects.IN.INItemRep.TerminationDate : Edm.DateTimeOffset "Termination Date"
PX.Objects.IN.INItemRep.ServiceLevel : Edm.Decimal "Service Level"
PX.Objects.IN.INItemRep.ServiceLevelPct : Edm.Decimal "Service Level (%)"
PX.Objects.IN.INItemRep.SafetyStock : Edm.Decimal [required] "Safety Stock"
PX.Objects.IN.INItemRep.MinQty : Edm.Decimal [required] "Reorder Point"
PX.Objects.IN.INItemRep.MaxQty : Edm.Decimal [required] "Max Qty."
PX.Objects.IN.INItemRep.TransferERQ : Edm.Decimal "Transfer ERQ"
PX.Objects.IN.INItemRep.ForecastModelType : Edm.String "Demand Forecast Model"
PX.Objects.IN.INItemRep.ForecastPeriodType : Edm.String "Forecast Period Type"
PX.Objects.IN.INItemRep.HistoryDepth : Edm.Int32 "Periods to Analyze"
PX.Objects.IN.INItemRep.ESSmoothingConstantL : Edm.Decimal "Level Smoothing Constant"
PX.Objects.IN.INItemRep.ESSmoothingConstantT : Edm.Decimal "Trend Smoothing Constant"
PX.Objects.IN.INItemRep.ESSmoothingConstantS : Edm.Decimal "Seasonality Smoothing Constant"
PX.Objects.IN.INItemRep.AutoFitModel : Edm.Boolean [required] "Auto Fit Model"
PX.Objects.IN.INItemRep.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemRep.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemRep.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemRep.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemRep.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemRep.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemRep.tstamp : Edm.Binary
PX.Objects.IN.INItemRep.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemRep.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemRep.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemRep.INReplenishmentClassByReplenishmentClassID -> PX.Objects.IN.INReplenishmentClass (ReplenishmentClassID=ReplenishmentClassID)
PX.Objects.IN.INItemRep.INReplenishmentPolicyByReplenishmentPolicyID -> PX.Objects.IN.INReplenishmentPolicy (ReplenishmentPolicyID=ReplenishmentPolicyID)
PX.Objects.IN.INItemRep.INSiteByReplenishmentSourceSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INItemRep.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.IN.INItemRep.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.IN.INItemRep.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)

# PX.Objects.IN.INItemSalesHist (EntityType)

Label: "Item Sales History"
Key: CostSiteID, CostSubItemID, FinPeriodID, InventoryID
Entity sets: PX_Objects_IN_INItemSalesHist, ItemSalesHistory, INItemSalesHist

PX.Objects.IN.INItemSalesHist.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INItemSalesHist.CostSubItemID : Edm.Int32 [key]
PX.Objects.IN.INItemSalesHist.CostSiteID : Edm.Int32 [key]
PX.Objects.IN.INItemSalesHist.FinPeriodID : Edm.String [key]
PX.Objects.IN.INItemSalesHist.FinPtdCOGS : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinPtdCOGSCredits : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinPtdCOGSDropShips : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinPtdQtySales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinPtdQtyCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinPtdQtyDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinPtdSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinPtdCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinPtdDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdCOGS : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdCOGSCredits : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdCOGSDropShips : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdQtySales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdQtyCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdQtyDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.FinYtdDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdCOGS : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdCOGSCredits : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdCOGSDropShips : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdQtySales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdQtyCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdQtyDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranPtdDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdCOGS : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdCOGSCredits : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdCOGSDropShips : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdQtySales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdQtyCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdQtyDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdCreditMemos : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.TranYtdDropShipSales : Edm.Decimal [required]
PX.Objects.IN.INItemSalesHist.tstamp : Edm.Binary
PX.Objects.IN.INItemSalesHist.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemSalesHist.INSubItemByCostSubItemID -> PX.Objects.IN.INSubItem (CostSubItemID=SubItemID)

# PX.Objects.IN.INItemSite (EntityType)

Label: "Item/Warehouse Settings"
Key: InventoryID, SiteID
Entity sets: PX_Objects_IN_INItemSite, ItemWarehouseSettings, INItemSite
Non-filterable, non-selectable: LastCostDate, IsDefault, NoteText, ServiceLevelPct, DemandPerDaySTDEV, LeadTimeSTDEV

PX.Objects.IN.INItemSite.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemSite.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemSite.Active : Edm.Boolean "Active"
PX.Objects.IN.INItemSite.SiteStatus : Edm.String "Status"
PX.Objects.IN.INItemSite.OverrideInvtAcctSub : Edm.Boolean [required] "Override Inventory Account/Sub."
PX.Objects.IN.INItemSite.ValMethod : Edm.String
PX.Objects.IN.INItemSite.DfltSalesUnit : Edm.String "Sales Unit"
PX.Objects.IN.INItemSite.DfltPurchaseUnit : Edm.String "Purchase Unit"
PX.Objects.IN.INItemSite.LastStdCost : Edm.Decimal [required] "Last Cost"
PX.Objects.IN.INItemSite.PendingStdCost : Edm.Decimal [required] "Pending Cost"
PX.Objects.IN.INItemSite.PendingStdCostDate : Edm.DateTimeOffset "Pending Cost Date"
PX.Objects.IN.INItemSite.PendingStdCostReset : Edm.Boolean [required]
PX.Objects.IN.INItemSite.StdCost : Edm.Decimal [required] "Current Cost"
PX.Objects.IN.INItemSite.StdCostDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.IN.INItemSite.LastBasePrice : Edm.Decimal [required] "Last Price"
PX.Objects.IN.INItemSite.PendingBasePrice : Edm.Decimal [required] "Pending Price"
PX.Objects.IN.INItemSite.PendingBasePriceDate : Edm.DateTimeOffset "Pending Price Date"
PX.Objects.IN.INItemSite.BasePrice : Edm.Decimal [required] "Current Price"
PX.Objects.IN.INItemSite.BasePriceDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.IN.INItemSite.LastCostDate : Edm.DateTimeOffset
PX.Objects.IN.INItemSite.LastCost : Edm.Decimal "Last Cost"
PX.Objects.IN.INItemSite.AvgCost : Edm.Decimal "Average Cost"
PX.Objects.IN.INItemSite.MinCost : Edm.Decimal "Min. Cost"
PX.Objects.IN.INItemSite.MaxCost : Edm.Decimal "Max. Cost"
PX.Objects.IN.INItemSite.TranUnitCost : Edm.Decimal
PX.Objects.IN.INItemSite.PreferredVendorOverride : Edm.Boolean [required] "Override Preferred Vendor"
PX.Objects.IN.INItemSite.PreferredVendorID : Edm.Int32 "Preferred Vendor"
PX.Objects.IN.INItemSite.ProductManagerOverride : Edm.Boolean [required] "Override Product Manager"
PX.Objects.IN.INItemSite.ProductWorkgroupID : Edm.Int32 "Product Workgroup"
PX.Objects.IN.INItemSite.ProductManagerID : Edm.Int32 "Product Manager"
PX.Objects.IN.INItemSite.PriceWorkgroupID : Edm.Int32 "Price Workgroup"
PX.Objects.IN.INItemSite.PriceManagerID : Edm.Int32 "Price Manager"
PX.Objects.IN.INItemSite.IsDefault : Edm.Boolean "Default"
PX.Objects.IN.INItemSite.StdCostOverride : Edm.Boolean [required] "Override Std. Cost"
PX.Objects.IN.INItemSite.BasePriceOverride : Edm.Boolean [required] "Price Override"
PX.Objects.IN.INItemSite.Commissionable : Edm.Boolean [required] "Subject to Commission"
PX.Objects.IN.INItemSite.ABCCodeOverride : Edm.Boolean "ABC Code Override"
PX.Objects.IN.INItemSite.ABCCodeID : Edm.String "ABC Code"
PX.Objects.IN.INItemSite.ABCCodeIsFixed : Edm.Boolean [required] "Fixed ABC Code"
PX.Objects.IN.INItemSite.MovementClassOverride : Edm.Boolean "Movement Class Override"
PX.Objects.IN.INItemSite.MovementClassID : Edm.String "Movement Class"
PX.Objects.IN.INItemSite.PendingMovementClassID : Edm.String
PX.Objects.IN.INItemSite.MovementClassIsFixed : Edm.Boolean [required] "Fixed Movement Class"
PX.Objects.IN.INItemSite.PendingMovementClassPeriodID : Edm.String
PX.Objects.IN.INItemSite.PendingMovementClassUpdateDate : Edm.DateTimeOffset
PX.Objects.IN.INItemSite.NoteID : Edm.Guid
PX.Objects.IN.INItemSite.NoteText : Edm.String "Note Text"
PX.Objects.IN.INItemSite.POCreate : Edm.Boolean "Mark fo PO"
PX.Objects.IN.INItemSite.POSource : Edm.String
PX.Objects.IN.INItemSite.MarkupPct : Edm.Decimal "Markup %"
PX.Objects.IN.INItemSite.MarkupPctOverride : Edm.Boolean [required] "Override Markup %"
PX.Objects.IN.INItemSite.RecPrice : Edm.Decimal "MSRP"
PX.Objects.IN.INItemSite.RecPriceOverride : Edm.Boolean [required] "Override Price"
PX.Objects.IN.INItemSite.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemSite.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemSite.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemSite.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemSite.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemSite.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemSite.ReplenishmentClassID : Edm.String "Replenishment Class"
PX.Objects.IN.INItemSite.ReplenishmentPolicyOverride : Edm.Boolean [required] "Override Replenishment Settings"
PX.Objects.IN.INItemSite.ReplenishmentPolicyID : Edm.String "Seasonality"
PX.Objects.IN.INItemSite.ReplenishmentMethod : Edm.String "Replenishment Method"
PX.Objects.IN.INItemSite.MaxShelfLifeOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.MaxShelfLife : Edm.Int32 "Max. Shelf Life (Days)"
PX.Objects.IN.INItemSite.LaunchDateOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.LaunchDate : Edm.DateTimeOffset "Launch Date"
PX.Objects.IN.INItemSite.TerminationDateOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.TerminationDate : Edm.DateTimeOffset "Termination Date"
PX.Objects.IN.INItemSite.ServiceLevelOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.ServiceLevel : Edm.Decimal "Service Level"
PX.Objects.IN.INItemSite.ServiceLevelPct : Edm.Decimal "Service Level (%)"
PX.Objects.IN.INItemSite.SafetyStockOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.SafetyStock : Edm.Decimal "Safety Stock"
PX.Objects.IN.INItemSite.MinQtyOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.MinQty : Edm.Decimal "Reorder Point"
PX.Objects.IN.INItemSite.MaxQtyOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.MaxQty : Edm.Decimal "Max Qty."
PX.Objects.IN.INItemSite.TransferERQOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.TransferERQ : Edm.Decimal "Transfer ERQ"
PX.Objects.IN.INItemSite.SafetyStockSuggested : Edm.Decimal "Safety Stock Suggested"
PX.Objects.IN.INItemSite.MinQtySuggested : Edm.Decimal "Reorder Point Suggested"
PX.Objects.IN.INItemSite.MaxQtySuggested : Edm.Decimal "Max Qty Suggested"
PX.Objects.IN.INItemSite.ESSmoothingConstantL : Edm.Decimal "Level Smoothing Constant"
PX.Objects.IN.INItemSite.ESSmoothingConstantLOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.ESSmoothingConstantT : Edm.Decimal "Trend Smoothing Constant"
PX.Objects.IN.INItemSite.ESSmoothingConstantTOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.ESSmoothingConstantS : Edm.Decimal "Seasonality Smoothing Constant"
PX.Objects.IN.INItemSite.ESSmoothingConstantSOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.INItemSite.AutoFitModel : Edm.Boolean [required] "Auto Fit Model"
PX.Objects.IN.INItemSite.DemandPerDayAverage : Edm.Decimal "Daily Demand Forecast"
PX.Objects.IN.INItemSite.DemandPerDayMSE : Edm.Decimal "Daily Demand Forecast Error(MSE)"
PX.Objects.IN.INItemSite.DemandPerDayMAD : Edm.Decimal "Daily Forecast Error(MAD)"
PX.Objects.IN.INItemSite.DemandPerDaySTDEV : Edm.Decimal "Daily Demand Forecast Error(STDEV)"
PX.Objects.IN.INItemSite.LeadTimeAverage : Edm.Decimal "Lead Time Average"
PX.Objects.IN.INItemSite.LeadTimeMSE : Edm.Decimal "Lead Time Deviation"
PX.Objects.IN.INItemSite.LeadTimeSTDEV : Edm.Decimal "Lead Time STDEV"
PX.Objects.IN.INItemSite.LastForecastDate : Edm.DateTimeOffset "Last Forecast Date"
PX.Objects.IN.INItemSite.ForecastModelType : Edm.String "Demand Forecast Model Used"
PX.Objects.IN.INItemSite.ForecastPeriodType : Edm.String "Forecast Period Type Used"
PX.Objects.IN.INItemSite.LastFCApplicationDate : Edm.DateTimeOffset "Last Forecast Results Application Date"
PX.Objects.IN.INItemSite.CountryOfOrigin : Edm.String "Country Of Origin"
PX.Objects.IN.INItemSite.tstamp : Edm.Binary
PX.Objects.IN.INItemSite.EPEmployeeByProductManagerID -> PX.Objects.EP.EPEmployee (ProductManagerID=BAccountID)
PX.Objects.IN.INItemSite.EPEmployeeByPriceManagerID -> PX.Objects.EP.EPEmployee (PriceManagerID=BAccountID)
PX.Objects.IN.INItemSite.VendorByPreferredVendorID -> PX.Objects.AP.Vendor (PreferredVendorID=BAccountID)
PX.Objects.IN.INItemSite.BAccountByPreferredVendorID -> PX.Objects.CR.BAccount (PreferredVendorID=BAccountID)
PX.Objects.IN.INItemSite.ContactByProductManagerID -> PX.Objects.CR.Contact (ProductManagerID=ContactID)
PX.Objects.IN.INItemSite.ContactByPriceManagerID -> PX.Objects.CR.Contact (PriceManagerID=ContactID)
PX.Objects.IN.INItemSite.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemSite.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemSite.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemSite.EPCompanyTreeByProductWorkgroupID -> PX.TM.EPCompanyTree (ProductWorkgroupID=WorkGroupID)
PX.Objects.IN.INItemSite.EPCompanyTreeByPriceWorkgroupID -> PX.TM.EPCompanyTree (PriceWorkgroupID=WorkGroupID)
PX.Objects.IN.INItemSite.CountryByCountryOfOrigin -> PX.Objects.CS.Country (CountryOfOrigin=CountryID)
PX.Objects.IN.INItemSite.INABCCodeByABCCodeID -> PX.Objects.IN.INABCCode (ABCCodeID=ABCCodeID)
PX.Objects.IN.INItemSite.INLocationByDfltShipLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INItemSite.INLocationByDfltReceiptLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INItemSite.INLocationByDfltPutawayLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INItemSite.INLocationBySiteID -> PX.Objects.IN.INLocation (SiteID=SiteID)
PX.Objects.IN.INItemSite.INMovementClassByMovementClassID -> PX.Objects.IN.INMovementClass (MovementClassID=MovementClassID)
PX.Objects.IN.INItemSite.INMovementClassByPendingMovementClassID -> PX.Objects.IN.INMovementClass (PendingMovementClassID=MovementClassID)
PX.Objects.IN.INItemSite.INReplenishmentClassByReplenishmentClassID -> PX.Objects.IN.INReplenishmentClass (ReplenishmentClassID=ReplenishmentClassID)
PX.Objects.IN.INItemSite.INReplenishmentPolicyByReplenishmentPolicyID -> PX.Objects.IN.INReplenishmentPolicy (ReplenishmentPolicyID=ReplenishmentPolicyID)
PX.Objects.IN.INItemSite.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INItemSite.INSiteByReplenishmentSourceSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INItemSite.INUnitByDfltSalesUnit -> PX.Objects.IN.INUnit (DfltSalesUnit=FromUnit)
PX.Objects.IN.INItemSite.INUnitByDfltPurchaseUnit -> PX.Objects.IN.INUnit (DfltPurchaseUnit=FromUnit)
PX.Objects.IN.INItemSite.INSitePlanningStrategyByPlanningStrategyID -> PX.Objects.IN.DAC.INSitePlanningStrategy
PX.Objects.IN.INItemSite.INSitePlanningStrategyBySiteID -> PX.Objects.IN.DAC.INSitePlanningStrategy
PX.Objects.IN.INItemSite.AccountByInvtAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INItemSite.SubByInvtSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INItemSite.LocationByPreferredVendorLocationID -> PX.Objects.CR.Location (PreferredVendorID=BAccountID)
PX.Objects.IN.INItemSite.LocationByPreferredVendorID -> PX.Objects.CR.Location (PreferredVendorID=BAccountID)
PX.Objects.IN.INItemSite.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.INItemSite.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.INItemSite.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.IN.INItemSite.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.INItemSite.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.INItemSite.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.INItemSite.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.INItemSite.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)

# PX.Objects.IN.INItemSiteHist (EntityType)

Label: "IN Item Site History"
Key: FinPeriodID, InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INItemSiteHist, INItemSiteHistory, INItemSiteHist
Non-filterable, non-selectable: LastActivityPeriod

PX.Objects.IN.INItemSiteHist.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemSiteHist.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemSiteHist.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemSiteHist.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INItemSiteHist.FinPeriodID : Edm.String [key] "Fin. Period"
PX.Objects.IN.INItemSiteHist.LastActivityPeriod : Edm.String
PX.Objects.IN.INItemSiteHist.FinPtdQtyIssued : Edm.Decimal [required] "Issued"
PX.Objects.IN.INItemSiteHist.FinPtdQtyReceived : Edm.Decimal [required] "Received"
PX.Objects.IN.INItemSiteHist.FinBegQty : Edm.Decimal [required] "Beginning Qty."
PX.Objects.IN.INItemSiteHist.FinYtdQty : Edm.Decimal [required] "Ending Qty."
PX.Objects.IN.INItemSiteHist.FinPtdQtySales : Edm.Decimal [required] "Sales"
PX.Objects.IN.INItemSiteHist.FinPtdQtyCreditMemos : Edm.Decimal [required] "Credit Memos"
PX.Objects.IN.INItemSiteHist.FinPtdQtyDropShipSales : Edm.Decimal [required] "Drop Ship Sales"
PX.Objects.IN.INItemSiteHist.FinPtdQtyTransferIn : Edm.Decimal [required] "Transfer In"
PX.Objects.IN.INItemSiteHist.FinPtdQtyTransferOut : Edm.Decimal [required] "Transfer Out"
PX.Objects.IN.INItemSiteHist.FinPtdQtyAssemblyIn : Edm.Decimal [required] "Assembly In"
PX.Objects.IN.INItemSiteHist.FinPtdQtyAssemblyOut : Edm.Decimal [required] "Assembly Out"
PX.Objects.IN.INItemSiteHist.FinPtdQtyAdjusted : Edm.Decimal "Adjusted"
PX.Objects.IN.INItemSiteHist.FinPtdQtyAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemSiteHist.FinPtdQtyAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemSiteHist.TranPtdQtyReceived : Edm.Decimal [required] "Received"
PX.Objects.IN.INItemSiteHist.TranPtdQtyIssued : Edm.Decimal [required] "Issued"
PX.Objects.IN.INItemSiteHist.TranPtdQtySales : Edm.Decimal [required] "Sales"
PX.Objects.IN.INItemSiteHist.TranPtdQtyCreditMemos : Edm.Decimal [required] "Credit Memos"
PX.Objects.IN.INItemSiteHist.TranPtdQtyDropShipSales : Edm.Decimal [required] "Drop Ship Sales"
PX.Objects.IN.INItemSiteHist.TranPtdQtyTransferIn : Edm.Decimal [required] "Transfer In"
PX.Objects.IN.INItemSiteHist.TranPtdQtyTransferOut : Edm.Decimal [required] "Transfer Out"
PX.Objects.IN.INItemSiteHist.TranPtdQtyAssemblyIn : Edm.Decimal [required] "Assembly In"
PX.Objects.IN.INItemSiteHist.TranPtdQtyAssemblyOut : Edm.Decimal [required] "Assembly Out"
PX.Objects.IN.INItemSiteHist.TranPtdQtyAdjusted : Edm.Decimal "Adjusted"
PX.Objects.IN.INItemSiteHist.TranPtdQtyAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemSiteHist.TranPtdQtyAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemSiteHist.TranBegQty : Edm.Decimal [required] "Beginning Qty."
PX.Objects.IN.INItemSiteHist.TranYtdQty : Edm.Decimal [required] "Ending Qty."
PX.Objects.IN.INItemSiteHist.tstamp : Edm.Binary
PX.Objects.IN.INItemSiteHist.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemSiteHist.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INItemSiteHist.INLocationBySiteID -> PX.Objects.IN.INLocation (LocationID=LocationID, SiteID=SiteID)
PX.Objects.IN.INItemSiteHist.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INItemSiteHist.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.IN.INItemSiteHistByDay (EntityType)

Label: "IN Item Site History by Day"
Key: Date, InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INItemSiteHistByDay, INItemSiteHistorybyDay, INItemSiteHistByDay

PX.Objects.IN.INItemSiteHistByDay.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemSiteHistByDay.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemSiteHistByDay.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemSiteHistByDay.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INItemSiteHistByDay.LastActivityDate : Edm.DateTimeOffset
PX.Objects.IN.INItemSiteHistByDay.Date : Edm.DateTimeOffset [key] "Date"

# PX.Objects.IN.INItemSiteHistByLastDayInPeriod (EntityType)

Label: "IN Item Site History by Last Day In Period"
Key: FinPeriodID, InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INItemSiteHistByLastDayInPeriod, INItemSiteHistorybyLastDayInPeriod, INItemSiteHistByLastDayInPeriod

PX.Objects.IN.INItemSiteHistByLastDayInPeriod.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemSiteHistByLastDayInPeriod.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemSiteHistByLastDayInPeriod.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemSiteHistByLastDayInPeriod.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INItemSiteHistByLastDayInPeriod.LastActivityDate : Edm.DateTimeOffset
PX.Objects.IN.INItemSiteHistByLastDayInPeriod.FinPeriodID : Edm.String [key] "Financial Period ID"
PX.Objects.IN.INItemSiteHistByLastDayInPeriod.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.IN.INItemSiteHistByLastDayInPeriod.PMHistoryCollection -> Collection(PX.Objects.PM.PMHistory)

# PX.Objects.IN.INItemSiteHistByLatestSDate (EntityType)

Label: "IN Item Site History by Latest SDate"
Key: InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INItemSiteHistByLatestSDate, INItemSiteHistorybyLatestSDate, INItemSiteHistByLatestSDate

PX.Objects.IN.INItemSiteHistByLatestSDate.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemSiteHistByLatestSDate.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemSiteHistByLatestSDate.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemSiteHistByLatestSDate.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INItemSiteHistByLatestSDate.LastActivityDate : Edm.DateTimeOffset

# PX.Objects.IN.INItemSiteHistByPeriod (EntityType)

Label: "IN Item Site History by Period"
Key: FinPeriodID, InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INItemSiteHistByPeriod, INItemSiteHistorybyPeriod, INItemSiteHistByPeriod

PX.Objects.IN.INItemSiteHistByPeriod.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemSiteHistByPeriod.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemSiteHistByPeriod.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemSiteHistByPeriod.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INItemSiteHistByPeriod.LastActivityPeriod : Edm.String
PX.Objects.IN.INItemSiteHistByPeriod.FinPeriodID : Edm.String [key] "Fin. Period"

# PX.Objects.IN.INItemSiteHistDay (EntityType)

Label: "IN Item Site History Day"
Key: InventoryID, LocationID, SDate, SiteID, SubItemID
Entity sets: PX_Objects_IN_INItemSiteHistDay, INItemSiteHistoryDay, INItemSiteHistDay
Non-filterable, non-selectable: QtyIn, QtyOut

PX.Objects.IN.INItemSiteHistDay.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemSiteHistDay.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemSiteHistDay.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemSiteHistDay.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INItemSiteHistDay.SDate : Edm.DateTimeOffset [key]
PX.Objects.IN.INItemSiteHistDay.QtyReceived : Edm.Decimal [required] "Received"
PX.Objects.IN.INItemSiteHistDay.QtyIssued : Edm.Decimal [required] "Issued"
PX.Objects.IN.INItemSiteHistDay.QtySales : Edm.Decimal [required] "Sales"
PX.Objects.IN.INItemSiteHistDay.QtyCreditMemos : Edm.Decimal [required] "Credit Memos"
PX.Objects.IN.INItemSiteHistDay.QtyDropShipSales : Edm.Decimal [required] "Drop Ship Sales"
PX.Objects.IN.INItemSiteHistDay.QtyTransferIn : Edm.Decimal [required] "Transfer In"
PX.Objects.IN.INItemSiteHistDay.QtyTransferOut : Edm.Decimal [required] "Transfer Out"
PX.Objects.IN.INItemSiteHistDay.QtyAssemblyIn : Edm.Decimal [required] "Assembly In"
PX.Objects.IN.INItemSiteHistDay.QtyAssemblyOut : Edm.Decimal [required] "Assembly Out"
PX.Objects.IN.INItemSiteHistDay.QtyAdjustedIn : Edm.Decimal [required]
PX.Objects.IN.INItemSiteHistDay.QtyAdjustedOut : Edm.Decimal [required]
PX.Objects.IN.INItemSiteHistDay.QtyDebit : Edm.Decimal [required] "Debit"
PX.Objects.IN.INItemSiteHistDay.QtyCredit : Edm.Decimal [required] "Credit"
PX.Objects.IN.INItemSiteHistDay.BegQty : Edm.Decimal [required] "Beginning Qty."
PX.Objects.IN.INItemSiteHistDay.QtyIn : Edm.Decimal "Qty. In"
PX.Objects.IN.INItemSiteHistDay.QtyOut : Edm.Decimal "Qty. Out"
PX.Objects.IN.INItemSiteHistDay.EndQty : Edm.Decimal [required] "Ending Qty."
PX.Objects.IN.INItemSiteHistDay.tstamp : Edm.Binary
PX.Objects.IN.INItemSiteHistDay.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemSiteHistDay.INItemSiteReplenishmentBySubItemID -> PX.Objects.IN.INItemSiteReplenishment (InventoryID=InventoryID, SiteID=SiteID, SubItemID=SubItemID)
PX.Objects.IN.INItemSiteHistDay.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INItemSiteHistDay.INLocationBySiteID -> PX.Objects.IN.INLocation (LocationID=LocationID, SiteID=SiteID)
PX.Objects.IN.INItemSiteHistDay.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INItemSiteHistDay.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.IN.INItemSiteReplenishment (EntityType)

Label: "SubItem Replenishment Info"
Key: InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INItemSiteReplenishment, SubItemReplenishmentInfo, INItemSiteReplenishment
Non-filterable, non-selectable: DemandPerDaySTDEV

PX.Objects.IN.INItemSiteReplenishment.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemSiteReplenishment.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INItemSiteReplenishment.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemSiteReplenishment.SafetyStock : Edm.Decimal [required] "Safety Stock"
PX.Objects.IN.INItemSiteReplenishment.MinQty : Edm.Decimal [required] "Reorder Point"
PX.Objects.IN.INItemSiteReplenishment.MaxQty : Edm.Decimal [required] "Max Qty."
PX.Objects.IN.INItemSiteReplenishment.TransferERQ : Edm.Decimal "Transfer ERQ"
PX.Objects.IN.INItemSiteReplenishment.ItemStatus : Edm.String "Status"
PX.Objects.IN.INItemSiteReplenishment.SafetyStockSuggested : Edm.Decimal "Safety Stock Suggested"
PX.Objects.IN.INItemSiteReplenishment.MinQtySuggested : Edm.Decimal "Reorder Point Suggested"
PX.Objects.IN.INItemSiteReplenishment.MaxQtySuggested : Edm.Decimal "Max Qty Suggested"
PX.Objects.IN.INItemSiteReplenishment.DemandPerDayAverage : Edm.Decimal "Daily Demand Forecast"
PX.Objects.IN.INItemSiteReplenishment.DemandPerDayMSE : Edm.Decimal "Daily Demand Forecast Error(MSE)"
PX.Objects.IN.INItemSiteReplenishment.DemandPerDayMAD : Edm.Decimal "Daily Forecast Error MAD"
PX.Objects.IN.INItemSiteReplenishment.DemandPerDaySTDEV : Edm.Decimal "Daily Demand Forecast Error(STDEV)"
PX.Objects.IN.INItemSiteReplenishment.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemSiteReplenishment.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemSiteReplenishment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemSiteReplenishment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemSiteReplenishment.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemSiteReplenishment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemSiteReplenishment.tstamp : Edm.Binary
PX.Objects.IN.INItemSiteReplenishment.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemSiteReplenishment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemSiteReplenishment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemSiteReplenishment.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INItemSiteReplenishment.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INItemSiteReplenishment.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)

# PX.Objects.IN.INItemStats (EntityType)

Label: "IN Item Statistics"
Key: InventoryID, SiteID
Entity sets: PX_Objects_IN_INItemStats, INItemStatistics, INItemStats
Non-filterable, non-selectable: QtyReceived, CostReceived

PX.Objects.IN.INItemStats.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INItemStats.SiteID : Edm.Int32 [key]
PX.Objects.IN.INItemStats.ValMethod : Edm.String
PX.Objects.IN.INItemStats.LastCost : Edm.Decimal [required] "Last Cost"
PX.Objects.IN.INItemStats.LastCostDate : Edm.DateTimeOffset [required]
PX.Objects.IN.INItemStats.AvgCost : Edm.Decimal "Average Cost"
PX.Objects.IN.INItemStats.MinCost : Edm.Decimal [required] "Minimal Cost"
PX.Objects.IN.INItemStats.MaxCost : Edm.Decimal [required] "Max. Cost"
PX.Objects.IN.INItemStats.QtyOnHand : Edm.Decimal [required]
PX.Objects.IN.INItemStats.TotalCost : Edm.Decimal [required]
PX.Objects.IN.INItemStats.QtyReceived : Edm.Decimal
PX.Objects.IN.INItemStats.CostReceived : Edm.Decimal
PX.Objects.IN.INItemStats.LastPurchaseDate : Edm.DateTimeOffset "Last Purchase Date"
PX.Objects.IN.INItemStats.tstamp : Edm.Binary
PX.Objects.IN.INItemStats.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemStats.INItemSiteBySiteID -> PX.Objects.IN.INItemSite (InventoryID=InventoryID, SiteID=SiteID)
PX.Objects.IN.INItemStats.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.IN.INItemXRef (EntityType)

Label: "Cross-Reference"
Key: AlternateID, AlternateType, BAccountID, InventoryID, SubItemID
Entity sets: PX_Objects_IN_INItemXRef, CrossReference, INItemXRef
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INItemXRef.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INItemXRef.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INItemXRef.AlternateType : Edm.String [key required] "Alternate Type"
PX.Objects.IN.INItemXRef.BAccountID : Edm.Int32 [key] "Vendor/Customer"
PX.Objects.IN.INItemXRef.AlternateID : Edm.String [key] "Alternate ID"
PX.Objects.IN.INItemXRef.Descr : Edm.String "Description"
PX.Objects.IN.INItemXRef.UOM : Edm.String "Alt. ID Unit"
PX.Objects.IN.INItemXRef.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INItemXRef.CreatedByScreenID : Edm.String
PX.Objects.IN.INItemXRef.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemXRef.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INItemXRef.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INItemXRef.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INItemXRef.NoteID : Edm.Guid
PX.Objects.IN.INItemXRef.NoteText : Edm.String "Note Text"
PX.Objects.IN.INItemXRef.tstamp : Edm.Binary
PX.Objects.IN.INItemXRef.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.IN.INItemXRef.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INItemXRef.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INItemXRef.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INItemXRef.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INItemXRef.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.IN.INKitRegister (EntityType)

Label: "IN Kit"
Key: DocType, RefNbr
Entity sets: PX_Objects_IN_INKitRegister, INKit, INKitRegister
Non-filterable, non-selectable: TotalCostStock, TotalCostNonStock, LotSerTrack

PX.Objects.IN.INKitRegister.DocType : Edm.String [key] "Type"
PX.Objects.IN.INKitRegister.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.IN.INKitRegister.OrigModule : Edm.String
PX.Objects.IN.INKitRegister.TranDesc : Edm.String "Description"
PX.Objects.IN.INKitRegister.Released : Edm.Boolean
PX.Objects.IN.INKitRegister.Hold : Edm.Boolean "Hold"
PX.Objects.IN.INKitRegister.Status : Edm.String "Status"
PX.Objects.IN.INKitRegister.Approved : Edm.Boolean
PX.Objects.IN.INKitRegister.Rejected : Edm.Boolean
PX.Objects.IN.INKitRegister.TranDate : Edm.DateTimeOffset "Date"
PX.Objects.IN.INKitRegister.TransferType : Edm.String "Transfer Type"
PX.Objects.IN.INKitRegister.FinPeriodID : Edm.String "Post Period"
PX.Objects.IN.INKitRegister.TranPeriodID : Edm.String
PX.Objects.IN.INKitRegister.LineCntr : Edm.Int32
PX.Objects.IN.INKitRegister.TotalQty : Edm.Decimal "Total Qty."
PX.Objects.IN.INKitRegister.TotalAmount : Edm.Decimal "Total Amount"
PX.Objects.IN.INKitRegister.TotalCost : Edm.Decimal "Total Cost"
PX.Objects.IN.INKitRegister.TotalCostStock : Edm.Decimal "Stock Total Cost"
PX.Objects.IN.INKitRegister.TotalCostNonStock : Edm.Decimal "Non-Stock Total Cost"
PX.Objects.IN.INKitRegister.ControlQty : Edm.Decimal "Control Qty."
PX.Objects.IN.INKitRegister.ControlAmount : Edm.Decimal "Control Amount"
PX.Objects.IN.INKitRegister.ControlCost : Edm.Decimal "Control Cost"
PX.Objects.IN.INKitRegister.KitInventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INKitRegister.KitRevisionID : Edm.String "Revision"
PX.Objects.IN.INKitRegister.KitLineNbr : Edm.Int32
PX.Objects.IN.INKitRegister.KitRequestDate : Edm.DateTimeOffset "Requested On"
PX.Objects.IN.INKitRegister.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.IN.INKitRegister.LotSerTrack : Edm.String
PX.Objects.IN.INKitRegister.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INKitRegister.CreatedByScreenID : Edm.String
PX.Objects.IN.INKitRegister.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INKitRegister.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INKitRegister.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INKitRegister.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitRegister.NoteID : Edm.Guid
PX.Objects.IN.INKitRegister.tstamp : Edm.Binary
PX.Objects.IN.INKitRegister.WorkgroupID : Edm.Int32
PX.Objects.IN.INKitRegister.OwnerID : Edm.Int32 "Owner"
PX.Objects.IN.INKitRegister.TranDocType : Edm.String
PX.Objects.IN.INKitRegister.TranOrigModule : Edm.String
PX.Objects.IN.INKitRegister.TranType : Edm.String "Tran. Type"
PX.Objects.IN.INKitRegister.TranRefNbr : Edm.String
PX.Objects.IN.INKitRegister.TranBranchID : Edm.Int32
PX.Objects.IN.INKitRegister.LineNbr : Edm.Int32
PX.Objects.IN.INKitRegister.AssyType : Edm.String
PX.Objects.IN.INKitRegister.ProjectID : Edm.Int32
PX.Objects.IN.INKitRegister.TaskID : Edm.Int32
PX.Objects.IN.INKitRegister.TranTranDate : Edm.DateTimeOffset
PX.Objects.IN.INKitRegister.InvtMult : Edm.Int16
PX.Objects.IN.INKitRegister.IsStockItem : Edm.Boolean
PX.Objects.IN.INKitRegister.InventoryID : Edm.Int32
PX.Objects.IN.INKitRegister.UOM : Edm.String "UOM"
PX.Objects.IN.INKitRegister.Qty : Edm.Decimal "Quantity"
PX.Objects.IN.INKitRegister.BaseQty : Edm.Decimal
PX.Objects.IN.INKitRegister.UnassignedQty : Edm.Decimal
PX.Objects.IN.INKitRegister.TranReleased : Edm.Boolean
PX.Objects.IN.INKitRegister.TranFinPeriodID : Edm.String
PX.Objects.IN.INKitRegister.TranTranPeriodID : Edm.String
PX.Objects.IN.INKitRegister.UnitPrice : Edm.Decimal "Unit Price"
PX.Objects.IN.INKitRegister.TranAmt : Edm.Decimal "Ext. Price"
PX.Objects.IN.INKitRegister.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.IN.INKitRegister.TranCost : Edm.Decimal "Ext. Cost"
PX.Objects.IN.INKitRegister.TranTranDesc : Edm.String "Description"
PX.Objects.IN.INKitRegister.ReasonCode : Edm.String "Reason Code"
PX.Objects.IN.INKitRegister.UpdateShippedNotInvoiced : Edm.Boolean
PX.Objects.IN.INKitRegister.IsIntercompany : Edm.Boolean
PX.Objects.IN.INKitRegister.CostCenterID : Edm.Int32
PX.Objects.IN.INKitRegister.ToCostCenterID : Edm.Int32
PX.Objects.IN.INKitRegister.CostLayerType : Edm.String
PX.Objects.IN.INKitRegister.ToCostLayerType : Edm.String
PX.Objects.IN.INKitRegister.InventorySource : Edm.String
PX.Objects.IN.INKitRegister.ToInventorySource : Edm.String
PX.Objects.IN.INKitRegister.IsUnassigned : Edm.Boolean
PX.Objects.IN.INKitRegister.TranCreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INKitRegister.TranCreatedByScreenID : Edm.String
PX.Objects.IN.INKitRegister.TranCreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitRegister.TranLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INKitRegister.TranLastModifiedByScreenID : Edm.String
PX.Objects.IN.INKitRegister.TranLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitRegister.Trantstamp : Edm.Binary
PX.Objects.IN.INKitRegister.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.IN.INKitRegister.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.IN.INKitRegister.INTranByLineNbr -> PX.Objects.IN.INTran (TranDocType=DocType, TranRefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.IN.INKitRegister.INTranByKitLineNbr -> PX.Objects.IN.INTran (DocType=DocType, RefNbr=RefNbr, KitLineNbr=LineNbr)
PX.Objects.IN.INKitRegister.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.IN.INKitRegister.InventoryItemByKitInventoryID -> PX.Objects.IN.InventoryItem (KitInventoryID=InventoryID)
PX.Objects.IN.INKitRegister.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INKitRegister.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.IN.INKitRegister.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.IN.INKitRegister.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.IN.INKitRegister.INKitSpecHdrByKitRevisionID -> PX.Objects.IN.INKitSpecHdr (KitInventoryID=KitInventoryID, KitRevisionID=RevisionID)
PX.Objects.IN.INKitRegister.INKitSpecHdrByKitInventoryID -> PX.Objects.IN.INKitSpecHdr (KitRevisionID=RevisionID, KitInventoryID=KitInventoryID)
PX.Objects.IN.INKitRegister.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INKitRegister.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INKitRegister.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INKitRegister.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INKitRegister.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.IN.INKitRegister.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INKitRegister.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INKitRegister.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.INKitRegister.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INKitRegister.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.IN.INKitRegister.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.IN.INKitRegister.SOBlanketOrderDisplayLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderDisplayLink)
PX.Objects.IN.INKitRegister.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.IN.INKitRegister.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.IN.INKitRegister.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INKitRegister.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INKitRegister.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.INKitRegister.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INKitRegister.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.IN.INKitRegister.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.IN.INKitRegister.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.IN.INKitRegister.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.IN.INKitRegister.MNMaterialListShipmentCollection -> Collection(PX.Objects.MN.MNMaterialListShipment)
PX.Objects.IN.INKitRegister.INKitSerialPartCollection -> Collection(PX.Objects.IN.INKitSerialPart)
PX.Objects.IN.INKitRegister.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.Objects.IN.INKitRegister.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.INKitRegister.INRegisterCartCollection -> Collection(PX.Objects.IN.DAC.INRegisterCart)
PX.Objects.IN.INKitRegister.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.Objects.IN.INKitRegister.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.IN.INKitRegister.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.IN.INKitRegister.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.IN.INKitRegister.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INKitRegister.POAccrualInquiryResultCollection -> Collection(PX.Objects.PO.POAccrualInquiryResult)
PX.Objects.IN.INKitRegister.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)
PX.Objects.IN.INKitRegister.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.IN.INKitRegister.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.INKitRegister.POCartReceiptCollection -> Collection(PX.Objects.PO.POCartReceipt)
PX.Objects.IN.INKitRegister.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)
PX.Objects.IN.INKitRegister.AdjustmentTranBySiteLotSerialCollection -> Collection(PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial)
PX.Objects.IN.INKitRegister.AdjustmentTranBySiteStatusCollection -> Collection(PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus)

# PX.Objects.IN.INKitSerialPart (EntityType)

Key: DocType, KitLineNbr, KitSplitLineNbr, PartLineNbr, PartSplitLineNbr, RefNbr
Entity sets: PX_Objects_IN_INKitSerialPart

PX.Objects.IN.INKitSerialPart.DocType : Edm.String [key]
PX.Objects.IN.INKitSerialPart.RefNbr : Edm.String [key]
PX.Objects.IN.INKitSerialPart.KitLineNbr : Edm.Int32 [key]
PX.Objects.IN.INKitSerialPart.KitSplitLineNbr : Edm.Int32 [key]
PX.Objects.IN.INKitSerialPart.PartLineNbr : Edm.Int32 [key]
PX.Objects.IN.INKitSerialPart.PartSplitLineNbr : Edm.Int32 [key]
PX.Objects.IN.INKitSerialPart.tstamp : Edm.Binary
PX.Objects.IN.INKitSerialPart.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INKitSerialPart.CreatedByScreenID : Edm.String
PX.Objects.IN.INKitSerialPart.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitSerialPart.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INKitSerialPart.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INKitSerialPart.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitSerialPart.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INKitSerialPart.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INKitSerialPart.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INKitSerialPart.INTranSplitByKitSplitLineNbr -> PX.Objects.IN.INTranSplit (DocType=DocType, RefNbr=RefNbr, KitLineNbr=LineNbr, KitSplitLineNbr=SplitLineNbr)

# PX.Objects.IN.INKitSpecHdr (EntityType)

Label: "Kit Specification"
Key: KitInventoryID, RevisionID
Entity sets: PX_Objects_IN_INKitSpecHdr, KitSpecification, INKitSpecHdr
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INKitSpecHdr.KitInventoryID : Edm.Int32 [key] "Kit Inventory ID"
PX.Objects.IN.INKitSpecHdr.RevisionID : Edm.String [key] "Revision"
PX.Objects.IN.INKitSpecHdr.Descr : Edm.String "Description"
PX.Objects.IN.INKitSpecHdr.IsActive : Edm.Boolean [required] "Active"
PX.Objects.IN.INKitSpecHdr.AllowCompAddition : Edm.Boolean [required] "Allow Component Addition"
PX.Objects.IN.INKitSpecHdr.IsStock : Edm.Boolean
PX.Objects.IN.INKitSpecHdr.IsNonStock : Edm.Boolean "Non-Stock"
PX.Objects.IN.INKitSpecHdr.NoteID : Edm.Guid
PX.Objects.IN.INKitSpecHdr.NoteText : Edm.String "Note Text"
PX.Objects.IN.INKitSpecHdr.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INKitSpecHdr.CreatedByScreenID : Edm.String
PX.Objects.IN.INKitSpecHdr.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitSpecHdr.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INKitSpecHdr.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INKitSpecHdr.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitSpecHdr.tstamp : Edm.Binary
PX.Objects.IN.INKitSpecHdr.InventoryItemByKitInventoryID -> PX.Objects.IN.InventoryItem (KitInventoryID=InventoryID)
PX.Objects.IN.INKitSpecHdr.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INKitSpecHdr.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INKitSpecHdr.INSubItemByKitSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INKitSpecHdr.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.INKitSpecHdr.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.IN.INKitSpecHdr.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.IN.INKitSpecHdr.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.INKitSpecHdr.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)

# PX.Objects.IN.INKitSpecNonStkDet (EntityType)

Label: "Non-Stock Component of Kit Specification"
Key: KitInventoryID, LineNbr, RevisionID
Entity sets: PX_Objects_IN_INKitSpecNonStkDet, NonStockComponentofKitSpecification, INKitSpecNonStkDet
Non-filterable, non-selectable: BaseDfltCompQty

PX.Objects.IN.INKitSpecNonStkDet.KitInventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INKitSpecNonStkDet.RevisionID : Edm.String [key]
PX.Objects.IN.INKitSpecNonStkDet.LineNbr : Edm.Int32 [key]
PX.Objects.IN.INKitSpecNonStkDet.CompInventoryID : Edm.Int32 "Component ID"
PX.Objects.IN.INKitSpecNonStkDet.DfltCompQty : Edm.Decimal [required] "Component Qty."
PX.Objects.IN.INKitSpecNonStkDet.BaseDfltCompQty : Edm.Decimal
PX.Objects.IN.INKitSpecNonStkDet.UOM : Edm.String "UOM"
PX.Objects.IN.INKitSpecNonStkDet.AllowQtyVariation : Edm.Boolean [required] "Allow Component Qty. Variance"
PX.Objects.IN.INKitSpecNonStkDet.MinCompQty : Edm.Decimal "Min. Component Qty."
PX.Objects.IN.INKitSpecNonStkDet.MaxCompQty : Edm.Decimal "Max. Component Qty."
PX.Objects.IN.INKitSpecNonStkDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INKitSpecNonStkDet.CreatedByScreenID : Edm.String
PX.Objects.IN.INKitSpecNonStkDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitSpecNonStkDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INKitSpecNonStkDet.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INKitSpecNonStkDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitSpecNonStkDet.tstamp : Edm.Binary
PX.Objects.IN.INKitSpecNonStkDet.InventoryItemByKitInventoryID -> PX.Objects.IN.InventoryItem (KitInventoryID=InventoryID)
PX.Objects.IN.INKitSpecNonStkDet.InventoryItemByCompInventoryID -> PX.Objects.IN.InventoryItem (CompInventoryID=InventoryID)
PX.Objects.IN.INKitSpecNonStkDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INKitSpecNonStkDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INKitSpecNonStkDet.INKitSpecHdrByRevisionID -> PX.Objects.IN.INKitSpecHdr (KitInventoryID=KitInventoryID, RevisionID=RevisionID)
PX.Objects.IN.INKitSpecNonStkDet.INUnitByCompInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, CompInventoryID=InventoryID)

# PX.Objects.IN.INKitSpecStkDet (EntityType)

Label: "Stock Component of Kit Specification"
Key: KitInventoryID, LineNbr, RevisionID
Entity sets: PX_Objects_IN_INKitSpecStkDet, StockComponentofKitSpecification, INKitSpecStkDet
Non-filterable, non-selectable: BaseDfltCompQty

PX.Objects.IN.INKitSpecStkDet.KitInventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INKitSpecStkDet.RevisionID : Edm.String [key]
PX.Objects.IN.INKitSpecStkDet.LineNbr : Edm.Int32 [key]
PX.Objects.IN.INKitSpecStkDet.CompInventoryID : Edm.Int32 "Component ID"
PX.Objects.IN.INKitSpecStkDet.DfltCompQty : Edm.Decimal [required] "Component Qty."
PX.Objects.IN.INKitSpecStkDet.BaseDfltCompQty : Edm.Decimal
PX.Objects.IN.INKitSpecStkDet.UOM : Edm.String "UOM"
PX.Objects.IN.INKitSpecStkDet.AllowQtyVariation : Edm.Boolean [required] "Allow Component Qty. Variance"
PX.Objects.IN.INKitSpecStkDet.MinCompQty : Edm.Decimal "Min. Component Qty."
PX.Objects.IN.INKitSpecStkDet.MaxCompQty : Edm.Decimal "Max. Component Qty."
PX.Objects.IN.INKitSpecStkDet.DisassemblyCoeff : Edm.Decimal [required] "Disassembly Coeff."
PX.Objects.IN.INKitSpecStkDet.AllowSubstitution : Edm.Boolean [required] "Allow Component Substitution"
PX.Objects.IN.INKitSpecStkDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INKitSpecStkDet.CreatedByScreenID : Edm.String
PX.Objects.IN.INKitSpecStkDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitSpecStkDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INKitSpecStkDet.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INKitSpecStkDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitSpecStkDet.tstamp : Edm.Binary
PX.Objects.IN.INKitSpecStkDet.InventoryItemByKitInventoryID -> PX.Objects.IN.InventoryItem (KitInventoryID=InventoryID)
PX.Objects.IN.INKitSpecStkDet.InventoryItemByCompInventoryID -> PX.Objects.IN.InventoryItem (CompInventoryID=InventoryID)
PX.Objects.IN.INKitSpecStkDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INKitSpecStkDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INKitSpecStkDet.INKitSpecHdrByRevisionID -> PX.Objects.IN.INKitSpecHdr (KitInventoryID=KitInventoryID, RevisionID=RevisionID)
PX.Objects.IN.INKitSpecStkDet.INSubItemByCompSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INKitSpecStkDet.INUnitByCompInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, CompInventoryID=InventoryID)

# PX.Objects.IN.INKitTranSplit (EntityType)

Label: "IN Kit Split"
Key: DocType, LineNbr, RefNbr, SplitLineNbr
Entity sets: PX_Objects_IN_INKitTranSplit, INKitSplit, INKitTranSplit
Non-filterable, non-selectable: LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.IN.INKitTranSplit.DocType : Edm.String [key]
PX.Objects.IN.INKitTranSplit.OrigModule : Edm.String
PX.Objects.IN.INKitTranSplit.TranType : Edm.String
PX.Objects.IN.INKitTranSplit.RefNbr : Edm.String [key]
PX.Objects.IN.INKitTranSplit.LineNbr : Edm.Int32 [key]
PX.Objects.IN.INKitTranSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.IN.INKitTranSplit.TranDate : Edm.DateTimeOffset
PX.Objects.IN.INKitTranSplit.InvtMult : Edm.Int16
PX.Objects.IN.INKitTranSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INKitTranSplit.LotSerClassID : Edm.String
PX.Objects.IN.INKitTranSplit.AssignedNbr : Edm.String
PX.Objects.IN.INKitTranSplit.Released : Edm.Boolean
PX.Objects.IN.INKitTranSplit.UOM : Edm.String "UOM"
PX.Objects.IN.INKitTranSplit.Qty : Edm.Decimal "Quantity"
PX.Objects.IN.INKitTranSplit.BaseQty : Edm.Decimal
PX.Objects.IN.INKitTranSplit.PlanID : Edm.Int64
PX.Objects.IN.INKitTranSplit.ProjectID : Edm.Int32
PX.Objects.IN.INKitTranSplit.TaskID : Edm.Int32
PX.Objects.IN.INKitTranSplit.IsIntercompany : Edm.Boolean
PX.Objects.IN.INKitTranSplit.IsUnassigned : Edm.Boolean
PX.Objects.IN.INKitTranSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INKitTranSplit.CreatedByScreenID : Edm.String
PX.Objects.IN.INKitTranSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitTranSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INKitTranSplit.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INKitTranSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INKitTranSplit.tstamp : Edm.Binary
PX.Objects.IN.INKitTranSplit.INTranByLineNbr -> PX.Objects.IN.INTran (DocType=DocType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.IN.INKitTranSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INKitTranSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.IN.INKitTranSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INKitTranSplit.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INKitTranSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INKitTranSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INKitTranSplit.INKitRegisterByLineNbr -> PX.Objects.IN.INKitRegister (DocType=DocType, RefNbr=RefNbr, LineNbr=KitLineNbr)
PX.Objects.IN.INKitTranSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.IN.INKitTranSplit.INKitRegisterByRefNbr -> PX.Objects.IN.INKitRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INKitTranSplit.INKitSerialPartCollection -> Collection(PX.Objects.IN.INKitSerialPart)
PX.Objects.IN.INKitTranSplit.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.IN.INLocation (EntityType)

Label: "IN Location"
Key: LocationCD, SiteID
Entity sets: PX_Objects_IN_INLocation, INLocation
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INLocation.LocationID : Edm.Int32
PX.Objects.IN.INLocation.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INLocation.LocationCD : Edm.String [key] "Location ID"
PX.Objects.IN.INLocation.Descr : Edm.String "Description"
PX.Objects.IN.INLocation.IsCosted : Edm.Boolean [required] "Cost Separately"
PX.Objects.IN.INLocation.IsSorting : Edm.Boolean [required] "Sort Location"
PX.Objects.IN.INLocation.CostSiteID : Edm.Int32
PX.Objects.IN.INLocation.InclQtyAvail : Edm.Boolean [required] "Include in Qty. Available"
PX.Objects.IN.INLocation.AssemblyValid : Edm.Boolean [required] "Assembly Allowed"
PX.Objects.IN.INLocation.PickPriority : Edm.Int16 [required] "Pick Priority"
PX.Objects.IN.INLocation.PathPriority : Edm.Int32 "Path"
PX.Objects.IN.INLocation.SalesValid : Edm.Boolean [required] "Sales Allowed"
PX.Objects.IN.INLocation.ReceiptsValid : Edm.Boolean [required] "Receipts Allowed"
PX.Objects.IN.INLocation.TransfersValid : Edm.Boolean [required] "Transfers Allowed"
PX.Objects.IN.INLocation.ProductionValid : Edm.Boolean [required] "Production Allowed"
PX.Objects.IN.INLocation.PrimaryItemValid : Edm.String "Primary Item Validation"
PX.Objects.IN.INLocation.PrimaryItemID : Edm.Int32 "Primary Item"
PX.Objects.IN.INLocation.PrimaryItemClassID : Edm.Int32 "Primary Item Class"
PX.Objects.IN.INLocation.Active : Edm.Boolean [required] "Active"
PX.Objects.IN.INLocation.NoteID : Edm.Guid
PX.Objects.IN.INLocation.NoteText : Edm.String "Note Text"
PX.Objects.IN.INLocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INLocation.CreatedByScreenID : Edm.String
PX.Objects.IN.INLocation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INLocation.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLocation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLocation.tstamp : Edm.Binary
PX.Objects.IN.INLocation.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.IN.INLocation.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.IN.INLocation.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.IN.INLocation.InventoryItemByPrimaryItemID -> PX.Objects.IN.InventoryItem (PrimaryItemID=InventoryID)
PX.Objects.IN.INLocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INLocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INLocation.INItemClassByPrimaryItemClassID -> PX.Objects.IN.INItemClass (PrimaryItemClassID=ItemClassID)
PX.Objects.IN.INLocation.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INLocation.INSiteZoneByZoneID -> PX.Objects.IN.DAC.INSiteZone
PX.Objects.IN.INLocation.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.INLocation.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INLocation.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INLocation.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INLocation.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.IN.INLocation.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.INLocation.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INLocation.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.INLocation.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INLocation.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.INLocation.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.INLocation.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INLocation.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.IN.INLocation.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INLocation.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INLocation.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INLocation.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.IN.INLocation.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.INLocation.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.INLocation.BCLocationsCollection -> Collection(PX.Commerce.Objects.BCLocations)
PX.Objects.IN.INLocation.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INLocation.SOPickerCollection -> Collection(PX.Objects.SO.SOPicker)
PX.Objects.IN.INLocation.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INLocation.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.INLocation.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.INLocation.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INLocation.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INLocation.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INLocation.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.INLocation.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.INLocation.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.INLocation.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.IN.INLocation.INPIClassLocationCollection -> Collection(PX.Objects.IN.INPIClassLocation)
PX.Objects.IN.INLocation.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.INLocation.INPIStatusLocCollection -> Collection(PX.Objects.IN.INPIStatusLoc)
PX.Objects.IN.INLocation.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.IN.INLocation.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.IN.INLocation.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.INLocation.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.IN.INLocation.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.IN.INLocation.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.INLocation.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.INLocation.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.INLocation.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.IN.INLocation.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.INLocation.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.Objects.IN.INLocation.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.INLocation.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.INLocation.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.INLocation.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.INLocation.AMWCCollection -> Collection(PX.Objects.AM.AMWC)
PX.Objects.IN.INLocation.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.INLocation.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INLocation.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INLocation.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.INLocation.SVStagingWarehouseCollection -> Collection(PX.Objects.SV.SVStagingWarehouse)
PX.Objects.IN.INLocation.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INLocation.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.INLocation.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.IN.INLocation.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.INLocation.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.INLocation.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.IN.INLocation.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.IN.INLocation.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INLocation.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.INLocation.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.INLocation.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.IN.INLocation.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.INLocation.StoragePlaceCollection -> Collection(PX.Objects.IN.StoragePlace)

# PX.Objects.IN.INLocationCostStatus (EntityType)

Key: InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INLocationCostStatus
Non-filterable, non-selectable: UnitCost

PX.Objects.IN.INLocationCostStatus.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INLocationCostStatus.SubItemID : Edm.Int32 [key]
PX.Objects.IN.INLocationCostStatus.SiteID : Edm.Int32 [key]
PX.Objects.IN.INLocationCostStatus.LocationID : Edm.Int32 [key]
PX.Objects.IN.INLocationCostStatus.QtyOnHand : Edm.Decimal
PX.Objects.IN.INLocationCostStatus.TotalCost : Edm.Decimal
PX.Objects.IN.INLocationCostStatus.DecPlPrcCst : Edm.Int16
PX.Objects.IN.INLocationCostStatus.UnitCost : Edm.Decimal
PX.Objects.IN.INLocationCostStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INLocationCostStatus.INSiteByCostSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INLocationCostStatus.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INLocationCostStatus.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.IN.INLocationStatus (EntityType)

Label: "IN Location Status"
Key: InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INLocationStatus, INLocationStatus
Non-filterable, non-selectable: Active, QtyNotAvail, QtyExpired

PX.Objects.IN.INLocationStatus.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INLocationStatus.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INLocationStatus.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INLocationStatus.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INLocationStatus.Active : Edm.Boolean "Active"
PX.Objects.IN.INLocationStatus.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INLocationStatus.QtyAvail : Edm.Decimal [required] "Qty. Available"
PX.Objects.IN.INLocationStatus.QtyNotAvail : Edm.Decimal
PX.Objects.IN.INLocationStatus.QtyExpired : Edm.Decimal
PX.Objects.IN.INLocationStatus.QtyHardAvail : Edm.Decimal [required] "Qty. Hard Available"
PX.Objects.IN.INLocationStatus.QtyActual : Edm.Decimal [required] "Qty. Available for Issue"
PX.Objects.IN.INLocationStatus.QtyInTransit : Edm.Decimal [required] "Qty. In-Transit"
PX.Objects.IN.INLocationStatus.QtyInTransitToSO : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPOPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPOOrders : Edm.Decimal [required] "Qty. Purchase Orders"
PX.Objects.IN.INLocationStatus.QtyPOReceipts : Edm.Decimal [required] "Qty. Purchase Receipts"
PX.Objects.IN.INLocationStatus.QtySOBackOrdered : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtySOPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtySOBooked : Edm.Decimal [required] "Qty. SO Booked"
PX.Objects.IN.INLocationStatus.QtySOShipped : Edm.Decimal [required] "Qty. SO Shipped"
PX.Objects.IN.INLocationStatus.QtySOShipping : Edm.Decimal [required] "Qty. SO Shipping"
PX.Objects.IN.INLocationStatus.QtyMLPrepared : Edm.Decimal [required] "Qty. Material Prepared"
PX.Objects.IN.INLocationStatus.QtyMLBooked : Edm.Decimal [required] "Qty. Material Booked"
PX.Objects.IN.INLocationStatus.QtyMLDispatched : Edm.Decimal [required] "Qty. Material Dispatched"
PX.Objects.IN.INLocationStatus.QtyMLAllocated : Edm.Decimal [required] "Qty. Material Allocated"
PX.Objects.IN.INLocationStatus.QtyINIssues : Edm.Decimal [required] "Qty On Inventory Issues"
PX.Objects.IN.INLocationStatus.QtyINReceipts : Edm.Decimal [required] "Qty On Inventory Receipts"
PX.Objects.IN.INLocationStatus.QtyINAssemblyDemand : Edm.Decimal [required] "Qty Demanded by Kit Assembly"
PX.Objects.IN.INLocationStatus.QtyINAssemblySupply : Edm.Decimal [required] "Qty On Kit Assembly"
PX.Objects.IN.INLocationStatus.QtyInTransitToProduction : Edm.Decimal [required] "Qty In Transit to Production"
PX.Objects.IN.INLocationStatus.QtyProductionSupplyPrepared : Edm.Decimal [required] "Qty Production Supply Prepared"
PX.Objects.IN.INLocationStatus.QtyProductionSupply : Edm.Decimal [required] "Qty On Production Supply"
PX.Objects.IN.INLocationStatus.QtyPOFixedProductionPrepared : Edm.Decimal [required] "Qty On Purchase for Prod. Prepared"
PX.Objects.IN.INLocationStatus.QtyPOFixedProductionOrders : Edm.Decimal [required] "Qty On Purchase for Production"
PX.Objects.IN.INLocationStatus.QtyProductionDemandPrepared : Edm.Decimal [required] "Qty On Production Demand Prepared"
PX.Objects.IN.INLocationStatus.QtyProductionDemand : Edm.Decimal [required] "Qty On Production Demand"
PX.Objects.IN.INLocationStatus.QtyProductionAllocated : Edm.Decimal [required] "Qty On Production Allocated"
PX.Objects.IN.INLocationStatus.QtySOFixedProduction : Edm.Decimal [required] "Qty On SO to Production"
PX.Objects.IN.INLocationStatus.QtyFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPOFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPOFixedFSSrvOrdPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPOFixedFSSrvOrdReceipts : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyProdFixedPurchase : Edm.Decimal [required] "Qty On Production to Purchase"
PX.Objects.IN.INLocationStatus.QtyProdFixedProduction : Edm.Decimal [required] "Qty On Production to Production"
PX.Objects.IN.INLocationStatus.QtyProdFixedProdOrdersPrepared : Edm.Decimal [required] "Qty On Production for Prod. Prepared"
PX.Objects.IN.INLocationStatus.QtyProdFixedProdOrders : Edm.Decimal [required] "Qty On Production for Production"
PX.Objects.IN.INLocationStatus.QtyProdFixedSalesOrdersPrepared : Edm.Decimal [required] "Qty On Production for SO Prepared"
PX.Objects.IN.INLocationStatus.QtyProdFixedSalesOrders : Edm.Decimal [required] "Qty On Production for SO"
PX.Objects.IN.INLocationStatus.QtyMLFixedProduction : Edm.Decimal "Material to Production"
PX.Objects.IN.INLocationStatus.QtyProdFixedMLPrepared : Edm.Decimal "Production for Material Prepared"
PX.Objects.IN.INLocationStatus.QtyProdFixedML : Edm.Decimal "Production for Material"
PX.Objects.IN.INLocationStatus.QtySOFixed : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPOFixedOrders : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPOFixedPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPOFixedReceipts : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyMLToPurchase : Edm.Decimal [required] "Qty. Material to Purchase"
PX.Objects.IN.INLocationStatus.QtyPurchaseForML : Edm.Decimal [required] "Material Purchase"
PX.Objects.IN.INLocationStatus.QtyPurchaseForMLPrepared : Edm.Decimal [required] "Material Purchase Prepared"
PX.Objects.IN.INLocationStatus.QtyReceiptsForML : Edm.Decimal [required] "Material Receipts"
PX.Objects.IN.INLocationStatus.QtySODropShip : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPODropShipOrders : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPODropShipPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.QtyPODropShipReceipts : Edm.Decimal [required]
PX.Objects.IN.INLocationStatus.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLocationStatus.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLocationStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INLocationStatus.INItemSiteBySiteID -> PX.Objects.IN.INItemSite (InventoryID=InventoryID, SiteID=SiteID)
PX.Objects.IN.INLocationStatus.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INLocationStatus.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INLocationStatus.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INLocationStatus.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INLocationStatus.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INLocationStatus.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.INLocationStatus.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INLocationStatus.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INLocationStatus.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.INLocationStatus.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.INLocationStatus.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INLocationStatus.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INLocationStatus.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INLocationStatus.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.INLocationStatus.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INLocationStatus.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INLocationStatus.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.INLocationStatus.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.INLocationStatus.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)

# PX.Objects.IN.INLocationStatusByCostCenter (EntityType)

Label: "IN Location Status by Cost Center"
Key: CostCenterID, InventoryID, LocationID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INLocationStatusByCostCenter, INLocationStatusbyCostCenter
Non-filterable, non-selectable: Active, QtyNotAvail, QtyExpired

PX.Objects.IN.INLocationStatusByCostCenter.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INLocationStatusByCostCenter.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INLocationStatusByCostCenter.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INLocationStatusByCostCenter.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INLocationStatusByCostCenter.CostCenterID : Edm.Int32 [key]
PX.Objects.IN.INLocationStatusByCostCenter.CostLayerType : Edm.String
PX.Objects.IN.INLocationStatusByCostCenter.Active : Edm.Boolean "Active"
PX.Objects.IN.INLocationStatusByCostCenter.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INLocationStatusByCostCenter.QtyAvail : Edm.Decimal [required] "Qty. Available"
PX.Objects.IN.INLocationStatusByCostCenter.QtyNotAvail : Edm.Decimal
PX.Objects.IN.INLocationStatusByCostCenter.QtyExpired : Edm.Decimal
PX.Objects.IN.INLocationStatusByCostCenter.QtyHardAvail : Edm.Decimal [required] "Qty. Available for Shipping"
PX.Objects.IN.INLocationStatusByCostCenter.QtyActual : Edm.Decimal [required] "Qty. Available for Issue"
PX.Objects.IN.INLocationStatusByCostCenter.QtyInTransit : Edm.Decimal [required] "Qty. In-Transit"
PX.Objects.IN.INLocationStatusByCostCenter.QtyInTransitToSO : Edm.Decimal [required] "Qty. In Transit to SO"
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOOrders : Edm.Decimal [required] "Qty. Purchase Orders"
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOReceipts : Edm.Decimal [required] "Qty. Purchase Receipts"
PX.Objects.IN.INLocationStatusByCostCenter.QtySOBackOrdered : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtySOPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtySOBooked : Edm.Decimal [required] "Qty. SO Booked"
PX.Objects.IN.INLocationStatusByCostCenter.QtySOShipped : Edm.Decimal [required] "Qty. SO Shipped"
PX.Objects.IN.INLocationStatusByCostCenter.QtySOShipping : Edm.Decimal [required] "Qty. SO Shipping"
PX.Objects.IN.INLocationStatusByCostCenter.QtyMLPrepared : Edm.Decimal [required] "Qty. Material Prepared"
PX.Objects.IN.INLocationStatusByCostCenter.QtyMLBooked : Edm.Decimal [required] "Qty. Material Booked"
PX.Objects.IN.INLocationStatusByCostCenter.QtyMLDispatched : Edm.Decimal [required] "Qty. Material Dispatched"
PX.Objects.IN.INLocationStatusByCostCenter.QtyMLAllocated : Edm.Decimal [required] "Qty. Material Allocated"
PX.Objects.IN.INLocationStatusByCostCenter.QtyINIssues : Edm.Decimal [required] "Qty On Inventory Issues"
PX.Objects.IN.INLocationStatusByCostCenter.QtyINReceipts : Edm.Decimal [required] "Qty On Inventory Receipts"
PX.Objects.IN.INLocationStatusByCostCenter.QtyINAssemblyDemand : Edm.Decimal [required] "Qty Demanded by Kit Assembly"
PX.Objects.IN.INLocationStatusByCostCenter.QtyINAssemblySupply : Edm.Decimal [required] "Qty On Kit Assembly"
PX.Objects.IN.INLocationStatusByCostCenter.QtyInTransitToProduction : Edm.Decimal [required] "Qty In Transit to Production"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProductionSupplyPrepared : Edm.Decimal [required] "Qty Production Supply Prepared"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProductionSupply : Edm.Decimal [required] "Qty On Production Supply"
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOFixedProductionPrepared : Edm.Decimal [required] "Qty On Purchase for Prod. Prepared"
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOFixedProductionOrders : Edm.Decimal [required] "Qty On Purchase for Production"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProductionDemandPrepared : Edm.Decimal [required] "Qty On Production Demand Prepared"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProductionDemand : Edm.Decimal [required] "Qty On Production Demand"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProductionAllocated : Edm.Decimal [required] "Qty On Production Allocated"
PX.Objects.IN.INLocationStatusByCostCenter.QtySOFixedProduction : Edm.Decimal [required] "Qty On SO to Production"
PX.Objects.IN.INLocationStatusByCostCenter.QtyFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOFixedFSSrvOrdPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOFixedFSSrvOrdReceipts : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyProdFixedPurchase : Edm.Decimal [required] "Qty On Production to Purchase"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProdFixedProduction : Edm.Decimal [required] "Qty On Production to Production"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProdFixedProdOrdersPrepared : Edm.Decimal [required] "Qty On Production for Prod. Prepared"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProdFixedProdOrders : Edm.Decimal [required] "Qty On Production for Production"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProdFixedSalesOrdersPrepared : Edm.Decimal [required] "Qty On Production for SO Prepared"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProdFixedSalesOrders : Edm.Decimal [required] "Qty On Production for SO"
PX.Objects.IN.INLocationStatusByCostCenter.QtySOFixed : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOFixedOrders : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOFixedPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPOFixedReceipts : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyMLToPurchase : Edm.Decimal [required] "Qty. Material to Purchase"
PX.Objects.IN.INLocationStatusByCostCenter.QtyPurchaseForML : Edm.Decimal [required] "Material Purchase"
PX.Objects.IN.INLocationStatusByCostCenter.QtyPurchaseForMLPrepared : Edm.Decimal [required] "Material Purchase Prepared"
PX.Objects.IN.INLocationStatusByCostCenter.QtyReceiptsForML : Edm.Decimal [required] "Material Receipts"
PX.Objects.IN.INLocationStatusByCostCenter.QtyMLFixedProduction : Edm.Decimal [required] "Material to Production"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProdFixedMLPrepared : Edm.Decimal [required] "Production for Material Prepared"
PX.Objects.IN.INLocationStatusByCostCenter.QtyProdFixedML : Edm.Decimal [required] "Production for Material"
PX.Objects.IN.INLocationStatusByCostCenter.QtySODropShip : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPODropShipOrders : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPODropShipPrepared : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.QtyPODropShipReceipts : Edm.Decimal [required]
PX.Objects.IN.INLocationStatusByCostCenter.tstamp : Edm.Binary
PX.Objects.IN.INLocationStatusByCostCenter.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLocationStatusByCostCenter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLocationStatusByCostCenter.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INLocationStatusByCostCenter.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.IN.INLocationStatusByCostCenter.INItemSiteBySiteID -> PX.Objects.IN.INItemSite (InventoryID=InventoryID, SiteID=SiteID)
PX.Objects.IN.INLocationStatusByCostCenter.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INLocationStatusByCostCenter.INLocationBySiteID -> PX.Objects.IN.INLocation (LocationID=LocationID, SiteID=SiteID)
PX.Objects.IN.INLocationStatusByCostCenter.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INLocationStatusByCostCenter.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INLocationStatusByCostCenter.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INLocationStatusByCostCenter.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INLocationStatusByCostCenter.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)

# PX.Objects.IN.INLotSerClass (EntityType)

Label: "Lot/Serial Class"
Key: LotSerClassID
Entity sets: PX_Objects_IN_INLotSerClass, LotSerialClass, INLotSerClass
Non-filterable, non-selectable: IsManualAssignRequired, NoteText

PX.Objects.IN.INLotSerClass.LotSerClassID : Edm.String [key] "Class ID"
PX.Objects.IN.INLotSerClass.Descr : Edm.String "Description"
PX.Objects.IN.INLotSerClass.LotSerTrack : Edm.String "Tracking Method"
PX.Objects.IN.INLotSerClass.LotSerAssign : Edm.String "Assignment Method"
PX.Objects.IN.INLotSerClass.LotSerIssueMethod : Edm.String "Issue Method"
PX.Objects.IN.INLotSerClass.LotSerNumShared : Edm.Boolean [required] "Share Auto-Incremental Value Between All Class Items"
PX.Objects.IN.INLotSerClass.LotSerFormatStr : Edm.String
PX.Objects.IN.INLotSerClass.LotSerTrackExpiration : Edm.Boolean [required] "Track Expiration Date"
PX.Objects.IN.INLotSerClass.AutoNextNbr : Edm.Boolean [required] "Auto-Generate Next Number"
PX.Objects.IN.INLotSerClass.AutoSerialMaxCount : Edm.Int32 [required] "Max. Auto-Generate Numbers"
PX.Objects.IN.INLotSerClass.RequiredForDropship : Edm.Boolean [required] "Required for Drop-ship"
PX.Objects.IN.INLotSerClass.IsManualAssignRequired : Edm.Boolean
PX.Objects.IN.INLotSerClass.NoteID : Edm.Guid
PX.Objects.IN.INLotSerClass.NoteText : Edm.String "Note Text"
PX.Objects.IN.INLotSerClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INLotSerClass.CreatedByScreenID : Edm.String
PX.Objects.IN.INLotSerClass.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INLotSerClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INLotSerClass.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLotSerClass.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INLotSerClass.tstamp : Edm.Binary
PX.Objects.IN.INLotSerClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INLotSerClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INLotSerClass.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.IN.INLotSerClass.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INLotSerClass.INLotSerClassAttributeCollection -> Collection(PX.Objects.IN.INLotSerClassAttribute)
PX.Objects.IN.INLotSerClass.INLotSerClassLotSerNumValCollection -> Collection(PX.Objects.IN.INLotSerClassLotSerNumVal)
PX.Objects.IN.INLotSerClass.INLotSerSegmentCollection -> Collection(PX.Objects.IN.INLotSerSegment)
PX.Objects.IN.INLotSerClass.INSetupCollection -> Collection(PX.Objects.IN.INSetup)

# PX.Objects.IN.INLotSerClassAttribute (EntityType)

Label: "Lot/Serial Class Attribute"
Key: AttributeID, LotSerClassID
Entity sets: PX_Objects_IN_INLotSerClassAttribute, LotSerialClassAttribute, INLotSerClassAttribute

PX.Objects.IN.INLotSerClassAttribute.LotSerClassID : Edm.String [key] "Class ID"
PX.Objects.IN.INLotSerClassAttribute.AttributeID : Edm.String [key] "Attribute ID"
PX.Objects.IN.INLotSerClassAttribute.SortOrder : Edm.Int16 "Sort Order"
PX.Objects.IN.INLotSerClassAttribute.Required : Edm.Boolean [required] "Required"
PX.Objects.IN.INLotSerClassAttribute.IsActive : Edm.Boolean [required] "Active"
PX.Objects.IN.INLotSerClassAttribute.tstamp : Edm.Binary
PX.Objects.IN.INLotSerClassAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INLotSerClassAttribute.CreatedByScreenID : Edm.String
PX.Objects.IN.INLotSerClassAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLotSerClassAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INLotSerClassAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLotSerClassAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLotSerClassAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INLotSerClassAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INLotSerClassAttribute.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.IN.INLotSerClassAttribute.INLotSerClassByLotSerClassID -> PX.Objects.IN.INLotSerClass (LotSerClassID=LotSerClassID)

# PX.Objects.IN.INLotSerClassLotSerNumVal (EntityType)

Label: "Auto-Incremental Value of a Lot/Serial Class"
Key: LotSerClassID
Entity sets: PX_Objects_IN_INLotSerClassLotSerNumVal, AutoIncrementalValueofaLotSerialClass, INLotSerClassLotSerNumVal

PX.Objects.IN.INLotSerClassLotSerNumVal.LotSerClassID : Edm.String [key]
PX.Objects.IN.INLotSerClassLotSerNumVal.LotSerNumVal : Edm.String "Auto-Incremental Value"
PX.Objects.IN.INLotSerClassLotSerNumVal.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INLotSerClassLotSerNumVal.CreatedByScreenID : Edm.String
PX.Objects.IN.INLotSerClassLotSerNumVal.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INLotSerClassLotSerNumVal.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INLotSerClassLotSerNumVal.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLotSerClassLotSerNumVal.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLotSerClassLotSerNumVal.tstamp : Edm.Binary
PX.Objects.IN.INLotSerClassLotSerNumVal.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INLotSerClassLotSerNumVal.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INLotSerClassLotSerNumVal.INLotSerClassByLotSerClassID -> PX.Objects.IN.INLotSerClass (LotSerClassID=LotSerClassID)

# PX.Objects.IN.INLotSerialStatus (EntityType)

Label: "IN Lot/Serial Status"
Key: InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID
Entity sets: PX_Objects_IN_INLotSerialStatus, INLotSerialStatus
Non-filterable, non-selectable: QtyNotAvail, QtyExpired

PX.Objects.IN.INLotSerialStatus.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INLotSerialStatus.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INLotSerialStatus.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INLotSerialStatus.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INLotSerialStatus.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.INLotSerialStatus.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INLotSerialStatus.QtyAvail : Edm.Decimal [required] "Qty. Available"
PX.Objects.IN.INLotSerialStatus.QtyNotAvail : Edm.Decimal
PX.Objects.IN.INLotSerialStatus.QtyExpired : Edm.Decimal
PX.Objects.IN.INLotSerialStatus.QtyHardAvail : Edm.Decimal [required] "Qty. Hard Available"
PX.Objects.IN.INLotSerialStatus.QtyActual : Edm.Decimal [required] "Qty. Available for Issue"
PX.Objects.IN.INLotSerialStatus.QtyInTransit : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyInTransitToSO : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOOrders : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOReceipts : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtySOBackOrdered : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtySOPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtySOBooked : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtySOShipped : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtySOShipping : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyMLPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyMLBooked : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyMLDispatched : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyMLAllocated : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyINIssues : Edm.Decimal [required] "Qty On Inventory Issues"
PX.Objects.IN.INLotSerialStatus.QtyINReceipts : Edm.Decimal [required] "Qty On Inventory Receipts"
PX.Objects.IN.INLotSerialStatus.QtyINAssemblyDemand : Edm.Decimal [required] "Qty Demanded by Kit Assembly"
PX.Objects.IN.INLotSerialStatus.QtyINAssemblySupply : Edm.Decimal [required] "Qty On Kit Assembly"
PX.Objects.IN.INLotSerialStatus.QtyInTransitToProduction : Edm.Decimal [required] "Qty In Transit to Production"
PX.Objects.IN.INLotSerialStatus.QtyProductionSupplyPrepared : Edm.Decimal [required] "Qty Production Supply Prepared"
PX.Objects.IN.INLotSerialStatus.QtyProductionSupply : Edm.Decimal [required] "Qty On Production Supply"
PX.Objects.IN.INLotSerialStatus.QtyPOFixedProductionPrepared : Edm.Decimal [required] "Qty On Purchase for Prod. Prepared"
PX.Objects.IN.INLotSerialStatus.QtyPOFixedProductionOrders : Edm.Decimal [required] "Qty On Purchase for Production"
PX.Objects.IN.INLotSerialStatus.QtyProductionDemandPrepared : Edm.Decimal [required] "Qty On Production Demand Prepared"
PX.Objects.IN.INLotSerialStatus.QtyProductionDemand : Edm.Decimal [required] "Qty On Production Demand"
PX.Objects.IN.INLotSerialStatus.QtyProductionAllocated : Edm.Decimal [required] "Qty On Production Allocated"
PX.Objects.IN.INLotSerialStatus.QtySOFixedProduction : Edm.Decimal [required] "Qty On SO to Production"
PX.Objects.IN.INLotSerialStatus.QtyFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOFixedFSSrvOrdPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOFixedFSSrvOrdReceipts : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyProdFixedPurchase : Edm.Decimal [required] "Qty On Production to Purchase"
PX.Objects.IN.INLotSerialStatus.QtyProdFixedProduction : Edm.Decimal [required] "Qty On Production to Production"
PX.Objects.IN.INLotSerialStatus.QtyProdFixedProdOrdersPrepared : Edm.Decimal [required] "Qty On Production for Prod. Prepared"
PX.Objects.IN.INLotSerialStatus.QtyProdFixedProdOrders : Edm.Decimal [required] "Qty On Production for Production"
PX.Objects.IN.INLotSerialStatus.QtyProdFixedSalesOrdersPrepared : Edm.Decimal [required] "Qty On Production for SO Prepared"
PX.Objects.IN.INLotSerialStatus.QtyProdFixedSalesOrders : Edm.Decimal [required] "Qty On Production for SO"
PX.Objects.IN.INLotSerialStatus.QtyMLFixedProduction : Edm.Decimal "Material to Production"
PX.Objects.IN.INLotSerialStatus.QtyProdFixedMLPrepared : Edm.Decimal "Production for Material Prepared"
PX.Objects.IN.INLotSerialStatus.QtyProdFixedML : Edm.Decimal "Production for Material"
PX.Objects.IN.INLotSerialStatus.QtySOFixed : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOFixedOrders : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOFixedPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPOFixedReceipts : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyMLToPurchase : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPurchaseForML : Edm.Decimal [required] "Material Purchase"
PX.Objects.IN.INLotSerialStatus.QtyPurchaseForMLPrepared : Edm.Decimal [required] "Material Purchase Prepared"
PX.Objects.IN.INLotSerialStatus.QtyReceiptsForML : Edm.Decimal [required] "Material Receipts"
PX.Objects.IN.INLotSerialStatus.QtySODropShip : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPODropShipOrders : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPODropShipPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.QtyPODropShipReceipts : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatus.ExpireDate : Edm.DateTimeOffset "Expiry Date"
PX.Objects.IN.INLotSerialStatus.ReceiptDate : Edm.DateTimeOffset
PX.Objects.IN.INLotSerialStatus.LotSerTrack : Edm.String
PX.Objects.IN.INLotSerialStatus.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLotSerialStatus.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLotSerialStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INLotSerialStatus.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INLotSerialStatus.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INLotSerialStatus.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INLotSerialStatus.INItemLotSerialByLotSerialNbr -> PX.Objects.IN.INItemLotSerial (InventoryID=InventoryID, LotSerialNbr=LotSerialNbr)
PX.Objects.IN.INLotSerialStatus.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID, LocationID=LocationID)
PX.Objects.IN.INLotSerialStatus.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INLotSerialStatus.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.INLotSerialStatus.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INLotSerialStatus.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INLotSerialStatus.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INLotSerialStatus.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INLotSerialStatus.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INLotSerialStatus.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INLotSerialStatus.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.INLotSerialStatus.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INLotSerialStatus.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INLotSerialStatus.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.INLotSerialStatus.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)

# PX.Objects.IN.INLotSerialStatusByCostCenter (EntityType)

Label: "IN Lot/Serial Status by Cost Center"
Key: CostCenterID, InventoryID, LocationID, LotSerialNbr, SiteID, SubItemID
Entity sets: PX_Objects_IN_INLotSerialStatusByCostCenter, INLotSerialStatusbyCostCenter
Non-filterable, non-selectable: QtyNotAvail, QtyExpired

PX.Objects.IN.INLotSerialStatusByCostCenter.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INLotSerialStatusByCostCenter.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INLotSerialStatusByCostCenter.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INLotSerialStatusByCostCenter.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INLotSerialStatusByCostCenter.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.INLotSerialStatusByCostCenter.CostCenterID : Edm.Int32 [key]
PX.Objects.IN.INLotSerialStatusByCostCenter.CostLayerType : Edm.String
PX.Objects.IN.INLotSerialStatusByCostCenter.ExpireDate : Edm.DateTimeOffset "Expiry Date"
PX.Objects.IN.INLotSerialStatusByCostCenter.ReceiptDate : Edm.DateTimeOffset
PX.Objects.IN.INLotSerialStatusByCostCenter.LotSerTrack : Edm.String
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyAvail : Edm.Decimal [required] "Qty. Available"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyNotAvail : Edm.Decimal
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyExpired : Edm.Decimal
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyHardAvail : Edm.Decimal [required] "Qty. Available for Shipping"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyActual : Edm.Decimal [required] "Qty. Available for Issue"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyInTransit : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyInTransitToSO : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOOrders : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOReceipts : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtySOBackOrdered : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtySOPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtySOBooked : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtySOShipped : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtySOShipping : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyMLPrepared : Edm.Decimal [required] "Qty. Material Prepared"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyMLBooked : Edm.Decimal [required] "Qty. Material Booked"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyMLDispatched : Edm.Decimal [required] "Qty. Material Dispatched"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyMLAllocated : Edm.Decimal [required] "Qty. Material Allocated"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyINIssues : Edm.Decimal [required] "Qty On Inventory Issues"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyINReceipts : Edm.Decimal [required] "Qty On Inventory Receipts"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyINAssemblyDemand : Edm.Decimal [required] "Qty Demanded by Kit Assembly"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyINAssemblySupply : Edm.Decimal [required] "Qty On Kit Assembly"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyInTransitToProduction : Edm.Decimal [required] "Qty In Transit to Production"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProductionSupplyPrepared : Edm.Decimal [required] "Qty Production Supply Prepared"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProductionSupply : Edm.Decimal [required] "Qty On Production Supply"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOFixedProductionPrepared : Edm.Decimal [required] "Qty On Purchase for Prod. Prepared"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOFixedProductionOrders : Edm.Decimal [required] "Qty On Purchase for Production"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProductionDemandPrepared : Edm.Decimal [required] "Qty On Production Demand Prepared"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProductionDemand : Edm.Decimal [required] "Qty On Production Demand"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProductionAllocated : Edm.Decimal [required] "Qty On Production Allocated"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtySOFixedProduction : Edm.Decimal [required] "Qty On SO to Production"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOFixedFSSrvOrdPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOFixedFSSrvOrdReceipts : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProdFixedPurchase : Edm.Decimal [required] "Qty On Production to Purchase"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProdFixedProduction : Edm.Decimal [required] "Qty On Production to Production"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProdFixedProdOrdersPrepared : Edm.Decimal [required] "Qty On Production for Prod. Prepared"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProdFixedProdOrders : Edm.Decimal [required] "Qty On Production for Production"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProdFixedSalesOrdersPrepared : Edm.Decimal [required] "Qty On Production for SO Prepared"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProdFixedSalesOrders : Edm.Decimal [required] "Qty On Production for SO"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtySOFixed : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOFixedOrders : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOFixedPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPOFixedReceipts : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyMLToPurchase : Edm.Decimal [required] "Qty. Material to Purchase"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPurchaseForML : Edm.Decimal [required] "Material Purchase"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPurchaseForMLPrepared : Edm.Decimal [required] "Material Purchase Prepared"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyReceiptsForML : Edm.Decimal [required] "Material Receipts"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyMLFixedProduction : Edm.Decimal [required] "Material to Production"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProdFixedMLPrepared : Edm.Decimal [required] "Production for Material Prepared"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyProdFixedML : Edm.Decimal [required] "Production for Material"
PX.Objects.IN.INLotSerialStatusByCostCenter.QtySODropShip : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPODropShipOrders : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPODropShipPrepared : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.QtyPODropShipReceipts : Edm.Decimal [required]
PX.Objects.IN.INLotSerialStatusByCostCenter.tstamp : Edm.Binary
PX.Objects.IN.INLotSerialStatusByCostCenter.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLotSerialStatusByCostCenter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLotSerialStatusByCostCenter.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INLotSerialStatusByCostCenter.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.IN.INLotSerialStatusByCostCenter.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INLotSerialStatusByCostCenter.INLocationBySiteID -> PX.Objects.IN.INLocation (LocationID=LocationID, SiteID=SiteID)
PX.Objects.IN.INLotSerialStatusByCostCenter.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INLotSerialStatusByCostCenter.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INLotSerialStatusByCostCenter.INItemLotSerialByLotSerialNbr -> PX.Objects.IN.INItemLotSerial (InventoryID=InventoryID, LotSerialNbr=LotSerialNbr)
PX.Objects.IN.INLotSerialStatusByCostCenter.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID, LocationID=LocationID)
PX.Objects.IN.INLotSerialStatusByCostCenter.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.INLotSerialStatusByCostCenter.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INLotSerialStatusByCostCenter.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.INLotSerialStatusByCostCenter.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INLotSerialStatusByCostCenter.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INLotSerialStatusByCostCenter.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INLotSerialStatusByCostCenter.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INLotSerialStatusByCostCenter.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.INLotSerialStatusByCostCenter.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.INLotSerialStatusByCostCenter.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.INLotSerialStatusByCostCenter.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)

# PX.Objects.IN.INLotSerSegment (EntityType)

Label: "Lot/Serial Segment"
Key: LotSerClassID, SegmentID
Entity sets: PX_Objects_IN_INLotSerSegment, LotSerialSegment, INLotSerSegment

PX.Objects.IN.INLotSerSegment.LotSerClassID : Edm.String [key]
PX.Objects.IN.INLotSerSegment.SegmentID : Edm.Int16 [key] "Segment Number"
PX.Objects.IN.INLotSerSegment.SegmentType : Edm.String "Type"
PX.Objects.IN.INLotSerSegment.SegmentValue : Edm.String "Value"
PX.Objects.IN.INLotSerSegment.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INLotSerSegment.CreatedByScreenID : Edm.String
PX.Objects.IN.INLotSerSegment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLotSerSegment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INLotSerSegment.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INLotSerSegment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INLotSerSegment.tstamp : Edm.Binary
PX.Objects.IN.INLotSerSegment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INLotSerSegment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INLotSerSegment.INLotSerClassByLotSerClassID -> PX.Objects.IN.INLotSerClass (LotSerClassID=LotSerClassID)

# PX.Objects.IN.INMovementClass (EntityType)

Label: "IN Movement Class"
Key: MovementClassID
Entity sets: PX_Objects_IN_INMovementClass, INMovementClass

PX.Objects.IN.INMovementClass.MovementClassID : Edm.String [key] "Movement Class ID"
PX.Objects.IN.INMovementClass.Descr : Edm.String "Description"
PX.Objects.IN.INMovementClass.CountsPerYear : Edm.Int16 "Counts Per Year"
PX.Objects.IN.INMovementClass.MaxTurnoverPct : Edm.Decimal [required] "Max. Turnover %"
PX.Objects.IN.INMovementClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INMovementClass.CreatedByScreenID : Edm.String
PX.Objects.IN.INMovementClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INMovementClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INMovementClass.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INMovementClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INMovementClass.tstamp : Edm.Binary
PX.Objects.IN.INMovementClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INMovementClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INMovementClass.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INMovementClass.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INMovementClass.INPIClassCollection -> Collection(PX.Objects.IN.INPIClass)

# PX.Objects.IN.INNotification (EntityType)

Label: "Default Notification setup"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_IN_INNotification

# PX.Objects.IN.INOverheadTran (EntityType)

Label: "IN Overhead"
Key: DocType, LineNbr, RefNbr
Entity sets: PX_Objects_IN_INOverheadTran, INOverhead, INOverheadTran

PX.Objects.IN.INOverheadTran.BranchID : Edm.Int32 "Branch"
PX.Objects.IN.INOverheadTran.DocType : Edm.String [key]
PX.Objects.IN.INOverheadTran.OrigModule : Edm.String
PX.Objects.IN.INOverheadTran.TranType : Edm.String
PX.Objects.IN.INOverheadTran.RefNbr : Edm.String [key]
PX.Objects.IN.INOverheadTran.LineNbr : Edm.Int32 [key]
PX.Objects.IN.INOverheadTran.AssyType : Edm.String
PX.Objects.IN.INOverheadTran.ProjectID : Edm.Int32
PX.Objects.IN.INOverheadTran.TranDate : Edm.DateTimeOffset
PX.Objects.IN.INOverheadTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INOverheadTran.SiteID : Edm.Int32
PX.Objects.IN.INOverheadTran.InvtMult : Edm.Int16
PX.Objects.IN.INOverheadTran.UOM : Edm.String "UOM"
PX.Objects.IN.INOverheadTran.Qty : Edm.Decimal "Quantity"
PX.Objects.IN.INOverheadTran.FinPeriodID : Edm.String
PX.Objects.IN.INOverheadTran.TranDesc : Edm.String "Description"
PX.Objects.IN.INOverheadTran.BaseQty : Edm.Decimal
PX.Objects.IN.INOverheadTran.UnassignedQty : Edm.Decimal
PX.Objects.IN.INOverheadTran.Released : Edm.Boolean
PX.Objects.IN.INOverheadTran.TranPeriodID : Edm.String
PX.Objects.IN.INOverheadTran.UnitPrice : Edm.Decimal "Unit Price"
PX.Objects.IN.INOverheadTran.TranAmt : Edm.Decimal "Ext. Price"
PX.Objects.IN.INOverheadTran.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.IN.INOverheadTran.TranCost : Edm.Decimal "Ext. Cost"
PX.Objects.IN.INOverheadTran.UpdateShippedNotInvoiced : Edm.Boolean
PX.Objects.IN.INOverheadTran.CostLayerType : Edm.String
PX.Objects.IN.INOverheadTran.ToCostLayerType : Edm.String
PX.Objects.IN.INOverheadTran.InventorySource : Edm.String
PX.Objects.IN.INOverheadTran.ToInventorySource : Edm.String
PX.Objects.IN.INOverheadTran.CostCenterID : Edm.Int32
PX.Objects.IN.INOverheadTran.ToCostCenterID : Edm.Int32
PX.Objects.IN.INOverheadTran.IsUnassigned : Edm.Boolean
PX.Objects.IN.INOverheadTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INOverheadTran.CreatedByScreenID : Edm.String
PX.Objects.IN.INOverheadTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INOverheadTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INOverheadTran.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INOverheadTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INOverheadTran.Tstamp : Edm.Binary
PX.Objects.IN.INOverheadTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.IN.INOverheadTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INOverheadTran.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.IN.INOverheadTran.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INOverheadTran.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INOverheadTran.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INOverheadTran.INKitRegisterByRefNbr -> PX.Objects.IN.INKitRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INOverheadTran.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INOverheadTran.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INOverheadTran.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.INOverheadTran.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INOverheadTran.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INOverheadTran.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.INOverheadTran.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.Objects.IN.INOverheadTran.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.IN.INOverheadTran.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.IN.INOverheadTran.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INOverheadTran.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INOverheadTran.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.IN.INPIClass (EntityType)

Label: "Physical Inventory Type"
Key: PIClassID
Entity sets: PX_Objects_IN_INPIClass, PhysicalInventoryType, INPIClass
Non-filterable, non-selectable: ByABCFrequency, ByMovementClassFrequency, ByCycleFrequency

PX.Objects.IN.INPIClass.PIClassID : Edm.String [key] "Type ID"
PX.Objects.IN.INPIClass.Descr : Edm.String "Description"
PX.Objects.IN.INPIClass.Method : Edm.String "Generation Method"
PX.Objects.IN.INPIClass.CycleID : Edm.String "Cycle ID"
PX.Objects.IN.INPIClass.ABCCodeID : Edm.String "ABC Code"
PX.Objects.IN.INPIClass.MovementClassID : Edm.String "Movement Class ID"
PX.Objects.IN.INPIClass.SelectedMethod : Edm.String "Selection Method"
PX.Objects.IN.INPIClass.ByFrequency : Edm.Boolean [required]
PX.Objects.IN.INPIClass.ByABCFrequency : Edm.Boolean "By Frequency"
PX.Objects.IN.INPIClass.ByMovementClassFrequency : Edm.Boolean "By Frequency"
PX.Objects.IN.INPIClass.ByCycleFrequency : Edm.Boolean "By Frequency"
PX.Objects.IN.INPIClass.IncludeZeroItems : Edm.Boolean [required] "Include Items with Zero Book Quantity in PI"
PX.Objects.IN.INPIClass.HideBookQty : Edm.Boolean [required] "Hide Book Qty. on PI Count"
PX.Objects.IN.INPIClass.NAO1 : Edm.String "1"
PX.Objects.IN.INPIClass.NAO2 : Edm.String "2"
PX.Objects.IN.INPIClass.NAO3 : Edm.String "3"
PX.Objects.IN.INPIClass.NAO4 : Edm.String "4"
PX.Objects.IN.INPIClass.BlankLines : Edm.Int16 "Blank Lines To Append"
PX.Objects.IN.INPIClass.RandomItemsLimit : Edm.Int16 "Max. Number of Items"
PX.Objects.IN.INPIClass.LastCountPeriod : Edm.Int16 "Last Count Before (Days)"
PX.Objects.IN.INPIClass.UnlockSiteOnCountingFinish : Edm.Boolean [required] "Unfreeze Stock When Counting Is Finished"
PX.Objects.IN.INPIClass.tstamp : Edm.Binary
PX.Objects.IN.INPIClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIClass.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIClass.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INPIClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPIClass.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPIClass.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INPIClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPIClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPIClass.INABCCodeByABCCodeID -> PX.Objects.IN.INABCCode (ABCCodeID=ABCCodeID)
PX.Objects.IN.INPIClass.INMovementClassByMovementClassID -> PX.Objects.IN.INMovementClass (MovementClassID=MovementClassID)
PX.Objects.IN.INPIClass.INPICycleByCycleID -> PX.Objects.IN.INPICycle (CycleID=CycleID)
PX.Objects.IN.INPIClass.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INPIClass.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.Objects.IN.INPIClass.INPIClassItemClassCollection -> Collection(PX.Objects.IN.INPIClassItemClass)
PX.Objects.IN.INPIClass.INPIClassLocationCollection -> Collection(PX.Objects.IN.INPIClassLocation)
PX.Objects.IN.INPIClass.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)

# PX.Objects.IN.INPIClassItem (EntityType)

Label: "Physical Inventory Type by Item"
Key: InventoryID, PIClassID
Entity sets: PX_Objects_IN_INPIClassItem, PhysicalInventoryTypebyItem, INPIClassItem

PX.Objects.IN.INPIClassItem.PIClassID : Edm.String [key]
PX.Objects.IN.INPIClassItem.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INPIClassItem.tstamp : Edm.Binary
PX.Objects.IN.INPIClassItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIClassItem.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIClassItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIClassItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INPIClassItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPIClassItem.INPIClassByPIClassID -> PX.Objects.IN.INPIClass (PIClassID=PIClassID)

# PX.Objects.IN.INPIClassItemClass (EntityType)

Key: ItemClassID, PIClassID
Entity sets: PX_Objects_IN_INPIClassItemClass

PX.Objects.IN.INPIClassItemClass.PIClassID : Edm.String [key]
PX.Objects.IN.INPIClassItemClass.ItemClassID : Edm.Int32 [key] "Item Class ID"
PX.Objects.IN.INPIClassItemClass.tstamp : Edm.Binary
PX.Objects.IN.INPIClassItemClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIClassItemClass.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIClassItemClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIClassItemClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPIClassItemClass.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPIClassItemClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIClassItemClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPIClassItemClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPIClassItemClass.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.INPIClassItemClass.INPIClassByPIClassID -> PX.Objects.IN.INPIClass (PIClassID=PIClassID)

# PX.Objects.IN.INPIClassLocation (EntityType)

Label: "Physical Inventory Type by Location"
Key: LocationID, PIClassID
Entity sets: PX_Objects_IN_INPIClassLocation, PhysicalInventoryTypebyLocation, INPIClassLocation

PX.Objects.IN.INPIClassLocation.PIClassID : Edm.String [key]
PX.Objects.IN.INPIClassLocation.LocationID : Edm.Int32 [key] "Location"
PX.Objects.IN.INPIClassLocation.tstamp : Edm.Binary
PX.Objects.IN.INPIClassLocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIClassLocation.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIClassLocation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIClassLocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPIClassLocation.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.IN.INPIClassLocation.INPIClassByPIClassID -> PX.Objects.IN.INPIClass (PIClassID=PIClassID)

# PX.Objects.IN.INPICycle (EntityType)

Label: "Physical Inventory Cycle"
Key: CycleID
Entity sets: PX_Objects_IN_INPICycle, PhysicalInventoryCycle, INPICycle

PX.Objects.IN.INPICycle.CycleID : Edm.String [key] "Cycle ID"
PX.Objects.IN.INPICycle.Descr : Edm.String "Description"
PX.Objects.IN.INPICycle.CountsPerYear : Edm.Int16 [required] "Counts Per Year"
PX.Objects.IN.INPICycle.MaxCountInaccuracyPct : Edm.Decimal "Max. Count Inaccuracy %"
PX.Objects.IN.INPICycle.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPICycle.CreatedByScreenID : Edm.String
PX.Objects.IN.INPICycle.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPICycle.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPICycle.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPICycle.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPICycle.tstamp : Edm.Binary
PX.Objects.IN.INPICycle.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPICycle.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPICycle.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INPICycle.INPIClassCollection -> Collection(PX.Objects.IN.INPIClass)

# PX.Objects.IN.INPIDetail (EntityType)

Label: "IN Physical count Detail"
Key: LineNbr, PIID
Entity sets: PX_Objects_IN_INPIDetail, INPhysicalcountDetail, INPIDetail
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INPIDetail.PIID : Edm.String [key] "Reference Nbr."
PX.Objects.IN.INPIDetail.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.IN.INPIDetail.TagNumber : Edm.Int32 "Tag Nbr."
PX.Objects.IN.INPIDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INPIDetail.ManualCost : Edm.Boolean [required] "Manual Cost"
PX.Objects.IN.INPIDetail.BookQty : Edm.Decimal "Book Quantity"
PX.Objects.IN.INPIDetail.PhysicalQty : Edm.Decimal "Physical Quantity"
PX.Objects.IN.INPIDetail.VarQty : Edm.Decimal "Variance Quantity"
PX.Objects.IN.INPIDetail.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.IN.INPIDetail.ReasonCode : Edm.String "Reason Code"
PX.Objects.IN.INPIDetail.ExtVarCost : Edm.Decimal "Estimated Ext. Variance Cost"
PX.Objects.IN.INPIDetail.FinalExtVarCost : Edm.Decimal "Final Ext. Variance Cost"
PX.Objects.IN.INPIDetail.Status : Edm.String "Status"
PX.Objects.IN.INPIDetail.NoteID : Edm.Guid
PX.Objects.IN.INPIDetail.NoteText : Edm.String "Note Text"
PX.Objects.IN.INPIDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIDetail.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPIDetail.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPIDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIDetail.tstamp : Edm.Binary
PX.Objects.IN.INPIDetail.LineType : Edm.String "Line Type"
PX.Objects.IN.INPIDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INPIDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPIDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPIDetail.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.IN.INPIDetail.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INPIDetail.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.INPIDetail.INPIHeaderByPIID -> PX.Objects.IN.INPIHeader (PIID=PIID)
PX.Objects.IN.INPIDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INPIDetail.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INPIDetail.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.IN.INPIDetail.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.IN.INPIDetail.INTranCollection -> Collection(PX.Objects.IN.INTran)

# PX.Objects.IN.INPIHeader (EntityType)

Label: "Physical Inventory Review"
Key: PIID
Entity sets: PX_Objects_IN_INPIHeader, PhysicalInventoryReview, INPIHeader
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INPIHeader.PIID : Edm.String [key] "Reference Nbr."
PX.Objects.IN.INPIHeader.PIClassID : Edm.String
PX.Objects.IN.INPIHeader.Descr : Edm.String "Description"
PX.Objects.IN.INPIHeader.LineCntr : Edm.Int32 [required] "Number Of Lines"
PX.Objects.IN.INPIHeader.TagNumbered : Edm.Boolean "Tag Numbered"
PX.Objects.IN.INPIHeader.FirstTagNbr : Edm.Int32
PX.Objects.IN.INPIHeader.FinPeriodID : Edm.String
PX.Objects.IN.INPIHeader.TranPeriodID : Edm.String
PX.Objects.IN.INPIHeader.Status : Edm.String "Status"
PX.Objects.IN.INPIHeader.CountDate : Edm.DateTimeOffset "Freeze Date"
PX.Objects.IN.INPIHeader.PIAdjRefNbr : Edm.String "Adjustment Ref. Nbr."
PX.Objects.IN.INPIHeader.PIRcptRefNbr : Edm.String "Receipt Ref. Nbr."
PX.Objects.IN.INPIHeader.TotalPhysicalQty : Edm.Decimal "Total Physical Qty."
PX.Objects.IN.INPIHeader.TotalVarQty : Edm.Decimal "Total Variance Qty."
PX.Objects.IN.INPIHeader.TotalVarCost : Edm.Decimal "Total Variance Cost"
PX.Objects.IN.INPIHeader.TotalNbrOfTags : Edm.Int32 [required] "Number Of Tags"
PX.Objects.IN.INPIHeader.NoteID : Edm.Guid
PX.Objects.IN.INPIHeader.NoteText : Edm.String "Note Text"
PX.Objects.IN.INPIHeader.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIHeader.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIHeader.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INPIHeader.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPIHeader.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPIHeader.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INPIHeader.tstamp : Edm.Binary
PX.Objects.IN.INPIHeader.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPIHeader.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPIHeader.INPIClassByPIClassID -> PX.Objects.IN.INPIClass (PIClassID=PIClassID)
PX.Objects.IN.INPIHeader.INRegisterByPIAdjRefNbr -> PX.Objects.IN.INRegister (PIAdjRefNbr=RefNbr)
PX.Objects.IN.INPIHeader.INRegisterByPIRcptRefNbr -> PX.Objects.IN.INRegister (PIRcptRefNbr=RefNbr)
PX.Objects.IN.INPIHeader.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INPIHeader.AccountByPIAdjAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPIHeader.SubByPIAdjSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPIHeader.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INPIHeader.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.INPIHeader.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.INPIHeader.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.IN.INPIHeader.INPIStatusLocCollection -> Collection(PX.Objects.IN.INPIStatusLoc)
PX.Objects.IN.INPIHeader.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)

# PX.Objects.IN.INPIStatus (EntityType)

Label: "Physical Inventory Status"
Key: LocRecordID, RecordID
Entity sets: PX_Objects_IN_INPIStatus, PhysicalInventoryStatus, INPIStatus

PX.Objects.IN.INPIStatus.RecordID : Edm.Int32 [key]
PX.Objects.IN.INPIStatus.LocRecordID : Edm.Int32 [key]
PX.Objects.IN.INPIStatus.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INPIStatus.Active : Edm.Boolean [required] "Active"
PX.Objects.IN.INPIStatus.PIID : Edm.String "Physical Count ID"
PX.Objects.IN.INPIStatus.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIStatus.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIStatus.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIStatus.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPIStatus.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPIStatus.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INPIStatus.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INPIStatus.INPIHeaderByPIID -> PX.Objects.IN.INPIHeader (PIID=PIID)
PX.Objects.IN.INPIStatus.INSiteBySiteID -> PX.Objects.IN.INSite

# PX.Objects.IN.INPIStatusItem (EntityType)

Key: RecordID
Entity sets: PX_Objects_IN_INPIStatusItem

PX.Objects.IN.INPIStatusItem.RecordID : Edm.Int32 [key]
PX.Objects.IN.INPIStatusItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INPIStatusItem.Active : Edm.Boolean [required] "Frozen"
PX.Objects.IN.INPIStatusItem.PIID : Edm.String "Physical Count ID"
PX.Objects.IN.INPIStatusItem.Excluded : Edm.Boolean [required] "Excluded"
PX.Objects.IN.INPIStatusItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIStatusItem.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIStatusItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIStatusItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPIStatusItem.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPIStatusItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIStatusItem.tstamp : Edm.Binary
PX.Objects.IN.INPIStatusItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INPIStatusItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPIStatusItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPIStatusItem.INPIHeaderByPIID -> PX.Objects.IN.INPIHeader (PIID=PIID)
PX.Objects.IN.INPIStatusItem.INSiteBySiteID -> PX.Objects.IN.INSite

# PX.Objects.IN.INPIStatusLoc (EntityType)

Key: RecordID
Entity sets: PX_Objects_IN_INPIStatusLoc

PX.Objects.IN.INPIStatusLoc.RecordID : Edm.Int32 [key]
PX.Objects.IN.INPIStatusLoc.Active : Edm.Boolean [required] "Frozen"
PX.Objects.IN.INPIStatusLoc.PIID : Edm.String "Physical Count ID"
PX.Objects.IN.INPIStatusLoc.Excluded : Edm.Boolean [required] "Excluded"
PX.Objects.IN.INPIStatusLoc.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPIStatusLoc.CreatedByScreenID : Edm.String
PX.Objects.IN.INPIStatusLoc.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIStatusLoc.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPIStatusLoc.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPIStatusLoc.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPIStatusLoc.tstamp : Edm.Binary
PX.Objects.IN.INPIStatusLoc.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPIStatusLoc.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPIStatusLoc.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INPIStatusLoc.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.INPIStatusLoc.INPIHeaderByPIID -> PX.Objects.IN.INPIHeader (PIID=PIID)
PX.Objects.IN.INPIStatusLoc.INSiteBySiteID -> PX.Objects.IN.INSite

# PX.Objects.IN.INPlanType (EntityType)

Label: "IN Item Plan Type"
Key: PlanType
Entity sets: PX_Objects_IN_INPlanType, INItemPlanType, INPlanType
Non-filterable, non-selectable: LocalizedDescr, DeleteOperation

PX.Objects.IN.INPlanType.PlanType : Edm.String [key] "Plan Type"
PX.Objects.IN.INPlanType.Descr : Edm.String "Description"
PX.Objects.IN.INPlanType.LocalizedDescr : Edm.String "Description"
PX.Objects.IN.INPlanType.IsFixed : Edm.Boolean [required] "Is Fixed"
PX.Objects.IN.INPlanType.IsSupply : Edm.Boolean [required] "Is Supply"
PX.Objects.IN.INPlanType.IsDemand : Edm.Boolean [required] "Is Demand"
PX.Objects.IN.INPlanType.IsForDate : Edm.Boolean [required] "Planned for Date"
PX.Objects.IN.INPlanType.InclQtySOBackOrdered : Edm.Int16 [required] "SO Back Ordered"
PX.Objects.IN.INPlanType.InclQtySOPrepared : Edm.Int16 [required] "SO Prepared"
PX.Objects.IN.INPlanType.InclQtySOBooked : Edm.Int16 [required] "SO Booked"
PX.Objects.IN.INPlanType.InclQtySOShipped : Edm.Int16 [required] "SO Shipped"
PX.Objects.IN.INPlanType.InclQtySOShipping : Edm.Int16 [required] "SO Allocated"
PX.Objects.IN.INPlanType.InclQtyMLPrepared : Edm.Int16 [required] "Material Prepared"
PX.Objects.IN.INPlanType.InclQtyMLBooked : Edm.Int16 [required] "Material Booked"
PX.Objects.IN.INPlanType.InclQtyMLDispatched : Edm.Int16 [required] "Material Dispatched"
PX.Objects.IN.INPlanType.InclQtyMLAllocated : Edm.Int16 [required] "Material Allocated"
PX.Objects.IN.INPlanType.InclQtyInTransit : Edm.Int16 [required] "In-Transit"
PX.Objects.IN.INPlanType.InclQtyInTransitToSO : Edm.Int16 [required] "In-Transit to SO"
PX.Objects.IN.INPlanType.InclQtyPOReceipts : Edm.Int16 [required] "PO Receipt"
PX.Objects.IN.INPlanType.InclQtyPOPrepared : Edm.Int16 [required] "PO Prepared"
PX.Objects.IN.INPlanType.InclQtyPOOrders : Edm.Int16 [required] "PO Order"
PX.Objects.IN.INPlanType.InclQtyINIssues : Edm.Int16 [required] "IN Issues"
PX.Objects.IN.INPlanType.InclQtyINReceipts : Edm.Int16 [required] "IN Receipts"
PX.Objects.IN.INPlanType.InclQtyINAssemblyDemand : Edm.Int16 [required] "IN Assembly Demand"
PX.Objects.IN.INPlanType.InclQtyINAssemblySupply : Edm.Int16 [required] "IN Assembly Supply"
PX.Objects.IN.INPlanType.InclQtyInTransitToProduction : Edm.Int16 [required] "In Transit to Production"
PX.Objects.IN.INPlanType.InclQtyProductionSupplyPrepared : Edm.Int16 [required] "Production Supply Prepared"
PX.Objects.IN.INPlanType.InclQtyProductionSupply : Edm.Int16 [required] "Production Supply"
PX.Objects.IN.INPlanType.InclQtyPOFixedProductionPrepared : Edm.Int16 [required] "Purchase for Prod. Prepared"
PX.Objects.IN.INPlanType.InclQtyPOFixedProductionOrders : Edm.Int16 [required] "Purchase for Production"
PX.Objects.IN.INPlanType.InclQtyProductionDemandPrepared : Edm.Int16 [required] "Production Demand Prepared"
PX.Objects.IN.INPlanType.InclQtyProductionDemand : Edm.Int16 [required] "Production Demand"
PX.Objects.IN.INPlanType.InclQtyProductionAllocated : Edm.Int16 [required] "Production Allocated"
PX.Objects.IN.INPlanType.InclQtySOFixedProduction : Edm.Int16 [required] "SO to Production"
PX.Objects.IN.INPlanType.InclQtyProdFixedPurchase : Edm.Int16 [required] "Production to Purchase"
PX.Objects.IN.INPlanType.InclQtyProdFixedProduction : Edm.Int16 [required] "Production to Production"
PX.Objects.IN.INPlanType.InclQtyProdFixedProdOrdersPrepared : Edm.Int16 [required] "Production for Prod. Prepared"
PX.Objects.IN.INPlanType.InclQtyProdFixedProdOrders : Edm.Int16 [required] "Production for Production"
PX.Objects.IN.INPlanType.InclQtyProdFixedSalesOrdersPrepared : Edm.Int16 [required] "Production for SO Prepared"
PX.Objects.IN.INPlanType.InclQtyProdFixedSalesOrders : Edm.Int16 [required] "Production for SO"
PX.Objects.IN.INPlanType.InclQtyINReplaned : Edm.Int16 [required] "IN Replanned"
PX.Objects.IN.INPlanType.InclQtySOFixed : Edm.Int16 [required] "SO to Purchase"
PX.Objects.IN.INPlanType.InclQtyPOFixedOrders : Edm.Int16 [required] "Purchase for SO"
PX.Objects.IN.INPlanType.InclQtyPOFixedPrepared : Edm.Int16 [required] "Purchase for SO Prepared"
PX.Objects.IN.INPlanType.InclQtyPOFixedReceipts : Edm.Int16 [required] "Receipts for SO"
PX.Objects.IN.INPlanType.InclQtyMLToPurchase : Edm.Int16 [required] "Material to Purchase"
PX.Objects.IN.INPlanType.InclQtyPurchaseForML : Edm.Int16 [required] "Material Purchase"
PX.Objects.IN.INPlanType.InclQtyPurchaseForMLPrepared : Edm.Int16 [required] "Material Purchase Prepared"
PX.Objects.IN.INPlanType.InclQtyReceiptsForML : Edm.Int16 [required] "Material Receipts"
PX.Objects.IN.INPlanType.InclQtySODropShip : Edm.Int16 [required] "SO to Drop-Ship"
PX.Objects.IN.INPlanType.InclQtyPODropShipOrders : Edm.Int16 [required] "Drop-Ship for SO"
PX.Objects.IN.INPlanType.InclQtyPODropShipPrepared : Edm.Int16 [required] "Drop-Ship for SO Prepared"
PX.Objects.IN.INPlanType.InclQtyPODropShipReceipts : Edm.Int16 [required] "Drop-Ship for SO Receipts"
PX.Objects.IN.INPlanType.DeleteOnEvent : Edm.Boolean [required] "Delete On Event"
PX.Objects.IN.INPlanType.ReplanOnEvent : Edm.String "Replan On Event"
PX.Objects.IN.INPlanType.DeleteOperation : Edm.Boolean
PX.Objects.IN.INPlanType.tstamp : Edm.Binary
PX.Objects.IN.INPlanType.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.INPlanType.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INPlanType.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INPlanType.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INPlanType.SOOrderTypeCollection -> Collection(PX.Objects.SO.SOOrderType)
PX.Objects.IN.INPlanType.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INPlanType.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INPlanType.SOOrderTypeOperationCollection -> Collection(PX.Objects.SO.SOOrderTypeOperation)
PX.Objects.IN.INPlanType.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INPlanType.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INPlanType.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INPlanType.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INPlanType.SOShipLineSplitForPackingCollection -> Collection(PX.Objects.SO.Report.SOShipLineSplitForPacking)

# PX.Objects.IN.INPostClass (EntityType)

Label: "Posting Class"
Key: PostClassID
Entity sets: PX_Objects_IN_INPostClass, PostingClass, INPostClass
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INPostClass.PostClassID : Edm.String [key] "Class ID"
PX.Objects.IN.INPostClass.Descr : Edm.String "Description"
PX.Objects.IN.INPostClass.PIReasonCode : Edm.String "Phys.Inventory Reason Code"
PX.Objects.IN.INPostClass.CorrectionReasonCode : Edm.String "Purchase Receipt Correction Reason Code"
PX.Objects.IN.INPostClass.InvtAcctDefault : Edm.String "Use Inventory/Accrual Account from"
PX.Objects.IN.INPostClass.COGSAcctDefault : Edm.String "Use COGS/Expense Account from"
PX.Objects.IN.INPostClass.SalesAcctDefault : Edm.String "Use Sales Account from"
PX.Objects.IN.INPostClass.StdCstRevAcctDefault : Edm.String "Use Std. Cost Revaluation Account from"
PX.Objects.IN.INPostClass.StdCstVarAcctDefault : Edm.String "Use Std. Cost Variance Account from"
PX.Objects.IN.INPostClass.PPVAcctDefault : Edm.String "Use Purchase Price Variance Account from"
PX.Objects.IN.INPostClass.POAccrualAcctDefault : Edm.String "Use PO Accrual Account from"
PX.Objects.IN.INPostClass.LCVarianceAcctDefault : Edm.String "Use Landed Cost Variance Account from"
PX.Objects.IN.INPostClass.NoteID : Edm.Guid
PX.Objects.IN.INPostClass.NoteText : Edm.String "Note Text"
PX.Objects.IN.INPostClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPostClass.CreatedByScreenID : Edm.String
PX.Objects.IN.INPostClass.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INPostClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPostClass.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPostClass.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INPostClass.tstamp : Edm.Binary
PX.Objects.IN.INPostClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPostClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPostClass.ReasonCodeByPIReasonCode -> PX.Objects.CS.ReasonCode (PIReasonCode=ReasonCodeID)
PX.Objects.IN.INPostClass.ReasonCodeByCorrectionReasonCode -> PX.Objects.CS.ReasonCode (CorrectionReasonCode=ReasonCodeID)
PX.Objects.IN.INPostClass.AccountByInvtAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.AccountByStdCstRevAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.AccountByPPVAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.AccountByStdCstVarAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.AccountByLCVarianceAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.AccountByDeferralAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INPostClass.SubByReasonCodeSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubByInvtSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubByCOGSSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubByStdCstRevSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubByPPVSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubByStdCstVarSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubByLCVarianceSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.SubByDeferralSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INPostClass.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.IN.INPostClass.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INPostClass.INSetupCollection -> Collection(PX.Objects.IN.INSetup)

# PX.Objects.IN.INPriceClass (EntityType)

Label: "IN Item Price Class"
Key: PriceClassID
Entity sets: PX_Objects_IN_INPriceClass, INItemPriceClass, INPriceClass
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INPriceClass.PriceClassID : Edm.String [key] "Price Class ID"
PX.Objects.IN.INPriceClass.Description : Edm.String "Description"
PX.Objects.IN.INPriceClass.NoteID : Edm.Guid
PX.Objects.IN.INPriceClass.NoteText : Edm.String "Note Text"
PX.Objects.IN.INPriceClass.tstamp : Edm.Binary
PX.Objects.IN.INPriceClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INPriceClass.CreatedByScreenID : Edm.String
PX.Objects.IN.INPriceClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPriceClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INPriceClass.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INPriceClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INPriceClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INPriceClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INPriceClass.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.IN.INPriceClass.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INPriceClass.DiscountInventoryPriceClassCollection -> Collection(PX.Objects.AR.DiscountInventoryPriceClass)
PX.Objects.IN.INPriceClass.SVMarkupCollection -> Collection(PX.Objects.SV.SVMarkup)
PX.Objects.IN.INPriceClass.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.INPriceClass.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)

# PX.Objects.IN.INRegister (EntityType)

Label: "Receipt"
Key: DocType, RefNbr
Entity sets: PX_Objects_IN_INRegister, Receipt, INRegister
Non-filterable, non-selectable: SrcDocType, SrcRefNbr, ReleasedToVerify, NoteText

PX.Objects.IN.INRegister.DocType : Edm.String [key] "Document Type"
PX.Objects.IN.INRegister.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.IN.INRegister.OrigModule : Edm.String "Source"
PX.Objects.IN.INRegister.OrigRefNbr : Edm.String
PX.Objects.IN.INRegister.SrcDocType : Edm.String
PX.Objects.IN.INRegister.SrcRefNbr : Edm.String
PX.Objects.IN.INRegister.ToSiteID : Edm.Int32 "To Warehouse ID"
PX.Objects.IN.INRegister.TransferType : Edm.String "Transfer Type"
PX.Objects.IN.INRegister.TransferNbr : Edm.String "Transfer Nbr."
PX.Objects.IN.INRegister.TranDesc : Edm.String "Description"
PX.Objects.IN.INRegister.Released : Edm.Boolean [required]
PX.Objects.IN.INRegister.ReleasedToVerify : Edm.Boolean
PX.Objects.IN.INRegister.Hold : Edm.Boolean "Hold"
PX.Objects.IN.INRegister.Status : Edm.String "Status"
PX.Objects.IN.INRegister.Approved : Edm.Boolean
PX.Objects.IN.INRegister.Rejected : Edm.Boolean [required]
PX.Objects.IN.INRegister.TranDate : Edm.DateTimeOffset "Date"
PX.Objects.IN.INRegister.FinPeriodID : Edm.String "Post Period"
PX.Objects.IN.INRegister.TranPeriodID : Edm.String
PX.Objects.IN.INRegister.LineCntr : Edm.Int32 [required]
PX.Objects.IN.INRegister.TotalQty : Edm.Decimal [required] "Total Qty."
PX.Objects.IN.INRegister.TotalAmount : Edm.Decimal [required] "Total Amount"
PX.Objects.IN.INRegister.TotalCost : Edm.Decimal [required] "Total Cost"
PX.Objects.IN.INRegister.ControlQty : Edm.Decimal [required] "Control Qty."
PX.Objects.IN.INRegister.ControlAmount : Edm.Decimal [required] "Control Amount"
PX.Objects.IN.INRegister.ControlCost : Edm.Decimal [required] "Control Cost"
PX.Objects.IN.INRegister.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.IN.INRegister.ExtRefNbr : Edm.String "External Ref."
PX.Objects.IN.INRegister.KitInventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INRegister.KitRevisionID : Edm.String "Revision"
PX.Objects.IN.INRegister.KitLineNbr : Edm.Int32
PX.Objects.IN.INRegister.KitRequestDate : Edm.DateTimeOffset "Requested On"
PX.Objects.IN.INRegister.SOOrderType : Edm.String "SO Order Type"
PX.Objects.IN.INRegister.SOOrderNbr : Edm.String "SO Order Nbr."
PX.Objects.IN.INRegister.SOShipmentType : Edm.String
PX.Objects.IN.INRegister.SOShipmentNbr : Edm.String "SO Shipment Nbr."
PX.Objects.IN.INRegister.POReceiptType : Edm.String "PO Receipt Type"
PX.Objects.IN.INRegister.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.IN.INRegister.PIID : Edm.String "PI Count Reference Nbr."
PX.Objects.IN.INRegister.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.IN.INRegister.OwnerID : Edm.Int32 "Owner"
PX.Objects.IN.INRegister.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INRegister.CreatedByScreenID : Edm.String
PX.Objects.IN.INRegister.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INRegister.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INRegister.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INRegister.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INRegister.NoteID : Edm.Guid
PX.Objects.IN.INRegister.NoteText : Edm.String "Note Text"
PX.Objects.IN.INRegister.tstamp : Edm.Binary
PX.Objects.IN.INRegister.IsPPVTran : Edm.Boolean [required]
PX.Objects.IN.INRegister.IsTaxAdjustmentTran : Edm.Boolean [required]
PX.Objects.IN.INRegister.IsCorrection : Edm.Boolean [required]
PX.Objects.IN.INRegister.OrigReceiptNbr : Edm.String
PX.Objects.IN.INRegister.IgnoreAllocationErrors : Edm.Boolean [required] "Ignore Item Allocations"
PX.Objects.IN.INRegister.INTranByKitLineNbr -> PX.Objects.IN.INTran (DocType=DocType, RefNbr=RefNbr, KitLineNbr=LineNbr)
PX.Objects.IN.INRegister.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.IN.INRegister.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.IN.INRegister.InventoryItemByKitInventoryID -> PX.Objects.IN.InventoryItem (KitInventoryID=InventoryID)
PX.Objects.IN.INRegister.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.IN.INRegister.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.IN.INRegister.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.IN.INRegister.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INRegister.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INRegister.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.IN.INRegister.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.IN.INRegister.SOShipmentBySOShipmentNbr -> PX.Objects.SO.SOShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr)
PX.Objects.IN.INRegister.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.IN.INRegister.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.IN.INRegister.INKitSpecHdrByKitRevisionID -> PX.Objects.IN.INKitSpecHdr (KitInventoryID=KitInventoryID, KitRevisionID=RevisionID)
PX.Objects.IN.INRegister.INPIHeaderByPIID -> PX.Objects.IN.INPIHeader (PIID=PIID)
PX.Objects.IN.INRegister.INRegisterByRefNbr -> PX.Objects.IN.INRegister (RefNbr=OrigReceiptNbr)
PX.Objects.IN.INRegister.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INRegister.INSiteByToSiteID -> PX.Objects.IN.INSite (ToSiteID=SiteID)
PX.Objects.IN.INRegister.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.IN.INRegister.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.IN.INRegister.SOBlanketOrderDisplayLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderDisplayLink)
PX.Objects.IN.INRegister.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.IN.INRegister.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INRegister.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INRegister.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.INRegister.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.IN.INRegister.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INRegister.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INRegister.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.INRegister.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INRegister.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.IN.INRegister.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.IN.INRegister.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.IN.INRegister.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.IN.INRegister.MNMaterialListShipmentCollection -> Collection(PX.Objects.MN.MNMaterialListShipment)
PX.Objects.IN.INRegister.INKitSerialPartCollection -> Collection(PX.Objects.IN.INKitSerialPart)
PX.Objects.IN.INRegister.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.Objects.IN.INRegister.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.INRegister.INRegisterCartCollection -> Collection(PX.Objects.IN.DAC.INRegisterCart)
PX.Objects.IN.INRegister.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.Objects.IN.INRegister.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.IN.INRegister.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.IN.INRegister.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.IN.INRegister.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INRegister.POAccrualInquiryResultCollection -> Collection(PX.Objects.PO.POAccrualInquiryResult)
PX.Objects.IN.INRegister.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)
PX.Objects.IN.INRegister.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.IN.INRegister.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INRegister.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.INRegister.POCartReceiptCollection -> Collection(PX.Objects.PO.POCartReceipt)
PX.Objects.IN.INRegister.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)
PX.Objects.IN.INRegister.AdjustmentTranBySiteLotSerialCollection -> Collection(PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteLotSerial)
PX.Objects.IN.INRegister.AdjustmentTranBySiteStatusCollection -> Collection(PX.Objects.IN.AffectedAvailability.AdjustmentTranBySiteStatus)

# PX.Objects.IN.INReplenishmentClass (EntityType)

Label: "Replenishment Class"
Key: ReplenishmentClassID
Entity sets: PX_Objects_IN_INReplenishmentClass, ReplenishmentClass, INReplenishmentClass

PX.Objects.IN.INReplenishmentClass.ReplenishmentClassID : Edm.String [key] "Class ID"
PX.Objects.IN.INReplenishmentClass.Descr : Edm.String "Description"
PX.Objects.IN.INReplenishmentClass.ReplenishmentSource : Edm.String "Replenishment Source"
PX.Objects.IN.INReplenishmentClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INReplenishmentClass.CreatedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INReplenishmentClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INReplenishmentClass.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INReplenishmentClass.tstamp : Edm.Binary
PX.Objects.IN.INReplenishmentClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INReplenishmentClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INReplenishmentClass.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.IN.INReplenishmentClass.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INReplenishmentClass.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.IN.INReplenishmentClass.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.IN.INReplenishmentClass.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)

# PX.Objects.IN.INReplenishmentItem (EntityType)

BaseType: PX.Objects.IN.S.INItemSite
Key: InventoryID, SiteID (inherited from PX.Objects.IN.S.INItemSite)
Entity sets: PX_Objects_IN_INReplenishmentItem
Non-filterable, non-selectable: QtyProcess, QtyProcessRounded

PX.Objects.IN.INReplenishmentItem.InventoryCD : Edm.String
PX.Objects.IN.INReplenishmentItem.SiteCD : Edm.String "Warehouse ID"
PX.Objects.IN.INReplenishmentItem.SubItemCD : Edm.String "Subitem ID"
PX.Objects.IN.INReplenishmentItem.Descr : Edm.String "Description"
PX.Objects.IN.INReplenishmentItem.PreferredVendorName : Edm.String "Preferred Vendor Name"
PX.Objects.IN.INReplenishmentItem.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.IN.INReplenishmentItem.BaseUnit : Edm.String "UOM"
PX.Objects.IN.INReplenishmentItem.PurchaseUnit : Edm.String "Purchase UOM"
PX.Objects.IN.INReplenishmentItem.DemandCalculation : Edm.String "Demand Calculation"
PX.Objects.IN.INReplenishmentItem.VendorClassID : Edm.String "Vendor Class"
PX.Objects.IN.INReplenishmentItem.PurchaseERQ : Edm.Decimal "Purchase ERQ"
PX.Objects.IN.INReplenishmentItem.InclQtySOBackOrdered : Edm.Boolean "Deduct Qty. on Back Orders"
PX.Objects.IN.INReplenishmentItem.InclQtySOPrepared : Edm.Boolean "Deduct Qty. on Sales Prepared"
PX.Objects.IN.INReplenishmentItem.InclQtySOBooked : Edm.Boolean "Deduct Qty. on Customer Orders"
PX.Objects.IN.INReplenishmentItem.InclQtySOShipped : Edm.Boolean "Deduct Qty. Shipped"
PX.Objects.IN.INReplenishmentItem.InclQtySOShipping : Edm.Boolean "Deduct Qty. Shipping"
PX.Objects.IN.INReplenishmentItem.InclQtyINIssues : Edm.Boolean "Deduct Qty. on Issues"
PX.Objects.IN.INReplenishmentItem.InclQtyINAssemblyDemand : Edm.Boolean "Deduct Qty. of Kit Assembly Demand"
PX.Objects.IN.INReplenishmentItem.InclQtyProductionSupplyPrepared : Edm.Boolean "Include Qty. of Production Supply Prepared"
PX.Objects.IN.INReplenishmentItem.InclQtyProductionSupply : Edm.Boolean "Include Qty. of Production Supply"
PX.Objects.IN.INReplenishmentItem.InclQtyProductionDemandPrepared : Edm.Boolean "Deduct Qty. on Production Demand Prepared"
PX.Objects.IN.INReplenishmentItem.InclQtyProductionDemand : Edm.Boolean "Deduct Qty. on Production Demand"
PX.Objects.IN.INReplenishmentItem.InclQtyProductionAllocated : Edm.Boolean "Deduct Qty. on Production Allocated"
PX.Objects.IN.INReplenishmentItem.QtyProcess : Edm.Decimal "Qty. To Process"
PX.Objects.IN.INReplenishmentItem.QtyProcessRounded : Edm.Boolean
PX.Objects.IN.INReplenishmentItem.DecimalBaseUnit : Edm.Boolean
PX.Objects.IN.INReplenishmentItem.QtyOnHand : Edm.Decimal "Qty. on Hand"
PX.Objects.IN.INReplenishmentItem.QtyFixedSOPODiff : Edm.Decimal
PX.Objects.IN.INReplenishmentItem.QtyFixedMLPODiff : Edm.Decimal
PX.Objects.IN.INReplenishmentItem.QtyNotAvail : Edm.Decimal "Qty. Not Available"
PX.Objects.IN.INReplenishmentItem.QtyPOPrepared : Edm.Decimal "Qty. PO Prepared"
PX.Objects.IN.INReplenishmentItem.QtyPOOrders : Edm.Decimal "Qty. PO Orders"
PX.Objects.IN.INReplenishmentItem.QtyPOReceipts : Edm.Decimal "Qty. PO Receipts"
PX.Objects.IN.INReplenishmentItem.QtyInTransit : Edm.Decimal "Qty. IN Transit"
PX.Objects.IN.INReplenishmentItem.QtyINReceipts : Edm.Decimal "Qty. IN Receipts"
PX.Objects.IN.INReplenishmentItem.QtyINAssemblySupply : Edm.Decimal "Qty. IN Assembly Supply"
PX.Objects.IN.INReplenishmentItem.QtyInTransitToProduction : Edm.Decimal "Qty In Transit to Production"
PX.Objects.IN.INReplenishmentItem.QtyProductionSupplyPrepared : Edm.Decimal "Qty Production Supply Prepared"
PX.Objects.IN.INReplenishmentItem.QtyProductionSupply : Edm.Decimal "Qty on Production Supply"
PX.Objects.IN.INReplenishmentItem.QtyPOFixedProductionPrepared : Edm.Decimal "Qty on Purchase for Prod. Prepared"
PX.Objects.IN.INReplenishmentItem.QtyPOFixedProductionOrders : Edm.Decimal "Qty on Purchase for Production"
PX.Objects.IN.INReplenishmentItem.QtySOBackOrdered : Edm.Decimal "Qty. SO Back Ordered"
PX.Objects.IN.INReplenishmentItem.QtySOPrepared : Edm.Decimal "Qty. SO Prepared"
PX.Objects.IN.INReplenishmentItem.QtySOBooked : Edm.Decimal "Qty. SO Booked"
PX.Objects.IN.INReplenishmentItem.QtySOShipped : Edm.Decimal "Qty. SO Shipped"
PX.Objects.IN.INReplenishmentItem.QtySOShipping : Edm.Decimal "Qty. SO Allocated"
PX.Objects.IN.INReplenishmentItem.QtyINIssues : Edm.Decimal "Qty. IN Issues"
PX.Objects.IN.INReplenishmentItem.QtyINAssemblyDemand : Edm.Decimal "Qty. IN Assembly Demand"
PX.Objects.IN.INReplenishmentItem.QtyProductionDemandPrepared : Edm.Decimal "Qty on Production Demand Prepared"
PX.Objects.IN.INReplenishmentItem.QtyProductionDemand : Edm.Decimal "Qty on Production Demand"
PX.Objects.IN.INReplenishmentItem.QtyProductionAllocated : Edm.Decimal "Qty on Production Allocated"
PX.Objects.IN.INReplenishmentItem.QtySOFixedProduction : Edm.Decimal "Qty on SO to Production"
PX.Objects.IN.INReplenishmentItem.QtyProdFixedPurchase : Edm.Decimal "Qty on Production to Purchase"
PX.Objects.IN.INReplenishmentItem.QtyProdFixedProduction : Edm.Decimal "Qty on Production to Production"
PX.Objects.IN.INReplenishmentItem.QtyProdFixedProdOrdersPrepared : Edm.Decimal "Qty on Production for Prod. Prepared"
PX.Objects.IN.INReplenishmentItem.QtyProdFixedProdOrders : Edm.Decimal "Qty on Production for Production"
PX.Objects.IN.INReplenishmentItem.QtyProdFixedSalesOrdersPrepared : Edm.Decimal "Qty on Production for SO Prepared"
PX.Objects.IN.INReplenishmentItem.QtyProdFixedSalesOrders : Edm.Decimal "Qty on Production for SO"
PX.Objects.IN.INReplenishmentItem.QtyINReplaned : Edm.Decimal "Replenishment Qty."
PX.Objects.IN.INReplenishmentItem.QtyReplenishment : Edm.Decimal "Qty. on Supply"
PX.Objects.IN.INReplenishmentItem.QtyHardDemand : Edm.Decimal "Qty. on Hard Demand"
PX.Objects.IN.INReplenishmentItem.QtyDemand : Edm.Decimal "Qty. on Demand"
PX.Objects.IN.INReplenishmentItem.QtyProcessInt : Edm.Decimal
PX.Objects.IN.INReplenishmentItem.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.INReplenishmentItem.VendorClassByVendorClassID -> PX.Objects.AP.VendorClass (VendorClassID=VendorClassID)

# PX.Objects.IN.INReplenishmentLine (EntityType)

Label: "Replenishment Line"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_IN_INReplenishmentLine, ReplenishmentLine, INReplenishmentLine

PX.Objects.IN.INReplenishmentLine.RefNbr : Edm.String [key]
PX.Objects.IN.INReplenishmentLine.LineNbr : Edm.Int32 [key]
PX.Objects.IN.INReplenishmentLine.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.IN.INReplenishmentLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INReplenishmentLine.UOM : Edm.String "UOM"
PX.Objects.IN.INReplenishmentLine.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.IN.INReplenishmentLine.BaseQty : Edm.Decimal [required]
PX.Objects.IN.INReplenishmentLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.IN.INReplenishmentLine.VendorLocationID : Edm.Int32
PX.Objects.IN.INReplenishmentLine.PlanID : Edm.Int64
PX.Objects.IN.INReplenishmentLine.POType : Edm.String "PO  Type"
PX.Objects.IN.INReplenishmentLine.PONbr : Edm.String "PO  Nbr."
PX.Objects.IN.INReplenishmentLine.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.IN.INReplenishmentLine.SOType : Edm.String "SO Type"
PX.Objects.IN.INReplenishmentLine.SONbr : Edm.String "SO Nbr."
PX.Objects.IN.INReplenishmentLine.SOLineNbr : Edm.Int32 "SO Line Nbr."
PX.Objects.IN.INReplenishmentLine.SOSplitLineNbr : Edm.Int32 "SO Split Nbr."
PX.Objects.IN.INReplenishmentLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INReplenishmentLine.CreatedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INReplenishmentLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INReplenishmentLine.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INReplenishmentLine.tstamp : Edm.Binary
PX.Objects.IN.INReplenishmentLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.IN.INReplenishmentLine.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.IN.INReplenishmentLine.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.IN.INReplenishmentLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.IN.INReplenishmentLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INReplenishmentLine.SOOrderBySONbr -> PX.Objects.SO.SOOrder (SOType=OrderType, SONbr=OrderNbr)
PX.Objects.IN.INReplenishmentLine.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.IN.INReplenishmentLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INReplenishmentLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INReplenishmentLine.SOLineBySOLineNbr -> PX.Objects.SO.SOLine (SOType=OrderType, SONbr=OrderNbr, SOLineNbr=LineNbr)
PX.Objects.IN.INReplenishmentLine.SOLineSplitBySOSplitLineNbr -> PX.Objects.SO.SOLineSplit (SOType=OrderType, SONbr=OrderNbr, SOLineNbr=LineNbr, SOSplitLineNbr=SplitLineNbr)
PX.Objects.IN.INReplenishmentLine.SOOrderTypeBySOType -> PX.Objects.SO.SOOrderType (SOType=OrderType)
PX.Objects.IN.INReplenishmentLine.INReplenishmentOrderByRefNbr -> PX.Objects.IN.INReplenishmentOrder (RefNbr=RefNbr)
PX.Objects.IN.INReplenishmentLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INReplenishmentLine.INSiteByDestinationSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INReplenishmentLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INReplenishmentLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.IN.INReplenishmentLine.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID, VendorLocationID=LocationID)

# PX.Objects.IN.INReplenishmentOrder (EntityType)

Label: "Replenishment Order"
Key: RefNbr
Entity sets: PX_Objects_IN_INReplenishmentOrder, ReplenishmentOrder, INReplenishmentOrder
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INReplenishmentOrder.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.IN.INReplenishmentOrder.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.IN.INReplenishmentOrder.LineCntr : Edm.Int32 [required]
PX.Objects.IN.INReplenishmentOrder.VendorID : Edm.Int32 "Vendor"
PX.Objects.IN.INReplenishmentOrder.NoteID : Edm.Guid
PX.Objects.IN.INReplenishmentOrder.NoteText : Edm.String "Note Text"
PX.Objects.IN.INReplenishmentOrder.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INReplenishmentOrder.CreatedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentOrder.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INReplenishmentOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INReplenishmentOrder.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentOrder.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INReplenishmentOrder.tstamp : Edm.Binary
PX.Objects.IN.INReplenishmentOrder.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.IN.INReplenishmentOrder.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.IN.INReplenishmentOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INReplenishmentOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INReplenishmentOrder.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INReplenishmentOrder.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)

# PX.Objects.IN.INReplenishmentPolicy (EntityType)

Label: "Replenishment Policy"
Key: ReplenishmentPolicyID
Entity sets: PX_Objects_IN_INReplenishmentPolicy, ReplenishmentPolicy, INReplenishmentPolicy
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INReplenishmentPolicy.ReplenishmentPolicyID : Edm.String [key] "Seasonality ID"
PX.Objects.IN.INReplenishmentPolicy.Descr : Edm.String "Description"
PX.Objects.IN.INReplenishmentPolicy.CalendarID : Edm.String "Calendar"
PX.Objects.IN.INReplenishmentPolicy.NoteID : Edm.Guid
PX.Objects.IN.INReplenishmentPolicy.NoteText : Edm.String "Note Text"
PX.Objects.IN.INReplenishmentPolicy.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INReplenishmentPolicy.CreatedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentPolicy.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INReplenishmentPolicy.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INReplenishmentPolicy.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentPolicy.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INReplenishmentPolicy.tstamp : Edm.Binary
PX.Objects.IN.INReplenishmentPolicy.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INReplenishmentPolicy.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INReplenishmentPolicy.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.IN.INReplenishmentPolicy.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INReplenishmentPolicy.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.IN.INReplenishmentPolicy.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.IN.INReplenishmentPolicy.INReplenishmentSeasonCollection -> Collection(PX.Objects.IN.INReplenishmentSeason)

# PX.Objects.IN.INReplenishmentSeason (EntityType)

Label: "Replenishment Seasonality"
Key: ReplenishmentPolicyID, SeasonID
Entity sets: PX_Objects_IN_INReplenishmentSeason, ReplenishmentSeasonality, INReplenishmentSeason

PX.Objects.IN.INReplenishmentSeason.ReplenishmentPolicyID : Edm.String [key] "Replenishment Policy ID"
PX.Objects.IN.INReplenishmentSeason.SeasonID : Edm.Int32 [key]
PX.Objects.IN.INReplenishmentSeason.Active : Edm.Boolean [required] "Active"
PX.Objects.IN.INReplenishmentSeason.StartDate : Edm.DateTimeOffset "Season Start Date"
PX.Objects.IN.INReplenishmentSeason.EndDate : Edm.DateTimeOffset "Season End Date"
PX.Objects.IN.INReplenishmentSeason.Factor : Edm.Decimal [required] "Factor"
PX.Objects.IN.INReplenishmentSeason.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INReplenishmentSeason.CreatedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentSeason.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INReplenishmentSeason.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INReplenishmentSeason.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INReplenishmentSeason.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INReplenishmentSeason.tstamp : Edm.Binary
PX.Objects.IN.INReplenishmentSeason.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INReplenishmentSeason.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INReplenishmentSeason.INReplenishmentPolicyByReplenishmentPolicyID -> PX.Objects.IN.INReplenishmentPolicy (ReplenishmentPolicyID=ReplenishmentPolicyID)

# PX.Objects.IN.INScanSetup (EntityType)

Label: "IN Scan Setup"
Key: BranchID
Entity sets: PX_Objects_IN_INScanSetup, INScanSetup

PX.Objects.IN.INScanSetup.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.IN.INScanSetup.ExplicitLineConfirmation : Edm.Boolean "Use Explicit Line Confirmation"
PX.Objects.IN.INScanSetup.QtyEnterModeInReceipt : Edm.String "Quantity Input Mode in Receipts"
PX.Objects.IN.INScanSetup.QtyEnterModeInIssue : Edm.String "Quantity Input Mode in Issues"
PX.Objects.IN.INScanSetup.QtyEnterModeInTransfer : Edm.String "Quantity Input Mode in Transfers"
PX.Objects.IN.INScanSetup.QtyEnterModeInCount : Edm.String "Quantity Input Mode in PI Counts"
PX.Objects.IN.INScanSetup.UseDefaultReasonCodeInReceipt : Edm.Boolean "Use Default Reason Code in Receipts"
PX.Objects.IN.INScanSetup.UseDefaultReasonCodeInIssue : Edm.Boolean "Use Default Reason Code in Issues"
PX.Objects.IN.INScanSetup.UseDefaultReasonCodeInTransfer : Edm.Boolean "Use Default Reason Code in Transfers"
PX.Objects.IN.INScanSetup.UseDefaultLotSerialNbrInTransfer : Edm.Boolean [required] "Use Default Lot/Serial Nbr. in Transfers"
PX.Objects.IN.INScanSetup.UseDefaultAutoGeneratedLotSerialNbrInReceipt : Edm.Boolean [required] "Use Default Auto-Generated Lot/Serial Nbr. in Receipts"
PX.Objects.IN.INScanSetup.RequestLocationForEachItemInReceipt : Edm.Boolean "Request Location for Each Item in Receipts"
PX.Objects.IN.INScanSetup.RequestLocationForEachItemInIssue : Edm.Boolean "Request Location for Each Item in Issues"
PX.Objects.IN.INScanSetup.RequestLocationForEachItemInTransfer : Edm.Boolean "Request Location for Each Item in Transfers"
PX.Objects.IN.INScanSetup.DefaultWarehouse : Edm.Boolean [required] "Use Warehouse from User Profile"
PX.Objects.IN.INScanSetup.tstamp : Edm.Binary
PX.Objects.IN.INScanSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INScanSetup.CreatedByScreenID : Edm.String
PX.Objects.IN.INScanSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INScanSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INScanSetup.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INScanSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INScanSetup.SiteMapByInventoryLabelsReportID -> PX.SM.SiteMap
PX.Objects.IN.INScanSetup.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.IN.INScanSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INScanSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.IN.INScanUserSetup (EntityType)

Label: "IN Scan User Setup"
Key: Mode, UserID
Entity sets: PX_Objects_IN_INScanUserSetup, INScanUserSetup

PX.Objects.IN.INScanUserSetup.UserID : Edm.Guid [key] "User"
PX.Objects.IN.INScanUserSetup.IsOverridden : Edm.Boolean [required] "Is Overridden"
PX.Objects.IN.INScanUserSetup.Mode : Edm.String [key] "Mode"
PX.Objects.IN.INScanUserSetup.DefaultWarehouse : Edm.Boolean [required] "Default Warehouse from User Profile"
PX.Objects.IN.INScanUserSetup.UseDefaultLotSerialNbr : Edm.Boolean [required] "Use Default Lot/Serial Nbr."
PX.Objects.IN.INScanUserSetup.tstamp : Edm.Binary
PX.Objects.IN.INScanUserSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INScanUserSetup.CreatedByScreenID : Edm.String
PX.Objects.IN.INScanUserSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INScanUserSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INScanUserSetup.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INScanUserSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INScanUserSetup.SiteMapByInventoryLabelsReportID -> PX.SM.SiteMap
PX.Objects.IN.INScanUserSetup.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.IN.INScanUserSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INScanUserSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INScanUserSetup.SMScaleByScaleDeviceID -> PX.SM.SMScale

# PX.Objects.IN.INSetup (EntityType)

Label: "IN Setup"
Singletons: PX_Objects_IN_INSetup, INSetup

PX.Objects.IN.INSetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.IN.INSetup.IssueNumberingID : Edm.String "Issue Numbering Sequence"
PX.Objects.IN.INSetup.ReceiptNumberingID : Edm.String "Receipt/Transfer Numbering Sequence"
PX.Objects.IN.INSetup.AdjustmentNumberingID : Edm.String "Adjustment Numbering Sequence"
PX.Objects.IN.INSetup.ReplenishmentNumberingID : Edm.String "Replenishment Numbering Sequence"
PX.Objects.IN.INSetup.tstamp : Edm.Binary
PX.Objects.IN.INSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INSetup.CreatedByScreenID : Edm.String
PX.Objects.IN.INSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INSetup.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSetup.HoldEntry : Edm.Boolean [required] "Hold Documents on Entry"
PX.Objects.IN.INSetup.RequireControlTotal : Edm.Boolean [required] "Validate Document Totals on Entry"
PX.Objects.IN.INSetup.UseInventorySubItem : Edm.Boolean "UseInventorySubItem"
PX.Objects.IN.INSetup.AutoAddLineBarcode : Edm.Boolean [required] "Automatically Add Receipt Line for Barcode"
PX.Objects.IN.INSetup.ShowBarcodesInOrderLines : Edm.Boolean [required] "Display Barcodes in Order Lines"
PX.Objects.IN.INSetup.AddByOneBarcode : Edm.Boolean [required] "Add One Unit per Barcode"
PX.Objects.IN.INSetup.IssuesReasonCode : Edm.String "Issue/Return Reason Code"
PX.Objects.IN.INSetup.ReceiptReasonCode : Edm.String "Receipt Reason Code"
PX.Objects.IN.INSetup.AdjustmentReasonCode : Edm.String "Adjustment Reason Code"
PX.Objects.IN.INSetup.AssemblyDisassemblyReasonCode : Edm.String "Assembly/Disassembly Reason Code"
PX.Objects.IN.INSetup.TransferReasonCode : Edm.String "Transfer Reason Code"
PX.Objects.IN.INSetup.DfltStkItemClassID : Edm.Int32 "Default Stock Item Class"
PX.Objects.IN.INSetup.DfltNonStkItemClassID : Edm.Int32 "Default Non-Stock Item Class"
PX.Objects.IN.INSetup.DfltPostClassID : Edm.String
PX.Objects.IN.INSetup.DfltLotSerClassID : Edm.String
PX.Objects.IN.INSetup.UpdateGL : Edm.Boolean [required] "Update GL"
PX.Objects.IN.INSetup.SummPost : Edm.Boolean [required] "Post Summary on Updating GL"
PX.Objects.IN.INSetup.AutoPost : Edm.Boolean [required] "Automatically Post on Release"
PX.Objects.IN.INSetup.PerRetainTran : Edm.Int16 "Keep Transactions for"
PX.Objects.IN.INSetup.PerRetainHist : Edm.Int16 "Periods to Retain History"
PX.Objects.IN.INSetup.NegQty : Edm.Boolean [required] "Allow Negative Quantity"
PX.Objects.IN.INSetup.PINumberingID : Edm.String "PI Numbering Sequence"
PX.Objects.IN.INSetup.PIUseTags : Edm.Boolean [required] "Use Tags"
PX.Objects.IN.INSetup.PILastTagNumber : Edm.Int32 [required] "Last Tag Number"
PX.Objects.IN.INSetup.PIReasonCode : Edm.String "Phys.Inventory Reason Code"
PX.Objects.IN.INSetup.KitAssemblyNumberingID : Edm.String "Kit Assembly Numbering Sequence"
PX.Objects.IN.INSetup.TurnoverPeriodsPerYear : Edm.Int16 [required] "Turnover Periods per Year"
PX.Objects.IN.INSetup.ServiceItemNumberingID : Edm.String "Equipment Numbering Sequence"
PX.Objects.IN.INSetup.ModelAttribute : Edm.String "Model Attribute"
PX.Objects.IN.INSetup.ManufactureAttribute : Edm.String "Manufacture Attribute"
PX.Objects.IN.INSetup.ReplanBackOrders : Edm.Boolean [required] "Replan Back Orders"
PX.Objects.IN.INSetup.TransitSiteID : Edm.Int32 "Site used for keep transit items"
PX.Objects.IN.INSetup.AutoReleasePIAdjustment : Edm.Boolean [required] "Release PI Adjustment Automatically"
PX.Objects.IN.INSetup.AllocateDocumentsOnHold : Edm.Boolean [required] "Allocate Items in Documents on Hold"
PX.Objects.IN.INSetup.IncludeSaleInTurnover : Edm.Boolean "Include Sales"
PX.Objects.IN.INSetup.IncludeProductionInTurnover : Edm.Boolean [required] "Include Production Orders"
PX.Objects.IN.INSetup.IncludeAssemblyInTurnover : Edm.Boolean [required] "Include Assemblies"
PX.Objects.IN.INSetup.IncludeIssueInTurnover : Edm.Boolean [required] "Include Issues and Adjustments"
PX.Objects.IN.INSetup.IncludeTransferInTurnover : Edm.Boolean [required] "Include Transfers"
PX.Objects.IN.INSetup.LeaveOldCrossSellSuggestion : Edm.Boolean [required]
PX.Objects.IN.INSetup.IsLotSerialAttributesValid : Edm.Boolean [required]
PX.Objects.IN.INSetup.DeadStockAvgCostV1 : Edm.Boolean [required]
PX.Objects.IN.INSetup.BranchByTransitBranchID -> PX.Objects.GL.Branch
PX.Objects.IN.INSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INSetup.CSAttributeByModelAttribute -> PX.Objects.CS.CSAttribute (ModelAttribute=AttributeID)
PX.Objects.IN.INSetup.CSAttributeByManufactureAttribute -> PX.Objects.CS.CSAttribute (ManufactureAttribute=AttributeID)
PX.Objects.IN.INSetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.IN.INSetup.NumberingByIssueNumberingID -> PX.Objects.CS.Numbering (IssueNumberingID=NumberingID)
PX.Objects.IN.INSetup.NumberingByReceiptNumberingID -> PX.Objects.CS.Numbering (ReceiptNumberingID=NumberingID)
PX.Objects.IN.INSetup.NumberingByAdjustmentNumberingID -> PX.Objects.CS.Numbering (AdjustmentNumberingID=NumberingID)
PX.Objects.IN.INSetup.NumberingByReplenishmentNumberingID -> PX.Objects.CS.Numbering (ReplenishmentNumberingID=NumberingID)
PX.Objects.IN.INSetup.NumberingByPINumberingID -> PX.Objects.CS.Numbering (PINumberingID=NumberingID)
PX.Objects.IN.INSetup.NumberingByKitAssemblyNumberingID -> PX.Objects.CS.Numbering (KitAssemblyNumberingID=NumberingID)
PX.Objects.IN.INSetup.NumberingByServiceItemNumberingID -> PX.Objects.CS.Numbering (ServiceItemNumberingID=NumberingID)
PX.Objects.IN.INSetup.NumberingByTransferListNumberingID -> PX.Objects.CS.Numbering
PX.Objects.IN.INSetup.NumberingByManufacturingNumberingID -> PX.Objects.CS.Numbering
PX.Objects.IN.INSetup.ReasonCodeByIssuesReasonCode -> PX.Objects.CS.ReasonCode (IssuesReasonCode=ReasonCodeID)
PX.Objects.IN.INSetup.ReasonCodeByReceiptReasonCode -> PX.Objects.CS.ReasonCode (ReceiptReasonCode=ReasonCodeID)
PX.Objects.IN.INSetup.ReasonCodeByAdjustmentReasonCode -> PX.Objects.CS.ReasonCode (AdjustmentReasonCode=ReasonCodeID)
PX.Objects.IN.INSetup.ReasonCodeByAssemblyDisassemblyReasonCode -> PX.Objects.CS.ReasonCode (AssemblyDisassemblyReasonCode=ReasonCodeID)
PX.Objects.IN.INSetup.ReasonCodeByTransferReasonCode -> PX.Objects.CS.ReasonCode (TransferReasonCode=ReasonCodeID)
PX.Objects.IN.INSetup.ReasonCodeByPIReasonCode -> PX.Objects.CS.ReasonCode (PIReasonCode=ReasonCodeID)
PX.Objects.IN.INSetup.INItemClassByDfltStkItemClassID -> PX.Objects.IN.INItemClass (DfltStkItemClassID=ItemClassID)
PX.Objects.IN.INSetup.INItemClassByDfltNonStkItemClassID -> PX.Objects.IN.INItemClass (DfltNonStkItemClassID=ItemClassID)
PX.Objects.IN.INSetup.INLotSerClassByDfltLotSerClassID -> PX.Objects.IN.INLotSerClass (DfltLotSerClassID=LotSerClassID)
PX.Objects.IN.INSetup.INPostClassByDfltPostClassID -> PX.Objects.IN.INPostClass (DfltPostClassID=PostClassID)
PX.Objects.IN.INSetup.INSiteByTransitSiteID -> PX.Objects.IN.INSite (TransitSiteID=SiteID)
PX.Objects.IN.INSetup.INSiteByDefaultSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INSetup.AccountByARClearingAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSetup.AccountByINTransitAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSetup.AccountByINProgressAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSetup.SubByARClearingSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSetup.SubByINTransitSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSetup.SubByINProgressSubID -> PX.Objects.GL.Sub

# PX.Objects.IN.INSite (EntityType)

Label: "Warehouse"
Key: SiteCD
Entity sets: PX_Objects_IN_INSite, Warehouse, INSite
Non-filterable, non-selectable: ReceiptLocationIDOverride, ShipLocationIDOverride, NoteText, Included, DiscAcctID, DiscSubID, FreightAcctID, FreightSubID, MiscAcctID, MiscSubID, Secured

PX.Objects.IN.INSite.SiteID : Edm.Int32
PX.Objects.IN.INSite.SiteCD : Edm.String [key] "Warehouse ID"
PX.Objects.IN.INSite.Descr : Edm.String "Description"
PX.Objects.IN.INSite.ReceiptLocationIDOverride : Edm.Boolean
PX.Objects.IN.INSite.ShipLocationIDOverride : Edm.Boolean
PX.Objects.IN.INSite.LocationValid : Edm.String "Location Entry"
PX.Objects.IN.INSite.BAccountID : Edm.Int32
PX.Objects.IN.INSite.BaseCuryID : Edm.String "Base Currency ID"
PX.Objects.IN.INSite.AddressID : Edm.Int32
PX.Objects.IN.INSite.ContactID : Edm.Int32
PX.Objects.IN.INSite.BuildingID : Edm.Int32 "Building ID"
PX.Objects.IN.INSite.NoteID : Edm.Guid
PX.Objects.IN.INSite.NoteText : Edm.String "Note Text"
PX.Objects.IN.INSite.ReplenishmentClassID : Edm.String "Replenishment Class"
PX.Objects.IN.INSite.AvgDefaultCost : Edm.String "Average Default Cost"
PX.Objects.IN.INSite.FIFODefaultCost : Edm.String "FIFO Default Cost"
PX.Objects.IN.INSite.OverrideInvtAccSub : Edm.Boolean [required] "Override Inventory Account/Sub."
PX.Objects.IN.INSite.Active : Edm.Boolean [required] "Active"
PX.Objects.IN.INSite.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INSite.CreatedByScreenID : Edm.String
PX.Objects.IN.INSite.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.INSite.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INSite.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INSite.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INSite.tstamp : Edm.Binary
PX.Objects.IN.INSite.Included : Edm.Boolean "Included"
PX.Objects.IN.INSite.UseItemDefaultLocationForPicking : Edm.Boolean [required] "Use Item Default Location for Picking"
PX.Objects.IN.INSite.CarrierFacility : Edm.String "Carrier Facility"
PX.Objects.IN.INSite.DiscAcctID : Edm.Int32
PX.Objects.IN.INSite.DiscSubID : Edm.Int32
PX.Objects.IN.INSite.FreightAcctID : Edm.Int32
PX.Objects.IN.INSite.FreightSubID : Edm.Int32
PX.Objects.IN.INSite.MiscAcctID : Edm.Int32
PX.Objects.IN.INSite.MiscSubID : Edm.Int32
PX.Objects.IN.INSite.Secured : Edm.Boolean "Secured"
PX.Objects.IN.INSite.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.IN.INSite.AddressByAddressID -> PX.Objects.CR.Address (AddressID=AddressID)
PX.Objects.IN.INSite.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.IN.INSite.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INSite.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INSite.INLocationByReceiptLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INSite.INLocationByShipLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INSite.INLocationByReturnLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INSite.INLocationByDropShipLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INSite.INLocationBySiteID -> PX.Objects.IN.INLocation (SiteID=SiteID)
PX.Objects.IN.INSite.INReplenishmentClassByReplenishmentClassID -> PX.Objects.IN.INReplenishmentClass (ReplenishmentClassID=ReplenishmentClassID)
PX.Objects.IN.INSite.INSiteBuildingByBuildingID -> PX.Objects.IN.INSiteBuilding (BuildingID=BuildingID)
PX.Objects.IN.INSite.INSiteBuildingByBranchID -> PX.Objects.IN.INSiteBuilding (BuildingID=BuildingID)
PX.Objects.IN.INSite.AccountByInvtAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSite.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSite.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSite.AccountByStdCstRevAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSite.AccountByPPVAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSite.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSite.AccountByStdCstVarAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSite.AccountByLCVarianceAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INSite.SubByInvtSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SubByCOGSSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SubByStdCstRevSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SubByPPVSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SubByStdCstVarSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SubByLCVarianceSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SubByReasonCodeSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INSite.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.IN.INSite.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.IN.INSite.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.IN.INSite.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)
PX.Objects.IN.INSite.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.INSite.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.INSite.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.IN.INSite.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INSite.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INSite.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INSite.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.INSite.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.IN.INSite.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.IN.INSite.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.INSite.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.IN.INSite.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INSite.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.INSite.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INSite.AMMachSchdCollection -> Collection(PX.Objects.AM.AMMachSchd)
PX.Objects.IN.INSite.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.INSite.AMWCSchdCollection -> Collection(PX.Objects.AM.AMWCSchd)
PX.Objects.IN.INSite.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.INSite.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INSite.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.IN.INSite.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INSite.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.INSite.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INSite.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.IN.INSite.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.IN.INSite.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INSite.INSiteZoneCollection -> Collection(PX.Objects.IN.DAC.INSiteZone)
PX.Objects.IN.INSite.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.Objects.IN.INSite.AMWCSchdDetailCollection -> Collection(PX.Objects.AM.AMWCSchdDetail)
PX.Objects.IN.INSite.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.IN.INSite.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.IN.INSite.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.INSite.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.INSite.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.INSite.BCLocationsCollection -> Collection(PX.Commerce.Objects.BCLocations)
PX.Objects.IN.INSite.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.INSite.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INSite.SOOrchestrationPlanCollection -> Collection(PX.Objects.SO.SOOrchestrationPlan)
PX.Objects.IN.INSite.SOOrchestrationPlanLineCollection -> Collection(PX.Objects.SO.SOOrchestrationPlanLine)
PX.Objects.IN.INSite.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.IN.INSite.SOOrderSiteCollection -> Collection(PX.Objects.SO.SOOrderSite)
PX.Objects.IN.INSite.SOPickerCollection -> Collection(PX.Objects.SO.SOPicker)
PX.Objects.IN.INSite.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INSite.SOPickerToShipmentLinkCollection -> Collection(PX.Objects.SO.SOPickerToShipmentLink)
PX.Objects.IN.INSite.SOPickingWorksheetCollection -> Collection(PX.Objects.SO.SOPickingWorksheet)
PX.Objects.IN.INSite.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.INSite.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.INSite.SOPickListEntryToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOPickListEntryToCartSplitLink)
PX.Objects.IN.INSite.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INSite.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INSite.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.IN.INSite.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)
PX.Objects.IN.INSite.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.IN.INSite.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.IN.INSite.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.IN.INSite.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.IN.INSite.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INSite.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.IN.INSite.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.INSite.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.INSite.CarrierPluginCollection -> Collection(PX.Objects.CS.CarrierPlugin)
PX.Objects.IN.INSite.INCartCollection -> Collection(PX.Objects.IN.INCart)
PX.Objects.IN.INSite.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.INSite.INToteCollection -> Collection(PX.Objects.IN.INTote)
PX.Objects.IN.INSite.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.IN.INSite.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.Objects.IN.INSite.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.IN.INSite.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.IN.INSite.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.IN.INSite.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.IN.INSite.INPIClassCollection -> Collection(PX.Objects.IN.INPIClass)
PX.Objects.IN.INSite.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.INSite.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.Objects.IN.INSite.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.IN.INSite.INPIStatusLocCollection -> Collection(PX.Objects.IN.INPIStatusLoc)
PX.Objects.IN.INSite.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.INSite.INReplenishmentOrderCollection -> Collection(PX.Objects.IN.INReplenishmentOrder)
PX.Objects.IN.INSite.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.IN.INSite.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.INSite.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.IN.INSite.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.IN.INSite.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.IN.INSite.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.IN.INSite.INRegisterCartCollection -> Collection(PX.Objects.IN.DAC.INRegisterCart)
PX.Objects.IN.INSite.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.Objects.IN.INSite.INItemClassSiteCollection -> Collection(PX.Objects.IN.DAC.INItemClassSite)
PX.Objects.IN.INSite.INSitePlanningStrategyCollection -> Collection(PX.Objects.IN.DAC.INSitePlanningStrategy)
PX.Objects.IN.INSite.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.INSite.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.IN.INSite.INTransferListCollection -> Collection(PX.Objects.IN.DAC.INTransferList)
PX.Objects.IN.INSite.WarehouseReferenceCollection -> Collection(PX.Objects.IN.DAC.WarehouseReference)
PX.Objects.IN.INSite.LocationBranchSettingsCollection -> Collection(PX.Objects.CR.LocationBranchSettings)
PX.Objects.IN.INSite.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.IN.INSite.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.IN.INSite.DiscountSiteCollection -> Collection(PX.Objects.AR.DiscountSite)
PX.Objects.IN.INSite.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.IN.INSite.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.IN.INSite.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.IN.INSite.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.IN.INSite.AMBOMCurySettingsCollection -> Collection(PX.Objects.AM.AMBOMCurySettings)
PX.Objects.IN.INSite.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.INSite.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.INSite.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.INSite.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.IN.INSite.AMConfigurationOptionCurySettingsCollection -> Collection(PX.Objects.AM.AMConfigurationOptionCurySettings)
PX.Objects.IN.INSite.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.IN.INSite.AMDepartmentCollection -> Collection(PX.Objects.AM.AMDepartment)
PX.Objects.IN.INSite.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.IN.INSite.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.IN.INSite.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.INSite.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.IN.INSite.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.IN.INSite.AMMachSchdDetailCollection -> Collection(PX.Objects.AM.AMMachSchdDetail)
PX.Objects.IN.INSite.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.IN.INSite.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.IN.INSite.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.IN.INSite.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.Objects.IN.INSite.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.INSite.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.INSite.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.INSite.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.IN.INSite.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.IN.INSite.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.Objects.IN.INSite.AMSiteTransferCollection -> Collection(PX.Objects.AM.AMSiteTransfer)
PX.Objects.IN.INSite.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.IN.INSite.AMToolSchdDetailCollection -> Collection(PX.Objects.AM.AMToolSchdDetail)
PX.Objects.IN.INSite.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.INSite.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.INSite.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.IN.INSite.AMWCCollection -> Collection(PX.Objects.AM.AMWC)
PX.Objects.IN.INSite.AMWCSubstituteCollection -> Collection(PX.Objects.AM.AMWCSubstitute)
PX.Objects.IN.INSite.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.INSite.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INSite.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.IN.INSite.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INSite.SPInventoryCartItemCollection -> Collection(PX.Objects.Portals.SP.DAC.SPInventoryCartItem)
PX.Objects.IN.INSite.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.IN.INSite.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.INSite.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.IN.INSite.SVStagingWarehouseCollection -> Collection(PX.Objects.SV.SVStagingWarehouse)
PX.Objects.IN.INSite.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.IN.INSite.BlanketSOOrderSiteCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOOrderSite)
PX.Objects.IN.INSite.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.IN.INSite.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INSite.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.IN.INSite.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.IN.INSite.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.IN.INSite.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.IN.INSite.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.IN.INSite.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.IN.INSite.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.IN.INSite.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.INSite.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.IN.INSite.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.INSite.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.IN.INSite.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.IN.INSite.VendorLocationCollection -> Collection(PX.Objects.PO.VendorLocation)
PX.Objects.IN.INSite.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.IN.INSite.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.INSite.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.INSite.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.IN.INSite.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.IN.INSite.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.IN.INSite.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.IN.INSite.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.INSite.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INSite.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.INSite.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.INSite.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.IN.INSite.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.INSite.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.INSite.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.IN.INSite.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.INSite.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.IN.INSite.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.IN.INSite.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.INSite.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.IN.INSite.SOShipmentPlanCollection -> Collection(PX.Objects.SO.SOShipmentPlan)
PX.Objects.IN.INSite.SOCartShipmentCollection -> Collection(PX.Objects.SO.SOCartShipment)
PX.Objects.IN.INSite.POCartReceiptCollection -> Collection(PX.Objects.PO.POCartReceipt)
PX.Objects.IN.INSite.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.IN.INSite.StoragePlaceCollection -> Collection(PX.Objects.IN.StoragePlace)

# PX.Objects.IN.INSiteBuilding (EntityType)

Label: "Warehouse Building"
Key: BuildingCD
Entity sets: PX_Objects_IN_INSiteBuilding, WarehouseBuilding, INSiteBuilding

PX.Objects.IN.INSiteBuilding.BuildingID : Edm.Int32
PX.Objects.IN.INSiteBuilding.BuildingCD : Edm.String [key] "Building ID"
PX.Objects.IN.INSiteBuilding.Descr : Edm.String "Description"
PX.Objects.IN.INSiteBuilding.AddressID : Edm.Int32
PX.Objects.IN.INSiteBuilding.tstamp : Edm.Binary
PX.Objects.IN.INSiteBuilding.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INSiteBuilding.CreatedByScreenID : Edm.String
PX.Objects.IN.INSiteBuilding.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSiteBuilding.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INSiteBuilding.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INSiteBuilding.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSiteBuilding.AddressByAddressID -> PX.Objects.CR.Address (AddressID=AddressID)
PX.Objects.IN.INSiteBuilding.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.IN.INSiteBuilding.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INSiteBuilding.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INSiteBuilding.INSiteCollection -> Collection(PX.Objects.IN.INSite)

# PX.Objects.IN.INSiteLotSerial (EntityType)

Label: "Lot/Serial by Warehouse"
Key: InventoryID, LotSerialNbr, SiteID
Entity sets: PX_Objects_IN_INSiteLotSerial, LotSerialbyWarehouse, INSiteLotSerial
Non-filterable, non-selectable: UpdateExpireDate

PX.Objects.IN.INSiteLotSerial.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INSiteLotSerial.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.IN.INSiteLotSerial.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INSiteLotSerial.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INSiteLotSerial.QtyNotAvail : Edm.Decimal [required] "Qty. Not Available"
PX.Objects.IN.INSiteLotSerial.QtyAvail : Edm.Decimal [required] "Qty. Available"
PX.Objects.IN.INSiteLotSerial.QtyHardAvail : Edm.Decimal [required] "Qty. Hard Available"
PX.Objects.IN.INSiteLotSerial.QtyActual : Edm.Decimal [required] "Qty. Available for Issue"
PX.Objects.IN.INSiteLotSerial.QtyInTransit : Edm.Decimal [required]
PX.Objects.IN.INSiteLotSerial.ExpireDate : Edm.DateTimeOffset "Expiry Date"
PX.Objects.IN.INSiteLotSerial.UpdateExpireDate : Edm.Boolean
PX.Objects.IN.INSiteLotSerial.LotSerTrack : Edm.String
PX.Objects.IN.INSiteLotSerial.LotSerAssign : Edm.String
PX.Objects.IN.INSiteLotSerial.tstamp : Edm.Binary
PX.Objects.IN.INSiteLotSerial.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INSiteLotSerial.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.INSiteLotSerial.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INSiteLotSerial.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.IN.INSiteStatus (EntityType)

Label: "IN Site Status"
Key: InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INSiteStatus, INSiteStatus
Non-filterable, non-selectable: QtyExpired

PX.Objects.IN.INSiteStatus.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INSiteStatus.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INSiteStatus.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INSiteStatus.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INSiteStatus.QtyNotAvail : Edm.Decimal [required] "Qty. Not Available"
PX.Objects.IN.INSiteStatus.QtyExpired : Edm.Decimal
PX.Objects.IN.INSiteStatus.QtyAvail : Edm.Decimal [required] "Qty. Available"
PX.Objects.IN.INSiteStatus.QtyHardAvail : Edm.Decimal [required] "Qty. Hard Available"
PX.Objects.IN.INSiteStatus.QtyActual : Edm.Decimal [required] "Qty. Available for Issue"
PX.Objects.IN.INSiteStatus.QtyInTransit : Edm.Decimal [required] "Qty. In-Transit"
PX.Objects.IN.INSiteStatus.QtyInTransitToSO : Edm.Decimal [required] "Qty. In Transit to SO"
PX.Objects.IN.INSiteStatus.QtyPOPrepared : Edm.Decimal [required] "Qty. PO Prepared"
PX.Objects.IN.INSiteStatus.QtyPOOrders : Edm.Decimal [required] "Qty. Purchase Orders"
PX.Objects.IN.INSiteStatus.QtyPOReceipts : Edm.Decimal [required] "Qty. Purchase Receipts"
PX.Objects.IN.INSiteStatus.QtySOBackOrdered : Edm.Decimal [required] "Qty. SO Backordered"
PX.Objects.IN.INSiteStatus.QtySOPrepared : Edm.Decimal [required] "Qty. SO Prepared"
PX.Objects.IN.INSiteStatus.QtySOBooked : Edm.Decimal [required] "Qty. SO Booked"
PX.Objects.IN.INSiteStatus.QtySOShipped : Edm.Decimal [required] "Qty. SO Shipped"
PX.Objects.IN.INSiteStatus.QtySOShipping : Edm.Decimal [required] "Qty. SO Shipping"
PX.Objects.IN.INSiteStatus.QtyMLPrepared : Edm.Decimal [required] "Qty. Material Prepared"
PX.Objects.IN.INSiteStatus.QtyMLBooked : Edm.Decimal [required] "Qty. Material Booked"
PX.Objects.IN.INSiteStatus.QtyMLDispatched : Edm.Decimal [required] "Qty. Material Dispatched"
PX.Objects.IN.INSiteStatus.QtyMLAllocated : Edm.Decimal [required] "Qty. Material Allocated"
PX.Objects.IN.INSiteStatus.QtyINIssues : Edm.Decimal [required] "Qty On Inventory Issues"
PX.Objects.IN.INSiteStatus.QtyINReceipts : Edm.Decimal [required] "Qty On Inventory Receipts"
PX.Objects.IN.INSiteStatus.QtyINAssemblyDemand : Edm.Decimal [required] "Qty Demanded by Kit Assembly"
PX.Objects.IN.INSiteStatus.QtyINAssemblySupply : Edm.Decimal [required] "Qty On Kit Assembly"
PX.Objects.IN.INSiteStatus.QtyInTransitToProduction : Edm.Decimal [required] "Qty In Transit to Production"
PX.Objects.IN.INSiteStatus.QtyProductionSupplyPrepared : Edm.Decimal [required] "Qty Production Supply Prepared"
PX.Objects.IN.INSiteStatus.QtyProductionSupply : Edm.Decimal [required] "Qty On Production Supply"
PX.Objects.IN.INSiteStatus.QtyPOFixedProductionPrepared : Edm.Decimal [required] "Qty On Purchase for Prod. Prepared"
PX.Objects.IN.INSiteStatus.QtyPOFixedProductionOrders : Edm.Decimal [required] "Qty On Purchase for Production"
PX.Objects.IN.INSiteStatus.QtyProductionDemandPrepared : Edm.Decimal [required] "Qty On Production Demand Prepared"
PX.Objects.IN.INSiteStatus.QtyProductionDemand : Edm.Decimal [required] "Qty On Production Demand"
PX.Objects.IN.INSiteStatus.QtyProductionAllocated : Edm.Decimal [required] "Qty On Production Allocated"
PX.Objects.IN.INSiteStatus.QtySOFixedProduction : Edm.Decimal [required] "Qty On SO to Production"
PX.Objects.IN.INSiteStatus.QtyProdFixedPurchase : Edm.Decimal [required] "Qty On Production to Purchase"
PX.Objects.IN.INSiteStatus.QtyProdFixedProduction : Edm.Decimal [required] "Qty On Production to Production"
PX.Objects.IN.INSiteStatus.QtyProdFixedProdOrdersPrepared : Edm.Decimal [required] "Qty On Production for Prod. Prepared"
PX.Objects.IN.INSiteStatus.QtyProdFixedProdOrders : Edm.Decimal [required] "Qty On Production for Production"
PX.Objects.IN.INSiteStatus.QtyProdFixedSalesOrdersPrepared : Edm.Decimal [required] "Qty On Production for SO Prepared"
PX.Objects.IN.INSiteStatus.QtyProdFixedSalesOrders : Edm.Decimal [required] "Qty On Production for SO Prepared"
PX.Objects.IN.INSiteStatus.QtyMLFixedProduction : Edm.Decimal "Material to Production"
PX.Objects.IN.INSiteStatus.QtyProdFixedMLPrepared : Edm.Decimal "Production for Material Prepared"
PX.Objects.IN.INSiteStatus.QtyProdFixedML : Edm.Decimal "Production for Material"
PX.Objects.IN.INSiteStatus.QtyINReplaned : Edm.Decimal [required] "Qty. Replanned"
PX.Objects.IN.INSiteStatus.QtyFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPOFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPOFixedFSSrvOrdPrepared : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPOFixedFSSrvOrdReceipts : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtySOFixed : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPOFixedOrders : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPOFixedPrepared : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPOFixedReceipts : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyMLToPurchase : Edm.Decimal [required] "Qty. Material to Purchase"
PX.Objects.IN.INSiteStatus.QtyPurchaseForML : Edm.Decimal [required] "Material Purchase"
PX.Objects.IN.INSiteStatus.QtyPurchaseForMLPrepared : Edm.Decimal [required] "Material Purchase Prepared"
PX.Objects.IN.INSiteStatus.QtyReceiptsForML : Edm.Decimal [required] "Material Receipts"
PX.Objects.IN.INSiteStatus.QtySODropShip : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPODropShipOrders : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPODropShipPrepared : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.QtyPODropShipReceipts : Edm.Decimal [required]
PX.Objects.IN.INSiteStatus.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INSiteStatus.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSiteStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INSiteStatus.INItemSiteBySiteID -> PX.Objects.IN.INItemSite (InventoryID=InventoryID, SiteID=SiteID)
PX.Objects.IN.INSiteStatus.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INSiteStatus.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INSiteStatus.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.INSiteStatus.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INSiteStatus.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.INSiteStatus.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INSiteStatus.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INSiteStatus.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INSiteStatus.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INSiteStatus.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.INSiteStatus.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.INSiteStatus.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INSiteStatus.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INSiteStatus.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INSiteStatus.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INSiteStatus.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)

# PX.Objects.IN.INSiteStatusByCostCenter (EntityType)

Label: "IN Site Status by Cost Center"
Key: CostCenterID, InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INSiteStatusByCostCenter, INSiteStatusbyCostCenter
Non-filterable, non-selectable: Active, QtyExpired

PX.Objects.IN.INSiteStatusByCostCenter.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INSiteStatusByCostCenter.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INSiteStatusByCostCenter.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INSiteStatusByCostCenter.CostCenterID : Edm.Int32 [key]
PX.Objects.IN.INSiteStatusByCostCenter.CostLayerType : Edm.String
PX.Objects.IN.INSiteStatusByCostCenter.Active : Edm.Boolean "Active"
PX.Objects.IN.INSiteStatusByCostCenter.QtyOnHand : Edm.Decimal [required] "Qty. On Hand"
PX.Objects.IN.INSiteStatusByCostCenter.QtyNotAvail : Edm.Decimal [required] "Qty. Not Available"
PX.Objects.IN.INSiteStatusByCostCenter.QtyExpired : Edm.Decimal
PX.Objects.IN.INSiteStatusByCostCenter.QtyAvail : Edm.Decimal [required] "Qty. Available"
PX.Objects.IN.INSiteStatusByCostCenter.QtyHardAvail : Edm.Decimal [required] "Qty. Available for Shipping"
PX.Objects.IN.INSiteStatusByCostCenter.QtyActual : Edm.Decimal [required] "Qty. Available for Issue"
PX.Objects.IN.INSiteStatusByCostCenter.QtyInTransit : Edm.Decimal [required] "Qty. In-Transit"
PX.Objects.IN.INSiteStatusByCostCenter.QtyInTransitToSO : Edm.Decimal [required] "Qty. In Transit to SO"
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOPrepared : Edm.Decimal [required] "Qty. PO Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOOrders : Edm.Decimal [required] "Qty. Purchase Orders"
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOReceipts : Edm.Decimal [required] "Qty. Purchase Receipts"
PX.Objects.IN.INSiteStatusByCostCenter.QtySOBackOrdered : Edm.Decimal [required] "Qty. SO Backordered"
PX.Objects.IN.INSiteStatusByCostCenter.QtySOPrepared : Edm.Decimal [required] "Qty. SO Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtySOBooked : Edm.Decimal [required] "Qty. SO Booked"
PX.Objects.IN.INSiteStatusByCostCenter.QtySOShipped : Edm.Decimal [required] "Qty. SO Shipped"
PX.Objects.IN.INSiteStatusByCostCenter.QtySOShipping : Edm.Decimal [required] "Qty. SO Shipping"
PX.Objects.IN.INSiteStatusByCostCenter.QtyMLPrepared : Edm.Decimal [required] "Qty. Material Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyMLBooked : Edm.Decimal [required] "Qty. Material Booked"
PX.Objects.IN.INSiteStatusByCostCenter.QtyMLDispatched : Edm.Decimal [required] "Qty. Material Dispatched"
PX.Objects.IN.INSiteStatusByCostCenter.QtyMLAllocated : Edm.Decimal [required] "Qty. Material Allocated"
PX.Objects.IN.INSiteStatusByCostCenter.QtyINIssues : Edm.Decimal [required] "Qty On Inventory Issues"
PX.Objects.IN.INSiteStatusByCostCenter.QtyINReceipts : Edm.Decimal [required] "Qty On Inventory Receipts"
PX.Objects.IN.INSiteStatusByCostCenter.QtyINAssemblyDemand : Edm.Decimal [required] "Qty Demanded by Kit Assembly"
PX.Objects.IN.INSiteStatusByCostCenter.QtyINAssemblySupply : Edm.Decimal [required] "Qty On Kit Assembly"
PX.Objects.IN.INSiteStatusByCostCenter.QtyInTransitToProduction : Edm.Decimal [required] "Qty In Transit to Production"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProductionSupplyPrepared : Edm.Decimal [required] "Qty Production Supply Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProductionSupply : Edm.Decimal [required] "Qty On Production Supply"
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOFixedProductionPrepared : Edm.Decimal [required] "Qty On Purchase for Prod. Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOFixedProductionOrders : Edm.Decimal [required] "Qty On Purchase for Production"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProductionDemandPrepared : Edm.Decimal [required] "Qty On Production Demand Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProductionDemand : Edm.Decimal [required] "Qty On Production Demand"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProductionAllocated : Edm.Decimal [required] "Qty On Production Allocated"
PX.Objects.IN.INSiteStatusByCostCenter.QtySOFixedProduction : Edm.Decimal [required] "Qty On SO to Production"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProdFixedPurchase : Edm.Decimal [required] "Qty On Production to Purchase"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProdFixedProduction : Edm.Decimal [required] "Qty On Production to Production"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProdFixedProdOrdersPrepared : Edm.Decimal [required] "Qty On Production for Prod. Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProdFixedProdOrders : Edm.Decimal [required] "Qty On Production for Production"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProdFixedSalesOrdersPrepared : Edm.Decimal [required] "Qty On Production for SO Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProdFixedSalesOrders : Edm.Decimal [required] "Qty On Production for SO Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyINReplaned : Edm.Decimal [required] "Qty. Replaned"
PX.Objects.IN.INSiteStatusByCostCenter.QtyFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOFixedFSSrvOrd : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOFixedFSSrvOrdPrepared : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOFixedFSSrvOrdReceipts : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtySOFixed : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOFixedOrders : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOFixedPrepared : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPOFixedReceipts : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyMLToPurchase : Edm.Decimal [required] "Qty. Material to Purchase"
PX.Objects.IN.INSiteStatusByCostCenter.QtyPurchaseForML : Edm.Decimal [required] "Material Purchase"
PX.Objects.IN.INSiteStatusByCostCenter.QtyPurchaseForMLPrepared : Edm.Decimal [required] "Material Purchase Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyReceiptsForML : Edm.Decimal [required] "Material Receipts"
PX.Objects.IN.INSiteStatusByCostCenter.QtyMLFixedProduction : Edm.Decimal [required] "Material to Production"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProdFixedMLPrepared : Edm.Decimal [required] "Production for Material Prepared"
PX.Objects.IN.INSiteStatusByCostCenter.QtyProdFixedML : Edm.Decimal [required] "Production for Material"
PX.Objects.IN.INSiteStatusByCostCenter.QtySODropShip : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPODropShipOrders : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPODropShipPrepared : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.QtyPODropShipReceipts : Edm.Decimal [required]
PX.Objects.IN.INSiteStatusByCostCenter.tstamp : Edm.Binary
PX.Objects.IN.INSiteStatusByCostCenter.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INSiteStatusByCostCenter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSiteStatusByCostCenter.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INSiteStatusByCostCenter.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.IN.INSiteStatusByCostCenter.INItemSiteBySiteID -> PX.Objects.IN.INItemSite (InventoryID=InventoryID, SiteID=SiteID)
PX.Objects.IN.INSiteStatusByCostCenter.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INSiteStatusByCostCenter.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INSiteStatusByCostCenter.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INSiteStatusByCostCenter.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INSiteStatusByCostCenter.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INSiteStatusByCostCenter.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)

# PX.Objects.IN.INSiteStatusByCostCenterShort (EntityType)

Label: "IN Site Status by Cost Center Short"
Key: CostCenterID, InventoryID, SiteID, SubItemID
Entity sets: PX_Objects_IN_INSiteStatusByCostCenterShort, INSiteStatusbyCostCenterShort

PX.Objects.IN.INSiteStatusByCostCenterShort.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INSiteStatusByCostCenterShort.SubItemID : Edm.Int32 [key]
PX.Objects.IN.INSiteStatusByCostCenterShort.SiteID : Edm.Int32 [key]
PX.Objects.IN.INSiteStatusByCostCenterShort.CostCenterID : Edm.Int32 [key]
PX.Objects.IN.INSiteStatusByCostCenterShort.QtyOnHand : Edm.Decimal
PX.Objects.IN.INSiteStatusByCostCenterShort.QtyNotAvail : Edm.Decimal
PX.Objects.IN.INSiteStatusByCostCenterShort.QtyAvail : Edm.Decimal
PX.Objects.IN.INSiteStatusByCostCenterShort.QtyHardAvail : Edm.Decimal
PX.Objects.IN.INSiteStatusByCostCenterShort.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INSiteStatusByCostCenterShort.INItemSiteBySiteID -> PX.Objects.IN.INItemSite (InventoryID=InventoryID, SiteID=SiteID)
PX.Objects.IN.INSiteStatusByCostCenterShort.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INSiteStatusByCostCenterShort.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INSiteStatusByCostCenterShort.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.IN.INSiteStatusByCostCenterShort.SalesAllocationCollection -> Collection(PX.Objects.SO.SalesAllocation)
PX.Objects.IN.INSiteStatusByCostCenterShort.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INSiteStatusByCostCenterShort.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INSiteStatusByCostCenterShort.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INSiteStatusByCostCenterShort.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)

# PX.Objects.IN.INSiteStatusQtyAggregated (EntityType)

Label: "Sum of Inventory Qtys by InventoryID with LastModifiedDateTime"
Key: InventoryID
Entity sets: PX_Objects_IN_INSiteStatusQtyAggregated, SumofInventoryQtysbyInventoryIDwithLastModifiedDateTime, INSiteStatusQtyAggregated

PX.Objects.IN.INSiteStatusQtyAggregated.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INSiteStatusQtyAggregated.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.IN.INSiteStatusQtyAggregated.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"

# PX.Objects.IN.INSiteStatusSelected (EntityType)

Key: InventoryID
Entity sets: PX_Objects_IN_INSiteStatusSelected
Non-filterable, non-selectable: QtySelected, Rank

PX.Objects.IN.INSiteStatusSelected.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INSiteStatusSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.IN.INSiteStatusSelected.Descr : Edm.String "Description"
PX.Objects.IN.INSiteStatusSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.IN.INSiteStatusSelected.ItemClassCD : Edm.String
PX.Objects.IN.INSiteStatusSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.IN.INSiteStatusSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.IN.INSiteStatusSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.IN.INSiteStatusSelected.BarCode : Edm.String
PX.Objects.IN.INSiteStatusSelected.SiteCD : Edm.String
PX.Objects.IN.INSiteStatusSelected.LocationCD : Edm.String
PX.Objects.IN.INSiteStatusSelected.SubItemCD : Edm.String
PX.Objects.IN.INSiteStatusSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.IN.INSiteStatusSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.IN.INSiteStatusSelected.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.IN.INSiteStatusSelected.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.IN.INSiteStatusSelected.NoteID : Edm.Guid
PX.Objects.IN.INSiteStatusSelected.CostCenterID : Edm.Int32
PX.Objects.IN.INSiteStatusSelected.CostCenterCD : Edm.String
PX.Objects.IN.INSiteStatusSelected.Rank : Edm.Int32
PX.Objects.IN.INSiteStatusSelected.CombinedSearchString : Edm.String
PX.Objects.IN.INSiteStatusSelected.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.IN.INSiteStatusSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.INSiteStatusSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.IN.INSiteStatusSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.IN.INSiteStatusSelected.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.IN.INSiteStatusSelected.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.IN.INSiteStatusSelected.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.IN.INSiteStatusSelected.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.IN.INSiteStatusSelected.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.IN.INSiteStatusSelected.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.IN.INSiteStatusSelected.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.IN.INSiteStatusSelected.FSAppointmentLogExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentLogExtItemLine)
PX.Objects.IN.INSiteStatusSelected.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.IN.INSiteStatusSelected.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.IN.INSiteStatusSelected.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.IN.INSiteStatusSelected.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.IN.INSiteStatusSelected.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.INSiteStatusSelected.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.INSiteStatusSelected.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.IN.INSiteStatusSelected.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.IN.INSiteStatusSelected.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.IN.INSiteStatusSelected.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.IN.INSiteStatusSelected.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.IN.INSiteStatusSelected.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.IN.INSiteStatusSelected.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INSiteStatusSelected.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INSiteStatusSelected.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INSiteStatusSelected.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.INSiteStatusSelected.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.IN.INSiteStatusSelected.INMatrixExcludedDataCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
PX.Objects.IN.INSiteStatusSelected.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.IN.INSiteStatusSelected.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.Objects.IN.INSiteStatusSelected.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.IN.INSiteStatusSelected.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.IN.INSiteStatusSelected.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.IN.INSiteStatusSelected.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.IN.INSiteStatusSelected.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.INSiteStatusSelected.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.IN.INSiteStatusSelected.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INSiteStatusSelected.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.INSiteStatusSelected.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INSiteStatusSelected.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.IN.INSiteStatusSelected.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.INSiteStatusSelected.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.INSiteStatusSelected.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INSiteStatusSelected.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.IN.INSiteStatusSelected.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.IN.INSiteStatusSelected.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.IN.INSiteStatusSelected.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INSiteStatusSelected.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.IN.INSiteStatusSelected.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.INSiteStatusSelected.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.IN.INSiteStatusSelected.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.IN.INSiteStatusSelected.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.IN.INSiteStatusSelected.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INSiteStatusSelected.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.IN.INSiteStatusSelected.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.IN.INSiteStatusSelected.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.IN.INSiteStatusSelected.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.IN.INSiteStatusSelected.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INSiteStatusSelected.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.IN.INSiteStatusSelected.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.IN.INSiteStatusSelected.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.IN.INSiteStatusSelected.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.Objects.IN.INSiteStatusSelected.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.IN.INSiteStatusSelected.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.IN.INSiteStatusSelected.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.IN.INSiteStatusSelected.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.IN.INSiteStatusSelected.InventoryPostingBatchDetailCollection -> Collection(PX.Objects.FS.InventoryPostingBatchDetail)
PX.Objects.IN.INSiteStatusSelected.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.IN.INSiteStatusSelected.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.INSiteStatusSelected.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.INSiteStatusSelected.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.INSiteStatusSelected.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.INSiteStatusSelected.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INSiteStatusSelected.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.IN.INSiteStatusSelected.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INSiteStatusSelected.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.INSiteStatusSelected.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.INSiteStatusSelected.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INSiteStatusSelected.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INSiteStatusSelected.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.IN.INSiteStatusSelected.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.IN.INSiteStatusSelected.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.Objects.IN.INSiteStatusSelected.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.IN.INSiteStatusSelected.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.IN.INSiteStatusSelected.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.IN.INSiteStatusSelected.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.IN.INSiteStatusSelected.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.IN.INSiteStatusSelected.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INSiteStatusSelected.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.IN.INSiteStatusSelected.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.IN.INSiteStatusSelected.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.IN.INSiteStatusSelected.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.IN.INSiteStatusSelected.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.IN.INSiteStatusSelected.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.IN.INSiteStatusSelected.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.IN.INSiteStatusSelected.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.IN.INSiteStatusSelected.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.Objects.IN.INSiteStatusSelected.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.INSiteStatusSelected.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.INSiteStatusSelected.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.IN.INSiteStatusSelected.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.IN.INSiteStatusSelected.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.IN.INSiteStatusSelected.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.INSiteStatusSelected.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)
PX.Objects.IN.INSiteStatusSelected.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.Objects.IN.INSiteStatusSelected.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.IN.INSiteStatusSelected.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.IN.INSiteStatusSelected.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.Objects.IN.INSiteStatusSelected.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.IN.INSiteStatusSelected.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.IN.INSiteStatusSelected.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.IN.INSiteStatusSelected.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.Objects.IN.INSiteStatusSelected.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.INSiteStatusSelected.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.IN.INSiteStatusSelected.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.INSiteStatusSelected.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.IN.INSiteStatusSelected.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.INSiteStatusSelected.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.IN.INSiteStatusSelected.InventoryItemLotSerNumValCollection -> Collection(PX.Objects.IN.InventoryItemLotSerNumVal)
PX.Objects.IN.INSiteStatusSelected.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.IN.INSiteStatusSelected.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.IN.INSiteStatusSelected.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.IN.INSiteStatusSelected.INRelatedInventoryUserFeedbackCollection -> Collection(PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback)
PX.Objects.IN.INSiteStatusSelected.INAttributeDescriptionGroupCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup)
PX.Objects.IN.INSiteStatusSelected.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.Objects.IN.INSiteStatusSelected.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.IN.INSiteStatusSelected.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.IN.INSiteStatusSelected.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.INSiteStatusSelected.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.IN.INSiteStatusSelected.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)
PX.Objects.IN.INSiteStatusSelected.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.Objects.IN.INSiteStatusSelected.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.IN.INSiteStatusSelected.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.IN.INSiteStatusSelected.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.IN.INSiteStatusSelected.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.Objects.IN.INSiteStatusSelected.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.IN.INSiteStatusSelected.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.IN.INSiteStatusSelected.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.IN.INSiteStatusSelected.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.IN.INSiteStatusSelected.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.IN.INSiteStatusSelected.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.IN.INSiteStatusSelected.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.Objects.IN.INSiteStatusSelected.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.Objects.IN.INSiteStatusSelected.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.IN.INSiteStatusSelected.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.IN.INSiteStatusSelected.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.IN.INSiteStatusSelected.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.IN.INSiteStatusSelected.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.IN.INSiteStatusSelected.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.IN.INSiteStatusSelected.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.IN.INSiteStatusSelected.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Objects.IN.INSiteStatusSelected.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.Objects.IN.INSiteStatusSelected.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.IN.INSiteStatusSelected.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.IN.INSiteStatusSelected.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.INSiteStatusSelected.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.INSiteStatusSelected.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.INSiteStatusSelected.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.IN.INSiteStatusSelected.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.IN.INSiteStatusSelected.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.IN.INSiteStatusSelected.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.IN.INSiteStatusSelected.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.IN.INSiteStatusSelected.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.IN.INSiteStatusSelected.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.INSiteStatusSelected.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.Objects.IN.INSiteStatusSelected.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.IN.INSiteStatusSelected.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.IN.INSiteStatusSelected.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.IN.INSiteStatusSelected.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.IN.INSiteStatusSelected.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.IN.INSiteStatusSelected.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.INSiteStatusSelected.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.INSiteStatusSelected.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.INSiteStatusSelected.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.IN.INSiteStatusSelected.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.IN.INSiteStatusSelected.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.IN.INSiteStatusSelected.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.INSiteStatusSelected.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.INSiteStatusSelected.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.INSiteStatusSelected.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.IN.INSiteStatusSelected.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INSiteStatusSelected.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.IN.INSiteStatusSelected.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.IN.INSiteStatusSelected.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.IN.INSiteStatusSelected.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.IN.INSiteStatusSelected.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.Objects.IN.INSiteStatusSelected.FSServiceInventoryItemCollection -> Collection(PX.Objects.FS.FSServiceInventoryItem)
PX.Objects.IN.INSiteStatusSelected.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)
PX.Objects.IN.INSiteStatusSelected.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)
PX.Objects.IN.INSiteStatusSelected.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.Objects.IN.INSiteStatusSelected.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)
PX.Objects.IN.INSiteStatusSelected.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INSiteStatusSelected.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.IN.INSiteStatusSelected.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.IN.INSiteStatusSelected.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.IN.INSiteStatusSelected.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.IN.INSiteStatusSelected.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.IN.INSiteStatusSelected.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.IN.INSiteStatusSelected.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.IN.INSiteStatusSelected.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.IN.INSiteStatusSelected.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.IN.INSiteStatusSelected.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.IN.INSiteStatusSelected.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.INSiteStatusSelected.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.IN.INSiteStatusSelected.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.IN.INSiteStatusSelected.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.IN.INSiteStatusSelected.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.IN.INSiteStatusSelected.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INSiteStatusSelected.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.IN.INSiteStatusSelected.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.IN.INSiteStatusSelected.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.IN.INSiteStatusSelected.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.IN.INSiteStatusSelected.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.IN.INSiteStatusSelected.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.IN.INSiteStatusSelected.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.IN.INSiteStatusSelected.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.IN.INSiteStatusSelected.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.IN.INSiteStatusSelected.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.IN.INSiteStatusSelected.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.IN.INSiteStatusSelected.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.IN.INSiteStatusSelected.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.INSiteStatusSelected.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.IN.INSiteStatusSelected.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.IN.INSiteStatusSelected.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.INSiteStatusSelected.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.IN.INSiteStatusSelected.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.IN.INSiteStatusSelected.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.IN.INSiteStatusSelected.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.IN.INSiteStatusSelected.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.IN.INSiteStatusSelected.POLineRCollection -> Collection(PX.Objects.PO.POLineR)
PX.Objects.IN.INSiteStatusSelected.PMItemRateCollection -> Collection(PX.Objects.PM.PMItemRate)
PX.Objects.IN.INSiteStatusSelected.PMProjectARTranPostDetailCollection -> Collection(PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail)
PX.Objects.IN.INSiteStatusSelected.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.INSiteStatusSelected.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.INSiteStatusSelected.INItemLotSerialCollection -> Collection(PX.Objects.IN.INItemLotSerial)
PX.Objects.IN.INSiteStatusSelected.INItemSalesHistCollection -> Collection(PX.Objects.IN.INItemSalesHist)
PX.Objects.IN.INSiteStatusSelected.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.IN.INSiteStatusSelected.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.IN.INSiteStatusSelected.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.IN.INSiteStatusSelected.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.IN.INSiteStatusSelected.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.INSiteStatusSelected.INSubItemSegmentValueCollection -> Collection(PX.Objects.IN.INSubItemSegmentValue)
PX.Objects.IN.INSiteStatusSelected.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INSiteStatusSelected.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.INSiteStatusSelected.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.INSiteStatusSelected.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.IN.INSiteStatusSelected.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.INSiteStatusSelected.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.INSiteStatusSelected.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.IN.INSiteStatusSelected.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.INSiteStatusSelected.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.IN.INSiteStatusSelected.RelatedItemCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItem)
PX.Objects.IN.INSiteStatusSelected.INItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeader)
PX.Objects.IN.INSiteStatusSelected.BCInventoryFileUrlsCollection -> Collection(PX.Commerce.Objects.BCInventoryFileUrls)
PX.Objects.IN.INSiteStatusSelected.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.IN.INSiteStatusSelected.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.INSiteStatusSelected.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.IN.INSiteStatusSelected.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.IN.INSiteStatusSelected.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.IN.INSiteStatusSelected.SchedulerEmployeeInventoryItemCollection -> Collection(PX.Objects.FS.SchedulerEmployeeInventoryItem)
PX.Objects.IN.INSiteStatusSelected.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)
PX.Objects.IN.INSiteStatusSelected.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.IN.INSiteStatusSelected.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.IN.INSiteStatusSelected.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.IN.INSiteStatusSelected.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)
PX.Objects.IN.INSiteStatusSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.IN.INSiteStatusSummary (EntityType)

Label: "IN Warehouse Status"
Key: InventoryID, SiteID
Entity sets: PX_Objects_IN_INSiteStatusSummary, INWarehouseStatus, INSiteStatusSummary

PX.Objects.IN.INSiteStatusSummary.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INSiteStatusSummary.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INSiteStatusSummary.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.IN.INSiteStatusSummary.QtyNotAvail : Edm.Decimal "Qty. Not Available"
PX.Objects.IN.INSiteStatusSummary.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.IN.INSiteStatusSummary.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INSiteStatusSummary.INItemSiteBySiteID -> PX.Objects.IN.INItemSite (InventoryID=InventoryID, SiteID=SiteID)
PX.Objects.IN.INSiteStatusSummary.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.IN.INSubItem (EntityType)

Label: "IN Sub Item"
Key: SubItemCD
Entity sets: PX_Objects_IN_INSubItem, INSubItem
Non-filterable, non-selectable: Secured

PX.Objects.IN.INSubItem.SubItemID : Edm.Int32 "Subitem ID"
PX.Objects.IN.INSubItem.SubItemCD : Edm.String [key] "Subitem ID"
PX.Objects.IN.INSubItem.Descr : Edm.String
PX.Objects.IN.INSubItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INSubItem.CreatedByScreenID : Edm.String
PX.Objects.IN.INSubItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSubItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INSubItem.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INSubItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSubItem.tstamp : Edm.Binary
PX.Objects.IN.INSubItem.Secured : Edm.Boolean "Secured"
PX.Objects.IN.INSubItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INSubItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INSubItem.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.IN.INSubItem.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.IN.INSubItem.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.INSubItem.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.INSubItem.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INSubItem.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INSubItem.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INSubItem.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.INSubItem.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.IN.INSubItem.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INSubItem.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.INSubItem.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INSubItem.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.INSubItem.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.INSubItem.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INSubItem.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.IN.INSubItem.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INSubItem.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.IN.INSubItem.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.INSubItem.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.IN.INSubItem.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INSubItem.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.IN.INSubItem.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.INSubItem.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.INSubItem.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.INSubItem.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.INSubItem.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INSubItem.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INSubItem.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.INSubItem.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.INSubItem.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INSubItem.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INSubItem.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.IN.INSubItem.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.IN.INSubItem.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.IN.INSubItem.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.IN.INSubItem.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INSubItem.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.IN.INSubItem.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.IN.INSubItem.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.INSubItem.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.INSubItem.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.INSubItem.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.IN.INSubItem.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.Objects.IN.INSubItem.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.IN.INSubItem.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.INSubItem.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.INSubItem.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.IN.INSubItem.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.INSubItem.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.IN.INSubItem.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.IN.INSubItem.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.IN.INSubItem.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.INSubItem.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.INSubItem.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.INSubItem.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.IN.INSubItem.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.IN.INSubItem.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.IN.INSubItem.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.IN.INSubItem.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.INSubItem.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.Objects.IN.INSubItem.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.IN.INSubItem.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.IN.INSubItem.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.IN.INSubItem.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.IN.INSubItem.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.INSubItem.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.INSubItem.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.INSubItem.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.IN.INSubItem.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.IN.INSubItem.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.INSubItem.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.INSubItem.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.INSubItem.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INSubItem.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.IN.INSubItem.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INSubItem.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.INSubItem.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INSubItem.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.IN.INSubItem.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.IN.INSubItem.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.IN.INSubItem.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.IN.INSubItem.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.INSubItem.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.IN.INSubItem.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.INSubItem.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.IN.INSubItem.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.IN.INSubItem.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.IN.INSubItem.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.INSubItem.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.INSubItem.INItemSalesHistCollection -> Collection(PX.Objects.IN.INItemSalesHist)
PX.Objects.IN.INSubItem.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.IN.INSubItem.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.IN.INSubItem.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.INSubItem.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INSubItem.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.INSubItem.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.INSubItem.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.INSubItem.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.INSubItem.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.INSubItem.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.IN.INSubItem.RelatedItemCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItem)
PX.Objects.IN.INSubItem.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.IN.INSubItem.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.INSubItem.INCostSubItemXRefCollection -> Collection(PX.Objects.IN.INCostSubItemXRef)

# PX.Objects.IN.INSubItemRep (EntityType)

Label: "Subitem Replenishment Settings"
Key: CuryID, InventoryID, ReplenishmentClassID, SubItemID
Entity sets: PX_Objects_IN_INSubItemRep, SubitemReplenishmentSettings, INSubItemRep

PX.Objects.IN.INSubItemRep.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INSubItemRep.CuryID : Edm.String [key] "Currency"
PX.Objects.IN.INSubItemRep.ReplenishmentClassID : Edm.String [key] "Replenishment Class ID"
PX.Objects.IN.INSubItemRep.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INSubItemRep.SafetyStock : Edm.Decimal [required] "Safety Stock"
PX.Objects.IN.INSubItemRep.MinQty : Edm.Decimal [required] "Reorder Point"
PX.Objects.IN.INSubItemRep.MaxQty : Edm.Decimal [required] "Max Qty."
PX.Objects.IN.INSubItemRep.TransferERQ : Edm.Decimal "Transfer ERQ"
PX.Objects.IN.INSubItemRep.ItemStatus : Edm.String "Status"
PX.Objects.IN.INSubItemRep.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INSubItemRep.CreatedByScreenID : Edm.String
PX.Objects.IN.INSubItemRep.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSubItemRep.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INSubItemRep.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INSubItemRep.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INSubItemRep.tstamp : Edm.Binary
PX.Objects.IN.INSubItemRep.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INSubItemRep.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INSubItemRep.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INSubItemRep.INItemRepByReplenishmentClassID -> PX.Objects.IN.INItemRep (InventoryID=InventoryID, CuryID=CuryID, ReplenishmentClassID=ReplenishmentClassID)
PX.Objects.IN.INSubItemRep.INReplenishmentClassByReplenishmentClassID -> PX.Objects.IN.INReplenishmentClass (ReplenishmentClassID=ReplenishmentClassID)
PX.Objects.IN.INSubItemRep.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.IN.INSubItemRep.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)

# PX.Objects.IN.INSubItemSegmentValue (EntityType)

Label: "IN Subitem Segment Value"
Key: InventoryID, SegmentID, Value
Entity sets: PX_Objects_IN_INSubItemSegmentValue, INSubitemSegmentValue

PX.Objects.IN.INSubItemSegmentValue.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INSubItemSegmentValue.SegmentID : Edm.Int16 [key] "Segment ID"
PX.Objects.IN.INSubItemSegmentValue.Value : Edm.String [key] "Value"
PX.Objects.IN.INSubItemSegmentValue.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)

# PX.Objects.IN.IntercompanyGoodsInTransitResult (EntityType)

Label: "Intercompany Goods in Transit Result"
Key: LineNbr, POReceiptNbr, POReceiptType, ShipmentNbr
Entity sets: PX_Objects_IN_IntercompanyGoodsInTransitResult, IntercompanyGoodsinTransitResult

PX.Objects.IN.IntercompanyGoodsInTransitResult.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.IN.IntercompanyGoodsInTransitResult.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.IN.IntercompanyGoodsInTransitResult.Operation : Edm.String "Operation"
PX.Objects.IN.IntercompanyGoodsInTransitResult.ShipmentType : Edm.String "Type"
PX.Objects.IN.IntercompanyGoodsInTransitResult.ShipDate : Edm.DateTimeOffset "Shipment Date"
PX.Objects.IN.IntercompanyGoodsInTransitResult.SellingBranchBAccountID : Edm.Int32
PX.Objects.IN.IntercompanyGoodsInTransitResult.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.IntercompanyGoodsInTransitResult.TranDesc : Edm.String "Description"
PX.Objects.IN.IntercompanyGoodsInTransitResult.UOM : Edm.String "UOM"
PX.Objects.IN.IntercompanyGoodsInTransitResult.ShippedQty : Edm.Decimal "In-Transit Qty."
PX.Objects.IN.IntercompanyGoodsInTransitResult.ExtCost : Edm.Decimal "Total Cost"
PX.Objects.IN.IntercompanyGoodsInTransitResult.DaysInTransit : Edm.Int32 "Days in Transit"
PX.Objects.IN.IntercompanyGoodsInTransitResult.DaysOverdue : Edm.Int32 "Days Overdue"
PX.Objects.IN.IntercompanyGoodsInTransitResult.PurchasingBranchBAccountID : Edm.Int32 "Purchasing Company"
PX.Objects.IN.IntercompanyGoodsInTransitResult.POReceiptType : Edm.String [key] "Receipt Type"
PX.Objects.IN.IntercompanyGoodsInTransitResult.POReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.IN.IntercompanyGoodsInTransitResult.StkItem : Edm.Boolean "Stock Item"
PX.Objects.IN.IntercompanyGoodsInTransitResult.ShipmentConfirmed : Edm.Boolean "Confirmed"
PX.Objects.IN.IntercompanyGoodsInTransitResult.ShipmentStatus : Edm.String "Shipment Status"
PX.Objects.IN.IntercompanyGoodsInTransitResult.ReceiptReleased : Edm.Boolean "Released"
PX.Objects.IN.IntercompanyGoodsInTransitResult.RequestDate : Edm.DateTimeOffset "Requested On"
PX.Objects.IN.IntercompanyGoodsInTransitResult.ReceiptDate : Edm.DateTimeOffset "Receipt Date"
PX.Objects.IN.IntercompanyGoodsInTransitResult.ExcludeFromIntercompanyProc : Edm.Boolean "Exclude from Intercompany Processing"
PX.Objects.IN.IntercompanyGoodsInTransitResult.NoteID : Edm.Guid
PX.Objects.IN.IntercompanyGoodsInTransitResult.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.IN.IntercompanyGoodsInTransitResult.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.IN.IntercompanyGoodsInTransitResult.SOShipmentByShipmentType -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr, ShipmentType=ShipmentType)
PX.Objects.IN.IntercompanyGoodsInTransitResult.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.IntercompanyGoodsInTransitResult.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.IN.IntercompanyGoodsInTransitResult.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)

# PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult (EntityType)

Label: "Intercompany Returned Goods in Transit Result"
Key: LineNbr, POReturnNbr
Entity sets: PX_Objects_IN_IntercompanyReturnedGoodsInTransitResult, IntercompanyReturnedGoodsinTransitResult

PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.POReturnNbr : Edm.String [key] "Return Nbr."
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.LineNbr : Edm.Int32 [key]
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.PurchasingBranchBAccountID : Edm.Int32
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.TranDesc : Edm.String "Description"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.UOM : Edm.String "UOM"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.ReturnedQty : Edm.Decimal "In-Transit Qty."
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.ExtCost : Edm.Decimal "Total Cost"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.ReturnDate : Edm.DateTimeOffset "Return Date"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.DaysInTransit : Edm.Int32 "Days in Transit"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SellingBranchBAccountID : Edm.Int32 "Selling Company"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SOType : Edm.String "SO Type"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SONbr : Edm.String "SO Nbr."
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SOLineNbr : Edm.Int32
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SOBehavior : Edm.String
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.StkItem : Edm.Boolean "Stock Item"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.ReturnReleased : Edm.Boolean "Released"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.ShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.ShipmentStatus : Edm.String "Shipment Status"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.ShipmentDate : Edm.DateTimeOffset "Shipment Date"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.ExcludeFromIntercompanyProc : Edm.Boolean "Exclude from Intercompany Processing"
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.OrigReceiptType : Edm.String
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.OrigReceiptNbr : Edm.String
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.NoteID : Edm.Guid
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SOOrderBySOType -> PX.Objects.SO.SOOrder (SONbr=OrderNbr, SOType=OrderType)
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.POReceiptByPOReturnNbr -> PX.Objects.PO.POReceipt (POReturnNbr=ReceiptNbr)
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.POReceiptByOrigReceiptNbr -> PX.Objects.PO.POReceipt (OrigReceiptType=ReceiptType, OrigReceiptNbr=ReceiptNbr)
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.POReceiptByOrigReceiptType -> PX.Objects.PO.POReceipt (OrigReceiptNbr=ReceiptNbr, OrigReceiptType=ReceiptType)
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SOShipmentByShipmentType -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)

# PX.Objects.IN.INTote (EntityType)

Label: "IN Tote"
Key: SiteID, ToteCD
Entity sets: PX_Objects_IN_INTote, INTote
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INTote.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.INTote.ToteID : Edm.Int32 "ToteID"
PX.Objects.IN.INTote.ToteCD : Edm.String [key] "Tote ID"
PX.Objects.IN.INTote.Descr : Edm.String "Description"
PX.Objects.IN.INTote.AssignedCartID : Edm.Int32 "Assigned Cart ID"
PX.Objects.IN.INTote.Active : Edm.Boolean [required] "Active"
PX.Objects.IN.INTote.NoteID : Edm.Guid
PX.Objects.IN.INTote.NoteText : Edm.String "Note Text"
PX.Objects.IN.INTote.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INTote.CreatedByScreenID : Edm.String
PX.Objects.IN.INTote.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTote.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INTote.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INTote.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTote.tstamp : Edm.Binary
PX.Objects.IN.INTote.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INTote.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INTote.INCartByAssignedCartID -> PX.Objects.IN.INCart (SiteID=SiteID, AssignedCartID=CartID)
PX.Objects.IN.INTote.INCartBySiteID -> PX.Objects.IN.INCart (AssignedCartID=CartID, SiteID=SiteID)
PX.Objects.IN.INTote.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.INTote.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INTote.SOPickerToShipmentLinkCollection -> Collection(PX.Objects.SO.SOPickerToShipmentLink)

# PX.Objects.IN.INTran (EntityType)

Label: "IN Transaction"
Key: DocType, LineNbr, RefNbr
Entity sets: PX_Objects_IN_INTran, INTransaction, INTran
Non-filterable, non-selectable: OverrideUnitCost, AvgCost, CostedQty, OrigTranCost, OrigTranAmt, ReceiptedBaseQty, INTransitBaseQty, ReceiptedQty, INTransitQty, NoteText, SalesMult

PX.Objects.IN.INTran.BranchID : Edm.Int32 "Branch"
PX.Objects.IN.INTran.DocType : Edm.String [key] "Document Type"
PX.Objects.IN.INTran.OrigModule : Edm.String "Source"
PX.Objects.IN.INTran.TranType : Edm.String "Tran. Type"
PX.Objects.IN.INTran.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.IN.INTran.LineNbr : Edm.Int32 [key] "Line Number"
PX.Objects.IN.INTran.SortOrder : Edm.Int32 "Line Order"
PX.Objects.IN.INTran.TranDate : Edm.DateTimeOffset
PX.Objects.IN.INTran.IsIntercompany : Edm.Boolean [required]
PX.Objects.IN.INTran.POLineType : Edm.String
PX.Objects.IN.INTran.InvtMult : Edm.Int16 "Multiplier"
PX.Objects.IN.INTran.IsStockItem : Edm.Boolean
PX.Objects.IN.INTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INTran.BAccountID : Edm.Int32
PX.Objects.IN.INTran.DestBranchID : Edm.Int32
PX.Objects.IN.INTran.SOOrderType : Edm.String "SO Order Type"
PX.Objects.IN.INTran.SOOrderNbr : Edm.String "SO Order Nbr."
PX.Objects.IN.INTran.SOOrderLineNbr : Edm.Int32
PX.Objects.IN.INTran.CostCenterID : Edm.Int32 [required]
PX.Objects.IN.INTran.OrigDocType : Edm.String
PX.Objects.IN.INTran.OrigTranType : Edm.String
PX.Objects.IN.INTran.OrigRefNbr : Edm.String "Receipt Nbr."
PX.Objects.IN.INTran.OrigLineNbr : Edm.Int32
PX.Objects.IN.INTran.OrigToLocationID : Edm.Int32
PX.Objects.IN.INTran.OrigIsLotSerial : Edm.Boolean
PX.Objects.IN.INTran.OrigNoteID : Edm.Guid
PX.Objects.IN.INTran.ReclassificationProhibited : Edm.Boolean [required]
PX.Objects.IN.INTran.ToSiteID : Edm.Int32 "To Site ID"
PX.Objects.IN.INTran.UOM : Edm.String "UOM"
PX.Objects.IN.INTran.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.IN.INTran.Released : Edm.Boolean [required] "Released"
PX.Objects.IN.INTran.ReleasedDateTime : Edm.DateTimeOffset "Release Date"
PX.Objects.IN.INTran.FinPeriodID : Edm.String
PX.Objects.IN.INTran.TranPeriodID : Edm.String
PX.Objects.IN.INTran.UnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.IN.INTran.TranAmt : Edm.Decimal [required] "Ext. Price"
PX.Objects.IN.INTran.ExactCost : Edm.Boolean [required]
PX.Objects.IN.INTran.ManualCost : Edm.Boolean [required] "Manual Cost"
PX.Objects.IN.INTran.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.IN.INTran.OverrideUnitCost : Edm.Boolean
PX.Objects.IN.INTran.AvgCost : Edm.Decimal
PX.Objects.IN.INTran.TranCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.IN.INTran.TranDesc : Edm.String "Description"
PX.Objects.IN.INTran.AccrueCost : Edm.Boolean [required]
PX.Objects.IN.INTran.ReasonCode : Edm.String "Reason Code"
PX.Objects.IN.INTran.OrigQty : Edm.Decimal
PX.Objects.IN.INTran.BaseQty : Edm.Decimal [required]
PX.Objects.IN.INTran.MaxTransferBaseQty : Edm.Decimal
PX.Objects.IN.INTran.UnassignedQty : Edm.Decimal [required]
PX.Objects.IN.INTran.CostedQty : Edm.Decimal
PX.Objects.IN.INTran.OrigTranCost : Edm.Decimal
PX.Objects.IN.INTran.OrigTranAmt : Edm.Decimal
PX.Objects.IN.INTran.ARDocType : Edm.String
PX.Objects.IN.INTran.ARRefNbr : Edm.String
PX.Objects.IN.INTran.ARLineNbr : Edm.Int32
PX.Objects.IN.INTran.SOShipmentType : Edm.String
PX.Objects.IN.INTran.SOShipmentNbr : Edm.String "SO Shipment Nbr."
PX.Objects.IN.INTran.SOShipmentLineNbr : Edm.Int32
PX.Objects.IN.INTran.SOLineType : Edm.String
PX.Objects.IN.INTran.UpdateShippedNotInvoiced : Edm.Boolean
PX.Objects.IN.INTran.POReceiptType : Edm.String "PO Receipt Type"
PX.Objects.IN.INTran.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.IN.INTran.POReceiptLineNbr : Edm.Int32
PX.Objects.IN.INTran.AssyType : Edm.String
PX.Objects.IN.INTran.OrigPlanType : Edm.String
PX.Objects.IN.INTran.ToCostCenterID : Edm.Int32 [required]
PX.Objects.IN.INTran.ReceiptedBaseQty : Edm.Decimal "Received Base Qty."
PX.Objects.IN.INTran.INTransitBaseQty : Edm.Decimal "In-Transit Base Qty."
PX.Objects.IN.INTran.ReceiptedQty : Edm.Decimal "Received Qty."
PX.Objects.IN.INTran.INTransitQty : Edm.Decimal "In-Transit Qty."
PX.Objects.IN.INTran.IsCostUnmanaged : Edm.Boolean
PX.Objects.IN.INTran.IsComponentItem : Edm.Boolean [required]
PX.Objects.IN.INTran.NoteID : Edm.Guid
PX.Objects.IN.INTran.NoteText : Edm.String "Note Text"
PX.Objects.IN.INTran.PIID : Edm.String
PX.Objects.IN.INTran.PILineNbr : Edm.Int32 "PI Line Nbr."
PX.Objects.IN.INTran.OrigUOM : Edm.String
PX.Objects.IN.INTran.OrigFullQty : Edm.Decimal
PX.Objects.IN.INTran.BaseOrigFullQty : Edm.Decimal
PX.Objects.IN.INTran.IsUnassigned : Edm.Boolean [required]
PX.Objects.IN.INTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INTran.CreatedByScreenID : Edm.String
PX.Objects.IN.INTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INTran.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTran.tstamp : Edm.Binary
PX.Objects.IN.INTran.SalesMult : Edm.Int16
PX.Objects.IN.INTran.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.IN.INTran.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.IN.INTran.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.IN.INTran.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.IN.INTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INTran.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.IN.INTran.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.IN.INTran.ARRegisterByARRefNbr -> PX.Objects.AR.ARRegister (ARDocType=DocType, ARRefNbr=RefNbr)
PX.Objects.IN.INTran.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.IN.INTran.BranchByDestBranchID -> PX.Objects.GL.Branch (DestBranchID=BranchID)
PX.Objects.IN.INTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INTran.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOOrderLineNbr=LineNbr)
PX.Objects.IN.INTran.SOOrderShipmentBySOShipmentType -> PX.Objects.SO.SOOrderShipment (SOShipmentNbr=ShipmentNbr, SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOShipmentType=ShipmentType)
PX.Objects.IN.INTran.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.IN.INTran.SOShipLineBySOShipmentLineNbr -> PX.Objects.SO.SOShipLine (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr, SOShipmentLineNbr=LineNbr)
PX.Objects.IN.INTran.SOShipmentBySOShipmentNbr -> PX.Objects.SO.SOShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr)
PX.Objects.IN.INTran.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.IN.INTran.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.IN.INTran.POReceiptLineByPOReceiptLineNbr -> PX.Objects.PO.POReceiptLine (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr, POReceiptLineNbr=LineNbr)
PX.Objects.IN.INTran.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.IN.INTran.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.IN.INTran.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INTran.INLocationByToLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INTran.INLocationByOrigToLocationID -> PX.Objects.IN.INLocation (OrigToLocationID=LocationID)
PX.Objects.IN.INTran.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.INTran.INPIDetailByPILineNbr -> PX.Objects.IN.INPIDetail (PIID=PIID, PILineNbr=LineNbr)
PX.Objects.IN.INTran.INPIHeaderByPIID -> PX.Objects.IN.INPIHeader (PIID=PIID)
PX.Objects.IN.INTran.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INTran.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INTran.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INTran.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.IN.INTran.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INTran.AccountByInvtAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INTran.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.IN.INTran.SubByInvtSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INTran.SubByCOGSSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INTran.ARTranByARLineNbr -> PX.Objects.AR.ARTran (ARDocType=TranType, ARRefNbr=RefNbr, ARLineNbr=LineNbr)
PX.Objects.IN.INTran.INKitRegisterByRefNbr -> PX.Objects.IN.INKitRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INTran.INCostStatusByLocationID -> PX.Objects.IN.INCostStatus (OrigRefNbr=ReceiptNbr, InventoryID=InventoryID, CostCenterID=CostSiteID)
PX.Objects.IN.INTran.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.IN.INTran.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.IN.INTran.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INTran.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.INTran.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INTran.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INTran.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.INTran.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.Objects.IN.INTran.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.IN.INTran.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.IN.INTran.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.INTran.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.INTran.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.IN.INTranCost (EntityType)

Label: "IN Transaction Cost"
Key: CostDocType, CostID, CostRefNbr, DocType, LineNbr, RefNbr
Entity sets: PX_Objects_IN_INTranCost, INTransactionCost, INTranCost
Non-filterable, non-selectable: TranAmt, QtyOnHand, UnitCost, TotalCost

PX.Objects.IN.INTranCost.DocType : Edm.String [key]
PX.Objects.IN.INTranCost.TranType : Edm.String "Transaction Type"
PX.Objects.IN.INTranCost.RefNbr : Edm.String [key] "Ref. Number"
PX.Objects.IN.INTranCost.LineNbr : Edm.Int32 [key]
PX.Objects.IN.INTranCost.CostID : Edm.Int64 [key]
PX.Objects.IN.INTranCost.CostDocType : Edm.String [key]
PX.Objects.IN.INTranCost.CostRefNbr : Edm.String [key]
PX.Objects.IN.INTranCost.IsOversold : Edm.Boolean [required]
PX.Objects.IN.INTranCost.InvtMult : Edm.Int16 [required] "Inventory Multiplier"
PX.Objects.IN.INTranCost.Qty : Edm.Decimal [required] "Qty."
PX.Objects.IN.INTranCost.OversoldQty : Edm.Decimal
PX.Objects.IN.INTranCost.TranCost : Edm.Decimal [required] "Transaction Cost"
PX.Objects.IN.INTranCost.OversoldTranCost : Edm.Decimal
PX.Objects.IN.INTranCost.VarCost : Edm.Decimal [required]
PX.Objects.IN.INTranCost.TranAmt : Edm.Decimal
PX.Objects.IN.INTranCost.TranDate : Edm.DateTimeOffset [required] "Transaction Date"
PX.Objects.IN.INTranCost.FinPeriodID : Edm.String
PX.Objects.IN.INTranCost.TranPeriodID : Edm.String
PX.Objects.IN.INTranCost.InventoryID : Edm.Int32
PX.Objects.IN.INTranCost.SiteID : Edm.Int32
PX.Objects.IN.INTranCost.CostSiteID : Edm.Int32
PX.Objects.IN.INTranCost.LotSerialNbr : Edm.String
PX.Objects.IN.INTranCost.IsVirtual : Edm.Boolean [required]
PX.Objects.IN.INTranCost.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INTranCost.CreatedByScreenID : Edm.String
PX.Objects.IN.INTranCost.CreatedDateTime : Edm.DateTimeOffset "Created"
PX.Objects.IN.INTranCost.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INTranCost.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INTranCost.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTranCost.tstamp : Edm.Binary
PX.Objects.IN.INTranCost.QtyOnHand : Edm.Decimal
PX.Objects.IN.INTranCost.UnitCost : Edm.Decimal
PX.Objects.IN.INTranCost.TotalCost : Edm.Decimal
PX.Objects.IN.INTranCost.CostType : Edm.String
PX.Objects.IN.INTranCost.INTranByLineNbr -> PX.Objects.IN.INTran (DocType=DocType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.IN.INTranCost.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INTranCost.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INTranCost.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INTranCost.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INTranCost.INRegisterByCostRefNbr -> PX.Objects.IN.INRegister (CostDocType=DocType, CostRefNbr=RefNbr)
PX.Objects.IN.INTranCost.INSiteByCostSiteID -> PX.Objects.IN.INSite (CostSiteID=SiteID)
PX.Objects.IN.INTranCost.INSubItemByCostSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INTranCost.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INTranCost.AccountByInvtAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INTranCost.SubByCOGSSubID -> PX.Objects.GL.Sub
PX.Objects.IN.INTranCost.SubByInvtSubID -> PX.Objects.GL.Sub

# PX.Objects.IN.INTranDetail (EntityType)

Label: "IN Transaction Detail"
Key: DocType, LineNbr, RefNbr, SplitLineNbr, TranType
Entity sets: PX_Objects_IN_INTranDetail, INTransactionDetail, INTranDetail
Non-filterable, non-selectable: TranCost

PX.Objects.IN.INTranDetail.TranType : Edm.String [key] "Transaction Type"
PX.Objects.IN.INTranDetail.DocType : Edm.String [key] "Document Type"
PX.Objects.IN.INTranDetail.RefNbr : Edm.String [key] "Ref. Number"
PX.Objects.IN.INTranDetail.LineNbr : Edm.Int32 [key] "Line Number"
PX.Objects.IN.INTranDetail.SplitLineNbr : Edm.Int32 [key]
PX.Objects.IN.INTranDetail.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.IN.INTranDetail.FinPeriodID : Edm.String
PX.Objects.IN.INTranDetail.TranPeriodID : Edm.String
PX.Objects.IN.INTranDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INTranDetail.CostSiteID : Edm.Int32
PX.Objects.IN.INTranDetail.InvtMult : Edm.Int16 "Inventory Multiplier"
PX.Objects.IN.INTranDetail.SumQty : Edm.Decimal
PX.Objects.IN.INTranDetail.SumTranCost : Edm.Decimal
PX.Objects.IN.INTranDetail.LotSerialNbr : Edm.String "Lot/Serial Number"
PX.Objects.IN.INTranDetail.UOM : Edm.String
PX.Objects.IN.INTranDetail.Qty : Edm.Decimal "Qty."
PX.Objects.IN.INTranDetail.BaseQty : Edm.Decimal "Base Qty."
PX.Objects.IN.INTranDetail.TranCost : Edm.Decimal
PX.Objects.IN.INTranDetail.INTranByLineNbr -> PX.Objects.IN.INTran (DocType=DocType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.IN.INTranDetail.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INTranDetail.INKitRegisterByRefNbr -> PX.Objects.IN.INKitRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INTranDetail.INKitSerialPartCollection -> Collection(PX.Objects.IN.INKitSerialPart)
PX.Objects.IN.INTranDetail.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.IN.INTransfer (EntityType)

Label: "Receipt"
BaseType: PX.Objects.IN.INRegister
Key: DocType, RefNbr (inherited from PX.Objects.IN.INRegister)
Entity sets: PX_Objects_IN_INTransfer

# PX.Objects.IN.INTransferLocationStatus (EntityType)

Key: InventoryID, SubItemID, TransferNbr
Entity sets: PX_Objects_IN_INTransferLocationStatus

PX.Objects.IN.INTransferLocationStatus.InventoryID : Edm.Int32 [key]
PX.Objects.IN.INTransferLocationStatus.SubItemID : Edm.Int32 [key]
PX.Objects.IN.INTransferLocationStatus.TransferNbr : Edm.String [key]
PX.Objects.IN.INTransferLocationStatus.QtyOnHand : Edm.Decimal
PX.Objects.IN.INTransferLocationStatus.ToSiteID : Edm.Int32 "To Warehouse ID"
PX.Objects.IN.INTransferLocationStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INTransferLocationStatus.INSiteByToSiteID -> PX.Objects.IN.INSite (ToSiteID=SiteID)
PX.Objects.IN.INTransferLocationStatus.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.IN.INTransferStatus (EntityType)

Key: InventoryID, SubItemID, TransferNbr
Entity sets: PX_Objects_IN_INTransferStatus
Non-filterable, non-selectable: UnitCost

PX.Objects.IN.INTransferStatus.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INTransferStatus.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INTransferStatus.TransferNbr : Edm.String [key]
PX.Objects.IN.INTransferStatus.QtyOnHand : Edm.Decimal
PX.Objects.IN.INTransferStatus.TotalCost : Edm.Decimal
PX.Objects.IN.INTransferStatus.DecPlPrcCst : Edm.Int16
PX.Objects.IN.INTransferStatus.UnitCost : Edm.Decimal
PX.Objects.IN.INTransferStatus.ToSiteID : Edm.Int32 "To Warehouse ID"
PX.Objects.IN.INTransferStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INTransferStatus.INRegisterByTransferNbr -> PX.Objects.IN.INRegister (TransferNbr=RefNbr)
PX.Objects.IN.INTransferStatus.INSiteByToSiteID -> PX.Objects.IN.INSite (ToSiteID=SiteID)
PX.Objects.IN.INTransferStatus.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)

# PX.Objects.IN.INTransitLine (EntityType)

Label: "Transfer Line"
Key: TransferLineNbr, TransferNbr
Entity sets: PX_Objects_IN_INTransitLine, TransferLine, INTransitLine
Non-filterable, non-selectable: NoteText

PX.Objects.IN.INTransitLine.CostSiteID : Edm.Int32
PX.Objects.IN.INTransitLine.TransferNbr : Edm.String [key]
PX.Objects.IN.INTransitLine.TransferLineNbr : Edm.Int32 [key]
PX.Objects.IN.INTransitLine.SOOrderType : Edm.String
PX.Objects.IN.INTransitLine.SOOrderNbr : Edm.String
PX.Objects.IN.INTransitLine.SOOrderLineNbr : Edm.Int32
PX.Objects.IN.INTransitLine.SOShipmentType : Edm.String
PX.Objects.IN.INTransitLine.SOShipmentNbr : Edm.String
PX.Objects.IN.INTransitLine.SOShipmentLineNbr : Edm.Int32
PX.Objects.IN.INTransitLine.ToSiteID : Edm.Int32 "To Warehouse ID"
PX.Objects.IN.INTransitLine.OrigModule : Edm.String
PX.Objects.IN.INTransitLine.IsLotSerial : Edm.Boolean [required]
PX.Objects.IN.INTransitLine.NoteID : Edm.Guid
PX.Objects.IN.INTransitLine.NoteText : Edm.String "Note Text"
PX.Objects.IN.INTransitLine.RefNoteID : Edm.Guid
PX.Objects.IN.INTransitLine.IsFixedInTransit : Edm.Boolean [required]
PX.Objects.IN.INTransitLine.TranDate : Edm.DateTimeOffset
PX.Objects.IN.INTransitLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INTransitLine.CreatedByScreenID : Edm.String
PX.Objects.IN.INTransitLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTransitLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INTransitLine.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INTransitLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTransitLine.tstamp : Edm.Binary
PX.Objects.IN.INTransitLine.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.IN.INTransitLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INTransitLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INTransitLine.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOOrderLineNbr=LineNbr)
PX.Objects.IN.INTransitLine.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.IN.INTransitLine.SOShipLineBySOShipmentLineNbr -> PX.Objects.SO.SOShipLine (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr, SOShipmentLineNbr=LineNbr)
PX.Objects.IN.INTransitLine.SOShipmentBySOShipmentNbr -> PX.Objects.SO.SOShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr)
PX.Objects.IN.INTransitLine.INLocationByToLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INTransitLine.INLocationByToSiteID -> PX.Objects.IN.INLocation (ToSiteID=SiteID)
PX.Objects.IN.INTransitLine.INSiteByToSiteID -> PX.Objects.IN.INSite (ToSiteID=SiteID)
PX.Objects.IN.INTransitLine.INSiteBySiteID -> PX.Objects.IN.INSite

# PX.Objects.IN.INTransitLineLotSerialStatus (EntityType)

Key: InventoryID, LotSerialNbr, SubItemID, TransferLineNbr, TransferNbr
Entity sets: PX_Objects_IN_INTransitLineLotSerialStatus

PX.Objects.IN.INTransitLineLotSerialStatus.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INTransitLineLotSerialStatus.SubItemID : Edm.Int32 [key] "Subitem"
PX.Objects.IN.INTransitLineLotSerialStatus.LotSerialNbr : Edm.String [key]
PX.Objects.IN.INTransitLineLotSerialStatus.CostSiteID : Edm.Int32
PX.Objects.IN.INTransitLineLotSerialStatus.ToSiteID : Edm.Int32 "To Warehouse ID"
PX.Objects.IN.INTransitLineLotSerialStatus.OrigModule : Edm.String "Source"
PX.Objects.IN.INTransitLineLotSerialStatus.NoteID : Edm.Guid
PX.Objects.IN.INTransitLineLotSerialStatus.TransferNbr : Edm.String [key]
PX.Objects.IN.INTransitLineLotSerialStatus.TransferLineNbr : Edm.Int32 [key]
PX.Objects.IN.INTransitLineLotSerialStatus.SOOrderType : Edm.String
PX.Objects.IN.INTransitLineLotSerialStatus.SOOrderNbr : Edm.String
PX.Objects.IN.INTransitLineLotSerialStatus.SOOrderLineNbr : Edm.Int32
PX.Objects.IN.INTransitLineLotSerialStatus.SOShipmentType : Edm.String
PX.Objects.IN.INTransitLineLotSerialStatus.SOShipmentNbr : Edm.String
PX.Objects.IN.INTransitLineLotSerialStatus.SOShipmentLineNbr : Edm.Int32
PX.Objects.IN.INTransitLineLotSerialStatus.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.IN.INTransitLineLotSerialStatus.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.IN.INTransitLineLotSerialStatus.QtyHardAvail : Edm.Decimal "Qty. Hard Available"
PX.Objects.IN.INTransitLineLotSerialStatus.QtyInTransit : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyInTransitToSO : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPOPrepared : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPOOrders : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPOReceipts : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtySOBackOrdered : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtySOPrepared : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtySOBooked : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtySOShipped : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtySOShipping : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyINIssues : Edm.Decimal "Qty On Inventory Issues"
PX.Objects.IN.INTransitLineLotSerialStatus.QtyINReceipts : Edm.Decimal "Qty On Inventory Receipts"
PX.Objects.IN.INTransitLineLotSerialStatus.QtyINAssemblyDemand : Edm.Decimal "Qty Demanded by Kit Assembly"
PX.Objects.IN.INTransitLineLotSerialStatus.QtyINAssemblySupply : Edm.Decimal "Qty On Kit Assembly"
PX.Objects.IN.INTransitLineLotSerialStatus.QtySOFixed : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPOFixedOrders : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPOFixedPrepared : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPOFixedReceipts : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtySODropShip : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPODropShipOrders : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPODropShipPrepared : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyPODropShipReceipts : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyNotAvail : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.QtyExpired : Edm.Decimal
PX.Objects.IN.INTransitLineLotSerialStatus.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.IN.INTransitLineLotSerialStatus.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOOrderLineNbr=LineNbr)
PX.Objects.IN.INTransitLineLotSerialStatus.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.IN.INTransitLineLotSerialStatus.SOShipLineBySOShipmentLineNbr -> PX.Objects.SO.SOShipLine (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr, SOShipmentLineNbr=LineNbr)
PX.Objects.IN.INTransitLineLotSerialStatus.SOShipmentBySOShipmentNbr -> PX.Objects.SO.SOShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr)

# PX.Objects.IN.INTransitLineStatus (EntityType)

Key: TransferLineNbr, TransferNbr
Entity sets: PX_Objects_IN_INTransitLineStatus

PX.Objects.IN.INTransitLineStatus.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INTransitLineStatus.CostSiteID : Edm.Int32
PX.Objects.IN.INTransitLineStatus.ToSiteID : Edm.Int32 "To Warehouse ID"
PX.Objects.IN.INTransitLineStatus.OrigModule : Edm.String "Source"
PX.Objects.IN.INTransitLineStatus.NoteID : Edm.Guid
PX.Objects.IN.INTransitLineStatus.RefNoteID : Edm.Guid
PX.Objects.IN.INTransitLineStatus.TransferNbr : Edm.String [key]
PX.Objects.IN.INTransitLineStatus.TransferLineNbr : Edm.Int32 [key]
PX.Objects.IN.INTransitLineStatus.SOOrderType : Edm.String
PX.Objects.IN.INTransitLineStatus.SOOrderNbr : Edm.String
PX.Objects.IN.INTransitLineStatus.SOOrderLineNbr : Edm.Int32
PX.Objects.IN.INTransitLineStatus.SOShipmentType : Edm.String
PX.Objects.IN.INTransitLineStatus.SOShipmentNbr : Edm.String
PX.Objects.IN.INTransitLineStatus.SOShipmentLineNbr : Edm.Int32
PX.Objects.IN.INTransitLineStatus.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.IN.INTransitLineStatus.QtyInTransit : Edm.Decimal
PX.Objects.IN.INTransitLineStatus.QtyInTransitToSO : Edm.Decimal
PX.Objects.IN.INTransitLineStatus.TranDate : Edm.DateTimeOffset "Date"
PX.Objects.IN.INTransitLineStatus.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.IN.INTransitLineStatus.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOOrderLineNbr=LineNbr)
PX.Objects.IN.INTransitLineStatus.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.IN.INTransitLineStatus.SOShipLineBySOShipmentLineNbr -> PX.Objects.SO.SOShipLine (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr, SOShipmentLineNbr=LineNbr)
PX.Objects.IN.INTransitLineStatus.SOShipmentBySOShipmentNbr -> PX.Objects.SO.SOShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr)

# PX.Objects.IN.INTranSplit (EntityType)

Label: "IN Transaction Split"
Key: DocType, LineNbr, RefNbr, SplitLineNbr
Entity sets: PX_Objects_IN_INTranSplit, INTransactionSplit, INTranSplit
Non-filterable, non-selectable: ValMethod, FromSiteID, FromLocationID, LotSerClassID, AssignedNbr, SkipCostUpdate, SkipQtyValidation, ProjectID, TaskID

PX.Objects.IN.INTranSplit.DocType : Edm.String [key] "Type"
PX.Objects.IN.INTranSplit.OrigModule : Edm.String "Source"
PX.Objects.IN.INTranSplit.TranType : Edm.String
PX.Objects.IN.INTranSplit.RefNbr : Edm.String [key] "Ref. Number"
PX.Objects.IN.INTranSplit.LineNbr : Edm.Int32 [key] "Line Number"
PX.Objects.IN.INTranSplit.POLineType : Edm.String
PX.Objects.IN.INTranSplit.SOLineType : Edm.String
PX.Objects.IN.INTranSplit.TransferType : Edm.String
PX.Objects.IN.INTranSplit.ToSiteID : Edm.Int32
PX.Objects.IN.INTranSplit.ToLocationID : Edm.Int32
PX.Objects.IN.INTranSplit.SplitLineNbr : Edm.Int32 [key] "Split Line Number"
PX.Objects.IN.INTranSplit.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.IN.INTranSplit.IsIntercompany : Edm.Boolean [required]
PX.Objects.IN.INTranSplit.InvtMult : Edm.Int16 "Inventory Multiplier"
PX.Objects.IN.INTranSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.INTranSplit.ValMethod : Edm.String
PX.Objects.IN.INTranSplit.CostSubItemID : Edm.Int32
PX.Objects.IN.INTranSplit.CostSiteID : Edm.Int32
PX.Objects.IN.INTranSplit.FromSiteID : Edm.Int32
PX.Objects.IN.INTranSplit.FromLocationID : Edm.Int32
PX.Objects.IN.INTranSplit.LotSerClassID : Edm.String
PX.Objects.IN.INTranSplit.AssignedNbr : Edm.String
PX.Objects.IN.INTranSplit.Released : Edm.Boolean [required] "Released"
PX.Objects.IN.INTranSplit.ReleasedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTranSplit.UOM : Edm.String "UOM"
PX.Objects.IN.INTranSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.IN.INTranSplit.BaseQty : Edm.Decimal
PX.Objects.IN.INTranSplit.QtyIn : Edm.Decimal
PX.Objects.IN.INTranSplit.QtyOut : Edm.Decimal
PX.Objects.IN.INTranSplit.MaxTransferBaseQty : Edm.Decimal
PX.Objects.IN.INTranSplit.OrigPlanType : Edm.String
PX.Objects.IN.INTranSplit.IsFixedInTransit : Edm.Boolean [required]
PX.Objects.IN.INTranSplit.PlanID : Edm.Int64
PX.Objects.IN.INTranSplit.TotalQty : Edm.Decimal [required]
PX.Objects.IN.INTranSplit.TotalCost : Edm.Decimal [required]
PX.Objects.IN.INTranSplit.AdditionalCost : Edm.Decimal [required]
PX.Objects.IN.INTranSplit.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.IN.INTranSplit.EstCost : Edm.Decimal "Estimated Cost"
PX.Objects.IN.INTranSplit.SkipCostUpdate : Edm.Boolean
PX.Objects.IN.INTranSplit.SkipQtyValidation : Edm.Boolean
PX.Objects.IN.INTranSplit.ProjectID : Edm.Int32
PX.Objects.IN.INTranSplit.TaskID : Edm.Int32
PX.Objects.IN.INTranSplit.IsUnassigned : Edm.Boolean [required]
PX.Objects.IN.INTranSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INTranSplit.CreatedByScreenID : Edm.String
PX.Objects.IN.INTranSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTranSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INTranSplit.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INTranSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INTranSplit.tstamp : Edm.Binary
PX.Objects.IN.INTranSplit.INTranByLineNbr -> PX.Objects.IN.INTran (DocType=DocType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.IN.INTranSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INTranSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.IN.INTranSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INTranSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INTranSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.INTranSplit.INLocationByToLocationID -> PX.Objects.IN.INLocation (ToLocationID=LocationID)
PX.Objects.IN.INTranSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.INTranSplit.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INTranSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.INTranSplit.INSiteByToSiteID -> PX.Objects.IN.INSite (ToSiteID=SiteID)
PX.Objects.IN.INTranSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.INTranSplit.INSubItemByCostSubItemID -> PX.Objects.IN.INSubItem (CostSubItemID=SubItemID)
PX.Objects.IN.INTranSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.IN.INTranSplit.INRegisterItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader (DocType=DocType, RefNbr=RefNbr, InventoryID=InventoryID)
PX.Objects.IN.INTranSplit.INKitRegisterByRefNbr -> PX.Objects.IN.INKitRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.IN.INTranSplit.INItemLotSerialByLotSerialNbr -> PX.Objects.IN.INItemLotSerial (InventoryID=InventoryID)
PX.Objects.IN.INTranSplit.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID)
PX.Objects.IN.INTranSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.IN.INTranSplit.INItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.IN.DAC.INItemLotSerialAttributesHeader (InventoryID=InventoryID)
PX.Objects.IN.INTranSplit.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.IN.INTranSplit.INKitSerialPartCollection -> Collection(PX.Objects.IN.INKitSerialPart)
PX.Objects.IN.INTranSplit.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.IN.INUnit (EntityType)

Label: "Inventory Unit Conversions"
Key: FromUnit, InventoryID, ItemClassID, ToUnit, UnitType
Entity sets: PX_Objects_IN_INUnit, InventoryUnitConversions, INUnit
Non-filterable, non-selectable: SampleToUnit

PX.Objects.IN.INUnit.UnitType : Edm.Int16 [key required] "Unit Type"
PX.Objects.IN.INUnit.ItemClassID : Edm.Int32 [key required] "Item Class ID"
PX.Objects.IN.INUnit.InventoryID : Edm.Int32 [key required] "Inventory ID"
PX.Objects.IN.INUnit.ToUnit : Edm.String [key] "To Unit"
PX.Objects.IN.INUnit.SampleToUnit : Edm.String "To Unit"
PX.Objects.IN.INUnit.FromUnit : Edm.String [key] "From Unit"
PX.Objects.IN.INUnit.UnitMultDiv : Edm.String "Multiply/Divide"
PX.Objects.IN.INUnit.UnitRate : Edm.Decimal [required] "Conversion Factor"
PX.Objects.IN.INUnit.PriceAdjustmentMultiplier : Edm.Decimal [required] "Price Adjustment Multiplier"
PX.Objects.IN.INUnit.RecordID : Edm.Int64
PX.Objects.IN.INUnit.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.INUnit.CreatedByScreenID : Edm.String
PX.Objects.IN.INUnit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INUnit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.INUnit.LastModifiedByScreenID : Edm.String
PX.Objects.IN.INUnit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.INUnit.tstamp : Edm.Binary
PX.Objects.IN.INUnit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.INUnit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.INUnit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.INUnit.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.INUnit.INUnitByToUnit -> PX.Objects.IN.INUnit (ToUnit=FromUnit)
PX.Objects.IN.INUnit.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.IN.INUnit.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.IN.INUnit.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.IN.INUnit.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.IN.INUnit.PMChangeRequestTaxCollection -> Collection(PX.Objects.PM.PMChangeRequestTax)
PX.Objects.IN.INUnit.PMChangeRequestTaxTranCollection -> Collection(PX.Objects.PM.PMChangeRequestTaxTran)
PX.Objects.IN.INUnit.GLTaxCollection -> Collection(PX.Objects.GL.GLTax)
PX.Objects.IN.INUnit.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.IN.INUnit.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.IN.INUnit.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.IN.INUnit.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.IN.INUnit.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.IN.INUnit.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.IN.INUnit.POLandedCostTaxCollection -> Collection(PX.Objects.PO.POLandedCostTax)
PX.Objects.IN.INUnit.POLandedCostTaxTranCollection -> Collection(PX.Objects.PO.POLandedCostTaxTran)
PX.Objects.IN.INUnit.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.IN.INUnit.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)
PX.Objects.IN.INUnit.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.INUnit.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.IN.INUnit.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.IN.INUnit.PMChangeOrderTaxTranCollection -> Collection(PX.Objects.PM.PMChangeOrderTaxTran)
PX.Objects.IN.INUnit.PMTaxCollection -> Collection(PX.Objects.PM.PMTax)
PX.Objects.IN.INUnit.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.IN.INUnit.PMTaxTranCollection -> Collection(PX.Objects.PM.PMTaxTran)
PX.Objects.IN.INUnit.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.IN.INUnit.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.IN.INUnit.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.INUnit.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.INUnit.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.INUnit.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.IN.INUnit.CABankChargeTaxCollection -> Collection(PX.Objects.CA.CABankChargeTax)
PX.Objects.IN.INUnit.CABankTaxCollection -> Collection(PX.Objects.CA.CABankTax)
PX.Objects.IN.INUnit.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.IN.INUnit.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.IN.INUnit.CAExpenseTaxCollection -> Collection(PX.Objects.CA.CAExpenseTax)
PX.Objects.IN.INUnit.CATaxCollection -> Collection(PX.Objects.CA.CATax)
PX.Objects.IN.INUnit.CROpportunityTaxCollection -> Collection(PX.Objects.CR.CROpportunityTax)
PX.Objects.IN.INUnit.CRTaxTranCollection -> Collection(PX.Objects.CR.CRTaxTran)
PX.Objects.IN.INUnit.EPTaxCollection -> Collection(PX.Objects.EP.EPTax)
PX.Objects.IN.INUnit.EPTaxAggregateCollection -> Collection(PX.Objects.EP.EPTaxAggregate)
PX.Objects.IN.INUnit.EPTaxTranCollection -> Collection(PX.Objects.EP.EPTaxTran)
PX.Objects.IN.INUnit.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.IN.INUnit.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.IN.INUnit.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.IN.INUnit.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.INUnit.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.INUnit.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.INUnit.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.INUnit.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.INUnit.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.INUnit.FSAppointmentTaxTranCollection -> Collection(PX.Objects.FS.FSAppointmentTaxTran)
PX.Objects.IN.INUnit.FSServiceOrderTaxTranCollection -> Collection(PX.Objects.FS.FSServiceOrderTaxTran)
PX.Objects.IN.INUnit.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.INUnit.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.Objects.IN.INUnit.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)
PX.Objects.IN.INUnit.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.INUnit.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.IN.INUnit.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.INUnit.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.IN.INUnit.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.IN.INUnit.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.IN.INUnit.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.INUnit.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.IN.INUnit.PMAccountGroupCollection -> Collection(PX.Objects.PM.PMAccountGroup)
PX.Objects.IN.INUnit.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.IN.INUnit.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.IN.INUnit.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.IN.INUnit.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.IN.INUnit.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.INUnit.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.IN.INUnit.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.IN.INUnit.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.IN.INUnit.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.Objects.IN.INUnit.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.IN.INUnit.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.IN.INUnit.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.INUnit.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.INUnit.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.INUnit.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.INUnit.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.INUnit.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.INUnit.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.INUnit.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.IN.INUnit.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.IN.INUnit.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.INUnit.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.IN.INUnit.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.IN.INUnit.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.IN.INUnit.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.IN.INUnit.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.INUnit.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.INUnit.FAServiceScheduleCollection -> Collection(PX.Objects.FA.FAServiceSchedule)
PX.Objects.IN.INUnit.FAUsageScheduleCollection -> Collection(PX.Objects.FA.FAUsageSchedule)
PX.Objects.IN.INUnit.CommonSetupCollection -> Collection(PX.Objects.CS.CommonSetup)
PX.Objects.IN.INUnit.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.INUnit.GS1UOMSetupCollection -> Collection(PX.Objects.IN.GS1UOMSetup)
PX.Objects.IN.INUnit.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.IN.INUnit.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.IN.INUnit.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.IN.INUnit.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.INUnit.UnitOfMeasureCollection -> Collection(PX.Objects.IN.UnitOfMeasure)
PX.Objects.IN.INUnit.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.IN.INUnit.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.INUnit.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.IN.INUnit.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.IN.INUnit.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.IN.INUnit.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.IN.INUnit.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.IN.INUnit.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.Objects.IN.INUnit.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.INUnit.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.INUnit.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.INUnit.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.INUnit.AMEstimatePriceBreakCollection -> Collection(PX.Objects.AM.AMEstimatePriceBreak)
PX.Objects.IN.INUnit.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.IN.INUnit.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.IN.INUnit.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.IN.INUnit.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.INUnit.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.INUnit.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.INUnit.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.INUnit.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.INUnit.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.INUnit.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.INUnit.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.IN.INUnit.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.IN.INUnit.FSSalesPriceCollection -> Collection(PX.Objects.FS.FSSalesPrice)
PX.Objects.IN.INUnit.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.IN.INUnit.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.Objects.IN.INUnit.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.INUnit.SPInventoryCartItemCollection -> Collection(PX.Objects.Portals.SP.DAC.SPInventoryCartItem)
PX.Objects.IN.INUnit.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.INUnit.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.IN.INUnit.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.IN.INUnit.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.IN.INUnit.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.IN.INUnit.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.IN.INUnit.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.IN.INUnit.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.INUnit.ContractDetailAcumCollection -> Collection(PX.Objects.CT.ContractDetailAcum)

# PX.Objects.IN.INUpdateStdCostRecord (EntityType)

Key: CuryID, InventoryID
Entity sets: PX_Objects_IN_INUpdateStdCostRecord

PX.Objects.IN.INUpdateStdCostRecord.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.INUpdateStdCostRecord.Descr : Edm.String "Description"
PX.Objects.IN.INUpdateStdCostRecord.RecordID : Edm.Int32
PX.Objects.IN.INUpdateStdCostRecord.PendingStdCost : Edm.Decimal "Pending Cost"
PX.Objects.IN.INUpdateStdCostRecord.PendingStdCostDate : Edm.DateTimeOffset "Pending Cost Date"
PX.Objects.IN.INUpdateStdCostRecord.PendingStdCostReset : Edm.Boolean
PX.Objects.IN.INUpdateStdCostRecord.StdCost : Edm.Decimal "Current Cost"
PX.Objects.IN.INUpdateStdCostRecord.StdCostOverride : Edm.Boolean "Std. Cost Override"
PX.Objects.IN.INUpdateStdCostRecord.CuryID : Edm.String [key] "Currency"
PX.Objects.IN.INUpdateStdCostRecord.IsTemplate : Edm.Boolean
PX.Objects.IN.INUpdateStdCostRecord.StkItem : Edm.Boolean
PX.Objects.IN.INUpdateStdCostRecord.AccountByInvtAcctID -> PX.Objects.GL.Account
PX.Objects.IN.INUpdateStdCostRecord.SubByInvtSubID -> PX.Objects.GL.Sub

# PX.Objects.IN.InventoryItem (EntityType)

Label: "Inventory Item"
Key: InventoryCD
Entity sets: PX_Objects_IN_InventoryItem, InventoryItem
Non-filterable, non-selectable: IsConversionMode, ExpenseAccrualAcctID, ExpenseAccrualSubID, ExpenseAcctID, ExpenseSubID, NegQty, TotalPercentage, NoteText, NotePopupText, Included, HasChild, SampleID, SampleDescription, UpdateOnlySelected, DiscAcctID, DiscSubID, EntityTypeID, Secured, DeletedDatabaseRecord

PX.Objects.IN.InventoryItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.InventoryItem.InventoryCD : Edm.String [key] "Inventory ID"
PX.Objects.IN.InventoryItem.IsConverted : Edm.Boolean [required] "Is Converted"
PX.Objects.IN.InventoryItem.IsConversionMode : Edm.Boolean
PX.Objects.IN.InventoryItem.StkItem : Edm.Boolean [required] "Stock Item"
PX.Objects.IN.InventoryItem.Descr : Edm.String "Description"
PX.Objects.IN.InventoryItem.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.IN.InventoryItem.ParentItemClassID : Edm.Int32
PX.Objects.IN.InventoryItem.ItemStatus : Edm.String "Item Status"
PX.Objects.IN.InventoryItem.ItemType : Edm.String "Type"
PX.Objects.IN.InventoryItem.ValMethod : Edm.String "Valuation Method"
PX.Objects.IN.InventoryItem.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.IN.InventoryItem.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.IN.InventoryItem.WeightItem : Edm.Boolean [required] "Weight Item"
PX.Objects.IN.InventoryItem.BaseUnit : Edm.String "Base Unit"
PX.Objects.IN.InventoryItem.SalesUnit : Edm.String "Sales Unit"
PX.Objects.IN.InventoryItem.PurchaseUnit : Edm.String "Purchase Unit"
PX.Objects.IN.InventoryItem.DecimalBaseUnit : Edm.Boolean [required] "Divisible Unit"
PX.Objects.IN.InventoryItem.DecimalSalesUnit : Edm.Boolean [required] "Divisible Unit"
PX.Objects.IN.InventoryItem.DecimalPurchaseUnit : Edm.Boolean [required] "Divisible Unit"
PX.Objects.IN.InventoryItem.Commisionable : Edm.Boolean [required] "Subject to Commission"
PX.Objects.IN.InventoryItem.PostClassID : Edm.String "Posting Class"
PX.Objects.IN.InventoryItem.ExpenseAccrualAcctID : Edm.Int32
PX.Objects.IN.InventoryItem.ExpenseAccrualSubID : Edm.Int32
PX.Objects.IN.InventoryItem.ExpenseAcctID : Edm.Int32
PX.Objects.IN.InventoryItem.ExpenseSubID : Edm.Int32
PX.Objects.IN.InventoryItem.LastSiteID : Edm.Int32
PX.Objects.IN.InventoryItem.LastStdCost : Edm.Decimal [required] "Last Cost"
PX.Objects.IN.InventoryItem.PendingStdCost : Edm.Decimal [required] "Pending Cost"
PX.Objects.IN.InventoryItem.PendingStdCostDate : Edm.DateTimeOffset "Pending Cost Date"
PX.Objects.IN.InventoryItem.StdCost : Edm.Decimal [required] "Current Cost"
PX.Objects.IN.InventoryItem.StdCostDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.IN.InventoryItem.BasePrice : Edm.Decimal [required] "Default Price"
PX.Objects.IN.InventoryItem.BaseWeight : Edm.Decimal [required]
PX.Objects.IN.InventoryItem.BaseVolume : Edm.Decimal [required] "Volume"
PX.Objects.IN.InventoryItem.BaseItemWeight : Edm.Decimal [required] "Weight"
PX.Objects.IN.InventoryItem.BaseItemVolume : Edm.Decimal [required] "Volume"
PX.Objects.IN.InventoryItem.WeightUOM : Edm.String "Weight UOM"
PX.Objects.IN.InventoryItem.VolumeUOM : Edm.String "Volume UOM"
PX.Objects.IN.InventoryItem.PackSeparately : Edm.Boolean [required] "Pack Separately"
PX.Objects.IN.InventoryItem.PackageOption : Edm.String "Packaging Option"
PX.Objects.IN.InventoryItem.PreferredVendorID : Edm.Int32 "Preferred Vendor"
PX.Objects.IN.InventoryItem.DefaultSubItemOnEntry : Edm.Boolean [required] "Use On Entry"
PX.Objects.IN.InventoryItem.ProductWorkgroupID : Edm.Int32 "Product Workgroup"
PX.Objects.IN.InventoryItem.ProductManagerID : Edm.Int32 "Product Manager"
PX.Objects.IN.InventoryItem.PriceWorkgroupID : Edm.Int32 "Price Workgroup"
PX.Objects.IN.InventoryItem.PriceManagerID : Edm.Int32 "Price Manager"
PX.Objects.IN.InventoryItem.NegQty : Edm.Boolean
PX.Objects.IN.InventoryItem.OrigLotSerClassID : Edm.String
PX.Objects.IN.InventoryItem.LotSerClassID : Edm.String "Lot/Serial Class"
PX.Objects.IN.InventoryItem.DeferredCode : Edm.String "Deferral Code"
PX.Objects.IN.InventoryItem.DefaultTerm : Edm.Decimal [required] "Default Term"
PX.Objects.IN.InventoryItem.DefaultTermUOM : Edm.String "Default Term UOM"
PX.Objects.IN.InventoryItem.PriceClassID : Edm.String "Price Class"
PX.Objects.IN.InventoryItem.IsSplitted : Edm.Boolean [required] "Split into Components"
PX.Objects.IN.InventoryItem.TotalPercentage : Edm.Decimal "Total Percentage"
PX.Objects.IN.InventoryItem.KitItem : Edm.Boolean [required] "Kit"
PX.Objects.IN.InventoryItem.MinGrossProfitPct : Edm.Decimal [required] "Min. Markup %"
PX.Objects.IN.InventoryItem.NonStockReceipt : Edm.Boolean [required] "Require Receipt"
PX.Objects.IN.InventoryItem.NonStockReceiptAsService : Edm.Boolean "Process Item via Receipt"
PX.Objects.IN.InventoryItem.NonStockShip : Edm.Boolean [required] "Require Shipment"
PX.Objects.IN.InventoryItem.PostToExpenseAccount : Edm.String "Post Cost to Expenses On"
PX.Objects.IN.InventoryItem.CostBasis : Edm.String "Cost Based On"
PX.Objects.IN.InventoryItem.PercentOfSalesPrice : Edm.Decimal [required] "Percent of Sales Price"
PX.Objects.IN.InventoryItem.CompletePOLine : Edm.String "Close PO Line"
PX.Objects.IN.InventoryItem.ABCCodeID : Edm.String "ABC Code"
PX.Objects.IN.InventoryItem.ABCCodeIsFixed : Edm.Boolean [required] "Fixed ABC Code"
PX.Objects.IN.InventoryItem.MovementClassID : Edm.String "Movement Class"
PX.Objects.IN.InventoryItem.MovementClassIsFixed : Edm.Boolean [required] "Fixed Movement Class"
PX.Objects.IN.InventoryItem.MarkupPct : Edm.Decimal "Markup %"
PX.Objects.IN.InventoryItem.RecPrice : Edm.Decimal "MSRP"
PX.Objects.IN.InventoryItem.ImageUrl : Edm.String "Image"
PX.Objects.IN.InventoryItem.CommodityCodeType : Edm.String "Commodity Code Type"
PX.Objects.IN.InventoryItem.HSTariffCode : Edm.String "Commodity Code"
PX.Objects.IN.InventoryItem.UndershipThreshold : Edm.Decimal [required] "Undership Threshold (%)"
PX.Objects.IN.InventoryItem.OvershipThreshold : Edm.Decimal [required] "Overship Threshold (%)"
PX.Objects.IN.InventoryItem.CountryOfOrigin : Edm.String "Country Of Origin"
PX.Objects.IN.InventoryItem.NoteID : Edm.Guid
PX.Objects.IN.InventoryItem.NoteText : Edm.String "Note Text"
PX.Objects.IN.InventoryItem.NotePopupText : Edm.String "Note Text"
PX.Objects.IN.InventoryItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.InventoryItem.CreatedByScreenID : Edm.String
PX.Objects.IN.InventoryItem.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.InventoryItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.InventoryItem.LastModifiedByScreenID : Edm.String
PX.Objects.IN.InventoryItem.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.InventoryItem.tstamp : Edm.Binary
PX.Objects.IN.InventoryItem.CycleID : Edm.String "PI Cycle"
PX.Objects.IN.InventoryItem.Included : Edm.Boolean "Included"
PX.Objects.IN.InventoryItem.Body : Edm.String "Content"
PX.Objects.IN.InventoryItem.IsTemplate : Edm.Boolean [required]
PX.Objects.IN.InventoryItem.GenerationRuleCntr : Edm.Int32 [required]
PX.Objects.IN.InventoryItem.HasChild : Edm.Boolean
PX.Objects.IN.InventoryItem.AttributeDescriptionGroupID : Edm.Int32
PX.Objects.IN.InventoryItem.ColumnAttributeValue : Edm.String
PX.Objects.IN.InventoryItem.RowAttributeValue : Edm.String
PX.Objects.IN.InventoryItem.SampleID : Edm.String
PX.Objects.IN.InventoryItem.SampleDescription : Edm.String
PX.Objects.IN.InventoryItem.UpdateOnlySelected : Edm.Boolean "Update Only Selected Items with Template Changes"
PX.Objects.IN.InventoryItem.DiscAcctID : Edm.Int32
PX.Objects.IN.InventoryItem.DiscSubID : Edm.Int32
PX.Objects.IN.InventoryItem.Visibility : Edm.String "Visibility"
PX.Objects.IN.InventoryItem.Availability : Edm.String "Availability"
PX.Objects.IN.InventoryItem.NotAvailMode : Edm.String "When Qty Unavailable"
PX.Objects.IN.InventoryItem.AvailabilityAdjustment : Edm.Decimal [required] "Availability Adjustment"
PX.Objects.IN.InventoryItem.ExportToExternal : Edm.Boolean "Export to External System"
PX.Objects.IN.InventoryItem.ReplenishmentSource : Edm.String "Source"
PX.Objects.IN.InventoryItem.SOSource : Edm.String "Source for Sales Order"
PX.Objects.IN.InventoryItem.EntityTypeID : Edm.Int32
PX.Objects.IN.InventoryItem.Secured : Edm.Boolean "Secured"
PX.Objects.IN.InventoryItem.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.IN.InventoryItem.EPEmployeeByProductManagerID -> PX.Objects.EP.EPEmployee (ProductManagerID=BAccountID)
PX.Objects.IN.InventoryItem.EPEmployeeByPriceManagerID -> PX.Objects.EP.EPEmployee (PriceManagerID=BAccountID)
PX.Objects.IN.InventoryItem.BAccountByPreferredVendorID -> PX.Objects.CR.BAccount (PreferredVendorID=BAccountID)
PX.Objects.IN.InventoryItem.ContactByProductManagerID -> PX.Objects.CR.Contact (ProductManagerID=ContactID)
PX.Objects.IN.InventoryItem.ContactByPriceManagerID -> PX.Objects.CR.Contact (PriceManagerID=ContactID)
PX.Objects.IN.InventoryItem.InventoryItemByTemplateItemID -> PX.Objects.IN.InventoryItem
PX.Objects.IN.InventoryItem.DRDeferredCodeByDeferredCode -> PX.Objects.DR.DRDeferredCode (DeferredCode=DeferredCodeID)
PX.Objects.IN.InventoryItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.InventoryItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.InventoryItem.EPCompanyTreeByProductWorkgroupID -> PX.TM.EPCompanyTree (ProductWorkgroupID=WorkGroupID)
PX.Objects.IN.InventoryItem.EPCompanyTreeByPriceWorkgroupID -> PX.TM.EPCompanyTree (PriceWorkgroupID=WorkGroupID)
PX.Objects.IN.InventoryItem.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.IN.InventoryItem.PMCostCodeByDefaultCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.IN.InventoryItem.CountryByCountryOfOrigin -> PX.Objects.CS.Country (CountryOfOrigin=CountryID)
PX.Objects.IN.InventoryItem.INABCCodeByABCCodeID -> PX.Objects.IN.INABCCode (ABCCodeID=ABCCodeID)
PX.Objects.IN.InventoryItem.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.InventoryItem.INLocationByDfltSiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.InventoryItem.INLotSerClassByLotSerClassID -> PX.Objects.IN.INLotSerClass (LotSerClassID=LotSerClassID)
PX.Objects.IN.InventoryItem.INMovementClassByMovementClassID -> PX.Objects.IN.INMovementClass (MovementClassID=MovementClassID)
PX.Objects.IN.InventoryItem.INPICycleByCycleID -> PX.Objects.IN.INPICycle (CycleID=CycleID)
PX.Objects.IN.InventoryItem.INPostClassByPostClassID -> PX.Objects.IN.INPostClass (PostClassID=PostClassID)
PX.Objects.IN.InventoryItem.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.IN.InventoryItem.INSiteByLastSiteID -> PX.Objects.IN.INSite (LastSiteID=SiteID)
PX.Objects.IN.InventoryItem.INSiteByDfltSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.InventoryItem.INSubItemByDefaultSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.IN.InventoryItem.INUnitByBaseUnit -> PX.Objects.IN.INUnit (BaseUnit=FromUnit)
PX.Objects.IN.InventoryItem.INUnitByInventoryID -> PX.Objects.IN.INUnit (SalesUnit=FromUnit, InventoryID=InventoryID)
PX.Objects.IN.InventoryItem.INUnitByWeightUOM -> PX.Objects.IN.INUnit (WeightUOM=FromUnit)
PX.Objects.IN.InventoryItem.INUnitByVolumeUOM -> PX.Objects.IN.INUnit (VolumeUOM=FromUnit)
PX.Objects.IN.InventoryItem.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.AccountByInvtAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.AccountByStdCstRevAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.AccountByPPVAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.AccountByDeferralAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.AccountByStdCstVarAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.AccountByLCVarianceAcctID -> PX.Objects.GL.Account
PX.Objects.IN.InventoryItem.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByInvtSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByCOGSSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByStdCstRevSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByPPVSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByDeferralSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByStdCstVarSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByReasonCodeSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.SubByLCVarianceSubID -> PX.Objects.GL.Sub
PX.Objects.IN.InventoryItem.LocationByPreferredVendorID -> PX.Objects.CR.Location (PreferredVendorID=BAccountID)
PX.Objects.IN.InventoryItem.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.IN.InventoryItem.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.IN.InventoryItem.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.IN.InventoryItem.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.IN.InventoryItem.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.IN.InventoryItem.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.IN.InventoryItem.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.IN.InventoryItem.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.IN.InventoryItem.FSAppointmentLogExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentLogExtItemLine)
PX.Objects.IN.InventoryItem.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.IN.InventoryItem.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.IN.InventoryItem.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.IN.InventoryItem.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.IN.InventoryItem.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.InventoryItem.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.InventoryItem.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.IN.InventoryItem.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.IN.InventoryItem.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.IN.InventoryItem.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.IN.InventoryItem.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.IN.InventoryItem.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.IN.InventoryItem.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.InventoryItem.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.InventoryItem.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.InventoryItem.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.InventoryItem.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.IN.InventoryItem.INMatrixExcludedDataCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
PX.Objects.IN.InventoryItem.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.IN.InventoryItem.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.Objects.IN.InventoryItem.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.IN.InventoryItem.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.IN.InventoryItem.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.IN.InventoryItem.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.IN.InventoryItem.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.InventoryItem.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.IN.InventoryItem.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.InventoryItem.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.InventoryItem.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.InventoryItem.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.IN.InventoryItem.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.InventoryItem.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.InventoryItem.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.InventoryItem.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.IN.InventoryItem.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.IN.InventoryItem.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.IN.InventoryItem.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.InventoryItem.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.IN.InventoryItem.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.InventoryItem.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.IN.InventoryItem.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.IN.InventoryItem.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.IN.InventoryItem.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.InventoryItem.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.IN.InventoryItem.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.IN.InventoryItem.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.IN.InventoryItem.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.IN.InventoryItem.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.InventoryItem.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.IN.InventoryItem.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.IN.InventoryItem.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.IN.InventoryItem.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.Objects.IN.InventoryItem.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.IN.InventoryItem.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.IN.InventoryItem.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.IN.InventoryItem.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.IN.InventoryItem.InventoryPostingBatchDetailCollection -> Collection(PX.Objects.FS.InventoryPostingBatchDetail)
PX.Objects.IN.InventoryItem.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.IN.InventoryItem.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.InventoryItem.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.InventoryItem.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.InventoryItem.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.InventoryItem.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.InventoryItem.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.IN.InventoryItem.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.InventoryItem.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.InventoryItem.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.InventoryItem.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.InventoryItem.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.InventoryItem.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.IN.InventoryItem.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.IN.InventoryItem.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.Objects.IN.InventoryItem.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.IN.InventoryItem.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.IN.InventoryItem.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.IN.InventoryItem.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.IN.InventoryItem.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.IN.InventoryItem.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.InventoryItem.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.IN.InventoryItem.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.IN.InventoryItem.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.IN.InventoryItem.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.IN.InventoryItem.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.IN.InventoryItem.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.IN.InventoryItem.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.IN.InventoryItem.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.IN.InventoryItem.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.Objects.IN.InventoryItem.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.InventoryItem.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.InventoryItem.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.IN.InventoryItem.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.IN.InventoryItem.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.IN.InventoryItem.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.InventoryItem.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)
PX.Objects.IN.InventoryItem.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.Objects.IN.InventoryItem.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.IN.InventoryItem.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.IN.InventoryItem.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.Objects.IN.InventoryItem.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.IN.InventoryItem.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.IN.InventoryItem.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.IN.InventoryItem.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.Objects.IN.InventoryItem.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.InventoryItem.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.IN.InventoryItem.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.InventoryItem.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.IN.InventoryItem.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.InventoryItem.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.IN.InventoryItem.InventoryItemLotSerNumValCollection -> Collection(PX.Objects.IN.InventoryItemLotSerNumVal)
PX.Objects.IN.InventoryItem.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.IN.InventoryItem.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.IN.InventoryItem.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.IN.InventoryItem.INRelatedInventoryUserFeedbackCollection -> Collection(PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback)
PX.Objects.IN.InventoryItem.INAttributeDescriptionGroupCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup)
PX.Objects.IN.InventoryItem.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.Objects.IN.InventoryItem.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.IN.InventoryItem.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.IN.InventoryItem.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.InventoryItem.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.IN.InventoryItem.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)
PX.Objects.IN.InventoryItem.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.Objects.IN.InventoryItem.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.IN.InventoryItem.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.IN.InventoryItem.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.IN.InventoryItem.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.Objects.IN.InventoryItem.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.IN.InventoryItem.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.IN.InventoryItem.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.IN.InventoryItem.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.IN.InventoryItem.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.IN.InventoryItem.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.IN.InventoryItem.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.Objects.IN.InventoryItem.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.Objects.IN.InventoryItem.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.IN.InventoryItem.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.IN.InventoryItem.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.IN.InventoryItem.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.IN.InventoryItem.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.IN.InventoryItem.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.IN.InventoryItem.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.IN.InventoryItem.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Objects.IN.InventoryItem.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.Objects.IN.InventoryItem.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.IN.InventoryItem.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.IN.InventoryItem.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.InventoryItem.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.InventoryItem.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.InventoryItem.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.IN.InventoryItem.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.IN.InventoryItem.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.IN.InventoryItem.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.IN.InventoryItem.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.IN.InventoryItem.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.IN.InventoryItem.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.InventoryItem.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.Objects.IN.InventoryItem.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.IN.InventoryItem.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.IN.InventoryItem.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.IN.InventoryItem.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.IN.InventoryItem.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.IN.InventoryItem.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.InventoryItem.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.InventoryItem.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.InventoryItem.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.IN.InventoryItem.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.IN.InventoryItem.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.IN.InventoryItem.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.InventoryItem.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.InventoryItem.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.InventoryItem.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.IN.InventoryItem.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.InventoryItem.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.IN.InventoryItem.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.IN.InventoryItem.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.IN.InventoryItem.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.IN.InventoryItem.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.Objects.IN.InventoryItem.FSServiceInventoryItemCollection -> Collection(PX.Objects.FS.FSServiceInventoryItem)
PX.Objects.IN.InventoryItem.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)
PX.Objects.IN.InventoryItem.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)
PX.Objects.IN.InventoryItem.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.Objects.IN.InventoryItem.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)
PX.Objects.IN.InventoryItem.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.InventoryItem.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.IN.InventoryItem.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.IN.InventoryItem.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.IN.InventoryItem.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.IN.InventoryItem.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.IN.InventoryItem.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.IN.InventoryItem.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.IN.InventoryItem.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.IN.InventoryItem.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.IN.InventoryItem.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.IN.InventoryItem.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.InventoryItem.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.IN.InventoryItem.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.IN.InventoryItem.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.IN.InventoryItem.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.IN.InventoryItem.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.InventoryItem.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.IN.InventoryItem.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.IN.InventoryItem.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.IN.InventoryItem.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.IN.InventoryItem.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.IN.InventoryItem.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.IN.InventoryItem.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.IN.InventoryItem.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.IN.InventoryItem.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.IN.InventoryItem.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.IN.InventoryItem.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.IN.InventoryItem.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.IN.InventoryItem.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.IN.InventoryItem.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.InventoryItem.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.IN.InventoryItem.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.IN.InventoryItem.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.InventoryItem.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.IN.InventoryItem.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.IN.InventoryItem.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.IN.InventoryItem.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.IN.InventoryItem.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.IN.InventoryItem.POLineRCollection -> Collection(PX.Objects.PO.POLineR)
PX.Objects.IN.InventoryItem.PMItemRateCollection -> Collection(PX.Objects.PM.PMItemRate)
PX.Objects.IN.InventoryItem.PMProjectARTranPostDetailCollection -> Collection(PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail)
PX.Objects.IN.InventoryItem.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.InventoryItem.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.InventoryItem.INItemLotSerialCollection -> Collection(PX.Objects.IN.INItemLotSerial)
PX.Objects.IN.InventoryItem.INItemSalesHistCollection -> Collection(PX.Objects.IN.INItemSalesHist)
PX.Objects.IN.InventoryItem.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.IN.InventoryItem.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.IN.InventoryItem.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.IN.InventoryItem.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.IN.InventoryItem.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.InventoryItem.INSubItemSegmentValueCollection -> Collection(PX.Objects.IN.INSubItemSegmentValue)
PX.Objects.IN.InventoryItem.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.InventoryItem.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.InventoryItem.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.InventoryItem.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.IN.InventoryItem.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.InventoryItem.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.InventoryItem.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.IN.InventoryItem.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.InventoryItem.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.IN.InventoryItem.RelatedItemCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItem)
PX.Objects.IN.InventoryItem.INItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeader)
PX.Objects.IN.InventoryItem.BCInventoryFileUrlsCollection -> Collection(PX.Commerce.Objects.BCInventoryFileUrls)
PX.Objects.IN.InventoryItem.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.IN.InventoryItem.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.InventoryItem.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.IN.InventoryItem.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.IN.InventoryItem.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.IN.InventoryItem.SchedulerEmployeeInventoryItemCollection -> Collection(PX.Objects.FS.SchedulerEmployeeInventoryItem)
PX.Objects.IN.InventoryItem.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)
PX.Objects.IN.InventoryItem.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.IN.InventoryItem.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.IN.InventoryItem.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.IN.InventoryItem.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.IN.InventoryItemCommon (EntityType)

Label: "Inventory Item Common Fields Only"
Key: InventoryCD
Entity sets: PX_Objects_IN_InventoryItemCommon, InventoryItemCommonFieldsOnly, InventoryItemCommon

PX.Objects.IN.InventoryItemCommon.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.InventoryItemCommon.InventoryCD : Edm.String [key] "Inventory ID"
PX.Objects.IN.InventoryItemCommon.Descr : Edm.String "Description"
PX.Objects.IN.InventoryItemCommon.ItemStatus : Edm.String
PX.Objects.IN.InventoryItemCommon.ItemClassID : Edm.Int32
PX.Objects.IN.InventoryItemCommon.LotSerClassID : Edm.String
PX.Objects.IN.InventoryItemCommon.StkItem : Edm.Boolean
PX.Objects.IN.InventoryItemCommon.IsTemplate : Edm.Boolean
PX.Objects.IN.InventoryItemCommon.NoteID : Edm.Guid
PX.Objects.IN.InventoryItemCommon.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.InventoryItemCommon.INLotSerClassByLotSerClassID -> PX.Objects.IN.INLotSerClass (LotSerClassID=LotSerClassID)
PX.Objects.IN.InventoryItemCommon.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.IN.InventoryItemCommon.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.IN.InventoryItemCommon.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.IN.InventoryItemCommon.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.IN.InventoryItemCommon.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.IN.InventoryItemCommon.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.IN.InventoryItemCommon.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.IN.InventoryItemCommon.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.IN.InventoryItemCommon.FSAppointmentLogExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentLogExtItemLine)
PX.Objects.IN.InventoryItemCommon.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.IN.InventoryItemCommon.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.IN.InventoryItemCommon.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.IN.InventoryItemCommon.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.IN.InventoryItemCommon.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.InventoryItemCommon.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.InventoryItemCommon.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.IN.InventoryItemCommon.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.IN.InventoryItemCommon.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.IN.InventoryItemCommon.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.IN.InventoryItemCommon.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.IN.InventoryItemCommon.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.IN.InventoryItemCommon.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.InventoryItemCommon.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.InventoryItemCommon.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.InventoryItemCommon.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.InventoryItemCommon.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.IN.InventoryItemCommon.INMatrixExcludedDataCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
PX.Objects.IN.InventoryItemCommon.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.IN.InventoryItemCommon.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.Objects.IN.InventoryItemCommon.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.IN.InventoryItemCommon.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.IN.InventoryItemCommon.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.IN.InventoryItemCommon.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.IN.InventoryItemCommon.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.InventoryItemCommon.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.IN.InventoryItemCommon.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.InventoryItemCommon.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.InventoryItemCommon.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.InventoryItemCommon.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.IN.InventoryItemCommon.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.InventoryItemCommon.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.InventoryItemCommon.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.InventoryItemCommon.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.IN.InventoryItemCommon.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.IN.InventoryItemCommon.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.IN.InventoryItemCommon.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.InventoryItemCommon.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.IN.InventoryItemCommon.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.InventoryItemCommon.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.IN.InventoryItemCommon.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.IN.InventoryItemCommon.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.IN.InventoryItemCommon.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.InventoryItemCommon.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.IN.InventoryItemCommon.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.IN.InventoryItemCommon.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.IN.InventoryItemCommon.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.IN.InventoryItemCommon.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.InventoryItemCommon.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.IN.InventoryItemCommon.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.IN.InventoryItemCommon.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.IN.InventoryItemCommon.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.Objects.IN.InventoryItemCommon.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.IN.InventoryItemCommon.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.IN.InventoryItemCommon.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.IN.InventoryItemCommon.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.IN.InventoryItemCommon.InventoryPostingBatchDetailCollection -> Collection(PX.Objects.FS.InventoryPostingBatchDetail)
PX.Objects.IN.InventoryItemCommon.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.IN.InventoryItemCommon.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.InventoryItemCommon.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.InventoryItemCommon.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.InventoryItemCommon.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.InventoryItemCommon.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.InventoryItemCommon.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.IN.InventoryItemCommon.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.InventoryItemCommon.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.InventoryItemCommon.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.InventoryItemCommon.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.InventoryItemCommon.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.InventoryItemCommon.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.IN.InventoryItemCommon.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.IN.InventoryItemCommon.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.Objects.IN.InventoryItemCommon.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.IN.InventoryItemCommon.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.IN.InventoryItemCommon.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.IN.InventoryItemCommon.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.IN.InventoryItemCommon.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.IN.InventoryItemCommon.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.InventoryItemCommon.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.IN.InventoryItemCommon.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.IN.InventoryItemCommon.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.IN.InventoryItemCommon.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.IN.InventoryItemCommon.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.IN.InventoryItemCommon.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.IN.InventoryItemCommon.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.IN.InventoryItemCommon.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.IN.InventoryItemCommon.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.Objects.IN.InventoryItemCommon.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.InventoryItemCommon.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.InventoryItemCommon.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.IN.InventoryItemCommon.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.IN.InventoryItemCommon.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.IN.InventoryItemCommon.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.InventoryItemCommon.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)
PX.Objects.IN.InventoryItemCommon.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.Objects.IN.InventoryItemCommon.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.IN.InventoryItemCommon.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.IN.InventoryItemCommon.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.Objects.IN.InventoryItemCommon.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.IN.InventoryItemCommon.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.IN.InventoryItemCommon.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.IN.InventoryItemCommon.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.Objects.IN.InventoryItemCommon.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.InventoryItemCommon.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.IN.InventoryItemCommon.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.InventoryItemCommon.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.IN.InventoryItemCommon.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.InventoryItemCommon.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.IN.InventoryItemCommon.InventoryItemLotSerNumValCollection -> Collection(PX.Objects.IN.InventoryItemLotSerNumVal)
PX.Objects.IN.InventoryItemCommon.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.IN.InventoryItemCommon.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.IN.InventoryItemCommon.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.IN.InventoryItemCommon.INRelatedInventoryUserFeedbackCollection -> Collection(PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback)
PX.Objects.IN.InventoryItemCommon.INAttributeDescriptionGroupCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup)
PX.Objects.IN.InventoryItemCommon.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.Objects.IN.InventoryItemCommon.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.IN.InventoryItemCommon.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.IN.InventoryItemCommon.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.InventoryItemCommon.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.IN.InventoryItemCommon.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)
PX.Objects.IN.InventoryItemCommon.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.Objects.IN.InventoryItemCommon.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.IN.InventoryItemCommon.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.IN.InventoryItemCommon.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.IN.InventoryItemCommon.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.Objects.IN.InventoryItemCommon.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.IN.InventoryItemCommon.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.IN.InventoryItemCommon.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.IN.InventoryItemCommon.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.IN.InventoryItemCommon.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.IN.InventoryItemCommon.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.IN.InventoryItemCommon.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.Objects.IN.InventoryItemCommon.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.Objects.IN.InventoryItemCommon.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.IN.InventoryItemCommon.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.IN.InventoryItemCommon.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.IN.InventoryItemCommon.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.IN.InventoryItemCommon.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.IN.InventoryItemCommon.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.IN.InventoryItemCommon.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.IN.InventoryItemCommon.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Objects.IN.InventoryItemCommon.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.Objects.IN.InventoryItemCommon.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.IN.InventoryItemCommon.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.IN.InventoryItemCommon.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.InventoryItemCommon.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.InventoryItemCommon.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.InventoryItemCommon.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.IN.InventoryItemCommon.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.IN.InventoryItemCommon.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.IN.InventoryItemCommon.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.IN.InventoryItemCommon.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.IN.InventoryItemCommon.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.IN.InventoryItemCommon.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.InventoryItemCommon.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.Objects.IN.InventoryItemCommon.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.IN.InventoryItemCommon.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.IN.InventoryItemCommon.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.IN.InventoryItemCommon.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.IN.InventoryItemCommon.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.IN.InventoryItemCommon.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.InventoryItemCommon.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.InventoryItemCommon.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.InventoryItemCommon.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.IN.InventoryItemCommon.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.IN.InventoryItemCommon.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.IN.InventoryItemCommon.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.InventoryItemCommon.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.InventoryItemCommon.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.InventoryItemCommon.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.IN.InventoryItemCommon.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.InventoryItemCommon.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.IN.InventoryItemCommon.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.IN.InventoryItemCommon.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.IN.InventoryItemCommon.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.IN.InventoryItemCommon.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.Objects.IN.InventoryItemCommon.FSServiceInventoryItemCollection -> Collection(PX.Objects.FS.FSServiceInventoryItem)
PX.Objects.IN.InventoryItemCommon.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)
PX.Objects.IN.InventoryItemCommon.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)
PX.Objects.IN.InventoryItemCommon.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.Objects.IN.InventoryItemCommon.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)
PX.Objects.IN.InventoryItemCommon.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.InventoryItemCommon.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.IN.InventoryItemCommon.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.IN.InventoryItemCommon.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.IN.InventoryItemCommon.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.IN.InventoryItemCommon.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.IN.InventoryItemCommon.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.IN.InventoryItemCommon.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.IN.InventoryItemCommon.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.IN.InventoryItemCommon.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.IN.InventoryItemCommon.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.IN.InventoryItemCommon.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.InventoryItemCommon.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.IN.InventoryItemCommon.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.IN.InventoryItemCommon.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.IN.InventoryItemCommon.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.IN.InventoryItemCommon.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.InventoryItemCommon.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.IN.InventoryItemCommon.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.IN.InventoryItemCommon.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.IN.InventoryItemCommon.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.IN.InventoryItemCommon.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.IN.InventoryItemCommon.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.IN.InventoryItemCommon.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.IN.InventoryItemCommon.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.IN.InventoryItemCommon.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.IN.InventoryItemCommon.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.IN.InventoryItemCommon.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.IN.InventoryItemCommon.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.IN.InventoryItemCommon.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.IN.InventoryItemCommon.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.InventoryItemCommon.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.IN.InventoryItemCommon.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.IN.InventoryItemCommon.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.InventoryItemCommon.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.IN.InventoryItemCommon.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.IN.InventoryItemCommon.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.IN.InventoryItemCommon.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.IN.InventoryItemCommon.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.IN.InventoryItemCommon.POLineRCollection -> Collection(PX.Objects.PO.POLineR)
PX.Objects.IN.InventoryItemCommon.PMItemRateCollection -> Collection(PX.Objects.PM.PMItemRate)
PX.Objects.IN.InventoryItemCommon.PMProjectARTranPostDetailCollection -> Collection(PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail)
PX.Objects.IN.InventoryItemCommon.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.InventoryItemCommon.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.InventoryItemCommon.INItemLotSerialCollection -> Collection(PX.Objects.IN.INItemLotSerial)
PX.Objects.IN.InventoryItemCommon.INItemSalesHistCollection -> Collection(PX.Objects.IN.INItemSalesHist)
PX.Objects.IN.InventoryItemCommon.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.IN.InventoryItemCommon.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.IN.InventoryItemCommon.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.IN.InventoryItemCommon.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.IN.InventoryItemCommon.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.InventoryItemCommon.INSubItemSegmentValueCollection -> Collection(PX.Objects.IN.INSubItemSegmentValue)
PX.Objects.IN.InventoryItemCommon.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.InventoryItemCommon.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.InventoryItemCommon.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.InventoryItemCommon.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.IN.InventoryItemCommon.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.InventoryItemCommon.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.InventoryItemCommon.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.IN.InventoryItemCommon.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.InventoryItemCommon.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.IN.InventoryItemCommon.RelatedItemCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItem)
PX.Objects.IN.InventoryItemCommon.INItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeader)
PX.Objects.IN.InventoryItemCommon.BCInventoryFileUrlsCollection -> Collection(PX.Commerce.Objects.BCInventoryFileUrls)
PX.Objects.IN.InventoryItemCommon.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.IN.InventoryItemCommon.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.InventoryItemCommon.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.IN.InventoryItemCommon.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.IN.InventoryItemCommon.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.IN.InventoryItemCommon.SchedulerEmployeeInventoryItemCollection -> Collection(PX.Objects.FS.SchedulerEmployeeInventoryItem)
PX.Objects.IN.InventoryItemCommon.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)
PX.Objects.IN.InventoryItemCommon.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.IN.InventoryItemCommon.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.IN.InventoryItemCommon.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.IN.InventoryItemCommon.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.IN.InventoryItemCurySettings (EntityType)

Label: "Inventory Item Currency Settings"
Key: CuryID, InventoryID
Entity sets: PX_Objects_IN_InventoryItemCurySettings, InventoryItemCurrencySettings, InventoryItemCurySettings

PX.Objects.IN.InventoryItemCurySettings.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.InventoryItemCurySettings.CuryID : Edm.String [key] "Currency"
PX.Objects.IN.InventoryItemCurySettings.LastStdCost : Edm.Decimal [required] "Last Cost"
PX.Objects.IN.InventoryItemCurySettings.PendingStdCost : Edm.Decimal [required] "Pending Cost"
PX.Objects.IN.InventoryItemCurySettings.PendingStdCostDate : Edm.DateTimeOffset "Pending Cost Date"
PX.Objects.IN.InventoryItemCurySettings.StdCost : Edm.Decimal [required] "Current Cost"
PX.Objects.IN.InventoryItemCurySettings.StdCostDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.IN.InventoryItemCurySettings.BasePrice : Edm.Decimal [required] "Default Price"
PX.Objects.IN.InventoryItemCurySettings.RecPrice : Edm.Decimal "MSRP"
PX.Objects.IN.InventoryItemCurySettings.PreferredVendorID : Edm.Int32 "Preferred Vendor"
PX.Objects.IN.InventoryItemCurySettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.InventoryItemCurySettings.CreatedByScreenID : Edm.String
PX.Objects.IN.InventoryItemCurySettings.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.InventoryItemCurySettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.InventoryItemCurySettings.LastModifiedByScreenID : Edm.String
PX.Objects.IN.InventoryItemCurySettings.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.IN.InventoryItemCurySettings.tstamp : Edm.Binary
PX.Objects.IN.InventoryItemCurySettings.VendorByPreferredVendorID -> PX.Objects.AP.Vendor (PreferredVendorID=BAccountID)
PX.Objects.IN.InventoryItemCurySettings.BAccountByPreferredVendorID -> PX.Objects.CR.BAccount (PreferredVendorID=BAccountID)
PX.Objects.IN.InventoryItemCurySettings.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.InventoryItemCurySettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.InventoryItemCurySettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.InventoryItemCurySettings.INLocationByDfltShipLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.InventoryItemCurySettings.INLocationByDfltReceiptLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.InventoryItemCurySettings.INLocationByDfltPutawayLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.InventoryItemCurySettings.INLocationByDfltSiteID -> PX.Objects.IN.INLocation
PX.Objects.IN.InventoryItemCurySettings.INSiteByDfltSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.InventoryItemCurySettings.INSitePlanningStrategyByPlanningStrategyID -> PX.Objects.IN.DAC.INSitePlanningStrategy
PX.Objects.IN.InventoryItemCurySettings.INSitePlanningStrategyByDfltSiteID -> PX.Objects.IN.DAC.INSitePlanningStrategy
PX.Objects.IN.InventoryItemCurySettings.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.IN.InventoryItemCurySettings.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.IN.InventoryItemCurySettings.LocationByPreferredVendorLocationID -> PX.Objects.CR.Location (PreferredVendorID=BAccountID)
PX.Objects.IN.InventoryItemCurySettings.LocationByPreferredVendorID -> PX.Objects.CR.Location (PreferredVendorID=BAccountID)
PX.Objects.IN.InventoryItemCurySettings.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)

# PX.Objects.IN.InventoryItemLotSerNumVal (EntityType)

Label: "Auto-Incremental Value of a Stock Item"
Key: InventoryID
Entity sets: PX_Objects_IN_InventoryItemLotSerNumVal, AutoIncrementalValueofaStockItem, InventoryItemLotSerNumVal

PX.Objects.IN.InventoryItemLotSerNumVal.InventoryID : Edm.Int32 [key]
PX.Objects.IN.InventoryItemLotSerNumVal.LotSerNumVal : Edm.String "Auto-Incremental Value"
PX.Objects.IN.InventoryItemLotSerNumVal.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.InventoryItemLotSerNumVal.CreatedByScreenID : Edm.String
PX.Objects.IN.InventoryItemLotSerNumVal.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.IN.InventoryItemLotSerNumVal.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.InventoryItemLotSerNumVal.LastModifiedByScreenID : Edm.String
PX.Objects.IN.InventoryItemLotSerNumVal.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.InventoryItemLotSerNumVal.tstamp : Edm.Binary
PX.Objects.IN.InventoryItemLotSerNumVal.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.InventoryItemLotSerNumVal.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.InventoryItemLotSerNumVal.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.IN.InventoryTranSumEnqResult (ComplexType)


PX.Objects.IN.InventoryTranSumEnqResult.InventoryID : Edm.Int32
PX.Objects.IN.InventoryTranSumEnqResult.SubItemID : Edm.Int32
PX.Objects.IN.InventoryTranSumEnqResult.SiteID : Edm.Int32
PX.Objects.IN.InventoryTranSumEnqResult.LocationID : Edm.Int32
PX.Objects.IN.InventoryTranSumEnqResult.LastActivityPeriod : Edm.String
PX.Objects.IN.InventoryTranSumEnqResult.FinPeriodID : Edm.String
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyIssued : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyReceived : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinBegQty : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinYtdQty : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtySales : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyCreditMemos : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyDropShipSales : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyTransferIn : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyTransferOut : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyAssemblyIn : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyAssemblyOut : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.FinPtdQtyAdjusted : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyReceived : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyIssued : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtySales : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyCreditMemos : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyDropShipSales : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyTransferIn : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyTransferOut : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyAssemblyIn : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyAssemblyOut : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranPtdQtyAdjusted : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranBegQty : Edm.Decimal
PX.Objects.IN.InventoryTranSumEnqResult.TranYtdQty : Edm.Decimal

# PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup (EntityType)

Label: "Attribute Description Group"
Key: GroupID, TemplateID
Entity sets: PX_Objects_IN_Matrix_DAC_INAttributeDescriptionGroup, AttributeDescriptionGroup, INAttributeDescriptionGroup

PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.TemplateID : Edm.Int32 [key] "Template ID"
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.GroupID : Edm.Int32 [key]
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.Description : Edm.String
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.CreatedByScreenID : Edm.String
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.LastModifiedByScreenID : Edm.String
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.tstamp : Edm.Binary
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.InventoryItemByTemplateID -> PX.Objects.IN.InventoryItem (TemplateID=InventoryID)
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)

# PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem (EntityType)

Label: "Attribute Description Item"
Key: AttributeID, GroupID, TemplateID
Entity sets: PX_Objects_IN_Matrix_DAC_INAttributeDescriptionItem, AttributeDescriptionItem, INAttributeDescriptionItem

PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.TemplateID : Edm.Int32 [key] "Template ID"
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.GroupID : Edm.Int32 [key]
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.AttributeID : Edm.String [key]
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.ValueID : Edm.String
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.CreatedByScreenID : Edm.String
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.LastModifiedByScreenID : Edm.String
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.tstamp : Edm.Binary
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.InventoryItemByTemplateID -> PX.Objects.IN.InventoryItem (TemplateID=InventoryID)
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem.INAttributeDescriptionGroupByGroupID -> PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup (TemplateID=TemplateID, GroupID=GroupID)

# PX.Objects.IN.Matrix.DAC.INMatrixExcludedData (EntityType)

Label: "Data Excluded From Update of Matrix Items"
Key: FieldName, TableName, TemplateID, Type
Entity sets: PX_Objects_IN_Matrix_DAC_INMatrixExcludedData, DataExcludedFromUpdateofMatrixItems, INMatrixExcludedData
Non-filterable, non-selectable: NoteText

PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.Type : Edm.String [key]
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.TableName : Edm.String [key] "Table Name"
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.FieldName : Edm.String [key] "Field Name"
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.TemplateID : Edm.Int32 [key]
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.IsActive : Edm.Boolean [required] "Active"
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.NoteID : Edm.Guid
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.NoteText : Edm.String "Note Text"
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.CreatedByScreenID : Edm.String
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.LastModifiedByScreenID : Edm.String
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.tstamp : Edm.Binary
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.InventoryItemByTemplateID -> PX.Objects.IN.InventoryItem (TemplateID=InventoryID)
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.Matrix.DAC.INMatrixExcludedData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule (EntityType)

Label: "Matrix Generation Rule"
Key: LineNbr, ParentID, ParentType, Type
Entity sets: PX_Objects_IN_Matrix_DAC_INMatrixGenerationRule, MatrixGenerationRule, INMatrixGenerationRule

PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.ParentID : Edm.Int32 [key]
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.ParentType : Edm.String [key required]
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.Type : Edm.String [key]
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.SegmentType : Edm.String "Segment Type"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.AttributeID : Edm.String "Attribute ID"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.Constant : Edm.String "Constant"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.NumberingID : Edm.String "Numbering ID"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.NumberOfCharacters : Edm.Int32 "Number of Characters"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.UseSpaceAsSeparator : Edm.Boolean [required] "Use Space as Separator"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.Separator : Edm.String "Separator"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.SortOrder : Edm.Int32 "Line Order"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.AddSpaces : Edm.Boolean "Add Spaces"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.CreatedByScreenID : Edm.String
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.LastModifiedByScreenID : Edm.String
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.tstamp : Edm.Binary
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.InventoryItemByParentID -> PX.Objects.IN.InventoryItem (ParentID=InventoryID)
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.NumberingByNumberingID -> PX.Objects.CS.Numbering (NumberingID=NumberingID)
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.INItemClassByParentID -> PX.Objects.IN.INItemClass (ParentID=ItemClassID)
PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule.CSAnswersByAttributeID -> PX.Objects.CS.CSAnswers (AttributeID=AttributeID)

# PX.Objects.IN.Matrix.DAC.Projections.DescriptionGenerationRule (EntityType)

Label: "Description Generation Rule"
BaseType: PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule
Key: LineNbr, ParentID, ParentType, Type (inherited from PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
Entity sets: PX_Objects_IN_Matrix_DAC_Projections_DescriptionGenerationRule, DescriptionGenerationRule

# PX.Objects.IN.Matrix.DAC.Projections.ExcludedAttribute (EntityType)

Label: "Attribute Excluded From Update of Matrix Items"
BaseType: PX.Objects.IN.Matrix.DAC.INMatrixExcludedData
Key: FieldName, TableName, TemplateID, Type (inherited from PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
Entity sets: PX_Objects_IN_Matrix_DAC_Projections_ExcludedAttribute, AttributeExcludedFromUpdateofMatrixItems, ExcludedAttribute

# PX.Objects.IN.Matrix.DAC.Projections.ExcludedField (EntityType)

Label: "Field Excluded From Update of Matrix Items"
BaseType: PX.Objects.IN.Matrix.DAC.INMatrixExcludedData
Key: FieldName, TableName, TemplateID, Type (inherited from PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
Entity sets: PX_Objects_IN_Matrix_DAC_Projections_ExcludedField, FieldExcludedFromUpdateofMatrixItems, ExcludedField

# PX.Objects.IN.Matrix.DAC.Projections.IDGenerationRule (EntityType)

Label: "ID Generation Rule"
BaseType: PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule
Key: LineNbr, ParentID, ParentType, Type (inherited from PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
Entity sets: PX_Objects_IN_Matrix_DAC_Projections_IDGenerationRule, IDGenerationRule

# PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem (EntityType)

Label: "Inventory Item with Attribute Values"
BaseType: PX.Objects.IN.InventoryItem
Key: InventoryCD (inherited from PX.Objects.IN.InventoryItem)
Entity sets: PX_Objects_IN_Matrix_DAC_Unbound_MatrixInventoryItem, InventoryItemwithAttributeValues, MatrixInventoryItem
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem.Exists : Edm.Boolean
PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem.New : Edm.Boolean "New"
PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem.Duplicate : Edm.Boolean
PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem.UOM : Edm.String "UOM"
PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem.UOMDisabled : Edm.Boolean
PX.Objects.IN.Matrix.DAC.Unbound.MatrixInventoryItem.Qty : Edm.Decimal "Quantity"

# PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback (EntityType)

Label: "Related Item ML Feedback"
Key: InventoryID, RelatedInventoryID
Entity sets: PX_Objects_IN_RelatedItems_DAC_INRelatedInventoryUserFeedback, RelatedItemMLFeedback, INRelatedInventoryUserFeedback

PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.InventoryID : Edm.Int32 [key]
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.RelatedInventoryID : Edm.Int32 [key]
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.IsCrossSell : Edm.Boolean
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.CreatedByScreenID : Edm.String
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.LastModifiedByScreenID : Edm.String
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.tstamp : Edm.Binary
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.InventoryItemByRelatedInventoryID -> PX.Objects.IN.InventoryItem (RelatedInventoryID=InventoryID)
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.IN.RelatedItems.INRelatedInventory (EntityType)

Label: "Related Item"
Key: InventoryID, LineID
Entity sets: PX_Objects_IN_RelatedItems_INRelatedInventory, RelatedItem, INRelatedInventory
Non-filterable, non-selectable: Desc, NoteText, NotePopupText

PX.Objects.IN.RelatedItems.INRelatedInventory.InventoryID : Edm.Int32 [key]
PX.Objects.IN.RelatedItems.INRelatedInventory.LineID : Edm.Int32 [key]
PX.Objects.IN.RelatedItems.INRelatedInventory.Relation : Edm.String "Relation"
PX.Objects.IN.RelatedItems.INRelatedInventory.Rank : Edm.Int32 "Rank"
PX.Objects.IN.RelatedItems.INRelatedInventory.Tag : Edm.String "Tag"
PX.Objects.IN.RelatedItems.INRelatedInventory.RelatedInventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.RelatedItems.INRelatedInventory.Desc : Edm.String "Description"
PX.Objects.IN.RelatedItems.INRelatedInventory.UOM : Edm.String "UOM"
PX.Objects.IN.RelatedItems.INRelatedInventory.Qty : Edm.Decimal "Quantity"
PX.Objects.IN.RelatedItems.INRelatedInventory.BaseQty : Edm.Decimal [required]
PX.Objects.IN.RelatedItems.INRelatedInventory.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.IN.RelatedItems.INRelatedInventory.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.IN.RelatedItems.INRelatedInventory.Interchangeable : Edm.Boolean [required] "Customer Approval Not Needed"
PX.Objects.IN.RelatedItems.INRelatedInventory.Required : Edm.Boolean [required] "Required"
PX.Objects.IN.RelatedItems.INRelatedInventory.IsActive : Edm.Boolean [required] "Active"
PX.Objects.IN.RelatedItems.INRelatedInventory.CreatedByPossibleRelatedItem : Edm.Boolean [required]
PX.Objects.IN.RelatedItems.INRelatedInventory.MLScore : Edm.Decimal
PX.Objects.IN.RelatedItems.INRelatedInventory.NoteID : Edm.Guid
PX.Objects.IN.RelatedItems.INRelatedInventory.NoteText : Edm.String "Note Text"
PX.Objects.IN.RelatedItems.INRelatedInventory.NotePopupText : Edm.String "Note Text"
PX.Objects.IN.RelatedItems.INRelatedInventory.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.RelatedItems.INRelatedInventory.CreatedByScreenID : Edm.String
PX.Objects.IN.RelatedItems.INRelatedInventory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.RelatedItems.INRelatedInventory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.RelatedItems.INRelatedInventory.LastModifiedByScreenID : Edm.String
PX.Objects.IN.RelatedItems.INRelatedInventory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.RelatedItems.INRelatedInventory.tstamp : Edm.Binary
PX.Objects.IN.RelatedItems.INRelatedInventory.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.RelatedItems.INRelatedInventory.InventoryItemByRelatedInventoryID -> PX.Objects.IN.InventoryItem (RelatedInventoryID=InventoryID)
PX.Objects.IN.RelatedItems.INRelatedInventory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.RelatedItems.INRelatedInventory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.RelatedItems.INRelatedInventory.INUnitByRelatedInventoryID -> PX.Objects.IN.INUnit (RelatedInventoryID=InventoryID)

# PX.Objects.IN.RelatedItems.RelatedItem (EntityType)

Label: "Related Item"
Key: InventoryID, LineID
Entity sets: PX_Objects_IN_RelatedItems_RelatedItem, RelatedItem1
Non-filterable, non-selectable: Desc, QtySelected, CuryUnitPrice, CuryExtPrice, PriceDiff

PX.Objects.IN.RelatedItems.RelatedItem.InventoryID : Edm.Int32 [key]
PX.Objects.IN.RelatedItems.RelatedItem.LineID : Edm.Int32 [key]
PX.Objects.IN.RelatedItems.RelatedItem.RelatedInventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.RelatedItems.RelatedItem.Desc : Edm.String "Description"
PX.Objects.IN.RelatedItems.RelatedItem.Relation : Edm.String "Relation"
PX.Objects.IN.RelatedItems.RelatedItem.Rank : Edm.Int32 "Rank"
PX.Objects.IN.RelatedItems.RelatedItem.Tag : Edm.String "Tag"
PX.Objects.IN.RelatedItems.RelatedItem.UOM : Edm.String "UOM"
PX.Objects.IN.RelatedItems.RelatedItem.Qty : Edm.Decimal
PX.Objects.IN.RelatedItems.RelatedItem.BaseQty : Edm.Decimal
PX.Objects.IN.RelatedItems.RelatedItem.Interchangeable : Edm.Boolean "Customer Approval Not Needed"
PX.Objects.IN.RelatedItems.RelatedItem.Required : Edm.Boolean "Required"
PX.Objects.IN.RelatedItems.RelatedItem.NoteID : Edm.Guid
PX.Objects.IN.RelatedItems.RelatedItem.SubItemCD : Edm.String
PX.Objects.IN.RelatedItems.RelatedItem.SiteCD : Edm.String
PX.Objects.IN.RelatedItems.RelatedItem.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.IN.RelatedItems.RelatedItem.BaseAvailableQty : Edm.Decimal
PX.Objects.IN.RelatedItems.RelatedItem.StkItem : Edm.Boolean
PX.Objects.IN.RelatedItems.RelatedItem.AvailableQty : Edm.Decimal "Qty. Available"
PX.Objects.IN.RelatedItems.RelatedItem.CuryUnitPrice : Edm.Decimal "Unit Price"
PX.Objects.IN.RelatedItems.RelatedItem.CuryExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.IN.RelatedItems.RelatedItem.PriceDiff : Edm.Decimal "Ext. Price Difference"
PX.Objects.IN.RelatedItems.RelatedItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.RelatedItems.RelatedItem.InventoryItemByRelatedInventoryID -> PX.Objects.IN.InventoryItem (RelatedInventoryID=InventoryID)
PX.Objects.IN.RelatedItems.RelatedItem.INSubItemBySubItemID -> PX.Objects.IN.INSubItem

# PX.Objects.IN.RelatedItems.RelatedItemHistory (EntityType)

Label: "Related Item History"
Key: LineID
Entity sets: PX_Objects_IN_RelatedItems_RelatedItemHistory, RelatedItemHistory
Non-filterable, non-selectable: OriginalInventoryDesc, RelatedInventoryDesc

PX.Objects.IN.RelatedItems.RelatedItemHistory.LineID : Edm.Int32 [key]
PX.Objects.IN.RelatedItems.RelatedItemHistory.IsDraft : Edm.Boolean [required]
PX.Objects.IN.RelatedItems.RelatedItemHistory.OriginalInventoryID : Edm.Int32 "Original Item ID"
PX.Objects.IN.RelatedItems.RelatedItemHistory.OriginalInventoryDesc : Edm.String "Original Item Description"
PX.Objects.IN.RelatedItems.RelatedItemHistory.OriginalInventoryUOM : Edm.String "Original Item UOM"
PX.Objects.IN.RelatedItems.RelatedItemHistory.OriginalInventoryQty : Edm.Decimal "Original Item Qty."
PX.Objects.IN.RelatedItems.RelatedItemHistory.RelatedInventoryID : Edm.Int32 "Related Item ID"
PX.Objects.IN.RelatedItems.RelatedItemHistory.RelatedInventoryDesc : Edm.String "Related Item Description"
PX.Objects.IN.RelatedItems.RelatedItemHistory.RelatedInventoryUOM : Edm.String "Related Item UOM"
PX.Objects.IN.RelatedItems.RelatedItemHistory.RelatedInventoryQty : Edm.Decimal "Related Item Qty."
PX.Objects.IN.RelatedItems.RelatedItemHistory.SoldQty : Edm.Decimal "Qty. Sold"
PX.Objects.IN.RelatedItems.RelatedItemHistory.Relation : Edm.String "Relation"
PX.Objects.IN.RelatedItems.RelatedItemHistory.Tag : Edm.String "Tag"
PX.Objects.IN.RelatedItems.RelatedItemHistory.DocumentDate : Edm.DateTimeOffset "Document Date"
PX.Objects.IN.RelatedItems.RelatedItemHistory.OrderType : Edm.String
PX.Objects.IN.RelatedItems.RelatedItemHistory.OrderNbr : Edm.String "Order Nbr."
PX.Objects.IN.RelatedItems.RelatedItemHistory.OriginalOrderLineNbr : Edm.Int32
PX.Objects.IN.RelatedItems.RelatedItemHistory.RelatedOrderLineNbr : Edm.Int32
PX.Objects.IN.RelatedItems.RelatedItemHistory.OpportunityID : Edm.String "Opportunity Nbr."
PX.Objects.IN.RelatedItems.RelatedItemHistory.DefQuoteID : Edm.Guid
PX.Objects.IN.RelatedItems.RelatedItemHistory.OriginalOpportunityLineNbr : Edm.Int32
PX.Objects.IN.RelatedItems.RelatedItemHistory.RelatedOpportunityLineNbr : Edm.Int32
PX.Objects.IN.RelatedItems.RelatedItemHistory.QuoteID : Edm.Guid
PX.Objects.IN.RelatedItems.RelatedItemHistory.QuoteNbr : Edm.String "Quote Nbr."
PX.Objects.IN.RelatedItems.RelatedItemHistory.OriginalQuoteLineNbr : Edm.Int32
PX.Objects.IN.RelatedItems.RelatedItemHistory.RelatedQuoteLineNbr : Edm.Int32
PX.Objects.IN.RelatedItems.RelatedItemHistory.InvoiceDocType : Edm.String
PX.Objects.IN.RelatedItems.RelatedItemHistory.InvoiceRefNbr : Edm.String "Invoice Nbr."
PX.Objects.IN.RelatedItems.RelatedItemHistory.OriginalInvoiceLineNbr : Edm.Int32
PX.Objects.IN.RelatedItems.RelatedItemHistory.RelatedInvoiceLineNbr : Edm.Int32
PX.Objects.IN.RelatedItems.RelatedItemHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.RelatedItems.RelatedItemHistory.CreatedByScreenID : Edm.String
PX.Objects.IN.RelatedItems.RelatedItemHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.RelatedItems.RelatedItemHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.RelatedItems.RelatedItemHistory.LastModifiedByScreenID : Edm.String
PX.Objects.IN.RelatedItems.RelatedItemHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.RelatedItems.RelatedItemHistory.tstamp : Edm.Binary
PX.Objects.IN.RelatedItems.RelatedItemHistory.ARInvoiceByInvoiceRefNbr -> PX.Objects.AR.ARInvoice (InvoiceDocType=DocType, InvoiceRefNbr=RefNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.InventoryItemByOriginalInventoryID -> PX.Objects.IN.InventoryItem (OriginalInventoryID=InventoryID)
PX.Objects.IN.RelatedItems.RelatedItemHistory.InventoryItemByRelatedInventoryID -> PX.Objects.IN.InventoryItem (RelatedInventoryID=InventoryID)
PX.Objects.IN.RelatedItems.RelatedItemHistory.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.SOOrderByOrderType -> PX.Objects.SO.SOOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.IN.RelatedItems.RelatedItemHistory.CROpportunityProductsByOriginalOpportunityLineNbr -> PX.Objects.CR.CROpportunityProducts (DefQuoteID=QuoteID, OriginalOpportunityLineNbr=LineNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.CROpportunityProductsByRelatedOpportunityLineNbr -> PX.Objects.CR.CROpportunityProducts (DefQuoteID=QuoteID, RelatedOpportunityLineNbr=LineNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.CROpportunityProductsByOriginalQuoteLineNbr -> PX.Objects.CR.CROpportunityProducts (QuoteID=QuoteID, OriginalQuoteLineNbr=LineNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.CROpportunityProductsByRelatedQuoteLineNbr -> PX.Objects.CR.CROpportunityProducts (QuoteID=QuoteID, RelatedQuoteLineNbr=LineNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.RelatedItems.RelatedItemHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.RelatedItems.RelatedItemHistory.SOLineByOriginalOrderLineNbr -> PX.Objects.SO.SOLine (OrderType=OrderType, OrderNbr=OrderNbr, OriginalOrderLineNbr=LineNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.SOLineByRelatedOrderLineNbr -> PX.Objects.SO.SOLine (OrderType=OrderType, OrderNbr=OrderNbr, RelatedOrderLineNbr=LineNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.INUnitByOriginalInventoryID -> PX.Objects.IN.INUnit (OriginalInventoryUOM=FromUnit, OriginalInventoryID=InventoryID)
PX.Objects.IN.RelatedItems.RelatedItemHistory.INUnitByRelatedInventoryID -> PX.Objects.IN.INUnit (RelatedInventoryUOM=FromUnit, RelatedInventoryID=InventoryID)
PX.Objects.IN.RelatedItems.RelatedItemHistory.ARTranByOriginalInvoiceLineNbr -> PX.Objects.AR.ARTran (InvoiceDocType=TranType, InvoiceRefNbr=RefNbr, OriginalInvoiceLineNbr=LineNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.ARTranByRelatedInvoiceLineNbr -> PX.Objects.AR.ARTran (InvoiceDocType=TranType, InvoiceRefNbr=RefNbr, RelatedInvoiceLineNbr=LineNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.CROpportunityByOpportunityID -> PX.Objects.CR.CROpportunity (OpportunityID=OpportunityID)
PX.Objects.IN.RelatedItems.RelatedItemHistory.CRQuoteByQuoteNbr -> PX.Objects.CR.CRQuote (QuoteNbr=QuoteNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.SOInvoiceByInvoiceRefNbr -> PX.Objects.SO.SOInvoice (InvoiceDocType=DocType, InvoiceRefNbr=RefNbr)
PX.Objects.IN.RelatedItems.RelatedItemHistory.SOInvoiceByInvoiceDocType -> PX.Objects.SO.SOInvoice (InvoiceRefNbr=RefNbr, InvoiceDocType=DocType)

# PX.Objects.IN.S.INItemSite (EntityType)

Key: InventoryID, SiteID
Entity sets: PX_Objects_IN_S_INItemSite
Non-filterable, non-selectable: IsDefault, NoteText

PX.Objects.IN.S.INItemSite.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.S.INItemSite.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.S.INItemSite.SiteStatus : Edm.String "Status"
PX.Objects.IN.S.INItemSite.ValMethod : Edm.String
PX.Objects.IN.S.INItemSite.DfltSalesUnit : Edm.String "Sales Unit"
PX.Objects.IN.S.INItemSite.DfltPurchaseUnit : Edm.String "Purchase Unit"
PX.Objects.IN.S.INItemSite.LastStdCost : Edm.Decimal [required] "Last Cost"
PX.Objects.IN.S.INItemSite.PendingStdCost : Edm.Decimal [required] "Pending Cost"
PX.Objects.IN.S.INItemSite.PendingStdCostDate : Edm.DateTimeOffset "Pending Cost Date"
PX.Objects.IN.S.INItemSite.StdCost : Edm.Decimal [required] "Current Cost"
PX.Objects.IN.S.INItemSite.StdCostDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.IN.S.INItemSite.LastBasePrice : Edm.Decimal [required] "Last Price"
PX.Objects.IN.S.INItemSite.PendingBasePrice : Edm.Decimal [required] "Pending Price"
PX.Objects.IN.S.INItemSite.PendingBasePriceDate : Edm.DateTimeOffset "Pending Price Date"
PX.Objects.IN.S.INItemSite.BasePrice : Edm.Decimal [required] "Current Price"
PX.Objects.IN.S.INItemSite.BasePriceDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.IN.S.INItemSite.PreferredVendorOverride : Edm.Boolean [required] "Preferred Vendor Override"
PX.Objects.IN.S.INItemSite.PreferredVendorID : Edm.Int32 "Preferred Vendor"
PX.Objects.IN.S.INItemSite.ProductWorkgroupID : Edm.Int32 "Product Workgroup"
PX.Objects.IN.S.INItemSite.ProductManagerID : Edm.Int32 "Product Manager"
PX.Objects.IN.S.INItemSite.PriceWorkgroupID : Edm.Int32 "Price Workgroup"
PX.Objects.IN.S.INItemSite.PriceManagerID : Edm.Int32 "Price Manager"
PX.Objects.IN.S.INItemSite.IsDefault : Edm.Boolean "Default"
PX.Objects.IN.S.INItemSite.StdCostOverride : Edm.Boolean [required] "Std. Cost Override"
PX.Objects.IN.S.INItemSite.BasePriceOverride : Edm.Boolean [required] "Price Override"
PX.Objects.IN.S.INItemSite.Commissionable : Edm.Boolean [required] "Subject to Commission"
PX.Objects.IN.S.INItemSite.ABCCodeID : Edm.String "ABC Code"
PX.Objects.IN.S.INItemSite.ABCCodeIsFixed : Edm.Boolean [required] "Fixed ABC Code"
PX.Objects.IN.S.INItemSite.MovementClassID : Edm.String "Movement Class"
PX.Objects.IN.S.INItemSite.MovementClassIsFixed : Edm.Boolean [required] "Fixed Movement Class"
PX.Objects.IN.S.INItemSite.NoteID : Edm.Guid
PX.Objects.IN.S.INItemSite.NoteText : Edm.String "Note Text"
PX.Objects.IN.S.INItemSite.POCreate : Edm.Boolean
PX.Objects.IN.S.INItemSite.MarkupPct : Edm.Decimal "Markup %"
PX.Objects.IN.S.INItemSite.MarkupPctOverride : Edm.Boolean [required] "Markup % Override"
PX.Objects.IN.S.INItemSite.RecPrice : Edm.Decimal "MSRP"
PX.Objects.IN.S.INItemSite.RecPriceOverride : Edm.Boolean [required] "Price Override"
PX.Objects.IN.S.INItemSite.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.S.INItemSite.CreatedByScreenID : Edm.String
PX.Objects.IN.S.INItemSite.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.S.INItemSite.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.S.INItemSite.LastModifiedByScreenID : Edm.String
PX.Objects.IN.S.INItemSite.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.S.INItemSite.ReplenishmentPolicyOverride : Edm.Boolean [required] "Replenishment Policy Override"
PX.Objects.IN.S.INItemSite.ReplenishmentPolicyID : Edm.String "Seasonality"
PX.Objects.IN.S.INItemSite.ReplenishmentSource : Edm.String "Replenishment Source"
PX.Objects.IN.S.INItemSite.ReplenishmentMethod : Edm.String "Replenishment Method"
PX.Objects.IN.S.INItemSite.MaxShelfLifeOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.S.INItemSite.MaxShelfLife : Edm.Int32 "Max. Shelf Life (Days)"
PX.Objects.IN.S.INItemSite.LaunchDateOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.S.INItemSite.LaunchDate : Edm.DateTimeOffset "Launch Date"
PX.Objects.IN.S.INItemSite.TerminationDateOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.S.INItemSite.TerminationDate : Edm.DateTimeOffset "Termination Date"
PX.Objects.IN.S.INItemSite.SafetyStockOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.S.INItemSite.SafetyStock : Edm.Decimal "Safety Stock"
PX.Objects.IN.S.INItemSite.MinQtyOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.S.INItemSite.MinQty : Edm.Decimal "Reorder Point"
PX.Objects.IN.S.INItemSite.MaxQtyOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.S.INItemSite.MaxQty : Edm.Decimal "Max Qty."
PX.Objects.IN.S.INItemSite.TransferERQOverride : Edm.Boolean [required] "Override"
PX.Objects.IN.S.INItemSite.TransferERQ : Edm.Decimal "Transfer ERQ"
PX.Objects.IN.S.INItemSite.tstamp : Edm.Binary
PX.Objects.IN.S.INItemSite.EPEmployeeByProductManagerID -> PX.Objects.EP.EPEmployee (ProductManagerID=BAccountID)
PX.Objects.IN.S.INItemSite.EPEmployeeByPriceManagerID -> PX.Objects.EP.EPEmployee (PriceManagerID=BAccountID)
PX.Objects.IN.S.INItemSite.VendorByPreferredVendorID -> PX.Objects.AP.Vendor (PreferredVendorID=BAccountID)
PX.Objects.IN.S.INItemSite.BAccountByPreferredVendorID -> PX.Objects.CR.BAccount (PreferredVendorID=BAccountID)
PX.Objects.IN.S.INItemSite.ContactByProductManagerID -> PX.Objects.CR.Contact (ProductManagerID=ContactID)
PX.Objects.IN.S.INItemSite.ContactByPriceManagerID -> PX.Objects.CR.Contact (PriceManagerID=ContactID)
PX.Objects.IN.S.INItemSite.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.S.INItemSite.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.S.INItemSite.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.S.INItemSite.EPCompanyTreeByProductWorkgroupID -> PX.TM.EPCompanyTree (ProductWorkgroupID=WorkGroupID)
PX.Objects.IN.S.INItemSite.EPCompanyTreeByPriceWorkgroupID -> PX.TM.EPCompanyTree (PriceWorkgroupID=WorkGroupID)
PX.Objects.IN.S.INItemSite.CountryByCountryOfOrigin -> PX.Objects.CS.Country
PX.Objects.IN.S.INItemSite.INABCCodeByABCCodeID -> PX.Objects.IN.INABCCode (ABCCodeID=ABCCodeID)
PX.Objects.IN.S.INItemSite.INLocationByDfltShipLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.S.INItemSite.INLocationByDfltReceiptLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.S.INItemSite.INLocationByDfltPutawayLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.S.INItemSite.INLocationBySiteID -> PX.Objects.IN.INLocation (SiteID=SiteID)
PX.Objects.IN.S.INItemSite.INMovementClassByMovementClassID -> PX.Objects.IN.INMovementClass (MovementClassID=MovementClassID)
PX.Objects.IN.S.INItemSite.INMovementClassByPendingMovementClassID -> PX.Objects.IN.INMovementClass
PX.Objects.IN.S.INItemSite.INReplenishmentClassByReplenishmentClassID -> PX.Objects.IN.INReplenishmentClass
PX.Objects.IN.S.INItemSite.INReplenishmentPolicyByReplenishmentPolicyID -> PX.Objects.IN.INReplenishmentPolicy (ReplenishmentPolicyID=ReplenishmentPolicyID)
PX.Objects.IN.S.INItemSite.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.S.INItemSite.INSiteByReplenishmentSourceSiteID -> PX.Objects.IN.INSite
PX.Objects.IN.S.INItemSite.INUnitByDfltSalesUnit -> PX.Objects.IN.INUnit (DfltSalesUnit=FromUnit)
PX.Objects.IN.S.INItemSite.INUnitByDfltPurchaseUnit -> PX.Objects.IN.INUnit (DfltPurchaseUnit=FromUnit)
PX.Objects.IN.S.INItemSite.INSitePlanningStrategyByPlanningStrategyID -> PX.Objects.IN.DAC.INSitePlanningStrategy
PX.Objects.IN.S.INItemSite.INSitePlanningStrategyBySiteID -> PX.Objects.IN.DAC.INSitePlanningStrategy
PX.Objects.IN.S.INItemSite.AccountByInvtAcctID -> PX.Objects.GL.Account
PX.Objects.IN.S.INItemSite.SubByInvtSubID -> PX.Objects.GL.Sub
PX.Objects.IN.S.INItemSite.LocationByPreferredVendorLocationID -> PX.Objects.CR.Location (PreferredVendorID=BAccountID)
PX.Objects.IN.S.INItemSite.LocationByPreferredVendorID -> PX.Objects.CR.Location (PreferredVendorID=BAccountID)
PX.Objects.IN.S.INItemSite.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.S.INItemSite.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.S.INItemSite.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.IN.S.INItemSite.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.S.INItemSite.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.S.INItemSite.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.S.INItemSite.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.S.INItemSite.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)

# PX.Objects.IN.StoragePlace (EntityType)

Label: "IN Storage Place"
Key: SiteID
Entity sets: PX_Objects_IN_StoragePlace, INStoragePlace, StoragePlace

PX.Objects.IN.StoragePlace.SiteID : Edm.Int32 [key]
PX.Objects.IN.StoragePlace.SiteCD : Edm.String "Warehouse ID"
PX.Objects.IN.StoragePlace.CartID : Edm.Int32 "Cart ID"
PX.Objects.IN.StoragePlace.StorageID : Edm.Int32
PX.Objects.IN.StoragePlace.StorageCD : Edm.String "Storage ID"
PX.Objects.IN.StoragePlace.Descr : Edm.String "Description"
PX.Objects.IN.StoragePlace.Active : Edm.Boolean "Active"
PX.Objects.IN.StoragePlace.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.IN.StoragePlace.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.IN.StoragePlace.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.StoragePlace.SOPickerCollection -> Collection(PX.Objects.SO.SOPicker)
PX.Objects.IN.StoragePlace.SOPickListEntryToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOPickListEntryToCartSplitLink)
PX.Objects.IN.StoragePlace.SOShipmentSplitToCartSplitLinkCollection -> Collection(PX.Objects.SO.SOShipmentSplitToCartSplitLink)
PX.Objects.IN.StoragePlace.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.IN.StoragePlace.INRegisterCartCollection -> Collection(PX.Objects.IN.DAC.INRegisterCart)
PX.Objects.IN.StoragePlace.INRegisterCartLineCollection -> Collection(PX.Objects.IN.DAC.INRegisterCartLine)
PX.Objects.IN.StoragePlace.SOCartShipmentCollection -> Collection(PX.Objects.SO.SOCartShipment)
PX.Objects.IN.StoragePlace.POCartReceiptCollection -> Collection(PX.Objects.PO.POCartReceipt)
PX.Objects.IN.StoragePlace.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.IN.StoragePlace.StoragePlaceCollection -> Collection(PX.Objects.IN.StoragePlace)
PX.Objects.IN.StoragePlace.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.IN.StoragePlace.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.IN.StoragePlace.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.IN.StoragePlace.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)
PX.Objects.IN.StoragePlace.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.IN.StoragePlace.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.IN.StoragePlace.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.IN.StoragePlace.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.IN.StoragePlace.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.IN.StoragePlace.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.IN.StoragePlace.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.IN.StoragePlace.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.IN.StoragePlace.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.IN.StoragePlace.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.IN.StoragePlace.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.IN.StoragePlace.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.IN.StoragePlace.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.IN.StoragePlace.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.IN.StoragePlace.AMMachSchdCollection -> Collection(PX.Objects.AM.AMMachSchd)
PX.Objects.IN.StoragePlace.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.IN.StoragePlace.AMWCSchdCollection -> Collection(PX.Objects.AM.AMWCSchd)
PX.Objects.IN.StoragePlace.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.IN.StoragePlace.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.IN.StoragePlace.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.IN.StoragePlace.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.IN.StoragePlace.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.IN.StoragePlace.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.IN.StoragePlace.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.IN.StoragePlace.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.IN.StoragePlace.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.IN.StoragePlace.INSiteZoneCollection -> Collection(PX.Objects.IN.DAC.INSiteZone)
PX.Objects.IN.StoragePlace.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.Objects.IN.StoragePlace.AMWCSchdDetailCollection -> Collection(PX.Objects.AM.AMWCSchdDetail)
PX.Objects.IN.StoragePlace.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.IN.StoragePlace.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.IN.StoragePlace.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.IN.StoragePlace.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.IN.StoragePlace.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.IN.StoragePlace.BCLocationsCollection -> Collection(PX.Commerce.Objects.BCLocations)
PX.Objects.IN.StoragePlace.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.StoragePlace.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.IN.StoragePlace.SOOrchestrationPlanCollection -> Collection(PX.Objects.SO.SOOrchestrationPlan)
PX.Objects.IN.StoragePlace.SOOrchestrationPlanLineCollection -> Collection(PX.Objects.SO.SOOrchestrationPlanLine)
PX.Objects.IN.StoragePlace.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.IN.StoragePlace.SOOrderSiteCollection -> Collection(PX.Objects.SO.SOOrderSite)
PX.Objects.IN.StoragePlace.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.IN.StoragePlace.SOPickerToShipmentLinkCollection -> Collection(PX.Objects.SO.SOPickerToShipmentLink)
PX.Objects.IN.StoragePlace.SOPickingWorksheetCollection -> Collection(PX.Objects.SO.SOPickingWorksheet)
PX.Objects.IN.StoragePlace.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.IN.StoragePlace.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.IN.StoragePlace.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.IN.StoragePlace.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.IN.StoragePlace.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.IN.StoragePlace.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.IN.StoragePlace.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.IN.StoragePlace.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.IN.StoragePlace.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.IN.StoragePlace.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.IN.StoragePlace.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.IN.StoragePlace.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.IN.StoragePlace.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.IN.StoragePlace.CarrierPluginCollection -> Collection(PX.Objects.CS.CarrierPlugin)
PX.Objects.IN.StoragePlace.INCartCollection -> Collection(PX.Objects.IN.INCart)
PX.Objects.IN.StoragePlace.INToteCollection -> Collection(PX.Objects.IN.INTote)
PX.Objects.IN.StoragePlace.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.IN.StoragePlace.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.Objects.IN.StoragePlace.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.IN.StoragePlace.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.IN.StoragePlace.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.IN.StoragePlace.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.IN.StoragePlace.INPIClassCollection -> Collection(PX.Objects.IN.INPIClass)
PX.Objects.IN.StoragePlace.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.IN.StoragePlace.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.Objects.IN.StoragePlace.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.IN.StoragePlace.INPIStatusLocCollection -> Collection(PX.Objects.IN.INPIStatusLoc)
PX.Objects.IN.StoragePlace.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.IN.StoragePlace.INReplenishmentOrderCollection -> Collection(PX.Objects.IN.INReplenishmentOrder)
PX.Objects.IN.StoragePlace.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.IN.StoragePlace.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.IN.StoragePlace.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.IN.StoragePlace.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.IN.StoragePlace.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.IN.StoragePlace.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.IN.StoragePlace.INItemClassSiteCollection -> Collection(PX.Objects.IN.DAC.INItemClassSite)
PX.Objects.IN.StoragePlace.INSitePlanningStrategyCollection -> Collection(PX.Objects.IN.DAC.INSitePlanningStrategy)
PX.Objects.IN.StoragePlace.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.IN.StoragePlace.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.IN.StoragePlace.INTransferListCollection -> Collection(PX.Objects.IN.DAC.INTransferList)
PX.Objects.IN.StoragePlace.WarehouseReferenceCollection -> Collection(PX.Objects.IN.DAC.WarehouseReference)
PX.Objects.IN.StoragePlace.LocationBranchSettingsCollection -> Collection(PX.Objects.CR.LocationBranchSettings)
PX.Objects.IN.StoragePlace.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.IN.StoragePlace.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.IN.StoragePlace.DiscountSiteCollection -> Collection(PX.Objects.AR.DiscountSite)
PX.Objects.IN.StoragePlace.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.IN.StoragePlace.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.IN.StoragePlace.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.IN.StoragePlace.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.IN.StoragePlace.AMBOMCurySettingsCollection -> Collection(PX.Objects.AM.AMBOMCurySettings)
PX.Objects.IN.StoragePlace.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.IN.StoragePlace.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.IN.StoragePlace.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.IN.StoragePlace.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.IN.StoragePlace.AMConfigurationOptionCurySettingsCollection -> Collection(PX.Objects.AM.AMConfigurationOptionCurySettings)
PX.Objects.IN.StoragePlace.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.IN.StoragePlace.AMDepartmentCollection -> Collection(PX.Objects.AM.AMDepartment)
PX.Objects.IN.StoragePlace.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.IN.StoragePlace.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.IN.StoragePlace.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.StoragePlace.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.IN.StoragePlace.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.IN.StoragePlace.AMMachSchdDetailCollection -> Collection(PX.Objects.AM.AMMachSchdDetail)
PX.Objects.IN.StoragePlace.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.IN.StoragePlace.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.IN.StoragePlace.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.IN.StoragePlace.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.Objects.IN.StoragePlace.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.IN.StoragePlace.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.IN.StoragePlace.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.IN.StoragePlace.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.IN.StoragePlace.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.IN.StoragePlace.AMSchdOperCollection -> Collection(PX.Objects.AM.AMSchdOper)
PX.Objects.IN.StoragePlace.AMSiteTransferCollection -> Collection(PX.Objects.AM.AMSiteTransfer)
PX.Objects.IN.StoragePlace.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.IN.StoragePlace.AMToolSchdDetailCollection -> Collection(PX.Objects.AM.AMToolSchdDetail)
PX.Objects.IN.StoragePlace.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.IN.StoragePlace.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.IN.StoragePlace.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.IN.StoragePlace.AMWCCollection -> Collection(PX.Objects.AM.AMWC)
PX.Objects.IN.StoragePlace.AMWCSubstituteCollection -> Collection(PX.Objects.AM.AMWCSubstitute)
PX.Objects.IN.StoragePlace.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.IN.StoragePlace.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.IN.StoragePlace.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.IN.StoragePlace.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.IN.StoragePlace.SPInventoryCartItemCollection -> Collection(PX.Objects.Portals.SP.DAC.SPInventoryCartItem)
PX.Objects.IN.StoragePlace.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.IN.StoragePlace.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.IN.StoragePlace.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.IN.StoragePlace.SVStagingWarehouseCollection -> Collection(PX.Objects.SV.SVStagingWarehouse)
PX.Objects.IN.StoragePlace.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.IN.StoragePlace.BlanketSOOrderSiteCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOOrderSite)
PX.Objects.IN.StoragePlace.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.IN.StoragePlace.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.IN.StoragePlace.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.IN.StoragePlace.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.IN.StoragePlace.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.IN.StoragePlace.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.IN.StoragePlace.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.IN.StoragePlace.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.IN.StoragePlace.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.IN.StoragePlace.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.IN.StoragePlace.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.IN.StoragePlace.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.IN.StoragePlace.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.IN.StoragePlace.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.IN.StoragePlace.VendorLocationCollection -> Collection(PX.Objects.PO.VendorLocation)
PX.Objects.IN.StoragePlace.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.IN.StoragePlace.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.IN.StoragePlace.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.IN.StoragePlace.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.IN.StoragePlace.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.IN.StoragePlace.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.IN.StoragePlace.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.IN.StoragePlace.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.IN.StoragePlace.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.IN.StoragePlace.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.IN.StoragePlace.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.IN.StoragePlace.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.IN.StoragePlace.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.IN.StoragePlace.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.IN.StoragePlace.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.IN.StoragePlace.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.IN.StoragePlace.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.IN.StoragePlace.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.IN.StoragePlace.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.IN.StoragePlace.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.IN.StoragePlace.SOShipmentPlanCollection -> Collection(PX.Objects.SO.SOShipmentPlan)

# PX.Objects.IN.Turnover.INTurnoverCalc (EntityType)

Label: "Turnover Calculation"
Key: BranchID, FromPeriodID, ToPeriodID
Entity sets: PX_Objects_IN_Turnover_INTurnoverCalc, TurnoverCalculation, INTurnoverCalc
Non-filterable, non-selectable: NoteText

PX.Objects.IN.Turnover.INTurnoverCalc.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.IN.Turnover.INTurnoverCalc.FromPeriodID : Edm.String [key] "From Period"
PX.Objects.IN.Turnover.INTurnoverCalc.ToPeriodID : Edm.String [key] "To Period"
PX.Objects.IN.Turnover.INTurnoverCalc.IsFullCalc : Edm.Boolean [required]
PX.Objects.IN.Turnover.INTurnoverCalc.IsInventoryListCalc : Edm.Boolean [required]
PX.Objects.IN.Turnover.INTurnoverCalc.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.IN.Turnover.INTurnoverCalc.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.Turnover.INTurnoverCalc.IncludedProduction : Edm.Boolean
PX.Objects.IN.Turnover.INTurnoverCalc.IncludedAssembly : Edm.Boolean
PX.Objects.IN.Turnover.INTurnoverCalc.IncludedIssue : Edm.Boolean
PX.Objects.IN.Turnover.INTurnoverCalc.IncludedTransfer : Edm.Boolean
PX.Objects.IN.Turnover.INTurnoverCalc.NoteID : Edm.Guid
PX.Objects.IN.Turnover.INTurnoverCalc.NoteText : Edm.String "Note Text"
PX.Objects.IN.Turnover.INTurnoverCalc.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.Turnover.INTurnoverCalc.CreatedByScreenID : Edm.String
PX.Objects.IN.Turnover.INTurnoverCalc.CreatedDateTime : Edm.DateTimeOffset "Calculation Date and Time"
PX.Objects.IN.Turnover.INTurnoverCalc.tstamp : Edm.Binary
PX.Objects.IN.Turnover.INTurnoverCalc.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.Turnover.INTurnoverCalc.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.IN.Turnover.INTurnoverCalc.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.Turnover.INTurnoverCalc.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.Turnover.INTurnoverCalc.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.IN.Turnover.INTurnoverCalc.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)

# PX.Objects.IN.Turnover.INTurnoverCalcItem (EntityType)

Label: "Turnover Calculation Item"
Key: BranchID, FromPeriodID, InventoryID, SiteID, ToPeriodID
Entity sets: PX_Objects_IN_Turnover_INTurnoverCalcItem, TurnoverCalculationItem, INTurnoverCalcItem

PX.Objects.IN.Turnover.INTurnoverCalcItem.BranchID : Edm.Int32 [key]
PX.Objects.IN.Turnover.INTurnoverCalcItem.FromPeriodID : Edm.String [key]
PX.Objects.IN.Turnover.INTurnoverCalcItem.ToPeriodID : Edm.String [key]
PX.Objects.IN.Turnover.INTurnoverCalcItem.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.IN.Turnover.INTurnoverCalcItem.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.IN.Turnover.INTurnoverCalcItem.BegQty : Edm.Decimal [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.BegCost : Edm.Decimal [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.YtdQty : Edm.Decimal [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.YtdCost : Edm.Decimal [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.AvgQty : Edm.Decimal [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.AvgCost : Edm.Decimal [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.SoldQty : Edm.Decimal [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.SoldCost : Edm.Decimal [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.QtyRatio : Edm.Decimal
PX.Objects.IN.Turnover.INTurnoverCalcItem.CostRatio : Edm.Decimal
PX.Objects.IN.Turnover.INTurnoverCalcItem.QtySellDays : Edm.Decimal
PX.Objects.IN.Turnover.INTurnoverCalcItem.CostSellDays : Edm.Decimal
PX.Objects.IN.Turnover.INTurnoverCalcItem.IsVirtual : Edm.Boolean [required]
PX.Objects.IN.Turnover.INTurnoverCalcItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.Turnover.INTurnoverCalcItem.CreatedByScreenID : Edm.String
PX.Objects.IN.Turnover.INTurnoverCalcItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.Turnover.INTurnoverCalcItem.tstamp : Edm.Binary
PX.Objects.IN.Turnover.INTurnoverCalcItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.IN.Turnover.INTurnoverCalcItem.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.IN.Turnover.INTurnoverCalcItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.Turnover.INTurnoverCalcItem.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.IN.Turnover.INTurnoverCalcItem.INTurnoverCalcByToPeriodID -> PX.Objects.IN.Turnover.INTurnoverCalc (BranchID=BranchID, FromPeriodID=FromPeriodID, ToPeriodID=ToPeriodID)

# PX.Objects.IN.Turnover.TurnoverCalcItem (EntityType)

Label: "Turnover Calculation Item"
Key: BranchID, FromPeriodID, InventoryCD, SiteCD, ToPeriodID
Entity sets: PX_Objects_IN_Turnover_TurnoverCalcItem, TurnoverCalculationItem1, TurnoverCalcItem

PX.Objects.IN.Turnover.TurnoverCalcItem.BranchID : Edm.Int32 [key]
PX.Objects.IN.Turnover.TurnoverCalcItem.FromPeriodID : Edm.String [key]
PX.Objects.IN.Turnover.TurnoverCalcItem.ToPeriodID : Edm.String [key]
PX.Objects.IN.Turnover.TurnoverCalcItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.IN.Turnover.TurnoverCalcItem.InventoryCD : Edm.String [key]
PX.Objects.IN.Turnover.TurnoverCalcItem.ItemClassID : Edm.Int32
PX.Objects.IN.Turnover.TurnoverCalcItem.Description : Edm.String "Description"
PX.Objects.IN.Turnover.TurnoverCalcItem.UOM : Edm.String "UOM"
PX.Objects.IN.Turnover.TurnoverCalcItem.SiteCD : Edm.String [key]
PX.Objects.IN.Turnover.TurnoverCalcItem.BegQty : Edm.Decimal "Beginning Inventory (Units)"
PX.Objects.IN.Turnover.TurnoverCalcItem.BegCost : Edm.Decimal "Beginning Inventory"
PX.Objects.IN.Turnover.TurnoverCalcItem.YtdQty : Edm.Decimal "Ending Inventory (Units)"
PX.Objects.IN.Turnover.TurnoverCalcItem.YtdCost : Edm.Decimal "Ending Inventory"
PX.Objects.IN.Turnover.TurnoverCalcItem.AvgQty : Edm.Decimal "Average  Inventory (Units)"
PX.Objects.IN.Turnover.TurnoverCalcItem.AvgCost : Edm.Decimal "Average Inventory"
PX.Objects.IN.Turnover.TurnoverCalcItem.SoldQty : Edm.Decimal "Qty. of Items Sold"
PX.Objects.IN.Turnover.TurnoverCalcItem.SoldCost : Edm.Decimal "Cost of Goods Sold"
PX.Objects.IN.Turnover.TurnoverCalcItem.QtyRatio : Edm.Decimal "Turnover Ratio (Units)"
PX.Objects.IN.Turnover.TurnoverCalcItem.CostRatio : Edm.Decimal "Turnover Ratio"
PX.Objects.IN.Turnover.TurnoverCalcItem.QtySellDays : Edm.Decimal
PX.Objects.IN.Turnover.TurnoverCalcItem.CostSellDays : Edm.Decimal "Days Sales of Inventory"
PX.Objects.IN.Turnover.TurnoverCalcItem.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.IN.Turnover.TurnoverCalcItem.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.IN.Turnover.TurnoverCalcItem.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.IN.Turnover.TurnoverCalcItem.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.IN.Turnover.TurnoverCalcItem.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.IN.UnitOfMeasure (EntityType)

Label: "Unit of Measure"
Key: Unit
Entity sets: PX_Objects_IN_UnitOfMeasure, UnitofMeasure
Non-filterable, non-selectable: NoteText

PX.Objects.IN.UnitOfMeasure.Unit : Edm.String [key] "Unit ID"
PX.Objects.IN.UnitOfMeasure.Descr : Edm.String "Description for Reports"
PX.Objects.IN.UnitOfMeasure.NoteID : Edm.Guid
PX.Objects.IN.UnitOfMeasure.NoteText : Edm.String "Note Text"
PX.Objects.IN.UnitOfMeasure.tstamp : Edm.Binary
PX.Objects.IN.UnitOfMeasure.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.UnitOfMeasure.CreatedByScreenID : Edm.String
PX.Objects.IN.UnitOfMeasure.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.UnitOfMeasure.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.UnitOfMeasure.LastModifiedByScreenID : Edm.String
PX.Objects.IN.UnitOfMeasure.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.UnitOfMeasure.L3Code : Edm.String "Level 3 Unit ID"
PX.Objects.IN.UnitOfMeasure.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.UnitOfMeasure.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.UnitOfMeasure.INUnitByUnit -> PX.Objects.IN.INUnit (Unit=RecordID)

# PX.Objects.IN.WMSJob (EntityType)

Label: "IN WMS Job"
Key: JobID
Entity sets: PX_Objects_IN_WMSJob, INWMSJob, WMSJob
Non-filterable, non-selectable: NoteText

PX.Objects.IN.WMSJob.JobID : Edm.Int32 [key]
PX.Objects.IN.WMSJob.JobType : Edm.String
PX.Objects.IN.WMSJob.Status : Edm.String "Status"
PX.Objects.IN.WMSJob.Priority : Edm.Int32 [required] "Priority"
PX.Objects.IN.WMSJob.PreferredAssigneeID : Edm.Guid "Preferred Assignee"
PX.Objects.IN.WMSJob.ActualAssigneeID : Edm.Guid "Actual Assignee"
PX.Objects.IN.WMSJob.EnqueuedAt : Edm.DateTimeOffset "Added to Queue at"
PX.Objects.IN.WMSJob.ReenqueuedAt : Edm.DateTimeOffset "Returned to Queue at"
PX.Objects.IN.WMSJob.CompletedAt : Edm.DateTimeOffset "Completed at"
PX.Objects.IN.WMSJob.MinutesSinceLastModification : Edm.Int32
PX.Objects.IN.WMSJob.NoteID : Edm.Guid
PX.Objects.IN.WMSJob.NoteText : Edm.String "Note Text"
PX.Objects.IN.WMSJob.CreatedByID : Edm.Guid "Created By"
PX.Objects.IN.WMSJob.CreatedByScreenID : Edm.String
PX.Objects.IN.WMSJob.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.IN.WMSJob.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.IN.WMSJob.LastModifiedByScreenID : Edm.String
PX.Objects.IN.WMSJob.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.IN.WMSJob.tstamp : Edm.Binary
PX.Objects.IN.WMSJob.UsersByPreferredAssigneeID -> PX.SM.Users (PreferredAssigneeID=PKID)
PX.Objects.IN.WMSJob.UsersByActualAssigneeID -> PX.SM.Users (ActualAssigneeID=PKID)
PX.Objects.IN.WMSJob.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.IN.WMSJob.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.IN.WMSJob.SOPickingJobCollection -> Collection(PX.Objects.SO.SOPickingJob)

# PX.Objects.Localizations.CA.APAdjustEFileRevision (EntityType)

Label: "APAdjust EFileRevision"
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr, OrgBAccountID, Revision
Entity sets: PX_Objects_Localizations_CA_APAdjustEFileRevision, APAdjustEFileRevision

PX.Objects.Localizations.CA.APAdjustEFileRevision.AdjgDocType : Edm.String [key]
PX.Objects.Localizations.CA.APAdjustEFileRevision.AdjgRefNbr : Edm.String [key]
PX.Objects.Localizations.CA.APAdjustEFileRevision.AdjNbr : Edm.Int32 [key]
PX.Objects.Localizations.CA.APAdjustEFileRevision.AdjdDocType : Edm.String [key]
PX.Objects.Localizations.CA.APAdjustEFileRevision.AdjdRefNbr : Edm.String [key]
PX.Objects.Localizations.CA.APAdjustEFileRevision.AdjdLineNbr : Edm.Int32 [key]
PX.Objects.Localizations.CA.APAdjustEFileRevision.OrgBAccountID : Edm.Int32 [key]
PX.Objects.Localizations.CA.APAdjustEFileRevision.Year : Edm.String
PX.Objects.Localizations.CA.APAdjustEFileRevision.Revision : Edm.String [key]
PX.Objects.Localizations.CA.APAdjustEFileRevision.IncludeInReport : Edm.Boolean
PX.Objects.Localizations.CA.APAdjustEFileRevision.T5018Service : Edm.Boolean
PX.Objects.Localizations.CA.APAdjustEFileRevision.Voided : Edm.Boolean
PX.Objects.Localizations.CA.APAdjustEFileRevision.APAdjustByAdjdLineNbr -> PX.Objects.AP.APAdjust (AdjgDocType=AdjgDocType, AdjgRefNbr=AdjgRefNbr, AdjNbr=AdjNbr, AdjdDocType=AdjdDocType, AdjdRefNbr=AdjdRefNbr, AdjdLineNbr=AdjdLineNbr)
PX.Objects.Localizations.CA.APAdjustEFileRevision.T5018MasterTableByRevision -> PX.Objects.Localizations.CA.T5018MasterTable (OrgBAccountID=OrgBAccountID, Year=Year, Revision=Revision)

# PX.Objects.Localizations.CA.CanadianOrganizationSettings (EntityType)

Label: "Canadian Organization Settings"
Key: OrgBAccountID
Entity sets: PX_Objects_Localizations_CA_CanadianOrganizationSettings, CanadianOrganizationSettings

PX.Objects.Localizations.CA.CanadianOrganizationSettings.OrgBAccountID : Edm.Int32 [key]
PX.Objects.Localizations.CA.CanadianOrganizationSettings.T5018ReportingYear : Edm.Int32 "T5018 Year Type"
PX.Objects.Localizations.CA.CanadianOrganizationSettings.ProgramNumber : Edm.String "Information Returns Account Number"
PX.Objects.Localizations.CA.CanadianOrganizationSettings.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount (OrgBAccountID=BAccountID)

# PX.Objects.Localizations.CA.CanadianVendor (EntityType)

Label: "Canadian Vendor"
Key: VendorID
Entity sets: PX_Objects_Localizations_CA_CanadianVendor, CanadianVendor

PX.Objects.Localizations.CA.CanadianVendor.VendorID : Edm.Int32 [key]
PX.Objects.Localizations.CA.CanadianVendor.CRAVendorReportingType : Edm.Int32 "CRA Reporting Type"
PX.Objects.Localizations.CA.CanadianVendor.CRAVendorType : Edm.Int32 "CRA Vendor Type"
PX.Objects.Localizations.CA.CanadianVendor.T5018ProgramNumber : Edm.String "CRA Information Returns Account Number"
PX.Objects.Localizations.CA.CanadianVendor.SocialInsNum : Edm.String "SIN"
PX.Objects.Localizations.CA.CanadianVendor.T4ADefaultBox : Edm.String "T4A Box"
PX.Objects.Localizations.CA.CanadianVendor.T4AProgramNumber : Edm.String "CRA Payroll Account Number"
PX.Objects.Localizations.CA.CanadianVendor.EmailT4AConsent : Edm.Boolean [required] "Email T4A Slip Consent"
PX.Objects.Localizations.CA.CanadianVendor.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)

# PX.Objects.Localizations.CA.T4AHistory (EntityType)

Label: "T4A History"
Key: BoxNbr, BranchID, Revision, VendorID, Year
Entity sets: PX_Objects_Localizations_CA_T4AHistory, T4AHistory

PX.Objects.Localizations.CA.T4AHistory.BranchID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4AHistory.VendorID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4AHistory.Year : Edm.String [key]
PX.Objects.Localizations.CA.T4AHistory.BoxNbr : Edm.String [key]
PX.Objects.Localizations.CA.T4AHistory.Revision : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4AHistory.HistAmt : Edm.Decimal [required]
PX.Objects.Localizations.CA.T4AHistory.tstamp : Edm.Binary

# PX.Objects.Localizations.CA.T4AHistoryDetails (EntityType)

Label: "T4A History Details"
Key: BoxNbr, BranchID, DocType, RefNbr, Revision, VendorID, Year
Entity sets: PX_Objects_Localizations_CA_T4AHistoryDetails, T4AHistoryDetails

PX.Objects.Localizations.CA.T4AHistoryDetails.BranchID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4AHistoryDetails.VendorID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4AHistoryDetails.Year : Edm.String [key]
PX.Objects.Localizations.CA.T4AHistoryDetails.BoxNbr : Edm.String [key] "T4A Box"
PX.Objects.Localizations.CA.T4AHistoryDetails.Revision : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4AHistoryDetails.DocType : Edm.String [key]
PX.Objects.Localizations.CA.T4AHistoryDetails.RefNbr : Edm.String [key]
PX.Objects.Localizations.CA.T4AHistoryDetails.AmtToReport : Edm.Decimal [required] "Amount To Report"
PX.Objects.Localizations.CA.T4AHistoryDetails.tstamp : Edm.Binary

# PX.Objects.Localizations.CA.T4AMasterTable (EntityType)

Label: "T4A Master Table"
Key: OrgBAccountID, Revision, Year
Entity sets: PX_Objects_Localizations_CA_T4AMasterTable, T4AMasterTable
Non-filterable, non-selectable: FromDate, ToDate, NoteText, ProgramNumber, TransmitterRepID, AcctName, AddressLine1, AddressLine2, City, Province, Country, PostalCode, Name, AreaCode, Phone, ExtensionNbr, Email, SecondEmail, Language, FilingType

PX.Objects.Localizations.CA.T4AMasterTable.OrgBAccountID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4AMasterTable.OrganizationID : Edm.Int32
PX.Objects.Localizations.CA.T4AMasterTable.BranchID : Edm.Int32
PX.Objects.Localizations.CA.T4AMasterTable.Year : Edm.String [key] "Year"
PX.Objects.Localizations.CA.T4AMasterTable.Revision : Edm.String [key] "Revision"
PX.Objects.Localizations.CA.T4AMasterTable.FromDate : Edm.DateTimeOffset "From"
PX.Objects.Localizations.CA.T4AMasterTable.ToDate : Edm.DateTimeOffset "To"
PX.Objects.Localizations.CA.T4AMasterTable.RevisionSubmitted : Edm.Boolean [required] "E-File Submitted to CRA"
PX.Objects.Localizations.CA.T4AMasterTable.XmlData : Edm.String "XmlData"
PX.Objects.Localizations.CA.T4AMasterTable.XmlCanceled : Edm.String "XmlCanceled"
PX.Objects.Localizations.CA.T4AMasterTable.XmlVersion : Edm.String "XmlVersion"
PX.Objects.Localizations.CA.T4AMasterTable.SubmissionNo : Edm.String "Submission Number"
PX.Objects.Localizations.CA.T4AMasterTable.ThresholdAmount : Edm.Decimal "Threshold Amount"
PX.Objects.Localizations.CA.T4AMasterTable.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.CA.T4AMasterTable.CreatedByScreenID : Edm.String
PX.Objects.Localizations.CA.T4AMasterTable.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.Localizations.CA.T4AMasterTable.NoteID : Edm.Guid
PX.Objects.Localizations.CA.T4AMasterTable.NoteText : Edm.String "Note Text"
PX.Objects.Localizations.CA.T4AMasterTable.ProgramNumber : Edm.String "Program Number"
PX.Objects.Localizations.CA.T4AMasterTable.TransmitterRepID : Edm.String "Transmitter RepID"
PX.Objects.Localizations.CA.T4AMasterTable.AcctName : Edm.String "Company Name"
PX.Objects.Localizations.CA.T4AMasterTable.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.Localizations.CA.T4AMasterTable.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.Localizations.CA.T4AMasterTable.City : Edm.String "City"
PX.Objects.Localizations.CA.T4AMasterTable.Province : Edm.String "Province"
PX.Objects.Localizations.CA.T4AMasterTable.Country : Edm.String "Country"
PX.Objects.Localizations.CA.T4AMasterTable.PostalCode : Edm.String "Postal Code"
PX.Objects.Localizations.CA.T4AMasterTable.Name : Edm.String "Name"
PX.Objects.Localizations.CA.T4AMasterTable.AreaCode : Edm.String "Contact Area Code"
PX.Objects.Localizations.CA.T4AMasterTable.Phone : Edm.String "Phone"
PX.Objects.Localizations.CA.T4AMasterTable.ExtensionNbr : Edm.String "Extension Number"
PX.Objects.Localizations.CA.T4AMasterTable.Email : Edm.String "Email"
PX.Objects.Localizations.CA.T4AMasterTable.SecondEmail : Edm.String "Second Email"
PX.Objects.Localizations.CA.T4AMasterTable.Language : Edm.String "Language"
PX.Objects.Localizations.CA.T4AMasterTable.FilingType : Edm.String "Filing Type"
PX.Objects.Localizations.CA.T4AMasterTable.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.Localizations.CA.T4AMasterTable.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.CA.T4AMasterTable.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)

# PX.Objects.Localizations.CA.T4ASlip (EntityType)

Label: "T4A Slip"
Key: BoxNbr, OrgBAccountID, Revision, VendorID, Year
Entity sets: PX_Objects_Localizations_CA_T4ASlip, T4ASlip
Non-filterable, non-selectable: NoteText

PX.Objects.Localizations.CA.T4ASlip.OrgBAccountID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4ASlip.VendorID : Edm.Int32 [key] "Vendor"
PX.Objects.Localizations.CA.T4ASlip.Year : Edm.String [key] "Year"
PX.Objects.Localizations.CA.T4ASlip.BoxNbr : Edm.String [key] "T4A Box"
PX.Objects.Localizations.CA.T4ASlip.Revision : Edm.Int32 [key]
PX.Objects.Localizations.CA.T4ASlip.AmtToReport : Edm.Decimal [required] "T4A Amount"
PX.Objects.Localizations.CA.T4ASlip.Printed : Edm.Boolean "Printed"
PX.Objects.Localizations.CA.T4ASlip.Emailed : Edm.Boolean "Emailed"
PX.Objects.Localizations.CA.T4ASlip.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.CA.T4ASlip.CreatedByScreenID : Edm.String
PX.Objects.Localizations.CA.T4ASlip.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.Localizations.CA.T4ASlip.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Localizations.CA.T4ASlip.LastModifiedByScreenID : Edm.String
PX.Objects.Localizations.CA.T4ASlip.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.CA.T4ASlip.tstamp : Edm.Binary
PX.Objects.Localizations.CA.T4ASlip.NoteID : Edm.Guid
PX.Objects.Localizations.CA.T4ASlip.NoteText : Edm.String "Note Text"
PX.Objects.Localizations.CA.T4ASlip.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.Localizations.CA.T4ASlip.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.CA.T4ASlip.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.Localizations.CA.T5018EFileRow (EntityType)

Label: "T5018 EFile Row"
Key: BAccountID, OrgBAccountID, Revision, Year
Entity sets: PX_Objects_Localizations_CA_T5018EFileRow, T5018EFileRow

PX.Objects.Localizations.CA.T5018EFileRow.OrgBAccountID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T5018EFileRow.Year : Edm.String [key]
PX.Objects.Localizations.CA.T5018EFileRow.Revision : Edm.String [key] "Revision"
PX.Objects.Localizations.CA.T5018EFileRow.OrganizationName : Edm.String "Payer"
PX.Objects.Localizations.CA.T5018EFileRow.BAccountID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T5018EFileRow.Amount : Edm.Decimal "Amount to Report"
PX.Objects.Localizations.CA.T5018EFileRow.TotalServiceAmount : Edm.Decimal "Total Service Amount"
PX.Objects.Localizations.CA.T5018EFileRow.VAcctCD : Edm.String "Vendor"
PX.Objects.Localizations.CA.T5018EFileRow.VendorName : Edm.String "Vendor Name"
PX.Objects.Localizations.CA.T5018EFileRow.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.Localizations.CA.T5018EFileRow.AmendmentRow : Edm.Boolean [required] "AmendmentRow"
PX.Objects.Localizations.CA.T5018EFileRow.ReportType : Edm.String "Report Type"
PX.Objects.Localizations.CA.T5018EFileRow.T5018MasterTableByRevision -> PX.Objects.Localizations.CA.T5018MasterTable (OrgBAccountID=OrgBAccountID, Year=Year, Revision=Revision)

# PX.Objects.Localizations.CA.T5018MasterTable (EntityType)

Label: "T5018 Master Table"
Key: OrgBAccountID, Revision, Year
Entity sets: PX_Objects_Localizations_CA_T5018MasterTable, T5018MasterTable
Non-filterable, non-selectable: NoteText

PX.Objects.Localizations.CA.T5018MasterTable.OrgBAccountID : Edm.Int32 [key] "Transmitter"
PX.Objects.Localizations.CA.T5018MasterTable.OrganizationID : Edm.Int32
PX.Objects.Localizations.CA.T5018MasterTable.BranchID : Edm.Int32
PX.Objects.Localizations.CA.T5018MasterTable.Year : Edm.String [key] "T5018 Tax Year"
PX.Objects.Localizations.CA.T5018MasterTable.Revision : Edm.String [key] "Revision"
PX.Objects.Localizations.CA.T5018MasterTable.RevisionSubmitted : Edm.Boolean [required] "E-File Submitted to CRA"
PX.Objects.Localizations.CA.T5018MasterTable.FromDate : Edm.DateTimeOffset "From"
PX.Objects.Localizations.CA.T5018MasterTable.ToDate : Edm.DateTimeOffset "To"
PX.Objects.Localizations.CA.T5018MasterTable.ProgramNumber : Edm.String "Program Number"
PX.Objects.Localizations.CA.T5018MasterTable.AcctName : Edm.String "Company Name"
PX.Objects.Localizations.CA.T5018MasterTable.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.Localizations.CA.T5018MasterTable.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.Localizations.CA.T5018MasterTable.City : Edm.String "City"
PX.Objects.Localizations.CA.T5018MasterTable.Province : Edm.String "Province"
PX.Objects.Localizations.CA.T5018MasterTable.Country : Edm.String "Country"
PX.Objects.Localizations.CA.T5018MasterTable.PostalCode : Edm.String "Postal Code"
PX.Objects.Localizations.CA.T5018MasterTable.Name : Edm.String "Name"
PX.Objects.Localizations.CA.T5018MasterTable.AreaCode : Edm.String "Contact Area Code"
PX.Objects.Localizations.CA.T5018MasterTable.Phone : Edm.String "Phone"
PX.Objects.Localizations.CA.T5018MasterTable.ExtensionNbr : Edm.String "Extension Number"
PX.Objects.Localizations.CA.T5018MasterTable.Email : Edm.String "Email"
PX.Objects.Localizations.CA.T5018MasterTable.SecondEmail : Edm.String "Second Email"
PX.Objects.Localizations.CA.T5018MasterTable.Language : Edm.String "Language"
PX.Objects.Localizations.CA.T5018MasterTable.FilingType : Edm.String "Filing Type"
PX.Objects.Localizations.CA.T5018MasterTable.SubmissionNo : Edm.String "Submission Number"
PX.Objects.Localizations.CA.T5018MasterTable.ThresholdAmount : Edm.Decimal "Threshold Amount"
PX.Objects.Localizations.CA.T5018MasterTable.TransmitterRepID : Edm.String "Transmitter RepID"
PX.Objects.Localizations.CA.T5018MasterTable.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.CA.T5018MasterTable.CreatedByScreenID : Edm.String
PX.Objects.Localizations.CA.T5018MasterTable.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.Localizations.CA.T5018MasterTable.NoteID : Edm.Guid
PX.Objects.Localizations.CA.T5018MasterTable.NoteText : Edm.String "Note Text"
PX.Objects.Localizations.CA.T5018MasterTable.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount (OrgBAccountID=BAccountID)
PX.Objects.Localizations.CA.T5018MasterTable.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.CA.T5018MasterTable.APAdjustEFileRevisionCollection -> Collection(PX.Objects.Localizations.CA.APAdjustEFileRevision)
PX.Objects.Localizations.CA.T5018MasterTable.T5018EFileRowCollection -> Collection(PX.Objects.Localizations.CA.T5018EFileRow)

# PX.Objects.Localizations.CA.T5018Transactions (EntityType)

Label: "T5018Transactions"
Key: BranchID, DocDate, DocType, RefNbr, VendorID
Entity sets: PX_Objects_Localizations_CA_T5018Transactions, T5018Transactions

PX.Objects.Localizations.CA.T5018Transactions.BranchID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T5018Transactions.VendorID : Edm.Int32 [key]
PX.Objects.Localizations.CA.T5018Transactions.DocDate : Edm.DateTimeOffset [key]
PX.Objects.Localizations.CA.T5018Transactions.DocType : Edm.String [key]
PX.Objects.Localizations.CA.T5018Transactions.RefNbr : Edm.String [key]
PX.Objects.Localizations.CA.T5018Transactions.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.CA.T5018Transactions.tstamp : Edm.Binary

# PX.Objects.Localizations.CA.TaxRegistration (EntityType)

Label: "Tax Registration"
Key: BAccountID, TaxID
Entity sets: PX_Objects_Localizations_CA_TaxRegistration, TaxRegistration

PX.Objects.Localizations.CA.TaxRegistration.BAccountID : Edm.Int32 [key]
PX.Objects.Localizations.CA.TaxRegistration.TaxID : Edm.String [key] "Tax ID"
PX.Objects.Localizations.CA.TaxRegistration.TaxRegistrationNumber : Edm.String "Tax Registration Number"
PX.Objects.Localizations.CA.TaxRegistration.Tstamp : Edm.Binary
PX.Objects.Localizations.CA.TaxRegistration.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.CA.TaxRegistration.CreatedByScreenID : Edm.String
PX.Objects.Localizations.CA.TaxRegistration.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.CA.TaxRegistration.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Localizations.CA.TaxRegistration.LastModifiedByScreenID : Edm.String
PX.Objects.Localizations.CA.TaxRegistration.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.CA.TaxRegistration.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.Localizations.CA.TaxRegistration.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.CA.TaxRegistration.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.Localizations.CA.TaxRegistration.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)

# PX.Objects.Localizations.GB.CISHistory (EntityType)

Label: "CISHistory"
Key: BranchID, Revision, TaxPeriodID, VendorID
Entity sets: PX_Objects_Localizations_GB_CISHistory, CISHistory

PX.Objects.Localizations.GB.CISHistory.BranchID : Edm.Int32 [key]
PX.Objects.Localizations.GB.CISHistory.VendorID : Edm.Int32 [key]
PX.Objects.Localizations.GB.CISHistory.TaxPeriodID : Edm.String [key]
PX.Objects.Localizations.GB.CISHistory.Revision : Edm.Int32 [key]
PX.Objects.Localizations.GB.CISHistory.TotalPayments : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistory.CostOfMaterials : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistory.LiableToDeduction : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistory.AmtDeducted : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistory.NetAmt : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistory.TaxRate : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistory.tstamp : Edm.Binary
PX.Objects.Localizations.GB.CISHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.GB.CISHistory.CreatedByScreenID : Edm.String
PX.Objects.Localizations.GB.CISHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.CISHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Localizations.GB.CISHistory.LastModifiedByScreenID : Edm.String
PX.Objects.Localizations.GB.CISHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.CISHistory.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.Localizations.GB.CISHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.GB.CISHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.Localizations.GB.CISHistoryDetails (EntityType)

Label: "CISHistoryDetails"
Key: BranchID, DocType, RefNbr, Revision, TaxPeriodID, VendorID
Entity sets: PX_Objects_Localizations_GB_CISHistoryDetails, CISHistoryDetails

PX.Objects.Localizations.GB.CISHistoryDetails.BranchID : Edm.Int32 [key]
PX.Objects.Localizations.GB.CISHistoryDetails.VendorID : Edm.Int32 [key]
PX.Objects.Localizations.GB.CISHistoryDetails.TaxPeriodID : Edm.String [key]
PX.Objects.Localizations.GB.CISHistoryDetails.Revision : Edm.Int32 [key]
PX.Objects.Localizations.GB.CISHistoryDetails.DocType : Edm.String [key]
PX.Objects.Localizations.GB.CISHistoryDetails.RefNbr : Edm.String [key]
PX.Objects.Localizations.GB.CISHistoryDetails.TotalPayments : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistoryDetails.CostOfMaterials : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistoryDetails.LiableToDeduction : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistoryDetails.AmtDeducted : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistoryDetails.NetAmt : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistoryDetails.TaxRate : Edm.Decimal [required]
PX.Objects.Localizations.GB.CISHistoryDetails.tstamp : Edm.Binary
PX.Objects.Localizations.GB.CISHistoryDetails.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.GB.CISHistoryDetails.CreatedByScreenID : Edm.String
PX.Objects.Localizations.GB.CISHistoryDetails.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.CISHistoryDetails.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Localizations.GB.CISHistoryDetails.LastModifiedByScreenID : Edm.String
PX.Objects.Localizations.GB.CISHistoryDetails.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.CISHistoryDetails.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.GB.CISHistoryDetails.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.Localizations.GB.CISMasterTable (EntityType)

Label: "CIS Master Table"
Key: OrgBAccountID, Revision, TaxPeriodID
Entity sets: PX_Objects_Localizations_GB_CISMasterTable, CISMasterTable
Non-filterable, non-selectable: NilReturnIndicatorDeclaration, NoteText

PX.Objects.Localizations.GB.CISMasterTable.OrgBAccountID : Edm.Int32 [key] "Contractor"
PX.Objects.Localizations.GB.CISMasterTable.TaxPeriodID : Edm.String [key] "Tax Period"
PX.Objects.Localizations.GB.CISMasterTable.Revision : Edm.Int32 [key]
PX.Objects.Localizations.GB.CISMasterTable.FilingType : Edm.String "Filing Type"
PX.Objects.Localizations.GB.CISMasterTable.NilReturn : Edm.Boolean [required] "Nil Return"
PX.Objects.Localizations.GB.CISMasterTable.PayerRefNbr : Edm.String "Employer's PAYE Ref. Nbr."
PX.Objects.Localizations.GB.CISMasterTable.AccountsOfficeRefNbr : Edm.String "Accounts Office Ref. Nbr."
PX.Objects.Localizations.GB.CISMasterTable.UniqueTaxpayerRefNbr : Edm.String "Unique Taxpayer Ref. Nbr."
PX.Objects.Localizations.GB.CISMasterTable.CISBusinessType : Edm.Int32 "Contractor's Business Type"
PX.Objects.Localizations.GB.CISMasterTable.EmploymentStatusDeclaration : Edm.Boolean [required] "Employment Status Declaration"
PX.Objects.Localizations.GB.CISMasterTable.SubcontractorVerificationDeclaration : Edm.Boolean [required] "Subcontractor Verification Declaration"
PX.Objects.Localizations.GB.CISMasterTable.HigherRateDeductionDeclaration : Edm.Boolean [required] "Higher Rate Deduction Declaration"
PX.Objects.Localizations.GB.CISMasterTable.InformationCorrectDeclaration : Edm.Boolean [required] "Information Correct Declaration"
PX.Objects.Localizations.GB.CISMasterTable.NilReturnIndicatorDeclaration : Edm.Boolean "Nil Return Indicator Declaration"
PX.Objects.Localizations.GB.CISMasterTable.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.GB.CISMasterTable.CreatedByScreenID : Edm.String
PX.Objects.Localizations.GB.CISMasterTable.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.Localizations.GB.CISMasterTable.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.CISMasterTable.LastModifiedByScreenID : Edm.String
PX.Objects.Localizations.GB.CISMasterTable.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Localizations.GB.CISMasterTable.NoteID : Edm.Guid
PX.Objects.Localizations.GB.CISMasterTable.NoteText : Edm.String "Note Text"
PX.Objects.Localizations.GB.CISMasterTable.tstamp : Edm.Binary
PX.Objects.Localizations.GB.CISMasterTable.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount (OrgBAccountID=BAccountID)
PX.Objects.Localizations.GB.CISMasterTable.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.GB.CISMasterTable.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.Localizations.GB.CISMasterTable.UKTaxReportingSettingsByOrgBAccountID -> PX.Objects.Localizations.GB.UKTaxReportingSettings (OrgBAccountID=OrgBAccountID)

# PX.Objects.Localizations.GB.CISSubcontractor (EntityType)

Label: "CIS Subcontractor"
Key: VendorID
Entity sets: PX_Objects_Localizations_GB_CISSubcontractor, CISSubcontractor

PX.Objects.Localizations.GB.CISSubcontractor.VendorID : Edm.Int32 [key]
PX.Objects.Localizations.GB.CISSubcontractor.CISVendor : Edm.Boolean "CIS Subcontractor"
PX.Objects.Localizations.GB.CISSubcontractor.CISTaxAgency : Edm.Boolean "CIS Tax Agency"
PX.Objects.Localizations.GB.CISSubcontractor.CISWithholdingTaxID : Edm.String "CIS Withholding Tax"
PX.Objects.Localizations.GB.CISSubcontractor.UniqueTaxpayerRefNbr : Edm.String "Unique Taxpayer Ref. Nbr."
PX.Objects.Localizations.GB.CISSubcontractor.CISBusinessType : Edm.Int32 "CIS Business Type"
PX.Objects.Localizations.GB.CISSubcontractor.NationalInsuranceNbr : Edm.String "National Insurance Nbr."
PX.Objects.Localizations.GB.CISSubcontractor.OrganizationRegistrationNbr : Edm.String "Company Registration Nbr."
PX.Objects.Localizations.GB.CISSubcontractor.VerificationNbr : Edm.String "Verification Nbr."
PX.Objects.Localizations.GB.CISSubcontractor.UnmatchedTaxRateIndicator : Edm.Boolean "Unmatched Tax Rate Indicator"
PX.Objects.Localizations.GB.CISSubcontractor.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.GB.CISSubcontractor.CreatedByScreenID : Edm.String
PX.Objects.Localizations.GB.CISSubcontractor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.CISSubcontractor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Localizations.GB.CISSubcontractor.LastModifiedByScreenID : Edm.String
PX.Objects.Localizations.GB.CISSubcontractor.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.CISSubcontractor.tstamp : Edm.Binary
PX.Objects.Localizations.GB.CISSubcontractor.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.Localizations.GB.CISSubcontractor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.GB.CISSubcontractor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.Localizations.GB.CISSubcontractor.TaxByCISWithholdingTaxID -> PX.Objects.TX.Tax (CISWithholdingTaxID=TaxID)

# PX.Objects.Localizations.GB.HMRC.DAC.BAccountMTDApplication (EntityType)

Label: "MTD External Application"
Key: BAccountID
Entity sets: PX_Objects_Localizations_GB_HMRC_DAC_BAccountMTDApplication, MTDExternalApplication, BAccountMTDApplication

PX.Objects.Localizations.GB.HMRC.DAC.BAccountMTDApplication.ApplicationID : Edm.Int32 "MTD External Application"
PX.Objects.Localizations.GB.HMRC.DAC.BAccountMTDApplication.BAccountID : Edm.Int32 [key]

# PX.Objects.Localizations.GB.HMRCSubmission (EntityType)

Label: "HMRC Submission"
Key: FormType, HMRCForm
Entity sets: PX_Objects_Localizations_GB_HMRCSubmission, HMRCSubmission

PX.Objects.Localizations.GB.HMRCSubmission.HMRCForm : Edm.Guid [key]
PX.Objects.Localizations.GB.HMRCSubmission.FormType : Edm.String [key]
PX.Objects.Localizations.GB.HMRCSubmission.SubmissionState : Edm.Int32 "CIS Return Status"
PX.Objects.Localizations.GB.HMRCSubmission.CorrelationID : Edm.String
PX.Objects.Localizations.GB.HMRCSubmission.PollInterval : Edm.Int32
PX.Objects.Localizations.GB.HMRCSubmission.HTTPEndPoint : Edm.String
PX.Objects.Localizations.GB.HMRCSubmission.tstamp : Edm.Binary
PX.Objects.Localizations.GB.HMRCSubmission.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.GB.HMRCSubmission.CreatedByScreenID : Edm.String
PX.Objects.Localizations.GB.HMRCSubmission.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.HMRCSubmission.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Localizations.GB.HMRCSubmission.LastModifiedByScreenID : Edm.String
PX.Objects.Localizations.GB.HMRCSubmission.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.HMRCSubmission.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.GB.HMRCSubmission.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.Localizations.GB.UKTaxReportingSettings (EntityType)

Label: "UK Tax Reporting Settings"
Key: OrgBAccountID
Entity sets: PX_Objects_Localizations_GB_UKTaxReportingSettings, UKTaxReportingSettings

PX.Objects.Localizations.GB.UKTaxReportingSettings.OrgBAccountID : Edm.Int32 [key]
PX.Objects.Localizations.GB.UKTaxReportingSettings.PayerRefNbr : Edm.String "Employer's PAYE Ref. Nbr."
PX.Objects.Localizations.GB.UKTaxReportingSettings.AccountsOfficeRefNbr : Edm.String "Accounts Office Ref. Nbr."
PX.Objects.Localizations.GB.UKTaxReportingSettings.UniqueTaxpayerRefNbr : Edm.String "Unique Taxpayer Ref. Nbr."
PX.Objects.Localizations.GB.UKTaxReportingSettings.CISBusinessType : Edm.Int32 "Contractor's Business Type"
PX.Objects.Localizations.GB.UKTaxReportingSettings.HMRCUserID : Edm.String "HMRC User ID"
PX.Objects.Localizations.GB.UKTaxReportingSettings.HMRCPassword : Edm.String "HMRC Password"
PX.Objects.Localizations.GB.UKTaxReportingSettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.Localizations.GB.UKTaxReportingSettings.CreatedByScreenID : Edm.String
PX.Objects.Localizations.GB.UKTaxReportingSettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.UKTaxReportingSettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Localizations.GB.UKTaxReportingSettings.LastModifiedByScreenID : Edm.String
PX.Objects.Localizations.GB.UKTaxReportingSettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Localizations.GB.UKTaxReportingSettings.tstamp : Edm.Binary
PX.Objects.Localizations.GB.UKTaxReportingSettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Localizations.GB.UKTaxReportingSettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.Localizations.GB.UKTaxReportingSettings.CISMasterTableCollection -> Collection(PX.Objects.Localizations.GB.CISMasterTable)

# PX.Objects.MN.DAC.Projections.MaterialMassProcessLine (EntityType)

Label: "Material Line"
Key: LineNbr, SourceNoteID
Entity sets: PX_Objects_MN_DAC_Projections_MaterialMassProcessLine, MaterialLine, MaterialMassProcessLine
Non-filterable, non-selectable: SourceNoteDisplayID, QtyAvailableForDispatch

PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.SourceNoteID : Edm.Guid [key]
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.SourceNoteDisplayID : Edm.Guid "Document ID"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.LineNbr : Edm.Int32 [key]
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.SourceType : Edm.String "Document Type"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.CustomerID : Edm.Int32 "Customer"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.Description : Edm.String "Description"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.UOM : Edm.String "UOM"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.RequiredQty : Edm.Decimal "Required Qty."
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.QtyProcured : Edm.Decimal "Qty. Procured"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.QtyAvailableForDispatch : Edm.Decimal "Qty. Available for Dispatch"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.QtyOnDispatch : Edm.Decimal "Qty. on Dispatch"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.QtyDispatched : Edm.Decimal "Qty. Dispatched"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.ShippedQty : Edm.Decimal
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.TransferredQty : Edm.Decimal
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.NotDispatchedQty : Edm.Decimal
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.QtyUsed : Edm.Decimal "Qty. Used"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.TranDate : Edm.DateTimeOffset "Document Date"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.ShipDate : Edm.DateTimeOffset "Dispatch On"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.NeededByDate : Edm.DateTimeOffset "Needed By"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.Status : Edm.String "Line Status"
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.CostCenterID : Edm.Int32
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.ProvisioningSource : Edm.String
PX.Objects.MN.DAC.Projections.MaterialMassProcessLine.NoteID : Edm.Guid

# PX.Objects.MN.MNMaterialList (EntityType)

Label: "Material List"
Key: RefNbr
Entity sets: PX_Objects_MN_MNMaterialList, MaterialList, MNMaterialList
Non-filterable, non-selectable: NoteText

PX.Objects.MN.MNMaterialList.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.MN.MNMaterialList.ProjectID : Edm.Int32 "Project"
PX.Objects.MN.MNMaterialList.CustomerID : Edm.Int32 "Customer"
PX.Objects.MN.MNMaterialList.ShipAddressID : Edm.Int32
PX.Objects.MN.MNMaterialList.ShipContactID : Edm.Int32 "Shipping Contact"
PX.Objects.MN.MNMaterialList.Date : Edm.DateTimeOffset "Date"
PX.Objects.MN.MNMaterialList.LineCntr : Edm.Int32 [required]
PX.Objects.MN.MNMaterialList.NoteID : Edm.Guid
PX.Objects.MN.MNMaterialList.NoteText : Edm.String "Note Text"
PX.Objects.MN.MNMaterialList.tstamp : Edm.Binary
PX.Objects.MN.MNMaterialList.CreatedByID : Edm.Guid "Created By"
PX.Objects.MN.MNMaterialList.CreatedByScreenID : Edm.String
PX.Objects.MN.MNMaterialList.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.MN.MNMaterialList.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.MN.MNMaterialList.LastModifiedByScreenID : Edm.String
PX.Objects.MN.MNMaterialList.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.MN.MNMaterialList.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.MN.MNMaterialList.PMContactByShipContactID -> PX.Objects.PM.PMContact (ShipContactID=ContactID)
PX.Objects.MN.MNMaterialList.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.MN.MNMaterialList.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.MN.MNMaterialList.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.MN.MNMaterialList.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.MN.MNMaterialList.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.MN.MNMaterialList.INSiteByDefaultSiteID -> PX.Objects.IN.INSite
PX.Objects.MN.MNMaterialList.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.MN.MNMaterialList.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.MN.MNMaterialList.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.MN.MNMaterialList.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.MN.MNMaterialList.MNMaterialListShipmentCollection -> Collection(PX.Objects.MN.MNMaterialListShipment)

# PX.Objects.MN.MNMaterialListLine (EntityType)

Label: "Material Line"
Key: LineNbr, MaterialListNoteID
Entity sets: PX_Objects_MN_MNMaterialListLine, MaterialLine1, MNMaterialListLine
Non-filterable, non-selectable: TranType, QtyAvailableForDispatch, IsKit, LineQtyAvail, LineQtyHardAvail, NoteText

PX.Objects.MN.MNMaterialListLine.MaterialListNoteID : Edm.Guid [key]
PX.Objects.MN.MNMaterialListLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.MN.MNMaterialListLine.DocumentType : Edm.String
PX.Objects.MN.MNMaterialListLine.CustomerID : Edm.Int32
PX.Objects.MN.MNMaterialListLine.ProjectID : Edm.Int32
PX.Objects.MN.MNMaterialListLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.MN.MNMaterialListLine.Description : Edm.String "Description"
PX.Objects.MN.MNMaterialListLine.LotSerialNbr : Edm.String "Lot Serial Number"
PX.Objects.MN.MNMaterialListLine.TranType : Edm.String
PX.Objects.MN.MNMaterialListLine.InvtMult : Edm.Int16
PX.Objects.MN.MNMaterialListLine.IsStockItem : Edm.Boolean
PX.Objects.MN.MNMaterialListLine.UOM : Edm.String "UOM"
PX.Objects.MN.MNMaterialListLine.RequiredQty : Edm.Decimal [required] "Required Qty."
PX.Objects.MN.MNMaterialListLine.BaseRequiredQty : Edm.Decimal [required] "Base Qty."
PX.Objects.MN.MNMaterialListLine.ClosedQty : Edm.Decimal
PX.Objects.MN.MNMaterialListLine.BaseClosedQty : Edm.Decimal
PX.Objects.MN.MNMaterialListLine.UnassignedQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyAllocated : Edm.Decimal [required] "Qty. Allocated"
PX.Objects.MN.MNMaterialListLine.BaseQtyAllocated : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.ShippedQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseShippedQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.TransferredQty : Edm.Decimal [required] "Qty. Transferred"
PX.Objects.MN.MNMaterialListLine.BaseTransferredQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyOnTransfers : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyOnTransfers : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.OpenQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseOpenQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyOnConfirmedShipments : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyOnConfirmedShipments : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyOnPurchaseLines : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyOnPurchaseLines : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyReceived : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyReceived : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyOnOrders : Edm.Decimal [required] "Qty. on Orders"
PX.Objects.MN.MNMaterialListLine.BaseQtyOnOrders : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyUnreceived : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyUnreceived : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyAwaiting : Edm.Decimal [required] "Qty. Awaiting Delivery"
PX.Objects.MN.MNMaterialListLine.BaseQtyAwaiting : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyAvailableForDispatch : Edm.Decimal "Qty. Available for Dispatch"
PX.Objects.MN.MNMaterialListLine.QtyOnDispatch : Edm.Decimal [required] "Qty. on Dispatch"
PX.Objects.MN.MNMaterialListLine.BaseQtyOnDispatch : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyDispatched : Edm.Decimal [required] "Qty. Dispatched"
PX.Objects.MN.MNMaterialListLine.BaseQtyDispatched : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyUsed : Edm.Decimal [required] "Qty. Used"
PX.Objects.MN.MNMaterialListLine.BaseQtyUsed : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.NotDispatchedQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseNotDispatchedQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.MN.MNMaterialListLine.ExtCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.MN.MNMaterialListLine.TranDate : Edm.DateTimeOffset
PX.Objects.MN.MNMaterialListLine.ExpectedByDate : Edm.DateTimeOffset "Expected By"
PX.Objects.MN.MNMaterialListLine.ShipDate : Edm.DateTimeOffset "Dispatch On"
PX.Objects.MN.MNMaterialListLine.NeededByDate : Edm.DateTimeOffset "Needed By"
PX.Objects.MN.MNMaterialListLine.POCreateDate : Edm.DateTimeOffset "Provisioning Doc. Creation Date"
PX.Objects.MN.MNMaterialListLine.ShippingRule : Edm.String
PX.Objects.MN.MNMaterialListLine.CompleteQtyMin : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.CompleteQtyMax : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.Hold : Edm.Boolean
PX.Objects.MN.MNMaterialListLine.Completed : Edm.Boolean [required]
PX.Objects.MN.MNMaterialListLine.Canceled : Edm.Boolean [required]
PX.Objects.MN.MNMaterialListLine.IsInTransfer : Edm.Boolean [required]
PX.Objects.MN.MNMaterialListLine.IsFullyTransferred : Edm.Boolean [required]
PX.Objects.MN.MNMaterialListLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.MN.MNMaterialListLine.ProvisioningSource : Edm.String "Provisioning Source"
PX.Objects.MN.MNMaterialListLine.InventorySource : Edm.String "Inventory Source"
PX.Objects.MN.MNMaterialListLine.QtyProcured : Edm.Decimal [required] "Qty. Procured"
PX.Objects.MN.MNMaterialListLine.BaseQtyProcured : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyOnProductionOrder : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyOnProductionOrder : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyCompletedOnProduction : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyCompletedOnProduction : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyRemainingOnProduction : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyRemainingOnProduction : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyScrappedOnProduction : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.BaseQtyScrappedOnProduction : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.QtyToOrder : Edm.Decimal [required] "Qty. to Order or Allocate"
PX.Objects.MN.MNMaterialListLine.BaseQtyToOrder : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLine.POCreated : Edm.Boolean [required]
PX.Objects.MN.MNMaterialListLine.Status : Edm.String "Status"
PX.Objects.MN.MNMaterialListLine.ProvisionNoteID : Edm.Guid "Provisioning Doc. Ref. Nbr."
PX.Objects.MN.MNMaterialListLine.SplitCntr : Edm.Int32 [required]
PX.Objects.MN.MNMaterialListLine.CostCenterID : Edm.Int32 [required]
PX.Objects.MN.MNMaterialListLine.WorkOrderNbr : Edm.String
PX.Objects.MN.MNMaterialListLine.OrigLineNbr : Edm.Int32 "Orig. Line Nbr."
PX.Objects.MN.MNMaterialListLine.LineType : Edm.String
PX.Objects.MN.MNMaterialListLine.IsKit : Edm.Boolean
PX.Objects.MN.MNMaterialListLine.LineQtyAvail : Edm.Decimal
PX.Objects.MN.MNMaterialListLine.LineQtyHardAvail : Edm.Decimal
PX.Objects.MN.MNMaterialListLine.NoteID : Edm.Guid
PX.Objects.MN.MNMaterialListLine.NoteText : Edm.String "Note Text"
PX.Objects.MN.MNMaterialListLine.tstamp : Edm.Binary
PX.Objects.MN.MNMaterialListLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.MN.MNMaterialListLine.CreatedByScreenID : Edm.String
PX.Objects.MN.MNMaterialListLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.MN.MNMaterialListLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.MN.MNMaterialListLine.LastModifiedByScreenID : Edm.String
PX.Objects.MN.MNMaterialListLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.MN.MNMaterialListLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.MN.MNMaterialListLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.MN.MNMaterialListLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.MN.MNMaterialListLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.MN.MNMaterialListLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.MN.MNMaterialListLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.MN.MNMaterialListLine.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.MN.MNMaterialListLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.MN.MNMaterialListLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.MN.MNMaterialListLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.MN.MNMaterialListLine.MNMaterialListByMaterialListNoteID -> PX.Objects.MN.MNMaterialList (MaterialListNoteID=NoteID)
PX.Objects.MN.MNMaterialListLine.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.MN.MNMaterialListLine.INLocationByToSiteID -> PX.Objects.IN.INLocation
PX.Objects.MN.MNMaterialListLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.MN.MNMaterialListLine.INSiteByPOSiteID -> PX.Objects.IN.INSite
PX.Objects.MN.MNMaterialListLine.INSiteByToSiteID -> PX.Objects.IN.INSite
PX.Objects.MN.MNMaterialListLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.MN.MNMaterialListLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.MN.MNMaterialListLine.INLocationStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLocationStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.MN.MNMaterialListLine.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, LotSerialNbr=LotSerialNbr, CostCenterID=CostCenterID)
PX.Objects.MN.MNMaterialListLine.INSiteStatusByCostCenterByCostCenterID -> PX.Objects.IN.INSiteStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.MN.MNMaterialListLine.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)

# PX.Objects.MN.MNMaterialListLineSplit (EntityType)

Label: "Material Line Split"
Key: LineNbr, MaterialListNoteID, SplitLineNbr
Entity sets: PX_Objects_MN_MNMaterialListLineSplit, MaterialLineSplit, MNMaterialListLineSplit
Non-filterable, non-selectable: TranType, LotSerClassID, AssignedNbr, UnreceivedQty, BaseUnreceivedQty, OpenQty, BaseOpenQty, ProjectID, TaskID, PlanType, POCreate

PX.Objects.MN.MNMaterialListLineSplit.MaterialListNoteID : Edm.Guid [key]
PX.Objects.MN.MNMaterialListLineSplit.LineNbr : Edm.Int32 [key] "Line Number"
PX.Objects.MN.MNMaterialListLineSplit.SplitLineNbr : Edm.Int32 [key] "Allocation ID"
PX.Objects.MN.MNMaterialListLineSplit.DocumentType : Edm.String
PX.Objects.MN.MNMaterialListLineSplit.ParentSplitLineNbr : Edm.Int32 "Parent Allocation ID"
PX.Objects.MN.MNMaterialListLineSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.MN.MNMaterialListLineSplit.TranDate : Edm.DateTimeOffset
PX.Objects.MN.MNMaterialListLineSplit.TranType : Edm.String
PX.Objects.MN.MNMaterialListLineSplit.InvtMult : Edm.Int16
PX.Objects.MN.MNMaterialListLineSplit.IsStockItem : Edm.Boolean
PX.Objects.MN.MNMaterialListLineSplit.LotSerClassID : Edm.String
PX.Objects.MN.MNMaterialListLineSplit.AssignedNbr : Edm.String
PX.Objects.MN.MNMaterialListLineSplit.ShippingRule : Edm.String "Shipping Rule"
PX.Objects.MN.MNMaterialListLineSplit.ShipDate : Edm.DateTimeOffset "Dispatch On"
PX.Objects.MN.MNMaterialListLineSplit.UOM : Edm.String "UOM"
PX.Objects.MN.MNMaterialListLineSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.MN.MNMaterialListLineSplit.BaseQty : Edm.Decimal
PX.Objects.MN.MNMaterialListLineSplit.ShippedQty : Edm.Decimal [required] "Qty. on Dispatch"
PX.Objects.MN.MNMaterialListLineSplit.BaseShippedQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLineSplit.ReceivedQty : Edm.Decimal [required] "Qty. Received"
PX.Objects.MN.MNMaterialListLineSplit.BaseReceivedQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLineSplit.UnreceivedQty : Edm.Decimal
PX.Objects.MN.MNMaterialListLineSplit.BaseUnreceivedQty : Edm.Decimal
PX.Objects.MN.MNMaterialListLineSplit.OpenQty : Edm.Decimal
PX.Objects.MN.MNMaterialListLineSplit.BaseOpenQty : Edm.Decimal
PX.Objects.MN.MNMaterialListLineSplit.TransferredQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLineSplit.BaseTransferredQty : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLineSplit.QtyOnTransfers : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLineSplit.BaseQtyOnTransfers : Edm.Decimal [required]
PX.Objects.MN.MNMaterialListLineSplit.Completed : Edm.Boolean [required] "Completed"
PX.Objects.MN.MNMaterialListLineSplit.IsAllocated : Edm.Boolean [required] "Allocated"
PX.Objects.MN.MNMaterialListLineSplit.HasINTransfer : Edm.Boolean [required]
PX.Objects.MN.MNMaterialListLineSplit.ShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.MN.MNMaterialListLineSplit.ProvisioningSource : Edm.String "Provisioning Source"
PX.Objects.MN.MNMaterialListLineSplit.POCompleted : Edm.Boolean
PX.Objects.MN.MNMaterialListLineSplit.POCanceled : Edm.Boolean
PX.Objects.MN.MNMaterialListLineSplit.VendorID : Edm.Int32
PX.Objects.MN.MNMaterialListLineSplit.POSiteID : Edm.Int32
PX.Objects.MN.MNMaterialListLineSplit.POType : Edm.String "PO Type"
PX.Objects.MN.MNMaterialListLineSplit.PONbr : Edm.String "PO Nbr."
PX.Objects.MN.MNMaterialListLineSplit.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.MN.MNMaterialListLineSplit.POReceiptType : Edm.String "PO Receipt Type"
PX.Objects.MN.MNMaterialListLineSplit.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.MN.MNMaterialListLineSplit.CostCenterID : Edm.Int32 [required]
PX.Objects.MN.MNMaterialListLineSplit.RefNoteID : Edm.Guid "Related Document"
PX.Objects.MN.MNMaterialListLineSplit.PlanID : Edm.Int64
PX.Objects.MN.MNMaterialListLineSplit.ProjectID : Edm.Int32
PX.Objects.MN.MNMaterialListLineSplit.TaskID : Edm.Int32
PX.Objects.MN.MNMaterialListLineSplit.PlanType : Edm.String
PX.Objects.MN.MNMaterialListLineSplit.tstamp : Edm.Binary
PX.Objects.MN.MNMaterialListLineSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.MN.MNMaterialListLineSplit.CreatedByScreenID : Edm.String
PX.Objects.MN.MNMaterialListLineSplit.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.MN.MNMaterialListLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.MN.MNMaterialListLineSplit.LastModifiedByScreenID : Edm.String
PX.Objects.MN.MNMaterialListLineSplit.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.MN.MNMaterialListLineSplit.POCreate : Edm.Boolean "Mark for PO"
PX.Objects.MN.MNMaterialListLineSplit.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.MN.MNMaterialListLineSplit.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.MN.MNMaterialListLineSplit.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.MN.MNMaterialListLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.MN.MNMaterialListLineSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.MN.MNMaterialListLineSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.MN.MNMaterialListLineSplit.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.MN.MNMaterialListLineSplit.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.MN.MNMaterialListLineSplit.MNMaterialListByMaterialListNoteID -> PX.Objects.MN.MNMaterialList (MaterialListNoteID=NoteID)
PX.Objects.MN.MNMaterialListLineSplit.MNMaterialListLineByLineNbr -> PX.Objects.MN.MNMaterialListLine (MaterialListNoteID=MaterialListNoteID, LineNbr=LineNbr)
PX.Objects.MN.MNMaterialListLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.MN.MNMaterialListLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.MN.MNMaterialListLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.MN.MNMaterialListLineSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.MN.MNMaterialListLineSplit.INLotSerialStatusByCostCenterBySiteID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)

# PX.Objects.MN.MNMaterialListShipment (EntityType)

Label: "Material List"
Key: MaterialListNoteID, ShipmentNoteID
Entity sets: PX_Objects_MN_MNMaterialListShipment, MaterialList1, MNMaterialListShipment

PX.Objects.MN.MNMaterialListShipment.ShipmentNoteID : Edm.Guid [key]
PX.Objects.MN.MNMaterialListShipment.MaterialListDocumentType : Edm.String
PX.Objects.MN.MNMaterialListShipment.MaterialListNoteID : Edm.Guid [key]
PX.Objects.MN.MNMaterialListShipment.ShipmentType : Edm.String "Shipment Type"
PX.Objects.MN.MNMaterialListShipment.ShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.MN.MNMaterialListShipment.ShipDate : Edm.DateTimeOffset "Shipment Date"
PX.Objects.MN.MNMaterialListShipment.ShipComplete : Edm.String
PX.Objects.MN.MNMaterialListShipment.ShippedQty : Edm.Decimal [required] "Shipped Qty."
PX.Objects.MN.MNMaterialListShipment.Confirmed : Edm.Boolean [required]
PX.Objects.MN.MNMaterialListShipment.CreateINDoc : Edm.Boolean [required]
PX.Objects.MN.MNMaterialListShipment.InvtDocType : Edm.String "Inventory Doc. Type"
PX.Objects.MN.MNMaterialListShipment.InvtRefNbr : Edm.String "Inventory Ref. Nbr."
PX.Objects.MN.MNMaterialListShipment.InvtNoteID : Edm.Guid
PX.Objects.MN.MNMaterialListShipment.CreatedByID : Edm.Guid "Created By"
PX.Objects.MN.MNMaterialListShipment.CreatedByScreenID : Edm.String
PX.Objects.MN.MNMaterialListShipment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.MN.MNMaterialListShipment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.MN.MNMaterialListShipment.LastModifiedByScreenID : Edm.String
PX.Objects.MN.MNMaterialListShipment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.MN.MNMaterialListShipment.tstamp : Edm.Binary
PX.Objects.MN.MNMaterialListShipment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.MN.MNMaterialListShipment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.MN.MNMaterialListShipment.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentType=ShipmentType, ShipmentNbr=ShipmentNbr)
PX.Objects.MN.MNMaterialListShipment.MNMaterialListByMaterialListNoteID -> PX.Objects.MN.MNMaterialList (MaterialListNoteID=NoteID)
PX.Objects.MN.MNMaterialListShipment.INRegisterByInvtRefNbr -> PX.Objects.IN.INRegister (InvtDocType=DocType, InvtRefNbr=RefNbr)
PX.Objects.MN.MNMaterialListShipment.INRegisterByInvtDocType -> PX.Objects.IN.INRegister (InvtRefNbr=RefNbr, InvtDocType=DocType)

# PX.Objects.MN.MNMaterialListSiteStatusSelected (EntityType)

Label: "Material Line Inventory Lookup Row"
Key: InventoryID
Entity sets: PX_Objects_MN_MNMaterialListSiteStatusSelected, MaterialLineInventoryLookupRow, MNMaterialListSiteStatusSelected
Non-filterable, non-selectable: QtySelected, Rank

PX.Objects.MN.MNMaterialListSiteStatusSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.MN.MNMaterialListSiteStatusSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.MN.MNMaterialListSiteStatusSelected.Descr : Edm.String "Description"
PX.Objects.MN.MNMaterialListSiteStatusSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.MN.MNMaterialListSiteStatusSelected.ItemClassCD : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.MN.MNMaterialListSiteStatusSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.MN.MNMaterialListSiteStatusSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.MN.MNMaterialListSiteStatusSelected.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.MN.MNMaterialListSiteStatusSelected.PreferredVendorDescription : Edm.String "Preferred Vendor Name"
PX.Objects.MN.MNMaterialListSiteStatusSelected.BarCode : Edm.String "Barcode"
PX.Objects.MN.MNMaterialListSiteStatusSelected.BarCodeType : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.BarCodeDescr : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.AlternateID : Edm.String "Alternate ID"
PX.Objects.MN.MNMaterialListSiteStatusSelected.AlternateType : Edm.String "Alternate Type"
PX.Objects.MN.MNMaterialListSiteStatusSelected.AlternateDescr : Edm.String "Alternate Description"
PX.Objects.MN.MNMaterialListSiteStatusSelected.InventoryAlternateID : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.InventoryAlternateType : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.InventoryAlternateDescr : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.SiteCD : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.SubItemCD : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.MN.MNMaterialListSiteStatusSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.MN.MNMaterialListSiteStatusSelected.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.MN.MNMaterialListSiteStatusSelected.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.MN.MNMaterialListSiteStatusSelected.QtyAvailSale : Edm.Decimal "Qty. Available"
PX.Objects.MN.MNMaterialListSiteStatusSelected.QtyOnHandSale : Edm.Decimal "Qty. On Hand"
PX.Objects.MN.MNMaterialListSiteStatusSelected.NoteID : Edm.Guid
PX.Objects.MN.MNMaterialListSiteStatusSelected.ItemStatus : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.Rank : Edm.Int32
PX.Objects.MN.MNMaterialListSiteStatusSelected.CombinedSearchString : Edm.String
PX.Objects.MN.MNMaterialListSiteStatusSelected.StkItem : Edm.Boolean
PX.Objects.MN.MNMaterialListSiteStatusSelected.KitItem : Edm.Boolean
PX.Objects.MN.MNMaterialListSiteStatusSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.MN.MNMaterialListSiteStatusSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.MN.MNMaterialListSiteStatusSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.MN.MNMaterialListSiteStatusSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.MN.POCreateExt.MNMaterialListLineProjection (EntityType)

Label: "Material Line"
Key: LineNbr, MaterialListNoteID
Entity sets: PX_Objects_MN_POCreateExt_MNMaterialListLineProjection, MaterialLine2, MNMaterialListLineProjection

PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.MaterialListNoteID : Edm.Guid [key]
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.LineNbr : Edm.Int32 [key]
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.CustomerID : Edm.Int32
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.BranchID : Edm.Int32
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.InventoryID : Edm.Int32
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.UOM : Edm.String
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.NoteID : Edm.Guid
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.ProjectID : Edm.Int32
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.ExpectedByDate : Edm.DateTimeOffset
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.OpenQty : Edm.Decimal
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.RequiredQty : Edm.Decimal
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.POCreateDate : Edm.DateTimeOffset
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.MNMaterialListByMaterialListNoteID -> PX.Objects.MN.MNMaterialList (MaterialListNoteID=NoteID)
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.MN.POCreateExt.MNMaterialListLineProjection.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)

# PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection (EntityType)

Label: "Material Line Split"
Key: LineNbr, MaterialListNoteID, SplitLineNbr
Entity sets: PX_Objects_MN_POCreateExt_MNMaterialListLineSplitProjection, MaterialLineSplit1, MNMaterialListLineSplitProjection

PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.MaterialListNoteID : Edm.Guid [key]
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.LineNbr : Edm.Int32 [key]
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.SplitLineNbr : Edm.Int32 [key]
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.UOM : Edm.String
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.Qty : Edm.Decimal
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.BaseQty : Edm.Decimal
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.BaseShippedQty : Edm.Decimal
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.POSiteID : Edm.Int32
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.PlanID : Edm.Int64
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.PONbr : Edm.String
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.MNMaterialListByMaterialListNoteID -> PX.Objects.MN.MNMaterialList (MaterialListNoteID=NoteID)
PX.Objects.MN.POCreateExt.MNMaterialListLineSplitProjection.MNMaterialListLineByLineNbr -> PX.Objects.MN.MNMaterialListLine (MaterialListNoteID=MaterialListNoteID, LineNbr=LineNbr)

# PX.Objects.PJ.Common.DAC.ContactForCurrentProject (EntityType)

Key: ContactID
Entity sets: PX_Objects_PJ_Common_DAC_ContactForCurrentProject

PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ContactID : Edm.Int32 [key]
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.DisplayName : Edm.String "Display Name"
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.Salutation : Edm.String "Job Title"
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.FullName : Edm.String "Account Name"
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EMail : Edm.String "Email"
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.Phone1 : Edm.String "Phone 1"
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ContactType : Edm.String "Type"
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.IsActive : Edm.Boolean
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ProjectId : Edm.Int32
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.IsRelatedToProject : Edm.Boolean "Is Related To Project Contact"
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMProjectByProjectId -> PX.Objects.PM.PMProject (ProjectId=ContractID)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.UsersByUserID -> PX.SM.Users
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PJSubmittalWorkflowItemCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRMarketingListCollection -> Collection(PX.Objects.CR.CRMarketingList)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPRuleCollection -> Collection(PX.Objects.EP.EPRule)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRReminderCollection -> Collection(PX.Objects.CR.CRReminder)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPAssignmentRouteCollection -> Collection(PX.Objects.EP.EPAssignmentRoute)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPRuleApproverCollection -> Collection(PX.Objects.EP.DAC.EPRuleApprover)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMEstimateClassCollection -> Collection(PX.Objects.AM.AMEstimateClass)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ContactExtAddressCollection -> Collection(PX.Objects.CR.ContactExtAddress)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.POContactCollection -> Collection(PX.Objects.PO.POContact)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.MultipleQuoteCollection -> Collection(PX.Objects.CN.CRM.CR.DAC.MultipleQuote)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.NotificationRecipientCollection -> Collection(PX.Objects.CS.NotificationRecipient)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ARContactCollection -> Collection(PX.Objects.AR.ARContact)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.SVEventCollection -> Collection(PX.Objects.SV.SVEvent)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRCampaignMembersCollection -> Collection(PX.Objects.CR.CRCampaignMembers)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRMarketingListMemberCollection -> Collection(PX.Objects.CR.CRMarketingListMember)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.SMTeamsMemberCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsMember)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.VPComplianceNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPCompanyTreeMemberCollection -> Collection(PX.TM.EPCompanyTreeMember)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PMProjectContactCollection -> Collection(PX.Objects.PM.PMProjectContact)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRMassMailMemberCollection -> Collection(PX.Objects.CR.CRMassMailMember)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.EPAttendeeCollection -> Collection(PX.Objects.EP.EPAttendee)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.APContactCollection -> Collection(PX.Objects.AP.APContact)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.HSMarketingListMemberCollection -> Collection(PX.DataSync.HubSpot.HSMarketingListMember)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.ESignRecipientCollection -> Collection(PX.ESign.ESignRecipient)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.FSManufacturerCollection -> Collection(PX.Objects.FS.FSManufacturer)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.PRTaxReportingAccountCollection -> Collection(PX.Objects.PR.PRTaxReportingAccount)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.SVServiceLocationContactCollection -> Collection(PX.Objects.SV.SVServiceLocationContact)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.BCRoleAssignmentCollection -> Collection(PX.Commerce.Shopify.BCRoleAssignment)
PX.Objects.PJ.Common.DAC.ContactForCurrentProject.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (EntityType)

Label: "Daily Field Report"
Key: DailyFieldReportCd
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReport, DailyFieldReport
Non-filterable, non-selectable: NoteText, WorkgroupID, OwnerID, TemperatureLevel, Humidity, Icon, TimeObserved, TimeActivitiesTimeBillableTotal, TimeActivitiesTimeSpentTotal, DeletedDatabaseRecord

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportCd : Edm.String [key] "DFR ID"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Hold : Edm.Boolean "Hold"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Approved : Edm.Boolean
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Rejected : Edm.Boolean
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Date : Edm.DateTimeOffset "DFR Date"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Status : Edm.String "Status"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.ProjectManagerId : Edm.Int32 "Project Manager"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.WorkgroupID : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.OwnerID : Edm.Int32 "Owner"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.SiteAddress : Edm.String "Site Address"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.City : Edm.String "City"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.CountryID : Edm.String "Country"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.State : Edm.String "State"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.PostalCode : Edm.String "Postal Code"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Latitude : Edm.Decimal "Latitude"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Longitude : Edm.Decimal "Longitude"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.TemperatureLevel : Edm.Decimal "Temperature"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Humidity : Edm.Decimal "Humidity (%)"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Icon : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.TimeObserved : Edm.DateTimeOffset "Time Observed"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Department : Edm.String "Department"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.SubDepartment : Edm.String "Subdepartment"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.StreetName : Edm.String "Street Name"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.BuildingNumber : Edm.String "Building Number"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.BuildingName : Edm.String "Building Name"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Floor : Edm.String "Floor"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.UnitNumber : Edm.String "Unit Number"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.PostBox : Edm.String "Post Box"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.Room : Edm.String "Room"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.TownLocationName : Edm.String "Town Location Name"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DistrictName : Edm.String "District Name"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.AddressType : Edm.String "Address Type"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.CareOf : Edm.String "Care Of"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.TimeActivitiesTimeBillableTotal : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.TimeActivitiesTimeSpentTotal : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.PMProjectByProjectId -> PX.Objects.PM.PMProject
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.ContactByProjectManagerId -> PX.Objects.CR.Contact (ProjectManagerId=ContactID)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.CountryByCountryId -> PX.Objects.CS.Country
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.StateByCountryId -> PX.Objects.CS.State (State=StateID)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportHistoryCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportNoteCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportSubcontractorActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportVisitorCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportWeatherCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.EquipmentProjectionCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportChangeOrderCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportChangeRequestCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportProjectIssueCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportProgressWorksheetCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportEquipmentCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportEmployeeExpenseCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportPhotoLogCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport.DailyFieldReportEmployeeActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder (EntityType)

Label: "Daily Field Report Change Order"
Key: DailyFieldReportChangeOrderId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportChangeOrder, DailyFieldReportChangeOrder

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder.DailyFieldReportChangeOrderId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder.ChangeOrderId : Edm.String "Reference Nbr."
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder.PMChangeOrderByChangeOrderId -> PX.Objects.PM.PMChangeOrder (ChangeOrderId=RefNbr)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest (EntityType)

Label: "Daily Field Report Change Request"
Key: DailyFieldReportChangeRequestId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportChangeRequest, DailyFieldReportChangeRequest

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest.DailyFieldReportChangeRequestId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest.ChangeRequestId : Edm.String "Reference Nbr."
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest.PMChangeRequestByChangeRequestId -> PX.Objects.PM.PMChangeRequest (ChangeRequestId=RefNbr)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration (EntityType)

Label: "Daily Field Report Copy Configuration"
Singletons: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportCopyConfiguration, DailyFieldReportCopyConfiguration

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.IsConfigurationEnabled : Edm.Boolean "Override Copy-Paste Settings in Daily Field Reports"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.Notes : Edm.Boolean "Notes"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.Date : Edm.Boolean "Date"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.ProjectManager : Edm.Boolean "Project Manager"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.Employee : Edm.Boolean "Employee"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeEarningType : Edm.Boolean "Earning Type"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeProjectTask : Edm.Boolean "Project Task"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeCostCode : Edm.Boolean "Cost Code"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeTime : Edm.Boolean "Time"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeTimeSpent : Edm.Boolean "Time Spent"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeIsBillable : Edm.Boolean "Billable"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeBillableTime : Edm.Boolean "Billable Time"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeDescription : Edm.Boolean "Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeTask : Edm.Boolean "Task"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeCertifiedJob : Edm.Boolean "Certified Job"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeUnionLocal : Edm.Boolean "Union Local"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeLaborItem : Edm.Boolean "Labor Item"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeWccCode : Edm.Boolean "WCC Code"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EmployeeContract : Edm.Boolean "Contract"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.SubcontractorVendorId : Edm.Boolean "Vendor ID"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.SubcontractorProjectTask : Edm.Boolean "Project Task"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.SubcontractorCostCode : Edm.Boolean "Cost Code"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.SubcontractorNumberOfWorkers : Edm.Boolean "Number of Workers"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.SubcontractorTimeArrived : Edm.Boolean "Arrived"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.SubcontractorTimeDeparted : Edm.Boolean "Departed"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.SubcontractorWorkingHours : Edm.Boolean "Working Hours"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.SubcontractorDescription : Edm.Boolean "Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EquipmentId : Edm.Boolean "Equipment ID"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EquipmentProjectTask : Edm.Boolean "Project Task"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EquipmentCostCode : Edm.Boolean "Cost Code"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EquipmentIsBillable : Edm.Boolean "Billable"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EquipmentSetupTime : Edm.Boolean "Setup Time"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EquipmentRunTime : Edm.Boolean "Run Time"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EquipmentSuspendTime : Edm.Boolean "Suspend Time"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.EquipmentDescription : Edm.Boolean "Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportCopyConfiguration.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity (EntityType)

Label: "Daily Field Report Employee Activity"
Key: DailyFieldReportId, EmployeeActivityId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEmployeeActivity, DailyFieldReportEmployeeActivity

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity.DailyFieldReportEmployeeActivityId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity.DailyFieldReportId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity.EmployeeActivityId : Edm.Guid [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity.PMTimeActivityByEmployeeActivityId -> PX.Objects.CR.PMTimeActivity (EmployeeActivityId=NoteID)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense (EntityType)

Label: "Daily Field Report Employee Expenses"
Key: DailyFieldReportEmployeeExpenseId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEmployeeExpense, DailyFieldReportEmployeeExpenses, DailyFieldReportEmployeeExpense

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense.DailyFieldReportEmployeeExpenseId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense.EmployeeExpenseId : Edm.String "Reference Number"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense.EPExpenseClaimDetailsByEmployeeExpenseId -> PX.Objects.EP.EPExpenseClaimDetails (EmployeeExpenseId=ClaimDetailCD)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment (EntityType)

Label: "Daily Field Report Equipment"
Key: DailyFieldReportId, EquipmentDetailLineNumber, EquipmentTimeCardCd
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportEquipment, DailyFieldReportEquipment

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment.DailyFieldReportEquipmentId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment.DailyFieldReportId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment.EquipmentTimeCardCd : Edm.String [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment.EquipmentDetailLineNumber : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment.EPEquipmentDetailByEquipmentDetailLineNumber -> PX.Objects.EP.EPEquipmentDetail (EquipmentTimeCardCd=TimeCardCD, EquipmentDetailLineNumber=LineNbr)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment.EPEquipmentTimeCardByEquipmentTimeCardCd -> PX.Objects.EP.EPEquipmentTimeCard (EquipmentTimeCardCd=TimeCardCD)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory (EntityType)

Label: "Daily Field Report History"
Key: DailyFieldReportHistoryId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportHistory, DailyFieldReportHistory
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.DailyFieldReportHistoryId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.FileName : Edm.String "File Name"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.Comment : Edm.String "Comment"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.CreatedById : Edm.Guid "Completed By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.CreatedDateTime : Edm.DateTimeOffset "Completed Date"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote (EntityType)

Label: "Daily Field Report Note"
Key: DailyFieldReportNoteId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportNote, DailyFieldReportNote
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.DailyFieldReportNoteId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.Time : Edm.DateTimeOffset "Time"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.Description : Edm.String "Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.LastModifiedDateTime : Edm.DateTimeOffset "Last Modification Date"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog (EntityType)

Label: "Daily Field Report Photo Log"
Key: DailyFieldReportPhotoLogId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportPhotoLog, DailyFieldReportPhotoLog

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog.DailyFieldReportPhotoLogId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog.PhotoLogId : Edm.Int32 "Photo Log ID"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog.PhotoLogByPhotoLogId -> PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog (PhotoLogId=PhotoLogId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet (EntityType)

Label: "Daily Field Report Progress Worksheet"
Key: DailyFieldReportId, ProgressWorksheetId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProgressWorksheet, DailyFieldReportProgressWorksheet

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet.DailyFieldReportProgressWorksheetId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet.DailyFieldReportId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet.ProgressWorksheetId : Edm.String [key] "Reference Nbr."
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet.PMProgressWorksheetByProgressWorksheetId -> PX.Objects.PM.PMProgressWorksheet (ProgressWorksheetId=RefNbr)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection (EntityType)

Key: DailyFieldReportCd
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProjection

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportCd : Edm.String [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportHistoryCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportHistory)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportNoteCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportNote)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportSubcontractorActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportVisitorCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportWeatherCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.EquipmentProjectionCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportChangeOrderCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportChangeRequestCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportProjectIssueCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportProgressWorksheetCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportEquipmentCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportEmployeeExpenseCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportPhotoLogCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjection.DailyFieldReportEmployeeActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue (EntityType)

Label: "Daily Field Report Project Issue"
Key: DailyFieldReportProjectIssueId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportProjectIssue, DailyFieldReportProjectIssue

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue.DailyFieldReportProjectIssueId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue.ProjectIssueId : Edm.Int32 "Project Issue ID"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue.ProjectIssueByProjectIssueId -> PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue (ProjectIssueId=ProjectIssueId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity (EntityType)

Label: "Daily Field Report Subcontractor Activity"
Key: SubcontractorId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportSubcontractorActivity, DailyFieldReportSubcontractorActivity
Non-filterable, non-selectable: VendorName, ProjectID, NoteText, DeletedDatabaseRecord

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.SubcontractorId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.VendorId : Edm.Int32 "Vendor ID"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.VendorName : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.ProjectID : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.ProjectTaskID : Edm.Int32 "Project Task"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.NumberOfWorkers : Edm.Int32 "Number of Workers"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.TimeArrived : Edm.DateTimeOffset "TimeArrived"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.TimeDeparted : Edm.DateTimeOffset "TimeDeparted"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.WorkingTimeSpent : Edm.Int32 "Working Hours"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.TotalWorkingTimeSpent : Edm.Int32 "Working Hours Total"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.Description : Edm.String "Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.LastModifiedDateTime : Edm.DateTimeOffset "Last Modification Date"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.VendorByVendorId -> PX.Objects.AP.Vendor (VendorId=BAccountID)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor (EntityType)

Label: "Daily Field Report Visitor"
Key: DailyFieldReportVisitorId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportVisitor, DailyFieldReportVisitor
Non-filterable, non-selectable: NoteText

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.DailyFieldReportVisitorId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.VisitorType : Edm.String "Visitor Type"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.VisitorName : Edm.String "Name"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.BusinessAccountId : Edm.Int32 "Business Account"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.Company : Edm.String "Company"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.TimeArrived : Edm.DateTimeOffset "TimeArrived"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.TimeDeparted : Edm.DateTimeOffset "TimeDeparted"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.PurposeOfVisit : Edm.String "Purpose of Visit"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.AreaVisited : Edm.String "Area Visited/Inspected Entity"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.Description : Edm.String "Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.LastModifiedDateTime : Edm.DateTimeOffset "Last Modification Date"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.BAccountByBusinessAccountId -> PX.Objects.CR.BAccount (BusinessAccountId=BAccountID)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather (EntityType)

Label: "Daily Field Report Weather"
Key: DailyFieldReportWeatherId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_DailyFieldReportWeather, DailyFieldReportWeather
Non-filterable, non-selectable: TemperatureLevelMobile, PrecipitationAmountMobile, WindSpeedMobile, NoteText

PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.DailyFieldReportWeatherId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.Icon : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.TimeObserved : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.Cloudiness : Edm.Int32 "Cloudiness (%)"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.SkyState : Edm.String "Sky"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.TemperatureLevel : Edm.Decimal "TemperatureLevel"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.TemperatureLevelMobile : Edm.Decimal "Temperature"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.Temperature : Edm.String "Temperature Perceived"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.Humidity : Edm.Decimal "Humidity (%)"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.PrecipitationAmount : Edm.Decimal "PrecipitationAmount"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.PrecipitationAmountMobile : Edm.Decimal "Rain/Snow"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.Precipitation : Edm.String "Precipitation Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.WindSpeed : Edm.Decimal "WindSpeed"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.WindSpeedMobile : Edm.Decimal "Wind"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.WindPower : Edm.String "Wind Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.LocationCondition : Edm.String "Site Conditions"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.IsObservationDelayed : Edm.Boolean "Delay"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.Description : Edm.String "Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.LastModifiedDateTime : Edm.DateTimeOffset "Last Modification Date"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportWeather.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection (EntityType)

Label: "Daily Field Report Equipment"
BaseType: PX.Objects.EP.EPEquipmentDetail
Key: LineNbr, TimeCardCD (inherited from PX.Objects.EP.EPEquipmentDetail)
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_EquipmentProjection, DailyFieldReportEquipment1, EquipmentProjection

PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.DailyFieldReportEquipmentId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.EquipmentTimeCardCd : Edm.String "Time Card Ref."
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.EquipmentDetailLineNumber : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.EquipmentId : Edm.Int32 "Equipment ID"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.EquipmentDescription : Edm.String "Equipment Description"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.TimeCardStatus : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.DailyFieldReportByDailyFieldReportId -> PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport (DailyFieldReportId=DailyFieldReportId)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.EPEquipmentByEquipmentId -> PX.Objects.EP.EPEquipment (EquipmentId=EquipmentID)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.EPEquipmentDetailByEquipmentDetailLineNumber -> PX.Objects.EP.EPEquipmentDetail (EquipmentTimeCardCd=TimeCardCD, EquipmentDetailLineNumber=LineNbr)
PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection.EPEquipmentTimeCardByEquipmentTimeCardCd -> PX.Objects.EP.EPEquipmentTimeCard (EquipmentTimeCardCd=TimeCardCD)

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup (EntityType)

Label: "Project Management Preferences - Weather Service Integration Settings"
Singletons: PX_Objects_PJ_DailyFieldReports_PJ_DAC_WeatherIntegrationSetup, ProjectManagementPreferencesWeatherServiceIntegrationSettings, WeatherIntegrationSetup

PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherIntegrationSetup.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog (EntityType)

Label: "Weather Processing Log"
Key: WeatherProcessingLogId
Entity sets: PX_Objects_PJ_DailyFieldReports_PJ_DAC_WeatherProcessingLog, WeatherProcessingLog
Non-filterable, non-selectable: NoteText

PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.Tstamp : Edm.Binary
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.CreatedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.NoteID : Edm.Guid
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.WeatherProcessingLogId : Edm.Int32 [key]
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.WeatherService : Edm.String "Weather Service"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.RequestTime : Edm.DateTimeOffset "Request Time"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.RequestBody : Edm.String "Request Body"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.RequestStatusIcon : Edm.String "Request Status Icon"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.ResponseTime : Edm.DateTimeOffset "Response Time"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.ResponseBody : Edm.String "Response Body"
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DailyFieldReports.PJ.DAC.WeatherProcessingLog.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog (EntityType)

Label: "Drawing Log"
Key: DrawingLogCd
Entity sets: PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLog, DrawingLog
Non-filterable, non-selectable: SelectorStatusId, UsrDrawingLogClassId, NoteText, DeletedDatabaseRecord

PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.Tstamp : Edm.Binary
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.CreatedByScreenId : Edm.String
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DrawingLogId : Edm.Int32
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DrawingLogCd : Edm.String [key] "Drawing Log ID"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.OwnerId : Edm.Int32 "Owner"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.OriginalDrawingId : Edm.Guid "Original Drawing"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DisciplineId : Edm.Int32 "Discipline"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.Number : Edm.String "Drawing Number"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.Revision : Edm.String "Revision"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.Sketch : Edm.String "Sketch"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.Title : Edm.String "Title"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.Description : Edm.String "Description"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.StatusId : Edm.Int32 "Status"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.SelectorStatusId : Edm.Int32 "Status"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DrawingDate : Edm.DateTimeOffset "Drawing Date"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.ReceivedDate : Edm.DateTimeOffset "Received Date"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.IsCurrent : Edm.Boolean [required] "Latest Revision"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.UsrDrawingLogClassId : Edm.String
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.NoteID : Edm.Guid
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.PMProjectByProjectId -> PX.Objects.PM.PMProject
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.PMTaskByProjectId -> PX.Objects.PM.PMTask
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.PMTaskByProjectTaskId -> PX.Objects.PM.PMTask
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.ContactByOwnerId -> PX.Objects.CR.Contact (OwnerId=ContactID)
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DrawingLogByOriginalDrawingId -> PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog (OriginalDrawingId=NoteID)
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DrawingLogDisciplineByDisciplineId -> PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline (DisciplineId=DrawingLogDisciplineId)
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DrawingLogStatusByStatusId -> PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus (StatusId=StatusId)
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)

# PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline (EntityType)

Label: "Drawing Log Discipline"
Key: DrawingLogDisciplineId
Entity sets: PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogDiscipline, DrawingLogDiscipline
Non-filterable, non-selectable: LineNbr

PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline.DrawingLogDisciplineId : Edm.Int32 [key]
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline.Name : Edm.String "Discipline"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline.IsDefault : Edm.Boolean
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline.IsActive : Edm.Boolean "Active"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline.LineNbr : Edm.Int32 "Line Nbr"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogDiscipline.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)

# PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogRevision (EntityType)

Label: "Drawing Log Revision"
Key: DrawingLogId, DrawingLogRevisionId
Entity sets: PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogRevision, DrawingLogRevision

PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogRevision.DrawingLogId : Edm.Int32 [key]
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogRevision.DrawingLogRevisionId : Edm.Int32 [key]

# PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup (EntityType)

Label: "Drawing Log Preferences"
Singletons: PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogSetup, DrawingLogPreferences, DrawingLogSetup

PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.Tstamp : Edm.Binary
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.CreatedByScreenId : Edm.String
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.NoteID : Edm.Guid
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.NoteText : Edm.String "Note Text"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.DrawingLogNumberingSequenceId : Edm.String "Drawing Log Numbering Sequence"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup.NumberingByDrawingLogNumberingSequenceId -> PX.Objects.CS.Numbering (DrawingLogNumberingSequenceId=NumberingID)

# PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus (EntityType)

Label: "Drawing Log Status"
Key: StatusId
Entity sets: PX_Objects_PJ_DrawingLogs_PJ_DAC_DrawingLogStatus, DrawingLogStatus

PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus.StatusId : Edm.Int32 [key]
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus.Name : Edm.String "Status"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus.Description : Edm.String "Description"
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus.IsDefault : Edm.Boolean
PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogStatus.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)

# PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings (EntityType)

Label: "Email Drawings"
Key: DrawingLogCd, RequestForInformationCd
Entity sets: PX_Objects_PJ_DrawingLogs_PJ_DAC_EmailDrawings, EmailDrawings

PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.RequestForInformationId : Edm.Int32
PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.RequestForInformationCd : Edm.String [key]
PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.DrawingLogId : Edm.Int32
PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.DrawingLogCd : Edm.String [key]
PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.Number : Edm.String
PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.Revision : Edm.String
PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.Sketch : Edm.String
PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.EmailNoteId : Edm.Guid
PX.Objects.PJ.DrawingLogs.PJ.DAC.EmailDrawings.RequestForInformationByRequestForInformationId -> PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation (RequestForInformationId=IncomingRequestForInformationId)

# PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo (EntityType)

Label: "Photo"
Key: PhotoCd
Entity sets: PX_Objects_PJ_PhotoLogs_PJ_DAC_Photo, Photo
Non-filterable, non-selectable: ImageUrl, NoteText, Tstamp, CreatedByScreenId, CreatedDateTime, LastModifiedById, LastModifiedByScreenId, LastModifiedDateTime, UsrPhotoClassId, Tags, DeletedDatabaseRecord

PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.PhotoLogId : Edm.Int32 "Photo Log ID"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.PhotoId : Edm.Int32
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.PhotoCd : Edm.String [key] "Photo ID"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.Name : Edm.String "Name"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.Description : Edm.String "Description"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.UploadedDate : Edm.DateTimeOffset "Uploaded On"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.UploadedById : Edm.Guid "Uploaded By"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.IsMainPhoto : Edm.Boolean "Main Photo"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.FileId : Edm.Guid "FileId"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.ImageUrl : Edm.String "Image"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.NoteID : Edm.Guid
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.NoteText : Edm.String "Note Text"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.Tstamp : Edm.Binary
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.CreatedByScreenId : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.UsrPhotoClassId : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.Tags : Edm.String "Tags"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.PhotoLogByPhotoLogId -> PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog (PhotoLogId=PhotoLogId)
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.UsersByUploadedById -> PX.SM.Users (UploadedById=PKID)
PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo.UsersByCreatedById -> PX.SM.Users (CreatedById=PKID)

# PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog (EntityType)

Label: "Photo Log"
Key: PhotoLogCd
Entity sets: PX_Objects_PJ_PhotoLogs_PJ_DAC_PhotoLog, PhotoLog
Non-filterable, non-selectable: SelectorStatusId, NoteText, DailyFieldReportId, FormCaptionDescription, PhotoLogClassID, DeletedDatabaseRecord

PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.Tstamp : Edm.Binary
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.CreatedByScreenId : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.PhotoLogId : Edm.Int32
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.PhotoLogCd : Edm.String [key] "Photo Log ID"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.Date : Edm.DateTimeOffset "Date"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.Description : Edm.String "Description"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.StatusId : Edm.Int32 "Status"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.SelectorStatusId : Edm.Int32 "Status"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.LastModifiedDateTime : Edm.DateTimeOffset "Last Modification Date"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.NoteID : Edm.Guid
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.NoteText : Edm.String "Note Text"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.DailyFieldReportId : Edm.Int32
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.FormCaptionDescription : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.PhotoLogClassID : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.PMProjectByProjectId -> PX.Objects.PM.PMProject
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.PMTaskByProjectId -> PX.Objects.PM.PMTask
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.PhotoLogStatusByStatusId -> PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus (StatusId=StatusId)
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.PhotoCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.Photo)
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog.DailyFieldReportPhotoLogCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportPhotoLog)

# PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup (EntityType)

Label: "Photo Log Preferences"
Singletons: PX_Objects_PJ_PhotoLogs_PJ_DAC_PhotoLogSetup, PhotoLogPreferences, PhotoLogSetup

PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.Tstamp : Edm.Binary
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.CreatedByScreenId : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.NoteID : Edm.Guid
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.NoteText : Edm.String "Note Text"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.PhotoLogNumberingId : Edm.String "Photo Log Numbering Sequence"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.PhotoNumberingId : Edm.String "Photo Numbering Sequence"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.NumberingByPhotoLogNumberingId -> PX.Objects.CS.Numbering (PhotoLogNumberingId=NumberingID)
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup.NumberingByPhotoNumberingId -> PX.Objects.CS.Numbering (PhotoNumberingId=NumberingID)

# PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus (EntityType)

Label: "Photo Log Status"
Key: StatusId
Entity sets: PX_Objects_PJ_PhotoLogs_PJ_DAC_PhotoLogStatus, PhotoLogStatus

PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus.StatusId : Edm.Int32 [key]
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus.Name : Edm.String "Status"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus.Description : Edm.String "Description"
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus.IsDefault : Edm.Boolean
PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogStatus.PhotoLogCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog)

# PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass (EntityType)

Label: "Project Management Class"
Key: ProjectManagementClassId
Entity sets: PX_Objects_PJ_ProjectManagement_PJ_DAC_ProjectManagementClass, ProjectManagementClass
Non-filterable, non-selectable: NoteText

PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.Tstamp : Edm.Binary
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.CreatedByScreenId : Edm.String
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.NoteID : Edm.Guid
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.NoteText : Edm.String "Note Text"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.ProjectManagementClassId : Edm.String [key] "Project Management Class ID"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.Description : Edm.String "Description"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.IsInternal : Edm.Boolean [required] "Internal"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.UseForProjectIssue : Edm.Boolean [required] "Project Issues"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.UseForRequestForInformation : Edm.Boolean [required] "Requests For Information"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.RequestForInformationResponseTimeFrame : Edm.Int32 "Answer Days Default"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.ProjectIssueResponseTimeFrame : Edm.Int32 "Answer Days Default"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)

# PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority (EntityType)

Label: "Project Management Class Priority"
Key: PriorityId
Entity sets: PX_Objects_PJ_ProjectManagement_PJ_DAC_ProjectManagementClassPriority, ProjectManagementClassPriority
Non-filterable, non-selectable: NoteText

PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.Tstamp : Edm.Binary
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.CreatedByScreenId : Edm.String
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.NoteID : Edm.Guid
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.NoteText : Edm.String "Note Text"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.PriorityId : Edm.Int32 [key]
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.ClassId : Edm.String
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.IsActive : Edm.Boolean "Active"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.PriorityName : Edm.String "Priority Name"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.IsDefault : Edm.Boolean "Default"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.IsSystemPriority : Edm.Boolean
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.IsHighestPriority : Edm.Boolean
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)

# PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup (EntityType)

Label: "Project Management Preferences"
Singletons: PX_Objects_PJ_ProjectManagement_PJ_DAC_ProjectManagementSetup, ProjectManagementPreferences, ProjectManagementSetup

PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.Tstamp : Edm.Binary
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.CreatedByScreenId : Edm.String
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.NoteID : Edm.Guid
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.NoteText : Edm.String "Note Text"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.AnswerDaysCalculationType : Edm.String "Due Date Calculation Type"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.CalendarId : Edm.String "Calendar"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.RequestForInformationNumberingId : Edm.String "RFI Numbering Sequence"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.ProjectIssueNumberingId : Edm.String "Project Issue Numbering Sequence"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.DefaultEmailNotification : Edm.Int32 "Default Email Notification"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.ProjectIssueAssignmentMapId : Edm.Int32 "Project Issue Assignment Map"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.RequestForInformationAssignmentMapId : Edm.Int32 "RFI Assignment Map"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.DailyFieldReportNumberingId : Edm.String "DFR Numbering Sequence"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.DailyFieldReportApprovalMapId : Edm.Int32 "DFR Approval Map"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.PendingApprovalNotification : Edm.Int32 "DFR Approval Notification"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.IsHistoryLogEnabled : Edm.Boolean "Enable History Log"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.SubmittalNumberingId : Edm.String "Submittal Numbering Sequence"
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.NotificationByDefaultEmailNotification -> PX.SM.Notification (DefaultEmailNotification=NotificationID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.NotificationByPendingApprovalNotification -> PX.SM.Notification (PendingApprovalNotification=NotificationID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.NumberingByRequestForInformationNumberingId -> PX.Objects.CS.Numbering (RequestForInformationNumberingId=NumberingID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.NumberingByProjectIssueNumberingId -> PX.Objects.CS.Numbering (ProjectIssueNumberingId=NumberingID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.NumberingByDailyFieldReportNumberingId -> PX.Objects.CS.Numbering (DailyFieldReportNumberingId=NumberingID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.NumberingBySubmittalNumberingId -> PX.Objects.CS.Numbering (SubmittalNumberingId=NumberingID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.EPAssignmentMapByProjectIssueAssignmentMapId -> PX.Objects.EP.EPAssignmentMap (ProjectIssueAssignmentMapId=AssignmentMapID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.EPAssignmentMapByRequestForInformationAssignmentMapId -> PX.Objects.EP.EPAssignmentMap (RequestForInformationAssignmentMapId=AssignmentMapID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.EPAssignmentMapByDailyFieldReportApprovalMapId -> PX.Objects.EP.EPAssignmentMap (DailyFieldReportApprovalMapId=AssignmentMapID)
PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup.CSCalendarByCalendarId -> PX.Objects.CS.CSCalendar (CalendarId=CalendarID)

# PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue (EntityType)

Label: "Project Issue"
Key: ProjectIssueCd
Entity sets: PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssue, ProjectIssue
Non-filterable, non-selectable: MajorStatus, NoteText, PriorityIcon, DailyFieldReportId, DeletedDatabaseRecord

PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.Tstamp : Edm.Binary
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.CreatedByScreenId : Edm.String
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.IsScheduleImpact : Edm.Boolean "Schedule Impact (Days)"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ScheduleImpact : Edm.Int32 "Schedule Impact (Days)"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.IsCostImpact : Edm.Boolean "Cost Impact"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.CostImpact : Edm.Decimal "Cost Impact"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ProjectIssueId : Edm.Int32 "Project Issue ID"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ProjectIssueCd : Edm.String [key] "Project Issue ID"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.Summary : Edm.String "Summary"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ClassId : Edm.String "Class ID"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.OwnerID : Edm.Int32 "Owner"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.Description : Edm.String "Description"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.PriorityId : Edm.Int32 "Priority"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.Status : Edm.String "Status"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.MajorStatus : Edm.String
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ResolvedOn : Edm.DateTimeOffset "Resolved On"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.CreationDate : Edm.DateTimeOffset "Created On"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ConvertedTo : Edm.Guid "Converted To"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.NoteID : Edm.Guid
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.NoteText : Edm.String "Note Text"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.RefNoteIDType : Edm.String "Related Entity Type"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.RefNoteID : Edm.Guid "Related Entity"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.PriorityIcon : Edm.String "Priority Icon"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ProjectIssueTypeId : Edm.Int32 "Project Issue Type"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.LastModifiedDateTime : Edm.DateTimeOffset "Last Modification Date"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.DailyFieldReportId : Edm.Int32 "DailyFieldReportId"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.PMProjectByProjectId -> PX.Objects.PM.PMProject
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.PMTaskByProjectTaskId -> PX.Objects.PM.PMTask
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.PMTaskByProjectId -> PX.Objects.PM.PMTask
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ProjectManagementClassByClassId -> PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass (ClassId=ProjectManagementClassId)
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ProjectManagementClassPriorityByClassId -> PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority (PriorityId=PriorityId, ClassId=ClassId)
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.ProjectIssueTypeByProjectIssueTypeId -> PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueType (ProjectIssueTypeId=ProjectIssueTypeId)
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue.DailyFieldReportProjectIssueCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProjectIssue)

# PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueDrawingLog (EntityType)

Label: "Project Issue Drawing Log"
Key: DrawingLogId, ProjectIssueId
Entity sets: PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssueDrawingLog, ProjectIssueDrawingLog

PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueDrawingLog.DrawingLogId : Edm.Int32 [key]
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueDrawingLog.ProjectIssueId : Edm.Int32 [key]

# PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueType (EntityType)

Label: "Project Issue Type"
Key: ProjectIssueTypeId
Entity sets: PX_Objects_PJ_ProjectsIssue_PJ_DAC_ProjectIssueType, ProjectIssueType

PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueType.ProjectIssueTypeId : Edm.Int32 [key]
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueType.TypeName : Edm.String "Project Issue Type"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueType.Description : Edm.String "Description"
PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssueType.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)

# PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation (EntityType)

Label: "Request For Information"
Key: RequestForInformationCd
Entity sets: PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformation, RequestForInformation
Non-filterable, non-selectable: NoteText, IsScheduleImpactFormatted, IsCostImpactFormatted, DesignChangeFormatted, DeletedDatabaseRecord

PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.Tstamp : Edm.Binary
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.CreatedByScreenId : Edm.String
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.IsScheduleImpact : Edm.Boolean "Schedule Impact (Days)"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ScheduleImpact : Edm.Int32 "Schedule Impact (Days)"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.IsCostImpact : Edm.Boolean "Cost Impact"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.CostImpact : Edm.Decimal "Cost Impact"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.RequestForInformationId : Edm.Int32 "RFI ID"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.RequestForInformationCd : Edm.String [key] "RFI ID"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.Summary : Edm.String "Summary"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.IncomingRequestForInformationId : Edm.Int32 "Link to Incoming RFI"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.RequestForInformationNumber : Edm.String "RFI Number."
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ClassId : Edm.String "Class ID"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.OwnerID : Edm.Int32 "Owner"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.RequestDetails : Edm.String "Question"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.RequestAnswer : Edm.String "Answer"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.LastModifiedRequestAnswer : Edm.DateTimeOffset "Last Modified Date"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.Status : Edm.String "Status"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.MajorStatus : Edm.String
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.BusinessAccountId : Edm.Int32 "Business Account"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ContactId : Edm.Int32 "Contact"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.DesignChange : Edm.Boolean "Design Change"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.Incoming : Edm.Boolean "Incoming"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.DocumentationLink : Edm.String "Specification"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.SpecSection : Edm.String "Specification Section"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.CreationDate : Edm.DateTimeOffset "Creation Date"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.PriorityId : Edm.Int32 "Priority"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ConvertedTo : Edm.Guid "Converted To"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ConvertedFrom : Edm.Guid "Converted From"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.Reason : Edm.String "Reason"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.DueResponseDate : Edm.DateTimeOffset "Answer Due Date"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.NoteID : Edm.Guid
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.NoteText : Edm.String "Note Text"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.IsScheduleImpactFormatted : Edm.String
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.IsCostImpactFormatted : Edm.String
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.DesignChangeFormatted : Edm.String
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.PMProjectByProjectId -> PX.Objects.PM.PMProject
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.RequestForInformationByRequestForInformationId -> PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation (RequestForInformationId=IncomingRequestForInformationId)
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.PMTaskByProjectTaskId -> PX.Objects.PM.PMTask
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.PMTaskByProjectId -> PX.Objects.PM.PMTask
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.BAccountByBusinessAccountId -> PX.Objects.CR.BAccount (BusinessAccountId=BAccountID)
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ContactByContactID -> PX.Objects.CR.Contact
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ContactByBusinessAccountId -> PX.Objects.CR.Contact (BusinessAccountId=BAccountID)
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ProjectManagementClassByClassId -> PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClass (ClassId=ProjectManagementClassId)
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.ProjectManagementClassPriorityByClassId -> PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementClassPriority (PriorityId=PriorityId, ClassId=ClassId)
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)

# PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationAttachment (EntityType)

Label: "Request For Information Attachment"
Key: FileID, RequestForInformationCd
Entity sets: PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationAttachment, RequestForInformationAttachment

PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationAttachment.RequestForInformationCd : Edm.String [key]
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationAttachment.FileID : Edm.Guid [key]
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationAttachment.Outgoing : Edm.Boolean

# PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationDrawingLog (EntityType)

Label: "Request For Information Drawing Log"
Key: DrawingLogId, RequestForInformationId
Entity sets: PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationDrawingLog, RequestForInformationDrawingLog

PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationDrawingLog.DrawingLogId : Edm.Int32 [key]
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationDrawingLog.RequestForInformationId : Edm.Int32 [key]

# PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation (EntityType)

Label: "Request For Information Relation"
Key: RequestForInformationRelationId
Entity sets: PX_Objects_PJ_RequestsForInformation_PJ_DAC_RequestForInformationRelation, RequestForInformationRelation
Non-filterable, non-selectable: BusinessAccountCd, BusinessAccountName, ContactName, ContactEmail

PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.RequestForInformationRelationId : Edm.Int32 [key] "RequestForInformationRelationId"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.RequestForInformationNoteId : Edm.Guid
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.Role : Edm.String "Role"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.IsPrimary : Edm.Boolean [required] "Primary"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.Type : Edm.String "Type"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.DocumentNoteId : Edm.Guid "Document"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.BusinessAccountId : Edm.Int32 "Account"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.BusinessAccountCd : Edm.String "Account/Employee"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.ContactId : Edm.Int32 "Contact"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.AddToCc : Edm.Boolean "Add to CC"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.BusinessAccountName : Edm.String "Name"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.ContactName : Edm.String "Contact"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.ContactEmail : Edm.String "Email"
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.BAccountByRequestForInformationNoteId -> PX.Objects.CR.BAccount (RequestForInformationNoteId=NoteID)
PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation.ContactByRequestForInformationNoteId -> PX.Objects.CR.Contact (RequestForInformationNoteId=NoteID)

# PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal (EntityType)

Label: "Submittal"
Key: RevisionID, SubmittalID
Entity sets: PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittal, Submittal, PJSubmittal
Non-filterable, non-selectable: DaysOverdue, WorkgroupID, FormCaptionDescription, NoteText

PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.SubmittalID : Edm.String [key] "Submittal ID"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.RevisionID : Edm.Int32 [key required] "Revision ID"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.TypeID : Edm.Int32 "Submittal Type"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.Summary : Edm.String "Summary"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.Status : Edm.String "Status"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.Reason : Edm.String "Reason"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.IsLastRevision : Edm.Boolean [required]
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.SpecificationInfo : Edm.String "Specification"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.SpecificationSection : Edm.String "Specification Section"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.DateOnSite : Edm.DateTimeOffset "Date Required on Site"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.DateCreated : Edm.DateTimeOffset "Date Created"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.DateClosed : Edm.DateTimeOffset "Date Closed"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.DaysOverdue : Edm.Int32 "Days Overdue"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.OwnerID : Edm.Int32 "Owner"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.WorkgroupID : Edm.Int32
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.CurrentWorkflowItemContactID : Edm.Int32 "Ball in Court"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.CurrentWorkflowItemLineNbr : Edm.Int32
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.Description : Edm.String "Description"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.FormCaptionDescription : Edm.String
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.NoteID : Edm.Guid
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.NoteText : Edm.String "Note Text"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.Tstamp : Edm.Binary
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.CreatedById : Edm.Guid "Created By"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.CreatedByScreenId : Edm.String
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.LastModifiedByScreenId : Edm.String
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.PMProjectByProjectId -> PX.Objects.PM.PMProject
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.PMTaskByProjectTaskId -> PX.Objects.PM.PMTask
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.PMTaskByProjectId -> PX.Objects.PM.PMTask
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.ContactByCurrentWorkflowItemContactID -> PX.Objects.CR.Contact (CurrentWorkflowItemContactID=ContactID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.UsersByLastModifiedById -> PX.SM.Users (LastModifiedById=PKID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.PJSubmittalTypeByTypeID -> PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType (TypeID=SubmittalTypeID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal.PJSubmittalWorkflowItemCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem)

# PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType (EntityType)

Label: "Submittal Type"
Key: SubmittalTypeID
Entity sets: PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittalType, SubmittalType, PJSubmittalType

PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.SubmittalTypeID : Edm.Int32 [key]
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.TypeName : Edm.String "Submittal Type"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.Description : Edm.String "Description"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.tstamp : Edm.Binary
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.CreatedByID : Edm.Guid "Created By"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.CreatedByScreenID : Edm.String
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.LastModifiedByScreenID : Edm.String
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalType.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)

# PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem (EntityType)

Label: "Submittal Workflow Item"
Key: LineNbr, RevisionID, SubmittalID
Entity sets: PX_Objects_PJ_Submittals_PJ_DAC_PJSubmittalWorkflowItem, SubmittalWorkflowItem, PJSubmittalWorkflowItem
Non-filterable, non-selectable: CanDelete, NoteText

PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.SubmittalID : Edm.String [key]
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.RevisionID : Edm.Int32 [key]
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.ContactID : Edm.Int32 "Contact"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.Role : Edm.String "Role"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.Status : Edm.String "Status"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.DaysForReview : Edm.Int32 "Days for Review"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.CompletionDate : Edm.DateTimeOffset "Completion Date"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.DateReceived : Edm.DateTimeOffset "Date Received"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.DateSent : Edm.DateTimeOffset "Date Sent"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.CanDelete : Edm.Boolean
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.EmailTo : Edm.Boolean [required] "EmailTo"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.NoteID : Edm.Guid
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.NoteText : Edm.String "Note Text"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.tstamp : Edm.Binary
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.CreatedByScreenID : Edm.String
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.LastModifiedByScreenID : Edm.String
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.PJSubmittalByRevisionID -> PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal (SubmittalID=SubmittalID, RevisionID=RevisionID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittalWorkflowItem.ContactForCurrentProjectByContactID -> PX.Objects.PJ.Common.DAC.ContactForCurrentProject (ContactID=ContactID)

# PX.Objects.PM.DAC.PMItemCostStatusByCostCenter (EntityType)

Label: "Item Cost Status by Cost Center"
Key: CostCenterID, InventoryID, SiteID
Entity sets: PX_Objects_PM_DAC_PMItemCostStatusByCostCenter, ItemCostStatusbyCostCenter, PMItemCostStatusByCostCenter

PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.InventoryID : Edm.Int32 [key]
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.CostCenterID : Edm.Int32 [key]
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.SiteID : Edm.Int32 [key]
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.QtyOnHand : Edm.Decimal
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.TotalCost : Edm.Decimal
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.INSiteByCostSiteID -> PX.Objects.IN.INSite
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.INSiteStatusSelectedCollection -> Collection(PX.Objects.IN.INSiteStatusSelected)
PX.Objects.PM.DAC.PMItemCostStatusByCostCenter.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)

# PX.Objects.PM.DAC.PMReportRowsMultiplier (EntityType)

Label: "Report Rows Multiplier"
Key: RecordID
Entity sets: PX_Objects_PM_DAC_PMReportRowsMultiplier, ReportRowsMultiplier, PMReportRowsMultiplier
Non-filterable, non-selectable: RecordID

PX.Objects.PM.DAC.PMReportRowsMultiplier.RecordID : Edm.Int32 [key] "RecordID"
PX.Objects.PM.DAC.PMReportRowsMultiplier.RowsCount : Edm.Int32
PX.Objects.PM.DAC.PMReportRowsMultiplier.RowNumber : Edm.Int32

# PX.Objects.PM.DAC.PMSelectedTag (EntityType)

Label: "Project Selected Tag"
BaseType: PX.Data.Wiki.Tags.Tag
Key: TagID (inherited from PX.Data.Wiki.Tags.Tag)
Entity sets: PX_Objects_PM_DAC_PMSelectedTag, ProjectSelectedTag, PMSelectedTag

# PX.Objects.PM.DAC.PMTagTemplate (EntityType)

Label: "Project Tag Template"
Key: TemplateCD
Entity sets: PX_Objects_PM_DAC_PMTagTemplate, ProjectTagTemplate, PMTagTemplate
Non-filterable, non-selectable: NoteText

PX.Objects.PM.DAC.PMTagTemplate.TemplateID : Edm.Guid "TemplateID"
PX.Objects.PM.DAC.PMTagTemplate.TemplateCD : Edm.String [key] "Template ID"
PX.Objects.PM.DAC.PMTagTemplate.DisplayNameTagTemplateCD : Edm.String
PX.Objects.PM.DAC.PMTagTemplate.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.DAC.PMTagTemplate.IsCustom : Edm.Boolean [required]
PX.Objects.PM.DAC.PMTagTemplate.Description : Edm.String "Description"
PX.Objects.PM.DAC.PMTagTemplate.NoteID : Edm.Guid
PX.Objects.PM.DAC.PMTagTemplate.NoteText : Edm.String "Note Text"
PX.Objects.PM.DAC.PMTagTemplate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.DAC.PMTagTemplate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.DAC.PMTagTemplate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.DAC.PMTagTemplate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.DAC.PMTagTemplate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.DAC.PMTagTemplate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.DAC.PMTagTemplate.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.DAC.PMTagTemplate.PMTagTemplateItemCollection -> Collection(PX.Objects.PM.DAC.PMTagTemplateItem)

# PX.Objects.PM.DAC.PMTagTemplateItem (EntityType)

Label: "Project Tag"
Key: TagID, TemplateID
Entity sets: PX_Objects_PM_DAC_PMTagTemplateItem, ProjectTag, PMTagTemplateItem
Non-filterable, non-selectable: TagCD, Description

PX.Objects.PM.DAC.PMTagTemplateItem.TemplateID : Edm.Guid [key] "Tag Template ID"
PX.Objects.PM.DAC.PMTagTemplateItem.TagID : Edm.Guid [key]
PX.Objects.PM.DAC.PMTagTemplateItem.TagCD : Edm.String "Tag Name"
PX.Objects.PM.DAC.PMTagTemplateItem.ParentTagID : Edm.Guid "Parent Tag"
PX.Objects.PM.DAC.PMTagTemplateItem.Description : Edm.String "Description"
PX.Objects.PM.DAC.PMTagTemplateItem.SortOrder : Edm.Int32 [required] "Sort Order"
PX.Objects.PM.DAC.PMTagTemplateItem.PMTagTemplateByTemplateID -> PX.Objects.PM.DAC.PMTagTemplate (TemplateID=TemplateID)

# PX.Objects.PM.DAC.Reports.PMRegister (EntityType)

Label: "Project Register"
Key: Module, RefNbr
Entity sets: PX_Objects_PM_DAC_Reports_PMRegister, ProjectRegister, PMRegister
Non-filterable, non-selectable: NoteText

PX.Objects.PM.DAC.Reports.PMRegister.Module : Edm.String [key] "Source"
PX.Objects.PM.DAC.Reports.PMRegister.RefNbr : Edm.String [key] "Ref. Number"
PX.Objects.PM.DAC.Reports.PMRegister.OrigNoteID : Edm.Guid "Orig. Doc. Nbr."
PX.Objects.PM.DAC.Reports.PMRegister.NoteID : Edm.Guid
PX.Objects.PM.DAC.Reports.PMRegister.NoteText : Edm.String "Note Text"
PX.Objects.PM.DAC.Reports.PMRegister.PMTranCollection -> Collection(PX.Objects.PM.PMTran)

# PX.Objects.PM.Lite.PMBudget (EntityType)

Label: "Budget"
Key: AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_PM_Lite_PMBudget, Budget1, PMBudget

PX.Objects.PM.Lite.PMBudget.ProjectID : Edm.Int32 [key]
PX.Objects.PM.Lite.PMBudget.ProjectTaskID : Edm.Int32 [key]
PX.Objects.PM.Lite.PMBudget.CostCodeID : Edm.Int32 [key]
PX.Objects.PM.Lite.PMBudget.AccountGroupID : Edm.Int32 [key]
PX.Objects.PM.Lite.PMBudget.InventoryID : Edm.Int32 [key]
PX.Objects.PM.Lite.PMBudget.Qty : Edm.Decimal [required]
PX.Objects.PM.Lite.PMBudget.UOM : Edm.String
PX.Objects.PM.Lite.PMBudget.CuryRevisedAmount : Edm.Decimal
PX.Objects.PM.Lite.PMBudget.CuryActualAmount : Edm.Decimal
PX.Objects.PM.Lite.PMBudget.CuryCommittedOpenAmount : Edm.Decimal
PX.Objects.PM.Lite.PMBudget.Type : Edm.String
PX.Objects.PM.Lite.PMBudget.Description : Edm.String
PX.Objects.PM.Lite.PMBudget.IsProduction : Edm.Boolean [required]
PX.Objects.PM.Lite.PMBudget.ProgressBillingBase : Edm.String
PX.Objects.PM.Lite.PMBudget.RevenueTaskID : Edm.Int32
PX.Objects.PM.Lite.PMBudget.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.Lite.PMBudget.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.PM.Lite.PMBudget.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PM.Lite.PMBudget.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.Lite.PMBudget.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.Lite.PMBudget.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PM.Lite.PMBudget.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory
PX.Objects.PM.Lite.PMBudget.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PM.Lite.PMBudget.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PM.Lite.PMBudget.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)

# PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument (ComplexType)


PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.ProjectID : Edm.Int32
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.LineNbr : Edm.Int32
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.InventoryID : Edm.Int32
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.DocumentType : Edm.String
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.DocNoteID : Edm.Guid
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.DocRefNbr : Edm.String
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.Status : Edm.String
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.DocumentDate : Edm.DateTimeOffset
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.InvtDocType : Edm.String
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.InvtRefNbr : Edm.String
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.Qty : Edm.Decimal
PX.Objects.PM.MaterialManagement.MaterialList.MaterialListForm.LinkedDocuments.PMMLLinkedDocument.UOM : Edm.String

# PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList (EntityType)

Label: "Material List"
Key: ProjectID
Entity sets: PX_Objects_PM_MaterialManagement_MaterialList_PMMaterialList, MaterialList2, PMMaterialList

PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList.NoteID : Edm.Guid
PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList.LineCounter : Edm.Int32 [required]
PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList.CustomerID : Edm.Int32
PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList.CustomerLocationID : Edm.Int32
PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)

# PX.Objects.PM.PMAccountGroup (EntityType)

Label: "Account Group"
Key: GroupCD
Entity sets: PX_Objects_PM_PMAccountGroup, AccountGroup, PMAccountGroup
Non-filterable, non-selectable: Included, ClassID, NoteText, Secured

PX.Objects.PM.PMAccountGroup.GroupID : Edm.Int32
PX.Objects.PM.PMAccountGroup.GroupCD : Edm.String [key] "Account Group ID"
PX.Objects.PM.PMAccountGroup.Description : Edm.String "Description"
PX.Objects.PM.PMAccountGroup.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMAccountGroup.IsExpense : Edm.Boolean [required] "Expense"
PX.Objects.PM.PMAccountGroup.RevenueAccountGroupID : Edm.Int32 "Default Revenue Account Group"
PX.Objects.PM.PMAccountGroup.DefaultUOM : Edm.String "Default UOM"
PX.Objects.PM.PMAccountGroup.Type : Edm.String "Type"
PX.Objects.PM.PMAccountGroup.ReportGroup : Edm.String "Reporting Group"
PX.Objects.PM.PMAccountGroup.CalculateProjectedCostByQuantity : Edm.Boolean [required] "Calculate Projected Cost by Quantity"
PX.Objects.PM.PMAccountGroup.AccountID : Edm.Int32
PX.Objects.PM.PMAccountGroup.SortOrder : Edm.Int16 "Sort Order"
PX.Objects.PM.PMAccountGroup.Included : Edm.Boolean "Included"
PX.Objects.PM.PMAccountGroup.ClassID : Edm.String
PX.Objects.PM.PMAccountGroup.NoteID : Edm.Guid
PX.Objects.PM.PMAccountGroup.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMAccountGroup.tstamp : Edm.Binary
PX.Objects.PM.PMAccountGroup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMAccountGroup.CreatedByScreenID : Edm.String
PX.Objects.PM.PMAccountGroup.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMAccountGroup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMAccountGroup.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMAccountGroup.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMAccountGroup.Secured : Edm.Boolean "Secured"
PX.Objects.PM.PMAccountGroup.PMAccountGroupByRevenueAccountGroupID -> PX.Objects.PM.PMAccountGroup (RevenueAccountGroupID=GroupID)
PX.Objects.PM.PMAccountGroup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMAccountGroup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMAccountGroup.INUnitByDefaultUOM -> PX.Objects.IN.INUnit (DefaultUOM=FromUnit)
PX.Objects.PM.PMAccountGroup.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.PM.PMAccountGroup.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMAccountGroup.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.PM.PMAccountGroup.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.PM.PMAccountGroup.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.PM.PMAccountGroup.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.PM.PMAccountGroup.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMAccountGroup.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.PM.PMAccountGroup.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.PM.PMAccountGroup.PMAccountGroupCollection -> Collection(PX.Objects.PM.PMAccountGroup)
PX.Objects.PM.PMAccountGroup.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.PM.PMAccountGroup.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.PM.PMAccountGroup.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.PM.PMAccountGroup.PRSetupCollection -> Collection(PX.Objects.PR.PRSetup)
PX.Objects.PM.PMAccountGroup.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.PM.PMAccountGroup.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.Objects.PM.PMAccountGroup.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.PM.PMAccountGroup.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.PM.PMAccountGroup.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.PM.PMAccountGroup.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.PM.PMAccountGroup.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.PM.PMAccountGroup.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.PM.PMAccountGroup.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.PM.PMAccountGroup.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.PM.PMAccountGroup.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.PM.PMAccountGroup.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.PM.PMAccountGroup.PMProgressLineTotalCollection -> Collection(PX.Objects.PM.PMProgressLineTotal)
PX.Objects.PM.PMAccountGroup.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.PM.PMAccountGroup.PMAccountGroupRateCollection -> Collection(PX.Objects.PM.PMAccountGroupRate)
PX.Objects.PM.PMAccountGroup.PMTransferRuleAccountGroupMapCollection -> Collection(PX.Objects.PM.PMTransferRuleAccountGroupMap)

# PX.Objects.PM.PMAccountGroupRate (EntityType)

Label: "PM Account Group Rate"
Key: AccountGroupID, RateCodeID, RateDefinitionID
Entity sets: PX_Objects_PM_PMAccountGroupRate, PMAccountGroupRate

PX.Objects.PM.PMAccountGroupRate.RateDefinitionID : Edm.Int32 [key]
PX.Objects.PM.PMAccountGroupRate.RateCodeID : Edm.String [key]
PX.Objects.PM.PMAccountGroupRate.AccountGroupID : Edm.Int32 [key] "Account Group"
PX.Objects.PM.PMAccountGroupRate.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMAccountGroupRate.PMRateSequenceByRateCodeID -> PX.Objects.PM.PMRateSequence (RateDefinitionID=RateDefinitionID, RateCodeID=RateCodeID)

# PX.Objects.PM.PMAccountTask (EntityType)

Label: "PM Account Task"
Key: AccountID, ProjectID
Entity sets: PX_Objects_PM_PMAccountTask, PMAccountTask
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMAccountTask.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMAccountTask.AccountID : Edm.Int32 [key] "Account"
PX.Objects.PM.PMAccountTask.NoteID : Edm.Guid
PX.Objects.PM.PMAccountTask.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMAccountTask.tstamp : Edm.Binary
PX.Objects.PM.PMAccountTask.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMAccountTask.CreatedByScreenID : Edm.String
PX.Objects.PM.PMAccountTask.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMAccountTask.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMAccountTask.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMAccountTask.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMAccountTask.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMAccountTask.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMAccountTask.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMAccountTask.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMAccountTask.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)

# PX.Objects.PM.PMAddress (EntityType)

Label: "PM Address"
Key: AddressID
Entity sets: PX_Objects_PM_PMAddress, PMAddress
Non-filterable, non-selectable: BAccountID, OverrideAddress

PX.Objects.PM.PMAddress.AddressID : Edm.Int32 [key] "Address ID"
PX.Objects.PM.PMAddress.CustomerID : Edm.Int32
PX.Objects.PM.PMAddress.BAccountID : Edm.Int32
PX.Objects.PM.PMAddress.CustomerAddressID : Edm.Int32
PX.Objects.PM.PMAddress.IsDefaultBillAddress : Edm.Boolean [required] "Customer Default"
PX.Objects.PM.PMAddress.OverrideAddress : Edm.Boolean "Override Address"
PX.Objects.PM.PMAddress.RevisionID : Edm.Int32
PX.Objects.PM.PMAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.PM.PMAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.PM.PMAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.PM.PMAddress.City : Edm.String "City"
PX.Objects.PM.PMAddress.CountryID : Edm.String "Country"
PX.Objects.PM.PMAddress.State : Edm.String "State"
PX.Objects.PM.PMAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.PM.PMAddress.Department : Edm.String "Department"
PX.Objects.PM.PMAddress.SubDepartment : Edm.String "Subdepartment"
PX.Objects.PM.PMAddress.StreetName : Edm.String "Street Name"
PX.Objects.PM.PMAddress.BuildingNumber : Edm.String "Building Number"
PX.Objects.PM.PMAddress.BuildingName : Edm.String "Building Name"
PX.Objects.PM.PMAddress.Floor : Edm.String "Floor"
PX.Objects.PM.PMAddress.UnitNumber : Edm.String "Unit Number"
PX.Objects.PM.PMAddress.PostBox : Edm.String "Post Box"
PX.Objects.PM.PMAddress.Room : Edm.String "Room"
PX.Objects.PM.PMAddress.TownLocationName : Edm.String "Town Location Name"
PX.Objects.PM.PMAddress.DistrictName : Edm.String "District Name"
PX.Objects.PM.PMAddress.AddressType : Edm.String "Address Type"
PX.Objects.PM.PMAddress.CareOf : Edm.String "Care Of"
PX.Objects.PM.PMAddress.NoteID : Edm.Guid
PX.Objects.PM.PMAddress.tstamp : Edm.Binary
PX.Objects.PM.PMAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMAddress.CreatedByScreenID : Edm.String
PX.Objects.PM.PMAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMAddress.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMAddress.Latitude : Edm.Decimal "Latitude"
PX.Objects.PM.PMAddress.Longitude : Edm.Decimal "Longitude"
PX.Objects.PM.PMAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PM.PMAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)

# PX.Objects.PM.PMAllocation (EntityType)

Label: "Allocation Rule"
Key: AllocationID
Entity sets: PX_Objects_PM_PMAllocation, AllocationRule, PMAllocation
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMAllocation.AllocationID : Edm.String [key] "Allocation Rule"
PX.Objects.PM.PMAllocation.Description : Edm.String "Description"
PX.Objects.PM.PMAllocation.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMAllocation.NoteID : Edm.Guid
PX.Objects.PM.PMAllocation.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMAllocation.tstamp : Edm.Binary
PX.Objects.PM.PMAllocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMAllocation.CreatedByScreenID : Edm.String
PX.Objects.PM.PMAllocation.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMAllocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMAllocation.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMAllocation.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMAllocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMAllocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMAllocation.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMAllocation.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMAllocation.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)

# PX.Objects.PM.PMAllocationAuditTran (EntityType)

Label: "PM Allocation Audit Transaction"
Key: AllocationID, SourceTranID, TranID
Entity sets: PX_Objects_PM_PMAllocationAuditTran, PMAllocationAuditTransaction, PMAllocationAuditTran

PX.Objects.PM.PMAllocationAuditTran.AllocationID : Edm.String [key]
PX.Objects.PM.PMAllocationAuditTran.TranID : Edm.Int64 [key]
PX.Objects.PM.PMAllocationAuditTran.SourceTranID : Edm.Int64 [key]

# PX.Objects.PM.PMAllocationDetail (EntityType)

Label: "Allocation Rule Step"
Key: AllocationID, StepID
Entity sets: PX_Objects_PM_PMAllocationDetail, AllocationRuleStep, PMAllocationDetail
Non-filterable, non-selectable: FullDetail, Allocation, AllocationText, NoteText

PX.Objects.PM.PMAllocationDetail.AllocationID : Edm.String [key]
PX.Objects.PM.PMAllocationDetail.StepID : Edm.Int32 [key] "Step ID"
PX.Objects.PM.PMAllocationDetail.Description : Edm.String "Description"
PX.Objects.PM.PMAllocationDetail.SelectOption : Edm.String "Select Transactions"
PX.Objects.PM.PMAllocationDetail.Post : Edm.Boolean [required] "Create Allocation Transaction"
PX.Objects.PM.PMAllocationDetail.QtyFormula : Edm.String "Quantity Formula"
PX.Objects.PM.PMAllocationDetail.BillableQtyFormula : Edm.String "Billable Qty. Formula"
PX.Objects.PM.PMAllocationDetail.AmountFormula : Edm.String "Amount Formula"
PX.Objects.PM.PMAllocationDetail.DescriptionFormula : Edm.String "Description Formula"
PX.Objects.PM.PMAllocationDetail.RangeStart : Edm.Int32 "Range Start"
PX.Objects.PM.PMAllocationDetail.RangeEnd : Edm.Int32 "Range End"
PX.Objects.PM.PMAllocationDetail.RateTypeID : Edm.String "Rate Type"
PX.Objects.PM.PMAllocationDetail.AccountGroupFrom : Edm.Int32 "Account Group From"
PX.Objects.PM.PMAllocationDetail.AccountGroupTo : Edm.Int32 "Account Group To"
PX.Objects.PM.PMAllocationDetail.Method : Edm.String "Allocation Method"
PX.Objects.PM.PMAllocationDetail.UpdateGL : Edm.Boolean [required] "Post Transaction to GL"
PX.Objects.PM.PMAllocationDetail.SourceBranchID : Edm.Int32 "Branch"
PX.Objects.PM.PMAllocationDetail.TargetBranchID : Edm.Int32 "Replace Branch With"
PX.Objects.PM.PMAllocationDetail.ProjectOrigin : Edm.String "Project"
PX.Objects.PM.PMAllocationDetail.TaskOrigin : Edm.String "Project Task"
PX.Objects.PM.PMAllocationDetail.TaskCD : Edm.String "TaskCD"
PX.Objects.PM.PMAllocationDetail.AccountGroupOrigin : Edm.String "Account Group"
PX.Objects.PM.PMAllocationDetail.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMAllocationDetail.AccountOrigin : Edm.String "Account Origin"
PX.Objects.PM.PMAllocationDetail.OffsetProjectOrigin : Edm.String "Project"
PX.Objects.PM.PMAllocationDetail.OffsetTaskOrigin : Edm.String "Project Task"
PX.Objects.PM.PMAllocationDetail.OffsetTaskCD : Edm.String "Project Task"
PX.Objects.PM.PMAllocationDetail.OffsetAccountGroupOrigin : Edm.String "Account Group"
PX.Objects.PM.PMAllocationDetail.OffsetAccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMAllocationDetail.OffsetAccountOrigin : Edm.String "Account Origin"
PX.Objects.PM.PMAllocationDetail.Reverse : Edm.String "Reverse Allocation"
PX.Objects.PM.PMAllocationDetail.UseReversalDateFromOriginal : Edm.Boolean [required] "Use Reversal Date from Original Transaction"
PX.Objects.PM.PMAllocationDetail.NoRateOption : Edm.String "If @Rate Is Not Defined"
PX.Objects.PM.PMAllocationDetail.DateSource : Edm.String "Date Source"
PX.Objects.PM.PMAllocationDetail.GroupByItem : Edm.Boolean [required] "By Item"
PX.Objects.PM.PMAllocationDetail.GroupByEmployee : Edm.Boolean [required] "By Employee"
PX.Objects.PM.PMAllocationDetail.GroupByDate : Edm.Boolean [required] "By Date"
PX.Objects.PM.PMAllocationDetail.GroupByVendor : Edm.Boolean [required] "By Vendor"
PX.Objects.PM.PMAllocationDetail.FullDetail : Edm.Boolean
PX.Objects.PM.PMAllocationDetail.Allocation : Edm.Int32 "Allocation"
PX.Objects.PM.PMAllocationDetail.AllocationText : Edm.String
PX.Objects.PM.PMAllocationDetail.AllocateZeroAmount : Edm.Boolean [required] "Create Transaction with Zero Amount"
PX.Objects.PM.PMAllocationDetail.AllocateZeroQty : Edm.Boolean [required] "Create Transaction with Zero Qty."
PX.Objects.PM.PMAllocationDetail.AllocateNonBillable : Edm.Boolean [required] "Allocate Non-Billable Transactions"
PX.Objects.PM.PMAllocationDetail.MarkAsNotAllocated : Edm.Boolean [required] "Can Be Used as a Source in Another Allocation"
PX.Objects.PM.PMAllocationDetail.CopyNotes : Edm.Boolean [required] "Copy Notes"
PX.Objects.PM.PMAllocationDetail.NoteID : Edm.Guid
PX.Objects.PM.PMAllocationDetail.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMAllocationDetail.tstamp : Edm.Binary
PX.Objects.PM.PMAllocationDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMAllocationDetail.CreatedByScreenID : Edm.String
PX.Objects.PM.PMAllocationDetail.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMAllocationDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMAllocationDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMAllocationDetail.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMAllocationDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMAllocationDetail.PMProjectByOffsetProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMAllocationDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMAllocationDetail.PMTaskByOffsetProjectID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMAllocationDetail.PMAccountGroupByAccountGroupFrom -> PX.Objects.PM.PMAccountGroup (AccountGroupFrom=GroupID)
PX.Objects.PM.PMAllocationDetail.PMAccountGroupByAccountGroupTo -> PX.Objects.PM.PMAccountGroup (AccountGroupTo=GroupID)
PX.Objects.PM.PMAllocationDetail.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMAllocationDetail.PMAccountGroupByOffsetAccountGroupID -> PX.Objects.PM.PMAccountGroup (OffsetAccountGroupID=GroupID)
PX.Objects.PM.PMAllocationDetail.BranchBySourceBranchID -> PX.Objects.GL.Branch (SourceBranchID=BranchID)
PX.Objects.PM.PMAllocationDetail.BranchByTargetBranchID -> PX.Objects.GL.Branch (TargetBranchID=BranchID)
PX.Objects.PM.PMAllocationDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMAllocationDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMAllocationDetail.PMAllocationByAllocationID -> PX.Objects.PM.PMAllocation (AllocationID=AllocationID)
PX.Objects.PM.PMAllocationDetail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMAllocationDetail.PMCostCodeByOffsetCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMAllocationDetail.PMRateTypeByRateTypeID -> PX.Objects.PM.PMRateType (RateTypeID=RateTypeID)
PX.Objects.PM.PMAllocationDetail.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMAllocationDetail.AccountByOffsetAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMAllocationDetail.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMAllocationDetail.SubByOffsetSubID -> PX.Objects.GL.Sub

# PX.Objects.PM.PMAllocationSourceTran (EntityType)

Label: "PM Allocation Source Transaction"
Key: AllocationID, StepID, TranID
Entity sets: PX_Objects_PM_PMAllocationSourceTran, PMAllocationSourceTransaction, PMAllocationSourceTran

PX.Objects.PM.PMAllocationSourceTran.AllocationID : Edm.String [key] "Allocation ID"
PX.Objects.PM.PMAllocationSourceTran.StepID : Edm.Int32 [key]
PX.Objects.PM.PMAllocationSourceTran.TranID : Edm.Int64 [key]
PX.Objects.PM.PMAllocationSourceTran.Rate : Edm.Decimal [required]
PX.Objects.PM.PMAllocationSourceTran.Qty : Edm.Decimal [required]
PX.Objects.PM.PMAllocationSourceTran.Amount : Edm.Decimal [required]
PX.Objects.PM.PMAllocationSourceTran.tstamp : Edm.Binary
PX.Objects.PM.PMAllocationSourceTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMAllocationSourceTran.CreatedByScreenID : Edm.String
PX.Objects.PM.PMAllocationSourceTran.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMAllocationSourceTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMAllocationSourceTran.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMAllocationSourceTran.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMAllocationSourceTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMAllocationSourceTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PM.PMBilling (EntityType)

Label: "Billing Rule"
Key: BillingID
Entity sets: PX_Objects_PM_PMBilling, BillingRule, PMBilling
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMBilling.BillingID : Edm.String [key] "Billing Rule"
PX.Objects.PM.PMBilling.Description : Edm.String "Description"
PX.Objects.PM.PMBilling.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMBilling.NoteID : Edm.Guid
PX.Objects.PM.PMBilling.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMBilling.tstamp : Edm.Binary
PX.Objects.PM.PMBilling.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMBilling.CreatedByScreenID : Edm.String
PX.Objects.PM.PMBilling.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMBilling.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMBilling.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMBilling.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMBilling.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMBilling.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMBilling.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMBilling.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMBilling.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)

# PX.Objects.PM.PMBillingAddress (EntityType)

Label: "PM Billing Address"
BaseType: PX.Objects.PM.PMAddress
Key: AddressID (inherited from PX.Objects.PM.PMAddress)
Entity sets: PX_Objects_PM_PMBillingAddress, PMBillingAddress

# PX.Objects.PM.PMBillingContact (EntityType)

Label: "PM Billing Contact"
BaseType: PX.Objects.PM.PMContact
Key: ContactID (inherited from PX.Objects.PM.PMContact)
Entity sets: PX_Objects_PM_PMBillingContact, PMBillingContact

# PX.Objects.PM.PMBillingRecord (EntityType)

Label: "Project Billing Record"
Key: BillingTag, ProjectID, RecordID
Entity sets: PX_Objects_PM_PMBillingRecord, ProjectBillingRecord, PMBillingRecord
Non-filterable, non-selectable: SortOrder, RecordNumber

PX.Objects.PM.PMBillingRecord.ProjectID : Edm.Int32 [key] "Project ID"
PX.Objects.PM.PMBillingRecord.RecordID : Edm.Int32 [key] "Billing Number"
PX.Objects.PM.PMBillingRecord.BillingTag : Edm.String [key required]
PX.Objects.PM.PMBillingRecord.Date : Edm.DateTimeOffset "Pro Forma Date"
PX.Objects.PM.PMBillingRecord.ProformaRefNbr : Edm.String "Pro Forma Reference Nbr."
PX.Objects.PM.PMBillingRecord.ARDocType : Edm.String "AR Doc. Type"
PX.Objects.PM.PMBillingRecord.ARRefNbr : Edm.String "AR Reference Nbr."
PX.Objects.PM.PMBillingRecord.SortOrder : Edm.Int32
PX.Objects.PM.PMBillingRecord.tstamp : Edm.Binary
PX.Objects.PM.PMBillingRecord.RecordNumber : Edm.Int32 "Billing Number"
PX.Objects.PM.PMBillingRecord.ARInvoiceByARRefNbr -> PX.Objects.AR.ARInvoice (ARRefNbr=RefNbr)
PX.Objects.PM.PMBillingRecord.PMProformaByProjectID -> PX.Objects.PM.PMProforma (ProformaRefNbr=RefNbr)

# PX.Objects.PM.PMBillingRule (EntityType)

Label: "Billing Rule Step"
Key: BillingID, StepID
Entity sets: PX_Objects_PM_PMBillingRule, BillingRuleStep, PMBillingRule
Non-filterable, non-selectable: BranchSourceBudget, IncludeZeroAmount, NoteText

PX.Objects.PM.PMBillingRule.BillingID : Edm.String [key]
PX.Objects.PM.PMBillingRule.StepID : Edm.Int32 [key] "Step ID"
PX.Objects.PM.PMBillingRule.Description : Edm.String "Description"
PX.Objects.PM.PMBillingRule.Type : Edm.String "Billing Type"
PX.Objects.PM.PMBillingRule.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMBillingRule.InvoiceGroup : Edm.String "Invoice Group"
PX.Objects.PM.PMBillingRule.BranchSource : Edm.String "Use Destination Branch From"
PX.Objects.PM.PMBillingRule.BranchSourceBudget : Edm.String "Use Destination Branch From"
PX.Objects.PM.PMBillingRule.TargetBranchID : Edm.Int32 "Destination Branch"
PX.Objects.PM.PMBillingRule.AccountSource : Edm.String "Use Sales Account From"
PX.Objects.PM.PMBillingRule.IncludeNonBillable : Edm.Boolean [required] "Include Non-Billable Transactions"
PX.Objects.PM.PMBillingRule.CopyNotes : Edm.Boolean [required] "Copy Notes and Files"
PX.Objects.PM.PMBillingRule.RateTypeID : Edm.String "Rate Type"
PX.Objects.PM.PMBillingRule.NoRateOption : Edm.String "If @Rate Is Not Defined"
PX.Objects.PM.PMBillingRule.InvoiceFormula : Edm.String "Invoice Description Formula"
PX.Objects.PM.PMBillingRule.QtyFormula : Edm.String "Line Quantity Formula"
PX.Objects.PM.PMBillingRule.AmountFormula : Edm.String "Line Amount Formula"
PX.Objects.PM.PMBillingRule.DescriptionFormula : Edm.String "Line Description Formula"
PX.Objects.PM.PMBillingRule.GroupByItem : Edm.Boolean [required] "Inventory ID"
PX.Objects.PM.PMBillingRule.GroupByEmployee : Edm.Boolean [required] "Employee"
PX.Objects.PM.PMBillingRule.GroupByDate : Edm.Boolean [required] "Date"
PX.Objects.PM.PMBillingRule.GroupByVendor : Edm.Boolean [required] "Vendor"
PX.Objects.PM.PMBillingRule.IncludeZeroAmountAndQty : Edm.Boolean [required] "Create Lines with Zero Amount and Quantity"
PX.Objects.PM.PMBillingRule.IncludeZeroAmount : Edm.Boolean "Create Lines with Zero Amount and Quantity"
PX.Objects.PM.PMBillingRule.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMBillingRule.NoteID : Edm.Guid
PX.Objects.PM.PMBillingRule.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMBillingRule.tstamp : Edm.Binary
PX.Objects.PM.PMBillingRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMBillingRule.CreatedByScreenID : Edm.String
PX.Objects.PM.PMBillingRule.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMBillingRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMBillingRule.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMBillingRule.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMBillingRule.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMBillingRule.BranchByTargetBranchID -> PX.Objects.GL.Branch (TargetBranchID=BranchID)
PX.Objects.PM.PMBillingRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMBillingRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMBillingRule.PMBillingByBillingID -> PX.Objects.PM.PMBilling (BillingID=BillingID)
PX.Objects.PM.PMBillingRule.PMRateTypeByRateTypeID -> PX.Objects.PM.PMRateType (RateTypeID=RateTypeID)
PX.Objects.PM.PMBillingRule.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMBillingRule.SubBySubID -> PX.Objects.GL.Sub

# PX.Objects.PM.PMBudget (EntityType)

Label: "Project Budget"
Key: AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_PM_PMBudget, ProjectBudget, PMBudget1
Non-filterable, non-selectable: RevenueTaskIDApiEndPoint, CuryActualPlusOpenCommittedAmount, ActualPlusOpenCommittedAmount, CuryVarianceAmount, VarianceAmount, Performance, SortOrder, NoteText, CuryRate

PX.Objects.PM.PMBudget.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMBudget.ProjectTaskID : Edm.Int32 [key]
PX.Objects.PM.PMBudget.CostCodeID : Edm.Int32 [key] "Cost Code"
PX.Objects.PM.PMBudget.AccountGroupID : Edm.Int32 [key] "Account Group"
PX.Objects.PM.PMBudget.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.PM.PMBudget.Type : Edm.String "Type"
PX.Objects.PM.PMBudget.RevenueTaskID : Edm.Int32 "Revenue Task"
PX.Objects.PM.PMBudget.RevenueTaskIDApiEndPoint : Edm.Int32
PX.Objects.PM.PMBudget.RevenueInventoryID : Edm.Int32
PX.Objects.PM.PMBudget.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.PMBudget.CuryInfoID : Edm.Int64
PX.Objects.PM.PMBudget.Description : Edm.String "Description"
PX.Objects.PM.PMBudget.Qty : Edm.Decimal [required] "Original Budgeted Quantity"
PX.Objects.PM.PMBudget.UOM : Edm.String "UOM"
PX.Objects.PM.PMBudget.CuryUnitRate : Edm.Decimal [required] "Unit Rate"
PX.Objects.PM.PMBudget.Rate : Edm.Decimal [required]
PX.Objects.PM.PMBudget.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.PM.PMBudget.UnitPrice : Edm.Decimal [required] "Unit Price in Base Currency"
PX.Objects.PM.PMBudget.CuryAmount : Edm.Decimal [required] "Original Budgeted Amount"
PX.Objects.PM.PMBudget.Amount : Edm.Decimal [required] "Original Budgeted Amount in Base Currency"
PX.Objects.PM.PMBudget.RevisedQty : Edm.Decimal [required] "Revised Budgeted Quantity"
PX.Objects.PM.PMBudget.CuryRevisedAmount : Edm.Decimal [required] "Revised Budgeted Amount"
PX.Objects.PM.PMBudget.RevisedAmount : Edm.Decimal [required] "Revised Budgeted Amount in Base Currency"
PX.Objects.PM.PMBudget.InvoicedQty : Edm.Decimal [required] "Draft Invoice Quantity"
PX.Objects.PM.PMBudget.CuryInvoicedAmount : Edm.Decimal [required] "Draft Invoice Amount"
PX.Objects.PM.PMBudget.InvoicedAmount : Edm.Decimal [required] "Draft Invoices Amount in Base Currency"
PX.Objects.PM.PMBudget.ActualQty : Edm.Decimal [required] "Actual Quantity"
PX.Objects.PM.PMBudget.CuryActualAmount : Edm.Decimal [required] "Actual Amount"
PX.Objects.PM.PMBudget.CuryInclTaxAmount : Edm.Decimal [required] "Inclusive Tax Amount"
PX.Objects.PM.PMBudget.InclTaxAmount : Edm.Decimal [required] "Inclusive Tax Amount in Base Currency"
PX.Objects.PM.PMBudget.CommittedQty : Edm.Decimal [required] "Revised Committed Quantity"
PX.Objects.PM.PMBudget.CuryCommittedAmount : Edm.Decimal [required] "Revised Committed Amount"
PX.Objects.PM.PMBudget.CommittedAmount : Edm.Decimal [required] "Revised Committed Amount in Base Currency"
PX.Objects.PM.PMBudget.CommittedOpenQty : Edm.Decimal [required] "Committed Open Quantity"
PX.Objects.PM.PMBudget.CuryCommittedOpenAmount : Edm.Decimal [required] "Committed Open Amount"
PX.Objects.PM.PMBudget.CommittedOpenAmount : Edm.Decimal [required] "Committed Open Amount in Base Currency"
PX.Objects.PM.PMBudget.CommittedReceivedQty : Edm.Decimal [required] "Committed Received Quantity"
PX.Objects.PM.PMBudget.CommittedInvoicedQty : Edm.Decimal [required] "Committed Invoiced Quantity"
PX.Objects.PM.PMBudget.CuryCommittedInvoicedAmount : Edm.Decimal [required] "Committed Invoiced Amount"
PX.Objects.PM.PMBudget.CommittedInvoicedAmount : Edm.Decimal [required] "Committed Invoiced Amount in Base Currency"
PX.Objects.PM.PMBudget.CuryActualPlusOpenCommittedAmount : Edm.Decimal "Actual + Open Committed Amount"
PX.Objects.PM.PMBudget.ActualPlusOpenCommittedAmount : Edm.Decimal "Actual + Open Committed Amount in Base Currency"
PX.Objects.PM.PMBudget.CuryVarianceAmount : Edm.Decimal "Variance Amount"
PX.Objects.PM.PMBudget.VarianceAmount : Edm.Decimal "Variance Amount in Base Currency"
PX.Objects.PM.PMBudget.Performance : Edm.Decimal "Performance (%)"
PX.Objects.PM.PMBudget.IsProduction : Edm.Boolean [required] "Autocompleted (%)"
PX.Objects.PM.PMBudget.Mode : Edm.String "Mode"
PX.Objects.PM.PMBudget.CompletedPct : Edm.Decimal [required] "Completed (%)"
PX.Objects.PM.PMBudget.QtyToInvoice : Edm.Decimal [required] "Pending Invoice Quantity"
PX.Objects.PM.PMBudget.CuryAmountToInvoice : Edm.Decimal [required] "Pending Invoice Amount"
PX.Objects.PM.PMBudget.AmountToInvoice : Edm.Decimal [required] "Pending Invoice Amount in Base Currency"
PX.Objects.PM.PMBudget.LimitQty : Edm.Boolean [required] "Limit Quantity"
PX.Objects.PM.PMBudget.LimitAmount : Edm.Boolean [required] "Limit Amount"
PX.Objects.PM.PMBudget.MaxQty : Edm.Decimal [required] "Maximum Quantity"
PX.Objects.PM.PMBudget.CuryMaxAmount : Edm.Decimal [required] "Maximum Amount"
PX.Objects.PM.PMBudget.MaxAmount : Edm.Decimal [required] "Maximum Amount in Base Currency"
PX.Objects.PM.PMBudget.CuryLastCostToComplete : Edm.Decimal [required] "Last Cost to Complete"
PX.Objects.PM.PMBudget.LastCostToComplete : Edm.Decimal [required] "Last Cost to Complete in Base Currency"
PX.Objects.PM.PMBudget.CuryCostToComplete : Edm.Decimal [required] "Cost to Complete"
PX.Objects.PM.PMBudget.CostToComplete : Edm.Decimal [required] "Cost To Complete in Base Currency"
PX.Objects.PM.PMBudget.LastPercentCompleted : Edm.Decimal [required] "Last Percentage of Completion"
PX.Objects.PM.PMBudget.PercentCompleted : Edm.Decimal [required] "Percentage of Completion"
PX.Objects.PM.PMBudget.CuryLastCostAtCompletion : Edm.Decimal [required] "Last Cost at Completion"
PX.Objects.PM.PMBudget.LastCostAtCompletion : Edm.Decimal [required] "Last Cost at Completion in Base Currency"
PX.Objects.PM.PMBudget.CuryCostAtCompletion : Edm.Decimal [required] "Cost at Completion"
PX.Objects.PM.PMBudget.CostAtCompletion : Edm.Decimal [required] "Cost at Completion"
PX.Objects.PM.PMBudget.LineCntr : Edm.Int32 [required]
PX.Objects.PM.PMBudget.SortOrder : Edm.Int32
PX.Objects.PM.PMBudget.ProgressBillingBase : Edm.String "Progress Billing Basis"
PX.Objects.PM.PMBudget.NoteID : Edm.Guid
PX.Objects.PM.PMBudget.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMBudget.tstamp : Edm.Binary
PX.Objects.PM.PMBudget.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMBudget.CreatedByScreenID : Edm.String
PX.Objects.PM.PMBudget.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMBudget.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMBudget.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMBudget.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMBudget.CuryRate : Edm.Decimal
PX.Objects.PM.PMBudget.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMBudget.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.PM.PMBudget.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PM.PMBudget.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMBudget.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMBudget.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMBudget.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PM.PMBudget.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PM.PMBudget.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PM.PMBudget.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)

# PX.Objects.PM.PMBudgetedCostCode (EntityType)

Label: "Budget"
Key: AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_PM_PMBudgetedCostCode, Budget2, PMBudgetedCostCode

PX.Objects.PM.PMBudgetedCostCode.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetedCostCode.ProjectTaskID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetedCostCode.CostCodeID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetedCostCode.AccountGroupID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetedCostCode.InventoryID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetedCostCode.Type : Edm.String
PX.Objects.PM.PMBudgetedCostCode.Description : Edm.String
PX.Objects.PM.PMBudgetedCostCode.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMBudgetedCostCode.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.PM.PMBudgetedCostCode.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PM.PMBudgetedCostCode.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMBudgetedCostCode.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMBudgetedCostCode.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PM.PMBudgetedCostCode.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)

# PX.Objects.PM.PMBudgetProduction (EntityType)

Label: "Budget Production"
Key: AccountGroupID, CostCodeID, InventoryID, LineNbr, ProjectID, ProjectTaskID
Entity sets: PX_Objects_PM_PMBudgetProduction, BudgetProduction, PMBudgetProduction
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMBudgetProduction.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetProduction.ProjectTaskID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetProduction.CostCodeID : Edm.Int32 [key] "Cost Code"
PX.Objects.PM.PMBudgetProduction.AccountGroupID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetProduction.InventoryID : Edm.Int32 [key]
PX.Objects.PM.PMBudgetProduction.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMBudgetProduction.CuryCostToComplete : Edm.Decimal [required] "Cost To Complete"
PX.Objects.PM.PMBudgetProduction.CostToComplete : Edm.Decimal [required] "Cost To Complete in Base Currency"
PX.Objects.PM.PMBudgetProduction.PercentCompleted : Edm.Decimal [required] "% Complete"
PX.Objects.PM.PMBudgetProduction.CuryCostAtCompletion : Edm.Decimal [required] "Cost At Completion"
PX.Objects.PM.PMBudgetProduction.CostAtCompletion : Edm.Decimal [required] "Cost At Completion in Base Currency"
PX.Objects.PM.PMBudgetProduction.NoteID : Edm.Guid
PX.Objects.PM.PMBudgetProduction.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMBudgetProduction.tstamp : Edm.Binary
PX.Objects.PM.PMBudgetProduction.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMBudgetProduction.CreatedByScreenID : Edm.String
PX.Objects.PM.PMBudgetProduction.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMBudgetProduction.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMBudgetProduction.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMBudgetProduction.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMBudgetProduction.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMBudgetProduction.PMBudgetByInventoryID -> PX.Objects.PM.PMBudget (ProjectID=ProjectID, ProjectTaskID=ProjectTaskID, AccountGroupID=AccountGroupID, CostCodeID=CostCodeID, InventoryID=InventoryID)
PX.Objects.PM.PMBudgetProduction.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.PM.PMBudgetProduction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMBudgetProduction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PM.PMChangeOrder (EntityType)

Label: "Change Order"
Key: RefNbr
Entity sets: PX_Objects_PM_PMChangeOrder, ChangeOrder, PMChangeOrder
Non-filterable, non-selectable: ChangeOrderTaskCD, DescriptionAsPlainText, ReversingRefNbr, RevenueChangeTotal, GrossMarginAmount, GrossMarginPct, CuryInfoID, IsCostVisible, IsRevenueVisible, IsDetailsVisible, IsChangeRequestVisible, FormCaptionDescription, NoteText, DailyFieldReportId

PX.Objects.PM.PMChangeOrder.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMChangeOrder.ProjectNbr : Edm.String "Revenue Change Order Nbr."
PX.Objects.PM.PMChangeOrder.ClassID : Edm.String "Class"
PX.Objects.PM.PMChangeOrder.ChangeOrderTaskCD : Edm.String "Change Order Task Nbr."
PX.Objects.PM.PMChangeOrder.Description : Edm.String "Description"
PX.Objects.PM.PMChangeOrder.Text : Edm.String "Details"
PX.Objects.PM.PMChangeOrder.DescriptionAsPlainText : Edm.String "DescriptionAsPlainText"
PX.Objects.PM.PMChangeOrder.Status : Edm.String "Status"
PX.Objects.PM.PMChangeOrder.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PM.PMChangeOrder.Approved : Edm.Boolean [required]
PX.Objects.PM.PMChangeOrder.Rejected : Edm.Boolean [required]
PX.Objects.PM.PMChangeOrder.SentToOwner : Edm.Boolean [required]
PX.Objects.PM.PMChangeOrder.ApprovedByOwner : Edm.Boolean [required]
PX.Objects.PM.PMChangeOrder.RejectedByOwner : Edm.Boolean [required]
PX.Objects.PM.PMChangeOrder.Canceled : Edm.Boolean [required]
PX.Objects.PM.PMChangeOrder.CustomerID : Edm.Int32 "Customer"
PX.Objects.PM.PMChangeOrder.Date : Edm.DateTimeOffset "Change Date"
PX.Objects.PM.PMChangeOrder.CompletionDate : Edm.DateTimeOffset "Approval Date"
PX.Objects.PM.PMChangeOrder.ExtRefNbr : Edm.String "External Ref. Nbr."
PX.Objects.PM.PMChangeOrder.OrigRefNbr : Edm.String "Original CO Nbr."
PX.Objects.PM.PMChangeOrder.ReversingRefNbr : Edm.String "Reversing CO Nbr."
PX.Objects.PM.PMChangeOrder.ReverseStatus : Edm.String "Reverse Status"
PX.Objects.PM.PMChangeOrder.CostTotal : Edm.Decimal [required] "Cost Budget Change Total"
PX.Objects.PM.PMChangeOrder.RevenueTotal : Edm.Decimal [required] "Revenue Budget Change Amount"
PX.Objects.PM.PMChangeOrder.RevenueTaxTotal : Edm.Decimal [required] "Revenue Budget Tax Total"
PX.Objects.PM.PMChangeOrder.RevenueChangeTotal : Edm.Decimal "Revenue Budget Change Total"
PX.Objects.PM.PMChangeOrder.RevenueRetainageTaxTotal : Edm.Decimal [required] "Revenue Budget Retainage Tax Total"
PX.Objects.PM.PMChangeOrder.RevenueTaxInclTotal : Edm.Decimal [required] "Revenue Budget Inclusive Tax Total"
PX.Objects.PM.PMChangeOrder.BilledAmount : Edm.Decimal "Billed Amount"
PX.Objects.PM.PMChangeOrder.PendingBillingAmount : Edm.Decimal "Pending Billing Amount"
PX.Objects.PM.PMChangeOrder.CommitmentTotal : Edm.Decimal [required] "Commitment Change Total"
PX.Objects.PM.PMChangeOrder.GrossMarginAmount : Edm.Decimal "Gross Margin Amount"
PX.Objects.PM.PMChangeOrder.GrossMarginPct : Edm.Decimal "Gross Margin (%)"
PX.Objects.PM.PMChangeOrder.CuryInfoID : Edm.Int64
PX.Objects.PM.PMChangeOrder.AddressID : Edm.Int32
PX.Objects.PM.PMChangeOrder.ContactID : Edm.Int32 "Billing Contact"
PX.Objects.PM.PMChangeOrder.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.PM.PMChangeOrder.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.PM.PMChangeOrder.TaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.PM.PMChangeOrder.TaxExemptionType : Edm.String "Tax Exemption Type"
PX.Objects.PM.PMChangeOrder.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.PM.PMChangeOrder.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMChangeOrder.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMChangeOrder.LineCntr : Edm.Int32 [required]
PX.Objects.PM.PMChangeOrder.BudgetLineCntr : Edm.Int32 [required]
PX.Objects.PM.PMChangeOrder.DelayDays : Edm.Int32 "Contract Change (Days)"
PX.Objects.PM.PMChangeOrder.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMChangeOrder.CostReleased : Edm.Boolean [required]
PX.Objects.PM.PMChangeOrder.IsCostVisible : Edm.Boolean "Visible Cost"
PX.Objects.PM.PMChangeOrder.IsRevenueVisible : Edm.Boolean "Visible Revenue"
PX.Objects.PM.PMChangeOrder.IsDetailsVisible : Edm.Boolean "Visible Details"
PX.Objects.PM.PMChangeOrder.IsChangeRequestVisible : Edm.Boolean "2-Tier Change Management"
PX.Objects.PM.PMChangeOrder.FormCaptionDescription : Edm.String
PX.Objects.PM.PMChangeOrder.NoteID : Edm.Guid
PX.Objects.PM.PMChangeOrder.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMChangeOrder.tstamp : Edm.Binary
PX.Objects.PM.PMChangeOrder.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeOrder.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrder.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMChangeOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeOrder.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrder.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMChangeOrder.DailyFieldReportId : Edm.Int32 "DailyFieldReportId"
PX.Objects.PM.PMChangeOrder.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMChangeOrder.PMContactByContactID -> PX.Objects.PM.PMContact (ContactID=ContactID)
PX.Objects.PM.PMChangeOrder.PMTaskByChangeOrderTaskTemplateID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMChangeOrder.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.PM.PMChangeOrder.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.PM.PMChangeOrder.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PM.PMChangeOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeOrder.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMChangeOrder.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PM.PMChangeOrder.PMChangeOrderClassByClassID -> PX.Objects.PM.PMChangeOrderClass (ClassID=ClassID)
PX.Objects.PM.PMChangeOrder.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)
PX.Objects.PM.PMChangeOrder.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.PM.PMChangeOrder.PMChangeOrderTaxTranCollection -> Collection(PX.Objects.PM.PMChangeOrderTaxTran)
PX.Objects.PM.PMChangeOrder.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMChangeOrder.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PM.PMChangeOrder.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.PM.PMChangeOrder.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PM.PMChangeOrder.DailyFieldReportChangeOrderCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder)

# PX.Objects.PM.PMChangeOrderBudget (EntityType)

Label: "Budget"
Key: LineNbr, RefNbr, Type
Entity sets: PX_Objects_PM_PMChangeOrderBudget, Budget3, PMChangeOrderBudget
Non-filterable, non-selectable: RevisedQty, RevisedAmount, PreviouslyApprovedQty, PreviouslyApprovedAmount, CommittedCOQty, CommittedCOAmount, OtherDraftRevisedAmount, TotalPotentialRevisedAmount, NoteText

PX.Objects.PM.PMChangeOrderBudget.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.PM.PMChangeOrderBudget.ProjectID : Edm.Int32
PX.Objects.PM.PMChangeOrderBudget.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMChangeOrderBudget.ProjectTaskID : Edm.Int32
PX.Objects.PM.PMChangeOrderBudget.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMChangeOrderBudget.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMChangeOrderBudget.Type : Edm.String [key] "Type"
PX.Objects.PM.PMChangeOrderBudget.Rate : Edm.Decimal [required] "Unit Rate"
PX.Objects.PM.PMChangeOrderBudget.Description : Edm.String "Description"
PX.Objects.PM.PMChangeOrderBudget.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.PM.PMChangeOrderBudget.UOM : Edm.String "UOM"
PX.Objects.PM.PMChangeOrderBudget.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PM.PMChangeOrderBudget.RevisedQty : Edm.Decimal "Revised Budgeted Quantity"
PX.Objects.PM.PMChangeOrderBudget.RevisedAmount : Edm.Decimal "Revised Budgeted Amount"
PX.Objects.PM.PMChangeOrderBudget.IsDisabled : Edm.Boolean [required]
PX.Objects.PM.PMChangeOrderBudget.PreviouslyApprovedQty : Edm.Decimal
PX.Objects.PM.PMChangeOrderBudget.PreviouslyApprovedAmount : Edm.Decimal
PX.Objects.PM.PMChangeOrderBudget.CommittedCOQty : Edm.Decimal
PX.Objects.PM.PMChangeOrderBudget.CommittedCOAmount : Edm.Decimal
PX.Objects.PM.PMChangeOrderBudget.OtherDraftRevisedAmount : Edm.Decimal
PX.Objects.PM.PMChangeOrderBudget.TotalPotentialRevisedAmount : Edm.Decimal
PX.Objects.PM.PMChangeOrderBudget.BilledAmount : Edm.Decimal [required] "Billed Amount"
PX.Objects.PM.PMChangeOrderBudget.PendingBillingAmount : Edm.Decimal [required] "Pending Billing Amount"
PX.Objects.PM.PMChangeOrderBudget.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMChangeOrderBudget.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.PMChangeOrderBudget.NoteID : Edm.Guid
PX.Objects.PM.PMChangeOrderBudget.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMChangeOrderBudget.tstamp : Edm.Binary
PX.Objects.PM.PMChangeOrderBudget.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeOrderBudget.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderBudget.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMChangeOrderBudget.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeOrderBudget.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderBudget.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMChangeOrderBudget.PMProjectByRefNbr -> PX.Objects.PM.PMProject (RefNbr=ContractID)
PX.Objects.PM.PMChangeOrderBudget.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMChangeOrderBudget.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.PM.PMChangeOrderBudget.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PM.PMChangeOrderBudget.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMChangeOrderBudget.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMChangeOrderBudget.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeOrderBudget.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeOrderBudget.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PM.PMChangeOrderBudget.PMChangeOrderByRefNbr -> PX.Objects.PM.PMChangeOrder (RefNbr=RefNbr)
PX.Objects.PM.PMChangeOrderBudget.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMChangeOrderBudget.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PM.PMChangeOrderBudget.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)

# PX.Objects.PM.PMChangeOrderClass (EntityType)

Label: "Change Order Class"
Key: ClassID
Entity sets: PX_Objects_PM_PMChangeOrderClass, ChangeOrderClass, PMChangeOrderClass
Non-filterable, non-selectable: IncrementsProjectNumber, NoteText

PX.Objects.PM.PMChangeOrderClass.ClassID : Edm.String [key] "Class ID"
PX.Objects.PM.PMChangeOrderClass.Description : Edm.String "Description"
PX.Objects.PM.PMChangeOrderClass.IsCostBudgetEnabled : Edm.Boolean [required] "Cost Budget"
PX.Objects.PM.PMChangeOrderClass.IsRevenueBudgetEnabled : Edm.Boolean [required] "Revenue Budget"
PX.Objects.PM.PMChangeOrderClass.IsPurchaseOrderEnabled : Edm.Boolean [required] "Commitments"
PX.Objects.PM.PMChangeOrderClass.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMChangeOrderClass.IncrementsProjectNumber : Edm.Boolean
PX.Objects.PM.PMChangeOrderClass.NoteID : Edm.Guid
PX.Objects.PM.PMChangeOrderClass.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMChangeOrderClass.tstamp : Edm.Binary
PX.Objects.PM.PMChangeOrderClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeOrderClass.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderClass.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMChangeOrderClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeOrderClass.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderClass.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMChangeOrderClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeOrderClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeOrderClass.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.PM.PMChangeOrderClass.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)

# PX.Objects.PM.PMChangeOrderCostBudget (EntityType)

Label: "Budget"
BaseType: PX.Objects.PM.PMChangeOrderBudget
Key: LineNbr, RefNbr, Type (inherited from PX.Objects.PM.PMChangeOrderBudget)
Entity sets: PX_Objects_PM_PMChangeOrderCostBudget, Budget4, PMChangeOrderCostBudget

# PX.Objects.PM.PMChangeOrderLine (EntityType)

Label: "Change Order Line"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PM_PMChangeOrderLine, ChangeOrderLine, PMChangeOrderLine
Non-filterable, non-selectable: PotentialRevisedQty, PotentialRevisedAmount, NoteText

PX.Objects.PM.PMChangeOrderLine.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMChangeOrderLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMChangeOrderLine.ProjectID : Edm.Int32
PX.Objects.PM.PMChangeOrderLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMChangeOrderLine.Description : Edm.String "Description"
PX.Objects.PM.PMChangeOrderLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.PM.PMChangeOrderLine.POOrderType : Edm.String "PO Type"
PX.Objects.PM.PMChangeOrderLine.POOrderNbr : Edm.String "PO Nbr."
PX.Objects.PM.PMChangeOrderLine.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.PM.PMChangeOrderLine.CuryID : Edm.String "Currency"
PX.Objects.PM.PMChangeOrderLine.UOM : Edm.String "UOM"
PX.Objects.PM.PMChangeOrderLine.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.PM.PMChangeOrderLine.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.PM.PMChangeOrderLine.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PM.PMChangeOrderLine.AmountInProjectCury : Edm.Decimal [required] "Amount in Project Currency"
PX.Objects.PM.PMChangeOrderLine.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMChangeOrderLine.LineType : Edm.String "Status"
PX.Objects.PM.PMChangeOrderLine.PotentialRevisedQty : Edm.Decimal
PX.Objects.PM.PMChangeOrderLine.PotentialRevisedAmount : Edm.Decimal
PX.Objects.PM.PMChangeOrderLine.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.PMChangeOrderLine.NoteID : Edm.Guid
PX.Objects.PM.PMChangeOrderLine.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMChangeOrderLine.tstamp : Edm.Binary
PX.Objects.PM.PMChangeOrderLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeOrderLine.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMChangeOrderLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeOrderLine.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMChangeOrderLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMChangeOrderLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PM.PMChangeOrderLine.POLineByPOOrderType -> PX.Objects.PO.POLine (POOrderNbr=OrderNbr, VendorID=VendorID, POOrderType=OrderType)
PX.Objects.PM.PMChangeOrderLine.POLineByPOOrderNbr -> PX.Objects.PO.POLine (POLineNbr=LineNbr, POOrderType=OrderType, POOrderNbr=OrderNbr)
PX.Objects.PM.PMChangeOrderLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMChangeOrderLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMChangeOrderLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PM.PMChangeOrderLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMChangeOrderLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeOrderLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeOrderLine.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PM.PMChangeOrderLine.PMChangeOrderByRefNbr -> PX.Objects.PM.PMChangeOrder (RefNbr=RefNbr)
PX.Objects.PM.PMChangeOrderLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMChangeOrderLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PM.PMChangeOrderLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PM.PMChangeOrderLine.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PM.PMChangeOrderLine.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMChangeOrderLine.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)

# PX.Objects.PM.PMChangeOrderRevenueBudget (EntityType)

Label: "Budget"
BaseType: PX.Objects.PM.PMChangeOrderBudget
Key: LineNbr, RefNbr, Type (inherited from PX.Objects.PM.PMChangeOrderBudget)
Entity sets: PX_Objects_PM_PMChangeOrderRevenueBudget, Budget5, PMChangeOrderRevenueBudget

# PX.Objects.PM.PMChangeOrderTax (EntityType)

Label: "PMChangeOrderTax"
Key: LineNbr, RefNbr, TaxID
Entity sets: PX_Objects_PM_PMChangeOrderTax, PMChangeOrderTax
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt

PX.Objects.PM.PMChangeOrderTax.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.PM.PMChangeOrderTax.NonDeductibleTaxRate : Edm.Decimal [required] "Deductible Tax Rate"
PX.Objects.PM.PMChangeOrderTax.ExpenseAmt : Edm.Decimal [required] "Expense Amount"
PX.Objects.PM.PMChangeOrderTax.CuryExpenseAmt : Edm.Decimal [required] "Expense Amount"
PX.Objects.PM.PMChangeOrderTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeOrderTax.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMChangeOrderTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeOrderTax.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMChangeOrderTax.RefNbr : Edm.String [key] "Change Order Nbr."
PX.Objects.PM.PMChangeOrderTax.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.PM.PMChangeOrderTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PM.PMChangeOrderTax.CuryInfoID : Edm.Int64
PX.Objects.PM.PMChangeOrderTax.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PM.PMChangeOrderTax.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PM.PMChangeOrderTax.RetainedTaxableAmt : Edm.Decimal [required] "Retained Taxable"
PX.Objects.PM.PMChangeOrderTax.RetainedTaxAmt : Edm.Decimal [required] "Retained Tax"
PX.Objects.PM.PMChangeOrderTax.tstamp : Edm.Binary
PX.Objects.PM.PMChangeOrderTax.PMChangeOrderBudgetByLineNbr -> PX.Objects.PM.PMChangeOrderBudget (RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.PM.PMChangeOrderTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PM.PMChangeOrderTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeOrderTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeOrderTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PM.PMChangeOrderTax.PMChangeOrderByRefNbr -> PX.Objects.PM.PMChangeOrder (RefNbr=RefNbr)
PX.Objects.PM.PMChangeOrderTax.PMChangeOrderLineByLineNbr -> PX.Objects.PM.PMChangeOrderLine (RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.PM.PMChangeOrderTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PM.PMChangeOrderTaxTran (EntityType)

Label: "PMChangeOrderTaxTran"
Key: RecordID, TaxID
Entity sets: PX_Objects_PM_PMChangeOrderTaxTran, PMChangeOrderTaxTran
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt, CuryID, CuryRate, CuryViewState

PX.Objects.PM.PMChangeOrderTaxTran.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.PM.PMChangeOrderTaxTran.NonDeductibleTaxRate : Edm.Decimal [required] "Deductible Tax Rate"
PX.Objects.PM.PMChangeOrderTaxTran.ExpenseAmt : Edm.Decimal [required] "Expense Amount"
PX.Objects.PM.PMChangeOrderTaxTran.CuryExpenseAmt : Edm.Decimal [required] "Expense Amount"
PX.Objects.PM.PMChangeOrderTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeOrderTaxTran.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMChangeOrderTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeOrderTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeOrderTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMChangeOrderTaxTran.RecordID : Edm.Int64 [key] "PM Tran."
PX.Objects.PM.PMChangeOrderTaxTran.RefNbr : Edm.String "Order Nbr."
PX.Objects.PM.PMChangeOrderTaxTran.LineNbr : Edm.Int32 [required] "Line Nbr."
PX.Objects.PM.PMChangeOrderTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PM.PMChangeOrderTaxTran.TaxZoneID : Edm.String
PX.Objects.PM.PMChangeOrderTaxTran.CuryInfoID : Edm.Int64
PX.Objects.PM.PMChangeOrderTaxTran.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PM.PMChangeOrderTaxTran.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PM.PMChangeOrderTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.PM.PMChangeOrderTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.PM.PMChangeOrderTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.PM.PMChangeOrderTaxTran.CuryID : Edm.String "Currency"
PX.Objects.PM.PMChangeOrderTaxTran.CuryRate : Edm.Decimal
PX.Objects.PM.PMChangeOrderTaxTran.CuryViewState : Edm.Boolean
PX.Objects.PM.PMChangeOrderTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeOrderTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeOrderTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PM.PMChangeOrderTaxTran.PMChangeOrderByRefNbr -> PX.Objects.PM.PMChangeOrder (RefNbr=RefNbr)
PX.Objects.PM.PMChangeOrderTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PM.PMChangeRequest (EntityType)

Label: "Change Request"
Key: RefNbr
Entity sets: PX_Objects_PM_PMChangeRequest, ChangeRequest, PMChangeRequest
Non-filterable, non-selectable: ChangeRequestTaskCD, DescriptionAsPlainText, GrossMarginPct, FormCaptionDescription, CuryInfoID, ChangeRequestTaxTotal, ChangeRequestTotal, NoteText, DailyFieldReportId

PX.Objects.PM.PMChangeRequest.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMChangeRequest.ChangeOrderNbr : Edm.String "Change Order Nbr."
PX.Objects.PM.PMChangeRequest.CostChangeOrderNbr : Edm.String "Cost Change Order Nbr."
PX.Objects.PM.PMChangeRequest.ChangeRequestTaskCD : Edm.String "Change Request Task Nbr."
PX.Objects.PM.PMChangeRequest.CostChangeOrderReleased : Edm.Boolean
PX.Objects.PM.PMChangeRequest.ChangeRequestTaskTemplateID : Edm.Int32 "Common Task for Change Request"
PX.Objects.PM.PMChangeRequest.ProjectNbr : Edm.String "Change Request Nbr."
PX.Objects.PM.PMChangeRequest.Description : Edm.String "Description"
PX.Objects.PM.PMChangeRequest.Text : Edm.String "Details"
PX.Objects.PM.PMChangeRequest.DescriptionAsPlainText : Edm.String "DescriptionAsPlainText"
PX.Objects.PM.PMChangeRequest.Status : Edm.String "Status"
PX.Objects.PM.PMChangeRequest.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PM.PMChangeRequest.Approved : Edm.Boolean [required]
PX.Objects.PM.PMChangeRequest.Rejected : Edm.Boolean [required]
PX.Objects.PM.PMChangeRequest.CustomerID : Edm.Int32 "Customer"
PX.Objects.PM.PMChangeRequest.Date : Edm.DateTimeOffset "Change Date"
PX.Objects.PM.PMChangeRequest.ExtRefNbr : Edm.String "External Ref. Nbr."
PX.Objects.PM.PMChangeRequest.CostTotal : Edm.Decimal [required] "Cost Total"
PX.Objects.PM.PMChangeRequest.LineTotal : Edm.Decimal [required] "Line Total"
PX.Objects.PM.PMChangeRequest.MarkupTotal : Edm.Decimal [required] "Markup Total"
PX.Objects.PM.PMChangeRequest.PriceTotal : Edm.Decimal [required] "Price Total"
PX.Objects.PM.PMChangeRequest.GrossMarginPct : Edm.Decimal "Gross Margin (%)"
PX.Objects.PM.PMChangeRequest.UnitPriceSource : Edm.String "Unit Price Source"
PX.Objects.PM.PMChangeRequest.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMChangeRequest.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMChangeRequest.LineCntr : Edm.Int32 [required]
PX.Objects.PM.PMChangeRequest.MarkupLineCntr : Edm.Int32 [required]
PX.Objects.PM.PMChangeRequest.DelayDays : Edm.Int32 "Contract Change (Days)"
PX.Objects.PM.PMChangeRequest.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMChangeRequest.Canceled : Edm.Boolean [required]
PX.Objects.PM.PMChangeRequest.MergedInRevenueBudget : Edm.Boolean [required]
PX.Objects.PM.PMChangeRequest.FormCaptionDescription : Edm.String
PX.Objects.PM.PMChangeRequest.CuryInfoID : Edm.Int64
PX.Objects.PM.PMChangeRequest.AddressID : Edm.Int32
PX.Objects.PM.PMChangeRequest.ContactID : Edm.Int32 "Contact"
PX.Objects.PM.PMChangeRequest.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.PM.PMChangeRequest.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.PM.PMChangeRequest.TaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.PM.PMChangeRequest.TaxExemptionType : Edm.String "Tax Exemption Type"
PX.Objects.PM.PMChangeRequest.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.PM.PMChangeRequest.EstimatedTaxTotal : Edm.Decimal [required] "Estimated Tax Total"
PX.Objects.PM.PMChangeRequest.EstimatedTaxInclTotal : Edm.Decimal [required] "Estimated Tax Inclusive Total"
PX.Objects.PM.PMChangeRequest.MarkupTaxTotal : Edm.Decimal [required] "Markup Tax Total"
PX.Objects.PM.PMChangeRequest.MarkupTaxInclTotal : Edm.Decimal [required] "Markup Tax Inclusive Total"
PX.Objects.PM.PMChangeRequest.ChangeRequestTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.PM.PMChangeRequest.ChangeRequestTotal : Edm.Decimal "Change Total"
PX.Objects.PM.PMChangeRequest.NoteID : Edm.Guid
PX.Objects.PM.PMChangeRequest.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMChangeRequest.tstamp : Edm.Binary
PX.Objects.PM.PMChangeRequest.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeRequest.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequest.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMChangeRequest.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeRequest.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequest.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMChangeRequest.DailyFieldReportId : Edm.Int32 "DailyFieldReportId"
PX.Objects.PM.PMChangeRequest.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMChangeRequest.PMContactByContactID -> PX.Objects.PM.PMContact (ContactID=ContactID)
PX.Objects.PM.PMChangeRequest.PMTaskByChangeRequestTaskTemplateID -> PX.Objects.PM.PMTask (ChangeRequestTaskTemplateID=TaskID)
PX.Objects.PM.PMChangeRequest.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.PM.PMChangeRequest.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PM.PMChangeRequest.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeRequest.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeRequest.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMChangeRequest.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PM.PMChangeRequest.PMChangeOrderByChangeOrderNbr -> PX.Objects.PM.PMChangeOrder (ChangeOrderNbr=RefNbr)
PX.Objects.PM.PMChangeRequest.PMChangeOrderByCostChangeOrderNbr -> PX.Objects.PM.PMChangeOrder (CostChangeOrderNbr=RefNbr)
PX.Objects.PM.PMChangeRequest.PMChangeRequestTaxCollection -> Collection(PX.Objects.PM.PMChangeRequestTax)
PX.Objects.PM.PMChangeRequest.PMChangeRequestTaxTranCollection -> Collection(PX.Objects.PM.PMChangeRequestTaxTran)
PX.Objects.PM.PMChangeRequest.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMChangeRequest.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.PM.PMChangeRequest.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.PM.PMChangeRequest.DailyFieldReportChangeRequestCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeRequest)

# PX.Objects.PM.PMChangeRequestAudit (EntityType)

Label: "Change Request Audit"
Key: RecordID
Entity sets: PX_Objects_PM_PMChangeRequestAudit, ChangeRequestAudit, PMChangeRequestAudit

PX.Objects.PM.PMChangeRequestAudit.RecordID : Edm.Int32 [key] "Record ID"
PX.Objects.PM.PMChangeRequestAudit.ChangeRequestNbr : Edm.String "Reference Nbr."
PX.Objects.PM.PMChangeRequestAudit.ChangeOrderNbr : Edm.String "Change Order Nbr."
PX.Objects.PM.PMChangeRequestAudit.OldChangeOrderNbr : Edm.String "Old Change Order Nbr."
PX.Objects.PM.PMChangeRequestAudit.tstamp : Edm.Binary
PX.Objects.PM.PMChangeRequestAudit.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeRequestAudit.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestAudit.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Objects.PM.PMChangeRequestAudit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeRequestAudit.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestAudit.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.PM.PMChangeRequestAudit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeRequestAudit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PM.PMChangeRequestLine (EntityType)

Label: "Change Request"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PM_PMChangeRequestLine, ChangeRequest1, PMChangeRequestLine
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMChangeRequestLine.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMChangeRequestLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMChangeRequestLine.ProjectID : Edm.Int32
PX.Objects.PM.PMChangeRequestLine.CostAccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMChangeRequestLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMChangeRequestLine.RevenueAccountGroupID : Edm.Int32 "Revenue Account Group"
PX.Objects.PM.PMChangeRequestLine.RevenueInventoryID : Edm.Int32 "Revenue Inventory ID"
PX.Objects.PM.PMChangeRequestLine.Description : Edm.String "Description"
PX.Objects.PM.PMChangeRequestLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.PM.PMChangeRequestLine.IsCommitment : Edm.Boolean [required] "Create Commitment"
PX.Objects.PM.PMChangeRequestLine.IsCommitmentProcessed : Edm.Boolean [required]
PX.Objects.PM.PMChangeRequestLine.POOrderType : Edm.String "PO Type"
PX.Objects.PM.PMChangeRequestLine.POOrderNbr : Edm.String "PO Nbr."
PX.Objects.PM.PMChangeRequestLine.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.PM.PMChangeRequestLine.LineType : Edm.String "Status"
PX.Objects.PM.PMChangeRequestLine.UOM : Edm.String "UOM"
PX.Objects.PM.PMChangeRequestLine.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.PM.PMChangeRequestLine.UnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.PM.PMChangeRequestLine.ExtCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.PM.PMChangeRequestLine.PriceMarkupPct : Edm.Decimal [required] "Price Markup (%)"
PX.Objects.PM.PMChangeRequestLine.UnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.PM.PMChangeRequestLine.ExtPrice : Edm.Decimal [required] "Ext. Price"
PX.Objects.PM.PMChangeRequestLine.LineMarkupPct : Edm.Decimal [required] "Line Markup (%)"
PX.Objects.PM.PMChangeRequestLine.LineAmount : Edm.Decimal [required] "Line Amount"
PX.Objects.PM.PMChangeRequestLine.TaxCategoryID : Edm.String "Revenue Tax Category"
PX.Objects.PM.PMChangeRequestLine.NoteID : Edm.Guid
PX.Objects.PM.PMChangeRequestLine.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMChangeRequestLine.tstamp : Edm.Binary
PX.Objects.PM.PMChangeRequestLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeRequestLine.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMChangeRequestLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeRequestLine.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMChangeRequestLine.POLineByPOOrderType -> PX.Objects.PO.POLine (POOrderNbr=OrderNbr, VendorID=VendorID, POOrderType=OrderType)
PX.Objects.PM.PMChangeRequestLine.POLineByProjectID -> PX.Objects.PO.POLine (POLineNbr=LineNbr, POOrderType=OrderType, POOrderNbr=OrderNbr)
PX.Objects.PM.PMChangeRequestLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMChangeRequestLine.PMTaskByCostTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMChangeRequestLine.PMTaskByRevenueTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMChangeRequestLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PM.PMChangeRequestLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMChangeRequestLine.InventoryItemByRevenueInventoryID -> PX.Objects.IN.InventoryItem (RevenueInventoryID=InventoryID)
PX.Objects.PM.PMChangeRequestLine.PMAccountGroupByCostAccountGroupID -> PX.Objects.PM.PMAccountGroup (CostAccountGroupID=GroupID)
PX.Objects.PM.PMChangeRequestLine.PMAccountGroupByRevenueAccountGroupID -> PX.Objects.PM.PMAccountGroup (RevenueAccountGroupID=GroupID)
PX.Objects.PM.PMChangeRequestLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeRequestLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeRequestLine.PMChangeRequestByRefNbr -> PX.Objects.PM.PMChangeRequest (RefNbr=RefNbr)
PX.Objects.PM.PMChangeRequestLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PM.PMChangeRequestLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PM.PMChangeRequestLine.PMChangeRequestTaxCollection -> Collection(PX.Objects.PM.PMChangeRequestTax)

# PX.Objects.PM.PMChangeRequestLineTax (EntityType)

Label: "Change Request Line Tax"
BaseType: PX.Objects.PM.PMChangeRequestTax
Key: LineNbr, RefNbr, TaxID, Type (inherited from PX.Objects.PM.PMChangeRequestTax)
Entity sets: PX_Objects_PM_PMChangeRequestLineTax, ChangeRequestLineTax, PMChangeRequestLineTax

# PX.Objects.PM.PMChangeRequestLineTaxTran (EntityType)

Label: "PChange Request Line Tax Tran"
BaseType: PX.Objects.PM.PMChangeRequestTaxTran
Key: RecordID, TaxID (inherited from PX.Objects.PM.PMChangeRequestTaxTran)
Entity sets: PX_Objects_PM_PMChangeRequestLineTaxTran, PChangeRequestLineTaxTran, PMChangeRequestLineTaxTran

# PX.Objects.PM.PMChangeRequestMarkup (EntityType)

Label: "Markup"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PM_PMChangeRequestMarkup, Markup1, PMChangeRequestMarkup
Non-filterable, non-selectable: ProjectID, NoteText

PX.Objects.PM.PMChangeRequestMarkup.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMChangeRequestMarkup.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMChangeRequestMarkup.Type : Edm.String "Type"
PX.Objects.PM.PMChangeRequestMarkup.Description : Edm.String "Description"
PX.Objects.PM.PMChangeRequestMarkup.Value : Edm.Decimal "Value"
PX.Objects.PM.PMChangeRequestMarkup.Amount : Edm.Decimal "Amount Subject to Markup"
PX.Objects.PM.PMChangeRequestMarkup.MarkupAmount : Edm.Decimal "Markup Amount"
PX.Objects.PM.PMChangeRequestMarkup.ProjectID : Edm.Int32
PX.Objects.PM.PMChangeRequestMarkup.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMChangeRequestMarkup.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMChangeRequestMarkup.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.PMChangeRequestMarkup.NoteID : Edm.Guid
PX.Objects.PM.PMChangeRequestMarkup.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMChangeRequestMarkup.tstamp : Edm.Binary
PX.Objects.PM.PMChangeRequestMarkup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeRequestMarkup.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestMarkup.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMChangeRequestMarkup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeRequestMarkup.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestMarkup.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMChangeRequestMarkup.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMChangeRequestMarkup.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMChangeRequestMarkup.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMChangeRequestMarkup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeRequestMarkup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeRequestMarkup.PMChangeRequestByRefNbr -> PX.Objects.PM.PMChangeRequest (RefNbr=RefNbr)
PX.Objects.PM.PMChangeRequestMarkup.PMChangeRequestTaxCollection -> Collection(PX.Objects.PM.PMChangeRequestTax)

# PX.Objects.PM.PMChangeRequestMarkupTax (EntityType)

Label: "Change Request Markup Tax"
BaseType: PX.Objects.PM.PMChangeRequestTax
Key: LineNbr, RefNbr, TaxID, Type (inherited from PX.Objects.PM.PMChangeRequestTax)
Entity sets: PX_Objects_PM_PMChangeRequestMarkupTax, ChangeRequestMarkupTax, PMChangeRequestMarkupTax

# PX.Objects.PM.PMChangeRequestMarkupTaxTran (EntityType)

Label: "PChange Request Markup Tax Tran"
BaseType: PX.Objects.PM.PMChangeRequestTaxTran
Key: RecordID, TaxID (inherited from PX.Objects.PM.PMChangeRequestTaxTran)
Entity sets: PX_Objects_PM_PMChangeRequestMarkupTaxTran, PChangeRequestMarkupTaxTran, PMChangeRequestMarkupTaxTran

# PX.Objects.PM.PMChangeRequestTax (EntityType)

Label: "Change Request Tax"
Key: LineNbr, RefNbr, TaxID, Type
Entity sets: PX_Objects_PM_PMChangeRequestTax, ChangeRequestTax, PMChangeRequestTax
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt

PX.Objects.PM.PMChangeRequestTax.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.PM.PMChangeRequestTax.NonDeductibleTaxRate : Edm.Decimal [required] "Deductible Tax Rate"
PX.Objects.PM.PMChangeRequestTax.ExpenseAmt : Edm.Decimal [required] "Expense Amount"
PX.Objects.PM.PMChangeRequestTax.CuryExpenseAmt : Edm.Decimal [required] "Expense Amount"
PX.Objects.PM.PMChangeRequestTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeRequestTax.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMChangeRequestTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeRequestTax.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMChangeRequestTax.Type : Edm.String [key] "Type"
PX.Objects.PM.PMChangeRequestTax.RefNbr : Edm.String [key] "Change Request Nbr."
PX.Objects.PM.PMChangeRequestTax.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.PM.PMChangeRequestTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PM.PMChangeRequestTax.CuryInfoID : Edm.Int64
PX.Objects.PM.PMChangeRequestTax.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PM.PMChangeRequestTax.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PM.PMChangeRequestTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeRequestTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeRequestTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PM.PMChangeRequestTax.PMChangeRequestByRefNbr -> PX.Objects.PM.PMChangeRequest (RefNbr=RefNbr)
PX.Objects.PM.PMChangeRequestTax.PMChangeRequestLineByLineNbr -> PX.Objects.PM.PMChangeRequestLine (RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.PM.PMChangeRequestTax.PMChangeRequestMarkupByLineNbr -> PX.Objects.PM.PMChangeRequestMarkup (RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.PM.PMChangeRequestTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PM.PMChangeRequestTaxTran (EntityType)

Label: "PChange Request Tax Tran"
Key: RecordID, TaxID
Entity sets: PX_Objects_PM_PMChangeRequestTaxTran, PChangeRequestTaxTran, PMChangeRequestTaxTran
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt, CuryID, CuryRate, CuryViewState

PX.Objects.PM.PMChangeRequestTaxTran.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.PM.PMChangeRequestTaxTran.NonDeductibleTaxRate : Edm.Decimal [required] "Deductible Tax Rate"
PX.Objects.PM.PMChangeRequestTaxTran.ExpenseAmt : Edm.Decimal [required] "Expense Amount"
PX.Objects.PM.PMChangeRequestTaxTran.CuryExpenseAmt : Edm.Decimal [required] "Expense Amount"
PX.Objects.PM.PMChangeRequestTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMChangeRequestTaxTran.CreatedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMChangeRequestTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMChangeRequestTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMChangeRequestTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMChangeRequestTaxTran.RecordID : Edm.Int64 [key]
PX.Objects.PM.PMChangeRequestTaxTran.Type : Edm.String "Type"
PX.Objects.PM.PMChangeRequestTaxTran.RefNbr : Edm.String "Order Nbr."
PX.Objects.PM.PMChangeRequestTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PM.PMChangeRequestTaxTran.TaxZoneID : Edm.String
PX.Objects.PM.PMChangeRequestTaxTran.CuryInfoID : Edm.Int64
PX.Objects.PM.PMChangeRequestTaxTran.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PM.PMChangeRequestTaxTran.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PM.PMChangeRequestTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.PM.PMChangeRequestTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.PM.PMChangeRequestTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.PM.PMChangeRequestTaxTran.CuryID : Edm.String "Currency"
PX.Objects.PM.PMChangeRequestTaxTran.CuryRate : Edm.Decimal
PX.Objects.PM.PMChangeRequestTaxTran.CuryViewState : Edm.Boolean
PX.Objects.PM.PMChangeRequestTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMChangeRequestTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMChangeRequestTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PM.PMChangeRequestTaxTran.PMChangeRequestByRefNbr -> PX.Objects.PM.PMChangeRequest (RefNbr=RefNbr)
PX.Objects.PM.PMChangeRequestTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PM.PMChangeRequestTotalTaxTran (EntityType)

Label: "PChange Request Total Tax Tran"
BaseType: PX.Objects.PM.PMChangeRequestTaxTran
Key: RecordID, TaxID (inherited from PX.Objects.PM.PMChangeRequestTaxTran)
Entity sets: PX_Objects_PM_PMChangeRequestTotalTaxTran, PChangeRequestTotalTaxTran, PMChangeRequestTotalTaxTran

# PX.Objects.PM.PMCommitment (EntityType)

Label: "Commitment Record"
Key: CommitmentID
Entity sets: PX_Objects_PM_PMCommitment, CommitmentRecord, PMCommitment
Non-filterable, non-selectable: CommittedVarianceQty, CommittedVarianceAmount, NoteText

PX.Objects.PM.PMCommitment.CommitmentID : Edm.Guid [key]
PX.Objects.PM.PMCommitment.BranchID : Edm.Int32 "Branch"
PX.Objects.PM.PMCommitment.Type : Edm.String "Type"
PX.Objects.PM.PMCommitment.Status : Edm.String "Status"
PX.Objects.PM.PMCommitment.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMCommitment.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMCommitment.ExtRefNbr : Edm.String "External Ref. Nbr"
PX.Objects.PM.PMCommitment.UOM : Edm.String "UOM"
PX.Objects.PM.PMCommitment.Qty : Edm.Decimal [required] "Revised Committed Quantity"
PX.Objects.PM.PMCommitment.Amount : Edm.Decimal [required] "Revised Committed Amount"
PX.Objects.PM.PMCommitment.ReceivedQty : Edm.Decimal [required] "Committed Received Quantity"
PX.Objects.PM.PMCommitment.InvoicedQty : Edm.Decimal [required] "Committed Invoiced Quantity"
PX.Objects.PM.PMCommitment.InvoicedAmount : Edm.Decimal [required] "Committed Invoiced Amount"
PX.Objects.PM.PMCommitment.CommittedVarianceQty : Edm.Decimal "Committed Variance Quantity"
PX.Objects.PM.PMCommitment.CommittedVarianceAmount : Edm.Decimal "Committed Variance Amount"
PX.Objects.PM.PMCommitment.OpenQty : Edm.Decimal [required] "Committed Open Quantity"
PX.Objects.PM.PMCommitment.OpenAmount : Edm.Decimal [required] "Committed Open Amount"
PX.Objects.PM.PMCommitment.RefNoteID : Edm.Guid "Related Document"
PX.Objects.PM.PMCommitment.NoteID : Edm.Guid
PX.Objects.PM.PMCommitment.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMCommitment.tstamp : Edm.Binary
PX.Objects.PM.PMCommitment.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMCommitment.CreatedByScreenID : Edm.String
PX.Objects.PM.PMCommitment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMCommitment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMCommitment.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMCommitment.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMCommitment.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMCommitment.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMCommitment.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMCommitment.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMCommitment.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMCommitment.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.PM.PMCommitment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMCommitment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMCommitment.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMCommitment.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
