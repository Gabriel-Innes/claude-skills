<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# PX.Objects.PM.PMContact (EntityType)

Label: "Project Contact"
Key: ContactID
Entity sets: PX_Objects_PM_PMContact, ProjectContact, PMContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.PM.PMContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.PM.PMContact.CustomerID : Edm.Int32
PX.Objects.PM.PMContact.CustomerContactID : Edm.Int32
PX.Objects.PM.PMContact.IsDefaultContact : Edm.Boolean [required] "Default Customer Contact"
PX.Objects.PM.PMContact.OverrideContact : Edm.Boolean "Override Contact"
PX.Objects.PM.PMContact.RevisionID : Edm.Int32
PX.Objects.PM.PMContact.Title : Edm.String "Title"
PX.Objects.PM.PMContact.Salutation : Edm.String "Job Title"
PX.Objects.PM.PMContact.Attention : Edm.String "Attention"
PX.Objects.PM.PMContact.FullName : Edm.String "Account Name"
PX.Objects.PM.PMContact.Email : Edm.String "Email"
PX.Objects.PM.PMContact.Fax : Edm.String "Fax"
PX.Objects.PM.PMContact.FaxType : Edm.String "Fax"
PX.Objects.PM.PMContact.Phone1 : Edm.String "Phone 1"
PX.Objects.PM.PMContact.Phone1Type : Edm.String "Phone 1"
PX.Objects.PM.PMContact.Phone2 : Edm.String "Phone 2"
PX.Objects.PM.PMContact.Phone2Type : Edm.String "Phone 2"
PX.Objects.PM.PMContact.Phone3 : Edm.String "Phone 3"
PX.Objects.PM.PMContact.Phone3Type : Edm.String "Phone 3"
PX.Objects.PM.PMContact.NoteID : Edm.Guid
PX.Objects.PM.PMContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMContact.CreatedByScreenID : Edm.String
PX.Objects.PM.PMContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMContact.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMContact.tstamp : Edm.Binary
PX.Objects.PM.PMContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMContact.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.PM.PMContact.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.PM.PMContact.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMContact.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.PM.PMContact.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)

# PX.Objects.PM.PMCostBudget (EntityType)

Label: "Project Cost Budget"
BaseType: PX.Objects.PM.PMBudget
Key: AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID (inherited from PX.Objects.PM.PMBudget)
Entity sets: PX_Objects_PM_PMCostBudget, ProjectCostBudget, PMCostBudget

# PX.Objects.PM.PMCostCode (EntityType)

Label: "Cost Code"
Key: CostCodeCD
Entity sets: PX_Objects_PM_PMCostCode, CostCode, PMCostCode
Non-filterable, non-selectable: IsProjectOverride, NoteText

PX.Objects.PM.PMCostCode.CostCodeID : Edm.Int32
PX.Objects.PM.PMCostCode.CostCodeCD : Edm.String [key] "Cost Code"
PX.Objects.PM.PMCostCode.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.PM.PMCostCode.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMCostCode.Description : Edm.String "Description"
PX.Objects.PM.PMCostCode.IsProjectOverride : Edm.Boolean "Used in Project"
PX.Objects.PM.PMCostCode.NoteID : Edm.Guid
PX.Objects.PM.PMCostCode.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMCostCode.tstamp : Edm.Binary
PX.Objects.PM.PMCostCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMCostCode.CreatedByScreenID : Edm.String
PX.Objects.PM.PMCostCode.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMCostCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMCostCode.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMCostCode.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMCostCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMCostCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMCostCode.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.PM.PMCostCode.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.PM.PMCostCode.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.PM.PMCostCode.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.PM.PMCostCode.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.PM.PMCostCode.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.PM.PMCostCode.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.PM.PMCostCode.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMCostCode.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PM.PMCostCode.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.PM.PMCostCode.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.PM.PMCostCode.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.PM.PMCostCode.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.PM.PMCostCode.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.PM.PMCostCode.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.PM.PMCostCode.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.PM.PMCostCode.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.PM.PMCostCode.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.PM.PMCostCode.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.PM.PMCostCode.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PM.PMCostCode.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PM.PMCostCode.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.PM.PMCostCode.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.PM.PMCostCode.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.PM.PMCostCode.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.PM.PMCostCode.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.PM.PMCostCode.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.PM.PMCostCode.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PM.PMCostCode.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PM.PMCostCode.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PM.PMCostCode.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.PM.PMCostCode.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.PM.PMCostCode.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PM.PMCostCode.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.PM.PMCostCode.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.PM.PMCostCode.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.PM.PMCostCode.PMWorkCodeCostCodeRangeCollection -> Collection(PX.Objects.PM.PMWorkCodeCostCodeRange)
PX.Objects.PM.PMCostCode.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.PM.PMCostCode.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PM.PMCostCode.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.PM.PMCostCode.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.PM.PMCostCode.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.PM.PMCostCode.EPEquipmentSummaryCollection -> Collection(PX.Objects.EP.EPEquipmentSummary)
PX.Objects.PM.PMCostCode.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.PM.PMCostCode.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.PM.PMCostCode.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.PM.PMCostCode.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.PM.PMCostCode.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.PM.PMCostCode.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.PM.PMCostCode.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.PM.PMCostCode.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.PM.PMCostCode.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.PM.PMCostCode.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PM.PMCostCode.PMProgressLineTotalCollection -> Collection(PX.Objects.PM.PMProgressLineTotal)
PX.Objects.PM.PMCostCode.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)

# PX.Objects.PM.PMCostProjection (EntityType)

Label: "Cost Projection"
Key: ProjectID, RevisionID
Entity sets: PX_Objects_PM_PMCostProjection, CostProjection, PMCostProjection
Non-filterable, non-selectable: FormCaptionDescription, NoteText

PX.Objects.PM.PMCostProjection.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.PMCostProjection.RevisionID : Edm.String [key] "Revision"
PX.Objects.PM.PMCostProjection.ClassID : Edm.String "Cost Projection Class"
PX.Objects.PM.PMCostProjection.Status : Edm.String "Status"
PX.Objects.PM.PMCostProjection.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PM.PMCostProjection.Approved : Edm.Boolean [required]
PX.Objects.PM.PMCostProjection.Rejected : Edm.Boolean [required]
PX.Objects.PM.PMCostProjection.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMCostProjection.Description : Edm.String "Description"
PX.Objects.PM.PMCostProjection.Date : Edm.DateTimeOffset "Revision Date"
PX.Objects.PM.PMCostProjection.LineCntr : Edm.Int32 [required]
PX.Objects.PM.PMCostProjection.TotalBudgetedQuantity : Edm.Decimal [required] "Total Budgeted Quantity"
PX.Objects.PM.PMCostProjection.TotalBudgetedAmount : Edm.Decimal [required] "Budgeted Cost at Completion"
PX.Objects.PM.PMCostProjection.TotalActualQuantity : Edm.Decimal [required] "Total Actual Quantity"
PX.Objects.PM.PMCostProjection.TotalActualAmount : Edm.Decimal [required] "Total Actual Amount"
PX.Objects.PM.PMCostProjection.TotalUnbilledQuantity : Edm.Decimal [required] "Total Unbilled Quantity"
PX.Objects.PM.PMCostProjection.TotalUnbilledAmount : Edm.Decimal [required] "Total Unbilled Amount"
PX.Objects.PM.PMCostProjection.TotalQuantity : Edm.Decimal [required] "Total Projected Quantity to Complete"
PX.Objects.PM.PMCostProjection.TotalAmount : Edm.Decimal [required] "Projected Cost to Complete"
PX.Objects.PM.PMCostProjection.TotalProjectedQuantity : Edm.Decimal [required] "Total Projected Quantity at Completion"
PX.Objects.PM.PMCostProjection.TotalProjectedAmount : Edm.Decimal [required] "Projected Cost at Completion"
PX.Objects.PM.PMCostProjection.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMCostProjection.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMCostProjection.FormCaptionDescription : Edm.String
PX.Objects.PM.PMCostProjection.NoteID : Edm.Guid
PX.Objects.PM.PMCostProjection.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMCostProjection.tstamp : Edm.Binary
PX.Objects.PM.PMCostProjection.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMCostProjection.CreatedByScreenID : Edm.String
PX.Objects.PM.PMCostProjection.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMCostProjection.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMCostProjection.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMCostProjection.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMCostProjection.TotalQuantityToComplete : Edm.Decimal [required] "Quantity to Complete"
PX.Objects.PM.PMCostProjection.TotalAmountToComplete : Edm.Decimal [required] "Budgeted Cost to Complete"
PX.Objects.PM.PMCostProjection.TotalVarianceAmount : Edm.Decimal [required] "Cost Variance"
PX.Objects.PM.PMCostProjection.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMCostProjection.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PM.PMCostProjection.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMCostProjection.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMCostProjection.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMCostProjection.PMCostProjectionClassByClassID -> PX.Objects.PM.PMCostProjectionClass (ClassID=ClassID)
PX.Objects.PM.PMCostProjection.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)

# PX.Objects.PM.PMCostProjectionByDate (EntityType)

Label: "Cost Projection By Date"
Key: RefNbr
Entity sets: PX_Objects_PM_PMCostProjectionByDate, CostProjectionByDate, PMCostProjectionByDate
Non-filterable, non-selectable: CuryCompletedAmountTotal, CompletedAmountTotal, CompletedPctTotal, CuryBudgetBacklogAmountTotal, BudgetBacklogAmountTotal, CuryRevenueBudgetBacklogAmountTotal, RevenueBudgetBacklogAmountTotal, CuryExpectedAmountTotal, ExpectedAmountTotal, CuryRevenueExpectedAmountTotal, RevenueExpectedAmountTotal, PerformanceTotal, AnticipatedPerformanceTotal, CuryOverbillingAmountTotal, OverbillingAmountTotal, ProjectedMarginTotal, CompletedQtyPctTotal, NoteText

PX.Objects.PM.PMCostProjectionByDate.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMCostProjectionByDate.Status : Edm.String "Status"
PX.Objects.PM.PMCostProjectionByDate.ProjectionDate : Edm.DateTimeOffset "Projection Date"
PX.Objects.PM.PMCostProjectionByDate.ActualTillDate : Edm.DateTimeOffset
PX.Objects.PM.PMCostProjectionByDate.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PM.PMCostProjectionByDate.Approved : Edm.Boolean [required]
PX.Objects.PM.PMCostProjectionByDate.Rejected : Edm.Boolean [required]
PX.Objects.PM.PMCostProjectionByDate.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMCostProjectionByDate.Description : Edm.String "Description"
PX.Objects.PM.PMCostProjectionByDate.GroupByProjectTaskID : Edm.Boolean [required] "Project Task"
PX.Objects.PM.PMCostProjectionByDate.GroupByAccountGroupID : Edm.Boolean [required] "Account Group"
PX.Objects.PM.PMCostProjectionByDate.GroupByInventoryID : Edm.Boolean [required] "Inventory ID"
PX.Objects.PM.PMCostProjectionByDate.IncludePendingChangeOrders : Edm.Boolean "Include Pending CO in Calculations"
PX.Objects.PM.PMCostProjectionByDate.UpdateProjectBudget : Edm.Boolean [required] "Update Project Budget"
PX.Objects.PM.PMCostProjectionByDate.CalculateByQuantity : Edm.Boolean [required] "Calculate Projected Cost by Quantity"
PX.Objects.PM.PMCostProjectionByDate.CuryAmountToCompleteTotal : Edm.Decimal "Projected Cost to Complete"
PX.Objects.PM.PMCostProjectionByDate.AmountToCompleteTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.ProjectedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryBudgetedAmountTotal : Edm.Decimal "Revised Budgeted Cost"
PX.Objects.PM.PMCostProjectionByDate.BudgetedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryOriginalBudgetedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.OriginalBudgetedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryRevisedBudgetedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.RevisedBudgetedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryChangeOrderAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.ChangeOrderAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryPendingChangeOrderAmountTotal : Edm.Decimal "Pending CO Cost"
PX.Objects.PM.PMCostProjectionByDate.PendingChangeOrderAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryPendingRevenueChangeOrderAmountTotal : Edm.Decimal "Pending CO Revenue"
PX.Objects.PM.PMCostProjectionByDate.PendingRevenueChangeOrderAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryActualAmountTotal : Edm.Decimal "Actual Cost to Date"
PX.Objects.PM.PMCostProjectionByDate.ActualAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryCommitmentOpenAmountTotal : Edm.Decimal "Committed Open Cost"
PX.Objects.PM.PMCostProjectionByDate.CommitmentOpenAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryPendingCommitmentAmountTotal : Edm.Decimal "Pending CO Commitments"
PX.Objects.PM.PMCostProjectionByDate.PendingCommitmentAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryCompletedAmountTotal : Edm.Decimal "Anticipated Cost"
PX.Objects.PM.PMCostProjectionByDate.CompletedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.RevisedRevenueBudgetedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryBilledRevenueAmountTotal : Edm.Decimal "Billed Revenue"
PX.Objects.PM.PMCostProjectionByDate.BilledRevenueAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CompletedPctTotal : Edm.Decimal "Completed (%)"
PX.Objects.PM.PMCostProjectionByDate.CuryBudgetBacklogAmountTotal : Edm.Decimal "Cost Budget Backlog"
PX.Objects.PM.PMCostProjectionByDate.BudgetBacklogAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryRevenueBudgetBacklogAmountTotal : Edm.Decimal "Revenue Budget Backlog"
PX.Objects.PM.PMCostProjectionByDate.RevenueBudgetBacklogAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryExpectedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.ExpectedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.CuryRevenueExpectedAmountTotal : Edm.Decimal "Expected Current Revenue"
PX.Objects.PM.PMCostProjectionByDate.RevenueExpectedAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.PerformanceTotal : Edm.Decimal "Performance (%)"
PX.Objects.PM.PMCostProjectionByDate.AnticipatedPerformanceTotal : Edm.Decimal "Anticipated Performance (%)"
PX.Objects.PM.PMCostProjectionByDate.CuryOverbillingAmountTotal : Edm.Decimal "Overbilling or Underbilling"
PX.Objects.PM.PMCostProjectionByDate.OverbillingAmountTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.ProjectedMarginTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.ToCompleteQtyTotal : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDate.ProjectedQtyTotal : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDate.ActualQtyTotal : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDate.RevisedBudgetedQtyTotal : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDate.CompletedQtyPctTotal : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDate.OpenCommittedQtyTotal : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDate.PendingCOQtyTotal : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDate.PendingCOCommittedQtyTotal : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDate.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMCostProjectionByDate.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMCostProjectionByDate.NoteID : Edm.Guid
PX.Objects.PM.PMCostProjectionByDate.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMCostProjectionByDate.tstamp : Edm.Binary
PX.Objects.PM.PMCostProjectionByDate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMCostProjectionByDate.CreatedByScreenID : Edm.String
PX.Objects.PM.PMCostProjectionByDate.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMCostProjectionByDate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMCostProjectionByDate.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMCostProjectionByDate.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMCostProjectionByDate.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMCostProjectionByDate.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PM.PMCostProjectionByDate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMCostProjectionByDate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMCostProjectionByDate.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMCostProjectionByDate.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.Objects.PM.PMCostProjectionByDate.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.PM.PMCostProjectionByDate.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)

# PX.Objects.PM.PMCostProjectionByDateLine (EntityType)

Label: "Cost Projection By Date Line"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PM_PMCostProjectionByDateLine, CostProjectionByDateLine, PMCostProjectionByDateLine
Non-filterable, non-selectable: CuryCompletedAmount, CompletedAmount, CuryBudgetBacklogAmount, BudgetBacklogAmount, Performance, AnticipatedPerformance, AnticipatedQty, CuryAnticipatedUnitRate, AnticipatedUnitRate, QtyPerformance, AnticipatedQtyPerformance, ProjectedQtyVariance, CuryProjectedCostVariance, ProjectedCostVariance, IsHeader, NoteText

PX.Objects.PM.PMCostProjectionByDateLine.RefNbr : Edm.String [key] "Number"
PX.Objects.PM.PMCostProjectionByDateLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMCostProjectionByDateLine.ProjectID : Edm.Int32
PX.Objects.PM.PMCostProjectionByDateLine.ProjectTaskID : Edm.Int32 "Project Task"
PX.Objects.PM.PMCostProjectionByDateLine.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMCostProjectionByDateLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMCostProjectionByDateLine.CompletedPct : Edm.Decimal "Completed (%)"
PX.Objects.PM.PMCostProjectionByDateLine.CuryAmountToComplete : Edm.Decimal "Projected Cost to Complete"
PX.Objects.PM.PMCostProjectionByDateLine.AmountToComplete : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryProjectedAmount : Edm.Decimal "Projected Cost at Completion"
PX.Objects.PM.PMCostProjectionByDateLine.ProjectedAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryBudgetedAmount : Edm.Decimal "Revised Budgeted Cost"
PX.Objects.PM.PMCostProjectionByDateLine.BudgetedAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryOriginalBudgetedAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.OriginalBudgetedAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryRevisedBudgetedAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.RevisedBudgetedAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryChangeOrderAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.ChangeOrderAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryPendingChangeOrderAmount : Edm.Decimal "Pending CO Cost"
PX.Objects.PM.PMCostProjectionByDateLine.PendingChangeOrderAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryActualAmount : Edm.Decimal "Actual Cost to Date"
PX.Objects.PM.PMCostProjectionByDateLine.ActualAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryCommitmentOpenAmount : Edm.Decimal "Open Commitments"
PX.Objects.PM.PMCostProjectionByDateLine.CommitmentOpenAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryPendingCommitmentAmount : Edm.Decimal "Pending CO Commitments"
PX.Objects.PM.PMCostProjectionByDateLine.PendingCommitmentAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryCompletedAmount : Edm.Decimal "Anticipated Cost"
PX.Objects.PM.PMCostProjectionByDateLine.CompletedAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.CuryBudgetBacklogAmount : Edm.Decimal "Cost Budget Backlog"
PX.Objects.PM.PMCostProjectionByDateLine.BudgetBacklogAmount : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.Performance : Edm.Decimal "Performance (%)"
PX.Objects.PM.PMCostProjectionByDateLine.AnticipatedPerformance : Edm.Decimal "Anticipated Performance (%)"
PX.Objects.PM.PMCostProjectionByDateLine.Description : Edm.String "Description"
PX.Objects.PM.PMCostProjectionByDateLine.CalculateByQuantity : Edm.Boolean [required] "Calculate by Quantity"
PX.Objects.PM.PMCostProjectionByDateLine.UOM : Edm.String "UOM"
PX.Objects.PM.PMCostProjectionByDateLine.ActualQty : Edm.Decimal [required] "Actual Quantity to Date"
PX.Objects.PM.PMCostProjectionByDateLine.CuryActualUnitRate : Edm.Decimal [required] "Actual Unit Rate to Date"
PX.Objects.PM.PMCostProjectionByDateLine.ActualUnitRate : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.ToCompleteQty : Edm.Decimal [required] "Projected Quantity to Complete"
PX.Objects.PM.PMCostProjectionByDateLine.CuryToCompleteUnitRate : Edm.Decimal [required] "Projected Unit Rate to Complete"
PX.Objects.PM.PMCostProjectionByDateLine.ToCompleteUnitRate : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.ProjectedQty : Edm.Decimal [required] "Projected Quantity at Completion"
PX.Objects.PM.PMCostProjectionByDateLine.OriginalBudgetedQty : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.BudgetRevisedQty : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.ChangeOrderQty : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.CuryProjectedUnitRate : Edm.Decimal [required] "Projected Unit Rate at Completion"
PX.Objects.PM.PMCostProjectionByDateLine.ProjectedUnitRate : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.RevisedBudgetedQty : Edm.Decimal [required] "Revised Budgeted Quantity"
PX.Objects.PM.PMCostProjectionByDateLine.CuryRevisedBudgetedUnitRate : Edm.Decimal [required] "Revised Budgeted Unit Rate"
PX.Objects.PM.PMCostProjectionByDateLine.RevisedBudgetedUnitRate : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.CompletedQtyPct : Edm.Decimal "Completed by Quantity (%)"
PX.Objects.PM.PMCostProjectionByDateLine.OpenCommittedQty : Edm.Decimal [required] "Open Committed Quantity"
PX.Objects.PM.PMCostProjectionByDateLine.CuryOpenCommittedUnitRate : Edm.Decimal [required] "Open Committed Unit Rate"
PX.Objects.PM.PMCostProjectionByDateLine.OpenCommittedUnitRate : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.PendingCOQty : Edm.Decimal [required] "Pending CO Quantity"
PX.Objects.PM.PMCostProjectionByDateLine.CuryPendingCOUnitRate : Edm.Decimal [required] "Pending CO Unit Rate"
PX.Objects.PM.PMCostProjectionByDateLine.PendingCOUnitRate : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.PendingCOCommittedQty : Edm.Decimal [required] "Pending CO Committed Quantity"
PX.Objects.PM.PMCostProjectionByDateLine.CuryPendingCOCommittedUnitRate : Edm.Decimal [required] "Pending CO Committed Unit Rate"
PX.Objects.PM.PMCostProjectionByDateLine.PendingCOCommittedUnitRate : Edm.Decimal [required]
PX.Objects.PM.PMCostProjectionByDateLine.AnticipatedQty : Edm.Decimal "Anticipated Quantity"
PX.Objects.PM.PMCostProjectionByDateLine.CuryAnticipatedUnitRate : Edm.Decimal "Anticipated Unit Rate"
PX.Objects.PM.PMCostProjectionByDateLine.AnticipatedUnitRate : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.QtyPerformance : Edm.Decimal "Quantity Performance (%)"
PX.Objects.PM.PMCostProjectionByDateLine.AnticipatedQtyPerformance : Edm.Decimal "Anticipated Quantity Performance (%)"
PX.Objects.PM.PMCostProjectionByDateLine.ProjectedQtyVariance : Edm.Decimal "Projected Quantity Variance"
PX.Objects.PM.PMCostProjectionByDateLine.CuryProjectedCostVariance : Edm.Decimal "Projected Cost Variance"
PX.Objects.PM.PMCostProjectionByDateLine.ProjectedCostVariance : Edm.Decimal
PX.Objects.PM.PMCostProjectionByDateLine.IsHeader : Edm.Boolean
PX.Objects.PM.PMCostProjectionByDateLine.NoteID : Edm.Guid
PX.Objects.PM.PMCostProjectionByDateLine.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMCostProjectionByDateLine.tstamp : Edm.Binary
PX.Objects.PM.PMCostProjectionByDateLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMCostProjectionByDateLine.CreatedByScreenID : Edm.String
PX.Objects.PM.PMCostProjectionByDateLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMCostProjectionByDateLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMCostProjectionByDateLine.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMCostProjectionByDateLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMCostProjectionByDateLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMCostProjectionByDateLine.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.PM.PMCostProjectionByDateLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PM.PMCostProjectionByDateLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMCostProjectionByDateLine.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMCostProjectionByDateLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMCostProjectionByDateLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMCostProjectionByDateLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMCostProjectionByDateLine.PMCostProjectionByDateByRefNbr -> PX.Objects.PM.PMCostProjectionByDate (RefNbr=RefNbr)
PX.Objects.PM.PMCostProjectionByDateLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.PM.PMCostProjectionClass (EntityType)

Label: "Cost Projection Class"
Key: ClassID
Entity sets: PX_Objects_PM_PMCostProjectionClass, CostProjectionClass, PMCostProjectionClass
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMCostProjectionClass.ClassID : Edm.String [key] "Class ID"
PX.Objects.PM.PMCostProjectionClass.Description : Edm.String "Description"
PX.Objects.PM.PMCostProjectionClass.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMCostProjectionClass.TaskID : Edm.Boolean [required] "Cost Task"
PX.Objects.PM.PMCostProjectionClass.AccountGroupID : Edm.Boolean [required] "Account Group"
PX.Objects.PM.PMCostProjectionClass.InventoryID : Edm.Boolean [required] "Inventory ID"
PX.Objects.PM.PMCostProjectionClass.NoteID : Edm.Guid
PX.Objects.PM.PMCostProjectionClass.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMCostProjectionClass.tstamp : Edm.Binary
PX.Objects.PM.PMCostProjectionClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMCostProjectionClass.CreatedByScreenID : Edm.String
PX.Objects.PM.PMCostProjectionClass.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMCostProjectionClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMCostProjectionClass.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMCostProjectionClass.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMCostProjectionClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMCostProjectionClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMCostProjectionClass.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)

# PX.Objects.PM.PMCostProjectionLine (EntityType)

Label: "Cost Projection Line"
Key: LineNbr, ProjectID, RevisionID
Entity sets: PX_Objects_PM_PMCostProjectionLine, CostProjectionLine, PMCostProjectionLine
Non-filterable, non-selectable: CompletedQuantity, CompletedAmount, QuantityToComplete, AmountToComplete, NoteText

PX.Objects.PM.PMCostProjectionLine.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMCostProjectionLine.RevisionID : Edm.String [key] "Revision"
PX.Objects.PM.PMCostProjectionLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMCostProjectionLine.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMCostProjectionLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMCostProjectionLine.Description : Edm.String "Description"
PX.Objects.PM.PMCostProjectionLine.UOM : Edm.String "UOM"
PX.Objects.PM.PMCostProjectionLine.BudgetedQuantity : Edm.Decimal [required] "Budgeted Quantity"
PX.Objects.PM.PMCostProjectionLine.BudgetedAmount : Edm.Decimal [required] "Budgeted Cost"
PX.Objects.PM.PMCostProjectionLine.ActualQuantity : Edm.Decimal [required] "Actual Quantity"
PX.Objects.PM.PMCostProjectionLine.ActualAmount : Edm.Decimal [required] "Actual Cost"
PX.Objects.PM.PMCostProjectionLine.UnbilledQuantity : Edm.Decimal [required] "Committed Open Quantity"
PX.Objects.PM.PMCostProjectionLine.UnbilledAmount : Edm.Decimal [required] "Committed Open Cost"
PX.Objects.PM.PMCostProjectionLine.CompletedQuantity : Edm.Decimal "Actual + Committed Open Quantity"
PX.Objects.PM.PMCostProjectionLine.CompletedAmount : Edm.Decimal "Actual + Committed Open Cost"
PX.Objects.PM.PMCostProjectionLine.QuantityToComplete : Edm.Decimal "Quantity to Complete"
PX.Objects.PM.PMCostProjectionLine.AmountToComplete : Edm.Decimal "Cost to Complete"
PX.Objects.PM.PMCostProjectionLine.Mode : Edm.String "Mode"
PX.Objects.PM.PMCostProjectionLine.Quantity : Edm.Decimal [required] "Projected Quantity to Complete"
PX.Objects.PM.PMCostProjectionLine.Amount : Edm.Decimal [required] "Projected Cost to Complete"
PX.Objects.PM.PMCostProjectionLine.ProjectedQuantity : Edm.Decimal [required] "Projected Quantity at Completion"
PX.Objects.PM.PMCostProjectionLine.ProjectedAmount : Edm.Decimal [required] "Projected Cost at Completion"
PX.Objects.PM.PMCostProjectionLine.VarianceQuantity : Edm.Decimal [required] "Projected Variance Quantity"
PX.Objects.PM.PMCostProjectionLine.VarianceAmount : Edm.Decimal [required] "Projected Variance Cost"
PX.Objects.PM.PMCostProjectionLine.CompletedPct : Edm.Decimal [required] "Projected Completed (%)"
PX.Objects.PM.PMCostProjectionLine.NoteID : Edm.Guid
PX.Objects.PM.PMCostProjectionLine.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMCostProjectionLine.tstamp : Edm.Binary
PX.Objects.PM.PMCostProjectionLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMCostProjectionLine.CreatedByScreenID : Edm.String
PX.Objects.PM.PMCostProjectionLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMCostProjectionLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMCostProjectionLine.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMCostProjectionLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMCostProjectionLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMCostProjectionLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMCostProjectionLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMCostProjectionLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMCostProjectionLine.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMCostProjectionLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMCostProjectionLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMCostProjectionLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMCostProjectionLine.PMCostProjectionByRevisionID -> PX.Objects.PM.PMCostProjection (ProjectID=ProjectID, RevisionID=RevisionID)

# PX.Objects.PM.PMEmployeeRate (EntityType)

Label: "PM Item Employee"
Key: EmployeeID, RateCodeID, RateDefinitionID
Entity sets: PX_Objects_PM_PMEmployeeRate, PMItemEmployee, PMEmployeeRate

PX.Objects.PM.PMEmployeeRate.RateDefinitionID : Edm.Int32 [key]
PX.Objects.PM.PMEmployeeRate.RateCodeID : Edm.String [key]
PX.Objects.PM.PMEmployeeRate.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.PM.PMEmployeeRate.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.PM.PMEmployeeRate.PMRateSequenceByRateCodeID -> PX.Objects.PM.PMRateSequence (RateDefinitionID=RateDefinitionID, RateCodeID=RateCodeID)

# PX.Objects.PM.PMForecast (EntityType)

Label: "Budget Forecast"
Key: ProjectID, RevisionID
Entity sets: PX_Objects_PM_PMForecast, BudgetForecast, PMForecast
Non-filterable, non-selectable: FormCaptionDescription, NoteText

PX.Objects.PM.PMForecast.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.PMForecast.RevisionID : Edm.String [key] "Revision"
PX.Objects.PM.PMForecast.Description : Edm.String "Description"
PX.Objects.PM.PMForecast.FormCaptionDescription : Edm.String
PX.Objects.PM.PMForecast.NoteID : Edm.Guid
PX.Objects.PM.PMForecast.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMForecast.tstamp : Edm.Binary
PX.Objects.PM.PMForecast.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMForecast.CreatedByScreenID : Edm.String
PX.Objects.PM.PMForecast.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMForecast.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMForecast.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMForecast.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMForecast.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMForecast.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMForecast.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMForecast.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)

# PX.Objects.PM.PMForecastDetail (EntityType)

Label: "Budget Forecast Detail"
Key: AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID, RevisionID
Entity sets: PX_Objects_PM_PMForecastDetail, BudgetForecastDetail, PMForecastDetail
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMForecastDetail.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMForecastDetail.RevisionID : Edm.String [key] "Revision"
PX.Objects.PM.PMForecastDetail.ProjectTaskID : Edm.Int32 [key] "Project Task"
PX.Objects.PM.PMForecastDetail.AccountGroupID : Edm.Int32 [key] "Account Group"
PX.Objects.PM.PMForecastDetail.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.PM.PMForecastDetail.CostCodeID : Edm.Int32 [key] "Cost Code"
PX.Objects.PM.PMForecastDetail.PeriodID : Edm.String [key] "Financial Period"
PX.Objects.PM.PMForecastDetail.Description : Edm.String "Description"
PX.Objects.PM.PMForecastDetail.Qty : Edm.Decimal [required] "Original Budgeted Quantity"
PX.Objects.PM.PMForecastDetail.CuryAmount : Edm.Decimal [required] "Original Budgeted Amount"
PX.Objects.PM.PMForecastDetail.RevisedQty : Edm.Decimal [required] "Revised Budgeted Quantity"
PX.Objects.PM.PMForecastDetail.CuryRevisedAmount : Edm.Decimal [required] "Revised Budgeted Amount"
PX.Objects.PM.PMForecastDetail.NoteID : Edm.Guid
PX.Objects.PM.PMForecastDetail.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMForecastDetail.tstamp : Edm.Binary
PX.Objects.PM.PMForecastDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMForecastDetail.CreatedByScreenID : Edm.String
PX.Objects.PM.PMForecastDetail.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMForecastDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMForecastDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMForecastDetail.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMForecastDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMForecastDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PM.PMForecastDetail.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.PM.PMForecastDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMForecastDetail.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMForecastDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMForecastDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMForecastDetail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PM.PMForecastDetail.PMForecastByRevisionID -> PX.Objects.PM.PMForecast (ProjectID=ProjectID, RevisionID=RevisionID)
PX.Objects.PM.PMForecastDetail.MasterFinPeriodByPeriodID -> PX.Objects.GL.FinPeriods.MasterFinPeriod (PeriodID=FinPeriodID)

# PX.Objects.PM.PMForecastHistory (EntityType)

Label: "Budget Forecast History"
Key: AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_PM_PMForecastHistory, BudgetForecastHistory, PMForecastHistory

PX.Objects.PM.PMForecastHistory.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMForecastHistory.ProjectTaskID : Edm.Int32 [key]
PX.Objects.PM.PMForecastHistory.AccountGroupID : Edm.Int32 [key]
PX.Objects.PM.PMForecastHistory.InventoryID : Edm.Int32 [key]
PX.Objects.PM.PMForecastHistory.CostCodeID : Edm.Int32 [key]
PX.Objects.PM.PMForecastHistory.PeriodID : Edm.String [key]
PX.Objects.PM.PMForecastHistory.ActualQty : Edm.Decimal [required] "Actual Quantity"
PX.Objects.PM.PMForecastHistory.CuryArAmount : Edm.Decimal [required] "Actual Amount generated by AR Invoices"
PX.Objects.PM.PMForecastHistory.CuryActualAmount : Edm.Decimal [required] "Actual Amount"
PX.Objects.PM.PMForecastHistory.ActualAmount : Edm.Decimal [required] "Actual Amount in Base Currency"
PX.Objects.PM.PMForecastHistory.CuryInclTaxAmount : Edm.Decimal [required] "Inclusive Tax Amount"
PX.Objects.PM.PMForecastHistory.InclTaxAmount : Edm.Decimal [required] "Inclusive Tax Amount in Base Currency"
PX.Objects.PM.PMForecastHistory.tstamp : Edm.Binary

# PX.Objects.PM.PMForecastProject (EntityType)

Label: "Project"
Key: ContractID
Entity sets: PX_Objects_PM_PMForecastProject, Project1, PMForecastProject
Non-filterable, non-selectable: TotalBudgetedCompletedAmount, TotalBudgetedAmountToComplete, TotalBudgetedGrossProfit, TotalProjectedGrossProfit

PX.Objects.PM.PMForecastProject.ContractID : Edm.Int32 [key]
PX.Objects.PM.PMForecastProject.TotalBudgetedRevenueAmount : Edm.Decimal "Budgeted Revenue"
PX.Objects.PM.PMForecastProject.CuryCommittedCostAmount : Edm.Decimal "Committed Cost"
PX.Objects.PM.PMForecastProject.CuryActualCostAmount : Edm.Decimal "Actual Cost"
PX.Objects.PM.PMForecastProject.CuryCommittedInvoicedCostAmount : Edm.Decimal "Committed Invoiced Cost"
PX.Objects.PM.PMForecastProject.TotalBudgetedCostAmount : Edm.Decimal "Cost at Completion"
PX.Objects.PM.PMForecastProject.TotalBudgetedCompletedAmount : Edm.Decimal "Actual + Committed Costs"
PX.Objects.PM.PMForecastProject.TotalBudgetedAmountToComplete : Edm.Decimal "Cost to Complete"
PX.Objects.PM.PMForecastProject.TotalBudgetedGrossProfit : Edm.Decimal "Gross Profit"
PX.Objects.PM.PMForecastProject.TotalBudgetedVarianceAmount : Edm.Decimal "Cost Variance"
PX.Objects.PM.PMForecastProject.TotalProjectedGrossProfit : Edm.Decimal "Projected Gross Profit"
PX.Objects.PM.PMForecastProject.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.PM.PMForecastProject.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.PM.PMForecastProject.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.PM.PMForecastProject.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.PM.PMForecastProject.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMForecastProject.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.PM.PMForecastProject.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.PM.PMForecastProject.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.PM.PMForecastProject.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.PM.PMForecastProject.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.PM.PMForecastProject.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.Objects.PM.PMForecastProject.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.PM.PMForecastProject.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.Objects.PM.PMForecastProject.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.PM.PMForecastProject.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.PM.PMForecastProject.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.PM.PMForecastProject.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.PM.PMForecastProject.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.PM.PMForecastProject.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.PM.PMForecastProject.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.PM.PMForecastProject.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMForecastProject.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PM.PMForecastProject.LienWaiverRecipientCollection -> Collection(PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient)
PX.Objects.PM.PMForecastProject.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.PM.PMForecastProject.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.PM.PMForecastProject.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.PM.PMForecastProject.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.Objects.PM.PMForecastProject.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.PM.PMForecastProject.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.PM.PMForecastProject.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.PM.PMForecastProject.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.PM.PMForecastProject.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.PM.PMForecastProject.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.PM.PMForecastProject.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.PM.PMForecastProject.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.PM.PMForecastProject.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.PM.PMForecastProject.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.PM.PMForecastProject.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.PM.PMForecastProject.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.PM.PMForecastProject.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.PM.PMForecastProject.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.PM.PMForecastProject.PhotoLogCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog)
PX.Objects.PM.PMForecastProject.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.PM.PMForecastProject.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.Objects.PM.PMForecastProject.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PM.PMForecastProject.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PM.PMForecastProject.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.PM.PMForecastProject.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.PM.PMForecastProject.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.PM.PMForecastProject.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.PM.PMForecastProject.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.PM.PMForecastProject.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.Objects.PM.PMForecastProject.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.PM.PMForecastProject.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.PM.PMForecastProject.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.PM.PMForecastProject.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PM.PMForecastProject.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PM.PMForecastProject.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PM.PMForecastProject.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.PM.PMForecastProject.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.PM.PMForecastProject.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.PM.PMForecastProject.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.PM.PMForecastProject.PMAccountTaskCollection -> Collection(PX.Objects.PM.PMAccountTask)
PX.Objects.PM.PMForecastProject.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.PM.PMForecastProject.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)
PX.Objects.PM.PMForecastProject.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PM.PMForecastProject.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.PM.PMForecastProject.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.Objects.PM.PMForecastProject.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.PM.PMForecastProject.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.PM.PMForecastProject.PMForecastCollection -> Collection(PX.Objects.PM.PMForecast)
PX.Objects.PM.PMForecastProject.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.PM.PMForecastProject.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.PM.PMForecastProject.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.PM.PMForecastProject.PMProgressWorksheetCollection -> Collection(PX.Objects.PM.PMProgressWorksheet)
PX.Objects.PM.PMForecastProject.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.PM.PMForecastProject.PMProjectCostSpreadLineCollection -> Collection(PX.Objects.PM.PMProjectCostSpreadLine)
PX.Objects.PM.PMForecastProject.PMRetainageStepCollection -> Collection(PX.Objects.PM.PMRetainageStep)
PX.Objects.PM.PMForecastProject.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.PM.PMForecastProject.PMWorkCodeProjectTaskSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeProjectTaskSource)
PX.Objects.PM.PMForecastProject.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.PM.PMForecastProject.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.PM.PMForecastProject.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.PM.PMForecastProject.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.PM.PMForecastProject.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PM.PMForecastProject.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.PM.PMForecastProject.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.PM.PMForecastProject.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.Objects.PM.PMForecastProject.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.PM.PMForecastProject.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.PM.PMForecastProject.EPEarningTypeCollection -> Collection(PX.Objects.EP.EPEarningType)
PX.Objects.PM.PMForecastProject.EPEquipmentRateCollection -> Collection(PX.Objects.EP.EPEquipmentRate)
PX.Objects.PM.PMForecastProject.EPEquipmentSummaryCollection -> Collection(PX.Objects.EP.EPEquipmentSummary)
PX.Objects.PM.PMForecastProject.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.PM.PMForecastProject.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.PM.PMForecastProject.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.PM.PMForecastProject.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.PM.PMForecastProject.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.PM.PMForecastProject.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.PM.PMForecastProject.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.PM.PMForecastProject.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.PM.PMForecastProject.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.PM.PMForecastProject.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.PM.PMForecastProject.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.Objects.PM.PMForecastProject.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.PM.PMForecastProject.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.PM.PMForecastProject.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.PM.PMForecastProject.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.PM.PMForecastProject.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.PM.PMForecastProject.PRProjectFringeBenefitRateReducingDeductCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct)
PX.Objects.PM.PMForecastProject.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.PM.PMForecastProject.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.PM.PMForecastProject.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.PM.PMForecastProject.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.PM.PMForecastProject.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.PM.PMForecastProject.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.PM.PMForecastProject.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.PM.PMForecastProject.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.PM.PMForecastProject.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PM.PMForecastProject.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.PM.PMForecastProject.ProjectARTranCollection -> Collection(PX.Objects.PM.ProjectARTran)
PX.Objects.PM.PMForecastProject.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.PM.PMForecastProject.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.PM.PMForecastProject.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.PM.PMForecastProject.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.PM.PMForecastProject.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.PM.PMForecastProject.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.PM.PMForecastProject.PMProgressLineTotalCollection -> Collection(PX.Objects.PM.PMProgressLineTotal)
PX.Objects.PM.PMForecastProject.PMProjectUnionCollection -> Collection(PX.Objects.PM.PMProjectUnion)
PX.Objects.PM.PMForecastProject.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.PM.PMForecastProject.ProjectPMTranCollection -> Collection(PX.Objects.PM.ProjectPMTran)
PX.Objects.PM.PMForecastProject.ProjectGLTranCollection -> Collection(PX.Objects.PM.ProjectGLTran)
PX.Objects.PM.PMForecastProject.ProjectAPTranCollection -> Collection(PX.Objects.PM.ProjectAPTran)
PX.Objects.PM.PMForecastProject.ProjectINTranCollection -> Collection(PX.Objects.PM.ProjectINTran)
PX.Objects.PM.PMForecastProject.ProjectCASplitCollection -> Collection(PX.Objects.PM.ProjectCASplit)
PX.Objects.PM.PMForecastProject.ContactForCurrentProjectCollection -> Collection(PX.Objects.PJ.Common.DAC.ContactForCurrentProject)
PX.Objects.PM.PMForecastProject.PMMaterialListCollection -> Collection(PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList)
PX.Objects.PM.PMForecastProject.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.PM.PMForecastProject.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.PM.PMForecastProject.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.PM.PMForecastProject.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.PM.PMHistory (EntityType)

Label: "Project History"
Key: AccountGroupID, BranchID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_PM_PMHistory, ProjectHistory, PMHistory
Non-filterable, non-selectable: BranchID

PX.Objects.PM.PMHistory.ProjectID : Edm.Int32 [key] "Project ID"
PX.Objects.PM.PMHistory.ProjectTaskID : Edm.Int32 [key] "Project Task ID"
PX.Objects.PM.PMHistory.AccountGroupID : Edm.Int32 [key] "Account Group ID"
PX.Objects.PM.PMHistory.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.PM.PMHistory.CostCodeID : Edm.Int32 [key] "Cost Code"
PX.Objects.PM.PMHistory.PeriodID : Edm.String [key] "Financial Period"
PX.Objects.PM.PMHistory.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.PM.PMHistory.FinPTDQty : Edm.Decimal [required] "Financial PTD Quantity"
PX.Objects.PM.PMHistory.TranPTDQty : Edm.Decimal [required]
PX.Objects.PM.PMHistory.FinPTDCuryAmount : Edm.Decimal [required] "Financial PTD Amount"
PX.Objects.PM.PMHistory.FinPTDAmount : Edm.Decimal [required] "Financial PTD Amount"
PX.Objects.PM.PMHistory.TranPTDCuryAmount : Edm.Decimal [required]
PX.Objects.PM.PMHistory.TranPTDAmount : Edm.Decimal [required]
PX.Objects.PM.PMHistory.FinYTDQty : Edm.Decimal [required]
PX.Objects.PM.PMHistory.TranYTDQty : Edm.Decimal [required]
PX.Objects.PM.PMHistory.FinYTDCuryAmount : Edm.Decimal [required]
PX.Objects.PM.PMHistory.FinYTDAmount : Edm.Decimal [required]
PX.Objects.PM.PMHistory.TranYTDCuryAmount : Edm.Decimal [required]
PX.Objects.PM.PMHistory.TranYTDAmount : Edm.Decimal [required]
PX.Objects.PM.PMHistory.tstamp : Edm.Binary
PX.Objects.PM.PMHistory.MasterFinPeriodByPeriodID -> PX.Objects.GL.FinPeriods.MasterFinPeriod (PeriodID=FinPeriodID)

# PX.Objects.PM.PMHistoryByDate (EntityType)

Label: "Project History By Date"
Key: AccountGroupID, CostCodeID, Date, InventoryID, PeriodID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_PM_PMHistoryByDate, ProjectHistoryByDate, PMHistoryByDate
Non-filterable, non-selectable: GroupID

PX.Objects.PM.PMHistoryByDate.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMHistoryByDate.ProjectTaskID : Edm.Int32 [key]
PX.Objects.PM.PMHistoryByDate.AccountGroupID : Edm.Int32 [key]
PX.Objects.PM.PMHistoryByDate.InventoryID : Edm.Int32 [key]
PX.Objects.PM.PMHistoryByDate.CostCodeID : Edm.Int32 [key]
PX.Objects.PM.PMHistoryByDate.BudgetInventoryID : Edm.Int32
PX.Objects.PM.PMHistoryByDate.BudgetCostCodeID : Edm.Int32
PX.Objects.PM.PMHistoryByDate.Date : Edm.DateTimeOffset [key]
PX.Objects.PM.PMHistoryByDate.PeriodID : Edm.String [key]
PX.Objects.PM.PMHistoryByDate.Year : Edm.Int32
PX.Objects.PM.PMHistoryByDate.Quarter : Edm.Int32
PX.Objects.PM.PMHistoryByDate.Month : Edm.Int32
PX.Objects.PM.PMHistoryByDate.Week : Edm.Int32
PX.Objects.PM.PMHistoryByDate.WeekOfYear : Edm.Int32
PX.Objects.PM.PMHistoryByDate.Day : Edm.Int32
PX.Objects.PM.PMHistoryByDate.ActualQty : Edm.Decimal [required]
PX.Objects.PM.PMHistoryByDate.UOM : Edm.String "UOM"
PX.Objects.PM.PMHistoryByDate.CuryActualAmount : Edm.Decimal [required] "Amount"
PX.Objects.PM.PMHistoryByDate.ActualAmount : Edm.Decimal [required]
PX.Objects.PM.PMHistoryByDate.tstamp : Edm.Binary
PX.Objects.PM.PMHistoryByDate.GroupID : Edm.Int32
PX.Objects.PM.PMHistoryByDate.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMHistoryByDate.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.PM.PMHistoryByDate.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMHistoryByDate.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMHistoryByDate.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PM.PMHistoryByDate.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.PM.PMItemRate (EntityType)

Label: "PM Item Rate"
Key: InventoryID, RateCodeID, RateDefinitionID
Entity sets: PX_Objects_PM_PMItemRate, PMItemRate

PX.Objects.PM.PMItemRate.RateDefinitionID : Edm.Int32 [key]
PX.Objects.PM.PMItemRate.RateCodeID : Edm.String [key]
PX.Objects.PM.PMItemRate.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.PM.PMItemRate.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMItemRate.PMRateSequenceByRateCodeID -> PX.Objects.PM.PMRateSequence (RateDefinitionID=RateDefinitionID, RateCodeID=RateCodeID)

# PX.Objects.PM.PMLaborCostRate (EntityType)

Label: "Labor Cost Rates"
Key: RecordID
Entity sets: PX_Objects_PM_PMLaborCostRate, LaborCostRates, PMLaborCostRate
Non-filterable, non-selectable: UOM, NoteText

PX.Objects.PM.PMLaborCostRate.RecordID : Edm.Int32 [key]
PX.Objects.PM.PMLaborCostRate.Type : Edm.String "Labor Rate Type"
PX.Objects.PM.PMLaborCostRate.UnionID : Edm.String "Union Local"
PX.Objects.PM.PMLaborCostRate.EmployeeID : Edm.Int32 "Employee"
PX.Objects.PM.PMLaborCostRate.InventoryID : Edm.Int32 "Labor Item"
PX.Objects.PM.PMLaborCostRate.Description : Edm.String "Description"
PX.Objects.PM.PMLaborCostRate.EmploymentType : Edm.String "Type of Employment"
PX.Objects.PM.PMLaborCostRate.RegularHours : Edm.Decimal "Regular Hours per week"
PX.Objects.PM.PMLaborCostRate.AnnualSalary : Edm.Decimal "Annual Rate"
PX.Objects.PM.PMLaborCostRate.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.PM.PMLaborCostRate.UOM : Edm.String "UOM"
PX.Objects.PM.PMLaborCostRate.WageRate : Edm.Decimal [required] "Wage Rate"
PX.Objects.PM.PMLaborCostRate.BurdenRate : Edm.Decimal [required] "Burden Rate"
PX.Objects.PM.PMLaborCostRate.Rate : Edm.Decimal [required] "Cost Rate"
PX.Objects.PM.PMLaborCostRate.CuryID : Edm.String "Currency"
PX.Objects.PM.PMLaborCostRate.ExtRefNbr : Edm.String "External Ref. Nbr"
PX.Objects.PM.PMLaborCostRate.NoteID : Edm.Guid
PX.Objects.PM.PMLaborCostRate.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMLaborCostRate.tstamp : Edm.Binary
PX.Objects.PM.PMLaborCostRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMLaborCostRate.CreatedByScreenID : Edm.String
PX.Objects.PM.PMLaborCostRate.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMLaborCostRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMLaborCostRate.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMLaborCostRate.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMLaborCostRate.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.PM.PMLaborCostRate.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMLaborCostRate.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMLaborCostRate.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMLaborCostRate.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.PM.PMLaborCostRate.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMLaborCostRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMLaborCostRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMLaborCostRate.PMUnionByUnionID -> PX.Objects.PM.PMUnion (UnionID=UnionID)
PX.Objects.PM.PMLaborCostRate.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)

# PX.Objects.PM.PMMarkup (EntityType)

Label: "Markup"
Key: LineNbr, ProjectID
Entity sets: PX_Objects_PM_PMMarkup, Markup2, PMMarkup
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMMarkup.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMMarkup.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMMarkup.Type : Edm.String "Type"
PX.Objects.PM.PMMarkup.Description : Edm.String "Description"
PX.Objects.PM.PMMarkup.Value : Edm.Decimal "Value"
PX.Objects.PM.PMMarkup.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMMarkup.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMMarkup.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.PMMarkup.NoteID : Edm.Guid
PX.Objects.PM.PMMarkup.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMMarkup.tstamp : Edm.Binary
PX.Objects.PM.PMMarkup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMMarkup.CreatedByScreenID : Edm.String
PX.Objects.PM.PMMarkup.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMMarkup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMMarkup.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMMarkup.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMMarkup.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMMarkup.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMMarkup.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMMarkup.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMMarkup.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMMarkup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMMarkup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMMarkup.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)

# PX.Objects.PM.PMPOHistoryByDate (EntityType)

Label: "Project Commitment History"
Key: COLineNbr, CONbr, Date, POLineNbr, POOrderNbr, POOrderType, RecordType
Entity sets: PX_Objects_PM_PMPOHistoryByDate, ProjectCommitmentHistory, PMPOHistoryByDate

PX.Objects.PM.PMPOHistoryByDate.RecordType : Edm.String [key] "Record Type"
PX.Objects.PM.PMPOHistoryByDate.POOrderType : Edm.String [key] "Commitment Doc. Type"
PX.Objects.PM.PMPOHistoryByDate.POOrderNbr : Edm.String [key] "Commitment Ref. Nbr."
PX.Objects.PM.PMPOHistoryByDate.POLineNbr : Edm.Int32 [key] "Commitment Line Nbr."
PX.Objects.PM.PMPOHistoryByDate.CONbr : Edm.String [key]
PX.Objects.PM.PMPOHistoryByDate.COLineNbr : Edm.Int32 [key]
PX.Objects.PM.PMPOHistoryByDate.Date : Edm.DateTimeOffset [key] "Date"
PX.Objects.PM.PMPOHistoryByDate.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMPOHistoryByDate.InventoryID : Edm.Int32
PX.Objects.PM.PMPOHistoryByDate.BudgetInventoryID : Edm.Int32
PX.Objects.PM.PMPOHistoryByDate.CuryID : Edm.String
PX.Objects.PM.PMPOHistoryByDate.BaseCuryInfoID : Edm.Int64
PX.Objects.PM.PMPOHistoryByDate.ProjectCuryInfoID : Edm.Int64
PX.Objects.PM.PMPOHistoryByDate.UOM : Edm.String "UOM"
PX.Objects.PM.PMPOHistoryByDate.VendorID : Edm.Int32 "Vendor"
PX.Objects.PM.PMPOHistoryByDate.CommittedQty : Edm.Decimal [required] "Committed Qty."
PX.Objects.PM.PMPOHistoryByDate.BudgetCommittedQty : Edm.Decimal "Committed Qty."
PX.Objects.PM.PMPOHistoryByDate.CommittedCOQty : Edm.Decimal [required]
PX.Objects.PM.PMPOHistoryByDate.BudgetCommittedCOQty : Edm.Decimal
PX.Objects.PM.PMPOHistoryByDate.ProjectCuryCommittedAmt : Edm.Decimal [required] "Committed Amount (Project Curr.)"
PX.Objects.PM.PMPOHistoryByDate.ProjectCuryCommittedCOAmt : Edm.Decimal [required]
PX.Objects.PM.PMPOHistoryByDate.CommittedCOAmt : Edm.Decimal [required]
PX.Objects.PM.PMPOHistoryByDate.ProjectCuryCommittedCORetainage : Edm.Decimal [required]
PX.Objects.PM.PMPOHistoryByDate.CommittedCORetainage : Edm.Decimal [required]
PX.Objects.PM.PMPOHistoryByDate.ProjectCuryCommittedUnitCost : Edm.Decimal "Committed Unit Cost (Project Curr.)"
PX.Objects.PM.PMPOHistoryByDate.CommittedUnitCost : Edm.Decimal "Committed Unit Cost (Base Curr.)"
PX.Objects.PM.PMPOHistoryByDate.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMPOHistoryByDate.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMPOHistoryByDate.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PM.PMPOHistoryByDate.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMPOHistoryByDate.InventoryItemByBudgetInventoryID -> PX.Objects.IN.InventoryItem (BudgetInventoryID=InventoryID)
PX.Objects.PM.PMPOHistoryByDate.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMPOHistoryByDate.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PM.PMPOHistoryByDate.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.PM.PMProfitHistoryByDate (EntityType)

Label: "PMProfitHistoryByDate"
Key: AccountGroupID, ProjectID, TaskID
Entity sets: PX_Objects_PM_PMProfitHistoryByDate, PMProfitHistoryByDate

PX.Objects.PM.PMProfitHistoryByDate.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMProfitHistoryByDate.TaskID : Edm.Int32 [key]
PX.Objects.PM.PMProfitHistoryByDate.AccountGroupID : Edm.Int32 [key]
PX.Objects.PM.PMProfitHistoryByDate.AccountGroupType : Edm.String
PX.Objects.PM.PMProfitHistoryByDate.ReportGroup : Edm.String
PX.Objects.PM.PMProfitHistoryByDate.CuryActualAmount : Edm.Decimal
PX.Objects.PM.PMProfitHistoryByDate.Date : Edm.DateTimeOffset
PX.Objects.PM.PMProfitHistoryByDate.CuryContractToDate : Edm.Decimal "Billed Amount to Date"
PX.Objects.PM.PMProfitHistoryByDate.CuryCostToDate : Edm.Decimal "Actual Costs to Date"
PX.Objects.PM.PMProfitHistoryByDate.CuryProfitToDate : Edm.Decimal "Profit to Date"
PX.Objects.PM.PMProfitHistoryByDate.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMProfitHistoryByDate.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)

# PX.Objects.PM.PMProforma (EntityType)

Label: "Pro Forma Invoice"
Key: RefNbr, RevisionID
Entity sets: PX_Objects_PM_PMProforma, ProFormaInvoice, PMProforma
Non-filterable, non-selectable: CuryTaxTotalWithRetainage, ARInvoiceRefName, NoteText, CuryRate

PX.Objects.PM.PMProforma.RevisionID : Edm.Int32 [key required] "Revision"
PX.Objects.PM.PMProforma.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMProforma.Description : Edm.String "Description"
PX.Objects.PM.PMProforma.Status : Edm.String "Status"
PX.Objects.PM.PMProforma.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PM.PMProforma.Approved : Edm.Boolean [required]
PX.Objects.PM.PMProforma.Rejected : Edm.Boolean [required]
PX.Objects.PM.PMProforma.CustomerID : Edm.Int32 "Customer"
PX.Objects.PM.PMProforma.BillAddressID : Edm.Int32
PX.Objects.PM.PMProforma.BillContactID : Edm.Int32 "Billing Contact"
PX.Objects.PM.PMProforma.ShipAddressID : Edm.Int32
PX.Objects.PM.PMProforma.ShipContactID : Edm.Int32 "Shipping Contact"
PX.Objects.PM.PMProforma.TaxZoneID : Edm.String "Customer Tax Zone"
PX.Objects.PM.PMProforma.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.PM.PMProforma.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.PM.PMProforma.CuryID : Edm.String "Currency"
PX.Objects.PM.PMProforma.CuryInfoID : Edm.Int64
PX.Objects.PM.PMProforma.InvoiceNbr : Edm.String "Customer Order Nbr."
PX.Objects.PM.PMProforma.InvoiceDate : Edm.DateTimeOffset "Invoice Date"
PX.Objects.PM.PMProforma.FinPeriodID : Edm.String "Post Period"
PX.Objects.PM.PMProforma.TermsID : Edm.String "Terms"
PX.Objects.PM.PMProforma.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.PM.PMProforma.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.PM.PMProforma.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMProforma.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMProforma.LineCntr : Edm.Int32 [required]
PX.Objects.PM.PMProforma.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMProforma.Corrected : Edm.Boolean [required] "Corrected"
PX.Objects.PM.PMProforma.EnableProgressive : Edm.Boolean [required] "Enable Progressive Tab"
PX.Objects.PM.PMProforma.EnableTransactional : Edm.Boolean [required] "Enable Transactions Tab"
PX.Objects.PM.PMProforma.ExtRefNbr : Edm.String "External Ref. Nbr"
PX.Objects.PM.PMProforma.CuryTransactionalTotal : Edm.Decimal [required] "Time and Material Total"
PX.Objects.PM.PMProforma.TransactionalTotal : Edm.Decimal [required] "Time and Material Total in Base Currency"
PX.Objects.PM.PMProforma.CuryProgressiveTotal : Edm.Decimal [required] "Progress Billing Total"
PX.Objects.PM.PMProforma.ProgressiveTotal : Edm.Decimal [required] "Progress Billing Total in Base Currency"
PX.Objects.PM.PMProforma.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.PM.PMProforma.TaxTotal : Edm.Decimal [required] "Tax Total in Base Currency"
PX.Objects.PM.PMProforma.CuryTaxInclTotal : Edm.Decimal [required] "Inclusive Tax Total"
PX.Objects.PM.PMProforma.TaxInclTotal : Edm.Decimal [required] "Inclusive Tax Total in Base Currency"
PX.Objects.PM.PMProforma.CuryTaxTotalWithRetainage : Edm.Decimal "Tax Total"
PX.Objects.PM.PMProforma.CuryDocTotal : Edm.Decimal [required] "Invoice Total"
PX.Objects.PM.PMProforma.DocTotal : Edm.Decimal [required] "Invoice Total in Base Currency"
PX.Objects.PM.PMProforma.AllocatedRetainedTotal : Edm.Decimal [required]
PX.Objects.PM.PMProforma.RetainagePct : Edm.Decimal [required] "Retainage (%)"
PX.Objects.PM.PMProforma.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.PM.PMProforma.IsAIAOutdated : Edm.Boolean [required] "AIA Is Outdated"
PX.Objects.PM.PMProforma.ARInvoiceDocType : Edm.String "AR Doc. Type"
PX.Objects.PM.PMProforma.ARInvoiceRefNbr : Edm.String "AR Ref. Nbr."
PX.Objects.PM.PMProforma.ARInvoiceRefStatus : Edm.String "AR Doc. Status"
PX.Objects.PM.PMProforma.ARInvoiceRefName : Edm.String "AR Ref. Nbr."
PX.Objects.PM.PMProforma.ReversedARInvoiceDocType : Edm.String "Reversing Doc. Type"
PX.Objects.PM.PMProforma.ReversedARInvoiceRefNbr : Edm.String "Reversing Ref. Nbr."
PX.Objects.PM.PMProforma.IsMigratedRecord : Edm.Boolean [required] "Migrated"
PX.Objects.PM.PMProforma.NumberOfLines : Edm.Int32
PX.Objects.PM.PMProforma.NoteID : Edm.Guid
PX.Objects.PM.PMProforma.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMProforma.tstamp : Edm.Binary
PX.Objects.PM.PMProforma.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProforma.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProforma.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProforma.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProforma.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProforma.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMProforma.CuryRate : Edm.Decimal
PX.Objects.PM.PMProforma.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMProforma.ARInvoiceByARInvoiceDocType -> PX.Objects.AR.ARInvoice (ARInvoiceRefNbr=RefNbr, CustomerID=CustomerID, ARInvoiceDocType=DocType)
PX.Objects.PM.PMProforma.ARInvoiceByReversedARInvoiceDocType -> PX.Objects.AR.ARInvoice (ReversedARInvoiceRefNbr=RefNbr, ReversedARInvoiceDocType=DocType)
PX.Objects.PM.PMProforma.PMContactByShipContactID -> PX.Objects.PM.PMContact (ShipContactID=ContactID)
PX.Objects.PM.PMProforma.PMContactByBillContactID -> PX.Objects.PM.PMContact (BillContactID=ContactID)
PX.Objects.PM.PMProforma.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.PM.PMProforma.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PM.PMProforma.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PM.PMProforma.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProforma.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProforma.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMProforma.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PM.PMProforma.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.PM.PMProforma.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PM.PMProforma.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.PM.PMProforma.PMTaxCollection -> Collection(PX.Objects.PM.PMTax)
PX.Objects.PM.PMProforma.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.PM.PMProforma.PMTaxTranCollection -> Collection(PX.Objects.PM.PMTaxTran)
PX.Objects.PM.PMProforma.PMBillingRecordCollection -> Collection(PX.Objects.PM.PMBillingRecord)

# PX.Objects.PM.PMProformaLine (EntityType)

Label: "Pro Forma Line"
Key: LineNbr, RefNbr, RevisionID
Entity sets: PX_Objects_PM_PMProformaLine, ProFormaLine, PMProformaLine
Non-filterable, non-selectable: CompletedPct, CurrentInvoicedPct, NoteText

PX.Objects.PM.PMProformaLine.RefNbr : Edm.String [key] "Ref. Number"
PX.Objects.PM.PMProformaLine.RevisionID : Edm.Int32 [key] "Revision"
PX.Objects.PM.PMProformaLine.LineNbr : Edm.Int32 [key] "Line Number"
PX.Objects.PM.PMProformaLine.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.PM.PMProformaLine.Type : Edm.String
PX.Objects.PM.PMProformaLine.BranchID : Edm.Int32 "Branch"
PX.Objects.PM.PMProformaLine.Description : Edm.String "Description"
PX.Objects.PM.PMProformaLine.ProjectID : Edm.Int32
PX.Objects.PM.PMProformaLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMProformaLine.AccountGroupID : Edm.Int32
PX.Objects.PM.PMProformaLine.OrigAccountGroupID : Edm.Int32
PX.Objects.PM.PMProformaLine.MergedToLineNbr : Edm.Int32 "Progress Billing Line Nbr."
PX.Objects.PM.PMProformaLine.ResourceID : Edm.Int32 "Employee"
PX.Objects.PM.PMProformaLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.PM.PMProformaLine.Date : Edm.DateTimeOffset "Date"
PX.Objects.PM.PMProformaLine.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.PMProformaLine.UOM : Edm.String "UOM"
PX.Objects.PM.PMProformaLine.CuryInfoID : Edm.Int64
PX.Objects.PM.PMProformaLine.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.PM.PMProformaLine.UnitPrice : Edm.Decimal [required] "Unit Price in Base Currency"
PX.Objects.PM.PMProformaLine.CompletedPct : Edm.Decimal "Total Completed (%)"
PX.Objects.PM.PMProformaLine.CurrentInvoicedPct : Edm.Decimal "Currently Invoiced (%)"
PX.Objects.PM.PMProformaLine.BillableQty : Edm.Decimal [required] "Billed Quantity"
PX.Objects.PM.PMProformaLine.CuryBillableAmount : Edm.Decimal [required] "Billed Amount"
PX.Objects.PM.PMProformaLine.BillableAmount : Edm.Decimal [required] "Billed Amount in Base Currency"
PX.Objects.PM.PMProformaLine.Qty : Edm.Decimal [required] "Quantity to Invoice"
PX.Objects.PM.PMProformaLine.CuryMergedAmount : Edm.Decimal [required] "Amount Included in Progress Billing"
PX.Objects.PM.PMProformaLine.MergedAmount : Edm.Decimal [required]
PX.Objects.PM.PMProformaLine.CuryTimeMaterialAmount : Edm.Decimal [required] "Time and Material Amount"
PX.Objects.PM.PMProformaLine.TimeMaterialAmount : Edm.Decimal [required] "Time and Material Amount in Base Currency"
PX.Objects.PM.PMProformaLine.CuryLineTotal : Edm.Decimal [required] "Amount to Invoice"
PX.Objects.PM.PMProformaLine.LineTotal : Edm.Decimal [required] "Amount To Invoice in Base Currency"
PX.Objects.PM.PMProformaLine.AllocatedRetainedAmount : Edm.Decimal [required]
PX.Objects.PM.PMProformaLine.Option : Edm.String "Status"
PX.Objects.PM.PMProformaLine.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMProformaLine.Corrected : Edm.Boolean [required] "Corrected"
PX.Objects.PM.PMProformaLine.Merged : Edm.Boolean [required] "Include in Progress Billing"
PX.Objects.PM.PMProformaLine.ARInvoiceDocType : Edm.String
PX.Objects.PM.PMProformaLine.ARInvoiceRefNbr : Edm.String
PX.Objects.PM.PMProformaLine.ARInvoiceLineNbr : Edm.Int32
PX.Objects.PM.PMProformaLine.ChangeOrderRefNbr : Edm.String "Change Order Nbr."
PX.Objects.PM.PMProformaLine.ChangeOrderLineNbr : Edm.Int32 "Change Order Line Nbr."
PX.Objects.PM.PMProformaLine.ProgressBillingBase : Edm.String "Progress Billing Basis"
PX.Objects.PM.PMProformaLine.CuryPreviouslyInvoiced : Edm.Decimal "Previously Invoiced Amount"
PX.Objects.PM.PMProformaLine.PreviouslyInvoiced : Edm.Decimal "Previously Invoiced in Base Currency"
PX.Objects.PM.PMProformaLine.PreviouslyInvoicedQty : Edm.Decimal "Previously Invoiced Quantity"
PX.Objects.PM.PMProformaLine.ActualQty : Edm.Decimal "Actual Quantity"
PX.Objects.PM.PMProformaLine.NoteID : Edm.Guid
PX.Objects.PM.PMProformaLine.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMProformaLine.tstamp : Edm.Binary
PX.Objects.PM.PMProformaLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProformaLine.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProformaLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProformaLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProformaLine.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProformaLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMProformaLine.EPEmployeeByResourceID -> PX.Objects.EP.EPEmployee (ResourceID=BAccountID)
PX.Objects.PM.PMProformaLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMProformaLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMProformaLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMProformaLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PM.PMProformaLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMProformaLine.DRDeferredCodeByDefCode -> PX.Objects.DR.DRDeferredCode
PX.Objects.PM.PMProformaLine.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMProformaLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.PM.PMProformaLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProformaLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProformaLine.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PM.PMProformaLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMProformaLine.PMProformaByRevisionID -> PX.Objects.PM.PMProforma (RefNbr=RefNbr, RevisionID=RevisionID)
PX.Objects.PM.PMProformaLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PM.PMProformaLine.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMProformaLine.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMProformaLine.PMTaxCollection -> Collection(PX.Objects.PM.PMTax)

# PX.Objects.PM.PMProformaLineWithPrevious (EntityType)

Label: "Pro Forma Line"
BaseType: PX.Objects.PM.PMProformaLine
Key: LineNbr, RefNbr, RevisionID (inherited from PX.Objects.PM.PMProformaLine)
Entity sets: PX_Objects_PM_PMProformaLineWithPrevious, ProFormaLine1, PMProformaLineWithPrevious
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.PM.PMProformaLineWithPrevious.QuantityBaseCompletedPct : Edm.Decimal "Total Completed (%)"

# PX.Objects.PM.PMProformaProgressLine (EntityType)

Label: "Pro Forma Line"
BaseType: PX.Objects.PM.PMProformaLine
Key: LineNbr, RefNbr, RevisionID (inherited from PX.Objects.PM.PMProformaLine)
Entity sets: PX_Objects_PM_PMProformaProgressLine, ProFormaLine2, PMProformaProgressLine

# PX.Objects.PM.PMProformaRevision (EntityType)

Label: "Pro Forma Invoice Revision"
Key: RefNbr, RevisionID
Entity sets: PX_Objects_PM_PMProformaRevision, ProFormaInvoiceRevision, PMProformaRevision

PX.Objects.PM.PMProformaRevision.RefNbr : Edm.String [key]
PX.Objects.PM.PMProformaRevision.RevisionID : Edm.Int32 [key] "Revision"
PX.Objects.PM.PMProformaRevision.Description : Edm.String "Description"
PX.Objects.PM.PMProformaRevision.CuryInfoID : Edm.Int64
PX.Objects.PM.PMProformaRevision.CuryDocTotal : Edm.Decimal "Invoice Total"
PX.Objects.PM.PMProformaRevision.DocTotal : Edm.Decimal "Invoice Total in Base Currency"
PX.Objects.PM.PMProformaRevision.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.PM.PMProformaRevision.TaxTotal : Edm.Decimal "Tax Total in Base Currency"
PX.Objects.PM.PMProformaRevision.ARInvoiceDocType : Edm.String "AR Doc. Type"
PX.Objects.PM.PMProformaRevision.ARInvoiceRefNbr : Edm.String "AR Ref. Nbr."
PX.Objects.PM.PMProformaRevision.ReversedARInvoiceDocType : Edm.String "Reversing Doc. Type"
PX.Objects.PM.PMProformaRevision.ReversedARInvoiceRefNbr : Edm.String "Reversing Ref. Nbr."
PX.Objects.PM.PMProformaRevision.ARInvoiceByARInvoiceDocType -> PX.Objects.AR.ARInvoice (ARInvoiceRefNbr=RefNbr, ARInvoiceDocType=DocType)
PX.Objects.PM.PMProformaRevision.ARInvoiceByReversedARInvoiceDocType -> PX.Objects.AR.ARInvoice (ReversedARInvoiceRefNbr=RefNbr, ReversedARInvoiceDocType=DocType)
PX.Objects.PM.PMProformaRevision.PMTaxCollection -> Collection(PX.Objects.PM.PMTax)
PX.Objects.PM.PMProformaRevision.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.PM.PMProformaRevision.PMTaxTranCollection -> Collection(PX.Objects.PM.PMTaxTran)
PX.Objects.PM.PMProformaRevision.PMBillingRecordCollection -> Collection(PX.Objects.PM.PMBillingRecord)

# PX.Objects.PM.PMProformaTransactLine (EntityType)

Label: "Pro Forma Line"
BaseType: PX.Objects.PM.PMProformaLine
Key: LineNbr, RefNbr, RevisionID (inherited from PX.Objects.PM.PMProformaLine)
Entity sets: PX_Objects_PM_PMProformaTransactLine, ProFormaLine3, PMProformaTransactLine
Non-filterable, non-selectable: CuryMaxAmount, MaxAmount, CuryAvailableAmount, AvailableAmount, CuryOverflowAmount, OverflowAmount

PX.Objects.PM.PMProformaTransactLine.CuryAmount : Edm.Decimal "Amount"
PX.Objects.PM.PMProformaTransactLine.CuryMaxAmount : Edm.Decimal "Max Limit Amount"
PX.Objects.PM.PMProformaTransactLine.MaxAmount : Edm.Decimal "Max Limit Amount in Base Currency"
PX.Objects.PM.PMProformaTransactLine.CuryAvailableAmount : Edm.Decimal "Max Available Amount"
PX.Objects.PM.PMProformaTransactLine.AvailableAmount : Edm.Decimal "Max Available Amount in Base Currency"
PX.Objects.PM.PMProformaTransactLine.CuryOverflowAmount : Edm.Decimal "Over-Limit Amount"
PX.Objects.PM.PMProformaTransactLine.OverflowAmount : Edm.Decimal "Overflow Amount in Base Currency"

# PX.Objects.PM.PMProgressLineTotal (EntityType)

Label: "Pro Forma Line"
Key: AccountGroupID, ProjectID, RefNbr, TaskID
Entity sets: PX_Objects_PM_PMProgressLineTotal, ProFormaLine4, PMProgressLineTotal

PX.Objects.PM.PMProgressLineTotal.RefNbr : Edm.String [key]
PX.Objects.PM.PMProgressLineTotal.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMProgressLineTotal.TaskID : Edm.Int32 [key]
PX.Objects.PM.PMProgressLineTotal.InventoryID : Edm.Int32
PX.Objects.PM.PMProgressLineTotal.CostCodeID : Edm.Int32
PX.Objects.PM.PMProgressLineTotal.AccountGroupID : Edm.Int32 [key]
PX.Objects.PM.PMProgressLineTotal.CuryMaterialStoredAmount : Edm.Decimal "Stored Material"
PX.Objects.PM.PMProgressLineTotal.MaterialStoredAmount : Edm.Decimal "Stored Material in Base Currency"
PX.Objects.PM.PMProgressLineTotal.CuryLineTotal : Edm.Decimal "Total"
PX.Objects.PM.PMProgressLineTotal.LineTotal : Edm.Decimal "Total in Base Currency"
PX.Objects.PM.PMProgressLineTotal.CuryRetainage : Edm.Decimal "Retainage"
PX.Objects.PM.PMProgressLineTotal.Retainage : Edm.Decimal "Retainage in Base Currency"
PX.Objects.PM.PMProgressLineTotal.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMProgressLineTotal.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.PM.PMProgressLineTotal.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMProgressLineTotal.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PM.PMProgressLineTotal.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMProgressLineTotal.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)

# PX.Objects.PM.PMProgressWorksheet (EntityType)

Label: "Progress Worksheet"
Key: RefNbr
Entity sets: PX_Objects_PM_PMProgressWorksheet, ProgressWorksheet, PMProgressWorksheet
Non-filterable, non-selectable: HiddenRefNbr, HiddenStatus, NoteText

PX.Objects.PM.PMProgressWorksheet.RefNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.PM.PMProgressWorksheet.Status : Edm.String "Status"
PX.Objects.PM.PMProgressWorksheet.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PM.PMProgressWorksheet.Approved : Edm.Boolean [required]
PX.Objects.PM.PMProgressWorksheet.Rejected : Edm.Boolean [required]
PX.Objects.PM.PMProgressWorksheet.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMProgressWorksheet.Date : Edm.DateTimeOffset "Date"
PX.Objects.PM.PMProgressWorksheet.LineCntr : Edm.Int32 [required]
PX.Objects.PM.PMProgressWorksheet.Hidden : Edm.Boolean [required]
PX.Objects.PM.PMProgressWorksheet.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMProgressWorksheet.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMProgressWorksheet.HiddenRefNbr : Edm.String "Worksheet Nbr."
PX.Objects.PM.PMProgressWorksheet.Description : Edm.String "Description"
PX.Objects.PM.PMProgressWorksheet.HiddenStatus : Edm.String "Status"
PX.Objects.PM.PMProgressWorksheet.NoteID : Edm.Guid
PX.Objects.PM.PMProgressWorksheet.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMProgressWorksheet.tstamp : Edm.Binary
PX.Objects.PM.PMProgressWorksheet.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProgressWorksheet.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProgressWorksheet.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProgressWorksheet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProgressWorksheet.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProgressWorksheet.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMProgressWorksheet.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMProgressWorksheet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProgressWorksheet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProgressWorksheet.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMProgressWorksheet.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.PM.PMProgressWorksheet.DailyFieldReportProgressWorksheetCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportProgressWorksheet)

# PX.Objects.PM.PMProgressWorksheetCostLine (EntityType)

Label: "Progress Worksheet Cost Line"
BaseType: PX.Objects.PM.PMProgressWorksheetLine
Key: LineNbr, RefNbr (inherited from PX.Objects.PM.PMProgressWorksheetLine)
Entity sets: PX_Objects_PM_PMProgressWorksheetCostLine, ProgressWorksheetCostLine, PMProgressWorksheetCostLine

# PX.Objects.PM.PMProgressWorksheetLine (EntityType)

Label: "Progress Worksheet Line"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PM_PMProgressWorksheetLine, ProgressWorksheetLine, PMProgressWorksheetLine
Non-filterable, non-selectable: Description, UOM, PreviouslyCompletedQuantity, PriorPeriodQuantity, CurrentPeriodQuantity, TotalCompletedQuantity, CompletedPercentTotalQuantity, TotalBudgetedQuantity, NoteText

PX.Objects.PM.PMProgressWorksheetLine.LineNbr : Edm.Int32 [key] "Line Number"
PX.Objects.PM.PMProgressWorksheetLine.RefNbr : Edm.String [key] "Worksheet Nbr."
PX.Objects.PM.PMProgressWorksheetLine.Type : Edm.String
PX.Objects.PM.PMProgressWorksheetLine.ProjectID : Edm.Int32
PX.Objects.PM.PMProgressWorksheetLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMProgressWorksheetLine.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMProgressWorksheetLine.Description : Edm.String "Description"
PX.Objects.PM.PMProgressWorksheetLine.UOM : Edm.String "UOM"
PX.Objects.PM.PMProgressWorksheetLine.Qty : Edm.Decimal [required] "Completed Quantity"
PX.Objects.PM.PMProgressWorksheetLine.PreviouslyCompletedQuantity : Edm.Decimal "Previously Completed Quantity"
PX.Objects.PM.PMProgressWorksheetLine.PriorPeriodQuantity : Edm.Decimal "Prior Period Quantity"
PX.Objects.PM.PMProgressWorksheetLine.CurrentPeriodQuantity : Edm.Decimal "Current Period Quantity"
PX.Objects.PM.PMProgressWorksheetLine.TotalCompletedQuantity : Edm.Decimal "Total Completed Quantity"
PX.Objects.PM.PMProgressWorksheetLine.CompletedPercentTotalQuantity : Edm.Decimal "Completed (%), Total"
PX.Objects.PM.PMProgressWorksheetLine.TotalBudgetedQuantity : Edm.Decimal "Total Budgeted Quantity"
PX.Objects.PM.PMProgressWorksheetLine.OwnerID : Edm.Int32 "Employee"
PX.Objects.PM.PMProgressWorksheetLine.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMProgressWorksheetLine.NoteID : Edm.Guid
PX.Objects.PM.PMProgressWorksheetLine.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMProgressWorksheetLine.tstamp : Edm.Binary
PX.Objects.PM.PMProgressWorksheetLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProgressWorksheetLine.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProgressWorksheetLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProgressWorksheetLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProgressWorksheetLine.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProgressWorksheetLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMProgressWorksheetLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMProgressWorksheetLine.VendorByOwnerID -> PX.Objects.AP.Vendor (OwnerID=DefContactID)
PX.Objects.PM.PMProgressWorksheetLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMProgressWorksheetLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMProgressWorksheetLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMProgressWorksheetLine.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMProgressWorksheetLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProgressWorksheetLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProgressWorksheetLine.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMProgressWorksheetLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMProgressWorksheetLine.PMProgressWorksheetByRefNbr -> PX.Objects.PM.PMProgressWorksheet (RefNbr=RefNbr)

# PX.Objects.PM.PMProgressWorksheetRevenueLine (EntityType)

Label: "Progress Worksheet Revenue Line"
BaseType: PX.Objects.PM.PMProgressWorksheetLine
Key: LineNbr, RefNbr (inherited from PX.Objects.PM.PMProgressWorksheetLine)
Entity sets: PX_Objects_PM_PMProgressWorksheetRevenueLine, ProgressWorksheetRevenueLine, PMProgressWorksheetRevenueLine

# PX.Objects.PM.PMProject (EntityType)

Label: "Project"
BaseType: PX.Objects.CT.Contract
Key: BaseType, ContractCD (inherited from PX.Objects.CT.Contract)
Entity sets: PX_Objects_PM_PMProject, Project, PMProject
Non-filterable, non-selectable: ProjectType, Included, CapAmount, CuryRate

PX.Objects.PM.PMProject.ProjectType : Edm.String "Type"
PX.Objects.PM.PMProject.BudgetLevel : Edm.String "Revenue Budget Level"
PX.Objects.PM.PMProject.CostBudgetLevel : Edm.String "Cost Budget Level"
PX.Objects.PM.PMProject.BudgetFinalized : Edm.Boolean
PX.Objects.PM.PMProject.CuryInfoID : Edm.Int64
PX.Objects.PM.PMProject.BillAddressID : Edm.Int32
PX.Objects.PM.PMProject.BillContactID : Edm.Int32 "Billing Contact"
PX.Objects.PM.PMProject.BillingCuryID : Edm.String "Billing Currency"
PX.Objects.PM.PMProject.SiteAddressID : Edm.Int32
PX.Objects.PM.PMProject.AssistantID : Edm.Int32 "Project Manager Assistant"
PX.Objects.PM.PMProject.RevenuePercentageCalculationRule : Edm.String "Revenue Percentage Calculation Rule"
PX.Objects.PM.PMProject.ExtRefNbr : Edm.String "External Ref. Nbr"
PX.Objects.PM.PMProject.CalculateProjectedCostByQuantity : Edm.Boolean "Calculate Projected Cost by Quantity"
PX.Objects.PM.PMProject.Included : Edm.Boolean "Included"
PX.Objects.PM.PMProject.IncludeCO : Edm.Boolean "Include CO"
PX.Objects.PM.PMProject.RestrictProjectSelect : Edm.String "Restrict Project Selection"
PX.Objects.PM.PMProject.CapAmount : Edm.Decimal
PX.Objects.PM.PMProject.CuryRate : Edm.Decimal
PX.Objects.PM.PMProject.ProjectGroupID : Edm.String "Project Group"
PX.Objects.PM.PMProject.StatusCode : Edm.Int32
PX.Objects.PM.PMProject.TagTemplateID : Edm.Guid "Tag Template"
PX.Objects.PM.PMProject.EPEmployeeByAssistantID -> PX.Objects.EP.EPEmployee (AssistantID=BAccountID)
PX.Objects.PM.PMProject.PMProjectByTemplateID -> PX.Objects.PM.PMProject (TemplateID=ContractID)
PX.Objects.PM.PMProject.PMProjectByParentProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMProject.PMContactByBillContactID -> PX.Objects.PM.PMContact (BillContactID=ContactID)
PX.Objects.PM.PMProject.BAccountByApproverID -> PX.Objects.CR.BAccount (ApproverID=BAccountID)
PX.Objects.PM.PMProject.BAccountByAssistantID -> PX.Objects.CR.BAccount (AssistantID=BAccountID)
PX.Objects.PM.PMProject.TaxZoneByCostTaxZoneID -> PX.Objects.TX.TaxZone (CostTaxZoneID=TaxZoneID)
PX.Objects.PM.PMProject.TaxZoneByRevenueTaxZoneID -> PX.Objects.TX.TaxZone (RevenueTaxZoneID=TaxZoneID)
PX.Objects.PM.PMProject.PMAllocationByAllocationID -> PX.Objects.PM.PMAllocation (AllocationID=AllocationID)
PX.Objects.PM.PMProject.PMBillingByBillingID -> PX.Objects.PM.PMBilling (BillingID=BillingID)
PX.Objects.PM.PMProject.PMProjectGroupByProjectGroupID -> PX.Objects.PM.PMProjectGroup (ProjectGroupID=ProjectGroupID)
PX.Objects.PM.PMProject.PMRateTableByRateTableID -> PX.Objects.PM.PMRateTable (RateTableID=RateTableID)
PX.Objects.PM.PMProject.PMRevenuePercentageCalculationRuleByRevenuePercentageCalculationRule -> PX.Objects.PM.PMRevenuePercentageCalculationRule (RevenuePercentageCalculationRule=RuleID)
PX.Objects.PM.PMProject.PMTransferRuleByTransferRuleID -> PX.Objects.PM.PMTransferRule
PX.Objects.PM.PMProject.PMTagTemplateByTagTemplateID -> PX.Objects.PM.DAC.PMTagTemplate (TagTemplateID=TemplateID)
PX.Objects.PM.PMProject.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList
PX.Objects.PM.PMProject.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.PM.PMProject.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.PM.PMProject.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.PM.PMProject.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.PM.PMProject.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.PM.PMProject.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMProject.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.PM.PMProject.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.PM.PMProject.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.PM.PMProject.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.PM.PMProject.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.Objects.PM.PMProject.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.PM.PMProject.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.Objects.PM.PMProject.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.PM.PMProject.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.PM.PMProject.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.PM.PMProject.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.PM.PMProject.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.PM.PMProject.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.PM.PMProject.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.PM.PMProject.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PM.PMProject.LienWaiverRecipientCollection -> Collection(PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient)
PX.Objects.PM.PMProject.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.PM.PMProject.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.PM.PMProject.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.Objects.PM.PMProject.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.PM.PMProject.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.PM.PMProject.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.PM.PMProject.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.PM.PMProject.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.PM.PMProject.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.PM.PMProject.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.PM.PMProject.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.PM.PMProject.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.PM.PMProject.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.PM.PMProject.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.PM.PMProject.PhotoLogCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog)
PX.Objects.PM.PMProject.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.PM.PMProject.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.Objects.PM.PMProject.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PM.PMProject.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PM.PMProject.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.PM.PMProject.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.PM.PMProject.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.PM.PMProject.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.PM.PMProject.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.PM.PMProject.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.Objects.PM.PMProject.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.PM.PMProject.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.PM.PMProject.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.PM.PMProject.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PM.PMProject.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PM.PMProject.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PM.PMProject.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.PM.PMProject.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.PM.PMProject.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.PM.PMProject.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.PM.PMProject.PMAccountTaskCollection -> Collection(PX.Objects.PM.PMAccountTask)
PX.Objects.PM.PMProject.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.PM.PMProject.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)
PX.Objects.PM.PMProject.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PM.PMProject.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.PM.PMProject.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.Objects.PM.PMProject.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.PM.PMProject.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.PM.PMProject.PMForecastCollection -> Collection(PX.Objects.PM.PMForecast)
PX.Objects.PM.PMProject.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.PM.PMProject.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.PM.PMProject.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.PM.PMProject.PMProgressWorksheetCollection -> Collection(PX.Objects.PM.PMProgressWorksheet)
PX.Objects.PM.PMProject.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.PM.PMProject.PMProjectCostSpreadLineCollection -> Collection(PX.Objects.PM.PMProjectCostSpreadLine)
PX.Objects.PM.PMProject.PMRetainageStepCollection -> Collection(PX.Objects.PM.PMRetainageStep)
PX.Objects.PM.PMProject.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.PM.PMProject.PMWorkCodeProjectTaskSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeProjectTaskSource)
PX.Objects.PM.PMProject.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.PM.PMProject.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.PM.PMProject.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.PM.PMProject.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.PM.PMProject.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PM.PMProject.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.PM.PMProject.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.PM.PMProject.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.Objects.PM.PMProject.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.PM.PMProject.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.PM.PMProject.EPEarningTypeCollection -> Collection(PX.Objects.EP.EPEarningType)
PX.Objects.PM.PMProject.EPEquipmentRateCollection -> Collection(PX.Objects.EP.EPEquipmentRate)
PX.Objects.PM.PMProject.EPEquipmentSummaryCollection -> Collection(PX.Objects.EP.EPEquipmentSummary)
PX.Objects.PM.PMProject.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.PM.PMProject.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.PM.PMProject.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.PM.PMProject.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.PM.PMProject.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.PM.PMProject.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.PM.PMProject.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.PM.PMProject.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.PM.PMProject.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.PM.PMProject.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.PM.PMProject.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.Objects.PM.PMProject.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.PM.PMProject.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.PM.PMProject.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.PM.PMProject.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.PM.PMProject.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.PM.PMProject.PRProjectFringeBenefitRateReducingDeductCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct)
PX.Objects.PM.PMProject.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.PM.PMProject.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.PM.PMProject.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.PM.PMProject.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.PM.PMProject.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.PM.PMProject.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.PM.PMProject.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.PM.PMProject.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.PM.PMProject.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PM.PMProject.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.PM.PMProject.ProjectARTranCollection -> Collection(PX.Objects.PM.ProjectARTran)
PX.Objects.PM.PMProject.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.PM.PMProject.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.PM.PMProject.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.PM.PMProject.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.PM.PMProject.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.PM.PMProject.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.PM.PMProject.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.PM.PMProject.PMProgressLineTotalCollection -> Collection(PX.Objects.PM.PMProgressLineTotal)
PX.Objects.PM.PMProject.PMProjectRateCollection -> Collection(PX.Objects.PM.PMProjectRate)
PX.Objects.PM.PMProject.PMProjectUnionCollection -> Collection(PX.Objects.PM.PMProjectUnion)
PX.Objects.PM.PMProject.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.PM.PMProject.ProjectPMTranCollection -> Collection(PX.Objects.PM.ProjectPMTran)
PX.Objects.PM.PMProject.ProjectGLTranCollection -> Collection(PX.Objects.PM.ProjectGLTran)
PX.Objects.PM.PMProject.ProjectAPTranCollection -> Collection(PX.Objects.PM.ProjectAPTran)
PX.Objects.PM.PMProject.ProjectINTranCollection -> Collection(PX.Objects.PM.ProjectINTran)
PX.Objects.PM.PMProject.ProjectCASplitCollection -> Collection(PX.Objects.PM.ProjectCASplit)
PX.Objects.PM.PMProject.ContactForCurrentProjectCollection -> Collection(PX.Objects.PJ.Common.DAC.ContactForCurrentProject)
PX.Objects.PM.PMProject.PMMaterialListCollection -> Collection(PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList)
PX.Objects.PM.PMProject.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.PM.PMProject.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.PM.PMProject.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.PM.PMProject.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.PM.PMProjectBudgetHistory (EntityType)

Label: "Project Budget History"
Key: AccountGroupID, ChangeOrderRefNbr, CostCodeID, Date, InventoryID, ProjectID, TaskID
Entity sets: PX_Objects_PM_PMProjectBudgetHistory, ProjectBudgetHistory, PMProjectBudgetHistory

PX.Objects.PM.PMProjectBudgetHistory.Date : Edm.DateTimeOffset [key]
PX.Objects.PM.PMProjectBudgetHistory.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.PMProjectBudgetHistory.TaskID : Edm.Int32 [key] "Project Task"
PX.Objects.PM.PMProjectBudgetHistory.AccountGroupID : Edm.Int32 [key] "Account Group"
PX.Objects.PM.PMProjectBudgetHistory.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.PM.PMProjectBudgetHistory.CostCodeID : Edm.Int32 [key] "Cost Code"
PX.Objects.PM.PMProjectBudgetHistory.ChangeOrderRefNbr : Edm.String [key]
PX.Objects.PM.PMProjectBudgetHistory.Type : Edm.String
PX.Objects.PM.PMProjectBudgetHistory.CuryInfoID : Edm.Int64
PX.Objects.PM.PMProjectBudgetHistory.UOM : Edm.String "UOM"
PX.Objects.PM.PMProjectBudgetHistory.RevisedBudgetQty : Edm.Decimal [required]
PX.Objects.PM.PMProjectBudgetHistory.RevisedBudgetAmt : Edm.Decimal [required] "Amount"
PX.Objects.PM.PMProjectBudgetHistory.CuryRevisedBudgetAmt : Edm.Decimal [required] "Amount"
PX.Objects.PM.PMProjectBudgetHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProjectBudgetHistory.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProjectBudgetHistory.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProjectBudgetHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProjectBudgetHistory.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProjectBudgetHistory.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMProjectBudgetHistory.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMProjectBudgetHistory.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.PM.PMProjectBudgetHistory.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PM.PMProjectBudgetHistory.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMProjectBudgetHistory.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMProjectBudgetHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProjectBudgetHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProjectBudgetHistory.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PM.PMProjectBudgetHistory.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.PM.PMProjectBudgetProfitHistory (EntityType)

Label: "PMProjectBudgetProfitHistory"
Key: AccountGroupID, ProjectID, TaskID
Entity sets: PX_Objects_PM_PMProjectBudgetProfitHistory, PMProjectBudgetProfitHistory

PX.Objects.PM.PMProjectBudgetProfitHistory.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMProjectBudgetProfitHistory.TaskID : Edm.Int32 [key]
PX.Objects.PM.PMProjectBudgetProfitHistory.AccountGroupID : Edm.Int32 [key]
PX.Objects.PM.PMProjectBudgetProfitHistory.AccountGroupType : Edm.String
PX.Objects.PM.PMProjectBudgetProfitHistory.ReportGroup : Edm.String
PX.Objects.PM.PMProjectBudgetProfitHistory.ChangeOrderRefNbr : Edm.String
PX.Objects.PM.PMProjectBudgetProfitHistory.CuryRevisedBudgetAmt : Edm.Decimal
PX.Objects.PM.PMProjectBudgetProfitHistory.Date : Edm.DateTimeOffset
PX.Objects.PM.PMProjectBudgetProfitHistory.CuryOriginalContract : Edm.Decimal "Original Contract Amount"
PX.Objects.PM.PMProjectBudgetProfitHistory.CuryOriginalBudget : Edm.Decimal "Original Cost Amount"
PX.Objects.PM.PMProjectBudgetProfitHistory.CuryOriginalProfit : Edm.Decimal "Original Profit"
PX.Objects.PM.PMProjectBudgetProfitHistory.CuryRevisedContract : Edm.Decimal "Revised Contract Amount"
PX.Objects.PM.PMProjectBudgetProfitHistory.CuryRevisedBudget : Edm.Decimal "Revised Cost Amount"
PX.Objects.PM.PMProjectBudgetProfitHistory.CuryRevisedProfit : Edm.Decimal "Revised Profit"
PX.Objects.PM.PMProjectBudgetProfitHistory.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMProjectBudgetProfitHistory.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.PM.PMProjectBudgetProfitHistory.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PM.PMProjectBudgetProfitHistory.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)

# PX.Objects.PM.PMProjectContact (EntityType)

Label: "Project Contact"
Key: ContactID, ProjectID
Entity sets: PX_Objects_PM_PMProjectContact, ProjectContact1, PMProjectContact
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMProjectContact.IsActive : Edm.Boolean [required] "Currently Involved"
PX.Objects.PM.PMProjectContact.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.PMProjectContact.BusinessAccountID : Edm.Int32 "Business Account"
PX.Objects.PM.PMProjectContact.ContactID : Edm.Int32 [key] "Contact"
PX.Objects.PM.PMProjectContact.RoleID : Edm.String "Role"
PX.Objects.PM.PMProjectContact.RoleDescription : Edm.String "Role Description"
PX.Objects.PM.PMProjectContact.NoteID : Edm.Guid
PX.Objects.PM.PMProjectContact.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMProjectContact.tstamp : Edm.Binary
PX.Objects.PM.PMProjectContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProjectContact.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProjectContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProjectContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProjectContact.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProjectContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMProjectContact.BAccountByBusinessAccountID -> PX.Objects.CR.BAccount (BusinessAccountID=BAccountID)
PX.Objects.PM.PMProjectContact.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.PM.PMProjectContact.ContactByBusinessAccountID -> PX.Objects.CR.Contact (ContactID=ContactID, BusinessAccountID=BAccountID)
PX.Objects.PM.PMProjectContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProjectContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProjectContact.PMRoleByRoleID -> PX.Objects.PMRole (RoleID=RoleID)

# PX.Objects.PM.PMProjectCostForecastTotal (EntityType)

Label: "Contract Total"
Key: ProjectID
Entity sets: PX_Objects_PM_PMProjectCostForecastTotal, ContractTotal, PMProjectCostForecastTotal
Non-filterable, non-selectable: CompletedAmount

PX.Objects.PM.PMProjectCostForecastTotal.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMProjectCostForecastTotal.CuryRevisedAmount : Edm.Decimal "Cost at Completion"
PX.Objects.PM.PMProjectCostForecastTotal.CuryCommittedAmount : Edm.Decimal "Committed Cost"
PX.Objects.PM.PMProjectCostForecastTotal.CuryActualAmount : Edm.Decimal "Actual Cost"
PX.Objects.PM.PMProjectCostForecastTotal.CuryCommittedInvoicedAmount : Edm.Decimal "Committed Invoiced Cost"
PX.Objects.PM.PMProjectCostForecastTotal.CuryCostProjectionCostAtCompletion : Edm.Decimal "Projected Cost at Completion"
PX.Objects.PM.PMProjectCostForecastTotal.CompletedAmount : Edm.Decimal "Actual + Committed Costs"
PX.Objects.PM.PMProjectCostForecastTotal.CuryAmount : Edm.Decimal "Original Budgeted Amount"
PX.Objects.PM.PMProjectCostForecastTotal.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)

# PX.Objects.PM.PMProjectCostSpread (EntityType)

Label: "Project Monthly Cost Spread"
Key: RefNbr
Entity sets: PX_Objects_PM_PMProjectCostSpread, ProjectMonthlyCostSpread, PMProjectCostSpread
Non-filterable, non-selectable: CurrentPeriod, NoteText

PX.Objects.PM.PMProjectCostSpread.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMProjectCostSpread.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.PM.PMProjectCostSpread.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.PM.PMProjectCostSpread.Date : Edm.DateTimeOffset "Cost Spread Date"
PX.Objects.PM.PMProjectCostSpread.Year : Edm.Int32
PX.Objects.PM.PMProjectCostSpread.Month : Edm.Int32
PX.Objects.PM.PMProjectCostSpread.CurrentPeriod : Edm.DateTimeOffset "CurrentPeriod"
PX.Objects.PM.PMProjectCostSpread.SelectedPeriod : Edm.String "Effective Period"
PX.Objects.PM.PMProjectCostSpread.CurveType : Edm.String "S-Curve Type"
PX.Objects.PM.PMProjectCostSpread.Description : Edm.String "Description"
PX.Objects.PM.PMProjectCostSpread.CostProjectionByDateRefNbr : Edm.String "CostProjectionByDateRefNbr"
PX.Objects.PM.PMProjectCostSpread.ProjectedCostAtCompletion : Edm.Decimal [required] "Projected Cost at Completion"
PX.Objects.PM.PMProjectCostSpread.RevisedBudgetedAmount : Edm.Decimal [required] "Revised Budgeted Amount"
PX.Objects.PM.PMProjectCostSpread.RemainingBudgetAmount : Edm.Decimal [required] "Remaining Budget Amount"
PX.Objects.PM.PMProjectCostSpread.Status : Edm.String "Status"
PX.Objects.PM.PMProjectCostSpread.Hold : Edm.Boolean [required]
PX.Objects.PM.PMProjectCostSpread.Approved : Edm.Boolean [required]
PX.Objects.PM.PMProjectCostSpread.Rejected : Edm.Boolean [required]
PX.Objects.PM.PMProjectCostSpread.Released : Edm.Boolean [required]
PX.Objects.PM.PMProjectCostSpread.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMProjectCostSpread.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMProjectCostSpread.BaselineCostPTDTotal : Edm.Decimal [required] "BaselineCostPTDTotal"
PX.Objects.PM.PMProjectCostSpread.ProjectedCostPTDTotal : Edm.Decimal [required] "ProjectedCostPTDTotal"
PX.Objects.PM.PMProjectCostSpread.ActualCostPTDTotal : Edm.Decimal [required] "ActualCostPTDTotal"
PX.Objects.PM.PMProjectCostSpread.CostToCompletePTDTotal : Edm.Decimal [required] "CostToCompletePTDTotal"
PX.Objects.PM.PMProjectCostSpread.NoteID : Edm.Guid
PX.Objects.PM.PMProjectCostSpread.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMProjectCostSpread.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProjectCostSpread.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProjectCostSpread.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProjectCostSpread.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProjectCostSpread.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProjectCostSpread.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.PM.PMProjectCostSpread.Tstamp : Edm.Binary
PX.Objects.PM.PMProjectCostSpread.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMProjectCostSpread.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PM.PMProjectCostSpread.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProjectCostSpread.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProjectCostSpread.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMProjectCostSpread.PMCostProjectionByDateByCostProjectionByDateRefNbr -> PX.Objects.PM.PMCostProjectionByDate (CostProjectionByDateRefNbr=RefNbr)
PX.Objects.PM.PMProjectCostSpread.PMProjectCostSpreadLineCollection -> Collection(PX.Objects.PM.PMProjectCostSpreadLine)

# PX.Objects.PM.PMProjectCostSpreadLine (EntityType)

Label: "Project Monthly Cost Spread Line"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PM_PMProjectCostSpreadLine, ProjectMonthlyCostSpreadLine, PMProjectCostSpreadLine
Non-filterable, non-selectable: Period, VariancePTD, Variance, CostToCompletePTD, CostToComplete, EffectiveWeight, IsPastPeriod, IsCurrentPeriod, IsHeader, NoteText

PX.Objects.PM.PMProjectCostSpreadLine.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.PM.PMProjectCostSpreadLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMProjectCostSpreadLine.ProjectID : Edm.Int32 "Project"
PX.Objects.PM.PMProjectCostSpreadLine.Year : Edm.Int32
PX.Objects.PM.PMProjectCostSpreadLine.Month : Edm.Int32
PX.Objects.PM.PMProjectCostSpreadLine.Period : Edm.DateTimeOffset "Period"
PX.Objects.PM.PMProjectCostSpreadLine.BaselineCostPTD : Edm.Decimal [required] "Baseline PTD Cost"
PX.Objects.PM.PMProjectCostSpreadLine.BaselineCost : Edm.Decimal "Baseline Cost"
PX.Objects.PM.PMProjectCostSpreadLine.ProjectedCostPTD : Edm.Decimal [required] "Projected PTD Cost"
PX.Objects.PM.PMProjectCostSpreadLine.ProjectedCost : Edm.Decimal [required] "Projected Cost"
PX.Objects.PM.PMProjectCostSpreadLine.ActualCostPTD : Edm.Decimal [required] "Actual PTD Cost"
PX.Objects.PM.PMProjectCostSpreadLine.ActualCost : Edm.Decimal [required] "Actual Cost"
PX.Objects.PM.PMProjectCostSpreadLine.VariancePTD : Edm.Decimal "PTD Variance"
PX.Objects.PM.PMProjectCostSpreadLine.Variance : Edm.Decimal "Variance (Baseline vs. Projected)"
PX.Objects.PM.PMProjectCostSpreadLine.CostToCompletePTD : Edm.Decimal "PTD Cost to Complete"
PX.Objects.PM.PMProjectCostSpreadLine.CostToComplete : Edm.Decimal "Cost to Complete"
PX.Objects.PM.PMProjectCostSpreadLine.BaselineWeight : Edm.Decimal [required] "Baseline Weight"
PX.Objects.PM.PMProjectCostSpreadLine.EffectiveWeight : Edm.Decimal "EffectiveWeight"
PX.Objects.PM.PMProjectCostSpreadLine.IsPastPeriod : Edm.Boolean "IsPastPeriod"
PX.Objects.PM.PMProjectCostSpreadLine.IsCurrentPeriod : Edm.Boolean "IsCurrentPeriod"
PX.Objects.PM.PMProjectCostSpreadLine.IsHeader : Edm.Boolean "IsHeader"
PX.Objects.PM.PMProjectCostSpreadLine.NoteID : Edm.Guid
PX.Objects.PM.PMProjectCostSpreadLine.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMProjectCostSpreadLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProjectCostSpreadLine.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProjectCostSpreadLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMProjectCostSpreadLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProjectCostSpreadLine.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProjectCostSpreadLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMProjectCostSpreadLine.Tstamp : Edm.Binary
PX.Objects.PM.PMProjectCostSpreadLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMProjectCostSpreadLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProjectCostSpreadLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProjectCostSpreadLine.PMProjectCostSpreadByRefNbr -> PX.Objects.PM.PMProjectCostSpread (RefNbr=RefNbr)

# PX.Objects.PM.PMProjectGroup (EntityType)

Label: "Project Group"
Key: ProjectGroupID
Entity sets: PX_Objects_PM_PMProjectGroup, ProjectGroup, PMProjectGroup
Non-filterable, non-selectable: Included, NoteText, Secured

PX.Objects.PM.PMProjectGroup.ProjectGroupID : Edm.String [key] "Project Group ID"
PX.Objects.PM.PMProjectGroup.Description : Edm.String "Description"
PX.Objects.PM.PMProjectGroup.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMProjectGroup.Included : Edm.Boolean "Included"
PX.Objects.PM.PMProjectGroup.NoteID : Edm.Guid
PX.Objects.PM.PMProjectGroup.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMProjectGroup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProjectGroup.CreatedByScreenID : Edm.String
PX.Objects.PM.PMProjectGroup.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProjectGroup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProjectGroup.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMProjectGroup.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMProjectGroup.tstamp : Edm.Binary
PX.Objects.PM.PMProjectGroup.Secured : Edm.Boolean "Secured"
PX.Objects.PM.PMProjectGroup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMProjectGroup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMProjectGroup.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)

# PX.Objects.PM.PMProjectRate (EntityType)

Label: "PM Project Rate"
Key: ProjectCD, RateCodeID, RateDefinitionID
Entity sets: PX_Objects_PM_PMProjectRate, PMProjectRate

PX.Objects.PM.PMProjectRate.RateDefinitionID : Edm.Int32 [key]
PX.Objects.PM.PMProjectRate.RateCodeID : Edm.String [key]
PX.Objects.PM.PMProjectRate.ProjectCD : Edm.String [key] "Project"
PX.Objects.PM.PMProjectRate.PMProjectByProjectCD -> PX.Objects.PM.PMProject (ProjectCD=ContractCD)
PX.Objects.PM.PMProjectRate.PMRateSequenceByRateCodeID -> PX.Objects.PM.PMRateSequence (RateDefinitionID=RateDefinitionID, RateCodeID=RateCodeID)

# PX.Objects.PM.PMProjectRevenueTotal (EntityType)

Label: "Contract Total"
Key: ProjectID
Entity sets: PX_Objects_PM_PMProjectRevenueTotal, ContractTotal1, PMProjectRevenueTotal
Non-filterable, non-selectable: ContractCompletedPct, ContractCompletedWithCOPct

PX.Objects.PM.PMProjectRevenueTotal.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMProjectRevenueTotal.CuryAmount : Edm.Decimal "Contract Total"
PX.Objects.PM.PMProjectRevenueTotal.CuryRevisedAmount : Edm.Decimal "Contract Total"
PX.Objects.PM.PMProjectRevenueTotal.CuryInvoicedAmount : Edm.Decimal "Draft Invoice Amount"
PX.Objects.PM.PMProjectRevenueTotal.CuryActualAmount : Edm.Decimal "Actual Amount"
PX.Objects.PM.PMProjectRevenueTotal.CuryInclTaxAmount : Edm.Decimal "Inclusive Tax Amount"
PX.Objects.PM.PMProjectRevenueTotal.CuryAmountToInvoice : Edm.Decimal "Amount to Invoice"
PX.Objects.PM.PMProjectRevenueTotal.ContractCompletedPct : Edm.Decimal "Completed (%)"
PX.Objects.PM.PMProjectRevenueTotal.ContractCompletedWithCOPct : Edm.Decimal "Completed (%)"
PX.Objects.PM.PMProjectRevenueTotal.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)

# PX.Objects.PM.PMProjectTemplate (EntityType)

Label: "Project Template"
Key: ContractCD
Entity sets: PX_Objects_PM_PMProjectTemplate, ProjectTemplate, PMProjectTemplate

PX.Objects.PM.PMProjectTemplate.ContractID : Edm.Int32
PX.Objects.PM.PMProjectTemplate.ContractCD : Edm.String [key] "Project ID"
PX.Objects.PM.PMProjectTemplate.Description : Edm.String "Description"
PX.Objects.PM.PMProjectTemplate.Status : Edm.String "Status"
PX.Objects.PM.PMProjectTemplate.DefaultBranchID : Edm.Int32 "Branch"
PX.Objects.PM.PMProjectTemplate.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMProjectTemplate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMProjectTemplate.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMProjectTemplate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMProjectTemplate.ProjectGroupID : Edm.String "Project Group"
PX.Objects.PM.PMProjectTemplate.PMProjectGroupByProjectGroupID -> PX.Objects.PM.PMProjectGroup (ProjectGroupID=ProjectGroupID)
PX.Objects.PM.PMProjectTemplate.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.PM.PMProjectTemplate.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.PM.PMProjectTemplate.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.PM.PMProjectTemplate.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.PM.PMProjectTemplate.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMProjectTemplate.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.PM.PMProjectTemplate.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.PM.PMProjectTemplate.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.PM.PMProjectTemplate.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.PM.PMProjectTemplate.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.PM.PMProjectTemplate.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.Objects.PM.PMProjectTemplate.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.PM.PMProjectTemplate.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.Objects.PM.PMProjectTemplate.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.PM.PMProjectTemplate.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.PM.PMProjectTemplate.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.PM.PMProjectTemplate.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.PM.PMProjectTemplate.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.PM.PMProjectTemplate.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.PM.PMProjectTemplate.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.PM.PMProjectTemplate.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMProjectTemplate.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PM.PMProjectTemplate.LienWaiverRecipientCollection -> Collection(PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient)
PX.Objects.PM.PMProjectTemplate.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.PM.PMProjectTemplate.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.PM.PMProjectTemplate.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.PM.PMProjectTemplate.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.Objects.PM.PMProjectTemplate.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.PM.PMProjectTemplate.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.PM.PMProjectTemplate.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.PM.PMProjectTemplate.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.PM.PMProjectTemplate.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.PM.PMProjectTemplate.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.PM.PMProjectTemplate.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.PM.PMProjectTemplate.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.PM.PMProjectTemplate.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.PM.PMProjectTemplate.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.PM.PMProjectTemplate.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.PM.PMProjectTemplate.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.PM.PMProjectTemplate.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.PM.PMProjectTemplate.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.PM.PMProjectTemplate.PhotoLogCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog)
PX.Objects.PM.PMProjectTemplate.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.PM.PMProjectTemplate.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.Objects.PM.PMProjectTemplate.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PM.PMProjectTemplate.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PM.PMProjectTemplate.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.PM.PMProjectTemplate.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.PM.PMProjectTemplate.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.PM.PMProjectTemplate.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.PM.PMProjectTemplate.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.PM.PMProjectTemplate.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.Objects.PM.PMProjectTemplate.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.PM.PMProjectTemplate.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.PM.PMProjectTemplate.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.PM.PMProjectTemplate.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PM.PMProjectTemplate.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PM.PMProjectTemplate.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PM.PMProjectTemplate.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.PM.PMProjectTemplate.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.PM.PMProjectTemplate.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.PM.PMProjectTemplate.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.PM.PMProjectTemplate.PMAccountTaskCollection -> Collection(PX.Objects.PM.PMAccountTask)
PX.Objects.PM.PMProjectTemplate.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.PM.PMProjectTemplate.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)
PX.Objects.PM.PMProjectTemplate.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PM.PMProjectTemplate.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.PM.PMProjectTemplate.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.Objects.PM.PMProjectTemplate.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.PM.PMProjectTemplate.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.PM.PMProjectTemplate.PMForecastCollection -> Collection(PX.Objects.PM.PMForecast)
PX.Objects.PM.PMProjectTemplate.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.PM.PMProjectTemplate.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.PM.PMProjectTemplate.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.PM.PMProjectTemplate.PMProgressWorksheetCollection -> Collection(PX.Objects.PM.PMProgressWorksheet)
PX.Objects.PM.PMProjectTemplate.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.PM.PMProjectTemplate.PMProjectCostSpreadLineCollection -> Collection(PX.Objects.PM.PMProjectCostSpreadLine)
PX.Objects.PM.PMProjectTemplate.PMRetainageStepCollection -> Collection(PX.Objects.PM.PMRetainageStep)
PX.Objects.PM.PMProjectTemplate.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.PM.PMProjectTemplate.PMWorkCodeProjectTaskSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeProjectTaskSource)
PX.Objects.PM.PMProjectTemplate.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.PM.PMProjectTemplate.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.PM.PMProjectTemplate.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.PM.PMProjectTemplate.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.PM.PMProjectTemplate.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PM.PMProjectTemplate.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.PM.PMProjectTemplate.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.PM.PMProjectTemplate.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.Objects.PM.PMProjectTemplate.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.PM.PMProjectTemplate.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.PM.PMProjectTemplate.EPEarningTypeCollection -> Collection(PX.Objects.EP.EPEarningType)
PX.Objects.PM.PMProjectTemplate.EPEquipmentRateCollection -> Collection(PX.Objects.EP.EPEquipmentRate)
PX.Objects.PM.PMProjectTemplate.EPEquipmentSummaryCollection -> Collection(PX.Objects.EP.EPEquipmentSummary)
PX.Objects.PM.PMProjectTemplate.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.PM.PMProjectTemplate.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.PM.PMProjectTemplate.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.PM.PMProjectTemplate.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.PM.PMProjectTemplate.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.PM.PMProjectTemplate.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.PM.PMProjectTemplate.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.PM.PMProjectTemplate.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.PM.PMProjectTemplate.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.PM.PMProjectTemplate.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.PM.PMProjectTemplate.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.Objects.PM.PMProjectTemplate.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.PM.PMProjectTemplate.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.PM.PMProjectTemplate.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.PM.PMProjectTemplate.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.PM.PMProjectTemplate.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.PM.PMProjectTemplate.PRProjectFringeBenefitRateReducingDeductCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct)
PX.Objects.PM.PMProjectTemplate.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.PM.PMProjectTemplate.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.PM.PMProjectTemplate.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.PM.PMProjectTemplate.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.PM.PMProjectTemplate.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.PM.PMProjectTemplate.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.PM.PMProjectTemplate.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.PM.PMProjectTemplate.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.PM.PMProjectTemplate.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PM.PMProjectTemplate.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.PM.PMProjectTemplate.ProjectARTranCollection -> Collection(PX.Objects.PM.ProjectARTran)
PX.Objects.PM.PMProjectTemplate.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.PM.PMProjectTemplate.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.PM.PMProjectTemplate.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.PM.PMProjectTemplate.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.PM.PMProjectTemplate.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.PM.PMProjectTemplate.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.PM.PMProjectTemplate.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.PM.PMProjectTemplate.PMProgressLineTotalCollection -> Collection(PX.Objects.PM.PMProgressLineTotal)
PX.Objects.PM.PMProjectTemplate.PMProjectRateCollection -> Collection(PX.Objects.PM.PMProjectRate)
PX.Objects.PM.PMProjectTemplate.PMProjectUnionCollection -> Collection(PX.Objects.PM.PMProjectUnion)
PX.Objects.PM.PMProjectTemplate.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.PM.PMProjectTemplate.ProjectPMTranCollection -> Collection(PX.Objects.PM.ProjectPMTran)
PX.Objects.PM.PMProjectTemplate.ProjectGLTranCollection -> Collection(PX.Objects.PM.ProjectGLTran)
PX.Objects.PM.PMProjectTemplate.ProjectAPTranCollection -> Collection(PX.Objects.PM.ProjectAPTran)
PX.Objects.PM.PMProjectTemplate.ProjectINTranCollection -> Collection(PX.Objects.PM.ProjectINTran)
PX.Objects.PM.PMProjectTemplate.ProjectCASplitCollection -> Collection(PX.Objects.PM.ProjectCASplit)
PX.Objects.PM.PMProjectTemplate.ContactForCurrentProjectCollection -> Collection(PX.Objects.PJ.Common.DAC.ContactForCurrentProject)
PX.Objects.PM.PMProjectTemplate.PMMaterialListCollection -> Collection(PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList)
PX.Objects.PM.PMProjectTemplate.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.PM.PMProjectTemplate.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.PM.PMProjectTemplate.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.PM.PMProjectTemplate.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.PM.PMProjectUnion (EntityType)

Label: "Project Union Locals"
Key: ProjectID, UnionID
Entity sets: PX_Objects_PM_PMProjectUnion, ProjectUnionLocals, PMProjectUnion

PX.Objects.PM.PMProjectUnion.ProjectID : Edm.Int32 [key] "Project ID"
PX.Objects.PM.PMProjectUnion.UnionID : Edm.String [key] "Union Local"
PX.Objects.PM.PMProjectUnion.tstamp : Edm.Binary
PX.Objects.PM.PMProjectUnion.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMProjectUnion.PMUnionByUnionID -> PX.Objects.PM.PMUnion (UnionID=UnionID)

# PX.Objects.PM.PMQuote (EntityType)

Label: "Project Quote"
Key: QuoteNbr
Entity sets: PX_Objects_PM_PMQuote, ProjectQuote, PMQuote
Non-filterable, non-selectable: Hold, SubmitCancelled, IsSetupApprovalRequired, IsDisabled, IsFirstQuote, GrossMarginAmount, CuryGrossMarginAmount, GrossMarginPct, QuoteTotal, CuryQuoteTotal, TextForProductsGrid, CuryWgtAmount, ClassID, FormCaptionDescription, SuggestRelatedItems, CuryRate

PX.Objects.PM.PMQuote.QuoteID : Edm.Guid
PX.Objects.PM.PMQuote.QuoteNbr : Edm.String [key] "Quote Nbr."
PX.Objects.PM.PMQuote.QuoteNbrUnq : Edm.String "Original Quote Nbr."
PX.Objects.PM.PMQuote.QuoteType : Edm.String "Type"
PX.Objects.PM.PMQuote.OpportunityIsActive : Edm.Boolean "Opportunity Is Active"
PX.Objects.PM.PMQuote.DefQuoteID : Edm.Guid
PX.Objects.PM.PMQuote.ManualTotalEntry : Edm.Boolean "Manual Amount"
PX.Objects.PM.PMQuote.TermsID : Edm.String "Credit Terms"
PX.Objects.PM.PMQuote.DocumentDate : Edm.DateTimeOffset "Date"
PX.Objects.PM.PMQuote.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.PM.PMQuote.Status : Edm.String "Status"
PX.Objects.PM.PMQuote.OpportunityAddressID : Edm.Int32
PX.Objects.PM.PMQuote.OpportunityContactID : Edm.Int32
PX.Objects.PM.PMQuote.AllowOverrideContactAddress : Edm.Boolean "Override Contact and Address"
PX.Objects.PM.PMQuote.BAccountID : Edm.Int32 "Business Account"
PX.Objects.PM.PMQuote.ContactID : Edm.Int32 "Contact"
PX.Objects.PM.PMQuote.ShipContactID : Edm.Int32
PX.Objects.PM.PMQuote.ShipAddressID : Edm.Int32
PX.Objects.PM.PMQuote.AllowOverrideShippingContactAddress : Edm.Boolean "Override"
PX.Objects.PM.PMQuote.Subject : Edm.String "Description"
PX.Objects.PM.PMQuote.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.PM.PMQuote.ProjectID : Edm.Int32
PX.Objects.PM.PMQuote.QuoteProjectID : Edm.Int32 "Project ID"
PX.Objects.PM.PMQuote.QuoteProjectCD : Edm.String "New Project ID"
PX.Objects.PM.PMQuote.TemplateID : Edm.Int32 "Project Template"
PX.Objects.PM.PMQuote.ProjectManager : Edm.Int32 "Project Manager"
PX.Objects.PM.PMQuote.ExternalRef : Edm.String "External Ref."
PX.Objects.PM.PMQuote.CampaignSourceID : Edm.String "Source Campaign"
PX.Objects.PM.PMQuote.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMQuote.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMQuote.Hold : Edm.Boolean "Hold"
PX.Objects.PM.PMQuote.Approved : Edm.Boolean "Approved"
PX.Objects.PM.PMQuote.Rejected : Edm.Boolean "Rejected"
PX.Objects.PM.PMQuote.SubmitCancelled : Edm.Boolean
PX.Objects.PM.PMQuote.IsSetupApprovalRequired : Edm.Boolean "Approvable Setup"
PX.Objects.PM.PMQuote.IsDisabled : Edm.Boolean "Disabled"
PX.Objects.PM.PMQuote.IsFirstQuote : Edm.Boolean
PX.Objects.PM.PMQuote.CuryID : Edm.String "Currency"
PX.Objects.PM.PMQuote.CuryInfoID : Edm.Int64
PX.Objects.PM.PMQuote.ExtPriceTotal : Edm.Decimal
PX.Objects.PM.PMQuote.CuryExtPriceTotal : Edm.Decimal "Subtotal"
PX.Objects.PM.PMQuote.LineTotal : Edm.Decimal
PX.Objects.PM.PMQuote.CuryLineTotal : Edm.Decimal "Total Sales"
PX.Objects.PM.PMQuote.CostTotal : Edm.Decimal
PX.Objects.PM.PMQuote.CuryCostTotal : Edm.Decimal "Total Cost"
PX.Objects.PM.PMQuote.GrossMarginAmount : Edm.Decimal "Gross Margin Amount"
PX.Objects.PM.PMQuote.CuryGrossMarginAmount : Edm.Decimal "Gross Margin Amount"
PX.Objects.PM.PMQuote.GrossMarginPct : Edm.Decimal "Gross Margin (%)"
PX.Objects.PM.PMQuote.QuoteTotal : Edm.Decimal "Quote Total"
PX.Objects.PM.PMQuote.CuryQuoteTotal : Edm.Decimal "Quote Total"
PX.Objects.PM.PMQuote.LineDiscountTotal : Edm.Decimal
PX.Objects.PM.PMQuote.CuryLineDiscountTotal : Edm.Decimal "Line Discounts"
PX.Objects.PM.PMQuote.LineDocDiscountTotal : Edm.Decimal
PX.Objects.PM.PMQuote.CuryLineDocDiscountTotal : Edm.Decimal "CuryLineDocDiscountTotal"
PX.Objects.PM.PMQuote.TextForProductsGrid : Edm.String "Availability footer"
PX.Objects.PM.PMQuote.IsTaxValid : Edm.Boolean "Tax Is Up to Date"
PX.Objects.PM.PMQuote.TaxTotal : Edm.Decimal
PX.Objects.PM.PMQuote.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.PM.PMQuote.TaxInclTotal : Edm.Decimal "Inclusive Tax Total in Base Currency"
PX.Objects.PM.PMQuote.CuryTaxInclTotal : Edm.Decimal "Inclusive Tax Total"
PX.Objects.PM.PMQuote.Amount : Edm.Decimal
PX.Objects.PM.PMQuote.CuryAmount : Edm.Decimal "Detail Total"
PX.Objects.PM.PMQuote.DiscTot : Edm.Decimal
PX.Objects.PM.PMQuote.CuryDiscTot : Edm.Decimal "Discount"
PX.Objects.PM.PMQuote.CuryProductsAmount : Edm.Decimal "Total"
PX.Objects.PM.PMQuote.ProductsAmount : Edm.Decimal
PX.Objects.PM.PMQuote.CuryWgtAmount : Edm.Decimal "Wgt. Total"
PX.Objects.PM.PMQuote.CuryVatExemptTotal : Edm.Decimal "VAT Exempt Total"
PX.Objects.PM.PMQuote.VatExemptTotal : Edm.Decimal
PX.Objects.PM.PMQuote.CuryVatTaxableTotal : Edm.Decimal "VAT Taxable Total"
PX.Objects.PM.PMQuote.VatTaxableTotal : Edm.Decimal
PX.Objects.PM.PMQuote.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.PM.PMQuote.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.PM.PMQuote.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.PM.PMQuote.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.PM.PMQuote.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.PM.PMQuote.NoteID : Edm.Guid
PX.Objects.PM.PMQuote.RNoteID : Edm.Guid
PX.Objects.PM.PMQuote.ClassID : Edm.String
PX.Objects.PM.PMQuote.ProductCntr : Edm.Int32
PX.Objects.PM.PMQuote.LineCntr : Edm.Int32
PX.Objects.PM.PMQuote.RefOpportunityID : Edm.String
PX.Objects.PM.PMQuote.FormCaptionDescription : Edm.String
PX.Objects.PM.PMQuote.tstamp : Edm.Binary
PX.Objects.PM.PMQuote.CreatedByScreenID : Edm.String
PX.Objects.PM.PMQuote.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMQuote.CreatedDateTime : Edm.DateTimeOffset "Date Created"
PX.Objects.PM.PMQuote.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMQuote.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMQuote.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date"
PX.Objects.PM.PMQuote.RCreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMQuote.RCreatedByScreenID : Edm.String
PX.Objects.PM.PMQuote.RCreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMQuote.RLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMQuote.RLastModifiedByScreenID : Edm.String
PX.Objects.PM.PMQuote.RLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMQuote.CarrierID : Edm.String "Ship Via"
PX.Objects.PM.PMQuote.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.PM.PMQuote.ShipZoneID : Edm.String "Shipping Zone"
PX.Objects.PM.PMQuote.FOBPointID : Edm.String "FOB Point"
PX.Objects.PM.PMQuote.Resedential : Edm.Boolean "Residential Delivery"
PX.Objects.PM.PMQuote.SaturdayDelivery : Edm.Boolean "Saturday Delivery"
PX.Objects.PM.PMQuote.Insurance : Edm.Boolean "Insurance"
PX.Objects.PM.PMQuote.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.PM.PMQuote.SuggestRelatedItems : Edm.Boolean
PX.Objects.PM.PMQuote.CuryRate : Edm.Decimal
PX.Objects.PM.PMQuote.EPEmployeeByProjectManager -> PX.Objects.EP.EPEmployee (ProjectManager=BAccountID)
PX.Objects.PM.PMQuote.PMProjectByQuoteProjectID -> PX.Objects.PM.PMProject (QuoteProjectID=ContractID)
PX.Objects.PM.PMQuote.PMProjectByTemplateID -> PX.Objects.PM.PMProject (TemplateID=ContractID)
PX.Objects.PM.PMQuote.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMQuote.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PM.PMQuote.CarrierByCarrierID -> PX.Objects.CS.Carrier (CarrierID=CarrierID)
PX.Objects.PM.PMQuote.FOBPointByFOBPointID -> PX.Objects.CS.FOBPoint (FOBPointID=FOBPointID)
PX.Objects.PM.PMQuote.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.PM.PMQuote.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.PM.PMQuote.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.PM.PMQuote.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.PM.PMQuote.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PM.PMQuote.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign (CampaignSourceID=CampaignID)
PX.Objects.PM.PMQuote.CROpportunityByOpportunityID -> PX.Objects.CR.CROpportunity
PX.Objects.PM.PMQuote.PMQuoteTaskCollection -> Collection(PX.Objects.PM.PMQuoteTask)

# PX.Objects.PM.PMQuoteTask (EntityType)

Label: "Project Task"
Key: QuoteID, TaskCD
Entity sets: PX_Objects_PM_PMQuoteTask, ProjectTask1, PMQuoteTask
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMQuoteTask.QuoteID : Edm.Guid [key]
PX.Objects.PM.PMQuoteTask.TaskCD : Edm.String [key] "Task ID"
PX.Objects.PM.PMQuoteTask.Description : Edm.String "Description"
PX.Objects.PM.PMQuoteTask.PlannedStartDate : Edm.DateTimeOffset "Planned Start Date"
PX.Objects.PM.PMQuoteTask.PlannedEndDate : Edm.DateTimeOffset "Planned End Date"
PX.Objects.PM.PMQuoteTask.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.PMQuoteTask.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.PM.PMQuoteTask.NoteID : Edm.Guid
PX.Objects.PM.PMQuoteTask.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMQuoteTask.tstamp : Edm.Binary
PX.Objects.PM.PMQuoteTask.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMQuoteTask.CreatedByScreenID : Edm.String
PX.Objects.PM.PMQuoteTask.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMQuoteTask.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMQuoteTask.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMQuoteTask.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMQuoteTask.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMQuoteTask.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMQuoteTask.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PM.PMQuoteTask.PMQuoteByQuoteID -> PX.Objects.PM.PMQuote (QuoteID=QuoteID)

# PX.Objects.PM.PMRate (EntityType)

Label: "Rate"
Key: LineNbr, RateCodeID, RateDefinitionID
Entity sets: PX_Objects_PM_PMRate, Rate, PMRate
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMRate.RateDefinitionID : Edm.Int32 [key]
PX.Objects.PM.PMRate.RateCodeID : Edm.String [key]
PX.Objects.PM.PMRate.LineNbr : Edm.Int32 [key]
PX.Objects.PM.PMRate.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.PM.PMRate.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.PM.PMRate.Rate : Edm.Decimal [required] "Rate"
PX.Objects.PM.PMRate.NoteID : Edm.Guid
PX.Objects.PM.PMRate.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRate.tstamp : Edm.Binary
PX.Objects.PM.PMRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRate.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRate.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRate.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRate.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMRate.PMRateSequenceByRateCodeID -> PX.Objects.PM.PMRateSequence (RateDefinitionID=RateDefinitionID, RateCodeID=RateCodeID)

# PX.Objects.PM.PMRateDefinition (EntityType)

Label: "Rate Lookup Rule"
Key: RateDefinitionID
Entity sets: PX_Objects_PM_PMRateDefinition, RateLookupRule, PMRateDefinition
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMRateDefinition.RateDefinitionID : Edm.Int32 [key]
PX.Objects.PM.PMRateDefinition.RateTableID : Edm.String
PX.Objects.PM.PMRateDefinition.RateTypeID : Edm.String
PX.Objects.PM.PMRateDefinition.Sequence : Edm.Int16 [required] "Rate Table Sequence"
PX.Objects.PM.PMRateDefinition.Description : Edm.String "Description"
PX.Objects.PM.PMRateDefinition.Project : Edm.Boolean [required] "Project"
PX.Objects.PM.PMRateDefinition.Task : Edm.Boolean [required] "Project Task"
PX.Objects.PM.PMRateDefinition.AccountGroup : Edm.Boolean [required] "Account Group"
PX.Objects.PM.PMRateDefinition.RateItem : Edm.Boolean [required] "Inventory"
PX.Objects.PM.PMRateDefinition.Employee : Edm.Boolean [required] "Employee"
PX.Objects.PM.PMRateDefinition.NoteID : Edm.Guid
PX.Objects.PM.PMRateDefinition.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRateDefinition.tstamp : Edm.Binary
PX.Objects.PM.PMRateDefinition.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRateDefinition.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRateDefinition.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRateDefinition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRateDefinition.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRateDefinition.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMRateDefinition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMRateDefinition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMRateDefinition.PMRateSequenceCollection -> Collection(PX.Objects.PM.PMRateSequence)

# PX.Objects.PM.PMRateSequence (EntityType)

Label: "Rate Lookup Rule Sequence"
Key: RateCodeID, RateTableID, RateTypeID, Sequence
Entity sets: PX_Objects_PM_PMRateSequence, RateLookupRuleSequence, PMRateSequence
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMRateSequence.RateTableID : Edm.String [key] "Rate Table Code"
PX.Objects.PM.PMRateSequence.RateTypeID : Edm.String [key] "Rate Type"
PX.Objects.PM.PMRateSequence.Sequence : Edm.Int32 [key] "Rate Table Sequence"
PX.Objects.PM.PMRateSequence.RateCodeID : Edm.String [key] "Rate Code"
PX.Objects.PM.PMRateSequence.Description : Edm.String "Description"
PX.Objects.PM.PMRateSequence.RateDefinitionID : Edm.Int32
PX.Objects.PM.PMRateSequence.LineCntr : Edm.Int32 [required]
PX.Objects.PM.PMRateSequence.NoteID : Edm.Guid
PX.Objects.PM.PMRateSequence.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRateSequence.tstamp : Edm.Binary
PX.Objects.PM.PMRateSequence.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRateSequence.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRateSequence.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRateSequence.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRateSequence.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRateSequence.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMRateSequence.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMRateSequence.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMRateSequence.PMRateDefinitionBySequence -> PX.Objects.PM.PMRateDefinition (RateTableID=RateTableID, RateTypeID=RateTypeID, Sequence=Sequence)
PX.Objects.PM.PMRateSequence.PMRateTableByRateTableID -> PX.Objects.PM.PMRateTable (RateTableID=RateTableID)
PX.Objects.PM.PMRateSequence.PMRateTypeByRateTypeID -> PX.Objects.PM.PMRateType (RateTypeID=RateTypeID)
PX.Objects.PM.PMRateSequence.PMRateCollection -> Collection(PX.Objects.PM.PMRate)
PX.Objects.PM.PMRateSequence.PMProjectRateCollection -> Collection(PX.Objects.PM.PMProjectRate)
PX.Objects.PM.PMRateSequence.PMTaskRateCollection -> Collection(PX.Objects.PM.PMTaskRate)
PX.Objects.PM.PMRateSequence.PMEmployeeRateCollection -> Collection(PX.Objects.PM.PMEmployeeRate)
PX.Objects.PM.PMRateSequence.PMAccountGroupRateCollection -> Collection(PX.Objects.PM.PMAccountGroupRate)
PX.Objects.PM.PMRateSequence.PMItemRateCollection -> Collection(PX.Objects.PM.PMItemRate)

# PX.Objects.PM.PMRateTable (EntityType)

Label: "Rate Table Code"
Key: RateTableID
Entity sets: PX_Objects_PM_PMRateTable, RateTableCode, PMRateTable
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMRateTable.RateTableID : Edm.String [key] "Rate Table Code"
PX.Objects.PM.PMRateTable.Description : Edm.String "Description"
PX.Objects.PM.PMRateTable.NoteID : Edm.Guid
PX.Objects.PM.PMRateTable.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRateTable.tstamp : Edm.Binary
PX.Objects.PM.PMRateTable.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRateTable.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRateTable.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRateTable.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRateTable.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRateTable.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMRateTable.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMRateTable.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMRateTable.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMRateTable.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMRateTable.PMRateSequenceCollection -> Collection(PX.Objects.PM.PMRateSequence)

# PX.Objects.PM.PMRateType (EntityType)

Label: "Rate Type"
Key: RateTypeID
Entity sets: PX_Objects_PM_PMRateType, RateType, PMRateType
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMRateType.RateTypeID : Edm.String [key] "Rate Type"
PX.Objects.PM.PMRateType.Description : Edm.String "Description"
PX.Objects.PM.PMRateType.NoteID : Edm.Guid
PX.Objects.PM.PMRateType.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRateType.tstamp : Edm.Binary
PX.Objects.PM.PMRateType.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRateType.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRateType.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRateType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRateType.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRateType.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMRateType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMRateType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMRateType.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.PM.PMRateType.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.Objects.PM.PMRateType.PMRateSequenceCollection -> Collection(PX.Objects.PM.PMRateSequence)

# PX.Objects.PM.PMRecurringItem (EntityType)

Label: "Recurring Items"
Key: InventoryID, ProjectID, TaskID
Entity sets: PX_Objects_PM_PMRecurringItem, RecurringItems, PMRecurringItem
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMRecurringItem.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMRecurringItem.TaskID : Edm.Int32 [key]
PX.Objects.PM.PMRecurringItem.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.PM.PMRecurringItem.UOM : Edm.String "UOM"
PX.Objects.PM.PMRecurringItem.Description : Edm.String "Description"
PX.Objects.PM.PMRecurringItem.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PM.PMRecurringItem.AccountSource : Edm.String "Account Source"
PX.Objects.PM.PMRecurringItem.ResetUsage : Edm.String "Reset Usage"
PX.Objects.PM.PMRecurringItem.Included : Edm.Decimal [required] "Included"
PX.Objects.PM.PMRecurringItem.Used : Edm.Decimal "Used"
PX.Objects.PM.PMRecurringItem.UsedTotal : Edm.Decimal "Used Total"
PX.Objects.PM.PMRecurringItem.LastBilledDate : Edm.DateTimeOffset "Last Billed Date"
PX.Objects.PM.PMRecurringItem.LastBilledQty : Edm.Decimal [required] "Last Billed Qty."
PX.Objects.PM.PMRecurringItem.NoteID : Edm.Guid
PX.Objects.PM.PMRecurringItem.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRecurringItem.tstamp : Edm.Binary
PX.Objects.PM.PMRecurringItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRecurringItem.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRecurringItem.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRecurringItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRecurringItem.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRecurringItem.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMRecurringItem.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMRecurringItem.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.PM.PMRecurringItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMRecurringItem.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PM.PMRecurringItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMRecurringItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMRecurringItem.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PM.PMRecurringItem.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMRecurringItem.SubBySubID -> PX.Objects.GL.Sub

# PX.Objects.PM.PMRegister (EntityType)

Label: "Project Register"
Key: Module, RefNbr
Entity sets: PX_Objects_PM_PMRegister, ProjectRegister1, PMRegister1
Non-filterable, non-selectable: NoteText, IsBaseCury

PX.Objects.PM.PMRegister.Module : Edm.String [key required] "Source"
PX.Objects.PM.PMRegister.RefNbr : Edm.String [key] "Ref. Number"
PX.Objects.PM.PMRegister.Date : Edm.DateTimeOffset "Transaction Date"
PX.Objects.PM.PMRegister.Description : Edm.String "Description"
PX.Objects.PM.PMRegister.Status : Edm.String "Status"
PX.Objects.PM.PMRegister.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMRegister.Hold : Edm.Boolean [required] "On Hold"
PX.Objects.PM.PMRegister.IsAllocation : Edm.Boolean [required] "Allocation Transaction"
PX.Objects.PM.PMRegister.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.PM.PMRegister.OrigDocNbr : Edm.String "Orig. Doc. Nbr."
PX.Objects.PM.PMRegister.OrigNoteID : Edm.Guid "Orig. Doc. Nbr."
PX.Objects.PM.PMRegister.QtyTotal : Edm.Decimal "Total Quantity"
PX.Objects.PM.PMRegister.BillableQtyTotal : Edm.Decimal "Total Billable Quantity"
PX.Objects.PM.PMRegister.AmtTotal : Edm.Decimal "Total Amount"
PX.Objects.PM.PMRegister.IsMigratedRecord : Edm.Boolean [required] "Migrated"
PX.Objects.PM.PMRegister.NoteID : Edm.Guid
PX.Objects.PM.PMRegister.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRegister.tstamp : Edm.Binary
PX.Objects.PM.PMRegister.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRegister.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRegister.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRegister.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRegister.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRegister.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMRegister.IsBaseCury : Edm.Boolean
PX.Objects.PM.PMRegister.PMTranCollection -> Collection(PX.Objects.PM.PMTran)

# PX.Objects.PM.PMRetainageStep (EntityType)

Label: "Retainage Step"
Key: LineNbr, ProjectID
Entity sets: PX_Objects_PM_PMRetainageStep, RetainageStep, PMRetainageStep
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMRetainageStep.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMRetainageStep.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMRetainageStep.ThresholdPct : Edm.Decimal "Threshold (%)"
PX.Objects.PM.PMRetainageStep.RetainagePct : Edm.Decimal "Retainage (%)"
PX.Objects.PM.PMRetainageStep.NoteID : Edm.Guid
PX.Objects.PM.PMRetainageStep.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRetainageStep.tstamp : Edm.Binary
PX.Objects.PM.PMRetainageStep.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRetainageStep.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRetainageStep.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRetainageStep.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRetainageStep.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRetainageStep.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMRetainageStep.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMRetainageStep.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMRetainageStep.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PM.PMRevenueBudget (EntityType)

Label: "Project Revenue Budget"
BaseType: PX.Objects.PM.PMBudget
Key: AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID (inherited from PX.Objects.PM.PMBudget)
Entity sets: PX_Objects_PM_PMRevenueBudget, ProjectRevenueBudget, PMRevenueBudget
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.PM.PMRevenueBudget.RecommendedCompletion : Edm.Decimal "Recommended Completion %"
PX.Objects.PM.PMRevenueBudget.CapAmount : Edm.Decimal
PX.Objects.PM.PMRevenueBudget.RecommendedCompletionRevisedAmt : Edm.Decimal "Recommended Completion % (REVISEDAMT)"
PX.Objects.PM.PMRevenueBudget.RecommendedCompletionRevisedQty : Edm.Decimal "Recommended Completion % (REVISEDQTY)"

# PX.Objects.PM.PMRevenuePercentageCalculationRule (EntityType)

Label: "Revenue Percentage Calculation Rule"
Key: RuleID
Entity sets: PX_Objects_PM_PMRevenuePercentageCalculationRule, RevenuePercentageCalculationRule, PMRevenuePercentageCalculationRule
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMRevenuePercentageCalculationRule.RuleID : Edm.String [key] "Rule ID"
PX.Objects.PM.PMRevenuePercentageCalculationRule.Description : Edm.String "Description"
PX.Objects.PM.PMRevenuePercentageCalculationRule.Source : Edm.String "Budget Line Source"
PX.Objects.PM.PMRevenuePercentageCalculationRule.GroupByTask : Edm.String "Group by Task"
PX.Objects.PM.PMRevenuePercentageCalculationRule.GroupByItem : Edm.Boolean [required] "Group by Item"
PX.Objects.PM.PMRevenuePercentageCalculationRule.Formula : Edm.String "Formula"
PX.Objects.PM.PMRevenuePercentageCalculationRule.tstamp : Edm.Binary
PX.Objects.PM.PMRevenuePercentageCalculationRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMRevenuePercentageCalculationRule.CreatedByScreenID : Edm.String
PX.Objects.PM.PMRevenuePercentageCalculationRule.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMRevenuePercentageCalculationRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMRevenuePercentageCalculationRule.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMRevenuePercentageCalculationRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMRevenuePercentageCalculationRule.NoteID : Edm.Guid
PX.Objects.PM.PMRevenuePercentageCalculationRule.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMRevenuePercentageCalculationRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMRevenuePercentageCalculationRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMRevenuePercentageCalculationRule.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMRevenuePercentageCalculationRule.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)

# PX.Objects.PM.PMSetup (EntityType)

Label: "Project Preferences"
Singletons: PX_Objects_PM_PMSetup, ProjectPreferences, PMSetup

PX.Objects.PM.PMSetup.IsActive : Edm.Boolean "IsActive"
PX.Objects.PM.PMSetup.NonProjectCode : Edm.String "Non-Project Code"
PX.Objects.PM.PMSetup.EmptyItemCode : Edm.String "Empty Item Code"
PX.Objects.PM.PMSetup.EmptyItemUOM : Edm.String "Empty Item UOM"
PX.Objects.PM.PMSetup.TranNumbering : Edm.String "Transaction Numbering Sequence"
PX.Objects.PM.PMSetup.ProformaNumbering : Edm.String "Pro Forma Numbering Sequence"
PX.Objects.PM.PMSetup.VendorDocumentRequirementNumbering : Edm.String "Requirement Numbering Sequence"
PX.Objects.PM.PMSetup.AutoPost : Edm.Boolean [required] "Automatically Post on Release"
PX.Objects.PM.PMSetup.AutoReleaseAllocation : Edm.Boolean [required] "Automatically Release Allocations"
PX.Objects.PM.PMSetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.PM.PMSetup.ExpenseAccountSource : Edm.String "Expense Account Source"
PX.Objects.PM.PMSetup.ExpenseAccrualAccountSource : Edm.String "Expense Accrual Account Source"
PX.Objects.PM.PMSetup.AssignmentMapID : Edm.Int32 "Project Approval Map"
PX.Objects.PM.PMSetup.AssignmentNotificationID : Edm.Int32 "Project Approval Notification"
PX.Objects.PM.PMSetup.ProformaApprovalMapID : Edm.Int32 "Pro Forma Invoice Approval Map"
PX.Objects.PM.PMSetup.ProformaApprovalNotificationID : Edm.Int32 "Pro Forma Invoice Approval Notification"
PX.Objects.PM.PMSetup.ProformaAssignmentMapID : Edm.Int32 "Pro Forma Assignment Map"
PX.Objects.PM.PMSetup.ProformaAssignmentNotificationID : Edm.Int32 "Pro Forma Assignment Notification"
PX.Objects.PM.PMSetup.QuoteApprovalMapID : Edm.Int32 "Project Quote Approval Map"
PX.Objects.PM.PMSetup.QuoteApprovalNotificationID : Edm.Int32 "Project Quote Approval Notification"
PX.Objects.PM.PMSetup.CostCommitmentTracking : Edm.Boolean [required] "Internal Cost Commitment Tracking"
PX.Objects.PM.PMSetup.CalculateProjectSpecificTaxes : Edm.Boolean [required] "Calculate Project-Specific Taxes"
PX.Objects.PM.PMSetup.CutoffDate : Edm.String "Billing Cutoff"
PX.Objects.PM.PMSetup.OverLimitErrorLevel : Edm.String "Validate T&M Revenue Budget Limits"
PX.Objects.PM.PMSetup.CostBudgetUpdateMode : Edm.String "Cost Budget Update"
PX.Objects.PM.PMSetup.BudgetControl : Edm.String "Budget Control"
PX.Objects.PM.PMSetup.RevenueBudgetUpdateMode : Edm.String "Revenue Budget Update"
PX.Objects.PM.PMSetup.CopySettingsOnBudgetLineCreationFrom : Edm.String "Copy Settings on Budget Line Creation From"
PX.Objects.PM.PMSetup.VisibleInGL : Edm.Boolean [required] "GL"
PX.Objects.PM.PMSetup.VisibleInAP : Edm.Boolean [required] "AP"
PX.Objects.PM.PMSetup.VisibleInAR : Edm.Boolean [required] "AR"
PX.Objects.PM.PMSetup.VisibleInSO : Edm.Boolean [required] "SO"
PX.Objects.PM.PMSetup.VisibleInPO : Edm.Boolean [required] "PO"
PX.Objects.PM.PMSetup.VisibleInTA : Edm.Boolean [required] "Time Entries"
PX.Objects.PM.PMSetup.VisibleInEA : Edm.Boolean [required] "Expenses"
PX.Objects.PM.PMSetup.VisibleInIN : Edm.Boolean [required] "IN"
PX.Objects.PM.PMSetup.VisibleInCA : Edm.Boolean [required] "CA"
PX.Objects.PM.PMSetup.VisibleInCR : Edm.Boolean [required] "CRM"
PX.Objects.PM.PMSetup.RestrictProjectSelect : Edm.String "Restrict Project Selection"
PX.Objects.PM.PMSetup.QuoteNumberingID : Edm.String "Quote Numbering Sequence"
PX.Objects.PM.PMSetup.AutoCompleteRevenueBudget : Edm.Boolean [required] "Automatically Adjust Unbilled Revenue Based on the Completed Cost"
PX.Objects.PM.PMSetup.MigrationMode : Edm.Boolean [required] "Activate Migration Mode"
PX.Objects.PM.PMSetup.BranchInProjectDocuments : Edm.String "Branch in Project Documents"
PX.Objects.PM.PMSetup.BlockProcessingOnBranchMismatch : Edm.Boolean [required] "Block Doc. Processing on Branch Mismatch"
PX.Objects.PM.PMSetup.StockInitRequired : Edm.Boolean [required]
PX.Objects.PM.PMSetup.LargeProjectTemplateSize : Edm.Int32
PX.Objects.PM.PMSetup.DefaultShipDestType : Edm.String "Default Shipping Destination Type"
PX.Objects.PM.PMSetup.DropshipExpenseAccountSource : Edm.String "Use Expense Account From"
PX.Objects.PM.PMSetup.DropshipReceiptProcessing : Edm.String "Drop-Ship Receipt Processing"
PX.Objects.PM.PMSetup.DropshipExpenseRecording : Edm.String "Record Drop-Ship Expenses"
PX.Objects.PM.PMSetup.ReclassPostingOption : Edm.String "Reclassification Posting"
PX.Objects.PM.PMSetup.tstamp : Edm.Binary
PX.Objects.PM.PMSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMSetup.CreatedByScreenID : Edm.String
PX.Objects.PM.PMSetup.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMSetup.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMSetup.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMSetup.PMProjectByQuoteTemplateID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMSetup.PMTaskByDefaultChangeOrderTaskTemplateID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMSetup.PMTaskByDefaultChangeRequestTaskTemplateID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMSetup.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.PM.PMSetup.NotificationByProformaApprovalNotificationID -> PX.SM.Notification (ProformaApprovalNotificationID=NotificationID)
PX.Objects.PM.PMSetup.NotificationByProformaAssignmentNotificationID -> PX.SM.Notification (ProformaAssignmentNotificationID=NotificationID)
PX.Objects.PM.PMSetup.NotificationByChangeOrderApprovalNotificationID -> PX.SM.Notification
PX.Objects.PM.PMSetup.NotificationByChangeRequestApprovalNotificationID -> PX.SM.Notification
PX.Objects.PM.PMSetup.NotificationByProgressWorksheetApprovalNotificationID -> PX.SM.Notification
PX.Objects.PM.PMSetup.NotificationByQuoteApprovalNotificationID -> PX.SM.Notification (QuoteApprovalNotificationID=NotificationID)
PX.Objects.PM.PMSetup.NotificationByCostProjectionApprovalNotificationID -> PX.SM.Notification
PX.Objects.PM.PMSetup.NotificationByCostProjectionByDateApprovalNotificationID -> PX.SM.Notification
PX.Objects.PM.PMSetup.NotificationByWipAdjustmentApprovalNotificationID -> PX.SM.Notification
PX.Objects.PM.PMSetup.NotificationByCostSpreadApprovalNotificationID -> PX.SM.Notification
PX.Objects.PM.PMSetup.PMChangeOrderClassByDefaultChangeOrderClassID -> PX.Objects.PM.PMChangeOrderClass
PX.Objects.PM.PMSetup.NumberingByTranNumbering -> PX.Objects.CS.Numbering (TranNumbering=NumberingID)
PX.Objects.PM.PMSetup.NumberingByProformaNumbering -> PX.Objects.CS.Numbering (ProformaNumbering=NumberingID)
PX.Objects.PM.PMSetup.NumberingByChangeOrderNumbering -> PX.Objects.CS.Numbering
PX.Objects.PM.PMSetup.NumberingByCostProjectionNumbering -> PX.Objects.CS.Numbering
PX.Objects.PM.PMSetup.NumberingByVendorDocumentRequirementNumbering -> PX.Objects.CS.Numbering (VendorDocumentRequirementNumbering=NumberingID)
PX.Objects.PM.PMSetup.NumberingByWipAdjustmentNumbering -> PX.Objects.CS.Numbering
PX.Objects.PM.PMSetup.NumberingByProjectCostSpreadNumbering -> PX.Objects.CS.Numbering
PX.Objects.PM.PMSetup.NumberingByChangeRequestNumbering -> PX.Objects.CS.Numbering
PX.Objects.PM.PMSetup.NumberingByProgressWorksheetNumbering -> PX.Objects.CS.Numbering
PX.Objects.PM.PMSetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.PM.PMSetup.NumberingByQuoteNumberingID -> PX.Objects.CS.Numbering (QuoteNumberingID=NumberingID)
PX.Objects.PM.PMSetup.INUnitByEmptyItemUOM -> PX.Objects.IN.INUnit (EmptyItemUOM=FromUnit)
PX.Objects.PM.PMSetup.AccountByWipAdjustmentOverbillingAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMSetup.AccountByWipAdjustmentUnderbillingAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMSetup.AccountByWipAdjustmentRevenueAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMSetup.AccountByUnbilledRemainderAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMSetup.AccountByUnbilledRemainderOffsetAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMSetup.SubByWipAdjustmentOverbillingSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMSetup.SubByWipAdjustmentUnderbillingSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMSetup.SubByWipAdjustmentRevenueSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMSetup.SubByUnbilledRemainderSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMSetup.SubByUnbilledRemainderOffsetSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMSetup.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)
PX.Objects.PM.PMSetup.EPAssignmentMapByProformaApprovalMapID -> PX.Objects.EP.EPAssignmentMap (ProformaApprovalMapID=AssignmentMapID)
PX.Objects.PM.PMSetup.EPAssignmentMapByProformaAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (ProformaAssignmentMapID=AssignmentMapID)
PX.Objects.PM.PMSetup.EPAssignmentMapByChangeOrderApprovalMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.PM.PMSetup.EPAssignmentMapByChangeRequestApprovalMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.PM.PMSetup.EPAssignmentMapByProgressWorksheetApprovalMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.PM.PMSetup.EPAssignmentMapByQuoteApprovalMapID -> PX.Objects.EP.EPAssignmentMap (QuoteApprovalMapID=AssignmentMapID)
PX.Objects.PM.PMSetup.EPAssignmentMapByCostProjectionApprovalMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.PM.PMSetup.EPAssignmentMapByCostProjectionByDateApprovalMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.PM.PMSetup.EPAssignmentMapByWipAdjustmentApprovalMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.PM.PMSetup.EPAssignmentMapByCostSpreadApprovalMapID -> PX.Objects.EP.EPAssignmentMap

# PX.Objects.PM.PMShippingAddress (EntityType)

Label: "PM Address"
BaseType: PX.Objects.PM.PMAddress
Key: AddressID (inherited from PX.Objects.PM.PMAddress)
Entity sets: PX_Objects_PM_PMShippingAddress, PMAddress1, PMShippingAddress

# PX.Objects.PM.PMShippingContact (EntityType)

Label: "Project Contact"
BaseType: PX.Objects.PM.PMContact
Key: ContactID (inherited from PX.Objects.PM.PMContact)
Entity sets: PX_Objects_PM_PMShippingContact, ProjectContact2, PMShippingContact

# PX.Objects.PM.PMSiteAddress (EntityType)

Label: "PM Address"
BaseType: PX.Objects.PM.PMAddress
Key: AddressID (inherited from PX.Objects.PM.PMAddress)
Entity sets: PX_Objects_PM_PMSiteAddress, PMAddress2, PMSiteAddress

# PX.Objects.PM.PMTask (EntityType)

Label: "Project Task"
Key: ProjectID, TaskCD
Entity sets: PX_Objects_PM_PMTask, ProjectTask, PMTask
Non-filterable, non-selectable: FormCaptionDescription, ClassID, TemplateID, NoteText

PX.Objects.PM.PMTask.ProjectID : Edm.Int32 [key] "Project ID"
PX.Objects.PM.PMTask.TaskID : Edm.Int32
PX.Objects.PM.PMTask.TaskCD : Edm.String [key] "Task ID"
PX.Objects.PM.PMTask.Description : Edm.String "Description"
PX.Objects.PM.PMTask.CustomerID : Edm.Int32 "Customer"
PX.Objects.PM.PMTask.RateTableID : Edm.String "Rate Table Code"
PX.Objects.PM.PMTask.BillingID : Edm.String "Billing Rule"
PX.Objects.PM.PMTask.AllocationID : Edm.String "Allocation Rule"
PX.Objects.PM.PMTask.BillingOption : Edm.String "Billing Option"
PX.Objects.PM.PMTask.CompletedPctMethod : Edm.String "Completion Method"
PX.Objects.PM.PMTask.RevenuePercentageCalculationRule : Edm.String "Revenue Percentage Calculation Rule"
PX.Objects.PM.PMTask.Status : Edm.String "Status"
PX.Objects.PM.PMTask.PlannedStartDate : Edm.DateTimeOffset "Planned Start Date"
PX.Objects.PM.PMTask.PlannedEndDate : Edm.DateTimeOffset "Planned End Date"
PX.Objects.PM.PMTask.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.PM.PMTask.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.PM.PMTask.ExtRefNbr : Edm.String "External Ref. Nbr"
PX.Objects.PM.PMTask.ApproverID : Edm.Int32 "Approver"
PX.Objects.PM.PMTask.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.PMTask.WipAccountGroupID : Edm.Int32 "Non-Billable WIP Account Group"
PX.Objects.PM.PMTask.CompletedPercent : Edm.Decimal [required] "Completed (%)"
PX.Objects.PM.PMTask.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.PM.PMTask.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMTask.IsCompleted : Edm.Boolean [required] "Completed"
PX.Objects.PM.PMTask.IsCancelled : Edm.Boolean [required] "Cancelled"
PX.Objects.PM.PMTask.BillSeparately : Edm.Boolean [required] "Bill Separately"
PX.Objects.PM.PMTask.ProgressBillingBase : Edm.String "Progress Billing Basis"
PX.Objects.PM.PMTask.Type : Edm.String "Type"
PX.Objects.PM.PMTask.VisibleInGL : Edm.Boolean "GL"
PX.Objects.PM.PMTask.VisibleInAP : Edm.Boolean "AP"
PX.Objects.PM.PMTask.VisibleInAR : Edm.Boolean "AR"
PX.Objects.PM.PMTask.VisibleInSO : Edm.Boolean "SO"
PX.Objects.PM.PMTask.VisibleInPO : Edm.Boolean "PO"
PX.Objects.PM.PMTask.VisibleInTA : Edm.Boolean "Time Entries"
PX.Objects.PM.PMTask.VisibleInEA : Edm.Boolean "Expenses"
PX.Objects.PM.PMTask.VisibleInIN : Edm.Boolean "IN"
PX.Objects.PM.PMTask.VisibleInCA : Edm.Boolean "CA"
PX.Objects.PM.PMTask.VisibleInCR : Edm.Boolean "CRM"
PX.Objects.PM.PMTask.AutoIncludeInPrj : Edm.Boolean [required] "Automatically Include in Project"
PX.Objects.PM.PMTask.FormCaptionDescription : Edm.String
PX.Objects.PM.PMTask.ClassID : Edm.String
PX.Objects.PM.PMTask.TemplateID : Edm.Int32
PX.Objects.PM.PMTask.NoteID : Edm.Guid
PX.Objects.PM.PMTask.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMTask.tstamp : Edm.Binary
PX.Objects.PM.PMTask.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMTask.CreatedByScreenID : Edm.String
PX.Objects.PM.PMTask.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMTask.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMTask.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMTask.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMTask.EPEmployeeByApproverID -> PX.Objects.EP.EPEmployee (ApproverID=BAccountID)
PX.Objects.PM.PMTask.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMTask.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMTask.ContractByProjectID -> PX.Objects.CT.Contract (ProjectID=ContractID)
PX.Objects.PM.PMTask.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.PM.PMTask.PMAccountGroupByWipAccountGroupID -> PX.Objects.PM.PMAccountGroup (WipAccountGroupID=GroupID)
PX.Objects.PM.PMTask.BranchByDefaultBranchID -> PX.Objects.GL.Branch
PX.Objects.PM.PMTask.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMTask.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMTask.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PM.PMTask.PMAllocationByAllocationID -> PX.Objects.PM.PMAllocation (AllocationID=AllocationID)
PX.Objects.PM.PMTask.PMBillingByBillingID -> PX.Objects.PM.PMBilling (BillingID=BillingID)
PX.Objects.PM.PMTask.PMChangeOrderByChangeOrderNbr -> PX.Objects.PM.PMChangeOrder
PX.Objects.PM.PMTask.PMChangeRequestByChangeRequestNbr -> PX.Objects.PM.PMChangeRequest
PX.Objects.PM.PMTask.PMCostCodeByDefaultCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMTask.PMRateTableByRateTableID -> PX.Objects.PM.PMRateTable (RateTableID=RateTableID)
PX.Objects.PM.PMTask.PMRevenuePercentageCalculationRuleByRevenuePercentageCalculationRule -> PX.Objects.PM.PMRevenuePercentageCalculationRule (RevenuePercentageCalculationRule=RuleID)
PX.Objects.PM.PMTask.AccountByDefaultSalesAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMTask.AccountByDefaultExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMTask.AccountByDefaultAccrualAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMTask.SubByDefaultSalesSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMTask.SubByDefaultExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMTask.SubByDefaultAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMTask.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.PM.PMTask.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.PM.PMTask.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.PM.PMTask.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.PM.PMTask.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.PM.PMTask.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.PM.PMTask.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.PM.PMTask.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.PM.PMTask.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.PM.PMTask.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.PM.PMTask.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.Objects.PM.PMTask.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.Objects.PM.PMTask.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.PM.PMTask.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.PM.PMTask.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.PM.PMTask.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.PM.PMTask.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.PM.PMTask.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PM.PMTask.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.PM.PMTask.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.PM.PMTask.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.PM.PMTask.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.PM.PMTask.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.PM.PMTask.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.PM.PMTask.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.PM.PMTask.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.PM.PMTask.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.PM.PMTask.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.PM.PMTask.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.PM.PMTask.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.PM.PMTask.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.PM.PMTask.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.PM.PMTask.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.PM.PMTask.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.PM.PMTask.PhotoLogCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog)
PX.Objects.PM.PMTask.DailyFieldReportSubcontractorActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity)
PX.Objects.PM.PMTask.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.Objects.PM.PMTask.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PM.PMTask.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PM.PMTask.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.PM.PMTask.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.PM.PMTask.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.PM.PMTask.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.PM.PMTask.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.PM.PMTask.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.PM.PMTask.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.PM.PMTask.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.PM.PMTask.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.PM.PMTask.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PM.PMTask.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PM.PMTask.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PM.PMTask.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.PM.PMTask.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.PM.PMTask.PMAccountTaskCollection -> Collection(PX.Objects.PM.PMAccountTask)
PX.Objects.PM.PMTask.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.PM.PMTask.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)
PX.Objects.PM.PMTask.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PM.PMTask.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.PM.PMTask.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.PM.PMTask.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.PM.PMTask.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.PM.PMTask.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.PM.PMTask.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.PM.PMTask.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.PM.PMTask.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.PM.PMTask.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.PM.PMTask.PMWorkCodeProjectTaskSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeProjectTaskSource)
PX.Objects.PM.PMTask.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.PM.PMTask.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.PM.PMTask.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.PM.PMTask.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PM.PMTask.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.PM.PMTask.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.PM.PMTask.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.Objects.PM.PMTask.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.PM.PMTask.EPEarningTypeCollection -> Collection(PX.Objects.EP.EPEarningType)
PX.Objects.PM.PMTask.EPEquipmentSummaryCollection -> Collection(PX.Objects.EP.EPEquipmentSummary)
PX.Objects.PM.PMTask.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.PM.PMTask.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.PM.PMTask.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.PM.PMTask.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.PM.PMTask.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.PM.PMTask.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.PM.PMTask.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.PM.PMTask.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.PM.PMTask.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.PM.PMTask.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.PM.PMTask.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.PM.PMTask.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.PM.PMTask.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.PM.PMTask.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.PM.PMTask.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.PM.PMTask.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.PM.PMTask.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.PM.PMTask.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.PM.PMTask.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.PM.PMTask.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PM.PMTask.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.PM.PMTask.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.PM.PMTask.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.PM.PMTask.PMProgressLineTotalCollection -> Collection(PX.Objects.PM.PMProgressLineTotal)
PX.Objects.PM.PMTask.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.PM.PMTask.PMTaskRateCollection -> Collection(PX.Objects.PM.PMTaskRate)

# PX.Objects.PM.PMTaskRate (EntityType)

Label: "PM Task Rate"
Key: RateCodeID, RateDefinitionID, TaskCD
Entity sets: PX_Objects_PM_PMTaskRate, PMTaskRate

PX.Objects.PM.PMTaskRate.RateDefinitionID : Edm.Int32 [key]
PX.Objects.PM.PMTaskRate.RateCodeID : Edm.String [key]
PX.Objects.PM.PMTaskRate.TaskCD : Edm.String [key] "Project Task"
PX.Objects.PM.PMTaskRate.PMTaskByTaskCD -> PX.Objects.PM.PMTask (TaskCD=TaskCD)
PX.Objects.PM.PMTaskRate.PMRateSequenceByRateCodeID -> PX.Objects.PM.PMRateSequence (RateDefinitionID=RateDefinitionID, RateCodeID=RateCodeID)

# PX.Objects.PM.PMTaskTotal (EntityType)

Label: "Task Total"
Key: ProjectID, TaskID
Entity sets: PX_Objects_PM_PMTaskTotal, TaskTotal, PMTaskTotal
Non-filterable, non-selectable: CuryMargin, Margin, MarginPct

PX.Objects.PM.PMTaskTotal.ProjectID : Edm.Int32 [key]
PX.Objects.PM.PMTaskTotal.TaskID : Edm.Int32 [key]
PX.Objects.PM.PMTaskTotal.CuryAsset : Edm.Decimal [required] "Asset"
PX.Objects.PM.PMTaskTotal.Asset : Edm.Decimal [required]
PX.Objects.PM.PMTaskTotal.CuryLiability : Edm.Decimal [required] "Liability"
PX.Objects.PM.PMTaskTotal.Liability : Edm.Decimal [required]
PX.Objects.PM.PMTaskTotal.CuryIncome : Edm.Decimal [required] "Income"
PX.Objects.PM.PMTaskTotal.Income : Edm.Decimal [required]
PX.Objects.PM.PMTaskTotal.CuryExpense : Edm.Decimal [required] "Expense"
PX.Objects.PM.PMTaskTotal.Expense : Edm.Decimal [required]
PX.Objects.PM.PMTaskTotal.CuryMargin : Edm.Decimal "Margin Amount"
PX.Objects.PM.PMTaskTotal.Margin : Edm.Decimal
PX.Objects.PM.PMTaskTotal.MarginPct : Edm.Decimal "Margin (%)"
PX.Objects.PM.PMTaskTotal.tstamp : Edm.Binary

# PX.Objects.PM.PMTax (EntityType)

Label: "PM Tax Detail"
Key: LineNbr, RefNbr, RevisionID, TaxID
Entity sets: PX_Objects_PM_PMTax, PMTaxDetail, PMTax
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt

PX.Objects.PM.PMTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.PM.PMTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.PM.PMTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PM.PMTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PM.PMTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMTax.CreatedByScreenID : Edm.String
PX.Objects.PM.PMTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMTax.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMTax.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMTax.RevisionID : Edm.Int32 [key] "Revision"
PX.Objects.PM.PMTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PM.PMTax.CuryInfoID : Edm.Int64
PX.Objects.PM.PMTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.PM.PMTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.PM.PMTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.PM.PMTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.PM.PMTax.RetainedTaxableAmt : Edm.Decimal "Retained Taxable"
PX.Objects.PM.PMTax.RetainedTaxAmt : Edm.Decimal "Retained Tax"
PX.Objects.PM.PMTax.tstamp : Edm.Binary
PX.Objects.PM.PMTax.PMProformaLineByRevisionID -> PX.Objects.PM.PMProformaLine (RefNbr=RefNbr, LineNbr=LineNbr, RevisionID=RevisionID)
PX.Objects.PM.PMTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PM.PMTax.PMProformaByRevisionID -> PX.Objects.PM.PMProforma (RefNbr=RefNbr, RevisionID=RevisionID)
PX.Objects.PM.PMTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PM.PMTaxTran (EntityType)

Label: "PM Tax"
Key: LineNbr, RecordID, RefNbr, RevisionID, TaxID
Entity sets: PX_Objects_PM_PMTaxTran, PMTax1, PMTaxTran

PX.Objects.PM.PMTaxTran.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.PM.PMTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMTaxTran.CreatedByScreenID : Edm.String
PX.Objects.PM.PMTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMTaxTran.RefNbr : Edm.String [key] "Order Nbr."
PX.Objects.PM.PMTaxTran.RevisionID : Edm.Int32 [key] "Revision"
PX.Objects.PM.PMTaxTran.LineNbr : Edm.Int32 [key required] "Line Nbr."
PX.Objects.PM.PMTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PM.PMTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.PM.PMTaxTran.CuryInfoID : Edm.Int64
PX.Objects.PM.PMTaxTran.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.PM.PMTaxTran.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.PM.PMTaxTran.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.PM.PMTaxTran.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.PM.PMTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.PM.PMTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PM.PMTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PM.PMTaxTran.RetainedTaxableAmt : Edm.Decimal "Retained Taxable"
PX.Objects.PM.PMTaxTran.TaxZoneID : Edm.String
PX.Objects.PM.PMTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.PM.PMTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.PM.PMTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.PM.PMTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PM.PMTaxTran.PMProformaByRevisionID -> PX.Objects.PM.PMProforma (RefNbr=RefNbr, RevisionID=RevisionID)
PX.Objects.PM.PMTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PM.PMTran (EntityType)

Label: "Project Transaction"
Key: TranID
Entity sets: PX_Objects_PM_PMTran, ProjectTransaction, PMTran
Non-filterable, non-selectable: TranIDDisplay, SourceModule, NonProject, BaseType, InvoicedDescription, TranCuryAmountCopy, IsFree, Proportion, Skip, Prefix, NoteText, IsInverted, IsCreditPair, CreatedByCurrentAllocation, CuryRate

PX.Objects.PM.PMTran.TranID : Edm.Int64 [key] "PM Tran."
PX.Objects.PM.PMTran.TranIDDisplay : Edm.String "PM Tran."
PX.Objects.PM.PMTran.TranType : Edm.String
PX.Objects.PM.PMTran.SourceModule : Edm.String
PX.Objects.PM.PMTran.RefNbr : Edm.String "Ref. Number"
PX.Objects.PM.PMTran.Date : Edm.DateTimeOffset "Date"
PX.Objects.PM.PMTran.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.PM.PMTran.TranDate : Edm.DateTimeOffset
PX.Objects.PM.PMTran.TranPeriodID : Edm.String
PX.Objects.PM.PMTran.ProjectID : Edm.Int32 "Project"
PX.Objects.PM.PMTran.NonProject : Edm.Boolean
PX.Objects.PM.PMTran.BaseType : Edm.String
PX.Objects.PM.PMTran.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.PMTran.OffsetAccountGroupID : Edm.Int32 "Credit Account Group"
PX.Objects.PM.PMTran.MigrationOffsetAccountGroupID : Edm.Int32
PX.Objects.PM.PMTran.ResourceID : Edm.Int32 "Employee"
PX.Objects.PM.PMTran.BAccountID : Edm.Int32 "Customer/Vendor"
PX.Objects.PM.PMTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.PMTran.Description : Edm.String "Description"
PX.Objects.PM.PMTran.InvoicedDescription : Edm.String
PX.Objects.PM.PMTran.UOM : Edm.String "UOM"
PX.Objects.PM.PMTran.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.PM.PMTran.Billable : Edm.Boolean [required] "Billable"
PX.Objects.PM.PMTran.UseBillableQty : Edm.Boolean [required] "Use Billable Quantity in Amount Formula"
PX.Objects.PM.PMTran.BillableQty : Edm.Decimal "Billable Quantity"
PX.Objects.PM.PMTran.InvoicedQty : Edm.Decimal [required] "Billed Quantity"
PX.Objects.PM.PMTran.BaseCuryInfoID : Edm.Int64
PX.Objects.PM.PMTran.ProjectCuryInfoID : Edm.Int64
PX.Objects.PM.PMTran.TranCuryUnitRate : Edm.Decimal [required] "Unit Rate"
PX.Objects.PM.PMTran.UnitRate : Edm.Decimal [required]
PX.Objects.PM.PMTran.TranCuryAmount : Edm.Decimal [required] "Amount"
PX.Objects.PM.PMTran.Amount : Edm.Decimal [required]
PX.Objects.PM.PMTran.TranCuryAmountCopy : Edm.Decimal
PX.Objects.PM.PMTran.ProjectCuryInvoicedAmount : Edm.Decimal [required] "Billed Amount"
PX.Objects.PM.PMTran.InvoicedAmount : Edm.Decimal [required]
PX.Objects.PM.PMTran.Allocated : Edm.Boolean [required] "Allocated"
PX.Objects.PM.PMTran.ExcludedFromAllocation : Edm.Boolean [required] "Excluded from Allocation"
PX.Objects.PM.PMTran.Released : Edm.Boolean [required] "Released"
PX.Objects.PM.PMTran.BatchNbr : Edm.String "GL Batch Nbr."
PX.Objects.PM.PMTran.OrigModule : Edm.String "OrigModule"
PX.Objects.PM.PMTran.OrigTranType : Edm.String "OrigTranType"
PX.Objects.PM.PMTran.OrigRefNbr : Edm.String "OrigRefNbr"
PX.Objects.PM.PMTran.OrigLineNbr : Edm.Int32 "OrigLineNbr"
PX.Objects.PM.PMTran.BillingID : Edm.String
PX.Objects.PM.PMTran.AllocationID : Edm.String "AllocationID"
PX.Objects.PM.PMTran.Billed : Edm.Boolean [required] "Billed"
PX.Objects.PM.PMTran.ExcludedFromBilling : Edm.Boolean [required] "Excluded from Billing"
PX.Objects.PM.PMTran.ExcludedFromBillingReason : Edm.String "Excluded from Billing Reason"
PX.Objects.PM.PMTran.ExcludedFromBalance : Edm.Boolean [required] "Excluded from Balance"
PX.Objects.PM.PMTran.BilledDate : Edm.DateTimeOffset "Billed Date"
PX.Objects.PM.PMTran.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.PM.PMTran.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.PM.PMTran.OrigRefID : Edm.Guid
PX.Objects.PM.PMTran.IsNonGL : Edm.Boolean [required]
PX.Objects.PM.PMTran.IsQtyOnly : Edm.Boolean [required]
PX.Objects.PM.PMTran.Reverse : Edm.String "Reverse"
PX.Objects.PM.PMTran.EarningType : Edm.String "Earning Type"
PX.Objects.PM.PMTran.OvertimeMultiplier : Edm.Decimal "Multiplier"
PX.Objects.PM.PMTran.CaseCD : Edm.String "Case ID"
PX.Objects.PM.PMTran.ARTranType : Edm.String
PX.Objects.PM.PMTran.ARRefNbr : Edm.String "AR Reference Nbr."
PX.Objects.PM.PMTran.RefLineNbr : Edm.Int32
PX.Objects.PM.PMTran.OrigProjectID : Edm.Int32
PX.Objects.PM.PMTran.OrigTaskID : Edm.Int32
PX.Objects.PM.PMTran.OrigAccountGroupID : Edm.Int32
PX.Objects.PM.PMTran.ProformaRefNbr : Edm.String "Pro Forma Ref. Nbr."
PX.Objects.PM.PMTran.ProformaLineNbr : Edm.Int32
PX.Objects.PM.PMTran.ExtRefNbr : Edm.String "External Ref. Nbr."
PX.Objects.PM.PMTran.OrigTranID : Edm.Int64
PX.Objects.PM.PMTran.RemainderOfTranID : Edm.Int64
PX.Objects.PM.PMTran.DuplicateOfTranID : Edm.Int64
PX.Objects.PM.PMTran.IsFree : Edm.Boolean
PX.Objects.PM.PMTran.Proportion : Edm.Decimal
PX.Objects.PM.PMTran.Skip : Edm.Boolean "Skip"
PX.Objects.PM.PMTran.Prefix : Edm.String
PX.Objects.PM.PMTran.NoteID : Edm.Guid
PX.Objects.PM.PMTran.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMTran.tstamp : Edm.Binary
PX.Objects.PM.PMTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMTran.CreatedByScreenID : Edm.String
PX.Objects.PM.PMTran.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMTran.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMTran.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMTran.IsInverted : Edm.Boolean
PX.Objects.PM.PMTran.IsCreditPair : Edm.Boolean
PX.Objects.PM.PMTran.CreatedByCurrentAllocation : Edm.Boolean
PX.Objects.PM.PMTran.IsReclass : Edm.Boolean [required] "Reclassification Transaction"
PX.Objects.PM.PMTran.IsReclassReversal : Edm.Boolean [required] "Reversing Transaction"
PX.Objects.PM.PMTran.CuryRate : Edm.Decimal
PX.Objects.PM.PMTran.EPEmployeeByResourceID -> PX.Objects.EP.EPEmployee (ResourceID=BAccountID)
PX.Objects.PM.PMTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.PMTran.PMProjectByParentProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMTran.ARInvoiceByARRefNbr -> PX.Objects.AR.ARInvoice (ARRefNbr=RefNbr)
PX.Objects.PM.PMTran.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMTran.PMTaskByParentTaskID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMTran.PMTaskByParentProjectID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMTran.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PM.PMTran.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.PM.PMTran.BAccountByResourceID -> PX.Objects.CR.BAccount (ResourceID=BAccountID)
PX.Objects.PM.PMTran.BatchByTranType -> PX.Objects.GL.Batch (BatchNbr=BatchNbr, TranType=Module)
PX.Objects.PM.PMTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.PMTran.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.PM.PMTran.PMAccountGroupByOffsetAccountGroupID -> PX.Objects.PM.PMAccountGroup (OffsetAccountGroupID=GroupID)
PX.Objects.PM.PMTran.PMAccountGroupByParentAccountGroupID -> PX.Objects.PM.PMAccountGroup
PX.Objects.PM.PMTran.PMAccountGroupByMigrationOffsetAccountGroupID -> PX.Objects.PM.PMAccountGroup (MigrationOffsetAccountGroupID=GroupID)
PX.Objects.PM.PMTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PM.PMTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMTran.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMTran.PMCostCodeByParentCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PM.PMTran.PMRegisterByRefNbr -> PX.Objects.PM.PMRegister (TranType=Module, RefNbr=RefNbr)
PX.Objects.PM.PMTran.PMUnionByUnionID -> PX.Objects.PM.PMUnion
PX.Objects.PM.PMTran.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode
PX.Objects.PM.PMTran.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PM.PMTran.CurrencyListByTranCuryID -> PX.Objects.CM.CurrencyList
PX.Objects.PM.PMTran.AccountByOffsetAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMTran.AccountByAccountGroupID -> PX.Objects.GL.Account (AccountGroupID=AccountGroupID)
PX.Objects.PM.PMTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMTran.SubByOffsetSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMTran.LocationByBAccountID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.PM.PMTran.CRCaseByCaseCD -> PX.Objects.CR.CRCase (CaseCD=CaseCD)
PX.Objects.PM.PMTran.EPEarningTypeByEarningType -> PX.Objects.EP.EPEarningType (EarningType=TypeCD)
PX.Objects.PM.PMTran.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.PM.PMTran.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.PM.PMTran.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.PM.PMTranConsolidated (ComplexType)


PX.Objects.PM.PMTranConsolidated.TranID : Edm.Int64
PX.Objects.PM.PMTranConsolidated.TranType : Edm.String
PX.Objects.PM.PMTranConsolidated.RefNbr : Edm.String
PX.Objects.PM.PMTranConsolidated.Date : Edm.DateTimeOffset
PX.Objects.PM.PMTranConsolidated.FinPeriodID : Edm.String
PX.Objects.PM.PMTranConsolidated.TranDate : Edm.DateTimeOffset
PX.Objects.PM.PMTranConsolidated.TranPeriodID : Edm.String
PX.Objects.PM.PMTranConsolidated.ProjectID : Edm.Int32
PX.Objects.PM.PMTranConsolidated.AccountGroupID : Edm.Int32
PX.Objects.PM.PMTranConsolidated.ResourceID : Edm.Int32
PX.Objects.PM.PMTranConsolidated.BAccountID : Edm.Int32
PX.Objects.PM.PMTranConsolidated.InventoryID : Edm.Int32
PX.Objects.PM.PMTranConsolidated.Description : Edm.String
PX.Objects.PM.PMTranConsolidated.UOM : Edm.String
PX.Objects.PM.PMTranConsolidated.Qty : Edm.Decimal
PX.Objects.PM.PMTranConsolidated.Billable : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.UseBillableQty : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.BillableQty : Edm.Decimal
PX.Objects.PM.PMTranConsolidated.InvoicedQty : Edm.Decimal
PX.Objects.PM.PMTranConsolidated.BaseCuryInfoID : Edm.Int64
PX.Objects.PM.PMTranConsolidated.ProjectCuryInfoID : Edm.Int64
PX.Objects.PM.PMTranConsolidated.UnitRate : Edm.Decimal
PX.Objects.PM.PMTranConsolidated.Amount : Edm.Decimal
PX.Objects.PM.PMTranConsolidated.ProjectCuryInvoicedAmount : Edm.Decimal
PX.Objects.PM.PMTranConsolidated.InvoicedAmount : Edm.Decimal
PX.Objects.PM.PMTranConsolidated.Allocated : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.ExcludedFromAllocation : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.Released : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.BatchNbr : Edm.String
PX.Objects.PM.PMTranConsolidated.OrigModule : Edm.String
PX.Objects.PM.PMTranConsolidated.OrigTranType : Edm.String
PX.Objects.PM.PMTranConsolidated.OrigRefNbr : Edm.String
PX.Objects.PM.PMTranConsolidated.OrigLineNbr : Edm.Int32
PX.Objects.PM.PMTranConsolidated.Billed : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.ExcludedFromBilling : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.ExcludedFromBillingReason : Edm.String
PX.Objects.PM.PMTranConsolidated.ExcludedFromBalance : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.BilledDate : Edm.DateTimeOffset
PX.Objects.PM.PMTranConsolidated.StartDate : Edm.DateTimeOffset
PX.Objects.PM.PMTranConsolidated.EndDate : Edm.DateTimeOffset
PX.Objects.PM.PMTranConsolidated.IsNonGL : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.IsQtyOnly : Edm.Boolean
PX.Objects.PM.PMTranConsolidated.EarningType : Edm.String
PX.Objects.PM.PMTranConsolidated.ARTranType : Edm.String
PX.Objects.PM.PMTranConsolidated.ARRefNbr : Edm.String
PX.Objects.PM.PMTranConsolidated.RefLineNbr : Edm.Int32
PX.Objects.PM.PMTranConsolidated.ProformaRefNbr : Edm.String
PX.Objects.PM.PMTranConsolidated.ProformaLineNbr : Edm.Int32
PX.Objects.PM.PMTranConsolidated.ParentCostCodeID : Edm.Int32

# PX.Objects.PM.PMTransferRule (EntityType)

Label: "Rollup Rule"
Key: TransferRuleID
Entity sets: PX_Objects_PM_PMTransferRule, RollupRule, PMTransferRule
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMTransferRule.TransferRuleID : Edm.String [key] "Rollup Rule ID"
PX.Objects.PM.PMTransferRule.Description : Edm.String "Description"
PX.Objects.PM.PMTransferRule.Type : Edm.String "Transactions for Rollup"
PX.Objects.PM.PMTransferRule.AccountGroupFormula : Edm.String "Account Group Mapping Formula"
PX.Objects.PM.PMTransferRule.CostCodeFormula : Edm.String "Cost Code Mapping Formula"
PX.Objects.PM.PMTransferRule.SkipTranFormula : Edm.String "Transaction Exclusion Formula"
PX.Objects.PM.PMTransferRule.UseAccountGroupFormula : Edm.Boolean [required] "Use Formula"
PX.Objects.PM.PMTransferRule.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMTransferRule.NoteID : Edm.Guid
PX.Objects.PM.PMTransferRule.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMTransferRule.tstamp : Edm.Binary
PX.Objects.PM.PMTransferRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMTransferRule.CreatedByScreenID : Edm.String
PX.Objects.PM.PMTransferRule.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMTransferRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMTransferRule.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMTransferRule.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMTransferRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMTransferRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMTransferRule.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.PM.PMTransferRule.PMTransferRuleAccountGroupMapCollection -> Collection(PX.Objects.PM.PMTransferRuleAccountGroupMap)
PX.Objects.PM.PMTransferRule.PMTransferRuleCostCodeMapCollection -> Collection(PX.Objects.PM.PMTransferRuleCostCodeMap)

# PX.Objects.PM.PMTransferRuleAccountGroupMap (EntityType)

Label: "Rollup Rule Account Group Map"
Key: SourceAccountGroupID, TransferRuleID
Entity sets: PX_Objects_PM_PMTransferRuleAccountGroupMap, RollupRuleAccountGroupMap, PMTransferRuleAccountGroupMap

PX.Objects.PM.PMTransferRuleAccountGroupMap.TransferRuleID : Edm.String [key] "Rollup Rule"
PX.Objects.PM.PMTransferRuleAccountGroupMap.SourceAccountGroupID : Edm.Int32 [key] "Source Account Group"
PX.Objects.PM.PMTransferRuleAccountGroupMap.TargetAccountGroupID : Edm.Int32 "Target Account Group"
PX.Objects.PM.PMTransferRuleAccountGroupMap.PMAccountGroupBySourceAccountGroupID -> PX.Objects.PM.PMAccountGroup (SourceAccountGroupID=GroupID)
PX.Objects.PM.PMTransferRuleAccountGroupMap.PMAccountGroupByTargetAccountGroupID -> PX.Objects.PM.PMAccountGroup (TargetAccountGroupID=GroupID)
PX.Objects.PM.PMTransferRuleAccountGroupMap.PMTransferRuleByTransferRuleID -> PX.Objects.PM.PMTransferRule (TransferRuleID=TransferRuleID)

# PX.Objects.PM.PMTransferRuleCostCodeMap (EntityType)

Label: "Rollup Rule Cost Code Map"
Key: SourceCostCodeID, TransferRuleID
Entity sets: PX_Objects_PM_PMTransferRuleCostCodeMap, RollupRuleCostCodeMap, PMTransferRuleCostCodeMap

PX.Objects.PM.PMTransferRuleCostCodeMap.TransferRuleID : Edm.String [key] "Rollup Rule"
PX.Objects.PM.PMTransferRuleCostCodeMap.SourceCostCodeID : Edm.Int32 [key] "Source Cost Code"
PX.Objects.PM.PMTransferRuleCostCodeMap.PMTransferRuleByTransferRuleID -> PX.Objects.PM.PMTransferRule (TransferRuleID=TransferRuleID)

# PX.Objects.PM.PMUnion (EntityType)

Label: "Union Local"
Key: UnionID
Entity sets: PX_Objects_PM_PMUnion, UnionLocal, PMUnion
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMUnion.UnionID : Edm.String [key] "Union Local ID"
PX.Objects.PM.PMUnion.Description : Edm.String "Description"
PX.Objects.PM.PMUnion.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMUnion.VendorID : Edm.Int32 "Vendor"
PX.Objects.PM.PMUnion.NoteID : Edm.Guid
PX.Objects.PM.PMUnion.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMUnion.tstamp : Edm.Binary
PX.Objects.PM.PMUnion.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMUnion.CreatedByScreenID : Edm.String
PX.Objects.PM.PMUnion.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMUnion.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMUnion.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMUnion.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMUnion.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PM.PMUnion.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PM.PMUnion.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMUnion.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMUnion.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PM.PMUnion.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PM.PMUnion.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.PM.PMUnion.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.PM.PMUnion.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.PM.PMUnion.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.PM.PMUnion.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.PM.PMUnion.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.PM.PMUnion.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PM.PMUnion.PREmployeeClassCollection -> Collection(PX.Objects.PR.PREmployeeClass)
PX.Objects.PM.PMUnion.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.PM.PMUnion.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.PM.PMUnion.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.Objects.PM.PMUnion.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.PM.PMUnion.PMProjectUnionCollection -> Collection(PX.Objects.PM.PMProjectUnion)

# PX.Objects.PM.PMWipAdjustment (EntityType)

Label: "Project WIP Adjustment"
Key: RefNbr
Entity sets: PX_Objects_PM_PMWipAdjustment, ProjectWIPAdjustment, PMWipAdjustment
Non-filterable, non-selectable: CuryTotalAmount, TotalAmount, CuryTotalAdjustmentAmount, TotalAdjustmentAmount, NoteText, CuryRate

PX.Objects.PM.PMWipAdjustment.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMWipAdjustment.BranchID : Edm.Int32 "Branch"
PX.Objects.PM.PMWipAdjustment.CuryID : Edm.String "Currency"
PX.Objects.PM.PMWipAdjustment.RateTypeID : Edm.String "Currency Rate Type"
PX.Objects.PM.PMWipAdjustment.CuryInfoID : Edm.Int64
PX.Objects.PM.PMWipAdjustment.Status : Edm.String "Status"
PX.Objects.PM.PMWipAdjustment.Date : Edm.DateTimeOffset "Date"
PX.Objects.PM.PMWipAdjustment.TranPeriodID : Edm.String
PX.Objects.PM.PMWipAdjustment.FinPeriodID : Edm.String "Financial Period"
PX.Objects.PM.PMWipAdjustment.ProjectionDate : Edm.DateTimeOffset "Adjustment Date"
PX.Objects.PM.PMWipAdjustment.LineCntr : Edm.Int32 [required]
PX.Objects.PM.PMWipAdjustment.Hold : Edm.Boolean [required]
PX.Objects.PM.PMWipAdjustment.Approved : Edm.Boolean [required]
PX.Objects.PM.PMWipAdjustment.Rejected : Edm.Boolean [required]
PX.Objects.PM.PMWipAdjustment.Released : Edm.Boolean [required]
PX.Objects.PM.PMWipAdjustment.Description : Edm.String "Description"
PX.Objects.PM.PMWipAdjustment.ProjectStatus : Edm.String "Project Status"
PX.Objects.PM.PMWipAdjustment.OwnerID : Edm.Int32 "Owner"
PX.Objects.PM.PMWipAdjustment.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PM.PMWipAdjustment.BatchNbr : Edm.String "GL Batch"
PX.Objects.PM.PMWipAdjustment.OverbillingUnderbillingOption : Edm.String "Overbilling/Underbilling Posting Level"
PX.Objects.PM.PMWipAdjustment.RevenueOption : Edm.String "Revenue Posting Level"
PX.Objects.PM.PMWipAdjustment.CuryOverbillingAmount : Edm.Decimal "Overbilling Amount"
PX.Objects.PM.PMWipAdjustment.OverbillingAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustment.CuryUnderbillingAmount : Edm.Decimal "Underbilling Amount"
PX.Objects.PM.PMWipAdjustment.UnderbillingAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustment.CuryTotalAmount : Edm.Decimal "Total Amount"
PX.Objects.PM.PMWipAdjustment.TotalAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustment.CuryOverbillingAdjustmentAmount : Edm.Decimal "Overbilling Adjustment"
PX.Objects.PM.PMWipAdjustment.OverbillingAdjustmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustment.CuryUnderbillingAdjustmentAmount : Edm.Decimal "Underbilling Adjustment"
PX.Objects.PM.PMWipAdjustment.UnderbillingAdjustmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustment.CuryTotalAdjustmentAmount : Edm.Decimal "Total Adjustment"
PX.Objects.PM.PMWipAdjustment.TotalAdjustmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustment.IncludePendingChangeOrders : Edm.Boolean [required] "Include Pending CO in Calculations"
PX.Objects.PM.PMWipAdjustment.NoteID : Edm.Guid
PX.Objects.PM.PMWipAdjustment.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMWipAdjustment.tstamp : Edm.Binary
PX.Objects.PM.PMWipAdjustment.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMWipAdjustment.CreatedByScreenID : Edm.String
PX.Objects.PM.PMWipAdjustment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMWipAdjustment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMWipAdjustment.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMWipAdjustment.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMWipAdjustment.CuryRate : Edm.Decimal
PX.Objects.PM.PMWipAdjustment.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.PM.PMWipAdjustment.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PM.PMWipAdjustment.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.PM.PMWipAdjustment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMWipAdjustment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMWipAdjustment.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PM.PMWipAdjustment.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.PM.PMWipAdjustment.CurrencyRateTypeByRateTypeID -> PX.Objects.CM.CurrencyRateType (RateTypeID=CuryRateTypeID)
PX.Objects.PM.PMWipAdjustment.AccountByOverbillingAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMWipAdjustment.AccountByUnderbillingAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMWipAdjustment.AccountByRevenueAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMWipAdjustment.SubByOverbillingSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMWipAdjustment.SubByUnderbillingSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMWipAdjustment.SubByRevenueSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMWipAdjustment.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)

# PX.Objects.PM.PMWipAdjustmentLine (EntityType)

Label: "Project WIP Adjustment Line"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PM_PMWipAdjustmentLine, ProjectWIPAdjustmentLine, PMWipAdjustmentLine
Non-filterable, non-selectable: CuryBudgetedRevenueChangeOrderAmount, BudgetedRevenueChangeOrderAmount, CuryBudgetedCostChangeOrderAmount, BudgetedCostChangeOrderAmount, CuryRevisedCommitmentAmount, RevisedCommitmentAmount, BudgetUsedPct, CuryGrossProfitAmount, GrossProfitAmount, MarginPct, CuryRevenueBacklogAmount, RevenueBacklogAmount, CuryGrossProfitBacklogAmount, GrossProfitBacklogAmount, CuryRemainingContractgAmount, RemainingContractgAmount, NoteText

PX.Objects.PM.PMWipAdjustmentLine.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.PMWipAdjustmentLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.PMWipAdjustmentLine.ProjectionRefNbr : Edm.String "Last Cost Projection"
PX.Objects.PM.PMWipAdjustmentLine.CuryOriginalRevenueAmount : Edm.Decimal "Original Contract Amount"
PX.Objects.PM.PMWipAdjustmentLine.OriginalRevenueAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryPendingRevenueChangeOrderAmount : Edm.Decimal "Pending CO Revenue"
PX.Objects.PM.PMWipAdjustmentLine.PendingRevenueChangeOrderAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryRevisedRevenueBudgetedAmount : Edm.Decimal "Revised Contract Amount"
PX.Objects.PM.PMWipAdjustmentLine.RevisedRevenueBudgetedAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryBudgetedRevenueChangeOrderAmount : Edm.Decimal "Budgeted CO Revenue"
PX.Objects.PM.PMWipAdjustmentLine.BudgetedRevenueChangeOrderAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryOriginalCostAmount : Edm.Decimal "Original Budgeted Cost"
PX.Objects.PM.PMWipAdjustmentLine.OriginalCostAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryPendingCostChangeOrderAmount : Edm.Decimal "Pending CO Cost"
PX.Objects.PM.PMWipAdjustmentLine.PendingCostChangeOrderAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryRevisedCostBudgetedAmount : Edm.Decimal "Revised Budgeted Cost"
PX.Objects.PM.PMWipAdjustmentLine.RevisedCostBudgetedAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryBudgetedCostChangeOrderAmount : Edm.Decimal "Budgeted CO Cost"
PX.Objects.PM.PMWipAdjustmentLine.BudgetedCostChangeOrderAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryOriginalCommitmentAmount : Edm.Decimal "Original Commitment Total"
PX.Objects.PM.PMWipAdjustmentLine.OriginalCommitmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryApprovedCommitmentAmount : Edm.Decimal "Approved Commitment Change Total"
PX.Objects.PM.PMWipAdjustmentLine.ApprovedCommitmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryPendingCommitmentAmount : Edm.Decimal "Pending Commitment Change Total"
PX.Objects.PM.PMWipAdjustmentLine.PendingCommitmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryRevisedCommitmentAmount : Edm.Decimal "Revised Commitment Total"
PX.Objects.PM.PMWipAdjustmentLine.RevisedCommitmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryProjectedAmount : Edm.Decimal "Projected Cost at Completion"
PX.Objects.PM.PMWipAdjustmentLine.ProjectedAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryProjectedMarginAmount : Edm.Decimal "Est. Gross Profit"
PX.Objects.PM.PMWipAdjustmentLine.ProjectedMarginAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.ProjectedMarginPct : Edm.Decimal "Est. Margin (%)"
PX.Objects.PM.PMWipAdjustmentLine.CuryPeriodCostAmount : Edm.Decimal "Actual Period Costs"
PX.Objects.PM.PMWipAdjustmentLine.PeriodCostAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.BudgetUsedPct : Edm.Decimal "% Budget Used"
PX.Objects.PM.PMWipAdjustmentLine.CuryPeriodBillingAmount : Edm.Decimal "Period Billings"
PX.Objects.PM.PMWipAdjustmentLine.PeriodBillingAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryActualAmount : Edm.Decimal "Costs to Period"
PX.Objects.PM.PMWipAdjustmentLine.ActualAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CompletedPct : Edm.Decimal "Completed (%)"
PX.Objects.PM.PMWipAdjustmentLine.CuryRevenueExpectedAmount : Edm.Decimal "Earned Revenue"
PX.Objects.PM.PMWipAdjustmentLine.RevenueExpectedAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryBilledRevenueAmount : Edm.Decimal "Billings to Period"
PX.Objects.PM.PMWipAdjustmentLine.BilledRevenueAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryOverbillingAmount : Edm.Decimal "Overbilling Amount"
PX.Objects.PM.PMWipAdjustmentLine.OverbillingAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryUnderbillingAmount : Edm.Decimal "Underbilling Amount"
PX.Objects.PM.PMWipAdjustmentLine.UnderbillingAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryGrossProfitAmount : Edm.Decimal "Gross Profit"
PX.Objects.PM.PMWipAdjustmentLine.GrossProfitAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.MarginPct : Edm.Decimal "Margin (%)"
PX.Objects.PM.PMWipAdjustmentLine.CuryRevenueBacklogAmount : Edm.Decimal "Revenue Backlog"
PX.Objects.PM.PMWipAdjustmentLine.RevenueBacklogAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryGrossProfitBacklogAmount : Edm.Decimal "Gross Profit Backlog"
PX.Objects.PM.PMWipAdjustmentLine.GrossProfitBacklogAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryRemainingContractgAmount : Edm.Decimal "Remaining Contract"
PX.Objects.PM.PMWipAdjustmentLine.RemainingContractgAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryOverbillingAdjustmentAmount : Edm.Decimal "Overbilling Adjustment"
PX.Objects.PM.PMWipAdjustmentLine.OverbillingAdjustmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.CuryUnderbillingAdjustmentAmount : Edm.Decimal "Underbilling Adjustment"
PX.Objects.PM.PMWipAdjustmentLine.UnderbillingAdjustmentAmount : Edm.Decimal
PX.Objects.PM.PMWipAdjustmentLine.IncludePendingChangeOrders : Edm.Boolean "Pending CO Included"
PX.Objects.PM.PMWipAdjustmentLine.NoteID : Edm.Guid
PX.Objects.PM.PMWipAdjustmentLine.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMWipAdjustmentLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMWipAdjustmentLine.CreatedByScreenID : Edm.String
PX.Objects.PM.PMWipAdjustmentLine.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMWipAdjustmentLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMWipAdjustmentLine.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMWipAdjustmentLine.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMWipAdjustmentLine.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMWipAdjustmentLine.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMWipAdjustmentLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMWipAdjustmentLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMWipAdjustmentLine.PMCostProjectionByDateByProjectionRefNbr -> PX.Objects.PM.PMCostProjectionByDate (ProjectionRefNbr=RefNbr)
PX.Objects.PM.PMWipAdjustmentLine.PMCostProjectionByDateByProjectID -> PX.Objects.PM.PMCostProjectionByDate (ProjectionRefNbr=RefNbr)
PX.Objects.PM.PMWipAdjustmentLine.PMWipAdjustmentByRefNbr -> PX.Objects.PM.PMWipAdjustment (RefNbr=RefNbr)
PX.Objects.PM.PMWipAdjustmentLine.AccountByOverbillingAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMWipAdjustmentLine.AccountByUnderbillingAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMWipAdjustmentLine.AccountByRevenueAccountID -> PX.Objects.GL.Account
PX.Objects.PM.PMWipAdjustmentLine.SubByOverbillingSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMWipAdjustmentLine.SubByUnderbillingSubID -> PX.Objects.GL.Sub
PX.Objects.PM.PMWipAdjustmentLine.SubByRevenueSubID -> PX.Objects.GL.Sub

# PX.Objects.PM.PMWorkCode (EntityType)

Label: "WorkCode"
Key: WorkCodeID
Entity sets: PX_Objects_PM_PMWorkCode, WorkCode, PMWorkCode
Non-filterable, non-selectable: NoteText

PX.Objects.PM.PMWorkCode.WorkCodeID : Edm.String [key] "WCC Code"
PX.Objects.PM.PMWorkCode.Description : Edm.String "Description"
PX.Objects.PM.PMWorkCode.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PM.PMWorkCode.NoteID : Edm.Guid
PX.Objects.PM.PMWorkCode.NoteText : Edm.String "Note Text"
PX.Objects.PM.PMWorkCode.tstamp : Edm.Binary
PX.Objects.PM.PMWorkCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMWorkCode.CreatedByScreenID : Edm.String
PX.Objects.PM.PMWorkCode.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.PMWorkCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMWorkCode.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMWorkCode.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.PMWorkCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMWorkCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMWorkCode.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.PM.PMWorkCode.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.PM.PMWorkCode.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.PM.PMWorkCode.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.PM.PMWorkCode.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.PM.PMWorkCode.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.PM.PMWorkCode.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PM.PMWorkCode.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.PM.PMWorkCode.PREmployeeClassCollection -> Collection(PX.Objects.PR.PREmployeeClass)
PX.Objects.PM.PMWorkCode.PMWorkCodeCostCodeRangeCollection -> Collection(PX.Objects.PM.PMWorkCodeCostCodeRange)
PX.Objects.PM.PMWorkCode.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.Objects.PM.PMWorkCode.PMWorkCodeProjectTaskSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeProjectTaskSource)
PX.Objects.PM.PMWorkCode.PRPaymentWCPremiumCollection -> Collection(PX.Objects.PR.PRPaymentWCPremium)
PX.Objects.PM.PMWorkCode.PRWorkCompensationBenefitRateCollection -> Collection(PX.Objects.PR.PRWorkCompensationBenefitRate)
PX.Objects.PM.PMWorkCode.PRWorkCompensationMaximumInsurableWageCollection -> Collection(PX.Objects.PR.PRWorkCompensationMaximumInsurableWage)

# PX.Objects.PM.PMWorkCodeCostCodeRange (EntityType)

Label: "Workers' Compensation Code Cost Code Range"
Key: LineNbr, WorkCodeID
Entity sets: PX_Objects_PM_PMWorkCodeCostCodeRange, WorkersCompensationCodeCostCodeRange, PMWorkCodeCostCodeRange

PX.Objects.PM.PMWorkCodeCostCodeRange.WorkCodeID : Edm.String [key]
PX.Objects.PM.PMWorkCodeCostCodeRange.LineNbr : Edm.Int32 [key]
PX.Objects.PM.PMWorkCodeCostCodeRange.CostCodeFrom : Edm.String "Cost Code From"
PX.Objects.PM.PMWorkCodeCostCodeRange.CostCodeTo : Edm.String "Cost Code To"
PX.Objects.PM.PMWorkCodeCostCodeRange.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMWorkCodeCostCodeRange.CreatedByScreenID : Edm.String
PX.Objects.PM.PMWorkCodeCostCodeRange.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMWorkCodeCostCodeRange.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMWorkCodeCostCodeRange.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMWorkCodeCostCodeRange.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMWorkCodeCostCodeRange.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMWorkCodeCostCodeRange.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMWorkCodeCostCodeRange.PMCostCodeByCostCodeFrom -> PX.Objects.PM.PMCostCode (CostCodeFrom=CostCodeID)
PX.Objects.PM.PMWorkCodeCostCodeRange.PMCostCodeByCostCodeTo -> PX.Objects.PM.PMCostCode (CostCodeTo=CostCodeID)
PX.Objects.PM.PMWorkCodeCostCodeRange.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)

# PX.Objects.PM.PMWorkCodeLaborItemSource (EntityType)

Label: "Workers' Compensation Labor Item Source"
Key: LaborItemID, WorkCodeID
Entity sets: PX_Objects_PM_PMWorkCodeLaborItemSource, WorkersCompensationLaborItemSource, PMWorkCodeLaborItemSource

PX.Objects.PM.PMWorkCodeLaborItemSource.WorkCodeID : Edm.String [key]
PX.Objects.PM.PMWorkCodeLaborItemSource.LaborItemID : Edm.Int32 [key] "Labor Item"
PX.Objects.PM.PMWorkCodeLaborItemSource.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMWorkCodeLaborItemSource.CreatedByScreenID : Edm.String
PX.Objects.PM.PMWorkCodeLaborItemSource.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMWorkCodeLaborItemSource.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMWorkCodeLaborItemSource.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMWorkCodeLaborItemSource.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMWorkCodeLaborItemSource.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PM.PMWorkCodeLaborItemSource.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMWorkCodeLaborItemSource.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMWorkCodeLaborItemSource.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)

# PX.Objects.PM.PMWorkCodeProjectTaskSource (EntityType)

Label: "Workers' Compensation Project Task Source"
Key: LineNbr, WorkCodeID
Entity sets: PX_Objects_PM_PMWorkCodeProjectTaskSource, WorkersCompensationProjectTaskSource, PMWorkCodeProjectTaskSource

PX.Objects.PM.PMWorkCodeProjectTaskSource.WorkCodeID : Edm.String [key]
PX.Objects.PM.PMWorkCodeProjectTaskSource.LineNbr : Edm.Int32 [key]
PX.Objects.PM.PMWorkCodeProjectTaskSource.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.PMWorkCodeProjectTaskSource.CreatedByScreenID : Edm.String
PX.Objects.PM.PMWorkCodeProjectTaskSource.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMWorkCodeProjectTaskSource.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.PMWorkCodeProjectTaskSource.LastModifiedByScreenID : Edm.String
PX.Objects.PM.PMWorkCodeProjectTaskSource.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PM.PMWorkCodeProjectTaskSource.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.PMWorkCodeProjectTaskSource.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMWorkCodeProjectTaskSource.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PM.PMWorkCodeProjectTaskSource.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.PMWorkCodeProjectTaskSource.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PM.PMWorkCodeProjectTaskSource.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)

# PX.Objects.PM.POLinePM (EntityType)

Label: "PO Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PM_POLinePM, POLine, POLinePM
Non-filterable, non-selectable: LineAmount, CalcOpenQty, CalcCuryOpenAmt

PX.Objects.PM.POLinePM.OrderType : Edm.String [key] "PO Type"
PX.Objects.PM.POLinePM.OrderNbr : Edm.String [key] "PO Nbr."
PX.Objects.PM.POLinePM.LineNbr : Edm.Int32 [key] "PO Line Nbr."
PX.Objects.PM.POLinePM.LineType : Edm.String "Status"
PX.Objects.PM.POLinePM.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PM.POLinePM.VendorID : Edm.Int32 "Vendor"
PX.Objects.PM.POLinePM.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.PM.POLinePM.PromisedDate : Edm.DateTimeOffset "Promised"
PX.Objects.PM.POLinePM.Cancelled : Edm.Boolean "Canceled"
PX.Objects.PM.POLinePM.Completed : Edm.Boolean "Completed"
PX.Objects.PM.POLinePM.SiteID : Edm.Int32
PX.Objects.PM.POLinePM.UOM : Edm.String "UOM"
PX.Objects.PM.POLinePM.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.PM.POLinePM.BaseOrderQty : Edm.Decimal
PX.Objects.PM.POLinePM.OpenQty : Edm.Decimal
PX.Objects.PM.POLinePM.BaseOpenQty : Edm.Decimal
PX.Objects.PM.POLinePM.ReceivedQty : Edm.Decimal "Qty. On Receipts"
PX.Objects.PM.POLinePM.BaseReceivedQty : Edm.Decimal
PX.Objects.PM.POLinePM.CuryUnbilledAmt : Edm.Decimal
PX.Objects.PM.POLinePM.TranDesc : Edm.String "Line Description"
PX.Objects.PM.POLinePM.OrderProjectID : Edm.Int32
PX.Objects.PM.POLinePM.CuryInfoID : Edm.Int64
PX.Objects.PM.POLinePM.CuryUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.PM.POLinePM.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.PM.POLinePM.CuryLineAmt : Edm.Decimal "Ext. Cost"
PX.Objects.PM.POLinePM.LineAmount : Edm.Decimal "Ext. Cost in Base Currency"
PX.Objects.PM.POLinePM.CuryExtCost : Edm.Decimal "Line Amount"
PX.Objects.PM.POLinePM.ExtCost : Edm.Decimal "Line Amount in Base Currency"
PX.Objects.PM.POLinePM.AlternateID : Edm.String "Alternate ID"
PX.Objects.PM.POLinePM.ExpenseAcctID : Edm.Int32
PX.Objects.PM.POLinePM.UnbilledQty : Edm.Decimal
PX.Objects.PM.POLinePM.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PM.POLinePM.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.PM.POLinePM.CuryID : Edm.String "Currency"
PX.Objects.PM.POLinePM.HasMultipleProjects : Edm.Boolean
PX.Objects.PM.POLinePM.CalcOpenQty : Edm.Decimal "Open Qty."
PX.Objects.PM.POLinePM.CalcCuryOpenAmt : Edm.Decimal "Open Amount"
PX.Objects.PM.POLinePM.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.PM.POLinePM.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PM.POLinePM.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PM.POLinePM.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PM.POLinePM.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PM.POLinePM.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.PM.POLinePM.AccountByExpenseAcctID -> PX.Objects.GL.Account (ExpenseAcctID=AccountID)
PX.Objects.PM.POLinePM.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.PM.POLinePM.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.PM.POLinePM.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PM.POLinePM.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PM.POLinePM.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PM.POLinePM.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PM.POLinePM.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PM.POLinePM.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PM.POLinePM.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.PM.POLinePM.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PM.POLinePM.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.PM.POLinePM.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PM.POLinePM.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PM.POLinePM.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PM.POLinePM.PMWorkCodeCostCodeRangeCollection -> Collection(PX.Objects.PM.PMWorkCodeCostCodeRange)

# PX.Objects.PM.POOrderPM (EntityType)

Label: "Purchase Order"
Key: OrderNbr, OrderType
Entity sets: PX_Objects_PM_POOrderPM, PurchaseOrder1, POOrderPM

PX.Objects.PM.POOrderPM.OrderType : Edm.String [key] "PO Type"
PX.Objects.PM.POOrderPM.OrderNbr : Edm.String [key] "PO Nbr."
PX.Objects.PM.POOrderPM.VendorID : Edm.Int32 "Vendor"
PX.Objects.PM.POOrderPM.CuryID : Edm.String "Currency"
PX.Objects.PM.POOrderPM.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr)
PX.Objects.PM.POOrderPM.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PM.POOrderPM.POOrderByOriginalPOType -> PX.Objects.PO.POOrder
PX.Objects.PM.POOrderPM.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.PM.POOrderPM.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.PM.POOrderPM.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.PM.POOrderPM.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.PM.POOrderPM.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.PM.POOrderPM.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.PM.POOrderPM.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.PM.POOrderPM.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PM.POOrderPM.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PM.POOrderPM.POOrderReceiptCollection -> Collection(PX.Objects.PO.POOrderReceipt)
PX.Objects.PM.POOrderPM.VPComplianceNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent)
PX.Objects.PM.POOrderPM.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PM.POOrderPM.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PM.POOrderPM.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.PM.POOrderPM.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.PM.POOrderPM.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.PM.POOrderPM.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PM.POOrderPM.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.PM.POOrderPM.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PM.POOrderPM.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.PM.POOrderPM.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.PM.POOrderPM.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.PM.POOrderPM.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PM.POOrderPM.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PM.POOrderPM.DropShipSOLineCollection -> Collection(PX.Objects.SO.DropShipSOLine)
PX.Objects.PM.POOrderPM.SupplyPOLineCollection -> Collection(PX.Objects.SO.SupplyPOLine)
PX.Objects.PM.POOrderPM.POLine3Collection -> Collection(PX.Objects.SO.POLine3)
PX.Objects.PM.POOrderPM.RQRequisitionOrderCollection -> Collection(PX.Objects.RQ.RQRequisitionOrder)
PX.Objects.PM.POOrderPM.DropShipPOLineCollection -> Collection(PX.Objects.PO.DropShipPOLine)
PX.Objects.PM.POOrderPM.LinkLineOrderCollection -> Collection(PX.Objects.PO.LinkLineOrder)
PX.Objects.PM.POOrderPM.LinkLineReceiptCollection -> Collection(PX.Objects.PO.LinkLineReceipt)
PX.Objects.PM.POOrderPM.POAccrualInquiryResultCollection -> Collection(PX.Objects.PO.POAccrualInquiryResult)
PX.Objects.PM.POOrderPM.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.PM.POOrderPM.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.PM.POOrderPM.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.PM.POOrderPM.POOrderPOReceiptCollection -> Collection(PX.Objects.PO.POOrderPOReceipt)
PX.Objects.PM.POOrderPM.POReceiptLinePOReceiptCollection -> Collection(PX.Objects.PO.POReceiptLinePOReceipt)
PX.Objects.PM.POOrderPM.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PM.POOrderPM.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.PM.POOrderPM.POBlanketOrderPOOrderCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder)
PX.Objects.PM.POOrderPM.POBlanketOrderPOReceiptCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt)
PX.Objects.PM.POOrderPM.POLinePMCollection -> Collection(PX.Objects.PM.POLinePM)
PX.Objects.PM.POOrderPM.POOrderPMCollection -> Collection(PX.Objects.PM.POOrderPM)
PX.Objects.PM.POOrderPM.SelectedProdMatlCollection -> Collection(PX.Objects.AM.SelectedProdMatl)

# PX.Objects.PM.Project.Cashflow.PMProjectAPDetails (ComplexType)


PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.DocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.RefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.LineNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.Type : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.DocDate : Edm.DateTimeOffset
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.POOrderType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.PONbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.POLineNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CONbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.AccountGroupID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.InventoryID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryID : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.BaseCuryInfoID : Edm.Int64
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ProjectCuryInfoID : Edm.Int64
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ProjectCurrencyRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.UOM : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.VendorID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.SourceDocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.SourceRefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.SourceLineNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.OrigDocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.OrigRefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.DocProjRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.LineAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.TranCuryLineAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.BilledQty : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.UnitCost : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.Amount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.TranCuryAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.OpenAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.TranCuryPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.PaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.OpenRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ReleasedRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.PaidRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.PPDAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.DiscAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.WhTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.RGOLAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.InclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ExclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.UseTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.RetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ExclusiveRetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.RetainedTaxReleasedAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.InclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ExclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryLineAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryUnitCost : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryOpenAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryOpenRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryReleasedRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryPaidRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryPPDAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryDiscAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryWhTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryRGOLAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryInclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryExclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryUseTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryRetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryExclusiveRetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryRetainedTaxReleasedAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryInclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryExclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CommittedQty : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.BudgetCommittedQty : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CommittedCOQty : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.BudgetCommittedCOQty : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ProjectCuryCommittedAmt : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ProjectCuryCommittedCOAmt : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CommittedCOAmt : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ProjectCuryCommittedCORetainage : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CommittedCORetainage : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.ProjectCuryCommittedUnitCost : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CommittedUnitCost : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPDetails.CuryViewState : Edm.Boolean

# PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail (ComplexType)


PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.DocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.RefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.ID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.LineNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.POOrderType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.PONbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.POLineNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.TaskID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.AccountGroupID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.InventoryID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryID : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.UOM : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.VendorID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.Type : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.DocDate : Edm.DateTimeOffset
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.SourceDocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.SourceRefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.SourceLineNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.OrigDocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.OrigRefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.DocumentCuryInfoID : Edm.Int64
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.ProjectCuryInfoID : Edm.Int64
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.DocProjRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.ProjBaseRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.LineAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.TranCuryLineAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.BilledQty : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.UnitCost : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.Amount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.TranCuryAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.OpenAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.PaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.TranCuryPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.OpenRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.ReleasedRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.PPDAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.DiscAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.WhTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.RGOLAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.InclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.ExclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.UseTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.RetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.ExclusiveRetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.RetainedTaxReleasedAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.InclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.ExclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryLineAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryUnitCost : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryOpenAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryOpenRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryReleasedRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryPPDAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryDiscAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryWhTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryRGOLAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryInclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryExclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryUseTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryRetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryExclusiveRetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryRetainedTaxReleasedAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryInclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryExclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectAPTranPostDetail.CuryViewState : Edm.Boolean

# PX.Objects.PM.Project.Cashflow.PMProjectARTranPost (ComplexType)


PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.DocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.RefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.ID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.AdjNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.ProjectID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.Type : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.DocDate : Edm.DateTimeOffset
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.SourceDocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.SourceRefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.OrigDocType : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.OrigRefNbr : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryID : Edm.String
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.DocumentCuryInfoID : Edm.Int64
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.ProjectCuryInfoID : Edm.Int64
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.DocProjRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.ProjBaseRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.Sign : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.Amount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.TranCuryAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.OpenAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.PaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.TranCuryPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.OpenRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.ReleasedRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.PaidRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.PPDAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.DiscAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.WOAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.RGOLAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.TotalTranAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.TotalRetainageTranAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.PaymentsByLinesAllowed : Edm.Boolean
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.AmountRatio : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.RetainageRatio : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.InclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.ExclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.RetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.RetainedTaxReleasedAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.InclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.ExclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.RetainedTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryOpenAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryOpenRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryReleasedRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryPaidRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryPPDAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryDiscAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryWOAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryRGOLAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryInclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryExclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryRetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryRetainedTaxReleasedAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryInclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryExclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryRetainedTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPost.CuryViewState : Edm.Boolean

# PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail (EntityType)

Label: "Project AR History"
Key: DocType, ID, LineNbr, RefNbr, SourceLineNbr
Entity sets: PX_Objects_PM_Project_Cashflow_PMProjectARTranPostDetail, ProjectARHistory, PMProjectARTranPostDetail
Non-filterable, non-selectable: CuryRate, CuryViewState

PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.DocType : Edm.String [key] "Doc. Type"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.ID : Edm.Int32 [key]
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.AdjNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.InventoryID : Edm.Int32
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryID : Edm.String "Currency"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.UOM : Edm.String "UOM"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CustomerID : Edm.Int32 "Customer"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.Type : Edm.String "Transaction type"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.SourceDocType : Edm.String "Source Doc. Type"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.SourceRefNbr : Edm.String "Source Ref. Nbr."
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.OrigRefNbr : Edm.String "Orig Ref. Nbr."
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.SourceLineNbr : Edm.Int32 [key] "Source Line Nbr."
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.DocumentCuryInfoID : Edm.Int64
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.ProjectCuryInfoID : Edm.Int64
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.DocProjRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.ProjBaseRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.ExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.TranCuryExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.InvoicedQty : Edm.Decimal "Invoiced Qty."
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.UnitPrice : Edm.Decimal "Unit Price (Base Curr.)"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.Amount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.TranCuryAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.OpenAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.PaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.TranCuryPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.OpenRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.ReleasedRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.PaidRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.PPDAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.DiscAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.WOAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.RGOLAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.InclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.ExclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.RetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.RetainedTaxReleasedAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.InclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.ExclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.RetainedTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryUnitPrice : Edm.Decimal "Unit Price (Project Curr.)"
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryOpenAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryOpenRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryReleasedRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryPaidRetainageAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryPPDAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryDiscAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryWOAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryRGOLAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryInclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryExclusiveTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryRetainedTaxAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryRetainedTaxReleasedAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryInclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryExclusiveTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryRetainedTaxPaidAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryRate : Edm.Decimal
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.CuryViewState : Edm.Boolean
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)

# PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate (ComplexType)


PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.POOrderType : Edm.String
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.POOrderNbr : Edm.String
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.POLineNbr : Edm.Int32
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.Date : Edm.DateTimeOffset
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectID : Edm.Int32
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.TaskID : Edm.Int32
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.AccountGroupID : Edm.Int32
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.BudgetInventoryID : Edm.Int32
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.BudgetCostCodeID : Edm.Int32
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.BilledQty : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryExtCost : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ExtCost : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryAPRetainageHeld : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.APRetainageHeld : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryAPRetainedTaxHeld : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.APRetainedTaxHeld : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryAPRetainageReleased : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.APRetainageReleased : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryAPRetainedTaxReleased : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.APRetainedTaxReleased : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryAPAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.APAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryPaidAPAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.PaidAPAmount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryAPCashDiscount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.APCashDiscount : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryBilledExclusiveTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.BilledExclusiveTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryBilledInclusiveTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.BilledInclusiveTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryPaidExclusiveTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.PaidExclusiveTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryPaidInclusiveTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.PaidInclusiveTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryWithheldTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.WithheldTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryUseTax : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.ProjectCuryRGOL : Edm.Decimal
PX.Objects.PM.Project.Cashflow.Projections.PMCommitmentBillingByDate.RGOL : Edm.Decimal

# PX.Objects.PM.ProjectAPTran (EntityType)

Label: "AP Transactions"
Key: ProjectID, RefNbr, TranType
Entity sets: PX_Objects_PM_ProjectAPTran, APTransactions1, ProjectAPTran

PX.Objects.PM.ProjectAPTran.TranType : Edm.String [key] "Tran. Type"
PX.Objects.PM.ProjectAPTran.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.ProjectAPTran.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.ProjectAPTran.CuryTranAmt : Edm.Decimal "Total Amount"
PX.Objects.PM.ProjectAPTran.CuryTranBal : Edm.Decimal "Balance"
PX.Objects.PM.ProjectAPTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.ProjectAPTran.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.PM.ProjectAPTran.APPaymentByRefNbr -> PX.Objects.AP.APPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.PM.ProjectAPTran.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)

# PX.Objects.PM.ProjectARTran (EntityType)

Label: "AR Transactions"
Key: ProjectID, RefNbr, TranType
Entity sets: PX_Objects_PM_ProjectARTran, ARTransactions1, ProjectARTran

PX.Objects.PM.ProjectARTran.TranType : Edm.String [key] "Tran. Type"
PX.Objects.PM.ProjectARTran.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.ProjectARTran.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.ProjectARTran.CuryTranAmt : Edm.Decimal "Total Amount"
PX.Objects.PM.ProjectARTran.CuryTranBal : Edm.Decimal "Balance"
PX.Objects.PM.ProjectARTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.ProjectARTran.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.PM.ProjectARTran.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.PM.ProjectARTran.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.PM.ProjectARTran.DRScheduleByTranType -> PX.Objects.DR.DRSchedule (TranType=DocType)
PX.Objects.PM.ProjectARTran.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.PM.ProjectARTran.SOInvoiceByOrigInvoiceType -> PX.Objects.SO.SOInvoice

# PX.Objects.PM.ProjectCASplit (EntityType)

Label: "CA Transaction Details"
Key: ProjectID, RefNbr, TranType
Entity sets: PX_Objects_PM_ProjectCASplit, CATransactionDetails1, ProjectCASplit

PX.Objects.PM.ProjectCASplit.TranType : Edm.String [key] "Tran. Type"
PX.Objects.PM.ProjectCASplit.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.ProjectCASplit.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.ProjectCASplit.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)

# PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile (EntityType)

Label: "Linked File"
BaseType: PX.SM.UploadFileWithTags
Key: FileID (inherited from PX.SM.UploadFile)
Entity sets: PX_Objects_PM_ProjectFiles_FileEntryForms_PMLinkedFile, LinkedFile, PMLinkedFile
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.IsChecked : Edm.Boolean
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.Initialized : Edm.Boolean "Initialized"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.ImageUrl : Edm.String "Image"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.FileType : Edm.String "File Type"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.LinkType : Edm.String
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.BAccountID : Edm.Int32 "Business Account"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.LinkedDocumentType : Edm.String "Document Type"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.LinkedDocumentNumber : Edm.Guid "Document Number"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.LinkedDocumentNoteID : Edm.Guid "Document ID"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.Version : Edm.String "Version"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.CreationDate : Edm.String "Creation Date"
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.CheckOutEnabled : Edm.Boolean
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.CheckInEnabled : Edm.Boolean
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.UnlinkFromEntityEnabled : Edm.Boolean
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.CreateNewVersionEnabled : Edm.Boolean
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.LinkToEntityEnabled : Edm.Boolean
PX.Objects.PM.ProjectFiles.FileEntryForms.PMLinkedFile.DeleteFileEnabled : Edm.Boolean

# PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity (EntityType)

Label: "Project Entity"
Key: LinkedDocumentNoteID, LinkedEntityNoteID, ProjectID
Entity sets: PX_Objects_PM_ProjectFiles_ProjectEntities_PMProjectEntity, ProjectEntity, PMProjectEntity
Non-filterable, non-selectable: LinkedDocumentNumber

PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.LinkType : Edm.String
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.LinkedDocumentType : Edm.String "Document Type"
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.LinkedDocumentNoteID : Edm.Guid [key] "Document Number"
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.LinkedEntityNoteID : Edm.Guid [key]
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.LinkedDocumentNumber : Edm.String "Document Number"
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.CreatedByScreenID : Edm.String
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.LastModifiedByScreenID : Edm.String
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.ProjectFiles.ProjectEntities.PMProjectEntity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity (EntityType)

Label: "Vendor Entity"
Key: BAccountID, LinkedDocumentNoteID, LinkedEntityNoteID
Entity sets: PX_Objects_PM_ProjectFiles_VendorEntities_PMVendorEntity, VendorEntity, PMVendorEntity
Non-filterable, non-selectable: LinkedDocumentNumber

PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.BAccountID : Edm.Int32 [key] "BAccount"
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.LinkType : Edm.String
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.LinkedDocumentType : Edm.String "Document Type"
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.LinkedDocumentNoteID : Edm.Guid [key] "Document Number"
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.LinkedEntityNoteID : Edm.Guid [key]
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.LinkedDocumentNumber : Edm.String "Document Number"
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.CreatedByID : Edm.Guid "Created By"
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.CreatedByScreenID : Edm.String
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.LastModifiedByScreenID : Edm.String
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PM.ProjectFiles.VendorEntities.PMVendorEntity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PM.ProjectGLTran (EntityType)

Label: "GL Transaction"
Key: BatchNbr, Module, ProjectID
Entity sets: PX_Objects_PM_ProjectGLTran, GLTransaction1, ProjectGLTran

PX.Objects.PM.ProjectGLTran.Module : Edm.String [key] "Module"
PX.Objects.PM.ProjectGLTran.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.PM.ProjectGLTran.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.ProjectGLTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.ProjectGLTran.BatchByBatchNbr -> PX.Objects.GL.Batch (Module=Module, BatchNbr=BatchNbr)

# PX.Objects.PM.ProjectINTran (EntityType)

Label: "IN Transaction"
Key: DocType, ProjectID, RefNbr
Entity sets: PX_Objects_PM_ProjectINTran, INTransaction1, ProjectINTran

PX.Objects.PM.ProjectINTran.DocType : Edm.String [key] "Document Type"
PX.Objects.PM.ProjectINTran.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.ProjectINTran.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.ProjectINTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.ProjectINTran.INRegisterByRefNbr -> PX.Objects.IN.INRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PM.ProjectINTran.INKitRegisterByRefNbr -> PX.Objects.IN.INKitRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PM.ProjectINTran.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)

# PX.Objects.PM.ProjectParentChild.PMChildProject (EntityType)

Label: "Child Project"
BaseType: PX.Objects.PM.PMProject
Key: BaseType, ContractCD (inherited from PX.Objects.CT.Contract)
Entity sets: PX_Objects_PM_ProjectParentChild_PMChildProject, ChildProject, PMChildProject

# PX.Objects.PM.ProjectParentChild.PMChildTask (EntityType)

Label: "Child Task"
BaseType: PX.Objects.PM.PMTask
Key: ProjectID, TaskCD (inherited from PX.Objects.PM.PMTask)
Entity sets: PX_Objects_PM_ProjectParentChild_PMChildTask, ChildTask, PMChildTask

PX.Objects.PM.ProjectParentChild.PMChildTask.ParentTaskID : Edm.Int32

# PX.Objects.PM.ProjectParentChild.PMParentProject (EntityType)

Label: "Child Project"
BaseType: PX.Objects.PM.PMProject
Key: BaseType, ContractCD (inherited from PX.Objects.CT.Contract)
Entity sets: PX_Objects_PM_ProjectParentChild_PMParentProject, ChildProject1, PMParentProject

# PX.Objects.PM.ProjectPMTran (EntityType)

Label: "Project Transaction"
Key: ProjectID, RefNbr, TranType
Entity sets: PX_Objects_PM_ProjectPMTran, ProjectTransaction1, ProjectPMTran

PX.Objects.PM.ProjectPMTran.TranType : Edm.String [key] "Tran. Type"
PX.Objects.PM.ProjectPMTran.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PM.ProjectPMTran.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.PM.ProjectPMTran.BAccountID : Edm.Int32
PX.Objects.PM.ProjectPMTran.CuryTranAmt : Edm.Decimal "Total Amount"
PX.Objects.PM.ProjectPMTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PM.ProjectPMTran.PMProjectByParentProjectID -> PX.Objects.PM.PMProject
PX.Objects.PM.ProjectPMTran.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.PM.ProjectPMTran.BAccountByResourceID -> PX.Objects.CR.BAccount
PX.Objects.PM.ProjectPMTran.PMRegisterByRefNbr -> PX.Objects.PM.PMRegister (TranType=Module, RefNbr=RefNbr)

# PX.Objects.PMRole (EntityType)

Label: "Project Role"
Singletons: PX_Objects_PMRole, ProjectRole, PMRole

PX.Objects.PMRole.RoleID : Edm.String "Role"
PX.Objects.PMRole.Description : Edm.String "Description"
PX.Objects.PMRole.LocalizedDescription : Edm.String "Role"
PX.Objects.PMRole.tstamp : Edm.Binary
PX.Objects.PMRole.PMProjectContactCollection -> Collection(PX.Objects.PM.PMProjectContact)

# PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc (EntityType)

Label: "Purchase Order to Accounts Payable Document Link"
Key: DocType, PONbr, POType, RefNbr
Entity sets: PX_Objects_PO_DAC_Projections_POBlanketOrderAPDoc, PurchaseOrdertoAccountsPayableDocumentLink, POBlanketOrderAPDoc
Non-filterable, non-selectable: TotalAmt, StatusText

PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.DocType : Edm.String [key] "Type"
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.POType : Edm.String [key] "PO Type"
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.PONbr : Edm.String [key] "PO Number"
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.Status : Edm.String "Status"
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.TotalQty : Edm.Decimal "Billed Qty."
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.TotalTranAmt : Edm.Decimal
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.TotalRetainageAmt : Edm.Decimal
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.TotalAmt : Edm.Decimal "Billed Amt."
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.TotalPPVAmt : Edm.Decimal "PPV Amt"
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.CuryID : Edm.String "Currency"
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.StatusText : Edm.String
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.POOrderByOrderNbr -> PX.Objects.PO.POOrder
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder (EntityType)

Label: "Purchase Blanket Order to Purchase Order Link"
Key: OrderNbr, OrderType, PONbr, POType
Entity sets: PX_Objects_PO_DAC_Projections_POBlanketOrderPOOrder, PurchaseBlanketOrdertoPurchaseOrderLink, POBlanketOrderPOOrder
Non-filterable, non-selectable: NoteText, StatusText

PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.Status : Edm.String "Order Status"
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.TotalQty : Edm.Decimal "Ordered Qty."
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.POType : Edm.String [key]
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.PONbr : Edm.String [key]
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.NoteID : Edm.Guid
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.NoteText : Edm.String "Note Text"
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.StatusText : Edm.String
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)

# PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt (EntityType)

Label: "Purchase Blanket Order to Purchase Receipt Link"
Key: OrderNbr, OrderType, PONbr, POType, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_DAC_Projections_POBlanketOrderPOReceipt, PurchaseBlanketOrdertoPurchaseReceiptLink, POBlanketOrderPOReceipt

PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.ReceiptType : Edm.String [key] "Receipt Type"
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.POType : Edm.String [key]
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.PONbr : Edm.String [key]
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.ReceiptDate : Edm.DateTimeOffset "Receipt Date"
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.Status : Edm.String "Receipt Status"
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.TotalQty : Edm.Decimal "Received Qty."
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)

# PX.Objects.PO.DAC.Projections.POReceiptLineAdd (EntityType)

Label: "Purchase Receipt Line"
BaseType: PX.Objects.PO.POReceiptLineS
Key: LineNbr, ReceiptNbr, ReceiptType (inherited from PX.Objects.PO.POReceiptLineS)
Entity sets: PX_Objects_PO_DAC_Projections_POReceiptLineAdd

# PX.Objects.PO.DropShipPOLine (EntityType)

Label: "PO Drop-Ship Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PO_DropShipPOLine, PODropShipLine, DropShipPOLine

PX.Objects.PO.DropShipPOLine.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.DropShipPOLine.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.DropShipPOLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.DropShipPOLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.DropShipPOLine.TranDesc : Edm.String "Description"
PX.Objects.PO.DropShipPOLine.UOM : Edm.String "UOM"
PX.Objects.PO.DropShipPOLine.OrderQty : Edm.Decimal "Not Linked Qty."
PX.Objects.PO.DropShipPOLine.NoteID : Edm.Guid
PX.Objects.PO.DropShipPOLine.SOOrderType : Edm.String
PX.Objects.PO.DropShipPOLine.SOOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.PO.DropShipPOLine.SOLineNbr : Edm.Int32 "Sales Order Line Nbr."
PX.Objects.PO.DropShipPOLine.SOLinkActive : Edm.Boolean "SO Linked"
PX.Objects.PO.DropShipPOLine.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.PO.DropShipPOLine.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.PO.DropShipPOLine.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.DropShipPOLine.SOLineBySOLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOLineNbr=LineNbr)
PX.Objects.PO.DropShipPOLine.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.PO.DropShipPOLine.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.PO.DropShipPOLine.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.DropShipPOLine.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.DropShipPOLine.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PO.DropShipPOLine.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PO.DropShipPOLine.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PO.DropShipPOLine.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PO.DropShipPOLine.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.PO.DropShipPOLine.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PO.DropShipPOLine.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.PO.DropShipPOLine.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PO.DropShipPOLine.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PO.DropShipPOLine.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.PO.INTransitLineStatusSO (EntityType)

Key: SOShipmentLineNbr, SOShipmentNbr
Entity sets: PX_Objects_PO_INTransitLineStatusSO

PX.Objects.PO.INTransitLineStatusSO.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.INTransitLineStatusSO.CostSiteID : Edm.Int32
PX.Objects.PO.INTransitLineStatusSO.ToSiteID : Edm.Int32 "To Warehouse ID"
PX.Objects.PO.INTransitLineStatusSO.OrigModule : Edm.String "Source"
PX.Objects.PO.INTransitLineStatusSO.NoteID : Edm.Guid
PX.Objects.PO.INTransitLineStatusSO.RefNoteID : Edm.Guid
PX.Objects.PO.INTransitLineStatusSO.TransferNbr : Edm.String
PX.Objects.PO.INTransitLineStatusSO.TransferLineNbr : Edm.Int32
PX.Objects.PO.INTransitLineStatusSO.SOOrderType : Edm.String
PX.Objects.PO.INTransitLineStatusSO.SOOrderNbr : Edm.String
PX.Objects.PO.INTransitLineStatusSO.SOOrderLineNbr : Edm.Int32
PX.Objects.PO.INTransitLineStatusSO.SOShipmentType : Edm.String
PX.Objects.PO.INTransitLineStatusSO.SOShipmentNbr : Edm.String [key]
PX.Objects.PO.INTransitLineStatusSO.SOShipmentLineNbr : Edm.Int32 [key]
PX.Objects.PO.INTransitLineStatusSO.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.PO.INTransitLineStatusSO.QtyInTransit : Edm.Decimal
PX.Objects.PO.INTransitLineStatusSO.QtyInTransitToSO : Edm.Decimal
PX.Objects.PO.INTransitLineStatusSO.TranDate : Edm.DateTimeOffset
PX.Objects.PO.INTransitLineStatusSO.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.PO.INTransitLineStatusSO.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOOrderLineNbr=LineNbr)
PX.Objects.PO.INTransitLineStatusSO.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.PO.INTransitLineStatusSO.SOShipLineBySOShipmentLineNbr -> PX.Objects.SO.SOShipLine (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr, SOShipmentLineNbr=LineNbr)
PX.Objects.PO.INTransitLineStatusSO.SOShipmentBySOShipmentNbr -> PX.Objects.SO.SOShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr)

# PX.Objects.PO.LandedCostCode (EntityType)

Label: "Landed Cost Code"
Key: LandedCostCodeID
Entity sets: PX_Objects_PO_LandedCostCode, LandedCostCode
Non-filterable, non-selectable: NoteText

PX.Objects.PO.LandedCostCode.LandedCostCodeID : Edm.String [key] "Landed Cost Code"
PX.Objects.PO.LandedCostCode.Descr : Edm.String "Description"
PX.Objects.PO.LandedCostCode.LCType : Edm.String "Type"
PX.Objects.PO.LandedCostCode.AllocationMethod : Edm.String "Allocation Method"
PX.Objects.PO.LandedCostCode.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.LandedCostCode.TermsID : Edm.String "Terms"
PX.Objects.PO.LandedCostCode.ReasonCode : Edm.String "Reason Code"
PX.Objects.PO.LandedCostCode.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PO.LandedCostCode.NoteID : Edm.Guid
PX.Objects.PO.LandedCostCode.NoteText : Edm.String "Note Text"
PX.Objects.PO.LandedCostCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.LandedCostCode.CreatedByScreenID : Edm.String
PX.Objects.PO.LandedCostCode.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PO.LandedCostCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.LandedCostCode.LastModifiedByScreenID : Edm.String
PX.Objects.PO.LandedCostCode.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PO.LandedCostCode.TStamp : Edm.Binary
PX.Objects.PO.LandedCostCode.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.LandedCostCode.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.LandedCostCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.LandedCostCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.LandedCostCode.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PO.LandedCostCode.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.PO.LandedCostCode.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.PO.LandedCostCode.AccountByLCAccrualAcct -> PX.Objects.GL.Account
PX.Objects.PO.LandedCostCode.AccountByLCVarianceAcct -> PX.Objects.GL.Account
PX.Objects.PO.LandedCostCode.SubByLCAccrualSub -> PX.Objects.GL.Sub
PX.Objects.PO.LandedCostCode.SubByLCVarianceSub -> PX.Objects.GL.Sub
PX.Objects.PO.LandedCostCode.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.LandedCostCode.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.LandedCostCode.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.PO.LandedCostCode.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.LandedCostCode.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.PO.LandedCostCode.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)

# PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail (EntityType)

Label: "Landed Costs Receipt"
BaseType: PX.Objects.PO.POLandedCostReceipt
Key: LCDocType, LCRefNbr, POReceiptNbr, POReceiptType (inherited from PX.Objects.PO.POLandedCostReceipt)
Entity sets: PX_Objects_PO_LandedCosts_POReceiptLandedCostDetail, LandedCostsReceipt, POReceiptLandedCostDetail
Non-filterable, non-selectable: CuryLineAmt

PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.Status : Edm.String "Status"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.CuryID : Edm.String "Currency"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.CuryInfoID : Edm.Int64
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.LandedCostCodeID : Edm.String "Landed Cost Code"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.Descr : Edm.String "Description"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.AllocationMethod : Edm.String "Allocation Method"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.POLandedCostSplitCuryLineAmt : Edm.Decimal
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.POLandedCostDetailCuryLineAmt : Edm.Decimal
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.CuryLineAmt : Edm.Decimal "Amount"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.POLandedCostDetailLineAmt : Edm.Decimal
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.LineAmt : Edm.Decimal
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.APDocType : Edm.String "AP Doc. Type"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.APRefNbr : Edm.String "AP Ref. Nbr."
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.INDocType : Edm.String "IN Doc. Type"
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.INRefNbr : Edm.String "IN Ref. Nbr."
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.APInvoiceByAPDocType -> PX.Objects.AP.APInvoice (APRefNbr=RefNbr, APDocType=DocType)
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.LandedCostCodeByLandedCostCodeID -> PX.Objects.PO.LandedCostCode (LandedCostCodeID=LandedCostCodeID)
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.INRegisterByINDocType -> PX.Objects.IN.INRegister (INRefNbr=RefNbr, INDocType=DocType)
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.APInvoiceByAPRefNbr -> PX.Objects.AP.APInvoice (APDocType=DocType, APRefNbr=RefNbr)
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail.INRegisterByINRefNbr -> PX.Objects.IN.INRegister (INDocType=DocType, INRefNbr=RefNbr)

# PX.Objects.PO.LandedCosts.POReceiptLineAdd (EntityType)

Label: "Purchase Receipt Line"
Key: LineNbr, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_LandedCosts_POReceiptLineAdd, PurchaseReceiptLine, POReceiptLineAdd

PX.Objects.PO.LandedCosts.POReceiptLineAdd.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.LandedCosts.POReceiptLineAdd.ReceiptType : Edm.String [key] "Receipt Type"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.InvoiceNbr : Edm.String "Vendor Ref."
PX.Objects.PO.LandedCosts.POReceiptLineAdd.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.LandedCosts.POReceiptLineAdd.SortOrder : Edm.Int32
PX.Objects.PO.LandedCosts.POReceiptLineAdd.Released : Edm.Boolean "Released"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.LineType : Edm.String "Line Type"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.IsStockItem : Edm.Boolean
PX.Objects.PO.LandedCosts.POReceiptLineAdd.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.ReceiptDate : Edm.DateTimeOffset
PX.Objects.PO.LandedCosts.POReceiptLineAdd.ReceiptLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.LandedCosts.POReceiptLineAdd.UOM : Edm.String "UOM"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.ReceiptQty : Edm.Decimal "Receipt Qty."
PX.Objects.PO.LandedCosts.POReceiptLineAdd.BaseReceiptQty : Edm.Decimal
PX.Objects.PO.LandedCosts.POReceiptLineAdd.CuryInfoID : Edm.Int64
PX.Objects.PO.LandedCosts.POReceiptLineAdd.UnitCost : Edm.Decimal
PX.Objects.PO.LandedCosts.POReceiptLineAdd.TranCostFinal : Edm.Decimal "Final IN Ext. Cost"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.UnitWeight : Edm.Decimal "Unit Weight"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.UnitVolume : Edm.Decimal "Unit Volume"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.ExpenseAcctID : Edm.Int32
PX.Objects.PO.LandedCosts.POReceiptLineAdd.ExpenseSubID : Edm.Int32
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POAccrualAcctID : Edm.Int32
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POAccrualSubID : Edm.Int32
PX.Objects.PO.LandedCosts.POReceiptLineAdd.TranDesc : Edm.String "Transaction Descr."
PX.Objects.PO.LandedCosts.POReceiptLineAdd.ProjectID : Edm.Int32
PX.Objects.PO.LandedCosts.POReceiptLineAdd.TaskID : Edm.Int32
PX.Objects.PO.LandedCosts.POReceiptLineAdd.CostCodeID : Edm.Int32
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POType : Edm.String "Order Type"
PX.Objects.PO.LandedCosts.POReceiptLineAdd.PONbr : Edm.String "Order Nbr."
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.PO.LandedCosts.POReceiptLineAdd.IsUnderCorrection : Edm.Boolean
PX.Objects.PO.LandedCosts.POReceiptLineAdd.Canceled : Edm.Boolean
PX.Objects.PO.LandedCosts.POReceiptLineAdd.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POReceiptByOrigReceiptNbr -> PX.Objects.PO.POReceipt
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POReceiptByOrigReceiptType -> PX.Objects.PO.POReceipt
PX.Objects.PO.LandedCosts.POReceiptLineAdd.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.AccountByExpenseAcctID -> PX.Objects.GL.Account (ExpenseAcctID=AccountID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.AccountByPOAccrualAcctID -> PX.Objects.GL.Account (POAccrualAcctID=AccountID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.SubByExpenseSubID -> PX.Objects.GL.Sub (ExpenseSubID=SubID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.SubByPOAccrualSubID -> PX.Objects.GL.Sub (POAccrualSubID=SubID)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.PO.LandedCosts.POReceiptLineAdd.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.PO.LinkLineOrder (EntityType)

Key: OrderLineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PO_LinkLineOrder

PX.Objects.PO.LinkLineOrder.OrderType : Edm.String [key] "Type"
PX.Objects.PO.LinkLineOrder.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.LinkLineOrder.OrderLineNbr : Edm.Int32 [key] "PO Line"
PX.Objects.PO.LinkLineOrder.POAccrualType : Edm.String
PX.Objects.PO.LinkLineOrder.OrderNoteID : Edm.Guid
PX.Objects.PO.LinkLineOrder.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.LinkLineOrder.VendorID : Edm.Int32
PX.Objects.PO.LinkLineOrder.VendorLocationID : Edm.Int32
PX.Objects.PO.LinkLineOrder.UOM : Edm.String "UOM"
PX.Objects.PO.LinkLineOrder.OrderBaseQty : Edm.Decimal
PX.Objects.PO.LinkLineOrder.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.PO.LinkLineOrder.OrderAmount : Edm.Decimal
PX.Objects.PO.LinkLineOrder.OrderCuryAmount : Edm.Decimal "Amount"
PX.Objects.PO.LinkLineOrder.OrderCuryID : Edm.String "Currency"
PX.Objects.PO.LinkLineOrder.OrderExpenseAcctID : Edm.Int32
PX.Objects.PO.LinkLineOrder.OrderExpenseSubID : Edm.Int32
PX.Objects.PO.LinkLineOrder.OrderTranDesc : Edm.String "Transaction Descr."
PX.Objects.PO.LinkLineOrder.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.PO.LinkLineOrder.PayToVendorID : Edm.Int32
PX.Objects.PO.LinkLineOrder.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.PO.LinkLineOrder.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.LinkLineOrder.VendorByPayToVendorID -> PX.Objects.AP.Vendor (PayToVendorID=BAccountID)
PX.Objects.PO.LinkLineOrder.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.LinkLineOrder.BAccountByShipToBAccountID -> PX.Objects.CR.BAccount
PX.Objects.PO.LinkLineOrder.BAccountByPayToVendorID -> PX.Objects.CR.BAccount (PayToVendorID=BAccountID)
PX.Objects.PO.LinkLineOrder.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID, VendorLocationID=LocationID)
PX.Objects.PO.LinkLineOrder.LocationByShipToLocationID -> PX.Objects.CR.Location
PX.Objects.PO.LinkLineOrder.LocationByVendorID -> PX.Objects.CR.Location (VendorLocationID=LocationID, VendorID=BAccountID)
PX.Objects.PO.LinkLineOrder.LocationByShipToBAccountID -> PX.Objects.CR.Location

# PX.Objects.PO.LinkLineReceipt (EntityType)

Key: ReceiptLineNbr, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_LinkLineReceipt

PX.Objects.PO.LinkLineReceipt.POAccrualType : Edm.String
PX.Objects.PO.LinkLineReceipt.POAccrualRefNoteID : Edm.Guid
PX.Objects.PO.LinkLineReceipt.POAccrualLineNbr : Edm.Int32
PX.Objects.PO.LinkLineReceipt.OrderType : Edm.String "Type"
PX.Objects.PO.LinkLineReceipt.OrderNbr : Edm.String "Order Nbr."
PX.Objects.PO.LinkLineReceipt.OrderLineNbr : Edm.Int32 "PO Line"
PX.Objects.PO.LinkLineReceipt.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.LinkLineReceipt.VendorID : Edm.Int32
PX.Objects.PO.LinkLineReceipt.VendorLocationID : Edm.Int32
PX.Objects.PO.LinkLineReceipt.UOM : Edm.String "UOM"
PX.Objects.PO.LinkLineReceipt.ReceiptType : Edm.String [key] "Type"
PX.Objects.PO.LinkLineReceipt.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.LinkLineReceipt.ReceiptLineNbr : Edm.Int32 [key] "PO Receipt Line"
PX.Objects.PO.LinkLineReceipt.ReceiptSortOrder : Edm.Int32
PX.Objects.PO.LinkLineReceipt.ReceiptQty : Edm.Decimal "Receipt Qty."
PX.Objects.PO.LinkLineReceipt.ReceiptCuryID : Edm.String "Order Currency"
PX.Objects.PO.LinkLineReceipt.ReceiptUnbilledQty : Edm.Decimal "Unbilled Qty."
PX.Objects.PO.LinkLineReceipt.ReceiptBaseUnbilledQty : Edm.Decimal
PX.Objects.PO.LinkLineReceipt.POAccrualAcctID : Edm.Int32
PX.Objects.PO.LinkLineReceipt.POAccrualSubID : Edm.Int32
PX.Objects.PO.LinkLineReceipt.ReceiptExpenseAcctID : Edm.Int32
PX.Objects.PO.LinkLineReceipt.ReceiptExpenseSubID : Edm.Int32
PX.Objects.PO.LinkLineReceipt.ReciptTranDesc : Edm.String "Transaction Descr."
PX.Objects.PO.LinkLineReceipt.ReceiptVendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.PO.LinkLineReceipt.PayToVendorID : Edm.Int32
PX.Objects.PO.LinkLineReceipt.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.PO.LinkLineReceipt.POReceiptByReceiptType -> PX.Objects.PO.POReceipt (ReceiptNbr=ReceiptNbr, ReceiptType=ReceiptType)
PX.Objects.PO.LinkLineReceipt.POAccrualStatusByPOAccrualType -> PX.Objects.PO.POAccrualStatus (POAccrualRefNoteID=RefNoteID, POAccrualLineNbr=LineNbr, POAccrualType=Type)
PX.Objects.PO.LinkLineReceipt.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.LinkLineReceipt.POReceiptByOrigReceiptNbr -> PX.Objects.PO.POReceipt
PX.Objects.PO.LinkLineReceipt.POReceiptByOrigReceiptType -> PX.Objects.PO.POReceipt
PX.Objects.PO.LinkLineReceipt.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PO.LinkLineReceipt.AccountByPOAccrualAcctID -> PX.Objects.GL.Account (POAccrualAcctID=AccountID)
PX.Objects.PO.LinkLineReceipt.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PO.LinkLineReceipt.SubByPOAccrualSubID -> PX.Objects.GL.Sub (POAccrualSubID=SubID)
PX.Objects.PO.LinkLineReceipt.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.LinkLineReceipt.BAccountByShipToBAccountID -> PX.Objects.CR.BAccount
PX.Objects.PO.LinkLineReceipt.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.LinkLineReceipt.BAccountByDropshipCustomerID -> PX.Objects.CR.BAccount
PX.Objects.PO.LinkLineReceipt.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID, VendorLocationID=LocationID)
PX.Objects.PO.LinkLineReceipt.LocationByShipToLocationID -> PX.Objects.CR.Location
PX.Objects.PO.LinkLineReceipt.LocationByVendorID -> PX.Objects.CR.Location (VendorLocationID=LocationID, VendorID=BAccountID)
PX.Objects.PO.LinkLineReceipt.LocationByShipToBAccountID -> PX.Objects.CR.Location
PX.Objects.PO.LinkLineReceipt.LocationByDropshipCustomerID -> PX.Objects.CR.Location

# PX.Objects.PO.POAccrualDetail (EntityType)

Label: "PO Accrual Detail"
Key: DocumentNoteID, LineNbr
Entity sets: PX_Objects_PO_POAccrualDetail, POAccrualDetail

PX.Objects.PO.POAccrualDetail.DocumentNoteID : Edm.Guid [key]
PX.Objects.PO.POAccrualDetail.LineNbr : Edm.Int32 [key]
PX.Objects.PO.POAccrualDetail.POAccrualRefNoteID : Edm.Guid
PX.Objects.PO.POAccrualDetail.POAccrualLineNbr : Edm.Int32
PX.Objects.PO.POAccrualDetail.POAccrualType : Edm.String
PX.Objects.PO.POAccrualDetail.APDocType : Edm.String
PX.Objects.PO.POAccrualDetail.APRefNbr : Edm.String
PX.Objects.PO.POAccrualDetail.POReceiptType : Edm.String
PX.Objects.PO.POAccrualDetail.POReceiptNbr : Edm.String
PX.Objects.PO.POAccrualDetail.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POAccrualDetail.Posted : Edm.Boolean [required]
PX.Objects.PO.POAccrualDetail.IsDropShip : Edm.Boolean [required]
PX.Objects.PO.POAccrualDetail.IsReversed : Edm.Boolean [required]
PX.Objects.PO.POAccrualDetail.IsReversing : Edm.Boolean [required]
PX.Objects.PO.POAccrualDetail.DocDate : Edm.DateTimeOffset
PX.Objects.PO.POAccrualDetail.FinPeriodID : Edm.String
PX.Objects.PO.POAccrualDetail.TranDesc : Edm.String
PX.Objects.PO.POAccrualDetail.UOM : Edm.String
PX.Objects.PO.POAccrualDetail.AccruedQty : Edm.Decimal [required]
PX.Objects.PO.POAccrualDetail.BaseAccruedQty : Edm.Decimal [required]
PX.Objects.PO.POAccrualDetail.AccruedCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualDetail.PPVAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualDetail.TaxAccruedCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualDetail.TaxAdjAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualDetail.AccruedCostTotal : Edm.Decimal
PX.Objects.PO.POAccrualDetail.PPVAdjRefNbr : Edm.String
PX.Objects.PO.POAccrualDetail.PPVAdjPosted : Edm.Boolean [required]
PX.Objects.PO.POAccrualDetail.TaxAdjRefNbr : Edm.String
PX.Objects.PO.POAccrualDetail.TaxAdjPosted : Edm.Boolean [required]
PX.Objects.PO.POAccrualDetail.UseOrigINDoc : Edm.Boolean [required]
PX.Objects.PO.POAccrualDetail.OrigINDocType : Edm.String
PX.Objects.PO.POAccrualDetail.OrigINDocRefNbr : Edm.String
PX.Objects.PO.POAccrualDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAccrualDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POAccrualDetail.CreatedByScreenID : Edm.String
PX.Objects.PO.POAccrualDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAccrualDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POAccrualDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POAccrualDetail.tstamp : Edm.Binary
PX.Objects.PO.POAccrualDetail.ReversedFinPeriodID : Edm.String
PX.Objects.PO.POAccrualDetail.ReversingFinPeriodID : Edm.String
PX.Objects.PO.POAccrualDetail.APInvoiceByAPRefNbr -> PX.Objects.AP.APInvoice (APDocType=DocType, APRefNbr=RefNbr)
PX.Objects.PO.POAccrualDetail.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POAccrualDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PO.POAccrualDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POAccrualDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POAccrualDetail.POAccrualStatusByPOAccrualType -> PX.Objects.PO.POAccrualStatus (POAccrualRefNoteID=RefNoteID, POAccrualLineNbr=LineNbr, POAccrualType=Type)
PX.Objects.PO.POAccrualDetail.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.PO.POAccrualDetail.POReceiptLineByLineNbr -> PX.Objects.PO.POReceiptLine (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr, LineNbr=LineNbr)
PX.Objects.PO.POAccrualDetail.APTranByLineNbr -> PX.Objects.AP.APTran (APDocType=TranType, APRefNbr=RefNbr, LineNbr=LineNbr)

# PX.Objects.PO.POAccrualInquiryResult (EntityType)

Label: "Purchase Accrual Balance Result"
Key: DocumentNoteID, LineNbr
Entity sets: PX_Objects_PO_POAccrualInquiryResult, PurchaseAccrualBalanceResult, POAccrualInquiryResult
Non-filterable, non-selectable: NoteText, DocumentType, DocumentNbr, VendorName, UnbilledAmt, NotAdjustedAmt, NotReceivedAmt, NotInvoicedAmt, AccrualAmt

PX.Objects.PO.POAccrualInquiryResult.DocumentNoteID : Edm.Guid [key]
PX.Objects.PO.POAccrualInquiryResult.NoteText : Edm.String "Note Text"
PX.Objects.PO.POAccrualInquiryResult.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POAccrualInquiryResult.OrderType : Edm.String "PO Type"
PX.Objects.PO.POAccrualInquiryResult.OrderNbr : Edm.String "PO Ref. Nbr."
PX.Objects.PO.POAccrualInquiryResult.NotReceivedQty : Edm.Decimal "Qty. Not Received"
PX.Objects.PO.POAccrualInquiryResult.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.PO.POAccrualInquiryResult.UnbilledQty : Edm.Decimal "Unbilled Qty."
PX.Objects.PO.POAccrualInquiryResult.POReceiptType : Edm.String
PX.Objects.PO.POAccrualInquiryResult.POReceiptNbr : Edm.String
PX.Objects.PO.POAccrualInquiryResult.APDocType : Edm.String
PX.Objects.PO.POAccrualInquiryResult.APRefNbr : Edm.String
PX.Objects.PO.POAccrualInquiryResult.IsReversed : Edm.Boolean
PX.Objects.PO.POAccrualInquiryResult.IsReversing : Edm.Boolean
PX.Objects.PO.POAccrualInquiryResult.DocumentType : Edm.String "Document Type"
PX.Objects.PO.POAccrualInquiryResult.DocumentNbr : Edm.String "Document Number"
PX.Objects.PO.POAccrualInquiryResult.FinPeriodID : Edm.String "Post Period"
PX.Objects.PO.POAccrualInquiryResult.DocDate : Edm.DateTimeOffset "Document Date"
PX.Objects.PO.POAccrualInquiryResult.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POAccrualInquiryResult.VendorName : Edm.String "Vendor Name"
PX.Objects.PO.POAccrualInquiryResult.INDocType : Edm.String "IN Document Type"
PX.Objects.PO.POAccrualInquiryResult.INRefNbr : Edm.String "IN Document Ref. Nbr."
PX.Objects.PO.POAccrualInquiryResult.PPVAdjRefNbr : Edm.String "PPV Adj. Ref. Nbr."
PX.Objects.PO.POAccrualInquiryResult.PPVAdjPosted : Edm.Boolean
PX.Objects.PO.POAccrualInquiryResult.TaxAdjRefNbr : Edm.String "Tax Adj. Ref. Nbr."
PX.Objects.PO.POAccrualInquiryResult.TaxAdjPosted : Edm.Boolean
PX.Objects.PO.POAccrualInquiryResult.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POAccrualInquiryResult.TranDesc : Edm.String "Description"
PX.Objects.PO.POAccrualInquiryResult.AccruedCost : Edm.Decimal
PX.Objects.PO.POAccrualInquiryResult.PPVAmt : Edm.Decimal
PX.Objects.PO.POAccrualInquiryResult.AccruedCostTotal : Edm.Decimal
PX.Objects.PO.POAccrualInquiryResult.TaxAdjAmt : Edm.Decimal
PX.Objects.PO.POAccrualInquiryResult.AccruedByReceiptsCost : Edm.Decimal
PX.Objects.PO.POAccrualInquiryResult.AccruedByReceiptsPPVAmt : Edm.Decimal
PX.Objects.PO.POAccrualInquiryResult.AccruedByReceiptsTotal : Edm.Decimal
PX.Objects.PO.POAccrualInquiryResult.AccruedByBillsTotal : Edm.Decimal
PX.Objects.PO.POAccrualInquiryResult.UnbilledAmt : Edm.Decimal "Unbilled Amount"
PX.Objects.PO.POAccrualInquiryResult.NotAdjustedAmt : Edm.Decimal "IN Adjustment Amount Not Released"
PX.Objects.PO.POAccrualInquiryResult.NotReceivedAmt : Edm.Decimal "Not Received Amount"
PX.Objects.PO.POAccrualInquiryResult.NotInvoicedAmt : Edm.Decimal "Drop-Ship Amount Not Invoiced"
PX.Objects.PO.POAccrualInquiryResult.AccrualAmt : Edm.Decimal "PO Accrued Amount"
PX.Objects.PO.POAccrualInquiryResult.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.PO.POAccrualInquiryResult.INRegisterByINDocType -> PX.Objects.IN.INRegister (INRefNbr=RefNbr, INDocType=DocType)
PX.Objects.PO.POAccrualInquiryResult.INRegisterByPPVAdjRefNbr -> PX.Objects.IN.INRegister (PPVAdjRefNbr=RefNbr)
PX.Objects.PO.POAccrualInquiryResult.INRegisterByTaxAdjRefNbr -> PX.Objects.IN.INRegister (TaxAdjRefNbr=RefNbr)
PX.Objects.PO.POAccrualInquiryResult.APInvoiceByAPRefNbr -> PX.Objects.AP.APInvoice (APDocType=DocType, APRefNbr=RefNbr)
PX.Objects.PO.POAccrualInquiryResult.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.PO.POAccrualInquiryResult.POReceiptLineByLineNbr -> PX.Objects.PO.POReceiptLine (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr, LineNbr=LineNbr)
PX.Objects.PO.POAccrualInquiryResult.APTranByLineNbr -> PX.Objects.AP.APTran (APDocType=TranType, APRefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.PO.POAccrualInquiryResult.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)

# PX.Objects.PO.POAccrualSplit (EntityType)

Label: "PO Accrual Allocation"
Key: APDocType, APLineNbr, APRefNbr, POReceiptLineNbr, POReceiptNbr, POReceiptType
Entity sets: PX_Objects_PO_POAccrualSplit, POAccrualAllocation, POAccrualSplit

PX.Objects.PO.POAccrualSplit.RefNoteID : Edm.Guid
PX.Objects.PO.POAccrualSplit.LineNbr : Edm.Int32
PX.Objects.PO.POAccrualSplit.Type : Edm.String
PX.Objects.PO.POAccrualSplit.APDocType : Edm.String [key]
PX.Objects.PO.POAccrualSplit.APRefNbr : Edm.String [key]
PX.Objects.PO.POAccrualSplit.APLineNbr : Edm.Int32 [key]
PX.Objects.PO.POAccrualSplit.POReceiptType : Edm.String [key]
PX.Objects.PO.POAccrualSplit.POReceiptNbr : Edm.String [key]
PX.Objects.PO.POAccrualSplit.POReceiptLineNbr : Edm.Int32 [key]
PX.Objects.PO.POAccrualSplit.UOM : Edm.String
PX.Objects.PO.POAccrualSplit.AccruedQty : Edm.Decimal
PX.Objects.PO.POAccrualSplit.BaseAccruedQty : Edm.Decimal [required]
PX.Objects.PO.POAccrualSplit.AccruedCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualSplit.PPVAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualSplit.IsReversed : Edm.Boolean [required]
PX.Objects.PO.POAccrualSplit.TaxAccruedCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualSplit.FinPeriodID : Edm.String
PX.Objects.PO.POAccrualSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAccrualSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POAccrualSplit.CreatedByScreenID : Edm.String
PX.Objects.PO.POAccrualSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAccrualSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POAccrualSplit.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POAccrualSplit.tstamp : Edm.Binary
PX.Objects.PO.POAccrualSplit.APInvoiceByAPRefNbr -> PX.Objects.AP.APInvoice (APDocType=DocType, APRefNbr=RefNbr)
PX.Objects.PO.POAccrualSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POAccrualSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POAccrualSplit.POAccrualStatusByType -> PX.Objects.PO.POAccrualStatus (RefNoteID=RefNoteID, LineNbr=LineNbr, Type=Type)
PX.Objects.PO.POAccrualSplit.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.PO.POAccrualSplit.POReceiptLineByPOReceiptLineNbr -> PX.Objects.PO.POReceiptLine (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr, POReceiptLineNbr=LineNbr)
PX.Objects.PO.POAccrualSplit.APTranByAPLineNbr -> PX.Objects.AP.APTran (APDocType=TranType, APRefNbr=RefNbr, APLineNbr=LineNbr)

# PX.Objects.PO.POAccrualStatus (EntityType)

Label: "PO Accrual Status"
Key: LineNbr, RefNoteID, Type
Entity sets: PX_Objects_PO_POAccrualStatus, POAccrualStatus
Non-filterable, non-selectable: IsAccountAffected, UOM

PX.Objects.PO.POAccrualStatus.RefNoteID : Edm.Guid [key]
PX.Objects.PO.POAccrualStatus.LineNbr : Edm.Int32 [key]
PX.Objects.PO.POAccrualStatus.Type : Edm.String [key]
PX.Objects.PO.POAccrualStatus.LineType : Edm.String
PX.Objects.PO.POAccrualStatus.OrderType : Edm.String
PX.Objects.PO.POAccrualStatus.OrderNbr : Edm.String
PX.Objects.PO.POAccrualStatus.OrderLineNbr : Edm.Int32
PX.Objects.PO.POAccrualStatus.ReceiptType : Edm.String
PX.Objects.PO.POAccrualStatus.ReceiptNbr : Edm.String
PX.Objects.PO.POAccrualStatus.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POAccrualStatus.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POAccrualStatus.OrigUOM : Edm.String
PX.Objects.PO.POAccrualStatus.OrigQty : Edm.Decimal
PX.Objects.PO.POAccrualStatus.BaseOrigQty : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.OrigCuryID : Edm.String
PX.Objects.PO.POAccrualStatus.CuryOrigAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.OrigAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.CuryOrigCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.OrigCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.CuryOrigDiscAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.OrigDiscAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.ReceivedUOM : Edm.String
PX.Objects.PO.POAccrualStatus.ReceivedQty : Edm.Decimal
PX.Objects.PO.POAccrualStatus.BaseReceivedQty : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.ReceivedCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.BilledUOM : Edm.String
PX.Objects.PO.POAccrualStatus.BilledQty : Edm.Decimal
PX.Objects.PO.POAccrualStatus.BaseBilledQty : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.BillCuryID : Edm.String
PX.Objects.PO.POAccrualStatus.CuryBilledAmt : Edm.Decimal
PX.Objects.PO.POAccrualStatus.BilledAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.CuryBilledCost : Edm.Decimal
PX.Objects.PO.POAccrualStatus.BilledCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.CuryBilledDiscAmt : Edm.Decimal
PX.Objects.PO.POAccrualStatus.BilledDiscAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.PPVAmt : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.ReceivedTaxAdjCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.CuryBilledTaxAdjCost : Edm.Decimal
PX.Objects.PO.POAccrualStatus.BilledTaxAdjCost : Edm.Decimal [required]
PX.Objects.PO.POAccrualStatus.IsClosed : Edm.Boolean
PX.Objects.PO.POAccrualStatus.IsAccountAffected : Edm.Boolean
PX.Objects.PO.POAccrualStatus.DropshipExpenseRecording : Edm.String
PX.Objects.PO.POAccrualStatus.UOM : Edm.String
PX.Objects.PO.POAccrualStatus.MaxFinPeriodID : Edm.String
PX.Objects.PO.POAccrualStatus.ClosedFinPeriodID : Edm.String
PX.Objects.PO.POAccrualStatus.UnreleasedReceiptCntr : Edm.Int32 [required]
PX.Objects.PO.POAccrualStatus.UnreleasedPPVAdjCntr : Edm.Int32 [required]
PX.Objects.PO.POAccrualStatus.UnreleasedTaxAdjCntr : Edm.Int32 [required]
PX.Objects.PO.POAccrualStatus.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAccrualStatus.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POAccrualStatus.CreatedByScreenID : Edm.String
PX.Objects.PO.POAccrualStatus.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAccrualStatus.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POAccrualStatus.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POAccrualStatus.tstamp : Edm.Binary
PX.Objects.PO.POAccrualStatus.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.POAccrualStatus.VendorByPayToVendorID -> PX.Objects.AP.Vendor
PX.Objects.PO.POAccrualStatus.POLineByOrderLineNbr -> PX.Objects.PO.POLine (OrderType=OrderType, OrderNbr=OrderNbr, OrderLineNbr=LineNbr)
PX.Objects.PO.POAccrualStatus.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POAccrualStatus.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POAccrualStatus.BAccountByPayToVendorID -> PX.Objects.CR.BAccount
PX.Objects.PO.POAccrualStatus.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POAccrualStatus.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POAccrualStatus.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POAccrualStatus.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POAccrualStatus.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POAccrualStatus.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POAccrualStatus.CurrencyByOrigCuryID -> PX.Objects.CM.Currency (OrigCuryID=CuryID)
PX.Objects.PO.POAccrualStatus.CurrencyByBillCuryID -> PX.Objects.CM.Currency (BillCuryID=CuryID)
PX.Objects.PO.POAccrualStatus.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POAccrualStatus.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.PO.POAccrualStatus.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POAccrualStatus.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.PO.POAccrualStatus.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.PO.POAccrualStatus.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.PO.POAddress (EntityType)

Label: "PO Address"
Key: AddressID
Entity sets: PX_Objects_PO_POAddress, POAddress
Non-filterable, non-selectable: OverrideAddress

PX.Objects.PO.POAddress.AddressID : Edm.Int32 [key]
PX.Objects.PO.POAddress.BAccountID : Edm.Int32
PX.Objects.PO.POAddress.BAccountAddressID : Edm.Int32
PX.Objects.PO.POAddress.IsDefaultAddress : Edm.Boolean [required] "Is Default Address"
PX.Objects.PO.POAddress.OverrideAddress : Edm.Boolean "Override"
PX.Objects.PO.POAddress.RevisionID : Edm.Int32 "RevisionID"
PX.Objects.PO.POAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.PO.POAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.PO.POAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.PO.POAddress.City : Edm.String "City"
PX.Objects.PO.POAddress.CountryID : Edm.String "Country"
PX.Objects.PO.POAddress.State : Edm.String "State"
PX.Objects.PO.POAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.PO.POAddress.Department : Edm.String "Department"
PX.Objects.PO.POAddress.SubDepartment : Edm.String "Subdepartment"
PX.Objects.PO.POAddress.StreetName : Edm.String "Street Name"
PX.Objects.PO.POAddress.BuildingNumber : Edm.String "Building Number"
PX.Objects.PO.POAddress.BuildingName : Edm.String "Building Name"
PX.Objects.PO.POAddress.Floor : Edm.String "Floor"
PX.Objects.PO.POAddress.UnitNumber : Edm.String "Unit Number"
PX.Objects.PO.POAddress.PostBox : Edm.String "Post Box"
PX.Objects.PO.POAddress.Room : Edm.String "Room"
PX.Objects.PO.POAddress.TownLocationName : Edm.String "Town Location Name"
PX.Objects.PO.POAddress.DistrictName : Edm.String "District Name"
PX.Objects.PO.POAddress.AddressType : Edm.String "Address Type"
PX.Objects.PO.POAddress.CareOf : Edm.String "Care Of"
PX.Objects.PO.POAddress.NoteID : Edm.Guid
PX.Objects.PO.POAddress.tstamp : Edm.Binary
PX.Objects.PO.POAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POAddress.CreatedByScreenID : Edm.String
PX.Objects.PO.POAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POAddress.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAddress.Latitude : Edm.Decimal "Latitude"
PX.Objects.PO.POAddress.Longitude : Edm.Decimal "Longitude"
PX.Objects.PO.POAddress.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.PO.POAddress.AddressByBAccountAddressID -> PX.Objects.CR.Address (BAccountAddressID=AddressID)
PX.Objects.PO.POAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PO.POAddress.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.PO.POAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.PO.POAddress.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.PO.POAddress.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)

# PX.Objects.PO.POAdjust (EntityType)

Label: "Purchase Order Adjust"
Key: AdjdDocType, AdjdOrderNbr, AdjdOrderType, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr
Entity sets: PX_Objects_PO_POAdjust, PurchaseOrderAdjust, POAdjust
Non-filterable, non-selectable: ForceDelete, NoteText

PX.Objects.PO.POAdjust.IsRequest : Edm.Boolean [required] "Linked to Prepayment"
PX.Objects.PO.POAdjust.AdjgDocType : Edm.String [key] "Doc. Type"
PX.Objects.PO.POAdjust.AdjgRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POAdjust.AdjdOrderType : Edm.String [key required] "PO Type"
PX.Objects.PO.POAdjust.AdjdOrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POAdjust.AdjNbr : Edm.Int32 [key]
PX.Objects.PO.POAdjust.AdjdDocType : Edm.String [key required] "Doc. Type"
PX.Objects.PO.POAdjust.AdjdRefNbr : Edm.String [key required] "Reference Nbr."
PX.Objects.PO.POAdjust.Released : Edm.Boolean [required] "Released"
PX.Objects.PO.POAdjust.Voided : Edm.Boolean [required] "Voided"
PX.Objects.PO.POAdjust.AdjgCuryInfoID : Edm.Int64
PX.Objects.PO.POAdjust.CuryAdjgAmt : Edm.Decimal [required] "Applied To Order"
PX.Objects.PO.POAdjust.AdjgAmt : Edm.Decimal [required]
PX.Objects.PO.POAdjust.CuryAdjgBilledAmt : Edm.Decimal [required] "Transferred to Bill"
PX.Objects.PO.POAdjust.AdjgBilledAmt : Edm.Decimal [required]
PX.Objects.PO.POAdjust.AdjdCuryInfoID : Edm.Int64
PX.Objects.PO.POAdjust.CuryAdjdAmt : Edm.Decimal [required]
PX.Objects.PO.POAdjust.AdjdAmt : Edm.Decimal [required]
PX.Objects.PO.POAdjust.StubNbr : Edm.String
PX.Objects.PO.POAdjust.CashAccountID : Edm.Int32
PX.Objects.PO.POAdjust.PaymentMethodID : Edm.String
PX.Objects.PO.POAdjust.ForceDelete : Edm.Boolean
PX.Objects.PO.POAdjust.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAdjust.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POAdjust.CreatedByScreenID : Edm.String
PX.Objects.PO.POAdjust.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POAdjust.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POAdjust.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POAdjust.tstamp : Edm.Binary
PX.Objects.PO.POAdjust.NoteID : Edm.Guid
PX.Objects.PO.POAdjust.NoteText : Edm.String "Note Text"
PX.Objects.PO.POAdjust.APInvoiceByAdjdRefNbr -> PX.Objects.AP.APInvoice (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.PO.POAdjust.APInvoiceByAdjdDocType -> PX.Objects.AP.APInvoice (AdjdRefNbr=RefNbr, AdjdDocType=DocType)
PX.Objects.PO.POAdjust.POOrderByAdjdOrderNbr -> PX.Objects.PO.POOrder (AdjdOrderType=OrderType, AdjdOrderNbr=OrderNbr)
PX.Objects.PO.POAdjust.POOrderByAdjdOrderType -> PX.Objects.PO.POOrder (AdjdOrderNbr=OrderNbr, AdjdOrderType=OrderType)
PX.Objects.PO.POAdjust.APPaymentByAdjgRefNbr -> PX.Objects.AP.APPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.PO.POAdjust.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POAdjust.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POAdjust.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.PO.POAdjust.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)

# PX.Objects.PO.POCartReceipt (EntityType)

Label: "Receipt Cart"
Key: CartID, SiteID
Entity sets: PX_Objects_PO_POCartReceipt, ReceiptCart1, POCartReceipt

PX.Objects.PO.POCartReceipt.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.PO.POCartReceipt.CartID : Edm.Int32 [key]
PX.Objects.PO.POCartReceipt.ReceiptType : Edm.String
PX.Objects.PO.POCartReceipt.ReceiptNbr : Edm.String
PX.Objects.PO.POCartReceipt.TransferNbr : Edm.String
PX.Objects.PO.POCartReceipt.tstamp : Edm.Binary
PX.Objects.PO.POCartReceipt.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POCartReceipt.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.PO.POCartReceipt.INRegisterByTransferNbr -> PX.Objects.IN.INRegister (TransferNbr=RefNbr)
PX.Objects.PO.POCartReceipt.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.PO.POContact (EntityType)

Label: "PO Contact"
Key: ContactID
Entity sets: PX_Objects_PO_POContact, POContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.PO.POContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.PO.POContact.BAccountID : Edm.Int32
PX.Objects.PO.POContact.BAccountContactID : Edm.Int32
PX.Objects.PO.POContact.IsDefaultContact : Edm.Boolean [required] "Vendor Default"
PX.Objects.PO.POContact.OverrideContact : Edm.Boolean "Override"
PX.Objects.PO.POContact.RevisionID : Edm.Int32 "RevisionID"
PX.Objects.PO.POContact.Title : Edm.String "Title"
PX.Objects.PO.POContact.Salutation : Edm.String "Job Title"
PX.Objects.PO.POContact.Attention : Edm.String "Attention"
PX.Objects.PO.POContact.FullName : Edm.String "Account Name"
PX.Objects.PO.POContact.Email : Edm.String "Email"
PX.Objects.PO.POContact.Fax : Edm.String "Fax"
PX.Objects.PO.POContact.FaxType : Edm.String "Fax"
PX.Objects.PO.POContact.Phone1 : Edm.String "Phone 1"
PX.Objects.PO.POContact.Phone1Type : Edm.String "Phone 1"
PX.Objects.PO.POContact.Phone2 : Edm.String "Phone 2"
PX.Objects.PO.POContact.Phone2Type : Edm.String "Phone 2"
PX.Objects.PO.POContact.Phone3 : Edm.String "Phone 3"
PX.Objects.PO.POContact.Phone3Type : Edm.String "Phone 3"
PX.Objects.PO.POContact.NoteID : Edm.Guid
PX.Objects.PO.POContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POContact.CreatedByScreenID : Edm.String
PX.Objects.PO.POContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PO.POContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POContact.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PO.POContact.tstamp : Edm.Binary
PX.Objects.PO.POContact.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.PO.POContact.ContactByBAccountContactID -> PX.Objects.CR.Contact (BAccountContactID=ContactID)
PX.Objects.PO.POContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POContact.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.PO.POContact.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)

# PX.Objects.PO.POFixedDemand (EntityType)

Label: "PO Fixed Demand"
BaseType: PX.Objects.IN.INItemPlan
Key: PlanID (inherited from PX.Objects.IN.INItemPlan)
Entity sets: PX_Objects_PO_POFixedDemand, POFixedDemand
Non-filterable, non-selectable: LocalizedPlanDescr, SourceSiteDescr, OrderQty, NoteText, AddLeadTimeDays, EffPrice, ExtWeight, ExtVolume, ExtCost, DemandProjectID, CuryID, SorterString, SalesBranchID, SalesCustomerID, IsSpecialOrder

PX.Objects.PO.POFixedDemand.RequestedDate : Edm.DateTimeOffset "Requested On"
PX.Objects.PO.POFixedDemand.PlanDescr : Edm.String
PX.Objects.PO.POFixedDemand.LocalizedPlanDescr : Edm.String "Plan Type"
PX.Objects.PO.POFixedDemand.SourceSiteDescr : Edm.String "Demand Warehouse Description"
PX.Objects.PO.POFixedDemand.PriceRecordID : Edm.Int32
PX.Objects.PO.POFixedDemand.DemandUOM : Edm.String "UOM"
PX.Objects.PO.POFixedDemand.UnitMultDiv : Edm.String
PX.Objects.PO.POFixedDemand.UnitRate : Edm.Decimal
PX.Objects.PO.POFixedDemand.PlanUnitQty : Edm.Decimal
PX.Objects.PO.POFixedDemand.OrderQty : Edm.Decimal "Quantity"
PX.Objects.PO.POFixedDemand.NoteID : Edm.Guid
PX.Objects.PO.POFixedDemand.NoteText : Edm.String "Note Text"
PX.Objects.PO.POFixedDemand.AddLeadTimeDays : Edm.Int16 "Add. Lead Time (Days)"
PX.Objects.PO.POFixedDemand.EffPrice : Edm.Decimal "Vendor Price"
PX.Objects.PO.POFixedDemand.ExtWeight : Edm.Decimal "Weight"
PX.Objects.PO.POFixedDemand.ExtVolume : Edm.Decimal "Volume"
PX.Objects.PO.POFixedDemand.ExtCost : Edm.Decimal "Extended Amt."
PX.Objects.PO.POFixedDemand.DemandProjectID : Edm.Int32
PX.Objects.PO.POFixedDemand.ItemClassCD : Edm.String "Class ID"
PX.Objects.PO.POFixedDemand.CuryID : Edm.String "Currency"
PX.Objects.PO.POFixedDemand.SorterString : Edm.String
PX.Objects.PO.POFixedDemand.SalesBranchID : Edm.Int32
PX.Objects.PO.POFixedDemand.SalesCustomerID : Edm.Int32 "Customer"
PX.Objects.PO.POFixedDemand.IsSpecialOrder : Edm.Boolean
PX.Objects.PO.POFixedDemand.INItemClassByItemClassCD -> PX.Objects.IN.INItemClass (ItemClassCD=ItemClassCD)
PX.Objects.PO.POFixedDemand.INSiteByPOSiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POFixedDemand.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.PO.POLandedCostDetail (EntityType)

Label: "Landed Costs Detail"
Key: DocType, LineNbr, RefNbr
Entity sets: PX_Objects_PO_POLandedCostDetail, LandedCostsDetail, POLandedCostDetail
Non-filterable, non-selectable: NoteText

PX.Objects.PO.POLandedCostDetail.BranchID : Edm.Int32 "Branch"
PX.Objects.PO.POLandedCostDetail.DocType : Edm.String [key] "Doc. Type"
PX.Objects.PO.POLandedCostDetail.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POLandedCostDetail.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POLandedCostDetail.SortOrder : Edm.Int32 "Line Order"
PX.Objects.PO.POLandedCostDetail.CuryInfoID : Edm.Int64
PX.Objects.PO.POLandedCostDetail.LandedCostCodeID : Edm.String "Landed Cost Code"
PX.Objects.PO.POLandedCostDetail.Descr : Edm.String "Description"
PX.Objects.PO.POLandedCostDetail.AllocationMethod : Edm.String "Allocation Method"
PX.Objects.PO.POLandedCostDetail.CuryLineAmt : Edm.Decimal [required] "Amount"
PX.Objects.PO.POLandedCostDetail.LineAmt : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDetail.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PO.POLandedCostDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POLandedCostDetail.LCAccrualAcct : Edm.Int32
PX.Objects.PO.POLandedCostDetail.LCAccrualSub : Edm.Int32
PX.Objects.PO.POLandedCostDetail.APDocType : Edm.String "AP Doc. Type"
PX.Objects.PO.POLandedCostDetail.APRefNbr : Edm.String "AP Ref. Nbr."
PX.Objects.PO.POLandedCostDetail.INDocType : Edm.String "IN Doc. Type"
PX.Objects.PO.POLandedCostDetail.INRefNbr : Edm.String "IN Ref. Nbr."
PX.Objects.PO.POLandedCostDetail.NoteID : Edm.Guid
PX.Objects.PO.POLandedCostDetail.NoteText : Edm.String "Note Text"
PX.Objects.PO.POLandedCostDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POLandedCostDetail.CreatedByScreenID : Edm.String
PX.Objects.PO.POLandedCostDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLandedCostDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POLandedCostDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POLandedCostDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLandedCostDetail.tstamp : Edm.Binary
PX.Objects.PO.POLandedCostDetail.APInvoiceByAPRefNbr -> PX.Objects.AP.APInvoice (APDocType=DocType, APRefNbr=RefNbr)
PX.Objects.PO.POLandedCostDetail.APInvoiceByAPDocType -> PX.Objects.AP.APInvoice (APRefNbr=RefNbr, APDocType=DocType)
PX.Objects.PO.POLandedCostDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POLandedCostDetail.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.PO.POLandedCostDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLandedCostDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POLandedCostDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POLandedCostDetail.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PO.POLandedCostDetail.LandedCostCodeByLandedCostCodeID -> PX.Objects.PO.LandedCostCode (LandedCostCodeID=LandedCostCodeID)
PX.Objects.PO.POLandedCostDetail.POLandedCostDocByRefNbr -> PX.Objects.PO.POLandedCostDoc (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PO.POLandedCostDetail.INRegisterByINRefNbr -> PX.Objects.IN.INRegister (INDocType=DocType, INRefNbr=RefNbr)
PX.Objects.PO.POLandedCostDetail.INRegisterByINDocType -> PX.Objects.IN.INRegister (INRefNbr=RefNbr, INDocType=DocType)
PX.Objects.PO.POLandedCostDetail.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POLandedCostDetail.AccountByLCAccrualAcct -> PX.Objects.GL.Account (LCAccrualAcct=AccountID)
PX.Objects.PO.POLandedCostDetail.SubByLCAccrualSub -> PX.Objects.GL.Sub (LCAccrualSub=SubID)
PX.Objects.PO.POLandedCostDetail.POLandedCostTaxCollection -> Collection(PX.Objects.PO.POLandedCostTax)
PX.Objects.PO.POLandedCostDetail.APTranCollection -> Collection(PX.Objects.AP.APTran)

# PX.Objects.PO.POLandedCostDetailS (EntityType)

Key: DocType, LineNbr, RefNbr
Entity sets: PX_Objects_PO_POLandedCostDetailS

PX.Objects.PO.POLandedCostDetailS.DocType : Edm.String [key] "Doc. Type"
PX.Objects.PO.POLandedCostDetailS.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POLandedCostDetailS.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POLandedCostDetailS.SortOrder : Edm.Int32 "Line Order"
PX.Objects.PO.POLandedCostDetailS.CuryID : Edm.String "Currency"
PX.Objects.PO.POLandedCostDetailS.CuryInfoID : Edm.Int64
PX.Objects.PO.POLandedCostDetailS.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.PO.POLandedCostDetailS.LandedCostCodeID : Edm.String "Landed Cost Code"
PX.Objects.PO.POLandedCostDetailS.Descr : Edm.String "Description"
PX.Objects.PO.POLandedCostDetailS.CuryLineAmt : Edm.Decimal "Amount"
PX.Objects.PO.POLandedCostDetailS.LineAmt : Edm.Decimal
PX.Objects.PO.POLandedCostDetailS.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PO.POLandedCostDetailS.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POLandedCostDetailS.APDocType : Edm.String "AP Doc. Type"
PX.Objects.PO.POLandedCostDetailS.APRefNbr : Edm.String "AP Ref. Nbr."
PX.Objects.PO.POLandedCostDetailS.INDocType : Edm.String "IN Doc. Type"
PX.Objects.PO.POLandedCostDetailS.INRefNbr : Edm.String "IN Ref. Nbr."
PX.Objects.PO.POLandedCostDetailS.APInvoiceByAPDocType -> PX.Objects.AP.APInvoice (APRefNbr=RefNbr, APDocType=DocType)
PX.Objects.PO.POLandedCostDetailS.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POLandedCostDetailS.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PO.POLandedCostDetailS.LandedCostCodeByLandedCostCodeID -> PX.Objects.PO.LandedCostCode (LandedCostCodeID=LandedCostCodeID)
PX.Objects.PO.POLandedCostDetailS.POLandedCostDocByRefNbr -> PX.Objects.PO.POLandedCostDoc (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PO.POLandedCostDetailS.INRegisterByINDocType -> PX.Objects.IN.INRegister (INRefNbr=RefNbr, INDocType=DocType)
PX.Objects.PO.POLandedCostDetailS.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POLandedCostDetailS.APInvoiceByAPRefNbr -> PX.Objects.AP.APInvoice (APDocType=DocType, APRefNbr=RefNbr)
PX.Objects.PO.POLandedCostDetailS.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLandedCostDetailS.INRegisterByINRefNbr -> PX.Objects.IN.INRegister (INDocType=DocType, INRefNbr=RefNbr)
PX.Objects.PO.POLandedCostDetailS.POLandedCostTaxCollection -> Collection(PX.Objects.PO.POLandedCostTax)
PX.Objects.PO.POLandedCostDetailS.APTranCollection -> Collection(PX.Objects.AP.APTran)

# PX.Objects.PO.POLandedCostDoc (EntityType)

Label: "Landed Costs Document"
Key: DocType, RefNbr
Entity sets: PX_Objects_PO_POLandedCostDoc, LandedCostsDocument, POLandedCostDoc
Non-filterable, non-selectable: NoteText, CuryRate

PX.Objects.PO.POLandedCostDoc.DocType : Edm.String [key required] "Type"
PX.Objects.PO.POLandedCostDoc.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POLandedCostDoc.OpenDoc : Edm.Boolean [required] "Open"
PX.Objects.PO.POLandedCostDoc.Released : Edm.Boolean [required] "Released"
PX.Objects.PO.POLandedCostDoc.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PO.POLandedCostDoc.Status : Edm.String "Status"
PX.Objects.PO.POLandedCostDoc.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.PO.POLandedCostDoc.NonTaxable : Edm.Boolean [required] "Non-Taxable"
PX.Objects.PO.POLandedCostDoc.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.POLandedCostDoc.FinPeriodID : Edm.String "Post Period"
PX.Objects.PO.POLandedCostDoc.TranPeriodID : Edm.String "Transaction Period"
PX.Objects.PO.POLandedCostDoc.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POLandedCostDoc.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.PO.POLandedCostDoc.TaxTotal : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDoc.LineCntr : Edm.Int32 [required]
PX.Objects.PO.POLandedCostDoc.CuryID : Edm.String "Currency"
PX.Objects.PO.POLandedCostDoc.CuryInfoID : Edm.Int64
PX.Objects.PO.POLandedCostDoc.CreateBill : Edm.Boolean "Create Bill"
PX.Objects.PO.POLandedCostDoc.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.PO.POLandedCostDoc.CuryLineTotal : Edm.Decimal [required] "Amount Total"
PX.Objects.PO.POLandedCostDoc.LineTotal : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDoc.CuryDocTotal : Edm.Decimal [required] "Document Total"
PX.Objects.PO.POLandedCostDoc.DocTotal : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDoc.CuryAllocatedTotal : Edm.Decimal [required] "Total Allocated Amount"
PX.Objects.PO.POLandedCostDoc.AllocatedTotal : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDoc.CuryControlTotal : Edm.Decimal [required] "Control Total"
PX.Objects.PO.POLandedCostDoc.ControlTotal : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDoc.TermsID : Edm.String "Terms"
PX.Objects.PO.POLandedCostDoc.BillDate : Edm.DateTimeOffset "Bill Date"
PX.Objects.PO.POLandedCostDoc.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.PO.POLandedCostDoc.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.PO.POLandedCostDoc.CuryDiscAmt : Edm.Decimal [required] "Cash Discount"
PX.Objects.PO.POLandedCostDoc.DiscAmt : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDoc.TaxZoneID : Edm.String "Vendor Tax Zone"
PX.Objects.PO.POLandedCostDoc.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PO.POLandedCostDoc.OwnerID : Edm.Int32 "Owner"
PX.Objects.PO.POLandedCostDoc.APDocCreated : Edm.Boolean [required]
PX.Objects.PO.POLandedCostDoc.INDocCreated : Edm.Boolean [required]
PX.Objects.PO.POLandedCostDoc.CuryVatExemptTotal : Edm.Decimal [required] "Tax Exempt Total"
PX.Objects.PO.POLandedCostDoc.VatExemptTotal : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDoc.CuryVatTaxableTotal : Edm.Decimal [required] "Taxable Total"
PX.Objects.PO.POLandedCostDoc.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.PO.POLandedCostDoc.NoteID : Edm.Guid
PX.Objects.PO.POLandedCostDoc.NoteText : Edm.String "Note Text"
PX.Objects.PO.POLandedCostDoc.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POLandedCostDoc.CreatedByScreenID : Edm.String
PX.Objects.PO.POLandedCostDoc.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PO.POLandedCostDoc.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POLandedCostDoc.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POLandedCostDoc.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PO.POLandedCostDoc.tstamp : Edm.Binary
PX.Objects.PO.POLandedCostDoc.CuryRate : Edm.Decimal
PX.Objects.PO.POLandedCostDoc.VendorByPayToVendorID -> PX.Objects.AP.Vendor
PX.Objects.PO.POLandedCostDoc.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POLandedCostDoc.BAccountByPayToVendorID -> PX.Objects.CR.BAccount
PX.Objects.PO.POLandedCostDoc.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PO.POLandedCostDoc.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PO.POLandedCostDoc.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLandedCostDoc.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POLandedCostDoc.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POLandedCostDoc.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PO.POLandedCostDoc.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PO.POLandedCostDoc.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.PO.POLandedCostDoc.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POLandedCostDoc.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POLandedCostDoc.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POLandedCostDoc.POLandedCostTaxCollection -> Collection(PX.Objects.PO.POLandedCostTax)
PX.Objects.PO.POLandedCostDoc.POLandedCostTaxTranCollection -> Collection(PX.Objects.PO.POLandedCostTaxTran)
PX.Objects.PO.POLandedCostDoc.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POLandedCostDoc.POLandedCostReceiptCollection -> Collection(PX.Objects.PO.POLandedCostReceipt)
PX.Objects.PO.POLandedCostDoc.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.PO.POLandedCostDoc.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.PO.POLandedCostDoc.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.PO.POLandedCostDoc.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)

# PX.Objects.PO.POLandedCostDocS (EntityType)

Key: DocType, RefNbr
Entity sets: PX_Objects_PO_POLandedCostDocS

PX.Objects.PO.POLandedCostDocS.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POLandedCostDocS.DocType : Edm.String [key] "Type"
PX.Objects.PO.POLandedCostDocS.OpenDoc : Edm.Boolean "Open"
PX.Objects.PO.POLandedCostDocS.Released : Edm.Boolean "Released"
PX.Objects.PO.POLandedCostDocS.Hold : Edm.Boolean "Hold"
PX.Objects.PO.POLandedCostDocS.Status : Edm.String "Status"
PX.Objects.PO.POLandedCostDocS.IsTaxValid : Edm.Boolean "Tax Is Up to Date"
PX.Objects.PO.POLandedCostDocS.NonTaxable : Edm.Boolean "Non-Taxable"
PX.Objects.PO.POLandedCostDocS.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.POLandedCostDocS.FinPeriodID : Edm.String "Post Period"
PX.Objects.PO.POLandedCostDocS.TranPeriodID : Edm.String "Transaction Period"
PX.Objects.PO.POLandedCostDocS.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POLandedCostDocS.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.PO.POLandedCostDocS.TaxTotal : Edm.Decimal "Tax Total"
PX.Objects.PO.POLandedCostDocS.LineCntr : Edm.Int32
PX.Objects.PO.POLandedCostDocS.CuryID : Edm.String "Currency"
PX.Objects.PO.POLandedCostDocS.CuryInfoID : Edm.Int64
PX.Objects.PO.POLandedCostDocS.CreateBill : Edm.Boolean "Create Bill"
PX.Objects.PO.POLandedCostDocS.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.PO.POLandedCostDocS.CuryLineTotal : Edm.Decimal "Detail Total"
PX.Objects.PO.POLandedCostDocS.LineTotal : Edm.Decimal
PX.Objects.PO.POLandedCostDocS.CuryOrigDocAmt : Edm.Decimal "Amount"
PX.Objects.PO.POLandedCostDocS.OrigDocAmt : Edm.Decimal
PX.Objects.PO.POLandedCostDocS.CuryControlTotal : Edm.Decimal "Control Total"
PX.Objects.PO.POLandedCostDocS.ControlTotal : Edm.Decimal
PX.Objects.PO.POLandedCostDocS.CuryDocBal : Edm.Decimal "Balance"
PX.Objects.PO.POLandedCostDocS.DocBal : Edm.Decimal
PX.Objects.PO.POLandedCostDocS.TermsID : Edm.String "Terms"
PX.Objects.PO.POLandedCostDocS.BillDate : Edm.DateTimeOffset "Bill Date"
PX.Objects.PO.POLandedCostDocS.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.PO.POLandedCostDocS.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.PO.POLandedCostDocS.CuryDiscAmt : Edm.Decimal "Cash Discount"
PX.Objects.PO.POLandedCostDocS.DiscAmt : Edm.Decimal
PX.Objects.PO.POLandedCostDocS.TaxZoneID : Edm.String "Vendor Tax Zone"
PX.Objects.PO.POLandedCostDocS.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PO.POLandedCostDocS.OwnerID : Edm.Int32 "Owner"
PX.Objects.PO.POLandedCostDocS.APDocCreated : Edm.Boolean
PX.Objects.PO.POLandedCostDocS.INDocCreated : Edm.Boolean
PX.Objects.PO.POLandedCostDocS.CuryVatExemptTotal : Edm.Decimal "VAT Exempt Total"
PX.Objects.PO.POLandedCostDocS.VatExemptTotal : Edm.Decimal
PX.Objects.PO.POLandedCostDocS.CuryVatTaxableTotal : Edm.Decimal "VAT Taxable Total"
PX.Objects.PO.POLandedCostDocS.VatTaxableTotal : Edm.Decimal
PX.Objects.PO.POLandedCostDocS.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POLandedCostDocS.CreatedByScreenID : Edm.String
PX.Objects.PO.POLandedCostDocS.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PO.POLandedCostDocS.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POLandedCostDocS.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POLandedCostDocS.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PO.POLandedCostDocS.tstamp : Edm.Binary
PX.Objects.PO.POLandedCostDocS.VendorByPayToVendorID -> PX.Objects.AP.Vendor
PX.Objects.PO.POLandedCostDocS.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POLandedCostDocS.BAccountByPayToVendorID -> PX.Objects.CR.BAccount
PX.Objects.PO.POLandedCostDocS.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PO.POLandedCostDocS.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PO.POLandedCostDocS.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POLandedCostDocS.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POLandedCostDocS.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PO.POLandedCostDocS.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PO.POLandedCostDocS.POLandedCostDocByRefNbr -> PX.Objects.PO.POLandedCostDoc (RefNbr=RefNbr)
PX.Objects.PO.POLandedCostDocS.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.PO.POLandedCostDocS.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POLandedCostDocS.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POLandedCostDocS.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)

# PX.Objects.PO.POLandedCostReceipt (EntityType)

Label: "Landed Costs Receipt"
Key: LCDocType, LCRefNbr, POReceiptNbr, POReceiptType
Entity sets: PX_Objects_PO_POLandedCostReceipt, LandedCostsReceipt1, POLandedCostReceipt
Non-filterable, non-selectable: LineCntr

PX.Objects.PO.POLandedCostReceipt.LCDocType : Edm.String [key] "Landed Cost Type"
PX.Objects.PO.POLandedCostReceipt.LCRefNbr : Edm.String [key] "Landed Cost Nbr."
PX.Objects.PO.POLandedCostReceipt.POReceiptType : Edm.String [key] "PO Receipt Type"
PX.Objects.PO.POLandedCostReceipt.POReceiptNbr : Edm.String [key] "PO Receipt Nbr."
PX.Objects.PO.POLandedCostReceipt.LineCntr : Edm.Int32
PX.Objects.PO.POLandedCostReceipt.tstamp : Edm.Binary
PX.Objects.PO.POLandedCostReceipt.POLandedCostDocByLCRefNbr -> PX.Objects.PO.POLandedCostDoc (LCDocType=DocType, LCRefNbr=RefNbr)
PX.Objects.PO.POLandedCostReceipt.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.PO.POLandedCostReceipt.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.PO.POLandedCostReceipt.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)

# PX.Objects.PO.POLandedCostReceiptLine (EntityType)

Label: "Landed Costs Receipt Line"
Key: DocType, LineNbr, RefNbr
Entity sets: PX_Objects_PO_POLandedCostReceiptLine, LandedCostsReceiptLine, POLandedCostReceiptLine
Non-filterable, non-selectable: POReceiptBaseCuryID

PX.Objects.PO.POLandedCostReceiptLine.BranchID : Edm.Int32 "Branch"
PX.Objects.PO.POLandedCostReceiptLine.DocType : Edm.String [key] "Doc. Type"
PX.Objects.PO.POLandedCostReceiptLine.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POLandedCostReceiptLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POLandedCostReceiptLine.SortOrder : Edm.Int32 "Line Order"
PX.Objects.PO.POLandedCostReceiptLine.IsStockItem : Edm.Boolean
PX.Objects.PO.POLandedCostReceiptLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POLandedCostReceiptLine.TranDesc : Edm.String "Line Description"
PX.Objects.PO.POLandedCostReceiptLine.CuryInfoID : Edm.Int64
PX.Objects.PO.POLandedCostReceiptLine.POReceiptType : Edm.String "PO Receipt Type"
PX.Objects.PO.POLandedCostReceiptLine.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.PO.POLandedCostReceiptLine.POReceiptLineNbr : Edm.Int32 "PO Receipt Line Nbr."
PX.Objects.PO.POLandedCostReceiptLine.POReceiptBaseCuryID : Edm.String "Currency"
PX.Objects.PO.POLandedCostReceiptLine.UOM : Edm.String "UOM"
PX.Objects.PO.POLandedCostReceiptLine.ReceiptQty : Edm.Decimal [required] "Receipt Qty."
PX.Objects.PO.POLandedCostReceiptLine.BaseReceiptQty : Edm.Decimal [required]
PX.Objects.PO.POLandedCostReceiptLine.UnitWeight : Edm.Decimal
PX.Objects.PO.POLandedCostReceiptLine.UnitVolume : Edm.Decimal
PX.Objects.PO.POLandedCostReceiptLine.ExtWeight : Edm.Decimal [required] "Weight"
PX.Objects.PO.POLandedCostReceiptLine.ExtVolume : Edm.Decimal [required] "Volume"
PX.Objects.PO.POLandedCostReceiptLine.LineAmt : Edm.Decimal [required] "Ext. Cost"
PX.Objects.PO.POLandedCostReceiptLine.CuryAllocatedLCAmt : Edm.Decimal [required] "Allocated Amount"
PX.Objects.PO.POLandedCostReceiptLine.AllocatedLCAmt : Edm.Decimal [required]
PX.Objects.PO.POLandedCostReceiptLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POLandedCostReceiptLine.CreatedByScreenID : Edm.String
PX.Objects.PO.POLandedCostReceiptLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLandedCostReceiptLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POLandedCostReceiptLine.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POLandedCostReceiptLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLandedCostReceiptLine.tstamp : Edm.Binary
PX.Objects.PO.POLandedCostReceiptLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POLandedCostReceiptLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.PO.POLandedCostReceiptLine.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLandedCostReceiptLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POLandedCostReceiptLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POLandedCostReceiptLine.POLandedCostDocByRefNbr -> PX.Objects.PO.POLandedCostDoc (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PO.POLandedCostReceiptLine.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.PO.POLandedCostReceiptLine.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.PO.POLandedCostReceiptLine.POReceiptLineByPOReceiptLineNbr -> PX.Objects.PO.POReceiptLine (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr, POReceiptLineNbr=LineNbr)
PX.Objects.PO.POLandedCostReceiptLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POLandedCostReceiptLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POLandedCostReceiptLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PO.POLandedCostReceiptLine.POLandedCostReceiptByPOReceiptNbr -> PX.Objects.PO.POLandedCostReceipt (DocType=LCDocType, RefNbr=LCRefNbr, POReceiptType=POReceiptType, POReceiptNbr=POReceiptNbr)

# PX.Objects.PO.POLandedCostTax (EntityType)

Label: "Landed Costs Tax Detail"
Key: DocType, LineNbr, RefNbr, TaxID
Entity sets: PX_Objects_PO_POLandedCostTax, LandedCostsTaxDetail, POLandedCostTax
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt

PX.Objects.PO.POLandedCostTax.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.PO.POLandedCostTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.PO.POLandedCostTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PO.POLandedCostTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PO.POLandedCostTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POLandedCostTax.CreatedByScreenID : Edm.String
PX.Objects.PO.POLandedCostTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLandedCostTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POLandedCostTax.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POLandedCostTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLandedCostTax.DocType : Edm.String [key] "Doc. Type"
PX.Objects.PO.POLandedCostTax.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POLandedCostTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POLandedCostTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PO.POLandedCostTax.CuryInfoID : Edm.Int64
PX.Objects.PO.POLandedCostTax.CuryTaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PO.POLandedCostTax.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PO.POLandedCostTax.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PO.POLandedCostTax.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PO.POLandedCostTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLandedCostTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POLandedCostTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POLandedCostTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PO.POLandedCostTax.POLandedCostDetailByLineNbr -> PX.Objects.PO.POLandedCostDetail (DocType=DocType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.PO.POLandedCostTax.POLandedCostDocByRefNbr -> PX.Objects.PO.POLandedCostDoc (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PO.POLandedCostTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PO.POLandedCostTaxTran (EntityType)

Label: "Landed Costs Tax"
Key: DocType, RecordID, RefNbr, TaxID
Entity sets: PX_Objects_PO_POLandedCostTaxTran, LandedCostsTax, POLandedCostTaxTran
Non-filterable, non-selectable: NonDeductibleTaxRate

PX.Objects.PO.POLandedCostTaxTran.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.PO.POLandedCostTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.PO.POLandedCostTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PO.POLandedCostTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POLandedCostTaxTran.CreatedByScreenID : Edm.String
PX.Objects.PO.POLandedCostTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLandedCostTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POLandedCostTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POLandedCostTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLandedCostTaxTran.DocType : Edm.String [key] "Document Type"
PX.Objects.PO.POLandedCostTaxTran.RefNbr : Edm.String [key] "Document Nbr."
PX.Objects.PO.POLandedCostTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PO.POLandedCostTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.PO.POLandedCostTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.PO.POLandedCostTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.PO.POLandedCostTaxTran.CuryInfoID : Edm.Int64
PX.Objects.PO.POLandedCostTaxTran.CuryTaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PO.POLandedCostTaxTran.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PO.POLandedCostTaxTran.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PO.POLandedCostTaxTran.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PO.POLandedCostTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PO.POLandedCostTaxTran.TaxZoneID : Edm.String
PX.Objects.PO.POLandedCostTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.PO.POLandedCostTaxTran.tstamp : Edm.Binary
PX.Objects.PO.POLandedCostTaxTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLandedCostTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POLandedCostTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POLandedCostTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PO.POLandedCostTaxTran.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PO.POLandedCostTaxTran.POLandedCostDocByRefNbr -> PX.Objects.PO.POLandedCostDoc (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PO.POLandedCostTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PO.POLine (EntityType)

Label: "PO Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PO_POLine, POLine1
Non-filterable, non-selectable: ClearPlanID, VendorLocationID, ShipToBAccountID, ShipToLocationID, CalculateDiscountsOnImport, NoteText, ItemRequiresTerms, SOOrderStatus, SOOrderType, SOOrderNbr, SOLineNbr, LeftToReceiveQty, LeftToReceiveBaseQty, NonOrderedQty, DisplayReqPrepaidQty, IsKit, OrderedQtyAltered, OverridenUOM, OverridenQty, BaseOverridenQty, CuryReceivedCost, ViewDemandEnabled

PX.Objects.PO.POLine.BranchID : Edm.Int32 "Branch"
PX.Objects.PO.POLine.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.POLine.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POLine.DropshipReceiptProcessing : Edm.String "Drop-Ship Receipt Processing"
PX.Objects.PO.POLine.DropshipExpenseRecording : Edm.String "Record Drop-Ship Expenses"
PX.Objects.PO.POLine.SortOrder : Edm.Int32 "Line Order"
PX.Objects.PO.POLine.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.PO.POLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POLine.LineType : Edm.String "Line Type"
PX.Objects.PO.POLine.ProcessNonStockAsServiceViaPR : Edm.Boolean "Process as Service via Purchase Receipt"
PX.Objects.PO.POLine.AccrueCost : Edm.Boolean "Accrue Cost"
PX.Objects.PO.POLine.PlanID : Edm.Int64 "Plan ID"
PX.Objects.PO.POLine.ClearPlanID : Edm.Boolean
PX.Objects.PO.POLine.POType : Edm.String "Blanket PO Type"
PX.Objects.PO.POLine.PONbr : Edm.String "Blanket PO Nbr."
PX.Objects.PO.POLine.POLineNbr : Edm.Int32 "Blanket PO Line Nbr."
PX.Objects.PO.POLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POLine.VendorLocationID : Edm.Int32
PX.Objects.PO.POLine.ShipToBAccountID : Edm.Int32
PX.Objects.PO.POLine.ShipToLocationID : Edm.Int32
PX.Objects.PO.POLine.OrderDate : Edm.DateTimeOffset
PX.Objects.PO.POLine.LotSerialNbr : Edm.String "Lot Serial Number"
PX.Objects.PO.POLine.BLType : Edm.String
PX.Objects.PO.POLine.BLOrderNbr : Edm.String
PX.Objects.PO.POLine.BLLineNbr : Edm.Int32
PX.Objects.PO.POLine.RQReqNbr : Edm.String
PX.Objects.PO.POLine.RQReqLineNbr : Edm.Int32
PX.Objects.PO.POLine.MaterialListNoteID : Edm.Guid
PX.Objects.PO.POLine.MaterialListLineNbr : Edm.Int32
PX.Objects.PO.POLine.UOM : Edm.String "UOM"
PX.Objects.PO.POLine.OrderQty : Edm.Decimal [required] "Order Qty."
PX.Objects.PO.POLine.OrigOrderQty : Edm.Decimal
PX.Objects.PO.POLine.BaseOrderQty : Edm.Decimal [required] "Base Order Qty."
PX.Objects.PO.POLine.OrderedQty : Edm.Decimal [required] "Qty. On Orders"
PX.Objects.PO.POLine.BaseOrderedQty : Edm.Decimal [required]
PX.Objects.PO.POLine.ReceivedQty : Edm.Decimal [required] "Qty. On Receipts"
PX.Objects.PO.POLine.BaseReceivedQty : Edm.Decimal [required] "Base Received Qty."
PX.Objects.PO.POLine.CuryInfoID : Edm.Int64
PX.Objects.PO.POLine.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.PO.POLine.UnitCost : Edm.Decimal
PX.Objects.PO.POLine.CalculateDiscountsOnImport : Edm.Boolean "Calculate automatic discounts on import"
PX.Objects.PO.POLine.DiscPct : Edm.Decimal [required] "Discount Percent"
PX.Objects.PO.POLine.CuryDiscAmt : Edm.Decimal [required] "Discount Amount"
PX.Objects.PO.POLine.DiscAmt : Edm.Decimal [required]
PX.Objects.PO.POLine.ManualPrice : Edm.Boolean "Manual Cost"
PX.Objects.PO.POLine.ManualDisc : Edm.Boolean "Manual Discount"
PX.Objects.PO.POLine.CuryLineAmt : Edm.Decimal [required] "Ext. Cost"
PX.Objects.PO.POLine.LineAmt : Edm.Decimal [required]
PX.Objects.PO.POLine.CuryDiscCost : Edm.Decimal "Disc. Unit Cost"
PX.Objects.PO.POLine.DiscCost : Edm.Decimal
PX.Objects.PO.POLine.RetainagePct : Edm.Decimal [required] "Retainage Percent"
PX.Objects.PO.POLine.CuryRetainageAmt : Edm.Decimal [required] "Retainage Amount"
PX.Objects.PO.POLine.RetainageAmt : Edm.Decimal [required]
PX.Objects.PO.POLine.CuryExtCost : Edm.Decimal [required] "Amount"
PX.Objects.PO.POLine.ExtCost : Edm.Decimal [required] "Amount"
PX.Objects.PO.POLine.OrigExtCost : Edm.Decimal
PX.Objects.PO.POLine.GroupDiscountRate : Edm.Decimal [required]
PX.Objects.PO.POLine.DocumentDiscountRate : Edm.Decimal [required]
PX.Objects.PO.POLine.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PO.POLine.TaxID : Edm.String "Tax ID"
PX.Objects.PO.POLine.AlternateID : Edm.String "Alternate ID"
PX.Objects.PO.POLine.TranDesc : Edm.String "Line Description"
PX.Objects.PO.POLine.UnitWeight : Edm.Decimal [required] "Unit Weight"
PX.Objects.PO.POLine.UnitVolume : Edm.Decimal [required] "Unit Volume"
PX.Objects.PO.POLine.ExtWeight : Edm.Decimal [required] "Weight"
PX.Objects.PO.POLine.ExtVolume : Edm.Decimal [required] "Volume"
PX.Objects.PO.POLine.CommitmentID : Edm.Guid
PX.Objects.PO.POLine.ReasonCode : Edm.String
PX.Objects.PO.POLine.NoteID : Edm.Guid
PX.Objects.PO.POLine.NoteText : Edm.String "Note Text"
PX.Objects.PO.POLine.RcptQtyMin : Edm.Decimal "Min. Receipt (%)"
PX.Objects.PO.POLine.RcptQtyMax : Edm.Decimal "Max. Receipt (%)"
PX.Objects.PO.POLine.RcptQtyThreshold : Edm.Decimal "Complete On (%)"
PX.Objects.PO.POLine.RcptQtyAction : Edm.String "Receipt Action"
PX.Objects.PO.POLine.ReceiptStatus : Edm.String
PX.Objects.PO.POLine.CuryBLOrderedCost : Edm.Decimal [required] "Received Cost"
PX.Objects.PO.POLine.BLOrderedCost : Edm.Decimal [required]
PX.Objects.PO.POLine.DRTermStartDate : Edm.DateTimeOffset "Term Start Date"
PX.Objects.PO.POLine.DRTermEndDate : Edm.DateTimeOffset "Term End Date"
PX.Objects.PO.POLine.ItemRequiresTerms : Edm.Boolean
PX.Objects.PO.POLine.SOOrderStatus : Edm.String "Sales Order Status"
PX.Objects.PO.POLine.SOOrderType : Edm.String
PX.Objects.PO.POLine.SOOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.PO.POLine.SOLineNbr : Edm.Int32 "Sales Order Line Nbr."
PX.Objects.PO.POLine.CostCenterID : Edm.Int32 [required]
PX.Objects.PO.POLine.tstamp : Edm.Binary
PX.Objects.PO.POLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POLine.CreatedByScreenID : Edm.String
PX.Objects.PO.POLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POLine.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLine.CompletedQty : Edm.Decimal [required] "Received Qty."
PX.Objects.PO.POLine.BaseCompletedQty : Edm.Decimal [required]
PX.Objects.PO.POLine.BilledQty : Edm.Decimal [required] "Billed Qty."
PX.Objects.PO.POLine.BaseBilledQty : Edm.Decimal [required]
PX.Objects.PO.POLine.CuryBilledAmt : Edm.Decimal [required] "Billed Amount"
PX.Objects.PO.POLine.BilledAmt : Edm.Decimal [required]
PX.Objects.PO.POLine.OpenQty : Edm.Decimal [required] "Open Qty."
PX.Objects.PO.POLine.BaseOpenQty : Edm.Decimal [required]
PX.Objects.PO.POLine.UnbilledQty : Edm.Decimal [required] "Unbilled Qty."
PX.Objects.PO.POLine.BaseUnbilledQty : Edm.Decimal [required]
PX.Objects.PO.POLine.CuryUnbilledAmt : Edm.Decimal [required] "Unbilled Amount"
PX.Objects.PO.POLine.UnbilledAmt : Edm.Decimal [required]
PX.Objects.PO.POLine.LeftToReceiveQty : Edm.Decimal "Open Qty."
PX.Objects.PO.POLine.LeftToReceiveBaseQty : Edm.Decimal
PX.Objects.PO.POLine.NonOrderedQty : Edm.Decimal "Blanket Open Qty."
PX.Objects.PO.POLine.ReqPrepaidQty : Edm.Decimal [required]
PX.Objects.PO.POLine.BaseReqPrepaidQty : Edm.Decimal [required]
PX.Objects.PO.POLine.DisplayReqPrepaidQty : Edm.Decimal "Prepaid Qty."
PX.Objects.PO.POLine.CuryReqPrepaidAmt : Edm.Decimal [required] "Prepaid Amount"
PX.Objects.PO.POLine.ReqPrepaidAmt : Edm.Decimal [required]
PX.Objects.PO.POLine.RequestedDate : Edm.DateTimeOffset "Requested"
PX.Objects.PO.POLine.PromisedDate : Edm.DateTimeOffset "Promised"
PX.Objects.PO.POLine.Cancelled : Edm.Boolean [required] "Cancelled"
PX.Objects.PO.POLine.CompletePOLine : Edm.String "Close PO Line"
PX.Objects.PO.POLine.Completed : Edm.Boolean [required] "Completed"
PX.Objects.PO.POLine.Closed : Edm.Boolean [required] "Closed"
PX.Objects.PO.POLine.POAccrualType : Edm.String "Billing Based On"
PX.Objects.PO.POLine.OrderNoteID : Edm.Guid
PX.Objects.PO.POLine.AllowComplete : Edm.Boolean [required] "Allow Complete"
PX.Objects.PO.POLine.IsKit : Edm.Boolean "Kit"
PX.Objects.PO.POLine.DiscountID : Edm.String "Discount Code"
PX.Objects.PO.POLine.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.PO.POLine.OrderedQtyAltered : Edm.Boolean
PX.Objects.PO.POLine.OverridenUOM : Edm.String
PX.Objects.PO.POLine.OverridenQty : Edm.Decimal
PX.Objects.PO.POLine.BaseOverridenQty : Edm.Decimal
PX.Objects.PO.POLine.CuryReceivedCost : Edm.Decimal
PX.Objects.PO.POLine.HasInclusiveTaxes : Edm.Boolean [required]
PX.Objects.PO.POLine.AllowEditUnitCostInPR : Edm.Boolean [required] "Editable Unit Cost in Receipt"
PX.Objects.PO.POLine.ViewDemandEnabled : Edm.Boolean
PX.Objects.PO.POLine.SODeleted : Edm.Boolean [required]
PX.Objects.PO.POLine.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PO.POLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.POLine.RQRequisitionLineByRQReqLineNbr -> PX.Objects.RQ.RQRequisitionLine (RQReqNbr=ReqNbr, RQReqLineNbr=LineNbr)
PX.Objects.PO.POLine.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POLine.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.PO.POLine.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PO.POLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POLine.VendorDiscountSequenceByDiscountSequenceID -> PX.Objects.AP.VendorDiscountSequence (VendorID=VendorID, DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.PO.POLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POLine.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.PO.POLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.PO.POLine.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POLine.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PO.POLine.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PO.POLine.RQRequisitionByRQReqNbr -> PX.Objects.RQ.RQRequisition (RQReqNbr=ReqNbr)
PX.Objects.PO.POLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PO.POLine.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.PO.POLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PO.POLine.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POLine.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POLine.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POLine.APDiscountByVendorID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID, VendorID=BAccountID)
PX.Objects.PO.POLine.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.PO.POLine.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.PO.POLine.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.PO.POLine.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POLine.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POLine.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PO.POLine.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PO.POLine.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PO.POLine.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.PO.POLine.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PO.POLine.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.PO.POLine.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PO.POLine.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.PO.POLine.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PO.POLine.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PO.POLine.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.PO.POLineBillingRevision (EntityType)

Label: "PO Line Billing Revision"
Key: APDocType, APRefNbr, OrderLineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PO_POLineBillingRevision, POLineBillingRevision

PX.Objects.PO.POLineBillingRevision.APDocType : Edm.String [key]
PX.Objects.PO.POLineBillingRevision.APRefNbr : Edm.String [key]
PX.Objects.PO.POLineBillingRevision.OrderType : Edm.String [key]
PX.Objects.PO.POLineBillingRevision.OrderNbr : Edm.String [key]
PX.Objects.PO.POLineBillingRevision.OrderLineNbr : Edm.Int32 [key]
PX.Objects.PO.POLineBillingRevision.LineType : Edm.String
PX.Objects.PO.POLineBillingRevision.CuryID : Edm.String
PX.Objects.PO.POLineBillingRevision.InventoryID : Edm.Int32
PX.Objects.PO.POLineBillingRevision.UOM : Edm.String
PX.Objects.PO.POLineBillingRevision.OrderQty : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.BaseOrderQty : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.ReceivedQty : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.BaseReceivedQty : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.RcptQtyMax : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.UnbilledQty : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.BaseUnbilledQty : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.CuryUnbilledAmt : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.UnbilledAmt : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.CuryUnitCost : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.UnitCost : Edm.Decimal
PX.Objects.PO.POLineBillingRevision.tstamp : Edm.Binary
PX.Objects.PO.POLineBillingRevision.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POLineBillingRevision.CreatedByScreenID : Edm.String
PX.Objects.PO.POLineBillingRevision.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLineBillingRevision.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Objects.PO.POLineR (EntityType)

Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PO_POLineR

PX.Objects.PO.POLineR.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.POLineR.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POLineR.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POLineR.SortOrder : Edm.Int32
PX.Objects.PO.POLineR.LineType : Edm.String "Line Type"
PX.Objects.PO.POLineR.OrderedQty : Edm.Decimal
PX.Objects.PO.POLineR.BaseOrderedQty : Edm.Decimal
PX.Objects.PO.POLineR.ReceivedQty : Edm.Decimal "Received Qty."
PX.Objects.PO.POLineR.BaseReceivedQty : Edm.Decimal "Base Received Qty."
PX.Objects.PO.POLineR.BilledQty : Edm.Decimal
PX.Objects.PO.POLineR.CuryInfoID : Edm.Int64
PX.Objects.PO.POLineR.CuryBLOrderedCost : Edm.Decimal
PX.Objects.PO.POLineR.BLOrderedCost : Edm.Decimal
PX.Objects.PO.POLineR.UOM : Edm.String "UOM"
PX.Objects.PO.POLineR.Completed : Edm.Boolean
PX.Objects.PO.POLineR.Cancelled : Edm.Boolean
PX.Objects.PO.POLineR.Closed : Edm.Boolean
PX.Objects.PO.POLineR.OrderQty : Edm.Decimal
PX.Objects.PO.POLineR.BaseOrderQty : Edm.Decimal
PX.Objects.PO.POLineR.OpenQty : Edm.Decimal "Open Qty."
PX.Objects.PO.POLineR.BaseOpenQty : Edm.Decimal
PX.Objects.PO.POLineR.ExtCost : Edm.Decimal
PX.Objects.PO.POLineR.BilledAmt : Edm.Decimal
PX.Objects.PO.POLineR.RetainageAmt : Edm.Decimal
PX.Objects.PO.POLineR.InventoryID : Edm.Int32
PX.Objects.PO.POLineR.POType : Edm.String
PX.Objects.PO.POLineR.PONbr : Edm.String
PX.Objects.PO.POLineR.POLineNbr : Edm.Int32
PX.Objects.PO.POLineR.tstamp : Edm.Binary
PX.Objects.PO.POLineR.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POLineR.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POLineR.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POLineR.AllowComplete : Edm.Boolean "Allow Complete"
PX.Objects.PO.POLineR.CompletePOLine : Edm.String
PX.Objects.PO.POLineR.RcptQtyThreshold : Edm.Decimal
PX.Objects.PO.POLineR.DRTermStartDate : Edm.DateTimeOffset "Term Start Date"
PX.Objects.PO.POLineR.DRTermEndDate : Edm.DateTimeOffset "Term End Date"
PX.Objects.PO.POLineR.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POLineR.POLineRByPOLineNbr -> PX.Objects.PO.POLineR (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.PO.POLineR.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POLineR.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLineR.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.PO.POLineR.POLineRCollection -> Collection(PX.Objects.PO.POLineR)
PX.Objects.PO.POLineR.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.PO.POLineR.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POLineR.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POLineR.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PO.POLineR.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PO.POLineR.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PO.POLineR.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PO.POLineR.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.PO.POLineR.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PO.POLineR.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.PO.POLineR.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PO.POLineR.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PO.POLineR.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.PO.POLineRS (EntityType)

Label: "PO Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PO_POLineRS, POLine2, POLineRS

PX.Objects.PO.POLineRS.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.POLineRS.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POLineRS.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POLineRS.SortOrder : Edm.Int32 "Line Order"
PX.Objects.PO.POLineRS.IsStockItem : Edm.Boolean
PX.Objects.PO.POLineRS.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POLineRS.AccrueCost : Edm.Boolean
PX.Objects.PO.POLineRS.LineType : Edm.String "Line Type"
PX.Objects.PO.POLineRS.Status : Edm.String "Status"
PX.Objects.PO.POLineRS.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POLineRS.TaxZoneID : Edm.String
PX.Objects.PO.POLineRS.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.PO.POLineRS.LotSerialNbr : Edm.String "Lot Serial Number"
PX.Objects.PO.POLineRS.UOM : Edm.String "UOM"
PX.Objects.PO.POLineRS.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.PO.POLineRS.BaseOrderQty : Edm.Decimal "Base Order Qty."
PX.Objects.PO.POLineRS.CuryID : Edm.String "Currency"
PX.Objects.PO.POLineRS.CuryInfoID : Edm.Int64
PX.Objects.PO.POLineRS.CuryUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.PO.POLineRS.UnitCost : Edm.Decimal
PX.Objects.PO.POLineRS.DiscPct : Edm.Decimal
PX.Objects.PO.POLineRS.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.PO.POLineRS.DiscAmt : Edm.Decimal
PX.Objects.PO.POLineRS.CuryLineAmt : Edm.Decimal "Ext. Cost"
PX.Objects.PO.POLineRS.LineAmt : Edm.Decimal
PX.Objects.PO.POLineRS.RetainagePct : Edm.Decimal
PX.Objects.PO.POLineRS.RcptQtyThreshold : Edm.Decimal
PX.Objects.PO.POLineRS.CuryRetainageAmt : Edm.Decimal
PX.Objects.PO.POLineRS.RetainageAmt : Edm.Decimal
PX.Objects.PO.POLineRS.CuryExtCost : Edm.Decimal "Amount"
PX.Objects.PO.POLineRS.ExtCost : Edm.Decimal "Amount"
PX.Objects.PO.POLineRS.GroupDiscountRate : Edm.Decimal
PX.Objects.PO.POLineRS.DocumentDiscountRate : Edm.Decimal
PX.Objects.PO.POLineRS.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PO.POLineRS.TaxID : Edm.String "Tax ID"
PX.Objects.PO.POLineRS.TranDesc : Edm.String "Line Description"
PX.Objects.PO.POLineRS.Cancelled : Edm.Boolean "Cancelled"
PX.Objects.PO.POLineRS.CompletePOLine : Edm.String
PX.Objects.PO.POLineRS.Closed : Edm.Boolean "Closed"
PX.Objects.PO.POLineRS.Billed : Edm.Boolean
PX.Objects.PO.POLineRS.POAccrualType : Edm.String
PX.Objects.PO.POLineRS.OrderNoteID : Edm.Guid
PX.Objects.PO.POLineRS.DiscountID : Edm.String "Discount Code"
PX.Objects.PO.POLineRS.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.PO.POLineRS.RefNoteID : Edm.Guid
PX.Objects.PO.POLineRS.BilledUOM : Edm.String
PX.Objects.PO.POLineRS.BilledQty : Edm.Decimal "Billed Qty."
PX.Objects.PO.POLineRS.BaseBilledQty : Edm.Decimal
PX.Objects.PO.POLineRS.CuryBilledAmt : Edm.Decimal "Billed Amount"
PX.Objects.PO.POLineRS.BilledAmt : Edm.Decimal
PX.Objects.PO.POLineRS.CuryBilledCost : Edm.Decimal
PX.Objects.PO.POLineRS.BilledCost : Edm.Decimal
PX.Objects.PO.POLineRS.CuryBilledDiscAmt : Edm.Decimal
PX.Objects.PO.POLineRS.BilledDiscAmt : Edm.Decimal
PX.Objects.PO.POLineRS.ReceivedUOM : Edm.String
PX.Objects.PO.POLineRS.ReceivedQty : Edm.Decimal
PX.Objects.PO.POLineRS.BaseReceivedQty : Edm.Decimal
PX.Objects.PO.POLineRS.ReceivedCost : Edm.Decimal
PX.Objects.PO.POLineRS.PPVAmt : Edm.Decimal
PX.Objects.PO.POLineRS.CuryOrderBilledAmt : Edm.Decimal
PX.Objects.PO.POLineRS.OrderBilledAmt : Edm.Decimal
PX.Objects.PO.POLineRS.OrderBilledQty : Edm.Decimal
PX.Objects.PO.POLineRS.BaseOrderBilledQty : Edm.Decimal
PX.Objects.PO.POLineRS.UnbilledQty : Edm.Decimal "Unbilled Qty."
PX.Objects.PO.POLineRS.BaseUnbilledQty : Edm.Decimal
PX.Objects.PO.POLineRS.CuryUnbilledAmt : Edm.Decimal "Unbilled Amount"
PX.Objects.PO.POLineRS.UnbilledAmt : Edm.Decimal
PX.Objects.PO.POLineRS.ReqPrepaidQty : Edm.Decimal
PX.Objects.PO.POLineRS.CuryReqPrepaidAmt : Edm.Decimal
PX.Objects.PO.POLineRS.ReqPrepaidAmt : Edm.Decimal
PX.Objects.PO.POLineRS.DRTermStartDate : Edm.DateTimeOffset
PX.Objects.PO.POLineRS.DRTermEndDate : Edm.DateTimeOffset
PX.Objects.PO.POLineRS.DropshipExpenseRecording : Edm.String
PX.Objects.PO.POLineRS.CostCenterID : Edm.Int32
PX.Objects.PO.POLineRS.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PO.POLineRS.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.POLineRS.VendorByPayToVendorID -> PX.Objects.AP.Vendor
PX.Objects.PO.POLineRS.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POLineRS.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.PO.POLineRS.VendorDiscountSequenceByDiscountSequenceID -> PX.Objects.AP.VendorDiscountSequence (VendorID=VendorID, DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.PO.POLineRS.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POLineRS.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PO.POLineRS.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLineRS.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PO.POLineRS.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PO.POLineRS.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PO.POLineRS.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PO.POLineRS.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POLineRS.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POLineRS.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POLineRS.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POLineRS.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POLineRS.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POLineRS.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POLineRS.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POLineRS.APDiscountByVendorID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID, VendorID=BAccountID)
PX.Objects.PO.POLineRS.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.PO.POLineRS.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.PO.POLineRS.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POLineRS.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POLineRS.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PO.POLineRS.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PO.POLineRS.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PO.POLineRS.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PO.POLineRS.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.PO.POLineRS.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PO.POLineRS.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.PO.POLineRS.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PO.POLineRS.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PO.POLineRS.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.PO.POLineS (EntityType)

Label: "PO Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PO_POLineS, POLine3, POLineS

PX.Objects.PO.POLineS.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.POLineS.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POLineS.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POLineS.SortOrder : Edm.Int32 "Line Order"
PX.Objects.PO.POLineS.IsStockItem : Edm.Boolean
PX.Objects.PO.POLineS.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POLineS.AccrueCost : Edm.Boolean
PX.Objects.PO.POLineS.LineType : Edm.String "Line Type"
PX.Objects.PO.POLineS.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POLineS.OrderDate : Edm.DateTimeOffset
PX.Objects.PO.POLineS.LotSerialNbr : Edm.String "Lot Serial Number"
PX.Objects.PO.POLineS.UOM : Edm.String "UOM"
PX.Objects.PO.POLineS.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.PO.POLineS.BaseOrderQty : Edm.Decimal "Base Order Qty."
PX.Objects.PO.POLineS.CuryInfoID : Edm.Int64
PX.Objects.PO.POLineS.CuryUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.PO.POLineS.UnitCost : Edm.Decimal
PX.Objects.PO.POLineS.DiscPct : Edm.Decimal
PX.Objects.PO.POLineS.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.PO.POLineS.DiscAmt : Edm.Decimal
PX.Objects.PO.POLineS.CuryLineAmt : Edm.Decimal "Ext. Cost"
PX.Objects.PO.POLineS.LineAmt : Edm.Decimal
PX.Objects.PO.POLineS.RetainagePct : Edm.Decimal
PX.Objects.PO.POLineS.CuryRetainageAmt : Edm.Decimal
PX.Objects.PO.POLineS.RetainageAmt : Edm.Decimal
PX.Objects.PO.POLineS.CuryExtCost : Edm.Decimal "Amount"
PX.Objects.PO.POLineS.ExtCost : Edm.Decimal "Amount"
PX.Objects.PO.POLineS.GroupDiscountRate : Edm.Decimal
PX.Objects.PO.POLineS.DocumentDiscountRate : Edm.Decimal
PX.Objects.PO.POLineS.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PO.POLineS.TaxID : Edm.String "Tax ID"
PX.Objects.PO.POLineS.TranDesc : Edm.String "Line Description"
PX.Objects.PO.POLineS.Cancelled : Edm.Boolean "Cancelled"
PX.Objects.PO.POLineS.CompletePOLine : Edm.String
PX.Objects.PO.POLineS.Closed : Edm.Boolean "Closed"
PX.Objects.PO.POLineS.Billed : Edm.Boolean
PX.Objects.PO.POLineS.POAccrualType : Edm.String
PX.Objects.PO.POLineS.OrderNoteID : Edm.Guid
PX.Objects.PO.POLineS.DiscountID : Edm.String "Discount Code"
PX.Objects.PO.POLineS.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.PO.POLineS.RefNoteID : Edm.Guid
PX.Objects.PO.POLineS.BilledUOM : Edm.String
PX.Objects.PO.POLineS.BilledQty : Edm.Decimal
PX.Objects.PO.POLineS.BaseBilledQty : Edm.Decimal
PX.Objects.PO.POLineS.CuryBilledAmt : Edm.Decimal
PX.Objects.PO.POLineS.BilledAmt : Edm.Decimal
PX.Objects.PO.POLineS.CuryBilledCost : Edm.Decimal
PX.Objects.PO.POLineS.BilledCost : Edm.Decimal
PX.Objects.PO.POLineS.CuryBilledDiscAmt : Edm.Decimal
PX.Objects.PO.POLineS.BilledDiscAmt : Edm.Decimal
PX.Objects.PO.POLineS.ReceivedUOM : Edm.String
PX.Objects.PO.POLineS.ReceivedQty : Edm.Decimal
PX.Objects.PO.POLineS.BaseReceivedQty : Edm.Decimal
PX.Objects.PO.POLineS.ReceivedCost : Edm.Decimal
PX.Objects.PO.POLineS.PPVAmt : Edm.Decimal
PX.Objects.PO.POLineS.UnbilledQty : Edm.Decimal "Unbilled Qty."
PX.Objects.PO.POLineS.BaseUnbilledQty : Edm.Decimal
PX.Objects.PO.POLineS.CuryUnbilledAmt : Edm.Decimal "Unbilled Amount"
PX.Objects.PO.POLineS.UnbilledAmt : Edm.Decimal
PX.Objects.PO.POLineS.DRTermStartDate : Edm.DateTimeOffset
PX.Objects.PO.POLineS.DRTermEndDate : Edm.DateTimeOffset
PX.Objects.PO.POLineS.DropshipExpenseRecording : Edm.String
PX.Objects.PO.POLineS.CostCenterID : Edm.Int32
PX.Objects.PO.POLineS.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PO.POLineS.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.POLineS.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POLineS.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.PO.POLineS.VendorDiscountSequenceByDiscountSequenceID -> PX.Objects.AP.VendorDiscountSequence (VendorID=VendorID, DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.PO.POLineS.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POLineS.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PO.POLineS.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POLineS.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PO.POLineS.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PO.POLineS.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PO.POLineS.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POLineS.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POLineS.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POLineS.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POLineS.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POLineS.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POLineS.APDiscountByVendorID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID, VendorID=BAccountID)
PX.Objects.PO.POLineS.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.PO.POLineS.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.PO.POLineS.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POLineS.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POLineS.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PO.POLineS.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PO.POLineS.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.PO.POLineS.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PO.POLineS.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.PO.POLineS.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PO.POLineS.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.PO.POLineS.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PO.POLineS.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PO.POLineS.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.PO.PONotification (EntityType)

Label: "Default Notification setup"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_PO_PONotification

# PX.Objects.PO.POOrder (EntityType)

Label: "Purchase Order"
Key: OrderNbr, OrderType
Entity sets: PX_Objects_PO_POOrder, PurchaseOrder, POOrder
Non-filterable, non-selectable: OverrideCurrency, Rejected, RequestApproval, ExternalTaxesImportInProgress, NoteText, SiteIdErrorMessage, EmployeeID, WorkgroupID, PrintedExt, EmailedExt, UpdateVendorCost, POAccrualType, LinesStatusUpdated, IntercompanySOCancelled, IntercompanySOWithEmptyInventory, CuryRate

PX.Objects.PO.POOrder.OrderType : Edm.String [key required] "Type"
PX.Objects.PO.POOrder.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POOrder.OverrideCurrency : Edm.Boolean
PX.Objects.PO.POOrder.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POOrder.OrderDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.POOrder.ExpectedDate : Edm.DateTimeOffset "Promised On"
PX.Objects.PO.POOrder.ExpirationDate : Edm.DateTimeOffset "Expires On"
PX.Objects.PO.POOrder.Status : Edm.String "Status"
PX.Objects.PO.POOrder.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PO.POOrder.Approved : Edm.Boolean [required]
PX.Objects.PO.POOrder.Rejected : Edm.Boolean "Reject"
PX.Objects.PO.POOrder.RequestApproval : Edm.Boolean "Request Approval"
PX.Objects.PO.POOrder.Cancelled : Edm.Boolean [required] "Cancel"
PX.Objects.PO.POOrder.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.PO.POOrder.IsUnbilledTaxValid : Edm.Boolean [required]
PX.Objects.PO.POOrder.ExternalTaxesImportInProgress : Edm.Boolean
PX.Objects.PO.POOrder.NoteID : Edm.Guid
PX.Objects.PO.POOrder.NoteText : Edm.String "Note Text"
PX.Objects.PO.POOrder.CuryID : Edm.String "Currency"
PX.Objects.PO.POOrder.CuryInfoID : Edm.Int64
PX.Objects.PO.POOrder.LineCntr : Edm.Int32 [required]
PX.Objects.PO.POOrder.LinesToCloseCntr : Edm.Int32 [required]
PX.Objects.PO.POOrder.LinesToCompleteCntr : Edm.Int32 [required]
PX.Objects.PO.POOrder.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.PO.POOrder.CuryOrderTotal : Edm.Decimal [required] "Order Total"
PX.Objects.PO.POOrder.OrderTotal : Edm.Decimal [required] "Order Total"
PX.Objects.PO.POOrder.CuryControlTotal : Edm.Decimal [required] "Control Total"
PX.Objects.PO.POOrder.ControlTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.OrderQty : Edm.Decimal [required] "Order Qty"
PX.Objects.PO.POOrder.CuryLineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.PO.POOrder.LineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.PO.POOrder.CuryGroupDiscTotal : Edm.Decimal [required] "Group Discounts"
PX.Objects.PO.POOrder.GroupDiscTotal : Edm.Decimal [required] "Group Discounts"
PX.Objects.PO.POOrder.CuryDocumentDiscTotal : Edm.Decimal [required] "Document Discount"
PX.Objects.PO.POOrder.DocumentDiscTotal : Edm.Decimal [required] "Document Discount"
PX.Objects.PO.POOrder.DiscTot : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryDiscTot : Edm.Decimal [required] "Document Discounts"
PX.Objects.PO.POOrder.CuryOrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.PO.POOrder.OrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.PO.POOrder.CuryGoodsExtCostTotal : Edm.Decimal [required] "Goods"
PX.Objects.PO.POOrder.GoodsExtCostTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryServiceExtCostTotal : Edm.Decimal [required] "Services"
PX.Objects.PO.POOrder.ServiceExtCostTotal : Edm.Decimal
PX.Objects.PO.POOrder.CuryFreightTot : Edm.Decimal [required] "Freight Total"
PX.Objects.PO.POOrder.FreightTot : Edm.Decimal
PX.Objects.PO.POOrder.CuryDetailExtCostTotal : Edm.Decimal "Detail Total"
PX.Objects.PO.POOrder.DetailExtCostTotal : Edm.Decimal
PX.Objects.PO.POOrder.CuryLineTotal : Edm.Decimal [required] "Line Total"
PX.Objects.PO.POOrder.LineTotal : Edm.Decimal [required] "Line Total"
PX.Objects.PO.POOrder.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.PO.POOrder.TaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryInclTaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.InclTaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryVatExemptTotal : Edm.Decimal [required] "Tax Exempt Total"
PX.Objects.PO.POOrder.VatExemptTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryVatTaxableTotal : Edm.Decimal [required] "Taxable Total"
PX.Objects.PO.POOrder.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.TaxZoneID : Edm.String "Vendor Tax Zone"
PX.Objects.PO.POOrder.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.PO.POOrder.TermsID : Edm.String "Terms"
PX.Objects.PO.POOrder.RemitAddressID : Edm.Int32 "RemitAddressID"
PX.Objects.PO.POOrder.RemitContactID : Edm.Int32
PX.Objects.PO.POOrder.SOOrderType : Edm.String "Sales Order Type"
PX.Objects.PO.POOrder.SOOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.PO.POOrder.BLType : Edm.String
PX.Objects.PO.POOrder.BLOrderNbr : Edm.String
PX.Objects.PO.POOrder.RQReqNbr : Edm.String "Requisition Ref. Nbr."
PX.Objects.PO.POOrder.OrderDesc : Edm.String "Description"
PX.Objects.PO.POOrder.DropShipLinesCount : Edm.Int32 [required]
PX.Objects.PO.POOrder.DropShipLinkedLinesCount : Edm.Int32 [required]
PX.Objects.PO.POOrder.DropShipActiveLinksCount : Edm.Int32 [required]
PX.Objects.PO.POOrder.DropShipOpenLinesCntr : Edm.Int32 [required]
PX.Objects.PO.POOrder.DropShipNotLinkedLinesCntr : Edm.Int32 [required]
PX.Objects.PO.POOrder.IsLegacyDropShip : Edm.Boolean [required]
PX.Objects.PO.POOrder.tstamp : Edm.Binary
PX.Objects.PO.POOrder.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POOrder.CreatedByScreenID : Edm.String
PX.Objects.PO.POOrder.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PO.POOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POOrder.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POOrder.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PO.POOrder.ShipDestType : Edm.String "Shipping Destination Type"
PX.Objects.PO.POOrder.SiteIdErrorMessage : Edm.String
PX.Objects.PO.POOrder.ShipToBAccountID : Edm.Int32 "Ship To"
PX.Objects.PO.POOrder.ShipAddressID : Edm.Int32 "ShipAddressID"
PX.Objects.PO.POOrder.ShipContactID : Edm.Int32 "ShipContactID"
PX.Objects.PO.POOrder.OpenOrderQty : Edm.Decimal [required] "Open Quantity"
PX.Objects.PO.POOrder.CuryUnbilledOrderTotal : Edm.Decimal [required] "Unbilled Amount"
PX.Objects.PO.POOrder.UnbilledOrderTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryUnbilledLineTotal : Edm.Decimal [required] "Unbilled Line Total"
PX.Objects.PO.POOrder.UnbilledLineTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryUnbilledTaxTotal : Edm.Decimal [required] "Unbilled Tax Total"
PX.Objects.PO.POOrder.UnbilledTaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryUnbilledInclTaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.UnbilledInclTaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.UnbilledOrderQty : Edm.Decimal [required] "Unbilled Quantity"
PX.Objects.PO.POOrder.EmployeeID : Edm.Int32 "Owner"
PX.Objects.PO.POOrder.OwnerWorkgroupID : Edm.Int32 "Workgroup ID"
PX.Objects.PO.POOrder.WorkgroupID : Edm.Int32 "Approval Workgroup ID"
PX.Objects.PO.POOrder.OwnerID : Edm.Int32 "Owner"
PX.Objects.PO.POOrder.DontPrint : Edm.Boolean [required] "Do Not Print"
PX.Objects.PO.POOrder.Printed : Edm.Boolean [required] "Printed"
PX.Objects.PO.POOrder.DontEmail : Edm.Boolean [required] "Do Not Email"
PX.Objects.PO.POOrder.Emailed : Edm.Boolean [required] "Emailed"
PX.Objects.PO.POOrder.PrintedExt : Edm.Boolean
PX.Objects.PO.POOrder.EmailedExt : Edm.Boolean
PX.Objects.PO.POOrder.FOBPoint : Edm.String "FOB Point"
PX.Objects.PO.POOrder.ShipVia : Edm.String "Ship Via"
PX.Objects.PO.POOrder.PrepaymentPct : Edm.Decimal "Prepayment Percent"
PX.Objects.PO.POOrder.OrderWeight : Edm.Decimal [required] "Weight"
PX.Objects.PO.POOrder.OrderVolume : Edm.Decimal [required] "Volume"
PX.Objects.PO.POOrder.LockCommitment : Edm.Boolean [required]
PX.Objects.PO.POOrder.CuryLineRetainageTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.LineRetainageTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.RetainedTaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryRetainedInclTaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.RetainedInclTaxTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.RetainedDiscTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.RetainageTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryPrepaidTotal : Edm.Decimal [required] "Unbilled Prepayment Total"
PX.Objects.PO.POOrder.PrepaidTotal : Edm.Decimal [required]
PX.Objects.PO.POOrder.CuryUnprepaidTotal : Edm.Decimal "Unpaid Amount"
PX.Objects.PO.POOrder.UnprepaidTotal : Edm.Decimal
PX.Objects.PO.POOrder.HasMultipleProjects : Edm.Boolean [required]
PX.Objects.PO.POOrder.DropshipReceiptProcessing : Edm.String "Drop-Ship Receipt Processing"
PX.Objects.PO.POOrder.DropshipExpenseRecording : Edm.String "Record Drop-Ship Expenses"
PX.Objects.PO.POOrder.UpdateVendorCost : Edm.Boolean
PX.Objects.PO.POOrder.DisableAutomaticDiscountCalculation : Edm.Boolean [required] "Disable Automatic Discount Update"
PX.Objects.PO.POOrder.OrderBasedAPBill : Edm.Boolean "Allow AP Bill Before Receipt"
PX.Objects.PO.POOrder.POAccrualType : Edm.String "Billing Based On"
PX.Objects.PO.POOrder.LinesStatusUpdated : Edm.Boolean
PX.Objects.PO.POOrder.ReceivedOrCompletedOrCanceledLineCntr : Edm.Int32 [required]
PX.Objects.PO.POOrder.IsIntercompany : Edm.Boolean
PX.Objects.PO.POOrder.IsIntercompanySOCreated : Edm.Boolean [required]
PX.Objects.PO.POOrder.IntercompanySOCancelled : Edm.Boolean
PX.Objects.PO.POOrder.IntercompanySOWithEmptyInventory : Edm.Boolean
PX.Objects.PO.POOrder.SpecialLineCntr : Edm.Int32 [required]
PX.Objects.PO.POOrder.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.PO.POOrder.EntityUsageType : Edm.String "Tax Exemption Type"
PX.Objects.PO.POOrder.CuryRate : Edm.Decimal
PX.Objects.PO.POOrder.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PO.POOrder.VendorByPayToVendorID -> PX.Objects.AP.Vendor
PX.Objects.PO.POOrder.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=BLType, OrderNbr=BLOrderNbr)
PX.Objects.PO.POOrder.POOrderByOriginalPOType -> PX.Objects.PO.POOrder
PX.Objects.PO.POOrder.POAddressByShipAddressID -> PX.Objects.PO.POAddress (ShipAddressID=AddressID)
PX.Objects.PO.POOrder.POAddressByRemitAddressID -> PX.Objects.PO.POAddress (RemitAddressID=AddressID)
PX.Objects.PO.POOrder.POContactByShipContactID -> PX.Objects.PO.POContact (ShipContactID=ContactID)
PX.Objects.PO.POOrder.POContactByRemitContactID -> PX.Objects.PO.POContact (RemitContactID=ContactID)
PX.Objects.PO.POOrder.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POOrder.BAccountByShipToBAccountID -> PX.Objects.CR.BAccount (ShipToBAccountID=BAccountID)
PX.Objects.PO.POOrder.BAccountByPayToVendorID -> PX.Objects.CR.BAccount
PX.Objects.PO.POOrder.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PO.POOrder.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.PO.POOrder.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.PO.POOrder.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PO.POOrder.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POOrder.EPCompanyTreeByOwnerWorkgroupID -> PX.TM.EPCompanyTree (OwnerWorkgroupID=WorkGroupID)
PX.Objects.PO.POOrder.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PO.POOrder.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.PO.POOrder.RQRequisitionByRQReqNbr -> PX.Objects.RQ.RQRequisition (RQReqNbr=ReqNbr)
PX.Objects.PO.POOrder.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.PO.POOrder.FOBPointByFOBPoint -> PX.Objects.CS.FOBPoint (FOBPoint=FOBPointID)
PX.Objects.PO.POOrder.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.PO.POOrder.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POOrder.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POOrder.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POOrder.LocationByShipToLocationID -> PX.Objects.CR.Location (ShipToBAccountID=BAccountID)
PX.Objects.PO.POOrder.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POOrder.LocationByShipToBAccountID -> PX.Objects.CR.Location (ShipToBAccountID=BAccountID)
PX.Objects.PO.POOrder.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.PO.POOrder.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.PO.POOrder.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.PO.POOrder.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.PO.POOrder.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.PO.POOrder.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.PO.POOrder.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.PO.POOrder.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POOrder.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POOrder.POOrderReceiptCollection -> Collection(PX.Objects.PO.POOrderReceipt)
PX.Objects.PO.POOrder.VPComplianceNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent)
PX.Objects.PO.POOrder.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PO.POOrder.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PO.POOrder.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.PO.POOrder.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.PO.POOrder.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.PO.POOrder.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PO.POOrder.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.PO.POOrder.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.PO.POOrder.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.PO.POOrder.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.PO.POOrder.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.PO.POOrder.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PO.POOrder.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PO.POOrder.DropShipSOLineCollection -> Collection(PX.Objects.SO.DropShipSOLine)
PX.Objects.PO.POOrder.SupplyPOLineCollection -> Collection(PX.Objects.SO.SupplyPOLine)
PX.Objects.PO.POOrder.POLine3Collection -> Collection(PX.Objects.SO.POLine3)
PX.Objects.PO.POOrder.RQRequisitionOrderCollection -> Collection(PX.Objects.RQ.RQRequisitionOrder)
PX.Objects.PO.POOrder.DropShipPOLineCollection -> Collection(PX.Objects.PO.DropShipPOLine)
PX.Objects.PO.POOrder.LinkLineOrderCollection -> Collection(PX.Objects.PO.LinkLineOrder)
PX.Objects.PO.POOrder.LinkLineReceiptCollection -> Collection(PX.Objects.PO.LinkLineReceipt)
PX.Objects.PO.POOrder.POAccrualInquiryResultCollection -> Collection(PX.Objects.PO.POAccrualInquiryResult)
PX.Objects.PO.POOrder.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.PO.POOrder.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.PO.POOrder.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.PO.POOrder.POOrderPOReceiptCollection -> Collection(PX.Objects.PO.POOrderPOReceipt)
PX.Objects.PO.POOrder.POReceiptLinePOReceiptCollection -> Collection(PX.Objects.PO.POReceiptLinePOReceipt)
PX.Objects.PO.POOrder.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PO.POOrder.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.PO.POOrder.POBlanketOrderPOOrderCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderPOOrder)
PX.Objects.PO.POOrder.POBlanketOrderPOReceiptCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt)
PX.Objects.PO.POOrder.POLinePMCollection -> Collection(PX.Objects.PM.POLinePM)
PX.Objects.PO.POOrder.POOrderPMCollection -> Collection(PX.Objects.PM.POOrderPM)
PX.Objects.PO.POOrder.SelectedProdMatlCollection -> Collection(PX.Objects.AM.SelectedProdMatl)

# PX.Objects.PO.POOrderAPDoc (EntityType)

Label: "Purchase Order to Accounts Payable Document Link"
Key: DocType, PONbr, POOrderType, RefNbr
Entity sets: PX_Objects_PO_POOrderAPDoc, PurchaseOrdertoAccountsPayableDocumentLink1, POOrderAPDoc
Non-filterable, non-selectable: TotalAmt, StatusText

PX.Objects.PO.POOrderAPDoc.DocType : Edm.String [key] "Type"
PX.Objects.PO.POOrderAPDoc.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POOrderAPDoc.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.POOrderAPDoc.Status : Edm.String "Status"
PX.Objects.PO.POOrderAPDoc.TotalQty : Edm.Decimal "Billed Qty."
PX.Objects.PO.POOrderAPDoc.TotalTranAmt : Edm.Decimal
PX.Objects.PO.POOrderAPDoc.TotalRetainageAmt : Edm.Decimal
PX.Objects.PO.POOrderAPDoc.TotalAmt : Edm.Decimal "Billed Amt."
PX.Objects.PO.POOrderAPDoc.TotalPPVAmt : Edm.Decimal "PPV Amt"
PX.Objects.PO.POOrderAPDoc.CuryID : Edm.String "Currency"
PX.Objects.PO.POOrderAPDoc.POOrderType : Edm.String [key] "PO Type"
PX.Objects.PO.POOrderAPDoc.PONbr : Edm.String [key] "PO Number"
PX.Objects.PO.POOrderAPDoc.StatusText : Edm.String
PX.Objects.PO.POOrderAPDoc.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PO.POOrderAPDoc.APInvoiceByDocType -> PX.Objects.AP.APInvoice (RefNbr=RefNbr, DocType=DocType)
PX.Objects.PO.POOrderAPDoc.POOrderByPONbr -> PX.Objects.PO.POOrder (POOrderType=OrderType, PONbr=OrderNbr)
PX.Objects.PO.POOrderAPDoc.POOrderByPOOrderType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POOrderType=OrderType)
PX.Objects.PO.POOrderAPDoc.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POOrderAPDoc.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.PO.POOrderAPDoc.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POOrderAPDoc.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.PO.POOrderAPDoc.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.PO.POOrderAPDoc.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.PO.POOrderAPDoc.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.PO.POOrderAPDoc.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.PO.POOrderAPDoc.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PO.POOrderAPDoc.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PO.POOrderAPDoc.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.PO.POOrderAPDoc.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.PO.POOrderAPDoc.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.PO.POOrderAPDoc.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.PO.POOrderAPDoc.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.Objects.PO.POOrderAPDoc.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.PO.POOrderAPDoc.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.PO.POOrderAPDoc.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.PO.POOrderAPDoc.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.PO.POOrderAPDoc.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.PO.POOrderAPDoc.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.PO.POOrderAPDoc.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.PO.POOrderAPDoc.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)

# PX.Objects.PO.POOrderDiscountDetail (EntityType)

Label: "Purchase Order Discount Detail"
Key: OrderNbr, OrderType, RecordID
Entity sets: PX_Objects_PO_POOrderDiscountDetail, PurchaseOrderDiscountDetail, POOrderDiscountDetail
Non-filterable, non-selectable: IsOrigDocDiscount

PX.Objects.PO.POOrderDiscountDetail.RecordID : Edm.Int32 [key]
PX.Objects.PO.POOrderDiscountDetail.LineNbr : Edm.Int32
PX.Objects.PO.POOrderDiscountDetail.SkipDiscount : Edm.Boolean [required] "Skip Discount"
PX.Objects.PO.POOrderDiscountDetail.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.POOrderDiscountDetail.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POOrderDiscountDetail.DiscountID : Edm.String "Discount Code"
PX.Objects.PO.POOrderDiscountDetail.DiscountSequenceID : Edm.String "Sequence ID"
PX.Objects.PO.POOrderDiscountDetail.Type : Edm.String "Type"
PX.Objects.PO.POOrderDiscountDetail.CuryInfoID : Edm.Int64
PX.Objects.PO.POOrderDiscountDetail.DiscountableAmt : Edm.Decimal
PX.Objects.PO.POOrderDiscountDetail.CuryDiscountableAmt : Edm.Decimal "Discountable Amt."
PX.Objects.PO.POOrderDiscountDetail.DiscountableQty : Edm.Decimal "Discountable Qty."
PX.Objects.PO.POOrderDiscountDetail.DiscountAmt : Edm.Decimal [required]
PX.Objects.PO.POOrderDiscountDetail.CuryDiscountAmt : Edm.Decimal [required] "Discount Amt."
PX.Objects.PO.POOrderDiscountDetail.RetainedDiscountAmt : Edm.Decimal [required]
PX.Objects.PO.POOrderDiscountDetail.DiscountPct : Edm.Decimal "Discount Percent"
PX.Objects.PO.POOrderDiscountDetail.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.PO.POOrderDiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.PO.POOrderDiscountDetail.IsManual : Edm.Boolean [required] "Manual Discount"
PX.Objects.PO.POOrderDiscountDetail.IsOrigDocDiscount : Edm.Boolean
PX.Objects.PO.POOrderDiscountDetail.ExtDiscCode : Edm.String "External Discount Code"
PX.Objects.PO.POOrderDiscountDetail.Description : Edm.String "Description"
PX.Objects.PO.POOrderDiscountDetail.tstamp : Edm.Binary
PX.Objects.PO.POOrderDiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POOrderDiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.PO.POOrderDiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POOrderDiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POOrderDiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POOrderDiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POOrderDiscountDetail.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POOrderDiscountDetail.VendorDiscountSequenceByDiscountSequenceID -> PX.Objects.AP.VendorDiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.PO.POOrderDiscountDetail.VendorDiscountSequenceByDiscountID -> PX.Objects.AP.VendorDiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)
PX.Objects.PO.POOrderDiscountDetail.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.PO.POOrderDiscountDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POOrderDiscountDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POOrderDiscountDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POOrderDiscountDetail.APDiscountByDiscountID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID)

# PX.Objects.PO.POOrderPOReceipt (EntityType)

Label: "Purchase Order to Purchase Receipt Link"
Key: PONbr, POType, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_POOrderPOReceipt, PurchaseOrdertoPurchaseReceiptLink, POOrderPOReceipt
Non-filterable, non-selectable: StatusText, NoteText

PX.Objects.PO.POOrderPOReceipt.ReceiptType : Edm.String [key] "Type"
PX.Objects.PO.POOrderPOReceipt.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.POOrderPOReceipt.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.POOrderPOReceipt.Status : Edm.String "Status"
PX.Objects.PO.POOrderPOReceipt.TotalQty : Edm.Decimal "Received Qty."
PX.Objects.PO.POOrderPOReceipt.POType : Edm.String [key] "PO Type"
PX.Objects.PO.POOrderPOReceipt.PONbr : Edm.String [key] "PO Number"
PX.Objects.PO.POOrderPOReceipt.StatusText : Edm.String
PX.Objects.PO.POOrderPOReceipt.NoteID : Edm.Guid
PX.Objects.PO.POOrderPOReceipt.NoteText : Edm.String "Note Text"
PX.Objects.PO.POOrderPOReceipt.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.PO.POOrderPOReceipt.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.PO.POOrderPOReceipt.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POOrderPOReceipt.POReceiptByReceiptType -> PX.Objects.PO.POReceipt (ReceiptNbr=ReceiptNbr, ReceiptType=ReceiptType)

# PX.Objects.PO.POOrderPrepayment (EntityType)

Label: "PO Prepayment"
Key: APDocType, APRefNbr, OrderNbr, OrderType
Entity sets: PX_Objects_PO_POOrderPrepayment, POPrepayment, POOrderPrepayment
Non-filterable, non-selectable: StatusText

PX.Objects.PO.POOrderPrepayment.OrderType : Edm.String [key] "Type"
PX.Objects.PO.POOrderPrepayment.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POOrderPrepayment.APDocType : Edm.String [key] "Doc. Type"
PX.Objects.PO.POOrderPrepayment.APRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POOrderPrepayment.IsRequest : Edm.Boolean [required]
PX.Objects.PO.POOrderPrepayment.CuryInfoID : Edm.Int64
PX.Objects.PO.POOrderPrepayment.CuryAppliedAmt : Edm.Decimal [required] "Applied to Order"
PX.Objects.PO.POOrderPrepayment.AppliedAmt : Edm.Decimal [required]
PX.Objects.PO.POOrderPrepayment.PayDocType : Edm.String
PX.Objects.PO.POOrderPrepayment.PayRefNbr : Edm.String "Payment Ref."
PX.Objects.PO.POOrderPrepayment.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POOrderPrepayment.CreatedByScreenID : Edm.String
PX.Objects.PO.POOrderPrepayment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POOrderPrepayment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POOrderPrepayment.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POOrderPrepayment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POOrderPrepayment.tstamp : Edm.Binary
PX.Objects.PO.POOrderPrepayment.StatusText : Edm.String
PX.Objects.PO.POOrderPrepayment.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POOrderPrepayment.APRegisterByAPRefNbr -> PX.Objects.AP.APRegister (APDocType=DocType, APRefNbr=RefNbr)
PX.Objects.PO.POOrderPrepayment.APRegisterByPayRefNbr -> PX.Objects.AP.APRegister (PayDocType=DocType, PayRefNbr=RefNbr)
PX.Objects.PO.POOrderPrepayment.APRegisterByPayDocType -> PX.Objects.AP.APRegister (PayRefNbr=RefNbr, PayDocType=DocType)
PX.Objects.PO.POOrderPrepayment.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POOrderPrepayment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POOrderPrepayment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PO.POOrderReceipt (EntityType)

Key: PONbr, POType, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_POOrderReceipt
Non-filterable, non-selectable: NoteText

PX.Objects.PO.POOrderReceipt.ReceiptType : Edm.String [key]
PX.Objects.PO.POOrderReceipt.ReceiptNbr : Edm.String [key]
PX.Objects.PO.POOrderReceipt.POType : Edm.String [key] "Type"
PX.Objects.PO.POOrderReceipt.PONbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POOrderReceipt.ReceiptNoteID : Edm.Guid
PX.Objects.PO.POOrderReceipt.OrderNoteID : Edm.Guid
PX.Objects.PO.POOrderReceipt.NoteText : Edm.String "Note Text"
PX.Objects.PO.POOrderReceipt.tstamp : Edm.Binary
PX.Objects.PO.POOrderReceipt.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.PO.POOrderReceipt.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)

# PX.Objects.PO.POOrderReceiptLink (EntityType)

Label: "Purchase Receipt to Purchase Order Link"
BaseType: PX.Objects.PO.POOrderReceipt
Key: PONbr, POType, ReceiptNbr, ReceiptType (inherited from PX.Objects.PO.POOrderReceipt)
Entity sets: PX_Objects_PO_POOrderReceiptLink, PurchaseReceipttoPurchaseOrderLink, POOrderReceiptLink

PX.Objects.PO.POOrderReceiptLink.Status : Edm.String "Status"
PX.Objects.PO.POOrderReceiptLink.TaxZoneID : Edm.String "Vendor Tax Zone"
PX.Objects.PO.POOrderReceiptLink.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.PO.POOrderReceiptLink.TermsID : Edm.String "Terms"
PX.Objects.PO.POOrderReceiptLink.CuryID : Edm.String "Currency"
PX.Objects.PO.POOrderReceiptLink.UnbilledOrderQty : Edm.Decimal "Unbilled Quantity"
PX.Objects.PO.POOrderReceiptLink.CuryUnbilledOrderTotal : Edm.Decimal "Unbilled Amount"
PX.Objects.PO.POOrderReceiptLink.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.PO.POOrderReceiptLink.EntityUsageType : Edm.String "Tax Exemption Type"
PX.Objects.PO.POOrderReceiptLink.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PO.POOrderReceiptLink.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.PO.POOrderReceiptLink.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)

# PX.Objects.PO.POOrderRS (EntityType)

Label: "Purchase Order"
BaseType: PX.Objects.PO.POOrder
Key: OrderNbr, OrderType (inherited from PX.Objects.PO.POOrder)
Entity sets: PX_Objects_PO_POOrderRS

# PX.Objects.PO.POReceipt (EntityType)

Label: "Purchase Receipt"
Key: ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_POReceipt, PurchaseReceipt, POReceipt
Non-filterable, non-selectable: NoteText, CuryControlTotal, InventoryDocType, InventoryRefNbr, ShowPurchaseOrdersTab, ShowPutAwayHistoryTab, ShowLandedCostsTab, IntercompanySOCancelled, DropshipFieldsSet, CorrectionReceiptNbr, ReversalInvtDocType, ReversalInvtRefNbr, CuryRate, DailyFieldReportId

PX.Objects.PO.POReceipt.APRefNbr : Edm.String "Reference Nbr."
PX.Objects.PO.POReceipt.ReceiptType : Edm.String [key required] "Type"
PX.Objects.PO.POReceipt.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.POReceipt.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POReceipt.ReceiptDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.POReceipt.InvoiceDate : Edm.DateTimeOffset "Bill Date"
PX.Objects.PO.POReceipt.FinPeriodID : Edm.String "Post Period"
PX.Objects.PO.POReceipt.TranPeriodID : Edm.String
PX.Objects.PO.POReceipt.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PO.POReceipt.Released : Edm.Boolean [required] "Released"
PX.Objects.PO.POReceipt.Received : Edm.Boolean [required] "Received"
PX.Objects.PO.POReceipt.Picked : Edm.Boolean [required] "Picked"
PX.Objects.PO.POReceipt.Status : Edm.String "Status"
PX.Objects.PO.POReceipt.NoteID : Edm.Guid
PX.Objects.PO.POReceipt.NoteText : Edm.String "Note Text"
PX.Objects.PO.POReceipt.CuryID : Edm.String "Currency"
PX.Objects.PO.POReceipt.CuryInfoID : Edm.Int64
PX.Objects.PO.POReceipt.LineCntr : Edm.Int32 [required]
PX.Objects.PO.POReceipt.OrderQty : Edm.Decimal [required] "Total Qty."
PX.Objects.PO.POReceipt.ControlQty : Edm.Decimal [required] "Control Qty."
PX.Objects.PO.POReceipt.APDocType : Edm.String "Type"
PX.Objects.PO.POReceipt.InvtDocType : Edm.String "Inventory Doc. Type"
PX.Objects.PO.POReceipt.InvtRefNbr : Edm.String "Inventory Ref. Nbr."
PX.Objects.PO.POReceipt.InvoiceNbr : Edm.String "Vendor Ref."
PX.Objects.PO.POReceipt.AutoCreateInvoice : Edm.Boolean "Create Bill"
PX.Objects.PO.POReceipt.ReturnInventoryCostMode : Edm.String "Cost of Inventory Return From"
PX.Objects.PO.POReceipt.ReturnOrigCost : Edm.Boolean "Process Return with Original Cost"
PX.Objects.PO.POReceipt.tstamp : Edm.Binary
PX.Objects.PO.POReceipt.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POReceipt.CreatedByScreenID : Edm.String
PX.Objects.PO.POReceipt.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PO.POReceipt.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POReceipt.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POReceipt.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PO.POReceipt.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.PO.POReceipt.OwnerID : Edm.Int32 "Owner"
PX.Objects.PO.POReceipt.UnbilledQty : Edm.Decimal [required] "Unbilled Quantity"
PX.Objects.PO.POReceipt.ReceiptWeight : Edm.Decimal [required] "Weight"
PX.Objects.PO.POReceipt.ReceiptVolume : Edm.Decimal [required] "Volume"
PX.Objects.PO.POReceipt.POType : Edm.String "Order Type"
PX.Objects.PO.POReceipt.ShipToBAccountID : Edm.Int32 "Ship To"
PX.Objects.PO.POReceipt.CuryOrderTotal : Edm.Decimal [required] "Total Cost"
PX.Objects.PO.POReceipt.OrderTotal : Edm.Decimal [required]
PX.Objects.PO.POReceipt.CuryControlTotal : Edm.Decimal
PX.Objects.PO.POReceipt.InventoryDocType : Edm.String "IN Doc. Type"
PX.Objects.PO.POReceipt.InventoryRefNbr : Edm.String "IN Ref. Nbr."
PX.Objects.PO.POReceipt.WMSSingleOrder : Edm.Boolean [required]
PX.Objects.PO.POReceipt.OrigPONbr : Edm.String
PX.Objects.PO.POReceipt.ShowPurchaseOrdersTab : Edm.Boolean "ShowPurchaseOrdersTab"
PX.Objects.PO.POReceipt.ShowPutAwayHistoryTab : Edm.Boolean "ShowPutAwayHistoryTab"
PX.Objects.PO.POReceipt.ShowLandedCostsTab : Edm.Boolean "ShowLandedCostsTab"
PX.Objects.PO.POReceipt.IsIntercompany : Edm.Boolean
PX.Objects.PO.POReceipt.IsIntercompanySOCreated : Edm.Boolean [required]
PX.Objects.PO.POReceipt.IntercompanySOCancelled : Edm.Boolean
PX.Objects.PO.POReceipt.SOOrderType : Edm.String
PX.Objects.PO.POReceipt.SOOrderNbr : Edm.String "SO Return"
PX.Objects.PO.POReceipt.DropshipFieldsSet : Edm.Boolean
PX.Objects.PO.POReceipt.DropshipCustomerID : Edm.Int32 "Customer"
PX.Objects.PO.POReceipt.DropshipCustomerOrderNbr : Edm.String
PX.Objects.PO.POReceipt.DropshipShipVia : Edm.String "Ship Via"
PX.Objects.PO.POReceipt.OrigReceiptNbr : Edm.String "Original Doc. Ref. Nbr."
PX.Objects.PO.POReceipt.CorrectionReceiptNbr : Edm.String "Correction Doc. Ref. Nbr."
PX.Objects.PO.POReceipt.ReversalInvtDocType : Edm.String "Reversal IN Doc. Type"
PX.Objects.PO.POReceipt.ReversalInvtRefNbr : Edm.String "Reversal IN Ref. Nbr."
PX.Objects.PO.POReceipt.IsUnderCorrection : Edm.Boolean [required] "IsUnderCorrection"
PX.Objects.PO.POReceipt.Canceled : Edm.Boolean [required] "Canceled"
PX.Objects.PO.POReceipt.CuryRate : Edm.Decimal
PX.Objects.PO.POReceipt.DailyFieldReportId : Edm.Int32 "DailyFieldReportId"
PX.Objects.PO.POReceipt.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PO.POReceipt.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.POReceipt.BAccountByShipToBAccountID -> PX.Objects.CR.BAccount (ShipToBAccountID=BAccountID)
PX.Objects.PO.POReceipt.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POReceipt.BAccountByDropshipCustomerID -> PX.Objects.CR.BAccount (DropshipCustomerID=BAccountID)
PX.Objects.PO.POReceipt.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.PO.POReceipt.APRegisterByAPDocType -> PX.Objects.AP.APRegister (APRefNbr=RefNbr, APDocType=DocType)
PX.Objects.PO.POReceipt.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.PO.POReceipt.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PO.POReceipt.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POReceipt.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POReceipt.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.PO.POReceipt.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.PO.POReceipt.SOShipmentByIntercompanyShipmentNbr -> PX.Objects.SO.SOShipment
PX.Objects.PO.POReceipt.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptNbr=OrigReceiptNbr)
PX.Objects.PO.POReceipt.CarrierByDropshipShipVia -> PX.Objects.CS.Carrier (DropshipShipVia=CarrierID)
PX.Objects.PO.POReceipt.INRegisterByInvtDocType -> PX.Objects.IN.INRegister (InvtRefNbr=RefNbr, InvtDocType=DocType)
PX.Objects.PO.POReceipt.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POReceipt.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POReceipt.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POReceipt.LocationByShipToLocationID -> PX.Objects.CR.Location (ShipToBAccountID=BAccountID)
PX.Objects.PO.POReceipt.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POReceipt.LocationByShipToBAccountID -> PX.Objects.CR.Location (ShipToBAccountID=BAccountID)
PX.Objects.PO.POReceipt.LocationByDropshipCustomerID -> PX.Objects.CR.Location (DropshipCustomerID=BAccountID)
PX.Objects.PO.POReceipt.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.PO.POReceipt.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)
PX.Objects.PO.POReceipt.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PO.POReceipt.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.PO.POReceipt.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POReceipt.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POReceipt.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.PO.POReceipt.POOrderReceiptCollection -> Collection(PX.Objects.PO.POOrderReceipt)
PX.Objects.PO.POReceipt.POLandedCostReceiptCollection -> Collection(PX.Objects.PO.POLandedCostReceipt)
PX.Objects.PO.POReceipt.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PO.POReceipt.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.PO.POReceipt.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.PO.POReceipt.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PO.POReceipt.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.PO.POReceipt.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.PO.POReceipt.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.PO.POReceipt.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.PO.POReceipt.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.Objects.PO.POReceipt.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PO.POReceipt.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.PO.POReceipt.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.PO.POReceipt.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PO.POReceipt.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PO.POReceipt.LinkLineReceiptCollection -> Collection(PX.Objects.PO.LinkLineReceipt)
PX.Objects.PO.POReceipt.POOrderPOReceiptCollection -> Collection(PX.Objects.PO.POOrderPOReceipt)
PX.Objects.PO.POReceipt.POReceiptLinePOReceiptCollection -> Collection(PX.Objects.PO.POReceiptLinePOReceipt)
PX.Objects.PO.POReceipt.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PO.POReceipt.POBlanketOrderPOReceiptCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt)
PX.Objects.PO.POReceipt.IntercompanyReturnedGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult)
PX.Objects.PO.POReceipt.POCartReceiptCollection -> Collection(PX.Objects.PO.POCartReceipt)
PX.Objects.PO.POReceipt.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.PO.POReceipt.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)
PX.Objects.PO.POReceipt.IntercompanyGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyGoodsInTransitResult)

# PX.Objects.PO.POReceiptItemLotSerialAttributesHeader (EntityType)

Label: "POReceiptItemLotSerialAttributesHeader"
Key: InventoryID, LotSerialNbr, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_POReceiptItemLotSerialAttributesHeader, POReceiptItemLotSerialAttributesHeader
Non-filterable, non-selectable: NoteText

PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.ReceiptType : Edm.String [key] "Type"
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.InventoryID : Edm.Int32 [key]
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.LotSerialNbr : Edm.String [key] "Lot/Serial Nbr."
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.MfgLotSerialNbr : Edm.String "Manufacturer Lot/Serial Nbr."
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.NoteID : Edm.Guid
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.NoteText : Edm.String "Note Text"
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.CreatedByScreenID : Edm.String
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.tstamp : Edm.Binary
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.INItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.IN.DAC.INItemLotSerialAttributesHeader (InventoryID=InventoryID, LotSerialNbr=LotSerialNbr)
PX.Objects.PO.POReceiptItemLotSerialAttributesHeader.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)

# PX.Objects.PO.POReceiptLine (EntityType)

Label: "Purchase Receipt Line"
Key: LineNbr, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_POReceiptLine, PurchaseReceiptLine1, POReceiptLine
Non-filterable, non-selectable: TranType, AllowComplete, AllowOpen, NoteText, OrigOrderQty, OpenOrderQty, ReturnedQty, IsKit, IsLSEntryBlocked, CuryLineAmt, AllowResetCorrectionLine

PX.Objects.PO.POReceiptLine.BranchID : Edm.Int32 "Branch"
PX.Objects.PO.POReceiptLine.ReceiptType : Edm.String [key] "Type"
PX.Objects.PO.POReceiptLine.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.POReceiptLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POReceiptLine.SortOrder : Edm.Int32 "Line Order"
PX.Objects.PO.POReceiptLine.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.PO.POReceiptLine.OrigReceiptType : Edm.String "PO Receipt Type"
PX.Objects.PO.POReceiptLine.OrigReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.PO.POReceiptLine.OrigReceiptLineNbr : Edm.Int32 "PO Receipt Line Nbr."
PX.Objects.PO.POReceiptLine.IsCorrection : Edm.Boolean
PX.Objects.PO.POReceiptLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POReceiptLine.LineType : Edm.String "Line Type"
PX.Objects.PO.POReceiptLine.AccrueCost : Edm.Boolean "Accrue Cost"
PX.Objects.PO.POReceiptLine.IsIntercompany : Edm.Boolean
PX.Objects.PO.POReceiptLine.TranType : Edm.String
PX.Objects.PO.POReceiptLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POReceiptLine.ReceiptDate : Edm.DateTimeOffset
PX.Objects.PO.POReceiptLine.UOM : Edm.String "UOM"
PX.Objects.PO.POReceiptLine.POType : Edm.String "PO Order Type"
PX.Objects.PO.POReceiptLine.PONbr : Edm.String "PO Order Nbr."
PX.Objects.PO.POReceiptLine.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.PO.POReceiptLine.InvtMult : Edm.Int16 "Inventory Multiplier"
PX.Objects.PO.POReceiptLine.AllowComplete : Edm.Boolean "Complete PO Line"
PX.Objects.PO.POReceiptLine.AllowOpen : Edm.Boolean "Open PO Line"
PX.Objects.PO.POReceiptLine.ReceiptQty : Edm.Decimal [required] "Receipt Qty."
PX.Objects.PO.POReceiptLine.BaseReceiptQty : Edm.Decimal [required] "Base Receipt Qty."
PX.Objects.PO.POReceiptLine.ReceivedToDateQty : Edm.Decimal [required] "Received to Date"
PX.Objects.PO.POReceiptLine.MaxTransferQty : Edm.Decimal
PX.Objects.PO.POReceiptLine.MaxTransferBaseQty : Edm.Decimal
PX.Objects.PO.POReceiptLine.BaseMultReceiptQty : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.UnassignedQty : Edm.Decimal [required] "Unassigned Qty."
PX.Objects.PO.POReceiptLine.CuryInfoID : Edm.Int64
PX.Objects.PO.POReceiptLine.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.PO.POReceiptLine.UnitCost : Edm.Decimal
PX.Objects.PO.POReceiptLine.CuryTranUnitCost : Edm.Decimal
PX.Objects.PO.POReceiptLine.TranUnitCost : Edm.Decimal
PX.Objects.PO.POReceiptLine.ManualPrice : Edm.Boolean "Manual Cost"
PX.Objects.PO.POReceiptLine.DiscPct : Edm.Decimal [required] "Discount Percent"
PX.Objects.PO.POReceiptLine.CuryExtCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.PO.POReceiptLine.ExtCost : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.CuryDiscAmt : Edm.Decimal [required] "Discount Amount"
PX.Objects.PO.POReceiptLine.DiscAmt : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.GroupDiscountRate : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.DocumentDiscountRate : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.CuryTranCost : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.TranCost : Edm.Decimal "Estimated IN Ext. Cost"
PX.Objects.PO.POReceiptLine.TranCostFinal : Edm.Decimal "Final IN Ext. Cost"
PX.Objects.PO.POReceiptLine.ReasonCode : Edm.String "Reason Code"
PX.Objects.PO.POReceiptLine.AlternateID : Edm.String
PX.Objects.PO.POReceiptLine.TranDesc : Edm.String "Transaction Descr."
PX.Objects.PO.POReceiptLine.UnitWeight : Edm.Decimal [required] "Unit Weight"
PX.Objects.PO.POReceiptLine.UnitVolume : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.ExtWeight : Edm.Decimal [required] "Weight"
PX.Objects.PO.POReceiptLine.ExtVolume : Edm.Decimal [required] "Volume"
PX.Objects.PO.POReceiptLine.NoteID : Edm.Guid
PX.Objects.PO.POReceiptLine.NoteText : Edm.String "Note Text"
PX.Objects.PO.POReceiptLine.OrigDocType : Edm.String
PX.Objects.PO.POReceiptLine.OrigTranType : Edm.String
PX.Objects.PO.POReceiptLine.OrigRefNbr : Edm.String
PX.Objects.PO.POReceiptLine.OrigLineNbr : Edm.Int32
PX.Objects.PO.POReceiptLine.OrigToLocationID : Edm.Int32
PX.Objects.PO.POReceiptLine.OrigIsLotSerial : Edm.Boolean
PX.Objects.PO.POReceiptLine.OrigNoteID : Edm.Guid
PX.Objects.PO.POReceiptLine.OrigIsFixedInTransit : Edm.Boolean
PX.Objects.PO.POReceiptLine.SOOrderType : Edm.String "Transfer Order Type"
PX.Objects.PO.POReceiptLine.SOOrderNbr : Edm.String "Transfer Order Nbr."
PX.Objects.PO.POReceiptLine.SOOrderLineNbr : Edm.Int32 "Transfer Line Nbr."
PX.Objects.PO.POReceiptLine.SOShipmentType : Edm.String
PX.Objects.PO.POReceiptLine.SOShipmentNbr : Edm.String "Transfer Shipment Nbr."
PX.Objects.PO.POReceiptLine.OrigPlanType : Edm.String
PX.Objects.PO.POReceiptLine.Released : Edm.Boolean "Released"
PX.Objects.PO.POReceiptLine.INReleased : Edm.Boolean [required]
PX.Objects.PO.POReceiptLine.IsUnassigned : Edm.Boolean [required]
PX.Objects.PO.POReceiptLine.tstamp : Edm.Binary
PX.Objects.PO.POReceiptLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POReceiptLine.CreatedByScreenID : Edm.String
PX.Objects.PO.POReceiptLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceiptLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POReceiptLine.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POReceiptLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceiptLine.OrigOrderQty : Edm.Decimal "Ordered Qty."
PX.Objects.PO.POReceiptLine.OpenOrderQty : Edm.Decimal "Open Qty."
PX.Objects.PO.POReceiptLine.UnbilledQty : Edm.Decimal [required] "Unbilled Qty."
PX.Objects.PO.POReceiptLine.BaseUnbilledQty : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.BillPPVAmt : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.POAccrualType : Edm.String "Billing Based On"
PX.Objects.PO.POReceiptLine.POAccrualRefNoteID : Edm.Guid
PX.Objects.PO.POReceiptLine.POAccrualLineNbr : Edm.Int32
PX.Objects.PO.POReceiptLine.OrigReceiptLineType : Edm.String
PX.Objects.PO.POReceiptLine.BaseOrigQty : Edm.Decimal
PX.Objects.PO.POReceiptLine.BaseReturnedQty : Edm.Decimal [required]
PX.Objects.PO.POReceiptLine.ReturnedQty : Edm.Decimal "Returned Qty."
PX.Objects.PO.POReceiptLine.IsKit : Edm.Boolean "Kit"
PX.Objects.PO.POReceiptLine.IsLSEntryBlocked : Edm.Boolean
PX.Objects.PO.POReceiptLine.AllowEditUnitCost : Edm.Boolean [required] "Editable Unit Cost"
PX.Objects.PO.POReceiptLine.IntercompanyShipmentLineNbr : Edm.Int32
PX.Objects.PO.POReceiptLine.CuryLineAmt : Edm.Decimal
PX.Objects.PO.POReceiptLine.LotSerialNbrRequiredForDropship : Edm.Boolean [required]
PX.Objects.PO.POReceiptLine.DropshipExpenseRecording : Edm.String
PX.Objects.PO.POReceiptLine.IsSpecialOrder : Edm.Boolean [required]
PX.Objects.PO.POReceiptLine.CostCenterID : Edm.Int32 [required]
PX.Objects.PO.POReceiptLine.CanceledWithoutCorrection : Edm.Boolean [required] "CanceledWithoutCorrection"
PX.Objects.PO.POReceiptLine.IsAdjusted : Edm.Boolean [required] "Corrected"
PX.Objects.PO.POReceiptLine.IsAdjustedIN : Edm.Boolean [required]
PX.Objects.PO.POReceiptLine.AllowResetCorrectionLine : Edm.Boolean
PX.Objects.PO.POReceiptLine.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PO.POReceiptLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.POReceiptLine.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.PO.POReceiptLine.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.PO.POReceiptLine.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.PO.POReceiptLine.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.PO.POReceiptLine.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PO.POReceiptLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POReceiptLine.INTranByOrigLineNbr -> PX.Objects.IN.INTran (OrigDocType=DocType, OrigRefNbr=RefNbr, OrigLineNbr=LineNbr)
PX.Objects.PO.POReceiptLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLine.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.PO.POReceiptLine.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.PO.POReceiptLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.PO.POReceiptLine.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POReceiptLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POReceiptLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POReceiptLine.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOOrderLineNbr=LineNbr)
PX.Objects.PO.POReceiptLine.SOShipmentBySOShipmentNbr -> PX.Objects.SO.SOShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr)
PX.Objects.PO.POReceiptLine.SOShipmentBySOShipmentType -> PX.Objects.SO.SOShipment (SOShipmentNbr=ShipmentNbr, SOShipmentType=ShipmentType)
PX.Objects.PO.POReceiptLine.POAccrualStatusByPOAccrualType -> PX.Objects.PO.POAccrualStatus (POAccrualRefNoteID=RefNoteID, POAccrualLineNbr=LineNbr, POAccrualType=Type)
PX.Objects.PO.POReceiptLine.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POReceiptLine.POReceiptByOrigReceiptNbr -> PX.Objects.PO.POReceipt (OrigReceiptType=ReceiptType, OrigReceiptNbr=ReceiptNbr)
PX.Objects.PO.POReceiptLine.POReceiptByOrigReceiptType -> PX.Objects.PO.POReceipt (OrigReceiptNbr=ReceiptNbr, OrigReceiptType=ReceiptType)
PX.Objects.PO.POReceiptLine.POReceiptLineByOrigReceiptLineNbr -> PX.Objects.PO.POReceiptLine (ReceiptType=OrigReceiptType, ReceiptNbr=OrigReceiptNbr, OrigReceiptLineNbr=LineNbr)
PX.Objects.PO.POReceiptLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PO.POReceiptLine.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.PO.POReceiptLine.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.PO.POReceiptLine.INRegisterByOrigRefNbr -> PX.Objects.IN.INRegister (OrigDocType=DocType, OrigRefNbr=RefNbr)
PX.Objects.PO.POReceiptLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POReceiptLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POReceiptLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PO.POReceiptLine.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POReceiptLine.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POReceiptLine.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POReceiptLine.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POReceiptLine.INLocationStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLocationStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.PO.POReceiptLine.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.PO.POReceiptLine.INSiteStatusByCostCenterByCostCenterID -> PX.Objects.IN.INSiteStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.PO.POReceiptLine.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLine.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLine.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLine.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.PO.POReceiptLine.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PO.POReceiptLine.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POReceiptLine.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POReceiptLine.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.PO.POReceiptLine.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.PO.POReceiptLine.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.PO.POReceiptLine.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.PO.POReceiptLine.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.PO.POReceiptLine.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.PO.POReceiptLinePOReceipt (EntityType)

Label: "Purchase Receipt Line"
Key: LineNbr, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_POReceiptLinePOReceipt, PurchaseReceiptLine2, POReceiptLinePOReceipt

PX.Objects.PO.POReceiptLinePOReceipt.ReceiptType : Edm.String [key] "Type"
PX.Objects.PO.POReceiptLinePOReceipt.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.POReceiptLinePOReceipt.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POReceiptLinePOReceipt.POType : Edm.String "Order Type"
PX.Objects.PO.POReceiptLinePOReceipt.PONbr : Edm.String "Order Nbr."
PX.Objects.PO.POReceiptLinePOReceipt.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.PO.POReceiptLinePOReceipt.ReceiptDate : Edm.DateTimeOffset "Date"
PX.Objects.PO.POReceiptLinePOReceipt.Status : Edm.String "Status"
PX.Objects.PO.POReceiptLinePOReceipt.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POReceiptLinePOReceipt.LotSerialNbr : Edm.String
PX.Objects.PO.POReceiptLinePOReceipt.UOM : Edm.String "UOM"
PX.Objects.PO.POReceiptLinePOReceipt.ReceiptQty : Edm.Decimal "Receipt Qty."
PX.Objects.PO.POReceiptLinePOReceipt.InvtMult : Edm.Int16 "Inventory Multiplier"
PX.Objects.PO.POReceiptLinePOReceipt.IsUnderCorrection : Edm.Boolean "IsUnderCorrection"
PX.Objects.PO.POReceiptLinePOReceipt.Canceled : Edm.Boolean "Canceled"
PX.Objects.PO.POReceiptLinePOReceipt.POOrderByPONbr -> PX.Objects.PO.POOrder (PONbr=OrderNbr)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptByReceiptType -> PX.Objects.PO.POReceipt (ReceiptNbr=ReceiptNbr, ReceiptType=ReceiptType)
PX.Objects.PO.POReceiptLinePOReceipt.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.PO.POReceiptLinePOReceipt.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptNbr=OrigReceiptNbr)
PX.Objects.PO.POReceiptLinePOReceipt.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.PO.POReceiptLinePOReceipt.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)
PX.Objects.PO.POReceiptLinePOReceipt.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PO.POReceiptLinePOReceipt.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.PO.POReceiptLinePOReceipt.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POReceiptLinePOReceipt.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.PO.POReceiptLinePOReceipt.POOrderReceiptCollection -> Collection(PX.Objects.PO.POOrderReceipt)
PX.Objects.PO.POReceiptLinePOReceipt.POLandedCostReceiptCollection -> Collection(PX.Objects.PO.POLandedCostReceipt)
PX.Objects.PO.POReceiptLinePOReceipt.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.PO.POReceiptLinePOReceipt.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.PO.POReceiptLinePOReceipt.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.PO.POReceiptLinePOReceipt.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.PO.POReceiptLinePOReceipt.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.Objects.PO.POReceiptLinePOReceipt.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.PO.POReceiptLinePOReceipt.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.PO.POReceiptLinePOReceipt.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.PO.POReceiptLinePOReceipt.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.PO.POReceiptLinePOReceipt.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.PO.POReceiptLinePOReceipt.LinkLineReceiptCollection -> Collection(PX.Objects.PO.LinkLineReceipt)
PX.Objects.PO.POReceiptLinePOReceipt.POOrderPOReceiptCollection -> Collection(PX.Objects.PO.POOrderPOReceipt)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptLinePOReceiptCollection -> Collection(PX.Objects.PO.POReceiptLinePOReceipt)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.PO.POReceiptLinePOReceipt.POBlanketOrderPOReceiptCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderPOReceipt)
PX.Objects.PO.POReceiptLinePOReceipt.IntercompanyReturnedGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult)
PX.Objects.PO.POReceiptLinePOReceipt.POCartReceiptCollection -> Collection(PX.Objects.PO.POCartReceipt)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.PO.POReceiptLinePOReceipt.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)
PX.Objects.PO.POReceiptLinePOReceipt.IntercompanyGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyGoodsInTransitResult)

# PX.Objects.PO.POReceiptLineS (EntityType)

Label: "Purchase Receipt Line"
Key: LineNbr, ReceiptNbr, ReceiptType
Entity sets: PX_Objects_PO_POReceiptLineS, PurchaseReceiptLine3, POReceiptLineS

PX.Objects.PO.POReceiptLineS.OrderType : Edm.String
PX.Objects.PO.POReceiptLineS.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.POReceiptLineS.ReceiptType : Edm.String [key] "Receipt Type"
PX.Objects.PO.POReceiptLineS.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POReceiptLineS.SortOrder : Edm.Int32
PX.Objects.PO.POReceiptLineS.LineType : Edm.String "Line Type"
PX.Objects.PO.POReceiptLineS.IsStockItem : Edm.Boolean
PX.Objects.PO.POReceiptLineS.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POReceiptLineS.AccrueCost : Edm.Boolean
PX.Objects.PO.POReceiptLineS.VendorID : Edm.Int32 "Vendor"
PX.Objects.PO.POReceiptLineS.ReceiptDate : Edm.DateTimeOffset
PX.Objects.PO.POReceiptLineS.UOM : Edm.String "UOM"
PX.Objects.PO.POReceiptLineS.ReceiptQty : Edm.Decimal "Receipt Qty."
PX.Objects.PO.POReceiptLineS.BaseReceiptQty : Edm.Decimal
PX.Objects.PO.POReceiptLineS.CuryID : Edm.String "Order Currency"
PX.Objects.PO.POReceiptLineS.ReturnInventoryCostMode : Edm.String "Cost of Inventory Return From"
PX.Objects.PO.POReceiptLineS.OrderCuryInfoID : Edm.Int64
PX.Objects.PO.POReceiptLineS.ReceiptCuryInfoID : Edm.Int64
PX.Objects.PO.POReceiptLineS.CuryOrderUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.PO.POReceiptLineS.OrderUnitCost : Edm.Decimal
PX.Objects.PO.POReceiptLineS.CuryExtCost : Edm.Decimal "Order Line Amount"
PX.Objects.PO.POReceiptLineS.ExtCost : Edm.Decimal
PX.Objects.PO.POReceiptLineS.CuryOrderLineAmt : Edm.Decimal
PX.Objects.PO.POReceiptLineS.OrderLineAmt : Edm.Decimal
PX.Objects.PO.POReceiptLineS.OrderDiscPct : Edm.Decimal "Discount Percent"
PX.Objects.PO.POReceiptLineS.CompletePOLine : Edm.String
PX.Objects.PO.POReceiptLineS.ReceiptDiscPct : Edm.Decimal "Discount Percent"
PX.Objects.PO.POReceiptLineS.CuryOrderDiscAmt : Edm.Decimal
PX.Objects.PO.POReceiptLineS.OrderDiscAmt : Edm.Decimal
PX.Objects.PO.POReceiptLineS.CuryReceiptDiscAmt : Edm.Decimal
PX.Objects.PO.POReceiptLineS.ReceiptDiscAmt : Edm.Decimal
PX.Objects.PO.POReceiptLineS.CuryReceiptUnitCost : Edm.Decimal "Receipt Unit Cost"
PX.Objects.PO.POReceiptLineS.ReceiptUnitCost : Edm.Decimal
PX.Objects.PO.POReceiptLineS.CuryReceiptExtCost : Edm.Decimal
PX.Objects.PO.POReceiptLineS.ReceiptExtCost : Edm.Decimal
PX.Objects.PO.POReceiptLineS.UnbilledQty : Edm.Decimal "Unbilled Qty."
PX.Objects.PO.POReceiptLineS.BaseUnbilledQty : Edm.Decimal
PX.Objects.PO.POReceiptLineS.OrderUOM : Edm.String "UOM"
PX.Objects.PO.POReceiptLineS.OrderQty : Edm.Decimal "Ordered Qty."
PX.Objects.PO.POReceiptLineS.BaseOrderQty : Edm.Decimal
PX.Objects.PO.POReceiptLineS.RetainageAmt : Edm.Decimal
PX.Objects.PO.POReceiptLineS.CuryUnbilledAmt : Edm.Decimal "Unbilled Amount"
PX.Objects.PO.POReceiptLineS.UnbilledAmt : Edm.Decimal
PX.Objects.PO.POReceiptLineS.GroupDiscountRate : Edm.Decimal
PX.Objects.PO.POReceiptLineS.DocumentDiscountRate : Edm.Decimal
PX.Objects.PO.POReceiptLineS.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.PO.POReceiptLineS.ExpenseAcctID : Edm.Int32
PX.Objects.PO.POReceiptLineS.ExpenseSubID : Edm.Int32
PX.Objects.PO.POReceiptLineS.POAccrualAcctID : Edm.Int32
PX.Objects.PO.POReceiptLineS.POAccrualSubID : Edm.Int32
PX.Objects.PO.POReceiptLineS.TranDesc : Edm.String "Transaction Descr."
PX.Objects.PO.POReceiptLineS.TaxID : Edm.String "Tax ID"
PX.Objects.PO.POReceiptLineS.ProjectID : Edm.Int32
PX.Objects.PO.POReceiptLineS.TaskID : Edm.Int32
PX.Objects.PO.POReceiptLineS.CostCodeID : Edm.Int32
PX.Objects.PO.POReceiptLineS.POAccrualType : Edm.String
PX.Objects.PO.POReceiptLineS.POAccrualRefNoteID : Edm.Guid
PX.Objects.PO.POReceiptLineS.POAccrualLineNbr : Edm.Int32
PX.Objects.PO.POReceiptLineS.POType : Edm.String "Order Type"
PX.Objects.PO.POReceiptLineS.PONbr : Edm.String "Order Nbr."
PX.Objects.PO.POReceiptLineS.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.PO.POReceiptLineS.DiscountID : Edm.String
PX.Objects.PO.POReceiptLineS.DiscountSequenceID : Edm.String
PX.Objects.PO.POReceiptLineS.AllowEditUnitCost : Edm.Boolean
PX.Objects.PO.POReceiptLineS.DRTermStartDate : Edm.DateTimeOffset
PX.Objects.PO.POReceiptLineS.DRTermEndDate : Edm.DateTimeOffset
PX.Objects.PO.POReceiptLineS.DropshipExpenseRecording : Edm.String
PX.Objects.PO.POReceiptLineS.CostCenterID : Edm.Int32
PX.Objects.PO.POReceiptLineS.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PO.POReceiptLineS.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.POReceiptLineS.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.PO.POReceiptLineS.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.PO.POReceiptLineS.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.PO.POReceiptLineS.VendorDiscountSequenceByDiscountSequenceID -> PX.Objects.AP.VendorDiscountSequence (VendorID=VendorID, DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.PO.POReceiptLineS.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineS.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PO.POReceiptLineS.CurrencyInfoByOrderCuryInfoID -> PX.Objects.CM.CurrencyInfo (OrderCuryInfoID=CuryInfoID)
PX.Objects.PO.POReceiptLineS.CurrencyInfoByReceiptCuryInfoID -> PX.Objects.CM.CurrencyInfo (ReceiptCuryInfoID=CuryInfoID)
PX.Objects.PO.POReceiptLineS.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PO.POReceiptLineS.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.PO.POReceiptLineS.POAccrualStatusByPOAccrualType -> PX.Objects.PO.POAccrualStatus (POAccrualRefNoteID=RefNoteID, POAccrualLineNbr=LineNbr, POAccrualType=Type)
PX.Objects.PO.POReceiptLineS.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POReceiptLineS.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.PO.POReceiptLineS.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POReceiptLineS.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POReceiptLineS.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POReceiptLineS.AccountByExpenseAcctID -> PX.Objects.GL.Account (ExpenseAcctID=AccountID)
PX.Objects.PO.POReceiptLineS.AccountByPOAccrualAcctID -> PX.Objects.GL.Account (POAccrualAcctID=AccountID)
PX.Objects.PO.POReceiptLineS.SubByExpenseSubID -> PX.Objects.GL.Sub (ExpenseSubID=SubID)
PX.Objects.PO.POReceiptLineS.SubByPOAccrualSubID -> PX.Objects.GL.Sub (POAccrualSubID=SubID)
PX.Objects.PO.POReceiptLineS.APDiscountByVendorID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID, VendorID=BAccountID)
PX.Objects.PO.POReceiptLineS.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.PO.POReceiptLineS.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.PO.POReceiptLineS.POReceiptByOrigReceiptNbr -> PX.Objects.PO.POReceipt
PX.Objects.PO.POReceiptLineS.POReceiptByOrigReceiptType -> PX.Objects.PO.POReceipt
PX.Objects.PO.POReceiptLineS.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType)
PX.Objects.PO.POReceiptLineS.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.PO.POReceiptLineS.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.PO.POReceiptLineS.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.PO.POReceiptLineS.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.PO.POReceiptLineS.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.PO.POReceiptLineS.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.PO.POReceiptLineS.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.PO.POReceiptLineS.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.PO.POReceiptLineSplit (EntityType)

Label: "Purchase Receipt Line Split"
Key: LineNbr, ReceiptNbr, ReceiptType, SplitLineNbr
Entity sets: PX_Objects_PO_POReceiptLineSplit, PurchaseReceiptLineSplit, POReceiptLineSplit
Non-filterable, non-selectable: TranType, LotSerClassID, AssignedNbr, ProjectID, TaskID

PX.Objects.PO.POReceiptLineSplit.ReceiptType : Edm.String [key] "Type"
PX.Objects.PO.POReceiptLineSplit.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.POReceiptLineSplit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POReceiptLineSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.PO.POReceiptLineSplit.PONbr : Edm.String
PX.Objects.PO.POReceiptLineSplit.LineType : Edm.String
PX.Objects.PO.POReceiptLineSplit.ReceiptDate : Edm.DateTimeOffset "Ship On"
PX.Objects.PO.POReceiptLineSplit.InvtMult : Edm.Int16
PX.Objects.PO.POReceiptLineSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POReceiptLineSplit.IsIntercompany : Edm.Boolean
PX.Objects.PO.POReceiptLineSplit.TranType : Edm.String
PX.Objects.PO.POReceiptLineSplit.OrigPlanType : Edm.String
PX.Objects.PO.POReceiptLineSplit.PlanID : Edm.Int64
PX.Objects.PO.POReceiptLineSplit.LotSerClassID : Edm.String
PX.Objects.PO.POReceiptLineSplit.AssignedNbr : Edm.String
PX.Objects.PO.POReceiptLineSplit.UOM : Edm.String "UOM"
PX.Objects.PO.POReceiptLineSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.PO.POReceiptLineSplit.BaseQty : Edm.Decimal [required]
PX.Objects.PO.POReceiptLineSplit.ReceivedQty : Edm.Decimal [required] "Received to Date"
PX.Objects.PO.POReceiptLineSplit.BaseReceivedQty : Edm.Decimal
PX.Objects.PO.POReceiptLineSplit.PutAwayQty : Edm.Decimal [required] "Putaway Qty."
PX.Objects.PO.POReceiptLineSplit.BasePutAwayQty : Edm.Decimal
PX.Objects.PO.POReceiptLineSplit.MaxTransferBaseQty : Edm.Decimal
PX.Objects.PO.POReceiptLineSplit.IsUnassigned : Edm.Boolean [required]
PX.Objects.PO.POReceiptLineSplit.ProjectID : Edm.Int32
PX.Objects.PO.POReceiptLineSplit.TaskID : Edm.Int32
PX.Objects.PO.POReceiptLineSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POReceiptLineSplit.CreatedByScreenID : Edm.String
PX.Objects.PO.POReceiptLineSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceiptLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POReceiptLineSplit.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POReceiptLineSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceiptLineSplit.tstamp : Edm.Binary
PX.Objects.PO.POReceiptLineSplit.IsReverse : Edm.Boolean [required]
PX.Objects.PO.POReceiptLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.PO.POReceiptLineSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POReceiptLineSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POReceiptLineSplit.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POReceiptLineSplit.POReceiptItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.PO.POReceiptItemLotSerialAttributesHeader (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr, InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.POReceiptLineByLineNbr -> PX.Objects.PO.POReceiptLine (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr, LineNbr=LineNbr)
PX.Objects.PO.POReceiptLineSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.PO.POReceiptLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.PO.POReceiptLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.PO.POReceiptLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POReceiptLineSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.INItemLotSerialByLotSerialNbr -> PX.Objects.IN.INItemLotSerial (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.INItemLotSerialAttributesHeaderByLotSerialNbr -> PX.Objects.IN.DAC.INItemLotSerialAttributesHeader (InventoryID=InventoryID)
PX.Objects.PO.POReceiptLineSplit.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.PO.POReceiptLineSplit.POReceiptSplitToCartSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToCartSplitLink)
PX.Objects.PO.POReceiptLineSplit.POReceiptSplitToTransferSplitLinkCollection -> Collection(PX.Objects.PO.POReceiptSplitToTransferSplitLink)

# PX.Objects.PO.POReceiptSplitToCartSplitLink (EntityType)

Label: "Receipt Line Split To Cart Split Link"
Key: CartID, CartSplitLineNbr, ReceiptLineNbr, ReceiptNbr, ReceiptSplitLineNbr, ReceiptType, SiteID
Entity sets: PX_Objects_PO_POReceiptSplitToCartSplitLink, ReceiptLineSplitToCartSplitLink, POReceiptSplitToCartSplitLink

PX.Objects.PO.POReceiptSplitToCartSplitLink.ReceiptType : Edm.String [key]
PX.Objects.PO.POReceiptSplitToCartSplitLink.ReceiptNbr : Edm.String [key]
PX.Objects.PO.POReceiptSplitToCartSplitLink.ReceiptLineNbr : Edm.Int32 [key]
PX.Objects.PO.POReceiptSplitToCartSplitLink.ReceiptSplitLineNbr : Edm.Int32 [key]
PX.Objects.PO.POReceiptSplitToCartSplitLink.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.PO.POReceiptSplitToCartSplitLink.CartID : Edm.Int32 [key]
PX.Objects.PO.POReceiptSplitToCartSplitLink.CartSplitLineNbr : Edm.Int32 [key]
PX.Objects.PO.POReceiptSplitToCartSplitLink.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.PO.POReceiptSplitToCartSplitLink.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POReceiptSplitToCartSplitLink.POReceiptLineByReceiptLineNbr -> PX.Objects.PO.POReceiptLine (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr, ReceiptLineNbr=LineNbr)
PX.Objects.PO.POReceiptSplitToCartSplitLink.POReceiptLineSplitByReceiptSplitLineNbr -> PX.Objects.PO.POReceiptLineSplit (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr, ReceiptLineNbr=LineNbr, ReceiptSplitLineNbr=SplitLineNbr)
PX.Objects.PO.POReceiptSplitToCartSplitLink.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.PO.POReceiptSplitToCartSplitLink.INCartSplitByCartSplitLineNbr -> PX.Objects.IN.INCartSplit (SiteID=SiteID, CartID=CartID, CartSplitLineNbr=SplitLineNbr)
PX.Objects.PO.POReceiptSplitToCartSplitLink.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.PO.POReceiptSplitToTransferSplitLink (EntityType)

Label: "Receipt Line Split To Transfer Line Split Link"
Key: ReceiptLineNbr, ReceiptNbr, ReceiptSplitLineNbr, ReceiptType, TransferDocType, TransferLineNbr, TransferRefNbr, TransferSplitLineNbr
Entity sets: PX_Objects_PO_POReceiptSplitToTransferSplitLink, ReceiptLineSplitToTransferLineSplitLink, POReceiptSplitToTransferSplitLink

PX.Objects.PO.POReceiptSplitToTransferSplitLink.ReceiptType : Edm.String [key]
PX.Objects.PO.POReceiptSplitToTransferSplitLink.ReceiptNbr : Edm.String [key]
PX.Objects.PO.POReceiptSplitToTransferSplitLink.ReceiptLineNbr : Edm.Int32 [key]
PX.Objects.PO.POReceiptSplitToTransferSplitLink.ReceiptSplitLineNbr : Edm.Int32 [key]
PX.Objects.PO.POReceiptSplitToTransferSplitLink.TransferDocType : Edm.String [key]
PX.Objects.PO.POReceiptSplitToTransferSplitLink.TransferRefNbr : Edm.String [key] "Transfer Ref Nbr."
PX.Objects.PO.POReceiptSplitToTransferSplitLink.TransferLineNbr : Edm.Int32 [key]
PX.Objects.PO.POReceiptSplitToTransferSplitLink.TransferSplitLineNbr : Edm.Int32 [key]
PX.Objects.PO.POReceiptSplitToTransferSplitLink.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.PO.POReceiptSplitToTransferSplitLink.INTranByTransferLineNbr -> PX.Objects.IN.INTran (TransferDocType=DocType, TransferRefNbr=RefNbr, TransferLineNbr=LineNbr)
PX.Objects.PO.POReceiptSplitToTransferSplitLink.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.PO.POReceiptSplitToTransferSplitLink.POReceiptLineByReceiptLineNbr -> PX.Objects.PO.POReceiptLine (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr, ReceiptLineNbr=LineNbr)
PX.Objects.PO.POReceiptSplitToTransferSplitLink.POReceiptLineSplitByReceiptSplitLineNbr -> PX.Objects.PO.POReceiptLineSplit (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr, ReceiptLineNbr=LineNbr, ReceiptSplitLineNbr=SplitLineNbr)
PX.Objects.PO.POReceiptSplitToTransferSplitLink.INRegisterByTransferRefNbr -> PX.Objects.IN.INRegister (TransferDocType=DocType, TransferRefNbr=RefNbr)
PX.Objects.PO.POReceiptSplitToTransferSplitLink.INTranSplitByTransferSplitLineNbr -> PX.Objects.IN.INTranSplit (TransferDocType=DocType, TransferRefNbr=RefNbr, TransferLineNbr=LineNbr, TransferSplitLineNbr=SplitLineNbr)

# PX.Objects.PO.POReceiptToShipmentLink (EntityType)

Label: "Purchase Receipt to Shipment Link"
Key: ReceiptNbr, ReceiptType, SOOrderNbr, SOOrderType, SOShipmentNbr, SOShipmentType
Entity sets: PX_Objects_PO_POReceiptToShipmentLink, PurchaseReceipttoShipmentLink, POReceiptToShipmentLink

PX.Objects.PO.POReceiptToShipmentLink.ReceiptType : Edm.String [key] "Receipt Type"
PX.Objects.PO.POReceiptToShipmentLink.ReceiptNbr : Edm.String [key] "Receipt Nbr."
PX.Objects.PO.POReceiptToShipmentLink.SOShipmentType : Edm.String [key] "Shipment Type"
PX.Objects.PO.POReceiptToShipmentLink.SOShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.PO.POReceiptToShipmentLink.SOOrderType : Edm.String [key] "Sales Order Type"
PX.Objects.PO.POReceiptToShipmentLink.SOOrderNbr : Edm.String [key] "Sales Order Nbr."
PX.Objects.PO.POReceiptToShipmentLink.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POReceiptToShipmentLink.CreatedByScreenID : Edm.String
PX.Objects.PO.POReceiptToShipmentLink.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceiptToShipmentLink.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POReceiptToShipmentLink.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POReceiptToShipmentLink.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceiptToShipmentLink.tstamp : Edm.Binary
PX.Objects.PO.POReceiptToShipmentLink.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.PO.POReceiptToShipmentLink.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POReceiptToShipmentLink.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POReceiptToShipmentLink.SOOrderShipmentBySOOrderNbr -> PX.Objects.SO.SOOrderShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr, SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.PO.POReceiptToShipmentLink.SOShipmentBySOShipmentNbr -> PX.Objects.SO.SOShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr)
PX.Objects.PO.POReceiptToShipmentLink.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)

# PX.Objects.PO.POReceivePutAwaySetup (EntityType)

Label: "Receive Put Away Setup"
Key: BranchID
Entity sets: PX_Objects_PO_POReceivePutAwaySetup, ReceivePutAwaySetup, POReceivePutAwaySetup

PX.Objects.PO.POReceivePutAwaySetup.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.PO.POReceivePutAwaySetup.ShowReceivingTab : Edm.Boolean "Display the Receive Tab"
PX.Objects.PO.POReceivePutAwaySetup.ShowReturningTab : Edm.Boolean "Display the Return Tab"
PX.Objects.PO.POReceivePutAwaySetup.ShowPutAwayTab : Edm.Boolean "Display the Put Away Tab"
PX.Objects.PO.POReceivePutAwaySetup.ShowScanLogTab : Edm.Boolean "Display the Scan Log Tab"
PX.Objects.PO.POReceivePutAwaySetup.ShowReceiveTransferTab : Edm.Boolean [required] "Display the Receive Transfer Tab"
PX.Objects.PO.POReceivePutAwaySetup.ExplicitLineConfirmation : Edm.Boolean "Use Explicit Line Confirmation"
PX.Objects.PO.POReceivePutAwaySetup.QtyEnterMode : Edm.String "Quantity Input Mode"
PX.Objects.PO.POReceivePutAwaySetup.RequestLocationForEachItemInReceive : Edm.Boolean [required] "Request Location for Each Item on Receiving"
PX.Objects.PO.POReceivePutAwaySetup.VerifyReceiptsBeforeRelease : Edm.Boolean [required] "Verify Receipts Before Release"
PX.Objects.PO.POReceivePutAwaySetup.VerifyReturnsBeforeRelease : Edm.Boolean [required] "Verify Returns Before Release"
PX.Objects.PO.POReceivePutAwaySetup.KeepZeroLinesOnReceiptConfirmation : Edm.Boolean [required] "Keep Zero Lines on Receipt Confirmation"
PX.Objects.PO.POReceivePutAwaySetup.RequestLocationForEachItemInPutAway : Edm.Boolean [required] "Request Location for Each Item on Putting Away"
PX.Objects.PO.POReceivePutAwaySetup.RequestLocationForEachItemInReturn : Edm.Boolean [required] "Request Location for Each Item on Returning"
PX.Objects.PO.POReceivePutAwaySetup.DefaultReceivingLocation : Edm.Boolean [required] "Use Default Receiving Location"
PX.Objects.PO.POReceivePutAwaySetup.DefaultLotSerialNumber : Edm.Boolean [required] "Use Default Auto-Generated Lot/Serial Nbr."
PX.Objects.PO.POReceivePutAwaySetup.DefaultExpireDate : Edm.Boolean [required] "Use Default Expiration Date"
PX.Objects.PO.POReceivePutAwaySetup.tstamp : Edm.Binary
PX.Objects.PO.POReceivePutAwaySetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POReceivePutAwaySetup.CreatedByScreenID : Edm.String
PX.Objects.PO.POReceivePutAwaySetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceivePutAwaySetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POReceivePutAwaySetup.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POReceivePutAwaySetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POReceivePutAwaySetup.SiteMapByInventoryLabelsReportID -> PX.SM.SiteMap
PX.Objects.PO.POReceivePutAwaySetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POReceivePutAwaySetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PO.POReceivePutAwayUserSetup (EntityType)

Label: "Receive Put Away User Setup"
Key: UserID
Entity sets: PX_Objects_PO_POReceivePutAwayUserSetup, ReceivePutAwayUserSetup, POReceivePutAwayUserSetup

PX.Objects.PO.POReceivePutAwayUserSetup.UserID : Edm.Guid [key] "User"
PX.Objects.PO.POReceivePutAwayUserSetup.IsOverridden : Edm.Boolean [required] "Is Overridden"
PX.Objects.PO.POReceivePutAwayUserSetup.DefaultLotSerialNumber : Edm.Boolean [required] "Use Default Auto-Generated Lot/Serial Nbr."
PX.Objects.PO.POReceivePutAwayUserSetup.DefaultExpireDate : Edm.Boolean [required] "Use Default Expiration Date"
PX.Objects.PO.POReceivePutAwayUserSetup.SiteMapByInventoryLabelsReportID -> PX.SM.SiteMap
PX.Objects.PO.POReceivePutAwayUserSetup.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.PO.POReceivePutAwayUserSetup.SMScaleByScaleDeviceID -> PX.SM.SMScale

# PX.Objects.PO.PORemitAddress (EntityType)

Label: "PO Remittance Address"
BaseType: PX.Objects.PO.POAddress
Key: AddressID (inherited from PX.Objects.PO.POAddress)
Entity sets: PX_Objects_PO_PORemitAddress, PORemittanceAddress, PORemitAddress

# PX.Objects.PO.PORemitContact (EntityType)

Label: "PO Remittance Contact"
BaseType: PX.Objects.PO.POContact
Key: ContactID (inherited from PX.Objects.PO.POContact)
Entity sets: PX_Objects_PO_PORemitContact, PORemittanceContact, PORemitContact

# PX.Objects.PO.POSetup (EntityType)

Label: "Purchasing Preferences"
Singletons: PX_Objects_PO_POSetup, PurchasingPreferences, POSetup

PX.Objects.PO.POSetup.StandardPONumberingID : Edm.String "Blanket Order Numbering Sequence"
PX.Objects.PO.POSetup.RegularPONumberingID : Edm.String "Regular Order Numbering Sequence"
PX.Objects.PO.POSetup.ReceiptNumberingID : Edm.String "Receipt Numbering Sequence"
PX.Objects.PO.POSetup.LandedCostDocNumberingID : Edm.String "Landed Cost Numbering Sequence"
PX.Objects.PO.POSetup.RequireReceiptControlTotal : Edm.Boolean [required] "For Receipts"
PX.Objects.PO.POSetup.RequireOrderControlTotal : Edm.Boolean [required] "For Normal and Standard Orders"
PX.Objects.PO.POSetup.RequireBlanketControlTotal : Edm.Boolean [required] "For Blanket Orders"
PX.Objects.PO.POSetup.RequireDropShipControlTotal : Edm.Boolean [required] "For Drop-Ship Orders"
PX.Objects.PO.POSetup.RequireProjectDropShipControlTotal : Edm.Boolean [required] "For Project Drop-Ship Orders"
PX.Objects.PO.POSetup.RequireLandedCostsControlTotal : Edm.Boolean [required] "For Landed Costs"
PX.Objects.PO.POSetup.HoldReceipts : Edm.Boolean [required] "Hold Receipts on Entry"
PX.Objects.PO.POSetup.HoldLandedCosts : Edm.Boolean [required] "Hold Landed Costs on Entry"
PX.Objects.PO.POSetup.AddServicesFromNormalPOtoPR : Edm.Boolean [required] "Process Service lines from Normal Purchase Orders via Purchase Receipts"
PX.Objects.PO.POSetup.AddServicesFromDSPOtoPR : Edm.Boolean [required] "Process Service lines from Drop-Ship Purchase Orders via Purchase Receipts"
PX.Objects.PO.POSetup.OrderRequestApproval : Edm.Boolean "Require Approval"
PX.Objects.PO.POSetup.DefaultReceiptAssignmentMapID : Edm.Int32 "Receipt Assignment Map"
PX.Objects.PO.POSetup.ReceiptRequestApproval : Edm.Boolean "Require Approval"
PX.Objects.PO.POSetup.AutoCreateInvoiceOnReceipt : Edm.Boolean [required] "Create Bill on Receipt Release"
PX.Objects.PO.POSetup.RCReturnReasonCodeID : Edm.String "PO Return Reason Code"
PX.Objects.PO.POSetup.PPVAllocationMode : Edm.String "Allocation Mode"
PX.Objects.PO.POSetup.PPVReasonCodeID : Edm.String "Reason Code"
PX.Objects.PO.POSetup.AutoReleaseAP : Edm.Boolean [required] "Release AP Documents Automatically"
PX.Objects.PO.POSetup.AutoReleaseIN : Edm.Boolean [required] "Release IN Documents Automatically"
PX.Objects.PO.POSetup.AutoCreateLCAP : Edm.Boolean [required] "Create Bill on LC Release"
PX.Objects.PO.POSetup.AutoReleaseLCIN : Edm.Boolean [required] "Release LC IN Adjustments Automatically"
PX.Objects.PO.POSetup.CopyLineDescrSO : Edm.Boolean [required] "Copy Line Descriptions from Sales Orders"
PX.Objects.PO.POSetup.CopyLineNoteSO : Edm.Boolean [required] "Copy Line Notes from Sales Orders"
PX.Objects.PO.POSetup.ShipDestType : Edm.String "Default Ship Dest. Type"
PX.Objects.PO.POSetup.AutoAddLineReceiptBarcode : Edm.Boolean [required] "Automatically Add Receipt Line for Barcode"
PX.Objects.PO.POSetup.ReceiptByOneBarcodeReceiptBarcode : Edm.Boolean [required] "Add One Unit per Barcode"
PX.Objects.PO.POSetup.ReturnOrigCost : Edm.Boolean [required] "Process Return with Original Cost"
PX.Objects.PO.POSetup.DefaultReceiptQty : Edm.String "Default Receipt Quantity"
PX.Objects.PO.POSetup.CopyLineNotesToReceipt : Edm.Boolean [required] "Copy Line Notes to Receipt"
PX.Objects.PO.POSetup.CopyLineFilesToReceipt : Edm.Boolean [required] "Copy Line Attachments to Receipt"
PX.Objects.PO.POSetup.APInvoiceValidation : Edm.String "Bill Against Commitments"
PX.Objects.PO.POSetup.tstamp : Edm.Binary
PX.Objects.PO.POSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POSetup.CreatedByScreenID : Edm.String
PX.Objects.PO.POSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POSetup.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POSetup.NumberingByStandardPONumberingID -> PX.Objects.CS.Numbering (StandardPONumberingID=NumberingID)
PX.Objects.PO.POSetup.NumberingByRegularPONumberingID -> PX.Objects.CS.Numbering (RegularPONumberingID=NumberingID)
PX.Objects.PO.POSetup.NumberingByReceiptNumberingID -> PX.Objects.CS.Numbering (ReceiptNumberingID=NumberingID)
PX.Objects.PO.POSetup.NumberingByLandedCostDocNumberingID -> PX.Objects.CS.Numbering (LandedCostDocNumberingID=NumberingID)
PX.Objects.PO.POSetup.ReasonCodeByRCReturnReasonCodeID -> PX.Objects.CS.ReasonCode (RCReturnReasonCodeID=ReasonCodeID)
PX.Objects.PO.POSetup.ReasonCodeByTaxReasonCodeID -> PX.Objects.CS.ReasonCode
PX.Objects.PO.POSetup.ReasonCodeByPPVReasonCodeID -> PX.Objects.CS.ReasonCode (PPVReasonCodeID=ReasonCodeID)
PX.Objects.PO.POSetup.AccountByFreightExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PO.POSetup.SubByFreightExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PO.POSetup.EPAssignmentMapByDefaultReceiptAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultReceiptAssignmentMapID=AssignmentMapID)

# PX.Objects.PO.POSetupApproval (EntityType)

Label: "PO Approval"
Key: ApprovalID
Entity sets: PX_Objects_PO_POSetupApproval, POApproval, POSetupApproval

PX.Objects.PO.POSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.PO.POSetupApproval.OrderType : Edm.String "PO Type"
PX.Objects.PO.POSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.PO.POSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.PO.POSetupApproval.tstamp : Edm.Binary
PX.Objects.PO.POSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.PO.POSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POSetupApproval.IsActive : Edm.Boolean
PX.Objects.PO.POSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.PO.POSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.PO.POShipAddress (EntityType)

Label: "PO Shipping Address"
BaseType: PX.Objects.PO.POAddress
Key: AddressID (inherited from PX.Objects.PO.POAddress)
Entity sets: PX_Objects_PO_POShipAddress, POShippingAddress, POShipAddress

# PX.Objects.PO.POShipContact (EntityType)

Label: "PO Shipping Contact"
BaseType: PX.Objects.PO.POContact
Key: ContactID (inherited from PX.Objects.PO.POContact)
Entity sets: PX_Objects_PO_POShipContact, POShippingContact, POShipContact

# PX.Objects.PO.POSiteStatusSelected (EntityType)

Key: InventoryID
Entity sets: PX_Objects_PO_POSiteStatusSelected
Non-filterable, non-selectable: QtySelected, Rank

PX.Objects.PO.POSiteStatusSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.PO.POSiteStatusSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.PO.POSiteStatusSelected.Descr : Edm.String "Description"
PX.Objects.PO.POSiteStatusSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.PO.POSiteStatusSelected.ItemClassCD : Edm.String
PX.Objects.PO.POSiteStatusSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.PO.POSiteStatusSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.PO.POSiteStatusSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.PO.POSiteStatusSelected.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.PO.POSiteStatusSelected.PreferredVendorDescription : Edm.String "Preferred Vendor Name"
PX.Objects.PO.POSiteStatusSelected.BarCode : Edm.String
PX.Objects.PO.POSiteStatusSelected.BarCodeType : Edm.String
PX.Objects.PO.POSiteStatusSelected.BarCodeDescr : Edm.String
PX.Objects.PO.POSiteStatusSelected.AlternateID : Edm.String "Alternate ID"
PX.Objects.PO.POSiteStatusSelected.AlternateType : Edm.String "Alternate Type"
PX.Objects.PO.POSiteStatusSelected.AlternateDescr : Edm.String "Alternate Description"
PX.Objects.PO.POSiteStatusSelected.InventoryAlternateID : Edm.String
PX.Objects.PO.POSiteStatusSelected.InventoryAlternateType : Edm.String
PX.Objects.PO.POSiteStatusSelected.InventoryAlternateDescr : Edm.String
PX.Objects.PO.POSiteStatusSelected.SiteCD : Edm.String
PX.Objects.PO.POSiteStatusSelected.SubItemCD : Edm.String
PX.Objects.PO.POSiteStatusSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.PO.POSiteStatusSelected.PurchaseUnit : Edm.String "Purchase Unit"
PX.Objects.PO.POSiteStatusSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.PO.POSiteStatusSelected.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.PO.POSiteStatusSelected.QtyOnHandExt : Edm.Decimal "Qty. On Hand"
PX.Objects.PO.POSiteStatusSelected.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.PO.POSiteStatusSelected.QtyAvailExt : Edm.Decimal "Qty. Available"
PX.Objects.PO.POSiteStatusSelected.QtyPOPrepared : Edm.Decimal "Qty. PO Prepared"
PX.Objects.PO.POSiteStatusSelected.QtyPOPreparedExt : Edm.Decimal "Qty. PO Prepared"
PX.Objects.PO.POSiteStatusSelected.QtyPOOrders : Edm.Decimal "Qty. PO Orders"
PX.Objects.PO.POSiteStatusSelected.QtyPOOrdersExt : Edm.Decimal "Qty. PO Orders"
PX.Objects.PO.POSiteStatusSelected.QtyPOReceipts : Edm.Decimal "Qty. PO Receipts"
PX.Objects.PO.POSiteStatusSelected.QtyPOReceiptsExt : Edm.Decimal "Qty. PO Receipts"
PX.Objects.PO.POSiteStatusSelected.NoteID : Edm.Guid
PX.Objects.PO.POSiteStatusSelected.Rank : Edm.Int32
PX.Objects.PO.POSiteStatusSelected.CombinedSearchString : Edm.String
PX.Objects.PO.POSiteStatusSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.PO.POSiteStatusSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.PO.POSiteStatusSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.PO.POSiteStatusSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.PO.POTax (EntityType)

Label: "PO Tax Detail"
Key: LineNbr, OrderNbr, OrderType, TaxID
Entity sets: PX_Objects_PO_POTax, POTaxDetail, POTax
Non-filterable, non-selectable: NonDeductibleTaxRate

PX.Objects.PO.POTax.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.PO.POTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.PO.POTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PO.POTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POTax.CreatedByScreenID : Edm.String
PX.Objects.PO.POTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POTax.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POTax.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.POTax.OrderNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PO.POTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PO.POTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PO.POTax.CuryInfoID : Edm.Int64
PX.Objects.PO.POTax.CuryTaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PO.POTax.CuryUnbilledTaxableAmt : Edm.Decimal [required] "Unbilled Taxable Amount"
PX.Objects.PO.POTax.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PO.POTax.UnbilledTaxableAmt : Edm.Decimal [required]
PX.Objects.PO.POTax.UnbilledTaxableQty : Edm.Decimal [required] "Unbilled Taxable Qty."
PX.Objects.PO.POTax.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PO.POTax.CuryUnbilledTaxAmt : Edm.Decimal [required] "Unbilled Tax Amount"
PX.Objects.PO.POTax.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PO.POTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PO.POTax.UnbilledTaxAmt : Edm.Decimal [required]
PX.Objects.PO.POTax.TaxZoneID : Edm.String
PX.Objects.PO.POTax.CuryRetainedTaxableAmt : Edm.Decimal [required] "Retained Taxable"
PX.Objects.PO.POTax.RetainedTaxableAmt : Edm.Decimal [required] "Retained Taxable"
PX.Objects.PO.POTax.CuryRetainedTaxAmt : Edm.Decimal [required] "Retained Tax"
PX.Objects.PO.POTax.RetainedTaxAmt : Edm.Decimal [required] "Retained Tax"
PX.Objects.PO.POTax.POLineByLineNbr -> PX.Objects.PO.POLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.PO.POTax.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PO.POTax.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PO.POTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.PO.POTax.POLineRByLineNbr -> PX.Objects.PO.POLineR (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.PO.POTax.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)

# PX.Objects.PO.POTaxTran (EntityType)

Label: "PO Tax"
Key: LineNbr, OrderNbr, OrderType, RecordID, TaxID
Entity sets: PX_Objects_PO_POTaxTran, POTax1, POTaxTran

PX.Objects.PO.POTaxTran.TaxRate : Edm.Decimal [required] "Tax Rate"
PX.Objects.PO.POTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.PO.POTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PO.POTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POTaxTran.CreatedByScreenID : Edm.String
PX.Objects.PO.POTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POTaxTran.OrderType : Edm.String [key] "Order Type"
PX.Objects.PO.POTaxTran.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.PO.POTaxTran.LineNbr : Edm.Int32 [key required] "Line Nbr."
PX.Objects.PO.POTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.PO.POTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.PO.POTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.PO.POTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.PO.POTaxTran.CuryInfoID : Edm.Int64
PX.Objects.PO.POTaxTran.CuryTaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PO.POTaxTran.CuryUnbilledTaxableAmt : Edm.Decimal [required] "Unbilled Taxable Amount"
PX.Objects.PO.POTaxTran.TaxableAmt : Edm.Decimal [required] "Taxable Amount"
PX.Objects.PO.POTaxTran.UnbilledTaxableAmt : Edm.Decimal [required]
PX.Objects.PO.POTaxTran.UnbilledTaxableQty : Edm.Decimal [required] "Unbilled Taxable Qty."
PX.Objects.PO.POTaxTran.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PO.POTaxTran.CuryUnbilledTaxAmt : Edm.Decimal [required] "Unbilled Tax Amount"
PX.Objects.PO.POTaxTran.TaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.PO.POTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.PO.POTaxTran.UnbilledTaxAmt : Edm.Decimal [required]
PX.Objects.PO.POTaxTran.TaxZoneID : Edm.String
PX.Objects.PO.POTaxTran.tstamp : Edm.Binary
PX.Objects.PO.POTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.PO.POTaxTran.POTaxByTaxID -> PX.Objects.PO.POTax (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr, TaxID=TaxID)
PX.Objects.PO.POTaxTran.POLineByLineNbr -> PX.Objects.PO.POLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.PO.POTaxTran.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.PO.POTaxTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PO.POTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.PO.POTaxTran.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.PO.POTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit

# PX.Objects.PO.POTaxTranImported (EntityType)

Label: "PO Tax"
BaseType: PX.Objects.PO.POTaxTran
Key: LineNbr, OrderNbr, OrderType, RecordID, TaxID (inherited from PX.Objects.PO.POTaxTran)
Entity sets: PX_Objects_PO_POTaxTranImported

# PX.Objects.PO.POVendorInventory (EntityType)

Label: "Inventory Item Vendor Details"
Key: RecordID
Entity sets: PX_Objects_PO_POVendorInventory, InventoryItemVendorDetails, POVendorInventory
Non-filterable, non-selectable: IsDefault, NoteText

PX.Objects.PO.POVendorInventory.RecordID : Edm.Int32 [key]
PX.Objects.PO.POVendorInventory.VendorID : Edm.Int32 "Vendor ID"
PX.Objects.PO.POVendorInventory.AllLocations : Edm.Boolean "All Locations"
PX.Objects.PO.POVendorInventory.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.PO.POVendorInventory.PurchaseUnit : Edm.String "Purchase Unit"
PX.Objects.PO.POVendorInventory.VendorInventoryID : Edm.String "Vendor Inventory ID"
PX.Objects.PO.POVendorInventory.VLeadTime : Edm.Int16 "Vendor Lead Time (Days)"
PX.Objects.PO.POVendorInventory.OverrideSettings : Edm.Boolean [required] "Override"
PX.Objects.PO.POVendorInventory.AddLeadTimeDays : Edm.Int16 [required] "Add. Lead Time (Days)"
PX.Objects.PO.POVendorInventory.Active : Edm.Boolean [required] "Active"
PX.Objects.PO.POVendorInventory.MinOrdFreq : Edm.Int32 "Min. Order Freq.(Days)"
PX.Objects.PO.POVendorInventory.MinOrdQty : Edm.Decimal [required] "Min. Order Qty."
PX.Objects.PO.POVendorInventory.MaxOrdQty : Edm.Decimal [required] "Max Order Qty."
PX.Objects.PO.POVendorInventory.LotSize : Edm.Decimal [required] "Lot Size"
PX.Objects.PO.POVendorInventory.ERQ : Edm.Decimal [required] "EOQ"
PX.Objects.PO.POVendorInventory.LastPrice : Edm.Decimal [required] "Last Vendor Price"
PX.Objects.PO.POVendorInventory.CuryID : Edm.String "Currency ID"
PX.Objects.PO.POVendorInventory.IsDefault : Edm.Boolean "Default"
PX.Objects.PO.POVendorInventory.PrepaymentPct : Edm.Decimal "Prepayment Percent"
PX.Objects.PO.POVendorInventory.NoteID : Edm.Guid
PX.Objects.PO.POVendorInventory.NoteText : Edm.String "Note Text"
PX.Objects.PO.POVendorInventory.tstamp : Edm.Binary
PX.Objects.PO.POVendorInventory.CreatedByID : Edm.Guid "Created By"
PX.Objects.PO.POVendorInventory.CreatedByScreenID : Edm.String
PX.Objects.PO.POVendorInventory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POVendorInventory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PO.POVendorInventory.LastModifiedByScreenID : Edm.String
PX.Objects.PO.POVendorInventory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PO.POVendorInventory.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.PO.POVendorInventory.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PO.POVendorInventory.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.PO.POVendorInventory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PO.POVendorInventory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PO.POVendorInventory.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.PO.POVendorInventory.INUnitByInventoryID -> PX.Objects.IN.INUnit (PurchaseUnit=FromUnit, InventoryID=InventoryID)
PX.Objects.PO.POVendorInventory.INUnitByPurchaseUnit -> PX.Objects.IN.INUnit (PurchaseUnit=FromUnit)
PX.Objects.PO.POVendorInventory.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.POVendorInventory.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.PO.POVendorInventory.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)

# PX.Objects.PO.VendorLocation (EntityType)

Label: "Vendor Location"
Key: BAccountID, LocationID
Entity sets: PX_Objects_PO_VendorLocation, VendorLocation

PX.Objects.PO.VendorLocation.BAccountID : Edm.Int32 [key] "Vendor"
PX.Objects.PO.VendorLocation.AcctCD : Edm.String "Vendor"
PX.Objects.PO.VendorLocation.LocationID : Edm.Int32 [key] "Location"
PX.Objects.PO.VendorLocation.CuryID : Edm.String "Currency"
PX.Objects.PO.VendorLocation.BaseCuryID : Edm.String
PX.Objects.PO.VendorLocation.VSiteID : Edm.Int32 "Warehouse"
PX.Objects.PO.VendorLocation.VLeadTime : Edm.Int16 "Lead Time (Days)"
PX.Objects.PO.VendorLocation.NoteID : Edm.Guid
PX.Objects.PO.VendorLocation.INSiteByVSiteID -> PX.Objects.IN.INSite (VSiteID=SiteID)
PX.Objects.PO.VendorLocation.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.PO.VendorLocation.INSiteByCSiteID -> PX.Objects.IN.INSite
PX.Objects.PO.VendorLocation.CurrencyByPriceListCuryID -> PX.Objects.CM.Currency
PX.Objects.PO.VendorLocation.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)
PX.Objects.PO.VendorLocation.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)

# PX.Objects.Portals.SP.DAC.SPARPayment (EntityType)

Label: "Portal AR Payment"
BaseType: PX.Objects.AR.ARPayment
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_Portals_SP_DAC_SPARPayment, PortalARPayment, SPARPayment

# PX.Objects.Portals.SP.DAC.SPARStatement (EntityType)

Label: "Portal AR Statement"
Key: BranchID, StatementDate
Entity sets: PX_Objects_Portals_SP_DAC_SPARStatement, PortalARStatement, SPARStatement
Non-filterable, non-selectable: StatementDateText

PX.Objects.Portals.SP.DAC.SPARStatement.CustomerID : Edm.Int32 "Customer"
PX.Objects.Portals.SP.DAC.SPARStatement.StatementCustomerID : Edm.Int32
PX.Objects.Portals.SP.DAC.SPARStatement.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.Portals.SP.DAC.SPARStatement.BranchCD : Edm.String "Branch ID"
PX.Objects.Portals.SP.DAC.SPARStatement.AcctName : Edm.String "Branch"
PX.Objects.Portals.SP.DAC.SPARStatement.CuryID : Edm.String "Currency ID"
PX.Objects.Portals.SP.DAC.SPARStatement.BaseCuryID : Edm.String "Currency ID"
PX.Objects.Portals.SP.DAC.SPARStatement.EndBalance : Edm.Decimal "Statement Balance"
PX.Objects.Portals.SP.DAC.SPARStatement.CuryEndBalance : Edm.Decimal "Statement Balance"
PX.Objects.Portals.SP.DAC.SPARStatement.StatementCycleId : Edm.String "Statement Cycle ID"
PX.Objects.Portals.SP.DAC.SPARStatement.StatementDate : Edm.DateTimeOffset [key] "Statement Date"
PX.Objects.Portals.SP.DAC.SPARStatement.StatementDateText : Edm.String "Statement Date"
PX.Objects.Portals.SP.DAC.SPARStatement.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.Portals.SP.DAC.SPARStatement.CustomerByStatementCustomerID -> PX.Objects.AR.Customer (StatementCustomerID=BAccountID)
PX.Objects.Portals.SP.DAC.SPARStatement.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.Portals.SP.DAC.SPARStatement.ARStatementCycleByStatementCycleId -> PX.Objects.AR.ARStatementCycle (StatementCycleId=StatementCycleId)
PX.Objects.Portals.SP.DAC.SPARStatement.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.Portals.SP.DAC.SPARStatement.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)
PX.Objects.Portals.SP.DAC.SPARStatement.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.Objects.Portals.SP.DAC.SPARStatement.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.Portals.SP.DAC.SPARStatement.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.Portals.SP.DAC.SPCRCase (EntityType)

Label: "Portal Case"
BaseType: PX.Objects.CR.CRCase
Key: CaseCD (inherited from PX.Objects.CR.CRCase)
Entity sets: PX_Objects_Portals_SP_DAC_SPCRCase, PortalCase, SPCRCase
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.Portals.SP.DAC.SPCRCase.LastMessage : Edm.String

# PX.Objects.Portals.SP.DAC.SPInventoryCartItem (EntityType)

Label: "Products added to the shopping cart."
Key: RecordID
Entity sets: PX_Objects_Portals_SP_DAC_SPInventoryCartItem, Productsaddedtotheshoppingcart, SPInventoryCartItem
Non-filterable, non-selectable: SiteIDList, UOMList, RemoveFromCart

PX.Objects.Portals.SP.DAC.SPInventoryCartItem.RecordID : Edm.Int32 [key]
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.UserID : Edm.Guid "UserID"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.InventoryID : Edm.Int32 "InventoryID"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.PortalID : Edm.Int32 "PortalID"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.Qty : Edm.Decimal "Qty"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.SiteIDList : Edm.Int32 "Warehouse"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.UOM : Edm.String "Unit"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.UOMList : Edm.String "Unit"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.RemoveFromCart : Edm.String "Remove"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.CreatedByScreenID : Edm.String
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.LastModifiedByScreenID : Edm.String
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.Tstamp : Edm.Binary "Tstamp"
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.Portals.SP.DAC.SPInventoryCartItem.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.Portals.SP.DAC.SPSOOrder (EntityType)

Label: "Portal Sales Order"
BaseType: PX.Objects.SO.SOOrder
Key: OrderNbr, OrderType (inherited from PX.Objects.SO.SOOrder)
Entity sets: PX_Objects_Portals_SP_DAC_SPSOOrder, PortalSalesOrder, SPSOOrder

# PX.Objects.Portals.SPPortal (EntityType)

Label: "Portal Configuration"
Key: PortalName
Entity sets: PX_Objects_Portals_SPPortal, PortalConfiguration, SPPortal
Non-filterable, non-selectable: VisibleWarehouses, VisiblePaymentMethods, PrimaryColor, BackgroundColor, NoteText

PX.Objects.Portals.SPPortal.PortalID : Edm.Int32
PX.Objects.Portals.SPPortal.PortalName : Edm.String [key] "Portal Name"
PX.Objects.Portals.SPPortal.PortalDescription : Edm.String "Portal Description"
PX.Objects.Portals.SPPortal.IsActive : Edm.Boolean "Online"
PX.Objects.Portals.SPPortal.PortalURL : Edm.String "Portal URL"
PX.Objects.Portals.SPPortal.PortalType : Edm.Int32 "Portal Type"
PX.Objects.Portals.SPPortal.LoginTypeID : Edm.Int32 "User Type"
PX.Objects.Portals.SPPortal.AccessRole : Edm.String "Portal Access Role"
PX.Objects.Portals.SPPortal.DefaultOrderType : Edm.String "Sales Order Type"
PX.Objects.Portals.SPPortal.DefaultStockItemWareHouse : Edm.Int32 "Default Stock Item Warehouse"
PX.Objects.Portals.SPPortal.DefaultNonStockItemWareHouse : Edm.Int32 "Default Non-Stock Item Warehouse"
PX.Objects.Portals.SPPortal.VisibleWarehouses : Edm.String "Visible Warehouses"
PX.Objects.Portals.SPPortal.DisplayAvailableQuantities : Edm.Boolean "Show Available Quantities"
PX.Objects.Portals.SPPortal.AllowOnlySalesUnitForPurchase : Edm.Boolean "Allow Only Sales Unit for Purchase"
PX.Objects.Portals.SPPortal.VisiblePaymentMethods : Edm.String "Payment Methods"
PX.Objects.Portals.SPPortal.SecurityContactID : Edm.Int32 "Security Contact"
PX.Objects.Portals.SPPortal.NotifyOnFinancialManagerRoleAssignment : Edm.Boolean [required] "Notify on Financial Manager Role Assignment"
PX.Objects.Portals.SPPortal.NotifyOnPaymentInstructionChanges : Edm.Boolean [required] "Notify on Payment Instruction Changes"
PX.Objects.Portals.SPPortal.CaseClassID : Edm.String "Default Case Class"
PX.Objects.Portals.SPPortal.CaseActivityNotificationTemplateID : Edm.Int32 "Case Notification Template"
PX.Objects.Portals.SPPortal.ContactClassID : Edm.String "Default Contact Class"
PX.Objects.Portals.SPPortal.ProcessingCenterID : Edm.String "Processing Center"
PX.Objects.Portals.SPPortal.CCPaymentMethodID : Edm.String "Default CC Payment Method"
PX.Objects.Portals.SPPortal.EFTPaymentMethodID : Edm.String "Default EFT Payment Method"
PX.Objects.Portals.SPPortal.InterfaceTheme : Edm.String "Interface Theme"
PX.Objects.Portals.SPPortal.PortalLogo : Edm.String "Portal Logo"
PX.Objects.Portals.SPPortal.CompanyNameToDisplay : Edm.String "Company Name to Display"
PX.Objects.Portals.SPPortal.SignInPageImage : Edm.String "Sign-In Page Image"
PX.Objects.Portals.SPPortal.PrimaryColor : Edm.String "Primary Color"
PX.Objects.Portals.SPPortal.BackgroundColor : Edm.String "Background Color"
PX.Objects.Portals.SPPortal.AddressLookupPluginID : Edm.String "Address Lookup Plug-In"
PX.Objects.Portals.SPPortal.DefaultScreenID : Edm.String "Default Home Form"
PX.Objects.Portals.SPPortal.ShowNavigation : Edm.Boolean [required] "Display Navigation Panels"
PX.Objects.Portals.SPPortal.ShowTopMessage : Edm.Boolean [required] "Display Top Message"
PX.Objects.Portals.SPPortal.TopMessageImage : Edm.String "Top Message Image"
PX.Objects.Portals.SPPortal.TopMessageText : Edm.String "Top Message Text"
PX.Objects.Portals.SPPortal.ShowGoToCartButton : Edm.Boolean [required] "Display Go to Catalog Button"
PX.Objects.Portals.SPPortal.GoToCartImage : Edm.String "Go to Catalog Image"
PX.Objects.Portals.SPPortal.GoToCartText : Edm.String "Go to Catalog Text"
PX.Objects.Portals.SPPortal.CreatedByID : Edm.Guid "Created By"
PX.Objects.Portals.SPPortal.CreatedByScreenID : Edm.String
PX.Objects.Portals.SPPortal.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Objects.Portals.SPPortal.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Portals.SPPortal.LastModifiedByScreenID : Edm.String
PX.Objects.Portals.SPPortal.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.Portals.SPPortal.Tstamp : Edm.Binary "Tstamp"
PX.Objects.Portals.SPPortal.NoteID : Edm.Guid
PX.Objects.Portals.SPPortal.NoteText : Edm.String "Note Text"
PX.Objects.Portals.SPPortal.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.Portals.SPPortal.CRContactClassByContactClassID -> PX.Objects.CR.CRContactClass (ContactClassID=ClassID)
PX.Objects.Portals.SPPortal.ContactBySecurityContactID -> PX.Objects.CR.Contact (SecurityContactID=ContactID)
PX.Objects.Portals.SPPortal.BranchByRestrictByBranchID -> PX.Objects.GL.Branch
PX.Objects.Portals.SPPortal.BranchByDefaultBranchID -> PX.Objects.GL.Branch
PX.Objects.Portals.SPPortal.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Portals.SPPortal.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.Portals.SPPortal.NotificationByCaseActivityNotificationTemplateID -> PX.SM.Notification (CaseActivityNotificationTemplateID=NotificationID)
PX.Objects.Portals.SPPortal.EPLoginTypeByLoginTypeID -> PX.EP.EPLoginType (LoginTypeID=LoginTypeID)
PX.Objects.Portals.SPPortal.RolesByAccessRole -> PX.SM.Roles (AccessRole=Rolename)
PX.Objects.Portals.SPPortal.OrganizationByRestrictByOrganizationID -> PX.Objects.GL.DAC.Organization
PX.Objects.Portals.SPPortal.SOOrderTypeByDefaultOrderType -> PX.Objects.SO.SOOrderType (DefaultOrderType=OrderType)
PX.Objects.Portals.SPPortal.AddressValidatorPluginByAddressLookupPluginID -> PX.Objects.CS.AddressValidatorPlugin (AddressLookupPluginID=AddressValidatorPluginID)
PX.Objects.Portals.SPPortal.CashAccountByDefaultBranchID -> PX.Objects.CA.CashAccount
PX.Objects.Portals.SPPortal.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.Portals.SPPortal.PaymentMethodByCcPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.Objects.Portals.SPPortal.PaymentMethodByEftPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.Objects.Portals.SPPortal.CRCaseClassByCaseClassID -> PX.Objects.CR.CRCaseClass (CaseClassID=CaseClassID)
PX.Objects.Portals.SPPortal.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)

# PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent (EntityType)

Label: "Vendor Portal Compliance Notification Event"
Key: NotificationEventID
Entity sets: PX_Objects_Portals_Vendor_Configuration_VPComplianceNotificationEvent, VendorPortalComplianceNotificationEvent, VPComplianceNotificationEvent
Non-filterable, non-selectable: NoteText

PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.NotificationEventID : Edm.Int32 [key]
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.OwnerContactID : Edm.Int32
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.OwnerName : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.OwnerEmail : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.DocumentType : Edm.String "Document Type"
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.DocumentRefNbr : Edm.String "Reference Nbr."
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.DocumentLink : Edm.String "Document Link"
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.OrderType : Edm.String "Order Type"
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.OrderNbr : Edm.String "Order Nbr."
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.OrderNoteID : Edm.Guid
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.EventDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.CreatedByID : Edm.Guid "Created By"
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.CreatedByScreenID : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.LastModifiedByScreenID : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.Tstamp : Edm.Binary
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.NoteID : Edm.Guid
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.NoteText : Edm.String "Note Text"
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.ContactByOwnerContactID -> PX.Objects.CR.Contact (OwnerContactID=ContactID)
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent (EntityType)

Label: "Vendor Portal Security Notification Event"
Key: NotificationEventID
Entity sets: PX_Objects_Portals_Vendor_Configuration_VPSecurityNotificationEvent, VendorPortalSecurityNotificationEvent, VPSecurityNotificationEvent
Non-filterable, non-selectable: NoteText

PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.NotificationEventID : Edm.Int32 [key]
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.EventType : Edm.String "Event Type"
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.PortalID : Edm.Int32 "Portal ID"
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.SecurityContactID : Edm.Int32
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.SecurityContactName : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.SecurityContactEmail : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.VendorID : Edm.Int32 "Vendor ID"
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.VendorName : Edm.String "Vendor"
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.ActorUserID : Edm.Guid
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.ActorDisplayName : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.ExternalUserID : Edm.Guid
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.ExternalUserDisplayName : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.EventDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.CreatedByID : Edm.Guid "Created By"
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.CreatedByScreenID : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.LastModifiedByScreenID : Edm.String
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.Tstamp : Edm.Binary
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.NoteID : Edm.Guid
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.NoteText : Edm.String "Note Text"
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.ContactBySecurityContactID -> PX.Objects.CR.Contact (SecurityContactID=ContactID)
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.UsersByActorUserID -> PX.SM.Users (ActorUserID=PKID)
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.UsersByExternalUserID -> PX.SM.Users (ExternalUserID=PKID)
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent.SPPortalByPortalID -> PX.Objects.Portals.SPPortal (PortalID=PortalID)

# PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity (EntityType)

Label: "Recent Activity"
Key: ActivityID
Entity sets: PX_Objects_Portals_Vendor_Dashboard_RecentActivities_VPRecentActivity, RecentActivity, VPRecentActivity
Non-filterable, non-selectable: StatusIcon, TimeAgo

PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.ActivityID : Edm.Guid [key]
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.ActivityType : Edm.String
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.EntityType : Edm.String "Entity Type"
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.EntityNoteID : Edm.Guid "Entity Note ID"
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.VendorID : Edm.Int32
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.EntityNbr : Edm.String
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.Status : Edm.String "Status"
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.StatusIcon : Edm.String
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.Description : Edm.String "Description"
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.Currency : Edm.String "Currency"
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.Amount : Edm.Decimal "Amount"
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.TimeAgo : Edm.String
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.CreatedByID : Edm.Guid "Created By"
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.CreatedByScreenID : Edm.String
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.LastModifiedByScreenID : Edm.String
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.Tstamp : Edm.Binary
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Portals.Vendor.Dashboard.RecentActivities.VPRecentActivity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState (EntityType)

Label: "User To Do State"
Key: EntityNoteID
Entity sets: PX_Objects_Portals_Vendor_Dashboard_ToDo_VPToDoState, UserToDoState, VPToDoState

PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.EntityNoteID : Edm.Guid [key] "Entity Note ID"
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.Completed : Edm.Boolean [required] "Completed"
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.CreatedByID : Edm.Guid "Created By"
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.CreatedByScreenID : Edm.String
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.LastModifiedByScreenID : Edm.String
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.Tstamp : Edm.Binary
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Portals.Vendor.Dashboard.ToDo.VPToDoState.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PRAcaAggregateGroupMember (EntityType)

Label: "ACA Aggregate Group Member"
Key: MemberEin, OrgBAccountID, Year
Entity sets: PX_Objects_PR_PRAcaAggregateGroupMember, ACAAggregateGroupMember, PRAcaAggregateGroupMember

PX.Objects.PR.PRAcaAggregateGroupMember.BranchID : Edm.Int32
PX.Objects.PR.PRAcaAggregateGroupMember.OrgBAccountID : Edm.Int32 [key] "OrgBAccountID"
PX.Objects.PR.PRAcaAggregateGroupMember.Year : Edm.String [key] "Year"
PX.Objects.PR.PRAcaAggregateGroupMember.MemberCompanyName : Edm.String "Account Name"
PX.Objects.PR.PRAcaAggregateGroupMember.MemberEin : Edm.String [key] "Member EIN"
PX.Objects.PR.PRAcaAggregateGroupMember.HighestMonthlyFteNumber : Edm.Int32 "Highest Monthly FTE Number"
PX.Objects.PR.PRAcaAggregateGroupMember.TStamp : Edm.Binary
PX.Objects.PR.PRAcaAggregateGroupMember.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRAcaAggregateGroupMember.CreatedByScreenID : Edm.String
PX.Objects.PR.PRAcaAggregateGroupMember.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaAggregateGroupMember.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRAcaAggregateGroupMember.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRAcaAggregateGroupMember.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaAggregateGroupMember.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRAcaAggregateGroupMember.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRAcaAggregateGroupMember.OrganizationByOrgBAccountID -> PX.Objects.GL.DAC.Organization (OrgBAccountID=OrganizationID)
PX.Objects.PR.PRAcaAggregateGroupMember.PRAcaCompanyYearlyInformationByYear -> PX.Objects.PR.PRAcaCompanyYearlyInformation (OrgBAccountID=OrgBAccountID, Year=Year)
PX.Objects.PR.PRAcaAggregateGroupMember.PRAcaCompanyYearlyInformationByOrgBAccountID -> PX.Objects.PR.PRAcaCompanyYearlyInformation (Year=Year, OrgBAccountID=OrgBAccountID)

# PX.Objects.PR.PRAcaCompanyMonthlyInformation (EntityType)

Label: "ACA Company Monthly Information"
Key: Month, OrgBAccountID, Year
Entity sets: PX_Objects_PR_PRAcaCompanyMonthlyInformation, ACACompanyMonthlyInformation, PRAcaCompanyMonthlyInformation

PX.Objects.PR.PRAcaCompanyMonthlyInformation.BranchID : Edm.Int32
PX.Objects.PR.PRAcaCompanyMonthlyInformation.OrgBAccountID : Edm.Int32 [key] "OrgBAccountID"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.Year : Edm.String [key] "Year"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.Month : Edm.Int32 [key] "Month"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.NumberOfFte : Edm.Int32 "Nbr. FTE"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.NumberOfEmployees : Edm.Int32 "Nbr. Employees"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.PctEmployeesCoveredByMec : Edm.Decimal "% of Employees Covered by MEC"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.CertificationOfEligibility : Edm.String "Certification of Eligibility"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.SelfInsured : Edm.Boolean [required] "Self-Insured"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.Numberof1095C : Edm.Int32 "Nbr. of 1095-C Forms"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.TStamp : Edm.Binary
PX.Objects.PR.PRAcaCompanyMonthlyInformation.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.CreatedByScreenID : Edm.String
PX.Objects.PR.PRAcaCompanyMonthlyInformation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaCompanyMonthlyInformation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRAcaCompanyMonthlyInformation.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRAcaCompanyMonthlyInformation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaCompanyMonthlyInformation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRAcaCompanyMonthlyInformation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRAcaCompanyMonthlyInformation.OrganizationByOrgBAccountID -> PX.Objects.GL.DAC.Organization (OrgBAccountID=OrganizationID)
PX.Objects.PR.PRAcaCompanyMonthlyInformation.PRAcaCompanyYearlyInformationByYear -> PX.Objects.PR.PRAcaCompanyYearlyInformation (OrgBAccountID=OrgBAccountID, Year=Year)
PX.Objects.PR.PRAcaCompanyMonthlyInformation.PRAcaCompanyYearlyInformationByOrgBAccountID -> PX.Objects.PR.PRAcaCompanyYearlyInformation (Year=Year, OrgBAccountID=OrgBAccountID)

# PX.Objects.PR.PRAcaCompanyYearlyInformation (EntityType)

Label: "ACA Company Yearly Information"
Key: OrgBAccountID, Year
Entity sets: PX_Objects_PR_PRAcaCompanyYearlyInformation, ACACompanyYearlyInformation, PRAcaCompanyYearlyInformation
Non-filterable, non-selectable: Ein, HeaderDescription

PX.Objects.PR.PRAcaCompanyYearlyInformation.BranchID : Edm.Int32
PX.Objects.PR.PRAcaCompanyYearlyInformation.OrgBAccountID : Edm.Int32 [key] "Company/Branch"
PX.Objects.PR.PRAcaCompanyYearlyInformation.Year : Edm.String [key] "Year"
PX.Objects.PR.PRAcaCompanyYearlyInformation.IsPartOfAggregateGroup : Edm.Boolean [required] "Part of an Aggregate Group"
PX.Objects.PR.PRAcaCompanyYearlyInformation.IsAuthoritativeTransmittal : Edm.Boolean "Authoritative Transmittal"
PX.Objects.PR.PRAcaCompanyYearlyInformation.Ein : Edm.String "Tax Registration Number"
PX.Objects.PR.PRAcaCompanyYearlyInformation.HeaderDescription : Edm.String
PX.Objects.PR.PRAcaCompanyYearlyInformation.TStamp : Edm.Binary
PX.Objects.PR.PRAcaCompanyYearlyInformation.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRAcaCompanyYearlyInformation.CreatedByScreenID : Edm.String
PX.Objects.PR.PRAcaCompanyYearlyInformation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaCompanyYearlyInformation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRAcaCompanyYearlyInformation.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRAcaCompanyYearlyInformation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaCompanyYearlyInformation.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount (OrgBAccountID=BAccountID)
PX.Objects.PR.PRAcaCompanyYearlyInformation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRAcaCompanyYearlyInformation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRAcaCompanyYearlyInformation.OrganizationByOrgBAccountID -> PX.Objects.GL.DAC.Organization (OrgBAccountID=OrganizationID)
PX.Objects.PR.PRAcaCompanyYearlyInformation.PRPayGroupYearByYear -> PX.Objects.PR.PRPayGroupYear (Year=Year)
PX.Objects.PR.PRAcaCompanyYearlyInformation.PRAcaAggregateGroupMemberCollection -> Collection(PX.Objects.PR.PRAcaAggregateGroupMember)
PX.Objects.PR.PRAcaCompanyYearlyInformation.PRAcaCompanyMonthlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyMonthlyInformation)
PX.Objects.PR.PRAcaCompanyYearlyInformation.PRAcaEmployeeMonthlyInformationCollection -> Collection(PX.Objects.PR.PRAcaEmployeeMonthlyInformation)

# PX.Objects.PR.PRAcaDeductCoverageInfo (EntityType)

Label: "ACA Deduction Code Coverage Information"
Key: CoverageType, DeductCodeID
Entity sets: PX_Objects_PR_PRAcaDeductCoverageInfo, ACADeductionCodeCoverageInformation, PRAcaDeductCoverageInfo

PX.Objects.PR.PRAcaDeductCoverageInfo.DeductCodeID : Edm.Int32 [key] "Code ID"
PX.Objects.PR.PRAcaDeductCoverageInfo.CoverageType : Edm.String [key] "Coverage Type"
PX.Objects.PR.PRAcaDeductCoverageInfo.HealthPlanType : Edm.String "Health Plan Type"
PX.Objects.PR.PRAcaDeductCoverageInfo.TStamp : Edm.Binary
PX.Objects.PR.PRAcaDeductCoverageInfo.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRAcaDeductCoverageInfo.CreatedByScreenID : Edm.String
PX.Objects.PR.PRAcaDeductCoverageInfo.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaDeductCoverageInfo.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRAcaDeductCoverageInfo.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRAcaDeductCoverageInfo.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaDeductCoverageInfo.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRAcaDeductCoverageInfo.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRAcaDeductCoverageInfo.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)

# PX.Objects.PR.PRAcaEmployeeMonthlyInformation (EntityType)

Label: "ACA Employee Monthly Information"
Key: EmployeeID, Month, OrgBAccountID, Year
Entity sets: PX_Objects_PR_PRAcaEmployeeMonthlyInformation, ACAEmployeeMonthlyInformation, PRAcaEmployeeMonthlyInformation

PX.Objects.PR.PRAcaEmployeeMonthlyInformation.BranchID : Edm.Int32
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.OrgBAccountID : Edm.Int32 [key] "OrgBAccountID"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.Year : Edm.String [key] "Year"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.Month : Edm.Int32 [key] "Month"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.FTStatus : Edm.String "ACA FT Status"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.OfferOfCoverage : Edm.String "Offer of Coverage"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.Section4980H : Edm.String "Section 4980H"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.MinimumIndividualContribution : Edm.Decimal "Minimum Individual Contribution"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.HoursWorked : Edm.Decimal "Number of Hours Worked"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.SelfInsured : Edm.Boolean "Self-Insured"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.TStamp : Edm.Binary
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.CreatedByScreenID : Edm.String
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.OrganizationByOrgBAccountID -> PX.Objects.GL.DAC.Organization (OrgBAccountID=OrganizationID)
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.PRAcaCompanyYearlyInformationByYear -> PX.Objects.PR.PRAcaCompanyYearlyInformation (OrgBAccountID=OrgBAccountID, Year=Year)
PX.Objects.PR.PRAcaEmployeeMonthlyInformation.PRAcaCompanyYearlyInformationByOrgBAccountID -> PX.Objects.PR.PRAcaCompanyYearlyInformation (Year=Year, OrgBAccountID=OrgBAccountID)

# PX.Objects.PR.PRBandingRulePTOBank (EntityType)

Label: "Banding Rules"
Key: RecordID
Entity sets: PX_Objects_PR_PRBandingRulePTOBank, BandingRules, PRBandingRulePTOBank

PX.Objects.PR.PRBandingRulePTOBank.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRBandingRulePTOBank.EmployeeClassID : Edm.String "Employee Class"
PX.Objects.PR.PRBandingRulePTOBank.BankID : Edm.String "PTO Bank"
PX.Objects.PR.PRBandingRulePTOBank.YearsOfService : Edm.Int32 "Years of Service"
PX.Objects.PR.PRBandingRulePTOBank.AccrualRate : Edm.Decimal [required] "Accrual %"
PX.Objects.PR.PRBandingRulePTOBank.AccrualLimit : Edm.Decimal "Balance Limit"
PX.Objects.PR.PRBandingRulePTOBank.HoursPerYear : Edm.Decimal [required] "Hours per Year"
PX.Objects.PR.PRBandingRulePTOBank.CarryoverAmount : Edm.Decimal "Carryover Hours"
PX.Objects.PR.PRBandingRulePTOBank.FrontLoadingAmount : Edm.Decimal "Front Loading Hours"
PX.Objects.PR.PRBandingRulePTOBank.TStamp : Edm.Binary
PX.Objects.PR.PRBandingRulePTOBank.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRBandingRulePTOBank.CreatedByScreenID : Edm.String
PX.Objects.PR.PRBandingRulePTOBank.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBandingRulePTOBank.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRBandingRulePTOBank.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRBandingRulePTOBank.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBandingRulePTOBank.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRBandingRulePTOBank.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRBandingRulePTOBank.PREmployeeClassByEmployeeClassID -> PX.Objects.PR.PREmployeeClass (EmployeeClassID=EmployeeClassID)
PX.Objects.PR.PRBandingRulePTOBank.PRPTOBankByBankID -> PX.Objects.PR.PRPTOBank (BankID=BankID)

# PX.Objects.PR.PRBatch (EntityType)

Label: "Batch"
Key: BatchNbr
Entity sets: PX_Objects_PR_PRBatch, Batch1, PRBatch
Non-filterable, non-selectable: IsWeeklyOrBiWeeklyPeriod, NoteText, HeaderDescription

PX.Objects.PR.PRBatch.BatchNbr : Edm.String [key] "Batch ID"
PX.Objects.PR.PRBatch.Status : Edm.String "Status"
PX.Objects.PR.PRBatch.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PR.PRBatch.Open : Edm.Boolean [required]
PX.Objects.PR.PRBatch.Closed : Edm.Boolean [required]
PX.Objects.PR.PRBatch.PayrollType : Edm.String "Payroll Type"
PX.Objects.PR.PRBatch.PayGroupID : Edm.String "Pay Group"
PX.Objects.PR.PRBatch.DocDesc : Edm.String "Description"
PX.Objects.PR.PRBatch.IsWeeklyOrBiWeeklyPeriod : Edm.Boolean "Is Weekly or Biweekly Period"
PX.Objects.PR.PRBatch.PayPeriodID : Edm.String "Pay Period"
PX.Objects.PR.PRBatch.StartDate : Edm.DateTimeOffset "Period Start"
PX.Objects.PR.PRBatch.EndDate : Edm.DateTimeOffset "Period End"
PX.Objects.PR.PRBatch.TransactionDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.PR.PRBatch.NumberOfEmployees : Edm.Int32 "Number of Employees"
PX.Objects.PR.PRBatch.TotalHourQty : Edm.Decimal [required] "Total Hour Qty"
PX.Objects.PR.PRBatch.ApplyOvertimeRules : Edm.Boolean [required] "Apply Overtime Rules for the Document"
PX.Objects.PR.PRBatch.TotalEarnings : Edm.Decimal [required] "Total Earnings"
PX.Objects.PR.PRBatch.NoteID : Edm.Guid
PX.Objects.PR.PRBatch.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRBatch.HeaderDescription : Edm.String
PX.Objects.PR.PRBatch.TStamp : Edm.Binary
PX.Objects.PR.PRBatch.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRBatch.CreatedByScreenID : Edm.String
PX.Objects.PR.PRBatch.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRBatch.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRBatch.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRBatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRBatch.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup (PayGroupID=PayGroupID)
PX.Objects.PR.PRBatch.PRPayGroupPeriodByPayPeriodID -> PX.Objects.PR.PRPayGroupPeriod (PayGroupID=PayGroupID, PayPeriodID=FinPeriodID)
PX.Objects.PR.PRBatch.PRPayGroupPeriodByPayGroupID -> PX.Objects.PR.PRPayGroupPeriod (PayPeriodID=FinPeriodID, PayGroupID=PayGroupID)
PX.Objects.PR.PRBatch.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.PR.PRBatch.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PR.PRBatch.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PR.PRBatch.PRBatchEmployeeCollection -> Collection(PX.Objects.PR.PRBatchEmployee)
PX.Objects.PR.PRBatch.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PR.PRBatch.PRBatchDeductCollection -> Collection(PX.Objects.PR.PRBatchDeduct)
PX.Objects.PR.PRBatch.PRBatchOvertimeRuleCollection -> Collection(PX.Objects.PR.PRBatchOvertimeRule)
PX.Objects.PR.PRBatch.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)

# PX.Objects.PR.PRBatchDeduct (EntityType)

Label: "Batch Deduction"
Key: BatchNbr, CodeID
Entity sets: PX_Objects_PR_PRBatchDeduct, BatchDeduction, PRBatchDeduct

PX.Objects.PR.PRBatchDeduct.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.PR.PRBatchDeduct.CodeID : Edm.Int32 [key] "Deduction Code"
PX.Objects.PR.PRBatchDeduct.IsEnabled : Edm.Boolean [required] "Enabled"
PX.Objects.PR.PRBatchDeduct.TStamp : Edm.Binary
PX.Objects.PR.PRBatchDeduct.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRBatchDeduct.CreatedByScreenID : Edm.String
PX.Objects.PR.PRBatchDeduct.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBatchDeduct.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRBatchDeduct.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRBatchDeduct.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBatchDeduct.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRBatchDeduct.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRBatchDeduct.PRDeductCodeByCodeID -> PX.Objects.PR.PRDeductCode (CodeID=CodeID)
PX.Objects.PR.PRBatchDeduct.PRBatchByBatchNbr -> PX.Objects.PR.PRBatch (BatchNbr=BatchNbr)

# PX.Objects.PR.PRBatchEmployee (EntityType)

Label: "Batch Employee"
Key: BatchNbr, EmployeeID
Entity sets: PX_Objects_PR_PRBatchEmployee, BatchEmployee, PRBatchEmployee
Non-filterable, non-selectable: BatchStatus, PaymentRefNbr, PaymentDocAndRef, VoidPaymentDocAndRef, HasNegativeHoursEarnings

PX.Objects.PR.PRBatchEmployee.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.PR.PRBatchEmployee.BatchStatus : Edm.String "BatchStatus"
PX.Objects.PR.PRBatchEmployee.EmployeeID : Edm.Int32 [key]
PX.Objects.PR.PRBatchEmployee.EmpType : Edm.String "Employee Type"
PX.Objects.PR.PRBatchEmployee.HourQty : Edm.Decimal [required] "Hours"
PX.Objects.PR.PRBatchEmployee.Rate : Edm.Decimal "Rate"
PX.Objects.PR.PRBatchEmployee.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRBatchEmployee.RegularAmount : Edm.Decimal "Regular Amount to Be Paid"
PX.Objects.PR.PRBatchEmployee.ManualRegularAmount : Edm.Boolean [required] "Manual Amount"
PX.Objects.PR.PRBatchEmployee.PaymentRefNbr : Edm.String
PX.Objects.PR.PRBatchEmployee.PaymentDocAndRef : Edm.String "Paycheck Ref"
PX.Objects.PR.PRBatchEmployee.VoidPaymentDocAndRef : Edm.String "Void Paycheck Ref"
PX.Objects.PR.PRBatchEmployee.HasNegativeHoursEarnings : Edm.Boolean
PX.Objects.PR.PRBatchEmployee.AcctCD : Edm.String "Employee"
PX.Objects.PR.PRBatchEmployee.AcctName : Edm.String "Employee Name"
PX.Objects.PR.PRBatchEmployee.ParentBAccountID : Edm.Int32
PX.Objects.PR.PRBatchEmployee.BranchID : Edm.Int32
PX.Objects.PR.PRBatchEmployee.PayGroupID : Edm.String
PX.Objects.PR.PRBatchEmployee.EmployeeCountryID : Edm.String
PX.Objects.PR.PRBatchEmployee.TStamp : Edm.Binary
PX.Objects.PR.PRBatchEmployee.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRBatchEmployee.CreatedByScreenID : Edm.String
PX.Objects.PR.PRBatchEmployee.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBatchEmployee.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRBatchEmployee.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRBatchEmployee.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBatchEmployee.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRBatchEmployee.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRBatchEmployee.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRBatchEmployee.PRBatchByBatchNbr -> PX.Objects.PR.PRBatch (BatchNbr=BatchNbr)

# PX.Objects.PR.PRBatchOvertimeRule (EntityType)

Label: "Batch Overtime Rule"
Key: BatchNbr, OvertimeRuleID
Entity sets: PX_Objects_PR_PRBatchOvertimeRule, BatchOvertimeRule, PRBatchOvertimeRule
Non-filterable, non-selectable: RuleType

PX.Objects.PR.PRBatchOvertimeRule.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.PR.PRBatchOvertimeRule.OvertimeRuleID : Edm.String [key] "Overtime Rule"
PX.Objects.PR.PRBatchOvertimeRule.RuleType : Edm.String "RuleType"
PX.Objects.PR.PRBatchOvertimeRule.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PRBatchOvertimeRule.TStamp : Edm.Binary
PX.Objects.PR.PRBatchOvertimeRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRBatchOvertimeRule.CreatedByScreenID : Edm.String
PX.Objects.PR.PRBatchOvertimeRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBatchOvertimeRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRBatchOvertimeRule.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRBatchOvertimeRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBatchOvertimeRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRBatchOvertimeRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRBatchOvertimeRule.PRBatchByBatchNbr -> PX.Objects.PR.PRBatch (BatchNbr=BatchNbr)
PX.Objects.PR.PRBatchOvertimeRule.PROvertimeRuleByOvertimeRuleID -> PX.Objects.PR.PROvertimeRule (OvertimeRuleID=OvertimeRuleID)

# PX.Objects.PR.PRBenefitDetail (EntityType)

Label: "Benefit Detail"
Key: RecordID
Entity sets: PX_Objects_PR_PRBenefitDetail, BenefitDetail, PRBenefitDetail
Non-filterable, non-selectable: IsPayableBenefit, PaymentCountryID

PX.Objects.PR.PRBenefitDetail.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRBenefitDetail.OriginalRecordID : Edm.Int32
PX.Objects.PR.PRBenefitDetail.EmployeeID : Edm.Int32 "Employee"
PX.Objects.PR.PRBenefitDetail.BatchNbr : Edm.String "Batch Number"
PX.Objects.PR.PRBenefitDetail.PaymentDocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRBenefitDetail.PaymentRefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRBenefitDetail.CodeID : Edm.Int32 "Code"
PX.Objects.PR.PRBenefitDetail.IsPayableBenefit : Edm.Boolean "IsPayableBenefit"
PX.Objects.PR.PRBenefitDetail.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRBenefitDetail.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRBenefitDetail.EarningTypeCD : Edm.String "Earning Type Code"
PX.Objects.PR.PRBenefitDetail.Released : Edm.Boolean [required] "Released"
PX.Objects.PR.PRBenefitDetail.APInvoiceDocType : Edm.String "Type"
PX.Objects.PR.PRBenefitDetail.APInvoiceRefNbr : Edm.String "Reference Nbr."
PX.Objects.PR.PRBenefitDetail.LiabilityPaid : Edm.Boolean [required] "Liability Paid"
PX.Objects.PR.PRBenefitDetail.PaymentCountryID : Edm.String
PX.Objects.PR.PRBenefitDetail.TStamp : Edm.Binary
PX.Objects.PR.PRBenefitDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRBenefitDetail.CreatedByScreenID : Edm.String
PX.Objects.PR.PRBenefitDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBenefitDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRBenefitDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRBenefitDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRBenefitDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PRBenefitDetail.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRBenefitDetail.APInvoiceByApInvoiceRefNbr -> PX.Objects.AP.APInvoice
PX.Objects.PR.PRBenefitDetail.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRBenefitDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRBenefitDetail.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.PR.PRBenefitDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRBenefitDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRBenefitDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRBenefitDetail.PRDeductCodeByCodeID -> PX.Objects.PR.PRDeductCode (CodeID=CodeID)
PX.Objects.PR.PRBenefitDetail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PR.PRBenefitDetail.AccountByExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PRBenefitDetail.AccountByLiabilityAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PRBenefitDetail.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRBenefitDetail.SubByLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRBenefitDetail.EPEarningTypeByEarningTypeCD -> PX.Objects.EP.EPEarningType (EarningTypeCD=TypeCD)
PX.Objects.PR.PRBenefitDetail.PRBatchByBatchNbr -> PX.Objects.PR.PRBatch (BatchNbr=BatchNbr)
PX.Objects.PR.PRBenefitDetail.PRPaymentByPaymentRefNbr -> PX.Objects.PR.PRPayment (PaymentDocType=DocType, PaymentRefNbr=RefNbr)
PX.Objects.PR.PRBenefitDetail.PRPaymentDeductByCodeID -> PX.Objects.PR.PRPaymentDeduct (PaymentDocType=DocType, PaymentRefNbr=RefNbr, CodeID=CodeID)

# PX.Objects.PR.PRCABatch (EntityType)

Label: "CA Batch for Payroll"
BaseType: PX.Objects.CA.CABatch
Key: BatchNbr (inherited from PX.Objects.CA.CABatch)
Entity sets: PX_Objects_PR_PRCABatch, CABatchforPayroll, PRCABatch
Non-filterable, non-selectable: BatchTotal, HeaderDescription

PX.Objects.PR.PRCABatch.PRPrintChecks : Edm.Boolean "PRPrintChecks"
PX.Objects.PR.PRCABatch.BatchTotal : Edm.Decimal "Batch Total"
PX.Objects.PR.PRCABatch.PaymentTotal : Edm.Decimal "PaymentTotal"
PX.Objects.PR.PRCABatch.DirectDepositSplitTotal : Edm.Decimal "DirectDepositSplitTotal"
PX.Objects.PR.PRCABatch.HeaderDescription : Edm.String

# PX.Objects.PR.PRCompanyTaxAttribute (EntityType)

Label: "Company Tax Setting"
Key: SettingName
Entity sets: PX_Objects_PR_PRCompanyTaxAttribute, CompanyTaxSetting, PRCompanyTaxAttribute
Non-filterable, non-selectable: Description, AllowOverride, UseDefault, UsedForGovernmentReporting, NoteText, ErrorLevel, SettingLevelEnabled, FEINDisplaySetting, IsTaxAgency

PX.Objects.PR.PRCompanyTaxAttribute.TypeName : Edm.String "Type"
PX.Objects.PR.PRCompanyTaxAttribute.SettingName : Edm.String [key] "Setting"
PX.Objects.PR.PRCompanyTaxAttribute.Description : Edm.String "Description"
PX.Objects.PR.PRCompanyTaxAttribute.State : Edm.String "State"
PX.Objects.PR.PRCompanyTaxAttribute.CountryID : Edm.String
PX.Objects.PR.PRCompanyTaxAttribute.IsEncryptionRequired : Edm.Boolean [required]
PX.Objects.PR.PRCompanyTaxAttribute.IsEncrypted : Edm.Boolean [required]
PX.Objects.PR.PRCompanyTaxAttribute.CanadaReportMapping : Edm.Int32 "CanadaReportMapping"
PX.Objects.PR.PRCompanyTaxAttribute.Value : Edm.String "Default Value"
PX.Objects.PR.PRCompanyTaxAttribute.AllowOverride : Edm.Boolean
PX.Objects.PR.PRCompanyTaxAttribute.SettingLevel : Edm.String "Setting Level"
PX.Objects.PR.PRCompanyTaxAttribute.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.PR.PRCompanyTaxAttribute.Required : Edm.Boolean [required] "Required"
PX.Objects.PR.PRCompanyTaxAttribute.UseDefault : Edm.Boolean
PX.Objects.PR.PRCompanyTaxAttribute.AatrixMapping : Edm.Int32 "AatrixMapping"
PX.Objects.PR.PRCompanyTaxAttribute.AdditionalInformation : Edm.String "Additional Information"
PX.Objects.PR.PRCompanyTaxAttribute.UsedForTaxCalculation : Edm.Boolean [required] "Used for Tax Calculation"
PX.Objects.PR.PRCompanyTaxAttribute.UsedForGovernmentReporting : Edm.Boolean "Used for Government Reporting"
PX.Objects.PR.PRCompanyTaxAttribute.FormBox : Edm.String "Form/Box"
PX.Objects.PR.PRCompanyTaxAttribute.NoteID : Edm.Guid
PX.Objects.PR.PRCompanyTaxAttribute.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRCompanyTaxAttribute.ErrorLevel : Edm.Int32
PX.Objects.PR.PRCompanyTaxAttribute.TaxesInState : Edm.Int32
PX.Objects.PR.PRCompanyTaxAttribute.SettingLevelEnabled : Edm.Boolean "Setting Level Enabled"
PX.Objects.PR.PRCompanyTaxAttribute.IsEmployeeSpecific : Edm.Boolean [required]
PX.Objects.PR.PRCompanyTaxAttribute.FEINDisplaySetting : Edm.Int32
PX.Objects.PR.PRCompanyTaxAttribute.IsTaxAgency : Edm.Boolean
PX.Objects.PR.PRCompanyTaxAttribute.TStamp : Edm.Binary
PX.Objects.PR.PRCompanyTaxAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRCompanyTaxAttribute.CreatedByScreenID : Edm.String
PX.Objects.PR.PRCompanyTaxAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRCompanyTaxAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRCompanyTaxAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRCompanyTaxAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRCompanyTaxAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRCompanyTaxAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRCompanyTaxAttribute.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.PRCompanyTaxAttribute.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.PR.PRCompanyTaxAttribute.PREmployeeAttributeCollection -> Collection(PX.Objects.PR.PREmployeeAttribute)

# PX.Objects.PR.PRCRAPayrollAccount (EntityType)

Label: "CRA Payroll Account"
Key: PayrollAccountID
Entity sets: PX_Objects_PR_PRCRAPayrollAccount, CRAPayrollAccount, PRCRAPayrollAccount

PX.Objects.PR.PRCRAPayrollAccount.PayrollAccountID : Edm.Int32 [key]
PX.Objects.PR.PRCRAPayrollAccount.PayrollAccountCD : Edm.String "CRA Payroll Account Number"
PX.Objects.PR.PRCRAPayrollAccount.IsT4ATaxReportingNumber : Edm.Boolean [required] "T4A"
PX.Objects.PR.PRCRAPayrollAccount.BAccountID : Edm.Int32
PX.Objects.PR.PRCRAPayrollAccount.SetAsDefault : Edm.Boolean [required] "Set as Default"
PX.Objects.PR.PRCRAPayrollAccount.TStamp : Edm.Binary
PX.Objects.PR.PRCRAPayrollAccount.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRCRAPayrollAccount.CreatedByScreenID : Edm.String
PX.Objects.PR.PRCRAPayrollAccount.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRCRAPayrollAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRCRAPayrollAccount.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRCRAPayrollAccount.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRCRAPayrollAccount.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.PR.PRCRAPayrollAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRCRAPayrollAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRCRAPayrollAccount.PREIPremiumRateCollection -> Collection(PX.Objects.PR.PREIPremiumRate)

# PX.Objects.PR.PRDeductCode (EntityType)

Label: "Deduction Code"
Key: CodeCD
Entity sets: PX_Objects_PR_PRDeductCode, DeductionCode, PRDeductCode
Non-filterable, non-selectable: ShowApplicableWageTab, ShowGarnishmentNetIncomeTab, AssociatedSource, ShowUSTaxSettingsTab, ShowCANTaxSettingsTab, NoteText

PX.Objects.PR.PRDeductCode.CodeID : Edm.Int32 "Code ID"
PX.Objects.PR.PRDeductCode.CodeCD : Edm.String [key] "Code"
PX.Objects.PR.PRDeductCode.Description : Edm.String "Description"
PX.Objects.PR.PRDeductCode.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PRDeductCode.IsGarnishment : Edm.Boolean [required] "Garnishment"
PX.Objects.PR.PRDeductCode.AffectsTaxes : Edm.Boolean "Affects Tax Calculation"
PX.Objects.PR.PRDeductCode.ContribType : Edm.String "Contribution Type"
PX.Objects.PR.PRDeductCode.BAccountID : Edm.Int32 "Vendor"
PX.Objects.PR.PRDeductCode.IncludeType : Edm.String "Impact on Taxable Wage"
PX.Objects.PR.PRDeductCode.BenefitTypeCD : Edm.Int32 "Code Type"
PX.Objects.PR.PRDeductCode.BenefitCalculationMethod : Edm.Int32 "Calculation Method"
PX.Objects.PR.PRDeductCode.DedCalcType : Edm.String "Calculation Method"
PX.Objects.PR.PRDeductCode.DedAmount : Edm.Decimal "Amount"
PX.Objects.PR.PRDeductCode.DedPercent : Edm.Decimal "Percent"
PX.Objects.PR.PRDeductCode.DedMaxAmount : Edm.Decimal "Limit Amount"
PX.Objects.PR.PRDeductCode.DedMaxFreqType : Edm.String "Limit Frequency"
PX.Objects.PR.PRDeductCode.DedApplicableEarnings : Edm.String "Applicable Earnings"
PX.Objects.PR.PRDeductCode.DedReportType : Edm.Int32 "Reporting Type"
PX.Objects.PR.PRDeductCode.CntCalcType : Edm.String "Calculation Method"
PX.Objects.PR.PRDeductCode.CntAmount : Edm.Decimal "Amount"
PX.Objects.PR.PRDeductCode.CntPercent : Edm.Decimal "Percent"
PX.Objects.PR.PRDeductCode.CntMaxAmount : Edm.Decimal "Limit Amount"
PX.Objects.PR.PRDeductCode.CntMaxFreqType : Edm.String "Limit Frequency"
PX.Objects.PR.PRDeductCode.CntApplicableEarnings : Edm.String "Applicable Earnings"
PX.Objects.PR.PRDeductCode.CntReportType : Edm.Int32 "Reporting Type"
PX.Objects.PR.PRDeductCode.ContributesToGrossCalculation : Edm.Boolean [required] "Contributes to Gross Calculation"
PX.Objects.PR.PRDeductCode.ContributesToBenefitApplicableWage : Edm.Boolean [required] "Contributes to Benefit Applicable Wage"
PX.Objects.PR.PRDeductCode.DedInvDescrType : Edm.String "Invoice Description Source"
PX.Objects.PR.PRDeductCode.VndInvDescr : Edm.String "Vendor Invoice Description"
PX.Objects.PR.PRDeductCode.IsWorkersCompensation : Edm.Boolean [required]
PX.Objects.PR.PRDeductCode.IsCertifiedProject : Edm.Boolean [required]
PX.Objects.PR.PRDeductCode.IsUnion : Edm.Boolean [required]
PX.Objects.PR.PRDeductCode.IsPayableBenefit : Edm.Boolean [required] "Payable Benefit"
PX.Objects.PR.PRDeductCode.State : Edm.String "State"
PX.Objects.PR.PRDeductCode.CountryID : Edm.String "CountryID"
PX.Objects.PR.PRDeductCode.CertifiedReportType : Edm.Int32 "Certified Reporting Type"
PX.Objects.PR.PRDeductCode.EarningsIncreasingWageIncludeType : Edm.String "Inclusion Type"
PX.Objects.PR.PRDeductCode.BenefitsIncreasingWageIncludeType : Edm.String "Inclusion Type"
PX.Objects.PR.PRDeductCode.TaxesIncreasingWageIncludeType : Edm.String "Inclusion Type"
PX.Objects.PR.PRDeductCode.DeductionsDecreasingWageIncludeType : Edm.String "Inclusion Type"
PX.Objects.PR.PRDeductCode.TaxesDecreasingWageIncludeType : Edm.String "Inclusion Type"
PX.Objects.PR.PRDeductCode.NoFinancialTransaction : Edm.Boolean [required] "No Financial Transaction"
PX.Objects.PR.PRDeductCode.AllowSupplementalElection : Edm.Boolean [required] "Include Supplemental Earnings"
PX.Objects.PR.PRDeductCode.DedReportTypeCAN : Edm.Int32 "Federal Reporting Type"
PX.Objects.PR.PRDeductCode.CntReportTypeCAN : Edm.Int32 "Federal Reporting Type"
PX.Objects.PR.PRDeductCode.DedQuebecReportTypeCAN : Edm.Int32 "Quebec Reporting Type"
PX.Objects.PR.PRDeductCode.CntQuebecReportTypeCAN : Edm.Int32 "Quebec Reporting Type"
PX.Objects.PR.PRDeductCode.ShowApplicableWageTab : Edm.Boolean "ShowApplicableWageTab"
PX.Objects.PR.PRDeductCode.ShowGarnishmentNetIncomeTab : Edm.Boolean "ShowGarnishmentNetIncomeTab"
PX.Objects.PR.PRDeductCode.AssociatedSource : Edm.String "Associated With"
PX.Objects.PR.PRDeductCode.ShowUSTaxSettingsTab : Edm.Boolean
PX.Objects.PR.PRDeductCode.ShowCANTaxSettingsTab : Edm.Boolean
PX.Objects.PR.PRDeductCode.NoteID : Edm.Guid
PX.Objects.PR.PRDeductCode.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRDeductCode.WorkCodeID : Edm.String "Workers' Compensation Code"
PX.Objects.PR.PRDeductCode.TStamp : Edm.Binary
PX.Objects.PR.PRDeductCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductCode.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductCode.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductCode.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductCode.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCode.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PRDeductCode.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.PR.PRDeductCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductCode.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)
PX.Objects.PR.PRDeductCode.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.PRDeductCode.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.PR.PRDeductCode.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.PR.PRDeductCode.AccountByDedLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRDeductCode.AccountByBenefitExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRDeductCode.AccountByBenefitLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRDeductCode.SubByDedLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRDeductCode.SubByBenefitExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRDeductCode.SubByBenefitLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRDeductCode.PRDeductCodeDetailCollection -> Collection(PX.Objects.PR.PRDeductCodeDetail)
PX.Objects.PR.PRDeductCode.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.PR.PRDeductCode.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PR.PRDeductCode.PRAcaDeductCoverageInfoCollection -> Collection(PX.Objects.PR.PRAcaDeductCoverageInfo)
PX.Objects.PR.PRDeductCode.PRBatchDeductCollection -> Collection(PX.Objects.PR.PRBatchDeduct)
PX.Objects.PR.PRDeductCode.PRDeductCodeBenefitIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeBenefitIncreasingWage)
PX.Objects.PR.PRDeductCode.PRDeductCodeDeductionDecreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeDeductionDecreasingWage)
PX.Objects.PR.PRDeductCode.PRDeductCodeEarningIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeEarningIncreasingWage)
PX.Objects.PR.PRDeductCode.PRDeductCodeTaxDecreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxDecreasingWage)
PX.Objects.PR.PRDeductCode.PRDeductCodeTaxIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxIncreasingWage)
PX.Objects.PR.PRDeductCode.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.PR.PRDeductCode.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.PR.PRDeductCode.PRDeductionsReducingDisposableNetCollection -> Collection(PX.Objects.PR.PRDeductionsReducingDisposableNet)
PX.Objects.PR.PRDeductCode.PREmployeeDeductCollection -> Collection(PX.Objects.PR.PREmployeeDeduct)
PX.Objects.PR.PRDeductCode.PRNonPayableBenefitsIncreasingDisposableNetCollection -> Collection(PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet)
PX.Objects.PR.PRDeductCode.PRPaymentDeductCollection -> Collection(PX.Objects.PR.PRPaymentDeduct)
PX.Objects.PR.PRDeductCode.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.PR.PRDeductCode.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.PR.PRDeductCode.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.PR.PRDeductCode.PRPaymentWCPremiumCollection -> Collection(PX.Objects.PR.PRPaymentWCPremium)
PX.Objects.PR.PRDeductCode.PRProjectFringeBenefitRateReducingDeductCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct)
PX.Objects.PR.PRDeductCode.PRWorkCompensationBenefitRateCollection -> Collection(PX.Objects.PR.PRWorkCompensationBenefitRate)
PX.Objects.PR.PRDeductCode.PRWorkCompensationMaximumInsurableWageCollection -> Collection(PX.Objects.PR.PRWorkCompensationMaximumInsurableWage)
PX.Objects.PR.PRDeductCode.PRYtdDeductionsCollection -> Collection(PX.Objects.PR.PRYtdDeductions)

# PX.Objects.PR.PRDeductCodeBenefitIncreasingWage (EntityType)

Label: "Deduct Code Benefit Increasing Wage"
Key: ApplicableBenefitCodeID, DeductCodeID
Entity sets: PX_Objects_PR_PRDeductCodeBenefitIncreasingWage, DeductCodeBenefitIncreasingWage, PRDeductCodeBenefitIncreasingWage

PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.DeductCodeID : Edm.Int32 [key]
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.ApplicableBenefitCodeID : Edm.Int32 [key] "Benefit Code"
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.ApplicableBenefitCodeCountryID : Edm.String
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.TStamp : Edm.Binary
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRDeductCodeBenefitIncreasingWage.PRDeductCodeByApplicableBenefitCodeID -> PX.Objects.PR.PRDeductCode (ApplicableBenefitCodeID=CodeID)

# PX.Objects.PR.PRDeductCodeDeductionDecreasingWage (EntityType)

Label: "Deduct Code Deduction Decreasing Wage"
Key: ApplicableDeductionCodeID, DeductCodeID
Entity sets: PX_Objects_PR_PRDeductCodeDeductionDecreasingWage, DeductCodeDeductionDecreasingWage, PRDeductCodeDeductionDecreasingWage

PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.DeductCodeID : Edm.Int32 [key]
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.ApplicableDeductionCodeID : Edm.Int32 [key] "Deduction Code"
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.ApplicableDeductionCodeCountryID : Edm.String
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.TStamp : Edm.Binary
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRDeductCodeDeductionDecreasingWage.PRDeductCodeByApplicableDeductionCodeID -> PX.Objects.PR.PRDeductCode (ApplicableDeductionCodeID=CodeID)

# PX.Objects.PR.PRDeductCodeDetail (EntityType)

Label: "Deduction Code Taxability"
Key: CodeID, TaxID
Entity sets: PX_Objects_PR_PRDeductCodeDetail, DeductionCodeTaxability, PRDeductCodeDetail

PX.Objects.PR.PRDeductCodeDetail.CodeID : Edm.Int32 [key] "Code ID"
PX.Objects.PR.PRDeductCodeDetail.TaxID : Edm.Int32 [key] "Tax ID"
PX.Objects.PR.PRDeductCodeDetail.TStamp : Edm.Binary
PX.Objects.PR.PRDeductCodeDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductCodeDetail.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductCodeDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductCodeDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductCodeDetail.PRDeductCodeByCodeID -> PX.Objects.PR.PRDeductCode (CodeID=CodeID)
PX.Objects.PR.PRDeductCodeDetail.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)

# PX.Objects.PR.PRDeductCodeEarningIncreasingWage (EntityType)

Label: "Deduct Code Earning Increasing Wage"
Key: ApplicableTypeCD, DeductCodeID
Entity sets: PX_Objects_PR_PRDeductCodeEarningIncreasingWage, DeductCodeEarningIncreasingWage, PRDeductCodeEarningIncreasingWage

PX.Objects.PR.PRDeductCodeEarningIncreasingWage.DeductCodeID : Edm.Int32 [key]
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.ApplicableTypeCD : Edm.String [key] "Earning Type Code"
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.TStamp : Edm.Binary
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRDeductCodeEarningIncreasingWage.EPEarningTypeByApplicableTypeCD -> PX.Objects.EP.EPEarningType (ApplicableTypeCD=TypeCD)

# PX.Objects.PR.PRDeductCodeTaxDecreasingWage (EntityType)

Label: "Deduct Code Tax Decreasing Wage"
Key: ApplicableTaxID, DeductCodeID
Entity sets: PX_Objects_PR_PRDeductCodeTaxDecreasingWage, DeductCodeTaxDecreasingWage, PRDeductCodeTaxDecreasingWage

PX.Objects.PR.PRDeductCodeTaxDecreasingWage.DeductCodeID : Edm.Int32 [key]
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.ApplicableTaxID : Edm.Int32 [key] "Tax Code"
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.TStamp : Edm.Binary
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRDeductCodeTaxDecreasingWage.PRTaxCodeByApplicableTaxID -> PX.Objects.PR.PRTaxCode (ApplicableTaxID=TaxID)

# PX.Objects.PR.PRDeductCodeTaxIncreasingWage (EntityType)

Label: "Deduct Code Tax Increasing Wage"
Key: ApplicableTaxID, DeductCodeID
Entity sets: PX_Objects_PR_PRDeductCodeTaxIncreasingWage, DeductCodeTaxIncreasingWage, PRDeductCodeTaxIncreasingWage

PX.Objects.PR.PRDeductCodeTaxIncreasingWage.DeductCodeID : Edm.Int32 [key]
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.ApplicableTaxID : Edm.Int32 [key] "Tax Code"
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.TStamp : Edm.Binary
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRDeductCodeTaxIncreasingWage.PRTaxCodeByApplicableTaxID -> PX.Objects.PR.PRTaxCode (ApplicableTaxID=TaxID)

# PX.Objects.PR.PRDeductionAndBenefitProjectPackage (EntityType)

Label: "Deductions And Benefits Project Package"
Key: RecordID
Entity sets: PX_Objects_PR_PRDeductionAndBenefitProjectPackage, DeductionsAndBenefitsProjectPackage, PRDeductionAndBenefitProjectPackage
Non-filterable, non-selectable: CountryUS

PX.Objects.PR.PRDeductionAndBenefitProjectPackage.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.ProjectID : Edm.Int32
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.DeductionAndBenefitCodeID : Edm.Int32 "Deduction and Benefit Code"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.DeductionAmount : Edm.Decimal "Deduction Amount"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.DeductionRate : Edm.Decimal "Deduction Percent"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.BenefitAmount : Edm.Decimal "Contribution Amount"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.BenefitRate : Edm.Decimal "Contribution Percent"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.CountryUS : Edm.String
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.TStamp : Edm.Binary
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductionAndBenefitProjectPackage.PRDeductCodeByDeductionAndBenefitCodeID -> PX.Objects.PR.PRDeductCode (DeductionAndBenefitCodeID=CodeID)

# PX.Objects.PR.PRDeductionAndBenefitUnionPackage (EntityType)

Label: "Deductions And Benefits Union Package"
Key: RecordID
Entity sets: PX_Objects_PR_PRDeductionAndBenefitUnionPackage, DeductionsAndBenefitsUnionPackage, PRDeductionAndBenefitUnionPackage

PX.Objects.PR.PRDeductionAndBenefitUnionPackage.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.UnionID : Edm.String
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.DeductionAndBenefitCodeID : Edm.Int32 "Deduction and Benefit Code"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.DeductionAmount : Edm.Decimal "Deduction Amount"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.DeductionRate : Edm.Decimal "Deduction Percent"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.BenefitAmount : Edm.Decimal "Contribution Amount"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.BenefitRate : Edm.Decimal "Contribution Percent"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.TStamp : Edm.Binary
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.PRDeductCodeByDeductionAndBenefitCodeID -> PX.Objects.PR.PRDeductCode (DeductionAndBenefitCodeID=CodeID)
PX.Objects.PR.PRDeductionAndBenefitUnionPackage.PMUnionByUnionID -> PX.Objects.PM.PMUnion (UnionID=UnionID)

# PX.Objects.PR.PRDeductionDetail (EntityType)

Label: "Deduction Details"
Key: RecordID
Entity sets: PX_Objects_PR_PRDeductionDetail, DeductionDetails, PRDeductionDetail
Non-filterable, non-selectable: PaymentCountryID

PX.Objects.PR.PRDeductionDetail.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRDeductionDetail.OriginalRecordID : Edm.Int32
PX.Objects.PR.PRDeductionDetail.EmployeeID : Edm.Int32 "Employee"
PX.Objects.PR.PRDeductionDetail.BatchNbr : Edm.String "Batch Number"
PX.Objects.PR.PRDeductionDetail.PaymentDocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRDeductionDetail.PaymentRefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRDeductionDetail.CodeID : Edm.Int32 "Code"
PX.Objects.PR.PRDeductionDetail.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRDeductionDetail.Released : Edm.Boolean [required] "Released"
PX.Objects.PR.PRDeductionDetail.APInvoiceDocType : Edm.String "Type"
PX.Objects.PR.PRDeductionDetail.APInvoiceRefNbr : Edm.String "Reference Nbr."
PX.Objects.PR.PRDeductionDetail.LiabilityPaid : Edm.Boolean [required] "Liability Paid"
PX.Objects.PR.PRDeductionDetail.PaymentCountryID : Edm.String
PX.Objects.PR.PRDeductionDetail.TStamp : Edm.Binary
PX.Objects.PR.PRDeductionDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductionDetail.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductionDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductionDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductionDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductionDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductionDetail.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRDeductionDetail.APInvoiceByApInvoiceRefNbr -> PX.Objects.AP.APInvoice
PX.Objects.PR.PRDeductionDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRDeductionDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductionDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductionDetail.PRDeductCodeByCodeID -> PX.Objects.PR.PRDeductCode (CodeID=CodeID)
PX.Objects.PR.PRDeductionDetail.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PRDeductionDetail.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRDeductionDetail.PRBatchByBatchNbr -> PX.Objects.PR.PRBatch (BatchNbr=BatchNbr)
PX.Objects.PR.PRDeductionDetail.PRPaymentByPaymentRefNbr -> PX.Objects.PR.PRPayment (PaymentDocType=DocType, PaymentRefNbr=RefNbr)
PX.Objects.PR.PRDeductionDetail.PRPaymentDeductByCodeID -> PX.Objects.PR.PRPaymentDeduct (PaymentDocType=DocType, PaymentRefNbr=RefNbr, CodeID=CodeID)

# PX.Objects.PR.PRDeductionsReducingDisposableNet (EntityType)

Label: "Deductions Reducing Disposable Net Income"
Key: ApplicableDeductionCodeID, DeductCodeID
Entity sets: PX_Objects_PR_PRDeductionsReducingDisposableNet, DeductionsReducingDisposableNetIncome, PRDeductionsReducingDisposableNet

PX.Objects.PR.PRDeductionsReducingDisposableNet.DeductCodeID : Edm.Int32 [key]
PX.Objects.PR.PRDeductionsReducingDisposableNet.ApplicableDeductionCodeID : Edm.Int32 [key] "Deduction Code"
PX.Objects.PR.PRDeductionsReducingDisposableNet.TStamp : Edm.Binary
PX.Objects.PR.PRDeductionsReducingDisposableNet.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDeductionsReducingDisposableNet.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDeductionsReducingDisposableNet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductionsReducingDisposableNet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDeductionsReducingDisposableNet.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDeductionsReducingDisposableNet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDeductionsReducingDisposableNet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDeductionsReducingDisposableNet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDeductionsReducingDisposableNet.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRDeductionsReducingDisposableNet.PRDeductCodeByApplicableDeductionCodeID -> PX.Objects.PR.PRDeductCode (ApplicableDeductionCodeID=CodeID)

# PX.Objects.PR.PRDirectDepositSplit (EntityType)

Label: "Direct Deposit Split"
Key: DocType, LineNbr, RefNbr
Entity sets: PX_Objects_PR_PRDirectDepositSplit, DirectDepositSplit, PRDirectDepositSplit

PX.Objects.PR.PRDirectDepositSplit.DocType : Edm.String [key] "Payment Type"
PX.Objects.PR.PRDirectDepositSplit.RefNbr : Edm.String [key] "Payment Reference Nbr."
PX.Objects.PR.PRDirectDepositSplit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PR.PRDirectDepositSplit.BankAcctNbr : Edm.String "Account Nbr."
PX.Objects.PR.PRDirectDepositSplit.BankRoutingNbr : Edm.String "Bank Routing Nbr."
PX.Objects.PR.PRDirectDepositSplit.BankAcctType : Edm.String "Type"
PX.Objects.PR.PRDirectDepositSplit.BankName : Edm.String "Bank Name"
PX.Objects.PR.PRDirectDepositSplit.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRDirectDepositSplit.CATranID : Edm.Int64
PX.Objects.PR.PRDirectDepositSplit.Released : Edm.Boolean [required]
PX.Objects.PR.PRDirectDepositSplit.BankTransitNbrCan : Edm.String "Bank Transit Number"
PX.Objects.PR.PRDirectDepositSplit.FinInstNbrCan : Edm.String "Financial Institution Number"
PX.Objects.PR.PRDirectDepositSplit.BankAcctNbrCan : Edm.String "Bank Account Number"
PX.Objects.PR.PRDirectDepositSplit.BeneficiaryName : Edm.String "Beneficiary Name"
PX.Objects.PR.PRDirectDepositSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRDirectDepositSplit.CreatedByScreenID : Edm.String
PX.Objects.PR.PRDirectDepositSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDirectDepositSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRDirectDepositSplit.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRDirectDepositSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRDirectDepositSplit.CATranByCaTranID -> PX.Objects.CA.CATran
PX.Objects.PR.PRDirectDepositSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRDirectDepositSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRDirectDepositSplit.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.PR.PREarningDetail (EntityType)

Label: "Earning Detail"
Key: RecordID
Entity sets: PX_Objects_PR_PREarningDetail, EarningDetail, PREarningDetail
Non-filterable, non-selectable: ExcelRecordID, SortingRecordID, AllowCopy, IsOvertime, IsPiecework, IsAmountBased, PTODisbursementWithFinancialTransaction, PTODisbursementWithAverageRate

PX.Objects.PR.PREarningDetail.RecordID : Edm.Int32 [key]
PX.Objects.PR.PREarningDetail.ExcelRecordID : Edm.String "Record ID"
PX.Objects.PR.PREarningDetail.BaseOvertimeRecordID : Edm.Int32 "Base RecordID"
PX.Objects.PR.PREarningDetail.BasePTORecordID : Edm.Int32
PX.Objects.PR.PREarningDetail.SortingRecordID : Edm.Int32 "Sorting RecordID"
PX.Objects.PR.PREarningDetail.AllowCopy : Edm.Boolean "AllowCopy"
PX.Objects.PR.PREarningDetail.EmployeeID : Edm.Int32
PX.Objects.PR.PREarningDetail.BatchNbr : Edm.String "Batch Number"
PX.Objects.PR.PREarningDetail.PaymentDocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PREarningDetail.PaymentRefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PREarningDetail.Date : Edm.DateTimeOffset "Date"
PX.Objects.PR.PREarningDetail.TypeCD : Edm.String "Code"
PX.Objects.PR.PREarningDetail.IsOvertime : Edm.Boolean "Overtime"
PX.Objects.PR.PREarningDetail.IsPiecework : Edm.Boolean "Piecework"
PX.Objects.PR.PREarningDetail.IsAmountBased : Edm.Boolean "Amount-Based"
PX.Objects.PR.PREarningDetail.LocationID : Edm.Int32 "Location"
PX.Objects.PR.PREarningDetail.Hours : Edm.Decimal "Hours"
PX.Objects.PR.PREarningDetail.Units : Edm.Decimal "Units"
PX.Objects.PR.PREarningDetail.UnitType : Edm.String "Unit Type"
PX.Objects.PR.PREarningDetail.Rate : Edm.Decimal "Rate"
PX.Objects.PR.PREarningDetail.ManualRate : Edm.Boolean [required] "Manual Rate"
PX.Objects.PR.PREarningDetail.IsRegularRate : Edm.Boolean [required] "IsRegularRate"
PX.Objects.PR.PREarningDetail.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PREarningDetail.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PREarningDetail.Released : Edm.Boolean [required] "Released"
PX.Objects.PR.PREarningDetail.SourceType : Edm.String "Data Source Type"
PX.Objects.PR.PREarningDetail.SourceNoteID : Edm.Guid "Time Activity"
PX.Objects.PR.PREarningDetail.TimeCardMinutes : Edm.Int32
PX.Objects.PR.PREarningDetail.SourceCommnPeriod : Edm.String "Source Commn Period"
PX.Objects.PR.PREarningDetail.UnionID : Edm.String "Union Local"
PX.Objects.PR.PREarningDetail.CertifiedJob : Edm.Boolean "Certified Job"
PX.Objects.PR.PREarningDetail.WorkCodeID : Edm.String "WCC Code"
PX.Objects.PR.PREarningDetail.IsFringeRateEarning : Edm.Boolean [required] "IsFringeRateEarning"
PX.Objects.PR.PREarningDetail.EmployeeAcctCD : Edm.String
PX.Objects.PR.PREarningDetail.IsPayingSettlement : Edm.Boolean [required] "IsPayingSettlement"
PX.Objects.PR.PREarningDetail.TStamp : Edm.Binary
PX.Objects.PR.PREarningDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREarningDetail.CreatedByScreenID : Edm.String
PX.Objects.PR.PREarningDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREarningDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREarningDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREarningDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREarningDetail.PTODisbursementWithFinancialTransaction : Edm.Boolean
PX.Objects.PR.PREarningDetail.PTODisbursementWithAverageRate : Edm.Boolean
PX.Objects.PR.PREarningDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PREarningDetail.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PREarningDetail.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PR.PREarningDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PR.PREarningDetail.PMTimeActivityBySourceNoteID -> PX.Objects.CR.PMTimeActivity (SourceNoteID=NoteID)
PX.Objects.PR.PREarningDetail.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.PR.PREarningDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PREarningDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREarningDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREarningDetail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PR.PREarningDetail.PMUnionByUnionID -> PX.Objects.PM.PMUnion (UnionID=UnionID)
PX.Objects.PR.PREarningDetail.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)
PX.Objects.PR.PREarningDetail.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PREarningDetail.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREarningDetail.EPEarningTypeByTypeCD -> PX.Objects.EP.EPEarningType (TypeCD=TypeCD)
PX.Objects.PR.PREarningDetail.EPShiftCodeByShiftID -> PX.Objects.EP.EPShiftCode
PX.Objects.PR.PREarningDetail.PRBatchByBatchNbr -> PX.Objects.PR.PRBatch (BatchNbr=BatchNbr)
PX.Objects.PR.PREarningDetail.PRLocationByLocationID -> PX.Objects.PR.PRLocation (LocationID=LocationID)
PX.Objects.PR.PREarningDetail.PRPaymentByPaymentRefNbr -> PX.Objects.PR.PRPayment (PaymentDocType=DocType, PaymentRefNbr=RefNbr)
PX.Objects.PR.PREarningDetail.PRPaymentEarningByLocationID -> PX.Objects.PR.PRPaymentEarning (PaymentDocType=DocType, PaymentRefNbr=RefNbr, TypeCD=TypeCD, LocationID=LocationID)

# PX.Objects.PR.PREarningTypeDetail (EntityType)

Label: "Earning Type Detail"
Key: CountryID, TaxID, TypeCD
Entity sets: PX_Objects_PR_PREarningTypeDetail, EarningTypeDetail, PREarningTypeDetail

PX.Objects.PR.PREarningTypeDetail.TypeCD : Edm.String [key] "Earning Type Code"
PX.Objects.PR.PREarningTypeDetail.TaxID : Edm.Int32 [key] "Tax Code"
PX.Objects.PR.PREarningTypeDetail.CountryID : Edm.String [key]
PX.Objects.PR.PREarningTypeDetail.TStamp : Edm.Binary
PX.Objects.PR.PREarningTypeDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREarningTypeDetail.CreatedByScreenID : Edm.String
PX.Objects.PR.PREarningTypeDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREarningTypeDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREarningTypeDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREarningTypeDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREarningTypeDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREarningTypeDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREarningTypeDetail.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PREarningTypeDetail.PRTaxCodeByCountryID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID, CountryID=CountryID)
PX.Objects.PR.PREarningTypeDetail.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.PREarningTypeDetail.EPEarningTypeByTypecd -> PX.Objects.EP.EPEarningType

# PX.Objects.PR.PREIPremiumRate (EntityType)

Label: "EI Premium Rates"
Key: RateID
Entity sets: PX_Objects_PR_PREIPremiumRate, EIPremiumRates, PREIPremiumRate

PX.Objects.PR.PREIPremiumRate.RateID : Edm.Int32 [key]
PX.Objects.PR.PREIPremiumRate.RateCD : Edm.String "Rate Name"
PX.Objects.PR.PREIPremiumRate.Rate : Edm.Decimal "Employer's EI Premium Rate (%)"
PX.Objects.PR.PREIPremiumRate.PayrollAccountCD : Edm.String "CRA Payroll Account Number"
PX.Objects.PR.PREIPremiumRate.TStamp : Edm.Binary
PX.Objects.PR.PREIPremiumRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREIPremiumRate.CreatedByScreenID : Edm.String
PX.Objects.PR.PREIPremiumRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREIPremiumRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREIPremiumRate.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREIPremiumRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREIPremiumRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREIPremiumRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREIPremiumRate.PRCRAPayrollAccountByPayrollAccountCD -> PX.Objects.PR.PRCRAPayrollAccount (PayrollAccountCD=PayrollAccountID)

# PX.Objects.PR.PREmployee (EntityType)

Label: "Payroll Employee"
BaseType: PX.Objects.EP.EPEmployee
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_PR_PREmployee, PayrollEmployee, PREmployee
Non-filterable, non-selectable: HoursPerWeek

PX.Objects.PR.PREmployee.ActiveInPayroll : Edm.Boolean [required] "Active"
PX.Objects.PR.PREmployee.EmployeeClassID : Edm.String "Class ID"
PX.Objects.PR.PREmployee.EmpType : Edm.String "Employee Type"
PX.Objects.PR.PREmployee.EmpTypeUseDflt : Edm.Boolean "Use Default"
PX.Objects.PR.PREmployee.PayGroupID : Edm.String "Pay Group"
PX.Objects.PR.PREmployee.PayGroupUseDflt : Edm.Boolean "Use Default"
PX.Objects.PR.PREmployee.CalendarIDUseDflt : Edm.Boolean [required] "Use Default"
PX.Objects.PR.PREmployee.HoursPerWeek : Edm.Decimal "Working Hours per Week"
PX.Objects.PR.PREmployee.StdWeeksPerYear : Edm.Byte "Working Weeks per Year"
PX.Objects.PR.PREmployee.StdWeeksPerYearUseDflt : Edm.Boolean "Use Default"
PX.Objects.PR.PREmployee.HoursPerYear : Edm.Decimal "Working Hours per Year"
PX.Objects.PR.PREmployee.NetPayMin : Edm.Decimal "Net Pay Minimum"
PX.Objects.PR.PREmployee.NetPayMinUseDflt : Edm.Boolean "Use Default"
PX.Objects.PR.PREmployee.GrnMaxPctNet : Edm.Decimal "Maximum Percent of Net Pay for All Garnishments"
PX.Objects.PR.PREmployee.GrnMaxPctUseDflt : Edm.Boolean "Use Default"
PX.Objects.PR.PREmployee.LocationUseDflt : Edm.Boolean "Use Class Default Work Locations"
PX.Objects.PR.PREmployee.UnionID : Edm.String "Default Union"
PX.Objects.PR.PREmployee.UnionUseDflt : Edm.Boolean "Use Default"
PX.Objects.PR.PREmployee.UseCustomSettings : Edm.Boolean [required] "Use Custom Settings"
PX.Objects.PR.PREmployee.WorkCodeID : Edm.String "Default WCC Code"
PX.Objects.PR.PREmployee.WorkCodeUseDflt : Edm.Boolean "Use Default"
PX.Objects.PR.PREmployee.ExemptFromOvertimeRules : Edm.Boolean [required] "Exempt from Overtime Rules"
PX.Objects.PR.PREmployee.ExemptFromOvertimeRulesUseDflt : Edm.Boolean [required] "Use Default"
PX.Objects.PR.PREmployee.OverrideHoursPerYearForCertified : Edm.Boolean [required] "Override Hours per Year for Certified Project"
PX.Objects.PR.PREmployee.OverrideHoursPerYearForCertifiedUseDflt : Edm.Boolean [required] "Use Default"
PX.Objects.PR.PREmployee.HoursPerYearForCertified : Edm.Int32 "Certified Project Hours per Year"
PX.Objects.PR.PREmployee.HoursPerYearForCertifiedUseDflt : Edm.Boolean [required] "Use Default"
PX.Objects.PR.PREmployee.ExemptFromCertifiedReporting : Edm.Boolean [required] "Exempt from Certified Reporting"
PX.Objects.PR.PREmployee.ExemptFromCertifiedReportingUseDflt : Edm.Boolean [required] "Use Default"
PX.Objects.PR.PREmployee.UsePayrollProjectWorkLocation : Edm.Boolean [required] "Use Payroll Work Location from Project"
PX.Objects.PR.PREmployee.UsePayrollProjectWorkLocationUseDflt : Edm.Boolean [required] "Use Class Default Value"
PX.Objects.PR.PREmployee.LineCntr : Edm.Int32 [required]
PX.Objects.PR.PREmployee.DedSplitType : Edm.String "Split Method"
PX.Objects.PR.PREmployee.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.PR.PREmployee.ActivePositionID : Edm.String "Position"
PX.Objects.PR.PREmployee.CountryID : Edm.String
PX.Objects.PR.PREmployee.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PREmployee.PREmployeeClassByEmployeeClassID -> PX.Objects.PR.PREmployeeClass (EmployeeClassID=EmployeeClassID)
PX.Objects.PR.PREmployee.PREmployeeClassByCountryID -> PX.Objects.PR.PREmployeeClass (EmployeeClassID=EmployeeClassID, CountryID=CountryID)
PX.Objects.PR.PREmployee.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)
PX.Objects.PR.PREmployee.AccountByEarningsAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.AccountByDedLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.AccountByBenefitExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.AccountByBenefitLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.AccountByPayrollTaxExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.AccountByPayrollTaxLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.AccountByPtoExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.AccountByPtoLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.AccountByPtoAssetAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PREmployee.SubByEarningsSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.SubByDedLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.SubByBenefitExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.SubByBenefitLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.SubByPayrollTaxExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.SubByPayrollTaxLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.SubByPtoExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.SubByPtoLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.SubByPtoAssetSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PREmployee.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.PR.PREmployee.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.PR.PREmployee.EPPositionByActivePositionID -> PX.Objects.EP.EPPosition (ActivePositionID=PositionID)
PX.Objects.PR.PREmployee.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup (PayGroupID=PayGroupID)

# PX.Objects.PR.PREmployeeAttribute (EntityType)

Label: "Employee Setting"
Key: BAccountID, SettingName
Entity sets: PX_Objects_PR_PREmployeeAttribute, EmployeeSetting, PREmployeeAttribute
Non-filterable, non-selectable: SettingLevel, Description, UseDefault, AllowOverride, IsFederal, SortOrder, Required, UsedForGovernmentReporting, CompanyNotes, NoteText, ErrorLevel, IsEmployeeSpecific, FEINDisplaySetting, IsTaxAgency, MaskedValue

PX.Objects.PR.PREmployeeAttribute.BAccountID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeAttribute.TypeName : Edm.String "Type"
PX.Objects.PR.PREmployeeAttribute.SettingName : Edm.String [key] "Setting"
PX.Objects.PR.PREmployeeAttribute.SettingLevel : Edm.String "Setting Level"
PX.Objects.PR.PREmployeeAttribute.State : Edm.String "State"
PX.Objects.PR.PREmployeeAttribute.CountryID : Edm.String
PX.Objects.PR.PREmployeeAttribute.Description : Edm.String "Name"
PX.Objects.PR.PREmployeeAttribute.IsEncryptionRequired : Edm.Boolean
PX.Objects.PR.PREmployeeAttribute.IsEncrypted : Edm.Boolean [required]
PX.Objects.PR.PREmployeeAttribute.CanadaReportMapping : Edm.Int32 "CanadaReportMapping"
PX.Objects.PR.PREmployeeAttribute.Value : Edm.String "Value"
PX.Objects.PR.PREmployeeAttribute.UseDefault : Edm.Boolean
PX.Objects.PR.PREmployeeAttribute.AllowOverride : Edm.Boolean
PX.Objects.PR.PREmployeeAttribute.IsFederal : Edm.Boolean "Is Federal Attribute"
PX.Objects.PR.PREmployeeAttribute.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.PR.PREmployeeAttribute.Required : Edm.Boolean "Required"
PX.Objects.PR.PREmployeeAttribute.AatrixMapping : Edm.Int32 "AatrixMapping"
PX.Objects.PR.PREmployeeAttribute.AdditionalInformation : Edm.String "Additional Information"
PX.Objects.PR.PREmployeeAttribute.UsedForTaxCalculation : Edm.Boolean [required] "Used for Tax Calculation"
PX.Objects.PR.PREmployeeAttribute.UsedForGovernmentReporting : Edm.Boolean "Used for Government Reporting"
PX.Objects.PR.PREmployeeAttribute.FormBox : Edm.String "Form/Box"
PX.Objects.PR.PREmployeeAttribute.CompanyNotes : Edm.String "Company Notes"
PX.Objects.PR.PREmployeeAttribute.NoteID : Edm.Guid
PX.Objects.PR.PREmployeeAttribute.NoteText : Edm.String "Note Text"
PX.Objects.PR.PREmployeeAttribute.ErrorLevel : Edm.Int32
PX.Objects.PR.PREmployeeAttribute.IsEmployeeSpecific : Edm.Boolean
PX.Objects.PR.PREmployeeAttribute.FEINDisplaySetting : Edm.Int32
PX.Objects.PR.PREmployeeAttribute.IsTaxAgency : Edm.Boolean
PX.Objects.PR.PREmployeeAttribute.MaskedValue : Edm.String
PX.Objects.PR.PREmployeeAttribute.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeAttribute.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeAttribute.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PREmployeeAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeAttribute.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.PREmployeeAttribute.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.PR.PREmployeeAttribute.PRCompanyTaxAttributeBySettingName -> PX.Objects.PR.PRCompanyTaxAttribute (SettingName=SettingName)

# PX.Objects.PR.PREmployeeClass (EntityType)

Label: "Employee Payroll Class"
Key: EmployeeClassID
Entity sets: PX_Objects_PR_PREmployeeClass, EmployeePayrollClass, PREmployeeClass
Non-filterable, non-selectable: HoursPerWeek, HoursPerYear, NoteText

PX.Objects.PR.PREmployeeClass.EmployeeClassID : Edm.String [key] "Payroll Class ID"
PX.Objects.PR.PREmployeeClass.Descr : Edm.String "Description"
PX.Objects.PR.PREmployeeClass.EmpType : Edm.String "Employee Type"
PX.Objects.PR.PREmployeeClass.PayGroupID : Edm.String "Pay Group"
PX.Objects.PR.PREmployeeClass.CalendarID : Edm.String "Default Calendar"
PX.Objects.PR.PREmployeeClass.HoursPerWeek : Edm.Decimal "Working Hours per Week"
PX.Objects.PR.PREmployeeClass.StdWeeksPerYear : Edm.Byte "Working Weeks per Year"
PX.Objects.PR.PREmployeeClass.HoursPerYear : Edm.Decimal "Working Hours per Year"
PX.Objects.PR.PREmployeeClass.ExemptFromOvertimeRules : Edm.Boolean [required] "Exempt from Overtime Rules"
PX.Objects.PR.PREmployeeClass.NetPayMin : Edm.Decimal [required] "Net Pay Minimum"
PX.Objects.PR.PREmployeeClass.WorkCodeID : Edm.String "Default WCC Code"
PX.Objects.PR.PREmployeeClass.UnionID : Edm.String "Default Union"
PX.Objects.PR.PREmployeeClass.ExemptFromCertifiedReporting : Edm.Boolean [required] "Exempt from Certified Reporting"
PX.Objects.PR.PREmployeeClass.GrnMaxPctNet : Edm.Decimal [required] "Maximum Percent of Net Pay for All Garnishments"
PX.Objects.PR.PREmployeeClass.WorkLocationCount : Edm.Int32 [required] "Work Location Count"
PX.Objects.PR.PREmployeeClass.UsePayrollProjectWorkLocation : Edm.Boolean [required] "Use Payroll Work Location from Project"
PX.Objects.PR.PREmployeeClass.OverrideHoursPerYearForCertified : Edm.Boolean [required] "Override Hours per Year for Certified Project"
PX.Objects.PR.PREmployeeClass.HoursPerYearForCertified : Edm.Int32 "Certified Project Hours per Year"
PX.Objects.PR.PREmployeeClass.CountryID : Edm.String "CountryID"
PX.Objects.PR.PREmployeeClass.NoteID : Edm.Guid
PX.Objects.PR.PREmployeeClass.NoteText : Edm.String "Note Text"
PX.Objects.PR.PREmployeeClass.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeClass.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeClass.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeClass.PMUnionByUnionID -> PX.Objects.PM.PMUnion (UnionID=UnionID)
PX.Objects.PR.PREmployeeClass.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)
PX.Objects.PR.PREmployeeClass.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.PREmployeeClass.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup (PayGroupID=PayGroupID)
PX.Objects.PR.PREmployeeClass.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.PR.PREmployeeClass.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.PR.PREmployeeClass.PRBandingRulePTOBankCollection -> Collection(PX.Objects.PR.PRBandingRulePTOBank)
PX.Objects.PR.PREmployeeClass.PREmployeeClassPTOBankCollection -> Collection(PX.Objects.PR.PREmployeeClassPTOBank)
PX.Objects.PR.PREmployeeClass.PREmployeeClassWorkLocationCollection -> Collection(PX.Objects.PR.PREmployeeClassWorkLocation)

# PX.Objects.PR.PREmployeeClassPTOBank (EntityType)

Label: "Employee Class PTO Bank"
Key: RecordID
Entity sets: PX_Objects_PR_PREmployeeClassPTOBank, EmployeeClassPTOBank, PREmployeeClassPTOBank
Non-filterable, non-selectable: CreateFinancialTransaction

PX.Objects.PR.PREmployeeClassPTOBank.RecordID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeClassPTOBank.EmployeeClassID : Edm.String "Employee Class"
PX.Objects.PR.PREmployeeClassPTOBank.BankID : Edm.String "PTO Bank"
PX.Objects.PR.PREmployeeClassPTOBank.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PREmployeeClassPTOBank.AllowNegativeBalance : Edm.Boolean [required] "Allow Negative Balance"
PX.Objects.PR.PREmployeeClassPTOBank.DisburseFromCarryover : Edm.Boolean [required] "Disburse Only from Carryover"
PX.Objects.PR.PREmployeeClassPTOBank.AccrualRate : Edm.Decimal [required] "Accrual %"
PX.Objects.PR.PREmployeeClassPTOBank.HoursPerYear : Edm.Decimal [required] "Hours per Year"
PX.Objects.PR.PREmployeeClassPTOBank.AccrualLimit : Edm.Decimal "Balance Limit"
PX.Objects.PR.PREmployeeClassPTOBank.StartDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.PR.PREmployeeClassPTOBank.PTOYearStartDate : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeClassPTOBank.CarryoverAmount : Edm.Decimal "Carryover Hours"
PX.Objects.PR.PREmployeeClassPTOBank.FrontLoadingAmount : Edm.Decimal "Front Loading Hours"
PX.Objects.PR.PREmployeeClassPTOBank.CreateFinancialTransaction : Edm.Boolean
PX.Objects.PR.PREmployeeClassPTOBank.ProbationPeriodBehaviour : Edm.String "During Probation Period"
PX.Objects.PR.PREmployeeClassPTOBank.Unassigned : Edm.Boolean [required] "Unassigned"
PX.Objects.PR.PREmployeeClassPTOBank.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeClassPTOBank.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeClassPTOBank.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeClassPTOBank.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeClassPTOBank.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeClassPTOBank.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeClassPTOBank.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeClassPTOBank.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeClassPTOBank.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeClassPTOBank.PREmployeeClassByEmployeeClassID -> PX.Objects.PR.PREmployeeClass (EmployeeClassID=EmployeeClassID)
PX.Objects.PR.PREmployeeClassPTOBank.PRPTOBankByBankID -> PX.Objects.PR.PRPTOBank (BankID=BankID)

# PX.Objects.PR.PREmployeeClassWorkLocation (EntityType)

Label: "Employee Class Work Location"
Key: RecordID
Entity sets: PX_Objects_PR_PREmployeeClassWorkLocation, EmployeeClassWorkLocation, PREmployeeClassWorkLocation
Non-filterable, non-selectable: EmployeeClassCountryID

PX.Objects.PR.PREmployeeClassWorkLocation.RecordID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeClassWorkLocation.EmployeeClassID : Edm.String
PX.Objects.PR.PREmployeeClassWorkLocation.LocationID : Edm.Int32 "Location"
PX.Objects.PR.PREmployeeClassWorkLocation.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.PR.PREmployeeClassWorkLocation.EmployeeClassCountryID : Edm.String
PX.Objects.PR.PREmployeeClassWorkLocation.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeClassWorkLocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeClassWorkLocation.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeClassWorkLocation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeClassWorkLocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeClassWorkLocation.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeClassWorkLocation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeClassWorkLocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeClassWorkLocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeClassWorkLocation.PREmployeeClassByEmployeeClassID -> PX.Objects.PR.PREmployeeClass (EmployeeClassID=EmployeeClassID)
PX.Objects.PR.PREmployeeClassWorkLocation.PRLocationByLocationID -> PX.Objects.PR.PRLocation (LocationID=LocationID)

# PX.Objects.PR.PREmployeeDeduct (EntityType)

Label: "Employee Deduct"
Key: BAccountID, LineNbr
Entity sets: PX_Objects_PR_PREmployeeDeduct, EmployeeDeduct, PREmployeeDeduct
Non-filterable, non-selectable: ContribType, CntCalcType, DedCalcType, IsGarnishment, EmployeeCountryID

PX.Objects.PR.PREmployeeDeduct.BAccountID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeDeduct.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PR.PREmployeeDeduct.CodeID : Edm.Int32 "Deduction Code"
PX.Objects.PR.PREmployeeDeduct.ContribType : Edm.String "Contribution Type"
PX.Objects.PR.PREmployeeDeduct.CntCalcType : Edm.String "Calculation Method"
PX.Objects.PR.PREmployeeDeduct.CntMaxFreqType : Edm.String "Contribution Limit Frequency"
PX.Objects.PR.PREmployeeDeduct.DedCalcType : Edm.String "Calculation Method"
PX.Objects.PR.PREmployeeDeduct.DedMaxFreqType : Edm.String "Deduction Limit Frequency"
PX.Objects.PR.PREmployeeDeduct.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.PR.PREmployeeDeduct.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.PR.PREmployeeDeduct.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PREmployeeDeduct.DedAmount : Edm.Decimal "Deduction Amount"
PX.Objects.PR.PREmployeeDeduct.DedPercent : Edm.Decimal "Deduction Percent"
PX.Objects.PR.PREmployeeDeduct.DedMaxAmount : Edm.Decimal "Deduction Limit"
PX.Objects.PR.PREmployeeDeduct.DedUseDflt : Edm.Boolean "Use Deduction Defaults"
PX.Objects.PR.PREmployeeDeduct.CntAmount : Edm.Decimal "Contribution Amount"
PX.Objects.PR.PREmployeeDeduct.CntPercent : Edm.Decimal "Contribution Percent"
PX.Objects.PR.PREmployeeDeduct.CntMaxAmount : Edm.Decimal "Contribution Limit"
PX.Objects.PR.PREmployeeDeduct.CntUseDflt : Edm.Boolean "Use Contribution Defaults"
PX.Objects.PR.PREmployeeDeduct.Sequence : Edm.Int32 "Sequence"
PX.Objects.PR.PREmployeeDeduct.IsGarnishment : Edm.Boolean "Garnishment"
PX.Objects.PR.PREmployeeDeduct.GarnBAccountID : Edm.Int32 "Vendor"
PX.Objects.PR.PREmployeeDeduct.VndInvDescr : Edm.String "Vendor Invoice Description"
PX.Objects.PR.PREmployeeDeduct.GarnCourtDate : Edm.DateTimeOffset "Court Date"
PX.Objects.PR.PREmployeeDeduct.GarnCourtName : Edm.String "Court Name"
PX.Objects.PR.PREmployeeDeduct.GarnDocRefNbr : Edm.String "Document ID"
PX.Objects.PR.PREmployeeDeduct.GarnOrigAmount : Edm.Decimal "Original Amount"
PX.Objects.PR.PREmployeeDeduct.GarnPaidAmount : Edm.Decimal "Amount Paid"
PX.Objects.PR.PREmployeeDeduct.EmployeeCountryID : Edm.String
PX.Objects.PR.PREmployeeDeduct.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeDeduct.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeDeduct.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeDeduct.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeDeduct.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeDeduct.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeDeduct.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeDeduct.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PREmployeeDeduct.VendorByGarnBAccountID -> PX.Objects.AP.Vendor (GarnBAccountID=BAccountID)
PX.Objects.PR.PREmployeeDeduct.BAccountByGarnBAccountID -> PX.Objects.CR.BAccount (GarnBAccountID=BAccountID)
PX.Objects.PR.PREmployeeDeduct.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeDeduct.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeDeduct.PRDeductCodeByCodeID -> PX.Objects.PR.PRDeductCode (CodeID=CodeID)

# PX.Objects.PR.PREmployeeDirectDeposit (EntityType)

Label: "Employee Direct Deposit"
Key: BAccountID, LineNbr
Entity sets: PX_Objects_PR_PREmployeeDirectDeposit, EmployeeDirectDeposit, PREmployeeDirectDeposit

PX.Objects.PR.PREmployeeDirectDeposit.BAccountID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeDirectDeposit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PR.PREmployeeDirectDeposit.BankAcctNbr : Edm.String "Account Number"
PX.Objects.PR.PREmployeeDirectDeposit.BankRoutingNbr : Edm.String "Bank Routing Number"
PX.Objects.PR.PREmployeeDirectDeposit.BankAcctType : Edm.String "Type"
PX.Objects.PR.PREmployeeDirectDeposit.BankName : Edm.String "Bank Name"
PX.Objects.PR.PREmployeeDirectDeposit.Amount : Edm.Decimal "Amount"
PX.Objects.PR.PREmployeeDirectDeposit.Percent : Edm.Decimal "Percent"
PX.Objects.PR.PREmployeeDirectDeposit.GetsRemainder : Edm.Boolean "Gets Remainder"
PX.Objects.PR.PREmployeeDirectDeposit.SortOrder : Edm.Int32 "Sequence"
PX.Objects.PR.PREmployeeDirectDeposit.BankTransitNbrCan : Edm.String "Bank Transit Number"
PX.Objects.PR.PREmployeeDirectDeposit.FinInstNbrCan : Edm.String "Financial Institution Number"
PX.Objects.PR.PREmployeeDirectDeposit.BankAcctNbrCan : Edm.String "Bank Account Number"
PX.Objects.PR.PREmployeeDirectDeposit.BeneficiaryName : Edm.String "Beneficiary Name"
PX.Objects.PR.PREmployeeDirectDeposit.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeDirectDeposit.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeDirectDeposit.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeDirectDeposit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeDirectDeposit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeDirectDeposit.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeDirectDeposit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeDirectDeposit.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PREmployeeDirectDeposit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeDirectDeposit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PREmployeeEarning (EntityType)

Label: "Employee Earning"
Key: BAccountID, LineNbr
Entity sets: PX_Objects_PR_PREmployeeEarning, EmployeeEarning, PREmployeeEarning
Non-filterable, non-selectable: IsPiecework

PX.Objects.PR.PREmployeeEarning.BAccountID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeEarning.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PR.PREmployeeEarning.TypeCD : Edm.String "Earning Type"
PX.Objects.PR.PREmployeeEarning.IsPiecework : Edm.Boolean "Piecework"
PX.Objects.PR.PREmployeeEarning.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.PR.PREmployeeEarning.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.PR.PREmployeeEarning.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PREmployeeEarning.PayRate : Edm.Decimal "Pay Rate"
PX.Objects.PR.PREmployeeEarning.UnitType : Edm.String "Unit of Pay"
PX.Objects.PR.PREmployeeEarning.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeEarning.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeEarning.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeEarning.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeEarning.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeEarning.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeEarning.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeEarning.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PREmployeeEarning.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeEarning.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeEarning.EPEarningTypeByTypeCD -> PX.Objects.EP.EPEarningType (TypeCD=TypeCD)

# PX.Objects.PR.PREmployeePTOBank (EntityType)

Label: "Employee PTO Bank"
Key: BAccountID, BankID, StartDate
Entity sets: PX_Objects_PR_PREmployeePTOBank, EmployeePTOBank, PREmployeePTOBank
Non-filterable, non-selectable: CreateFinancialTransaction, AllowViewAvailablePTOPaidHours

PX.Objects.PR.PREmployeePTOBank.BAccountID : Edm.Int32 [key]
PX.Objects.PR.PREmployeePTOBank.BankID : Edm.String [key] "PTO Bank"
PX.Objects.PR.PREmployeePTOBank.EmployeeClassID : Edm.String "Class ID"
PX.Objects.PR.PREmployeePTOBank.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PREmployeePTOBank.AccrualMethod : Edm.String "Accrual Method"
PX.Objects.PR.PREmployeePTOBank.AccrualRate : Edm.Decimal [required] "Accrual %"
PX.Objects.PR.PREmployeePTOBank.HoursPerYear : Edm.Decimal [required] "Hours per Year"
PX.Objects.PR.PREmployeePTOBank.AccrualLimit : Edm.Decimal "Balance Limit"
PX.Objects.PR.PREmployeePTOBank.CarryoverType : Edm.String "Carryover Type"
PX.Objects.PR.PREmployeePTOBank.CarryoverAmount : Edm.Decimal "Carryover Hours"
PX.Objects.PR.PREmployeePTOBank.FrontLoadingAmount : Edm.Decimal "Front Loading Hours"
PX.Objects.PR.PREmployeePTOBank.StartDate : Edm.DateTimeOffset [key] "Start Date"
PX.Objects.PR.PREmployeePTOBank.PTOYearStartDate : Edm.DateTimeOffset
PX.Objects.PR.PREmployeePTOBank.BandingRule : Edm.Int32 "Banding Rule"
PX.Objects.PR.PREmployeePTOBank.AllowNegativeBalance : Edm.Boolean [required] "Allow Negative Balance"
PX.Objects.PR.PREmployeePTOBank.TransferDate : Edm.DateTimeOffset "Transfer Date"
PX.Objects.PR.PREmployeePTOBank.ProbationPeriodBehaviour : Edm.String "During Probation Period"
PX.Objects.PR.PREmployeePTOBank.SettlementBalanceType : Edm.String "On Settlement"
PX.Objects.PR.PREmployeePTOBank.DisburseFromCarryover : Edm.Boolean [required] "Can Only Disburse from Carryover"
PX.Objects.PR.PREmployeePTOBank.CreateFinancialTransaction : Edm.Boolean
PX.Objects.PR.PREmployeePTOBank.AllowViewAvailablePTOPaidHours : Edm.Boolean
PX.Objects.PR.PREmployeePTOBank.TStamp : Edm.Binary
PX.Objects.PR.PREmployeePTOBank.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeePTOBank.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeePTOBank.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeePTOBank.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeePTOBank.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeePTOBank.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeePTOBank.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PREmployeePTOBank.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeePTOBank.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeePTOBank.PRPTOBankByBankID -> PX.Objects.PR.PRPTOBank (BankID=BankID)

# PX.Objects.PR.PREmployeePTOHistory (EntityType)

Label: "Employee PTO History"
Key: RecordID
Entity sets: PX_Objects_PR_PREmployeePTOHistory, EmployeePTOHistory, PREmployeePTOHistory

PX.Objects.PR.PREmployeePTOHistory.RecordID : Edm.Int32 [key] "Record ID"
PX.Objects.PR.PREmployeePTOHistory.DocType : Edm.String "Type"
PX.Objects.PR.PREmployeePTOHistory.RefNbr : Edm.String "Reference Nbr."
PX.Objects.PR.PREmployeePTOHistory.BAccountID : Edm.Int32 "Employee"
PX.Objects.PR.PREmployeePTOHistory.BankID : Edm.String "Bank"
PX.Objects.PR.PREmployeePTOHistory.Type : Edm.String "Type"
PX.Objects.PR.PREmployeePTOHistory.Date : Edm.DateTimeOffset "Date"
PX.Objects.PR.PREmployeePTOHistory.Amount : Edm.Decimal "Amount"
PX.Objects.PR.PREmployeePTOHistory.IsFrontLoading : Edm.Boolean [required] "Is Front Loading"
PX.Objects.PR.PREmployeePTOHistory.IsCarryover : Edm.Boolean [required] "Is Carryover"

# PX.Objects.PR.PREmployeeTax (EntityType)

Label: "Employee Tax"
Key: BAccountID, TaxID
Entity sets: PX_Objects_PR_PREmployeeTax, EmployeeTax, PREmployeeTax
Non-filterable, non-selectable: State, EmployeeCountryID, ErrorLevel

PX.Objects.PR.PREmployeeTax.BAccountID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeTax.TaxID : Edm.Int32 [key] "Tax Code"
PX.Objects.PR.PREmployeeTax.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PREmployeeTax.State : Edm.String "State"
PX.Objects.PR.PREmployeeTax.CountryID : Edm.String
PX.Objects.PR.PREmployeeTax.EmployeeCountryID : Edm.String
PX.Objects.PR.PREmployeeTax.ErrorLevel : Edm.Int32
PX.Objects.PR.PREmployeeTax.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeTax.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeTax.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeTax.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PREmployeeTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeTax.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PREmployeeTax.PREmployeeTaxAttributeCollection -> Collection(PX.Objects.PR.PREmployeeTaxAttribute)

# PX.Objects.PR.PREmployeeTaxAttribute (EntityType)

Label: "Employee Tax Setting"
Key: BAccountID, SettingName, TaxID
Entity sets: PX_Objects_PR_PREmployeeTaxAttribute, EmployeeTaxSetting, PREmployeeTaxAttribute
Non-filterable, non-selectable: Description, IsEncryptionRequired, IsEncrypted, UseDefault, AllowOverride, SortOrder, Required, State, CompanyNotes, NoteText, ErrorLevel, IsEmployeeSpecific, FEINDisplaySetting, IsTaxAgency

PX.Objects.PR.PREmployeeTaxAttribute.BAccountID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeTaxAttribute.TaxID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeTaxAttribute.TypeName : Edm.String "Type"
PX.Objects.PR.PREmployeeTaxAttribute.SettingName : Edm.String [key] "Setting"
PX.Objects.PR.PREmployeeTaxAttribute.Description : Edm.String "Name"
PX.Objects.PR.PREmployeeTaxAttribute.IsEncryptionRequired : Edm.Boolean
PX.Objects.PR.PREmployeeTaxAttribute.IsEncrypted : Edm.Boolean
PX.Objects.PR.PREmployeeTaxAttribute.CanadaReportMapping : Edm.Int32 "CanadaReportMapping"
PX.Objects.PR.PREmployeeTaxAttribute.Value : Edm.String "Value"
PX.Objects.PR.PREmployeeTaxAttribute.UseDefault : Edm.Boolean
PX.Objects.PR.PREmployeeTaxAttribute.AllowOverride : Edm.Boolean
PX.Objects.PR.PREmployeeTaxAttribute.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.PR.PREmployeeTaxAttribute.Required : Edm.Boolean "Required"
PX.Objects.PR.PREmployeeTaxAttribute.AatrixMapping : Edm.Int32 "AatrixMapping"
PX.Objects.PR.PREmployeeTaxAttribute.AdditionalInformation : Edm.String "Additional Information"
PX.Objects.PR.PREmployeeTaxAttribute.FormBox : Edm.String "Form/Box"
PX.Objects.PR.PREmployeeTaxAttribute.State : Edm.String
PX.Objects.PR.PREmployeeTaxAttribute.CompanyNotes : Edm.String "Company Notes"
PX.Objects.PR.PREmployeeTaxAttribute.NoteID : Edm.Guid
PX.Objects.PR.PREmployeeTaxAttribute.NoteText : Edm.String "Note Text"
PX.Objects.PR.PREmployeeTaxAttribute.ErrorLevel : Edm.Int32
PX.Objects.PR.PREmployeeTaxAttribute.IsEmployeeSpecific : Edm.Boolean
PX.Objects.PR.PREmployeeTaxAttribute.FEINDisplaySetting : Edm.Int32
PX.Objects.PR.PREmployeeTaxAttribute.IsTaxAgency : Edm.Boolean
PX.Objects.PR.PREmployeeTaxAttribute.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeTaxAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeTaxAttribute.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeTaxAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeTaxAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeTaxAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeTaxAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeTaxAttribute.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PREmployeeTaxAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeTaxAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeTaxAttribute.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PREmployeeTaxAttribute.PREmployeeTaxByTaxID -> PX.Objects.PR.PREmployeeTax (BAccountID=BAccountID, TaxID=TaxID)
PX.Objects.PR.PREmployeeTaxAttribute.PRTaxCodeAttributeBySettingName -> PX.Objects.PR.PRTaxCodeAttribute (TaxID=TaxID, SettingName=SettingName)
PX.Objects.PR.PREmployeeTaxAttribute.PRTaxCodeAttributeByTaxID -> PX.Objects.PR.PRTaxCodeAttribute (SettingName=SettingName, TaxID=TaxID)

# PX.Objects.PR.PREmployeeTaxForm (EntityType)

Label: "Employee Tax Form"
Key: BatchID, EmployeeID, ProvinceOfEmployment
Entity sets: PX_Objects_PR_PREmployeeTaxForm, EmployeeTaxForm, PREmployeeTaxForm
Non-filterable, non-selectable: NotPublished, PublishedFrom, DeletedDatabaseRecord

PX.Objects.PR.PREmployeeTaxForm.BatchID : Edm.String [key] "Batch ID"
PX.Objects.PR.PREmployeeTaxForm.EmployeeID : Edm.Int32 [key] "EmployeeID"
PX.Objects.PR.PREmployeeTaxForm.ProvinceOfEmployment : Edm.String [key] "Province of Employment"
PX.Objects.PR.PREmployeeTaxForm.Published : Edm.Boolean [required] "Published"
PX.Objects.PR.PREmployeeTaxForm.EverPublished : Edm.Boolean [required] "EverPublished"
PX.Objects.PR.PREmployeeTaxForm.NotPublished : Edm.Boolean
PX.Objects.PR.PREmployeeTaxForm.PublishedFrom : Edm.String "Published From"
PX.Objects.PR.PREmployeeTaxForm.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeTaxForm.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeTaxForm.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeTaxForm.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeTaxForm.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeTaxForm.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeTaxForm.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeTaxForm.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PR.PREmployeeTaxForm.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PREmployeeTaxForm.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeTaxForm.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeTaxForm.PRTaxFormBatchByBatchID -> PX.Objects.PR.PRTaxFormBatch (BatchID=BatchID)

# PX.Objects.PR.PREmployeeTaxFormData (EntityType)

Label: "Employee Tax Form Data"
Key: BatchID, EmployeeID, FormFileType, ProvinceOfEmployment
Entity sets: PX_Objects_PR_PREmployeeTaxFormData, EmployeeTaxFormData, PREmployeeTaxFormData
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.PR.PREmployeeTaxFormData.BatchID : Edm.String [key] "Batch ID"
PX.Objects.PR.PREmployeeTaxFormData.EmployeeID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeTaxFormData.FormFileType : Edm.String [key] "Form File Type"
PX.Objects.PR.PREmployeeTaxFormData.ProvinceOfEmployment : Edm.String [key] "Province of Employment"
PX.Objects.PR.PREmployeeTaxFormData.FormData : Edm.String
PX.Objects.PR.PREmployeeTaxFormData.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeTaxFormData.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeTaxFormData.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeTaxFormData.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeTaxFormData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeTaxFormData.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeTaxFormData.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeTaxFormData.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PR.PREmployeeTaxFormData.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PREmployeeTaxFormData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeTaxFormData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeTaxFormData.PRTaxFormBatchByBatchID -> PX.Objects.PR.PRTaxFormBatch (BatchID=BatchID)

# PX.Objects.PR.PREmployeeWorkLocation (EntityType)

Label: "Employee Work Location"
Key: EmployeeID, LocationID
Entity sets: PX_Objects_PR_PREmployeeWorkLocation, EmployeeWorkLocation, PREmployeeWorkLocation
Non-filterable, non-selectable: EmployeeCountryID

PX.Objects.PR.PREmployeeWorkLocation.EmployeeID : Edm.Int32 [key]
PX.Objects.PR.PREmployeeWorkLocation.LocationID : Edm.Int32 [key] "Location"
PX.Objects.PR.PREmployeeWorkLocation.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.PR.PREmployeeWorkLocation.EmployeeCountryID : Edm.String
PX.Objects.PR.PREmployeeWorkLocation.TStamp : Edm.Binary
PX.Objects.PR.PREmployeeWorkLocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREmployeeWorkLocation.CreatedByScreenID : Edm.String
PX.Objects.PR.PREmployeeWorkLocation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeWorkLocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREmployeeWorkLocation.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREmployeeWorkLocation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREmployeeWorkLocation.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PREmployeeWorkLocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREmployeeWorkLocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREmployeeWorkLocation.PRLocationByLocationID -> PX.Objects.PR.PRLocation (LocationID=LocationID)

# PX.Objects.PR.PREntityCompanyTaxAttribute (EntityType)

Label: "Entity Company Tax Attribute"
Key: EntityID, SettingName
Entity sets: PX_Objects_PR_PREntityCompanyTaxAttribute, EntityCompanyTaxAttribute, PREntityCompanyTaxAttribute
Non-filterable, non-selectable: OrganizationCD, OrganizationName, BranchCD, BranchName, EmployeeCD, EmployeeName, Branch, Company

PX.Objects.PR.PREntityCompanyTaxAttribute.SettingName : Edm.String [key] "Setting"
PX.Objects.PR.PREntityCompanyTaxAttribute.EntityID : Edm.Int32 [key]
PX.Objects.PR.PREntityCompanyTaxAttribute.EntityType : Edm.String "Entity Type"
PX.Objects.PR.PREntityCompanyTaxAttribute.IsEncryptionRequired : Edm.Boolean [required]
PX.Objects.PR.PREntityCompanyTaxAttribute.IsEncrypted : Edm.Boolean [required]
PX.Objects.PR.PREntityCompanyTaxAttribute.Value : Edm.String "Value"
PX.Objects.PR.PREntityCompanyTaxAttribute.OrganizationCD : Edm.String "Company ID"
PX.Objects.PR.PREntityCompanyTaxAttribute.OrganizationName : Edm.String "Company Name"
PX.Objects.PR.PREntityCompanyTaxAttribute.BranchCD : Edm.String "Branch ID"
PX.Objects.PR.PREntityCompanyTaxAttribute.BranchName : Edm.String "Branch Name"
PX.Objects.PR.PREntityCompanyTaxAttribute.EmployeeCD : Edm.String "Employee ID"
PX.Objects.PR.PREntityCompanyTaxAttribute.EmployeeName : Edm.String "Employee Name"
PX.Objects.PR.PREntityCompanyTaxAttribute.Branch : Edm.String "Branch"
PX.Objects.PR.PREntityCompanyTaxAttribute.Company : Edm.String "Company"
PX.Objects.PR.PREntityCompanyTaxAttribute.TStamp : Edm.Binary
PX.Objects.PR.PREntityCompanyTaxAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREntityCompanyTaxAttribute.CreatedByScreenID : Edm.String
PX.Objects.PR.PREntityCompanyTaxAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREntityCompanyTaxAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREntityCompanyTaxAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREntityCompanyTaxAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREntityCompanyTaxAttribute.BAccountByEntityID -> PX.Objects.CR.BAccount (EntityID=BAccountID)
PX.Objects.PR.PREntityCompanyTaxAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREntityCompanyTaxAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PREntityTaxCodeAttribute (EntityType)

Label: "Entity Tax Code Attribute"
Key: EntityID, SettingName, TaxID
Entity sets: PX_Objects_PR_PREntityTaxCodeAttribute, EntityTaxCodeAttribute, PREntityTaxCodeAttribute
Non-filterable, non-selectable: OrganizationCD, OrganizationName, BranchCD, BranchName, EmployeeCD, EmployeeName, Branch, Company

PX.Objects.PR.PREntityTaxCodeAttribute.TaxID : Edm.Int32 [key]
PX.Objects.PR.PREntityTaxCodeAttribute.SettingName : Edm.String [key] "Setting"
PX.Objects.PR.PREntityTaxCodeAttribute.EntityID : Edm.Int32 [key]
PX.Objects.PR.PREntityTaxCodeAttribute.EntityType : Edm.String "Entity Type"
PX.Objects.PR.PREntityTaxCodeAttribute.Value : Edm.String "Value"
PX.Objects.PR.PREntityTaxCodeAttribute.OrganizationCD : Edm.String "Company ID"
PX.Objects.PR.PREntityTaxCodeAttribute.OrganizationName : Edm.String "Company Name"
PX.Objects.PR.PREntityTaxCodeAttribute.BranchCD : Edm.String "Branch ID"
PX.Objects.PR.PREntityTaxCodeAttribute.BranchName : Edm.String "Branch Name"
PX.Objects.PR.PREntityTaxCodeAttribute.EmployeeCD : Edm.String "Employee ID"
PX.Objects.PR.PREntityTaxCodeAttribute.EmployeeName : Edm.String "Employee Name"
PX.Objects.PR.PREntityTaxCodeAttribute.Branch : Edm.String "Branch"
PX.Objects.PR.PREntityTaxCodeAttribute.Company : Edm.String "Company"
PX.Objects.PR.PREntityTaxCodeAttribute.TStamp : Edm.Binary
PX.Objects.PR.PREntityTaxCodeAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PREntityTaxCodeAttribute.CreatedByScreenID : Edm.String
PX.Objects.PR.PREntityTaxCodeAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREntityTaxCodeAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PREntityTaxCodeAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PREntityTaxCodeAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PREntityTaxCodeAttribute.BAccountByEntityID -> PX.Objects.CR.BAccount (EntityID=BAccountID)
PX.Objects.PR.PREntityTaxCodeAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PREntityTaxCodeAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PREntityTaxCodeAttribute.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PREntityTaxCodeAttribute.PRTaxCodeAttributeBySettingName -> PX.Objects.PR.PRTaxCodeAttribute (TaxID=TaxID, SettingName=SettingName)

# PX.Objects.PR.PRGovernmentSlip (EntityType)

Label: "Government Slip"
Key: SlipName, Year
Entity sets: PX_Objects_PR_PRGovernmentSlip, GovernmentSlip, PRGovernmentSlip

PX.Objects.PR.PRGovernmentSlip.SlipName : Edm.String [key] "Slip Name"
PX.Objects.PR.PRGovernmentSlip.Year : Edm.Int32 [key] "Year"
PX.Objects.PR.PRGovernmentSlip.Timestamp : Edm.DateTimeOffset "Timestamp"
PX.Objects.PR.PRGovernmentSlip.SlipData : Edm.String "Slip Data"
PX.Objects.PR.PRGovernmentSlip.TStamp : Edm.Binary
PX.Objects.PR.PRGovernmentSlip.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRGovernmentSlip.CreatedByScreenID : Edm.String
PX.Objects.PR.PRGovernmentSlip.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRGovernmentSlip.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRGovernmentSlip.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRGovernmentSlip.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRGovernmentSlip.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRGovernmentSlip.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRGovernmentSlip.PRGovernmentSlipFieldCollection -> Collection(PX.Objects.PR.PRGovernmentSlipField)

# PX.Objects.PR.PRGovernmentSlipField (EntityType)

Label: "Government Slip Field"
Key: FieldCode, Page, SlipName, Year
Entity sets: PX_Objects_PR_PRGovernmentSlipField, GovernmentSlipField, PRGovernmentSlipField

PX.Objects.PR.PRGovernmentSlipField.SlipName : Edm.String [key] "Slip Name"
PX.Objects.PR.PRGovernmentSlipField.Year : Edm.Int32 [key] "Year"
PX.Objects.PR.PRGovernmentSlipField.Page : Edm.Int32 [key] "Page"
PX.Objects.PR.PRGovernmentSlipField.FieldCode : Edm.String [key] "Field Code"
PX.Objects.PR.PRGovernmentSlipField.FieldName : Edm.String "Field Name"
PX.Objects.PR.PRGovernmentSlipField.DataType : Edm.String "Data Type"
PX.Objects.PR.PRGovernmentSlipField.Fillable : Edm.Boolean "Fillable"
PX.Objects.PR.PRGovernmentSlipField.Multiline : Edm.Boolean "Multiline"
PX.Objects.PR.PRGovernmentSlipField.FontName : Edm.String "Font Name"
PX.Objects.PR.PRGovernmentSlipField.FontSize : Edm.Double "Font Size"
PX.Objects.PR.PRGovernmentSlipField.Color : Edm.String "Color"
PX.Objects.PR.PRGovernmentSlipField.Alignment : Edm.String "Alignment"
PX.Objects.PR.PRGovernmentSlipField.LeftX : Edm.Double "Left X"
PX.Objects.PR.PRGovernmentSlipField.TopY : Edm.Double "Top Y"
PX.Objects.PR.PRGovernmentSlipField.Width : Edm.Double "Width"
PX.Objects.PR.PRGovernmentSlipField.Height : Edm.Double "Height"
PX.Objects.PR.PRGovernmentSlipField.TStamp : Edm.Binary
PX.Objects.PR.PRGovernmentSlipField.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRGovernmentSlipField.CreatedByScreenID : Edm.String
PX.Objects.PR.PRGovernmentSlipField.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRGovernmentSlipField.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRGovernmentSlipField.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRGovernmentSlipField.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRGovernmentSlipField.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRGovernmentSlipField.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRGovernmentSlipField.PRGovernmentSlipByYear -> PX.Objects.PR.PRGovernmentSlip (SlipName=SlipName, Year=Year)

# PX.Objects.PR.PRLocation (EntityType)

Label: "Location"
Key: LocationCD
Entity sets: PX_Objects_PR_PRLocation, Location1, PRLocation
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.PR.PRLocation.LocationID : Edm.Int32
PX.Objects.PR.PRLocation.LocationCD : Edm.String [key] "Location ID"
PX.Objects.PR.PRLocation.Description : Edm.String "Location Name"
PX.Objects.PR.PRLocation.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PRLocation.AddressID : Edm.Int32 "Address ID"
PX.Objects.PR.PRLocation.NoteID : Edm.Guid
PX.Objects.PR.PRLocation.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRLocation.TStamp : Edm.Binary
PX.Objects.PR.PRLocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRLocation.CreatedByScreenID : Edm.String
PX.Objects.PR.PRLocation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRLocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRLocation.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRLocation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRLocation.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PR.PRLocation.AddressByAddressID -> PX.Objects.CR.Address (AddressID=AddressID)
PX.Objects.PR.PRLocation.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRLocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRLocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRLocation.PRPaymentEarningCollection -> Collection(PX.Objects.PR.PRPaymentEarning)
PX.Objects.PR.PRLocation.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PR.PRLocation.PREmployeeClassWorkLocationCollection -> Collection(PX.Objects.PR.PREmployeeClassWorkLocation)
PX.Objects.PR.PRLocation.PREmployeeWorkLocationCollection -> Collection(PX.Objects.PR.PREmployeeWorkLocation)
PX.Objects.PR.PRLocation.PRYtdEarningsCollection -> Collection(PX.Objects.PR.PRYtdEarnings)

# PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet (EntityType)

Label: "Non-payable Benefits Increasing Disposable Net Income"
Key: ApplicableBenefitCodeID, DeductCodeID
Entity sets: PX_Objects_PR_PRNonPayableBenefitsIncreasingDisposableNet, NonpayableBenefitsIncreasingDisposableNetIncome, PRNonPayableBenefitsIncreasingDisposableNet

PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.DeductCodeID : Edm.Int32 [key]
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.ApplicableBenefitCodeID : Edm.Int32 [key] "Benefit Code"
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.TStamp : Edm.Binary
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.CreatedByScreenID : Edm.String
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet.PRDeductCodeByApplicableBenefitCodeID -> PX.Objects.PR.PRDeductCode (ApplicableBenefitCodeID=CodeID)

# PX.Objects.PR.PROvertimeRule (EntityType)

Label: "Overtime Rule"
Key: OvertimeRuleID
Entity sets: PX_Objects_PR_PROvertimeRule, OvertimeRule, PROvertimeRule
Non-filterable, non-selectable: OvertimeMultiplier

PX.Objects.PR.PROvertimeRule.OvertimeRuleID : Edm.String [key] "Overtime Rule"
PX.Objects.PR.PROvertimeRule.Description : Edm.String "Description"
PX.Objects.PR.PROvertimeRule.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PROvertimeRule.DisbursingTypeCD : Edm.String "Disbursing Earning Type"
PX.Objects.PR.PROvertimeRule.OvertimeMultiplier : Edm.Decimal "Multiplier"
PX.Objects.PR.PROvertimeRule.RuleType : Edm.String "Type"
PX.Objects.PR.PROvertimeRule.OvertimeThreshold : Edm.Decimal [required] "Threshold for Overtime (Hours)"
PX.Objects.PR.PROvertimeRule.WeekDay : Edm.Byte "Day of Week"
PX.Objects.PR.PROvertimeRule.NumberOfConsecutiveDays : Edm.Byte "Number of Consecutive Days"
PX.Objects.PR.PROvertimeRule.CountryID : Edm.String "CountryID"
PX.Objects.PR.PROvertimeRule.State : Edm.String "State"
PX.Objects.PR.PROvertimeRule.UnionID : Edm.String "Union Local"
PX.Objects.PR.PROvertimeRule.TStamp : Edm.Binary
PX.Objects.PR.PROvertimeRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PROvertimeRule.CreatedByScreenID : Edm.String
PX.Objects.PR.PROvertimeRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PROvertimeRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PROvertimeRule.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PROvertimeRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PROvertimeRule.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PROvertimeRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PROvertimeRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PROvertimeRule.PMUnionByUnionID -> PX.Objects.PM.PMUnion (UnionID=UnionID)
PX.Objects.PR.PROvertimeRule.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.PROvertimeRule.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.PR.PROvertimeRule.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.PR.PROvertimeRule.EPEarningTypeByDisbursingTypeCD -> PX.Objects.EP.EPEarningType (DisbursingTypeCD=TypeCD)
PX.Objects.PR.PROvertimeRule.PRBatchOvertimeRuleCollection -> Collection(PX.Objects.PR.PRBatchOvertimeRule)
PX.Objects.PR.PROvertimeRule.PRPaymentOvertimeRuleCollection -> Collection(PX.Objects.PR.PRPaymentOvertimeRule)

# PX.Objects.PR.PRPayGroup (EntityType)

Label: "Pay Group"
Key: PayGroupID
Entity sets: PX_Objects_PR_PRPayGroup, PayGroup, PRPayGroup
Non-filterable, non-selectable: IsPayGroupIDFilled, NoteText

PX.Objects.PR.PRPayGroup.PayGroupID : Edm.String [key] "Pay Group ID"
PX.Objects.PR.PRPayGroup.RoleName : Edm.String "User Role"
PX.Objects.PR.PRPayGroup.Description : Edm.String "Pay Group Name"
PX.Objects.PR.PRPayGroup.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.PR.PRPayGroup.IsPayGroupIDFilled : Edm.Boolean "IsPayGroupIDFilled"
PX.Objects.PR.PRPayGroup.NoteID : Edm.Guid
PX.Objects.PR.PRPayGroup.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRPayGroup.TStamp : Edm.Binary
PX.Objects.PR.PRPayGroup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPayGroup.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPayGroup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPayGroup.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPayGroup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPayGroup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPayGroup.RolesByRoleName -> PX.SM.Roles (RoleName=Rolename)
PX.Objects.PR.PRPayGroup.AccountByEarningsAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.AccountByDedLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.AccountByBenefitExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.AccountByBenefitLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.AccountByTaxExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.AccountByTaxLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.AccountByPtoExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.AccountByPtoLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.AccountByPtoAssetAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPayGroup.SubByEarningsSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.SubByDedLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.SubByBenefitExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.SubByBenefitLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.SubByTaxExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.SubByTaxLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.SubByPtoExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.SubByPtoLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.SubByPtoAssetSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPayGroup.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.PR.PRPayGroup.PREmployeeClassCollection -> Collection(PX.Objects.PR.PREmployeeClass)
PX.Objects.PR.PRPayGroup.PRBatchCollection -> Collection(PX.Objects.PR.PRBatch)
PX.Objects.PR.PRPayGroup.PRPayGroupPeriodCollection -> Collection(PX.Objects.PR.PRPayGroupPeriod)
PX.Objects.PR.PRPayGroup.PRPayGroupYearCollection -> Collection(PX.Objects.PR.PRPayGroupYear)
PX.Objects.PR.PRPayGroup.PRPayGroupYearSetupCollection -> Collection(PX.Objects.PR.PRPayGroupYearSetup)
PX.Objects.PR.PRPayGroup.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)

# PX.Objects.PR.PRPayGroupPeriod (EntityType)

Label: "Pay Periods"
Key: FinPeriodID, PayGroupID
Entity sets: PX_Objects_PR_PRPayGroupPeriod, PayPeriods, PRPayGroupPeriod
Non-filterable, non-selectable: PeriodNbrAsInt, EndDateUI

PX.Objects.PR.PRPayGroupPeriod.PayGroupID : Edm.String [key]
PX.Objects.PR.PRPayGroupPeriod.FinPeriodID : Edm.String [key] "Pay Period ID"
PX.Objects.PR.PRPayGroupPeriod.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.PR.PRPayGroupPeriod.EndDate : Edm.DateTimeOffset [required] "End Date"
PX.Objects.PR.PRPayGroupPeriod.TransactionDate : Edm.DateTimeOffset [required] "Transaction Date"
PX.Objects.PR.PRPayGroupPeriod.Descr : Edm.String "Description"
PX.Objects.PR.PRPayGroupPeriod.Closed : Edm.Boolean [required] "Closed in GL"
PX.Objects.PR.PRPayGroupPeriod.DateLocked : Edm.Boolean [required] "Date Locked"
PX.Objects.PR.PRPayGroupPeriod.PeriodNbr : Edm.String "Period Nbr."
PX.Objects.PR.PRPayGroupPeriod.PeriodNbrAsInt : Edm.Int32
PX.Objects.PR.PRPayGroupPeriod.FinYear : Edm.String "Financial Year"
PX.Objects.PR.PRPayGroupPeriod.OriginalDescr : Edm.String "OriginalDescr"
PX.Objects.PR.PRPayGroupPeriod.OriginalPeriodNbr : Edm.String "OriginalPeriodNbr"
PX.Objects.PR.PRPayGroupPeriod.OriginalYear : Edm.String "OriginalYear"
PX.Objects.PR.PRPayGroupPeriod.OriginalFinPeriodID : Edm.String "OriginalFinPeriodID"
PX.Objects.PR.PRPayGroupPeriod.TStamp : Edm.Binary
PX.Objects.PR.PRPayGroupPeriod.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPayGroupPeriod.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPayGroupPeriod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroupPeriod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPayGroupPeriod.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPayGroupPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroupPeriod.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.PR.PRPayGroupPeriod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPayGroupPeriod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPayGroupPeriod.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization
PX.Objects.PR.PRPayGroupPeriod.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup (PayGroupID=PayGroupID)
PX.Objects.PR.PRPayGroupPeriod.PRPayGroupYearByFinYear -> PX.Objects.PR.PRPayGroupYear (PayGroupID=PayGroupID, FinYear=Year)
PX.Objects.PR.PRPayGroupPeriod.PRBatchCollection -> Collection(PX.Objects.PR.PRBatch)
PX.Objects.PR.PRPayGroupPeriod.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)

# PX.Objects.PR.PRPayGroupPeriodSetup (EntityType)

Label: "Pay Group Period Setup"
Key: PayGroupID, PeriodNbr
Entity sets: PX_Objects_PR_PRPayGroupPeriodSetup, PayGroupPeriodSetup, PRPayGroupPeriodSetup
Non-filterable, non-selectable: EndDateUI

PX.Objects.PR.PRPayGroupPeriodSetup.PayGroupID : Edm.String [key]
PX.Objects.PR.PRPayGroupPeriodSetup.PeriodNbr : Edm.String [key] "Period Nbr."
PX.Objects.PR.PRPayGroupPeriodSetup.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.PR.PRPayGroupPeriodSetup.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.PR.PRPayGroupPeriodSetup.TransactionDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.PR.PRPayGroupPeriodSetup.Descr : Edm.String "Description"
PX.Objects.PR.PRPayGroupPeriodSetup.tstamp : Edm.Binary
PX.Objects.PR.PRPayGroupPeriodSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPayGroupPeriodSetup.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPayGroupPeriodSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroupPeriodSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPayGroupPeriodSetup.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPayGroupPeriodSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroupPeriodSetup.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.PR.PRPayGroupPeriodSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPayGroupPeriodSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPayGroupPeriodSetup.PRPayGroupYearSetupByPayGroupID -> PX.Objects.PR.PRPayGroupYearSetup (PayGroupID=PayGroupID)

# PX.Objects.PR.PRPayGroupYear (EntityType)

Label: "Pay Group Year"
Key: PayGroupID, Year
Entity sets: PX_Objects_PR_PRPayGroupYear, PayGroupYear, PRPayGroupYear
Non-filterable, non-selectable: HeaderDescription

PX.Objects.PR.PRPayGroupYear.PayGroupID : Edm.String [key] "Pay Group"
PX.Objects.PR.PRPayGroupYear.Year : Edm.String [key required] "Year"
PX.Objects.PR.PRPayGroupYear.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.PR.PRPayGroupYear.FinPeriods : Edm.Int16 [required] "Number of Periods"
PX.Objects.PR.PRPayGroupYear.OverrideFinPeriods : Edm.Boolean [required] "Override"
PX.Objects.PR.PRPayGroupYear.EndDate : Edm.DateTimeOffset "EndDate"
PX.Objects.PR.PRPayGroupYear.UseTransactionDateExceptions : Edm.Boolean "UseTransactionDateExceptions"
PX.Objects.PR.PRPayGroupYear.TransactionDateExceptionBehavior : Edm.String "TransactionDateExceptionBehavior"
PX.Objects.PR.PRPayGroupYear.PeriodsFullyCreated : Edm.Boolean [required] "PeriodsFullyCreated"
PX.Objects.PR.PRPayGroupYear.HeaderDescription : Edm.String
PX.Objects.PR.PRPayGroupYear.tstamp : Edm.Binary
PX.Objects.PR.PRPayGroupYear.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPayGroupYear.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPayGroupYear.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroupYear.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPayGroupYear.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPayGroupYear.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroupYear.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPayGroupYear.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPayGroupYear.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup (PayGroupID=PayGroupID)
PX.Objects.PR.PRPayGroupYear.PRAcaCompanyYearlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyYearlyInformation)
PX.Objects.PR.PRPayGroupYear.PRPayGroupPeriodCollection -> Collection(PX.Objects.PR.PRPayGroupPeriod)

# PX.Objects.PR.PRPayGroupYearSetup (EntityType)

Label: "Pay Group Calendar"
Key: PayGroupID
Entity sets: PX_Objects_PR_PRPayGroupYearSetup, PayGroupCalendar, PRPayGroupYearSetup
Non-filterable, non-selectable: NoteText, IsWeeklyOrBiWeeklyPeriod, AdjustToPeriodStart, HasAdjustmentPeriod, BelongsToNextYear

PX.Objects.PR.PRPayGroupYearSetup.PayGroupID : Edm.String [key] "Pay Group"
PX.Objects.PR.PRPayGroupYearSetup.FirstFinYear : Edm.String "First Year"
PX.Objects.PR.PRPayGroupYearSetup.BegFinYear : Edm.DateTimeOffset "Year Starts On"
PX.Objects.PR.PRPayGroupYearSetup.FinPeriods : Edm.Int16 [required] "Number of Periods"
PX.Objects.PR.PRPayGroupYearSetup.UserDefined : Edm.Boolean "User-Defined Periods"
PX.Objects.PR.PRPayGroupYearSetup.NoteID : Edm.Guid
PX.Objects.PR.PRPayGroupYearSetup.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRPayGroupYearSetup.PeriodType : Edm.String "Period Type"
PX.Objects.PR.PRPayGroupYearSetup.IsWeeklyOrBiWeeklyPeriod : Edm.Boolean "Is Weekly or Biweekly Period"
PX.Objects.PR.PRPayGroupYearSetup.PeriodLength : Edm.Int16 "Length of Period (Days)"
PX.Objects.PR.PRPayGroupYearSetup.PeriodsStartDate : Edm.DateTimeOffset "First Period Starts On"
PX.Objects.PR.PRPayGroupYearSetup.TransactionsStartDate : Edm.DateTimeOffset "First Transaction Date"
PX.Objects.PR.PRPayGroupYearSetup.SecondPeriodsStartDate : Edm.DateTimeOffset "2nd Period Starts On"
PX.Objects.PR.PRPayGroupYearSetup.SecondTransactionsStartDate : Edm.DateTimeOffset "2nd Transaction Date"
PX.Objects.PR.PRPayGroupYearSetup.EndYearCalcMethod : Edm.String "Year End Calculation Method"
PX.Objects.PR.PRPayGroupYearSetup.EndYearDayOfWeek : Edm.Int32 [required] "Week Starts On"
PX.Objects.PR.PRPayGroupYearSetup.TranDayOfWeek : Edm.Int32 [required] "Paid On"
PX.Objects.PR.PRPayGroupYearSetup.TranWeekDiff : Edm.Int32 [required] "Payment Released"
PX.Objects.PR.PRPayGroupYearSetup.IsSecondWeekOfYear : Edm.Boolean "Occurs On Second Week Of Year"
PX.Objects.PR.PRPayGroupYearSetup.tstamp : Edm.Binary
PX.Objects.PR.PRPayGroupYearSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPayGroupYearSetup.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPayGroupYearSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroupYearSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPayGroupYearSetup.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPayGroupYearSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayGroupYearSetup.AdjustToPeriodStart : Edm.Boolean "Adjust To Period Start"
PX.Objects.PR.PRPayGroupYearSetup.HasAdjustmentPeriod : Edm.Boolean
PX.Objects.PR.PRPayGroupYearSetup.BelongsToNextYear : Edm.Boolean "Belongs To Next Year"
PX.Objects.PR.PRPayGroupYearSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPayGroupYearSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPayGroupYearSetup.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup (PayGroupID=PayGroupID)
PX.Objects.PR.PRPayGroupYearSetup.PRPayGroupPeriodSetupCollection -> Collection(PX.Objects.PR.PRPayGroupPeriodSetup)

# PX.Objects.PR.PRPayment (EntityType)

Label: "Payment"
Key: DocType, RefNbr
Entity sets: PX_Objects_PR_PRPayment, Payment1, PRPayment
Non-filterable, non-selectable: ReleasedToVerify, IsWeeklyOrBiWeeklyPeriod, OrganizationID, DrCr, AverageRate, ExemptFromOvertimeRules, PaymentDocAndRef, IsPrintChecksPaymentMethod, NetAmountToWords, ShowROETab, NoteText, CuryID, CuryRate, CuryViewState

PX.Objects.PR.PRPayment.DocType : Edm.String [key required] "Type"
PX.Objects.PR.PRPayment.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PR.PRPayment.Status : Edm.String "Status"
PX.Objects.PR.PRPayment.Hold : Edm.Boolean [required] "Hold"
PX.Objects.PR.PRPayment.Released : Edm.Boolean [required] "Released"
PX.Objects.PR.PRPayment.ReleasedToVerify : Edm.Boolean
PX.Objects.PR.PRPayment.Voided : Edm.Boolean [required] "Voided"
PX.Objects.PR.PRPayment.Closed : Edm.Boolean [required] "Closed"
PX.Objects.PR.PRPayment.LiabilityPartiallyPaid : Edm.Boolean [required] "Liability Partially Paid"
PX.Objects.PR.PRPayment.Paid : Edm.Boolean [required] "Paid"
PX.Objects.PR.PRPayment.Calculated : Edm.Boolean [required] "Calculated"
PX.Objects.PR.PRPayment.HasUpdatedGL : Edm.Boolean "HasUpdatedGL"
PX.Objects.PR.PRPayment.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.PR.PRPayment.PayGroupID : Edm.String "Pay Group"
PX.Objects.PR.PRPayment.IsWeeklyOrBiWeeklyPeriod : Edm.Boolean "Is Weekly or Biweekly Period"
PX.Objects.PR.PRPayment.PayPeriodID : Edm.String "Pay Period"
PX.Objects.PR.PRPayment.StartDate : Edm.DateTimeOffset "Period Start"
PX.Objects.PR.PRPayment.EndDate : Edm.DateTimeOffset "Period End"
PX.Objects.PR.PRPayment.TransactionDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.PR.PRPayment.OrganizationID : Edm.Int32
PX.Objects.PR.PRPayment.FinPeriodID : Edm.String "Posting Period"
PX.Objects.PR.PRPayment.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.PR.PRPayment.CashAccountID : Edm.Int32 "Cash Account"
PX.Objects.PR.PRPayment.DocDesc : Edm.String "Description"
PX.Objects.PR.PRPayment.ChkVoidType : Edm.String "Void Reason"
PX.Objects.PR.PRPayment.ChkCreateNew : Edm.Boolean [required] "Create New Payment from Voided Payment"
PX.Objects.PR.PRPayment.EmployeeID : Edm.Int32 "Employee"
PX.Objects.PR.PRPayment.EmpType : Edm.String "Employee Type"
PX.Objects.PR.PRPayment.RegularAmount : Edm.Decimal "Regular Amount to Be Paid"
PX.Objects.PR.PRPayment.ManualRegularAmount : Edm.Boolean [required] "Manual Amount"
PX.Objects.PR.PRPayment.PayBatchNbr : Edm.String "Pay Batch Nbr."
PX.Objects.PR.PRPayment.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.PR.PRPayment.TotalEarnings : Edm.Decimal [required] "TotalEarnings"
PX.Objects.PR.PRPayment.GrossAmount : Edm.Decimal [required] "Gross Pay"
PX.Objects.PR.PRPayment.DedAmount : Edm.Decimal [required] "Deductions"
PX.Objects.PR.PRPayment.TaxAmount : Edm.Decimal [required] "Taxes"
PX.Objects.PR.PRPayment.NetAmount : Edm.Decimal [required] "Net Pay"
PX.Objects.PR.PRPayment.CuryInfoID : Edm.Int64
PX.Objects.PR.PRPayment.PayableBenefitAmount : Edm.Decimal [required] "PayableBenefitAmount"
PX.Objects.PR.PRPayment.BenefitAmount : Edm.Decimal [required] "Total Benefits"
PX.Objects.PR.PRPayment.EmployerTaxAmount : Edm.Decimal [required] "Total Employer Tax"
PX.Objects.PR.PRPayment.CATranID : Edm.Int64
PX.Objects.PR.PRPayment.DetailLinesCount : Edm.Int32 [required] "Nbr. of Detail Lines"
PX.Objects.PR.PRPayment.OrigDocType : Edm.String "Original Doc. Type"
PX.Objects.PR.PRPayment.OrigRefNbr : Edm.String "Original Document"
PX.Objects.PR.PRPayment.DrCr : Edm.String
PX.Objects.PR.PRPayment.AverageRate : Edm.Decimal "Average Rate"
PX.Objects.PR.PRPayment.TotalHours : Edm.Decimal [required] "Total Hours"
PX.Objects.PR.PRPayment.ExemptFromOvertimeRules : Edm.Boolean "Exempt from Overtime Rules"
PX.Objects.PR.PRPayment.ApplyOvertimeRules : Edm.Boolean "Apply Overtime Rules for the Document"
PX.Objects.PR.PRPayment.PaymentDocAndRef : Edm.String "Paycheck Ref"
PX.Objects.PR.PRPayment.IsPrintChecksPaymentMethod : Edm.Boolean "Print Checks Payment Method"
PX.Objects.PR.PRPayment.NetAmountToWords : Edm.String
PX.Objects.PR.PRPayment.LaborCostSplitType : Edm.String "LaborCostSplitType"
PX.Objects.PR.PRPayment.PTOCostSplitType : Edm.String "PTOCostSplitType"
PX.Objects.PR.PRPayment.PaymentBatchNbr : Edm.String "Payment Batch Nbr."
PX.Objects.PR.PRPayment.CountryID : Edm.String "Payment country"
PX.Objects.PR.PRPayment.TerminationReason : Edm.String "Termination Reason"
PX.Objects.PR.PRPayment.ShowROETab : Edm.Boolean "ShowROETab"
PX.Objects.PR.PRPayment.IsRehirable : Edm.Boolean "Eligible for Rehire"
PX.Objects.PR.PRPayment.TerminationDate : Edm.DateTimeOffset "Termination Date"
PX.Objects.PR.PRPayment.NoteID : Edm.Guid
PX.Objects.PR.PRPayment.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRPayment.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPayment.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPayment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPayment.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPayment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPayment.CuryID : Edm.String "Currency"
PX.Objects.PR.PRPayment.CuryRate : Edm.Decimal
PX.Objects.PR.PRPayment.CuryViewState : Edm.Boolean
PX.Objects.PR.PRPayment.PREmployeeByPayGroupID -> PX.Objects.PR.PREmployee (EmployeeID=BAccountID, PayGroupID=PayGroupID)
PX.Objects.PR.PRPayment.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRPayment.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.PR.PRPayment.CATranByCaTranID -> PX.Objects.CA.CATran
PX.Objects.PR.PRPayment.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRPayment.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.PR.PRPayment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPayment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPayment.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.PRPayment.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.PR.PRPayment.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.PR.PRPayment.PRBatchByPayBatchNbr -> PX.Objects.PR.PRBatch (PayBatchNbr=BatchNbr)
PX.Objects.PR.PRPayment.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup (PayGroupID=PayGroupID)
PX.Objects.PR.PRPayment.PRPayGroupPeriodByFinPeriodID -> PX.Objects.PR.PRPayGroupPeriod (PayGroupID=PayGroupID, FinPeriodID=FinPeriodID)
PX.Objects.PR.PRPayment.PRPayGroupPeriodByPayGroupID -> PX.Objects.PR.PRPayGroupPeriod (PayPeriodID=FinPeriodID, PayGroupID=PayGroupID)
PX.Objects.PR.PRPayment.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.PR.PRPayment.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PR.PRPayment.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PR.PRPayment.PRPaymentEarningCollection -> Collection(PX.Objects.PR.PRPaymentEarning)
PX.Objects.PR.PRPayment.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.PR.PRPayment.PRPaymentTaxCollection -> Collection(PX.Objects.PR.PRPaymentTax)
PX.Objects.PR.PRPayment.PRDirectDepositSplitCollection -> Collection(PX.Objects.PR.PRDirectDepositSplit)
PX.Objects.PR.PRPayment.PRPaymentBatchExportDetailsCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportDetails)
PX.Objects.PR.PRPayment.PRPaymentDeductCollection -> Collection(PX.Objects.PR.PRPaymentDeduct)
PX.Objects.PR.PRPayment.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.PR.PRPayment.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.PR.PRPayment.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.PR.PRPayment.PRPaymentOvertimeRuleCollection -> Collection(PX.Objects.PR.PRPaymentOvertimeRule)
PX.Objects.PR.PRPayment.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.PR.PRPayment.PRPaymentPTOBankCollection -> Collection(PX.Objects.PR.PRPaymentPTOBank)
PX.Objects.PR.PRPayment.PRPaymentTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPaymentTaxApplicableAmounts)
PX.Objects.PR.PRPayment.PRPaymentTaxSplitCollection -> Collection(PX.Objects.PR.PRPaymentTaxSplit)
PX.Objects.PR.PRPayment.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.PR.PRPayment.PRPaymentWCPremiumCollection -> Collection(PX.Objects.PR.PRPaymentWCPremium)
PX.Objects.PR.PRPayment.PRPTOAdjustmentDetailCollection -> Collection(PX.Objects.PR.PRPTOAdjustmentDetail)
PX.Objects.PR.PRPayment.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.PR.PRPayment.PRRecordOfEmploymentCollection -> Collection(PX.Objects.PR.PRRecordOfEmployment)

# PX.Objects.PR.PRPaymentBatchExportDetails (EntityType)

Label: "Payment Batch Export Details"
Key: ExportHistoryLineNbr, LineNbr, PaymentBatchNbr
Entity sets: PX_Objects_PR_PRPaymentBatchExportDetails, PaymentBatchExportDetails, PRPaymentBatchExportDetails

PX.Objects.PR.PRPaymentBatchExportDetails.PaymentBatchNbr : Edm.String [key] "Payment Batch Nbr."
PX.Objects.PR.PRPaymentBatchExportDetails.ExportHistoryLineNbr : Edm.Int32 [key] "Export History Line Nbr."
PX.Objects.PR.PRPaymentBatchExportDetails.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.PR.PRPaymentBatchExportDetails.DocType : Edm.String "Type"
PX.Objects.PR.PRPaymentBatchExportDetails.RefNbr : Edm.String "Reference Nbr"
PX.Objects.PR.PRPaymentBatchExportDetails.DocDesc : Edm.String "Description"
PX.Objects.PR.PRPaymentBatchExportDetails.EmployeeID : Edm.Int32 "Employee"
PX.Objects.PR.PRPaymentBatchExportDetails.PayGroupID : Edm.String "Pay Group"
PX.Objects.PR.PRPaymentBatchExportDetails.PayPeriodID : Edm.String "Pay Period"
PX.Objects.PR.PRPaymentBatchExportDetails.NetAmount : Edm.Decimal "Net Amount"
PX.Objects.PR.PRPaymentBatchExportDetails.ExtRefNbr : Edm.String "Check Nbr."
PX.Objects.PR.PRPaymentBatchExportDetails.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentBatchExportDetails.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentBatchExportDetails.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentBatchExportDetails.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentBatchExportDetails.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentBatchExportDetails.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentBatchExportDetails.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRPaymentBatchExportDetails.CABatchByPaymentBatchNbr -> PX.Objects.CA.CABatch (PaymentBatchNbr=BatchNbr)
PX.Objects.PR.PRPaymentBatchExportDetails.BranchByPaymentBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRPaymentBatchExportDetails.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentBatchExportDetails.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentBatchExportDetails.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentBatchExportDetails.PRPaymentBatchExportHistoryByExportHistoryLineNbr -> PX.Objects.PR.PRPaymentBatchExportHistory (PaymentBatchNbr=PaymentBatchNbr, ExportHistoryLineNbr=LineNbr)

# PX.Objects.PR.PRPaymentBatchExportHistory (EntityType)

Label: "Payment Batch Export History"
Key: LineNbr, PaymentBatchNbr
Entity sets: PX_Objects_PR_PRPaymentBatchExportHistory, PaymentBatchExportHistory, PRPaymentBatchExportHistory

PX.Objects.PR.PRPaymentBatchExportHistory.PaymentBatchNbr : Edm.String [key] "Payment Batch"
PX.Objects.PR.PRPaymentBatchExportHistory.LineNbr : Edm.Int32 [key]
PX.Objects.PR.PRPaymentBatchExportHistory.UserID : Edm.Guid "User"
PX.Objects.PR.PRPaymentBatchExportHistory.ExportDateTime : Edm.DateTimeOffset "Export Time"
PX.Objects.PR.PRPaymentBatchExportHistory.Reason : Edm.String "Reason"
PX.Objects.PR.PRPaymentBatchExportHistory.BatchTotal : Edm.Decimal "Batch Total"
PX.Objects.PR.PRPaymentBatchExportHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentBatchExportHistory.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentBatchExportHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentBatchExportHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentBatchExportHistory.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentBatchExportHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentBatchExportHistory.CABatchByPaymentBatchNbr -> PX.Objects.CA.CABatch (PaymentBatchNbr=BatchNbr)
PX.Objects.PR.PRPaymentBatchExportHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentBatchExportHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentBatchExportHistory.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.PR.PRPaymentBatchExportHistory.PRPaymentBatchExportDetailsCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportDetails)

# PX.Objects.PR.PRPaymentDeduct (EntityType)

Label: "Deduction Summary"
Key: CodeID, DocType, RefNbr, Source
Entity sets: PX_Objects_PR_PRPaymentDeduct, DeductionSummary, PRPaymentDeduct
Non-filterable, non-selectable: NoFinancialTransaction, PaymentCountryID

PX.Objects.PR.PRPaymentDeduct.DocType : Edm.String [key] "Payment Doc. Type"
PX.Objects.PR.PRPaymentDeduct.RefNbr : Edm.String [key] "Payment Ref. Number"
PX.Objects.PR.PRPaymentDeduct.CodeID : Edm.Int32 [key] "Deduction Code"
PX.Objects.PR.PRPaymentDeduct.IsGarnishment : Edm.Boolean "Garnishment"
PX.Objects.PR.PRPaymentDeduct.ContribType : Edm.String "Contribution Type"
PX.Objects.PR.PRPaymentDeduct.DedAmount : Edm.Decimal "Deduction Amount"
PX.Objects.PR.PRPaymentDeduct.CntAmount : Edm.Decimal "Employer Contribution"
PX.Objects.PR.PRPaymentDeduct.PtdAmount : Edm.Decimal "PTD Amount"
PX.Objects.PR.PRPaymentDeduct.YtdAmount : Edm.Decimal [required] "YTD Amount"
PX.Objects.PR.PRPaymentDeduct.EmployerPtdAmount : Edm.Decimal "PTD Employer Amount"
PX.Objects.PR.PRPaymentDeduct.EmployerYtdAmount : Edm.Decimal [required] "YTD Employer Amount"
PX.Objects.PR.PRPaymentDeduct.WageBaseAmount : Edm.Decimal "Wage Base Amount"
PX.Objects.PR.PRPaymentDeduct.WageBaseHours : Edm.Decimal "Wage Base Hours"
PX.Objects.PR.PRPaymentDeduct.SaveOverride : Edm.Boolean "Save Override"
PX.Objects.PR.PRPaymentDeduct.IsActive : Edm.Boolean "Active"
PX.Objects.PR.PRPaymentDeduct.Source : Edm.String [key] "Source"
PX.Objects.PR.PRPaymentDeduct.NoFinancialTransaction : Edm.Boolean
PX.Objects.PR.PRPaymentDeduct.PaymentCountryID : Edm.String
PX.Objects.PR.PRPaymentDeduct.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentDeduct.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentDeduct.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentDeduct.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentDeduct.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentDeduct.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentDeduct.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentDeduct.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentDeduct.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentDeduct.PRDeductCodeByCodeID -> PX.Objects.PR.PRDeductCode (CodeID=CodeID)
PX.Objects.PR.PRPaymentDeduct.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentDeduct.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.PR.PRPaymentDeduct.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)

# PX.Objects.PR.PRPaymentEarning (EntityType)

Label: "Payment Earning"
Key: DocType, LocationID, RefNbr, TypeCD
Entity sets: PX_Objects_PR_PRPaymentEarning, PaymentEarning, PRPaymentEarning
Non-filterable, non-selectable: RoundedHours

PX.Objects.PR.PRPaymentEarning.DocType : Edm.String [key] "Payment Doc. Type"
PX.Objects.PR.PRPaymentEarning.RefNbr : Edm.String [key] "Payment Ref. Number"
PX.Objects.PR.PRPaymentEarning.TypeCD : Edm.String [key] "Code"
PX.Objects.PR.PRPaymentEarning.LocationID : Edm.Int32 [key] "Location"
PX.Objects.PR.PRPaymentEarning.Hours : Edm.Decimal "Hours"
PX.Objects.PR.PRPaymentEarning.RoundedHours : Edm.Decimal "Hours"
PX.Objects.PR.PRPaymentEarning.Rate : Edm.Decimal "Rate"
PX.Objects.PR.PRPaymentEarning.Amount : Edm.Decimal [required] "Ext Amount"
PX.Objects.PR.PRPaymentEarning.MTDAmount : Edm.Decimal [required] "MTD Amount"
PX.Objects.PR.PRPaymentEarning.QTDAmount : Edm.Decimal [required] "QTD Amount"
PX.Objects.PR.PRPaymentEarning.YTDAmount : Edm.Decimal [required] "YTD Amount"
PX.Objects.PR.PRPaymentEarning.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentEarning.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentEarning.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentEarning.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentEarning.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentEarning.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentEarning.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentEarning.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentEarning.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentEarning.EPEarningTypeByTypeCD -> PX.Objects.EP.EPEarningType (TypeCD=TypeCD)
PX.Objects.PR.PRPaymentEarning.PRLocationByLocationID -> PX.Objects.PR.PRLocation (LocationID=LocationID)
PX.Objects.PR.PRPaymentEarning.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentEarning.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)

# PX.Objects.PR.PRPaymentEarningAggregatedByCode (EntityType)

Label: "Payment Earning Aggregated by Earning Type Code"
Key: DocType, RefNbr, TypeCD
Entity sets: PX_Objects_PR_PRPaymentEarningAggregatedByCode, PaymentEarningAggregatedbyEarningTypeCode, PRPaymentEarningAggregatedByCode

PX.Objects.PR.PRPaymentEarningAggregatedByCode.DocType : Edm.String [key] "Payment Doc. Type"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.RefNbr : Edm.String [key] "Payment Ref. Number"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.TypeCD : Edm.String [key] "Code"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.Hours : Edm.Decimal "Hours"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.RoundedHours : Edm.Decimal "Hours"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.Amount : Edm.Decimal "Ext Amount"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.MTDAmount : Edm.Decimal "MTD Amount"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.QTDAmount : Edm.Decimal "QTD Amount"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.YTDAmount : Edm.Decimal "YTD Amount"
PX.Objects.PR.PRPaymentEarningAggregatedByCode.EPEarningTypeByTypeCD -> PX.Objects.EP.EPEarningType (TypeCD=TypeCD)
PX.Objects.PR.PRPaymentEarningAggregatedByCode.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.PR.PRPaymentFringeBenefit (EntityType)

Label: "Payment Fringe Benefit"
Key: RecordID
Entity sets: PX_Objects_PR_PRPaymentFringeBenefit, PaymentFringeBenefit, PRPaymentFringeBenefit
Non-filterable, non-selectable: CalculatedFringeRate

PX.Objects.PR.PRPaymentFringeBenefit.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRPaymentFringeBenefit.DocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRPaymentFringeBenefit.RefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRPaymentFringeBenefit.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRPaymentFringeBenefit.ApplicableHours : Edm.Decimal [required] "Applicable Hours"
PX.Objects.PR.PRPaymentFringeBenefit.ProjectHours : Edm.Decimal [required] "Project Hours"
PX.Objects.PR.PRPaymentFringeBenefit.FringeRate : Edm.Decimal [required] "Fringe Rate"
PX.Objects.PR.PRPaymentFringeBenefit.ReducingRate : Edm.Decimal [required] "Benefit Rate Reducing the Fringe Rate"
PX.Objects.PR.PRPaymentFringeBenefit.PaidFringeAmount : Edm.Decimal [required] "Paid Fringe Amount"
PX.Objects.PR.PRPaymentFringeBenefit.FringeAmountInBenefit : Edm.Decimal [required]
PX.Objects.PR.PRPaymentFringeBenefit.CalculatedFringeRate : Edm.Decimal "Calculated Fringe Rate"
PX.Objects.PR.PRPaymentFringeBenefit.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentFringeBenefit.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentFringeBenefit.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentFringeBenefit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentFringeBenefit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentFringeBenefit.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentFringeBenefit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentFringeBenefit.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PRPaymentFringeBenefit.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRPaymentFringeBenefit.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRPaymentFringeBenefit.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PR.PRPaymentFringeBenefit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentFringeBenefit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentFringeBenefit.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentFringeBenefit.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.PR.PRPaymentFringeBenefit.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)

# PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate (EntityType)

Label: "Payment Fringe Benefit Decreasing Rate"
Key: RecordID
Entity sets: PX_Objects_PR_PRPaymentFringeBenefitDecreasingRate, PaymentFringeBenefitDecreasingRate, PRPaymentFringeBenefitDecreasingRate
Non-filterable, non-selectable: AnnualizationException, CountryUS

PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.DocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.RefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.DeductCodeID : Edm.Int32 "Deduction and Benefit Code"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.ApplicableHours : Edm.Decimal "Applicable Hours"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.Amount : Edm.Decimal "Amount"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.BenefitRate : Edm.Decimal "Benefit Rate"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.AnnualHours : Edm.Int32 "Annual Hours"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.AnnualWeeks : Edm.Byte "Annual Weeks"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.AnnualizationException : Edm.Boolean "Annualization Exception"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.CountryUS : Edm.String
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate.PRPaymentFringeBenefitByProjectTaskID -> PX.Objects.PR.PRPaymentFringeBenefit (DocType=DocType, RefNbr=RefNbr, LaborItemID=LaborItemID)

# PX.Objects.PR.PRPaymentFringeEarningDecreasingRate (EntityType)

Label: "Payment Fringe Earning Decreasing Rate"
Key: RecordID
Entity sets: PX_Objects_PR_PRPaymentFringeEarningDecreasingRate, PaymentFringeEarningDecreasingRate, PRPaymentFringeEarningDecreasingRate
Non-filterable, non-selectable: AnnualizationException

PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.DocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.RefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.EarningTypeCD : Edm.String "Earning Type Code"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.ApplicableHours : Edm.Decimal "Applicable Hours"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.Amount : Edm.Decimal "Amount"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.BenefitRate : Edm.Decimal "Benefit Rate"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.AnnualHours : Edm.Int32 "Annual Hours"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.AnnualWeeks : Edm.Byte "Annual Weeks"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.ActualPayRate : Edm.Decimal [required] "Pay Rate"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.PrevailingWage : Edm.Decimal [required] "Prevailing Wage"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.AnnualizationException : Edm.Boolean "Annualization Exception"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.EPEarningTypeByEarningTypeCD -> PX.Objects.EP.EPEarningType (EarningTypeCD=TypeCD)
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentFringeEarningDecreasingRate.PRPaymentFringeBenefitByProjectTaskID -> PX.Objects.PR.PRPaymentFringeBenefit (DocType=DocType, RefNbr=RefNbr, LaborItemID=LaborItemID)

# PX.Objects.PR.PRPaymentOvertimeRule (EntityType)

Label: "Payment Overtime Rule"
Key: OvertimeRuleID, PaymentDocType, PaymentRefNbr
Entity sets: PX_Objects_PR_PRPaymentOvertimeRule, PaymentOvertimeRule, PRPaymentOvertimeRule
Non-filterable, non-selectable: RuleType

PX.Objects.PR.PRPaymentOvertimeRule.PaymentDocType : Edm.String [key] "Payment Type"
PX.Objects.PR.PRPaymentOvertimeRule.PaymentRefNbr : Edm.String [key] "Payment Reference Nbr."
PX.Objects.PR.PRPaymentOvertimeRule.OvertimeRuleID : Edm.String [key] "Overtime Rule"
PX.Objects.PR.PRPaymentOvertimeRule.RuleType : Edm.String "RuleType"
PX.Objects.PR.PRPaymentOvertimeRule.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PRPaymentOvertimeRule.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentOvertimeRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentOvertimeRule.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentOvertimeRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentOvertimeRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentOvertimeRule.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentOvertimeRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentOvertimeRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentOvertimeRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentOvertimeRule.PROvertimeRuleByOvertimeRuleID -> PX.Objects.PR.PROvertimeRule (OvertimeRuleID=OvertimeRuleID)
PX.Objects.PR.PRPaymentOvertimeRule.PRPaymentByPaymentRefNbr -> PX.Objects.PR.PRPayment (PaymentDocType=DocType, PaymentRefNbr=RefNbr)

# PX.Objects.PR.PRPaymentProjectPackageDeduct (EntityType)

Label: "Payment Project Package Deduction"
Key: RecordID
Entity sets: PX_Objects_PR_PRPaymentProjectPackageDeduct, PaymentProjectPackageDeduction, PRPaymentProjectPackageDeduct
Non-filterable, non-selectable: WageBaseHours, WageBaseAmount, DeductionCalcType, BenefitCalcType, CountryUS

PX.Objects.PR.PRPaymentProjectPackageDeduct.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRPaymentProjectPackageDeduct.DocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRPaymentProjectPackageDeduct.RefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRPaymentProjectPackageDeduct.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRPaymentProjectPackageDeduct.DeductCodeID : Edm.Int32 "Deduction Code"
PX.Objects.PR.PRPaymentProjectPackageDeduct.RegularWageBaseHours : Edm.Decimal [required] "Applicable Regular Hours"
PX.Objects.PR.PRPaymentProjectPackageDeduct.OvertimeWageBaseHours : Edm.Decimal [required] "Applicable Overtime Hours"
PX.Objects.PR.PRPaymentProjectPackageDeduct.WageBaseHours : Edm.Decimal "Total Applicable Hours"
PX.Objects.PR.PRPaymentProjectPackageDeduct.RegularWageBaseAmount : Edm.Decimal [required] "Applicable Regular Wages"
PX.Objects.PR.PRPaymentProjectPackageDeduct.OvertimeWageBaseAmount : Edm.Decimal [required] "Applicable Overtime Wages"
PX.Objects.PR.PRPaymentProjectPackageDeduct.WageBaseAmount : Edm.Decimal "Total Applicable Wages"
PX.Objects.PR.PRPaymentProjectPackageDeduct.DeductionAmount : Edm.Decimal [required] "Deduction Amount"
PX.Objects.PR.PRPaymentProjectPackageDeduct.BenefitAmount : Edm.Decimal [required] "Benefit Amount"
PX.Objects.PR.PRPaymentProjectPackageDeduct.ContribType : Edm.String
PX.Objects.PR.PRPaymentProjectPackageDeduct.DeductionCalcType : Edm.String "Deduction Calculation Method"
PX.Objects.PR.PRPaymentProjectPackageDeduct.BenefitCalcType : Edm.String "Benefit Calculation Method"
PX.Objects.PR.PRPaymentProjectPackageDeduct.CountryUS : Edm.String
PX.Objects.PR.PRPaymentProjectPackageDeduct.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentProjectPackageDeduct.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentProjectPackageDeduct.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentProjectPackageDeduct.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentProjectPackageDeduct.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentProjectPackageDeduct.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentProjectPackageDeduct.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentProjectPackageDeduct.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PRPaymentProjectPackageDeduct.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PR.PRPaymentProjectPackageDeduct.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentProjectPackageDeduct.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentProjectPackageDeduct.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRPaymentProjectPackageDeduct.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.PR.PRPaymentPTOBank (EntityType)

Label: "Payment PTO Bank"
Key: BankID, DocType, EffectiveStartDate, RefNbr
Entity sets: PX_Objects_PR_PRPaymentPTOBank, PaymentPTOBank, PRPaymentPTOBank
Non-filterable, non-selectable: EarningTypeCD, EffectiveCoefficient, TotalAccrual, TotalDisbursement, CreateFinancialTransaction, CalculationFormula

PX.Objects.PR.PRPaymentPTOBank.DocType : Edm.String [key] "Type"
PX.Objects.PR.PRPaymentPTOBank.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PR.PRPaymentPTOBank.BankID : Edm.String [key] "PTO Bank"
PX.Objects.PR.PRPaymentPTOBank.EffectiveStartDate : Edm.DateTimeOffset [key] "Effective Date"
PX.Objects.PR.PRPaymentPTOBank.EffectiveEndDate : Edm.DateTimeOffset "Effective End Date"
PX.Objects.PR.PRPaymentPTOBank.EarningTypeCD : Edm.String "Disbursing Earning Type"
PX.Objects.PR.PRPaymentPTOBank.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PRPaymentPTOBank.IsCertifiedJob : Edm.Boolean [required] "Applies to Certified Job Only"
PX.Objects.PR.PRPaymentPTOBank.AccrualMethod : Edm.String "Accrual Method"
PX.Objects.PR.PRPaymentPTOBank.AccrualRate : Edm.Decimal "Accrual %"
PX.Objects.PR.PRPaymentPTOBank.HoursPerYear : Edm.Decimal [required] "Hours per Year"
PX.Objects.PR.PRPaymentPTOBank.AccrualLimit : Edm.Decimal "Balance Limit"
PX.Objects.PR.PRPaymentPTOBank.AccumulatedAmount : Edm.Decimal "Total Accrued Hours"
PX.Objects.PR.PRPaymentPTOBank.UsedAmount : Edm.Decimal "Total Used Hours"
PX.Objects.PR.PRPaymentPTOBank.AvailableAmount : Edm.Decimal "Total Available Hours"
PX.Objects.PR.PRPaymentPTOBank.AccruingHours : Edm.Decimal [required]
PX.Objects.PR.PRPaymentPTOBank.AccruingDays : Edm.Int32
PX.Objects.PR.PRPaymentPTOBank.DaysInPeriod : Edm.Int32
PX.Objects.PR.PRPaymentPTOBank.EffectiveCoefficient : Edm.Decimal
PX.Objects.PR.PRPaymentPTOBank.AccrualAmount : Edm.Decimal [required] "Paycheck Accrual Hours"
PX.Objects.PR.PRPaymentPTOBank.DisbursementAmount : Edm.Decimal [required] "Disbursement Hours"
PX.Objects.PR.PRPaymentPTOBank.ProcessedFrontLoading : Edm.Boolean [required] "Processed Front Loading"
PX.Objects.PR.PRPaymentPTOBank.FrontLoadingAmount : Edm.Decimal [required] "Front Loading Hours"
PX.Objects.PR.PRPaymentPTOBank.ProcessedCarryover : Edm.Boolean [required] "Processed Carryover"
PX.Objects.PR.PRPaymentPTOBank.CarryoverAmount : Edm.Decimal [required] "Carryover Hours"
PX.Objects.PR.PRPaymentPTOBank.TotalAccrual : Edm.Decimal "Paycheck Total Accrual Hours"
PX.Objects.PR.PRPaymentPTOBank.TotalDisbursement : Edm.Decimal "Paycheck Disbursed Hours"
PX.Objects.PR.PRPaymentPTOBank.AdjustmentHours : Edm.Decimal [required] "Adjustment Hours"
PX.Objects.PR.PRPaymentPTOBank.AdjustmentCarryoverHours : Edm.Decimal [required] "Adjustment Carryover Hours"
PX.Objects.PR.PRPaymentPTOBank.CreateFinancialTransaction : Edm.Boolean
PX.Objects.PR.PRPaymentPTOBank.NbrOfPayPeriods : Edm.Int16
PX.Objects.PR.PRPaymentPTOBank.CalculationFormula : Edm.String "Paycheck Accrual Calculation"
PX.Objects.PR.PRPaymentPTOBank.SettlementDiscardAmount : Edm.Decimal [required] "Settlement Discard Amount"
PX.Objects.PR.PRPaymentPTOBank.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentPTOBank.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentPTOBank.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentPTOBank.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentPTOBank.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentPTOBank.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentPTOBank.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentPTOBank.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentPTOBank.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentPTOBank.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentPTOBank.PRPTOBankByBankID -> PX.Objects.PR.PRPTOBank (BankID=BankID)

# PX.Objects.PR.PRPaymentTax (EntityType)

Label: "Payment Tax"
Key: DocType, RefNbr, TaxID
Entity sets: PX_Objects_PR_PRPaymentTax, PaymentTax, PRPaymentTax
Non-filterable, non-selectable: PaymentCountryID

PX.Objects.PR.PRPaymentTax.DocType : Edm.String [key] "Payment Doc. Type"
PX.Objects.PR.PRPaymentTax.RefNbr : Edm.String [key] "Payment Ref. Number"
PX.Objects.PR.PRPaymentTax.TaxID : Edm.Int32 [key] "Code"
PX.Objects.PR.PRPaymentTax.TaxCategory : Edm.String "Tax Category"
PX.Objects.PR.PRPaymentTax.TaxAmount : Edm.Decimal [required] "Tax Amount"
PX.Objects.PR.PRPaymentTax.YtdAmount : Edm.Decimal "YTD Amount"
PX.Objects.PR.PRPaymentTax.WageBaseAmount : Edm.Decimal "Taxable Wages"
PX.Objects.PR.PRPaymentTax.PickupAmount : Edm.Decimal [required] "Pickup Amount"
PX.Objects.PR.PRPaymentTax.WageBaseHours : Edm.Decimal "Taxable Hours"
PX.Objects.PR.PRPaymentTax.WageBaseGrossAmt : Edm.Decimal "Taxable Gross"
PX.Objects.PR.PRPaymentTax.AdjustedGrossAmount : Edm.Decimal [required] "Adjusted Gross Amount"
PX.Objects.PR.PRPaymentTax.ExemptionAmount : Edm.Decimal [required] "Exemption Amount"
PX.Objects.PR.PRPaymentTax.PaymentCountryID : Edm.String
PX.Objects.PR.PRPaymentTax.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentTax.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentTax.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentTax.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PRPaymentTax.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentTax.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PR.PRPaymentTax.PRPaymentTaxSplitCollection -> Collection(PX.Objects.PR.PRPaymentTaxSplit)

# PX.Objects.PR.PRPaymentTaxApplicableAmounts (EntityType)

Label: "Payment Tax Applicable Amounts"
Key: DocType, IsSupplemental, RefNbr, TaxID, WageTypeID
Entity sets: PX_Objects_PR_PRPaymentTaxApplicableAmounts, PaymentTaxApplicableAmounts, PRPaymentTaxApplicableAmounts
Non-filterable, non-selectable: PaymentCountryID

PX.Objects.PR.PRPaymentTaxApplicableAmounts.DocType : Edm.String [key]
PX.Objects.PR.PRPaymentTaxApplicableAmounts.RefNbr : Edm.String [key]
PX.Objects.PR.PRPaymentTaxApplicableAmounts.TaxID : Edm.Int32 [key] "Code"
PX.Objects.PR.PRPaymentTaxApplicableAmounts.WageTypeID : Edm.Int32 [key] "Wage Type"
PX.Objects.PR.PRPaymentTaxApplicableAmounts.IsSupplemental : Edm.Boolean [key required] "Is Supplemental"
PX.Objects.PR.PRPaymentTaxApplicableAmounts.AmountAllowed : Edm.Decimal [required] "Amount Allowed"
PX.Objects.PR.PRPaymentTaxApplicableAmounts.PaymentCountryID : Edm.String
PX.Objects.PR.PRPaymentTaxApplicableAmounts.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentTaxApplicableAmounts.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentTaxApplicableAmounts.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentTaxApplicableAmounts.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentTaxApplicableAmounts.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentTaxApplicableAmounts.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentTaxApplicableAmounts.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentTaxApplicableAmounts.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentTaxApplicableAmounts.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentTaxApplicableAmounts.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PRPaymentTaxApplicableAmounts.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.PR.PRPaymentTaxSplit (EntityType)

Label: "Tax Splits"
Key: RecordID
Entity sets: PX_Objects_PR_PRPaymentTaxSplit, TaxSplits, PRPaymentTaxSplit
Non-filterable, non-selectable: CountryID

PX.Objects.PR.PRPaymentTaxSplit.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRPaymentTaxSplit.DocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRPaymentTaxSplit.RefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRPaymentTaxSplit.TaxID : Edm.Int32 "Code"
PX.Objects.PR.PRPaymentTaxSplit.WageType : Edm.Int32 "Type"
PX.Objects.PR.PRPaymentTaxSplit.WageBaseAmount : Edm.Decimal "Taxable Wages"
PX.Objects.PR.PRPaymentTaxSplit.PickupAmount : Edm.Decimal [required] "Pickup Amount"
PX.Objects.PR.PRPaymentTaxSplit.CountryID : Edm.String
PX.Objects.PR.PRPaymentTaxSplit.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentTaxSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentTaxSplit.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentTaxSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentTaxSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentTaxSplit.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentTaxSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentTaxSplit.TaxAmount : Edm.Decimal [required]
PX.Objects.PR.PRPaymentTaxSplit.WageBaseHours : Edm.Decimal
PX.Objects.PR.PRPaymentTaxSplit.WageBaseGrossAmt : Edm.Decimal
PX.Objects.PR.PRPaymentTaxSplit.SubjectCommissionAmount : Edm.Decimal
PX.Objects.PR.PRPaymentTaxSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentTaxSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentTaxSplit.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PRPaymentTaxSplit.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.PR.PRPaymentTaxSplit.PRPaymentTaxByTaxID -> PX.Objects.PR.PRPaymentTax (DocType=DocType, RefNbr=RefNbr, TaxID=TaxID)

# PX.Objects.PR.PRPaymentUnionPackageDeduct (EntityType)

Label: "Payment Union Package Deduction"
Key: RecordID
Entity sets: PX_Objects_PR_PRPaymentUnionPackageDeduct, PaymentUnionPackageDeduction, PRPaymentUnionPackageDeduct
Non-filterable, non-selectable: WageBaseHours, WageBaseAmount, DeductionCalcType, BenefitCalcType, PaymentCountryID

PX.Objects.PR.PRPaymentUnionPackageDeduct.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRPaymentUnionPackageDeduct.DocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRPaymentUnionPackageDeduct.RefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRPaymentUnionPackageDeduct.UnionID : Edm.String "Union"
PX.Objects.PR.PRPaymentUnionPackageDeduct.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRPaymentUnionPackageDeduct.DeductCodeID : Edm.Int32 "Deduction Code"
PX.Objects.PR.PRPaymentUnionPackageDeduct.RegularWageBaseHours : Edm.Decimal [required] "Applicable Regular Hours"
PX.Objects.PR.PRPaymentUnionPackageDeduct.OvertimeWageBaseHours : Edm.Decimal [required] "Applicable Overtime Hours"
PX.Objects.PR.PRPaymentUnionPackageDeduct.RegularWageBaseAmount : Edm.Decimal [required] "Applicable Regular Wages"
PX.Objects.PR.PRPaymentUnionPackageDeduct.OvertimeWageBaseAmount : Edm.Decimal [required] "Applicable Overtime Wages"
PX.Objects.PR.PRPaymentUnionPackageDeduct.WageBaseHours : Edm.Decimal "Total Applicable Hours"
PX.Objects.PR.PRPaymentUnionPackageDeduct.WageBaseAmount : Edm.Decimal "Total Applicable Wages"
PX.Objects.PR.PRPaymentUnionPackageDeduct.DeductionAmount : Edm.Decimal [required] "Deduction Amount"
PX.Objects.PR.PRPaymentUnionPackageDeduct.BenefitAmount : Edm.Decimal [required] "Benefit Amount"
PX.Objects.PR.PRPaymentUnionPackageDeduct.ContribType : Edm.String
PX.Objects.PR.PRPaymentUnionPackageDeduct.DeductionCalcType : Edm.String "Deduction Calculation Method"
PX.Objects.PR.PRPaymentUnionPackageDeduct.BenefitCalcType : Edm.String "Benefit Calculation Method"
PX.Objects.PR.PRPaymentUnionPackageDeduct.PaymentCountryID : Edm.String
PX.Objects.PR.PRPaymentUnionPackageDeduct.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentUnionPackageDeduct.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentUnionPackageDeduct.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentUnionPackageDeduct.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentUnionPackageDeduct.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentUnionPackageDeduct.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentUnionPackageDeduct.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentUnionPackageDeduct.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PR.PRPaymentUnionPackageDeduct.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentUnionPackageDeduct.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentUnionPackageDeduct.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRPaymentUnionPackageDeduct.PMUnionByUnionID -> PX.Objects.PM.PMUnion (UnionID=UnionID)
PX.Objects.PR.PRPaymentUnionPackageDeduct.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.PR.PRPaymentWCPremium (EntityType)

Label: "Payment Work Compensation Premium"
Key: BranchID, ContribType, DeductCodeID, DocType, RefNbr, WorkCodeID
Entity sets: PX_Objects_PR_PRPaymentWCPremium, PaymentWorkCompensationPremium, PRPaymentWCPremium
Non-filterable, non-selectable: WageBaseAmount, WageBaseHours, DeductionCalcType, BenefitCalcType, PaymentCountryID

PX.Objects.PR.PRPaymentWCPremium.DocType : Edm.String [key] "Payment Doc. Type"
PX.Objects.PR.PRPaymentWCPremium.RefNbr : Edm.String [key] "Payment Ref. Number"
PX.Objects.PR.PRPaymentWCPremium.WorkCodeID : Edm.String [key] "WCC Code"
PX.Objects.PR.PRPaymentWCPremium.DeductCodeID : Edm.Int32 [key] "Deduction Code"
PX.Objects.PR.PRPaymentWCPremium.DeductionRate : Edm.Decimal "Deduction Rate"
PX.Objects.PR.PRPaymentWCPremium.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.PR.PRPaymentWCPremium.Rate : Edm.Decimal "Benefit Rate"
PX.Objects.PR.PRPaymentWCPremium.DeductionAmount : Edm.Decimal "Deduction Amount"
PX.Objects.PR.PRPaymentWCPremium.Amount : Edm.Decimal [required] "Benefit Amount"
PX.Objects.PR.PRPaymentWCPremium.RegularWageBaseAmount : Edm.Decimal [required] "Applicable Regular Wages"
PX.Objects.PR.PRPaymentWCPremium.OvertimeWageBaseAmount : Edm.Decimal [required] "Applicable Overtime Wages"
PX.Objects.PR.PRPaymentWCPremium.WageBaseAmount : Edm.Decimal "Total Applicable Wages"
PX.Objects.PR.PRPaymentWCPremium.RegularWageBaseHours : Edm.Decimal [required] "Applicable Regular Hours"
PX.Objects.PR.PRPaymentWCPremium.OvertimeWageBaseHours : Edm.Decimal [required] "Applicable Overtime Hours"
PX.Objects.PR.PRPaymentWCPremium.WageBaseHours : Edm.Decimal "Total Applicable Hours"
PX.Objects.PR.PRPaymentWCPremium.ContribType : Edm.String [key]
PX.Objects.PR.PRPaymentWCPremium.DeductionCalcType : Edm.String "Deduction Calculation Method"
PX.Objects.PR.PRPaymentWCPremium.BenefitCalcType : Edm.String "Benefit Calculation Method"
PX.Objects.PR.PRPaymentWCPremium.PaymentCountryID : Edm.String
PX.Objects.PR.PRPaymentWCPremium.TStamp : Edm.Binary
PX.Objects.PR.PRPaymentWCPremium.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPaymentWCPremium.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPaymentWCPremium.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentWCPremium.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPaymentWCPremium.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPaymentWCPremium.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPaymentWCPremium.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.PR.PRPaymentWCPremium.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPaymentWCPremium.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPaymentWCPremium.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRPaymentWCPremium.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)
PX.Objects.PR.PRPaymentWCPremium.PRPaymentByRefNbr -> PX.Objects.PR.PRPayment (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.PR.PRPeriodTaxApplicableAmounts (EntityType)

Label: "Period Tax Applicable Amounts"
Key: EmployeeID, IsSupplemental, PeriodNbr, TaxID, WageTypeID, Year
Entity sets: PX_Objects_PR_PRPeriodTaxApplicableAmounts, PeriodTaxApplicableAmounts, PRPeriodTaxApplicableAmounts

PX.Objects.PR.PRPeriodTaxApplicableAmounts.Year : Edm.String [key]
PX.Objects.PR.PRPeriodTaxApplicableAmounts.EmployeeID : Edm.Int32 [key]
PX.Objects.PR.PRPeriodTaxApplicableAmounts.TaxID : Edm.Int32 [key]
PX.Objects.PR.PRPeriodTaxApplicableAmounts.WageTypeID : Edm.Int32 [key]
PX.Objects.PR.PRPeriodTaxApplicableAmounts.IsSupplemental : Edm.Boolean [key]
PX.Objects.PR.PRPeriodTaxApplicableAmounts.PeriodNbr : Edm.Int32 [key]
PX.Objects.PR.PRPeriodTaxApplicableAmounts.Week : Edm.Int32
PX.Objects.PR.PRPeriodTaxApplicableAmounts.Month : Edm.Int32
PX.Objects.PR.PRPeriodTaxApplicableAmounts.AmountAllowed : Edm.Decimal [required]
PX.Objects.PR.PRPeriodTaxApplicableAmounts.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPeriodTaxApplicableAmounts.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPeriodTaxApplicableAmounts.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPeriodTaxApplicableAmounts.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPeriodTaxApplicableAmounts.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPeriodTaxApplicableAmounts.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPeriodTaxApplicableAmounts.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRPeriodTaxApplicableAmounts.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPeriodTaxApplicableAmounts.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPeriodTaxApplicableAmounts.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)

# PX.Objects.PR.PRPeriodTaxes (EntityType)

Label: "Period Taxes"
Key: EmployeeID, PeriodNbr, TaxID, Year
Entity sets: PX_Objects_PR_PRPeriodTaxes, PeriodTaxes, PRPeriodTaxes

PX.Objects.PR.PRPeriodTaxes.Year : Edm.String [key] "Year"
PX.Objects.PR.PRPeriodTaxes.EmployeeID : Edm.Int32 [key] "Employee"
PX.Objects.PR.PRPeriodTaxes.TaxID : Edm.Int32 [key] "Tax Code"
PX.Objects.PR.PRPeriodTaxes.PeriodNbr : Edm.Int32 [key] "Period"
PX.Objects.PR.PRPeriodTaxes.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRPeriodTaxes.PickupAmount : Edm.Decimal [required]
PX.Objects.PR.PRPeriodTaxes.AdjustedGrossAmount : Edm.Decimal [required]
PX.Objects.PR.PRPeriodTaxes.ExemptionAmount : Edm.Decimal [required]
PX.Objects.PR.PRPeriodTaxes.Week : Edm.Int32 "Week"
PX.Objects.PR.PRPeriodTaxes.Month : Edm.Int32 "Month"
PX.Objects.PR.PRPeriodTaxes.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPeriodTaxes.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPeriodTaxes.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPeriodTaxes.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPeriodTaxes.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPeriodTaxes.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPeriodTaxes.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRPeriodTaxes.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPeriodTaxes.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPeriodTaxes.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PRPeriodTaxes.PRYtdTaxesByTaxID -> PX.Objects.PR.PRYtdTaxes (Year=Year, EmployeeID=EmployeeID, TaxID=TaxID)

# PX.Objects.PR.PRProjectFringeBenefitRate (EntityType)

Label: "Project Fringe Benefit Rate"
Key: RecordID
Entity sets: PX_Objects_PR_PRProjectFringeBenefitRate, ProjectFringeBenefitRate, PRProjectFringeBenefitRate

PX.Objects.PR.PRProjectFringeBenefitRate.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRProjectFringeBenefitRate.ProjectID : Edm.Int32
PX.Objects.PR.PRProjectFringeBenefitRate.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRProjectFringeBenefitRate.Rate : Edm.Decimal [required] "Rate"
PX.Objects.PR.PRProjectFringeBenefitRate.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.PR.PRProjectFringeBenefitRate.TStamp : Edm.Binary
PX.Objects.PR.PRProjectFringeBenefitRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRProjectFringeBenefitRate.CreatedByScreenID : Edm.String
PX.Objects.PR.PRProjectFringeBenefitRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRProjectFringeBenefitRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRProjectFringeBenefitRate.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRProjectFringeBenefitRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRProjectFringeBenefitRate.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PR.PRProjectFringeBenefitRate.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PR.PRProjectFringeBenefitRate.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.PR.PRProjectFringeBenefitRate.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.PR.PRProjectFringeBenefitRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRProjectFringeBenefitRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct (EntityType)

Label: "Project Fringe Benefit Rate Reducing Deduction"
Key: DeductCodeID, ProjectID
Entity sets: PX_Objects_PR_PRProjectFringeBenefitRateReducingDeduct, ProjectFringeBenefitRateReducingDeduction, PRProjectFringeBenefitRateReducingDeduct
Non-filterable, non-selectable: CountryUS

PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.ProjectID : Edm.Int32 [key]
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.DeductCodeID : Edm.Int32 [key] "Benefit Code"
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.AnnualizationException : Edm.Boolean [required] "Annualization Exception"
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.CountryUS : Edm.String
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.TStamp : Edm.Binary
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.CreatedByScreenID : Edm.String
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)

# PX.Objects.PR.PRPTOAdjustment (EntityType)

Label: "PTO Adjustment"
Key: RefNbr, Type
Entity sets: PX_Objects_PR_PRPTOAdjustment, PTOAdjustment, PRPTOAdjustment

PX.Objects.PR.PRPTOAdjustment.Type : Edm.String [key required] "Type"
PX.Objects.PR.PRPTOAdjustment.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PR.PRPTOAdjustment.Status : Edm.String "Status"
PX.Objects.PR.PRPTOAdjustment.Date : Edm.DateTimeOffset "Date"
PX.Objects.PR.PRPTOAdjustment.Description : Edm.String "Description"
PX.Objects.PR.PRPTOAdjustment.TStamp : Edm.Binary
PX.Objects.PR.PRPTOAdjustment.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPTOAdjustment.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPTOAdjustment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPTOAdjustment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPTOAdjustment.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPTOAdjustment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPTOAdjustment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPTOAdjustment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPTOAdjustment.PRPTOAdjustmentDetailCollection -> Collection(PX.Objects.PR.PRPTOAdjustmentDetail)

# PX.Objects.PR.PRPTOAdjustmentDetail (EntityType)

Label: "PTO Adjustment Detail"
Key: BAccountID, BankID, RefNbr, Type
Entity sets: PX_Objects_PR_PRPTOAdjustmentDetail, PTOAdjustmentDetail, PRPTOAdjustmentDetail

PX.Objects.PR.PRPTOAdjustmentDetail.Type : Edm.String [key]
PX.Objects.PR.PRPTOAdjustmentDetail.RefNbr : Edm.String [key]
PX.Objects.PR.PRPTOAdjustmentDetail.BAccountID : Edm.Int32 [key] "Employee"
PX.Objects.PR.PRPTOAdjustmentDetail.BankID : Edm.String [key] "PTO Bank"
PX.Objects.PR.PRPTOAdjustmentDetail.EffectiveStartDate : Edm.DateTimeOffset "PTO Bank Effective From"
PX.Objects.PR.PRPTOAdjustmentDetail.PaymentDocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRPTOAdjustmentDetail.PaymentRefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRPTOAdjustmentDetail.InitialBalance : Edm.Decimal [required] "Initial Balance"
PX.Objects.PR.PRPTOAdjustmentDetail.AdjustmentHours : Edm.Decimal "Adjustment Hours"
PX.Objects.PR.PRPTOAdjustmentDetail.AdjustmentReason : Edm.String "Adjustment Reason"
PX.Objects.PR.PRPTOAdjustmentDetail.ReasonDetails : Edm.String "Reason Details"
PX.Objects.PR.PRPTOAdjustmentDetail.NewBalance : Edm.Decimal "New Balance"
PX.Objects.PR.PRPTOAdjustmentDetail.BalanceLimit : Edm.Decimal "Balance Limit"
PX.Objects.PR.PRPTOAdjustmentDetail.TStamp : Edm.Binary
PX.Objects.PR.PRPTOAdjustmentDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPTOAdjustmentDetail.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPTOAdjustmentDetail.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.PR.PRPTOAdjustmentDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPTOAdjustmentDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPTOAdjustmentDetail.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.PR.PRPTOAdjustmentDetail.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PRPTOAdjustmentDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPTOAdjustmentDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPTOAdjustmentDetail.PRPaymentByPaymentRefNbr -> PX.Objects.PR.PRPayment (PaymentDocType=DocType, PaymentRefNbr=RefNbr)
PX.Objects.PR.PRPTOAdjustmentDetail.PRPTOAdjustmentByRefNbr -> PX.Objects.PR.PRPTOAdjustment (Type=Type, RefNbr=RefNbr)
PX.Objects.PR.PRPTOAdjustmentDetail.PRPTOBankByBankID -> PX.Objects.PR.PRPTOBank (BankID=BankID)

# PX.Objects.PR.PRPTOBank (EntityType)

Label: "PTO Bank"
Key: BankID
Entity sets: PX_Objects_PR_PRPTOBank, PTOBank, PRPTOBank
Non-filterable, non-selectable: StartDateMonth, StartDateDay, PTOYearStartDate, IsPercentageBased

PX.Objects.PR.PRPTOBank.BankID : Edm.String [key] "Bank ID"
PX.Objects.PR.PRPTOBank.Description : Edm.String "Description"
PX.Objects.PR.PRPTOBank.AccrualMethod : Edm.String "Accrual Method"
PX.Objects.PR.PRPTOBank.EarningTypeCD : Edm.String "Disbursing Earning Type"
PX.Objects.PR.PRPTOBank.IsActive : Edm.Boolean [required] "Active"
PX.Objects.PR.PRPTOBank.ApplyBandingRules : Edm.Boolean [required] "Apply Banding Rules"
PX.Objects.PR.PRPTOBank.IsCertifiedJobAccrual : Edm.Boolean [required] "Accrue Only on Certified Job"
PX.Objects.PR.PRPTOBank.StartDate : Edm.DateTimeOffset "Transfer Date"
PX.Objects.PR.PRPTOBank.StartDateMonth : Edm.Int32 "Start Date"
PX.Objects.PR.PRPTOBank.StartDateDay : Edm.Int32 "Start Date"
PX.Objects.PR.PRPTOBank.TransferDateType : Edm.String "Transfer Date Type"
PX.Objects.PR.PRPTOBank.PTOYearStartDate : Edm.DateTimeOffset
PX.Objects.PR.PRPTOBank.CarryoverType : Edm.String "Carryover Type"
PX.Objects.PR.PRPTOBank.SettlementBalanceType : Edm.String "On Settlement"
PX.Objects.PR.PRPTOBank.BandingRuleRoundingMethod : Edm.String "Rounding Method for Years of Service"
PX.Objects.PR.PRPTOBank.ApplicableEarningIncludeType : Edm.String "Accrue Time Off Based On"
PX.Objects.PR.PRPTOBank.IsPercentageBased : Edm.Boolean
PX.Objects.PR.PRPTOBank.AllowNegativeBalance : Edm.Boolean [required] "Allow Negative Balance"
PX.Objects.PR.PRPTOBank.DisburseFromCarryover : Edm.Boolean [required] "Can Only Disburse from Carryover"
PX.Objects.PR.PRPTOBank.TStamp : Edm.Binary
PX.Objects.PR.PRPTOBank.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPTOBank.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPTOBank.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPTOBank.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPTOBank.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPTOBank.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPTOBank.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPTOBank.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPTOBank.AccountByPtoExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPTOBank.AccountByPtoLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPTOBank.AccountByPtoAssetAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRPTOBank.SubByPtoExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPTOBank.SubByPtoLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPTOBank.SubByPtoAssetSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPTOBank.EPEarningTypeByEarningTypeCD -> PX.Objects.EP.EPEarningType (EarningTypeCD=TypeCD)
PX.Objects.PR.PRPTOBank.PRBandingRulePTOBankCollection -> Collection(PX.Objects.PR.PRBandingRulePTOBank)
PX.Objects.PR.PRPTOBank.PREmployeeClassPTOBankCollection -> Collection(PX.Objects.PR.PREmployeeClassPTOBank)
PX.Objects.PR.PRPTOBank.PREmployeePTOBankCollection -> Collection(PX.Objects.PR.PREmployeePTOBank)
PX.Objects.PR.PRPTOBank.PRPaymentPTOBankCollection -> Collection(PX.Objects.PR.PRPaymentPTOBank)
PX.Objects.PR.PRPTOBank.PRPTOAdjustmentDetailCollection -> Collection(PX.Objects.PR.PRPTOAdjustmentDetail)
PX.Objects.PR.PRPTOBank.PRPTOBankApplicableEarningTypeCollection -> Collection(PX.Objects.PR.PRPTOBankApplicableEarningType)
PX.Objects.PR.PRPTOBank.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)

# PX.Objects.PR.PRPTOBankApplicableEarningType (EntityType)

Label: "PTO Bank Applicable Earning Type"
Key: BankID, EarningTypeCD
Entity sets: PX_Objects_PR_PRPTOBankApplicableEarningType, PTOBankApplicableEarningType, PRPTOBankApplicableEarningType

PX.Objects.PR.PRPTOBankApplicableEarningType.BankID : Edm.String [key] "PTO Bank"
PX.Objects.PR.PRPTOBankApplicableEarningType.EarningTypeCD : Edm.String [key] "Earning Type"
PX.Objects.PR.PRPTOBankApplicableEarningType.TStamp : Edm.Binary
PX.Objects.PR.PRPTOBankApplicableEarningType.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPTOBankApplicableEarningType.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPTOBankApplicableEarningType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPTOBankApplicableEarningType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPTOBankApplicableEarningType.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPTOBankApplicableEarningType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPTOBankApplicableEarningType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPTOBankApplicableEarningType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPTOBankApplicableEarningType.EPEarningTypeByEarningTypeCD -> PX.Objects.EP.EPEarningType (EarningTypeCD=TypeCD)
PX.Objects.PR.PRPTOBankApplicableEarningType.PRPTOBankByBankID -> PX.Objects.PR.PRPTOBank (BankID=BankID)

# PX.Objects.PR.PRPTODetail (EntityType)

Label: "PTO Detail"
Key: RecordID
Entity sets: PX_Objects_PR_PRPTODetail, PTODetail, PRPTODetail

PX.Objects.PR.PRPTODetail.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRPTODetail.EmployeeID : Edm.Int32 "Employee"
PX.Objects.PR.PRPTODetail.PaymentDocType : Edm.String
PX.Objects.PR.PRPTODetail.PaymentRefNbr : Edm.String
PX.Objects.PR.PRPTODetail.BankID : Edm.String "PTO Bank"
PX.Objects.PR.PRPTODetail.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRPTODetail.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRPTODetail.EarningTypeCD : Edm.String "Earning Type Code"
PX.Objects.PR.PRPTODetail.Released : Edm.Boolean [required]
PX.Objects.PR.PRPTODetail.CreditAmountFromAssetAccount : Edm.Decimal
PX.Objects.PR.PRPTODetail.TStamp : Edm.Binary
PX.Objects.PR.PRPTODetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRPTODetail.CreatedByScreenID : Edm.String
PX.Objects.PR.PRPTODetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPTODetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRPTODetail.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRPTODetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRPTODetail.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PRPTODetail.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRPTODetail.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRPTODetail.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRPTODetail.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.PR.PRPTODetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRPTODetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRPTODetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRPTODetail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PR.PRPTODetail.AccountByExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PRPTODetail.AccountByLiabilityAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PRPTODetail.AccountByAssetAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PRPTODetail.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPTODetail.SubByLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPTODetail.SubByAssetSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRPTODetail.EPEarningTypeByEarningTypeCD -> PX.Objects.EP.EPEarningType (EarningTypeCD=TypeCD)
PX.Objects.PR.PRPTODetail.PRPaymentByPaymentRefNbr -> PX.Objects.PR.PRPayment (PaymentDocType=DocType, PaymentRefNbr=RefNbr)
PX.Objects.PR.PRPTODetail.PRPTOBankByBankID -> PX.Objects.PR.PRPTOBank (BankID=BankID)

# PX.Objects.PR.PRRecordOfEmployment (EntityType)

Label: "Record Of Employment"
Key: RefNbr
Entity sets: PX_Objects_PR_PRRecordOfEmployment, RecordOfEmployment, PRRecordOfEmployment
Non-filterable, non-selectable: NoteText

PX.Objects.PR.PRRecordOfEmployment.RefNbr : Edm.String [key] "Reference Nbr. (Block 1)"
PX.Objects.PR.PRRecordOfEmployment.Status : Edm.String "Status"
PX.Objects.PR.PRRecordOfEmployment.EmployeeID : Edm.Int32 "Employee"
PX.Objects.PR.PRRecordOfEmployment.Amendment : Edm.Boolean [required] "Amendment"
PX.Objects.PR.PRRecordOfEmployment.AmendedRefNbr : Edm.String "Amended ROE Ref. Nbr. (Block 2)"
PX.Objects.PR.PRRecordOfEmployment.ReasonForROE : Edm.String "Reason for ROE (Block 16)"
PX.Objects.PR.PRRecordOfEmployment.PeriodType : Edm.String "Period Type (Block 6)"
PX.Objects.PR.PRRecordOfEmployment.OrigDocType : Edm.String "Original Doc. Type"
PX.Objects.PR.PRRecordOfEmployment.OrigRefNbr : Edm.String "Original Document"
PX.Objects.PR.PRRecordOfEmployment.Comments : Edm.String "Comments (Block 18)"
PX.Objects.PR.PRRecordOfEmployment.DocDesc : Edm.String "Description"
PX.Objects.PR.PRRecordOfEmployment.AddressID : Edm.Int32 "Address ID"
PX.Objects.PR.PRRecordOfEmployment.CRAPayrollAccountNumber : Edm.String "CRA Payroll Account Number (Block 5)"
PX.Objects.PR.PRRecordOfEmployment.FirstDayWorked : Edm.DateTimeOffset "First Day Worked (Block 10)"
PX.Objects.PR.PRRecordOfEmployment.LastDayForWhichPaid : Edm.DateTimeOffset "Last Day for Which Paid (Block 11)"
PX.Objects.PR.PRRecordOfEmployment.FinalPayPeriodEndingDate : Edm.DateTimeOffset "Final Pay Period Ending Date (Block 12)"
PX.Objects.PR.PRRecordOfEmployment.VacationPay : Edm.Decimal [required] "Vacation Pay (Block 17A)"
PX.Objects.PR.PRRecordOfEmployment.TotalInsurableHours : Edm.Decimal [required] "Total Insurable Hours (Block 15A)"
PX.Objects.PR.PRRecordOfEmployment.TotalInsurableEarnings : Edm.Decimal [required] "Total Insurable Earnings (Block 15B)"
PX.Objects.PR.PRRecordOfEmployment.NoteID : Edm.Guid
PX.Objects.PR.PRRecordOfEmployment.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRRecordOfEmployment.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRRecordOfEmployment.CreatedByScreenID : Edm.String
PX.Objects.PR.PRRecordOfEmployment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRRecordOfEmployment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRRecordOfEmployment.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRRecordOfEmployment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRRecordOfEmployment.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRRecordOfEmployment.AddressByAddressID -> PX.Objects.CR.Address (AddressID=AddressID)
PX.Objects.PR.PRRecordOfEmployment.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRRecordOfEmployment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRRecordOfEmployment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRRecordOfEmployment.PRPaymentByOrigRefNbr -> PX.Objects.PR.PRPayment (OrigDocType=DocType, OrigRefNbr=RefNbr)
PX.Objects.PR.PRRecordOfEmployment.PRROEInsurableEarningsByPayPeriodCollection -> Collection(PX.Objects.PR.PRROEInsurableEarningsByPayPeriod)
PX.Objects.PR.PRRecordOfEmployment.PRROEOtherMoniesCollection -> Collection(PX.Objects.PR.PRROEOtherMonies)
PX.Objects.PR.PRRecordOfEmployment.PRROEStatutoryHolidayPayCollection -> Collection(PX.Objects.PR.PRROEStatutoryHolidayPay)

# PX.Objects.PR.PRRegularTypeForOvertime (EntityType)

Label: "Regular Type for Overtime"
Key: OvertimeTypeCD, RegularTypeCD
Entity sets: PX_Objects_PR_PRRegularTypeForOvertime, RegularTypeforOvertime, PRRegularTypeForOvertime

PX.Objects.PR.PRRegularTypeForOvertime.OvertimeTypeCD : Edm.String [key]
PX.Objects.PR.PRRegularTypeForOvertime.RegularTypeCD : Edm.String [key] "Code"
PX.Objects.PR.PRRegularTypeForOvertime.TStamp : Edm.Binary
PX.Objects.PR.PRRegularTypeForOvertime.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRRegularTypeForOvertime.CreatedByScreenID : Edm.String
PX.Objects.PR.PRRegularTypeForOvertime.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRRegularTypeForOvertime.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRRegularTypeForOvertime.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRRegularTypeForOvertime.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRRegularTypeForOvertime.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRRegularTypeForOvertime.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRRegularTypeForOvertime.EPEarningTypeByOvertimeTypeCD -> PX.Objects.EP.EPEarningType (OvertimeTypeCD=TypeCD)
PX.Objects.PR.PRRegularTypeForOvertime.EPEarningTypeByRegularTypeCD -> PX.Objects.EP.EPEarningType (RegularTypeCD=TypeCD)

# PX.Objects.PR.PRROEInsurableEarningsByPayPeriod (EntityType)

Label: "Insurable Earnings by Pay Period"
Key: PayPeriodID, RefNbr
Entity sets: PX_Objects_PR_PRROEInsurableEarningsByPayPeriod, InsurableEarningsbyPayPeriod, PRROEInsurableEarningsByPayPeriod

PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.PayPeriodID : Edm.String [key] "Pay Period ID"
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.InsurableHours : Edm.Decimal [required] "Insurable Hours"
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.InsurableEarnings : Edm.Decimal [required] "Insurable Earnings"
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.TStamp : Edm.Binary
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.CreatedByScreenID : Edm.String
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRROEInsurableEarningsByPayPeriod.PRRecordOfEmploymentByRefNbr -> PX.Objects.PR.PRRecordOfEmployment (RefNbr=RefNbr)

# PX.Objects.PR.PRROEOtherMonies (EntityType)

Label: "Other Monies"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PR_PRROEOtherMonies, OtherMonies, PRROEOtherMonies

PX.Objects.PR.PRROEOtherMonies.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PR.PRROEOtherMonies.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PR.PRROEOtherMonies.TypeCD : Edm.String "Earning Code"
PX.Objects.PR.PRROEOtherMonies.OtherMoniesCD : Edm.String "Other Monies (Code)"
PX.Objects.PR.PRROEOtherMonies.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRROEOtherMonies.TStamp : Edm.Binary
PX.Objects.PR.PRROEOtherMonies.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRROEOtherMonies.CreatedByScreenID : Edm.String
PX.Objects.PR.PRROEOtherMonies.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRROEOtherMonies.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRROEOtherMonies.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRROEOtherMonies.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRROEOtherMonies.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRROEOtherMonies.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRROEOtherMonies.EPEarningTypeByTypeCD -> PX.Objects.EP.EPEarningType (TypeCD=TypeCD)
PX.Objects.PR.PRROEOtherMonies.PRRecordOfEmploymentByRefNbr -> PX.Objects.PR.PRRecordOfEmployment (RefNbr=RefNbr)

# PX.Objects.PR.PRROEStatutoryHolidayPay (EntityType)

Label: "Statutory Holiday Pay"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_PR_PRROEStatutoryHolidayPay, StatutoryHolidayPay, PRROEStatutoryHolidayPay

PX.Objects.PR.PRROEStatutoryHolidayPay.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.PR.PRROEStatutoryHolidayPay.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.PR.PRROEStatutoryHolidayPay.Date : Edm.DateTimeOffset "Date"
PX.Objects.PR.PRROEStatutoryHolidayPay.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRROEStatutoryHolidayPay.TStamp : Edm.Binary
PX.Objects.PR.PRROEStatutoryHolidayPay.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRROEStatutoryHolidayPay.CreatedByScreenID : Edm.String
PX.Objects.PR.PRROEStatutoryHolidayPay.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRROEStatutoryHolidayPay.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRROEStatutoryHolidayPay.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRROEStatutoryHolidayPay.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRROEStatutoryHolidayPay.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRROEStatutoryHolidayPay.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRROEStatutoryHolidayPay.PRRecordOfEmploymentByRefNbr -> PX.Objects.PR.PRRecordOfEmployment (RefNbr=RefNbr)

# PX.Objects.PR.PRSetup (EntityType)

Label: "Payroll Preferences"
Singletons: PX_Objects_PR_PRSetup, PayrollPreferences, PRSetup

PX.Objects.PR.PRSetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.PR.PRSetup.BatchNumberingCD : Edm.String "Payroll Batch Numbering Sequence"
PX.Objects.PR.PRSetup.TranNumberingCD : Edm.String "Transaction Numbering Sequence"
PX.Objects.PR.PRSetup.PTOAdjustmentNumberingCD : Edm.String "PTO Adjustment Numbering Sequence"
PX.Objects.PR.PRSetup.UpdateGL : Edm.Boolean [required] "Update GL"
PX.Objects.PR.PRSetup.SummPost : Edm.Boolean [required] "Post Summary on Updating GL"
PX.Objects.PR.PRSetup.AutoPost : Edm.Boolean [required] "Automatically Post on Release"
PX.Objects.PR.PRSetup.DisableGLWarnings : Edm.Boolean [required] "Disable GL Account Warnings on Payment Release"
PX.Objects.PR.PRSetup.PayPeriodDateChangeAllowed : Edm.Boolean [required] "Allow Changing Pay Period Dates"
PX.Objects.PR.PRSetup.PayRateDecimalPlaces : Edm.Int16 "Pay Rate Decimal Places"
PX.Objects.PR.PRSetup.DedBenDecimalPlaces : Edm.Int16 [required] "Deduction and Benefit Decimal Places"
PX.Objects.PR.PRSetup.EarningsAcctDefault : Edm.String "Use Earnings Account from"
PX.Objects.PR.PRSetup.EarningsAlternateAcctDefault : Edm.String "Fallback Source for Earnings Account"
PX.Objects.PR.PRSetup.DeductLiabilityAcctDefault : Edm.String "Use Deduction Liability Account from"
PX.Objects.PR.PRSetup.BenefitExpenseAcctDefault : Edm.String "Use Benefit Expense Account from"
PX.Objects.PR.PRSetup.BenefitExpenseAlternateAcctDefault : Edm.String "Fallback Source for Benefit Expense Account"
PX.Objects.PR.PRSetup.BenefitLiabilityAcctDefault : Edm.String "Use Benefit Liability Account from"
PX.Objects.PR.PRSetup.TaxExpenseAcctDefault : Edm.String "Use Tax Expense Account from"
PX.Objects.PR.PRSetup.TaxExpenseAlternateAcctDefault : Edm.String "Fallback Source for Tax Expense Account"
PX.Objects.PR.PRSetup.TaxLiabilityAcctDefault : Edm.String "Use Tax Liability Account from"
PX.Objects.PR.PRSetup.SummarizeTimeCard : Edm.Boolean [required] "Summarize Time Card Data"
PX.Objects.PR.PRSetup.RegularHoursType : Edm.String "Regular Hours Earning Type for Quick Pay"
PX.Objects.PR.PRSetup.HolidaysType : Edm.String "Holiday Earning Type for Quick Pay"
PX.Objects.PR.PRSetup.CommissionType : Edm.String "Commission Earning Type"
PX.Objects.PR.PRSetup.EnablePieceworkEarningType : Edm.Boolean [required] "Enable Piecework as an Earning Type"
PX.Objects.PR.PRSetup.HoldEntry : Edm.Boolean [required] "Hold Paycheck on Entry"
PX.Objects.PR.PRSetup.NoWeekendTransactionDate : Edm.Boolean [required] "Transaction Date Cannot Be on Weekend"
PX.Objects.PR.PRSetup.HideEmployeeInfo : Edm.Boolean [required] "Hide Employee Name on Transactions"
PX.Objects.PR.PRSetup.ProjectCostAssignment : Edm.String "Project Cost Assignment"
PX.Objects.PR.PRSetup.AutoReleaseOnPay : Edm.Boolean [required] "Automatically Release on Payment"
PX.Objects.PR.PRSetup.TimePostingOption : Edm.String "Time Posting Option"
PX.Objects.PR.PRSetup.OffBalanceAccountGroupID : Edm.Int32 "Off-Balance Account Group"
PX.Objects.PR.PRSetup.tstamp : Edm.Binary
PX.Objects.PR.PRSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRSetup.CreatedByScreenID : Edm.String
PX.Objects.PR.PRSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRSetup.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRSetup.PMAccountGroupByOffBalanceAccountGroupID -> PX.Objects.PM.PMAccountGroup (OffBalanceAccountGroupID=GroupID)
PX.Objects.PR.PRSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRSetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.PR.PRSetup.NumberingByBatchNumberingCD -> PX.Objects.CS.Numbering (BatchNumberingCD=NumberingID)
PX.Objects.PR.PRSetup.NumberingByTranNumberingCD -> PX.Objects.CS.Numbering (TranNumberingCD=NumberingID)
PX.Objects.PR.PRSetup.NumberingByRoeNumberingCD -> PX.Objects.CS.Numbering
PX.Objects.PR.PRSetup.NumberingByBatchForSubmissionNumberingCD -> PX.Objects.CS.Numbering
PX.Objects.PR.PRSetup.NumberingByPtoAdjustmentNumberingCD -> PX.Objects.CS.Numbering
PX.Objects.PR.PRSetup.EPEarningTypeByRegularHoursType -> PX.Objects.EP.EPEarningType (RegularHoursType=TypeCD)
PX.Objects.PR.PRSetup.EPEarningTypeByHolidaysType -> PX.Objects.EP.EPEarningType (HolidaysType=TypeCD)
PX.Objects.PR.PRSetup.EPEarningTypeByCommissionType -> PX.Objects.EP.EPEarningType (CommissionType=TypeCD)

# PX.Objects.PR.PRTaxCode (EntityType)

Label: "Tax Code"
Key: TaxCD
Entity sets: PX_Objects_PR_PRTaxCode, TaxCode, PRTaxCode
Non-filterable, non-selectable: NoteText, ErrorLevel

PX.Objects.PR.PRTaxCode.TaxID : Edm.Int32
PX.Objects.PR.PRTaxCode.TaxCD : Edm.String [key] "Code"
PX.Objects.PR.PRTaxCode.Description : Edm.String "Name"
PX.Objects.PR.PRTaxCode.TaxCategory : Edm.String "Tax Category"
PX.Objects.PR.PRTaxCode.TypeName : Edm.String "Type"
PX.Objects.PR.PRTaxCode.JurisdictionLevel : Edm.String "Jurisdiction Level"
PX.Objects.PR.PRTaxCode.TaxTypeDescription : Edm.String "Type"
PX.Objects.PR.PRTaxCode.GovtRefNbr : Edm.String "Employer Govt. Tax ID"
PX.Objects.PR.PRTaxCode.BAccountID : Edm.Int32 "Vendor"
PX.Objects.PR.PRTaxCode.TaxUniqueCode : Edm.String "Tax Unique ID"
PX.Objects.PR.PRTaxCode.TaxInvDescrType : Edm.String "Invoice Description Source"
PX.Objects.PR.PRTaxCode.VndInvDescr : Edm.String "Vendor Invoice Description"
PX.Objects.PR.PRTaxCode.TaxState : Edm.String "Tax State"
PX.Objects.PR.PRTaxCode.CountryID : Edm.String "CountryID"
PX.Objects.PR.PRTaxCode.NoteID : Edm.Guid
PX.Objects.PR.PRTaxCode.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRTaxCode.ErrorLevel : Edm.Int32
PX.Objects.PR.PRTaxCode.IsDeleted : Edm.Boolean [required]
PX.Objects.PR.PRTaxCode.TStamp : Edm.Binary
PX.Objects.PR.PRTaxCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxCode.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxCode.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxCode.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxCode.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxCode.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.PRTaxCode.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.PR.PRTaxCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRTaxCode.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.PRTaxCode.StateByTaxState -> PX.Objects.CS.State (CountryID=CountryID, TaxState=StateID)
PX.Objects.PR.PRTaxCode.StateByCountryID -> PX.Objects.CS.State (TaxState=StateID, CountryID=CountryID)
PX.Objects.PR.PRTaxCode.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRTaxCode.AccountByLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.PRTaxCode.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRTaxCode.SubByLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRTaxCode.PRDeductCodeDetailCollection -> Collection(PX.Objects.PR.PRDeductCodeDetail)
PX.Objects.PR.PRTaxCode.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PR.PRTaxCode.PREarningTypeDetailCollection -> Collection(PX.Objects.PR.PREarningTypeDetail)
PX.Objects.PR.PRTaxCode.PRPaymentTaxCollection -> Collection(PX.Objects.PR.PRPaymentTax)
PX.Objects.PR.PRTaxCode.PRDeductCodeTaxDecreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxDecreasingWage)
PX.Objects.PR.PRTaxCode.PRDeductCodeTaxIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxIncreasingWage)
PX.Objects.PR.PRTaxCode.PREmployeeTaxCollection -> Collection(PX.Objects.PR.PREmployeeTax)
PX.Objects.PR.PRTaxCode.PREmployeeTaxAttributeCollection -> Collection(PX.Objects.PR.PREmployeeTaxAttribute)
PX.Objects.PR.PRTaxCode.PREntityTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PREntityTaxCodeAttribute)
PX.Objects.PR.PRTaxCode.PRPaymentTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPaymentTaxApplicableAmounts)
PX.Objects.PR.PRTaxCode.PRPaymentTaxSplitCollection -> Collection(PX.Objects.PR.PRPaymentTaxSplit)
PX.Objects.PR.PRTaxCode.PRTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PRTaxCodeAttribute)
PX.Objects.PR.PRTaxCode.PRPeriodTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPeriodTaxApplicableAmounts)
PX.Objects.PR.PRTaxCode.PRPeriodTaxesCollection -> Collection(PX.Objects.PR.PRPeriodTaxes)
PX.Objects.PR.PRTaxCode.PRYtdTaxesCollection -> Collection(PX.Objects.PR.PRYtdTaxes)

# PX.Objects.PR.PRTaxCodeAttribute (EntityType)

Label: "Tax Code Setting"
Key: SettingName, TaxID
Entity sets: PX_Objects_PR_PRTaxCodeAttribute, TaxCodeSetting, PRTaxCodeAttribute
Non-filterable, non-selectable: Description, IsEncryptionRequired, IsEncrypted, AllowOverride, UseDefault, State, NoteText, ErrorLevel, SettingLevelEnabled, IsEmployeeSpecific

PX.Objects.PR.PRTaxCodeAttribute.TaxID : Edm.Int32 [key]
PX.Objects.PR.PRTaxCodeAttribute.TypeName : Edm.String "Type"
PX.Objects.PR.PRTaxCodeAttribute.SettingName : Edm.String [key] "Setting"
PX.Objects.PR.PRTaxCodeAttribute.Description : Edm.String "Description"
PX.Objects.PR.PRTaxCodeAttribute.IsEncryptionRequired : Edm.Boolean
PX.Objects.PR.PRTaxCodeAttribute.CanadaReportMapping : Edm.Int32 "CanadaReportMapping"
PX.Objects.PR.PRTaxCodeAttribute.IsEncrypted : Edm.Boolean
PX.Objects.PR.PRTaxCodeAttribute.Value : Edm.String "Default Value"
PX.Objects.PR.PRTaxCodeAttribute.AllowOverride : Edm.Boolean
PX.Objects.PR.PRTaxCodeAttribute.SettingLevel : Edm.String "Setting Level"
PX.Objects.PR.PRTaxCodeAttribute.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.PR.PRTaxCodeAttribute.Required : Edm.Boolean [required] "Required"
PX.Objects.PR.PRTaxCodeAttribute.UseDefault : Edm.Boolean
PX.Objects.PR.PRTaxCodeAttribute.AatrixMapping : Edm.Int32 "AatrixMapping"
PX.Objects.PR.PRTaxCodeAttribute.AdditionalInformation : Edm.String "Additional Information"
PX.Objects.PR.PRTaxCodeAttribute.FormBox : Edm.String "Form/Box"
PX.Objects.PR.PRTaxCodeAttribute.State : Edm.String
PX.Objects.PR.PRTaxCodeAttribute.NoteID : Edm.Guid
PX.Objects.PR.PRTaxCodeAttribute.NoteText : Edm.String "Note Text"
PX.Objects.PR.PRTaxCodeAttribute.ErrorLevel : Edm.Int32
PX.Objects.PR.PRTaxCodeAttribute.SettingLevelEnabled : Edm.Boolean "Setting Level Enabled"
PX.Objects.PR.PRTaxCodeAttribute.IsEmployeeSpecific : Edm.Boolean
PX.Objects.PR.PRTaxCodeAttribute.FEINDisplaySetting : Edm.Int32 [required]
PX.Objects.PR.PRTaxCodeAttribute.IsTaxAgency : Edm.Boolean [required]
PX.Objects.PR.PRTaxCodeAttribute.TStamp : Edm.Binary
PX.Objects.PR.PRTaxCodeAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxCodeAttribute.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxCodeAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxCodeAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxCodeAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxCodeAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxCodeAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxCodeAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRTaxCodeAttribute.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PRTaxCodeAttribute.PREmployeeTaxAttributeCollection -> Collection(PX.Objects.PR.PREmployeeTaxAttribute)
PX.Objects.PR.PRTaxCodeAttribute.PREntityTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PREntityTaxCodeAttribute)

# PX.Objects.PR.PRTaxDetail (EntityType)

Label: "Tax Detail"
Key: RecordID
Entity sets: PX_Objects_PR_PRTaxDetail, TaxDetail, PRTaxDetail
Non-filterable, non-selectable: AmountErrorMessage

PX.Objects.PR.PRTaxDetail.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRTaxDetail.OriginalRecordID : Edm.Int32
PX.Objects.PR.PRTaxDetail.EmployeeID : Edm.Int32 "Employee"
PX.Objects.PR.PRTaxDetail.BatchNbr : Edm.String "Batch Number"
PX.Objects.PR.PRTaxDetail.PaymentDocType : Edm.String "Payment Doc. Type"
PX.Objects.PR.PRTaxDetail.PaymentRefNbr : Edm.String "Payment Ref. Number"
PX.Objects.PR.PRTaxDetail.TaxID : Edm.Int32 "Tax"
PX.Objects.PR.PRTaxDetail.TaxCategory : Edm.String "Tax Category"
PX.Objects.PR.PRTaxDetail.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRTaxDetail.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.PR.PRTaxDetail.EarningTypeCD : Edm.String "Earning Type Code"
PX.Objects.PR.PRTaxDetail.Released : Edm.Boolean [required] "Released"
PX.Objects.PR.PRTaxDetail.APInvoiceDocType : Edm.String "Type"
PX.Objects.PR.PRTaxDetail.APInvoiceRefNbr : Edm.String "Reference Nbr."
PX.Objects.PR.PRTaxDetail.LiabilityPaid : Edm.Boolean [required] "Liability Paid"
PX.Objects.PR.PRTaxDetail.AmountErrorMessage : Edm.String
PX.Objects.PR.PRTaxDetail.PaymentCountryID : Edm.String
PX.Objects.PR.PRTaxDetail.TStamp : Edm.Binary
PX.Objects.PR.PRTaxDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxDetail.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxDetail.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.PR.PRTaxDetail.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRTaxDetail.APInvoiceByApInvoiceRefNbr -> PX.Objects.AP.APInvoice
PX.Objects.PR.PRTaxDetail.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRTaxDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.PR.PRTaxDetail.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.PR.PRTaxDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRTaxDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRTaxDetail.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PRTaxDetail.PRTaxCodeByPaymentCountryID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID, PaymentCountryID=CountryID)
PX.Objects.PR.PRTaxDetail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.PR.PRTaxDetail.AccountByExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PRTaxDetail.AccountByLiabilityAccountID -> PX.Objects.GL.Account
PX.Objects.PR.PRTaxDetail.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRTaxDetail.SubByLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.PRTaxDetail.EPEarningTypeByEarningTypeCD -> PX.Objects.EP.EPEarningType (EarningTypeCD=TypeCD)
PX.Objects.PR.PRTaxDetail.PRBatchByBatchNbr -> PX.Objects.PR.PRBatch (BatchNbr=BatchNbr)
PX.Objects.PR.PRTaxDetail.PRPaymentByPaymentRefNbr -> PX.Objects.PR.PRPayment (PaymentDocType=DocType, PaymentRefNbr=RefNbr)
PX.Objects.PR.PRTaxDetail.PRPaymentTaxByTaxID -> PX.Objects.PR.PRPaymentTax (PaymentDocType=DocType, PaymentRefNbr=RefNbr, TaxID=TaxID)

# PX.Objects.PR.PRTaxFormBatch (EntityType)

Label: "Tax Form Batch"
Key: BatchID
Entity sets: PX_Objects_PR_PRTaxFormBatch, TaxFormBatch, PRTaxFormBatch
Non-filterable, non-selectable: OrgBAccountIDDynamicLabel, DeletedDatabaseRecord

PX.Objects.PR.PRTaxFormBatch.BatchID : Edm.String [key] "Batch ID"
PX.Objects.PR.PRTaxFormBatch.Status : Edm.String "Status"
PX.Objects.PR.PRTaxFormBatch.FormType : Edm.String "Form Name"
PX.Objects.PR.PRTaxFormBatch.DocType : Edm.String "Document Type"
PX.Objects.PR.PRTaxFormBatch.Year : Edm.String "Year"
PX.Objects.PR.PRTaxFormBatch.OrgBAccountIDDynamicLabel : Edm.String "OrgBAccountIDDynamicLabel"
PX.Objects.PR.PRTaxFormBatch.DownloadedAt : Edm.DateTimeOffset "Downloaded On"
PX.Objects.PR.PRTaxFormBatch.EverPublished : Edm.Boolean [required] "EverPublished"
PX.Objects.PR.PRTaxFormBatch.NumberOfEmployees : Edm.Int32 "Number of Employees"
PX.Objects.PR.PRTaxFormBatch.NumberOfPublishedEmployees : Edm.Int32 "NumberOfPublishedEmployees"
PX.Objects.PR.PRTaxFormBatch.ProvinceOfEmployment : Edm.String "Province of Employment"
PX.Objects.PR.PRTaxFormBatch.CRAPayrollAccountID : Edm.String "CRA Payroll Account Number"
PX.Objects.PR.PRTaxFormBatch.TStamp : Edm.Binary
PX.Objects.PR.PRTaxFormBatch.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxFormBatch.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxFormBatch.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxFormBatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxFormBatch.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxFormBatch.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxFormBatch.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.PR.PRTaxFormBatch.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.PR.PRTaxFormBatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxFormBatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRTaxFormBatch.PREmployeeTaxFormCollection -> Collection(PX.Objects.PR.PREmployeeTaxForm)
PX.Objects.PR.PRTaxFormBatch.PREmployeeTaxFormDataCollection -> Collection(PX.Objects.PR.PREmployeeTaxFormData)

# PX.Objects.PR.PRTaxRegistration (EntityType)

Label: "Tax Registration"
Key: TaxRegistrationID
Entity sets: PX_Objects_PR_PRTaxRegistration, TaxRegistration1, PRTaxRegistration
Non-filterable, non-selectable: Entities

PX.Objects.PR.PRTaxRegistration.TaxRegistrationID : Edm.String [key] "EIN"
PX.Objects.PR.PRTaxRegistration.Entities : Edm.String "Company/Branch"
PX.Objects.PR.PRTaxRegistration.TStamp : Edm.Binary
PX.Objects.PR.PRTaxRegistration.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxRegistration.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxRegistration.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxRegistration.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxRegistration.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxRegistration.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxRegistration.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxRegistration.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PRTaxRegistrationAttribute (EntityType)

Label: "Tax Registration Attribute"
Key: SettingName, TaxID, TaxRegistrationID
Entity sets: PX_Objects_PR_PRTaxRegistrationAttribute, TaxRegistrationAttribute, PRTaxRegistrationAttribute

PX.Objects.PR.PRTaxRegistrationAttribute.TaxID : Edm.Int32 [key]
PX.Objects.PR.PRTaxRegistrationAttribute.SettingName : Edm.String [key] "Setting"
PX.Objects.PR.PRTaxRegistrationAttribute.TaxRegistrationID : Edm.String [key] "EIN"
PX.Objects.PR.PRTaxRegistrationAttribute.Value : Edm.String "Value"
PX.Objects.PR.PRTaxRegistrationAttribute.VendorID : Edm.Int32 "Vendor"
PX.Objects.PR.PRTaxRegistrationAttribute.TStamp : Edm.Binary
PX.Objects.PR.PRTaxRegistrationAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxRegistrationAttribute.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxRegistrationAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxRegistrationAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxRegistrationAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxRegistrationAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxRegistrationAttribute.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.PR.PRTaxRegistrationAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxRegistrationAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PRTaxReportingAccount (EntityType)

Label: "Tax Reporting Account"
Key: BAccountID
Entity sets: PX_Objects_PR_PRTaxReportingAccount, TaxReportingAccount, PRTaxReportingAccount

PX.Objects.PR.PRTaxReportingAccount.BAccountID : Edm.Int32 [key] "Account ID"
PX.Objects.PR.PRTaxReportingAccount.T4ContactID : Edm.Int32 "T4 Reporting Contact"
PX.Objects.PR.PRTaxReportingAccount.RL1IdentificationNumber : Edm.String "Identification Number"
PX.Objects.PR.PRTaxReportingAccount.RL1FileNumber : Edm.String "File Number"
PX.Objects.PR.PRTaxReportingAccount.RL1QuebecEnterpriseNumber : Edm.String "Quebec Enterprise Number"
PX.Objects.PR.PRTaxReportingAccount.RL1QuebecTransmitterNumber : Edm.String "Quebec Transmitter Number"
PX.Objects.PR.PRTaxReportingAccount.TransmitterRepID : Edm.String "Transmitter Rep. ID"
PX.Objects.PR.PRTaxReportingAccount.TStamp : Edm.Binary
PX.Objects.PR.PRTaxReportingAccount.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxReportingAccount.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxReportingAccount.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxReportingAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxReportingAccount.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxReportingAccount.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxReportingAccount.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.PR.PRTaxReportingAccount.ContactByT4ContactID -> PX.Objects.CR.Contact (T4ContactID=ContactID)
PX.Objects.PR.PRTaxReportingAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxReportingAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PRTaxSettingAdditionalInformation (EntityType)

Label: "Tax Setting Additional Information"
Key: CountryID, SettingName, State
Entity sets: PX_Objects_PR_PRTaxSettingAdditionalInformation, TaxSettingAdditionalInformation, PRTaxSettingAdditionalInformation

PX.Objects.PR.PRTaxSettingAdditionalInformation.TypeName : Edm.String
PX.Objects.PR.PRTaxSettingAdditionalInformation.SettingName : Edm.String [key]
PX.Objects.PR.PRTaxSettingAdditionalInformation.AdditionalInformation : Edm.String
PX.Objects.PR.PRTaxSettingAdditionalInformation.UsedForTaxCalculation : Edm.Boolean [required]
PX.Objects.PR.PRTaxSettingAdditionalInformation.FormBox : Edm.String
PX.Objects.PR.PRTaxSettingAdditionalInformation.State : Edm.String [key required]
PX.Objects.PR.PRTaxSettingAdditionalInformation.CountryID : Edm.String [key]
PX.Objects.PR.PRTaxSettingAdditionalInformation.TStamp : Edm.Binary
PX.Objects.PR.PRTaxSettingAdditionalInformation.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxSettingAdditionalInformation.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxSettingAdditionalInformation.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxSettingAdditionalInformation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxSettingAdditionalInformation.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxSettingAdditionalInformation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxSettingAdditionalInformation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxSettingAdditionalInformation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PRTaxWebServiceData (EntityType)

Label: "Tax Web Service Data"
Key: CountryID
Entity sets: PX_Objects_PR_PRTaxWebServiceData, TaxWebServiceData, PRTaxWebServiceData

PX.Objects.PR.PRTaxWebServiceData.CountryID : Edm.String [key]
PX.Objects.PR.PRTaxWebServiceData.TaxSettings : Edm.String
PX.Objects.PR.PRTaxWebServiceData.DeductionTypes : Edm.String
PX.Objects.PR.PRTaxWebServiceData.WageTypes : Edm.String
PX.Objects.PR.PRTaxWebServiceData.ReportingTypes : Edm.String
PX.Objects.PR.PRTaxWebServiceData.QuebecReportingTypes : Edm.String
PX.Objects.PR.PRTaxWebServiceData.States : Edm.String
PX.Objects.PR.PRTaxWebServiceData.TStamp : Edm.Binary
PX.Objects.PR.PRTaxWebServiceData.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTaxWebServiceData.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTaxWebServiceData.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxWebServiceData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTaxWebServiceData.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTaxWebServiceData.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTaxWebServiceData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTaxWebServiceData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.PR.PRTransactionDateException (EntityType)

Label: "Transaction Date Exception"
Key: RecordID
Entity sets: PX_Objects_PR_PRTransactionDateException, TransactionDateException, PRTransactionDateException
Non-filterable, non-selectable: DayOfWeek

PX.Objects.PR.PRTransactionDateException.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRTransactionDateException.Date : Edm.DateTimeOffset "Date"
PX.Objects.PR.PRTransactionDateException.Description : Edm.String "Description"
PX.Objects.PR.PRTransactionDateException.CountryID : Edm.String "CountryID"
PX.Objects.PR.PRTransactionDateException.DayOfWeek : Edm.String "Day of Week"
PX.Objects.PR.PRTransactionDateException.TStamp : Edm.Binary
PX.Objects.PR.PRTransactionDateException.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRTransactionDateException.CreatedByScreenID : Edm.String
PX.Objects.PR.PRTransactionDateException.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTransactionDateException.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRTransactionDateException.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRTransactionDateException.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRTransactionDateException.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRTransactionDateException.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRTransactionDateException.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)

# PX.Objects.PR.PRWorkCompensationBenefitRate (EntityType)

Label: "Work Compensation Benefit Rate"
Key: RecordID
Entity sets: PX_Objects_PR_PRWorkCompensationBenefitRate, WorkCompensationBenefitRate, PRWorkCompensationBenefitRate
Non-filterable, non-selectable: IsActive, ContribType, DeductionCalcType, WorkCodeCountryID, DeductCodeCountryID

PX.Objects.PR.PRWorkCompensationBenefitRate.RecordID : Edm.Int32 [key]
PX.Objects.PR.PRWorkCompensationBenefitRate.WorkCodeID : Edm.String "WCC Code"
PX.Objects.PR.PRWorkCompensationBenefitRate.DeductCodeID : Edm.Int32 "Deduction and Benefit Code"
PX.Objects.PR.PRWorkCompensationBenefitRate.DeductionRate : Edm.Decimal "Deduction Rate"
PX.Objects.PR.PRWorkCompensationBenefitRate.Rate : Edm.Decimal [required] "Benefit Rate"
PX.Objects.PR.PRWorkCompensationBenefitRate.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.PR.PRWorkCompensationBenefitRate.IsActive : Edm.Boolean "Active"
PX.Objects.PR.PRWorkCompensationBenefitRate.ContribType : Edm.String "Contribution Type"
PX.Objects.PR.PRWorkCompensationBenefitRate.DeductionCalcType : Edm.String "Deduction Calculation Method"
PX.Objects.PR.PRWorkCompensationBenefitRate.WorkCodeCountryID : Edm.String
PX.Objects.PR.PRWorkCompensationBenefitRate.DeductCodeCountryID : Edm.String
PX.Objects.PR.PRWorkCompensationBenefitRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRWorkCompensationBenefitRate.CreatedByScreenID : Edm.String
PX.Objects.PR.PRWorkCompensationBenefitRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRWorkCompensationBenefitRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRWorkCompensationBenefitRate.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRWorkCompensationBenefitRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRWorkCompensationBenefitRate.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.PR.PRWorkCompensationBenefitRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRWorkCompensationBenefitRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRWorkCompensationBenefitRate.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRWorkCompensationBenefitRate.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)

# PX.Objects.PR.PRWorkCompensationMaximumInsurableWage (EntityType)

Label: "Work Compensation Benefit Rate"
Key: DeductCodeID, EffectiveDate, WorkCodeID
Entity sets: PX_Objects_PR_PRWorkCompensationMaximumInsurableWage, WorkCompensationBenefitRate1, PRWorkCompensationMaximumInsurableWage
Non-filterable, non-selectable: WorkCodeCountryID

PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.WorkCodeID : Edm.String [key] "WC Code"
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.DeductCodeID : Edm.Int32 [key] "Deduction and Benefit Code"
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.MaximumInsurableWage : Edm.Decimal [required] "Wage Limit"
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.EffectiveDate : Edm.DateTimeOffset [key] "Effective Date"
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.WorkCodeCountryID : Edm.String
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.CreatedByScreenID : Edm.String
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.PRDeductCodeByDeductCodeID -> PX.Objects.PR.PRDeductCode (DeductCodeID=CodeID)
PX.Objects.PR.PRWorkCompensationMaximumInsurableWage.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)

# PX.Objects.PR.PRYtdDeductions (EntityType)

Label: "YTD Deductions"
Key: CodeID, EmployeeID, Year
Entity sets: PX_Objects_PR_PRYtdDeductions, YTDDeductions, PRYtdDeductions

PX.Objects.PR.PRYtdDeductions.Year : Edm.String [key] "Year"
PX.Objects.PR.PRYtdDeductions.EmployeeID : Edm.Int32 [key] "Employee"
PX.Objects.PR.PRYtdDeductions.CodeID : Edm.Int32 [key] "Code"
PX.Objects.PR.PRYtdDeductions.Amount : Edm.Decimal "Amount"
PX.Objects.PR.PRYtdDeductions.EmployerAmount : Edm.Decimal "Employer Amount"
PX.Objects.PR.PRYtdDeductions.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRYtdDeductions.CreatedByScreenID : Edm.String
PX.Objects.PR.PRYtdDeductions.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRYtdDeductions.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRYtdDeductions.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRYtdDeductions.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRYtdDeductions.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRYtdDeductions.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRYtdDeductions.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRYtdDeductions.PRDeductCodeByCodeID -> PX.Objects.PR.PRDeductCode (CodeID=CodeID)

# PX.Objects.PR.PRYtdEarnings (EntityType)

Label: "YTD Earnings"
Key: EmployeeID, LocationID, Month, TypeCD, Year
Entity sets: PX_Objects_PR_PRYtdEarnings, YTDEarnings, PRYtdEarnings

PX.Objects.PR.PRYtdEarnings.Month : Edm.Int32 [key] "Month"
PX.Objects.PR.PRYtdEarnings.Year : Edm.String [key] "Year"
PX.Objects.PR.PRYtdEarnings.EmployeeID : Edm.Int32 [key] "Employee"
PX.Objects.PR.PRYtdEarnings.TypeCD : Edm.String [key] "Code"
PX.Objects.PR.PRYtdEarnings.LocationID : Edm.Int32 [key] "Location"
PX.Objects.PR.PRYtdEarnings.Amount : Edm.Decimal "Amount"
PX.Objects.PR.PRYtdEarnings.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRYtdEarnings.CreatedByScreenID : Edm.String
PX.Objects.PR.PRYtdEarnings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRYtdEarnings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRYtdEarnings.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRYtdEarnings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRYtdEarnings.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRYtdEarnings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRYtdEarnings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRYtdEarnings.EPEarningTypeByTypeCD -> PX.Objects.EP.EPEarningType (TypeCD=TypeCD)
PX.Objects.PR.PRYtdEarnings.PRLocationByLocationID -> PX.Objects.PR.PRLocation (LocationID=LocationID)

# PX.Objects.PR.PRYtdTaxes (EntityType)

Label: "YTD Taxes"
Key: EmployeeID, TaxID, Year
Entity sets: PX_Objects_PR_PRYtdTaxes, YTDTaxes, PRYtdTaxes

PX.Objects.PR.PRYtdTaxes.Year : Edm.String [key] "Year"
PX.Objects.PR.PRYtdTaxes.EmployeeID : Edm.Int32 [key] "Employee"
PX.Objects.PR.PRYtdTaxes.TaxID : Edm.Int32 [key] "Tax Code"
PX.Objects.PR.PRYtdTaxes.Amount : Edm.Decimal [required] "Amount"
PX.Objects.PR.PRYtdTaxes.PickupAmount : Edm.Decimal [required]
PX.Objects.PR.PRYtdTaxes.TaxableWages : Edm.Decimal [required]
PX.Objects.PR.PRYtdTaxes.MostRecentWH : Edm.Decimal [required]
PX.Objects.PR.PRYtdTaxes.CreatedByID : Edm.Guid "Created By"
PX.Objects.PR.PRYtdTaxes.CreatedByScreenID : Edm.String
PX.Objects.PR.PRYtdTaxes.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRYtdTaxes.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.PR.PRYtdTaxes.LastModifiedByScreenID : Edm.String
PX.Objects.PR.PRYtdTaxes.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.PR.PRYtdTaxes.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.PR.PRYtdTaxes.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.PR.PRYtdTaxes.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.PR.PRYtdTaxes.PRTaxCodeByTaxID -> PX.Objects.PR.PRTaxCode (TaxID=TaxID)
PX.Objects.PR.PRYtdTaxes.PRPeriodTaxesCollection -> Collection(PX.Objects.PR.PRPeriodTaxes)

# PX.Objects.PR.Standalone.PRDeductCode (EntityType)

Label: "Payroll Deduction and Benefit Code"
Singletons: PX_Objects_PR_Standalone_PRDeductCode, PayrollDeductionandBenefitCode, PRDeductCode1

PX.Objects.PR.Standalone.PRDeductCode.CodeID : Edm.Int32 "Code ID"
PX.Objects.PR.Standalone.PRDeductCode.CountryID : Edm.String
PX.Objects.PR.Standalone.PRDeductCode.VendorByBAccountID -> PX.Objects.AP.Vendor
PX.Objects.PR.Standalone.PRDeductCode.BAccountByBAccountID -> PX.Objects.CR.BAccount
PX.Objects.PR.Standalone.PRDeductCode.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PR.Standalone.PRDeductCode.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PR.Standalone.PRDeductCode.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode
PX.Objects.PR.Standalone.PRDeductCode.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.Standalone.PRDeductCode.StateByState -> PX.Objects.CS.State (CountryID=CountryID)
PX.Objects.PR.Standalone.PRDeductCode.StateByCountryID -> PX.Objects.CS.State (CountryID=CountryID)
PX.Objects.PR.Standalone.PRDeductCode.AccountByDedLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PRDeductCode.AccountByBenefitExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PRDeductCode.AccountByBenefitLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PRDeductCode.SubByDedLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PRDeductCode.SubByBenefitExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PRDeductCode.SubByBenefitLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PRDeductCode.PRDeductCodeDetailCollection -> Collection(PX.Objects.PR.PRDeductCodeDetail)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.PR.Standalone.PRDeductCode.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.PR.Standalone.PRDeductCode.PRAcaDeductCoverageInfoCollection -> Collection(PX.Objects.PR.PRAcaDeductCoverageInfo)
PX.Objects.PR.Standalone.PRDeductCode.PRBatchDeductCollection -> Collection(PX.Objects.PR.PRBatchDeduct)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductCodeBenefitIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeBenefitIncreasingWage)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductCodeDeductionDecreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeDeductionDecreasingWage)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductCodeEarningIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeEarningIncreasingWage)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductCodeTaxDecreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxDecreasingWage)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductCodeTaxIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxIncreasingWage)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.PR.Standalone.PRDeductCode.PRDeductionsReducingDisposableNetCollection -> Collection(PX.Objects.PR.PRDeductionsReducingDisposableNet)
PX.Objects.PR.Standalone.PRDeductCode.PREmployeeDeductCollection -> Collection(PX.Objects.PR.PREmployeeDeduct)
PX.Objects.PR.Standalone.PRDeductCode.PRNonPayableBenefitsIncreasingDisposableNetCollection -> Collection(PX.Objects.PR.PRNonPayableBenefitsIncreasingDisposableNet)
PX.Objects.PR.Standalone.PRDeductCode.PRPaymentDeductCollection -> Collection(PX.Objects.PR.PRPaymentDeduct)
PX.Objects.PR.Standalone.PRDeductCode.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.PR.Standalone.PRDeductCode.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.PR.Standalone.PRDeductCode.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.PR.Standalone.PRDeductCode.PRPaymentWCPremiumCollection -> Collection(PX.Objects.PR.PRPaymentWCPremium)
PX.Objects.PR.Standalone.PRDeductCode.PRProjectFringeBenefitRateReducingDeductCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct)
PX.Objects.PR.Standalone.PRDeductCode.PRWorkCompensationBenefitRateCollection -> Collection(PX.Objects.PR.PRWorkCompensationBenefitRate)
PX.Objects.PR.Standalone.PRDeductCode.PRWorkCompensationMaximumInsurableWageCollection -> Collection(PX.Objects.PR.PRWorkCompensationMaximumInsurableWage)
PX.Objects.PR.Standalone.PRDeductCode.PRYtdDeductionsCollection -> Collection(PX.Objects.PR.PRYtdDeductions)

# PX.Objects.PR.Standalone.PREarningType (EntityType)

Label: "Payroll Earning Type"
Key: TypeCD
Entity sets: PX_Objects_PR_Standalone_PREarningType, PayrollEarningType, PREarningType

PX.Objects.PR.Standalone.PREarningType.TypeCD : Edm.String [key] "Code"

# PX.Objects.PR.Standalone.PREmployee (EntityType)

Label: "Payroll Employee"
Key: BAccountID
Entity sets: PX_Objects_PR_Standalone_PREmployee, PayrollEmployee1, PREmployee1

PX.Objects.PR.Standalone.PREmployee.BAccountID : Edm.Int32 [key]
PX.Objects.PR.Standalone.PREmployee.ActiveInPayroll : Edm.Boolean
PX.Objects.PR.Standalone.PREmployee.EmployeeClassID : Edm.String
PX.Objects.PR.Standalone.PREmployee.WorkCodeUseDflt : Edm.Boolean
PX.Objects.PR.Standalone.PREmployee.WorkCodeID : Edm.String
PX.Objects.PR.Standalone.PREmployee.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.PR.Standalone.PREmployee.PREmployeeClassByEmployeeClassID -> PX.Objects.PR.PREmployeeClass (EmployeeClassID=EmployeeClassID)
PX.Objects.PR.Standalone.PREmployee.PREmployeeClassByCountryID -> PX.Objects.PR.PREmployeeClass (EmployeeClassID=EmployeeClassID)
PX.Objects.PR.Standalone.PREmployee.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)
PX.Objects.PR.Standalone.PREmployee.AccountByEarningsAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.AccountByDedLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.AccountByBenefitExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.AccountByBenefitLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.AccountByPayrollTaxExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.AccountByPayrollTaxLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.AccountByPtoExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.AccountByPtoLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.AccountByPtoAssetAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PREmployee.SubByEarningsSubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.SubByDedLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.SubByBenefitExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.SubByBenefitLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.SubByPayrollTaxExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.SubByPayrollTaxLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.SubByPtoExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.SubByPtoLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.SubByPtoAssetSubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PREmployee.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.PR.Standalone.PREmployee.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.Objects.PR.Standalone.PREmployee.EPPositionByActivePositionID -> PX.Objects.EP.EPPosition
PX.Objects.PR.Standalone.PREmployee.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup
PX.Objects.PR.Standalone.PREmployee.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)

# PX.Objects.PR.Standalone.PREmployeeClass (EntityType)

Label: "Payroll Employee Class"
Key: EmployeeClassID
Entity sets: PX_Objects_PR_Standalone_PREmployeeClass, PayrollEmployeeClass, PREmployeeClass1

PX.Objects.PR.Standalone.PREmployeeClass.EmployeeClassID : Edm.String [key]
PX.Objects.PR.Standalone.PREmployeeClass.WorkCodeID : Edm.String
PX.Objects.PR.Standalone.PREmployeeClass.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PR.Standalone.PREmployeeClass.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PR.Standalone.PREmployeeClass.PMUnionByUnionID -> PX.Objects.PM.PMUnion
PX.Objects.PR.Standalone.PREmployeeClass.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode (WorkCodeID=WorkCodeID)
PX.Objects.PR.Standalone.PREmployeeClass.CountryByCountryID -> PX.Objects.CS.Country
PX.Objects.PR.Standalone.PREmployeeClass.PRPayGroupByPayGroupID -> PX.Objects.PR.PRPayGroup
PX.Objects.PR.Standalone.PREmployeeClass.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar
PX.Objects.PR.Standalone.PREmployeeClass.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.PR.Standalone.PREmployeeClass.PRBandingRulePTOBankCollection -> Collection(PX.Objects.PR.PRBandingRulePTOBank)
PX.Objects.PR.Standalone.PREmployeeClass.PREmployeeClassPTOBankCollection -> Collection(PX.Objects.PR.PREmployeeClassPTOBank)
PX.Objects.PR.Standalone.PREmployeeClass.PREmployeeClassWorkLocationCollection -> Collection(PX.Objects.PR.PREmployeeClassWorkLocation)

# PX.Objects.PR.Standalone.PRSetup (EntityType)

Label: "Payroll Preferences"
Singletons: PX_Objects_PR_Standalone_PRSetup, PayrollPreferences1, PRSetup1

PX.Objects.PR.Standalone.PRSetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.PR.Standalone.PRSetup.BatchNumberingCD : Edm.String "Payroll Batch Numbering Sequence"
PX.Objects.PR.Standalone.PRSetup.HideEmployeeInfo : Edm.Boolean [required] "Hide Employee Name on Transactions"
PX.Objects.PR.Standalone.PRSetup.ProjectCostAssignment : Edm.String
PX.Objects.PR.Standalone.PRSetup.TimePostingOption : Edm.String
PX.Objects.PR.Standalone.PRSetup.OffBalanceAccountGroupID : Edm.Int32
PX.Objects.PR.Standalone.PRSetup.PMAccountGroupByOffBalanceAccountGroupID -> PX.Objects.PM.PMAccountGroup (OffBalanceAccountGroupID=GroupID)
PX.Objects.PR.Standalone.PRSetup.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PR.Standalone.PRSetup.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PR.Standalone.PRSetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.PR.Standalone.PRSetup.NumberingByBatchNumberingCD -> PX.Objects.CS.Numbering (BatchNumberingCD=NumberingID)
PX.Objects.PR.Standalone.PRSetup.NumberingByTranNumberingCD -> PX.Objects.CS.Numbering
PX.Objects.PR.Standalone.PRSetup.NumberingByRoeNumberingCD -> PX.Objects.CS.Numbering
PX.Objects.PR.Standalone.PRSetup.NumberingByBatchForSubmissionNumberingCD -> PX.Objects.CS.Numbering
PX.Objects.PR.Standalone.PRSetup.NumberingByPtoAdjustmentNumberingCD -> PX.Objects.CS.Numbering
PX.Objects.PR.Standalone.PRSetup.EPEarningTypeByRegularHoursType -> PX.Objects.EP.EPEarningType
PX.Objects.PR.Standalone.PRSetup.EPEarningTypeByHolidaysType -> PX.Objects.EP.EPEarningType
PX.Objects.PR.Standalone.PRSetup.EPEarningTypeByCommissionType -> PX.Objects.EP.EPEarningType

# PX.Objects.PR.Standalone.PRTaxCode (EntityType)

Label: "Payroll Tax Code"
Singletons: PX_Objects_PR_Standalone_PRTaxCode, PayrollTaxCode, PRTaxCode1

PX.Objects.PR.Standalone.PRTaxCode.TaxID : Edm.Int32
PX.Objects.PR.Standalone.PRTaxCode.CountryID : Edm.String
PX.Objects.PR.Standalone.PRTaxCode.IsDeleted : Edm.Boolean [required]
PX.Objects.PR.Standalone.PRTaxCode.VendorByBAccountID -> PX.Objects.AP.Vendor
PX.Objects.PR.Standalone.PRTaxCode.BAccountByBAccountID -> PX.Objects.CR.BAccount
PX.Objects.PR.Standalone.PRTaxCode.UsersByCreatedByID -> PX.SM.Users
PX.Objects.PR.Standalone.PRTaxCode.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.PR.Standalone.PRTaxCode.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.PR.Standalone.PRTaxCode.StateByTaxState -> PX.Objects.CS.State (CountryID=CountryID)
PX.Objects.PR.Standalone.PRTaxCode.StateByCountryID -> PX.Objects.CS.State (CountryID=CountryID)
PX.Objects.PR.Standalone.PRTaxCode.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PRTaxCode.AccountByLiabilityAcctID -> PX.Objects.GL.Account
PX.Objects.PR.Standalone.PRTaxCode.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PRTaxCode.SubByLiabilitySubID -> PX.Objects.GL.Sub
PX.Objects.PR.Standalone.PRTaxCode.PRDeductCodeDetailCollection -> Collection(PX.Objects.PR.PRDeductCodeDetail)
PX.Objects.PR.Standalone.PRTaxCode.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.PR.Standalone.PRTaxCode.PREarningTypeDetailCollection -> Collection(PX.Objects.PR.PREarningTypeDetail)
PX.Objects.PR.Standalone.PRTaxCode.PRPaymentTaxCollection -> Collection(PX.Objects.PR.PRPaymentTax)
PX.Objects.PR.Standalone.PRTaxCode.PRDeductCodeTaxDecreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxDecreasingWage)
PX.Objects.PR.Standalone.PRTaxCode.PRDeductCodeTaxIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeTaxIncreasingWage)
PX.Objects.PR.Standalone.PRTaxCode.PREmployeeTaxCollection -> Collection(PX.Objects.PR.PREmployeeTax)
PX.Objects.PR.Standalone.PRTaxCode.PREmployeeTaxAttributeCollection -> Collection(PX.Objects.PR.PREmployeeTaxAttribute)
PX.Objects.PR.Standalone.PRTaxCode.PREntityTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PREntityTaxCodeAttribute)
PX.Objects.PR.Standalone.PRTaxCode.PRPaymentTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPaymentTaxApplicableAmounts)
PX.Objects.PR.Standalone.PRTaxCode.PRPaymentTaxSplitCollection -> Collection(PX.Objects.PR.PRPaymentTaxSplit)
PX.Objects.PR.Standalone.PRTaxCode.PRTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PRTaxCodeAttribute)
PX.Objects.PR.Standalone.PRTaxCode.PRPeriodTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPeriodTaxApplicableAmounts)
PX.Objects.PR.Standalone.PRTaxCode.PRPeriodTaxesCollection -> Collection(PX.Objects.PR.PRPeriodTaxes)
PX.Objects.PR.Standalone.PRTaxCode.PRYtdTaxesCollection -> Collection(PX.Objects.PR.PRYtdTaxes)

# PX.Objects.RQ.DAC.RQBudgetLedger (EntityType)

Label: "Budget Ledger"
Key: BudgetLedgerID
Entity sets: PX_Objects_RQ_DAC_RQBudgetLedger, BudgetLedger, RQBudgetLedger
Non-filterable, non-selectable: OrganizationName, BaseCuryID, LedgerName

PX.Objects.RQ.DAC.RQBudgetLedger.BudgetLedgerID : Edm.Int32 [key]
PX.Objects.RQ.DAC.RQBudgetLedger.OrganizationName : Edm.String "Company Name"
PX.Objects.RQ.DAC.RQBudgetLedger.BaseCuryID : Edm.String "Base Currency"
PX.Objects.RQ.DAC.RQBudgetLedger.LedgerID : Edm.Int32 "Ledger ID"
PX.Objects.RQ.DAC.RQBudgetLedger.LedgerName : Edm.String "Ledger Name"
PX.Objects.RQ.DAC.RQBudgetLedger.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.DAC.RQBudgetLedger.CreatedByScreenID : Edm.String
PX.Objects.RQ.DAC.RQBudgetLedger.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.RQ.DAC.RQBudgetLedger.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.DAC.RQBudgetLedger.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.DAC.RQBudgetLedger.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.RQ.DAC.RQBudgetLedger.tstamp : Edm.Binary
PX.Objects.RQ.DAC.RQBudgetLedger.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.DAC.RQBudgetLedger.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.DAC.RQBudgetLedger.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization
PX.Objects.RQ.DAC.RQBudgetLedger.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)

# PX.Objects.RQ.RQBidding (EntityType)

Key: LineID
Entity sets: PX_Objects_RQ_RQBidding
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.RQ.RQBidding.LineID : Edm.Int32 [key]
PX.Objects.RQ.RQBidding.ReqNbr : Edm.String
PX.Objects.RQ.RQBidding.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.RQ.RQBidding.VendorID : Edm.Int32 "Vendor"
PX.Objects.RQ.RQBidding.QuoteNumber : Edm.String "Bid Number"
PX.Objects.RQ.RQBidding.QuoteQty : Edm.Decimal [required] "Bid Qty."
PX.Objects.RQ.RQBidding.CuryID : Edm.String "Currency"
PX.Objects.RQ.RQBidding.CuryInfoID : Edm.Int64
PX.Objects.RQ.RQBidding.CuryQuoteUnitCost : Edm.Decimal [required] "Bid Unit Cost"
PX.Objects.RQ.RQBidding.QuoteUnitCost : Edm.Decimal [required]
PX.Objects.RQ.RQBidding.OrderQty : Edm.Decimal [required] "Order Qty."
PX.Objects.RQ.RQBidding.CuryQuoteExtCost : Edm.Decimal [required] "Bid Extended Cost"
PX.Objects.RQ.RQBidding.QuoteExtCost : Edm.Decimal [required]
PX.Objects.RQ.RQBidding.MinQty : Edm.Decimal [required] "Min. Qty."
PX.Objects.RQ.RQBidding.tstamp : Edm.Binary
PX.Objects.RQ.RQBidding.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQBidding.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQBidding.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQBidding.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQBidding.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQBidding.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQBidding.CuryRate : Edm.Decimal
PX.Objects.RQ.RQBidding.CuryViewState : Edm.Boolean
PX.Objects.RQ.RQBidding.RQRequisitionLineByLineNbr -> PX.Objects.RQ.RQRequisitionLine (ReqNbr=ReqNbr, LineNbr=LineNbr)
PX.Objects.RQ.RQBidding.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.RQ.RQBidding.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQBidding.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQBidding.RQBiddingVendorByVendorLocationID -> PX.Objects.RQ.RQBiddingVendor (ReqNbr=ReqNbr, VendorID=VendorID)
PX.Objects.RQ.RQBidding.RQRequisitionByReqNbr -> PX.Objects.RQ.RQRequisition (ReqNbr=ReqNbr)
PX.Objects.RQ.RQBidding.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)

# PX.Objects.RQ.RQBiddingVendor (EntityType)

Label: "Bidding Vendor"
Key: LineID
Entity sets: PX_Objects_RQ_RQBiddingVendor, BiddingVendor, RQBiddingVendor
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.RQ.RQBiddingVendor.LineID : Edm.Int32 [key]
PX.Objects.RQ.RQBiddingVendor.ReqNbr : Edm.String
PX.Objects.RQ.RQBiddingVendor.VendorID : Edm.Int32 "Vendor"
PX.Objects.RQ.RQBiddingVendor.RemitAddressID : Edm.Int32 "RemitAddressID"
PX.Objects.RQ.RQBiddingVendor.RemitContactID : Edm.Int32
PX.Objects.RQ.RQBiddingVendor.CuryID : Edm.String "Currency"
PX.Objects.RQ.RQBiddingVendor.CuryInfoID : Edm.Int64 "Currency"
PX.Objects.RQ.RQBiddingVendor.EntryDate : Edm.DateTimeOffset "Entry Date"
PX.Objects.RQ.RQBiddingVendor.ExpireDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.RQ.RQBiddingVendor.PromisedDate : Edm.DateTimeOffset "Promised Date"
PX.Objects.RQ.RQBiddingVendor.FOBPoint : Edm.String "FOB Point"
PX.Objects.RQ.RQBiddingVendor.ShipVia : Edm.String "Ship Via"
PX.Objects.RQ.RQBiddingVendor.TotalQuoteQty : Edm.Decimal [required] "Total Bid Qty."
PX.Objects.RQ.RQBiddingVendor.CuryTotalQuoteExtCost : Edm.Decimal [required] "Total Extended Cost"
PX.Objects.RQ.RQBiddingVendor.TotalQuoteExtCost : Edm.Decimal [required]
PX.Objects.RQ.RQBiddingVendor.Status : Edm.Boolean [required] "Request Sent"
PX.Objects.RQ.RQBiddingVendor.tstamp : Edm.Binary
PX.Objects.RQ.RQBiddingVendor.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQBiddingVendor.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQBiddingVendor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQBiddingVendor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQBiddingVendor.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQBiddingVendor.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQBiddingVendor.CuryRate : Edm.Decimal
PX.Objects.RQ.RQBiddingVendor.CuryViewState : Edm.Boolean
PX.Objects.RQ.RQBiddingVendor.POAddressByRemitAddressID -> PX.Objects.PO.POAddress (RemitAddressID=AddressID)
PX.Objects.RQ.RQBiddingVendor.POContactByRemitContactID -> PX.Objects.PO.POContact (RemitContactID=ContactID)
PX.Objects.RQ.RQBiddingVendor.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.RQ.RQBiddingVendor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQBiddingVendor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQBiddingVendor.RQRequisitionByReqNbr -> PX.Objects.RQ.RQRequisition (ReqNbr=ReqNbr)
PX.Objects.RQ.RQBiddingVendor.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.RQ.RQBiddingVendor.FOBPointByFOBPoint -> PX.Objects.CS.FOBPoint (FOBPoint=FOBPointID)
PX.Objects.RQ.RQBiddingVendor.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.RQ.RQBiddingVendor.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)

# PX.Objects.RQ.RQBudget (EntityType)

Label: "Request Budget Line"
Key: ExpenseAcctID, ExpenseSubID
Entity sets: PX_Objects_RQ_RQBudget, RequestBudgetLine, RQBudget
Non-filterable, non-selectable: DocRequestAmt, CuryDocRequestAmt, BudgetAmt, UsageAmt

PX.Objects.RQ.RQBudget.CuryID : Edm.String "Currency"
PX.Objects.RQ.RQBudget.CuryInfoID : Edm.Int64
PX.Objects.RQ.RQBudget.ExpenseAcctID : Edm.Int32 [key] "Account"
PX.Objects.RQ.RQBudget.ExpenseSubID : Edm.Int32 [key] "Sub."
PX.Objects.RQ.RQBudget.DocRequestAmt : Edm.Decimal "Document Amount"
PX.Objects.RQ.RQBudget.CuryDocRequestAmt : Edm.Decimal
PX.Objects.RQ.RQBudget.RequestAmt : Edm.Decimal "Request Amount"
PX.Objects.RQ.RQBudget.CuryRequestAmt : Edm.Decimal
PX.Objects.RQ.RQBudget.AprovedAmt : Edm.Decimal "Approved Amount"
PX.Objects.RQ.RQBudget.CuryAprovedAmt : Edm.Decimal
PX.Objects.RQ.RQBudget.UnaprovedAmt : Edm.Decimal "Unapproved Amount"
PX.Objects.RQ.RQBudget.CuryUnaprovedAmt : Edm.Decimal
PX.Objects.RQ.RQBudget.OrderNbr : Edm.String "Ref. Nbr."
PX.Objects.RQ.RQBudget.OrderDate : Edm.DateTimeOffset "Date"
PX.Objects.RQ.RQBudget.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.RQ.RQBudget.BudgetAmt : Edm.Decimal "Budget Amount"
PX.Objects.RQ.RQBudget.UsageAmt : Edm.Decimal "Amount Spent"
PX.Objects.RQ.RQBudget.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.RQ.RQBudget.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)

# PX.Objects.RQ.RQInventoryItem (EntityType)

Key: InventoryCD
Entity sets: PX_Objects_RQ_RQInventoryItem

PX.Objects.RQ.RQInventoryItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.RQ.RQInventoryItem.InventoryCD : Edm.String [key] "Inventory ID"
PX.Objects.RQ.RQInventoryItem.Descr : Edm.String "Description"
PX.Objects.RQ.RQInventoryItem.ItemClassID : Edm.Int32 "Item Class"
PX.Objects.RQ.RQInventoryItem.ItemStatus : Edm.String "Item Status"
PX.Objects.RQ.RQInventoryItem.ItemType : Edm.String "Type"
PX.Objects.RQ.RQInventoryItem.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.RQ.RQInventoryItem.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.Objects.RQ.RQInventoryItem.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.RQ.RQInventoryItem.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.RQ.RQInventoryItem.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.RQ.RQInventoryItem.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.RQ.RQInventoryItem.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.RQ.RQInventoryItem.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.RQ.RQInventoryItem.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.RQ.RQInventoryItem.FSAppointmentLogExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentLogExtItemLine)
PX.Objects.RQ.RQInventoryItem.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.RQ.RQInventoryItem.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.RQ.RQInventoryItem.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.RQ.RQInventoryItem.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.RQ.RQInventoryItem.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.RQ.RQInventoryItem.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.RQ.RQInventoryItem.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.RQ.RQInventoryItem.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.RQ.RQInventoryItem.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.RQ.RQInventoryItem.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.RQ.RQInventoryItem.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.RQ.RQInventoryItem.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.RQ.RQInventoryItem.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.RQ.RQInventoryItem.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.RQ.RQInventoryItem.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.RQ.RQInventoryItem.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.RQ.RQInventoryItem.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.RQ.RQInventoryItem.INMatrixExcludedDataCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
PX.Objects.RQ.RQInventoryItem.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.RQ.RQInventoryItem.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.Objects.RQ.RQInventoryItem.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.RQ.RQInventoryItem.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.RQ.RQInventoryItem.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.RQ.RQInventoryItem.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.RQ.RQInventoryItem.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.RQ.RQInventoryItem.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.RQ.RQInventoryItem.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.RQ.RQInventoryItem.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.RQ.RQInventoryItem.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.RQ.RQInventoryItem.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.RQ.RQInventoryItem.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.RQ.RQInventoryItem.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.RQ.RQInventoryItem.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.RQ.RQInventoryItem.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.RQ.RQInventoryItem.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.RQ.RQInventoryItem.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.RQ.RQInventoryItem.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.RQ.RQInventoryItem.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.RQ.RQInventoryItem.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.RQ.RQInventoryItem.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.RQ.RQInventoryItem.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.RQ.RQInventoryItem.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.RQ.RQInventoryItem.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.RQ.RQInventoryItem.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.RQ.RQInventoryItem.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.RQ.RQInventoryItem.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.RQ.RQInventoryItem.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.RQ.RQInventoryItem.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.RQ.RQInventoryItem.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.RQ.RQInventoryItem.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.RQ.RQInventoryItem.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.RQ.RQInventoryItem.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.Objects.RQ.RQInventoryItem.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.RQ.RQInventoryItem.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.RQ.RQInventoryItem.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.RQ.RQInventoryItem.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.RQ.RQInventoryItem.InventoryPostingBatchDetailCollection -> Collection(PX.Objects.FS.InventoryPostingBatchDetail)
PX.Objects.RQ.RQInventoryItem.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.RQ.RQInventoryItem.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.RQ.RQInventoryItem.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.RQ.RQInventoryItem.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.RQ.RQInventoryItem.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.RQ.RQInventoryItem.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.RQ.RQInventoryItem.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.RQ.RQInventoryItem.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.RQ.RQInventoryItem.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.RQ.RQInventoryItem.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.RQ.RQInventoryItem.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.RQ.RQInventoryItem.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.RQ.RQInventoryItem.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.RQ.RQInventoryItem.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.RQ.RQInventoryItem.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.RQ.RQInventoryItem.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.RQ.RQInventoryItem.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.RQ.RQInventoryItem.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.RQ.RQInventoryItem.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.RQ.RQInventoryItem.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.RQ.RQInventoryItem.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.RQ.RQInventoryItem.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.RQ.RQInventoryItem.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.RQ.RQInventoryItem.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.RQ.RQInventoryItem.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.RQ.RQInventoryItem.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.RQ.RQInventoryItem.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.RQ.RQInventoryItem.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.RQ.RQInventoryItem.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.Objects.RQ.RQInventoryItem.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.RQ.RQInventoryItem.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.RQ.RQInventoryItem.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.RQ.RQInventoryItem.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.RQ.RQInventoryItem.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.RQ.RQInventoryItem.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.RQ.RQInventoryItem.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)
PX.Objects.RQ.RQInventoryItem.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.Objects.RQ.RQInventoryItem.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.RQ.RQInventoryItem.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.RQ.RQInventoryItem.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.Objects.RQ.RQInventoryItem.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.RQ.RQInventoryItem.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.RQ.RQInventoryItem.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.RQ.RQInventoryItem.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.Objects.RQ.RQInventoryItem.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.RQ.RQInventoryItem.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.RQ.RQInventoryItem.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.RQ.RQInventoryItem.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.RQ.RQInventoryItem.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.RQ.RQInventoryItem.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.RQ.RQInventoryItem.InventoryItemLotSerNumValCollection -> Collection(PX.Objects.IN.InventoryItemLotSerNumVal)
PX.Objects.RQ.RQInventoryItem.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.RQ.RQInventoryItem.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.RQ.RQInventoryItem.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.RQ.RQInventoryItem.INRelatedInventoryUserFeedbackCollection -> Collection(PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback)
PX.Objects.RQ.RQInventoryItem.INAttributeDescriptionGroupCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup)
PX.Objects.RQ.RQInventoryItem.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.Objects.RQ.RQInventoryItem.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.RQ.RQInventoryItem.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.RQ.RQInventoryItem.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.RQ.RQInventoryItem.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.RQ.RQInventoryItem.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)
PX.Objects.RQ.RQInventoryItem.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.Objects.RQ.RQInventoryItem.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.RQ.RQInventoryItem.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.RQ.RQInventoryItem.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.RQ.RQInventoryItem.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.Objects.RQ.RQInventoryItem.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.RQ.RQInventoryItem.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.RQ.RQInventoryItem.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.RQ.RQInventoryItem.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.RQ.RQInventoryItem.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.RQ.RQInventoryItem.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.RQ.RQInventoryItem.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.Objects.RQ.RQInventoryItem.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.Objects.RQ.RQInventoryItem.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.RQ.RQInventoryItem.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.RQ.RQInventoryItem.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.RQ.RQInventoryItem.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.RQ.RQInventoryItem.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.RQ.RQInventoryItem.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.RQ.RQInventoryItem.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.RQ.RQInventoryItem.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Objects.RQ.RQInventoryItem.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.Objects.RQ.RQInventoryItem.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.RQ.RQInventoryItem.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.RQ.RQInventoryItem.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.RQ.RQInventoryItem.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.RQ.RQInventoryItem.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.RQ.RQInventoryItem.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.RQ.RQInventoryItem.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.RQ.RQInventoryItem.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.RQ.RQInventoryItem.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.RQ.RQInventoryItem.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.RQ.RQInventoryItem.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.RQ.RQInventoryItem.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.RQ.RQInventoryItem.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.Objects.RQ.RQInventoryItem.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.RQ.RQInventoryItem.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.RQ.RQInventoryItem.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.RQ.RQInventoryItem.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.RQ.RQInventoryItem.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.RQ.RQInventoryItem.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.RQ.RQInventoryItem.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.RQ.RQInventoryItem.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.RQ.RQInventoryItem.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.RQ.RQInventoryItem.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.RQ.RQInventoryItem.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.RQ.RQInventoryItem.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.RQ.RQInventoryItem.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.RQ.RQInventoryItem.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.RQ.RQInventoryItem.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.RQ.RQInventoryItem.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.RQ.RQInventoryItem.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.RQ.RQInventoryItem.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.RQ.RQInventoryItem.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.RQ.RQInventoryItem.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.RQ.RQInventoryItem.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.Objects.RQ.RQInventoryItem.FSServiceInventoryItemCollection -> Collection(PX.Objects.FS.FSServiceInventoryItem)
PX.Objects.RQ.RQInventoryItem.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)
PX.Objects.RQ.RQInventoryItem.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)
PX.Objects.RQ.RQInventoryItem.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.Objects.RQ.RQInventoryItem.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)
PX.Objects.RQ.RQInventoryItem.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.RQ.RQInventoryItem.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.RQ.RQInventoryItem.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.RQ.RQInventoryItem.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.RQ.RQInventoryItem.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.RQ.RQInventoryItem.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.RQ.RQInventoryItem.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.RQ.RQInventoryItem.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.RQ.RQInventoryItem.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.RQ.RQInventoryItem.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.RQ.RQInventoryItem.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.RQ.RQInventoryItem.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.RQ.RQInventoryItem.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.RQ.RQInventoryItem.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.RQ.RQInventoryItem.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.RQ.RQInventoryItem.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.RQ.RQInventoryItem.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.RQ.RQInventoryItem.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.RQ.RQInventoryItem.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.RQ.RQInventoryItem.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.RQ.RQInventoryItem.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.RQ.RQInventoryItem.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.RQ.RQInventoryItem.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.RQ.RQInventoryItem.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.RQ.RQInventoryItem.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.RQ.RQInventoryItem.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.RQ.RQInventoryItem.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.RQ.RQInventoryItem.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.RQ.RQInventoryItem.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.RQ.RQInventoryItem.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.RQ.RQInventoryItem.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.RQ.RQInventoryItem.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.RQ.RQInventoryItem.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.RQ.RQInventoryItem.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.RQ.RQInventoryItem.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.RQ.RQInventoryItem.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.RQ.RQInventoryItem.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.RQ.RQInventoryItem.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.RQ.RQInventoryItem.POLineRCollection -> Collection(PX.Objects.PO.POLineR)
PX.Objects.RQ.RQInventoryItem.PMItemRateCollection -> Collection(PX.Objects.PM.PMItemRate)
PX.Objects.RQ.RQInventoryItem.PMProjectARTranPostDetailCollection -> Collection(PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail)
PX.Objects.RQ.RQInventoryItem.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.RQ.RQInventoryItem.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.RQ.RQInventoryItem.INItemLotSerialCollection -> Collection(PX.Objects.IN.INItemLotSerial)
PX.Objects.RQ.RQInventoryItem.INItemSalesHistCollection -> Collection(PX.Objects.IN.INItemSalesHist)
PX.Objects.RQ.RQInventoryItem.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.RQ.RQInventoryItem.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.RQ.RQInventoryItem.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.RQ.RQInventoryItem.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.RQ.RQInventoryItem.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.RQ.RQInventoryItem.INSubItemSegmentValueCollection -> Collection(PX.Objects.IN.INSubItemSegmentValue)
PX.Objects.RQ.RQInventoryItem.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.RQ.RQInventoryItem.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.RQ.RQInventoryItem.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.RQ.RQInventoryItem.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.RQ.RQInventoryItem.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.RQ.RQInventoryItem.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.RQ.RQInventoryItem.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.RQ.RQInventoryItem.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.RQ.RQInventoryItem.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.RQ.RQInventoryItem.RelatedItemCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItem)
PX.Objects.RQ.RQInventoryItem.INItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeader)
PX.Objects.RQ.RQInventoryItem.BCInventoryFileUrlsCollection -> Collection(PX.Commerce.Objects.BCInventoryFileUrls)
PX.Objects.RQ.RQInventoryItem.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.RQ.RQInventoryItem.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.RQ.RQInventoryItem.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.RQ.RQInventoryItem.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.RQ.RQInventoryItem.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.RQ.RQInventoryItem.SchedulerEmployeeInventoryItemCollection -> Collection(PX.Objects.FS.SchedulerEmployeeInventoryItem)
PX.Objects.RQ.RQInventoryItem.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)
PX.Objects.RQ.RQInventoryItem.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.RQ.RQInventoryItem.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.RQ.RQInventoryItem.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.RQ.RQInventoryItem.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.RQ.RQNotification (EntityType)

Label: "Default Notification setup"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_RQ_RQNotification

# PX.Objects.RQ.RQRequest (EntityType)

Label: "Request"
Key: OrderNbr
Entity sets: PX_Objects_RQ_RQRequest, Request, RQRequest
Non-filterable, non-selectable: Rejected, NoteText, VendorHidden, CustomerRequest, BudgetValidation, ApprovalWorkgroupID, ApprovalOwnerID, SiteIdErrorMessage, CuryRate, CuryViewState

PX.Objects.RQ.RQRequest.OrderNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.RQ.RQRequest.OrderDate : Edm.DateTimeOffset "Date"
PX.Objects.RQ.RQRequest.ReqClassID : Edm.String "Request Class"
PX.Objects.RQ.RQRequest.Priority : Edm.Int32 [required] "Priority"
PX.Objects.RQ.RQRequest.Status : Edm.String "Status"
PX.Objects.RQ.RQRequest.Description : Edm.String "Description"
PX.Objects.RQ.RQRequest.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.RQ.RQRequest.Hold : Edm.Boolean [required] "Hold"
PX.Objects.RQ.RQRequest.Approved : Edm.Boolean [required]
PX.Objects.RQ.RQRequest.Rejected : Edm.Boolean "Reject"
PX.Objects.RQ.RQRequest.Cancelled : Edm.Boolean [required] "Cancel"
PX.Objects.RQ.RQRequest.NoteID : Edm.Guid
PX.Objects.RQ.RQRequest.NoteText : Edm.String "Note Text"
PX.Objects.RQ.RQRequest.VendorHidden : Edm.Boolean "Vendor Hidden"
PX.Objects.RQ.RQRequest.CustomerRequest : Edm.Boolean "Customer Request"
PX.Objects.RQ.RQRequest.BudgetValidation : Edm.Boolean "Budget Validation"
PX.Objects.RQ.RQRequest.VendorID : Edm.Int32 "Vendor"
PX.Objects.RQ.RQRequest.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.RQ.RQRequest.OwnerID : Edm.Int32 "Owner"
PX.Objects.RQ.RQRequest.ApprovalWorkgroupID : Edm.Int32 "Approval Workgroup ID"
PX.Objects.RQ.RQRequest.ApprovalOwnerID : Edm.Int32 "Approver"
PX.Objects.RQ.RQRequest.CheckBudget : Edm.Boolean [required] "Check Budget"
PX.Objects.RQ.RQRequest.ShipDestType : Edm.String "Shipping Destination Type"
PX.Objects.RQ.RQRequest.SiteIdErrorMessage : Edm.String
PX.Objects.RQ.RQRequest.ShipToBAccountID : Edm.Int32 "Ship To"
PX.Objects.RQ.RQRequest.ShipAddressID : Edm.Int32 "ShipAddressID"
PX.Objects.RQ.RQRequest.ShipContactID : Edm.Int32 "ShipContactID"
PX.Objects.RQ.RQRequest.RemitAddressID : Edm.Int32 "RemitAddressID"
PX.Objects.RQ.RQRequest.RemitContactID : Edm.Int32
PX.Objects.RQ.RQRequest.EmployeeID : Edm.Int32 "Requested By"
PX.Objects.RQ.RQRequest.DepartmentID : Edm.String "Department"
PX.Objects.RQ.RQRequest.CuryID : Edm.String "Currency"
PX.Objects.RQ.RQRequest.CuryInfoID : Edm.Int64
PX.Objects.RQ.RQRequest.OpenOrderQty : Edm.Decimal [required] "Open Qty."
PX.Objects.RQ.RQRequest.CuryEstExtCostTotal : Edm.Decimal [required] "Est. Ext. Cost"
PX.Objects.RQ.RQRequest.EstExtCostTotal : Edm.Decimal [required]
PX.Objects.RQ.RQRequest.Purpose : Edm.String "Purpose"
PX.Objects.RQ.RQRequest.LineCntr : Edm.Int32 [required]
PX.Objects.RQ.RQRequest.IsOverbudget : Edm.Boolean [required] "Is Over Budget"
PX.Objects.RQ.RQRequest.tstamp : Edm.Binary
PX.Objects.RQ.RQRequest.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQRequest.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQRequest.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.RQ.RQRequest.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQRequest.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQRequest.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.RQ.RQRequest.CuryRate : Edm.Decimal
PX.Objects.RQ.RQRequest.CuryViewState : Edm.Boolean
PX.Objects.RQ.RQRequest.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.RQ.RQRequest.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.RQ.RQRequest.BAccountByShipToBAccountID -> PX.Objects.CR.BAccount (ShipToBAccountID=BAccountID)
PX.Objects.RQ.RQRequest.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.RQ.RQRequest.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.RQ.RQRequest.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQRequest.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQRequest.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.RQ.RQRequest.RQRequestClassByReqClassID -> PX.Objects.RQ.RQRequestClass (ReqClassID=ReqClassID)
PX.Objects.RQ.RQRequest.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.RQ.RQRequest.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.RQ.RQRequest.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.RQ.RQRequest.LocationByShipToBAccountID -> PX.Objects.CR.Location (ShipToBAccountID=BAccountID)
PX.Objects.RQ.RQRequest.LocationByEmployeeID -> PX.Objects.CR.Location (EmployeeID=BAccountID)
PX.Objects.RQ.RQRequest.EPDepartmentByDepartmentID -> PX.Objects.EP.EPDepartment (DepartmentID=DepartmentID)
PX.Objects.RQ.RQRequest.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)

# PX.Objects.RQ.RQRequestClass (EntityType)

Label: "Request Class"
Key: ReqClassID
Entity sets: PX_Objects_RQ_RQRequestClass, RequestClass, RQRequestClass
Non-filterable, non-selectable: NoteText

PX.Objects.RQ.RQRequestClass.ReqClassID : Edm.String [key] "Request Class"
PX.Objects.RQ.RQRequestClass.Descr : Edm.String "Description"
PX.Objects.RQ.RQRequestClass.VendorNotRequest : Edm.Boolean [required] "Vendor Information Is Not Required"
PX.Objects.RQ.RQRequestClass.VendorMultiply : Edm.Boolean [required] "Allow Multiple Vendors per Request"
PX.Objects.RQ.RQRequestClass.RestrictItemList : Edm.Boolean [required] "Restrict Requested Items to the Specified List"
PX.Objects.RQ.RQRequestClass.HideInventoryID : Edm.Boolean [required] "Hide Inventory Item"
PX.Objects.RQ.RQRequestClass.IssueRequestor : Edm.Boolean [required] "Issue to Requester"
PX.Objects.RQ.RQRequestClass.CustomerRequest : Edm.Boolean [required] "Customer Request"
PX.Objects.RQ.RQRequestClass.ExpenseAccountDefault : Edm.String "Use Expense Account From"
PX.Objects.RQ.RQRequestClass.PromisedLeadTime : Edm.Int16 [required] "Promised Lead Time (Days)"
PX.Objects.RQ.RQRequestClass.BudgetValidation : Edm.Int32 [required] "Budget Validation"
PX.Objects.RQ.RQRequestClass.NoteID : Edm.Guid
PX.Objects.RQ.RQRequestClass.NoteText : Edm.String "Note Text"
PX.Objects.RQ.RQRequestClass.tstamp : Edm.Binary
PX.Objects.RQ.RQRequestClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQRequestClass.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQRequestClass.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.RQ.RQRequestClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQRequestClass.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQRequestClass.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.RQ.RQRequestClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQRequestClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQRequestClass.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.RQ.RQRequestClass.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.RQ.RQRequestClass.RQRequestLineOwnedCollection -> Collection(PX.Objects.RQ.RQRequestLineOwned)
PX.Objects.RQ.RQRequestClass.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.RQ.RQRequestClass.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.Objects.RQ.RQRequestClass.RQSetupCollection -> Collection(PX.Objects.RQ.RQSetup)

# PX.Objects.RQ.RQRequestClassItem (EntityType)

Key: LineID
Entity sets: PX_Objects_RQ_RQRequestClassItem

PX.Objects.RQ.RQRequestClassItem.LineID : Edm.Int32 [key]
PX.Objects.RQ.RQRequestClassItem.ReqClassID : Edm.String "Class"
PX.Objects.RQ.RQRequestClassItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.RQ.RQRequestClassItem.tstamp : Edm.Binary
PX.Objects.RQ.RQRequestClassItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQRequestClassItem.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQRequestClassItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQRequestClassItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQRequestClassItem.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQRequestClassItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQRequestClassItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.RQ.RQRequestClassItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQRequestClassItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQRequestClassItem.RQRequestClassByReqClassID -> PX.Objects.RQ.RQRequestClass (ReqClassID=ReqClassID)
PX.Objects.RQ.RQRequestClassItem.RQInventoryItemByInventoryID -> PX.Objects.RQ.RQInventoryItem (InventoryID=InventoryID)

# PX.Objects.RQ.RQRequestLine (EntityType)

Label: "Request Line"
Key: LineNbr, OrderNbr
Entity sets: PX_Objects_RQ_RQRequestLine, RequestLine, RQRequestLine
Non-filterable, non-selectable: IssueStatus, NoteText, Updatable, CuryID, CuryRate, CuryViewState

PX.Objects.RQ.RQRequestLine.BranchID : Edm.Int32 "Branch"
PX.Objects.RQ.RQRequestLine.OrderNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.RQ.RQRequestLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.RQ.RQRequestLine.DepartmentID : Edm.String
PX.Objects.RQ.RQRequestLine.InventoryID : Edm.Int32 "Inventory"
PX.Objects.RQ.RQRequestLine.Description : Edm.String "Description"
PX.Objects.RQ.RQRequestLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.RQ.RQRequestLine.VendorName : Edm.String "Vendor Name"
PX.Objects.RQ.RQRequestLine.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.RQ.RQRequestLine.VendorDescription : Edm.String "Vendor Description"
PX.Objects.RQ.RQRequestLine.UOM : Edm.String "UOM"
PX.Objects.RQ.RQRequestLine.AlternateID : Edm.String "Alternate ID"
PX.Objects.RQ.RQRequestLine.OrderQty : Edm.Decimal [required] "Order Qty."
PX.Objects.RQ.RQRequestLine.BaseOrderQty : Edm.Decimal [required]
PX.Objects.RQ.RQRequestLine.OriginQty : Edm.Decimal [required] "Original Qty."
PX.Objects.RQ.RQRequestLine.BaseOriginQty : Edm.Decimal [required]
PX.Objects.RQ.RQRequestLine.IssuedQty : Edm.Decimal [required] "Issued Qty."
PX.Objects.RQ.RQRequestLine.BaseIssuedQty : Edm.Decimal [required]
PX.Objects.RQ.RQRequestLine.ReqQty : Edm.Decimal [required] "Requisition Qty."
PX.Objects.RQ.RQRequestLine.BaseReqQty : Edm.Decimal
PX.Objects.RQ.RQRequestLine.OpenQty : Edm.Decimal [required] "Open Qty."
PX.Objects.RQ.RQRequestLine.BaseOpenQty : Edm.Decimal
PX.Objects.RQ.RQRequestLine.IssueStatus : Edm.String "Issue Status"
PX.Objects.RQ.RQRequestLine.CuryInfoID : Edm.Int64
PX.Objects.RQ.RQRequestLine.CuryEstUnitCost : Edm.Decimal [required] "Est. Unit Cost"
PX.Objects.RQ.RQRequestLine.EstUnitCost : Edm.Decimal [required]
PX.Objects.RQ.RQRequestLine.CuryEstExtCost : Edm.Decimal [required] "Est. Ext. Cost"
PX.Objects.RQ.RQRequestLine.EstExtCost : Edm.Decimal [required]
PX.Objects.RQ.RQRequestLine.ManualPrice : Edm.Boolean [required] "Manual Cost"
PX.Objects.RQ.RQRequestLine.NoteID : Edm.Guid
PX.Objects.RQ.RQRequestLine.NoteText : Edm.String "Note Text"
PX.Objects.RQ.RQRequestLine.RequestedDate : Edm.DateTimeOffset "Required Date"
PX.Objects.RQ.RQRequestLine.PromisedDate : Edm.DateTimeOffset "Promised Date"
PX.Objects.RQ.RQRequestLine.Approved : Edm.Boolean [required] "Approved"
PX.Objects.RQ.RQRequestLine.Cancelled : Edm.Boolean [required] "Canceled"
PX.Objects.RQ.RQRequestLine.tstamp : Edm.Binary
PX.Objects.RQ.RQRequestLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQRequestLine.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQRequestLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQRequestLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQRequestLine.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQRequestLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQRequestLine.Updatable : Edm.Boolean
PX.Objects.RQ.RQRequestLine.CuryID : Edm.String "Currency"
PX.Objects.RQ.RQRequestLine.CuryRate : Edm.Decimal
PX.Objects.RQ.RQRequestLine.CuryViewState : Edm.Boolean
PX.Objects.RQ.RQRequestLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.RQ.RQRequestLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.RQ.RQRequestLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.RQ.RQRequestLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQRequestLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQRequestLine.RQRequestByOrderNbr -> PX.Objects.RQ.RQRequest (OrderNbr=OrderNbr)
PX.Objects.RQ.RQRequestLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.RQ.RQRequestLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.RQ.RQRequestLine.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.RQ.RQRequestLine.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.RQ.RQRequestLine.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.RQ.RQRequestLine.RQRequisitionContentCollection -> Collection(PX.Objects.RQ.RQRequisitionContent)

# PX.Objects.RQ.RQRequestLineOwned (EntityType)

Label: "Request Line"
BaseType: PX.Objects.RQ.RQRequestLine
Key: LineNbr, OrderNbr (inherited from PX.Objects.RQ.RQRequestLine)
Entity sets: PX_Objects_RQ_RQRequestLineOwned

PX.Objects.RQ.RQRequestLineOwned.ReqClassID : Edm.String "Request Class"
PX.Objects.RQ.RQRequestLineOwned.Priority : Edm.Int32 "Priority"
PX.Objects.RQ.RQRequestLineOwned.OrderDate : Edm.DateTimeOffset "Date"
PX.Objects.RQ.RQRequestLineOwned.CustomerRequest : Edm.Boolean "Customer Request"
PX.Objects.RQ.RQRequestLineOwned.EmployeeID : Edm.Int32 "Requested By"
PX.Objects.RQ.RQRequestLineOwned.ShipDestType : Edm.String "Shipping Destination Type"
PX.Objects.RQ.RQRequestLineOwned.BaseCuryID : Edm.String
PX.Objects.RQ.RQRequestLineOwned.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.RQ.RQRequestLineOwned.RQRequestClassByReqClassID -> PX.Objects.RQ.RQRequestClass (ReqClassID=ReqClassID)
PX.Objects.RQ.RQRequestLineOwned.BAccountByShipToBAccountID -> PX.Objects.CR.BAccount
PX.Objects.RQ.RQRequestLineOwned.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)

# PX.Objects.RQ.RQRequestLineSelect (EntityType)

Key: LineNbr, OrderNbr
Entity sets: PX_Objects_RQ_RQRequestLineSelect
Non-filterable, non-selectable: SelectQty, BaseSelectQty

PX.Objects.RQ.RQRequestLineSelect.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.RQ.RQRequestLineSelect.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.RQ.RQRequestLineSelect.CuryID : Edm.String "Currency"
PX.Objects.RQ.RQRequestLineSelect.SelectQty : Edm.Decimal "Select Qty."
PX.Objects.RQ.RQRequestLineSelect.BaseSelectQty : Edm.Decimal
PX.Objects.RQ.RQRequestLineSelect.OpenQty : Edm.Decimal "Open Qty."
PX.Objects.RQ.RQRequestLineSelect.BaseOpenQty : Edm.Decimal
PX.Objects.RQ.RQRequestLineSelect.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.RQ.RQRequestLineSelect.Description : Edm.String "Description"
PX.Objects.RQ.RQRequestLineSelect.UOM : Edm.String "UOM"
PX.Objects.RQ.RQRequestLineSelect.VendorID : Edm.Int32 "Vendor"
PX.Objects.RQ.RQRequestLineSelect.VendorName : Edm.String "Vendor Name"
PX.Objects.RQ.RQRequestLineSelect.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.RQ.RQRequestLineSelect.VendorDescription : Edm.String "Vendor Description"
PX.Objects.RQ.RQRequestLineSelect.AlternateID : Edm.String "Alternate ID"
PX.Objects.RQ.RQRequestLineSelect.RequestedDate : Edm.DateTimeOffset "Required Date"
PX.Objects.RQ.RQRequestLineSelect.PromisedDate : Edm.DateTimeOffset "Promised Date"
PX.Objects.RQ.RQRequestLineSelect.ReqQty : Edm.Decimal "Requisition Qty."
PX.Objects.RQ.RQRequestLineSelect.BaseReqQty : Edm.Decimal
PX.Objects.RQ.RQRequestLineSelect.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.RQ.RQRequestLineSelect.RQRequestByOrderNbr -> PX.Objects.RQ.RQRequest (OrderNbr=OrderNbr)
PX.Objects.RQ.RQRequestLineSelect.RQRequisitionContentCollection -> Collection(PX.Objects.RQ.RQRequisitionContent)

# PX.Objects.RQ.RQRequisition (EntityType)

Label: "Requisition"
Key: ReqNbr
Entity sets: PX_Objects_RQ_RQRequisition, Requisition, RQRequisition
Non-filterable, non-selectable: Rejected, NoteText, ApprovalWorkgroupID, ApprovalOwnerID, SiteIdErrorMessage, VendorRequestSent, SkipValidateWithVendorCuryOrRate, CuryRate, CuryViewState

PX.Objects.RQ.RQRequisition.ReqNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.RQ.RQRequisition.OrderDate : Edm.DateTimeOffset "Date"
PX.Objects.RQ.RQRequisition.Priority : Edm.Int32 [required] "Priority"
PX.Objects.RQ.RQRequisition.Status : Edm.String "Status"
PX.Objects.RQ.RQRequisition.Description : Edm.String "Description"
PX.Objects.RQ.RQRequisition.Hold : Edm.Boolean [required] "Hold"
PX.Objects.RQ.RQRequisition.Approved : Edm.Boolean [required] "Approved"
PX.Objects.RQ.RQRequisition.Rejected : Edm.Boolean "Reject"
PX.Objects.RQ.RQRequisition.Cancelled : Edm.Boolean [required] "Cancel"
PX.Objects.RQ.RQRequisition.Splittable : Edm.Boolean [required] "Splittable"
PX.Objects.RQ.RQRequisition.Released : Edm.Boolean [required] "Released"
PX.Objects.RQ.RQRequisition.BiddingComplete : Edm.Boolean [required] "Complete Bidding"
PX.Objects.RQ.RQRequisition.Quoted : Edm.Boolean [required] "Quoted"
PX.Objects.RQ.RQRequisition.NoteID : Edm.Guid
PX.Objects.RQ.RQRequisition.NoteText : Edm.String "Note Text"
PX.Objects.RQ.RQRequisition.EmployeeID : Edm.Int32 "Creator"
PX.Objects.RQ.RQRequisition.CustomerID : Edm.Int32 "Customer"
PX.Objects.RQ.RQRequisition.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.RQ.RQRequisition.OwnerID : Edm.Int32 "Owner"
PX.Objects.RQ.RQRequisition.ApprovalWorkgroupID : Edm.Int32 "Approval Workgroup ID"
PX.Objects.RQ.RQRequisition.ApprovalOwnerID : Edm.Int32 "Approver"
PX.Objects.RQ.RQRequisition.ShipDestType : Edm.String "Shipping Destination Type"
PX.Objects.RQ.RQRequisition.SiteIdErrorMessage : Edm.String
PX.Objects.RQ.RQRequisition.ShipToBAccountID : Edm.Int32 "Ship To"
PX.Objects.RQ.RQRequisition.ShipAddressID : Edm.Int32 "ShipAddressID"
PX.Objects.RQ.RQRequisition.ShipContactID : Edm.Int32 "ShipContactID"
PX.Objects.RQ.RQRequisition.FOBPoint : Edm.String "FOB Point"
PX.Objects.RQ.RQRequisition.ShipVia : Edm.String "Ship Via"
PX.Objects.RQ.RQRequisition.VendorID : Edm.Int32 "Vendor"
PX.Objects.RQ.RQRequisition.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.RQ.RQRequisition.VendorRequestSent : Edm.Boolean "Vendor Requests Sent"
PX.Objects.RQ.RQRequisition.SkipValidateWithVendorCuryOrRate : Edm.Boolean
PX.Objects.RQ.RQRequisition.TermsID : Edm.String "Terms"
PX.Objects.RQ.RQRequisition.RemitAddressID : Edm.Int32 "RemitAddressID"
PX.Objects.RQ.RQRequisition.RemitContactID : Edm.Int32
PX.Objects.RQ.RQRequisition.OpenOrderQty : Edm.Decimal "Open Quantity"
PX.Objects.RQ.RQRequisition.CuryID : Edm.String "Currency"
PX.Objects.RQ.RQRequisition.CuryInfoID : Edm.Int64
PX.Objects.RQ.RQRequisition.EstExtCostTotal : Edm.Decimal [required]
PX.Objects.RQ.RQRequisition.CuryEstExtCostTotal : Edm.Decimal [required] "Est. Ext. Cost"
PX.Objects.RQ.RQRequisition.POType : Edm.String "PO Type"
PX.Objects.RQ.RQRequisition.LineCntr : Edm.Int32 [required]
PX.Objects.RQ.RQRequisition.BiddingVendorCntr : Edm.Int32 [required]
PX.Objects.RQ.RQRequisition.tstamp : Edm.Binary
PX.Objects.RQ.RQRequisition.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQRequisition.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQRequisition.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.RQ.RQRequisition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQRequisition.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQRequisition.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.RQ.RQRequisition.CuryRate : Edm.Decimal
PX.Objects.RQ.RQRequisition.CuryViewState : Edm.Boolean
PX.Objects.RQ.RQRequisition.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.RQ.RQRequisition.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.RQ.RQRequisition.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.RQ.RQRequisition.BAccountByShipToBAccountID -> PX.Objects.CR.BAccount (ShipToBAccountID=BAccountID)
PX.Objects.RQ.RQRequisition.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.RQ.RQRequisition.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.RQ.RQRequisition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQRequisition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQRequisition.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.RQ.RQRequisition.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.RQ.RQRequisition.FOBPointByFOBPoint -> PX.Objects.CS.FOBPoint (FOBPoint=FOBPointID)
PX.Objects.RQ.RQRequisition.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.RQ.RQRequisition.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.RQ.RQRequisition.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.RQ.RQRequisition.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.RQ.RQRequisition.LocationByShipToBAccountID -> PX.Objects.CR.Location (ShipToBAccountID=BAccountID)
PX.Objects.RQ.RQRequisition.LocationByVendorID -> PX.Objects.CR.Location (VendorID=BAccountID)
PX.Objects.RQ.RQRequisition.LocationByCustomerLocationID -> PX.Objects.CR.Location
PX.Objects.RQ.RQRequisition.LocationByShipToLocationID -> PX.Objects.CR.Location
PX.Objects.RQ.RQRequisition.LocationByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.RQ.RQRequisition.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.RQ.RQRequisition.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.RQ.RQRequisition.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.RQ.RQRequisition.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)
PX.Objects.RQ.RQRequisition.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.Objects.RQ.RQRequisition.RQRequisitionContentCollection -> Collection(PX.Objects.RQ.RQRequisitionContent)
PX.Objects.RQ.RQRequisition.RQRequisitionOrderCollection -> Collection(PX.Objects.RQ.RQRequisitionOrder)

# PX.Objects.RQ.RQRequisitionContent (EntityType)

Key: LineNbr, OrderNbr, ReqLineNbr, ReqNbr
Entity sets: PX_Objects_RQ_RQRequisitionContent
Non-filterable, non-selectable: RecalcOnly

PX.Objects.RQ.RQRequisitionContent.ReqNbr : Edm.String [key] "Req. Nbr."
PX.Objects.RQ.RQRequisitionContent.ReqLineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.RQ.RQRequisitionContent.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.RQ.RQRequisitionContent.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.RQ.RQRequisitionContent.ItemQty : Edm.Decimal [required] "Qty."
PX.Objects.RQ.RQRequisitionContent.BaseItemQty : Edm.Decimal [required]
PX.Objects.RQ.RQRequisitionContent.ReqQty : Edm.Decimal [required] "Qty."
PX.Objects.RQ.RQRequisitionContent.BaseReqQty : Edm.Decimal [required]
PX.Objects.RQ.RQRequisitionContent.RecalcOnly : Edm.Boolean
PX.Objects.RQ.RQRequisitionContent.tstamp : Edm.Binary
PX.Objects.RQ.RQRequisitionContent.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQRequisitionContent.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQRequisitionContent.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQRequisitionContent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQRequisitionContent.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQRequisitionContent.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQRequisitionContent.RQRequisitionLineByReqLineNbr -> PX.Objects.RQ.RQRequisitionLine (ReqNbr=ReqNbr, ReqLineNbr=LineNbr)
PX.Objects.RQ.RQRequisitionContent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQRequisitionContent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQRequisitionContent.RQRequestLineByLineNbr -> PX.Objects.RQ.RQRequestLine (OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.RQ.RQRequisitionContent.RQRequisitionByReqNbr -> PX.Objects.RQ.RQRequisition (ReqNbr=ReqNbr)

# PX.Objects.RQ.RQRequisitionLine (EntityType)

Label: "Requisition Line"
Key: LineNbr, ReqNbr
Entity sets: PX_Objects_RQ_RQRequisitionLine, RequisitionLine, RQRequisitionLine
Non-filterable, non-selectable: LineSource, NoteText, Availability, CuryID, CuryRate, CuryViewState

PX.Objects.RQ.RQRequisitionLine.BranchID : Edm.Int32 "Branch"
PX.Objects.RQ.RQRequisitionLine.ReqNbr : Edm.String [key] "Req. Nbr."
PX.Objects.RQ.RQRequisitionLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.RQ.RQRequisitionLine.LineSource : Edm.String "Line Source"
PX.Objects.RQ.RQRequisitionLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.RQ.RQRequisitionLine.LineType : Edm.String "Line Type"
PX.Objects.RQ.RQRequisitionLine.Description : Edm.String "Description"
PX.Objects.RQ.RQRequisitionLine.UOM : Edm.String "UOM"
PX.Objects.RQ.RQRequisitionLine.AlternateID : Edm.String "Alternate ID"
PX.Objects.RQ.RQRequisitionLine.OrderQty : Edm.Decimal [required] "Order Qty."
PX.Objects.RQ.RQRequisitionLine.BaseOrderQty : Edm.Decimal [required]
PX.Objects.RQ.RQRequisitionLine.OriginQty : Edm.Decimal [required] "Original Qty."
PX.Objects.RQ.RQRequisitionLine.BaseOriginQty : Edm.Decimal [required]
PX.Objects.RQ.RQRequisitionLine.CuryInfoID : Edm.Int64
PX.Objects.RQ.RQRequisitionLine.CuryEstUnitCost : Edm.Decimal "Est. Unit Cost"
PX.Objects.RQ.RQRequisitionLine.EstUnitCost : Edm.Decimal
PX.Objects.RQ.RQRequisitionLine.CuryEstExtCost : Edm.Decimal "Est. Ext. Cost"
PX.Objects.RQ.RQRequisitionLine.EstExtCost : Edm.Decimal [required]
PX.Objects.RQ.RQRequisitionLine.ManualPrice : Edm.Boolean [required] "Manual Cost"
PX.Objects.RQ.RQRequisitionLine.NoteID : Edm.Guid
PX.Objects.RQ.RQRequisitionLine.NoteText : Edm.String "Note Text"
PX.Objects.RQ.RQRequisitionLine.RcptQtyMin : Edm.Decimal [required] "Min. Receipt, %"
PX.Objects.RQ.RQRequisitionLine.RcptQtyMax : Edm.Decimal [required] "Max. Receipt, %"
PX.Objects.RQ.RQRequisitionLine.RcptQtyThreshold : Edm.Decimal [required] "Complete On, %"
PX.Objects.RQ.RQRequisitionLine.RcptQtyAction : Edm.String "Receipt Action"
PX.Objects.RQ.RQRequisitionLine.IsUseMarkup : Edm.Boolean [required] "Use Markup"
PX.Objects.RQ.RQRequisitionLine.MarkupPct : Edm.Decimal [required] "Markup, %"
PX.Objects.RQ.RQRequisitionLine.RequestedDate : Edm.DateTimeOffset "Required Date"
PX.Objects.RQ.RQRequisitionLine.PromisedDate : Edm.DateTimeOffset "Promised Date"
PX.Objects.RQ.RQRequisitionLine.Approved : Edm.Boolean [required] "Approved"
PX.Objects.RQ.RQRequisitionLine.Cancelled : Edm.Boolean [required] "Canceled"
PX.Objects.RQ.RQRequisitionLine.TransferRequest : Edm.Boolean [required] "Transfer"
PX.Objects.RQ.RQRequisitionLine.TransferType : Edm.String "Transfer Type"
PX.Objects.RQ.RQRequisitionLine.SourceTranReqNbr : Edm.String "Source Transfer"
PX.Objects.RQ.RQRequisitionLine.SourceTranLineNbr : Edm.Int32 "Source Transfer Line"
PX.Objects.RQ.RQRequisitionLine.TransferQty : Edm.Decimal [required] "Transfer Qty."
PX.Objects.RQ.RQRequisitionLine.BaseTransferQty : Edm.Decimal [required]
PX.Objects.RQ.RQRequisitionLine.OpenQty : Edm.Decimal [required] "Open Qty."
PX.Objects.RQ.RQRequisitionLine.BaseOpenQty : Edm.Decimal
PX.Objects.RQ.RQRequisitionLine.BiddingQty : Edm.Decimal [required] "Bidding Qty."
PX.Objects.RQ.RQRequisitionLine.BaseBiddingQty : Edm.Decimal
PX.Objects.RQ.RQRequisitionLine.ByRequest : Edm.Boolean
PX.Objects.RQ.RQRequisitionLine.QTOrderNbr : Edm.String
PX.Objects.RQ.RQRequisitionLine.QTLineNbr : Edm.Int32
PX.Objects.RQ.RQRequisitionLine.Availability : Edm.String "Availability"
PX.Objects.RQ.RQRequisitionLine.tstamp : Edm.Binary
PX.Objects.RQ.RQRequisitionLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQRequisitionLine.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQRequisitionLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQRequisitionLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQRequisitionLine.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQRequisitionLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQRequisitionLine.CuryID : Edm.String "Currency"
PX.Objects.RQ.RQRequisitionLine.CuryRate : Edm.Decimal
PX.Objects.RQ.RQRequisitionLine.CuryViewState : Edm.Boolean
PX.Objects.RQ.RQRequisitionLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.RQ.RQRequisitionLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.RQ.RQRequisitionLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQRequisitionLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQRequisitionLine.RQRequisitionByReqNbr -> PX.Objects.RQ.RQRequisition (ReqNbr=ReqNbr)
PX.Objects.RQ.RQRequisitionLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.RQ.RQRequisitionLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.RQ.RQRequisitionLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.RQ.RQRequisitionLine.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.RQ.RQRequisitionLine.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.RQ.RQRequisitionLine.RQRequisitionContentCollection -> Collection(PX.Objects.RQ.RQRequisitionContent)
PX.Objects.RQ.RQRequisitionLine.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.RQ.RQRequisitionLine.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)

# PX.Objects.RQ.RQRequisitionLineBidding (EntityType)

Key: LineNbr, ReqNbr
Entity sets: PX_Objects_RQ_RQRequisitionLineBidding
Non-filterable, non-selectable: QuoteNumber, QuoteQty, CuryQuoteUnitCost, QuoteUnitCost, CuryQuoteExtCost, QuoteExtCost, MinQty

PX.Objects.RQ.RQRequisitionLineBidding.ReqNbr : Edm.String [key]
PX.Objects.RQ.RQRequisitionLineBidding.LineNbr : Edm.Int32 [key]
PX.Objects.RQ.RQRequisitionLineBidding.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.RQ.RQRequisitionLineBidding.Description : Edm.String "Description"
PX.Objects.RQ.RQRequisitionLineBidding.AlternateID : Edm.String "Alternate ID"
PX.Objects.RQ.RQRequisitionLineBidding.CuryInfoID : Edm.Int64
PX.Objects.RQ.RQRequisitionLineBidding.UOM : Edm.String "UOM"
PX.Objects.RQ.RQRequisitionLineBidding.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.RQ.RQRequisitionLineBidding.BaseOrderQty : Edm.Decimal
PX.Objects.RQ.RQRequisitionLineBidding.QuoteNumber : Edm.String "Bid Number"
PX.Objects.RQ.RQRequisitionLineBidding.QuoteQty : Edm.Decimal "Bid Qty."
PX.Objects.RQ.RQRequisitionLineBidding.CuryQuoteUnitCost : Edm.Decimal "Bid Unit Cost"
PX.Objects.RQ.RQRequisitionLineBidding.QuoteUnitCost : Edm.Decimal
PX.Objects.RQ.RQRequisitionLineBidding.CuryQuoteExtCost : Edm.Decimal "Bid Extended Cost"
PX.Objects.RQ.RQRequisitionLineBidding.QuoteExtCost : Edm.Decimal
PX.Objects.RQ.RQRequisitionLineBidding.MinQty : Edm.Decimal "Min. Qty."
PX.Objects.RQ.RQRequisitionLineBidding.RQRequisitionByReqNbr -> PX.Objects.RQ.RQRequisition (ReqNbr=ReqNbr)
PX.Objects.RQ.RQRequisitionLineBidding.RQRequisitionContentCollection -> Collection(PX.Objects.RQ.RQRequisitionContent)
PX.Objects.RQ.RQRequisitionLineBidding.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.RQ.RQRequisitionLineBidding.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)

# PX.Objects.RQ.RQRequisitionLineReceived (EntityType)

Label: "Requisition Line"
BaseType: PX.Objects.RQ.RQRequisitionLine
Key: LineNbr, ReqNbr (inherited from PX.Objects.RQ.RQRequisitionLine)
Entity sets: PX_Objects_RQ_RQRequisitionLineReceived
Non-filterable, non-selectable: Status

PX.Objects.RQ.RQRequisitionLineReceived.POOrderQty : Edm.Decimal "Ordered Qty."
PX.Objects.RQ.RQRequisitionLineReceived.POReceivedQty : Edm.Decimal "Received Qty."
PX.Objects.RQ.RQRequisitionLineReceived.Status : Edm.String "Status"

# PX.Objects.RQ.RQRequisitionOrder (EntityType)

Key: OrderCategory, OrderNbr, OrderType, ReqNbr
Entity sets: PX_Objects_RQ_RQRequisitionOrder

PX.Objects.RQ.RQRequisitionOrder.ReqNbr : Edm.String [key]
PX.Objects.RQ.RQRequisitionOrder.OrderCategory : Edm.String [key]
PX.Objects.RQ.RQRequisitionOrder.OrderType : Edm.String [key]
PX.Objects.RQ.RQRequisitionOrder.OrderNbr : Edm.String [key]
PX.Objects.RQ.RQRequisitionOrder.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.RQ.RQRequisitionOrder.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.RQ.RQRequisitionOrder.RQRequisitionByReqNbr -> PX.Objects.RQ.RQRequisition (ReqNbr=ReqNbr)

# PX.Objects.RQ.RQSetup (EntityType)

Label: "Requisition Preferences"
Singletons: PX_Objects_RQ_RQSetup, RequisitionPreferences, RQSetup

PX.Objects.RQ.RQSetup.RequestNumberingID : Edm.String "Numbering Sequence"
PX.Objects.RQ.RQSetup.RequestApproval : Edm.Boolean [required] "Require Approval"
PX.Objects.RQ.RQSetup.RequestAssignmentMapID : Edm.Int32 "Assignment Map"
PX.Objects.RQ.RQSetup.RequestOverBudgetWarning : Edm.String "Over Budget Warning"
PX.Objects.RQ.RQSetup.MonthRetainRequest : Edm.Int32 [required] "Months Retained"
PX.Objects.RQ.RQSetup.RequisitionNumberingID : Edm.String "Numbering Sequence"
PX.Objects.RQ.RQSetup.RequisitionApproval : Edm.Boolean [required] "Require Approval"
PX.Objects.RQ.RQSetup.RequisitionAssignmentMapID : Edm.Int32 "Assignment Map"
PX.Objects.RQ.RQSetup.RequisitionOverBudgetWarning : Edm.String "Over Budget Warning"
PX.Objects.RQ.RQSetup.RequisitionMergeLines : Edm.Boolean [required] "Merge Lines by Default"
PX.Objects.RQ.RQSetup.MonthRetainRequisition : Edm.Int32 [required] "Months Retained"
PX.Objects.RQ.RQSetup.POHold : Edm.Boolean [required] "Create Purchase Order on Hold"
PX.Objects.RQ.RQSetup.ShowBudgetLedgers : Edm.Boolean "ShowBudgetLedgers"
PX.Objects.RQ.RQSetup.BudgetCalculation : Edm.String "Budget Calculation"
PX.Objects.RQ.RQSetup.ValidateBy : Edm.String "Validate By"
PX.Objects.RQ.RQSetup.DefaultReqClassID : Edm.String "Default Request Class"
PX.Objects.RQ.RQSetup.SOOrderType : Edm.String "Default Type of Requisition Sales"
PX.Objects.RQ.RQSetup.QTOrderType : Edm.String "Default Type of Requisition Quote"
PX.Objects.RQ.RQSetup.tstamp : Edm.Binary
PX.Objects.RQ.RQSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQSetup.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQSetup.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQSetup.SOOrderTypeBySoOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.RQ.RQSetup.SOOrderTypeByQtOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.RQ.RQSetup.RQRequestClassByDefaultReqClassID -> PX.Objects.RQ.RQRequestClass (DefaultReqClassID=ReqClassID)
PX.Objects.RQ.RQSetup.NumberingByRequestNumberingID -> PX.Objects.CS.Numbering (RequestNumberingID=NumberingID)
PX.Objects.RQ.RQSetup.NumberingByRequisitionNumberingID -> PX.Objects.CS.Numbering (RequisitionNumberingID=NumberingID)
PX.Objects.RQ.RQSetup.EPAssignmentMapByRequestAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (RequestAssignmentMapID=AssignmentMapID)
PX.Objects.RQ.RQSetup.EPAssignmentMapByRequisitionAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (RequisitionAssignmentMapID=AssignmentMapID)

# PX.Objects.RQ.RQSetupApproval (EntityType)

Key: ApprovalID
Entity sets: PX_Objects_RQ_RQSetupApproval

PX.Objects.RQ.RQSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.RQ.RQSetupApproval.Type : Edm.String "Type"
PX.Objects.RQ.RQSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.RQ.RQSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.RQ.RQSetupApproval.tstamp : Edm.Binary
PX.Objects.RQ.RQSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.RQ.RQSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.RQ.RQSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.RQ.RQSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.RQ.RQSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.RQ.RQSetupApproval.IsActive : Edm.Boolean
PX.Objects.RQ.RQSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.RQ.RQSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.RQ.RQSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.RQ.RQSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.RQ.RQSiteStatusSelected (EntityType)

Key: InventoryID
Entity sets: PX_Objects_RQ_RQSiteStatusSelected
Non-filterable, non-selectable: QtySelected, Rank

PX.Objects.RQ.RQSiteStatusSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.RQ.RQSiteStatusSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.RQ.RQSiteStatusSelected.Descr : Edm.String "Description"
PX.Objects.RQ.RQSiteStatusSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.RQ.RQSiteStatusSelected.ItemClassCD : Edm.String
PX.Objects.RQ.RQSiteStatusSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.RQ.RQSiteStatusSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.RQ.RQSiteStatusSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.RQ.RQSiteStatusSelected.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.RQ.RQSiteStatusSelected.PreferredVendorDescription : Edm.String "Preferred Vendor Name"
PX.Objects.RQ.RQSiteStatusSelected.BarCode : Edm.String
PX.Objects.RQ.RQSiteStatusSelected.SiteCD : Edm.String
PX.Objects.RQ.RQSiteStatusSelected.SubItemCD : Edm.String
PX.Objects.RQ.RQSiteStatusSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.RQ.RQSiteStatusSelected.PurchaseUnit : Edm.String "Purchase Unit"
PX.Objects.RQ.RQSiteStatusSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.RQ.RQSiteStatusSelected.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.RQ.RQSiteStatusSelected.QtyOnHandExt : Edm.Decimal "Qty. On Hand"
PX.Objects.RQ.RQSiteStatusSelected.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.RQ.RQSiteStatusSelected.QtyAvailExt : Edm.Decimal "Qty. Available"
PX.Objects.RQ.RQSiteStatusSelected.QtyPOPrepared : Edm.Decimal "Qty. PO Prepared"
PX.Objects.RQ.RQSiteStatusSelected.QtyPOPreparedExt : Edm.Decimal "Qty. PO Prepared"
PX.Objects.RQ.RQSiteStatusSelected.QtyPOOrders : Edm.Decimal "Qty. PO Orders"
PX.Objects.RQ.RQSiteStatusSelected.QtyPOOrdersExt : Edm.Decimal "Qty. PO Orders"
PX.Objects.RQ.RQSiteStatusSelected.QtyPOReceipts : Edm.Decimal "Qty. PO Receipts"
PX.Objects.RQ.RQSiteStatusSelected.QtyPOReceiptsExt : Edm.Decimal "Qty. PO Receipts"
PX.Objects.RQ.RQSiteStatusSelected.NoteID : Edm.Guid
PX.Objects.RQ.RQSiteStatusSelected.Rank : Edm.Int32
PX.Objects.RQ.RQSiteStatusSelected.CombinedSearchString : Edm.String
PX.Objects.RQ.RQSiteStatusSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.RQ.RQSiteStatusSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.RQ.RQSiteStatusSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.RQ.RQSiteStatusSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice (EntityType)

Label: "AR Transactions"
Key: LineNbr, RefNbr, TranType
Entity sets: PX_Objects_SO_DAC_Projections_ARTranForDirectInvoice, ARTransactions2, ARTranForDirectInvoice

PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.TranType : Edm.String [key] "Doc. Type"
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.LineType : Edm.String "Line Type"
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.CustomerID : Edm.Int32 "Customer"
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.TranDate : Edm.DateTimeOffset "Doc. Date"
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.UOM : Edm.String "UOM"
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.Qty : Edm.Decimal "Qty"
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.CuryUnitPrice : Edm.Decimal "Unit Price"
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.Released : Edm.Boolean
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.SubItemID : Edm.Int32
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.SiteID : Edm.Int32
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.LocationID : Edm.Int32
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.LotSerialNbr : Edm.String
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.ExpireDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.DRScheduleByTranType -> PX.Objects.DR.DRSchedule (TranType=DocType)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.INLocationBySiteID -> PX.Objects.IN.INLocation (LocationID=LocationID, SiteID=SiteID)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.SOInvoiceByOrigInvoiceType -> PX.Objects.SO.SOInvoice
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.SO.DAC.Projections.ARTranForDirectInvoice.ARFinChargeTranCollection -> Collection(PX.Objects.AR.ARFinChargeTran)

# PX.Objects.SO.DAC.Projections.BlanketSOAdjust (EntityType)

Label: "Blanket SO Adjustment"
Key: AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr, RecordID
Entity sets: PX_Objects_SO_DAC_Projections_BlanketSOAdjust, BlanketSOAdjustment, BlanketSOAdjust

PX.Objects.SO.DAC.Projections.BlanketSOAdjust.RecordID : Edm.Int32 [key]
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.AdjgDocType : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.AdjgRefNbr : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.AdjdOrderType : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.AdjdOrderNbr : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.CuryAdjgAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.AdjAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.CuryAdjdAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.CuryAdjdBilledAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.IsCCPayment : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.PaymentReleased : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.IsCCAuthorized : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.IsCCCaptured : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.Voided : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.CuryAdjgTransferredToChildrenAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.AdjTransferredToChildrenAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.CuryAdjdTransferredToChildrenAmt : Edm.Decimal "Transferred to Child Orders"
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.CuryAdjdOrigBlanketAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.AdjOrigBlanketAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.CuryAdjgOrigBlanketAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.tstamp : Edm.Binary
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.ARPaymentTotalsByAdjgRefNbr -> PX.Objects.AR.ARPaymentTotals (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.BlanketSOOrderByAdjdOrderNbr -> PX.Objects.SO.DAC.Projections.BlanketSOOrder (AdjdOrderType=OrderType, AdjdOrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.ARInvoiceByAdjgRefNbr -> PX.Objects.AR.ARInvoice (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.ARPaymentByAdjgRefNbr -> PX.Objects.AR.ARPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.SOOrderByAdjdOrderNbr -> PX.Objects.SO.SOOrder (AdjdOrderType=OrderType, AdjdOrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.SOOrderByAdjgRefNbr -> PX.Objects.SO.SOOrder (AdjgDocType=OrderType, AdjgRefNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.SOOrderByCustomerID -> PX.Objects.SO.SOOrder (AdjdOrderNbr=OrderNbr, AdjdOrderType=OrderType)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.SOOrderTypeByAdjdOrderType -> PX.Objects.SO.SOOrderType (AdjdOrderType=OrderType)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.SO.DAC.Projections.BlanketSOAdjust.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)

# PX.Objects.SO.DAC.Projections.BlanketSOLine (EntityType)

Label: "Blanket SO Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_DAC_Projections_BlanketSOLine, BlanketSOLine
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.SO.DAC.Projections.BlanketSOLine.BranchID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.OrderType : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOLine.OrderNbr : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOLine.LineNbr : Edm.Int32 [key]
PX.Objects.SO.DAC.Projections.BlanketSOLine.Behavior : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.Operation : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.LineSign : Edm.Int16
PX.Objects.SO.DAC.Projections.BlanketSOLine.IsStockItem : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.InventoryID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.SubItemID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.SiteID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.TranDesc : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.UOM : Edm.String "UOM"
PX.Objects.SO.DAC.Projections.BlanketSOLine.OrderQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BaseOrderQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.RequestDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOLine.TaxCategoryID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.ProjectID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.TaskID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.CostCodeID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.ShipComplete : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryInfoID : Edm.Int64
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryUnitPrice : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.UnitPrice : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryExtPrice : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.ExtPrice : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.DiscPct : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryDiscAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.DiscAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.IsFree : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.ManualDisc : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.SkipLineDiscounts : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.AutomaticDiscountsDisabled : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.DiscountID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.LineType : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.Completed : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryLineAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.LineAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.GroupDiscountRate : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.DocumentDiscountRate : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.SalesPersonID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.SalesAcctID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.SalesSubID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.POCreate : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.POSource : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.POCreated : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.VendorID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.QtyOnOrders : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BaseQtyOnOrders : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.CustomerOrderNbr : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.SchedOrderDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOLine.SchedShipDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOLine.TaxZoneID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.CustomerID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.CustomerLocationID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.ShipVia : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.FOBPoint : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.ShipTermsID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.ShipZoneID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.BlanketOpenQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.ChildLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.OpenChildLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLine.OpenLine : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.ShippedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BaseShippedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.ClosedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BaseClosedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.OpenQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BaseOpenQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryOpenAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.OpenAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.OrigCuryOpenAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BilledQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BaseBilledQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.UnbilledQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BaseUnbilledQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryBilledAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.BilledAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryUnbilledAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.UnbilledAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.NoteID : Edm.Guid
PX.Objects.SO.DAC.Projections.BlanketSOLine.tstamp : Edm.Binary
PX.Objects.SO.DAC.Projections.BlanketSOLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.DAC.Projections.BlanketSOLine.LastModifiedByScreenID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryID : Edm.String "Currency"
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryRate : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLine.CuryViewState : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLine.BlanketSOOrderSiteBySiteID -> PX.Objects.SO.DAC.Projections.BlanketSOOrderSite (OrderType=OrderType, OrderNbr=OrderNbr, SiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.BlanketSOOrderByOrderNbr -> PX.Objects.SO.DAC.Projections.BlanketSOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOOrderSiteBySiteID -> PX.Objects.SO.SOOrderSite (OrderType=OrderType, OrderNbr=OrderNbr, SiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOSalesPerTranBySalesPersonID -> PX.Objects.SO.SOSalesPerTran (OrderType=OrderType, OrderNbr=OrderNbr, SalesPersonID=SalespersonID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.FOBPointByFOBPoint -> PX.Objects.CS.FOBPoint (FOBPoint=FOBPointID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.INSiteByPOSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.DAC.Projections.BlanketSOLine.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.AccountBySalesAcctID -> PX.Objects.GL.Account (SalesAcctID=AccountID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SubBySalesSubID -> PX.Objects.GL.Sub (SalesSubID=SubID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerLocationID=LocationID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.DAC.Projections.BlanketSOLine.BlanketSOLineSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOLineSplit)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.DAC.Projections.BlanketSOLine.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.DAC.Projections.BlanketSOLine.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.DAC.Projections.BlanketSOLine.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.DAC.Projections.BlanketSOLine.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.DAC.Projections.BlanketSOLine.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.SO.DAC.Projections.BlanketSOLine.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.DAC.Projections.BlanketSOLine.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.DAC.Projections.BlanketSOLine.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.DAC.Projections.BlanketSOLine.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.DAC.Projections.BlanketSOLine.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.DAC.Projections.BlanketSOLine.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.DAC.Projections.BlanketSOLine.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.SO.DAC.Projections.BlanketSOLineSplit (EntityType)

Label: "Blanket SO Line Split"
Key: LineNbr, OrderNbr, OrderType, SplitLineNbr
Entity sets: PX_Objects_SO_DAC_Projections_BlanketSOLineSplit, BlanketSOLineSplit
Non-filterable, non-selectable: BaseUnreceivedQty

PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.OrderType : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.OrderNbr : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.LineNbr : Edm.Int32 [key]
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SplitLineNbr : Edm.Int32 [key]
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.InventoryID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.LineType : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SiteID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.LocationID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SubItemID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.UOM : Edm.String "UOM"
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.Qty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BaseQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.ToSiteID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.LotSerialNbr : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.IsAllocated : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POCreate : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POType : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.PONbr : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POLineNbr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POReceiptType : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POReceiptNbr : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.RefNoteID : Edm.Guid
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POCompleted : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POCancelled : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POSource : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.VendorID : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.Completed : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.PlanID : Edm.Int64
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.QtyOnOrders : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BaseQtyOnOrders : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.CustomerOrderNbr : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SchedOrderDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SchedShipDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BlanketOpenQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.ChildLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.EffectiveChildLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.OpenChildLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.ShippedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BaseShippedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.ClosedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BaseClosedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.ReceivedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BaseReceivedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BaseUnreceivedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.tstamp : Edm.Binary
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.LastModifiedByScreenID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BlanketSOLineByLineNbr -> PX.Objects.SO.DAC.Projections.BlanketSOLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.BlanketSOOrderByOrderNbr -> PX.Objects.SO.DAC.Projections.BlanketSOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SOLineByLineNbr -> PX.Objects.SO.SOLine (OrderType=OrderType, OrderNbr=OrderNbr, LineNbr=LineNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SOLineSplitBySplitLineNbr -> PX.Objects.SO.SOLineSplit (SplitLineNbr=ParentSplitLineNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INLocationByLocationID -> PX.Objects.IN.INLocation (LocationID=LocationID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation (LocationID=LocationID, SiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INSiteByToSiteID -> PX.Objects.IN.INSite (ToSiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SupplyPOLineByPOLineNbr -> PX.Objects.SO.SupplyPOLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID, LocationID=LocationID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID, LocationID=LocationID, LotSerialNbr=LotSerialNbr)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID, SubItemID=SubItemID, SiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INSiteStatusByToSiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID, SubItemID=SubItemID, ToSiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.DAC.Projections.BlanketSOLineSplit.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)

# PX.Objects.SO.DAC.Projections.BlanketSOOrder (EntityType)

Label: "Blanket Sales Order"
Key: OrderNbr, OrderType
Entity sets: PX_Objects_SO_DAC_Projections_BlanketSOOrder, BlanketSalesOrder, BlanketSOOrder
Non-filterable, non-selectable: ShipmentCntrUpdated, CuryRate, CuryViewState

PX.Objects.SO.DAC.Projections.BlanketSOOrder.OrderType : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OrderNbr : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOOrder.Hold : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.Approved : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.Completed : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenDoc : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryID : Edm.String "Currency"
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryInfoID : Edm.Int64
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OrderDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOOrder.TaxCalcMode : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryFreightTot : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.FreightTot : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.FreightTaxCategoryID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ExpireDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOOrder.IsExpired : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.QtyOnOrders : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.BlanketOpenQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryOpenOrderTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenOrderTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryOpenLineTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenLineTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryOpenDiscTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenDiscTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryOpenTaxTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenTaxTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryOpenInclTaxTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenInclTaxTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenOrderQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnbilledOrderQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryUnbilledMiscTot : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnbilledMiscTot : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryUnbilledDiscTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnbilledDiscTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryUnbilledFreightTot : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnbilledFreightTot : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryUnbilledOrderTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnbilledOrderTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryUnbilledLineTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnbilledLineTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryUnbilledTaxTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnbilledTaxTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryUnbilledInclTaxTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnbilledInclTaxTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.MinSchedOrderDate : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryDiscTot : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.DiscTot : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.BilledCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ReleasedCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OpenSiteCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OrigOpenLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryUnreleasedPaymentAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.UnreleasedPaymentAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryCCAuthorizedAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CCAuthorizedAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryPaidAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.PaidAmt : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryPaymentTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.IsOpenTaxValid : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.OrderTaxAllocated : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.PaymentTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryPaymentOverall : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.PaymentOverall : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryTransferredToChildrenPaymentTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.TransferredToChildrenPaymentTotal : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ShipmentCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ShipmentCntrUpdated : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ChildLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOOrder.NoteID : Edm.Guid
PX.Objects.SO.DAC.Projections.BlanketSOOrder.tstamp : Edm.Binary
PX.Objects.SO.DAC.Projections.BlanketSOOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.DAC.Projections.BlanketSOOrder.LastModifiedByScreenID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOOrder.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryRate : Edm.Decimal
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CuryViewState : Edm.Boolean
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.TaxCategoryByFreightTaxCategoryID -> PX.Objects.TX.TaxCategory (FreightTaxCategoryID=TaxCategoryID)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOOrderTypeByOrigOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.BlanketSOOrderSiteCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOOrderSite)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.BlanketSOLineSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOLineSplit)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.BlanketSOAdjustCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOAdjust)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.BlanketSOLineCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOBlanketOrderLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderLink)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.AMFixedDemandCollection -> Collection(PX.Objects.AM.AMFixedDemand)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.CCPayLinkCollection -> Collection(PX.Objects.CC.CCPayLink)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOOrderSiteCollection -> Collection(PX.Objects.SO.SOOrderSite)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.POReceiptToShipmentLinkCollection -> Collection(PX.Objects.PO.POReceiptToShipmentLink)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOOrderCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.SOOrderCarrierData)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SchedulerProductionOrderCollection -> Collection(PX.Objects.AM.SchedulerProductionOrder)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.DropShipSOLineCollection -> Collection(PX.Objects.SO.DropShipSOLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.RQRequisitionOrderCollection -> Collection(PX.Objects.RQ.RQRequisitionOrder)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.DropShipPOLineCollection -> Collection(PX.Objects.PO.DropShipPOLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SalesAllocationCollection -> Collection(PX.Objects.SO.SalesAllocation)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOLine2Collection -> Collection(PX.Objects.SO.SOLine2)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOLine4Collection -> Collection(PX.Objects.SO.SOLine4)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOMiscLine2Collection -> Collection(PX.Objects.SO.SOMiscLine2)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.IntercompanyReturnedGoodsInTransitResultCollection -> Collection(PX.Objects.IN.IntercompanyReturnedGoodsInTransitResult)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SOOrderRisksCollection -> Collection(PX.Commerce.Objects.SOOrderRisks)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.AMConfigurationKeysCollection -> Collection(PX.Objects.AM.AMConfigurationKeys)
PX.Objects.SO.DAC.Projections.BlanketSOOrder.SchedulerMachineOperationCollection -> Collection(PX.Objects.AM.SchedulerMachineOperation)

# PX.Objects.SO.DAC.Projections.BlanketSOOrderSite (EntityType)

Label: "Blanket SO Order Site"
Key: OrderNbr, OrderType, SiteID
Entity sets: PX_Objects_SO_DAC_Projections_BlanketSOOrderSite, BlanketSOOrderSite

PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.OrderType : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.OrderNbr : Edm.String [key]
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.SiteID : Edm.Int32 [key]
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.OpenLineCntr : Edm.Int32
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.LastModifiedByScreenID : Edm.String
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.tstamp : Edm.Binary
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.BlanketSOOrderByOrderNbr -> PX.Objects.SO.DAC.Projections.BlanketSOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.BlanketSOLineCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.DAC.Projections.BlanketSOOrderSite.SOLine4Collection -> Collection(PX.Objects.SO.SOLine4)

# PX.Objects.SO.DAC.Projections.InvoiceSplit (EntityType)

Label: "Invoice Split"
Key: ARDocType, ARLineNbr, ARRefNbr, INDocType, INLineNbr, INRefNbr, INSplitLineNbr
Entity sets: PX_Objects_SO_DAC_Projections_InvoiceSplit, InvoiceSplit
Non-filterable, non-selectable: QtyAvailForReturn, QtyReturned, QtyToReturn, SerialIsOnHand, SerialIsAlreadyReceived, SerialIsAlreadyReceivedRef, AutoCreateIssueLine

PX.Objects.SO.DAC.Projections.InvoiceSplit.ARDocType : Edm.String [key] "AR Doc. Type"
PX.Objects.SO.DAC.Projections.InvoiceSplit.ARRefNbr : Edm.String [key] "AR Doc. Nbr."
PX.Objects.SO.DAC.Projections.InvoiceSplit.ARLineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.DAC.Projections.InvoiceSplit.ARLineType : Edm.String
PX.Objects.SO.DAC.Projections.InvoiceSplit.ARTranDate : Edm.DateTimeOffset "AR Doc. Date"
PX.Objects.SO.DAC.Projections.InvoiceSplit.CustomerID : Edm.Int32 "Customer"
PX.Objects.SO.DAC.Projections.InvoiceSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.DAC.Projections.InvoiceSplit.DropShip : Edm.Boolean "Drop Ship"
PX.Objects.SO.DAC.Projections.InvoiceSplit.SOOrderType : Edm.String "Order Type"
PX.Objects.SO.DAC.Projections.InvoiceSplit.SOOrderNbr : Edm.String "Order Nbr."
PX.Objects.SO.DAC.Projections.InvoiceSplit.SOLineNbr : Edm.Int32 "Line Nbr."
PX.Objects.SO.DAC.Projections.InvoiceSplit.SOLineType : Edm.String
PX.Objects.SO.DAC.Projections.InvoiceSplit.SOOrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.SO.DAC.Projections.InvoiceSplit.SalesPersonID : Edm.Int32
PX.Objects.SO.DAC.Projections.InvoiceSplit.INDocType : Edm.String [key]
PX.Objects.SO.DAC.Projections.InvoiceSplit.INRefNbr : Edm.String [key]
PX.Objects.SO.DAC.Projections.InvoiceSplit.INLineNbr : Edm.Int32 [key]
PX.Objects.SO.DAC.Projections.InvoiceSplit.INSplitLineNbr : Edm.Int32 [key]
PX.Objects.SO.DAC.Projections.InvoiceSplit.TranDesc : Edm.String "Line Description"
PX.Objects.SO.DAC.Projections.InvoiceSplit.ComponentID : Edm.Int32 "Component ID"
PX.Objects.SO.DAC.Projections.InvoiceSplit.ComponentDesc : Edm.String "Component Description"
PX.Objects.SO.DAC.Projections.InvoiceSplit.UOM : Edm.String "UOM"
PX.Objects.SO.DAC.Projections.InvoiceSplit.Qty : Edm.Decimal "Original Qty."
PX.Objects.SO.DAC.Projections.InvoiceSplit.BaseQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.InvoiceSplit.QtyAvailForReturn : Edm.Decimal "Available for Return"
PX.Objects.SO.DAC.Projections.InvoiceSplit.QtyReturned : Edm.Decimal "Qty. Returned"
PX.Objects.SO.DAC.Projections.InvoiceSplit.QtyToReturn : Edm.Decimal "Qty. to Return"
PX.Objects.SO.DAC.Projections.InvoiceSplit.SerialIsOnHand : Edm.Boolean
PX.Objects.SO.DAC.Projections.InvoiceSplit.SerialIsAlreadyReceived : Edm.Boolean
PX.Objects.SO.DAC.Projections.InvoiceSplit.SerialIsAlreadyReceivedRef : Edm.String
PX.Objects.SO.DAC.Projections.InvoiceSplit.ARTranQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.InvoiceSplit.ARTranUOM : Edm.String "UOM"
PX.Objects.SO.DAC.Projections.InvoiceSplit.ARTranDrCr : Edm.String
PX.Objects.SO.DAC.Projections.InvoiceSplit.INTranQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.InvoiceSplit.INTranUOM : Edm.String "UOM"
PX.Objects.SO.DAC.Projections.InvoiceSplit.IsKit : Edm.Boolean
PX.Objects.SO.DAC.Projections.InvoiceSplit.AutoCreateIssueLine : Edm.Boolean
PX.Objects.SO.DAC.Projections.InvoiceSplit.ARInvoiceByARDocType -> PX.Objects.AR.ARInvoice (ARRefNbr=RefNbr, ARDocType=DocType)
PX.Objects.SO.DAC.Projections.InvoiceSplit.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.SO.DAC.Projections.InvoiceSplit.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.SO.DAC.Projections.InvoiceSplit.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.SO.DAC.Projections.InvoiceSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.DAC.Projections.InvoiceSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.DAC.Projections.InvoiceSplit.INUnitByUOM -> PX.Objects.IN.INUnit (UOM=FromUnit)
PX.Objects.SO.DAC.Projections.InvoiceSplit.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)

# PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice (EntityType)

Label: "Sales Order Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_DAC_Projections_SOLineForDirectInvoice, SalesOrderLine, SOLineForDirectInvoice

PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.CustomerID : Edm.Int32 "Customer"
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.Operation : Edm.String "Operation"
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.ShipDate : Edm.DateTimeOffset "Ship On"
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.UOM : Edm.String "UOM"
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.BaseOrderQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.ShippedQty : Edm.Decimal "Qty. on Shipments"
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.BaseShippedQty : Edm.Decimal
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.Completed : Edm.Boolean "Completed"
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.DAC.Projections.SOLineForDirectInvoice.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult (EntityType)

Label: "Credit Card Processing for Sales Result"
BaseType: PX.Objects.AR.ARPayment
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_SO_DAC_Unbound_SOPaymentProcessResult, CreditCardProcessingforSalesResult, SOPaymentProcessResult
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.CuryIncreasedAuthorizedAmount : Edm.Decimal "Increased Authorized Amount"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.IncreasedAuthorizedAmount : Edm.Decimal
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.CuryIncreasedAppliedAmount : Edm.Decimal "Increased Applied Amount"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.IncreasedAppliedAmount : Edm.Decimal
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.FundHoldExpDate : Edm.DateTimeOffset "Funds Hold Expiration Date"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedTranProcessingStatus : Edm.String "Proc. Status"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocument : Edm.String "Document Type"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentType : Edm.String "Document Type"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentNumber : Edm.String "Document Number"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentStatus : Edm.String "Document Status"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentCuryInfoID : Edm.Int64
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentCuryID : Edm.String
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentAppliedAmount : Edm.Decimal
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.CuryRelatedDocumentAppliedAmount : Edm.Decimal "Applied Amount"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentUnpaidAmount : Edm.Decimal
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.CuryRelatedDocumentUnpaidAmount : Edm.Decimal
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentCreditTerms : Edm.String "Credit Terms"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.ErrorDescription : Edm.String "Error Description"
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.RelatedDocumentPaymentCntr : Edm.Int32
PX.Objects.SO.DAC.Unbound.SOPaymentProcessResult.CuryViewState : Edm.Boolean

# PX.Objects.SO.DropShipSOLine (EntityType)

Label: "SO Drop-Ship Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_DropShipSOLine, SODropShipLine, DropShipSOLine

PX.Objects.SO.DropShipSOLine.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.DropShipSOLine.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.DropShipSOLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.DropShipSOLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.DropShipSOLine.TranDesc : Edm.String "Description"
PX.Objects.SO.DropShipSOLine.Operation : Edm.String
PX.Objects.SO.DropShipSOLine.OrderQty : Edm.Decimal "Not Linked Qty."
PX.Objects.SO.DropShipSOLine.UOM : Edm.String "UOM"
PX.Objects.SO.DropShipSOLine.IsLegacyDropShip : Edm.Boolean
PX.Objects.SO.DropShipSOLine.NoteID : Edm.Guid
PX.Objects.SO.DropShipSOLine.POOrderType : Edm.String
PX.Objects.SO.DropShipSOLine.POOrderNbr : Edm.String "Drop-Ship PO Nbr."
PX.Objects.SO.DropShipSOLine.POLineNbr : Edm.Int32 "Drop-Ship PO Line Nbr."
PX.Objects.SO.DropShipSOLine.POLinkActive : Edm.Boolean "PO Linked"
PX.Objects.SO.DropShipSOLine.POOrderByPOOrderType -> PX.Objects.PO.POOrder (POOrderNbr=OrderNbr, POOrderType=OrderType)
PX.Objects.SO.DropShipSOLine.SOOrderByOrderType -> PX.Objects.SO.SOOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.SO.DropShipSOLine.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.DropShipSOLine.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.DropShipSOLine.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.DropShipSOLine.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.DropShipSOLine.POLineByPOLineNbr -> PX.Objects.PO.POLine (POOrderType=OrderType, POOrderNbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.SO.DropShipSOLine.POOrderByPOOrderNbr -> PX.Objects.PO.POOrder (POOrderType=OrderType, POOrderNbr=OrderNbr)
PX.Objects.SO.DropShipSOLine.SupplyPOLineByPOLineNbr -> PX.Objects.SO.SupplyPOLine (POOrderType=OrderType, POOrderNbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.SO.DropShipSOLine.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.DropShipSOLine.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.DropShipSOLine.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.DropShipSOLine.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.DropShipSOLine.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.DropShipSOLine.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.DropShipSOLine.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.DropShipSOLine.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.DropShipSOLine.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.SO.DropShipSOLine.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.DropShipSOLine.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.DropShipSOLine.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.DropShipSOLine.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.DropShipSOLine.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.DropShipSOLine.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.DropShipSOLine.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)

# PX.Objects.SO.LocationOverrideEntry (ComplexType)


PX.Objects.SO.LocationOverrideEntry.DocType : Edm.String
PX.Objects.SO.LocationOverrideEntry.DocumentNbr : Edm.String
PX.Objects.SO.LocationOverrideEntry.ShipmentNbr : Edm.String
PX.Objects.SO.LocationOverrideEntry.WorksheetNbr : Edm.String
PX.Objects.SO.LocationOverrideEntry.SiteID : Edm.Int32
PX.Objects.SO.LocationOverrideEntry.CustomerID : Edm.Int32
PX.Objects.SO.LocationOverrideEntry.PickerID : Edm.Guid
PX.Objects.SO.LocationOverrideEntry.Date : Edm.DateTimeOffset
PX.Objects.SO.LocationOverrideEntry.InventoryID : Edm.Int32
PX.Objects.SO.LocationOverrideEntry.InitialLocationID : Edm.Int32
PX.Objects.SO.LocationOverrideEntry.CurrentLocationID : Edm.Int32
PX.Objects.SO.LocationOverrideEntry.InitialLotSerialNbr : Edm.String
PX.Objects.SO.LocationOverrideEntry.CurrentLotSerialNbr : Edm.String
PX.Objects.SO.LocationOverrideEntry.BaseQty : Edm.Decimal
PX.Objects.SO.LocationOverrideEntry.UOM : Edm.String

# PX.Objects.SO.POLine3 (EntityType)

Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_POLine3
Non-filterable, non-selectable: VendorRefNbr, SOOrderType, SOOrderNbr, SOOrderLineNbr, LinkedToCurrentSOLine, DemandQty

PX.Objects.SO.POLine3.OrderType : Edm.String [key] "PO Type"
PX.Objects.SO.POLine3.OrderNbr : Edm.String [key] "PO Nbr."
PX.Objects.SO.POLine3.VendorRefNbr : Edm.String "Vendor Ref."
PX.Objects.SO.POLine3.LineNbr : Edm.Int32 [key] "PO Line Nbr."
PX.Objects.SO.POLine3.SortOrder : Edm.Int32
PX.Objects.SO.POLine3.LineType : Edm.String "Line Type"
PX.Objects.SO.POLine3.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.POLine3.PlanID : Edm.Int64 "PlanID"
PX.Objects.SO.POLine3.VendorID : Edm.Int32 "Vendor"
PX.Objects.SO.POLine3.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.SO.POLine3.PromisedDate : Edm.DateTimeOffset "Promised"
PX.Objects.SO.POLine3.Cancelled : Edm.Boolean
PX.Objects.SO.POLine3.Completed : Edm.Boolean
PX.Objects.SO.POLine3.Closed : Edm.Boolean
PX.Objects.SO.POLine3.SiteID : Edm.Int32
PX.Objects.SO.POLine3.UOM : Edm.String "UOM"
PX.Objects.SO.POLine3.OrderQty : Edm.Decimal "Order Qty."
PX.Objects.SO.POLine3.BaseOrderQty : Edm.Decimal
PX.Objects.SO.POLine3.OpenQty : Edm.Decimal "Open Qty."
PX.Objects.SO.POLine3.BaseOpenQty : Edm.Decimal
PX.Objects.SO.POLine3.ReceivedQty : Edm.Decimal
PX.Objects.SO.POLine3.BaseReceivedQty : Edm.Decimal
PX.Objects.SO.POLine3.TranDesc : Edm.String "Line Description"
PX.Objects.SO.POLine3.ReceiptStatus : Edm.String
PX.Objects.SO.POLine3.SOOrderType : Edm.String
PX.Objects.SO.POLine3.SOOrderNbr : Edm.String
PX.Objects.SO.POLine3.SOOrderLineNbr : Edm.Int32
PX.Objects.SO.POLine3.LinkedToCurrentSOLine : Edm.Boolean
PX.Objects.SO.POLine3.DemandQty : Edm.Decimal
PX.Objects.SO.POLine3.tstamp : Edm.Binary
PX.Objects.SO.POLine3.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.POLine3.LastModifiedByScreenID : Edm.String
PX.Objects.SO.POLine3.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.POLine3.POOrderByOrderType -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.SO.POLine3.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.POLine3.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.SO.POLine3.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.SO.POLine3.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.SO.POLine3.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.SO.POLine3.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.POLine3.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.SO.POLine3.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.POLine3.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.SO.POLine3.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.SO.POLine3.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.SO.POLine3.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.POLine3.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.SO.POLine3.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.POLine3.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.SO.POLine3.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.SO.POLine3.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.SO.Report.SOShipLineSplitForPacking (EntityType)

Label: "Shipment Line Split For Packing"
Key: LineNbr, ShipmentNbr, SplitLineNbr
Entity sets: PX_Objects_SO_Report_SOShipLineSplitForPacking, ShipmentLineSplitForPacking, SOShipLineSplitForPacking
Non-filterable, non-selectable: TranType, LastLotSerialNbr, LotSerClassID, AssignedNbr

PX.Objects.SO.Report.SOShipLineSplitForPacking.ShipmentNbr : Edm.String [key]
PX.Objects.SO.Report.SOShipLineSplitForPacking.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.Report.SOShipLineSplitForPacking.OrigOrderType : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.OrigOrderNbr : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.OrigLineNbr : Edm.Int32
PX.Objects.SO.Report.SOShipLineSplitForPacking.OrigSplitLineNbr : Edm.Int32
PX.Objects.SO.Report.SOShipLineSplitForPacking.OrigPlanType : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.Operation : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.SplitLineNbr : Edm.Int32 [key]
PX.Objects.SO.Report.SOShipLineSplitForPacking.InvtMult : Edm.Int16
PX.Objects.SO.Report.SOShipLineSplitForPacking.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.Report.SOShipLineSplitForPacking.LineType : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.IsStockItem : Edm.Boolean
PX.Objects.SO.Report.SOShipLineSplitForPacking.IsComponentItem : Edm.Boolean
PX.Objects.SO.Report.SOShipLineSplitForPacking.TranType : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.PlanType : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.PlanID : Edm.Int64
PX.Objects.SO.Report.SOShipLineSplitForPacking.LotSerialNbr : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.LastLotSerialNbr : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.LotSerClassID : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.AssignedNbr : Edm.String
PX.Objects.SO.Report.SOShipLineSplitForPacking.ExpireDate : Edm.DateTimeOffset
PX.Objects.SO.Report.SOShipLineSplitForPacking.UOM : Edm.String "UOM"
PX.Objects.SO.Report.SOShipLineSplitForPacking.Qty : Edm.Decimal "Quantity"
PX.Objects.SO.Report.SOShipLineSplitForPacking.BaseQty : Edm.Decimal
PX.Objects.SO.Report.SOShipLineSplitForPacking.PickedQty : Edm.Decimal "Picked Quantity"
PX.Objects.SO.Report.SOShipLineSplitForPacking.BasePickedQty : Edm.Decimal
PX.Objects.SO.Report.SOShipLineSplitForPacking.PackedQty : Edm.Decimal "Packed Quantity"
PX.Objects.SO.Report.SOShipLineSplitForPacking.BasePackedQty : Edm.Decimal
PX.Objects.SO.Report.SOShipLineSplitForPacking.ShipDate : Edm.DateTimeOffset
PX.Objects.SO.Report.SOShipLineSplitForPacking.Confirmed : Edm.Boolean "Confirmed"
PX.Objects.SO.Report.SOShipLineSplitForPacking.Released : Edm.Boolean "Released"
PX.Objects.SO.Report.SOShipLineSplitForPacking.IsUnassigned : Edm.Boolean
PX.Objects.SO.Report.SOShipLineSplitForPacking.SOOrderTypeOperationByOrigOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrigOrderType=OrderType)
PX.Objects.SO.Report.SOShipLineSplitForPacking.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)

# PX.Objects.SO.SalesAllocation (EntityType)

Label: "Sales Allocation"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_SalesAllocation, SalesAllocation
Non-filterable, non-selectable: QtyHardAvail, QtyToAllocate, QtyToDeallocate, BufferedQty, BufferedTime, IsExtraAllocation

PX.Objects.SO.SalesAllocation.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SalesAllocation.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SalesAllocation.LineNbr : Edm.Int32 [key] "SO Line Nbr."
PX.Objects.SO.SalesAllocation.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SalesAllocation.SubItemID : Edm.Int32
PX.Objects.SO.SalesAllocation.CostCenterID : Edm.Int32
PX.Objects.SO.SalesAllocation.TranDesc : Edm.String "Description"
PX.Objects.SO.SalesAllocation.UOM : Edm.String "UOM"
PX.Objects.SO.SalesAllocation.LineQty : Edm.Decimal "Line Qty."
PX.Objects.SO.SalesAllocation.BaseLineQty : Edm.Decimal "Base Qty."
PX.Objects.SO.SalesAllocation.ShipComplete : Edm.String "Line Shipping Rule"
PX.Objects.SO.SalesAllocation.RequestDate : Edm.DateTimeOffset "Line Requested On"
PX.Objects.SO.SalesAllocation.ShipDate : Edm.DateTimeOffset "Line Ship On"
PX.Objects.SO.SalesAllocation.CuryLineAmt : Edm.Decimal "Line Amount"
PX.Objects.SO.SalesAllocation.LineAmt : Edm.Decimal
PX.Objects.SO.SalesAllocation.QtyAllocated : Edm.Decimal "Qty. Allocated"
PX.Objects.SO.SalesAllocation.QtyUnallocated : Edm.Decimal "Qty. Unallocated"
PX.Objects.SO.SalesAllocation.LotSerialQtyAllocated : Edm.Decimal
PX.Objects.SO.SalesAllocation.BaseUOM : Edm.String "Base UOM"
PX.Objects.SO.SalesAllocation.InventoryCD : Edm.String
PX.Objects.SO.SalesAllocation.OrderPriority : Edm.Int16 "Order Priority"
PX.Objects.SO.SalesAllocation.OrderStatus : Edm.String "Order Status"
PX.Objects.SO.SalesAllocation.OrderHold : Edm.Boolean
PX.Objects.SO.SalesAllocation.OrderDesc : Edm.String "Order Description"
PX.Objects.SO.SalesAllocation.CustomerID : Edm.Int32 "Customer"
PX.Objects.SO.SalesAllocation.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.SO.SalesAllocation.CancelDate : Edm.DateTimeOffset "Cancel By"
PX.Objects.SO.SalesAllocation.SalesPersonID : Edm.Int32 "Salesperson ID"
PX.Objects.SO.SalesAllocation.CuryID : Edm.String "Currency"
PX.Objects.SO.SalesAllocation.OrderCreatedOn : Edm.DateTimeOffset
PX.Objects.SO.SalesAllocation.CuryOrderTotal : Edm.Decimal "Order Total"
PX.Objects.SO.SalesAllocation.OrderTotal : Edm.Decimal
PX.Objects.SO.SalesAllocation.CustomerName : Edm.String "Customer Name"
PX.Objects.SO.SalesAllocation.CustomerClassID : Edm.String "Customer Class"
PX.Objects.SO.SalesAllocation.QtyHardAvail : Edm.Decimal "Available for Shipping"
PX.Objects.SO.SalesAllocation.QtyToAllocate : Edm.Decimal "Qty. to Allocate"
PX.Objects.SO.SalesAllocation.QtyToDeallocate : Edm.Decimal "Qty. to Deallocate"
PX.Objects.SO.SalesAllocation.BufferedQty : Edm.Decimal
PX.Objects.SO.SalesAllocation.BufferedTime : Edm.DateTimeOffset
PX.Objects.SO.SalesAllocation.IsExtraAllocation : Edm.Boolean
PX.Objects.SO.SalesAllocation.NoteID : Edm.Guid
PX.Objects.SO.SalesAllocation.SOOrderByOrderType -> PX.Objects.SO.SOOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.SO.SalesAllocation.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SalesAllocation.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass (CustomerClassID=CustomerClassID)
PX.Objects.SO.SalesAllocation.INSiteStatusByCostCenterShortByCostCenterID -> PX.Objects.IN.INSiteStatusByCostCenterShort (InventoryID=InventoryID, SubItemID=SubItemID, CostCenterID=CostCenterID)
PX.Objects.SO.SalesAllocation.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SalesAllocation.INSubItemBySubItemID -> PX.Objects.IN.INSubItem (SubItemID=SubItemID)
PX.Objects.SO.SalesAllocation.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.SO.SalesAllocation.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.SalesAllocation.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.SalesAllocation.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SalesAllocation.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SalesAllocation.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SalesAllocation.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SalesAllocation.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SalesAllocation.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SalesAllocation.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.SO.SalesAllocation.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SalesAllocation.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SalesAllocation.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.SalesAllocation.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.SalesAllocation.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.SalesAllocation.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SalesAllocation.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.SO.SalesAllocation.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.SO.SalesAllocation.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.SO.SalesAllocation.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.SO.SOAddress (EntityType)

Label: "SO Address"
Key: AddressID
Entity sets: PX_Objects_SO_SOAddress, SOAddress
Non-filterable, non-selectable: OverrideAddress

PX.Objects.SO.SOAddress.AddressID : Edm.Int32 [key] "Address ID"
PX.Objects.SO.SOAddress.CustomerID : Edm.Int32
PX.Objects.SO.SOAddress.CustomerAddressID : Edm.Int32
PX.Objects.SO.SOAddress.IsDefaultAddress : Edm.Boolean [required] "Default Customer Address"
PX.Objects.SO.SOAddress.OverrideAddress : Edm.Boolean "Override Address"
PX.Objects.SO.SOAddress.IsEncrypted : Edm.Boolean
PX.Objects.SO.SOAddress.RevisionID : Edm.Int32 "RevisionID"
PX.Objects.SO.SOAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.SO.SOAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.SO.SOAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.SO.SOAddress.City : Edm.String "City"
PX.Objects.SO.SOAddress.CountryID : Edm.String "Country"
PX.Objects.SO.SOAddress.State : Edm.String "State"
PX.Objects.SO.SOAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.SO.SOAddress.Department : Edm.String "Department"
PX.Objects.SO.SOAddress.SubDepartment : Edm.String "Subdepartment"
PX.Objects.SO.SOAddress.StreetName : Edm.String "Street Name"
PX.Objects.SO.SOAddress.BuildingNumber : Edm.String "Building Number"
PX.Objects.SO.SOAddress.BuildingName : Edm.String "Building Name"
PX.Objects.SO.SOAddress.Floor : Edm.String "Floor"
PX.Objects.SO.SOAddress.UnitNumber : Edm.String "Unit Number"
PX.Objects.SO.SOAddress.PostBox : Edm.String "Post Box"
PX.Objects.SO.SOAddress.Room : Edm.String "Room"
PX.Objects.SO.SOAddress.TownLocationName : Edm.String "Town Location Name"
PX.Objects.SO.SOAddress.DistrictName : Edm.String "District Name"
PX.Objects.SO.SOAddress.AddressType : Edm.String "Address Type"
PX.Objects.SO.SOAddress.CareOf : Edm.String "Care Of"
PX.Objects.SO.SOAddress.NoteID : Edm.Guid
PX.Objects.SO.SOAddress.tstamp : Edm.Binary
PX.Objects.SO.SOAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOAddress.CreatedByScreenID : Edm.String
PX.Objects.SO.SOAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOAddress.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOAddress.Latitude : Edm.Decimal "Latitude"
PX.Objects.SO.SOAddress.Longitude : Edm.Decimal "Longitude"
PX.Objects.SO.SOAddress.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOAddress.ARAddressByCustomerAddressID -> PX.Objects.AR.ARAddress (CustomerAddressID=AddressID)
PX.Objects.SO.SOAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.SO.SOAddress.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.SO.SOAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.SO.SOAddress.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SO.SOAddress.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.SO.SOAddress.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOAddress.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)

# PX.Objects.SO.SOAdjust (EntityType)

Label: "Sales Order Adjust"
Key: AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr, RecordID
Entity sets: PX_Objects_SO_SOAdjust, SalesOrderAdjust, SOAdjust
Non-filterable, non-selectable: CuryAdjgDiscAmt, CuryAdjdDiscAmt, AdjDiscAmt, CuryDocBal, CuryInitialDocBal, CuryInitialDiscBal, CuryInitialWBal, DocBal, RefTranExtNbr, ExternalRef, Authorize, Capture, Refund, NoteText, IsBalanceRecalculationRequired, NewCard, SaveCard

PX.Objects.SO.SOAdjust.RecordID : Edm.Int32 [key]
PX.Objects.SO.SOAdjust.Hold : Edm.Boolean
PX.Objects.SO.SOAdjust.CustomerID : Edm.Int32
PX.Objects.SO.SOAdjust.AdjgDocType : Edm.String [key] "Doc. Type"
PX.Objects.SO.SOAdjust.AdjgRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.SO.SOAdjust.AdjdOrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOAdjust.AdjdOrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOAdjust.CuryAdjgAmt : Edm.Decimal [required] "Applied To Order"
PX.Objects.SO.SOAdjust.AdjAmt : Edm.Decimal [required]
PX.Objects.SO.SOAdjust.CuryAdjdAmt : Edm.Decimal [required]
PX.Objects.SO.SOAdjust.CuryOrigAdjdAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.OrigAdjAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.CuryOrigAdjgAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.CuryAdjdOrigBlanketAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.AdjOrigBlanketAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.CuryAdjgOrigBlanketAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.CuryAdjgDiscAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.CuryAdjdDiscAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.AdjDiscAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.AdjdOrigCuryInfoID : Edm.Int64
PX.Objects.SO.SOAdjust.AdjgCuryInfoID : Edm.Int64
PX.Objects.SO.SOAdjust.AdjdCuryInfoID : Edm.Int64
PX.Objects.SO.SOAdjust.AdjgDocDate : Edm.DateTimeOffset "Application Date"
PX.Objects.SO.SOAdjust.AdjdOrderDate : Edm.DateTimeOffset "Date"
PX.Objects.SO.SOAdjust.CuryAdjgBilledAmt : Edm.Decimal [required] "Transferred to Invoice"
PX.Objects.SO.SOAdjust.AdjBilledAmt : Edm.Decimal [required]
PX.Objects.SO.SOAdjust.CuryAdjdBilledAmt : Edm.Decimal [required] "Transferred to Invoice"
PX.Objects.SO.SOAdjust.CuryAdjgTransferredToChildrenAmt : Edm.Decimal [required] "Transferred to Child Orders"
PX.Objects.SO.SOAdjust.AdjTransferredToChildrenAmt : Edm.Decimal [required]
PX.Objects.SO.SOAdjust.CuryAdjdTransferredToChildrenAmt : Edm.Decimal [required] "Transferred to Child Orders"
PX.Objects.SO.SOAdjust.CuryDocBal : Edm.Decimal "Balance"
PX.Objects.SO.SOAdjust.CuryInitialDocBal : Edm.Decimal
PX.Objects.SO.SOAdjust.CuryInitialDiscBal : Edm.Decimal
PX.Objects.SO.SOAdjust.CuryInitialWBal : Edm.Decimal
PX.Objects.SO.SOAdjust.DocBal : Edm.Decimal
PX.Objects.SO.SOAdjust.IsCCPayment : Edm.Boolean
PX.Objects.SO.SOAdjust.PaymentReleased : Edm.Boolean
PX.Objects.SO.SOAdjust.IsCCAuthorized : Edm.Boolean
PX.Objects.SO.SOAdjust.IsCCCaptured : Edm.Boolean
PX.Objects.SO.SOAdjust.Voided : Edm.Boolean
PX.Objects.SO.SOAdjust.BlanketRecordID : Edm.Int32
PX.Objects.SO.SOAdjust.BlanketType : Edm.String "Blanket SO Type"
PX.Objects.SO.SOAdjust.BlanketNbr : Edm.String "Blanket SO Ref. Nbr."
PX.Objects.SO.SOAdjust.RefTranExtNbr : Edm.String
PX.Objects.SO.SOAdjust.ExternalRef : Edm.String
PX.Objects.SO.SOAdjust.Authorize : Edm.Boolean
PX.Objects.SO.SOAdjust.Capture : Edm.Boolean
PX.Objects.SO.SOAdjust.Refund : Edm.Boolean
PX.Objects.SO.SOAdjust.ValidateCCRefundOrigTransaction : Edm.Boolean
PX.Objects.SO.SOAdjust.NoteID : Edm.Guid
PX.Objects.SO.SOAdjust.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOAdjust.IsBalanceRecalculationRequired : Edm.Boolean
PX.Objects.SO.SOAdjust.tstamp : Edm.Binary
PX.Objects.SO.SOAdjust.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOAdjust.CreatedByScreenID : Edm.String
PX.Objects.SO.SOAdjust.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOAdjust.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOAdjust.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOAdjust.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOAdjust.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.SO.SOAdjust.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.SO.SOAdjust.ProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.SO.SOAdjust.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.SO.SOAdjust.DocDesc : Edm.String "Description"
PX.Objects.SO.SOAdjust.CuryOrigDocAmt : Edm.Decimal "Payment Amount"
PX.Objects.SO.SOAdjust.OrigDocAmt : Edm.Decimal
PX.Objects.SO.SOAdjust.SyncLock : Edm.Boolean
PX.Objects.SO.SOAdjust.SyncLockReason : Edm.String
PX.Objects.SO.SOAdjust.NewCard : Edm.Boolean
PX.Objects.SO.SOAdjust.SaveCard : Edm.Boolean "Save Card"
PX.Objects.SO.SOAdjust.PendingPayment : Edm.Boolean
PX.Objects.SO.SOAdjust.ARInvoiceByAdjgRefNbr -> PX.Objects.AR.ARInvoice (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SO.SOAdjust.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOAdjust.ARPaymentByAdjgRefNbr -> PX.Objects.AR.ARPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SO.SOAdjust.SOOrderByAdjdOrderNbr -> PX.Objects.SO.SOOrder (AdjdOrderType=OrderType, AdjdOrderNbr=OrderNbr)
PX.Objects.SO.SOAdjust.SOOrderByAdjgRefNbr -> PX.Objects.SO.SOOrder (AdjgDocType=OrderType, AdjgRefNbr=OrderNbr)
PX.Objects.SO.SOAdjust.SOOrderByCustomerID -> PX.Objects.SO.SOOrder (AdjdOrderNbr=OrderNbr, AdjdOrderType=OrderType, CustomerID=CustomerID)
PX.Objects.SO.SOAdjust.CurrencyInfoByAdjgCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjgCuryInfoID=CuryInfoID)
PX.Objects.SO.SOAdjust.CurrencyInfoByAdjdCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdCuryInfoID=CuryInfoID)
PX.Objects.SO.SOAdjust.CurrencyInfoByAdjdOrigCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdOrigCuryInfoID=CuryInfoID)
PX.Objects.SO.SOAdjust.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOAdjust.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOAdjust.SOOrderTypeByAdjdOrderType -> PX.Objects.SO.SOOrderType (AdjdOrderType=OrderType)
PX.Objects.SO.SOAdjust.AccountByCashAccountID -> PX.Objects.GL.Account
PX.Objects.SO.SOAdjust.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.SO.SOAdjust.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.SO.SOAdjust.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.SO.SOAdjust.ARPaymentTotalsByAdjgRefNbr -> PX.Objects.AR.ARPaymentTotals (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.SO.SOAdjust.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.SO.SOAdjust.BlanketSOAdjustByAdjgRefNbr -> PX.Objects.SO.DAC.Projections.BlanketSOAdjust (BlanketRecordID=RecordID, BlanketType=AdjdOrderType, BlanketNbr=AdjdOrderNbr, AdjgDocType=AdjgDocType, AdjgRefNbr=AdjgRefNbr)
PX.Objects.SO.SOAdjust.BlanketSOOrderByBlanketNbr -> PX.Objects.SO.DAC.Projections.BlanketSOOrder (BlanketType=OrderType, BlanketNbr=OrderNbr)
PX.Objects.SO.SOAdjust.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)

# PX.Objects.SO.SOBillingAddress (EntityType)

Label: "Billing Address"
BaseType: PX.Objects.SO.SOAddress
Key: AddressID (inherited from PX.Objects.SO.SOAddress)
Entity sets: PX_Objects_SO_SOBillingAddress, BillingAddress, SOBillingAddress

# PX.Objects.SO.SOBillingContact (EntityType)

Label: "Billing Contact"
BaseType: PX.Objects.SO.SOContact
Key: ContactID (inherited from PX.Objects.SO.SOContact)
Entity sets: PX_Objects_SO_SOBillingContact, BillingContact, SOBillingContact

# PX.Objects.SO.SOBlanketOrderDisplayLink (EntityType)

Label: "Blanket Order Display Link"
BaseType: PX.Objects.SO.SOBlanketOrderLink
Key: BlanketNbr, BlanketType, OrderNbr, OrderType (inherited from PX.Objects.SO.SOBlanketOrderLink)
Entity sets: PX_Objects_SO_SOBlanketOrderDisplayLink, BlanketOrderDisplayLink, SOBlanketOrderDisplayLink
Non-filterable, non-selectable: DisplayShippingRefNoteID

PX.Objects.SO.SOBlanketOrderDisplayLink.OrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.SO.SOBlanketOrderDisplayLink.OrderStatus : Edm.String "Order Status"
PX.Objects.SO.SOBlanketOrderDisplayLink.Operation : Edm.String "Operation"
PX.Objects.SO.SOBlanketOrderDisplayLink.ShippingRefNoteID : Edm.Guid
PX.Objects.SO.SOBlanketOrderDisplayLink.DisplayShippingRefNoteID : Edm.Guid "Document Nbr."
PX.Objects.SO.SOBlanketOrderDisplayLink.ShipmentType : Edm.String "Shipment Type"
PX.Objects.SO.SOBlanketOrderDisplayLink.ShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.SO.SOBlanketOrderDisplayLink.ShipmentDate : Edm.DateTimeOffset "Shipment Date"
PX.Objects.SO.SOBlanketOrderDisplayLink.ShipmentStatus : Edm.String "Shipment Status"
PX.Objects.SO.SOBlanketOrderDisplayLink.ShippedQty : Edm.Decimal "Shipped Qty."
PX.Objects.SO.SOBlanketOrderDisplayLink.InvoiceType : Edm.String "Invoice Type"
PX.Objects.SO.SOBlanketOrderDisplayLink.InvoiceNbr : Edm.String "Invoice Nbr."
PX.Objects.SO.SOBlanketOrderDisplayLink.InvoiceDate : Edm.DateTimeOffset "Invoice Date"
PX.Objects.SO.SOBlanketOrderDisplayLink.InvoiceStatus : Edm.String "Invoice Status"
PX.Objects.SO.SOBlanketOrderDisplayLink.InvtDocType : Edm.String "Inventory Doc. Type"
PX.Objects.SO.SOBlanketOrderDisplayLink.InvtRefNbr : Edm.String "Inventory Ref. Nbr."
PX.Objects.SO.SOBlanketOrderDisplayLink.INRegisterByInvtRefNbr -> PX.Objects.IN.INRegister (InvtRefNbr=RefNbr)
PX.Objects.SO.SOBlanketOrderDisplayLink.SOInvoiceByInvoiceType -> PX.Objects.SO.SOInvoice (InvoiceNbr=RefNbr, InvoiceType=DocType)
PX.Objects.SO.SOBlanketOrderDisplayLink.ARInvoiceByInvoiceNbr -> PX.Objects.AR.ARInvoice (InvoiceType=DocType, InvoiceNbr=RefNbr)
PX.Objects.SO.SOBlanketOrderDisplayLink.ARRegisterByInvoiceNbr -> PX.Objects.AR.ARRegister (InvoiceType=DocType, InvoiceNbr=RefNbr)
PX.Objects.SO.SOBlanketOrderDisplayLink.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentType=ShipmentType, ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOBlanketOrderDisplayLink.SOShipmentByShipmentType -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr, ShipmentType=ShipmentType)
PX.Objects.SO.SOBlanketOrderDisplayLink.INRegisterByInvtDocType -> PX.Objects.IN.INRegister (InvtRefNbr=RefNbr, InvtDocType=DocType)
PX.Objects.SO.SOBlanketOrderDisplayLink.SOInvoiceByInvoiceNbr -> PX.Objects.SO.SOInvoice (InvoiceType=DocType, InvoiceNbr=RefNbr)

# PX.Objects.SO.SOBlanketOrderLink (EntityType)

Label: "Blanket Order Link"
Key: BlanketNbr, BlanketType, OrderNbr, OrderType
Entity sets: PX_Objects_SO_SOBlanketOrderLink, BlanketOrderLink, SOBlanketOrderLink
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOBlanketOrderLink.BlanketType : Edm.String [key]
PX.Objects.SO.SOBlanketOrderLink.BlanketNbr : Edm.String [key] "Blanket Order Nbr."
PX.Objects.SO.SOBlanketOrderLink.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOBlanketOrderLink.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOBlanketOrderLink.OrderedQty : Edm.Decimal [required] "Ordered Qty."
PX.Objects.SO.SOBlanketOrderLink.CuryInfoID : Edm.Int64
PX.Objects.SO.SOBlanketOrderLink.CuryOrderedAmt : Edm.Decimal [required] "Ordered Amount"
PX.Objects.SO.SOBlanketOrderLink.OrderedAmt : Edm.Decimal [required]
PX.Objects.SO.SOBlanketOrderLink.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOBlanketOrderLink.CreatedByScreenID : Edm.String
PX.Objects.SO.SOBlanketOrderLink.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOBlanketOrderLink.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOBlanketOrderLink.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOBlanketOrderLink.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOBlanketOrderLink.tstamp : Edm.Binary
PX.Objects.SO.SOBlanketOrderLink.CuryID : Edm.String "Currency"
PX.Objects.SO.SOBlanketOrderLink.CuryRate : Edm.Decimal
PX.Objects.SO.SOBlanketOrderLink.CuryViewState : Edm.Boolean
PX.Objects.SO.SOBlanketOrderLink.SOOrderByBlanketNbr -> PX.Objects.SO.SOOrder (BlanketType=OrderType, BlanketNbr=OrderNbr)
PX.Objects.SO.SOBlanketOrderLink.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOBlanketOrderLink.SOOrderByBlanketType -> PX.Objects.SO.SOOrder (BlanketNbr=OrderNbr, BlanketType=OrderType)
PX.Objects.SO.SOBlanketOrderLink.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOBlanketOrderLink.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOBlanketOrderLink.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOBlanketOrderLink.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOBlanketOrderLink.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)

# PX.Objects.SO.SOCartShipment (EntityType)

Label: "Shipment Cart"
Key: CartID, SiteID
Entity sets: PX_Objects_SO_SOCartShipment, ShipmentCart, SOCartShipment

PX.Objects.SO.SOCartShipment.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.SO.SOCartShipment.CartID : Edm.Int32 [key]
PX.Objects.SO.SOCartShipment.ShipmentNbr : Edm.String
PX.Objects.SO.SOCartShipment.tstamp : Edm.Binary
PX.Objects.SO.SOCartShipment.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOCartShipment.INCartByCartID -> PX.Objects.IN.INCart (SiteID=SiteID, CartID=CartID)
PX.Objects.SO.SOCartShipment.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)

# PX.Objects.SO.SOContact (EntityType)

Label: "SO Contact"
Key: ContactID
Entity sets: PX_Objects_SO_SOContact, SOContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.SO.SOContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.SO.SOContact.CustomerID : Edm.Int32
PX.Objects.SO.SOContact.CustomerContactID : Edm.Int32
PX.Objects.SO.SOContact.IsDefaultContact : Edm.Boolean [required] "Default Customer Contact"
PX.Objects.SO.SOContact.OverrideContact : Edm.Boolean "Override Contact"
PX.Objects.SO.SOContact.IsEncrypted : Edm.Boolean
PX.Objects.SO.SOContact.RevisionID : Edm.Int32 "RevisionID"
PX.Objects.SO.SOContact.Title : Edm.String "Title"
PX.Objects.SO.SOContact.Salutation : Edm.String "Job Title"
PX.Objects.SO.SOContact.Attention : Edm.String "Attention"
PX.Objects.SO.SOContact.FullName : Edm.String "Account Name"
PX.Objects.SO.SOContact.Email : Edm.String "Email"
PX.Objects.SO.SOContact.Fax : Edm.String "Fax"
PX.Objects.SO.SOContact.FaxType : Edm.String "Fax"
PX.Objects.SO.SOContact.Phone1 : Edm.String "Phone 1"
PX.Objects.SO.SOContact.Phone1Type : Edm.String "Phone 1"
PX.Objects.SO.SOContact.Phone2 : Edm.String "Phone 2"
PX.Objects.SO.SOContact.Phone2Type : Edm.String "Phone 2"
PX.Objects.SO.SOContact.Phone3 : Edm.String "Phone 3"
PX.Objects.SO.SOContact.Phone3Type : Edm.String "Phone 3"
PX.Objects.SO.SOContact.NoteID : Edm.Guid
PX.Objects.SO.SOContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOContact.CreatedByScreenID : Edm.String
PX.Objects.SO.SOContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.SO.SOContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOContact.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.SO.SOContact.tstamp : Edm.Binary
PX.Objects.SO.SOContact.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOContact.ARContactByCustomerContactID -> PX.Objects.AR.ARContact (CustomerContactID=ContactID)
PX.Objects.SO.SOContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOContact.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SO.SOContact.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.SO.SOContact.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOContact.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)

# PX.Objects.SO.SOFreightDetail (EntityType)

Label: "SO Freight Detail"
Key: DocType, OrderNbr, OrderType, RefNbr, ShipmentNbr, ShipmentType
Entity sets: PX_Objects_SO_SOFreightDetail, SOFreightDetail
Non-filterable, non-selectable: NoteText

PX.Objects.SO.SOFreightDetail.DocType : Edm.String [key]
PX.Objects.SO.SOFreightDetail.RefNbr : Edm.String [key]
PX.Objects.SO.SOFreightDetail.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOFreightDetail.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOFreightDetail.ShipmentType : Edm.String [key] "Shipment Type"
PX.Objects.SO.SOFreightDetail.ShipmentNbr : Edm.String [key] "Shipment Nbr."
PX.Objects.SO.SOFreightDetail.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.SO.SOFreightDetail.ShipZoneID : Edm.String "Shipping Zone ID"
PX.Objects.SO.SOFreightDetail.ShipVia : Edm.String "Ship Via"
PX.Objects.SO.SOFreightDetail.Weight : Edm.Decimal [required] "Weight"
PX.Objects.SO.SOFreightDetail.Volume : Edm.Decimal [required] "Volume"
PX.Objects.SO.SOFreightDetail.CuryInfoID : Edm.Int64
PX.Objects.SO.SOFreightDetail.CuryLineTotal : Edm.Decimal [required] "Line Total"
PX.Objects.SO.SOFreightDetail.LineTotal : Edm.Decimal
PX.Objects.SO.SOFreightDetail.CuryFreightCost : Edm.Decimal [required] "Freight Cost"
PX.Objects.SO.SOFreightDetail.FreightCost : Edm.Decimal
PX.Objects.SO.SOFreightDetail.CuryFreightAmt : Edm.Decimal [required] "Freight Price"
PX.Objects.SO.SOFreightDetail.FreightAmt : Edm.Decimal
PX.Objects.SO.SOFreightDetail.CuryPremiumFreightAmt : Edm.Decimal [required] "Premium Freight Price"
PX.Objects.SO.SOFreightDetail.PremiumFreightAmt : Edm.Decimal
PX.Objects.SO.SOFreightDetail.CuryTotalFreightAmt : Edm.Decimal [required] "Total Freight Price"
PX.Objects.SO.SOFreightDetail.TotalFreightAmt : Edm.Decimal
PX.Objects.SO.SOFreightDetail.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.SO.SOFreightDetail.ProjectID : Edm.Int32
PX.Objects.SO.SOFreightDetail.NoteID : Edm.Guid
PX.Objects.SO.SOFreightDetail.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOFreightDetail.tstamp : Edm.Binary
PX.Objects.SO.SOFreightDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOFreightDetail.CreatedByScreenID : Edm.String
PX.Objects.SO.SOFreightDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOFreightDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOFreightDetail.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOFreightDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOFreightDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SO.SOFreightDetail.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.SO.SOFreightDetail.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.SO.SOFreightDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.SO.SOFreightDetail.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOFreightDetail.SOOrderByOrderType -> PX.Objects.SO.SOOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.SO.SOFreightDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOFreightDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOFreightDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOFreightDetail.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SO.SOFreightDetail.SOOrderShipmentByOrderNbr -> PX.Objects.SO.SOOrderShipment (ShipmentType=ShipmentType, ShipmentNbr=ShipmentNbr, OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOFreightDetail.SOOrderShipmentByShipmentType -> PX.Objects.SO.SOOrderShipment (ShipmentNbr=ShipmentNbr, OrderType=OrderType, OrderNbr=OrderNbr, ShipmentType=ShipmentType)
PX.Objects.SO.SOFreightDetail.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOFreightDetail.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentType=ShipmentType, ShipmentNbr=ShipmentNbr)
PX.Objects.SO.SOFreightDetail.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.SO.SOFreightDetail.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.SO.SOFreightDetail.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.SO.SOFreightDetail.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.SO.SOFreightDetail.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.SO.SOFreightDetail.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.SO.SOInvoice (EntityType)

Label: "SO Invoice"
Key: DocType, RefNbr
Entity sets: PX_Objects_SO_SOInvoice, SOInvoice
Non-filterable, non-selectable: NoteText, ARPaymentPMInstanceID, ARPaymentPaymentMethodID, ARPaymentCashAccountID, ARPaymentExtRefNbr, ARPaymentCleared, ARPaymentClearDate, ARPaymentCATranID, ARPaymentDepositAsBatch, SuggestRelatedItems

PX.Objects.SO.SOInvoice.DocType : Edm.String [key] "Type"
PX.Objects.SO.SOInvoice.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.SO.SOInvoice.CustomerID : Edm.Int32 "Customer"
PX.Objects.SO.SOInvoice.CuryInfoID : Edm.Int64
PX.Objects.SO.SOInvoice.BillAddressID : Edm.Int32
PX.Objects.SO.SOInvoice.BillContactID : Edm.Int32
PX.Objects.SO.SOInvoice.ShipAddressID : Edm.Int32
PX.Objects.SO.SOInvoice.ShipContactID : Edm.Int32
PX.Objects.SO.SOInvoice.CuryManDisc : Edm.Decimal [required] "Manual Total"
PX.Objects.SO.SOInvoice.ManDisc : Edm.Decimal [required]
PX.Objects.SO.SOInvoice.tstamp : Edm.Binary
PX.Objects.SO.SOInvoice.CuryPaymentAmt : Edm.Decimal [required] "Payment Amount"
PX.Objects.SO.SOInvoice.PaymentAmt : Edm.Decimal [required]
PX.Objects.SO.SOInvoice.CuryID : Edm.String
PX.Objects.SO.SOInvoice.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.SO.SOInvoice.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.SO.SOInvoice.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.SO.SOInvoice.Cleared : Edm.Boolean [required] "Cleared"
PX.Objects.SO.SOInvoice.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.SO.SOInvoice.CATranID : Edm.Int64
PX.Objects.SO.SOInvoice.ARRegisterDocType : Edm.String
PX.Objects.SO.SOInvoice.ARRegisterRefNbr : Edm.String
PX.Objects.SO.SOInvoice.Released : Edm.Boolean
PX.Objects.SO.SOInvoice.Hold : Edm.Boolean
PX.Objects.SO.SOInvoice.DocDesc : Edm.String "Description"
PX.Objects.SO.SOInvoice.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.SO.SOInvoice.Status : Edm.String "Status"
PX.Objects.SO.SOInvoice.IsTaxValid : Edm.Boolean
PX.Objects.SO.SOInvoice.IsTaxSaved : Edm.Boolean "Tax has been saved in the external tax provider"
PX.Objects.SO.SOInvoice.NoteID : Edm.Guid
PX.Objects.SO.SOInvoice.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOInvoice.CuryOrigDocAmt : Edm.Decimal
PX.Objects.SO.SOInvoice.OrigDocAmt : Edm.Decimal
PX.Objects.SO.SOInvoice.DisableAutomaticTaxCalculation : Edm.Boolean
PX.Objects.SO.SOInvoice.ARPaymentDocType : Edm.String
PX.Objects.SO.SOInvoice.ARPaymentRefNbr : Edm.String
PX.Objects.SO.SOInvoice.ARPaymentPMInstanceID : Edm.Int32
PX.Objects.SO.SOInvoice.ARPaymentPaymentMethodID : Edm.String
PX.Objects.SO.SOInvoice.ARPaymentCashAccountID : Edm.Int32
PX.Objects.SO.SOInvoice.ARPaymentExtRefNbr : Edm.String
PX.Objects.SO.SOInvoice.AdjDate : Edm.DateTimeOffset
PX.Objects.SO.SOInvoice.AdjFinPeriodID : Edm.String
PX.Objects.SO.SOInvoice.AdjTranPeriodID : Edm.String
PX.Objects.SO.SOInvoice.ARPaymentCleared : Edm.Boolean
PX.Objects.SO.SOInvoice.ARPaymentClearDate : Edm.DateTimeOffset
PX.Objects.SO.SOInvoice.ARPaymentCATranID : Edm.Int64
PX.Objects.SO.SOInvoice.ARPaymentDepositAsBatch : Edm.Boolean
PX.Objects.SO.SOInvoice.DepositAfter : Edm.DateTimeOffset
PX.Objects.SO.SOInvoice.Deposited : Edm.Boolean
PX.Objects.SO.SOInvoice.DepositType : Edm.String
PX.Objects.SO.SOInvoice.DepositNbr : Edm.String
PX.Objects.SO.SOInvoice.ChargeCntr : Edm.Int32
PX.Objects.SO.SOInvoice.CuryConsolidateChargeTotal : Edm.Decimal "Consolidate Charges"
PX.Objects.SO.SOInvoice.ConsolidateChargeTotal : Edm.Decimal
PX.Objects.SO.SOInvoice.CreateINDoc : Edm.Boolean [required]
PX.Objects.SO.SOInvoice.TranCntr : Edm.Int32 [required]
PX.Objects.SO.SOInvoice.SOOrderType : Edm.String "Order Type"
PX.Objects.SO.SOInvoice.SOOrderNbr : Edm.String "Order Nbr."
PX.Objects.SO.SOInvoice.InitialSOBehavior : Edm.String
PX.Objects.SO.SOInvoice.SuggestRelatedItems : Edm.Boolean
PX.Objects.SO.SOInvoice.PMProjectByPaymentProjectID -> PX.Objects.PM.PMProject
PX.Objects.SO.SOInvoice.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.SO.SOInvoice.SOAddressByBillAddressID -> PX.Objects.SO.SOAddress (BillAddressID=AddressID)
PX.Objects.SO.SOInvoice.SOAddressByShipAddressID -> PX.Objects.SO.SOAddress (ShipAddressID=AddressID)
PX.Objects.SO.SOInvoice.SOContactByBillContactID -> PX.Objects.SO.SOContact (BillContactID=ContactID)
PX.Objects.SO.SOInvoice.SOContactByShipContactID -> PX.Objects.SO.SOContact (ShipContactID=ContactID)
PX.Objects.SO.SOInvoice.PMTaskByPaymentTaskID -> PX.Objects.PM.PMTask
PX.Objects.SO.SOInvoice.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.SO.SOInvoice.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOInvoice.ARPaymentByARPaymentRefNbr -> PX.Objects.AR.ARPayment (ARPaymentDocType=DocType, ARPaymentRefNbr=RefNbr)
PX.Objects.SO.SOInvoice.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.SO.SOInvoice.ARRegisterByARRegisterRefNbr -> PX.Objects.AR.ARRegister (ARRegisterDocType=DocType, ARRegisterRefNbr=RefNbr)
PX.Objects.SO.SOInvoice.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOInvoice.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.SO.SOInvoice.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.SO.SOInvoice.AccountByCashAccountID -> PX.Objects.GL.Account
PX.Objects.SO.SOInvoice.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.SO.SOInvoice.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.SO.SOInvoice.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.SO.SOInvoice.CustomerPaymentMethodByPaymentMethodID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID, CustomerID=BAccountID, PaymentMethodID=PaymentMethodID)
PX.Objects.SO.SOInvoice.SOBlanketOrderDisplayLinkCollection -> Collection(PX.Objects.SO.SOBlanketOrderDisplayLink)
PX.Objects.SO.SOInvoice.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.SO.SOInvoice.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.SO.SOInvoice.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOInvoice.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.SO.SOInvoice.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.SO.SOInvoice.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.SO.SOInvoice.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.SOInvoice.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SOInvoice.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.SO.SOInvoice.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.SO.SOInvoice.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.SO.SOInvoice.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.SO.SOInvoice.ARTranAccrueCostCollection -> Collection(PX.Objects.AR.ARTranAccrueCost)

# PX.Objects.SO.SOInvoiceSiteStatusSelected (EntityType)

Label: "Invoice Inventory Lookup Row"
Key: InventoryID
Entity sets: PX_Objects_SO_SOInvoiceSiteStatusSelected, InvoiceInventoryLookupRow, SOInvoiceSiteStatusSelected
Non-filterable, non-selectable: CuryID, CuryInfoID, QtySelected, CuryUnitPrice, DropShipCuryUnitPrice, Rank, CuryRate, CuryViewState

PX.Objects.SO.SOInvoiceSiteStatusSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.SO.SOInvoiceSiteStatusSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.SO.SOInvoiceSiteStatusSelected.Descr : Edm.String "Description"
PX.Objects.SO.SOInvoiceSiteStatusSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.SO.SOInvoiceSiteStatusSelected.ItemClassCD : Edm.String
PX.Objects.SO.SOInvoiceSiteStatusSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.SO.SOInvoiceSiteStatusSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.SO.SOInvoiceSiteStatusSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.SO.SOInvoiceSiteStatusSelected.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.SO.SOInvoiceSiteStatusSelected.PreferredVendorDescription : Edm.String "Preferred Vendor Name"
PX.Objects.SO.SOInvoiceSiteStatusSelected.BarCode : Edm.String "Barcode"
PX.Objects.SO.SOInvoiceSiteStatusSelected.AlternateID : Edm.String "Alternate ID"
PX.Objects.SO.SOInvoiceSiteStatusSelected.AlternateType : Edm.String "Alternate Type"
PX.Objects.SO.SOInvoiceSiteStatusSelected.AlternateDescr : Edm.String "Alternate Description"
PX.Objects.SO.SOInvoiceSiteStatusSelected.SiteCD : Edm.String
PX.Objects.SO.SOInvoiceSiteStatusSelected.SubItemCD : Edm.String
PX.Objects.SO.SOInvoiceSiteStatusSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.SO.SOInvoiceSiteStatusSelected.CuryID : Edm.String "Currency"
PX.Objects.SO.SOInvoiceSiteStatusSelected.CuryInfoID : Edm.Int64
PX.Objects.SO.SOInvoiceSiteStatusSelected.SalesUnit : Edm.String "Sales Unit"
PX.Objects.SO.SOInvoiceSiteStatusSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.SO.SOInvoiceSiteStatusSelected.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.SO.SOInvoiceSiteStatusSelected.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.SO.SOInvoiceSiteStatusSelected.QtyLast : Edm.Decimal
PX.Objects.SO.SOInvoiceSiteStatusSelected.BaseUnitPrice : Edm.Decimal
PX.Objects.SO.SOInvoiceSiteStatusSelected.CuryUnitPrice : Edm.Decimal "Last Unit Price"
PX.Objects.SO.SOInvoiceSiteStatusSelected.QtyAvailSale : Edm.Decimal "Qty. Available"
PX.Objects.SO.SOInvoiceSiteStatusSelected.QtyOnHandSale : Edm.Decimal "Qty. On Hand"
PX.Objects.SO.SOInvoiceSiteStatusSelected.QtyLastSale : Edm.Decimal "Qty. Last Sales"
PX.Objects.SO.SOInvoiceSiteStatusSelected.LastSalesDate : Edm.DateTimeOffset "Last Sales Date"
PX.Objects.SO.SOInvoiceSiteStatusSelected.DropShipLastBaseQty : Edm.Decimal
PX.Objects.SO.SOInvoiceSiteStatusSelected.DropShipLastQty : Edm.Decimal "Qty. of Last Drop Ship"
PX.Objects.SO.SOInvoiceSiteStatusSelected.DropShipLastUnitPrice : Edm.Decimal
PX.Objects.SO.SOInvoiceSiteStatusSelected.DropShipCuryUnitPrice : Edm.Decimal "Unit Price of Last Drop Ship"
PX.Objects.SO.SOInvoiceSiteStatusSelected.DropShipLastDate : Edm.DateTimeOffset "Date of Last Drop Ship"
PX.Objects.SO.SOInvoiceSiteStatusSelected.NoteID : Edm.Guid
PX.Objects.SO.SOInvoiceSiteStatusSelected.ItemStatus : Edm.String
PX.Objects.SO.SOInvoiceSiteStatusSelected.Rank : Edm.Int32
PX.Objects.SO.SOInvoiceSiteStatusSelected.CombinedSearchString : Edm.String
PX.Objects.SO.SOInvoiceSiteStatusSelected.CuryRate : Edm.Decimal
PX.Objects.SO.SOInvoiceSiteStatusSelected.CuryViewState : Edm.Boolean
PX.Objects.SO.SOInvoiceSiteStatusSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.SO.SOInvoiceSiteStatusSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.SO.SOInvoiceSiteStatusSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.SO.SOInvoiceSiteStatusSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.SO.SOLine (EntityType)

Label: "Sales Order Line"
Key: LineNbr, OrderNbr, OrderType
Entity sets: PX_Objects_SO_SOLine, SalesOrderLine1, SOLine
Non-filterable, non-selectable: IsBeingCopied, IsKit, TranType, PlanType, RequireReasonCode, RequireShipping, RequireAllocation, RequireLocation, LineQtyAvail, LineQtyHardAvail, CalculateDiscountsOnImport, FreezeManualDisc, SkipDisc, AvgCost, NoteText, OrigIsSpecialOrder, POOrderStatus, POOrderType, POOrderNbr, POLineNbr, POLinkActive, IsPOLinkAllowed, ItemRequiresTerms, ItemHasResidual, IsCut, CuryID, CuryRate, CuryViewState

PX.Objects.SO.SOLine.BranchID : Edm.Int32 "Branch"
PX.Objects.SO.SOLine.OrderType : Edm.String [key] "Order Type"
PX.Objects.SO.SOLine.OrderNbr : Edm.String [key] "Order Nbr."
PX.Objects.SO.SOLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.SO.SOLine.SortOrder : Edm.Int32 "Line Order"
PX.Objects.SO.SOLine.Behavior : Edm.String
PX.Objects.SO.SOLine.DefaultOperation : Edm.String
PX.Objects.SO.SOLine.Operation : Edm.String "Operation"
PX.Objects.SO.SOLine.LineSign : Edm.Int16
PX.Objects.SO.SOLine.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.SO.SOLine.Completed : Edm.Boolean "Completed"
PX.Objects.SO.SOLine.OpenLine : Edm.Boolean "Open Line"
PX.Objects.SO.SOLine.IsBeingCopied : Edm.Boolean
PX.Objects.SO.SOLine.CustomerID : Edm.Int32
PX.Objects.SO.SOLine.OrderDate : Edm.DateTimeOffset
PX.Objects.SO.SOLine.CancelDate : Edm.DateTimeOffset "Cancel By"
PX.Objects.SO.SOLine.RequestDate : Edm.DateTimeOffset "Requested On"
PX.Objects.SO.SOLine.ShipDate : Edm.DateTimeOffset "Ship On"
PX.Objects.SO.SOLine.InvoiceType : Edm.String "Invoice Type"
PX.Objects.SO.SOLine.InvoiceNbr : Edm.String "Invoice Nbr."
PX.Objects.SO.SOLine.InvoiceLineNbr : Edm.Int32 "Invoice Line Nbr."
PX.Objects.SO.SOLine.InvoiceDate : Edm.DateTimeOffset "Original Sale Date"
PX.Objects.SO.SOLine.InvtMult : Edm.Int16 "Inventory Multiplier"
PX.Objects.SO.SOLine.ManualPrice : Edm.Boolean "Manual Price"
PX.Objects.SO.SOLine.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.SO.SOLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.SO.SOLine.LineType : Edm.String "Line Type"
PX.Objects.SO.SOLine.IsKit : Edm.Boolean "Kit"
PX.Objects.SO.SOLine.TranType : Edm.String
PX.Objects.SO.SOLine.PlanType : Edm.String
PX.Objects.SO.SOLine.OrigPlanType : Edm.String
PX.Objects.SO.SOLine.RequireReasonCode : Edm.Boolean
PX.Objects.SO.SOLine.RequireShipping : Edm.Boolean
PX.Objects.SO.SOLine.RequireAllocation : Edm.Boolean
PX.Objects.SO.SOLine.RequireLocation : Edm.Boolean
PX.Objects.SO.SOLine.LineQtyAvail : Edm.Decimal
PX.Objects.SO.SOLine.LineQtyHardAvail : Edm.Decimal
PX.Objects.SO.SOLine.OrigOrderType : Edm.String "Orig. Order Type"
PX.Objects.SO.SOLine.OrigOrderNbr : Edm.String "Orig. Order Nbr."
PX.Objects.SO.SOLine.OrigLineNbr : Edm.Int32
PX.Objects.SO.SOLine.OrigShipmentType : Edm.String
PX.Objects.SO.SOLine.UOM : Edm.String "UOM"
PX.Objects.SO.SOLine.InvoiceUOM : Edm.String
PX.Objects.SO.SOLine.ClosedQty : Edm.Decimal
PX.Objects.SO.SOLine.BaseClosedQty : Edm.Decimal
PX.Objects.SO.SOLine.OrderQty : Edm.Decimal [required] "Quantity"
PX.Objects.SO.SOLine.BaseOrderQty : Edm.Decimal [required] "Base Order Qty."
PX.Objects.SO.SOLine.VerifyOrderQty : Edm.Decimal
PX.Objects.SO.SOLine.UnassignedQty : Edm.Decimal [required]
PX.Objects.SO.SOLine.ShippedQty : Edm.Decimal [required] "Qty. On Shipments"
PX.Objects.SO.SOLine.BaseShippedQty : Edm.Decimal [required]
PX.Objects.SO.SOLine.OpenQty : Edm.Decimal [required] "Open Qty."
PX.Objects.SO.SOLine.BaseOpenQty : Edm.Decimal [required] "Base Open Qty."
PX.Objects.SO.SOLine.BilledQty : Edm.Decimal [required] "Billed Quantity"
PX.Objects.SO.SOLine.BaseBilledQty : Edm.Decimal [required]
PX.Objects.SO.SOLine.UnbilledQty : Edm.Decimal [required] "Unbilled Quantity"
PX.Objects.SO.SOLine.BaseUnbilledQty : Edm.Decimal [required]
PX.Objects.SO.SOLine.CompleteQtyMin : Edm.Decimal [required] "Undership Threshold (%)"
PX.Objects.SO.SOLine.CompleteQtyMax : Edm.Decimal [required] "Overship Threshold (%)"
PX.Objects.SO.SOLine.CuryInfoID : Edm.Int64
PX.Objects.SO.SOLine.PriceType : Edm.String "Price Type"
PX.Objects.SO.SOLine.IsPromotionalPrice : Edm.Boolean [required] "Promotional Price"
PX.Objects.SO.SOLine.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.SO.SOLine.UnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.SO.SOLine.UnitCost : Edm.Decimal
PX.Objects.SO.SOLine.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.SO.SOLine.CuryExtPrice : Edm.Decimal [required] "Ext. Price"
PX.Objects.SO.SOLine.ExtPrice : Edm.Decimal [required]
PX.Objects.SO.SOLine.CuryExtCost : Edm.Decimal [required] "Extended Cost"
PX.Objects.SO.SOLine.ExtCost : Edm.Decimal [required]
PX.Objects.SO.SOLine.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.SO.SOLine.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.SO.SOLine.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.SO.SOLine.AlternateID : Edm.String "Alternate ID"
PX.Objects.SO.SOLine.CommnPct : Edm.Decimal
PX.Objects.SO.SOLine.CuryCommnAmt : Edm.Decimal
PX.Objects.SO.SOLine.CommnAmt : Edm.Decimal
PX.Objects.SO.SOLine.TranDesc : Edm.String "Line Description"
PX.Objects.SO.SOLine.UnitWeigth : Edm.Decimal [required] "Unit Weight"
PX.Objects.SO.SOLine.UnitVolume : Edm.Decimal [required]
PX.Objects.SO.SOLine.ExtWeight : Edm.Decimal [required] "Ext. Weight"
PX.Objects.SO.SOLine.ExtVolume : Edm.Decimal [required] "Ext. Volume"
PX.Objects.SO.SOLine.IsFree : Edm.Boolean "Free Item"
PX.Objects.SO.SOLine.CalculateDiscountsOnImport : Edm.Boolean "Calculate automatic discounts on import"
PX.Objects.SO.SOLine.DiscPct : Edm.Decimal [required] "Discount Percent"
PX.Objects.SO.SOLine.CuryDiscAmt : Edm.Decimal [required] "Discount Amount"
PX.Objects.SO.SOLine.DiscAmt : Edm.Decimal [required]
PX.Objects.SO.SOLine.ManualDisc : Edm.Boolean "Manual Discount"
PX.Objects.SO.SOLine.FreezeManualDisc : Edm.Boolean
PX.Objects.SO.SOLine.SkipDisc : Edm.Boolean
PX.Objects.SO.SOLine.SkipLineDiscounts : Edm.Boolean [required] "Ignore Automatic Line Discounts"
PX.Objects.SO.SOLine.AutomaticDiscountsDisabled : Edm.Boolean [required] "Automatic Discounts Disabled"
PX.Objects.SO.SOLine.DisableAutomaticTaxCalculation : Edm.Boolean [required] "Disable Automatic Tax Calculation"
PX.Objects.SO.SOLine.CuryLineAmt : Edm.Decimal [required] "Amount"
PX.Objects.SO.SOLine.LineAmt : Edm.Decimal [required]
PX.Objects.SO.SOLine.CuryOpenAmt : Edm.Decimal [required] "Open Amount"
PX.Objects.SO.SOLine.OpenAmt : Edm.Decimal [required]
PX.Objects.SO.SOLine.CuryBilledAmt : Edm.Decimal [required]
PX.Objects.SO.SOLine.BilledAmt : Edm.Decimal [required]
PX.Objects.SO.SOLine.CuryUnbilledAmt : Edm.Decimal [required] "Unbilled Amount"
PX.Objects.SO.SOLine.UnbilledAmt : Edm.Decimal [required]
PX.Objects.SO.SOLine.CuryDiscPrice : Edm.Decimal "Disc. Unit Price"
PX.Objects.SO.SOLine.DiscPrice : Edm.Decimal
PX.Objects.SO.SOLine.GroupDiscountRate : Edm.Decimal [required]
PX.Objects.SO.SOLine.DocumentDiscountRate : Edm.Decimal [required]
PX.Objects.SO.SOLine.AvgCost : Edm.Decimal "Average Cost"
PX.Objects.SO.SOLine.ProjectID : Edm.Int32
PX.Objects.SO.SOLine.ReasonCode : Edm.String "Reason Code"
PX.Objects.SO.SOLine.SalesPersonID : Edm.Int32 "Salesperson ID"
PX.Objects.SO.SOLine.NoteID : Edm.Guid
PX.Objects.SO.SOLine.NoteText : Edm.String "Note Text"
PX.Objects.SO.SOLine.Commissionable : Edm.Boolean "Commissionable"
PX.Objects.SO.SOLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.SO.SOLine.CreatedByScreenID : Edm.String
PX.Objects.SO.SOLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.SO.SOLine.LastModifiedByScreenID : Edm.String
PX.Objects.SO.SOLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.SO.SOLine.tstamp : Edm.Binary
PX.Objects.SO.SOLine.AutoCreateIssueLine : Edm.Boolean "Auto Create Issue"
PX.Objects.SO.SOLine.IsLegacyDropShip : Edm.Boolean [required]
PX.Objects.SO.SOLine.DiscountID : Edm.String "Discount Code"
PX.Objects.SO.SOLine.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.SO.SOLine.POCreate : Edm.Boolean [required] "Mark for PO"
PX.Objects.SO.SOLine.OrigIsSpecialOrder : Edm.Boolean
PX.Objects.SO.SOLine.CostCenterID : Edm.Int32 [required]
PX.Objects.SO.SOLine.POSource : Edm.String "PO Source"
PX.Objects.SO.SOLine.POCreated : Edm.Boolean [required]
PX.Objects.SO.SOLine.POOrderStatus : Edm.String "Drop-Ship PO Status"
PX.Objects.SO.SOLine.POOrderType : Edm.String
PX.Objects.SO.SOLine.POOrderNbr : Edm.String "Drop-Ship PO Nbr."
PX.Objects.SO.SOLine.POLineNbr : Edm.Int32 "Drop-Ship PO Line Nbr."
PX.Objects.SO.SOLine.POLinkActive : Edm.Boolean "PO Linked"
PX.Objects.SO.SOLine.IsPOLinkAllowed : Edm.Boolean
PX.Objects.SO.SOLine.VendorID : Edm.Int32 "Vendor"
PX.Objects.SO.SOLine.DRTermStartDate : Edm.DateTimeOffset "Term Start Date"
PX.Objects.SO.SOLine.DRTermEndDate : Edm.DateTimeOffset "Term End Date"
PX.Objects.SO.SOLine.ItemRequiresTerms : Edm.Boolean
PX.Objects.SO.SOLine.ItemHasResidual : Edm.Boolean
PX.Objects.SO.SOLine.CuryUnitPriceDR : Edm.Decimal "Unit Price for DR"
PX.Objects.SO.SOLine.DiscPctDR : Edm.Decimal "Discount Percent for DR"
PX.Objects.SO.SOLine.DefScheduleID : Edm.Int32
PX.Objects.SO.SOLine.IsCut : Edm.Boolean
PX.Objects.SO.SOLine.IntercompanyPOLineNbr : Edm.Int32
PX.Objects.SO.SOLine.SubstitutionRequired : Edm.Boolean [required] "Substitution Required"
PX.Objects.SO.SOLine.BlanketType : Edm.String
PX.Objects.SO.SOLine.BlanketNbr : Edm.String "Blanket SO Ref. Nbr."
PX.Objects.SO.SOLine.BlanketLineNbr : Edm.Int32
PX.Objects.SO.SOLine.BlanketSplitLineNbr : Edm.Int32
PX.Objects.SO.SOLine.QtyOnOrders : Edm.Decimal [required] "Qty. On Orders"
PX.Objects.SO.SOLine.BaseQtyOnOrders : Edm.Decimal [required]
PX.Objects.SO.SOLine.CustomerOrderNbr : Edm.String "Customer Order Nbr."
PX.Objects.SO.SOLine.SchedOrderDate : Edm.DateTimeOffset "Sched. Order Date"
PX.Objects.SO.SOLine.ChildLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOLine.OpenChildLineCntr : Edm.Int32 [required]
PX.Objects.SO.SOLine.Cancelled : Edm.Boolean [required]
PX.Objects.SO.SOLine.RelatedDocumentType : Edm.String "Related Document Type"
PX.Objects.SO.SOLine.RelatedDocumentID : Edm.Guid "Related Document"
PX.Objects.SO.SOLine.RelatedDocumentLineNbr : Edm.Int32 "Related Document Detail Line Nbr."
PX.Objects.SO.SOLine.CuryTaxableAmt : Edm.Decimal [required]
PX.Objects.SO.SOLine.TaxableAmt : Edm.Decimal [required]
PX.Objects.SO.SOLine.IncludedInMarginCalc : Edm.Boolean [required]
PX.Objects.SO.SOLine.CuryNetSales : Edm.Decimal [required]
PX.Objects.SO.SOLine.NetSales : Edm.Decimal [required]
PX.Objects.SO.SOLine.CuryMarginAmt : Edm.Decimal "Est. Margin Amount"
PX.Objects.SO.SOLine.MarginAmt : Edm.Decimal
PX.Objects.SO.SOLine.MarginPct : Edm.Decimal "Est. Margin (%)"
PX.Objects.SO.SOLine.OrchestrationOriginalLineNbr : Edm.Int32
PX.Objects.SO.SOLine.OrchestrationOriginalSiteID : Edm.Int32
PX.Objects.SO.SOLine.CuryID : Edm.String "Currency"
PX.Objects.SO.SOLine.CuryRate : Edm.Decimal
PX.Objects.SO.SOLine.CuryViewState : Edm.Boolean
PX.Objects.SO.SOLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.SO.SOLine.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.SO.SOLine.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.SO.SOLine.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.SO.SOLine.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.SO.SOLine.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.SO.SOLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.SO.SOLine.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOLine.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.SO.SOLine.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.SO.SOLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.SO.SOLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.SO.SOLine.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.SO.SOLine.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.SO.SOLine.SOOrchestrationPlanByOrchestrationPlanID -> PX.Objects.SO.SOOrchestrationPlan
PX.Objects.SO.SOLine.SOOrderSiteBySiteID -> PX.Objects.SO.SOOrderSite (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.SO.SOLine.SOOrderTypeByOrderType -> PX.Objects.SO.SOOrderType (OrderType=OrderType)
PX.Objects.SO.SOLine.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (OrderType=OrderType, Operation=Operation)
PX.Objects.SO.SOLine.SOOrderTypeOperationByOrderType -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation, OrderType=OrderType)
PX.Objects.SO.SOLine.SOSalesPerTranBySalesPersonID -> PX.Objects.SO.SOSalesPerTran (OrderType=OrderType, OrderNbr=OrderNbr, SalesPersonID=SalespersonID)
PX.Objects.SO.SOLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.SO.SOLine.DRScheduleByDefScheduleID -> PX.Objects.DR.DRSchedule (DefScheduleID=ScheduleID)
PX.Objects.SO.SOLine.CarrierByShipVia -> PX.Objects.CS.Carrier
PX.Objects.SO.SOLine.FOBPointByFOBPoint -> PX.Objects.CS.FOBPoint
PX.Objects.SO.SOLine.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.SO.SOLine.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone
PX.Objects.SO.SOLine.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms
PX.Objects.SO.SOLine.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOLine.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.SO.SOLine.INSiteByPOSiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOLine.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.SO.SOLine.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.SO.SOLine.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.SO.SOLine.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.SO.SOLine.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.SO.SOLine.LocationByCustomerLocationID -> PX.Objects.CR.Location
PX.Objects.SO.SOLine.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.SO.SOLine.ARTranByInvoiceLineNbr -> PX.Objects.AR.ARTran (InvoiceType=TranType, InvoiceNbr=RefNbr, InvoiceLineNbr=LineNbr)
PX.Objects.SO.SOLine.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.SO.SOLine.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.SO.SOLine.SOInvoiceByInvoiceNbr -> PX.Objects.SO.SOInvoice (InvoiceType=DocType, InvoiceNbr=RefNbr)
PX.Objects.SO.SOLine.INLotSerialStatusByCostCenterByCostCenterID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.SO.SOLine.INSiteStatusByCostCenterByCostCenterID -> PX.Objects.IN.INSiteStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.SO.SOLine.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.SO.SOLine.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.SO.SOLine.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.SO.SOLine.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.SO.SOLine.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.SO.SOLine.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.SO.SOLine.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.SO.SOLine.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.SO.SOLine.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.SO.SOLine.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.SO.SOLine.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.SO.SOLine.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.SO.SOLine.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.SO.SOLine.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.SO.SOLine.INTransitLineCollection -> Collection(PX.Objects.IN.INTransitLine)
PX.Objects.SO.SOLine.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.SO.SOLine.DropShipLinkCollection -> Collection(PX.Objects.Common.DAC.DropShipLink)
PX.Objects.SO.SOLine.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.SO.SOLine.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.SO.SOLine.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
