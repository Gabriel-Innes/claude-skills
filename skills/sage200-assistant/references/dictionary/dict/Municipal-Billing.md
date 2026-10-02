# Sage 200 Evolution table dictionary - Municipal Billing

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _mtblAreas
PK: idAreas
Columns (5):
  idAreas int NOT NULL identity PK
  cArea varchar(50) NULL
  cAreaDescription varchar(100) NULL
  cAreaDetails varchar(2000) NULL
  iAreaTypeID int NULL

## _mtblAreaTypes
PK: idAreaTypes
Columns (3):
  idAreaTypes int NOT NULL identity PK
  cAreaType varchar(50) NULL
  cAreaTypeDescription varchar(100) NULL

## _mtblBillingCycles
PK: idBillingCycle
Columns (3):
  idBillingCycle int NOT NULL identity PK
  cBillingCycleName varchar(50) NULL
  dBillingDate int NULL

## _mtblBillingRunDetails
PK: idBillingRunDetails
Columns (9):
  idBillingRunDetails bigint NOT NULL identity PK
  iBillingRunID int NULL
  iPropertyPortionServiceID int NULL
  iRateTariffBandID int NOT NULL
  fExclusive float NULL
  fTaxAmount float NULL
  fInclusive float NULL
  cDescription varchar(50) NULL
  fUnits float NULL

## _mtblBillingRuns
PK: idBillingRun
Columns (20):
  idBillingRun int NOT NULL identity PK
  iBillingRunPeriodID int NULL
  cFromAccount varchar(20) NULL
  cToAccount varchar(20) NULL
  cServices varchar(1024) NULL
  bBillingRunProcessed bit NOT NULL default (0)
  cUserNameCalculated varchar(50) NULL
  iSysDateCalculated datetime NULL
  cUserNameProcessed varchar(50) NULL
  iSysDateProcessed datetime NULL
  cRegions varchar(1024) NULL
  cSubRegions varchar(1024) NULL
  cAreas varchar(1024) NULL
  bBillMonthlyRates bit NOT NULL default (0)
  bBillQuarterlyRates bit NOT NULL default (0)
  bBillAnnuallyRates bit NOT NULL default (0)
  cWalks varchar(1024) NULL
  bBill10MonthlyRates bit NOT NULL default (0)
  cBillingRunNumber nvarchar(50) NULL
  dBillingCycleDate datetime NULL

## _mtblCategories
PK: idCategory
Columns (6):
  idCategory int NOT NULL identity PK
  cCategory varchar(50) NULL
  cCategoryDescription varchar(100) NULL
  bIsUsageCategory bit NULL
  bIsZonalCategory bit NULL
  bIsRatingCategory bit NULL

## _mtblClearanceCertificateBuyers
PK: idClearanceCertificateBuyers
Columns (12):
  idClearanceCertificateBuyers bigint NOT NULL identity PK
  iBuyerClearanceCertificateID int NULL
  cBuyerName varchar(50) NULL
  bBuyerIsCompany bit NULL
  cBuyerIDNumber varchar(50) NULL
  cBuyerPassportNumber varchar(50) NULL
  cBuyerAddress1 varchar(50) NULL
  cBuyerAddress2 varchar(50) NULL
  cBuyerAddress3 varchar(50) NULL
  cBuyerAddressPC varchar(15) NULL
  cBuyerTelephone1 varchar(25) NULL
  fBuyerPercentage float NULL

## _mtblClearanceCertificateDetails
PK: idClearanceCertificateDetails
Columns (6):
  idClearanceCertificateDetails int NOT NULL identity PK
  iClearanceCertificateID int NULL
  iServiceID int NULL
  fAverageBillingAmountPerMonth float NULL
  fTotalBillingAmountAllMonths float NULL
  iCustomerID int NULL default (0)

