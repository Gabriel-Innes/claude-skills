<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BusinessPartners (Object)

BusinessPartners is a business object that represents the Business Partners Master Data in the Business Partners module. This object enables you to: - Add a business partner record. - Retrieve a business partner record by its key. - Update a business partner record. - Remove a business partner record. - Save the object in XML format. Source table: OCRD.

**Remarks:** To display the form in the application: - Select Business Partners --> Business Partner Master Data.

## Properties (249)
- `Public Property AcceptsEndorsedChecks() As BoYesNoEnum` [R/W] property AcceptsEndorsedChecks
- `Public Property AccountRecivablePayables() As BPAccountReceivablePayble` [R] Returns the BPAccountReceivablePayble object. Field name: DebPayAcct. Length: 15 characters.
- `Public Property AccrualCriteria() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether the business partner reports on accrual basis or cash basis. Field name: AccCritria.
  - remarks: Accrual basis: tYES. Cash basis: tNO.
- `Public Property AdditionalID() As String` [R/W] Sets or returns an additional ID number of the business partner (that is, in addition to the CardCode). Field name: AddID. Length: 18 characters.
- `Public Property Address() As String` [R/W] Sets or returns the street of the Bill To address, which is the address of the physical location of the business partner. Field name: Address. Length: 100 characters.
  - remarks: Use this property only if the physical address is different from the Ship To address (mailing address). If you do not set this property, when adding a new business partner card, SAP Business One will copy the data from the MailAddress property.
- `Public Property Addresses() As BPAddresses` [R] Returns the BPAddresses object. Field name: None.
- `Public Property Affiliate() As BoYesNoEnum` [R/W] Indicates whether the business partner is an affiliate. Field name: Affiliate.
  - remarks: The property is for SAP Business One integration for SAP NetWeaver - Subsidiary Integration.
- `Public Property AgentCode() As String` [R/W] property AgentCode
- `Public Property AliasName() As String` [R/W] property AliasName
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property AutomaticPosting() As AutomaticPostingEnum` [R/W] property AutomaticPosting
- `Public Property AvarageLate() As Long` [R/W] Sets or returns the average delay in days for the customer's payments. Field name: AvrageLate.
  - remarks: Setting a value in this field adjusts the value dates of the custome'r debts in the Cash Flow report.
- `Public Property BackOrder() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to enable partial items and partial quantities in sales order documents. Field name: BackOrder.
  - remarks: To enable backorders set also the PartialDelivery property to tYES. Backorder enables you to change the commitments and over-ride the blockage of stocks marked against sales documents/deliveries. For example, you receive an order from a very important customer for material "A" but the entire quantity of A is committed to another customer "B" via earlier sales orders and this is where BACKORDER processing helps you to change the committment and shift stock due for B to A. This is the benefit of this functionality.
- `Public Property BankChargesAllocationCode() As String` [R/W] Sets or returns the default bank charges allocation code. Field name: DflBCACode. This is a foreign key to the Bank Charges Allocation Codes object, OBCA, not exposed through the DI API).
- `Public Property BankCountry() As String` [R/W] Sets or returns the country of the business partner bank account. Field name: BankCountr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property BillofExchangeonCollection() As String` [R/W] Sets or returns the G/L account number for bill-of-exchange on collection. Field name: BoEOnClct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property BillToBuildingFloorRoom() As String` [R/W] Sets or returns a memo type string that specifies additional details of the Bill To address, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters.
- `Public Property BilltoDefault() As String` [R/W] Sets or returns the default Bill To address name. Field name: BillToDef. Length: 50 characters.
- `Public Property BillToState() As String` [R/W] Sets or returns the state of the Bill To address, which is the address of the physical location of the business partner. Field name: State1. Length: 3 characters. This is a foreign key to the Countries table (OCST - not exposed through the DI API).
- `Public Property Block() As String` [R/W] Sets or returns the block of the Bill To address, which is the address of the physical location of the business partner. Field name: Block. Length: 100 characters.
- `Public Property BlockDunning() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to block dunning letters to the business partner. Field name: BlockDunn. Length: 1 character.
- `Public Property BlockSendingMarketingContent() As BoYesNoEnum` [R/W] Specifies whether or not to block sending marketing contnet to the business partner. Field name: BlockComm. Length: 1 character.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
            SAPbobsCOM.BusinessPartners oBP=g_Company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oBusinessPartners);

            oBP.CardCode = "C001";

            oBP.BlockSendingMarketingContent = SAPbobsCOM.BoYesNoEnum.tYES;

            oBP.BPBlockSendingMarketingContents.CommunicationMediaId = -2;

            oBP.BPBlockSendingMarketingContents.Choose = SAPbobsCOM.BoYesNoEnum.tYES;

            SAPbobsCOM.ContactEmployees oCP = oBP.ContactEmployees;

            oCP.SetCurrentLine(0);

            oCP.Name = "CP1";

            oCP.LastName = "LN";

            oCP.BlockSendingMarketingContent = SAPbobsCOM.BoYesNoEnum.tYES;

            oCP.ContactEmployeeBlockSendingMarketingContents.CommunicationMediaId = -1;

            oCP.ContactEmployeeBlockSendingMarketingContents.Choose = SAPbobsCOM.BoYesNoEnum.tYES;

            int retCode = oBP.Add();
    ```
- `Public Property BookkeepingCertified() As BoYesNoEnum` [R/W] property BookkeepingCertified
- `Public Property Box1099() As String` [R/W] Sets or returns the number of Box 1099 on the Form 1099 where the payment should be entered. Field name: Box1099. Length: 20 characters.
  - remarks: Country-specific property for USA. Set this property only if you set FormCode1099 Property for a business partner that requires a 1099 statement.
- `Public Property BPBankAccounts() As BPBankAccounts` [R] Returns the BPBankAccounts object.
- `Public Property BPBlockSendingMarketingContents() As BPBlockSendingMarketingContents` [R] Returns the BPBlockSendingMarketingContents object.
- `Public Property BPBranchAssignment() As BPBranchAssignment` [R] property BPBranchAssignment
- `Public Property BPCurrencies() As BPCurrencies` [R] property BPCurrencies
- `Public Property BPPaymentDates() As BPPaymentDates` [R] Returns the BPPaymentDates object.
- `Public Property BPPaymentMethods() As BPPaymentMethods` [R] Returns the BPPaymentMethods object.
- `Public Property BPWithholdingTax() As BPWithholdingTax` [R] Returns the BPWithholdingTax object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BusinessType() As String` [R/W] property BusinessType
- `Public Property CampaignNumber() As Long` [R/W] property CampaignNumber
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner identification key in SAP Business One. Field name: CardCode. Mandatory property. Length: 15 characters.
  - remarks: SAP Business One validates the CardCode, and if not valid, returns an error code. The card code is the primary key of the business partners records in SAP Business One. You can use this property to search and display business partners records.
