<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# PX.Objects.CR.CRValidationRules (EntityType)

Label: "Duplicate Validation Rules"
Key: NoteID
Entity sets: PX_Objects_CR_CRValidationRules, DuplicateValidationRules, CRValidationRules
Non-filterable, non-selectable: NoteText

PX.Objects.CR.CRValidationRules.ValidationType : Edm.String "Validation Type"
PX.Objects.CR.CRValidationRules.MatchingEntity : Edm.String "Matching Entity"
PX.Objects.CR.CRValidationRules.MatchingField : Edm.String "Matching Field"
PX.Objects.CR.CRValidationRules.MatchingFieldUI : Edm.String "Matching Field"
PX.Objects.CR.CRValidationRules.ScoreWeight : Edm.Decimal [required] "Score Weight"
PX.Objects.CR.CRValidationRules.TransformationRule : Edm.String "Transformation Rule"
PX.Objects.CR.CRValidationRules.CreateOnEntry : Edm.String "Create on Entry"
PX.Objects.CR.CRValidationRules.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRValidationRules.CreatedByScreenID : Edm.String
PX.Objects.CR.CRValidationRules.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRValidationRules.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRValidationRules.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRValidationRules.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRValidationRules.tstamp : Edm.Binary
PX.Objects.CR.CRValidationRules.NoteID : Edm.Guid [key]
PX.Objects.CR.CRValidationRules.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRValidationRules.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRValidationRules.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CR.DAC.CRNotification (EntityType)

Label: "CR Notification"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_CR_DAC_CRNotification, CRNotification

# PX.Objects.CR.DAC.Standalone.CRCampaign (EntityType)

Label: "Campaign Statistics"
Key: CampaignID
Entity sets: PX_Objects_CR_DAC_Standalone_CRCampaign, CampaignStatistics, CRCampaign1
Non-filterable, non-selectable: NoteText

PX.Objects.CR.DAC.Standalone.CRCampaign.CampaignID : Edm.String [key] "Campaign ID"
PX.Objects.CR.DAC.Standalone.CRCampaign.CampaignName : Edm.String "Campaign Name"
PX.Objects.CR.DAC.Standalone.CRCampaign.LeadsGenerated : Edm.Int32 "Leads Generated"
PX.Objects.CR.DAC.Standalone.CRCampaign.LeadsConverted : Edm.Int32 "Leads Converted"
PX.Objects.CR.DAC.Standalone.CRCampaign.Contacts : Edm.Int32 "Total Members"
PX.Objects.CR.DAC.Standalone.CRCampaign.MembersContacted : Edm.Int32 "Members Contacted"
PX.Objects.CR.DAC.Standalone.CRCampaign.MembersResponded : Edm.Int32 "Members Responded"
PX.Objects.CR.DAC.Standalone.CRCampaign.Opportunities : Edm.Int32 "Opportunities"
PX.Objects.CR.DAC.Standalone.CRCampaign.ClosedOpportunities : Edm.Int32 "Won Opportunities"
PX.Objects.CR.DAC.Standalone.CRCampaign.OpportunitiesValue : Edm.Decimal "Opportunities Value"
PX.Objects.CR.DAC.Standalone.CRCampaign.ClosedOpportunitiesValue : Edm.Decimal "Won Opportunities Value"
PX.Objects.CR.DAC.Standalone.CRCampaign.LeadsGeneratedClosedOpportunities : Edm.Int32 "Generated Leads Converted to Won Opportunities"
PX.Objects.CR.DAC.Standalone.CRCampaign.NoteID : Edm.Guid
PX.Objects.CR.DAC.Standalone.CRCampaign.NoteText : Edm.String "Note Text"
PX.Objects.CR.DAC.Standalone.CRCampaign.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.CR.DAC.Standalone.CRCampaign.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.CR.DAC.Standalone.CRCampaign.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.CR.DAC.Standalone.CRCampaign.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CR.DAC.Standalone.CRCampaign.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CR.DAC.Standalone.CRCampaign.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.CR.DAC.Standalone.CRCampaign.CRCampaignTypeByCampaignType -> PX.Objects.CR.CRCampaignType
PX.Objects.CR.DAC.Standalone.CRCampaign.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CR.DAC.Standalone.CRCampaign.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CR.DAC.Standalone.CRCampaign.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CR.DAC.Standalone.CRCampaign.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CR.DAC.Standalone.CRCampaign.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.CR.DAC.Standalone.CRCampaign.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.CR.DAC.Standalone.CRCampaign.CRCampaignMembersCollection -> Collection(PX.Objects.CR.CRCampaignMembers)
PX.Objects.CR.DAC.Standalone.CRCampaign.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CR.DAC.Standalone.CRCampaign.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.DAC.Standalone.CRCampaign.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CR.DAC.Standalone.CRCampaign.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CR.DAC.Standalone.CRCampaign.CRCampaignToCRMarketingListLinkCollection -> Collection(PX.Objects.CR.CRCampaignToCRMarketingListLink)

# PX.Objects.CR.Inquiry.CRSMEmail (EntityType)

Label: "Email Activity"
BaseType: PX.Objects.CR.CRSMEmail
Key: NoteID (inherited from PX.Objects.CR.CRActivity)
Entity sets: PX_Objects_CR_Inquiry_CRSMEmail, EmailActivity1, CRSMEmail1

# PX.Objects.CR.Location (EntityType)

Label: "Location"
Key: BAccountID, LocationCD
Entity sets: PX_Objects_CR_Location, Location
Non-filterable, non-selectable: NoteText, IsARAccountSameAsMain, OverrideRemitAddress, IsRemitAddressSameAsMain, OverrideRemitContact, IsRemitContactSameAsMain, IsAPAccountSameAsMain, IsAPPaymentInfoSameAsMain, IsAddressSameAsMain, OverrideAddress, IsContactSameAsMain, OverrideContact

PX.Objects.CR.Location.BAccountID : Edm.Int32 [key] "Account ID"
PX.Objects.CR.Location.LocationID : Edm.Int32 "LocationID"
PX.Objects.CR.Location.LocationCD : Edm.String [key] "Location ID"
PX.Objects.CR.Location.LocType : Edm.String "Location Type"
PX.Objects.CR.Location.Descr : Edm.String "Location Name"
PX.Objects.CR.Location.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.CR.Location.DefAddressID : Edm.Int32 "Default Address"
PX.Objects.CR.Location.DefContactID : Edm.Int32 "Default Contact"
PX.Objects.CR.Location.NoteID : Edm.Guid
PX.Objects.CR.Location.NoteText : Edm.String "Note Text"
PX.Objects.CR.Location.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CR.Location.Status : Edm.String "Status"
PX.Objects.CR.Location.IsDefault : Edm.Boolean "Default"
PX.Objects.CR.Location.CTaxZoneID : Edm.String "Tax Zone"
PX.Objects.CR.Location.CTaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.Location.CAvalaraExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.CR.Location.CAvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.CR.Location.CCarrierID : Edm.String "Ship Via"
PX.Objects.CR.Location.CShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.Location.CShipZoneID : Edm.String "Shipping Zone"
PX.Objects.CR.Location.CFOBPointID : Edm.String "FOB Point"
PX.Objects.CR.Location.CResedential : Edm.Boolean [required] "Residential Delivery"
PX.Objects.CR.Location.CAdditionalHandling : Edm.Boolean [required] "Additional Handling"
PX.Objects.CR.Location.CLiftGate : Edm.Boolean [required] "Lift Gate"
PX.Objects.CR.Location.CInsideDelivery : Edm.Boolean [required] "Inside Delivery"
PX.Objects.CR.Location.CLimitedAccess : Edm.Boolean [required] "Limited Access"
PX.Objects.CR.Location.CSaturdayDelivery : Edm.Boolean [required] "Saturday Delivery"
PX.Objects.CR.Location.CGroundCollect : Edm.Boolean [required] "Ground Collect"
PX.Objects.CR.Location.CInsurance : Edm.Boolean [required] "Insurance"
PX.Objects.CR.Location.CLeadTime : Edm.Int16 "Lead Time (Days)"
PX.Objects.CR.Location.CPriceClassID : Edm.String "Price Class"
PX.Objects.CR.Location.CSiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.Location.CShipComplete : Edm.String "Shipping Rule"
PX.Objects.CR.Location.COrderPriority : Edm.Int16 "Order Priority"
PX.Objects.CR.Location.CCalendarID : Edm.String "Calendar"
PX.Objects.CR.Location.CARAccountLocationID : Edm.Int32
PX.Objects.CR.Location.IsARAccountSameAsMain : Edm.Boolean "Same As Default Location's"
PX.Objects.CR.Location.VTaxZoneID : Edm.String "Tax Zone"
PX.Objects.CR.Location.VTaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.Location.VCarrierID : Edm.String "Ship Via"
PX.Objects.CR.Location.VShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.Location.VFOBPointID : Edm.String "FOB Point"
PX.Objects.CR.Location.VLeadTime : Edm.Int16 "Lead Time (Days)"
PX.Objects.CR.Location.VRcptQtyMin : Edm.Decimal [required] "Min. Receipt (%)"
PX.Objects.CR.Location.VRcptQtyMax : Edm.Decimal [required] "Max. Receipt (%)"
PX.Objects.CR.Location.VRcptQtyThreshold : Edm.Decimal [required] "Threshold Receipt (%)"
PX.Objects.CR.Location.VRcptQtyAction : Edm.String "Receipt Action"
PX.Objects.CR.Location.VSiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.Location.VSiteIDIsNull : Edm.Int16
PX.Objects.CR.Location.VPrintOrder : Edm.Boolean [required] "Print Order"
PX.Objects.CR.Location.VEmailOrder : Edm.Boolean [required] "Email Order"
PX.Objects.CR.Location.VAPAccountLocationID : Edm.Int32
PX.Objects.CR.Location.VPaymentInfoLocationID : Edm.Int32
PX.Objects.CR.Location.OverrideRemitAddress : Edm.Boolean "Override"
PX.Objects.CR.Location.IsRemitAddressSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.Location.VRemitAddressID : Edm.Int32
PX.Objects.CR.Location.OverrideRemitContact : Edm.Boolean "Override"
PX.Objects.CR.Location.IsRemitContactSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.Location.VRemitContactID : Edm.Int32
PX.Objects.CR.Location.VPaymentMethodID : Edm.String "Payment Method"
PX.Objects.CR.Location.VPaymentLeadTime : Edm.Int16 "Payment Lead Time (Days)"
PX.Objects.CR.Location.VPaymentByType : Edm.Int32 [required] "Payment By"
PX.Objects.CR.Location.VSeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.CR.Location.VPrepaymentPct : Edm.Decimal [required] "Prepayment Percent"
PX.Objects.CR.Location.VAllowAPBillBeforeReceipt : Edm.Boolean [required] "Allow AP Bill Before Receipt"
PX.Objects.CR.Location.IsAPAccountSameAsMain : Edm.Boolean "Same As Default Location's"
PX.Objects.CR.Location.IsAPPaymentInfoSameAsMain : Edm.Boolean "Same As Default Location's"
PX.Objects.CR.Location.LocationAPAccountSubBAccountID : Edm.Int32
PX.Objects.CR.Location.LocationARAccountSubBAccountID : Edm.Int32
PX.Objects.CR.Location.LocationAPPaymentInfoBAccountID : Edm.Int32
PX.Objects.CR.Location.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.CR.Location.PaymentLeadTime : Edm.Int16 "Payment Lead Time (Days)"
PX.Objects.CR.Location.SeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.CR.Location.PaymentByType : Edm.Int32 "Payment By"
PX.Objects.CR.Location.BAccountBAccountID : Edm.Int32
PX.Objects.CR.Location.VDefAddressID : Edm.Int32
PX.Objects.CR.Location.VDefContactID : Edm.Int32
PX.Objects.CR.Location.CMPSiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.Location.ExtRefNbr : Edm.String "External ID"
PX.Objects.CR.Location.tstamp : Edm.Binary
PX.Objects.CR.Location.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.Location.CreatedByScreenID : Edm.String
PX.Objects.CR.Location.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.Location.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.Location.LastModifiedByScreenID : Edm.String
PX.Objects.CR.Location.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.Location.IsAddressSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.Location.OverrideAddress : Edm.Boolean "Override"
PX.Objects.CR.Location.IsContactSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.Location.OverrideContact : Edm.Boolean "Override"
PX.Objects.CR.Location.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CR.Location.ContactByDefContactID -> PX.Objects.CR.Contact (DefContactID=ContactID)
PX.Objects.CR.Location.ContactByVRemitContactID -> PX.Objects.CR.Contact (VRemitContactID=ContactID)
PX.Objects.CR.Location.AddressByDefAddressID -> PX.Objects.CR.Address (DefAddressID=AddressID)
PX.Objects.CR.Location.AddressByVRemitAddressID -> PX.Objects.CR.Address (VRemitAddressID=AddressID)
PX.Objects.CR.Location.BranchByCBranchID -> PX.Objects.GL.Branch
PX.Objects.CR.Location.BranchByVBranchID -> PX.Objects.GL.Branch
PX.Objects.CR.Location.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.Location.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.Location.TaxZoneByCTaxZoneID -> PX.Objects.TX.TaxZone (CTaxZoneID=TaxZoneID)
PX.Objects.CR.Location.TaxZoneByVTaxZoneID -> PX.Objects.TX.TaxZone (VTaxZoneID=TaxZoneID)
PX.Objects.CR.Location.CarrierByCCarrierID -> PX.Objects.CS.Carrier (CCarrierID=CarrierID)
PX.Objects.CR.Location.CarrierByVCarrierID -> PX.Objects.CS.Carrier (VCarrierID=CarrierID)
PX.Objects.CR.Location.FOBPointByCFOBPointID -> PX.Objects.CS.FOBPoint (CFOBPointID=FOBPointID)
PX.Objects.CR.Location.FOBPointByVFOBPointID -> PX.Objects.CS.FOBPoint (VFOBPointID=FOBPointID)
PX.Objects.CR.Location.ShippingZoneByCShipZoneID -> PX.Objects.CS.ShippingZone (CShipZoneID=ZoneID)
PX.Objects.CR.Location.ShipTermsByCShipTermsID -> PX.Objects.CS.ShipTerms (CShipTermsID=ShipTermsID)
PX.Objects.CR.Location.ShipTermsByVShipTermsID -> PX.Objects.CS.ShipTerms (VShipTermsID=ShipTermsID)
PX.Objects.CR.Location.INSiteByCSiteID -> PX.Objects.IN.INSite (CSiteID=SiteID)
PX.Objects.CR.Location.INSiteByVSiteID -> PX.Objects.IN.INSite (VSiteID=SiteID)
PX.Objects.CR.Location.INSiteByCMPSiteID -> PX.Objects.IN.INSite (CMPSiteID=SiteID)
PX.Objects.CR.Location.AccountByCSalesAcctID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByCDiscountAcctID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByCRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByCFreightAcctID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByCARAccountID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByVExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByVRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByVFreightAcctID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByVDiscountAcctID -> PX.Objects.GL.Account
PX.Objects.CR.Location.AccountByVAPAccountID -> PX.Objects.GL.Account
PX.Objects.CR.Location.SubByCSalesSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCFreightSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCARSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByVExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByVRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByVFreightSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByVDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByVAPSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCMPSalesSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCMPExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCMPFreightSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCMPDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.SubByCMPGainLossSubID -> PX.Objects.GL.Sub
PX.Objects.CR.Location.CashAccountByVBranchID -> PX.Objects.CA.CashAccount
PX.Objects.CR.Location.PaymentMethodByVPaymentMethodID -> PX.Objects.CA.PaymentMethod (VPaymentMethodID=PaymentMethodID)
PX.Objects.CR.Location.ARPriceClassByCPriceClassID -> PX.Objects.AR.ARPriceClass (CPriceClassID=PriceClassID)
PX.Objects.CR.Location.CSCalendarByCCalendarID -> PX.Objects.CS.CSCalendar (CCalendarID=CalendarID)
PX.Objects.CR.Location.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CR.Location.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.CR.Location.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CR.Location.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CR.Location.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CR.Location.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CR.Location.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CR.Location.FSAppointmentInRouteCollection -> Collection(PX.Objects.FS.FSAppointmentInRoute)
PX.Objects.CR.Location.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CR.Location.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.CR.Location.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.CR.Location.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CR.Location.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CR.Location.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.CR.Location.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.CR.Location.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CR.Location.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.CR.Location.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CR.Location.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CR.Location.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.CR.Location.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.Objects.CR.Location.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CR.Location.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.CR.Location.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CR.Location.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CR.Location.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CR.Location.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CR.Location.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.CR.Location.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.CR.Location.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CR.Location.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.CR.Location.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.CR.Location.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CR.Location.AppointmentToPostCollection -> Collection(PX.Objects.FS.AppointmentToPost)
PX.Objects.CR.Location.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.CR.Location.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.CR.Location.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.CR.Location.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.CR.Location.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CR.Location.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.Objects.CR.Location.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.CR.Location.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.CR.Location.VendorPaymentMethodDetailCollection -> Collection(PX.Objects.AP.VendorPaymentMethodDetail)
PX.Objects.CR.Location.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.CR.Location.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CR.Location.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.CR.Location.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.CR.Location.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.CR.Location.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CR.Location.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)
PX.Objects.CR.Location.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.Objects.CR.Location.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.CR.Location.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.CR.Location.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CR.Location.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CR.Location.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CR.Location.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CR.Location.PMUnionCollection -> Collection(PX.Objects.PM.PMUnion)
PX.Objects.CR.Location.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.CR.Location.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.CR.Location.CarrierPluginCustomerCollection -> Collection(PX.Objects.CS.CarrierPluginCustomer)
PX.Objects.CR.Location.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.CR.Location.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.CR.Location.LocationBranchSettingsCollection -> Collection(PX.Objects.CR.LocationBranchSettings)
PX.Objects.CR.Location.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CR.Location.APDiscountLocationCollection -> Collection(PX.Objects.AP.APDiscountLocation)
PX.Objects.CR.Location.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.Objects.CR.Location.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.CR.Location.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.Objects.CR.Location.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.CR.Location.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.CR.Location.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CR.Location.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.CR.Location.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CR.Location.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.CR.Location.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.CR.Location.SVServiceLocationCustomerCollection -> Collection(PX.Objects.SV.SVServiceLocationCustomer)
PX.Objects.CR.Location.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.Location.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CR.Location.BCRoleAssignmentCollection -> Collection(PX.Commerce.Shopify.BCRoleAssignment)
PX.Objects.CR.Location.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.CR.Location.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.CR.Location.BAccountLocationCollection -> Collection(PX.Objects.FS.BAccountLocation)
PX.Objects.CR.Location.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.Objects.CR.Location.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.CR.Location.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.CR.Location.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.CR.Location.AMBomOperCuryCollection -> Collection(PX.Objects.AM.AMBomOperCury)
PX.Objects.CR.Location.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)

# PX.Objects.CR.LocationARAccountSub (EntityType)

Label: "Location GL Accounts"
Key: BAccountID, LocationID
Entity sets: PX_Objects_CR_LocationARAccountSub, LocationGLAccounts1, LocationARAccountSub

PX.Objects.CR.LocationARAccountSub.BAccountID : Edm.Int32 [key]
PX.Objects.CR.LocationARAccountSub.LocationID : Edm.Int32 [key]
PX.Objects.CR.LocationARAccountSub.CARAccountLocationID : Edm.Int32
PX.Objects.CR.LocationARAccountSub.SubByCARSubID -> PX.Objects.GL.Sub
PX.Objects.CR.LocationARAccountSub.SubByCRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.CR.LocationARAccountSub.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)

# PX.Objects.CR.LocationBranchSettings (EntityType)

Label: "Location Settings for Current Branch"
Key: BAccountID, BranchID, LocationID
Entity sets: PX_Objects_CR_LocationBranchSettings, LocationSettingsforCurrentBranch, LocationBranchSettings

PX.Objects.CR.LocationBranchSettings.BAccountID : Edm.Int32 [key]
PX.Objects.CR.LocationBranchSettings.LocationID : Edm.Int32 [key]
PX.Objects.CR.LocationBranchSettings.BranchID : Edm.Int32 [key]
PX.Objects.CR.LocationBranchSettings.tstamp : Edm.Binary
PX.Objects.CR.LocationBranchSettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.LocationBranchSettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.LocationBranchSettings.CreatedByScreenID : Edm.String
PX.Objects.CR.LocationBranchSettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.LocationBranchSettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.LocationBranchSettings.LastModifiedByScreenID : Edm.String
PX.Objects.CR.LocationBranchSettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.LocationBranchSettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.LocationBranchSettings.INSiteByVSiteID -> PX.Objects.IN.INSite
PX.Objects.CR.LocationBranchSettings.LocationByLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID, LocationID=LocationID)

# PX.Objects.CR.LocationExtAddress (EntityType)

Label: "Location with Address"
BaseType: PX.Objects.CR.Address
Key: AddressID (inherited from PX.Objects.CR.Address)
Entity sets: PX_Objects_CR_LocationExtAddress, LocationwithAddress, LocationExtAddress
Non-filterable, non-selectable: IsARAccountSameAsMain, IsAPAccountSameAsMain, IsAddressSameAsMain, IsContactSameAsMain

PX.Objects.CR.LocationExtAddress.LocationBAccountID : Edm.Int32 "Business Account ID"
PX.Objects.CR.LocationExtAddress.LocationID : Edm.Int32 "LocationID"
PX.Objects.CR.LocationExtAddress.LocationCD : Edm.String "Location ID"
PX.Objects.CR.LocationExtAddress.LocType : Edm.String "Location Type"
PX.Objects.CR.LocationExtAddress.Descr : Edm.String "Location Name"
PX.Objects.CR.LocationExtAddress.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.CR.LocationExtAddress.DefAddressID : Edm.Int32 "Default Address"
PX.Objects.CR.LocationExtAddress.DefContactID : Edm.Int32
PX.Objects.CR.LocationExtAddress.IsActive : Edm.Boolean "Active"
PX.Objects.CR.LocationExtAddress.CTaxZoneID : Edm.String "Tax Zone"
PX.Objects.CR.LocationExtAddress.CTaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.LocationExtAddress.CAvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.CR.LocationExtAddress.CCarrierID : Edm.String "Ship Via"
PX.Objects.CR.LocationExtAddress.CShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.LocationExtAddress.CShipZoneID : Edm.String "Shipping Zone"
PX.Objects.CR.LocationExtAddress.CFOBPointID : Edm.String "Shipping Zone ID"
PX.Objects.CR.LocationExtAddress.CResedential : Edm.Boolean "Residential Delivery"
PX.Objects.CR.LocationExtAddress.CAdditionalHandling : Edm.Boolean "Additional Handling"
PX.Objects.CR.LocationExtAddress.CLiftGate : Edm.Boolean "Lift Gate"
PX.Objects.CR.LocationExtAddress.CInsideDelivery : Edm.Boolean "Inside Delivery"
PX.Objects.CR.LocationExtAddress.CLimitedAccess : Edm.Boolean "Limited Access"
PX.Objects.CR.LocationExtAddress.CSaturdayDelivery : Edm.Boolean "Saturday Delivery"
PX.Objects.CR.LocationExtAddress.CGroundCollect : Edm.Boolean "Ground Collect"
PX.Objects.CR.LocationExtAddress.CInsurance : Edm.Boolean "Insurance"
PX.Objects.CR.LocationExtAddress.CLeadTime : Edm.Int16 "Lead Time (Days)"
PX.Objects.CR.LocationExtAddress.CPriceClassID : Edm.String "Price Class ID"
PX.Objects.CR.LocationExtAddress.CSiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.LocationExtAddress.CShipComplete : Edm.String "Shipping Rule"
PX.Objects.CR.LocationExtAddress.COrderPriority : Edm.Int16 "Order Priority"
PX.Objects.CR.LocationExtAddress.CARAccountLocationID : Edm.Int32
PX.Objects.CR.LocationExtAddress.IsARAccountSameAsMain : Edm.Boolean
PX.Objects.CR.LocationExtAddress.VTaxZoneID : Edm.String "Tax Zone ID"
PX.Objects.CR.LocationExtAddress.VTaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.LocationExtAddress.VCarrierID : Edm.String "Ship Via"
PX.Objects.CR.LocationExtAddress.VShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.LocationExtAddress.VFOBPointID : Edm.String "FOB Point"
PX.Objects.CR.LocationExtAddress.VLeadTime : Edm.Int16 "Lead Time (Days)"
PX.Objects.CR.LocationExtAddress.VRcptQtyMin : Edm.Decimal "Min. Receipt (%)"
PX.Objects.CR.LocationExtAddress.VRcptQtyMax : Edm.Decimal "Max. Receipt (%)"
PX.Objects.CR.LocationExtAddress.VRcptQtyThreshold : Edm.Decimal "Threshold Receipt (%)"
PX.Objects.CR.LocationExtAddress.VRcptQtyAction : Edm.String "Receipt Action"
PX.Objects.CR.LocationExtAddress.VSiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.LocationExtAddress.VPrintOrder : Edm.Boolean "Print Orders"
PX.Objects.CR.LocationExtAddress.VEmailOrder : Edm.Boolean "Send Orders by Email"
PX.Objects.CR.LocationExtAddress.VAPAccountLocationID : Edm.Int32
PX.Objects.CR.LocationExtAddress.VPaymentInfoLocationID : Edm.Int32
PX.Objects.CR.LocationExtAddress.VRemitAddressID : Edm.Int32
PX.Objects.CR.LocationExtAddress.VRemitContactID : Edm.Int32
PX.Objects.CR.LocationExtAddress.VPaymentMethodID : Edm.String "Payment Method"
PX.Objects.CR.LocationExtAddress.VPaymentLeadTime : Edm.Int16 "Payment Lead Time (Days)"
PX.Objects.CR.LocationExtAddress.VPaymentByType : Edm.Int32 "Payment By"
PX.Objects.CR.LocationExtAddress.VSeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.CR.LocationExtAddress.VPrepaymentPct : Edm.Decimal "Prepayment Percent"
PX.Objects.CR.LocationExtAddress.VAllowAPBillBeforeReceipt : Edm.Boolean "Allow AP Bill Before Receipt"
PX.Objects.CR.LocationExtAddress.IsAPAccountSameAsMain : Edm.Boolean
PX.Objects.CR.LocationExtAddress.BAccountBAccountID : Edm.Int32
PX.Objects.CR.LocationExtAddress.VDefAddressID : Edm.Int32
PX.Objects.CR.LocationExtAddress.VDefContactID : Edm.Int32
PX.Objects.CR.LocationExtAddress.CMPSiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.LocationExtAddress.LocationCreatedByID : Edm.Guid "Created By"
PX.Objects.CR.LocationExtAddress.LocationCreatedByScreenID : Edm.String
PX.Objects.CR.LocationExtAddress.LocationCreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.LocationExtAddress.LocationLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.LocationExtAddress.LocationLastModifiedByScreenID : Edm.String
PX.Objects.CR.LocationExtAddress.LocationLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.LocationExtAddress.IsAddressSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.LocationExtAddress.IsContactSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.LocationExtAddress.TaxZoneByCTaxZoneID -> PX.Objects.TX.TaxZone (CTaxZoneID=TaxZoneID)
PX.Objects.CR.LocationExtAddress.TaxZoneByVTaxZoneID -> PX.Objects.TX.TaxZone (VTaxZoneID=TaxZoneID)
PX.Objects.CR.LocationExtAddress.CarrierByCCarrierID -> PX.Objects.CS.Carrier (CCarrierID=CarrierID)
PX.Objects.CR.LocationExtAddress.CarrierByVCarrierID -> PX.Objects.CS.Carrier (VCarrierID=CarrierID)
PX.Objects.CR.LocationExtAddress.FOBPointByCFOBPointID -> PX.Objects.CS.FOBPoint (CFOBPointID=FOBPointID)
PX.Objects.CR.LocationExtAddress.FOBPointByVFOBPointID -> PX.Objects.CS.FOBPoint (VFOBPointID=FOBPointID)
PX.Objects.CR.LocationExtAddress.ShippingZoneByCShipZoneID -> PX.Objects.CS.ShippingZone (CShipZoneID=ZoneID)
PX.Objects.CR.LocationExtAddress.ShipTermsByCShipTermsID -> PX.Objects.CS.ShipTerms (CShipTermsID=ShipTermsID)
PX.Objects.CR.LocationExtAddress.ShipTermsByVShipTermsID -> PX.Objects.CS.ShipTerms (VShipTermsID=ShipTermsID)
PX.Objects.CR.LocationExtAddress.INSiteByCSiteID -> PX.Objects.IN.INSite (CSiteID=SiteID)
PX.Objects.CR.LocationExtAddress.INSiteByVSiteID -> PX.Objects.IN.INSite (VSiteID=SiteID)
PX.Objects.CR.LocationExtAddress.INSiteByCMPSiteID -> PX.Objects.IN.INSite (CMPSiteID=SiteID)
PX.Objects.CR.LocationExtAddress.PaymentMethodByVPaymentMethodID -> PX.Objects.CA.PaymentMethod (VPaymentMethodID=PaymentMethodID)
PX.Objects.CR.LocationExtAddress.ARPriceClassByCPriceClassID -> PX.Objects.AR.ARPriceClass (CPriceClassID=PriceClassID)
PX.Objects.CR.LocationExtAddress.ContactByDefContactID -> PX.Objects.CR.Contact (DefContactID=ContactID)
PX.Objects.CR.LocationExtAddress.ContactByVRemitContactID -> PX.Objects.CR.Contact (VRemitContactID=ContactID)
PX.Objects.CR.LocationExtAddress.AddressByDefAddressID -> PX.Objects.CR.Address (DefAddressID=AddressID)
PX.Objects.CR.LocationExtAddress.AddressByVRemitAddressID -> PX.Objects.CR.Address (VRemitAddressID=AddressID)

# PX.Objects.CR.PMCRActivity (EntityType)

Label: "Activity"
BaseType: PX.Objects.CR.CRPMTimeActivity
Key: NoteID (inherited from PX.Objects.CR.CRActivity)
Entity sets: PX_Objects_CR_PMCRActivity
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.CR.PMCRActivity.DisplayStatus : Edm.String "Status"

# PX.Objects.CR.PMTimeActivity (EntityType)

Label: "Time Activity"
Key: NoteID
Entity sets: PX_Objects_CR_PMTimeActivity, TimeActivity, PMTimeActivity
Non-filterable, non-selectable: NoteText, DayOfWeek, ARDocType, ARRefNbr, NeedToBeDeleted, IsActivityExists, ReportedOnDate, TimeLogID, DeletedDatabaseRecord

PX.Objects.CR.PMTimeActivity.NoteID : Edm.Guid [key]
PX.Objects.CR.PMTimeActivity.RefNoteID : Edm.Guid "RefNoteID"
PX.Objects.CR.PMTimeActivity.NoteText : Edm.String "Note Text"
PX.Objects.CR.PMTimeActivity.SourceRefNoteID : Edm.Guid "Related Document"
PX.Objects.CR.PMTimeActivity.ParentTaskNoteID : Edm.Guid "Task"
PX.Objects.CR.PMTimeActivity.TrackTime : Edm.Boolean "Track Time and Costs"
PX.Objects.CR.PMTimeActivity.TimeCardCD : Edm.String "TimeCardCD"
PX.Objects.CR.PMTimeActivity.TimeSheetCD : Edm.String "TimeSheetCD"
PX.Objects.CR.PMTimeActivity.Summary : Edm.String "Summary"
PX.Objects.CR.PMTimeActivity.Date : Edm.DateTimeOffset "Date"
PX.Objects.CR.PMTimeActivity.DayOfWeek : Edm.Int32 "Day"
PX.Objects.CR.PMTimeActivity.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.PMTimeActivity.EarningTypeID : Edm.String "Earning Type"
PX.Objects.CR.PMTimeActivity.ExtRefNbr : Edm.String "External Ref. Nbr"
PX.Objects.CR.PMTimeActivity.ApproverID : Edm.Int32 "Approver"
PX.Objects.CR.PMTimeActivity.ApprovalStatus : Edm.String "Approval Status"
PX.Objects.CR.PMTimeActivity.ApprovedDate : Edm.DateTimeOffset "Approved Date"
PX.Objects.CR.PMTimeActivity.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.PMTimeActivity.ContractID : Edm.Int32 "Contract"
PX.Objects.CR.PMTimeActivity.TimeSpent : Edm.Int32 "Time Spent"
PX.Objects.CR.PMTimeActivity.OvertimeSpent : Edm.Int32 "Overtime"
PX.Objects.CR.PMTimeActivity.IsCorrected : Edm.Boolean
PX.Objects.CR.PMTimeActivity.OrigNoteID : Edm.Guid
PX.Objects.CR.PMTimeActivity.TranID : Edm.Int64
PX.Objects.CR.PMTimeActivity.WeekID : Edm.Int32 "Time Card Week"
PX.Objects.CR.PMTimeActivity.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.CR.PMTimeActivity.OvertimeItemID : Edm.Int32 "OvertimeItemID"
PX.Objects.CR.PMTimeActivity.JobID : Edm.Int32
PX.Objects.CR.PMTimeActivity.EmployeeRate : Edm.Decimal "Cost Rate"
PX.Objects.CR.PMTimeActivity.SummaryLineNbr : Edm.Int32
PX.Objects.CR.PMTimeActivity.ARDocType : Edm.String "Type"
PX.Objects.CR.PMTimeActivity.ARRefNbr : Edm.String "Reference Nbr."
PX.Objects.CR.PMTimeActivity.ReportedInTimeZoneID : Edm.String "Reported in Time Zone"
PX.Objects.CR.PMTimeActivity.TimeCardPeriodType : Edm.String "Frequency"
PX.Objects.CR.PMTimeActivity.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.CR.PMTimeActivity.CreatedByScreenID : Edm.String
PX.Objects.CR.PMTimeActivity.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.PMTimeActivity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.PMTimeActivity.LastModifiedByScreenID : Edm.String
PX.Objects.CR.PMTimeActivity.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.PMTimeActivity.tstamp : Edm.Binary
PX.Objects.CR.PMTimeActivity.NeedToBeDeleted : Edm.Boolean
PX.Objects.CR.PMTimeActivity.IsActivityExists : Edm.Boolean "Activity Exists"
PX.Objects.CR.PMTimeActivity.ReportedOnDate : Edm.DateTimeOffset "Reported On"
PX.Objects.CR.PMTimeActivity.TimeLogID : Edm.Int32 "TimeLogID"
PX.Objects.CR.PMTimeActivity.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CR.PMTimeActivity.EPEmployeeByApproverID -> PX.Objects.EP.EPEmployee (ApproverID=BAccountID)
PX.Objects.CR.PMTimeActivity.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.CR.PMTimeActivity.VendorByApproverID -> PX.Objects.AP.Vendor (ApproverID=BAccountID)
PX.Objects.CR.PMTimeActivity.VendorByOwnerID -> PX.Objects.AP.Vendor (OwnerID=DefContactID)
PX.Objects.CR.PMTimeActivity.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.CR.PMTimeActivity.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.CR.PMTimeActivity.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CR.PMTimeActivity.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.PMTimeActivity.PMTimeActivityByOrigNoteID -> PX.Objects.CR.PMTimeActivity (OrigNoteID=NoteID)
PX.Objects.CR.PMTimeActivity.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.CR.PMTimeActivity.InventoryItemByOvertimeItemID -> PX.Objects.IN.InventoryItem (OvertimeItemID=InventoryID)
PX.Objects.CR.PMTimeActivity.CRActivityByRefNoteID -> PX.Objects.CR.CRActivity (RefNoteID=NoteID)
PX.Objects.CR.PMTimeActivity.CRActivityByParentTaskNoteID -> PX.Objects.CR.CRActivity (ParentTaskNoteID=NoteID)
PX.Objects.CR.PMTimeActivity.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CR.PMTimeActivity.BranchByOffsetBranchID -> PX.Objects.GL.Branch
PX.Objects.CR.PMTimeActivity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.PMTimeActivity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.PMTimeActivity.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.PMTimeActivity.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.CR.PMTimeActivity.PMUnionByUnionID -> PX.Objects.PM.PMUnion
PX.Objects.CR.PMTimeActivity.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode
PX.Objects.CR.PMTimeActivity.EPEarningTypeByEarningTypeID -> PX.Objects.EP.EPEarningType (EarningTypeID=TypeCD)
PX.Objects.CR.PMTimeActivity.EPShiftCodeByShiftID -> PX.Objects.EP.EPShiftCode
PX.Objects.CR.PMTimeActivity.EPTimeActivitiesSummaryByOwnerID -> PX.Objects.EP.EPTimeActivitiesSummary (WorkgroupID=WorkgroupID, WeekID=Week, OwnerID=ContactID)
PX.Objects.CR.PMTimeActivity.EPTimeCardByTimeCardCD -> PX.Objects.EP.EPTimeCard (TimeCardCD=TimeCardCD)
PX.Objects.CR.PMTimeActivity.DailyFieldReportEmployeeActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeActivity)
PX.Objects.CR.PMTimeActivity.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.CR.PMTimeActivity.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)

# PX.Objects.CR.SMEmail (EntityType)

Label: "System Email"
Key: NoteID
Entity sets: PX_Objects_CR_SMEmail, SystemEmail, SMEmail
Non-filterable, non-selectable: NoteText, RedException, Source, DeletedDatabaseRecord

PX.Objects.CR.SMEmail.NoteID : Edm.Guid [key]
PX.Objects.CR.SMEmail.RefNoteID : Edm.Guid
PX.Objects.CR.SMEmail.NoteText : Edm.String "Note Text"
PX.Objects.CR.SMEmail.ResponseToNoteID : Edm.Guid "In Response To"
PX.Objects.CR.SMEmail.Subject : Edm.String "Summary"
PX.Objects.CR.SMEmail.Body : Edm.String "Activity Details"
PX.Objects.CR.SMEmail.MPStatus : Edm.String "Email Status"
PX.Objects.CR.SMEmail.IsArchived : Edm.Boolean "Archived"
PX.Objects.CR.SMEmail.ImcUID : Edm.Guid "ImcUID"
PX.Objects.CR.SMEmail.Pop3UID : Edm.String "Pop3UID"
PX.Objects.CR.SMEmail.ImapUID : Edm.Int32 "ImapUID"
PX.Objects.CR.SMEmail.MailAccountID : Edm.Int32 "From"
PX.Objects.CR.SMEmail.MailFrom : Edm.String "From"
PX.Objects.CR.SMEmail.MailReply : Edm.String "Reply"
PX.Objects.CR.SMEmail.MailTo : Edm.String "To"
PX.Objects.CR.SMEmail.MailCc : Edm.String "CC"
PX.Objects.CR.SMEmail.MailBcc : Edm.String "BCC"
PX.Objects.CR.SMEmail.MailDate : Edm.DateTimeOffset
PX.Objects.CR.SMEmail.RetryCount : Edm.Int32 [required] "RetryCount"
PX.Objects.CR.SMEmail.MessageId : Edm.String "MessageId"
PX.Objects.CR.SMEmail.MessageReference : Edm.String "MessageReference"
PX.Objects.CR.SMEmail.InReplyTo : Edm.String "InReplyTo"
PX.Objects.CR.SMEmail.Exception : Edm.String "Error Message"
PX.Objects.CR.SMEmail.RedException : Edm.String "Error Message"
PX.Objects.CR.SMEmail.Format : Edm.String "Format"
PX.Objects.CR.SMEmail.ReportFormat : Edm.String "Format"
PX.Objects.CR.SMEmail.TrackingID : Edm.String "TrackingID"
PX.Objects.CR.SMEmail.Ticket : Edm.String "Ticket"
PX.Objects.CR.SMEmail.IsIncome : Edm.Boolean "Is Income"
PX.Objects.CR.SMEmail.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.CR.SMEmail.CreatedByScreenID : Edm.String
PX.Objects.CR.SMEmail.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.SMEmail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.SMEmail.LastModifiedByScreenID : Edm.String
PX.Objects.CR.SMEmail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.SMEmail.tstamp : Edm.Binary
PX.Objects.CR.SMEmail.Source : Edm.String
PX.Objects.CR.SMEmail.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CR.SMEmail.CRActivityByRefNoteID -> PX.Objects.CR.CRActivity (RefNoteID=NoteID)
PX.Objects.CR.SMEmail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.SMEmail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.SMEmail.EMailAccountByMailAccountID -> PX.SM.EMailAccount (MailAccountID=EmailAccountID)
PX.Objects.CR.SMEmail.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.CR.SMEmail.SMSendGridRecipientCollection -> Collection(PX.DataSync.SendGrid.SMSendGridRecipient)
PX.Objects.CR.SMEmail.EmailLogCollection -> Collection(PX.Mail.Log.DAC.EmailLog)

# PX.Objects.CR.SMTeamsActivity (EntityType)

Label: "Teams Activity"
Key: NoteID
Entity sets: PX_Objects_CR_SMTeamsActivity, TeamsActivity1, SMTeamsActivity
Non-filterable, non-selectable: NoteText

PX.Objects.CR.SMTeamsActivity.NoteID : Edm.Guid [key]
PX.Objects.CR.SMTeamsActivity.RefNoteID : Edm.Guid
PX.Objects.CR.SMTeamsActivity.NoteText : Edm.String "Note Text"
PX.Objects.CR.SMTeamsActivity.Subject : Edm.String "Summary"
PX.Objects.CR.SMTeamsActivity.Body : Edm.String "Activity Details"
PX.Objects.CR.SMTeamsActivity.MPStatus : Edm.String "Mail Status"
PX.Objects.CR.SMTeamsActivity.ChannelID : Edm.String "Channel"
PX.Objects.CR.SMTeamsActivity.MemberID : Edm.Guid "Member"
PX.Objects.CR.SMTeamsActivity.IsIncome : Edm.Boolean "Is Income"
PX.Objects.CR.SMTeamsActivity.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.CR.SMTeamsActivity.CreatedByScreenID : Edm.String
PX.Objects.CR.SMTeamsActivity.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.SMTeamsActivity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.SMTeamsActivity.LastModifiedByScreenID : Edm.String
PX.Objects.CR.SMTeamsActivity.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.SMTeamsActivity.tstamp : Edm.Binary
PX.Objects.CR.SMTeamsActivity.CRActivityByRefNoteID -> PX.Objects.CR.CRActivity (RefNoteID=NoteID)
PX.Objects.CR.SMTeamsActivity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.SMTeamsActivity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CR.Standalone.CRLead (EntityType)

Label: "Lead"
Key: ContactID
Entity sets: PX_Objects_CR_Standalone_CRLead, Lead1, CRLead1
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CR.Standalone.CRLead.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.CR.Standalone.CRLead.Status : Edm.String "Status"
PX.Objects.CR.Standalone.CRLead.Resolution : Edm.String "Reason"
PX.Objects.CR.Standalone.CRLead.ClassID : Edm.String "Lead Class"
PX.Objects.CR.Standalone.CRLead.RefContactID : Edm.Int32 "Contact"
PX.Objects.CR.Standalone.CRLead.OverrideRefContact : Edm.Boolean [required] "Override"
PX.Objects.CR.Standalone.CRLead.Description : Edm.String "Description"
PX.Objects.CR.Standalone.CRLead.QualificationDate : Edm.DateTimeOffset "Qualification Date"
PX.Objects.CR.Standalone.CRLead.ConvertedBy : Edm.Guid "Converted By"
PX.Objects.CR.Standalone.CRLead.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CR.Standalone.CRLead.BAccountByBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CR.Standalone.CRLead.ContactByRefContactID -> PX.Objects.CR.Contact (RefContactID=ContactID)
PX.Objects.CR.Standalone.CRLead.ContactByDisplayName -> PX.Objects.CR.Contact
PX.Objects.CR.Standalone.CRLead.CRLeadClassByClassID -> PX.Objects.CR.CRLeadClass (ClassID=ClassID)
PX.Objects.CR.Standalone.CRLead.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CR.Standalone.CRLead.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CR.Standalone.CRLead.UsersByConvertedBy -> PX.SM.Users (ConvertedBy=PKID)
PX.Objects.CR.Standalone.CRLead.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CR.Standalone.CRLead.CRCampaignByCampaignID -> PX.Objects.CR.CRCampaign
PX.Objects.CR.Standalone.CRLead.LocaleByLanguageID -> PX.SM.Locale

# PX.Objects.CR.Standalone.CROpportunity (EntityType)

Key: OpportunityID
Entity sets: PX_Objects_CR_Standalone_CROpportunity
Non-filterable, non-selectable: NoteText

PX.Objects.CR.Standalone.CROpportunity.OpportunityID : Edm.String [key] "Opportunity ID"
PX.Objects.CR.Standalone.CROpportunity.LeadID : Edm.Guid "Source Lead"
PX.Objects.CR.Standalone.CROpportunity.ClassID : Edm.String "Opportunity Class"
PX.Objects.CR.Standalone.CROpportunity.Subject : Edm.String "Description"
PX.Objects.CR.Standalone.CROpportunity.Details : Edm.String "Details"
PX.Objects.CR.Standalone.CROpportunity.CloseDate : Edm.DateTimeOffset "Estimation"
PX.Objects.CR.Standalone.CROpportunity.StageChangedDate : Edm.DateTimeOffset "Stage Change Date"
PX.Objects.CR.Standalone.CROpportunity.StageID : Edm.String "Stage"
PX.Objects.CR.Standalone.CROpportunity.Status : Edm.String "Status"
PX.Objects.CR.Standalone.CROpportunity.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CR.Standalone.CROpportunity.Resolution : Edm.String "Reason"
PX.Objects.CR.Standalone.CROpportunity.AssignDate : Edm.DateTimeOffset "Assignment Date"
PX.Objects.CR.Standalone.CROpportunity.ClosingDate : Edm.DateTimeOffset "Actual Close Date"
PX.Objects.CR.Standalone.CROpportunity.NoteID : Edm.Guid
PX.Objects.CR.Standalone.CROpportunity.NoteText : Edm.String "Note Text"
PX.Objects.CR.Standalone.CROpportunity.Source : Edm.String "Source"
PX.Objects.CR.Standalone.CROpportunity.ExternalRef : Edm.String "External Ref."
PX.Objects.CR.Standalone.CROpportunity.tstamp : Edm.Binary
PX.Objects.CR.Standalone.CROpportunity.CreatedByScreenID : Edm.String
PX.Objects.CR.Standalone.CROpportunity.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.Standalone.CROpportunity.CreatedDateTime : Edm.DateTimeOffset "Date Created"
PX.Objects.CR.Standalone.CROpportunity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.Standalone.CROpportunity.LastModifiedByScreenID : Edm.String
PX.Objects.CR.Standalone.CROpportunity.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date"
PX.Objects.CR.Standalone.CROpportunity.DefQuoteID : Edm.Guid
PX.Objects.CR.Standalone.CROpportunity.BAccountByBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CR.Standalone.CROpportunity.BAccountByParentBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CR.Standalone.CROpportunity.ContactByContactID -> PX.Objects.CR.Contact
PX.Objects.CR.Standalone.CROpportunity.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.CR.Standalone.CROpportunity.ContactByLeadID -> PX.Objects.CR.Contact (LeadID=NoteID)
PX.Objects.CR.Standalone.CROpportunity.CROpportunityClassByClassID -> PX.Objects.CR.CROpportunityClass (ClassID=CROpportunityClassID)
PX.Objects.CR.Standalone.CROpportunity.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CR.Standalone.CROpportunity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.Standalone.CROpportunity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.Standalone.CROpportunity.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.CR.Standalone.CROpportunity.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone
PX.Objects.CR.Standalone.CROpportunity.CarrierByCarrierID -> PX.Objects.CS.Carrier
PX.Objects.CR.Standalone.CROpportunity.FOBPointByFOBPointID -> PX.Objects.CS.FOBPoint
PX.Objects.CR.Standalone.CROpportunity.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CR.Standalone.CROpportunity.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone
PX.Objects.CR.Standalone.CROpportunity.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms
PX.Objects.CR.Standalone.CROpportunity.TermsByTermsID -> PX.Objects.CS.Terms
PX.Objects.CR.Standalone.CROpportunity.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.CR.Standalone.CROpportunity.CurrencyByCuryID -> PX.Objects.CM.Currency
PX.Objects.CR.Standalone.CROpportunity.LocationByLocationID -> PX.Objects.CR.Location
PX.Objects.CR.Standalone.CROpportunity.CRAddressByOpportunityAddressID -> PX.Objects.CR.CRAddress
PX.Objects.CR.Standalone.CROpportunity.CRAddressByShipAddressID -> PX.Objects.CR.CRAddress
PX.Objects.CR.Standalone.CROpportunity.CRAddressByBillAddressID -> PX.Objects.CR.CRAddress
PX.Objects.CR.Standalone.CROpportunity.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign
PX.Objects.CR.Standalone.CROpportunity.CRContactByOpportunityContactID -> PX.Objects.CR.CRContact
PX.Objects.CR.Standalone.CROpportunity.CRContactByShipContactID -> PX.Objects.CR.CRContact
PX.Objects.CR.Standalone.CROpportunity.CRContactByBillContactID -> PX.Objects.CR.CRContact
PX.Objects.CR.Standalone.CROpportunity.LocaleByLanguageID -> PX.SM.Locale
PX.Objects.CR.Standalone.CROpportunity.CRTaxTranCollection -> Collection(PX.Objects.CR.CRTaxTran)
PX.Objects.CR.Standalone.CROpportunity.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.CR.Standalone.CROpportunity.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.CR.Standalone.CROpportunity.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.CR.Standalone.CROpportunity.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.CR.Standalone.CROpportunity.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.CR.Standalone.CROpportunity.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CR.Standalone.CROpportunity.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)

# PX.Objects.CR.Standalone.CROpportunityRevision (EntityType)

Key: NoteID
Entity sets: PX_Objects_CR_Standalone_CROpportunityRevision
Non-filterable, non-selectable: NoteText, CuryWgtAmount, QuoteStatus, CuryRate, CuryViewState

PX.Objects.CR.Standalone.CROpportunityRevision.NoteID : Edm.Guid [key]
PX.Objects.CR.Standalone.CROpportunityRevision.NoteText : Edm.String "Note Text"
PX.Objects.CR.Standalone.CROpportunityRevision.OpportunityID : Edm.String "Opportunity ID"
PX.Objects.CR.Standalone.CROpportunityRevision.BAccountID : Edm.Int32 "Business Account"
PX.Objects.CR.Standalone.CROpportunityRevision.ContactID : Edm.Int32 "Contact"
PX.Objects.CR.Standalone.CROpportunityRevision.AllowOverrideContactAddress : Edm.Boolean "Override"
PX.Objects.CR.Standalone.CROpportunityRevision.OpportunityContactID : Edm.Int32
PX.Objects.CR.Standalone.CROpportunityRevision.OpportunityAddressID : Edm.Int32
PX.Objects.CR.Standalone.CROpportunityRevision.AllowOverrideShippingContactAddress : Edm.Boolean [required] "Override Shipping Info"
PX.Objects.CR.Standalone.CROpportunityRevision.ShipContactID : Edm.Int32
PX.Objects.CR.Standalone.CROpportunityRevision.ShipAddressID : Edm.Int32
PX.Objects.CR.Standalone.CROpportunityRevision.BillContactID : Edm.Int32
PX.Objects.CR.Standalone.CROpportunityRevision.BillAddressID : Edm.Int32
PX.Objects.CR.Standalone.CROpportunityRevision.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.CR.Standalone.CROpportunityRevision.QuoteProjectID : Edm.Int32 "Project ID"
PX.Objects.CR.Standalone.CROpportunityRevision.QuoteProjectCD : Edm.String "Project ID"
PX.Objects.CR.Standalone.CROpportunityRevision.ProjectManager : Edm.Int32 "Project Manager"
PX.Objects.CR.Standalone.CROpportunityRevision.ExternalRef : Edm.String "External Ref."
PX.Objects.CR.Standalone.CROpportunityRevision.DocumentDate : Edm.DateTimeOffset "Estimation"
PX.Objects.CR.Standalone.CROpportunityRevision.CampaignSourceID : Edm.String "Source Campaign"
PX.Objects.CR.Standalone.CROpportunityRevision.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.Standalone.CROpportunityRevision.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryID : Edm.String "Currency"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryInfoID : Edm.Int64
PX.Objects.CR.Standalone.CROpportunityRevision.LineTotal : Edm.Decimal
PX.Objects.CR.Standalone.CROpportunityRevision.CuryLineTotal : Edm.Decimal "Detail Total"
PX.Objects.CR.Standalone.CROpportunityRevision.CostTotal : Edm.Decimal
PX.Objects.CR.Standalone.CROpportunityRevision.CuryCostTotal : Edm.Decimal "Total Cost"
PX.Objects.CR.Standalone.CROpportunityRevision.ProgressiveTotal : Edm.Decimal
PX.Objects.CR.Standalone.CROpportunityRevision.CuryProgressiveTotal : Edm.Decimal "Total Amount"
PX.Objects.CR.Standalone.CROpportunityRevision.ExtPriceTotal : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.CuryExtPriceTotal : Edm.Decimal [required] "Subtotal"
PX.Objects.CR.Standalone.CROpportunityRevision.LineDiscountTotal : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.CuryLineDiscountTotal : Edm.Decimal [required] "Detail Discount Total"
PX.Objects.CR.Standalone.CROpportunityRevision.LineDocDiscountTotal : Edm.Decimal
PX.Objects.CR.Standalone.CROpportunityRevision.CuryLineDocDiscountTotal : Edm.Decimal "CuryLineDocDiscountTotal"
PX.Objects.CR.Standalone.CROpportunityRevision.IsTaxValid : Edm.Boolean "Tax Is Up to Date"
PX.Objects.CR.Standalone.CROpportunityRevision.TaxTotal : Edm.Decimal
PX.Objects.CR.Standalone.CROpportunityRevision.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.CR.Standalone.CROpportunityRevision.TaxInclTotal : Edm.Decimal "Inclusive Tax Total in Base Currency"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryTaxInclTotal : Edm.Decimal "Inclusive Tax Total"
PX.Objects.CR.Standalone.CROpportunityRevision.ManualTotalEntry : Edm.Boolean [required] "Manual Amount"
PX.Objects.CR.Standalone.CROpportunityRevision.Amount : Edm.Decimal [required] "Amount"
PX.Objects.CR.Standalone.CROpportunityRevision.RawAmount : Edm.Decimal
PX.Objects.CR.Standalone.CROpportunityRevision.CuryAmount : Edm.Decimal [required] "Amount"
PX.Objects.CR.Standalone.CROpportunityRevision.DiscTot : Edm.Decimal
PX.Objects.CR.Standalone.CROpportunityRevision.CuryDiscTot : Edm.Decimal "Discount"
PX.Objects.CR.Standalone.CROpportunityRevision.ProductsAmount : Edm.Decimal "Products Amount"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryProductsAmount : Edm.Decimal "Total"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryOrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.CR.Standalone.CROpportunityRevision.OrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryWgtAmount : Edm.Decimal "Wgt. Total"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryVatExemptTotal : Edm.Decimal [required] "VAT Exempt Total"
PX.Objects.CR.Standalone.CROpportunityRevision.VatExemptTotal : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.CuryVatTaxableTotal : Edm.Decimal [required] "VAT Taxable Total"
PX.Objects.CR.Standalone.CROpportunityRevision.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.CR.Standalone.CROpportunityRevision.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.Standalone.CROpportunityRevision.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.CR.Standalone.CROpportunityRevision.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.CR.Standalone.CROpportunityRevision.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.CR.Standalone.CROpportunityRevision.QuoteStatus : Edm.String "Quote Status"
PX.Objects.CR.Standalone.CROpportunityRevision.DisableAutomaticDiscountCalculation : Edm.Boolean [required] "Disable Automatic Discount Update"
PX.Objects.CR.Standalone.CROpportunityRevision.TermsID : Edm.String "Terms"
PX.Objects.CR.Standalone.CROpportunityRevision.tstamp : Edm.Binary
PX.Objects.CR.Standalone.CROpportunityRevision.CreatedByScreenID : Edm.String
PX.Objects.CR.Standalone.CROpportunityRevision.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.Standalone.CROpportunityRevision.CreatedDateTime : Edm.DateTimeOffset "Date Created"
PX.Objects.CR.Standalone.CROpportunityRevision.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.Standalone.CROpportunityRevision.LastModifiedByScreenID : Edm.String
PX.Objects.CR.Standalone.CROpportunityRevision.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date"
PX.Objects.CR.Standalone.CROpportunityRevision.ProductCntr : Edm.Int32
PX.Objects.CR.Standalone.CROpportunityRevision.LineCntr : Edm.Int32
PX.Objects.CR.Standalone.CROpportunityRevision.Approved : Edm.Boolean "Approved"
PX.Objects.CR.Standalone.CROpportunityRevision.Rejected : Edm.Boolean "Rejected"
PX.Objects.CR.Standalone.CROpportunityRevision.LanguageID : Edm.String "Language/Locale"
PX.Objects.CR.Standalone.CROpportunityRevision.SiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.Standalone.CROpportunityRevision.CarrierID : Edm.String "Ship Via"
PX.Objects.CR.Standalone.CROpportunityRevision.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.Standalone.CROpportunityRevision.ShipZoneID : Edm.String "Shipping Zone"
PX.Objects.CR.Standalone.CROpportunityRevision.FOBPointID : Edm.String "FOB Point"
PX.Objects.CR.Standalone.CROpportunityRevision.Resedential : Edm.Boolean [required] "Residential Delivery"
PX.Objects.CR.Standalone.CROpportunityRevision.SaturdayDelivery : Edm.Boolean [required] "Saturday Delivery"
PX.Objects.CR.Standalone.CROpportunityRevision.Insurance : Edm.Boolean [required] "Insurance"
PX.Objects.CR.Standalone.CROpportunityRevision.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryMarginAmt : Edm.Decimal [required] "Est. Margin Amount"
PX.Objects.CR.Standalone.CROpportunityRevision.MarginAmt : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.MarginPct : Edm.Decimal [required] "Est. Margin (%)"
PX.Objects.CR.Standalone.CROpportunityRevision.CuryNetSalesTotal : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.NetSalesTotal : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.CurySalesCostTotal : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.SalesCostTotal : Edm.Decimal [required]
PX.Objects.CR.Standalone.CROpportunityRevision.CuryRate : Edm.Decimal
PX.Objects.CR.Standalone.CROpportunityRevision.CuryViewState : Edm.Boolean
PX.Objects.CR.Standalone.CROpportunityRevision.EPEmployeeByProjectManager -> PX.Objects.EP.EPEmployee (ProjectManager=BAccountID)
PX.Objects.CR.Standalone.CROpportunityRevision.PMProjectByQuoteProjectID -> PX.Objects.PM.PMProject (QuoteProjectID=ContractID)
PX.Objects.CR.Standalone.CROpportunityRevision.BAccountByBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID, BAccountID=BAccountID)
PX.Objects.CR.Standalone.CROpportunityRevision.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.Standalone.CROpportunityRevision.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CR.Standalone.CROpportunityRevision.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CR.Standalone.CROpportunityRevision.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.Standalone.CROpportunityRevision.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.Standalone.CROpportunityRevision.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.Standalone.CROpportunityRevision.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.CR.Standalone.CROpportunityRevision.CarrierByCarrierID -> PX.Objects.CS.Carrier (CarrierID=CarrierID)
PX.Objects.CR.Standalone.CROpportunityRevision.FOBPointByFOBPointID -> PX.Objects.CS.FOBPoint (FOBPointID=FOBPointID)
PX.Objects.CR.Standalone.CROpportunityRevision.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CR.Standalone.CROpportunityRevision.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.CR.Standalone.CROpportunityRevision.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.CR.Standalone.CROpportunityRevision.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.CR.Standalone.CROpportunityRevision.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.CR.Standalone.CROpportunityRevision.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CR.Standalone.CROpportunityRevision.LocationByLocationID -> PX.Objects.CR.Location
PX.Objects.CR.Standalone.CROpportunityRevision.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign (CampaignSourceID=CampaignID)
PX.Objects.CR.Standalone.CROpportunityRevision.LocaleByLanguageID -> PX.SM.Locale (LanguageID=LocaleName)
PX.Objects.CR.Standalone.CROpportunityRevision.CROpportunityTaxCollection -> Collection(PX.Objects.CR.CROpportunityTax)
PX.Objects.CR.Standalone.CROpportunityRevision.CROpportunityRevisionCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.CROpportunityRevisionCarrierData)

# PX.Objects.CR.Standalone.CRQuote (EntityType)

Key: QuoteID, QuoteNbr
Entity sets: PX_Objects_CR_Standalone_CRQuote
Non-filterable, non-selectable: NoteText

PX.Objects.CR.Standalone.CRQuote.QuoteID : Edm.Guid [key]
PX.Objects.CR.Standalone.CRQuote.QuoteNbr : Edm.String [key] "Quote Nbr."
PX.Objects.CR.Standalone.CRQuote.QuoteNbrUnq : Edm.String "Original Quote Nbr."
PX.Objects.CR.Standalone.CRQuote.QuoteType : Edm.String "Type"
PX.Objects.CR.Standalone.CRQuote.Subject : Edm.String "Subject"
PX.Objects.CR.Standalone.CRQuote.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.CR.Standalone.CRQuote.Status : Edm.String "Status"
PX.Objects.CR.Standalone.CRQuote.NoteID : Edm.Guid
PX.Objects.CR.Standalone.CRQuote.NoteText : Edm.String "Note Text"
PX.Objects.CR.Standalone.CRQuote.tstamp : Edm.Binary
PX.Objects.CR.Standalone.CRQuote.CreatedByScreenID : Edm.String
PX.Objects.CR.Standalone.CRQuote.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.Standalone.CRQuote.CreatedDateTime : Edm.DateTimeOffset "Date Created"
PX.Objects.CR.Standalone.CRQuote.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.Standalone.CRQuote.LastModifiedByScreenID : Edm.String
PX.Objects.CR.Standalone.CRQuote.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date"
PX.Objects.CR.Standalone.CRQuote.PMProjectByQuoteProjectID -> PX.Objects.PM.PMProject
PX.Objects.CR.Standalone.CRQuote.BAccountByBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CR.Standalone.CRQuote.BAccountByParentBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CR.Standalone.CRQuote.ContactByContactID -> PX.Objects.CR.Contact
PX.Objects.CR.Standalone.CRQuote.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.CR.Standalone.CRQuote.CROpportunityClassByOpportunityClassID -> PX.Objects.CR.CROpportunityClass
PX.Objects.CR.Standalone.CRQuote.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CR.Standalone.CRQuote.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.Standalone.CRQuote.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.Standalone.CRQuote.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.CR.Standalone.CRQuote.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone
PX.Objects.CR.Standalone.CRQuote.CarrierByCarrierID -> PX.Objects.CS.Carrier
PX.Objects.CR.Standalone.CRQuote.FOBPointByFOBPointID -> PX.Objects.CS.FOBPoint
PX.Objects.CR.Standalone.CRQuote.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CR.Standalone.CRQuote.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone
PX.Objects.CR.Standalone.CRQuote.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms
PX.Objects.CR.Standalone.CRQuote.TermsByTermsID -> PX.Objects.CS.Terms
PX.Objects.CR.Standalone.CRQuote.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.CR.Standalone.CRQuote.CurrencyByCuryID -> PX.Objects.CM.Currency
PX.Objects.CR.Standalone.CRQuote.LocationByLocationID -> PX.Objects.CR.Location
PX.Objects.CR.Standalone.CRQuote.CRAddressByOpportunityAddressID -> PX.Objects.CR.CRAddress
PX.Objects.CR.Standalone.CRQuote.CRAddressByShipAddressID -> PX.Objects.CR.CRAddress
PX.Objects.CR.Standalone.CRQuote.CRAddressByBillAddressID -> PX.Objects.CR.CRAddress
PX.Objects.CR.Standalone.CRQuote.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign
PX.Objects.CR.Standalone.CRQuote.CRContactByOpportunityContactID -> PX.Objects.CR.CRContact
PX.Objects.CR.Standalone.CRQuote.CRContactByShipContactID -> PX.Objects.CR.CRContact
PX.Objects.CR.Standalone.CRQuote.CRContactByBillContactID -> PX.Objects.CR.CRContact
PX.Objects.CR.Standalone.CRQuote.CROpportunityByOpportunityID -> PX.Objects.CR.CROpportunity
PX.Objects.CR.Standalone.CRQuote.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.CR.Standalone.CRQuote.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)

# PX.Objects.CR.Standalone.Location (EntityType)

Key: BAccountID, LocationCD
Entity sets: PX_Objects_CR_Standalone_Location
Non-filterable, non-selectable: OverrideAddress, IsAddressSameAsMain, OverrideContact, IsContactSameAsMain, NoteText, IsDefault, IsARAccountSameAsMain, OverrideRemitAddress, IsRemitAddressSameAsMain, OverrideRemitContact, IsRemitContactSameAsMain, IsAPAccountSameAsMain, IsAPPaymentInfoSameAsMain

PX.Objects.CR.Standalone.Location.BAccountID : Edm.Int32 [key] "Account ID"
PX.Objects.CR.Standalone.Location.LocationID : Edm.Int32 "LocationID"
PX.Objects.CR.Standalone.Location.LocationCD : Edm.String [key]
PX.Objects.CR.Standalone.Location.LocType : Edm.String "Location Type"
PX.Objects.CR.Standalone.Location.Descr : Edm.String "Location Name"
PX.Objects.CR.Standalone.Location.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.CR.Standalone.Location.DefAddressID : Edm.Int32 "Default Address"
PX.Objects.CR.Standalone.Location.OverrideAddress : Edm.Boolean "Override"
PX.Objects.CR.Standalone.Location.IsAddressSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.Standalone.Location.DefContactID : Edm.Int32 "Default Contact"
PX.Objects.CR.Standalone.Location.OverrideContact : Edm.Boolean "Override"
PX.Objects.CR.Standalone.Location.IsContactSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.Standalone.Location.NoteID : Edm.Guid
PX.Objects.CR.Standalone.Location.NoteText : Edm.String "Note Text"
PX.Objects.CR.Standalone.Location.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CR.Standalone.Location.Status : Edm.String "Status"
PX.Objects.CR.Standalone.Location.IsDefault : Edm.Boolean "Default"
PX.Objects.CR.Standalone.Location.CTaxZoneID : Edm.String "Tax Zone"
PX.Objects.CR.Standalone.Location.CTaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.Standalone.Location.CAvalaraExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.CR.Standalone.Location.CAvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.CR.Standalone.Location.CCarrierID : Edm.String "Ship Via"
PX.Objects.CR.Standalone.Location.CShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.Standalone.Location.CShipZoneID : Edm.String "Shipping Zone"
PX.Objects.CR.Standalone.Location.CFOBPointID : Edm.String "FOB Point"
PX.Objects.CR.Standalone.Location.CResedential : Edm.Boolean [required] "Residential Delivery"
PX.Objects.CR.Standalone.Location.CSaturdayDelivery : Edm.Boolean [required] "Saturday Delivery"
PX.Objects.CR.Standalone.Location.CAdditionalHandling : Edm.Boolean [required] "Additional Handling"
PX.Objects.CR.Standalone.Location.CLiftGate : Edm.Boolean [required] "Lift Gate"
PX.Objects.CR.Standalone.Location.CInsideDelivery : Edm.Boolean [required] "Inside Delivery"
PX.Objects.CR.Standalone.Location.CLimitedAccess : Edm.Boolean [required] "Limited Access"
PX.Objects.CR.Standalone.Location.CGroundCollect : Edm.Boolean [required] "Ground Collect"
PX.Objects.CR.Standalone.Location.CInsurance : Edm.Boolean [required] "Insurance"
PX.Objects.CR.Standalone.Location.CLeadTime : Edm.Int16 "Lead Time (Days)"
PX.Objects.CR.Standalone.Location.CBranchID : Edm.Int32 "Shipping Branch"
PX.Objects.CR.Standalone.Location.CSalesAcctID : Edm.Int32 "Sales Account"
PX.Objects.CR.Standalone.Location.CSalesSubID : Edm.Int32 "Sales Sub."
PX.Objects.CR.Standalone.Location.CPriceClassID : Edm.String "Price Class"
PX.Objects.CR.Standalone.Location.CSiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.Standalone.Location.CDiscountAcctID : Edm.Int32 "Discount Account"
PX.Objects.CR.Standalone.Location.CDiscountSubID : Edm.Int32 "Discount Sub."
PX.Objects.CR.Standalone.Location.CRetainageAcctID : Edm.Int32 "Retainage Receivable Account"
PX.Objects.CR.Standalone.Location.CRetainageSubID : Edm.Int32 "Retainage Receivable Sub."
PX.Objects.CR.Standalone.Location.CFreightAcctID : Edm.Int32 "Freight Account"
PX.Objects.CR.Standalone.Location.CFreightSubID : Edm.Int32 "Freight Sub."
PX.Objects.CR.Standalone.Location.CShipComplete : Edm.String "Shipping Rule"
PX.Objects.CR.Standalone.Location.COrderPriority : Edm.Int16 "Order Priority"
PX.Objects.CR.Standalone.Location.CCalendarID : Edm.String "Calendar"
PX.Objects.CR.Standalone.Location.CDefProjectID : Edm.Int32 "Default Project"
PX.Objects.CR.Standalone.Location.CARAccountLocationID : Edm.Int32
PX.Objects.CR.Standalone.Location.CARAccountID : Edm.Int32 "AR Account"
PX.Objects.CR.Standalone.Location.CARSubID : Edm.Int32 "AR Sub."
PX.Objects.CR.Standalone.Location.IsARAccountSameAsMain : Edm.Boolean "Same As Default Location's"
PX.Objects.CR.Standalone.Location.VTaxZoneID : Edm.String "Tax Zone"
PX.Objects.CR.Standalone.Location.VTaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.Standalone.Location.VCarrierID : Edm.String "Ship Via"
PX.Objects.CR.Standalone.Location.VShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.Standalone.Location.VFOBPointID : Edm.String "FOB Point"
PX.Objects.CR.Standalone.Location.VLeadTime : Edm.Int16 "Lead Time (Days)"
PX.Objects.CR.Standalone.Location.VBranchID : Edm.Int32 "Receiving Branch"
PX.Objects.CR.Standalone.Location.VExpenseAcctID : Edm.Int32 "Expense Account"
PX.Objects.CR.Standalone.Location.VExpenseSubID : Edm.Int32 "Expense Sub."
PX.Objects.CR.Standalone.Location.VRetainageAcctID : Edm.Int32 "Retainage Payable Account"
PX.Objects.CR.Standalone.Location.VRetainageSubID : Edm.Int32 "Retainage Payable Sub."
PX.Objects.CR.Standalone.Location.VFreightAcctID : Edm.Int32 "Freight Account"
PX.Objects.CR.Standalone.Location.VFreightSubID : Edm.Int32 "Freight Sub."
PX.Objects.CR.Standalone.Location.VDiscountAcctID : Edm.Int32 "Discount Account"
PX.Objects.CR.Standalone.Location.VDiscountSubID : Edm.Int32 "Discount Sub."
PX.Objects.CR.Standalone.Location.VRcptQtyMin : Edm.Decimal [required] "Min. Receipt (%)"
PX.Objects.CR.Standalone.Location.VRcptQtyMax : Edm.Decimal [required] "Max. Receipt (%)"
PX.Objects.CR.Standalone.Location.VRcptQtyThreshold : Edm.Decimal [required] "Threshold Receipt (%)"
PX.Objects.CR.Standalone.Location.VRcptQtyAction : Edm.String "Receipt Action"
PX.Objects.CR.Standalone.Location.VSiteIDIsNull : Edm.Int16
PX.Objects.CR.Standalone.Location.VPrintOrder : Edm.Boolean [required] "Print Order"
PX.Objects.CR.Standalone.Location.VEmailOrder : Edm.Boolean [required] "Email Order"
PX.Objects.CR.Standalone.Location.VAPAccountLocationID : Edm.Int32
PX.Objects.CR.Standalone.Location.VAPAccountID : Edm.Int32 "AP Account"
PX.Objects.CR.Standalone.Location.VAPSubID : Edm.Int32 "AP Sub."
PX.Objects.CR.Standalone.Location.VPaymentInfoLocationID : Edm.Int32
PX.Objects.CR.Standalone.Location.OverrideRemitAddress : Edm.Boolean "Override"
PX.Objects.CR.Standalone.Location.IsRemitAddressSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.Standalone.Location.VRemitAddressID : Edm.Int32
PX.Objects.CR.Standalone.Location.OverrideRemitContact : Edm.Boolean "Override"
PX.Objects.CR.Standalone.Location.IsRemitContactSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.Standalone.Location.VRemitContactID : Edm.Int32
PX.Objects.CR.Standalone.Location.VPaymentMethodID : Edm.String "Payment Method"
PX.Objects.CR.Standalone.Location.VCashAccountID : Edm.Int32 "Cash Account"
PX.Objects.CR.Standalone.Location.VPaymentLeadTime : Edm.Int16 "Payment Lead Time (Days)"
PX.Objects.CR.Standalone.Location.VPaymentByType : Edm.Int32 [required] "Payment By"
PX.Objects.CR.Standalone.Location.VSeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.CR.Standalone.Location.VPrepaymentPct : Edm.Decimal [required] "Prepayment Percent"
PX.Objects.CR.Standalone.Location.VAllowAPBillBeforeReceipt : Edm.Boolean [required] "Allow AP Bill Before Receipt"
PX.Objects.CR.Standalone.Location.IsAPAccountSameAsMain : Edm.Boolean "Same As Default Location's"
PX.Objects.CR.Standalone.Location.IsAPPaymentInfoSameAsMain : Edm.Boolean "Same As Default Location's"
PX.Objects.CR.Standalone.Location.CMPSalesSubID : Edm.Int32 "Sales Sub."
PX.Objects.CR.Standalone.Location.CMPExpenseSubID : Edm.Int32 "Expense Sub."
PX.Objects.CR.Standalone.Location.CMPFreightSubID : Edm.Int32 "Freight Sub."
PX.Objects.CR.Standalone.Location.CMPDiscountSubID : Edm.Int32 "Discount Sub."
PX.Objects.CR.Standalone.Location.CMPGainLossSubID : Edm.Int32 "Currency Gain/Loss Sub."
PX.Objects.CR.Standalone.Location.CMPSiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.Standalone.Location.ExtRefNbr : Edm.String "External ID"
PX.Objects.CR.Standalone.Location.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.Standalone.Location.CreatedByScreenID : Edm.String
PX.Objects.CR.Standalone.Location.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.Standalone.Location.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.Standalone.Location.LastModifiedByScreenID : Edm.String
PX.Objects.CR.Standalone.Location.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.Standalone.Location.tstamp : Edm.Binary
PX.Objects.CR.Standalone.Location.ContactByDefContactID -> PX.Objects.CR.Contact (DefContactID=ContactID)
PX.Objects.CR.Standalone.Location.ContactByVRemitContactID -> PX.Objects.CR.Contact (VRemitContactID=ContactID)
PX.Objects.CR.Standalone.Location.AddressByDefAddressID -> PX.Objects.CR.Address (DefAddressID=AddressID)
PX.Objects.CR.Standalone.Location.AddressByVRemitAddressID -> PX.Objects.CR.Address (VRemitAddressID=AddressID)
PX.Objects.CR.Standalone.Location.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.Standalone.Location.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.Standalone.Location.INSiteByCSiteID -> PX.Objects.IN.INSite (CSiteID=SiteID)
PX.Objects.CR.Standalone.Location.INSiteByVSiteID -> PX.Objects.IN.INSite
PX.Objects.CR.Standalone.Location.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)

# PX.Objects.CS.AddressValidatorPlugin (EntityType)

Label: "Address Verification Service"
Key: AddressValidatorPluginID
Entity sets: PX_Objects_CS_AddressValidatorPlugin, AddressVerificationService, AddressValidatorPlugin
Non-filterable, non-selectable: NoteText

PX.Objects.CS.AddressValidatorPlugin.AddressValidatorPluginID : Edm.String [key] "Provider ID"
PX.Objects.CS.AddressValidatorPlugin.Description : Edm.String "Description"
PX.Objects.CS.AddressValidatorPlugin.PluginTypeName : Edm.String "Plug-In"
PX.Objects.CS.AddressValidatorPlugin.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.AddressValidatorPlugin.NoteID : Edm.Guid
PX.Objects.CS.AddressValidatorPlugin.NoteText : Edm.String "Note Text"
PX.Objects.CS.AddressValidatorPlugin.tstamp : Edm.Binary
PX.Objects.CS.AddressValidatorPlugin.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.AddressValidatorPlugin.CreatedByScreenID : Edm.String
PX.Objects.CS.AddressValidatorPlugin.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CS.AddressValidatorPlugin.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.AddressValidatorPlugin.LastModifiedByScreenID : Edm.String
PX.Objects.CS.AddressValidatorPlugin.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CS.AddressValidatorPlugin.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.AddressValidatorPlugin.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.AddressValidatorPlugin.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CS.AddressValidatorPlugin.PreferencesGeneralCollection -> Collection(PX.SM.PreferencesGeneral)
PX.Objects.CS.AddressValidatorPlugin.AddressValidatorPluginDetailCollection -> Collection(PX.Objects.CS.AddressValidatorPluginDetail)
PX.Objects.CS.AddressValidatorPlugin.CountryCollection -> Collection(PX.Objects.CS.Country)

# PX.Objects.CS.AddressValidatorPluginDetail (EntityType)

Label: "Address Verification Service Details"
Key: AddressValidatorPluginID, SettingID
Entity sets: PX_Objects_CS_AddressValidatorPluginDetail, AddressVerificationServiceDetails, AddressValidatorPluginDetail

PX.Objects.CS.AddressValidatorPluginDetail.AddressValidatorPluginID : Edm.String [key]
PX.Objects.CS.AddressValidatorPluginDetail.SettingID : Edm.String [key] "ID"
PX.Objects.CS.AddressValidatorPluginDetail.SortOrder : Edm.Int32
PX.Objects.CS.AddressValidatorPluginDetail.Description : Edm.String "Description"
PX.Objects.CS.AddressValidatorPluginDetail.Value : Edm.String "Value"
PX.Objects.CS.AddressValidatorPluginDetail.ControlTypeValue : Edm.Int32 [required] "Control Type"
PX.Objects.CS.AddressValidatorPluginDetail.ComboValuesStr : Edm.String
PX.Objects.CS.AddressValidatorPluginDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.AddressValidatorPluginDetail.CreatedByScreenID : Edm.String
PX.Objects.CS.AddressValidatorPluginDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.AddressValidatorPluginDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.AddressValidatorPluginDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CS.AddressValidatorPluginDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.AddressValidatorPluginDetail.tstamp : Edm.Binary
PX.Objects.CS.AddressValidatorPluginDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.AddressValidatorPluginDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.AddressValidatorPluginDetail.AddressValidatorPluginByAddressValidatorPluginID -> PX.Objects.CS.AddressValidatorPlugin (AddressValidatorPluginID=AddressValidatorPluginID)

# PX.Objects.CS.ArmGLHistoryByPeriod (EntityType)

Label: "GL History by Period"
Key: AccountID, BranchID, FinPeriodID, LedgerID, SubID
Entity sets: PX_Objects_CS_ArmGLHistoryByPeriod, GLHistorybyPeriod, ArmGLHistoryByPeriod
Non-filterable, non-selectable: FinYear

PX.Objects.CS.ArmGLHistoryByPeriod.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.CS.ArmGLHistoryByPeriod.LedgerID : Edm.Int32 [key] "Ledger"
PX.Objects.CS.ArmGLHistoryByPeriod.AccountID : Edm.Int32 [key] "Account"
PX.Objects.CS.ArmGLHistoryByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.CS.ArmGLHistoryByPeriod.LastActivityPeriod : Edm.String "Last Activity Period"
PX.Objects.CS.ArmGLHistoryByPeriod.AccountClassID : Edm.String
PX.Objects.CS.ArmGLHistoryByPeriod.FinPeriodID : Edm.String [key] "Financial Period"
PX.Objects.CS.ArmGLHistoryByPeriod.FinYear : Edm.String
PX.Objects.CS.ArmGLHistoryByPeriod.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CS.ArmGLHistoryByPeriod.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.CS.ArmGLHistoryByPeriod.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.CS.ArmGLHistoryByPeriod.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)
PX.Objects.CS.ArmGLHistoryByPeriod.AccountClassByAccountClassID -> PX.Objects.GL.AccountClass (AccountClassID=AccountClassID)

# PX.Objects.CS.ARTranAlias (EntityType)

Key: RefNbr, TranType
Entity sets: PX_Objects_CS_ARTranAlias

PX.Objects.CS.ARTranAlias.TranType : Edm.String [key]
PX.Objects.CS.ARTranAlias.RefNbr : Edm.String [key]
PX.Objects.CS.ARTranAlias.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.CS.ARTranAlias.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.CS.ARTranAlias.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.CS.ARTranAlias.DRScheduleByTranType -> PX.Objects.DR.DRSchedule (TranType=DocType)
PX.Objects.CS.ARTranAlias.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.CS.ARTranAlias.SOInvoiceByOrigInvoiceType -> PX.Objects.SO.SOInvoice

# PX.Objects.CS.Carrier (EntityType)

Label: "Carrier"
Key: CarrierID
Entity sets: PX_Objects_CS_Carrier, Carrier
Non-filterable, non-selectable: NoteText

PX.Objects.CS.Carrier.CarrierID : Edm.String [key] "Ship Via"
PX.Objects.CS.Carrier.CalcMethod : Edm.String "Calculation Method"
PX.Objects.CS.Carrier.Description : Edm.String "Description"
PX.Objects.CS.Carrier.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.Carrier.DeliveryType : Edm.String "Delivery Type"
PX.Objects.CS.Carrier.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.CS.Carrier.CalendarID : Edm.String "Calendar"
PX.Objects.CS.Carrier.BaseRate : Edm.Decimal [required] "Base Rate"
PX.Objects.CS.Carrier.IsExternal : Edm.Boolean "External Plug-in"
PX.Objects.CS.Carrier.CarrierPluginID : Edm.String "Carrier"
PX.Objects.CS.Carrier.PluginMethod : Edm.String "Service Method"
PX.Objects.CS.Carrier.ConfirmationRequired : Edm.Boolean [required] "Confirmation for Each Box Is Required"
PX.Objects.CS.Carrier.PackageRequired : Edm.Boolean [required] "At least one Package Is Required"
PX.Objects.CS.Carrier.IsCommonCarrier : Edm.Boolean [required] "Common Carrier"
PX.Objects.CS.Carrier.ReturnLabel : Edm.Boolean [required] "Generate Return Label Automatically"
PX.Objects.CS.Carrier.ValidatePackedQty : Edm.Boolean [required] "Validate Packed Quantities on Shipment Confirmation"
PX.Objects.CS.Carrier.IsExternalShippingApplication : Edm.Boolean [required] "Use External Shipping Application"
PX.Objects.CS.Carrier.ShippingApplicationType : Edm.String "Shipping Application"
PX.Objects.CS.Carrier.CalcFreightOnReturn : Edm.Boolean [required] "Calculate Freight on Returns"
PX.Objects.CS.Carrier.NoteID : Edm.Guid
PX.Objects.CS.Carrier.NoteText : Edm.String "Note Text"
PX.Objects.CS.Carrier.tstamp : Edm.Binary
PX.Objects.CS.Carrier.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.Carrier.CreatedByScreenID : Edm.String
PX.Objects.CS.Carrier.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CS.Carrier.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.Carrier.LastModifiedByScreenID : Edm.String
PX.Objects.CS.Carrier.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CS.Carrier.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.Carrier.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.Carrier.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.CS.Carrier.CarrierPluginByCarrierPluginID -> PX.Objects.CS.CarrierPlugin (CarrierPluginID=CarrierPluginID)
PX.Objects.CS.Carrier.AccountByFreightSalesAcctID -> PX.Objects.GL.Account
PX.Objects.CS.Carrier.AccountByFreightExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.CS.Carrier.SubByFreightSalesSubID -> PX.Objects.GL.Sub
PX.Objects.CS.Carrier.SubByFreightExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.CS.Carrier.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.CS.Carrier.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.Objects.CS.Carrier.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CS.Carrier.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CS.Carrier.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.CS.Carrier.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CS.Carrier.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CS.Carrier.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CS.Carrier.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.CS.Carrier.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CS.Carrier.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.Objects.CS.Carrier.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CS.Carrier.CarrierPackageCollection -> Collection(PX.Objects.CS.CarrierPackage)
PX.Objects.CS.Carrier.FreightRateCollection -> Collection(PX.Objects.CS.FreightRate)
PX.Objects.CS.Carrier.NotificationSetupUserOverrideCollection -> Collection(PX.Objects.CS.NotificationSetupUserOverride)
PX.Objects.CS.Carrier.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CS.Carrier.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CS.Carrier.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CS.Carrier.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CS.Carrier.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CS.Carrier.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CS.Carrier.BCShippingMappingsCollection -> Collection(PX.Commerce.Objects.BCShippingMappings)

# PX.Objects.CS.CarrierPackage (EntityType)

Label: "Carrier Package"
Key: BoxID, CarrierID
Entity sets: PX_Objects_CS_CarrierPackage, CarrierPackage

PX.Objects.CS.CarrierPackage.CarrierID : Edm.String [key]
PX.Objects.CS.CarrierPackage.BoxID : Edm.String [key] "Box ID"
PX.Objects.CS.CarrierPackage.CarrierBox : Edm.String "Carrier's Package"
PX.Objects.CS.CarrierPackage.tstamp : Edm.Binary
PX.Objects.CS.CarrierPackage.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CarrierPackage.CreatedByScreenID : Edm.String
PX.Objects.CS.CarrierPackage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CarrierPackage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CarrierPackage.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CarrierPackage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CarrierPackage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CarrierPackage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CarrierPackage.CarrierByCarrierID -> PX.Objects.CS.Carrier (CarrierID=CarrierID)
PX.Objects.CS.CarrierPackage.CSBoxByBoxID -> PX.Objects.CS.CSBox (BoxID=BoxID)

# PX.Objects.CS.CarrierPlugin (EntityType)

Label: "Carrier Plugin"
Key: CarrierPluginID
Entity sets: PX_Objects_CS_CarrierPlugin, CarrierPlugin
Non-filterable, non-selectable: KilogramUOM, PoundUOM, CentimeterUOM, InchUOM, NoteText

PX.Objects.CS.CarrierPlugin.CarrierPluginID : Edm.String [key] "Carrier ID"
PX.Objects.CS.CarrierPlugin.DetailLineCntr : Edm.Int32 [required]
PX.Objects.CS.CarrierPlugin.Description : Edm.String "Description"
PX.Objects.CS.CarrierPlugin.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.CarrierPlugin.PluginTypeName : Edm.String "Plug-In"
PX.Objects.CS.CarrierPlugin.UnitType : Edm.String "Carrier Units"
PX.Objects.CS.CarrierPlugin.UOM : Edm.String
PX.Objects.CS.CarrierPlugin.LinearUOM : Edm.String
PX.Objects.CS.CarrierPlugin.ReturnLabelNotification : Edm.Int32 "Email Template for Return Label"
PX.Objects.CS.CarrierPlugin.KilogramUOM : Edm.String "Kilogram"
PX.Objects.CS.CarrierPlugin.PoundUOM : Edm.String "Pound"
PX.Objects.CS.CarrierPlugin.CentimeterUOM : Edm.String "Centimeter"
PX.Objects.CS.CarrierPlugin.InchUOM : Edm.String "Inch"
PX.Objects.CS.CarrierPlugin.NoteID : Edm.Guid
PX.Objects.CS.CarrierPlugin.NoteText : Edm.String "Note Text"
PX.Objects.CS.CarrierPlugin.tstamp : Edm.Binary
PX.Objects.CS.CarrierPlugin.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CarrierPlugin.CreatedByScreenID : Edm.String
PX.Objects.CS.CarrierPlugin.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CS.CarrierPlugin.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CarrierPlugin.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CarrierPlugin.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CS.CarrierPlugin.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CarrierPlugin.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CarrierPlugin.NotificationByReturnLabelNotification -> PX.SM.Notification (ReturnLabelNotification=NotificationID)
PX.Objects.CS.CarrierPlugin.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.CS.CarrierPlugin.CarrierCollection -> Collection(PX.Objects.CS.Carrier)
PX.Objects.CS.CarrierPlugin.CarrierPluginCustomerCollection -> Collection(PX.Objects.CS.CarrierPluginCustomer)
PX.Objects.CS.CarrierPlugin.CarrierPluginDetailCollection -> Collection(PX.Objects.CS.CarrierPluginDetail)
PX.Objects.CS.CarrierPlugin.ShipEngineCarrierServiceCollection -> Collection(PX.ExternalCarriersCommon.ShipEngineCarrierService)
PX.Objects.CS.CarrierPlugin.SETerritoriesMappingCollection -> Collection(PX.ExternalCarriersHelper.SETerritoriesMapping)

# PX.Objects.CS.CarrierPluginCustomer (EntityType)

Label: "Carrier Plugin Customer"
Key: CarrierPluginID, RecordID
Entity sets: PX_Objects_CS_CarrierPluginCustomer, CarrierPluginCustomer

PX.Objects.CS.CarrierPluginCustomer.CarrierPluginID : Edm.String [key] "Carrier"
PX.Objects.CS.CarrierPluginCustomer.RecordID : Edm.Int32 [key]
PX.Objects.CS.CarrierPluginCustomer.CustomerID : Edm.Int32 "Customer ID"
PX.Objects.CS.CarrierPluginCustomer.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.CarrierPluginCustomer.CarrierAccount : Edm.String "Carrier Billing Account"
PX.Objects.CS.CarrierPluginCustomer.PostalCode : Edm.String "Billing Postal Code"
PX.Objects.CS.CarrierPluginCustomer.CarrierBillingType : Edm.String "Billing Type"
PX.Objects.CS.CarrierPluginCustomer.CountryID : Edm.String "Billing Country"
PX.Objects.CS.CarrierPluginCustomer.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CarrierPluginCustomer.CreatedByScreenID : Edm.String
PX.Objects.CS.CarrierPluginCustomer.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CarrierPluginCustomer.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CarrierPluginCustomer.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CarrierPluginCustomer.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CarrierPluginCustomer.tstamp : Edm.Binary
PX.Objects.CS.CarrierPluginCustomer.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.CS.CarrierPluginCustomer.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CarrierPluginCustomer.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CarrierPluginCustomer.CarrierPluginByCarrierPluginID -> PX.Objects.CS.CarrierPlugin (CarrierPluginID=CarrierPluginID)
PX.Objects.CS.CarrierPluginCustomer.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.CS.CarrierPluginCustomer.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)

# PX.Objects.CS.CarrierPluginDetail (EntityType)

Label: "Carrier Plugin Detail"
Key: CarrierPluginID, DetailID
Entity sets: PX_Objects_CS_CarrierPluginDetail, CarrierPluginDetail

PX.Objects.CS.CarrierPluginDetail.CarrierPluginID : Edm.String [key]
PX.Objects.CS.CarrierPluginDetail.DetailID : Edm.String [key] "ID"
PX.Objects.CS.CarrierPluginDetail.DetailLineNbr : Edm.Int32 "Line Nbr."
PX.Objects.CS.CarrierPluginDetail.Descr : Edm.String "Description"
PX.Objects.CS.CarrierPluginDetail.Value : Edm.String "Value"
PX.Objects.CS.CarrierPluginDetail.ControlType : Edm.Int32 [required] "Control Type"
PX.Objects.CS.CarrierPluginDetail.ComboValues : Edm.String
PX.Objects.CS.CarrierPluginDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CarrierPluginDetail.CreatedByScreenID : Edm.String
PX.Objects.CS.CarrierPluginDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CarrierPluginDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CarrierPluginDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CarrierPluginDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CarrierPluginDetail.tstamp : Edm.Binary
PX.Objects.CS.CarrierPluginDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CarrierPluginDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CarrierPluginDetail.CarrierPluginByCarrierPluginID -> PX.Objects.CS.CarrierPlugin (CarrierPluginID=CarrierPluginID)

# PX.Objects.CS.CommonSetup (EntityType)

Label: "Common Setup"
Singletons: PX_Objects_CS_CommonSetup, CommonSetup

PX.Objects.CS.CommonSetup.DecPlPrcCst : Edm.Int16 [required] "Price/Cost Decimal Places"
PX.Objects.CS.CommonSetup.DecPlQty : Edm.Int16 [required] "Quantity Decimal Places"
PX.Objects.CS.CommonSetup.WeightUOM : Edm.String "Weight UOM"
PX.Objects.CS.CommonSetup.LinearUOM : Edm.String "Linear UOM"
PX.Objects.CS.CommonSetup.VolumeUOM : Edm.String "Volume UOM"
PX.Objects.CS.CommonSetup.tstamp : Edm.Binary
PX.Objects.CS.CommonSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CommonSetup.CreatedByScreenID : Edm.String
PX.Objects.CS.CommonSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CommonSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CommonSetup.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CommonSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CommonSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CommonSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CommonSetup.INUnitByWeightUOM -> PX.Objects.IN.INUnit (WeightUOM=FromUnit)
PX.Objects.CS.CommonSetup.INUnitByLinearUOM -> PX.Objects.IN.INUnit (LinearUOM=FromUnit)
PX.Objects.CS.CommonSetup.INUnitByVolumeUOM -> PX.Objects.IN.INUnit (VolumeUOM=FromUnit)

# PX.Objects.CS.Country (EntityType)

Label: "Country"
Key: CountryID
Entity sets: PX_Objects_CS_Country, Country
Non-filterable, non-selectable: NoteText

PX.Objects.CS.Country.CountryID : Edm.String [key] "Country ID"
PX.Objects.CS.Country.Description : Edm.String "Country Name"
PX.Objects.CS.Country.CountryValidationMethod : Edm.String "Validation Mode"
PX.Objects.CS.Country.CountryRegexp : Edm.String "Validation Regexp"
PX.Objects.CS.Country.StateValidationMethod : Edm.String "Validation Mode"
PX.Objects.CS.Country.ZipCodeMask : Edm.String "Input Mask"
PX.Objects.CS.Country.ZipCodeRegexp : Edm.String "Validation Regexp"
PX.Objects.CS.Country.PhoneCountryCode : Edm.String "Country Phone Code"
PX.Objects.CS.Country.PhoneMask : Edm.String "Input Mask"
PX.Objects.CS.Country.PhoneRegexp : Edm.String "Phone Validation Reg. Exp."
PX.Objects.CS.Country.AddressValidatorPluginID : Edm.String "Address Validation Plug-In"
PX.Objects.CS.Country.AutoOverrideAddress : Edm.Boolean [required] "Override Address Automatically"
PX.Objects.CS.Country.LanguageID : Edm.String "Language/Locale"
PX.Objects.CS.Country.NoteID : Edm.Guid
PX.Objects.CS.Country.NoteText : Edm.String "Note Text"
PX.Objects.CS.Country.tstamp : Edm.Binary
PX.Objects.CS.Country.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.Country.CreatedByScreenID : Edm.String
PX.Objects.CS.Country.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Country.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.Country.LastModifiedByScreenID : Edm.String
PX.Objects.CS.Country.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Country.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.Country.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.Country.AddressValidatorPluginByAddressValidatorPluginID -> PX.Objects.CS.AddressValidatorPlugin (AddressValidatorPluginID=AddressValidatorPluginID)
PX.Objects.CS.Country.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CS.Country.LocaleByLanguageID -> PX.SM.Locale (LanguageID=LocaleName)
PX.Objects.CS.Country.VendorPaymentMethodCollection -> Collection(PX.Objects.AP.DAC.VendorPaymentMethod)
PX.Objects.CS.Country.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)
PX.Objects.CS.Country.POAddressCollection -> Collection(PX.Objects.PO.POAddress)
PX.Objects.CS.Country.PMAddressCollection -> Collection(PX.Objects.PM.PMAddress)
PX.Objects.CS.Country.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.CS.Country.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.CS.Country.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.Objects.CS.Country.AddressCollection -> Collection(PX.Objects.CR.Address)
PX.Objects.CS.Country.CRAddressCollection -> Collection(PX.Objects.CR.CRAddress)
PX.Objects.CS.Country.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CS.Country.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.Objects.CS.Country.FSAddressCollection -> Collection(PX.Objects.FS.FSAddress)
PX.Objects.CS.Country.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.CS.Country.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.CS.Country.FSGeoZonePostalCodeCollection -> Collection(PX.Objects.SV.FSGeoZonePostalCode)
PX.Objects.CS.Country.FSGeoZoneCollection -> Collection(PX.Objects.SV.FSGeoZone)
PX.Objects.CS.Country.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.CS.Country.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CS.Country.PREarningTypeDetailCollection -> Collection(PX.Objects.PR.PREarningTypeDetail)
PX.Objects.CS.Country.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.CS.Country.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)
PX.Objects.CS.Country.TaxZoneAddressMappingCollection -> Collection(PX.Objects.TX.TaxZoneAddressMapping)
PX.Objects.CS.Country.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.CS.Country.PREmployeeClassCollection -> Collection(PX.Objects.PR.PREmployeeClass)
PX.Objects.CS.Country.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.CS.Country.CarrierPluginCustomerCollection -> Collection(PX.Objects.CS.CarrierPluginCustomer)
PX.Objects.CS.Country.SalesTerritoryCollection -> Collection(PX.Objects.CS.SalesTerritory)
PX.Objects.CS.Country.ShippingZoneLineCollection -> Collection(PX.Objects.CS.ShippingZoneLine)
PX.Objects.CS.Country.StateCollection -> Collection(PX.Objects.CS.State)
PX.Objects.CS.Country.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CS.Country.APAddressCollection -> Collection(PX.Objects.AP.APAddress)
PX.Objects.CS.Country.SETerritoriesMappingCollection -> Collection(PX.ExternalCarriersHelper.SETerritoriesMapping)
PX.Objects.CS.Country.AMVendorShipmentAddressCollection -> Collection(PX.Objects.AM.AMVendorShipmentAddress)
PX.Objects.CS.Country.PRCompanyTaxAttributeCollection -> Collection(PX.Objects.PR.PRCompanyTaxAttribute)
PX.Objects.CS.Country.PREmployeeAttributeCollection -> Collection(PX.Objects.PR.PREmployeeAttribute)
PX.Objects.CS.Country.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.Objects.CS.Country.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.CS.Country.PRTransactionDateExceptionCollection -> Collection(PX.Objects.PR.PRTransactionDateException)
PX.Objects.CS.Country.SVAddressCollection -> Collection(PX.Objects.SV.SVAddress)

# PX.Objects.CS.CSAnswers (EntityType)

Label: "Answers"
Key: AttributeID, RefNoteID
Entity sets: PX_Objects_CS_CSAnswers, Answers, CSAnswers
Non-filterable, non-selectable: IsRequired, Order, NotInClass

PX.Objects.CS.CSAnswers.RefNoteID : Edm.Guid [key] "RefNoteID"
PX.Objects.CS.CSAnswers.AttributeID : Edm.String [key] "Attribute"
PX.Objects.CS.CSAnswers.Value : Edm.String "Value"
PX.Objects.CS.CSAnswers.IsRequired : Edm.Boolean "Required"
PX.Objects.CS.CSAnswers.Order : Edm.Int16
PX.Objects.CS.CSAnswers.NotInClass : Edm.Boolean
PX.Objects.CS.CSAnswers.NoteID : Edm.Guid
PX.Objects.CS.CSAnswers.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.CS.CSAnswers.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.CS.CSAnswers.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)

# PX.Objects.CS.CSAttribute (EntityType)

Label: "Attribute"
Key: AttributeID
Entity sets: PX_Objects_CS_CSAttribute, Attribute, CSAttribute
Non-filterable, non-selectable: NoteText

PX.Objects.CS.CSAttribute.AttributeID : Edm.String [key] "Attribute ID"
PX.Objects.CS.CSAttribute.Description : Edm.String "Description"
PX.Objects.CS.CSAttribute.ControlType : Edm.Int32 [required] "Control Type"
PX.Objects.CS.CSAttribute.EntryMask : Edm.String "Entry Mask"
PX.Objects.CS.CSAttribute.RegExp : Edm.String "Reg. Exp."
PX.Objects.CS.CSAttribute.Precision : Edm.Int32 [required] "Decimal Places"
PX.Objects.CS.CSAttribute.List : Edm.String
PX.Objects.CS.CSAttribute.IsInternal : Edm.Boolean "Internal"
PX.Objects.CS.CSAttribute.NoteID : Edm.Guid
PX.Objects.CS.CSAttribute.NoteText : Edm.String "Note Text"
PX.Objects.CS.CSAttribute.tstamp : Edm.Binary
PX.Objects.CS.CSAttribute.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CSAttribute.CreatedByScreenID : Edm.String
PX.Objects.CS.CSAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSAttribute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CSAttribute.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CSAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSAttribute.ObjectName : Edm.String "Schema Object"
PX.Objects.CS.CSAttribute.FieldName : Edm.String "Schema Field"
PX.Objects.CS.CSAttribute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CSAttribute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CSAttribute.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.CS.CSAttribute.AMMTranAttributeCollection -> Collection(PX.Objects.AM.AMMTranAttribute)
PX.Objects.CS.CSAttribute.CSAttributeGroupCollection -> Collection(PX.Objects.CS.CSAttributeGroup)
PX.Objects.CS.CSAttribute.CSAnswersCollection -> Collection(PX.Objects.CS.CSAnswers)
PX.Objects.CS.CSAttribute.CSAttributeDetailCollection -> Collection(PX.Objects.CS.CSAttributeDetail)
PX.Objects.CS.CSAttribute.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.Objects.CS.CSAttribute.INLotSerClassAttributeCollection -> Collection(PX.Objects.IN.INLotSerClassAttribute)
PX.Objects.CS.CSAttribute.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.CS.CSAttribute.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.Objects.CS.CSAttribute.PaymentMethodDetailCollection -> Collection(PX.Objects.CA.PaymentMethodDetail)
PX.Objects.CS.CSAttribute.AMBomAttributeCollection -> Collection(PX.Objects.AM.AMBomAttribute)
PX.Objects.CS.CSAttribute.AMConfigResultsAttributeCollection -> Collection(PX.Objects.AM.AMConfigResultsAttribute)
PX.Objects.CS.CSAttribute.AMConfigurationAttributeCollection -> Collection(PX.Objects.AM.AMConfigurationAttribute)
PX.Objects.CS.CSAttribute.AMFeatureAttributeCollection -> Collection(PX.Objects.AM.AMFeatureAttribute)
PX.Objects.CS.CSAttribute.AMOrderTypeAttributeCollection -> Collection(PX.Objects.AM.AMOrderTypeAttribute)
PX.Objects.CS.CSAttribute.AMProdAttributeCollection -> Collection(PX.Objects.AM.AMProdAttribute)

# PX.Objects.CS.CSAttributeDetail (EntityType)

Label: "Attribute Detail"
Key: AttributeID, ValueID
Entity sets: PX_Objects_CS_CSAttributeDetail, AttributeDetail, CSAttributeDetail
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.CS.CSAttributeDetail.AttributeID : Edm.String [key] "Attribute ID"
PX.Objects.CS.CSAttributeDetail.ValueID : Edm.String [key] "Value ID"
PX.Objects.CS.CSAttributeDetail.Description : Edm.String "Description"
PX.Objects.CS.CSAttributeDetail.SortOrder : Edm.Int16 "Sort Order"
PX.Objects.CS.CSAttributeDetail.Disabled : Edm.Boolean [required] "Disabled"
PX.Objects.CS.CSAttributeDetail.NoteID : Edm.Guid
PX.Objects.CS.CSAttributeDetail.NoteText : Edm.String "Note Text"
PX.Objects.CS.CSAttributeDetail.tstamp : Edm.Binary
PX.Objects.CS.CSAttributeDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CSAttributeDetail.CreatedByScreenID : Edm.String
PX.Objects.CS.CSAttributeDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSAttributeDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CSAttributeDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CSAttributeDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSAttributeDetail.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CS.CSAttributeDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CSAttributeDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CSAttributeDetail.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.CS.CSAttributeDetail.BCMatrixOptionsMappingCollection -> Collection(PX.Commerce.Objects.BCMatrixOptionsMapping)

# PX.Objects.CS.CSAttributeGroup (EntityType)

Label: "Attribute Group"
Key: AttributeID, EntityClassID, EntityType
Entity sets: PX_Objects_CS_CSAttributeGroup, AttributeGroup, CSAttributeGroup
Non-filterable, non-selectable: Description, ControlType

PX.Objects.CS.CSAttributeGroup.AttributeID : Edm.String [key] "Attribute ID"
PX.Objects.CS.CSAttributeGroup.EntityClassID : Edm.String [key] "Entity Class ID"
PX.Objects.CS.CSAttributeGroup.EntityType : Edm.String [key] "Type"
PX.Objects.CS.CSAttributeGroup.SortOrder : Edm.Int16 "Sort Order"
PX.Objects.CS.CSAttributeGroup.Description : Edm.String "Description"
PX.Objects.CS.CSAttributeGroup.Required : Edm.Boolean [required] "Required"
PX.Objects.CS.CSAttributeGroup.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.CSAttributeGroup.ControlType : Edm.Int32 "Control Type"
PX.Objects.CS.CSAttributeGroup.DefaultValue : Edm.String "Default Value"
PX.Objects.CS.CSAttributeGroup.tstamp : Edm.Binary
PX.Objects.CS.CSAttributeGroup.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CSAttributeGroup.CreatedByScreenID : Edm.String
PX.Objects.CS.CSAttributeGroup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSAttributeGroup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CSAttributeGroup.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CSAttributeGroup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSAttributeGroup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CSAttributeGroup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CSAttributeGroup.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.CS.CSAttributeGroup.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.CS.CSAttributeGroup.BCMatrixOptionsMappingCollection -> Collection(PX.Commerce.Objects.BCMatrixOptionsMapping)

# PX.Objects.CS.CSBox (EntityType)

Label: "Box"
Key: BoxID
Entity sets: PX_Objects_CS_CSBox, Box, CSBox

PX.Objects.CS.CSBox.BoxID : Edm.String [key] "Box ID"
PX.Objects.CS.CSBox.MaxWeight : Edm.Decimal [required] "Max. Weight"
PX.Objects.CS.CSBox.BoxWeight : Edm.Decimal [required] "Box Weight"
PX.Objects.CS.CSBox.MaxVolume : Edm.Decimal [required] "Max Volume"
PX.Objects.CS.CSBox.Length : Edm.Decimal "Length"
PX.Objects.CS.CSBox.Width : Edm.Decimal "Width"
PX.Objects.CS.CSBox.Height : Edm.Decimal "Height"
PX.Objects.CS.CSBox.Description : Edm.String "Description"
PX.Objects.CS.CSBox.AllowOverrideDimension : Edm.Boolean [required] "Editable Dimensions"
PX.Objects.CS.CSBox.ActiveByDefault : Edm.Boolean [required] "Active by Default"
PX.Objects.CS.CSBox.tstamp : Edm.Binary
PX.Objects.CS.CSBox.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.CSBox.CreatedByScreenID : Edm.String
PX.Objects.CS.CSBox.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSBox.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CSBox.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CSBox.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSBox.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.CSBox.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CSBox.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.CS.CSBox.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.CS.CSBox.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.CS.CSBox.CarrierPackageCollection -> Collection(PX.Objects.CS.CarrierPackage)

# PX.Objects.CS.CSCalendar (EntityType)

Label: "Calendar"
Key: CalendarID
Entity sets: PX_Objects_CS_CSCalendar, Calendar, CSCalendar
Non-filterable, non-selectable: SunWorkTime, MonWorkTime, TueWorkTime, WedWorkTime, ThuWorkTime, FriWorkTime, SatWorkTime

PX.Objects.CS.CSCalendar.CalendarID : Edm.String [key] "Calendar ID"
PX.Objects.CS.CSCalendar.Description : Edm.String "Description"
PX.Objects.CS.CSCalendar.WorkdayTime : Edm.Int32 [required] "Workday Hours"
PX.Objects.CS.CSCalendar.WorkdayTimeOverride : Edm.Boolean [required] "Override"
PX.Objects.CS.CSCalendar.TimeZone : Edm.String "Time Zone"
PX.Objects.CS.CSCalendar.SunWorkDay : Edm.Boolean [required] "Sunday"
PX.Objects.CS.CSCalendar.SunStartTime : Edm.DateTimeOffset "Sunday Start Time"
PX.Objects.CS.CSCalendar.SunEndTime : Edm.DateTimeOffset "Sunday End Time"
PX.Objects.CS.CSCalendar.SunUnpaidTime : Edm.Int32 "Sun Unpaid Break Time"
PX.Objects.CS.CSCalendar.SunWorkTime : Edm.Int32 "Sun Hours Worked"
PX.Objects.CS.CSCalendar.MonWorkDay : Edm.Boolean [required] "Monday"
PX.Objects.CS.CSCalendar.MonStartTime : Edm.DateTimeOffset "Monday Start Time"
PX.Objects.CS.CSCalendar.MonEndTime : Edm.DateTimeOffset "Monday End Time"
PX.Objects.CS.CSCalendar.MonUnpaidTime : Edm.Int32 "Mon Unpaid Break Time"
PX.Objects.CS.CSCalendar.MonWorkTime : Edm.Int32 "Mon Hours Worked"
PX.Objects.CS.CSCalendar.TueWorkDay : Edm.Boolean [required] "Tuesday"
PX.Objects.CS.CSCalendar.TueStartTime : Edm.DateTimeOffset "Tuesday Start Time"
PX.Objects.CS.CSCalendar.TueEndTime : Edm.DateTimeOffset "Tuesday End Time"
PX.Objects.CS.CSCalendar.TueUnpaidTime : Edm.Int32 "Tue Unpaid Break Time"
PX.Objects.CS.CSCalendar.TueWorkTime : Edm.Int32 "Tue Hours Worked"
PX.Objects.CS.CSCalendar.WedWorkDay : Edm.Boolean [required] "Wednesday"
PX.Objects.CS.CSCalendar.WedStartTime : Edm.DateTimeOffset "Wednesday Start Time"
PX.Objects.CS.CSCalendar.WedEndTime : Edm.DateTimeOffset "Wednesday End Time"
PX.Objects.CS.CSCalendar.WedUnpaidTime : Edm.Int32 "Wed Unpaid Break Time"
PX.Objects.CS.CSCalendar.WedWorkTime : Edm.Int32 "Wed Hours Worked"
PX.Objects.CS.CSCalendar.ThuWorkDay : Edm.Boolean [required] "Thursday"
PX.Objects.CS.CSCalendar.ThuStartTime : Edm.DateTimeOffset "Thursday Start Time"
PX.Objects.CS.CSCalendar.ThuEndTime : Edm.DateTimeOffset "Thursday End Time"
PX.Objects.CS.CSCalendar.ThuUnpaidTime : Edm.Int32 "Thu Unpaid Break Time"
PX.Objects.CS.CSCalendar.ThuWorkTime : Edm.Int32 "Thu Hours Worked"
PX.Objects.CS.CSCalendar.FriWorkDay : Edm.Boolean [required] "Friday"
PX.Objects.CS.CSCalendar.FriStartTime : Edm.DateTimeOffset "Friday Start Time"
PX.Objects.CS.CSCalendar.FriEndTime : Edm.DateTimeOffset "Friday End Time"
PX.Objects.CS.CSCalendar.FriUnpaidTime : Edm.Int32 "Fri Unpaid Break Time"
PX.Objects.CS.CSCalendar.FriWorkTime : Edm.Int32 "Fri Hours Worked"
PX.Objects.CS.CSCalendar.SatWorkDay : Edm.Boolean [required] "Saturday"
PX.Objects.CS.CSCalendar.SatStartTime : Edm.DateTimeOffset "Saturday Start Time"
PX.Objects.CS.CSCalendar.SatEndTime : Edm.DateTimeOffset "Saturday End Time"
PX.Objects.CS.CSCalendar.SatUnpaidTime : Edm.Int32 "Sat Unpaid Break Time"
PX.Objects.CS.CSCalendar.SatWorkTime : Edm.Int32 "Sat Hours Worked"
PX.Objects.CS.CSCalendar.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CS.CSCalendar.FSAppointmentStaffMemberCollection -> Collection(PX.Objects.FS.FSAppointmentStaffMember)
PX.Objects.CS.CSCalendar.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CS.CSCalendar.ProjectManagementSetupCollection -> Collection(PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup)
PX.Objects.CS.CSCalendar.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CS.CSCalendar.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CS.CSCalendar.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CS.CSCalendar.CSCalendarBreakTimeCollection -> Collection(PX.Objects.CS.CSCalendarBreakTime)
PX.Objects.CS.CSCalendar.PREmployeeClassCollection -> Collection(PX.Objects.PR.PREmployeeClass)
PX.Objects.CS.CSCalendar.CarrierCollection -> Collection(PX.Objects.CS.Carrier)
PX.Objects.CS.CSCalendar.INReplenishmentPolicyCollection -> Collection(PX.Objects.IN.INReplenishmentPolicy)
PX.Objects.CS.CSCalendar.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.Objects.CS.CSCalendar.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.CS.CSCalendar.AMMachCollection -> Collection(PX.Objects.AM.AMMach)
PX.Objects.CS.CSCalendar.AMShiftCollection -> Collection(PX.Objects.AM.AMShift)
PX.Objects.CS.CSCalendar.FSSetupCollection -> Collection(PX.Objects.SV.FSSetup)
PX.Objects.CS.CSCalendar.SVSchedulingSetupCollection -> Collection(PX.Objects.SV.SVSchedulingSetup)
PX.Objects.CS.CSCalendar.AMPSetupCollection -> Collection(PX.Objects.AM.AMPSetup)
PX.Objects.CS.CSCalendar.AMRPSetupCollection -> Collection(PX.Objects.AM.AMRPSetup)

# PX.Objects.CS.CSCalendarBreakTime (EntityType)

Label: "Calendar Break Time"
Key: CalendarID, DayOfWeek, StartTime
Entity sets: PX_Objects_CS_CSCalendarBreakTime, CalendarBreakTime1, CSCalendarBreakTime

PX.Objects.CS.CSCalendarBreakTime.CalendarID : Edm.String [key] "Calendar ID"
PX.Objects.CS.CSCalendarBreakTime.DayOfWeek : Edm.Int32 [key required] "Day Of Week"
PX.Objects.CS.CSCalendarBreakTime.StartTime : Edm.DateTimeOffset [key] "Start Time"
PX.Objects.CS.CSCalendarBreakTime.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.CS.CSCalendarBreakTime.BreakTime : Edm.Int32 "Break Duration"
PX.Objects.CS.CSCalendarBreakTime.Description : Edm.String "Description"
PX.Objects.CS.CSCalendarBreakTime.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.CSCalendarBreakTime.LastModifiedByScreenID : Edm.String
PX.Objects.CS.CSCalendarBreakTime.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.CSCalendarBreakTime.tstamp : Edm.Binary
PX.Objects.CS.CSCalendarBreakTime.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.CSCalendarBreakTime.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)

# PX.Objects.CS.CSCalendarExceptions (EntityType)

Label: "Calendar Exception"
Key: CalendarID, Date
Entity sets: PX_Objects_CS_CSCalendarExceptions, CalendarException, CSCalendarExceptions

PX.Objects.CS.CSCalendarExceptions.CalendarID : Edm.String [key] "Calendar ID"
PX.Objects.CS.CSCalendarExceptions.YearID : Edm.Int32 [required] "Year"
PX.Objects.CS.CSCalendarExceptions.Date : Edm.DateTimeOffset [key] "Date"
PX.Objects.CS.CSCalendarExceptions.DayOfWeek : Edm.Int32 [required] "Day Of Week"
PX.Objects.CS.CSCalendarExceptions.Description : Edm.String "Description"
PX.Objects.CS.CSCalendarExceptions.WorkDay : Edm.Boolean [required] "Work Day"
PX.Objects.CS.CSCalendarExceptions.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.CS.CSCalendarExceptions.EndTime : Edm.DateTimeOffset "End Time"
PX.Objects.CS.CSCalendarExceptions.UnpaidTime : Edm.Int32 [required] "Break Duration"
PX.Objects.CS.CSCalendarExceptions.YearIDAsString : Edm.String "Year"

# PX.Objects.CS.DAC.OrganizationBAccount (EntityType)

Label: "Company"
BaseType: PX.Objects.CR.BAccount
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_CS_DAC_OrganizationBAccount, Company, OrganizationBAccount

PX.Objects.CS.DAC.OrganizationBAccount.OrganizationType : Edm.String
PX.Objects.CS.DAC.OrganizationBAccount.OrganizationID : Edm.Int32

# PX.Objects.CS.DaylightShift (EntityType)

Label: "Daylight Shift"
Key: TimeZone, Year
Entity sets: PX_Objects_CS_DaylightShift, DaylightShift
Non-filterable, non-selectable: TimeZoneDescription, OriginalShift

PX.Objects.CS.DaylightShift.Year : Edm.Int32 [key] "Year"
PX.Objects.CS.DaylightShift.TimeZone : Edm.String [key] "TimeZone"
PX.Objects.CS.DaylightShift.TimeZoneDescription : Edm.String "Time Zone"
PX.Objects.CS.DaylightShift.IsActive : Edm.Boolean "Custom"
PX.Objects.CS.DaylightShift.FromDate : Edm.DateTimeOffset "From"
PX.Objects.CS.DaylightShift.ToDate : Edm.DateTimeOffset "To"
PX.Objects.CS.DaylightShift.Shift : Edm.Int32 "Shift (minutes)"
PX.Objects.CS.DaylightShift.OriginalShift : Edm.Double "OriginalShift"

# PX.Objects.CS.Dimension (EntityType)

Label: "Dimension"
Key: DimensionID
Entity sets: PX_Objects_CS_Dimension, Dimension
Non-filterable, non-selectable: MaxLength

PX.Objects.CS.Dimension.DimensionID : Edm.String [key] "Segmented Key ID"
PX.Objects.CS.Dimension.Descr : Edm.String "Description"
PX.Objects.CS.Dimension.Length : Edm.Int16 [required] "Length"
PX.Objects.CS.Dimension.MaxLength : Edm.Int32 "Max Length"
PX.Objects.CS.Dimension.Segments : Edm.Int16 [required] "Segments"
PX.Objects.CS.Dimension.Internal : Edm.Boolean [required]
PX.Objects.CS.Dimension.NumberingID : Edm.String "Numbering ID"
PX.Objects.CS.Dimension.LookupMode : Edm.String "Lookup Mode"
PX.Objects.CS.Dimension.Validate : Edm.Boolean [required] "Allow Adding New Values On the Fly"
PX.Objects.CS.Dimension.SpecificModule : Edm.String "Specific Module"
PX.Objects.CS.Dimension.ParentDimensionID : Edm.String "Parent"
PX.Objects.CS.Dimension.tstamp : Edm.Binary
PX.Objects.CS.Dimension.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.Dimension.CreatedByScreenID : Edm.String
PX.Objects.CS.Dimension.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Dimension.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.Dimension.LastModifiedByScreenID : Edm.String
PX.Objects.CS.Dimension.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Dimension.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.Dimension.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.Dimension.DimensionByParentDimensionID -> PX.Objects.CS.Dimension (ParentDimensionID=DimensionID)
PX.Objects.CS.Dimension.NumberingByNumberingID -> PX.Objects.CS.Numbering (NumberingID=NumberingID)
PX.Objects.CS.Dimension.DimensionCollection -> Collection(PX.Objects.CS.Dimension)
PX.Objects.CS.Dimension.SegmentCollection -> Collection(PX.Objects.CS.Segment)

# PX.Objects.CS.Email.EMailSyncFolder (EntityType)

Label: "EMailSyncFolder"
Key: FolderID, ItemType, SyncAccountNoteID
Entity sets: PX_Objects_CS_Email_EMailSyncFolder, EMailSyncFolder

PX.Objects.CS.Email.EMailSyncFolder.SyncAccountNoteID : Edm.Guid [key]
PX.Objects.CS.Email.EMailSyncFolder.ItemType : Edm.String [key]
PX.Objects.CS.Email.EMailSyncFolder.FolderID : Edm.String [key]
PX.Objects.CS.Email.EMailSyncFolder.Name : Edm.String
PX.Objects.CS.Email.EMailSyncFolder.ParentFolderID : Edm.String
PX.Objects.CS.Email.EMailSyncFolder.FoldersStructureDeltaToken : Edm.String
PX.Objects.CS.Email.EMailSyncFolder.OutlookItemsDeltaToken : Edm.String

# PX.Objects.CS.FeaturesSet (EntityType)

Label: "Features Set"
Key: Status
Entity sets: PX_Objects_CS_FeaturesSet, FeaturesSet
Non-filterable, non-selectable: LicenseID

PX.Objects.CS.FeaturesSet.LicenseID : Edm.String "License ID"
PX.Objects.CS.FeaturesSet.Status : Edm.Int32 [key required] "Activation Status"
PX.Objects.CS.FeaturesSet.ValidUntill : Edm.DateTimeOffset "Next Validation Date"
PX.Objects.CS.FeaturesSet.ValidationCode : Edm.String
PX.Objects.CS.FeaturesSet.FinancialModule : Edm.Boolean [required] "Finance"
PX.Objects.CS.FeaturesSet.FinancialStandard : Edm.Boolean [required] "Standard Financials"
PX.Objects.CS.FeaturesSet.Branch : Edm.Boolean [required] "Multibranch Support"
PX.Objects.CS.FeaturesSet.MultiCompany : Edm.Boolean [required] "Multicompany Support"
PX.Objects.CS.FeaturesSet.AccountLocations : Edm.Boolean [required] "Business Account Locations"
PX.Objects.CS.FeaturesSet.Multicurrency : Edm.Boolean [required] "Multicurrency Accounting"
PX.Objects.CS.FeaturesSet.CentralizedPeriodsManagement : Edm.Boolean [required] "Centralized Period Management"
PX.Objects.CS.FeaturesSet.SupportBreakQty : Edm.Boolean [required] "Volume Pricing"
PX.Objects.CS.FeaturesSet.Prebooking : Edm.Boolean [required] "Expense Reclassification"
PX.Objects.CS.FeaturesSet.TaxEntryFromGL : Edm.Boolean [required] "Tax Entry from GL Module"
PX.Objects.CS.FeaturesSet.VATReporting : Edm.Boolean [required] "VAT Reporting"
PX.Objects.CS.FeaturesSet.VATRecognitionOnPrepaymentsAP : Edm.Boolean [required] "VAT Recognition on AP Prepayments"
PX.Objects.CS.FeaturesSet.VATRecognitionOnPrepaymentsAR : Edm.Boolean [required] "VAT Recognition on AR Prepayments"
PX.Objects.CS.FeaturesSet.Reporting1099 : Edm.Boolean [required] "1099 Reporting"
PX.Objects.CS.FeaturesSet.NetGrossEntryMode : Edm.Boolean [required] "Net/Gross Entry Mode"
PX.Objects.CS.FeaturesSet.InvoiceRounding : Edm.Boolean [required] "Invoice Rounding"
PX.Objects.CS.FeaturesSet.ExpenseManagement : Edm.Boolean [required] "Expense Management"
PX.Objects.CS.FeaturesSet.FinancialAdvanced : Edm.Boolean [required] "Advanced Financials"
PX.Objects.CS.FeaturesSet.SubAccount : Edm.Boolean [required] "Subaccounts"
PX.Objects.CS.FeaturesSet.AllocationTemplates : Edm.Boolean [required] "General Ledger Allocation Templates"
PX.Objects.CS.FeaturesSet.InterBranch : Edm.Boolean [required] "Inter-Branch Transactions"
PX.Objects.CS.FeaturesSet.ProjectAccounting : Edm.Boolean [required] "Projects"
PX.Objects.CS.FeaturesSet.BudgetForecast : Edm.Boolean [required] "Budget Forecast"
PX.Objects.CS.FeaturesSet.ChangeOrder : Edm.Boolean [required] "Change Orders"
PX.Objects.CS.FeaturesSet.ChangeRequest : Edm.Boolean [required] "Change Requests"
PX.Objects.CS.FeaturesSet.Construction : Edm.Boolean [required] "Construction"
PX.Objects.CS.FeaturesSet.ConstructionProjectManagement : Edm.Boolean [required] "Construction Project Management"
PX.Objects.CS.FeaturesSet.ProjectOverview : Edm.Boolean [required] "360 Dashboards"
PX.Objects.CS.FeaturesSet.WeatherServices : Edm.Boolean [required] "Weather Services"
PX.Objects.CS.FeaturesSet.CostCodes : Edm.Boolean [required] "Cost Codes"
PX.Objects.CS.FeaturesSet.ProjectMultiCurrency : Edm.Boolean [required] "Multicurrency Projects"
PX.Objects.CS.FeaturesSet.ProfessionalServices : Edm.Boolean [required] "Professional Services"
PX.Objects.CS.FeaturesSet.ProjectQuotes : Edm.Boolean [required] "Project Quotes"
PX.Objects.CS.FeaturesSet.ProjectParentChild : Edm.Boolean [required] "Parent-Child Projects"
PX.Objects.CS.FeaturesSet.MaterialManagement : Edm.Boolean [required] "Project-Specific Inventory"
PX.Objects.CS.FeaturesSet.FileManagement : Edm.Boolean [required] "Document Management"
PX.Objects.CS.FeaturesSet.MaterialListManagement : Edm.Boolean [required] "Material Management"
PX.Objects.CS.FeaturesSet.VisibilityRestriction : Edm.Boolean [required] "Customer and Vendor Visibility Restriction"
PX.Objects.CS.FeaturesSet.MultipleBaseCurrencies : Edm.Boolean [required] "Multiple Base Currencies"
PX.Objects.CS.FeaturesSet.MultipleCalendarsSupport : Edm.Boolean [required] "Multiple Calendar Support"
PX.Objects.CS.FeaturesSet.GLConsolidation : Edm.Boolean [required] "General Ledger Consolidation"
PX.Objects.CS.FeaturesSet.FinStatementCurTranslation : Edm.Boolean [required] "Translation of Financial Statements"
PX.Objects.CS.FeaturesSet.CustomerDiscounts : Edm.Boolean [required] "Customer Discounts"
PX.Objects.CS.FeaturesSet.VendorDiscounts : Edm.Boolean [required] "Vendor Discounts"
PX.Objects.CS.FeaturesSet.Commissions : Edm.Boolean [required] "Commissions"
PX.Objects.CS.FeaturesSet.OverdueFinCharges : Edm.Boolean [required] "Overdue Charges"
PX.Objects.CS.FeaturesSet.DunningLetter : Edm.Boolean [required] "Dunning Letter Management"
PX.Objects.CS.FeaturesSet.DefferedRevenue : Edm.Boolean [required] "Deferred Revenue Management"
PX.Objects.CS.FeaturesSet.ASC606 : Edm.Boolean [required] "Revenue Recognition by IFRS 15/ASC 606"
PX.Objects.CS.FeaturesSet.ConsolidatedPosting : Edm.Boolean [required] "Consolidated Posting to GL"
PX.Objects.CS.FeaturesSet.ParentChildAccount : Edm.Boolean [required] "Parent-Child Customer Relationship"
PX.Objects.CS.FeaturesSet.Retainage : Edm.Boolean [required] "Retainage Support"
PX.Objects.CS.FeaturesSet.PerUnitTaxSupport : Edm.Boolean [required] "Per Unit/Specific Tax Support"
PX.Objects.CS.FeaturesSet.PaymentsByLines : Edm.Boolean [required] "Payment Application by Line"
PX.Objects.CS.FeaturesSet.ExemptedTaxReporting : Edm.Boolean [required] "Exempted Tax Reporting"
PX.Objects.CS.FeaturesSet.BankTransactionSplits : Edm.Boolean [required] "Bank Transaction Splits"
PX.Objects.CS.FeaturesSet.ContractManagement : Edm.Boolean [required] "Contract Management"
PX.Objects.CS.FeaturesSet.FixedAsset : Edm.Boolean [required] "Fixed Asset Management"
PX.Objects.CS.FeaturesSet.DistributionModule : Edm.Boolean [required] "Inventory and Order Management"
PX.Objects.CS.FeaturesSet.Inventory : Edm.Boolean [required] "Inventory"
PX.Objects.CS.FeaturesSet.MultipleUnitMeasure : Edm.Boolean [required] "Multiple Units of Measure"
PX.Objects.CS.FeaturesSet.LotSerialTracking : Edm.Boolean [required] "Lot and Serial Tracking"
PX.Objects.CS.FeaturesSet.BlanketPO : Edm.Boolean [required] "Blanket and Standard Purchase Orders"
PX.Objects.CS.FeaturesSet.POReceiptsWithoutInventory : Edm.Boolean [required] "Purchase Receipts Without Inventory"
PX.Objects.CS.FeaturesSet.DropShipments : Edm.Boolean [required] "Drop Shipments"
PX.Objects.CS.FeaturesSet.Warehouse : Edm.Boolean [required] "Multiple Warehouses"
PX.Objects.CS.FeaturesSet.OrderOrchestration : Edm.Boolean [required] "Order Orchestration"
PX.Objects.CS.FeaturesSet.AvailableToPromise : Edm.Boolean [required] "Available-to-Promise"
PX.Objects.CS.FeaturesSet.DistributionReqPlan : Edm.Boolean [required] "Distribution Requirements Planning"
PX.Objects.CS.FeaturesSet.WarehouseLocation : Edm.Boolean [required] "Multiple Warehouse Locations"
PX.Objects.CS.FeaturesSet.Replenishment : Edm.Boolean [required] "Inventory Replenishment"
PX.Objects.CS.FeaturesSet.MatrixItem : Edm.Boolean [required] "Matrix Items"
PX.Objects.CS.FeaturesSet.SubItem : Edm.Boolean [required] "Inventory Subitems"
PX.Objects.CS.FeaturesSet.AutoPackaging : Edm.Boolean [required] "Automatic Packaging"
PX.Objects.CS.FeaturesSet.KitAssemblies : Edm.Boolean [required] "Kit Assembly"
PX.Objects.CS.FeaturesSet.RelatedItems : Edm.Boolean [required] "Related Items"
PX.Objects.CS.FeaturesSet.AdvancedPhysicalCounts : Edm.Boolean [required] "Advanced Physical Count"
PX.Objects.CS.FeaturesSet.SOToPOLink : Edm.Boolean [required] "Sales Order to Purchase Order Link"
PX.Objects.CS.FeaturesSet.SpecialOrders : Edm.Boolean [required] "Special Orders"
PX.Objects.CS.FeaturesSet.UserDefinedOrderTypes : Edm.Boolean [required] "Custom Order Types"
PX.Objects.CS.FeaturesSet.PurchaseRequisitions : Edm.Boolean [required] "Purchase Requisitions"
PX.Objects.CS.FeaturesSet.AdvancedSOInvoices : Edm.Boolean [required] "Advanced SO Invoices"
PX.Objects.CS.FeaturesSet.CrossReferenceUniqueness : Edm.Boolean [required] "Cross-Reference Uniqueness"
PX.Objects.CS.FeaturesSet.VendorRelations : Edm.Boolean [required] "Vendor Relations"
PX.Objects.CS.FeaturesSet.AdvancedFulfillment : Edm.Boolean [required] "Warehouse Management"
PX.Objects.CS.FeaturesSet.WMSFulfillment : Edm.Boolean [required] "Fulfillment"
PX.Objects.CS.FeaturesSet.WMSPaperlessPicking : Edm.Boolean [required] "Paperless Picking"
PX.Objects.CS.FeaturesSet.WMSAdvancedPicking : Edm.Boolean [required] "Advanced Picking"
PX.Objects.CS.FeaturesSet.WMSReceiving : Edm.Boolean [required] "Receiving"
PX.Objects.CS.FeaturesSet.WMSInventory : Edm.Boolean [required] "Inventory Operations"
PX.Objects.CS.FeaturesSet.WMSCartTracking : Edm.Boolean [required] "Cart Tracking"
PX.Objects.CS.FeaturesSet.OrganizationModule : Edm.Boolean [required] "Organization"
PX.Objects.CS.FeaturesSet.CustomerModule : Edm.Boolean [required] "Customer Management"
PX.Objects.CS.FeaturesSet.CaseManagement : Edm.Boolean [required] "Case Management"
PX.Objects.CS.FeaturesSet.ContactDuplicate : Edm.Boolean [required] "Duplicate Validation"
PX.Objects.CS.FeaturesSet.SendGridIntegration : Edm.Boolean [required] "SendGrid Integration"
PX.Objects.CS.FeaturesSet.SalesQuotes : Edm.Boolean [required] "Sales Quotes"
PX.Objects.CS.FeaturesSet.AddressLookup : Edm.Boolean [required] "Address Lookup Integration"
PX.Objects.CS.FeaturesSet.ProjectModule : Edm.Boolean [required] "Project Accounting"
PX.Objects.CS.FeaturesSet.ModernPortalModule : Edm.Boolean [required] "Modern Customer Portal"
PX.Objects.CS.FeaturesSet.PortalModule : Edm.Boolean [required] "Customer Portal"
PX.Objects.CS.FeaturesSet.B2BOrdering : Edm.Boolean [required] "B2B Ordering"
PX.Objects.CS.FeaturesSet.PortalCaseManagement : Edm.Boolean [required] "Case Management on Portal"
PX.Objects.CS.FeaturesSet.PortalFinancials : Edm.Boolean [required] "Financials on Portal"
PX.Objects.CS.FeaturesSet.ServiceManagementModule : Edm.Boolean [required] "Service Management"
PX.Objects.CS.FeaturesSet.EquipmentManagementModule : Edm.Boolean [required] "Equipment Management"
PX.Objects.CS.FeaturesSet.RouteManagementModule : Edm.Boolean [required] "Route Management"
PX.Objects.CS.FeaturesSet.NewServiceManagement : Edm.Boolean [required] "Work Order Management"
PX.Objects.CS.FeaturesSet.Scheduling : Edm.Boolean [required] "Scheduling"
PX.Objects.CS.FeaturesSet.AdvancedIntegration : Edm.Boolean [required] "Advanced Integration Engine"
PX.Objects.CS.FeaturesSet.CommerceIntegration : Edm.Boolean [required] "Retail Commerce"
PX.Objects.CS.FeaturesSet.AmazonIntegration : Edm.Boolean [required] "Amazon Connector"
PX.Objects.CS.FeaturesSet.BigCommerceIntegration : Edm.Boolean [required] "BigCommerce Connector"
PX.Objects.CS.FeaturesSet.ShopifyIntegration : Edm.Boolean [required] "Shopify Connector"
PX.Objects.CS.FeaturesSet.ShopifyPOS : Edm.Boolean [required] "Shopify POS Connector"
PX.Objects.CS.FeaturesSet.ShopifyChannelTaxWithheld : Edm.Boolean [required] "Tax Withheld by Marketplaces"
PX.Objects.CS.FeaturesSet.CustomCommerceConnectors : Edm.Boolean [required] "Custom Connectors"
PX.Objects.CS.FeaturesSet.ShopifyB2B : Edm.Boolean [required] "Shopify B2B Integration"
PX.Objects.CS.FeaturesSet.BigCommerceB2B : Edm.Boolean [required] "BigCommerce B2B Integration"
PX.Objects.CS.FeaturesSet.BankFeedIntegration : Edm.Boolean [required] "Bank Feed Integration"
PX.Objects.CS.FeaturesSet.IntegratedCardProcessing : Edm.Boolean [required] "Integrated Card Processing"
PX.Objects.CS.FeaturesSet.AcumaticaPayments : Edm.Boolean [required] "Acumatica Payments"
PX.Objects.CS.FeaturesSet.AuthorizeNetIntegration : Edm.Boolean [required] "Authorize.Net Payment Plug-In"
PX.Objects.CS.FeaturesSet.StripeIntegration : Edm.Boolean [required] "Stripe Payment Plug-In"
PX.Objects.CS.FeaturesSet.CustomCCIntegration : Edm.Boolean [required] "Custom Payment Plug-In"
PX.Objects.CS.FeaturesSet.PayrollModule : Edm.Boolean [required] "Payroll"
PX.Objects.CS.FeaturesSet.ShiftDifferential : Edm.Boolean [required] "Shift Differential"
PX.Objects.CS.FeaturesSet.PayrollUS : Edm.Boolean [required] "US Payroll"
PX.Objects.CS.FeaturesSet.PayrollCAN : Edm.Boolean [required] "Canadian Payroll"
PX.Objects.CS.FeaturesSet.PayrollConstruction : Edm.Boolean [required] "PayrollConstruction"
PX.Objects.CS.FeaturesSet.PlatformModule : Edm.Boolean [required] "Platform"
PX.Objects.CS.FeaturesSet.AIStudioFeatures : Edm.Boolean [required] "AI Studio"
PX.Objects.CS.FeaturesSet.AiAssistant : Edm.Boolean [required] "AI Assistant"
PX.Objects.CS.FeaturesSet.MiscModule : Edm.Boolean [required] "Monitoring & Automation"
PX.Objects.CS.FeaturesSet.TimeReportingModule : Edm.Boolean [required] "Time Management"
PX.Objects.CS.FeaturesSet.ApprovalWorkflow : Edm.Boolean [required] "Approval Workflow"
PX.Objects.CS.FeaturesSet.FieldLevelLogging : Edm.Boolean [required] "Field-Level Audit"
PX.Objects.CS.FeaturesSet.RowLevelSecurity : Edm.Boolean [required] "Row-Level Security"
PX.Objects.CS.FeaturesSet.ScheduleModule : Edm.Boolean [required] "Scheduled Processing"
PX.Objects.CS.FeaturesSet.NotificationModule : Edm.Boolean [required] "Change Notifications"
PX.Objects.CS.FeaturesSet.DeviceHub : Edm.Boolean [required] "DeviceHub"
PX.Objects.CS.FeaturesSet.GDPRCompliance : Edm.Boolean [required] "GDPR Compliance Tools"
PX.Objects.CS.FeaturesSet.SecureBusinessDate : Edm.Boolean [required] "Secure Business Date"
PX.Objects.CS.FeaturesSet.IntegrationModule : Edm.Boolean [required] "Third-Party Integrations"
PX.Objects.CS.FeaturesSet.CarrierIntegration : Edm.Boolean [required] "Shipping Carrier Integration"
PX.Objects.CS.FeaturesSet.FedExCarrierIntegration : Edm.Boolean [required] "FedEx"
PX.Objects.CS.FeaturesSet.UPSCarrierIntegration : Edm.Boolean [required] "UPS"
PX.Objects.CS.FeaturesSet.StampsCarrierIntegration : Edm.Boolean [required] "Stamps.com"
PX.Objects.CS.FeaturesSet.ShipEngineCarrierIntegration : Edm.Boolean [required] "ShipEngine"
PX.Objects.CS.FeaturesSet.EasyPostCarrierIntegration : Edm.Boolean [required] "EasyPost"
PX.Objects.CS.FeaturesSet.PacejetCarrierIntegration : Edm.Boolean [required] "Pacejet"
PX.Objects.CS.FeaturesSet.CustomCarrierIntegration : Edm.Boolean [required] "Custom"
PX.Objects.CS.FeaturesSet.ExchangeIntegration : Edm.Boolean [required] "Exchange Integration"
PX.Objects.CS.FeaturesSet.AvalaraTax : Edm.Boolean [required] "External Tax Calculation Integration"
PX.Objects.CS.FeaturesSet.ECM : Edm.Boolean [required] "Exemption Certificate Management"
PX.Objects.CS.FeaturesSet.AddressValidation : Edm.Boolean [required] "Address Validation Integration"
PX.Objects.CS.FeaturesSet.PaymentProcessor : Edm.Boolean [required] "BILL Integration"
PX.Objects.CS.FeaturesSet.AvidXchange : Edm.Boolean [required] "AvidXchange Integration"
PX.Objects.CS.FeaturesSet.SalesforceIntegration : Edm.Boolean [required] "Salesforce Integration"
PX.Objects.CS.FeaturesSet.HubSpotIntegration : Edm.Boolean [required] "HubSpot Integration"
PX.Objects.CS.FeaturesSet.ProcoreIntegration : Edm.Boolean [required] "Procore Integration"
PX.Objects.CS.FeaturesSet.OutlookIntegration : Edm.Boolean [required] "Outlook Integration"
PX.Objects.CS.FeaturesSet.PDFAnnotatorIntegration : Edm.Boolean [required] "PDF Annotator Integration"
PX.Objects.CS.FeaturesSet.Manufacturing : Edm.Boolean [required] "Manufacturing"
PX.Objects.CS.FeaturesSet.ManufacturingMRP : Edm.Boolean [required] "Material Requirements Planning"
PX.Objects.CS.FeaturesSet.ManufacturingProductConfigurator : Edm.Boolean [required] "Product Configurator"
PX.Objects.CS.FeaturesSet.ManufacturingEstimating : Edm.Boolean [required] "Estimating"
PX.Objects.CS.FeaturesSet.ManufacturingAdvancedPlanning : Edm.Boolean [required] "Advanced Planning and Scheduling (Classic)"
PX.Objects.CS.FeaturesSet.ManufacturingAdvancedPlanningEngine : Edm.Boolean [required] "Advanced Planning and Scheduling (Optimized)"
PX.Objects.CS.FeaturesSet.ManufacturingECC : Edm.Boolean [required] "Engineering Change Control"
PX.Objects.CS.FeaturesSet.ManufacturingDataCollection : Edm.Boolean [required] "Manufacturing Data Collection"
PX.Objects.CS.FeaturesSet.ManufacturingShopFloorKiosk : Edm.Boolean [required] "Shop Floor Kiosk"
PX.Objects.CS.FeaturesSet.ManufacturingBase : Edm.Boolean [required] "Core Manufacturing"
PX.Objects.CS.FeaturesSet.ImageRecognition : Edm.Boolean [required] "Image Recognition for Expense Receipts"
PX.Objects.CS.FeaturesSet.APDocumentRecognition : Edm.Boolean [required] "AP Document Recognition Service"
PX.Objects.CS.FeaturesSet.RouteOptimizer : Edm.Boolean [required] "Workwave Route Optimization"
PX.Objects.CS.FeaturesSet.AdvancedAuthentication : Edm.Boolean [required] "Authentication"
PX.Objects.CS.FeaturesSet.TwoFactorAuthentication : Edm.Boolean [required] "Two-Factor Authentication"
PX.Objects.CS.FeaturesSet.ActiveDirectoryAndOtherExternalSSO : Edm.Boolean [required] "Active Directory and Other External SSO"
PX.Objects.CS.FeaturesSet.OpenIDConnect : Edm.Boolean [required] "OpenID Connect"
PX.Objects.CS.FeaturesSet.CanadianLocalization : Edm.Boolean [required] "Canadian Localization"
PX.Objects.CS.FeaturesSet.UKLocalization : Edm.Boolean [required] "UK Localization"
PX.Objects.CS.FeaturesSet.ExperimentalFeatures : Edm.Boolean [required] "Experimental Features"
PX.Objects.CS.FeaturesSet.ImportSendGridDesigns : Edm.Boolean [required] "Import of SendGrid Designs"
PX.Objects.CS.FeaturesSet.RelatedItemAssistant : Edm.Boolean [required] "Related Item Assistant"
PX.Objects.CS.FeaturesSet.TeamsIntegration : Edm.Boolean [required] "Teams Integration"
PX.Objects.CS.FeaturesSet.ArmToExcel : Edm.Boolean [required] "InsightXL (Excel-Based Financial Reporting)"
PX.Objects.CS.FeaturesSet.IntelligentTextCompletion : Edm.Boolean [required] "Intelligent Text Completion"
PX.Objects.CS.FeaturesSet.GIAnomalyDetection : Edm.Boolean [required] "Anomaly Detection"
PX.Objects.CS.FeaturesSet.AIAutomation : Edm.Boolean [required] "AI Automation"
PX.Objects.CS.FeaturesSet.McpServer : Edm.Boolean [required] "MCP Server"
PX.Objects.CS.FeaturesSet.BankFeedAccountsMultipleMapping : Edm.Boolean [required] "Mapping of Multiple Accounts for Bank Feeds"
PX.Objects.CS.FeaturesSet.SalesTerritoryManagement : Edm.Boolean [required] "Sales Territory Management"
PX.Objects.CS.FeaturesSet.CaseCommitmentsTracking : Edm.Boolean [required] "Case Commitments"
PX.Objects.CS.FeaturesSet.ModernPortalB2BOrdering : Edm.Boolean [required] "B2B Ordering (Modern Portal)"
PX.Objects.CS.FeaturesSet.ModernPortalCaseManagement : Edm.Boolean [required] "Case Management (Modern Portal)"
PX.Objects.CS.FeaturesSet.ModernPortalFinancials : Edm.Boolean [required] "Financials (Modern Portal)"
PX.Objects.CS.FeaturesSet.ModernPortalPayments : Edm.Boolean [required] "Payments (Modern Portal)"
PX.Objects.CS.FeaturesSet.VendorPortalModule : Edm.Boolean [required] "Vendor Portal"
PX.Objects.CS.FeaturesSet.LotSerialAttributes : Edm.Boolean [required] "Lot/Serial Attributes"
PX.Objects.CS.FeaturesSet.ProjectRelatedDocumentsRecognition : Edm.Boolean [required] "Recognition of Project-Related Documents"
PX.Objects.CS.FeaturesSet.InventoryFullTextSearch : Edm.Boolean [required] "Full-Text Search for Inventory"
PX.Objects.CS.FeaturesSet.ClockInClockOut : Edm.Boolean [required] "Clock In and Clock Out"
PX.Objects.CS.FeaturesSet.ESignIntegration : Edm.Boolean [required] "eSign Integration"
PX.Objects.CS.FeaturesSet.HierarchicalGI : Edm.Boolean [required] "Grouped Table Views in Generic Inquiries"
PX.Objects.CS.FeaturesSet.AmexBankFeed : Edm.Boolean [required] "AMEX GL1025 File Import for Bank Feeds"
PX.Objects.CS.FeaturesSet.DataWarehousing : Edm.Boolean [required] "Data Warehousing"
PX.Objects.CS.FeaturesSet.WarehousePlanningStrategy : Edm.Boolean [required] "Warehouse Planning Strategies"
PX.Objects.CS.FeaturesSet.AdvancedTransfers : Edm.Boolean [required] "Advanced Transfers"
PX.Objects.CS.FeaturesSet.ReceiptAgent : Edm.Boolean [required] "Receipt Agent"

# PX.Objects.CS.FOBPoint (EntityType)

Label: "FOB Point"
Key: FOBPointID
Entity sets: PX_Objects_CS_FOBPoint, FOBPoint
Non-filterable, non-selectable: NoteText

PX.Objects.CS.FOBPoint.FOBPointID : Edm.String [key] "FOB Point ID"
PX.Objects.CS.FOBPoint.Description : Edm.String "Description"
PX.Objects.CS.FOBPoint.tstamp : Edm.Binary
PX.Objects.CS.FOBPoint.NoteID : Edm.Guid
PX.Objects.CS.FOBPoint.NoteText : Edm.String "Note Text"
PX.Objects.CS.FOBPoint.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.FOBPoint.CreatedByScreenID : Edm.String
PX.Objects.CS.FOBPoint.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.FOBPoint.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.FOBPoint.LastModifiedByScreenID : Edm.String
PX.Objects.CS.FOBPoint.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.FOBPoint.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.FOBPoint.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.FOBPoint.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.FOBPoint.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CS.FOBPoint.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CS.FOBPoint.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.CS.FOBPoint.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CS.FOBPoint.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CS.FOBPoint.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CS.FOBPoint.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CS.FOBPoint.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.Objects.CS.FOBPoint.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CS.FOBPoint.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CS.FOBPoint.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CS.FOBPoint.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CS.FOBPoint.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)

# PX.Objects.CS.FreightRate (EntityType)

Label: "Freight Rate"
Key: CarrierID, LineNbr
Entity sets: PX_Objects_CS_FreightRate, FreightRate

PX.Objects.CS.FreightRate.CarrierID : Edm.String [key]
PX.Objects.CS.FreightRate.LineNbr : Edm.Int32 [key]
PX.Objects.CS.FreightRate.Weight : Edm.Decimal "Weight"
PX.Objects.CS.FreightRate.Volume : Edm.Decimal "Volume"
PX.Objects.CS.FreightRate.ZoneID : Edm.String "Zone ID"
PX.Objects.CS.FreightRate.Rate : Edm.Decimal [required] "Rate"
PX.Objects.CS.FreightRate.tstamp : Edm.Binary
PX.Objects.CS.FreightRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.FreightRate.CreatedByScreenID : Edm.String
PX.Objects.CS.FreightRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.FreightRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.FreightRate.LastModifiedByScreenID : Edm.String
PX.Objects.CS.FreightRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.FreightRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.FreightRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.FreightRate.CarrierByCarrierID -> PX.Objects.CS.Carrier (CarrierID=CarrierID)
PX.Objects.CS.FreightRate.ShippingZoneByZoneID -> PX.Objects.CS.ShippingZone (ZoneID=ZoneID)

# PX.Objects.CS.NotificationRecipient (EntityType)

Label: "Notification Recipient"
Key: NotificationID
Entity sets: PX_Objects_CS_NotificationRecipient, NotificationRecipient
Non-filterable, non-selectable: OriginalContactID, Hidden, Email, OrderID

PX.Objects.CS.NotificationRecipient.NotificationID : Edm.Int32 [key] "Notification ID"
PX.Objects.CS.NotificationRecipient.SetupID : Edm.Guid
PX.Objects.CS.NotificationRecipient.SourceID : Edm.Int32
PX.Objects.CS.NotificationRecipient.ClassID : Edm.String
PX.Objects.CS.NotificationRecipient.RefNoteID : Edm.Guid
PX.Objects.CS.NotificationRecipient.ContactType : Edm.String "Contact Type"
PX.Objects.CS.NotificationRecipient.ContactID : Edm.Int32 "Contact ID"
PX.Objects.CS.NotificationRecipient.OriginalContactID : Edm.Int32 "OriginalContactID"
PX.Objects.CS.NotificationRecipient.Format : Edm.String "Format"
PX.Objects.CS.NotificationRecipient.Active : Edm.Boolean "Active"
PX.Objects.CS.NotificationRecipient.AddTo : Edm.String "Add To"
PX.Objects.CS.NotificationRecipient.Hidden : Edm.Boolean "Bcc"
PX.Objects.CS.NotificationRecipient.Email : Edm.String "Email"
PX.Objects.CS.NotificationRecipient.OrderID : Edm.Int32
PX.Objects.CS.NotificationRecipient.tstamp : Edm.Binary
PX.Objects.CS.NotificationRecipient.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.NotificationRecipient.CreatedByScreenID : Edm.String
PX.Objects.CS.NotificationRecipient.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationRecipient.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.NotificationRecipient.LastModifiedByScreenID : Edm.String
PX.Objects.CS.NotificationRecipient.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationRecipient.NotificationSetupBySetupID -> PX.Objects.CS.NotificationSetup (SetupID=SetupID)
PX.Objects.CS.NotificationRecipient.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CS.NotificationRecipient.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.NotificationRecipient.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.NotificationRecipient.NotificationSourceBySourceID -> PX.Objects.CS.NotificationSource (SourceID=SourceID)

# PX.Objects.CS.NotificationSetup (EntityType)

Label: "Default Notification setup"
Key: SetupID
Entity sets: PX_Objects_CS_NotificationSetup, DefaultNotificationsetup, NotificationSetup

PX.Objects.CS.NotificationSetup.SetupID : Edm.Guid [key]
PX.Objects.CS.NotificationSetup.Module : Edm.String "Module"
PX.Objects.CS.NotificationSetup.SourceCD : Edm.String "Source"
PX.Objects.CS.NotificationSetup.NotificationCD : Edm.String "Mailing ID"
PX.Objects.CS.NotificationSetup.EMailAccountID : Edm.Int32 "Default Email Account"
PX.Objects.CS.NotificationSetup.ReportID : Edm.String "Report ID"
PX.Objects.CS.NotificationSetup.NotificationID : Edm.Int32 "Email Template"
PX.Objects.CS.NotificationSetup.Format : Edm.String "Format"
PX.Objects.CS.NotificationSetup.Active : Edm.Boolean [required] "Active"
PX.Objects.CS.NotificationSetup.RecipientsBehavior : Edm.String "Recipients"
PX.Objects.CS.NotificationSetup.ShipVia : Edm.String
PX.Objects.CS.NotificationSetup.tstamp : Edm.Binary
PX.Objects.CS.NotificationSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.NotificationSetup.CreatedByScreenID : Edm.String
PX.Objects.CS.NotificationSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.NotificationSetup.LastModifiedByScreenID : Edm.String
PX.Objects.CS.NotificationSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationSetup.SiteMapByReportID -> PX.SM.SiteMap (ReportID=NodeID)
PX.Objects.CS.NotificationSetup.BranchByNBranchID -> PX.Objects.GL.Branch
PX.Objects.CS.NotificationSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.NotificationSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.NotificationSetup.NotificationByNotificationID -> PX.SM.Notification (NotificationID=NotificationID)
PX.Objects.CS.NotificationSetup.EMailAccountByEMailAccountID -> PX.SM.EMailAccount (EMailAccountID=EmailAccountID)
PX.Objects.CS.NotificationSetup.SMPrinterByDefaultPrinterID -> PX.SM.SMPrinter
PX.Objects.CS.NotificationSetup.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.CS.NotificationSetup.NotificationSetupRecipientCollection -> Collection(PX.Objects.CS.NotificationSetupRecipient)
PX.Objects.CS.NotificationSetup.NotificationRecipientCollection -> Collection(PX.Objects.CS.NotificationRecipient)
PX.Objects.CS.NotificationSetup.NotificationSetupUserOverrideCollection -> Collection(PX.Objects.CS.NotificationSetupUserOverride)
PX.Objects.CS.NotificationSetup.NotificationSourceCollection -> Collection(PX.Objects.CS.NotificationSource)

# PX.Objects.CS.NotificationSetupRecipient (EntityType)

Label: "Default Notification Recipient"
Key: RecipientID
Entity sets: PX_Objects_CS_NotificationSetupRecipient, DefaultNotificationRecipient, NotificationSetupRecipient
Non-filterable, non-selectable: OriginalContactID, Hidden, Email

PX.Objects.CS.NotificationSetupRecipient.RecipientID : Edm.Guid [key]
PX.Objects.CS.NotificationSetupRecipient.SetupID : Edm.Guid
PX.Objects.CS.NotificationSetupRecipient.ContactType : Edm.String "Contact Type"
PX.Objects.CS.NotificationSetupRecipient.ContactID : Edm.Int32
PX.Objects.CS.NotificationSetupRecipient.OriginalContactID : Edm.Int32 "OriginalContactID"
PX.Objects.CS.NotificationSetupRecipient.Format : Edm.String "Format"
PX.Objects.CS.NotificationSetupRecipient.Active : Edm.Boolean "Active"
PX.Objects.CS.NotificationSetupRecipient.AddTo : Edm.String "Add To"
PX.Objects.CS.NotificationSetupRecipient.Hidden : Edm.Boolean "Bcc"
PX.Objects.CS.NotificationSetupRecipient.Email : Edm.String "Email"
PX.Objects.CS.NotificationSetupRecipient.tstamp : Edm.Binary
PX.Objects.CS.NotificationSetupRecipient.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.NotificationSetupRecipient.CreatedByScreenID : Edm.String
PX.Objects.CS.NotificationSetupRecipient.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationSetupRecipient.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.NotificationSetupRecipient.LastModifiedByScreenID : Edm.String
PX.Objects.CS.NotificationSetupRecipient.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationSetupRecipient.NotificationSetupBySetupID -> PX.Objects.CS.NotificationSetup (SetupID=SetupID)
PX.Objects.CS.NotificationSetupRecipient.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.NotificationSetupRecipient.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CS.NotificationSetupUserOverride (EntityType)

Label: "User's Notification Setup"
Key: SetupID, UserID
Entity sets: PX_Objects_CS_NotificationSetupUserOverride, UsersNotificationSetup, NotificationSetupUserOverride
Non-filterable, non-selectable: ReportID

PX.Objects.CS.NotificationSetupUserOverride.UserID : Edm.Guid [key]
PX.Objects.CS.NotificationSetupUserOverride.SetupID : Edm.Guid [key] "Mailing ID"
PX.Objects.CS.NotificationSetupUserOverride.ReportID : Edm.String "Report ID"
PX.Objects.CS.NotificationSetupUserOverride.Active : Edm.Boolean [required] "Active"
PX.Objects.CS.NotificationSetupUserOverride.ShipVia : Edm.String "Ship Via"
PX.Objects.CS.NotificationSetupUserOverride.tstamp : Edm.Binary
PX.Objects.CS.NotificationSetupUserOverride.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.NotificationSetupUserOverride.CreatedByScreenID : Edm.String
PX.Objects.CS.NotificationSetupUserOverride.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationSetupUserOverride.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.NotificationSetupUserOverride.LastModifiedByScreenID : Edm.String
PX.Objects.CS.NotificationSetupUserOverride.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationSetupUserOverride.NotificationSetupBySetupID -> PX.Objects.CS.NotificationSetup (SetupID=SetupID)
PX.Objects.CS.NotificationSetupUserOverride.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.CS.NotificationSetupUserOverride.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.NotificationSetupUserOverride.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.NotificationSetupUserOverride.SMPrinterByDefaultPrinterID -> PX.SM.SMPrinter
PX.Objects.CS.NotificationSetupUserOverride.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)

# PX.Objects.CS.NotificationSource (EntityType)

Label: "Notification Source"
Key: SetupID, SourceID
Entity sets: PX_Objects_CS_NotificationSource, NotificationSource
Non-filterable, non-selectable: OverrideSource

PX.Objects.CS.NotificationSource.SourceID : Edm.Int32 [key]
PX.Objects.CS.NotificationSource.SetupID : Edm.Guid [key] "Mailing ID"
PX.Objects.CS.NotificationSource.RefNoteID : Edm.Guid
PX.Objects.CS.NotificationSource.ClassID : Edm.String "Class ID"
PX.Objects.CS.NotificationSource.EMailAccountID : Edm.Int32 "Email Account"
PX.Objects.CS.NotificationSource.ReportID : Edm.String "Report"
PX.Objects.CS.NotificationSource.NotificationID : Edm.Int32 "Email Template"
PX.Objects.CS.NotificationSource.Format : Edm.String "Format"
PX.Objects.CS.NotificationSource.Active : Edm.Boolean "Active"
PX.Objects.CS.NotificationSource.RecipientsBehavior : Edm.String "Recipients"
PX.Objects.CS.NotificationSource.OverrideSource : Edm.Boolean "Overridden"
PX.Objects.CS.NotificationSource.tstamp : Edm.Binary
PX.Objects.CS.NotificationSource.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.NotificationSource.CreatedByScreenID : Edm.String
PX.Objects.CS.NotificationSource.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationSource.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.NotificationSource.LastModifiedByScreenID : Edm.String
PX.Objects.CS.NotificationSource.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NotificationSource.NotificationSetupBySetupID -> PX.Objects.CS.NotificationSetup (SetupID=SetupID)
PX.Objects.CS.NotificationSource.BranchByNBranchID -> PX.Objects.GL.Branch
PX.Objects.CS.NotificationSource.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.NotificationSource.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.NotificationSource.NotificationByNotificationID -> PX.SM.Notification (NotificationID=NotificationID)
PX.Objects.CS.NotificationSource.EMailAccountByEMailAccountID -> PX.SM.EMailAccount (EMailAccountID=EmailAccountID)
PX.Objects.CS.NotificationSource.NotificationRecipientCollection -> Collection(PX.Objects.CS.NotificationRecipient)

# PX.Objects.CS.Numbering (EntityType)

Label: "Numbering Sequence"
Key: NumberingID
Entity sets: PX_Objects_CS_Numbering, NumberingSequence, Numbering
Non-filterable, non-selectable: NoteText

PX.Objects.CS.Numbering.NumberingID : Edm.String [key] "Numbering ID"
PX.Objects.CS.Numbering.Descr : Edm.String "Description"
PX.Objects.CS.Numbering.UserNumbering : Edm.Boolean [required] "Manual Numbering"
PX.Objects.CS.Numbering.NewSymbol : Edm.String "New Number Symbol"
PX.Objects.CS.Numbering.tstamp : Edm.Binary
PX.Objects.CS.Numbering.NoteID : Edm.Guid
PX.Objects.CS.Numbering.NoteText : Edm.String "Note Text"
PX.Objects.CS.Numbering.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.Numbering.CreatedByScreenID : Edm.String
PX.Objects.CS.Numbering.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Numbering.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.Numbering.LastModifiedByScreenID : Edm.String
PX.Objects.CS.Numbering.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Numbering.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.Numbering.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.Numbering.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CS.Numbering.ProjectManagementSetupCollection -> Collection(PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup)
PX.Objects.CS.Numbering.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.CS.Numbering.SOOrderTypeCollection -> Collection(PX.Objects.SO.SOOrderType)
PX.Objects.CS.Numbering.PhotoLogSetupCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLogSetup)
PX.Objects.CS.Numbering.DrawingLogSetupCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLogSetup)
PX.Objects.CS.Numbering.SCSetupCollection -> Collection(PX.Objects.CN.SCSetup)
PX.Objects.CS.Numbering.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.CS.Numbering.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.CS.Numbering.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.Objects.CS.Numbering.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.CS.Numbering.TXSetupCollection -> Collection(PX.Objects.TX.TXSetup)
PX.Objects.CS.Numbering.SOSetupCollection -> Collection(PX.Objects.SO.SOSetup)
PX.Objects.CS.Numbering.RQSetupCollection -> Collection(PX.Objects.RQ.RQSetup)
PX.Objects.CS.Numbering.PRSetupCollection -> Collection(PX.Objects.PR.PRSetup)
PX.Objects.CS.Numbering.POSetupCollection -> Collection(PX.Objects.PO.POSetup)
PX.Objects.CS.Numbering.FASetupCollection -> Collection(PX.Objects.FA.FASetup)
PX.Objects.CS.Numbering.DimensionCollection -> Collection(PX.Objects.CS.Dimension)
PX.Objects.CS.Numbering.NumberingSequenceCollection -> Collection(PX.Objects.CS.NumberingSequence)
PX.Objects.CS.Numbering.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.CS.Numbering.CMSetupCollection -> Collection(PX.Objects.CM.CMSetup)
PX.Objects.CS.Numbering.GLSetupCollection -> Collection(PX.Objects.GL.GLSetup)
PX.Objects.CS.Numbering.CASetupCollection -> Collection(PX.Objects.CA.CASetup)
PX.Objects.CS.Numbering.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.CS.Numbering.APSetupCollection -> Collection(PX.Objects.AP.APSetup)
PX.Objects.CS.Numbering.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.CS.Numbering.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.CS.Numbering.AMEstimateSetupCollection -> Collection(PX.Objects.AM.AMEstimateSetup)
PX.Objects.CS.Numbering.AMMPSTypeCollection -> Collection(PX.Objects.AM.AMMPSType)
PX.Objects.CS.Numbering.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.Objects.CS.Numbering.FSRouteSetupCollection -> Collection(PX.Objects.FS.FSRouteSetup)
PX.Objects.CS.Numbering.FSSetupCollection -> Collection(PX.Objects.SV.FSSetup)
PX.Objects.CS.Numbering.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.CS.Numbering.SVSetupCollection -> Collection(PX.Objects.SV.SVSetup)
PX.Objects.CS.Numbering.DRSetupCollection -> Collection(PX.Objects.DR.DRSetup)
PX.Objects.CS.Numbering.AMBSetupCollection -> Collection(PX.Objects.AM.AMBSetup)
PX.Objects.CS.Numbering.AMConfiguratorSetupCollection -> Collection(PX.Objects.AM.AMConfiguratorSetup)
PX.Objects.CS.Numbering.AMPSetupCollection -> Collection(PX.Objects.AM.AMPSetup)
PX.Objects.CS.Numbering.AMRPSetupCollection -> Collection(PX.Objects.AM.AMRPSetup)

# PX.Objects.CS.NumberingSequence (EntityType)

Label: "Numbering Sequence Detail"
Key: NumberingID, NumberingSEQ
Entity sets: PX_Objects_CS_NumberingSequence, NumberingSequenceDetail, NumberingSequence1

PX.Objects.CS.NumberingSequence.NumberingID : Edm.String [key] "Numbering ID"
PX.Objects.CS.NumberingSequence.NumberingSEQ : Edm.Int32 [key] "Numbering Seq"
PX.Objects.CS.NumberingSequence.StartNbr : Edm.String "Start Number"
PX.Objects.CS.NumberingSequence.EndNbr : Edm.String "End Number"
PX.Objects.CS.NumberingSequence.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.CS.NumberingSequence.LastNbr : Edm.String "Last Number"
PX.Objects.CS.NumberingSequence.WarnNbr : Edm.String "Warning Number"
PX.Objects.CS.NumberingSequence.NbrStep : Edm.Int32 [required] "Numbering Step"
PX.Objects.CS.NumberingSequence.tstamp : Edm.Binary
PX.Objects.CS.NumberingSequence.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.NumberingSequence.CreatedByScreenID : Edm.String
PX.Objects.CS.NumberingSequence.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NumberingSequence.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.NumberingSequence.LastModifiedByScreenID : Edm.String
PX.Objects.CS.NumberingSequence.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.NumberingSequence.BranchByNBranchID -> PX.Objects.GL.Branch
PX.Objects.CS.NumberingSequence.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.NumberingSequence.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.NumberingSequence.NumberingByNumberingID -> PX.Objects.CS.Numbering (NumberingID=NumberingID)

# PX.Objects.CS.ReasonCode (EntityType)

Label: "Reason Code"
Key: ReasonCodeID
Entity sets: PX_Objects_CS_ReasonCode, ReasonCode
Non-filterable, non-selectable: NoteText

PX.Objects.CS.ReasonCode.ReasonCodeID : Edm.String [key] "Reason Code"
PX.Objects.CS.ReasonCode.Descr : Edm.String "Description"
PX.Objects.CS.ReasonCode.Usage : Edm.String "Usage"
PX.Objects.CS.ReasonCode.SubMask : Edm.String "Combine Sub from Combined"
PX.Objects.CS.ReasonCode.NoteID : Edm.Guid
PX.Objects.CS.ReasonCode.NoteText : Edm.String "Note Text"
PX.Objects.CS.ReasonCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.ReasonCode.CreatedByScreenID : Edm.String
PX.Objects.CS.ReasonCode.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CS.ReasonCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.ReasonCode.LastModifiedByScreenID : Edm.String
PX.Objects.CS.ReasonCode.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CS.ReasonCode.tstamp : Edm.Binary
PX.Objects.CS.ReasonCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.ReasonCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.ReasonCode.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CS.ReasonCode.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.CS.ReasonCode.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CS.ReasonCode.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.CS.ReasonCode.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.CS.ReasonCode.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.CS.ReasonCode.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.CS.ReasonCode.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.CS.ReasonCode.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CS.ReasonCode.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.CS.ReasonCode.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.CS.ReasonCode.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.CS.ReasonCode.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.CS.ReasonCode.POSetupCollection -> Collection(PX.Objects.PO.POSetup)
PX.Objects.CS.ReasonCode.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.CS.ReasonCode.INPostClassCollection -> Collection(PX.Objects.IN.INPostClass)
PX.Objects.CS.ReasonCode.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.CS.ReasonCode.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.CS.ReasonCode.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.CS.ReasonCode.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.CS.ReasonCode.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.CS.ReasonCode.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.CS.ReasonCode.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)

# PX.Objects.CS.SalesTerritory (EntityType)

Label: "Sales Territory"
Key: SalesTerritoryID
Entity sets: PX_Objects_CS_SalesTerritory, SalesTerritory
Non-filterable, non-selectable: NoteText

PX.Objects.CS.SalesTerritory.SalesTerritoryID : Edm.String [key] "Sales Territory"
PX.Objects.CS.SalesTerritory.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.SalesTerritory.SalesTerritoryType : Edm.String "Territory Type"
PX.Objects.CS.SalesTerritory.CountryID : Edm.String "Country"
PX.Objects.CS.SalesTerritory.NoteID : Edm.Guid
PX.Objects.CS.SalesTerritory.NoteText : Edm.String "Note Text"
PX.Objects.CS.SalesTerritory.tstamp : Edm.Binary
PX.Objects.CS.SalesTerritory.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.SalesTerritory.CreatedByScreenID : Edm.String
PX.Objects.CS.SalesTerritory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.SalesTerritory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.SalesTerritory.LastModifiedByScreenID : Edm.String
PX.Objects.CS.SalesTerritory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.SalesTerritory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.SalesTerritory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.SalesTerritory.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.CS.SalesTerritory.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CS.SalesTerritory.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CS.SalesTerritory.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CS.SalesTerritory.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CS.SalesTerritory.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.CS.SalesTerritory.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.CS.SalesTerritory.CountryCollection -> Collection(PX.Objects.CS.Country)
PX.Objects.CS.SalesTerritory.StateCollection -> Collection(PX.Objects.CS.State)
PX.Objects.CS.SalesTerritory.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CS.SalesTerritory.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CS.SalesTerritory.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CS.SalesTerritory.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)

# PX.Objects.CS.Segment (EntityType)

Label: "Segment"
Key: DimensionID, SegmentID
Entity sets: PX_Objects_CS_Segment, Segment
Non-filterable, non-selectable: Inherited, IsOverrideForUI

PX.Objects.CS.Segment.DimensionID : Edm.String [key] "Segmented Key ID"
PX.Objects.CS.Segment.SegmentID : Edm.Int16 [key] "Segment ID"
PX.Objects.CS.Segment.Descr : Edm.String "Description"
PX.Objects.CS.Segment.Length : Edm.Int16 [required] "Length"
PX.Objects.CS.Segment.Align : Edm.Int16 [required] "Align"
PX.Objects.CS.Segment.FillCharacter : Edm.String "Fill Character"
PX.Objects.CS.Segment.PromptCharacter : Edm.String "Prompt Character"
PX.Objects.CS.Segment.EditMask : Edm.String "Edit Mask"
PX.Objects.CS.Segment.CaseConvert : Edm.Int16 [required] "Case Conversion"
PX.Objects.CS.Segment.Validate : Edm.Boolean [required] "Validate"
PX.Objects.CS.Segment.AutoNumber : Edm.Boolean [required] "Auto Number"
PX.Objects.CS.Segment.Separator : Edm.String "Separator"
PX.Objects.CS.Segment.tstamp : Edm.Binary
PX.Objects.CS.Segment.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.Segment.CreatedByScreenID : Edm.String
PX.Objects.CS.Segment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Segment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.Segment.LastModifiedByScreenID : Edm.String
PX.Objects.CS.Segment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Segment.ConsolOrder : Edm.Int16 [required] "Consol. Order"
PX.Objects.CS.Segment.ConsolNumChar : Edm.Int16 [required] "Number of characters"
PX.Objects.CS.Segment.IsCosted : Edm.Boolean "Include in Cost"
PX.Objects.CS.Segment.ParentDimensionID : Edm.String
PX.Objects.CS.Segment.Inherited : Edm.Boolean
PX.Objects.CS.Segment.IsOverrideForUI : Edm.Boolean "Override"
PX.Objects.CS.Segment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.Segment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.Segment.DimensionByDimensionID -> PX.Objects.CS.Dimension (DimensionID=DimensionID)
PX.Objects.CS.Segment.SegmentValueCollection -> Collection(PX.Objects.CS.SegmentValue)
PX.Objects.CS.Segment.GLSetupCollection -> Collection(PX.Objects.GL.GLSetup)

# PX.Objects.CS.SegmentValue (EntityType)

Label: "Segment Value"
Key: DimensionID, SegmentID, Value
Entity sets: PX_Objects_CS_SegmentValue, SegmentValue
Non-filterable, non-selectable: Included, Secured

PX.Objects.CS.SegmentValue.DimensionID : Edm.String [key] "Segmented Key ID"
PX.Objects.CS.SegmentValue.SegmentID : Edm.Int16 [key] "Segment ID"
PX.Objects.CS.SegmentValue.Value : Edm.String [key] "Value"
PX.Objects.CS.SegmentValue.Descr : Edm.String "Description"
PX.Objects.CS.SegmentValue.Active : Edm.Boolean [required] "Active"
PX.Objects.CS.SegmentValue.IsConsolidatedValue : Edm.Boolean "Aggregation"
PX.Objects.CS.SegmentValue.tstamp : Edm.Binary
PX.Objects.CS.SegmentValue.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.SegmentValue.CreatedByScreenID : Edm.String
PX.Objects.CS.SegmentValue.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.SegmentValue.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.SegmentValue.LastModifiedByScreenID : Edm.String
PX.Objects.CS.SegmentValue.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.SegmentValue.MappedSegValue : Edm.String "Mapped Value"
PX.Objects.CS.SegmentValue.Included : Edm.Boolean "Included"
PX.Objects.CS.SegmentValue.Secured : Edm.Boolean "Secured"
PX.Objects.CS.SegmentValue.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.SegmentValue.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.SegmentValue.SegmentBySegmentID -> PX.Objects.CS.Segment (DimensionID=DimensionID, SegmentID=SegmentID)
PX.Objects.CS.SegmentValue.GLConsolSetupCollection -> Collection(PX.Objects.GL.GLConsolSetup)

# PX.Objects.CS.ShippingZone (EntityType)

Label: "Shipping Zone"
Key: ZoneID
Entity sets: PX_Objects_CS_ShippingZone, ShippingZone

PX.Objects.CS.ShippingZone.ZoneID : Edm.String [key] "Zone ID"
PX.Objects.CS.ShippingZone.Description : Edm.String "Description"
PX.Objects.CS.ShippingZone.ShippingZoneLineCntr : Edm.Int32 [required]
PX.Objects.CS.ShippingZone.tstamp : Edm.Binary
PX.Objects.CS.ShippingZone.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.ShippingZone.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.ShippingZone.CreatedByScreenID : Edm.String
PX.Objects.CS.ShippingZone.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.ShippingZone.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.ShippingZone.LastModifiedByScreenID : Edm.String
PX.Objects.CS.ShippingZone.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.ShippingZone.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.ShippingZone.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.ShippingZone.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CS.ShippingZone.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.CS.ShippingZone.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CS.ShippingZone.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CS.ShippingZone.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.CS.ShippingZone.SOOrchestrationPlanCollection -> Collection(PX.Objects.SO.SOOrchestrationPlan)
PX.Objects.CS.ShippingZone.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CS.ShippingZone.FreightRateCollection -> Collection(PX.Objects.CS.FreightRate)
PX.Objects.CS.ShippingZone.ShippingZoneLineCollection -> Collection(PX.Objects.CS.ShippingZoneLine)
PX.Objects.CS.ShippingZone.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CS.ShippingZone.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CS.ShippingZone.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CS.ShippingZone.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CS.ShippingZone.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CS.ShippingZone.BCShippingMappingsCollection -> Collection(PX.Commerce.Objects.BCShippingMappings)

# PX.Objects.CS.ShippingZoneLine (EntityType)

Label: "Shipping Zone Line"
Key: LineNbr, ZoneID
Entity sets: PX_Objects_CS_ShippingZoneLine, ShippingZoneLine

PX.Objects.CS.ShippingZoneLine.ZoneID : Edm.String [key]
PX.Objects.CS.ShippingZoneLine.LineNbr : Edm.Int32 [key]
PX.Objects.CS.ShippingZoneLine.CountryID : Edm.String "Country"
PX.Objects.CS.ShippingZoneLine.StateID : Edm.String "State"
PX.Objects.CS.ShippingZoneLine.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.ShippingZoneLine.CreatedByScreenID : Edm.String
PX.Objects.CS.ShippingZoneLine.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.ShippingZoneLine.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.ShippingZoneLine.LastModifiedByScreenID : Edm.String
PX.Objects.CS.ShippingZoneLine.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.ShippingZoneLine.tstamp : Edm.Binary
PX.Objects.CS.ShippingZoneLine.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.ShippingZoneLine.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.ShippingZoneLine.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.CS.ShippingZoneLine.ShippingZoneByZoneID -> PX.Objects.CS.ShippingZone (ZoneID=ZoneID)
PX.Objects.CS.ShippingZoneLine.StateByStateID -> PX.Objects.CS.State (CountryID=CountryID, StateID=StateID)
PX.Objects.CS.ShippingZoneLine.StateByCountryID -> PX.Objects.CS.State (StateID=StateID, CountryID=CountryID)

# PX.Objects.CS.ShipTerms (EntityType)

Label: "Shipping Terms"
Key: ShipTermsID
Entity sets: PX_Objects_CS_ShipTerms, ShippingTerms, ShipTerms
Non-filterable, non-selectable: NoteText

PX.Objects.CS.ShipTerms.ShipTermsID : Edm.String [key] "Term ID"
PX.Objects.CS.ShipTerms.FreightAmountSource : Edm.String "Invoice Freight Price Based On"
PX.Objects.CS.ShipTerms.Description : Edm.String "Description"
PX.Objects.CS.ShipTerms.tstamp : Edm.Binary
PX.Objects.CS.ShipTerms.NoteID : Edm.Guid
PX.Objects.CS.ShipTerms.NoteText : Edm.String "Note Text"
PX.Objects.CS.ShipTerms.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.ShipTerms.CreatedByScreenID : Edm.String
PX.Objects.CS.ShipTerms.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CS.ShipTerms.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.ShipTerms.LastModifiedByScreenID : Edm.String
PX.Objects.CS.ShipTerms.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CS.ShipTerms.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CS.ShipTerms.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.ShipTerms.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.ShipTerms.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CS.ShipTerms.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.CS.ShipTerms.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CS.ShipTerms.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CS.ShipTerms.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CS.ShipTerms.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CS.ShipTerms.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.CS.ShipTerms.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CS.ShipTerms.ShipTermsDetailCollection -> Collection(PX.Objects.CS.ShipTermsDetail)
PX.Objects.CS.ShipTerms.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CS.ShipTerms.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CS.ShipTerms.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CS.ShipTerms.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CS.ShipTerms.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CS.ShipTerms.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CS.ShipTerms.BCShippingMappingsCollection -> Collection(PX.Commerce.Objects.BCShippingMappings)

# PX.Objects.CS.ShipTermsDetail (EntityType)

Label: "Shiping Terms Detail"
Key: LineNbr, ShipTermsID
Entity sets: PX_Objects_CS_ShipTermsDetail, ShipingTermsDetail, ShipTermsDetail

PX.Objects.CS.ShipTermsDetail.ShipTermsID : Edm.String [key]
PX.Objects.CS.ShipTermsDetail.LineNbr : Edm.Int32 [key]
PX.Objects.CS.ShipTermsDetail.BreakAmount : Edm.Decimal [required] "Break Amount"
PX.Objects.CS.ShipTermsDetail.FreightCostPercent : Edm.Decimal [required] "Freight Cost %"
PX.Objects.CS.ShipTermsDetail.InvoiceAmountPercent : Edm.Decimal [required] "Invoice Amount %"
PX.Objects.CS.ShipTermsDetail.ShippingHandling : Edm.Decimal [required] "Shipping and Handling"
PX.Objects.CS.ShipTermsDetail.LineHandling : Edm.Decimal [required] "Line Handling"
PX.Objects.CS.ShipTermsDetail.tstamp : Edm.Binary
PX.Objects.CS.ShipTermsDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.ShipTermsDetail.CreatedByScreenID : Edm.String
PX.Objects.CS.ShipTermsDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.ShipTermsDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.ShipTermsDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CS.ShipTermsDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.ShipTermsDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.ShipTermsDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.ShipTermsDetail.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)

# PX.Objects.CS.State (EntityType)

Label: "State"
Key: CountryID, StateID
Entity sets: PX_Objects_CS_State, State
Non-filterable, non-selectable: NoteText

PX.Objects.CS.State.CountryID : Edm.String [key] "Country"
PX.Objects.CS.State.StateID : Edm.String [key] "State ID"
PX.Objects.CS.State.Name : Edm.String "State Name"
PX.Objects.CS.State.StateRegexp : Edm.String "Validation Regexp"
PX.Objects.CS.State.Is1099State : Edm.Boolean [required]
PX.Objects.CS.State.IsTaxRegistrationRequired : Edm.Boolean [required] "Tax Registration Required"
PX.Objects.CS.State.TaxRegistrationMask : Edm.String "Tax Registration Mask"
PX.Objects.CS.State.TaxRegistrationRegexp : Edm.String "Tax Registration Reg. Exp."
PX.Objects.CS.State.NonTaxable : Edm.Boolean [required] "Non-Taxable"
PX.Objects.CS.State.NoteID : Edm.Guid
PX.Objects.CS.State.NoteText : Edm.String "Note Text"
PX.Objects.CS.State.tstamp : Edm.Binary
PX.Objects.CS.State.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.State.CreatedByScreenID : Edm.String
PX.Objects.CS.State.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.State.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.State.LastModifiedByScreenID : Edm.String
PX.Objects.CS.State.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.State.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.State.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.State.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.CS.State.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CS.State.SalesTerritoryByCountryID -> PX.Objects.CS.SalesTerritory (CountryID=CountryID)
PX.Objects.CS.State.FSAppointmentInRouteCollection -> Collection(PX.Objects.FS.FSAppointmentInRoute)
PX.Objects.CS.State.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)
PX.Objects.CS.State.POAddressCollection -> Collection(PX.Objects.PO.POAddress)
PX.Objects.CS.State.PMAddressCollection -> Collection(PX.Objects.PM.PMAddress)
PX.Objects.CS.State.AddressCollection -> Collection(PX.Objects.CR.Address)
PX.Objects.CS.State.CRAddressCollection -> Collection(PX.Objects.CR.CRAddress)
PX.Objects.CS.State.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.Objects.CS.State.FSAddressCollection -> Collection(PX.Objects.FS.FSAddress)
PX.Objects.CS.State.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.CS.State.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.CS.State.TaxZoneAddressMappingCollection -> Collection(PX.Objects.TX.TaxZoneAddressMapping)
PX.Objects.CS.State.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.CS.State.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.CS.State.ShippingZoneLineCollection -> Collection(PX.Objects.CS.ShippingZoneLine)
PX.Objects.CS.State.APAddressCollection -> Collection(PX.Objects.AP.APAddress)
PX.Objects.CS.State.SETerritoriesMappingCollection -> Collection(PX.ExternalCarriersHelper.SETerritoriesMapping)
PX.Objects.CS.State.AMVendorShipmentAddressCollection -> Collection(PX.Objects.AM.AMVendorShipmentAddress)
PX.Objects.CS.State.PRCompanyTaxAttributeCollection -> Collection(PX.Objects.PR.PRCompanyTaxAttribute)
PX.Objects.CS.State.PREmployeeAttributeCollection -> Collection(PX.Objects.PR.PREmployeeAttribute)
PX.Objects.CS.State.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.Objects.CS.State.SVAddressCollection -> Collection(PX.Objects.SV.SVAddress)

# PX.Objects.CS.Terms (EntityType)

Label: "Terms"
Key: TermsID
Entity sets: PX_Objects_CS_Terms, Terms
Non-filterable, non-selectable: NoteText

PX.Objects.CS.Terms.TermsID : Edm.String [key] "Terms ID"
PX.Objects.CS.Terms.Descr : Edm.String "Description"
PX.Objects.CS.Terms.VisibleTo : Edm.String "Visible To"
PX.Objects.CS.Terms.DueType : Edm.String "Due Date Type"
PX.Objects.CS.Terms.DayDue00 : Edm.Int16 [required] "Due Day 1"
PX.Objects.CS.Terms.DayFrom00 : Edm.Int16 [required] "Day From 1"
PX.Objects.CS.Terms.DayTo00 : Edm.Int16 [required] "Day To 1"
PX.Objects.CS.Terms.DayDue01 : Edm.Int16 [required] "Due Day 2"
PX.Objects.CS.Terms.DayFrom01 : Edm.Int16 [required] "Day From 2"
PX.Objects.CS.Terms.DayTo01 : Edm.Int16 [required] "Day To 2"
PX.Objects.CS.Terms.DiscType : Edm.String "Discount Type"
PX.Objects.CS.Terms.DayDisc : Edm.Int16 [required] "Discount Day"
PX.Objects.CS.Terms.DiscPercent : Edm.Decimal "Discount %"
PX.Objects.CS.Terms.InstallmentType : Edm.String "Installment Type"
PX.Objects.CS.Terms.InstallmentCntr : Edm.Int16 [required] "Number of Installments"
PX.Objects.CS.Terms.InstallmentFreq : Edm.String "Installment Frequency"
PX.Objects.CS.Terms.InstallmentMthd : Edm.String "Installment Method"
PX.Objects.CS.Terms.NoteID : Edm.Guid
PX.Objects.CS.Terms.NoteText : Edm.String "Note Text"
PX.Objects.CS.Terms.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.Terms.CreatedByScreenID : Edm.String
PX.Objects.CS.Terms.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Terms.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.Terms.LastModifiedByScreenID : Edm.String
PX.Objects.CS.Terms.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.Terms.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.Terms.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.Terms.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CS.Terms.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CS.Terms.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CS.Terms.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CS.Terms.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CS.Terms.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.CS.Terms.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.CS.Terms.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CS.Terms.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CS.Terms.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CS.Terms.PendingPPDARTaxAdjAppCollection -> Collection(PX.Objects.AR.PendingPPDARTaxAdjApp)
PX.Objects.CS.Terms.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CS.Terms.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CS.Terms.AppointmentToPostCollection -> Collection(PX.Objects.FS.AppointmentToPost)
PX.Objects.CS.Terms.ServiceOrderToPostCollection -> Collection(PX.Objects.FS.ServiceOrderToPost)
PX.Objects.CS.Terms.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CS.Terms.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CS.Terms.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.CS.Terms.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CS.Terms.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CS.Terms.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CS.Terms.TermsInstallmentsCollection -> Collection(PX.Objects.CS.TermsInstallments)
PX.Objects.CS.Terms.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CS.Terms.ARFinChargeCollection -> Collection(PX.Objects.AR.ARFinCharge)
PX.Objects.CS.Terms.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.CS.Terms.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CS.Terms.FSSetupCollection -> Collection(PX.Objects.SV.FSSetup)
PX.Objects.CS.Terms.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.CS.Terms.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CS.Terms.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CS.Terms.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CS.Terms.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CS.Terms.BCPaymentTermsMappingCollection -> Collection(PX.Commerce.Objects.BCPaymentTermsMapping)

# PX.Objects.CS.TermsInstallments (EntityType)

Label: "Terms Installments Detail"
Key: InstallmentNbr, TermsID
Entity sets: PX_Objects_CS_TermsInstallments, TermsInstallmentsDetail, TermsInstallments

PX.Objects.CS.TermsInstallments.TermsID : Edm.String [key] "TermsID"
PX.Objects.CS.TermsInstallments.InstallmentNbr : Edm.Int16 [key] "Inst.#"
PX.Objects.CS.TermsInstallments.InstDays : Edm.Int16 [required] "Days"
PX.Objects.CS.TermsInstallments.InstPercent : Edm.Decimal "Percent"
PX.Objects.CS.TermsInstallments.CreatedByID : Edm.Guid "Created By"
PX.Objects.CS.TermsInstallments.CreatedByScreenID : Edm.String
PX.Objects.CS.TermsInstallments.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CS.TermsInstallments.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CS.TermsInstallments.LastModifiedByScreenID : Edm.String
PX.Objects.CS.TermsInstallments.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CS.TermsInstallments.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CS.TermsInstallments.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CS.TermsInstallments.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)

# PX.Objects.CT.Contract (EntityType)

Label: "Contract"
Key: BaseType, ContractCD
Entity sets: PX_Objects_CT_Contract, Contract
Non-filterable, non-selectable: ContractInfo, Balance, StrIsTemplate, WorkgroupID, PendingSetup, PendingRecurring, PendingRenewal, TotalPending, CurrentSetup, CurrentRecurring, CurrentRenewal, TotalsCalculated, TotalRecurring, TotalUsage, TotalDue, NoteText, DaysBeforeExpiration, Days, Min, ClassID, Secured, DeletedDatabaseRecord

PX.Objects.CT.Contract.ContractID : Edm.Int32 "Contract ID"
PX.Objects.CT.Contract.BaseType : Edm.String [key required] "Entity Type"
PX.Objects.CT.Contract.ContractCD : Edm.String [key] "Contract ID"
PX.Objects.CT.Contract.TemplateID : Edm.Int32 "Contract Template"
PX.Objects.CT.Contract.Description : Edm.String "Description"
PX.Objects.CT.Contract.ContractInfo : Edm.String "ContractInfo"
PX.Objects.CT.Contract.OriginalContractID : Edm.Int32 "Contract"
PX.Objects.CT.Contract.MasterContractID : Edm.Int32 "Master Contract"
PX.Objects.CT.Contract.CaseItemID : Edm.Int32 "Case Count Item"
PX.Objects.CT.Contract.Type : Edm.String "Contract Type"
PX.Objects.CT.Contract.ClassType : Edm.String
PX.Objects.CT.Contract.CustomerID : Edm.Int32 "Customer"
PX.Objects.CT.Contract.RateTableID : Edm.String
PX.Objects.CT.Contract.Balance : Edm.Decimal "Balance"
PX.Objects.CT.Contract.Status : Edm.String "Status"
PX.Objects.CT.Contract.Duration : Edm.Int32 "Duration"
PX.Objects.CT.Contract.DurationType : Edm.String "Duration Unit"
PX.Objects.CT.Contract.StartDate : Edm.DateTimeOffset "Setup Date"
PX.Objects.CT.Contract.ActivationDate : Edm.DateTimeOffset "Activation Date"
PX.Objects.CT.Contract.RenewalBillingStartDate : Edm.DateTimeOffset
PX.Objects.CT.Contract.ExpireDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.CT.Contract.TerminationDate : Edm.DateTimeOffset "Termination Date"
PX.Objects.CT.Contract.GracePeriod : Edm.Int32 [required] "Grace Period"
PX.Objects.CT.Contract.GraceDate : Edm.DateTimeOffset
PX.Objects.CT.Contract.AutoRenew : Edm.Boolean [required] "Mass Renewal"
PX.Objects.CT.Contract.AutoRenewDays : Edm.Int32 [required] "Renewal Point"
PX.Objects.CT.Contract.IsTemplate : Edm.Boolean
PX.Objects.CT.Contract.StrIsTemplate : Edm.String "Type"
PX.Objects.CT.Contract.CuryID : Edm.String "Currency"
PX.Objects.CT.Contract.RateTypeID : Edm.String "Rate Type"
PX.Objects.CT.Contract.AllowOverrideCury : Edm.Boolean [required] "Enable Currency Override"
PX.Objects.CT.Contract.AllowOverrideRate : Edm.Boolean [required] "Enable Rate Override"
PX.Objects.CT.Contract.CalendarID : Edm.String "Calendar"
PX.Objects.CT.Contract.CreateProforma : Edm.Boolean [required] "Create Pro Forma Invoice on Billing"
PX.Objects.CT.Contract.AutomaticReleaseAR : Edm.Boolean [required] "Automatically Release AR Documents"
PX.Objects.CT.Contract.Refundable : Edm.Boolean "Refundable"
PX.Objects.CT.Contract.RefundPeriod : Edm.Int32 "Refund Period"
PX.Objects.CT.Contract.EffectiveFrom : Edm.DateTimeOffset "Effective From"
PX.Objects.CT.Contract.DiscontinueAfter : Edm.DateTimeOffset "Discontinue After"
PX.Objects.CT.Contract.DiscountID : Edm.String "Promo Code"
PX.Objects.CT.Contract.DetailedBilling : Edm.Int32 [required] "Billing Format"
PX.Objects.CT.Contract.AllowOverride : Edm.Boolean [required] "Enable Template Item Override"
PX.Objects.CT.Contract.RefreshOnRenewal : Edm.Boolean "Refresh Items from Template on Renewal"
PX.Objects.CT.Contract.IsContinuous : Edm.Boolean [required] "Shift Expire Date on Renew"
PX.Objects.CT.Contract.DefaultBranchID : Edm.Int32 "Branch"
PX.Objects.CT.Contract.QuoteNbr : Edm.String "Quote Ref. Nbr."
PX.Objects.CT.Contract.RestrictToEmployeeList : Edm.Boolean [required] "Restrict Employees"
PX.Objects.CT.Contract.RestrictToResourceList : Edm.Boolean [required] "Restrict Equipment"
PX.Objects.CT.Contract.ApproverID : Edm.Int32 "Project Manager"
PX.Objects.CT.Contract.WorkgroupID : Edm.Int32
PX.Objects.CT.Contract.OwnerID : Edm.Int32 "Owner"
PX.Objects.CT.Contract.SalesPersonID : Edm.Int32 "Sales Person"
PX.Objects.CT.Contract.ScheduleStartsOn : Edm.String "Billing Schedule Starts On"
PX.Objects.CT.Contract.AccountingMode : Edm.String
PX.Objects.CT.Contract.LimitsEnabled : Edm.Boolean [required] "Use T&M Revenue Budget Limits"
PX.Objects.CT.Contract.LockCommitments : Edm.Boolean [required]
PX.Objects.CT.Contract.BudgetMetricsEnabled : Edm.Boolean [required] "Track Production Data"
PX.Objects.CT.Contract.BillingID : Edm.String
PX.Objects.CT.Contract.AllocationID : Edm.String
PX.Objects.CT.Contract.ContractAccountGroup : Edm.Int32 "Account Group"
PX.Objects.CT.Contract.TermsID : Edm.String "Terms"
PX.Objects.CT.Contract.RetainagePct : Edm.Decimal [required]
PX.Objects.CT.Contract.PendingSetup : Edm.Decimal "Pending Setup"
PX.Objects.CT.Contract.PendingRecurring : Edm.Decimal "Pending Recurring"
PX.Objects.CT.Contract.PendingRenewal : Edm.Decimal "Pending Renewal"
PX.Objects.CT.Contract.TotalPending : Edm.Decimal "Total Pending"
PX.Objects.CT.Contract.CurrentSetup : Edm.Decimal "Current Setup"
PX.Objects.CT.Contract.CurrentRecurring : Edm.Decimal "Current Recurring"
PX.Objects.CT.Contract.CurrentRenewal : Edm.Decimal "Current Renewal"
PX.Objects.CT.Contract.TotalsCalculated : Edm.Int32
PX.Objects.CT.Contract.TotalRecurring : Edm.Decimal "Recurring Total"
PX.Objects.CT.Contract.TotalUsage : Edm.Decimal "Extra Usage Total"
PX.Objects.CT.Contract.TotalDue : Edm.Decimal "Total Due"
PX.Objects.CT.Contract.Hold : Edm.Boolean [required] "Hold"
PX.Objects.CT.Contract.Approved : Edm.Boolean [required] "Approved"
PX.Objects.CT.Contract.Rejected : Edm.Boolean [required] "Reject"
PX.Objects.CT.Contract.IsActive : Edm.Boolean [required]
PX.Objects.CT.Contract.IsCompleted : Edm.Boolean [required]
PX.Objects.CT.Contract.IsCancelled : Edm.Boolean [required]
PX.Objects.CT.Contract.IsPendingUpdate : Edm.Boolean [required]
PX.Objects.CT.Contract.AutoAllocate : Edm.Boolean [required]
PX.Objects.CT.Contract.IsLastActionUndoable : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInGL : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInAP : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInAR : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInSO : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInPO : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInTA : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInEA : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInIN : Edm.Boolean [required]
PX.Objects.CT.Contract.VisibleInCA : Edm.Boolean [required] "CA"
PX.Objects.CT.Contract.VisibleInCR : Edm.Boolean [required] "CRM"
PX.Objects.CT.Contract.NonProject : Edm.Boolean [required]
PX.Objects.CT.Contract.RevID : Edm.Int32 [required]
PX.Objects.CT.Contract.LastActiveRevID : Edm.Int32
PX.Objects.CT.Contract.LineCtr : Edm.Int32
PX.Objects.CT.Contract.BillingLineCntr : Edm.Int32 [required]
PX.Objects.CT.Contract.NoteID : Edm.Guid
PX.Objects.CT.Contract.NoteText : Edm.String "Note Text"
PX.Objects.CT.Contract.tstamp : Edm.Binary
PX.Objects.CT.Contract.CreatedByID : Edm.Guid "Created By"
PX.Objects.CT.Contract.CreatedByScreenID : Edm.String
PX.Objects.CT.Contract.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CT.Contract.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CT.Contract.LastModifiedByScreenID : Edm.String
PX.Objects.CT.Contract.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CT.Contract.DaysBeforeExpiration : Edm.String "DaysBeforeExpiration"
PX.Objects.CT.Contract.Days : Edm.String "Days"
PX.Objects.CT.Contract.Min : Edm.String "Min"
PX.Objects.CT.Contract.ServiceActivate : Edm.Boolean
PX.Objects.CT.Contract.ClassID : Edm.String
PX.Objects.CT.Contract.DefaultShipDestType : Edm.String
PX.Objects.CT.Contract.DropshipExpenseAccountSource : Edm.String
PX.Objects.CT.Contract.DropshipReceiptProcessing : Edm.String
PX.Objects.CT.Contract.DropshipExpenseRecording : Edm.String
PX.Objects.CT.Contract.CostTaxZoneID : Edm.String
PX.Objects.CT.Contract.RevenueTaxZoneID : Edm.String
PX.Objects.CT.Contract.Secured : Edm.Boolean "Secured"
PX.Objects.CT.Contract.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CT.Contract.EPEmployeeByApproverID -> PX.Objects.EP.EPEmployee (ApproverID=BAccountID)
PX.Objects.CT.Contract.VendorByApproverID -> PX.Objects.AP.Vendor (ApproverID=BAccountID)
PX.Objects.CT.Contract.ContractByTemplateID -> PX.Objects.CT.Contract (TemplateID=ContractID)
PX.Objects.CT.Contract.ContractByOriginalContractID -> PX.Objects.CT.Contract (OriginalContractID=ContractID)
PX.Objects.CT.Contract.ContractByMasterContractID -> PX.Objects.CT.Contract (MasterContractID=ContractID)
PX.Objects.CT.Contract.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.CT.Contract.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.CT.Contract.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CT.Contract.InventoryItemByCaseItemID -> PX.Objects.IN.InventoryItem (CaseItemID=InventoryID)
PX.Objects.CT.Contract.PMAccountGroupByContractAccountGroup -> PX.Objects.PM.PMAccountGroup (ContractAccountGroup=GroupID)
PX.Objects.CT.Contract.BranchByDefaultBranchID -> PX.Objects.GL.Branch (DefaultBranchID=BranchID)
PX.Objects.CT.Contract.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CT.Contract.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CT.Contract.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.CT.Contract.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CT.Contract.CurrencyRateTypeByRateTypeID -> PX.Objects.CM.CurrencyRateType (RateTypeID=CuryRateTypeID)
PX.Objects.CT.Contract.AccountByDefaultAccrualAccountID -> PX.Objects.GL.Account
PX.Objects.CT.Contract.AccountByDefaultSalesAccountID -> PX.Objects.GL.Account
PX.Objects.CT.Contract.AccountByDefaultExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.CT.Contract.AccountByDefaultOverbillingAccountID -> PX.Objects.GL.Account
PX.Objects.CT.Contract.AccountByDefaultUnderbillingAccountID -> PX.Objects.GL.Account
PX.Objects.CT.Contract.SubByDefaultAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.CT.Contract.SubByDefaultSalesSubID -> PX.Objects.GL.Sub
PX.Objects.CT.Contract.SubByDefaultExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.CT.Contract.SubByDefaultOverbillingSubID -> PX.Objects.GL.Sub
PX.Objects.CT.Contract.SubByDefaultUnderbillingSubID -> PX.Objects.GL.Sub
PX.Objects.CT.Contract.LocationByLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.CT.Contract.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.CT.Contract.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.CT.Contract.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.CT.Contract.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.CT.Contract.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CT.Contract.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.CT.Contract.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.CT.Contract.ContractSLAMappingCollection -> Collection(PX.Objects.CT.ContractSLAMapping)
PX.Objects.CT.Contract.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CT.Contract.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.CT.Contract.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.CT.Contract.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.CT.Contract.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.CT.Contract.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.CT.Contract.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CT.Contract.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CT.Contract.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.CT.Contract.ContractBillingTraceCollection -> Collection(PX.Objects.CT.ContractBillingTrace)
PX.Objects.CT.Contract.ContractRenewalHistoryCollection -> Collection(PX.Objects.CT.ContractRenewalHistory)
PX.Objects.CT.Contract.EPEmployeeContractCollection -> Collection(PX.Objects.EP.EPEmployeeContract)
PX.Objects.CT.Contract.ContractRevisionByPeriodCollection -> Collection(PX.Objects.CT.ContractRevisionByPeriod)
PX.Objects.CT.Contract.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)

# PX.Objects.CT.ContractBillingSchedule (EntityType)

Label: "Contract Billing Schedule"
Key: ContractID
Entity sets: PX_Objects_CT_ContractBillingSchedule, ContractBillingSchedule

PX.Objects.CT.ContractBillingSchedule.ContractID : Edm.Int32 [key]
PX.Objects.CT.ContractBillingSchedule.Type : Edm.String "Billing Period"
PX.Objects.CT.ContractBillingSchedule.NextDate : Edm.DateTimeOffset "Next Billing Date"
PX.Objects.CT.ContractBillingSchedule.LastDate : Edm.DateTimeOffset "Last Billing Date"
PX.Objects.CT.ContractBillingSchedule.BillTo : Edm.String "Bill To"
PX.Objects.CT.ContractBillingSchedule.StartBilling : Edm.DateTimeOffset "Billing Schedule Starts On"
PX.Objects.CT.ContractBillingSchedule.AccountID : Edm.Int32 "Account"
PX.Objects.CT.ContractBillingSchedule.InvoiceFormula : Edm.String "Invoice Description"
PX.Objects.CT.ContractBillingSchedule.TranFormula : Edm.String "Line Description"
PX.Objects.CT.ContractBillingSchedule.tstamp : Edm.Binary
PX.Objects.CT.ContractBillingSchedule.CreatedByID : Edm.Guid "Created By"
PX.Objects.CT.ContractBillingSchedule.CreatedByScreenID : Edm.String
PX.Objects.CT.ContractBillingSchedule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractBillingSchedule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CT.ContractBillingSchedule.LastModifiedByScreenID : Edm.String
PX.Objects.CT.ContractBillingSchedule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractBillingSchedule.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CT.ContractBillingSchedule.BAccountByAccountID -> PX.Objects.CR.BAccount (AccountID=BAccountID)
PX.Objects.CT.ContractBillingSchedule.CustomerByAccountID -> PX.Objects.AR.Customer (AccountID=BAccountID)
PX.Objects.CT.ContractBillingSchedule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CT.ContractBillingSchedule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CT.ContractBillingSchedule.LocationByLocationID -> PX.Objects.CR.Location (AccountID=BAccountID)
PX.Objects.CT.ContractBillingSchedule.LocationByAccountID -> PX.Objects.CR.Location (AccountID=BAccountID)
PX.Objects.CT.ContractBillingSchedule.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)

# PX.Objects.CT.ContractBillingTrace (EntityType)

Label: "Contract Billing Trace"
Key: ContractID, DocType, RecordID, RefNbr
Entity sets: PX_Objects_CT_ContractBillingTrace, ContractBillingTrace

PX.Objects.CT.ContractBillingTrace.ContractID : Edm.Int32 [key]
PX.Objects.CT.ContractBillingTrace.RecordID : Edm.Int32 [key]
PX.Objects.CT.ContractBillingTrace.DocType : Edm.String [key]
PX.Objects.CT.ContractBillingTrace.RefNbr : Edm.String [key]
PX.Objects.CT.ContractBillingTrace.NextDate : Edm.DateTimeOffset
PX.Objects.CT.ContractBillingTrace.LastDate : Edm.DateTimeOffset
PX.Objects.CT.ContractBillingTrace.tstamp : Edm.Binary
PX.Objects.CT.ContractBillingTrace.CreatedByID : Edm.Guid "Created By"
PX.Objects.CT.ContractBillingTrace.CreatedByScreenID : Edm.String
PX.Objects.CT.ContractBillingTrace.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractBillingTrace.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CT.ContractBillingTrace.LastModifiedByScreenID : Edm.String
PX.Objects.CT.ContractBillingTrace.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractBillingTrace.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CT.ContractBillingTrace.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CT.ContractBillingTrace.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CT.ContractDetail (EntityType)

Label: "Contract Detail"
Key: ContractID, LineNbr
Entity sets: PX_Objects_CT_ContractDetail, ContractDetail
Non-filterable, non-selectable: Change, Deposit, RecurringIncluded, RecurringUsed, RecurringUsedTotal, BaseDiscountAmt, RecurringDiscountAmt, RenewalDiscountAmt, BasePriceVal, BasePriceEditable, RenewalPriceVal, RenewalPriceEditable, FixedRecurringPriceVal, FixedRecurringPriceEditable, UsagePriceVal, UsagePriceEditable, NoteText, WarningAmountForDeposit

PX.Objects.CT.ContractDetail.ContractDetailID : Edm.Int32
PX.Objects.CT.ContractDetail.ContractID : Edm.Int32 [key]
PX.Objects.CT.ContractDetail.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CT.ContractDetail.RevID : Edm.Int32
PX.Objects.CT.ContractDetail.InventoryID : Edm.Int32 "Non-Stock Item"
PX.Objects.CT.ContractDetail.ContractItemID : Edm.Int32 "Item Code"
PX.Objects.CT.ContractDetail.Description : Edm.String "Description"
PX.Objects.CT.ContractDetail.ResetUsage : Edm.String "Reset Usage"
PX.Objects.CT.ContractDetail.Included : Edm.Decimal [required] "Included"
PX.Objects.CT.ContractDetail.Used : Edm.Decimal "Used"
PX.Objects.CT.ContractDetail.UsedTotal : Edm.Decimal "Used Total"
PX.Objects.CT.ContractDetail.UOM : Edm.String "UOM"
PX.Objects.CT.ContractDetail.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.CT.ContractDetail.LastQty : Edm.Decimal
PX.Objects.CT.ContractDetail.Change : Edm.Decimal "Difference"
PX.Objects.CT.ContractDetail.Deposit : Edm.Boolean
PX.Objects.CT.ContractDetail.DepositAmt : Edm.Decimal [required] "Deposit Amount"
PX.Objects.CT.ContractDetail.DepositUsed : Edm.Decimal [required] "Deposit Used"
PX.Objects.CT.ContractDetail.DepositUsedTotal : Edm.Decimal [required] "Deposit Used Total"
PX.Objects.CT.ContractDetail.RecurringIncluded : Edm.Decimal "Included"
PX.Objects.CT.ContractDetail.RecurringUsed : Edm.Decimal "Unbilled"
PX.Objects.CT.ContractDetail.RecurringUsedTotal : Edm.Decimal "Used Total"
PX.Objects.CT.ContractDetail.LastBilledDate : Edm.DateTimeOffset "Last Billed Date"
PX.Objects.CT.ContractDetail.LastBilledQty : Edm.Decimal [required] "Last Billed Qty."
PX.Objects.CT.ContractDetail.BaseDiscountID : Edm.String
PX.Objects.CT.ContractDetail.BaseDiscountSeq : Edm.String
PX.Objects.CT.ContractDetail.RecurringDiscountID : Edm.String
PX.Objects.CT.ContractDetail.RecurringDiscountSeq : Edm.String
PX.Objects.CT.ContractDetail.RenewalDiscountID : Edm.String
PX.Objects.CT.ContractDetail.RenewalDiscountSeq : Edm.String
PX.Objects.CT.ContractDetail.BaseDiscountPct : Edm.Decimal [required] "Setup Discount,%"
PX.Objects.CT.ContractDetail.RecurringDiscountPct : Edm.Decimal [required] "Recurring Discount,%"
PX.Objects.CT.ContractDetail.RenewalDiscountPct : Edm.Decimal [required] "Renewal Discount,%"
PX.Objects.CT.ContractDetail.LastBaseDiscountPct : Edm.Decimal
PX.Objects.CT.ContractDetail.LastRecurringDiscountPct : Edm.Decimal
PX.Objects.CT.ContractDetail.LastRenewalDiscountPct : Edm.Decimal
PX.Objects.CT.ContractDetail.BaseDiscountAmt : Edm.Decimal "Setup Discount"
PX.Objects.CT.ContractDetail.RecurringDiscountAmt : Edm.Decimal "Recurring Discount"
PX.Objects.CT.ContractDetail.RenewalDiscountAmt : Edm.Decimal "Renewal Discount"
PX.Objects.CT.ContractDetail.BasePrice : Edm.Decimal "Price/Percent"
PX.Objects.CT.ContractDetail.BasePriceOption : Edm.String "Setup Pricing"
PX.Objects.CT.ContractDetail.RenewalPrice : Edm.Decimal "Price/Percent"
PX.Objects.CT.ContractDetail.RenewalPriceOption : Edm.String "Renewal Pricing"
PX.Objects.CT.ContractDetail.FixedRecurringPrice : Edm.Decimal "Price/Percent"
PX.Objects.CT.ContractDetail.FixedRecurringPriceOption : Edm.String "Fixed Recurring"
PX.Objects.CT.ContractDetail.UsagePrice : Edm.Decimal "Price/Percent"
PX.Objects.CT.ContractDetail.UsagePriceOption : Edm.String "Usage Price"
PX.Objects.CT.ContractDetail.BasePriceVal : Edm.Decimal "Setup Price"
PX.Objects.CT.ContractDetail.BasePriceEditable : Edm.Boolean
PX.Objects.CT.ContractDetail.IsBaseValid : Edm.Boolean
PX.Objects.CT.ContractDetail.RenewalPriceVal : Edm.Decimal "Renewal Price"
PX.Objects.CT.ContractDetail.RenewalPriceEditable : Edm.Boolean
PX.Objects.CT.ContractDetail.IsRenewalValid : Edm.Boolean
PX.Objects.CT.ContractDetail.FixedRecurringPriceVal : Edm.Decimal "Recurring Price"
PX.Objects.CT.ContractDetail.FixedRecurringPriceEditable : Edm.Boolean
PX.Objects.CT.ContractDetail.IsFixedRecurringValid : Edm.Boolean
PX.Objects.CT.ContractDetail.UsagePriceVal : Edm.Decimal "Extra Usage Price"
PX.Objects.CT.ContractDetail.UsagePriceEditable : Edm.Boolean
PX.Objects.CT.ContractDetail.IsUsageValid : Edm.Boolean
PX.Objects.CT.ContractDetail.NoteID : Edm.Guid
PX.Objects.CT.ContractDetail.NoteText : Edm.String "Note Text"
PX.Objects.CT.ContractDetail.WarningAmountForDeposit : Edm.Boolean
PX.Objects.CT.ContractDetail.tstamp : Edm.Binary
PX.Objects.CT.ContractDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CT.ContractDetail.CreatedByScreenID : Edm.String
PX.Objects.CT.ContractDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CT.ContractDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CT.ContractDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractDetail.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CT.ContractDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.CT.ContractDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CT.ContractDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CT.ContractDetail.ContractBillingScheduleByContractID -> PX.Objects.CT.ContractBillingSchedule (ContractID=ContractID)
PX.Objects.CT.ContractDetail.ContractItemByContractItemID -> PX.Objects.CT.ContractItem (ContractItemID=ContractItemID)
PX.Objects.CT.ContractDetail.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)

# PX.Objects.CT.ContractDetailAcum (EntityType)

Label: "Contract Detail"
BaseType: PX.Objects.CT.ContractDetail
Key: ContractID, LineNbr (inherited from PX.Objects.CT.ContractDetail)
Entity sets: PX_Objects_CT_ContractDetailAcum

# PX.Objects.CT.ContractItem (EntityType)

Label: "Contract Item"
Key: ContractItemCD
Entity sets: PX_Objects_CT_ContractItem, ContractItem
Non-filterable, non-selectable: RecurringTypeForDeposits, UOMForDeposits, BaseItemCurySettingsID, BasePriceVal, RenewalItemCurySettingsID, RenewalPriceVal, RecurringItemCurySettingsID, FixedRecurringPriceVal, UsagePriceVal, NoteText

PX.Objects.CT.ContractItem.ContractItemID : Edm.Int32 "ContractItemID"
PX.Objects.CT.ContractItem.ContractItemCD : Edm.String [key] "Contract Item"
PX.Objects.CT.ContractItem.Descr : Edm.String "Description"
PX.Objects.CT.ContractItem.DefaultQty : Edm.Decimal [required] "Default Quantity"
PX.Objects.CT.ContractItem.MinQty : Edm.Decimal [required] "Minimum Allowed Quantity"
PX.Objects.CT.ContractItem.MaxQty : Edm.Decimal [required] "Maximum Allowed Quantity"
PX.Objects.CT.ContractItem.CuryID : Edm.String "Currency ID"
PX.Objects.CT.ContractItem.BaseItemID : Edm.Int32 "Setup Item"
PX.Objects.CT.ContractItem.BasePriceOption : Edm.String "Setup Pricing"
PX.Objects.CT.ContractItem.BasePrice : Edm.Decimal "Item Price/Percent"
PX.Objects.CT.ContractItem.ProrateSetup : Edm.Boolean [required] "Prorate Setup"
PX.Objects.CT.ContractItem.RetainRate : Edm.Decimal [required] "Retain Rate"
PX.Objects.CT.ContractItem.Refundable : Edm.Boolean [required] "Refundable"
PX.Objects.CT.ContractItem.Deposit : Edm.Boolean [required] "Deposit"
PX.Objects.CT.ContractItem.CollectRenewFeeOnActivation : Edm.Boolean [required] "Collect Renewal Fee on Activation"
PX.Objects.CT.ContractItem.RenewalItemID : Edm.Int32 "Renewal Item"
PX.Objects.CT.ContractItem.RenewalPriceOption : Edm.String "Renewal Pricing"
PX.Objects.CT.ContractItem.RenewalPrice : Edm.Decimal "Item Price/Percent"
PX.Objects.CT.ContractItem.RecurringType : Edm.String "Billing Type"
PX.Objects.CT.ContractItem.RecurringTypeForDeposits : Edm.String "Billing Type"
PX.Objects.CT.ContractItem.UOMForDeposits : Edm.String "UOM"
PX.Objects.CT.ContractItem.RecurringItemID : Edm.Int32 "Recurring Item"
PX.Objects.CT.ContractItem.ResetUsageOnBilling : Edm.Boolean [required] "Reset Usage on Billing"
PX.Objects.CT.ContractItem.FixedRecurringPriceOption : Edm.String "Recurring Pricing"
PX.Objects.CT.ContractItem.FixedRecurringPrice : Edm.Decimal "Item Price/Percent"
PX.Objects.CT.ContractItem.UsagePriceOption : Edm.String "Extra Usage Pricing"
PX.Objects.CT.ContractItem.UsagePrice : Edm.Decimal "Item Price/Percent"
PX.Objects.CT.ContractItem.DiscontinueAfter : Edm.DateTimeOffset "Discontinue After"
PX.Objects.CT.ContractItem.ReplacementItemID : Edm.Int32 "Replacement Item"
PX.Objects.CT.ContractItem.DepositItemID : Edm.Int32 "Deposit Item"
PX.Objects.CT.ContractItem.BaseItemCurySettingsID : Edm.Int32
PX.Objects.CT.ContractItem.BasePriceVal : Edm.Decimal "Setup Price"
PX.Objects.CT.ContractItem.RenewalItemCurySettingsID : Edm.Int32
PX.Objects.CT.ContractItem.RenewalPriceVal : Edm.Decimal "Renewal Price"
PX.Objects.CT.ContractItem.RecurringItemCurySettingsID : Edm.Int32
PX.Objects.CT.ContractItem.FixedRecurringPriceVal : Edm.Decimal "Recurring Price"
PX.Objects.CT.ContractItem.UsagePriceVal : Edm.Decimal "Extra Usage Price"
PX.Objects.CT.ContractItem.IsBaseValid : Edm.Boolean
PX.Objects.CT.ContractItem.IsRenewalValid : Edm.Boolean
PX.Objects.CT.ContractItem.IsFixedRecurringValid : Edm.Boolean
PX.Objects.CT.ContractItem.IsUsageValid : Edm.Boolean
PX.Objects.CT.ContractItem.NoteID : Edm.Guid
PX.Objects.CT.ContractItem.NoteText : Edm.String "Note Text"
PX.Objects.CT.ContractItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.CT.ContractItem.CreatedByScreenID : Edm.String
PX.Objects.CT.ContractItem.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CT.ContractItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CT.ContractItem.LastModifiedByScreenID : Edm.String
PX.Objects.CT.ContractItem.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CT.ContractItem.tstamp : Edm.Binary
PX.Objects.CT.ContractItem.InventoryItemByBaseItemID -> PX.Objects.IN.InventoryItem (BaseItemID=InventoryID)
PX.Objects.CT.ContractItem.InventoryItemByRenewalItemID -> PX.Objects.IN.InventoryItem (RenewalItemID=InventoryID)
PX.Objects.CT.ContractItem.InventoryItemByRecurringItemID -> PX.Objects.IN.InventoryItem (RecurringItemID=InventoryID)
PX.Objects.CT.ContractItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CT.ContractItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CT.ContractItem.ContractItemByReplacementItemID -> PX.Objects.CT.ContractItem (ReplacementItemID=ContractItemID)
PX.Objects.CT.ContractItem.ContractItemByDepositItemID -> PX.Objects.CT.ContractItem (DepositItemID=ContractItemID)
PX.Objects.CT.ContractItem.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CT.ContractItem.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.CT.ContractItem.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.CT.ContractItem.ContractDetailAcumCollection -> Collection(PX.Objects.CT.ContractDetailAcum)

# PX.Objects.CT.ContractRenewalHistory (EntityType)

Label: "Contract Renewal History"
Key: ContractID, RevID
Entity sets: PX_Objects_CT_ContractRenewalHistory, ContractRenewalHistory
Non-filterable, non-selectable: Date

PX.Objects.CT.ContractRenewalHistory.ContractID : Edm.Int32 [key]
PX.Objects.CT.ContractRenewalHistory.RevID : Edm.Int32 [key]
PX.Objects.CT.ContractRenewalHistory.RenewalDate : Edm.DateTimeOffset "Renewal Date"
PX.Objects.CT.ContractRenewalHistory.ActionBusinessDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.Status : Edm.String "Status"
PX.Objects.CT.ContractRenewalHistory.Action : Edm.String "Action"
PX.Objects.CT.ContractRenewalHistory.ChildContractID : Edm.Int32 "Related Contract"
PX.Objects.CT.ContractRenewalHistory.ExpireDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.EffectiveFrom : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.ActivationDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.StartDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.NextDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.LastDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.StartBilling : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.TerminationDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.IsActive : Edm.Boolean [required]
PX.Objects.CT.ContractRenewalHistory.IsCompleted : Edm.Boolean [required]
PX.Objects.CT.ContractRenewalHistory.IsCancelled : Edm.Boolean [required]
PX.Objects.CT.ContractRenewalHistory.IsPendingUpdate : Edm.Boolean [required]
PX.Objects.CT.ContractRenewalHistory.Date : Edm.DateTimeOffset "Date"
PX.Objects.CT.ContractRenewalHistory.DiscountID : Edm.String
PX.Objects.CT.ContractRenewalHistory.tstamp : Edm.Binary
PX.Objects.CT.ContractRenewalHistory.CreatedByID : Edm.Guid "User"
PX.Objects.CT.ContractRenewalHistory.CreatedByScreenID : Edm.String
PX.Objects.CT.ContractRenewalHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractRenewalHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CT.ContractRenewalHistory.LastModifiedByScreenID : Edm.String
PX.Objects.CT.ContractRenewalHistory.LastModifiedDateTime : Edm.DateTimeOffset "Modified Time"
PX.Objects.CT.ContractRenewalHistory.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CT.ContractRenewalHistory.ContractByChildContractID -> PX.Objects.CT.Contract (ChildContractID=ContractID)
PX.Objects.CT.ContractRenewalHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CT.ContractRenewalHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CT.ContractRenewalHistory.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)

# PX.Objects.CT.ContractRevisionByPeriod (EntityType)

Label: "Contract revision by period"
Key: ContractID, FinPeriodID
Entity sets: PX_Objects_CT_ContractRevisionByPeriod, Contractrevisionbyperiod
Non-filterable, non-selectable: NewCount

PX.Objects.CT.ContractRevisionByPeriod.FinPeriodID : Edm.String [key]
PX.Objects.CT.ContractRevisionByPeriod.ContractID : Edm.Int32 [key] "Contract ID"
PX.Objects.CT.ContractRevisionByPeriod.RevID : Edm.Int32 "Revision Number"
PX.Objects.CT.ContractRevisionByPeriod.ActivationDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRevisionByPeriod.EffectiveFrom : Edm.DateTimeOffset "Effective From"
PX.Objects.CT.ContractRevisionByPeriod.ExpireDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.CT.ContractRevisionByPeriod.TerminationDate : Edm.DateTimeOffset
PX.Objects.CT.ContractRevisionByPeriod.StartFinPeriod : Edm.DateTimeOffset "Start Date"
PX.Objects.CT.ContractRevisionByPeriod.EndFinPeriod : Edm.DateTimeOffset
PX.Objects.CT.ContractRevisionByPeriod.NewCount : Edm.Int32
PX.Objects.CT.ContractRevisionByPeriod.ExpiredCount : Edm.Int32 "Expired"
PX.Objects.CT.ContractRevisionByPeriod.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CT.ContractRevisionByPeriod.ContractByChildContractID -> PX.Objects.CT.Contract

# PX.Objects.CT.ContractSLAMapping (EntityType)

Label: "Contract SLA Mapping"
Key: ContractSLAMappingID
Entity sets: PX_Objects_CT_ContractSLAMapping, ContractSLAMapping

PX.Objects.CT.ContractSLAMapping.ContractSLAMappingID : Edm.Int32 [key] "ContractSLAMappingID"
PX.Objects.CT.ContractSLAMapping.ContractID : Edm.Int32
PX.Objects.CT.ContractSLAMapping.Severity : Edm.String "Severity"
PX.Objects.CT.ContractSLAMapping.Period : Edm.Int32 "Terms"
PX.Objects.CT.ContractSLAMapping.CreatedByID : Edm.Guid "Created By"
PX.Objects.CT.ContractSLAMapping.CreatedByScreenID : Edm.String
PX.Objects.CT.ContractSLAMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractSLAMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CT.ContractSLAMapping.LastModifiedByScreenID : Edm.String
PX.Objects.CT.ContractSLAMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CT.ContractSLAMapping.tstamp : Edm.Binary
PX.Objects.CT.ContractSLAMapping.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CT.ContractSLAMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CT.ContractSLAMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CT.ContractTemplate (EntityType)

Label: "Contract Template"
BaseType: PX.Objects.CT.Contract
Key: BaseType, ContractCD (inherited from PX.Objects.CT.Contract)
Entity sets: PX_Objects_CT_ContractTemplate, ContractTemplate
Non-filterable, non-selectable: ContractStrID

PX.Objects.CT.ContractTemplate.LocationID : Edm.Int32
PX.Objects.CT.ContractTemplate.AllowOverrideFormulaDescription : Edm.Boolean "Enable Overriding Formulas in Contracts"
PX.Objects.CT.ContractTemplate.ContractStrID : Edm.String "ContractStrID"

# PX.Objects.CT.SelContractWatcher (EntityType)

Key: ContractID, EMail
Entity sets: PX_Objects_CT_SelContractWatcher

PX.Objects.CT.SelContractWatcher.ContractID : Edm.Int32 [key] "Contract ID"
PX.Objects.CT.SelContractWatcher.ContactID : Edm.Int32 "Contact"
PX.Objects.CT.SelContractWatcher.WatchTypeID : Edm.String "Watch Type"
PX.Objects.CT.SelContractWatcher.EMail : Edm.String [key] "Email"
PX.Objects.CT.SelContractWatcher.DisplayName : Edm.String "DisplayName"
PX.Objects.CT.SelContractWatcher.FirstName : Edm.String "First Name"
PX.Objects.CT.SelContractWatcher.MidName : Edm.String "Middle Name"
PX.Objects.CT.SelContractWatcher.LastName : Edm.String "Last Name"
PX.Objects.CT.SelContractWatcher.Title : Edm.String "Title"
PX.Objects.CT.SelContractWatcher.Salutation : Edm.String "Attention"
PX.Objects.CT.SelContractWatcher.Phone1 : Edm.String "Phone 1"
PX.Objects.CT.SelContractWatcher.BAccountID : Edm.Int32 "Customer ID"
PX.Objects.CT.SelContractWatcher.ContactContactID : Edm.Int32 "ContactContactID"
PX.Objects.CT.SelContractWatcher.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CT.SelContractWatcher.BAccountByParentBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CT.SelContractWatcher.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CT.SelContractWatcher.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CT.SelContractWatcher.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.CT.SelContractWatcher.ContactExtAddressCollection -> Collection(PX.Objects.CR.ContactExtAddress)

# PX.Objects.CT.Standalone.ContractDetail (EntityType)

Key: ContractDetailID, ContractID, RevID
Entity sets: PX_Objects_CT_Standalone_ContractDetail
Non-filterable, non-selectable: BasePriceVal, FixedRecurringPriceVal

PX.Objects.CT.Standalone.ContractDetail.ContractDetailID : Edm.Int32 [key] "Contract Detail ID"
PX.Objects.CT.Standalone.ContractDetail.ContractID : Edm.Int32 [key] "Contract ID"
PX.Objects.CT.Standalone.ContractDetail.LineNbr : Edm.Int32
PX.Objects.CT.Standalone.ContractDetail.RevID : Edm.Int32 [key] "Revision Number"
PX.Objects.CT.Standalone.ContractDetail.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.CT.Standalone.ContractDetail.FixedRecurringPrice : Edm.Decimal "Price/Percent"
PX.Objects.CT.Standalone.ContractDetail.ContractItemID : Edm.Int32 "Item Code"
PX.Objects.CT.Standalone.ContractDetail.FixedRecurringPriceOption : Edm.String "Fixed Recurring"
PX.Objects.CT.Standalone.ContractDetail.BasePrice : Edm.Decimal "Price/Percent"
PX.Objects.CT.Standalone.ContractDetail.BasePriceOption : Edm.String "Setup Pricing"
PX.Objects.CT.Standalone.ContractDetail.BasePriceVal : Edm.Decimal "Setup Price"
PX.Objects.CT.Standalone.ContractDetail.HistoryStatus : Edm.String "Status"
PX.Objects.CT.Standalone.ContractDetail.HistoryNextDate : Edm.DateTimeOffset "Next Billing Date"
PX.Objects.CT.Standalone.ContractDetail.HistoryActivationDate : Edm.DateTimeOffset
PX.Objects.CT.Standalone.ContractDetail.HistoryStartDate : Edm.DateTimeOffset
PX.Objects.CT.Standalone.ContractDetail.HistoryExpireDate : Edm.DateTimeOffset
PX.Objects.CT.Standalone.ContractDetail.HistoryTerminationDate : Edm.DateTimeOffset
PX.Objects.CT.Standalone.ContractDetail.BillingScheduleNextDate : Edm.DateTimeOffset "Next Billing Date"
PX.Objects.CT.Standalone.ContractDetail.FixedRecurringPriceVal : Edm.Decimal "Recurring Price"
PX.Objects.CT.Standalone.ContractDetail.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CT.Standalone.ContractDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem
PX.Objects.CT.Standalone.ContractDetail.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CT.Standalone.ContractDetail.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CT.Standalone.ContractDetail.ContractBillingScheduleByContractID -> PX.Objects.CT.ContractBillingSchedule (ContractID=ContractID)
PX.Objects.CT.Standalone.ContractDetail.ContractItemByContractItemID -> PX.Objects.CT.ContractItem (ContractItemID=ContractItemID)
PX.Objects.CT.Standalone.ContractDetail.INUnitByInventoryID -> PX.Objects.IN.INUnit

# PX.Objects.DR.DRDeferredCode (EntityType)

Label: "Deferral Code"
Key: DeferredCodeID
Entity sets: PX_Objects_DR_DRDeferredCode, DeferralCode, DRDeferredCode
Non-filterable, non-selectable: Periods, NoteText

PX.Objects.DR.DRDeferredCode.DeferredCodeID : Edm.String [key] "Deferral Code"
PX.Objects.DR.DRDeferredCode.Description : Edm.String "Description"
PX.Objects.DR.DRDeferredCode.AccountType : Edm.String "Code Type"
PX.Objects.DR.DRDeferredCode.Active : Edm.Boolean [required] "Active"
PX.Objects.DR.DRDeferredCode.ReconNowPct : Edm.Decimal [required] "Recognize Now %"
PX.Objects.DR.DRDeferredCode.StartOffset : Edm.Int16 [required] "Start Offset"
PX.Objects.DR.DRDeferredCode.Occurrences : Edm.Int16 [required] "Occurrences"
PX.Objects.DR.DRDeferredCode.Frequency : Edm.Int16 "Every"
PX.Objects.DR.DRDeferredCode.ScheduleOption : Edm.String "Schedule Options"
PX.Objects.DR.DRDeferredCode.FixedDay : Edm.Int16 "Fixed Day of the Period"
PX.Objects.DR.DRDeferredCode.Method : Edm.String "Recognition Method"
PX.Objects.DR.DRDeferredCode.MultiDeliverableArrangement : Edm.Boolean [required] "Multiple-Deliverable Arrangement"
PX.Objects.DR.DRDeferredCode.AccountSource : Edm.String "Use Deferral Account From"
PX.Objects.DR.DRDeferredCode.CopySubFromSourceTran : Edm.Boolean [required] "Copy Sub. from Sales/Expense Sub."
PX.Objects.DR.DRDeferredCode.Periods : Edm.String "Period(s)"
PX.Objects.DR.DRDeferredCode.NoteID : Edm.Guid
PX.Objects.DR.DRDeferredCode.NoteText : Edm.String "Note Text"
PX.Objects.DR.DRDeferredCode.RecognizeInPastPeriods : Edm.Boolean [required] "Allow Recognition in Previous Periods"
PX.Objects.DR.DRDeferredCode.tstamp : Edm.Binary
PX.Objects.DR.DRDeferredCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.DR.DRDeferredCode.CreatedByScreenID : Edm.String
PX.Objects.DR.DRDeferredCode.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.DR.DRDeferredCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.DR.DRDeferredCode.LastModifiedByScreenID : Edm.String
PX.Objects.DR.DRDeferredCode.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.DR.DRDeferredCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.DR.DRDeferredCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.DR.DRDeferredCode.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.DR.DRDeferredCode.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.DR.DRDeferredCode.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.DR.DRDeferredCode.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.DR.DRDeferredCode.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.DR.DRDeferredCode.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.DR.DRDeferredCode.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.DR.DRDeferredCode.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.DR.DRDeferredCode.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.DR.DRDeferredCode.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)

# PX.Objects.DR.DRExpenseBalance (EntityType)

Label: "DR Expense Balance"
Key: AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID
Entity sets: PX_Objects_DR_DRExpenseBalance, DRExpenseBalance

PX.Objects.DR.DRExpenseBalance.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.DR.DRExpenseBalance.AcctID : Edm.Int32 [key] "Account"
PX.Objects.DR.DRExpenseBalance.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.DR.DRExpenseBalance.ComponentID : Edm.Int32 [key]
PX.Objects.DR.DRExpenseBalance.VendorID : Edm.Int32 [key]
PX.Objects.DR.DRExpenseBalance.ProjectID : Edm.Int32 [key required]
PX.Objects.DR.DRExpenseBalance.FinPeriodID : Edm.String [key] "FinPeriod"
PX.Objects.DR.DRExpenseBalance.BegBalance : Edm.Decimal [required] "Begin Balance"
PX.Objects.DR.DRExpenseBalance.BegProjected : Edm.Decimal [required] "Begin Projected"
PX.Objects.DR.DRExpenseBalance.PTDDeferred : Edm.Decimal [required] "Deferred Amount"
PX.Objects.DR.DRExpenseBalance.PTDRecognized : Edm.Decimal [required] "Recognized Amount"
PX.Objects.DR.DRExpenseBalance.PTDRecognizedSamePeriod : Edm.Decimal [required] "Recognized Amount in Same Period"
PX.Objects.DR.DRExpenseBalance.PTDProjected : Edm.Decimal [required] "Projected Amount"
PX.Objects.DR.DRExpenseBalance.EndBalance : Edm.Decimal [required] "End Balance"
PX.Objects.DR.DRExpenseBalance.EndProjected : Edm.Decimal [required] "End Projected"
PX.Objects.DR.DRExpenseBalance.TranBegBalance : Edm.Decimal [required] "Begin Balance"
PX.Objects.DR.DRExpenseBalance.TranBegProjected : Edm.Decimal [required] "Begin Projected"
PX.Objects.DR.DRExpenseBalance.TranPTDDeferred : Edm.Decimal [required] "Deferred Amount"
PX.Objects.DR.DRExpenseBalance.TranPTDRecognized : Edm.Decimal [required] "Recognized Amount"
PX.Objects.DR.DRExpenseBalance.TranPTDRecognizedSamePeriod : Edm.Decimal [required] "Recognized Amount in Same Period"
PX.Objects.DR.DRExpenseBalance.TranPTDProjected : Edm.Decimal [required] "Projected Amount"
PX.Objects.DR.DRExpenseBalance.TranEndBalance : Edm.Decimal [required] "End Balance"
PX.Objects.DR.DRExpenseBalance.TranEndProjected : Edm.Decimal [required] "End Projected"
PX.Objects.DR.DRExpenseBalance.tstamp : Edm.Binary
PX.Objects.DR.DRExpenseBalance.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.DR.DRExpenseBalance.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.DR.DRExpenseBalance.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.DR.DRExpenseBalance.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.DR.DRExpenseBalance.AccountByAcctID -> PX.Objects.GL.Account (AcctID=AccountID)
PX.Objects.DR.DRExpenseBalance.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.DR.DRExpenseBalance2 (EntityType)

Label: "DR Expense Balance"
BaseType: PX.Objects.DR.DRExpenseBalance
Key: AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID (inherited from PX.Objects.DR.DRExpenseBalance)
Entity sets: PX_Objects_DR_DRExpenseBalance2

# PX.Objects.DR.DRExpenseBalanceByPeriod (EntityType)

Label: "DR Expense Balance by Period"
Key: AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID
Entity sets: PX_Objects_DR_DRExpenseBalanceByPeriod, DRExpenseBalancebyPeriod

PX.Objects.DR.DRExpenseBalanceByPeriod.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.DR.DRExpenseBalanceByPeriod.AcctID : Edm.Int32 [key] "Account"
PX.Objects.DR.DRExpenseBalanceByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.DR.DRExpenseBalanceByPeriod.ComponentID : Edm.Int32 [key]
PX.Objects.DR.DRExpenseBalanceByPeriod.VendorID : Edm.Int32 [key]
PX.Objects.DR.DRExpenseBalanceByPeriod.ProjectID : Edm.Int32 [key]
PX.Objects.DR.DRExpenseBalanceByPeriod.LastActivityPeriod : Edm.String
PX.Objects.DR.DRExpenseBalanceByPeriod.FinPeriodID : Edm.String [key]
PX.Objects.DR.DRExpenseBalanceByPeriod.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.DR.DRExpenseBalanceByPeriod.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.DR.DRExpenseBalanceByPeriod.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.DR.DRExpenseBalanceByPeriod.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.DR.DRExpenseBalanceByPeriod.AccountByAcctID -> PX.Objects.GL.Account (AcctID=AccountID)
PX.Objects.DR.DRExpenseBalanceByPeriod.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.DR.DRExpenseProjection (EntityType)

Label: "DR Expense Projection"
Key: AcctID, BranchID, ComponentID, FinPeriodID, ProjectID, SubID, VendorID
Entity sets: PX_Objects_DR_DRExpenseProjection, DRExpenseProjection

PX.Objects.DR.DRExpenseProjection.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.DR.DRExpenseProjection.AcctID : Edm.Int32 [key] "Account"
PX.Objects.DR.DRExpenseProjection.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.DR.DRExpenseProjection.ComponentID : Edm.Int32 [key]
PX.Objects.DR.DRExpenseProjection.VendorID : Edm.Int32 [key]
PX.Objects.DR.DRExpenseProjection.ProjectID : Edm.Int32 [key]
PX.Objects.DR.DRExpenseProjection.FinPeriodID : Edm.String [key] "FinPeriod"
PX.Objects.DR.DRExpenseProjection.PTDProjected : Edm.Decimal [required] "Projected Amount"
PX.Objects.DR.DRExpenseProjection.PTDRecognized : Edm.Decimal [required] "Recognized Amount"
PX.Objects.DR.DRExpenseProjection.PTDRecognizedSamePeriod : Edm.Decimal [required] "Recognized Amount in Same Period"
PX.Objects.DR.DRExpenseProjection.TranPTDProjected : Edm.Decimal [required] "Projected Amount"
PX.Objects.DR.DRExpenseProjection.TranPTDRecognized : Edm.Decimal [required] "Recognized Amount"
PX.Objects.DR.DRExpenseProjection.TranPTDRecognizedSamePeriod : Edm.Decimal [required] "Recognized Amount in Same Period"
PX.Objects.DR.DRExpenseProjection.tstamp : Edm.Binary
PX.Objects.DR.DRExpenseProjection.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.DR.DRExpenseProjection.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.DR.DRExpenseProjection.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.DR.DRExpenseProjection.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.DR.DRExpenseProjection.AccountByAcctID -> PX.Objects.GL.Account (AcctID=AccountID)
PX.Objects.DR.DRExpenseProjection.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.DR.DRRevenueBalance (EntityType)

Label: "DR Revenue Balance"
Key: AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID
Entity sets: PX_Objects_DR_DRRevenueBalance, DRRevenueBalance

PX.Objects.DR.DRRevenueBalance.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.DR.DRRevenueBalance.AcctID : Edm.Int32 [key] "Account"
PX.Objects.DR.DRRevenueBalance.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.DR.DRRevenueBalance.ComponentID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueBalance.CustomerID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueBalance.ProjectID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueBalance.FinPeriodID : Edm.String [key] "FinPeriod"
PX.Objects.DR.DRRevenueBalance.BegBalance : Edm.Decimal [required] "Begin Balance"
PX.Objects.DR.DRRevenueBalance.BegProjected : Edm.Decimal [required] "Begin Projected"
PX.Objects.DR.DRRevenueBalance.PTDDeferred : Edm.Decimal [required] "Deferred Amount"
PX.Objects.DR.DRRevenueBalance.PTDRecognized : Edm.Decimal [required] "Recognized Amount"
PX.Objects.DR.DRRevenueBalance.PTDRecognizedSamePeriod : Edm.Decimal [required] "Recognized Amount in Same Period"
PX.Objects.DR.DRRevenueBalance.PTDProjected : Edm.Decimal [required] "Projected Amount"
PX.Objects.DR.DRRevenueBalance.EndBalance : Edm.Decimal [required] "End Balance"
PX.Objects.DR.DRRevenueBalance.EndProjected : Edm.Decimal [required] "End Projected"
PX.Objects.DR.DRRevenueBalance.TranBegBalance : Edm.Decimal [required] "Begin Balance"
PX.Objects.DR.DRRevenueBalance.TranBegProjected : Edm.Decimal [required] "Begin Projected"
PX.Objects.DR.DRRevenueBalance.TranPTDDeferred : Edm.Decimal [required] "Deferred Amount"
PX.Objects.DR.DRRevenueBalance.TranPTDRecognized : Edm.Decimal [required] "Recognized Amount"
PX.Objects.DR.DRRevenueBalance.TranPTDRecognizedSamePeriod : Edm.Decimal [required] "Recognized Amount in Same Period"
PX.Objects.DR.DRRevenueBalance.TranPTDProjected : Edm.Decimal [required] "Projected Amount"
PX.Objects.DR.DRRevenueBalance.TranEndBalance : Edm.Decimal [required] "End Balance"
PX.Objects.DR.DRRevenueBalance.TranEndProjected : Edm.Decimal [required] "End Projected"
PX.Objects.DR.DRRevenueBalance.tstamp : Edm.Binary
PX.Objects.DR.DRRevenueBalance.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.DR.DRRevenueBalance.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.DR.DRRevenueBalance.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.DR.DRRevenueBalance.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.DR.DRRevenueBalance.AccountByAcctID -> PX.Objects.GL.Account (AcctID=AccountID)
PX.Objects.DR.DRRevenueBalance.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.DR.DRRevenueBalance2 (EntityType)

Label: "DR Revenue Balance"
BaseType: PX.Objects.DR.DRRevenueBalance
Key: AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID (inherited from PX.Objects.DR.DRRevenueBalance)
Entity sets: PX_Objects_DR_DRRevenueBalance2

# PX.Objects.DR.DRRevenueBalanceByPeriod (EntityType)

Label: "DR Revenue Balance by Period"
Key: AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID
Entity sets: PX_Objects_DR_DRRevenueBalanceByPeriod, DRRevenueBalancebyPeriod

PX.Objects.DR.DRRevenueBalanceByPeriod.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.DR.DRRevenueBalanceByPeriod.AcctID : Edm.Int32 [key] "Account"
PX.Objects.DR.DRRevenueBalanceByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.DR.DRRevenueBalanceByPeriod.ComponentID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueBalanceByPeriod.CustomerID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueBalanceByPeriod.ProjectID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueBalanceByPeriod.LastActivityPeriod : Edm.String
PX.Objects.DR.DRRevenueBalanceByPeriod.FinPeriodID : Edm.String [key]
PX.Objects.DR.DRRevenueBalanceByPeriod.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.DR.DRRevenueBalanceByPeriod.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.DR.DRRevenueBalanceByPeriod.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.DR.DRRevenueBalanceByPeriod.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.DR.DRRevenueBalanceByPeriod.AccountByAcctID -> PX.Objects.GL.Account (AcctID=AccountID)
PX.Objects.DR.DRRevenueBalanceByPeriod.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.DR.DRRevenueProjection (EntityType)

Label: "DR Revenue Projection"
Key: AcctID, BranchID, ComponentID, CustomerID, FinPeriodID, ProjectID, SubID
Entity sets: PX_Objects_DR_DRRevenueProjection, DRRevenueProjection

PX.Objects.DR.DRRevenueProjection.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.DR.DRRevenueProjection.AcctID : Edm.Int32 [key] "Account"
PX.Objects.DR.DRRevenueProjection.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.DR.DRRevenueProjection.ComponentID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueProjection.CustomerID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueProjection.ProjectID : Edm.Int32 [key]
PX.Objects.DR.DRRevenueProjection.FinPeriodID : Edm.String [key] "FinPeriod"
PX.Objects.DR.DRRevenueProjection.PTDProjected : Edm.Decimal [required] "Projected Amount"
PX.Objects.DR.DRRevenueProjection.PTDRecognized : Edm.Decimal [required] "Recognized Amount"
PX.Objects.DR.DRRevenueProjection.PTDRecognizedSamePeriod : Edm.Decimal [required] "Recognized Amount in Same Period"
PX.Objects.DR.DRRevenueProjection.TranPTDProjected : Edm.Decimal [required] "Projected Amount"
PX.Objects.DR.DRRevenueProjection.TranPTDRecognized : Edm.Decimal [required] "Recognized Amount"
PX.Objects.DR.DRRevenueProjection.TranPTDRecognizedSamePeriod : Edm.Decimal [required] "Recognized Amount in Same Period"
PX.Objects.DR.DRRevenueProjection.tstamp : Edm.Binary
PX.Objects.DR.DRRevenueProjection.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.DR.DRRevenueProjection.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.DR.DRRevenueProjection.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.DR.DRRevenueProjection.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.DR.DRRevenueProjection.AccountByAcctID -> PX.Objects.GL.Account (AcctID=AccountID)
PX.Objects.DR.DRRevenueProjection.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.DR.DRSchedule (EntityType)

Label: "Deferral Schedule"
Key: ScheduleNbr
Entity sets: PX_Objects_DR_DRSchedule, DeferralSchedule, DRSchedule
Non-filterable, non-selectable: DocumentType, BAccountType, OrigLineAmt, CuryNetTranPrice, NetTranPrice, ComponentsTotal, DefTotal, DocumentTypeEx, Status, IsPoolVisible, IsRecalculated, IsSuspense, NoteText, CuryRate, CuryViewState

PX.Objects.DR.DRSchedule.ScheduleID : Edm.Int32
PX.Objects.DR.DRSchedule.ScheduleNbr : Edm.String [key] "Schedule Number"
PX.Objects.DR.DRSchedule.DocType : Edm.String "Doc. Type"
PX.Objects.DR.DRSchedule.Module : Edm.String "Module"
PX.Objects.DR.DRSchedule.RefNbr : Edm.String "Ref. Nbr."
PX.Objects.DR.DRSchedule.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.DR.DRSchedule.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.DR.DRSchedule.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.DR.DRSchedule.BAccountID : Edm.Int32 "Business Account"
PX.Objects.DR.DRSchedule.BaseCuryID : Edm.String "Currency"
PX.Objects.DR.DRSchedule.TranDesc : Edm.String "Transaction Descr."
PX.Objects.DR.DRSchedule.IsCustom : Edm.Boolean [required] "Is Custom"
PX.Objects.DR.DRSchedule.IsDraft : Edm.Boolean [required] "Is Draft"
PX.Objects.DR.DRSchedule.IsOverridden : Edm.Boolean [required] "Override"
PX.Objects.DR.DRSchedule.DetailLineCntr : Edm.Int32 [required]
PX.Objects.DR.DRSchedule.ProjectID : Edm.Int32 "Project"
PX.Objects.DR.DRSchedule.CuryID : Edm.String "Doc. Currency"
PX.Objects.DR.DRSchedule.CuryInfoID : Edm.Int64
PX.Objects.DR.DRSchedule.DocumentType : Edm.String "Doc. Type"
PX.Objects.DR.DRSchedule.BAccountType : Edm.String "Entity Type"
PX.Objects.DR.DRSchedule.OrigLineAmt : Edm.Decimal "Line Amount"
PX.Objects.DR.DRSchedule.CuryNetTranPrice : Edm.Decimal "Net Tran. Price"
PX.Objects.DR.DRSchedule.NetTranPrice : Edm.Decimal "Base Net Tran. Price"
PX.Objects.DR.DRSchedule.ComponentsTotal : Edm.Decimal "Comp. Total"
PX.Objects.DR.DRSchedule.DefTotal : Edm.Decimal "Comp.  Deferred"
PX.Objects.DR.DRSchedule.DocumentTypeEx : Edm.String "Doc. Type"
PX.Objects.DR.DRSchedule.TermStartDate : Edm.DateTimeOffset "Term Start Date"
PX.Objects.DR.DRSchedule.TermEndDate : Edm.DateTimeOffset "Term End Date"
PX.Objects.DR.DRSchedule.Status : Edm.String "Status"
PX.Objects.DR.DRSchedule.IsPoolVisible : Edm.Boolean
PX.Objects.DR.DRSchedule.IsRecalculated : Edm.Boolean
PX.Objects.DR.DRSchedule.IsSuspense : Edm.Boolean
PX.Objects.DR.DRSchedule.NoteID : Edm.Guid
PX.Objects.DR.DRSchedule.NoteText : Edm.String "Note Text"
PX.Objects.DR.DRSchedule.tstamp : Edm.Binary
PX.Objects.DR.DRSchedule.CreatedByID : Edm.Guid "Created By"
PX.Objects.DR.DRSchedule.CreatedByScreenID : Edm.String
PX.Objects.DR.DRSchedule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.DR.DRSchedule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.DR.DRSchedule.LastModifiedByScreenID : Edm.String
PX.Objects.DR.DRSchedule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.DR.DRSchedule.CuryRate : Edm.Decimal
PX.Objects.DR.DRSchedule.CuryViewState : Edm.Boolean
PX.Objects.DR.DRSchedule.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.DR.DRSchedule.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.DR.DRSchedule.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.DR.DRSchedule.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.DR.DRSchedule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.DR.DRSchedule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.DR.DRSchedule.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.DR.DRSchedule.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)
PX.Objects.DR.DRSchedule.LocationByBAccountLocID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.DR.DRSchedule.LocationByBAccountID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.DR.DRSchedule.ARTranByLineNbr -> PX.Objects.AR.ARTran (DocType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.DR.DRSchedule.APTranByLineNbr -> PX.Objects.AP.APTran (DocType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.DR.DRSchedule.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.DR.DRSchedule.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.DR.DRSchedule.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.DR.DRSchedule.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.DR.DRSchedule.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)

# PX.Objects.DR.DRScheduleDetail (EntityType)

Label: "Deferral Schedule Component"
Key: ComponentID, DetailLineNbr, ScheduleID
Entity sets: PX_Objects_DR_DRScheduleDetail, DeferralScheduleComponent, DRScheduleDetail
Non-filterable, non-selectable: ParentInventoryID, ReceiptNbr, PONbr, AllowControlAccountForModule, DefTotal, DocumentType, BAccountType, DefCodeType, AllocationWeightResidual, CuryID, CuryRate, CuryViewState

PX.Objects.DR.DRScheduleDetail.ScheduleID : Edm.Int32 [key] "Schedule Number"
PX.Objects.DR.DRScheduleDetail.ComponentID : Edm.Int32 [key] "Component ID"
PX.Objects.DR.DRScheduleDetail.ParentInventoryID : Edm.Int32
PX.Objects.DR.DRScheduleDetail.DetailLineNbr : Edm.Int32 [key] "Detail Line Nbr."
PX.Objects.DR.DRScheduleDetail.Module : Edm.String "Module"
PX.Objects.DR.DRScheduleDetail.DocType : Edm.String "Doc. Type"
PX.Objects.DR.DRScheduleDetail.RefNbr : Edm.String "Ref. Nbr."
PX.Objects.DR.DRScheduleDetail.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.DR.DRScheduleDetail.CuryInfoID : Edm.Int64
PX.Objects.DR.DRScheduleDetail.Status : Edm.String "Status"
PX.Objects.DR.DRScheduleDetail.TotalAmt : Edm.Decimal [required] "Total Amount"
PX.Objects.DR.DRScheduleDetail.CuryTotalAmt : Edm.Decimal
PX.Objects.DR.DRScheduleDetail.CuryDefAmt : Edm.Decimal
PX.Objects.DR.DRScheduleDetail.DefAmt : Edm.Decimal [required] "Deferred Amount"
PX.Objects.DR.DRScheduleDetail.DefCode : Edm.String "Deferral Code"
PX.Objects.DR.DRScheduleDetail.ReceiptNbr : Edm.String
PX.Objects.DR.DRScheduleDetail.PONbr : Edm.String
PX.Objects.DR.DRScheduleDetail.AllowControlAccountForModule : Edm.String
PX.Objects.DR.DRScheduleDetail.IsOpen : Edm.Boolean [required] "IsOpen"
PX.Objects.DR.DRScheduleDetail.DefTotal : Edm.Decimal "Line Total"
PX.Objects.DR.DRScheduleDetail.LineCntr : Edm.Int32 [required]
PX.Objects.DR.DRScheduleDetail.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.DR.DRScheduleDetail.TranPeriodID : Edm.String
PX.Objects.DR.DRScheduleDetail.FinPeriodID : Edm.String "Post Period"
PX.Objects.DR.DRScheduleDetail.LastRecFinPeriodID : Edm.String "Last Recognition Period"
PX.Objects.DR.DRScheduleDetail.CloseFinPeriodID : Edm.String "Close Period"
PX.Objects.DR.DRScheduleDetail.CreditLineNbr : Edm.Int32 [required] "Credit Line Nbr."
PX.Objects.DR.DRScheduleDetail.BAccountID : Edm.Int32 "Business Account"
PX.Objects.DR.DRScheduleDetail.IsCustom : Edm.Boolean [required] "Is Custom"
PX.Objects.DR.DRScheduleDetail.DocumentType : Edm.String "Doc. Type"
PX.Objects.DR.DRScheduleDetail.BAccountType : Edm.String
PX.Objects.DR.DRScheduleDetail.DefCodeType : Edm.String
PX.Objects.DR.DRScheduleDetail.ProjectID : Edm.Int32 "Contract ID"
PX.Objects.DR.DRScheduleDetail.IsResidual : Edm.Boolean [required]
PX.Objects.DR.DRScheduleDetail.UOM : Edm.String "UOM"
PX.Objects.DR.DRScheduleDetail.BaseQty : Edm.Decimal "Base Qty."
PX.Objects.DR.DRScheduleDetail.Qty : Edm.Decimal "Quantity"
PX.Objects.DR.DRScheduleDetail.FairValuePrice : Edm.Decimal "Fair Value Price"
PX.Objects.DR.DRScheduleDetail.DiscountPercent : Edm.Decimal "Discount Percent"
PX.Objects.DR.DRScheduleDetail.Percentage : Edm.Decimal "Share"
PX.Objects.DR.DRScheduleDetail.CoTermRate : Edm.Decimal "CoTerm Rate"
PX.Objects.DR.DRScheduleDetail.EffectiveFairValuePrice : Edm.Decimal "Effective Fair Value Price"
PX.Objects.DR.DRScheduleDetail.FairValueCuryID : Edm.String "Fair Value Currency"
PX.Objects.DR.DRScheduleDetail.AllocationWeightResidual : Edm.Decimal "Allocation Weight Residual"
PX.Objects.DR.DRScheduleDetail.tstamp : Edm.Binary
PX.Objects.DR.DRScheduleDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.DR.DRScheduleDetail.CreatedByScreenID : Edm.String
PX.Objects.DR.DRScheduleDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.DR.DRScheduleDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.DR.DRScheduleDetail.LastModifiedByScreenID : Edm.String
PX.Objects.DR.DRScheduleDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.DR.DRScheduleDetail.CuryID : Edm.String "Currency"
PX.Objects.DR.DRScheduleDetail.CuryRate : Edm.Decimal
PX.Objects.DR.DRScheduleDetail.CuryViewState : Edm.Boolean
PX.Objects.DR.DRScheduleDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.DR.DRScheduleDetail.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.DR.DRScheduleDetail.ContractByProjectID -> PX.Objects.CT.Contract (ProjectID=ContractID)
PX.Objects.DR.DRScheduleDetail.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.DR.DRScheduleDetail.DRDeferredCodeByDefCode -> PX.Objects.DR.DRDeferredCode (DefCode=DeferredCodeID)
PX.Objects.DR.DRScheduleDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.DR.DRScheduleDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.DR.DRScheduleDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.DR.DRScheduleDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.DR.DRScheduleDetail.DRScheduleByScheduleID -> PX.Objects.DR.DRSchedule (ScheduleID=ScheduleID)
PX.Objects.DR.DRScheduleDetail.INUnitByComponentID -> PX.Objects.IN.INUnit (UOM=FromUnit, ComponentID=InventoryID)
PX.Objects.DR.DRScheduleDetail.AccountByDefAcctID -> PX.Objects.GL.Account
PX.Objects.DR.DRScheduleDetail.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.DR.DRScheduleDetail.SubByDefSubID -> PX.Objects.GL.Sub
PX.Objects.DR.DRScheduleDetail.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.DR.DRScheduleDetail.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)

# PX.Objects.DR.DRScheduleTran (EntityType)

Label: "DRScheduleTran"
Key: ComponentID, DetailLineNbr, LineNbr, ScheduleID
Entity sets: PX_Objects_DR_DRScheduleTran, DRScheduleTran
Non-filterable, non-selectable: ReceiptNbr, PONbr, AllowControlAccountForModule

PX.Objects.DR.DRScheduleTran.ScheduleID : Edm.Int32 [key] "Schedule Number"
PX.Objects.DR.DRScheduleTran.ComponentID : Edm.Int32 [key]
PX.Objects.DR.DRScheduleTran.DetailLineNbr : Edm.Int32 [key]
PX.Objects.DR.DRScheduleTran.LineNbr : Edm.Int32 [key] "Tran. Nbr."
PX.Objects.DR.DRScheduleTran.Status : Edm.String "Status"
PX.Objects.DR.DRScheduleTran.RecDate : Edm.DateTimeOffset "Rec. Date"
PX.Objects.DR.DRScheduleTran.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.DR.DRScheduleTran.Amount : Edm.Decimal [required] "Amount"
PX.Objects.DR.DRScheduleTran.ReceiptNbr : Edm.String
PX.Objects.DR.DRScheduleTran.PONbr : Edm.String
PX.Objects.DR.DRScheduleTran.AllowControlAccountForModule : Edm.String
PX.Objects.DR.DRScheduleTran.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.DR.DRScheduleTran.TranPeriodID : Edm.String
PX.Objects.DR.DRScheduleTran.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.DR.DRScheduleTran.AdjgDocType : Edm.String
PX.Objects.DR.DRScheduleTran.AdjgRefNbr : Edm.String
PX.Objects.DR.DRScheduleTran.AdjNbr : Edm.Int32
PX.Objects.DR.DRScheduleTran.IsSamePeriod : Edm.Boolean [required] "Is Same Period"
PX.Objects.DR.DRScheduleTran.tstamp : Edm.Binary
PX.Objects.DR.DRScheduleTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.DR.DRScheduleTran.CreatedByScreenID : Edm.String
PX.Objects.DR.DRScheduleTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.DR.DRScheduleTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.DR.DRScheduleTran.LastModifiedByScreenID : Edm.String
PX.Objects.DR.DRScheduleTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.DR.DRScheduleTran.InventoryItemByComponentID -> PX.Objects.IN.InventoryItem (ComponentID=InventoryID)
PX.Objects.DR.DRScheduleTran.DRScheduleDetailByDetailLineNbr -> PX.Objects.DR.DRScheduleDetail (ScheduleID=ScheduleID, ComponentID=ComponentID, DetailLineNbr=DetailLineNbr)
PX.Objects.DR.DRScheduleTran.DRScheduleDetailByComponentID -> PX.Objects.DR.DRScheduleDetail (ScheduleID=ScheduleID, ComponentID=ComponentID)
PX.Objects.DR.DRScheduleTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.DR.DRScheduleTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.DR.DRScheduleTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.DR.DRScheduleTran.DRScheduleByScheduleID -> PX.Objects.DR.DRSchedule (ScheduleID=ScheduleID)
PX.Objects.DR.DRScheduleTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.DR.DRScheduleTran.SubBySubID -> PX.Objects.GL.Sub

# PX.Objects.DR.DRScheduleTranLineLink (EntityType)

Label: "DR Schedule Transaction Lines"
Key: ScheduleID
Entity sets: PX_Objects_DR_DRScheduleTranLineLink, DRScheduleTransactionLines, DRScheduleTranLineLink

PX.Objects.DR.DRScheduleTranLineLink.ScheduleID : Edm.Int32 [key] "Schedule ID"
PX.Objects.DR.DRScheduleTranLineLink.Module : Edm.String "Module"
PX.Objects.DR.DRScheduleTranLineLink.DocType : Edm.String "Doc Type"
PX.Objects.DR.DRScheduleTranLineLink.RefNbr : Edm.String "Reference Nbr."
PX.Objects.DR.DRScheduleTranLineLink.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.DR.DRScheduleTranLineLink.SortOrder : Edm.Int32 "Line Nbr."
PX.Objects.DR.DRScheduleTranLineLink.ARTranByLineNbr -> PX.Objects.AR.ARTran (DocType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.DR.DRScheduleTranLineLink.APTranByLineNbr -> PX.Objects.AP.APTran (DocType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.DR.DRScheduleTranLineLink.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.DR.DRScheduleTranLineLink.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.DR.DRScheduleTranLineLink.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.DR.DRScheduleTranLineLink.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.DR.DRScheduleTranLineLink.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)

# PX.Objects.DR.DRSetup (EntityType)

Label: "Deferred Revenue Preferences"
Singletons: PX_Objects_DR_DRSetup, DeferredRevenuePreferences, DRSetup

PX.Objects.DR.DRSetup.ScheduleNumberingID : Edm.String "Deferral Schedule Numbering Sequence"
PX.Objects.DR.DRSetup.PendingRevenueValidate : Edm.Boolean [required]
PX.Objects.DR.DRSetup.PendingExpenseValidate : Edm.Boolean [required]
PX.Objects.DR.DRSetup.NumberingByScheduleNumberingID -> PX.Objects.CS.Numbering (ScheduleNumberingID=NumberingID)
PX.Objects.DR.DRSetup.AccountBySuspenseAccountID -> PX.Objects.GL.Account
PX.Objects.DR.DRSetup.SubBySuspenseSubID -> PX.Objects.GL.Sub

# PX.Objects.EP.ClockInClockOut.EPClockInTimerData (EntityType)

Label: "Timer"
Key: TimerDataID
Entity sets: PX_Objects_EP_ClockInClockOut_EPClockInTimerData, Timer, EPClockInTimerData
Non-filterable, non-selectable: NoteText, Status, EntityName, DocumentDescr, StartDateUTC, TimerDisplay, IsClockIn, IsPause, IsStart, IsStop

PX.Objects.EP.ClockInClockOut.EPClockInTimerData.TimerDataID : Edm.Int32 [key]
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.EmployeeID : Edm.Int32
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.TimeLogTypeID : Edm.String "Type"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.Summary : Edm.String "Summary"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.DocumentNbr : Edm.String "Document Nbr."
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.RelatedEntityType : Edm.String
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.RelatedEntityID : Edm.Guid
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.TimeSpent : Edm.Int32 "Time Spent"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.NoteID : Edm.Guid
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.NoteText : Edm.String "Note Text"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.Status : Edm.String "Status"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.EntityName : Edm.String "Entity Name"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.DocumentDescr : Edm.String "Track Time To"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.StartDateUTC : Edm.String "Start Date"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.TimerDisplay : Edm.String
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.IsClockIn : Edm.Boolean
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.IsPause : Edm.Boolean
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.IsStart : Edm.Boolean
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.IsStop : Edm.Boolean
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.tstamp : Edm.Binary
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.CreatedByScreenID : Edm.String "Created At"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.ClockInClockOut.EPClockInTimerData.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.EP.ClockInClockOut.EPTimeLog (EntityType)

Label: "Time Log"
Key: TimeLogID
Entity sets: PX_Objects_EP_ClockInClockOut_EPTimeLog, TimeLog, EPTimeLog

PX.Objects.EP.ClockInClockOut.EPTimeLog.TimeLogID : Edm.Int32 [key]
PX.Objects.EP.ClockInClockOut.EPTimeLog.EmployeeID : Edm.Int32 "Employee"
PX.Objects.EP.ClockInClockOut.EPTimeLog.RelatedEntityType : Edm.String "Record Type"
PX.Objects.EP.ClockInClockOut.EPTimeLog.RelatedEntityID : Edm.Guid
PX.Objects.EP.ClockInClockOut.EPTimeLog.TimeLogTypeID : Edm.String "Type"
PX.Objects.EP.ClockInClockOut.EPTimeLog.DocumentNbr : Edm.String "Record ID"
PX.Objects.EP.ClockInClockOut.EPTimeLog.Summary : Edm.String "Description"
PX.Objects.EP.ClockInClockOut.EPTimeLog.ReportedInTimeZoneID : Edm.String "Reported in Time Zone"
PX.Objects.EP.ClockInClockOut.EPTimeLog.StartDateReported : Edm.DateTimeOffset "Start Date"
PX.Objects.EP.ClockInClockOut.EPTimeLog.EndDateReported : Edm.DateTimeOffset "End Date"
PX.Objects.EP.ClockInClockOut.EPTimeLog.StartDate : Edm.DateTimeOffset "Start Date UTC"
PX.Objects.EP.ClockInClockOut.EPTimeLog.EndDate : Edm.DateTimeOffset "End Date UTC"
PX.Objects.EP.ClockInClockOut.EPTimeLog.TimeSpent : Edm.Int32 "Time Spent"
PX.Objects.EP.ClockInClockOut.EPTimeLog.IsLocked : Edm.Boolean [required]
PX.Objects.EP.ClockInClockOut.EPTimeLog.tstamp : Edm.Binary
PX.Objects.EP.ClockInClockOut.EPTimeLog.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.ClockInClockOut.EPTimeLog.CreatedByScreenID : Edm.String "Created At"
PX.Objects.EP.ClockInClockOut.EPTimeLog.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.EP.ClockInClockOut.EPTimeLog.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.ClockInClockOut.EPTimeLog.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.EP.ClockInClockOut.EPTimeLog.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.EP.ClockInClockOut.EPTimeLog.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.EP.ClockInClockOut.EPTimeLog.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.ClockInClockOut.EPTimeLog.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.EP.ClockInClockOut.EPTimeLogType (EntityType)

Label: "Time Log Type"
Key: TimeLogTypeID
Entity sets: PX_Objects_EP_ClockInClockOut_EPTimeLogType, TimeLogType, EPTimeLogType

PX.Objects.EP.ClockInClockOut.EPTimeLogType.TimeLogTypeID : Edm.String [key] "Type"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.Description : Edm.String "Description"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.EarningTypeID : Edm.String "Earning Type"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.tstamp : Edm.Binary
PX.Objects.EP.ClockInClockOut.EPTimeLogType.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.CreatedByScreenID : Edm.String "Created At"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.LastModifiedByScreenID : Edm.String "Last Modified At"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.EP.ClockInClockOut.EPTimeLogType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.ClockInClockOut.EPTimeLogType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.ClockInClockOut.EPTimeLogType.EPEarningTypeByEarningTypeID -> PX.Objects.EP.EPEarningType (EarningTypeID=TypeCD)

# PX.Objects.EP.ContractEx (EntityType)

Label: "Contract"
BaseType: PX.Objects.CT.Contract
Key: BaseType, ContractCD (inherited from PX.Objects.CT.Contract)
Entity sets: PX_Objects_EP_ContractEx

# PX.Objects.EP.ContractExEx (EntityType)

Label: "Contract"
BaseType: PX.Objects.CT.Contract
Key: BaseType, ContractCD (inherited from PX.Objects.CT.Contract)
Entity sets: PX_Objects_EP_ContractExEx

# PX.Objects.EP.DAC.EPEmployeeCorpCardLink (EntityType)

Label: "Employee Corporate Card Reference"
Key: CorpCardID, EmployeeID
Entity sets: PX_Objects_EP_DAC_EPEmployeeCorpCardLink, EmployeeCorporateCardReference, EPEmployeeCorpCardLink

PX.Objects.EP.DAC.EPEmployeeCorpCardLink.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.EP.DAC.EPEmployeeCorpCardLink.CorpCardID : Edm.Int32 [key] "Corporate Card ID"
PX.Objects.EP.DAC.EPEmployeeCorpCardLink.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.EP.DAC.EPEmployeeCorpCardLink.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.EP.DAC.EPEmployeeCorpCardLink.CACorpCardByCorpCardID -> PX.Objects.CA.CACorpCard (CorpCardID=CorpCardID)

# PX.Objects.EP.DAC.EPExpenseClaimForCurrentUser (EntityType)

Label: "Expense Claim"
BaseType: PX.Objects.EP.EPExpenseClaim
Key: RefNbr (inherited from PX.Objects.EP.EPExpenseClaim)
Entity sets: PX_Objects_EP_DAC_EPExpenseClaimForCurrentUser, ExpenseClaim1, EPExpenseClaimForCurrentUser

# PX.Objects.EP.DAC.EPRuleApprover (EntityType)

Label: "Rule Approver"
Key: RuleApproverID
Entity sets: PX_Objects_EP_DAC_EPRuleApprover, RuleApprover, EPRuleApprover

PX.Objects.EP.DAC.EPRuleApprover.RuleApproverID : Edm.Int32 [key]
PX.Objects.EP.DAC.EPRuleApprover.OwnerID : Edm.Int32 "Employee Name"
PX.Objects.EP.DAC.EPRuleApprover.RuleID : Edm.Guid "Rule ID"
PX.Objects.EP.DAC.EPRuleApprover.CreatedByScreenID : Edm.String
PX.Objects.EP.DAC.EPRuleApprover.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.DAC.EPRuleApprover.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.DAC.EPRuleApprover.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.DAC.EPRuleApprover.LastModifiedByScreenID : Edm.String
PX.Objects.EP.DAC.EPRuleApprover.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.DAC.EPRuleApprover.tstamp : Edm.Binary
PX.Objects.EP.DAC.EPRuleApprover.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.EP.DAC.EPRuleApprover.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.DAC.EPRuleApprover.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.DAC.EPRuleApprover.EPRuleByOwnerID -> PX.Objects.EP.EPRule (OwnerID=RuleID)
PX.Objects.EP.DAC.EPRuleApprover.EPRuleByRuleID -> PX.Objects.EP.EPRule (RuleID=RuleID)

# PX.Objects.EP.EPActivityApprove (EntityType)

Label: "Time Activity"
BaseType: PX.Objects.CR.PMTimeActivity
Key: NoteID (inherited from PX.Objects.CR.PMTimeActivity)
Entity sets: PX_Objects_EP_EPActivityApprove
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.EP.EPActivityApprove.IsApproved : Edm.Boolean "Approve"
PX.Objects.EP.EPActivityApprove.IsReject : Edm.Boolean "Reject"
PX.Objects.EP.EPActivityApprove.ProjectDescription : Edm.String "Project Description"
PX.Objects.EP.EPActivityApprove.ProjectTaskDescription : Edm.String "Project Task Description"
PX.Objects.EP.EPActivityApprove.CostCodeDescription : Edm.String "Cost Code Description"
PX.Objects.EP.EPActivityApprove.Hold : Edm.Boolean "Hold"

# PX.Objects.EP.EPActivityApprove2 (EntityType)

Label: "Mass Weekly Crew Time Entry"
BaseType: PX.Objects.EP.EPActivityApprove
Key: NoteID (inherited from PX.Objects.CR.PMTimeActivity)
Entity sets: PX_Objects_EP_EPActivityApprove2, MassWeeklyCrewTimeEntry, EPActivityApprove2

PX.Objects.EP.EPActivityApprove2.ProjectID : Edm.Int32 "Project"

# PX.Objects.EP.EPActivityRelease (EntityType)

Label: "Release Time Activity"
BaseType: PX.Objects.EP.EPActivityApprove
Key: NoteID (inherited from PX.Objects.CR.PMTimeActivity)
Entity sets: PX_Objects_EP_EPActivityRelease, ReleaseTimeActivity, EPActivityRelease

PX.Objects.EP.EPActivityRelease.CaseCD : Edm.String

# PX.Objects.EP.EPActivityType (EntityType)

Label: "Activity Type"
Key: Type
Entity sets: PX_Objects_EP_EPActivityType, ActivityType, EPActivityType
Non-filterable, non-selectable: NoteText

PX.Objects.EP.EPActivityType.Type : Edm.String [key] "Type ID"
PX.Objects.EP.EPActivityType.Description : Edm.String "Description"
PX.Objects.EP.EPActivityType.Active : Edm.Boolean [required] "Active"
PX.Objects.EP.EPActivityType.IsDefault : Edm.Boolean [required] "System Default"
PX.Objects.EP.EPActivityType.ImageUrl : Edm.String "Image"
PX.Objects.EP.EPActivityType.Color : Edm.String "Color"
PX.Objects.EP.EPActivityType.Application : Edm.Int32 [required] "Originated By"
PX.Objects.EP.EPActivityType.PrivateByDefault : Edm.Boolean "Internal"
PX.Objects.EP.EPActivityType.RequireTimeByDefault : Edm.Boolean "Track Time and Costs"
PX.Objects.EP.EPActivityType.Incoming : Edm.Boolean [required] "Incoming"
PX.Objects.EP.EPActivityType.Outgoing : Edm.Boolean [required] "Outgoing"
PX.Objects.EP.EPActivityType.NoteID : Edm.Guid
PX.Objects.EP.EPActivityType.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPActivityType.tstamp : Edm.Binary
PX.Objects.EP.EPActivityType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPActivityType.LastModifiedDateTime : Edm.DateTimeOffset "Last Activity"
PX.Objects.EP.EPActivityType.ClassID : Edm.Int32 [required] "Class"
PX.Objects.EP.EPActivityType.IsSystem : Edm.Boolean "Is System"
PX.Objects.EP.EPActivityType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPActivityType.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.EP.EPActivityType.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.EP.EPActivityType.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.EP.EPActivityType.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.EP.EPActivityType.NotificationCollection -> Collection(PX.SM.Notification)

# PX.Objects.EP.EPApproval (EntityType)

Label: "Approval"
Key: ApprovalID
Entity sets: PX_Objects_EP_EPApproval, Approval, EPApproval
Non-filterable, non-selectable: NoteText, DocType

PX.Objects.EP.EPApproval.ApprovalID : Edm.Int32 [key] "Approval ID"
PX.Objects.EP.EPApproval.RefNoteIDType : Edm.String "Related Entity Type"
PX.Objects.EP.EPApproval.RefNoteID : Edm.Guid "References Nbr."
PX.Objects.EP.EPApproval.AssignmentMapID : Edm.Int32 "Map"
PX.Objects.EP.EPApproval.StepID : Edm.Guid "Map Step"
PX.Objects.EP.EPApproval.RuleID : Edm.Guid "Map Rule"
PX.Objects.EP.EPApproval.NotificationID : Edm.Int32
PX.Objects.EP.EPApproval.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.EP.EPApproval.OrigOwnerID : Edm.Int32 "Original Assignee"
PX.Objects.EP.EPApproval.OwnerID : Edm.Int32 "Assignee"
PX.Objects.EP.EPApproval.DelegationRecordID : Edm.Int32 "Delegation"
PX.Objects.EP.EPApproval.IgnoreDelegations : Edm.Boolean [required] "Ignore Delegations"
PX.Objects.EP.EPApproval.DocumentOwnerID : Edm.Int32 "Owner"
PX.Objects.EP.EPApproval.ApprovedByID : Edm.Int32 "Approver ID"
PX.Objects.EP.EPApproval.ApproveDate : Edm.DateTimeOffset "Date"
PX.Objects.EP.EPApproval.ApprovalSortOrder : Edm.Int32
PX.Objects.EP.EPApproval.NoteID : Edm.Guid
PX.Objects.EP.EPApproval.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPApproval.Status : Edm.String "Decision"
PX.Objects.EP.EPApproval.DocDate : Edm.DateTimeOffset "Document Date"
PX.Objects.EP.EPApproval.BAccountID : Edm.Int32 "Business Account"
PX.Objects.EP.EPApproval.WaitTime : Edm.Int32 "Wait Time"
PX.Objects.EP.EPApproval.PendingWaitTime : Edm.Int32 "Pending Wait Time"
PX.Objects.EP.EPApproval.IsPreApproved : Edm.Boolean [required]
PX.Objects.EP.EPApproval.Descr : Edm.String "Description"
PX.Objects.EP.EPApproval.Reason : Edm.String "Reason"
PX.Objects.EP.EPApproval.Details : Edm.String "Details"
PX.Objects.EP.EPApproval.CuryInfoID : Edm.Int64
PX.Objects.EP.EPApproval.CuryTotalAmount : Edm.Decimal "Amount"
PX.Objects.EP.EPApproval.TotalAmount : Edm.Decimal
PX.Objects.EP.EPApproval.SourceItemType : Edm.String
PX.Objects.EP.EPApproval.DocType : Edm.String "Document"
PX.Objects.EP.EPApproval.Obsolete : Edm.Boolean [required] "Obsolete"
PX.Objects.EP.EPApproval.ObsoleteText : Edm.String "Obsolete Status"
PX.Objects.EP.EPApproval.tstamp : Edm.Binary
PX.Objects.EP.EPApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPApproval.CreatedByScreenID : Edm.String
PX.Objects.EP.EPApproval.CreatedDateTime : Edm.DateTimeOffset "Assignment Date"
PX.Objects.EP.EPApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPApproval.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPApproval.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.EP.EPApproval.ContactByOrigOwnerID -> PX.Objects.CR.Contact (OrigOwnerID=ContactID)
PX.Objects.EP.EPApproval.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.EP.EPApproval.ContactByDocumentOwnerID -> PX.Objects.CR.Contact (DocumentOwnerID=ContactID)
PX.Objects.EP.EPApproval.ContactByApprovedByID -> PX.Objects.CR.Contact (ApprovedByID=ContactID)
PX.Objects.EP.EPApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPApproval.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.EP.EPApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)
PX.Objects.EP.EPApproval.EPRuleByRuleID -> PX.Objects.EP.EPRule (RuleID=RuleID)
PX.Objects.EP.EPApproval.EPRuleByStepID -> PX.Objects.EP.EPRule (StepID=RuleID)
PX.Objects.EP.EPApproval.EPWingmanByDelegationRecordID -> PX.Objects.EP.EPWingman (DelegationRecordID=RecordID)

# PX.Objects.EP.EPAssignmentMap (EntityType)

Label: "Assignment Map"
Key: AssignmentMapID
Entity sets: PX_Objects_EP_EPAssignmentMap, AssignmentMap, EPAssignmentMap
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.EP.EPAssignmentMap.AssignmentMapID : Edm.Int32 [key] "Map"
PX.Objects.EP.EPAssignmentMap.Name : Edm.String "Name"
PX.Objects.EP.EPAssignmentMap.EntityType : Edm.String "Entity"
PX.Objects.EP.EPAssignmentMap.GraphType : Edm.String "Entity"
PX.Objects.EP.EPAssignmentMap.MapType : Edm.Int32 [required] "Map Type"
PX.Objects.EP.EPAssignmentMap.NoteID : Edm.Guid
PX.Objects.EP.EPAssignmentMap.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPAssignmentMap.tstamp : Edm.Binary
PX.Objects.EP.EPAssignmentMap.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPAssignmentMap.CreatedByScreenID : Edm.String
PX.Objects.EP.EPAssignmentMap.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPAssignmentMap.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPAssignmentMap.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPAssignmentMap.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPAssignmentMap.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.EP.EPAssignmentMap.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPAssignmentMap.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPAssignmentMap.ProjectManagementSetupCollection -> Collection(PX.Objects.PJ.ProjectManagement.PJ.DAC.ProjectManagementSetup)
PX.Objects.EP.EPAssignmentMap.CRContactClassCollection -> Collection(PX.Objects.CR.CRContactClass)
PX.Objects.EP.EPAssignmentMap.CRCustomerClassCollection -> Collection(PX.Objects.CR.CRCustomerClass)
PX.Objects.EP.EPAssignmentMap.CRLeadClassCollection -> Collection(PX.Objects.CR.CRLeadClass)
PX.Objects.EP.EPAssignmentMap.CROpportunityClassCollection -> Collection(PX.Objects.CR.CROpportunityClass)
PX.Objects.EP.EPAssignmentMap.EPRuleCollection -> Collection(PX.Objects.EP.EPRule)
PX.Objects.EP.EPAssignmentMap.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.Objects.EP.EPAssignmentMap.SCSetupCollection -> Collection(PX.Objects.CN.SCSetup)
PX.Objects.EP.EPAssignmentMap.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.EP.EPAssignmentMap.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.Objects.EP.EPAssignmentMap.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.EP.EPAssignmentMap.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.Objects.EP.EPAssignmentMap.SOSetupCollection -> Collection(PX.Objects.SO.SOSetup)
PX.Objects.EP.EPAssignmentMap.SOSetupApprovalCollection -> Collection(PX.Objects.SO.SOSetupApproval)
PX.Objects.EP.EPAssignmentMap.SOSetupInvoiceApprovalCollection -> Collection(PX.Objects.SO.SOSetupInvoiceApproval)
PX.Objects.EP.EPAssignmentMap.RQSetupCollection -> Collection(PX.Objects.RQ.RQSetup)
PX.Objects.EP.EPAssignmentMap.RQSetupApprovalCollection -> Collection(PX.Objects.RQ.RQSetupApproval)
PX.Objects.EP.EPAssignmentMap.POSetupCollection -> Collection(PX.Objects.PO.POSetup)
PX.Objects.EP.EPAssignmentMap.POSetupApprovalCollection -> Collection(PX.Objects.PO.POSetupApproval)
PX.Objects.EP.EPAssignmentMap.INSetupApprovalCollection -> Collection(PX.Objects.IN.DAC.INSetupApproval)
PX.Objects.EP.EPAssignmentMap.GLSetupApprovalCollection -> Collection(PX.Objects.GL.GLSetupApproval)
PX.Objects.EP.EPAssignmentMap.CASetupApprovalCollection -> Collection(PX.Objects.CA.CASetupApproval)
PX.Objects.EP.EPAssignmentMap.ARSetupApprovalCollection -> Collection(PX.Objects.AR.ARSetupApproval)
PX.Objects.EP.EPAssignmentMap.EPAssignmentRouteCollection -> Collection(PX.Objects.EP.EPAssignmentRoute)
PX.Objects.EP.EPAssignmentMap.APSetupApprovalCollection -> Collection(PX.Objects.AP.APSetupApproval)
PX.Objects.EP.EPAssignmentMap.AMECOSetupApprovalCollection -> Collection(PX.Objects.AM.AMECOSetupApproval)
PX.Objects.EP.EPAssignmentMap.AMECRSetupApprovalCollection -> Collection(PX.Objects.AM.AMECRSetupApproval)
PX.Objects.EP.EPAssignmentMap.SVSetupInvoiceApprovalCollection -> Collection(PX.Objects.SV.SVSetupInvoiceApproval)

# PX.Objects.EP.EPAssignmentRoute (EntityType)

Label: "Legacy Assignment Route"
Key: AssignmentRouteID
Entity sets: PX_Objects_EP_EPAssignmentRoute, LegacyAssignmentRoute, EPAssignmentRoute
Non-filterable, non-selectable: Icon

PX.Objects.EP.EPAssignmentRoute.AssignmentRouteID : Edm.Int32 [key] "Route ID"
PX.Objects.EP.EPAssignmentRoute.Parent : Edm.Int32
PX.Objects.EP.EPAssignmentRoute.AssignmentMapID : Edm.Int32
PX.Objects.EP.EPAssignmentRoute.RouterType : Edm.String "Type"
PX.Objects.EP.EPAssignmentRoute.WorkgroupID : Edm.Int32 "Assign to"
PX.Objects.EP.EPAssignmentRoute.OwnerID : Edm.Int32 "Assign to"
PX.Objects.EP.EPAssignmentRoute.OwnerSource : Edm.String "Owner Source"
PX.Objects.EP.EPAssignmentRoute.UseWorkgroupByOwner : Edm.Boolean [required] "Use Workgroup by Owner"
PX.Objects.EP.EPAssignmentRoute.Name : Edm.String "Name"
PX.Objects.EP.EPAssignmentRoute.RouteID : Edm.Int32 "Jump to"
PX.Objects.EP.EPAssignmentRoute.Sequence : Edm.Int32 "Seq."
PX.Objects.EP.EPAssignmentRoute.RuleType : Edm.String "Rule Type"
PX.Objects.EP.EPAssignmentRoute.WaitTime : Edm.Int32 "Wait Time"
PX.Objects.EP.EPAssignmentRoute.Icon : Edm.String
PX.Objects.EP.EPAssignmentRoute.tstamp : Edm.Binary
PX.Objects.EP.EPAssignmentRoute.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPAssignmentRoute.CreatedByScreenID : Edm.String
PX.Objects.EP.EPAssignmentRoute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPAssignmentRoute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPAssignmentRoute.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPAssignmentRoute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPAssignmentRoute.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.EP.EPAssignmentRoute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPAssignmentRoute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPAssignmentRoute.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.EP.EPAssignmentRoute.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)
PX.Objects.EP.EPAssignmentRoute.EPAssignmentRouteByParent -> PX.Objects.EP.EPAssignmentRoute (Parent=AssignmentRouteID)
PX.Objects.EP.EPAssignmentRoute.EPAssignmentRouteByRouteID -> PX.Objects.EP.EPAssignmentRoute (RouteID=AssignmentRouteID)
PX.Objects.EP.EPAssignmentRoute.EPAssignmentRouteCollection -> Collection(PX.Objects.EP.EPAssignmentRoute)
PX.Objects.EP.EPAssignmentRoute.EPAssignmentRuleCollection -> Collection(PX.Objects.EP.EPAssignmentRule)

# PX.Objects.EP.EPAssignmentRule (EntityType)

Label: "Legacy Assignmnent Rule"
Key: AssignmentRuleID
Entity sets: PX_Objects_EP_EPAssignmentRule, LegacyAssignmnentRule, EPAssignmentRule

PX.Objects.EP.EPAssignmentRule.AssignmentRuleID : Edm.Int32 [key]
PX.Objects.EP.EPAssignmentRule.AssignmentRouteID : Edm.Int32
PX.Objects.EP.EPAssignmentRule.Entity : Edm.String "Entity"
PX.Objects.EP.EPAssignmentRule.FieldName : Edm.String "Field Name"
PX.Objects.EP.EPAssignmentRule.FieldValue : Edm.String "Field Value"
PX.Objects.EP.EPAssignmentRule.Condition : Edm.Int32 [required] "Condition"
PX.Objects.EP.EPAssignmentRule.tstamp : Edm.Binary
PX.Objects.EP.EPAssignmentRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPAssignmentRule.CreatedByScreenID : Edm.String
PX.Objects.EP.EPAssignmentRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPAssignmentRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPAssignmentRule.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPAssignmentRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPAssignmentRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPAssignmentRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPAssignmentRule.EPAssignmentRouteByAssignmentRouteID -> PX.Objects.EP.EPAssignmentRoute (AssignmentRouteID=AssignmentRouteID)

# PX.Objects.EP.EPAttendee (EntityType)

Label: "Attendee"
Key: AttendeeID, EventNoteID
Entity sets: PX_Objects_EP_EPAttendee, Attendee, EPAttendee

PX.Objects.EP.EPAttendee.EventNoteID : Edm.Guid [key]
PX.Objects.EP.EPAttendee.AttendeeID : Edm.Guid [key]
PX.Objects.EP.EPAttendee.Email : Edm.String "Email"
PX.Objects.EP.EPAttendee.Comment : Edm.String "Comment"
PX.Objects.EP.EPAttendee.ContactID : Edm.Int32 "Contact"
PX.Objects.EP.EPAttendee.Invitation : Edm.Int32 [required] "Invitation"
PX.Objects.EP.EPAttendee.IsOptional : Edm.Boolean [required] "Optional"
PX.Objects.EP.EPAttendee.IsOwner : Edm.Boolean [required] "Is Owner"
PX.Objects.EP.EPAttendee.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPAttendee.CreatedByScreenID : Edm.String
PX.Objects.EP.EPAttendee.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPAttendee.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPAttendee.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPAttendee.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPAttendee.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.EP.EPAttendee.CRActivityByEventNoteID -> PX.Objects.CR.CRActivity (EventNoteID=NoteID)
PX.Objects.EP.EPAttendee.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPAttendee.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.EP.EPContractRate (EntityType)

Label: "Contract Rates"
Key: RecordID
Entity sets: PX_Objects_EP_EPContractRate, ContractRates, EPContractRate

PX.Objects.EP.EPContractRate.RecordID : Edm.Int32 [key]
PX.Objects.EP.EPContractRate.EmployeeID : Edm.Int32
PX.Objects.EP.EPContractRate.EarningType : Edm.String "Earning Type"
PX.Objects.EP.EPContractRate.ContractID : Edm.Int32
PX.Objects.EP.EPContractRate.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.EP.EPContractRate.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPContractRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPContractRate.CreatedByScreenID : Edm.String
PX.Objects.EP.EPContractRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPContractRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPContractRate.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPContractRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPContractRate.tstamp : Edm.Binary
PX.Objects.EP.EPContractRate.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.EP.EPContractRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPContractRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPContractRate.EPEarningTypeByEarningType -> PX.Objects.EP.EPEarningType (EarningType=TypeCD)
PX.Objects.EP.EPContractRate.EPEmployeeContractByContractID -> PX.Objects.EP.EPEmployeeContract (EmployeeID=EmployeeID, ContractID=ContractID)

# PX.Objects.EP.EPCustomWeek (EntityType)

Label: "Custom Week"
Key: WeekID
Entity sets: PX_Objects_EP_EPCustomWeek, CustomWeek, EPCustomWeek
Non-filterable, non-selectable: FullNumber, Description, ShortDescription, EntityDescription

PX.Objects.EP.EPCustomWeek.WeekID : Edm.Int32 [key] "WeekID"
PX.Objects.EP.EPCustomWeek.FullNumber : Edm.String "Week"
PX.Objects.EP.EPCustomWeek.Year : Edm.Int32 "Year"
PX.Objects.EP.EPCustomWeek.Number : Edm.Int32 "Number"
PX.Objects.EP.EPCustomWeek.StartDate : Edm.DateTimeOffset "Start"
PX.Objects.EP.EPCustomWeek.EndDate : Edm.DateTimeOffset "End"
PX.Objects.EP.EPCustomWeek.IsFullWeek : Edm.Boolean [required] "Full Week"
PX.Objects.EP.EPCustomWeek.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPCustomWeek.Description : Edm.String "Description"
PX.Objects.EP.EPCustomWeek.ShortDescription : Edm.String "Description"
PX.Objects.EP.EPCustomWeek.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.EP.EPCustomWeek.CreatedByScreenID : Edm.String
PX.Objects.EP.EPCustomWeek.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.EP.EPCustomWeek.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPCustomWeek.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPCustomWeek.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPCustomWeek.EntityDescription : Edm.String "Entity"
PX.Objects.EP.EPCustomWeek.tstamp : Edm.Binary
PX.Objects.EP.EPCustomWeek.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPCustomWeek.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.EP.EPDepartment (EntityType)

Label: "Department"
Key: DepartmentID
Entity sets: PX_Objects_EP_EPDepartment, Department, EPDepartment

PX.Objects.EP.EPDepartment.DepartmentID : Edm.String [key] "Department ID"
PX.Objects.EP.EPDepartment.Description : Edm.String "Description"
PX.Objects.EP.EPDepartment.CreatedByScreenID : Edm.String
PX.Objects.EP.EPDepartment.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPDepartment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPDepartment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPDepartment.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPDepartment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPDepartment.tstamp : Edm.Binary
PX.Objects.EP.EPDepartment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPDepartment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPDepartment.AccountByExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.EP.EPDepartment.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.EP.EPDepartment.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.EP.EPDepartment.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.EP.EPDepartment.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.EP.EPDepartment.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)

# PX.Objects.EP.EPEarningType (EntityType)

Label: "Earning Type"
Key: TypeCD
Entity sets: PX_Objects_EP_EPEarningType, EarningType, EPEarningType

PX.Objects.EP.EPEarningType.TypeCD : Edm.String [key] "Code"
PX.Objects.EP.EPEarningType.Description : Edm.String "Description"
PX.Objects.EP.EPEarningType.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPEarningType.IsOvertime : Edm.Boolean [required] "Overtime"
PX.Objects.EP.EPEarningType.isBillable : Edm.Boolean [required] "Billable"
PX.Objects.EP.EPEarningType.OvertimeMultiplier : Edm.Decimal "Multiplier"
PX.Objects.EP.EPEarningType.tstamp : Edm.Binary
PX.Objects.EP.EPEarningType.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEarningType.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEarningType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEarningType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEarningType.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEarningType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEarningType.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.EP.EPEarningType.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.EP.EPEarningType.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.EP.EPEarningType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEarningType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEarningType.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.EP.EPEarningType.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.EP.EPEarningType.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.EP.EPEarningType.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.EP.EPEarningType.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.EP.EPEarningType.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.EP.EPEarningType.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.EP.EPEarningType.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.EP.EPEarningType.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.EP.EPEarningType.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.EP.EPEarningType.PREarningTypeDetailCollection -> Collection(PX.Objects.PR.PREarningTypeDetail)
PX.Objects.EP.EPEarningType.PRPaymentEarningCollection -> Collection(PX.Objects.PR.PRPaymentEarning)
PX.Objects.EP.EPEarningType.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.EP.EPEarningType.PRSetupCollection -> Collection(PX.Objects.PR.PRSetup)
PX.Objects.EP.EPEarningType.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.EP.EPEarningType.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.Objects.EP.EPEarningType.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.EP.EPEarningType.EPTimeLogTypeCollection -> Collection(PX.Objects.EP.ClockInClockOut.EPTimeLogType)
PX.Objects.EP.EPEarningType.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.EP.EPEarningType.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.EP.EPEarningType.PRDeductCodeEarningIncreasingWageCollection -> Collection(PX.Objects.PR.PRDeductCodeEarningIncreasingWage)
PX.Objects.EP.EPEarningType.PREmployeeEarningCollection -> Collection(PX.Objects.PR.PREmployeeEarning)
PX.Objects.EP.EPEarningType.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.Objects.EP.EPEarningType.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.EP.EPEarningType.PRPTOBankCollection -> Collection(PX.Objects.PR.PRPTOBank)
PX.Objects.EP.EPEarningType.PRPTOBankApplicableEarningTypeCollection -> Collection(PX.Objects.PR.PRPTOBankApplicableEarningType)
PX.Objects.EP.EPEarningType.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.EP.EPEarningType.PRRegularTypeForOvertimeCollection -> Collection(PX.Objects.PR.PRRegularTypeForOvertime)
PX.Objects.EP.EPEarningType.PRROEOtherMoniesCollection -> Collection(PX.Objects.PR.PRROEOtherMonies)
PX.Objects.EP.EPEarningType.PRYtdEarningsCollection -> Collection(PX.Objects.PR.PRYtdEarnings)

# PX.Objects.EP.EPEmployee (EntityType)

Label: "Employee"
BaseType: PX.Objects.AP.Vendor
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_EP_EPEmployee, Employee1, EPEmployee

PX.Objects.EP.EPEmployee.DepartmentID : Edm.String "Department"
PX.Objects.EP.EPEmployee.SupervisorID : Edm.Int32 "Reports to"
PX.Objects.EP.EPEmployee.SalesPersonID : Edm.Int32 "Salesperson"
PX.Objects.EP.EPEmployee.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.EP.EPEmployee.UserID : Edm.Guid "Employee Login"
PX.Objects.EP.EPEmployee.CalendarID : Edm.String "Calendar"
PX.Objects.EP.EPEmployee.DefaultWorkgroupID : Edm.Int32 "Default Workgroup"
PX.Objects.EP.EPEmployee.PositionLineCntr : Edm.Int32 [required]
PX.Objects.EP.EPEmployee.RouteEmails : Edm.Boolean [required] "Route Emails"
PX.Objects.EP.EPEmployee.TimeCardRequired : Edm.Boolean "Time Card Is Required"
PX.Objects.EP.EPEmployee.HoursValidation : Edm.String "Regular Hours Validation"
PX.Objects.EP.EPEmployee.ReceiptAndClaimTaxZoneID : Edm.String
PX.Objects.EP.EPEmployee.TimeCardPeriodType : Edm.String "Time Card Frequency"
PX.Objects.EP.EPEmployee.EPEmployeeBySupervisorID -> PX.Objects.EP.EPEmployee (SupervisorID=BAccountID)
PX.Objects.EP.EPEmployee.ContactByParentBAccountID -> PX.Objects.CR.Contact (DefContactID=ContactID, ParentBAccountID=BAccountID)
PX.Objects.EP.EPEmployee.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.EP.EPEmployee.AddressByParentBAccountID -> PX.Objects.CR.Address (DefAddressID=AddressID, ParentBAccountID=BAccountID)
PX.Objects.EP.EPEmployee.BranchByParentBAccountID -> PX.Objects.GL.Branch (ParentBAccountID=BAccountID)
PX.Objects.EP.EPEmployee.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.EP.EPEmployee.EPCompanyTreeByDefContactID -> PX.TM.EPCompanyTree (DefaultWorkgroupID=WorkGroupID, DefContactID=WorkGroupID)
PX.Objects.EP.EPEmployee.PMUnionByUnionID -> PX.Objects.PM.PMUnion
PX.Objects.EP.EPEmployee.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.EP.EPEmployee.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.EP.EPEmployee.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.EP.EPEmployee.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.EP.EPEmployee.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.EP.EPEmployee.EPDepartmentByDepartmentID -> PX.Objects.EP.EPDepartment (DepartmentID=DepartmentID)
PX.Objects.EP.EPEmployee.EPShiftCodeByShiftID -> PX.Objects.EP.EPShiftCode
PX.Objects.EP.EPEmployee.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.EP.EPEmployee.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)
PX.Objects.EP.EPEmployee.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.Objects.EP.EPEmployee.EPTimeLogCollection -> Collection(PX.Objects.EP.ClockInClockOut.EPTimeLog)
PX.Objects.EP.EPEmployee.TimecardWithTotalsCollection -> Collection(PX.Objects.EP.TimecardWithTotals)
PX.Objects.EP.EPEmployee.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.EP.EPEmployee.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.EP.EPEmployee.AMEstimateClassCollection -> Collection(PX.Objects.AM.AMEstimateClass)
PX.Objects.EP.EPEmployee.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.EP.EPEmployee.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.EP.EPEmployee.PMEmployeeRateCollection -> Collection(PX.Objects.PM.PMEmployeeRate)

# PX.Objects.EP.EPEmployeeClass (EntityType)

Label: "Employee Class"
BaseType: PX.Objects.AP.VendorClass
Key: VendorClassID (inherited from PX.Objects.AP.VendorClass)
Entity sets: PX_Objects_EP_EPEmployeeClass, EmployeeClass, EPEmployeeClass

PX.Objects.EP.EPEmployeeClass.CalendarID : Edm.String "Calendar"
PX.Objects.EP.EPEmployeeClass.HoursValidation : Edm.String "Regular Hours Validation"
PX.Objects.EP.EPEmployeeClass.DefaultDateInActivity : Edm.String "Default Date in Time Cards"
PX.Objects.EP.EPEmployeeClass.ProbationPeriodMonths : Edm.Int32 [required] "Probation Period (Months)"
PX.Objects.EP.EPEmployeeClass.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.EP.EPEmployeeClass.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.EP.EPEmployeeClass.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)

# PX.Objects.EP.EPEmployeeClassLaborMatrix (EntityType)

Label: "Employee Class Labor"
Key: EarningType, EmployeeID
Entity sets: PX_Objects_EP_EPEmployeeClassLaborMatrix, EmployeeClassLabor, EPEmployeeClassLaborMatrix

PX.Objects.EP.EPEmployeeClassLaborMatrix.EmployeeID : Edm.Int32 [key]
PX.Objects.EP.EPEmployeeClassLaborMatrix.EarningType : Edm.String [key] "Earning Type"
PX.Objects.EP.EPEmployeeClassLaborMatrix.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.EP.EPEmployeeClassLaborMatrix.tstamp : Edm.Binary
PX.Objects.EP.EPEmployeeClassLaborMatrix.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEmployeeClassLaborMatrix.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEmployeeClassLaborMatrix.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEmployeeClassLaborMatrix.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEmployeeClassLaborMatrix.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEmployeeClassLaborMatrix.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEmployeeClassLaborMatrix.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.EP.EPEmployeeClassLaborMatrix.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.EP.EPEmployeeClassLaborMatrix.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEmployeeClassLaborMatrix.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEmployeeClassLaborMatrix.EPEarningTypeByEarningType -> PX.Objects.EP.EPEarningType (EarningType=TypeCD)

# PX.Objects.EP.EPEmployeeContract (EntityType)

Label: "Employee Contract"
Key: ContractID, EmployeeID
Entity sets: PX_Objects_EP_EPEmployeeContract, EmployeeContract, EPEmployeeContract

PX.Objects.EP.EPEmployeeContract.EmployeeID : Edm.Int32 [key]
PX.Objects.EP.EPEmployeeContract.ContractID : Edm.Int32 [key] "Project/Contract"
PX.Objects.EP.EPEmployeeContract.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEmployeeContract.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEmployeeContract.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEmployeeContract.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEmployeeContract.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEmployeeContract.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEmployeeContract.tstamp : Edm.Binary
PX.Objects.EP.EPEmployeeContract.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.EP.EPEmployeeContract.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.EP.EPEmployeeContract.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEmployeeContract.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEmployeeContract.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)

# PX.Objects.EP.EPEmployeeEx (EntityType)

Label: "Employee"
BaseType: PX.Objects.EP.EPEmployee
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_EP_EPEmployeeEx

# PX.Objects.EP.EPEmployeePosition (EntityType)

Label: "Employee Position"
Key: EmployeeID, LineNbr
Entity sets: PX_Objects_EP_EPEmployeePosition, EmployeePosition, EPEmployeePosition
Non-filterable, non-selectable: NoteText

PX.Objects.EP.EPEmployeePosition.EmployeeID : Edm.Int32 [key]
PX.Objects.EP.EPEmployeePosition.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.EP.EPEmployeePosition.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPEmployeePosition.PositionID : Edm.String "Position"
PX.Objects.EP.EPEmployeePosition.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.EP.EPEmployeePosition.StartReason : Edm.String "Start Reason"
PX.Objects.EP.EPEmployeePosition.ProbationPeriodEndDate : Edm.DateTimeOffset "Probation Period End Date"
PX.Objects.EP.EPEmployeePosition.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.EP.EPEmployeePosition.TermReason : Edm.String "Termination Reason"
PX.Objects.EP.EPEmployeePosition.IsTerminated : Edm.Boolean [required] "Terminated"
PX.Objects.EP.EPEmployeePosition.IsRehirable : Edm.Boolean [required] "Eligible for Rehire"
PX.Objects.EP.EPEmployeePosition.NoteID : Edm.Guid
PX.Objects.EP.EPEmployeePosition.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPEmployeePosition.tstamp : Edm.Binary
PX.Objects.EP.EPEmployeePosition.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEmployeePosition.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEmployeePosition.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEmployeePosition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEmployeePosition.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEmployeePosition.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEmployeePosition.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.EP.EPEmployeePosition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEmployeePosition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEmployeePosition.EPPositionByPositionID -> PX.Objects.EP.EPPosition (PositionID=PositionID)

# PX.Objects.EP.EPEquipment (EntityType)

Label: "Equipment"
Key: EquipmentCD
Entity sets: PX_Objects_EP_EPEquipment, Equipment, EPEquipment
Non-filterable, non-selectable: ClassID, NoteText

PX.Objects.EP.EPEquipment.EquipmentID : Edm.Int32
PX.Objects.EP.EPEquipment.EquipmentCD : Edm.String [key] "Equipment ID"
PX.Objects.EP.EPEquipment.Description : Edm.String "Description"
PX.Objects.EP.EPEquipment.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPEquipment.FixedAssetID : Edm.Int32 "Fixed Asset"
PX.Objects.EP.EPEquipment.CalendarID : Edm.String "Calendar"
PX.Objects.EP.EPEquipment.RunRateItemID : Edm.Int32 "Run-Rate Item"
PX.Objects.EP.EPEquipment.SetupRateItemID : Edm.Int32 "Setup-Rate Item"
PX.Objects.EP.EPEquipment.SuspendRateItemID : Edm.Int32 "Suspend-Rate Item"
PX.Objects.EP.EPEquipment.RunRate : Edm.Decimal [required] "Run Rate"
PX.Objects.EP.EPEquipment.SetupRate : Edm.Decimal [required] "Setup Rate"
PX.Objects.EP.EPEquipment.SuspendRate : Edm.Decimal [required] "Suspend Rate"
PX.Objects.EP.EPEquipment.DefAccountGroupID : Edm.Int32 "Default Account Group"
PX.Objects.EP.EPEquipment.ClassID : Edm.String
PX.Objects.EP.EPEquipment.NoteID : Edm.Guid
PX.Objects.EP.EPEquipment.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPEquipment.tstamp : Edm.Binary
PX.Objects.EP.EPEquipment.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEquipment.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEquipment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.EP.EPEquipment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEquipment.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEquipment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipment.FixedAssetByFixedAssetID -> PX.Objects.FA.FixedAsset (FixedAssetID=AssetID)
PX.Objects.EP.EPEquipment.InventoryItemByRunRateItemID -> PX.Objects.IN.InventoryItem (RunRateItemID=InventoryID)
PX.Objects.EP.EPEquipment.InventoryItemBySetupRateItemID -> PX.Objects.IN.InventoryItem (SetupRateItemID=InventoryID)
PX.Objects.EP.EPEquipment.InventoryItemBySuspendRateItemID -> PX.Objects.IN.InventoryItem (SuspendRateItemID=InventoryID)
PX.Objects.EP.EPEquipment.PMAccountGroupByDefAccountGroupID -> PX.Objects.PM.PMAccountGroup (DefAccountGroupID=GroupID)
PX.Objects.EP.EPEquipment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEquipment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEquipment.AccountByDefaultAccountID -> PX.Objects.GL.Account
PX.Objects.EP.EPEquipment.SubByDefaultSubID -> PX.Objects.GL.Sub
PX.Objects.EP.EPEquipment.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.EP.EPEquipment.EPEquipmentTimeCardCollection -> Collection(PX.Objects.EP.EPEquipmentTimeCard)
PX.Objects.EP.EPEquipment.EquipmentProjectionCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.EquipmentProjection)
PX.Objects.EP.EPEquipment.EPEquipmentRateCollection -> Collection(PX.Objects.EP.EPEquipmentRate)

# PX.Objects.EP.EPEquipmentDetail (EntityType)

Label: "Equipment Time Card Detail"
Key: LineNbr, TimeCardCD
Entity sets: PX_Objects_EP_EPEquipmentDetail, EquipmentTimeCardDetail, EPEquipmentDetail
Non-filterable, non-selectable: NoteText

PX.Objects.EP.EPEquipmentDetail.TimeCardCD : Edm.String [key] "TimeCardCD"
PX.Objects.EP.EPEquipmentDetail.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.EP.EPEquipmentDetail.SetupSummaryLineNbr : Edm.Int32
PX.Objects.EP.EPEquipmentDetail.RunSummaryLineNbr : Edm.Int32
PX.Objects.EP.EPEquipmentDetail.SuspendSummaryLineNbr : Edm.Int32
PX.Objects.EP.EPEquipmentDetail.OrigLineNbr : Edm.Int32
PX.Objects.EP.EPEquipmentDetail.Date : Edm.DateTimeOffset "Date"
PX.Objects.EP.EPEquipmentDetail.Description : Edm.String "Description"
PX.Objects.EP.EPEquipmentDetail.ProjectID : Edm.Int32 "Project"
PX.Objects.EP.EPEquipmentDetail.RunTime : Edm.Int32 "Run Time"
PX.Objects.EP.EPEquipmentDetail.SetupTime : Edm.Int32 "Setup Time"
PX.Objects.EP.EPEquipmentDetail.SuspendTime : Edm.Int32 "Suspend Time"
PX.Objects.EP.EPEquipmentDetail.IsBillable : Edm.Boolean [required] "Billable"
PX.Objects.EP.EPEquipmentDetail.NoteID : Edm.Guid
PX.Objects.EP.EPEquipmentDetail.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPEquipmentDetail.tstamp : Edm.Binary
PX.Objects.EP.EPEquipmentDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEquipmentDetail.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEquipmentDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipmentDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEquipmentDetail.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEquipmentDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipmentDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.EP.EPEquipmentDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.EP.EPEquipmentDetail.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.EP.EPEquipmentDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.EP.EPEquipmentDetail.BranchByOffsetBranchID -> PX.Objects.GL.Branch
PX.Objects.EP.EPEquipmentDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEquipmentDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEquipmentDetail.EPEquipmentTimeCardByTimeCardCD -> PX.Objects.EP.EPEquipmentTimeCard (TimeCardCD=TimeCardCD)
PX.Objects.EP.EPEquipmentDetail.DailyFieldReportEquipmentCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment)

# PX.Objects.EP.EPEquipmentRate (EntityType)

Label: "Equipment Rate"
Key: EquipmentID, ProjectID
Entity sets: PX_Objects_EP_EPEquipmentRate, EquipmentRate, EPEquipmentRate
Non-filterable, non-selectable: NoteText

PX.Objects.EP.EPEquipmentRate.EquipmentID : Edm.Int32 [key]
PX.Objects.EP.EPEquipmentRate.ProjectID : Edm.Int32 [key] "Project"
PX.Objects.EP.EPEquipmentRate.RunRate : Edm.Decimal "Run Rate"
PX.Objects.EP.EPEquipmentRate.SetupRate : Edm.Decimal "Setup Rate"
PX.Objects.EP.EPEquipmentRate.SuspendRate : Edm.Decimal "Suspend Rate"
PX.Objects.EP.EPEquipmentRate.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPEquipmentRate.NoteID : Edm.Guid
PX.Objects.EP.EPEquipmentRate.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPEquipmentRate.tstamp : Edm.Binary
PX.Objects.EP.EPEquipmentRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEquipmentRate.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEquipmentRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipmentRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEquipmentRate.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEquipmentRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipmentRate.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.EP.EPEquipmentRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEquipmentRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEquipmentRate.EPEquipmentByEquipmentID -> PX.Objects.EP.EPEquipment (EquipmentID=EquipmentID)

# PX.Objects.EP.EPEquipmentSummary (EntityType)

Label: "Equipment Time Card Summary"
Key: LineNbr, TimeCardCD
Entity sets: PX_Objects_EP_EPEquipmentSummary, EquipmentTimeCardSummary, EPEquipmentSummary
Non-filterable, non-selectable: TimeSpent, NoteText, LabourClassCalc

PX.Objects.EP.EPEquipmentSummary.TimeCardCD : Edm.String [key] "TimeCardCD"
PX.Objects.EP.EPEquipmentSummary.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.EP.EPEquipmentSummary.RateType : Edm.String "Rate Type"
PX.Objects.EP.EPEquipmentSummary.ProjectID : Edm.Int32 "Project"
PX.Objects.EP.EPEquipmentSummary.TimeSpent : Edm.Int32 "Time Spent"
PX.Objects.EP.EPEquipmentSummary.Sun : Edm.Int32 "Sun"
PX.Objects.EP.EPEquipmentSummary.Mon : Edm.Int32 "Mon"
PX.Objects.EP.EPEquipmentSummary.Tue : Edm.Int32 "Tue"
PX.Objects.EP.EPEquipmentSummary.Wed : Edm.Int32 "Wed"
PX.Objects.EP.EPEquipmentSummary.Thu : Edm.Int32 "Thu"
PX.Objects.EP.EPEquipmentSummary.Fri : Edm.Int32 "Fri"
PX.Objects.EP.EPEquipmentSummary.Sat : Edm.Int32 "Sat"
PX.Objects.EP.EPEquipmentSummary.IsBillable : Edm.Boolean [required] "Billable"
PX.Objects.EP.EPEquipmentSummary.Description : Edm.String "Description"
PX.Objects.EP.EPEquipmentSummary.NoteID : Edm.Guid
PX.Objects.EP.EPEquipmentSummary.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPEquipmentSummary.tstamp : Edm.Binary
PX.Objects.EP.EPEquipmentSummary.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEquipmentSummary.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEquipmentSummary.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipmentSummary.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEquipmentSummary.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEquipmentSummary.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipmentSummary.LabourClassCalc : Edm.Int32 "Labor Item"
PX.Objects.EP.EPEquipmentSummary.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.EP.EPEquipmentSummary.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.EP.EPEquipmentSummary.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.EP.EPEquipmentSummary.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEquipmentSummary.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEquipmentSummary.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.EP.EPEquipmentSummary.EPEquipmentTimeCardByTimeCardCD -> PX.Objects.EP.EPEquipmentTimeCard (TimeCardCD=TimeCardCD)

# PX.Objects.EP.EPEquipmentTimeCard (EntityType)

Label: "Equipment Time Card"
Key: TimeCardCD
Entity sets: PX_Objects_EP_EPEquipmentTimeCard, EquipmentTimeCard, EPEquipmentTimeCard
Non-filterable, non-selectable: WorkgroupID, OwnerID, NoteText, WeekStartDate, WeekDescription, WeekShortDescription, TimeSetupCalc, TimeRunCalc, TimeSuspendCalc, TimeTotalCalc, TimeBillableSetupCalc, TimeBillableRunCalc, TimeBillableSuspendCalc, TimeBillableTotalCalc, TimecardType, SunTotal, MonTotal, TueTotal, WedTotal, ThuTotal, FriTotal, SatTotal, WeekTotal

PX.Objects.EP.EPEquipmentTimeCard.TimeCardCD : Edm.String [key] "Ref. Nbr."
PX.Objects.EP.EPEquipmentTimeCard.EquipmentID : Edm.Int32 "Equipment ID"
PX.Objects.EP.EPEquipmentTimeCard.Status : Edm.String "Status"
PX.Objects.EP.EPEquipmentTimeCard.OrigTimeCardCD : Edm.String "Orig. Ref. Nbr."
PX.Objects.EP.EPEquipmentTimeCard.WeekID : Edm.Int32 "Week"
PX.Objects.EP.EPEquipmentTimeCard.IsHold : Edm.Boolean [required] "IsHold"
PX.Objects.EP.EPEquipmentTimeCard.IsApproved : Edm.Boolean [required]
PX.Objects.EP.EPEquipmentTimeCard.IsRejected : Edm.Boolean [required]
PX.Objects.EP.EPEquipmentTimeCard.IsReleased : Edm.Boolean [required] "IsReleased"
PX.Objects.EP.EPEquipmentTimeCard.WorkgroupID : Edm.Int32 "Workgroup ID"
PX.Objects.EP.EPEquipmentTimeCard.OwnerID : Edm.Int32 "OwnerID"
PX.Objects.EP.EPEquipmentTimeCard.SummaryLineCntr : Edm.Int32 [required]
PX.Objects.EP.EPEquipmentTimeCard.DetailLineCntr : Edm.Int32 [required]
PX.Objects.EP.EPEquipmentTimeCard.NoteID : Edm.Guid
PX.Objects.EP.EPEquipmentTimeCard.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPEquipmentTimeCard.tstamp : Edm.Binary
PX.Objects.EP.EPEquipmentTimeCard.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEquipmentTimeCard.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEquipmentTimeCard.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipmentTimeCard.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEquipmentTimeCard.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEquipmentTimeCard.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEquipmentTimeCard.WeekStartDate : Edm.DateTimeOffset "Week Start Date"
PX.Objects.EP.EPEquipmentTimeCard.WeekDescription : Edm.String "Week"
PX.Objects.EP.EPEquipmentTimeCard.WeekShortDescription : Edm.String "Week"
PX.Objects.EP.EPEquipmentTimeCard.TimeSetupCalc : Edm.Int32 "Time Spent"
PX.Objects.EP.EPEquipmentTimeCard.TimeRunCalc : Edm.Int32 "Run"
PX.Objects.EP.EPEquipmentTimeCard.TimeSuspendCalc : Edm.Int32 "Suspend"
PX.Objects.EP.EPEquipmentTimeCard.TimeTotalCalc : Edm.Int32 "Total"
PX.Objects.EP.EPEquipmentTimeCard.TimeBillableSetupCalc : Edm.Int32 "Billable"
PX.Objects.EP.EPEquipmentTimeCard.TimeBillableRunCalc : Edm.Int32 "Billable Run"
PX.Objects.EP.EPEquipmentTimeCard.TimeBillableSuspendCalc : Edm.Int32 "Billable Suspend"
PX.Objects.EP.EPEquipmentTimeCard.TimeBillableTotalCalc : Edm.Int32 "Billable Total"
PX.Objects.EP.EPEquipmentTimeCard.TimecardType : Edm.String "Type"
PX.Objects.EP.EPEquipmentTimeCard.SunTotal : Edm.Int32
PX.Objects.EP.EPEquipmentTimeCard.MonTotal : Edm.Int32
PX.Objects.EP.EPEquipmentTimeCard.TueTotal : Edm.Int32
PX.Objects.EP.EPEquipmentTimeCard.WedTotal : Edm.Int32
PX.Objects.EP.EPEquipmentTimeCard.ThuTotal : Edm.Int32
PX.Objects.EP.EPEquipmentTimeCard.FriTotal : Edm.Int32
PX.Objects.EP.EPEquipmentTimeCard.SatTotal : Edm.Int32
PX.Objects.EP.EPEquipmentTimeCard.WeekTotal : Edm.Int32
PX.Objects.EP.EPEquipmentTimeCard.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEquipmentTimeCard.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEquipmentTimeCard.EPEquipmentByEquipmentID -> PX.Objects.EP.EPEquipment (EquipmentID=EquipmentID)
PX.Objects.EP.EPEquipmentTimeCard.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.Objects.EP.EPEquipmentTimeCard.EPEquipmentSummaryCollection -> Collection(PX.Objects.EP.EPEquipmentSummary)
PX.Objects.EP.EPEquipmentTimeCard.DailyFieldReportEquipmentCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEquipment)

# PX.Objects.EP.EPEventCategory (EntityType)

Label: "Event Category"
Key: CategoryID
Entity sets: PX_Objects_EP_EPEventCategory, EventCategory, EPEventCategory

PX.Objects.EP.EPEventCategory.CategoryID : Edm.Int32 [key]
PX.Objects.EP.EPEventCategory.Description : Edm.String "Description"
PX.Objects.EP.EPEventCategory.Style : Edm.String "Style"
PX.Objects.EP.EPEventCategory.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPEventCategory.CreatedByScreenID : Edm.String
PX.Objects.EP.EPEventCategory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEventCategory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPEventCategory.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPEventCategory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPEventCategory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPEventCategory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPEventCategory.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.EP.EPEventCategory.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.EP.EPEventCategory.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)

# PX.Objects.EP.EPExpenseClaim (EntityType)

Label: "Expense Claim"
Key: RefNbr
Entity sets: PX_Objects_EP_EPExpenseClaim, ExpenseClaim, EPExpenseClaim
Non-filterable, non-selectable: ReleasedToVerify, HasWithHoldTax, HasUseTax, NoteText, CuryLineTotal, LineTotal, OwnerID, FormCaptionDescription, CuryRate, CuryViewState

PX.Objects.EP.EPExpenseClaim.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.EP.EPExpenseClaim.EmployeeID : Edm.Int32 "Claimed By"
PX.Objects.EP.EPExpenseClaim.WorkgroupID : Edm.Int32 "Approval Workgroup"
PX.Objects.EP.EPExpenseClaim.ApproverID : Edm.Int32 "Approver"
PX.Objects.EP.EPExpenseClaim.ApprovedByID : Edm.Int32 "Approved By"
PX.Objects.EP.EPExpenseClaim.DepartmentID : Edm.String "Department ID"
PX.Objects.EP.EPExpenseClaim.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.EP.EPExpenseClaim.ApproveDate : Edm.DateTimeOffset "Approval Date"
PX.Objects.EP.EPExpenseClaim.TranPeriodID : Edm.String
PX.Objects.EP.EPExpenseClaim.FinPeriodID : Edm.String "Post to Period"
PX.Objects.EP.EPExpenseClaim.DocDesc : Edm.String "Description"
PX.Objects.EP.EPExpenseClaim.CuryID : Edm.String "Currency"
PX.Objects.EP.EPExpenseClaim.CuryInfoID : Edm.Int64
PX.Objects.EP.EPExpenseClaim.CuryDocBal : Edm.Decimal [required] "Claim Total"
PX.Objects.EP.EPExpenseClaim.DocBal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaim.Hold : Edm.Boolean [required]
PX.Objects.EP.EPExpenseClaim.Approved : Edm.Boolean [required]
PX.Objects.EP.EPExpenseClaim.Rejected : Edm.Boolean [required]
PX.Objects.EP.EPExpenseClaim.Released : Edm.Boolean [required] "Released"
PX.Objects.EP.EPExpenseClaim.ReleasedToVerify : Edm.Boolean
PX.Objects.EP.EPExpenseClaim.Status : Edm.String "Status"
PX.Objects.EP.EPExpenseClaim.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.EP.EPExpenseClaim.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.EP.EPExpenseClaim.HasWithHoldTax : Edm.Boolean
PX.Objects.EP.EPExpenseClaim.HasUseTax : Edm.Boolean
PX.Objects.EP.EPExpenseClaim.CreatedByScreenID : Edm.String
PX.Objects.EP.EPExpenseClaim.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPExpenseClaim.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPExpenseClaim.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPExpenseClaim.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPExpenseClaim.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPExpenseClaim.NoteID : Edm.Guid
PX.Objects.EP.EPExpenseClaim.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPExpenseClaim.tstamp : Edm.Binary
PX.Objects.EP.EPExpenseClaim.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.EP.EPExpenseClaim.TaxTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaim.CuryTaxRoundDiff : Edm.Decimal [required] "Tax Discrepancy"
PX.Objects.EP.EPExpenseClaim.TaxRoundDiff : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaim.CuryLineTotal : Edm.Decimal "Detail Total"
PX.Objects.EP.EPExpenseClaim.LineTotal : Edm.Decimal
PX.Objects.EP.EPExpenseClaim.CustomerID : Edm.Int32 "Customer"
PX.Objects.EP.EPExpenseClaim.CuryVatExemptTotal : Edm.Decimal [required] "VAT Exempt Total"
PX.Objects.EP.EPExpenseClaim.VatExemptTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaim.CuryVatTaxableTotal : Edm.Decimal [required] "VAT Taxable Total"
PX.Objects.EP.EPExpenseClaim.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaim.OwnerID : Edm.Int32
PX.Objects.EP.EPExpenseClaim.FormCaptionDescription : Edm.String
PX.Objects.EP.EPExpenseClaim.CuryRate : Edm.Decimal
PX.Objects.EP.EPExpenseClaim.CuryViewState : Edm.Boolean
PX.Objects.EP.EPExpenseClaim.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.EP.EPExpenseClaim.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.EP.EPExpenseClaim.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.EP.EPExpenseClaim.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.EP.EPExpenseClaim.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.EP.EPExpenseClaim.ContactByApproverID -> PX.Objects.CR.Contact (ApproverID=ContactID)
PX.Objects.EP.EPExpenseClaim.ContactByApprovedByID -> PX.Objects.CR.Contact (ApprovedByID=ContactID)
PX.Objects.EP.EPExpenseClaim.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.EP.EPExpenseClaim.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPExpenseClaim.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPExpenseClaim.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.EP.EPExpenseClaim.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.EP.EPExpenseClaim.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.EP.EPExpenseClaim.LocationByLocationID -> PX.Objects.CR.Location (EmployeeID=BAccountID)
PX.Objects.EP.EPExpenseClaim.LocationByEmployeeID -> PX.Objects.CR.Location (EmployeeID=BAccountID)
PX.Objects.EP.EPExpenseClaim.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.EP.EPExpenseClaim.EPDepartmentByDepartmentID -> PX.Objects.EP.EPDepartment (DepartmentID=DepartmentID)
PX.Objects.EP.EPExpenseClaim.EPTaxAggregateCollection -> Collection(PX.Objects.EP.EPTaxAggregate)
PX.Objects.EP.EPExpenseClaim.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)

# PX.Objects.EP.EPExpenseClaimDetails (EntityType)

Label: "Expense Receipt"
Key: ClaimDetailCD
Entity sets: PX_Objects_EP_EPExpenseClaimDetails, ExpenseReceipt, EPExpenseClaimDetails
Non-filterable, non-selectable: RefNbrNotFiltered, CuryTaxTipTotal, TaxTipTotal, HasWithHoldTax, HasUseTax, CuryNetAmount, NetAmount, StatusClaim, HoldClaim, NoteText, DailyFieldReportId, CuryRate, CuryViewState, ClaimCuryID

PX.Objects.EP.EPExpenseClaimDetails.ClaimDetailID : Edm.Int32 "Receipt Number"
PX.Objects.EP.EPExpenseClaimDetails.ClaimDetailCD : Edm.String [key] "Receipt Number"
PX.Objects.EP.EPExpenseClaimDetails.BranchID : Edm.Int32 "Branch"
PX.Objects.EP.EPExpenseClaimDetails.RefNbr : Edm.String "Expense Claim Ref. Nbr."
PX.Objects.EP.EPExpenseClaimDetails.RefNbrNotFiltered : Edm.String
PX.Objects.EP.EPExpenseClaimDetails.EmployeeID : Edm.Int32 "Claimed by"
PX.Objects.EP.EPExpenseClaimDetails.OwnerID : Edm.Int32 "Owner"
PX.Objects.EP.EPExpenseClaimDetails.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.EP.EPExpenseClaimDetails.Hold : Edm.Boolean [required] "Hold"
PX.Objects.EP.EPExpenseClaimDetails.Approved : Edm.Boolean [required]
PX.Objects.EP.EPExpenseClaimDetails.Rejected : Edm.Boolean [required]
PX.Objects.EP.EPExpenseClaimDetails.CuryInfoID : Edm.Int64
PX.Objects.EP.EPExpenseClaimDetails.CuryID : Edm.String "Currency"
PX.Objects.EP.EPExpenseClaimDetails.CardCuryInfoID : Edm.Int64
PX.Objects.EP.EPExpenseClaimDetails.CardCuryID : Edm.String "CardCuryID"
PX.Objects.EP.EPExpenseClaimDetails.ClaimCuryInfoID : Edm.Int64
PX.Objects.EP.EPExpenseClaimDetails.ExpenseDate : Edm.DateTimeOffset "Date"
PX.Objects.EP.EPExpenseClaimDetails.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.EP.EPExpenseClaimDetails.TaxTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.CuryTaxTipTotal : Edm.Decimal
PX.Objects.EP.EPExpenseClaimDetails.TaxTipTotal : Edm.Decimal
PX.Objects.EP.EPExpenseClaimDetails.CuryTaxRoundDiff : Edm.Decimal [required] "Tax Discrepancy"
PX.Objects.EP.EPExpenseClaimDetails.TaxRoundDiff : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.ExpenseRefNbr : Edm.String "Ref. Nbr."
PX.Objects.EP.EPExpenseClaimDetails.InventoryID : Edm.Int32 "Expense Item"
PX.Objects.EP.EPExpenseClaimDetails.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.EP.EPExpenseClaimDetails.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.EP.EPExpenseClaimDetails.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.EP.EPExpenseClaimDetails.HasWithHoldTax : Edm.Boolean
PX.Objects.EP.EPExpenseClaimDetails.HasUseTax : Edm.Boolean
PX.Objects.EP.EPExpenseClaimDetails.UOM : Edm.String "UOM"
PX.Objects.EP.EPExpenseClaimDetails.CuryTipAmt : Edm.Decimal [required] "Tip Amount"
PX.Objects.EP.EPExpenseClaimDetails.TipAmt : Edm.Decimal [required] "Original Tip Amount"
PX.Objects.EP.EPExpenseClaimDetails.TaxTipCategoryID : Edm.String
PX.Objects.EP.EPExpenseClaimDetails.Qty : Edm.Decimal "Quantity"
PX.Objects.EP.EPExpenseClaimDetails.CuryUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.EP.EPExpenseClaimDetails.UnitCost : Edm.Decimal
PX.Objects.EP.EPExpenseClaimDetails.CuryEmployeePart : Edm.Decimal "Employee Part"
PX.Objects.EP.EPExpenseClaimDetails.EmployeePart : Edm.Decimal "Original Employee Part"
PX.Objects.EP.EPExpenseClaimDetails.CuryExtCost : Edm.Decimal "Amount"
PX.Objects.EP.EPExpenseClaimDetails.ExtCost : Edm.Decimal "Original Total Amount"
PX.Objects.EP.EPExpenseClaimDetails.CuryTaxAmt : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.TaxAmt : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.CuryTaxableAmtFromTax : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.TaxableAmtFromTax : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.CuryTaxableAmt : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.TaxableAmt : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.CuryTranAmt : Edm.Decimal [required] "Claim Amount"
PX.Objects.EP.EPExpenseClaimDetails.CuryTranAmtWithTaxes : Edm.Decimal [required] "Claim Amount"
PX.Objects.EP.EPExpenseClaimDetails.CuryAmountWithTaxes : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.TranAmt : Edm.Decimal "Original Claim Amount"
PX.Objects.EP.EPExpenseClaimDetails.TranAmtWithTaxes : Edm.Decimal "Original Claim Amount with Taxes"
PX.Objects.EP.EPExpenseClaimDetails.ClaimCuryTranAmt : Edm.Decimal "Amount in Claim Curr."
PX.Objects.EP.EPExpenseClaimDetails.CuryNetAmount : Edm.Decimal "Net Amount"
PX.Objects.EP.EPExpenseClaimDetails.NetAmount : Edm.Decimal
PX.Objects.EP.EPExpenseClaimDetails.ClaimTranAmt : Edm.Decimal "Amount in Claim Original"
PX.Objects.EP.EPExpenseClaimDetails.ClaimCuryTranAmtWithTaxes : Edm.Decimal [required] "Amount in Claim Curr."
PX.Objects.EP.EPExpenseClaimDetails.ClaimTranAmtWithTaxes : Edm.Decimal [required] "Amount in Claim Original"
PX.Objects.EP.EPExpenseClaimDetails.ClaimCuryTaxTotal : Edm.Decimal [required] "Amount in Claim Curr."
PX.Objects.EP.EPExpenseClaimDetails.ClaimTaxTotal : Edm.Decimal [required] "Amount in Claim Original"
PX.Objects.EP.EPExpenseClaimDetails.ClaimCuryTaxRoundDiff : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.ClaimTaxRoundDiff : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.ClaimCuryVatExemptTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.ClaimVatExemptTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.ClaimCuryVatTaxableTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.ClaimVatTaxableTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.CuryVatExemptTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.VatExemptTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.CuryVatTaxableTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.EP.EPExpenseClaimDetails.TranDesc : Edm.String "Description"
PX.Objects.EP.EPExpenseClaimDetails.CustomerID : Edm.Int32 "Customer"
PX.Objects.EP.EPExpenseClaimDetails.ContractID : Edm.Int32 "Project/Contract"
PX.Objects.EP.EPExpenseClaimDetails.Billable : Edm.Boolean [required] "Billable"
PX.Objects.EP.EPExpenseClaimDetails.Billed : Edm.Boolean [required] "Billed"
PX.Objects.EP.EPExpenseClaimDetails.Released : Edm.Boolean [required] "Released"
PX.Objects.EP.EPExpenseClaimDetails.ARDocType : Edm.String "AR Doument Type"
PX.Objects.EP.EPExpenseClaimDetails.ARRefNbr : Edm.String "AR Reference Nbr."
PX.Objects.EP.EPExpenseClaimDetails.APDocType : Edm.String "AP Document Type"
PX.Objects.EP.EPExpenseClaimDetails.APRefNbr : Edm.String "AP Reference Nbr."
PX.Objects.EP.EPExpenseClaimDetails.APLineNbr : Edm.Int32 "AP Document Line Nbr."
PX.Objects.EP.EPExpenseClaimDetails.Status : Edm.String "Status"
PX.Objects.EP.EPExpenseClaimDetails.StatusClaim : Edm.String "Expense Claim Status"
PX.Objects.EP.EPExpenseClaimDetails.HoldClaim : Edm.Boolean "HoldClaim"
PX.Objects.EP.EPExpenseClaimDetails.CreatedFromClaim : Edm.Boolean [required] "Created from Claim"
PX.Objects.EP.EPExpenseClaimDetails.SubmitedDate : Edm.DateTimeOffset
PX.Objects.EP.EPExpenseClaimDetails.LegacyReceipt : Edm.Boolean [required]
PX.Objects.EP.EPExpenseClaimDetails.CorpCardID : Edm.Int32 "Corporate Card"
PX.Objects.EP.EPExpenseClaimDetails.PaidWith : Edm.String "Paid With"
PX.Objects.EP.EPExpenseClaimDetails.BankTranDate : Edm.DateTimeOffset
PX.Objects.EP.EPExpenseClaimDetails.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPExpenseClaimDetails.CreatedByScreenID : Edm.String
PX.Objects.EP.EPExpenseClaimDetails.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPExpenseClaimDetails.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPExpenseClaimDetails.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPExpenseClaimDetails.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPExpenseClaimDetails.NoteID : Edm.Guid
PX.Objects.EP.EPExpenseClaimDetails.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPExpenseClaimDetails.tstamp : Edm.Binary
PX.Objects.EP.EPExpenseClaimDetails.DailyFieldReportId : Edm.Int32 "DailyFieldReportId"
PX.Objects.EP.EPExpenseClaimDetails.CuryRate : Edm.Decimal
PX.Objects.EP.EPExpenseClaimDetails.CuryViewState : Edm.Boolean
PX.Objects.EP.EPExpenseClaimDetails.ClaimCuryID : Edm.String "Claim Currency"
PX.Objects.EP.EPExpenseClaimDetails.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.EP.EPExpenseClaimDetails.PMProjectByContractID -> PX.Objects.PM.PMProject (ContractID=ContractID)
PX.Objects.EP.EPExpenseClaimDetails.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.EP.EPExpenseClaimDetails.APInvoiceByAPRefNbr -> PX.Objects.AP.APInvoice (APDocType=DocType, APRefNbr=RefNbr)
PX.Objects.EP.EPExpenseClaimDetails.APInvoiceByAPDocType -> PX.Objects.AP.APInvoice (APRefNbr=RefNbr, APDocType=DocType)
PX.Objects.EP.EPExpenseClaimDetails.ARInvoiceByARRefNbr -> PX.Objects.AR.ARInvoice (ARDocType=DocType, ARRefNbr=RefNbr)
PX.Objects.EP.EPExpenseClaimDetails.ARInvoiceByARDocType -> PX.Objects.AR.ARInvoice (ARRefNbr=RefNbr, ARDocType=DocType)
PX.Objects.EP.EPExpenseClaimDetails.PMTaskByTaskID -> PX.Objects.PM.PMTask (ContractID=ProjectID)
PX.Objects.EP.EPExpenseClaimDetails.PMTaskByContractID -> PX.Objects.PM.PMTask (ContractID=ProjectID)
PX.Objects.EP.EPExpenseClaimDetails.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.EP.EPExpenseClaimDetails.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.EP.EPExpenseClaimDetails.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.EP.EPExpenseClaimDetails.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.EP.EPExpenseClaimDetails.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.EP.EPExpenseClaimDetails.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.EP.EPExpenseClaimDetails.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.EP.EPExpenseClaimDetails.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPExpenseClaimDetails.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPExpenseClaimDetails.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.EP.EPExpenseClaimDetails.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.EP.EPExpenseClaimDetails.TaxCategoryByTaxTipCategoryID -> PX.Objects.TX.TaxCategory (TaxTipCategoryID=TaxCategoryID)
PX.Objects.EP.EPExpenseClaimDetails.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.EP.EPExpenseClaimDetails.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.EP.EPExpenseClaimDetails.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.EP.EPExpenseClaimDetails.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.EP.EPExpenseClaimDetails.AccountByExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.EP.EPExpenseClaimDetails.AccountBySalesAccountID -> PX.Objects.GL.Account
PX.Objects.EP.EPExpenseClaimDetails.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.EP.EPExpenseClaimDetails.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.EP.EPExpenseClaimDetails.CACorpCardByCorpCardID -> PX.Objects.CA.CACorpCard (CorpCardID=CorpCardID)
PX.Objects.EP.EPExpenseClaimDetails.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.EP.EPExpenseClaimDetails.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.EP.EPExpenseClaimDetails.EPExpenseClaimByRefNbr -> PX.Objects.EP.EPExpenseClaim (RefNbr=RefNbr)
PX.Objects.EP.EPExpenseClaimDetails.APTranByAPLineNbr -> PX.Objects.AP.APTran (APDocType=TranType, APRefNbr=RefNbr, APLineNbr=LineNbr)
PX.Objects.EP.EPExpenseClaimDetails.EPTaxCollection -> Collection(PX.Objects.EP.EPTax)
PX.Objects.EP.EPExpenseClaimDetails.EPTaxTranCollection -> Collection(PX.Objects.EP.EPTaxTran)
PX.Objects.EP.EPExpenseClaimDetails.DailyFieldReportEmployeeExpenseCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportEmployeeExpense)

# PX.Objects.EP.EPPosition (EntityType)

Label: "Position"
Key: PositionID
Entity sets: PX_Objects_EP_EPPosition, Position, EPPosition

PX.Objects.EP.EPPosition.PositionID : Edm.String [key] "Position ID"
PX.Objects.EP.EPPosition.Description : Edm.String "Description"
PX.Objects.EP.EPPosition.CreatedByScreenID : Edm.String
PX.Objects.EP.EPPosition.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPPosition.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPPosition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPPosition.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPPosition.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPPosition.tstamp : Edm.Binary
PX.Objects.EP.EPPosition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPPosition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPPosition.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.EP.EPPosition.FSAppointmentStaffMemberCollection -> Collection(PX.Objects.FS.FSAppointmentStaffMember)
PX.Objects.EP.EPPosition.SVWorkTaskLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskLabor)
PX.Objects.EP.EPPosition.EPEmployeePositionCollection -> Collection(PX.Objects.EP.EPEmployeePosition)
PX.Objects.EP.EPPosition.SVWorkTaskTemplateLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskTemplateLabor)

# PX.Objects.EP.EPRule (EntityType)

Label: "Assignment/Approval Rule"
Key: RuleID
Entity sets: PX_Objects_EP_EPRule, AssignmentApprovalRule, EPRule
Non-filterable, non-selectable: NoteText, StepName, Icon

PX.Objects.EP.EPRule.RuleID : Edm.Guid [key] "Rule ID"
PX.Objects.EP.EPRule.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPRule.AssignmentMapID : Edm.Int32
PX.Objects.EP.EPRule.StepID : Edm.Guid "Step ID"
PX.Objects.EP.EPRule.Sequence : Edm.Int32 [required] "Seq."
PX.Objects.EP.EPRule.Name : Edm.String "Description"
PX.Objects.EP.EPRule.StepName : Edm.String "Step"
PX.Objects.EP.EPRule.Icon : Edm.String
PX.Objects.EP.EPRule.RuleType : Edm.String "Approver"
PX.Objects.EP.EPRule.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPRule.ApproveType : Edm.String "On Approval"
PX.Objects.EP.EPRule.EmptyStepType : Edm.String "If No Approver Found"
PX.Objects.EP.EPRule.ExecuteStep : Edm.String "Execute Step"
PX.Objects.EP.EPRule.ReasonForApprove : Edm.String "Reason for Approval"
PX.Objects.EP.EPRule.ReasonForReject : Edm.String "Reason for Rejection"
PX.Objects.EP.EPRule.WaitTime : Edm.Int32 "Decision Wait Time"
PX.Objects.EP.EPRule.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.EP.EPRule.OwnerID : Edm.Int32 "Employee"
PX.Objects.EP.EPRule.OwnerSource : Edm.String "Employee"
PX.Objects.EP.EPRule.AllowReassignment : Edm.Boolean [required] "Allow Reassignment of Approvals"
PX.Objects.EP.EPRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPRule.CreatedByScreenID : Edm.String
PX.Objects.EP.EPRule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPRule.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPRule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPRule.tstamp : Edm.Binary
PX.Objects.EP.EPRule.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.EP.EPRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPRule.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.EP.EPRule.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)
PX.Objects.EP.EPRule.EPRuleConditionCollection -> Collection(PX.Objects.EP.EPRuleCondition)
PX.Objects.EP.EPRule.EPRuleEmployeeConditionCollection -> Collection(PX.Objects.EP.EPRuleEmployeeCondition)
PX.Objects.EP.EPRule.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.Objects.EP.EPRule.EPRuleApproverCollection -> Collection(PX.Objects.EP.DAC.EPRuleApprover)

# PX.Objects.EP.EPRuleCondition (EntityType)

Label: "Assignment/Approval Rule Condition"
Key: RowNbr, RuleID
Entity sets: PX_Objects_EP_EPRuleCondition, AssignmentApprovalRuleCondition, EPRuleCondition
Non-filterable, non-selectable: IsField, UiNoteID

PX.Objects.EP.EPRuleCondition.RuleID : Edm.Guid [key] "Rule ID"
PX.Objects.EP.EPRuleCondition.RowNbr : Edm.Int16 [key]
PX.Objects.EP.EPRuleCondition.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.Objects.EP.EPRuleCondition.Entity : Edm.String "Entity"
PX.Objects.EP.EPRuleCondition.FieldName : Edm.String "Field Name"
PX.Objects.EP.EPRuleCondition.Condition : Edm.Int32 [required] "Condition"
PX.Objects.EP.EPRuleCondition.IsRelative : Edm.Boolean [required] "Is Relative"
PX.Objects.EP.EPRuleCondition.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPRuleCondition.IsField : Edm.Boolean "From Doc."
PX.Objects.EP.EPRuleCondition.Value : Edm.String "Value"
PX.Objects.EP.EPRuleCondition.Value2 : Edm.String "Value 2"
PX.Objects.EP.EPRuleCondition.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.Objects.EP.EPRuleCondition.Operator : Edm.Int32 [required] "Operator"
PX.Objects.EP.EPRuleCondition.UiNoteID : Edm.Guid "UI NoteID"
PX.Objects.EP.EPRuleCondition.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPRuleCondition.CreatedByScreenID : Edm.String
PX.Objects.EP.EPRuleCondition.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPRuleCondition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPRuleCondition.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPRuleCondition.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPRuleCondition.tstamp : Edm.Binary
PX.Objects.EP.EPRuleCondition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPRuleCondition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPRuleCondition.EPRuleByRuleID -> PX.Objects.EP.EPRule (RuleID=RuleID)

# PX.Objects.EP.EPRuleEmployeeCondition (EntityType)

Label: "Assignment/Approval Rule Employee Condition"
Key: RowNbr, RuleID
Entity sets: PX_Objects_EP_EPRuleEmployeeCondition, AssignmentApprovalRuleEmployeeCondition, EPRuleEmployeeCondition
Non-filterable, non-selectable: UiNoteID

PX.Objects.EP.EPRuleEmployeeCondition.RuleID : Edm.Guid [key] "Rule ID"
PX.Objects.EP.EPRuleEmployeeCondition.RowNbr : Edm.Int16 [key]
PX.Objects.EP.EPRuleEmployeeCondition.OpenBrackets : Edm.Int32 [required] "Brackets"
PX.Objects.EP.EPRuleEmployeeCondition.Entity : Edm.String "Entity"
PX.Objects.EP.EPRuleEmployeeCondition.FieldName : Edm.String "Field Name"
PX.Objects.EP.EPRuleEmployeeCondition.Condition : Edm.Int32 [required] "Condition"
PX.Objects.EP.EPRuleEmployeeCondition.IsRelative : Edm.Boolean [required] "Is Relative"
PX.Objects.EP.EPRuleEmployeeCondition.IsField : Edm.Boolean [required] "From Doc."
PX.Objects.EP.EPRuleEmployeeCondition.Value : Edm.String "Value"
PX.Objects.EP.EPRuleEmployeeCondition.Value2 : Edm.String "Value 2"
PX.Objects.EP.EPRuleEmployeeCondition.CloseBrackets : Edm.Int32 [required] "Brackets"
PX.Objects.EP.EPRuleEmployeeCondition.Operator : Edm.Int32 [required] "Operator"
PX.Objects.EP.EPRuleEmployeeCondition.UiNoteID : Edm.Guid "UI NoteID"
PX.Objects.EP.EPRuleEmployeeCondition.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPRuleEmployeeCondition.CreatedByScreenID : Edm.String
PX.Objects.EP.EPRuleEmployeeCondition.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPRuleEmployeeCondition.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPRuleEmployeeCondition.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPRuleEmployeeCondition.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPRuleEmployeeCondition.tstamp : Edm.Binary
PX.Objects.EP.EPRuleEmployeeCondition.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPRuleEmployeeCondition.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPRuleEmployeeCondition.EPRuleByRuleID -> PX.Objects.EP.EPRule (RuleID=RuleID)

# PX.Objects.EP.EPRuleTree (EntityType)

Label: "Assignment/Approval Rule"
BaseType: PX.Objects.EP.EPRule
Key: RuleID (inherited from PX.Objects.EP.EPRule)
Entity sets: PX_Objects_EP_EPRuleTree

# PX.Objects.EP.EPSetup (EntityType)

Label: "Time & Expenses Preferences"
Singletons: PX_Objects_EP_EPSetup, TimeExpensesPreferences, EPSetup

PX.Objects.EP.EPSetup.ClaimNumberingID : Edm.String "Expense Claim Numbering Sequence"
PX.Objects.EP.EPSetup.ReceiptNumberingID : Edm.String "Expense Receipt Numbering Sequence"
PX.Objects.EP.EPSetup.PerRetainTran : Edm.Int16 [required] "Keep Transactions for"
PX.Objects.EP.EPSetup.PerRetainHist : Edm.Int16 [required] "Periods to Retain History"
PX.Objects.EP.EPSetup.HoldEntry : Edm.Boolean [required] "Hold Expense Claims on Entry"
PX.Objects.EP.EPSetup.PostSummarizedCorpCardExpenseReceipts : Edm.Boolean [required] "Post Summarized Company Expenses by Corporate Cards"
PX.Objects.EP.EPSetup.RequireRefNbrInExpenseReceipts : Edm.Boolean [required] "Require Ref. Nbr. in Expense Receipts"
PX.Objects.EP.EPSetup.CopyNotesAR : Edm.Boolean [required] "Copy Notes to AR Documents"
PX.Objects.EP.EPSetup.CopyFilesAR : Edm.Boolean [required] "Copy Files to AR Documents"
PX.Objects.EP.EPSetup.CopyNotesAP : Edm.Boolean [required] "Copy Notes to AP Documents"
PX.Objects.EP.EPSetup.CopyFilesAP : Edm.Boolean [required] "Copy Files to AP Documents"
PX.Objects.EP.EPSetup.CopyNotesPM : Edm.Boolean [required] "Copy Notes to PM Documents"
PX.Objects.EP.EPSetup.CopyFilesPM : Edm.Boolean [required] "Copy Files to PM Documents"
PX.Objects.EP.EPSetup.AutomaticReleaseAP : Edm.Boolean [required] "Automatically Release AP Documents"
PX.Objects.EP.EPSetup.AutomaticReleaseAR : Edm.Boolean [required] "Automatically Release AR Documents"
PX.Objects.EP.EPSetup.AutomaticReleasePM : Edm.Boolean [required] "Automatically Release PM Documents"
PX.Objects.EP.EPSetup.ClaimAssignmentMapID : Edm.Int32 "Expense Claim Approval Map"
PX.Objects.EP.EPSetup.ClaimAssignmentNotificationID : Edm.Int32 "Expense Claim Notification"
PX.Objects.EP.EPSetup.NonTaxableTipItem : Edm.Int32 "Non-Taxable Tip Item"
PX.Objects.EP.EPSetup.UseReceiptAccountForTips : Edm.Boolean [required] "Use Receipt Accounts for Tips"
PX.Objects.EP.EPSetup.AllowMixedTaxSettingInClaims : Edm.Boolean [required] "Allow Mixed Tax Settings in Claims"
PX.Objects.EP.EPSetup.ValidateAttachmentsInReceipts : Edm.Boolean [required] "Validate Attachments in Receipts"
PX.Objects.EP.EPSetup.SendOnlyEventCard : Edm.Boolean [required] "Only iCalendar Card"
PX.Objects.EP.EPSetup.IsSimpleNotification : Edm.Boolean [required] "Simple Notification"
PX.Objects.EP.EPSetup.AddContactInformation : Edm.Boolean [required] "Add Contact Information"
PX.Objects.EP.EPSetup.InvitationTemplateID : Edm.Int32 "Invitation Template"
PX.Objects.EP.EPSetup.RescheduleTemplateID : Edm.Int32 "Reschedule Template"
PX.Objects.EP.EPSetup.CancelInvitationTemplateID : Edm.Int32 "Cancel Invitation Template"
PX.Objects.EP.EPSetup.SearchOnlyInWorkingTime : Edm.Boolean [required] "Search Only In Working Time"
PX.Objects.EP.EPSetup.RequireTimes : Edm.Boolean [required] "Require Time On Activity"
PX.Objects.EP.EPSetup.TimeCardNumberingID : Edm.String "Time Card Numbering Sequence"
PX.Objects.EP.EPSetup.TimeCardAssignmentMapID : Edm.Int32 "Time Card Approval Map"
PX.Objects.EP.EPSetup.TimeCardAssignmentNotificationID : Edm.Int32 "Time Card Notification"
PX.Objects.EP.EPSetup.ActivityTimeUnit : Edm.String "Activity Time Unit"
PX.Objects.EP.EPSetup.EmployeeRateUnit : Edm.String "Employee Hour Rate Unit"
PX.Objects.EP.EPSetup.GroupTransactgion : Edm.String "Group Transaction by"
PX.Objects.EP.EPSetup.DefaultActivityType : Edm.String "Default Time Activity Type"
PX.Objects.EP.EPSetup.MinBillableTime : Edm.Int32 [required] "Min Billable Time"
PX.Objects.EP.EPSetup.RegularHoursType : Edm.String "Regular Hours Earning Type"
PX.Objects.EP.EPSetup.HolidaysType : Edm.String "Holiday Earning Type"
PX.Objects.EP.EPSetup.VacationsType : Edm.String "Vacations Earning Type"
PX.Objects.EP.EPSetup.isPreloadHolidays : Edm.Boolean [required] "Preload Holidays on Time Card Entry"
PX.Objects.EP.EPSetup.DefTasksFilterID : Edm.Int64 "Default Task Filter"
PX.Objects.EP.EPSetup.DefEventsFilterID : Edm.Int64 "Default Event Filter"
PX.Objects.EP.EPSetup.PostingOption : Edm.String "Project Time"
PX.Objects.EP.EPSetup.OffBalanceAccountGroupID : Edm.Int32 "Off-Balance Account Group"
PX.Objects.EP.EPSetup.CustomWeek : Edm.Boolean [required] "Custom Week Configuration"
PX.Objects.EP.EPSetup.FirstCustomWeekID : Edm.Int32 "First Custom Week ID"
PX.Objects.EP.EPSetup.LastCustomWeekID : Edm.Int32 "Last Custom Week ID"
PX.Objects.EP.EPSetup.FirstDayOfWeek : Edm.Int32 "First Day of Week"
PX.Objects.EP.EPSetup.TimeCardPeriodType : Edm.String "Default Frequency"
PX.Objects.EP.EPSetup.FirstDayOfBiweeklyPeriod : Edm.Int32 [required] "Biweekly Period Start Day"
PX.Objects.EP.EPSetup.SemiMonthlyStartDay : Edm.Int32 [required] "Start Day of 1st Semimonthly Period"
PX.Objects.EP.EPSetup.SemiMonthlyCutOffDay : Edm.Int32 [required] "Start Day of 2nd Semimonthly Period"
PX.Objects.EP.EPSetup.MonthlyStartDay : Edm.Int32 [required] "Start Day of Monthly Period"
PX.Objects.EP.EPSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPSetup.CreatedByScreenID : Edm.String
PX.Objects.EP.EPSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPSetup.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPSetup.tstamp : Edm.Binary
PX.Objects.EP.EPSetup.ClaimDetailsAssignmentMapID : Edm.Int32 "Expense Receipt Approval Map"
PX.Objects.EP.EPSetup.ClaimDetailsAssignmentNotificationID : Edm.Int32 "Expense Receipt Notification"
PX.Objects.EP.EPSetup.AssignmentMapID : Edm.Int32
PX.Objects.EP.EPSetup.AssignmentNotificationID : Edm.Int32
PX.Objects.EP.EPSetup.IsActive : Edm.Boolean
PX.Objects.EP.EPSetup.InventoryItemByNonTaxableTipItem -> PX.Objects.IN.InventoryItem (NonTaxableTipItem=InventoryID)
PX.Objects.EP.EPSetup.PMAccountGroupByOffBalanceAccountGroupID -> PX.Objects.PM.PMAccountGroup (OffBalanceAccountGroupID=GroupID)
PX.Objects.EP.EPSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPSetup.NotificationByClaimAssignmentNotificationID -> PX.SM.Notification (ClaimAssignmentNotificationID=NotificationID)
PX.Objects.EP.EPSetup.NotificationByInvitationTemplateID -> PX.SM.Notification (InvitationTemplateID=NotificationID)
PX.Objects.EP.EPSetup.NotificationByRescheduleTemplateID -> PX.SM.Notification (RescheduleTemplateID=NotificationID)
PX.Objects.EP.EPSetup.NotificationByCancelInvitationTemplateID -> PX.SM.Notification (CancelInvitationTemplateID=NotificationID)
PX.Objects.EP.EPSetup.NotificationByTimeCardAssignmentNotificationID -> PX.SM.Notification (TimeCardAssignmentNotificationID=NotificationID)
PX.Objects.EP.EPSetup.NotificationByEquipmentTimeCardAssignmentNotificationID -> PX.SM.Notification
PX.Objects.EP.EPSetup.NotificationByClaimDetailsAssignmentNotificationID -> PX.SM.Notification (ClaimDetailsAssignmentNotificationID=NotificationID)
PX.Objects.EP.EPSetup.NumberingByClaimNumberingID -> PX.Objects.CS.Numbering (ClaimNumberingID=NumberingID)
PX.Objects.EP.EPSetup.NumberingByReceiptNumberingID -> PX.Objects.CS.Numbering (ReceiptNumberingID=NumberingID)
PX.Objects.EP.EPSetup.NumberingByTimeCardNumberingID -> PX.Objects.CS.Numbering (TimeCardNumberingID=NumberingID)
PX.Objects.EP.EPSetup.NumberingByEquipmentTimeCardNumberingID -> PX.Objects.CS.Numbering
PX.Objects.EP.EPSetup.INUnitByActivityTimeUnit -> PX.Objects.IN.INUnit (ActivityTimeUnit=FromUnit)
PX.Objects.EP.EPSetup.INUnitByEmployeeRateUnit -> PX.Objects.IN.INUnit (EmployeeRateUnit=FromUnit)
PX.Objects.EP.EPSetup.EPAssignmentMapByClaimAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (ClaimAssignmentMapID=AssignmentMapID)
PX.Objects.EP.EPSetup.EPAssignmentMapByTimeCardAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (TimeCardAssignmentMapID=AssignmentMapID)
PX.Objects.EP.EPSetup.EPAssignmentMapByEquipmentTimeCardAssignmentMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.EP.EPSetup.EPAssignmentMapByClaimDetailsAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (ClaimDetailsAssignmentMapID=AssignmentMapID)
PX.Objects.EP.EPSetup.EPEarningTypeByRegularHoursType -> PX.Objects.EP.EPEarningType (RegularHoursType=TypeCD)
PX.Objects.EP.EPSetup.EPEarningTypeByHolidaysType -> PX.Objects.EP.EPEarningType (HolidaysType=TypeCD)
PX.Objects.EP.EPSetup.EPEarningTypeByVacationsType -> PX.Objects.EP.EPEarningType (VacationsType=TypeCD)
PX.Objects.EP.EPSetup.EPActivityTypeByDefaultActivityType -> PX.Objects.EP.EPActivityType (DefaultActivityType=Type)
PX.Objects.EP.EPSetup.FilterHeaderByDefTasksFilterID -> PX.Data.FilterHeader (DefTasksFilterID=FilterID)
PX.Objects.EP.EPSetup.FilterHeaderByDefEventsFilterID -> PX.Data.FilterHeader (DefEventsFilterID=FilterID)

# PX.Objects.EP.EPShiftCode (EntityType)

Label: "Shift Code"
Key: ShiftCD
Entity sets: PX_Objects_EP_EPShiftCode, ShiftCode, EPShiftCode
Non-filterable, non-selectable: NoteText

PX.Objects.EP.EPShiftCode.ShiftID : Edm.Int32
PX.Objects.EP.EPShiftCode.ShiftCD : Edm.String [key] "Code"
PX.Objects.EP.EPShiftCode.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPShiftCode.Description : Edm.String "Description"
PX.Objects.EP.EPShiftCode.IsManufacturingShift : Edm.Boolean [required]
PX.Objects.EP.EPShiftCode.NoteID : Edm.Guid
PX.Objects.EP.EPShiftCode.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPShiftCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPShiftCode.CreatedByScreenID : Edm.String
PX.Objects.EP.EPShiftCode.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPShiftCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPShiftCode.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPShiftCode.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPShiftCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPShiftCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPShiftCode.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.EP.EPShiftCode.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.EP.EPShiftCode.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.EP.EPShiftCode.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.EP.EPShiftCode.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.EP.EPShiftCode.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.EP.EPShiftCode.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.EP.EPShiftCode.AMWCSchdCollection -> Collection(PX.Objects.AM.AMWCSchd)
PX.Objects.EP.EPShiftCode.AMWCSchdDetailCollection -> Collection(PX.Objects.AM.AMWCSchdDetail)
PX.Objects.EP.EPShiftCode.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.EP.EPShiftCode.EPShiftCodeRateCollection -> Collection(PX.Objects.EP.EPShiftCodeRate)
PX.Objects.EP.EPShiftCode.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.EP.EPShiftCode.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.EP.EPShiftCode.AMShiftCollection -> Collection(PX.Objects.AM.AMShift)
PX.Objects.EP.EPShiftCode.SchedulerWCOperationCollection -> Collection(PX.Objects.AM.SchedulerWCOperation)

# PX.Objects.EP.EPShiftCodeRate (EntityType)

Label: "Shift Code Rate"
Key: CuryID, EffectiveDate, ShiftID
Entity sets: PX_Objects_EP_EPShiftCodeRate, ShiftCodeRate, EPShiftCodeRate

PX.Objects.EP.EPShiftCodeRate.ShiftID : Edm.Int32 [key]
PX.Objects.EP.EPShiftCodeRate.EffectiveDate : Edm.DateTimeOffset [key] "Effective Date"
PX.Objects.EP.EPShiftCodeRate.CuryID : Edm.String [key] "Currency"
PX.Objects.EP.EPShiftCodeRate.Type : Edm.String "Type"
PX.Objects.EP.EPShiftCodeRate.Percent : Edm.Decimal "Percent"
PX.Objects.EP.EPShiftCodeRate.WageAmount : Edm.Decimal "Wage Amount"
PX.Objects.EP.EPShiftCodeRate.CostingAmount : Edm.Decimal "Costing Amount"
PX.Objects.EP.EPShiftCodeRate.BurdenAmount : Edm.Decimal "Burden Amount"
PX.Objects.EP.EPShiftCodeRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPShiftCodeRate.CreatedByScreenID : Edm.String
PX.Objects.EP.EPShiftCodeRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPShiftCodeRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPShiftCodeRate.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPShiftCodeRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPShiftCodeRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPShiftCodeRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPShiftCodeRate.EPShiftCodeByShiftID -> PX.Objects.EP.EPShiftCode (ShiftID=ShiftID)

# PX.Objects.EP.EPTax (EntityType)

Label: "EP Tax Detail"
Key: ClaimDetailID, IsTipTax, TaxID
Entity sets: PX_Objects_EP_EPTax, EPTaxDetail, EPTax
Non-filterable, non-selectable: NonDeductibleTaxRate, CuryID, CuryRate, CuryViewState

PX.Objects.EP.EPTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.EP.EPTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.EP.EPTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.EP.EPTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPTax.CreatedByScreenID : Edm.String
PX.Objects.EP.EPTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPTax.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTax.ClaimDetailID : Edm.Int32 [key] "Line Nbr."
PX.Objects.EP.EPTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.EP.EPTax.IsTipTax : Edm.Boolean [key required]
PX.Objects.EP.EPTax.CuryInfoID : Edm.Int64
PX.Objects.EP.EPTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.EP.EPTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.EP.EPTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.EP.EPTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.EP.EPTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.EP.EPTax.tstamp : Edm.Binary
PX.Objects.EP.EPTax.CuryID : Edm.String "Currency"
PX.Objects.EP.EPTax.CuryRate : Edm.Decimal
PX.Objects.EP.EPTax.CuryViewState : Edm.Boolean
PX.Objects.EP.EPTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.EP.EPTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.EP.EPTax.EPExpenseClaimDetailsByClaimDetailID -> PX.Objects.EP.EPExpenseClaimDetails (ClaimDetailID=ClaimDetailID)

# PX.Objects.EP.EPTaxAggregate (EntityType)

Key: RefNbr, TaxID
Entity sets: PX_Objects_EP_EPTaxAggregate
Non-filterable, non-selectable: NonDeductibleTaxRate

PX.Objects.EP.EPTaxAggregate.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPTaxAggregate.CreatedByScreenID : Edm.String
PX.Objects.EP.EPTaxAggregate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTaxAggregate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPTaxAggregate.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPTaxAggregate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTaxAggregate.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.EP.EPTaxAggregate.TaxID : Edm.String [key] "Tax ID"
PX.Objects.EP.EPTaxAggregate.CuryInfoID : Edm.Int64
PX.Objects.EP.EPTaxAggregate.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.EP.EPTaxAggregate.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.EP.EPTaxAggregate.TaxableAmt : Edm.Decimal
PX.Objects.EP.EPTaxAggregate.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.EP.EPTaxAggregate.TaxAmt : Edm.Decimal
PX.Objects.EP.EPTaxAggregate.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.EP.EPTaxAggregate.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.EP.EPTaxAggregate.ExpenseAmt : Edm.Decimal
PX.Objects.EP.EPTaxAggregate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPTaxAggregate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPTaxAggregate.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.EP.EPTaxAggregate.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.EP.EPTaxAggregate.EPExpenseClaimByRefNbr -> PX.Objects.EP.EPExpenseClaim (RefNbr=RefNbr)

# PX.Objects.EP.EPTaxTran (EntityType)

Key: ClaimDetailID, IsTipTax, TaxID
Entity sets: PX_Objects_EP_EPTaxTran
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.EP.EPTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.EP.EPTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPTaxTran.CreatedByScreenID : Edm.String
PX.Objects.EP.EPTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTaxTran.ClaimDetailID : Edm.Int32 [key]
PX.Objects.EP.EPTaxTran.RefNbr : Edm.String
PX.Objects.EP.EPTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.EP.EPTaxTran.IsTipTax : Edm.Boolean [key required]
PX.Objects.EP.EPTaxTran.CuryInfoID : Edm.Int64
PX.Objects.EP.EPTaxTran.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.EP.EPTaxTran.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.EP.EPTaxTran.TaxableAmt : Edm.Decimal
PX.Objects.EP.EPTaxTran.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.EP.EPTaxTran.TaxAmt : Edm.Decimal
PX.Objects.EP.EPTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.EP.EPTaxTran.ExpenseAmt : Edm.Decimal
PX.Objects.EP.EPTaxTran.ClaimCuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.EP.EPTaxTran.ClaimCuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.EP.EPTaxTran.ClaimCuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.EP.EPTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.EP.EPTaxTran.CuryID : Edm.String "Currency"
PX.Objects.EP.EPTaxTran.CuryRate : Edm.Decimal
PX.Objects.EP.EPTaxTran.CuryViewState : Edm.Boolean
PX.Objects.EP.EPTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.EP.EPTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.EP.EPTaxTran.EPExpenseClaimDetailsByClaimDetailID -> PX.Objects.EP.EPExpenseClaimDetails (ClaimDetailID=ClaimDetailID)

# PX.Objects.EP.EPTimeActivitiesSummary (EntityType)

Label: "Time Activities Summary"
Key: ContactID, Week, WorkgroupID
Entity sets: PX_Objects_EP_EPTimeActivitiesSummary, TimeActivitiesSummary, EPTimeActivitiesSummary
Non-filterable, non-selectable: IsWithoutActivities

PX.Objects.EP.EPTimeActivitiesSummary.ContactID : Edm.Int32 [key] "Employee"
PX.Objects.EP.EPTimeActivitiesSummary.WorkgroupID : Edm.Int32 [key] "Workgroup"
PX.Objects.EP.EPTimeActivitiesSummary.Week : Edm.Int32 [key] "Week"
PX.Objects.EP.EPTimeActivitiesSummary.MondayTime : Edm.Int32 [required] "Monday"
PX.Objects.EP.EPTimeActivitiesSummary.TuesdayTime : Edm.Int32 [required] "Tuesday"
PX.Objects.EP.EPTimeActivitiesSummary.WednesdayTime : Edm.Int32 [required] "Wednesday"
PX.Objects.EP.EPTimeActivitiesSummary.ThursdayTime : Edm.Int32 [required] "Thursday"
PX.Objects.EP.EPTimeActivitiesSummary.FridayTime : Edm.Int32 [required] "Friday"
PX.Objects.EP.EPTimeActivitiesSummary.SaturdayTime : Edm.Int32 [required] "Saturday"
PX.Objects.EP.EPTimeActivitiesSummary.SundayTime : Edm.Int32 [required] "Sunday"
PX.Objects.EP.EPTimeActivitiesSummary.TotalRegularTime : Edm.Int32 [required] "Total Regular Time"
PX.Objects.EP.EPTimeActivitiesSummary.TotalBillableTime : Edm.Int32 [required] "Total Billable Time"
PX.Objects.EP.EPTimeActivitiesSummary.TotalOvertime : Edm.Int32 [required] "Total Overtime"
PX.Objects.EP.EPTimeActivitiesSummary.TotalBillableOvertime : Edm.Int32 [required] "Total Billable Overtime"
PX.Objects.EP.EPTimeActivitiesSummary.Status : Edm.String "Status"
PX.Objects.EP.EPTimeActivitiesSummary.IsMemberActive : Edm.Boolean
PX.Objects.EP.EPTimeActivitiesSummary.EmployeeStatus : Edm.String "Employee Status"
PX.Objects.EP.EPTimeActivitiesSummary.IsWithoutActivities : Edm.Boolean
PX.Objects.EP.EPTimeActivitiesSummary.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPTimeActivitiesSummary.CreatedByScreenID : Edm.String
PX.Objects.EP.EPTimeActivitiesSummary.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTimeActivitiesSummary.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPTimeActivitiesSummary.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPTimeActivitiesSummary.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTimeActivitiesSummary.VendorByContactID -> PX.Objects.AP.Vendor (ContactID=DefContactID)
PX.Objects.EP.EPTimeActivitiesSummary.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPTimeActivitiesSummary.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPTimeActivitiesSummary.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.EP.EPTimeActivitiesSummary.EPWeeklyCrewTimeActivityByWeek -> PX.Objects.EP.EPWeeklyCrewTimeActivity (WorkgroupID=WorkgroupID, Week=Week)
PX.Objects.EP.EPTimeActivitiesSummary.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)

# PX.Objects.EP.EPTimeCard (EntityType)

Label: "Employee Time Card"
Key: TimeCardCD
Entity sets: PX_Objects_EP_EPTimeCard, EmployeeTimeCard, EPTimeCard
Non-filterable, non-selectable: WorkgroupID, OwnerID, TotalTimeSpent, TotalTimeBillable, FormCaptionDescription, NoteText, WeekStartDate, WeekEndDate, WeekDescription, WeekShortDescription, TimeSpentCalc, OvertimeSpentCalc, TotalSpentCalc, TimeBillableCalc, OvertimeBillableCalc, TotalBillableCalc, TimecardType, BillingRateCalc, SunTotal, MonTotal, TueTotal, WedTotal, ThuTotal, FriTotal, SatTotal, Day1Total, Day2Total, Day3Total, Day4Total, Day5Total, Day6Total, Day7Total, Day8Total, Day9Total, Day10Total, Day11Total, Day12Total, Day13Total, Day14Total, Day15Total, Day16Total, Day17Total, Day18Total, Day19Total, Day20Total, Day21Total, Day22Total, Day23Total, Day24Total, Day25Total, Day26Total, Day27Total, Day28Total, Day29Total, Day30Total, Day31Total, WeekTotal

PX.Objects.EP.EPTimeCard.TimeCardCD : Edm.String [key] "Ref. Nbr."
PX.Objects.EP.EPTimeCard.EmployeeID : Edm.Int32 "Employee"
PX.Objects.EP.EPTimeCard.Status : Edm.String "Status"
PX.Objects.EP.EPTimeCard.OrigTimeCardCD : Edm.String "Orig. Ref. Nbr."
PX.Objects.EP.EPTimeCard.TimeCardPeriodType : Edm.String "Frequency"
PX.Objects.EP.EPTimeCard.WeekID : Edm.Int32 "Period"
PX.Objects.EP.EPTimeCard.IsHold : Edm.Boolean [required] "IsHold"
PX.Objects.EP.EPTimeCard.IsApproved : Edm.Boolean [required]
PX.Objects.EP.EPTimeCard.IsRejected : Edm.Boolean [required]
PX.Objects.EP.EPTimeCard.IsReleased : Edm.Boolean [required] "IsReleased"
PX.Objects.EP.EPTimeCard.WorkgroupID : Edm.Int32 "Workgroup ID"
PX.Objects.EP.EPTimeCard.OwnerID : Edm.Int32 "OwnerID"
PX.Objects.EP.EPTimeCard.SummaryLineCntr : Edm.Int32 [required]
PX.Objects.EP.EPTimeCard.TimeSpent : Edm.Int32 [required] "Time Spent"
PX.Objects.EP.EPTimeCard.OvertimeSpent : Edm.Int32 [required] "Overtime"
PX.Objects.EP.EPTimeCard.TimeBillable : Edm.Int32 [required] "Time Billable"
PX.Objects.EP.EPTimeCard.OvertimeBillable : Edm.Int32 [required] "Billable Overtime"
PX.Objects.EP.EPTimeCard.TotalTimeSpent : Edm.Int32 "Total Time Spent"
PX.Objects.EP.EPTimeCard.TotalTimeBillable : Edm.Int32 "Total Time Billable"
PX.Objects.EP.EPTimeCard.FormCaptionDescription : Edm.String
PX.Objects.EP.EPTimeCard.StartDate : Edm.DateTimeOffset "Period Start"
PX.Objects.EP.EPTimeCard.EndDate : Edm.DateTimeOffset "Period End"
PX.Objects.EP.EPTimeCard.NoteID : Edm.Guid
PX.Objects.EP.EPTimeCard.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPTimeCard.tstamp : Edm.Binary
PX.Objects.EP.EPTimeCard.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPTimeCard.CreatedByScreenID : Edm.String
PX.Objects.EP.EPTimeCard.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTimeCard.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPTimeCard.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPTimeCard.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTimeCard.WeekStartDate : Edm.DateTimeOffset "Week Start Date"
PX.Objects.EP.EPTimeCard.WeekEndDate : Edm.DateTimeOffset
PX.Objects.EP.EPTimeCard.WeekDescription : Edm.String "Period"
PX.Objects.EP.EPTimeCard.WeekShortDescription : Edm.String "Period"
PX.Objects.EP.EPTimeCard.TimeSpentCalc : Edm.Int32 "Time Spent"
PX.Objects.EP.EPTimeCard.OvertimeSpentCalc : Edm.Int32 "Overtime Spent"
PX.Objects.EP.EPTimeCard.TotalSpentCalc : Edm.Int32 "Total Time Spent"
PX.Objects.EP.EPTimeCard.TimeBillableCalc : Edm.Int32 "Billable"
PX.Objects.EP.EPTimeCard.OvertimeBillableCalc : Edm.Int32 "Billable Overtime"
PX.Objects.EP.EPTimeCard.TotalBillableCalc : Edm.Int32 "Total Billable"
PX.Objects.EP.EPTimeCard.TimecardType : Edm.String "Type"
PX.Objects.EP.EPTimeCard.BillingRateCalc : Edm.Int32 "Billing Ratio"
PX.Objects.EP.EPTimeCard.SunTotal : Edm.Int32
PX.Objects.EP.EPTimeCard.MonTotal : Edm.Int32
PX.Objects.EP.EPTimeCard.TueTotal : Edm.Int32
PX.Objects.EP.EPTimeCard.WedTotal : Edm.Int32
PX.Objects.EP.EPTimeCard.ThuTotal : Edm.Int32
PX.Objects.EP.EPTimeCard.FriTotal : Edm.Int32
PX.Objects.EP.EPTimeCard.SatTotal : Edm.Int32
PX.Objects.EP.EPTimeCard.Day1Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day2Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day3Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day4Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day5Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day6Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day7Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day8Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day9Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day10Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day11Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day12Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day13Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day14Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day15Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day16Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day17Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day18Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day19Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day20Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day21Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day22Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day23Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day24Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day25Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day26Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day27Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day28Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day29Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day30Total : Edm.Int32
PX.Objects.EP.EPTimeCard.Day31Total : Edm.Int32
PX.Objects.EP.EPTimeCard.WeekTotal : Edm.Int32
PX.Objects.EP.EPTimeCard.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.EP.EPTimeCard.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.EP.EPTimeCard.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPTimeCard.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPTimeCard.EPTimeCardByTimeCardCD -> PX.Objects.EP.EPTimeCard (TimeCardCD=OrigTimeCardCD)
PX.Objects.EP.EPTimeCard.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.EP.EPTimeCard.EPTimeCardCollection -> Collection(PX.Objects.EP.EPTimeCard)
PX.Objects.EP.EPTimeCard.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.EP.EPTimeCard.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.EP.EPTimeCard.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.EP.EPTimeCard.TimecardWithTotalsCollection -> Collection(PX.Objects.EP.TimecardWithTotals)

# PX.Objects.EP.EPTimeCardEx (EntityType)

Label: "Employee Time Card"
BaseType: PX.Objects.EP.EPTimeCard
Key: TimeCardCD (inherited from PX.Objects.EP.EPTimeCard)
Entity sets: PX_Objects_EP_EPTimeCardEx

# PX.Objects.EP.EPTimeCardItem (EntityType)

Label: "Time Card Item"
Key: LineNbr, TimeCardCD
Entity sets: PX_Objects_EP_EPTimeCardItem, TimeCardItem, EPTimeCardItem
Non-filterable, non-selectable: Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13, Day14, Day15, Day16, Day17, Day18, Day19, Day20, Day21, Day22, Day23, Day24, Day25, Day26, Day27, Day28, Day29, Day30, Day31, DayName1, DayName2, DayName3, DayName4, DayName5, DayName6, DayName7, DayName8, DayName9, DayName10, DayName11, DayName12, DayName13, DayName14, DayName15, DayName16, DayName17, DayName18, DayName19, DayName20, DayName21, DayName22, DayName23, DayName24, DayName25, DayName26, DayName27, DayName28, DayName29, DayName30, DayName31, NoteText

PX.Objects.EP.EPTimeCardItem.TimeCardCD : Edm.String [key] "TimeCardCD"
PX.Objects.EP.EPTimeCardItem.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.EP.EPTimeCardItem.ProjectID : Edm.Int32 "Project"
PX.Objects.EP.EPTimeCardItem.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.EP.EPTimeCardItem.Description : Edm.String "Description"
PX.Objects.EP.EPTimeCardItem.UOM : Edm.String "UOM"
PX.Objects.EP.EPTimeCardItem.Mon : Edm.Decimal "Mon"
PX.Objects.EP.EPTimeCardItem.Tue : Edm.Decimal "Tue"
PX.Objects.EP.EPTimeCardItem.Wed : Edm.Decimal "Wed"
PX.Objects.EP.EPTimeCardItem.Thu : Edm.Decimal "Thu"
PX.Objects.EP.EPTimeCardItem.Fri : Edm.Decimal "Fri"
PX.Objects.EP.EPTimeCardItem.Sat : Edm.Decimal "Sat"
PX.Objects.EP.EPTimeCardItem.Sun : Edm.Decimal "Sun"
PX.Objects.EP.EPTimeCardItem.TotalQty : Edm.Decimal "Total Qty."
PX.Objects.EP.EPTimeCardItem.TimeCardPeriodType : Edm.String "Frequency"
PX.Objects.EP.EPTimeCardItem.Day1 : Edm.Decimal "Day 1"
PX.Objects.EP.EPTimeCardItem.Day2 : Edm.Decimal "Day 2"
PX.Objects.EP.EPTimeCardItem.Day3 : Edm.Decimal "Day 3"
PX.Objects.EP.EPTimeCardItem.Day4 : Edm.Decimal "Day 4"
PX.Objects.EP.EPTimeCardItem.Day5 : Edm.Decimal "Day 5"
PX.Objects.EP.EPTimeCardItem.Day6 : Edm.Decimal "Day 6"
PX.Objects.EP.EPTimeCardItem.Day7 : Edm.Decimal "Day 7"
PX.Objects.EP.EPTimeCardItem.Day8 : Edm.Decimal "Day 8"
PX.Objects.EP.EPTimeCardItem.Day9 : Edm.Decimal "Day 9"
PX.Objects.EP.EPTimeCardItem.Day10 : Edm.Decimal "Day 10"
PX.Objects.EP.EPTimeCardItem.Day11 : Edm.Decimal "Day 11"
PX.Objects.EP.EPTimeCardItem.Day12 : Edm.Decimal "Day 12"
PX.Objects.EP.EPTimeCardItem.Day13 : Edm.Decimal "Day 13"
PX.Objects.EP.EPTimeCardItem.Day14 : Edm.Decimal "Day 14"
PX.Objects.EP.EPTimeCardItem.Day15 : Edm.Decimal "Day 15"
PX.Objects.EP.EPTimeCardItem.Day16 : Edm.Decimal "Day 16"
PX.Objects.EP.EPTimeCardItem.Day17 : Edm.Decimal "Day 17"
PX.Objects.EP.EPTimeCardItem.Day18 : Edm.Decimal "Day 18"
PX.Objects.EP.EPTimeCardItem.Day19 : Edm.Decimal "Day 19"
PX.Objects.EP.EPTimeCardItem.Day20 : Edm.Decimal "Day 20"
PX.Objects.EP.EPTimeCardItem.Day21 : Edm.Decimal "Day 21"
PX.Objects.EP.EPTimeCardItem.Day22 : Edm.Decimal "Day 22"
PX.Objects.EP.EPTimeCardItem.Day23 : Edm.Decimal "Day 23"
PX.Objects.EP.EPTimeCardItem.Day24 : Edm.Decimal "Day 24"
PX.Objects.EP.EPTimeCardItem.Day25 : Edm.Decimal "Day 25"
PX.Objects.EP.EPTimeCardItem.Day26 : Edm.Decimal "Day 26"
PX.Objects.EP.EPTimeCardItem.Day27 : Edm.Decimal "Day 27"
PX.Objects.EP.EPTimeCardItem.Day28 : Edm.Decimal "Day 28"
PX.Objects.EP.EPTimeCardItem.Day29 : Edm.Decimal "Day 29"
PX.Objects.EP.EPTimeCardItem.Day30 : Edm.Decimal "Day 30"
PX.Objects.EP.EPTimeCardItem.Day31 : Edm.Decimal "Day 31"
PX.Objects.EP.EPTimeCardItem.DayName1 : Edm.String "Day Name 1"
PX.Objects.EP.EPTimeCardItem.DayName2 : Edm.String "Day Name 2"
PX.Objects.EP.EPTimeCardItem.DayName3 : Edm.String "Day Name 3"
PX.Objects.EP.EPTimeCardItem.DayName4 : Edm.String "Day Name 4"
PX.Objects.EP.EPTimeCardItem.DayName5 : Edm.String "Day Name 5"
PX.Objects.EP.EPTimeCardItem.DayName6 : Edm.String "Day Name 6"
PX.Objects.EP.EPTimeCardItem.DayName7 : Edm.String "Day Name 7"
PX.Objects.EP.EPTimeCardItem.DayName8 : Edm.String "Day Name 8"
PX.Objects.EP.EPTimeCardItem.DayName9 : Edm.String "Day Name 9"
PX.Objects.EP.EPTimeCardItem.DayName10 : Edm.String "Day Name 10"
PX.Objects.EP.EPTimeCardItem.DayName11 : Edm.String "Day Name 11"
PX.Objects.EP.EPTimeCardItem.DayName12 : Edm.String "Day Name 12"
PX.Objects.EP.EPTimeCardItem.DayName13 : Edm.String "Day Name 13"
PX.Objects.EP.EPTimeCardItem.DayName14 : Edm.String "Day Name 14"
PX.Objects.EP.EPTimeCardItem.DayName15 : Edm.String "Day Name 15"
PX.Objects.EP.EPTimeCardItem.DayName16 : Edm.String "Day Name 16"
PX.Objects.EP.EPTimeCardItem.DayName17 : Edm.String "Day Name 17"
PX.Objects.EP.EPTimeCardItem.DayName18 : Edm.String "Day Name 18"
PX.Objects.EP.EPTimeCardItem.DayName19 : Edm.String "Day Name 19"
PX.Objects.EP.EPTimeCardItem.DayName20 : Edm.String "Day Name 20"
PX.Objects.EP.EPTimeCardItem.DayName21 : Edm.String "Day Name 21"
PX.Objects.EP.EPTimeCardItem.DayName22 : Edm.String "Day Name 22"
PX.Objects.EP.EPTimeCardItem.DayName23 : Edm.String "Day Name 23"
PX.Objects.EP.EPTimeCardItem.DayName24 : Edm.String "Day Name 24"
PX.Objects.EP.EPTimeCardItem.DayName25 : Edm.String "Day Name 25"
PX.Objects.EP.EPTimeCardItem.DayName26 : Edm.String "Day Name 26"
PX.Objects.EP.EPTimeCardItem.DayName27 : Edm.String "Day Name 27"
PX.Objects.EP.EPTimeCardItem.DayName28 : Edm.String "Day Name 28"
PX.Objects.EP.EPTimeCardItem.DayName29 : Edm.String "Day Name 29"
PX.Objects.EP.EPTimeCardItem.DayName30 : Edm.String "Day Name 30"
PX.Objects.EP.EPTimeCardItem.DayName31 : Edm.String "Day Name 31"
PX.Objects.EP.EPTimeCardItem.OrigLineNbr : Edm.Int32
PX.Objects.EP.EPTimeCardItem.NoteID : Edm.Guid
PX.Objects.EP.EPTimeCardItem.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPTimeCardItem.tstamp : Edm.Binary
PX.Objects.EP.EPTimeCardItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPTimeCardItem.CreatedByScreenID : Edm.String
PX.Objects.EP.EPTimeCardItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTimeCardItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPTimeCardItem.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPTimeCardItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTimeCardItem.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.EP.EPTimeCardItem.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.EP.EPTimeCardItem.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.EP.EPTimeCardItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.EP.EPTimeCardItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPTimeCardItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPTimeCardItem.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.EP.EPTimeCardItem.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.EP.EPTimeCardItem.EPTimeCardByTimeCardCD -> PX.Objects.EP.EPTimeCard (TimeCardCD=TimeCardCD)

# PX.Objects.EP.EPTimeCardSummary (EntityType)

Label: "Time Card Summary"
Key: LineNbr, TimeCardCD
Entity sets: PX_Objects_EP_EPTimeCardSummary, TimeCardSummary, EPTimeCardSummary
Non-filterable, non-selectable: EmployeeID, NoteText, EmployeeRate

PX.Objects.EP.EPTimeCardSummary.TimeCardCD : Edm.String [key] "TimeCardCD"
PX.Objects.EP.EPTimeCardSummary.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.EP.EPTimeCardSummary.EarningType : Edm.String "Earning Type"
PX.Objects.EP.EPTimeCardSummary.JobID : Edm.Int32
PX.Objects.EP.EPTimeCardSummary.ParentNoteID : Edm.Guid "Task ID"
PX.Objects.EP.EPTimeCardSummary.ProjectID : Edm.Int32 "Project"
PX.Objects.EP.EPTimeCardSummary.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.EP.EPTimeCardSummary.TimeSpent : Edm.Int32 "Time Spent"
PX.Objects.EP.EPTimeCardSummary.Sun : Edm.Int32 "Sun"
PX.Objects.EP.EPTimeCardSummary.Mon : Edm.Int32 "Mon"
PX.Objects.EP.EPTimeCardSummary.Tue : Edm.Int32 "Tue"
PX.Objects.EP.EPTimeCardSummary.Wed : Edm.Int32 "Wed"
PX.Objects.EP.EPTimeCardSummary.Thu : Edm.Int32 "Thu"
PX.Objects.EP.EPTimeCardSummary.Fri : Edm.Int32 "Fri"
PX.Objects.EP.EPTimeCardSummary.Sat : Edm.Int32 "Sat"
PX.Objects.EP.EPTimeCardSummary.TimeCardPeriodType : Edm.String "Frequency"
PX.Objects.EP.EPTimeCardSummary.IsBillable : Edm.Boolean "Billable"
PX.Objects.EP.EPTimeCardSummary.Description : Edm.String "Description"
PX.Objects.EP.EPTimeCardSummary.EmployeeID : Edm.Int32
PX.Objects.EP.EPTimeCardSummary.NoteID : Edm.Guid
PX.Objects.EP.EPTimeCardSummary.NoteText : Edm.String "Note Text"
PX.Objects.EP.EPTimeCardSummary.tstamp : Edm.Binary
PX.Objects.EP.EPTimeCardSummary.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPTimeCardSummary.CreatedByScreenID : Edm.String
PX.Objects.EP.EPTimeCardSummary.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTimeCardSummary.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPTimeCardSummary.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPTimeCardSummary.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPTimeCardSummary.EmployeeRate : Edm.Decimal "Cost Rate"
PX.Objects.EP.EPTimeCardSummary.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.EP.EPTimeCardSummary.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.EP.EPTimeCardSummary.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.EP.EPTimeCardSummary.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.EP.EPTimeCardSummary.CRActivityByParentNoteID -> PX.Objects.CR.CRActivity (ParentNoteID=NoteID)
PX.Objects.EP.EPTimeCardSummary.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPTimeCardSummary.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPTimeCardSummary.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.EP.EPTimeCardSummary.PMUnionByUnionID -> PX.Objects.PM.PMUnion
PX.Objects.EP.EPTimeCardSummary.PMWorkCodeByWorkCodeID -> PX.Objects.PM.PMWorkCode
PX.Objects.EP.EPTimeCardSummary.EPEarningTypeByEarningType -> PX.Objects.EP.EPEarningType (EarningType=TypeCD)
PX.Objects.EP.EPTimeCardSummary.EPShiftCodeByShiftID -> PX.Objects.EP.EPShiftCode
PX.Objects.EP.EPTimeCardSummary.EPTimeCardByTimeCardCD -> PX.Objects.EP.EPTimeCard (TimeCardCD=TimeCardCD)

# PX.Objects.EP.EPView (EntityType)

Label: "Activity View Status"
Key: ContactID, NoteID
Entity sets: PX_Objects_EP_EPView, ActivityViewStatus, EPView

PX.Objects.EP.EPView.NoteID : Edm.Guid [key]
PX.Objects.EP.EPView.ContactID : Edm.Int32 [key]
PX.Objects.EP.EPView.Status : Edm.Int32 [required] "Status"
PX.Objects.EP.EPView.Read : Edm.Boolean "Read"
PX.Objects.EP.EPView.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPView.CreatedByScreenID : Edm.String
PX.Objects.EP.EPView.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPView.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPView.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPView.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPView.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPView.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.EP.EPViewMy (EntityType)

Label: "Activity View Status"
BaseType: PX.Objects.EP.EPView
Key: ContactID, NoteID (inherited from PX.Objects.EP.EPView)
Entity sets: PX_Objects_EP_EPViewMy, ActivityViewStatus1, EPViewMy

# PX.Objects.EP.EPWeeklyCrewTimeActivity (EntityType)

Label: "Weekly Crew Time Activity"
Key: Week, WorkgroupID
Entity sets: PX_Objects_EP_EPWeeklyCrewTimeActivity, WeeklyCrewTimeActivity, EPWeeklyCrewTimeActivity

PX.Objects.EP.EPWeeklyCrewTimeActivity.WorkgroupID : Edm.Int32 [key] "Workgroup"
PX.Objects.EP.EPWeeklyCrewTimeActivity.Week : Edm.Int32 [key] "Week"
PX.Objects.EP.EPWeeklyCrewTimeActivity.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPWeeklyCrewTimeActivity.CreatedByScreenID : Edm.String
PX.Objects.EP.EPWeeklyCrewTimeActivity.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPWeeklyCrewTimeActivity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPWeeklyCrewTimeActivity.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPWeeklyCrewTimeActivity.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.EP.EPWeeklyCrewTimeActivity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPWeeklyCrewTimeActivity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPWeeklyCrewTimeActivity.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.EP.EPWeeklyCrewTimeActivity.EPTimeActivitiesSummaryCollection -> Collection(PX.Objects.EP.EPTimeActivitiesSummary)

# PX.Objects.EP.EPWingman (EntityType)

Label: "Delegate"
Key: RecordID
Entity sets: PX_Objects_EP_EPWingman, Delegate, EPWingman

PX.Objects.EP.EPWingman.RecordID : Edm.Int32 [key]
PX.Objects.EP.EPWingman.EmployeeID : Edm.Int32
PX.Objects.EP.EPWingman.WingmanID : Edm.Int32 "Delegated To"
PX.Objects.EP.EPWingman.DelegationOf : Edm.String "Delegation Of"
PX.Objects.EP.EPWingman.StartsOn : Edm.DateTimeOffset "Starts On"
PX.Objects.EP.EPWingman.ExpiresOn : Edm.DateTimeOffset "Expires On"
PX.Objects.EP.EPWingman.IsActive : Edm.Boolean [required] "Active"
PX.Objects.EP.EPWingman.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.EPWingman.CreatedByScreenID : Edm.String
PX.Objects.EP.EPWingman.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.EP.EPWingman.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.EP.EPWingman.LastModifiedByScreenID : Edm.String
PX.Objects.EP.EPWingman.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.EP.EPWingman.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.EP.EPWingman.EPEmployeeByWingmanID -> PX.Objects.EP.EPEmployee (WingmanID=BAccountID)
PX.Objects.EP.EPWingman.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.EP.EPWingman.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.EP.EPWingman.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.EP.EPWingman.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)

# PX.Objects.EP.Standalone.EPEmployeeClass (EntityType)

Key: VendorClassID
Entity sets: PX_Objects_EP_Standalone_EPEmployeeClass

PX.Objects.EP.Standalone.EPEmployeeClass.VendorClassID : Edm.String [key]
PX.Objects.EP.Standalone.EPEmployeeClass.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.EP.Standalone.EPEmployeeClass.UsersByCreatedByID -> PX.SM.Users
PX.Objects.EP.Standalone.EPEmployeeClass.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.EP.Standalone.EPEmployeeClass.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone
PX.Objects.EP.Standalone.EPEmployeeClass.CountryByCountryID -> PX.Objects.CS.Country
PX.Objects.EP.Standalone.EPEmployeeClass.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms
PX.Objects.EP.Standalone.EPEmployeeClass.TermsByTermsID -> PX.Objects.CS.Terms
PX.Objects.EP.Standalone.EPEmployeeClass.CurrencyByCuryID -> PX.Objects.CM.Currency
PX.Objects.EP.Standalone.EPEmployeeClass.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList
PX.Objects.EP.Standalone.EPEmployeeClass.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType
PX.Objects.EP.Standalone.EPEmployeeClass.AccountByDiscTakenAcctID -> PX.Objects.GL.Account
PX.Objects.EP.Standalone.EPEmployeeClass.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.EP.Standalone.EPEmployeeClass.AccountByAPAcctID -> PX.Objects.GL.Account
PX.Objects.EP.Standalone.EPEmployeeClass.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.EP.Standalone.EPEmployeeClass.AccountByPrepaymentAcctID -> PX.Objects.GL.Account
PX.Objects.EP.Standalone.EPEmployeeClass.AccountByUnrealizedGainAcctID -> PX.Objects.GL.Account
PX.Objects.EP.Standalone.EPEmployeeClass.AccountByUnrealizedLossAcctID -> PX.Objects.GL.Account
PX.Objects.EP.Standalone.EPEmployeeClass.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.EP.Standalone.EPEmployeeClass.SubByDiscTakenSubID -> PX.Objects.GL.Sub
PX.Objects.EP.Standalone.EPEmployeeClass.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.EP.Standalone.EPEmployeeClass.SubByAPSubID -> PX.Objects.GL.Sub
PX.Objects.EP.Standalone.EPEmployeeClass.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.EP.Standalone.EPEmployeeClass.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.EP.Standalone.EPEmployeeClass.SubByUnrealizedGainSubID -> PX.Objects.GL.Sub
PX.Objects.EP.Standalone.EPEmployeeClass.SubByUnrealizedLossSubID -> PX.Objects.GL.Sub
PX.Objects.EP.Standalone.EPEmployeeClass.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.EP.Standalone.EPEmployeeClass.CashAccountByCashAcctID -> PX.Objects.CA.CashAccount
PX.Objects.EP.Standalone.EPEmployeeClass.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.Objects.EP.Standalone.EPEmployeeClass.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar
PX.Objects.EP.Standalone.EPEmployeeClass.RelationGroupByGroupMask -> PX.SM.RelationGroup
PX.Objects.EP.Standalone.EPEmployeeClass.LocaleByLocaleName -> PX.SM.Locale
PX.Objects.EP.Standalone.EPEmployeeClass.VendorCollection -> Collection(PX.Objects.AP.Vendor)

# PX.Objects.EP.TimecardWithTotals (EntityType)

Key: TimeCardCD
Entity sets: PX_Objects_EP_TimecardWithTotals
Non-filterable, non-selectable: WeekStartDate

PX.Objects.EP.TimecardWithTotals.TimeCardCD : Edm.String [key] "Ref. Nbr."
PX.Objects.EP.TimecardWithTotals.StartDate : Edm.DateTimeOffset "Period Start"
PX.Objects.EP.TimecardWithTotals.EndDate : Edm.DateTimeOffset "Period End"
PX.Objects.EP.TimecardWithTotals.NoteID : Edm.Guid
PX.Objects.EP.TimecardWithTotals.IsApproved : Edm.Boolean "IsApproved"
PX.Objects.EP.TimecardWithTotals.IsRejected : Edm.Boolean "IsRejected"
PX.Objects.EP.TimecardWithTotals.IsHold : Edm.Boolean "IsHold"
PX.Objects.EP.TimecardWithTotals.IsReleased : Edm.Boolean "IsReleased"
PX.Objects.EP.TimecardWithTotals.CreatedByID : Edm.Guid "Created By"
PX.Objects.EP.TimecardWithTotals.TimeSpentFinal : Edm.Int32
PX.Objects.EP.TimecardWithTotals.TimeBillableFinal : Edm.Int32
PX.Objects.EP.TimecardWithTotals.OvertimeSpentFinal : Edm.Int32
PX.Objects.EP.TimecardWithTotals.OvertimeBillableFinal : Edm.Int32
PX.Objects.EP.TimecardWithTotals.TimeSpentCurrent : Edm.Int32
PX.Objects.EP.TimecardWithTotals.TimeBillableCurrent : Edm.Int32
PX.Objects.EP.TimecardWithTotals.OvertimeSpentCurrent : Edm.Int32
PX.Objects.EP.TimecardWithTotals.OvertimeBillableCurrent : Edm.Int32
PX.Objects.EP.TimecardWithTotals.DefContactID : Edm.Int32 "Employee Login"
PX.Objects.EP.TimecardWithTotals.WeekStartDate : Edm.DateTimeOffset "Week Start Date"
PX.Objects.EP.TimecardWithTotals.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee
PX.Objects.EP.TimecardWithTotals.EPTimeCardByTimeCardCD -> PX.Objects.EP.EPTimeCard (TimeCardCD=TimeCardCD)
PX.Objects.EP.TimecardWithTotals.VendorByEmployeeID -> PX.Objects.AP.Vendor
PX.Objects.EP.TimecardWithTotals.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.EP.TimecardWithTotals.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.EP.TimecardWithTotals.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.EP.TimecardWithTotals.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.EP.TimecardWithTotals.TimecardWithTotalsCollection -> Collection(PX.Objects.EP.TimecardWithTotals)

# PX.Objects.FA.DAC.FALocationHistoryByPeriod (EntityType)

Label: "FA Location History by Period"
Key: AssetID, LastRevisionID
Entity sets: PX_Objects_FA_DAC_FALocationHistoryByPeriod, FALocationHistorybyPeriod

PX.Objects.FA.DAC.FALocationHistoryByPeriod.AssetID : Edm.Int32 [key]
PX.Objects.FA.DAC.FALocationHistoryByPeriod.PeriodID : Edm.String
PX.Objects.FA.DAC.FALocationHistoryByPeriod.LastPeriodID : Edm.String
PX.Objects.FA.DAC.FALocationHistoryByPeriod.LastRevisionID : Edm.Int32 [key]
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FABookBalanceCollection -> Collection(PX.Objects.FA.FABookBalance)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FABookHistoryCollection -> Collection(PX.Objects.FA.FABookHistory)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FAApplicableMethodCollection -> Collection(PX.Objects.FA.FAApplicableMethod)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FABookSettingsCollection -> Collection(PX.Objects.FA.FABookSettings)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FAHistoryByPeriodCollection -> Collection(PX.Objects.FA.FAHistoryByPeriod)
PX.Objects.FA.DAC.FALocationHistoryByPeriod.FALocationHistoryByPeriodCollection -> Collection(PX.Objects.FA.DAC.FALocationHistoryByPeriod)

# PX.Objects.FA.FAAccrualTran (EntityType)

Label: "FA Accrual Transaction"
Key: GLTranID
Entity sets: PX_Objects_FA_FAAccrualTran, FAAccrualTransaction, FAAccrualTran
Non-filterable, non-selectable: SelectedQty, SelectedAmt, ClassID, EmployeeID, Department, Component

PX.Objects.FA.FAAccrualTran.TranID : Edm.Int32
PX.Objects.FA.FAAccrualTran.GLTranID : Edm.Int32 [key]
PX.Objects.FA.FAAccrualTran.GLTranAccountID : Edm.Int32
PX.Objects.FA.FAAccrualTran.GLTranSubID : Edm.Int32
PX.Objects.FA.FAAccrualTran.GLTranQty : Edm.Decimal "Orig. Quantity"
PX.Objects.FA.FAAccrualTran.GLTranAmt : Edm.Decimal "Orig. Amount"
PX.Objects.FA.FAAccrualTran.SelectedQty : Edm.Decimal "Selected Quantity"
PX.Objects.FA.FAAccrualTran.SelectedAmt : Edm.Decimal "Selected Amount"
PX.Objects.FA.FAAccrualTran.OpenQty : Edm.Decimal "Open Quantity"
PX.Objects.FA.FAAccrualTran.OpenAmt : Edm.Decimal "Open Amount"
PX.Objects.FA.FAAccrualTran.ClosedAmt : Edm.Decimal [required]
PX.Objects.FA.FAAccrualTran.ClosedQty : Edm.Decimal [required]
PX.Objects.FA.FAAccrualTran.UnitCost : Edm.Decimal "Unit Cost"
PX.Objects.FA.FAAccrualTran.Reconciled : Edm.Boolean [required] "Reconciled"
PX.Objects.FA.FAAccrualTran.GLTranQtyCalc : Edm.Decimal
PX.Objects.FA.FAAccrualTran.GLTranAmtCalc : Edm.Decimal
PX.Objects.FA.FAAccrualTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FAAccrualTran.CreatedByScreenID : Edm.String
PX.Objects.FA.FAAccrualTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAAccrualTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FAAccrualTran.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FAAccrualTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAAccrualTran.ClassID : Edm.Int32 "Asset Class"
PX.Objects.FA.FAAccrualTran.EmployeeID : Edm.Int32 "Custodian"
PX.Objects.FA.FAAccrualTran.Department : Edm.String "Department"
PX.Objects.FA.FAAccrualTran.Component : Edm.Boolean "Component"
PX.Objects.FA.FAAccrualTran.GLTranDebitAmt : Edm.Decimal
PX.Objects.FA.FAAccrualTran.GLTranCreditAmt : Edm.Decimal
PX.Objects.FA.FAAccrualTran.GLTranOrigQty : Edm.Decimal
PX.Objects.FA.FAAccrualTran.GLTranInventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FA.FAAccrualTran.GLTranModule : Edm.String "Module"
PX.Objects.FA.FAAccrualTran.GLTranBatchNbr : Edm.String "Batch Number"
PX.Objects.FA.FAAccrualTran.GLTranUOM : Edm.String "UOM"
PX.Objects.FA.FAAccrualTran.GLTranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.FA.FAAccrualTran.GLTranRefNbr : Edm.String "Ref. Number"
PX.Objects.FA.FAAccrualTran.GLTranReferenceID : Edm.Int32 "Customer/Vendor"
PX.Objects.FA.FAAccrualTran.GLTranDesc : Edm.String "Transaction Description"
PX.Objects.FA.FAAccrualTran.GLReclassified : Edm.Boolean
PX.Objects.FA.FAAccrualTran.GLReclassRemainingAmt : Edm.Decimal
PX.Objects.FA.FAAccrualTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FA.FAAccrualTran.UOM : Edm.String "UOM"
PX.Objects.FA.FAAccrualTran.BAccountByGLTranReferenceID -> PX.Objects.CR.BAccount (GLTranReferenceID=BAccountID)
PX.Objects.FA.FAAccrualTran.BatchByGLTranBatchNbr -> PX.Objects.GL.Batch (GLTranBatchNbr=BatchNbr)
PX.Objects.FA.FAAccrualTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FA.FAAccrualTran.BranchByGLTranID -> PX.Objects.GL.Branch (GLTranID=BranchID)
PX.Objects.FA.FAAccrualTran.BranchByGLTranBranchID -> PX.Objects.GL.Branch
PX.Objects.FA.FAAccrualTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FAAccrualTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FAAccrualTran.AccountByGLTranAccountID -> PX.Objects.GL.Account (GLTranAccountID=AccountID)
PX.Objects.FA.FAAccrualTran.SubByGLTranSubID -> PX.Objects.GL.Sub (GLTranSubID=SubID)
PX.Objects.FA.FAAccrualTran.FATranCollection -> Collection(PX.Objects.FA.FATran)

# PX.Objects.FA.FAApplicableMethod (EntityType)

Label: "FA Applicable Method"
Key: AssetID, BookID, StartPeriodID
Entity sets: PX_Objects_FA_FAApplicableMethod, FAApplicableMethod
Non-filterable, non-selectable: AveragingConvention, IsOriginal

PX.Objects.FA.FAApplicableMethod.AssetID : Edm.Int32 [key]
PX.Objects.FA.FAApplicableMethod.BookID : Edm.Int32 [key]
PX.Objects.FA.FAApplicableMethod.DepreciationMethodID : Edm.Int32 "Depreciation Method"
PX.Objects.FA.FAApplicableMethod.AveragingConvention : Edm.String
PX.Objects.FA.FAApplicableMethod.StartPeriodID : Edm.String [key] "Start Period"
PX.Objects.FA.FAApplicableMethod.IsOriginal : Edm.Boolean
PX.Objects.FA.FAApplicableMethod.PercentPerYear : Edm.Decimal "Percent per Year"
PX.Objects.FA.FAApplicableMethod.UsefulLife : Edm.Decimal "Useful Life (Years)"
PX.Objects.FA.FAApplicableMethod.DeprToDate : Edm.DateTimeOffset
PX.Objects.FA.FAApplicableMethod.DeprToPeriod : Edm.String
PX.Objects.FA.FAApplicableMethod.CreatedByScreenID : Edm.String
PX.Objects.FA.FAApplicableMethod.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FAApplicableMethod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAApplicableMethod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FAApplicableMethod.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FAApplicableMethod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAApplicableMethod.tstamp : Edm.Binary
PX.Objects.FA.FAApplicableMethod.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FAApplicableMethod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FAApplicableMethod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FAApplicableMethod.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FAApplicableMethod.FABookBalanceByBookID -> PX.Objects.FA.FABookBalance (AssetID=AssetID, BookID=BookID)
PX.Objects.FA.FAApplicableMethod.FABookBalanceByAssetID -> PX.Objects.FA.FABookBalance (BookID=BookID, AssetID=AssetID)

# PX.Objects.FA.FABonus (EntityType)

Label: "Bonus"
Key: BonusCD
Entity sets: PX_Objects_FA_FABonus, Bonus, FABonus
Non-filterable, non-selectable: NoteText

PX.Objects.FA.FABonus.BonusID : Edm.Int32 "BonusID"
PX.Objects.FA.FABonus.BonusCD : Edm.String [key] "Bonus ID"
PX.Objects.FA.FABonus.State : Edm.String "State"
PX.Objects.FA.FABonus.Description : Edm.String "Description"
PX.Objects.FA.FABonus.NoteID : Edm.Guid
PX.Objects.FA.FABonus.NoteText : Edm.String "Note Text"
PX.Objects.FA.FABonus.tstamp : Edm.Binary
PX.Objects.FA.FABonus.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABonus.CreatedByScreenID : Edm.String
PX.Objects.FA.FABonus.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABonus.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABonus.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABonus.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABonus.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABonus.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABonus.FABonusDetailsCollection -> Collection(PX.Objects.FA.FABonusDetails)
PX.Objects.FA.FABonus.FABookBalanceCollection -> Collection(PX.Objects.FA.FABookBalance)

# PX.Objects.FA.FABonusDetails (EntityType)

Label: "FA Bonus Details"
Key: BonusID, LineNbr
Entity sets: PX_Objects_FA_FABonusDetails, FABonusDetails

PX.Objects.FA.FABonusDetails.BonusID : Edm.Int32 [key] "BonusID"
PX.Objects.FA.FABonusDetails.LineNbr : Edm.Int32 [key]
PX.Objects.FA.FABonusDetails.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.FA.FABonusDetails.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.FA.FABonusDetails.BonusPercent : Edm.Decimal "Bonus, %"
PX.Objects.FA.FABonusDetails.BonusMax : Edm.Decimal "Max. Bonus"
PX.Objects.FA.FABonusDetails.tstamp : Edm.Binary
PX.Objects.FA.FABonusDetails.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABonusDetails.CreatedByScreenID : Edm.String
PX.Objects.FA.FABonusDetails.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABonusDetails.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABonusDetails.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABonusDetails.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABonusDetails.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABonusDetails.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABonusDetails.FABonusByBonusID -> PX.Objects.FA.FABonus (BonusID=BonusID)

# PX.Objects.FA.FABook (EntityType)

Label: "FA Book"
Key: BookCode
Entity sets: PX_Objects_FA_FABook, FABook

PX.Objects.FA.FABook.BookCode : Edm.String [key] "Book ID"
PX.Objects.FA.FABook.Description : Edm.String "Description"
PX.Objects.FA.FABook.BookID : Edm.Int32
PX.Objects.FA.FABook.UpdateGL : Edm.Boolean [required] "Posting Book"
PX.Objects.FA.FABook.MidMonthType : Edm.String "Mid-Period Type"
PX.Objects.FA.FABook.MidMonthDay : Edm.Int16 "Mid-Period Day"
PX.Objects.FA.FABook.tstamp : Edm.Binary
PX.Objects.FA.FABook.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABook.CreatedByScreenID : Edm.String
PX.Objects.FA.FABook.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABook.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABook.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABook.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABook.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABook.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABook.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.FA.FABook.FABookHistoryCollection -> Collection(PX.Objects.FA.FABookHistory)
PX.Objects.FA.FABook.FABookPeriodCollection -> Collection(PX.Objects.FA.FABookPeriod)
PX.Objects.FA.FABook.FABookYearCollection -> Collection(PX.Objects.FA.FABookYear)
PX.Objects.FA.FABook.FAApplicableMethodCollection -> Collection(PX.Objects.FA.FAApplicableMethod)
PX.Objects.FA.FABook.FABookBalanceCollection -> Collection(PX.Objects.FA.FABookBalance)
PX.Objects.FA.FABook.FABookPeriodSetupCollection -> Collection(PX.Objects.FA.FABookPeriodSetup)
PX.Objects.FA.FABook.FABookSettingsCollection -> Collection(PX.Objects.FA.FABookSettings)
PX.Objects.FA.FABook.FABookYearSetupCollection -> Collection(PX.Objects.FA.FABookYearSetup)
PX.Objects.FA.FABook.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.Objects.FA.FABook.FAHistoryByPeriodCollection -> Collection(PX.Objects.FA.FAHistoryByPeriod)

# PX.Objects.FA.FABookBalance (EntityType)

Label: "FA Book Balance"
Key: AssetID, BookID
Entity sets: PX_Objects_FA_FABookBalance, FABookBalance
Non-filterable, non-selectable: DeprFromYear, DeprToYear, DisposalAmount, AllowChangeDeprFromPeriod, NoteText

PX.Objects.FA.FABookBalance.AssetID : Edm.Int32 [key] "Fixed Asset"
PX.Objects.FA.FABookBalance.ClassID : Edm.Int32 "Asset Class"
PX.Objects.FA.FABookBalance.BookID : Edm.Int32 [key] "Book"
PX.Objects.FA.FABookBalance.Status : Edm.String "Status"
PX.Objects.FA.FABookBalance.UpdateGL : Edm.Boolean "Posting Book"
PX.Objects.FA.FABookBalance.BookCD : Edm.String "Book CD"
PX.Objects.FA.FABookBalance.Depreciate : Edm.Boolean "Depreciable"
PX.Objects.FA.FABookBalance.IsMultipleMethodsMode : Edm.Boolean [required] "Multiple Methods"
PX.Objects.FA.FABookBalance.AveragingConvention : Edm.String "Averaging Convention"
PX.Objects.FA.FABookBalance.PercentPerYear : Edm.Decimal "Percent per Year"
PX.Objects.FA.FABookBalance.UsefulLife : Edm.Decimal "Useful Life, Years"
PX.Objects.FA.FABookBalance.MidMonthType : Edm.String "Mid-Period Type"
PX.Objects.FA.FABookBalance.MidMonthDay : Edm.Int16 "Mid-Period Day"
PX.Objects.FA.FABookBalance.ADSLife : Edm.Decimal "ADS Life, Years"
PX.Objects.FA.FABookBalance.AcquisitionCost : Edm.Decimal "Orig. Acquisition Cost"
PX.Objects.FA.FABookBalance.SalvageAmount : Edm.Decimal "Salvage Amount"
PX.Objects.FA.FABookBalance.BusinessUse : Edm.Decimal "Business Use, %"
PX.Objects.FA.FABookBalance.BonusID : Edm.Int32 "Bonus"
PX.Objects.FA.FABookBalance.BonusRate : Edm.Decimal "Bonus Rate"
PX.Objects.FA.FABookBalance.BonusAmount : Edm.Decimal "Bonus Amount"
PX.Objects.FA.FABookBalance.Tax179Amount : Edm.Decimal "Tax 179 Amount"
PX.Objects.FA.FABookBalance.DeprFromDate : Edm.DateTimeOffset "Depr. From"
PX.Objects.FA.FABookBalance.DeprFromPeriod : Edm.String "Depr. From Period"
PX.Objects.FA.FABookBalance.DeprFromYear : Edm.String
PX.Objects.FA.FABookBalance.DepreciationMethodID : Edm.Int32 "Depreciation Method"
PX.Objects.FA.FABookBalance.RecoveryPeriod : Edm.Int32 "Recovery Periods"
PX.Objects.FA.FABookBalance.DeprToDate : Edm.DateTimeOffset "Depr. to"
PX.Objects.FA.FABookBalance.DeprToPeriod : Edm.String "Depr. to Period"
PX.Objects.FA.FABookBalance.DeprToYear : Edm.String
PX.Objects.FA.FABookBalance.LastDeprPeriod : Edm.String "Last Depr. Period"
PX.Objects.FA.FABookBalance.CurrDeprPeriod : Edm.String "Current Period"
PX.Objects.FA.FABookBalance.InitPeriod : Edm.String
PX.Objects.FA.FABookBalance.LastPeriod : Edm.String
PX.Objects.FA.FABookBalance.HistPeriod : Edm.String
PX.Objects.FA.FABookBalance.MaxHistoryPeriodID : Edm.String
PX.Objects.FA.FABookBalance.DisposalPeriodID : Edm.String
PX.Objects.FA.FABookBalance.YtdDeprBase : Edm.Decimal "Basis"
PX.Objects.FA.FABookBalance.YtdDepreciated : Edm.Decimal "Accum. Depr."
PX.Objects.FA.FABookBalance.YtdBal : Edm.Decimal "Net Value"
PX.Objects.FA.FABookBalance.YtdAcquired : Edm.Decimal "Current Cost"
PX.Objects.FA.FABookBalance.YtdTax179Recap : Edm.Decimal "Tax 179 Recapture"
PX.Objects.FA.FABookBalance.YtdBonusRecap : Edm.Decimal "Bonus Recapture"
PX.Objects.FA.FABookBalance.YtdRGOL : Edm.Decimal "Gain/Loss Amount"
PX.Objects.FA.FABookBalance.PtdDeprDisposed : Edm.Decimal
PX.Objects.FA.FABookBalance.YtdSuspended : Edm.Int32
PX.Objects.FA.FABookBalance.YtdReconciled : Edm.Decimal
PX.Objects.FA.FABookBalance.DisposalAmount : Edm.Decimal "Disposal Amount"
PX.Objects.FA.FABookBalance.OrigDeprToDate : Edm.DateTimeOffset
PX.Objects.FA.FABookBalance.AllowChangeDeprFromPeriod : Edm.Boolean
PX.Objects.FA.FABookBalance.IsAcquired : Edm.Boolean [required]
PX.Objects.FA.FABookBalance.tstamp : Edm.Binary
PX.Objects.FA.FABookBalance.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABookBalance.CreatedByScreenID : Edm.String
PX.Objects.FA.FABookBalance.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookBalance.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABookBalance.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABookBalance.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookBalance.NoteID : Edm.Guid
PX.Objects.FA.FABookBalance.NoteText : Edm.String "Note Text"
PX.Objects.FA.FABookBalance.FixedAssetByClassID -> PX.Objects.FA.FixedAsset (ClassID=AssetID)
PX.Objects.FA.FABookBalance.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FABookBalance.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABookBalance.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABookBalance.FABonusByBonusID -> PX.Objects.FA.FABonus (BonusID=BonusID)
PX.Objects.FA.FABookBalance.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FABookBalance.FADepreciationMethodByUsefulLife -> PX.Objects.FA.FADepreciationMethod (DepreciationMethodID=MethodID, UsefulLife=UsefulLife)
PX.Objects.FA.FABookBalance.FAApplicableMethodCollection -> Collection(PX.Objects.FA.FAApplicableMethod)

# PX.Objects.FA.FABookHistory (EntityType)

Label: "FA Book History"
Key: AssetID, BookID, FinPeriodID
Entity sets: PX_Objects_FA_FABookHistory, FABookHistory
Non-filterable, non-selectable: Reopen

PX.Objects.FA.FABookHistory.AssetID : Edm.Int32 [key]
PX.Objects.FA.FABookHistory.BookID : Edm.Int32 [key]
PX.Objects.FA.FABookHistory.FinPeriodID : Edm.String [key]
PX.Objects.FA.FABookHistory.Closed : Edm.Boolean [required]
PX.Objects.FA.FABookHistory.Reopen : Edm.Boolean
PX.Objects.FA.FABookHistory.Suspended : Edm.Boolean [required]
PX.Objects.FA.FABookHistory.BegBal : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdBal : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.BegDeprBase : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdDeprBase : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdDeprBase : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdAcquired : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdAcquired : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdReconciled : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdReconciled : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdDepreciated : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdDepreciated : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdAdjusted : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdDeprDisposed : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdCalculated : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdCalculated : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdBonus : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdBonus : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdBonusTaken : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdBonusTaken : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdBonusCalculated : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdBonusCalculated : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdBonusRecap : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdBonusRecap : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdTax179 : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdTax179 : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdTax179Taken : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdTax179Taken : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdTax179Calculated : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdTax179Calculated : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdTax179Recap : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdTax179Recap : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdRevalueAmount : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdRevalueAmount : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdDisposalAmount : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdDisposalAmount : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdRGOL : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.PtdRGOL : Edm.Decimal [required]
PX.Objects.FA.FABookHistory.YtdSuspended : Edm.Int32 [required]
PX.Objects.FA.FABookHistory.YtdReversed : Edm.Int32 [required]
PX.Objects.FA.FABookHistory.tstamp : Edm.Binary
PX.Objects.FA.FABookHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABookHistory.CreatedByScreenID : Edm.String
PX.Objects.FA.FABookHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABookHistory.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABookHistory.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookHistory.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FABookHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABookHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABookHistory.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)

# PX.Objects.FA.FABookHistoryByPeriod (EntityType)

Label: "FA Book History by Period"
Key: AssetID, BookID, FinPeriodID
Entity sets: PX_Objects_FA_FABookHistoryByPeriod, FABookHistorybyPeriod

PX.Objects.FA.FABookHistoryByPeriod.AssetID : Edm.Int32 [key]
PX.Objects.FA.FABookHistoryByPeriod.BookID : Edm.Int32 [key]
PX.Objects.FA.FABookHistoryByPeriod.FinPeriodID : Edm.String [key]
PX.Objects.FA.FABookHistoryByPeriod.LastActivityPeriod : Edm.String "Last Activity Period"
PX.Objects.FA.FABookHistoryByPeriod.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FABookHistoryByPeriod.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)

# PX.Objects.FA.FABookHistoryRecon (EntityType)

Label: "FA Book History for Reconciliation"
Key: AssetID, BookID
Entity sets: PX_Objects_FA_FABookHistoryRecon, FABookHistoryforReconciliation, FABookHistoryRecon

PX.Objects.FA.FABookHistoryRecon.AssetID : Edm.Int32 [key]
PX.Objects.FA.FABookHistoryRecon.BookID : Edm.Int32 [key]
PX.Objects.FA.FABookHistoryRecon.UpdateGL : Edm.Boolean
PX.Objects.FA.FABookHistoryRecon.YtdAcquired : Edm.Decimal
PX.Objects.FA.FABookHistoryRecon.YtdReconciled : Edm.Decimal
PX.Objects.FA.FABookHistoryRecon.CurrentCost : Edm.Decimal
PX.Objects.FA.FABookHistoryRecon.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FABookHistoryRecon.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)

# PX.Objects.FA.FABookPeriod (EntityType)

Label: "FA Book Period"
Key: BookID, FinPeriodID, OrganizationID
Entity sets: PX_Objects_FA_FABookPeriod, FABookPeriod
Non-filterable, non-selectable: StartDateUI, EndDateUI

PX.Objects.FA.FABookPeriod.BookID : Edm.Int32 [key]
PX.Objects.FA.FABookPeriod.OrganizationID : Edm.Int32 [key required]
PX.Objects.FA.FABookPeriod.FinYear : Edm.String "FinYear"
PX.Objects.FA.FABookPeriod.FinPeriodID : Edm.String [key] "Financial Period ID"
PX.Objects.FA.FABookPeriod.MasterFinPeriodID : Edm.String "Master Calendar Period ID"
PX.Objects.FA.FABookPeriod.StartDateUI : Edm.DateTimeOffset "Start Date"
PX.Objects.FA.FABookPeriod.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.FA.FABookPeriod.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.FA.FABookPeriod.EndDate : Edm.DateTimeOffset [required] "EndDate"
PX.Objects.FA.FABookPeriod.Descr : Edm.String "Description"
PX.Objects.FA.FABookPeriod.Closed : Edm.Boolean [required] "Closed in GL"
PX.Objects.FA.FABookPeriod.DateLocked : Edm.Boolean [required] "Date Locked"
PX.Objects.FA.FABookPeriod.Active : Edm.Boolean [required] "Active"
PX.Objects.FA.FABookPeriod.PeriodNbr : Edm.String "Period Nbr."
PX.Objects.FA.FABookPeriod.tstamp : Edm.Binary
PX.Objects.FA.FABookPeriod.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABookPeriod.CreatedByScreenID : Edm.String
PX.Objects.FA.FABookPeriod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookPeriod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABookPeriod.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABookPeriod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookPeriod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABookPeriod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABookPeriod.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.FA.FABookPeriod.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FABookPeriod.FABookYearByOrganizationID -> PX.Objects.FA.FABookYear (BookID=BookID, OrganizationID=OrganizationID)

# PX.Objects.FA.FABookPeriodSetup (EntityType)

Label: "FA Book Period Template"
Key: BookID, PeriodNbr
Entity sets: PX_Objects_FA_FABookPeriodSetup, FABookPeriodTemplate, FABookPeriodSetup
Non-filterable, non-selectable: StartDateUI, EndDateUI

PX.Objects.FA.FABookPeriodSetup.BookID : Edm.Int32 [key]
PX.Objects.FA.FABookPeriodSetup.PeriodNbr : Edm.String [key] "Period Nbr."
PX.Objects.FA.FABookPeriodSetup.StartDateUI : Edm.DateTimeOffset "Start Date"
PX.Objects.FA.FABookPeriodSetup.EndDateUI : Edm.DateTimeOffset "End Date"
PX.Objects.FA.FABookPeriodSetup.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.FA.FABookPeriodSetup.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.FA.FABookPeriodSetup.Descr : Edm.String "Description"
PX.Objects.FA.FABookPeriodSetup.tstamp : Edm.Binary
PX.Objects.FA.FABookPeriodSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABookPeriodSetup.CreatedByScreenID : Edm.String
PX.Objects.FA.FABookPeriodSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookPeriodSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABookPeriodSetup.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABookPeriodSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookPeriodSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABookPeriodSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABookPeriodSetup.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FABookPeriodSetup.FABookYearSetupByBookID -> PX.Objects.FA.FABookYearSetup (BookID=BookID)

# PX.Objects.FA.FABookSettings (EntityType)

Label: "FA Book Preferences"
Key: AssetID, BookID
Entity sets: PX_Objects_FA_FABookSettings, FABookPreferences, FABookSettings

PX.Objects.FA.FABookSettings.BookID : Edm.Int32 [key] "Book"
PX.Objects.FA.FABookSettings.AssetID : Edm.Int32 [key] "Asset Class"
PX.Objects.FA.FABookSettings.Depreciate : Edm.Boolean "Depreciable"
PX.Objects.FA.FABookSettings.UpdateGL : Edm.Boolean "Posting Book"
PX.Objects.FA.FABookSettings.DepreciationMethodID : Edm.Int32 "Class Method"
PX.Objects.FA.FABookSettings.MidMonthType : Edm.String "Mid-Period Type"
PX.Objects.FA.FABookSettings.MidMonthDay : Edm.Int16 "Mid-Period Day"
PX.Objects.FA.FABookSettings.Bonus : Edm.Boolean [required] "Bonus"
PX.Objects.FA.FABookSettings.Sect179 : Edm.Boolean [required] "Sect. 179"
PX.Objects.FA.FABookSettings.AveragingConvention : Edm.String "Averaging Convention"
PX.Objects.FA.FABookSettings.PercentPerYear : Edm.Decimal "Percent per Year"
PX.Objects.FA.FABookSettings.UsefulLife : Edm.Decimal "Useful Life, Years"
PX.Objects.FA.FABookSettings.tstamp : Edm.Binary
PX.Objects.FA.FABookSettings.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABookSettings.CreatedByScreenID : Edm.String
PX.Objects.FA.FABookSettings.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookSettings.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABookSettings.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABookSettings.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookSettings.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FABookSettings.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABookSettings.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABookSettings.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FABookSettings.FADepreciationMethodByDepreciationMethodID -> PX.Objects.FA.FADepreciationMethod (DepreciationMethodID=MethodID)
PX.Objects.FA.FABookSettings.FADepreciationMethodByUsefulLife -> PX.Objects.FA.FADepreciationMethod (DepreciationMethodID=MethodID, UsefulLife=UsefulLife)

# PX.Objects.FA.FABookYear (EntityType)

Label: "FA Book Year"
Key: BookID, OrganizationID, Year
Entity sets: PX_Objects_FA_FABookYear, FABookYear

PX.Objects.FA.FABookYear.BookID : Edm.Int32 [key] "Book"
PX.Objects.FA.FABookYear.OrganizationID : Edm.Int32 [key required]
PX.Objects.FA.FABookYear.Year : Edm.String [key required] "Financial Year"
PX.Objects.FA.FABookYear.StartMasterFinPeriodID : Edm.String "Start Master Period ID"
PX.Objects.FA.FABookYear.StartDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.FA.FABookYear.FinPeriods : Edm.Int16 [required] "Number of Periods"
PX.Objects.FA.FABookYear.EndDate : Edm.DateTimeOffset "EndDate"
PX.Objects.FA.FABookYear.tstamp : Edm.Binary
PX.Objects.FA.FABookYear.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABookYear.CreatedByScreenID : Edm.String
PX.Objects.FA.FABookYear.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookYear.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABookYear.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABookYear.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookYear.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABookYear.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABookYear.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization (OrganizationID=OrganizationID)
PX.Objects.FA.FABookYear.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FABookYear.FABookPeriodCollection -> Collection(PX.Objects.FA.FABookPeriod)

# PX.Objects.FA.FABookYearSetup (EntityType)

Label: "Book Calendar"
Key: BookID
Entity sets: PX_Objects_FA_FABookYearSetup, BookCalendar, FABookYearSetup
Non-filterable, non-selectable: NoteText, BelongsToNextYear

PX.Objects.FA.FABookYearSetup.BookID : Edm.Int32 [key] "Book"
PX.Objects.FA.FABookYearSetup.FirstFinYear : Edm.String "First Year"
PX.Objects.FA.FABookYearSetup.BegFinYear : Edm.DateTimeOffset "Year Starts On"
PX.Objects.FA.FABookYearSetup.FinPeriods : Edm.Int16 [required] "Number of Periods"
PX.Objects.FA.FABookYearSetup.UserDefined : Edm.Boolean "User-Defined Periods"
PX.Objects.FA.FABookYearSetup.NoteID : Edm.Guid
PX.Objects.FA.FABookYearSetup.NoteText : Edm.String "Note Text"
PX.Objects.FA.FABookYearSetup.PeriodType : Edm.String "Period Type"
PX.Objects.FA.FABookYearSetup.PeriodLength : Edm.Int16 "Length of Period(days)"
PX.Objects.FA.FABookYearSetup.PeriodsStartDate : Edm.DateTimeOffset "First Period Starts On"
PX.Objects.FA.FABookYearSetup.HasAdjustmentPeriod : Edm.Boolean [required] "Has Adjustment Period"
PX.Objects.FA.FABookYearSetup.EndYearCalcMethod : Edm.String "Year End Calculation Method"
PX.Objects.FA.FABookYearSetup.EndYearDayOfWeek : Edm.Int32 [required] "Day Of Week"
PX.Objects.FA.FABookYearSetup.tstamp : Edm.Binary
PX.Objects.FA.FABookYearSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FABookYearSetup.CreatedByScreenID : Edm.String
PX.Objects.FA.FABookYearSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookYearSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FABookYearSetup.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FABookYearSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FABookYearSetup.BelongsToNextYear : Edm.Boolean "Belongs To Next Year"
PX.Objects.FA.FABookYearSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FABookYearSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FABookYearSetup.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FABookYearSetup.FABookPeriodSetupCollection -> Collection(PX.Objects.FA.FABookPeriodSetup)

# PX.Objects.FA.FAClass (EntityType)

Label: "Asset Class"
BaseType: PX.Objects.FA.FixedAsset
Key: AssetCD (inherited from PX.Objects.FA.FixedAsset)
Entity sets: PX_Objects_FA_FAClass, AssetClass, FAClass

# PX.Objects.FA.FAComponent (EntityType)

Label: "FA Component"
BaseType: PX.Objects.FA.FixedAsset
Key: AssetCD (inherited from PX.Objects.FA.FixedAsset)
Entity sets: PX_Objects_FA_FAComponent, FAComponent

# PX.Objects.FA.FADepreciationMethod (EntityType)

Label: "Depreciation Method"
Key: MethodCD
Entity sets: PX_Objects_FA_FADepreciationMethod, DepreciationMethod, FADepreciationMethod
Non-filterable, non-selectable: DisplayTotalPercents, DepreciationPeriodsInYear, DepreciationStartDate, DepreciationStopDate, BookID, Source, NoteText

PX.Objects.FA.FADepreciationMethod.MethodID : Edm.Int32
PX.Objects.FA.FADepreciationMethod.Description : Edm.String "Description"
PX.Objects.FA.FADepreciationMethod.MethodCD : Edm.String [key] "Depreciation Method ID"
PX.Objects.FA.FADepreciationMethod.ParentMethodID : Edm.Int32 "Class Method"
PX.Objects.FA.FADepreciationMethod.DepreciationMethod : Edm.String "Calculation Method"
PX.Objects.FA.FADepreciationMethod.AveragingConvention : Edm.String "Averaging Convention"
PX.Objects.FA.FADepreciationMethod.RecoveryPeriod : Edm.Int32 "Recovery Period"
PX.Objects.FA.FADepreciationMethod.DisplayTotalPercents : Edm.Decimal "Total Percent"
PX.Objects.FA.FADepreciationMethod.TotalPercents : Edm.Decimal
PX.Objects.FA.FADepreciationMethod.AveragingConvPeriod : Edm.Int16 "Convention Period"
PX.Objects.FA.FADepreciationMethod.DepreciationPeriodsInYear : Edm.Int16 "Depreciation periods in Year"
PX.Objects.FA.FADepreciationMethod.DepreciationStartDate : Edm.DateTimeOffset "Depreciation Start Date"
PX.Objects.FA.FADepreciationMethod.DepreciationStopDate : Edm.DateTimeOffset "Depreciation Stop Date"
PX.Objects.FA.FADepreciationMethod.BookID : Edm.Int32 "Book"
PX.Objects.FA.FADepreciationMethod.RecordType : Edm.String "Record Type"
PX.Objects.FA.FADepreciationMethod.UsefulLife : Edm.Decimal "Useful Life, Years"
PX.Objects.FA.FADepreciationMethod.IsTableMethod : Edm.Boolean [required] "Is Table Method"
PX.Objects.FA.FADepreciationMethod.IsPredefined : Edm.Boolean [required]
PX.Objects.FA.FADepreciationMethod.Source : Edm.String "Source"
PX.Objects.FA.FADepreciationMethod.YearlyAccountancy : Edm.Boolean [required] "Yearly Accountancy"
PX.Objects.FA.FADepreciationMethod.DBMultiPlier : Edm.Decimal "DB Multiplier"
PX.Objects.FA.FADepreciationMethod.SwitchToSL : Edm.Boolean [required] "Switch to SL"
PX.Objects.FA.FADepreciationMethod.PercentPerYear : Edm.Decimal "Percent per Year"
PX.Objects.FA.FADepreciationMethod.NoteID : Edm.Guid
PX.Objects.FA.FADepreciationMethod.NoteText : Edm.String "Note Text"
PX.Objects.FA.FADepreciationMethod.tstamp : Edm.Binary
PX.Objects.FA.FADepreciationMethod.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FADepreciationMethod.CreatedByScreenID : Edm.String
PX.Objects.FA.FADepreciationMethod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FADepreciationMethod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FADepreciationMethod.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FADepreciationMethod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FADepreciationMethod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FADepreciationMethod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FADepreciationMethod.FADepreciationMethodByParentMethodID -> PX.Objects.FA.FADepreciationMethod (ParentMethodID=MethodID)
PX.Objects.FA.FADepreciationMethod.FABookBalanceCollection -> Collection(PX.Objects.FA.FABookBalance)
PX.Objects.FA.FADepreciationMethod.FABookSettingsCollection -> Collection(PX.Objects.FA.FABookSettings)
PX.Objects.FA.FADepreciationMethod.FADepreciationMethodCollection -> Collection(PX.Objects.FA.FADepreciationMethod)
PX.Objects.FA.FADepreciationMethod.FADepreciationMethodLinesCollection -> Collection(PX.Objects.FA.FADepreciationMethodLines)

# PX.Objects.FA.FADepreciationMethodLines (EntityType)

Label: "FA Depreciation Method Lines"
Key: MethodID, Year
Entity sets: PX_Objects_FA_FADepreciationMethodLines, FADepreciationMethodLines
Non-filterable, non-selectable: DisplayRatioPerYear, NoteText

PX.Objects.FA.FADepreciationMethodLines.MethodID : Edm.Int32 [key] "MethodID"
PX.Objects.FA.FADepreciationMethodLines.Year : Edm.Int32 [key] "Recovery Year"
PX.Objects.FA.FADepreciationMethodLines.DisplayRatioPerYear : Edm.Decimal "Percent per Year"
PX.Objects.FA.FADepreciationMethodLines.RatioPerYear : Edm.Decimal [required]
PX.Objects.FA.FADepreciationMethodLines.tstamp : Edm.Binary
PX.Objects.FA.FADepreciationMethodLines.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FADepreciationMethodLines.CreatedByScreenID : Edm.String
PX.Objects.FA.FADepreciationMethodLines.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FADepreciationMethodLines.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FADepreciationMethodLines.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FADepreciationMethodLines.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FADepreciationMethodLines.NoteID : Edm.Guid
PX.Objects.FA.FADepreciationMethodLines.NoteText : Edm.String "Note Text"
PX.Objects.FA.FADepreciationMethodLines.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FADepreciationMethodLines.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FADepreciationMethodLines.FADepreciationMethodByMethodID -> PX.Objects.FA.FADepreciationMethod (MethodID=MethodID)

# PX.Objects.FA.FADetails (EntityType)

Label: "FA Details"
Key: AssetID
Entity sets: PX_Objects_FA_FADetails, FADetails
Non-filterable, non-selectable: TransferPeriod, BaseCuryID, DisplayDisposalDate, DisplayDisposalPeriodID, DisplayDisposalMethodID, DisplaySaleAmount

PX.Objects.FA.FADetails.AssetID : Edm.Int32 [key] "AssetID"
PX.Objects.FA.FADetails.PropertyType : Edm.String "Property Type"
PX.Objects.FA.FADetails.Status : Edm.String "Status"
PX.Objects.FA.FADetails.Condition : Edm.String "Condition"
PX.Objects.FA.FADetails.ReceiptDate : Edm.DateTimeOffset "Receipt Date"
PX.Objects.FA.FADetails.ReceiptType : Edm.String "Receipt Type"
PX.Objects.FA.FADetails.ReceiptNbr : Edm.String "Receipt Nbr."
PX.Objects.FA.FADetails.PONumber : Edm.String "PO Number"
PX.Objects.FA.FADetails.BillNumber : Edm.String "Bill Number"
PX.Objects.FA.FADetails.Manufacturer : Edm.String "Manufacturer"
PX.Objects.FA.FADetails.Model : Edm.String "Model"
PX.Objects.FA.FADetails.SerialNumber : Edm.String "Serial Number"
PX.Objects.FA.FADetails.LocationRevID : Edm.Int32
PX.Objects.FA.FADetails.CurrentCost : Edm.Decimal "Basis"
PX.Objects.FA.FADetails.AccrualBalance : Edm.Decimal
PX.Objects.FA.FADetails.IsReconciled : Edm.Boolean
PX.Objects.FA.FADetails.TransferPeriod : Edm.String "Transfer Period"
PX.Objects.FA.FADetails.Barcode : Edm.String "Barcode"
PX.Objects.FA.FADetails.TagNbr : Edm.String "Tag Number"
PX.Objects.FA.FADetails.LastCountDate : Edm.DateTimeOffset "Last Count Date"
PX.Objects.FA.FADetails.DepreciateFromDate : Edm.DateTimeOffset "Placed-in-Service Date"
PX.Objects.FA.FADetails.AcquisitionCost : Edm.Decimal [required] "Orig. Acquisition Cost"
PX.Objects.FA.FADetails.SalvageAmount : Edm.Decimal [required] "Salvage Amount"
PX.Objects.FA.FADetails.ReplacementCost : Edm.Decimal "Replacement Cost"
PX.Objects.FA.FADetails.BaseCuryID : Edm.String "Currency"
PX.Objects.FA.FADetails.DisposalDate : Edm.DateTimeOffset "Disposal Date"
PX.Objects.FA.FADetails.DisplayDisposalDate : Edm.DateTimeOffset "Disposal Date"
PX.Objects.FA.FADetails.DisposalPeriodID : Edm.String
PX.Objects.FA.FADetails.DisplayDisposalPeriodID : Edm.String
PX.Objects.FA.FADetails.DisposalMethodID : Edm.Int32 "Disposal Method"
PX.Objects.FA.FADetails.DisplayDisposalMethodID : Edm.Int32 "Disposal Method"
PX.Objects.FA.FADetails.SaleAmount : Edm.Decimal "Disposal Amount"
PX.Objects.FA.FADetails.DisplaySaleAmount : Edm.Decimal "Disposal Amount"
PX.Objects.FA.FADetails.Warrantor : Edm.String "Warrantor"
PX.Objects.FA.FADetails.WarrantyExpirationDate : Edm.DateTimeOffset "Warranty Expires On"
PX.Objects.FA.FADetails.WarrantyCertificateNumber : Edm.String "Warranty Certificate Number"
PX.Objects.FA.FADetails.NextServiceDate : Edm.DateTimeOffset "Next Service Date"
PX.Objects.FA.FADetails.NextServiceValue : Edm.Decimal "Next Service Value"
PX.Objects.FA.FADetails.NextMeasurementUsageDate : Edm.DateTimeOffset "Next Measurement Date"
PX.Objects.FA.FADetails.LastServiceDate : Edm.DateTimeOffset "Last Service Date"
PX.Objects.FA.FADetails.LastServiceValue : Edm.Decimal "Last Service Value"
PX.Objects.FA.FADetails.LastMeasurementUsageDate : Edm.DateTimeOffset "Last Measurement Date"
PX.Objects.FA.FADetails.TotalExpectedUsage : Edm.Decimal "Total Expected Usage"
PX.Objects.FA.FADetails.FairMarketValue : Edm.Decimal "Fair Market Value"
PX.Objects.FA.FADetails.LessorID : Edm.Int32 "Lessor"
PX.Objects.FA.FADetails.LeaseRentTerm : Edm.Int32 "Lease/Rent Term, months"
PX.Objects.FA.FADetails.LeaseNumber : Edm.String "Lease Number"
PX.Objects.FA.FADetails.RentAmount : Edm.Decimal "Rent Amount"
PX.Objects.FA.FADetails.RetailCost : Edm.Decimal "Retail Cost"
PX.Objects.FA.FADetails.ManufacturingYear : Edm.String "Manufacturing Year"
PX.Objects.FA.FADetails.ReportingLineNbr : Edm.String "Personal Property Type"
PX.Objects.FA.FADetails.IsTemplate : Edm.Boolean [required] "Is Template"
PX.Objects.FA.FADetails.TemplateID : Edm.Int32 "Template"
PX.Objects.FA.FADetails.Hold : Edm.Boolean [required] "Hold"
PX.Objects.FA.FADetails.tstamp : Edm.Binary
PX.Objects.FA.FADetails.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FADetails.CreatedByScreenID : Edm.String
PX.Objects.FA.FADetails.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FADetails.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FADetails.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FADetails.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FADetails.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FADetails.FixedAssetByTemplateID -> PX.Objects.FA.FixedAsset (TemplateID=AssetID)
PX.Objects.FA.FADetails.BAccountByLessorID -> PX.Objects.CR.BAccount (LessorID=BAccountID)
PX.Objects.FA.FADetails.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FADetails.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FADetails.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.FA.FADetails.FADisposalMethodByDisposalMethodID -> PX.Objects.FA.FADisposalMethod (DisposalMethodID=DisposalMethodID)
PX.Objects.FA.FADetails.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)

# PX.Objects.FA.FADetailsTransfer (EntityType)

Label: "FA Details"
BaseType: PX.Objects.FA.FADetails
Key: AssetID (inherited from PX.Objects.FA.FADetails)
Entity sets: PX_Objects_FA_FADetailsTransfer, FADetails1, FADetailsTransfer

PX.Objects.FA.FADetailsTransfer.TransferPeriodID : Edm.String "Transfer Period"

# PX.Objects.FA.FADisposalMethod (EntityType)

Label: "FA Disposal Method"
Key: DisposalMethodCD
Entity sets: PX_Objects_FA_FADisposalMethod, FADisposalMethod

PX.Objects.FA.FADisposalMethod.DisposalMethodID : Edm.Int32 "DisposalMethodID"
PX.Objects.FA.FADisposalMethod.DisposalMethodCD : Edm.String [key] "Disposal Method ID"
PX.Objects.FA.FADisposalMethod.Description : Edm.String "Description"
PX.Objects.FA.FADisposalMethod.tstamp : Edm.Binary
PX.Objects.FA.FADisposalMethod.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FADisposalMethod.CreatedByScreenID : Edm.String
PX.Objects.FA.FADisposalMethod.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FADisposalMethod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FADisposalMethod.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FADisposalMethod.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FADisposalMethod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FADisposalMethod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FADisposalMethod.AccountByProceedsAcctID -> PX.Objects.GL.Account
PX.Objects.FA.FADisposalMethod.SubByProceedsSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FADisposalMethod.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)

# PX.Objects.FA.FAHistoryByPeriod (EntityType)

Label: "FA History by Period"
Key: AssetID, BookID, FinPeriodID
Entity sets: PX_Objects_FA_FAHistoryByPeriod, FAHistorybyPeriod

PX.Objects.FA.FAHistoryByPeriod.AssetID : Edm.Int32 [key]
PX.Objects.FA.FAHistoryByPeriod.BookID : Edm.Int32 [key]
PX.Objects.FA.FAHistoryByPeriod.FinPeriodID : Edm.String [key]
PX.Objects.FA.FAHistoryByPeriod.LastActivityPeriod : Edm.String
PX.Objects.FA.FAHistoryByPeriod.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FAHistoryByPeriod.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)

# PX.Objects.FA.FALocationHistory (EntityType)

Label: "FA Location History"
Key: AssetID, RevisionID
Entity sets: PX_Objects_FA_FALocationHistory, FALocationHistory

PX.Objects.FA.FALocationHistory.AssetID : Edm.Int32 [key] "AssetID"
PX.Objects.FA.FALocationHistory.TransactionType : Edm.String "Transaction Type"
PX.Objects.FA.FALocationHistory.TransactionDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.FA.FALocationHistory.PeriodID : Edm.String "Period ID"
PX.Objects.FA.FALocationHistory.ClassID : Edm.Int32 "Asset Class"
PX.Objects.FA.FALocationHistory.BuildingID : Edm.Int32 "Building"
PX.Objects.FA.FALocationHistory.Floor : Edm.String "Floor"
PX.Objects.FA.FALocationHistory.Room : Edm.String "Room"
PX.Objects.FA.FALocationHistory.EmployeeID : Edm.Int32 "Custodian"
PX.Objects.FA.FALocationHistory.Custodian : Edm.Guid
PX.Objects.FA.FALocationHistory.Department : Edm.String "Department"
PX.Objects.FA.FALocationHistory.RevisionID : Edm.Int32 [key required]
PX.Objects.FA.FALocationHistory.PrevRevisionID : Edm.Int32
PX.Objects.FA.FALocationHistory.RefNbr : Edm.String "Transfer Document Nbr."
PX.Objects.FA.FALocationHistory.Reason : Edm.String "Reason"
PX.Objects.FA.FALocationHistory.tstamp : Edm.Binary
PX.Objects.FA.FALocationHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FALocationHistory.CreatedByScreenID : Edm.String
PX.Objects.FA.FALocationHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FALocationHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FALocationHistory.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FALocationHistory.LastModifiedDateTime : Edm.DateTimeOffset "Modification Date"
PX.Objects.FA.FALocationHistory.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.FA.FALocationHistory.FixedAssetByClassID -> PX.Objects.FA.FixedAsset (ClassID=AssetID)
PX.Objects.FA.FALocationHistory.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FALocationHistory.BranchByLocationID -> PX.Objects.GL.Branch
PX.Objects.FA.FALocationHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FALocationHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FALocationHistory.AccountByFAAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FALocationHistory.AccountByAccumulatedDepreciationAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FALocationHistory.AccountByDepreciatedExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FALocationHistory.AccountByDisposalAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FALocationHistory.AccountByGainAcctID -> PX.Objects.GL.Account
PX.Objects.FA.FALocationHistory.AccountByLossAcctID -> PX.Objects.GL.Account
PX.Objects.FA.FALocationHistory.SubByFASubID -> PX.Objects.GL.Sub
PX.Objects.FA.FALocationHistory.SubByAccumulatedDepreciationSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FALocationHistory.SubByDepreciatedExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FALocationHistory.SubByDisposalSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FALocationHistory.SubByGainSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FALocationHistory.SubByLossSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FALocationHistory.BuildingByLocationID -> PX.Objects.CR.Building (BuildingID=BuildingID)
PX.Objects.FA.FALocationHistory.EPDepartmentByDepartment -> PX.Objects.EP.EPDepartment (Department=DepartmentID)

# PX.Objects.FA.FAOrganizationBook (EntityType)

Label: "FA Book"
BaseType: PX.Objects.FA.FABook
Key: BookCode (inherited from PX.Objects.FA.FABook)
Entity sets: PX_Objects_FA_FAOrganizationBook
Non-filterable, non-selectable: OrganizationID, FirstCalendarYear, LastCalendarYear

PX.Objects.FA.FAOrganizationBook.RawOrganizationID : Edm.Int32
PX.Objects.FA.FAOrganizationBook.OrganizationID : Edm.Int32
PX.Objects.FA.FAOrganizationBook.OrganizationCD : Edm.String "Company ID"
PX.Objects.FA.FAOrganizationBook.FirstCalendarYear : Edm.String "First Calendar Year"
PX.Objects.FA.FAOrganizationBook.LastCalendarYear : Edm.String "Last Calendar Year"

# PX.Objects.FA.FAProjectedGLTran (EntityType)

Label: "FA transactions in GL representation"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_FA_FAProjectedGLTran, FAtransactionsinGLrepresentation, FAProjectedGLTran

PX.Objects.FA.FAProjectedGLTran.RefNbr : Edm.String [key] "Reference Number"
PX.Objects.FA.FAProjectedGLTran.LineNbr : Edm.Int32 [key]
PX.Objects.FA.FAProjectedGLTran.AssetID : Edm.Int32 "Asset"
PX.Objects.FA.FAProjectedGLTran.BookID : Edm.Int32 "Book"
PX.Objects.FA.FAProjectedGLTran.FinPeriodID : Edm.String
PX.Objects.FA.FAProjectedGLTran.SignedAmt : Edm.Decimal
PX.Objects.FA.FAProjectedGLTran.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FAProjectedGLTran.BranchByGLBranchID -> PX.Objects.GL.Branch
PX.Objects.FA.FAProjectedGLTran.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FAProjectedGLTran.FARegisterByRefNbr -> PX.Objects.FA.FARegister (RefNbr=RefNbr)
PX.Objects.FA.FAProjectedGLTran.AccountByGLAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FAProjectedGLTran.SubByGLSubID -> PX.Objects.GL.Sub

# PX.Objects.FA.FARegister (EntityType)

Label: "Fixed Asset Transaction"
Key: RefNbr
Entity sets: PX_Objects_FA_FARegister, FixedAssetTransaction, FARegister
Non-filterable, non-selectable: NoteText, TranAmt

PX.Objects.FA.FARegister.RefNbr : Edm.String [key] "Reference Number"
PX.Objects.FA.FARegister.DocDate : Edm.DateTimeOffset "Document Date"
PX.Objects.FA.FARegister.FinPeriodID : Edm.String "Period ID"
PX.Objects.FA.FARegister.DocDesc : Edm.String "Description"
PX.Objects.FA.FARegister.LineCntr : Edm.Int32 [required]
PX.Objects.FA.FARegister.Status : Edm.String "Status"
PX.Objects.FA.FARegister.Origin : Edm.String "Origin"
PX.Objects.FA.FARegister.Released : Edm.Boolean [required] "Released"
PX.Objects.FA.FARegister.Hold : Edm.Boolean [required] "On Hold"
PX.Objects.FA.FARegister.Posted : Edm.Boolean [required]
PX.Objects.FA.FARegister.Reason : Edm.String "Reason"
PX.Objects.FA.FARegister.NoteID : Edm.Guid
PX.Objects.FA.FARegister.NoteText : Edm.String "Note Text"
PX.Objects.FA.FARegister.IsEmpty : Edm.Boolean "Empty"
PX.Objects.FA.FARegister.TranAmt : Edm.Decimal "Document Total"
PX.Objects.FA.FARegister.tstamp : Edm.Binary
PX.Objects.FA.FARegister.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FARegister.CreatedByScreenID : Edm.String
PX.Objects.FA.FARegister.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FA.FARegister.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FARegister.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FARegister.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FA.FARegister.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.FA.FARegister.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FARegister.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FARegister.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.FA.FARegister.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)

# PX.Objects.FA.FAService (EntityType)

Label: "FA Service"
Key: AssetID, ServiceNumber
Entity sets: PX_Objects_FA_FAService, FAService

PX.Objects.FA.FAService.AssetID : Edm.Int32 [key] "AssetID"
PX.Objects.FA.FAService.ServiceNumber : Edm.String [key] "Service Nbr."
PX.Objects.FA.FAService.ServiceDate : Edm.DateTimeOffset "Service Date"
PX.Objects.FA.FAService.ScheduledDate : Edm.DateTimeOffset "Scheduled Date"
PX.Objects.FA.FAService.PerfomedBy : Edm.Guid "Perfomed By"
PX.Objects.FA.FAService.InspectedBy : Edm.Guid "Inspected By"
PX.Objects.FA.FAService.Description : Edm.String "Description"
PX.Objects.FA.FAService.ServiceAmount : Edm.Decimal [required] "Service Amount"
PX.Objects.FA.FAService.VendorID : Edm.Int32 "Vendor"
PX.Objects.FA.FAService.BillNumber : Edm.String "Bill Number"
PX.Objects.FA.FAService.Completed : Edm.Boolean [required] "Completed"
PX.Objects.FA.FAService.tstamp : Edm.Binary
PX.Objects.FA.FAService.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FAService.CreatedByScreenID : Edm.String
PX.Objects.FA.FAService.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAService.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FAService.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FAService.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAService.EPEmployeeByPerfomedBy -> PX.Objects.EP.EPEmployee (PerfomedBy=UserID)
PX.Objects.FA.FAService.EPEmployeeByInspectedBy -> PX.Objects.EP.EPEmployee (InspectedBy=UserID)
PX.Objects.FA.FAService.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.FA.FAService.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FAService.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.FA.FAService.APRegisterByVendorID -> PX.Objects.AP.APRegister (BillNumber=RefNbr, VendorID=VendorID)
PX.Objects.FA.FAService.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FAService.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FA.FAServiceSchedule (EntityType)

Label: "FA Service Schedule"
Key: ScheduleCD
Entity sets: PX_Objects_FA_FAServiceSchedule, FAServiceSchedule

PX.Objects.FA.FAServiceSchedule.ScheduleCD : Edm.String [key] "Schedule ID"
PX.Objects.FA.FAServiceSchedule.Description : Edm.String "Description"
PX.Objects.FA.FAServiceSchedule.ServiceEveryValue : Edm.Int32 "Service Every"
PX.Objects.FA.FAServiceSchedule.ServiceEveryPeriod : Edm.String
PX.Objects.FA.FAServiceSchedule.ServiceAfterUsageValue : Edm.Decimal "Service after Usage"
PX.Objects.FA.FAServiceSchedule.ServiceAfterUsageUOM : Edm.String "UOM"
PX.Objects.FA.FAServiceSchedule.ScheduleID : Edm.Int32 "ScheduleID"
PX.Objects.FA.FAServiceSchedule.tstamp : Edm.Binary
PX.Objects.FA.FAServiceSchedule.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FAServiceSchedule.CreatedByScreenID : Edm.String
PX.Objects.FA.FAServiceSchedule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAServiceSchedule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FAServiceSchedule.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FAServiceSchedule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAServiceSchedule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FAServiceSchedule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FAServiceSchedule.INUnitByServiceAfterUsageUOM -> PX.Objects.IN.INUnit (ServiceAfterUsageUOM=FromUnit)
PX.Objects.FA.FAServiceSchedule.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)

# PX.Objects.FA.FASetup (EntityType)

Label: "Fixed Assets Preferences"
Singletons: PX_Objects_FA_FASetup, FixedAssetsPreferences, FASetup

PX.Objects.FA.FASetup.RegisterNumberingID : Edm.String "Transaction Numbering Sequence"
PX.Objects.FA.FASetup.AssetNumberingID : Edm.String "Asset Numbering Sequence"
PX.Objects.FA.FASetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.FA.FASetup.TagNumberingID : Edm.String "Tag Numbering Sequence"
PX.Objects.FA.FASetup.CopyTagFromAssetID : Edm.Boolean [required] "Copy Tag Number from Asset ID"
PX.Objects.FA.FASetup.AutoPost : Edm.Boolean [required] "Automatically Post on Release"
PX.Objects.FA.FASetup.AutoReleaseAsset : Edm.Boolean [required] "Automatically Release Acquisition Transactions"
PX.Objects.FA.FASetup.AutoReleaseDepr : Edm.Boolean [required] "Automatically Release Depreciation Transactions"
PX.Objects.FA.FASetup.AutoReleaseDisp : Edm.Boolean [required] "Automatically Release Disposal Transactions"
PX.Objects.FA.FASetup.AutoReleaseTransfer : Edm.Boolean [required] "Automatically Release Transfer Transactions"
PX.Objects.FA.FASetup.AutoReleaseReversal : Edm.Boolean [required] "Automatically Release Reversal Transactions"
PX.Objects.FA.FASetup.AutoReleaseSplit : Edm.Boolean [required] "Automatically Release Split Transactions"
PX.Objects.FA.FASetup.UpdateGL : Edm.Boolean [required] "Update GL"
PX.Objects.FA.FASetup.DeprHistoryView : Edm.String "Depreciation History View"
PX.Objects.FA.FASetup.ShowSideBySide : Edm.Boolean "ShowSideBySide"
PX.Objects.FA.FASetup.ShowBookSheet : Edm.Boolean "ShowBookSheet"
PX.Objects.FA.FASetup.SummPost : Edm.Boolean [required] "Post Summary on Updating GL"
PX.Objects.FA.FASetup.SummPostDepreciation : Edm.Boolean "Post Depreciation Summary on Updating GL"
PX.Objects.FA.FASetup.DepreciateInDisposalPeriod : Edm.Boolean [required] "Depreciate in Disposal Period"
PX.Objects.FA.FASetup.AccurateDepreciation : Edm.Boolean [required] "Show Accurate Depreciation"
PX.Objects.FA.FASetup.ReconcileBeforeDisposal : Edm.Boolean [required] "Require Full Reconciliation before Disposal"
PX.Objects.FA.FASetup.AllowEditPredefinedDeprMethod : Edm.Boolean [required] "Allow to Modify Predefined Depreciation Methods"
PX.Objects.FA.FASetup.AllowMultipleMethodsMode : Edm.Boolean [required] "Allow Multiple Depreciation Methods"
PX.Objects.FA.FASetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FASetup.CreatedByScreenID : Edm.String
PX.Objects.FA.FASetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FASetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FASetup.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FASetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FASetup.tstamp : Edm.Binary
PX.Objects.FA.FASetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FASetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FASetup.NumberingByRegisterNumberingID -> PX.Objects.CS.Numbering (RegisterNumberingID=NumberingID)
PX.Objects.FA.FASetup.NumberingByAssetNumberingID -> PX.Objects.CS.Numbering (AssetNumberingID=NumberingID)
PX.Objects.FA.FASetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.FA.FASetup.NumberingByTagNumberingID -> PX.Objects.CS.Numbering (TagNumberingID=NumberingID)
PX.Objects.FA.FASetup.AccountByFAAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.FA.FASetup.AccountByProceedsAcctID -> PX.Objects.GL.Account
PX.Objects.FA.FASetup.SubByFAAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FASetup.SubByProceedsSubID -> PX.Objects.GL.Sub

# PX.Objects.FA.FATran (EntityType)

Label: "Fixed Asset Transaction"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_FA_FATran, FixedAssetTransaction1, FATran
Non-filterable, non-selectable: ReceiptDate, DeprFromDate, ClassID, TargetAssetID, EmployeeID, Department, NewAsset, Component, NoteText, AssetCD, Depreciable

PX.Objects.FA.FATran.RefNbr : Edm.String [key] "Reference Number"
PX.Objects.FA.FATran.LineNbr : Edm.Int32 [key]
PX.Objects.FA.FATran.AssetID : Edm.Int32 "Asset"
PX.Objects.FA.FATran.BookID : Edm.Int32 "Book"
PX.Objects.FA.FATran.ReceiptDate : Edm.DateTimeOffset "Receipt Date"
PX.Objects.FA.FATran.DeprFromDate : Edm.DateTimeOffset "Placed-in-Service Date"
PX.Objects.FA.FATran.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.FA.FATran.FinPeriodID : Edm.String "Tran. Period"
PX.Objects.FA.FATran.TranPeriodID : Edm.String
PX.Objects.FA.FATran.TranType : Edm.String "Transaction Type"
PX.Objects.FA.FATran.TranAmt : Edm.Decimal [required] "Transaction Amount"
PX.Objects.FA.FATran.RGOLAmt : Edm.Decimal [required] "RGOL Amount"
PX.Objects.FA.FATran.MethodDesc : Edm.String "Method"
PX.Objects.FA.FATran.TranDesc : Edm.String "Transaction Description"
PX.Objects.FA.FATran.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.FA.FATran.Released : Edm.Boolean [required] "Released"
PX.Objects.FA.FATran.Posted : Edm.Boolean [required]
PX.Objects.FA.FATran.Origin : Edm.String "Origin"
PX.Objects.FA.FATran.ClassID : Edm.Int32
PX.Objects.FA.FATran.TargetAssetID : Edm.Int32
PX.Objects.FA.FATran.EmployeeID : Edm.Int32
PX.Objects.FA.FATran.Department : Edm.String
PX.Objects.FA.FATran.NewAsset : Edm.Boolean "Create Asset"
PX.Objects.FA.FATran.Component : Edm.Boolean "Component"
PX.Objects.FA.FATran.GLTranID : Edm.Int32
PX.Objects.FA.FATran.TranID : Edm.Int32
PX.Objects.FA.FATran.NoteID : Edm.Guid
PX.Objects.FA.FATran.NoteText : Edm.String "Note Text"
PX.Objects.FA.FATran.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.FA.FATran.AssetCD : Edm.String "Asset ID"
PX.Objects.FA.FATran.Depreciable : Edm.Boolean
PX.Objects.FA.FATran.ReclassificationOnDebitProhibited : Edm.Boolean "Reclassification on Debit Is Prohibited"
PX.Objects.FA.FATran.ReclassificationOnCreditProhibited : Edm.Boolean "Reclassification on credit prohibited"
PX.Objects.FA.FATran.tstamp : Edm.Binary
PX.Objects.FA.FATran.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FATran.CreatedByScreenID : Edm.String
PX.Objects.FA.FATran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FATran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FATran.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FATran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FATran.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FATran.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.FA.FATran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.FA.FATran.BranchByGLtranID -> PX.Objects.GL.Branch
PX.Objects.FA.FATran.BranchBySrcBranchID -> PX.Objects.GL.Branch
PX.Objects.FA.FATran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FATran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FATran.FAAccrualTranByGLtranID -> PX.Objects.FA.FAAccrualTran
PX.Objects.FA.FATran.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.FATran.FARegisterByRefNbr -> PX.Objects.FA.FARegister (RefNbr=RefNbr)
PX.Objects.FA.FATran.AccountByDebitAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FATran.AccountByCreditAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FATran.SubByDebitSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FATran.SubByCreditSubID -> PX.Objects.GL.Sub

# PX.Objects.FA.FAType (EntityType)

Label: "FA Type"
Key: AssetTypeID
Entity sets: PX_Objects_FA_FAType, FAType

PX.Objects.FA.FAType.AssetTypeID : Edm.String [key] "Asset Type ID"
PX.Objects.FA.FAType.Description : Edm.String "Description"
PX.Objects.FA.FAType.IsTangible : Edm.Boolean [required] "Tangible"
PX.Objects.FA.FAType.Depreciable : Edm.Boolean [required] "Depreciable"
PX.Objects.FA.FAType.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)

# PX.Objects.FA.FAUsage (EntityType)

Label: "FA Usage"
Key: AssetID, Number
Entity sets: PX_Objects_FA_FAUsage, FAUsage

PX.Objects.FA.FAUsage.AssetID : Edm.Int32 [key] "AssetID"
PX.Objects.FA.FAUsage.Number : Edm.Int32 [key] "Number"
PX.Objects.FA.FAUsage.MeasurementDate : Edm.DateTimeOffset "Measurement Date"
PX.Objects.FA.FAUsage.ScheduledDate : Edm.DateTimeOffset "Scheduled Date"
PX.Objects.FA.FAUsage.MeasuredBy : Edm.Guid "Measured By"
PX.Objects.FA.FAUsage.Value : Edm.Decimal "Value"
PX.Objects.FA.FAUsage.Difference : Edm.Decimal [required] "Difference with Previos Measurement Value"
PX.Objects.FA.FAUsage.DepreciationPercent : Edm.Decimal "Depreciation Rate"
PX.Objects.FA.FAUsage.UsageUOM : Edm.String "UOM"
PX.Objects.FA.FAUsage.Depreciated : Edm.Boolean [required] "Depreciated"
PX.Objects.FA.FAUsage.tstamp : Edm.Binary
PX.Objects.FA.FAUsage.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FAUsage.CreatedByScreenID : Edm.String
PX.Objects.FA.FAUsage.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAUsage.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FAUsage.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FAUsage.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAUsage.EPEmployeeByMeasuredBy -> PX.Objects.EP.EPEmployee (MeasuredBy=UserID)
PX.Objects.FA.FAUsage.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.FAUsage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FAUsage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FAUsage.FADetailsByAssetID -> PX.Objects.FA.FADetails (AssetID=AssetID)

# PX.Objects.FA.FAUsageSchedule (EntityType)

Label: "FA Usage Schedule"
Key: ScheduleCD
Entity sets: PX_Objects_FA_FAUsageSchedule, FAUsageSchedule

PX.Objects.FA.FAUsageSchedule.ScheduleID : Edm.Int32 "ScheduleID"
PX.Objects.FA.FAUsageSchedule.Description : Edm.String "Description"
PX.Objects.FA.FAUsageSchedule.ScheduleCD : Edm.String [key] "Schedule ID"
PX.Objects.FA.FAUsageSchedule.ReadUsageEveryValue : Edm.Int32 [required] "Read Every"
PX.Objects.FA.FAUsageSchedule.ReadUsageEveryPeriod : Edm.String "Interval"
PX.Objects.FA.FAUsageSchedule.UsageUOM : Edm.String "UOM"
PX.Objects.FA.FAUsageSchedule.tstamp : Edm.Binary
PX.Objects.FA.FAUsageSchedule.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FAUsageSchedule.CreatedByScreenID : Edm.String
PX.Objects.FA.FAUsageSchedule.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAUsageSchedule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FAUsageSchedule.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FAUsageSchedule.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.FAUsageSchedule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FAUsageSchedule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FAUsageSchedule.INUnitByUsageUOM -> PX.Objects.IN.INUnit (UsageUOM=FromUnit)
PX.Objects.FA.FAUsageSchedule.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)

# PX.Objects.FA.FixedAsset (EntityType)

Label: "Fixed Asset"
Key: AssetCD
Entity sets: PX_Objects_FA_FixedAsset, FixedAsset
Non-filterable, non-selectable: NoteText, DisposalAmt, SalvageAmtAfterSplit

PX.Objects.FA.FixedAsset.RecordType : Edm.String "Record Type"
PX.Objects.FA.FixedAsset.AssetCD : Edm.String [key] "Asset ID"
PX.Objects.FA.FixedAsset.Description : Edm.String "Description"
PX.Objects.FA.FixedAsset.ParentAssetID : Edm.Int32 "Parent Asset"
PX.Objects.FA.FixedAsset.AssetTypeID : Edm.String "Asset Type"
PX.Objects.FA.FixedAsset.ClassID : Edm.Int32 "Asset Class"
PX.Objects.FA.FixedAsset.AssetID : Edm.Int32 "AssetID"
PX.Objects.FA.FixedAsset.BaseCuryID : Edm.String "Currency"
PX.Objects.FA.FixedAsset.OldClassID : Edm.Int32
PX.Objects.FA.FixedAsset.Status : Edm.String "Status"
PX.Objects.FA.FixedAsset.FASubMask : Edm.String
PX.Objects.FA.FixedAsset.AccumDeprSubMask : Edm.String
PX.Objects.FA.FixedAsset.DeprExpenceSubMask : Edm.String
PX.Objects.FA.FixedAsset.ProceedsSubMask : Edm.String
PX.Objects.FA.FixedAsset.GainLossSubMask : Edm.String
PX.Objects.FA.FixedAsset.Depreciable : Edm.Boolean "Depreciable"
PX.Objects.FA.FixedAsset.UnderConstruction : Edm.Boolean "Under Construction"
PX.Objects.FA.FixedAsset.UsefulLife : Edm.Decimal "Useful Life, Years"
PX.Objects.FA.FixedAsset.IsTangible : Edm.Boolean [required] "Tangible"
PX.Objects.FA.FixedAsset.Active : Edm.Boolean [required] "Active"
PX.Objects.FA.FixedAsset.IsAcquired : Edm.Boolean
PX.Objects.FA.FixedAsset.Suspended : Edm.Boolean [required] "Suspended"
PX.Objects.FA.FixedAsset.HoldEntry : Edm.Boolean [required] "Hold on Entry"
PX.Objects.FA.FixedAsset.AcceleratedDepreciation : Edm.Boolean [required] "Accelerated Depreciation for SL Depr. Method"
PX.Objects.FA.FixedAsset.ServiceScheduleID : Edm.Int32 "Service Schedule"
PX.Objects.FA.FixedAsset.UsageScheduleID : Edm.Int32 "Usage Measurement Schedule"
PX.Objects.FA.FixedAsset.NoteID : Edm.Guid
PX.Objects.FA.FixedAsset.NoteText : Edm.String "Note Text"
PX.Objects.FA.FixedAsset.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.FA.FixedAsset.SplittedFrom : Edm.Int32
PX.Objects.FA.FixedAsset.DisposalAmt : Edm.Decimal "Proceeds Amount"
PX.Objects.FA.FixedAsset.SalvageAmtAfterSplit : Edm.Decimal
PX.Objects.FA.FixedAsset.tstamp : Edm.Binary
PX.Objects.FA.FixedAsset.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.FixedAsset.CreatedByScreenID : Edm.String
PX.Objects.FA.FixedAsset.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FA.FixedAsset.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.FixedAsset.LastModifiedByScreenID : Edm.String
PX.Objects.FA.FixedAsset.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FA.FixedAsset.FixedAssetByClassID -> PX.Objects.FA.FixedAsset (ClassID=AssetID)
PX.Objects.FA.FixedAsset.FixedAssetByParentAssetID -> PX.Objects.FA.FixedAsset (ParentAssetID=AssetID)
PX.Objects.FA.FixedAsset.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.FA.FixedAsset.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.FixedAsset.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.FixedAsset.FAServiceScheduleByServiceScheduleID -> PX.Objects.FA.FAServiceSchedule (ServiceScheduleID=ScheduleID)
PX.Objects.FA.FixedAsset.FAUsageScheduleByUsageScheduleID -> PX.Objects.FA.FAUsageSchedule (UsageScheduleID=ScheduleID)
PX.Objects.FA.FixedAsset.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)
PX.Objects.FA.FixedAsset.AccountByConstructionAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByFAAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByFAAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByAccumulatedDepreciationAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByDepreciatedExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByDisposalAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByRentAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByLeaseAccountID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByGainAcctID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.AccountByLossAcctID -> PX.Objects.GL.Account
PX.Objects.FA.FixedAsset.SubByConstructionSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByFASubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByFAAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByAccumulatedDepreciationSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByDepreciatedExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByDisposalSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByRentSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByLeaseSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByGainSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.SubByLossSubID -> PX.Objects.GL.Sub
PX.Objects.FA.FixedAsset.FATypeByAssetTypeID -> PX.Objects.FA.FAType (AssetTypeID=AssetTypeID)
PX.Objects.FA.FixedAsset.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.FA.FixedAsset.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.FA.FixedAsset.FABookBalanceCollection -> Collection(PX.Objects.FA.FABookBalance)
PX.Objects.FA.FixedAsset.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.FA.FixedAsset.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)
PX.Objects.FA.FixedAsset.FABookHistoryCollection -> Collection(PX.Objects.FA.FABookHistory)
PX.Objects.FA.FixedAsset.FAApplicableMethodCollection -> Collection(PX.Objects.FA.FAApplicableMethod)
PX.Objects.FA.FixedAsset.FABookSettingsCollection -> Collection(PX.Objects.FA.FABookSettings)
PX.Objects.FA.FixedAsset.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.FA.FixedAsset.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)
PX.Objects.FA.FixedAsset.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.FA.FixedAsset.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.Objects.FA.FixedAsset.FAHistoryByPeriodCollection -> Collection(PX.Objects.FA.FAHistoryByPeriod)
PX.Objects.FA.FixedAsset.FALocationHistoryByPeriodCollection -> Collection(PX.Objects.FA.DAC.FALocationHistoryByPeriod)

# PX.Objects.FA.Overrides.AssetProcess.FABookHist (EntityType)

Label: "FA Book History"
BaseType: PX.Objects.FA.FABookHistory
Key: AssetID, BookID, FinPeriodID (inherited from PX.Objects.FA.FABookHistory)
Entity sets: PX_Objects_FA_Overrides_AssetProcess_FABookHist

# PX.Objects.FA.SplitParams (EntityType)

Label: "Fixed Asset"
BaseType: PX.Objects.FA.FixedAsset
Key: AssetCD (inherited from PX.Objects.FA.FixedAsset)
Entity sets: PX_Objects_FA_SplitParams
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FA.SplitParams.SplitID : Edm.Int32
PX.Objects.FA.SplitParams.SplittedAssetCD : Edm.String "Asset ID"
PX.Objects.FA.SplitParams.Cost : Edm.Decimal "Cost"
PX.Objects.FA.SplitParams.SplittedQty : Edm.Decimal "Quantity"
PX.Objects.FA.SplitParams.Ratio : Edm.Decimal "Ratio"

# PX.Objects.FA.Standalone.FABookBalance (EntityType)

Key: AssetID, BookID
Entity sets: PX_Objects_FA_Standalone_FABookBalance

PX.Objects.FA.Standalone.FABookBalance.AssetID : Edm.Int32 [key]
PX.Objects.FA.Standalone.FABookBalance.BookID : Edm.Int32 [key]
PX.Objects.FA.Standalone.FABookBalance.LastDeprPeriod : Edm.String
PX.Objects.FA.Standalone.FABookBalance.CurrDeprPeriod : Edm.String
PX.Objects.FA.Standalone.FABookBalance.FixedAssetByClassID -> PX.Objects.FA.FixedAsset
PX.Objects.FA.Standalone.FABookBalance.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.Standalone.FABookBalance.UsersByCreatedByID -> PX.SM.Users
PX.Objects.FA.Standalone.FABookBalance.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.FA.Standalone.FABookBalance.FABonusByBonusID -> PX.Objects.FA.FABonus
PX.Objects.FA.Standalone.FABookBalance.FABookByBookID -> PX.Objects.FA.FABook (BookID=BookID)
PX.Objects.FA.Standalone.FABookBalance.FADepreciationMethodByUsefulLife -> PX.Objects.FA.FADepreciationMethod
PX.Objects.FA.Standalone.FABookBalance.FAApplicableMethodCollection -> Collection(PX.Objects.FA.FAApplicableMethod)

# PX.Objects.FA.Standalone.FADetails (EntityType)

Label: "FA Details"
Key: AssetID
Entity sets: PX_Objects_FA_Standalone_FADetails, FADetails2
Non-filterable, non-selectable: DisplayDisposalDate, DisplayDisposalPeriodID, DisplayDisposalMethodID, DisplaySaleAmount

PX.Objects.FA.Standalone.FADetails.AssetID : Edm.Int32 [key] "AssetID"
PX.Objects.FA.Standalone.FADetails.PropertyType : Edm.String "Property Type"
PX.Objects.FA.Standalone.FADetails.Status : Edm.String "Status"
PX.Objects.FA.Standalone.FADetails.Condition : Edm.String "Condition"
PX.Objects.FA.Standalone.FADetails.ReceiptDate : Edm.DateTimeOffset "Receipt Date"
PX.Objects.FA.Standalone.FADetails.ReceiptType : Edm.String "Receipt Type"
PX.Objects.FA.Standalone.FADetails.ReceiptNbr : Edm.String "Receipt Nbr."
PX.Objects.FA.Standalone.FADetails.PONumber : Edm.String "PO Number"
PX.Objects.FA.Standalone.FADetails.BillNumber : Edm.String "Bill Number"
PX.Objects.FA.Standalone.FADetails.Manufacturer : Edm.String "Manufacturer"
PX.Objects.FA.Standalone.FADetails.Model : Edm.String "Model"
PX.Objects.FA.Standalone.FADetails.SerialNumber : Edm.String "Serial Number"
PX.Objects.FA.Standalone.FADetails.LocationRevID : Edm.Int32
PX.Objects.FA.Standalone.FADetails.Barcode : Edm.String "Barcode"
PX.Objects.FA.Standalone.FADetails.TagNbr : Edm.String "Tag Number"
PX.Objects.FA.Standalone.FADetails.DepreciateFromDate : Edm.DateTimeOffset "Placed-in-Service Date"
PX.Objects.FA.Standalone.FADetails.AcquisitionCost : Edm.Decimal [required] "Orig. Acquisition Cost"
PX.Objects.FA.Standalone.FADetails.SalvageAmount : Edm.Decimal [required] "Salvage Amount"
PX.Objects.FA.Standalone.FADetails.ReplacementCost : Edm.Decimal "Replacement Cost"
PX.Objects.FA.Standalone.FADetails.DisposalDate : Edm.DateTimeOffset "Disposal Date"
PX.Objects.FA.Standalone.FADetails.DisplayDisposalDate : Edm.DateTimeOffset "Disposal Date"
PX.Objects.FA.Standalone.FADetails.DisposalPeriodID : Edm.String
PX.Objects.FA.Standalone.FADetails.DisplayDisposalPeriodID : Edm.String
PX.Objects.FA.Standalone.FADetails.DisposalMethodID : Edm.Int32 "Disposal Method"
PX.Objects.FA.Standalone.FADetails.DisplayDisposalMethodID : Edm.Int32 "Disposal Method"
PX.Objects.FA.Standalone.FADetails.SaleAmount : Edm.Decimal "Disposal Amount"
PX.Objects.FA.Standalone.FADetails.DisplaySaleAmount : Edm.Decimal "Disposal Amount"
PX.Objects.FA.Standalone.FADetails.Warrantor : Edm.String "Warrantor"
PX.Objects.FA.Standalone.FADetails.WarrantyExpirationDate : Edm.DateTimeOffset "Warranty Expires On"
PX.Objects.FA.Standalone.FADetails.WarrantyCertificateNumber : Edm.String "Warranty Certificate Number"
PX.Objects.FA.Standalone.FADetails.Hold : Edm.Boolean [required] "Hold"
PX.Objects.FA.Standalone.FADetails.tstamp : Edm.Binary
PX.Objects.FA.Standalone.FADetails.CreatedByID : Edm.Guid "Created By"
PX.Objects.FA.Standalone.FADetails.CreatedByScreenID : Edm.String
PX.Objects.FA.Standalone.FADetails.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FA.Standalone.FADetails.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FA.Standalone.FADetails.LastModifiedByScreenID : Edm.String
PX.Objects.FA.Standalone.FADetails.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FA.Standalone.FADetails.FixedAssetByAssetID -> PX.Objects.FA.FixedAsset (AssetID=AssetID)
PX.Objects.FA.Standalone.FADetails.FixedAssetByTemplateID -> PX.Objects.FA.FixedAsset
PX.Objects.FA.Standalone.FADetails.BAccountByLessorID -> PX.Objects.CR.BAccount
PX.Objects.FA.Standalone.FADetails.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FA.Standalone.FADetails.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FA.Standalone.FADetails.POReceiptByReceiptNbr -> PX.Objects.PO.POReceipt (ReceiptType=ReceiptType, ReceiptNbr=ReceiptNbr)
PX.Objects.FA.Standalone.FADetails.FADisposalMethodByDisposalMethodID -> PX.Objects.FA.FADisposalMethod (DisposalMethodID=DisposalMethodID)
PX.Objects.FA.Standalone.FADetails.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)

# PX.Objects.FA.Transact (EntityType)

Label: "Fixed Asset Transaction"
BaseType: PX.Objects.FA.FATran
Key: LineNbr, RefNbr (inherited from PX.Objects.FA.FATran)
Entity sets: PX_Objects_FA_Transact
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FA.Transact.DebitAmt : Edm.Decimal "Debit"
PX.Objects.FA.Transact.CreditAmt : Edm.Decimal "Credit"

# PX.Objects.FS.ActiveSchedule (EntityType)

BaseType: PX.Objects.FS.FSSchedule
Key: CustomerID, RefNbr (inherited from PX.Objects.FS.FSSchedule)
Entity sets: PX_Objects_FS_ActiveSchedule
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FS.ActiveSchedule.ChangeRecurrence : Edm.Boolean "Change Recurrence"
PX.Objects.FS.ActiveSchedule.EffectiveRecurrenceStartDate : Edm.DateTimeOffset "Effective Recurrence Start Date"
PX.Objects.FS.ActiveSchedule.NextExecution : Edm.DateTimeOffset "Next Execution"

# PX.Objects.FS.AppointmentBoxComponentField (EntityType)

BaseType: PX.Objects.FS.FSCalendarComponentField
Key: ComponentType, FieldName, ObjectName (inherited from PX.Objects.FS.FSCalendarComponentField)
Entity sets: PX_Objects_FS_AppointmentBoxComponentField

# PX.Objects.FS.AppointmentToPost (EntityType)

Label: "Appointment"
BaseType: PX.Objects.FS.FSAppointment
Key: RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSAppointment)
Entity sets: PX_Objects_FS_AppointmentToPost
Non-filterable, non-selectable: RowIndex, GroupKey, BatchID, ErrorFlag

PX.Objects.FS.AppointmentToPost.PostTo : Edm.String "Post To"
PX.Objects.FS.AppointmentToPost.PostOrderType : Edm.String
PX.Objects.FS.AppointmentToPost.PostOrderTypeNegativeBalance : Edm.String
PX.Objects.FS.AppointmentToPost.PostNegBalanceToAP : Edm.Boolean "Create a Bill Document in AP for Negative Balances"
PX.Objects.FS.AppointmentToPost.DfltTermIDARSO : Edm.String
PX.Objects.FS.AppointmentToPost.BillingCycleID : Edm.Int32 "Billing Cycle ID"
PX.Objects.FS.AppointmentToPost.FrequencyType : Edm.String "Frequency Type"
PX.Objects.FS.AppointmentToPost.WeeklyFrequency : Edm.Int32 "Frequency Week Day"
PX.Objects.FS.AppointmentToPost.MonthlyFrequency : Edm.Int32 "Frequency Month Day"
PX.Objects.FS.AppointmentToPost.SendInvoicesTo : Edm.String "Send Invoices to"
PX.Objects.FS.AppointmentToPost.BillingBy : Edm.String
PX.Objects.FS.AppointmentToPost.GroupBillByLocations : Edm.Boolean "Create Separate Invoices for Customer Locations"
PX.Objects.FS.AppointmentToPost.BranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.AppointmentToPost.ServiceOrderStatus : Edm.String "Status"
PX.Objects.FS.AppointmentToPost.CustWorkOrderRefNbr : Edm.String "Customer Work Order Ref. Nbr."
PX.Objects.FS.AppointmentToPost.CustPORefNbr : Edm.String "Customer Purchase Order Ref. Nbr."
PX.Objects.FS.AppointmentToPost.PostedBy : Edm.String
PX.Objects.FS.AppointmentToPost.BillingCycleCD : Edm.String "Billing Cycle ID"
PX.Objects.FS.AppointmentToPost.BillingCycleType : Edm.String
PX.Objects.FS.AppointmentToPost.InvoiceOnlyCompletedServiceOrder : Edm.Boolean "Invoice only completed or closed Service Orders"
PX.Objects.FS.AppointmentToPost.TimeCycleType : Edm.String "Time Cycle Type"
PX.Objects.FS.AppointmentToPost.TimeCycleWeekDay : Edm.Int32 "Day of Week"
PX.Objects.FS.AppointmentToPost.TimeCycleDayOfMonth : Edm.Int32 "Day of Month"
PX.Objects.FS.AppointmentToPost.ProjectID : Edm.Int32 "Project ID"
PX.Objects.FS.AppointmentToPost.DocType : Edm.String
PX.Objects.FS.AppointmentToPost.RowIndex : Edm.Int32
PX.Objects.FS.AppointmentToPost.GroupKey : Edm.String
PX.Objects.FS.AppointmentToPost.BatchID : Edm.Int32 "Batch Nbr."
PX.Objects.FS.AppointmentToPost.ErrorFlag : Edm.Boolean
PX.Objects.FS.AppointmentToPost.SOOrderTypeByPostOrderType -> PX.Objects.SO.SOOrderType (PostOrderType=OrderType)
PX.Objects.FS.AppointmentToPost.SOOrderTypeByPostOrderTypeNegativeBalance -> PX.Objects.SO.SOOrderType (PostOrderTypeNegativeBalance=OrderType)
PX.Objects.FS.AppointmentToPost.TermsByDfltTermIDARSO -> PX.Objects.CS.Terms (DfltTermIDARSO=TermsID)
PX.Objects.FS.AppointmentToPost.LocationByBillLocationID -> PX.Objects.CR.Location (BillCustomerID=BAccountID)
PX.Objects.FS.AppointmentToPost.FSBillingCycleByBillingCycleID -> PX.Objects.FS.FSBillingCycle (BillingCycleID=BillingCycleID)
PX.Objects.FS.AppointmentToPost.FSBillingCycleByBillingCycleCD -> PX.Objects.FS.FSBillingCycle (BillingCycleCD=BillingCycleCD)
PX.Objects.FS.AppointmentToPost.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.AppointmentToPost.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.AppointmentToPost.SOOrderTypeByAllocationOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.FS.AppointmentToPost.TermsByDfltTermIDAP -> PX.Objects.CS.Terms
PX.Objects.FS.AppointmentToPost.AppointmentToPostCollection -> Collection(PX.Objects.FS.AppointmentToPost)
PX.Objects.FS.AppointmentToPost.ServiceOrderToPostCollection -> Collection(PX.Objects.FS.ServiceOrderToPost)

# PX.Objects.FS.BAccountLocation (EntityType)

Key: CustomerID, LocationID
Entity sets: PX_Objects_FS_BAccountLocation

PX.Objects.FS.BAccountLocation.CustomerID : Edm.Int32 [key] "Customer"
PX.Objects.FS.BAccountLocation.LocationID : Edm.Int32 [key] "Location"
PX.Objects.FS.BAccountLocation.Descr : Edm.String "Location Name"
PX.Objects.FS.BAccountLocation.CustomerCD : Edm.String "Customer ID"
PX.Objects.FS.BAccountLocation.IsActive : Edm.Boolean "Active"
PX.Objects.FS.BAccountLocation.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.FS.BAccountLocation.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.BAccountLocation.LocationByLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID, LocationID=LocationID)
PX.Objects.FS.BAccountLocation.LocationByCustomerID -> PX.Objects.CR.Location (LocationID=LocationID, CustomerID=BAccountID)
PX.Objects.FS.BAccountLocation.BAccountByBAccountID -> PX.Objects.CR.BAccount
PX.Objects.FS.BAccountLocation.FSAppointmentInRouteCollection -> Collection(PX.Objects.FS.FSAppointmentInRoute)
PX.Objects.FS.BAccountLocation.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.FS.BAccountLocation.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.FS.BAccountLocation.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.FS.BAccountLocation.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.FS.BAccountLocation.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.FS.BAccountLocation.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.FS.BAccountLocation.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.BAccountLocation.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.FS.BAccountLocation.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.FS.BAccountLocation.APDiscountLocationCollection -> Collection(PX.Objects.AP.APDiscountLocation)
PX.Objects.FS.BAccountLocation.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.Objects.FS.BAccountLocation.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.Objects.FS.BAccountLocation.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.FS.BAccountLocation.BCRoleAssignmentCollection -> Collection(PX.Commerce.Shopify.BCRoleAssignment)
PX.Objects.FS.BAccountLocation.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.FS.BAccountLocation.AMBomOperCuryCollection -> Collection(PX.Objects.AM.AMBomOperCury)

# PX.Objects.FS.BAccountSelectorBase (EntityType)

Label: "Business Account"
BaseType: PX.Objects.CR.BAccount
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_FS_BAccountSelectorBase

# PX.Objects.FS.BAccountStaffMember (EntityType)

Label: "Business Account"
BaseType: PX.Objects.FS.BAccountSelectorBase
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_FS_BAccountStaffMember

# PX.Objects.FS.ContractPeriodToPost (EntityType)

Key: ContractPeriodID, ServiceContractID
Entity sets: PX_Objects_FS_ContractPeriodToPost
Non-filterable, non-selectable: ContractPostBatchID, BillingPeriod

PX.Objects.FS.ContractPeriodToPost.CustomerID : Edm.Int32
PX.Objects.FS.ContractPeriodToPost.RefNbr : Edm.String "Service Contract ID"
PX.Objects.FS.ContractPeriodToPost.CustomerContractNbr : Edm.String "Customer Contract Nbr."
PX.Objects.FS.ContractPeriodToPost.ServiceContractID : Edm.Int32 [key]
PX.Objects.FS.ContractPeriodToPost.BillCustomerID : Edm.Int32 "Billing Customer"
PX.Objects.FS.ContractPeriodToPost.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.ContractPeriodToPost.BranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.ContractPeriodToPost.BillingType : Edm.String "Billing Type"
PX.Objects.FS.ContractPeriodToPost.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.FS.ContractPeriodToPost.Status : Edm.String "Status"
PX.Objects.FS.ContractPeriodToPost.DocDesc : Edm.String "Description"
PX.Objects.FS.ContractPeriodToPost.EndPeriodDate : Edm.DateTimeOffset
PX.Objects.FS.ContractPeriodToPost.StartPeriodDate : Edm.DateTimeOffset
PX.Objects.FS.ContractPeriodToPost.NextBillingInvoiceDate : Edm.DateTimeOffset "Next Billing Date"
PX.Objects.FS.ContractPeriodToPost.ContractPeriodID : Edm.Int32 [key]
PX.Objects.FS.ContractPeriodToPost.ContractPostBatchID : Edm.Int32 "Batch Nbr."
PX.Objects.FS.ContractPeriodToPost.BillingPeriod : Edm.String "Billing Period"
PX.Objects.FS.ContractPeriodToPost.NoteID : Edm.Guid
PX.Objects.FS.ContractPeriodToPost.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.ContractPeriodToPost.CustomerByBillCustomerID -> PX.Objects.AR.Customer (BillCustomerID=BAccountID)
PX.Objects.FS.ContractPeriodToPost.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.ContractPeriodToPost.LocationByBillLocationID -> PX.Objects.CR.Location (BillCustomerID=BAccountID)
PX.Objects.FS.ContractPeriodToPost.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.ContractPeriodToPost.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.ContractPeriodToPost.FSContractPeriodByContractPeriodID -> PX.Objects.FS.FSContractPeriod (ContractPeriodID=ContractPeriodID)
PX.Objects.FS.ContractPeriodToPost.FSServiceContractByRefNbr -> PX.Objects.FS.FSServiceContract (RefNbr=RefNbr)
PX.Objects.FS.ContractPeriodToPost.FSServiceContractByCustomerID -> PX.Objects.FS.FSServiceContract (RefNbr=RefNbr, CustomerID=CustomerID)
PX.Objects.FS.ContractPeriodToPost.FSRouteContractScheduleFSServiceContractCollection -> Collection(PX.Objects.FS.FSRouteContractScheduleFSServiceContract)
PX.Objects.FS.ContractPeriodToPost.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.FS.ContractPeriodToPost.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.ContractPeriodToPost.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.ContractPeriodToPost.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.Objects.FS.ContractPeriodToPost.FSContractActionCollection -> Collection(PX.Objects.FS.FSContractAction)
PX.Objects.FS.ContractPeriodToPost.FSContractPeriodCollection -> Collection(PX.Objects.FS.FSContractPeriod)
PX.Objects.FS.ContractPeriodToPost.FSContractPostDocCollection -> Collection(PX.Objects.FS.FSContractPostDoc)
PX.Objects.FS.ContractPeriodToPost.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.FS.ContractPeriodToPost.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.FS.ContractPeriodToPost.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.FS.ContractPeriodToPost.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.FS.ContractPeriodToPost.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)

# PX.Objects.FS.ContractPostBatchDetail (EntityType)

Key: ContractPostBatchID, ContractPostDocID
Entity sets: PX_Objects_FS_ContractPostBatchDetail
Non-filterable, non-selectable: ContractRefNbr, CustomerContractNbr, AcctName

PX.Objects.FS.ContractPostBatchDetail.ContractPostDocID : Edm.Int32 [key] "Contract Post Doc. ID"
PX.Objects.FS.ContractPostBatchDetail.ContractPostBatchID : Edm.Int32 [key] "Contract Post Batch ID"
PX.Objects.FS.ContractPostBatchDetail.PostedTO : Edm.String "Posted to"
PX.Objects.FS.ContractPostBatchDetail.PostRefNbr : Edm.String "Document Nbr."
PX.Objects.FS.ContractPostBatchDetail.PostDocType : Edm.String "Document Type"
PX.Objects.FS.ContractPostBatchDetail.ContractRefNbr : Edm.String "Service Contract ID"
PX.Objects.FS.ContractPostBatchDetail.CustomerContractNbr : Edm.String "Customer Contract Nbr."
PX.Objects.FS.ContractPostBatchDetail.ServiceContractID : Edm.Int32
PX.Objects.FS.ContractPostBatchDetail.BillCustomerID : Edm.Int32 "Billing Customer ID"
PX.Objects.FS.ContractPostBatchDetail.AcctName : Edm.String "Customer Name"
PX.Objects.FS.ContractPostBatchDetail.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.FS.ContractPostBatchDetail.NextBillingInvoiceDate : Edm.DateTimeOffset "Next Billing Date"
PX.Objects.FS.ContractPostBatchDetail.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.ContractPostBatchDetail.BranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.ContractPostBatchDetail.DocDesc : Edm.String "Description"
PX.Objects.FS.ContractPostBatchDetail.CustomerByBillCustomerID -> PX.Objects.AR.Customer (BillCustomerID=BAccountID)
PX.Objects.FS.ContractPostBatchDetail.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.ContractPostBatchDetail.LocationByBillLocationID -> PX.Objects.CR.Location (BillCustomerID=BAccountID)
PX.Objects.FS.ContractPostBatchDetail.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.ContractPostBatchDetail.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.ContractPostBatchDetail.FSContractPostBatchByContractPostBatchID -> PX.Objects.FS.FSContractPostBatch (ContractPostBatchID=ContractPostBatchID)
PX.Objects.FS.ContractPostBatchDetail.FSContractPostDocByContractPostDocID -> PX.Objects.FS.FSContractPostDoc (ContractPostDocID=ContractPostDocID)
PX.Objects.FS.ContractPostBatchDetail.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID)
PX.Objects.FS.ContractPostBatchDetail.CustomerByCustomerID -> PX.Objects.AR.Customer
PX.Objects.FS.ContractPostBatchDetail.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.FS.ContractPostBatchDetail.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.FS.ContractPostBatchDetail.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.ContractPostBatchDetail.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.ContractPostBatchDetail.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.Objects.FS.ContractPostBatchDetail.FSContractActionCollection -> Collection(PX.Objects.FS.FSContractAction)
PX.Objects.FS.ContractPostBatchDetail.FSContractPeriodCollection -> Collection(PX.Objects.FS.FSContractPeriod)
PX.Objects.FS.ContractPostBatchDetail.FSContractPostDocCollection -> Collection(PX.Objects.FS.FSContractPostDoc)
PX.Objects.FS.ContractPostBatchDetail.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.FS.ContractPostBatchDetail.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)

# PX.Objects.FS.EPEmployeeFSRouteEmployee (EntityType)

Label: "Employee"
BaseType: PX.Objects.EP.EPEmployee
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_FS_EPEmployeeFSRouteEmployee
Non-filterable, non-selectable: MemDriverName

PX.Objects.FS.EPEmployeeFSRouteEmployee.RouteID : Edm.Int32
PX.Objects.FS.EPEmployeeFSRouteEmployee.PriorityPreference : Edm.Int32 "Priority Preference"
PX.Objects.FS.EPEmployeeFSRouteEmployee.MemDriverName : Edm.String "Driver Name"
PX.Objects.FS.EPEmployeeFSRouteEmployee.FSRouteByRouteID -> PX.Objects.FS.FSRoute (RouteID=RouteID)

# PX.Objects.FS.FSAddress (EntityType)

Label: "Field Service Address"
Key: AddressID
Entity sets: PX_Objects_FS_FSAddress, FieldServiceAddress, FSAddress
Non-filterable, non-selectable: OverrideAddress, FullAddress

PX.Objects.FS.FSAddress.AddressID : Edm.Int32 [key] "Address ID"
PX.Objects.FS.FSAddress.EntityType : Edm.String "Entity Type"
PX.Objects.FS.FSAddress.BAccountID : Edm.Int32
PX.Objects.FS.FSAddress.BAccountAddressID : Edm.Int32
PX.Objects.FS.FSAddress.IsDefaultAddress : Edm.Boolean "Default Customer Address"
PX.Objects.FS.FSAddress.OverrideAddress : Edm.Boolean "Override Address"
PX.Objects.FS.FSAddress.RevisionID : Edm.Int32
PX.Objects.FS.FSAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.FS.FSAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.FS.FSAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.FS.FSAddress.City : Edm.String "City"
PX.Objects.FS.FSAddress.CountryID : Edm.String "Country"
PX.Objects.FS.FSAddress.State : Edm.String "State"
PX.Objects.FS.FSAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.FS.FSAddress.Department : Edm.String "Department"
PX.Objects.FS.FSAddress.SubDepartment : Edm.String "Subdepartment"
PX.Objects.FS.FSAddress.StreetName : Edm.String "Street Name"
PX.Objects.FS.FSAddress.BuildingNumber : Edm.String "Building Number"
PX.Objects.FS.FSAddress.BuildingName : Edm.String "Building Name"
PX.Objects.FS.FSAddress.Floor : Edm.String "Floor"
PX.Objects.FS.FSAddress.UnitNumber : Edm.String "Unit Number"
PX.Objects.FS.FSAddress.PostBox : Edm.String "Post Box"
PX.Objects.FS.FSAddress.Room : Edm.String "Room"
PX.Objects.FS.FSAddress.TownLocationName : Edm.String "Town Location Name"
PX.Objects.FS.FSAddress.DistrictName : Edm.String "District Name"
PX.Objects.FS.FSAddress.AddressType : Edm.String "Address Type"
PX.Objects.FS.FSAddress.CareOf : Edm.String "Care Of"
PX.Objects.FS.FSAddress.NoteID : Edm.Guid
PX.Objects.FS.FSAddress.tstamp : Edm.Binary
PX.Objects.FS.FSAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSAddress.CreatedByScreenID : Edm.String
PX.Objects.FS.FSAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSAddress.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAddress.Latitude : Edm.Decimal "Latitude"
PX.Objects.FS.FSAddress.Longitude : Edm.Decimal "Longitude"
PX.Objects.FS.FSAddress.FullAddress : Edm.String "Address"
PX.Objects.FS.FSAddress.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.FS.FSAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.FS.FSAddress.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.FS.FSAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.FS.FSAddress.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSAddress.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.FS.FSAddress.FSManufacturerCollection -> Collection(PX.Objects.FS.FSManufacturer)

# PX.Objects.FS.FSAdjust (EntityType)

Key: AdjdOrderNbr, AdjdOrderType, AdjgDocType, AdjgRefNbr
Entity sets: PX_Objects_FS_FSAdjust
Non-filterable, non-selectable: CuryAdjgDiscAmt, CuryAdjdDiscAmt, AdjDiscAmt, CuryDocBal, DocBal, NoteText, SOCuryCompletedBillableTotal, AdjdOrigCuryID, CuryRate, CuryViewState, AdjdCuryID

PX.Objects.FS.FSAdjust.Hold : Edm.Boolean [required]
PX.Objects.FS.FSAdjust.CustomerID : Edm.Int32
PX.Objects.FS.FSAdjust.AdjgDocType : Edm.String [key] "Doc. Type"
PX.Objects.FS.FSAdjust.AdjgRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.FS.FSAdjust.AdjdOrderType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAdjust.AdjdOrderNbr : Edm.String [key] "Service Order Nbr."
PX.Objects.FS.FSAdjust.CuryAdjgAmt : Edm.Decimal [required] "Applied To Order"
PX.Objects.FS.FSAdjust.AdjAmt : Edm.Decimal [required]
PX.Objects.FS.FSAdjust.CuryAdjdAmt : Edm.Decimal [required]
PX.Objects.FS.FSAdjust.CuryOrigAdjdAmt : Edm.Decimal
PX.Objects.FS.FSAdjust.OrigAdjAmt : Edm.Decimal
PX.Objects.FS.FSAdjust.CuryOrigAdjgAmt : Edm.Decimal
PX.Objects.FS.FSAdjust.CuryAdjgDiscAmt : Edm.Decimal
PX.Objects.FS.FSAdjust.CuryAdjdDiscAmt : Edm.Decimal
PX.Objects.FS.FSAdjust.AdjDiscAmt : Edm.Decimal
PX.Objects.FS.FSAdjust.AdjdOrigCuryInfoID : Edm.Int64
PX.Objects.FS.FSAdjust.AdjgCuryInfoID : Edm.Int64
PX.Objects.FS.FSAdjust.AdjdCuryInfoID : Edm.Int64
PX.Objects.FS.FSAdjust.AdjgDocDate : Edm.DateTimeOffset
PX.Objects.FS.FSAdjust.AdjdOrderDate : Edm.DateTimeOffset "Date"
PX.Objects.FS.FSAdjust.CuryAdjgBilledAmt : Edm.Decimal [required] "Transferred to Invoice"
PX.Objects.FS.FSAdjust.AdjBilledAmt : Edm.Decimal [required]
PX.Objects.FS.FSAdjust.CuryAdjdBilledAmt : Edm.Decimal [required] "Transferred to Invoice"
PX.Objects.FS.FSAdjust.CuryDocBal : Edm.Decimal "Balance"
PX.Objects.FS.FSAdjust.DocBal : Edm.Decimal
PX.Objects.FS.FSAdjust.Voided : Edm.Boolean [required]
PX.Objects.FS.FSAdjust.NoteID : Edm.Guid
PX.Objects.FS.FSAdjust.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSAdjust.tstamp : Edm.Binary
PX.Objects.FS.FSAdjust.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSAdjust.CreatedByScreenID : Edm.String
PX.Objects.FS.FSAdjust.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAdjust.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSAdjust.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSAdjust.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAdjust.SOCuryCompletedBillableTotal : Edm.Decimal "Service Order Billable Total"
PX.Objects.FS.FSAdjust.AdjdAppRefNbr : Edm.String "Source Appointment Nbr."
PX.Objects.FS.FSAdjust.AdjdOrigCuryID : Edm.String "Currency"
PX.Objects.FS.FSAdjust.CuryRate : Edm.Decimal
PX.Objects.FS.FSAdjust.CuryViewState : Edm.Boolean
PX.Objects.FS.FSAdjust.AdjdCuryID : Edm.String "Currency"
PX.Objects.FS.FSAdjust.ARPaymentByAdjgRefNbr -> PX.Objects.AR.ARPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.FS.FSAdjust.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAdjust.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSAdjust.FSServiceOrderByAdjdOrderNbr -> PX.Objects.FS.FSServiceOrder (AdjdOrderType=SrvOrdType, AdjdOrderNbr=RefNbr)
PX.Objects.FS.FSAdjust.FSServiceOrderByAdjdOrderType -> PX.Objects.FS.FSServiceOrder (AdjdOrderNbr=RefNbr, CustomerID=CustomerID, AdjdOrderType=SrvOrdType)
PX.Objects.FS.FSAdjust.FSSrvOrdTypeByAdjdOrderType -> PX.Objects.FS.FSSrvOrdType (AdjdOrderType=SrvOrdType)

# PX.Objects.FS.FSAppointment (EntityType)

Label: "Appointment"
Key: RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSAppointment, Appointment, FSAppointment
Non-filterable, non-selectable: SrvOrdTypeCode, BillCustomerID, UserConfirmedUnclosing, StartActionRunning, PauseActionRunning, ResumeActionRunning, CompleteActionRunning, CloseActionRunning, UnCloseActionRunning, CancelActionRunning, ReopenActionRunning, ReloadServiceOrderRelated, AreActualFieldsActive, EffDocDate, NoteText, ProfitPercent, ProfitMarginPercent, CuryLineDocDiscountTotal, DocDisc, CuryDocDisc, SkipExternalTaxCalculation, AppCompletedBillableTotal, IntTravelInProcess, isBeingCloned, ScheduledDuration, ActualDuration, ScheduledDateBegin, IsRouteAppoinment, IsPrepaymentEnable, IsReassigned, ActualDurationTotalReport, AppointmentRefReport, IsCalledFromQuickProcess, IsPosted, TravelCanBeStarted, TravelCanBeCompleted, MustUpdateServiceOrder, FormCaptionDescription, IsINReleaseProcess, TrackTimeChanged, CuryActualBillableTotal, ActualBillableTotal, EditActionRunning, CuryRate

PX.Objects.FS.FSAppointment.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSAppointment.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointment.SrvOrdTypeCode : Edm.String
PX.Objects.FS.FSAppointment.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointment.AppointmentID : Edm.Int32
PX.Objects.FS.FSAppointment.WorkflowTypeID : Edm.String "Workflow Type"
PX.Objects.FS.FSAppointment.SORefNbr : Edm.String "Service Order Nbr."
PX.Objects.FS.FSAppointment.SOID : Edm.Int32
PX.Objects.FS.FSAppointment.CustomerID : Edm.Int32 "Customer"
PX.Objects.FS.FSAppointment.BillCustomerID : Edm.Int32 "Billing Customer"
PX.Objects.FS.FSAppointment.DocDesc : Edm.String "Description"
PX.Objects.FS.FSAppointment.ScheduledDateTimeBegin : Edm.DateTimeOffset "Scheduled Start Date"
PX.Objects.FS.FSAppointment.HandleManuallyScheduleTime : Edm.Boolean [required] "Handle Manually"
PX.Objects.FS.FSAppointment.ScheduledDateTimeEnd : Edm.DateTimeOffset "Scheduled End Date"
PX.Objects.FS.FSAppointment.ExecutionDate : Edm.DateTimeOffset "Actual Start Date"
PX.Objects.FS.FSAppointment.ActualDateTimeBegin : Edm.DateTimeOffset "Actual Start Date"
PX.Objects.FS.FSAppointment.HandleManuallyActualTime : Edm.Boolean [required] "Handle Manually"
PX.Objects.FS.FSAppointment.ActualDateTimeEnd : Edm.DateTimeOffset "Actual End Date"
PX.Objects.FS.FSAppointment.CuryID : Edm.String "Currency"
PX.Objects.FS.FSAppointment.CuryInfoID : Edm.Int64
PX.Objects.FS.FSAppointment.AutoDocDesc : Edm.String "Service Description"
PX.Objects.FS.FSAppointment.Confirmed : Edm.Boolean [required] "Confirmed"
PX.Objects.FS.FSAppointment.DeliveryNotes : Edm.String "Delivery Notes"
PX.Objects.FS.FSAppointment.LongDescr : Edm.String "Description"
PX.Objects.FS.FSAppointment.NotStarted : Edm.Boolean [required] "Not Started"
PX.Objects.FS.FSAppointment.Hold : Edm.Boolean [required] "Hold"
PX.Objects.FS.FSAppointment.Awaiting : Edm.Boolean [required] "Awaiting"
PX.Objects.FS.FSAppointment.InProcess : Edm.Boolean [required] "In Process"
PX.Objects.FS.FSAppointment.Paused : Edm.Boolean [required] "Paused"
PX.Objects.FS.FSAppointment.Completed : Edm.Boolean [required] "Completed"
PX.Objects.FS.FSAppointment.Closed : Edm.Boolean [required] "Closed"
PX.Objects.FS.FSAppointment.Canceled : Edm.Boolean [required] "Canceled"
PX.Objects.FS.FSAppointment.Billed : Edm.Boolean [required] "Billed"
PX.Objects.FS.FSAppointment.GeneratedByContract : Edm.Boolean [required] "Generated by Contract"
PX.Objects.FS.FSAppointment.UserConfirmedUnclosing : Edm.Boolean
PX.Objects.FS.FSAppointment.StartActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.PauseActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.ResumeActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.CompleteActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.CloseActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.UnCloseActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.CancelActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.ReopenActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.ReloadServiceOrderRelated : Edm.Boolean
PX.Objects.FS.FSAppointment.Status : Edm.String "Status"
PX.Objects.FS.FSAppointment.AreActualFieldsActive : Edm.Boolean
PX.Objects.FS.FSAppointment.EffDocDate : Edm.DateTimeOffset "Effective Document Date"
PX.Objects.FS.FSAppointment.LineCntr : Edm.Int32 [required]
PX.Objects.FS.FSAppointment.SplitLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSAppointment.LogLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSAppointment.EmployeeLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSAppointment.PendingPOLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSAppointment.PendingApptPOLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSAppointment.APBillLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSAppointment.StaffCntr : Edm.Int32 [required]
PX.Objects.FS.FSAppointment.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSAppointment.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSAppointment.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSAppointment.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSAppointment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSAppointment.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSAppointment.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSAppointment.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSAppointment.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSAppointment.EstimatedDurationTotal : Edm.Int32 [required] "Estimated Duration"
PX.Objects.FS.FSAppointment.ActualDurationTotal : Edm.Int32 [required] "Actual Duration"
PX.Objects.FS.FSAppointment.DriveTime : Edm.Int32 "Driving Time"
PX.Objects.FS.FSAppointment.MapLatitude : Edm.Decimal "Latitude"
PX.Objects.FS.FSAppointment.MapLongitude : Edm.Decimal "Longitude"
PX.Objects.FS.FSAppointment.RoutePosition : Edm.Int32 "Route Position"
PX.Objects.FS.FSAppointment.TimeLocked : Edm.Boolean [required] "Time Locked"
PX.Objects.FS.FSAppointment.OriginalAppointmentID : Edm.Int32 "Original Appointment ID"
PX.Objects.FS.FSAppointment.UnreachedCustomer : Edm.Boolean [required] "Unreached Customer"
PX.Objects.FS.FSAppointment.RouteID : Edm.Int32 "Route ID"
PX.Objects.FS.FSAppointment.RouteDocumentID : Edm.Int32 "Route Nbr."
PX.Objects.FS.FSAppointment.ValidatedByDispatcher : Edm.Boolean [required] "Validated by Dispatcher"
PX.Objects.FS.FSAppointment.GenerationID : Edm.Int32 "Generation ID"
PX.Objects.FS.FSAppointment.FinPeriodID : Edm.String "Post Period"
PX.Objects.FS.FSAppointment.WFStageID : Edm.Int32 "Workflow Stage"
PX.Objects.FS.FSAppointment.TimeRegistered : Edm.Boolean [required] "Approved Staff Times"
PX.Objects.FS.FSAppointment.customerSignaturePath : Edm.String "Customer Signature"
PX.Objects.FS.FSAppointment.CustomerSignedReport : Edm.Guid "Signed Report ID"
PX.Objects.FS.FSAppointment.FullNameSignature : Edm.String "Full Name"
PX.Objects.FS.FSAppointment.SalesPersonID : Edm.Int32 "Salesperson"
PX.Objects.FS.FSAppointment.Commissionable : Edm.Boolean "Commissionable"
PX.Objects.FS.FSAppointment.PendingAPARSOPost : Edm.Boolean [required]
PX.Objects.FS.FSAppointment.PendingINPost : Edm.Boolean [required]
PX.Objects.FS.FSAppointment.PostingStatusAPARSO : Edm.String "PostingStatusAPARSO"
PX.Objects.FS.FSAppointment.PostingStatusIN : Edm.String "PostingStatusIN"
PX.Objects.FS.FSAppointment.CutOffDate : Edm.DateTimeOffset "Cut-Off Date"
PX.Objects.FS.FSAppointment.GPSLatitudeStart : Edm.Decimal "Latitude"
PX.Objects.FS.FSAppointment.GPSLongitudeStart : Edm.Decimal "Longitude"
PX.Objects.FS.FSAppointment.GPSLatitudeComplete : Edm.Decimal "Latitude"
PX.Objects.FS.FSAppointment.GPSLongitudeComplete : Edm.Decimal "Longitude"
PX.Objects.FS.FSAppointment.EstimatedLineTotal : Edm.Decimal "Base Estimated Total"
PX.Objects.FS.FSAppointment.CuryEstimatedLineTotal : Edm.Decimal "Estimated Total"
PX.Objects.FS.FSAppointment.EstimatedCostTotal : Edm.Decimal "EstimatedCostTotal"
PX.Objects.FS.FSAppointment.CuryEstimatedCostTotal : Edm.Decimal "Estimated Cost Total"
PX.Objects.FS.FSAppointment.LineTotal : Edm.Decimal [required] "Base Ext. Price Total"
PX.Objects.FS.FSAppointment.CuryLineTotal : Edm.Decimal "Ext. Price Total"
PX.Objects.FS.FSAppointment.LogBillableTranAmountTotal : Edm.Decimal [required] "Base Billable Labor Total"
PX.Objects.FS.FSAppointment.CuryLogBillableTranAmountTotal : Edm.Decimal [required] "Billable Labor Total"
PX.Objects.FS.FSAppointment.BillableLineTotal : Edm.Decimal "Base Billable Total"
PX.Objects.FS.FSAppointment.CuryBillableLineTotal : Edm.Decimal "Actual Billable Total"
PX.Objects.FS.FSAppointment.BillContractPeriodID : Edm.Int32 "Contract Period"
PX.Objects.FS.FSAppointment.CuryCostTotal : Edm.Decimal [required] "Cost Total"
PX.Objects.FS.FSAppointment.CostTotal : Edm.Decimal [required] "CostTotal"
PX.Objects.FS.FSAppointment.ProfitPercent : Edm.Decimal "Profit Markup (%)"
PX.Objects.FS.FSAppointment.ProfitMarginPercent : Edm.Decimal "Profit Margin (%)"
PX.Objects.FS.FSAppointment.CuryVatExemptTotal : Edm.Decimal [required] "VAT Exempt Total"
PX.Objects.FS.FSAppointment.VatExemptTotal : Edm.Decimal [required]
PX.Objects.FS.FSAppointment.CuryVatTaxableTotal : Edm.Decimal [required] "VAT Taxable Total"
PX.Objects.FS.FSAppointment.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.FS.FSAppointment.TaxZoneID : Edm.String "Customer Tax Zone"
PX.Objects.FS.FSAppointment.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.FS.FSAppointment.TaxTotal : Edm.Decimal [required]
PX.Objects.FS.FSAppointment.CuryTaxTotal : Edm.Decimal [required] "Actual Tax Total"
PX.Objects.FS.FSAppointment.DiscTot : Edm.Decimal [required] "Discount Total"
PX.Objects.FS.FSAppointment.CuryDiscTot : Edm.Decimal [required] "Discount Total"
PX.Objects.FS.FSAppointment.DocTotal : Edm.Decimal "Base Order Total"
PX.Objects.FS.FSAppointment.CuryDocTotal : Edm.Decimal [required] "Invoice Total"
PX.Objects.FS.FSAppointment.CuryLineDocDiscountTotal : Edm.Decimal "CuryLineDocDiscountTotal"
PX.Objects.FS.FSAppointment.DocDisc : Edm.Decimal
PX.Objects.FS.FSAppointment.CuryDocDisc : Edm.Decimal "Document Discount"
PX.Objects.FS.FSAppointment.SkipExternalTaxCalculation : Edm.Boolean "Skip External Tax Calculation"
PX.Objects.FS.FSAppointment.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.FS.FSAppointment.MinLogTimeBegin : Edm.DateTimeOffset "Min Log Time Begin"
PX.Objects.FS.FSAppointment.MaxLogTimeEnd : Edm.DateTimeOffset "Max Log Time End"
PX.Objects.FS.FSAppointment.Finished : Edm.Boolean "Finished"
PX.Objects.FS.FSAppointment.AppCompletedBillableTotal : Edm.Decimal "Appointment Billable Total"
PX.Objects.FS.FSAppointment.IntTravelInProcess : Edm.Int32
PX.Objects.FS.FSAppointment.TravelInProcess : Edm.Boolean [required] "Travel in Process"
PX.Objects.FS.FSAppointment.MaxLineNbr : Edm.Int32
PX.Objects.FS.FSAppointment.isBeingCloned : Edm.Boolean
PX.Objects.FS.FSAppointment.ScheduledDuration : Edm.Int32 "Scheduled Duration"
PX.Objects.FS.FSAppointment.ActualDuration : Edm.Int32 "Actual Duration"
PX.Objects.FS.FSAppointment.ScheduledDateBegin : Edm.DateTimeOffset
PX.Objects.FS.FSAppointment.IsRouteAppoinment : Edm.Boolean "IsRouteAppoinment"
PX.Objects.FS.FSAppointment.IsPrepaymentEnable : Edm.Boolean "IsPrepaymentEnable"
PX.Objects.FS.FSAppointment.IsReassigned : Edm.Boolean
PX.Objects.FS.FSAppointment.ActualDurationTotalReport : Edm.Int32
PX.Objects.FS.FSAppointment.AppointmentRefReport : Edm.Int32
PX.Objects.FS.FSAppointment.ActualDateTimeBeginUTC : Edm.DateTimeOffset "Actual Date"
PX.Objects.FS.FSAppointment.ActualDateTimeEndUTC : Edm.DateTimeOffset "Actual Date End"
PX.Objects.FS.FSAppointment.ScheduledDateTimeBeginUTC : Edm.DateTimeOffset "Scheduled Date"
PX.Objects.FS.FSAppointment.ScheduledDateTimeEndUTC : Edm.DateTimeOffset "Scheduled Date End"
PX.Objects.FS.FSAppointment.IsCalledFromQuickProcess : Edm.Boolean
PX.Objects.FS.FSAppointment.IsPosted : Edm.Boolean
PX.Objects.FS.FSAppointment.TravelCanBeStarted : Edm.Boolean "TravelCanBeStarted"
PX.Objects.FS.FSAppointment.TravelCanBeCompleted : Edm.Boolean "TravelCanBeCompleted"
PX.Objects.FS.FSAppointment.MustUpdateServiceOrder : Edm.Boolean
PX.Objects.FS.FSAppointment.FormCaptionDescription : Edm.String
PX.Objects.FS.FSAppointment.IsINReleaseProcess : Edm.Boolean
PX.Objects.FS.FSAppointment.TrackTimeChanged : Edm.Boolean "TrackTimeChanged"
PX.Objects.FS.FSAppointment.CuryActualBillableTotal : Edm.Decimal "Actual Billable Total"
PX.Objects.FS.FSAppointment.ActualBillableTotal : Edm.Decimal "Actual Billable Total"
PX.Objects.FS.FSAppointment.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.FS.FSAppointment.EntityUsageType : Edm.String "Tax Exemption Type"
PX.Objects.FS.FSAppointment.EditActionRunning : Edm.Boolean
PX.Objects.FS.FSAppointment.CuryRate : Edm.Decimal
PX.Objects.FS.FSAppointment.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.FS.FSAppointment.PMTaskByDfltProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSAppointment.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSAppointment.BAccountByPrimaryDriver -> PX.Objects.CR.BAccount
PX.Objects.FS.FSAppointment.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.FS.FSAppointment.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSAppointment.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule
PX.Objects.FS.FSAppointment.FSEquipmentByVehicleID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSAppointment.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSAppointment.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSAppointment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAppointment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSAppointment.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.FS.FSAppointment.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.FS.FSAppointment.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.FS.FSAppointment.FSRouteByRouteID -> PX.Objects.FS.FSRoute (RouteID=RouteID)
PX.Objects.FS.FSAppointment.FSRouteDocumentByRouteDocumentID -> PX.Objects.FS.FSRouteDocument (RouteDocumentID=RouteDocumentID)
PX.Objects.FS.FSAppointment.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract
PX.Objects.FS.FSAppointment.FSServiceContractByBillServiceContractID -> PX.Objects.FS.FSServiceContract
PX.Objects.FS.FSAppointment.FSServiceContractByCustomerID -> PX.Objects.FS.FSServiceContract (CustomerID=CustomerID)
PX.Objects.FS.FSAppointment.FSServiceOrderBySoRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSAppointment.FSServiceOrderBySrvOrdType -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSAppointment.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSAppointment.FSWFStageByWFStageID -> PX.Objects.FS.FSWFStage (WFStageID=WFStageID)
PX.Objects.FS.FSAppointment.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.FSAppointment.FSAppointmentResourceCollection -> Collection(PX.Objects.FS.FSAppointmentResource)
PX.Objects.FS.FSAppointment.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSAppointment.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.FS.FSAppointment.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.FSAppointment.FSAppointmentTaxTranCollection -> Collection(PX.Objects.FS.FSAppointmentTaxTran)
PX.Objects.FS.FSAppointment.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.FS.FSAppointment.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.FSAppointment.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.FS.FSAppointment.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.FS.FSAppointment.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.Objects.FS.FSAppointment.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.FSAppointment.FSPostDocCollection -> Collection(PX.Objects.FS.FSPostDoc)
PX.Objects.FS.FSAppointment.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.FS.FSAppointment.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.FSAppointment.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.Objects.FS.FSAppointment.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.FS.FSAppointment.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.FS.FSAppointment.SchedulerAppointmentCollection -> Collection(PX.Objects.FS.SchedulerAppointment)

# PX.Objects.FS.FSAppointmentDet (EntityType)

Label: "Appointment Item Detail"
Key: LineNbr, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSAppointmentDet, AppointmentItemDetail, FSAppointmentDet
Non-filterable, non-selectable: SOLineType, UIStatus, AreActualFieldsActive, Qty, NoteText, CuryExtPrice, CuryLineAmt, SkipCostCodeValidation, InventoryIDReport, CanChangeMarkForPO, EnableUnlinkPO, TabOrigin, LinkedDisplayRefNbr, InventoryCD, Operation, TranType, InvtMult, LocationID, TaskID, IsLotSerialRequired, INOpenQty

PX.Objects.FS.FSAppointmentDet.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointmentDet.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointmentDet.AppointmentID : Edm.Int32 "Appointment Nbr."
PX.Objects.FS.FSAppointmentDet.AppDetID : Edm.Int32
PX.Objects.FS.FSAppointmentDet.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.FSAppointmentDet.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.FS.FSAppointmentDet.SODetID : Edm.Int32 "Service Order Detail Ref. Nbr."
PX.Objects.FS.FSAppointmentDet.LineRef : Edm.String "Ref. Nbr."
PX.Objects.FS.FSAppointmentDet.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSAppointmentDet.CuryInfoID : Edm.Int64
PX.Objects.FS.FSAppointmentDet.LineType : Edm.String "Line Type"
PX.Objects.FS.FSAppointmentDet.IsPrepaid : Edm.Boolean [required] "Prepaid Item"
PX.Objects.FS.FSAppointmentDet.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSAppointmentDet.UOM : Edm.String "UOM"
PX.Objects.FS.FSAppointmentDet.BillingRule : Edm.String "Billing Rule"
PX.Objects.FS.FSAppointmentDet.IsTravelItem : Edm.Boolean [required] "Is a Travel Item"
PX.Objects.FS.FSAppointmentDet.SOLineType : Edm.String "SO Line Type"
PX.Objects.FS.FSAppointmentDet.Status : Edm.String "Line Status"
PX.Objects.FS.FSAppointmentDet.UIStatus : Edm.String "Line Status"
PX.Objects.FS.FSAppointmentDet.IsCanceledNotPerformed : Edm.Boolean
PX.Objects.FS.FSAppointmentDet.EstimatedDuration : Edm.Int32 [required] "Estimated Duration"
PX.Objects.FS.FSAppointmentDet.EstimatedQty : Edm.Decimal "Estimated Quantity"
PX.Objects.FS.FSAppointmentDet.BaseEstimatedQty : Edm.Decimal [required] "Base Estimated Qty."
PX.Objects.FS.FSAppointmentDet.LogActualDuration : Edm.Int32 [required] "Log Actual Duration"
PX.Objects.FS.FSAppointmentDet.AreActualFieldsActive : Edm.Boolean
PX.Objects.FS.FSAppointmentDet.ActualDuration : Edm.Int32 "Actual Duration"
PX.Objects.FS.FSAppointmentDet.ActualQty : Edm.Decimal "Actual Quantity"
PX.Objects.FS.FSAppointmentDet.BaseActualQty : Edm.Decimal [required] "Base Actual Qty."
PX.Objects.FS.FSAppointmentDet.EffTranQty : Edm.Decimal [required] "Transaction Qty."
PX.Objects.FS.FSAppointmentDet.Qty : Edm.Decimal "Qty."
PX.Objects.FS.FSAppointmentDet.BaseEffTranQty : Edm.Decimal [required] "Base Transaction Qty."
PX.Objects.FS.FSAppointmentDet.ManualPrice : Edm.Boolean [required] "Manual Price"
PX.Objects.FS.FSAppointmentDet.IsBillable : Edm.Boolean "Billable"
PX.Objects.FS.FSAppointmentDet.IsFree : Edm.Boolean "Free Item"
PX.Objects.FS.FSAppointmentDet.BillableQty : Edm.Decimal "Billable Quantity"
PX.Objects.FS.FSAppointmentDet.BaseBillableQty : Edm.Decimal "Base Billable Qty."
PX.Objects.FS.FSAppointmentDet.TranDesc : Edm.String "Description"
PX.Objects.FS.FSAppointmentDet.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSAppointmentDet.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSAppointmentDet.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSAppointmentDet.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSAppointmentDet.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSAppointmentDet.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSAppointmentDet.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSAppointmentDet.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSAppointmentDet.tstamp : Edm.Binary
PX.Objects.FS.FSAppointmentDet.ExpenseEmployeeID : Edm.Int32 "Expense Staff Member ID"
PX.Objects.FS.FSAppointmentDet.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.FS.FSAppointmentDet.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.FS.FSAppointmentDet.UnitCost : Edm.Decimal [required]
PX.Objects.FS.FSAppointmentDet.CuryEstimatedExtCost : Edm.Decimal "CuryEstimatedExtCost"
PX.Objects.FS.FSAppointmentDet.EstimatedExtCost : Edm.Decimal
PX.Objects.FS.FSAppointmentDet.ManualCost : Edm.Boolean [required] "Manual Cost"
PX.Objects.FS.FSAppointmentDet.CuryUnitPrice : Edm.Decimal "Unit Price"
PX.Objects.FS.FSAppointmentDet.UnitPrice : Edm.Decimal "Base Unit Price"
PX.Objects.FS.FSAppointmentDet.EstimatedTranAmt : Edm.Decimal "Base Estimated Amount"
PX.Objects.FS.FSAppointmentDet.CuryEstimatedTranAmt : Edm.Decimal "Estimated Amount"
PX.Objects.FS.FSAppointmentDet.CuryExtCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.FS.FSAppointmentDet.ExtCost : Edm.Decimal [required]
PX.Objects.FS.FSAppointmentDet.CuryBillableExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.FS.FSAppointmentDet.BillableExtPrice : Edm.Decimal
PX.Objects.FS.FSAppointmentDet.CuryBillableTranAmt : Edm.Decimal "Billable Amount"
PX.Objects.FS.FSAppointmentDet.BillableTranAmt : Edm.Decimal "Base Billable Amount"
PX.Objects.FS.FSAppointmentDet.CuryExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.FS.FSAppointmentDet.CuryLineAmt : Edm.Decimal "Amount"
PX.Objects.FS.FSAppointmentDet.CuryTranAmt : Edm.Decimal "Actual Amount"
PX.Objects.FS.FSAppointmentDet.TranAmt : Edm.Decimal "Base Actual Amount"
PX.Objects.FS.FSAppointmentDet.ManualDisc : Edm.Boolean "Manual Discount"
PX.Objects.FS.FSAppointmentDet.DiscPct : Edm.Decimal "Discount Percent"
PX.Objects.FS.FSAppointmentDet.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.FS.FSAppointmentDet.DiscAmt : Edm.Decimal
PX.Objects.FS.FSAppointmentDet.DiscountID : Edm.String "Discount Code"
PX.Objects.FS.FSAppointmentDet.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.FS.FSAppointmentDet.PostID : Edm.Int32 "Post ID"
PX.Objects.FS.FSAppointmentDet.ProjectID : Edm.Int32 "ProjectID"
PX.Objects.FS.FSAppointmentDet.ScheduleDetID : Edm.Int32 "ScheduleDetID"
PX.Objects.FS.FSAppointmentDet.CostCenterID : Edm.Int32 [required]
PX.Objects.FS.FSAppointmentDet.StaffID : Edm.Int32 "Staff Member ID"
PX.Objects.FS.FSAppointmentDet.PriceType : Edm.String "Price Type"
PX.Objects.FS.FSAppointmentDet.PriceCode : Edm.String "Price Code"
PX.Objects.FS.FSAppointmentDet.ScheduleID : Edm.Int32
PX.Objects.FS.FSAppointmentDet.SkipCostCodeValidation : Edm.Boolean
PX.Objects.FS.FSAppointmentDet.InventoryIDReport : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSAppointmentDet.EquipmentItemClass : Edm.String
PX.Objects.FS.FSAppointmentDet.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.FS.FSAppointmentDet.GroupDiscountRate : Edm.Decimal
PX.Objects.FS.FSAppointmentDet.DocumentDiscountRate : Edm.Decimal [required]
PX.Objects.FS.FSAppointmentDet.CanChangeMarkForPO : Edm.Boolean
PX.Objects.FS.FSAppointmentDet.EnableUnlinkPO : Edm.Boolean "Allow PO Unlinking"
PX.Objects.FS.FSAppointmentDet.AllocatedFromSrvOrdPOQty : Edm.Decimal [required] "Allocated from Service Order PO Qty."
PX.Objects.FS.FSAppointmentDet.BaseAllocatedFromSrvOrdPOQty : Edm.Decimal
PX.Objects.FS.FSAppointmentDet.TabOrigin : Edm.Int32
PX.Objects.FS.FSAppointmentDet.LotSerTrack : Edm.String
PX.Objects.FS.FSAppointmentDet.LinkedEntityType : Edm.String "Related Doc. Type"
PX.Objects.FS.FSAppointmentDet.LinkedDocType : Edm.String "LinkedDocType"
PX.Objects.FS.FSAppointmentDet.LinkedDocRefNbr : Edm.String "LinkedDocRefNbr"
PX.Objects.FS.FSAppointmentDet.LinkedDisplayRefNbr : Edm.String "Related Doc. Nbr."
PX.Objects.FS.FSAppointmentDet.LinkedLineNbr : Edm.Int32 "Related Doc. Line Nbr."
PX.Objects.FS.FSAppointmentDet.SODetCreate : Edm.Boolean [required] "SODetCreate"
PX.Objects.FS.FSAppointmentDet.InventoryCD : Edm.String "Inventory ID"
PX.Objects.FS.FSAppointmentDet.OrigSrvOrdNbr : Edm.String "Service Order Nbr."
PX.Objects.FS.FSAppointmentDet.OrigLineNbr : Edm.Int32 "Service Order Line Nbr."
PX.Objects.FS.FSAppointmentDet.UnassignedQty : Edm.Decimal "Unassigned Qty."
PX.Objects.FS.FSAppointmentDet.Operation : Edm.String
PX.Objects.FS.FSAppointmentDet.TranType : Edm.String
PX.Objects.FS.FSAppointmentDet.InvtMult : Edm.Int16 "Inventory Multiplier"
PX.Objects.FS.FSAppointmentDet.LocationID : Edm.Int32
PX.Objects.FS.FSAppointmentDet.TaskID : Edm.Int32
PX.Objects.FS.FSAppointmentDet.IsLotSerialRequired : Edm.Boolean
PX.Objects.FS.FSAppointmentDet.INOpenQty : Edm.Decimal
PX.Objects.FS.FSAppointmentDet.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.FS.FSAppointmentDet.VendorByPoVendorID -> PX.Objects.AP.Vendor
PX.Objects.FS.FSAppointmentDet.POOrderByPoNbr -> PX.Objects.PO.POOrder
PX.Objects.FS.FSAppointmentDet.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.FS.FSAppointmentDet.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.FS.FSAppointmentDet.BAccountByStaffID -> PX.Objects.CR.BAccount (StaffID=BAccountID)
PX.Objects.FS.FSAppointmentDet.BAccountByPoVendorID -> PX.Objects.CR.BAccount
PX.Objects.FS.FSAppointmentDet.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSAppointmentDet.InventoryItemByPickupDeliveryServiceID -> PX.Objects.IN.InventoryItem
PX.Objects.FS.FSAppointmentDet.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule (ScheduleID=ScheduleID)
PX.Objects.FS.FSAppointmentDet.FSEquipmentBySMequipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSAppointmentDet.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSAppointmentDet.FSSODetBySODetID -> PX.Objects.FS.FSSODet (SODetID=SODetID)
PX.Objects.FS.FSAppointmentDet.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSAppointmentDet.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSAppointmentDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAppointmentDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSAppointmentDet.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.FS.FSAppointmentDet.SOOrderTypeByPoType -> PX.Objects.SO.SOOrderType
PX.Objects.FS.FSAppointmentDet.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.FS.FSAppointmentDet.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.FS.FSAppointmentDet.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.FS.FSAppointmentDet.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSAppointmentDet.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.FS.FSAppointmentDet.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.FS.FSAppointmentDet.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.FS.FSAppointmentDet.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.FS.FSAppointmentDet.LocationByPoVendorID -> PX.Objects.CR.Location
PX.Objects.FS.FSAppointmentDet.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.FS.FSAppointmentDet.FSAppointmentDetByPickupDeliveryAppLineRef -> PX.Objects.FS.FSAppointmentDet
PX.Objects.FS.FSAppointmentDet.FSAppointmentDetByNewTargetEquipmentLineNbr -> PX.Objects.FS.FSAppointmentDet
PX.Objects.FS.FSAppointmentDet.FSEquipmentComponentByEquipmentLineRef -> PX.Objects.FS.FSEquipmentComponent
PX.Objects.FS.FSAppointmentDet.FSEquipmentComponentBySMequipmentID -> PX.Objects.FS.FSEquipmentComponent
PX.Objects.FS.FSAppointmentDet.FSModelTemplateComponentByComponentID -> PX.Objects.FS.FSModelTemplateComponent
PX.Objects.FS.FSAppointmentDet.FSPostInfoByPostID -> PX.Objects.FS.FSPostInfo (PostID=PostID)
PX.Objects.FS.FSAppointmentDet.FSScheduleDetByScheduleDetID -> PX.Objects.FS.FSScheduleDet (ScheduleID=ScheduleID, ScheduleDetID=ScheduleDetID)
PX.Objects.FS.FSAppointmentDet.FSServiceOrderByOrigSrvOrdNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, OrigSrvOrdNbr=RefNbr)
PX.Objects.FS.FSAppointmentDet.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSAppointmentDet.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.FS.FSAppointmentDet.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.FS.FSAppointmentDet.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.FSAppointmentDet.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSAppointmentDet.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.FSAppointmentDet.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)

# PX.Objects.FS.FSAppointmentDiscountDetail (EntityType)

BaseType: PX.Objects.FS.FSDiscountDetail
Key: EntityType, RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSDiscountDetail)
Entity sets: PX_Objects_FS_FSAppointmentDiscountDetail

# PX.Objects.FS.FSAppointmentEmployee (EntityType)

Label: "FSAppointmentEmployee"
Key: LineNbr, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSAppointmentEmployee, FSAppointmentEmployee
Non-filterable, non-selectable: NoteText, SkipCostCodeValidation, IsStaffCalendar

PX.Objects.FS.FSAppointmentEmployee.EmployeeID : Edm.Int32 "Staff Member"
PX.Objects.FS.FSAppointmentEmployee.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointmentEmployee.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointmentEmployee.AppointmentID : Edm.Int32 "Appointment Ref. Nbr."
PX.Objects.FS.FSAppointmentEmployee.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.FSAppointmentEmployee.LineRef : Edm.String "Ref. Nbr."
PX.Objects.FS.FSAppointmentEmployee.ServiceLineRef : Edm.String "Detail Ref. Nbr."
PX.Objects.FS.FSAppointmentEmployee.PrimaryDriver : Edm.Boolean [required] "Primary Driver"
PX.Objects.FS.FSAppointmentEmployee.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSAppointmentEmployee.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSAppointmentEmployee.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSAppointmentEmployee.CreatedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentEmployee.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentEmployee.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSAppointmentEmployee.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentEmployee.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentEmployee.tstamp : Edm.Binary
PX.Objects.FS.FSAppointmentEmployee.IsDriver : Edm.Boolean [required] "Route Driver"
PX.Objects.FS.FSAppointmentEmployee.Type : Edm.String "Staff Type"
PX.Objects.FS.FSAppointmentEmployee.EarningType : Edm.String "Earning Type"
PX.Objects.FS.FSAppointmentEmployee.TrackTime : Edm.Boolean "Track Time"
PX.Objects.FS.FSAppointmentEmployee.SkipCostCodeValidation : Edm.Boolean
PX.Objects.FS.FSAppointmentEmployee.LaborItemID : Edm.Int32 "Labor Item"
PX.Objects.FS.FSAppointmentEmployee.IsStaffCalendar : Edm.Boolean "IsStaffCalendar"
PX.Objects.FS.FSAppointmentEmployee.PMProjectByDfltProjectID -> PX.Objects.PM.PMProject
PX.Objects.FS.FSAppointmentEmployee.PMTaskByDfltProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSAppointmentEmployee.PMTaskByDfltProjectID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSAppointmentEmployee.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.FS.FSAppointmentEmployee.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.FS.FSAppointmentEmployee.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSAppointmentEmployee.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAppointmentEmployee.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSAppointmentEmployee.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.FS.FSAppointmentEmployee.EPEarningTypeByEarningType -> PX.Objects.EP.EPEarningType (EarningType=TypeCD)
PX.Objects.FS.FSAppointmentEmployee.FSAppointmentDetByAppointmentID -> PX.Objects.FS.FSAppointmentDet (ServiceLineRef=LineRef, AppointmentID=AppointmentID)
PX.Objects.FS.FSAppointmentEmployee.FSAppointmentDetByServiceLineRef -> PX.Objects.FS.FSAppointmentDet (ServiceLineRef=LineRef)
PX.Objects.FS.FSAppointmentEmployee.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSAppointmentFSServiceOrder (EntityType)

Label: "Appointment"
BaseType: PX.Objects.FS.FSAppointment
Key: RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSAppointment)
Entity sets: PX_Objects_FS_FSAppointmentFSServiceOrder

PX.Objects.FS.FSAppointmentFSServiceOrder.ScheduleID : Edm.Int32 "Schedule ID"
PX.Objects.FS.FSAppointmentFSServiceOrder.BillServiceContractID : Edm.Int32 "Service Contract ID"
PX.Objects.FS.FSAppointmentFSServiceOrder.WaitingForParts : Edm.Boolean "Waiting for Purchased Items"
PX.Objects.FS.FSAppointmentFSServiceOrder.ActualBeginDateTimeUTC : Edm.DateTimeOffset "Actual Date"
PX.Objects.FS.FSAppointmentFSServiceOrder.ActualEndDateTimeUTC : Edm.DateTimeOffset "Actual Date End"
PX.Objects.FS.FSAppointmentFSServiceOrder.ScheduledBeginDateTimeUTC : Edm.DateTimeOffset "Scheduled Date"
PX.Objects.FS.FSAppointmentFSServiceOrder.ScheduledEndDateTimeUTC : Edm.DateTimeOffset "Scheduled Date End"
PX.Objects.FS.FSAppointmentFSServiceOrder.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.FS.FSAppointmentFSServiceOrder.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.FS.FSAppointmentFSServiceOrder.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.FS.FSAppointmentFSServiceOrder.AddressValidated : Edm.Boolean "Address Validated"
PX.Objects.FS.FSAppointmentFSServiceOrder.AssignedEmpID : Edm.Int32 "Assigned To"
PX.Objects.FS.FSAppointmentFSServiceOrder.City : Edm.String "City"
PX.Objects.FS.FSAppointmentFSServiceOrder.ContactID : Edm.Int32 "Contact"
PX.Objects.FS.FSAppointmentFSServiceOrder.ContractID : Edm.Int32 "Contract"
PX.Objects.FS.FSAppointmentFSServiceOrder.CountryID : Edm.String "Country"
PX.Objects.FS.FSAppointmentFSServiceOrder.BranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.FSAppointmentFSServiceOrder.RoomID : Edm.String "Room"
PX.Objects.FS.FSAppointmentFSServiceOrder.SODocDesc : Edm.String "Description"
PX.Objects.FS.FSAppointmentFSServiceOrder.EMail : Edm.String "Email"
PX.Objects.FS.FSAppointmentFSServiceOrder.Fax : Edm.String "Fax"
PX.Objects.FS.FSAppointmentFSServiceOrder.Phone1 : Edm.String "Phone 1"
PX.Objects.FS.FSAppointmentFSServiceOrder.Phone2 : Edm.String "Phone 2"
PX.Objects.FS.FSAppointmentFSServiceOrder.Phone3 : Edm.String "Phone 3"
PX.Objects.FS.FSAppointmentFSServiceOrder.PostalCode : Edm.String "Postal Code"
PX.Objects.FS.FSAppointmentFSServiceOrder.CuryEstimatedOrderTotal : Edm.Decimal "Estimated Order Total"
PX.Objects.FS.FSAppointmentFSServiceOrder.Priority : Edm.String "Priority"
PX.Objects.FS.FSAppointmentFSServiceOrder.ProblemID : Edm.Int32 "Problem ID"
PX.Objects.FS.FSAppointmentFSServiceOrder.Severity : Edm.String "Severity"
PX.Objects.FS.FSAppointmentFSServiceOrder.SLAETA : Edm.DateTimeOffset "Deadline - SLA"
PX.Objects.FS.FSAppointmentFSServiceOrder.SourceDocType : Edm.String "Source document type"
PX.Objects.FS.FSAppointmentFSServiceOrder.SourceID : Edm.Int32
PX.Objects.FS.FSAppointmentFSServiceOrder.SourceRefNbr : Edm.String "Source Ref. Nbr."
PX.Objects.FS.FSAppointmentFSServiceOrder.SourceType : Edm.String "Source Type"
PX.Objects.FS.FSAppointmentFSServiceOrder.State : Edm.String "State"
PX.Objects.FS.FSAppointmentFSServiceOrder.BAccountRequired : Edm.Boolean "Customer Required"
PX.Objects.FS.FSAppointmentFSServiceOrder.Quote : Edm.Boolean "Quote"
PX.Objects.FS.FSAppointmentFSServiceOrder.CustWorkOrderRefNbr : Edm.String "Customer Work Order Ref. Nbr."
PX.Objects.FS.FSAppointmentFSServiceOrder.PostedBy : Edm.String
PX.Objects.FS.FSAppointmentFSServiceOrder.SLAETAUTC : Edm.DateTimeOffset "Deadline - SLA"
PX.Objects.FS.FSAppointmentFSServiceOrder.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.FS.FSAppointmentFSServiceOrder.BAccountByAssignedEmpID -> PX.Objects.CR.BAccount (AssignedEmpID=BAccountID)
PX.Objects.FS.FSAppointmentFSServiceOrder.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.FS.FSAppointmentFSServiceOrder.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.FS.FSAppointmentFSServiceOrder.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.FSAppointmentFSServiceOrder.FSProblemByProblemID -> PX.Objects.FS.FSProblem (ProblemID=ProblemID)
PX.Objects.FS.FSAppointmentFSServiceOrder.FSRoomByRoomID -> PX.Objects.FS.FSRoom (BranchLocationID=BranchLocationID, RoomID=RoomID)
PX.Objects.FS.FSAppointmentFSServiceOrder.ContractByLocationID -> PX.Objects.CT.Contract (ContractID=ContractID, CustomerID=CustomerID)
PX.Objects.FS.FSAppointmentFSServiceOrder.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.FSAppointmentFSServiceOrder.FSRoomByBranchLocationID -> PX.Objects.FS.FSRoom (RoomID=RoomID, BranchLocationID=BranchLocationID)
PX.Objects.FS.FSAppointmentFSServiceOrder.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.FS.FSAppointmentFSServiceOrder.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)

# PX.Objects.FS.FSAppointmentInRoute (EntityType)

Label: "Appointment"
BaseType: PX.Objects.FS.FSAppointment
Key: RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSAppointment)
Entity sets: PX_Objects_FS_FSAppointmentInRoute

PX.Objects.FS.FSAppointmentInRoute.CustomerContractNbr : Edm.String "Customer Contract Nbr."
PX.Objects.FS.FSAppointmentInRoute.State : Edm.String "State"
PX.Objects.FS.FSAppointmentInRoute.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.FS.FSAppointmentInRoute.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.FS.FSAppointmentInRoute.PostalCode : Edm.String "Postal code"
PX.Objects.FS.FSAppointmentInRoute.City : Edm.String "City"
PX.Objects.FS.FSAppointmentInRoute.MapApiKey : Edm.String "Map API Key"
PX.Objects.FS.FSAppointmentInRoute.StateByState -> PX.Objects.CS.State (State=StateID)
PX.Objects.FS.FSAppointmentInRoute.LocationByLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.FSAppointmentInRoute.BAccountByAssignedEmpID -> PX.Objects.CR.BAccount

# PX.Objects.FS.FSAppointmentLog (EntityType)

Label: "Log"
BaseType: PX.Objects.FS.FSLog
Key: LogID (inherited from PX.Objects.FS.FSLog)
Entity sets: PX_Objects_FS_FSAppointmentLog, Log, FSAppointmentLog
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FS.FSAppointmentLog.Travel : Edm.Boolean "Travel"
PX.Objects.FS.FSAppointmentLog.ServiceDateTimeBegin : Edm.DateTimeOffset "ServiceDateTimeBegin"
PX.Objects.FS.FSAppointmentLog.ServiceDateTimeEnd : Edm.DateTimeOffset "ServiceDateTimeEnd"

# PX.Objects.FS.FSAppointmentLogExtItemLine (EntityType)

Label: "Log"
BaseType: PX.Objects.FS.FSAppointmentLog
Key: LogID (inherited from PX.Objects.FS.FSLog)
Entity sets: PX_Objects_FS_FSAppointmentLogExtItemLine

PX.Objects.FS.FSAppointmentLogExtItemLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSAppointmentLogExtItemLine.UserID : Edm.Guid "UserID"
PX.Objects.FS.FSAppointmentLogExtItemLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSAppointmentLogExtItemLine.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.FS.FSAppointmentLogExtItemLine.ContactByPrimaryContactID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentLogExtItemLine.ContactByDefContactID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentLogExtItemLine.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentLogExtItemLine.ContactByParentBAccountID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentLogExtItemLine.InventoryItemByPickupDeliveryServiceID -> PX.Objects.IN.InventoryItem
PX.Objects.FS.FSAppointmentLogExtItemLine.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.FS.FSAppointmentLogExtItemLine.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)

# PX.Objects.FS.FSAppointmentResource (EntityType)

Key: RefNbr, SMEquipmentID, SrvOrdType
Entity sets: PX_Objects_FS_FSAppointmentResource
Non-filterable, non-selectable: SMEquipmentIDReport

PX.Objects.FS.FSAppointmentResource.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointmentResource.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointmentResource.AppointmentID : Edm.Int32 "Appointment Ref. Nbr."
PX.Objects.FS.FSAppointmentResource.SMEquipmentID : Edm.Int32 [key] "Equipment ID"
PX.Objects.FS.FSAppointmentResource.Comment : Edm.String "Comment"
PX.Objects.FS.FSAppointmentResource.Qty : Edm.Int32 [required] "Quantity"
PX.Objects.FS.FSAppointmentResource.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSAppointmentResource.CreatedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentResource.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentResource.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSAppointmentResource.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentResource.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentResource.tstamp : Edm.Binary
PX.Objects.FS.FSAppointmentResource.SMEquipmentIDReport : Edm.Int32
PX.Objects.FS.FSAppointmentResource.FSEquipmentBySMequipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSAppointmentResource.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSAppointmentResource.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAppointmentResource.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSAppointmentResource.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSAppointmentScheduleBoard (EntityType)

Key: RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSAppointmentScheduleBoard
Non-filterable, non-selectable: RoomDesc, FirstServiceDesc, StatusUI, CustomID, CustomDateID, CustomRoomID, AppointmentCustomID, CustomDateTimeStart, CustomDateTimeEnd, EmployeeID, OldEmployeeID, EmployeeList, EmployeeCount, ServiceCount, ServiceList, CanDeleteAppointment, MemRefNbr, MemAcctName, OpenAppointmentScreenOnError, IsPosted, Resizable, Draggable

PX.Objects.FS.FSAppointmentScheduleBoard.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointmentScheduleBoard.AppointmentID : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.SOID : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointmentScheduleBoard.SORefNbr : Edm.String "Service Order Nbr."
PX.Objects.FS.FSAppointmentScheduleBoard.Closed : Edm.Boolean "Closed"
PX.Objects.FS.FSAppointmentScheduleBoard.Canceled : Edm.Boolean "Canceled"
PX.Objects.FS.FSAppointmentScheduleBoard.Billed : Edm.Boolean "Billed"
PX.Objects.FS.FSAppointmentScheduleBoard.Status : Edm.String "Status"
PX.Objects.FS.FSAppointmentScheduleBoard.Confirmed : Edm.Boolean "Confirmed"
PX.Objects.FS.FSAppointmentScheduleBoard.ValidatedByDispatcher : Edm.Boolean "Confirmed"
PX.Objects.FS.FSAppointmentScheduleBoard.BranchID : Edm.Int32 "Branch ID"
PX.Objects.FS.FSAppointmentScheduleBoard.BranchLocationID : Edm.Int32 "Branch Location ID"
PX.Objects.FS.FSAppointmentScheduleBoard.BranchLocationDesc : Edm.String "Branch Location Desc"
PX.Objects.FS.FSAppointmentScheduleBoard.ScheduledDateTimeBegin : Edm.DateTimeOffset "Scheduled Start Date"
PX.Objects.FS.FSAppointmentScheduleBoard.ScheduledDateTimeEnd : Edm.DateTimeOffset "Scheduled End Date"
PX.Objects.FS.FSAppointmentScheduleBoard.ContactName : Edm.String "Contact Name"
PX.Objects.FS.FSAppointmentScheduleBoard.ContactPhone : Edm.String "Contact Phone"
PX.Objects.FS.FSAppointmentScheduleBoard.ContactEmail : Edm.String "Contact Email"
PX.Objects.FS.FSAppointmentScheduleBoard.CustomerID : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.CustomerName : Edm.String "Customer Name"
PX.Objects.FS.FSAppointmentScheduleBoard.CustomerLocation : Edm.Int32 "Customer Location"
PX.Objects.FS.FSAppointmentScheduleBoard.WFStageCD : Edm.String "WFStageCD"
PX.Objects.FS.FSAppointmentScheduleBoard.LocationDesc : Edm.String "LocationDesc"
PX.Objects.FS.FSAppointmentScheduleBoard.RoomID : Edm.String "Room"
PX.Objects.FS.FSAppointmentScheduleBoard.RoomDesc : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.FirstServiceDesc : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.DocDesc : Edm.String "DocDesc"
PX.Objects.FS.FSAppointmentScheduleBoard.AddressID : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.StatusUI : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.CustomID : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.CustomDateID : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.CustomRoomID : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.AppointmentCustomID : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.CustomDateTimeStart : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.CustomDateTimeEnd : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.EmployeeID : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.OldEmployeeID : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.EmployeeList : Collection(Edm.String)
PX.Objects.FS.FSAppointmentScheduleBoard.EmployeeCount : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.ServiceCount : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.ServiceList : Collection(Edm.String)
PX.Objects.FS.FSAppointmentScheduleBoard.SMEquipmentID : Edm.Int32
PX.Objects.FS.FSAppointmentScheduleBoard.PostingStatusAPARSO : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.PostingStatusIN : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.CanDeleteAppointment : Edm.Boolean
PX.Objects.FS.FSAppointmentScheduleBoard.MemRefNbr : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.MemAcctName : Edm.String
PX.Objects.FS.FSAppointmentScheduleBoard.OpenAppointmentScreenOnError : Edm.Boolean
PX.Objects.FS.FSAppointmentScheduleBoard.IsPosted : Edm.Boolean
PX.Objects.FS.FSAppointmentScheduleBoard.Resizable : Edm.Boolean
PX.Objects.FS.FSAppointmentScheduleBoard.Draggable : Edm.Boolean
PX.Objects.FS.FSAppointmentScheduleBoard.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSAppointmentScheduleBoard.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.FSAppointmentScheduleBoard.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.FSAppointmentScheduleBoard.FSRoomByRoomID -> PX.Objects.FS.FSRoom (BranchLocationID=BranchLocationID, RoomID=RoomID)
PX.Objects.FS.FSAppointmentScheduleBoard.FSRoomByBranchLocationID -> PX.Objects.FS.FSRoom (RoomID=RoomID, BranchLocationID=BranchLocationID)
PX.Objects.FS.FSAppointmentScheduleBoard.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSAppointmentScheduleBoard.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.FSAppointmentScheduleBoard.FSAppointmentResourceCollection -> Collection(PX.Objects.FS.FSAppointmentResource)
PX.Objects.FS.FSAppointmentScheduleBoard.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSAppointmentScheduleBoard.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.FSAppointmentScheduleBoard.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.FS.FSAppointmentScheduleBoard.FSPostDocCollection -> Collection(PX.Objects.FS.FSPostDoc)
PX.Objects.FS.FSAppointmentScheduleBoard.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.FS.FSAppointmentScheduleBoard.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.FSAppointmentScheduleBoard.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.Objects.FS.FSAppointmentScheduleBoard.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.FS.FSAppointmentScheduleBoard.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.FS.FSAppointmentScheduleBoard.SchedulerAppointmentCollection -> Collection(PX.Objects.FS.SchedulerAppointment)
PX.Objects.FS.FSAppointmentScheduleBoard.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.FSAppointmentScheduleBoard.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.FSAppointmentScheduleBoard.FSSOResourceCollection -> Collection(PX.Objects.FS.FSSOResource)

# PX.Objects.FS.FSAppointmentServiceEmployee (EntityType)

Label: "Appointment Item Detail"
BaseType: PX.Objects.FS.FSAppointmentDet
Key: LineNbr, RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSAppointmentDet)
Entity sets: PX_Objects_FS_FSAppointmentServiceEmployee

# PX.Objects.FS.FSAppointmentStaffDistinct (EntityType)

Key: BAccountID, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSAppointmentStaffDistinct

PX.Objects.FS.FSAppointmentStaffDistinct.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointmentStaffDistinct.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointmentStaffDistinct.DocID : Edm.Int32 "Appointment Ref. Nbr."
PX.Objects.FS.FSAppointmentStaffDistinct.BAccountID : Edm.Int32 [key] "Staff Member"
PX.Objects.FS.FSAppointmentStaffDistinct.UserID : Edm.Guid "UserID"
PX.Objects.FS.FSAppointmentStaffDistinct.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.FS.FSAppointmentStaffDistinct.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSAppointmentStaffDistinct.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.FS.FSAppointmentStaffDistinct.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSAppointmentStaffDistinct.ContactByPrimaryContactID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentStaffDistinct.ContactByDefContactID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentStaffDistinct.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentStaffDistinct.ContactByParentBAccountID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentStaffDistinct.UsersByCreatedByID -> PX.SM.Users
PX.Objects.FS.FSAppointmentStaffDistinct.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.FS.FSAppointmentStaffDistinct.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.FS.FSAppointmentStaffDistinct.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)

# PX.Objects.FS.FSAppointmentStaffExtItemLine (EntityType)

Key: LineNbr, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSAppointmentStaffExtItemLine

PX.Objects.FS.FSAppointmentStaffExtItemLine.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointmentStaffExtItemLine.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointmentStaffExtItemLine.DocID : Edm.Int32 "Appointment Ref. Nbr."
PX.Objects.FS.FSAppointmentStaffExtItemLine.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.FSAppointmentStaffExtItemLine.BAccountID : Edm.Int32 "Staff Member"
PX.Objects.FS.FSAppointmentStaffExtItemLine.LineRef : Edm.String "Staff Ref. Nbr."
PX.Objects.FS.FSAppointmentStaffExtItemLine.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSAppointmentStaffExtItemLine.Descr : Edm.String "Description"
PX.Objects.FS.FSAppointmentStaffExtItemLine.EstimatedDuration : Edm.Int32 "Estimated Duration"
PX.Objects.FS.FSAppointmentStaffExtItemLine.UserID : Edm.Guid "UserID"
PX.Objects.FS.FSAppointmentStaffExtItemLine.DetLineRef : Edm.String "Detail Ref. Nbr."
PX.Objects.FS.FSAppointmentStaffExtItemLine.IsTravelItem : Edm.Boolean "Is a Travel Item"
PX.Objects.FS.FSAppointmentStaffExtItemLine.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.FS.FSAppointmentStaffExtItemLine.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSAppointmentStaffExtItemLine.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSAppointmentStaffExtItemLine.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.FS.FSAppointmentStaffExtItemLine.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSAppointmentStaffExtItemLine.ContactByPrimaryContactID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentStaffExtItemLine.ContactByDefContactID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentStaffExtItemLine.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentStaffExtItemLine.ContactByParentBAccountID -> PX.Objects.CR.Contact
PX.Objects.FS.FSAppointmentStaffExtItemLine.UsersByCreatedByID -> PX.SM.Users
PX.Objects.FS.FSAppointmentStaffExtItemLine.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.FS.FSAppointmentStaffExtItemLine.InventoryItemByPickupDeliveryServiceID -> PX.Objects.IN.InventoryItem
PX.Objects.FS.FSAppointmentStaffExtItemLine.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.FS.FSAppointmentStaffExtItemLine.FAUsageCollection -> Collection(PX.Objects.FA.FAUsage)

# PX.Objects.FS.FSAppointmentStaffMember (EntityType)

Label: "Business Account"
BaseType: PX.Objects.FS.BAccountStaffMember
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_FS_FSAppointmentStaffMember

PX.Objects.FS.FSAppointmentStaffMember.VendorSDEnabled : Edm.Boolean "Staff Member in Service Management"
PX.Objects.FS.FSAppointmentStaffMember.EmployeeSDEnabled : Edm.Boolean "Staff Member in Service Management"
PX.Objects.FS.FSAppointmentStaffMember.PositionID : Edm.String "Position"
PX.Objects.FS.FSAppointmentStaffMember.CalendarID : Edm.String "Calendar"
PX.Objects.FS.FSAppointmentStaffMember.BAccountByAcctCD -> PX.Objects.CR.BAccount (AcctCD=AcctCD)
PX.Objects.FS.FSAppointmentStaffMember.EPPositionByPositionID -> PX.Objects.EP.EPPosition (PositionID=PositionID)
PX.Objects.FS.FSAppointmentStaffMember.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)

# PX.Objects.FS.FSAppointmentStaffScheduleBoard (EntityType)

BaseType: PX.Objects.FS.FSAppointmentScheduleBoard
Key: RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSAppointmentScheduleBoard)
Entity sets: PX_Objects_FS_FSAppointmentStaffScheduleBoard

PX.Objects.FS.FSAppointmentStaffScheduleBoard.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)

# PX.Objects.FS.FSAppointmentStatusColor (EntityType)

Label: "Appointment Status Color"
Key: StatusID
Entity sets: PX_Objects_FS_FSAppointmentStatusColor, AppointmentStatusColor, FSAppointmentStatusColor

PX.Objects.FS.FSAppointmentStatusColor.StatusID : Edm.String [key] "ID"
PX.Objects.FS.FSAppointmentStatusColor.StatusLabel : Edm.String "Status"
PX.Objects.FS.FSAppointmentStatusColor.IsVisible : Edm.Boolean [required] "Visible"
PX.Objects.FS.FSAppointmentStatusColor.BackgroundColor : Edm.String "Background Color"
PX.Objects.FS.FSAppointmentStatusColor.TextColor : Edm.String "Text Color"
PX.Objects.FS.FSAppointmentStatusColor.BandColor : Edm.String "Bar Color"
PX.Objects.FS.FSAppointmentStatusColor.SystemRecord : Edm.Boolean [required] "System Record"
PX.Objects.FS.FSAppointmentStatusColor.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSAppointmentStatusColor.CreatedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentStatusColor.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentStatusColor.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSAppointmentStatusColor.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentStatusColor.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentStatusColor.Tstamp : Edm.Binary "Tstamp"
PX.Objects.FS.FSAppointmentStatusColor.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAppointmentStatusColor.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSAppointmentTax (EntityType)

Label: "Appointment Tax"
Key: LineNbr, RefNbr, SrvOrdType, TaxID
Entity sets: PX_Objects_FS_FSAppointmentTax, AppointmentTax, FSAppointmentTax
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt

PX.Objects.FS.FSAppointmentTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.FS.FSAppointmentTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.FS.FSAppointmentTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.FS.FSAppointmentTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.FS.FSAppointmentTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSAppointmentTax.CreatedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSAppointmentTax.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentTax.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointmentTax.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointmentTax.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.FS.FSAppointmentTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.FS.FSAppointmentTax.CuryInfoID : Edm.Int64
PX.Objects.FS.FSAppointmentTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.FS.FSAppointmentTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.FS.FSAppointmentTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.FS.FSAppointmentTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.FS.FSAppointmentTax.tstamp : Edm.Binary
PX.Objects.FS.FSAppointmentTax.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSAppointmentTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSAppointmentTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAppointmentTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSAppointmentTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.FS.FSAppointmentTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.FS.FSAppointmentTax.FSAppointmentDetByLineNbr -> PX.Objects.FS.FSAppointmentDet (SrvOrdType=SrvOrdType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.FS.FSAppointmentTax.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSAppointmentTaxTran (EntityType)

Label: "Appointment Tax Detail"
Key: RecordID, RefNbr, SrvOrdType, TaxID
Entity sets: PX_Objects_FS_FSAppointmentTaxTran, AppointmentTaxDetail, FSAppointmentTaxTran
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt, TaxZoneID

PX.Objects.FS.FSAppointmentTaxTran.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.FS.FSAppointmentTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.FS.FSAppointmentTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.FS.FSAppointmentTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.FS.FSAppointmentTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSAppointmentTaxTran.CreatedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSAppointmentTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSAppointmentTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSAppointmentTaxTran.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSAppointmentTaxTran.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSAppointmentTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.FS.FSAppointmentTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.FS.FSAppointmentTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.FS.FSAppointmentTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.FS.FSAppointmentTaxTran.CuryInfoID : Edm.Int64
PX.Objects.FS.FSAppointmentTaxTran.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.FS.FSAppointmentTaxTran.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.FS.FSAppointmentTaxTran.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.FS.FSAppointmentTaxTran.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.FS.FSAppointmentTaxTran.TaxZoneID : Edm.String
PX.Objects.FS.FSAppointmentTaxTran.tstamp : Edm.Binary
PX.Objects.FS.FSAppointmentTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.FS.FSAppointmentTaxTran.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSAppointmentTaxTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSAppointmentTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSAppointmentTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSAppointmentTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.FS.FSAppointmentTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.FS.FSAppointmentTaxTran.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSAppQuickProcessParams (EntityType)

BaseType: PX.Objects.SO.SOQuickProcessParameters
Key: OrderType (inherited from PX.Objects.SO.SOQuickProcessParameters)
Entity sets: PX_Objects_FS_FSAppQuickProcessParams
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FS.FSAppQuickProcessParams.SrvOrdType : Edm.String
PX.Objects.FS.FSAppQuickProcessParams.CloseAppointment : Edm.Boolean "Close"
PX.Objects.FS.FSAppQuickProcessParams.EmailSignedAppointment : Edm.Boolean "Email Signed Appointment"
PX.Objects.FS.FSAppQuickProcessParams.GenerateInvoiceFromAppointment : Edm.Boolean "Run Billing"
PX.Objects.FS.FSAppQuickProcessParams.SOQuickProcess : Edm.Boolean "Use Sales Order Quick Processing"
PX.Objects.FS.FSAppQuickProcessParams.EmailSalesOrder : Edm.Boolean "Email Sales Order/Quote"

# PX.Objects.FS.FSApptLineSplit (EntityType)

Label: "Appointment Lot/Serial Detail"
Key: ApptNbr, LineNbr, SplitLineNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSApptLineSplit, AppointmentLotSerialDetail, FSApptLineSplit
Non-filterable, non-selectable: TranType, LastLotSerialNbr, LotSerClassID, AssignedNbr, ProjectID, TaskID, CuryID, CuryRate, CuryViewState

PX.Objects.FS.FSApptLineSplit.SrvOrdType : Edm.String [key]
PX.Objects.FS.FSApptLineSplit.ApptNbr : Edm.String [key]
PX.Objects.FS.FSApptLineSplit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.FSApptLineSplit.OrigSrvOrdType : Edm.String
PX.Objects.FS.FSApptLineSplit.OrigSrvOrdNbr : Edm.String
PX.Objects.FS.FSApptLineSplit.OrigLineNbr : Edm.Int32
PX.Objects.FS.FSApptLineSplit.OrigSplitLineNbr : Edm.Int32
PX.Objects.FS.FSApptLineSplit.OrigPlanType : Edm.String
PX.Objects.FS.FSApptLineSplit.Operation : Edm.String
PX.Objects.FS.FSApptLineSplit.SplitLineNbr : Edm.Int32 [key] "Allocation ID"
PX.Objects.FS.FSApptLineSplit.ParentSplitLineNbr : Edm.Int32 "Parent Allocation ID"
PX.Objects.FS.FSApptLineSplit.InvtMult : Edm.Int16
PX.Objects.FS.FSApptLineSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSApptLineSplit.LineType : Edm.String
PX.Objects.FS.FSApptLineSplit.IsStockItem : Edm.Boolean
PX.Objects.FS.FSApptLineSplit.IsComponentItem : Edm.Boolean
PX.Objects.FS.FSApptLineSplit.TranType : Edm.String
PX.Objects.FS.FSApptLineSplit.PlanType : Edm.String
PX.Objects.FS.FSApptLineSplit.PlanID : Edm.Int64
PX.Objects.FS.FSApptLineSplit.LastLotSerialNbr : Edm.String
PX.Objects.FS.FSApptLineSplit.LotSerClassID : Edm.String
PX.Objects.FS.FSApptLineSplit.AssignedNbr : Edm.String
PX.Objects.FS.FSApptLineSplit.UOM : Edm.String "UOM"
PX.Objects.FS.FSApptLineSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.FS.FSApptLineSplit.BaseQty : Edm.Decimal
PX.Objects.FS.FSApptLineSplit.ApptDate : Edm.DateTimeOffset
PX.Objects.FS.FSApptLineSplit.Confirmed : Edm.Boolean "Confirmed"
PX.Objects.FS.FSApptLineSplit.Released : Edm.Boolean "Released"
PX.Objects.FS.FSApptLineSplit.IsUnassigned : Edm.Boolean [required]
PX.Objects.FS.FSApptLineSplit.ProjectID : Edm.Int32
PX.Objects.FS.FSApptLineSplit.TaskID : Edm.Int32
PX.Objects.FS.FSApptLineSplit.CostCenterID : Edm.Int32 [required]
PX.Objects.FS.FSApptLineSplit.POCreate : Edm.Boolean "Mark for PO"
PX.Objects.FS.FSApptLineSplit.POCompleted : Edm.Boolean
PX.Objects.FS.FSApptLineSplit.POCancelled : Edm.Boolean
PX.Objects.FS.FSApptLineSplit.POSource : Edm.String
PX.Objects.FS.FSApptLineSplit.VendorID : Edm.Int32
PX.Objects.FS.FSApptLineSplit.POSiteID : Edm.Int32
PX.Objects.FS.FSApptLineSplit.POType : Edm.String "PO Type"
PX.Objects.FS.FSApptLineSplit.PONbr : Edm.String "PO Nbr."
PX.Objects.FS.FSApptLineSplit.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.FS.FSApptLineSplit.POReceiptType : Edm.String "PO Receipt Type"
PX.Objects.FS.FSApptLineSplit.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.FS.FSApptLineSplit.RefNoteID : Edm.Guid "Related Document"
PX.Objects.FS.FSApptLineSplit.CuryInfoID : Edm.Int64
PX.Objects.FS.FSApptLineSplit.UnitCost : Edm.Decimal
PX.Objects.FS.FSApptLineSplit.CuryExtCost : Edm.Decimal "Ext. Cost"
PX.Objects.FS.FSApptLineSplit.ExtCost : Edm.Decimal
PX.Objects.FS.FSApptLineSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSApptLineSplit.CreatedByScreenID : Edm.String
PX.Objects.FS.FSApptLineSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSApptLineSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSApptLineSplit.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSApptLineSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSApptLineSplit.tstamp : Edm.Binary
PX.Objects.FS.FSApptLineSplit.CuryID : Edm.String "Currency"
PX.Objects.FS.FSApptLineSplit.CuryRate : Edm.Decimal
PX.Objects.FS.FSApptLineSplit.CuryViewState : Edm.Boolean
PX.Objects.FS.FSApptLineSplit.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.FS.FSApptLineSplit.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.FS.FSApptLineSplit.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.FS.FSApptLineSplit.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.FS.FSApptLineSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSApptLineSplit.FSAppointmentByApptNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, ApptNbr=RefNbr)
PX.Objects.FS.FSApptLineSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSApptLineSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSApptLineSplit.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.FS.FSApptLineSplit.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.FS.FSApptLineSplit.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.FS.FSApptLineSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.FS.FSApptLineSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.FS.FSApptLineSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSApptLineSplit.INSiteByPOSiteID -> PX.Objects.IN.INSite (POSiteID=SiteID)
PX.Objects.FS.FSApptLineSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.FS.FSApptLineSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.FS.FSApptLineSplit.FSAppointmentDetByLineNbr -> PX.Objects.FS.FSAppointmentDet (SrvOrdType=SrvOrdType, ApptNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.FS.FSApptLineSplit.FSSODetSplitByOrigSplitLineNbr -> PX.Objects.FS.FSSODetSplit (OrigSrvOrdType=SrvOrdType, OrigSrvOrdNbr=RefNbr, OrigLineNbr=LineNbr, OrigSplitLineNbr=SplitLineNbr)
PX.Objects.FS.FSApptLineSplit.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.FS.FSApptLineSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.FS.FSApptLineSplit.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)

# PX.Objects.FS.FSBillHistory (EntityType)

Label: "Field Service Billing History"
Key: RecordID
Entity sets: PX_Objects_FS_FSBillHistory, FieldServiceBillingHistory, FSBillHistory
Non-filterable, non-selectable: ChildDocLink, ParentDocLink, ChildDocDesc, ChildDocDate, ChildDocStatus, IsChildDocDeleted, ChildAmount, ServiceContractPeriodID, ContractPeriodStatus, RelatedDocument

PX.Objects.FS.FSBillHistory.RecordID : Edm.Int32 [key]
PX.Objects.FS.FSBillHistory.BatchID : Edm.Int32 "Batch Nbr."
PX.Objects.FS.FSBillHistory.SrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSBillHistory.ServiceOrderRefNbr : Edm.String "Service Order Nbr."
PX.Objects.FS.FSBillHistory.AppointmentRefNbr : Edm.String "Appointment Nbr."
PX.Objects.FS.FSBillHistory.ServiceContractRefNbr : Edm.String "Service Contract Nbr."
PX.Objects.FS.FSBillHistory.ParentEntityType : Edm.String "Origin Entity Type"
PX.Objects.FS.FSBillHistory.ParentDocType : Edm.String "Origin Doc Type"
PX.Objects.FS.FSBillHistory.ParentRefNbr : Edm.String "Origin Doc Nbr."
PX.Objects.FS.FSBillHistory.ChildEntityType : Edm.String "Doc. Type"
PX.Objects.FS.FSBillHistory.ChildDocType : Edm.String "Created Doc. Type"
PX.Objects.FS.FSBillHistory.ChildRefNbr : Edm.String "Created Doc. Nbr."
PX.Objects.FS.FSBillHistory.ChildDocLink : Edm.String "Reference Nbr."
PX.Objects.FS.FSBillHistory.ParentDocLink : Edm.String "Origin Doc. Ref. Nbr."
PX.Objects.FS.FSBillHistory.ChildDocDesc : Edm.String "Description"
PX.Objects.FS.FSBillHistory.ChildDocDate : Edm.DateTimeOffset "Date"
PX.Objects.FS.FSBillHistory.ChildDocStatus : Edm.String "Status"
PX.Objects.FS.FSBillHistory.IsChildDocDeleted : Edm.Boolean
PX.Objects.FS.FSBillHistory.ChildAmount : Edm.Decimal "Amount"
PX.Objects.FS.FSBillHistory.ServiceContractPeriodID : Edm.Int32 "Service Contract Billing Period"
PX.Objects.FS.FSBillHistory.ContractPeriodStatus : Edm.String "Contract Period Status"
PX.Objects.FS.FSBillHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSBillHistory.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSBillHistory.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSBillHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSBillHistory.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSBillHistory.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSBillHistory.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSBillHistory.RelatedDocument : Edm.String "Svc. Ref. Nbr."
PX.Objects.FS.FSBillHistory.FSAppointmentByAppointmentRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, AppointmentRefNbr=RefNbr)
PX.Objects.FS.FSBillHistory.FSAppointmentByServiceOrderRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, ServiceOrderRefNbr=RefNbr)
PX.Objects.FS.FSBillHistory.FSAppointmentBySrvOrdType -> PX.Objects.FS.FSAppointment (AppointmentRefNbr=RefNbr, SrvOrdType=SrvOrdType)
PX.Objects.FS.FSBillHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSBillHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSBillHistory.FSServiceContractByServiceContractRefNbr -> PX.Objects.FS.FSServiceContract (ServiceContractRefNbr=ServiceContractID)
PX.Objects.FS.FSBillHistory.FSServiceOrderBySrvOrdType -> PX.Objects.FS.FSServiceOrder (ServiceOrderRefNbr=RefNbr, SrvOrdType=SrvOrdType)
PX.Objects.FS.FSBillHistory.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSBillingCycle (EntityType)

Label: "Billing Cycle"
Key: BillingCycleCD
Entity sets: PX_Objects_FS_FSBillingCycle, BillingCycle, FSBillingCycle
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSBillingCycle.BillingCycleID : Edm.Int32
PX.Objects.FS.FSBillingCycle.BillingCycleCD : Edm.String [key] "Billing Cycle ID"
PX.Objects.FS.FSBillingCycle.BillingCycleType : Edm.String "Group Billing Documents By"
PX.Objects.FS.FSBillingCycle.Descr : Edm.String "Description"
PX.Objects.FS.FSBillingCycle.InvoiceOnlyCompletedServiceOrder : Edm.Boolean [required] "Bill Only Completed or Closed Service Orders"
PX.Objects.FS.FSBillingCycle.TimeCycleType : Edm.String "Time Cycle Type"
PX.Objects.FS.FSBillingCycle.TimeCycleWeekDay : Edm.Int32 "Day of Week"
PX.Objects.FS.FSBillingCycle.TimeCycleDayOfMonth : Edm.Int32 "Day of Month"
PX.Objects.FS.FSBillingCycle.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSBillingCycle.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSBillingCycle.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSBillingCycle.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSBillingCycle.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSBillingCycle.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSBillingCycle.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSBillingCycle.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSBillingCycle.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSBillingCycle.BillingBy : Edm.String "Run Billing For"
PX.Objects.FS.FSBillingCycle.GroupBillByLocations : Edm.Boolean [required] "Separate Billing Documents by Customer Location"
PX.Objects.FS.FSBillingCycle.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSBillingCycle.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSBillingCycle.AppointmentToPostCollection -> Collection(PX.Objects.FS.AppointmentToPost)
PX.Objects.FS.FSBillingCycle.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.FS.FSBillingCycle.ServiceOrderToPostCollection -> Collection(PX.Objects.FS.ServiceOrderToPost)
PX.Objects.FS.FSBillingCycle.FSCustomerBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerBillingSetup)
PX.Objects.FS.FSBillingCycle.FSCustomerClassBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerClassBillingSetup)
PX.Objects.FS.FSBillingCycle.FSPostBatchCollection -> Collection(PX.Objects.FS.FSPostBatch)

# PX.Objects.FS.FSBLOCAddress (EntityType)

Label: "Field Service Address"
BaseType: PX.Objects.FS.FSAddress
Key: AddressID (inherited from PX.Objects.FS.FSAddress)
Entity sets: PX_Objects_FS_FSBLOCAddress

# PX.Objects.FS.FSBLOCContact (EntityType)

Label: "Field Service Contact"
BaseType: PX.Objects.FS.FSContact
Key: ContactID (inherited from PX.Objects.FS.FSContact)
Entity sets: PX_Objects_FS_FSBLOCContact

# PX.Objects.FS.FSBranchLocation (EntityType)

Label: "Branch Location"
Key: BranchLocationCD
Entity sets: PX_Objects_FS_FSBranchLocation, BranchLocation, FSBranchLocation
Non-filterable, non-selectable: NoteText, RoomFeatureEnabled, DeletedDatabaseRecord

PX.Objects.FS.FSBranchLocation.BranchLocationID : Edm.Int32 "BranchLocationID"
PX.Objects.FS.FSBranchLocation.BranchLocationCD : Edm.String [key] "Branch Location ID"
PX.Objects.FS.FSBranchLocation.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSBranchLocation.BranchLocationAddressID : Edm.Int32
PX.Objects.FS.FSBranchLocation.BranchLocationContactID : Edm.Int32
PX.Objects.FS.FSBranchLocation.AllowOverrideContactAddress : Edm.Boolean "Override"
PX.Objects.FS.FSBranchLocation.Descr : Edm.String "Description"
PX.Objects.FS.FSBranchLocation.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSBranchLocation.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSBranchLocation.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSBranchLocation.CreatedByScreenID : Edm.String
PX.Objects.FS.FSBranchLocation.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSBranchLocation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSBranchLocation.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSBranchLocation.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSBranchLocation.tstamp : Edm.Binary
PX.Objects.FS.FSBranchLocation.DfltUOM : Edm.String "Default Unit"
PX.Objects.FS.FSBranchLocation.RoomFeatureEnabled : Edm.Boolean "Manage Rooms"
PX.Objects.FS.FSBranchLocation.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.FS.FSBranchLocation.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSBranchLocation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSBranchLocation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSBranchLocation.INSiteByDfltSiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSBranchLocation.INSubItemByDfltSubItemID -> PX.Objects.IN.INSubItem
PX.Objects.FS.FSBranchLocation.INUnitByDfltUOM -> PX.Objects.IN.INUnit (DfltUOM=FromUnit)
PX.Objects.FS.FSBranchLocation.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.FS.FSBranchLocation.FSAddressByBranchLocationAddressID -> PX.Objects.FS.FSAddress (BranchLocationAddressID=AddressID)
PX.Objects.FS.FSBranchLocation.FSContactByBranchLocationContactID -> PX.Objects.FS.FSContact (BranchLocationContactID=ContactID)
PX.Objects.FS.FSBranchLocation.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.FS.FSBranchLocation.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSBranchLocation.AppointmentToPostCollection -> Collection(PX.Objects.FS.AppointmentToPost)
PX.Objects.FS.FSBranchLocation.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.FS.FSBranchLocation.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.FS.FSBranchLocation.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.FS.FSBranchLocation.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.FSBranchLocation.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.Objects.FS.FSBranchLocation.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.FS.FSBranchLocation.FSRoomCollection -> Collection(PX.Objects.FS.FSRoom)
PX.Objects.FS.FSBranchLocation.FSRouteCollection -> Collection(PX.Objects.FS.FSRoute)
PX.Objects.FS.FSBranchLocation.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.FS.FSBranchLocation.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.FSBranchLocation.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.FS.FSBranchLocation.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.FS.FSBranchLocation.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)

# PX.Objects.FS.FSCalendarComponentField (EntityType)

Key: ComponentType, FieldName, ObjectName
Entity sets: PX_Objects_FS_FSCalendarComponentField
Non-filterable, non-selectable: LineNbr

PX.Objects.FS.FSCalendarComponentField.ComponentType : Edm.String [key] "Component Type"
PX.Objects.FS.FSCalendarComponentField.LineNbr : Edm.Int32 "LineNbr"
PX.Objects.FS.FSCalendarComponentField.SortOrder : Edm.Int32 [required] "SortOrder"
PX.Objects.FS.FSCalendarComponentField.IsActive : Edm.Boolean [required] "Visible"
PX.Objects.FS.FSCalendarComponentField.ObjectName : Edm.String [key] "Object"
PX.Objects.FS.FSCalendarComponentField.FieldName : Edm.String [key] "Field Name"
PX.Objects.FS.FSCalendarComponentField.ImageUrl : Edm.String "Icon"
PX.Objects.FS.FSCalendarComponentField.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSCalendarComponentField.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSCalendarComponentField.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSCalendarComponentField.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSCalendarComponentField.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSCalendarComponentField.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSCalendarComponentField.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSCalendarComponentField.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSCalendarComponentField.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSContact (EntityType)

Label: "Field Service Contact"
Key: ContactID
Entity sets: PX_Objects_FS_FSContact, FieldServiceContact, FSContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.FS.FSContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.FS.FSContact.EntityType : Edm.String "Entity Type"
PX.Objects.FS.FSContact.FirstName : Edm.String "First Name"
PX.Objects.FS.FSContact.LastName : Edm.String "Last Name"
PX.Objects.FS.FSContact.MidName : Edm.String "Middle Name"
PX.Objects.FS.FSContact.DisplayName : Edm.String "Display Name"
PX.Objects.FS.FSContact.WebSite : Edm.String "Web"
PX.Objects.FS.FSContact.BAccountID : Edm.Int32
PX.Objects.FS.FSContact.BAccountContactID : Edm.Int32
PX.Objects.FS.FSContact.BAccountLocationID : Edm.Int32
PX.Objects.FS.FSContact.IsDefaultContact : Edm.Boolean
PX.Objects.FS.FSContact.OverrideContact : Edm.Boolean "Override Contact"
PX.Objects.FS.FSContact.RevisionID : Edm.Int32
PX.Objects.FS.FSContact.Title : Edm.String "Title"
PX.Objects.FS.FSContact.Salutation : Edm.String "Job Title"
PX.Objects.FS.FSContact.Attention : Edm.String "Attention"
PX.Objects.FS.FSContact.FullName : Edm.String "Account Name"
PX.Objects.FS.FSContact.Email : Edm.String "Email"
PX.Objects.FS.FSContact.Fax : Edm.String "Fax"
PX.Objects.FS.FSContact.FaxType : Edm.String "Fax Type"
PX.Objects.FS.FSContact.Phone1 : Edm.String "Phone 1"
PX.Objects.FS.FSContact.Phone1Type : Edm.String "Phone 1 Type"
PX.Objects.FS.FSContact.Phone2 : Edm.String "Phone 2"
PX.Objects.FS.FSContact.Phone2Type : Edm.String "Phone 2 Type"
PX.Objects.FS.FSContact.Phone3 : Edm.String "Phone 3"
PX.Objects.FS.FSContact.Phone3Type : Edm.String "Phone 3 Type"
PX.Objects.FS.FSContact.NoteID : Edm.Guid
PX.Objects.FS.FSContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSContact.CreatedByScreenID : Edm.String
PX.Objects.FS.FSContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSContact.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSContact.tstamp : Edm.Binary
PX.Objects.FS.FSContact.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.FS.FSContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSContact.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSContact.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.FS.FSContact.FSManufacturerCollection -> Collection(PX.Objects.FS.FSManufacturer)

# PX.Objects.FS.FSContractAction (EntityType)

Key: RecordID
Entity sets: PX_Objects_FS_FSContractAction

PX.Objects.FS.FSContractAction.ServiceContractID : Edm.Int32 "Service Contract ID"
PX.Objects.FS.FSContractAction.RecordID : Edm.Int32 [key]
PX.Objects.FS.FSContractAction.Type : Edm.String "Type"
PX.Objects.FS.FSContractAction.Action : Edm.String "Action"
PX.Objects.FS.FSContractAction.ActionBusinessDate : Edm.DateTimeOffset "Date"
PX.Objects.FS.FSContractAction.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.FS.FSContractAction.ScheduleChangeRecurrence : Edm.Boolean "Change Recurrence"
PX.Objects.FS.FSContractAction.ScheduleNextExecutionDate : Edm.DateTimeOffset "Effective Recurrence Start Date"
PX.Objects.FS.FSContractAction.ScheduleRecurrenceDescr : Edm.String "Recurrence Description"
PX.Objects.FS.FSContractAction.ScheduleRefNbr : Edm.String "Schedule ID"
PX.Objects.FS.FSContractAction.OrigServiceContractRefNbr : Edm.String "Orig. Service Contract ID"
PX.Objects.FS.FSContractAction.OrigScheduleRefNbr : Edm.String "Orig. Schedule ID"
PX.Objects.FS.FSContractAction.Applied : Edm.Boolean [required] "Applied"
PX.Objects.FS.FSContractAction.CreatedByID : Edm.Guid "Created By ID"
PX.Objects.FS.FSContractAction.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSContractAction.CreatedDateTime : Edm.DateTimeOffset "Created DateTime"
PX.Objects.FS.FSContractAction.LastModifiedByID : Edm.Guid "Last Modified By ID"
PX.Objects.FS.FSContractAction.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSContractAction.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.FS.FSContractAction.tstamp : Edm.Binary
PX.Objects.FS.FSContractAction.FSScheduleByOrigScheduleRefNbr -> PX.Objects.FS.FSSchedule (OrigScheduleRefNbr=RefNbr)
PX.Objects.FS.FSContractAction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContractAction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSContractAction.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID)
PX.Objects.FS.FSContractAction.FSServiceContractByOrigServiceContractRefNbr -> PX.Objects.FS.FSServiceContract (OrigServiceContractRefNbr=RefNbr)

# PX.Objects.FS.FSContractForecast (EntityType)

Key: ForecastID, ServiceContractID
Entity sets: PX_Objects_FS_FSContractForecast

PX.Objects.FS.FSContractForecast.ForecastID : Edm.Guid [key]
PX.Objects.FS.FSContractForecast.ServiceContractID : Edm.Int32 [key]
PX.Objects.FS.FSContractForecast.Active : Edm.Boolean [required] "Active"
PX.Objects.FS.FSContractForecast.LineCntr : Edm.Int32 [required]
PX.Objects.FS.FSContractForecast.DateTimeBegin : Edm.DateTimeOffset "Start Time"
PX.Objects.FS.FSContractForecast.DateTimeEnd : Edm.DateTimeOffset "End Time"
PX.Objects.FS.FSContractForecast.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSContractForecast.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSContractForecast.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSContractForecast.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSContractForecast.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSContractForecast.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSContractForecast.tstamp : Edm.Binary
PX.Objects.FS.FSContractForecast.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContractForecast.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSContractForecast.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)

# PX.Objects.FS.FSContractForecastDet (EntityType)

Key: ForecastID, LineNbr, ServiceContractID
Entity sets: PX_Objects_FS_FSContractForecastDet

PX.Objects.FS.FSContractForecastDet.ServiceContractID : Edm.Int32 [key]
PX.Objects.FS.FSContractForecastDet.ForecastID : Edm.Guid [key]
PX.Objects.FS.FSContractForecastDet.LineNbr : Edm.Int32 [key]
PX.Objects.FS.FSContractForecastDet.ForecastDetType : Edm.String "Forecast Type"
PX.Objects.FS.FSContractForecastDet.LineType : Edm.String "Line Type"
PX.Objects.FS.FSContractForecastDet.ScheduleID : Edm.Int32
PX.Objects.FS.FSContractForecastDet.ScheduleDetID : Edm.Int32
PX.Objects.FS.FSContractForecastDet.ContractPeriodID : Edm.Int32
PX.Objects.FS.FSContractForecastDet.ContractPeriodDetID : Edm.Int32
PX.Objects.FS.FSContractForecastDet.BillingRule : Edm.String "Billing Rule"
PX.Objects.FS.FSContractForecastDet.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSContractForecastDet.ComponentID : Edm.Int32
PX.Objects.FS.FSContractForecastDet.Occurrences : Edm.Int32
PX.Objects.FS.FSContractForecastDet.UOM : Edm.String "UOM"
PX.Objects.FS.FSContractForecastDet.UnitPrice : Edm.Decimal "Unit Price"
PX.Objects.FS.FSContractForecastDet.ExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.FS.FSContractForecastDet.OveragePrice : Edm.Decimal "Overage Price"
PX.Objects.FS.FSContractForecastDet.Qty : Edm.Decimal "Quantity"
PX.Objects.FS.FSContractForecastDet.TotalPrice : Edm.Decimal "Total Price per Duration"
PX.Objects.FS.FSContractForecastDet.TranDesc : Edm.String "Description"
PX.Objects.FS.FSContractForecastDet.RecurrenceDesc : Edm.String "Recurrence Description"
PX.Objects.FS.FSContractForecastDet.TimeDuration : Edm.Int32 "Duration"
PX.Objects.FS.FSContractForecastDet.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSContractForecastDet.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSContractForecastDet.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSContractForecastDet.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSContractForecastDet.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSContractForecastDet.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSContractForecastDet.tstamp : Edm.Binary
PX.Objects.FS.FSContractForecastDet.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.FS.FSContractForecastDet.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSContractForecastDet.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSContractForecastDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContractForecastDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSContractForecastDet.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.FS.FSContractForecastDet.FSContractForecastByServiceContractID -> PX.Objects.FS.FSContractForecast (ForecastID=ForecastID, ServiceContractID=ServiceContractID)
PX.Objects.FS.FSContractForecastDet.FSEquipmentComponentBySMequipmentID -> PX.Objects.FS.FSEquipmentComponent (ComponentID=ComponentID)

# PX.Objects.FS.FSContractGenerationHistory (EntityType)

Label: "Contract Generation History"
Key: ContractGenerationHistoryID
Entity sets: PX_Objects_FS_FSContractGenerationHistory, ContractGenerationHistory, FSContractGenerationHistory

PX.Objects.FS.FSContractGenerationHistory.ContractGenerationHistoryID : Edm.Int32 [key] "ContractGenerationHistoryID"
PX.Objects.FS.FSContractGenerationHistory.GenerationID : Edm.Int32 "Generation ID"
PX.Objects.FS.FSContractGenerationHistory.ScheduleID : Edm.Int32 "ScheduleID"
PX.Objects.FS.FSContractGenerationHistory.EntityType : Edm.String "Entity Type"
PX.Objects.FS.FSContractGenerationHistory.LastGeneratedElementDate : Edm.DateTimeOffset "Last Generated Element"
PX.Objects.FS.FSContractGenerationHistory.LastProcessedDate : Edm.DateTimeOffset "Up to Date"
PX.Objects.FS.FSContractGenerationHistory.PreviousGeneratedElementDate : Edm.DateTimeOffset "Previous Generated Element"
PX.Objects.FS.FSContractGenerationHistory.PreviousProcessedDate : Edm.DateTimeOffset "Previous Last Processed"
PX.Objects.FS.FSContractGenerationHistory.RecordType : Edm.String
PX.Objects.FS.FSContractGenerationHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSContractGenerationHistory.CreatedByScreenID : Edm.String
PX.Objects.FS.FSContractGenerationHistory.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSContractGenerationHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSContractGenerationHistory.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSContractGenerationHistory.LastModifiedDateTime : Edm.DateTimeOffset "Generation Date"
PX.Objects.FS.FSContractGenerationHistory.tstamp : Edm.Binary
PX.Objects.FS.FSContractGenerationHistory.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule (ScheduleID=ScheduleID)
PX.Objects.FS.FSContractGenerationHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContractGenerationHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSContractPeriod (EntityType)

Key: ContractPeriodID, ServiceContractID
Entity sets: PX_Objects_FS_FSContractPeriod
Non-filterable, non-selectable: BillingPeriod

PX.Objects.FS.FSContractPeriod.ServiceContractID : Edm.Int32 [key] "Service Contract ID"
PX.Objects.FS.FSContractPeriod.ContractPeriodID : Edm.Int32 [key]
PX.Objects.FS.FSContractPeriod.ContractPostDocID : Edm.Int32
PX.Objects.FS.FSContractPeriod.EndPeriodDate : Edm.DateTimeOffset "End Period Date"
PX.Objects.FS.FSContractPeriod.Invoiced : Edm.Boolean [required] "Invoiced"
PX.Objects.FS.FSContractPeriod.PeriodTotal : Edm.Decimal "Period Total"
PX.Objects.FS.FSContractPeriod.StartPeriodDate : Edm.DateTimeOffset "Start Period Date"
PX.Objects.FS.FSContractPeriod.Status : Edm.String
PX.Objects.FS.FSContractPeriod.CreatedByID : Edm.Guid "Created By ID"
PX.Objects.FS.FSContractPeriod.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSContractPeriod.CreatedDateTime : Edm.DateTimeOffset "Created DateTime"
PX.Objects.FS.FSContractPeriod.LastModifiedByID : Edm.Guid "Last Modified By ID"
PX.Objects.FS.FSContractPeriod.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSContractPeriod.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.FS.FSContractPeriod.tstamp : Edm.Binary
PX.Objects.FS.FSContractPeriod.BillingPeriod : Edm.String "Billing Period"
PX.Objects.FS.FSContractPeriod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContractPeriod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSContractPeriod.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID)
PX.Objects.FS.FSContractPeriod.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.FS.FSContractPeriod.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)

# PX.Objects.FS.FSContractPeriodDet (EntityType)

Label: "Contract Period Detail"
Key: ContractPeriodDetID, ContractPeriodID
Entity sets: PX_Objects_FS_FSContractPeriodDet, ContractPeriodDetail, FSContractPeriodDet
Non-filterable, non-selectable: ScheduledQty, ScheduledTime, SkipCostCodeValidation, Amount, RemainingAmount, UsedAmount, ScheduledAmount

PX.Objects.FS.FSContractPeriodDet.ServiceContractID : Edm.Int32 "Service Contract ID"
PX.Objects.FS.FSContractPeriodDet.ContractPeriodID : Edm.Int32 [key]
PX.Objects.FS.FSContractPeriodDet.ContractPeriodDetID : Edm.Int32 [key]
PX.Objects.FS.FSContractPeriodDet.LineType : Edm.String "Line Type"
PX.Objects.FS.FSContractPeriodDet.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSContractPeriodDet.UOM : Edm.String "UOM"
PX.Objects.FS.FSContractPeriodDet.BillingRule : Edm.String "Billing Rule"
PX.Objects.FS.FSContractPeriodDet.Time : Edm.Int32 "Time"
PX.Objects.FS.FSContractPeriodDet.Qty : Edm.Decimal "Quantity"
PX.Objects.FS.FSContractPeriodDet.UsedQty : Edm.Decimal "Used Period Quantity"
PX.Objects.FS.FSContractPeriodDet.UsedTime : Edm.Int32 "Used Period Time"
PX.Objects.FS.FSContractPeriodDet.RecurringUnitPrice : Edm.Decimal "Recurring Item Price"
PX.Objects.FS.FSContractPeriodDet.RecurringTotalPrice : Edm.Decimal "Total Recurring Price"
PX.Objects.FS.FSContractPeriodDet.OverageItemPrice : Edm.Decimal "Overage Item Price"
PX.Objects.FS.FSContractPeriodDet.Rollover : Edm.Boolean [required] "Rollover"
PX.Objects.FS.FSContractPeriodDet.RemainingQty : Edm.Decimal "Remaining Period Quantity"
PX.Objects.FS.FSContractPeriodDet.RemainingTime : Edm.Int32 "Remaining Period Time"
PX.Objects.FS.FSContractPeriodDet.ScheduledQty : Edm.Decimal "Scheduled Period Quantity"
PX.Objects.FS.FSContractPeriodDet.ScheduledTime : Edm.Int32 "Scheduled Period Time"
PX.Objects.FS.FSContractPeriodDet.DeferredCode : Edm.String "Deferral Code"
PX.Objects.FS.FSContractPeriodDet.ProjectID : Edm.Int32
PX.Objects.FS.FSContractPeriodDet.SkipCostCodeValidation : Edm.Boolean
PX.Objects.FS.FSContractPeriodDet.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSContractPeriodDet.CreatedDateTime : Edm.DateTimeOffset "Created DateTime"
PX.Objects.FS.FSContractPeriodDet.LastModifiedByID : Edm.Guid "Last Modified By ID"
PX.Objects.FS.FSContractPeriodDet.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSContractPeriodDet.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.FS.FSContractPeriodDet.tstamp : Edm.Binary
PX.Objects.FS.FSContractPeriodDet.RegularPrice : Edm.Decimal "Regular Price"
PX.Objects.FS.FSContractPeriodDet.Amount : Edm.String "Value"
PX.Objects.FS.FSContractPeriodDet.RemainingAmount : Edm.String "Remaining Period Value"
PX.Objects.FS.FSContractPeriodDet.UsedAmount : Edm.String "Used Period Value"
PX.Objects.FS.FSContractPeriodDet.ScheduledAmount : Edm.String "Scheduled Period Value"
PX.Objects.FS.FSContractPeriodDet.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.FS.FSContractPeriodDet.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.FS.FSContractPeriodDet.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.FS.FSContractPeriodDet.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSContractPeriodDet.DRDeferredCodeByDeferredCode -> PX.Objects.DR.DRDeferredCode (DeferredCode=DeferredCodeID)
PX.Objects.FS.FSContractPeriodDet.FSEquipmentBySMequipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSContractPeriodDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSContractPeriodDet.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.FS.FSContractPeriodDet.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.FS.FSContractPeriodDet.FSContractPeriodByContractPeriodID -> PX.Objects.FS.FSContractPeriod (ServiceContractID=ServiceContractID, ContractPeriodID=ContractPeriodID)
PX.Objects.FS.FSContractPeriodDet.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID)

# PX.Objects.FS.FSContractPostBatch (EntityType)

Key: ContractPostBatchNbr
Entity sets: PX_Objects_FS_FSContractPostBatch

PX.Objects.FS.FSContractPostBatch.ContractPostBatchID : Edm.Int32 "Contract Post Batch ID"
PX.Objects.FS.FSContractPostBatch.ContractPostBatchNbr : Edm.String [key] "Batch Nbr."
PX.Objects.FS.FSContractPostBatch.FinPeriodID : Edm.String "Billing Period"
PX.Objects.FS.FSContractPostBatch.InvoiceDate : Edm.DateTimeOffset "Billing Date"
PX.Objects.FS.FSContractPostBatch.PostTo : Edm.String "Generated In"
PX.Objects.FS.FSContractPostBatch.UpToDate : Edm.DateTimeOffset "Up to Date"
PX.Objects.FS.FSContractPostBatch.CreatedByID : Edm.Guid "Created On"
PX.Objects.FS.FSContractPostBatch.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSContractPostBatch.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSContractPostBatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSContractPostBatch.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSContractPostBatch.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSContractPostBatch.tstamp : Edm.Binary
PX.Objects.FS.FSContractPostBatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContractPostBatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSContractPostBatch.FSContractPostDocCollection -> Collection(PX.Objects.FS.FSContractPostDoc)
PX.Objects.FS.FSContractPostBatch.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)

# PX.Objects.FS.FSContractPostDet (EntityType)

Key: ContractPostDetID
Entity sets: PX_Objects_FS_FSContractPostDet

PX.Objects.FS.FSContractPostDet.ContractPostDetID : Edm.Int32 [key]
PX.Objects.FS.FSContractPostDet.AppDetID : Edm.Int32
PX.Objects.FS.FSContractPostDet.AppointmentID : Edm.Int32
PX.Objects.FS.FSContractPostDet.ContractPeriodDetID : Edm.Int32
PX.Objects.FS.FSContractPostDet.ContractPeriodID : Edm.Int32 "Contract Period Nbr."
PX.Objects.FS.FSContractPostDet.ContractPostBatchID : Edm.Int32
PX.Objects.FS.FSContractPostDet.ContractPostDocID : Edm.Int32 "Contract PostDoc Nbr."
PX.Objects.FS.FSContractPostDet.SODetID : Edm.Int32
PX.Objects.FS.FSContractPostDet.SOID : Edm.Int32
PX.Objects.FS.FSContractPostDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSContractPostDet.CreatedByScreenID : Edm.String
PX.Objects.FS.FSContractPostDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSContractPostDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSContractPostDet.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSContractPostDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSContractPostDet.tstamp : Edm.Binary
PX.Objects.FS.FSContractPostDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContractPostDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSContractPostDoc (EntityType)

Key: ContractPostDocID
Entity sets: PX_Objects_FS_FSContractPostDoc

PX.Objects.FS.FSContractPostDoc.ContractPostDocID : Edm.Int32 [key]
PX.Objects.FS.FSContractPostDoc.ContractPeriodID : Edm.Int32 "Contract Period Nbr."
PX.Objects.FS.FSContractPostDoc.ContractPostBatchID : Edm.Int32
PX.Objects.FS.FSContractPostDoc.PostDocType : Edm.String "Document Type"
PX.Objects.FS.FSContractPostDoc.PostedTO : Edm.String "Posted to"
PX.Objects.FS.FSContractPostDoc.PostRefNbr : Edm.String "Document Nbr."
PX.Objects.FS.FSContractPostDoc.ServiceContractID : Edm.Int32 "Service Contract ID"
PX.Objects.FS.FSContractPostDoc.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSContractPostDoc.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSContractPostDoc.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSContractPostDoc.tstamp : Edm.Binary
PX.Objects.FS.FSContractPostDoc.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSContractPostDoc.FSContractPostBatchByContractPostBatchID -> PX.Objects.FS.FSContractPostBatch (ContractPostBatchID=ContractPostBatchID)
PX.Objects.FS.FSContractPostDoc.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID)
PX.Objects.FS.FSContractPostDoc.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)

# PX.Objects.FS.FSContractPostRegister (EntityType)

Key: ContractPeriodID, ServiceContractID
Entity sets: PX_Objects_FS_FSContractPostRegister

PX.Objects.FS.FSContractPostRegister.ContractPeriodID : Edm.Int32 [key] "Contract Period ID"
PX.Objects.FS.FSContractPostRegister.ContractPostBatchID : Edm.Int32
PX.Objects.FS.FSContractPostRegister.PostDocType : Edm.String
PX.Objects.FS.FSContractPostRegister.PostedTO : Edm.String
PX.Objects.FS.FSContractPostRegister.PostRefNbr : Edm.String
PX.Objects.FS.FSContractPostRegister.ServiceContractID : Edm.Int32 [key] "Service Contract ID"

# PX.Objects.FS.FSContractSchedule (EntityType)

BaseType: PX.Objects.FS.FSSchedule
Key: CustomerID, RefNbr (inherited from PX.Objects.FS.FSSchedule)
Entity sets: PX_Objects_FS_FSContractSchedule
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FS.FSContractSchedule.FormCaptionDescription : Edm.String

# PX.Objects.FS.FSCreatedDoc (EntityType)

Key: RecordID
Entity sets: PX_Objects_FS_FSCreatedDoc

PX.Objects.FS.FSCreatedDoc.BatchID : Edm.Int32
PX.Objects.FS.FSCreatedDoc.RecordID : Edm.Int32 [key]
PX.Objects.FS.FSCreatedDoc.PostTo : Edm.String "Document"
PX.Objects.FS.FSCreatedDoc.CreatedDocType : Edm.String "Document Type"
PX.Objects.FS.FSCreatedDoc.CreatedRefNbr : Edm.String "Document Nbr."
PX.Objects.FS.FSCreatedDoc.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSCreatedDoc.CreatedByScreenID : Edm.String
PX.Objects.FS.FSCreatedDoc.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSCreatedDoc.tstamp : Edm.Binary
PX.Objects.FS.FSCreatedDoc.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Objects.FS.FSCustomer (EntityType)

Label: "Customer"
BaseType: PX.Objects.AR.Customer
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_FS_FSCustomer

# PX.Objects.FS.FSCustomerBillingSetup (EntityType)

Label: "FSCustomerBillingSetup"
Key: CBID
Entity sets: PX_Objects_FS_FSCustomerBillingSetup, FSCustomerBillingSetup

PX.Objects.FS.FSCustomerBillingSetup.CustomerID : Edm.Int32
PX.Objects.FS.FSCustomerBillingSetup.CBID : Edm.Int32 [key]
PX.Objects.FS.FSCustomerBillingSetup.Active : Edm.Boolean [required] "Active"
PX.Objects.FS.FSCustomerBillingSetup.SrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSCustomerBillingSetup.BillingCycleID : Edm.Int32 "Billing Cycle"
PX.Objects.FS.FSCustomerBillingSetup.FrequencyType : Edm.String "Frequency Type"
PX.Objects.FS.FSCustomerBillingSetup.WeeklyFrequency : Edm.Int32 "Frequency Week Day"
PX.Objects.FS.FSCustomerBillingSetup.MonthlyFrequency : Edm.Int32 "Frequency Month Day"
PX.Objects.FS.FSCustomerBillingSetup.SendInvoicesTo : Edm.String "Bill-To Address"
PX.Objects.FS.FSCustomerBillingSetup.BillShipmentSource : Edm.String "Ship-To Address"
PX.Objects.FS.FSCustomerBillingSetup.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSCustomerBillingSetup.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSCustomerBillingSetup.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSCustomerBillingSetup.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSCustomerBillingSetup.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSCustomerBillingSetup.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSCustomerBillingSetup.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSCustomerBillingSetup.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSCustomerBillingSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSCustomerBillingSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSCustomerBillingSetup.FSBillingCycleByBillingCycleID -> PX.Objects.FS.FSBillingCycle (BillingCycleID=BillingCycleID)
PX.Objects.FS.FSCustomerBillingSetup.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSCustomerBillingSetup.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)

# PX.Objects.FS.FSCustomerClassBillingSetup (EntityType)

Label: "FSCustomerClassBillingSetup"
Key: CBID, CustomerClassID
Entity sets: PX_Objects_FS_FSCustomerClassBillingSetup, FSCustomerClassBillingSetup

PX.Objects.FS.FSCustomerClassBillingSetup.CustomerClassID : Edm.String [key]
PX.Objects.FS.FSCustomerClassBillingSetup.CBID : Edm.Int32 [key]
PX.Objects.FS.FSCustomerClassBillingSetup.SrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSCustomerClassBillingSetup.BillingCycleID : Edm.Int32 "Billing Cycle"
PX.Objects.FS.FSCustomerClassBillingSetup.FrequencyType : Edm.String "Frequency Type"
PX.Objects.FS.FSCustomerClassBillingSetup.SendInvoicesTo : Edm.String "Bill-To Address"
PX.Objects.FS.FSCustomerClassBillingSetup.BillShipmentSource : Edm.String "Ship-To Address"
PX.Objects.FS.FSCustomerClassBillingSetup.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSCustomerClassBillingSetup.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSCustomerClassBillingSetup.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSCustomerClassBillingSetup.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSCustomerClassBillingSetup.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSCustomerClassBillingSetup.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSCustomerClassBillingSetup.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSCustomerClassBillingSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSCustomerClassBillingSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSCustomerClassBillingSetup.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass (CustomerClassID=CustomerClassID)
PX.Objects.FS.FSCustomerClassBillingSetup.FSBillingCycleByBillingCycleID -> PX.Objects.FS.FSBillingCycle (BillingCycleID=BillingCycleID)
PX.Objects.FS.FSCustomerClassBillingSetup.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSDetailFSLogAction (EntityType)

Key: LineNbr, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSDetailFSLogAction

PX.Objects.FS.FSDetailFSLogAction.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSDetailFSLogAction.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.FSDetailFSLogAction.AppointmentID : Edm.Int32 "Appointment Nbr."
PX.Objects.FS.FSDetailFSLogAction.AppDetID : Edm.Int32
PX.Objects.FS.FSDetailFSLogAction.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.FSDetailFSLogAction.SODetID : Edm.Int32 "Service Order Detail Ref. Nbr."
PX.Objects.FS.FSDetailFSLogAction.LineRef : Edm.String "Detail Ref. Nbr."
PX.Objects.FS.FSDetailFSLogAction.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSDetailFSLogAction.Descr : Edm.String "Description"
PX.Objects.FS.FSDetailFSLogAction.EstimatedDuration : Edm.Int32 "Estimated Duration"
PX.Objects.FS.FSDetailFSLogAction.IsTravelItem : Edm.Boolean "Is a Travel Item"
PX.Objects.FS.FSDetailFSLogAction.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSDetailFSLogAction.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSDetailFSLogAction.FSSODetBySODetID -> PX.Objects.FS.FSSODet (SODetID=SODetID)
PX.Objects.FS.FSDetailFSLogAction.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSDetailFSLogAction.InventoryItemByPickupDeliveryServiceID -> PX.Objects.IN.InventoryItem
PX.Objects.FS.FSDetailFSLogAction.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.FS.FSDetailFSLogAction.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.FSDetailFSLogAction.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSDetailFSLogAction.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.FSDetailFSLogAction.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)

# PX.Objects.FS.FSDiscountDetail (EntityType)

Key: EntityType, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSDiscountDetail
Non-filterable, non-selectable: IsOrigDocDiscount

PX.Objects.FS.FSDiscountDetail.RecordID : Edm.Int32
PX.Objects.FS.FSDiscountDetail.LineNbr : Edm.Int32
PX.Objects.FS.FSDiscountDetail.SkipDiscount : Edm.Boolean [required] "Skip Discount"
PX.Objects.FS.FSDiscountDetail.EntityType : Edm.String [key] "EntityType"
PX.Objects.FS.FSDiscountDetail.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSDiscountDetail.RefNbr : Edm.String [key] "Order Nbr."
PX.Objects.FS.FSDiscountDetail.DiscountID : Edm.String "Discount Code"
PX.Objects.FS.FSDiscountDetail.DiscountSequenceID : Edm.String "Sequence ID"
PX.Objects.FS.FSDiscountDetail.Type : Edm.String "Type"
PX.Objects.FS.FSDiscountDetail.ManualOrder : Edm.Int16 "Line Nbr."
PX.Objects.FS.FSDiscountDetail.CuryInfoID : Edm.Int64
PX.Objects.FS.FSDiscountDetail.DiscountableAmt : Edm.Decimal
PX.Objects.FS.FSDiscountDetail.CuryDiscountableAmt : Edm.Decimal "Discountable Amt."
PX.Objects.FS.FSDiscountDetail.DiscountableQty : Edm.Decimal "Discountable Qty."
PX.Objects.FS.FSDiscountDetail.DiscountAmt : Edm.Decimal
PX.Objects.FS.FSDiscountDetail.CuryDiscountAmt : Edm.Decimal "Discount Amt."
PX.Objects.FS.FSDiscountDetail.DiscountPct : Edm.Decimal "Discount Percent"
PX.Objects.FS.FSDiscountDetail.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.FS.FSDiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.FS.FSDiscountDetail.IsManual : Edm.Boolean [required] "Manual Discount"
PX.Objects.FS.FSDiscountDetail.IsOrigDocDiscount : Edm.Boolean
PX.Objects.FS.FSDiscountDetail.ExtDiscCode : Edm.String "External Discount Code"
PX.Objects.FS.FSDiscountDetail.Description : Edm.String "Description"
PX.Objects.FS.FSDiscountDetail.tstamp : Edm.Binary
PX.Objects.FS.FSDiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSDiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.FS.FSDiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSDiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSDiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSDiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSDiscountDetail.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.FS.FSDiscountDetail.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSDiscountDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSDiscountDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSDiscountDetail.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.FS.FSDiscountDetail.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)
PX.Objects.FS.FSDiscountDetail.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, RefNbr=RefNbr)

# PX.Objects.FS.FSEmployeeSkill (EntityType)

Key: EmployeeID, SkillID
Entity sets: PX_Objects_FS_FSEmployeeSkill
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSEmployeeSkill.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.FS.FSEmployeeSkill.SkillID : Edm.Int32 [key] "Skill ID"
PX.Objects.FS.FSEmployeeSkill.NoteID : Edm.Guid
PX.Objects.FS.FSEmployeeSkill.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSEmployeeSkill.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSEmployeeSkill.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSEmployeeSkill.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSEmployeeSkill.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSEmployeeSkill.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSEmployeeSkill.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSEmployeeSkill.tstamp : Edm.Binary
PX.Objects.FS.FSEmployeeSkill.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.FS.FSEmployeeSkill.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.FS.FSEmployeeSkill.FSSkillBySkillID -> PX.Objects.SV.FSSkill (SkillID=SkillID)
PX.Objects.FS.FSEmployeeSkill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSEmployeeSkill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSEquipment (EntityType)

Label: "Equipment"
Key: RefNbr
Entity sets: PX_Objects_FS_FSEquipment, Equipment1, FSEquipment
Non-filterable, non-selectable: NoteText, MemDescription, MemReplacedEquipment, MemDescrVehicle, MemDescrAdditionalVehicle1, ReportSMEquipmentID, FixedAssetCD, DeletedDatabaseRecord

PX.Objects.FS.FSEquipment.RefNbr : Edm.String [key] "Equipment Nbr."
PX.Objects.FS.FSEquipment.SMEquipmentID : Edm.Int32
PX.Objects.FS.FSEquipment.Barcode : Edm.String "Barcode"
PX.Objects.FS.FSEquipment.IsVehicle : Edm.Boolean [required] "Vehicle"
PX.Objects.FS.FSEquipment.ManufacturerID : Edm.Int32 "Manufacturer"
PX.Objects.FS.FSEquipment.ManufacturerModelID : Edm.Int32 "Manufacturer Model"
PX.Objects.FS.FSEquipment.PropertyType : Edm.String "Property Type"
PX.Objects.FS.FSEquipment.SerialNumber : Edm.String "Serial Nbr."
PX.Objects.FS.FSEquipment.Status : Edm.String "Status"
PX.Objects.FS.FSEquipment.TagNbr : Edm.String "Tag Nbr."
PX.Objects.FS.FSEquipment.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSEquipment.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSEquipment.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSEquipment.CreatedByScreenID : Edm.String
PX.Objects.FS.FSEquipment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSEquipment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSEquipment.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSEquipment.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSEquipment.tstamp : Edm.Binary
PX.Objects.FS.FSEquipment.EquipmentTypeID : Edm.Int32 "Equipment Type"
PX.Objects.FS.FSEquipment.SourceID : Edm.Int32
PX.Objects.FS.FSEquipment.SourceDocType : Edm.String "Document Type"
PX.Objects.FS.FSEquipment.SourceRefNbr : Edm.String "Document Ref. Nbr."
PX.Objects.FS.FSEquipment.SourceType : Edm.String "Document Type"
PX.Objects.FS.FSEquipment.ManufacturingYear : Edm.String "Manufacturing Year"
PX.Objects.FS.FSEquipment.DateInstalled : Edm.DateTimeOffset "Installation Date"
PX.Objects.FS.FSEquipment.VendorID : Edm.Int32 "Vendor"
PX.Objects.FS.FSEquipment.PurchDate : Edm.DateTimeOffset "Purchase Date"
PX.Objects.FS.FSEquipment.PurchPONumber : Edm.String "Purchase Order Nbr."
PX.Objects.FS.FSEquipment.PurchAmount : Edm.Decimal "Purchase Amount"
PX.Objects.FS.FSEquipment.RegistrationNbr : Edm.String "Registration Nbr."
PX.Objects.FS.FSEquipment.RegisteredDate : Edm.DateTimeOffset "Registered Date"
PX.Objects.FS.FSEquipment.Axles : Edm.Int16 [required] "Axles"
PX.Objects.FS.FSEquipment.FuelType : Edm.String "Fuel Type"
PX.Objects.FS.FSEquipment.FuelTank1 : Edm.Decimal [required] "Tank 1 - Gallons"
PX.Objects.FS.FSEquipment.FuelTank2 : Edm.Decimal [required] "Tank 2 - Gallons"
PX.Objects.FS.FSEquipment.GrossVehicleWeight : Edm.Decimal [required] "Gross Vehicle Weight"
PX.Objects.FS.FSEquipment.MaxMiles : Edm.Decimal [required] "Max Miles"
PX.Objects.FS.FSEquipment.TareWeight : Edm.Decimal [required] "Tare Weight"
PX.Objects.FS.FSEquipment.WeightCapacity : Edm.Decimal [required] "Weight Capacity"
PX.Objects.FS.FSEquipment.CustomerID : Edm.Int32 "Customer"
PX.Objects.FS.FSEquipment.Descr : Edm.String "Description"
PX.Objects.FS.FSEquipment.VehicleTypeID : Edm.Int32 "Vehicle Type ID"
PX.Objects.FS.FSEquipment.Color : Edm.Int32 "Color"
PX.Objects.FS.FSEquipment.EngineNo : Edm.String "Engine Nbr."
PX.Objects.FS.FSEquipment.InventoryID : Edm.Int32 "Model Equipment"
PX.Objects.FS.FSEquipment.OwnerType : Edm.String "Owner Type"
PX.Objects.FS.FSEquipment.OwnerID : Edm.Int32 "Customer"
PX.Objects.FS.FSEquipment.INSerialNumber : Edm.String "Model Serial Nbr."
PX.Objects.FS.FSEquipment.RequireMaintenance : Edm.Boolean [required] "Target Equipment"
PX.Objects.FS.FSEquipment.ResourceEquipment : Edm.Boolean [required] "Resource Equipment"
PX.Objects.FS.FSEquipment.SalesDate : Edm.DateTimeOffset "Sales Date"
PX.Objects.FS.FSEquipment.ARTranLineNbr : Edm.Int32
PX.Objects.FS.FSEquipment.LocationType : Edm.String "Location Type"
PX.Objects.FS.FSEquipment.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSEquipment.BranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.FSEquipment.InstSrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSEquipment.InstServiceOrderRefNbr : Edm.String "Service Order Nbr."
PX.Objects.FS.FSEquipment.InstAppointmentRefNbr : Edm.String "Appointment Nbr."
PX.Objects.FS.FSEquipment.DisposalDate : Edm.DateTimeOffset "Disposal Date"
PX.Objects.FS.FSEquipment.ReplaceEquipmentID : Edm.Int32 "Replacement Equipment Nbr."
PX.Objects.FS.FSEquipment.DispSrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSEquipment.DispServiceOrderRefNbr : Edm.String "Service Order Nbr."
PX.Objects.FS.FSEquipment.DispAppointmentRefNbr : Edm.String "Appointment Nbr."
PX.Objects.FS.FSEquipment.CpnyWarrantyValue : Edm.Int32 "Company Warranty"
PX.Objects.FS.FSEquipment.CpnyWarrantyType : Edm.String "CpnyWarrantyType"
PX.Objects.FS.FSEquipment.CpnyWarrantyEndDate : Edm.DateTimeOffset "Company Warranty End Date"
PX.Objects.FS.FSEquipment.VendorWarrantyValue : Edm.Int32 "Vendor Warranty"
PX.Objects.FS.FSEquipment.VendorWarrantyType : Edm.String "VendorWarrantyType"
PX.Objects.FS.FSEquipment.VendorWarrantyEndDate : Edm.DateTimeOffset "Vendor Warranty End Date"
PX.Objects.FS.FSEquipment.SalesOrderType : Edm.String "Sales Order Type"
PX.Objects.FS.FSEquipment.SalesOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.FS.FSEquipment.EquipmentReplacedID : Edm.Int32 "Equipment Replaced"
PX.Objects.FS.FSEquipment.ImageUrl : Edm.String "Image"
PX.Objects.FS.FSEquipment.EquipmentTypeCD : Edm.String "EquipmentTypeCD"
PX.Objects.FS.FSEquipment.MemDescription : Edm.String "Equipment Description"
PX.Objects.FS.FSEquipment.MemReplacedEquipment : Edm.String "Suspended Target Equipment ID"
PX.Objects.FS.FSEquipment.MemDescrVehicle : Edm.String "Vehicle Description"
PX.Objects.FS.FSEquipment.MemDescrAdditionalVehicle1 : Edm.String "Additional Vehicle 1 Description"
PX.Objects.FS.FSEquipment.ReportSMEquipmentID : Edm.Int32
PX.Objects.FS.FSEquipment.FixedAssetCD : Edm.String "Fixed Asset"
PX.Objects.FS.FSEquipment.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.FS.FSEquipment.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.FS.FSEquipment.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSEquipment.CustomerByOwnerID -> PX.Objects.AR.Customer (OwnerID=BAccountID)
PX.Objects.FS.FSEquipment.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSEquipment.FSEquipmentBySMequipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSEquipment.FSAppointmentByInstAppointmentRefNbr -> PX.Objects.FS.FSAppointment (InstSrvOrdType=SrvOrdType, InstAppointmentRefNbr=RefNbr)
PX.Objects.FS.FSEquipment.FSAppointmentByDispAppointmentRefNbr -> PX.Objects.FS.FSAppointment (DispSrvOrdType=SrvOrdType, DispAppointmentRefNbr=RefNbr)
PX.Objects.FS.FSEquipment.FSAppointmentByInstSrvOrdType -> PX.Objects.FS.FSAppointment (InstAppointmentRefNbr=RefNbr, InstSrvOrdType=SrvOrdType)
PX.Objects.FS.FSEquipment.FSAppointmentByDispSrvOrdType -> PX.Objects.FS.FSAppointment (DispAppointmentRefNbr=RefNbr, DispSrvOrdType=SrvOrdType)
PX.Objects.FS.FSEquipment.SOOrderBySalesOrderType -> PX.Objects.SO.SOOrder (SalesOrderNbr=OrderNbr, SalesOrderType=OrderType)
PX.Objects.FS.FSEquipment.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSEquipment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSEquipment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSEquipment.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.FS.FSEquipment.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.FS.FSEquipment.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSEquipment.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.FS.FSEquipment.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.FSEquipment.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.FSEquipment.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.FSEquipment.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.FSEquipment.FSEquipmentTypeByEquipmentTypeID -> PX.Objects.FS.FSEquipmentType (EquipmentTypeID=EquipmentTypeCD)
PX.Objects.FS.FSEquipment.FSManufacturerByManufacturerID -> PX.Objects.FS.FSManufacturer (ManufacturerID=ManufacturerID)
PX.Objects.FS.FSEquipment.FSManufacturerModelByManufacturerModelID -> PX.Objects.FS.FSManufacturerModel (ManufacturerID=ManufacturerID, ManufacturerModelID=ManufacturerModelCD)
PX.Objects.FS.FSEquipment.FSManufacturerModelByManufacturerID -> PX.Objects.FS.FSManufacturerModel (ManufacturerModelID=ManufacturerModelID, ManufacturerID=ManufacturerID)
PX.Objects.FS.FSEquipment.FSServiceOrderByInstServiceOrderRefNbr -> PX.Objects.FS.FSServiceOrder (InstSrvOrdType=SrvOrdType, InstServiceOrderRefNbr=RefNbr)
PX.Objects.FS.FSEquipment.FSServiceOrderByDispServiceOrderRefNbr -> PX.Objects.FS.FSServiceOrder (DispSrvOrdType=SrvOrdType, DispServiceOrderRefNbr=RefNbr)
PX.Objects.FS.FSEquipment.FSServiceOrderByInstSrvOrdType -> PX.Objects.FS.FSServiceOrder (InstServiceOrderRefNbr=RefNbr, InstSrvOrdType=SrvOrdType)
PX.Objects.FS.FSEquipment.FSServiceOrderByDispSrvOrdType -> PX.Objects.FS.FSServiceOrder (DispServiceOrderRefNbr=RefNbr, DispSrvOrdType=SrvOrdType)
PX.Objects.FS.FSEquipment.FSVehicleTypeByVehicleTypeID -> PX.Objects.FS.FSVehicleType (VehicleTypeID=VehicleTypeID)
PX.Objects.FS.FSEquipment.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.FSEquipment.FSRouteDocumentCollection -> Collection(PX.Objects.FS.FSRouteDocument)
PX.Objects.FS.FSEquipment.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSEquipment.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.FSEquipment.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.FSEquipment.FSAppointmentResourceCollection -> Collection(PX.Objects.FS.FSAppointmentResource)
PX.Objects.FS.FSEquipment.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.FSEquipment.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.FS.FSEquipment.FSSOResourceCollection -> Collection(PX.Objects.FS.FSSOResource)
PX.Objects.FS.FSEquipment.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.FSEquipment.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)

# PX.Objects.FS.FSEquipmentComponent (EntityType)

Label: "FSEquipmentComponent"
Key: LineNbr, SMEquipmentID
Entity sets: PX_Objects_FS_FSEquipmentComponent, FSEquipmentComponent
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSEquipmentComponent.SMEquipmentID : Edm.Int32 [key] "Equipment ID"
PX.Objects.FS.FSEquipmentComponent.LineNbr : Edm.Int32 [key]
PX.Objects.FS.FSEquipmentComponent.LineRef : Edm.String "Ref. Nbr."
PX.Objects.FS.FSEquipmentComponent.ComponentID : Edm.Int32 "Component ID"
PX.Objects.FS.FSEquipmentComponent.CpnyWarrantyDuration : Edm.Int32 "Company Warranty"
PX.Objects.FS.FSEquipmentComponent.CpnyWarrantyEndDate : Edm.DateTimeOffset "Company Warranty End Date"
PX.Objects.FS.FSEquipmentComponent.InstallationDate : Edm.DateTimeOffset "Installation Date"
PX.Objects.FS.FSEquipmentComponent.LastReplacementDate : Edm.DateTimeOffset "Last Replacement Date"
PX.Objects.FS.FSEquipmentComponent.LongDescr : Edm.String "Description"
PX.Objects.FS.FSEquipmentComponent.VendorID : Edm.Int32 "Vendor ID"
PX.Objects.FS.FSEquipmentComponent.VendorWarrantyDuration : Edm.Int32 "Vendor Warranty"
PX.Objects.FS.FSEquipmentComponent.VendorWarrantyEndDate : Edm.DateTimeOffset "Vendor Warranty End Date"
PX.Objects.FS.FSEquipmentComponent.SerialNumber : Edm.String "Serial Nbr."
PX.Objects.FS.FSEquipmentComponent.RequireSerial : Edm.Boolean [required] "Requires Serial Nbr."
PX.Objects.FS.FSEquipmentComponent.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.FS.FSEquipmentComponent.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSEquipmentComponent.CpnyWarrantyType : Edm.String "Company Warranty Type"
PX.Objects.FS.FSEquipmentComponent.VendorWarrantyType : Edm.String "Vendor Warranty Type"
PX.Objects.FS.FSEquipmentComponent.SalesDate : Edm.DateTimeOffset "Sales Date"
PX.Objects.FS.FSEquipmentComponent.InstSrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSEquipmentComponent.InstServiceOrderRefNbr : Edm.String "Installation Service Order Nbr."
PX.Objects.FS.FSEquipmentComponent.InstAppointmentRefNbr : Edm.String "Installation Appointment Nbr."
PX.Objects.FS.FSEquipmentComponent.InvoiceRefNbr : Edm.String "Invoice Reference Nbr."
PX.Objects.FS.FSEquipmentComponent.SalesOrderType : Edm.String "Sales Order Type"
PX.Objects.FS.FSEquipmentComponent.SalesOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.FS.FSEquipmentComponent.Status : Edm.String "Status"
PX.Objects.FS.FSEquipmentComponent.Comment : Edm.String "Equipment Action Comment"
PX.Objects.FS.FSEquipmentComponent.ComponentReplaced : Edm.Int32 "Component Replaced"
PX.Objects.FS.FSEquipmentComponent.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSEquipmentComponent.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSEquipmentComponent.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSEquipmentComponent.CreatedByScreenID : Edm.String
PX.Objects.FS.FSEquipmentComponent.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSEquipmentComponent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSEquipmentComponent.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSEquipmentComponent.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSEquipmentComponent.tstamp : Edm.Binary
PX.Objects.FS.FSEquipmentComponent.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.FS.FSEquipmentComponent.ARInvoiceByInvoiceRefNbr -> PX.Objects.AR.ARInvoice (InvoiceRefNbr=RefNbr)
PX.Objects.FS.FSEquipmentComponent.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSEquipmentComponent.InventoryItemByItemClassID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID, ItemClassID=ItemClassID)
PX.Objects.FS.FSEquipmentComponent.FSEquipmentBySMequipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSEquipmentComponent.FSAppointmentByInstAppointmentRefNbr -> PX.Objects.FS.FSAppointment (InstSrvOrdType=SrvOrdType, InstAppointmentRefNbr=RefNbr)
PX.Objects.FS.FSEquipmentComponent.FSAppointmentByInstSrvOrdType -> PX.Objects.FS.FSAppointment (InstAppointmentRefNbr=RefNbr, InstSrvOrdType=SrvOrdType)
PX.Objects.FS.FSEquipmentComponent.SOOrderBySalesOrderType -> PX.Objects.SO.SOOrder (SalesOrderNbr=OrderNbr, SalesOrderType=OrderType)
PX.Objects.FS.FSEquipmentComponent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSEquipmentComponent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSEquipmentComponent.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.FS.FSEquipmentComponent.FSEquipmentComponentByLineNbr -> PX.Objects.FS.FSEquipmentComponent (LineNbr=ComponentReplaced)
PX.Objects.FS.FSEquipmentComponent.FSModelTemplateComponentByComponentID -> PX.Objects.FS.FSModelTemplateComponent (ComponentID=ComponentID)
PX.Objects.FS.FSEquipmentComponent.FSServiceOrderByInstServiceOrderRefNbr -> PX.Objects.FS.FSServiceOrder (InstSrvOrdType=SrvOrdType, InstServiceOrderRefNbr=RefNbr)
PX.Objects.FS.FSEquipmentComponent.FSServiceOrderByInstSrvOrdType -> PX.Objects.FS.FSServiceOrder (InstServiceOrderRefNbr=RefNbr, InstSrvOrdType=SrvOrdType)
PX.Objects.FS.FSEquipmentComponent.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSEquipmentComponent.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.FSEquipmentComponent.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.FS.FSEquipmentComponent.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.FSEquipmentComponent.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)

# PX.Objects.FS.FSEquipmentType (EntityType)

Label: "Equipment Type"
Key: EquipmentTypeCD
Entity sets: PX_Objects_FS_FSEquipmentType, EquipmentType, FSEquipmentType
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSEquipmentType.EquipmentTypeID : Edm.Int32 "EquipmentTypeID"
PX.Objects.FS.FSEquipmentType.EquipmentTypeCD : Edm.String [key] "Equipment Type"
PX.Objects.FS.FSEquipmentType.Descr : Edm.String "Description"
PX.Objects.FS.FSEquipmentType.RequireBranchLocation : Edm.Boolean [required] "Require Branch Location"
PX.Objects.FS.FSEquipmentType.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSEquipmentType.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSEquipmentType.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSEquipmentType.CreatedByScreenID : Edm.String
PX.Objects.FS.FSEquipmentType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSEquipmentType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSEquipmentType.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSEquipmentType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSEquipmentType.tstamp : Edm.Binary
PX.Objects.FS.FSEquipmentType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSEquipmentType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSEquipmentType.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.FSEquipmentType.FSManufacturerModelCollection -> Collection(PX.Objects.FS.FSManufacturerModel)
PX.Objects.FS.FSEquipmentType.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.Objects.FS.FSEquipmentType.SoldInventoryItemCollection -> Collection(PX.Objects.FS.SoldInventoryItem)

# PX.Objects.FS.FSGenerationLogError (EntityType)

Label: "Generation Log Error"
Key: LogID
Entity sets: PX_Objects_FS_FSGenerationLogError, GenerationLogError, FSGenerationLogError

PX.Objects.FS.FSGenerationLogError.LogID : Edm.Int32 [key]
PX.Objects.FS.FSGenerationLogError.GenerationID : Edm.Int32 "Generation ID"
PX.Objects.FS.FSGenerationLogError.ScheduleID : Edm.Int32 "Schedule ID"
PX.Objects.FS.FSGenerationLogError.ErrorMessage : Edm.String "Error Message"
PX.Objects.FS.FSGenerationLogError.ErrorDate : Edm.DateTimeOffset "Generation Date"
PX.Objects.FS.FSGenerationLogError.ProcessType : Edm.String
PX.Objects.FS.FSGenerationLogError.Ignore : Edm.Boolean [required] "Ignore"
PX.Objects.FS.FSGenerationLogError.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSGenerationLogError.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSGenerationLogError.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSGenerationLogError.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSGenerationLogError.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSGenerationLogError.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSGenerationLogError.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSGenerationLogError.ErrorDateUTC : Edm.DateTimeOffset "Generation Date"
PX.Objects.FS.FSGenerationLogError.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule (ScheduleID=ScheduleID)
PX.Objects.FS.FSGenerationLogError.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSGenerationLogError.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSGeoZone (EntityType)

Label: "Service Area"
Key: GeoZoneCD
Entity sets: PX_Objects_FS_FSGeoZone, ServiceArea, FSGeoZone
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSGeoZone.GeoZoneID : Edm.Int32 "Service Area"
PX.Objects.FS.FSGeoZone.GeoZoneCD : Edm.String [key] "Service Area ID"
PX.Objects.FS.FSGeoZone.CountryID : Edm.String "Country"
PX.Objects.FS.FSGeoZone.Descr : Edm.String "Description"
PX.Objects.FS.FSGeoZone.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSGeoZone.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSGeoZone.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSGeoZone.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSGeoZone.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSGeoZone.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSGeoZone.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSGeoZone.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSGeoZone.tstamp : Edm.Binary
PX.Objects.FS.FSGeoZone.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSGeoZone.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSGeoZone.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.FS.FSGeoZone.FSGeoZonePostalCodeCollection -> Collection(PX.Objects.SV.FSGeoZonePostalCode)
PX.Objects.FS.FSGeoZone.FSGeoZoneEmpCollection -> Collection(PX.Objects.FS.FSGeoZoneEmp)
PX.Objects.FS.FSGeoZone.SVServiceLocationCollection -> Collection(PX.Objects.SV.SVServiceLocation)
PX.Objects.FS.FSGeoZone.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.FS.FSGeoZone.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)

# PX.Objects.FS.FSGeoZoneEmp (EntityType)

Label: "Service Area - Employee"
Key: EmployeeID, GeoZoneID
Entity sets: PX_Objects_FS_FSGeoZoneEmp, ServiceAreaEmployee, FSGeoZoneEmp
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSGeoZoneEmp.GeoZoneID : Edm.Int32 [key] "Service Area ID"
PX.Objects.FS.FSGeoZoneEmp.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.FS.FSGeoZoneEmp.NoteID : Edm.Guid
PX.Objects.FS.FSGeoZoneEmp.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSGeoZoneEmp.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSGeoZoneEmp.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSGeoZoneEmp.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSGeoZoneEmp.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSGeoZoneEmp.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSGeoZoneEmp.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSGeoZoneEmp.tstamp : Edm.Binary
PX.Objects.FS.FSGeoZoneEmp.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.FS.FSGeoZoneEmp.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.FS.FSGeoZoneEmp.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.FS.FSGeoZoneEmp.FSGeoZoneByGeoZoneID -> PX.Objects.SV.FSGeoZone (GeoZoneID=GeoZoneID)
PX.Objects.FS.FSGeoZoneEmp.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSGeoZoneEmp.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSGeoZonePostalCode (EntityType)

Label: "Service Area - Postal Code"
Key: GeoZoneID, PostalCode
Entity sets: PX_Objects_FS_FSGeoZonePostalCode, ServiceAreaPostalCode, FSGeoZonePostalCode

PX.Objects.FS.FSGeoZonePostalCode.GeoZoneID : Edm.Int32 [key] "Service Area"
PX.Objects.FS.FSGeoZonePostalCode.CountryID : Edm.String "Country"
PX.Objects.FS.FSGeoZonePostalCode.PostalCode : Edm.String [key] "Postal Code"
PX.Objects.FS.FSGeoZonePostalCode.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSGeoZonePostalCode.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSGeoZonePostalCode.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSGeoZonePostalCode.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSGeoZonePostalCode.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSGeoZonePostalCode.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSGeoZonePostalCode.tstamp : Edm.Binary
PX.Objects.FS.FSGeoZonePostalCode.FSGeoZoneByGeoZoneID -> PX.Objects.SV.FSGeoZone (GeoZoneID=GeoZoneID)
PX.Objects.FS.FSGeoZonePostalCode.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSGeoZonePostalCode.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSGeoZonePostalCode.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)

# PX.Objects.FS.FSGPSTrackingLocation (EntityType)

BaseType: PX.FS.FSGPSTrackingRequest
Key: RequestID (inherited from PX.FS.FSGPSTrackingRequest)
Entity sets: PX_Objects_FS_FSGPSTrackingLocation
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FS.FSGPSTrackingLocation.WeekDay : Edm.Int32 "Day of Week"

# PX.Objects.FS.FSLicense (EntityType)

Label: "License"
Key: RefNbr
Entity sets: PX_Objects_FS_FSLicense, License, FSLicense
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSLicense.LicenseID : Edm.Int32 "License ID"
PX.Objects.FS.FSLicense.RefNbr : Edm.String [key] "License Nbr."
PX.Objects.FS.FSLicense.Descr : Edm.String "Description"
PX.Objects.FS.FSLicense.EmployeeID : Edm.Int32 "Staff Member"
PX.Objects.FS.FSLicense.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.FS.FSLicense.IssueDate : Edm.DateTimeOffset "Issue Date"
PX.Objects.FS.FSLicense.LicenseTypeID : Edm.Int32 "License Type"
PX.Objects.FS.FSLicense.NeverExpires : Edm.Boolean [required] "Never Expires"
PX.Objects.FS.FSLicense.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSLicense.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSLicense.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSLicense.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSLicense.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSLicense.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSLicense.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSLicense.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSLicense.tstamp : Edm.Binary
PX.Objects.FS.FSLicense.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.FS.FSLicense.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.FS.FSLicense.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.FS.FSLicense.FSLicenseTypeByLicenseTypeID -> PX.Objects.SV.FSLicenseType (LicenseTypeID=LicenseTypeID)
PX.Objects.FS.FSLicense.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSLicense.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSLicenseType (EntityType)

Label: "License Type"
Key: LicenseTypeCD
Entity sets: PX_Objects_FS_FSLicenseType, LicenseType, FSLicenseType
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.FS.FSLicenseType.LicenseTypeID : Edm.Int32 "LicenseTypeID"
PX.Objects.FS.FSLicenseType.LicenseTypeCD : Edm.String [key] "License Type ID"
PX.Objects.FS.FSLicenseType.Descr : Edm.String "Description"
PX.Objects.FS.FSLicenseType.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSLicenseType.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSLicenseType.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSLicenseType.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSLicenseType.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSLicenseType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSLicenseType.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSLicenseType.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSLicenseType.tstamp : Edm.Binary
PX.Objects.FS.FSLicenseType.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.FS.FSLicenseType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSLicenseType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSLicenseType.FSLicenseCollection -> Collection(PX.Objects.SV.FSLicense)
PX.Objects.FS.FSLicenseType.SVVendorLicenseCollection -> Collection(PX.Objects.SV.SVVendorLicense)
PX.Objects.FS.FSLicenseType.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)

# PX.Objects.FS.FSLog (EntityType)

Label: "Log"
Key: LogID
Entity sets: PX_Objects_FS_FSLog, Log1, FSLog
Non-filterable, non-selectable: BillableTimeDurationInt, NoteText, SkipCostCodeValidation, TimeDurationReport

PX.Objects.FS.FSLog.LogID : Edm.Int32 [key]
PX.Objects.FS.FSLog.DocType : Edm.String
PX.Objects.FS.FSLog.DocRefNbr : Edm.String
PX.Objects.FS.FSLog.DocID : Edm.Int32 "DocID"
PX.Objects.FS.FSLog.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.FS.FSLog.ItemType : Edm.String "Log Type"
PX.Objects.FS.FSLog.Status : Edm.String "Log Line Status"
PX.Objects.FS.FSLog.DateTimeBegin : Edm.DateTimeOffset "Start Time"
PX.Objects.FS.FSLog.DateTimeEnd : Edm.DateTimeOffset "End Time"
PX.Objects.FS.FSLog.TimeDuration : Edm.Int32 "Duration"
PX.Objects.FS.FSLog.ApprovedTime : Edm.Boolean [required] "Approved"
PX.Objects.FS.FSLog.CuryExtCost : Edm.Decimal [required] "CuryExtCost"
PX.Objects.FS.FSLog.CuryInfoID : Edm.Int64
PX.Objects.FS.FSLog.CuryUnitCost : Edm.Decimal "CuryUnitCost"
PX.Objects.FS.FSLog.Descr : Edm.String "Description"
PX.Objects.FS.FSLog.DetLineRef : Edm.String "Detail Ref. Nbr."
PX.Objects.FS.FSLog.EarningType : Edm.String "Earning Type"
PX.Objects.FS.FSLog.BAccountID : Edm.Int32 "Staff Member"
PX.Objects.FS.FSLog.BAccountType : Edm.String "Staff Type"
PX.Objects.FS.FSLog.ExtCost : Edm.Decimal [required]
PX.Objects.FS.FSLog.KeepDateTimes : Edm.Boolean [required] "Manage Time Manually"
PX.Objects.FS.FSLog.LaborItemID : Edm.Int32 "Labor Item ID"
PX.Objects.FS.FSLog.LineRef : Edm.String "Log Ref. Nbr."
PX.Objects.FS.FSLog.TrackTime : Edm.Boolean [required] "Track Time"
PX.Objects.FS.FSLog.TrackOnService : Edm.Boolean "Add to Actual Duration"
PX.Objects.FS.FSLog.TimeCardCD : Edm.String "Time Card Ref. Nbr."
PX.Objects.FS.FSLog.UnitCost : Edm.Decimal
PX.Objects.FS.FSLog.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.FS.FSLog.IsBillable : Edm.Boolean [required] "Billable"
PX.Objects.FS.FSLog.BillableTimeDuration : Edm.Int32 [required] "Billable Time"
PX.Objects.FS.FSLog.BillableTimeDurationInt : Edm.Int32
PX.Objects.FS.FSLog.BillableQty : Edm.Decimal [required] "Billable Quantity"
PX.Objects.FS.FSLog.CuryBillableTranAmount : Edm.Decimal [required] "Billable Amount"
PX.Objects.FS.FSLog.BillableTranAmount : Edm.Decimal [required] "Base Billable Amount"
PX.Objects.FS.FSLog.TimeActivityStatus : Edm.String
PX.Objects.FS.FSLog.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSLog.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSLog.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSLog.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSLog.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSLog.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSLog.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSLog.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSLog.tstamp : Edm.Binary
PX.Objects.FS.FSLog.SkipCostCodeValidation : Edm.Boolean
PX.Objects.FS.FSLog.TimeDurationReport : Edm.Int32
PX.Objects.FS.FSLog.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.FS.FSLog.VendorByBAccountID -> PX.Objects.AP.Vendor (BAccountID=BAccountID)
PX.Objects.FS.FSLog.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSLog.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSLog.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.FS.FSLog.InventoryItemByLaborItemID -> PX.Objects.IN.InventoryItem (LaborItemID=InventoryID)
PX.Objects.FS.FSLog.FSAppointmentByDocRefNbr -> PX.Objects.FS.FSAppointment (DocType=SrvOrdType, DocRefNbr=RefNbr)
PX.Objects.FS.FSLog.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSLog.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSLog.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSLog.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.FS.FSLog.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.FS.FSLog.EPEarningTypeByEarningType -> PX.Objects.EP.EPEarningType (EarningType=TypeCD)
PX.Objects.FS.FSLog.EPTimeCardByTimeCardCD -> PX.Objects.EP.EPTimeCard (TimeCardCD=TimeCardCD)
PX.Objects.FS.FSLog.FSAppointmentDetByDetLineRef -> PX.Objects.FS.FSAppointmentDet (DetLineRef=LineRef)
PX.Objects.FS.FSLog.FSSrvOrdTypeByDocType -> PX.Objects.FS.FSSrvOrdType (DocType=SrvOrdType)

# PX.Objects.FS.FSManufacturer (EntityType)

Label: "Manufacturer"
Key: ManufacturerCD
Entity sets: PX_Objects_FS_FSManufacturer, Manufacturer, FSManufacturer
Non-filterable, non-selectable: LocationID, NoteText, ManufacturerGICD, DeletedDatabaseRecord

PX.Objects.FS.FSManufacturer.ManufacturerID : Edm.Int32 "ManufacturerID"
PX.Objects.FS.FSManufacturer.ManufacturerCD : Edm.String [key] "Manufacturer ID"
PX.Objects.FS.FSManufacturer.ManufacturerAddressID : Edm.Int32
PX.Objects.FS.FSManufacturer.ManufacturerContactID : Edm.Int32
PX.Objects.FS.FSManufacturer.AllowOverrideContactAddress : Edm.Boolean "Override"
PX.Objects.FS.FSManufacturer.LocationID : Edm.Int32
PX.Objects.FS.FSManufacturer.ContactID : Edm.Int32 "Contact"
PX.Objects.FS.FSManufacturer.Descr : Edm.String "Description"
PX.Objects.FS.FSManufacturer.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSManufacturer.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSManufacturer.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSManufacturer.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSManufacturer.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSManufacturer.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSManufacturer.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSManufacturer.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSManufacturer.tstamp : Edm.Binary
PX.Objects.FS.FSManufacturer.ManufacturerGICD : Edm.String "Manufacturer"
PX.Objects.FS.FSManufacturer.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.FS.FSManufacturer.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.FS.FSManufacturer.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSManufacturer.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSManufacturer.FSAddressByManufacturerAddressID -> PX.Objects.FS.FSAddress (ManufacturerAddressID=AddressID)
PX.Objects.FS.FSManufacturer.FSContactByManufacturerContactID -> PX.Objects.FS.FSContact (ManufacturerContactID=ContactID)
PX.Objects.FS.FSManufacturer.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.FSManufacturer.FSManufacturerModelCollection -> Collection(PX.Objects.FS.FSManufacturerModel)

# PX.Objects.FS.FSManufacturerModel (EntityType)

Label: "Manufacturer Model"
Key: ManufacturerID, ManufacturerModelCD
Entity sets: PX_Objects_FS_FSManufacturerModel, ManufacturerModel, FSManufacturerModel
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.FS.FSManufacturerModel.ManufacturerID : Edm.Int32 [key] "Manufacturer ID"
PX.Objects.FS.FSManufacturerModel.ManufacturerModelID : Edm.Int32 "ManufacturerModelID"
PX.Objects.FS.FSManufacturerModel.ManufacturerModelCD : Edm.String [key] "Manufacturer Model"
PX.Objects.FS.FSManufacturerModel.Descr : Edm.String "Description"
PX.Objects.FS.FSManufacturerModel.EquipmentTypeID : Edm.Int32 "Equipment Type"
PX.Objects.FS.FSManufacturerModel.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSManufacturerModel.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSManufacturerModel.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSManufacturerModel.CreatedByScreenID : Edm.String
PX.Objects.FS.FSManufacturerModel.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSManufacturerModel.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSManufacturerModel.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSManufacturerModel.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSManufacturerModel.tstamp : Edm.Binary
PX.Objects.FS.FSManufacturerModel.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.FS.FSManufacturerModel.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSManufacturerModel.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSManufacturerModel.FSEquipmentTypeByEquipmentTypeID -> PX.Objects.FS.FSEquipmentType (EquipmentTypeID=EquipmentTypeCD)
PX.Objects.FS.FSManufacturerModel.FSManufacturerByManufacturerID -> PX.Objects.FS.FSManufacturer (ManufacturerID=ManufacturerID)
PX.Objects.FS.FSManufacturerModel.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)

# PX.Objects.FS.FSMasterContract (EntityType)

Key: MasterContractCD
Entity sets: PX_Objects_FS_FSMasterContract
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSMasterContract.MasterContractID : Edm.Int32 "MasterContractID"
PX.Objects.FS.FSMasterContract.MasterContractCD : Edm.String [key] "Master Contract ID"
PX.Objects.FS.FSMasterContract.Descr : Edm.String "Description"
PX.Objects.FS.FSMasterContract.CustomerID : Edm.Int32 "Customer"
PX.Objects.FS.FSMasterContract.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSMasterContract.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSMasterContract.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSMasterContract.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSMasterContract.CreatedByScreenID : Edm.String
PX.Objects.FS.FSMasterContract.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSMasterContract.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSMasterContract.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSMasterContract.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSMasterContract.tstamp : Edm.Binary
PX.Objects.FS.FSMasterContract.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSMasterContract.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSMasterContract.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSMasterContract.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSMasterContract.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)

# PX.Objects.FS.FSModelComponent (EntityType)

Label: "Model Warranty"
Key: ComponentID, ModelID
Entity sets: PX_Objects_FS_FSModelComponent, ModelWarranty, FSModelComponent
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSModelComponent.ModelID : Edm.Int32 [key]
PX.Objects.FS.FSModelComponent.ComponentID : Edm.Int32 [key] "Component ID"
PX.Objects.FS.FSModelComponent.Active : Edm.Boolean [required] "Active"
PX.Objects.FS.FSModelComponent.Descr : Edm.String "Description"
PX.Objects.FS.FSModelComponent.RequireSerial : Edm.Boolean [required] "Requires Serial"
PX.Objects.FS.FSModelComponent.VendorWarrantyValue : Edm.Int32 "Vendor Warranty"
PX.Objects.FS.FSModelComponent.VendorWarrantyType : Edm.String "Vendor Warranty Type"
PX.Objects.FS.FSModelComponent.VendorID : Edm.Int32 "Vendor ID"
PX.Objects.FS.FSModelComponent.CpnyWarrantyValue : Edm.Int32 "Company Warranty"
PX.Objects.FS.FSModelComponent.CpnyWarrantyType : Edm.String "Company Warranty Type"
PX.Objects.FS.FSModelComponent.ClassID : Edm.Int32 "Item Class ID"
PX.Objects.FS.FSModelComponent.Qty : Edm.Int32 "Quantity"
PX.Objects.FS.FSModelComponent.Optional : Edm.Boolean [required] "Optional"
PX.Objects.FS.FSModelComponent.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSModelComponent.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSModelComponent.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSModelComponent.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSModelComponent.CreatedByScreenID : Edm.String
PX.Objects.FS.FSModelComponent.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSModelComponent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSModelComponent.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSModelComponent.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSModelComponent.tstamp : Edm.Binary
PX.Objects.FS.FSModelComponent.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.FS.FSModelComponent.InventoryItemByModelID -> PX.Objects.IN.InventoryItem (ModelID=InventoryID)
PX.Objects.FS.FSModelComponent.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSModelComponent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSModelComponent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSModelComponent.INItemClassByClassID -> PX.Objects.IN.INItemClass (ClassID=ItemClassID)
PX.Objects.FS.FSModelComponent.FSModelTemplateComponentByComponentID -> PX.Objects.FS.FSModelTemplateComponent (ComponentID=ComponentID)

# PX.Objects.FS.FSModelTemplateComponent (EntityType)

Label: "Model Template Component"
Key: ComponentCD, ModelTemplateID
Entity sets: PX_Objects_FS_FSModelTemplateComponent, ModelTemplateComponent, FSModelTemplateComponent
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSModelTemplateComponent.ModelTemplateID : Edm.Int32 [key]
PX.Objects.FS.FSModelTemplateComponent.Active : Edm.Boolean [required] "Active"
PX.Objects.FS.FSModelTemplateComponent.ComponentID : Edm.Int32
PX.Objects.FS.FSModelTemplateComponent.ComponentCD : Edm.String [key] "Component ID"
PX.Objects.FS.FSModelTemplateComponent.Descr : Edm.String "Description"
PX.Objects.FS.FSModelTemplateComponent.ClassID : Edm.Int32 "Item Class ID"
PX.Objects.FS.FSModelTemplateComponent.Qty : Edm.Int32 [required] "Quantity"
PX.Objects.FS.FSModelTemplateComponent.Optional : Edm.Boolean [required] "Optional"
PX.Objects.FS.FSModelTemplateComponent.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSModelTemplateComponent.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSModelTemplateComponent.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSModelTemplateComponent.CreatedByScreenID : Edm.String
PX.Objects.FS.FSModelTemplateComponent.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSModelTemplateComponent.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSModelTemplateComponent.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSModelTemplateComponent.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSModelTemplateComponent.tstamp : Edm.Binary
PX.Objects.FS.FSModelTemplateComponent.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSModelTemplateComponent.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSModelTemplateComponent.INItemClassByModelTemplateID -> PX.Objects.IN.INItemClass (ModelTemplateID=ItemClassID)
PX.Objects.FS.FSModelTemplateComponent.INItemClassByClassID -> PX.Objects.IN.INItemClass (ClassID=ItemClassID)
PX.Objects.FS.FSModelTemplateComponent.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSModelTemplateComponent.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.FSModelTemplateComponent.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.FSModelTemplateComponent.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.FS.FSModelTemplateComponent.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)

# PX.Objects.FS.FSPostBatch (EntityType)

Label: "Field Service Billing Batch"
Key: BatchNbr
Entity sets: PX_Objects_FS_FSPostBatch, FieldServiceBillingBatch, FSPostBatch

PX.Objects.FS.FSPostBatch.BatchID : Edm.Int32 "Batch ID"
PX.Objects.FS.FSPostBatch.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.FS.FSPostBatch.Status : Edm.String "Status"
PX.Objects.FS.FSPostBatch.PostTo : Edm.String "Generated In"
PX.Objects.FS.FSPostBatch.QtyDoc : Edm.Int32 "Documents Processed"
PX.Objects.FS.FSPostBatch.FinPeriodID : Edm.String "Billing Period"
PX.Objects.FS.FSPostBatch.InvoiceDate : Edm.DateTimeOffset "Billing Date"
PX.Objects.FS.FSPostBatch.BillingCycleID : Edm.Int32 "Billing Cycle"
PX.Objects.FS.FSPostBatch.UpToDate : Edm.DateTimeOffset "Up to Date"
PX.Objects.FS.FSPostBatch.CutOffDate : Edm.DateTimeOffset "Billing Cycle Cut-Off Date"
PX.Objects.FS.FSPostBatch.CreatedByID : Edm.Guid "Created On"
PX.Objects.FS.FSPostBatch.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSPostBatch.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSPostBatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSPostBatch.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSPostBatch.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSPostBatch.tstamp : Edm.Binary
PX.Objects.FS.FSPostBatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSPostBatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSPostBatch.FSBillingCycleByBillingCycleID -> PX.Objects.FS.FSBillingCycle (BillingCycleID=BillingCycleID)
PX.Objects.FS.FSPostBatch.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.FS.FSPostBatch.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)

# PX.Objects.FS.FSPostDet (EntityType)

Key: BatchID, PostDetID
Entity sets: PX_Objects_FS_FSPostDet
Non-filterable, non-selectable: PostDocType, PostDocReferenceNbr, INPostDocReferenceNbr, InvoiceRefNbr, InvoiceDocType, InvoiceReferenceNbr, BatchNbr

PX.Objects.FS.FSPostDet.BatchID : Edm.Int32 [key] "Batch ID"
PX.Objects.FS.FSPostDet.PostDetID : Edm.Int32 [key] "PostDetID"
PX.Objects.FS.FSPostDet.PostID : Edm.Int32 "PostID"
PX.Objects.FS.FSPostDet.SOPosted : Edm.Boolean "Invoiced through Sales Order"
PX.Objects.FS.FSPostDet.SOOrderType : Edm.String "Sales Order Type"
PX.Objects.FS.FSPostDet.SOOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.FS.FSPostDet.SOLineNbr : Edm.Int32 "Sales Order Line Nbr."
PX.Objects.FS.FSPostDet.ARPosted : Edm.Boolean "Invoiced through AR"
PX.Objects.FS.FSPostDet.ARDocType : Edm.String "AR Document Type"
PX.Objects.FS.FSPostDet.ARRefNbr : Edm.String "AR Reference Nbr."
PX.Objects.FS.FSPostDet.ARLineNbr : Edm.Int32 "AR Line Nbr."
PX.Objects.FS.FSPostDet.APPosted : Edm.Boolean "Invoiced through AP"
PX.Objects.FS.FSPostDet.APDocType : Edm.String "AP Document Type"
PX.Objects.FS.FSPostDet.APRefNbr : Edm.String "AP Reference Nbr."
PX.Objects.FS.FSPostDet.APLineNbr : Edm.Int32 "AP Line Nbr."
PX.Objects.FS.FSPostDet.INPosted : Edm.Boolean "Invoiced through IN"
PX.Objects.FS.FSPostDet.INDocType : Edm.String "IN Document Type"
PX.Objects.FS.FSPostDet.INRefNbr : Edm.String "IN Reference Nbr."
PX.Objects.FS.FSPostDet.INLineNbr : Edm.Int32 "IN Line Nbr."
PX.Objects.FS.FSPostDet.SOInvPosted : Edm.Boolean "Invoiced through SO Invoice"
PX.Objects.FS.FSPostDet.SOInvDocType : Edm.String "SO Invoice Document Type"
PX.Objects.FS.FSPostDet.SOInvRefNbr : Edm.String "SO Invoice Ref. Nbr."
PX.Objects.FS.FSPostDet.SOInvLineNbr : Edm.Int32 "SO Invoice Line Nbr."
PX.Objects.FS.FSPostDet.PMPosted : Edm.Boolean "Invoiced through PM"
PX.Objects.FS.FSPostDet.PMDocType : Edm.String "PM Document Type"
PX.Objects.FS.FSPostDet.PMRefNbr : Edm.String "PM Reference Nbr."
PX.Objects.FS.FSPostDet.PMTranID : Edm.Int64 "PM Tran ID"
PX.Objects.FS.FSPostDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSPostDet.CreatedByScreenID : Edm.String
PX.Objects.FS.FSPostDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSPostDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSPostDet.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSPostDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSPostDet.tstamp : Edm.Binary
PX.Objects.FS.FSPostDet.PostDocType : Edm.String "Document Type"
PX.Objects.FS.FSPostDet.PostDocReferenceNbr : Edm.String "Reference Nbr."
PX.Objects.FS.FSPostDet.INPostDocReferenceNbr : Edm.String "Issue Reference Nbr."
PX.Objects.FS.FSPostDet.InvoiceRefNbr : Edm.String "InvoiceRefNbr"
PX.Objects.FS.FSPostDet.InvoiceDocType : Edm.String "InvoiceDocType"
PX.Objects.FS.FSPostDet.InvoiceReferenceNbr : Edm.String "Invoice Nbr."
PX.Objects.FS.FSPostDet.BatchNbr : Edm.String "Batch Number"
PX.Objects.FS.FSPostDet.APInvoiceByApRefNbr -> PX.Objects.AP.APInvoice
PX.Objects.FS.FSPostDet.ARInvoiceByArRefNbr -> PX.Objects.AR.ARInvoice
PX.Objects.FS.FSPostDet.INTranByINLineNbr -> PX.Objects.IN.INTran (INDocType=DocType, INRefNbr=RefNbr, INLineNbr=LineNbr)
PX.Objects.FS.FSPostDet.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.FS.FSPostDet.PMTranByPMTranID -> PX.Objects.PM.PMTran (PMTranID=TranID)
PX.Objects.FS.FSPostDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSPostDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSPostDet.SOLineBySOLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOLineNbr=LineNbr)
PX.Objects.FS.FSPostDet.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.FS.FSPostDet.INRegisterByINRefNbr -> PX.Objects.IN.INRegister (INDocType=DocType, INRefNbr=RefNbr)
PX.Objects.FS.FSPostDet.ARTranByARLineNbr -> PX.Objects.AR.ARTran (ARLineNbr=LineNbr)
PX.Objects.FS.FSPostDet.ARTranBySOInvLineNbr -> PX.Objects.AR.ARTran (SOInvDocType=TranType, SOInvRefNbr=RefNbr, SOInvLineNbr=LineNbr)
PX.Objects.FS.FSPostDet.APTranByAPLineNbr -> PX.Objects.AP.APTran (APLineNbr=LineNbr)
PX.Objects.FS.FSPostDet.FSPostBatchByBatchID -> PX.Objects.FS.FSPostBatch (BatchID=BatchNbr)
PX.Objects.FS.FSPostDet.SOInvoiceBySOInvRefNbr -> PX.Objects.SO.SOInvoice (SOInvDocType=DocType, SOInvRefNbr=RefNbr)

# PX.Objects.FS.FSPostDoc (EntityType)

Key: RecordID
Entity sets: PX_Objects_FS_FSPostDoc
Non-filterable, non-selectable: InvtMult

PX.Objects.FS.FSPostDoc.ProcessID : Edm.Guid
PX.Objects.FS.FSPostDoc.RecordID : Edm.Int32 [key]
PX.Objects.FS.FSPostDoc.BillingCycleID : Edm.Int32
PX.Objects.FS.FSPostDoc.GroupKey : Edm.String
PX.Objects.FS.FSPostDoc.AppointmentID : Edm.Int32 "Appointment Nbr."
PX.Objects.FS.FSPostDoc.SOID : Edm.Int32 "Service Order Nbr."
PX.Objects.FS.FSPostDoc.RowIndex : Edm.Int32
PX.Objects.FS.FSPostDoc.PostNegBalanceToAP : Edm.Boolean
PX.Objects.FS.FSPostDoc.PostOrderType : Edm.String
PX.Objects.FS.FSPostDoc.PostOrderTypeNegativeBalance : Edm.String
PX.Objects.FS.FSPostDoc.InvtMult : Edm.Int16
PX.Objects.FS.FSPostDoc.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSPostDoc.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSPostDoc.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSPostDoc.tstamp : Edm.Binary
PX.Objects.FS.FSPostDoc.BatchID : Edm.Int32
PX.Objects.FS.FSPostDoc.EntityType : Edm.String
PX.Objects.FS.FSPostDoc.PostedTO : Edm.String "Posted to"
PX.Objects.FS.FSPostDoc.PostDocType : Edm.String "Document Type"
PX.Objects.FS.FSPostDoc.PostRefNbr : Edm.String "Document Nbr."
PX.Objects.FS.FSPostDoc.FSAppointmentByAppointmentID -> PX.Objects.FS.FSAppointment (AppointmentID=AppointmentID)
PX.Objects.FS.FSPostDoc.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSPostDoc.FSServiceOrderBySOID -> PX.Objects.FS.FSServiceOrder (SOID=SOID)

# PX.Objects.FS.FSPostInfo (EntityType)

Label: "FSPostInfo"
Key: PostID
Entity sets: PX_Objects_FS_FSPostInfo, FSPostInfo
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.FS.FSPostInfo.PostID : Edm.Int32 [key] "PostID"
PX.Objects.FS.FSPostInfo.AppointmentID : Edm.Int32
PX.Objects.FS.FSPostInfo.SOID : Edm.Int32
PX.Objects.FS.FSPostInfo.SOPosted : Edm.Boolean [required] "Invoiced through Sales Order"
PX.Objects.FS.FSPostInfo.SOOrderType : Edm.String "Sales Order Type"
PX.Objects.FS.FSPostInfo.SOOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.FS.FSPostInfo.SOLineNbr : Edm.Int32 "Sales Order Line Nbr."
PX.Objects.FS.FSPostInfo.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSPostInfo.CreatedByScreenID : Edm.String
PX.Objects.FS.FSPostInfo.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSPostInfo.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSPostInfo.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSPostInfo.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSPostInfo.tstamp : Edm.Binary
PX.Objects.FS.FSPostInfo.ARPosted : Edm.Boolean "Invoiced through AR"
PX.Objects.FS.FSPostInfo.ARDocType : Edm.String "AR Document Type"
PX.Objects.FS.FSPostInfo.ARRefNbr : Edm.String "AR Ref. Nbr."
PX.Objects.FS.FSPostInfo.ARLineNbr : Edm.Int32 "AR Line Nbr."
PX.Objects.FS.FSPostInfo.APPosted : Edm.Boolean "Invoiced through AP"
PX.Objects.FS.FSPostInfo.APDocType : Edm.String "AP Document Type"
PX.Objects.FS.FSPostInfo.APRefNbr : Edm.String "AP Reference Nbr."
PX.Objects.FS.FSPostInfo.APLineNbr : Edm.Int32 "AP Line Nbr."
PX.Objects.FS.FSPostInfo.INPosted : Edm.Boolean "Invoiced through IN"
PX.Objects.FS.FSPostInfo.INDocType : Edm.String "IN Document Type"
PX.Objects.FS.FSPostInfo.INRefNbr : Edm.String "IN Reference Nbr."
PX.Objects.FS.FSPostInfo.INLineNbr : Edm.Int32 "IN Line Nbr."
PX.Objects.FS.FSPostInfo.SOInvPosted : Edm.Boolean "Invoiced through SO Invoice"
PX.Objects.FS.FSPostInfo.SOInvDocType : Edm.String "SO Invoice Document Type"
PX.Objects.FS.FSPostInfo.SOInvRefNbr : Edm.String "SO Invoice Ref. Nbr."
PX.Objects.FS.FSPostInfo.SOInvLineNbr : Edm.Int32 "SO Invoice Line Nbr."
PX.Objects.FS.FSPostInfo.PMPosted : Edm.Boolean "Invoiced through PM"
PX.Objects.FS.FSPostInfo.PMDocType : Edm.String "PM Document Type"
PX.Objects.FS.FSPostInfo.PMRefNbr : Edm.String "PM Reference Nbr."
PX.Objects.FS.FSPostInfo.PMTranID : Edm.Int64 "PM Tran ID"
PX.Objects.FS.FSPostInfo.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.FS.FSPostInfo.APInvoiceByApRefNbr -> PX.Objects.AP.APInvoice
PX.Objects.FS.FSPostInfo.ARInvoiceByArRefNbr -> PX.Objects.AR.ARInvoice
PX.Objects.FS.FSPostInfo.INTranByINLineNbr -> PX.Objects.IN.INTran (INDocType=DocType, INRefNbr=RefNbr, INLineNbr=LineNbr)
PX.Objects.FS.FSPostInfo.FSAppointmentByAppointmentID -> PX.Objects.FS.FSAppointment (AppointmentID=AppointmentID)
PX.Objects.FS.FSPostInfo.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.FS.FSPostInfo.PMTranByPMTranID -> PX.Objects.PM.PMTran (PMTranID=TranID)
PX.Objects.FS.FSPostInfo.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSPostInfo.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSPostInfo.SOLineBySOLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOLineNbr=LineNbr)
PX.Objects.FS.FSPostInfo.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.FS.FSPostInfo.INRegisterByINRefNbr -> PX.Objects.IN.INRegister (INDocType=DocType, INRefNbr=RefNbr)
PX.Objects.FS.FSPostInfo.ARTranByARLineNbr -> PX.Objects.AR.ARTran (ARLineNbr=LineNbr)
PX.Objects.FS.FSPostInfo.ARTranBySOInvLineNbr -> PX.Objects.AR.ARTran (SOInvDocType=TranType, SOInvRefNbr=RefNbr, SOInvLineNbr=LineNbr)
PX.Objects.FS.FSPostInfo.APTranByAPLineNbr -> PX.Objects.AP.APTran (APLineNbr=LineNbr)
PX.Objects.FS.FSPostInfo.FSServiceOrderBySOID -> PX.Objects.FS.FSServiceOrder (SOID=SOID)
PX.Objects.FS.FSPostInfo.SOInvoiceBySOInvRefNbr -> PX.Objects.SO.SOInvoice (SOInvDocType=DocType, SOInvRefNbr=RefNbr)
PX.Objects.FS.FSPostInfo.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSPostInfo.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)

# PX.Objects.FS.FSPostRegister (EntityType)

Key: EntityType, PostedTO, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSPostRegister

PX.Objects.FS.FSPostRegister.EntityType : Edm.String [key]
PX.Objects.FS.FSPostRegister.SrvOrdType : Edm.String [key]
PX.Objects.FS.FSPostRegister.RefNbr : Edm.String [key]
PX.Objects.FS.FSPostRegister.PostedTO : Edm.String [key]
PX.Objects.FS.FSPostRegister.Type : Edm.String
PX.Objects.FS.FSPostRegister.ProcessID : Edm.Guid
PX.Objects.FS.FSPostRegister.BatchID : Edm.Int32
PX.Objects.FS.FSPostRegister.PostDocType : Edm.String
PX.Objects.FS.FSPostRegister.PostRefNbr : Edm.String

# PX.Objects.FS.FSProblem (EntityType)

Label: "Problem"
Key: ProblemCD
Entity sets: PX_Objects_FS_FSProblem, Problem, FSProblem
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSProblem.ProblemID : Edm.Int32 "ProblemID"
PX.Objects.FS.FSProblem.ProblemCD : Edm.String [key] "Problem ID"
PX.Objects.FS.FSProblem.Descr : Edm.String "Description"
PX.Objects.FS.FSProblem.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSProblem.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSProblem.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSProblem.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSProblem.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSProblem.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSProblem.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSProblem.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSProblem.tstamp : Edm.Binary
PX.Objects.FS.FSProblem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSProblem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSProblem.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSProblem.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.FS.FSProblem.FSSrvOrdTypeProblemCollection -> Collection(PX.Objects.FS.FSSrvOrdTypeProblem)
PX.Objects.FS.FSProblem.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)

# PX.Objects.FS.FSProcessIdentity (EntityType)

Key: ProcessID
Entity sets: PX_Objects_FS_FSProcessIdentity

PX.Objects.FS.FSProcessIdentity.ProcessID : Edm.Int32 [key]
PX.Objects.FS.FSProcessIdentity.ProcessType : Edm.String
PX.Objects.FS.FSProcessIdentity.FilterFromTo : Edm.DateTimeOffset "From Date"
PX.Objects.FS.FSProcessIdentity.FilterUpTo : Edm.DateTimeOffset "To Date"
PX.Objects.FS.FSProcessIdentity.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSProcessIdentity.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSProcessIdentity.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSProcessIdentity.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSProcessIdentity.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSProcessIdentity.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSProcessIdentity.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSProcessIdentity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSProcessIdentity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSQuickProcessParameters (EntityType)

Key: SrvOrdType
Entity sets: PX_Objects_FS_FSQuickProcessParameters
Non-filterable, non-selectable: GenerateInvoice

PX.Objects.FS.FSQuickProcessParameters.SrvOrdType : Edm.String [key]
PX.Objects.FS.FSQuickProcessParameters.AllowInvoiceServiceOrder : Edm.Boolean [required] "Allow Billing"
PX.Objects.FS.FSQuickProcessParameters.CompleteServiceOrder : Edm.Boolean [required] "Complete"
PX.Objects.FS.FSQuickProcessParameters.CloseAppointment : Edm.Boolean [required] "Close"
PX.Objects.FS.FSQuickProcessParameters.CloseServiceOrder : Edm.Boolean [required] "Close"
PX.Objects.FS.FSQuickProcessParameters.EmailInvoice : Edm.Boolean [required] "Email Invoice"
PX.Objects.FS.FSQuickProcessParameters.EmailSalesOrder : Edm.Boolean [required] "Email Sales Order/Quote"
PX.Objects.FS.FSQuickProcessParameters.EmailSignedAppointment : Edm.Boolean [required] "Email Signed Appointment"
PX.Objects.FS.FSQuickProcessParameters.GenerateInvoiceFromAppointment : Edm.Boolean [required] "Run Billing"
PX.Objects.FS.FSQuickProcessParameters.GenerateInvoiceFromServiceOrder : Edm.Boolean [required] "Run Billing"
PX.Objects.FS.FSQuickProcessParameters.PayBill : Edm.Boolean [required] "Pay Bill"
PX.Objects.FS.FSQuickProcessParameters.PrepareInvoice : Edm.Boolean [required] "Prepare Invoice"
PX.Objects.FS.FSQuickProcessParameters.ReleaseBill : Edm.Boolean [required] "Release Bill"
PX.Objects.FS.FSQuickProcessParameters.ReleaseInvoice : Edm.Boolean [required] "Release Invoice"
PX.Objects.FS.FSQuickProcessParameters.SOQuickProcess : Edm.Boolean [required] "Use Sales Order Quick Processing"
PX.Objects.FS.FSQuickProcessParameters.GenerateInvoice : Edm.Boolean "Generate Invoice"
PX.Objects.FS.FSQuickProcessParameters.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSRoom (EntityType)

Label: "Room"
Key: BranchLocationID, RecordID
Entity sets: PX_Objects_FS_FSRoom, Room, FSRoom
Non-filterable, non-selectable: NoteText, CustomRoomID, FormCaptionDescription

PX.Objects.FS.FSRoom.RecordID : Edm.Int32 [key]
PX.Objects.FS.FSRoom.BranchLocationID : Edm.Int32 [key] "Branch Location ID"
PX.Objects.FS.FSRoom.RoomID : Edm.String "Room ID"
PX.Objects.FS.FSRoom.Descr : Edm.String "Description"
PX.Objects.FS.FSRoom.FloorNbr : Edm.Int32 [required] "Floor Nbr."
PX.Objects.FS.FSRoom.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSRoom.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSRoom.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSRoom.CreatedByScreenID : Edm.String
PX.Objects.FS.FSRoom.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSRoom.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSRoom.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSRoom.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSRoom.tstamp : Edm.Binary
PX.Objects.FS.FSRoom.CustomRoomID : Edm.String
PX.Objects.FS.FSRoom.FormCaptionDescription : Edm.String
PX.Objects.FS.FSRoom.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSRoom.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSRoom.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationCD)
PX.Objects.FS.FSRoom.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSRoom.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.FS.FSRoom.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.FS.FSRoom.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.FSRoom.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)

# PX.Objects.FS.FSRoute (EntityType)

Label: "Route"
Key: RouteCD
Entity sets: PX_Objects_FS_FSRoute, Route, FSRoute
Non-filterable, non-selectable: NoteText, BeginBranchCD, EndBranchCD, BeginBranchLocationCD, EndBranchLocationCD, MemRouteName, MemRoute, MemRouteDescription

PX.Objects.FS.FSRoute.RouteID : Edm.Int32 "RouteID"
PX.Objects.FS.FSRoute.RouteCD : Edm.String [key] "Route ID"
PX.Objects.FS.FSRoute.ActiveOnMonday : Edm.Boolean "Monday"
PX.Objects.FS.FSRoute.ActiveOnTuesday : Edm.Boolean "Tuesday"
PX.Objects.FS.FSRoute.ActiveOnWednesday : Edm.Boolean "Wednesday"
PX.Objects.FS.FSRoute.ActiveOnThursday : Edm.Boolean "Thursday"
PX.Objects.FS.FSRoute.ActiveOnFriday : Edm.Boolean "Friday"
PX.Objects.FS.FSRoute.ActiveOnSaturday : Edm.Boolean "Saturday"
PX.Objects.FS.FSRoute.ActiveOnSunday : Edm.Boolean "Sunday"
PX.Objects.FS.FSRoute.BeginTimeOnMonday : Edm.DateTimeOffset "Start time"
PX.Objects.FS.FSRoute.BeginTimeOnTuesday : Edm.DateTimeOffset "Start time"
PX.Objects.FS.FSRoute.BeginTimeOnWednesday : Edm.DateTimeOffset "Start time"
PX.Objects.FS.FSRoute.BeginTimeOnThursday : Edm.DateTimeOffset "Start time"
PX.Objects.FS.FSRoute.BeginTimeOnFriday : Edm.DateTimeOffset "Start time"
PX.Objects.FS.FSRoute.BeginTimeOnSaturday : Edm.DateTimeOffset "Start time"
PX.Objects.FS.FSRoute.BeginTimeOnSunday : Edm.DateTimeOffset "Start time"
PX.Objects.FS.FSRoute.NbrTripOnMonday : Edm.Int32 "Nbr. Trip(s) per Day"
PX.Objects.FS.FSRoute.NbrTripOnTuesday : Edm.Int32 "Nbr. Trip(s) per Day"
PX.Objects.FS.FSRoute.NbrTripOnWednesday : Edm.Int32 "Nbr. Trip(s) per Day"
PX.Objects.FS.FSRoute.NbrTripOnThursday : Edm.Int32 "Nbr. Trip(s) per Day"
PX.Objects.FS.FSRoute.NbrTripOnFriday : Edm.Int32 "Nbr. Trip(s) per Day"
PX.Objects.FS.FSRoute.NbrTripOnSaturday : Edm.Int32 "Nbr. Trip(s) per Day"
PX.Objects.FS.FSRoute.NbrTripOnSunday : Edm.Int32 "Nbr. Trip(s) per Day"
PX.Objects.FS.FSRoute.Descr : Edm.String "Description"
PX.Objects.FS.FSRoute.VehicleTypeID : Edm.Int32 "Vehicle Type"
PX.Objects.FS.FSRoute.OriginRouteID : Edm.Int32 "Origin Route"
PX.Objects.FS.FSRoute.MaxAppointmentQty : Edm.Int32 "Max. Appointment Qty."
PX.Objects.FS.FSRoute.NoAppointmentLimit : Edm.Boolean [required] "No Limit"
PX.Objects.FS.FSRoute.RouteShort : Edm.String "Route Short"
PX.Objects.FS.FSRoute.WeekCode : Edm.String "Week Code(s) e.g.: 1, 2B, 1ACS"
PX.Objects.FS.FSRoute.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSRoute.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSRoute.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSRoute.CreatedByScreenID : Edm.String
PX.Objects.FS.FSRoute.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSRoute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSRoute.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSRoute.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSRoute.RouteBeginLocationType : Edm.String "Start Location Type"
PX.Objects.FS.FSRoute.RouteEndLocationType : Edm.String "End Location Type"
PX.Objects.FS.FSRoute.BeginBranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSRoute.BeginBranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.FSRoute.EndBranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSRoute.EndBranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.FSRoute.tstamp : Edm.Binary
PX.Objects.FS.FSRoute.BeginBranchCD : Edm.String "Start Branch"
PX.Objects.FS.FSRoute.EndBranchCD : Edm.String "End Branch"
PX.Objects.FS.FSRoute.BeginBranchLocationCD : Edm.String "Start Branch Location"
PX.Objects.FS.FSRoute.EndBranchLocationCD : Edm.String "End Branch Location"
PX.Objects.FS.FSRoute.MemRouteName : Edm.String "Route Name"
PX.Objects.FS.FSRoute.MemRoute : Edm.String "Route"
PX.Objects.FS.FSRoute.MemRouteDescription : Edm.String "Route Description"
PX.Objects.FS.FSRoute.BranchByBeginBranchID -> PX.Objects.GL.Branch (BeginBranchID=BranchID)
PX.Objects.FS.FSRoute.BranchByEndBranchID -> PX.Objects.GL.Branch (EndBranchID=BranchID)
PX.Objects.FS.FSRoute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSRoute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSRoute.FSBranchLocationByBeginBranchLocationID -> PX.Objects.FS.FSBranchLocation (BeginBranchLocationID=BranchLocationID)
PX.Objects.FS.FSRoute.FSBranchLocationByEndBranchLocationID -> PX.Objects.FS.FSBranchLocation (EndBranchLocationID=BranchLocationID)
PX.Objects.FS.FSRoute.FSBranchLocationByBeginBranchID -> PX.Objects.FS.FSBranchLocation (BeginBranchLocationID=BranchLocationID, BeginBranchID=BranchID)
PX.Objects.FS.FSRoute.FSBranchLocationByEndBranchID -> PX.Objects.FS.FSBranchLocation (EndBranchLocationID=BranchLocationID, EndBranchID=BranchID)
PX.Objects.FS.FSRoute.FSRouteByRouteID -> PX.Objects.FS.FSRoute (RouteID=OriginRouteID)
PX.Objects.FS.FSRoute.FSVehicleTypeByVehicleTypeID -> PX.Objects.FS.FSVehicleType (VehicleTypeID=VehicleTypeID)
PX.Objects.FS.FSRoute.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.FSRoute.FSRouteCollection -> Collection(PX.Objects.FS.FSRoute)
PX.Objects.FS.FSRoute.FSRouteDocumentCollection -> Collection(PX.Objects.FS.FSRouteDocument)
PX.Objects.FS.FSRoute.FSRouteEmployeeCollection -> Collection(PX.Objects.FS.FSRouteEmployee)
PX.Objects.FS.FSRoute.FSScheduleRouteCollection -> Collection(PX.Objects.FS.FSScheduleRoute)
PX.Objects.FS.FSRoute.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)

# PX.Objects.FS.FSRouteAppointmentForecasting (EntityType)

Key: ScheduleID, StartDate
Entity sets: PX_Objects_FS_FSRouteAppointmentForecasting

PX.Objects.FS.FSRouteAppointmentForecasting.ScheduleID : Edm.Int32 [key] "ScheduleID"
PX.Objects.FS.FSRouteAppointmentForecasting.StartDate : Edm.DateTimeOffset [key] "Start Date"
PX.Objects.FS.FSRouteAppointmentForecasting.RouteID : Edm.Int32 "Route ID"
PX.Objects.FS.FSRouteAppointmentForecasting.CustomerID : Edm.Int32 "Customer"
PX.Objects.FS.FSRouteAppointmentForecasting.ServiceContractID : Edm.Int32 "Service Contract ID"
PX.Objects.FS.FSRouteAppointmentForecasting.SequenceOrder : Edm.Int32 "Sequence Order"
PX.Objects.FS.FSRouteAppointmentForecasting.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSRouteAppointmentForecasting.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule (ScheduleID=ScheduleID)
PX.Objects.FS.FSRouteAppointmentForecasting.FSScheduleByServiceContractID -> PX.Objects.FS.FSSchedule (ScheduleID=ScheduleID, ServiceContractID=EntityID)
PX.Objects.FS.FSRouteAppointmentForecasting.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.FSRouteAppointmentForecasting.FSRouteByRouteID -> PX.Objects.FS.FSRoute (RouteID=RouteID)
PX.Objects.FS.FSRouteAppointmentForecasting.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID)
PX.Objects.FS.FSRouteAppointmentForecasting.FSServiceContractByCustomerID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID, CustomerID=CustomerID)

# PX.Objects.FS.FSRouteContractSchedule (EntityType)

BaseType: PX.Objects.FS.FSSchedule
Key: CustomerID, RefNbr (inherited from PX.Objects.FS.FSSchedule)
Entity sets: PX_Objects_FS_FSRouteContractSchedule
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FS.FSRouteContractSchedule.FormCaptionDescription : Edm.String

# PX.Objects.FS.FSRouteContractScheduleFSServiceContract (EntityType)

BaseType: PX.Objects.FS.FSRouteContractSchedule
Key: CustomerID, RefNbr (inherited from PX.Objects.FS.FSSchedule)
Entity sets: PX_Objects_FS_FSRouteContractScheduleFSServiceContract

PX.Objects.FS.FSRouteContractScheduleFSServiceContract.ServiceContractRefNbr : Edm.String "Service Contract ID"
PX.Objects.FS.FSRouteContractScheduleFSServiceContract.CustomerContractNbr : Edm.String "Customer Contract Nbr."
PX.Objects.FS.FSRouteContractScheduleFSServiceContract.DocDesc : Edm.String "Description"
PX.Objects.FS.FSRouteContractScheduleFSServiceContract.FSServiceContractByServiceContractRefNbr -> PX.Objects.FS.FSServiceContract (ServiceContractRefNbr=RefNbr)

# PX.Objects.FS.FSRouteDocument (EntityType)

Label: "Route Document"
Key: RefNbr
Entity sets: PX_Objects_FS_FSRouteDocument, RouteDocument, FSRouteDocument
Non-filterable, non-selectable: NoteText, FormCaptionDescription, RouteNumberingID, MemActualDuration, MemBusinessDateTime, GPSLatitudeLongitude, MustRecalculateStats, MemAdditionalDriverName, ApproximateValuesLabel

PX.Objects.FS.FSRouteDocument.RefNbr : Edm.String [key] "Route Nbr."
PX.Objects.FS.FSRouteDocument.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSRouteDocument.RouteDocumentID : Edm.Int32 "RouteDocumentID"
PX.Objects.FS.FSRouteDocument.Date : Edm.DateTimeOffset "Schedule Start Date"
PX.Objects.FS.FSRouteDocument.RouteID : Edm.Int32 "Route"
PX.Objects.FS.FSRouteDocument.DriverID : Edm.Int32 "Driver"
PX.Objects.FS.FSRouteDocument.AdditionalDriverID : Edm.Int32 "Additional Driver"
PX.Objects.FS.FSRouteDocument.RouteStatsUpdated : Edm.Boolean "Route Stats Updated"
PX.Objects.FS.FSRouteDocument.Status : Edm.String "Status"
PX.Objects.FS.FSRouteDocument.TimeBegin : Edm.DateTimeOffset "Start Time"
PX.Objects.FS.FSRouteDocument.TimeEnd : Edm.DateTimeOffset "End Time"
PX.Objects.FS.FSRouteDocument.TripNbr : Edm.Int32 "Trip Nbr."
PX.Objects.FS.FSRouteDocument.ActualStartTime : Edm.DateTimeOffset "Actual Start Date"
PX.Objects.FS.FSRouteDocument.ActualEndTime : Edm.DateTimeOffset "Actual End Date"
PX.Objects.FS.FSRouteDocument.TotalNumAppointments : Edm.Int32 "Number of Appointments"
PX.Objects.FS.FSRouteDocument.TotalDuration : Edm.Int32 "Total Driving Duration"
PX.Objects.FS.FSRouteDocument.TotalDistance : Edm.Decimal
PX.Objects.FS.FSRouteDocument.TotalDistanceFriendly : Edm.String "Total Distance"
PX.Objects.FS.FSRouteDocument.TotalServices : Edm.Int32 "Total Services"
PX.Objects.FS.FSRouteDocument.TotalServicesDuration : Edm.Int32 "Total Services Duration"
PX.Objects.FS.FSRouteDocument.TotalTravelTime : Edm.Int32 "Total Route Duration"
PX.Objects.FS.FSRouteDocument.VehicleID : Edm.Int32 "Vehicle"
PX.Objects.FS.FSRouteDocument.AdditionalVehicleID1 : Edm.Int32 "Additional Vehicle 1"
PX.Objects.FS.FSRouteDocument.AdditionalVehicleID2 : Edm.Int32 "Additional Vehicle 2"
PX.Objects.FS.FSRouteDocument.GPSLatitudeStart : Edm.Decimal "Latitude"
PX.Objects.FS.FSRouteDocument.GPSLongitudeStart : Edm.Decimal "Longitude"
PX.Objects.FS.FSRouteDocument.GPSLatitudeComplete : Edm.Decimal "Latitude"
PX.Objects.FS.FSRouteDocument.GPSLongitudeComplete : Edm.Decimal "Longitude"
PX.Objects.FS.FSRouteDocument.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSRouteDocument.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSRouteDocument.GeneratedBySystem : Edm.Boolean [required] "Generated by System"
PX.Objects.FS.FSRouteDocument.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSRouteDocument.CreatedByScreenID : Edm.String
PX.Objects.FS.FSRouteDocument.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSRouteDocument.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSRouteDocument.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSRouteDocument.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSRouteDocument.tstamp : Edm.Binary
PX.Objects.FS.FSRouteDocument.Miles : Edm.Int32 "Miles"
PX.Objects.FS.FSRouteDocument.Weight : Edm.Int32 "Weight"
PX.Objects.FS.FSRouteDocument.FuelQty : Edm.Int32 "Fuel Qty."
PX.Objects.FS.FSRouteDocument.FuelType : Edm.String "Fuel Type"
PX.Objects.FS.FSRouteDocument.Oil : Edm.Int32 "Oil"
PX.Objects.FS.FSRouteDocument.AntiFreeze : Edm.Int32 "Anti-freeze"
PX.Objects.FS.FSRouteDocument.DEF : Edm.Int32 "DEF"
PX.Objects.FS.FSRouteDocument.Propane : Edm.Int32 "Propane"
PX.Objects.FS.FSRouteDocument.FormCaptionDescription : Edm.String
PX.Objects.FS.FSRouteDocument.RouteNumberingID : Edm.String "Route Numbering ID"
PX.Objects.FS.FSRouteDocument.MemActualDuration : Edm.Int32 "Actual Duration"
PX.Objects.FS.FSRouteDocument.MemBusinessDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSRouteDocument.GPSLatitudeLongitude : Edm.String "GPS Latitude Longitude"
PX.Objects.FS.FSRouteDocument.MustRecalculateStats : Edm.Boolean
PX.Objects.FS.FSRouteDocument.RouteCD : Edm.String "RouteCD"
PX.Objects.FS.FSRouteDocument.MemAdditionalDriverName : Edm.String "Additional Driver Name"
PX.Objects.FS.FSRouteDocument.ApproximateValuesLabel : Edm.String
PX.Objects.FS.FSRouteDocument.TimeBeginUTC : Edm.DateTimeOffset "Start Time"
PX.Objects.FS.FSRouteDocument.TimeEndUTC : Edm.DateTimeOffset "End Time"
PX.Objects.FS.FSRouteDocument.ActualStartTimeUTC : Edm.DateTimeOffset "Actual Start Time"
PX.Objects.FS.FSRouteDocument.ActualEndTimeUTC : Edm.DateTimeOffset "Actual End Time"
PX.Objects.FS.FSRouteDocument.EPEmployeeFSRouteEmployeeByRouteID -> PX.Objects.FS.EPEmployeeFSRouteEmployee (DriverID=BAccountID, RouteID=RouteID)
PX.Objects.FS.FSRouteDocument.VendorByDriverID -> PX.Objects.AP.Vendor (DriverID=BAccountID)
PX.Objects.FS.FSRouteDocument.VendorByAdditionalDriverID -> PX.Objects.AP.Vendor (AdditionalDriverID=BAccountID)
PX.Objects.FS.FSRouteDocument.FSEquipmentByVehicleID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSRouteDocument.FSEquipmentByAdditionalVehicleID1 -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSRouteDocument.FSEquipmentByAdditionalVehicleID2 -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSRouteDocument.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSRouteDocument.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSRouteDocument.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSRouteDocument.FSRouteByRouteID -> PX.Objects.FS.FSRoute (RouteID=RouteID)
PX.Objects.FS.FSRouteDocument.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)

# PX.Objects.FS.FSRouteEmployee (EntityType)

Key: EmployeeID, RouteID
Entity sets: PX_Objects_FS_FSRouteEmployee

PX.Objects.FS.FSRouteEmployee.RouteID : Edm.Int32 [key]
PX.Objects.FS.FSRouteEmployee.EmployeeID : Edm.Int32 [key] "Employee ID"
PX.Objects.FS.FSRouteEmployee.PriorityPreference : Edm.Int32 [required] "Priority Preference"
PX.Objects.FS.FSRouteEmployee.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSRouteEmployee.CreatedByScreenID : Edm.String
PX.Objects.FS.FSRouteEmployee.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSRouteEmployee.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSRouteEmployee.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSRouteEmployee.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSRouteEmployee.tstamp : Edm.Binary
PX.Objects.FS.FSRouteEmployee.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.FS.FSRouteEmployee.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSRouteEmployee.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSRouteEmployee.FSRouteByRouteID -> PX.Objects.FS.FSRoute (RouteID=RouteID)

# PX.Objects.FS.FSRouteSetup (EntityType)

Label: "Route Management Preferences"
Singletons: PX_Objects_FS_FSRouteSetup, RouteManagementPreferences, FSRouteSetup

PX.Objects.FS.FSRouteSetup.RouteNumberingID : Edm.String "Route Numbering Sequence"
PX.Objects.FS.FSRouteSetup.AutoCalculateRouteStats : Edm.Boolean [required] "Calculate Route Statistics Automatically"
PX.Objects.FS.FSRouteSetup.DfltSrvOrdType : Edm.String "Default Service Order Type"
PX.Objects.FS.FSRouteSetup.GroupINDocumentsByPostingProcess : Edm.Boolean [required] "Group Inventory Documents by Posting Process"
PX.Objects.FS.FSRouteSetup.TrackRouteLocation : Edm.Boolean [required] "Track Start and Complete Location of Route"
PX.Objects.FS.FSRouteSetup.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSRouteSetup.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSRouteSetup.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSRouteSetup.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSRouteSetup.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSRouteSetup.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSRouteSetup.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSRouteSetup.SetFirstManualAppointment : Edm.Boolean [required] "Set Appointments Created Manually as First in Route"
PX.Objects.FS.FSRouteSetup.EnableSeasonScheduleContract : Edm.Boolean "Enable Seasons in Schedule Contracts"
PX.Objects.FS.FSRouteSetup.NoteID : Edm.Guid
PX.Objects.FS.FSRouteSetup.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSRouteSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSRouteSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSRouteSetup.NumberingByRouteNumberingID -> PX.Objects.CS.Numbering (RouteNumberingID=NumberingID)
PX.Objects.FS.FSRouteSetup.FSSrvOrdTypeByDfltSrvOrdType -> PX.Objects.FS.FSSrvOrdType (DfltSrvOrdType=SrvOrdType)

# PX.Objects.FS.FSSalesPrice (EntityType)

Key: InventoryID, ServiceContractID, UOM
Entity sets: PX_Objects_FS_FSSalesPrice
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSSalesPrice.SalesPriceID : Edm.Int32
PX.Objects.FS.FSSalesPrice.ServiceContractID : Edm.Int32 [key] "Service Contract ID"
PX.Objects.FS.FSSalesPrice.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.FS.FSSalesPrice.LineType : Edm.String "Line Type"
PX.Objects.FS.FSSalesPrice.UnitPrice : Edm.Decimal
PX.Objects.FS.FSSalesPrice.UOM : Edm.String [key] "UOM"
PX.Objects.FS.FSSalesPrice.CuryID : Edm.String "Currency"
PX.Objects.FS.FSSalesPrice.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSSalesPrice.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSSalesPrice.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSSalesPrice.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSSalesPrice.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSSalesPrice.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSSalesPrice.tstamp : Edm.Binary
PX.Objects.FS.FSSalesPrice.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSSalesPrice.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSSalesPrice.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSalesPrice.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSalesPrice.INUnitByUOM -> PX.Objects.IN.INUnit (UOM=FromUnit)
PX.Objects.FS.FSSalesPrice.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)

# PX.Objects.FS.FSSchedule (EntityType)

Key: CustomerID, RefNbr
Entity sets: PX_Objects_FS_FSSchedule
Non-filterable, non-selectable: NoteText, YearlyLabel, MonthlyLabel, WeeklyLabel, DailyLabel, SrvOrdTypeMessage, ContractDescr, ReportScheduleID, OrigScheduleRefNbr, OrigServiceContractRefNbr, BillCustomerID

PX.Objects.FS.FSSchedule.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.FS.FSSchedule.ScheduleID : Edm.Int32 "ScheduleID"
PX.Objects.FS.FSSchedule.Active : Edm.Boolean "Active"
PX.Objects.FS.FSSchedule.AnnualFrequency : Edm.Int16 "Every"
PX.Objects.FS.FSSchedule.AnnualOnDay : Edm.Int16 "On Day"
PX.Objects.FS.FSSchedule.AnnualOnDayOfWeek : Edm.Int16 "Day of Week"
PX.Objects.FS.FSSchedule.AnnualOnWeek : Edm.Int16 "On the"
PX.Objects.FS.FSSchedule.AnnualRecurrenceType : Edm.String "Schedule On"
PX.Objects.FS.FSSchedule.AnnualOnJan : Edm.Boolean "January"
PX.Objects.FS.FSSchedule.AnnualOnFeb : Edm.Boolean "February"
PX.Objects.FS.FSSchedule.AnnualOnMar : Edm.Boolean "March"
PX.Objects.FS.FSSchedule.AnnualOnApr : Edm.Boolean "April"
PX.Objects.FS.FSSchedule.AnnualOnMay : Edm.Boolean "May"
PX.Objects.FS.FSSchedule.AnnualOnJun : Edm.Boolean "June"
PX.Objects.FS.FSSchedule.AnnualOnJul : Edm.Boolean "July"
PX.Objects.FS.FSSchedule.AnnualOnAug : Edm.Boolean "August"
PX.Objects.FS.FSSchedule.AnnualOnSep : Edm.Boolean "September"
PX.Objects.FS.FSSchedule.AnnualOnOct : Edm.Boolean "October"
PX.Objects.FS.FSSchedule.AnnualOnNov : Edm.Boolean "November"
PX.Objects.FS.FSSchedule.AnnualOnDec : Edm.Boolean "December"
PX.Objects.FS.FSSchedule.BranchID : Edm.Int32 "Branch ID"
PX.Objects.FS.FSSchedule.BranchLocationID : Edm.Int32 "Branch Location ID"
PX.Objects.FS.FSSchedule.CustomerID : Edm.Int32 [key] "Customer"
PX.Objects.FS.FSSchedule.DailyFrequency : Edm.Int16 "Every"
PX.Objects.FS.FSSchedule.EndDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.FS.FSSchedule.EntityID : Edm.Int32 "Entity ID"
PX.Objects.FS.FSSchedule.EntityType : Edm.String "Entity Type"
PX.Objects.FS.FSSchedule.FrequencyType : Edm.String "Frequency"
PX.Objects.FS.FSSchedule.LastGeneratedElementDate : Edm.DateTimeOffset "Last Generated"
PX.Objects.FS.FSSchedule.LineCntr : Edm.Int32 [required]
PX.Objects.FS.FSSchedule.Monthly2Selected : Edm.Boolean "Second Recurrence"
PX.Objects.FS.FSSchedule.Monthly3Selected : Edm.Boolean "Third Recurrence"
PX.Objects.FS.FSSchedule.Monthly4Selected : Edm.Boolean "Fourth Recurrence"
PX.Objects.FS.FSSchedule.MonthlyFrequency : Edm.Int16 "Every"
PX.Objects.FS.FSSchedule.MonthlyRecurrenceType1 : Edm.String "Schedule On"
PX.Objects.FS.FSSchedule.MonthlyRecurrenceType2 : Edm.String "Schedule On"
PX.Objects.FS.FSSchedule.MonthlyRecurrenceType3 : Edm.String "Schedule On"
PX.Objects.FS.FSSchedule.MonthlyRecurrenceType4 : Edm.String "Schedule On"
PX.Objects.FS.FSSchedule.MonthlyOnDay1 : Edm.Int16 "On Day"
PX.Objects.FS.FSSchedule.MonthlyOnDay2 : Edm.Int16 "On Day"
PX.Objects.FS.FSSchedule.MonthlyOnDay3 : Edm.Int16 "On Day"
PX.Objects.FS.FSSchedule.MonthlyOnDay4 : Edm.Int16 "On Day"
PX.Objects.FS.FSSchedule.MonthlyOnWeek1 : Edm.Int16 "On the"
PX.Objects.FS.FSSchedule.MonthlyOnWeek2 : Edm.Int16 "On the"
PX.Objects.FS.FSSchedule.MonthlyOnWeek3 : Edm.Int16 "On the"
PX.Objects.FS.FSSchedule.MonthlyOnWeek4 : Edm.Int16 "On the"
PX.Objects.FS.FSSchedule.MonthlyOnDayOfWeek1 : Edm.Int16 "Day of Week"
PX.Objects.FS.FSSchedule.MonthlyOnDayOfWeek2 : Edm.Int16 "Day of Week"
PX.Objects.FS.FSSchedule.MonthlyOnDayOfWeek3 : Edm.Int16 "Day of Week"
PX.Objects.FS.FSSchedule.MonthlyOnDayOfWeek4 : Edm.Int16 "Day of Week"
PX.Objects.FS.FSSchedule.NoRunLimit : Edm.Boolean "No Limit"
PX.Objects.FS.FSSchedule.RestrictionMax : Edm.Boolean [required] "Enable Max. Restriction"
PX.Objects.FS.FSSchedule.RestrictionMin : Edm.Boolean [required] "Enable Min. Restriction"
PX.Objects.FS.FSSchedule.RestrictionMaxTime : Edm.DateTimeOffset "Maximum Time Restriction"
PX.Objects.FS.FSSchedule.RestrictionMinTime : Edm.DateTimeOffset "Minimum Time Restriction"
PX.Objects.FS.FSSchedule.RunCntr : Edm.Int16 "Executed (times)"
PX.Objects.FS.FSSchedule.RunLimit : Edm.Int16 "Execution Limit (times)"
PX.Objects.FS.FSSchedule.SrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSSchedule.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.FS.FSSchedule.WeeklyFrequency : Edm.Int16 "Every"
PX.Objects.FS.FSSchedule.WeeklyOnSun : Edm.Boolean "Sunday"
PX.Objects.FS.FSSchedule.WeeklyOnMon : Edm.Boolean "Monday"
PX.Objects.FS.FSSchedule.WeeklyOnTue : Edm.Boolean "Tuesday"
PX.Objects.FS.FSSchedule.WeeklyOnWed : Edm.Boolean "Wednesday"
PX.Objects.FS.FSSchedule.WeeklyOnThu : Edm.Boolean "Thursday"
PX.Objects.FS.FSSchedule.WeeklyOnFri : Edm.Boolean "Friday"
PX.Objects.FS.FSSchedule.WeeklyOnSat : Edm.Boolean "Saturday"
PX.Objects.FS.FSSchedule.VendorID : Edm.Int32 "Vendor"
PX.Objects.FS.FSSchedule.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSSchedule.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSSchedule.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSSchedule.CreatedByScreenID : Edm.String
PX.Objects.FS.FSSchedule.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSSchedule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSSchedule.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSSchedule.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSSchedule.tstamp : Edm.Binary
PX.Objects.FS.FSSchedule.VehicleTypeID : Edm.Int32 "Vehicle Type ID"
PX.Objects.FS.FSSchedule.RecurrenceDescription : Edm.String "Recurrence Description"
PX.Objects.FS.FSSchedule.EmployeeID : Edm.Int32 "Employee ID"
PX.Objects.FS.FSSchedule.ScheduleType : Edm.String "Schedule Type"
PX.Objects.FS.FSSchedule.WeekCode : Edm.String "Week Codes e.g.: 1, 2B, 1ACS"
PX.Objects.FS.FSSchedule.SeasonOnJan : Edm.Boolean "January"
PX.Objects.FS.FSSchedule.SeasonOnFeb : Edm.Boolean "February"
PX.Objects.FS.FSSchedule.SeasonOnMar : Edm.Boolean "March"
PX.Objects.FS.FSSchedule.SeasonOnApr : Edm.Boolean "April"
PX.Objects.FS.FSSchedule.SeasonOnMay : Edm.Boolean "May"
PX.Objects.FS.FSSchedule.SeasonOnJun : Edm.Boolean "June"
PX.Objects.FS.FSSchedule.SeasonOnJul : Edm.Boolean "July"
PX.Objects.FS.FSSchedule.SeasonOnAug : Edm.Boolean "August"
PX.Objects.FS.FSSchedule.SeasonOnSep : Edm.Boolean "September"
PX.Objects.FS.FSSchedule.SeasonOnOct : Edm.Boolean "October"
PX.Objects.FS.FSSchedule.SeasonOnNov : Edm.Boolean "November"
PX.Objects.FS.FSSchedule.SeasonOnDec : Edm.Boolean "December"
PX.Objects.FS.FSSchedule.EnableExpirationDate : Edm.Boolean [required] "Enable Expiration Date"
PX.Objects.FS.FSSchedule.YearlyLabel : Edm.String "YearlyLabel"
PX.Objects.FS.FSSchedule.MonthlyLabel : Edm.String "MonthlyLabel"
PX.Objects.FS.FSSchedule.WeeklyLabel : Edm.String "WeeklyLabel"
PX.Objects.FS.FSSchedule.DailyLabel : Edm.String "DailyLabel"
PX.Objects.FS.FSSchedule.SrvOrdTypeMessage : Edm.String "SrvOrdTypeMessage"
PX.Objects.FS.FSSchedule.ContractDescr : Edm.String "ContractDescr"
PX.Objects.FS.FSSchedule.CustomerLocationID : Edm.Int32 "Location"
PX.Objects.FS.FSSchedule.ScheduleGenType : Edm.String "Schedule Generation Type"
PX.Objects.FS.FSSchedule.ScheduleStartTime : Edm.DateTimeOffset "Schedule Start Time"
PX.Objects.FS.FSSchedule.NextExecutionDate : Edm.DateTimeOffset "Next Execution Date"
PX.Objects.FS.FSSchedule.RestrictionMaxTimeUTC : Edm.DateTimeOffset "Maximum Time Restriction"
PX.Objects.FS.FSSchedule.RestrictionMinTimeUTC : Edm.DateTimeOffset "Minimum Time Restriction"
PX.Objects.FS.FSSchedule.EndDateUTC : Edm.DateTimeOffset "Expiration Date"
PX.Objects.FS.FSSchedule.ReportScheduleID : Edm.Int32 "Schedule ID"
PX.Objects.FS.FSSchedule.OverrideDuration : Edm.Boolean "Override"
PX.Objects.FS.FSSchedule.ScheduleDuration : Edm.Int32 [required] "Schedule Duration"
PX.Objects.FS.FSSchedule.EstimatedDurationTotal : Edm.Int32 [required] "Estimated Duration Total"
PX.Objects.FS.FSSchedule.OrigScheduleRefNbr : Edm.String "Orig. Schedule ID"
PX.Objects.FS.FSSchedule.OrigServiceContractRefNbr : Edm.String "Orig. Service Contract ID"
PX.Objects.FS.FSSchedule.BillCustomerID : Edm.Int32 "Billing Customer"
PX.Objects.FS.FSSchedule.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.FS.FSSchedule.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.FS.FSSchedule.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.FS.FSSchedule.PMTaskByDfltProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSSchedule.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSSchedule.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSSchedule.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSSchedule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSchedule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSchedule.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID, CustomerLocationID=LocationID)
PX.Objects.FS.FSSchedule.LocationByCustomerID -> PX.Objects.CR.Location (CustomerLocationID=LocationID, CustomerID=BAccountID)
PX.Objects.FS.FSSchedule.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.FSSchedule.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.FSSchedule.FSServiceContractByEntityID -> PX.Objects.FS.FSServiceContract (EntityID=ServiceContractID)
PX.Objects.FS.FSSchedule.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSSchedule.FSVehicleTypeByVehicleTypeID -> PX.Objects.FS.FSVehicleType (VehicleTypeID=VehicleTypeID)
PX.Objects.FS.FSSchedule.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSSchedule.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSSchedule.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.FSSchedule.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.FSSchedule.FSContractActionCollection -> Collection(PX.Objects.FS.FSContractAction)
PX.Objects.FS.FSSchedule.FSContractGenerationHistoryCollection -> Collection(PX.Objects.FS.FSContractGenerationHistory)
PX.Objects.FS.FSSchedule.FSGenerationLogErrorCollection -> Collection(PX.Objects.FS.FSGenerationLogError)
PX.Objects.FS.FSSchedule.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.FS.FSSchedule.FSScheduleRouteCollection -> Collection(PX.Objects.FS.FSScheduleRoute)
PX.Objects.FS.FSSchedule.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)

# PX.Objects.FS.FSScheduleDet (EntityType)

Label: "FSScheduleDet"
Key: LineNbr, ScheduleID
Entity sets: PX_Objects_FS_FSScheduleDet, FSScheduleDet
Non-filterable, non-selectable: NoteText, SkipCostCodeValidation

PX.Objects.FS.FSScheduleDet.ScheduleID : Edm.Int32 [key] "ScheduleID"
PX.Objects.FS.FSScheduleDet.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.FSScheduleDet.ScheduleDetID : Edm.Int32 "ScheduleDetID"
PX.Objects.FS.FSScheduleDet.LineType : Edm.String "Line Type"
PX.Objects.FS.FSScheduleDet.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSScheduleDet.BillingRule : Edm.String "Billing Rule"
PX.Objects.FS.FSScheduleDet.EstimatedDuration : Edm.Int32 "Estimated Duration"
PX.Objects.FS.FSScheduleDet.Qty : Edm.Decimal "Estimated Quantity"
PX.Objects.FS.FSScheduleDet.ServiceTemplateID : Edm.Int32 "Service Template ID"
PX.Objects.FS.FSScheduleDet.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.FS.FSScheduleDet.TranDesc : Edm.String "Transaction Description"
PX.Objects.FS.FSScheduleDet.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSScheduleDet.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSScheduleDet.UOM : Edm.String "UOM"
PX.Objects.FS.FSScheduleDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSScheduleDet.CreatedByScreenID : Edm.String
PX.Objects.FS.FSScheduleDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSScheduleDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSScheduleDet.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSScheduleDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSScheduleDet.tstamp : Edm.Binary
PX.Objects.FS.FSScheduleDet.ProjectID : Edm.Int32
PX.Objects.FS.FSScheduleDet.SkipCostCodeValidation : Edm.Boolean
PX.Objects.FS.FSScheduleDet.EquipmentItemClass : Edm.String
PX.Objects.FS.FSScheduleDet.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.FS.FSScheduleDet.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.FS.FSScheduleDet.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.FS.FSScheduleDet.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSScheduleDet.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule (ScheduleID=ScheduleID)
PX.Objects.FS.FSScheduleDet.FSEquipmentBySMequipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSScheduleDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSScheduleDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSScheduleDet.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.FS.FSScheduleDet.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.FS.FSScheduleDet.FSEquipmentComponentByEquipmentLineRef -> PX.Objects.FS.FSEquipmentComponent
PX.Objects.FS.FSScheduleDet.FSEquipmentComponentBySMequipmentID -> PX.Objects.FS.FSEquipmentComponent
PX.Objects.FS.FSScheduleDet.FSModelTemplateComponentByComponentID -> PX.Objects.FS.FSModelTemplateComponent
PX.Objects.FS.FSScheduleDet.FSServiceTemplateByServiceTemplateID -> PX.Objects.FS.FSServiceTemplate (ServiceTemplateID=ServiceTemplateID)
PX.Objects.FS.FSScheduleDet.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSScheduleDet.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)

# PX.Objects.FS.FSScheduleRoute (EntityType)

Label: "FSScheduleRoute"
Key: ScheduleID
Entity sets: PX_Objects_FS_FSScheduleRoute, FSScheduleRoute
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSScheduleRoute.ScheduleID : Edm.Int32 [key]
PX.Objects.FS.FSScheduleRoute.DfltRouteID : Edm.Int32 "Route ID"
PX.Objects.FS.FSScheduleRoute.GlobalSequence : Edm.String "Order"
PX.Objects.FS.FSScheduleRoute.RouteIDFriday : Edm.Int32 "Route Friday"
PX.Objects.FS.FSScheduleRoute.RouteIDMonday : Edm.Int32 "Route Monday"
PX.Objects.FS.FSScheduleRoute.RouteIDSaturday : Edm.Int32 "Route Saturday"
PX.Objects.FS.FSScheduleRoute.RouteIDSunday : Edm.Int32 "Route Sunday"
PX.Objects.FS.FSScheduleRoute.RouteIDThursday : Edm.Int32 "Route Thursday"
PX.Objects.FS.FSScheduleRoute.RouteIDTuesday : Edm.Int32 "Route Tuesday"
PX.Objects.FS.FSScheduleRoute.RouteIDWednesday : Edm.Int32 "Route Wednesday"
PX.Objects.FS.FSScheduleRoute.SequenceFriday : Edm.String "Sequence Friday"
PX.Objects.FS.FSScheduleRoute.SequenceMonday : Edm.String "Sequence Monday"
PX.Objects.FS.FSScheduleRoute.SequenceSaturday : Edm.String "Sequence Saturday"
PX.Objects.FS.FSScheduleRoute.SequenceSunday : Edm.String "Sequence Sunday"
PX.Objects.FS.FSScheduleRoute.SequenceThursday : Edm.String "Sequence Thursday"
PX.Objects.FS.FSScheduleRoute.SequenceTuesday : Edm.String "Sequence Tuesday"
PX.Objects.FS.FSScheduleRoute.SequenceWednesday : Edm.String "Sequence Wednesday"
PX.Objects.FS.FSScheduleRoute.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSScheduleRoute.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSScheduleRoute.DeliveryNotes : Edm.String "Delivery Notes"
PX.Objects.FS.FSScheduleRoute.InternalNotes : Edm.String "Internal Notes"
PX.Objects.FS.FSScheduleRoute.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSScheduleRoute.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSScheduleRoute.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSScheduleRoute.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSScheduleRoute.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSScheduleRoute.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSScheduleRoute.tstamp : Edm.Binary
PX.Objects.FS.FSScheduleRoute.SortingIndex : Edm.Int32 "Sorting Index"
PX.Objects.FS.FSScheduleRoute.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule (ScheduleID=ScheduleID)
PX.Objects.FS.FSScheduleRoute.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSScheduleRoute.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSScheduleRoute.FSRouteByDfltRouteID -> PX.Objects.FS.FSRoute (DfltRouteID=RouteID)
PX.Objects.FS.FSScheduleRoute.FSRouteByRouteIDMonday -> PX.Objects.FS.FSRoute (RouteIDMonday=RouteID)
PX.Objects.FS.FSScheduleRoute.FSRouteByRouteIDTuesday -> PX.Objects.FS.FSRoute (RouteIDTuesday=RouteID)
PX.Objects.FS.FSScheduleRoute.FSRouteByRouteIDWednesday -> PX.Objects.FS.FSRoute (RouteIDWednesday=RouteID)
PX.Objects.FS.FSScheduleRoute.FSRouteByRouteIDThursday -> PX.Objects.FS.FSRoute (RouteIDThursday=RouteID)
PX.Objects.FS.FSScheduleRoute.FSRouteByRouteIDFriday -> PX.Objects.FS.FSRoute (RouteIDFriday=RouteID)
PX.Objects.FS.FSScheduleRoute.FSRouteByRouteIDSaturday -> PX.Objects.FS.FSRoute (RouteIDSaturday=RouteID)
PX.Objects.FS.FSScheduleRoute.FSRouteByRouteIDSunday -> PX.Objects.FS.FSRoute (RouteIDSunday=RouteID)

# PX.Objects.FS.FSServiceContract (EntityType)

Label: "Service Contract"
Key: RefNbr
Entity sets: PX_Objects_FS_FSServiceContract, ServiceContract, FSServiceContract
Non-filterable, non-selectable: ClassID, NoteText, ReportServiceContractID, HasSchedule, HasProcessedSchedule, HasForecast, ShowInvoicesTab, UsageBillingCycleID, FormCaptionDescription, OrigServiceContractRefNbr, EmailNotificationCD, DeletedDatabaseRecord

PX.Objects.FS.FSServiceContract.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSServiceContract.RefNbr : Edm.String [key] "Service Contract ID"
PX.Objects.FS.FSServiceContract.CustomerContractNbr : Edm.String "Customer Contract Nbr."
PX.Objects.FS.FSServiceContract.CustomerID : Edm.Int32 "Customer"
PX.Objects.FS.FSServiceContract.ServiceContractID : Edm.Int32
PX.Objects.FS.FSServiceContract.ClassID : Edm.String
PX.Objects.FS.FSServiceContract.BillingPeriod : Edm.String "Period"
PX.Objects.FS.FSServiceContract.BillingType : Edm.String "Billing Type"
PX.Objects.FS.FSServiceContract.BillTo : Edm.String "Bill To"
PX.Objects.FS.FSServiceContract.BillCustomerID : Edm.Int32 "Billing Customer"
PX.Objects.FS.FSServiceContract.BranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.FSServiceContract.DocDesc : Edm.String "Description"
PX.Objects.FS.FSServiceContract.ExpirationType : Edm.String "Expiration Type"
PX.Objects.FS.FSServiceContract.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.FS.FSServiceContract.DurationType : Edm.String "Duration Type"
PX.Objects.FS.FSServiceContract.RenewalDate : Edm.DateTimeOffset "Renewal Date"
PX.Objects.FS.FSServiceContract.EndDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.FS.FSServiceContract.Duration : Edm.Int32 "Duration"
PX.Objects.FS.FSServiceContract.LastBillingInvoiceDate : Edm.DateTimeOffset "Last Billing Date"
PX.Objects.FS.FSServiceContract.MasterContractID : Edm.Int32 "Master Contract"
PX.Objects.FS.FSServiceContract.NextBillingInvoiceDate : Edm.DateTimeOffset "Next Billing Date"
PX.Objects.FS.FSServiceContract.RecordType : Edm.String
PX.Objects.FS.FSServiceContract.Status : Edm.String "Status"
PX.Objects.FS.FSServiceContract.StatusEffectiveFromDate : Edm.DateTimeOffset "Effective From Date"
PX.Objects.FS.FSServiceContract.StatusEffectiveUntilDate : Edm.DateTimeOffset "Effective Until Date"
PX.Objects.FS.FSServiceContract.UpcomingStatus : Edm.String "Upcoming Status"
PX.Objects.FS.FSServiceContract.CustomerContactID : Edm.Int32 "Contact"
PX.Objects.FS.FSServiceContract.VendorID : Edm.Int32 "Vendor"
PX.Objects.FS.FSServiceContract.SourcePrice : Edm.String "Take Prices From"
PX.Objects.FS.FSServiceContract.SalesPersonID : Edm.Int32 "Salesperson ID"
PX.Objects.FS.FSServiceContract.Commissionable : Edm.Boolean "Commissionable"
PX.Objects.FS.FSServiceContract.ScheduleGenType : Edm.String "Schedule Generation Type"
PX.Objects.FS.FSServiceContract.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSServiceContract.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSServiceContract.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceContract.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSServiceContract.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSServiceContract.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceContract.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSServiceContract.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSServiceContract.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSServiceContract.IsFixedRateContract : Edm.Boolean
PX.Objects.FS.FSServiceContract.ReportServiceContractID : Edm.String
PX.Objects.FS.FSServiceContract.HasSchedule : Edm.Boolean
PX.Objects.FS.FSServiceContract.HasProcessedSchedule : Edm.Boolean
PX.Objects.FS.FSServiceContract.HasForecast : Edm.Boolean
PX.Objects.FS.FSServiceContract.ShowInvoicesTab : Edm.Boolean "ShowInvoicesTab"
PX.Objects.FS.FSServiceContract.UsageBillingCycleID : Edm.Int32 "Usage Billing Cycle"
PX.Objects.FS.FSServiceContract.ActivePeriodID : Edm.Int32
PX.Objects.FS.FSServiceContract.FormCaptionDescription : Edm.String
PX.Objects.FS.FSServiceContract.OrigServiceContractRefNbr : Edm.String "Orig Service Contract ID"
PX.Objects.FS.FSServiceContract.EmailNotificationCD : Edm.String
PX.Objects.FS.FSServiceContract.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.FS.FSServiceContract.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.FS.FSServiceContract.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.FS.FSServiceContract.PMTaskByDfltProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSServiceContract.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSServiceContract.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSServiceContract.CustomerByBillCustomerID -> PX.Objects.AR.Customer (BillCustomerID=BAccountID)
PX.Objects.FS.FSServiceContract.ContactByCustomerContactID -> PX.Objects.CR.Contact (CustomerContactID=ContactID)
PX.Objects.FS.FSServiceContract.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSServiceContract.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceContract.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSServiceContract.PMCostCodeByDfltCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.FS.FSServiceContract.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.FSServiceContract.LocationByBillLocationID -> PX.Objects.CR.Location (BillCustomerID=BAccountID)
PX.Objects.FS.FSServiceContract.LocationByBillCustomerID -> PX.Objects.CR.Location (BillCustomerID=BAccountID)
PX.Objects.FS.FSServiceContract.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.FSServiceContract.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.FS.FSServiceContract.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.FSServiceContract.FSMasterContractByMasterContractID -> PX.Objects.FS.FSMasterContract (MasterContractID=MasterContractID)
PX.Objects.FS.FSServiceContract.FSMasterContractByCustomerID -> PX.Objects.FS.FSMasterContract (MasterContractID=MasterContractID, CustomerID=CustomerID)
PX.Objects.FS.FSServiceContract.FSRouteContractScheduleFSServiceContractCollection -> Collection(PX.Objects.FS.FSRouteContractScheduleFSServiceContract)
PX.Objects.FS.FSServiceContract.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.FS.FSServiceContract.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSServiceContract.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.FSServiceContract.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.Objects.FS.FSServiceContract.FSContractActionCollection -> Collection(PX.Objects.FS.FSContractAction)
PX.Objects.FS.FSServiceContract.FSContractPeriodCollection -> Collection(PX.Objects.FS.FSContractPeriod)
PX.Objects.FS.FSServiceContract.FSContractPostDocCollection -> Collection(PX.Objects.FS.FSContractPostDoc)
PX.Objects.FS.FSServiceContract.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.FS.FSServiceContract.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.FS.FSServiceContract.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.FS.FSServiceContract.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.FS.FSServiceContract.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)

# PX.Objects.FS.FSServiceEquipmentType (EntityType)

Key: EquipmentTypeID, ServiceID
Entity sets: PX_Objects_FS_FSServiceEquipmentType

PX.Objects.FS.FSServiceEquipmentType.ServiceID : Edm.Int32 [key]
PX.Objects.FS.FSServiceEquipmentType.EquipmentTypeID : Edm.Int32 [key] "Equipment Type ID"
PX.Objects.FS.FSServiceEquipmentType.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceEquipmentType.CreatedByScreenID : Edm.String
PX.Objects.FS.FSServiceEquipmentType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceEquipmentType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceEquipmentType.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSServiceEquipmentType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceEquipmentType.tstamp : Edm.Binary
PX.Objects.FS.FSServiceEquipmentType.InventoryItemByServiceID -> PX.Objects.IN.InventoryItem (ServiceID=InventoryID)
PX.Objects.FS.FSServiceEquipmentType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceEquipmentType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSServiceEquipmentType.FSEquipmentTypeByEquipmentTypeID -> PX.Objects.FS.FSEquipmentType (EquipmentTypeID=EquipmentTypeID)

# PX.Objects.FS.FSServiceInventoryItem (EntityType)

Key: InventoryID, ServiceID
Entity sets: PX_Objects_FS_FSServiceInventoryItem

PX.Objects.FS.FSServiceInventoryItem.ServiceID : Edm.Int32 [key]
PX.Objects.FS.FSServiceInventoryItem.InventoryID : Edm.Int32 [key] "Pickup/Delivery Item ID"
PX.Objects.FS.FSServiceInventoryItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceInventoryItem.CreatedByScreenID : Edm.String
PX.Objects.FS.FSServiceInventoryItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceInventoryItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceInventoryItem.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSServiceInventoryItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceInventoryItem.tstamp : Edm.Binary
PX.Objects.FS.FSServiceInventoryItem.InventoryItemByServiceID -> PX.Objects.IN.InventoryItem (ServiceID=InventoryID)
PX.Objects.FS.FSServiceInventoryItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSServiceInventoryItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceInventoryItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSServiceLicenseType (EntityType)

Label: "Service - License Type"
Key: LicenseTypeID, ServiceID
Entity sets: PX_Objects_FS_FSServiceLicenseType, ServiceLicenseType, FSServiceLicenseType

PX.Objects.FS.FSServiceLicenseType.ServiceID : Edm.Int32 [key]
PX.Objects.FS.FSServiceLicenseType.LicenseTypeID : Edm.Int32 [key] "License Type ID"
PX.Objects.FS.FSServiceLicenseType.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSServiceLicenseType.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSServiceLicenseType.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSServiceLicenseType.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSServiceLicenseType.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSServiceLicenseType.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSServiceLicenseType.tstamp : Edm.Binary
PX.Objects.FS.FSServiceLicenseType.InventoryItemByServiceID -> PX.Objects.IN.InventoryItem (ServiceID=InventoryID)
PX.Objects.FS.FSServiceLicenseType.FSLicenseTypeByLicenseTypeID -> PX.Objects.SV.FSLicenseType (LicenseTypeID=LicenseTypeID)
PX.Objects.FS.FSServiceLicenseType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceLicenseType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSServiceOrder (EntityType)

Label: "Service Order"
Key: RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSServiceOrder, ServiceOrder, FSServiceOrder
Non-filterable, non-selectable: UserConfirmedClosing, UserConfirmedUnclosing, ProcessReopenAction, ProcessCompleteAction, CompleteAppointments, ProcessCloseAction, CloseAppointments, ProcessCancelAction, CancelAppointments, CompleteActionRunning, CancelActionRunning, ReopenActionRunning, CloseActionRunning, UnCloseActionRunning, NoteText, CuryAppointmentTaxTotal, AppointmentTaxTotal, CuryAppointmentDocTotal, AppointmentDocTotal, CuryEffectiveBillableLineTotal, EffectiveBillableLineTotal, CuryEffectiveLogBillableTranAmountTotal, EffectiveLogBillableTranAmountTotal, CuryEffectiveBillableTaxTotal, EffectiveBillableTaxTotal, CuryEffectiveBillableDocTotal, EffectiveBillableDocTotal, CuryShortLabelEffectiveBillableDocTotal, ShortLabelEffectiveBillableDocTotal, CuryEffectiveCostTotal, EffectiveCostTotal, SOCuryUnpaidBalanace, SOUnpaidBalanace, SOCuryBillableUnpaidBalanace, SOBillableUnpaidBalanace, SOPrepaymentReceived, SOPrepaymentRemaining, SOPrepaymentApplied, ReportLocationID, AppointmentsCompletedCntr, AppointmentsCompletedOrClosedCntr, MemRefNbr, MemAcctName, IsPrepaymentEnable, ShowInvoicesTab, SourceReferenceNbr, CanCreatePurchaseOrder, SLARemaining, CustomerDisplayName, ContactName, ContactPhone, ContactEmail, AssignedEmployeeDisplayName, ServicesRemaining, ServicesCount, BranchLocationDesc, TreeID, Text, Leaf, CustomOrderDate, SkipExternalTaxCalculation, CuryLineDocDiscountTotal, CuryDocDisc, DocDisc, ProfitPercent, ProfitMarginPercent, IsCalledFromQuickProcess, FormCaptionDescription, IsINReleaseProcess, CuryEstimatedBillableTotal, EstimatedBillableTotal, CuryRate

PX.Objects.FS.FSServiceOrder.SrvOrdType : Edm.String [key] "Order Type"
PX.Objects.FS.FSServiceOrder.RefNbr : Edm.String [key] "Order Nbr."
PX.Objects.FS.FSServiceOrder.SOID : Edm.Int32
PX.Objects.FS.FSServiceOrder.WorkflowTypeID : Edm.String "Workflow Type"
PX.Objects.FS.FSServiceOrder.ServiceOrderAddressID : Edm.Int32
PX.Objects.FS.FSServiceOrder.ServiceOrderContactID : Edm.Int32
PX.Objects.FS.FSServiceOrder.AllowOverrideContactAddress : Edm.Boolean "Override"
PX.Objects.FS.FSServiceOrder.AllowInvoice : Edm.Boolean [required] "Allow Billing"
PX.Objects.FS.FSServiceOrder.AssignedEmpID : Edm.Int32 "Supervisor"
PX.Objects.FS.FSServiceOrder.AutoDocDesc : Edm.String "Service description"
PX.Objects.FS.FSServiceOrder.CustomerID : Edm.Int32 "Customer"
PX.Objects.FS.FSServiceOrder.BillCustomerID : Edm.Int32 "Billing Customer"
PX.Objects.FS.FSServiceOrder.DocDesc : Edm.String "Description"
PX.Objects.FS.FSServiceOrder.ContactID : Edm.Int32 "Contact"
PX.Objects.FS.FSServiceOrder.ContractID : Edm.Int32 "Contract"
PX.Objects.FS.FSServiceOrder.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSServiceOrder.BranchLocationID : Edm.Int32 "Branch Location"
PX.Objects.FS.FSServiceOrder.RoomID : Edm.String "Room"
PX.Objects.FS.FSServiceOrder.OrderDate : Edm.DateTimeOffset "Date"
PX.Objects.FS.FSServiceOrder.UserConfirmedClosing : Edm.Boolean
PX.Objects.FS.FSServiceOrder.UserConfirmedUnclosing : Edm.Boolean
PX.Objects.FS.FSServiceOrder.Copied : Edm.Boolean [required] "Copied"
PX.Objects.FS.FSServiceOrder.Confirmed : Edm.Boolean [required] "Confirmed"
PX.Objects.FS.FSServiceOrder.OpenDoc : Edm.Boolean [required] "Open"
PX.Objects.FS.FSServiceOrder.ProcessReopenAction : Edm.Boolean
PX.Objects.FS.FSServiceOrder.Hold : Edm.Boolean [required] "Hold"
PX.Objects.FS.FSServiceOrder.Awaiting : Edm.Boolean [required] "Awaiting"
PX.Objects.FS.FSServiceOrder.Completed : Edm.Boolean [required] "Completed"
PX.Objects.FS.FSServiceOrder.ProcessCompleteAction : Edm.Boolean
PX.Objects.FS.FSServiceOrder.CompleteAppointments : Edm.Boolean
PX.Objects.FS.FSServiceOrder.Closed : Edm.Boolean [required] "Closed"
PX.Objects.FS.FSServiceOrder.ProcessCloseAction : Edm.Boolean
PX.Objects.FS.FSServiceOrder.CloseAppointments : Edm.Boolean
PX.Objects.FS.FSServiceOrder.Canceled : Edm.Boolean [required] "Canceled"
PX.Objects.FS.FSServiceOrder.ProcessCancelAction : Edm.Boolean
PX.Objects.FS.FSServiceOrder.CancelAppointments : Edm.Boolean
PX.Objects.FS.FSServiceOrder.Billed : Edm.Boolean [required] "Billed"
PX.Objects.FS.FSServiceOrder.BillingBy : Edm.String "Billing By"
PX.Objects.FS.FSServiceOrder.BillOnlyCompletedClosed : Edm.Boolean "Bill Only Completed or Closed Service Orders"
PX.Objects.FS.FSServiceOrder.CompleteActionRunning : Edm.Boolean
PX.Objects.FS.FSServiceOrder.CancelActionRunning : Edm.Boolean
PX.Objects.FS.FSServiceOrder.ReopenActionRunning : Edm.Boolean
PX.Objects.FS.FSServiceOrder.CloseActionRunning : Edm.Boolean
PX.Objects.FS.FSServiceOrder.UnCloseActionRunning : Edm.Boolean
PX.Objects.FS.FSServiceOrder.Status : Edm.String "Status"
PX.Objects.FS.FSServiceOrder.WFStageID : Edm.Int32 "Workflow Stage"
PX.Objects.FS.FSServiceOrder.CuryID : Edm.String "Currency"
PX.Objects.FS.FSServiceOrder.CuryInfoID : Edm.Int64
PX.Objects.FS.FSServiceOrder.EstimatedDurationTotal : Edm.Int32 [required] "Estimated Duration"
PX.Objects.FS.FSServiceOrder.LongDescr : Edm.String "Description"
PX.Objects.FS.FSServiceOrder.EstimatedOrderTotal : Edm.Decimal "Base Ext. Price Total"
PX.Objects.FS.FSServiceOrder.CuryEstimatedOrderTotal : Edm.Decimal "Ext. Price Total"
PX.Objects.FS.FSServiceOrder.BillableOrderTotal : Edm.Decimal "Base Estimated Billable Total"
PX.Objects.FS.FSServiceOrder.CuryBillableOrderTotal : Edm.Decimal "Estimated Billable Total"
PX.Objects.FS.FSServiceOrder.Priority : Edm.String "Priority"
PX.Objects.FS.FSServiceOrder.ProblemID : Edm.Int32 "Problem"
PX.Objects.FS.FSServiceOrder.Severity : Edm.String "Severity"
PX.Objects.FS.FSServiceOrder.SLAETA : Edm.DateTimeOffset "SLA"
PX.Objects.FS.FSServiceOrder.SourceDocType : Edm.String "Source Document Type"
PX.Objects.FS.FSServiceOrder.SourceID : Edm.Int32
PX.Objects.FS.FSServiceOrder.SourceRefNbr : Edm.String "Source Ref. Nbr."
PX.Objects.FS.FSServiceOrder.SourceType : Edm.String "Document Type"
PX.Objects.FS.FSServiceOrder.NoteID : Edm.Guid
PX.Objects.FS.FSServiceOrder.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSServiceOrder.LineCntr : Edm.Int32 [required]
PX.Objects.FS.FSServiceOrder.SplitLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSServiceOrder.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceOrder.CreatedByScreenID : Edm.String "Created By Screen ID"
PX.Objects.FS.FSServiceOrder.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSServiceOrder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceOrder.LastModifiedByScreenID : Edm.String "Last Modified By Screen ID"
PX.Objects.FS.FSServiceOrder.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSServiceOrder.tstamp : Edm.Binary
PX.Objects.FS.FSServiceOrder.BAccountRequired : Edm.Boolean "Customer Required"
PX.Objects.FS.FSServiceOrder.Quote : Edm.Boolean [required] "Quote"
PX.Objects.FS.FSServiceOrder.FinPeriodID : Edm.String "Post Period"
PX.Objects.FS.FSServiceOrder.GenerationID : Edm.Int32 "Generation ID"
PX.Objects.FS.FSServiceOrder.CustWorkOrderRefNbr : Edm.String "External Reference"
PX.Objects.FS.FSServiceOrder.CustPORefNbr : Edm.String "Customer Order"
PX.Objects.FS.FSServiceOrder.ServiceCount : Edm.Int32 "Service Count"
PX.Objects.FS.FSServiceOrder.ScheduledServiceCount : Edm.Int32 "Scheduled Service Count"
PX.Objects.FS.FSServiceOrder.CompleteServiceCount : Edm.Int32 "Complete Service Count"
PX.Objects.FS.FSServiceOrder.PostedBy : Edm.String
PX.Objects.FS.FSServiceOrder.PendingAPARSOPost : Edm.Boolean [required]
PX.Objects.FS.FSServiceOrder.PendingINPost : Edm.Boolean [required]
PX.Objects.FS.FSServiceOrder.CBID : Edm.Int32
PX.Objects.FS.FSServiceOrder.SalesPersonID : Edm.Int32 "Salesperson"
PX.Objects.FS.FSServiceOrder.Commissionable : Edm.Boolean "Commissionable"
PX.Objects.FS.FSServiceOrder.CutOffDate : Edm.DateTimeOffset "Cut-Off Date"
PX.Objects.FS.FSServiceOrder.ApptDurationTotal : Edm.Int32 [required] "Appointment Duration"
PX.Objects.FS.FSServiceOrder.CuryApptOrderTotal : Edm.Decimal "Actual Billable Total"
PX.Objects.FS.FSServiceOrder.ApptOrderTotal : Edm.Decimal "Base Appointment Line Total"
PX.Objects.FS.FSServiceOrder.CuryAppointmentTaxTotal : Edm.Decimal "Actual Tax Total"
PX.Objects.FS.FSServiceOrder.AppointmentTaxTotal : Edm.Decimal "Base Appointment Tax Total"
PX.Objects.FS.FSServiceOrder.CuryAppointmentDocTotal : Edm.Decimal "Invoice Total"
PX.Objects.FS.FSServiceOrder.AppointmentDocTotal : Edm.Decimal "Base Invoice Total"
PX.Objects.FS.FSServiceOrder.BillContractPeriodID : Edm.Int32 "Contract Period"
PX.Objects.FS.FSServiceOrder.CuryEffectiveBillableLineTotal : Edm.Decimal "Line Total"
PX.Objects.FS.FSServiceOrder.EffectiveBillableLineTotal : Edm.Decimal
PX.Objects.FS.FSServiceOrder.CuryEffectiveLogBillableTranAmountTotal : Edm.Decimal "Billable Labor Total"
PX.Objects.FS.FSServiceOrder.EffectiveLogBillableTranAmountTotal : Edm.Decimal
PX.Objects.FS.FSServiceOrder.CuryEffectiveBillableTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.FS.FSServiceOrder.EffectiveBillableTaxTotal : Edm.Decimal
PX.Objects.FS.FSServiceOrder.CuryEffectiveBillableDocTotal : Edm.Decimal "Invoice Total"
PX.Objects.FS.FSServiceOrder.EffectiveBillableDocTotal : Edm.Decimal
PX.Objects.FS.FSServiceOrder.CuryShortLabelEffectiveBillableDocTotal : Edm.Decimal "Billable Total"
PX.Objects.FS.FSServiceOrder.ShortLabelEffectiveBillableDocTotal : Edm.Decimal
PX.Objects.FS.FSServiceOrder.CuryEffectiveCostTotal : Edm.Decimal "Cost Total"
PX.Objects.FS.FSServiceOrder.EffectiveCostTotal : Edm.Decimal
PX.Objects.FS.FSServiceOrder.SOCuryUnpaidBalanace : Edm.Decimal "Service Order Unpaid Balance"
PX.Objects.FS.FSServiceOrder.SOUnpaidBalanace : Edm.Decimal
PX.Objects.FS.FSServiceOrder.SOCuryBillableUnpaidBalanace : Edm.Decimal "Service Order Billable Unpaid Balance"
PX.Objects.FS.FSServiceOrder.SOBillableUnpaidBalanace : Edm.Decimal
PX.Objects.FS.FSServiceOrder.SOPrepaymentReceived : Edm.Decimal "Prepayment Received"
PX.Objects.FS.FSServiceOrder.SOPrepaymentRemaining : Edm.Decimal "Prepayment Remaining"
PX.Objects.FS.FSServiceOrder.SOPrepaymentApplied : Edm.Decimal "Prepayment Applied"
PX.Objects.FS.FSServiceOrder.AppointmentsNeeded : Edm.Boolean "Appointments Needed"
PX.Objects.FS.FSServiceOrder.MaxLineNbr : Edm.Int32
PX.Objects.FS.FSServiceOrder.ApptNeededLineCntr : Edm.Int32
PX.Objects.FS.FSServiceOrder.PendingPOLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSServiceOrder.APBillLineCntr : Edm.Int32 [required]
PX.Objects.FS.FSServiceOrder.ReportLocationID : Edm.Int32
PX.Objects.FS.FSServiceOrder.InvoicedByContract : Edm.Boolean "InvoicedByContract"
PX.Objects.FS.FSServiceOrder.AppointmentsCompletedCntr : Edm.Int32
PX.Objects.FS.FSServiceOrder.AppointmentsCompletedOrClosedCntr : Edm.Int32
PX.Objects.FS.FSServiceOrder.MemRefNbr : Edm.String
PX.Objects.FS.FSServiceOrder.MemAcctName : Edm.String
PX.Objects.FS.FSServiceOrder.IsPrepaymentEnable : Edm.Boolean "IsPrepaymentEnable"
PX.Objects.FS.FSServiceOrder.ShowInvoicesTab : Edm.Boolean "ShowInvoicesTab"
PX.Objects.FS.FSServiceOrder.SourceReferenceNbr : Edm.String "Reference Nbr."
PX.Objects.FS.FSServiceOrder.CanCreatePurchaseOrder : Edm.Boolean
PX.Objects.FS.FSServiceOrder.SLARemaining : Edm.Int32
PX.Objects.FS.FSServiceOrder.CustomerDisplayName : Edm.String
PX.Objects.FS.FSServiceOrder.ContactName : Edm.String
PX.Objects.FS.FSServiceOrder.ContactPhone : Edm.String
PX.Objects.FS.FSServiceOrder.ContactEmail : Edm.String
PX.Objects.FS.FSServiceOrder.AssignedEmployeeDisplayName : Edm.String
PX.Objects.FS.FSServiceOrder.ServicesRemaining : Edm.Int32
PX.Objects.FS.FSServiceOrder.ServicesCount : Edm.Int32
PX.Objects.FS.FSServiceOrder.BranchLocationDesc : Edm.String
PX.Objects.FS.FSServiceOrder.TreeID : Edm.Int32
PX.Objects.FS.FSServiceOrder.Text : Edm.String
PX.Objects.FS.FSServiceOrder.Leaf : Edm.Boolean
PX.Objects.FS.FSServiceOrder.CustomOrderDate : Edm.String
PX.Objects.FS.FSServiceOrder.SLAETAUTC : Edm.DateTimeOffset "Deadline - SLA"
PX.Objects.FS.FSServiceOrder.TaxZoneID : Edm.String "Customer Tax Zone"
PX.Objects.FS.FSServiceOrder.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.FS.FSServiceOrder.CuryVatExemptTotal : Edm.Decimal [required] "VAT Exempt Total"
PX.Objects.FS.FSServiceOrder.VatExemptTotal : Edm.Decimal [required]
PX.Objects.FS.FSServiceOrder.CuryVatTaxableTotal : Edm.Decimal [required] "VAT Taxable Total"
PX.Objects.FS.FSServiceOrder.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.FS.FSServiceOrder.CuryTaxTotal : Edm.Decimal [required] "Estimated Tax Total"
PX.Objects.FS.FSServiceOrder.TaxTotal : Edm.Decimal [required]
PX.Objects.FS.FSServiceOrder.SkipExternalTaxCalculation : Edm.Boolean "Skip External Tax Calculation"
PX.Objects.FS.FSServiceOrder.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.FS.FSServiceOrder.CuryLineDocDiscountTotal : Edm.Decimal "CuryLineDocDiscountTotal"
PX.Objects.FS.FSServiceOrder.CuryDocDisc : Edm.Decimal "Document Discount"
PX.Objects.FS.FSServiceOrder.DocDisc : Edm.Decimal
PX.Objects.FS.FSServiceOrder.CuryDiscTot : Edm.Decimal [required] "Discount Total"
PX.Objects.FS.FSServiceOrder.DiscTot : Edm.Decimal [required] "Discount Total"
PX.Objects.FS.FSServiceOrder.CuryDocTotal : Edm.Decimal [required] "Estimated Total"
PX.Objects.FS.FSServiceOrder.DocTotal : Edm.Decimal "Base Service Order Total"
PX.Objects.FS.FSServiceOrder.CuryCostTotal : Edm.Decimal [required] "Cost Total"
PX.Objects.FS.FSServiceOrder.CostTotal : Edm.Decimal [required]
PX.Objects.FS.FSServiceOrder.ProfitPercent : Edm.Decimal "Profit Markup (%)"
PX.Objects.FS.FSServiceOrder.ProfitMarginPercent : Edm.Decimal "Profit Margin (%)"
PX.Objects.FS.FSServiceOrder.IsCalledFromQuickProcess : Edm.Boolean
PX.Objects.FS.FSServiceOrder.FormCaptionDescription : Edm.String
PX.Objects.FS.FSServiceOrder.IsINReleaseProcess : Edm.Boolean
PX.Objects.FS.FSServiceOrder.CuryEstimatedBillableTotal : Edm.Decimal "Estimated Billable Total"
PX.Objects.FS.FSServiceOrder.EstimatedBillableTotal : Edm.Decimal "Estimated Billable Total"
PX.Objects.FS.FSServiceOrder.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.FS.FSServiceOrder.EntityUsageType : Edm.String "Tax Exemption Type"
PX.Objects.FS.FSServiceOrder.CuryRate : Edm.Decimal
PX.Objects.FS.FSServiceOrder.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.FS.FSServiceOrder.PMTaskByDfltProjectTaskID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSServiceOrder.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.FS.FSServiceOrder.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.FS.FSServiceOrder.ContractByLocationID -> PX.Objects.CT.Contract (ContractID=ContractID, CustomerID=CustomerID)
PX.Objects.FS.FSServiceOrder.BAccountByAssignedEmpID -> PX.Objects.CR.BAccount (AssignedEmpID=BAccountID)
PX.Objects.FS.FSServiceOrder.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.FS.FSServiceOrder.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSServiceOrder.CustomerByBillCustomerID -> PX.Objects.AR.Customer (BillCustomerID=BAccountID)
PX.Objects.FS.FSServiceOrder.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.FS.FSServiceOrder.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule
PX.Objects.FS.FSServiceOrder.FSScheduleByServiceContractID -> PX.Objects.FS.FSSchedule
PX.Objects.FS.FSServiceOrder.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSServiceOrder.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSServiceOrder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceOrder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSServiceOrder.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.FS.FSServiceOrder.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.FS.FSServiceOrder.LocationByLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.FSServiceOrder.LocationByBillLocationID -> PX.Objects.CR.Location (BillCustomerID=BAccountID)
PX.Objects.FS.FSServiceOrder.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.FSServiceOrder.LocationByBillCustomerID -> PX.Objects.CR.Location (BillCustomerID=BAccountID)
PX.Objects.FS.FSServiceOrder.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.FS.FSServiceOrder.FSAddressByServiceOrderAddressID -> PX.Objects.FS.FSAddress (ServiceOrderAddressID=AddressID)
PX.Objects.FS.FSServiceOrder.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.FSServiceOrder.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.FSServiceOrder.FSContactByServiceOrderContactID -> PX.Objects.FS.FSContact (ServiceOrderContactID=ContactID)
PX.Objects.FS.FSServiceOrder.FSCustomerBillingSetupByCBID -> PX.Objects.FS.FSCustomerBillingSetup (CBID=CBID)
PX.Objects.FS.FSServiceOrder.FSProblemByProblemID -> PX.Objects.FS.FSProblem (ProblemID=ProblemCD)
PX.Objects.FS.FSServiceOrder.FSRoomByRoomID -> PX.Objects.FS.FSRoom (BranchLocationID=BranchLocationID, RoomID=RoomID)
PX.Objects.FS.FSServiceOrder.FSRoomByBranchLocationID -> PX.Objects.FS.FSRoom (RoomID=RoomID, BranchLocationID=BranchLocationID)
PX.Objects.FS.FSServiceOrder.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract
PX.Objects.FS.FSServiceOrder.FSServiceContractByBillServiceContractID -> PX.Objects.FS.FSServiceContract
PX.Objects.FS.FSServiceOrder.FSServiceContractByCustomerID -> PX.Objects.FS.FSServiceContract (CustomerID=CustomerID)
PX.Objects.FS.FSServiceOrder.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSServiceOrder.FSWFStageByWFStageID -> PX.Objects.FS.FSWFStage (WFStageID=WFStageID)
PX.Objects.FS.FSServiceOrder.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.FS.FSServiceOrder.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSServiceOrder.FSServiceOrderTaxTranCollection -> Collection(PX.Objects.FS.FSServiceOrderTaxTran)
PX.Objects.FS.FSServiceOrder.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.FSServiceOrder.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.FSServiceOrder.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.FS.FSServiceOrder.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.FSServiceOrder.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.FS.FSServiceOrder.FSAdjustCollection -> Collection(PX.Objects.FS.FSAdjust)
PX.Objects.FS.FSServiceOrder.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.Objects.FS.FSServiceOrder.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.FSServiceOrder.FSPostDocCollection -> Collection(PX.Objects.FS.FSPostDoc)
PX.Objects.FS.FSServiceOrder.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.FS.FSServiceOrder.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.FS.FSServiceOrder.FSSOEmployeeCollection -> Collection(PX.Objects.FS.FSSOEmployee)
PX.Objects.FS.FSServiceOrder.FSSOResourceCollection -> Collection(PX.Objects.FS.FSSOResource)
PX.Objects.FS.FSServiceOrder.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.FSServiceOrder.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.FS.FSServiceOrder.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.FS.FSServiceOrder.SchedulerAppointmentCollection -> Collection(PX.Objects.FS.SchedulerAppointment)

# PX.Objects.FS.FSServiceOrderDiscountDetail (EntityType)

BaseType: PX.Objects.FS.FSDiscountDetail
Key: EntityType, RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSDiscountDetail)
Entity sets: PX_Objects_FS_FSServiceOrderDiscountDetail

# PX.Objects.FS.FSServiceOrderTax (EntityType)

Label: "Service Order Tax"
Key: LineNbr, RefNbr, SrvOrdType, TaxID
Entity sets: PX_Objects_FS_FSServiceOrderTax, ServiceOrderTax, FSServiceOrderTax
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt

PX.Objects.FS.FSServiceOrderTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.FS.FSServiceOrderTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.FS.FSServiceOrderTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.FS.FSServiceOrderTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.FS.FSServiceOrderTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceOrderTax.CreatedByScreenID : Edm.String
PX.Objects.FS.FSServiceOrderTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceOrderTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceOrderTax.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSServiceOrderTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceOrderTax.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSServiceOrderTax.RefNbr : Edm.String [key] "Service Order Nbr."
PX.Objects.FS.FSServiceOrderTax.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.FS.FSServiceOrderTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.FS.FSServiceOrderTax.CuryInfoID : Edm.Int64
PX.Objects.FS.FSServiceOrderTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.FS.FSServiceOrderTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.FS.FSServiceOrderTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.FS.FSServiceOrderTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.FS.FSServiceOrderTax.tstamp : Edm.Binary
PX.Objects.FS.FSServiceOrderTax.FSSODetByLineNbr -> PX.Objects.FS.FSSODet (SrvOrdType=SrvOrdType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.FS.FSServiceOrderTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSServiceOrderTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceOrderTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSServiceOrderTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.FS.FSServiceOrderTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.FS.FSServiceOrderTax.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSServiceOrderTax.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSServiceOrderTaxTran (EntityType)

Label: "Service Order Tax Detail"
Key: RecordID, RefNbr, SrvOrdType, TaxID
Entity sets: PX_Objects_FS_FSServiceOrderTaxTran, ServiceOrderTaxDetail, FSServiceOrderTaxTran
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt, TaxZoneID

PX.Objects.FS.FSServiceOrderTaxTran.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.FS.FSServiceOrderTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.FS.FSServiceOrderTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.FS.FSServiceOrderTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.FS.FSServiceOrderTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceOrderTaxTran.CreatedByScreenID : Edm.String
PX.Objects.FS.FSServiceOrderTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceOrderTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceOrderTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSServiceOrderTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceOrderTaxTran.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSServiceOrderTaxTran.RefNbr : Edm.String [key] "Service Order Nbr."
PX.Objects.FS.FSServiceOrderTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.FS.FSServiceOrderTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.FS.FSServiceOrderTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.FS.FSServiceOrderTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.FS.FSServiceOrderTaxTran.CuryInfoID : Edm.Int64
PX.Objects.FS.FSServiceOrderTaxTran.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.FS.FSServiceOrderTaxTran.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.FS.FSServiceOrderTaxTran.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.FS.FSServiceOrderTaxTran.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.FS.FSServiceOrderTaxTran.TaxZoneID : Edm.String
PX.Objects.FS.FSServiceOrderTaxTran.tstamp : Edm.Binary
PX.Objects.FS.FSServiceOrderTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.FS.FSServiceOrderTaxTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSServiceOrderTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceOrderTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSServiceOrderTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.FS.FSServiceOrderTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.FS.FSServiceOrderTaxTran.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSServiceOrderTaxTran.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSServiceSkill (EntityType)

Key: ServiceID, SkillID
Entity sets: PX_Objects_FS_FSServiceSkill

PX.Objects.FS.FSServiceSkill.ServiceID : Edm.Int32 [key] "Service ID"
PX.Objects.FS.FSServiceSkill.SkillID : Edm.Int32 [key] "Skill ID"
PX.Objects.FS.FSServiceSkill.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceSkill.CreatedByScreenID : Edm.String "Created By ScreenID"
PX.Objects.FS.FSServiceSkill.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSServiceSkill.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceSkill.LastModifiedByScreenID : Edm.String "Last Modified By ScreenID"
PX.Objects.FS.FSServiceSkill.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSServiceSkill.tstamp : Edm.Binary
PX.Objects.FS.FSServiceSkill.InventoryItemByServiceID -> PX.Objects.IN.InventoryItem (ServiceID=InventoryID)
PX.Objects.FS.FSServiceSkill.FSSkillBySkillID -> PX.Objects.SV.FSSkill (SkillID=SkillID)
PX.Objects.FS.FSServiceSkill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceSkill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSServiceTemplate (EntityType)

Key: ServiceTemplateCD
Entity sets: PX_Objects_FS_FSServiceTemplate
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSServiceTemplate.ServiceTemplateID : Edm.Int32 "ServiceTemplateID"
PX.Objects.FS.FSServiceTemplate.ServiceTemplateCD : Edm.String [key] "Service Template ID"
PX.Objects.FS.FSServiceTemplate.Descr : Edm.String "Description"
PX.Objects.FS.FSServiceTemplate.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSServiceTemplate.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSServiceTemplate.SrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSServiceTemplate.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceTemplate.CreatedByScreenID : Edm.String
PX.Objects.FS.FSServiceTemplate.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSServiceTemplate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceTemplate.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSServiceTemplate.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSServiceTemplate.tstamp : Edm.Binary
PX.Objects.FS.FSServiceTemplate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceTemplate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSServiceTemplate.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSServiceTemplate.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.FS.FSServiceTemplate.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)

# PX.Objects.FS.FSServiceTemplateDet (EntityType)

Label: "FSServiceTemplateDet"
Key: ServiceTemplateDetID, ServiceTemplateID
Entity sets: PX_Objects_FS_FSServiceTemplateDet, FSServiceTemplateDet

PX.Objects.FS.FSServiceTemplateDet.ServiceTemplateID : Edm.Int32 [key] "Service Template ID"
PX.Objects.FS.FSServiceTemplateDet.ServiceTemplateDetID : Edm.Int32 [key] "ServiceTemplateDetID"
PX.Objects.FS.FSServiceTemplateDet.LineType : Edm.String "Line Type"
PX.Objects.FS.FSServiceTemplateDet.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSServiceTemplateDet.UOM : Edm.String "UOM"
PX.Objects.FS.FSServiceTemplateDet.Qty : Edm.Decimal "Quantity"
PX.Objects.FS.FSServiceTemplateDet.TranDesc : Edm.String "Transaction Description"
PX.Objects.FS.FSServiceTemplateDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceTemplateDet.CreatedByScreenID : Edm.String
PX.Objects.FS.FSServiceTemplateDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceTemplateDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceTemplateDet.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSServiceTemplateDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceTemplateDet.tstamp : Edm.Binary
PX.Objects.FS.FSServiceTemplateDet.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSServiceTemplateDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceTemplateDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSServiceTemplateDet.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.FS.FSServiceTemplateDet.FSServiceTemplateByServiceTemplateID -> PX.Objects.FS.FSServiceTemplate (ServiceTemplateID=ServiceTemplateID)

# PX.Objects.FS.FSServiceVehicleType (EntityType)

Key: ServiceID, VehicleTypeID
Entity sets: PX_Objects_FS_FSServiceVehicleType

PX.Objects.FS.FSServiceVehicleType.ServiceID : Edm.Int32 [key]
PX.Objects.FS.FSServiceVehicleType.VehicleTypeID : Edm.Int32 [key] "Vehicle Type ID"
PX.Objects.FS.FSServiceVehicleType.PriorityPreference : Edm.Int32 [required] "Priority Preference"
PX.Objects.FS.FSServiceVehicleType.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSServiceVehicleType.CreatedByScreenID : Edm.String
PX.Objects.FS.FSServiceVehicleType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceVehicleType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSServiceVehicleType.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSServiceVehicleType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSServiceVehicleType.tstamp : Edm.Binary
PX.Objects.FS.FSServiceVehicleType.InventoryItemByServiceID -> PX.Objects.IN.InventoryItem (ServiceID=InventoryID)
PX.Objects.FS.FSServiceVehicleType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSServiceVehicleType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSServiceVehicleType.FSVehicleTypeByVehicleTypeID -> PX.Objects.FS.FSVehicleType (VehicleTypeID=VehicleTypeID)

# PX.Objects.FS.FSSetup (EntityType)

Label: "Service Management Preferences"
Singletons: PX_Objects_FS_FSSetup, ServiceManagementPreferences, FSSetup

PX.Objects.FS.FSSetup.AppAutoConfirmGap : Edm.Int32 [required] "Appointment Auto-Confirm Time"
PX.Objects.FS.FSSetup.AppResizePrecision : Edm.Int32 [required] "Appointment Resize Precision"
PX.Objects.FS.FSSetup.CalendarID : Edm.String "Work Calendar"
PX.Objects.FS.FSSetup.ShowServiceOrderDaysGap : Edm.Int32 "Show Service Orders in a Period Of"
PX.Objects.FS.FSSetup.DenyWarnByGeoZone : Edm.String "Service Areas"
PX.Objects.FS.FSSetup.DenyWarnByLicense : Edm.String "Licenses"
PX.Objects.FS.FSSetup.DenyWarnBySkill : Edm.String "Skills"
PX.Objects.FS.FSSetup.DfltAppContactInfoSource : Edm.String "Default Appointment Contact Info Source"
PX.Objects.FS.FSSetup.EmpSchedulePrecision : Edm.Int32 "Employee Schedule Precision"
PX.Objects.FS.FSSetup.InitialAppRefNbr : Edm.String "Initial Appointment Ref. Nbr."
PX.Objects.FS.FSSetup.DfltBusinessAcctType : Edm.String "Default Business Account Type"
PX.Objects.FS.FSSetup.DfltSrvOrdType : Edm.String "Default Service Order Type"
PX.Objects.FS.FSSetup.DfltSOSrvOrdType : Edm.String "Default Service Order Type for Sales Orders"
PX.Objects.FS.FSSetup.DfltCalendarViewMode : Edm.String "View Mode"
PX.Objects.FS.FSSetup.DfltCalendarPageSize : Edm.Int32 "Number of Staff Members"
PX.Objects.FS.FSSetup.DfltCasesSrvOrdType : Edm.String "Default Service Order Type for Cases"
PX.Objects.FS.FSSetup.DfltOpportunitySrvOrdType : Edm.String "Default Opportunities Service Order Type"
PX.Objects.FS.FSSetup.DaysAheadRecurringAppointments : Edm.Int32 [required] "Number of days ahead for recurring appointments"
PX.Objects.FS.FSSetup.DenyWarnByEquipment : Edm.String "Equipments"
PX.Objects.FS.FSSetup.EmpSchdlNumberingID : Edm.String "Staff Schedule Numbering Sequence"
PX.Objects.FS.FSSetup.LicenseNumberingID : Edm.String "License Numbering Sequence"
PX.Objects.FS.FSSetup.EquipmentNumberingID : Edm.String "Equipment Numbering Sequence"
PX.Objects.FS.FSSetup.DenyWarnByAppOverlap : Edm.String "Overlapping Appointments"
PX.Objects.FS.FSSetup.ManageRooms : Edm.Boolean "Enable Rooms"
PX.Objects.FS.FSSetup.DfltBranchID : Edm.Int32
PX.Objects.FS.FSSetup.EnableEmpTimeCardIntegration : Edm.Boolean [required] "Enable Time & Expenses Integration"
PX.Objects.FS.FSSetup.PostBatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.FS.FSSetup.ScheduleNumberingID : Edm.String "Service Contract Schedule Numbering Sequence"
PX.Objects.FS.FSSetup.ServiceContractNumberingID : Edm.String "Service Contract Numbering Sequence"
PX.Objects.FS.FSSetup.CustomerMultipleBillingOptions : Edm.Boolean [required] "Manage Multiple Billing Options per Customer"
PX.Objects.FS.FSSetup.AlertBeforeCloseServiceOrder : Edm.Boolean [required] "Alert About Open Appointments Before Service Orders Are Closed"
PX.Objects.FS.FSSetup.FilterInvoicingManually : Edm.Boolean [required] "Require Manual Filtering on Billing Forms"
PX.Objects.FS.FSSetup.EnableSeasonScheduleContract : Edm.Boolean [required] "Enable Seasons in Schedule Contracts"
PX.Objects.FS.FSSetup.EquipmentCalculateWarrantyFrom : Edm.String "Calculate Warranty From"
PX.Objects.FS.FSSetup.DfltCalendarStartTime : Edm.DateTimeOffset "Day Start Time"
PX.Objects.FS.FSSetup.DfltCalendarEndTime : Edm.DateTimeOffset "Day End Time"
PX.Objects.FS.FSSetup.TimeRange : Edm.String "Time Range"
PX.Objects.FS.FSSetup.TimeFilter : Edm.String "Time Filter"
PX.Objects.FS.FSSetup.DayResolution : Edm.Int32 [required] "Day Resolution"
PX.Objects.FS.FSSetup.WeekResolution : Edm.Int32 [required] "Week Resolution"
PX.Objects.FS.FSSetup.MonthResolution : Edm.Int32 [required] "Month Resolution"
PX.Objects.FS.FSSetup.MapApiKey : Edm.String "Map API Key"
PX.Objects.FS.FSSetup.TrackAppointmentLocation : Edm.Boolean [required] "Track Start and Completion Appointment Locations"
PX.Objects.FS.FSSetup.EnableGPSTracking : Edm.Boolean [required] "Show Location Tracking"
PX.Objects.FS.FSSetup.GPSRefreshTrackingTime : Edm.Int32 [required] "Refresh GPS Locations Every"
PX.Objects.FS.FSSetup.HistoryDistanceAccuracy : Edm.Int32 [required] "History Distance Accuracy"
PX.Objects.FS.FSSetup.HistoryTimeAccuracy : Edm.Int32 [required] "History Time Accuracy"
PX.Objects.FS.FSSetup.DisableFixScheduleAction : Edm.Boolean [required] "Enable Fix Schedules Without Next Execution Date"
PX.Objects.FS.FSSetup.ContractPostTo : Edm.String "Generated Billing Documents"
PX.Objects.FS.FSSetup.DfltContractTermIDARSO : Edm.String "Default Terms"
PX.Objects.FS.FSSetup.ContractPostOrderType : Edm.String "Order Type for Billing"
PX.Objects.FS.FSSetup.ContractSalesAcctSource : Edm.String "Use Sales Account From"
PX.Objects.FS.FSSetup.EnableContractPeriodWhenInvoice : Edm.Boolean [required] "Automatically Activate Upcoming Period"
PX.Objects.FS.FSSetup.ShowWorkflowStageField : Edm.Boolean [required] "Enable Workflow Stages"
PX.Objects.FS.FSSetup.EnableUnlinkPOAction : Edm.Boolean [required] "Allow PO Unlinking"
PX.Objects.FS.FSSetup.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSSetup.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSSetup.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSSetup.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSSetup.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSSetup.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSSetup.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSSetup.EnableAllTargetEquipment : Edm.Boolean [required] "Enable Service on All Target Equipment"
PX.Objects.FS.FSSetup.EnableDfltStaffOnServiceOrder : Edm.Boolean [required] "Enable Default Staff in Service Orders"
PX.Objects.FS.FSSetup.EnableDfltResEquipOnServiceOrder : Edm.Boolean [required] "Enable Default Resource Equipment in Service Orders"
PX.Objects.FS.FSSetup.ReadyToUpgradeTo2017R2 : Edm.Boolean [required]
PX.Objects.FS.FSSetup.NoteID : Edm.Guid
PX.Objects.FS.FSSetup.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSSetup.CustomDfltCalendarStartTime : Edm.String
PX.Objects.FS.FSSetup.CustomDfltCalendarEndTime : Edm.String
PX.Objects.FS.FSSetup.SOOrderTypeByContractPostOrderType -> PX.Objects.SO.SOOrderType (ContractPostOrderType=OrderType)
PX.Objects.FS.FSSetup.FSSrvOrdTypeByDfltSrvOrdType -> PX.Objects.FS.FSSrvOrdType (DfltSrvOrdType=SrvOrdType)
PX.Objects.FS.FSSetup.FSSrvOrdTypeByDfltSOSrvOrdType -> PX.Objects.FS.FSSrvOrdType (DfltSOSrvOrdType=SrvOrdType)
PX.Objects.FS.FSSetup.FSSrvOrdTypeByDfltCasesSrvOrdType -> PX.Objects.FS.FSSrvOrdType (DfltCasesSrvOrdType=SrvOrdType)
PX.Objects.FS.FSSetup.FSSrvOrdTypeByDfltOpportunitySrvOrdType -> PX.Objects.FS.FSSrvOrdType (DfltOpportunitySrvOrdType=SrvOrdType)

# PX.Objects.FS.FSShippingAddress (EntityType)

Label: "Field Service Shipping Address"
BaseType: PX.Objects.FS.FSAddress
Key: AddressID (inherited from PX.Objects.FS.FSAddress)
Entity sets: PX_Objects_FS_FSShippingAddress, FieldServiceShippingAddress, FSShippingAddress

# PX.Objects.FS.FSShippingContact (EntityType)

Label: "Field Service Shipping Contact"
BaseType: PX.Objects.FS.FSContact
Key: ContactID (inherited from PX.Objects.FS.FSContact)
Entity sets: PX_Objects_FS_FSShippingContact, FieldServiceShippingContact, FSShippingContact

# PX.Objects.FS.FSSiteStatusSelected (EntityType)

Key: InventoryID
Entity sets: PX_Objects_FS_FSSiteStatusSelected
Non-filterable, non-selectable: CuryID, CuryInfoID, QtySelected, DurationSelected, CuryUnitPrice, DropShipCuryUnitPrice, CuryRate, CuryViewState

PX.Objects.FS.FSSiteStatusSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.FS.FSSiteStatusSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.FS.FSSiteStatusSelected.Descr : Edm.String "Description"
PX.Objects.FS.FSSiteStatusSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.FS.FSSiteStatusSelected.ItemClassCD : Edm.String
PX.Objects.FS.FSSiteStatusSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.FS.FSSiteStatusSelected.ItemType : Edm.String "Type"
PX.Objects.FS.FSSiteStatusSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.FS.FSSiteStatusSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.FS.FSSiteStatusSelected.PreferredVendorID : Edm.Int32 "Preferred Vendor ID"
PX.Objects.FS.FSSiteStatusSelected.PreferredVendorDescription : Edm.String "Preferred Vendor Name"
PX.Objects.FS.FSSiteStatusSelected.BarCode : Edm.String "Barcode"
PX.Objects.FS.FSSiteStatusSelected.AlternateID : Edm.String "Alternate ID"
PX.Objects.FS.FSSiteStatusSelected.AlternateType : Edm.String "Alternate Type"
PX.Objects.FS.FSSiteStatusSelected.AlternateDescr : Edm.String "Alternate Description"
PX.Objects.FS.FSSiteStatusSelected.SiteCD : Edm.String
PX.Objects.FS.FSSiteStatusSelected.SubItemCD : Edm.String
PX.Objects.FS.FSSiteStatusSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.FS.FSSiteStatusSelected.CuryID : Edm.String "Currency"
PX.Objects.FS.FSSiteStatusSelected.CuryInfoID : Edm.Int64
PX.Objects.FS.FSSiteStatusSelected.SalesUnit : Edm.String "Sales Unit"
PX.Objects.FS.FSSiteStatusSelected.BillingRule : Edm.String "Billing Rule"
PX.Objects.FS.FSSiteStatusSelected.EstimatedDuration : Edm.Int32 "Estimated Duration"
PX.Objects.FS.FSSiteStatusSelected.QtySelected : Edm.Decimal "Qty. Selected"
PX.Objects.FS.FSSiteStatusSelected.DurationSelected : Edm.Int32 "Duration Selected"
PX.Objects.FS.FSSiteStatusSelected.QtyOnHand : Edm.Decimal "Qty. On Hand"
PX.Objects.FS.FSSiteStatusSelected.QtyAvail : Edm.Decimal "Qty. Available"
PX.Objects.FS.FSSiteStatusSelected.QtyLast : Edm.Decimal
PX.Objects.FS.FSSiteStatusSelected.BaseUnitPrice : Edm.Decimal
PX.Objects.FS.FSSiteStatusSelected.CuryUnitPrice : Edm.Decimal "Last Unit Price"
PX.Objects.FS.FSSiteStatusSelected.QtyAvailSale : Edm.Decimal "Qty. Available"
PX.Objects.FS.FSSiteStatusSelected.QtyOnHandSale : Edm.Decimal "Qty. On Hand"
PX.Objects.FS.FSSiteStatusSelected.QtyLastSale : Edm.Decimal "Qty. Last Sales"
PX.Objects.FS.FSSiteStatusSelected.LastSalesDate : Edm.DateTimeOffset "Last Sales Date"
PX.Objects.FS.FSSiteStatusSelected.DropShipLastBaseQty : Edm.Decimal
PX.Objects.FS.FSSiteStatusSelected.DropShipLastQty : Edm.Decimal "Qty. of Last Drop Ship"
PX.Objects.FS.FSSiteStatusSelected.DropShipLastUnitPrice : Edm.Decimal
PX.Objects.FS.FSSiteStatusSelected.DropShipCuryUnitPrice : Edm.Decimal "Unit Price of Last Drop Ship"
PX.Objects.FS.FSSiteStatusSelected.DropShipLastDate : Edm.DateTimeOffset "Date of Last Drop Ship"
PX.Objects.FS.FSSiteStatusSelected.NoteID : Edm.Guid
PX.Objects.FS.FSSiteStatusSelected.CuryRate : Edm.Decimal
PX.Objects.FS.FSSiteStatusSelected.CuryViewState : Edm.Boolean
PX.Objects.FS.FSSiteStatusSelected.VendorByPreferredVendorID -> PX.Objects.AP.Vendor (PreferredVendorID=BAccountID)
PX.Objects.FS.FSSiteStatusSelected.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSSiteStatusSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.FS.FSSiteStatusSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.FS.FSSiteStatusSelected.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSSiteStatusSelected.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.FS.FSSiteStatusSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.FS.FSSiteStatusSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.FS.FSSkill (EntityType)

Label: "Skill"
Key: SkillCD
Entity sets: PX_Objects_FS_FSSkill, Skill, FSSkill
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.FS.FSSkill.SkillID : Edm.Int32
PX.Objects.FS.FSSkill.SkillCD : Edm.String [key] "Skill ID"
PX.Objects.FS.FSSkill.Descr : Edm.String "Description"
PX.Objects.FS.FSSkill.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSSkill.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSSkill.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSSkill.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSSkill.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSSkill.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSSkill.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSSkill.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSSkill.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSSkill.IsDriverSkill : Edm.Boolean [required] "Driver Skill"
PX.Objects.FS.FSSkill.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.FS.FSSkill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSkill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSkill.FSEmployeeSkillCollection -> Collection(PX.Objects.SV.FSEmployeeSkill)
PX.Objects.FS.FSSkill.SVWorkTaskLaborCollection -> Collection(PX.Objects.SV.SVWorkTaskLabor)
PX.Objects.FS.FSSkill.SVVendorSkillCollection -> Collection(PX.Objects.SV.SVVendorSkill)
PX.Objects.FS.FSSkill.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)

# PX.Objects.FS.FSSODet (EntityType)

Label: "Service Order Item Detail"
Key: LineNbr, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSSODet, ServiceOrderItemDetail, FSSODet
Non-filterable, non-selectable: Behavior, TranType, SOLineType, IsStockItem, IsKit, OrderQty, BaseOrderQty, DeductQty, BaseDeductQty, RequireShipping, RequireAllocation, RequireLocation, LineQtyAvail, LineQtyHardAvail, NoteText, EnableUnlinkPO, CuryExtPrice, CuryLineAmt, SkipCostCodeValidation, EstimatedDurationReport, TabOrigin, SkipUnitPriceCalc, AlreadyCalculatedUnitPrice, IsTravelItem, EnableStaffID, InventoryIDReport, LinkedDisplayRefNbr

PX.Objects.FS.FSSODet.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSSODet.RefNbr : Edm.String [key] "Service Order Nbr."
PX.Objects.FS.FSSODet.SOID : Edm.Int32 "SOID"
PX.Objects.FS.FSSODet.SODetID : Edm.Int32 "SODetID"
PX.Objects.FS.FSSODet.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.FSSODet.LineRef : Edm.String "Ref. Nbr."
PX.Objects.FS.FSSODet.BranchID : Edm.Int32 "Branch"
PX.Objects.FS.FSSODet.Operation : Edm.String "Operation"
PX.Objects.FS.FSSODet.Behavior : Edm.String
PX.Objects.FS.FSSODet.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.FS.FSSODet.TranType : Edm.String
PX.Objects.FS.FSSODet.InvtMult : Edm.Int16 "Inventory Multiplier"
PX.Objects.FS.FSSODet.Completed : Edm.Boolean "Completed"
PX.Objects.FS.FSSODet.BillCustomerID : Edm.Int32
PX.Objects.FS.FSSODet.CuryInfoID : Edm.Int64
PX.Objects.FS.FSSODet.LineType : Edm.String "Line Type"
PX.Objects.FS.FSSODet.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSSODet.SOLineType : Edm.String "SO Line Type"
PX.Objects.FS.FSSODet.BillingRule : Edm.String "Billing Rule"
PX.Objects.FS.FSSODet.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.FS.FSSODet.IsKit : Edm.Boolean "Is a Kit"
PX.Objects.FS.FSSODet.UOM : Edm.String "UOM"
PX.Objects.FS.FSSODet.UnassignedQty : Edm.Decimal
PX.Objects.FS.FSSODet.EstimatedDuration : Edm.Int32 [required] "Estimated Duration"
PX.Objects.FS.FSSODet.EstimatedQty : Edm.Decimal "Estimated Quantity"
PX.Objects.FS.FSSODet.BaseEstimatedQty : Edm.Decimal "Base Estimated Qty."
PX.Objects.FS.FSSODet.OrderQty : Edm.Decimal "Allocation Quantity"
PX.Objects.FS.FSSODet.BaseOrderQty : Edm.Decimal "Base Order Qty."
PX.Objects.FS.FSSODet.DeductQty : Edm.Decimal
PX.Objects.FS.FSSODet.BaseDeductQty : Edm.Decimal
PX.Objects.FS.FSSODet.ShippedQty : Edm.Decimal "Qty. On Shipments"
PX.Objects.FS.FSSODet.BaseShippedQty : Edm.Decimal
PX.Objects.FS.FSSODet.OpenQty : Edm.Decimal "Open Qty."
PX.Objects.FS.FSSODet.BaseOpenQty : Edm.Decimal "Base Open Qty."
PX.Objects.FS.FSSODet.ClosedQty : Edm.Decimal
PX.Objects.FS.FSSODet.BaseClosedQty : Edm.Decimal
PX.Objects.FS.FSSODet.ManualCost : Edm.Boolean [required] "Manual Cost"
PX.Objects.FS.FSSODet.ManualPrice : Edm.Boolean [required] "Manual Price"
PX.Objects.FS.FSSODet.IsBillable : Edm.Boolean "Billable"
PX.Objects.FS.FSSODet.IsFree : Edm.Boolean "Free Item"
PX.Objects.FS.FSSODet.BillableQty : Edm.Decimal [required] "Quantity"
PX.Objects.FS.FSSODet.BaseBillableQty : Edm.Decimal "Base Billable Qty."
PX.Objects.FS.FSSODet.ProjectID : Edm.Int32 "ProjectID"
PX.Objects.FS.FSSODet.CostCenterID : Edm.Int32 [required]
PX.Objects.FS.FSSODet.SourceLineID : Edm.Int32 "Source Line ID"
PX.Objects.FS.FSSODet.SourceNoteID : Edm.Guid "Source Note ID"
PX.Objects.FS.FSSODet.SourceLineNbr : Edm.Int32 "Source Line Nbr."
PX.Objects.FS.FSSODet.TranDate : Edm.DateTimeOffset "Transaction Date"
PX.Objects.FS.FSSODet.PlanType : Edm.String
PX.Objects.FS.FSSODet.RequireShipping : Edm.Boolean
PX.Objects.FS.FSSODet.RequireAllocation : Edm.Boolean
PX.Objects.FS.FSSODet.RequireLocation : Edm.Boolean
PX.Objects.FS.FSSODet.LineQtyAvail : Edm.Decimal
PX.Objects.FS.FSSODet.LineQtyHardAvail : Edm.Decimal
PX.Objects.FS.FSSODet.ShipDate : Edm.DateTimeOffset "Ship On"
PX.Objects.FS.FSSODet.TranDesc : Edm.String "Description"
PX.Objects.FS.FSSODet.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSSODet.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSSODet.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSSODet.CreatedByScreenID : Edm.String
PX.Objects.FS.FSSODet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSODet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSSODet.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSSODet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSODet.tstamp : Edm.Binary
PX.Objects.FS.FSSODet.Status : Edm.String "Line Status"
PX.Objects.FS.FSSODet.ScheduleDetID : Edm.Int32 "ScheduleDetID"
PX.Objects.FS.FSSODet.PostID : Edm.Int32 "Post ID"
PX.Objects.FS.FSSODet.ScheduleID : Edm.Int32
PX.Objects.FS.FSSODet.EnableUnlinkPO : Edm.Boolean "Allow PO Unlinking"
PX.Objects.FS.FSSODet.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.FS.FSSODet.UnitCost : Edm.Decimal
PX.Objects.FS.FSSODet.CuryExtCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.FS.FSSODet.ExtCost : Edm.Decimal [required]
PX.Objects.FS.FSSODet.OrigUnitCost : Edm.Decimal
PX.Objects.FS.FSSODet.CuryUnitPrice : Edm.Decimal "Unit Price"
PX.Objects.FS.FSSODet.UnitPrice : Edm.Decimal "Base Unit Price"
PX.Objects.FS.FSSODet.EstimatedTranAmt : Edm.Decimal "Base Estimated Amount"
PX.Objects.FS.FSSODet.CuryEstimatedTranAmt : Edm.Decimal "Estimated Amount"
PX.Objects.FS.FSSODet.CuryBillableExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.FS.FSSODet.BillableExtPrice : Edm.Decimal
PX.Objects.FS.FSSODet.CuryBillableTranAmt : Edm.Decimal "Amount"
PX.Objects.FS.FSSODet.BillableTranAmt : Edm.Decimal "Base Billable Amount"
PX.Objects.FS.FSSODet.CuryExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.FS.FSSODet.CuryLineAmt : Edm.Decimal "Amount"
PX.Objects.FS.FSSODet.ManualDisc : Edm.Boolean "Manual Discount"
PX.Objects.FS.FSSODet.DiscPct : Edm.Decimal "Discount Percent"
PX.Objects.FS.FSSODet.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.FS.FSSODet.DiscAmt : Edm.Decimal
PX.Objects.FS.FSSODet.DiscountID : Edm.String "Discount Code"
PX.Objects.FS.FSSODet.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.FS.FSSODet.ApptCntr : Edm.Int32 "Appointment Count"
PX.Objects.FS.FSSODet.ApptEstimatedDuration : Edm.Int32 "Appointment Estimated Duration"
PX.Objects.FS.FSSODet.ApptDuration : Edm.Int32 "Appointment Duration"
PX.Objects.FS.FSSODet.ApptQty : Edm.Decimal "Appointment Quantity"
PX.Objects.FS.FSSODet.CuryApptTranAmt : Edm.Decimal "Appointment Amount"
PX.Objects.FS.FSSODet.ApptTranAmt : Edm.Decimal "Base Appointment Amount"
PX.Objects.FS.FSSODet.StaffID : Edm.Int32 "Staff Member ID"
PX.Objects.FS.FSSODet.EquipmentItemClass : Edm.String
PX.Objects.FS.FSSODet.SkipCostCodeValidation : Edm.Boolean
PX.Objects.FS.FSSODet.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.FS.FSSODet.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.FS.FSSODet.GroupDiscountRate : Edm.Decimal
PX.Objects.FS.FSSODet.DocumentDiscountRate : Edm.Decimal [required]
PX.Objects.FS.FSSODet.EstimatedDurationReport : Edm.Int32
PX.Objects.FS.FSSODet.TabOrigin : Edm.Int32
PX.Objects.FS.FSSODet.SkipUnitPriceCalc : Edm.Boolean
PX.Objects.FS.FSSODet.AlreadyCalculatedUnitPrice : Edm.Decimal
PX.Objects.FS.FSSODet.IsTravelItem : Edm.Boolean "Is a Travel Item"
PX.Objects.FS.FSSODet.EnableStaffID : Edm.Boolean
PX.Objects.FS.FSSODet.InventoryIDReport : Edm.Int32
PX.Objects.FS.FSSODet.LinkedEntityType : Edm.String "Related Doc. Type"
PX.Objects.FS.FSSODet.LinkedDocType : Edm.String "LinkedDocType"
PX.Objects.FS.FSSODet.LinkedDocRefNbr : Edm.String "LinkedDocRefNbr"
PX.Objects.FS.FSSODet.LinkedDisplayRefNbr : Edm.String "Related Doc. Nbr."
PX.Objects.FS.FSSODet.LinkedLineNbr : Edm.Int32 "Related Doc. Line Nbr."
PX.Objects.FS.FSSODet.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.FS.FSSODet.VendorByPoVendorID -> PX.Objects.AP.Vendor
PX.Objects.FS.FSSODet.POOrderByPoNbr -> PX.Objects.PO.POOrder
PX.Objects.FS.FSSODet.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.FS.FSSODet.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.FS.FSSODet.BAccountByStaffID -> PX.Objects.CR.BAccount (StaffID=BAccountID)
PX.Objects.FS.FSSODet.BAccountByPoVendorID -> PX.Objects.CR.BAccount
PX.Objects.FS.FSSODet.CustomerByBillCustomerID -> PX.Objects.AR.Customer (BillCustomerID=BAccountID)
PX.Objects.FS.FSSODet.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSSODet.FSScheduleByScheduleID -> PX.Objects.FS.FSSchedule (ScheduleID=ScheduleID)
PX.Objects.FS.FSSODet.FSEquipmentBySMequipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSSODet.FSSODetByNewTargetEquipmentLineNbr -> PX.Objects.FS.FSSODet
PX.Objects.FS.FSSODet.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSSODet.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.FS.FSSODet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSODet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSODet.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.FS.FSSODet.SOOrderTypeByPoType -> PX.Objects.SO.SOOrderType
PX.Objects.FS.FSSODet.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation)
PX.Objects.FS.FSSODet.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.FS.FSSODet.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.FS.FSSODet.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.FS.FSSODet.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSSODet.INSiteByPOSiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSSODet.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.FS.FSSODet.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.FS.FSSODet.AccountByAcctID -> PX.Objects.GL.Account
PX.Objects.FS.FSSODet.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.FS.FSSODet.LocationByPoVendorID -> PX.Objects.CR.Location
PX.Objects.FS.FSSODet.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.FS.FSSODet.FSEquipmentComponentByEquipmentLineRef -> PX.Objects.FS.FSEquipmentComponent
PX.Objects.FS.FSSODet.FSEquipmentComponentBySMequipmentID -> PX.Objects.FS.FSEquipmentComponent
PX.Objects.FS.FSSODet.FSModelTemplateComponentByComponentID -> PX.Objects.FS.FSModelTemplateComponent
PX.Objects.FS.FSSODet.FSPostInfoByPostID -> PX.Objects.FS.FSPostInfo (PostID=PostID)
PX.Objects.FS.FSSODet.FSScheduleDetByScheduleDetID -> PX.Objects.FS.FSScheduleDet (ScheduleID=ScheduleID, ScheduleDetID=ScheduleDetID)
PX.Objects.FS.FSSODet.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSSODet.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSSODet.INLotSerialStatusByCostCenterBySiteLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.FS.FSSODet.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.FS.FSSODet.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.FS.FSSODet.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSSODet.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.FSSODet.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.FS.FSSODet.InventoryPostingBatchDetailCollection -> Collection(PX.Objects.FS.InventoryPostingBatchDetail)
PX.Objects.FS.FSSODet.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.FS.FSSODet.FSSOEmployeeCollection -> Collection(PX.Objects.FS.FSSOEmployee)
PX.Objects.FS.FSSODet.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.FS.FSSODet.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)

# PX.Objects.FS.FSSODetEmployee (EntityType)

Label: "Service Order Item Detail"
BaseType: PX.Objects.FS.FSSODet
Key: LineNbr, RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSSODet)
Entity sets: PX_Objects_FS_FSSODetEmployee

# PX.Objects.FS.FSSODetFSSODetSplit (EntityType)

Key: LineNbr, RefNbr, SplitLineNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSSODetFSSODetSplit

PX.Objects.FS.FSSODetFSSODetSplit.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSSODetFSSODetSplit.RefNbr : Edm.String [key] "Service Order Nbr."
PX.Objects.FS.FSSODetFSSODetSplit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.FSSODetFSSODetSplit.SplitLineNbr : Edm.Int32 [key] "Allocation ID"
PX.Objects.FS.FSSODetFSSODetSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSSODetFSSODetSplit.PlanID : Edm.Int64 "Plan ID"
PX.Objects.FS.FSSODetFSSODetSplit.POType : Edm.String "PO Type"
PX.Objects.FS.FSSODetFSSODetSplit.PONbr : Edm.String "PO Nbr."
PX.Objects.FS.FSSODetFSSODetSplit.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.FS.FSSODetFSSODetSplit.UnitPrice : Edm.Decimal "Base Unit Price"
PX.Objects.FS.FSSODetFSSODetSplit.UOM : Edm.String "UOM"
PX.Objects.FS.FSSODetFSSODetSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSSODetFSSODetSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.FS.FSSODetFSSODetSplit.FSSODetByLineNbr -> PX.Objects.FS.FSSODet (SrvOrdType=SrvOrdType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.FS.FSSODetFSSODetSplit.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSSODetFSSODetSplit.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSSODetFSSODetSplit.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.FS.FSSODetFSSODetSplit.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.FS.FSSODetFSSODetSplit.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.FS.FSSODetFSSODetSplit.FSSODetSplitBySplitLineNbr -> PX.Objects.FS.FSSODetSplit (SplitLineNbr=ParentSplitLineNbr)
PX.Objects.FS.FSSODetFSSODetSplit.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.FS.FSSODetFSSODetSplit.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSSODetFSSODetSplit.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.FS.FSSODetFSSODetSplit.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)

# PX.Objects.FS.FSSODetSplit (EntityType)

Label: "Service Order Lot/Serial Detail"
Key: LineNbr, RefNbr, SplitLineNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSSODetSplit, ServiceOrderLotSerialDetail, FSSODetSplit
Non-filterable, non-selectable: IsMergeable, LotSerClassID, AssignedNbr, UnreceivedQty, BaseUnreceivedQty, OpenQty, BaseOpenQty, TranType, RequireShipping, RequireAllocation, RequireLocation, ProjectID, TaskID, CuryID, CuryRate, CuryViewState

PX.Objects.FS.FSSODetSplit.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSSODetSplit.RefNbr : Edm.String [key]
PX.Objects.FS.FSSODetSplit.LineNbr : Edm.Int32 [key]
PX.Objects.FS.FSSODetSplit.SplitLineNbr : Edm.Int32 [key] "Allocation ID"
PX.Objects.FS.FSSODetSplit.ParentSplitLineNbr : Edm.Int32 "Parent Allocation ID"
PX.Objects.FS.FSSODetSplit.Operation : Edm.String
PX.Objects.FS.FSSODetSplit.InvtMult : Edm.Int16
PX.Objects.FS.FSSODetSplit.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.FSSODetSplit.LineType : Edm.String
PX.Objects.FS.FSSODetSplit.IsStockItem : Edm.Boolean
PX.Objects.FS.FSSODetSplit.IsAllocated : Edm.Boolean [required] "Allocated"
PX.Objects.FS.FSSODetSplit.IsMergeable : Edm.Boolean
PX.Objects.FS.FSSODetSplit.ShipDate : Edm.DateTimeOffset "Ship On"
PX.Objects.FS.FSSODetSplit.ShipComplete : Edm.String
PX.Objects.FS.FSSODetSplit.Completed : Edm.Boolean "Completed"
PX.Objects.FS.FSSODetSplit.ShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.FS.FSSODetSplit.LotSerClassID : Edm.String
PX.Objects.FS.FSSODetSplit.AssignedNbr : Edm.String
PX.Objects.FS.FSSODetSplit.UOM : Edm.String "UOM"
PX.Objects.FS.FSSODetSplit.Qty : Edm.Decimal [required] "Quantity"
PX.Objects.FS.FSSODetSplit.BaseQty : Edm.Decimal
PX.Objects.FS.FSSODetSplit.ShippedQty : Edm.Decimal [required] "Qty. On Shipments"
PX.Objects.FS.FSSODetSplit.BaseShippedQty : Edm.Decimal [required]
PX.Objects.FS.FSSODetSplit.ReceivedQty : Edm.Decimal "Qty. Received"
PX.Objects.FS.FSSODetSplit.BaseReceivedQty : Edm.Decimal
PX.Objects.FS.FSSODetSplit.UnreceivedQty : Edm.Decimal
PX.Objects.FS.FSSODetSplit.BaseUnreceivedQty : Edm.Decimal
PX.Objects.FS.FSSODetSplit.OpenQty : Edm.Decimal
PX.Objects.FS.FSSODetSplit.BaseOpenQty : Edm.Decimal
PX.Objects.FS.FSSODetSplit.OrderDate : Edm.DateTimeOffset
PX.Objects.FS.FSSODetSplit.TranType : Edm.String
PX.Objects.FS.FSSODetSplit.PlanType : Edm.String
PX.Objects.FS.FSSODetSplit.AllocatedPlanType : Edm.String
PX.Objects.FS.FSSODetSplit.BackOrderPlanType : Edm.String
PX.Objects.FS.FSSODetSplit.OrigPlanType : Edm.String
PX.Objects.FS.FSSODetSplit.RequireShipping : Edm.Boolean
PX.Objects.FS.FSSODetSplit.RequireAllocation : Edm.Boolean
PX.Objects.FS.FSSODetSplit.RequireLocation : Edm.Boolean
PX.Objects.FS.FSSODetSplit.POCreate : Edm.Boolean "Mark for PO"
PX.Objects.FS.FSSODetSplit.POCompleted : Edm.Boolean
PX.Objects.FS.FSSODetSplit.POCancelled : Edm.Boolean
PX.Objects.FS.FSSODetSplit.POSource : Edm.String
PX.Objects.FS.FSSODetSplit.FixedSource : Edm.String
PX.Objects.FS.FSSODetSplit.VendorID : Edm.Int32
PX.Objects.FS.FSSODetSplit.POSiteID : Edm.Int32
PX.Objects.FS.FSSODetSplit.POType : Edm.String "PO Type"
PX.Objects.FS.FSSODetSplit.PONbr : Edm.String "PO Nbr."
PX.Objects.FS.FSSODetSplit.POLineNbr : Edm.Int32 "PO Line Nbr."
PX.Objects.FS.FSSODetSplit.POReceiptType : Edm.String "PO Receipt Type"
PX.Objects.FS.FSSODetSplit.POReceiptNbr : Edm.String "PO Receipt Nbr."
PX.Objects.FS.FSSODetSplit.SOOrderType : Edm.String
PX.Objects.FS.FSSODetSplit.SOOrderNbr : Edm.String
PX.Objects.FS.FSSODetSplit.SOLineNbr : Edm.Int32
PX.Objects.FS.FSSODetSplit.SOSplitLineNbr : Edm.Int32
PX.Objects.FS.FSSODetSplit.RefNoteID : Edm.Guid "Related Document"
PX.Objects.FS.FSSODetSplit.PlanID : Edm.Int64
PX.Objects.FS.FSSODetSplit.ProjectID : Edm.Int32
PX.Objects.FS.FSSODetSplit.TaskID : Edm.Int32
PX.Objects.FS.FSSODetSplit.CostCenterID : Edm.Int32 [required]
PX.Objects.FS.FSSODetSplit.CuryInfoID : Edm.Int64
PX.Objects.FS.FSSODetSplit.UnitCost : Edm.Decimal [required]
PX.Objects.FS.FSSODetSplit.CuryExtCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.FS.FSSODetSplit.ExtCost : Edm.Decimal [required]
PX.Objects.FS.FSSODetSplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSSODetSplit.CreatedByScreenID : Edm.String
PX.Objects.FS.FSSODetSplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSODetSplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSSODetSplit.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSSODetSplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSODetSplit.tstamp : Edm.Binary
PX.Objects.FS.FSSODetSplit.CuryID : Edm.String "Currency"
PX.Objects.FS.FSSODetSplit.CuryRate : Edm.Decimal
PX.Objects.FS.FSSODetSplit.CuryViewState : Edm.Boolean
PX.Objects.FS.FSSODetSplit.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.FS.FSSODetSplit.POLineByPOLineNbr -> PX.Objects.PO.POLine (POType=OrderType, PONbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.FS.FSSODetSplit.POOrderByPONbr -> PX.Objects.PO.POOrder (POType=OrderType, PONbr=OrderNbr)
PX.Objects.FS.FSSODetSplit.POOrderByPOType -> PX.Objects.PO.POOrder (PONbr=OrderNbr, POType=OrderType)
PX.Objects.FS.FSSODetSplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.FSSODetSplit.INItemPlanByPlanID -> PX.Objects.IN.INItemPlan (PlanID=PlanID)
PX.Objects.FS.FSSODetSplit.FSSODetByLineNbr -> PX.Objects.FS.FSSODet (SrvOrdType=SrvOrdType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.FS.FSSODetSplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSODetSplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSODetSplit.SOOrderTypeOperationByOperation -> PX.Objects.SO.SOOrderTypeOperation (Operation=Operation)
PX.Objects.FS.FSSODetSplit.SOShipmentByShipmentNbr -> PX.Objects.SO.SOShipment (ShipmentNbr=ShipmentNbr)
PX.Objects.FS.FSSODetSplit.POReceiptByPOReceiptNbr -> PX.Objects.PO.POReceipt (POReceiptType=ReceiptType, POReceiptNbr=ReceiptNbr)
PX.Objects.FS.FSSODetSplit.POReceiptByPOReceiptType -> PX.Objects.PO.POReceipt (POReceiptNbr=ReceiptNbr, POReceiptType=ReceiptType)
PX.Objects.FS.FSSODetSplit.INCostCenterByCostCenterID -> PX.Objects.IN.INCostCenter (CostCenterID=CostCenterID)
PX.Objects.FS.FSSODetSplit.INLocationByLocationID -> PX.Objects.IN.INLocation
PX.Objects.FS.FSSODetSplit.INLocationBySiteID -> PX.Objects.IN.INLocation
PX.Objects.FS.FSSODetSplit.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSSODetSplit.INSiteByToSiteID -> PX.Objects.IN.INSite
PX.Objects.FS.FSSODetSplit.INSiteByPOSiteID -> PX.Objects.IN.INSite (POSiteID=SiteID)
PX.Objects.FS.FSSODetSplit.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.FS.FSSODetSplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.FS.FSSODetSplit.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSSODetSplit.FSSODetSplitBySplitLineNbr -> PX.Objects.FS.FSSODetSplit (SplitLineNbr=ParentSplitLineNbr)
PX.Objects.FS.FSSODetSplit.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.FSSODetSplit.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID, CostCenterID=CostCenterID)
PX.Objects.FS.FSSODetSplit.INLocationStatusByLocationID -> PX.Objects.IN.INLocationStatus (InventoryID=InventoryID)
PX.Objects.FS.FSSODetSplit.INLotSerialStatusByLotSerialNbr -> PX.Objects.IN.INLotSerialStatus (InventoryID=InventoryID)
PX.Objects.FS.FSSODetSplit.INSiteStatusBySiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.FS.FSSODetSplit.INSiteStatusByToSiteID -> PX.Objects.IN.INSiteStatus (InventoryID=InventoryID)
PX.Objects.FS.FSSODetSplit.INPlanTypeByOrigPlanType -> PX.Objects.IN.INPlanType (OrigPlanType=PlanType)
PX.Objects.FS.FSSODetSplit.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.FS.FSSODetSplit.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)

# PX.Objects.FS.FSSOEmployee (EntityType)

Label: "FSSOEmployee"
Key: LineNbr, RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_FSSOEmployee, FSSOEmployee
Non-filterable, non-selectable: CuryID, CuryRate, CuryViewState

PX.Objects.FS.FSSOEmployee.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSSOEmployee.RefNbr : Edm.String [key] "Service Order Nbr."
PX.Objects.FS.FSSOEmployee.LineNbr : Edm.Int32 [key]
PX.Objects.FS.FSSOEmployee.SOID : Edm.Int32 "SOID"
PX.Objects.FS.FSSOEmployee.LineRef : Edm.String "Ref. Nbr."
PX.Objects.FS.FSSOEmployee.ServiceLineRef : Edm.String "Detail Ref. Nbr."
PX.Objects.FS.FSSOEmployee.EmployeeID : Edm.Int32 "Staff Member"
PX.Objects.FS.FSSOEmployee.Comment : Edm.String "Comment"
PX.Objects.FS.FSSOEmployee.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSSOEmployee.CreatedByScreenID : Edm.String
PX.Objects.FS.FSSOEmployee.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSOEmployee.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSSOEmployee.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSSOEmployee.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSOEmployee.tstamp : Edm.Binary
PX.Objects.FS.FSSOEmployee.Type : Edm.String "Type"
PX.Objects.FS.FSSOEmployee.CuryInfoID : Edm.Int64
PX.Objects.FS.FSSOEmployee.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.FS.FSSOEmployee.UnitCost : Edm.Decimal [required]
PX.Objects.FS.FSSOEmployee.CuryExtCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.FS.FSSOEmployee.ExtCost : Edm.Decimal [required]
PX.Objects.FS.FSSOEmployee.CuryID : Edm.String "Currency"
PX.Objects.FS.FSSOEmployee.CuryRate : Edm.Decimal
PX.Objects.FS.FSSOEmployee.CuryViewState : Edm.Boolean
PX.Objects.FS.FSSOEmployee.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.FS.FSSOEmployee.FSSODetByServiceLineRef -> PX.Objects.FS.FSSODet (ServiceLineRef=LineRef)
PX.Objects.FS.FSSOEmployee.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSOEmployee.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSOEmployee.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSSOEmployee.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSSOResource (EntityType)

Label: "FSSOResource"
Key: RefNbr, SMEquipmentID, SrvOrdType
Entity sets: PX_Objects_FS_FSSOResource, FSSOResource

PX.Objects.FS.FSSOResource.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSSOResource.RefNbr : Edm.String [key] "Service Order Nbr."
PX.Objects.FS.FSSOResource.SMEquipmentID : Edm.Int32 [key] "Equipment ID"
PX.Objects.FS.FSSOResource.SOID : Edm.Int32 "SOID"
PX.Objects.FS.FSSOResource.Comment : Edm.String "Comment"
PX.Objects.FS.FSSOResource.Qty : Edm.Int32 [required] "Quantity"
PX.Objects.FS.FSSOResource.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSSOResource.CreatedByScreenID : Edm.String
PX.Objects.FS.FSSOResource.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSOResource.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSSOResource.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSSOResource.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSOResource.tstamp : Edm.Binary
PX.Objects.FS.FSSOResource.FSEquipmentBySMequipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSSOResource.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSOResource.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSOResource.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, RefNbr=RefNbr)
PX.Objects.FS.FSSOResource.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSSrvOrdQuickProcessParams (EntityType)

BaseType: PX.Objects.SO.SOQuickProcessParameters
Key: OrderType (inherited from PX.Objects.SO.SOQuickProcessParameters)
Entity sets: PX_Objects_FS_FSSrvOrdQuickProcessParams
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.FS.FSSrvOrdQuickProcessParams.SrvOrdType : Edm.String
PX.Objects.FS.FSSrvOrdQuickProcessParams.AllowInvoiceServiceOrder : Edm.Boolean "Allow Billing"
PX.Objects.FS.FSSrvOrdQuickProcessParams.CompleteServiceOrder : Edm.Boolean "Complete"
PX.Objects.FS.FSSrvOrdQuickProcessParams.CloseServiceOrder : Edm.Boolean "Close"
PX.Objects.FS.FSSrvOrdQuickProcessParams.GenerateInvoiceFromServiceOrder : Edm.Boolean "Run Billing"
PX.Objects.FS.FSSrvOrdQuickProcessParams.SOQuickProcess : Edm.Boolean "Use Sales Order Quick Processing"
PX.Objects.FS.FSSrvOrdQuickProcessParams.EmailSalesOrder : Edm.Boolean "Email Sales Order/Quote"

# PX.Objects.FS.FSSrvOrdType (EntityType)

Label: "Order Type"
Key: SrvOrdType
Entity sets: PX_Objects_FS_FSSrvOrdType, OrderType, FSSrvOrdType
Non-filterable, non-selectable: NoteText, ShowQuickProcessTab, PostToSOSIPM, AllowInventoryItems

PX.Objects.FS.FSSrvOrdType.SrvOrdTypeID : Edm.Int32 "SrvOrdTypeID"
PX.Objects.FS.FSSrvOrdType.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.FSSrvOrdType.Active : Edm.Boolean [required] "Active"
PX.Objects.FS.FSSrvOrdType.AllowPartialBilling : Edm.Boolean [required] "Allow Partial Billing"
PX.Objects.FS.FSSrvOrdType.AllowQuickProcess : Edm.Boolean [required] "Allow Quick Process"
PX.Objects.FS.FSSrvOrdType.AppAddressSource : Edm.String "Take Address and Contact Information From"
PX.Objects.FS.FSSrvOrdType.AppContactInfoSource : Edm.String "Appointment Contact info source"
PX.Objects.FS.FSSrvOrdType.BAccountRequired : Edm.Boolean [required] "Require Business Account"
PX.Objects.FS.FSSrvOrdType.Behavior : Edm.String "Behavior"
PX.Objects.FS.FSSrvOrdType.BillSeparately : Edm.Boolean [required] "Bill Separately"
PX.Objects.FS.FSSrvOrdType.CompleteSrvOrdWhenSrvDone : Edm.Boolean [required] "Complete Service Order When Its Appointments Are Completed"
PX.Objects.FS.FSSrvOrdType.CloseSrvOrdWhenSrvDone : Edm.Boolean [required] "Close Service Order When Its Appointments Are Closed"
PX.Objects.FS.FSSrvOrdType.DfltTermIDARSO : Edm.String "Default Terms for AR and SO"
PX.Objects.FS.FSSrvOrdType.DfltTermIDAP : Edm.String "Default Terms for AP"
PX.Objects.FS.FSSrvOrdType.Descr : Edm.String "Description"
PX.Objects.FS.FSSrvOrdType.EnableINPosting : Edm.Boolean [required] "Post Pickup/Delivery Items to Inventory"
PX.Objects.FS.FSSrvOrdType.GenerateInvoiceBy : Edm.String "Generate Invoice By"
PX.Objects.FS.FSSrvOrdType.AllowInvoiceOnlyClosedAppointment : Edm.Boolean [required] "Bill Only Closed Appointments"
PX.Objects.FS.FSSrvOrdType.PostNegBalanceToAP : Edm.Boolean [required] "Create AP Bills for Negative Balances"
PX.Objects.FS.FSSrvOrdType.PostOrderType : Edm.String "Order Type for Billing"
PX.Objects.FS.FSSrvOrdType.PostOrderTypeNegativeBalance : Edm.String "Order Type for Negative Balance Billing"
PX.Objects.FS.FSSrvOrdType.AllocationOrderType : Edm.String "Order Type for Allocation"
PX.Objects.FS.FSSrvOrdType.PostTo : Edm.String "Generated Billing Documents"
PX.Objects.FS.FSSrvOrdType.RequireAppConfirmation : Edm.Boolean [required] "Appointment Confirmation Required"
PX.Objects.FS.FSSrvOrdType.RequireAddressValidation : Edm.Boolean [required] "Require Address Validation"
PX.Objects.FS.FSSrvOrdType.RequireContact : Edm.Boolean [required] "Require Contact"
PX.Objects.FS.FSSrvOrdType.RequireCustomerSignature : Edm.Boolean "Require Customer Signature on Mobile App"
PX.Objects.FS.FSSrvOrdType.RequireRoom : Edm.Boolean [required] "Require Room"
PX.Objects.FS.FSSrvOrdType.RequireRoute : Edm.Boolean [required] "Require Route"
PX.Objects.FS.FSSrvOrdType.SalesAcctSource : Edm.String "Use Sales Account From"
PX.Objects.FS.FSSrvOrdType.SrvOrdNumberingID : Edm.String "Numbering Sequence"
PX.Objects.FS.FSSrvOrdType.RequireTimeApprovalToInvoice : Edm.Boolean [required] "Require Time Approval to Close/Bill Appointments"
PX.Objects.FS.FSSrvOrdType.CreateTimeActivitiesFromAppointment : Edm.Boolean "Automatically Create Time Activities from Appointments"
PX.Objects.FS.FSSrvOrdType.DfltEarningType : Edm.String "Default Earning Type"
PX.Objects.FS.FSSrvOrdType.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.FS.FSSrvOrdType.ReleaseProjectTransactionOnInvoice : Edm.Boolean [required] "Automatically Release Project Transactions"
PX.Objects.FS.FSSrvOrdType.BillingType : Edm.String "Billing Type"
PX.Objects.FS.FSSrvOrdType.ServiceOrderWorkflowTypeID : Edm.String "Service Order Workflow Type"
PX.Objects.FS.FSSrvOrdType.AppointmentWorkflowTypeID : Edm.String "Appointment Workflow Type"
PX.Objects.FS.FSSrvOrdType.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSSrvOrdType.CreatedByScreenID : Edm.String
PX.Objects.FS.FSSrvOrdType.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.FSSrvOrdType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSSrvOrdType.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSSrvOrdType.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.FS.FSSrvOrdType.tstamp : Edm.Binary
PX.Objects.FS.FSSrvOrdType.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSSrvOrdType.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSSrvOrdType.OnStartApptSetStartTimeInHeader : Edm.Boolean [required] "Set Start Time in Appointment"
PX.Objects.FS.FSSrvOrdType.OnStartApptSetNotStartItemInProcess : Edm.Boolean [required] "Set Not Started Items as In Process"
PX.Objects.FS.FSSrvOrdType.OnStartApptStartUnassignedStaff : Edm.Boolean [required] "Start Logging for Unassigned Staff"
PX.Objects.FS.FSSrvOrdType.OnStartApptStartServiceAndStaff : Edm.Boolean [required] "Start Logging for Services and Assigned Staff (If Any)"
PX.Objects.FS.FSSrvOrdType.OnCompleteApptSetEndTimeInHeader : Edm.Boolean [required] "Set End Time in Appointment"
PX.Objects.FS.FSSrvOrdType.OnCompleteApptSetInProcessItemsAs : Edm.String "Status to Set for In Process Items"
PX.Objects.FS.FSSrvOrdType.OnCompleteApptSetNotStartedItemsAs : Edm.String "Status to Set for Not Started Items"
PX.Objects.FS.FSSrvOrdType.OnStartTimeChangeUpdateLogStartTime : Edm.Boolean [required] "Update Log Start Time When Appointment Start Time is Updated"
PX.Objects.FS.FSSrvOrdType.OnEndTimeChangeUpdateLogEndTime : Edm.Boolean [required] "Update Log End Time When Appointment End Time is Updated"
PX.Objects.FS.FSSrvOrdType.OnCompleteApptRequireLog : Edm.Boolean [required] "Require Service Logs on Appointment Completion"
PX.Objects.FS.FSSrvOrdType.OnTravelCompleteStartAppt : Edm.Boolean [required] "Start Appointment When Travel Is Completed"
PX.Objects.FS.FSSrvOrdType.DfltBillableTravelItem : Edm.Int32 "Default Travel Item"
PX.Objects.FS.FSSrvOrdType.SetTimeInHeaderBasedOnLog : Edm.Boolean [required] "Update Appointment Time Based on Logged Time"
PX.Objects.FS.FSSrvOrdType.AllowManualLogTimeEdition : Edm.Boolean [required] "Manually Manage Time"
PX.Objects.FS.FSSrvOrdType.SalesPersonID : Edm.Int32 "Salesperson ID"
PX.Objects.FS.FSSrvOrdType.Commissionable : Edm.Boolean [required] "Commissionable"
PX.Objects.FS.FSSrvOrdType.CopyNotesFromCustomer : Edm.Boolean [required] "Copy Notes from Customer"
PX.Objects.FS.FSSrvOrdType.CopyAttachmentsFromCustomer : Edm.Boolean [required] "Copy Attachments from Customer"
PX.Objects.FS.FSSrvOrdType.CopyNotesFromCustomerLocation : Edm.Boolean [required] "Copy Notes from Customer Location"
PX.Objects.FS.FSSrvOrdType.CopyAttachmentsFromCustomerLocation : Edm.Boolean [required] "Copy Attachments from Customer Location"
PX.Objects.FS.FSSrvOrdType.CopyNotesToAppoinment : Edm.Boolean [required] "Copy Notes and Comments to Appointment"
PX.Objects.FS.FSSrvOrdType.CopyAttachmentsToAppoinment : Edm.Boolean [required] "Copy Attachments to Appointment"
PX.Objects.FS.FSSrvOrdType.CopyNotesToInvoice : Edm.Boolean [required] "Copy Notes to Invoice"
PX.Objects.FS.FSSrvOrdType.CopyAttachmentsToInvoice : Edm.Boolean [required] "Copy Attachments to Invoice"
PX.Objects.FS.FSSrvOrdType.CopyLineNotesToInvoice : Edm.Boolean [required] "Copy Line Notes to Invoice"
PX.Objects.FS.FSSrvOrdType.CopyLineAttachmentsToInvoice : Edm.Boolean [required] "Copy Line Attachments to Invoice"
PX.Objects.FS.FSSrvOrdType.ShowQuickProcessTab : Edm.Boolean
PX.Objects.FS.FSSrvOrdType.PostToSOSIPM : Edm.Boolean "PostToSOSIPM"
PX.Objects.FS.FSSrvOrdType.AllowInventoryItems : Edm.Boolean "AllowInventoryItems"
PX.Objects.FS.FSSrvOrdType.SetLotSerialNbrInAppts : Edm.Boolean "Copy Lot/Serial Nbrs. to Appointment from Service Order"
PX.Objects.FS.FSSrvOrdType.InventoryItemByDfltBillableTravelItem -> PX.Objects.IN.InventoryItem (DfltBillableTravelItem=InventoryID)
PX.Objects.FS.FSSrvOrdType.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.FS.FSSrvOrdType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSrvOrdType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSrvOrdType.SOOrderTypeByPostOrderType -> PX.Objects.SO.SOOrderType (PostOrderType=OrderType)
PX.Objects.FS.FSSrvOrdType.SOOrderTypeByPostOrderTypeNegativeBalance -> PX.Objects.SO.SOOrderType (PostOrderTypeNegativeBalance=OrderType)
PX.Objects.FS.FSSrvOrdType.SOOrderTypeByAllocationOrderType -> PX.Objects.SO.SOOrderType (AllocationOrderType=OrderType)
PX.Objects.FS.FSSrvOrdType.PMCostCodeByDfltCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.FS.FSSrvOrdType.NumberingBySrvOrdNumberingID -> PX.Objects.CS.Numbering (SrvOrdNumberingID=NumberingID)
PX.Objects.FS.FSSrvOrdType.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode
PX.Objects.FS.FSSrvOrdType.TermsByDfltTermIDARSO -> PX.Objects.CS.Terms (DfltTermIDARSO=TermsID)
PX.Objects.FS.FSSrvOrdType.TermsByDfltTermIDAP -> PX.Objects.CS.Terms (DfltTermIDAP=TermsID)
PX.Objects.FS.FSSrvOrdType.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.FS.FSSrvOrdType.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.FS.FSSrvOrdType.EPEarningTypeByDfltEarningType -> PX.Objects.EP.EPEarningType (DfltEarningType=TypeCD)
PX.Objects.FS.FSSrvOrdType.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.FS.FSSrvOrdType.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.FS.FSSrvOrdType.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.FSSrvOrdType.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.FS.FSSrvOrdType.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.FSSrvOrdType.FSAppointmentTaxTranCollection -> Collection(PX.Objects.FS.FSAppointmentTaxTran)
PX.Objects.FS.FSSrvOrdType.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSSrvOrdType.FSSetupCollection -> Collection(PX.Objects.FS.FSSetup)
PX.Objects.FS.FSSrvOrdType.FSServiceOrderTaxTranCollection -> Collection(PX.Objects.FS.FSServiceOrderTaxTran)
PX.Objects.FS.FSSrvOrdType.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.FSSrvOrdType.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.FSSrvOrdType.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.FS.FSSrvOrdType.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.Objects.FS.FSSrvOrdType.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.FS.FSSrvOrdType.FSAdjustCollection -> Collection(PX.Objects.FS.FSAdjust)
PX.Objects.FS.FSSrvOrdType.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.FSSrvOrdType.FSAppointmentResourceCollection -> Collection(PX.Objects.FS.FSAppointmentResource)
PX.Objects.FS.FSSrvOrdType.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.Objects.FS.FSSrvOrdType.FSCustomerBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerBillingSetup)
PX.Objects.FS.FSSrvOrdType.FSCustomerClassBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerClassBillingSetup)
PX.Objects.FS.FSSrvOrdType.FSRouteSetupCollection -> Collection(PX.Objects.FS.FSRouteSetup)
PX.Objects.FS.FSSrvOrdType.FSServiceTemplateCollection -> Collection(PX.Objects.FS.FSServiceTemplate)
PX.Objects.FS.FSSrvOrdType.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.FS.FSSrvOrdType.FSSOEmployeeCollection -> Collection(PX.Objects.FS.FSSOEmployee)
PX.Objects.FS.FSSrvOrdType.FSSOResourceCollection -> Collection(PX.Objects.FS.FSSOResource)
PX.Objects.FS.FSSrvOrdType.FSSrvOrdTypeProblemCollection -> Collection(PX.Objects.FS.FSSrvOrdTypeProblem)
PX.Objects.FS.FSSrvOrdType.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.FSSrvOrdType.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.Objects.FS.FSSrvOrdType.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.FS.FSSrvOrdType.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.FS.FSSrvOrdType.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.FS.FSSrvOrdType.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.FS.FSSrvOrdType.FSQuickProcessParametersCollection -> Collection(PX.Objects.FS.FSQuickProcessParameters)
PX.Objects.FS.FSSrvOrdType.SchedulerAppointmentCollection -> Collection(PX.Objects.FS.SchedulerAppointment)

# PX.Objects.FS.FSSrvOrdTypeProblem (EntityType)

Key: ProblemID, SrvOrdType
Entity sets: PX_Objects_FS_FSSrvOrdTypeProblem

PX.Objects.FS.FSSrvOrdTypeProblem.SrvOrdType : Edm.String [key]
PX.Objects.FS.FSSrvOrdTypeProblem.ProblemID : Edm.Int32 [key] "Problem ID"
PX.Objects.FS.FSSrvOrdTypeProblem.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSSrvOrdTypeProblem.CreatedByScreenID : Edm.String
PX.Objects.FS.FSSrvOrdTypeProblem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSrvOrdTypeProblem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSSrvOrdTypeProblem.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSSrvOrdTypeProblem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSSrvOrdTypeProblem.tstamp : Edm.Binary
PX.Objects.FS.FSSrvOrdTypeProblem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSSrvOrdTypeProblem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSSrvOrdTypeProblem.FSProblemByProblemID -> PX.Objects.FS.FSProblem (ProblemID=ProblemID)
PX.Objects.FS.FSSrvOrdTypeProblem.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.FSStaffSchedule (EntityType)

BaseType: PX.Objects.FS.FSSchedule
Key: CustomerID, RefNbr (inherited from PX.Objects.FS.FSSchedule)
Entity sets: PX_Objects_FS_FSStaffSchedule

PX.Objects.FS.FSStaffSchedule.StaffScheduleDescription : Edm.String "Description"
PX.Objects.FS.FSStaffSchedule.StartTime : Edm.DateTimeOffset "Start Time"
PX.Objects.FS.FSStaffSchedule.EndTime : Edm.DateTimeOffset "End Time"

# PX.Objects.FS.FSTimeSlot (EntityType)

Key: TimeSlotID
Entity sets: PX_Objects_FS_FSTimeSlot
Non-filterable, non-selectable: CustomID, CustomDateID, WrkEmployeeScheduleID, BranchLocationDesc, BranchLocationCD, CustomDateTimeStart, CustomDateTimeEnd, NoteText

PX.Objects.FS.FSTimeSlot.TimeSlotID : Edm.Int32 [key]
PX.Objects.FS.FSTimeSlot.BranchID : Edm.Int32 "Branch ID"
PX.Objects.FS.FSTimeSlot.BranchLocationID : Edm.Int32 "Branch Location ID"
PX.Objects.FS.FSTimeSlot.EmployeeID : Edm.Int32 "Employee ID"
PX.Objects.FS.FSTimeSlot.TimeStart : Edm.DateTimeOffset "Time Start"
PX.Objects.FS.FSTimeSlot.TimeEnd : Edm.DateTimeOffset "Time End"
PX.Objects.FS.FSTimeSlot.ScheduleID : Edm.Int32 "Schedule ID"
PX.Objects.FS.FSTimeSlot.RecordCount : Edm.Int32 "Record Count"
PX.Objects.FS.FSTimeSlot.ScheduleType : Edm.String
PX.Objects.FS.FSTimeSlot.GenerationID : Edm.Int32 "Generation ID"
PX.Objects.FS.FSTimeSlot.TimeDiff : Edm.Decimal "Time Difference"
PX.Objects.FS.FSTimeSlot.SlotLevel : Edm.Int32 [required] "Slot Level"
PX.Objects.FS.FSTimeSlot.CustomID : Edm.String
PX.Objects.FS.FSTimeSlot.CustomDateID : Edm.String
PX.Objects.FS.FSTimeSlot.WrkEmployeeScheduleID : Edm.String
PX.Objects.FS.FSTimeSlot.BranchLocationDesc : Edm.String
PX.Objects.FS.FSTimeSlot.BranchLocationCD : Edm.String
PX.Objects.FS.FSTimeSlot.CustomDateTimeStart : Edm.String
PX.Objects.FS.FSTimeSlot.CustomDateTimeEnd : Edm.String
PX.Objects.FS.FSTimeSlot.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSTimeSlot.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSTimeSlot.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSTimeSlot.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSTimeSlot.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSTimeSlot.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSTimeSlot.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSTimeSlot.NoteID : Edm.Guid
PX.Objects.FS.FSTimeSlot.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSTimeSlot.TimeStartUTC : Edm.DateTimeOffset "Time Start"
PX.Objects.FS.FSTimeSlot.TimeEndUTC : Edm.DateTimeOffset "Time End"
PX.Objects.FS.FSTimeSlot.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSTimeSlot.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSTimeSlot.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSVehicle (EntityType)

Label: "Equipment"
BaseType: PX.Objects.FS.FSEquipment
Key: RefNbr (inherited from PX.Objects.FS.FSEquipment)
Entity sets: PX_Objects_FS_FSVehicle

PX.Objects.FS.FSVehicle.VehicleTypeCD : Edm.String "VehicleTypeCD"

# PX.Objects.FS.FSVehicleType (EntityType)

Label: "Vehicle Type"
Key: VehicleTypeCD
Entity sets: PX_Objects_FS_FSVehicleType, VehicleType, FSVehicleType
Non-filterable, non-selectable: NoteText, VehicleTypeGICD

PX.Objects.FS.FSVehicleType.VehicleTypeID : Edm.Int32
PX.Objects.FS.FSVehicleType.VehicleTypeCD : Edm.String [key] "Vehicle Type ID"
PX.Objects.FS.FSVehicleType.Descr : Edm.String "Description"
PX.Objects.FS.FSVehicleType.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSVehicleType.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSVehicleType.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSVehicleType.CreatedByScreenID : Edm.String
PX.Objects.FS.FSVehicleType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSVehicleType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.FS.FSVehicleType.LastModifiedByScreenID : Edm.String
PX.Objects.FS.FSVehicleType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSVehicleType.tstamp : Edm.Binary
PX.Objects.FS.FSVehicleType.VehicleTypeGICD : Edm.String "Vehicle Type"
PX.Objects.FS.FSVehicleType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSVehicleType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSVehicleType.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.FS.FSVehicleType.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.FSVehicleType.FSRouteCollection -> Collection(PX.Objects.FS.FSRoute)
PX.Objects.FS.FSVehicleType.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)

# PX.Objects.FS.FSWeekCodeDate (EntityType)

Label: "Contracts/Routes calendar Week Code"
Key: WeekCodeDate
Entity sets: PX_Objects_FS_FSWeekCodeDate, ContractsRoutescalendarWeekCode, FSWeekCodeDate

PX.Objects.FS.FSWeekCodeDate.WeekCodeDate : Edm.DateTimeOffset [key] "Date"
PX.Objects.FS.FSWeekCodeDate.WeekCode : Edm.String "Week Code"
PX.Objects.FS.FSWeekCodeDate.WeekCodeP1 : Edm.String "Week Code P1"
PX.Objects.FS.FSWeekCodeDate.WeekCodeP2 : Edm.String "Week Code P2"
PX.Objects.FS.FSWeekCodeDate.WeekCodeP3 : Edm.String "Week Code P3"
PX.Objects.FS.FSWeekCodeDate.WeekCodeP4 : Edm.String "Week Code P4"
PX.Objects.FS.FSWeekCodeDate.BeginDateOfWeek : Edm.DateTimeOffset "Start Date of Week"
PX.Objects.FS.FSWeekCodeDate.EndDateOfWeek : Edm.DateTimeOffset "End Date of Week"
PX.Objects.FS.FSWeekCodeDate.DayOfWeek : Edm.Int32 "Day of Week"
PX.Objects.FS.FSWeekCodeDate.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSWeekCodeDate.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSWeekCodeDate.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSWeekCodeDate.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSWeekCodeDate.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSWeekCodeDate.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSWeekCodeDate.tstamp : Edm.Binary
PX.Objects.FS.FSWeekCodeDate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSWeekCodeDate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.FS.FSWFStage (EntityType)

Label: "Order Stage"
Key: ParentWFStageID, WFID, WFStageCD
Entity sets: PX_Objects_FS_FSWFStage, OrderStage, FSWFStage
Non-filterable, non-selectable: NoteText

PX.Objects.FS.FSWFStage.WFID : Edm.Int32 [key] "Workflow ID"
PX.Objects.FS.FSWFStage.ParentWFStageID : Edm.Int32 [key] "Parent Workflow Stage ID"
PX.Objects.FS.FSWFStage.WFStageID : Edm.Int32 "Workflow Stage ID"
PX.Objects.FS.FSWFStage.WFStageCD : Edm.String [key] "Workflow Stage ID"
PX.Objects.FS.FSWFStage.AllowCancel : Edm.Boolean [required] "Allow Cancel"
PX.Objects.FS.FSWFStage.AllowDelete : Edm.Boolean [required] "Allow Delete"
PX.Objects.FS.FSWFStage.AllowModify : Edm.Boolean [required] "Allow Update"
PX.Objects.FS.FSWFStage.AllowPost : Edm.Boolean [required] "Allow Post"
PX.Objects.FS.FSWFStage.AllowComplete : Edm.Boolean [required] "Allow Complete"
PX.Objects.FS.FSWFStage.AllowReopen : Edm.Boolean [required] "Allow Reopen"
PX.Objects.FS.FSWFStage.AllowClose : Edm.Boolean [required] "Allow Close"
PX.Objects.FS.FSWFStage.Descr : Edm.String "Description"
PX.Objects.FS.FSWFStage.RequireReason : Edm.Boolean [required] "Require Reason"
PX.Objects.FS.FSWFStage.SortOrder : Edm.Int32 [required] "Sort Order"
PX.Objects.FS.FSWFStage.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.FSWFStage.NoteText : Edm.String "Note Text"
PX.Objects.FS.FSWFStage.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.FS.FSWFStage.CreatedByScreenID : Edm.String "CreatedByScreenID"
PX.Objects.FS.FSWFStage.CreatedDateTime : Edm.DateTimeOffset "CreatedDateTime"
PX.Objects.FS.FSWFStage.LastModifiedByID : Edm.Guid "LastModifiedByID"
PX.Objects.FS.FSWFStage.LastModifiedByScreenID : Edm.String "LastModifiedByScreenID"
PX.Objects.FS.FSWFStage.LastModifiedDateTime : Edm.DateTimeOffset "LastModifiedDateTime"
PX.Objects.FS.FSWFStage.tstamp : Edm.Binary "tstamp"
PX.Objects.FS.FSWFStage.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSWFStage.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.FS.FSWFStage.FSWFStageByWFStageID -> PX.Objects.FS.FSWFStage (WFStageID=ParentWFStageID)
PX.Objects.FS.FSWFStage.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.FS.FSWFStage.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.FSWFStage.FSWFStageCollection -> Collection(PX.Objects.FS.FSWFStage)

# PX.Objects.FS.FSWrkProcess (EntityType)

Label: "FSWrkProcess"
Key: ProcessID
Entity sets: PX_Objects_FS_FSWrkProcess, FSWrkProcess

PX.Objects.FS.FSWrkProcess.ProcessID : Edm.Int32 [key] "ProcessID"
PX.Objects.FS.FSWrkProcess.SrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.FSWrkProcess.SOID : Edm.Int32 "Service Order ID"
PX.Objects.FS.FSWrkProcess.AppointmentID : Edm.Int32 "Appointment ID"
PX.Objects.FS.FSWrkProcess.BranchID : Edm.Int32 "Branch ID"
PX.Objects.FS.FSWrkProcess.BranchLocationID : Edm.Int32 "Branch Location ID"
PX.Objects.FS.FSWrkProcess.CustomerID : Edm.Int32 "Customer ID"
PX.Objects.FS.FSWrkProcess.RoomID : Edm.String "Room ID"
PX.Objects.FS.FSWrkProcess.ScheduledDateTimeBegin : Edm.DateTimeOffset "Scheduled Date Time Begin"
PX.Objects.FS.FSWrkProcess.ScheduledDateTimeEnd : Edm.DateTimeOffset "Scheduled Date Time End"
PX.Objects.FS.FSWrkProcess.LineRefList : Edm.String "Ref. Nbr. List"
PX.Objects.FS.FSWrkProcess.EmployeeIDList : Edm.String "Employee ID List"
PX.Objects.FS.FSWrkProcess.EquipmentIDList : Edm.String "Equipment ID List"
PX.Objects.FS.FSWrkProcess.TargetScreenID : Edm.String "Target Screen ID"
PX.Objects.FS.FSWrkProcess.ExtraParms : Edm.String "Extra Parameters"
PX.Objects.FS.FSWrkProcess.SMEquipmentID : Edm.Int32
PX.Objects.FS.FSWrkProcess.CreatedByID : Edm.Guid "Created By"
PX.Objects.FS.FSWrkProcess.CreatedByScreenID : Edm.String
PX.Objects.FS.FSWrkProcess.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.FS.FSWrkProcess.tstamp : Edm.Binary
PX.Objects.FS.FSWrkProcess.ScheduledDateTimeBeginUTC : Edm.DateTimeOffset "Scheduled Date Time Begin"
PX.Objects.FS.FSWrkProcess.ScheduledDateTimeEndUTC : Edm.DateTimeOffset "Scheduled Date Time End"
PX.Objects.FS.FSWrkProcess.SiteMapByTargetScreenID -> PX.SM.SiteMap (TargetScreenID=ScreenID)
PX.Objects.FS.FSWrkProcess.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.FSWrkProcess.FSEquipmentBySmEquipmentID -> PX.Objects.FS.FSEquipment
PX.Objects.FS.FSWrkProcess.FSAppointmentByAppointmentID -> PX.Objects.FS.FSAppointment (AppointmentID=AppointmentID)
PX.Objects.FS.FSWrkProcess.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.FS.FSWrkProcess.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.FS.FSWrkProcess.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.FSWrkProcess.FSRoomByRoomID -> PX.Objects.FS.FSRoom (BranchLocationID=BranchLocationID, RoomID=RoomID)
PX.Objects.FS.FSWrkProcess.FSServiceOrderBySOID -> PX.Objects.FS.FSServiceOrder (SOID=SOID)
PX.Objects.FS.FSWrkProcess.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)

# PX.Objects.FS.InventoryPostingBatchDetail (EntityType)

BaseType: PX.Objects.FS.PostingBatchDetail
Key: AppointmentRefNbr, BatchID, SrvOrdType (inherited from PX.Objects.FS.PostingBatchDetail)
Entity sets: PX_Objects_FS_InventoryPostingBatchDetail

PX.Objects.FS.InventoryPostingBatchDetail.AppointmentInventoryItemID : Edm.Int32
PX.Objects.FS.InventoryPostingBatchDetail.SODetID : Edm.Int32 "Service Order Detail Ref. Nbr."
PX.Objects.FS.InventoryPostingBatchDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.FS.InventoryPostingBatchDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.InventoryPostingBatchDetail.FSSODetByAppointmentID -> PX.Objects.FS.FSSODet (SODetID=SODetID, AppointmentID=SOID)
PX.Objects.FS.InventoryPostingBatchDetail.InventoryItemByPickupDeliveryServiceID -> PX.Objects.IN.InventoryItem
PX.Objects.FS.InventoryPostingBatchDetail.FSSODetBySODetID -> PX.Objects.FS.FSSODet (SODetID=SODetID)

# PX.Objects.FS.LicenseTypeGridFilter (EntityType)

Label: "License Type"
BaseType: PX.Objects.FS.FSLicenseType
Key: LicenseTypeCD (inherited from PX.Objects.FS.FSLicenseType)
Entity sets: PX_Objects_FS_LicenseTypeGridFilter

# PX.Objects.FS.POEnabledFSSODet (EntityType)

Label: "Service Order Item Detail"
BaseType: PX.Objects.FS.FSSODet
Key: LineNbr, RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSSODet)
Entity sets: PX_Objects_FS_POEnabledFSSODet
Non-filterable, non-selectable: PONbrCreated

PX.Objects.FS.POEnabledFSSODet.SrvBranchID : Edm.Int32 "Branch"
PX.Objects.FS.POEnabledFSSODet.SrvBranchLocationID : Edm.Int32 "Branch Location ID"
PX.Objects.FS.POEnabledFSSODet.InventoryItemClassID : Edm.Int32 "Item Class"
PX.Objects.FS.POEnabledFSSODet.OrderDate : Edm.DateTimeOffset "Requested on"
PX.Objects.FS.POEnabledFSSODet.SrvCustomerID : Edm.Int32 "Customer ID"
PX.Objects.FS.POEnabledFSSODet.PONbrCreated : Edm.String "PO Nbr."
PX.Objects.FS.POEnabledFSSODet.POVendorID : Edm.Int32 "Vendor ID"
PX.Objects.FS.POEnabledFSSODet.SrvCuryUnitCost : Edm.Decimal "Unit Cost"
PX.Objects.FS.POEnabledFSSODet.BAccountBySrvCustomerID -> PX.Objects.CR.BAccount (SrvCustomerID=BAccountID)
PX.Objects.FS.POEnabledFSSODet.CustomerBySrvCustomerID -> PX.Objects.AR.Customer (SrvCustomerID=BAccountID)
PX.Objects.FS.POEnabledFSSODet.BranchBySrvBranchID -> PX.Objects.GL.Branch (SrvBranchID=BranchID)
PX.Objects.FS.POEnabledFSSODet.INItemClassByInventoryItemClassID -> PX.Objects.IN.INItemClass (InventoryItemClassID=ItemClassID)
PX.Objects.FS.POEnabledFSSODet.LocationBySrvLocationID -> PX.Objects.CR.Location (SrvCustomerID=BAccountID)
PX.Objects.FS.POEnabledFSSODet.FSBranchLocationBySrvBranchLocationID -> PX.Objects.FS.FSBranchLocation (SrvBranchLocationID=BranchLocationID)
PX.Objects.FS.POEnabledFSSODet.FSBranchLocationBySrvBranchID -> PX.Objects.FS.FSBranchLocation (SrvBranchLocationID=BranchLocationID, SrvBranchID=BranchID)

# PX.Objects.FS.PostingBatchDetail (EntityType)

Key: AppointmentRefNbr, BatchID, SrvOrdType
Entity sets: PX_Objects_FS_PostingBatchDetail
Non-filterable, non-selectable: SOPosted, SOOrderType, SOOrderNbr, SOLineNbr, ARPosted, ARDocType, ARRefNbr, ARLineNbr, APPosted, APDocType, APRefNbr, APLineNbr, INPosted, INDocType, INRefNbr, INLineNbr, SOInvPosted, SOInvDocType, SOInvRefNbr, SOInvLineNbr, PMPosted, PMDocType, PMRefNbr, PMTranID, AcctName, InvoiceRefNbr

PX.Objects.FS.PostingBatchDetail.BatchID : Edm.Int32 [key] "Batch ID"
PX.Objects.FS.PostingBatchDetail.PostDetID : Edm.Int32
PX.Objects.FS.PostingBatchDetail.PostedTO : Edm.String
PX.Objects.FS.PostingBatchDetail.PostDocType : Edm.String
PX.Objects.FS.PostingBatchDetail.PostRefNbr : Edm.String
PX.Objects.FS.PostingBatchDetail.SOPosted : Edm.Boolean "Invoiced through Sales Order"
PX.Objects.FS.PostingBatchDetail.SOOrderType : Edm.String "Sales Order Type"
PX.Objects.FS.PostingBatchDetail.SOOrderNbr : Edm.String "Sales Order Nbr."
PX.Objects.FS.PostingBatchDetail.SOLineNbr : Edm.Int32 "Sales Order Line Nbr."
PX.Objects.FS.PostingBatchDetail.ARPosted : Edm.Boolean "Invoiced through AR"
PX.Objects.FS.PostingBatchDetail.ARDocType : Edm.String "AR Document Type"
PX.Objects.FS.PostingBatchDetail.ARRefNbr : Edm.String "AR Reference Nbr."
PX.Objects.FS.PostingBatchDetail.ARLineNbr : Edm.Int32 "AR Line Nbr."
PX.Objects.FS.PostingBatchDetail.APPosted : Edm.Boolean "Invoiced through AP"
PX.Objects.FS.PostingBatchDetail.APDocType : Edm.String "AP Document Type"
PX.Objects.FS.PostingBatchDetail.APRefNbr : Edm.String "AP Reference Nbr."
PX.Objects.FS.PostingBatchDetail.APLineNbr : Edm.Int32 "AP Line Nbr."
PX.Objects.FS.PostingBatchDetail.INPosted : Edm.Boolean "Invoiced through IN"
PX.Objects.FS.PostingBatchDetail.INDocType : Edm.String "IN Document Type"
PX.Objects.FS.PostingBatchDetail.INRefNbr : Edm.String "IN Reference Nbr."
PX.Objects.FS.PostingBatchDetail.INLineNbr : Edm.Int32 "IN Line Nbr."
PX.Objects.FS.PostingBatchDetail.SOInvPosted : Edm.Boolean "Invoiced through SO Invoice"
PX.Objects.FS.PostingBatchDetail.SOInvDocType : Edm.String "SO Invoice Document Type"
PX.Objects.FS.PostingBatchDetail.SOInvRefNbr : Edm.String "SO Invoice Ref. Nbr."
PX.Objects.FS.PostingBatchDetail.SOInvLineNbr : Edm.Int32 "SO Invoice Line Nbr."
PX.Objects.FS.PostingBatchDetail.PMPosted : Edm.Boolean "Invoiced through PM"
PX.Objects.FS.PostingBatchDetail.PMDocType : Edm.String "PM Document Type"
PX.Objects.FS.PostingBatchDetail.PMRefNbr : Edm.String "PM Reference Nbr."
PX.Objects.FS.PostingBatchDetail.PMTranID : Edm.Int64 "PM Tran ID"
PX.Objects.FS.PostingBatchDetail.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.PostingBatchDetail.AppointmentRefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.PostingBatchDetail.SORefNbr : Edm.String "Service Order Nbr."
PX.Objects.FS.PostingBatchDetail.BillCustomerID : Edm.Int32 "Billing Customer ID"
PX.Objects.FS.PostingBatchDetail.ActualDateTimeBegin : Edm.DateTimeOffset "Actual Date"
PX.Objects.FS.PostingBatchDetail.ActualDateTimeEnd : Edm.DateTimeOffset "Actual Date End"
PX.Objects.FS.PostingBatchDetail.BranchLocationID : Edm.Int32 "Branch Location ID"
PX.Objects.FS.PostingBatchDetail.GeoZoneCD : Edm.String "Service Area ID"
PX.Objects.FS.PostingBatchDetail.DocDesc : Edm.String "Description"
PX.Objects.FS.PostingBatchDetail.SOID : Edm.Int32 "Service Order ID"
PX.Objects.FS.PostingBatchDetail.AppointmentID : Edm.Int32
PX.Objects.FS.PostingBatchDetail.NoteID : Edm.Guid "NoteID"
PX.Objects.FS.PostingBatchDetail.AcctName : Edm.String "Customer Name"
PX.Objects.FS.PostingBatchDetail.InvoiceRefNbr : Edm.String "Invoice Nbr."
PX.Objects.FS.PostingBatchDetail.CustomerByBillCustomerID -> PX.Objects.AR.Customer (BillCustomerID=BAccountID)
PX.Objects.FS.PostingBatchDetail.FSAppointmentByAppointmentRefNbr -> PX.Objects.FS.FSAppointment (SrvOrdType=SrvOrdType, AppointmentRefNbr=RefNbr)
PX.Objects.FS.PostingBatchDetail.FSGeoZoneByGeoZoneCD -> PX.Objects.SV.FSGeoZone (GeoZoneCD=GeoZoneCD)
PX.Objects.FS.PostingBatchDetail.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.PostingBatchDetail.FSPostBatchByBatchID -> PX.Objects.FS.FSPostBatch (BatchID=BatchNbr)
PX.Objects.FS.PostingBatchDetail.FSServiceOrderBySORefNbr -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType, SORefNbr=RefNbr)
PX.Objects.FS.PostingBatchDetail.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.PostingBatchDetail.CustomerByCustomerID -> PX.Objects.AR.Customer
PX.Objects.FS.PostingBatchDetail.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.PostingBatchDetail.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.PostingBatchDetail.FSAppointmentResourceCollection -> Collection(PX.Objects.FS.FSAppointmentResource)
PX.Objects.FS.PostingBatchDetail.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.PostingBatchDetail.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.PostingBatchDetail.FSPostDocCollection -> Collection(PX.Objects.FS.FSPostDoc)
PX.Objects.FS.PostingBatchDetail.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.FS.PostingBatchDetail.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.PostingBatchDetail.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.Objects.FS.PostingBatchDetail.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.FS.PostingBatchDetail.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.FS.PostingBatchDetail.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.PostingBatchDetail.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.PostingBatchDetail.FSSOResourceCollection -> Collection(PX.Objects.FS.FSSOResource)

# PX.Objects.FS.RelatedServiceOrder (EntityType)

Label: "Service Order"
BaseType: PX.Objects.FS.FSServiceOrder
Key: RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSServiceOrder)
Entity sets: PX_Objects_FS_RelatedServiceOrder

# PX.Objects.FS.RouteAppointmentInfo (EntityType)

Label: "Appointment"
BaseType: PX.Objects.FS.FSAppointment
Key: RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSAppointment)
Entity sets: PX_Objects_FS_RouteAppointmentInfo

PX.Objects.FS.RouteAppointmentInfo.EmployeeID : Edm.Int32 "Staff Member ID"
PX.Objects.FS.RouteAppointmentInfo.State : Edm.String "State"
PX.Objects.FS.RouteAppointmentInfo.Priority : Edm.String "Priority"
PX.Objects.FS.RouteAppointmentInfo.ServiceID : Edm.Int32
PX.Objects.FS.RouteAppointmentInfo.SODetID : Edm.Int32 "Service Order Detail Ref. Nbr."
PX.Objects.FS.RouteAppointmentInfo.GeoZoneID : Edm.Int32 "Geographical Zone ID"
PX.Objects.FS.RouteAppointmentInfo.BranchLocationID : Edm.Int32 "Branch Location ID"
PX.Objects.FS.RouteAppointmentInfo.RoomID : Edm.String "Room"
PX.Objects.FS.RouteAppointmentInfo.CustomerBillingCycleID : Edm.Int32 "Billing Cycle ID"
PX.Objects.FS.RouteAppointmentInfo.CustomerBillingSrvOrdType : Edm.String "Service Order Type"
PX.Objects.FS.RouteAppointmentInfo.FSxCustomerBillingCycleID : Edm.Int32 "Billing Cycle ID"
PX.Objects.FS.RouteAppointmentInfo.SLAETA : Edm.DateTimeOffset "Deadline - SLA"
PX.Objects.FS.RouteAppointmentInfo.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.FS.RouteAppointmentInfo.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.FS.RouteAppointmentInfo.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.FS.RouteAppointmentInfo.PostalCode : Edm.String "Postal code"
PX.Objects.FS.RouteAppointmentInfo.City : Edm.String "City"
PX.Objects.FS.RouteAppointmentInfo.BAccountByEmployeeID -> PX.Objects.CR.BAccount (EmployeeID=BAccountID)
PX.Objects.FS.RouteAppointmentInfo.InventoryItemByServiceID -> PX.Objects.IN.InventoryItem (ServiceID=InventoryID)
PX.Objects.FS.RouteAppointmentInfo.FSGeoZoneByGeoZoneID -> PX.Objects.SV.FSGeoZone (GeoZoneID=GeoZoneID)
PX.Objects.FS.RouteAppointmentInfo.FSSODetBySODetID -> PX.Objects.FS.FSSODet (SODetID=SODetID)
PX.Objects.FS.RouteAppointmentInfo.FSSODetBySOID -> PX.Objects.FS.FSSODet (SODetID=SODetID, SOID=SOID)
PX.Objects.FS.RouteAppointmentInfo.StateByState -> PX.Objects.CS.State (State=StateID)
PX.Objects.FS.RouteAppointmentInfo.LocationByLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.FS.RouteAppointmentInfo.LocationByBillLocationID -> PX.Objects.CR.Location (BillCustomerID=BAccountID)
PX.Objects.FS.RouteAppointmentInfo.FSBillingCycleByCustomerBillingCycleID -> PX.Objects.FS.FSBillingCycle (CustomerBillingCycleID=BillingCycleID)
PX.Objects.FS.RouteAppointmentInfo.FSBillingCycleByFsxCustomerBillingCycleID -> PX.Objects.FS.FSBillingCycle
PX.Objects.FS.RouteAppointmentInfo.FSBranchLocationByBranchLocationID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID)
PX.Objects.FS.RouteAppointmentInfo.FSRoomByRoomID -> PX.Objects.FS.FSRoom (BranchLocationID=BranchLocationID, RoomID=RoomID)
PX.Objects.FS.RouteAppointmentInfo.FSSrvOrdTypeByCustomerBillingSrvOrdType -> PX.Objects.FS.FSSrvOrdType (CustomerBillingSrvOrdType=SrvOrdType)
PX.Objects.FS.RouteAppointmentInfo.BAccountByAssignedEmpID -> PX.Objects.CR.BAccount
PX.Objects.FS.RouteAppointmentInfo.FSBranchLocationByBranchID -> PX.Objects.FS.FSBranchLocation (BranchLocationID=BranchLocationID, BranchID=BranchID)
PX.Objects.FS.RouteAppointmentInfo.FSRoomByBranchLocationID -> PX.Objects.FS.FSRoom (RoomID=RoomID, BranchLocationID=BranchLocationID)

# PX.Objects.FS.SchedulerAppointment (EntityType)

Label: "Appointment"
Key: RefNbr, SrvOrdType
Entity sets: PX_Objects_FS_SchedulerAppointment, Appointment1, SchedulerAppointment
Non-filterable, non-selectable: Locked

PX.Objects.FS.SchedulerAppointment.AppointmentID : Edm.Int32
PX.Objects.FS.SchedulerAppointment.RefNbr : Edm.String [key] "Appointment Nbr."
PX.Objects.FS.SchedulerAppointment.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.SchedulerAppointment.SORefNbr : Edm.String "Order Nbr."
PX.Objects.FS.SchedulerAppointment.SOID : Edm.Int32
PX.Objects.FS.SchedulerAppointment.Status : Edm.String "Appointment Status"
PX.Objects.FS.SchedulerAppointment.Closed : Edm.Boolean "Closed"
PX.Objects.FS.SchedulerAppointment.Canceled : Edm.Boolean "Canceled"
PX.Objects.FS.SchedulerAppointment.Completed : Edm.Boolean "Completed"
PX.Objects.FS.SchedulerAppointment.Billed : Edm.Boolean "Billed"
PX.Objects.FS.SchedulerAppointment.Confirmed : Edm.Boolean "Confirmed"
PX.Objects.FS.SchedulerAppointment.ValidatedByDispatcher : Edm.Boolean "Validated by Dispatcher"
PX.Objects.FS.SchedulerAppointment.ScheduledDateTimeBegin : Edm.DateTimeOffset "Scheduled Start Date"
PX.Objects.FS.SchedulerAppointment.ScheduledDateTimeEnd : Edm.DateTimeOffset "Scheduled End Date"
PX.Objects.FS.SchedulerAppointment.DocDesc : Edm.String "Description"
PX.Objects.FS.SchedulerAppointment.LongDescr : Edm.String "Other"
PX.Objects.FS.SchedulerAppointment.MapLatitude : Edm.Decimal "Latitude"
PX.Objects.FS.SchedulerAppointment.MapLongitude : Edm.Decimal "Longitude"
PX.Objects.FS.SchedulerAppointment.EstimatedDurationTotal : Edm.Int32 "Estimated Duration"
PX.Objects.FS.SchedulerAppointment.StaffCntr : Edm.Int32 "Multiple Staff Members"
PX.Objects.FS.SchedulerAppointment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.SchedulerAppointment.IsVisible : Edm.Boolean
PX.Objects.FS.SchedulerAppointment.BandColor : Edm.String
PX.Objects.FS.SchedulerAppointment.Locked : Edm.Boolean "Locked"
PX.Objects.FS.SchedulerAppointment.FSAppointmentByRefNbr -> PX.Objects.FS.FSAppointment (RefNbr=RefNbr)
PX.Objects.FS.SchedulerAppointment.FSServiceOrderBySoRefNbr -> PX.Objects.FS.FSServiceOrder
PX.Objects.FS.SchedulerAppointment.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.SchedulerAppointment.FSServiceOrderBySrvOrdType -> PX.Objects.FS.FSServiceOrder (SrvOrdType=SrvOrdType)
PX.Objects.FS.SchedulerAppointment.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.SchedulerAppointment.FSAppointmentResourceCollection -> Collection(PX.Objects.FS.FSAppointmentResource)
PX.Objects.FS.SchedulerAppointment.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.SchedulerAppointment.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.FS.SchedulerAppointment.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.SchedulerAppointment.FSAppointmentTaxTranCollection -> Collection(PX.Objects.FS.FSAppointmentTaxTran)
PX.Objects.FS.SchedulerAppointment.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.FS.SchedulerAppointment.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.SchedulerAppointment.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.FS.SchedulerAppointment.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.FS.SchedulerAppointment.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.Objects.FS.SchedulerAppointment.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.SchedulerAppointment.FSPostDocCollection -> Collection(PX.Objects.FS.FSPostDoc)
PX.Objects.FS.SchedulerAppointment.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.FS.SchedulerAppointment.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.SchedulerAppointment.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.Objects.FS.SchedulerAppointment.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.FS.SchedulerAppointment.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.FS.SchedulerAppointment.SchedulerAppointmentCollection -> Collection(PX.Objects.FS.SchedulerAppointment)

# PX.Objects.FS.SchedulerEmployeeInventoryItem (EntityType)

Label: "Employee Inventory Item"
Key: InventoryID
Entity sets: PX_Objects_FS_SchedulerEmployeeInventoryItem, EmployeeInventoryItem, SchedulerEmployeeInventoryItem

PX.Objects.FS.SchedulerEmployeeInventoryItem.InventoryID : Edm.Int32 [key] "Employee Service Type"
PX.Objects.FS.SchedulerEmployeeInventoryItem.InventoryCD : Edm.String
PX.Objects.FS.SchedulerEmployeeInventoryItem.ItemStatus : Edm.String
PX.Objects.FS.SchedulerEmployeeInventoryItem.ItemType : Edm.String
PX.Objects.FS.SchedulerEmployeeInventoryItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.FS.SchedulerEmployeeInventoryItem.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSAppointmentLogExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentLogExtItemLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.FS.SchedulerEmployeeInventoryItem.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INMatrixExcludedDataCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
PX.Objects.FS.SchedulerEmployeeInventoryItem.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.FS.SchedulerEmployeeInventoryItem.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.InventoryPostingBatchDetailCollection -> Collection(PX.Objects.FS.InventoryPostingBatchDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.Objects.FS.SchedulerEmployeeInventoryItem.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.FS.SchedulerEmployeeInventoryItem.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.FS.SchedulerEmployeeInventoryItem.InventoryItemLotSerNumValCollection -> Collection(PX.Objects.IN.InventoryItemLotSerNumVal)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INRelatedInventoryUserFeedbackCollection -> Collection(PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INAttributeDescriptionGroupCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.FS.SchedulerEmployeeInventoryItem.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.FS.SchedulerEmployeeInventoryItem.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.FS.SchedulerEmployeeInventoryItem.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.FS.SchedulerEmployeeInventoryItem.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.FS.SchedulerEmployeeInventoryItem.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.FS.SchedulerEmployeeInventoryItem.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Objects.FS.SchedulerEmployeeInventoryItem.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSServiceInventoryItemCollection -> Collection(PX.Objects.FS.FSServiceInventoryItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.FS.SchedulerEmployeeInventoryItem.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.FS.SchedulerEmployeeInventoryItem.POLineRCollection -> Collection(PX.Objects.PO.POLineR)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMItemRateCollection -> Collection(PX.Objects.PM.PMItemRate)
PX.Objects.FS.SchedulerEmployeeInventoryItem.PMProjectARTranPostDetailCollection -> Collection(PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemLotSerialCollection -> Collection(PX.Objects.IN.INItemLotSerial)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemSalesHistCollection -> Collection(PX.Objects.IN.INItemSalesHist)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INSubItemSegmentValueCollection -> Collection(PX.Objects.IN.INSubItemSegmentValue)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.FS.SchedulerEmployeeInventoryItem.RelatedItemCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeader)
PX.Objects.FS.SchedulerEmployeeInventoryItem.BCInventoryFileUrlsCollection -> Collection(PX.Commerce.Objects.BCInventoryFileUrls)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.FS.SchedulerEmployeeInventoryItem.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.FS.SchedulerEmployeeInventoryItem.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.FS.SchedulerEmployeeInventoryItem.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SchedulerEmployeeInventoryItemCollection -> Collection(PX.Objects.FS.SchedulerEmployeeInventoryItem)
PX.Objects.FS.SchedulerEmployeeInventoryItem.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.FS.SchedulerEmployeeInventoryItem.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.FS.SchedulerServiceOrder (EntityType)

Label: "Service Order"
Key: BranchCD, BranchLocationCD, CustomerAcctCD, ProblemCD, ServiceContractRefNbr, SrvOrdType
Entity sets: PX_Objects_FS_SchedulerServiceOrder, ServiceOrder1, SchedulerServiceOrder
Non-filterable, non-selectable: FullAddress

PX.Objects.FS.SchedulerServiceOrder.SrvOrdType : Edm.String [key] "Service Order Type"
PX.Objects.FS.SchedulerServiceOrder.SOID : Edm.Int32
PX.Objects.FS.SchedulerServiceOrder.RefNbr : Edm.String "Service Order Nbr."
PX.Objects.FS.SchedulerServiceOrder.Status : Edm.String "Service Order Status"
PX.Objects.FS.SchedulerServiceOrder.RoomID : Edm.String "Room ID"
PX.Objects.FS.SchedulerServiceOrder.CustomerID : Edm.Int32 "Customer"
PX.Objects.FS.SchedulerServiceOrder.ContactID : Edm.Int32 "Contact"
PX.Objects.FS.SchedulerServiceOrder.EstimatedDurationTotal : Edm.Int32 "Estimated Duration"
PX.Objects.FS.SchedulerServiceOrder.Priority : Edm.String "Priority"
PX.Objects.FS.SchedulerServiceOrder.Severity : Edm.String "Severity"
PX.Objects.FS.SchedulerServiceOrder.DocDesc : Edm.String "Description"
PX.Objects.FS.SchedulerServiceOrder.SLAETA : Edm.DateTimeOffset "SLA"
PX.Objects.FS.SchedulerServiceOrder.CustPORefNbr : Edm.String "Customer Order"
PX.Objects.FS.SchedulerServiceOrder.PendingPOLineCntr : Edm.Int32
PX.Objects.FS.SchedulerServiceOrder.OrderDate : Edm.DateTimeOffset "Date"
PX.Objects.FS.SchedulerServiceOrder.SourceType : Edm.String "Document Type"
PX.Objects.FS.SchedulerServiceOrder.AssignedEmpID : Edm.Int32 "Supervisor"
PX.Objects.FS.SchedulerServiceOrder.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.FS.SchedulerServiceOrder.ServiceOrderContactID : Edm.Int32
PX.Objects.FS.SchedulerServiceOrder.ServiceOrderAddressID : Edm.Int32
PX.Objects.FS.SchedulerServiceOrder.ProblemID : Edm.Int32
PX.Objects.FS.SchedulerServiceOrder.ServiceContractID : Edm.Int32
PX.Objects.FS.SchedulerServiceOrder.Quote : Edm.Boolean
PX.Objects.FS.SchedulerServiceOrder.Hold : Edm.Boolean
PX.Objects.FS.SchedulerServiceOrder.Closed : Edm.Boolean
PX.Objects.FS.SchedulerServiceOrder.Canceled : Edm.Boolean
PX.Objects.FS.SchedulerServiceOrder.Completed : Edm.Boolean
PX.Objects.FS.SchedulerServiceOrder.AppointmentsNeeded : Edm.Boolean
PX.Objects.FS.SchedulerServiceOrder.CustomerAcctCD : Edm.String [key] "Customer ID"
PX.Objects.FS.SchedulerServiceOrder.CustomerAcctName : Edm.String "Customer Name"
PX.Objects.FS.SchedulerServiceOrder.CustomerClassID : Edm.String "Customer Class"
PX.Objects.FS.SchedulerServiceOrder.Phone1 : Edm.String "Phone 1"
PX.Objects.FS.SchedulerServiceOrder.ContactDisplayName : Edm.String "Display Name"
PX.Objects.FS.SchedulerServiceOrder.Title : Edm.String
PX.Objects.FS.SchedulerServiceOrder.FirstName : Edm.String
PX.Objects.FS.SchedulerServiceOrder.LastName : Edm.String
PX.Objects.FS.SchedulerServiceOrder.MidName : Edm.String
PX.Objects.FS.SchedulerServiceOrder.Email : Edm.String "Email"
PX.Objects.FS.SchedulerServiceOrder.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.FS.SchedulerServiceOrder.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.FS.SchedulerServiceOrder.City : Edm.String "City"
PX.Objects.FS.SchedulerServiceOrder.CountryID : Edm.String "Country"
PX.Objects.FS.SchedulerServiceOrder.State : Edm.String "State"
PX.Objects.FS.SchedulerServiceOrder.PostalCode : Edm.String "Postal Code"
PX.Objects.FS.SchedulerServiceOrder.FullAddress : Edm.String "Address"
PX.Objects.FS.SchedulerServiceOrder.BranchCD : Edm.String [key] "Branch ID"
PX.Objects.FS.SchedulerServiceOrder.BranchName : Edm.String "Branch Name"
PX.Objects.FS.SchedulerServiceOrder.BranchLocationCD : Edm.String [key] "Branch Location ID"
PX.Objects.FS.SchedulerServiceOrder.BranchLocationDescr : Edm.String "Branch Location Description"
PX.Objects.FS.SchedulerServiceOrder.ProblemCD : Edm.String [key] "Problem ID"
PX.Objects.FS.SchedulerServiceOrder.ProblemDescr : Edm.String "Problem Description"
PX.Objects.FS.SchedulerServiceOrder.ServiceContractRefNbr : Edm.String [key] "Service Contract"
PX.Objects.FS.SchedulerServiceOrder.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.FS.SchedulerServiceOrder.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.FS.SchedulerServiceOrder.BranchByBranchCD -> PX.Objects.GL.Branch (BranchCD=BranchCD)
PX.Objects.FS.SchedulerServiceOrder.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass (CustomerClassID=CustomerClassID)
PX.Objects.FS.SchedulerServiceOrder.FSBranchLocationByBranchLocationCD -> PX.Objects.FS.FSBranchLocation (BranchLocationCD=BranchLocationCD)
PX.Objects.FS.SchedulerServiceOrder.FSProblemByProblemCD -> PX.Objects.FS.FSProblem (ProblemCD=ProblemCD)
PX.Objects.FS.SchedulerServiceOrder.FSRoomByRoomID -> PX.Objects.FS.FSRoom (RoomID=RoomID)
PX.Objects.FS.SchedulerServiceOrder.FSServiceContractByServiceContractRefNbr -> PX.Objects.FS.FSServiceContract (ServiceContractRefNbr=RefNbr)
PX.Objects.FS.SchedulerServiceOrder.FSServiceOrderByRefNbr -> PX.Objects.FS.FSServiceOrder (RefNbr=RefNbr)
PX.Objects.FS.SchedulerServiceOrder.FSSrvOrdTypeBySrvOrdType -> PX.Objects.FS.FSSrvOrdType (SrvOrdType=SrvOrdType)
PX.Objects.FS.SchedulerServiceOrder.BAccountByAssignedEmpID -> PX.Objects.CR.BAccount (AssignedEmpID=BAccountID)
PX.Objects.FS.SchedulerServiceOrder.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.FS.SchedulerServiceOrder.CustomerByBillCustomerID -> PX.Objects.AR.Customer
PX.Objects.FS.SchedulerServiceOrder.FSAddressByServiceOrderAddressID -> PX.Objects.FS.FSAddress (ServiceOrderAddressID=AddressID)
PX.Objects.FS.SchedulerServiceOrder.FSContactByServiceOrderContactID -> PX.Objects.FS.FSContact (ServiceOrderContactID=ContactID)
PX.Objects.FS.SchedulerServiceOrder.FSProblemByProblemID -> PX.Objects.FS.FSProblem (ProblemID=ProblemCD)
PX.Objects.FS.SchedulerServiceOrder.FSServiceContractByServiceContractID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID)
PX.Objects.FS.SchedulerServiceOrder.FSServiceContractByBillServiceContractID -> PX.Objects.FS.FSServiceContract
PX.Objects.FS.SchedulerServiceOrder.FSServiceContractByCustomerID -> PX.Objects.FS.FSServiceContract (ServiceContractID=ServiceContractID, CustomerID=CustomerID)
PX.Objects.FS.SchedulerServiceOrder.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.FS.SchedulerServiceOrder.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.FS.SchedulerServiceOrder.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.FS.SchedulerServiceOrder.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.FS.SchedulerServiceOrder.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.SchedulerServiceOrder.FSServiceOrderTaxTranCollection -> Collection(PX.Objects.FS.FSServiceOrderTaxTran)
PX.Objects.FS.SchedulerServiceOrder.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.SchedulerServiceOrder.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.FS.SchedulerServiceOrder.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.FS.SchedulerServiceOrder.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.SchedulerServiceOrder.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.FS.SchedulerServiceOrder.FSAdjustCollection -> Collection(PX.Objects.FS.FSAdjust)
PX.Objects.FS.SchedulerServiceOrder.FSBillHistoryCollection -> Collection(PX.Objects.FS.FSBillHistory)
PX.Objects.FS.SchedulerServiceOrder.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.SchedulerServiceOrder.FSPostDocCollection -> Collection(PX.Objects.FS.FSPostDoc)
PX.Objects.FS.SchedulerServiceOrder.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.FS.SchedulerServiceOrder.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.FS.SchedulerServiceOrder.FSSOEmployeeCollection -> Collection(PX.Objects.FS.FSSOEmployee)
PX.Objects.FS.SchedulerServiceOrder.FSSOResourceCollection -> Collection(PX.Objects.FS.FSSOResource)
PX.Objects.FS.SchedulerServiceOrder.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.FS.SchedulerServiceOrder.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.FS.SchedulerServiceOrder.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.FS.SchedulerServiceOrder.SchedulerAppointmentCollection -> Collection(PX.Objects.FS.SchedulerAppointment)
PX.Objects.FS.SchedulerServiceOrder.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.Objects.FS.SchedulerServiceOrder.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.FS.SchedulerServiceOrder.FSRoomCollection -> Collection(PX.Objects.FS.FSRoom)
PX.Objects.FS.SchedulerServiceOrder.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)

# PX.Objects.FS.ServiceOrderComponentField (EntityType)

BaseType: PX.Objects.FS.FSCalendarComponentField
Key: ComponentType, FieldName, ObjectName (inherited from PX.Objects.FS.FSCalendarComponentField)
Entity sets: PX_Objects_FS_ServiceOrderComponentField

# PX.Objects.FS.ServiceOrderToPost (EntityType)

Label: "Service Order"
BaseType: PX.Objects.FS.FSServiceOrder
Key: RefNbr, SrvOrdType (inherited from PX.Objects.FS.FSServiceOrder)
Entity sets: PX_Objects_FS_ServiceOrderToPost
Non-filterable, non-selectable: AppointmentID, RowIndex, GroupKey, BatchID, ErrorFlag

PX.Objects.FS.ServiceOrderToPost.PostTo : Edm.String "Post To"
PX.Objects.FS.ServiceOrderToPost.PostOrderType : Edm.String
PX.Objects.FS.ServiceOrderToPost.PostOrderTypeNegativeBalance : Edm.String
PX.Objects.FS.ServiceOrderToPost.PostNegBalanceToAP : Edm.Boolean "Create a Bill Document in AP for Negative Balances"
PX.Objects.FS.ServiceOrderToPost.DfltTermIDARSO : Edm.String
PX.Objects.FS.ServiceOrderToPost.BillingCycleID : Edm.Int32 "Billing Cycle ID"
PX.Objects.FS.ServiceOrderToPost.FrequencyType : Edm.String "Frequency Type"
PX.Objects.FS.ServiceOrderToPost.WeeklyFrequency : Edm.Int32 "Frequency Week Day"
PX.Objects.FS.ServiceOrderToPost.MonthlyFrequency : Edm.Int32 "Frequency Month Day"
PX.Objects.FS.ServiceOrderToPost.SendInvoicesTo : Edm.String "Send Invoices to"
PX.Objects.FS.ServiceOrderToPost.GroupBillByLocations : Edm.Boolean "Create Separate Invoices for Customer Locations"
PX.Objects.FS.ServiceOrderToPost.BillingCycleCD : Edm.String "Billing Cycle ID"
PX.Objects.FS.ServiceOrderToPost.BillingCycleType : Edm.String
PX.Objects.FS.ServiceOrderToPost.InvoiceOnlyCompletedServiceOrder : Edm.Boolean "Invoice only completed or closed Service Orders"
PX.Objects.FS.ServiceOrderToPost.TimeCycleType : Edm.String "Time Cycle Type"
PX.Objects.FS.ServiceOrderToPost.TimeCycleWeekDay : Edm.Int32 "Day of Week"
PX.Objects.FS.ServiceOrderToPost.TimeCycleDayOfMonth : Edm.Int32 "Day of Month"
PX.Objects.FS.ServiceOrderToPost.DocType : Edm.String
PX.Objects.FS.ServiceOrderToPost.AppointmentID : Edm.Int32
PX.Objects.FS.ServiceOrderToPost.RowIndex : Edm.Int32
PX.Objects.FS.ServiceOrderToPost.GroupKey : Edm.String
PX.Objects.FS.ServiceOrderToPost.BatchID : Edm.Int32 "Batch Nbr."
PX.Objects.FS.ServiceOrderToPost.ErrorFlag : Edm.Boolean
PX.Objects.FS.ServiceOrderToPost.SOOrderTypeByPostOrderType -> PX.Objects.SO.SOOrderType (PostOrderType=OrderType)
PX.Objects.FS.ServiceOrderToPost.SOOrderTypeByPostOrderTypeNegativeBalance -> PX.Objects.SO.SOOrderType (PostOrderTypeNegativeBalance=OrderType)
PX.Objects.FS.ServiceOrderToPost.TermsByDfltTermIDARSO -> PX.Objects.CS.Terms (DfltTermIDARSO=TermsID)
PX.Objects.FS.ServiceOrderToPost.FSBillingCycleByBillingCycleID -> PX.Objects.FS.FSBillingCycle (BillingCycleID=BillingCycleID)
PX.Objects.FS.ServiceOrderToPost.FSBillingCycleByBillingCycleCD -> PX.Objects.FS.FSBillingCycle (BillingCycleCD=BillingCycleCD)
PX.Objects.FS.ServiceOrderToPost.SOOrderTypeByAllocationOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.FS.ServiceOrderToPost.TermsByDfltTermIDAP -> PX.Objects.CS.Terms
PX.Objects.FS.ServiceOrderToPost.AppointmentToPostCollection -> Collection(PX.Objects.FS.AppointmentToPost)
PX.Objects.FS.ServiceOrderToPost.ServiceOrderToPostCollection -> Collection(PX.Objects.FS.ServiceOrderToPost)

# PX.Objects.FS.SkillGridFilter (EntityType)

Label: "Skill"
BaseType: PX.Objects.FS.FSSkill
Key: SkillCD (inherited from PX.Objects.FS.FSSkill)
Entity sets: PX_Objects_FS_SkillGridFilter

# PX.Objects.FS.SoldInventoryItem (EntityType)

Key: DocType, InvoiceLineNbr, InvoiceRefNbr, SOLineSplitNumber
Entity sets: PX_Objects_FS_SoldInventoryItem

PX.Objects.FS.SoldInventoryItem.InvoiceRefNbr : Edm.String [key] "Invoice Ref. Nbr."
PX.Objects.FS.SoldInventoryItem.InvoiceLineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.FS.SoldInventoryItem.SOLineSplitNumber : Edm.Int32 [key] "Split Line Nbr."
PX.Objects.FS.SoldInventoryItem.CustomerID : Edm.Int32 "Customer"
PX.Objects.FS.SoldInventoryItem.Descr : Edm.String "Description"
PX.Objects.FS.SoldInventoryItem.DocDate : Edm.DateTimeOffset "Billing Date"
PX.Objects.FS.SoldInventoryItem.DocType : Edm.String [key]
PX.Objects.FS.SoldInventoryItem.EquipmentTypeID : Edm.Int32 "Equipment Type"
PX.Objects.FS.SoldInventoryItem.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.FS.SoldInventoryItem.InventoryID : Edm.Int32
PX.Objects.FS.SoldInventoryItem.InventoryCD : Edm.String "Inventory ID"
PX.Objects.FS.SoldInventoryItem.LotSerialNumber : Edm.String "Lot Serial Number"
PX.Objects.FS.SoldInventoryItem.ShippedQty : Edm.Decimal "Qty"
PX.Objects.FS.SoldInventoryItem.Qty : Edm.Decimal "Order Qty"
PX.Objects.FS.SoldInventoryItem.SOOrderDate : Edm.DateTimeOffset "Order Date"
PX.Objects.FS.SoldInventoryItem.SOOrderType : Edm.String
PX.Objects.FS.SoldInventoryItem.SOOrderNbr : Edm.String "Order Type Nbr."
PX.Objects.FS.SoldInventoryItem.ARInvoiceByInvoiceRefNbr -> PX.Objects.AR.ARInvoice (InvoiceRefNbr=RefNbr)
PX.Objects.FS.SoldInventoryItem.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.FS.SoldInventoryItem.FSEquipmentTypeByEquipmentTypeID -> PX.Objects.FS.FSEquipmentType (EquipmentTypeID=EquipmentTypeID)
PX.Objects.FS.SoldInventoryItem.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.FS.SoldInventoryItem.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.FS.SoldInventoryItem.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.FS.SoldInventoryItem.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.FS.SoldInventoryItem.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.FS.SoldInventoryItem.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.FS.SoldInventoryItem.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.FS.SoldInventoryItem.FSAppointmentLogExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentLogExtItemLine)
PX.Objects.FS.SoldInventoryItem.SOPackageDetailCollection -> Collection(PX.Objects.SO.SOPackageDetail)
PX.Objects.FS.SoldInventoryItem.SOPackageInfoCollection -> Collection(PX.Objects.SO.SOPackageInfo)
PX.Objects.FS.SoldInventoryItem.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.FS.SoldInventoryItem.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.FS.SoldInventoryItem.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.FS.SoldInventoryItem.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.FS.SoldInventoryItem.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.FS.SoldInventoryItem.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.FS.SoldInventoryItem.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.FS.SoldInventoryItem.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.FS.SoldInventoryItem.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.FS.SoldInventoryItem.INItemBoxCollection -> Collection(PX.Objects.IN.INItemBox)
PX.Objects.FS.SoldInventoryItem.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.FS.SoldInventoryItem.INTranSplitCollection -> Collection(PX.Objects.IN.INTranSplit)
PX.Objects.FS.SoldInventoryItem.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.FS.SoldInventoryItem.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.FS.SoldInventoryItem.INMatrixGenerationRuleCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixGenerationRule)
PX.Objects.FS.SoldInventoryItem.INMatrixExcludedDataCollection -> Collection(PX.Objects.IN.Matrix.DAC.INMatrixExcludedData)
PX.Objects.FS.SoldInventoryItem.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.FS.SoldInventoryItem.VendorDiscountSequenceCollection -> Collection(PX.Objects.AP.VendorDiscountSequence)
PX.Objects.FS.SoldInventoryItem.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.FS.SoldInventoryItem.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.FS.SoldInventoryItem.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.FS.SoldInventoryItem.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.FS.SoldInventoryItem.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.FS.SoldInventoryItem.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.FS.SoldInventoryItem.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.FS.SoldInventoryItem.AMMTranSplitCollection -> Collection(PX.Objects.AM.AMMTranSplit)
PX.Objects.FS.SoldInventoryItem.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.FS.SoldInventoryItem.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.FS.SoldInventoryItem.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.FS.SoldInventoryItem.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.FS.SoldInventoryItem.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.FS.SoldInventoryItem.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.FS.SoldInventoryItem.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.FS.SoldInventoryItem.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.FS.SoldInventoryItem.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.FS.SoldInventoryItem.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.FS.SoldInventoryItem.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.FS.SoldInventoryItem.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.FS.SoldInventoryItem.ContractDetailCollection -> Collection(PX.Objects.CT.ContractDetail)
PX.Objects.FS.SoldInventoryItem.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.FS.SoldInventoryItem.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.FS.SoldInventoryItem.INUnitCollection -> Collection(PX.Objects.IN.INUnit)
PX.Objects.FS.SoldInventoryItem.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.FS.SoldInventoryItem.EPSetupCollection -> Collection(PX.Objects.EP.EPSetup)
PX.Objects.FS.SoldInventoryItem.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.FS.SoldInventoryItem.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.FS.SoldInventoryItem.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.FS.SoldInventoryItem.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.FS.SoldInventoryItem.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.FS.SoldInventoryItem.INRelatedInventoryCollection -> Collection(PX.Objects.IN.RelatedItems.INRelatedInventory)
PX.Objects.FS.SoldInventoryItem.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.FS.SoldInventoryItem.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.FS.SoldInventoryItem.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.FS.SoldInventoryItem.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.FS.SoldInventoryItem.InventoryPostingBatchDetailCollection -> Collection(PX.Objects.FS.InventoryPostingBatchDetail)
PX.Objects.FS.SoldInventoryItem.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.FS.SoldInventoryItem.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.FS.SoldInventoryItem.INLocationStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLocationStatusByCostCenter)
PX.Objects.FS.SoldInventoryItem.INLotSerialStatusByCostCenterCollection -> Collection(PX.Objects.IN.INLotSerialStatusByCostCenter)
PX.Objects.FS.SoldInventoryItem.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.FS.SoldInventoryItem.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.FS.SoldInventoryItem.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.FS.SoldInventoryItem.SOPickerListEntryCollection -> Collection(PX.Objects.SO.SOPickerListEntry)
PX.Objects.FS.SoldInventoryItem.SOPickingWorksheetLineCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLine)
PX.Objects.FS.SoldInventoryItem.SOPickingWorksheetLineSplitCollection -> Collection(PX.Objects.SO.SOPickingWorksheetLineSplit)
PX.Objects.FS.SoldInventoryItem.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.FS.SoldInventoryItem.SOShipLineSplitCollection -> Collection(PX.Objects.SO.SOShipLineSplit)
PX.Objects.FS.SoldInventoryItem.SOShipLineSplitPackageCollection -> Collection(PX.Objects.SO.SOShipLineSplitPackage)
PX.Objects.FS.SoldInventoryItem.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.FS.SoldInventoryItem.RQRequestClassItemCollection -> Collection(PX.Objects.RQ.RQRequestClassItem)
PX.Objects.FS.SoldInventoryItem.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.FS.SoldInventoryItem.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.FS.SoldInventoryItem.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.FS.SoldInventoryItem.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.FS.SoldInventoryItem.POReceiptItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.PO.POReceiptItemLotSerialAttributesHeader)
PX.Objects.FS.SoldInventoryItem.POReceiptLineSplitCollection -> Collection(PX.Objects.PO.POReceiptLineSplit)
PX.Objects.FS.SoldInventoryItem.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.FS.SoldInventoryItem.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.FS.SoldInventoryItem.PMChangeRequestMarkupCollection -> Collection(PX.Objects.PM.PMChangeRequestMarkup)
PX.Objects.FS.SoldInventoryItem.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.FS.SoldInventoryItem.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.FS.SoldInventoryItem.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.FS.SoldInventoryItem.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.FS.SoldInventoryItem.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.FS.SoldInventoryItem.PMWorkCodeLaborItemSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeLaborItemSource)
PX.Objects.FS.SoldInventoryItem.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.FS.SoldInventoryItem.MNMaterialListLineSplitCollection -> Collection(PX.Objects.MN.MNMaterialListLineSplit)
PX.Objects.FS.SoldInventoryItem.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.FS.SoldInventoryItem.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.FS.SoldInventoryItem.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.FS.SoldInventoryItem.INCartSplitCollection -> Collection(PX.Objects.IN.INCartSplit)
PX.Objects.FS.SoldInventoryItem.INItemCategoryCollection -> Collection(PX.Objects.IN.INItemCategory)
PX.Objects.FS.SoldInventoryItem.INItemLotSerialAttributeCollection -> Collection(PX.Objects.IN.INItemLotSerialAttribute)
PX.Objects.FS.SoldInventoryItem.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.FS.SoldInventoryItem.INItemSiteReplenishmentCollection -> Collection(PX.Objects.IN.INItemSiteReplenishment)
PX.Objects.FS.SoldInventoryItem.INKitSpecHdrCollection -> Collection(PX.Objects.IN.INKitSpecHdr)
PX.Objects.FS.SoldInventoryItem.INKitSpecNonStkDetCollection -> Collection(PX.Objects.IN.INKitSpecNonStkDet)
PX.Objects.FS.SoldInventoryItem.INKitSpecStkDetCollection -> Collection(PX.Objects.IN.INKitSpecStkDet)
PX.Objects.FS.SoldInventoryItem.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.FS.SoldInventoryItem.INPIClassItemCollection -> Collection(PX.Objects.IN.INPIClassItem)
PX.Objects.FS.SoldInventoryItem.INPIDetailCollection -> Collection(PX.Objects.IN.INPIDetail)
PX.Objects.FS.SoldInventoryItem.INPIStatusItemCollection -> Collection(PX.Objects.IN.INPIStatusItem)
PX.Objects.FS.SoldInventoryItem.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.FS.SoldInventoryItem.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.FS.SoldInventoryItem.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.FS.SoldInventoryItem.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.FS.SoldInventoryItem.InventoryItemLotSerNumValCollection -> Collection(PX.Objects.IN.InventoryItemLotSerNumVal)
PX.Objects.FS.SoldInventoryItem.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.FS.SoldInventoryItem.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.FS.SoldInventoryItem.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.FS.SoldInventoryItem.INRelatedInventoryUserFeedbackCollection -> Collection(PX.Objects.IN.RelatedItems.DAC.INRelatedInventoryUserFeedback)
PX.Objects.FS.SoldInventoryItem.INAttributeDescriptionGroupCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionGroup)
PX.Objects.FS.SoldInventoryItem.INAttributeDescriptionItemCollection -> Collection(PX.Objects.IN.Matrix.DAC.INAttributeDescriptionItem)
PX.Objects.FS.SoldInventoryItem.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.FS.SoldInventoryItem.INRegisterItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INRegisterItemLotSerialAttributesHeader)
PX.Objects.FS.SoldInventoryItem.INTransferDemandLineCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandLine)
PX.Objects.FS.SoldInventoryItem.INTransferDemandPutAwaySplitCollection -> Collection(PX.Objects.IN.DAC.INTransferDemandPutAwaySplit)
PX.Objects.FS.SoldInventoryItem.CABankFeedCollection -> Collection(PX.Objects.CA.CABankFeed)
PX.Objects.FS.SoldInventoryItem.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.Objects.FS.SoldInventoryItem.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.FS.SoldInventoryItem.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.FS.SoldInventoryItem.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.FS.SoldInventoryItem.CRCaseClassCollection -> Collection(PX.Objects.CR.CRCaseClass)
PX.Objects.FS.SoldInventoryItem.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.FS.SoldInventoryItem.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.FS.SoldInventoryItem.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.FS.SoldInventoryItem.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.FS.SoldInventoryItem.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.FS.SoldInventoryItem.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.FS.SoldInventoryItem.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.Objects.FS.SoldInventoryItem.EPContractRateCollection -> Collection(PX.Objects.EP.EPContractRate)
PX.Objects.FS.SoldInventoryItem.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.FS.SoldInventoryItem.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.FS.SoldInventoryItem.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.FS.SoldInventoryItem.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.FS.SoldInventoryItem.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.FS.SoldInventoryItem.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.FS.SoldInventoryItem.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.FS.SoldInventoryItem.BCBindingShopifyCollection -> Collection(PX.Commerce.Shopify.BCBindingShopify)
PX.Objects.FS.SoldInventoryItem.InventoryItemCarrierDataCollection -> Collection(PX.ExternalCarriersHelper.InventoryItemCarrierData)
PX.Objects.FS.SoldInventoryItem.AMBatchItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.AM.AMBatchItemLotSerialAttributesHeader)
PX.Objects.FS.SoldInventoryItem.AMBomCostHistoryCollection -> Collection(PX.Objects.AM.AMBomCostHistory)
PX.Objects.FS.SoldInventoryItem.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.FS.SoldInventoryItem.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.FS.SoldInventoryItem.AMClockTranSplitCollection -> Collection(PX.Objects.AM.AMClockTranSplit)
PX.Objects.FS.SoldInventoryItem.AMConfigResultsOptionCollection -> Collection(PX.Objects.AM.AMConfigResultsOption)
PX.Objects.FS.SoldInventoryItem.AMConfigurationCollection -> Collection(PX.Objects.AM.AMConfiguration)
PX.Objects.FS.SoldInventoryItem.AMConfigurationOptionCollection -> Collection(PX.Objects.AM.AMConfigurationOption)
PX.Objects.FS.SoldInventoryItem.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.FS.SoldInventoryItem.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.FS.SoldInventoryItem.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.FS.SoldInventoryItem.AMEstimateMatlCollection -> Collection(PX.Objects.AM.AMEstimateMatl)
PX.Objects.FS.SoldInventoryItem.AMFeatureOptionCollection -> Collection(PX.Objects.AM.AMFeatureOption)
PX.Objects.FS.SoldInventoryItem.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.FS.SoldInventoryItem.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.FS.SoldInventoryItem.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.FS.SoldInventoryItem.AMMRPBucketDetailInqCollection -> Collection(PX.Objects.AM.AMMRPBucketDetailInq)
PX.Objects.FS.SoldInventoryItem.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.FS.SoldInventoryItem.AMProdItemSplitCollection -> Collection(PX.Objects.AM.AMProdItemSplit)
PX.Objects.FS.SoldInventoryItem.AMProdMatlSplitCollection -> Collection(PX.Objects.AM.AMProdMatlSplit)
PX.Objects.FS.SoldInventoryItem.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.FS.SoldInventoryItem.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.FS.SoldInventoryItem.AMSchdItemCollection -> Collection(PX.Objects.AM.AMSchdItem)
PX.Objects.FS.SoldInventoryItem.AMSubItemDefaultCollection -> Collection(PX.Objects.AM.AMSubItemDefault)
PX.Objects.FS.SoldInventoryItem.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.FS.SoldInventoryItem.AMVendorShipLineSplitCollection -> Collection(PX.Objects.AM.AMVendorShipLineSplit)
PX.Objects.FS.SoldInventoryItem.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.FS.SoldInventoryItem.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.FS.SoldInventoryItem.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.FS.SoldInventoryItem.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.FS.SoldInventoryItem.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.FS.SoldInventoryItem.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.FS.SoldInventoryItem.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.FS.SoldInventoryItem.FSServiceEquipmentTypeCollection -> Collection(PX.Objects.FS.FSServiceEquipmentType)
PX.Objects.FS.SoldInventoryItem.FSServiceInventoryItemCollection -> Collection(PX.Objects.FS.FSServiceInventoryItem)
PX.Objects.FS.SoldInventoryItem.FSServiceLicenseTypeCollection -> Collection(PX.Objects.FS.FSServiceLicenseType)
PX.Objects.FS.SoldInventoryItem.FSServiceSkillCollection -> Collection(PX.Objects.FS.FSServiceSkill)
PX.Objects.FS.SoldInventoryItem.FSServiceTemplateDetCollection -> Collection(PX.Objects.FS.FSServiceTemplateDet)
PX.Objects.FS.SoldInventoryItem.FSServiceVehicleTypeCollection -> Collection(PX.Objects.FS.FSServiceVehicleType)
PX.Objects.FS.SoldInventoryItem.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.FS.SoldInventoryItem.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.FS.SoldInventoryItem.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.FS.SoldInventoryItem.PRDeductionAndBenefitUnionPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitUnionPackage)
PX.Objects.FS.SoldInventoryItem.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.FS.SoldInventoryItem.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.FS.SoldInventoryItem.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.FS.SoldInventoryItem.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.FS.SoldInventoryItem.PRPaymentUnionPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentUnionPackageDeduct)
PX.Objects.FS.SoldInventoryItem.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.FS.SoldInventoryItem.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.FS.SoldInventoryItem.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.FS.SoldInventoryItem.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.FS.SoldInventoryItem.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.FS.SoldInventoryItem.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.FS.SoldInventoryItem.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.FS.SoldInventoryItem.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.FS.SoldInventoryItem.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.FS.SoldInventoryItem.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.FS.SoldInventoryItem.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.FS.SoldInventoryItem.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.FS.SoldInventoryItem.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.FS.SoldInventoryItem.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.FS.SoldInventoryItem.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.FS.SoldInventoryItem.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.FS.SoldInventoryItem.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.FS.SoldInventoryItem.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.FS.SoldInventoryItem.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.FS.SoldInventoryItem.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.FS.SoldInventoryItem.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.FS.SoldInventoryItem.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.FS.SoldInventoryItem.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.FS.SoldInventoryItem.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.FS.SoldInventoryItem.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.FS.SoldInventoryItem.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.FS.SoldInventoryItem.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.FS.SoldInventoryItem.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.FS.SoldInventoryItem.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.FS.SoldInventoryItem.POLineRCollection -> Collection(PX.Objects.PO.POLineR)
PX.Objects.FS.SoldInventoryItem.PMItemRateCollection -> Collection(PX.Objects.PM.PMItemRate)
PX.Objects.FS.SoldInventoryItem.PMProjectARTranPostDetailCollection -> Collection(PX.Objects.PM.Project.Cashflow.PMProjectARTranPostDetail)
PX.Objects.FS.SoldInventoryItem.INCartContentByLocationCollection -> Collection(PX.Objects.IN.INCartContentByLocation)
PX.Objects.FS.SoldInventoryItem.INCartContentByLotSerialCollection -> Collection(PX.Objects.IN.INCartContentByLotSerial)
PX.Objects.FS.SoldInventoryItem.INItemLotSerialCollection -> Collection(PX.Objects.IN.INItemLotSerial)
PX.Objects.FS.SoldInventoryItem.INItemSalesHistCollection -> Collection(PX.Objects.IN.INItemSalesHist)
PX.Objects.FS.SoldInventoryItem.INItemSiteHistCollection -> Collection(PX.Objects.IN.INItemSiteHist)
PX.Objects.FS.SoldInventoryItem.INItemSiteHistDayCollection -> Collection(PX.Objects.IN.INItemSiteHistDay)
PX.Objects.FS.SoldInventoryItem.INItemStatsCollection -> Collection(PX.Objects.IN.INItemStats)
PX.Objects.FS.SoldInventoryItem.INSiteLotSerialCollection -> Collection(PX.Objects.IN.INSiteLotSerial)
PX.Objects.FS.SoldInventoryItem.INSiteStatusByCostCenterCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenter)
PX.Objects.FS.SoldInventoryItem.INSubItemSegmentValueCollection -> Collection(PX.Objects.IN.INSubItemSegmentValue)
PX.Objects.FS.SoldInventoryItem.INKitTranSplitCollection -> Collection(PX.Objects.IN.INKitTranSplit)
PX.Objects.FS.SoldInventoryItem.INLocationStatusCollection -> Collection(PX.Objects.IN.INLocationStatus)
PX.Objects.FS.SoldInventoryItem.INLotSerialStatusCollection -> Collection(PX.Objects.IN.INLotSerialStatus)
PX.Objects.FS.SoldInventoryItem.INPIStatusCollection -> Collection(PX.Objects.IN.INPIStatus)
PX.Objects.FS.SoldInventoryItem.INSiteStatusCollection -> Collection(PX.Objects.IN.INSiteStatus)
PX.Objects.FS.SoldInventoryItem.INSiteStatusByCostCenterShortCollection -> Collection(PX.Objects.IN.INSiteStatusByCostCenterShort)
PX.Objects.FS.SoldInventoryItem.INSiteStatusSummaryCollection -> Collection(PX.Objects.IN.INSiteStatusSummary)
PX.Objects.FS.SoldInventoryItem.INTransferStatusCollection -> Collection(PX.Objects.IN.INTransferStatus)
PX.Objects.FS.SoldInventoryItem.INTransferLocationStatusCollection -> Collection(PX.Objects.IN.INTransferLocationStatus)
PX.Objects.FS.SoldInventoryItem.RelatedItemCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItem)
PX.Objects.FS.SoldInventoryItem.INItemLotSerialAttributesHeaderCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeader)
PX.Objects.FS.SoldInventoryItem.BCInventoryFileUrlsCollection -> Collection(PX.Commerce.Objects.BCInventoryFileUrls)
PX.Objects.FS.SoldInventoryItem.AMBomCostCollection -> Collection(PX.Objects.AM.AMBomCost)
PX.Objects.FS.SoldInventoryItem.AMBomMatlCollection -> Collection(PX.Objects.AM.AMBomMatl)
PX.Objects.FS.SoldInventoryItem.INItemPlanAMExtensionCollection -> Collection(PX.Objects.AM.CacheExtensions.INItemPlanAMExtension)
PX.Objects.FS.SoldInventoryItem.FSDetailFSLogActionCollection -> Collection(PX.Objects.FS.FSDetailFSLogAction)
PX.Objects.FS.SoldInventoryItem.FSSODetFSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetFSSODetSplit)
PX.Objects.FS.SoldInventoryItem.SchedulerEmployeeInventoryItemCollection -> Collection(PX.Objects.FS.SchedulerEmployeeInventoryItem)
PX.Objects.FS.SoldInventoryItem.SVSiteStatusSelectedCollection -> Collection(PX.Objects.SV.SVSiteStatusSelected)
PX.Objects.FS.SoldInventoryItem.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.FS.SoldInventoryItem.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.FS.SoldInventoryItem.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.FS.SoldInventoryItem.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.FS.SOOrderTypeQuickProcess (EntityType)

Label: "Order Type"
BaseType: PX.Objects.SO.SOOrderType
Key: OrderType (inherited from PX.Objects.SO.SOOrderType)
Entity sets: PX_Objects_FS_SOOrderTypeQuickProcess

# PX.Objects.FS.UnassignedAppComponentField (EntityType)

BaseType: PX.Objects.FS.FSCalendarComponentField
Key: ComponentType, FieldName, ObjectName (inherited from PX.Objects.FS.FSCalendarComponentField)
Entity sets: PX_Objects_FS_UnassignedAppComponentField

# PX.Objects.GDPR.SMPersonalDataLog (EntityType)

Key: LogID
Entity sets: PX_Objects_GDPR_SMPersonalDataLog
Non-filterable, non-selectable: UIKey

PX.Objects.GDPR.SMPersonalDataLog.UIKey : Edm.String "Key"
PX.Objects.GDPR.SMPersonalDataLog.LogID : Edm.Int32 [key]
PX.Objects.GDPR.SMPersonalDataLog.CombinedKey : Edm.String "Key"
PX.Objects.GDPR.SMPersonalDataLog.TableName : Edm.String "Entity"
PX.Objects.GDPR.SMPersonalDataLog.CreatedByID : Edm.Guid "By User"
PX.Objects.GDPR.SMPersonalDataLog.CreatedDateTime : Edm.DateTimeOffset "On"
PX.Objects.GDPR.SMPersonalDataLog.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)

# PX.Objects.GL.Account (EntityType)

Label: "GL Account"
Key: AccountCD
Entity sets: PX_Objects_GL_Account, GLAccount, Account
Non-filterable, non-selectable: NoteText, TypeTotal, ReadableActive, TransactionsForGivenCurrencyExists, Included, Secured, DeletedDatabaseRecord

PX.Objects.GL.Account.AccountID : Edm.Int32 "Account ID"
PX.Objects.GL.Account.AccountCD : Edm.String [key] "Account"
PX.Objects.GL.Account.AccountingType : Edm.String
PX.Objects.GL.Account.AccountClassID : Edm.String "Account Class"
PX.Objects.GL.Account.Type : Edm.String "Type"
PX.Objects.GL.Account.ControlAccountModule : Edm.String "Control Account Module"
PX.Objects.GL.Account.AllowManualEntry : Edm.Boolean [required] "Allow Manual Entry"
PX.Objects.GL.Account.COAOrder : Edm.Int16 [required] "COA Order"
PX.Objects.GL.Account.Active : Edm.Boolean [required] "Active"
PX.Objects.GL.Account.Description : Edm.String "Description"
PX.Objects.GL.Account.PostOption : Edm.String "Post Option"
PX.Objects.GL.Account.DirectPost : Edm.Boolean [required] "Direct Post"
PX.Objects.GL.Account.NoSubDetail : Edm.Boolean [required] "Use Default Subaccount"
PX.Objects.GL.Account.RequireUnits : Edm.Boolean [required] "Require Units"
PX.Objects.GL.Account.GLConsolAccountCD : Edm.String "Consolidation Account"
PX.Objects.GL.Account.CuryID : Edm.String "Currency"
PX.Objects.GL.Account.AccountGroupID : Edm.Int32 "Account Group"
PX.Objects.GL.Account.RevalCuryRateTypeId : Edm.String "Revaluation Rate Type"
PX.Objects.GL.Account.Box1099 : Edm.Int16 "1099 Box"
PX.Objects.GL.Account.NoteID : Edm.Guid
PX.Objects.GL.Account.NoteText : Edm.String "Note Text"
PX.Objects.GL.Account.tstamp : Edm.Binary
PX.Objects.GL.Account.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.Account.CreatedByScreenID : Edm.String
PX.Objects.GL.Account.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.Account.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.Account.LastModifiedByScreenID : Edm.String
PX.Objects.GL.Account.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.Account.IsCashAccount : Edm.Boolean [required] "Cash Account"
PX.Objects.GL.Account.TypeTotal : Edm.String "TypeTotal"
PX.Objects.GL.Account.ReadableActive : Edm.Int32 "ReadableActive"
PX.Objects.GL.Account.TransactionsForGivenCurrencyExists : Edm.Boolean
PX.Objects.GL.Account.Included : Edm.Boolean "Included"
PX.Objects.GL.Account.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.GL.Account.Secured : Edm.Boolean "Secured"
PX.Objects.GL.Account.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.Account.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.GL.Account.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.Account.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.Account.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.GL.Account.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.GL.Account.CurrencyRateTypeByRevalCuryRateTypeId -> PX.Objects.CM.CurrencyRateType (RevalCuryRateTypeId=CuryRateTypeID)
PX.Objects.GL.Account.AccountByGLConsolAccountCD -> PX.Objects.GL.Account (GLConsolAccountCD=AccountCD)
PX.Objects.GL.Account.AccountClassByAccountClassID -> PX.Objects.GL.AccountClass (AccountClassID=AccountClassID)
PX.Objects.GL.Account.GLConsolAccountByGLConsolAccountCD -> PX.Objects.GL.GLConsolAccount (GLConsolAccountCD=AccountCD)
PX.Objects.GL.Account.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.GL.Account.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.GL.Account.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.GL.Account.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.GL.Account.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.GL.Account.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.GL.Account.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.GL.Account.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.GL.Account.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.GL.Account.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.GL.Account.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.GL.Account.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.GL.Account.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.GL.Account.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.GL.Account.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.GL.Account.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.GL.Account.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.GL.Account.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.GL.Account.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.GL.Account.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.GL.Account.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.GL.Account.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.GL.Account.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.GL.Account.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.GL.Account.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.GL.Account.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.GL.Account.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.GL.Account.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.GL.Account.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.GL.Account.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.GL.Account.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.GL.Account.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.GL.Account.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.GL.Account.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.GL.Account.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.GL.Account.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.GL.Account.DRDeferredCodeCollection -> Collection(PX.Objects.DR.DRDeferredCode)
PX.Objects.GL.Account.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.GL.Account.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.Objects.GL.Account.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.GL.Account.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.GL.Account.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.GL.Account.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.GL.Account.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.GL.Account.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.GL.Account.SOOrderTypeCollection -> Collection(PX.Objects.SO.SOOrderType)
PX.Objects.GL.Account.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.GL.Account.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.GL.Account.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.GL.Account.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.GL.Account.CurrencyCollection -> Collection(PX.Objects.CM.Currency)
PX.Objects.GL.Account.GLBudgetLineCollection -> Collection(PX.Objects.GL.GLBudgetLine)
PX.Objects.GL.Account.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.GL.Account.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.GL.Account.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.GL.Account.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.GL.Account.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.GL.Account.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.GL.Account.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.GL.Account.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.GL.Account.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.GL.Account.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.GL.Account.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.GL.Account.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.GL.Account.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.GL.Account.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.GL.Account.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.GL.Account.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.GL.Account.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.GL.Account.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.GL.Account.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.GL.Account.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.GL.Account.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.GL.Account.TXImportStateCollection -> Collection(PX.Objects.TX.TXImportState)
PX.Objects.GL.Account.TXSetupCollection -> Collection(PX.Objects.TX.TXSetup)
PX.Objects.GL.Account.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.GL.Account.RQRequestClassCollection -> Collection(PX.Objects.RQ.RQRequestClass)
PX.Objects.GL.Account.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.GL.Account.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.GL.Account.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.GL.Account.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.GL.Account.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.GL.Account.POSetupCollection -> Collection(PX.Objects.PO.POSetup)
PX.Objects.GL.Account.PMAccountTaskCollection -> Collection(PX.Objects.PM.PMAccountTask)
PX.Objects.GL.Account.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.GL.Account.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.Objects.GL.Account.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.GL.Account.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.GL.Account.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.GL.Account.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.GL.Account.FADisposalMethodCollection -> Collection(PX.Objects.FA.FADisposalMethod)
PX.Objects.GL.Account.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.GL.Account.FASetupCollection -> Collection(PX.Objects.FA.FASetup)
PX.Objects.GL.Account.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.GL.Account.CarrierCollection -> Collection(PX.Objects.CS.Carrier)
PX.Objects.GL.Account.ReasonCodeCollection -> Collection(PX.Objects.CS.ReasonCode)
PX.Objects.GL.Account.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.GL.Account.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.Objects.GL.Account.INPostClassCollection -> Collection(PX.Objects.IN.INPostClass)
PX.Objects.GL.Account.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.GL.Account.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.GL.Account.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.GL.Account.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.GL.Account.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.Objects.GL.Account.GLAllocationDestinationCollection -> Collection(PX.Objects.GL.GLAllocationDestination)
PX.Objects.GL.Account.GLAllocationSourceCollection -> Collection(PX.Objects.GL.GLAllocationSource)
PX.Objects.GL.Account.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)
PX.Objects.GL.Account.GLBudgetTreeCollection -> Collection(PX.Objects.GL.GLBudgetTree)
PX.Objects.GL.Account.GLSetupCollection -> Collection(PX.Objects.GL.GLSetup)
PX.Objects.GL.Account.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.GL.Account.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.GL.Account.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.GL.Account.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.GL.Account.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.GL.Account.CASetupCollection -> Collection(PX.Objects.CA.CASetup)
PX.Objects.GL.Account.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.Objects.GL.Account.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.GL.Account.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.GL.Account.ARFinChargeCollection -> Collection(PX.Objects.AR.ARFinCharge)
PX.Objects.GL.Account.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.GL.Account.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.GL.Account.EPDepartmentCollection -> Collection(PX.Objects.EP.EPDepartment)
PX.Objects.GL.Account.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.GL.Account.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.GL.Account.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.GL.Account.AMLaborCodeCollection -> Collection(PX.Objects.AM.AMLaborCode)
PX.Objects.GL.Account.AMMachCollection -> Collection(PX.Objects.AM.AMMach)
PX.Objects.GL.Account.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.Objects.GL.Account.AMOverheadCollection -> Collection(PX.Objects.AM.AMOverhead)
PX.Objects.GL.Account.AMToolMstCollection -> Collection(PX.Objects.AM.AMToolMst)
PX.Objects.GL.Account.AMWCMachCollection -> Collection(PX.Objects.AM.AMWCMach)
PX.Objects.GL.Account.PRPayGroupCollection -> Collection(PX.Objects.PR.PRPayGroup)
PX.Objects.GL.Account.PRPTOBankCollection -> Collection(PX.Objects.PR.PRPTOBank)
PX.Objects.GL.Account.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.GL.Account.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.GL.Account.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.GL.Account.SVOrderGLAccountCollection -> Collection(PX.Objects.SV.SVOrderGLAccount)
PX.Objects.GL.Account.SVOrderTypeCollection -> Collection(PX.Objects.SV.SVOrderType)
PX.Objects.GL.Account.SVOrderTypeGLAccountCollection -> Collection(PX.Objects.SV.SVOrderTypeGLAccount)
PX.Objects.GL.Account.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.GL.Account.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.GL.Account.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.GL.Account.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.GL.Account.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.GL.Account.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.GL.Account.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.GL.Account.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.Objects.GL.Account.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.GL.Account.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.GL.Account.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.GL.Account.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.GL.Account.ArmGLHistoryByPeriodCollection -> Collection(PX.Objects.CS.ArmGLHistoryByPeriod)
PX.Objects.GL.Account.BranchAcctMapFromCollection -> Collection(PX.Objects.GL.BranchAcctMapFrom)
PX.Objects.GL.Account.BranchAcctMapToCollection -> Collection(PX.Objects.GL.BranchAcctMapTo)
PX.Objects.GL.Account.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.Objects.GL.Account.GLHistoryByPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByPeriod)
PX.Objects.GL.Account.GLHistoryByCurrentPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByCurrentPeriod)
PX.Objects.GL.Account.GLHistoryLastRevaluationCollection -> Collection(PX.Objects.GL.GLHistoryLastRevaluation)
PX.Objects.GL.Account.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.GL.Account.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.GL.Account.DRSetupCollection -> Collection(PX.Objects.DR.DRSetup)
PX.Objects.GL.Account.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.GL.Account.INUpdateStdCostRecordCollection -> Collection(PX.Objects.IN.INUpdateStdCostRecord)
PX.Objects.GL.Account.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.GL.Account.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.GL.Account.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.GL.Account.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.GL.AccountClass (EntityType)

Label: "GL Account Class"
Key: AccountClassID
Entity sets: PX_Objects_GL_AccountClass, GLAccountClass, AccountClass
Non-filterable, non-selectable: NoteText

PX.Objects.GL.AccountClass.AccountClassID : Edm.String [key] "Account Class ID"
PX.Objects.GL.AccountClass.Descr : Edm.String "Description"
PX.Objects.GL.AccountClass.Type : Edm.String "Type"
PX.Objects.GL.AccountClass.tstamp : Edm.Binary
PX.Objects.GL.AccountClass.NoteID : Edm.Guid
PX.Objects.GL.AccountClass.NoteText : Edm.String "Note Text"
PX.Objects.GL.AccountClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.AccountClass.CreatedByScreenID : Edm.String
PX.Objects.GL.AccountClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.GL.AccountClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.AccountClass.LastModifiedByScreenID : Edm.String
PX.Objects.GL.AccountClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.GL.AccountClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.AccountClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.AccountClass.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.GL.AccountClass.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)

# PX.Objects.GL.AdjustedBranch (EntityType)

Label: "Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_AdjustedBranch

# PX.Objects.GL.AdjustingBranch (EntityType)

Label: "Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_AdjustingBranch

# PX.Objects.GL.ADL.Account (EntityType)

Singletons: PX_Objects_GL_ADL_Account

PX.Objects.GL.ADL.Account.AccountID : Edm.Int32 "Account ID"
PX.Objects.GL.ADL.Account.Type : Edm.String "Type"
PX.Objects.GL.ADL.Account.CuryID : Edm.String "Currency"
PX.Objects.GL.ADL.Account.TransactionsForGivenCurrencyExists : Edm.Boolean
PX.Objects.GL.ADL.Account.Included : Edm.Boolean "Included"
PX.Objects.GL.ADL.Account.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.GL.ADL.Account.Secured : Edm.Boolean "Secured"
PX.Objects.GL.ADL.Account.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.ADL.Account.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup
PX.Objects.GL.ADL.Account.UsersByCreatedByID -> PX.SM.Users
PX.Objects.GL.ADL.Account.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.GL.ADL.Account.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.GL.ADL.Account.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.GL.ADL.Account.CurrencyRateTypeByRevalCuryRateTypeId -> PX.Objects.CM.CurrencyRateType
PX.Objects.GL.ADL.Account.AccountByGLConsolAccountCD -> PX.Objects.GL.Account
PX.Objects.GL.ADL.Account.AccountClassByAccountClassID -> PX.Objects.GL.AccountClass
PX.Objects.GL.ADL.Account.GLConsolAccountByGLConsolAccountCD -> PX.Objects.GL.GLConsolAccount
PX.Objects.GL.ADL.Account.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.GL.ADL.Account.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.GL.ADL.Account.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.GL.ADL.Account.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.GL.ADL.Account.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.GL.ADL.Account.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.GL.ADL.Account.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.GL.ADL.Account.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.GL.ADL.Account.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.GL.ADL.Account.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.GL.ADL.Account.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.GL.ADL.Account.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.GL.ADL.Account.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.GL.ADL.Account.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.GL.ADL.Account.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.GL.ADL.Account.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.GL.ADL.Account.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.GL.ADL.Account.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.GL.ADL.Account.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.GL.ADL.Account.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.GL.ADL.Account.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.GL.ADL.Account.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.GL.ADL.Account.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.GL.ADL.Account.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.GL.ADL.Account.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.GL.ADL.Account.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.GL.ADL.Account.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.GL.ADL.Account.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.GL.ADL.Account.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.GL.ADL.Account.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.GL.ADL.Account.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.GL.ADL.Account.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.GL.ADL.Account.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.GL.ADL.Account.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.GL.ADL.Account.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.GL.ADL.Account.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.GL.ADL.Account.DRDeferredCodeCollection -> Collection(PX.Objects.DR.DRDeferredCode)
PX.Objects.GL.ADL.Account.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.GL.ADL.Account.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.Objects.GL.ADL.Account.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.GL.ADL.Account.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.GL.ADL.Account.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.GL.ADL.Account.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.GL.ADL.Account.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.GL.ADL.Account.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.GL.ADL.Account.SOOrderTypeCollection -> Collection(PX.Objects.SO.SOOrderType)
PX.Objects.GL.ADL.Account.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.GL.ADL.Account.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.GL.ADL.Account.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.GL.ADL.Account.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.GL.ADL.Account.CurrencyCollection -> Collection(PX.Objects.CM.Currency)
PX.Objects.GL.ADL.Account.GLBudgetLineCollection -> Collection(PX.Objects.GL.GLBudgetLine)
PX.Objects.GL.ADL.Account.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.GL.ADL.Account.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.GL.ADL.Account.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.GL.ADL.Account.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.GL.ADL.Account.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.GL.ADL.Account.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.GL.ADL.Account.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.GL.ADL.Account.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.GL.ADL.Account.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.GL.ADL.Account.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.GL.ADL.Account.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.GL.ADL.Account.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.GL.ADL.Account.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.GL.ADL.Account.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.GL.ADL.Account.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.GL.ADL.Account.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.GL.ADL.Account.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.GL.ADL.Account.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.GL.ADL.Account.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.GL.ADL.Account.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.GL.ADL.Account.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.GL.ADL.Account.TXImportStateCollection -> Collection(PX.Objects.TX.TXImportState)
PX.Objects.GL.ADL.Account.TXSetupCollection -> Collection(PX.Objects.TX.TXSetup)
PX.Objects.GL.ADL.Account.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.GL.ADL.Account.RQRequestClassCollection -> Collection(PX.Objects.RQ.RQRequestClass)
PX.Objects.GL.ADL.Account.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.GL.ADL.Account.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.GL.ADL.Account.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.GL.ADL.Account.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.GL.ADL.Account.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.GL.ADL.Account.POSetupCollection -> Collection(PX.Objects.PO.POSetup)
PX.Objects.GL.ADL.Account.PMAccountTaskCollection -> Collection(PX.Objects.PM.PMAccountTask)
PX.Objects.GL.ADL.Account.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.GL.ADL.Account.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.Objects.GL.ADL.Account.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.GL.ADL.Account.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.GL.ADL.Account.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.GL.ADL.Account.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.GL.ADL.Account.FADisposalMethodCollection -> Collection(PX.Objects.FA.FADisposalMethod)
PX.Objects.GL.ADL.Account.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.GL.ADL.Account.FASetupCollection -> Collection(PX.Objects.FA.FASetup)
PX.Objects.GL.ADL.Account.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.GL.ADL.Account.CarrierCollection -> Collection(PX.Objects.CS.Carrier)
PX.Objects.GL.ADL.Account.ReasonCodeCollection -> Collection(PX.Objects.CS.ReasonCode)
PX.Objects.GL.ADL.Account.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.GL.ADL.Account.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.Objects.GL.ADL.Account.INPostClassCollection -> Collection(PX.Objects.IN.INPostClass)
PX.Objects.GL.ADL.Account.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.GL.ADL.Account.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.GL.ADL.Account.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.GL.ADL.Account.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.GL.ADL.Account.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.Objects.GL.ADL.Account.GLAllocationDestinationCollection -> Collection(PX.Objects.GL.GLAllocationDestination)
PX.Objects.GL.ADL.Account.GLAllocationSourceCollection -> Collection(PX.Objects.GL.GLAllocationSource)
PX.Objects.GL.ADL.Account.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)
PX.Objects.GL.ADL.Account.GLBudgetTreeCollection -> Collection(PX.Objects.GL.GLBudgetTree)
PX.Objects.GL.ADL.Account.GLSetupCollection -> Collection(PX.Objects.GL.GLSetup)
PX.Objects.GL.ADL.Account.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.GL.ADL.Account.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.GL.ADL.Account.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.GL.ADL.Account.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.GL.ADL.Account.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.GL.ADL.Account.CASetupCollection -> Collection(PX.Objects.CA.CASetup)
PX.Objects.GL.ADL.Account.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.Objects.GL.ADL.Account.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.GL.ADL.Account.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.GL.ADL.Account.ARFinChargeCollection -> Collection(PX.Objects.AR.ARFinCharge)
PX.Objects.GL.ADL.Account.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.GL.ADL.Account.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.GL.ADL.Account.EPDepartmentCollection -> Collection(PX.Objects.EP.EPDepartment)
PX.Objects.GL.ADL.Account.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.GL.ADL.Account.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.GL.ADL.Account.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.GL.ADL.Account.AMLaborCodeCollection -> Collection(PX.Objects.AM.AMLaborCode)
PX.Objects.GL.ADL.Account.AMMachCollection -> Collection(PX.Objects.AM.AMMach)
PX.Objects.GL.ADL.Account.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.Objects.GL.ADL.Account.AMOverheadCollection -> Collection(PX.Objects.AM.AMOverhead)
PX.Objects.GL.ADL.Account.AMToolMstCollection -> Collection(PX.Objects.AM.AMToolMst)
PX.Objects.GL.ADL.Account.AMWCMachCollection -> Collection(PX.Objects.AM.AMWCMach)
PX.Objects.GL.ADL.Account.PRPayGroupCollection -> Collection(PX.Objects.PR.PRPayGroup)
PX.Objects.GL.ADL.Account.PRPTOBankCollection -> Collection(PX.Objects.PR.PRPTOBank)
PX.Objects.GL.ADL.Account.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.GL.ADL.Account.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.GL.ADL.Account.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.GL.ADL.Account.SVOrderGLAccountCollection -> Collection(PX.Objects.SV.SVOrderGLAccount)
PX.Objects.GL.ADL.Account.SVOrderTypeCollection -> Collection(PX.Objects.SV.SVOrderType)
PX.Objects.GL.ADL.Account.SVOrderTypeGLAccountCollection -> Collection(PX.Objects.SV.SVOrderTypeGLAccount)
PX.Objects.GL.ADL.Account.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.GL.ADL.Account.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.GL.ADL.Account.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.GL.ADL.Account.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.GL.ADL.Account.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.GL.ADL.Account.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.GL.ADL.Account.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.GL.ADL.Account.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.Objects.GL.ADL.Account.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.GL.ADL.Account.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.GL.ADL.Account.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.GL.ADL.Account.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.GL.ADL.Account.ArmGLHistoryByPeriodCollection -> Collection(PX.Objects.CS.ArmGLHistoryByPeriod)
PX.Objects.GL.ADL.Account.BranchAcctMapFromCollection -> Collection(PX.Objects.GL.BranchAcctMapFrom)
PX.Objects.GL.ADL.Account.BranchAcctMapToCollection -> Collection(PX.Objects.GL.BranchAcctMapTo)
PX.Objects.GL.ADL.Account.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.Objects.GL.ADL.Account.GLHistoryByPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByPeriod)
PX.Objects.GL.ADL.Account.GLHistoryByCurrentPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByCurrentPeriod)
PX.Objects.GL.ADL.Account.GLHistoryLastRevaluationCollection -> Collection(PX.Objects.GL.GLHistoryLastRevaluation)
PX.Objects.GL.ADL.Account.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.GL.ADL.Account.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.GL.ADL.Account.DRSetupCollection -> Collection(PX.Objects.DR.DRSetup)
PX.Objects.GL.ADL.Account.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.GL.ADL.Account.INUpdateStdCostRecordCollection -> Collection(PX.Objects.IN.INUpdateStdCostRecord)
PX.Objects.GL.ADL.Account.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.GL.ADL.Account.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.GL.ADL.Account.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.GL.ADL.Account.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.GL.ADL.Batch (EntityType)

Key: BatchNbr, Module
Entity sets: PX_Objects_GL_ADL_Batch
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.GL.ADL.Batch.Module : Edm.String [key] "Module"
PX.Objects.GL.ADL.Batch.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.GL.ADL.Batch.Description : Edm.String "Description"
PX.Objects.GL.ADL.Batch.DateEntered : Edm.DateTimeOffset "Transaction Date"
PX.Objects.GL.ADL.Batch.FinPeriodID : Edm.String "Post Period"
PX.Objects.GL.ADL.Batch.BatchType : Edm.String "Type"
PX.Objects.GL.ADL.Batch.Scheduled : Edm.Boolean [required]
PX.Objects.GL.ADL.Batch.Voided : Edm.Boolean [required] "Voided"
PX.Objects.GL.ADL.Batch.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.ADL.Batch.BatchByOrigBatchNbr -> PX.Objects.GL.Batch
PX.Objects.GL.ADL.Batch.BatchByOrigModule -> PX.Objects.GL.Batch
PX.Objects.GL.ADL.Batch.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.ADL.Batch.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.GL.ADL.Batch.UsersByCreatedByID -> PX.SM.Users
PX.Objects.GL.ADL.Batch.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.GL.ADL.Batch.CurrencyByCuryID -> PX.Objects.CM.Currency
PX.Objects.GL.ADL.Batch.LedgerByLedgerID -> PX.Objects.GL.Ledger
PX.Objects.GL.ADL.Batch.ScheduleByScheduleID -> PX.Objects.GL.Schedule
PX.Objects.GL.ADL.Batch.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.GL.ADL.Batch.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.GL.ADL.Batch.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.GL.ADL.Batch.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.GL.ADL.Batch.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.GL.ADL.Batch.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.GL.ADL.Batch.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.GL.ADL.Batch.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.GL.ADL.Batch.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.GL.ADL.Batch.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.Objects.GL.ADL.Batch.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.GL.ADL.Batch.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.GL.ADL.Batch.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.GL.ADL.Batch.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.GL.ADL.Batch.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.GL.ADL.Batch.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.GL.ADL.Batch.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.GL.ADL.Batch.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.GL.ADL.Batch.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.GL.ADL.Batch.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.GL.ADL.Batch.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.GL.ADL.Batch.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.GL.ADL.Batch.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.GL.ADL.Batch.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.GL.ADL.Batch.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.GL.ADL.Batch.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.Objects.GL.ADL.Batch.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.GL.ADL.Batch.GLTrialBalanceImportMapCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportMap)
PX.Objects.GL.ADL.Batch.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.GL.ADL.Batch.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.GL.ADL.Batch.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.GL.ADL.Batch.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.GL.ADL.Batch.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.Objects.GL.ADL.Batch.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.GL.ADL.Batch.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)
PX.Objects.GL.ADL.Batch.GLAllocationHistoryCollection -> Collection(PX.Objects.GL.GLAllocationHistory)

# PX.Objects.GL.ADL.Sub (EntityType)

Key: SubCD
Entity sets: PX_Objects_GL_ADL_Sub
Non-filterable, non-selectable: Secured, DeletedDatabaseRecord

PX.Objects.GL.ADL.Sub.SubID : Edm.Int32 "Sub. ID"
PX.Objects.GL.ADL.Sub.SubCD : Edm.String [key] "Subaccount"
PX.Objects.GL.ADL.Sub.Secured : Edm.Boolean "Secured"
PX.Objects.GL.ADL.Sub.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.ADL.Sub.UsersByCreatedByID -> PX.SM.Users
PX.Objects.GL.ADL.Sub.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.GL.ADL.Sub.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.GL.ADL.Sub.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.GL.ADL.Sub.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.GL.ADL.Sub.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.GL.ADL.Sub.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.GL.ADL.Sub.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.GL.ADL.Sub.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.GL.ADL.Sub.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.GL.ADL.Sub.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.GL.ADL.Sub.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.GL.ADL.Sub.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.GL.ADL.Sub.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.GL.ADL.Sub.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.GL.ADL.Sub.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.GL.ADL.Sub.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.GL.ADL.Sub.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.GL.ADL.Sub.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.GL.ADL.Sub.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.GL.ADL.Sub.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.GL.ADL.Sub.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.GL.ADL.Sub.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.GL.ADL.Sub.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.GL.ADL.Sub.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.GL.ADL.Sub.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.GL.ADL.Sub.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.GL.ADL.Sub.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.GL.ADL.Sub.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.GL.ADL.Sub.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.GL.ADL.Sub.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.GL.ADL.Sub.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.GL.ADL.Sub.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.GL.ADL.Sub.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.GL.ADL.Sub.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.GL.ADL.Sub.DRDeferredCodeCollection -> Collection(PX.Objects.DR.DRDeferredCode)
PX.Objects.GL.ADL.Sub.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.GL.ADL.Sub.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.Objects.GL.ADL.Sub.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.GL.ADL.Sub.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.GL.ADL.Sub.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.GL.ADL.Sub.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.GL.ADL.Sub.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.GL.ADL.Sub.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.GL.ADL.Sub.SOOrderTypeCollection -> Collection(PX.Objects.SO.SOOrderType)
PX.Objects.GL.ADL.Sub.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.GL.ADL.Sub.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.GL.ADL.Sub.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.GL.ADL.Sub.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.GL.ADL.Sub.CurrencyCollection -> Collection(PX.Objects.CM.Currency)
PX.Objects.GL.ADL.Sub.GLBudgetLineCollection -> Collection(PX.Objects.GL.GLBudgetLine)
PX.Objects.GL.ADL.Sub.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.GL.ADL.Sub.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.GL.ADL.Sub.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.GL.ADL.Sub.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.GL.ADL.Sub.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.GL.ADL.Sub.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.GL.ADL.Sub.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.GL.ADL.Sub.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.GL.ADL.Sub.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.GL.ADL.Sub.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.GL.ADL.Sub.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.GL.ADL.Sub.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.GL.ADL.Sub.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.GL.ADL.Sub.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.GL.ADL.Sub.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.GL.ADL.Sub.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.GL.ADL.Sub.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.GL.ADL.Sub.INCostStatusCollection -> Collection(PX.Objects.IN.INCostStatus)
PX.Objects.GL.ADL.Sub.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.GL.ADL.Sub.TXImportStateCollection -> Collection(PX.Objects.TX.TXImportState)
PX.Objects.GL.ADL.Sub.TXSetupCollection -> Collection(PX.Objects.TX.TXSetup)
PX.Objects.GL.ADL.Sub.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.GL.ADL.Sub.RQRequestClassCollection -> Collection(PX.Objects.RQ.RQRequestClass)
PX.Objects.GL.ADL.Sub.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.GL.ADL.Sub.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.GL.ADL.Sub.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.GL.ADL.Sub.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.GL.ADL.Sub.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.GL.ADL.Sub.POSetupCollection -> Collection(PX.Objects.PO.POSetup)
PX.Objects.GL.ADL.Sub.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.GL.ADL.Sub.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.Objects.GL.ADL.Sub.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.GL.ADL.Sub.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.GL.ADL.Sub.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.GL.ADL.Sub.FADisposalMethodCollection -> Collection(PX.Objects.FA.FADisposalMethod)
PX.Objects.GL.ADL.Sub.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.GL.ADL.Sub.FASetupCollection -> Collection(PX.Objects.FA.FASetup)
PX.Objects.GL.ADL.Sub.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.GL.ADL.Sub.CarrierCollection -> Collection(PX.Objects.CS.Carrier)
PX.Objects.GL.ADL.Sub.ReasonCodeCollection -> Collection(PX.Objects.CS.ReasonCode)
PX.Objects.GL.ADL.Sub.INComponentCollection -> Collection(PX.Objects.IN.INComponent)
PX.Objects.GL.ADL.Sub.INPIHeaderCollection -> Collection(PX.Objects.IN.INPIHeader)
PX.Objects.GL.ADL.Sub.INPostClassCollection -> Collection(PX.Objects.IN.INPostClass)
PX.Objects.GL.ADL.Sub.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.GL.ADL.Sub.INTranCostCollection -> Collection(PX.Objects.IN.INTranCost)
PX.Objects.GL.ADL.Sub.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.GL.ADL.Sub.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.Objects.GL.ADL.Sub.GLAllocationDestinationCollection -> Collection(PX.Objects.GL.GLAllocationDestination)
PX.Objects.GL.ADL.Sub.GLAllocationSourceCollection -> Collection(PX.Objects.GL.GLAllocationSource)
PX.Objects.GL.ADL.Sub.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)
PX.Objects.GL.ADL.Sub.GLBudgetTreeCollection -> Collection(PX.Objects.GL.GLBudgetTree)
PX.Objects.GL.ADL.Sub.GLSetupCollection -> Collection(PX.Objects.GL.GLSetup)
PX.Objects.GL.ADL.Sub.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.GL.ADL.Sub.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.GL.ADL.Sub.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.GL.ADL.Sub.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.GL.ADL.Sub.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.GL.ADL.Sub.CASetupCollection -> Collection(PX.Objects.CA.CASetup)
PX.Objects.GL.ADL.Sub.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.Objects.GL.ADL.Sub.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.GL.ADL.Sub.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.GL.ADL.Sub.ARFinChargeCollection -> Collection(PX.Objects.AR.ARFinCharge)
PX.Objects.GL.ADL.Sub.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.GL.ADL.Sub.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.GL.ADL.Sub.SalesPersonCollection -> Collection(PX.Objects.AR.SalesPerson)
PX.Objects.GL.ADL.Sub.EPDepartmentCollection -> Collection(PX.Objects.EP.EPDepartment)
PX.Objects.GL.ADL.Sub.EPEquipmentCollection -> Collection(PX.Objects.EP.EPEquipment)
PX.Objects.GL.ADL.Sub.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.GL.ADL.Sub.BCBindingAmazonCollection -> Collection(PX.Commerce.Amazon.BCBindingAmazon)
PX.Objects.GL.ADL.Sub.AMLaborCodeCollection -> Collection(PX.Objects.AM.AMLaborCode)
PX.Objects.GL.ADL.Sub.AMMachCollection -> Collection(PX.Objects.AM.AMMach)
PX.Objects.GL.ADL.Sub.AMOrderTypeCollection -> Collection(PX.Objects.AM.AMOrderType)
PX.Objects.GL.ADL.Sub.AMOverheadCollection -> Collection(PX.Objects.AM.AMOverhead)
PX.Objects.GL.ADL.Sub.AMToolMstCollection -> Collection(PX.Objects.AM.AMToolMst)
PX.Objects.GL.ADL.Sub.AMWCMachCollection -> Collection(PX.Objects.AM.AMWCMach)
PX.Objects.GL.ADL.Sub.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.GL.ADL.Sub.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.GL.ADL.Sub.PRPayGroupCollection -> Collection(PX.Objects.PR.PRPayGroup)
PX.Objects.GL.ADL.Sub.PRPTOBankCollection -> Collection(PX.Objects.PR.PRPTOBank)
PX.Objects.GL.ADL.Sub.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.GL.ADL.Sub.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.GL.ADL.Sub.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.GL.ADL.Sub.SVOrderGLAccountCollection -> Collection(PX.Objects.SV.SVOrderGLAccount)
PX.Objects.GL.ADL.Sub.SVOrderTypeGLAccountCollection -> Collection(PX.Objects.SV.SVOrderTypeGLAccount)
PX.Objects.GL.ADL.Sub.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.GL.ADL.Sub.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.GL.ADL.Sub.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.GL.ADL.Sub.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.GL.ADL.Sub.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.GL.ADL.Sub.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.GL.ADL.Sub.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.Objects.GL.ADL.Sub.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.GL.ADL.Sub.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.GL.ADL.Sub.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.GL.ADL.Sub.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.GL.ADL.Sub.ArmGLHistoryByPeriodCollection -> Collection(PX.Objects.CS.ArmGLHistoryByPeriod)
PX.Objects.GL.ADL.Sub.BranchAcctMapFromCollection -> Collection(PX.Objects.GL.BranchAcctMapFrom)
PX.Objects.GL.ADL.Sub.BranchAcctMapToCollection -> Collection(PX.Objects.GL.BranchAcctMapTo)
PX.Objects.GL.ADL.Sub.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.Objects.GL.ADL.Sub.GLHistoryByPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByPeriod)
PX.Objects.GL.ADL.Sub.GLHistoryByCurrentPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByCurrentPeriod)
PX.Objects.GL.ADL.Sub.GLHistoryLastRevaluationCollection -> Collection(PX.Objects.GL.GLHistoryLastRevaluation)
PX.Objects.GL.ADL.Sub.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.GL.ADL.Sub.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.GL.ADL.Sub.LocationARAccountSubCollection -> Collection(PX.Objects.CR.LocationARAccountSub)
PX.Objects.GL.ADL.Sub.LocationAPAccountSubCollection -> Collection(PX.Objects.AP.LocationAPAccountSub)
PX.Objects.GL.ADL.Sub.DRSetupCollection -> Collection(PX.Objects.DR.DRSetup)
PX.Objects.GL.ADL.Sub.INItemCostHistCollection -> Collection(PX.Objects.IN.INItemCostHist)
PX.Objects.GL.ADL.Sub.INUpdateStdCostRecordCollection -> Collection(PX.Objects.IN.INUpdateStdCostRecord)
PX.Objects.GL.ADL.Sub.INItemCostHistByPeriodCollection -> Collection(PX.Objects.IN.INItemCostHistByPeriod)
PX.Objects.GL.ADL.Sub.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.GL.ADL.Sub.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.GL.ADL.Sub.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.GL.ADL.Sub.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.GL.Batch (EntityType)

Label: "GL Batch"
Key: BatchNbr, Module
Entity sets: PX_Objects_GL_Batch, GLBatch, Batch
Non-filterable, non-selectable: NoteText, ReverseCount, HasRamainingAmount, ReleasedToVerify, PostedToVerify, ApproverID, ApproverWorkgroupID, CuryRate, CuryViewState, DeletedDatabaseRecord

PX.Objects.GL.Batch.Module : Edm.String [key] "Module"
PX.Objects.GL.Batch.BatchNbr : Edm.String [key] "Batch Number"
PX.Objects.GL.Batch.LedgerID : Edm.Int32 "Ledger"
PX.Objects.GL.Batch.DateEntered : Edm.DateTimeOffset "Transaction Date"
PX.Objects.GL.Batch.FinPeriodID : Edm.String "Post Period"
PX.Objects.GL.Batch.BatchType : Edm.String "Type"
PX.Objects.GL.Batch.NumberCode : Edm.String "Number. Code"
PX.Objects.GL.Batch.RefNbr : Edm.String "RefNbr"
PX.Objects.GL.Batch.Status : Edm.String "Status"
PX.Objects.GL.Batch.CuryDebitTotal : Edm.Decimal "Debit Total"
PX.Objects.GL.Batch.CuryCreditTotal : Edm.Decimal "Credit Total"
PX.Objects.GL.Batch.CuryControlTotal : Edm.Decimal "Control Total"
PX.Objects.GL.Batch.DebitTotal : Edm.Decimal
PX.Objects.GL.Batch.CreditTotal : Edm.Decimal
PX.Objects.GL.Batch.ControlTotal : Edm.Decimal
PX.Objects.GL.Batch.CuryInfoID : Edm.Int64
PX.Objects.GL.Batch.AutoReverse : Edm.Boolean "Auto Reversing"
PX.Objects.GL.Batch.AutoReverseCopy : Edm.Boolean "Reversing Entry"
PX.Objects.GL.Batch.OrigModule : Edm.String "Orig. Module"
PX.Objects.GL.Batch.OrigBatchNbr : Edm.String "Orig. Batch Number"
PX.Objects.GL.Batch.Released : Edm.Boolean "Released"
PX.Objects.GL.Batch.Posted : Edm.Boolean "Posted"
PX.Objects.GL.Batch.RequirePost : Edm.Boolean
PX.Objects.GL.Batch.PostErrorCount : Edm.Int32
PX.Objects.GL.Batch.Draft : Edm.Boolean [required]
PX.Objects.GL.Batch.TranPeriodID : Edm.String
PX.Objects.GL.Batch.LineCntr : Edm.Int32 [required]
PX.Objects.GL.Batch.CuryID : Edm.String "Currency"
PX.Objects.GL.Batch.ScheduleID : Edm.String
PX.Objects.GL.Batch.NoteID : Edm.Guid
PX.Objects.GL.Batch.NoteText : Edm.String "Note Text"
PX.Objects.GL.Batch.tstamp : Edm.Binary
PX.Objects.GL.Batch.CreatedByID : Edm.Guid "Created By"
PX.Objects.GL.Batch.CreatedByScreenID : Edm.String
PX.Objects.GL.Batch.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.GL.Batch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.GL.Batch.LastModifiedByScreenID : Edm.String
PX.Objects.GL.Batch.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.GL.Batch.Hold : Edm.Boolean [required] "Hold"
PX.Objects.GL.Batch.Scheduled : Edm.Boolean [required]
PX.Objects.GL.Batch.Voided : Edm.Boolean [required] "Voided"
PX.Objects.GL.Batch.Description : Edm.String "Description"
PX.Objects.GL.Batch.CreateTaxTrans : Edm.Boolean [required] "Create Tax Transactions"
PX.Objects.GL.Batch.SkipTaxValidation : Edm.Boolean [required] "Skip Tax Amount Validation"
PX.Objects.GL.Batch.ReverseCount : Edm.Int32 "Reversing Batches"
PX.Objects.GL.Batch.HasRamainingAmount : Edm.Boolean "HasRamainingAmount"
PX.Objects.GL.Batch.ReleasedToVerify : Edm.Boolean
PX.Objects.GL.Batch.PostedToVerify : Edm.Boolean
PX.Objects.GL.Batch.ApproverID : Edm.Int32 "Owner"
PX.Objects.GL.Batch.ApproverWorkgroupID : Edm.Int32
PX.Objects.GL.Batch.Approved : Edm.Boolean [required]
PX.Objects.GL.Batch.Rejected : Edm.Boolean [required]
PX.Objects.GL.Batch.DontApprove : Edm.Boolean
PX.Objects.GL.Batch.CuryRate : Edm.Decimal
PX.Objects.GL.Batch.CuryViewState : Edm.Boolean
PX.Objects.GL.Batch.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.Batch.BatchByOrigBatchNbr -> PX.Objects.GL.Batch (OrigModule=Module, OrigBatchNbr=BatchNbr)
PX.Objects.GL.Batch.BatchByOrigModule -> PX.Objects.GL.Batch (OrigBatchNbr=BatchNbr, OrigModule=Module)
PX.Objects.GL.Batch.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.GL.Batch.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.GL.Batch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.GL.Batch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.GL.Batch.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.GL.Batch.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.Batch.ScheduleByScheduleID -> PX.Objects.GL.Schedule (ScheduleID=ScheduleID)
PX.Objects.GL.Batch.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.GL.Batch.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.GL.Batch.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.GL.Batch.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.GL.Batch.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.GL.Batch.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.GL.Batch.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.GL.Batch.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.GL.Batch.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.GL.Batch.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.Objects.GL.Batch.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.GL.Batch.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.GL.Batch.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.GL.Batch.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.GL.Batch.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.GL.Batch.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.GL.Batch.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.GL.Batch.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.GL.Batch.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.GL.Batch.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.GL.Batch.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.GL.Batch.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.GL.Batch.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.GL.Batch.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.GL.Batch.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.GL.Batch.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.Objects.GL.Batch.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.GL.Batch.GLTrialBalanceImportMapCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportMap)
PX.Objects.GL.Batch.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.GL.Batch.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.GL.Batch.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.GL.Batch.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.GL.Batch.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.Objects.GL.Batch.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.GL.Batch.AMDisassembleBatchCollection -> Collection(PX.Objects.AM.AMDisassembleBatch)
PX.Objects.GL.Batch.GLAllocationHistoryCollection -> Collection(PX.Objects.GL.GLAllocationHistory)

# PX.Objects.GL.BatchPostedForModule (EntityType)

Label: "GL Batch"
BaseType: PX.Objects.GL.Batch
Key: BatchNbr, Module (inherited from PX.Objects.GL.Batch)
Entity sets: PX_Objects_GL_BatchPostedForModule

# PX.Objects.GL.BatchReport (EntityType)

Label: "GL Batch"
BaseType: PX.Objects.GL.Batch
Key: BatchNbr, Module (inherited from PX.Objects.GL.Batch)
Entity sets: PX_Objects_GL_BatchReport

# PX.Objects.GL.Branch (EntityType)

Label: "Branch"
Key: BranchCD
Entity sets: PX_Objects_GL_Branch, Branch
Non-filterable, non-selectable: BranchOrOrganizationLogoNameReport, LedgerCD, Included, Secured, DeletedDatabaseRecord

PX.Objects.GL.Branch.BranchID : Edm.Int32
PX.Objects.GL.Branch.BranchCD : Edm.String [key] "Branch ID"
PX.Objects.GL.Branch.RoleName : Edm.String "Access Role"
PX.Objects.GL.Branch.LogoName : Edm.String "Logo File"
PX.Objects.GL.Branch.LogoNameReport : Edm.String "Report Logo File"
PX.Objects.GL.Branch.MainLogoName : Edm.String "Logo File"
PX.Objects.GL.Branch.OrganizationLogoNameReport : Edm.String "Organization Logo File"
PX.Objects.GL.Branch.BranchOrOrganizationLogoNameReport : Edm.String "Branch or Organization Report Logo File"
PX.Objects.GL.Branch.LedgerID : Edm.Int32 "Posting Ledger"
PX.Objects.GL.Branch.LedgerCD : Edm.String
PX.Objects.GL.Branch.BAccountID : Edm.Int32 "BAccountID"
PX.Objects.GL.Branch.Active : Edm.Boolean [required] "Active"
PX.Objects.GL.Branch.PhoneMask : Edm.String "Phone Mask"
PX.Objects.GL.Branch.CountryID : Edm.String "Default Country"
PX.Objects.GL.Branch.AcctName : Edm.String "Branch Name"
PX.Objects.GL.Branch.BaseCuryID : Edm.String "Base Currency ID"
PX.Objects.GL.Branch.tstamp : Edm.Binary
PX.Objects.GL.Branch.Included : Edm.Boolean "Included"
PX.Objects.GL.Branch.TCC : Edm.String "Transmitter Control Code (TCC)"
PX.Objects.GL.Branch.ForeignEntity : Edm.Boolean "Foreign Entity"
PX.Objects.GL.Branch.CFSFiler : Edm.Boolean "Combined Federal/State Filer"
PX.Objects.GL.Branch.FirstName : Edm.String "First Name"
PX.Objects.GL.Branch.MiddleName : Edm.String "Middle Name"
PX.Objects.GL.Branch.LastName : Edm.String "Last Name"
PX.Objects.GL.Branch.CTelNumber : Edm.String "Phone Number"
PX.Objects.GL.Branch.PhoneType1099 : Edm.String "Phone Number Type"
PX.Objects.GL.Branch.CEmail : Edm.String "Contact E-mail"
PX.Objects.GL.Branch.NameControl : Edm.String "Name Control"
PX.Objects.GL.Branch.Reporting1099 : Edm.Boolean [required] "1099-MISC Reporting Entity"
PX.Objects.GL.Branch.ParentBranchID : Edm.Int32
PX.Objects.GL.Branch.CarrierFacility : Edm.String "Carrier Facility"
PX.Objects.GL.Branch.OverrideThemeVariables : Edm.Boolean [required] "Override Colors for the Selected Branch"
PX.Objects.GL.Branch.Secured : Edm.Boolean "Secured"
PX.Objects.GL.Branch.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.GL.Branch.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.GL.Branch.RolesByRoleName -> PX.SM.Roles (RoleName=Rolename)
PX.Objects.GL.Branch.SMPrinterByDefaultPrinterID -> PX.SM.SMPrinter
PX.Objects.GL.Branch.OrganizationByOrganizationID -> PX.Objects.GL.DAC.Organization
PX.Objects.GL.Branch.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.GL.Branch.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.GL.Branch.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)
PX.Objects.GL.Branch.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.GL.Branch.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.GL.Branch.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.GL.Branch.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.GL.Branch.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.GL.Branch.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.GL.Branch.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.GL.Branch.PRPaymentWCPremiumCollection -> Collection(PX.Objects.PR.PRPaymentWCPremium)
PX.Objects.GL.Branch.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.GL.Branch.PRWorkCompensationBenefitRateCollection -> Collection(PX.Objects.PR.PRWorkCompensationBenefitRate)
PX.Objects.GL.Branch.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.GL.Branch.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.GL.Branch.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.GL.Branch.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.GL.Branch.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.GL.Branch.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.GL.Branch.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.GL.Branch.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.GL.Branch.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.GL.Branch.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.GL.Branch.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.GL.Branch.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.GL.Branch.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.Objects.GL.Branch.NotificationSetupCollection -> Collection(PX.Objects.CS.NotificationSetup)
PX.Objects.GL.Branch.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.GL.Branch.RQRequisitionLineCollection -> Collection(PX.Objects.RQ.RQRequisitionLine)
PX.Objects.GL.Branch.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.GL.Branch.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.GL.Branch.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.GL.Branch.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.GL.Branch.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.GL.Branch.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.GL.Branch.FATranCollection -> Collection(PX.Objects.FA.FATran)
PX.Objects.GL.Branch.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.GL.Branch.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.GL.Branch.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.GL.Branch.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.GL.Branch.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.GL.Branch.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.GL.Branch.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.Objects.GL.Branch.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.GL.Branch.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.GL.Branch.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.GL.Branch.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.GL.Branch.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.GL.Branch.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.GL.Branch.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.GL.Branch.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.GL.Branch.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.GL.Branch.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.GL.Branch.GLAllocationCollection -> Collection(PX.Objects.GL.GLAllocation)
PX.Objects.GL.Branch.GLTrialBalanceImportDetailsCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportDetails)
PX.Objects.GL.Branch.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.GL.Branch.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.GL.Branch.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.GL.Branch.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.GL.Branch.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.GL.Branch.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.GL.Branch.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.GL.Branch.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.GL.Branch.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.GL.Branch.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.GL.Branch.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.GL.Branch.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.GL.Branch.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.Objects.GL.Branch.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.GL.Branch.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.GL.Branch.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.GL.Branch.GLBudgetLineCollection -> Collection(PX.Objects.GL.GLBudgetLine)
PX.Objects.GL.Branch.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.GL.Branch.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.GL.Branch.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.GL.Branch.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.GL.Branch.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.GL.Branch.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.GL.Branch.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.GL.Branch.AMBatchCollection -> Collection(PX.Objects.AM.AMBatch)
PX.Objects.GL.Branch.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.GL.Branch.MISC1099EFileProcessingInfoRawCollection -> Collection(PX.Objects.AP.MISC1099EFileProcessingInfoRaw)
PX.Objects.GL.Branch.AP1099HistoryCollection -> Collection(PX.Objects.AP.AP1099History)
PX.Objects.GL.Branch.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.GL.Branch.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.GL.Branch.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.GL.Branch.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.GL.Branch.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.GL.Branch.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.GL.Branch.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.GL.Branch.TaxPluginMappingCollection -> Collection(PX.Objects.TX.TaxPluginMapping)
PX.Objects.GL.Branch.SOPickPackShipSetupCollection -> Collection(PX.Objects.SO.SOPickPackShipSetup)
PX.Objects.GL.Branch.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.GL.Branch.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.GL.Branch.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.GL.Branch.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.GL.Branch.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.GL.Branch.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.GL.Branch.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.GL.Branch.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.GL.Branch.PMBillingRuleCollection -> Collection(PX.Objects.PM.PMBillingRule)
PX.Objects.GL.Branch.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.GL.Branch.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.GL.Branch.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.GL.Branch.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.GL.Branch.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.GL.Branch.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.GL.Branch.FARegisterCollection -> Collection(PX.Objects.FA.FARegister)
PX.Objects.GL.Branch.DRScheduleTranCollection -> Collection(PX.Objects.DR.DRScheduleTran)
PX.Objects.GL.Branch.NotificationSourceCollection -> Collection(PX.Objects.CS.NotificationSource)
PX.Objects.GL.Branch.NumberingSequenceCollection -> Collection(PX.Objects.CS.NumberingSequence)
PX.Objects.GL.Branch.INScanSetupCollection -> Collection(PX.Objects.IN.INScanSetup)
PX.Objects.GL.Branch.INSetupCollection -> Collection(PX.Objects.IN.INSetup)
PX.Objects.GL.Branch.INSiteBuildingCollection -> Collection(PX.Objects.IN.INSiteBuilding)
PX.Objects.GL.Branch.INTurnoverCalcCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalc)
PX.Objects.GL.Branch.INTurnoverCalcItemCollection -> Collection(PX.Objects.IN.Turnover.INTurnoverCalcItem)
PX.Objects.GL.Branch.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.Objects.GL.Branch.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.GL.Branch.TranslDefCollection -> Collection(PX.Objects.CM.TranslDef)
PX.Objects.GL.Branch.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.Objects.GL.Branch.GLAllocationDestinationCollection -> Collection(PX.Objects.GL.GLAllocationDestination)
PX.Objects.GL.Branch.GLAllocationSourceCollection -> Collection(PX.Objects.GL.GLAllocationSource)
PX.Objects.GL.Branch.GLBudgetCollection -> Collection(PX.Objects.GL.GLBudget)
PX.Objects.GL.Branch.GLBudgetLineDetailCollection -> Collection(PX.Objects.GL.GLBudgetLineDetail)
PX.Objects.GL.Branch.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.GL.Branch.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.GL.Branch.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.GL.Branch.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.GL.Branch.CACorpCardCollection -> Collection(PX.Objects.CA.CACorpCard)
PX.Objects.GL.Branch.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.GL.Branch.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.GL.Branch.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.GL.Branch.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.Objects.GL.Branch.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.GL.Branch.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.GL.Branch.CCProcessingCenterPmntMethodBranchCollection -> Collection(PX.Objects.CA.CCProcessingCenterPmntMethodBranch)
PX.Objects.GL.Branch.BuildingCollection -> Collection(PX.Objects.CR.Building)
PX.Objects.GL.Branch.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.GL.Branch.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.GL.Branch.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.GL.Branch.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.GL.Branch.DiscountBranchCollection -> Collection(PX.Objects.AR.DiscountBranch)
PX.Objects.GL.Branch.BCBindingCollection -> Collection(PX.Commerce.Core.BCBinding)
PX.Objects.GL.Branch.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.GL.Branch.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.GL.Branch.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.GL.Branch.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.GL.Branch.AMMPSCollection -> Collection(PX.Objects.AM.AMMPS)
PX.Objects.GL.Branch.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.GL.Branch.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.GL.Branch.FSBranchLocationCollection -> Collection(PX.Objects.FS.FSBranchLocation)
PX.Objects.GL.Branch.FSMasterContractCollection -> Collection(PX.Objects.FS.FSMasterContract)
PX.Objects.GL.Branch.FSRouteCollection -> Collection(PX.Objects.FS.FSRoute)
PX.Objects.GL.Branch.FSRouteDocumentCollection -> Collection(PX.Objects.FS.FSRouteDocument)
PX.Objects.GL.Branch.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.GL.Branch.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.GL.Branch.T4AMasterTableCollection -> Collection(PX.Objects.Localizations.CA.T4AMasterTable)
PX.Objects.GL.Branch.PRLocationCollection -> Collection(PX.Objects.PR.PRLocation)
PX.Objects.GL.Branch.PRPaymentBatchExportDetailsCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportDetails)
PX.Objects.GL.Branch.PRRecordOfEmploymentCollection -> Collection(PX.Objects.PR.PRRecordOfEmployment)
PX.Objects.GL.Branch.SVInvoiceCollection -> Collection(PX.Objects.SV.SVInvoice)
PX.Objects.GL.Branch.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.GL.Branch.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.GL.Branch.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.GL.Branch.SVServiceLocationCollection -> Collection(PX.Objects.SV.SVServiceLocation)
PX.Objects.GL.Branch.SVStagingWarehouseCollection -> Collection(PX.Objects.SV.SVStagingWarehouse)
PX.Objects.GL.Branch.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.GL.Branch.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.GL.Branch.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.GL.Branch.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.GL.Branch.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.GL.Branch.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.GL.Branch.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.GL.Branch.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.GL.Branch.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.Objects.GL.Branch.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.GL.Branch.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.GL.Branch.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.GL.Branch.TaxHistorySumCollection -> Collection(PX.Objects.TX.TaxHistorySum)
PX.Objects.GL.Branch.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.GL.Branch.FAProjectedGLTranCollection -> Collection(PX.Objects.FA.FAProjectedGLTran)
PX.Objects.GL.Branch.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.GL.Branch.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.GL.Branch.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.GL.Branch.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.GL.Branch.ArmGLHistoryByPeriodCollection -> Collection(PX.Objects.CS.ArmGLHistoryByPeriod)
PX.Objects.GL.Branch.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.GL.Branch.CCProcessingCenterBranchCollection -> Collection(PX.Objects.CC.CCProcessingCenterBranch)
PX.Objects.GL.Branch.BranchAcctMapFromCollection -> Collection(PX.Objects.GL.BranchAcctMapFrom)
PX.Objects.GL.Branch.BranchAcctMapToCollection -> Collection(PX.Objects.GL.BranchAcctMapTo)
PX.Objects.GL.Branch.GLAllocationAccountHistoryCollection -> Collection(PX.Objects.GL.GLAllocationAccountHistory)
PX.Objects.GL.Branch.GLConsolSetupCollection -> Collection(PX.Objects.GL.GLConsolSetup)
PX.Objects.GL.Branch.GLHistorySummaryCollection -> Collection(PX.Objects.GL.GLHistorySummary)
PX.Objects.GL.Branch.GLHistoryByPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByPeriod)
PX.Objects.GL.Branch.GLHistoryByCurrentPeriodCollection -> Collection(PX.Objects.GL.GLHistoryByCurrentPeriod)
PX.Objects.GL.Branch.GLHistoryByPeriodCurrentCollection -> Collection(PX.Objects.GL.GLHistoryByPeriodCurrent)
PX.Objects.GL.Branch.GLHistoryByPeriodMasterCurrentCollection -> Collection(PX.Objects.GL.GLHistoryByPeriodMasterCurrent)
PX.Objects.GL.Branch.GLHistoryLastRevaluationCollection -> Collection(PX.Objects.GL.GLHistoryLastRevaluation)
PX.Objects.GL.Branch.PaymentMethodAccountCollection -> Collection(PX.Objects.CA.PaymentMethodAccount)
PX.Objects.GL.Branch.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.Objects.GL.Branch.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.GL.Branch.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.GL.Branch.APHistoryByPeriodCollection -> Collection(PX.Objects.AP.APHistoryByPeriod)
PX.Objects.GL.Branch.BaseAPHistoryByPeriodCollection -> Collection(PX.Objects.AP.BaseAPHistoryByPeriod)
PX.Objects.GL.Branch.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.GL.Branch.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.GL.Branch.AMRPPlanCollection -> Collection(PX.Objects.AM.AMRPPlan)
PX.Objects.GL.Branch.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.GL.Branch.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.GL.Branch.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)
PX.Objects.GL.Branch.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.GL.Branch.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.GL.Branch.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.GL.Branch.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)
PX.Objects.GL.Branch.AUScheduleCollection -> Collection(PX.SM.AUSchedule)
PX.Objects.GL.Branch.UserPreferencesCollection -> Collection(PX.SM.UserPreferences)
PX.Objects.GL.Branch.FSTimeSlotCollection -> Collection(PX.Objects.FS.FSTimeSlot)

# PX.Objects.GL.BranchAcctMapFrom (EntityType)

Label: "Branch Account Map From"
Key: BranchID, LineNbr
Entity sets: PX_Objects_GL_BranchAcctMapFrom, BranchAccountMapFrom, BranchAcctMapFrom

PX.Objects.GL.BranchAcctMapFrom.BranchID : Edm.Int32 [key]
PX.Objects.GL.BranchAcctMapFrom.LineNbr : Edm.Int32 [key]
PX.Objects.GL.BranchAcctMapFrom.FromBranchID : Edm.Int32
PX.Objects.GL.BranchAcctMapFrom.ToBranchID : Edm.Int32 "Destination Branch"
PX.Objects.GL.BranchAcctMapFrom.FromAccountCD : Edm.String "Account From"
PX.Objects.GL.BranchAcctMapFrom.ToAccountCD : Edm.String "Account To"
PX.Objects.GL.BranchAcctMapFrom.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.BranchAcctMapFrom.BranchByFromBranchID -> PX.Objects.GL.Branch (FromBranchID=BranchID)
PX.Objects.GL.BranchAcctMapFrom.BranchByToBranchID -> PX.Objects.GL.Branch (ToBranchID=BranchID)
PX.Objects.GL.BranchAcctMapFrom.AccountByFromAccountCD -> PX.Objects.GL.Account (FromAccountCD=AccountCD)
PX.Objects.GL.BranchAcctMapFrom.AccountByToAccountCD -> PX.Objects.GL.Account (ToAccountCD=AccountCD)
PX.Objects.GL.BranchAcctMapFrom.AccountByMapAccountID -> PX.Objects.GL.Account
PX.Objects.GL.BranchAcctMapFrom.SubByMapSubID -> PX.Objects.GL.Sub

# PX.Objects.GL.BranchAcctMapTo (EntityType)

Label: "Branch Account Map To"
Key: BranchID, LineNbr
Entity sets: PX_Objects_GL_BranchAcctMapTo, BranchAccountMapTo, BranchAcctMapTo

PX.Objects.GL.BranchAcctMapTo.BranchID : Edm.Int32 [key]
PX.Objects.GL.BranchAcctMapTo.LineNbr : Edm.Int32 [key]
PX.Objects.GL.BranchAcctMapTo.FromBranchID : Edm.Int32 "Destination Branch"
PX.Objects.GL.BranchAcctMapTo.ToBranchID : Edm.Int32
PX.Objects.GL.BranchAcctMapTo.FromAccountCD : Edm.String "Account From"
PX.Objects.GL.BranchAcctMapTo.ToAccountCD : Edm.String "Account To"
PX.Objects.GL.BranchAcctMapTo.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.GL.BranchAcctMapTo.BranchByFromBranchID -> PX.Objects.GL.Branch (FromBranchID=BranchID)
PX.Objects.GL.BranchAcctMapTo.BranchByToBranchID -> PX.Objects.GL.Branch (ToBranchID=BranchID)
PX.Objects.GL.BranchAcctMapTo.AccountByFromAccountCD -> PX.Objects.GL.Account (FromAccountCD=AccountCD)
PX.Objects.GL.BranchAcctMapTo.AccountByToAccountCD -> PX.Objects.GL.Account (ToAccountCD=AccountCD)
PX.Objects.GL.BranchAcctMapTo.AccountByMapAccountID -> PX.Objects.GL.Account
PX.Objects.GL.BranchAcctMapTo.SubByMapSubID -> PX.Objects.GL.Sub

# PX.Objects.GL.CAExpenseBranch (EntityType)

Label: "Branch"
BaseType: PX.Objects.GL.Branch
Key: BranchCD (inherited from PX.Objects.GL.Branch)
Entity sets: PX_Objects_GL_CAExpenseBranch