## _mtblClearanceCertificates
PK: idClearanceCertificates
Columns (43):
  idClearanceCertificates int NOT NULL identity PK
  cClearanceCertificateCode varchar(50) NULL
  iClearanceStatus int NOT NULL
  iPropertyID int NOT NULL
  iCurrentOwnerID int NOT NULL
  iCalculationMonths int NULL
  fClearanceCertificateCost float NULL
  fValuationCertificateCost float NULL
  fCostScheduleCost float NULL
  fSellingPrice float NULL
  iClearanceFromPeriodID int NULL
  iClearanceToPeriodID int NULL
  dApplicationDate datetime NULL
  dSaleDate datetime NULL
  cReferenceNumber varchar(100) NULL
  bIncludeValuationCertificate bit NULL
  bIncludeClearanceCertificate bit NULL
  fCurrentDCBalance float NULL
  iTillID int NULL
  fPayment float NULL
  cApplicantName varchar(50) NULL
  cApplicantAddress1 varchar(50) NULL
  cApplicantAddress2 varchar(50) NULL
  cApplicantAddress3 varchar(50) NULL
  cApplicantAddressPC varchar(15) NULL
  cApplicantTelephone1 varchar(25) NULL
  iCurrentTenantID int NULL
  fCurrentTenantBalance float NULL
  cPortionIDs varchar(max) NULL
  cPortions varchar(max) NULL default ''
  cClearanceCost1Desc varchar(30) NULL default 'Other Cost 1'
  cClearanceCost2Desc varchar(30) NULL default 'Other Cost 2'
  cClearanceCost3Desc varchar(30) NULL default 'Other Cost 3'
  cClearanceCost4Desc varchar(30) NULL default 'Other Cost 4'
  fClearanceCost1 float NULL default (0)
  fClearanceCost2 float NULL default (0)
  fClearanceCost3 float NULL default (0)
  fClearanceCost4 float NULL default (0)
  dClearanceTxDate datetime NULL
  cUserNameCreated varchar(50) NULL
  dDateCreated datetime NULL
  cUserNameLastActioned varchar(50) NULL
  dDateLastAction datetime NULL

## _mtblClientRules
PK: iClientID+iRebateRuleID
Columns (2):
  iClientID int NOT NULL PK
  iRebateRuleID int NOT NULL PK

## _mtblCustomerMeterReadings
PK: idCustomerMeterReading
Columns (7):
  idCustomerMeterReading int NOT NULL identity PK
  iPeriodID int NOT NULL
  iMeterID int NOT NULL
  fCurrentReading float NOT NULL
  iFinalizationID int NULL
  iMeterReaderID int NULL
  dtReadingDate datetime NOT NULL default '1900/01/01'

## _mtblDefaults
PK: idDefaults
Columns (60):
  idDefaults int NOT NULL identity PK
  bAllowConsolidatedPayments bit NOT NULL default (1)
  iConsolidatedPaymentTrCodeID int NULL
  cReceiptPrefix varchar(10) NULL
  iReceiptNextNumber int NULL
  iReceiptPadNumber int NULL
  iAverageFailureReasonID int NULL
  bDepositsMeteredOnly bit NOT NULL default (1)
  PropertyFilterStartLength int NULL
  PortionFilterStartLength int NULL
  MeterFilterStartLength int NULL
  cFinalizationPrefix varchar(10) NULL
  iFinalizationNextNumber int NULL
  iFinalizationPadNumber int NULL
  iGPSFormat int NOT NULL default (0)
  cClearanceCertificatePrefix varchar(10) NULL
  iClearanceCertificateNextNumber int NULL
  iClearanceCertificatePadNumber int NULL
  bForceFinalizationTitleDeed bit NULL default (1)
  bConsolidateBillRunGLTrans bit NULL default (0)
  iPaymentPriorityType int NULL
  bUseBillingRunDate bit NULL
  iCostScheduleTrCodeID int NULL
  iClearanceCertificateTrCodeID int NULL
  iValuationCertificateTrCodeID int NULL
  bForceClearanceTitleDeed bit NULL default (1)
  iValuationDisplayType int NULL
  iDirectDepositTrCodeID int NULL
  iClearanceCertificateBackDateType int NULL default (0)
  iClearanceCertificateBackDateTimeInMonths int NULL
  iClearanceCertificateForwardDateType int NULL default (1)
  iDepositsNoPropertyTrCodeID int NULL default (0)
  cBillingRunPrefix nvarchar(10) NULL default N'BR'
  iBillingRunNextNumber int NULL default (1)
  iBillingRunPadNumber int NULL default (4)
  bAutomaticBillingRunNumbering bit NULL default (1)
  bUniqueBillingRunNumber bit NULL default (0)
  bProRateCalc bit NULL
  iProRateCutOffDays int NULL
  bProRateUseDaysInMonth bit NULL default (0)
  bUseBillingCycleDates bit NULL default (0)
  bRecalcSuccessivePeriods bit NULL default (0)
  bClearanceReceiptSelection bit NULL default (0)
  cAllowedTrCodes varchar(1024) NULL default ''
  bClearanceUseCost1 bit NOT NULL default (0)
  bClearanceUseCost2 bit NOT NULL default (0)
  bClearanceUseCost3 bit NOT NULL default (0)
  bClearanceUseCost4 bit NOT NULL default (0)
  cClearanceCost1Desc varchar(30) NOT NULL default 'Other Cost 1'
  cClearanceCost2Desc varchar(30) NOT NULL default 'Other Cost 2'
  cClearanceCost3Desc varchar(30) NOT NULL default 'Other Cost 3'
  cClearanceCost4Desc varchar(30) NOT NULL default 'Other Cost 4'
  bClearancePostOtherCosts bit NOT NULL default (1)
  bAllowMultipleClearances bit NOT NULL default (0)
  iFailureReasonOnActualReadings int NOT NULL default (0)
  bRecalcHistoricReadings bit NOT NULL default (0)
  bNonCumulativePreviousReading bit NOT NULL default (0)
  bRemoveDisconnectedFromWalk bit NOT NULL default (0)
  bRecalcPreviousPeriods bit NOT NULL default (0)
  iDisconnectedMeterFailureReason int NOT NULL default (0)