- `Public Property CardForeignName() As String` [R/W] Sets or returns the business partner's foreign name. Field name: CardFName. Length: 100 characters.
  - remarks: Use this property when you exchange documents with foreign companies, for example, to send an invoice to a customer abroad.
- `Public Property CardName() As String` [R/W] Sets or returns the business partner's full name. Field name: CardFName. Length: 100 characters.
  - remarks: You can use this property to represent company's name, organization name, person name, or any other entity that represents the business partner.
- `Public Property CardType() As BoCardTypes` [R/W] Sets or returns a valid value of BoCardTypes type that specifies the type of the business partner (customer, supplier, or lead). Field name: CardType.
  - remarks: In SAP Business One, for a business partner that its type is both customer and supplier create two sperate cards, one as a customer and the other as a supplier.
- `Public Property Cellular() As String` [R/W] Sets or returns the cellular phone number of the business partner. Field name: Cellular. Length: 50 characters.
- `Public Property CertificateDetails() As String` [R/W] property CertificateDetails
- `Public Property CertificateNumber() As String` [R/W] Sets or returns the number of the withholding tax certificate. Field name: CrtfcateNO. Length: 20 characters.
- `Public Property ChannelBP() As String` [R/W] Sets or returns the distribution channel card code for the business partner (the distribution channel is also a business partner). Relevant to business partners of customer type only. Field name: ChannlBP. Length: 15 characters.
- `Public Property City() As String` [R/W] Sets or returns the city of the Bill To address, which is the address of the physical location of the business partner. Field name: City. Length: 100 characters.
  - remarks: Set the City property only if the physical city is different from the value in the MailCity property. If you do not set the City property, SAP Business One copies the value from the MailCity property.
- `Public Property ClosingDateProcedureNumber() As Long` [R/W] Sets or returns the Closing Date Procedure Number. This is a foreign key to the ClosingDateProcedure object. Field name: CDPNum.
  - remarks: The ClosingDateProcedure object is applicable for cluster B (country-specific for Japan only).
- `Public Property CollectionAuthorization() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the business partner has authorized automatic collections from its bank account. Field name: CollecAuth. Length: 1 characters.
- `Public Property CommissionGroupCode() As Long` [R/W] Sets or returns the commission group number for the business partner. Field name: CommGrCode. This is a foreign key to the CommissionGroups object.
  - remarks: SAP Business One uses commission groups to manage commissions. Each customer is assigned to a specific commission group. When you create a business document, the commission value from CommissionPercent property or the value from commission group is copied to the business document.
- `Public Property CommissionPercent() As Double` [R/W] Sets or returns the commission percentage for the business partner. Field name: Commission.
  - remarks: SAP Business One uses commission groups to manage commissions. However, if a customer does not belong to any commission group, you can assign it with a specific commission percentage. When you create a business document, this value or the value from commission group is copied to the business document.
- `Public Property CompanyPrivate() As BoCardCompanyTypes` [R/W] Sets or returns a valid value that determines wether the user is a Company or a Private person. Field name: CmpPrivate.
- `Public Property CompanyRegistrationNumber() As String` [R/W] Sets or returns the Company Registration Number (CRN) of the business partner. This number is used as a means of identification in contacts with government authorities and other organizations. Field name: RegNum). Length: 32 characters.
- `Public Property ContactEmployees() As ContactEmployees` [R] Returns the ContactEmployees object that represents the employees responsible for this business partner.
- `Public Property ContactPerson() As String` [R/W] Sets or returns the contact person for this Business Partner. Field name: CntctPrsn.
- `Public Property Country() As String` [R/W] Sets or returns the country of the Bill To address, which is the address of the physical location of the business partner. Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: Use this property only if the physical address is different from the Ship To address (mailing address). If you do not set this property, when adding a new business partner card, SAP Business One will copy the data from the MailCountry property.
- `Public Property County() As String` [R/W] Sets or returns the county of the Bill To address, which is the address of the physical location of the business partner. Field name: County. Length: 100 characters. This is a foreign key to the States table (OCST - not exposed through the DI API).
  - remarks: Use this property only if the physical address is different from the Ship To address (mailing address). If you do not set this property, when adding a new business partner card, SAP Business One will copy the data from the MailCounty property.
- `Public Property CreateDate() As Date` [R] The date when the business partner master data created. Field name: CreateDate.
- `Public Property CreateTime() As Date` [R] The timestamp of the business partner master data created is recorded in the hhmmss format. Field name: CreateTS.
- `Public Property CreditCardCode() As Long` [R/W] Sets or returns the foreign key of the credit card as defined the CreditCards object. Field name: CreditCard. This is a foreign key to the CreditCards object.
- `Public Property CreditCardExpiration() As Date` [R/W] Sets or returns expiration date for the business partner's credit card. Field name: CardValid.
- `Public Property CreditCardNum() As String` [R/W] Sets or returns the business partner's credit card number. Field name: CrCardNum. Length: 20 characters.
- `Public Property CreditLimit() As Double` [R/W] Sets or returns the credit limit amount for a business partner. Field name: CreditLine.
  - remarks: SAP Business One automatically completes the value for this property from PaymentTermsTypes object (OCTG table) according to the selected payment terms (PayTermsGrpCode property).
- `Public Property Currency() As String` [R/W] Sets or returns the currency used by a business partner in documents. Field name: CRD_CURR. Length: 3 characters.
  - remarks: A business transaction may include more than one currency. In this case, use the GetCurrencyRate method to unify the total amount in different currencies into one currency. The value for multiple currencies is ##. The card currency determines the currency, in which all journal entries and marketing documents for that card will be performed. The card's default currency is the local currency, and it is used for all journal entries.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.BusinessPartners bp = (SAPbobsCOM.BusinessPartners)oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oBusinessPartners);
    bp.CardCode = "C10000";
    bp.Currency = "##";
    bp.DefaultCurrency = "JPY";
    bp.Add();
    ```
- `Public Property CurrentAccountBalance() As Double` [R] Returns the open balance for a specified business partner. Field name: Balance.
  - remarks: If a business transaction is not a Pay-Immediately transaction, the amount of money must be recorded to Account-Payable account or Account-Receivable account, and the open balance for the business partner will then be adjusted accordingly.
- `Public Property CustomerBillofExchangDisc() As String` [R/W] Sets or returns the business partner's G/L account number of type: Bill of Exchange Discounted. Field name: BoEDiscnt. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property CustomerBillofExchangPres() As String` [R/W] Sets or returns the business partner's G/L account number of type: Bill of Exchange Presentation. Field name: BoEDiscnt. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property DatevAccount() As String` [R/W] property DatevAccount
- `Public Property DatevFirstDataEntry() As BoYesNoEnum` [R/W] property DatevFirstDataEntry
- `Public Property DebitorAccount() As String` [R/W] Sets or returns the business partner's accounts receivable/payable number (as defined in chart of accounts). Field name: DebPayAcct. Length: 15 characters.
- `Public Property DeductibleAtSource() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the a business partner must deduct tax from payments. Field name: .
  - remarks: If the property is set to tYes, then the business partner must deduct tax from payments that they will pay to the company. If the property is set to tNo, then the business partner should not deduct tax at source (that is , pay the total including tax), and it is the responsibility of the company to record the tax and profit in a different account, and pay the tax.
- `Public Property DeductionOffice() As String` [R/W] Sets or returns the tax office name that appears on the supplier's tax deduction certificate. Field name: DdctOffice. Length: 10 characters.
- `Public Property DeductionPercent() As Double` [R/W] Sets or returns the deduction percentage as specified in the tax deduction certificate provided by the supplier. Field name: DdctPrcnt.
  - remarks: The deduction percentage specified in the certificate provided by the supplier.
- `Public Property DeductionValidUntil() As Date` [R/W] Sets or returns the expiration date of the tax deduction certificate provided by the supplier. Field name: ValidUntil.
- `Public Property DefaultAccount() As String` [R/W] Sets or returns the default bank account number of the business partner. Field name: DflAccount. Length: 50 characters.
  - remarks: You can use this account number for bank transfer, deposits, and so on.
- `Public Property DefaultBankCode() As String` [R/W] Sets or returns the default bank code of the business partner. Field name: DflBankKey. Length: 30 characters.
- `Public Property DefaultBlanketAgreementNumber() As Long` [R/W] property DefaultBlanketAgreementNumber
- `Public Property DefaultBranch() As String` [R/W] Sets or returns the default branch for the business partner. Field name: DflBranch. Length: 50 characters.
- `Public Property DefaultCurrency() As String` [R/W] property DefaultCurrency
- `Public Property DefaultTechnician() As Long` [R/W] Sets or returns the default technician, as defined in SAP Business One, for the business partner. Relevant to business partners of customer type only. Field name: DfTcnician. This is a foreign key to the EmployeesInfo object.
- `Public Property DefaultTransporterEntry() As Long` [R/W] property DefaultTransporterEntry
- `Public Property DefaultTransporterLineNumber() As Long` [R/W] property DefaultTransporterLineNumber
- `Public Property DeferCommitmentLimitOnDueDate() As BoDeferCommitmentLimitOnDueDateTypes` [R/W] Defer commitment limit on Due Date. Field name: DefCommDDt.
- `Public Property DeferCommitmentLimitOnDueDateDays() As Long` [R/W] Field name: DefCommDay.
- `Public Property DeferCommitmentLimitOnDueDateMonths() As Long` [R/W] Field name: DefCommMon.
- `Public Property DeferredTax() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the business partner applies deferred tax. Field name: DeferrTax. Length: 1 characters.
  - remarks: Country-specific for Spain, Italy, Portugal, and France.
- `Public Property DiscountBaseObject() As DiscountGroupBaseObjectEnum` [R/W] Indicates whether the discounts specified by the DiscountGroups property are based on item groups, properties, or manufacturers. If you change the value, all rows of the DiscountGroups subobject whose BaseObjectType is not equal to the new value are deleted. Field name: DscntObjct
- `Public Property DiscountGroups() As DiscountGroups` [R] Returns a list of special item discounts based on each item's group, properties, or manufacturer. Each business partner has its own set of discounts. For more information, see DiscountGroups.
- `Public Property DiscountPercent() As Double` [R/W] Sets or returns the discount percentage you specify for a customer, or the discount percentage a supplier specifies for you. Field name: Discount.
  - remarks: SAP Business One automatically completes the value for this property from PaymentTermsTypes object (OCTG table) according to the selected payment terms (PayTermsGrpCode property). For business partners defined as type 'Other' (neither a customer nor a supplier) you do not have to set this property. (For 5% discount set the value 5, not 0.05.)
- `Public Property DiscountRelations() As DiscountGroupRelationsEnum` [R/W] Indicates how to calculate item discounts if more than one of the discounts specified by the DiscountGroups property applies to an item. This property is relevant only when the DiscountBaseObject is set to item properties. Field name: DscntRel
- `Public Property DME() As String` [R/W] Sets or returns the DME identification/instruction key, which is relevant for the creation of the OPEX file by the Payment Engine add-on. Field name: DME.
  - remarks: Relevant for European countries, vendors only.
- `Public Property DownPaymentClearAct() As String` [R/W] Sets or returns the G/L account for down payment clearing. Field name: DpmClear. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property DownPaymentInterimAccount() As String` [R/W] The G/L account for A/P down payments. When creating a vendor business partner, the DownPaymentInterimAccount property is automatically set to this account.
- `Public Property DunningDate() As Date` [R] Returns the date for sending dunning letters. Field name: DunnDate.
- `Public Property DunningLevel() As Long` [R] Returns the dunning level. Field name: DunnLevel. This is a foreign key to the DunningLetters object.
  - remarks: Dunning is the process of methodically communicating with customers to insure the collection of accounts receivable. It follows the process that progresses from gentle reminders (low level) to almost threatening letters (high level) as accounts become more past due.