## _mtblDeposits
PK: idDeposit
Columns (10):
  idDeposit bigint NOT NULL identity PK
  cDescription varchar(50) NULL
  iPropertyPortionServicesID bigint NOT NULL
  iServiceID bigint NOT NULL
  iCustomerID bigint NOT NULL
  fDepositAmount float NULL
  iDepositFlag int NULL
  dTimeStamp datetime NOT NULL
  cUserName varchar(50) NULL
  dTxDate datetime NOT NULL default '1900/01/01'

## _mtblFailureReasons
PK: idFailureReason
Columns (2):
  idFailureReason int NOT NULL identity PK
  cFailureReason varchar(150) NULL

## _mtblFinalizationDetails
PK: idFinalizationDetail
Columns (52):
  idFinalizationDetail int NOT NULL identity PK
  iFinalizationID int NOT NULL
  iMeterID int NULL
  fPreviousReading float NOT NULL
  fFinalMeterReading float NOT NULL
  fFinalConsumption float NULL
  iMeterReaderID int NULL
  dFinalReadingFromDate datetime NULL
  dFinalReadingToDate datetime NULL
  iBillingPeriodID int NOT NULL
  cReadingDescription varchar(100) NOT NULL
  dCapturedDate datetime NOT NULL
  cDocument varchar(50) NULL
  iPropertyPortionServiceID int NOT NULL
  dTimeStamp datetime NOT NULL
  bProcessed bit NOT NULL
  iCalculationType int NOT NULL
  bApplyPortionSize bit NOT NULL
  iLinkedServiceID int NOT NULL
  iServiceConsumerID int NOT NULL
  iServiceRateTariffID int NOT NULL
  iPortionServiceID int NOT NULL
  fRebatePerc float NULL
  iBillingFrequency int NOT NULL
  bIsDualMeter bit NOT NULL
  iDualMeterID int NOT NULL
  iServiceUnits decimal(18,2) NOT NULL
  iBillTrCodeID int NOT NULL
  iRebateTrCodeID int NOT NULL
  iExclusionTrCodeID int NOT NULL
  iExemptionTrCodeID int NOT NULL
  iImpermissableTrCodeID int NOT NULL
  iReductionTrCodeID int NOT NULL
  bPercCalculation bit NOT NULL
  bIncrementalBilling bit NOT NULL
  bDemandBilling bit NOT NULL
  fAveragePerc float NOT NULL
  cRateTariff varchar(50) NOT NULL
  cRateTariffDescription varchar(100) NULL
  cReaderName varchar(50) NULL
  fFreeConsumption float NULL
  bBillable bit NOT NULL
  cMeterNumber varchar(50) NULL
  cCategory varchar(50) NULL
  fDeposit float NULL
  iDepositTrCodeID int NOT NULL
  fFinalizationDetailMeterFactor float NULL
  bFinalizationApplyPortionValue bit NOT NULL default (0)
  fFinalReadingConsumption float NOT NULL
  fOverrideFlatRate float NULL
  iFinalReadingConsumption int NULL
  fProRataBalance float NULL