- `Public Property DunningTerm() As String` [R/W] Sets or returns the Term Code as defined in Dunning Terms window in SAP Business One application (ODUT table, which is not exposed through the DI API). Field name: DunTerm. Length: 25 characters. This is a foreign key to the Dunning Terms table (ODUT - not exposed through the DI API).
- `Public Property EBooksVATExemptionCause() As Long` [R/W] property EBooksVATExemptionCause
- `Public Property ECommerceMerchantID() As String` [R/W] property ECommerceMerchantID
- `Public Property EDIRecipientID() As String` [R/W] property EDIRecipientID
- `Public Property EDISenderID() As String` [R/W] property EDISenderID
- `Public Property EDocBuildingNumber() As Long` [R/W] property EDocBuildingNumber
- `Public Property EDocCity() As String` [R/W] property EDocCity
- `Public Property EDocCountry() As String` [R/W] property EDocCountry
- `Public Property EDocDistrict() As String` [R/W] property EDocDistrict
- `Public Property EDocGenerationType() As EDocGenerationTypeEnum` [R/W] property EDocGenerationType
- `Public Property EDocPECAddress() As String` [R/W] property EDocPECAddress
- `Public Property EDocRepresentativeAdditionalId() As String` [R/W] property EDocRepresentativeAdditionalId
- `Public Property EDocRepresentativeCompany() As String` [R/W] property EDocRepresentativeCompany
- `Public Property EDocRepresentativeFirstName() As String` [R/W] property EDocRepresentativeFirstName
- `Public Property EDocRepresentativeFiscalCode() As String` [R/W] property EDocRepresentativeFiscalCode
- `Public Property EDocRepresentativeSurname() As String` [R/W] property EDocRepresentativeSurname
- `Public Property EDocStreet() As String` [R/W] property EDocStreet
- `Public Property EDocStreetNumber() As String` [R/W] property EDocStreetNumber
- `Public Property EDocZipCode() As String` [R/W] property EDocZipCode
- `Public Property EffectiveDiscount() As DiscountGroupRelationsEnum` [R/W] property EffectiveDiscount
- `Public Property EffectivePrice() As EffectivePriceEnum` [R/W] property EffectivePrice
- `Public Property EffectivePriceConsidersPriceBeforeDiscount() As BoYesNoEnum` [R/W] property EffectivePriceConsidersPriceBeforeDiscount
- `Public Property ElectronicProtocols() As ElectronicProtocols` [R] property ElectronicProtocols
- `Public Property EmailAddress() As String` [R/W] Sets or returns the e-mail address of the business partner. Field name: E_Mail. Length: 100 characters.
- `Public Property EndorsableChecksFromBP() As BoYesNoEnum` [R/W] property EndorsableChecksFromBP
- `Public Property EORINumber() As String` [R/W] EORI number. Field name: EORINumber. Length: 17 characters.
- `Public Property Equalization() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the business partner (customer type only) is liable to additional equalization tax. Field name: Equ.
  - remarks: Country-specific property for Spain, Italy, Portugal, and France.
- `Public Property ETaxWebSite() As Long` [R/W] property ETaxWebSite
- `Public Property ExchangeRateForIncomingPayment() As BoYesNoEnum` [R/W] property ExchangeRateForIncomingPayment
- `Public Property ExchangeRateForOutgoingPayment() As BoYesNoEnum` [R/W] property ExchangeRateForOutgoingPayment
- `Public Property ExemptionMaxAmountValidationType() As ExemptionMaxAmountValidationTypeEnum` [R/W] property ExemptionMaxAmountValidationType
- `Public Property ExemptionValidityDateFrom() As Date` [R/W] Returns the start date when the business partner is exempted from paying tax. Field name: FromDate.
- `Public Property ExemptionValidityDateTo() As Date` [R/W] Returns the ending date when the business partner is exempted from paying tax. Field name: ToDate.
- `Public Property ExemptNum() As String` [R/W] Sets or returns the number of the tax exemption. Field name: ExemptNo. Length: 50 characters.
- `Public Property ExpirationDate() As Date` [R/W] Sets or returns the expiration date of the withholding tax certificate. Field name: ExpireDate.
- `Public Property ExportCode() As String` [R/W] Sets or returns the code used for data export. Field name: ExportCode. Length: 8 characters.
- `Public Property FatherCard() As String` [R/W] Sets or returns the card code of the parent business partner (for example, card code of the head office related to the current business partner). Field name: FatherCard. Length: 15 characters.
  - remarks: In SAP Business One, you can organize business partners in hierarchical structure. Use this property to specify the parent business partner. Organizing business partners hierarchically is useful when you create separate business partner cards for branches of the same business partner. This allows you to consolidate all business activities for the head office. You can either send delivery notes together in one invoice to the head office or balance the invoices sent to the various branches by means of a payment from the head office.
- `Public Property FatherType() As BoFatherCardTypes` [R/W] Sets or returns a valid value of BoFatherCardTypes that specifies the method of handling deliveries and payments used by the parent business partner. Field name: FatherType.
  - remarks: Set to cDelivery_sum to send delivery notes in one invoice to the head office. Set to cPayments_sum to balance invoices sent to branches using payments from the head office.
- `Public Property Fax() As String` [R/W] Sets or returns the fax number of the business partner. Field name: Fax. Length: 50 characters.
- `Public Property FCEAsPaymentMeans() As BoYesNoEnum` [R/W] Use FCEs as Payment Means. Field name: FCEPmnMean.
- `Public Property FCERelevant() As BoYesNoEnum` [R/W] FCE relevant. Field name: FCERelevnt.
- `Public Property FCEValidateBaseDelivery() As BoYesNoEnum` [R/W] FCE validate base delivery. Field name: FCEVldte.
- `Public Property FederalTaxID() As String` [R/W] Sets or returns the federal tax ID number that is saved in documents and will be used for calculating the EU sales report. Field name: LicTradNum). Length: 32 characters.
- `Public Property FeeAccount() As String` [R/W] property FeeAccount
- `Public Property FiscalTaxID() As BPFiscalTaxID` [R] Returns the BPFiscalTaxID Object.
  - remarks: - This Object is specific to Cluster 2B (Country specific property for Brazil only).
- `Public Property FormCode1099() As Long` [R/W] Sets or returns the code of the Form 1099. Field name: FormCode. This is a foreign key to the Forms1099 object.
- `Public Property FreeText() As String` [R/W] Sets or returns a memo type string that specifies detailed information about the business partner (unlike the Notes property that contains a short notes of up to 100 characters). Field name: Free_Text. Length: 64,000 characters.
- `Public Property Frozen() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the business partner record is locked for a specified period (on-hold period). Field name: frozenFor.
- `Public Property FrozenFrom() As Date` [R/W] Sets or returns the beginning date of the period the business partner card is locked (on-hold). Field name: frozenFrom.
- `Public Property FrozenRemarks() As String` [R/W] Sets or returns remarks about locking the business partner card. Field name: FrozenComm. Length: 30 characters.
- `Public Property FrozenTo() As Date` [R/W] Sets or returns the ending date of the period the business partner card is locked (on-hold). Field name: frozenTo.
- `Public Property GlobalLocationNumber() As String` [R/W] property GlobalLocationNumber
- `Public Property GroupCode() As Long` [R/W] Sets or returns the group code for the business partner. Field name: GroupCode. This is a foreign key to the OCRG object.
  - remarks: In SAP Business One, you can classify business partners according to groups such as industry, region, importance, and so on. You can then create reports and evaluate business partners based on a specific group. The report can be generated from a specific cross-section of cards.