## _mtblFinalizations
PK: idFinalization
Columns (41):
  idFinalization int NOT NULL identity PK
  cFinalizationCode varchar(20) NOT NULL
  dFinalizationDate datetime NOT NULL
  iPropertyID int NOT NULL
  iPortionID int NOT NULL
  iFinalizationStatus int NOT NULL
  iFinalizationType int NOT NULL
  iCurrentCustomerID int NOT NULL
  cAccount varchar(20) NOT NULL
  cName varchar(50) NOT NULL
  cForwardingAddress01 varchar(40) NULL
  cForwardingAddress02 varchar(40) NULL
  cForwardingAddress03 varchar(40) NULL
  cForwardingAddress04 varchar(40) NULL
  cForwardingAddress05 varchar(40) NULL
  cForwardingPC varchar(15) NULL
  iNewCustomerID int NULL
  dDateCreated datetime NOT NULL
  dDateLastAction datetime NOT NULL
  dDateFinalized datetime NULL
  iPeriodID int NOT NULL
  iPropertyAreaID int NULL
  cERFNo varchar(50) NOT NULL
  cPortion varchar(50) NOT NULL
  fPortionSize float NULL
  fPortionLandValue float NULL
  fPortionImprovementValue float NULL
  iPortionUsageID int NOT NULL
  iPortionSubsidyType int NOT NULL
  bIsBodyCorporate bit NOT NULL
  iBodyCorporatePortions int NOT NULL
  cArea varchar(50) NULL
  cRegion varchar(50) NULL
  cSubRegion varchar(50) NULL
  fAccountBalance float NOT NULL
  cNewAccount varchar(20) NULL
  cNewName varchar(50) NULL
  cTitleDeed varchar(100) NULL
  bBasicServicesProRataCalculated bit NULL
  cUserNameCreated varchar(50) NULL
  cUserNameLastActioned varchar(50) NULL

## _mtblHistPropertyPortions
PK: idHistPropertyPortions
Columns (20):
  idHistPropertyPortions int NOT NULL identity PK
  cHistPortion varchar(50) NULL
  cHistPortionDescription varchar(100) NULL
  iHistPortionPropertyID int NULL
  iHistPortionPortionID int NULL
  fHistPortionSize float NULL
  fHistPortionLandValue float NULL
  fHistPortionImprovementValue float NULL
  iHistPropertyOwnerID int NULL
  iHistPortionUsageID int NULL
  iHistPortionRegionID int NULL
  iHistPortionSubRegionID int NULL
  iHistPortionAreaID int NULL
  iHistPortionWardID int NULL
  dHistValuationEndDate datetime NOT NULL
  iHistValuationRollID int NOT NULL
  iHistPropertyTaxRateTariffID int NULL
  iValuationChangedReasonID int NULL
  dTimeStamp datetime NOT NULL
  iHistPortionRatingID int NULL

## _mtblInvoiceNumbers
PK: idInvoiceNumber
Columns (4):
  idInvoiceNumber bigint NOT NULL identity PK
  iBillingRunId int NOT NULL
  iAccountNumber int NOT NULL
  iPeriodId int NOT NULL

## _mtblMBRCategories
PK: idMBRCategories
Columns (14):
  idMBRCategories int NOT NULL identity PK
  cMBRCategory varchar(20) NULL
  cMBRDescription varchar(100) NULL
  iMBRType int NULL
  iMBRCategoryLinkID int NULL
  _mtblMBRCategories_iBranchID int NULL
  _mtblMBRCategories_dCreatedDate datetime NULL
  _mtblMBRCategories_dModifiedDate datetime NULL
  _mtblMBRCategories_iCreatedBranchID int NULL
  _mtblMBRCategories_iModifiedBranchID int NULL
  _mtblMBRCategories_iCreatedAgentID int NULL
  _mtblMBRCategories_iModifiedAgentID int NULL
  _mtblMBRCategories_iChangeSetID int NULL
  _mtblMBRCategories_Checksum binary(20) NULL