- `Public Property GTSBankAccountNo() As String` [R/W] property GTSBankAccountNo
- `Public Property GTSBillingAddrTel() As String` [R/W] property GTSBillingAddrTel
- `Public Property GTSRegNo() As String` [R/W] property GTSRegNo
- `Public Property HierarchicalDeduction() As BoYesNoEnum` [R/W] property HierarchicalDeduction
- `Public Property HouseBank() As String` [R/W] Sets or returns the name of the house bank. Field name: HouseBank. Length: 30 characters.
  - remarks: House Bank means the bank that your company uses for payments. That is, paying to the business partner or receiving payments from the business partner.
- `Public Property HouseBankAccount() As String` [R/W] Sets or returns the account number of the house bank. Field name: HousBnkAct. Length: 50 characters.
  - remarks: House Bank means the bank that your company uses for payments. That is, paying to the business partner or receiving payments from the business partner.
- `Public Property HouseBankBranch() As String` [R/W] Sets or returns the branch name of the house bank. Field name: HousBnkBrn. Length: 50 characters.
  - remarks: House Bank means the bank that your company uses for payments. That is, paying to the business partner or receiving payments from the business partner.
- `Public Property HouseBankCountry() As String` [R/W] Sets or returns the country code of the house bank. Field name: HousBnkCry. Length: 3 characters.
  - remarks: House Bank means the bank that your company uses for payments. That is, paying to the business partner or receiving payments from the business partner.
- `Public Property HouseBankIBAN() As String` [R] The International Bank Account Number (IBAN) for the house back. Field name: HsBnkIban. Length: 50 characters.
- `Public Property IBAN() As String` [R/W] Sets or returns the International Bank Account Number (IBAN) for the business partner. Field name: IBAN. Length: 50 characters.
  - remarks: Europe only.
- `Public Property Indicator() As String` [R/W] Sets or returns the Factoring Indicator for the business partner master record. Field name: Indicator. Length: 2 characters. This is a foreign key to the FactoringIndicators object.
  - remarks: This indicator is automatically inserted as default value in outgoing invoices and may be displayed in the account statements. Can be used later for sorting invoices related to this business partner. You can set only an indicator that is already defined in SAP Business One.
- `Public Property Industry() As Long` [R/W] Industries related to the business partner. Field name: IndustryC. Length: 11 characters.
  - remarks: Not applicable for Korea localization.