## _mtblMeterHistory
PK: idMeterHistory
Columns (10):
  idMeterHistory int NOT NULL identity PK
  iHistoryMeterID int NULL
  iHistoryPropertyPortionServiceID int NULL
  iHistoryConsumerID int NULL
  iHistoryStatus int NULL
  dHistoryDate datetime NULL
  fHistoryReading float NOT NULL
  cReason varchar(200) NULL
  iHistoryUserName varchar(50) NULL
  dHistorySysDate datetime NULL

## _mtblMeterReaders
PK: idMeterReader
Columns (5):
  idMeterReader int NOT NULL identity PK
  cReaderName varchar(50) NOT NULL
  cIDNumber varchar(25) NULL
  cContactNumber varchar(25) NULL
  bActive bit NULL

## _mtblMeterReadingDetails
PK: idMeterReadingDetails
Columns (21):
  idMeterReadingDetails int NOT NULL identity PK
  iMeterReadingsID int NULL
  iMeterReadingsMeterID int NULL
  iBillingPeriodID int NULL
  dtFromReadingDate datetime NULL
  dtToReadingDate datetime NULL
  fPreviousReading float NOT NULL
  fCurrentReading float NOT NULL
  fConsumption float NULL
  iFailureReasonID int NULL
  bCalculated bit NOT NULL default (0)
  bProcessed bit NOT NULL default (0)
  iReadingType int NULL
  iNoteID int NULL
  iConsumerID int NULL
  bShouldBill bit NOT NULL default (1)
  fMeterReadingMeterFactor float NULL
  fReadingConsumption float NOT NULL
  cUserName varchar(20) NULL
  iReadingConsumption int NULL
  bEarlyReading bit NOT NULL default (0)

## _mtblMeterReadingDetailsTimeOfUse
PK: idMeterReadingDetailsTimeOfUse
Columns (5):
  idMeterReadingDetailsTimeOfUse int NOT NULL identity PK
  iMeterReadingDetailsID int NULL
  iRateTariffBandsID int NULL
  fConsumption float NULL
  iFinalizationDetailID int NULL

## _mtblMeterReadings
PK: idMeterReadings
Columns (9):
  idMeterReadings int NOT NULL identity PK
  iReadingWalkID int NULL
  iBillingPeriod int NULL
  iMeterReaderID int NULL
  cDocument varchar(50) NULL
  iReadingStatus int NULL
  bCalculationRun bit NOT NULL default (0)
  cReadingDescription varchar(100) NULL
  dCapturedDate datetime NULL

## _mtblMeters
PK: idMeter
Columns (20):
  idMeter int NOT NULL identity PK
  cMeterNumber varchar(50) NULL
  cMeterSerialNumber varchar(50) NULL
  cMeterLocation varchar(500) NULL
  iMeterTypeID int NULL
  iServiceTypeID int NULL
  iStatus int NULL
  dtStatusDate datetime NULL
  dtInstallDate datetime NULL
  fTakeonReading float NOT NULL
  iMeterUserID int NULL
  dtMeterSysDate datetime NULL
  bResetAfterReading bit NULL default (0)
  bIsControlMeter bit NULL
  iControlMeterID int NULL
  fMeterFactor float NULL
  fGPSLatitude float NOT NULL default (0)
  fGPSLongitude float NOT NULL default (0)
  bIsPhasedMeter bit NULL
  iDefaultAverageValueMeters int NULL

## _mtblMeterTypes
PK: idMeterType
Columns (7):
  idMeterType int NOT NULL identity PK
  cMeterType varchar(50) NULL
  cMeterTypeDescription varchar(100) NULL
  cMeterTypeManufacturer varchar(100) NULL
  iMeterTypeDigits int NULL
  iMeterTypeClockOver int NULL
  iMeterTypeTolerance int NULL

## _mtblPortionRules
PK: iPropertyPortionID+iRebateRuleID
Columns (2):
  iPropertyPortionID int NOT NULL PK
  iRebateRuleID int NOT NULL PK

## _mtblPreBillingTransactionsHistory
PK: idTransactions
Columns (26):
  idTransactions int NOT NULL identity PK
  iCustomerID int NULL
  iPropertyID int NULL
  iPortionID int NULL
  iPropertyPortionServiceID int NULL
  iServiceID int NULL
  iRateTariffID int NULL
  iRateTariffBandID int NULL
  iTrCodeID int NULL
  iPeriodID int NULL
  iUnits float NULL
  iMeterID int NULL
  fExclusiveAmount float NULL
  fTaxAmount float NULL
  fInclusiveAmount float NULL
  iPostARID bigint NULL
  cAuditNo varchar(50) NULL
  cReference varchar(50) NULL
  cDescription varchar(100) NULL
  iBillingRunID int NULL
  iTransType int NULL
  cUserName varchar(20) NULL
  iFinalizationID int NULL
  dteRunDateTime datetime NULL
  iLinkedTransID int NULL
  dTransactionDate datetime NULL