- `Public Property IndustryType() As String` [R/W] property IndustryType
- `Public Property InstructionKey() As String` [R/W] Sets or returns an instruction key that is used as an additional indicator of the business partner. This key is used in the payment run process. Field name: InstrucKey. Length: 30 characters.
- `Public Property InsuranceOperation347() As BoYesNoEnum` [R/W] Indicates if this business partner is reported with the insurance operation type in 347 reports. Field name: InsurOp347
  - remarks: For Spain only.
- `Public Property InterestAccount() As String` [R/W] property InterestAccount
- `Public Property IntrastatExtension() As BPIntrastatExtension` [R] property IntrastatExtension
- `Public Property IntrestRatePercent() As Double` [R/W] Sets or returns the interest percentage rate for delayed payments. In SAP Business One, called Interest on Arrears %. Field name: IntrstRate.
  - remarks: For 5% interest rate set the value 5, not 0.05.
- `Public Property IPACodeForPA() As String` [R/W] property IPACodeForPA
- `Public Property ISRBillerID() As String` [R/W] Sets or returns the ID of the ISR biller. Field name: ISRBillId. Length: 9 characters.
  - remarks: Country-specific property for Switzerland. Available only for vendors. This property enables the business partner to support the invoice ISR slip. The ID structure is XX-XXXXXX-X and if you set less than 9 digits, the system adds '0'.
- `Public Property LanguageCode() As Long` [R/W] Sets or returns the Language Code used by the business partner. Field name: LangCode. This is the foreign key of the UserLanguages object.
- `Public Property LastMultiReconciliationNum() As Long` [R/W] Not used.
- `Public Property LegalText() As String` [R/W] Legal text. Field name: LegalText. Length: 254 characters.
- `Public Property LinkedBusinessPartner() As String` [R/W] Sets or returns the business partner code that is connected to the current business partner. Field name: ConnBP. Length: 15 characters.
- `Public Property MailAddress() As String` [R/W] Sets or returns the street of the Ship To address. Field name: MailBlock. Length: 100 characters.
  - remarks: The MailAddress property does not include city, country, and zip code information. This information is maintained in other properties.
- `Public Property MailCity() As String` [R/W] Sets or returns the city of the Ship To address. Field name: MailCity. Length: 100 characters.
- `Public Property MailCountry() As String` [R/W] Sets or returns the country of the Ship To address. Field name: MailCounty. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property MailCounty() As String` [R/W] Sets or returns the county of the Ship To address. Field name: MailCounty. Length: 100 characters.
- `Public Property MailZipCode() As String` [R/W] Sets or returns the zip code of the Ship To address. Field name: MailZipCod. Length: 20 characters.
- `Public Property MainUsage() As Long` [R/W] Sets or returns the main usage in the Brazil (BR) localization.. Field name: MainUsage.
- `Public Property MaxAmountOfExemption() As Double` [R/W] Sets or returns the maximum amount of exemption defined in the exemption letter. Field name: MaxAmount.
- `Public Property MaxCommitment() As Double` [R/W] Sets or returns the maximum allowed debt for payments from the business partner. Field name: DebtLine.
  - remarks: SAP Business One automatically completes the value for this property from PaymentTermsTypes object (OCTG table) according to the selected payment terms (PayTermsGrpCode property).
- `Public Property MinIntrest() As Double` [R/W] Sets or returns the minimum interest rate for delayed payments. Field name: MinIntrst.
- `Public Property NationalInsuranceNum() As String` [R/W] Sets or returns the national insurance number of the business partner. Field name: NINum. Length: 20 characters.
- `Public Property NoDiscounts() As BoYesNoEnum` [R/W] property NoDiscounts
- `Public Property Notes() As String` [R/W] Sets or returns the short notes about the business partner. For example, "Customer entitled to preferred treatment" or "No checks". Field name: Notes. Length: 100 characters.
- `Public Property OpenChecksBalance() As Double` [R] property OpenChecksBalance
- `Public Property OpenDeliveryNotesBalance() As Double` [R] Returns the open balance of delivery notes. Field name: DNotesBal.
  - remarks: This property changes when you perform Goods Returns or Invoice transactions.
- `Public Property OpenOpportunities() As Long` [R] Returns the sum of open sales opportunities for a specified customer. Field name: OprCount.
- `Public Property OpenOrdersBalance() As Double` [R] Returns the open balance for open orders. Field name: OrderBalFC.
- `Public Property OperationCode347() As OperationCode347Enum` [R/W] Operation code for use in 347 reports. Field name: OpCode347
  - remarks: For Spain only.
- `Public Property OtherReceivablePayable() As String` [R/W] Returns the additional receivable/payable account of the business partner. Field name: OtrCtlAcct. Length: 15 characters.
- `Public Property OwnerCode() As Long` [R/W] property OwnerCode
- `Public Property OwnerIDNumber() As String` [R/W] Sets or returns the ID number of the credit card owner for payments. Field name: OwnerIdNum. Length: 15 characters.
- `Public Property Pager() As String` [R/W] Sets or returns the pager number of the contact person. Field name: Pager. Length: 30 characters.
- `Public Property PartialDelivery() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies, in the payment terms, whether or not to enable partial delivery. Field name: PartDelivr.
  - remarks: A partial delivery may be necessary if the entire quantity of goods ordered by the customer is not available on the requested delivery date. Another reason may be that no complete deliveries can be created during delivery processing because of, say, organizational or transportation capacity limitations.