## _mtblProperties
PK: idProperty
Columns (26):
  idProperty int NOT NULL identity PK
  cERFNo varchar(50) NULL
  cAddress1 varchar(50) NULL
  cAddress2 varchar(50) NULL
  cAddress3 varchar(50) NULL
  cAddress4 varchar(50) NULL
  cAddress5 varchar(50) NULL
  cPostalCode nchar(10) NULL
  cGPS varchar(50) NULL
  cDeedsNumber varchar(100) NULL
  iWardID int NULL
  iZoneID int NULL
  iUsageID int NULL
  iPropertyOwnerID int NULL
  fLandSize float NULL
  fLandValue float NULL
  fImprovementValue float NULL
  iNoPortions int NULL
  iPropertyRegionID int NULL
  iPropertySubRegionID int NULL
  iPropertyAreaID int NULL
  fPropertyGPSLatitude float NOT NULL default (0)
  fPropertyGPSLongitude float NOT NULL default (0)
  cSGCode varchar(50) NULL
  iRatingID int NULL
  iBillingCycle int NULL default (0)

## _mtblPropertyPortions
PK: idPropertyPortions
Columns (15):
  idPropertyPortions int NOT NULL identity PK
  cPortion varchar(50) NULL
  cPortionDescription varchar(100) NULL
  iPortionPropertyID int NULL
  fPortionSize float NULL
  fPortionLandValue float NULL
  fPortionImprovementValue float NULL
  iPortionConsumerID int NULL
  iPortionUsageID int NULL
  iPortionSubsidyType int NOT NULL default (0)
  bIsBodyCorporate bit NULL
  iBodyCorporatePortions int NULL
  iValuationRollID int NULL
  iPortionRatingID int NULL
  bAllowMultipleClearances bit NOT NULL default (0)

## _mtblPropertyPortionServices
PK: idPropertyPortionServices
Columns (15):
  idPropertyPortionServices int NOT NULL identity PK
  iPropertyPortionID int NULL
  iServiceConsumerID int NULL
  iPropertyPortionMeterID int NULL
  iServiceRateTariffID int NULL
  iPortionServiceID int NULL
  iServiceUnits decimal(18,2) NULL
  bBillable bit NOT NULL default (1)
  fDeposit float NULL
  fRebatePerc float NULL
  iDualMeterID int NULL
  bIsDualMeter bit NOT NULL default (0)
  fFreeConsumption float NULL
  fOverrideFlatRate float NULL
  iRateTariffQuota int NULL

## _mtblPropertyPortionServicesQuotaHistory
PK: idPropertyPortionServicesQuotaHistoryID
Columns (6):
  idPropertyPortionServicesQuotaHistoryID int NOT NULL identity PK
  iPropertyPortionServiceID int NULL
  iRateTariffQuotaID int NULL
  iPeriodID int NULL
  dServiceUnits decimal(18,2) NULL
  iRateTariffID int NULL

## _mtblPropertyServiceContracts
PK: idPropertyServiceContracts
Columns (7):
  idPropertyServiceContracts int NOT NULL identity PK
  iServiceContractPropertyID int NULL
  iServiceContractServiceID int NULL
  iServiceContractRateTariffID int NULL
  fDailyConsumptionLimit float NOT NULL
  bOverrideRateTariff bit NOT NULL default (0)
  fOverrideRate float NULL

## _mtblRateTariffBands
PK: idRateTariffBands
Columns (26):
  idRateTariffBands int NOT NULL identity PK
  iRateTariffID int NULL
  iFromPeriodID int NULL
  iToPeriodID int NULL
  fBandAmount float NULL
  bCalculateAverage bit NULL
  fExclusionAmount float NULL
  fExemptionAmount float NULL
  fReductionAmount float NULL
  fImpermissableAmount float NULL
  fToValue float NULL
  iMinLevel int NULL
  iMaxLevel int NULL
  iDefaultAverageValue int NULL
  iMaxAverageCalcMonths int NULL
  iCalcMonths int NULL
  iPhasingInCurrentYear int NULL
  fPhasingInYear1Perc float NULL
  fPhasingInYear2Perc float NULL
  fPhasingInYear3Perc float NULL
  fPhasingInYear4Perc float NULL
  iPhasingInTrCodeID int NULL
  fRebatePercentage float NULL
  iWeightPercentage int NULL
  bDefaultTOUBand bit NULL
  cDescription varchar(100) NULL