- `Public Property Password() As String` [R/W] Sets or returns the password to use with when connecting to B2B and B2C e-commerce applications. Field name: Password. Length: 32 characters.
- `Public Property PaymentBlock() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to block a payment due to a reason specified in PaymentBlockDescription property. Field name: PaymBlock.
- `Public Property PaymentBlockDescription() As Long` [R/W] Sets or returns a description of the payment block reason as defined in SAP Business One in 'Define Payment Block' table. Field name: PyBlckDesc.
  - remarks: To set the PaymentBlockDescription property, first set the PaymentBlock property to tYES.
- `Public Property PayTermsGrpCode() As Long` [R/W] Sets or returns the payment terms group number. Field name: GroupNum. This is a foreign key to the PaymentTermsTypes object.
  - remarks: SAP Business One uses this number to auto-complete the related payment terms properties from the OCTG table.
- `Public Property PeymentMethodCode() As String` [R/W] Sets or returns the code identifying the method for the movement of payment instructions (such as, check or bank transfer). Field name: PymCode. Length: 15 characters.
- `Public Property Phone1() As String` [R/W] Sets or returns the main phone number of the business partner. Field name: Phone1. Length: 50 characters.
- `Public Property Phone2() As String` [R/W] Sets or returns the secondary phone number of the business partner. Field name: Phone2. Length: 50 characters.
- `Public Property Picture() As String` [R/W] Sets or returns a picture file name. Field name: Picture. Length: 200 characters.
  - remarks: Include only the file name without the full path. To read or change the path, set the BitMapPath property.
- `Public Property PlanningGroup() As String` [R/W] The planning group related to the business partner that reflects certain characteristics, risks, or the type of business relationship. Field name: PlngGroup. Length: 10 characters.
  - remarks: The property is for SAP Business One integration for SAP NetWeaver - Subsidiary Integration.
- `Public Property PriceListNum() As Long` [R/W] Sets or returns the Price List index. Field name: ListNum. This is a foreign key to the PriceLists object.
  - remarks: The price list describes item prices in the warehouse. SAP Business One contains different Price Lists, using this property, you can reference any of them. SAP Business One automatically completes the value for this property from PaymentTermsTypes object (OCTG table) according to the selected payment terms (PayTermsGrpCode property).
- `Public Property PriceMode() As PriceModeEnum` [R/W] property PriceMode
- `Public Property Priority() As Long` [R/W] Sets or returns a foreign key to the priority of the business partner payments. The priorities are defined in the BPPriorities object. Field name: Priority. This is a foreign key to the BPPriorities object.
- `Public Property Profession() As String` [R/W] Sets or returns the business partner profession. Field name: Profession. Length: 50 characters.
  - remarks: The object is applicable for SAP Business One 2004C CEE (country-specific for Russia). See OCRD table of Database Tables Reference 2004C.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code related to the business partner. Field name: ProjectCod. Length: 8 characters. This is a foreign key to the Project table (OPRJ - not exposed through the DI API).
  - remarks: In SAP Business One, you can relate business transactions to projects. This can help you to create cost/income analyzes reports based on projects.
- `Public Property Properties(ByVal GroupNum As Long) As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the business partner belongs to one or more query groups. Field name: EMChrctrstcs.
  - remarks: This property represents the Properties of a Business Partner. In SAP Business One, you can enter up to 64 Properties per business partner and use them for cross-sections in reports. You can define different groups to describe the different characteristic of your business partners. One business partner can belong to one or more groups at the same time.
- `Public Property RateDiffAccount() As String` [R/W] Sets or returns the account number used for exchange rate differences. Field name: RateDifAct. Length: 15 characters.
  - remarks: In SAP Business One, you can use any currency to perform business transactions. Since the exchange rate changes every day, this account is used when there are monetary differences deriving from foreign currency exchange rates in sales documents and incoming payments.
- `Public Property ReferenceDetails() As String` [R/W] Sets or returns additional information to the house bank details of the business partner. Field name: RefDetails. Length: 20 characters.
- `Public Property RelationshipCode() As String` [R/W] property RelationshipCode
- `Public Property RelationshipDateFrom() As Date` [R/W] property RelationshipDateFrom
- `Public Property RelationshipDateTill() As Date` [R/W] property RelationshipDateTill
- `Public Property RepresentativeName() As String` [R/W] property RepresentativeName
- `Public Property ResidenNumber() As ResidenceNumberTypeEnum` [R/W] property ResidenNumber
- `Public Property SalesPersonCode() As Long` [R/W] Sets or returns the code (key) of the sales employee who contacts with the business partner (customer type only). Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property Series() As Long` [R/W] property Series
- `Public Property ShaamGroup() As ShaamGroupEnum` [R/W] property ShaamGroup
- `Public Property ShippingType() As Long` [R/W] Sets or returns the code of the shipping type (such as, Courier or Air Cargo). Field name: ShipType. This is a foreign key to the ShippingTypes object.
  - remarks: The shipping type defines how the goods will be transported to the customer, and how the expenses will be calculated.
- `Public Property ShipToBuildingFloorRoom() As String` [R/W] Sets or returns a memo type string that specifies additional details of the Ship To address, such as building number, floor number, and room number. Field name: MailBuildi. Length: 64,000 characters.
- `Public Property ShipToDefault() As String` [R/W] Sets or returns the default Ship To address name. Field name: ShipToDef. Length: 50 characters.
- `Public Property SinglePayment() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether the business partner must pay invoices in single payment or few partial payments. Field name: SinglePaym.
  - remarks: Relevant to customers only.
- `Public Property SubjectToWithholdingTax() As BoYesNoNoneEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the transactions with the business partner are subject to Withholding tax. Field name: WTLiable.
  - remarks: Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, India, and Portugal. For India localizations, if this property is set to yes, then the TaxId0 property of the BPFiscalTaxID object is mandatory and must be set to a 10-character value.
- `Public Property SurchargeOverlook() As BoYesNoEnum` [R/W] Indicates whether the surcharge threshold specified in the withholding tax code is ignored. Field name: SurOver
  - remarks: For India only.
- `Public Property TaxExemptionLetterNum() As String` [R/W] Returns the number of the tax exemption letter. Used in invoice documents. Field name: LetterNum. Length: 20 characters.
- `Public Property TaxRoundingRule() As BoTaxRoundingRuleTypes` [R/W] Sets or returns a valid value that specifies the rounding rule type for tax amounts. The options include: Company Default, Rounding Off, Rounding Up, and Rounding Down. This property is applicable for cluster B only (country-specific for Japan and Korea).
  - remarks: The default value for a new business partner is Company Default, which means the rounding rule for this business partner is the one defined in Company Details.
- `Public Property Territory() As Long` [R/W] Sets or returns the business partner territory as defined in SAP Business One. Relevant to business partners of customer type only. Field name: Territory. This is a foreign key to the Territories object.
- `Public Property ThresholdOverlook() As BoYesNoEnum` [R/W] Indicates whether the TDS threshold specified in the withholding tax code is ignored. Field name: ThreshOver
  - remarks: For India only.
- `Public Property TypeOfOperation() As TypeOfOperationEnum` [R/W] property TypeOfOperation
- `Public Property TypeReport() As AssesseeTypeEnum` [R/W] Specifies the type of nature of assessee (for TDS withholding tax reports). Field name: TypWTReprt
  - remarks: For India only.
- `Public Property UnifiedFederalTaxID() As String` [R/W] property UnifiedFederalTaxID
- `Public Property UnpaidBillofExchange() As String` [R/W] Sets or returns G/L account number for the Unpaid Bill of Exchange payments. Field name: UnpaidBoE. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property UpdateDate() As Date` [R] The date when the business partner master data updated. Field name: UpdateDate.
- `Public Property UpdateTime() As Date` [R] The timestamp of the business partner master data updated is recorded in the hhmmss format. Field name: UpdateTS.
- `Public Property UseBillToAddrToDetermineTax() As BoYesNoEnum` [R/W] property UseBillToAddrToDetermineTax
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UseShippedGoodsAccount() As BoYesNoEnum` [R/W] property UseShippedGoodsAccount
- `Public Property Valid() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the business partner record is active. Field name: validFor.
  - remarks: If you set this property to tYES also define the activity period and remarks.
- `Public Property ValidFrom() As Date` [R/W] Sets or returns the start date of the business partner activity period. Field name: validFor.
- `Public Property ValidRemarks() As String` [R/W] Sets or returns the remarks for the business partner activity period. Field name: ValidComm. Length: 30 characters.
- `Public Property ValidTo() As Date` [R/W] Sets or returns the end date of the business partner activity period. Field name: ValidTo.
- `Public Property VatGroup() As String` [R/W] Sets or returns the VAT group for the business partner. Field name: VatGroup. Length: 8 characters. This is a foreign key to the SalesTaxCodes object.
  - remarks: Use this property to assign Business Partners to VAT groups. The VAT group defines VAT amounts for transactions with this Business Partner.
- `Public Property VatGroupLatinAmerica() As String` [R/W] Sets or returns the VAT group for the business partner. Length: 8 characters.
  - remarks: Country-specific for Latin America. Use this property to assign Business Partners to VAT groups. The VAT group defines VAT amounts for transactions with this Business Partner.
- `Public Property VatIDNum() As String` [R/W] property VatIDNum
- `Public Property VatLiable() As BoVatStatus` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the transactions with the business partner are subject to VAT. Field name: VatStatus.
  - remarks: Set this property to vLiable to enable VAT in transactions with this business partner.
- `Public Property VATRegistrationNumber() As String` [R/W] property VATRegistrationNumber
- `Public Property VerificationNumber() As String` [R/W] Sets or returns the verification number of the withholding tax. Country-specific for UK. Field name: VerifNum). Length: 32 characters.
- `Public Property Website() As String` [R/W] Sets or returns the Internet address of the business partner. Field name: IntrntSite. Length: 100 characters.
- `Public Property WithholdingTaxCertified() As BoYesNoEnum` [R/W] property WithholdingTaxCertified
- `Public Property WithholdingTaxDeductionGroup() As Long` [R/W] The type of vendor for withholding tax purposes. Field name: DdgKey This is a foreign key to the DeductionTaxGroups object.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code assigned to the business partner. Field name: WTCode. Length: 4 characters. This is a foreign key to the WithholdingTaxCodes object.
  - remarks: This is a foreign key to WithholdingTaxCodes object. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, India, and Portugal. For India localizations, if this property is set to yes, then the TaxId0 property of the BPFiscalTaxID object is mandatory and must be set to a 10-character value.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code of the Bill To address, which is the address of the physical location of the business partner. Field name: ZipCode. Length: 20 characters.
  - remarks: Use this property only if the physical address is different from the Ship To address (mailing address). If you do not set this property, when adding a new business partner card, SAP Business One will copy the data from the MailZipCode property.

## Methods (10)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Not supported.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal CardCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `CardCode`: Specifies the identification key of the business object (CardCode).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
- `Public Function UpdateFromXML(ByVal FileName As String) As Long` Receives and processes the XML content. You can remove sub-object lines from the BusinessPartners object via the XML file.
  - param `FileName`: Specifies the path and file name of the XML data.
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    'Set import export model first
    vComp.XmlExportType = BoXmlExportTypes.xet_ExportImportMode

    'Delete line from the BusinessPartners object
    Dim obp As BusinessPartners = vComp.GetBusinessObject(BoObjectTypes.oBusinessPartners)

    'Get object
    obp.GetByKey("C001")
    obp.SaveToFile("C:\testbp.xml")

    'Delete sub line directly from C:\testbp.xml

    'Update object
    obp.UpdateFromXML("C:\testbp.xml")
    ```