## _mtblRateTariffCategories
PK: idRateTarrifCategories
Columns (3):
  idRateTarrifCategories int NOT NULL identity PK
  iRateTarrifID int NOT NULL
  iCategoryID int NOT NULL

## _mtblRateTariffQuota
PK: idQuota
Columns (11):
  idQuota int NOT NULL identity PK
  cQuotaName varchar(500) NULL
  fQuotaMaximum float NULL
  fQuotaTariff float NULL
  bApplySubsidy bit NULL
  fSubsidyUnits float NULL default (6)
  iBasicChargeRateTariffID int NULL
  iQuotaTariffRebatePercentage int NULL
  bApplySubsidyMaxExceeded bit NULL
  bIndigentTariffQuota bit NOT NULL default (0)
  iNonIndigentTariffQuotaID int NOT NULL default (0)

## _mtblRateTariffs
PK: idRateTariffs
Columns (31):
  idRateTariffs int NOT NULL identity PK
  cRateTariff varchar(50) NULL
  cRateTariffDescription varchar(100) NULL
  iRateTariffServiceID int NULL
  iCategoryID int NULL
  iBillTrCodeID int NULL
  iRecTrCodeID int NULL
  iAdjTrCodeID int NULL
  iDepositTrCodeID int NULL
  iRebateTrCodeID int NULL
  iExclusionTrCodeID int NULL
  iExemptionTrCodeID int NULL
  iImpermissableTrCodeID int NULL
  iReductionTrCodeID int NULL
  bIncrementalBilling bit NOT NULL default (1)
  bDualMeters bit NOT NULL default (0)
  fAveragePerc float NULL
  bDemandBilling bit NOT NULL default (0)
  bPercCalculation bit NOT NULL default (0)
  iRateTariffRegionID int NULL
  iRateTariffSubRegionID int NULL
  iRateTariffAreaID int NULL
  iBillingFrequency int NOT NULL default (0)
  iDepositReversalTrCodeID int NULL
  iDirectDepositTrCodeID int NULL
  iDepositRefundTrCodeID int NULL
  bTimeOfUseBilling bit NOT NULL default (0)
  bProRateIncrementalBilling bit NOT NULL default (0)
  iReversalTrCodeID int NULL
  bIndigentTariff bit NOT NULL default (0)
  iNonIndigentTariffID int NOT NULL default (0)

## _mtblRebateRules
PK: idRebateRule
Columns (10):
  idRebateRule int NOT NULL identity PK
  cRuleName nvarchar(255) NOT NULL
  cRuleDescription nvarchar(max) NOT NULL
  bActive bit NOT NULL
  bAppliesToAllServices bit NOT NULL
  bAppliesToPortion bit NOT NULL
  bAppliesToClient bit NOT NULL
  fRebateAmount float NOT NULL
  bRebateIsPercentage bit NOT NULL
  iRebateTRCodeID int NOT NULL

## _mtblRegions
PK: idRegions
Columns (4):
  idRegions int NOT NULL identity PK
  cRegion varchar(50) NULL
  cRegionDescription varchar(100) NULL
  cRegionDetails varchar(2000) NULL

## _mtblServiceGroups
PK: idServiceGroup
Columns (4):
  idServiceGroup int NOT NULL identity PK
  cServiceGroup varchar(50) NULL
  cServiceGroupDescription varchar(100) NULL
  iSupplierID int NULL

## _mtblServiceRules
PK: iServiceID+iRebateRuleID
Columns (2):
  iServiceID int NOT NULL PK
  iRebateRuleID int NOT NULL PK

## _mtblServices
PK: idService
Columns (17):
  idService int NOT NULL identity PK
  cService varchar(50) NULL
  cServiceDescription varchar(100) NULL
  iPaymentPriority int NULL
  iCalculationType int NULL
  bDefaultService bit NOT NULL default (0)
  iLinkedServiceID int NULL
  iServiceGroupID int NULL default (0)
  bApplyPortionSize bit NOT NULL default (0)
  iServiceReportingCatID int NULL
  cServiceUnitOfMeasure varchar(5) NULL
  bApplyPortionValue bit NOT NULL default (0)
  iApplyBandRateType int NULL default (0)
  bIncludeMainServiceFreeConsumption bit NULL default (1)
  fPaymentPriorityPercentage float NULL
  iUsageType int NULL
  bIsInterestOnly bit NOT NULL default (0)

## _mtblSubRegions
PK: idSubRegions
Columns (4):
  idSubRegions int NOT NULL identity PK
  cSubRegion varchar(50) NULL
  cSubRegionDescription varchar(100) NULL
  cSubRegionDetails varchar(2000) NULL

## _mtblSubsidies
PK: idSubsidy
Columns (6):
  idSubsidy int NOT NULL identity PK
  iSubsidyCategoryID int NOT NULL default (0)
  iSubsidyAreaID int NOT NULL default (0)
  bIsPercent bit NOT NULL default (0)
  fValue float NOT NULL default (0)
  iSubsidyTrCodeID int NOT NULL default (0)

## _mtblTransactions
PK: idTransactions
Columns (26):
  idTransactions int NOT NULL identity PK
  iCustomerID int NULL
  iPropertyID int NULL
  iPortionID int NULL
  iPropertyPortionServiceID int NULL
  iServiceID int NULL
  iRateTariffID int NULL
  iRateTariffBandID int NULL
  iTrCodeID int NULL
  iPeriodID int NULL
  iUnits float NULL
  iMeterID int NULL
  fExclusiveAmount float NULL
  fTaxAmount float NULL
  fInclusiveAmount float NULL
  iPostARID bigint NULL
  cAuditNo varchar(50) NULL
  cReference varchar(50) NULL
  cDescription varchar(100) NULL
  iBillingRunID int NULL
  iTransType int NULL
  cUserName varchar(20) NULL
  iFinalizationID int NULL
  iLinkedTransID int NULL
  dTransactionDate datetime NULL
  iPropertyPortionUsageID int NULL

## _mtblValuationChangedReasons
PK: idValuationChangedReason
Columns (3):
  idValuationChangedReason int NOT NULL identity PK
  cValuationChangedReasonCode varchar(50) NULL
  cValuationChangedReasonDescription varchar(150) NULL

## _mtblValuationRolls
PK: idValuationRoll
Columns (5):
  idValuationRoll int NOT NULL identity PK
  cValuationRoll varchar(50) NOT NULL
  cValuationRollDescription varchar(100) NULL
  dValuationEffectiveDate datetime NOT NULL
  iValuationType int NOT NULL

## _mtblWalkDetails
PK: idWalkDetail
Columns (6):
  idWalkDetail int NOT NULL identity PK
  iWalkID int NULL
  iWalkPropertyID int NULL
  iWalkPortionID int NULL
  iWalkMeterID int NULL
  iWalkSequence int NULL

## _mtblWalks
PK: idWalk
Columns (9):
  idWalk int NOT NULL identity PK
  cWalkCode varchar(50) NULL
  cWalkDescription varchar(100) NULL
  iWalkReaderID int NULL
  cWalkServices varchar(1024) NULL
  iWalkRegionID int NULL
  iWalkSubRegionID int NULL
  iWalkAreaID int NULL
  bTimeOfUseBillingProperties bit NULL default (0)

## _mtblWards
PK: idWard
Columns (4):
  idWard int NOT NULL identity PK
  cWard varchar(50) NOT NULL
  cWardDescription varchar(100) NULL
  cWardDetail varchar(2000) NULL

## _tAudit - Audit Table
Alias: Audit Table | Freedom Name:  | Record Identifier: 
Notes: Municipal billing Audit Table
PK: none
Columns (10):
  TableName varchar(128) NOT NULL
  TableID varchar(1000) NULL
  FieldName varchar(128) NOT NULL
  OldValue varchar(1000) NULL
  NewValue varchar(1000) NULL
  UpdateDate datetime NULL default getdate()
  UserName varchar(128) NULL default suser_sname()
  WorkStation varchar(128) NULL default host_name()
  Application varchar(128) NULL default app_name()
  Status int NULL
