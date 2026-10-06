<!-- source: DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata) | version: Acumatica ERP 2026 R2 | verified: 2026-10-06 -->

# PX.Objects.AP.CuryAPHistory (EntityType)

Label: "Currency AP History"
Key: AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID
Entity sets: PX_Objects_AP_CuryAPHistory, CurrencyAPHistory, CuryAPHistory
Non-filterable, non-selectable: FinFlag, PtdCrAdjustments, PtdDrAdjustments, PtdPurchases, PtdPayments, PtdDiscTaken, PtdWhTax, PtdRGOL, YtdBalance, BegBalance, PtdDeposits, YtdDeposits, CuryPtdCrAdjustments, CuryPtdDrAdjustments, CuryPtdPurchases, CuryPtdPayments, CuryPtdDiscTaken, CuryPtdWhTax, CuryYtdBalance, CuryBegBalance, CuryPtdDeposits, CuryYtdDeposits, PtdRetainageWithheld, YtdRetainageWithheld, CuryPtdRetainageWithheld, CuryYtdRetainageWithheld, PtdRetainageReleased, YtdRetainageReleased, CuryPtdRetainageReleased, CuryYtdRetainageReleased

PX.Objects.AP.CuryAPHistory.BranchID : Edm.Int32 [key]
PX.Objects.AP.CuryAPHistory.AccountID : Edm.Int32 [key]
PX.Objects.AP.CuryAPHistory.SubID : Edm.Int32 [key]
PX.Objects.AP.CuryAPHistory.FinPeriodID : Edm.String [key]
PX.Objects.AP.CuryAPHistory.VendorID : Edm.Int32 [key]
PX.Objects.AP.CuryAPHistory.CuryID : Edm.String [key]
PX.Objects.AP.CuryAPHistory.DetDeleted : Edm.Boolean [required]
PX.Objects.AP.CuryAPHistory.FinBegBalance : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdPurchases : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdPayments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdDiscTaken : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdWhTax : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdRGOL : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinYtdBalance : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdDeposits : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinYtdDeposits : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinPtdRevalued : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranBegBalance : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdPurchases : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdPayments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdDiscTaken : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdWhTax : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdRGOL : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranYtdBalance : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdDeposits : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranYtdDeposits : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinBegBalance : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinPtdPurchases : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinPtdPayments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinPtdDiscTaken : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinPtdWhTax : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinYtdBalance : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinPtdDeposits : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinYtdDeposits : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranBegBalance : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdPurchases : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdPayments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdDiscTaken : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdWhTax : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranYtdBalance : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdDeposits : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranYtdDeposits : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.tstamp : Edm.Binary
PX.Objects.AP.CuryAPHistory.FinFlag : Edm.Boolean
PX.Objects.AP.CuryAPHistory.PtdCrAdjustments : Edm.Decimal
PX.Objects.AP.CuryAPHistory.PtdDrAdjustments : Edm.Decimal
PX.Objects.AP.CuryAPHistory.PtdPurchases : Edm.Decimal
PX.Objects.AP.CuryAPHistory.PtdPayments : Edm.Decimal
PX.Objects.AP.CuryAPHistory.PtdDiscTaken : Edm.Decimal
PX.Objects.AP.CuryAPHistory.PtdWhTax : Edm.Decimal
PX.Objects.AP.CuryAPHistory.PtdRGOL : Edm.Decimal
PX.Objects.AP.CuryAPHistory.YtdBalance : Edm.Decimal
PX.Objects.AP.CuryAPHistory.BegBalance : Edm.Decimal
PX.Objects.AP.CuryAPHistory.PtdDeposits : Edm.Decimal
PX.Objects.AP.CuryAPHistory.YtdDeposits : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryPtdCrAdjustments : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryPtdDrAdjustments : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryPtdPurchases : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryPtdPayments : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryPtdDiscTaken : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryPtdWhTax : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryYtdBalance : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryBegBalance : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryPtdDeposits : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryYtdDeposits : Edm.Decimal
PX.Objects.AP.CuryAPHistory.FinPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.PtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.CuryAPHistory.YtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryFinPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryPtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryYtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.CuryAPHistory.FinPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.FinYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.TranYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.PtdRetainageReleased : Edm.Decimal
PX.Objects.AP.CuryAPHistory.YtdRetainageReleased : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryFinPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryFinYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryTranYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AP.CuryAPHistory.CuryPtdRetainageReleased : Edm.Decimal
PX.Objects.AP.CuryAPHistory.CuryYtdRetainageReleased : Edm.Decimal
PX.Objects.AP.CuryAPHistory.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.AP.CuryAPHistory.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.CuryAPHistory.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AP.CuryAPHistory.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AP.CuryAPHistory.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.AP.CuryAPHistory.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.AP.CuryAPHistoryTran (ComplexType)


PX.Objects.AP.CuryAPHistoryTran.ID : Edm.Int32
PX.Objects.AP.CuryAPHistoryTran.DocType : Edm.String
PX.Objects.AP.CuryAPHistoryTran.RefNbr : Edm.String
PX.Objects.AP.CuryAPHistoryTran.LineNbr : Edm.Int32
PX.Objects.AP.CuryAPHistoryTran.SourceDocType : Edm.String
PX.Objects.AP.CuryAPHistoryTran.SourceRefNbr : Edm.String
PX.Objects.AP.CuryAPHistoryTran.CuryInfoID : Edm.Int64
PX.Objects.AP.CuryAPHistoryTran.CuryID : Edm.String
PX.Objects.AP.CuryAPHistoryTran.VendorID : Edm.Int32
PX.Objects.AP.CuryAPHistoryTran.FinPeriodID : Edm.String
PX.Objects.AP.CuryAPHistoryTran.TranPeriodID : Edm.String
PX.Objects.AP.CuryAPHistoryTran.BatchNbr : Edm.String
PX.Objects.AP.CuryAPHistoryTran.Type : Edm.String
PX.Objects.AP.CuryAPHistoryTran.TranType : Edm.String
PX.Objects.AP.CuryAPHistoryTran.TranRefNbr : Edm.String
PX.Objects.AP.CuryAPHistoryTran.IsMigratedRecord : Edm.Boolean
PX.Objects.AP.CuryAPHistoryTran.CuryPtdPurchases : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.CuryPtdPayments : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.CuryPtdDrAdjustments : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.CuryPtdCrAdjustments : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.CuryPtdDiscTaken : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.CuryPtdWhTax : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.CuryPtdDeposits : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.CuryPtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.CuryPtdRetainageReleased : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdPurchases : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdPayments : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdDrAdjustments : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdCrAdjustments : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdDiscTaken : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdWhTax : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdRGOL : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdDeposits : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdRetainageWithheld : Edm.Decimal
PX.Objects.AP.CuryAPHistoryTran.PtdRetainageReleased : Edm.Decimal

# PX.Objects.AP.DAC.VendorPaymentMethod (EntityType)

Label: "Update Vendor Payment Methods"
BaseType: PX.Objects.AP.Vendor
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_AP_DAC_VendorPaymentMethod, UpdateVendorPaymentMethods, VendorPaymentMethod

PX.Objects.AP.DAC.VendorPaymentMethod.LocationID : Edm.Int32 "Location ID"
PX.Objects.AP.DAC.VendorPaymentMethod.VPaymentMethodID : Edm.String "Payment Method"
PX.Objects.AP.DAC.VendorPaymentMethod.City : Edm.String "City"
PX.Objects.AP.DAC.VendorPaymentMethod.State : Edm.String "State"
PX.Objects.AP.DAC.VendorPaymentMethod.CountryID : Edm.String "Country"
PX.Objects.AP.DAC.VendorPaymentMethod.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.AP.DAC.VendorPaymentMethod.CashAccountByVCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.AP.DAC.VendorPaymentMethod.PaymentMethodByVPaymentMethodID -> PX.Objects.CA.PaymentMethod (VPaymentMethodID=PaymentMethodID)
PX.Objects.AP.DAC.VendorPaymentMethod.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.AP.DAC.VendorPaymentMethod.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.AP.DAC.VendorPaymentMethod.FSAppointmentInRouteCollection -> Collection(PX.Objects.FS.FSAppointmentInRoute)
PX.Objects.AP.DAC.VendorPaymentMethod.BCRoleAssignmentCollection -> Collection(PX.Commerce.Shopify.BCRoleAssignment)
PX.Objects.AP.DAC.VendorPaymentMethod.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.AP.DAC.VendorPaymentMethod.AMBomOperCuryCollection -> Collection(PX.Objects.AM.AMBomOperCury)

# PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice (EntityType)

Label: "Recognized document"
BaseType: PX.Objects.AP.APInvoice
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_InvoiceRecognition_DAC_APRecognizedInvoice, Recognizeddocument, APRecognizedInvoice
Non-filterable, non-selectable: IsRedirect, RecognitionStatus, AllowFiles, AllowFilesMsg, AllowUploadFile, FileID, RecognizedDataJson, VendorTermIndex, VendorName, VendorSearchError, IsDataLoaded

PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordRefNbr : Edm.Guid "Recognized Record Ref. Nbr."
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.EntityType : Edm.String "Entity Type"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.FileHash : Edm.Binary "File Hash"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordStatus : Edm.String "Status"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognitionStarted : Edm.Boolean "Recognition Started"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognitionResult : Edm.String "Recognition Result"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognitionFeedback : Edm.String "Recognition Feedback"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.DocumentLink : Edm.Guid "Document Link"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.DuplicateLink : Edm.Guid "Link to Duplicate File"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.MailFrom : Edm.String "From"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.Subject : Edm.String "Summary"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.MessageID : Edm.String "Message ID"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.Owner : Edm.Int32 "Owner"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.CustomInfo : Edm.String "Custom Info"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.ErrorMessage : Edm.String "Error Message"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordCreatedByID : Edm.Guid "Created By"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordCreatedByScreenID : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordCreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordLastModifiedByScreenID : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedRecordTStamp : Edm.Binary
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.IsRedirect : Edm.Boolean "Is Redirect"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognitionStatus : Edm.String "Status"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.AllowFiles : Edm.String "Allow Files"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.AllowFilesMsg : Edm.String "Allow File Message"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.AllowUploadFile : Edm.Boolean "Allow File Upload"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.FileID : Edm.Guid "File ID"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.RecognizedDataJson : Edm.String "Recognized Data"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.VendorTermIndex : Edm.Int32 "Vendor Term"
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.VendorName : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.VendorSearchError : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.APRecognizedInvoice.IsDataLoaded : Edm.Boolean "Is Data Loaded"

# PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain (EntityType)

Label: "Excluded Email Domains"
Key: Name
Entity sets: PX_Objects_AP_InvoiceRecognition_DAC_ExcludedVendorDomain, ExcludedEmailDomains, ExcludedVendorDomain

PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.Name : Edm.String [key] "Domain Name"
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.CreatedByScreenID : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.LastModifiedByScreenID : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.TStamp : Edm.Binary
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.InvoiceRecognition.DAC.ExcludedVendorDomain.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.AP.InvoiceRecognition.DAC.RecognizedRecordSplit (EntityType)

Label: "Recognized Document Split"
Key: RefNbr
Entity sets: PX_Objects_AP_InvoiceRecognition_DAC_RecognizedRecordSplit, RecognizedDocumentSplit, RecognizedRecordSplit
Non-filterable, non-selectable: SplitStatus

PX.Objects.AP.InvoiceRecognition.DAC.RecognizedRecordSplit.RefNbr : Edm.Guid [key]
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedRecordSplit.OriginalRecordRefNbr : Edm.Guid
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedRecordSplit.SplitStatus : Edm.String "Split Status"
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedRecordSplit.RecognizedRecordByRefNbr -> PX.CloudServices.DAC.RecognizedRecord (RefNbr=RefNbr)

# PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping (EntityType)

Label: "Vendor Specified in Recognized Documents"
Key: Id
Entity sets: PX_Objects_AP_InvoiceRecognition_DAC_RecognizedVendorMapping, VendorSpecifiedinRecognizedDocuments, RecognizedVendorMapping

PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.Id : Edm.Guid [key]
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.VendorNamePrefix : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.VendorName : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.VendorID : Edm.Int32
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.CreatedByScreenID : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.LastModifiedByScreenID : Edm.String
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.TStamp : Edm.Binary
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.AP.LocationAPAccountSub (EntityType)

Label: "Location GL Accounts"
Key: BAccountID, LocationID
Entity sets: PX_Objects_AP_LocationAPAccountSub, LocationGLAccounts, LocationAPAccountSub

PX.Objects.AP.LocationAPAccountSub.BAccountID : Edm.Int32 [key]
PX.Objects.AP.LocationAPAccountSub.LocationID : Edm.Int32 [key]
PX.Objects.AP.LocationAPAccountSub.VPaymentInfoLocationID : Edm.Int32
PX.Objects.AP.LocationAPAccountSub.VPaymentMethodID : Edm.String "Payment Method"
PX.Objects.AP.LocationAPAccountSub.VPaymentLeadTime : Edm.Int16 "Payment Lead Time (Days)"
PX.Objects.AP.LocationAPAccountSub.VSeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.AP.LocationAPAccountSub.VRemitAddressID : Edm.Int32
PX.Objects.AP.LocationAPAccountSub.VRemitContactID : Edm.Int32
PX.Objects.AP.LocationAPAccountSub.VAPAccountLocationID : Edm.Int32
PX.Objects.AP.LocationAPAccountSub.SubByVAPSubID -> PX.Objects.GL.Sub
PX.Objects.AP.LocationAPAccountSub.SubByVRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.AP.LocationAPAccountSub.ContactByDefContactID -> PX.Objects.CR.Contact
PX.Objects.AP.LocationAPAccountSub.ContactByVRemitContactID -> PX.Objects.CR.Contact (VRemitContactID=ContactID)
PX.Objects.AP.LocationAPAccountSub.AddressByDefAddressID -> PX.Objects.CR.Address
PX.Objects.AP.LocationAPAccountSub.AddressByVRemitAddressID -> PX.Objects.CR.Address (VRemitAddressID=AddressID)
PX.Objects.AP.LocationAPAccountSub.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)

# PX.Objects.AP.LocationAPPaymentInfo (EntityType)

Label: "Location Payment Settings"
Key: BAccountID, LocationID
Entity sets: PX_Objects_AP_LocationAPPaymentInfo, LocationPaymentSettings, LocationAPPaymentInfo
Non-filterable, non-selectable: OverrideRemitAddress, IsRemitAddressSameAsMain, OverrideRemitContact, IsRemitContactSameAsMain

PX.Objects.AP.LocationAPPaymentInfo.BAccountID : Edm.Int32 [key]
PX.Objects.AP.LocationAPPaymentInfo.LocationID : Edm.Int32 [key]
PX.Objects.AP.LocationAPPaymentInfo.VDefAddressID : Edm.Int32
PX.Objects.AP.LocationAPPaymentInfo.VDefContactID : Edm.Int32
PX.Objects.AP.LocationAPPaymentInfo.VPaymentInfoLocationID : Edm.Int32
PX.Objects.AP.LocationAPPaymentInfo.VPaymentMethodID : Edm.String "Payment Method"
PX.Objects.AP.LocationAPPaymentInfo.VPaymentLeadTime : Edm.Int16 "Payment Lead Time (Days)"
PX.Objects.AP.LocationAPPaymentInfo.VSeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.AP.LocationAPPaymentInfo.VPaymentByType : Edm.Int32 "Payment By"
PX.Objects.AP.LocationAPPaymentInfo.OverrideRemitAddress : Edm.Boolean "Override"
PX.Objects.AP.LocationAPPaymentInfo.IsRemitAddressSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.AP.LocationAPPaymentInfo.OverrideRemitContact : Edm.Boolean "Override"
PX.Objects.AP.LocationAPPaymentInfo.IsRemitContactSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.AP.LocationAPPaymentInfo.VRemitAddressID : Edm.Int32
PX.Objects.AP.LocationAPPaymentInfo.VRemitContactID : Edm.Int32
PX.Objects.AP.LocationAPPaymentInfo.VAPAccountLocationID : Edm.Int32
PX.Objects.AP.LocationAPPaymentInfo.PaymentMethodByVPaymentMethodID -> PX.Objects.CA.PaymentMethod (VPaymentMethodID=PaymentMethodID)
PX.Objects.AP.LocationAPPaymentInfo.ContactByDefContactID -> PX.Objects.CR.Contact
PX.Objects.AP.LocationAPPaymentInfo.ContactByVRemitContactID -> PX.Objects.CR.Contact (VRemitContactID=ContactID)
PX.Objects.AP.LocationAPPaymentInfo.AddressByDefAddressID -> PX.Objects.CR.Address
PX.Objects.AP.LocationAPPaymentInfo.AddressByVRemitAddressID -> PX.Objects.CR.Address (VRemitAddressID=AddressID)
PX.Objects.AP.LocationAPPaymentInfo.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)

# PX.Objects.AP.MISC1099EFileProcessingInfoRaw (EntityType)

Label: "AP 1099 History"
BaseType: PX.Objects.AP.AP1099History
Key: BoxNbr, BranchID, FinYear, VendorID (inherited from PX.Objects.AP.AP1099History)
Entity sets: PX_Objects_AP_MISC1099EFileProcessingInfoRaw
Non-filterable, non-selectable: PayerBAccountID

PX.Objects.AP.MISC1099EFileProcessingInfoRaw.VAcctCD : Edm.String "Vendor"
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.VAcctName : Edm.String "Vendor Name"
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.LTaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.PayerOrganizationID : Edm.Int32 "Payer Company"
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.PayerBranchID : Edm.Int32 "Payer Branch"
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.PayerBAccountID : Edm.Int32 "Payer"
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.MinReportAmt : Edm.Decimal
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.CountryID : Edm.String
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.State : Edm.String
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.BranchByPayerBranchID -> PX.Objects.GL.Branch (PayerBranchID=BranchID)
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.OrganizationByPayerOrganizationID -> PX.Objects.GL.DAC.Organization (PayerOrganizationID=OrganizationID)
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.AP.MISC1099EFileProcessingInfoRaw.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)

# PX.Objects.AP.Overrides.APDocumentRelease.AP1099Hist (EntityType)

Label: "AP 1099 History"
BaseType: PX.Objects.AP.AP1099History
Key: BoxNbr, BranchID, FinYear, VendorID (inherited from PX.Objects.AP.AP1099History)
Entity sets: PX_Objects_AP_Overrides_APDocumentRelease_AP1099Hist

PX.Objects.AP.Overrides.APDocumentRelease.AP1099Hist.AP1099YearByFinYear -> PX.Objects.AP.AP1099Year (FinYear=FinYear)

# PX.Objects.AP.Overrides.APDocumentRelease.AP1099Yr (EntityType)

Label: "AP 1099 Year"
BaseType: PX.Objects.AP.AP1099Year
Key: FinYear, OrganizationID (inherited from PX.Objects.AP.AP1099Year)
Entity sets: PX_Objects_AP_Overrides_APDocumentRelease_AP1099Yr

# PX.Objects.AP.Overrides.APDocumentRelease.APHistory2 (EntityType)

Label: "AP History"
BaseType: PX.Objects.AP.APHistory
Key: AccountID, BranchID, FinPeriodID, SubID, VendorID (inherited from PX.Objects.AP.APHistory)
Entity sets: PX_Objects_AP_Overrides_APDocumentRelease_APHistory2

# PX.Objects.AP.Overrides.APDocumentRelease.CuryAPHistory2 (EntityType)

Label: "Currency AP History"
BaseType: PX.Objects.AP.CuryAPHistory
Key: AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID (inherited from PX.Objects.AP.CuryAPHistory)
Entity sets: PX_Objects_AP_Overrides_APDocumentRelease_CuryAPHistory2

# PX.Objects.AP.Overrides.ScheduleMaint.DocumentSelection (EntityType)

Label: "Document"
BaseType: PX.Objects.AP.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_Overrides_ScheduleMaint_DocumentSelection

# PX.Objects.AP.PendingPPDVATAdjApp (EntityType)

Label: "Applications Pending VAT Adjustment for Prompt Payment Discount"
BaseType: PX.Objects.AP.APAdjust
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr (inherited from PX.Objects.AP.APAdjust)
Entity sets: PX_Objects_AP_PendingPPDVATAdjApp, ApplicationsPendingVATAdjustmentforPromptPaymentDiscount, PendingPPDVATAdjApp
Non-filterable, non-selectable: Index

PX.Objects.AP.PendingPPDVATAdjApp.Index : Edm.Int32
PX.Objects.AP.PendingPPDVATAdjApp.PayDocType : Edm.String
PX.Objects.AP.PendingPPDVATAdjApp.PayRefNbr : Edm.String
PX.Objects.AP.PendingPPDVATAdjApp.InvDocType : Edm.String
PX.Objects.AP.PendingPPDVATAdjApp.InvRefNbr : Edm.String
PX.Objects.AP.PendingPPDVATAdjApp.PPDAdjNbr : Edm.Int32
PX.Objects.AP.PendingPPDVATAdjApp.InvCuryID : Edm.String "Currency"
PX.Objects.AP.PendingPPDVATAdjApp.InvCuryInfoID : Edm.Int64
PX.Objects.AP.PendingPPDVATAdjApp.InvVendorLocationID : Edm.Int32
PX.Objects.AP.PendingPPDVATAdjApp.InvTaxZoneID : Edm.String
PX.Objects.AP.PendingPPDVATAdjApp.InvTaxCalcMode : Edm.String
PX.Objects.AP.PendingPPDVATAdjApp.InvTermsID : Edm.String "Credit Terms"
PX.Objects.AP.PendingPPDVATAdjApp.InvCuryOrigDocAmt : Edm.Decimal "Amount"
PX.Objects.AP.PendingPPDVATAdjApp.InvCuryOrigDiscAmt : Edm.Decimal "Cash Discount"
PX.Objects.AP.PendingPPDVATAdjApp.InvCuryVatTaxableTotal : Edm.Decimal "VAT Taxable Total"
PX.Objects.AP.PendingPPDVATAdjApp.InvCuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.AP.PendingPPDVATAdjApp.InvCuryDocBal : Edm.Decimal
PX.Objects.AP.PendingPPDVATAdjApp.InvoiceNbr : Edm.String "Vendor Ref."
PX.Objects.AP.PendingPPDVATAdjApp.DocDesc : Edm.String "Description"

# PX.Objects.AP.Standalone.APQuickCheck (EntityType)

Label: "Cash Purchase"
BaseType: PX.Objects.AP.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_AP_Standalone_APQuickCheck, CashPurchase, APQuickCheck
Non-filterable, non-selectable: VoidAppl, IsPrintingProcess, IsReleaseCheckProcess, DepositDate, HasWithHoldTax, HasUseTax

PX.Objects.AP.Standalone.APQuickCheck.SuppliedByVendorID : Edm.Int32
PX.Objects.AP.Standalone.APQuickCheck.SuppliedByVendorLocationID : Edm.Int32
PX.Objects.AP.Standalone.APQuickCheck.RemitAddressID : Edm.Int32
PX.Objects.AP.Standalone.APQuickCheck.RemitContactID : Edm.Int32 "Remittance Contact"
PX.Objects.AP.Standalone.APQuickCheck.TermsID : Edm.String "Terms"
PX.Objects.AP.Standalone.APQuickCheck.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.AP.Standalone.APQuickCheck.TaxAmt : Edm.Decimal
PX.Objects.AP.Standalone.APQuickCheck.APInvoiceDocType : Edm.String
PX.Objects.AP.Standalone.APQuickCheck.APInvoiceRefNbr : Edm.String
PX.Objects.AP.Standalone.APQuickCheck.InvoiceNbr : Edm.String "Vendor Ref."
PX.Objects.AP.Standalone.APQuickCheck.InvoiceDate : Edm.DateTimeOffset "Vendor Ref. Date"
PX.Objects.AP.Standalone.APQuickCheck.TaxZoneID : Edm.String "Vendor Tax Zone"
PX.Objects.AP.Standalone.APQuickCheck.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.AP.Standalone.APQuickCheck.TaxTotal : Edm.Decimal
PX.Objects.AP.Standalone.APQuickCheck.CuryLineTotal : Edm.Decimal "Detail Total"
PX.Objects.AP.Standalone.APQuickCheck.LineTotal : Edm.Decimal
PX.Objects.AP.Standalone.APQuickCheck.CuryVatExemptTotal : Edm.Decimal "Tax Exempt Total"
PX.Objects.AP.Standalone.APQuickCheck.VatExemptTotal : Edm.Decimal
PX.Objects.AP.Standalone.APQuickCheck.CuryVatTaxableTotal : Edm.Decimal "Taxable Total"
PX.Objects.AP.Standalone.APQuickCheck.VatTaxableTotal : Edm.Decimal
PX.Objects.AP.Standalone.APQuickCheck.SeparateCheck : Edm.Boolean
PX.Objects.AP.Standalone.APQuickCheck.PaySel : Edm.Boolean
PX.Objects.AP.Standalone.APQuickCheck.EntityUsageType : Edm.String
PX.Objects.AP.Standalone.APQuickCheck.ExternalTaxExemptionNumber : Edm.String
PX.Objects.AP.Standalone.APQuickCheck.APPaymentDocType : Edm.String
PX.Objects.AP.Standalone.APQuickCheck.APPaymentRefNbr : Edm.String
PX.Objects.AP.Standalone.APQuickCheck.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AP.Standalone.APQuickCheck.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.AP.Standalone.APQuickCheck.AdjDate : Edm.DateTimeOffset "Date"
PX.Objects.AP.Standalone.APQuickCheck.AdjFinPeriodID : Edm.String "Post Period"
PX.Objects.AP.Standalone.APQuickCheck.AdjTranPeriodID : Edm.String
PX.Objects.AP.Standalone.APQuickCheck.StubCntr : Edm.Int32
PX.Objects.AP.Standalone.APQuickCheck.BillCntr : Edm.Int32
PX.Objects.AP.Standalone.APQuickCheck.Cleared : Edm.Boolean "Cleared"
PX.Objects.AP.Standalone.APQuickCheck.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.AP.Standalone.APQuickCheck.CATranID : Edm.Int64
PX.Objects.AP.Standalone.APQuickCheck.CuryOrigTaxDiscAmt : Edm.Decimal "Discounted Tax Amount"
PX.Objects.AP.Standalone.APQuickCheck.OrigTaxDiscAmt : Edm.Decimal
PX.Objects.AP.Standalone.APQuickCheck.ChargeCntr : Edm.Int32
PX.Objects.AP.Standalone.APQuickCheck.VoidAppl : Edm.Boolean
PX.Objects.AP.Standalone.APQuickCheck.PrintCheck : Edm.Boolean "Print Check"
PX.Objects.AP.Standalone.APQuickCheck.IsPrintingProcess : Edm.Boolean
PX.Objects.AP.Standalone.APQuickCheck.IsReleaseCheckProcess : Edm.Boolean
PX.Objects.AP.Standalone.APQuickCheck.DepositAsBatch : Edm.Boolean "Batch Deposit"
PX.Objects.AP.Standalone.APQuickCheck.DepositAfter : Edm.DateTimeOffset "Deposit After"
PX.Objects.AP.Standalone.APQuickCheck.Deposited : Edm.Boolean "Deposited"
PX.Objects.AP.Standalone.APQuickCheck.DepositDate : Edm.DateTimeOffset "Batch Deposit Date"
PX.Objects.AP.Standalone.APQuickCheck.DepositType : Edm.String "DepositType"
PX.Objects.AP.Standalone.APQuickCheck.DepositNbr : Edm.String "Batch Deposit Nbr."
PX.Objects.AP.Standalone.APQuickCheck.HasWithHoldTax : Edm.Boolean
PX.Objects.AP.Standalone.APQuickCheck.HasUseTax : Edm.Boolean
PX.Objects.AP.Standalone.APQuickCheck.ExternalPaymentID : Edm.String "External Payment ID"
PX.Objects.AP.Standalone.APQuickCheck.ExternalPaymentStatus : Edm.String "External Payment Status"
PX.Objects.AP.Standalone.APQuickCheck.ExternalPaymentIsVoidable : Edm.Boolean
PX.Objects.AP.Standalone.APQuickCheck.ExternalCheckDeliveryMethod : Edm.String "Fast Delivery Method"
PX.Objects.AP.Standalone.APQuickCheck.VendorBySuppliedByVendorID -> PX.Objects.AP.Vendor (SuppliedByVendorID=BAccountID)
PX.Objects.AP.Standalone.APQuickCheck.ContactByRemitContactID -> PX.Objects.CR.Contact (RemitContactID=ContactID)
PX.Objects.AP.Standalone.APQuickCheck.AddressByRemitAddressID -> PX.Objects.CR.Address (RemitAddressID=AddressID)
PX.Objects.AP.Standalone.APQuickCheck.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.AP.Standalone.APQuickCheck.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AP.Standalone.APQuickCheck.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AP.Standalone.APQuickCheck.LocationBySuppliedByVendorLocationID -> PX.Objects.CR.Location (SuppliedByVendorID=BAccountID, SuppliedByVendorLocationID=LocationID)
PX.Objects.AP.Standalone.APQuickCheck.APContactByRemitContactID -> PX.Objects.AP.APContact (RemitContactID=ContactID)

# PX.Objects.AP.Vendor (EntityType)

Label: "Vendor"
BaseType: PX.Objects.CR.BAccount
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_AP_Vendor, Vendor
Non-filterable, non-selectable: Hold, Included

PX.Objects.AP.Vendor.VendorClassID : Edm.String "Vendor Class"
PX.Objects.AP.Vendor.TermsID : Edm.String "Terms"
PX.Objects.AP.Vendor.DefPOAddressID : Edm.Int32
PX.Objects.AP.Vendor.PriceListCuryID : Edm.String "Currency ID"
PX.Objects.AP.Vendor.DefaultUOM : Edm.String "Default UOM"
PX.Objects.AP.Vendor.BaseRemitContactID : Edm.Int32 "Default Contact"
PX.Objects.AP.Vendor.Hold : Edm.Boolean "Hold"
PX.Objects.AP.Vendor.Approved : Edm.Boolean [required] "Approved"
PX.Objects.AP.Vendor.Rejected : Edm.Boolean [required] "Rejected"
PX.Objects.AP.Vendor.Vendor1099 : Edm.Boolean [required] "1099 Vendor"
PX.Objects.AP.Vendor.Box1099 : Edm.Int16 "1099 Box"
PX.Objects.AP.Vendor.FATCA : Edm.Boolean "FATCA"
PX.Objects.AP.Vendor.TaxAgency : Edm.Boolean [required] "Vendor Is Tax Agency"
PX.Objects.AP.Vendor.UpdClosedTaxPeriods : Edm.Boolean [required] "Update Closed Tax Periods"
PX.Objects.AP.Vendor.TaxReportPrecision : Edm.Int16 [required] "Tax Report Precision"
PX.Objects.AP.Vendor.TaxReportRounding : Edm.String "Tax Report Rounding"
PX.Objects.AP.Vendor.TaxUseVendorCurPrecision : Edm.Boolean [required] "Use Currency Precision"
PX.Objects.AP.Vendor.TaxReportFinPeriod : Edm.Boolean [required] "Define Tax Period by End Date of Financial Period"
PX.Objects.AP.Vendor.TaxPeriodType : Edm.String "Default Tax Period Type"
PX.Objects.AP.Vendor.AutoGenerateTaxBill : Edm.Boolean [required] "Automatically Generate Tax Bill"
PX.Objects.AP.Vendor.GroupMask : Edm.Binary
PX.Objects.AP.Vendor.LandedCostVendor : Edm.Boolean [required] "Landed Cost Vendor"
PX.Objects.AP.Vendor.Included : Edm.Boolean "Included"
PX.Objects.AP.Vendor.LineDiscountTarget : Edm.String "Apply Line Discounts to"
PX.Objects.AP.Vendor.IgnoreConfiguredDiscounts : Edm.Boolean [required] "Ignore Configured Discounts When Vendor Price Is Defined"
PX.Objects.AP.Vendor.ForeignEntity : Edm.Boolean "Foreign Entity"
PX.Objects.AP.Vendor.SVATReversalMethod : Edm.String "VAT Recognition Method"
PX.Objects.AP.Vendor.SVATInputTaxEntryRefNbr : Edm.String "Input Tax Entry Ref. Nbr."
PX.Objects.AP.Vendor.SVATOutputTaxEntryRefNbr : Edm.String "Output Tax Entry Ref. Nbr."
PX.Objects.AP.Vendor.SVATTaxInvoiceNumberingID : Edm.String "Tax Invoice Numbering"
PX.Objects.AP.Vendor.VendorByPayToVendorID -> PX.Objects.AP.Vendor
PX.Objects.AP.Vendor.BAccountByBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID, BAccountID=BAccountID)
PX.Objects.AP.Vendor.BAccountByPayToVendorID -> PX.Objects.CR.BAccount
PX.Objects.AP.Vendor.ContactByBaseRemitContactID -> PX.Objects.CR.Contact (BaseRemitContactID=ContactID)
PX.Objects.AP.Vendor.EPEmployeeClassByVendorClassID -> PX.Objects.EP.EPEmployeeClass (VendorClassID=VendorClassID)
PX.Objects.AP.Vendor.AddressByDefPOAddressID -> PX.Objects.CR.Address (DefPOAddressID=AddressID)
PX.Objects.AP.Vendor.NumberingBySVATTaxInvoiceNumberingID -> PX.Objects.CS.Numbering (SVATTaxInvoiceNumberingID=NumberingID)
PX.Objects.AP.Vendor.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AP.Vendor.CurrencyByPriceListCuryID -> PX.Objects.CM.Currency (PriceListCuryID=CuryID)
PX.Objects.AP.Vendor.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AP.Vendor.AccountByPrepaymentAcctID -> PX.Objects.GL.Account
PX.Objects.AP.Vendor.AccountByDiscTakenAcctID -> PX.Objects.GL.Account
PX.Objects.AP.Vendor.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.AP.Vendor.AccountByPrebookAcctID -> PX.Objects.GL.Account
PX.Objects.AP.Vendor.AccountBySalesTaxAcctID -> PX.Objects.GL.Account
PX.Objects.AP.Vendor.AccountByPurchTaxAcctID -> PX.Objects.GL.Account
PX.Objects.AP.Vendor.AccountByTaxExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.AP.Vendor.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.AP.Vendor.SubByDiscTakenSubID -> PX.Objects.GL.Sub
PX.Objects.AP.Vendor.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.AP.Vendor.SubByPrebookSubID -> PX.Objects.GL.Sub
PX.Objects.AP.Vendor.SubBySalesTaxSubID -> PX.Objects.GL.Sub
PX.Objects.AP.Vendor.SubByPurchTaxSubID -> PX.Objects.GL.Sub
PX.Objects.AP.Vendor.SubByTaxExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.AP.Vendor.VendorClassByVendorClassID -> PX.Objects.AP.VendorClass (VendorClassID=VendorClassID)
PX.Objects.AP.Vendor.AP1099BoxByBox1099 -> PX.Objects.AP.AP1099Box (Box1099=BoxNbr)
PX.Objects.AP.Vendor.BAccountByAcctCD -> PX.Objects.CA.Light.BAccount (AcctCD=AcctCD)
PX.Objects.AP.Vendor.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.AP.Vendor.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.AP.Vendor.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.AP.Vendor.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.AP.Vendor.PRBatchEmployeeCollection -> Collection(PX.Objects.PR.PRBatchEmployee)
PX.Objects.AP.Vendor.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.AP.Vendor.PRAcaEmployeeMonthlyInformationCollection -> Collection(PX.Objects.PR.PRAcaEmployeeMonthlyInformation)
PX.Objects.AP.Vendor.PREmployeeAttributeCollection -> Collection(PX.Objects.PR.PREmployeeAttribute)
PX.Objects.AP.Vendor.PREmployeeDirectDepositCollection -> Collection(PX.Objects.PR.PREmployeeDirectDeposit)
PX.Objects.AP.Vendor.PREmployeeEarningCollection -> Collection(PX.Objects.PR.PREmployeeEarning)
PX.Objects.AP.Vendor.PREmployeePTOBankCollection -> Collection(PX.Objects.PR.PREmployeePTOBank)
PX.Objects.AP.Vendor.PREmployeeTaxCollection -> Collection(PX.Objects.PR.PREmployeeTax)
PX.Objects.AP.Vendor.PREmployeeTaxAttributeCollection -> Collection(PX.Objects.PR.PREmployeeTaxAttribute)
PX.Objects.AP.Vendor.PREmployeeTaxFormCollection -> Collection(PX.Objects.PR.PREmployeeTaxForm)
PX.Objects.AP.Vendor.PREmployeeTaxFormDataCollection -> Collection(PX.Objects.PR.PREmployeeTaxFormData)
PX.Objects.AP.Vendor.PREmployeeWorkLocationCollection -> Collection(PX.Objects.PR.PREmployeeWorkLocation)
PX.Objects.AP.Vendor.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.AP.Vendor.PRPaymentBatchExportDetailsCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportDetails)
PX.Objects.AP.Vendor.PRPTOAdjustmentDetailCollection -> Collection(PX.Objects.PR.PRPTOAdjustmentDetail)
PX.Objects.AP.Vendor.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.AP.Vendor.PRRecordOfEmploymentCollection -> Collection(PX.Objects.PR.PRRecordOfEmployment)
PX.Objects.AP.Vendor.PRPeriodTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPeriodTaxApplicableAmounts)
PX.Objects.AP.Vendor.PRPeriodTaxesCollection -> Collection(PX.Objects.PR.PRPeriodTaxes)
PX.Objects.AP.Vendor.PRYtdDeductionsCollection -> Collection(PX.Objects.PR.PRYtdDeductions)
PX.Objects.AP.Vendor.PRYtdEarningsCollection -> Collection(PX.Objects.PR.PRYtdEarnings)
PX.Objects.AP.Vendor.PRYtdTaxesCollection -> Collection(PX.Objects.PR.PRYtdTaxes)
PX.Objects.AP.Vendor.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.AP.Vendor.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.AP.Vendor.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.AP.Vendor.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.AP.Vendor.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.AP.Vendor.EPTimeCardCollection -> Collection(PX.Objects.EP.EPTimeCard)
PX.Objects.AP.Vendor.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.AP.Vendor.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.AP.Vendor.FSEmployeeSkillCollection -> Collection(PX.Objects.SV.FSEmployeeSkill)
PX.Objects.AP.Vendor.EPWingmanCollection -> Collection(PX.Objects.EP.EPWingman)
PX.Objects.AP.Vendor.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.Objects.AP.Vendor.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.AP.Vendor.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.AP.Vendor.CABankFeedCorpCardCollection -> Collection(PX.Objects.CA.CABankFeedCorpCard)
PX.Objects.AP.Vendor.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.AP.Vendor.EPEmployeeContractCollection -> Collection(PX.Objects.EP.EPEmployeeContract)
PX.Objects.AP.Vendor.EPEmployeePositionCollection -> Collection(PX.Objects.EP.EPEmployeePosition)
PX.Objects.AP.Vendor.EPTimeActivitiesSummaryCollection -> Collection(PX.Objects.EP.EPTimeActivitiesSummary)
PX.Objects.AP.Vendor.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.AP.Vendor.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.AP.Vendor.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.AP.Vendor.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.AP.Vendor.AMSFKRecentActivityCollection -> Collection(PX.Objects.AM.SFK.AMSFKRecentActivity)
PX.Objects.AP.Vendor.FSRouteDocumentCollection -> Collection(PX.Objects.FS.FSRouteDocument)
PX.Objects.AP.Vendor.FSRouteEmployeeCollection -> Collection(PX.Objects.FS.FSRouteEmployee)
PX.Objects.AP.Vendor.SVMyDayReportCollection -> Collection(PX.Objects.SV.SVMyDayReport)
PX.Objects.AP.Vendor.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.AP.Vendor.EMailSyncAccountPreferencesCollection -> Collection(PX.SM.EMailSyncAccountPreferences)
PX.Objects.AP.Vendor.EPEmployeeCorpCardLinkCollection -> Collection(PX.Objects.EP.DAC.EPEmployeeCorpCardLink)
PX.Objects.AP.Vendor.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.AP.Vendor.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.AP.Vendor.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.Objects.AP.Vendor.ARContactCollection -> Collection(PX.Objects.AR.ARContact)
PX.Objects.AP.Vendor.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.AP.Vendor.DailyFieldReportSubcontractorActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity)
PX.Objects.AP.Vendor.APDiscountCollection -> Collection(PX.Objects.AP.APDiscount)
PX.Objects.AP.Vendor.AP1099HistoryCollection -> Collection(PX.Objects.AP.AP1099History)
PX.Objects.AP.Vendor.TaxBucketCollection -> Collection(PX.Objects.TX.TaxBucket)
PX.Objects.AP.Vendor.TaxBucketLineCollection -> Collection(PX.Objects.TX.TaxBucketLine)
PX.Objects.AP.Vendor.TaxReportLineCollection -> Collection(PX.Objects.TX.TaxReportLine)
PX.Objects.AP.Vendor.TaxRevCollection -> Collection(PX.Objects.TX.TaxRev)
PX.Objects.AP.Vendor.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.AP.Vendor.APAddressCollection -> Collection(PX.Objects.AP.APAddress)
PX.Objects.AP.Vendor.APContactCollection -> Collection(PX.Objects.AP.APContact)
PX.Objects.AP.Vendor.APDiscountLocationCollection -> Collection(PX.Objects.AP.APDiscountLocation)
PX.Objects.AP.Vendor.APDiscountVendorCollection -> Collection(PX.Objects.AP.APDiscountVendor)
PX.Objects.AP.Vendor.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.AP.Vendor.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.AP.Vendor.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.AP.Vendor.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.AP.Vendor.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.AP.Vendor.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.AP.Vendor.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.AP.Vendor.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.AP.Vendor.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.AP.Vendor.TaxHistorySumCollection -> Collection(PX.Objects.TX.TaxHistorySum)
PX.Objects.AP.Vendor.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.AP.Vendor.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.AP.Vendor.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.AP.Vendor.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.AP.Vendor.SVVendorLicenseCollection -> Collection(PX.Objects.SV.SVVendorLicense)
PX.Objects.AP.Vendor.SVVendorSkillCollection -> Collection(PX.Objects.SV.SVVendorSkill)
PX.Objects.AP.Vendor.CISHistoryCollection -> Collection(PX.Objects.Localizations.GB.CISHistory)
PX.Objects.AP.Vendor.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.AP.Vendor.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)

# PX.Objects.AP.VendorClass (EntityType)

Label: "Vendor Class"
Key: VendorClassID
Entity sets: PX_Objects_AP_VendorClass, VendorClass
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.AP.VendorClass.VendorClassID : Edm.String [key] "Class ID"
PX.Objects.AP.VendorClass.Descr : Edm.String "Description"
PX.Objects.AP.VendorClass.TermsID : Edm.String "Terms"
PX.Objects.AP.VendorClass.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AP.VendorClass.PaymentByType : Edm.Int32 [required] "Payment By"
PX.Objects.AP.VendorClass.CuryID : Edm.String "Currency ID"
PX.Objects.AP.VendorClass.CuryRateTypeID : Edm.String "Curr. Rate Type"
PX.Objects.AP.VendorClass.AllowOverrideCury : Edm.Boolean [required] "Enable Currency Override"
PX.Objects.AP.VendorClass.AllowOverrideRate : Edm.Boolean [required] "Enable Rate Override"
PX.Objects.AP.VendorClass.TaxZoneID : Edm.String "Tax Zone ID"
PX.Objects.AP.VendorClass.RequireTaxZone : Edm.Boolean [required] "Require Tax Zone"
PX.Objects.AP.VendorClass.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.AP.VendorClass.CountryID : Edm.String "Country"
PX.Objects.AP.VendorClass.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.AP.VendorClass.RcptQtyAction : Edm.String "Receipt Action"
PX.Objects.AP.VendorClass.PrintPO : Edm.Boolean [required] "Print Orders"
PX.Objects.AP.VendorClass.EmailPO : Edm.Boolean [required] "Send Orders by Email"
PX.Objects.AP.VendorClass.DefaultLocationCDFromBranch : Edm.Boolean [required] "Default Location ID from Branch"
PX.Objects.AP.VendorClass.LocaleName : Edm.String "Locale"
PX.Objects.AP.VendorClass.NoteID : Edm.Guid
PX.Objects.AP.VendorClass.NoteText : Edm.String "Note Text"
PX.Objects.AP.VendorClass.GroupMask : Edm.Binary "Default Restriction Group"
PX.Objects.AP.VendorClass.tstamp : Edm.Binary
PX.Objects.AP.VendorClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.VendorClass.CreatedByScreenID : Edm.String
PX.Objects.AP.VendorClass.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AP.VendorClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.VendorClass.LastModifiedByScreenID : Edm.String
PX.Objects.AP.VendorClass.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AP.VendorClass.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AP.VendorClass.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.AP.VendorClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.VendorClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.VendorClass.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.AP.VendorClass.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.AP.VendorClass.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.AP.VendorClass.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AP.VendorClass.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AP.VendorClass.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.AP.VendorClass.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType (CuryRateTypeID=CuryRateTypeID)
PX.Objects.AP.VendorClass.AccountByAPAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByPrepaymentAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByDiscountAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByDiscTakenAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByFreightAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByPrebookAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByUnrealizedGainAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByUnrealizedLossAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.AP.VendorClass.SubByAPSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByDiscTakenSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByFreightSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByPrebookSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByUnrealizedGainSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByUnrealizedLossSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.AP.VendorClass.CashAccountByCashAcctID -> PX.Objects.CA.CashAccount
PX.Objects.AP.VendorClass.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AP.VendorClass.RelationGroupByGroupMask -> PX.SM.RelationGroup (GroupMask=GroupMask)
PX.Objects.AP.VendorClass.LocaleByLocaleName -> PX.SM.Locale (LocaleName=LocaleName)
PX.Objects.AP.VendorClass.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.AP.VendorClass.INReplenishmentItemCollection -> Collection(PX.Objects.IN.INReplenishmentItem)
PX.Objects.AP.VendorClass.LienWaiverRecipientCollection -> Collection(PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient)
PX.Objects.AP.VendorClass.APSetupCollection -> Collection(PX.Objects.AP.APSetup)

# PX.Objects.AP.VendorDiscountSequence (EntityType)

Label: "Discount Sequence"
BaseType: PX.Objects.AR.DiscountSequence
Key: DiscountID, DiscountSequenceID (inherited from PX.Objects.AR.DiscountSequence)
Entity sets: PX_Objects_AP_VendorDiscountSequence

PX.Objects.AP.VendorDiscountSequence.VendorID : Edm.Int32 "Vendor"
PX.Objects.AP.VendorDiscountSequence.APDiscountByVendorID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID, VendorID=BAccountID)
PX.Objects.AP.VendorDiscountSequence.APDiscountByDiscountID -> PX.Objects.AP.APDiscount (DiscountID=DiscountID)
PX.Objects.AP.VendorDiscountSequence.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.AP.VendorDiscountSequence.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.AP.VendorDiscountSequence.APDiscountLocationCollection -> Collection(PX.Objects.AP.APDiscountLocation)
PX.Objects.AP.VendorDiscountSequence.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.AP.VendorDiscountSequence.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.AP.VendorDiscountSequence.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.AP.VendorDiscountSequence.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)

# PX.Objects.AP.VendorPaymentMethodDetail (EntityType)

Label: "Payment Type Detail"
Key: BAccountID, DetailID, LocationID, PaymentMethodID
Entity sets: PX_Objects_AP_VendorPaymentMethodDetail, PaymentTypeDetail, VendorPaymentMethodDetail

PX.Objects.AP.VendorPaymentMethodDetail.BAccountID : Edm.Int32 [key] "BAccountID"
PX.Objects.AP.VendorPaymentMethodDetail.LocationID : Edm.Int32 [key] "LocationID"
PX.Objects.AP.VendorPaymentMethodDetail.PaymentMethodID : Edm.String [key] "Payment Method"
PX.Objects.AP.VendorPaymentMethodDetail.DetailID : Edm.String [key] "ID"
PX.Objects.AP.VendorPaymentMethodDetail.DetailValue : Edm.String "Value"
PX.Objects.AP.VendorPaymentMethodDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AP.VendorPaymentMethodDetail.CreatedByScreenID : Edm.String
PX.Objects.AP.VendorPaymentMethodDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AP.VendorPaymentMethodDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AP.VendorPaymentMethodDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AP.VendorPaymentMethodDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AP.VendorPaymentMethodDetail.tstamp : Edm.Binary
PX.Objects.AP.VendorPaymentMethodDetail.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AP.VendorPaymentMethodDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AP.VendorPaymentMethodDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AP.VendorPaymentMethodDetail.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AP.VendorPaymentMethodDetail.PaymentMethodDetailByPaymentMethodID -> PX.Objects.CA.PaymentMethodDetail (DetailID=DetailID, PaymentMethodID=PaymentMethodID)
PX.Objects.AP.VendorPaymentMethodDetail.PaymentMethodDetailByDetailID -> PX.Objects.CA.PaymentMethodDetail (PaymentMethodID=PaymentMethodID, DetailID=DetailID)
PX.Objects.AP.VendorPaymentMethodDetail.LocationByLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID, LocationID=LocationID)

# PX.Objects.AP.VendorR (EntityType)

Label: "Vendor"
BaseType: PX.Objects.AP.Vendor
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_AP_VendorR, Vendor1, VendorR

# PX.Objects.AR.ARAddItemSelected (EntityType)

Key: InventoryID
Entity sets: PX_Objects_AR_ARAddItemSelected
Non-filterable, non-selectable: CuryID, CuryInfoID, CuryUnitPrice, CuryRate, CuryViewState

PX.Objects.AR.ARAddItemSelected.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AR.ARAddItemSelected.InventoryCD : Edm.String "Inventory ID"
PX.Objects.AR.ARAddItemSelected.Descr : Edm.String "Description"
PX.Objects.AR.ARAddItemSelected.ItemClassID : Edm.Int32 "Item Class ID"
PX.Objects.AR.ARAddItemSelected.ItemClassCD : Edm.String
PX.Objects.AR.ARAddItemSelected.ItemClassDescription : Edm.String "Item Class Description"
PX.Objects.AR.ARAddItemSelected.PriceClassID : Edm.String "Price Class ID"
PX.Objects.AR.ARAddItemSelected.PriceClassDescription : Edm.String "Price Class Description"
PX.Objects.AR.ARAddItemSelected.BaseUnit : Edm.String "Base Unit"
PX.Objects.AR.ARAddItemSelected.CuryID : Edm.String "Currency"
PX.Objects.AR.ARAddItemSelected.CuryInfoID : Edm.Int64
PX.Objects.AR.ARAddItemSelected.CuryUnitPrice : Edm.Decimal "Last Unit Price"
PX.Objects.AR.ARAddItemSelected.PriceWorkgroupID : Edm.Int32 "Price Workgroup"
PX.Objects.AR.ARAddItemSelected.PriceManagerID : Edm.Int32 "Price Manager"
PX.Objects.AR.ARAddItemSelected.NoteID : Edm.Guid
PX.Objects.AR.ARAddItemSelected.CuryRate : Edm.Decimal
PX.Objects.AR.ARAddItemSelected.CuryViewState : Edm.Boolean
PX.Objects.AR.ARAddItemSelected.EPCompanyTreeByPriceWorkgroupID -> PX.TM.EPCompanyTree (PriceWorkgroupID=WorkGroupID)
PX.Objects.AR.ARAddItemSelected.INItemClassByItemClassID -> PX.Objects.IN.INItemClass (ItemClassID=ItemClassID)
PX.Objects.AR.ARAddItemSelected.EPCompanyTreeByProductWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.AR.ARAddItemSelected.INPriceClassByPriceClassID -> PX.Objects.IN.INPriceClass (PriceClassID=PriceClassID)
PX.Objects.AR.ARAddItemSelected.CSAnswersByNoteID -> PX.Objects.CS.CSAnswers (NoteID=RefNoteID)
PX.Objects.AR.ARAddItemSelected.POFixedDemandCollection -> Collection(PX.Objects.PO.POFixedDemand)

# PX.Objects.AR.ARAddress (EntityType)

Label: "AR Address"
Key: AddressID
Entity sets: PX_Objects_AR_ARAddress, ARAddress
Non-filterable, non-selectable: OverrideAddress

PX.Objects.AR.ARAddress.AddressID : Edm.Int32 [key] "Address ID"
PX.Objects.AR.ARAddress.CustomerID : Edm.Int32
PX.Objects.AR.ARAddress.CustomerAddressID : Edm.Int32
PX.Objects.AR.ARAddress.IsDefaultBillAddress : Edm.Boolean [required] "Customer Default"
PX.Objects.AR.ARAddress.OverrideAddress : Edm.Boolean "Override Address"
PX.Objects.AR.ARAddress.IsEncrypted : Edm.Boolean
PX.Objects.AR.ARAddress.RevisionID : Edm.Int32 [required]
PX.Objects.AR.ARAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.AR.ARAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.AR.ARAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.AR.ARAddress.City : Edm.String "City"
PX.Objects.AR.ARAddress.CountryID : Edm.String "Country"
PX.Objects.AR.ARAddress.State : Edm.String "State"
PX.Objects.AR.ARAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.AR.ARAddress.Department : Edm.String "Department"
PX.Objects.AR.ARAddress.SubDepartment : Edm.String "Subdepartment"
PX.Objects.AR.ARAddress.StreetName : Edm.String "Street Name"
PX.Objects.AR.ARAddress.BuildingNumber : Edm.String "Building Number"
PX.Objects.AR.ARAddress.BuildingName : Edm.String "Building Name"
PX.Objects.AR.ARAddress.Floor : Edm.String "Floor"
PX.Objects.AR.ARAddress.UnitNumber : Edm.String "Unit Number"
PX.Objects.AR.ARAddress.PostBox : Edm.String "Post Box"
PX.Objects.AR.ARAddress.Room : Edm.String "Room"
PX.Objects.AR.ARAddress.TownLocationName : Edm.String "Town Location Name"
PX.Objects.AR.ARAddress.DistrictName : Edm.String "District Name"
PX.Objects.AR.ARAddress.AddressType : Edm.String "Address Type"
PX.Objects.AR.ARAddress.CareOf : Edm.String "Care Of"
PX.Objects.AR.ARAddress.NoteID : Edm.Guid
PX.Objects.AR.ARAddress.tstamp : Edm.Binary
PX.Objects.AR.ARAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARAddress.CreatedByScreenID : Edm.String
PX.Objects.AR.ARAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARAddress.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARAddress.Latitude : Edm.Decimal "Latitude"
PX.Objects.AR.ARAddress.Longitude : Edm.Decimal "Longitude"
PX.Objects.AR.ARAddress.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARAddress.AddressByCustomerAddressID -> PX.Objects.CR.Address (CustomerAddressID=AddressID)
PX.Objects.AR.ARAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.AR.ARAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.AR.ARAddress.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.ARAddress.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)

# PX.Objects.AR.ARAdjust (EntityType)

Label: "Applications"
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr
Entity sets: PX_Objects_AR_ARAdjust, Applications, ARAdjust
Non-filterable, non-selectable: AdjType, PrintAdjgDocType, AdjdCuryID, PrintAdjdDocType, HistoryAdjdDocType, DisplayDocType, CuryRGOLAmt, DisplayRGOLAmt, NoteText, CuryOrigDocAmt, OrigDocAmt, CuryDocBal, CuryAdjustedDocBal, AdjustedDocBal, DocBal, CuryDiscBal, CuryAdjustedDiscBal, DiscBal, CuryWOBal, CuryAdjustedWOBal, WOBal, VoidAppl, ReverseGainLoss, PPDVATAdjDescription, DisplayRefNbr, DisplayBranchID, DisplayCustomerID, DisplayDocDate, DisplayDocDesc, DisplayCuryID, DisplayFinPeriodID, DisplayStatus, DisplayCuryInfoID, DisplayAdjAmt, DisplayCuryAmt, DisplayCuryPPDAmt, DisplayCuryWOAmt, DisplayProcStatus

PX.Objects.AR.ARAdjust.CustomerID : Edm.Int32 "CustomerID"
PX.Objects.AR.ARAdjust.AdjdCustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARAdjust.AdjType : Edm.String
PX.Objects.AR.ARAdjust.AdjgDocType : Edm.String [key] "AdjgDocType"
PX.Objects.AR.ARAdjust.PrintAdjgDocType : Edm.String "Type"
PX.Objects.AR.ARAdjust.AdjgRefNbr : Edm.String [key] "AdjgRefNbr"
PX.Objects.AR.ARAdjust.AdjgBranchID : Edm.Int32 "Branch"
PX.Objects.AR.ARAdjust.AdjdCuryInfoID : Edm.Int64
PX.Objects.AR.ARAdjust.AdjdCuryID : Edm.String "Currency"
PX.Objects.AR.ARAdjust.AdjdDocType : Edm.String [key required] "Doc. Type"
PX.Objects.AR.ARAdjust.PrintAdjdDocType : Edm.String "Type"
PX.Objects.AR.ARAdjust.HistoryAdjdDocType : Edm.String "Type"
PX.Objects.AR.ARAdjust.DisplayDocType : Edm.String "Doc. Type"
PX.Objects.AR.ARAdjust.AdjdRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARAdjust.AdjdLineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AR.ARAdjust.AdjdOrderType : Edm.String "Order Type"
PX.Objects.AR.ARAdjust.AdjdOrderNbr : Edm.String "Order Nbr."
PX.Objects.AR.ARAdjust.AdjNbr : Edm.Int32 [key] "Adjustment Nbr."
PX.Objects.AR.ARAdjust.AdjBatchNbr : Edm.String "Batch Number"
PX.Objects.AR.ARAdjust.VoidAdjNbr : Edm.Int32
PX.Objects.AR.ARAdjust.AdjdOrigCuryInfoID : Edm.Int64
PX.Objects.AR.ARAdjust.AdjgCuryInfoID : Edm.Int64
PX.Objects.AR.ARAdjust.AdjgDocDate : Edm.DateTimeOffset
PX.Objects.AR.ARAdjust.AdjgFinPeriodID : Edm.String "Application Period"
PX.Objects.AR.ARAdjust.AdjgTranPeriodID : Edm.String
PX.Objects.AR.ARAdjust.AdjdDocDate : Edm.DateTimeOffset "Date"
PX.Objects.AR.ARAdjust.AdjdFinPeriodID : Edm.String "Post Period"
PX.Objects.AR.ARAdjust.AdjdTranPeriodID : Edm.String
PX.Objects.AR.ARAdjust.CuryAdjgDiscAmt : Edm.Decimal "Cash Discount Taken in Payment Currency"
PX.Objects.AR.ARAdjust.CuryAdjgPPDAmt : Edm.Decimal "Cash Discount Taken in Payment Currency"
PX.Objects.AR.ARAdjust.CuryAdjgWOAmt : Edm.Decimal [required] "Write-Off Amount in Payment Currency"
PX.Objects.AR.ARAdjust.CuryAdjgAmt : Edm.Decimal "Amount Paid in Payment Currency"
PX.Objects.AR.ARAdjust.CuryAdjgSignedAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.AdjDiscAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.AdjPPDAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.CuryAdjdDiscAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AR.ARAdjust.CuryAdjdPPDAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AR.ARAdjust.AdjWOAmt : Edm.Decimal [required]
PX.Objects.AR.ARAdjust.CuryAdjdWOAmt : Edm.Decimal [required] "Write-Off Amount"
PX.Objects.AR.ARAdjust.AdjAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.AdjSignedAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.CuryAdjdAmt : Edm.Decimal "Amount Paid"
PX.Objects.AR.ARAdjust.CuryAdjdOrigAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.CuryRGOLAmt : Edm.Decimal "RGOL Amount"
PX.Objects.AR.ARAdjust.DisplayRGOLAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.RGOLAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.Released : Edm.Boolean [required]
PX.Objects.AR.ARAdjust.Hold : Edm.Boolean [required]
PX.Objects.AR.ARAdjust.Voided : Edm.Boolean [required]
PX.Objects.AR.ARAdjust.tstamp : Edm.Binary
PX.Objects.AR.ARAdjust.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARAdjust.CreatedByScreenID : Edm.String
PX.Objects.AR.ARAdjust.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARAdjust.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARAdjust.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARAdjust.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARAdjust.NoteID : Edm.Guid
PX.Objects.AR.ARAdjust.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARAdjust.InvoiceID : Edm.Guid
PX.Objects.AR.ARAdjust.PaymentID : Edm.Guid
PX.Objects.AR.ARAdjust.MemoID : Edm.Guid
PX.Objects.AR.ARAdjust.CuryOrigDocAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.OrigDocAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.CuryDocBal : Edm.Decimal "Balance"
PX.Objects.AR.ARAdjust.CuryAdjustedDocBal : Edm.Decimal "Balance"
PX.Objects.AR.ARAdjust.AdjustedDocBal : Edm.Decimal
PX.Objects.AR.ARAdjust.DocBal : Edm.Decimal
PX.Objects.AR.ARAdjust.CuryDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.AR.ARAdjust.CuryAdjustedDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.AR.ARAdjust.DiscBal : Edm.Decimal
PX.Objects.AR.ARAdjust.CuryWOBal : Edm.Decimal "Write-Off Limit"
PX.Objects.AR.ARAdjust.CuryAdjustedWOBal : Edm.Decimal "Write-Off Limit"
PX.Objects.AR.ARAdjust.WOBal : Edm.Decimal
PX.Objects.AR.ARAdjust.WriteOffReasonCode : Edm.String "Write-Off Reason Code"
PX.Objects.AR.ARAdjust.VoidAppl : Edm.Boolean "Void Application"
PX.Objects.AR.ARAdjust.ReverseGainLoss : Edm.Boolean
PX.Objects.AR.ARAdjust.PPDVATAdjRefNbr : Edm.String "Tax Adjustment"
PX.Objects.AR.ARAdjust.PPDVATAdjDocType : Edm.String
PX.Objects.AR.ARAdjust.PPDVATAdjDescription : Edm.String "Tax Adjustment"
PX.Objects.AR.ARAdjust.AdjdHasPPDTaxes : Edm.Boolean
PX.Objects.AR.ARAdjust.PendingPPD : Edm.Boolean [required] "Subject to Tax Adjustment"
PX.Objects.AR.ARAdjust.StatementDate : Edm.DateTimeOffset
PX.Objects.AR.ARAdjust.TaxInvoiceNbr : Edm.String "Tax Doc. Nbr"
PX.Objects.AR.ARAdjust.IsMigratedRecord : Edm.Boolean
PX.Objects.AR.ARAdjust.IsInitialApplication : Edm.Boolean [required]
PX.Objects.AR.ARAdjust.IsCCPayment : Edm.Boolean
PX.Objects.AR.ARAdjust.PaymentPendingProcessing : Edm.Boolean
PX.Objects.AR.ARAdjust.PaymentReleased : Edm.Boolean
PX.Objects.AR.ARAdjust.IsCCAuthorized : Edm.Boolean
PX.Objects.AR.ARAdjust.IsCCCaptured : Edm.Boolean
PX.Objects.AR.ARAdjust.PaymentCaptureFailed : Edm.Boolean
PX.Objects.AR.ARAdjust.Recalculatable : Edm.Boolean [required]
PX.Objects.AR.ARAdjust.DisplayRefNbr : Edm.String "Reference Nbr."
PX.Objects.AR.ARAdjust.DisplayBranchID : Edm.Int32 "BranchID"
PX.Objects.AR.ARAdjust.DisplayCustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARAdjust.DisplayDocDate : Edm.DateTimeOffset "Date"
PX.Objects.AR.ARAdjust.DisplayDocDesc : Edm.String "Description"
PX.Objects.AR.ARAdjust.DisplayCuryID : Edm.String "Currency"
PX.Objects.AR.ARAdjust.DisplayFinPeriodID : Edm.String "Post Period"
PX.Objects.AR.ARAdjust.DisplayStatus : Edm.String "Status"
PX.Objects.AR.ARAdjust.DisplayCuryInfoID : Edm.Int64
PX.Objects.AR.ARAdjust.DisplayAdjAmt : Edm.Decimal
PX.Objects.AR.ARAdjust.DisplayCuryAmt : Edm.Decimal "Amount Paid"
PX.Objects.AR.ARAdjust.DisplayCuryPPDAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AR.ARAdjust.DisplayCuryWOAmt : Edm.Decimal "Write-Off Amount"
PX.Objects.AR.ARAdjust.DisplayProcStatus : Edm.String "Proc. Status"
PX.Objects.AR.ARAdjust.ARInvoiceByPPDVATAdjRefNbr -> PX.Objects.AR.ARInvoice (PPDVATAdjRefNbr=RefNbr)
PX.Objects.AR.ARAdjust.ARInvoiceByAdjdRefNbr -> PX.Objects.AR.ARInvoice (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.AR.ARAdjust.BAccountByAdjdCustomerID -> PX.Objects.CR.BAccount (AdjdCustomerID=BAccountID)
PX.Objects.AR.ARAdjust.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARAdjust.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARAdjust.CustomerByAdjdCustomerID -> PX.Objects.AR.Customer (AdjdCustomerID=BAccountID)
PX.Objects.AR.ARAdjust.BatchByAdjBatchNbr -> PX.Objects.GL.Batch (AdjBatchNbr=BatchNbr)
PX.Objects.AR.ARAdjust.ARPaymentByAdjgDocType -> PX.Objects.AR.ARPayment (AdjgRefNbr=RefNbr, AdjgDocType=DocType)
PX.Objects.AR.ARAdjust.ARPaymentByAdjgRefNbr -> PX.Objects.AR.ARPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.AR.ARAdjust.SOOrderByAdjdOrderNbr -> PX.Objects.SO.SOOrder (AdjdOrderType=OrderType, AdjdOrderNbr=OrderNbr)
PX.Objects.AR.ARAdjust.SOOrderByAdjdOrderType -> PX.Objects.SO.SOOrder (AdjdOrderNbr=OrderNbr, AdjdOrderType=OrderType)
PX.Objects.AR.ARAdjust.ARRegisterByAdjgRefNbr -> PX.Objects.AR.ARRegister (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.AR.ARAdjust.ARRegisterByAdjdRefNbr -> PX.Objects.AR.ARRegister (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.AR.ARAdjust.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (AdjdRefNbr=RefNbr, AdjdDocType=DocType)
PX.Objects.AR.ARAdjust.BranchByAdjgBranchID -> PX.Objects.GL.Branch (AdjgBranchID=BranchID)
PX.Objects.AR.ARAdjust.BranchByAdjdBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARAdjust.CurrencyInfoByAdjgCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjgCuryInfoID=CuryInfoID)
PX.Objects.AR.ARAdjust.CurrencyInfoByAdjdCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdCuryInfoID=CuryInfoID)
PX.Objects.AR.ARAdjust.CurrencyInfoByAdjdOrigCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdOrigCuryInfoID=CuryInfoID)
PX.Objects.AR.ARAdjust.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARAdjust.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARAdjust.SOAdjustByAdjgRefNbr -> PX.Objects.SO.SOAdjust (AdjdOrderType=AdjdOrderType, AdjdOrderNbr=AdjdOrderNbr, AdjgDocType=AdjgDocType, AdjgRefNbr=AdjgRefNbr)
PX.Objects.AR.ARAdjust.SOOrderTypeByAdjdOrderType -> PX.Objects.SO.SOOrderType (AdjdOrderType=OrderType)
PX.Objects.AR.ARAdjust.ReasonCodeByWriteOffReasonCode -> PX.Objects.CS.ReasonCode (WriteOffReasonCode=ReasonCodeID)
PX.Objects.AR.ARAdjust.AccountByAdjdARAcct -> PX.Objects.GL.Account
PX.Objects.AR.ARAdjust.SubByAdjdARSub -> PX.Objects.GL.Sub
PX.Objects.AR.ARAdjust.ARPaymentTotalsByAdjgRefNbr -> PX.Objects.AR.ARPaymentTotals (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.AR.ARAdjust.ARTranByAdjdRefNbr -> PX.Objects.AR.ARTran (AdjdLineNbr=LineNbr, AdjdDocType=TranType, AdjdRefNbr=RefNbr)

# PX.Objects.AR.ARAdjust2 (EntityType)

Label: "Applications"
BaseType: PX.Objects.AR.ARAdjust
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr (inherited from PX.Objects.AR.ARAdjust)
Entity sets: PX_Objects_AR_ARAdjust2, Applications1, ARAdjust2

PX.Objects.AR.ARAdjust2.AdjdBranchID : Edm.Int32 "Branch"

# PX.Objects.AR.ARAdjustedBalanceAtDate (EntityType)

Label: "ARAdjustedBalanceAtDate"
Key: DocType, RefNbr, SubmissionDate
Entity sets: PX_Objects_AR_ARAdjustedBalanceAtDate, ARAdjustedBalanceAtDate
Non-filterable, non-selectable: CuryLineTotal

PX.Objects.AR.ARAdjustedBalanceAtDate.DocType : Edm.String [key]
PX.Objects.AR.ARAdjustedBalanceAtDate.RefNbr : Edm.String [key]
PX.Objects.AR.ARAdjustedBalanceAtDate.SubmissionDate : Edm.DateTimeOffset [key]
PX.Objects.AR.ARAdjustedBalanceAtDate.LineTotal : Edm.Decimal
PX.Objects.AR.ARAdjustedBalanceAtDate.CuryLineTotal : Edm.Decimal
PX.Objects.AR.ARAdjustedBalanceAtDate.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.ARAdjustedBalanceAtDate.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.AR.ARAdjustedBalanceAtDate.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.AR.ARAdjustedBalanceAtDate.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.AR.ARAdjustedBalanceAtDate.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.AR.ARAdjustedBalanceAtDate.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.AR.ARAdjustedBalanceAtDate.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.AR.ARAdjustedBalanceAtDate.ARTranAccrueCostCollection -> Collection(PX.Objects.AR.ARTranAccrueCost)

# PX.Objects.AR.ARAdjustingBalanceAtDate (EntityType)

Label: "ARAdjustingBalanceAtDate"
Key: DocType, RefNbr, SubmissionDate
Entity sets: PX_Objects_AR_ARAdjustingBalanceAtDate, ARAdjustingBalanceAtDate
Non-filterable, non-selectable: CuryLineTotal

PX.Objects.AR.ARAdjustingBalanceAtDate.DocType : Edm.String [key]
PX.Objects.AR.ARAdjustingBalanceAtDate.RefNbr : Edm.String [key]
PX.Objects.AR.ARAdjustingBalanceAtDate.SubmissionDate : Edm.DateTimeOffset [key]
PX.Objects.AR.ARAdjustingBalanceAtDate.LineTotal : Edm.Decimal
PX.Objects.AR.ARAdjustingBalanceAtDate.CuryLineTotal : Edm.Decimal
PX.Objects.AR.ARAdjustingBalanceAtDate.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.ARAdjustingBalanceAtDate.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.AR.ARAdjustingBalanceAtDate.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.AR.ARAdjustingBalanceAtDate.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.AR.ARAdjustingBalanceAtDate.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.AR.ARAdjustingBalanceAtDate.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.AR.ARAdjustingBalanceAtDate.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.AR.ARAdjustingBalanceAtDate.ARTranAccrueCostCollection -> Collection(PX.Objects.AR.ARTranAccrueCost)

# PX.Objects.AR.ARAdjustReport (EntityType)

Label: "Applications"
BaseType: PX.Objects.AR.ARAdjust
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr (inherited from PX.Objects.AR.ARAdjust)
Entity sets: PX_Objects_AR_ARAdjustReport, Applications2, ARAdjustReport

PX.Objects.AR.ARAdjustReport.LineTotalAdjusted : Edm.Decimal
PX.Objects.AR.ARAdjustReport.CuryLineTotalAdjusted : Edm.Decimal
PX.Objects.AR.ARAdjustReport.LineTotalAdjusting : Edm.Decimal
PX.Objects.AR.ARAdjustReport.CuryLineTotalAdjusting : Edm.Decimal

# PX.Objects.AR.ARBalances (EntityType)

Label: "AR Balance"
Key: BranchID, CustomerID, CustomerLocationID
Entity sets: PX_Objects_AR_ARBalances, ARBalance, ARBalances
Non-filterable, non-selectable: DatesUpdated

PX.Objects.AR.ARBalances.BranchID : Edm.Int32 [key]
PX.Objects.AR.ARBalances.CustomerID : Edm.Int32 [key]
PX.Objects.AR.ARBalances.CustomerLocationID : Edm.Int32 [key]
PX.Objects.AR.ARBalances.CuryID : Edm.String
PX.Objects.AR.ARBalances.CurrentBal : Edm.Decimal [required]
PX.Objects.AR.ARBalances.UnreleasedBal : Edm.Decimal [required]
PX.Objects.AR.ARBalances.TotalPrepayments : Edm.Decimal [required]
PX.Objects.AR.ARBalances.TotalQuotations : Edm.Decimal [required]
PX.Objects.AR.ARBalances.TotalOpenOrders : Edm.Decimal [required]
PX.Objects.AR.ARBalances.TotalOpenWorkorders : Edm.Decimal [required]
PX.Objects.AR.ARBalances.TotalShipped : Edm.Decimal [required]
PX.Objects.AR.ARBalances.LastInvoiceDate : Edm.DateTimeOffset
PX.Objects.AR.ARBalances.OldInvoiceDate : Edm.DateTimeOffset
PX.Objects.AR.ARBalances.NumberInvoicePaid : Edm.Int32
PX.Objects.AR.ARBalances.PaidInvoiceDays : Edm.Int32
PX.Objects.AR.ARBalances.AverageDaysToPay : Edm.Int32
PX.Objects.AR.ARBalances.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARBalances.CreatedByScreenID : Edm.String
PX.Objects.AR.ARBalances.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARBalances.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARBalances.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARBalances.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARBalances.tstamp : Edm.Binary
PX.Objects.AR.ARBalances.DatesUpdated : Edm.Boolean
PX.Objects.AR.ARBalances.LastDocDate : Edm.DateTimeOffset
PX.Objects.AR.ARBalances.StatementRequired : Edm.Boolean [required]
PX.Objects.AR.ARBalances.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARBalances.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.ARBalances.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARBalances.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARBalances.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID, CustomerLocationID=LocationID)

# PX.Objects.AR.ARBalancesByBaseCuryID (EntityType)

Label: "AR Balance by Base Currency"
Key: BaseCuryID, CustomerID
Entity sets: PX_Objects_AR_ARBalancesByBaseCuryID, ARBalancebyBaseCurrency, ARBalancesByBaseCuryID

PX.Objects.AR.ARBalancesByBaseCuryID.CustomerID : Edm.Int32 [key]
PX.Objects.AR.ARBalancesByBaseCuryID.BaseCuryID : Edm.String [key] "Currency"
PX.Objects.AR.ARBalancesByBaseCuryID.CurrentBal : Edm.Decimal "Balance"
PX.Objects.AR.ARBalancesByBaseCuryID.TotalPrepayments : Edm.Decimal "Prepayment Balance"
PX.Objects.AR.ARBalancesByBaseCuryID.UnreleasedBal : Edm.Decimal "Unreleased Balance"
PX.Objects.AR.ARBalancesByBaseCuryID.ConsolidatedBalance : Edm.Decimal "Consolidated Balance"
PX.Objects.AR.ARBalancesByBaseCuryID.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARBalancesByBaseCuryID.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.AR.ARBalancesByBaseCuryID.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)

# PX.Objects.AR.ARBalancesSharedCredit (EntityType)

Label: "AR Balance Shared Credit"
Key: SharedCreditCustomerID
Entity sets: PX_Objects_AR_ARBalancesSharedCredit, ARBalanceSharedCredit, ARBalancesSharedCredit

PX.Objects.AR.ARBalancesSharedCredit.BranchID : Edm.Int32
PX.Objects.AR.ARBalancesSharedCredit.SharedCreditCustomerID : Edm.Int32 [key]
PX.Objects.AR.ARBalancesSharedCredit.CreditRule : Edm.String "Credit Verification"
PX.Objects.AR.ARBalancesSharedCredit.CreditLimit : Edm.Decimal "Credit Limit"
PX.Objects.AR.ARBalancesSharedCredit.CurrentBal : Edm.Decimal
PX.Objects.AR.ARBalancesSharedCredit.UnreleasedBal : Edm.Decimal
PX.Objects.AR.ARBalancesSharedCredit.TotalPrepayments : Edm.Decimal
PX.Objects.AR.ARBalancesSharedCredit.TotalOpenOrders : Edm.Decimal
PX.Objects.AR.ARBalancesSharedCredit.TotalShipped : Edm.Decimal
PX.Objects.AR.ARBalancesSharedCredit.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)

# PX.Objects.AR.ARContact (EntityType)

Label: "AR Contact"
Key: ContactID
Entity sets: PX_Objects_AR_ARContact, ARContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.AR.ARContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.AR.ARContact.CustomerID : Edm.Int32
PX.Objects.AR.ARContact.CustomerContactID : Edm.Int32
PX.Objects.AR.ARContact.IsDefaultContact : Edm.Boolean [required] "Default Customer Contact"
PX.Objects.AR.ARContact.OverrideContact : Edm.Boolean "Override Contact"
PX.Objects.AR.ARContact.IsEncrypted : Edm.Boolean
PX.Objects.AR.ARContact.RevisionID : Edm.Int32 [required]
PX.Objects.AR.ARContact.Title : Edm.String "Title"
PX.Objects.AR.ARContact.Salutation : Edm.String "Job Title"
PX.Objects.AR.ARContact.Attention : Edm.String "Attention"
PX.Objects.AR.ARContact.FullName : Edm.String "Account Name"
PX.Objects.AR.ARContact.Email : Edm.String "Email"
PX.Objects.AR.ARContact.Fax : Edm.String "Fax"
PX.Objects.AR.ARContact.FaxType : Edm.String "Fax"
PX.Objects.AR.ARContact.Phone1 : Edm.String "Phone 1"
PX.Objects.AR.ARContact.Phone1Type : Edm.String "Phone 1"
PX.Objects.AR.ARContact.Phone2 : Edm.String "Phone 2"
PX.Objects.AR.ARContact.Phone2Type : Edm.String "Phone 2"
PX.Objects.AR.ARContact.Phone3 : Edm.String "Phone 3"
PX.Objects.AR.ARContact.Phone3Type : Edm.String "Phone 3"
PX.Objects.AR.ARContact.NoteID : Edm.Guid
PX.Objects.AR.ARContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARContact.CreatedByScreenID : Edm.String
PX.Objects.AR.ARContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.ARContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARContact.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.ARContact.tstamp : Edm.Binary
PX.Objects.AR.ARContact.VendorByCustomerID -> PX.Objects.AP.Vendor (CustomerID=BAccountID)
PX.Objects.AR.ARContact.ContactByCustomerContactID -> PX.Objects.CR.Contact (CustomerContactID=ContactID)
PX.Objects.AR.ARContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARContact.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.ARContact.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.AR.ARContact.SOContactCollection -> Collection(PX.Objects.SO.SOContact)

# PX.Objects.AR.ARDiscount (EntityType)

Label: "AR Discount"
Key: DiscountID
Entity sets: PX_Objects_AR_ARDiscount, ARDiscount

PX.Objects.AR.ARDiscount.DiscountID : Edm.String [key] "Discount Code"
PX.Objects.AR.ARDiscount.Description : Edm.String "Description"
PX.Objects.AR.ARDiscount.Type : Edm.String "Discount Type"
PX.Objects.AR.ARDiscount.ApplicableTo : Edm.String "Applicable To"
PX.Objects.AR.ARDiscount.IsAppliedToDR : Edm.Boolean [required] "Apply to Deferred Revenue"
PX.Objects.AR.ARDiscount.IsManual : Edm.Boolean [required] "Manual"
PX.Objects.AR.ARDiscount.ExcludeFromDiscountableAmt : Edm.Boolean [required] "Exclude from Discountable Amount"
PX.Objects.AR.ARDiscount.SkipDocumentDiscounts : Edm.Boolean [required] "Skip Document Discounts"
PX.Objects.AR.ARDiscount.IsAutoNumber : Edm.Boolean [required] "Auto-Numbering"
PX.Objects.AR.ARDiscount.LastNumber : Edm.String "Last Number"
PX.Objects.AR.ARDiscount.tstamp : Edm.Binary
PX.Objects.AR.ARDiscount.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARDiscount.CreatedByScreenID : Edm.String
PX.Objects.AR.ARDiscount.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARDiscount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARDiscount.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARDiscount.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARDiscount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARDiscount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARDiscount.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.AR.ARDiscount.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.AR.ARDiscount.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.AR.ARDiscount.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.AR.ARDiscount.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.AR.ARDiscount.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.ARDiscount.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.AR.ARDiscount.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.AR.ARDiscount.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.AR.ARDiscount.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.AR.ARDiscount.ContractRenewalHistoryCollection -> Collection(PX.Objects.CT.ContractRenewalHistory)
PX.Objects.AR.ARDiscount.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.AR.ARDiscount.DiscountSequenceCollection -> Collection(PX.Objects.AR.DiscountSequence)
PX.Objects.AR.ARDiscount.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.AR.ARDiscount.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.AR.ARDiscount.SOMiscLine2Collection -> Collection(PX.Objects.SO.SOMiscLine2)

# PX.Objects.AR.ARDunningCustomerClass (EntityType)

Label: "AR Dunning Setup"
Key: CustomerClassID, DunningLetterLevel
Entity sets: PX_Objects_AR_ARDunningCustomerClass, ARDunningSetup, ARDunningCustomerClass
Non-filterable, non-selectable: NoteText

PX.Objects.AR.ARDunningCustomerClass.DunningLetterLevel : Edm.Int32 [key required] "Dunning Letter Level"
PX.Objects.AR.ARDunningCustomerClass.CustomerClassID : Edm.String [key]
PX.Objects.AR.ARDunningCustomerClass.DueDays : Edm.Int32 [required] "Days Past Due"
PX.Objects.AR.ARDunningCustomerClass.DaysToSettle : Edm.Int32 [required] "Days to Settle"
PX.Objects.AR.ARDunningCustomerClass.Descr : Edm.String "Description"
PX.Objects.AR.ARDunningCustomerClass.DunningFee : Edm.Decimal [required] "Dunning Fee"
PX.Objects.AR.ARDunningCustomerClass.NoteID : Edm.Guid
PX.Objects.AR.ARDunningCustomerClass.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARDunningCustomerClass.tstamp : Edm.Binary
PX.Objects.AR.ARDunningCustomerClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARDunningCustomerClass.CreatedByScreenID : Edm.String
PX.Objects.AR.ARDunningCustomerClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARDunningCustomerClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARDunningCustomerClass.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARDunningCustomerClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARDunningCustomerClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARDunningCustomerClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.AR.ARDunningLetter (EntityType)

Label: "Dunning Letter"
Key: DunningLetterID
Entity sets: PX_Objects_AR_ARDunningLetter, DunningLetter, ARDunningLetter
Non-filterable, non-selectable: Status, DetailsCount, CuryID, NoteText

PX.Objects.AR.ARDunningLetter.DunningLetterID : Edm.Int32 [key] "Dunning Letter ID"
PX.Objects.AR.ARDunningLetter.BAccountID : Edm.Int32 "Customer"
PX.Objects.AR.ARDunningLetter.DunningLetterDate : Edm.DateTimeOffset [required] "Dunning Letter Date"
PX.Objects.AR.ARDunningLetter.Deadline : Edm.DateTimeOffset "Deadline"
PX.Objects.AR.ARDunningLetter.DunningLetterLevel : Edm.Int32 "Dunning Letter Level"
PX.Objects.AR.ARDunningLetter.Printed : Edm.Boolean [required]
PX.Objects.AR.ARDunningLetter.DontPrint : Edm.Boolean [required] "Don't Print"
PX.Objects.AR.ARDunningLetter.Released : Edm.Boolean [required]
PX.Objects.AR.ARDunningLetter.Voided : Edm.Boolean [required]
PX.Objects.AR.ARDunningLetter.Status : Edm.String "Status"
PX.Objects.AR.ARDunningLetter.DetailsCount : Edm.Int32 "Number of Documents"
PX.Objects.AR.ARDunningLetter.FeeDocType : Edm.String "Fee Type"
PX.Objects.AR.ARDunningLetter.FeeRefNbr : Edm.String "Fee Reference Nbr."
PX.Objects.AR.ARDunningLetter.DunningFee : Edm.Decimal [required] "Dunning Fee"
PX.Objects.AR.ARDunningLetter.CuryID : Edm.String "Currency"
PX.Objects.AR.ARDunningLetter.Emailed : Edm.Boolean [required]
PX.Objects.AR.ARDunningLetter.NoteID : Edm.Guid
PX.Objects.AR.ARDunningLetter.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARDunningLetter.DontEmail : Edm.Boolean [required] "Don't Email"
PX.Objects.AR.ARDunningLetter.ConsolidationSettings : Edm.String
PX.Objects.AR.ARDunningLetter.LastLevel : Edm.Boolean [required]
PX.Objects.AR.ARDunningLetter.tstamp : Edm.Binary
PX.Objects.AR.ARDunningLetter.ARInvoiceByFeeRefNbr -> PX.Objects.AR.ARInvoice (FeeDocType=DocType, FeeRefNbr=RefNbr)
PX.Objects.AR.ARDunningLetter.CustomerByBAccountID -> PX.Objects.AR.Customer (BAccountID=BAccountID)
PX.Objects.AR.ARDunningLetter.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARDunningLetter.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)

# PX.Objects.AR.ARDunningLetterDetail (EntityType)

Label: "Dunning Letter Detail"
Key: DocType, DunningLetterID, RefNbr
Entity sets: PX_Objects_AR_ARDunningLetterDetail, DunningLetterDetail, ARDunningLetterDetail
Non-filterable, non-selectable: PrintDocType

PX.Objects.AR.ARDunningLetterDetail.DunningLetterID : Edm.Int32 [key] "DunningLetterID"
PX.Objects.AR.ARDunningLetterDetail.DocType : Edm.String [key] "Type"
PX.Objects.AR.ARDunningLetterDetail.PrintDocType : Edm.String "Type"
PX.Objects.AR.ARDunningLetterDetail.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARDunningLetterDetail.BAccountID : Edm.Int32 "Customer"
PX.Objects.AR.ARDunningLetterDetail.DunningLetterBAccountID : Edm.Int32
PX.Objects.AR.ARDunningLetterDetail.DocDate : Edm.DateTimeOffset [required]
PX.Objects.AR.ARDunningLetterDetail.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AR.ARDunningLetterDetail.CuryOrigDocAmt : Edm.Decimal
PX.Objects.AR.ARDunningLetterDetail.CuryDocBal : Edm.Decimal
PX.Objects.AR.ARDunningLetterDetail.CuryID : Edm.String "Currency ID"
PX.Objects.AR.ARDunningLetterDetail.OrigDocAmt : Edm.Decimal "Original Document Amount"
PX.Objects.AR.ARDunningLetterDetail.DocBal : Edm.Decimal "Outstanding Balance"
PX.Objects.AR.ARDunningLetterDetail.Overdue : Edm.Boolean [required]
PX.Objects.AR.ARDunningLetterDetail.OverdueBal : Edm.Decimal "Overdue Balance"
PX.Objects.AR.ARDunningLetterDetail.Voided : Edm.Boolean
PX.Objects.AR.ARDunningLetterDetail.Released : Edm.Boolean
PX.Objects.AR.ARDunningLetterDetail.tstamp : Edm.Binary
PX.Objects.AR.ARDunningLetterDetail.DunningLetterLevel : Edm.Int32 "Dunning Level"
PX.Objects.AR.ARDunningLetterDetail.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AR.ARDunningLetterDetail.CustomerByBAccountID -> PX.Objects.AR.Customer (BAccountID=BAccountID)
PX.Objects.AR.ARDunningLetterDetail.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.ARDunningLetterDetail.ARDunningLetterByDunningLetterID -> PX.Objects.AR.ARDunningLetter (DunningLetterID=DunningLetterID)

# PX.Objects.AR.ARDunningLetterDetailReport (EntityType)

Label: "Dunning Letter Detail"
BaseType: PX.Objects.AR.ARDunningLetterDetail
Key: DocType, DunningLetterID, RefNbr (inherited from PX.Objects.AR.ARDunningLetterDetail)
Entity sets: PX_Objects_AR_ARDunningLetterDetailReport, DunningLetterDetail1, ARDunningLetterDetailReport

PX.Objects.AR.ARDunningLetterDetailReport.SortDate : Edm.DateTimeOffset

# PX.Objects.AR.ARDunningSetup (EntityType)

Label: "AR Dunning Setup"
Key: DunningLetterLevel
Entity sets: PX_Objects_AR_ARDunningSetup, ARDunningSetup1
Non-filterable, non-selectable: NoteText

PX.Objects.AR.ARDunningSetup.DunningLetterLevel : Edm.Int32 [key required] "Dunning Letter Level"
PX.Objects.AR.ARDunningSetup.DueDays : Edm.Int32 [required] "Days Past Due"
PX.Objects.AR.ARDunningSetup.DaysToSettle : Edm.Int32 [required] "Days to Settle"
PX.Objects.AR.ARDunningSetup.Descr : Edm.String "Description"
PX.Objects.AR.ARDunningSetup.DunningFee : Edm.Decimal [required] "Dunning Fee"
PX.Objects.AR.ARDunningSetup.NoteID : Edm.Guid
PX.Objects.AR.ARDunningSetup.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARDunningSetup.tstamp : Edm.Binary
PX.Objects.AR.ARDunningSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARDunningSetup.CreatedByScreenID : Edm.String
PX.Objects.AR.ARDunningSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARDunningSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARDunningSetup.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARDunningSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARDunningSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARDunningSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.AR.ARFinCharge (EntityType)

Label: "AR Financial Charge"
Key: FinChargeID
Entity sets: PX_Objects_AR_ARFinCharge, ARFinancialCharge, ARFinCharge
Non-filterable, non-selectable: LineThreshold, FixedAmount, ChargingMethod, NoteText

PX.Objects.AR.ARFinCharge.FinChargeID : Edm.String [key] "Overdue Charge ID"
PX.Objects.AR.ARFinCharge.FinChargeDesc : Edm.String "Description"
PX.Objects.AR.ARFinCharge.TermsID : Edm.String "Terms"
PX.Objects.AR.ARFinCharge.BaseCurFlag : Edm.Boolean [required] "Base Currency"
PX.Objects.AR.ARFinCharge.MinFinChargeFlag : Edm.Boolean [required] "Use Line Minimum Amount"
PX.Objects.AR.ARFinCharge.MinFinChargeAmount : Edm.Decimal [required] "Min. Amount"
PX.Objects.AR.ARFinCharge.LineThreshold : Edm.Decimal "Threshold"
PX.Objects.AR.ARFinCharge.FixedAmount : Edm.Decimal "Amount"
PX.Objects.AR.ARFinCharge.MinChargeDocumentAmt : Edm.Decimal [required] "Total Threshold"
PX.Objects.AR.ARFinCharge.PercentFlag : Edm.Boolean [required] "Use Percent Rate"
PX.Objects.AR.ARFinCharge.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.AR.ARFinCharge.FeeAmount : Edm.Decimal [required] "Fee Amount"
PX.Objects.AR.ARFinCharge.FeeDesc : Edm.String "Fee Description"
PX.Objects.AR.ARFinCharge.CalculationMethod : Edm.Int32 [required] "Calculation Method"
PX.Objects.AR.ARFinCharge.ChargingMethod : Edm.Int32 "Charging Method"
PX.Objects.AR.ARFinCharge.tstamp : Edm.Binary
PX.Objects.AR.ARFinCharge.NoteID : Edm.Guid
PX.Objects.AR.ARFinCharge.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARFinCharge.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARFinCharge.CreatedByScreenID : Edm.String
PX.Objects.AR.ARFinCharge.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.ARFinCharge.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARFinCharge.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARFinCharge.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.ARFinCharge.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARFinCharge.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARFinCharge.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.AR.ARFinCharge.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AR.ARFinCharge.AccountByFinChargeAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARFinCharge.AccountByFeeAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARFinCharge.SubByFinChargeSubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARFinCharge.SubByFeeSubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARFinCharge.ARStatementCycleCollection -> Collection(PX.Objects.AR.ARStatementCycle)
PX.Objects.AR.ARFinCharge.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.AR.ARFinCharge.ARFinChargePercentCollection -> Collection(PX.Objects.AR.ARFinChargePercent)

# PX.Objects.AR.ARFinChargePercent (EntityType)

Label: "AR Financial Charge Percent"
Key: PercentID
Entity sets: PX_Objects_AR_ARFinChargePercent, ARFinancialChargePercent, ARFinChargePercent

PX.Objects.AR.ARFinChargePercent.FinChargeID : Edm.String
PX.Objects.AR.ARFinChargePercent.FinChargePercent : Edm.Decimal "Percent Rate"
PX.Objects.AR.ARFinChargePercent.BeginDate : Edm.DateTimeOffset [required] "Start Date"
PX.Objects.AR.ARFinChargePercent.PercentID : Edm.Int32 [key]
PX.Objects.AR.ARFinChargePercent.ARFinChargeByFinChargeID -> PX.Objects.AR.ARFinCharge (FinChargeID=FinChargeID)

# PX.Objects.AR.ARFinChargeTran (EntityType)

Label: "AR Financial Charge Transaction"
Key: LineNbr, RefNbr, TranType
Entity sets: PX_Objects_AR_ARFinChargeTran, ARFinancialChargeTransaction, ARFinChargeTran

PX.Objects.AR.ARFinChargeTran.TranType : Edm.String [key]
PX.Objects.AR.ARFinChargeTran.RefNbr : Edm.String [key]
PX.Objects.AR.ARFinChargeTran.LineNbr : Edm.Int32 [key]
PX.Objects.AR.ARFinChargeTran.OrigDocType : Edm.String
PX.Objects.AR.ARFinChargeTran.OrigRefNbr : Edm.String
PX.Objects.AR.ARFinChargeTran.CustomerID : Edm.Int32
PX.Objects.AR.ARFinChargeTran.DocDate : Edm.DateTimeOffset
PX.Objects.AR.ARFinChargeTran.FinChargeID : Edm.String
PX.Objects.AR.ARFinChargeTran.ARTranByLineNbr -> PX.Objects.AR.ARTran (TranType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)

# PX.Objects.AR.ARHistory (EntityType)

Label: "AR History"
Key: AccountID, BranchID, CustomerID, FinPeriodID, SubID
Entity sets: PX_Objects_AR_ARHistory, ARHistory
Non-filterable, non-selectable: FinFlag, PtdCrAdjustments, PtdDrAdjustments, PtdSales, PtdPayments, PtdDiscounts, YtdBalance, BegBalance, PtdCOGS, PtdRGOL, PtdFinCharges, PtdDeposits, YtdDeposits, PtdItemDiscounts, PtdRetainageWithheld, YtdRetainageWithheld, PtdRetainageReleased, YtdRetainageReleased

PX.Objects.AR.ARHistory.BranchID : Edm.Int32 [key]
PX.Objects.AR.ARHistory.AccountID : Edm.Int32 [key]
PX.Objects.AR.ARHistory.SubID : Edm.Int32 [key]
PX.Objects.AR.ARHistory.FinPeriodID : Edm.String [key]
PX.Objects.AR.ARHistory.CustomerID : Edm.Int32 [key] "Customer ID"
PX.Objects.AR.ARHistory.DetDeleted : Edm.Boolean [required]
PX.Objects.AR.ARHistory.FinPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdSales : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdPayments : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdDiscounts : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinYtdBalance : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinBegBalance : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdCOGS : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdRGOL : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdFinCharges : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdDeposits : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinYtdDeposits : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdItemDiscounts : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinPtdRevalued : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdSales : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdPayments : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdDiscounts : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranYtdBalance : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranBegBalance : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdCOGS : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdRGOL : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdFinCharges : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdDeposits : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranYtdDeposits : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdItemDiscounts : Edm.Decimal [required]
PX.Objects.AR.ARHistory.tstamp : Edm.Binary
PX.Objects.AR.ARHistory.FinFlag : Edm.Boolean
PX.Objects.AR.ARHistory.NumberInvoicePaid : Edm.Int32 [required]
PX.Objects.AR.ARHistory.PaidInvoiceDays : Edm.Int16 [required]
PX.Objects.AR.ARHistory.PtdCrAdjustments : Edm.Decimal
PX.Objects.AR.ARHistory.PtdDrAdjustments : Edm.Decimal
PX.Objects.AR.ARHistory.PtdSales : Edm.Decimal
PX.Objects.AR.ARHistory.PtdPayments : Edm.Decimal
PX.Objects.AR.ARHistory.PtdDiscounts : Edm.Decimal
PX.Objects.AR.ARHistory.YtdBalance : Edm.Decimal
PX.Objects.AR.ARHistory.BegBalance : Edm.Decimal
PX.Objects.AR.ARHistory.PtdCOGS : Edm.Decimal
PX.Objects.AR.ARHistory.PtdRGOL : Edm.Decimal
PX.Objects.AR.ARHistory.PtdFinCharges : Edm.Decimal
PX.Objects.AR.ARHistory.PtdDeposits : Edm.Decimal
PX.Objects.AR.ARHistory.YtdDeposits : Edm.Decimal
PX.Objects.AR.ARHistory.PtdItemDiscounts : Edm.Decimal
PX.Objects.AR.ARHistory.FinPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.ARHistory.PtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.ARHistory.YtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.ARHistory.FinPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.ARHistory.FinYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.ARHistory.TranYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.ARHistory.PtdRetainageReleased : Edm.Decimal
PX.Objects.AR.ARHistory.YtdRetainageReleased : Edm.Decimal
PX.Objects.AR.ARHistory.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARHistory.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARHistory.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.ARHistory.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.AR.ARHistory.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.AR.ARHistoryByPeriod (EntityType)

Label: "AR History by Period"
Key: AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID
Entity sets: PX_Objects_AR_ARHistoryByPeriod, ARHistorybyPeriod

PX.Objects.AR.ARHistoryByPeriod.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.AR.ARHistoryByPeriod.CustomerID : Edm.Int32 [key] "Customer"
PX.Objects.AR.ARHistoryByPeriod.AccountID : Edm.Int32 [key] "Account"
PX.Objects.AR.ARHistoryByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.AR.ARHistoryByPeriod.CuryID : Edm.String [key]
PX.Objects.AR.ARHistoryByPeriod.LastActivityPeriod : Edm.String
PX.Objects.AR.ARHistoryByPeriod.FinPeriodID : Edm.String [key]
PX.Objects.AR.ARHistoryByPeriod.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)

# PX.Objects.AR.ARHistorySumCreditSales (ComplexType)


PX.Objects.AR.ARHistorySumCreditSales.FinPeriodID : Edm.String
PX.Objects.AR.ARHistorySumCreditSales.TranYtdBalance : Edm.Decimal
PX.Objects.AR.ARHistorySumCreditSales.CreditSales : Edm.Decimal

# PX.Objects.AR.ARHistorySumForPeriod (EntityType)

Label: "AR History Sum For Period"
Key: FinPeriodID
Entity sets: PX_Objects_AR_ARHistorySumForPeriod, ARHistorySumForPeriod

PX.Objects.AR.ARHistorySumForPeriod.FinPeriodID : Edm.String [key]
PX.Objects.AR.ARHistorySumForPeriod.TranYtdBalance : Edm.Decimal
PX.Objects.AR.ARHistorySumForPeriod.TranPtdSales : Edm.Decimal
PX.Objects.AR.ARHistorySumForPeriod.TranPtdDrAdjustments : Edm.Decimal
PX.Objects.AR.ARHistorySumForPeriod.TranPtdCrAdjustments : Edm.Decimal

# PX.Objects.AR.ARHistoryTran (ComplexType)


PX.Objects.AR.ARHistoryTran.ID : Edm.Int32
PX.Objects.AR.ARHistoryTran.DocType : Edm.String
PX.Objects.AR.ARHistoryTran.RefNbr : Edm.String
PX.Objects.AR.ARHistoryTran.LineNbr : Edm.Int32
PX.Objects.AR.ARHistoryTran.SourceDocType : Edm.String
PX.Objects.AR.ARHistoryTran.SourceRefNbr : Edm.String
PX.Objects.AR.ARHistoryTran.CuryInfoID : Edm.Int64
PX.Objects.AR.ARHistoryTran.CustomerID : Edm.Int32
PX.Objects.AR.ARHistoryTran.FinPeriodID : Edm.String
PX.Objects.AR.ARHistoryTran.TranPeriodID : Edm.String
PX.Objects.AR.ARHistoryTran.BatchNbr : Edm.String
PX.Objects.AR.ARHistoryTran.Type : Edm.String
PX.Objects.AR.ARHistoryTran.TranType : Edm.String
PX.Objects.AR.ARHistoryTran.TranRefNbr : Edm.String
PX.Objects.AR.ARHistoryTran.ReferenceID : Edm.Int32
PX.Objects.AR.ARHistoryTran.IsMigratedRecord : Edm.Boolean
PX.Objects.AR.ARHistoryTran.PtdSales : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdPayments : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdDrAdjustments : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdCrAdjustments : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdDiscounts : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdItemDiscounts : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdRGOL : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdFinCharges : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdDeposits : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.ARHistoryTran.PtdRetainageReleased : Edm.Decimal

# PX.Objects.AR.ARInvoice (EntityType)

Label: "AR Invoice/Memo"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARInvoice, ARInvoiceMemo, ARInvoice
Non-filterable, non-selectable: ExternalTaxesImportInProgress, DrCr, CuryUnreleasedPaymentAmt, UnreleasedPaymentAmt, CuryCCAuthorizedAmt, CCAuthorizedAmt, CuryPaidAmt, PaidAmt, CuryApplicationBalance, ApplicationBalance, LastFinChargeDate, LastPaymentDate, CuryWhTaxBal, WhTaxBal, Hidden, HiddenOrderType, HiddenOrderNbr, HiddenByShipment, HiddenShipmentType, HiddenShipmentNbr, ApplyPaymentWhenTaxAvailable, DeferPriceDiscountRecalculation, IsPriceAndDiscountsValid, CorrectionDocType, CorrectionRefNbr, IsUnderCancellation, IsLoadApplications

PX.Objects.AR.ARInvoice.BillAddressID : Edm.Int32
PX.Objects.AR.ARInvoice.BillContactID : Edm.Int32 "Billing Contact"
PX.Objects.AR.ARInvoice.MultiShipAddress : Edm.Boolean [required] "Multiple Ship-To Addresses"
PX.Objects.AR.ARInvoice.ShipAddressID : Edm.Int32
PX.Objects.AR.ARInvoice.ShipContactID : Edm.Int32 "Shipping Contact"
PX.Objects.AR.ARInvoice.TermsID : Edm.String "Terms"
PX.Objects.AR.ARInvoice.DiscDate : Edm.DateTimeOffset "Cash Discount Date"
PX.Objects.AR.ARInvoice.InvoiceNbr : Edm.String "Customer Order Nbr."
PX.Objects.AR.ARInvoice.InvoiceDate : Edm.DateTimeOffset [required] "Customer Ref. Date"
PX.Objects.AR.ARInvoice.TaxZoneID : Edm.String "Customer Tax Zone"
PX.Objects.AR.ARInvoice.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.AR.ARInvoice.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.AR.ARInvoice.MasterRefNbr : Edm.String
PX.Objects.AR.ARInvoice.InstallmentCntr : Edm.Int16
PX.Objects.AR.ARInvoice.InstallmentNbr : Edm.Int16
PX.Objects.AR.ARInvoice.CuryVatExemptTotal : Edm.Decimal [required] "Tax Exempt Total"
PX.Objects.AR.ARInvoice.VatExemptTotal : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryVatTaxableTotal : Edm.Decimal [required] "Taxable Total"
PX.Objects.AR.ARInvoice.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.ExternalTaxesImportInProgress : Edm.Boolean
PX.Objects.AR.ARInvoice.DrCr : Edm.String
PX.Objects.AR.ARInvoice.CuryFreightCost : Edm.Decimal [required] "Freight Cost"
PX.Objects.AR.ARInvoice.FreightCost : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryGoodsTotal : Edm.Decimal [required] "Goods Total"
PX.Objects.AR.ARInvoice.GoodsTotal : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryLineTotal : Edm.Decimal [required] "Detail Total"
PX.Objects.AR.ARInvoice.LineTotal : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryLineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.AR.ARInvoice.LineDiscTotal : Edm.Decimal [required] "Line Discounts"
PX.Objects.AR.ARInvoice.CuryGroupDiscTotal : Edm.Decimal [required] "Group Discounts"
PX.Objects.AR.ARInvoice.GroupDiscTotal : Edm.Decimal [required] "Group Discounts"
PX.Objects.AR.ARInvoice.CuryDocumentDiscTotal : Edm.Decimal [required] "Document Discount"
PX.Objects.AR.ARInvoice.DocumentDiscTotal : Edm.Decimal [required] "Document Discount"
PX.Objects.AR.ARInvoice.CuryDiscTot : Edm.Decimal [required] "Group and Document Discount Total"
PX.Objects.AR.ARInvoice.DiscTot : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryOrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.AR.ARInvoice.OrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.AR.ARInvoice.CuryMiscTot : Edm.Decimal [required] "Misc. Total"
PX.Objects.AR.ARInvoice.MiscTot : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryGoodsExtPriceTotal : Edm.Decimal [required] "Goods"
PX.Objects.AR.ARInvoice.GoodsExtPriceTotal : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryMiscExtPriceTotal : Edm.Decimal [required] "Misc. Charges"
PX.Objects.AR.ARInvoice.MiscExtPriceTotal : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryDetailExtPriceTotal : Edm.Decimal "Detail Total"
PX.Objects.AR.ARInvoice.DetailExtPriceTotal : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.AR.ARInvoice.TaxTotal : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryFreightTot : Edm.Decimal [required] "Freight Total"
PX.Objects.AR.ARInvoice.FreightTot : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryFreightAmt : Edm.Decimal [required] "Freight Price"
PX.Objects.AR.ARInvoice.FreightAmt : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryPremiumFreightAmt : Edm.Decimal [required] "Premium Freight Price"
PX.Objects.AR.ARInvoice.PremiumFreightAmt : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryPaymentTotal : Edm.Decimal [required] "Total Paid"
PX.Objects.AR.ARInvoice.PaymentTotal : Edm.Decimal [required] "Total Paid"
PX.Objects.AR.ARInvoice.CuryBalanceWOTotal : Edm.Decimal [required] "Write-Off Total"
PX.Objects.AR.ARInvoice.BalanceWOTotal : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryUnreleasedPaymentAmt : Edm.Decimal "Not Released"
PX.Objects.AR.ARInvoice.UnreleasedPaymentAmt : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryCCAuthorizedAmt : Edm.Decimal "Authorized"
PX.Objects.AR.ARInvoice.CCAuthorizedAmt : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryPaidAmt : Edm.Decimal "Released"
PX.Objects.AR.ARInvoice.PaidAmt : Edm.Decimal
PX.Objects.AR.ARInvoice.CuryUnpaidBalance : Edm.Decimal [required] "Unpaid Balance"
PX.Objects.AR.ARInvoice.UnpaidBalance : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryDiscAppliedAmt : Edm.Decimal [required] "Cash Discount Taken"
PX.Objects.AR.ARInvoice.DiscAppliedAmt : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CommnPct : Edm.Decimal [required] "Commission %"
PX.Objects.AR.ARInvoice.CuryCommnAmt : Edm.Decimal [required] "Commission Amt."
PX.Objects.AR.ARInvoice.CommnAmt : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryApplicationBalance : Edm.Decimal "Application Balance"
PX.Objects.AR.ARInvoice.ApplicationBalance : Edm.Decimal
PX.Objects.AR.ARInvoice.ApplyOverdueCharge : Edm.Boolean [required] "Apply Overdue Charges"
PX.Objects.AR.ARInvoice.LastFinChargeDate : Edm.DateTimeOffset "Last Fin. Charge Date"
PX.Objects.AR.ARInvoice.LastPaymentDate : Edm.DateTimeOffset "Last Payment Date"
PX.Objects.AR.ARInvoice.CuryCommnblAmt : Edm.Decimal [required] "Total Commissionable"
PX.Objects.AR.ARInvoice.CommnblAmt : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.CuryWhTaxBal : Edm.Decimal
PX.Objects.AR.ARInvoice.WhTaxBal : Edm.Decimal
PX.Objects.AR.ARInvoice.CreditHold : Edm.Boolean [required] "Credit Hold"
PX.Objects.AR.ARInvoice.ApprovedCredit : Edm.Boolean [required]
PX.Objects.AR.ARInvoice.ApprovedCreditAmt : Edm.Decimal [required]
PX.Objects.AR.ARInvoice.ApprovedCaptureFailed : Edm.Boolean [required]
PX.Objects.AR.ARInvoice.ApprovedPrepaymentRequired : Edm.Boolean [required]
PX.Objects.AR.ARInvoice.ProjectID : Edm.Int32 "Project/Contract"
PX.Objects.AR.ARInvoice.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AR.ARInvoice.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.AR.ARInvoice.WorkgroupID : Edm.Int32 "Workgroup ID"
PX.Objects.AR.ARInvoice.OwnerID : Edm.Int32 "Owner"
PX.Objects.AR.ARInvoice.Hidden : Edm.Boolean
PX.Objects.AR.ARInvoice.HiddenOrderType : Edm.String
PX.Objects.AR.ARInvoice.HiddenOrderNbr : Edm.String
PX.Objects.AR.ARInvoice.HiddenByShipment : Edm.Boolean
PX.Objects.AR.ARInvoice.HiddenShipmentType : Edm.String
PX.Objects.AR.ARInvoice.HiddenShipmentNbr : Edm.String
PX.Objects.AR.ARInvoice.ApplyPaymentWhenTaxAvailable : Edm.Boolean
PX.Objects.AR.ARInvoice.IsPaymentsTransferred : Edm.Boolean [required]
PX.Objects.AR.ARInvoice.ProformaExists : Edm.Boolean [required] "Pro Forma Invoice Exists"
PX.Objects.AR.ARInvoice.Revoked : Edm.Boolean [required] "Revoked"
PX.Objects.AR.ARInvoice.DisableAutomaticDiscountCalculation : Edm.Boolean [required] "Disable Automatic Discount Update"
PX.Objects.AR.ARInvoice.DeferPriceDiscountRecalculation : Edm.Boolean "Defer Price/Discount Recalculation"
PX.Objects.AR.ARInvoice.IsPriceAndDiscountsValid : Edm.Boolean "Prices and discounts are up to date."
PX.Objects.AR.ARInvoice.CorrectionDocType : Edm.String
PX.Objects.AR.ARInvoice.CorrectionRefNbr : Edm.String
PX.Objects.AR.ARInvoice.IsUnderCancellation : Edm.Boolean
PX.Objects.AR.ARInvoice.PendingProcessingCntr : Edm.Int32 [required]
PX.Objects.AR.ARInvoice.CaptureFailedCntr : Edm.Int32 [required]
PX.Objects.AR.ARInvoice.IsLoadApplications : Edm.Boolean
PX.Objects.AR.ARInvoice.AuthorizedPaymentCntr : Edm.Int32 [required]
PX.Objects.AR.ARInvoice.ProjectCuryInfoID : Edm.Int64
PX.Objects.AR.ARInvoice.PayLinkID : Edm.Int32
PX.Objects.AR.ARInvoice.ProcessingCenterID : Edm.String "Processing Center"
PX.Objects.AR.ARInvoice.DeliveryMethod : Edm.String "Link Delivery Method"
PX.Objects.AR.ARInvoice.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.AR.ARInvoice.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.AR.ARInvoice.ARContactByBillContactID -> PX.Objects.AR.ARContact (BillContactID=ContactID)
PX.Objects.AR.ARInvoice.ARContactByShipContactID -> PX.Objects.AR.ARContact (ShipContactID=ContactID)
PX.Objects.AR.ARInvoice.ARRegisterByDocType -> PX.Objects.AR.ARRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AR.ARInvoice.ARAddressByBillAddressID -> PX.Objects.AR.ARAddress (BillAddressID=AddressID)
PX.Objects.AR.ARInvoice.ARAddressByShipAddressID -> PX.Objects.AR.ARAddress (ShipAddressID=AddressID)
PX.Objects.AR.ARInvoice.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.AR.ARInvoice.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.AR.ARInvoice.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AR.ARInvoice.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.AR.ARInvoice.CashAccountByBranchID -> PX.Objects.CA.CashAccount
PX.Objects.AR.ARInvoice.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AR.ARInvoice.CustomerPaymentMethodByPaymentMethodID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID, CustomerID=BAccountID, PaymentMethodID=PaymentMethodID)
PX.Objects.AR.ARInvoice.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (CustomerID=BAccountID, PMInstanceID=PMInstanceID)
PX.Objects.AR.ARInvoice.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.AR.ARInvoice.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AR.ARInvoice.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.AR.ARInvoice.CRRelationCollection -> Collection(PX.Objects.CR.CRRelation)
PX.Objects.AR.ARInvoice.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.AR.ARInvoice.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.AR.ARInvoice.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AR.ARInvoice.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.AR.ARInvoice.PMBillingRecordCollection -> Collection(PX.Objects.PM.PMBillingRecord)
PX.Objects.AR.ARInvoice.CCPayLinkCollection -> Collection(PX.Objects.CC.CCPayLink)
PX.Objects.AR.ARInvoice.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.AR.ARInvoice.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.AR.ARInvoice.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.AR.ARInvoice.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.AR.ARInvoice.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.AR.ARInvoice.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.AR.ARInvoice.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.AR.ARInvoice.SVInvoiceCollection -> Collection(PX.Objects.SV.SVInvoice)
PX.Objects.AR.ARInvoice.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.AR.ARInvoice.PMProformaRevisionCollection -> Collection(PX.Objects.PM.PMProformaRevision)
PX.Objects.AR.ARInvoice.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.Objects.AR.ARInvoice.SoldInventoryItemCollection -> Collection(PX.Objects.FS.SoldInventoryItem)

# PX.Objects.AR.ARInvoiceDiscountDetail (EntityType)

Label: "AR Invoice Discount Detail"
Key: DocType, RecordID, RefNbr
Entity sets: PX_Objects_AR_ARInvoiceDiscountDetail, ARInvoiceDiscountDetail
Non-filterable, non-selectable: IsOrigDocDiscount

PX.Objects.AR.ARInvoiceDiscountDetail.DocType : Edm.String [key] "Type"
PX.Objects.AR.ARInvoiceDiscountDetail.RecordID : Edm.Int32 [key]
PX.Objects.AR.ARInvoiceDiscountDetail.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.AR.ARInvoiceDiscountDetail.SkipDiscount : Edm.Boolean [required] "Skip Discount"
PX.Objects.AR.ARInvoiceDiscountDetail.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARInvoiceDiscountDetail.OrderType : Edm.String "Order Type"
PX.Objects.AR.ARInvoiceDiscountDetail.OrderNbr : Edm.String "Order Nbr."
PX.Objects.AR.ARInvoiceDiscountDetail.DiscountID : Edm.String "Discount Code"
PX.Objects.AR.ARInvoiceDiscountDetail.DiscountSequenceID : Edm.String "Sequence ID"
PX.Objects.AR.ARInvoiceDiscountDetail.Type : Edm.String "Type"
PX.Objects.AR.ARInvoiceDiscountDetail.CuryInfoID : Edm.Int64
PX.Objects.AR.ARInvoiceDiscountDetail.DiscountableAmt : Edm.Decimal
PX.Objects.AR.ARInvoiceDiscountDetail.CuryDiscountableAmt : Edm.Decimal "Discountable Amt."
PX.Objects.AR.ARInvoiceDiscountDetail.DiscountableQty : Edm.Decimal "Discountable Qty."
PX.Objects.AR.ARInvoiceDiscountDetail.DiscountAmt : Edm.Decimal
PX.Objects.AR.ARInvoiceDiscountDetail.CuryDiscountAmt : Edm.Decimal "Discount Amt."
PX.Objects.AR.ARInvoiceDiscountDetail.DiscountPct : Edm.Decimal "Discount Percent"
PX.Objects.AR.ARInvoiceDiscountDetail.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.AR.ARInvoiceDiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.AR.ARInvoiceDiscountDetail.IsManual : Edm.Boolean [required] "Manual Discount"
PX.Objects.AR.ARInvoiceDiscountDetail.IsOrigDocDiscount : Edm.Boolean
PX.Objects.AR.ARInvoiceDiscountDetail.ExtDiscCode : Edm.String "External Discount Code"
PX.Objects.AR.ARInvoiceDiscountDetail.Description : Edm.String "Description"
PX.Objects.AR.ARInvoiceDiscountDetail.RetainedDiscountAmt : Edm.Decimal [required]
PX.Objects.AR.ARInvoiceDiscountDetail.tstamp : Edm.Binary
PX.Objects.AR.ARInvoiceDiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARInvoiceDiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.AR.ARInvoiceDiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARInvoiceDiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARInvoiceDiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARInvoiceDiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARInvoiceDiscountDetail.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.AR.ARInvoiceDiscountDetail.SOOrderByOrderType -> PX.Objects.SO.SOOrder (OrderNbr=OrderNbr, OrderType=OrderType)
PX.Objects.AR.ARInvoiceDiscountDetail.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARInvoiceDiscountDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARInvoiceDiscountDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARInvoiceDiscountDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARInvoiceDiscountDetail.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.AR.ARInvoiceDiscountDetail.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AR.ARInvoiceDiscountDetail.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.ARInvoiceExt (EntityType)

Label: "AR Invoice/Memo"
BaseType: PX.Objects.AR.ARInvoice
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARInvoiceExt
Non-filterable, non-selectable: DisplayProjectID, CuryRetainageBal, RetainageBal, RetainageReleasePct, CuryRetainageReleasedAmt, RetainageReleasedAmt, CuryRetainageUnreleasedCalcAmt, RetainageUnreleasedCalcAmt

PX.Objects.AR.ARInvoiceExt.DisplayProjectID : Edm.Int32 "Project"
PX.Objects.AR.ARInvoiceExt.CuryRetainageBal : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.RetainageBal : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.RetainageReleasePct : Edm.Decimal "Percent to Release"
PX.Objects.AR.ARInvoiceExt.CuryRetainageReleasedAmt : Edm.Decimal "Retainage to Release"
PX.Objects.AR.ARInvoiceExt.RetainageReleasedAmt : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.CuryRetainageUnreleasedCalcAmt : Edm.Decimal "Unreleased Retainage"
PX.Objects.AR.ARInvoiceExt.RetainageUnreleasedCalcAmt : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.ARTranLineNbr : Edm.Int32
PX.Objects.AR.ARInvoiceExt.ARTranCuryOrigRetainageAmt : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.ARTranOrigRetainageAmt : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.ARTranCuryRetainageBal : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.ARTranRetainageBal : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.ARTranCuryOrigTranAmt : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.ARTranOrigTranAmt : Edm.Decimal
PX.Objects.AR.ARInvoiceExt.PMProjectByARTranProjectID -> PX.Objects.PM.PMProject
PX.Objects.AR.ARInvoiceExt.PMTaskByARTranTaskID -> PX.Objects.PM.PMTask
PX.Objects.AR.ARInvoiceExt.InventoryItemByARTranInventoryID -> PX.Objects.IN.InventoryItem
PX.Objects.AR.ARInvoiceExt.PMCostCodeByARTranCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.AR.ARInvoiceExt.AccountByARTranAccountID -> PX.Objects.GL.Account

# PX.Objects.AR.ARInvoiceRetainageBalanceAtDate (EntityType)

Label: "ARInvoiceRetainageBalanceAtDate"
Key: DocType, RefNbr, SubmissionDate
Entity sets: PX_Objects_AR_ARInvoiceRetainageBalanceAtDate, ARInvoiceRetainageBalanceAtDate

PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.DocType : Edm.String [key]
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.RefNbr : Edm.String [key]
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.SubmissionDate : Edm.DateTimeOffset [key]
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.LineTotal : Edm.Decimal
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.AR.ARInvoiceRetainageBalanceAtDate.ARTranAccrueCostCollection -> Collection(PX.Objects.AR.ARTranAccrueCost)

# PX.Objects.AR.ARNotification (EntityType)

Label: "AR Notification"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_AR_ARNotification, ARNotification

# PX.Objects.AR.ARPayment (EntityType)

Label: "AR Payment"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARPayment, ARPayment
Non-filterable, non-selectable: NewCard, NewAccount, UpdateNextNumber, CuryUnappliedBal, UnappliedBal, CuryApplAmt, CurySOApplAmt, SOApplAmt, ApplAmt, CuryWOAmt, WOAmt, VoidAppl, CanHaveBalance, DrCr, SaveAccount, DepositDate, NeedTaskValidation, PostponeReleasedFlag, PostponeVoidedFlag, OrigReleased

PX.Objects.AR.ARPayment.CuryOrigTaxDiscAmt : Edm.Decimal [required]
PX.Objects.AR.ARPayment.OrigTaxDiscAmt : Edm.Decimal [required]
PX.Objects.AR.ARPayment.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AR.ARPayment.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.AR.ARPayment.ProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.AR.ARPayment.SyncLock : Edm.Boolean
PX.Objects.AR.ARPayment.SyncLockReason : Edm.String
PX.Objects.AR.ARPayment.NewCard : Edm.Boolean "New Card"
PX.Objects.AR.ARPayment.TerminalID : Edm.String "Terminal"
PX.Objects.AR.ARPayment.CardPresent : Edm.Boolean [required]
PX.Objects.AR.ARPayment.NewAccount : Edm.Boolean "New Account"
PX.Objects.AR.ARPayment.UpdateNextNumber : Edm.Boolean "Update Next Number"
PX.Objects.AR.ARPayment.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.AR.ARPayment.AdjDate : Edm.DateTimeOffset "Application Date"
PX.Objects.AR.ARPayment.AdjFinPeriodID : Edm.String "Application Period"
PX.Objects.AR.ARPayment.AdjTranPeriodID : Edm.String
PX.Objects.AR.ARPayment.CuryConsolidateChargeTotal : Edm.Decimal [required] "Deducted Charges"
PX.Objects.AR.ARPayment.ConsolidateChargeTotal : Edm.Decimal [required]
PX.Objects.AR.ARPayment.ChargeCntr : Edm.Int32 [required]
PX.Objects.AR.ARPayment.CuryUnappliedBal : Edm.Decimal "Available Balance"
PX.Objects.AR.ARPayment.UnappliedBal : Edm.Decimal
PX.Objects.AR.ARPayment.CuryApplAmt : Edm.Decimal "Applied to Documents"
PX.Objects.AR.ARPayment.CurySOApplAmt : Edm.Decimal "Applied to Orders"
PX.Objects.AR.ARPayment.SOApplAmt : Edm.Decimal
PX.Objects.AR.ARPayment.ApplAmt : Edm.Decimal
PX.Objects.AR.ARPayment.CuryWOAmt : Edm.Decimal "Write-Off Amount"
PX.Objects.AR.ARPayment.WOAmt : Edm.Decimal
PX.Objects.AR.ARPayment.Cleared : Edm.Boolean "Cleared"
PX.Objects.AR.ARPayment.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.AR.ARPayment.VoidAppl : Edm.Boolean "Void Application"
PX.Objects.AR.ARPayment.CanHaveBalance : Edm.Boolean "Can Have Balance"
PX.Objects.AR.ARPayment.DrCr : Edm.String
PX.Objects.AR.ARPayment.CATranID : Edm.Int64
PX.Objects.AR.ARPayment.IsCCPayment : Edm.Boolean [required] "IsCCPayment"
PX.Objects.AR.ARPayment.IsCCAuthorized : Edm.Boolean [required]
PX.Objects.AR.ARPayment.IsCCCaptured : Edm.Boolean [required]
PX.Objects.AR.ARPayment.IsCCCaptureFailed : Edm.Boolean [required]
PX.Objects.AR.ARPayment.IsCCRefunded : Edm.Boolean [required]
PX.Objects.AR.ARPayment.IsCCUserAttention : Edm.Boolean [required]
PX.Objects.AR.ARPayment.SaveCard : Edm.Boolean [required] "Save Card"
PX.Objects.AR.ARPayment.SaveAccount : Edm.Boolean "Save Account"
PX.Objects.AR.ARPayment.CCPaymentStateDescr : Edm.String "Processing Status"
PX.Objects.AR.ARPayment.DepositAsBatch : Edm.Boolean [required] "Batch Deposit"
PX.Objects.AR.ARPayment.DepositAfter : Edm.DateTimeOffset "Deposit After"
PX.Objects.AR.ARPayment.DepositDate : Edm.DateTimeOffset "Batch Deposit Date"
PX.Objects.AR.ARPayment.Deposited : Edm.Boolean [required] "Deposited"
PX.Objects.AR.ARPayment.DepositType : Edm.String
PX.Objects.AR.ARPayment.DepositNbr : Edm.String "Batch Deposit Nbr."
PX.Objects.AR.ARPayment.CCTransactionRefund : Edm.Boolean "Use Orig. Transaction for Refund"
PX.Objects.AR.ARPayment.RefTranExtNbr : Edm.String "Orig. Transaction"
PX.Objects.AR.ARPayment.CCReauthDate : Edm.DateTimeOffset
PX.Objects.AR.ARPayment.CCReauthTriesLeft : Edm.Int32
PX.Objects.AR.ARPayment.CCActualExternalTransactionID : Edm.Int32
PX.Objects.AR.ARPayment.NeedTaskValidation : Edm.Boolean
PX.Objects.AR.ARPayment.PostponeReleasedFlag : Edm.Boolean
PX.Objects.AR.ARPayment.PostponeVoidedFlag : Edm.Boolean
PX.Objects.AR.ARPayment.Settled : Edm.Boolean [required] "Settled"
PX.Objects.AR.ARPayment.OrigReleased : Edm.Boolean
PX.Objects.AR.ARPayment.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AR.ARPayment.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AR.ARPayment.ARRegisterByDocType -> PX.Objects.AR.ARRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AR.ARPayment.CCProcessingCenterTerminalByProcessingCenterID -> PX.Objects.CC.CCProcessingCenterTerminal (TerminalID=TerminalID, ProcessingCenterID=ProcessingCenterID)
PX.Objects.AR.ARPayment.CADepositByDepositType -> PX.Objects.CA.CADeposit (DepositNbr=RefNbr, DepositType=TranType)
PX.Objects.AR.ARPayment.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.AR.ARPayment.CashAccountByBranchID -> PX.Objects.CA.CashAccount
PX.Objects.AR.ARPayment.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.AR.ARPayment.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AR.ARPayment.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.AR.ARPayment.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.AR.ARPayment.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.AR.ARPayment.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AR.ARPayment.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.AR.ARPayment.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.Objects.AR.ARPayment.FSAdjustCollection -> Collection(PX.Objects.FS.FSAdjust)
PX.Objects.AR.ARPayment.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)

# PX.Objects.AR.ARPaymentChargeTran (EntityType)

Label: "AR Payment Charge Transaction"
Key: DocType, LineNbr, RefNbr
Entity sets: PX_Objects_AR_ARPaymentChargeTran, ARPaymentChargeTransaction, ARPaymentChargeTran

PX.Objects.AR.ARPaymentChargeTran.DocType : Edm.String [key] "DocType"
PX.Objects.AR.ARPaymentChargeTran.RefNbr : Edm.String [key]
PX.Objects.AR.ARPaymentChargeTran.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AR.ARPaymentChargeTran.CashAccountID : Edm.Int32 "Cash Account ID"
PX.Objects.AR.ARPaymentChargeTran.DrCr : Edm.String "Disb./Receipt"
PX.Objects.AR.ARPaymentChargeTran.ExtRefNbr : Edm.String "ExtRefNbr"
PX.Objects.AR.ARPaymentChargeTran.EntryTypeID : Edm.String "Entry Type"
PX.Objects.AR.ARPaymentChargeTran.TranDate : Edm.DateTimeOffset "TranDate"
PX.Objects.AR.ARPaymentChargeTran.FinPeriodID : Edm.String "FinPeriodID"
PX.Objects.AR.ARPaymentChargeTran.TranPeriodID : Edm.String "TranPeriodID"
PX.Objects.AR.ARPaymentChargeTran.TranDesc : Edm.String "Description"
PX.Objects.AR.ARPaymentChargeTran.CuryInfoID : Edm.Int64
PX.Objects.AR.ARPaymentChargeTran.CashTranID : Edm.Int64
PX.Objects.AR.ARPaymentChargeTran.CuryTranAmt : Edm.Decimal [required] "Amount"
PX.Objects.AR.ARPaymentChargeTran.TranAmt : Edm.Decimal [required]
PX.Objects.AR.ARPaymentChargeTran.Released : Edm.Boolean [required] "Released"
PX.Objects.AR.ARPaymentChargeTran.Cleared : Edm.Boolean [required] "Cleared"
PX.Objects.AR.ARPaymentChargeTran.ClearDate : Edm.DateTimeOffset "ClearDate"
PX.Objects.AR.ARPaymentChargeTran.Consolidate : Edm.Boolean
PX.Objects.AR.ARPaymentChargeTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARPaymentChargeTran.CreatedByScreenID : Edm.String
PX.Objects.AR.ARPaymentChargeTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARPaymentChargeTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARPaymentChargeTran.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARPaymentChargeTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARPaymentChargeTran.tstamp : Edm.Binary
PX.Objects.AR.ARPaymentChargeTran.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.AR.ARPaymentChargeTran.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.AR.ARPaymentChargeTran.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.AR.ARPaymentChargeTran.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARPaymentChargeTran.BranchByCashAccountID -> PX.Objects.GL.Branch (CashAccountID=BranchID)
PX.Objects.AR.ARPaymentChargeTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARPaymentChargeTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARPaymentChargeTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARPaymentChargeTran.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.AR.ARPaymentChargeTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARPaymentChargeTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARPaymentChargeTran.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.AR.ARPaymentChargeTran.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)

# PX.Objects.AR.ARPaymentInfo (EntityType)

Label: "AR Payment"
BaseType: PX.Objects.AR.ARPayment
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARPaymentInfo
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.AR.ARPaymentInfo.PMInstanceDescr : Edm.String "Card/Account Nbr."
PX.Objects.AR.ARPaymentInfo.CCTranDescr : Edm.String "Error Descr."
PX.Objects.AR.ARPaymentInfo.IsCCExpired : Edm.Boolean "Expired"

# PX.Objects.AR.ARPaymentTotals (EntityType)

Label: "AR Payment Totals"
Key: DocType, RefNbr
Entity sets: PX_Objects_AR_ARPaymentTotals, ARPaymentTotals

PX.Objects.AR.ARPaymentTotals.DocType : Edm.String [key] "Type"
PX.Objects.AR.ARPaymentTotals.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARPaymentTotals.OrderCntr : Edm.Int32 [required]
PX.Objects.AR.ARPaymentTotals.AdjdOrderType : Edm.String "Order Type"
PX.Objects.AR.ARPaymentTotals.AdjdOrderNbr : Edm.String "Order Nbr."
PX.Objects.AR.ARPaymentTotals.InvoiceCntr : Edm.Int32 [required]
PX.Objects.AR.ARPaymentTotals.AdjdDocType : Edm.String "Doc. Type"
PX.Objects.AR.ARPaymentTotals.AdjdRefNbr : Edm.String "Reference Nbr."
PX.Objects.AR.ARPaymentTotals.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARPaymentTotals.CreatedByScreenID : Edm.String
PX.Objects.AR.ARPaymentTotals.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARPaymentTotals.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARPaymentTotals.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARPaymentTotals.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARPaymentTotals.tstamp : Edm.Binary
PX.Objects.AR.ARPaymentTotals.SOOrderByAdjdOrderType -> PX.Objects.SO.SOOrder (AdjdOrderNbr=OrderNbr, AdjdOrderType=OrderType)
PX.Objects.AR.ARPaymentTotals.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARPaymentTotals.ARRegisterByAdjdDocType -> PX.Objects.AR.ARRegister (AdjdRefNbr=RefNbr, AdjdDocType=DocType)
PX.Objects.AR.ARPaymentTotals.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARPaymentTotals.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARPaymentTotals.SOOrderTypeByAdjdOrderType -> PX.Objects.SO.SOOrderType (AdjdOrderType=OrderType)
PX.Objects.AR.ARPaymentTotals.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.ARPaymentTotals.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.AR.ARPaymentTotals.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.AR.ARPaymentTotals.BlanketSOAdjustCollection -> Collection(PX.Objects.SO.DAC.Projections.BlanketSOAdjust)

# PX.Objects.AR.ARPriceClass (EntityType)

Label: "AR Price Class"
Key: PriceClassID
Entity sets: PX_Objects_AR_ARPriceClass, ARPriceClass
Non-filterable, non-selectable: NoteText

PX.Objects.AR.ARPriceClass.PriceClassID : Edm.String [key] "Price Class ID"
PX.Objects.AR.ARPriceClass.Description : Edm.String "Description"
PX.Objects.AR.ARPriceClass.NoteID : Edm.Guid
PX.Objects.AR.ARPriceClass.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARPriceClass.tstamp : Edm.Binary
PX.Objects.AR.ARPriceClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARPriceClass.CreatedByScreenID : Edm.String
PX.Objects.AR.ARPriceClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARPriceClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARPriceClass.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARPriceClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARPriceClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARPriceClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARPriceClass.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.AR.ARPriceClass.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.AR.ARPriceClass.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.AR.ARPriceClass.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.AR.ARPriceClass.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.AR.ARPriceClass.DiscountCustomerPriceClassCollection -> Collection(PX.Objects.AR.DiscountCustomerPriceClass)

# PX.Objects.AR.ARPriceWorksheet (EntityType)

Label: "AR Price Worksheet"
Key: RefNbr
Entity sets: PX_Objects_AR_ARPriceWorksheet, ARPriceWorksheet
Non-filterable, non-selectable: NoteText

PX.Objects.AR.ARPriceWorksheet.Status : Edm.String "Status"
PX.Objects.AR.ARPriceWorksheet.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARPriceWorksheet.Hold : Edm.Boolean [required] "Hold"
PX.Objects.AR.ARPriceWorksheet.Approved : Edm.Boolean [required] "Approved"
PX.Objects.AR.ARPriceWorksheet.Descr : Edm.String "Description"
PX.Objects.AR.ARPriceWorksheet.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AR.ARPriceWorksheet.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AR.ARPriceWorksheet.IsPromotional : Edm.Boolean [required] "Promotional"
PX.Objects.AR.ARPriceWorksheet.SkipLineDiscounts : Edm.Boolean "Ignore Automatic Line Discounts"
PX.Objects.AR.ARPriceWorksheet.IsFairValue : Edm.Boolean [required] "Fair Value"
PX.Objects.AR.ARPriceWorksheet.IsProrated : Edm.Boolean [required] "Prorated"
PX.Objects.AR.ARPriceWorksheet.Discountable : Edm.Boolean [required] "Apply Discounts to Fair Value"
PX.Objects.AR.ARPriceWorksheet.OverwriteOverlapping : Edm.Boolean [required] "Overwrite Overlapping Prices"
PX.Objects.AR.ARPriceWorksheet.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.AR.ARPriceWorksheet.NoteID : Edm.Guid
PX.Objects.AR.ARPriceWorksheet.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARPriceWorksheet.tstamp : Edm.Binary
PX.Objects.AR.ARPriceWorksheet.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARPriceWorksheet.CreatedByScreenID : Edm.String
PX.Objects.AR.ARPriceWorksheet.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.ARPriceWorksheet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARPriceWorksheet.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARPriceWorksheet.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.ARPriceWorksheet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARPriceWorksheet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARPriceWorksheet.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)

# PX.Objects.AR.ARPriceWorksheetDetail (EntityType)

Label: "AR Price Worksheet Detail"
Key: LineID, RefNbr
Entity sets: PX_Objects_AR_ARPriceWorksheetDetail, ARPriceWorksheetDetail
Non-filterable, non-selectable: TaxCategoryID, RestrictInventoryByAlternateID

PX.Objects.AR.ARPriceWorksheetDetail.LineID : Edm.Int32 [key]
PX.Objects.AR.ARPriceWorksheetDetail.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARPriceWorksheetDetail.PriceType : Edm.String "Price Type"
PX.Objects.AR.ARPriceWorksheetDetail.PriceCode : Edm.String "Price Code"
PX.Objects.AR.ARPriceWorksheetDetail.CustPriceClassID : Edm.String
PX.Objects.AR.ARPriceWorksheetDetail.CustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARPriceWorksheetDetail.CustomerCD : Edm.String
PX.Objects.AR.ARPriceWorksheetDetail.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AR.ARPriceWorksheetDetail.InventoryCD : Edm.String
PX.Objects.AR.ARPriceWorksheetDetail.AlternateID : Edm.String "Alternate ID"
PX.Objects.AR.ARPriceWorksheetDetail.Description : Edm.String "Description"
PX.Objects.AR.ARPriceWorksheetDetail.UOM : Edm.String "UOM"
PX.Objects.AR.ARPriceWorksheetDetail.BreakQty : Edm.Decimal [required] "Break Qty."
PX.Objects.AR.ARPriceWorksheetDetail.CurrentPrice : Edm.Decimal "Source Price"
PX.Objects.AR.ARPriceWorksheetDetail.PendingPrice : Edm.Decimal "Pending Price"
PX.Objects.AR.ARPriceWorksheetDetail.CuryID : Edm.String "Currency"
PX.Objects.AR.ARPriceWorksheetDetail.SkipLineDiscounts : Edm.Boolean "Ignore Automatic Line Discounts"
PX.Objects.AR.ARPriceWorksheetDetail.TaxID : Edm.String "Tax"
PX.Objects.AR.ARPriceWorksheetDetail.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.AR.ARPriceWorksheetDetail.tstamp : Edm.Binary
PX.Objects.AR.ARPriceWorksheetDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARPriceWorksheetDetail.CreatedByScreenID : Edm.String
PX.Objects.AR.ARPriceWorksheetDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARPriceWorksheetDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARPriceWorksheetDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARPriceWorksheetDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARPriceWorksheetDetail.RestrictInventoryByAlternateID : Edm.Boolean
PX.Objects.AR.ARPriceWorksheetDetail.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARPriceWorksheetDetail.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARPriceWorksheetDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AR.ARPriceWorksheetDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARPriceWorksheetDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARPriceWorksheetDetail.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.AR.ARPriceWorksheetDetail.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AR.ARPriceWorksheetDetail.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AR.ARPriceWorksheetDetail.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AR.ARPriceWorksheetDetail.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.ARPriceWorksheetDetail.ARPriceClassByCustPriceClassID -> PX.Objects.AR.ARPriceClass (CustPriceClassID=PriceClassID)
PX.Objects.AR.ARPriceWorksheetDetail.ARPriceWorksheetByRefNbr -> PX.Objects.AR.ARPriceWorksheet (RefNbr=RefNbr)

# PX.Objects.AR.ARRegister (EntityType)

Label: "AR Document"
Key: DocType, RefNbr
Entity sets: PX_Objects_AR_ARRegister, ARDocument, ARRegister
Non-filterable, non-selectable: InternalDocType, PrintDocType, DocDisc, CuryDocDisc, DocClass, ReleasedToVerify, FromSchedule, SelfVoidingDoc, NoteText, CuryDiscountedDocTotal, DiscountedDocTotal, CuryDiscountedTaxableTotal, DiscountedTaxableTotal, CuryDiscountedPrice, DiscountedPrice, RetainagePaidTotal, PostponePendingPaymentFlag, CuryRate, DeletedDatabaseRecord

PX.Objects.AR.ARRegister.DocType : Edm.String [key] "Type"
PX.Objects.AR.ARRegister.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARRegister.CustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARRegister.InternalDocType : Edm.String "Document Type (Internal)"
PX.Objects.AR.ARRegister.PrintDocType : Edm.String "Type"
PX.Objects.AR.ARRegister.DocumentKey : Edm.String "Document Description"
PX.Objects.AR.ARRegister.OrigModule : Edm.String "Source"
PX.Objects.AR.ARRegister.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AR.ARRegister.OrigDocDate : Edm.DateTimeOffset
PX.Objects.AR.ARRegister.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AR.ARRegister.TranPeriodID : Edm.String
PX.Objects.AR.ARRegister.FinPeriodID : Edm.String "Post Period"
PX.Objects.AR.ARRegister.CuryID : Edm.String "Currency"
PX.Objects.AR.ARRegister.LineCntr : Edm.Int32 [required]
PX.Objects.AR.ARRegister.AdjCntr : Edm.Int32 [required]
PX.Objects.AR.ARRegister.DRSchedCntr : Edm.Int32
PX.Objects.AR.ARRegister.CuryInfoID : Edm.Int64
PX.Objects.AR.ARRegister.CuryOrigDocAmt : Edm.Decimal [required] "Amount"
PX.Objects.AR.ARRegister.OrigDocAmt : Edm.Decimal [required]
PX.Objects.AR.ARRegister.CuryDocBal : Edm.Decimal [required] "Balance"
PX.Objects.AR.ARRegister.DocBal : Edm.Decimal [required]
PX.Objects.AR.ARRegister.CuryInitDocBal : Edm.Decimal [required] "Balance"
PX.Objects.AR.ARRegister.InitDocBal : Edm.Decimal [required]
PX.Objects.AR.ARRegister.DisplayCuryInitDocBal : Edm.Decimal "Migrated Balance"
PX.Objects.AR.ARRegister.CuryOrigDiscAmt : Edm.Decimal [required] "Cash Discount"
PX.Objects.AR.ARRegister.OrigDiscAmt : Edm.Decimal [required]
PX.Objects.AR.ARRegister.CuryDiscTaken : Edm.Decimal [required]
PX.Objects.AR.ARRegister.DiscTaken : Edm.Decimal [required]
PX.Objects.AR.ARRegister.CuryDiscBal : Edm.Decimal [required] "Cash Discount Balance"
PX.Objects.AR.ARRegister.DiscBal : Edm.Decimal [required]
PX.Objects.AR.ARRegister.DocDisc : Edm.Decimal
PX.Objects.AR.ARRegister.CuryDocDisc : Edm.Decimal "Document Discount"
PX.Objects.AR.ARRegister.CuryChargeAmt : Edm.Decimal [required] "Finance Charges"
PX.Objects.AR.ARRegister.ChargeAmt : Edm.Decimal [required]
PX.Objects.AR.ARRegister.DocDesc : Edm.String "Description"
PX.Objects.AR.ARRegister.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.AR.ARRegister.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARRegister.CreatedByScreenID : Edm.String
PX.Objects.AR.ARRegister.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.ARRegister.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARRegister.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARRegister.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.ARRegister.tstamp : Edm.Binary
PX.Objects.AR.ARRegister.DocClass : Edm.String
PX.Objects.AR.ARRegister.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.AR.ARRegister.BatchSeq : Edm.Int16
PX.Objects.AR.ARRegister.Released : Edm.Boolean [required]
PX.Objects.AR.ARRegister.ReleasedToVerify : Edm.Boolean
PX.Objects.AR.ARRegister.OpenDoc : Edm.Boolean [required]
PX.Objects.AR.ARRegister.Hold : Edm.Boolean [required] "Hold"
PX.Objects.AR.ARRegister.Scheduled : Edm.Boolean [required]
PX.Objects.AR.ARRegister.FromSchedule : Edm.Boolean
PX.Objects.AR.ARRegister.Voided : Edm.Boolean [required]
PX.Objects.AR.ARRegister.SelfVoidingDoc : Edm.Boolean
PX.Objects.AR.ARRegister.NoteID : Edm.Guid
PX.Objects.AR.ARRegister.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARRegister.ClosedDate : Edm.DateTimeOffset "Closed Date"
PX.Objects.AR.ARRegister.RefNoteID : Edm.Guid
PX.Objects.AR.ARRegister.ClosedFinPeriodID : Edm.String "Closed Period"
PX.Objects.AR.ARRegister.ClosedTranPeriodID : Edm.String "Closed Period"
PX.Objects.AR.ARRegister.RGOLAmt : Edm.Decimal [required]
PX.Objects.AR.ARRegister.CuryRoundDiff : Edm.Decimal [required] "Rounding Diff."
PX.Objects.AR.ARRegister.RoundDiff : Edm.Decimal [required]
PX.Objects.AR.ARRegister.ScheduleID : Edm.String
PX.Objects.AR.ARRegister.ImpRefNbr : Edm.String
PX.Objects.AR.ARRegister.StatementDate : Edm.DateTimeOffset
PX.Objects.AR.ARRegister.SalesPersonID : Edm.Int32 "Salesperson ID"
PX.Objects.AR.ARRegister.DisableAutomaticTaxCalculation : Edm.Boolean "Disable Automatic Tax Calculation"
PX.Objects.AR.ARRegister.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.AR.ARRegister.IsTaxPosted : Edm.Boolean [required] "Tax Is Posted/Committed to External Tax Engine (Avalara)"
PX.Objects.AR.ARRegister.IsTaxSaved : Edm.Boolean [required] "Tax Is Saved in External Tax Engine (Avalara)"
PX.Objects.AR.ARRegister.NonTaxable : Edm.Boolean [required] "Non-Taxable"
PX.Objects.AR.ARRegister.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.AR.ARRegister.OrigRefNbr : Edm.String "Orig. Ref. Nbr."
PX.Objects.AR.ARRegister.Status : Edm.String "Status"
PX.Objects.AR.ARRegister.CuryDiscountedDocTotal : Edm.Decimal "Discounted Doc. Total"
PX.Objects.AR.ARRegister.DiscountedDocTotal : Edm.Decimal
PX.Objects.AR.ARRegister.CuryDiscountedTaxableTotal : Edm.Decimal "Discounted Taxable Total"
PX.Objects.AR.ARRegister.DiscountedTaxableTotal : Edm.Decimal
PX.Objects.AR.ARRegister.CuryDiscountedPrice : Edm.Decimal "Tax on Discounted Price"
PX.Objects.AR.ARRegister.DiscountedPrice : Edm.Decimal
PX.Objects.AR.ARRegister.HasPPDTaxes : Edm.Boolean [required]
PX.Objects.AR.ARRegister.PendingPPD : Edm.Boolean [required]
PX.Objects.AR.ARRegister.IsMigratedRecord : Edm.Boolean
PX.Objects.AR.ARRegister.ApproverID : Edm.Int32 "Owner"
PX.Objects.AR.ARRegister.ApproverWorkgroupID : Edm.Int32 "Approval Workgroup ID"
PX.Objects.AR.ARRegister.Approved : Edm.Boolean [required]
PX.Objects.AR.ARRegister.Rejected : Edm.Boolean [required]
PX.Objects.AR.ARRegister.DontApprove : Edm.Boolean
PX.Objects.AR.ARRegister.CuryLineRetainageTotal : Edm.Decimal [required]
PX.Objects.AR.ARRegister.LineRetainageTotal : Edm.Decimal [required]
PX.Objects.AR.ARRegister.RetainedTaxTotal : Edm.Decimal [required]
PX.Objects.AR.ARRegister.RetainedDiscTotal : Edm.Decimal [required]
PX.Objects.AR.ARRegister.RetainageUnpaidTotal : Edm.Decimal [required]
PX.Objects.AR.ARRegister.RetainagePaidTotal : Edm.Decimal
PX.Objects.AR.ARRegister.IsCancellation : Edm.Boolean [required]
PX.Objects.AR.ARRegister.IsCorrection : Edm.Boolean [required] "Correction Inv."
PX.Objects.AR.ARRegister.IsUnderCorrection : Edm.Boolean [required]
PX.Objects.AR.ARRegister.Canceled : Edm.Boolean [required]
PX.Objects.AR.ARRegister.PendingProcessing : Edm.Boolean [required]
PX.Objects.AR.ARRegister.ExternalRef : Edm.String
PX.Objects.AR.ARRegister.PendingPayment : Edm.Boolean [required]
PX.Objects.AR.ARRegister.PostponePendingPaymentFlag : Edm.Boolean
PX.Objects.AR.ARRegister.DontPrint : Edm.Boolean "Don't Print"
PX.Objects.AR.ARRegister.Printed : Edm.Boolean [required] "Printed"
PX.Objects.AR.ARRegister.DontEmail : Edm.Boolean "Don't Email"
PX.Objects.AR.ARRegister.Emailed : Edm.Boolean [required] "Emailed"
PX.Objects.AR.ARRegister.PrintInvoice : Edm.Boolean
PX.Objects.AR.ARRegister.EmailInvoice : Edm.Boolean
PX.Objects.AR.ARRegister.CuryRate : Edm.Decimal
PX.Objects.AR.ARRegister.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AR.ARRegister.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARRegister.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARRegister.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.AR.ARRegister.ContactByApproverID -> PX.Objects.CR.Contact (ApproverID=ContactID)
PX.Objects.AR.ARRegister.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (OrigDocType=DocType, RefNbr=OrigRefNbr)
PX.Objects.AR.ARRegister.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARRegister.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARRegister.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARRegister.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARRegister.EPCompanyTreeByApproverWorkgroupID -> PX.TM.EPCompanyTree (ApproverWorkgroupID=WorkGroupID)
PX.Objects.AR.ARRegister.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.ARRegister.AccountByARAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARRegister.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.AR.ARRegister.AccountByPrepaymentAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARRegister.ScheduleByScheduleID -> PX.Objects.GL.Schedule (ScheduleID=ScheduleID)
PX.Objects.AR.ARRegister.SubByARSubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARRegister.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARRegister.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARRegister.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.AR.ARRegister.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.AR.ARRegister.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.AR.ARRegister.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.ARRegister.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AR.ARRegister.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AR.ARRegister.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.AR.ARRegister.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.ARRegister.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.AR.ARRegister.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.AR.ARRegister.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.AR.ARRegister.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.ARRegister.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.ARRegister.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.AR.ARRegister.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.AR.ARRegister.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.AR.ARRegister.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.AR.ARRegister.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.AR.ARRegister.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.AR.ARRegister.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.AR.ARRegister.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.AR.ARRegister.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.AR.ARRegister.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.AR.ARRegister.ARTranAccrueCostCollection -> Collection(PX.Objects.AR.ARTranAccrueCost)

# PX.Objects.AR.ARRegisterAccess (EntityType)

Label: "Customer"
BaseType: PX.Objects.AR.Customer
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_AR_ARRegisterAccess

PX.Objects.AR.ARRegisterAccess.DocType : Edm.String
PX.Objects.AR.ARRegisterAccess.RefNbr : Edm.String
PX.Objects.AR.ARRegisterAccess.Scheduled : Edm.Boolean
PX.Objects.AR.ARRegisterAccess.ScheduleID : Edm.String
PX.Objects.AR.ARRegisterAccess.ScheduleByScheduleID -> PX.Objects.GL.Schedule (ScheduleID=ScheduleID)
PX.Objects.AR.ARRegisterAccess.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AR.ARRegisterAccess.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.AR.ARRegisterAccess.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.AR.ARRegisterAccess.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.AR.ARRegisterAccess.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.AR.ARRegisterAccess.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.AR.ARRegisterAccess.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.AR.ARRegisterAccess.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.AR.ARRegisterAccess.ARTranAccrueCostCollection -> Collection(PX.Objects.AR.ARTranAccrueCost)

# PX.Objects.AR.ARRegisterCashSales (EntityType)

Label: "ARRegister Cash Sales"
BaseType: PX.Objects.AR.ARRegisterSigned
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARRegisterCashSales, ARRegisterCashSales

# PX.Objects.AR.ARRegisterReport (EntityType)

Label: "AR Document"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARRegisterReport, ARDocument1, ARRegisterReport

PX.Objects.AR.ARRegisterReport.SignBalance : Edm.Decimal
PX.Objects.AR.ARRegisterReport.SignAmount : Edm.Decimal
PX.Objects.AR.ARRegisterReport.SignReleasedRetainage : Edm.Decimal

# PX.Objects.AR.ARRegisterSigned (EntityType)

Label: "AR Document"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARRegisterSigned, ARDocument2, ARRegisterSigned

PX.Objects.AR.ARRegisterSigned.SignAmount : Edm.Decimal
PX.Objects.AR.ARRegisterSigned.SignedOrigDocAmt : Edm.Decimal

# PX.Objects.AR.ARRetainageInvoice (EntityType)

Label: "AR Document"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARRetainageInvoice

# PX.Objects.AR.ARRetainageWithApplications (EntityType)

Label: "AR Retainage documents with released/paid amount"
BaseType: PX.Objects.AR.ARRetainageInvoice
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_ARRetainageWithApplications, ARRetainagedocumentswithreleasedpaidamount, ARRetainageWithApplications
Non-filterable, non-selectable: CuryRetainageReleasedAmt, CuryRetainagePaidAmt

PX.Objects.AR.ARRetainageWithApplications.GlSign : Edm.Int16
PX.Objects.AR.ARRetainageWithApplications.BalanceSign : Edm.Int16
PX.Objects.AR.ARRetainageWithApplications.RetainageAmt : Edm.Decimal
PX.Objects.AR.ARRetainageWithApplications.CuryRetainageAmt : Edm.Decimal
PX.Objects.AR.ARRetainageWithApplications.Amt : Edm.Decimal
PX.Objects.AR.ARRetainageWithApplications.CuryAmt : Edm.Decimal "Paid Retainage"
PX.Objects.AR.ARRetainageWithApplications.DiscAmt : Edm.Decimal
PX.Objects.AR.ARRetainageWithApplications.CuryDiscAmt : Edm.Decimal
PX.Objects.AR.ARRetainageWithApplications.WOAmt : Edm.Decimal
PX.Objects.AR.ARRetainageWithApplications.CuryWOAmt : Edm.Decimal
PX.Objects.AR.ARRetainageWithApplications.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AR.ARRetainageWithApplications.InvoiceNbr : Edm.String "Customer Order Nbr."
PX.Objects.AR.ARRetainageWithApplications.CuryRetainageReleasedAmt : Edm.Decimal "Released Retainage"
PX.Objects.AR.ARRetainageWithApplications.CuryRetainagePaidAmt : Edm.Decimal "Paid Retainage"
PX.Objects.AR.ARRetainageWithApplications.ARRegisterByDocType -> PX.Objects.AR.ARRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AR.ARRetainageWithApplications.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)

# PX.Objects.AR.ARSalesPerTran (EntityType)

Label: "AR Salesperson Commission"
Key: AdjdDocType, AdjdRefNbr, AdjNbr, DocType, RefNbr, SalespersonID
Entity sets: PX_Objects_AR_ARSalesPerTran, ARSalespersonCommission, ARSalesPerTran

PX.Objects.AR.ARSalesPerTran.DocType : Edm.String [key]
PX.Objects.AR.ARSalesPerTran.RefNbr : Edm.String [key]
PX.Objects.AR.ARSalesPerTran.SalespersonID : Edm.Int32 [key]
PX.Objects.AR.ARSalesPerTran.RefCntr : Edm.Int32 [required]
PX.Objects.AR.ARSalesPerTran.AdjNbr : Edm.Int32 [key required]
PX.Objects.AR.ARSalesPerTran.AdjdDocType : Edm.String [key required]
PX.Objects.AR.ARSalesPerTran.AdjdRefNbr : Edm.String [key required]
PX.Objects.AR.ARSalesPerTran.CuryInfoID : Edm.Int64
PX.Objects.AR.ARSalesPerTran.CommnPct : Edm.Decimal [required] "Commission %"
PX.Objects.AR.ARSalesPerTran.CuryCommnblAmt : Edm.Decimal [required] "Commissionable Amount"
PX.Objects.AR.ARSalesPerTran.CommnblAmt : Edm.Decimal [required]
PX.Objects.AR.ARSalesPerTran.CuryCommnAmt : Edm.Decimal [required] "Commission Amt."
PX.Objects.AR.ARSalesPerTran.CommnAmt : Edm.Decimal [required]
PX.Objects.AR.ARSalesPerTran.BaseCuryID : Edm.String
PX.Objects.AR.ARSalesPerTran.Released : Edm.Boolean [required]
PX.Objects.AR.ARSalesPerTran.tstamp : Edm.Binary
PX.Objects.AR.ARSalesPerTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARSalesPerTran.CreatedByScreenID : Edm.String
PX.Objects.AR.ARSalesPerTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARSalesPerTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARSalesPerTran.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARSalesPerTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARSalesPerTran.ActuallyUsed : Edm.Boolean [required]
PX.Objects.AR.ARSalesPerTran.CommnPaymntPeriod : Edm.String
PX.Objects.AR.ARSalesPerTran.CommnPaymntDate : Edm.DateTimeOffset
PX.Objects.AR.ARSalesPerTran.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARSalesPerTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARSalesPerTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARSalesPerTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARSalesPerTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARSalesPerTran.SalesPersonBySalespersonID -> PX.Objects.AR.SalesPerson (SalespersonID=SalesPersonID)
PX.Objects.AR.ARSalesPerTran.ARTranCollection -> Collection(PX.Objects.AR.ARTran)

# PX.Objects.AR.ARSalesPrice (EntityType)

Label: "AR Sales Price"
Key: RecordID
Entity sets: PX_Objects_AR_ARSalesPrice, ARSalesPrice
Non-filterable, non-selectable: PriceCode, CustomerCD, Description, TaxCategoryID, InventoryCD, NoteText, ItemStatus, ItemClassID, PriceClassID, PriceWorkgroupID, PriceManagerID

PX.Objects.AR.ARSalesPrice.RecordID : Edm.Int32 [key]
PX.Objects.AR.ARSalesPrice.PriceType : Edm.String "Price Type"
PX.Objects.AR.ARSalesPrice.PriceCode : Edm.String "Price Code"
PX.Objects.AR.ARSalesPrice.CustPriceClassID : Edm.String "Customer Price Class"
PX.Objects.AR.ARSalesPrice.CustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARSalesPrice.CustomerCD : Edm.String
PX.Objects.AR.ARSalesPrice.Description : Edm.String "Description"
PX.Objects.AR.ARSalesPrice.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.AR.ARSalesPrice.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AR.ARSalesPrice.InventoryCD : Edm.String
PX.Objects.AR.ARSalesPrice.AlternateID : Edm.String "Alternate ID"
PX.Objects.AR.ARSalesPrice.CuryID : Edm.String "Currency"
PX.Objects.AR.ARSalesPrice.UOM : Edm.String "UOM"
PX.Objects.AR.ARSalesPrice.IsPromotionalPrice : Edm.Boolean "Promotion"
PX.Objects.AR.ARSalesPrice.SkipLineDiscounts : Edm.Boolean "Ignore Automatic Line Discounts"
PX.Objects.AR.ARSalesPrice.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AR.ARSalesPrice.SalesPrice : Edm.Decimal "Price"
PX.Objects.AR.ARSalesPrice.TaxID : Edm.String "Tax"
PX.Objects.AR.ARSalesPrice.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.AR.ARSalesPrice.BreakQty : Edm.Decimal [required] "Break Qty."
PX.Objects.AR.ARSalesPrice.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AR.ARSalesPrice.IsFairValue : Edm.Boolean [required] "Fair Value"
PX.Objects.AR.ARSalesPrice.IsProrated : Edm.Boolean [required] "Prorated"
PX.Objects.AR.ARSalesPrice.Discountable : Edm.Boolean [required] "Apply Discounts to Fair Value"
PX.Objects.AR.ARSalesPrice.NoteID : Edm.Guid
PX.Objects.AR.ARSalesPrice.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARSalesPrice.ItemStatus : Edm.String
PX.Objects.AR.ARSalesPrice.ItemClassID : Edm.Int32
PX.Objects.AR.ARSalesPrice.PriceClassID : Edm.String
PX.Objects.AR.ARSalesPrice.PriceWorkgroupID : Edm.Int32
PX.Objects.AR.ARSalesPrice.PriceManagerID : Edm.Int32
PX.Objects.AR.ARSalesPrice.tstamp : Edm.Binary
PX.Objects.AR.ARSalesPrice.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARSalesPrice.CreatedByScreenID : Edm.String
PX.Objects.AR.ARSalesPrice.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARSalesPrice.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARSalesPrice.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARSalesPrice.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARSalesPrice.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARSalesPrice.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARSalesPrice.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AR.ARSalesPrice.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARSalesPrice.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARSalesPrice.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.AR.ARSalesPrice.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.AR.ARSalesPrice.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AR.ARSalesPrice.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.ARSalesPrice.ARPriceClassByCustPriceClassID -> PX.Objects.AR.ARPriceClass (CustPriceClassID=PriceClassID)

# PX.Objects.AR.ARSetup (EntityType)

Label: "Account Receivable Preferences"
Singletons: PX_Objects_AR_ARSetup, AccountReceivablePreferences, ARSetup

PX.Objects.AR.ARSetup.BatchNumberingID : Edm.String "GL Batch Numbering Sequence"
PX.Objects.AR.ARSetup.DfltCustomerClassID : Edm.String "Default Customer Class ID"
PX.Objects.AR.ARSetup.PerRetainTran : Edm.Int16 [required] "Keep Transactions for"
PX.Objects.AR.ARSetup.PerRetainHist : Edm.Int16 [required] "Periods to Retain History"
PX.Objects.AR.ARSetup.InvoiceNumberingID : Edm.String "Invoice Numbering Sequence"
PX.Objects.AR.ARSetup.PaymentNumberingID : Edm.String "Payment Numbering Sequence"
PX.Objects.AR.ARSetup.CreditAdjNumberingID : Edm.String "Credit Memo Numbering Sequence"
PX.Objects.AR.ARSetup.DebitAdjNumberingID : Edm.String "Debit Memo Numbering Sequence"
PX.Objects.AR.ARSetup.WriteOffNumberingID : Edm.String "Write-Off Numbering Sequence"
PX.Objects.AR.ARSetup.PrepaymentInvoiceNumberingID : Edm.String "Prepayment Invoice Numbering Sequence"
PX.Objects.AR.ARSetup.UsageNumberingID : Edm.String "Usage Transaction Numbering Sequence"
PX.Objects.AR.ARSetup.PriceWSNumberingID : Edm.String "Price Worksheet Numbering Sequence"
PX.Objects.AR.ARSetup.DunningFeeNumberingID : Edm.String "Dunning Fee Numbering Sequence"
PX.Objects.AR.ARSetup.DefaultTranDesc : Edm.String "Default Transaction Description"
PX.Objects.AR.ARSetup.AutoPost : Edm.Boolean [required] "Automatically Post on Release"
PX.Objects.AR.ARSetup.TransactionPosting : Edm.String "Transaction Posting"
PX.Objects.AR.ARSetup.FinChargeNumberingID : Edm.String "Overdue Charge Numbering Sequence"
PX.Objects.AR.ARSetup.FinChargeOnCharge : Edm.Boolean [required] "Calculate on Overdue Charge Documents"
PX.Objects.AR.ARSetup.AgeCredits : Edm.Boolean [required] "Age Credits"
PX.Objects.AR.ARSetup.DataInconsistencyHandlingMode : Edm.String "Extra Data Validation"
PX.Objects.AR.ARSetup.tstamp : Edm.Binary
PX.Objects.AR.ARSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARSetup.CreatedByScreenID : Edm.String
PX.Objects.AR.ARSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARSetup.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARSetup.HoldEntry : Edm.Boolean [required] "Hold Documents on Entry"
PX.Objects.AR.ARSetup.RequireControlTotal : Edm.Boolean [required] "Validate Document Totals on Entry"
PX.Objects.AR.ARSetup.RequireExtRef : Edm.Boolean [required] "Require Payment Reference on Entry"
PX.Objects.AR.ARSetup.SummaryPost : Edm.Boolean "Post Summary on Updating GL"
PX.Objects.AR.ARSetup.CreditCheckError : Edm.Boolean [required] "Hold Document on Failed Credit Check"
PX.Objects.AR.ARSetup.SPCommnCalcType : Edm.String "Salesperson Commission By"
PX.Objects.AR.ARSetup.SPCommnPeriodType : Edm.String "Commission Period Type"
PX.Objects.AR.ARSetup.DefFinChargeFromCycle : Edm.Boolean [required] "Set Default Overdue Charges by Statement Cycle"
PX.Objects.AR.ARSetup.FinChargeFirst : Edm.Boolean [required] "Apply Payments to Overdue Charges First"
PX.Objects.AR.ARSetup.PrintBeforeRelease : Edm.Boolean [required] "Require Invoice/Memo Printing Before Release"
PX.Objects.AR.ARSetup.EmailBeforeRelease : Edm.Boolean [required] "Require Invoice/Memo Emailing Before Release"
PX.Objects.AR.ARSetup.IntegratedCCProcessing : Edm.Boolean [required] "Enable Integrated CC Processing"
PX.Objects.AR.ARSetup.PrepareStatements : Edm.String "Prepare Statements"
PX.Objects.AR.ARSetup.PrepareDunningLetters : Edm.String "Prepare Dunning Letters"
PX.Objects.AR.ARSetup.DunningLetterProcessType : Edm.Int32 [required] "Dunning Process"
PX.Objects.AR.ARSetup.AutoReleaseDunningFee : Edm.Boolean [required] "Automatically Release Dunning Fee Documents"
PX.Objects.AR.ARSetup.AutoReleaseDunningLetter : Edm.Boolean [required] "Automatically Release Dunning Letters"
PX.Objects.AR.ARSetup.IncludeNonOverdueDunning : Edm.Boolean [required] "Add Coming-Due Documents"
PX.Objects.AR.ARSetup.AddOpenPaymentsAndCreditMemos : Edm.Boolean [required] "Add Open Payments and Credit Memos"
PX.Objects.AR.ARSetup.AddUnpaidPPI : Edm.Boolean [required] "Add Unpaid Prepayment Invoices"
PX.Objects.AR.ARSetup.DunningFeeInventoryID : Edm.Int32 "Dunning Fee Item"
PX.Objects.AR.ARSetup.DunningFeeTermID : Edm.String "Terms"
PX.Objects.AR.ARSetup.InvoicePrecision : Edm.Decimal [required] "Rounding Precision"
PX.Objects.AR.ARSetup.InvoiceRounding : Edm.String "Rounding Rule for Invoices"
PX.Objects.AR.ARSetup.BalanceWriteOff : Edm.String "Balance Write-Off Reason Code"
PX.Objects.AR.ARSetup.CreditWriteOff : Edm.String "Credit Write-Off Reason Code"
PX.Objects.AR.ARSetup.DefaultRateTypeID : Edm.String "Default Rate Type"
PX.Objects.AR.ARSetup.AlwaysFromBaseCury : Edm.Boolean [required] "Always Calculate Price from Base Currency Price"
PX.Objects.AR.ARSetup.LoadSalesPricesUsingAlternateID : Edm.Boolean [required] "Load Sales Prices by Alternate ID"
PX.Objects.AR.ARSetup.LineDiscountTarget : Edm.String "Line Discount Basis"
PX.Objects.AR.ARSetup.ApplyQuantityDiscountBy : Edm.String "Apply Quantity Discounts To"
PX.Objects.AR.ARSetup.RetentionType : Edm.String "Retention Type"
PX.Objects.AR.ARSetup.NumberOfMonths : Edm.Int32 "Number of Months"
PX.Objects.AR.ARSetup.AutoReleasePPDCreditMemo : Edm.Boolean [required] "Automatically Release Tax Adjustments"
PX.Objects.AR.ARSetup.PPDCreditMemoDescr : Edm.String "Tax Adjustment Description"
PX.Objects.AR.ARSetup.TermsInCreditMemos : Edm.Boolean [required] "Use Credit Terms in Credit Memos"
PX.Objects.AR.ARSetup.NoteID : Edm.Guid
PX.Objects.AR.ARSetup.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARSetup.MigrationMode : Edm.Boolean [required] "Activate Migration Mode"
PX.Objects.AR.ARSetup.AutoLoadMaxDocs : Edm.Int16 [required] "Max. Number of Documents by Auto Loading"
PX.Objects.AR.ARSetup.InventoryItemByDunningFeeInventoryID -> PX.Objects.IN.InventoryItem (DunningFeeInventoryID=InventoryID)
PX.Objects.AR.ARSetup.BranchByStatementBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARSetup.BranchByDunningLetterBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARSetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByInvoiceNumberingID -> PX.Objects.CS.Numbering (InvoiceNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByPaymentNumberingID -> PX.Objects.CS.Numbering (PaymentNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByDebitAdjNumberingID -> PX.Objects.CS.Numbering (DebitAdjNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByCreditAdjNumberingID -> PX.Objects.CS.Numbering (CreditAdjNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByWriteOffNumberingID -> PX.Objects.CS.Numbering (WriteOffNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByPrepaymentInvoiceNumberingID -> PX.Objects.CS.Numbering (PrepaymentInvoiceNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByFinChargeNumberingID -> PX.Objects.CS.Numbering (FinChargeNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByUsageNumberingID -> PX.Objects.CS.Numbering (UsageNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByPriceWSNumberingID -> PX.Objects.CS.Numbering (PriceWSNumberingID=NumberingID)
PX.Objects.AR.ARSetup.NumberingByDunningFeeNumberingID -> PX.Objects.CS.Numbering (DunningFeeNumberingID=NumberingID)
PX.Objects.AR.ARSetup.ReasonCodeByBalanceWriteOff -> PX.Objects.CS.ReasonCode (BalanceWriteOff=ReasonCodeID)
PX.Objects.AR.ARSetup.ReasonCodeByCreditWriteOff -> PX.Objects.CS.ReasonCode (CreditWriteOff=ReasonCodeID)
PX.Objects.AR.ARSetup.TermsByDunningFeeTermID -> PX.Objects.CS.Terms (DunningFeeTermID=TermsID)
PX.Objects.AR.ARSetup.CurrencyRateTypeByDefaultRateTypeID -> PX.Objects.CM.CurrencyRateType (DefaultRateTypeID=CuryRateTypeID)
PX.Objects.AR.ARSetup.CustomerClassByDfltCustomerClassID -> PX.Objects.AR.CustomerClass (DfltCustomerClassID=CustomerClassID)

# PX.Objects.AR.ARSetupApproval (EntityType)

Key: ApprovalID
Entity sets: PX_Objects_AR_ARSetupApproval

PX.Objects.AR.ARSetupApproval.DocType : Edm.String "Type"
PX.Objects.AR.ARSetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.AR.ARSetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.AR.ARSetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.AR.ARSetupApproval.tstamp : Edm.Binary
PX.Objects.AR.ARSetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARSetupApproval.CreatedByScreenID : Edm.String
PX.Objects.AR.ARSetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARSetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARSetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARSetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARSetupApproval.IsActive : Edm.Boolean [required] "Active"
PX.Objects.AR.ARSetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARSetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARSetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.AR.ARSetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.AR.ARShippingAddress (EntityType)

Label: "AR Address"
BaseType: PX.Objects.AR.ARAddress
Key: AddressID (inherited from PX.Objects.AR.ARAddress)
Entity sets: PX_Objects_AR_ARShippingAddress, ARAddress1, ARShippingAddress

# PX.Objects.AR.ARShippingContact (EntityType)

Label: "AR Contact"
BaseType: PX.Objects.AR.ARContact
Key: ContactID (inherited from PX.Objects.AR.ARContact)
Entity sets: PX_Objects_AR_ARShippingContact, ARContact1, ARShippingContact

# PX.Objects.AR.ARSPCommissionPeriod (EntityType)

Label: "AR Salesperson Commission Period"
Key: CommnPeriodID
Entity sets: PX_Objects_AR_ARSPCommissionPeriod, ARSalespersonCommissionPeriod, ARSPCommissionPeriod
Non-filterable, non-selectable: StartDateUI, EndDateUI

PX.Objects.AR.ARSPCommissionPeriod.CommnPeriodID : Edm.String [key] "Commission Period"
PX.Objects.AR.ARSPCommissionPeriod.Year : Edm.String
PX.Objects.AR.ARSPCommissionPeriod.StartDate : Edm.DateTimeOffset
PX.Objects.AR.ARSPCommissionPeriod.StartDateUI : Edm.DateTimeOffset "From"
PX.Objects.AR.ARSPCommissionPeriod.EndDate : Edm.DateTimeOffset
PX.Objects.AR.ARSPCommissionPeriod.Status : Edm.String "Status"
PX.Objects.AR.ARSPCommissionPeriod.Filed : Edm.Boolean [required]
PX.Objects.AR.ARSPCommissionPeriod.tstamp : Edm.Binary
PX.Objects.AR.ARSPCommissionPeriod.EndDateUI : Edm.DateTimeOffset "To"

# PX.Objects.AR.ARSPCommissionYear (EntityType)

Label: "AR Salesperson Commission Year"
Key: Year
Entity sets: PX_Objects_AR_ARSPCommissionYear, ARSalespersonCommissionYear, ARSPCommissionYear

PX.Objects.AR.ARSPCommissionYear.Year : Edm.String [key]
PX.Objects.AR.ARSPCommissionYear.Filed : Edm.Boolean [required]
PX.Objects.AR.ARSPCommissionYear.tstamp : Edm.Binary

# PX.Objects.AR.ARSPCommnHistory (EntityType)

Label: "AR Salesperson Commission History"
Key: BranchID, CommnPeriod, CustomerID, CustomerLocationID, SalesPersonID
Entity sets: PX_Objects_AR_ARSPCommnHistory, ARSalespersonCommissionHistory, ARSPCommnHistory
Non-filterable, non-selectable: Type

PX.Objects.AR.ARSPCommnHistory.SalesPersonID : Edm.Int32 [key] "Salesperson ID"
PX.Objects.AR.ARSPCommnHistory.CommnPeriod : Edm.String [key] "Commission Period"
PX.Objects.AR.ARSPCommnHistory.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.AR.ARSPCommnHistory.CustomerID : Edm.Int32 [key]
PX.Objects.AR.ARSPCommnHistory.CustomerLocationID : Edm.Int32 [key]
PX.Objects.AR.ARSPCommnHistory.CommnAmt : Edm.Decimal [required] "Commission Amount"
PX.Objects.AR.ARSPCommnHistory.CommnblAmt : Edm.Decimal [required] "Commissionable Amount"
PX.Objects.AR.ARSPCommnHistory.PRProcessedDate : Edm.DateTimeOffset "PR Processed Date"
PX.Objects.AR.ARSPCommnHistory.BaseCuryID : Edm.String
PX.Objects.AR.ARSPCommnHistory.Type : Edm.String "Type"
PX.Objects.AR.ARSPCommnHistory.tstamp : Edm.Binary
PX.Objects.AR.ARSPCommnHistory.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARSPCommnHistory.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.ARSPCommnHistory.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID, CustomerLocationID=LocationID)
PX.Objects.AR.ARSPCommnHistory.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)

# PX.Objects.AR.ARStatement (EntityType)

Label: "AR Statement"
Key: BranchID, CuryID, CustomerID, StatementDate
Entity sets: PX_Objects_AR_ARStatement, ARStatement
Non-filterable, non-selectable: Processed, NoteText, IsParentCustomerStatement

PX.Objects.AR.ARStatement.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.AR.ARStatement.CuryID : Edm.String [key] "Currency ID"
PX.Objects.AR.ARStatement.CustomerID : Edm.Int32 [key] "Customer"
PX.Objects.AR.ARStatement.StatementCustomerID : Edm.Int32
PX.Objects.AR.ARStatement.StatementDate : Edm.DateTimeOffset [key] "Statement Date"
PX.Objects.AR.ARStatement.PrevStatementDate : Edm.DateTimeOffset "Last Statement Date"
PX.Objects.AR.ARStatement.StatementCycleId : Edm.String "Statement Cycle ID"
PX.Objects.AR.ARStatement.StatementType : Edm.String "Statement Type"
PX.Objects.AR.ARStatement.BegBalance : Edm.Decimal [required] "Beg. Balance"
PX.Objects.AR.ARStatement.CuryBegBalance : Edm.Decimal [required] "Curr. Beg. Balance"
PX.Objects.AR.ARStatement.EndBalance : Edm.Decimal [required]
PX.Objects.AR.ARStatement.CuryEndBalance : Edm.Decimal [required]
PX.Objects.AR.ARStatement.AgeBalance00 : Edm.Decimal [required] "Age00 Balance"
PX.Objects.AR.ARStatement.CuryAgeBalance00 : Edm.Decimal [required] "Cury. Age00 Balance"
PX.Objects.AR.ARStatement.AgeBalance01 : Edm.Decimal [required] "Age01 Balance"
PX.Objects.AR.ARStatement.CuryAgeBalance01 : Edm.Decimal [required] "Cury. Age01 Balance"
PX.Objects.AR.ARStatement.AgeBalance02 : Edm.Decimal [required] "Age02 Balance"
PX.Objects.AR.ARStatement.CuryAgeBalance02 : Edm.Decimal [required] "Cury. Age02 Balance"
PX.Objects.AR.ARStatement.AgeBalance03 : Edm.Decimal [required] "Cury. Age03 Balance"
PX.Objects.AR.ARStatement.CuryAgeBalance03 : Edm.Decimal [required] "Cury. Age03 Balance"
PX.Objects.AR.ARStatement.AgeBalance04 : Edm.Decimal [required] "Age04 Balance"
PX.Objects.AR.ARStatement.CuryAgeBalance04 : Edm.Decimal [required] "Cury. Age04 Balance"
PX.Objects.AR.ARStatement.AgeDays00 : Edm.Int16
PX.Objects.AR.ARStatement.AgeDays01 : Edm.Int16
PX.Objects.AR.ARStatement.AgeDays02 : Edm.Int16
PX.Objects.AR.ARStatement.AgeDays03 : Edm.Int16
PX.Objects.AR.ARStatement.AgeDays04 : Edm.Int16
PX.Objects.AR.ARStatement.AgeBucketCurrentDescription : Edm.String "Age Message 0"
PX.Objects.AR.ARStatement.AgeBucket01Description : Edm.String "Age Message 1"
PX.Objects.AR.ARStatement.AgeBucket02Description : Edm.String "Age Message 2"
PX.Objects.AR.ARStatement.AgeBucket03Description : Edm.String "Age Message 3"
PX.Objects.AR.ARStatement.AgeBucket04Description : Edm.String "Age Message 4"
PX.Objects.AR.ARStatement.DontPrint : Edm.Boolean [required] "Don't Print"
PX.Objects.AR.ARStatement.Printed : Edm.Boolean [required] "Printed"
PX.Objects.AR.ARStatement.PrevPrintedCnt : Edm.Int16 [required] "Previously Printed Count"
PX.Objects.AR.ARStatement.DontEmail : Edm.Boolean [required] "Don't Email"
PX.Objects.AR.ARStatement.Emailed : Edm.Boolean [required] "Emailed"
PX.Objects.AR.ARStatement.Processed : Edm.Boolean
PX.Objects.AR.ARStatement.PrevEmailedCnt : Edm.Int16 [required] "Previously Emailed Count"
PX.Objects.AR.ARStatement.OnDemand : Edm.Boolean [required] "On-Demand Statement"
PX.Objects.AR.ARStatement.LocaleName : Edm.String "Locale"
PX.Objects.AR.ARStatement.NoteID : Edm.Guid
PX.Objects.AR.ARStatement.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARStatement.tstamp : Edm.Binary
PX.Objects.AR.ARStatement.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARStatement.CreatedByScreenID : Edm.String
PX.Objects.AR.ARStatement.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARStatement.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARStatement.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARStatement.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARStatement.IsParentCustomerStatement : Edm.Boolean
PX.Objects.AR.ARStatement.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARStatement.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARStatement.CustomerByStatementCustomerID -> PX.Objects.AR.Customer (StatementCustomerID=BAccountID)
PX.Objects.AR.ARStatement.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.ARStatement.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARStatement.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARStatement.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.ARStatement.ARStatementCycleByStatementCycleId -> PX.Objects.AR.ARStatementCycle (StatementCycleId=StatementCycleId)
PX.Objects.AR.ARStatement.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.AR.ARStatement.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)

# PX.Objects.AR.ARStatementCycle (EntityType)

Label: "Statement Cycle"
Key: StatementCycleId
Entity sets: PX_Objects_AR_ARStatementCycle, StatementCycle, ARStatementCycle
Non-filterable, non-selectable: NextStmtDate, Bucket01LowerInclusiveBound, Bucket02LowerInclusiveBound, Bucket03LowerInclusiveBound, Bucket04LowerExclusiveBound, NoteText

PX.Objects.AR.ARStatementCycle.NextStmtDate : Edm.DateTimeOffset "Next Statement Date"
PX.Objects.AR.ARStatementCycle.StatementCycleId : Edm.String [key] "Cycle ID"
PX.Objects.AR.ARStatementCycle.Descr : Edm.String "Description"
PX.Objects.AR.ARStatementCycle.UseFinPeriodForAging : Edm.Boolean [required] "Use Financial Periods for Aging"
PX.Objects.AR.ARStatementCycle.AgeDays00 : Edm.Int16 [required] "Age Days 1"
PX.Objects.AR.ARStatementCycle.AgeDays01 : Edm.Int16 [required] "Age Days 2"
PX.Objects.AR.ARStatementCycle.AgeDays02 : Edm.Int16 [required] "Age Days 3"
PX.Objects.AR.ARStatementCycle.Bucket01LowerInclusiveBound : Edm.Int32 "Bucket01LowerInclusiveBound"
PX.Objects.AR.ARStatementCycle.Bucket02LowerInclusiveBound : Edm.Int32 "Bucket02LowerInclusiveBound"
PX.Objects.AR.ARStatementCycle.Bucket03LowerInclusiveBound : Edm.Int32 "Bucket03LowerInclusiveBound"
PX.Objects.AR.ARStatementCycle.Bucket04LowerExclusiveBound : Edm.Int32 "Bucket04LowerExclusiveBound"
PX.Objects.AR.ARStatementCycle.AgeMsgCurrent : Edm.String "Age Message 0"
PX.Objects.AR.ARStatementCycle.AgeMsg00 : Edm.String "Age Message 1"
PX.Objects.AR.ARStatementCycle.AgeMsg01 : Edm.String "Age Message 2"
PX.Objects.AR.ARStatementCycle.AgeMsg02 : Edm.String "Age Message 3"
PX.Objects.AR.ARStatementCycle.AgeMsg03 : Edm.String "Age Message 4"
PX.Objects.AR.ARStatementCycle.LastAgeDate : Edm.DateTimeOffset
PX.Objects.AR.ARStatementCycle.LastFinChrgDate : Edm.DateTimeOffset "Last Finance Charge Date"
PX.Objects.AR.ARStatementCycle.LastStmtDate : Edm.DateTimeOffset "Last Statement Date"
PX.Objects.AR.ARStatementCycle.PrepareOn : Edm.String "Schedule Type"
PX.Objects.AR.ARStatementCycle.Day00 : Edm.Int16 "Day of Month 1"
PX.Objects.AR.ARStatementCycle.Day01 : Edm.Int16 "Day of Month 2"
PX.Objects.AR.ARStatementCycle.DayOfWeek : Edm.Int32 [required] "Day of Week"
PX.Objects.AR.ARStatementCycle.FinChargeApply : Edm.Boolean [required] "Apply Overdue Charges"
PX.Objects.AR.ARStatementCycle.FinChargeID : Edm.String "Overdue Charge ID"
PX.Objects.AR.ARStatementCycle.RequirePaymentApplication : Edm.Boolean [required] "Require Payment Application Before Statement"
PX.Objects.AR.ARStatementCycle.RequireFinChargeProcessing : Edm.Boolean [required] "Require Overdue Charges Calculation Before Statement"
PX.Objects.AR.ARStatementCycle.AgeBasedOn : Edm.String "Age Based On"
PX.Objects.AR.ARStatementCycle.PrintEmptyStatements : Edm.Boolean [required] "Print Empty Statements"
PX.Objects.AR.ARStatementCycle.NoteID : Edm.Guid
PX.Objects.AR.ARStatementCycle.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARStatementCycle.tstamp : Edm.Binary
PX.Objects.AR.ARStatementCycle.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARStatementCycle.CreatedByScreenID : Edm.String
PX.Objects.AR.ARStatementCycle.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.ARStatementCycle.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARStatementCycle.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARStatementCycle.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.ARStatementCycle.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARStatementCycle.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARStatementCycle.ARFinChargeByFinChargeID -> PX.Objects.AR.ARFinCharge (FinChargeID=FinChargeID)
PX.Objects.AR.ARStatementCycle.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.AR.ARStatementCycle.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.AR.ARStatementCycle.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.AR.ARStatementCycle.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)

# PX.Objects.AR.ARStatementDetail (EntityType)

Label: "AR Statement Detail"
Key: CuryID, CustomerID, DocType, RefNbr, RefNoteID, StatementDate
Entity sets: PX_Objects_AR_ARStatementDetail, ARStatementDetail

PX.Objects.AR.ARStatementDetail.CustomerID : Edm.Int32 [key] "Customer ID"
PX.Objects.AR.ARStatementDetail.StatementDate : Edm.DateTimeOffset [key] "Statement Date"
PX.Objects.AR.ARStatementDetail.CuryID : Edm.String [key] "Currency ID"
PX.Objects.AR.ARStatementDetail.DocType : Edm.String [key] "DocType"
PX.Objects.AR.ARStatementDetail.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.AR.ARStatementDetail.DocBalance : Edm.Decimal "Doc. Balance"
PX.Objects.AR.ARStatementDetail.CuryDocBalance : Edm.Decimal "Cury. Doc. Balance"
PX.Objects.AR.ARStatementDetail.StatementType : Edm.String "Statement Type"
PX.Objects.AR.ARStatementDetail.BegBalance : Edm.Decimal [required] "Beg. Balance"
PX.Objects.AR.ARStatementDetail.CuryBegBalance : Edm.Decimal [required] "Curr. Beg. Balance"
PX.Objects.AR.ARStatementDetail.AgeBalance00 : Edm.Decimal [required] "Age00 Balance"
PX.Objects.AR.ARStatementDetail.CuryAgeBalance00 : Edm.Decimal [required] "Cury. Age00 Balance"
PX.Objects.AR.ARStatementDetail.AgeBalance01 : Edm.Decimal [required] "Age01 Balance"
PX.Objects.AR.ARStatementDetail.CuryAgeBalance01 : Edm.Decimal [required] "Cury. Age01 Balance"
PX.Objects.AR.ARStatementDetail.AgeBalance02 : Edm.Decimal [required] "Age02 Balance"
PX.Objects.AR.ARStatementDetail.CuryAgeBalance02 : Edm.Decimal [required] "Cury. Age02 Balance"
PX.Objects.AR.ARStatementDetail.AgeBalance03 : Edm.Decimal [required] "Cury. Age03 Balance"
PX.Objects.AR.ARStatementDetail.CuryAgeBalance03 : Edm.Decimal [required] "Cury. Age03 Balance"
PX.Objects.AR.ARStatementDetail.AgeBalance04 : Edm.Decimal [required] "Age04 Balance"
PX.Objects.AR.ARStatementDetail.CuryAgeBalance04 : Edm.Decimal [required] "Cury. Age04 Balance"
PX.Objects.AR.ARStatementDetail.IsOpen : Edm.Boolean [required]
PX.Objects.AR.ARStatementDetail.RefNoteID : Edm.Guid [key]
PX.Objects.AR.ARStatementDetail.TranPostID : Edm.Int32
PX.Objects.AR.ARStatementDetail.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARStatementDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARStatementDetail.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.ARStatementDetail.ARStatementByStatementDate -> PX.Objects.AR.ARStatement (CustomerID=CustomerID, CuryID=CuryID, StatementDate=StatementDate)
PX.Objects.AR.ARStatementDetail.ARStatementByCuryID -> PX.Objects.AR.ARStatement (CustomerID=CustomerID, StatementDate=StatementDate, CuryID=CuryID)

# PX.Objects.AR.ARStatementDetailInfo (EntityType)

Label: "AR Statement Detail Info"
Key: AdjdDocType, AdjgDocType, AdjgRefNbr, DocType, RefNbr, RefNoteID, SourceDocType, SourceRefNbr, StatementDate
Entity sets: PX_Objects_AR_ARStatementDetailInfo, ARStatementDetailInfo
Non-filterable, non-selectable: PrintDocType, DocExtRefNbr, CuryOrigDocAmtSigned, OrigDocAmtSigned, CuryInitDocBalSigned, InitDocBalSigned, CuryDocBalanceSigned, DocBalanceSigned, IsOrphanApplication, IsInterCurrencyApplication, IsInterBranchApplication, IsInterCustomerApplication, IsInterStatementApplication, AdjgRefNbr, AdjdDocType, AdjdRefNbr, AdjdCuryID, AdjgCuryID, SignBalanceDelta

PX.Objects.AR.ARStatementDetailInfo.ID : Edm.Int32
PX.Objects.AR.ARStatementDetailInfo.StatementDate : Edm.DateTimeOffset [key] "Statement Date"
PX.Objects.AR.ARStatementDetailInfo.IsOpen : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.DocStatementDate : Edm.DateTimeOffset
PX.Objects.AR.ARStatementDetailInfo.DocDesc : Edm.String "Description"
PX.Objects.AR.ARStatementDetailInfo.IsMigratedRecord : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.PrintDocType : Edm.String "Type"
PX.Objects.AR.ARStatementDetailInfo.CuryInfoID : Edm.Int64
PX.Objects.AR.ARStatementDetailInfo.RefNoteID : Edm.Guid [key]
PX.Objects.AR.ARStatementDetailInfo.CuryOrigDocAmt : Edm.Decimal "Amount"
PX.Objects.AR.ARStatementDetailInfo.OrigDocAmt : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.CuryInitDocBal : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.InitDocBal : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.InvoiceNbr : Edm.String "Customer Ref. Nbr."
PX.Objects.AR.ARStatementDetailInfo.DueDate : Edm.DateTimeOffset "Due Date"
PX.Objects.AR.ARStatementDetailInfo.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.AR.ARStatementDetailInfo.DocExtRefNbr : Edm.String "Ext. Ref.#"
PX.Objects.AR.ARStatementDetailInfo.CuryOrigDocAmtSigned : Edm.Decimal "Origin. Amt"
PX.Objects.AR.ARStatementDetailInfo.OrigDocAmtSigned : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.CuryInitDocBalSigned : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.InitDocBalSigned : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.DocBalance : Edm.Decimal "Doc. Balance"
PX.Objects.AR.ARStatementDetailInfo.CuryDocBalance : Edm.Decimal "Cury. Doc. Balance"
PX.Objects.AR.ARStatementDetailInfo.CuryDocBalanceSigned : Edm.Decimal "Amount Due"
PX.Objects.AR.ARStatementDetailInfo.DocBalanceSigned : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.StatementType : Edm.String "Statement Type"
PX.Objects.AR.ARStatementDetailInfo.BegBalance : Edm.Decimal "Beg. Balance"
PX.Objects.AR.ARStatementDetailInfo.CuryBegBalance : Edm.Decimal "Curr. Beg. Balance"
PX.Objects.AR.ARStatementDetailInfo.AgeBalance00 : Edm.Decimal "Age00 Balance"
PX.Objects.AR.ARStatementDetailInfo.CuryAgeBalance00 : Edm.Decimal "Cury. Age00 Balance"
PX.Objects.AR.ARStatementDetailInfo.AgeBalance01 : Edm.Decimal "Age01 Balance"
PX.Objects.AR.ARStatementDetailInfo.CuryAgeBalance01 : Edm.Decimal "Cury. Age01 Balance"
PX.Objects.AR.ARStatementDetailInfo.AgeBalance02 : Edm.Decimal "Age02 Balance"
PX.Objects.AR.ARStatementDetailInfo.CuryAgeBalance02 : Edm.Decimal "Cury. Age02 Balance"
PX.Objects.AR.ARStatementDetailInfo.AgeBalance03 : Edm.Decimal "Cury. Age03 Balance"
PX.Objects.AR.ARStatementDetailInfo.CuryAgeBalance03 : Edm.Decimal "Cury. Age03 Balance"
PX.Objects.AR.ARStatementDetailInfo.AgeBalance04 : Edm.Decimal "Age04 Balance"
PX.Objects.AR.ARStatementDetailInfo.CuryAgeBalance04 : Edm.Decimal "Cury. Age04 Balance"
PX.Objects.AR.ARStatementDetailInfo.Type : Edm.String
PX.Objects.AR.ARStatementDetailInfo.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AR.ARStatementDetailInfo.DocType : Edm.String [key] "Doc. Type"
PX.Objects.AR.ARStatementDetailInfo.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.AR.ARStatementDetailInfo.SourceDocType : Edm.String [key] "Source Doc. Type"
PX.Objects.AR.ARStatementDetailInfo.SourceRefNbr : Edm.String [key] "Source Ref. Nbr."
PX.Objects.AR.ARStatementDetailInfo.CustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARStatementDetailInfo.CuryBalanceAmt : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.BalanceAmt : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.CuryTurnDiscAmt : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.TurnDiscAmt : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.CuryTurnWOAmt : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.RGOLAmt : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.TurnWOAmt : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.TranType : Edm.String
PX.Objects.AR.ARStatementDetailInfo.IsSelfVoidingVoidApplication : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.IsOrphanApplication : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.IsDocumentPresent : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.IsSourceDocumentPresent : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.CuryID : Edm.String
PX.Objects.AR.ARStatementDetailInfo.SourceCuryID : Edm.String
PX.Objects.AR.ARStatementDetailInfo.IsInterCurrencyApplication : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.IsInterBranchApplication : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.SourceCustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARStatementDetailInfo.IsInterCustomerApplication : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.IsInterStatementApplication : Edm.Boolean
PX.Objects.AR.ARStatementDetailInfo.AdjgDocType : Edm.String [key]
PX.Objects.AR.ARStatementDetailInfo.AdjgRefNbr : Edm.String [key]
PX.Objects.AR.ARStatementDetailInfo.AdjdDocType : Edm.String [key]
PX.Objects.AR.ARStatementDetailInfo.AdjdRefNbr : Edm.String
PX.Objects.AR.ARStatementDetailInfo.AdjdCustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARStatementDetailInfo.AdjgCustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARStatementDetailInfo.AdjdCuryID : Edm.String
PX.Objects.AR.ARStatementDetailInfo.AdjgCuryID : Edm.String
PX.Objects.AR.ARStatementDetailInfo.SignBalanceDelta : Edm.Decimal
PX.Objects.AR.ARStatementDetailInfo.BAccountByAdjdCustomerID -> PX.Objects.CR.BAccount (AdjdCustomerID=BAccountID)
PX.Objects.AR.ARStatementDetailInfo.BAccountByAdjgCustomerID -> PX.Objects.CR.BAccount (AdjgCustomerID=BAccountID)
PX.Objects.AR.ARStatementDetailInfo.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARStatementDetailInfo.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARStatementDetailInfo.BranchByAdjdbranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARStatementDetailInfo.BranchByAdjgbranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARStatementDetailInfo.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARStatementDetailInfo.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.ARStatementDetailInfo.ARStatementByStatementDate -> PX.Objects.AR.ARStatement (CustomerID=CustomerID, CuryID=CuryID, StatementDate=StatementDate)

# PX.Objects.AR.ARTax (EntityType)

Label: "AR Tax Detail"
Key: LineNbr, RefNbr, TaxID, TranType
Entity sets: PX_Objects_AR_ARTax, ARTaxDetail, ARTax
Non-filterable, non-selectable: NonDeductibleTaxRate, CuryTaxDiscountAmt, TaxDiscountAmt

PX.Objects.AR.ARTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.AR.ARTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.AR.ARTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.AR.ARTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARTax.CreatedByScreenID : Edm.String
PX.Objects.AR.ARTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARTax.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARTax.TranType : Edm.String [key] "Tran. Type"
PX.Objects.AR.ARTax.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AR.ARTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.AR.ARTax.CuryInfoID : Edm.Int64
PX.Objects.AR.ARTax.CuryOrigTaxableAmt : Edm.Decimal
PX.Objects.AR.ARTax.OrigTaxableAmt : Edm.Decimal
PX.Objects.AR.ARTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.AR.ARTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.AR.ARTax.CuryTaxableDiscountAmt : Edm.Decimal [required]
PX.Objects.AR.ARTax.TaxableDiscountAmt : Edm.Decimal [required]
PX.Objects.AR.ARTax.CuryTaxDiscountAmt : Edm.Decimal
PX.Objects.AR.ARTax.TaxDiscountAmt : Edm.Decimal
PX.Objects.AR.ARTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.AR.ARTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.AR.ARTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.AR.ARTax.RetainedTaxableAmt : Edm.Decimal [required] "Retained Taxable Amount"
PX.Objects.AR.ARTax.RetainedTaxAmt : Edm.Decimal [required] "Retained Tax"
PX.Objects.AR.ARTax.tstamp : Edm.Binary
PX.Objects.AR.ARTax.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTax.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.AR.ARTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.AR.ARTax.ARTranByLineNbr -> PX.Objects.AR.ARTran (TranType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)
PX.Objects.AR.ARTax.APTranByLineNbr -> PX.Objects.AP.APTran (TranType=TranType, RefNbr=RefNbr, LineNbr=LineNbr)

# PX.Objects.AR.ARTaxTran (EntityType)

Label: "AR Tax"
BaseType: PX.Objects.TX.TaxTran
Key: Module, RecordID (inherited from PX.Objects.TX.TaxTran)
Entity sets: PX_Objects_AR_ARTaxTran, ARTax1, ARTaxTran
Non-filterable, non-selectable: CuryTaxableDiscountAmt, TaxableDiscountAmt, CuryDiscountedTaxableAmt, DiscountedTaxableAmt, CuryDiscountedPrice, DiscountedPrice

PX.Objects.AR.ARTaxTran.BranchID : Edm.Int32 "Branch"
PX.Objects.AR.ARTaxTran.CuryTaxableDiscountAmt : Edm.Decimal
PX.Objects.AR.ARTaxTran.TaxableDiscountAmt : Edm.Decimal
PX.Objects.AR.ARTaxTran.CuryTaxDiscountAmt : Edm.Decimal
PX.Objects.AR.ARTaxTran.TaxDiscountAmt : Edm.Decimal
PX.Objects.AR.ARTaxTran.CuryDiscountedTaxableAmt : Edm.Decimal "Discounted Taxable Amount"
PX.Objects.AR.ARTaxTran.DiscountedTaxableAmt : Edm.Decimal
PX.Objects.AR.ARTaxTran.CuryDiscountedPrice : Edm.Decimal "Tax on Discounted Price"
PX.Objects.AR.ARTaxTran.DiscountedPrice : Edm.Decimal

# PX.Objects.AR.ARTran (EntityType)

Label: "AR Transactions"
Key: LineNbr, RefNbr, TranType
Entity sets: PX_Objects_AR_ARTran, ARTransactions, ARTran
Non-filterable, non-selectable: IsFree, CalculateDiscountsOnImport, CostBasisNull, CuryInventoryID, ReleasedToVerify, AllowControlAccountForModule, NoteText, RequireINUpdate, FreezeManualDisc, RequiresTerms, ItemHasResidual, UnassignedQty

PX.Objects.AR.ARTran.BranchID : Edm.Int32 "Branch"
PX.Objects.AR.ARTran.TranType : Edm.String [key] "Tran. Type"
PX.Objects.AR.ARTran.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.AR.ARTran.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.AR.ARTran.SortOrder : Edm.Int32 "Line Nbr."
PX.Objects.AR.ARTran.SOOrderType : Edm.String "Order Type"
PX.Objects.AR.ARTran.SOOrderNbr : Edm.String "Order Nbr."
PX.Objects.AR.ARTran.SOOrderLineNbr : Edm.Int32 "Order Line Nbr"
PX.Objects.AR.ARTran.SOOrderLineOperation : Edm.String
PX.Objects.AR.ARTran.SOOrderSortOrder : Edm.Int32 "Order Sort Order"
PX.Objects.AR.ARTran.SOOrderLineSign : Edm.Int16
PX.Objects.AR.ARTran.SOShipmentType : Edm.String
PX.Objects.AR.ARTran.SOShipmentNbr : Edm.String "Shipment Nbr."
PX.Objects.AR.ARTran.SOShipmentLineGroupNbr : Edm.Int32
PX.Objects.AR.ARTran.SOShipmentLineNbr : Edm.Int32
PX.Objects.AR.ARTran.CustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARTran.LineType : Edm.String "Line Type"
PX.Objects.AR.ARTran.IsFree : Edm.Boolean
PX.Objects.AR.ARTran.ProjectID : Edm.Int32 "Project"
PX.Objects.AR.ARTran.PMDeltaOption : Edm.String
PX.Objects.AR.ARTran.ExpenseDate : Edm.DateTimeOffset
PX.Objects.AR.ARTran.CuryInfoID : Edm.Int64
PX.Objects.AR.ARTran.ManualPrice : Edm.Boolean "Manual Price"
PX.Objects.AR.ARTran.InvtMult : Edm.Int16 [required] "Multiplier"
PX.Objects.AR.ARTran.IsStockItem : Edm.Boolean "Is stock"
PX.Objects.AR.ARTran.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AR.ARTran.TaxID : Edm.String "Tax ID"
PX.Objects.AR.ARTran.DeferredCode : Edm.String "Deferral Code"
PX.Objects.AR.ARTran.SiteID : Edm.Int32
PX.Objects.AR.ARTran.UOM : Edm.String "UOM"
PX.Objects.AR.ARTran.Qty : Edm.Decimal "Quantity"
PX.Objects.AR.ARTran.BaseQty : Edm.Decimal "Base Qty."
PX.Objects.AR.ARTran.UnitCost : Edm.Decimal
PX.Objects.AR.ARTran.TranCost : Edm.Decimal [required] "Ext. Cost"
PX.Objects.AR.ARTran.TranCostOrig : Edm.Decimal [required] "Orig. Ext. Cost"
PX.Objects.AR.ARTran.IsTranCostFinal : Edm.Boolean [required]
PX.Objects.AR.ARTran.CostCenterID : Edm.Int32 [required]
PX.Objects.AR.ARTran.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.AR.ARTran.UnitPrice : Edm.Decimal
PX.Objects.AR.ARTran.CuryExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.AR.ARTran.ExtPrice : Edm.Decimal
PX.Objects.AR.ARTran.CalculateDiscountsOnImport : Edm.Boolean "Calculate automatic discounts on import"
PX.Objects.AR.ARTran.DiscPct : Edm.Decimal "Discount Percent"
PX.Objects.AR.ARTran.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.AR.ARTran.DiscAmt : Edm.Decimal
PX.Objects.AR.ARTran.ManualDisc : Edm.Boolean "Manual Discount"
PX.Objects.AR.ARTran.AutomaticDiscountsDisabled : Edm.Boolean [required] "Automatic Discounts Disabled"
PX.Objects.AR.ARTran.OrigLineNbr : Edm.Int32
PX.Objects.AR.ARTran.OrigGroupDiscountRate : Edm.Decimal [required]
PX.Objects.AR.ARTran.OrigDocumentDiscountRate : Edm.Decimal [required]
PX.Objects.AR.ARTran.GroupDiscountRate : Edm.Decimal
PX.Objects.AR.ARTran.DocumentDiscountRate : Edm.Decimal [required]
PX.Objects.AR.ARTran.SkipLineDiscounts : Edm.Boolean [required] "Ignore Automatic Line Discounts"
PX.Objects.AR.ARTran.RetainagePct : Edm.Decimal [required] "RetainagePct"
PX.Objects.AR.ARTran.CuryRetainageAmt : Edm.Decimal [required] "CuryRetainageAmt"
PX.Objects.AR.ARTran.RetainageAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.CuryTranAmt : Edm.Decimal "Amount"
PX.Objects.AR.ARTran.TranAmt : Edm.Decimal
PX.Objects.AR.ARTran.AccrueCost : Edm.Boolean "Accrue Cost"
PX.Objects.AR.ARTran.CostBasis : Edm.String
PX.Objects.AR.ARTran.CostBasisNull : Edm.String "Cost Based On"
PX.Objects.AR.ARTran.CuryInventoryID : Edm.Int32
PX.Objects.AR.ARTran.CuryAccruedCost : Edm.Decimal [required] "Cost Accrual"
PX.Objects.AR.ARTran.AccruedCost : Edm.Decimal [required]
PX.Objects.AR.ARTran.TaxableAmt : Edm.Decimal
PX.Objects.AR.ARTran.CuryTaxAmt : Edm.Decimal "VAT"
PX.Objects.AR.ARTran.TaxAmt : Edm.Decimal
PX.Objects.AR.ARTran.OrigTaxableAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.OrigTaxAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.RetainedTaxableAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.RetainedTaxAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.CashDiscBal : Edm.Decimal [required]
PX.Objects.AR.ARTran.OrigRetainageAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.RetainageBal : Edm.Decimal [required]
PX.Objects.AR.ARTran.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.AR.ARTran.OrigRefNbr : Edm.String "Orig. Ref. Nbr."
PX.Objects.AR.ARTran.OrigTranAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.TranBal : Edm.Decimal [required] "Balance"
PX.Objects.AR.ARTran.TranClass : Edm.String
PX.Objects.AR.ARTran.DrCr : Edm.String
PX.Objects.AR.ARTran.TranDate : Edm.DateTimeOffset "Document Date"
PX.Objects.AR.ARTran.OrigInvoiceDate : Edm.DateTimeOffset "Original Invoice date"
PX.Objects.AR.ARTran.FinPeriodID : Edm.String
PX.Objects.AR.ARTran.TranPeriodID : Edm.String
PX.Objects.AR.ARTran.TranDesc : Edm.String "Transaction Descr."
PX.Objects.AR.ARTran.ReleasedToVerify : Edm.Boolean
PX.Objects.AR.ARTran.Released : Edm.Boolean [required]
PX.Objects.AR.ARTran.SalesPersonID : Edm.Int32 "Salesperson ID"
PX.Objects.AR.ARTran.EmployeeID : Edm.Int32
PX.Objects.AR.ARTran.CommnPct : Edm.Decimal [required]
PX.Objects.AR.ARTran.CuryCommnAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.CommnAmt : Edm.Decimal [required]
PX.Objects.AR.ARTran.DefScheduleID : Edm.Int32 "Original Deferral Schedule"
PX.Objects.AR.ARTran.DisableAutomaticTaxCalculation : Edm.Boolean [required] "Disable Automatic Tax Calculation"
PX.Objects.AR.ARTran.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.AR.ARTran.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.AR.ARTran.ReasonCode : Edm.String "Reason Code"
PX.Objects.AR.ARTran.AllowControlAccountForModule : Edm.String
PX.Objects.AR.ARTran.tstamp : Edm.Binary
PX.Objects.AR.ARTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.ARTran.CreatedByScreenID : Edm.String
PX.Objects.AR.ARTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.ARTran.LastModifiedByScreenID : Edm.String
PX.Objects.AR.ARTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.ARTran.NoteID : Edm.Guid
PX.Objects.AR.ARTran.NoteText : Edm.String "Note Text"
PX.Objects.AR.ARTran.Commissionable : Edm.Boolean "Commissionable"
PX.Objects.AR.ARTran.Date : Edm.DateTimeOffset "Expense Date"
PX.Objects.AR.ARTran.CaseCD : Edm.String "Case ID"
PX.Objects.AR.ARTran.RequireINUpdate : Edm.Boolean
PX.Objects.AR.ARTran.FreezeManualDisc : Edm.Boolean
PX.Objects.AR.ARTran.DiscountID : Edm.String "Discount Code"
PX.Objects.AR.ARTran.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.AR.ARTran.DRTermStartDate : Edm.DateTimeOffset "Term Start Date"
PX.Objects.AR.ARTran.DRTermEndDate : Edm.DateTimeOffset "Term End Date"
PX.Objects.AR.ARTran.RequiresTerms : Edm.Boolean
PX.Objects.AR.ARTran.CuryUnitPriceDR : Edm.Decimal "Unit Price for DR"
PX.Objects.AR.ARTran.DiscPctDR : Edm.Decimal "Discount Percent for DR"
PX.Objects.AR.ARTran.ItemHasResidual : Edm.Boolean
PX.Objects.AR.ARTran.GroupDiscountAmount : Edm.Decimal "Group Discount Amount"
PX.Objects.AR.ARTran.DocumentDiscountAmount : Edm.Decimal "Document Discount Amount"
PX.Objects.AR.ARTran.GrossSalesAmount : Edm.Decimal "Gross Sales Amount"
PX.Objects.AR.ARTran.Cost : Edm.Decimal "Cost"
PX.Objects.AR.ARTran.NetSalesAmount : Edm.Decimal "Net Sales Amount"
PX.Objects.AR.ARTran.Margin : Edm.Decimal "Margin"
PX.Objects.AR.ARTran.MarginPercent : Edm.Decimal "Margin Percent"
PX.Objects.AR.ARTran.UnassignedQty : Edm.Decimal
PX.Objects.AR.ARTran.PlanID : Edm.Int64
PX.Objects.AR.ARTran.OrigInvoiceType : Edm.String "Orig. Inv. Type"
PX.Objects.AR.ARTran.OrigInvoiceNbr : Edm.String "Orig. Inv. Nbr."
PX.Objects.AR.ARTran.OrigInvoiceLineNbr : Edm.Int32 "Orig. Inv. Line Nbr."
PX.Objects.AR.ARTran.InvtDocType : Edm.String "Inventory Doc. Type"
PX.Objects.AR.ARTran.InvtRefNbr : Edm.String "Inventory Ref. Nbr."
PX.Objects.AR.ARTran.InvtReleased : Edm.Boolean [required]
PX.Objects.AR.ARTran.IsCancellation : Edm.Boolean
PX.Objects.AR.ARTran.Canceled : Edm.Boolean [required]
PX.Objects.AR.ARTran.SubstitutionRequired : Edm.Boolean [required] "Substitution Required"
PX.Objects.AR.ARTran.BlanketType : Edm.String
PX.Objects.AR.ARTran.BlanketNbr : Edm.String "Blanket SO Ref. Nbr."
PX.Objects.AR.ARTran.BlanketLineNbr : Edm.Int32
PX.Objects.AR.ARTran.BlanketSplitLineNbr : Edm.Int32
PX.Objects.AR.ARTran.RelatedDocumentType : Edm.String "Related Document Type"
PX.Objects.AR.ARTran.RelatedDocumentID : Edm.Guid "Related Document"
PX.Objects.AR.ARTran.RelatedDocumentLineNbr : Edm.Int32 "Related Document Detail Line Nbr."
PX.Objects.AR.ARTran.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.AR.ARTran.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTran.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.AR.ARTran.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.AR.ARTran.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARTran.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARTran.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTran.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AR.ARTran.DRDeferredCodeByDeferredCode -> PX.Objects.DR.DRDeferredCode (DeferredCode=DeferredCodeID)
PX.Objects.AR.ARTran.SOOrderBySOOrderNbr -> PX.Objects.SO.SOOrder (SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.AR.ARTran.SOOrderBySOOrderType -> PX.Objects.SO.SOOrder (SOOrderNbr=OrderNbr, SOOrderType=OrderType)
PX.Objects.AR.ARTran.SOOrderByBlanketType -> PX.Objects.SO.SOOrder (BlanketNbr=OrderNbr, BlanketType=OrderType)
PX.Objects.AR.ARTran.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTran.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.ARTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.ARTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.ARTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.AR.ARTran.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.AR.ARTran.SOBlanketOrderLinkBySOOrderNbr -> PX.Objects.SO.SOBlanketOrderLink (BlanketType=BlanketType, BlanketNbr=BlanketNbr, SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.AR.ARTran.SOLineBySOOrderLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOOrderLineNbr=LineNbr)
PX.Objects.AR.ARTran.SOOrderShipmentBySOOrderNbr -> PX.Objects.SO.SOOrderShipment (SOShipmentType=ShipmentType, SOShipmentNbr=ShipmentNbr, SOOrderType=OrderType, SOOrderNbr=OrderNbr)
PX.Objects.AR.ARTran.SOOrderShipmentBySOShipmentType -> PX.Objects.SO.SOOrderShipment (SOShipmentNbr=ShipmentNbr, SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOShipmentType=ShipmentType)
PX.Objects.AR.ARTran.SOOrderTypeBySOOrderType -> PX.Objects.SO.SOOrderType (SOOrderType=OrderType)
PX.Objects.AR.ARTran.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.AR.ARTran.DRScheduleByTranType -> PX.Objects.DR.DRSchedule (DefScheduleID=ScheduleID, TranType=DocType)
PX.Objects.AR.ARTran.ReasonCodeByReasonCode -> PX.Objects.CS.ReasonCode (ReasonCode=ReasonCodeID)
PX.Objects.AR.ARTran.INLocationBySiteID -> PX.Objects.IN.INLocation (SiteID=SiteID)
PX.Objects.AR.ARTran.INRegisterByInvtDocType -> PX.Objects.IN.INRegister (InvtRefNbr=RefNbr, InvtDocType=DocType)
PX.Objects.AR.ARTran.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AR.ARTran.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.AR.ARTran.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AR.ARTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARTran.AccountByExpenseAccrualAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARTran.AccountByExpenseAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARTran.SubByExpenseAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARTran.SubByExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARTran.CRCaseByCaseCD -> PX.Objects.CR.CRCase (CaseCD=CaseCD)
PX.Objects.AR.ARTran.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.AR.ARTran.ARSalesPerTranBySalesPersonID -> PX.Objects.AR.ARSalesPerTran (TranType=DocType, RefNbr=RefNbr, SalesPersonID=SalespersonID)
PX.Objects.AR.ARTran.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.AR.ARTran.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTran.SOInvoiceByOrigInvoiceType -> PX.Objects.SO.SOInvoice (OrigInvoiceNbr=RefNbr, OrigInvoiceType=DocType)
PX.Objects.AR.ARTran.INLotSerialStatusByCostCenterByLocationID -> PX.Objects.IN.INLotSerialStatusByCostCenter (InventoryID=InventoryID)
PX.Objects.AR.ARTran.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AR.ARTran.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.AR.ARTran.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.ARTran.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.AR.ARTran.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.AR.ARTran.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.AR.ARTran.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.AR.ARTran.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.AR.ARTran.ARFinChargeTranCollection -> Collection(PX.Objects.AR.ARFinChargeTran)

# PX.Objects.AR.ARTranAccrueCost (EntityType)

Key: LineNbr, RefNbr, TranType
Entity sets: PX_Objects_AR_ARTranAccrueCost
Non-filterable, non-selectable: IsStockItem

PX.Objects.AR.ARTranAccrueCost.BranchID : Edm.Int32
PX.Objects.AR.ARTranAccrueCost.TranType : Edm.String [key]
PX.Objects.AR.ARTranAccrueCost.RefNbr : Edm.String [key]
PX.Objects.AR.ARTranAccrueCost.LineNbr : Edm.Int32 [key]
PX.Objects.AR.ARTranAccrueCost.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.AR.ARTranAccrueCost.IsStockItem : Edm.Boolean
PX.Objects.AR.ARTranAccrueCost.UOM : Edm.String "UOM"
PX.Objects.AR.ARTranAccrueCost.Qty : Edm.Decimal
PX.Objects.AR.ARTranAccrueCost.BaseQty : Edm.Decimal
PX.Objects.AR.ARTranAccrueCost.AccrueCost : Edm.Boolean
PX.Objects.AR.ARTranAccrueCost.CostBasis : Edm.String
PX.Objects.AR.ARTranAccrueCost.CuryAccruedCost : Edm.Decimal
PX.Objects.AR.ARTranAccrueCost.AccruedCost : Edm.Decimal
PX.Objects.AR.ARTranAccrueCost.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranAccrueCost.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranAccrueCost.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranAccrueCost.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranAccrueCost.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.ARTranAccrueCost.DRScheduleByTranType -> PX.Objects.DR.DRSchedule (TranType=DocType)
PX.Objects.AR.ARTranAccrueCost.SOInvoiceByOrigInvoiceType -> PX.Objects.SO.SOInvoice
PX.Objects.AR.ARTranAccrueCost.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.AR.ARTranAccrueCost.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.AR.ARTranAccrueCost.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.ARTranAccrueCost.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.AR.ARTranAccrueCost.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.AR.ARTranAccrueCost.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.AR.ARTranAccrueCost.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.AR.ARTranAccrueCost.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.AR.ARTranAccrueCost.ARFinChargeTranCollection -> Collection(PX.Objects.AR.ARFinChargeTran)

# PX.Objects.AR.ARTranPost (EntityType)

Label: "AR Document transaction"
Key: DocType, ID, RefNbr
Entity sets: PX_Objects_AR_ARTranPost, ARDocumenttransaction, ARTranPost
Non-filterable, non-selectable: IsVoidPrepayment

PX.Objects.AR.ARTranPost.BranchID : Edm.Int32 "Branch"
PX.Objects.AR.ARTranPost.DocType : Edm.String [key] "Doc. Type"
PX.Objects.AR.ARTranPost.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.AR.ARTranPost.ID : Edm.Int32 [key]
PX.Objects.AR.ARTranPost.AdjNbr : Edm.Int32
PX.Objects.AR.ARTranPost.RefNoteID : Edm.Guid
PX.Objects.AR.ARTranPost.SourceDocType : Edm.String "Source Doc. Type"
PX.Objects.AR.ARTranPost.SourceRefNbr : Edm.String "Source Ref. Nbr."
PX.Objects.AR.ARTranPost.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AR.ARTranPost.CustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARTranPost.FinPeriodID : Edm.String "Application Period"
PX.Objects.AR.ARTranPost.TranPeriodID : Edm.String
PX.Objects.AR.ARTranPost.CuryInfoID : Edm.Int64
PX.Objects.AR.ARTranPost.BatchNbr : Edm.String "Batch Nbr."
PX.Objects.AR.ARTranPost.CuryAmt : Edm.Decimal "Amount"
PX.Objects.AR.ARTranPost.CuryPPDAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AR.ARTranPost.CuryDiscAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.AR.ARTranPost.CuryRetainageAmt : Edm.Decimal
PX.Objects.AR.ARTranPost.CuryWOAmt : Edm.Decimal [required] "Write-Off Amount"
PX.Objects.AR.ARTranPost.CuryItemDiscAmt : Edm.Decimal [required]
PX.Objects.AR.ARTranPost.Amt : Edm.Decimal
PX.Objects.AR.ARTranPost.PPDAmt : Edm.Decimal
PX.Objects.AR.ARTranPost.DiscAmt : Edm.Decimal
PX.Objects.AR.ARTranPost.RetainageAmt : Edm.Decimal
PX.Objects.AR.ARTranPost.WOAmt : Edm.Decimal [required]
PX.Objects.AR.ARTranPost.ItemDiscAmt : Edm.Decimal [required]
PX.Objects.AR.ARTranPost.RGOLAmt : Edm.Decimal
PX.Objects.AR.ARTranPost.IsMigratedRecord : Edm.Boolean
PX.Objects.AR.ARTranPost.IsVoidPrepayment : Edm.Boolean
PX.Objects.AR.ARTranPost.Type : Edm.String "Transaction type"
PX.Objects.AR.ARTranPost.TranType : Edm.String "Tran. Type"
PX.Objects.AR.ARTranPost.TranRefNbr : Edm.String "Tran. Ref. Nbr."
PX.Objects.AR.ARTranPost.ReferenceID : Edm.Int32 "Customer"
PX.Objects.AR.ARTranPost.BalanceSign : Edm.Int16
PX.Objects.AR.ARTranPost.GLSign : Edm.Int16
PX.Objects.AR.ARTranPost.TranClass : Edm.String
PX.Objects.AR.ARTranPost.StatementDate : Edm.DateTimeOffset
PX.Objects.AR.ARTranPost.VoidAdjNbr : Edm.Int32
PX.Objects.AR.ARTranPost.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranPost.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARTranPost.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.AR.ARTranPost.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARTranPost.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.AR.ARTranPost.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranPost.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranPost.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.ARTranPost.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARTranPost.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARTranPost.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARTranPost.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (DocType=DocType, RefNbr=RefNbr)

# PX.Objects.AR.ARTranPostGL (EntityType)

Label: "AR Document Post GL"
Key: DocType, ID, RefNbr
Entity sets: PX_Objects_AR_ARTranPostGL, ARDocumentPostGL, ARTranPostGL

PX.Objects.AR.ARTranPostGL.DocType : Edm.String [key] "Doc. Type"
PX.Objects.AR.ARTranPostGL.RefNbr : Edm.String [key] "Ref. Nbr."
PX.Objects.AR.ARTranPostGL.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.AR.ARTranPostGL.ID : Edm.Int32 [key]
PX.Objects.AR.ARTranPostGL.AdjNbr : Edm.Int32
PX.Objects.AR.ARTranPostGL.RefNoteID : Edm.Guid
PX.Objects.AR.ARTranPostGL.SourceDocType : Edm.String "Source Doc. Type"
PX.Objects.AR.ARTranPostGL.SourceRefNbr : Edm.String "Source Ref. Nbr."
PX.Objects.AR.ARTranPostGL.CuryID : Edm.String
PX.Objects.AR.ARTranPostGL.CuryInfoID : Edm.Int64
PX.Objects.AR.ARTranPostGL.DocDate : Edm.DateTimeOffset "Date"
PX.Objects.AR.ARTranPostGL.CustomerID : Edm.Int32 "Customer"
PX.Objects.AR.ARTranPostGL.FinPeriodID : Edm.String "Application Period"
PX.Objects.AR.ARTranPostGL.TranPeriodID : Edm.String
PX.Objects.AR.ARTranPostGL.BalanceSign : Edm.Int16
PX.Objects.AR.ARTranPostGL.BatchNbr : Edm.String "Batch Number"
PX.Objects.AR.ARTranPostGL.Type : Edm.String
PX.Objects.AR.ARTranPostGL.TranClass : Edm.String
PX.Objects.AR.ARTranPostGL.TranType : Edm.String
PX.Objects.AR.ARTranPostGL.TranRefNbr : Edm.String
PX.Objects.AR.ARTranPostGL.ReferenceID : Edm.Int32
PX.Objects.AR.ARTranPostGL.IsMigratedRecord : Edm.Boolean
PX.Objects.AR.ARTranPostGL.RGOLAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryBalanceAmt : Edm.Decimal "Balance"
PX.Objects.AR.ARTranPostGL.BalanceAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryDebitARAmt : Edm.Decimal "Debit AR Amt."
PX.Objects.AR.ARTranPostGL.DebitARAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryCreditARAmt : Edm.Decimal "Credit AR Amt."
PX.Objects.AR.ARTranPostGL.CreditARAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryTurnAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.TurnAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryTurnDiscAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.TurnDiscAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryTurnItemDiscAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.TurnItemDiscAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryTurnWOAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.TurnWOAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryTurnRetainageAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.TurnRetainageAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryRetainageReleasedAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.RetainageReleasedAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryRetainageUnreleasedAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.RetainageUnreleasedAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.CuryRetainagePaidTotal : Edm.Decimal
PX.Objects.AR.ARTranPostGL.RetainagePaidTotal : Edm.Decimal
PX.Objects.AR.ARTranPostGL.TurnRGOLAmt : Edm.Decimal
PX.Objects.AR.ARTranPostGL.StatementDate : Edm.DateTimeOffset
PX.Objects.AR.ARTranPostGL.VoidAdjNbr : Edm.Int32
PX.Objects.AR.ARTranPostGL.GLSign : Edm.Int16
PX.Objects.AR.ARTranPostGL.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranPostGL.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.ARTranPostGL.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranPostGL.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranPostGL.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.AR.ARTranPostGL.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.AR.ARTranPostGL.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.AR.ARTranPostGL.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.AR.ARTranPostGL.SOInvoiceByRefNbr -> PX.Objects.SO.SOInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ARTranPostGL.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.ARTranPostGL.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.AR.ARTranPostGL.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)

# PX.Objects.AR.BalancedARDocument (EntityType)

Label: "AR Document"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_BalancedARDocument
Non-filterable, non-selectable: CustomerRefNbr

PX.Objects.AR.BalancedARDocument.InvoiceNbr : Edm.String
PX.Objects.AR.BalancedARDocument.ExtRefNbr : Edm.String
PX.Objects.AR.BalancedARDocument.CustomerRefNbr : Edm.String "Customer Order Nbr."
PX.Objects.AR.BalancedARDocument.PaymentMethodID : Edm.String "Payment Method"

# PX.Objects.AR.BaseARHistoryByPeriod (EntityType)

Label: "Base AR History by Period"
Key: AccountID, BranchID, CustomerID, FinPeriodID, SubID
Entity sets: PX_Objects_AR_BaseARHistoryByPeriod, BaseARHistorybyPeriod

PX.Objects.AR.BaseARHistoryByPeriod.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.AR.BaseARHistoryByPeriod.CustomerID : Edm.Int32 [key] "Customer"
PX.Objects.AR.BaseARHistoryByPeriod.AccountID : Edm.Int32 [key] "Account"
PX.Objects.AR.BaseARHistoryByPeriod.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.AR.BaseARHistoryByPeriod.LastActivityPeriod : Edm.String
PX.Objects.AR.BaseARHistoryByPeriod.FinPeriodID : Edm.String [key]

# PX.Objects.AR.CCProcTran (EntityType)

Label: "Credit Card Processing Transaction"
Key: TranNbr
Entity sets: PX_Objects_AR_CCProcTran, CreditCardProcessingTransaction, CCProcTran
Non-filterable, non-selectable: FundHoldExpDate, PCTranApiNumber, CommerceTranNumber, TerminalID, MaskedCardNumber, DeletedDatabaseRecord

PX.Objects.AR.CCProcTran.TranNbr : Edm.Int32 [key] "Tran. Nbr."
PX.Objects.AR.CCProcTran.TransactionID : Edm.Int32 "Ext. Tran. ID"
PX.Objects.AR.CCProcTran.PMInstanceID : Edm.Int32
PX.Objects.AR.CCProcTran.ProcessingCenterID : Edm.String "Proc. Center"
PX.Objects.AR.CCProcTran.DocType : Edm.String "Doc. Type"
PX.Objects.AR.CCProcTran.RefNbr : Edm.String "Doc. Reference Nbr."
PX.Objects.AR.CCProcTran.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.AR.CCProcTran.OrigRefNbr : Edm.String "Orig. Doc. Ref. Nbr."
PX.Objects.AR.CCProcTran.TranType : Edm.String "Tran. Type"
PX.Objects.AR.CCProcTran.ProcStatus : Edm.String "Proc. Status"
PX.Objects.AR.CCProcTran.TranStatus : Edm.String "Tran. Status"
PX.Objects.AR.CCProcTran.CVVVerificationStatus : Edm.String "CVV Verification"
PX.Objects.AR.CCProcTran.CuryID : Edm.String "Currency"
PX.Objects.AR.CCProcTran.Amount : Edm.Decimal [required] "Tran. Amount"
PX.Objects.AR.CCProcTran.SubtotalAmount : Edm.Decimal "Subtotal Amount"
PX.Objects.AR.CCProcTran.Tax : Edm.Decimal "Tax"
PX.Objects.AR.CCProcTran.FundHoldExpDate : Edm.DateTimeOffset "Expire On (Est.)"
PX.Objects.AR.CCProcTran.RefTranNbr : Edm.Int32 "Referenced Tran. Nbr."
PX.Objects.AR.CCProcTran.RefPCTranNumber : Edm.String "Proc. Center Ref. Tran. Nbr."
PX.Objects.AR.CCProcTran.PCTranNumber : Edm.String "Proc. Center Tran. Nbr."
PX.Objects.AR.CCProcTran.PCTranApiNumber : Edm.String
PX.Objects.AR.CCProcTran.CommerceTranNumber : Edm.String
PX.Objects.AR.CCProcTran.AuthNumber : Edm.String "Proc. Center Auth. Nbr."
PX.Objects.AR.CCProcTran.TerminalID : Edm.String "Terminal ID"
PX.Objects.AR.CCProcTran.PCResponseCode : Edm.String
PX.Objects.AR.CCProcTran.PCResponseReasonCode : Edm.String
PX.Objects.AR.CCProcTran.PCResponseReasonText : Edm.String "Proc. Center Response Reason"
PX.Objects.AR.CCProcTran.PCResponse : Edm.String
PX.Objects.AR.CCProcTran.StartTime : Edm.DateTimeOffset "Tran. Time"
PX.Objects.AR.CCProcTran.EndTime : Edm.DateTimeOffset
PX.Objects.AR.CCProcTran.ExpirationDate : Edm.DateTimeOffset
PX.Objects.AR.CCProcTran.ErrorSource : Edm.String "Error Source"
PX.Objects.AR.CCProcTran.ErrorText : Edm.String "Error Text"
PX.Objects.AR.CCProcTran.MaskedCardNumber : Edm.String "Card/Account Nbr."
PX.Objects.AR.CCProcTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.CCProcTran.CreatedByScreenID : Edm.String
PX.Objects.AR.CCProcTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.CCProcTran.Imported : Edm.Boolean [required] "Imported"
PX.Objects.AR.CCProcTran.tstamp : Edm.Binary
PX.Objects.AR.CCProcTran.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AR.CCProcTran.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.CCProcTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.CCProcTran.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.CCProcTran.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.AR.CCProcTran.CCProcTranByTranNbr -> PX.Objects.AR.CCProcTran (TranNbr=RefTranNbr)
PX.Objects.AR.CCProcTran.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.AR.CCProcTran.ExternalTransactionByTransactionID -> PX.Objects.AR.ExternalTransaction (TransactionID=TransactionID)
PX.Objects.AR.CCProcTran.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)

# PX.Objects.AR.CuryARHistory (EntityType)

Label: "Currency AR History"
Key: AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID
Entity sets: PX_Objects_AR_CuryARHistory, CurrencyARHistory, CuryARHistory
Non-filterable, non-selectable: FinFlag, PtdCrAdjustments, PtdDrAdjustments, PtdSales, PtdPayments, PtdDiscounts, YtdBalance, BegBalance, PtdCOGS, PtdRGOL, PtdFinCharges, PtdDeposits, YtdDeposits, PtdItemDiscounts, CuryPtdCrAdjustments, CuryPtdDrAdjustments, CuryPtdSales, CuryPtdPayments, CuryPtdDiscounts, CuryPtdFinCharges, CuryYtdBalance, CuryBegBalance, CuryPtdDeposits, CuryYtdDeposits, PtdRetainageWithheld, YtdRetainageWithheld, CuryPtdRetainageWithheld, CuryYtdRetainageWithheld, PtdRetainageReleased, YtdRetainageReleased, CuryPtdRetainageReleased, CuryYtdRetainageReleased

PX.Objects.AR.CuryARHistory.BranchID : Edm.Int32 [key]
PX.Objects.AR.CuryARHistory.AccountID : Edm.Int32 [key]
PX.Objects.AR.CuryARHistory.SubID : Edm.Int32 [key]
PX.Objects.AR.CuryARHistory.FinPeriodID : Edm.String [key]
PX.Objects.AR.CuryARHistory.CustomerID : Edm.Int32 [key]
PX.Objects.AR.CuryARHistory.CuryID : Edm.String [key] "Currency ID"
PX.Objects.AR.CuryARHistory.DetDeleted : Edm.Boolean [required]
PX.Objects.AR.CuryARHistory.FinPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdSales : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdPayments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdDiscounts : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinYtdBalance : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinBegBalance : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdCOGS : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdRGOL : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdFinCharges : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdRevalued : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinPtdDeposits : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinYtdDeposits : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdSales : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdPayments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdDiscounts : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranYtdBalance : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranBegBalance : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdRGOL : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdCOGS : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdFinCharges : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdDeposits : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranYtdDeposits : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinPtdSales : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinPtdPayments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinPtdDiscounts : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinPtdFinCharges : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinYtdBalance : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinBegBalance : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinPtdDeposits : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinYtdDeposits : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdDrAdjustments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdCrAdjustments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdSales : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdPayments : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdDiscounts : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdFinCharges : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranYtdBalance : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranBegBalance : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdDeposits : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranYtdDeposits : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.tstamp : Edm.Binary
PX.Objects.AR.CuryARHistory.FinFlag : Edm.Boolean
PX.Objects.AR.CuryARHistory.PtdCrAdjustments : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdDrAdjustments : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdSales : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdPayments : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdDiscounts : Edm.Decimal
PX.Objects.AR.CuryARHistory.YtdBalance : Edm.Decimal
PX.Objects.AR.CuryARHistory.BegBalance : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdCOGS : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdRGOL : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdFinCharges : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdDeposits : Edm.Decimal
PX.Objects.AR.CuryARHistory.YtdDeposits : Edm.Decimal
PX.Objects.AR.CuryARHistory.PtdItemDiscounts : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryPtdCrAdjustments : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryPtdDrAdjustments : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryPtdSales : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryPtdPayments : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryPtdDiscounts : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryPtdFinCharges : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryYtdBalance : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryBegBalance : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryPtdDeposits : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryYtdDeposits : Edm.Decimal
PX.Objects.AR.CuryARHistory.FinPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.PtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.CuryARHistory.YtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryFinPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranYtdRetainageWithheld : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryPtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryYtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.CuryARHistory.FinPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.FinYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.TranYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.PtdRetainageReleased : Edm.Decimal
PX.Objects.AR.CuryARHistory.YtdRetainageReleased : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryFinPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryFinYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranPtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryTranYtdRetainageReleased : Edm.Decimal [required]
PX.Objects.AR.CuryARHistory.CuryPtdRetainageReleased : Edm.Decimal
PX.Objects.AR.CuryARHistory.CuryYtdRetainageReleased : Edm.Decimal
PX.Objects.AR.CuryARHistory.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.CuryARHistory.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.CuryARHistory.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.CuryARHistory.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.CuryARHistory.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.AR.CuryARHistory.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.AR.CuryARHistoryTran (ComplexType)


PX.Objects.AR.CuryARHistoryTran.ID : Edm.Int32
PX.Objects.AR.CuryARHistoryTran.DocType : Edm.String
PX.Objects.AR.CuryARHistoryTran.RefNbr : Edm.String
PX.Objects.AR.CuryARHistoryTran.LineNbr : Edm.Int32
PX.Objects.AR.CuryARHistoryTran.SourceDocType : Edm.String
PX.Objects.AR.CuryARHistoryTran.SourceRefNbr : Edm.String
PX.Objects.AR.CuryARHistoryTran.CuryID : Edm.String
PX.Objects.AR.CuryARHistoryTran.CuryInfoID : Edm.Int64
PX.Objects.AR.CuryARHistoryTran.CustomerID : Edm.Int32
PX.Objects.AR.CuryARHistoryTran.FinPeriodID : Edm.String
PX.Objects.AR.CuryARHistoryTran.TranPeriodID : Edm.String
PX.Objects.AR.CuryARHistoryTran.BatchNbr : Edm.String
PX.Objects.AR.CuryARHistoryTran.Type : Edm.String
PX.Objects.AR.CuryARHistoryTran.TranType : Edm.String
PX.Objects.AR.CuryARHistoryTran.TranRefNbr : Edm.String
PX.Objects.AR.CuryARHistoryTran.ReferenceID : Edm.Int32
PX.Objects.AR.CuryARHistoryTran.IsMigratedRecord : Edm.Boolean
PX.Objects.AR.CuryARHistoryTran.CuryPtdSales : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdPayments : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdDrAdjustments : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdCrAdjustments : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdDiscounts : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdItemDiscounts : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdFinCharges : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdDeposits : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.CuryPtdRetainageReleased : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdSales : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdPayments : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdDrAdjustments : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdCrAdjustments : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdDiscounts : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdItemDiscounts : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdRGOL : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdFinCharges : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdDeposits : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdRetainageWithheld : Edm.Decimal
PX.Objects.AR.CuryARHistoryTran.PtdRetainageReleased : Edm.Decimal

# PX.Objects.AR.Customer (EntityType)

Label: "Customer"
BaseType: PX.Objects.CR.BAccount
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_AR_Customer, Customer
Non-filterable, non-selectable: OverrideBillAddress, IsBillSameAsMain, OverrideBillContact, IsBillContSameAsMain, Included, SharedCreditChild, StatementChild

PX.Objects.AR.Customer.ConsolidateStatements : Edm.Boolean [required] "Consolidate Statements"
PX.Objects.AR.Customer.SharedCreditPolicy : Edm.Boolean [required] "Share Credit Policy"
PX.Objects.AR.Customer.StatementCustomerID : Edm.Int32
PX.Objects.AR.Customer.SharedCreditCustomerID : Edm.Int32
PX.Objects.AR.Customer.CustomerClassID : Edm.String "Customer Class"
PX.Objects.AR.Customer.LanguageID : Edm.String
PX.Objects.AR.Customer.DefSOAddressID : Edm.Int32
PX.Objects.AR.Customer.DefBillAddressID : Edm.Int32
PX.Objects.AR.Customer.DefBillContactID : Edm.Int32 "Default Contact"
PX.Objects.AR.Customer.BaseBillContactID : Edm.Int32 "Default Contact"
PX.Objects.AR.Customer.TermsID : Edm.String "Terms"
PX.Objects.AR.Customer.AutoApplyPayments : Edm.Boolean [required] "Auto-Apply Payments"
PX.Objects.AR.Customer.PrintStatements : Edm.Boolean [required] "Print Statements"
PX.Objects.AR.Customer.PrintCuryStatements : Edm.Boolean [required] "Multi-Currency Statements"
PX.Objects.AR.Customer.SendStatementByEmail : Edm.Boolean [required] "Send Statements by Email"
PX.Objects.AR.Customer.CreditRule : Edm.String "Credit Verification"
PX.Objects.AR.Customer.CreditLimit : Edm.Decimal [required] "Credit Limit"
PX.Objects.AR.Customer.CreditDaysPastDue : Edm.Int16 "Credit Days Past Due"
PX.Objects.AR.Customer.StatementType : Edm.String "Statement Type"
PX.Objects.AR.Customer.StatementCycleId : Edm.String "Statement Cycle ID"
PX.Objects.AR.Customer.StatementLastDate : Edm.DateTimeOffset "Statement Last Date"
PX.Objects.AR.Customer.SmallBalanceAllow : Edm.Boolean [required] "Enable Write-Offs"
PX.Objects.AR.Customer.SmallBalanceLimit : Edm.Decimal "Write-Off Limit"
PX.Objects.AR.Customer.FinChargeApply : Edm.Boolean [required] "Apply Overdue Charges"
PX.Objects.AR.Customer.OverrideBillAddress : Edm.Boolean "Override"
PX.Objects.AR.Customer.IsBillSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.AR.Customer.OverrideBillContact : Edm.Boolean "Override"
PX.Objects.AR.Customer.IsBillContSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.AR.Customer.GroupMask : Edm.Binary
PX.Objects.AR.Customer.DefPaymentMethodID : Edm.String "Default Payment Method"
PX.Objects.AR.Customer.CCProcessingID : Edm.String
PX.Objects.AR.Customer.DefPMInstanceID : Edm.Int32
PX.Objects.AR.Customer.PrintInvoices : Edm.Boolean [required] "Print Invoices"
PX.Objects.AR.Customer.MailInvoices : Edm.Boolean [required] "Send Invoices by Email"
PX.Objects.AR.Customer.PrintDunningLetters : Edm.Boolean [required] "Print Dunning Letters"
PX.Objects.AR.Customer.MailDunningLetters : Edm.Boolean [required] "Send Dunning Letters by Email"
PX.Objects.AR.Customer.Included : Edm.Boolean "Included"
PX.Objects.AR.Customer.SharedCreditChild : Edm.Boolean
PX.Objects.AR.Customer.StatementChild : Edm.Boolean
PX.Objects.AR.Customer.CustomerCategory : Edm.String "Customer Category"
PX.Objects.AR.Customer.ECMCompanyCode : Edm.String "Company Code"
PX.Objects.AR.Customer.IsECMValid : Edm.Boolean [required]
PX.Objects.AR.Customer.BAccountByBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID, BAccountID=BAccountID)
PX.Objects.AR.Customer.CustomerByStatementCustomerID -> PX.Objects.AR.Customer (StatementCustomerID=BAccountID)
PX.Objects.AR.Customer.CustomerBySharedCreditCustomerID -> PX.Objects.AR.Customer (SharedCreditCustomerID=BAccountID)
PX.Objects.AR.Customer.ContactByDefBillContactID -> PX.Objects.CR.Contact (DefBillContactID=ContactID)
PX.Objects.AR.Customer.AddressByDefBillAddressID -> PX.Objects.CR.Address (DefBillAddressID=AddressID)
PX.Objects.AR.Customer.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AR.Customer.AccountByDiscTakenAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Customer.AccountByPrepaymentAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Customer.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Customer.SubByDiscTakenSubID -> PX.Objects.GL.Sub
PX.Objects.AR.Customer.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.AR.Customer.PaymentMethodByDefPaymentMethodID -> PX.Objects.CA.PaymentMethod (DefPaymentMethodID=PaymentMethodID)
PX.Objects.AR.Customer.ARStatementCycleByStatementCycleId -> PX.Objects.AR.ARStatementCycle (StatementCycleId=StatementCycleId)
PX.Objects.AR.Customer.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass (CustomerClassID=CustomerClassID)
PX.Objects.AR.Customer.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)
PX.Objects.AR.Customer.SOContactCollection -> Collection(PX.Objects.SO.SOContact)
PX.Objects.AR.Customer.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.Objects.AR.Customer.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.AR.Customer.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.AR.Customer.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.AR.Customer.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.AR.Customer.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.AR.Customer.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.AR.Customer.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.AR.Customer.FSCustomerBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerBillingSetup)
PX.Objects.AR.Customer.FSMasterContractCollection -> Collection(PX.Objects.FS.FSMasterContract)
PX.Objects.AR.Customer.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.AR.Customer.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.AR.Customer.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.AR.Customer.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.AR.Customer.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.Objects.AR.Customer.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.AR.Customer.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.AR.Customer.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.AR.Customer.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.Objects.AR.Customer.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.AR.Customer.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.AR.Customer.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.AR.Customer.CustomerPaymentMethodInfoCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodInfo)
PX.Objects.AR.Customer.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.AR.Customer.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)
PX.Objects.AR.Customer.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.AR.Customer.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.AR.CustomerClass (EntityType)

Label: "Customer Class"
Key: CustomerClassID
Entity sets: PX_Objects_AR_CustomerClass, CustomerClass
Non-filterable, non-selectable: NoteText

PX.Objects.AR.CustomerClass.CustomerClassID : Edm.String [key] "Class ID"
PX.Objects.AR.CustomerClass.Descr : Edm.String "Description"
PX.Objects.AR.CustomerClass.TermsID : Edm.String "Terms"
PX.Objects.AR.CustomerClass.TaxZoneID : Edm.String "Tax Zone ID"
PX.Objects.AR.CustomerClass.RequireTaxZone : Edm.Boolean [required] "Require Tax Zone"
PX.Objects.AR.CustomerClass.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.AR.CustomerClass.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.AR.CustomerClass.RequireAvalaraCustomerUsageType : Edm.Boolean [required] "Require Tax Exemption Type"
PX.Objects.AR.CustomerClass.PriceClassID : Edm.String "Price Class"
PX.Objects.AR.CustomerClass.CuryID : Edm.String "Currency ID"
PX.Objects.AR.CustomerClass.CuryRateTypeID : Edm.String "Currency Rate Type"
PX.Objects.AR.CustomerClass.AllowOverrideCury : Edm.Boolean [required] "Enable Currency Override"
PX.Objects.AR.CustomerClass.AllowOverrideRate : Edm.Boolean [required] "Enable Rate Override"
PX.Objects.AR.CustomerClass.AutoApplyPayments : Edm.Boolean [required] "Auto-Apply Payments"
PX.Objects.AR.CustomerClass.PrintStatements : Edm.Boolean [required] "Print Statements"
PX.Objects.AR.CustomerClass.PrintCuryStatements : Edm.Boolean [required] "Multi-Currency Statements"
PX.Objects.AR.CustomerClass.SendStatementByEmail : Edm.Boolean [required] "Send Statements by Email"
PX.Objects.AR.CustomerClass.CreditRule : Edm.String "Credit Verification"
PX.Objects.AR.CustomerClass.CreditLimit : Edm.Decimal [required] "Credit Limit"
PX.Objects.AR.CustomerClass.CreditDaysPastDue : Edm.Int16 "Credit Days Past Due"
PX.Objects.AR.CustomerClass.StatementType : Edm.String "Statement Type"
PX.Objects.AR.CustomerClass.StatementCycleId : Edm.String "Statement Cycle ID"
PX.Objects.AR.CustomerClass.SmallBalanceAllow : Edm.Boolean [required] "Enable Write-Offs"
PX.Objects.AR.CustomerClass.SmallBalanceLimit : Edm.Decimal "Write-Off Limit"
PX.Objects.AR.CustomerClass.FinChargeApply : Edm.Boolean [required] "Apply Overdue Charges"
PX.Objects.AR.CustomerClass.FinChargeID : Edm.String "Overdue Charge ID"
PX.Objects.AR.CustomerClass.CountryID : Edm.String "Country"
PX.Objects.AR.CustomerClass.OverLimitAmount : Edm.Decimal [required] "Over-Limit Amount"
PX.Objects.AR.CustomerClass.DefPaymentMethodID : Edm.String "Payment Method"
PX.Objects.AR.CustomerClass.SavePaymentProfiles : Edm.String "Save Payment Profiles"
PX.Objects.AR.CustomerClass.PrintInvoices : Edm.Boolean [required] "Print Invoices"
PX.Objects.AR.CustomerClass.MailInvoices : Edm.Boolean [required] "Send Invoices by Email"
PX.Objects.AR.CustomerClass.PrintDunningLetters : Edm.Boolean [required] "Print Dunning Letters"
PX.Objects.AR.CustomerClass.MailDunningLetters : Edm.Boolean [required] "Send Dunning Letters by Email"
PX.Objects.AR.CustomerClass.DefaultLocationCDFromBranch : Edm.Boolean [required] "Default Location ID from Branch"
PX.Objects.AR.CustomerClass.ShipVia : Edm.String "Ship Via"
PX.Objects.AR.CustomerClass.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.AR.CustomerClass.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.AR.CustomerClass.SalesPersonID : Edm.Int32 "Salesperson ID"
PX.Objects.AR.CustomerClass.DiscountLimit : Edm.Decimal [required] "Group/Document Discount Limit (%)"
PX.Objects.AR.CustomerClass.LocaleName : Edm.String "Locale"
PX.Objects.AR.CustomerClass.NoteID : Edm.Guid
PX.Objects.AR.CustomerClass.NoteText : Edm.String "Note Text"
PX.Objects.AR.CustomerClass.GroupMask : Edm.Binary "Default Restriction Group"
PX.Objects.AR.CustomerClass.tstamp : Edm.Binary
PX.Objects.AR.CustomerClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.CustomerClass.CreatedByScreenID : Edm.String
PX.Objects.AR.CustomerClass.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.CustomerClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.CustomerClass.LastModifiedByScreenID : Edm.String
PX.Objects.AR.CustomerClass.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.CustomerClass.BAccountByOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.AR.CustomerClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.CustomerClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.CustomerClass.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.AR.CustomerClass.CarrierByShipVia -> PX.Objects.CS.Carrier (ShipVia=CarrierID)
PX.Objects.AR.CustomerClass.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.AR.CustomerClass.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.AR.CustomerClass.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AR.CustomerClass.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.AR.CustomerClass.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType (CuryRateTypeID=CuryRateTypeID)
PX.Objects.AR.CustomerClass.AccountByARAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByDiscountAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByDiscTakenAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountBySalesAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByFreightAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByMiscAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByPrepaymentAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByUnrealizedGainAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByUnrealizedLossAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.AR.CustomerClass.SubByARSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByDiscTakenSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByCOGSSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByFreightSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByMiscSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByUnrealizedGainSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByUnrealizedLossSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.AR.CustomerClass.PaymentMethodByDefPaymentMethodID -> PX.Objects.CA.PaymentMethod (DefPaymentMethodID=PaymentMethodID)
PX.Objects.AR.CustomerClass.ARFinChargeByFinChargeID -> PX.Objects.AR.ARFinCharge (FinChargeID=FinChargeID)
PX.Objects.AR.CustomerClass.ARPriceClassByPriceClassID -> PX.Objects.AR.ARPriceClass (PriceClassID=PriceClassID)
PX.Objects.AR.CustomerClass.ARStatementCycleByStatementCycleId -> PX.Objects.AR.ARStatementCycle (StatementCycleId=StatementCycleId)
PX.Objects.AR.CustomerClass.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)
PX.Objects.AR.CustomerClass.RelationGroupByGroupMask -> PX.SM.RelationGroup (GroupMask=GroupMask)
PX.Objects.AR.CustomerClass.LocaleByLocaleName -> PX.SM.Locale (LocaleName=LocaleName)
PX.Objects.AR.CustomerClass.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.AR.CustomerClass.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.AR.CustomerClass.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.AR.CustomerClass.FSCustomerClassBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerClassBillingSetup)
PX.Objects.AR.CustomerClass.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)
PX.Objects.AR.CustomerClass.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.AR.CustomerClass.SalesAllocationCollection -> Collection(PX.Objects.SO.SalesAllocation)

# PX.Objects.AR.CustomerMaster (EntityType)

Label: "Customer (alias)"
Key: BAccountID
Entity sets: PX_Objects_AR_CustomerMaster, Customeralias, CustomerMaster

PX.Objects.AR.CustomerMaster.BAccountID : Edm.Int32 [key] "Customer ID"
PX.Objects.AR.CustomerMaster.AcctCD : Edm.String "Customer ID"
PX.Objects.AR.CustomerMaster.AcctName : Edm.String "Customer Name"
PX.Objects.AR.CustomerMaster.StatementCycleId : Edm.String "Statement Cycle ID"
PX.Objects.AR.CustomerMaster.ConsolidateToParent : Edm.Boolean "Consolidate Balance"
PX.Objects.AR.CustomerMaster.ConsolidatingBAccountID : Edm.Int32
PX.Objects.AR.CustomerMaster.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.AR.CustomerMaster.CustomerClassID : Edm.String "Customer Class"
PX.Objects.AR.CustomerMaster.BaseBillContactID : Edm.Int32 "Default Contact"
PX.Objects.AR.CustomerMaster.BAccountByParentBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID)
PX.Objects.AR.CustomerMaster.ContactByBaseBillContactID -> PX.Objects.CR.Contact (BaseBillContactID=ContactID)
PX.Objects.AR.CustomerMaster.ARStatementCycleByStatementCycleId -> PX.Objects.AR.ARStatementCycle (StatementCycleId=StatementCycleId)
PX.Objects.AR.CustomerMaster.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass (CustomerClassID=CustomerClassID)
PX.Objects.AR.CustomerMaster.CustomerMasterByParentBAccountID -> PX.Objects.AR.CustomerMaster (ParentBAccountID=BAccountID)
PX.Objects.AR.CustomerMaster.BAccountByBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID, BAccountID=BAccountID)
PX.Objects.AR.CustomerMaster.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)

# PX.Objects.AR.CustomerPaymentMethod (EntityType)

Label: "Customer Payment Method"
Key: BAccountID, PMInstanceID
Entity sets: PX_Objects_AR_CustomerPaymentMethod, CustomerPaymentMethod
Non-filterable, non-selectable: NoteText, DisplayCardType, HasBillingInfo, IsBillAddressSameAsMain, IsBillContactSameAsMain, DeletedDatabaseRecord

PX.Objects.AR.CustomerPaymentMethod.BAccountID : Edm.Int32 [key] "Customer"
PX.Objects.AR.CustomerPaymentMethod.PMInstanceID : Edm.Int32 [key] "Card Number"
PX.Objects.AR.CustomerPaymentMethod.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AR.CustomerPaymentMethod.Descr : Edm.String "Card/Account Nbr."
PX.Objects.AR.CustomerPaymentMethod.IsActive : Edm.Boolean [required] "Active"
PX.Objects.AR.CustomerPaymentMethod.NoteID : Edm.Guid
PX.Objects.AR.CustomerPaymentMethod.NoteText : Edm.String "Note Text"
PX.Objects.AR.CustomerPaymentMethod.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AR.CustomerPaymentMethod.ExpirationDateFormated : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AR.CustomerPaymentMethod.CardType : Edm.String "Card/Account Type"
PX.Objects.AR.CustomerPaymentMethod.ProcCenterCardTypeCode : Edm.String "Proc. Center Card Type"
PX.Objects.AR.CustomerPaymentMethod.DisplayCardType : Edm.String "Card/Account Type"
PX.Objects.AR.CustomerPaymentMethod.CVVVerifyTran : Edm.Int32
PX.Objects.AR.CustomerPaymentMethod.BillAddressID : Edm.Int32
PX.Objects.AR.CustomerPaymentMethod.BillContactID : Edm.Int32
PX.Objects.AR.CustomerPaymentMethod.HasBillingInfo : Edm.Boolean "Has Billing Info"
PX.Objects.AR.CustomerPaymentMethod.IsBillAddressSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.AR.CustomerPaymentMethod.IsBillContactSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.AR.CustomerPaymentMethod.CCProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.AR.CustomerPaymentMethod.CustomerCCPID : Edm.String "Customer Profile ID"
PX.Objects.AR.CustomerPaymentMethod.AvailableOnPortals : Edm.Boolean [required] "Available on Portals"
PX.Objects.AR.CustomerPaymentMethod.IsPortalDefault : Edm.Boolean [required] "Is Default (Portal)"
PX.Objects.AR.CustomerPaymentMethod.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.CustomerPaymentMethod.CreatedByScreenID : Edm.String
PX.Objects.AR.CustomerPaymentMethod.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.CustomerPaymentMethod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.CustomerPaymentMethod.LastModifiedByScreenID : Edm.String
PX.Objects.AR.CustomerPaymentMethod.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.CustomerPaymentMethod.tstamp : Edm.Binary
PX.Objects.AR.CustomerPaymentMethod.LastNotificationDate : Edm.DateTimeOffset "Notification Date"
PX.Objects.AR.CustomerPaymentMethod.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AR.CustomerPaymentMethod.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AR.CustomerPaymentMethod.CustomerByBAccountID -> PX.Objects.AR.Customer (BAccountID=BAccountID)
PX.Objects.AR.CustomerPaymentMethod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.CustomerPaymentMethod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.CustomerPaymentMethod.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.AR.CustomerPaymentMethod.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AR.CustomerPaymentMethod.CustomerProcessingCenterIDByCCProcessingCenterID -> PX.Objects.CA.CustomerProcessingCenterID (CustomerCCPID=CustomerCCPID, BAccountID=BAccountID, CCProcessingCenterID=CCProcessingCenterID)
PX.Objects.AR.CustomerPaymentMethod.CCProcessingCenterPmntMethodByPaymentMethodID -> PX.Objects.CA.CCProcessingCenterPmntMethod (CCProcessingCenterID=ProcessingCenterID, PaymentMethodID=PaymentMethodID)
PX.Objects.AR.CustomerPaymentMethod.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.CustomerPaymentMethod.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.CustomerPaymentMethod.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.AR.CustomerPaymentMethod.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.AR.CustomerPaymentMethod.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.AR.CustomerPaymentMethod.PaymentMethodCollection -> Collection(PX.Objects.CA.PaymentMethod)
PX.Objects.AR.CustomerPaymentMethod.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.AR.CustomerPaymentMethod.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AR.CustomerPaymentMethod.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.Objects.AR.CustomerPaymentMethod.CustomerPaymentMethodDetailCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodDetail)
PX.Objects.AR.CustomerPaymentMethod.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.AR.CustomerPaymentMethod.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)

# PX.Objects.AR.CustomerPaymentMethodDetail (EntityType)

Label: "Customer Payment Method Detail"
Key: DetailID, PaymentMethodID, PMInstanceID
Entity sets: PX_Objects_AR_CustomerPaymentMethodDetail, CustomerPaymentMethodDetail

PX.Objects.AR.CustomerPaymentMethodDetail.PMInstanceID : Edm.Int32 [key]
PX.Objects.AR.CustomerPaymentMethodDetail.PaymentMethodID : Edm.String [key]
PX.Objects.AR.CustomerPaymentMethodDetail.DetailID : Edm.String [key] "Description"
PX.Objects.AR.CustomerPaymentMethodDetail.Value : Edm.String "Value"
PX.Objects.AR.CustomerPaymentMethodDetail.tstamp : Edm.Binary
PX.Objects.AR.CustomerPaymentMethodDetail.CreatedByScreenID : Edm.String
PX.Objects.AR.CustomerPaymentMethodDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.CustomerPaymentMethodDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.CustomerPaymentMethodDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.CustomerPaymentMethodDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AR.CustomerPaymentMethodDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.CustomerPaymentMethodDetail.NoteID : Edm.Guid
PX.Objects.AR.CustomerPaymentMethodDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.CustomerPaymentMethodDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.CustomerPaymentMethodDetail.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AR.CustomerPaymentMethodDetail.PaymentMethodDetailByPaymentMethodID -> PX.Objects.CA.PaymentMethodDetail (DetailID=DetailID, PaymentMethodID=PaymentMethodID)
PX.Objects.AR.CustomerPaymentMethodDetail.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)

# PX.Objects.AR.CustomerPaymentMethodInfo (EntityType)

Label: "Customer Payment Method"
Key: PMInstanceID
Entity sets: PX_Objects_AR_CustomerPaymentMethodInfo, CustomerPaymentMethod1, CustomerPaymentMethodInfo

PX.Objects.AR.CustomerPaymentMethodInfo.BAccountID : Edm.Int32
PX.Objects.AR.CustomerPaymentMethodInfo.IsDefault : Edm.Boolean "Is Default"
PX.Objects.AR.CustomerPaymentMethodInfo.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AR.CustomerPaymentMethodInfo.PMInstanceID : Edm.Int32 [key]
PX.Objects.AR.CustomerPaymentMethodInfo.CashAccountID : Edm.Int32 "Cash Account"
PX.Objects.AR.CustomerPaymentMethodInfo.Descr : Edm.String "Description"
PX.Objects.AR.CustomerPaymentMethodInfo.IsActive : Edm.Boolean "Active"
PX.Objects.AR.CustomerPaymentMethodInfo.ARIsOnePerCustomer : Edm.Boolean
PX.Objects.AR.CustomerPaymentMethodInfo.IsCustomerPaymentMethod : Edm.Boolean "Override"
PX.Objects.AR.CustomerPaymentMethodInfo.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AR.CustomerPaymentMethodInfo.CCProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.AR.CustomerPaymentMethodInfo.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.CustomerPaymentMethodInfo.AvailableOnPortals : Edm.Boolean "Available on Portals"
PX.Objects.AR.CustomerPaymentMethodInfo.IsPortalDefault : Edm.Boolean "Is Default (Portal)"
PX.Objects.AR.CustomerPaymentMethodInfo.PaymentType : Edm.String
PX.Objects.AR.CustomerPaymentMethodInfo.CustomerByBAccountID -> PX.Objects.AR.Customer (BAccountID=BAccountID)
PX.Objects.AR.CustomerPaymentMethodInfo.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.AR.CustomerPaymentMethodInfo.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AR.CustomerPaymentMethodInfo.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AR.CustomerPaymentMethodInfo.CustomerCollection -> Collection(PX.Objects.AR.Customer)

# PX.Objects.AR.CustomerSharedCredit (EntityType)

Label: "Customer Shared Credit"
Key: BAccountID
Entity sets: PX_Objects_AR_CustomerSharedCredit, CustomerSharedCredit

PX.Objects.AR.CustomerSharedCredit.BAccountID : Edm.Int32 [key]
PX.Objects.AR.CustomerSharedCredit.AcctCD : Edm.String "Customer ID"
PX.Objects.AR.CustomerSharedCredit.AcctName : Edm.String "Customer Name"
PX.Objects.AR.CustomerSharedCredit.SharedCreditCustomerID : Edm.Int32
PX.Objects.AR.CustomerSharedCredit.SharedCreditPolicy : Edm.Boolean
PX.Objects.AR.CustomerSharedCredit.CreditRule : Edm.String "Credit Verification"
PX.Objects.AR.CustomerSharedCredit.CreditLimit : Edm.Decimal "Credit Limit"
PX.Objects.AR.CustomerSharedCredit.CustomerByStatementCustomerID -> PX.Objects.AR.Customer
PX.Objects.AR.CustomerSharedCredit.CustomerBySharedCreditCustomerID -> PX.Objects.AR.Customer (SharedCreditCustomerID=BAccountID)
PX.Objects.AR.CustomerSharedCredit.ContactByDefBillContactID -> PX.Objects.CR.Contact
PX.Objects.AR.CustomerSharedCredit.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.AR.CustomerSharedCredit.LocationByDefLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.AR.CustomerSharedCredit.LocationByBAccountID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.AR.CustomerSharedCredit.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.CustomerSharedCredit.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.CustomerSharedCredit.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.AR.CustomerSharedCredit.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.AR.CustomerSharedCredit.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)
PX.Objects.AR.CustomerSharedCredit.SOContactCollection -> Collection(PX.Objects.SO.SOContact)
PX.Objects.AR.CustomerSharedCredit.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.AR.CustomerSharedCredit.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.AR.CustomerSharedCredit.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.CustomerSharedCredit.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.Objects.AR.CustomerSharedCredit.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.AR.CustomerSharedCredit.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AR.CustomerSharedCredit.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.AR.CustomerSharedCredit.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.AR.CustomerSharedCredit.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.AR.CustomerSharedCredit.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.AR.CustomerSharedCredit.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.AR.CustomerSharedCredit.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.AR.CustomerSharedCredit.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.AR.CustomerSharedCredit.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.AR.CustomerSharedCredit.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.AR.CustomerSharedCredit.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.CustomerSharedCredit.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.AR.CustomerSharedCredit.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.AR.CustomerSharedCredit.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.AR.CustomerSharedCredit.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.AR.CustomerSharedCredit.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.AR.CustomerSharedCredit.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.AR.CustomerSharedCredit.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.AR.CustomerSharedCredit.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.AR.CustomerSharedCredit.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.AR.CustomerSharedCredit.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.AR.CustomerSharedCredit.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.AR.CustomerSharedCredit.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.AR.CustomerSharedCredit.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.AR.CustomerSharedCredit.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.AR.CustomerSharedCredit.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.AR.CustomerSharedCredit.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.AR.CustomerSharedCredit.DiscountCustomerCollection -> Collection(PX.Objects.AR.DiscountCustomer)
PX.Objects.AR.CustomerSharedCredit.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.AR.CustomerSharedCredit.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.AR.CustomerSharedCredit.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.AR.CustomerSharedCredit.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.AR.CustomerSharedCredit.FSCustomerBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerBillingSetup)
PX.Objects.AR.CustomerSharedCredit.FSMasterContractCollection -> Collection(PX.Objects.FS.FSMasterContract)
PX.Objects.AR.CustomerSharedCredit.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.AR.CustomerSharedCredit.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.AR.CustomerSharedCredit.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.AR.CustomerSharedCredit.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.AR.CustomerSharedCredit.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.AR.CustomerSharedCredit.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.AR.CustomerSharedCredit.BAccountLocationCollection -> Collection(PX.Objects.FS.BAccountLocation)
PX.Objects.AR.CustomerSharedCredit.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.AR.CustomerSharedCredit.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.Objects.AR.CustomerSharedCredit.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.AR.CustomerSharedCredit.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.AR.CustomerSharedCredit.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.AR.CustomerSharedCredit.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.Objects.AR.CustomerSharedCredit.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.AR.CustomerSharedCredit.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.AR.CustomerSharedCredit.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.AR.CustomerSharedCredit.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.AR.CustomerSharedCredit.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.AR.CustomerSharedCredit.CustomerProcessingCenterIDCollection -> Collection(PX.Objects.CA.CustomerProcessingCenterID)
PX.Objects.AR.CustomerSharedCredit.CustomerPaymentMethodInfoCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodInfo)
PX.Objects.AR.CustomerSharedCredit.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.AR.CustomerSharedCredit.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)
PX.Objects.AR.CustomerSharedCredit.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.AR.CustomerSharedCredit.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.AR.CustSalesPeople (EntityType)

Label: "Customer Salespersons"
Key: BAccountID, LocationID, SalesPersonID
Entity sets: PX_Objects_AR_CustSalesPeople, CustomerSalespersons, CustSalesPeople

PX.Objects.AR.CustSalesPeople.SalesPersonID : Edm.Int32 [key]
PX.Objects.AR.CustSalesPeople.BAccountID : Edm.Int32 [key] "Customer"
PX.Objects.AR.CustSalesPeople.LocationID : Edm.Int32 [key] "Location"
PX.Objects.AR.CustSalesPeople.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.AR.CustSalesPeople.CommisionPct : Edm.Decimal "Commission %"
PX.Objects.AR.CustSalesPeople.tstamp : Edm.Binary
PX.Objects.AR.CustSalesPeople.CreatedByScreenID : Edm.String
PX.Objects.AR.CustSalesPeople.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.CustSalesPeople.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.CustSalesPeople.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.CustSalesPeople.LastModifiedByScreenID : Edm.String
PX.Objects.AR.CustSalesPeople.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.CustSalesPeople.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AR.CustSalesPeople.CustomerByBAccountID -> PX.Objects.AR.Customer (BAccountID=BAccountID)
PX.Objects.AR.CustSalesPeople.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.CustSalesPeople.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.CustSalesPeople.LocationByLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID, LocationID=LocationID)
PX.Objects.AR.CustSalesPeople.LocationByBAccountID -> PX.Objects.CR.Location (LocationID=LocationID, BAccountID=BAccountID)
PX.Objects.AR.CustSalesPeople.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson (SalesPersonID=SalesPersonID)

# PX.Objects.AR.DiscountBranch (EntityType)

Label: "Discount for Branch"
Key: BranchID, DiscountID, DiscountSequenceID
Entity sets: PX_Objects_AR_DiscountBranch, DiscountforBranch, DiscountBranch

PX.Objects.AR.DiscountBranch.DiscountID : Edm.String [key]
PX.Objects.AR.DiscountBranch.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.AR.DiscountBranch.DiscountSequenceID : Edm.String [key]
PX.Objects.AR.DiscountBranch.tstamp : Edm.Binary
PX.Objects.AR.DiscountBranch.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountBranch.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountBranch.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountBranch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountBranch.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountBranch.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountBranch.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.AR.DiscountBranch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.DiscountBranch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.DiscountBranch.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AR.DiscountBranch.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.DiscountCustomer (EntityType)

Label: "Discount for Customer"
Key: CustomerID, DiscountID, DiscountSequenceID
Entity sets: PX_Objects_AR_DiscountCustomer, DiscountforCustomer, DiscountCustomer

PX.Objects.AR.DiscountCustomer.DiscountID : Edm.String [key]
PX.Objects.AR.DiscountCustomer.CustomerID : Edm.Int32 [key] "Customer"
PX.Objects.AR.DiscountCustomer.DiscountSequenceID : Edm.String [key]
PX.Objects.AR.DiscountCustomer.tstamp : Edm.Binary
PX.Objects.AR.DiscountCustomer.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountCustomer.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountCustomer.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountCustomer.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountCustomer.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountCustomer.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountCustomer.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.AR.DiscountCustomer.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.AR.DiscountCustomer.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.DiscountCustomer.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.DiscountCustomer.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AR.DiscountCustomer.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.DiscountCustomerPriceClass (EntityType)

Label: "Discount for Customer and Price Class"
Key: CustomerPriceClassID, DiscountID, DiscountSequenceID
Entity sets: PX_Objects_AR_DiscountCustomerPriceClass, DiscountforCustomerandPriceClass, DiscountCustomerPriceClass

PX.Objects.AR.DiscountCustomerPriceClass.DiscountID : Edm.String [key]
PX.Objects.AR.DiscountCustomerPriceClass.CustomerPriceClassID : Edm.String [key] "Price Class ID"
PX.Objects.AR.DiscountCustomerPriceClass.DiscountSequenceID : Edm.String [key]
PX.Objects.AR.DiscountCustomerPriceClass.tstamp : Edm.Binary
PX.Objects.AR.DiscountCustomerPriceClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountCustomerPriceClass.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountCustomerPriceClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountCustomerPriceClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountCustomerPriceClass.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountCustomerPriceClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountCustomerPriceClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.DiscountCustomerPriceClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.DiscountCustomerPriceClass.ARPriceClassByCustomerPriceClassID -> PX.Objects.AR.ARPriceClass (CustomerPriceClassID=PriceClassID)
PX.Objects.AR.DiscountCustomerPriceClass.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AR.DiscountCustomerPriceClass.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.DiscountDetail (EntityType)

Label: "Discount Breakpoint"
Key: DiscountDetailsID
Entity sets: PX_Objects_AR_DiscountDetail, DiscountBreakpoint, DiscountDetail
Non-filterable, non-selectable: DiscountPercent, LastDiscountPercent, PendingDiscountPercent

PX.Objects.AR.DiscountDetail.DiscountDetailsID : Edm.Int32 [key]
PX.Objects.AR.DiscountDetail.LineNbr : Edm.Int32
PX.Objects.AR.DiscountDetail.DiscountID : Edm.String
PX.Objects.AR.DiscountDetail.DiscountSequenceID : Edm.String
PX.Objects.AR.DiscountDetail.IsActive : Edm.Boolean "Active"
PX.Objects.AR.DiscountDetail.Amount : Edm.Decimal "Break Amount"
PX.Objects.AR.DiscountDetail.AmountTo : Edm.Decimal
PX.Objects.AR.DiscountDetail.LastAmount : Edm.Decimal "Last Break Amount"
PX.Objects.AR.DiscountDetail.LastAmountTo : Edm.Decimal
PX.Objects.AR.DiscountDetail.PendingAmount : Edm.Decimal "Pending Break Amount"
PX.Objects.AR.DiscountDetail.Quantity : Edm.Decimal "Break Quantity"
PX.Objects.AR.DiscountDetail.QuantityTo : Edm.Decimal
PX.Objects.AR.DiscountDetail.LastQuantity : Edm.Decimal "Last Break Quantity"
PX.Objects.AR.DiscountDetail.LastQuantityTo : Edm.Decimal
PX.Objects.AR.DiscountDetail.PendingQuantity : Edm.Decimal "Pending Break Quantity"
PX.Objects.AR.DiscountDetail.Discount : Edm.Decimal "Discount Amount"
PX.Objects.AR.DiscountDetail.DiscountPercent : Edm.Decimal "Discount Percent"
PX.Objects.AR.DiscountDetail.LastDiscount : Edm.Decimal "Last Discount Amount"
PX.Objects.AR.DiscountDetail.LastDiscountPercent : Edm.Decimal "Last Discount Percent"
PX.Objects.AR.DiscountDetail.PendingDiscount : Edm.Decimal "Pending Discount Amount"
PX.Objects.AR.DiscountDetail.PendingDiscountPercent : Edm.Decimal "Pending Discount Percent"
PX.Objects.AR.DiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.AR.DiscountDetail.LastFreeItemQty : Edm.Decimal "Last Free Item Qty."
PX.Objects.AR.DiscountDetail.PendingFreeItemQty : Edm.Decimal "Pending Free Item Qty."
PX.Objects.AR.DiscountDetail.StartDate : Edm.DateTimeOffset "Pending Date"
PX.Objects.AR.DiscountDetail.LastDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AR.DiscountDetail.tstamp : Edm.Binary
PX.Objects.AR.DiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountDetail.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.DiscountInventoryPriceClass (EntityType)

Label: "Discount for Inventory and Price Class"
Key: DiscountID, DiscountSequenceID, InventoryPriceClassID
Entity sets: PX_Objects_AR_DiscountInventoryPriceClass, DiscountforInventoryandPriceClass, DiscountInventoryPriceClass

PX.Objects.AR.DiscountInventoryPriceClass.DiscountID : Edm.String [key]
PX.Objects.AR.DiscountInventoryPriceClass.InventoryPriceClassID : Edm.String [key] "Price Class ID"
PX.Objects.AR.DiscountInventoryPriceClass.DiscountSequenceID : Edm.String [key]
PX.Objects.AR.DiscountInventoryPriceClass.tstamp : Edm.Binary
PX.Objects.AR.DiscountInventoryPriceClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountInventoryPriceClass.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountInventoryPriceClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountInventoryPriceClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountInventoryPriceClass.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountInventoryPriceClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountInventoryPriceClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.DiscountInventoryPriceClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.DiscountInventoryPriceClass.INPriceClassByInventoryPriceClassID -> PX.Objects.IN.INPriceClass (InventoryPriceClassID=PriceClassID)
PX.Objects.AR.DiscountInventoryPriceClass.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AR.DiscountInventoryPriceClass.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.DiscountItem (EntityType)

Label: "Discount Item"
Key: DiscountID, DiscountSequenceID, InventoryID
Entity sets: PX_Objects_AR_DiscountItem, DiscountItem

PX.Objects.AR.DiscountItem.DiscountID : Edm.String [key]
PX.Objects.AR.DiscountItem.InventoryID : Edm.Int32 [key] "Inventory ID"
PX.Objects.AR.DiscountItem.DiscountSequenceID : Edm.String [key]
PX.Objects.AR.DiscountItem.Amount : Edm.Decimal "Amount"
PX.Objects.AR.DiscountItem.Quantity : Edm.Decimal "Quantity"
PX.Objects.AR.DiscountItem.UOM : Edm.String "UOM"
PX.Objects.AR.DiscountItem.tstamp : Edm.Binary
PX.Objects.AR.DiscountItem.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountItem.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountItem.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountItem.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountItem.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountItem.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountItem.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.AR.DiscountItem.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.DiscountItem.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.DiscountItem.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.AR.DiscountItem.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AR.DiscountItem.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.DiscountSequence (EntityType)

Label: "Discount Sequence"
Key: DiscountID, DiscountSequenceID
Entity sets: PX_Objects_AR_DiscountSequence, DiscountSequence
Non-filterable, non-selectable: ShowFreeItem, NoteText

PX.Objects.AR.DiscountSequence.DiscountID : Edm.String [key] "Discount Code"
PX.Objects.AR.DiscountSequence.DiscountSequenceID : Edm.String [key] "Sequence"
PX.Objects.AR.DiscountSequence.LineCntr : Edm.Int32
PX.Objects.AR.DiscountSequence.Description : Edm.String "Description"
PX.Objects.AR.DiscountSequence.DiscountedFor : Edm.String "Discount By"
PX.Objects.AR.DiscountSequence.BreakBy : Edm.String "Break By"
PX.Objects.AR.DiscountSequence.IsPromotion : Edm.Boolean [required] "Promotional"
PX.Objects.AR.DiscountSequence.IsActive : Edm.Boolean [required] "Active"
PX.Objects.AR.DiscountSequence.Prorate : Edm.Boolean [required] "Prorate Discount"
PX.Objects.AR.DiscountSequence.StartDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AR.DiscountSequence.EndDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AR.DiscountSequence.UpdateDate : Edm.DateTimeOffset "Last Update Date"
PX.Objects.AR.DiscountSequence.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.AR.DiscountSequence.PendingFreeItemID : Edm.Int32 "Pending Free Item"
PX.Objects.AR.DiscountSequence.LastFreeItemID : Edm.Int32 "Last Free Item"
PX.Objects.AR.DiscountSequence.ShowFreeItem : Edm.Boolean "ShowFreeItem"
PX.Objects.AR.DiscountSequence.NoteID : Edm.Guid
PX.Objects.AR.DiscountSequence.NoteText : Edm.String "Note Text"
PX.Objects.AR.DiscountSequence.tstamp : Edm.Binary
PX.Objects.AR.DiscountSequence.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountSequence.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountSequence.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.DiscountSequence.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountSequence.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountSequence.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.DiscountSequence.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.AR.DiscountSequence.InventoryItemByPendingFreeItemID -> PX.Objects.IN.InventoryItem (PendingFreeItemID=InventoryID)
PX.Objects.AR.DiscountSequence.InventoryItemByLastFreeItemID -> PX.Objects.IN.InventoryItem (LastFreeItemID=InventoryID)
PX.Objects.AR.DiscountSequence.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.DiscountSequence.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.DiscountSequence.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.AR.DiscountSequence.DiscountSequenceDetailCollection -> Collection(PX.Objects.AR.DiscountSequenceDetail)
PX.Objects.AR.DiscountSequence.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.AR.DiscountSequence.FSDiscountDetailCollection -> Collection(PX.Objects.FS.FSDiscountDetail)
PX.Objects.AR.DiscountSequence.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.AR.DiscountSequence.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.AR.DiscountSequence.SOShipmentDiscountDetailCollection -> Collection(PX.Objects.SO.SOShipmentDiscountDetail)
PX.Objects.AR.DiscountSequence.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.AR.DiscountSequence.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.AR.DiscountSequence.DiscountBranchCollection -> Collection(PX.Objects.AR.DiscountBranch)
PX.Objects.AR.DiscountSequence.DiscountCustomerCollection -> Collection(PX.Objects.AR.DiscountCustomer)
PX.Objects.AR.DiscountSequence.DiscountCustomerPriceClassCollection -> Collection(PX.Objects.AR.DiscountCustomerPriceClass)
PX.Objects.AR.DiscountSequence.DiscountInventoryPriceClassCollection -> Collection(PX.Objects.AR.DiscountInventoryPriceClass)
PX.Objects.AR.DiscountSequence.DiscountItemCollection -> Collection(PX.Objects.AR.DiscountItem)
PX.Objects.AR.DiscountSequence.DiscountSiteCollection -> Collection(PX.Objects.AR.DiscountSite)
PX.Objects.AR.DiscountSequence.APDiscountVendorCollection -> Collection(PX.Objects.AP.APDiscountVendor)
PX.Objects.AR.DiscountSequence.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.AR.DiscountSequence.DiscountDetailCollection -> Collection(PX.Objects.AR.DiscountDetail)

# PX.Objects.AR.DiscountSequenceDetail (EntityType)

Label: "Discount Sequence Detail"
Key: DiscountDetailsID, IsLast
Entity sets: PX_Objects_AR_DiscountSequenceDetail, DiscountSequenceDetail
Non-filterable, non-selectable: DiscountPercent, PendingDiscountPercent

PX.Objects.AR.DiscountSequenceDetail.DiscountDetailsID : Edm.Int32 [key]
PX.Objects.AR.DiscountSequenceDetail.LineNbr : Edm.Int32 [required]
PX.Objects.AR.DiscountSequenceDetail.DiscountID : Edm.String
PX.Objects.AR.DiscountSequenceDetail.DiscountSequenceID : Edm.String
PX.Objects.AR.DiscountSequenceDetail.IsLast : Edm.Boolean [key required]
PX.Objects.AR.DiscountSequenceDetail.IsActive : Edm.Boolean [required] "Active"
PX.Objects.AR.DiscountSequenceDetail.Amount : Edm.Decimal "Break Amount"
PX.Objects.AR.DiscountSequenceDetail.AmountTo : Edm.Decimal
PX.Objects.AR.DiscountSequenceDetail.PendingAmount : Edm.Decimal "Pending Break Amount"
PX.Objects.AR.DiscountSequenceDetail.Quantity : Edm.Decimal "Break Quantity"
PX.Objects.AR.DiscountSequenceDetail.QuantityTo : Edm.Decimal
PX.Objects.AR.DiscountSequenceDetail.PendingQuantity : Edm.Decimal "Pending Break Quantity"
PX.Objects.AR.DiscountSequenceDetail.Discount : Edm.Decimal "Discount Amount"
PX.Objects.AR.DiscountSequenceDetail.DiscountPercent : Edm.Decimal "Discount Percent"
PX.Objects.AR.DiscountSequenceDetail.PendingDiscount : Edm.Decimal "Pending Discount Amount"
PX.Objects.AR.DiscountSequenceDetail.PendingDiscountPercent : Edm.Decimal "Pending Discount Percent"
PX.Objects.AR.DiscountSequenceDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.AR.DiscountSequenceDetail.PendingFreeItemQty : Edm.Decimal "Pending Free Item Qty."
PX.Objects.AR.DiscountSequenceDetail.PendingDate : Edm.DateTimeOffset "Pending Date"
PX.Objects.AR.DiscountSequenceDetail.LastDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.AR.DiscountSequenceDetail.tstamp : Edm.Binary
PX.Objects.AR.DiscountSequenceDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountSequenceDetail.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountSequenceDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountSequenceDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountSequenceDetail.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountSequenceDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountSequenceDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.DiscountSequenceDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.DiscountSequenceDetail.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.DiscountSequenceDetail2 (EntityType)

Label: "Discount Sequence Detail"
BaseType: PX.Objects.AR.DiscountSequenceDetail
Key: DiscountDetailsID, IsLast (inherited from PX.Objects.AR.DiscountSequenceDetail)
Entity sets: PX_Objects_AR_DiscountSequenceDetail2

# PX.Objects.AR.DiscountSite (EntityType)

Label: "Discount for Warehouse"
Key: DiscountID, DiscountSequenceID, SiteID
Entity sets: PX_Objects_AR_DiscountSite, DiscountforWarehouse, DiscountSite

PX.Objects.AR.DiscountSite.DiscountID : Edm.String [key]
PX.Objects.AR.DiscountSite.SiteID : Edm.Int32 [key] "Warehouse"
PX.Objects.AR.DiscountSite.DiscountSequenceID : Edm.String [key]
PX.Objects.AR.DiscountSite.tstamp : Edm.Binary
PX.Objects.AR.DiscountSite.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.DiscountSite.CreatedByScreenID : Edm.String
PX.Objects.AR.DiscountSite.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountSite.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.DiscountSite.LastModifiedByScreenID : Edm.String
PX.Objects.AR.DiscountSite.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.AR.DiscountSite.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.DiscountSite.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.DiscountSite.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.AR.DiscountSite.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.AR.DiscountSite.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)

# PX.Objects.AR.ExternalTransaction (EntityType)

Label: "External Transaction"
Key: TransactionID
Entity sets: PX_Objects_AR_ExternalTransaction, ExternalTransaction
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.AR.ExternalTransaction.TransactionID : Edm.Int32 [key] "Ext. Tran. ID"
PX.Objects.AR.ExternalTransaction.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.AR.ExternalTransaction.PayLinkID : Edm.Int32
PX.Objects.AR.ExternalTransaction.ProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.AR.ExternalTransaction.TerminalID : Edm.String "Terminal ID"
PX.Objects.AR.ExternalTransaction.DocType : Edm.String "Doc. Type"
PX.Objects.AR.ExternalTransaction.RefNbr : Edm.String "Doc. Reference Nbr."
PX.Objects.AR.ExternalTransaction.OrigDocType : Edm.String "Orig. Doc. Type"
PX.Objects.AR.ExternalTransaction.OrigRefNbr : Edm.String "Orig. Doc. Ref. Nbr."
PX.Objects.AR.ExternalTransaction.VoidDocType : Edm.String
PX.Objects.AR.ExternalTransaction.VoidRefNbr : Edm.String
PX.Objects.AR.ExternalTransaction.TranNumber : Edm.String "Proc. Center Tran. Nbr."
PX.Objects.AR.ExternalTransaction.TranApiNumber : Edm.String
PX.Objects.AR.ExternalTransaction.AuthNumber : Edm.String "Proc. Center Auth. Nbr."
PX.Objects.AR.ExternalTransaction.Amount : Edm.Decimal [required] "Tran. Amount"
PX.Objects.AR.ExternalTransaction.CardType : Edm.String "Card/Account Type"
PX.Objects.AR.ExternalTransaction.ProcCenterCardTypeCode : Edm.String "Proc. Center Card Type"
PX.Objects.AR.ExternalTransaction.ProcStatus : Edm.String "Proc. Status"
PX.Objects.AR.ExternalTransaction.LastActivityDate : Edm.DateTimeOffset "Last Activity Date"
PX.Objects.AR.ExternalTransaction.Direction : Edm.String
PX.Objects.AR.ExternalTransaction.Active : Edm.Boolean [required] "Active"
PX.Objects.AR.ExternalTransaction.SaveProfile : Edm.Boolean [required] "Load Payment Profile"
PX.Objects.AR.ExternalTransaction.NeedSync : Edm.Boolean [required] "Validation Is Required"
PX.Objects.AR.ExternalTransaction.SyncStatus : Edm.String "Validation Status"
PX.Objects.AR.ExternalTransaction.SyncMessage : Edm.String
PX.Objects.AR.ExternalTransaction.ExtProfileId : Edm.String "Ext. Profile ID"
PX.Objects.AR.ExternalTransaction.Completed : Edm.Boolean [required] "Completed"
PX.Objects.AR.ExternalTransaction.ParentTranID : Edm.Int32
PX.Objects.AR.ExternalTransaction.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.AR.ExternalTransaction.CVVVerification : Edm.String "CVV Verification"
PX.Objects.AR.ExternalTransaction.FundHoldExpDate : Edm.DateTimeOffset
PX.Objects.AR.ExternalTransaction.Settled : Edm.Boolean [required] "Settled"
PX.Objects.AR.ExternalTransaction.L3Status : Edm.String "Processing Status"
PX.Objects.AR.ExternalTransaction.L3Error : Edm.String "Error Description"
PX.Objects.AR.ExternalTransaction.LastDigits : Edm.String "Last Digits"
PX.Objects.AR.ExternalTransaction.SurchargeAmount : Edm.Decimal "Surcharge Amount"
PX.Objects.AR.ExternalTransaction.tstamp : Edm.Binary
PX.Objects.AR.ExternalTransaction.NoteID : Edm.Guid
PX.Objects.AR.ExternalTransaction.NoteText : Edm.String "Note Text"
PX.Objects.AR.ExternalTransaction.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AR.ExternalTransaction.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.AR.ExternalTransaction.SOOrderByOrigDocType -> PX.Objects.SO.SOOrder (OrigRefNbr=OrderNbr, OrigDocType=OrderType)
PX.Objects.AR.ExternalTransaction.ARRegisterByDocType -> PX.Objects.AR.ARRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.AR.ExternalTransaction.CCPayLinkByPayLinkID -> PX.Objects.CC.CCPayLink (PayLinkID=PayLinkID)
PX.Objects.AR.ExternalTransaction.SOOrderTypeByOrigDocType -> PX.Objects.SO.SOOrderType (OrigDocType=OrderType)
PX.Objects.AR.ExternalTransaction.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.AR.ExternalTransaction.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.AR.ExternalTransaction.ExternalTransactionByTransactionID -> PX.Objects.AR.ExternalTransaction (TransactionID=ParentTranID)
PX.Objects.AR.ExternalTransaction.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.AR.ExternalTransaction.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.AR.ExternalTransaction.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.Objects.AR.ExternalTransaction.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)

# PX.Objects.AR.FSCTNotification (EntityType)

Label: "Default Notification setup"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_AR_FSCTNotification

# PX.Objects.AR.FSNotification (EntityType)

Label: "Default Notification setup"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_AR_FSNotification

# PX.Objects.AR.Light.Customer (EntityType)

Label: "Light version of Customer DAC for Statements Printing"
Key: AcctCD
Entity sets: PX_Objects_AR_Light_Customer, LightversionofCustomerDACforStatementsPrinting, Customer1
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.AR.Light.Customer.BAccountID : Edm.Int32
PX.Objects.AR.Light.Customer.AcctName : Edm.String "Account Name"
PX.Objects.AR.Light.Customer.ConsolidatingBAccountID : Edm.Int32
PX.Objects.AR.Light.Customer.AcctCD : Edm.String [key] "Account ID"
PX.Objects.AR.Light.Customer.CuryID : Edm.String
PX.Objects.AR.Light.Customer.Status : Edm.String
PX.Objects.AR.Light.Customer.LocaleName : Edm.String "Locale"
PX.Objects.AR.Light.Customer.NoteID : Edm.Guid
PX.Objects.AR.Light.Customer.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.AR.Light.Customer.CustomerClassID : Edm.String
PX.Objects.AR.Light.Customer.StatementCycleId : Edm.String
PX.Objects.AR.Light.Customer.PrintCuryStatements : Edm.Boolean "Multi-Currency Statements"
PX.Objects.AR.Light.Customer.SendStatementByEmail : Edm.Boolean "Send Statements by Email"
PX.Objects.AR.Light.Customer.PrintStatements : Edm.Boolean "Print Statements"
PX.Objects.AR.Light.Customer.DefBillContactID : Edm.Int32 "Default Contact"
PX.Objects.AR.Light.Customer.DefBillAddressID : Edm.Int32
PX.Objects.AR.Light.Customer.StatementType : Edm.String "Statement Type"
PX.Objects.AR.Light.Customer.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AR.Light.Customer.BAccountByBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID, BAccountID=BAccountID)
PX.Objects.AR.Light.Customer.CustomerByStatementCustomerID -> PX.Objects.AR.Customer
PX.Objects.AR.Light.Customer.CustomerBySharedCreditCustomerID -> PX.Objects.AR.Customer
PX.Objects.AR.Light.Customer.ContactByDefBillContactID -> PX.Objects.CR.Contact (DefBillContactID=ContactID)
PX.Objects.AR.Light.Customer.AddressByDefBillAddressID -> PX.Objects.CR.Address (DefBillAddressID=AddressID)
PX.Objects.AR.Light.Customer.TermsByTermsID -> PX.Objects.CS.Terms
PX.Objects.AR.Light.Customer.AccountByDiscTakenAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Light.Customer.AccountByPrepaymentAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Light.Customer.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Light.Customer.SubByDiscTakenSubID -> PX.Objects.GL.Sub
PX.Objects.AR.Light.Customer.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.AR.Light.Customer.PaymentMethodByDefPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.Objects.AR.Light.Customer.ARStatementCycleByStatementCycleId -> PX.Objects.AR.ARStatementCycle (StatementCycleId=StatementCycleId)
PX.Objects.AR.Light.Customer.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass (CustomerClassID=CustomerClassID)
PX.Objects.AR.Light.Customer.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)
PX.Objects.AR.Light.Customer.SOContactCollection -> Collection(PX.Objects.SO.SOContact)
PX.Objects.AR.Light.Customer.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.Objects.AR.Light.Customer.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.AR.Light.Customer.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.AR.Light.Customer.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.AR.Light.Customer.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.AR.Light.Customer.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.AR.Light.Customer.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.AR.Light.Customer.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.AR.Light.Customer.FSCustomerBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerBillingSetup)
PX.Objects.AR.Light.Customer.FSMasterContractCollection -> Collection(PX.Objects.FS.FSMasterContract)
PX.Objects.AR.Light.Customer.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.AR.Light.Customer.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.AR.Light.Customer.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.AR.Light.Customer.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.AR.Light.Customer.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.Objects.AR.Light.Customer.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.AR.Light.Customer.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.AR.Light.Customer.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.AR.Light.Customer.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.Objects.AR.Light.Customer.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.AR.Light.Customer.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.AR.Light.Customer.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.AR.Light.Customer.CustomerPaymentMethodInfoCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodInfo)
PX.Objects.AR.Light.Customer.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.AR.Light.Customer.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)
PX.Objects.AR.Light.Customer.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.AR.Light.Customer.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.AR.Override.BAccount (EntityType)

Key: BAccountID
Entity sets: PX_Objects_AR_Override_BAccount
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.AR.Override.BAccount.BAccountID : Edm.Int32 [key]
PX.Objects.AR.Override.BAccount.AcctName : Edm.String
PX.Objects.AR.Override.BAccount.ConsolidateToParent : Edm.Boolean
PX.Objects.AR.Override.BAccount.ParentBAccountID : Edm.Int32
PX.Objects.AR.Override.BAccount.ConsolidatingBAccountID : Edm.Int32
PX.Objects.AR.Override.BAccount.BaseCuryID : Edm.String
PX.Objects.AR.Override.BAccount.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AR.Override.BAccount.VendorByOwnerID -> PX.Objects.AP.Vendor
PX.Objects.AR.Override.BAccount.BAccountByParentBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID)
PX.Objects.AR.Override.BAccount.BAccountByCOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.AR.Override.BAccount.ContactByDefContactID -> PX.Objects.CR.Contact
PX.Objects.AR.Override.BAccount.ContactByPrimaryContactID -> PX.Objects.CR.Contact
PX.Objects.AR.Override.BAccount.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.AR.Override.BAccount.ContactByBAccountID -> PX.Objects.CR.Contact (BAccountID=BAccountID)
PX.Objects.AR.Override.BAccount.CRCustomerClassByClassID -> PX.Objects.CR.CRCustomerClass
PX.Objects.AR.Override.BAccount.AddressByDefAddressID -> PX.Objects.CR.Address
PX.Objects.AR.Override.BAccount.UsersByCreatedByID -> PX.SM.Users
PX.Objects.AR.Override.BAccount.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.AR.Override.BAccount.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.AR.Override.BAccount.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.AR.Override.BAccount.CurrencyByCuryID -> PX.Objects.CM.Currency
PX.Objects.AR.Override.BAccount.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)
PX.Objects.AR.Override.BAccount.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType
PX.Objects.AR.Override.BAccount.LocationByDefLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.AR.Override.BAccount.LocationByBAccountID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.AR.Override.BAccount.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign
PX.Objects.AR.Override.BAccount.LocaleByLocaleName -> PX.SM.Locale
PX.Objects.AR.Override.BAccount.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.Objects.AR.Override.BAccount.PRCRAPayrollAccountCollection -> Collection(PX.Objects.PR.PRCRAPayrollAccount)
PX.Objects.AR.Override.BAccount.PRTaxReportingAccountCollection -> Collection(PX.Objects.PR.PRTaxReportingAccount)
PX.Objects.AR.Override.BAccount.CanadianOrganizationSettingsCollection -> Collection(PX.Objects.Localizations.CA.CanadianOrganizationSettings)
PX.Objects.AR.Override.BAccount.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.AR.Override.BAccount.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.AR.Override.BAccount.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.AR.Override.BAccount.AUScheduleCollection -> Collection(PX.SM.AUSchedule)
PX.Objects.AR.Override.BAccount.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.AR.Override.BAccount.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.AR.Override.BAccount.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.AR.Override.BAccount.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.AR.Override.BAccount.GLTrialBalanceImportMapCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportMap)
PX.Objects.AR.Override.BAccount.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.AR.Override.BAccount.CISMasterTableCollection -> Collection(PX.Objects.Localizations.GB.CISMasterTable)
PX.Objects.AR.Override.BAccount.PRAcaCompanyYearlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyYearlyInformation)
PX.Objects.AR.Override.BAccount.PRTaxFormBatchCollection -> Collection(PX.Objects.PR.PRTaxFormBatch)
PX.Objects.AR.Override.BAccount.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.AR.Override.BAccount.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.AR.Override.BAccount.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.AR.Override.BAccount.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.Override.BAccount.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.AR.Override.BAccount.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.Override.BAccount.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.AR.Override.BAccount.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.AR.Override.BAccount.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.AR.Override.BAccount.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.AR.Override.BAccount.SVATConversionHistExtCollection -> Collection(PX.Objects.TX.SVATConversionHistExt)
PX.Objects.AR.Override.BAccount.RQRequestLineOwnedCollection -> Collection(PX.Objects.RQ.RQRequestLineOwned)
PX.Objects.AR.Override.BAccount.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.AR.Override.BAccount.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.AR.Override.BAccount.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.AR.Override.BAccount.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.AR.Override.BAccount.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.AR.Override.BAccount.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.AR.Override.BAccount.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.AR.Override.BAccount.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)
PX.Objects.AR.Override.BAccount.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.AR.Override.BAccount.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.AR.Override.BAccount.MultipleQuoteCollection -> Collection(PX.Objects.CN.CRM.CR.DAC.MultipleQuote)
PX.Objects.AR.Override.BAccount.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.AR.Override.BAccount.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.AR.Override.BAccount.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.AR.Override.BAccount.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.AR.Override.BAccount.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.AR.Override.BAccount.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.AR.Override.BAccount.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.Override.BAccount.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.AR.Override.BAccount.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.AR.Override.BAccount.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.AR.Override.BAccount.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.AR.Override.BAccount.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.AR.Override.BAccount.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AR.Override.BAccount.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.AR.Override.BAccount.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.AR.Override.BAccount.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.AR.Override.BAccount.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.AR.Override.BAccount.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.AR.Override.BAccount.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.AR.Override.BAccount.DailyFieldReportVisitorCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor)
PX.Objects.AR.Override.BAccount.FSLicenseCollection -> Collection(PX.Objects.SV.FSLicense)
PX.Objects.AR.Override.BAccount.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.AR.Override.BAccount.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.AR.Override.BAccount.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.AR.Override.BAccount.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.AR.Override.BAccount.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.AR.Override.BAccount.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.AR.Override.BAccount.JointPayeeCollection -> Collection(PX.Objects.CN.JointChecks.JointPayee)
PX.Objects.AR.Override.BAccount.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.AR.Override.BAccount.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.AR.Override.BAccount.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.AR.Override.BAccount.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.Override.BAccount.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.AR.Override.BAccount.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.AR.Override.BAccount.T5018MasterTableCollection -> Collection(PX.Objects.Localizations.CA.T5018MasterTable)
PX.Objects.AR.Override.BAccount.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.AR.Override.BAccount.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.AR.Override.BAccount.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.AR.Override.BAccount.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.AR.Override.BAccount.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.AR.Override.BAccount.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.AR.Override.BAccount.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.AR.Override.BAccount.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.AR.Override.BAccount.TaxYearCollection -> Collection(PX.Objects.TX.TaxYear)
PX.Objects.AR.Override.BAccount.TaxPeriodCollection -> Collection(PX.Objects.TX.TaxPeriod)
PX.Objects.AR.Override.BAccount.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.AR.Override.BAccount.TaxReportCollection -> Collection(PX.Objects.TX.TaxReport)
PX.Objects.AR.Override.BAccount.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)
PX.Objects.AR.Override.BAccount.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.AR.Override.BAccount.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.AR.Override.BAccount.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)
PX.Objects.AR.Override.BAccount.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.Objects.AR.Override.BAccount.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.AR.Override.BAccount.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.AR.Override.BAccount.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.AR.Override.BAccount.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.AR.Override.BAccount.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.AR.Override.BAccount.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.AR.Override.BAccount.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.AR.Override.BAccount.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.AR.Override.BAccount.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.AR.Override.BAccount.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.AR.Override.BAccount.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.AR.Override.BAccount.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.AR.Override.BAccount.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.AR.Override.BAccount.PMProjectContactCollection -> Collection(PX.Objects.PM.PMProjectContact)
PX.Objects.AR.Override.BAccount.PMUnionCollection -> Collection(PX.Objects.PM.PMUnion)
PX.Objects.AR.Override.BAccount.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.AR.Override.BAccount.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.AR.Override.BAccount.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.AR.Override.BAccount.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.AR.Override.BAccount.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.AR.Override.BAccount.CarrierPluginCustomerCollection -> Collection(PX.Objects.CS.CarrierPluginCustomer)
PX.Objects.AR.Override.BAccount.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.AR.Override.BAccount.INReplenishmentOrderCollection -> Collection(PX.Objects.IN.INReplenishmentOrder)
PX.Objects.AR.Override.BAccount.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.AR.Override.BAccount.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.Objects.AR.Override.BAccount.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.AR.Override.BAccount.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.AR.Override.BAccount.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.AR.Override.BAccount.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.AR.Override.BAccount.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.AR.Override.BAccount.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.AR.Override.BAccount.DiscountCustomerCollection -> Collection(PX.Objects.AR.DiscountCustomer)
PX.Objects.AR.Override.BAccount.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.AR.Override.BAccount.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.AR.Override.BAccount.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.Objects.AR.Override.BAccount.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.AR.Override.BAccount.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.Objects.AR.Override.BAccount.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.AR.Override.BAccount.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.AR.Override.BAccount.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.AR.Override.BAccount.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.AR.Override.BAccount.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.AR.Override.BAccount.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.AR.Override.BAccount.FSGeoZoneEmpCollection -> Collection(PX.Objects.FS.FSGeoZoneEmp)
PX.Objects.AR.Override.BAccount.T4ASlipCollection -> Collection(PX.Objects.Localizations.CA.T4ASlip)
PX.Objects.AR.Override.BAccount.PREmployeeDeductCollection -> Collection(PX.Objects.PR.PREmployeeDeduct)
PX.Objects.AR.Override.BAccount.PRTaxRegistrationAttributeCollection -> Collection(PX.Objects.PR.PRTaxRegistrationAttribute)
PX.Objects.AR.Override.BAccount.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.AR.Override.BAccount.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.AR.Override.BAccount.SVServiceLocationCustomerCollection -> Collection(PX.Objects.SV.SVServiceLocationCustomer)
PX.Objects.AR.Override.BAccount.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)
PX.Objects.AR.Override.BAccount.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.AR.Override.BAccount.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.AR.Override.BAccount.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.AR.Override.BAccount.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.AR.Override.BAccount.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.AR.Override.BAccount.CustomerProcessingCenterIDCollection -> Collection(PX.Objects.CA.CustomerProcessingCenterID)
PX.Objects.AR.Override.BAccount.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.AR.Override.BAccount.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.AR.Override.BAccount.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.AR.Override.BAccount.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.AR.Override.BAccount.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.AR.Override.BAccount.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.AR.Override.BAccount.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.AR.Override.BAccount.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.AR.Override.BAccount.FSSOEmployeeCollection -> Collection(PX.Objects.FS.FSSOEmployee)
PX.Objects.AR.Override.BAccount.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.Objects.AR.Override.BAccount.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.AR.Override.BAccount.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.AR.Override.BAccount.FSAppointmentStaffMemberCollection -> Collection(PX.Objects.FS.FSAppointmentStaffMember)
PX.Objects.AR.Override.BAccount.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.AR.Override.BAccount.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.AR.Override.BAccount.POAddressCollection -> Collection(PX.Objects.PO.POAddress)
PX.Objects.AR.Override.BAccount.POContactCollection -> Collection(PX.Objects.PO.POContact)
PX.Objects.AR.Override.BAccount.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.AR.Override.BAccount.AddressCollection -> Collection(PX.Objects.CR.Address)
PX.Objects.AR.Override.BAccount.CRAddressCollection -> Collection(PX.Objects.CR.CRAddress)
PX.Objects.AR.Override.BAccount.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.Objects.AR.Override.BAccount.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.Objects.AR.Override.BAccount.FSAddressCollection -> Collection(PX.Objects.FS.FSAddress)
PX.Objects.AR.Override.BAccount.FSContactCollection -> Collection(PX.Objects.FS.FSContact)
PX.Objects.AR.Override.BAccount.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.AR.Override.BAccount.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.AR.Override.BAccount.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.Objects.AR.Override.BAccount.VendorPaymentMethodDetailCollection -> Collection(PX.Objects.AP.VendorPaymentMethodDetail)
PX.Objects.AR.Override.BAccount.CRRelationCollection -> Collection(PX.Objects.CR.CRRelation)
PX.Objects.AR.Override.BAccount.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.AR.Override.BAccount.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.AR.Override.BAccount.SelContractWatcherCollection -> Collection(PX.Objects.CT.SelContractWatcher)
PX.Objects.AR.Override.BAccount.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)
PX.Objects.AR.Override.BAccount.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.AR.Override.BAccount.CABankTranBAccountMappingCollection -> Collection(PX.Objects.CA.CABankTranBAccountMapping)
PX.Objects.AR.Override.BAccount.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.AR.Override.BAccount.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.AR.Override.BAccount.RecognizedVendorMappingCollection -> Collection(PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping)
PX.Objects.AR.Override.BAccount.TaxRegistrationCollection -> Collection(PX.Objects.Localizations.CA.TaxRegistration)
PX.Objects.AR.Override.BAccount.CISSubcontractorCollection -> Collection(PX.Objects.Localizations.GB.CISSubcontractor)
PX.Objects.AR.Override.BAccount.PREntityCompanyTaxAttributeCollection -> Collection(PX.Objects.PR.PREntityCompanyTaxAttribute)
PX.Objects.AR.Override.BAccount.PREntityTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PREntityTaxCodeAttribute)
PX.Objects.AR.Override.BAccount.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.AR.Override.BAccount.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.AR.Override.BAccount.RequestForInformationRelationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation)
PX.Objects.AR.Override.BAccount.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.AR.Override.BAccount.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.AR.Override.BAccount.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.AR.Override.BAccount.BAccountLocationCollection -> Collection(PX.Objects.FS.BAccountLocation)
PX.Objects.AR.Override.BAccount.CanadianVendorCollection -> Collection(PX.Objects.Localizations.CA.CanadianVendor)

# PX.Objects.AR.Override.Customer (EntityType)

Key: BAccountID
Entity sets: PX_Objects_AR_Override_Customer
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.AR.Override.Customer.BAccountID : Edm.Int32 [key]
PX.Objects.AR.Override.Customer.StatementCycleId : Edm.String
PX.Objects.AR.Override.Customer.ConsolidateStatements : Edm.Boolean
PX.Objects.AR.Override.Customer.SharedCreditCustomerID : Edm.Int32
PX.Objects.AR.Override.Customer.SharedCreditPolicy : Edm.Boolean
PX.Objects.AR.Override.Customer.StatementLastDate : Edm.DateTimeOffset
PX.Objects.AR.Override.Customer.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.AR.Override.Customer.BAccountByParentBAccountID -> PX.Objects.CR.BAccount
PX.Objects.AR.Override.Customer.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.AR.Override.Customer.CustomerByStatementCustomerID -> PX.Objects.AR.Customer
PX.Objects.AR.Override.Customer.CustomerBySharedCreditCustomerID -> PX.Objects.AR.Customer (SharedCreditCustomerID=BAccountID)
PX.Objects.AR.Override.Customer.ContactByDefBillContactID -> PX.Objects.CR.Contact
PX.Objects.AR.Override.Customer.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.AR.Override.Customer.AddressByDefBillAddressID -> PX.Objects.CR.Address
PX.Objects.AR.Override.Customer.UsersByCreatedByID -> PX.SM.Users
PX.Objects.AR.Override.Customer.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.AR.Override.Customer.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.AR.Override.Customer.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.AR.Override.Customer.TermsByTermsID -> PX.Objects.CS.Terms
PX.Objects.AR.Override.Customer.CurrencyByCuryID -> PX.Objects.CM.Currency
PX.Objects.AR.Override.Customer.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList
PX.Objects.AR.Override.Customer.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType
PX.Objects.AR.Override.Customer.AccountByDiscTakenAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Override.Customer.AccountByPrepaymentAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Override.Customer.AccountByCOGSAcctID -> PX.Objects.GL.Account
PX.Objects.AR.Override.Customer.SubByDiscTakenSubID -> PX.Objects.GL.Sub
PX.Objects.AR.Override.Customer.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.AR.Override.Customer.PaymentMethodByDefPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.Objects.AR.Override.Customer.LocationByDefLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.AR.Override.Customer.LocationByBAccountID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.AR.Override.Customer.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign
PX.Objects.AR.Override.Customer.ARStatementCycleByStatementCycleId -> PX.Objects.AR.ARStatementCycle (StatementCycleId=StatementCycleId)
PX.Objects.AR.Override.Customer.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass
PX.Objects.AR.Override.Customer.LocaleByLocaleName -> PX.SM.Locale
PX.Objects.AR.Override.Customer.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.Override.Customer.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.Override.Customer.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.AR.Override.Customer.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.AR.Override.Customer.SOAddressCollection -> Collection(PX.Objects.SO.SOAddress)
PX.Objects.AR.Override.Customer.SOContactCollection -> Collection(PX.Objects.SO.SOContact)
PX.Objects.AR.Override.Customer.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.AR.Override.Customer.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.AR.Override.Customer.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.AR.Override.Customer.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.Objects.AR.Override.Customer.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.AR.Override.Customer.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.AR.Override.Customer.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.AR.Override.Customer.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.AR.Override.Customer.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.AR.Override.Customer.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.AR.Override.Customer.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.AR.Override.Customer.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.AR.Override.Customer.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.AR.Override.Customer.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.AR.Override.Customer.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.AR.Override.Customer.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.Override.Customer.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.AR.Override.Customer.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.AR.Override.Customer.PostingBatchDetailCollection -> Collection(PX.Objects.FS.PostingBatchDetail)
PX.Objects.AR.Override.Customer.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.AR.Override.Customer.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.AR.Override.Customer.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.AR.Override.Customer.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.AR.Override.Customer.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.AR.Override.Customer.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.AR.Override.Customer.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.AR.Override.Customer.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.AR.Override.Customer.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.AR.Override.Customer.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.AR.Override.Customer.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.AR.Override.Customer.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.AR.Override.Customer.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.AR.Override.Customer.DiscountCustomerCollection -> Collection(PX.Objects.AR.DiscountCustomer)
PX.Objects.AR.Override.Customer.BCBindingExtCollection -> Collection(PX.Commerce.Objects.BCBindingExt)
PX.Objects.AR.Override.Customer.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.AR.Override.Customer.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.AR.Override.Customer.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.AR.Override.Customer.FSCustomerBillingSetupCollection -> Collection(PX.Objects.FS.FSCustomerBillingSetup)
PX.Objects.AR.Override.Customer.FSMasterContractCollection -> Collection(PX.Objects.FS.FSMasterContract)
PX.Objects.AR.Override.Customer.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.AR.Override.Customer.FSWrkProcessCollection -> Collection(PX.Objects.FS.FSWrkProcess)
PX.Objects.AR.Override.Customer.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.AR.Override.Customer.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.AR.Override.Customer.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.AR.Override.Customer.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.AR.Override.Customer.BAccountLocationCollection -> Collection(PX.Objects.FS.BAccountLocation)
PX.Objects.AR.Override.Customer.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.AR.Override.Customer.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.Objects.AR.Override.Customer.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.AR.Override.Customer.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.AR.Override.Customer.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.AR.Override.Customer.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.Objects.AR.Override.Customer.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.AR.Override.Customer.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.AR.Override.Customer.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.AR.Override.Customer.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.AR.Override.Customer.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.AR.Override.Customer.CustomerProcessingCenterIDCollection -> Collection(PX.Objects.CA.CustomerProcessingCenterID)
PX.Objects.AR.Override.Customer.CustomerPaymentMethodInfoCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodInfo)
PX.Objects.AR.Override.Customer.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.AR.Override.Customer.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)
PX.Objects.AR.Override.Customer.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.AR.Override.Customer.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.AR.Overrides.ARDocumentRelease.ARHistory2 (EntityType)

Label: "AR History"
BaseType: PX.Objects.AR.ARHistory
Key: AccountID, BranchID, CustomerID, FinPeriodID, SubID (inherited from PX.Objects.AR.ARHistory)
Entity sets: PX_Objects_AR_Overrides_ARDocumentRelease_ARHistory2

# PX.Objects.AR.Overrides.ARDocumentRelease.CuryARHistory2 (EntityType)

Label: "Currency AR History"
BaseType: PX.Objects.AR.CuryARHistory
Key: AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID (inherited from PX.Objects.AR.CuryARHistory)
Entity sets: PX_Objects_AR_Overrides_ARDocumentRelease_CuryARHistory2

# PX.Objects.AR.Overrides.ScheduleMaint.DocumentSelection (EntityType)

Label: "AR Document to Process"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_Overrides_ScheduleMaint_DocumentSelection, ARDocumenttoProcess, DocumentSelection

# PX.Objects.AR.PendingPPDARTaxAdjApp (EntityType)

Label: "Pending PPD AR Tax Adj App"
BaseType: PX.Objects.AR.ARAdjust
Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr (inherited from PX.Objects.AR.ARAdjust)
Entity sets: PX_Objects_AR_PendingPPDARTaxAdjApp, PendingPPDARTaxAdjApp
Non-filterable, non-selectable: Index

PX.Objects.AR.PendingPPDARTaxAdjApp.Index : Edm.Int32
PX.Objects.AR.PendingPPDARTaxAdjApp.PayDocType : Edm.String
PX.Objects.AR.PendingPPDARTaxAdjApp.PayRefNbr : Edm.String
PX.Objects.AR.PendingPPDARTaxAdjApp.InvDocType : Edm.String
PX.Objects.AR.PendingPPDARTaxAdjApp.InvRefNbr : Edm.String
PX.Objects.AR.PendingPPDARTaxAdjApp.InvCuryID : Edm.String "Currency"
PX.Objects.AR.PendingPPDARTaxAdjApp.InvCuryInfoID : Edm.Int64
PX.Objects.AR.PendingPPDARTaxAdjApp.InvCustomerLocationID : Edm.Int32
PX.Objects.AR.PendingPPDARTaxAdjApp.InvTaxZoneID : Edm.String
PX.Objects.AR.PendingPPDARTaxAdjApp.InvTaxCalcMode : Edm.String
PX.Objects.AR.PendingPPDARTaxAdjApp.InvTermsID : Edm.String "Credit Terms"
PX.Objects.AR.PendingPPDARTaxAdjApp.InvCuryOrigDocAmt : Edm.Decimal "Amount"
PX.Objects.AR.PendingPPDARTaxAdjApp.InvCuryOrigDiscAmt : Edm.Decimal "Cash Discount"
PX.Objects.AR.PendingPPDARTaxAdjApp.InvCuryVatTaxableTotal : Edm.Decimal "VAT Taxable Total"
PX.Objects.AR.PendingPPDARTaxAdjApp.InvCuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.AR.PendingPPDARTaxAdjApp.InvCuryDocBal : Edm.Decimal
PX.Objects.AR.PendingPPDARTaxAdjApp.TermsByInvTermsID -> PX.Objects.CS.Terms (InvTermsID=TermsID)
PX.Objects.AR.PendingPPDARTaxAdjApp.CurrencyByInvCuryID -> PX.Objects.CM.Currency (InvCuryID=CuryID)

# PX.Objects.AR.SalesPerson (EntityType)

Label: "Sales Person"
Key: SalesPersonCD
Entity sets: PX_Objects_AR_SalesPerson, SalesPerson
Non-filterable, non-selectable: NoteText

PX.Objects.AR.SalesPerson.SalesPersonID : Edm.Int32 "SalesPerson ID"
PX.Objects.AR.SalesPerson.SalesPersonCD : Edm.String [key] "Salesperson ID"
PX.Objects.AR.SalesPerson.CommnPct : Edm.Decimal [required] "Default Commission %"
PX.Objects.AR.SalesPerson.tstamp : Edm.Binary
PX.Objects.AR.SalesPerson.CreatedByID : Edm.Guid "Created By"
PX.Objects.AR.SalesPerson.CreatedByScreenID : Edm.String
PX.Objects.AR.SalesPerson.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.AR.SalesPerson.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.AR.SalesPerson.LastModifiedByScreenID : Edm.String
PX.Objects.AR.SalesPerson.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.AR.SalesPerson.Descr : Edm.String "Name"
PX.Objects.AR.SalesPerson.IsActive : Edm.Boolean [required] "Is Active"
PX.Objects.AR.SalesPerson.NoteID : Edm.Guid
PX.Objects.AR.SalesPerson.NoteText : Edm.String "Note Text"
PX.Objects.AR.SalesPerson.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.AR.SalesPerson.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.AR.SalesPerson.SubBySalesSubID -> PX.Objects.GL.Sub
PX.Objects.AR.SalesPerson.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.AR.SalesPerson.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.AR.SalesPerson.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.AR.SalesPerson.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.AR.SalesPerson.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.AR.SalesPerson.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.AR.SalesPerson.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.AR.SalesPerson.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.AR.SalesPerson.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.AR.SalesPerson.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.AR.SalesPerson.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.AR.SalesPerson.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.AR.SalesPerson.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.AR.SalesPerson.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.AR.SalesPerson.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.Objects.AR.SalesPerson.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.AR.SalesPerson.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.AR.SalesPerson.FSSrvOrdTypeCollection -> Collection(PX.Objects.FS.FSSrvOrdType)
PX.Objects.AR.SalesPerson.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)

# PX.Objects.AR.Standalone.ARCashSale (EntityType)

Label: "Cash Sale"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_AR_Standalone_ARCashSale, CashSale, ARCashSale
Non-filterable, non-selectable: DetailExtLineTotal, CuryDetailExtPriceTotal, DepositDate, VoidAppl

PX.Objects.AR.Standalone.ARCashSale.TermsID : Edm.String "Terms"
PX.Objects.AR.Standalone.ARCashSale.ARInvoiceDocType : Edm.String
PX.Objects.AR.Standalone.ARCashSale.ARInvoiceRefNbr : Edm.String
PX.Objects.AR.Standalone.ARCashSale.BillAddressID : Edm.Int32
PX.Objects.AR.Standalone.ARCashSale.BillContactID : Edm.Int32 "Billing Contact"
PX.Objects.AR.Standalone.ARCashSale.ShipAddressID : Edm.Int32
PX.Objects.AR.Standalone.ARCashSale.ShipContactID : Edm.Int32 "Shipping Contact"
PX.Objects.AR.Standalone.ARCashSale.InvoiceNbr : Edm.String
PX.Objects.AR.Standalone.ARCashSale.InvoiceDate : Edm.DateTimeOffset
PX.Objects.AR.Standalone.ARCashSale.TaxZoneID : Edm.String "Customer Tax Zone"
PX.Objects.AR.Standalone.ARCashSale.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.AR.Standalone.ARCashSale.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.AR.Standalone.ARCashSale.MasterRefNbr : Edm.String
PX.Objects.AR.Standalone.ARCashSale.InstallmentNbr : Edm.Int16
PX.Objects.AR.Standalone.ARCashSale.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.AR.Standalone.ARCashSale.TaxTotal : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CuryOrigTaxDiscAmt : Edm.Decimal "Discounted Tax Amount"
PX.Objects.AR.Standalone.ARCashSale.OrigTaxDiscAmt : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CuryLineTotal : Edm.Decimal "Detail Total"
PX.Objects.AR.Standalone.ARCashSale.CuryVatExemptTotal : Edm.Decimal "Tax Exempt Total"
PX.Objects.AR.Standalone.ARCashSale.VatExemptTotal : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CuryVatTaxableTotal : Edm.Decimal "Taxable Total"
PX.Objects.AR.Standalone.ARCashSale.VatTaxableTotal : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.LineTotal : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CommnPct : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CuryCommnAmt : Edm.Decimal "Commission Amt."
PX.Objects.AR.Standalone.ARCashSale.CommnAmt : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CuryCommnblAmt : Edm.Decimal "Total Commissionable"
PX.Objects.AR.Standalone.ARCashSale.CommnblAmt : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CreditHold : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.ApprovedCredit : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.ApprovedCreditAmt : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.WorkgroupID : Edm.Int32 "Workgroup ID"
PX.Objects.AR.Standalone.ARCashSale.OwnerID : Edm.Int32 "Owner ID"
PX.Objects.AR.Standalone.ARCashSale.CuryLineDiscTotal : Edm.Decimal "Line Discounts"
PX.Objects.AR.Standalone.ARCashSale.LineDiscTotal : Edm.Decimal "Line Discounts"
PX.Objects.AR.Standalone.ARCashSale.CuryGoodsExtPriceTotal : Edm.Decimal "Goods"
PX.Objects.AR.Standalone.ARCashSale.GoodsExtPriceTotal : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CuryMiscExtPriceTotal : Edm.Decimal "Misc. Charges"
PX.Objects.AR.Standalone.ARCashSale.MiscExtPriceTotal : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.DetailExtLineTotal : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.CuryDetailExtPriceTotal : Edm.Decimal "Detail Total"
PX.Objects.AR.Standalone.ARCashSale.ApplyOverdueCharge : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.IsPaymentsTransferred : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.ARPaymentDocType : Edm.String
PX.Objects.AR.Standalone.ARCashSale.ARPaymentRefNbr : Edm.String
PX.Objects.AR.Standalone.ARCashSale.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.AR.Standalone.ARCashSale.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.AR.Standalone.ARCashSale.ProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.AR.Standalone.ARCashSale.TerminalID : Edm.String "Terminal"
PX.Objects.AR.Standalone.ARCashSale.CardPresent : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.ExtRefNbr : Edm.String "Payment Ref."
PX.Objects.AR.Standalone.ARCashSale.AdjDate : Edm.DateTimeOffset "Date"
PX.Objects.AR.Standalone.ARCashSale.AdjFinPeriodID : Edm.String "Post Period"
PX.Objects.AR.Standalone.ARCashSale.AdjTranPeriodID : Edm.String
PX.Objects.AR.Standalone.ARCashSale.Cleared : Edm.Boolean "Cleared"
PX.Objects.AR.Standalone.ARCashSale.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.AR.Standalone.ARCashSale.Settled : Edm.Boolean "Settled"
PX.Objects.AR.Standalone.ARCashSale.CATranID : Edm.Int64
PX.Objects.AR.Standalone.ARCashSale.DepositAsBatch : Edm.Boolean "Batch Deposit"
PX.Objects.AR.Standalone.ARCashSale.ChargeCntr : Edm.Int32
PX.Objects.AR.Standalone.ARCashSale.DepositAfter : Edm.DateTimeOffset "Deposit After"
PX.Objects.AR.Standalone.ARCashSale.Deposited : Edm.Boolean "Deposited"
PX.Objects.AR.Standalone.ARCashSale.DepositDate : Edm.DateTimeOffset "Batch Deposit Date"
PX.Objects.AR.Standalone.ARCashSale.DepositType : Edm.String "DepositType"
PX.Objects.AR.Standalone.ARCashSale.DepositNbr : Edm.String "Batch Deposit Nbr."
PX.Objects.AR.Standalone.ARCashSale.CuryConsolidateChargeTotal : Edm.Decimal "Deducted Charges"
PX.Objects.AR.Standalone.ARCashSale.ConsolidateChargeTotal : Edm.Decimal
PX.Objects.AR.Standalone.ARCashSale.RefTranExtNbr : Edm.String "Orig. Transaction"
PX.Objects.AR.Standalone.ARCashSale.IsCCAuthorized : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.IsCCCaptured : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.IsCCCaptureFailed : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.IsCCRefunded : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.IsCCUserAttention : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.CCActualExternalTransactionID : Edm.Int32
PX.Objects.AR.Standalone.ARCashSale.CCPaymentStateDescr : Edm.String "Processing Status"
PX.Objects.AR.Standalone.ARCashSale.VoidAppl : Edm.Boolean
PX.Objects.AR.Standalone.ARCashSale.IsCCPayment : Edm.Boolean "IsCCPayment"
PX.Objects.AR.Standalone.ARCashSale.ARContactByShipContactID -> PX.Objects.AR.ARContact (ShipContactID=ContactID)
PX.Objects.AR.Standalone.ARCashSale.ARContactByBillContactID -> PX.Objects.AR.ARContact (BillContactID=ContactID)
PX.Objects.AR.Standalone.ARCashSale.ARRegisterByOrigRefNbr -> PX.Objects.AR.ARRegister (OrigDocType=DocType, OrigRefNbr=RefNbr)
PX.Objects.AR.Standalone.ARCashSale.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.AR.Standalone.ARCashSale.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.AR.Standalone.ARCashSale.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.AR.Standalone.ARCashSale.CCProcessingCenterTerminalByProcessingCenterID -> PX.Objects.CC.CCProcessingCenterTerminal (TerminalID=TerminalID, ProcessingCenterID=ProcessingCenterID)
PX.Objects.AR.Standalone.ARCashSale.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.AR.Standalone.ARCashSale.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.AR.Standalone.ARCashSale.CustomerPaymentMethodByPaymentMethodID -> PX.Objects.AR.CustomerPaymentMethod (CustomerID=BAccountID, PaymentMethodID=PaymentMethodID)
PX.Objects.AR.Standalone.ARCashSale.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (CustomerID=BAccountID, PaymentMethodID=PaymentMethodID, PMInstanceID=PMInstanceID)
PX.Objects.AR.Standalone.ARCashSale.ExternalTransactionByPMInstanceID -> PX.Objects.AR.ExternalTransaction (RefTranExtNbr=TranNumber, PMInstanceID=PMInstanceID)

# PX.Objects.CA.ACHPlugInParameter (EntityType)

Label: "ACHPlugInParameter"
Key: ParameterID, PaymentMethodID, PlugInTypeName
Entity sets: PX_Objects_CA_ACHPlugInParameter, ACHPlugInParameter
Non-filterable, non-selectable: DetailMapping, ExportScenarioMapping, DataElementSize

PX.Objects.CA.ACHPlugInParameter.PaymentMethodID : Edm.String [key] "Payment Method ID"
PX.Objects.CA.ACHPlugInParameter.PlugInTypeName : Edm.String [key] "Export Plug-In (Type)"
PX.Objects.CA.ACHPlugInParameter.ParameterID : Edm.String [key] "Parameter ID"
PX.Objects.CA.ACHPlugInParameter.ParameterCode : Edm.String "Setting"
PX.Objects.CA.ACHPlugInParameter.Description : Edm.String "Description"
PX.Objects.CA.ACHPlugInParameter.Value : Edm.String "Value"
PX.Objects.CA.ACHPlugInParameter.Required : Edm.Boolean
PX.Objects.CA.ACHPlugInParameter.ReadOnly : Edm.Boolean
PX.Objects.CA.ACHPlugInParameter.Visible : Edm.Boolean
PX.Objects.CA.ACHPlugInParameter.Type : Edm.Int32
PX.Objects.CA.ACHPlugInParameter.Order : Edm.Int32
PX.Objects.CA.ACHPlugInParameter.UsedIn : Edm.Int32
PX.Objects.CA.ACHPlugInParameter.DetailMapping : Edm.Int32
PX.Objects.CA.ACHPlugInParameter.ExportScenarioMapping : Edm.Int32
PX.Objects.CA.ACHPlugInParameter.IsGroupHeader : Edm.Boolean
PX.Objects.CA.ACHPlugInParameter.IsAvailableInShortForm : Edm.Boolean
PX.Objects.CA.ACHPlugInParameter.IsFormula : Edm.Boolean "Is Formula"
PX.Objects.CA.ACHPlugInParameter.DataElementSize : Edm.Int32
PX.Objects.CA.ACHPlugInParameter.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)

# PX.Objects.CA.ACHPlugInParameter2 (EntityType)

Label: "ACHPlugInParameter"
BaseType: PX.Objects.CA.ACHPlugInParameter
Key: ParameterID, PaymentMethodID, PlugInTypeName (inherited from PX.Objects.CA.ACHPlugInParameter)
Entity sets: PX_Objects_CA_ACHPlugInParameter2, ACHPlugInParameter1, ACHPlugInParameter2

# PX.Objects.CA.BankStatementHelpers.CATranExt (EntityType)

Label: "CA Transaction"
BaseType: PX.Objects.CA.CATran
Key: TranID (inherited from PX.Objects.CA.CATran)
Entity sets: PX_Objects_CA_BankStatementHelpers_CATranExt
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.CA.BankStatementHelpers.CATranExt.IsMatched : Edm.Boolean "Matched"
PX.Objects.CA.BankStatementHelpers.CATranExt.MatchRelevance : Edm.Decimal "Match Relevance"
PX.Objects.CA.BankStatementHelpers.CATranExt.MatchRelevancePercent : Edm.Decimal "Match Relevance, %"
PX.Objects.CA.BankStatementHelpers.CATranExt.CuryTranAbsAmt : Edm.Decimal "Amount"
PX.Objects.CA.BankStatementHelpers.CATranExt.TranAbsAmt : Edm.Decimal "Tran. Amount"
PX.Objects.CA.BankStatementHelpers.CATranExt.CuryTranAmtCalc : Edm.Decimal "Amount"
PX.Objects.CA.BankStatementHelpers.CATranExt.TranAmtCalc : Edm.Decimal "Tran. Amount"
PX.Objects.CA.BankStatementHelpers.CATranExt.IsBestMatch : Edm.Boolean "Best Match"

# PX.Objects.CA.CAAdj (EntityType)

Label: "Cash Transactions"
Key: AdjRefNbr, AdjTranType
Entity sets: PX_Objects_CA_CAAdj, CashTransactions, CAAdj
Non-filterable, non-selectable: ReverseCount, WorkgroupID, OwnerID, NoteText, HasWithHoldTax, HasUseTax, DepositDate, FormCaptionDescription, CuryRate, DeletedDatabaseRecord

PX.Objects.CA.CAAdj.AdjTranType : Edm.String [key required] "Tran. Type"
PX.Objects.CA.CAAdj.AdjRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CAAdj.ExtRefNbr : Edm.String "Document Ref."
PX.Objects.CA.CAAdj.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.CA.CAAdj.DrCr : Edm.String "Disbursement/Receipt"
PX.Objects.CA.CAAdj.TranDesc : Edm.String "Description"
PX.Objects.CA.CAAdj.TranPeriodID : Edm.String
PX.Objects.CA.CAAdj.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.CA.CAAdj.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.CA.CAAdj.CuryInfoID : Edm.Int64
PX.Objects.CA.CAAdj.OrigAdjTranType : Edm.String "Orig. Tran. Type"
PX.Objects.CA.CAAdj.OrigAdjRefNbr : Edm.String "Orig. Ref. Nbr."
PX.Objects.CA.CAAdj.ReverseCount : Edm.Int32 "Reversing Transactions"
PX.Objects.CA.CAAdj.Draft : Edm.Boolean [required] "Draft"
PX.Objects.CA.CAAdj.Hold : Edm.Boolean "Hold"
PX.Objects.CA.CAAdj.Approved : Edm.Boolean [required] "Approved"
PX.Objects.CA.CAAdj.Rejected : Edm.Boolean [required] "Reject"
PX.Objects.CA.CAAdj.Released : Edm.Boolean [required]
PX.Objects.CA.CAAdj.IsTaxValid : Edm.Boolean [required] "Tax Is Up to Date"
PX.Objects.CA.CAAdj.IsTaxPosted : Edm.Boolean [required] "Tax Is Posted/Committed to External Tax Engine (Avalara)"
PX.Objects.CA.CAAdj.IsTaxSaved : Edm.Boolean [required] "Tax has been saved in the external tax provider"
PX.Objects.CA.CAAdj.NonTaxable : Edm.Boolean [required] "Non-Taxable"
PX.Objects.CA.CAAdj.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.CA.CAAdj.TaxTotal : Edm.Decimal [required]
PX.Objects.CA.CAAdj.CuryVatExemptTotal : Edm.Decimal [required] "Tax Exempt Total"
PX.Objects.CA.CAAdj.VatExemptTotal : Edm.Decimal [required]
PX.Objects.CA.CAAdj.CuryVatTaxableTotal : Edm.Decimal [required] "Taxable Total"
PX.Objects.CA.CAAdj.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.CA.CAAdj.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.CA.CAAdj.TaxAmt : Edm.Decimal [required]
PX.Objects.CA.CAAdj.CurySplitTotal : Edm.Decimal [required] "Detail Total"
PX.Objects.CA.CAAdj.SplitTotal : Edm.Decimal [required]
PX.Objects.CA.CAAdj.CuryTranAmt : Edm.Decimal [required] "Amount"
PX.Objects.CA.CAAdj.TranAmt : Edm.Decimal [required] "Tran. Amount"
PX.Objects.CA.CAAdj.CuryID : Edm.String "Currency"
PX.Objects.CA.CAAdj.CuryControlAmt : Edm.Decimal [required] "Control Total"
PX.Objects.CA.CAAdj.ControlAmt : Edm.Decimal [required]
PX.Objects.CA.CAAdj.EmployeeID : Edm.Int32 "Owner"
PX.Objects.CA.CAAdj.WorkgroupID : Edm.Int32 "Approval Workgroup ID"
PX.Objects.CA.CAAdj.OwnerID : Edm.Int32 "Approver"
PX.Objects.CA.CAAdj.NoteID : Edm.Guid
PX.Objects.CA.CAAdj.NoteText : Edm.String "Note Text"
PX.Objects.CA.CAAdj.CABankTranRefNoteID : Edm.Guid
PX.Objects.CA.CAAdj.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CAAdj.CreatedByScreenID : Edm.String
PX.Objects.CA.CAAdj.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CAAdj.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CAAdj.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CAAdj.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CAAdj.tstamp : Edm.Binary
PX.Objects.CA.CAAdj.LineCntr : Edm.Int32
PX.Objects.CA.CAAdj.TranID : Edm.Int64
PX.Objects.CA.CAAdj.Status : Edm.String "Status"
PX.Objects.CA.CAAdj.EntryTypeID : Edm.String "Entry Type"
PX.Objects.CA.CAAdj.PaymentsReclassification : Edm.Boolean
PX.Objects.CA.CAAdj.Cleared : Edm.Boolean [required] "Cleared"
PX.Objects.CA.CAAdj.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.CA.CAAdj.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CA.CAAdj.CuryTaxRoundDiff : Edm.Decimal [required] "Rounding Diff."
PX.Objects.CA.CAAdj.TaxRoundDiff : Edm.Decimal [required]
PX.Objects.CA.CAAdj.HasWithHoldTax : Edm.Boolean
PX.Objects.CA.CAAdj.HasUseTax : Edm.Boolean
PX.Objects.CA.CAAdj.DontApprove : Edm.Boolean "Don't Approve"
PX.Objects.CA.CAAdj.DepositAsBatch : Edm.Boolean [required] "Batch Deposit"
PX.Objects.CA.CAAdj.DepositAfter : Edm.DateTimeOffset "Deposit After"
PX.Objects.CA.CAAdj.DepositDate : Edm.DateTimeOffset "Batch Deposit Date"
PX.Objects.CA.CAAdj.Deposited : Edm.Boolean [required] "Deposited"
PX.Objects.CA.CAAdj.DepositType : Edm.String
PX.Objects.CA.CAAdj.DepositNbr : Edm.String "Batch Deposit Nbr."
PX.Objects.CA.CAAdj.FormCaptionDescription : Edm.String
PX.Objects.CA.CAAdj.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.CA.CAAdj.EntityUsageType : Edm.String "Tax Exemption Type"
PX.Objects.CA.CAAdj.CuryRate : Edm.Decimal
PX.Objects.CA.CAAdj.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.CAAdj.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.CA.CAAdj.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.CA.CAAdj.CATranByTranID -> PX.Objects.CA.CATran (TranID=TranID)
PX.Objects.CA.CAAdj.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CAAdj.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CAAdj.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CAAdj.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CAAdj.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.CA.CAAdj.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CAAdj.CAAdjByOrigAdjTranType -> PX.Objects.CA.CAAdj (OrigAdjRefNbr=AdjRefNbr, OrigAdjTranType=AdjTranType)
PX.Objects.CA.CAAdj.CADepositByDepositType -> PX.Objects.CA.CADeposit (DepositNbr=RefNbr, DepositType=TranType)
PX.Objects.CA.CAAdj.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.CA.CAAdj.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CAAdj.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CA.CAAdj.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CA.CAAdj.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.CAAdj.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CA.CAAdj.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CA.CAAdj.CASplitCollection -> Collection(PX.Objects.CA.CASplit)

# PX.Objects.CA.CABankChargeTax (EntityType)

Label: "CABankChargeTax"
Key: BankTranID, LineNbr, MatchType, TaxID
Entity sets: PX_Objects_CA_CABankChargeTax, CABankChargeTax

PX.Objects.CA.CABankChargeTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.CA.CABankChargeTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.CA.CABankChargeTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CABankChargeTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankChargeTax.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankChargeTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankChargeTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankChargeTax.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankChargeTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankChargeTax.BankTranID : Edm.Int32 [key]
PX.Objects.CA.CABankChargeTax.LineNbr : Edm.Int32 [key]
PX.Objects.CA.CABankChargeTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.CA.CABankChargeTax.MatchType : Edm.String [key required] "Type"
PX.Objects.CA.CABankChargeTax.CuryInfoID : Edm.Int64
PX.Objects.CA.CABankChargeTax.CuryOrigTaxableAmt : Edm.Decimal
PX.Objects.CA.CABankChargeTax.OrigTaxableAmt : Edm.Decimal
PX.Objects.CA.CABankChargeTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CABankChargeTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CABankChargeTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CABankChargeTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CABankChargeTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CABankChargeTax.tstamp : Edm.Binary
PX.Objects.CA.CABankChargeTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankChargeTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankChargeTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.CA.CABankChargeTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.CA.CABankChargeTax.CABankTranMatchByMatchType -> PX.Objects.CA.CABankTranMatch (BankTranID=TranID, LineNbr=LineNbr, MatchType=MatchType)

# PX.Objects.CA.CABankFeed (EntityType)

Label: "Bank Feed"
Key: BankFeedID
Entity sets: PX_Objects_CA_CABankFeed, BankFeed, CABankFeed
Non-filterable, non-selectable: IsTestFeed, StatementImportSource, NoteText

PX.Objects.CA.CABankFeed.BankFeedID : Edm.String [key] "Bank Feed ID"
PX.Objects.CA.CABankFeed.OrganizationID : Edm.Int32 [required]
PX.Objects.CA.CABankFeed.Status : Edm.String "Status"
PX.Objects.CA.CABankFeed.RetrievalStatus : Edm.String "Retrieval Status"
PX.Objects.CA.CABankFeed.RetrievalDate : Edm.DateTimeOffset "Retrieval Date"
PX.Objects.CA.CABankFeed.Type : Edm.String "Bank Feed Type"
PX.Objects.CA.CABankFeed.AccessToken : Edm.String "AccessToken"
PX.Objects.CA.CABankFeed.ExternalItemID : Edm.String "Item ID/Member ID"
PX.Objects.CA.CABankFeed.ExternalUserID : Edm.String "User ID"
PX.Objects.CA.CABankFeed.Institution : Edm.String "Financial Institution"
PX.Objects.CA.CABankFeed.InstitutionID : Edm.String
PX.Objects.CA.CABankFeed.Descr : Edm.String "Description"
PX.Objects.CA.CABankFeed.CreateExpenseReceipt : Edm.Boolean [required] "Create Expense Receipts"
PX.Objects.CA.CABankFeed.CreateReceiptForPendingTran : Edm.Boolean [required] "Create Expense Receipts for Pending Transactions"
PX.Objects.CA.CABankFeed.CreateReceiptForRefund : Edm.Boolean [required] "Create Expense Receipts for Refunds"
PX.Objects.CA.CABankFeed.MultipleMapping : Edm.Boolean [required] "Map Multiple Bank Accounts to One Cash Account"
PX.Objects.CA.CABankFeed.DefaultExpenseItemID : Edm.Int32 "Default Expense Item"
PX.Objects.CA.CABankFeed.ImportStartDate : Edm.DateTimeOffset "Import Start Date"
PX.Objects.CA.CABankFeed.ErrorMessage : Edm.String "Error message"
PX.Objects.CA.CABankFeed.IsTestFeed : Edm.Boolean
PX.Objects.CA.CABankFeed.StatementImportSource : Edm.String "Statement Import Source"
PX.Objects.CA.CABankFeed.FileAmountFormat : Edm.String "Amount Format"
PX.Objects.CA.CABankFeed.DebitLabel : Edm.String "Disbursement Property"
PX.Objects.CA.CABankFeed.CreditLabel : Edm.String "Receipt Property"
PX.Objects.CA.CABankFeed.FolderPath : Edm.String "URL"
PX.Objects.CA.CABankFeed.FileFormat : Edm.String "File Format"
PX.Objects.CA.CABankFeed.FolderLogin : Edm.String "Login"
PX.Objects.CA.CABankFeed.FolderPassword : Edm.String "Password"
PX.Objects.CA.CABankFeed.SshCertificateName : Edm.String "SSH Private Key"
PX.Objects.CA.CABankFeed.FileName : Edm.String "File Name"
PX.Objects.CA.CABankFeed.UseFileNameWildcards : Edm.Boolean [required] "Use Wildcards (*, ?)"
PX.Objects.CA.CABankFeed.ProviderID : Edm.Guid "Data Provider"
PX.Objects.CA.CABankFeed.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankFeed.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankFeed.AccountQty : Edm.Int32 "Accounts"
PX.Objects.CA.CABankFeed.UnmatchedAccountQty : Edm.Int32 "Unmatched Accounts"
PX.Objects.CA.CABankFeed.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Objects.CA.CABankFeed.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankFeed.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankFeed.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.CA.CABankFeed.Noteid : Edm.Guid "Noteid"
PX.Objects.CA.CABankFeed.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankFeed.Tstamp : Edm.Binary "Tstamp"
PX.Objects.CA.CABankFeed.InventoryItemByDefaultExpenseItemID -> PX.Objects.IN.InventoryItem (DefaultExpenseItemID=InventoryID)
PX.Objects.CA.CABankFeed.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankFeed.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankFeed.SYProviderByProviderID -> PX.Api.SYProvider (ProviderID=ProviderID)
PX.Objects.CA.CABankFeed.CertificateBySshCertificateName -> PX.SM.Certificate (SshCertificateName=Name)
PX.Objects.CA.CABankFeed.CABankFeedAccountMappingCollection -> Collection(PX.Objects.CA.CABankFeedAccountMapping)
PX.Objects.CA.CABankFeed.CABankFeedCorpCardCollection -> Collection(PX.Objects.CA.CABankFeedCorpCard)
PX.Objects.CA.CABankFeed.CABankFeedDetailCollection -> Collection(PX.Objects.CA.CABankFeedDetail)
PX.Objects.CA.CABankFeed.CABankFeedExpenseCollection -> Collection(PX.Objects.CA.CABankFeedExpense)
PX.Objects.CA.CABankFeed.CABankFeedFieldMappingCollection -> Collection(PX.Objects.CA.CABankFeedFieldMapping)

# PX.Objects.CA.CABankFeedAccountMapping (EntityType)

Label: "Bank Feed Account Mapping"
Key: BankFeedAccountMapID
Entity sets: PX_Objects_CA_CABankFeedAccountMapping, BankFeedAccountMapping, CABankFeedAccountMapping

PX.Objects.CA.CABankFeedAccountMapping.BankFeedAccountMapID : Edm.Guid [key]
PX.Objects.CA.CABankFeedAccountMapping.BankFeedID : Edm.String
PX.Objects.CA.CABankFeedAccountMapping.LineNbr : Edm.Int32
PX.Objects.CA.CABankFeedAccountMapping.Type : Edm.String "Bank Feed Type"
PX.Objects.CA.CABankFeedAccountMapping.InstitutionID : Edm.String
PX.Objects.CA.CABankFeedAccountMapping.AccountName : Edm.String
PX.Objects.CA.CABankFeedAccountMapping.AccountMask : Edm.String
PX.Objects.CA.CABankFeedAccountMapping.AccountNameMask : Edm.String
PX.Objects.CA.CABankFeedAccountMapping.CashAccountID : Edm.Int32
PX.Objects.CA.CABankFeedAccountMapping.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankFeedAccountMapping.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankFeedAccountMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankFeedAccountMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankFeedAccountMapping.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankFeedAccountMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankFeedAccountMapping.tstamp : Edm.Binary
PX.Objects.CA.CABankFeedAccountMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankFeedAccountMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankFeedAccountMapping.CABankFeedByBankFeedID -> PX.Objects.CA.CABankFeed (BankFeedID=BankFeedID)
PX.Objects.CA.CABankFeedAccountMapping.CABankFeedDetailByLineNbr -> PX.Objects.CA.CABankFeedDetail (BankFeedID=BankFeedID, LineNbr=LineNbr)
PX.Objects.CA.CABankFeedAccountMapping.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)

# PX.Objects.CA.CABankFeedCorpCard (EntityType)

Label: "Bank Feed Corporate Cards"
Key: BankFeedID, LineNbr
Entity sets: PX_Objects_CA_CABankFeedCorpCard, BankFeedCorporateCards, CABankFeedCorpCard
Non-filterable, non-selectable: CardNumber, CardName, EmployeeName, NoteText

PX.Objects.CA.CABankFeedCorpCard.BankFeedID : Edm.String [key]
PX.Objects.CA.CABankFeedCorpCard.LineNbr : Edm.Int32 [key]
PX.Objects.CA.CABankFeedCorpCard.AccountID : Edm.String "Account Name"
PX.Objects.CA.CABankFeedCorpCard.CashAccountID : Edm.Int32 "Cash Account"
PX.Objects.CA.CABankFeedCorpCard.CorpCardID : Edm.Int32 "Corporate Card ID"
PX.Objects.CA.CABankFeedCorpCard.CardNumber : Edm.String "Card Number"
PX.Objects.CA.CABankFeedCorpCard.CardName : Edm.String "Name"
PX.Objects.CA.CABankFeedCorpCard.EmployeeID : Edm.Int32 "Employee ID"
PX.Objects.CA.CABankFeedCorpCard.EmployeeName : Edm.String "Employee Name"
PX.Objects.CA.CABankFeedCorpCard.MatchField : Edm.String "Field to Match"
PX.Objects.CA.CABankFeedCorpCard.MatchRule : Edm.String "Rule"
PX.Objects.CA.CABankFeedCorpCard.MatchValue : Edm.String "Value"
PX.Objects.CA.CABankFeedCorpCard.Tstamp : Edm.Binary "Tstamp"
PX.Objects.CA.CABankFeedCorpCard.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankFeedCorpCard.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankFeedCorpCard.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankFeedCorpCard.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankFeedCorpCard.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankFeedCorpCard.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankFeedCorpCard.Noteid : Edm.Guid "Noteid"
PX.Objects.CA.CABankFeedCorpCard.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankFeedCorpCard.VendorByEmployeeID -> PX.Objects.AP.Vendor (EmployeeID=BAccountID)
PX.Objects.CA.CABankFeedCorpCard.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankFeedCorpCard.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankFeedCorpCard.CABankFeedByBankFeedID -> PX.Objects.CA.CABankFeed (BankFeedID=BankFeedID)
PX.Objects.CA.CABankFeedCorpCard.CABankFeedDetailByAccountID -> PX.Objects.CA.CABankFeedDetail (AccountID=AccountID)
PX.Objects.CA.CABankFeedCorpCard.CACorpCardByCashAccountID -> PX.Objects.CA.CACorpCard (CorpCardID=CorpCardID)
PX.Objects.CA.CABankFeedCorpCard.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)

# PX.Objects.CA.CABankFeedDetail (EntityType)

Label: "Bank Feed Detail"
Key: BankFeedID, LineNbr
Entity sets: PX_Objects_CA_CABankFeedDetail, BankFeedDetail, CABankFeedDetail
Non-filterable, non-selectable: ImportStartDate, NoteText

PX.Objects.CA.CABankFeedDetail.BankFeedID : Edm.String [key]
PX.Objects.CA.CABankFeedDetail.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.CA.CABankFeedDetail.AccountID : Edm.String "Account ID"
PX.Objects.CA.CABankFeedDetail.AccountName : Edm.String "Account Name"
PX.Objects.CA.CABankFeedDetail.AccountMask : Edm.String "Account Mask"
PX.Objects.CA.CABankFeedDetail.AccountType : Edm.String "Account Type"
PX.Objects.CA.CABankFeedDetail.AccountSubType : Edm.String "Account Subtype"
PX.Objects.CA.CABankFeedDetail.Currency : Edm.String "Currency"
PX.Objects.CA.CABankFeedDetail.Descr : Edm.String "Description"
PX.Objects.CA.CABankFeedDetail.CashAccountID : Edm.Int32 "Cash Account"
PX.Objects.CA.CABankFeedDetail.StatementPeriod : Edm.String "Statement Period"
PX.Objects.CA.CABankFeedDetail.StatementStartDay : Edm.Int32 "Statement Start Day"
PX.Objects.CA.CABankFeedDetail.ImportStartDate : Edm.DateTimeOffset "Import Transactions From"
PX.Objects.CA.CABankFeedDetail.OverrideDate : Edm.Boolean [required]
PX.Objects.CA.CABankFeedDetail.ManualImportDate : Edm.DateTimeOffset
PX.Objects.CA.CABankFeedDetail.RetrievalStatus : Edm.String "Retrieval Status"
PX.Objects.CA.CABankFeedDetail.RetrievalDate : Edm.DateTimeOffset "Retrieval Date"
PX.Objects.CA.CABankFeedDetail.ErrorMessage : Edm.String "Error message"
PX.Objects.CA.CABankFeedDetail.Hidden : Edm.Boolean [required] "Hidden"
PX.Objects.CA.CABankFeedDetail.FileID : Edm.Guid
PX.Objects.CA.CABankFeedDetail.FileRevisionID : Edm.Int32
PX.Objects.CA.CABankFeedDetail.FileDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankFeedDetail.Tstamp : Edm.Binary "Tstamp"
PX.Objects.CA.CABankFeedDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankFeedDetail.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankFeedDetail.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Objects.CA.CABankFeedDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankFeedDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankFeedDetail.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.CA.CABankFeedDetail.Noteid : Edm.Guid "Noteid"
PX.Objects.CA.CABankFeedDetail.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankFeedDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankFeedDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankFeedDetail.CurrencyListByCurrency -> PX.Objects.CM.CurrencyList (Currency=CuryID)
PX.Objects.CA.CABankFeedDetail.CABankFeedByBankFeedID -> PX.Objects.CA.CABankFeed (BankFeedID=BankFeedID)
PX.Objects.CA.CABankFeedDetail.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.CABankFeedDetail.CABankFeedAccountMappingCollection -> Collection(PX.Objects.CA.CABankFeedAccountMapping)
PX.Objects.CA.CABankFeedDetail.CABankFeedCorpCardCollection -> Collection(PX.Objects.CA.CABankFeedCorpCard)

# PX.Objects.CA.CABankFeedExpense (EntityType)

Label: "Bank Feed Expense Items"
Key: BankFeedID, LineNbr
Entity sets: PX_Objects_CA_CABankFeedExpense, BankFeedExpenseItems, CABankFeedExpense
Non-filterable, non-selectable: NoteText

PX.Objects.CA.CABankFeedExpense.BankFeedID : Edm.String [key]
PX.Objects.CA.CABankFeedExpense.LineNbr : Edm.Int32 [key]
PX.Objects.CA.CABankFeedExpense.MatchRule : Edm.String "Rule"
PX.Objects.CA.CABankFeedExpense.MatchField : Edm.String "Field to Match"
PX.Objects.CA.CABankFeedExpense.MatchValue : Edm.String "Value"
PX.Objects.CA.CABankFeedExpense.InventoryItemID : Edm.Int32 "Expense Item"
PX.Objects.CA.CABankFeedExpense.DoNotCreate : Edm.Boolean [required] "Skip"
PX.Objects.CA.CABankFeedExpense.Tstamp : Edm.Binary "Tstamp"
PX.Objects.CA.CABankFeedExpense.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankFeedExpense.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankFeedExpense.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Objects.CA.CABankFeedExpense.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankFeedExpense.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankFeedExpense.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.CA.CABankFeedExpense.Noteid : Edm.Guid "Noteid"
PX.Objects.CA.CABankFeedExpense.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankFeedExpense.InventoryItemByInventoryItemID -> PX.Objects.IN.InventoryItem (InventoryItemID=InventoryID)
PX.Objects.CA.CABankFeedExpense.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankFeedExpense.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankFeedExpense.CABankFeedByBankFeedID -> PX.Objects.CA.CABankFeed (BankFeedID=BankFeedID)

# PX.Objects.CA.CABankFeedFieldMapping (EntityType)

Label: "CABankFeedFieldMapping"
Key: BankFeedID, LineNbr
Entity sets: PX_Objects_CA_CABankFeedFieldMapping, CABankFeedFieldMapping
Non-filterable, non-selectable: NoteText

PX.Objects.CA.CABankFeedFieldMapping.BankFeedID : Edm.String [key]
PX.Objects.CA.CABankFeedFieldMapping.LineNbr : Edm.Int32 [key] "LineNbr"
PX.Objects.CA.CABankFeedFieldMapping.Active : Edm.Boolean [required] "Active"
PX.Objects.CA.CABankFeedFieldMapping.TargetField : Edm.String "Target Field"
PX.Objects.CA.CABankFeedFieldMapping.SourceFieldOrValue : Edm.String "Source Field or Value"
PX.Objects.CA.CABankFeedFieldMapping.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankFeedFieldMapping.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankFeedFieldMapping.CreatedDateTime : Edm.DateTimeOffset "Created Date Time"
PX.Objects.CA.CABankFeedFieldMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankFeedFieldMapping.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankFeedFieldMapping.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date Time"
PX.Objects.CA.CABankFeedFieldMapping.Noteid : Edm.Guid "Noteid"
PX.Objects.CA.CABankFeedFieldMapping.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankFeedFieldMapping.Tstamp : Edm.Binary "Tstamp"
PX.Objects.CA.CABankFeedFieldMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankFeedFieldMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankFeedFieldMapping.CABankFeedByBankFeedID -> PX.Objects.CA.CABankFeed (BankFeedID=BankFeedID)

# PX.Objects.CA.CABankTax (EntityType)

Label: "CA Bank Tax Detail"
Key: BankTranID, BankTranType, LineNbr, TaxID
Entity sets: PX_Objects_CA_CABankTax, CABankTaxDetail, CABankTax

PX.Objects.CA.CABankTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.CA.CABankTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.CA.CABankTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CABankTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTax.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTax.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTax.BankTranID : Edm.Int32 [key]
PX.Objects.CA.CABankTax.LineNbr : Edm.Int32 [key]
PX.Objects.CA.CABankTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.CA.CABankTax.BankTranType : Edm.String [key] "Type"
PX.Objects.CA.CABankTax.CuryInfoID : Edm.Int64
PX.Objects.CA.CABankTax.CuryOrigTaxableAmt : Edm.Decimal
PX.Objects.CA.CABankTax.OrigTaxableAmt : Edm.Decimal
PX.Objects.CA.CABankTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CABankTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CABankTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CABankTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CABankTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CABankTax.tstamp : Edm.Binary
PX.Objects.CA.CABankTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.CA.CABankTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.CA.CABankTax.CABankTranDetailByLineNbr -> PX.Objects.CA.CABankTranDetail (BankTranID=BankTranID, BankTranType=BankTranType, LineNbr=LineNbr)

# PX.Objects.CA.CABankTaxTran (EntityType)

Label: "CA Bank Tax Transaction"
Key: BankTranID, BankTranType, Module, RecordID, TaxID
Entity sets: PX_Objects_CA_CABankTaxTran, CABankTaxTransaction, CABankTaxTran

PX.Objects.CA.CABankTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.CA.CABankTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CABankTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTaxTran.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTaxTran.Module : Edm.String [key required] "Module"
PX.Objects.CA.CABankTaxTran.BankTranType : Edm.String [key] "Type"
PX.Objects.CA.CABankTaxTran.BankTranID : Edm.Int32 [key]
PX.Objects.CA.CABankTaxTran.TranDate : Edm.DateTimeOffset
PX.Objects.CA.CABankTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.CA.CABankTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.CA.CABankTaxTran.VendorID : Edm.Int32
PX.Objects.CA.CABankTaxTran.TaxPeriodID : Edm.String
PX.Objects.CA.CABankTaxTran.FinPeriodID : Edm.String
PX.Objects.CA.CABankTaxTran.FinDate : Edm.DateTimeOffset
PX.Objects.CA.CABankTaxTran.Released : Edm.Boolean [required]
PX.Objects.CA.CABankTaxTran.Voided : Edm.Boolean [required]
PX.Objects.CA.CABankTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.CA.CABankTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.CA.CABankTaxTran.CuryInfoID : Edm.Int64
PX.Objects.CA.CABankTaxTran.CuryTaxDiscountAmt : Edm.Decimal [required]
PX.Objects.CA.CABankTaxTran.TaxDiscountAmt : Edm.Decimal [required]
PX.Objects.CA.CABankTaxTran.CuryOrigTaxableAmt : Edm.Decimal "Orig. Taxable Amount"
PX.Objects.CA.CABankTaxTran.OrigTaxableAmt : Edm.Decimal "Orig. Taxable Amount"
PX.Objects.CA.CABankTaxTran.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CABankTaxTran.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CABankTaxTran.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CABankTaxTran.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CABankTaxTran.BAccountID : Edm.Int32
PX.Objects.CA.CABankTaxTran.CuryTaxAmtSumm : Edm.Decimal [required]
PX.Objects.CA.CABankTaxTran.TaxAmtSumm : Edm.Decimal [required]
PX.Objects.CA.CABankTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CABankTaxTran.CuryID : Edm.String "Currency"
PX.Objects.CA.CABankTaxTran.TaxType : Edm.String
PX.Objects.CA.CABankTaxTran.TaxZoneID : Edm.String
PX.Objects.CA.CABankTaxTran.TaxBucketID : Edm.Int32
PX.Objects.CA.CABankTaxTran.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.CA.CABankTaxTran.TaxInvoiceNbr : Edm.String "Tax Invoice Nbr."
PX.Objects.CA.CABankTaxTran.TaxInvoiceDate : Edm.DateTimeOffset "Tax Invoice Date"
PX.Objects.CA.CABankTaxTran.OrigTranType : Edm.String "Orig. Tran. Type"
PX.Objects.CA.CABankTaxTran.OrigRefNbr : Edm.String "Orig. Doc. Number"
PX.Objects.CA.CABankTaxTran.LineRefNbr : Edm.String "Line Ref. Number"
PX.Objects.CA.CABankTaxTran.RevisionID : Edm.Int32
PX.Objects.CA.CABankTaxTran.AdjdDocType : Edm.String
PX.Objects.CA.CABankTaxTran.AdjdRefNbr : Edm.String
PX.Objects.CA.CABankTaxTran.AdjNbr : Edm.Int32
PX.Objects.CA.CABankTaxTran.Description : Edm.String "Description"
PX.Objects.CA.CABankTaxTran.tstamp : Edm.Binary
PX.Objects.CA.CABankTaxTran.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CABankTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.CA.CABankTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.CA.CABankTaxTran.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CABankTaxTran.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CABankTaxTran.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CA.CABankTaxTran.CABankTranByBankTranID -> PX.Objects.CA.CABankTran (BankTranID=TranID)

# PX.Objects.CA.CABankTaxTranMatch (EntityType)

Label: "CABankTaxTranMatch"
Key: BankTranID, BankTranType, Module, RecordID, TaxID
Entity sets: PX_Objects_CA_CABankTaxTranMatch, CABankTaxTranMatch

PX.Objects.CA.CABankTaxTranMatch.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.CA.CABankTaxTranMatch.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CABankTaxTranMatch.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTaxTranMatch.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTaxTranMatch.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTaxTranMatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTaxTranMatch.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTaxTranMatch.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTaxTranMatch.Module : Edm.String [key required] "Module"
PX.Objects.CA.CABankTaxTranMatch.BankTranType : Edm.String [key] "Type"
PX.Objects.CA.CABankTaxTranMatch.BankTranID : Edm.Int32 [key]
PX.Objects.CA.CABankTaxTranMatch.TranDate : Edm.DateTimeOffset
PX.Objects.CA.CABankTaxTranMatch.TaxID : Edm.String [key] "Tax ID"
PX.Objects.CA.CABankTaxTranMatch.RecordID : Edm.Int32 [key]
PX.Objects.CA.CABankTaxTranMatch.VendorID : Edm.Int32
PX.Objects.CA.CABankTaxTranMatch.TaxPeriodID : Edm.String
PX.Objects.CA.CABankTaxTranMatch.FinPeriodID : Edm.String
PX.Objects.CA.CABankTaxTranMatch.FinDate : Edm.DateTimeOffset
PX.Objects.CA.CABankTaxTranMatch.Released : Edm.Boolean [required]
PX.Objects.CA.CABankTaxTranMatch.Voided : Edm.Boolean [required]
PX.Objects.CA.CABankTaxTranMatch.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.CA.CABankTaxTranMatch.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.CA.CABankTaxTranMatch.CuryInfoID : Edm.Int64
PX.Objects.CA.CABankTaxTranMatch.CuryTaxDiscountAmt : Edm.Decimal [required]
PX.Objects.CA.CABankTaxTranMatch.TaxDiscountAmt : Edm.Decimal [required]
PX.Objects.CA.CABankTaxTranMatch.CuryOrigTaxableAmt : Edm.Decimal "Orig. Taxable Amount"
PX.Objects.CA.CABankTaxTranMatch.OrigTaxableAmt : Edm.Decimal "Orig. Taxable Amount"
PX.Objects.CA.CABankTaxTranMatch.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CABankTaxTranMatch.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CABankTaxTranMatch.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CABankTaxTranMatch.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CABankTaxTranMatch.BAccountID : Edm.Int32
PX.Objects.CA.CABankTaxTranMatch.CuryTaxAmtSumm : Edm.Decimal [required]
PX.Objects.CA.CABankTaxTranMatch.TaxAmtSumm : Edm.Decimal [required]
PX.Objects.CA.CABankTaxTranMatch.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CABankTaxTranMatch.CuryID : Edm.String "Currency"
PX.Objects.CA.CABankTaxTranMatch.TaxType : Edm.String
PX.Objects.CA.CABankTaxTranMatch.TaxZoneID : Edm.String
PX.Objects.CA.CABankTaxTranMatch.TaxBucketID : Edm.Int32
PX.Objects.CA.CABankTaxTranMatch.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.CA.CABankTaxTranMatch.TaxInvoiceNbr : Edm.String "Tax Invoice Nbr."
PX.Objects.CA.CABankTaxTranMatch.TaxInvoiceDate : Edm.DateTimeOffset "Tax Invoice Date"
PX.Objects.CA.CABankTaxTranMatch.OrigTranType : Edm.String "Orig. Tran. Type"
PX.Objects.CA.CABankTaxTranMatch.OrigRefNbr : Edm.String "Orig. Doc. Number"
PX.Objects.CA.CABankTaxTranMatch.LineRefNbr : Edm.String "Line Ref. Number"
PX.Objects.CA.CABankTaxTranMatch.RevisionID : Edm.Int32
PX.Objects.CA.CABankTaxTranMatch.AdjdDocType : Edm.String
PX.Objects.CA.CABankTaxTranMatch.AdjdRefNbr : Edm.String
PX.Objects.CA.CABankTaxTranMatch.AdjNbr : Edm.Int32
PX.Objects.CA.CABankTaxTranMatch.Description : Edm.String "Description"
PX.Objects.CA.CABankTaxTranMatch.tstamp : Edm.Binary
PX.Objects.CA.CABankTaxTranMatch.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CABankTaxTranMatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTaxTranMatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTaxTranMatch.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.CA.CABankTaxTranMatch.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.CA.CABankTaxTranMatch.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CABankTaxTranMatch.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CABankTaxTranMatch.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CA.CABankTaxTranMatch.CABankTranByBankTranID -> PX.Objects.CA.CABankTran (BankTranID=TranID)

# PX.Objects.CA.CABankTran (EntityType)

Label: "Bank Transaction"
Key: TranID
Entity sets: PX_Objects_CA_CABankTran, BankTransaction, CABankTran
Non-filterable, non-selectable: RuleApplied, ApplyRuleEnabled, MatchedToExisting, MatchedToInvoice, MatchedToExpenseReceipt, Status, CuryDebitAmt, CuryCreditAmt, CuryTotalAmt, CuryTotalAmtCopy, CuryTotalAmtDisplay, CuryUnappliedBal, CuryApplAmtMatchToInvoice, CuryApplAmtMatchToPayment, CuryUnappliedBalMatch, CuryUnappliedBalMatchToInvoice, CuryUnappliedBalMatchToPayment, DocType, PayeeBAccountIDCopy, PaymentMethodIDCopy, PMInstanceIDCopy, CountMatches, CountInvoiceMatches, CountExpenseReceiptDetailMatches, MatchStatsInfo, AcctName, PayeeBAccountID1, PayeeLocationID1, PaymentMethodID1, InvoiceInfo1, EntryTypeID1, OrigModule1, CuryWOAmt, WOAmt, SortOrder, NoteText, Cleared, ClearDate, CuryRate

PX.Objects.CA.CABankTran.TranType : Edm.String "Type"
PX.Objects.CA.CABankTran.TranID : Edm.Int32 [key] "ID"
PX.Objects.CA.CABankTran.HeaderRefNbr : Edm.String "Statement Nbr."
PX.Objects.CA.CABankTran.ExtTranID : Edm.String "Ext. Tran. ID"
PX.Objects.CA.CABankTran.DrCr : Edm.String "DrCr"
PX.Objects.CA.CABankTran.CuryID : Edm.String "Currency"
PX.Objects.CA.CABankTran.CuryInfoID : Edm.Int64
PX.Objects.CA.CABankTran.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.CA.CABankTran.MatchingPaymentDate : Edm.DateTimeOffset "Payment Date"
PX.Objects.CA.CABankTran.MatchingFinPeriodID : Edm.String "Fin. Period"
PX.Objects.CA.CABankTran.TranPeriodID : Edm.String
PX.Objects.CA.CABankTran.TranEntryDate : Edm.DateTimeOffset "Tran. Entry Date"
PX.Objects.CA.CABankTran.CuryTranAmt : Edm.Decimal [required] "CuryTranAmt"
PX.Objects.CA.CABankTran.OrigCuryID : Edm.String "Orig. Currency"
PX.Objects.CA.CABankTran.ExtRefNbr : Edm.String "Ext. Ref. Nbr."
PX.Objects.CA.CABankTran.TranDesc : Edm.String "Tran. Desc"
PX.Objects.CA.CABankTran.UserDesc : Edm.String "Custom Tran. Desc."
PX.Objects.CA.CABankTran.PayeeName : Edm.String "Payee/Payer"
PX.Objects.CA.CABankTran.PayeeAddress1 : Edm.String "Payee Address1"
PX.Objects.CA.CABankTran.PayeeCity : Edm.String "Payee City"
PX.Objects.CA.CABankTran.PayeeState : Edm.String "Payee State"
PX.Objects.CA.CABankTran.PayeePostalCode : Edm.String "Payee Postal Code"
PX.Objects.CA.CABankTran.PayeePhone : Edm.String "Payee Phone"
PX.Objects.CA.CABankTran.TranCode : Edm.String "Tran. Code"
PX.Objects.CA.CABankTran.OrigModule : Edm.String "Module"
PX.Objects.CA.CABankTran.PayeeBAccountID : Edm.Int32 "Business Account"
PX.Objects.CA.CABankTran.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.CA.CABankTran.PMInstanceID : Edm.Int32 "Card/Account Nbr."
PX.Objects.CA.CABankTran.InvoiceInfo : Edm.String "Invoice Nbr."
PX.Objects.CA.CABankTran.DocumentMatched : Edm.Boolean [required] "Matched"
PX.Objects.CA.CABankTran.RuleApplied : Edm.Boolean "Rule Applied"
PX.Objects.CA.CABankTran.ApplyRuleEnabled : Edm.Boolean "Create Rule Enabled"
PX.Objects.CA.CABankTran.MatchedToExisting : Edm.Boolean "Matched"
PX.Objects.CA.CABankTran.MatchedToInvoice : Edm.Boolean "Matched to Invoice"
PX.Objects.CA.CABankTran.HistMatchedToInvoice : Edm.Boolean "Matched to Invoice"
PX.Objects.CA.CABankTran.MatchedToExpenseReceipt : Edm.Boolean "Matched To Expense Receipt"
PX.Objects.CA.CABankTran.CreateDocument : Edm.Boolean [required] "Create"
PX.Objects.CA.CABankTran.MultipleMatching : Edm.Boolean [required] "Match to Multiple Documents"
PX.Objects.CA.CABankTran.MultipleMatchingToPayments : Edm.Boolean [required] "Match to Multiple Payments"
PX.Objects.CA.CABankTran.MatchReceiptsAndDisbursements : Edm.Boolean [required] "Match to Receipts and Disbursements"
PX.Objects.CA.CABankTran.Status : Edm.String "Match Type"
PX.Objects.CA.CABankTran.Processed : Edm.Boolean [required] "Processed"
PX.Objects.CA.CABankTran.EntryTypeID : Edm.String "Entry Type ID"
PX.Objects.CA.CABankTran.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.CA.CABankTran.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CA.CABankTran.ChargeTypeID : Edm.String "Charge Type"
PX.Objects.CA.CABankTran.ChargeTaxZoneID : Edm.String "Charge Tax Zone"
PX.Objects.CA.CABankTran.ChargeTaxCalcMode : Edm.String "Charge Tax Calculation Mode"
PX.Objects.CA.CABankTran.ChargeDrCr : Edm.String
PX.Objects.CA.CABankTran.CuryDebitAmt : Edm.Decimal "Receipt"
PX.Objects.CA.CABankTran.CuryCreditAmt : Edm.Decimal "Disbursement"
PX.Objects.CA.CABankTran.CuryTotalAmt : Edm.Decimal "Total Amount"
PX.Objects.CA.CABankTran.CuryTotalAmtCopy : Edm.Decimal "Transaction Amount"
PX.Objects.CA.CABankTran.CuryDetailsWithTaxesTotal : Edm.Decimal [required] "Amount"
PX.Objects.CA.CABankTran.DetailsWithTaxesTotal : Edm.Decimal [required]
PX.Objects.CA.CABankTran.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.CA.CABankTran.TaxTotal : Edm.Decimal [required]
PX.Objects.CA.CABankTran.CuryTotalAmtDisplay : Edm.Decimal "Transaction Amount"
PX.Objects.CA.CABankTran.CuryApplAmtCA : Edm.Decimal "Detail Total"
PX.Objects.CA.CABankTran.CuryUnappliedBalCA : Edm.Decimal [required] "Discrepancy"
PX.Objects.CA.CABankTran.UnappliedBalCA : Edm.Decimal [required]
PX.Objects.CA.CABankTran.CuryApplAmt : Edm.Decimal "Application Amount"
PX.Objects.CA.CABankTran.CuryUnappliedBal : Edm.Decimal "Unapplied Balance"
PX.Objects.CA.CABankTran.CuryApplAmtMatch : Edm.Decimal "Matched Amount"
PX.Objects.CA.CABankTran.CuryApplAmtMatchToInvoice : Edm.Decimal "Matched Amount"
PX.Objects.CA.CABankTran.CuryApplAmtMatchToPayment : Edm.Decimal "Matched Amount"
PX.Objects.CA.CABankTran.CuryUnappliedBalMatch : Edm.Decimal "Unmatched Amount"
PX.Objects.CA.CABankTran.CuryVatExemptTotal : Edm.Decimal [required] "VAT Exempt Total"
PX.Objects.CA.CABankTran.VatExemptTotal : Edm.Decimal [required]
PX.Objects.CA.CABankTran.CuryVatTaxableTotal : Edm.Decimal [required] "VAT Taxable Total"
PX.Objects.CA.CABankTran.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.CA.CABankTran.CuryTaxRoundDiff : Edm.Decimal [required] "Rounding Diff."
PX.Objects.CA.CABankTran.TaxRoundDiff : Edm.Decimal [required]
PX.Objects.CA.CABankTran.CuryChargeAmt : Edm.Decimal "Charge Amount"
PX.Objects.CA.CABankTran.CuryChargeTaxAmt : Edm.Decimal "Charge Tax Amount"
PX.Objects.CA.CABankTran.CuryUnappliedBalMatchToInvoice : Edm.Decimal "Unmatched Amount"
PX.Objects.CA.CABankTran.CuryUnappliedBalMatchToPayment : Edm.Decimal "Unmatched Amount"
PX.Objects.CA.CABankTran.DocType : Edm.String
PX.Objects.CA.CABankTran.LineCntr : Edm.Int32 [required]
PX.Objects.CA.CABankTran.LineCntrCA : Edm.Int32 [required]
PX.Objects.CA.CABankTran.LineCntrMatch : Edm.Int32 [required]
PX.Objects.CA.CABankTran.DetailErrorCount : Edm.Int32 [required]
PX.Objects.CA.CABankTran.PayeeBAccountIDCopy : Edm.Int32 "Business Account"
PX.Objects.CA.CABankTran.PaymentMethodIDCopy : Edm.String "Payment Method"
PX.Objects.CA.CABankTran.PMInstanceIDCopy : Edm.Int32 "Card/Account Nbr."
PX.Objects.CA.CABankTran.RuleID : Edm.Int32 "Applied Rule"
PX.Objects.CA.CABankTran.Hidden : Edm.Boolean [required] "Hidden"
PX.Objects.CA.CABankTran.InvoiceNotFound : Edm.Boolean
PX.Objects.CA.CABankTran.CountMatches : Edm.Int32 "CountMatches"
PX.Objects.CA.CABankTran.CountInvoiceMatches : Edm.Int32 "CountInvoiceMatches"
PX.Objects.CA.CABankTran.CountExpenseReceiptDetailMatches : Edm.Int32 "CountExpenseReceiptDetailMatches"
PX.Objects.CA.CABankTran.MatchStatsInfo : Edm.String "MatchStatsInfo"
PX.Objects.CA.CABankTran.AcctName : Edm.Int32 "Business Account Name"
PX.Objects.CA.CABankTran.PayeeBAccountID1 : Edm.Int32 "Business Account"
PX.Objects.CA.CABankTran.PayeeLocationID1 : Edm.Int32 "Location"
PX.Objects.CA.CABankTran.PaymentMethodID1 : Edm.String "Payment Method"
PX.Objects.CA.CABankTran.InvoiceInfo1 : Edm.String "Invoice Nbr."
PX.Objects.CA.CABankTran.EntryTypeID1 : Edm.String "Entry Type ID"
PX.Objects.CA.CABankTran.OrigModule1 : Edm.String "Module"
PX.Objects.CA.CABankTran.CuryWOAmt : Edm.Decimal "Write-Off Amount"
PX.Objects.CA.CABankTran.WOAmt : Edm.Decimal
PX.Objects.CA.CABankTran.CardNumber : Edm.String "Card Number"
PX.Objects.CA.CABankTran.CountAdjustments : Edm.Int32
PX.Objects.CA.CABankTran.SortOrder : Edm.Int32
PX.Objects.CA.CABankTran.AllowedOperations : Edm.String "Allowed Operations"
PX.Objects.CA.CABankTran.MatchReason : Edm.String "Match Reason"
PX.Objects.CA.CABankTran.LastAutoMatchDate : Edm.DateTimeOffset "Last Auto-Match Date"
PX.Objects.CA.CABankTran.NoteID : Edm.Guid
PX.Objects.CA.CABankTran.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTran.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTran.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTran.tstamp : Edm.Binary
PX.Objects.CA.CABankTran.Cleared : Edm.Boolean
PX.Objects.CA.CABankTran.ClearDate : Edm.DateTimeOffset
PX.Objects.CA.CABankTran.CuryRate : Edm.Decimal
PX.Objects.CA.CABankTran.BAccountByPayeeBAccountID -> PX.Objects.CR.BAccount (PayeeBAccountID=BAccountID)
PX.Objects.CA.CABankTran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CABankTran.CurrencyInfoByOrigCuryID -> PX.Objects.CM.CurrencyInfo (OrigCuryID=CuryInfoID)
PX.Objects.CA.CABankTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTran.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.CA.CABankTran.TaxZoneByChargeTaxZoneID -> PX.Objects.TX.TaxZone (ChargeTaxZoneID=TaxZoneID)
PX.Objects.CA.CABankTran.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CABankTran.CurrencyByOrigCuryID -> PX.Objects.CM.Currency (OrigCuryID=CuryID)
PX.Objects.CA.CABankTran.CABankTranHeaderByTranType -> PX.Objects.CA.CABankTranHeader (HeaderRefNbr=RefNbr, TranType=TranType)
PX.Objects.CA.CABankTran.CABankTranRuleByRuleID -> PX.Objects.CA.CABankTranRule (RuleID=RuleID)
PX.Objects.CA.CABankTran.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.CA.CABankTran.CAEntryTypeByDrCr -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId, DrCr=DrCr)
PX.Objects.CA.CABankTran.CAEntryTypeByChargeTypeID -> PX.Objects.CA.CAEntryType (ChargeTypeID=EntryTypeId)
PX.Objects.CA.CABankTran.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CABankTran.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CABankTran.LocationByPayeeLocationID -> PX.Objects.CR.Location (PayeeBAccountID=BAccountID)
PX.Objects.CA.CABankTran.LocationByPayeeBAccountID -> PX.Objects.CR.Location (PayeeBAccountID=BAccountID)
PX.Objects.CA.CABankTran.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.CA.CABankTran.CustomerPaymentMethodByPaymentMethodID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID, PayeeBAccountID=BAccountID, PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CABankTran.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.CA.CABankTran.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.CA.CABankTran.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.CA.CABankTran.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.CA.CABankTran.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)

# PX.Objects.CA.CABankTranAdjustment (EntityType)

Label: "Bank Transaction Adjustment"
Key: AdjNbr, TranID
Entity sets: PX_Objects_CA_CABankTranAdjustment, BankTransactionAdjustment, CABankTranAdjustment
Non-filterable, non-selectable: SeparateCheck, AdjdCuryID, PrintAdjdDocType, CuryDocBal, CuryAdjustedDocBal, DocBal, CuryDiscBal, CuryAdjustedDiscBal, DiscBal, CuryWhTaxBal, CuryAdjustedWhTaxBal, WhTaxBal, CuryAdjdWOAmt, AdjgWOAmt, NoteText

PX.Objects.CA.CABankTranAdjustment.TranID : Edm.Int32 [key]
PX.Objects.CA.CABankTranAdjustment.AdjdModule : Edm.String
PX.Objects.CA.CABankTranAdjustment.AdjdDocType : Edm.String "Document Type"
PX.Objects.CA.CABankTranAdjustment.AdjdRefNbr : Edm.String "Reference Nbr."
PX.Objects.CA.CABankTranAdjustment.AdjNbr : Edm.Int32 [key required] "Adjustment Nbr."
PX.Objects.CA.CABankTranAdjustment.CuryAdjdAmt : Edm.Decimal "Amount Paid"
PX.Objects.CA.CABankTranAdjustment.SeparateCheck : Edm.Boolean "Pay Separately"
PX.Objects.CA.CABankTranAdjustment.AdjdCuryInfoID : Edm.Int64
PX.Objects.CA.CABankTranAdjustment.AdjdCuryID : Edm.String "Currency"
PX.Objects.CA.CABankTranAdjustment.PrintAdjdDocType : Edm.String "Type"
PX.Objects.CA.CABankTranAdjustment.StubNbr : Edm.String
PX.Objects.CA.CABankTranAdjustment.AdjBatchNbr : Edm.String "Batch Number"
PX.Objects.CA.CABankTranAdjustment.VoidAdjNbr : Edm.Int32
PX.Objects.CA.CABankTranAdjustment.AdjdOrigCuryInfoID : Edm.Int64
PX.Objects.CA.CABankTranAdjustment.AdjgCuryInfoID : Edm.Int64
PX.Objects.CA.CABankTranAdjustment.AdjgDocDate : Edm.DateTimeOffset
PX.Objects.CA.CABankTranAdjustment.AdjgFinPeriodID : Edm.String "Application Period"
PX.Objects.CA.CABankTranAdjustment.AdjgTranPeriodID : Edm.String
PX.Objects.CA.CABankTranAdjustment.AdjdDocDate : Edm.DateTimeOffset "Date"
PX.Objects.CA.CABankTranAdjustment.AdjdFinPeriodID : Edm.String "Post Period"
PX.Objects.CA.CABankTranAdjustment.AdjdClosedFinPeriodID : Edm.String
PX.Objects.CA.CABankTranAdjustment.AdjdTranPeriodID : Edm.String
PX.Objects.CA.CABankTranAdjustment.CuryOrigDocAmt : Edm.Decimal "Invoice Amount"
PX.Objects.CA.CABankTranAdjustment.AdjDiscAmt : Edm.Decimal
PX.Objects.CA.CABankTranAdjustment.CuryAdjdDiscAmt : Edm.Decimal "Cash Discount Taken"
PX.Objects.CA.CABankTranAdjustment.AdjWhTaxAmt : Edm.Decimal [required]
PX.Objects.CA.CABankTranAdjustment.CuryAdjdWhTaxAmt : Edm.Decimal [required] "With. Tax"
PX.Objects.CA.CABankTranAdjustment.AdjAmt : Edm.Decimal
PX.Objects.CA.CABankTranAdjustment.OrigDocAmt : Edm.Decimal
PX.Objects.CA.CABankTranAdjustment.RGOLAmt : Edm.Decimal
PX.Objects.CA.CABankTranAdjustment.Released : Edm.Boolean [required]
PX.Objects.CA.CABankTranAdjustment.Hold : Edm.Boolean [required]
PX.Objects.CA.CABankTranAdjustment.Voided : Edm.Boolean
PX.Objects.CA.CABankTranAdjustment.AdjdCuryRate : Edm.Decimal "Cross Rate"
PX.Objects.CA.CABankTranAdjustment.APExtRefNbr : Edm.String "Vendor Ref."
PX.Objects.CA.CABankTranAdjustment.CuryDocBal : Edm.Decimal "Balance"
PX.Objects.CA.CABankTranAdjustment.CuryAdjustedDocBal : Edm.Decimal "Balance"
PX.Objects.CA.CABankTranAdjustment.DocBal : Edm.Decimal
PX.Objects.CA.CABankTranAdjustment.CuryDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.CA.CABankTranAdjustment.CuryAdjustedDiscBal : Edm.Decimal "Cash Discount Balance"
PX.Objects.CA.CABankTranAdjustment.DiscBal : Edm.Decimal
PX.Objects.CA.CABankTranAdjustment.CuryWhTaxBal : Edm.Decimal "With. Tax Balance"
PX.Objects.CA.CABankTranAdjustment.CuryAdjustedWhTaxBal : Edm.Decimal "With. Tax Balance"
PX.Objects.CA.CABankTranAdjustment.WhTaxBal : Edm.Decimal
PX.Objects.CA.CABankTranAdjustment.WriteOffReasonCode : Edm.String "Write-Off Reason Code"
PX.Objects.CA.CABankTranAdjustment.CuryAdjdWOAmt : Edm.Decimal "Write-Off Amount"
PX.Objects.CA.CABankTranAdjustment.AdjgWOAmt : Edm.Decimal
PX.Objects.CA.CABankTranAdjustment.AdjgBalSign : Edm.Int32
PX.Objects.CA.CABankTranAdjustment.NoteID : Edm.Guid
PX.Objects.CA.CABankTranAdjustment.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankTranAdjustment.tstamp : Edm.Binary
PX.Objects.CA.CABankTranAdjustment.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTranAdjustment.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTranAdjustment.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTranAdjustment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTranAdjustment.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTranAdjustment.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTranAdjustment.APInvoiceByAdjdRefNbr -> PX.Objects.AP.APInvoice (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.CA.CABankTranAdjustment.BatchByAdjBatchNbr -> PX.Objects.GL.Batch (AdjdModule=Module, AdjBatchNbr=BatchNbr)
PX.Objects.CA.CABankTranAdjustment.BranchByAdjdBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CABankTranAdjustment.CurrencyInfoByAdjdCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdCuryInfoID=CuryInfoID)
PX.Objects.CA.CABankTranAdjustment.CurrencyInfoByAdjdOrigCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjdOrigCuryInfoID=CuryInfoID)
PX.Objects.CA.CABankTranAdjustment.CurrencyInfoByAdjgCuryInfoID -> PX.Objects.CM.CurrencyInfo (AdjgCuryInfoID=CuryInfoID)
PX.Objects.CA.CABankTranAdjustment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTranAdjustment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTranAdjustment.ReasonCodeByWriteOffReasonCode -> PX.Objects.CS.ReasonCode (WriteOffReasonCode=ReasonCodeID)
PX.Objects.CA.CABankTranAdjustment.AccountByAdjdAPAcct -> PX.Objects.GL.Account
PX.Objects.CA.CABankTranAdjustment.AccountByAdjdARAcct -> PX.Objects.GL.Account
PX.Objects.CA.CABankTranAdjustment.AccountByAdjdWhTaxAcctID -> PX.Objects.GL.Account
PX.Objects.CA.CABankTranAdjustment.SubByAdjdAPSub -> PX.Objects.GL.Sub
PX.Objects.CA.CABankTranAdjustment.SubByAdjdARSub -> PX.Objects.GL.Sub
PX.Objects.CA.CABankTranAdjustment.SubByAdjdWhTaxSubID -> PX.Objects.GL.Sub
PX.Objects.CA.CABankTranAdjustment.CABankTranByTranID -> PX.Objects.CA.CABankTran (TranID=TranID)

# PX.Objects.CA.CABankTranBAccountMapping (EntityType)

Label: "Bank Transaction Payee Business Account Mapping"
Key: MappingID
Entity sets: PX_Objects_CA_CABankTranBAccountMapping, BankTransactionPayeeBusinessAccountMapping, CABankTranBAccountMapping

PX.Objects.CA.CABankTranBAccountMapping.MappingID : Edm.Int32 [key]
PX.Objects.CA.CABankTranBAccountMapping.CashAccountID : Edm.Int32
PX.Objects.CA.CABankTranBAccountMapping.Payee : Edm.String
PX.Objects.CA.CABankTranBAccountMapping.BAccountID : Edm.Int32
PX.Objects.CA.CABankTranBAccountMapping.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTranBAccountMapping.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTranBAccountMapping.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTranBAccountMapping.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTranBAccountMapping.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTranBAccountMapping.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTranBAccountMapping.tstamp : Edm.Binary
PX.Objects.CA.CABankTranBAccountMapping.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CA.CABankTranBAccountMapping.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTranBAccountMapping.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTranBAccountMapping.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)

# PX.Objects.CA.CABankTranDetail (EntityType)

Label: "CA Bank Transaction Detail"
Key: BankTranID, BankTranType, LineNbr
Entity sets: PX_Objects_CA_CABankTranDetail, CABankTransactionDetail, CABankTranDetail
Non-filterable, non-selectable: NoteText

PX.Objects.CA.CABankTranDetail.BankTranID : Edm.Int32 [key] "BankTranID"
PX.Objects.CA.CABankTranDetail.BankTranType : Edm.String [key] "Type"
PX.Objects.CA.CABankTranDetail.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CA.CABankTranDetail.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.CA.CABankTranDetail.ReferenceID : Edm.Int32
PX.Objects.CA.CABankTranDetail.TranDesc : Edm.String "Description"
PX.Objects.CA.CABankTranDetail.CuryInfoID : Edm.Int64
PX.Objects.CA.CABankTranDetail.CuryTranAmt : Edm.Decimal [required] "Amount"
PX.Objects.CA.CABankTranDetail.TranAmt : Edm.Decimal [required] "Tran. Amount"
PX.Objects.CA.CABankTranDetail.CuryTaxableAmt : Edm.Decimal
PX.Objects.CA.CABankTranDetail.TaxableAmt : Edm.Decimal
PX.Objects.CA.CABankTranDetail.CuryTaxAmt : Edm.Decimal
PX.Objects.CA.CABankTranDetail.TaxAmt : Edm.Decimal
PX.Objects.CA.CABankTranDetail.InventoryID : Edm.Int32 "Item ID"
PX.Objects.CA.CABankTranDetail.Qty : Edm.Decimal "Quantity"
PX.Objects.CA.CABankTranDetail.UnitPrice : Edm.Decimal
PX.Objects.CA.CABankTranDetail.CuryUnitPrice : Edm.Decimal "Price"
PX.Objects.CA.CABankTranDetail.NoteID : Edm.Guid
PX.Objects.CA.CABankTranDetail.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankTranDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTranDetail.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTranDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTranDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTranDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTranDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABankTranDetail.tstamp : Edm.Binary
PX.Objects.CA.CABankTranDetail.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.CA.CABankTranDetail.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.CA.CABankTranDetail.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.CA.CABankTranDetail.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.CA.CABankTranDetail.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.CA.CABankTranDetail.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CABankTranDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CABankTranDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTranDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTranDetail.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.CA.CABankTranDetail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.CA.CABankTranDetail.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CABankTranDetail.AccountBySubID -> PX.Objects.GL.Account
PX.Objects.CA.CABankTranDetail.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CA.CABankTranDetail.CABankTranByBankTranID -> PX.Objects.CA.CABankTran (BankTranID=TranID)
PX.Objects.CA.CABankTranDetail.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CABankTranDetail.CABankTaxCollection -> Collection(PX.Objects.CA.CABankTax)

# PX.Objects.CA.CABankTranHeader (EntityType)

Label: "Bank Statement"
Key: CashAccountID, RefNbr, TranType
Entity sets: PX_Objects_CA_CABankTranHeader, BankStatement, CABankTranHeader
Non-filterable, non-selectable: CuryDetailsEndBalance, NoteText

PX.Objects.CA.CABankTranHeader.TranType : Edm.String [key required] "Type"
PX.Objects.CA.CABankTranHeader.CashAccountID : Edm.Int32 [key] "Cash Account"
PX.Objects.CA.CABankTranHeader.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CABankTranHeader.DocDate : Edm.DateTimeOffset "Statement Date"
PX.Objects.CA.CABankTranHeader.CuryID : Edm.String "Currency"
PX.Objects.CA.CABankTranHeader.StartBalanceDate : Edm.DateTimeOffset "Start Balance Date"
PX.Objects.CA.CABankTranHeader.EndBalanceDate : Edm.DateTimeOffset "End Balance Date"
PX.Objects.CA.CABankTranHeader.CuryBegBalance : Edm.Decimal [required] "Beginning Balance"
PX.Objects.CA.CABankTranHeader.CuryEndBalance : Edm.Decimal [required] "Ending Balance"
PX.Objects.CA.CABankTranHeader.CuryDebitsTotal : Edm.Decimal [required] "Total Receipts"
PX.Objects.CA.CABankTranHeader.CuryCreditsTotal : Edm.Decimal [required] "Total Disbursements"
PX.Objects.CA.CABankTranHeader.CuryDetailsEndBalance : Edm.Decimal "Calculated Balance"
PX.Objects.CA.CABankTranHeader.BankStatementFormat : Edm.String "Bank Statements Format"
PX.Objects.CA.CABankTranHeader.FormatVerisionNbr : Edm.String "Format Verision Nbr"
PX.Objects.CA.CABankTranHeader.TranMaxDate : Edm.DateTimeOffset
PX.Objects.CA.CABankTranHeader.ManualMatchingAllowed : Edm.Boolean [required] "Manual Matching Allowed"
PX.Objects.CA.CABankTranHeader.NoteID : Edm.Guid
PX.Objects.CA.CABankTranHeader.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankTranHeader.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTranHeader.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTranHeader.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CABankTranHeader.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTranHeader.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTranHeader.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CABankTranHeader.tstamp : Edm.Binary
PX.Objects.CA.CABankTranHeader.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTranHeader.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTranHeader.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CABankTranHeader.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.CABankTranHeader.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)

# PX.Objects.CA.CABankTranMatch (EntityType)

Label: "Bank Transaction Match"
Key: LineNbr, MatchType, TranID
Entity sets: PX_Objects_CA_CABankTranMatch, BankTransactionMatch, CABankTranMatch

PX.Objects.CA.CABankTranMatch.TranID : Edm.Int32 [key]
PX.Objects.CA.CABankTranMatch.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CA.CABankTranMatch.MatchType : Edm.String [key required]
PX.Objects.CA.CABankTranMatch.TranType : Edm.String
PX.Objects.CA.CABankTranMatch.CATranID : Edm.Int64
PX.Objects.CA.CABankTranMatch.DocModule : Edm.String
PX.Objects.CA.CABankTranMatch.DocType : Edm.String
PX.Objects.CA.CABankTranMatch.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.CA.CABankTranMatch.DocRefNbr : Edm.String
PX.Objects.CA.CABankTranMatch.ReferenceID : Edm.Int32
PX.Objects.CA.CABankTranMatch.CuryAmt : Edm.Decimal
PX.Objects.CA.CABankTranMatch.CuryApplAmt : Edm.Decimal
PX.Objects.CA.CABankTranMatch.CuryApplTaxableAmt : Edm.Decimal
PX.Objects.CA.CABankTranMatch.CuryApplTaxAmt : Edm.Decimal
PX.Objects.CA.CABankTranMatch.IsCharge : Edm.Boolean
PX.Objects.CA.CABankTranMatch.CuryInfoID : Edm.Int64
PX.Objects.CA.CABankTranMatch.tstamp : Edm.Binary
PX.Objects.CA.CABankTranMatch.APInvoiceByDocRefNbr -> PX.Objects.AP.APInvoice (DocType=DocType, DocRefNbr=RefNbr)
PX.Objects.CA.CABankTranMatch.ARInvoiceByDocRefNbr -> PX.Objects.AR.ARInvoice (DocType=DocType, DocRefNbr=RefNbr)
PX.Objects.CA.CABankTranMatch.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.CA.CABankTranMatch.CATranByCATranID -> PX.Objects.CA.CATran (CATranID=TranID)
PX.Objects.CA.CABankTranMatch.CABankTranByTranID -> PX.Objects.CA.CABankTran (TranID=TranID)
PX.Objects.CA.CABankTranMatch.CABankChargeTaxCollection -> Collection(PX.Objects.CA.CABankChargeTax)

# PX.Objects.CA.CABankTranMatch2 (EntityType)

Label: "Bank Transaction Match"
BaseType: PX.Objects.CA.CABankTranMatch
Key: LineNbr, MatchType, TranID (inherited from PX.Objects.CA.CABankTranMatch)
Entity sets: PX_Objects_CA_CABankTranMatch2

# PX.Objects.CA.CABankTranRule (EntityType)

Label: "CA Bank Transactions Rule"
Key: RuleID
Entity sets: PX_Objects_CA_CABankTranRule, CABankTransactionsRule, CABankTranRule
Non-filterable, non-selectable: CuryMinTranAmt, NoteText

PX.Objects.CA.CABankTranRule.RuleID : Edm.Int32 [key] "Rule ID"
PX.Objects.CA.CABankTranRule.Description : Edm.String "Rule Description"
PX.Objects.CA.CABankTranRule.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CA.CABankTranRule.BankDrCr : Edm.String "Debit/Credit"
PX.Objects.CA.CABankTranRule.TranCuryID : Edm.String "Currency"
PX.Objects.CA.CABankTranRule.AmountMatchingMode : Edm.String "Matching Mode"
PX.Objects.CA.CABankTranRule.CuryTranAmt : Edm.Decimal "Amount"
PX.Objects.CA.CABankTranRule.CuryMinTranAmt : Edm.Decimal "Min. Amount"
PX.Objects.CA.CABankTranRule.MaxCuryTranAmt : Edm.Decimal "Max. Amount"
PX.Objects.CA.CABankTranRule.TranCode : Edm.String "Tran. Code"
PX.Objects.CA.CABankTranRule.BankTranDescription : Edm.String "Tran. Description"
PX.Objects.CA.CABankTranRule.MatchDescriptionCase : Edm.Boolean [required] "Match Case"
PX.Objects.CA.CABankTranRule.UseDescriptionWildcards : Edm.Boolean [required] "Use Wildcards (*, ?)"
PX.Objects.CA.CABankTranRule.PayeeName : Edm.String "Payee/Payer"
PX.Objects.CA.CABankTranRule.UsePayeeNameWildcards : Edm.Boolean [required] "Use Wildcards (*, ?)"
PX.Objects.CA.CABankTranRule.Action : Edm.String "Action"
PX.Objects.CA.CABankTranRule.DocumentModule : Edm.String "Resulting Document Module"
PX.Objects.CA.CABankTranRule.DocumentEntryTypeID : Edm.String "Resulting Entry Type"
PX.Objects.CA.CABankTranRule.NoteID : Edm.Guid
PX.Objects.CA.CABankTranRule.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABankTranRule.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABankTranRule.CreatedByScreenID : Edm.String
PX.Objects.CA.CABankTranRule.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CABankTranRule.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABankTranRule.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABankTranRule.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CABankTranRule.tstamp : Edm.Binary
PX.Objects.CA.CABankTranRule.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABankTranRule.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABankTranRule.CurrencyByTranCuryID -> PX.Objects.CM.Currency (TranCuryID=CuryID)
PX.Objects.CA.CABankTranRule.CAEntryTypeByDocumentEntryTypeID -> PX.Objects.CA.CAEntryType (DocumentEntryTypeID=EntryTypeId)
PX.Objects.CA.CABankTranRule.CAEntryTypeByBankDrCr -> PX.Objects.CA.CAEntryType (DocumentEntryTypeID=EntryTypeId, DocumentModule=Module, BankDrCr=DrCr)
PX.Objects.CA.CABankTranRule.CashAccountByBankTranCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CABankTranRule.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)

# PX.Objects.CA.CABankTranRulePopup (EntityType)

Label: "CA Bank Transactions Rule"
BaseType: PX.Objects.CA.CABankTranRule
Key: RuleID (inherited from PX.Objects.CA.CABankTranRule)
Entity sets: PX_Objects_CA_CABankTranRulePopup

# PX.Objects.CA.CABatch (EntityType)

Label: "CA Batch"
Key: BatchNbr
Entity sets: PX_Objects_CA_CABatch, CABatch
Non-filterable, non-selectable: Status, NoteText, Total, FormCaptionDescription, DeletedDatabaseRecord

PX.Objects.CA.CABatch.BatchNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CABatch.OrigModule : Edm.String "Module"
PX.Objects.CA.CABatch.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.CA.CABatch.ReferenceID : Edm.Int32 "Bank"
PX.Objects.CA.CABatch.BatchSeqNbr : Edm.String "Batch Seq. Number"
PX.Objects.CA.CABatch.ExtRefNbr : Edm.String "Document Ref."
PX.Objects.CA.CABatch.TranDate : Edm.DateTimeOffset "Batch Date"
PX.Objects.CA.CABatch.TranDesc : Edm.String "Description"
PX.Objects.CA.CABatch.DateSeqNbr : Edm.Int16 [required] "Seq. Number Within Day"
PX.Objects.CA.CABatch.SkipExport : Edm.Boolean "Release Batch Payment Before Export"
PX.Objects.CA.CABatch.Hold : Edm.Boolean "Hold"
PX.Objects.CA.CABatch.Exported : Edm.Boolean [required] "Exported"
PX.Objects.CA.CABatch.Canceled : Edm.Boolean [required] "Canceled"
PX.Objects.CA.CABatch.Voided : Edm.Boolean [required] "Voided"
PX.Objects.CA.CABatch.Released : Edm.Boolean [required] "Released"
PX.Objects.CA.CABatch.Status : Edm.String "Status"
PX.Objects.CA.CABatch.CuryID : Edm.String "Currency"
PX.Objects.CA.CABatch.CuryDetailTotal : Edm.Decimal [required] "Batch Total"
PX.Objects.CA.CABatch.DetailTotal : Edm.Decimal [required]
PX.Objects.CA.CABatch.Cleared : Edm.Boolean [required] "Cleared"
PX.Objects.CA.CABatch.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.CA.CABatch.VoidDate : Edm.DateTimeOffset "Void Date"
PX.Objects.CA.CABatch.NoteID : Edm.Guid
PX.Objects.CA.CABatch.NoteText : Edm.String "Note Text"
PX.Objects.CA.CABatch.ExportFileName : Edm.String "Exported File Name"
PX.Objects.CA.CABatch.ExportTime : Edm.DateTimeOffset "File Export Time"
PX.Objects.CA.CABatch.CountOfPayments : Edm.Int32 "Payment Count"
PX.Objects.CA.CABatch.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABatch.CreatedByScreenID : Edm.String
PX.Objects.CA.CABatch.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CABatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABatch.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABatch.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CABatch.tstamp : Edm.Binary
PX.Objects.CA.CABatch.Total : Edm.Decimal
PX.Objects.CA.CABatch.Reconciled : Edm.Boolean [required]
PX.Objects.CA.CABatch.ReconDate : Edm.DateTimeOffset
PX.Objects.CA.CABatch.ReconNbr : Edm.String
PX.Objects.CA.CABatch.FormCaptionDescription : Edm.String
PX.Objects.CA.CABatch.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.CABatch.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.CA.CABatch.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CABatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CABatch.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CABatch.CAReconByReconNbr -> PX.Objects.CA.CARecon (ReconNbr=ReconNbr)
PX.Objects.CA.CABatch.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CABatch.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CABatch.CABatchDetailCollection -> Collection(PX.Objects.CA.CABatchDetail)
PX.Objects.CA.CABatch.PRPaymentBatchExportDetailsCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportDetails)
PX.Objects.CA.CABatch.PRPaymentBatchExportHistoryCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportHistory)

# PX.Objects.CA.CABatchDetail (EntityType)

Label: "CA Batch Details"
Key: BatchNbr, OrigDocType, OrigLineNbr, OrigModule, OrigRefNbr
Entity sets: PX_Objects_CA_CABatchDetail, CABatchDetails, CABatchDetail

PX.Objects.CA.CABatchDetail.BatchNbr : Edm.String [key]
PX.Objects.CA.CABatchDetail.OrigModule : Edm.String [key required] "Module"
PX.Objects.CA.CABatchDetail.OrigDocType : Edm.String [key] "Doc. Type"
PX.Objects.CA.CABatchDetail.OrigRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CABatchDetail.OrigLineNbr : Edm.Int32 [key required] "Line Nbr."
PX.Objects.CA.CABatchDetail.AddendaPaymentRelatedInfo : Edm.String "Payment-Related Info (Addenda)"
PX.Objects.CA.CABatchDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CABatchDetail.CreatedByScreenID : Edm.String
PX.Objects.CA.CABatchDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABatchDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CABatchDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CABatchDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CABatchDetail.APPaymentByOrigRefNbr -> PX.Objects.AP.APPayment (OrigDocType=DocType, OrigRefNbr=RefNbr)
PX.Objects.CA.CABatchDetail.CABatchByBatchNbr -> PX.Objects.CA.CABatch (BatchNbr=BatchNbr)
PX.Objects.CA.CABatchDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CABatchDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CA.CABatchDetailOrigDocAggregate (EntityType)

Label: "Aggregated CA Batch Details"
BaseType: PX.Objects.CA.CABatchDetail
Key: BatchNbr, OrigDocType, OrigLineNbr, OrigModule, OrigRefNbr (inherited from PX.Objects.CA.CABatchDetail)
Entity sets: PX_Objects_CA_CABatchDetailOrigDocAggregate, AggregatedCABatchDetails, CABatchDetailOrigDocAggregate

# PX.Objects.CA.CACorpCard (EntityType)

Label: "Corporate Card"
Key: CorpCardCD
Entity sets: PX_Objects_CA_CACorpCard, CorporateCard, CACorpCard
Non-filterable, non-selectable: NoteText

PX.Objects.CA.CACorpCard.CorpCardID : Edm.Int32 "Corporate Card ID"
PX.Objects.CA.CACorpCard.CorpCardCD : Edm.String [key] "Corporate Card ID"
PX.Objects.CA.CACorpCard.Name : Edm.String "Name"
PX.Objects.CA.CACorpCard.CardNumber : Edm.String "Card Number"
PX.Objects.CA.CACorpCard.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CA.CACorpCard.Tstamp : Edm.Binary
PX.Objects.CA.CACorpCard.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CACorpCard.CreatedByScreenID : Edm.String
PX.Objects.CA.CACorpCard.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CACorpCard.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CACorpCard.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CACorpCard.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CACorpCard.Noteid : Edm.Guid
PX.Objects.CA.CACorpCard.NoteText : Edm.String "Note Text"
PX.Objects.CA.CACorpCard.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CACorpCard.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CACorpCard.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CACorpCard.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CACorpCard.CashAccountByBranchID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CACorpCard.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CA.CACorpCard.CABankFeedCorpCardCollection -> Collection(PX.Objects.CA.CABankFeedCorpCard)
PX.Objects.CA.CACorpCard.EPEmployeeCorpCardLinkCollection -> Collection(PX.Objects.EP.DAC.EPEmployeeCorpCardLink)

# PX.Objects.CA.CADailySummary (EntityType)

Label: "CA Daily Summary"
Key: CashAccountID, TranDate
Entity sets: PX_Objects_CA_CADailySummary, CADailySummary

PX.Objects.CA.CADailySummary.CashAccountID : Edm.Int32 [key] "Cash Account"
PX.Objects.CA.CADailySummary.TranDate : Edm.DateTimeOffset [key]
PX.Objects.CA.CADailySummary.AmtReleasedClearedDr : Edm.Decimal [required]
PX.Objects.CA.CADailySummary.AmtUnreleasedClearedDr : Edm.Decimal [required]
PX.Objects.CA.CADailySummary.AmtReleasedUnclearedDr : Edm.Decimal [required]
PX.Objects.CA.CADailySummary.AmtUnreleasedUnclearedDr : Edm.Decimal [required]
PX.Objects.CA.CADailySummary.AmtReleasedClearedCr : Edm.Decimal [required]
PX.Objects.CA.CADailySummary.AmtUnreleasedClearedCr : Edm.Decimal [required]
PX.Objects.CA.CADailySummary.AmtReleasedUnclearedCr : Edm.Decimal [required]
PX.Objects.CA.CADailySummary.AmtUnreleasedUnclearedCr : Edm.Decimal [required]
PX.Objects.CA.CADailySummary.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)

# PX.Objects.CA.CADeposit (EntityType)

Label: "CA Deposit"
Key: RefNbr, TranType
Entity sets: PX_Objects_CA_CADeposit, CADeposit
Non-filterable, non-selectable: NoteText, ChargeMult, FormCaptionDescription, IsManual, AdjustmentCounter, CuryRate, DeletedDatabaseRecord

PX.Objects.CA.CADeposit.TranType : Edm.String [key required] "Tran. Type"
PX.Objects.CA.CADeposit.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CADeposit.ExtRefNbr : Edm.String "Document Ref."
PX.Objects.CA.CADeposit.TranDate : Edm.DateTimeOffset "Deposit Date"
PX.Objects.CA.CADeposit.DrCr : Edm.String
PX.Objects.CA.CADeposit.TranDesc : Edm.String "Description"
PX.Objects.CA.CADeposit.TranPeriodID : Edm.String
PX.Objects.CA.CADeposit.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.CA.CADeposit.Hold : Edm.Boolean "Hold"
PX.Objects.CA.CADeposit.Released : Edm.Boolean [required]
PX.Objects.CA.CADeposit.Voided : Edm.Boolean [required] "Voided"
PX.Objects.CA.CADeposit.Status : Edm.String "Status"
PX.Objects.CA.CADeposit.CuryID : Edm.String "Currency"
PX.Objects.CA.CADeposit.CuryInfoID : Edm.Int64
PX.Objects.CA.CADeposit.CuryTranAmt : Edm.Decimal [required] "Total Amount"
PX.Objects.CA.CADeposit.TranAmt : Edm.Decimal [required] "Tran Amount"
PX.Objects.CA.CADeposit.CuryDetailTotal : Edm.Decimal [required] "Deposits Total"
PX.Objects.CA.CADeposit.DetailTotal : Edm.Decimal [required]
PX.Objects.CA.CADeposit.CuryChargeTotal : Edm.Decimal [required] "Charge Total"
PX.Objects.CA.CADeposit.ChargeTotal : Edm.Decimal [required]
PX.Objects.CA.CADeposit.CuryExtraCashTotal : Edm.Decimal [required] "Cash Drop Amount"
PX.Objects.CA.CADeposit.ExtraCashTotal : Edm.Decimal [required]
PX.Objects.CA.CADeposit.CuryControlAmt : Edm.Decimal [required] "Control Total"
PX.Objects.CA.CADeposit.ControlAmt : Edm.Decimal [required]
PX.Objects.CA.CADeposit.LineCntr : Edm.Int32
PX.Objects.CA.CADeposit.LineCntrCharge : Edm.Int32 [required]
PX.Objects.CA.CADeposit.TranID : Edm.Int64
PX.Objects.CA.CADeposit.CashTranID : Edm.Int64
PX.Objects.CA.CADeposit.ChargeTranID : Edm.Int64
PX.Objects.CA.CADeposit.ChargesSeparate : Edm.Boolean [required] "Separate Charges"
PX.Objects.CA.CADeposit.Cleared : Edm.Boolean [required] "Cleared"
PX.Objects.CA.CADeposit.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.CA.CADeposit.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CA.CADeposit.OwnerID : Edm.Int32 "Owner"
PX.Objects.CA.CADeposit.NoteID : Edm.Guid
PX.Objects.CA.CADeposit.NoteText : Edm.String "Note Text"
PX.Objects.CA.CADeposit.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CADeposit.CreatedByScreenID : Edm.String
PX.Objects.CA.CADeposit.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CADeposit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CADeposit.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CADeposit.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CADeposit.tstamp : Edm.Binary
PX.Objects.CA.CADeposit.ChargeMult : Edm.Decimal "Control Total"
PX.Objects.CA.CADeposit.FormCaptionDescription : Edm.String
PX.Objects.CA.CADeposit.IsManual : Edm.Boolean
PX.Objects.CA.CADeposit.AdjustmentCounter : Edm.Int32
PX.Objects.CA.CADeposit.CuryRate : Edm.Decimal
PX.Objects.CA.CADeposit.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.CADeposit.CATranByTranID -> PX.Objects.CA.CATran (TranID=TranID)
PX.Objects.CA.CADeposit.CATranByCashTranID -> PX.Objects.CA.CATran (CashTranID=TranID)
PX.Objects.CA.CADeposit.CATranByChargeTranID -> PX.Objects.CA.CATran (ChargeTranID=TranID)
PX.Objects.CA.CADeposit.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CA.CADeposit.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CADeposit.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CADeposit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CADeposit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CADeposit.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CA.CADeposit.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CADeposit.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CADeposit.CashAccountByExtraCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CADeposit.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CA.CADeposit.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CA.CADeposit.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CA.CADeposit.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CA.CADeposit.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.CA.CADeposit.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CA.CADeposit.CCBatchCollection -> Collection(PX.Objects.CA.CCBatch)

# PX.Objects.CA.CADepositCharge (EntityType)

Label: "CA Deposit Charge"
Key: LineNbr, RefNbr, TranType
Entity sets: PX_Objects_CA_CADepositCharge, CADepositCharge

PX.Objects.CA.CADepositCharge.TranType : Edm.String [key] "Tran. Type"
PX.Objects.CA.CADepositCharge.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CADepositCharge.LineNbr : Edm.Int32 [key]
PX.Objects.CA.CADepositCharge.EntryTypeID : Edm.String "Charge"
PX.Objects.CA.CADepositCharge.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.CA.CADepositCharge.DrCr : Edm.String "Disb. / Receipt"
PX.Objects.CA.CADepositCharge.ChargeRate : Edm.Decimal "Charge Rate"
PX.Objects.CA.CADepositCharge.CuryInfoID : Edm.Int64
PX.Objects.CA.CADepositCharge.CuryChargeableAmt : Edm.Decimal "Chargeable Amount"
PX.Objects.CA.CADepositCharge.ChargeableAmt : Edm.Decimal
PX.Objects.CA.CADepositCharge.CuryChargeAmt : Edm.Decimal "Charge Amount"
PX.Objects.CA.CADepositCharge.ChargeAmt : Edm.Decimal "Charge Amount"
PX.Objects.CA.CADepositCharge.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CADepositCharge.CreatedByScreenID : Edm.String
PX.Objects.CA.CADepositCharge.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CADepositCharge.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CADepositCharge.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CADepositCharge.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CADepositCharge.tstamp : Edm.Binary
PX.Objects.CA.CADepositCharge.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CADepositCharge.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CADepositCharge.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CADepositCharge.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CADepositCharge.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CA.CADepositCharge.CADepositByRefNbr -> PX.Objects.CA.CADeposit (TranType=TranType, RefNbr=RefNbr)
PX.Objects.CA.CADepositCharge.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.CA.CADepositCharge.CashAccountByDepositAcctID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CADepositCharge.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)

# PX.Objects.CA.CADepositDetail (EntityType)

Label: "CA Deposit Detail"
Key: LineNbr, RefNbr, TranType
Entity sets: PX_Objects_CA_CADepositDetail, CADepositDetail
Non-filterable, non-selectable: ChargeEntryTypeID, SourceDrCr, CuryChargeTotal, ChargeTotal, CuryConsolidateChargeTotal, ConsolidateChargeTotal, DepositAfter, CuryOrigAmtSigned, OrigAmtSigned

PX.Objects.CA.CADepositDetail.TranType : Edm.String [key] "Tran. Type"
PX.Objects.CA.CADepositDetail.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CADepositDetail.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CA.CADepositDetail.DetailType : Edm.String "Detail. Type"
PX.Objects.CA.CADepositDetail.OrigModule : Edm.String "Doc. Module"
PX.Objects.CA.CADepositDetail.OrigDocType : Edm.String "Doc.Type"
PX.Objects.CA.CADepositDetail.OrigRefNbr : Edm.String "Reference Nbr."
PX.Objects.CA.CADepositDetail.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.CA.CADepositDetail.DrCr : Edm.String "Disb. / Receipt"
PX.Objects.CA.CADepositDetail.TranDesc : Edm.String "Description"
PX.Objects.CA.CADepositDetail.CuryInfoID : Edm.Int64
PX.Objects.CA.CADepositDetail.CuryTranAmt : Edm.Decimal [required] "Deposit Amount"
PX.Objects.CA.CADepositDetail.TranAmt : Edm.Decimal [required] "Tran Amount"
PX.Objects.CA.CADepositDetail.OrigCuryID : Edm.String "Currency"
PX.Objects.CA.CADepositDetail.OrigCuryInfoID : Edm.Int64
PX.Objects.CA.CADepositDetail.OrigDrCr : Edm.String
PX.Objects.CA.CADepositDetail.CuryOrigAmt : Edm.Decimal [required] "Original Amount"
PX.Objects.CA.CADepositDetail.OrigAmt : Edm.Decimal [required]
PX.Objects.CA.CADepositDetail.TranID : Edm.Int64 "CA Tran ID"
PX.Objects.CA.CADepositDetail.ChargeEntryTypeID : Edm.String "Charge Type"
PX.Objects.CA.CADepositDetail.Voided : Edm.Boolean [required] "Voided"
PX.Objects.CA.CADepositDetail.SourceDrCr : Edm.String
PX.Objects.CA.CADepositDetail.CuryChargeTotal : Edm.Decimal
PX.Objects.CA.CADepositDetail.ChargeTotal : Edm.Decimal
PX.Objects.CA.CADepositDetail.CuryConsolidateChargeTotal : Edm.Decimal
PX.Objects.CA.CADepositDetail.ConsolidateChargeTotal : Edm.Decimal
PX.Objects.CA.CADepositDetail.DepositAfter : Edm.DateTimeOffset
PX.Objects.CA.CADepositDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CADepositDetail.CreatedByScreenID : Edm.String
PX.Objects.CA.CADepositDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CADepositDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CADepositDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CADepositDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CADepositDetail.tstamp : Edm.Binary
PX.Objects.CA.CADepositDetail.CuryOrigAmtSigned : Edm.Decimal
PX.Objects.CA.CADepositDetail.OrigAmtSigned : Edm.Decimal
PX.Objects.CA.CADepositDetail.ARPaymentByOrigRefNbr -> PX.Objects.AR.ARPayment (OrigDocType=DocType, OrigRefNbr=RefNbr)
PX.Objects.CA.CADepositDetail.APPaymentByOrigRefNbr -> PX.Objects.AP.APPayment (OrigDocType=DocType, OrigRefNbr=RefNbr)
PX.Objects.CA.CADepositDetail.CATranByTranID -> PX.Objects.CA.CATran (TranID=TranID)
PX.Objects.CA.CADepositDetail.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CADepositDetail.CurrencyInfoByOrigCuryInfoID -> PX.Objects.CM.CurrencyInfo (OrigCuryInfoID=CuryInfoID)
PX.Objects.CA.CADepositDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CADepositDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CADepositDetail.CurrencyByOrigCuryID -> PX.Objects.CM.Currency (OrigCuryID=CuryID)
PX.Objects.CA.CADepositDetail.CAAdjByOrigRefNbr -> PX.Objects.CA.CAAdj (OrigDocType=AdjTranType, OrigRefNbr=AdjRefNbr)
PX.Objects.CA.CADepositDetail.CADepositByRefNbr -> PX.Objects.CA.CADeposit (TranType=TranType, RefNbr=RefNbr)
PX.Objects.CA.CADepositDetail.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CADepositDetail.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)

# PX.Objects.CA.CAEntryType (EntityType)

Label: "CA Entry Type"
Key: EntryTypeId
Entity sets: PX_Objects_CA_CAEntryType, CAEntryType
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CA.CAEntryType.EntryTypeId : Edm.String [key] "Entry Type ID"
PX.Objects.CA.CAEntryType.Module : Edm.String "Module"
PX.Objects.CA.CAEntryType.ReferenceID : Edm.Int32 "Business Account"
PX.Objects.CA.CAEntryType.DrCr : Edm.String "Disb./Receipt"
PX.Objects.CA.CAEntryType.Descr : Edm.String "Entry Type Description"
PX.Objects.CA.CAEntryType.UseToReclassifyPayments : Edm.Boolean [required] "Use for Payment Reclassification"
PX.Objects.CA.CAEntryType.Consolidate : Edm.Boolean [required] "Deduct from Payment"
PX.Objects.CA.CAEntryType.tstamp : Edm.Binary
PX.Objects.CA.CAEntryType.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CAEntryType.CreatedByScreenID : Edm.String
PX.Objects.CA.CAEntryType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CAEntryType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CAEntryType.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CAEntryType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CAEntryType.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.CAEntryType.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.CA.CAEntryType.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CAEntryType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CAEntryType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CAEntryType.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CAEntryType.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CA.CAEntryType.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CAEntryType.CABankTranRuleCollection -> Collection(PX.Objects.CA.CABankTranRule)
PX.Objects.CA.CAEntryType.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CA.CAEntryType.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.CAEntryType.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CA.CAEntryType.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.CA.CAEntryType.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.CA.CAEntryType.CASetupCollection -> Collection(PX.Objects.CA.CASetup)
PX.Objects.CA.CAEntryType.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.Objects.CA.CAEntryType.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.CA.CAEntryType.CCProcessingCenterFeeTypeCollection -> Collection(PX.Objects.CA.CCProcessingCenterFeeType)
PX.Objects.CA.CAEntryType.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.CA.CAEntryType.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.CA.CAEntryType.CashAccountDepositCollection -> Collection(PX.Objects.CA.CashAccountDeposit)
PX.Objects.CA.CAEntryType.BCFeeMappingCollection -> Collection(PX.Commerce.Objects.BCFeeMapping)

# PX.Objects.CA.CAExpense (EntityType)

Label: "CAExpense"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_CA_CAExpense, CAExpense
Non-filterable, non-selectable: AdjCuryRate, HasWithHoldTax, HasUseTax, NoteText

PX.Objects.CA.CAExpense.RefNbr : Edm.String [key]
PX.Objects.CA.CAExpense.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CA.CAExpense.TranDate : Edm.DateTimeOffset "Doc. Date"
PX.Objects.CA.CAExpense.TranPeriodID : Edm.String
PX.Objects.CA.CAExpense.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.CA.CAExpense.CuryInfoID : Edm.Int64
PX.Objects.CA.CAExpense.CuryID : Edm.String "Currency"
PX.Objects.CA.CAExpense.AdjCuryRate : Edm.Decimal "Currency Rate"
PX.Objects.CA.CAExpense.EntryTypeID : Edm.String "Entry Type"
PX.Objects.CA.CAExpense.DrCr : Edm.String "Disb./Receipt"
PX.Objects.CA.CAExpense.CashTranID : Edm.Int64
PX.Objects.CA.CAExpense.CuryTaxableAmt : Edm.Decimal [required] "Amount"
PX.Objects.CA.CAExpense.TaxableAmt : Edm.Decimal [required] "Amount"
PX.Objects.CA.CAExpense.CuryTranAmt : Edm.Decimal [required] "Total Amount"
PX.Objects.CA.CAExpense.TranAmt : Edm.Decimal [required] "Total Amount"
PX.Objects.CA.CAExpense.Released : Edm.Boolean [required] "Released"
PX.Objects.CA.CAExpense.Cleared : Edm.Boolean "Cleared"
PX.Objects.CA.CAExpense.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.CA.CAExpense.ExtRefNbr : Edm.String "Document Ref."
PX.Objects.CA.CAExpense.TranDesc : Edm.String "Description"
PX.Objects.CA.CAExpense.BatchNbr : Edm.String "Batch Number"
PX.Objects.CA.CAExpense.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.CA.CAExpense.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.CA.CAExpense.CuryTaxTotal : Edm.Decimal [required] "Tax Total"
PX.Objects.CA.CAExpense.TaxTotal : Edm.Decimal [required]
PX.Objects.CA.CAExpense.CuryVatExemptTotal : Edm.Decimal [required] "VAT Exempt Total"
PX.Objects.CA.CAExpense.VatExemptTotal : Edm.Decimal [required]
PX.Objects.CA.CAExpense.CuryVatTaxableTotal : Edm.Decimal [required] "VAT Taxable Total"
PX.Objects.CA.CAExpense.VatTaxableTotal : Edm.Decimal [required]
PX.Objects.CA.CAExpense.CuryTaxAmt : Edm.Decimal [required] "Tax Amount"
PX.Objects.CA.CAExpense.TaxAmt : Edm.Decimal [required]
PX.Objects.CA.CAExpense.CurySplitTotal : Edm.Decimal [required] "Detail Total"
PX.Objects.CA.CAExpense.SplitTotal : Edm.Decimal [required]
PX.Objects.CA.CAExpense.CuryControlAmt : Edm.Decimal [required] "Control Total"
PX.Objects.CA.CAExpense.ControlAmt : Edm.Decimal [required]
PX.Objects.CA.CAExpense.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CA.CAExpense.CuryTaxRoundDiff : Edm.Decimal [required] "Rounding Diff."
PX.Objects.CA.CAExpense.TaxRoundDiff : Edm.Decimal [required]
PX.Objects.CA.CAExpense.HasWithHoldTax : Edm.Boolean
PX.Objects.CA.CAExpense.HasUseTax : Edm.Boolean
PX.Objects.CA.CAExpense.PaymentsReclassification : Edm.Boolean
PX.Objects.CA.CAExpense.NoteID : Edm.Guid
PX.Objects.CA.CAExpense.NoteText : Edm.String "Note Text"
PX.Objects.CA.CAExpense.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CAExpense.CreatedByScreenID : Edm.String
PX.Objects.CA.CAExpense.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CAExpense.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CAExpense.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CAExpense.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CAExpense.tstamp : Edm.Binary
PX.Objects.CA.CAExpense.CATranByCashTranID -> PX.Objects.CA.CATran (CashTranID=TranID)
PX.Objects.CA.CAExpense.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CAExpense.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CAExpense.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CAExpense.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CAExpense.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.CA.CAExpense.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.CA.CAExpense.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CAExpense.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CAExpense.AccountByCuryID -> PX.Objects.GL.Account (CuryID=CuryID)
PX.Objects.CA.CAExpense.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CA.CAExpense.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.CA.CAExpense.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CAExpense.CATransferByRefNbr -> PX.Objects.CA.CATransfer (RefNbr=TransferNbr)
PX.Objects.CA.CAExpense.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CA.CAExpense.CAExpenseTaxCollection -> Collection(PX.Objects.CA.CAExpenseTax)

# PX.Objects.CA.CAExpenseTax (EntityType)

Label: "CAExpenseTax"
Key: LineNbr, RefNbr, TaxID, TranType
Entity sets: PX_Objects_CA_CAExpenseTax, CAExpenseTax
Non-filterable, non-selectable: NonDeductibleTaxRate

PX.Objects.CA.CAExpenseTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.CA.CAExpenseTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.CA.CAExpenseTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CAExpenseTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CAExpenseTax.CreatedByScreenID : Edm.String
PX.Objects.CA.CAExpenseTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CAExpenseTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CAExpenseTax.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CAExpenseTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CAExpenseTax.TranType : Edm.String [key required] "Tran. Type"
PX.Objects.CA.CAExpenseTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CA.CAExpenseTax.RefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CAExpenseTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.CA.CAExpenseTax.CuryInfoID : Edm.Int64
PX.Objects.CA.CAExpenseTax.CuryOrigTaxableAmt : Edm.Decimal
PX.Objects.CA.CAExpenseTax.OrigTaxableAmt : Edm.Decimal
PX.Objects.CA.CAExpenseTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CAExpenseTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CAExpenseTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CAExpenseTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CAExpenseTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CAExpenseTax.tstamp : Edm.Binary
PX.Objects.CA.CAExpenseTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CAExpenseTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CAExpenseTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.CA.CAExpenseTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.CA.CAExpenseTax.CAExpenseByLineNbr -> PX.Objects.CA.CAExpense (RefNbr=RefNbr, LineNbr=LineNbr)

# PX.Objects.CA.CAExpenseTaxTran (EntityType)

Label: "CAExpenseTaxTran"
BaseType: PX.Objects.TX.TaxTran
Key: Module, RecordID (inherited from PX.Objects.TX.TaxTran)
Entity sets: PX_Objects_CA_CAExpenseTaxTran, CAExpenseTaxTran

# PX.Objects.CA.CARecon (EntityType)

Label: "Reconciliation Statement"
Key: CashAccountID, ReconNbr
Entity sets: PX_Objects_CA_CARecon, ReconciliationStatement, CARecon
Non-filterable, non-selectable: LoadDocumentsTill, IsUserLoadDocumentsTill, CuryReconciledTurnover, ReconciledTurnover, WorkgroupID, OwnerID, NoteText, CuryRate, CuryViewState, DeletedDatabaseRecord

PX.Objects.CA.CARecon.CashAccountID : Edm.Int32 [key] "Cash Account"
PX.Objects.CA.CARecon.ReconNbr : Edm.String [key] "Ref. Number"
PX.Objects.CA.CARecon.ReconDate : Edm.DateTimeOffset "Reconciliation Date"
PX.Objects.CA.CARecon.LastReconDate : Edm.DateTimeOffset "Last Reconciliation Date"
PX.Objects.CA.CARecon.LoadDocumentsTill : Edm.DateTimeOffset "Load Documents Up To"
PX.Objects.CA.CARecon.IsUserLoadDocumentsTill : Edm.Boolean
PX.Objects.CA.CARecon.Reconciled : Edm.Boolean [required] "Reconciled"
PX.Objects.CA.CARecon.Voided : Edm.Boolean [required] "Voided"
PX.Objects.CA.CARecon.Hold : Edm.Boolean "Hold"
PX.Objects.CA.CARecon.CuryBegBalance : Edm.Decimal [required] "Beginning Balance"
PX.Objects.CA.CARecon.CuryBalance : Edm.Decimal [required] "Statement Balance"
PX.Objects.CA.CARecon.CuryReconciledDebits : Edm.Decimal "Reconciled Receipts"
PX.Objects.CA.CARecon.ReconciledDebits : Edm.Decimal "Reconciled Receipts"
PX.Objects.CA.CARecon.CuryReconciledCredits : Edm.Decimal "Reconciled Disb."
PX.Objects.CA.CARecon.ReconciledCredits : Edm.Decimal "Reconciled Disb."
PX.Objects.CA.CARecon.CuryReconciledBalance : Edm.Decimal "Reconciled Balance"
PX.Objects.CA.CARecon.CuryReconciledTurnover : Edm.Decimal "Reconciled Turnover"
PX.Objects.CA.CARecon.ReconciledTurnover : Edm.Decimal "Reconciled Turnover"
PX.Objects.CA.CARecon.CuryDiffBalance : Edm.Decimal "Difference"
PX.Objects.CA.CARecon.CuryID : Edm.String "Currency"
PX.Objects.CA.CARecon.CuryInfoID : Edm.Int64
PX.Objects.CA.CARecon.Status : Edm.String "Status"
PX.Objects.CA.CARecon.CountDebit : Edm.Int32 [required] "Receipt Count"
PX.Objects.CA.CARecon.CountCredit : Edm.Int32 [required] "Disbursement Count"
PX.Objects.CA.CARecon.SkipVoided : Edm.Boolean "Voided Transactions Are Skipped"
PX.Objects.CA.CARecon.ShowBatchPayments : Edm.Boolean "Bank Transactions Are Matched to Batch Payments"
PX.Objects.CA.CARecon.Approved : Edm.Boolean [required]
PX.Objects.CA.CARecon.Rejected : Edm.Boolean [required]
PX.Objects.CA.CARecon.ExcludeFromApproval : Edm.Boolean
PX.Objects.CA.CARecon.EmployeeID : Edm.Int32 "Owner"
PX.Objects.CA.CARecon.WorkgroupID : Edm.Int32 "Approval Workgroup ID"
PX.Objects.CA.CARecon.OwnerID : Edm.Int32 "Approver"
PX.Objects.CA.CARecon.tstamp : Edm.Binary
PX.Objects.CA.CARecon.NoteID : Edm.Guid
PX.Objects.CA.CARecon.NoteText : Edm.String "Note Text"
PX.Objects.CA.CARecon.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CARecon.CreatedByScreenID : Edm.String
PX.Objects.CA.CARecon.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CARecon.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CARecon.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CARecon.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CARecon.CuryRate : Edm.Decimal
PX.Objects.CA.CARecon.CuryViewState : Edm.Boolean
PX.Objects.CA.CARecon.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.CARecon.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.CA.CARecon.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CARecon.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CARecon.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CARecon.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CARecon.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.CARecon.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CA.CARecon.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.CA.CARecon.CASummaryOnReconDateCollection -> Collection(PX.Objects.CA.CASummaryOnReconDate)

# PX.Objects.CA.CAReconByPeriod (EntityType)

Label: "Reconciliation by Period"
Key: CashAccountID, FinPeriodID
Entity sets: PX_Objects_CA_CAReconByPeriod, ReconciliationbyPeriod, CAReconByPeriod

PX.Objects.CA.CAReconByPeriod.CashAccountID : Edm.Int32 [key] "Cash Account"
PX.Objects.CA.CAReconByPeriod.LastReconDate : Edm.DateTimeOffset "Last Reconciliation Date"
PX.Objects.CA.CAReconByPeriod.FinPeriodID : Edm.String [key]
PX.Objects.CA.CAReconByPeriod.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)

# PX.Objects.CA.CASetup (EntityType)

Label: "Cash Management Preferences"
Singletons: PX_Objects_CA_CASetup, CashManagementPreferences, CASetup

PX.Objects.CA.CASetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.CA.CASetup.RegisterNumberingID : Edm.String "Transaction Numbering Sequence"
PX.Objects.CA.CASetup.TransferNumberingID : Edm.String "Transfer Numbering Sequence"
PX.Objects.CA.CASetup.CABatchNumberingID : Edm.String "Payment Batch Numbering Sequence"
PX.Objects.CA.CASetup.CAStatementNumberingID : Edm.String "Bank Statement Numbering Sequence"
PX.Objects.CA.CASetup.CorpCardNumberingID : Edm.String "Corporate Card Numbering Sequence"
PX.Objects.CA.CASetup.RequireControlTotal : Edm.Boolean [required] "Validate Control Totals on Entry"
PX.Objects.CA.CASetup.RequireControlTaxTotal : Edm.Boolean [required] "Validate Tax Totals on Entry"
PX.Objects.CA.CASetup.HoldEntry : Edm.Boolean [required] "Hold Transactions on Entry"
PX.Objects.CA.CASetup.ReleaseAP : Edm.Boolean [required] "Release AP Documents from CA Module"
PX.Objects.CA.CASetup.ReleaseAR : Edm.Boolean [required] "Release AR Documents from CA Module"
PX.Objects.CA.CASetup.CalcBalDebitUnclearedUnreleased : Edm.Boolean [required] "Unreleased Uncleared"
PX.Objects.CA.CASetup.CalcBalDebitClearedUnreleased : Edm.Boolean [required] "Unreleased Cleared"
PX.Objects.CA.CASetup.CalcBalDebitUnclearedReleased : Edm.Boolean [required] "Released Uncleared"
PX.Objects.CA.CASetup.CalcBalCreditUnclearedUnreleased : Edm.Boolean [required] "Unreleased Uncleared"
PX.Objects.CA.CASetup.CalcBalCreditClearedUnreleased : Edm.Boolean [required] "Unreleased Cleared"
PX.Objects.CA.CASetup.CalcBalCreditUnclearedReleased : Edm.Boolean [required] "Released Uncleared"
PX.Objects.CA.CASetup.AutoPostOption : Edm.Boolean [required] "Automatically Post to GL on Release"
PX.Objects.CA.CASetup.DateRangeDefault : Edm.String "Default Date Range"
PX.Objects.CA.CASetup.ReceiptTranDaysBefore : Edm.Int32 "Days Before Bank Transaction Date"
PX.Objects.CA.CASetup.ReceiptTranDaysAfter : Edm.Int32 "Days After Bank Transaction Date"
PX.Objects.CA.CASetup.DisbursementTranDaysBefore : Edm.Int32 "Days Before Bank Transaction Date"
PX.Objects.CA.CASetup.DisbursementTranDaysAfter : Edm.Int32 "Days After Bank Transaction Date"
PX.Objects.CA.CASetup.AllowMatchingCreditMemo : Edm.Boolean [required] "Allow Matching to Credit Memo"
PX.Objects.CA.CASetup.AllowMatchingDebitAdjustment : Edm.Boolean [required] "Allow Matching to Debit Adjustment"
PX.Objects.CA.CASetup.RefNbrCompareWeight : Edm.Decimal "Ref. Nbr. Weight"
PX.Objects.CA.CASetup.DateCompareWeight : Edm.Decimal "Doc. Date Weight"
PX.Objects.CA.CASetup.PayeeCompareWeight : Edm.Decimal "Doc. Payee Weight"
PX.Objects.CA.CASetup.DateMeanOffset : Edm.Decimal "Payment Clearing Average Delay"
PX.Objects.CA.CASetup.DateSigma : Edm.Decimal "Estimated Deviation (Days)"
PX.Objects.CA.CASetup.CuryDiffThreshold : Edm.Decimal "Amount Difference Threshold (%)"
PX.Objects.CA.CASetup.AmountWeight : Edm.Decimal "Amount Weight"
PX.Objects.CA.CASetup.EmptyRefNbrMatching : Edm.Boolean [required] "Consider Empty Ref. Nbr. as Matching"
PX.Objects.CA.CASetup.IgnoreCuryCheckOnImport : Edm.Boolean [required] "Ignore Currency Check on Bank Statement Import"
PX.Objects.CA.CASetup.ImportToSingleAccount : Edm.Boolean [required] "Import Bank Statement to Single Cash Account"
PX.Objects.CA.CASetup.AllowEmptyFITID : Edm.Boolean [required] "Allow Empty FITID"
PX.Objects.CA.CASetup.AllowMatchingToUnreleasedBatch : Edm.Boolean [required] "Allow Matching to Unreleased Batch Payments"
PX.Objects.CA.CASetup.UnknownPaymentEntryTypeID : Edm.String "Unrecognized Receipts Type"
PX.Objects.CA.CASetup.StatementImportTypeName : Edm.String "Statement Import Service"
PX.Objects.CA.CASetup.SkipVoided : Edm.Boolean [required] "Skip Voided Transactions"
PX.Objects.CA.CASetup.SkipReconciled : Edm.Boolean [required] "Skip Reconciled Transactions in Matching"
PX.Objects.CA.CASetup.RequireExtRefNbr : Edm.Boolean [required] "Require Document Ref. Nbr. on Entry"
PX.Objects.CA.CASetup.ValidateDataConsistencyOnRelease : Edm.Boolean [required] "Validate data consistency on Release"
PX.Objects.CA.CASetup.MatchThreshold : Edm.Decimal "Absolute Relevance Threshold"
PX.Objects.CA.CASetup.RelativeMatchThreshold : Edm.Decimal "Relative Relevance Threshold"
PX.Objects.CA.CASetup.InvoiceFilterByDate : Edm.Boolean "Match by Discount and Due Date"
PX.Objects.CA.CASetup.DaysBeforeInvoiceDiscountDate : Edm.Int32 "Days Before Discount Date"
PX.Objects.CA.CASetup.DaysBeforeInvoiceDueDate : Edm.Int32 "Days Before Due Date"
PX.Objects.CA.CASetup.DaysAfterInvoiceDueDate : Edm.Int32 "Days After Due Date"
PX.Objects.CA.CASetup.InvoiceFilterByCashAccount : Edm.Boolean "Match by Cash Account"
PX.Objects.CA.CASetup.InvoiceRefNbrCompareWeight : Edm.Decimal "Ref. Nbr. Weight"
PX.Objects.CA.CASetup.InvoiceDateCompareWeight : Edm.Decimal "Doc. Date Weight"
PX.Objects.CA.CASetup.InvoicePayeeCompareWeight : Edm.Decimal "Doc. Payee Weight"
PX.Objects.CA.CASetup.AveragePaymentDelay : Edm.Decimal "Average Payment Delay"
PX.Objects.CA.CASetup.InvoiceDateSigma : Edm.Decimal "Estimated Deviation (Days)"
PX.Objects.CA.CASetup.tstamp : Edm.Binary
PX.Objects.CA.CASetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CASetup.CreatedByScreenID : Edm.String
PX.Objects.CA.CASetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CASetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CASetup.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CASetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CASetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CASetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CASetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.CA.CASetup.NumberingByRegisterNumberingID -> PX.Objects.CS.Numbering (RegisterNumberingID=NumberingID)
PX.Objects.CA.CASetup.NumberingByTransferNumberingID -> PX.Objects.CS.Numbering (TransferNumberingID=NumberingID)
PX.Objects.CA.CASetup.NumberingByCABatchNumberingID -> PX.Objects.CS.Numbering (CABatchNumberingID=NumberingID)
PX.Objects.CA.CASetup.NumberingByCAStatementNumberingID -> PX.Objects.CS.Numbering (CAStatementNumberingID=NumberingID)
PX.Objects.CA.CASetup.NumberingByCorpCardNumberingID -> PX.Objects.CS.Numbering (CorpCardNumberingID=NumberingID)
PX.Objects.CA.CASetup.AccountByTransitAcctId -> PX.Objects.GL.Account
PX.Objects.CA.CASetup.SubByTransitSubID -> PX.Objects.GL.Sub
PX.Objects.CA.CASetup.CAEntryTypeByUnknownPaymentEntryTypeID -> PX.Objects.CA.CAEntryType (UnknownPaymentEntryTypeID=EntryTypeId)

# PX.Objects.CA.CASetupApproval (EntityType)

Label: "CA Approval Preferences"
Key: ApprovalID
Entity sets: PX_Objects_CA_CASetupApproval, CAApprovalPreferences, CASetupApproval

PX.Objects.CA.CASetupApproval.ApprovalID : Edm.Int32 [key]
PX.Objects.CA.CASetupApproval.GraphType : Edm.String "Type"
PX.Objects.CA.CASetupApproval.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.CA.CASetupApproval.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.CA.CASetupApproval.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CA.CASetupApproval.tstamp : Edm.Binary
PX.Objects.CA.CASetupApproval.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CASetupApproval.CreatedByScreenID : Edm.String
PX.Objects.CA.CASetupApproval.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CASetupApproval.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CASetupApproval.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CASetupApproval.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CASetupApproval.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CASetupApproval.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CASetupApproval.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.CA.CASetupApproval.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)
PX.Objects.CA.CASetupApproval.EPAssignmentMapByGraphType -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID, GraphType=GraphType)

# PX.Objects.CA.CashAccount (EntityType)

Label: "Cash Account"
Key: CashAccountCD
Entity sets: PX_Objects_CA_CashAccount, CashAccount
Non-filterable, non-selectable: AllowOverrideCury, AllowOverrideRate, PTInstancesAllowed, AcctSettingsAllowed, RefNbrComparePercent, DateComparePercent, PayeeComparePercent, ExpenseReceiptRefNbrComparePercent, ExpenseReceiptDateComparePercent, ExpenseReceiptAmountComparePercent, RatioInRelevanceCalculationLabel, InvoiceRefNbrComparePercent, InvoiceDateComparePercent, InvoicePayeeComparePercent, NoteText

PX.Objects.CA.CashAccount.Active : Edm.Boolean [required] "Active"
PX.Objects.CA.CashAccount.CashAccountID : Edm.Int32 "CashAccountID"
PX.Objects.CA.CashAccount.CashAccountCD : Edm.String [key] "Cash Account"
PX.Objects.CA.CashAccount.Descr : Edm.String "Description"
PX.Objects.CA.CashAccount.CuryID : Edm.String "Currency"
PX.Objects.CA.CashAccount.CuryRateTypeID : Edm.String "Curr. Rate Type"
PX.Objects.CA.CashAccount.AllowOverrideCury : Edm.Boolean "Enable Currency Override"
PX.Objects.CA.CashAccount.AllowOverrideRate : Edm.Boolean "Enable Rate Override"
PX.Objects.CA.CashAccount.ExtRefNbr : Edm.String "External Ref. Number"
PX.Objects.CA.CashAccount.Reconcile : Edm.Boolean [required] "Requires Reconciliation"
PX.Objects.CA.CashAccount.ReferenceID : Edm.Int32 "Bank ID"
PX.Objects.CA.CashAccount.ReconNumberingID : Edm.String "Reconciliation Numbering Sequence"
PX.Objects.CA.CashAccount.ClearingAccount : Edm.Boolean [required] "Clearing Account"
PX.Objects.CA.CashAccount.Signature : Edm.String "Signature"
PX.Objects.CA.CashAccount.SignatureDescr : Edm.String "Name"
PX.Objects.CA.CashAccount.StatementImportTypeName : Edm.String "Statement Import Service"
PX.Objects.CA.CashAccount.RestrictVisibilityWithBranch : Edm.Boolean [required] "Restrict Visibility with Branch"
PX.Objects.CA.CashAccount.PTInstancesAllowed : Edm.Boolean "Cards Allowed"
PX.Objects.CA.CashAccount.AcctSettingsAllowed : Edm.Boolean "Account Settings Allowed"
PX.Objects.CA.CashAccount.MatchToBatch : Edm.Boolean [required] "Match Bank Transactions to Batch Payments"
PX.Objects.CA.CashAccount.UseForCorpCard : Edm.Boolean [required] "Use for Corporate Cards"
PX.Objects.CA.CashAccount.BaseCuryID : Edm.String
PX.Objects.CA.CashAccount.ReceiptTranDaysBefore : Edm.Int32 "Days Before Bank Transaction Date"
PX.Objects.CA.CashAccount.ReceiptTranDaysAfter : Edm.Int32 "Days After Bank Transaction Date"
PX.Objects.CA.CashAccount.DisbursementTranDaysBefore : Edm.Int32 "Days Before Bank Transaction Date"
PX.Objects.CA.CashAccount.DisbursementTranDaysAfter : Edm.Int32 "Days After Bank Transaction Date"
PX.Objects.CA.CashAccount.AllowMatchingCreditMemo : Edm.Boolean [required] "Allow Matching to Credit Memo"
PX.Objects.CA.CashAccount.AllowMatchingDebitAdjustment : Edm.Boolean [required] "Allow Matching to Debit Adjustment"
PX.Objects.CA.CashAccount.RefNbrCompareWeight : Edm.Decimal "Ref. Nbr. Weight"
PX.Objects.CA.CashAccount.DateCompareWeight : Edm.Decimal "Doc. Date Weight"
PX.Objects.CA.CashAccount.PayeeCompareWeight : Edm.Decimal "Doc. Payee Weight"
PX.Objects.CA.CashAccount.RefNbrComparePercent : Edm.Decimal "%"
PX.Objects.CA.CashAccount.EmptyRefNbrMatching : Edm.Boolean [required] "Consider Empty Ref. Nbr. as Matching"
PX.Objects.CA.CashAccount.DateComparePercent : Edm.Decimal "%"
PX.Objects.CA.CashAccount.PayeeComparePercent : Edm.Decimal "%"
PX.Objects.CA.CashAccount.DateMeanOffset : Edm.Decimal "Payment Clearing Average Delay"
PX.Objects.CA.CashAccount.DateSigma : Edm.Decimal "Estimated Deviation (Days)"
PX.Objects.CA.CashAccount.SkipVoided : Edm.Boolean [required] "Skip Voided Transactions During Matching"
PX.Objects.CA.CashAccount.CuryDiffThreshold : Edm.Decimal "Amount Difference Threshold (%)"
PX.Objects.CA.CashAccount.AmountWeight : Edm.Decimal "Amount Weight"
PX.Objects.CA.CashAccount.ExpenseReceiptRefNbrComparePercent : Edm.Decimal
PX.Objects.CA.CashAccount.ExpenseReceiptDateComparePercent : Edm.Decimal
PX.Objects.CA.CashAccount.ExpenseReceiptAmountComparePercent : Edm.Decimal
PX.Objects.CA.CashAccount.RatioInRelevanceCalculationLabel : Edm.String "RatioInRelevanceCalculationLabel"
PX.Objects.CA.CashAccount.MatchSettingsPerAccount : Edm.Boolean
PX.Objects.CA.CashAccount.MatchThreshold : Edm.Decimal "Absolute Relevance Threshold"
PX.Objects.CA.CashAccount.RelativeMatchThreshold : Edm.Decimal "Relative Relevance Threshold"
PX.Objects.CA.CashAccount.InvoiceFilterByDate : Edm.Boolean "Match by Discount and Due Date"
PX.Objects.CA.CashAccount.DaysBeforeInvoiceDiscountDate : Edm.Int32 "Days Before Discount Date"
PX.Objects.CA.CashAccount.DaysBeforeInvoiceDueDate : Edm.Int32 "Days Before Due Date"
PX.Objects.CA.CashAccount.DaysAfterInvoiceDueDate : Edm.Int32 "Days After Due Date"
PX.Objects.CA.CashAccount.InvoiceFilterByCashAccount : Edm.Boolean "Match by Cash Account"
PX.Objects.CA.CashAccount.InvoiceRefNbrCompareWeight : Edm.Decimal "Ref. Nbr. Weight"
PX.Objects.CA.CashAccount.InvoiceDateCompareWeight : Edm.Decimal "Doc. Date Weight"
PX.Objects.CA.CashAccount.InvoicePayeeCompareWeight : Edm.Decimal "Doc. Payee Weight"
PX.Objects.CA.CashAccount.InvoiceRefNbrComparePercent : Edm.Decimal "%"
PX.Objects.CA.CashAccount.InvoiceDateComparePercent : Edm.Decimal "%"
PX.Objects.CA.CashAccount.InvoicePayeeComparePercent : Edm.Decimal "%"
PX.Objects.CA.CashAccount.AveragePaymentDelay : Edm.Decimal "Average Payment Delay"
PX.Objects.CA.CashAccount.InvoiceDateSigma : Edm.Decimal "Estimated Deviation (Days)"
PX.Objects.CA.CashAccount.NoteID : Edm.Guid
PX.Objects.CA.CashAccount.NoteText : Edm.String "Note Text"
PX.Objects.CA.CashAccount.tstamp : Edm.Binary
PX.Objects.CA.CashAccount.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CashAccount.CreatedByScreenID : Edm.String
PX.Objects.CA.CashAccount.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CashAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CashAccount.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CashAccount.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CashAccount.VendorByReferenceID -> PX.Objects.AP.Vendor (ReferenceID=BAccountID)
PX.Objects.CA.CashAccount.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.CA.CashAccount.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CashAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CashAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CashAccount.NumberingByReconNumberingID -> PX.Objects.CS.Numbering (ReconNumberingID=NumberingID)
PX.Objects.CA.CashAccount.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CashAccount.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType (CuryRateTypeID=CuryRateTypeID)
PX.Objects.CA.CashAccount.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CashAccount.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CA.CashAccount.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.CA.CashAccount.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CA.CashAccount.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CA.CashAccount.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CA.CashAccount.VendorPaymentMethodCollection -> Collection(PX.Objects.AP.DAC.VendorPaymentMethod)
PX.Objects.CA.CashAccount.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CA.CashAccount.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CA.CashAccount.CABankTranRuleCollection -> Collection(PX.Objects.CA.CABankTranRule)
PX.Objects.CA.CashAccount.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.CA.CashAccount.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CA.CashAccount.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CA.CashAccount.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CA.CashAccount.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.CA.CashAccount.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CA.CashAccount.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CA.CashAccount.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.CA.CashAccount.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.CashAccount.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CA.CashAccount.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.CA.CashAccount.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CA.CashAccount.CABankFeedAccountMappingCollection -> Collection(PX.Objects.CA.CABankFeedAccountMapping)
PX.Objects.CA.CashAccount.CABankFeedCorpCardCollection -> Collection(PX.Objects.CA.CABankFeedCorpCard)
PX.Objects.CA.CashAccount.CABankFeedDetailCollection -> Collection(PX.Objects.CA.CABankFeedDetail)
PX.Objects.CA.CashAccount.CABankTranBAccountMappingCollection -> Collection(PX.Objects.CA.CABankTranBAccountMapping)
PX.Objects.CA.CashAccount.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.CA.CashAccount.CABankTranHeaderCollection -> Collection(PX.Objects.CA.CABankTranHeader)
PX.Objects.CA.CashAccount.CACorpCardCollection -> Collection(PX.Objects.CA.CACorpCard)
PX.Objects.CA.CashAccount.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.CA.CashAccount.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.CA.CashAccount.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CA.CashAccount.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.CA.CashAccount.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.CA.CashAccount.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.Objects.CA.CashAccount.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.CA.CashAccount.CashAccountETDetailCollection -> Collection(PX.Objects.CA.CashAccountETDetail)
PX.Objects.CA.CashAccount.CashForecastTranCollection -> Collection(PX.Objects.CA.CashForecastTran)
PX.Objects.CA.CashAccount.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.CA.CashAccount.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.CA.CashAccount.CCProcessingCenterCollection -> Collection(PX.Objects.CA.CCProcessingCenter)
PX.Objects.CA.CashAccount.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.CA.CashAccount.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.CA.CashAccount.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.CA.CashAccount.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.CA.CashAccount.PPBillcomFundingAccountCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomFundingAccount)
PX.Objects.CA.CashAccount.PPAvidFundingAccountCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidFundingAccount)
PX.Objects.CA.CashAccount.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CA.CashAccount.CCProcessingCenterBranchCollection -> Collection(PX.Objects.CC.CCProcessingCenterBranch)
PX.Objects.CA.CashAccount.PaymentMethodAccountCollection -> Collection(PX.Objects.CA.PaymentMethodAccount)
PX.Objects.CA.CashAccount.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.CA.CashAccount.CustomerPaymentMethodInfoCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodInfo)
PX.Objects.CA.CashAccount.BCPaymentMethodsCollection -> Collection(PX.Commerce.Objects.BCPaymentMethods)
PX.Objects.CA.CashAccount.CAReconByPeriodCollection -> Collection(PX.Objects.CA.CAReconByPeriod)
PX.Objects.CA.CashAccount.CashAccountDepositCollection -> Collection(PX.Objects.CA.CashAccountDeposit)
PX.Objects.CA.CashAccount.CashAccountPaymentMethodDetailCollection -> Collection(PX.Objects.CA.CashAccountPaymentMethodDetail)
PX.Objects.CA.CashAccount.CADailySummaryCollection -> Collection(PX.Objects.CA.CADailySummary)

# PX.Objects.CA.CashAccountCheck (EntityType)

Label: "Cash Account Check"
Key: CashAccountID, CheckNbr, PaymentMethodID
Entity sets: PX_Objects_CA_CashAccountCheck, CashAccountCheck

PX.Objects.CA.CashAccountCheck.CashAccountID : Edm.Int32 [key] "Cash Account ID"
PX.Objects.CA.CashAccountCheck.PaymentMethodID : Edm.String [key] "Payment Method"
PX.Objects.CA.CashAccountCheck.CashAccountCheckID : Edm.Int32
PX.Objects.CA.CashAccountCheck.CheckNbr : Edm.String [key] "Check Number"
PX.Objects.CA.CashAccountCheck.DocType : Edm.String "Document Type"
PX.Objects.CA.CashAccountCheck.RefNbr : Edm.String "Reference Nbr."
PX.Objects.CA.CashAccountCheck.FinPeriodID : Edm.String "Application Period"
PX.Objects.CA.CashAccountCheck.DocDate : Edm.DateTimeOffset "Document Date"
PX.Objects.CA.CashAccountCheck.VendorID : Edm.Int32 "Vendor"
PX.Objects.CA.CashAccountCheck.tstamp : Edm.Binary
PX.Objects.CA.CashAccountCheck.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CashAccountCheck.CreatedByScreenID : Edm.String
PX.Objects.CA.CashAccountCheck.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CashAccountCheck.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CashAccountCheck.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CashAccountCheck.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CashAccountCheck.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.CA.CashAccountCheck.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.CA.CashAccountCheck.APPaymentByRefNbr -> PX.Objects.AP.APPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.CA.CashAccountCheck.APPaymentByDocType -> PX.Objects.AP.APPayment (RefNbr=RefNbr, DocType=DocType)
PX.Objects.CA.CashAccountCheck.APAdjustByCashAccountID -> PX.Objects.AP.APAdjust (CheckNbr=StubNbr, PaymentMethodID=PaymentMethodID, CashAccountID=CashAccountID)
PX.Objects.CA.CashAccountCheck.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CashAccountCheck.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CashAccountCheck.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.CashAccountCheck.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)

# PX.Objects.CA.CashAccountDeposit (EntityType)

Label: "Clearing Account"
Key: CashAccountID, DepositAcctID, PaymentMethodID
Entity sets: PX_Objects_CA_CashAccountDeposit, ClearingAccount, CashAccountDeposit

PX.Objects.CA.CashAccountDeposit.CashAccountID : Edm.Int32 [key] "Cash Account ID"
PX.Objects.CA.CashAccountDeposit.DepositAcctID : Edm.Int32 [key] "Clearing Account"
PX.Objects.CA.CashAccountDeposit.PaymentMethodID : Edm.String [key required] "Payment Method"
PX.Objects.CA.CashAccountDeposit.ChargeEntryTypeID : Edm.String "Charge Type"
PX.Objects.CA.CashAccountDeposit.ChargeRate : Edm.Decimal "Charge Rate, %"
PX.Objects.CA.CashAccountDeposit.CAEntryTypeByChargeEntryTypeID -> PX.Objects.CA.CAEntryType (ChargeEntryTypeID=EntryTypeId)
PX.Objects.CA.CashAccountDeposit.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.CashAccountDeposit.CashAccountByDepositAcctID -> PX.Objects.CA.CashAccount (DepositAcctID=CashAccountID)
PX.Objects.CA.CashAccountDeposit.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)

# PX.Objects.CA.CashAccountETDetail (EntityType)

Label: "Entry Type for Cash Account"
Key: CashAccountID, EntryTypeID
Entity sets: PX_Objects_CA_CashAccountETDetail, EntryTypeforCashAccount, CashAccountETDetail

PX.Objects.CA.CashAccountETDetail.CashAccountID : Edm.Int32 [key] "AccountID"
PX.Objects.CA.CashAccountETDetail.EntryTypeID : Edm.String [key] "Entry Type ID"
PX.Objects.CA.CashAccountETDetail.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.CA.CashAccountETDetail.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CA.CashAccountETDetail.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.CA.CashAccountETDetail.tstamp : Edm.Binary
PX.Objects.CA.CashAccountETDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CashAccountETDetail.CreatedByScreenID : Edm.String
PX.Objects.CA.CashAccountETDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CashAccountETDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CashAccountETDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CashAccountETDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CashAccountETDetail.BranchByOffsetBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CashAccountETDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CashAccountETDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CashAccountETDetail.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.CA.CashAccountETDetail.AccountByOffsetAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CashAccountETDetail.SubByOffsetSubID -> PX.Objects.GL.Sub
PX.Objects.CA.CashAccountETDetail.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.CA.CashAccountETDetail.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.CashAccountETDetail.CashAccountByOffsetCashAccountID -> PX.Objects.CA.CashAccount

# PX.Objects.CA.CashAccountPaymentMethodDetail (EntityType)

Label: "Remittance Settings"
Key: CashAccountID, DetailID, PaymentMethodID
Entity sets: PX_Objects_CA_CashAccountPaymentMethodDetail, RemittanceSettings, CashAccountPaymentMethodDetail

PX.Objects.CA.CashAccountPaymentMethodDetail.CashAccountID : Edm.Int32 [key] "Cash Account"
PX.Objects.CA.CashAccountPaymentMethodDetail.AccountID : Edm.Int32
PX.Objects.CA.CashAccountPaymentMethodDetail.PaymentMethodID : Edm.String [key] "Payment Method"
PX.Objects.CA.CashAccountPaymentMethodDetail.DetailID : Edm.String [key] "ID"
PX.Objects.CA.CashAccountPaymentMethodDetail.DetailValue : Edm.String "Value"
PX.Objects.CA.CashAccountPaymentMethodDetail.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.CashAccountPaymentMethodDetail.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CashAccountPaymentMethodDetail.PaymentMethodDetailByDetailID -> PX.Objects.CA.PaymentMethodDetail (PaymentMethodID=PaymentMethodID, DetailID=DetailID)
PX.Objects.CA.CashAccountPaymentMethodDetail.PaymentMethodDetailByPaymentMethodID -> PX.Objects.CA.PaymentMethodDetail (DetailID=DetailID, PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CashAccountPaymentMethodDetail.PaymentMethodAccountByCashAccountID -> PX.Objects.CA.PaymentMethodAccount (PaymentMethodID=PaymentMethodID, CashAccountID=CashAccountID)
PX.Objects.CA.CashAccountPaymentMethodDetail.PaymentMethodAccountByPaymentMethodID -> PX.Objects.CA.PaymentMethodAccount (CashAccountID=CashAccountID, PaymentMethodID=PaymentMethodID)

# PX.Objects.CA.CashForecastTran (EntityType)

Label: "Cash Transactions"
Key: TranID
Entity sets: PX_Objects_CA_CashForecastTran, CashTransactions1, CashForecastTran
Non-filterable, non-selectable: NoteText

PX.Objects.CA.CashForecastTran.TranID : Edm.Int32 [key] "Document Number"
PX.Objects.CA.CashForecastTran.TranDate : Edm.DateTimeOffset "Tran. Date"
PX.Objects.CA.CashForecastTran.DrCr : Edm.String "Disb. / Receipt"
PX.Objects.CA.CashForecastTran.TranDesc : Edm.String "Description"
PX.Objects.CA.CashForecastTran.CuryID : Edm.String "Currency"
PX.Objects.CA.CashForecastTran.CuryTranAmt : Edm.Decimal [required] "Amount"
PX.Objects.CA.CashForecastTran.TranAmt : Edm.Decimal [required] "Tran. Amount"
PX.Objects.CA.CashForecastTran.NoteID : Edm.Guid
PX.Objects.CA.CashForecastTran.NoteText : Edm.String "Note Text"
PX.Objects.CA.CashForecastTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CashForecastTran.CreatedByScreenID : Edm.String
PX.Objects.CA.CashForecastTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CashForecastTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CashForecastTran.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CashForecastTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CashForecastTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CashForecastTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CashForecastTran.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CashForecastTran.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount

# PX.Objects.CA.CASplit (EntityType)

Label: "CA Transaction Details"
Key: AdjRefNbr, AdjTranType, LineNbr
Entity sets: PX_Objects_CA_CASplit, CATransactionDetails, CASplit
Non-filterable, non-selectable: ReclassificationProhibited, NoteText

PX.Objects.CA.CASplit.BranchID : Edm.Int32 "Branch"
PX.Objects.CA.CASplit.AdjRefNbr : Edm.String [key] "AdjRefNbr"
PX.Objects.CA.CASplit.AdjTranType : Edm.String [key] "Type"
PX.Objects.CA.CASplit.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CA.CASplit.InventoryID : Edm.Int32 "Item ID"
PX.Objects.CA.CASplit.UOM : Edm.String "UOM"
PX.Objects.CA.CASplit.Qty : Edm.Decimal "Quantity"
PX.Objects.CA.CASplit.UnitPrice : Edm.Decimal
PX.Objects.CA.CASplit.CuryUnitPrice : Edm.Decimal "Price"
PX.Objects.CA.CASplit.ReclassificationProhibited : Edm.Boolean
PX.Objects.CA.CASplit.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.CA.CASplit.TranDesc : Edm.String "Description"
PX.Objects.CA.CASplit.CuryInfoID : Edm.Int64
PX.Objects.CA.CASplit.CuryTranAmt : Edm.Decimal [required] "Amount"
PX.Objects.CA.CASplit.TranAmt : Edm.Decimal [required] "Tran. Amount"
PX.Objects.CA.CASplit.CuryTaxableAmt : Edm.Decimal
PX.Objects.CA.CASplit.TaxableAmt : Edm.Decimal
PX.Objects.CA.CASplit.CuryTaxAmt : Edm.Decimal
PX.Objects.CA.CASplit.TaxAmt : Edm.Decimal
PX.Objects.CA.CASplit.FinPeriodID : Edm.String
PX.Objects.CA.CASplit.TranPeriodID : Edm.String
PX.Objects.CA.CASplit.NoteID : Edm.Guid
PX.Objects.CA.CASplit.NoteText : Edm.String "Note Text"
PX.Objects.CA.CASplit.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CASplit.CreatedByScreenID : Edm.String
PX.Objects.CA.CASplit.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CASplit.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CASplit.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CASplit.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CASplit.tstamp : Edm.Binary
PX.Objects.CA.CASplit.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.CA.CASplit.PMTaskByTaskID -> PX.Objects.PM.PMTask
PX.Objects.CA.CASplit.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.CA.CASplit.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.CA.CASplit.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CA.CASplit.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CASplit.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CASplit.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CASplit.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.CA.CASplit.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode
PX.Objects.CA.CASplit.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.CA.CASplit.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CA.CASplit.AccountBySubID -> PX.Objects.GL.Account
PX.Objects.CA.CASplit.SubBySubID -> PX.Objects.GL.Sub
PX.Objects.CA.CASplit.CAAdjByAdjRefNbr -> PX.Objects.CA.CAAdj (AdjTranType=AdjTranType, AdjRefNbr=AdjRefNbr)
PX.Objects.CA.CASplit.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CASplit.CATaxCollection -> Collection(PX.Objects.CA.CATax)

# PX.Objects.CA.CASummaryOnReconDate (EntityType)

Label: "Aggregated CA Daily Summary until Reconciliation Date"
Key: CashAccountID, ReconNbr
Entity sets: PX_Objects_CA_CASummaryOnReconDate, AggregatedCADailySummaryuntilReconciliationDate, CASummaryOnReconDate

PX.Objects.CA.CASummaryOnReconDate.CashAccountID : Edm.Int32 [key] "Cash Account"
PX.Objects.CA.CASummaryOnReconDate.ReconNbr : Edm.String [key]
PX.Objects.CA.CASummaryOnReconDate.ReconDate : Edm.DateTimeOffset "Reconciliation Date"
PX.Objects.CA.CASummaryOnReconDate.AmtReleasedClearedDr : Edm.Decimal
PX.Objects.CA.CASummaryOnReconDate.AmtReleasedClearedCr : Edm.Decimal
PX.Objects.CA.CASummaryOnReconDate.AmtReleasedUnclearedDr : Edm.Decimal
PX.Objects.CA.CASummaryOnReconDate.AmtReleasedUnclearedCr : Edm.Decimal
PX.Objects.CA.CASummaryOnReconDate.CAReconByReconNbr -> PX.Objects.CA.CARecon (ReconNbr=ReconNbr)
PX.Objects.CA.CASummaryOnReconDate.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CA.CASummaryOnReconDate.CASummaryOnReconDateCollection -> Collection(PX.Objects.CA.CASummaryOnReconDate)

# PX.Objects.CA.CATax (EntityType)

Label: "CA Tax Detail"
Key: AdjRefNbr, AdjTranType, LineNbr, TaxID
Entity sets: PX_Objects_CA_CATax, CATaxDetail, CATax
Non-filterable, non-selectable: NonDeductibleTaxRate

PX.Objects.CA.CATax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.CA.CATax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.CA.CATax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CATax.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CATax.CreatedByScreenID : Edm.String
PX.Objects.CA.CATax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CATax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CATax.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CATax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CATax.AdjTranType : Edm.String [key] "Tran. Type"
PX.Objects.CA.CATax.AdjRefNbr : Edm.String [key] "Reference Nbr."
PX.Objects.CA.CATax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CA.CATax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.CA.CATax.CuryInfoID : Edm.Int64
PX.Objects.CA.CATax.CuryOrigTaxableAmt : Edm.Decimal
PX.Objects.CA.CATax.OrigTaxableAmt : Edm.Decimal
PX.Objects.CA.CATax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CATax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CA.CATax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CATax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CA.CATax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CA.CATax.tstamp : Edm.Binary
PX.Objects.CA.CATax.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CATax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CATax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CATax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.CA.CATax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.CA.CATax.CASplitByLineNbr -> PX.Objects.CA.CASplit (AdjTranType=AdjTranType, AdjRefNbr=AdjRefNbr, LineNbr=LineNbr)

# PX.Objects.CA.CATaxTran (EntityType)

Label: "CA Tax Transaction"
BaseType: PX.Objects.TX.TaxTran
Key: Module, RecordID (inherited from PX.Objects.TX.TaxTran)
Entity sets: PX_Objects_CA_CATaxTran, CATaxTransaction, CATaxTran

# PX.Objects.CA.CATran (EntityType)

Label: "CA Transaction"
Key: TranID
Entity sets: PX_Objects_CA_CATran, CATransaction, CATran
Non-filterable, non-selectable: BegBal, EndBal, DayDesc, ReferenceName, Status, CuryDebitAmt, CuryCreditAmt, CuryClearedDebitAmt, CuryClearedCreditAmt, NoteText

PX.Objects.CA.CATran.BegBal : Edm.Decimal "BegBal"
PX.Objects.CA.CATran.EndBal : Edm.Decimal "Ending Balance"
PX.Objects.CA.CATran.DayDesc : Edm.String "Day of Week"
PX.Objects.CA.CATran.OrigModule : Edm.String "Module"
PX.Objects.CA.CATran.OrigTranType : Edm.String "Orig. Doc. Type"
PX.Objects.CA.CATran.OrigTranTypeUI : Edm.String "Tran. Type"
PX.Objects.CA.CATran.OrigRefNbr : Edm.String "Orig. Doc. Number"
PX.Objects.CA.CATran.IsPaymentChargeTran : Edm.Boolean [required]
PX.Objects.CA.CATran.OrigLineNbr : Edm.Int32
PX.Objects.CA.CATran.ExtRefNbr : Edm.String "Document Ref."
PX.Objects.CA.CATran.BranchID : Edm.Int32
PX.Objects.CA.CATran.TranID : Edm.Int64 [key] "Document Number"
PX.Objects.CA.CATran.TranDate : Edm.DateTimeOffset "Doc. Date"
PX.Objects.CA.CATran.DrCr : Edm.String "Disb. / Receipt"
PX.Objects.CA.CATran.ReferenceID : Edm.Int32 "Business Account"
PX.Objects.CA.CATran.ReferenceName : Edm.String "Business Name"
PX.Objects.CA.CATran.TranDesc : Edm.String "Description"
PX.Objects.CA.CATran.TranPeriodID : Edm.String
PX.Objects.CA.CATran.FinPeriodID : Edm.String "Post Period"
PX.Objects.CA.CATran.CuryInfoID : Edm.Int64
PX.Objects.CA.CATran.Hold : Edm.Boolean
PX.Objects.CA.CATran.PendingApproval : Edm.Boolean [required]
PX.Objects.CA.CATran.RequirePrint : Edm.Boolean [required]
PX.Objects.CA.CATran.Printed : Edm.Boolean [required]
PX.Objects.CA.CATran.Released : Edm.Boolean [required]
PX.Objects.CA.CATran.Voided : Edm.Boolean [required]
PX.Objects.CA.CATran.Posted : Edm.Boolean
PX.Objects.CA.CATran.Status : Edm.String "Status"
PX.Objects.CA.CATran.Reconciled : Edm.Boolean [required] "Reconciled"
PX.Objects.CA.CATran.ReconDate : Edm.DateTimeOffset
PX.Objects.CA.CATran.ReconNbr : Edm.String "Reconciled Number"
PX.Objects.CA.CATran.CuryTranAmt : Edm.Decimal [required] "Amount"
PX.Objects.CA.CATran.TranAmt : Edm.Decimal [required] "Tran. Amount"
PX.Objects.CA.CATran.BatchNbr : Edm.String "Batch Number"
PX.Objects.CA.CATran.CuryID : Edm.String "Currency"
PX.Objects.CA.CATran.Cleared : Edm.Boolean "Cleared"
PX.Objects.CA.CATran.ClearDate : Edm.DateTimeOffset "Clear Date"
PX.Objects.CA.CATran.CuryDebitAmt : Edm.Decimal "Receipt"
PX.Objects.CA.CATran.CuryCreditAmt : Edm.Decimal "Disbursement"
PX.Objects.CA.CATran.CuryClearedDebitAmt : Edm.Decimal "Receipt"
PX.Objects.CA.CATran.CuryClearedCreditAmt : Edm.Decimal "Disbursement"
PX.Objects.CA.CATran.NoteID : Edm.Guid
PX.Objects.CA.CATran.NoteText : Edm.String "Note Text"
PX.Objects.CA.CATran.RefTranID : Edm.Int64
PX.Objects.CA.CATran.RefSplitLineNbr : Edm.Int32
PX.Objects.CA.CATran.VoidedTranID : Edm.Int64
PX.Objects.CA.CATran.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CATran.CreatedByScreenID : Edm.String
PX.Objects.CA.CATran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CATran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CATran.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CATran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CATran.tstamp : Edm.Binary
PX.Objects.CA.CATran.BAccountByReferenceID -> PX.Objects.CR.BAccount (ReferenceID=BAccountID)
PX.Objects.CA.CATran.BatchByBatchNbr -> PX.Objects.GL.Batch (OrigModule=Module, BatchNbr=BatchNbr)
PX.Objects.CA.CATran.ARPaymentByOrigRefNbr -> PX.Objects.AR.ARPayment (OrigTranType=DocType, OrigRefNbr=RefNbr)
PX.Objects.CA.CATran.APPaymentByOrigRefNbr -> PX.Objects.AP.APPayment (OrigTranType=DocType, OrigRefNbr=RefNbr)
PX.Objects.CA.CATran.CATranByTranID -> PX.Objects.CA.CATran (TranID=RefTranID)
PX.Objects.CA.CATran.CATranByVoidedTranID -> PX.Objects.CA.CATran (VoidedTranID=TranID)
PX.Objects.CA.CATran.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CA.CATran.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.CATran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CATran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CATran.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CATran.CAAdjByOrigRefNbr -> PX.Objects.CA.CAAdj (OrigTranType=AdjTranType, OrigRefNbr=AdjRefNbr)
PX.Objects.CA.CATran.CADepositByOrigRefNbr -> PX.Objects.CA.CADeposit (OrigTranType=TranType, OrigRefNbr=RefNbr)
PX.Objects.CA.CATran.CAReconByReconNbr -> PX.Objects.CA.CARecon (ReconNbr=ReconNbr)
PX.Objects.CA.CATran.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CATran.CashAccountByRefTranAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CATran.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CA.CATran.PRDirectDepositSplitCollection -> Collection(PX.Objects.PR.PRDirectDepositSplit)
PX.Objects.CA.CATran.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.CA.CATran.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.CA.CATran.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CA.CATran.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CA.CATran.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.CA.CATran.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CA.CATran.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.CA.CATran.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.CA.CATran.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.CA.CATran.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)

# PX.Objects.CA.CATransfer (EntityType)

Label: "Transfer"
Key: TransferNbr
Entity sets: PX_Objects_CA_CATransfer, Transfer, CATransfer
Non-filterable, non-selectable: ReverseCount, NoteText, CashBalanceIn, CashBalanceOut, InGLBalance, OutGLBalance, BaseCuryID, TotalExpenses, CuryRate, OutCuryRate, DeletedDatabaseRecord

PX.Objects.CA.CATransfer.TransferNbr : Edm.String [key] "Transfer Number"
PX.Objects.CA.CATransfer.Descr : Edm.String "Description"
PX.Objects.CA.CATransfer.OutCuryInfoID : Edm.Int64
PX.Objects.CA.CATransfer.InCuryInfoID : Edm.Int64
PX.Objects.CA.CATransfer.InCuryID : Edm.String "Destination Currency"
PX.Objects.CA.CATransfer.OutCuryID : Edm.String "Source Currency"
PX.Objects.CA.CATransfer.CuryTranOut : Edm.Decimal [required] "Source Amount"
PX.Objects.CA.CATransfer.CuryTranIn : Edm.Decimal [required] "Destination Amount"
PX.Objects.CA.CATransfer.TranOut : Edm.Decimal [required] "Base Currency Amount"
PX.Objects.CA.CATransfer.TranIn : Edm.Decimal [required] "Base Currency Amount"
PX.Objects.CA.CATransfer.InDate : Edm.DateTimeOffset "Receipt Date"
PX.Objects.CA.CATransfer.OutDate : Edm.DateTimeOffset "Transfer Date"
PX.Objects.CA.CATransfer.InTranPeriodID : Edm.String
PX.Objects.CA.CATransfer.InPeriodID : Edm.String "In Period"
PX.Objects.CA.CATransfer.OutTranPeriodID : Edm.String
PX.Objects.CA.CATransfer.OutPeriodID : Edm.String "Out Period"
PX.Objects.CA.CATransfer.OutExtRefNbr : Edm.String "Document Ref."
PX.Objects.CA.CATransfer.InExtRefNbr : Edm.String "Document Ref."
PX.Objects.CA.CATransfer.TranIDOut : Edm.Int64
PX.Objects.CA.CATransfer.TranIDIn : Edm.Int64
PX.Objects.CA.CATransfer.ExpenseCntr : Edm.Int32 [required]
PX.Objects.CA.CATransfer.RGOLAmt : Edm.Decimal [required] "RGOL"
PX.Objects.CA.CATransfer.Hold : Edm.Boolean "Hold"
PX.Objects.CA.CATransfer.Released : Edm.Boolean [required]
PX.Objects.CA.CATransfer.OrigTransferNbr : Edm.String "Orig. Tran. Nbr."
PX.Objects.CA.CATransfer.ReverseCount : Edm.Int32 "Reversing Transactions"
PX.Objects.CA.CATransfer.NoteID : Edm.Guid
PX.Objects.CA.CATransfer.NoteText : Edm.String "Note Text"
PX.Objects.CA.CATransfer.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CATransfer.CreatedByScreenID : Edm.String
PX.Objects.CA.CATransfer.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CATransfer.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CATransfer.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CATransfer.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.CATransfer.tstamp : Edm.Binary
PX.Objects.CA.CATransfer.Status : Edm.String "Status"
PX.Objects.CA.CATransfer.ClearedOut : Edm.Boolean [required] "Cleared"
PX.Objects.CA.CATransfer.ClearDateOut : Edm.DateTimeOffset "Clear Date"
PX.Objects.CA.CATransfer.ClearedIn : Edm.Boolean [required] "Cleared"
PX.Objects.CA.CATransfer.ClearDateIn : Edm.DateTimeOffset "Clear Date"
PX.Objects.CA.CATransfer.CashBalanceIn : Edm.Decimal "Available Balance"
PX.Objects.CA.CATransfer.CashBalanceOut : Edm.Decimal "Available Balance"
PX.Objects.CA.CATransfer.InGLBalance : Edm.Decimal "GL Balance"
PX.Objects.CA.CATransfer.OutGLBalance : Edm.Decimal "GL Balance"
PX.Objects.CA.CATransfer.BaseCuryID : Edm.String "BaseCuryID"
PX.Objects.CA.CATransfer.TotalExpenses : Edm.Decimal "Total Charges"
PX.Objects.CA.CATransfer.CuryRate : Edm.Decimal
PX.Objects.CA.CATransfer.OutCuryRate : Edm.Decimal
PX.Objects.CA.CATransfer.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.CATransfer.CATranByTranIDOut -> PX.Objects.CA.CATran (TranIDOut=TranID)
PX.Objects.CA.CATransfer.CATranByTranIDIn -> PX.Objects.CA.CATran (TranIDIn=TranID)
PX.Objects.CA.CATransfer.BranchByOutBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CATransfer.BranchByInBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.CATransfer.CurrencyInfoByOutCuryInfoID -> PX.Objects.CM.CurrencyInfo (OutCuryInfoID=CuryInfoID)
PX.Objects.CA.CATransfer.CurrencyInfoByInCuryInfoID -> PX.Objects.CM.CurrencyInfo (InCuryInfoID=CuryInfoID)
PX.Objects.CA.CATransfer.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CATransfer.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CATransfer.CurrencyByInCuryID -> PX.Objects.CM.Currency (InCuryID=CuryID)
PX.Objects.CA.CATransfer.CurrencyByOutCuryID -> PX.Objects.CM.Currency (OutCuryID=CuryID)
PX.Objects.CA.CATransfer.CurrencyByTranIDOut -> PX.Objects.CM.Currency (TranIDOut=CuryID)
PX.Objects.CA.CATransfer.CurrencyByTranIDIn -> PX.Objects.CM.Currency (TranIDIn=CuryID)
PX.Objects.CA.CATransfer.AccountByTransitAcctID -> PX.Objects.GL.Account
PX.Objects.CA.CATransfer.SubByTransitSubID -> PX.Objects.GL.Sub
PX.Objects.CA.CATransfer.CashAccountByOutAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CATransfer.CashAccountByInAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CATransfer.CATransferByTransferNbr -> PX.Objects.CA.CATransfer (TransferNbr=OrigTransferNbr)
PX.Objects.CA.CATransfer.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.CA.CATransfer.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)

# PX.Objects.CA.CCBatch (EntityType)

Label: "CCBatch"
Key: BatchID
Entity sets: PX_Objects_CA_CCBatch, CCBatch
Non-filterable, non-selectable: SettlementTime, ExcludedCount, Description, NoteText

PX.Objects.CA.CCBatch.BatchID : Edm.Int32 [key] "Reference Number"
PX.Objects.CA.CCBatch.Status : Edm.String "Status"
PX.Objects.CA.CCBatch.ProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.CA.CCBatch.CuryID : Edm.String "Currency"
PX.Objects.CA.CCBatch.ExtBatchID : Edm.String "Ext. Batch ID"
PX.Objects.CA.CCBatch.SettlementTimeUTC : Edm.DateTimeOffset "Settlement Time UTC"
PX.Objects.CA.CCBatch.SettlementTime : Edm.DateTimeOffset "Settlement Time"
PX.Objects.CA.CCBatch.SettlementState : Edm.String "Settlement State"
PX.Objects.CA.CCBatch.ProcessedCount : Edm.Int32 [required] "Processed Count"
PX.Objects.CA.CCBatch.MissingCount : Edm.Int32 [required] "Missing Transaction Count"
PX.Objects.CA.CCBatch.HiddenCount : Edm.Int32 [required] "Hidden Count"
PX.Objects.CA.CCBatch.ExcludedCount : Edm.Int32 "Excluded from Deposit Count"
PX.Objects.CA.CCBatch.TransactionCount : Edm.Int32 [required] "Transaction Count"
PX.Objects.CA.CCBatch.ImportedTransactionCount : Edm.Int32 [required] "Imported Transaction Count"
PX.Objects.CA.CCBatch.UnprocessedCount : Edm.Int32 [required] "Unprocessed Transaction Count"
PX.Objects.CA.CCBatch.SettledAmount : Edm.Decimal [required] "Settled Amount"
PX.Objects.CA.CCBatch.SettledCount : Edm.Int32 [required] "Settled Count"
PX.Objects.CA.CCBatch.RefundAmount : Edm.Decimal [required] "Refund Amount"
PX.Objects.CA.CCBatch.RefundCount : Edm.Int32 [required] "Refund Count"
PX.Objects.CA.CCBatch.RejectedAmount : Edm.Decimal [required] "Rejected Amount"
PX.Objects.CA.CCBatch.RejectedCount : Edm.Int32 [required] "Rejected Count"
PX.Objects.CA.CCBatch.VoidCount : Edm.Int32 [required] "Void Count"
PX.Objects.CA.CCBatch.DeclineCount : Edm.Int32 [required] "Decline Count"
PX.Objects.CA.CCBatch.ErrorCount : Edm.Int32 [required] "Error Count"
PX.Objects.CA.CCBatch.DepositType : Edm.String
PX.Objects.CA.CCBatch.DepositNbr : Edm.String "Bank Deposit"
PX.Objects.CA.CCBatch.SkipDepositAutoCreation : Edm.Boolean [required]
PX.Objects.CA.CCBatch.BatchType : Edm.String
PX.Objects.CA.CCBatch.Description : Edm.String
PX.Objects.CA.CCBatch.IsManual : Edm.Boolean [required]
PX.Objects.CA.CCBatch.NetSettledAmount : Edm.Decimal "Net Amount"
PX.Objects.CA.CCBatch.Fee : Edm.Decimal "Fee"
PX.Objects.CA.CCBatch.FeeType : Edm.String "Fee Type"
PX.Objects.CA.CCBatch.AdjustmentCounter : Edm.Int32 [required] "Adjustment Count"
PX.Objects.CA.CCBatch.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCBatch.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CCBatch.CreatedByScreenID : Edm.String
PX.Objects.CA.CCBatch.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCBatch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CCBatch.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CCBatch.Tstamp : Edm.Binary "Tstamp"
PX.Objects.CA.CCBatch.Noteid : Edm.Guid
PX.Objects.CA.CCBatch.NoteText : Edm.String "Note Text"
PX.Objects.CA.CCBatch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CCBatch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CCBatch.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.CCBatch.CADepositByDepositNbr -> PX.Objects.CA.CADeposit (DepositType=TranType, DepositNbr=RefNbr)
PX.Objects.CA.CCBatch.CADepositByDepositType -> PX.Objects.CA.CADeposit (DepositNbr=RefNbr, DepositType=TranType)
PX.Objects.CA.CCBatch.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.CA.CCBatch.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.CA.CCBatch.CCBatchStatisticsCollection -> Collection(PX.Objects.CA.CCBatchStatistics)
PX.Objects.CA.CCBatch.CCBatchAdjustmentCollection -> Collection(PX.Objects.CA.CCBatchAdjustment)

# PX.Objects.CA.CCBatchAdjustment (EntityType)

Label: "CCBatchAdjustment"
Key: BatchID, ExternalID
Entity sets: PX_Objects_CA_CCBatchAdjustment, CCBatchAdjustment
Non-filterable, non-selectable: AdjustmentTime

PX.Objects.CA.CCBatchAdjustment.BatchID : Edm.Int32 [key]
PX.Objects.CA.CCBatchAdjustment.ExternalID : Edm.String [key] "Ext. Transaction ID"
PX.Objects.CA.CCBatchAdjustment.SourceID : Edm.String "Source ID"
PX.Objects.CA.CCBatchAdjustment.AdjustmentTimeUTC : Edm.DateTimeOffset "Adjustment Time"
PX.Objects.CA.CCBatchAdjustment.AdjustmentTime : Edm.DateTimeOffset "Adjustment Time"
PX.Objects.CA.CCBatchAdjustment.SettledAmount : Edm.Decimal "Amount"
PX.Objects.CA.CCBatchAdjustment.NetSettledAmount : Edm.Decimal "Net Amount"
PX.Objects.CA.CCBatchAdjustment.Fee : Edm.Decimal "Fee"
PX.Objects.CA.CCBatchAdjustment.FeeType : Edm.String "Fee Type"
PX.Objects.CA.CCBatchAdjustment.Description : Edm.String "Description"
PX.Objects.CA.CCBatchAdjustment.CCBatchByBatchID -> PX.Objects.CA.CCBatch (BatchID=BatchID)

# PX.Objects.CA.CCBatchStatistics (EntityType)

Label: "CCBatchStatistics"
Key: BatchID, ProcCenterCardTypeCode
Entity sets: PX_Objects_CA_CCBatchStatistics, CCBatchStatistics
Non-filterable, non-selectable: DisplayCardType, NoteText

PX.Objects.CA.CCBatchStatistics.BatchID : Edm.Int32 [key] "Batch ID"
PX.Objects.CA.CCBatchStatistics.ProcCenterCardTypeCode : Edm.String [key] "Proc. Center Card Type"
PX.Objects.CA.CCBatchStatistics.CardTypeCode : Edm.String "Card Type"
PX.Objects.CA.CCBatchStatistics.DisplayCardType : Edm.String "Card Type"
PX.Objects.CA.CCBatchStatistics.SettledAmount : Edm.Decimal "Settled Amount"
PX.Objects.CA.CCBatchStatistics.SettledCount : Edm.Int32 "Settled Count"
PX.Objects.CA.CCBatchStatistics.RefundAmount : Edm.Decimal "Refund Amount"
PX.Objects.CA.CCBatchStatistics.RefundCount : Edm.Int32 "Refund Count"
PX.Objects.CA.CCBatchStatistics.RejectedAmount : Edm.Decimal "Rejected Amount"
PX.Objects.CA.CCBatchStatistics.RejectedCount : Edm.Int32 [required] "Rejected Count"
PX.Objects.CA.CCBatchStatistics.VoidCount : Edm.Int32 "Void Count"
PX.Objects.CA.CCBatchStatistics.DeclineCount : Edm.Int32 "Decline Count"
PX.Objects.CA.CCBatchStatistics.ErrorCount : Edm.Int32 "Error Count"
PX.Objects.CA.CCBatchStatistics.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCBatchStatistics.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CCBatchStatistics.CreatedByScreenID : Edm.String
PX.Objects.CA.CCBatchStatistics.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCBatchStatistics.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CCBatchStatistics.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CCBatchStatistics.Tstamp : Edm.Binary "Tstamp"
PX.Objects.CA.CCBatchStatistics.Noteid : Edm.Guid
PX.Objects.CA.CCBatchStatistics.NoteText : Edm.String "Note Text"
PX.Objects.CA.CCBatchStatistics.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CCBatchStatistics.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CCBatchStatistics.CCBatchByBatchID -> PX.Objects.CA.CCBatch (BatchID=BatchID)

# PX.Objects.CA.CCBatchTransaction (EntityType)

Label: "CCBatchTransaction"
Key: BatchID, PCTranNumber, SettlementStatus
Entity sets: PX_Objects_CA_CCBatchTransaction, CCBatchTransaction
Non-filterable, non-selectable: SelectedToHide, SelectedToUnhide, DisplayCardType, NoteText

PX.Objects.CA.CCBatchTransaction.SelectedToHide : Edm.Boolean "Selected"
PX.Objects.CA.CCBatchTransaction.SelectedToUnhide : Edm.Boolean "Selected"
PX.Objects.CA.CCBatchTransaction.BatchID : Edm.Int32 [key] "Batch ID"
PX.Objects.CA.CCBatchTransaction.PCTranNumber : Edm.String [key] "Proc. Center Tran. Nbr."
PX.Objects.CA.CCBatchTransaction.PCCustomerID : Edm.String "Proc. Center Customer ID"
PX.Objects.CA.CCBatchTransaction.PCPaymentProfileID : Edm.String "Proc. Center Profile ID"
PX.Objects.CA.CCBatchTransaction.SettlementStatus : Edm.String [key] "Settlement Status"
PX.Objects.CA.CCBatchTransaction.InvoiceNbr : Edm.String "Invoice Nbr"
PX.Objects.CA.CCBatchTransaction.SubmitTime : Edm.DateTimeOffset "Submit Time"
PX.Objects.CA.CCBatchTransaction.ProcCenterCardTypeCode : Edm.String "Proc. Center Card Type"
PX.Objects.CA.CCBatchTransaction.CardTypeCode : Edm.String "Card Type"
PX.Objects.CA.CCBatchTransaction.DisplayCardType : Edm.String "Card Type"
PX.Objects.CA.CCBatchTransaction.AccountNumber : Edm.String "Card/Account Nbr."
PX.Objects.CA.CCBatchTransaction.Amount : Edm.Decimal "Amount"
PX.Objects.CA.CCBatchTransaction.FixedFee : Edm.Decimal "Fixed Fee"
PX.Objects.CA.CCBatchTransaction.PercentageFee : Edm.Decimal "Percentage Fee"
PX.Objects.CA.CCBatchTransaction.TotalFee : Edm.Decimal "Total Fee"
PX.Objects.CA.CCBatchTransaction.FeeType : Edm.String "Fee Type"
PX.Objects.CA.CCBatchTransaction.TransactionID : Edm.Int32 "Transaction ID"
PX.Objects.CA.CCBatchTransaction.OriginalStatus : Edm.String "Original Status"
PX.Objects.CA.CCBatchTransaction.CurrentStatus : Edm.String "Current Status"
PX.Objects.CA.CCBatchTransaction.ProcessingStatus : Edm.String "Processing Status"
PX.Objects.CA.CCBatchTransaction.DocType : Edm.String "Doc. Type"
PX.Objects.CA.CCBatchTransaction.RefNbr : Edm.String "Reference Nbr."
PX.Objects.CA.CCBatchTransaction.Comment : Edm.String "Comment"
PX.Objects.CA.CCBatchTransaction.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCBatchTransaction.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CCBatchTransaction.CreatedByScreenID : Edm.String
PX.Objects.CA.CCBatchTransaction.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCBatchTransaction.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CCBatchTransaction.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CCBatchTransaction.Tstamp : Edm.Binary "Tstamp"
PX.Objects.CA.CCBatchTransaction.Noteid : Edm.Guid
PX.Objects.CA.CCBatchTransaction.NoteText : Edm.String "Note Text"
PX.Objects.CA.CCBatchTransaction.ARPaymentByRefNbr -> PX.Objects.AR.ARPayment (DocType=DocType, RefNbr=RefNbr)
PX.Objects.CA.CCBatchTransaction.ARRegisterByDocType -> PX.Objects.AR.ARRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.CA.CCBatchTransaction.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CCBatchTransaction.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CCBatchTransaction.CCBatchByBatchID -> PX.Objects.CA.CCBatch (BatchID=BatchID)
PX.Objects.CA.CCBatchTransaction.ExternalTransactionByTransactionID -> PX.Objects.AR.ExternalTransaction (TransactionID=TransactionID)

# PX.Objects.CA.CCProcessingCenter (EntityType)

Label: "Processing Center"
Key: ProcessingCenterID
Entity sets: PX_Objects_CA_CCProcessingCenter, ProcessingCenter, CCProcessingCenter
Non-filterable, non-selectable: NeedsExpDateUpdate, LastSettlementDate, NoteText

PX.Objects.CA.CCProcessingCenter.ProcessingCenterID : Edm.String [key] "Proc. Center ID"
PX.Objects.CA.CCProcessingCenter.Name : Edm.String "Name"
PX.Objects.CA.CCProcessingCenter.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CA.CCProcessingCenter.ProcessingTypeName : Edm.String "Payment Plug-In"
PX.Objects.CA.CCProcessingCenter.ProcessingAssemblyName : Edm.String "Assembly Name"
PX.Objects.CA.CCProcessingCenter.OpenTranTimeout : Edm.Int32 "Transaction Timeout (s)"
PX.Objects.CA.CCProcessingCenter.AllowDirectInput : Edm.Boolean "Allow Direct Input"
PX.Objects.CA.CCProcessingCenter.NeedsExpDateUpdate : Edm.Boolean
PX.Objects.CA.CCProcessingCenter.SyncronizeDeletion : Edm.Boolean [required] "Synchronize Deletion"
PX.Objects.CA.CCProcessingCenter.UseAcceptPaymentForm : Edm.Boolean [required] "Accept Payments from New Cards"
PX.Objects.CA.CCProcessingCenter.AllowSaveProfile : Edm.Boolean [required] "Allow Saving Payment Profiles"
PX.Objects.CA.CCProcessingCenter.AllowUnlinkedRefund : Edm.Boolean [required] "Allow Unlinked Refunds"
PX.Objects.CA.CCProcessingCenter.AllowAuthorizedIncrement : Edm.Boolean [required] "Allow Increasing Authorized Amounts"
PX.Objects.CA.CCProcessingCenter.L3MissingInventoryItemID : Edm.Int32 "Missing Inventory ID (System Item)"
PX.Objects.CA.CCProcessingCenter.AcceptPOSPayments : Edm.Boolean [required] "Accept Payments from POS Terminals"
PX.Objects.CA.CCProcessingCenter.AllowMobileTerminal : Edm.Boolean [required] "Use EMV Card Reader with Mobile App"
PX.Objects.CA.CCProcessingCenter.SyncRetryAttemptsNo : Edm.Int32 "Number of Additional Synchronization Attempts"
PX.Objects.CA.CCProcessingCenter.SyncRetryDelayMs : Edm.Int32 "Delay Between Synchronization Attempts (ms)"
PX.Objects.CA.CCProcessingCenter.CreditCardLimit : Edm.Int32 "Maximum Credit Cards per Profile"
PX.Objects.CA.CCProcessingCenter.CreateAdditionalCustomerProfiles : Edm.Boolean "Create Additional Customer Profiles"
PX.Objects.CA.CCProcessingCenter.ImportSettlementBatches : Edm.Boolean [required] "Import Settlement Batches"
PX.Objects.CA.CCProcessingCenter.ImportStartDate : Edm.DateTimeOffset "Import Start Date"
PX.Objects.CA.CCProcessingCenter.LastSettlementDateUTC : Edm.DateTimeOffset "Last Settlement Date UTC"
PX.Objects.CA.CCProcessingCenter.LastSettlementDate : Edm.DateTimeOffset "Last Settlement Date"
PX.Objects.CA.CCProcessingCenter.ReauthRetryDelay : Edm.Int32 [required] "Reauthorization Retry Delay (Hours)"
PX.Objects.CA.CCProcessingCenter.ReauthRetryNbr : Edm.Int32 [required] "Number of Reauthorization Retries"
PX.Objects.CA.CCProcessingCenter.AutoCreateBankDeposit : Edm.Boolean [required] "Automatically Create Bank Deposits"
PX.Objects.CA.CCProcessingCenter.IsExternalAuthorizationOnly : Edm.Boolean [required]
PX.Objects.CA.CCProcessingCenter.AllowPayLink : Edm.Boolean [required] "Allow Payment Links"
PX.Objects.CA.CCProcessingCenter.AllowPartialPayment : Edm.Boolean [required] "Allow Partial Payment"
PX.Objects.CA.CCProcessingCenter.AttachDetailsToPayLink : Edm.Boolean [required] "Attach Document Details as PDF"
PX.Objects.CA.CCProcessingCenter.DocTypeForSOPayLink : Edm.String "Create from Payment Link (SO & Prepmt. Inv.)"
PX.Objects.CA.CCProcessingCenter.WebhookID : Edm.Guid "Webhook ID"
PX.Objects.CA.CCProcessingCenter.Environment : Edm.String
PX.Objects.CA.CCProcessingCenter.SurchargeConfigured : Edm.Boolean [required] "Compliant Surcharge"
PX.Objects.CA.CCProcessingCenter.SurchargeEntryType : Edm.String "Surcharge Entry Type"
PX.Objects.CA.CCProcessingCenter.NoteID : Edm.Guid
PX.Objects.CA.CCProcessingCenter.NoteText : Edm.String "Note Text"
PX.Objects.CA.CCProcessingCenter.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CCProcessingCenter.CreatedByScreenID : Edm.String
PX.Objects.CA.CCProcessingCenter.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCProcessingCenter.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CCProcessingCenter.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CCProcessingCenter.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCProcessingCenter.tstamp : Edm.Binary
PX.Objects.CA.CCProcessingCenter.InventoryItemByL3MissingInventoryItemID -> PX.Objects.IN.InventoryItem (L3MissingInventoryItemID=InventoryID)
PX.Objects.CA.CCProcessingCenter.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CCProcessingCenter.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CCProcessingCenter.CAEntryTypeBySurchargeEntryType -> PX.Objects.CA.CAEntryType (SurchargeEntryType=EntryTypeId)
PX.Objects.CA.CCProcessingCenter.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CCProcessingCenter.CashAccountByDepositAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CCProcessingCenter.WebHookByWebhookID -> PX.Api.Webhooks.DAC.WebHook (WebhookID=WebHookID)
PX.Objects.CA.CCProcessingCenter.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CA.CCProcessingCenter.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.CA.CCProcessingCenter.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.CA.CCProcessingCenter.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CA.CCProcessingCenter.CCProcessingCenterTerminalCollection -> Collection(PX.Objects.CC.CCProcessingCenterTerminal)
PX.Objects.CA.CCProcessingCenter.CCBatchCollection -> Collection(PX.Objects.CA.CCBatch)
PX.Objects.CA.CCProcessingCenter.CCProcessingCenterDetailCollection -> Collection(PX.Objects.CA.CCProcessingCenterDetail)
PX.Objects.CA.CCProcessingCenter.CCProcessingCenterFeeTypeCollection -> Collection(PX.Objects.CA.CCProcessingCenterFeeType)
PX.Objects.CA.CCProcessingCenter.CCProcessingCenterPmntMethodBranchCollection -> Collection(PX.Objects.CA.CCProcessingCenterPmntMethodBranch)
PX.Objects.CA.CCProcessingCenter.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.Objects.CA.CCProcessingCenter.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.CA.CCProcessingCenter.CCProcessingCenterBranchCollection -> Collection(PX.Objects.CC.CCProcessingCenterBranch)
PX.Objects.CA.CCProcessingCenter.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.CA.CCProcessingCenter.CustomerProcessingCenterIDCollection -> Collection(PX.Objects.CA.CustomerProcessingCenterID)
PX.Objects.CA.CCProcessingCenter.BCPaymentMethodsCollection -> Collection(PX.Commerce.Objects.BCPaymentMethods)
PX.Objects.CA.CCProcessingCenter.CCProcessingCenterPmntMethodCollection -> Collection(PX.Objects.CA.CCProcessingCenterPmntMethod)

# PX.Objects.CA.CCProcessingCenterDetail (EntityType)

Label: "Credit Card Processing Center Detail"
Key: DetailID, ProcessingCenterID
Entity sets: PX_Objects_CA_CCProcessingCenterDetail, CreditCardProcessingCenterDetail, CCProcessingCenterDetail

PX.Objects.CA.CCProcessingCenterDetail.ProcessingCenterID : Edm.String [key]
PX.Objects.CA.CCProcessingCenterDetail.DetailID : Edm.String [key] "ID"
PX.Objects.CA.CCProcessingCenterDetail.Descr : Edm.String "Description"
PX.Objects.CA.CCProcessingCenterDetail.IsEncryptionRequired : Edm.Boolean [required]
PX.Objects.CA.CCProcessingCenterDetail.IsEncrypted : Edm.Boolean [required]
PX.Objects.CA.CCProcessingCenterDetail.Value : Edm.String "Value"
PX.Objects.CA.CCProcessingCenterDetail.ControlType : Edm.Int32 [required] "Control Type"
PX.Objects.CA.CCProcessingCenterDetail.ComboValues : Edm.String
PX.Objects.CA.CCProcessingCenterDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CCProcessingCenterDetail.CreatedByScreenID : Edm.String
PX.Objects.CA.CCProcessingCenterDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCProcessingCenterDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CCProcessingCenterDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CCProcessingCenterDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCProcessingCenterDetail.tstamp : Edm.Binary
PX.Objects.CA.CCProcessingCenterDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CCProcessingCenterDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CCProcessingCenterDetail.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)

# PX.Objects.CA.CCProcessingCenterFeeType (EntityType)

Label: "Fee Type for Credit Card Processing Center"
Key: EntryTypeID, FeeType, ProcessingCenterID
Entity sets: PX_Objects_CA_CCProcessingCenterFeeType, FeeTypeforCreditCardProcessingCenter, CCProcessingCenterFeeType

PX.Objects.CA.CCProcessingCenterFeeType.ProcessingCenterID : Edm.String [key]
PX.Objects.CA.CCProcessingCenterFeeType.FeeType : Edm.String [key] "Fee Type"
PX.Objects.CA.CCProcessingCenterFeeType.EntryTypeID : Edm.String [key] "Entry Type"
PX.Objects.CA.CCProcessingCenterFeeType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCProcessingCenterFeeType.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CCProcessingCenterFeeType.CreatedByScreenID : Edm.String
PX.Objects.CA.CCProcessingCenterFeeType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCProcessingCenterFeeType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CCProcessingCenterFeeType.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CCProcessingCenterFeeType.Tstamp : Edm.Binary
PX.Objects.CA.CCProcessingCenterFeeType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CCProcessingCenterFeeType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CCProcessingCenterFeeType.CAEntryTypeByEntryTypeID -> PX.Objects.CA.CAEntryType (EntryTypeID=EntryTypeId)
PX.Objects.CA.CCProcessingCenterFeeType.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)

# PX.Objects.CA.CCProcessingCenterPmntMethod (EntityType)

Label: "Payment Method for Credit Card Processing Center"
Key: PaymentMethodID, ProcessingCenterID
Entity sets: PX_Objects_CA_CCProcessingCenterPmntMethod, PaymentMethodforCreditCardProcessingCenter, CCProcessingCenterPmntMethod

PX.Objects.CA.CCProcessingCenterPmntMethod.ProcessingCenterID : Edm.String [key] "Proc. Center ID"
PX.Objects.CA.CCProcessingCenterPmntMethod.PaymentMethodID : Edm.String [key] "Payment Method"
PX.Objects.CA.CCProcessingCenterPmntMethod.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CA.CCProcessingCenterPmntMethod.IsDefault : Edm.Boolean [required] "Default"
PX.Objects.CA.CCProcessingCenterPmntMethod.FundHoldPeriod : Edm.Int32 [required] "Funds Hold Period (Days)"
PX.Objects.CA.CCProcessingCenterPmntMethod.ReauthDelay : Edm.Int32 "Reauthorization Delay (Hours)"
PX.Objects.CA.CCProcessingCenterPmntMethod.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.CA.CCProcessingCenterPmntMethod.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CCProcessingCenterPmntMethod.CCProcessingCenterPmntMethodBranchCollection -> Collection(PX.Objects.CA.CCProcessingCenterPmntMethodBranch)
PX.Objects.CA.CCProcessingCenterPmntMethod.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.CA.CCProcessingCenterPmntMethod.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)

# PX.Objects.CA.CCProcessingCenterPmntMethodBranch (EntityType)

Label: "Overrides By Branch"
Key: BranchID, PaymentMethodID
Entity sets: PX_Objects_CA_CCProcessingCenterPmntMethodBranch, OverridesByBranch, CCProcessingCenterPmntMethodBranch

PX.Objects.CA.CCProcessingCenterPmntMethodBranch.ProcessingCenterID : Edm.String "Default Processing Center"
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.PaymentMethodID : Edm.String [key]
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.CreatedByScreenID : Edm.String
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.LastModifiedByScreenID : Edm.String
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.tstamp : Edm.Binary
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CCProcessingCenterPmntMethodBranch.CCProcessingCenterPmntMethodByPaymentMethodID -> PX.Objects.CA.CCProcessingCenterPmntMethod (ProcessingCenterID=ProcessingCenterID, PaymentMethodID=PaymentMethodID)

# PX.Objects.CA.CCSynchronizeCard (EntityType)

Key: RecordID
Entity sets: PX_Objects_CA_CCSynchronizeCard
Non-filterable, non-selectable: NoteText

PX.Objects.CA.CCSynchronizeCard.RecordID : Edm.Int32 [key] "RecordID"
PX.Objects.CA.CCSynchronizeCard.CCProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.CA.CCSynchronizeCard.CustomerCCPID : Edm.String "Proc. Center Cust. Profile ID"
PX.Objects.CA.CCSynchronizeCard.CustomerCCPIDHash : Edm.String
PX.Objects.CA.CCSynchronizeCard.PaymentCCPID : Edm.String "Proc. Center Payment Profile ID"
PX.Objects.CA.CCSynchronizeCard.PCCustomerID : Edm.String "Proc. Center Cust. ID"
PX.Objects.CA.CCSynchronizeCard.PCCustomerDescription : Edm.String "Proc. Center Cust. Descr."
PX.Objects.CA.CCSynchronizeCard.PCCustomerEmail : Edm.String "Proc. Center Cust. Email"
PX.Objects.CA.CCSynchronizeCard.CardType : Edm.String "Card Type"
PX.Objects.CA.CCSynchronizeCard.ProcCenterCardTypeCode : Edm.String "Proc. Center Card Type"
PX.Objects.CA.CCSynchronizeCard.CardNumber : Edm.String "Card Number"
PX.Objects.CA.CCSynchronizeCard.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.CA.CCSynchronizeCard.FirstName : Edm.String "Proc. Center Payment Profile First Name"
PX.Objects.CA.CCSynchronizeCard.LastName : Edm.String "Proc. Center Payment Profile Last Name"
PX.Objects.CA.CCSynchronizeCard.BAccountID : Edm.Int32 "Customer ID"
PX.Objects.CA.CCSynchronizeCard.PaymentType : Edm.String "Means of Payment"
PX.Objects.CA.CCSynchronizeCard.PaymentMethodID : Edm.String "Payment Method"
PX.Objects.CA.CCSynchronizeCard.Imported : Edm.Boolean [required]
PX.Objects.CA.CCSynchronizeCard.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.CCSynchronizeCard.NoteID : Edm.Guid
PX.Objects.CA.CCSynchronizeCard.NoteText : Edm.String "Note Text"
PX.Objects.CA.CCSynchronizeCard.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CA.CCSynchronizeCard.CustomerByBAccountID -> PX.Objects.AR.Customer (BAccountID=BAccountID)
PX.Objects.CA.CCSynchronizeCard.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.CCSynchronizeCard.CCProcessingCenterByCCProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (CCProcessingCenterID=ProcessingCenterID)
PX.Objects.CA.CCSynchronizeCard.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CCSynchronizeCard.CCProcessingCenterPmntMethodByPaymentMethodID -> PX.Objects.CA.CCProcessingCenterPmntMethod (CCProcessingCenterID=ProcessingCenterID, PaymentMethodID=PaymentMethodID)
PX.Objects.CA.CCSynchronizeCard.CCProcessingCenterPmntMethodByCCProcessingCenterID -> PX.Objects.CA.CCProcessingCenterPmntMethod (PaymentMethodID=PaymentMethodID, CCProcessingCenterID=ProcessingCenterID)

# PX.Objects.CA.CustomerProcessingCenterID (EntityType)

Label: "Customer Processing Center ID"
Key: InstanceID
Entity sets: PX_Objects_CA_CustomerProcessingCenterID, CustomerProcessingCenterID

PX.Objects.CA.CustomerProcessingCenterID.InstanceID : Edm.Int32 [key]
PX.Objects.CA.CustomerProcessingCenterID.BAccountID : Edm.Int32 "Customer"
PX.Objects.CA.CustomerProcessingCenterID.CCProcessingCenterID : Edm.String "Proc. Center ID"
PX.Objects.CA.CustomerProcessingCenterID.CustomerCCPID : Edm.String "Customer CCPID"
PX.Objects.CA.CustomerProcessingCenterID.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.CustomerProcessingCenterID.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CA.CustomerProcessingCenterID.CustomerByBAccountID -> PX.Objects.AR.Customer (BAccountID=BAccountID)
PX.Objects.CA.CustomerProcessingCenterID.CCProcessingCenterByCCProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (CCProcessingCenterID=ProcessingCenterID)
PX.Objects.CA.CustomerProcessingCenterID.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)

# PX.Objects.CA.Light.APAdjust (EntityType)

Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr
Entity sets: PX_Objects_CA_Light_APAdjust

PX.Objects.CA.Light.APAdjust.AdjgDocType : Edm.String [key]
PX.Objects.CA.Light.APAdjust.AdjgRefNbr : Edm.String [key]
PX.Objects.CA.Light.APAdjust.AdjdDocType : Edm.String [key]
PX.Objects.CA.Light.APAdjust.AdjdRefNbr : Edm.String [key]
PX.Objects.CA.Light.APAdjust.AdjNbr : Edm.Int32 [key]
PX.Objects.CA.Light.APAdjust.AdjdLineNbr : Edm.Int32 [key]
PX.Objects.CA.Light.APAdjust.Released : Edm.Boolean
PX.Objects.CA.Light.APAdjust.Voided : Edm.Boolean
PX.Objects.CA.Light.APAdjust.VendorByVendorID -> PX.Objects.AP.Vendor
PX.Objects.CA.Light.APAdjust.APInvoiceByAdjdRefNbr -> PX.Objects.AP.APInvoice (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.CA.Light.APAdjust.APInvoiceByAdjdDocType -> PX.Objects.AP.APInvoice (AdjdRefNbr=RefNbr, AdjdDocType=DocType)
PX.Objects.CA.Light.APAdjust.BAccountByVendorID -> PX.Objects.CR.BAccount
PX.Objects.CA.Light.APAdjust.BatchByAdjBatchNbr -> PX.Objects.GL.Batch
PX.Objects.CA.Light.APAdjust.APRegisterByAdjgRefNbr -> PX.Objects.AP.APRegister (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.CA.Light.APAdjust.APRegisterByAdjdRefNbr -> PX.Objects.AP.APRegister (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.CA.Light.APAdjust.APRegisterByPPDVATAdjRefNbr -> PX.Objects.AP.APRegister
PX.Objects.CA.Light.APAdjust.APRegisterByAdjdDocType -> PX.Objects.AP.APRegister (AdjdRefNbr=RefNbr, AdjdDocType=DocType)
PX.Objects.CA.Light.APAdjust.APRegisterByAdjgDocType -> PX.Objects.AP.APRegister (AdjgRefNbr=RefNbr, AdjgDocType=DocType)
PX.Objects.CA.Light.APAdjust.BranchByAdjgBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.Light.APAdjust.BranchByAdjdBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.Light.APAdjust.CurrencyInfoByAdjgCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CA.Light.APAdjust.CurrencyInfoByAdjdCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CA.Light.APAdjust.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CA.Light.APAdjust.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CA.Light.APAdjust.AccountByAdjdWhTaxAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.APAdjust.AccountByAdjdAPAcct -> PX.Objects.GL.Account
PX.Objects.CA.Light.APAdjust.SubByAdjdWhTaxSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.APAdjust.SubByAdjdAPSub -> PX.Objects.GL.Sub
PX.Objects.CA.Light.APAdjust.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount
PX.Objects.CA.Light.APAdjust.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.Objects.CA.Light.APAdjust.APTranByAdjdRefNbr -> PX.Objects.AP.APTran (AdjdLineNbr=LineNbr, AdjdDocType=TranType, AdjdRefNbr=RefNbr)
PX.Objects.CA.Light.APAdjust.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.CA.Light.APAdjust.APAdjustEFileRevisionCollection -> Collection(PX.Objects.Localizations.CA.APAdjustEFileRevision)

# PX.Objects.CA.Light.APInvoice (EntityType)

BaseType: PX.Objects.CA.Light.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.CA.Light.APRegister)
Entity sets: PX_Objects_CA_Light_APInvoice
Non-filterable, non-selectable: DrCr

PX.Objects.CA.Light.APInvoice.InvoiceNbr : Edm.String
PX.Objects.CA.Light.APInvoice.PayAccountID : Edm.Int32
PX.Objects.CA.Light.APInvoice.DueDate : Edm.DateTimeOffset
PX.Objects.CA.Light.APInvoice.PayDate : Edm.DateTimeOffset
PX.Objects.CA.Light.APInvoice.DrCr : Edm.String
PX.Objects.CA.Light.APInvoice.TermsID : Edm.String
PX.Objects.CA.Light.APInvoice.PayTypeID : Edm.String
PX.Objects.CA.Light.APInvoice.DiscDate : Edm.DateTimeOffset
PX.Objects.CA.Light.APInvoice.VendorBySuppliedByVendorID -> PX.Objects.AP.Vendor
PX.Objects.CA.Light.APInvoice.ARInvoiceByIntercompanyInvoiceNoteID -> PX.Objects.AR.ARInvoice
PX.Objects.CA.Light.APInvoice.BAccountBySuppliedByVendorID -> PX.Objects.CR.BAccount
PX.Objects.CA.Light.APInvoice.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.CA.Light.APInvoice.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone
PX.Objects.CA.Light.APInvoice.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.CA.Light.APInvoice.AccountByPrebookAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.APInvoice.SubByPrebookSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.APInvoice.CashAccountByPayAccountID -> PX.Objects.CA.CashAccount (PayAccountID=CashAccountID)
PX.Objects.CA.Light.APInvoice.CashAccountByBranchID -> PX.Objects.CA.CashAccount (PayAccountID=CashAccountID)
PX.Objects.CA.Light.APInvoice.PaymentMethodByPayTypeID -> PX.Objects.CA.PaymentMethod (PayTypeID=PaymentMethodID)
PX.Objects.CA.Light.APInvoice.LocationBySuppliedByVendorLocationID -> PX.Objects.CR.Location
PX.Objects.CA.Light.APInvoice.LocationBySuppliedByVendorID -> PX.Objects.CR.Location
PX.Objects.CA.Light.APInvoice.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.CA.Light.APInvoice.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CA.Light.APInvoice.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.Light.APInvoice.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.CA.Light.APInvoice.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.CA.Light.APInvoice.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.CA.Light.APInvoice.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.CA.Light.APInvoice.POAccrualSplitCollection -> Collection(PX.Objects.PO.POAccrualSplit)
PX.Objects.CA.Light.APInvoice.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.CA.Light.APInvoice.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.CA.Light.APInvoice.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.Objects.CA.Light.APInvoice.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.CA.Light.APInvoice.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.CA.Light.APInvoice.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.CA.Light.APInvoice.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.CA.Light.APInvoice.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.CA.Light.APInvoice.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)

# PX.Objects.CA.Light.APPayment (EntityType)

Label: "Document"
BaseType: PX.Objects.AP.APRegister
Key: DocType, RefNbr (inherited from PX.Objects.AP.APRegister)
Entity sets: PX_Objects_CA_Light_APPayment

PX.Objects.CA.Light.APPayment.ExtRefNbr : Edm.String
PX.Objects.CA.Light.APPayment.PaymentMethodID : Edm.String
PX.Objects.CA.Light.APPayment.CashAccountID : Edm.Int32
PX.Objects.CA.Light.APPayment.VendorLocationID : Edm.Int32
PX.Objects.CA.Light.APPayment.CATranID : Edm.Int64
PX.Objects.CA.Light.APPayment.DepositAsBatch : Edm.Boolean
PX.Objects.CA.Light.APPayment.DepositAfter : Edm.DateTimeOffset
PX.Objects.CA.Light.APPayment.Deposited : Edm.Boolean
PX.Objects.CA.Light.APPayment.DepositType : Edm.String
PX.Objects.CA.Light.APPayment.DepositNbr : Edm.String
PX.Objects.CA.Light.APPayment.CATranByCATranID -> PX.Objects.CA.CATran (CATranID=TranID)
PX.Objects.CA.Light.APPayment.ContactByRemitContactID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.APPayment.APRegisterByDocType -> PX.Objects.AP.APRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.CA.Light.APPayment.AddressByRemitAddressID -> PX.Objects.CR.Address
PX.Objects.CA.Light.APPayment.CADepositByDepositType -> PX.Objects.CA.CADeposit (DepositNbr=RefNbr, DepositType=TranType)
PX.Objects.CA.Light.APPayment.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.Light.APPayment.CashAccountByBranchID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.Light.APPayment.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.Light.APPayment.APContactByRemitContactID -> PX.Objects.AP.APContact
PX.Objects.CA.Light.APPayment.CABatchDetailCollection -> Collection(PX.Objects.CA.CABatchDetail)
PX.Objects.CA.Light.APPayment.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CA.Light.APPayment.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.Light.APPayment.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.CA.Light.APPayment.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)
PX.Objects.CA.Light.APPayment.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CA.Light.APPayment.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.CA.Light.APPayment.APPrintCheckDetailCollection -> Collection(PX.Objects.AP.APPrintCheckDetail)

# PX.Objects.CA.Light.APRegister (EntityType)

Key: DocType, RefNbr
Entity sets: PX_Objects_CA_Light_APRegister
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CA.Light.APRegister.BranchID : Edm.Int32
PX.Objects.CA.Light.APRegister.DocType : Edm.String [key]
PX.Objects.CA.Light.APRegister.RefNbr : Edm.String [key]
PX.Objects.CA.Light.APRegister.DocDate : Edm.DateTimeOffset
PX.Objects.CA.Light.APRegister.FinPeriodID : Edm.String
PX.Objects.CA.Light.APRegister.VendorID : Edm.Int32
PX.Objects.CA.Light.APRegister.VendorLocationID : Edm.Int32
PX.Objects.CA.Light.APRegister.CuryID : Edm.String
PX.Objects.CA.Light.APRegister.CuryInfoID : Edm.Int64
PX.Objects.CA.Light.APRegister.CuryDocBal : Edm.Decimal
PX.Objects.CA.Light.APRegister.DocBal : Edm.Decimal
PX.Objects.CA.Light.APRegister.CuryDiscBal : Edm.Decimal
PX.Objects.CA.Light.APRegister.DiscBal : Edm.Decimal
PX.Objects.CA.Light.APRegister.DocDesc : Edm.String
PX.Objects.CA.Light.APRegister.Released : Edm.Boolean
PX.Objects.CA.Light.APRegister.OpenDoc : Edm.Boolean
PX.Objects.CA.Light.APRegister.Voided : Edm.Boolean
PX.Objects.CA.Light.APRegister.PaymentsByLinesAllowed : Edm.Boolean
PX.Objects.CA.Light.APRegister.Scheduled : Edm.Boolean
PX.Objects.CA.Light.APRegister.ScheduleID : Edm.String
PX.Objects.CA.Light.APRegister.PendingPayment : Edm.Boolean
PX.Objects.CA.Light.APRegister.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.Light.APRegister.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.CA.Light.APRegister.VendorByEmployeeID -> PX.Objects.AP.Vendor
PX.Objects.CA.Light.APRegister.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.CA.Light.APRegister.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.CA.Light.APRegister.BatchByBatchNbr -> PX.Objects.GL.Batch
PX.Objects.CA.Light.APRegister.BatchByPrebookBatchNbr -> PX.Objects.GL.Batch
PX.Objects.CA.Light.APRegister.BatchByVoidBatchNbr -> PX.Objects.GL.Batch
PX.Objects.CA.Light.APRegister.ContactByEmployeeID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.APRegister.APRegisterByRefNbr -> PX.Objects.AP.APRegister (RefNbr=OrigRefNbr)
PX.Objects.CA.Light.APRegister.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CA.Light.APRegister.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.Light.APRegister.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CA.Light.APRegister.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CA.Light.APRegister.EPCompanyTreeByEmployeeWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.CA.Light.APRegister.INRegisterByTaxCostINAdjRefNbr -> PX.Objects.IN.INRegister
PX.Objects.CA.Light.APRegister.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.Light.APRegister.AccountByAPAccountID -> PX.Objects.GL.Account
PX.Objects.CA.Light.APRegister.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.APRegister.AccountByPrepaymentAccountID -> PX.Objects.GL.Account
PX.Objects.CA.Light.APRegister.ScheduleByScheduleID -> PX.Objects.GL.Schedule (ScheduleID=ScheduleID)
PX.Objects.CA.Light.APRegister.SubByAPSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.APRegister.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.APRegister.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.APRegister.LocationByVendorLocationID -> PX.Objects.CR.Location (VendorID=BAccountID, VendorLocationID=LocationID)
PX.Objects.CA.Light.APRegister.LocationByVendorID -> PX.Objects.CR.Location (VendorLocationID=LocationID, VendorID=BAccountID)
PX.Objects.CA.Light.APRegister.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CA.Light.APRegister.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.CA.Light.APRegister.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CA.Light.APRegister.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.CA.Light.APRegister.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.CA.Light.APRegister.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.CA.Light.APRegister.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.CA.Light.APRegister.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CA.Light.APRegister.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CA.Light.APRegister.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.CA.Light.APRegister.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.CA.Light.APRegister.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CA.Light.APRegister.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.CA.Light.APRegister.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.CA.Light.APRegister.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.CA.Light.APRegister.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.CA.Light.APRegister.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.CA.Light.APRegister.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.CA.Light.APRegister.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.CA.Light.APRegister.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.CA.Light.ARAdjust (EntityType)

Key: AdjdDocType, AdjdLineNbr, AdjdRefNbr, AdjgDocType, AdjgRefNbr, AdjNbr
Entity sets: PX_Objects_CA_Light_ARAdjust

PX.Objects.CA.Light.ARAdjust.AdjgDocType : Edm.String [key]
PX.Objects.CA.Light.ARAdjust.AdjgRefNbr : Edm.String [key]
PX.Objects.CA.Light.ARAdjust.AdjdDocType : Edm.String [key]
PX.Objects.CA.Light.ARAdjust.AdjdRefNbr : Edm.String [key]
PX.Objects.CA.Light.ARAdjust.AdjNbr : Edm.Int32 [key]
PX.Objects.CA.Light.ARAdjust.AdjdLineNbr : Edm.Int32 [key]
PX.Objects.CA.Light.ARAdjust.Released : Edm.Boolean
PX.Objects.CA.Light.ARAdjust.Voided : Edm.Boolean
PX.Objects.CA.Light.ARAdjust.ARInvoiceByPPDVATAdjRefNbr -> PX.Objects.AR.ARInvoice
PX.Objects.CA.Light.ARAdjust.ARInvoiceByAdjdRefNbr -> PX.Objects.AR.ARInvoice (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.CA.Light.ARAdjust.BAccountByAdjdCustomerID -> PX.Objects.CR.BAccount
PX.Objects.CA.Light.ARAdjust.BAccountByCustomerID -> PX.Objects.CR.BAccount
PX.Objects.CA.Light.ARAdjust.CustomerByCustomerID -> PX.Objects.AR.Customer
PX.Objects.CA.Light.ARAdjust.CustomerByAdjdCustomerID -> PX.Objects.AR.Customer
PX.Objects.CA.Light.ARAdjust.BatchByAdjBatchNbr -> PX.Objects.GL.Batch
PX.Objects.CA.Light.ARAdjust.ARPaymentByAdjgDocType -> PX.Objects.AR.ARPayment (AdjgRefNbr=RefNbr, AdjgDocType=DocType)
PX.Objects.CA.Light.ARAdjust.ARPaymentByAdjgRefNbr -> PX.Objects.AR.ARPayment (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.CA.Light.ARAdjust.SOOrderByAdjdOrderNbr -> PX.Objects.SO.SOOrder
PX.Objects.CA.Light.ARAdjust.SOOrderByAdjdOrderType -> PX.Objects.SO.SOOrder
PX.Objects.CA.Light.ARAdjust.ARRegisterByAdjgRefNbr -> PX.Objects.AR.ARRegister (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.CA.Light.ARAdjust.ARRegisterByAdjdRefNbr -> PX.Objects.AR.ARRegister (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.CA.Light.ARAdjust.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (AdjdRefNbr=RefNbr, AdjdDocType=DocType)
PX.Objects.CA.Light.ARAdjust.BranchByAdjgBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.Light.ARAdjust.BranchByAdjdBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.Light.ARAdjust.CurrencyInfoByAdjgCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CA.Light.ARAdjust.CurrencyInfoByAdjdCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CA.Light.ARAdjust.CurrencyInfoByAdjdOrigCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CA.Light.ARAdjust.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CA.Light.ARAdjust.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CA.Light.ARAdjust.SOAdjustByAdjgRefNbr -> PX.Objects.SO.SOAdjust (AdjgDocType=AdjgDocType, AdjgRefNbr=AdjgRefNbr)
PX.Objects.CA.Light.ARAdjust.SOOrderTypeByAdjdOrderType -> PX.Objects.SO.SOOrderType
PX.Objects.CA.Light.ARAdjust.ReasonCodeByWriteOffReasonCode -> PX.Objects.CS.ReasonCode
PX.Objects.CA.Light.ARAdjust.AccountByAdjdARAcct -> PX.Objects.GL.Account
PX.Objects.CA.Light.ARAdjust.SubByAdjdARSub -> PX.Objects.GL.Sub
PX.Objects.CA.Light.ARAdjust.ARPaymentTotalsByAdjgRefNbr -> PX.Objects.AR.ARPaymentTotals (AdjgDocType=DocType, AdjgRefNbr=RefNbr)
PX.Objects.CA.Light.ARAdjust.ARTranByAdjdRefNbr -> PX.Objects.AR.ARTran (AdjdLineNbr=LineNbr, AdjdDocType=TranType, AdjdRefNbr=RefNbr)

# PX.Objects.CA.Light.ARInvoice (EntityType)

BaseType: PX.Objects.CA.Light.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.CA.Light.ARRegister)
Entity sets: PX_Objects_CA_Light_ARInvoice
Non-filterable, non-selectable: DrCr

PX.Objects.CA.Light.ARInvoice.TermsID : Edm.String
PX.Objects.CA.Light.ARInvoice.InvoiceNbr : Edm.String
PX.Objects.CA.Light.ARInvoice.PaymentMethodID : Edm.String
PX.Objects.CA.Light.ARInvoice.PMInstanceID : Edm.Int32
PX.Objects.CA.Light.ARInvoice.CashAccountID : Edm.Int32
PX.Objects.CA.Light.ARInvoice.DrCr : Edm.String
PX.Objects.CA.Light.ARInvoice.DiscDate : Edm.DateTimeOffset
PX.Objects.CA.Light.ARInvoice.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.CA.Light.ARInvoice.ContactByOwnerID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.ARInvoice.ARContactByBillContactID -> PX.Objects.AR.ARContact
PX.Objects.CA.Light.ARInvoice.ARContactByShipContactID -> PX.Objects.AR.ARContact
PX.Objects.CA.Light.ARInvoice.ARRegisterByDocType -> PX.Objects.AR.ARRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.CA.Light.ARInvoice.ARAddressByBillAddressID -> PX.Objects.AR.ARAddress
PX.Objects.CA.Light.ARInvoice.ARAddressByShipAddressID -> PX.Objects.AR.ARAddress
PX.Objects.CA.Light.ARInvoice.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.CA.Light.ARInvoice.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone
PX.Objects.CA.Light.ARInvoice.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.CA.Light.ARInvoice.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.Light.ARInvoice.CashAccountByBranchID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.Light.ARInvoice.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.Light.ARInvoice.CustomerPaymentMethodByPaymentMethodID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID, CustomerID=BAccountID, PaymentMethodID=PaymentMethodID)
PX.Objects.CA.Light.ARInvoice.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (CustomerID=BAccountID, PMInstanceID=PMInstanceID)
PX.Objects.CA.Light.ARInvoice.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CA.Light.ARInvoice.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CA.Light.ARInvoice.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CA.Light.ARInvoice.CRRelationCollection -> Collection(PX.Objects.CR.CRRelation)
PX.Objects.CA.Light.ARInvoice.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.CA.Light.ARInvoice.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.CA.Light.ARInvoice.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.Light.ARInvoice.InvoiceSplitCollection -> Collection(PX.Objects.SO.DAC.Projections.InvoiceSplit)
PX.Objects.CA.Light.ARInvoice.PMBillingRecordCollection -> Collection(PX.Objects.PM.PMBillingRecord)
PX.Objects.CA.Light.ARInvoice.CCPayLinkCollection -> Collection(PX.Objects.CC.CCPayLink)
PX.Objects.CA.Light.ARInvoice.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.CA.Light.ARInvoice.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CA.Light.ARInvoice.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.CA.Light.ARInvoice.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.CA.Light.ARInvoice.FSPostDetCollection -> Collection(PX.Objects.FS.FSPostDet)
PX.Objects.CA.Light.ARInvoice.FSPostInfoCollection -> Collection(PX.Objects.FS.FSPostInfo)
PX.Objects.CA.Light.ARInvoice.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.CA.Light.ARInvoice.SVInvoiceCollection -> Collection(PX.Objects.SV.SVInvoice)
PX.Objects.CA.Light.ARInvoice.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.CA.Light.ARInvoice.PMProformaRevisionCollection -> Collection(PX.Objects.PM.PMProformaRevision)
PX.Objects.CA.Light.ARInvoice.ARDunningLetterCollection -> Collection(PX.Objects.AR.ARDunningLetter)
PX.Objects.CA.Light.ARInvoice.SoldInventoryItemCollection -> Collection(PX.Objects.FS.SoldInventoryItem)

# PX.Objects.CA.Light.ARPayment (EntityType)

Label: "AR Document"
BaseType: PX.Objects.AR.ARRegister
Key: DocType, RefNbr (inherited from PX.Objects.AR.ARRegister)
Entity sets: PX_Objects_CA_Light_ARPayment

PX.Objects.CA.Light.ARPayment.ExtRefNbr : Edm.String
PX.Objects.CA.Light.ARPayment.CustomerLocationID : Edm.Int32
PX.Objects.CA.Light.ARPayment.PaymentMethodID : Edm.String
PX.Objects.CA.Light.ARPayment.PMInstanceID : Edm.Int32
PX.Objects.CA.Light.ARPayment.CashAccountID : Edm.Int32
PX.Objects.CA.Light.ARPayment.CATranID : Edm.Int64
PX.Objects.CA.Light.ARPayment.CuryConsolidateChargeTotal : Edm.Decimal
PX.Objects.CA.Light.ARPayment.ConsolidateChargeTotal : Edm.Decimal
PX.Objects.CA.Light.ARPayment.DepositAsBatch : Edm.Boolean
PX.Objects.CA.Light.ARPayment.DepositAfter : Edm.DateTimeOffset
PX.Objects.CA.Light.ARPayment.Deposited : Edm.Boolean
PX.Objects.CA.Light.ARPayment.DepositType : Edm.String
PX.Objects.CA.Light.ARPayment.DepositNbr : Edm.String
PX.Objects.CA.Light.ARPayment.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.CA.Light.ARPayment.PMTaskByProjectID -> PX.Objects.PM.PMTask
PX.Objects.CA.Light.ARPayment.ARRegisterByDocType -> PX.Objects.AR.ARRegister (RefNbr=RefNbr, DocType=DocType)
PX.Objects.CA.Light.ARPayment.CCProcessingCenterTerminalByProcessingCenterID -> PX.Objects.CC.CCProcessingCenterTerminal
PX.Objects.CA.Light.ARPayment.CADepositByDepositType -> PX.Objects.CA.CADeposit (DepositNbr=RefNbr, DepositType=TranType)
PX.Objects.CA.Light.ARPayment.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.Light.ARPayment.CashAccountByBranchID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.Light.ARPayment.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter
PX.Objects.CA.Light.ARPayment.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.Light.ARPayment.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.CA.Light.ARPayment.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CA.Light.ARPayment.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.CA.Light.ARPayment.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.Light.ARPayment.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CA.Light.ARPayment.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.Objects.CA.Light.ARPayment.FSAdjustCollection -> Collection(PX.Objects.FS.FSAdjust)
PX.Objects.CA.Light.ARPayment.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)

# PX.Objects.CA.Light.ARRegister (EntityType)

Key: DocType, RefNbr
Entity sets: PX_Objects_CA_Light_ARRegister
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CA.Light.ARRegister.BranchID : Edm.Int32
PX.Objects.CA.Light.ARRegister.DocType : Edm.String [key]
PX.Objects.CA.Light.ARRegister.RefNbr : Edm.String [key]
PX.Objects.CA.Light.ARRegister.DocDate : Edm.DateTimeOffset
PX.Objects.CA.Light.ARRegister.DueDate : Edm.DateTimeOffset
PX.Objects.CA.Light.ARRegister.FinPeriodID : Edm.String
PX.Objects.CA.Light.ARRegister.CustomerID : Edm.Int32
PX.Objects.CA.Light.ARRegister.CustomerLocationID : Edm.Int32
PX.Objects.CA.Light.ARRegister.CuryID : Edm.String
PX.Objects.CA.Light.ARRegister.CuryInfoID : Edm.Int64
PX.Objects.CA.Light.ARRegister.CuryDocBal : Edm.Decimal
PX.Objects.CA.Light.ARRegister.DocBal : Edm.Decimal
PX.Objects.CA.Light.ARRegister.CuryDiscBal : Edm.Decimal
PX.Objects.CA.Light.ARRegister.DiscBal : Edm.Decimal
PX.Objects.CA.Light.ARRegister.DocDesc : Edm.String
PX.Objects.CA.Light.ARRegister.Released : Edm.Boolean
PX.Objects.CA.Light.ARRegister.OpenDoc : Edm.Boolean
PX.Objects.CA.Light.ARRegister.Voided : Edm.Boolean
PX.Objects.CA.Light.ARRegister.PaymentsByLinesAllowed : Edm.Boolean
PX.Objects.CA.Light.ARRegister.Scheduled : Edm.Boolean
PX.Objects.CA.Light.ARRegister.ScheduleID : Edm.String
PX.Objects.CA.Light.ARRegister.PendingPayment : Edm.Boolean
PX.Objects.CA.Light.ARRegister.CuryOrigDocAmt : Edm.Decimal
PX.Objects.CA.Light.ARRegister.OrigDocAmt : Edm.Decimal
PX.Objects.CA.Light.ARRegister.CuryChargeAmt : Edm.Decimal
PX.Objects.CA.Light.ARRegister.ChargeAmt : Edm.Decimal
PX.Objects.CA.Light.ARRegister.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.Light.ARRegister.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.CA.Light.ARRegister.CustomerByCustomerID -> PX.Objects.AR.Customer (CustomerID=BAccountID)
PX.Objects.CA.Light.ARRegister.BatchByBatchNbr -> PX.Objects.GL.Batch
PX.Objects.CA.Light.ARRegister.ContactByApproverID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.ARRegister.ARRegisterByRefNbr -> PX.Objects.AR.ARRegister (RefNbr=OrigRefNbr)
PX.Objects.CA.Light.ARRegister.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CA.Light.ARRegister.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CA.Light.ARRegister.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CA.Light.ARRegister.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CA.Light.ARRegister.EPCompanyTreeByApproverWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.CA.Light.ARRegister.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.Light.ARRegister.AccountByARAccountID -> PX.Objects.GL.Account
PX.Objects.CA.Light.ARRegister.AccountByRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.ARRegister.AccountByPrepaymentAccountID -> PX.Objects.GL.Account
PX.Objects.CA.Light.ARRegister.ScheduleByScheduleID -> PX.Objects.GL.Schedule (ScheduleID=ScheduleID)
PX.Objects.CA.Light.ARRegister.SubByARSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.ARRegister.SubByRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.ARRegister.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.ARRegister.LocationByCustomerLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID, CustomerLocationID=LocationID)
PX.Objects.CA.Light.ARRegister.LocationByCustomerID -> PX.Objects.CR.Location (CustomerLocationID=LocationID, CustomerID=BAccountID)
PX.Objects.CA.Light.ARRegister.SalesPersonBySalesPersonID -> PX.Objects.AR.SalesPerson
PX.Objects.CA.Light.ARRegister.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.CA.Light.ARRegister.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CA.Light.ARRegister.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.CA.Light.ARRegister.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.CA.Light.ARRegister.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.CA.Light.ARRegister.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.CA.Light.ARRegister.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.CA.Light.ARRegister.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.CA.Light.ARRegister.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CA.Light.ARRegister.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CA.Light.ARRegister.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.CA.Light.ARRegister.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.CA.Light.ARRegister.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CA.Light.ARRegister.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.CA.Light.ARRegister.CCBatchTransactionCollection -> Collection(PX.Objects.CA.CCBatchTransaction)
PX.Objects.CA.Light.ARRegister.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.CA.Light.ARRegister.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.CA.Light.ARRegister.ARPaymentTotalsCollection -> Collection(PX.Objects.AR.ARPaymentTotals)
PX.Objects.CA.Light.ARRegister.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CA.Light.ARRegister.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)
PX.Objects.CA.Light.ARRegister.ARTranAccrueCostCollection -> Collection(PX.Objects.AR.ARTranAccrueCost)

# PX.Objects.CA.Light.BAccount (EntityType)

Key: AcctCD
Entity sets: PX_Objects_CA_Light_BAccount
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CA.Light.BAccount.BAccountID : Edm.Int32
PX.Objects.CA.Light.BAccount.AcctName : Edm.String
PX.Objects.CA.Light.BAccount.CuryID : Edm.String
PX.Objects.CA.Light.BAccount.ConsolidatingBAccountID : Edm.Int32
PX.Objects.CA.Light.BAccount.AcctCD : Edm.String [key]
PX.Objects.CA.Light.BAccount.Status : Edm.String
PX.Objects.CA.Light.BAccount.VStatus : Edm.String
PX.Objects.CA.Light.BAccount.NoteID : Edm.Guid
PX.Objects.CA.Light.BAccount.VOrgBAccountID : Edm.Int32
PX.Objects.CA.Light.BAccount.COrgBAccountID : Edm.Int32
PX.Objects.CA.Light.BAccount.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.Light.BAccount.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CA.Light.BAccount.CustomerCollection -> Collection(PX.Objects.CA.Light.Customer)

# PX.Objects.CA.Light.CABankTranAdjustment (EntityType)

Key: AdjNbr, TranID
Entity sets: PX_Objects_CA_Light_CABankTranAdjustment

PX.Objects.CA.Light.CABankTranAdjustment.TranID : Edm.Int32 [key]
PX.Objects.CA.Light.CABankTranAdjustment.AdjdModule : Edm.String
PX.Objects.CA.Light.CABankTranAdjustment.AdjdDocType : Edm.String
PX.Objects.CA.Light.CABankTranAdjustment.AdjdRefNbr : Edm.String
PX.Objects.CA.Light.CABankTranAdjustment.AdjNbr : Edm.Int32 [key]
PX.Objects.CA.Light.CABankTranAdjustment.Released : Edm.Boolean
PX.Objects.CA.Light.CABankTranAdjustment.Voided : Edm.Boolean
PX.Objects.CA.Light.CABankTranAdjustment.APInvoiceByAdjdRefNbr -> PX.Objects.AP.APInvoice (AdjdDocType=DocType, AdjdRefNbr=RefNbr)
PX.Objects.CA.Light.CABankTranAdjustment.BatchByAdjBatchNbr -> PX.Objects.GL.Batch (AdjdModule=Module)
PX.Objects.CA.Light.CABankTranAdjustment.BranchByAdjdBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.Light.CABankTranAdjustment.CurrencyInfoByAdjdCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CA.Light.CABankTranAdjustment.CurrencyInfoByAdjdOrigCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CA.Light.CABankTranAdjustment.CurrencyInfoByAdjgCuryInfoID -> PX.Objects.CM.CurrencyInfo
PX.Objects.CA.Light.CABankTranAdjustment.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CA.Light.CABankTranAdjustment.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CA.Light.CABankTranAdjustment.ReasonCodeByWriteOffReasonCode -> PX.Objects.CS.ReasonCode
PX.Objects.CA.Light.CABankTranAdjustment.AccountByAdjdAPAcct -> PX.Objects.GL.Account
PX.Objects.CA.Light.CABankTranAdjustment.AccountByAdjdARAcct -> PX.Objects.GL.Account
PX.Objects.CA.Light.CABankTranAdjustment.AccountByAdjdWhTaxAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.CABankTranAdjustment.SubByAdjdAPSub -> PX.Objects.GL.Sub
PX.Objects.CA.Light.CABankTranAdjustment.SubByAdjdARSub -> PX.Objects.GL.Sub
PX.Objects.CA.Light.CABankTranAdjustment.SubByAdjdWhTaxSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.CABankTranAdjustment.CABankTranByTranID -> PX.Objects.CA.CABankTran (TranID=TranID)

# PX.Objects.CA.Light.Customer (EntityType)

Label: "Customer"
BaseType: PX.Objects.CA.Light.BAccount
Key: AcctCD (inherited from PX.Objects.CA.Light.BAccount)
Entity sets: PX_Objects_CA_Light_Customer, Customer2

PX.Objects.CA.Light.Customer.CustomerClassID : Edm.String
PX.Objects.CA.Light.Customer.StatementCycleId : Edm.String
PX.Objects.CA.Light.Customer.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CA.Light.Customer.BAccountByAcctCD -> PX.Objects.CA.Light.BAccount (AcctCD=AcctCD)

# PX.Objects.CA.Light.CustomerMaster (EntityType)

Label: "Customer"
BaseType: PX.Objects.CA.Light.Customer
Key: AcctCD (inherited from PX.Objects.CA.Light.BAccount)
Entity sets: PX_Objects_CA_Light_CustomerMaster

PX.Objects.CA.Light.CustomerMaster.BAccountByParentBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CA.Light.CustomerMaster.ContactByBaseBillContactID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.CustomerMaster.ARStatementCycleByStatementCycleId -> PX.Objects.AR.ARStatementCycle (StatementCycleId=StatementCycleId)
PX.Objects.CA.Light.CustomerMaster.CustomerClassByCustomerClassID -> PX.Objects.AR.CustomerClass (CustomerClassID=CustomerClassID)
PX.Objects.CA.Light.CustomerMaster.CustomerMasterByParentBAccountID -> PX.Objects.AR.CustomerMaster
PX.Objects.CA.Light.CustomerMaster.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)

# PX.Objects.CA.Light.Location (EntityType)

Label: "Location"
Key: BAccountID, LocationCD
Entity sets: PX_Objects_CA_Light_Location, Location2

PX.Objects.CA.Light.Location.BAccountID : Edm.Int32 [key]
PX.Objects.CA.Light.Location.LocationID : Edm.Int32
PX.Objects.CA.Light.Location.LocationCD : Edm.String [key] "Location ID"
PX.Objects.CA.Light.Location.Descr : Edm.String "Location Name"
PX.Objects.CA.Light.Location.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CA.Light.Location.ContactByDefContactID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.Location.ContactByVRemitContactID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.Location.AddressByDefAddressID -> PX.Objects.CR.Address
PX.Objects.CA.Light.Location.AddressByVRemitAddressID -> PX.Objects.CR.Address
PX.Objects.CA.Light.Location.BranchByCBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.Light.Location.BranchByVBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.Light.Location.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CA.Light.Location.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CA.Light.Location.TaxZoneByCTaxZoneID -> PX.Objects.TX.TaxZone
PX.Objects.CA.Light.Location.TaxZoneByVTaxZoneID -> PX.Objects.TX.TaxZone
PX.Objects.CA.Light.Location.CarrierByCCarrierID -> PX.Objects.CS.Carrier
PX.Objects.CA.Light.Location.CarrierByVCarrierID -> PX.Objects.CS.Carrier
PX.Objects.CA.Light.Location.FOBPointByCFOBPointID -> PX.Objects.CS.FOBPoint
PX.Objects.CA.Light.Location.FOBPointByVFOBPointID -> PX.Objects.CS.FOBPoint
PX.Objects.CA.Light.Location.ShippingZoneByCShipZoneID -> PX.Objects.CS.ShippingZone
PX.Objects.CA.Light.Location.ShipTermsByCShipTermsID -> PX.Objects.CS.ShipTerms
PX.Objects.CA.Light.Location.ShipTermsByVShipTermsID -> PX.Objects.CS.ShipTerms
PX.Objects.CA.Light.Location.INSiteByCSiteID -> PX.Objects.IN.INSite
PX.Objects.CA.Light.Location.INSiteByVSiteID -> PX.Objects.IN.INSite
PX.Objects.CA.Light.Location.INSiteByCMPSiteID -> PX.Objects.IN.INSite
PX.Objects.CA.Light.Location.AccountByCSalesAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByCDiscountAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByCRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByCFreightAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByCARAccountID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByVExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByVRetainageAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByVFreightAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByVDiscountAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.AccountByVAPAccountID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Location.SubByCSalesSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCFreightSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCARSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByVExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByVRetainageSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByVFreightSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByVDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByVAPSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCMPSalesSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCMPExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCMPFreightSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCMPDiscountSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.SubByCMPGainLossSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Location.CashAccountByVBranchID -> PX.Objects.CA.CashAccount
PX.Objects.CA.Light.Location.PaymentMethodByVPaymentMethodID -> PX.Objects.CA.PaymentMethod
PX.Objects.CA.Light.Location.ARPriceClassByCPriceClassID -> PX.Objects.AR.ARPriceClass
PX.Objects.CA.Light.Location.CSCalendarByCCalendarID -> PX.Objects.CS.CSCalendar
PX.Objects.CA.Light.Location.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CA.Light.Location.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.CA.Light.Location.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CA.Light.Location.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CA.Light.Location.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CA.Light.Location.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CA.Light.Location.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CA.Light.Location.FSAppointmentInRouteCollection -> Collection(PX.Objects.FS.FSAppointmentInRoute)
PX.Objects.CA.Light.Location.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CA.Light.Location.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.CA.Light.Location.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.CA.Light.Location.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CA.Light.Location.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CA.Light.Location.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.CA.Light.Location.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.CA.Light.Location.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CA.Light.Location.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.CA.Light.Location.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CA.Light.Location.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CA.Light.Location.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.CA.Light.Location.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.Objects.CA.Light.Location.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CA.Light.Location.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.CA.Light.Location.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CA.Light.Location.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CA.Light.Location.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CA.Light.Location.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CA.Light.Location.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.CA.Light.Location.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.CA.Light.Location.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CA.Light.Location.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.CA.Light.Location.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.CA.Light.Location.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CA.Light.Location.AppointmentToPostCollection -> Collection(PX.Objects.FS.AppointmentToPost)
PX.Objects.CA.Light.Location.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.CA.Light.Location.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.CA.Light.Location.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.CA.Light.Location.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.CA.Light.Location.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CA.Light.Location.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.Objects.CA.Light.Location.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.CA.Light.Location.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.CA.Light.Location.VendorPaymentMethodDetailCollection -> Collection(PX.Objects.AP.VendorPaymentMethodDetail)
PX.Objects.CA.Light.Location.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.CA.Light.Location.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.Light.Location.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.CA.Light.Location.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.CA.Light.Location.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.CA.Light.Location.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CA.Light.Location.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)
PX.Objects.CA.Light.Location.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.Objects.CA.Light.Location.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.CA.Light.Location.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.CA.Light.Location.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CA.Light.Location.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CA.Light.Location.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CA.Light.Location.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CA.Light.Location.PMUnionCollection -> Collection(PX.Objects.PM.PMUnion)
PX.Objects.CA.Light.Location.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.CA.Light.Location.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.CA.Light.Location.CarrierPluginCustomerCollection -> Collection(PX.Objects.CS.CarrierPluginCustomer)
PX.Objects.CA.Light.Location.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.CA.Light.Location.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.CA.Light.Location.LocationBranchSettingsCollection -> Collection(PX.Objects.CR.LocationBranchSettings)
PX.Objects.CA.Light.Location.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CA.Light.Location.APDiscountLocationCollection -> Collection(PX.Objects.AP.APDiscountLocation)
PX.Objects.CA.Light.Location.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.Objects.CA.Light.Location.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.CA.Light.Location.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.Objects.CA.Light.Location.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.CA.Light.Location.AMForecastStagingCollection -> Collection(PX.Objects.AM.AMForecastStaging)
PX.Objects.CA.Light.Location.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CA.Light.Location.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.CA.Light.Location.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CA.Light.Location.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.CA.Light.Location.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.CA.Light.Location.SVServiceLocationCustomerCollection -> Collection(PX.Objects.SV.SVServiceLocationCustomer)
PX.Objects.CA.Light.Location.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CA.Light.Location.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CA.Light.Location.BCRoleAssignmentCollection -> Collection(PX.Commerce.Shopify.BCRoleAssignment)
PX.Objects.CA.Light.Location.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.CA.Light.Location.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.CA.Light.Location.BAccountLocationCollection -> Collection(PX.Objects.FS.BAccountLocation)
PX.Objects.CA.Light.Location.ARSPCommnHistoryCollection -> Collection(PX.Objects.AR.ARSPCommnHistory)
PX.Objects.CA.Light.Location.ContractPostBatchDetailCollection -> Collection(PX.Objects.FS.ContractPostBatchDetail)
PX.Objects.CA.Light.Location.ContractPeriodToPostCollection -> Collection(PX.Objects.FS.ContractPeriodToPost)
PX.Objects.CA.Light.Location.FSRouteAppointmentForecastingCollection -> Collection(PX.Objects.FS.FSRouteAppointmentForecasting)
PX.Objects.CA.Light.Location.AMBomOperCuryCollection -> Collection(PX.Objects.AM.AMBomOperCury)
PX.Objects.CA.Light.Location.ARBalancesCollection -> Collection(PX.Objects.AR.ARBalances)

# PX.Objects.CA.Light.Vendor (EntityType)

Label: "Customer"
BaseType: PX.Objects.CA.Light.BAccount
Key: AcctCD (inherited from PX.Objects.CA.Light.BAccount)
Entity sets: PX_Objects_CA_Light_Vendor, Customer3, Vendor2

PX.Objects.CA.Light.Vendor.VendorClassID : Edm.String
PX.Objects.CA.Light.Vendor.VendorByPayToVendorID -> PX.Objects.AP.Vendor
PX.Objects.CA.Light.Vendor.BAccountByCOrgBAccountID -> PX.Objects.CR.BAccount (COrgBAccountID=BAccountID)
PX.Objects.CA.Light.Vendor.BAccountByVOrgBAccountID -> PX.Objects.CR.BAccount (VOrgBAccountID=BAccountID)
PX.Objects.CA.Light.Vendor.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CA.Light.Vendor.BAccountByPayToVendorID -> PX.Objects.CR.BAccount
PX.Objects.CA.Light.Vendor.ContactByDefContactID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.Vendor.ContactByBaseRemitContactID -> PX.Objects.CR.Contact
PX.Objects.CA.Light.Vendor.ContactByBAccountID -> PX.Objects.CR.Contact (BAccountID=BAccountID)
PX.Objects.CA.Light.Vendor.EPEmployeeClassByVendorClassID -> PX.Objects.EP.EPEmployeeClass (VendorClassID=VendorClassID)
PX.Objects.CA.Light.Vendor.AddressByDefPOAddressID -> PX.Objects.CR.Address
PX.Objects.CA.Light.Vendor.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CA.Light.Vendor.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CA.Light.Vendor.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree
PX.Objects.CA.Light.Vendor.NumberingBySVATTaxInvoiceNumberingID -> PX.Objects.CS.Numbering
PX.Objects.CA.Light.Vendor.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CA.Light.Vendor.TermsByTermsID -> PX.Objects.CS.Terms
PX.Objects.CA.Light.Vendor.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CA.Light.Vendor.CurrencyByPriceListCuryID -> PX.Objects.CM.Currency
PX.Objects.CA.Light.Vendor.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList
PX.Objects.CA.Light.Vendor.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.CA.Light.Vendor.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType
PX.Objects.CA.Light.Vendor.AccountByPrepaymentAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Vendor.AccountByDiscTakenAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Vendor.AccountByPOAccrualAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Vendor.AccountByPrebookAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Vendor.AccountBySalesTaxAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Vendor.AccountByPurchTaxAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Vendor.AccountByTaxExpenseAcctID -> PX.Objects.GL.Account
PX.Objects.CA.Light.Vendor.SubByPrepaymentSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Vendor.SubByDiscTakenSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Vendor.SubByPOAccrualSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Vendor.SubByPrebookSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Vendor.SubBySalesTaxSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Vendor.SubByPurchTaxSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Vendor.SubByTaxExpenseSubID -> PX.Objects.GL.Sub
PX.Objects.CA.Light.Vendor.LocationByDefLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.CA.Light.Vendor.LocationByBAccountID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.CA.Light.Vendor.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign
PX.Objects.CA.Light.Vendor.VendorClassByVendorClassID -> PX.Objects.AP.VendorClass (VendorClassID=VendorClassID)
PX.Objects.CA.Light.Vendor.AP1099BoxByBox1099 -> PX.Objects.AP.AP1099Box
PX.Objects.CA.Light.Vendor.LocaleByLocaleName -> PX.SM.Locale
PX.Objects.CA.Light.Vendor.BAccountByAcctCD -> PX.Objects.CA.Light.BAccount (AcctCD=AcctCD)
PX.Objects.CA.Light.Vendor.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.Objects.CA.Light.Vendor.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CA.Light.Vendor.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.CA.Light.Vendor.PRDeductionDetailCollection -> Collection(PX.Objects.PR.PRDeductionDetail)
PX.Objects.CA.Light.Vendor.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.CA.Light.Vendor.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.CA.Light.Vendor.PRBatchEmployeeCollection -> Collection(PX.Objects.PR.PRBatchEmployee)
PX.Objects.CA.Light.Vendor.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.CA.Light.Vendor.PRAcaEmployeeMonthlyInformationCollection -> Collection(PX.Objects.PR.PRAcaEmployeeMonthlyInformation)
PX.Objects.CA.Light.Vendor.PREmployeeAttributeCollection -> Collection(PX.Objects.PR.PREmployeeAttribute)
PX.Objects.CA.Light.Vendor.PREmployeeDeductCollection -> Collection(PX.Objects.PR.PREmployeeDeduct)
PX.Objects.CA.Light.Vendor.PREmployeeDirectDepositCollection -> Collection(PX.Objects.PR.PREmployeeDirectDeposit)
PX.Objects.CA.Light.Vendor.PREmployeeEarningCollection -> Collection(PX.Objects.PR.PREmployeeEarning)
PX.Objects.CA.Light.Vendor.PREmployeePTOBankCollection -> Collection(PX.Objects.PR.PREmployeePTOBank)
PX.Objects.CA.Light.Vendor.PREmployeeTaxCollection -> Collection(PX.Objects.PR.PREmployeeTax)
PX.Objects.CA.Light.Vendor.PREmployeeTaxAttributeCollection -> Collection(PX.Objects.PR.PREmployeeTaxAttribute)
PX.Objects.CA.Light.Vendor.PREmployeeTaxFormCollection -> Collection(PX.Objects.PR.PREmployeeTaxForm)
PX.Objects.CA.Light.Vendor.PREmployeeTaxFormDataCollection -> Collection(PX.Objects.PR.PREmployeeTaxFormData)
PX.Objects.CA.Light.Vendor.PREmployeeWorkLocationCollection -> Collection(PX.Objects.PR.PREmployeeWorkLocation)
PX.Objects.CA.Light.Vendor.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.CA.Light.Vendor.PRPaymentBatchExportDetailsCollection -> Collection(PX.Objects.PR.PRPaymentBatchExportDetails)
PX.Objects.CA.Light.Vendor.PRPTOAdjustmentDetailCollection -> Collection(PX.Objects.PR.PRPTOAdjustmentDetail)
PX.Objects.CA.Light.Vendor.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.CA.Light.Vendor.PRRecordOfEmploymentCollection -> Collection(PX.Objects.PR.PRRecordOfEmployment)
PX.Objects.CA.Light.Vendor.PRPeriodTaxApplicableAmountsCollection -> Collection(PX.Objects.PR.PRPeriodTaxApplicableAmounts)
PX.Objects.CA.Light.Vendor.PRPeriodTaxesCollection -> Collection(PX.Objects.PR.PRPeriodTaxes)
PX.Objects.CA.Light.Vendor.PRYtdDeductionsCollection -> Collection(PX.Objects.PR.PRYtdDeductions)
PX.Objects.CA.Light.Vendor.PRYtdEarningsCollection -> Collection(PX.Objects.PR.PRYtdEarnings)
PX.Objects.CA.Light.Vendor.PRYtdTaxesCollection -> Collection(PX.Objects.PR.PRYtdTaxes)
PX.Objects.CA.Light.Vendor.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.CA.Light.Vendor.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.CA.Light.Vendor.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.CA.Light.Vendor.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.CA.Light.Vendor.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.CA.Light.Vendor.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CA.Light.Vendor.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.CA.Light.Vendor.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CA.Light.Vendor.EPTimeCardCollection -> Collection(PX.Objects.EP.EPTimeCard)
PX.Objects.CA.Light.Vendor.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.CA.Light.Vendor.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CA.Light.Vendor.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.CA.Light.Vendor.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.CA.Light.Vendor.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.CA.Light.Vendor.FSLicenseCollection -> Collection(PX.Objects.SV.FSLicense)
PX.Objects.CA.Light.Vendor.FSEmployeeSkillCollection -> Collection(PX.Objects.SV.FSEmployeeSkill)
PX.Objects.CA.Light.Vendor.EPWingmanCollection -> Collection(PX.Objects.EP.EPWingman)
PX.Objects.CA.Light.Vendor.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.Objects.CA.Light.Vendor.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)
PX.Objects.CA.Light.Vendor.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CA.Light.Vendor.CABankFeedCorpCardCollection -> Collection(PX.Objects.CA.CABankFeedCorpCard)
PX.Objects.CA.Light.Vendor.EPEmployeeClassLaborMatrixCollection -> Collection(PX.Objects.EP.EPEmployeeClassLaborMatrix)
PX.Objects.CA.Light.Vendor.EPEmployeeContractCollection -> Collection(PX.Objects.EP.EPEmployeeContract)
PX.Objects.CA.Light.Vendor.EPEmployeePositionCollection -> Collection(PX.Objects.EP.EPEmployeePosition)
PX.Objects.CA.Light.Vendor.EPTimeActivitiesSummaryCollection -> Collection(PX.Objects.EP.EPTimeActivitiesSummary)
PX.Objects.CA.Light.Vendor.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.CA.Light.Vendor.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.CA.Light.Vendor.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.CA.Light.Vendor.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.CA.Light.Vendor.AMSFKRecentActivityCollection -> Collection(PX.Objects.AM.SFK.AMSFKRecentActivity)
PX.Objects.CA.Light.Vendor.FSGeoZoneEmpCollection -> Collection(PX.Objects.FS.FSGeoZoneEmp)
PX.Objects.CA.Light.Vendor.FSRouteDocumentCollection -> Collection(PX.Objects.FS.FSRouteDocument)
PX.Objects.CA.Light.Vendor.FSRouteEmployeeCollection -> Collection(PX.Objects.FS.FSRouteEmployee)
PX.Objects.CA.Light.Vendor.SVMyDayReportCollection -> Collection(PX.Objects.SV.SVMyDayReport)
PX.Objects.CA.Light.Vendor.SVTicketDetailCollection -> Collection(PX.Objects.SV.SVTicketDetail)
PX.Objects.CA.Light.Vendor.EMailSyncAccountPreferencesCollection -> Collection(PX.SM.EMailSyncAccountPreferences)
PX.Objects.CA.Light.Vendor.EPEmployeeCorpCardLinkCollection -> Collection(PX.Objects.EP.DAC.EPEmployeeCorpCardLink)
PX.Objects.CA.Light.Vendor.AMTranCostCollection -> Collection(PX.Objects.AM.AMTranCost)
PX.Objects.CA.Light.Vendor.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CA.Light.Vendor.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CA.Light.Vendor.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CA.Light.Vendor.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.CA.Light.Vendor.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.Objects.CA.Light.Vendor.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.CA.Light.Vendor.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.CA.Light.Vendor.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CA.Light.Vendor.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.CA.Light.Vendor.ARContactCollection -> Collection(PX.Objects.AR.ARContact)
PX.Objects.CA.Light.Vendor.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CA.Light.Vendor.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.CA.Light.Vendor.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.CA.Light.Vendor.FSEquipmentCollection -> Collection(PX.Objects.FS.FSEquipment)
PX.Objects.CA.Light.Vendor.DailyFieldReportSubcontractorActivityCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportSubcontractorActivity)
PX.Objects.CA.Light.Vendor.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.CA.Light.Vendor.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.CA.Light.Vendor.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.CA.Light.Vendor.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.CA.Light.Vendor.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.CA.Light.Vendor.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.CA.Light.Vendor.APDiscountCollection -> Collection(PX.Objects.AP.APDiscount)
PX.Objects.CA.Light.Vendor.AP1099HistoryCollection -> Collection(PX.Objects.AP.AP1099History)
PX.Objects.CA.Light.Vendor.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.CA.Light.Vendor.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.CA.Light.Vendor.TaxYearCollection -> Collection(PX.Objects.TX.TaxYear)
PX.Objects.CA.Light.Vendor.TaxPeriodCollection -> Collection(PX.Objects.TX.TaxPeriod)
PX.Objects.CA.Light.Vendor.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.CA.Light.Vendor.TaxBucketCollection -> Collection(PX.Objects.TX.TaxBucket)
PX.Objects.CA.Light.Vendor.TaxBucketLineCollection -> Collection(PX.Objects.TX.TaxBucketLine)
PX.Objects.CA.Light.Vendor.TaxReportCollection -> Collection(PX.Objects.TX.TaxReport)
PX.Objects.CA.Light.Vendor.TaxReportLineCollection -> Collection(PX.Objects.TX.TaxReportLine)
PX.Objects.CA.Light.Vendor.TaxRevCollection -> Collection(PX.Objects.TX.TaxRev)
PX.Objects.CA.Light.Vendor.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)
PX.Objects.CA.Light.Vendor.SOLineSplitCollection -> Collection(PX.Objects.SO.SOLineSplit)
PX.Objects.CA.Light.Vendor.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.CA.Light.Vendor.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.CA.Light.Vendor.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.CA.Light.Vendor.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.CA.Light.Vendor.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CA.Light.Vendor.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CA.Light.Vendor.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CA.Light.Vendor.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.CA.Light.Vendor.PMUnionCollection -> Collection(PX.Objects.PM.PMUnion)
PX.Objects.CA.Light.Vendor.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.CA.Light.Vendor.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.CA.Light.Vendor.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.CA.Light.Vendor.INReplenishmentOrderCollection -> Collection(PX.Objects.IN.INReplenishmentOrder)
PX.Objects.CA.Light.Vendor.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.CA.Light.Vendor.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.CA.Light.Vendor.APAddressCollection -> Collection(PX.Objects.AP.APAddress)
PX.Objects.CA.Light.Vendor.APContactCollection -> Collection(PX.Objects.AP.APContact)
PX.Objects.CA.Light.Vendor.APDiscountLocationCollection -> Collection(PX.Objects.AP.APDiscountLocation)
PX.Objects.CA.Light.Vendor.APDiscountVendorCollection -> Collection(PX.Objects.AP.APDiscountVendor)
PX.Objects.CA.Light.Vendor.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.CA.Light.Vendor.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.CA.Light.Vendor.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.CA.Light.Vendor.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.CA.Light.Vendor.FSApptLineSplitCollection -> Collection(PX.Objects.FS.FSApptLineSplit)
PX.Objects.CA.Light.Vendor.FSEquipmentComponentCollection -> Collection(PX.Objects.FS.FSEquipmentComponent)
PX.Objects.CA.Light.Vendor.FSModelComponentCollection -> Collection(PX.Objects.FS.FSModelComponent)
PX.Objects.CA.Light.Vendor.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.CA.Light.Vendor.FSSODetSplitCollection -> Collection(PX.Objects.FS.FSSODetSplit)
PX.Objects.CA.Light.Vendor.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.CA.Light.Vendor.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.CA.Light.Vendor.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.CA.Light.Vendor.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.CA.Light.Vendor.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.CA.Light.Vendor.TaxHistorySumCollection -> Collection(PX.Objects.TX.TaxHistorySum)
PX.Objects.CA.Light.Vendor.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.CA.Light.Vendor.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.CA.Light.Vendor.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.CA.Light.Vendor.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.CA.Light.Vendor.FSSiteStatusSelectedCollection -> Collection(PX.Objects.FS.FSSiteStatusSelected)
PX.Objects.CA.Light.Vendor.SVVendorLicenseCollection -> Collection(PX.Objects.SV.SVVendorLicense)
PX.Objects.CA.Light.Vendor.SVVendorSkillCollection -> Collection(PX.Objects.SV.SVVendorSkill)
PX.Objects.CA.Light.Vendor.CISHistoryCollection -> Collection(PX.Objects.Localizations.GB.CISHistory)
PX.Objects.CA.Light.Vendor.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.CA.Light.Vendor.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)

# PX.Objects.CA.PaymentMethod (EntityType)

Label: "Payment Method"
Key: PaymentMethodID
Entity sets: PX_Objects_CA_PaymentMethod, PaymentMethod
Non-filterable, non-selectable: NoteText, IsAccountNumberRequired, PrintOrExport, HasProcessingCenters, IsUsingPlugin, ExternalPaymentProcessorType, NeedAccountFilter, DeletedDatabaseRecord

PX.Objects.CA.PaymentMethod.PaymentMethodID : Edm.String [key] "Payment Method ID"
PX.Objects.CA.PaymentMethod.PMInstanceID : Edm.Int32
PX.Objects.CA.PaymentMethod.Descr : Edm.String "Description"
PX.Objects.CA.PaymentMethod.PaymentType : Edm.String "Means of Payment"
PX.Objects.CA.PaymentMethod.DirectDepositFileFormat : Edm.String "Direct Deposit File Format"
PX.Objects.CA.PaymentMethod.DefaultCashAccountID : Edm.Int32
PX.Objects.CA.PaymentMethod.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CA.PaymentMethod.UseForAR : Edm.Boolean [required] "Use in AR"
PX.Objects.CA.PaymentMethod.UseForAP : Edm.Boolean [required] "Use in AP"
PX.Objects.CA.PaymentMethod.UseForCA : Edm.Boolean [required] "Require Remittance Information for Cash Account"
PX.Objects.CA.PaymentMethod.APAdditionalProcessing : Edm.String "Additional Processing"
PX.Objects.CA.PaymentMethod.SkipExport : Edm.Boolean [required] "Release Batch Payment Before Export"
PX.Objects.CA.PaymentMethod.APCreateBatchPayment : Edm.Boolean [required] "Create Batch Payment"
PX.Objects.CA.PaymentMethod.APBatchExportMethod : Edm.String "Export Method"
PX.Objects.CA.PaymentMethod.APBatchExportSYMappingID : Edm.Guid "Export Scenario"
PX.Objects.CA.PaymentMethod.APBatchExportPlugInTypeName : Edm.String "Export Plug-In (Type)"
PX.Objects.CA.PaymentMethod.SkipPaymentsWithZeroAmt : Edm.Boolean [required] "Skip Payments with Zero Amount"
PX.Objects.CA.PaymentMethod.RequireBatchSeqNum : Edm.Boolean [required] "Require Batch Seq. Number"
PX.Objects.CA.PaymentMethod.APPrintChecks : Edm.Boolean [required] "Print Checks"
PX.Objects.CA.PaymentMethod.APCheckReportID : Edm.String "Report"
PX.Objects.CA.PaymentMethod.APStubLines : Edm.Int16 [required] "Lines per Stub"
PX.Objects.CA.PaymentMethod.APPrintRemittance : Edm.Boolean [required] "Print Remittance Report"
PX.Objects.CA.PaymentMethod.APRemittanceReportID : Edm.String "Remittance Report"
PX.Objects.CA.PaymentMethod.APRequirePaymentRef : Edm.Boolean [required] "Require Unique Payment Ref."
PX.Objects.CA.PaymentMethod.ARIsProcessingRequired : Edm.Boolean [required] "Integrated Processing"
PX.Objects.CA.PaymentMethod.ARIsOnePerCustomer : Edm.Boolean [required] "One Instance Per Customer"
PX.Objects.CA.PaymentMethod.ARDepositAsBatch : Edm.Boolean [required] "Batch Deposit"
PX.Objects.CA.PaymentMethod.ARVoidOnDepositAccount : Edm.Boolean [required] "Void Using Clearing Account"
PX.Objects.CA.PaymentMethod.ARDefaultVoidDateToDocumentDate : Edm.Boolean [required] "Use Document Date as Void Date"
PX.Objects.CA.PaymentMethod.ARHasBillingInfo : Edm.Boolean [required] "Has Billing Information"
PX.Objects.CA.PaymentMethod.PaymentDateToBankDate : Edm.Boolean [required] "Set Payment Date to Bank Transaction Date"
PX.Objects.CA.PaymentMethod.NoteID : Edm.Guid
PX.Objects.CA.PaymentMethod.NoteText : Edm.String "Note Text"
PX.Objects.CA.PaymentMethod.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.PaymentMethod.CreatedByScreenID : Edm.String
PX.Objects.CA.PaymentMethod.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CA.PaymentMethod.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.PaymentMethod.LastModifiedByScreenID : Edm.String
PX.Objects.CA.PaymentMethod.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.PaymentMethod.tstamp : Edm.Binary
PX.Objects.CA.PaymentMethod.IsAccountNumberRequired : Edm.Boolean "Require Card/Account Number"
PX.Objects.CA.PaymentMethod.PrintOrExport : Edm.Boolean "Print Checks/Export"
PX.Objects.CA.PaymentMethod.HasProcessingCenters : Edm.Boolean
PX.Objects.CA.PaymentMethod.IsUsingPlugin : Edm.Boolean
PX.Objects.CA.PaymentMethod.SendPaymentReceiptsAutomatically : Edm.Boolean [required] "Send Payment Receipts Automatically"
PX.Objects.CA.PaymentMethod.ExternalPaymentProcessorID : Edm.String "External Payment Processor"
PX.Objects.CA.PaymentMethod.ExternalPaymentProcessorType : Edm.String "External Processor Type"
PX.Objects.CA.PaymentMethod.NeedAccountFilter : Edm.Boolean
PX.Objects.CA.PaymentMethod.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.PaymentMethod.SiteMapByAPCheckReportID -> PX.SM.SiteMap (APCheckReportID=ScreenID)
PX.Objects.CA.PaymentMethod.SiteMapByAPRemittanceReportID -> PX.SM.SiteMap (APRemittanceReportID=ScreenID)
PX.Objects.CA.PaymentMethod.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.PaymentMethod.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.PaymentMethod.SYMappingByAPBatchExportSYMappingID -> PX.Api.SYMapping (APBatchExportSYMappingID=MappingID)
PX.Objects.CA.PaymentMethod.CustomerPaymentMethodByPMInstanceID -> PX.Objects.AR.CustomerPaymentMethod (PMInstanceID=PMInstanceID)
PX.Objects.CA.PaymentMethod.PPExternalByExternalPaymentProcessorID -> PX.PaymentProcessorCommon.DAC.PPExternal (ExternalPaymentProcessorID=ExternalPaymentProcessorID)
PX.Objects.CA.PaymentMethod.PREmployeeCollection -> Collection(PX.Objects.PR.PREmployee)
PX.Objects.CA.PaymentMethod.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CA.PaymentMethod.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CA.PaymentMethod.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CA.PaymentMethod.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CA.PaymentMethod.VendorPaymentMethodCollection -> Collection(PX.Objects.AP.DAC.VendorPaymentMethod)
PX.Objects.CA.PaymentMethod.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CA.PaymentMethod.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)
PX.Objects.CA.PaymentMethod.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.CA.PaymentMethod.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CA.PaymentMethod.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.CA.PaymentMethod.LocationExtAddressCollection -> Collection(PX.Objects.CR.LocationExtAddress)
PX.Objects.CA.PaymentMethod.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CA.PaymentMethod.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CA.PaymentMethod.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.CA.PaymentMethod.VendorPaymentMethodDetailCollection -> Collection(PX.Objects.AP.VendorPaymentMethodDetail)
PX.Objects.CA.PaymentMethod.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CA.PaymentMethod.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CA.PaymentMethod.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.CA.PaymentMethod.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CA.PaymentMethod.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CA.PaymentMethod.ACHPlugInParameterCollection -> Collection(PX.Objects.CA.ACHPlugInParameter)
PX.Objects.CA.PaymentMethod.POAdjustCollection -> Collection(PX.Objects.PO.POAdjust)
PX.Objects.CA.PaymentMethod.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.CA.PaymentMethod.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.CA.PaymentMethod.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CA.PaymentMethod.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.CA.PaymentMethod.CCProcessingCenterPmntMethodBranchCollection -> Collection(PX.Objects.CA.CCProcessingCenterPmntMethodBranch)
PX.Objects.CA.PaymentMethod.PaymentMethodDetailCollection -> Collection(PX.Objects.CA.PaymentMethodDetail)
PX.Objects.CA.PaymentMethod.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CA.PaymentMethod.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.CA.PaymentMethod.CustomerPaymentMethodDetailCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodDetail)
PX.Objects.CA.PaymentMethod.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.CA.PaymentMethod.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CA.PaymentMethod.CCProcessingCenterBranchCollection -> Collection(PX.Objects.CC.CCProcessingCenterBranch)
PX.Objects.CA.PaymentMethod.PaymentMethodAccountCollection -> Collection(PX.Objects.CA.PaymentMethodAccount)
PX.Objects.CA.PaymentMethod.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.CA.PaymentMethod.CustomerPaymentMethodInfoCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodInfo)
PX.Objects.CA.PaymentMethod.LocationAPPaymentInfoCollection -> Collection(PX.Objects.AP.LocationAPPaymentInfo)
PX.Objects.CA.PaymentMethod.BCPaymentMethodsCollection -> Collection(PX.Commerce.Objects.BCPaymentMethods)
PX.Objects.CA.PaymentMethod.CashAccountDepositCollection -> Collection(PX.Objects.CA.CashAccountDeposit)
PX.Objects.CA.PaymentMethod.CashAccountPaymentMethodDetailCollection -> Collection(PX.Objects.CA.CashAccountPaymentMethodDetail)
PX.Objects.CA.PaymentMethod.CCProcessingCenterPmntMethodCollection -> Collection(PX.Objects.CA.CCProcessingCenterPmntMethod)

# PX.Objects.CA.PaymentMethodAccount (EntityType)

Label: "Payment Method for Cash Account"
Key: CashAccountID, PaymentMethodID
Entity sets: PX_Objects_CA_PaymentMethodAccount, PaymentMethodforCashAccount, PaymentMethodAccount

PX.Objects.CA.PaymentMethodAccount.PaymentMethodID : Edm.String [key] "Payment Method"
PX.Objects.CA.PaymentMethodAccount.CashAccountID : Edm.Int32 [key] "Cash Account"
PX.Objects.CA.PaymentMethodAccount.UseForAP : Edm.Boolean [required] "Use in AP"
PX.Objects.CA.PaymentMethodAccount.APIsDefault : Edm.Boolean [required] "AP Default"
PX.Objects.CA.PaymentMethodAccount.APAutoNextNbr : Edm.Boolean [required] "AP - Suggest Next Number"
PX.Objects.CA.PaymentMethodAccount.APLastRefNbr : Edm.String "AP Last Reference Number"
PX.Objects.CA.PaymentMethodAccount.APBatchLastRefNbr : Edm.String "Batch Last Reference Number"
PX.Objects.CA.PaymentMethodAccount.APQuickBatchGeneration : Edm.Boolean [required] "Quick Batch Generation"
PX.Objects.CA.PaymentMethodAccount.UseForAR : Edm.Boolean [required] "Use in AR"
PX.Objects.CA.PaymentMethodAccount.ARIsDefault : Edm.Boolean [required] "AR Default"
PX.Objects.CA.PaymentMethodAccount.ARIsDefaultForRefund : Edm.Boolean [required] "AR Default For Refund"
PX.Objects.CA.PaymentMethodAccount.ARAutoNextNbr : Edm.Boolean [required] "AR - Suggest Next Number"
PX.Objects.CA.PaymentMethodAccount.ARLastRefNbr : Edm.String "AR Last Reference Number"
PX.Objects.CA.PaymentMethodAccount.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CA.PaymentMethodAccount.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CA.PaymentMethodAccount.CashAccountByCashAccountID -> PX.Objects.CA.CashAccount (CashAccountID=CashAccountID)
PX.Objects.CA.PaymentMethodAccount.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.PaymentMethodAccount.CashAccountPaymentMethodDetailCollection -> Collection(PX.Objects.CA.CashAccountPaymentMethodDetail)

# PX.Objects.CA.PaymentMethodDetail (EntityType)

Label: "Payment Method Detail"
Key: DetailID, PaymentMethodID, UseFor
Entity sets: PX_Objects_CA_PaymentMethodDetail, PaymentMethodDetail
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.CA.PaymentMethodDetail.PaymentMethodID : Edm.String [key] "Payment Method"
PX.Objects.CA.PaymentMethodDetail.UseFor : Edm.String [key required] "Used In"
PX.Objects.CA.PaymentMethodDetail.DetailID : Edm.String [key] "ID"
PX.Objects.CA.PaymentMethodDetail.Descr : Edm.String "Description"
PX.Objects.CA.PaymentMethodDetail.EntryMask : Edm.String "Entry Mask"
PX.Objects.CA.PaymentMethodDetail.ValidRegexp : Edm.String "Validation Reg. Exp."
PX.Objects.CA.PaymentMethodDetail.DisplayMask : Edm.String "Display Mask"
PX.Objects.CA.PaymentMethodDetail.IsEncrypted : Edm.Boolean [required] "Encrypted"
PX.Objects.CA.PaymentMethodDetail.IsRequired : Edm.Boolean [required] "Required"
PX.Objects.CA.PaymentMethodDetail.IsIdentifier : Edm.Boolean [required] "Card/Account Nbr."
PX.Objects.CA.PaymentMethodDetail.IsExpirationDate : Edm.Boolean [required] "Exp. Date"
PX.Objects.CA.PaymentMethodDetail.IsOwnerName : Edm.Boolean [required] "Name on Card"
PX.Objects.CA.PaymentMethodDetail.IsCCProcessingID : Edm.Boolean [required] "Payment Profile ID"
PX.Objects.CA.PaymentMethodDetail.IsCVV : Edm.Boolean [required] "CVV Code"
PX.Objects.CA.PaymentMethodDetail.ControlType : Edm.Int32 [required] "Control Type"
PX.Objects.CA.PaymentMethodDetail.AttributeID : Edm.String "Attribute ID"
PX.Objects.CA.PaymentMethodDetail.DefaultValue : Edm.String "Default Value"
PX.Objects.CA.PaymentMethodDetail.OrderIndex : Edm.Int16 "Sort Order"
PX.Objects.CA.PaymentMethodDetail.tstamp : Edm.Binary
PX.Objects.CA.PaymentMethodDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CA.PaymentMethodDetail.CreatedByScreenID : Edm.String
PX.Objects.CA.PaymentMethodDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CA.PaymentMethodDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CA.PaymentMethodDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CA.PaymentMethodDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CA.PaymentMethodDetail.NoteID : Edm.Guid
PX.Objects.CA.PaymentMethodDetail.NoteText : Edm.String "Note Text"
PX.Objects.CA.PaymentMethodDetail.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CA.PaymentMethodDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CA.PaymentMethodDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CA.PaymentMethodDetail.CSAttributeByAttributeID -> PX.Objects.CS.CSAttribute (AttributeID=AttributeID)
PX.Objects.CA.PaymentMethodDetail.PaymentMethodByPaymentMethodID -> PX.Objects.CA.PaymentMethod (PaymentMethodID=PaymentMethodID)
PX.Objects.CA.PaymentMethodDetail.VendorPaymentMethodDetailCollection -> Collection(PX.Objects.AP.VendorPaymentMethodDetail)
PX.Objects.CA.PaymentMethodDetail.CustomerPaymentMethodDetailCollection -> Collection(PX.Objects.AR.CustomerPaymentMethodDetail)
PX.Objects.CA.PaymentMethodDetail.CashAccountPaymentMethodDetailCollection -> Collection(PX.Objects.CA.CashAccountPaymentMethodDetail)

# PX.Objects.CC.CCPayLink (EntityType)

Label: "Payment Link"
Key: PayLinkID
Entity sets: PX_Objects_CC_CCPayLink, PaymentLink, CCPayLink
Non-filterable, non-selectable: NoteText

PX.Objects.CC.CCPayLink.PayLinkID : Edm.Int32 [key] "Pay Link ID"
PX.Objects.CC.CCPayLink.DeliveryMethod : Edm.String "Link Delivery Method"
PX.Objects.CC.CCPayLink.ProcessingCenterID : Edm.String "Processing Center"
PX.Objects.CC.CCPayLink.CuryID : Edm.String "Currency"
PX.Objects.CC.CCPayLink.Amount : Edm.Decimal [required] "Amount"
PX.Objects.CC.CCPayLink.DueDate : Edm.DateTimeOffset
PX.Objects.CC.CCPayLink.DocType : Edm.String "Doc. Type"
PX.Objects.CC.CCPayLink.RefNbr : Edm.String "Doc. Reference Nbr."
PX.Objects.CC.CCPayLink.OrderType : Edm.String "Order Type"
PX.Objects.CC.CCPayLink.OrderNbr : Edm.String "Order Reference Nbr."
PX.Objects.CC.CCPayLink.Action : Edm.String
PX.Objects.CC.CCPayLink.ActionStatus : Edm.String
PX.Objects.CC.CCPayLink.StatusDate : Edm.DateTimeOffset "Status Date"
PX.Objects.CC.CCPayLink.LinkStatus : Edm.String "Link Status"
PX.Objects.CC.CCPayLink.PaymentStatus : Edm.String "Payment Status"
PX.Objects.CC.CCPayLink.NeedSync : Edm.Boolean [required] "Synchronization Required"
PX.Objects.CC.CCPayLink.NeedReportSync : Edm.Boolean [required]
PX.Objects.CC.CCPayLink.ReportAttachmentID : Edm.String
PX.Objects.CC.CCPayLink.Url : Edm.String "Payment Link"
PX.Objects.CC.CCPayLink.ExternalID : Edm.String "Link External ID"
PX.Objects.CC.CCPayLink.ErrorMessage : Edm.String "Error Message"
PX.Objects.CC.CCPayLink.NoteID : Edm.Guid
PX.Objects.CC.CCPayLink.NoteText : Edm.String "Note Text"
PX.Objects.CC.CCPayLink.CreatedByID : Edm.Guid "Created By"
PX.Objects.CC.CCPayLink.CreatedByScreenID : Edm.String
PX.Objects.CC.CCPayLink.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CC.CCPayLink.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CC.CCPayLink.LastModifiedByScreenID : Edm.String
PX.Objects.CC.CCPayLink.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CC.CCPayLink.tstamp : Edm.Binary
PX.Objects.CC.CCPayLink.ARInvoiceByRefNbr -> PX.Objects.AR.ARInvoice (DocType=DocType, RefNbr=RefNbr)
PX.Objects.CC.CCPayLink.SOOrderByOrderNbr -> PX.Objects.SO.SOOrder (OrderType=OrderType, OrderNbr=OrderNbr)
PX.Objects.CC.CCPayLink.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CC.CCPayLink.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CC.CCPayLink.ExternalTransactionCollection -> Collection(PX.Objects.AR.ExternalTransaction)

# PX.Objects.CC.CCProcessingCenterBranch (EntityType)

Label: "Payment Creation Settings"
Key: BranchID, ProcessingCenterID
Entity sets: PX_Objects_CC_CCProcessingCenterBranch, PaymentCreationSettings, CCProcessingCenterBranch

PX.Objects.CC.CCProcessingCenterBranch.ProcessingCenterID : Edm.String [key] "Proc. Center ID"
PX.Objects.CC.CCProcessingCenterBranch.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.CC.CCProcessingCenterBranch.DefaultForBranch : Edm.Boolean [required] "Use by Default"
PX.Objects.CC.CCProcessingCenterBranch.CCPaymentMethodID : Edm.String "Credit Card Payment Method"
PX.Objects.CC.CCProcessingCenterBranch.EFTPaymentMethodID : Edm.String "EFT Payment Method"
PX.Objects.CC.CCProcessingCenterBranch.tstamp : Edm.Binary
PX.Objects.CC.CCProcessingCenterBranch.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CC.CCProcessingCenterBranch.CashAccountByBranchID -> PX.Objects.CA.CashAccount
PX.Objects.CC.CCProcessingCenterBranch.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.CC.CCProcessingCenterBranch.PaymentMethodByCCPaymentMethodID -> PX.Objects.CA.PaymentMethod (CCPaymentMethodID=PaymentMethodID)
PX.Objects.CC.CCProcessingCenterBranch.PaymentMethodByEFTPaymentMethodID -> PX.Objects.CA.PaymentMethod (EFTPaymentMethodID=PaymentMethodID)

# PX.Objects.CC.CCProcessingCenterTerminal (EntityType)

Label: "Processing Center Terminal"
Key: ProcessingCenterID, TerminalID
Entity sets: PX_Objects_CC_CCProcessingCenterTerminal, ProcessingCenterTerminal, CCProcessingCenterTerminal

PX.Objects.CC.CCProcessingCenterTerminal.ProcessingCenterID : Edm.String [key] "Processing Center ID"
PX.Objects.CC.CCProcessingCenterTerminal.TerminalID : Edm.String [key] "Terminal ID"
PX.Objects.CC.CCProcessingCenterTerminal.TerminalName : Edm.String "Terminal Name"
PX.Objects.CC.CCProcessingCenterTerminal.DisplayName : Edm.String "Display Name"
PX.Objects.CC.CCProcessingCenterTerminal.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CC.CCProcessingCenterTerminal.CanBeEnabled : Edm.Boolean [required]
PX.Objects.CC.CCProcessingCenterTerminal.CreatedByID : Edm.Guid "Created By"
PX.Objects.CC.CCProcessingCenterTerminal.CreatedByScreenID : Edm.String
PX.Objects.CC.CCProcessingCenterTerminal.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CC.CCProcessingCenterTerminal.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CC.CCProcessingCenterTerminal.LastModifiedByScreenID : Edm.String
PX.Objects.CC.CCProcessingCenterTerminal.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CC.CCProcessingCenterTerminal.tstamp : Edm.Binary
PX.Objects.CC.CCProcessingCenterTerminal.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CC.CCProcessingCenterTerminal.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CC.CCProcessingCenterTerminal.CCProcessingCenterByProcessingCenterID -> PX.Objects.CA.CCProcessingCenter (ProcessingCenterID=ProcessingCenterID)
PX.Objects.CC.CCProcessingCenterTerminal.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CC.CCProcessingCenterTerminal.ARCashSaleCollection -> Collection(PX.Objects.AR.Standalone.ARCashSale)

# PX.Objects.CC.DefaultTerminal (EntityType)

Label: "Default POS Terminal"
Key: BranchID, ProcessingCenterID, UserID
Entity sets: PX_Objects_CC_DefaultTerminal, DefaultPOSTerminal, DefaultTerminal

PX.Objects.CC.DefaultTerminal.UserID : Edm.Guid [key]
PX.Objects.CC.DefaultTerminal.BranchID : Edm.Int32 [key]
PX.Objects.CC.DefaultTerminal.ProcessingCenterID : Edm.String [key] "Processing Center ID"
PX.Objects.CC.DefaultTerminal.TerminalID : Edm.String "Terminal ID"

# PX.Objects.CM.APHistoryLastRevaluation (EntityType)

Key: AccountID, BranchID, CuryID, SubID, VendorID
Entity sets: PX_Objects_CM_APHistoryLastRevaluation

PX.Objects.CM.APHistoryLastRevaluation.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.CM.APHistoryLastRevaluation.VendorID : Edm.Int32 [key] "Vendor"
PX.Objects.CM.APHistoryLastRevaluation.AccountID : Edm.Int32 [key] "Account"
PX.Objects.CM.APHistoryLastRevaluation.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.CM.APHistoryLastRevaluation.CuryID : Edm.String [key]
PX.Objects.CM.APHistoryLastRevaluation.LastActivityPeriod : Edm.String
PX.Objects.CM.APHistoryLastRevaluation.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)

# PX.Objects.CM.ARHistoryLastRevaluation (EntityType)

Key: AccountID, BranchID, CuryID, CustomerID, SubID
Entity sets: PX_Objects_CM_ARHistoryLastRevaluation

PX.Objects.CM.ARHistoryLastRevaluation.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.CM.ARHistoryLastRevaluation.CustomerID : Edm.Int32 [key] "Customer"
PX.Objects.CM.ARHistoryLastRevaluation.AccountID : Edm.Int32 [key] "Account"
PX.Objects.CM.ARHistoryLastRevaluation.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.CM.ARHistoryLastRevaluation.CuryID : Edm.String [key]
PX.Objects.CM.ARHistoryLastRevaluation.LastActivityPeriod : Edm.String
PX.Objects.CM.ARHistoryLastRevaluation.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)

# PX.Objects.CM.CMSetup (EntityType)

Label: "Currency Management Preferences"
Singletons: PX_Objects_CM_CMSetup, CurrencyManagementPreferences, CMSetup

PX.Objects.CM.CMSetup.BatchNumberingID : Edm.String "Batch Numbering Sequence"
PX.Objects.CM.CMSetup.ExtRefNbrNumberingID : Edm.String "Batch Ref. Number Numbering Sequence"
PX.Objects.CM.CMSetup.APCuryOverride : Edm.Boolean [required] "Allow Vendor CurrencyID Override"
PX.Objects.CM.CMSetup.APRateTypeDflt : Edm.String "AP Rate Type"
PX.Objects.CM.CMSetup.APRateTypeOverride : Edm.Boolean [required] "Allow Vendor Rate Type Override"
PX.Objects.CM.CMSetup.APRateTypeReval : Edm.String "AP Revaluation Rate Type"
PX.Objects.CM.CMSetup.ARCuryOverride : Edm.Boolean [required] "Allow Customer Currency ID Override"
PX.Objects.CM.CMSetup.ARRateTypeDflt : Edm.String "AR Rate Type"
PX.Objects.CM.CMSetup.ARRateTypePrc : Edm.String "Sales Price Rate Type"
PX.Objects.CM.CMSetup.ARRateTypeOverride : Edm.Boolean [required] "Allow Customer Rate Type Override"
PX.Objects.CM.CMSetup.ARRateTypeReval : Edm.String "AR Revaluation Rate Type"
PX.Objects.CM.CMSetup.CARateTypeDflt : Edm.String "CA Rate Type"
PX.Objects.CM.CMSetup.GLRateTypeDflt : Edm.String "GL Rate Type"
PX.Objects.CM.CMSetup.GLRateTypeReval : Edm.String "GL Revaluation Rate Type"
PX.Objects.CM.CMSetup.PMRateTypeDflt : Edm.String "PM Rate Type"
PX.Objects.CM.CMSetup.SOFreightRateTypeDflt : Edm.String "SO Freight Rate Type"
PX.Objects.CM.CMSetup.RateVariance : Edm.Decimal "Rate Variance Allowed, %"
PX.Objects.CM.CMSetup.RateVarianceWarn : Edm.Boolean [required] "Warn About Rate Variance"
PX.Objects.CM.CMSetup.AutoPostOption : Edm.Boolean [required] "Automatically Post to GL on Release"
PX.Objects.CM.CMSetup.RevalueARPrepaymentsOption : Edm.Boolean [required] "Revalue AR Prepayment Balance"
PX.Objects.CM.CMSetup.RevalueAPPrepaymentsOption : Edm.Boolean [required] "Revalue AP Prepayment Balance"
PX.Objects.CM.CMSetup.TranslDefId : Edm.String "Default Translation ID"
PX.Objects.CM.CMSetup.RetainPeriodsNumber : Edm.Int16 "Keep History For Periods"
PX.Objects.CM.CMSetup.TranslNumberingID : Edm.String "Translation Numbering Sequence"
PX.Objects.CM.CMSetup.tstamp : Edm.Binary
PX.Objects.CM.CMSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.CMSetup.CreatedByScreenID : Edm.String
PX.Objects.CM.CMSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.CMSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.CMSetup.LastModifiedByScreenID : Edm.String
PX.Objects.CM.CMSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.CMSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.CMSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.CMSetup.NumberingByBatchNumberingID -> PX.Objects.CS.Numbering (BatchNumberingID=NumberingID)
PX.Objects.CM.CMSetup.NumberingByExtRefNbrNumberingID -> PX.Objects.CS.Numbering (ExtRefNbrNumberingID=NumberingID)
PX.Objects.CM.CMSetup.NumberingByTranslNumberingID -> PX.Objects.CS.Numbering (TranslNumberingID=NumberingID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByAPRateTypeDflt -> PX.Objects.CM.CurrencyRateType (APRateTypeDflt=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByAPRateTypeReval -> PX.Objects.CM.CurrencyRateType (APRateTypeReval=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByARRateTypeDflt -> PX.Objects.CM.CurrencyRateType (ARRateTypeDflt=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByARRateTypePrc -> PX.Objects.CM.CurrencyRateType (ARRateTypePrc=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByARRateTypeReval -> PX.Objects.CM.CurrencyRateType (ARRateTypeReval=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByCARateTypeDflt -> PX.Objects.CM.CurrencyRateType (CARateTypeDflt=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByGLRateTypeDflt -> PX.Objects.CM.CurrencyRateType (GLRateTypeDflt=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByGLRateTypeReval -> PX.Objects.CM.CurrencyRateType (GLRateTypeReval=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeByPMRateTypeDflt -> PX.Objects.CM.CurrencyRateType (PMRateTypeDflt=CuryRateTypeID)
PX.Objects.CM.CMSetup.CurrencyRateTypeBySOFreightRateTypeDflt -> PX.Objects.CM.CurrencyRateType (SOFreightRateTypeDflt=CuryRateTypeID)
PX.Objects.CM.CMSetup.TranslDefByTranslDefId -> PX.Objects.CM.TranslDef (TranslDefId=TranslDefId)

# PX.Objects.CM.Currency (EntityType)

Label: "Currency"
Key: CuryID
Entity sets: PX_Objects_CM_Currency, Currency
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.CM.Currency.CuryID : Edm.String [key] "Currency ID"
PX.Objects.CM.Currency.Description : Edm.String "Description"
PX.Objects.CM.Currency.CurySymbol : Edm.String "Currency Symbol"
PX.Objects.CM.Currency.CuryCaption : Edm.String "Currency Caption"
PX.Objects.CM.Currency.DecimalPlaces : Edm.Int16 "Decimal Precision"
PX.Objects.CM.Currency.UseARPreferencesSettings : Edm.Boolean [required] "Use AR Preferences Settings"
PX.Objects.CM.Currency.ARInvoicePrecision : Edm.Decimal [required] "Rounding Precision"
PX.Objects.CM.Currency.ARInvoiceRounding : Edm.String "Rounding Rule for Invoices"
PX.Objects.CM.Currency.UseAPPreferencesSettings : Edm.Boolean [required] "Use AP Preferences Settings"
PX.Objects.CM.Currency.APInvoicePrecision : Edm.Decimal [required] "Rounding Precision"
PX.Objects.CM.Currency.APInvoiceRounding : Edm.String "Rounding Rule for Bills"
PX.Objects.CM.Currency.CuryInfoID : Edm.Int64
PX.Objects.CM.Currency.CuryInfoBaseID : Edm.Int64
PX.Objects.CM.Currency.RoundingLimit : Edm.Decimal [required] "Rounding Limit"
PX.Objects.CM.Currency.NoteID : Edm.Guid
PX.Objects.CM.Currency.NoteText : Edm.String "Note Text"
PX.Objects.CM.Currency.tstamp : Edm.Binary
PX.Objects.CM.Currency.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.Currency.CreatedByScreenID : Edm.String
PX.Objects.CM.Currency.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Currency.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.Currency.LastModifiedByScreenID : Edm.String
PX.Objects.CM.Currency.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Currency.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CM.Currency.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.Currency.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.Currency.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.CM.Currency.AccountByRealGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByRealLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByRevalGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByRevalLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByAPProvAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByTranslationGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByTranslationLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByUnrealizedGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByRoundingGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByRoundingLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByARProvAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.AccountByUnrealizedLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Currency.SubByRealGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByRealLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByRevalGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByRevalLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByAPProvSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByTranslationGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByTranslationLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByUnrealizedGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByRoundingGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByRoundingLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByARProvSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.SubByUnrealizedLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Currency.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CM.Currency.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CM.Currency.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CM.Currency.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CM.Currency.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CM.Currency.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CM.Currency.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CM.Currency.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CM.Currency.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.CM.Currency.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CM.Currency.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CM.Currency.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CM.Currency.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CM.Currency.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CM.Currency.CurrencyRateCollection -> Collection(PX.Objects.CM.CurrencyRate)
PX.Objects.CM.Currency.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.CM.Currency.LedgerCollection -> Collection(PX.Objects.GL.Ledger)
PX.Objects.CM.Currency.CABankTranRuleCollection -> Collection(PX.Objects.CA.CABankTranRule)
PX.Objects.CM.Currency.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CM.Currency.CRCustomerClassCollection -> Collection(PX.Objects.CR.CRCustomerClass)
PX.Objects.CM.Currency.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CM.Currency.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CM.Currency.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CM.Currency.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CM.Currency.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CM.Currency.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CM.Currency.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.CM.Currency.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.CM.Currency.SVTicketCollection -> Collection(PX.Objects.SV.SVTicket)
PX.Objects.CM.Currency.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.CM.Currency.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.CM.Currency.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.CM.Currency.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CM.Currency.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.CM.Currency.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CM.Currency.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.CM.Currency.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.CM.Currency.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.CM.Currency.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.CM.Currency.CurrencyInfoCollection -> Collection(PX.Objects.CM.CurrencyInfo)
PX.Objects.CM.Currency.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.CM.Currency.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.CM.Currency.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CM.Currency.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.CM.Currency.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.CM.Currency.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CM.Currency.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CM.Currency.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.CM.Currency.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.Objects.CM.Currency.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.CM.Currency.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.CM.Currency.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.CM.Currency.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.Objects.CM.Currency.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.CM.Currency.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.CM.Currency.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CM.Currency.CABankTranHeaderCollection -> Collection(PX.Objects.CA.CABankTranHeader)
PX.Objects.CM.Currency.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.CM.Currency.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CM.Currency.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.CM.Currency.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.Objects.CM.Currency.CashForecastTranCollection -> Collection(PX.Objects.CA.CashForecastTran)
PX.Objects.CM.Currency.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.CM.Currency.CCBatchCollection -> Collection(PX.Objects.CA.CCBatch)
PX.Objects.CM.Currency.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CM.Currency.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.CM.Currency.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.CM.Currency.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.Objects.CM.Currency.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CM.Currency.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.CM.Currency.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.CM.Currency.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.CM.Currency.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CM.Currency.FSSalesPriceCollection -> Collection(PX.Objects.FS.FSSalesPrice)
PX.Objects.CM.Currency.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CM.Currency.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CM.Currency.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CM.Currency.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.CM.Currency.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.CM.Currency.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.CM.Currency.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.CM.Currency.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CM.Currency.AMConfigurationKeysCollection -> Collection(PX.Objects.AM.AMConfigurationKeys)
PX.Objects.CM.Currency.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.CM.Currency.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.CM.Currency.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.CM.Currency.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.CM.Currency.CompanyCollection -> Collection(PX.Objects.GL.Company)
PX.Objects.CM.Currency.RQBudgetCollection -> Collection(PX.Objects.RQ.RQBudget)
PX.Objects.CM.Currency.RQRequestLineSelectCollection -> Collection(PX.Objects.RQ.RQRequestLineSelect)
PX.Objects.CM.Currency.BCPaymentMethodsCollection -> Collection(PX.Commerce.Objects.BCPaymentMethods)
PX.Objects.CM.Currency.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.CM.Currency.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.CM.Currency.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.CM.Currency.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.CM.Currency.PendingPPDARTaxAdjAppCollection -> Collection(PX.Objects.AR.PendingPPDARTaxAdjApp)
PX.Objects.CM.Currency.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CM.Currency.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.CM.Currency.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.CM.Currency.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CM.Currency.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CM.Currency.POLinePMCollection -> Collection(PX.Objects.PM.POLinePM)
PX.Objects.CM.Currency.POOrderPMCollection -> Collection(PX.Objects.PM.POOrderPM)
PX.Objects.CM.Currency.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.CM.Currency.VendorLocationCollection -> Collection(PX.Objects.PO.VendorLocation)

# PX.Objects.CM.CurrencyInfo (EntityType)

Label: "Currency Info"
Key: CuryInfoID
Entity sets: PX_Objects_CM_CurrencyInfo, CurrencyInfo
Non-filterable, non-selectable: DisplayCuryID, SampleCuryRate, SampleRecipRate, CuryPrecision, BasePrecision

PX.Objects.CM.CurrencyInfo.CuryInfoID : Edm.Int64 [key] "CuryInfoID"
PX.Objects.CM.CurrencyInfo.BaseCalc : Edm.Boolean [required]
PX.Objects.CM.CurrencyInfo.BaseCuryID : Edm.String "Base Currency ID"
PX.Objects.CM.CurrencyInfo.CuryID : Edm.String "Currency"
PX.Objects.CM.CurrencyInfo.DisplayCuryID : Edm.String "Currency ID"
PX.Objects.CM.CurrencyInfo.CuryRateTypeID : Edm.String "Curr. Rate Type ID"
PX.Objects.CM.CurrencyInfo.CuryEffDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.CM.CurrencyInfo.CuryMultDiv : Edm.String "Mult Div"
PX.Objects.CM.CurrencyInfo.CuryRate : Edm.Decimal
PX.Objects.CM.CurrencyInfo.RecipRate : Edm.Decimal
PX.Objects.CM.CurrencyInfo.SampleCuryRate : Edm.Decimal "Curr. Rate"
PX.Objects.CM.CurrencyInfo.SampleRecipRate : Edm.Decimal "Reciprocal Rate"
PX.Objects.CM.CurrencyInfo.CuryPrecision : Edm.Int16
PX.Objects.CM.CurrencyInfo.BasePrecision : Edm.Int16
PX.Objects.CM.CurrencyInfo.tstamp : Edm.Binary
PX.Objects.CM.CurrencyInfo.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.CM.CurrencyInfo.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType (CuryRateTypeID=CuryRateTypeID)
PX.Objects.CM.CurrencyInfo.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CM.CurrencyInfo.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CM.CurrencyInfo.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CM.CurrencyInfo.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CM.CurrencyInfo.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.CM.CurrencyInfo.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.CM.CurrencyInfo.GLTaxCollection -> Collection(PX.Objects.GL.GLTax)
PX.Objects.CM.CurrencyInfo.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CM.CurrencyInfo.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.CM.CurrencyInfo.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CM.CurrencyInfo.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.CM.CurrencyInfo.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.CM.CurrencyInfo.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.Objects.CM.CurrencyInfo.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.CM.CurrencyInfo.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CM.CurrencyInfo.POLandedCostTaxCollection -> Collection(PX.Objects.PO.POLandedCostTax)
PX.Objects.CM.CurrencyInfo.POLandedCostTaxTranCollection -> Collection(PX.Objects.PO.POLandedCostTaxTran)
PX.Objects.CM.CurrencyInfo.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.CM.CurrencyInfo.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)
PX.Objects.CM.CurrencyInfo.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.CM.CurrencyInfo.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CM.CurrencyInfo.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.CM.CurrencyInfo.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.CM.CurrencyInfo.CATaxCollection -> Collection(PX.Objects.CA.CATax)
PX.Objects.CM.CurrencyInfo.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.CM.CurrencyInfo.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CM.CurrencyInfo.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.CM.CurrencyInfo.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CM.CurrencyInfo.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.CM.CurrencyInfo.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CM.CurrencyInfo.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.CM.CurrencyInfo.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CM.CurrencyInfo.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.CM.CurrencyInfo.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CM.CurrencyInfo.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.CM.CurrencyInfo.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.CM.CurrencyInfo.FSAppointmentTaxTranCollection -> Collection(PX.Objects.FS.FSAppointmentTaxTran)
PX.Objects.CM.CurrencyInfo.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CM.CurrencyInfo.FSServiceOrderTaxTranCollection -> Collection(PX.Objects.FS.FSServiceOrderTaxTran)
PX.Objects.CM.CurrencyInfo.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.CM.CurrencyInfo.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.CM.CurrencyInfo.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.Objects.CM.CurrencyInfo.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)
PX.Objects.CM.CurrencyInfo.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.CM.CurrencyInfo.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.CM.CurrencyInfo.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.CM.CurrencyInfo.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.CM.CurrencyInfo.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CM.CurrencyInfo.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.CM.CurrencyInfo.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.CM.CurrencyInfo.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.CM.CurrencyInfo.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.CM.CurrencyInfo.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.Objects.CM.CurrencyInfo.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CM.CurrencyInfo.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.CM.CurrencyInfo.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CM.CurrencyInfo.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.CM.CurrencyInfo.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.CM.CurrencyInfo.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.CM.CurrencyInfo.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.CM.CurrencyInfo.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CM.CurrencyInfo.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.CM.CurrencyInfo.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.CM.CurrencyInfo.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.CM.CurrencyInfo.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.CM.CurrencyInfo.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CM.CurrencyInfo.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.CM.CurrencyInfo.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.Objects.CM.CurrencyInfo.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.CM.CurrencyInfo.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.CM.CurrencyInfo.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.CM.CurrencyInfo.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.CM.CurrencyInfo.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.CM.CurrencyInfo.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.CM.CurrencyInfo.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.CM.CurrencyInfo.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.CM.CurrencyInfo.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CM.CurrencyInfo.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.CM.CurrencyInfo.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CM.CurrencyInfo.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CM.CurrencyInfo.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.CM.CurrencyInfo.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.CM.CurrencyInfo.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.CM.CurrencyInfo.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CM.CurrencyInfo.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.CM.CurrencyInfo.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.CM.CurrencyInfo.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.CM.CurrencyInfo.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)

# PX.Objects.CM.CurrencyList (EntityType)

Label: "Currency"
Key: CuryID
Entity sets: PX_Objects_CM_CurrencyList, Currency1, CurrencyList
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CM.CurrencyList.CuryID : Edm.String [key] "Currency ID"
PX.Objects.CM.CurrencyList.Description : Edm.String "Description"
PX.Objects.CM.CurrencyList.CurySymbol : Edm.String "Currency Symbol"
PX.Objects.CM.CurrencyList.CuryCaption : Edm.String "Currency Caption"
PX.Objects.CM.CurrencyList.DecimalPlaces : Edm.Int16 "Decimal Precision"
PX.Objects.CM.CurrencyList.ISODecimalPlaces : Edm.Int16
PX.Objects.CM.CurrencyList.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.CurrencyList.CreatedByScreenID : Edm.String
PX.Objects.CM.CurrencyList.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.CurrencyList.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.CurrencyList.LastModifiedByScreenID : Edm.String
PX.Objects.CM.CurrencyList.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.CurrencyList.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CM.CurrencyList.IsFinancial : Edm.Boolean [required] "Use for Accounting"
PX.Objects.CM.CurrencyList.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CM.CurrencyList.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.CurrencyList.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.CurrencyList.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CM.CurrencyList.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CM.CurrencyList.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CM.CurrencyList.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.CM.CurrencyList.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CM.CurrencyList.CurrencyRateCollection -> Collection(PX.Objects.CM.CurrencyRate)
PX.Objects.CM.CurrencyList.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.Objects.CM.CurrencyList.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CM.CurrencyList.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.CM.CurrencyList.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CM.CurrencyList.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CM.CurrencyList.CurrencyCollection -> Collection(PX.Objects.CM.Currency)
PX.Objects.CM.CurrencyList.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CM.CurrencyList.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.CM.CurrencyList.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.Objects.CM.CurrencyList.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.CM.CurrencyList.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.CM.CurrencyList.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.CM.CurrencyList.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.CM.CurrencyList.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.CM.CurrencyList.CABankFeedDetailCollection -> Collection(PX.Objects.CA.CABankFeedDetail)
PX.Objects.CM.CurrencyList.AMMachCurySettingsCollection -> Collection(PX.Objects.AM.AMMachCurySettings)
PX.Objects.CM.CurrencyList.AMOverheadCurySettingsCollection -> Collection(PX.Objects.AM.AMOverheadCurySettings)
PX.Objects.CM.CurrencyList.AMToolMstCurySettingsCollection -> Collection(PX.Objects.AM.AMToolMstCurySettings)
PX.Objects.CM.CurrencyList.AMWCCurySettingsCollection -> Collection(PX.Objects.AM.AMWCCurySettings)
PX.Objects.CM.CurrencyList.AMBomOperCuryCollection -> Collection(PX.Objects.AM.AMBomOperCury)
PX.Objects.CM.CurrencyList.CompanyCollection -> Collection(PX.Objects.GL.Company)
PX.Objects.CM.CurrencyList.RefreshRateCollection -> Collection(PX.Objects.CM.RefreshRate)
PX.Objects.CM.CurrencyList.AMBomMatlCuryCollection -> Collection(PX.Objects.AM.AMBomMatlCury)
PX.Objects.CM.CurrencyList.AMBomToolCuryCollection -> Collection(PX.Objects.AM.AMBomToolCury)
PX.Objects.CM.CurrencyList.AMWCCuryCollection -> Collection(PX.Objects.AM.AMWCCury)
PX.Objects.CM.CurrencyList.AMWCMachCuryCollection -> Collection(PX.Objects.AM.AMWCMachCury)
PX.Objects.CM.CurrencyList.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CM.CurrencyList.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.CM.CurrencyList.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)

# PX.Objects.CM.CurrencyRate (EntityType)

Label: "Currency Rate"
Key: CuryRateID
Entity sets: PX_Objects_CM_CurrencyRate, CurrencyRate
Non-filterable, non-selectable: NoteText

PX.Objects.CM.CurrencyRate.CuryRateID : Edm.Int32 [key] "CuryRate ID"
PX.Objects.CM.CurrencyRate.FromCuryID : Edm.String "From Currency"
PX.Objects.CM.CurrencyRate.CuryRateType : Edm.String "Currency Rate Type"
PX.Objects.CM.CurrencyRate.CuryEffDate : Edm.DateTimeOffset "Currency Effective Date"
PX.Objects.CM.CurrencyRate.CuryMultDiv : Edm.String "Mult./Div."
PX.Objects.CM.CurrencyRate.CuryRate : Edm.Decimal "Currency Rate"
PX.Objects.CM.CurrencyRate.RateReciprocal : Edm.Decimal "Rate Reciprocal"
PX.Objects.CM.CurrencyRate.ToCuryID : Edm.String "To Currency"
PX.Objects.CM.CurrencyRate.NoteID : Edm.Guid
PX.Objects.CM.CurrencyRate.NoteText : Edm.String "Note Text"
PX.Objects.CM.CurrencyRate.tstamp : Edm.Binary
PX.Objects.CM.CurrencyRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.CurrencyRate.CreatedByScreenID : Edm.String
PX.Objects.CM.CurrencyRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.CurrencyRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.CurrencyRate.LastModifiedByScreenID : Edm.String
PX.Objects.CM.CurrencyRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.CurrencyRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.CurrencyRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.CurrencyRate.CurrencyByFromCuryID -> PX.Objects.CM.Currency (FromCuryID=CuryID)
PX.Objects.CM.CurrencyRate.CurrencyByToCuryID -> PX.Objects.CM.Currency (ToCuryID=CuryID)
PX.Objects.CM.CurrencyRate.CurrencyListByFromCuryID -> PX.Objects.CM.CurrencyList (FromCuryID=CuryID)
PX.Objects.CM.CurrencyRate.CurrencyListByToCuryID -> PX.Objects.CM.CurrencyList (ToCuryID=CuryID)
PX.Objects.CM.CurrencyRate.CurrencyRateTypeByCuryRateType -> PX.Objects.CM.CurrencyRateType (CuryRateType=CuryRateTypeID)

# PX.Objects.CM.CurrencyRate2 (EntityType)

Label: "Effective Currency Rate"
BaseType: PX.Objects.CM.CurrencyRate
Key: CuryRateID (inherited from PX.Objects.CM.CurrencyRate)
Entity sets: PX_Objects_CM_CurrencyRate2, EffectiveCurrencyRate, CurrencyRate2

# PX.Objects.CM.CurrencyRateByDate (EntityType)

Label: "Currency Rate by Date"
BaseType: PX.Objects.CM.CurrencyRate
Key: CuryRateID (inherited from PX.Objects.CM.CurrencyRate)
Entity sets: PX_Objects_CM_CurrencyRateByDate, CurrencyRatebyDate

PX.Objects.CM.CurrencyRateByDate.NextEffDate : Edm.DateTimeOffset

# PX.Objects.CM.CurrencyRateByDateForVendor (EntityType)

Label: "Currency Rate by Date"
BaseType: PX.Objects.CM.CurrencyRate
Key: CuryRateID (inherited from PX.Objects.CM.CurrencyRate)
Entity sets: PX_Objects_CM_CurrencyRateByDateForVendor, CurrencyRatebyDate1, CurrencyRateByDateForVendor

PX.Objects.CM.CurrencyRateByDateForVendor.NextEffDate : Edm.DateTimeOffset

# PX.Objects.CM.CurrencyRateType (EntityType)

Label: "Currency Rate Type"
Key: CuryRateTypeID
Entity sets: PX_Objects_CM_CurrencyRateType, CurrencyRateType
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CM.CurrencyRateType.CuryRateTypeID : Edm.String [key] "Rate Type ID"
PX.Objects.CM.CurrencyRateType.Descr : Edm.String "Description"
PX.Objects.CM.CurrencyRateType.RateEffDays : Edm.Int16 [required] "Days Effective"
PX.Objects.CM.CurrencyRateType.RefreshOnline : Edm.Boolean [required] "Refresh Online"
PX.Objects.CM.CurrencyRateType.OnlineRateAdjustment : Edm.Decimal "Online Rate Adjustment (%)"
PX.Objects.CM.CurrencyRateType.tstamp : Edm.Binary
PX.Objects.CM.CurrencyRateType.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.CurrencyRateType.CreatedByScreenID : Edm.String
PX.Objects.CM.CurrencyRateType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.CurrencyRateType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.CurrencyRateType.LastModifiedByScreenID : Edm.String
PX.Objects.CM.CurrencyRateType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.CurrencyRateType.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CM.CurrencyRateType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.CurrencyRateType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.CurrencyRateType.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CM.CurrencyRateType.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CM.CurrencyRateType.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CM.CurrencyRateType.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CM.CurrencyRateType.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CM.CurrencyRateType.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CM.CurrencyRateType.CurrencyRateCollection -> Collection(PX.Objects.CM.CurrencyRate)
PX.Objects.CM.CurrencyRateType.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CM.CurrencyRateType.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.CM.CurrencyRateType.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.Objects.CM.CurrencyRateType.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CM.CurrencyRateType.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.CM.CurrencyRateType.CurrencyInfoCollection -> Collection(PX.Objects.CM.CurrencyInfo)
PX.Objects.CM.CurrencyRateType.CMSetupCollection -> Collection(PX.Objects.CM.CMSetup)
PX.Objects.CM.CurrencyRateType.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.CM.CurrencyRateType.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.Objects.CM.CurrencyRateType.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.CM.CurrencyRateType.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CM.CurrencyRateType.RefreshRateCollection -> Collection(PX.Objects.CM.RefreshRate)
PX.Objects.CM.CurrencyRateType.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CM.CurrencyRateType.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)

# PX.Objects.CM.Extensions.Currency (EntityType)

Label: "Currency"
Key: CuryID
Entity sets: PX_Objects_CM_Extensions_Currency, Currency2
Non-filterable, non-selectable: NoteText, DeletedDatabaseRecord

PX.Objects.CM.Extensions.Currency.CuryID : Edm.String [key] "Currency ID"
PX.Objects.CM.Extensions.Currency.Description : Edm.String "Description"
PX.Objects.CM.Extensions.Currency.CurySymbol : Edm.String "Currency Symbol"
PX.Objects.CM.Extensions.Currency.CuryCaption : Edm.String "Currency Caption"
PX.Objects.CM.Extensions.Currency.DecimalPlaces : Edm.Int16 "Decimal Precision"
PX.Objects.CM.Extensions.Currency.NoteID : Edm.Guid
PX.Objects.CM.Extensions.Currency.NoteText : Edm.String "Note Text"
PX.Objects.CM.Extensions.Currency.tstamp : Edm.Binary
PX.Objects.CM.Extensions.Currency.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.Extensions.Currency.CreatedByScreenID : Edm.String
PX.Objects.CM.Extensions.Currency.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Extensions.Currency.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.Extensions.Currency.LastModifiedByScreenID : Edm.String
PX.Objects.CM.Extensions.Currency.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Extensions.Currency.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CM.Extensions.Currency.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.Extensions.Currency.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.Extensions.Currency.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.CM.Extensions.Currency.AccountByRealGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByRealLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByRevalGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByRevalLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByAPProvAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByTranslationGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByTranslationLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByUnrealizedGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByRoundingGainAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByRoundingLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByARProvAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.AccountByUnrealizedLossAcctID -> PX.Objects.GL.Account
PX.Objects.CM.Extensions.Currency.SubByRealGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByRealLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByRevalGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByRevalLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByAPProvSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByTranslationGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByTranslationLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByUnrealizedGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByRoundingGainSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByRoundingLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByARProvSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.SubByUnrealizedLossSubID -> PX.Objects.GL.Sub
PX.Objects.CM.Extensions.Currency.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CM.Extensions.Currency.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CM.Extensions.Currency.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CM.Extensions.Currency.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CM.Extensions.Currency.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CM.Extensions.Currency.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CM.Extensions.Currency.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CM.Extensions.Currency.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CM.Extensions.Currency.GLHistoryCollection -> Collection(PX.Objects.GL.GLHistory)
PX.Objects.CM.Extensions.Currency.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CM.Extensions.Currency.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CM.Extensions.Currency.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CM.Extensions.Currency.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CM.Extensions.Currency.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CM.Extensions.Currency.CurrencyRateCollection -> Collection(PX.Objects.CM.CurrencyRate)
PX.Objects.CM.Extensions.Currency.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.CM.Extensions.Currency.LedgerCollection -> Collection(PX.Objects.GL.Ledger)
PX.Objects.CM.Extensions.Currency.CABankTranRuleCollection -> Collection(PX.Objects.CA.CABankTranRule)
PX.Objects.CM.Extensions.Currency.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CM.Extensions.Currency.CRCustomerClassCollection -> Collection(PX.Objects.CR.CRCustomerClass)
PX.Objects.CM.Extensions.Currency.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CM.Extensions.Currency.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CM.Extensions.Currency.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CM.Extensions.Currency.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CM.Extensions.Currency.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CM.Extensions.Currency.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CM.Extensions.Currency.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.CM.Extensions.Currency.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.CM.Extensions.Currency.SVTicketCollection -> Collection(PX.Objects.SV.SVTicket)
PX.Objects.CM.Extensions.Currency.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.CM.Extensions.Currency.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.CM.Extensions.Currency.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.CM.Extensions.Currency.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CM.Extensions.Currency.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.CM.Extensions.Currency.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CM.Extensions.Currency.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.CM.Extensions.Currency.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.CM.Extensions.Currency.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.CM.Extensions.Currency.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.CM.Extensions.Currency.CurrencyInfoCollection -> Collection(PX.Objects.CM.CurrencyInfo)
PX.Objects.CM.Extensions.Currency.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.CM.Extensions.Currency.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.CM.Extensions.Currency.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CM.Extensions.Currency.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.CM.Extensions.Currency.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.CM.Extensions.Currency.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CM.Extensions.Currency.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CM.Extensions.Currency.ContractItemCollection -> Collection(PX.Objects.CT.ContractItem)
PX.Objects.CM.Extensions.Currency.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.Objects.CM.Extensions.Currency.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.CM.Extensions.Currency.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.CM.Extensions.Currency.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.CM.Extensions.Currency.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.Objects.CM.Extensions.Currency.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.CM.Extensions.Currency.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.CM.Extensions.Currency.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CM.Extensions.Currency.CABankTranHeaderCollection -> Collection(PX.Objects.CA.CABankTranHeader)
PX.Objects.CM.Extensions.Currency.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.CM.Extensions.Currency.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CM.Extensions.Currency.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.CM.Extensions.Currency.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.Objects.CM.Extensions.Currency.CashForecastTranCollection -> Collection(PX.Objects.CA.CashForecastTran)
PX.Objects.CM.Extensions.Currency.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.CM.Extensions.Currency.CCBatchCollection -> Collection(PX.Objects.CA.CCBatch)
PX.Objects.CM.Extensions.Currency.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CM.Extensions.Currency.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.CM.Extensions.Currency.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.CM.Extensions.Currency.CCProcTranCollection -> Collection(PX.Objects.AR.CCProcTran)
PX.Objects.CM.Extensions.Currency.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CM.Extensions.Currency.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.CM.Extensions.Currency.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.CM.Extensions.Currency.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.CM.Extensions.Currency.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CM.Extensions.Currency.FSSalesPriceCollection -> Collection(PX.Objects.FS.FSSalesPrice)
PX.Objects.CM.Extensions.Currency.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CM.Extensions.Currency.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CM.Extensions.Currency.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CM.Extensions.Currency.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.CM.Extensions.Currency.POOrderAPDocCollection -> Collection(PX.Objects.PO.POOrderAPDoc)
PX.Objects.CM.Extensions.Currency.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.CM.Extensions.Currency.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.CM.Extensions.Currency.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CM.Extensions.Currency.AMConfigurationKeysCollection -> Collection(PX.Objects.AM.AMConfigurationKeys)
PX.Objects.CM.Extensions.Currency.TaxHistoryCollection -> Collection(PX.Objects.TX.TaxHistory)
PX.Objects.CM.Extensions.Currency.ARStatementDetailCollection -> Collection(PX.Objects.AR.ARStatementDetail)
PX.Objects.CM.Extensions.Currency.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.CM.Extensions.Currency.INItemCostCollection -> Collection(PX.Objects.IN.INItemCost)
PX.Objects.CM.Extensions.Currency.CompanyCollection -> Collection(PX.Objects.GL.Company)
PX.Objects.CM.Extensions.Currency.RQBudgetCollection -> Collection(PX.Objects.RQ.RQBudget)
PX.Objects.CM.Extensions.Currency.RQRequestLineSelectCollection -> Collection(PX.Objects.RQ.RQRequestLineSelect)
PX.Objects.CM.Extensions.Currency.BCPaymentMethodsCollection -> Collection(PX.Commerce.Objects.BCPaymentMethods)
PX.Objects.CM.Extensions.Currency.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.CM.Extensions.Currency.POReceiptLandedCostDetailCollection -> Collection(PX.Objects.PO.LandedCosts.POReceiptLandedCostDetail)
PX.Objects.CM.Extensions.Currency.CABankTaxTranCollection -> Collection(PX.Objects.CA.CABankTaxTran)
PX.Objects.CM.Extensions.Currency.CABankTaxTranMatchCollection -> Collection(PX.Objects.CA.CABankTaxTranMatch)
PX.Objects.CM.Extensions.Currency.PendingPPDARTaxAdjAppCollection -> Collection(PX.Objects.AR.PendingPPDARTaxAdjApp)
PX.Objects.CM.Extensions.Currency.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CM.Extensions.Currency.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.CM.Extensions.Currency.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.CM.Extensions.Currency.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CM.Extensions.Currency.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CM.Extensions.Currency.POLinePMCollection -> Collection(PX.Objects.PM.POLinePM)
PX.Objects.CM.Extensions.Currency.POOrderPMCollection -> Collection(PX.Objects.PM.POOrderPM)
PX.Objects.CM.Extensions.Currency.POLandedCostDetailSCollection -> Collection(PX.Objects.PO.POLandedCostDetailS)
PX.Objects.CM.Extensions.Currency.VendorLocationCollection -> Collection(PX.Objects.PO.VendorLocation)

# PX.Objects.CM.Extensions.CurrencyInfo (EntityType)

Label: "Currency Info"
Key: CuryInfoID
Entity sets: PX_Objects_CM_Extensions_CurrencyInfo, CurrencyInfo1
Non-filterable, non-selectable: DisplayCuryID, SampleCuryRate, SampleRecipRate, CuryPrecision, BasePrecision

PX.Objects.CM.Extensions.CurrencyInfo.CuryInfoID : Edm.Int64 [key] "CuryInfoID"
PX.Objects.CM.Extensions.CurrencyInfo.BaseCalc : Edm.Boolean [required]
PX.Objects.CM.Extensions.CurrencyInfo.BaseCuryID : Edm.String "Base Currency ID"
PX.Objects.CM.Extensions.CurrencyInfo.CuryID : Edm.String "Currency"
PX.Objects.CM.Extensions.CurrencyInfo.DisplayCuryID : Edm.String "Currency ID"
PX.Objects.CM.Extensions.CurrencyInfo.CuryRateTypeID : Edm.String "Curr. Rate Type ID"
PX.Objects.CM.Extensions.CurrencyInfo.CuryEffDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.CM.Extensions.CurrencyInfo.CuryMultDiv : Edm.String "Mult Div"
PX.Objects.CM.Extensions.CurrencyInfo.CuryRate : Edm.Decimal
PX.Objects.CM.Extensions.CurrencyInfo.RecipRate : Edm.Decimal
PX.Objects.CM.Extensions.CurrencyInfo.SampleCuryRate : Edm.Decimal "Curr. Rate"
PX.Objects.CM.Extensions.CurrencyInfo.SampleRecipRate : Edm.Decimal "Reciprocal Rate"
PX.Objects.CM.Extensions.CurrencyInfo.CuryPrecision : Edm.Int16
PX.Objects.CM.Extensions.CurrencyInfo.BasePrecision : Edm.Int16
PX.Objects.CM.Extensions.CurrencyInfo.tstamp : Edm.Binary
PX.Objects.CM.Extensions.CurrencyInfo.CurrencyByBaseCuryID -> PX.Objects.CM.Currency (BaseCuryID=CuryID)
PX.Objects.CM.Extensions.CurrencyInfo.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType (CuryRateTypeID=CuryRateTypeID)
PX.Objects.CM.Extensions.CurrencyInfo.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CM.Extensions.CurrencyInfo.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CM.Extensions.CurrencyInfo.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CM.Extensions.CurrencyInfo.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CM.Extensions.CurrencyInfo.SOTaxTranCollection -> Collection(PX.Objects.SO.SOTaxTran)
PX.Objects.CM.Extensions.CurrencyInfo.POTaxTranCollection -> Collection(PX.Objects.PO.POTaxTran)
PX.Objects.CM.Extensions.CurrencyInfo.GLTaxCollection -> Collection(PX.Objects.GL.GLTax)
PX.Objects.CM.Extensions.CurrencyInfo.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CM.Extensions.CurrencyInfo.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.CM.Extensions.CurrencyInfo.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CM.Extensions.CurrencyInfo.FSAppointmentTaxCollection -> Collection(PX.Objects.FS.FSAppointmentTax)
PX.Objects.CM.Extensions.CurrencyInfo.FSServiceOrderTaxCollection -> Collection(PX.Objects.FS.FSServiceOrderTax)
PX.Objects.CM.Extensions.CurrencyInfo.SVATConversionHistCollection -> Collection(PX.Objects.TX.SVATConversionHist)
PX.Objects.CM.Extensions.CurrencyInfo.SOTaxCollection -> Collection(PX.Objects.SO.SOTax)
PX.Objects.CM.Extensions.CurrencyInfo.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CM.Extensions.CurrencyInfo.POLandedCostTaxCollection -> Collection(PX.Objects.PO.POLandedCostTax)
PX.Objects.CM.Extensions.CurrencyInfo.POLandedCostTaxTranCollection -> Collection(PX.Objects.PO.POLandedCostTaxTran)
PX.Objects.CM.Extensions.CurrencyInfo.POTaxCollection -> Collection(PX.Objects.PO.POTax)
PX.Objects.CM.Extensions.CurrencyInfo.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)
PX.Objects.CM.Extensions.CurrencyInfo.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.CM.Extensions.CurrencyInfo.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CM.Extensions.CurrencyInfo.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.CM.Extensions.CurrencyInfo.BatchCollection -> Collection(PX.Objects.GL.Batch)
PX.Objects.CM.Extensions.CurrencyInfo.CATaxCollection -> Collection(PX.Objects.CA.CATax)
PX.Objects.CM.Extensions.CurrencyInfo.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.CM.Extensions.CurrencyInfo.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CM.Extensions.CurrencyInfo.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.CM.Extensions.CurrencyInfo.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CM.Extensions.CurrencyInfo.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.CM.Extensions.CurrencyInfo.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CM.Extensions.CurrencyInfo.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.CM.Extensions.CurrencyInfo.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CM.Extensions.CurrencyInfo.ARSalesPerTranCollection -> Collection(PX.Objects.AR.ARSalesPerTran)
PX.Objects.CM.Extensions.CurrencyInfo.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CM.Extensions.CurrencyInfo.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.CM.Extensions.CurrencyInfo.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.CM.Extensions.CurrencyInfo.FSAppointmentTaxTranCollection -> Collection(PX.Objects.FS.FSAppointmentTaxTran)
PX.Objects.CM.Extensions.CurrencyInfo.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CM.Extensions.CurrencyInfo.FSServiceOrderTaxTranCollection -> Collection(PX.Objects.FS.FSServiceOrderTaxTran)
PX.Objects.CM.Extensions.CurrencyInfo.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.CM.Extensions.CurrencyInfo.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.CM.Extensions.CurrencyInfo.SVTaxCollection -> Collection(PX.Objects.SV.SVTax)
PX.Objects.CM.Extensions.CurrencyInfo.SVTaxTranCollection -> Collection(PX.Objects.SV.SVTaxTran)
PX.Objects.CM.Extensions.CurrencyInfo.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.CM.Extensions.CurrencyInfo.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.CM.Extensions.CurrencyInfo.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.CM.Extensions.CurrencyInfo.SOAdjustCollection -> Collection(PX.Objects.SO.SOAdjust)
PX.Objects.CM.Extensions.CurrencyInfo.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CM.Extensions.CurrencyInfo.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.CM.Extensions.CurrencyInfo.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.CM.Extensions.CurrencyInfo.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.CM.Extensions.CurrencyInfo.SOOrderDiscountDetailCollection -> Collection(PX.Objects.SO.SOOrderDiscountDetail)
PX.Objects.CM.Extensions.CurrencyInfo.SOSalesPerTranCollection -> Collection(PX.Objects.SO.SOSalesPerTran)
PX.Objects.CM.Extensions.CurrencyInfo.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CM.Extensions.CurrencyInfo.POLandedCostDetailCollection -> Collection(PX.Objects.PO.POLandedCostDetail)
PX.Objects.CM.Extensions.CurrencyInfo.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CM.Extensions.CurrencyInfo.POLandedCostReceiptLineCollection -> Collection(PX.Objects.PO.POLandedCostReceiptLine)
PX.Objects.CM.Extensions.CurrencyInfo.POOrderDiscountDetailCollection -> Collection(PX.Objects.PO.POOrderDiscountDetail)
PX.Objects.CM.Extensions.CurrencyInfo.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.CM.Extensions.CurrencyInfo.GLDocBatchCollection -> Collection(PX.Objects.GL.GLDocBatch)
PX.Objects.CM.Extensions.CurrencyInfo.CAAdjCollection -> Collection(PX.Objects.CA.CAAdj)
PX.Objects.CM.Extensions.CurrencyInfo.CABankTranAdjustmentCollection -> Collection(PX.Objects.CA.CABankTranAdjustment)
PX.Objects.CM.Extensions.CurrencyInfo.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.CM.Extensions.CurrencyInfo.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.CM.Extensions.CurrencyInfo.CADepositChargeCollection -> Collection(PX.Objects.CA.CADepositCharge)
PX.Objects.CM.Extensions.CurrencyInfo.CADepositDetailCollection -> Collection(PX.Objects.CA.CADepositDetail)
PX.Objects.CM.Extensions.CurrencyInfo.CAExpenseCollection -> Collection(PX.Objects.CA.CAExpense)
PX.Objects.CM.Extensions.CurrencyInfo.CAReconCollection -> Collection(PX.Objects.CA.CARecon)
PX.Objects.CM.Extensions.CurrencyInfo.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.CM.Extensions.CurrencyInfo.CATransferCollection -> Collection(PX.Objects.CA.CATransfer)
PX.Objects.CM.Extensions.CurrencyInfo.ARInvoiceDiscountDetailCollection -> Collection(PX.Objects.AR.ARInvoiceDiscountDetail)
PX.Objects.CM.Extensions.CurrencyInfo.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.CM.Extensions.CurrencyInfo.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.CM.Extensions.CurrencyInfo.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.CM.Extensions.CurrencyInfo.PRPaymentCollection -> Collection(PX.Objects.PR.PRPayment)
PX.Objects.CM.Extensions.CurrencyInfo.SVAdjustCollection -> Collection(PX.Objects.SV.SVAdjust)
PX.Objects.CM.Extensions.CurrencyInfo.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CM.Extensions.CurrencyInfo.SVOrderDiscountDetailCollection -> Collection(PX.Objects.SV.SVOrderDiscountDetail)
PX.Objects.CM.Extensions.CurrencyInfo.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CM.Extensions.CurrencyInfo.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CM.Extensions.CurrencyInfo.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.CM.Extensions.CurrencyInfo.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.CM.Extensions.CurrencyInfo.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.CM.Extensions.CurrencyInfo.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CM.Extensions.CurrencyInfo.ARTranPostGLCollection -> Collection(PX.Objects.AR.ARTranPostGL)
PX.Objects.CM.Extensions.CurrencyInfo.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.CM.Extensions.CurrencyInfo.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.CM.Extensions.CurrencyInfo.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)

# PX.Objects.CM.Extensions.CurrencyList (EntityType)

Label: "Currency"
Key: CuryID
Entity sets: PX_Objects_CM_Extensions_CurrencyList, Currency3, CurrencyList1
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CM.Extensions.CurrencyList.CuryID : Edm.String [key] "Currency ID"
PX.Objects.CM.Extensions.CurrencyList.Description : Edm.String "Description"
PX.Objects.CM.Extensions.CurrencyList.CurySymbol : Edm.String "Currency Symbol"
PX.Objects.CM.Extensions.CurrencyList.CuryCaption : Edm.String "Currency Caption"
PX.Objects.CM.Extensions.CurrencyList.DecimalPlaces : Edm.Int16 "Decimal Precision"
PX.Objects.CM.Extensions.CurrencyList.ISODecimalPlaces : Edm.Int16
PX.Objects.CM.Extensions.CurrencyList.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.Extensions.CurrencyList.CreatedByScreenID : Edm.String
PX.Objects.CM.Extensions.CurrencyList.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Extensions.CurrencyList.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.Extensions.CurrencyList.LastModifiedByScreenID : Edm.String
PX.Objects.CM.Extensions.CurrencyList.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Extensions.CurrencyList.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CM.Extensions.CurrencyList.IsFinancial : Edm.Boolean [required] "Use for Accounting"
PX.Objects.CM.Extensions.CurrencyList.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CM.Extensions.CurrencyList.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.Extensions.CurrencyList.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.Extensions.CurrencyList.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CM.Extensions.CurrencyList.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CM.Extensions.CurrencyList.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CM.Extensions.CurrencyList.FixedAssetCollection -> Collection(PX.Objects.FA.FixedAsset)
PX.Objects.CM.Extensions.CurrencyList.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CM.Extensions.CurrencyList.CurrencyRateCollection -> Collection(PX.Objects.CM.CurrencyRate)
PX.Objects.CM.Extensions.CurrencyList.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.Objects.CM.Extensions.CurrencyList.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CM.Extensions.CurrencyList.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.CM.Extensions.CurrencyList.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CM.Extensions.CurrencyList.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CM.Extensions.CurrencyList.CurrencyCollection -> Collection(PX.Objects.CM.Currency)
PX.Objects.CM.Extensions.CurrencyList.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CM.Extensions.CurrencyList.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.CM.Extensions.CurrencyList.INItemClassCurySettingsCollection -> Collection(PX.Objects.IN.INItemClassCurySettings)
PX.Objects.CM.Extensions.CurrencyList.INItemClassRepCollection -> Collection(PX.Objects.IN.INItemClassRep)
PX.Objects.CM.Extensions.CurrencyList.INItemRepCollection -> Collection(PX.Objects.IN.INItemRep)
PX.Objects.CM.Extensions.CurrencyList.INSubItemRepCollection -> Collection(PX.Objects.IN.INSubItemRep)
PX.Objects.CM.Extensions.CurrencyList.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.CM.Extensions.CurrencyList.INItemLotSerialAttributesHeaderCurySettingsCollection -> Collection(PX.Objects.IN.DAC.INItemLotSerialAttributesHeaderCurySettings)
PX.Objects.CM.Extensions.CurrencyList.CABankFeedDetailCollection -> Collection(PX.Objects.CA.CABankFeedDetail)
PX.Objects.CM.Extensions.CurrencyList.AMMachCurySettingsCollection -> Collection(PX.Objects.AM.AMMachCurySettings)
PX.Objects.CM.Extensions.CurrencyList.AMOverheadCurySettingsCollection -> Collection(PX.Objects.AM.AMOverheadCurySettings)
PX.Objects.CM.Extensions.CurrencyList.AMToolMstCurySettingsCollection -> Collection(PX.Objects.AM.AMToolMstCurySettings)
PX.Objects.CM.Extensions.CurrencyList.AMWCCurySettingsCollection -> Collection(PX.Objects.AM.AMWCCurySettings)
PX.Objects.CM.Extensions.CurrencyList.AMBomOperCuryCollection -> Collection(PX.Objects.AM.AMBomOperCury)
PX.Objects.CM.Extensions.CurrencyList.CompanyCollection -> Collection(PX.Objects.GL.Company)
PX.Objects.CM.Extensions.CurrencyList.RefreshRateCollection -> Collection(PX.Objects.CM.RefreshRate)
PX.Objects.CM.Extensions.CurrencyList.AMBomMatlCuryCollection -> Collection(PX.Objects.AM.AMBomMatlCury)
PX.Objects.CM.Extensions.CurrencyList.AMBomToolCuryCollection -> Collection(PX.Objects.AM.AMBomToolCury)
PX.Objects.CM.Extensions.CurrencyList.AMWCCuryCollection -> Collection(PX.Objects.AM.AMWCCury)
PX.Objects.CM.Extensions.CurrencyList.AMWCMachCuryCollection -> Collection(PX.Objects.AM.AMWCMachCury)
PX.Objects.CM.Extensions.CurrencyList.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CM.Extensions.CurrencyList.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.CM.Extensions.CurrencyList.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)

# PX.Objects.CM.Extensions.CurrencyRate (EntityType)

Label: "Currency Rate"
Key: CuryRateID
Entity sets: PX_Objects_CM_Extensions_CurrencyRate, CurrencyRate1

PX.Objects.CM.Extensions.CurrencyRate.CuryRateID : Edm.Int32 [key] "CuryRate ID"
PX.Objects.CM.Extensions.CurrencyRate.FromCuryID : Edm.String "From Currency"
PX.Objects.CM.Extensions.CurrencyRate.CuryRateType : Edm.String "Currency Rate Type"
PX.Objects.CM.Extensions.CurrencyRate.CuryEffDate : Edm.DateTimeOffset "Currency Effective Date"
PX.Objects.CM.Extensions.CurrencyRate.CuryMultDiv : Edm.String "Mult/Div"
PX.Objects.CM.Extensions.CurrencyRate.CuryRate : Edm.Decimal "Currency Rate"
PX.Objects.CM.Extensions.CurrencyRate.RateReciprocal : Edm.Decimal "Rate Reciprocal"
PX.Objects.CM.Extensions.CurrencyRate.ToCuryID : Edm.String "To Currency"
PX.Objects.CM.Extensions.CurrencyRate.tstamp : Edm.Binary
PX.Objects.CM.Extensions.CurrencyRate.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.Extensions.CurrencyRate.CreatedByScreenID : Edm.String
PX.Objects.CM.Extensions.CurrencyRate.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Extensions.CurrencyRate.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.Extensions.CurrencyRate.LastModifiedByScreenID : Edm.String
PX.Objects.CM.Extensions.CurrencyRate.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Extensions.CurrencyRate.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.Extensions.CurrencyRate.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.Extensions.CurrencyRate.CurrencyByFromCuryID -> PX.Objects.CM.Currency (FromCuryID=CuryID)
PX.Objects.CM.Extensions.CurrencyRate.CurrencyByToCuryID -> PX.Objects.CM.Currency (ToCuryID=CuryID)
PX.Objects.CM.Extensions.CurrencyRate.CurrencyListByFromCuryID -> PX.Objects.CM.CurrencyList (FromCuryID=CuryID)
PX.Objects.CM.Extensions.CurrencyRate.CurrencyListByToCuryID -> PX.Objects.CM.CurrencyList (ToCuryID=CuryID)
PX.Objects.CM.Extensions.CurrencyRate.CurrencyRateTypeByCuryRateType -> PX.Objects.CM.CurrencyRateType (CuryRateType=CuryRateTypeID)

# PX.Objects.CM.Extensions.CurrencyRateType (EntityType)

Label: "Currency Rate Type"
Key: CuryRateTypeID
Entity sets: PX_Objects_CM_Extensions_CurrencyRateType, CurrencyRateType1
Non-filterable, non-selectable: DeletedDatabaseRecord

PX.Objects.CM.Extensions.CurrencyRateType.CuryRateTypeID : Edm.String [key] "Rate Type ID"
PX.Objects.CM.Extensions.CurrencyRateType.Descr : Edm.String "Description"
PX.Objects.CM.Extensions.CurrencyRateType.RateEffDays : Edm.Int16 [required] "Days Effective"
PX.Objects.CM.Extensions.CurrencyRateType.RefreshOnline : Edm.Boolean [required] "Refresh Online"
PX.Objects.CM.Extensions.CurrencyRateType.OnlineRateAdjustment : Edm.Decimal "Online Rate Adjustment (%)"
PX.Objects.CM.Extensions.CurrencyRateType.tstamp : Edm.Binary
PX.Objects.CM.Extensions.CurrencyRateType.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.Extensions.CurrencyRateType.CreatedByScreenID : Edm.String
PX.Objects.CM.Extensions.CurrencyRateType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Extensions.CurrencyRateType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.Extensions.CurrencyRateType.LastModifiedByScreenID : Edm.String
PX.Objects.CM.Extensions.CurrencyRateType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.Extensions.CurrencyRateType.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CM.Extensions.CurrencyRateType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.Extensions.CurrencyRateType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.Extensions.CurrencyRateType.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CM.Extensions.CurrencyRateType.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CM.Extensions.CurrencyRateType.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CM.Extensions.CurrencyRateType.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CM.Extensions.CurrencyRateType.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CM.Extensions.CurrencyRateType.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CM.Extensions.CurrencyRateType.CurrencyRateCollection -> Collection(PX.Objects.CM.CurrencyRate)
PX.Objects.CM.Extensions.CurrencyRateType.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CM.Extensions.CurrencyRateType.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.CM.Extensions.CurrencyRateType.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.Objects.CM.Extensions.CurrencyRateType.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CM.Extensions.CurrencyRateType.AccountCollection -> Collection(PX.Objects.GL.Account)
PX.Objects.CM.Extensions.CurrencyRateType.CurrencyInfoCollection -> Collection(PX.Objects.CM.CurrencyInfo)
PX.Objects.CM.Extensions.CurrencyRateType.CMSetupCollection -> Collection(PX.Objects.CM.CMSetup)
PX.Objects.CM.Extensions.CurrencyRateType.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.CM.Extensions.CurrencyRateType.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)
PX.Objects.CM.Extensions.CurrencyRateType.ARSetupCollection -> Collection(PX.Objects.AR.ARSetup)
PX.Objects.CM.Extensions.CurrencyRateType.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CM.Extensions.CurrencyRateType.RefreshRateCollection -> Collection(PX.Objects.CM.RefreshRate)
PX.Objects.CM.Extensions.CurrencyRateType.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CM.Extensions.CurrencyRateType.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)

# PX.Objects.CM.RefreshRate (EntityType)

Key: CuryRateType, FromCuryID
Entity sets: PX_Objects_CM_RefreshRate
Non-filterable, non-selectable: OnlineRateAdjustment

PX.Objects.CM.RefreshRate.FromCuryID : Edm.String [key] "From Currency"
PX.Objects.CM.RefreshRate.CuryRateType : Edm.String [key] "Currency Rate Type"
PX.Objects.CM.RefreshRate.OnlineRateAdjustment : Edm.Decimal "Online Rate Adjustment (%)"
PX.Objects.CM.RefreshRate.CuryRate : Edm.Decimal "Currency Rate"
PX.Objects.CM.RefreshRate.NoteID : Edm.Guid
PX.Objects.CM.RefreshRate.CurrencyListByFromCuryID -> PX.Objects.CM.CurrencyList (FromCuryID=CuryID)
PX.Objects.CM.RefreshRate.CurrencyRateTypeByCuryRateType -> PX.Objects.CM.CurrencyRateType (CuryRateType=CuryRateTypeID)
PX.Objects.CM.RefreshRate.CurrencyByFromCuryID -> PX.Objects.CM.Currency (FromCuryID=CuryID)
PX.Objects.CM.RefreshRate.CurrencyByToCuryID -> PX.Objects.CM.Currency
PX.Objects.CM.RefreshRate.CurrencyListByToCuryID -> PX.Objects.CM.CurrencyList

# PX.Objects.CM.RevaluedAPHistory (EntityType)

Label: "Revalued AP History"
BaseType: PX.Objects.AP.CuryAPHistory
Key: AccountID, BranchID, CuryID, FinPeriodID, SubID, VendorID (inherited from PX.Objects.AP.CuryAPHistory)
Entity sets: PX_Objects_CM_RevaluedAPHistory, RevaluedAPHistory
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.CM.RevaluedAPHistory.CuryRateTypeID : Edm.String "Currency Rate Type"
PX.Objects.CM.RevaluedAPHistory.CuryRate : Edm.Decimal "Currency Rate"
PX.Objects.CM.RevaluedAPHistory.RateReciprocal : Edm.Decimal
PX.Objects.CM.RevaluedAPHistory.CuryEffDate : Edm.DateTimeOffset
PX.Objects.CM.RevaluedAPHistory.CuryMultDiv : Edm.String
PX.Objects.CM.RevaluedAPHistory.VendorClassID : Edm.String "Vendor Class"
PX.Objects.CM.RevaluedAPHistory.FinPrevRevalued : Edm.Decimal "PTD Gain or Loss"
PX.Objects.CM.RevaluedAPHistory.FinYtdRevalued : Edm.Decimal "Revalued Balance"
PX.Objects.CM.RevaluedAPHistory.LastRevaluedFinPeriodID : Edm.String "Last Revaluation Period"

# PX.Objects.CM.RevaluedARHistory (EntityType)

Label: "Revalued AR History"
BaseType: PX.Objects.AR.CuryARHistory
Key: AccountID, BranchID, CuryID, CustomerID, FinPeriodID, SubID (inherited from PX.Objects.AR.CuryARHistory)
Entity sets: PX_Objects_CM_RevaluedARHistory, RevaluedARHistory
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.CM.RevaluedARHistory.CuryRateTypeID : Edm.String "Currency Rate Type"
PX.Objects.CM.RevaluedARHistory.CuryRate : Edm.Decimal "Currency Rate"
PX.Objects.CM.RevaluedARHistory.RateReciprocal : Edm.Decimal
PX.Objects.CM.RevaluedARHistory.CuryMultDiv : Edm.String
PX.Objects.CM.RevaluedARHistory.CuryEffDate : Edm.DateTimeOffset
PX.Objects.CM.RevaluedARHistory.CustomerClassID : Edm.String "Customer Class"
PX.Objects.CM.RevaluedARHistory.FinPrevRevalued : Edm.Decimal "PTD Gain or Loss"
PX.Objects.CM.RevaluedARHistory.FinYtdRevalued : Edm.Decimal "Revalued Balance"
PX.Objects.CM.RevaluedARHistory.LastRevaluedFinPeriodID : Edm.String "Last Revaluation Period"

# PX.Objects.CM.RevaluedGLHistory (EntityType)

Label: "GL History"
BaseType: PX.Objects.GL.GLHistory
Key: AccountID, BranchID, FinPeriodID, LedgerID, SubID (inherited from PX.Objects.GL.GLHistory)
Entity sets: PX_Objects_CM_RevaluedGLHistory
Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)

PX.Objects.CM.RevaluedGLHistory.CuryRateTypeID : Edm.String "Currency Rate Type"
PX.Objects.CM.RevaluedGLHistory.CuryRate : Edm.Decimal "Currency Rate"
PX.Objects.CM.RevaluedGLHistory.RateReciprocal : Edm.Decimal
PX.Objects.CM.RevaluedGLHistory.CuryEffDate : Edm.DateTimeOffset
PX.Objects.CM.RevaluedGLHistory.CuryMultDiv : Edm.String
PX.Objects.CM.RevaluedGLHistory.AccountType : Edm.String "Type"
PX.Objects.CM.RevaluedGLHistory.FinYtdRevalued : Edm.Decimal "Revalued Balance"
PX.Objects.CM.RevaluedGLHistory.LastRevaluedFinPeriodID : Edm.String "Last Revaluation Period"

# PX.Objects.CM.TranslationHistory (EntityType)

Label: "Translation History"
Key: ReferenceNbr
Entity sets: PX_Objects_CM_TranslationHistory, TranslationHistory
Non-filterable, non-selectable: NoteText

PX.Objects.CM.TranslationHistory.ReferenceNbr : Edm.String [key] "Translation Number"
PX.Objects.CM.TranslationHistory.Description : Edm.String "Description"
PX.Objects.CM.TranslationHistory.TranslDefId : Edm.String "Translation ID"
PX.Objects.CM.TranslationHistory.LedgerID : Edm.Int32 "Destination Ledger"
PX.Objects.CM.TranslationHistory.DestCuryID : Edm.String "Destination Currency"
PX.Objects.CM.TranslationHistory.DateEntered : Edm.DateTimeOffset "Translation Date"
PX.Objects.CM.TranslationHistory.FinPeriodID : Edm.String "Fin. Period"
PX.Objects.CM.TranslationHistory.Status : Edm.String "Status"
PX.Objects.CM.TranslationHistory.BatchNbr : Edm.String "Translation Batch Number"
PX.Objects.CM.TranslationHistory.CuryEffDate : Edm.DateTimeOffset "Currency Effective Date"
PX.Objects.CM.TranslationHistory.DebitTot : Edm.Decimal [required] "Debit Total"
PX.Objects.CM.TranslationHistory.CreditTot : Edm.Decimal [required] "Credit Total"
PX.Objects.CM.TranslationHistory.ControlTot : Edm.Decimal [required] "Control Total"
PX.Objects.CM.TranslationHistory.Released : Edm.Boolean [required]
PX.Objects.CM.TranslationHistory.NoteID : Edm.Guid
PX.Objects.CM.TranslationHistory.NoteText : Edm.String "Note Text"
PX.Objects.CM.TranslationHistory.tstamp : Edm.Binary
PX.Objects.CM.TranslationHistory.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.TranslationHistory.CreatedByScreenID : Edm.String
PX.Objects.CM.TranslationHistory.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CM.TranslationHistory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.TranslationHistory.LastModifiedByScreenID : Edm.String
PX.Objects.CM.TranslationHistory.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CM.TranslationHistory.BatchByBatchNbr -> PX.Objects.GL.Batch (BatchNbr=BatchNbr)
PX.Objects.CM.TranslationHistory.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CM.TranslationHistory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.TranslationHistory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.TranslationHistory.CurrencyByDestCuryID -> PX.Objects.CM.Currency (DestCuryID=CuryID)
PX.Objects.CM.TranslationHistory.TranslDefByTranslDefId -> PX.Objects.CM.TranslDef (TranslDefId=TranslDefId)
PX.Objects.CM.TranslationHistory.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.CM.TranslationHistory.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)

# PX.Objects.CM.TranslationHistoryDetails (EntityType)

Label: "Translation History Detail"
Key: AccountID, BranchID, LineType, ReferenceNbr, SubID
Entity sets: PX_Objects_CM_TranslationHistoryDetails, TranslationHistoryDetail, TranslationHistoryDetails
Non-filterable, non-selectable: NoteText

PX.Objects.CM.TranslationHistoryDetails.ReferenceNbr : Edm.String [key] "Translation Number"
PX.Objects.CM.TranslationHistoryDetails.TranslDefId : Edm.String
PX.Objects.CM.TranslationHistoryDetails.LedgerID : Edm.Int32
PX.Objects.CM.TranslationHistoryDetails.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.CM.TranslationHistoryDetails.AccountID : Edm.Int32 [key] "Account"
PX.Objects.CM.TranslationHistoryDetails.SubID : Edm.Int32 [key] "Subaccount"
PX.Objects.CM.TranslationHistoryDetails.CalcMode : Edm.Int16 [required] "Translation Method"
PX.Objects.CM.TranslationHistoryDetails.SourceAmt : Edm.Decimal [required] "Source Amount"
PX.Objects.CM.TranslationHistoryDetails.TranslatedAmt : Edm.Decimal [required] "Translated Amount"
PX.Objects.CM.TranslationHistoryDetails.OrigTranslatedAmt : Edm.Decimal [required] "Orig. Translated Amount"
PX.Objects.CM.TranslationHistoryDetails.FinPeriodID : Edm.String
PX.Objects.CM.TranslationHistoryDetails.CuryID : Edm.String "Currency"
PX.Objects.CM.TranslationHistoryDetails.RateTypeID : Edm.String "Rate Type"
PX.Objects.CM.TranslationHistoryDetails.CuryMultDiv : Edm.String "Mult/Div"
PX.Objects.CM.TranslationHistoryDetails.CuryEffDate : Edm.DateTimeOffset "Currency Effective Date"
PX.Objects.CM.TranslationHistoryDetails.CuryRate : Edm.Decimal [required] "Currency Rate"
PX.Objects.CM.TranslationHistoryDetails.LineType : Edm.String [key] "Line Type"
PX.Objects.CM.TranslationHistoryDetails.BatchNbr : Edm.String "Translation Batch Number"
PX.Objects.CM.TranslationHistoryDetails.LineNbr : Edm.Int32 "Line Nbr."
PX.Objects.CM.TranslationHistoryDetails.DebitAmt : Edm.Decimal [required] "Transaction Debit Amount"
PX.Objects.CM.TranslationHistoryDetails.CreditAmt : Edm.Decimal [required] "Transaction Credit Amount"
PX.Objects.CM.TranslationHistoryDetails.NoteID : Edm.Guid
PX.Objects.CM.TranslationHistoryDetails.NoteText : Edm.String "Note Text"
PX.Objects.CM.TranslationHistoryDetails.Released : Edm.Boolean [required] "Released"
PX.Objects.CM.TranslationHistoryDetails.tstamp : Edm.Binary
PX.Objects.CM.TranslationHistoryDetails.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.TranslationHistoryDetails.CreatedByScreenID : Edm.String
PX.Objects.CM.TranslationHistoryDetails.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.TranslationHistoryDetails.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.TranslationHistoryDetails.LastModifiedByScreenID : Edm.String
PX.Objects.CM.TranslationHistoryDetails.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.TranslationHistoryDetails.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CM.TranslationHistoryDetails.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.TranslationHistoryDetails.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.TranslationHistoryDetails.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CM.TranslationHistoryDetails.CurrencyRateTypeByRateTypeID -> PX.Objects.CM.CurrencyRateType (RateTypeID=CuryRateTypeID)
PX.Objects.CM.TranslationHistoryDetails.TranslationHistoryByReferenceNbr -> PX.Objects.CM.TranslationHistory (ReferenceNbr=ReferenceNbr)
PX.Objects.CM.TranslationHistoryDetails.TranslDefByTranslDefId -> PX.Objects.CM.TranslDef (TranslDefId=TranslDefId)
PX.Objects.CM.TranslationHistoryDetails.AccountByAccountID -> PX.Objects.GL.Account (AccountID=AccountID)
PX.Objects.CM.TranslationHistoryDetails.LedgerByLedgerID -> PX.Objects.GL.Ledger (LedgerID=LedgerID)
PX.Objects.CM.TranslationHistoryDetails.SubByAccountID -> PX.Objects.GL.Sub (AccountID=SubID)
PX.Objects.CM.TranslationHistoryDetails.SubBySubID -> PX.Objects.GL.Sub (SubID=SubID)

# PX.Objects.CM.TranslDef (EntityType)

Label: "Translation Definition"
Key: TranslDefId
Entity sets: PX_Objects_CM_TranslDef, TranslationDefinition, TranslDef
Non-filterable, non-selectable: NoteText, SourceCuryID, DestCuryID

PX.Objects.CM.TranslDef.TranslDefId : Edm.String [key] "Translation ID"
PX.Objects.CM.TranslDef.Active : Edm.Boolean [required] "Active"
PX.Objects.CM.TranslDef.Description : Edm.String "Description"
PX.Objects.CM.TranslDef.SourceLedgerId : Edm.Int32 "Source Ledger ID"
PX.Objects.CM.TranslDef.DestLedgerId : Edm.Int32 "Destination Ledger ID"
PX.Objects.CM.TranslDef.LineCntr : Edm.Int32
PX.Objects.CM.TranslDef.NoteID : Edm.Guid
PX.Objects.CM.TranslDef.NoteText : Edm.String "Note Text"
PX.Objects.CM.TranslDef.SourceCuryID : Edm.String "Source Currency"
PX.Objects.CM.TranslDef.DestCuryID : Edm.String "Destination Currency"
PX.Objects.CM.TranslDef.tstamp : Edm.Binary
PX.Objects.CM.TranslDef.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.TranslDef.CreatedByScreenID : Edm.String
PX.Objects.CM.TranslDef.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.TranslDef.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.TranslDef.LastModifiedByScreenID : Edm.String
PX.Objects.CM.TranslDef.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.TranslDef.BranchByBranchID -> PX.Objects.GL.Branch
PX.Objects.CM.TranslDef.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.TranslDef.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.TranslDef.LedgerBySourceLedgerId -> PX.Objects.GL.Ledger (SourceLedgerId=LedgerID)
PX.Objects.CM.TranslDef.LedgerByDestLedgerId -> PX.Objects.GL.Ledger (DestLedgerId=LedgerID)
PX.Objects.CM.TranslDef.CMSetupCollection -> Collection(PX.Objects.CM.CMSetup)
PX.Objects.CM.TranslDef.TranslationHistoryCollection -> Collection(PX.Objects.CM.TranslationHistory)
PX.Objects.CM.TranslDef.TranslationHistoryDetailsCollection -> Collection(PX.Objects.CM.TranslationHistoryDetails)
PX.Objects.CM.TranslDef.TranslDefDetCollection -> Collection(PX.Objects.CM.TranslDefDet)

# PX.Objects.CM.TranslDefDet (EntityType)

Label: "Translation Definition Detail"
Key: LineNbr, TranslDefId
Entity sets: PX_Objects_CM_TranslDefDet, TranslationDefinitionDetail, TranslDefDet
Non-filterable, non-selectable: NoteText

PX.Objects.CM.TranslDefDet.TranslDefId : Edm.String [key]
PX.Objects.CM.TranslDefDet.LineNbr : Edm.Int32 [key]
PX.Objects.CM.TranslDefDet.CalcMode : Edm.Int16 [required] "Translation Method"
PX.Objects.CM.TranslDefDet.RateTypeId : Edm.String "Rate Type"
PX.Objects.CM.TranslDefDet.NoteID : Edm.Guid
PX.Objects.CM.TranslDefDet.NoteText : Edm.String "Note Text"
PX.Objects.CM.TranslDefDet.tstamp : Edm.Binary
PX.Objects.CM.TranslDefDet.CreatedByID : Edm.Guid "Created By"
PX.Objects.CM.TranslDefDet.CreatedByScreenID : Edm.String
PX.Objects.CM.TranslDefDet.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CM.TranslDefDet.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CM.TranslDefDet.LastModifiedByScreenID : Edm.String
PX.Objects.CM.TranslDefDet.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CM.TranslDefDet.BranchByTranslDefId -> PX.Objects.GL.Branch (TranslDefId=BranchID)
PX.Objects.CM.TranslDefDet.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CM.TranslDefDet.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CM.TranslDefDet.CurrencyRateTypeByRateTypeId -> PX.Objects.CM.CurrencyRateType (RateTypeId=CuryRateTypeID)
PX.Objects.CM.TranslDefDet.TranslDefByTranslDefId -> PX.Objects.CM.TranslDef (TranslDefId=TranslDefId)
PX.Objects.CM.TranslDefDet.AccountByAccountIdFrom -> PX.Objects.GL.Account
PX.Objects.CM.TranslDefDet.AccountByAccountIdTo -> PX.Objects.GL.Account
PX.Objects.CM.TranslDefDet.SubBySubIdFrom -> PX.Objects.GL.Sub
PX.Objects.CM.TranslDefDet.SubBySubIdTo -> PX.Objects.GL.Sub

# PX.Objects.CN.Compliance.CL.DAC.ComplianceAnswer (EntityType)

Label: "Compliance Answer"
BaseType: PX.Objects.CS.CSAnswers
Key: AttributeID, RefNoteID (inherited from PX.Objects.CS.CSAnswers)
Entity sets: PX_Objects_CN_Compliance_CL_DAC_ComplianceAnswer, ComplianceAnswer

PX.Objects.CN.Compliance.CL.DAC.ComplianceAnswer.NoteId : Edm.Guid

# PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute (EntityType)

Label: "Compliance Attribute"
Key: AttributeId
Entity sets: PX_Objects_CN_Compliance_CL_DAC_ComplianceAttribute, ComplianceAttribute
Non-filterable, non-selectable: NoteText

PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.Tstamp : Edm.Binary
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.CreatedById : Edm.Guid "Created By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.CreatedByScreenId : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.LastModifiedByScreenId : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.NoteID : Edm.Guid
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.NoteText : Edm.String "Note Text"
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.AttributeId : Edm.Int32 [key]
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.Type : Edm.Int32
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.Value : Edm.String "Value"
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.ComplianceAttributeTypeByType -> PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType (Type=ComplianceAttributeTypeID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.VendorDocumentRequirementCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement)
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)

# PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType (EntityType)

Label: "Compliance Attribute Type"
Key: ComplianceAttributeTypeID
Entity sets: PX_Objects_CN_Compliance_CL_DAC_ComplianceAttributeType, ComplianceAttributeType

PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType.ComplianceAttributeTypeID : Edm.Int32 [key]
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType.Type : Edm.String "Type"
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType.ComplianceAttributeCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute)
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType.VendorDocumentRequirementCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement)
PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)

# PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument (EntityType)

Label: "Compliance Document"
Key: ComplianceDocumentID
Entity sets: PX_Objects_CN_Compliance_CL_DAC_ComplianceDocument, ComplianceDocument
Non-filterable, non-selectable: IsExpired, NoteText, SkipInit, NewClassID

PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ComplianceDocumentID : Edm.Int32 [key] "Document Id"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.Description : Edm.String "Description"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.Required : Edm.Boolean [required] "Required"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.Received : Edm.Boolean [required] "Received from Vendor"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CreationDate : Edm.DateTimeOffset "Creation Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ReceivedDate : Edm.DateTimeOffset "Vendor Received Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.SentDate : Edm.DateTimeOffset "Sent Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.EffectiveDate : Edm.DateTimeOffset "Effective Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.Limit : Edm.Decimal "Limit"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.DocumentType : Edm.Int32 "Document Type"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.DocumentTypeValue : Edm.Int32 "Document Category"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.Status : Edm.Int32 "Status"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.MethodSent : Edm.String "Method Sent"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ProjectID : Edm.Int32 "Project"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CostCodeID : Edm.Int32 "Cost Code"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CustomerID : Edm.Int32 "Customer"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CustomerName : Edm.String "Customer Name"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.VendorID : Edm.Int32 "Vendor"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.VendorName : Edm.String "Vendor Name"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.SecondaryVendorID : Edm.Int32 "Secondary Vendor"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.SecondaryVendorName : Edm.String "Secondary Vendor Name"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PurchaseOrder : Edm.Guid "Purchase Order"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PurchaseOrderLineItem : Edm.Int32 "Purchase Order Line Item"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.Subcontract : Edm.String "Subcontract"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.SubcontractLineItem : Edm.Int32 "Subcontract Line Item"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ChangeOrderNumber : Edm.String "Change Order"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.InvoiceID : Edm.Guid "AR Invoice"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.InvoiceAmount : Edm.Decimal "AR Invoice Amount"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.BillID : Edm.Guid "Bill"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.BillAmount : Edm.Decimal "Bill Amount"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.LienWaiverAmount : Edm.Decimal "Lien Waiver Amount (Vendor)"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.SponsorOrganization : Edm.String "Sponsor Organization"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CertificateNumber : Edm.String "Certificate Number"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.InsuranceCompany : Edm.String "Insurance Company"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.Policy : Edm.String "Policy"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.InsuranceDocumentTypeId : Edm.Int32
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ApPaymentMethodID : Edm.String "AP Payment Method"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ArPaymentMethodID : Edm.String "AR Payment Method"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ApCheckID : Edm.Guid "AP Payment"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CheckNumber : Edm.String "Payment Ref."
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ArPaymentID : Edm.Guid "AR Payment"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ProjectTransactionID : Edm.Guid "Project Transaction"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ReceiptDate : Edm.DateTimeOffset "Receipt Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.DateIssued : Edm.DateTimeOffset "Date Issued"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ThroughDate : Edm.DateTimeOffset "Through Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ReceiveDate : Edm.DateTimeOffset "Receive Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PaymentDate : Edm.DateTimeOffset "Payment Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ReceivedBy : Edm.String "Received By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.SourceType : Edm.String "Source"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.IsRequiredJointCheck : Edm.Boolean [required] "Requires Joint Payment"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.JointVendorInternalId : Edm.Int32 "Joint Payee (Vendor)"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.JointVendorExternalName : Edm.String "Joint Payee"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.LinkToPayment : Edm.Boolean [required] "Link To Payment"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.JointAmount : Edm.Decimal "Joint Amount Paid"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.JointRelease : Edm.String "Joint Release"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.JointReleaseReceived : Edm.Boolean [required] "Joint Release Received"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.IsExpired : Edm.Boolean "Expired"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.IsProcessed : Edm.Boolean "Processed"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.IsVoided : Edm.Boolean "Voided"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.IsCreatedAutomatically : Edm.Boolean [required] "Created Automatically"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.LienNoticeAmount : Edm.Decimal "Lien Notice Amount"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.JointLienNoticeAmount : Edm.Decimal "Joint Lien Notice Amount"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.IsReceivedFromJointVendor : Edm.Boolean "Received from Joint Payee"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.JointReceivedDate : Edm.DateTimeOffset "Joint Payee Received Date"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.JointLienWaiverAmount : Edm.Decimal "Joint Payee Lien Waiver Amount"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.Tstamp : Edm.Binary
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CreatedById : Edm.Guid "Created By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CreatedByScreenId : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.LastModifiedByScreenId : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.NoteID : Edm.Guid
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.NoteText : Edm.String "Note Text"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.SkipInit : Edm.Boolean
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.NewClassID : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.POLineBySubcontractLineItem -> PX.Objects.PO.POLine (SubcontractLineItem=LineNbr)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.POOrderBySubcontract -> PX.Objects.PO.POOrder (Subcontract=OrderNbr)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.BAccountBySecondaryVendorID -> PX.Objects.CR.BAccount (SecondaryVendorID=BAccountID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.BAccountByJointVendorInternalId -> PX.Objects.CR.BAccount (JointVendorInternalId=BAccountID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ComplianceAttributeByDocumentType -> PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute (DocumentTypeValue=AttributeId, DocumentType=Type)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ComplianceAttributeByStatus -> PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute (Status=AttributeId)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PMChangeOrderByChangeOrderNumber -> PX.Objects.PM.PMChangeOrder (ChangeOrderNumber=RefNbr)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.AccountByAccountID -> PX.Objects.GL.Account
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PaymentMethodByApPaymentMethodID -> PX.Objects.CA.PaymentMethod (ApPaymentMethodID=PaymentMethodID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.PaymentMethodByArPaymentMethodID -> PX.Objects.CA.PaymentMethod (ArPaymentMethodID=PaymentMethodID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ComplianceAttributeTypeByDocumentType -> PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType (DocumentType=ComplianceAttributeTypeID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument.ComplianceDocumentBillCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill)

# PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill (EntityType)

Label: "Compliance Document Bill Reference"
Key: ComplianceDocumentID, DocType, LineNbr, RefNbr
Entity sets: PX_Objects_CN_Compliance_CL_DAC_ComplianceDocumentBill, ComplianceDocumentBillReference, ComplianceDocumentBill
Non-filterable, non-selectable: NoteText

PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.ComplianceDocumentID : Edm.Int32 [key] "Document ID"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.DocType : Edm.String [key] "AP Doc. Type"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.RefNbr : Edm.String [key] "AP Reference Nbr."
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.AmountPaid : Edm.Decimal "Amount Paid"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.NoteID : Edm.Guid
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.NoteText : Edm.String "Note Text"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.tstamp : Edm.Binary
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.CreatedByID : Edm.Guid "Created By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.CreatedByScreenID : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.LastModifiedByScreenID : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentBill.ComplianceDocumentByComplianceDocumentID -> PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument (ComplianceDocumentID=ComplianceDocumentID)

# PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference (EntityType)

Label: "Compliance Document Reference"
Key: ComplianceDocumentReferenceId
Entity sets: PX_Objects_CN_Compliance_CL_DAC_ComplianceDocumentReference, ComplianceDocumentReference
Non-filterable, non-selectable: NoteText

PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.Tstamp : Edm.Binary
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.CreatedByScreenId : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.LastModifiedByScreenId : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.NoteID : Edm.Guid
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.NoteText : Edm.String "Note Text"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.ComplianceDocumentReferenceId : Edm.Guid [key]
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.Type : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.ReferenceNumber : Edm.String
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.RefNoteId : Edm.Guid
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.CreatedById : Edm.Guid "Created By"
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CN.Compliance.CL.DAC.ComplianceDocumentReference.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.CN.Compliance.CL.DAC.ComplianceNotification (EntityType)

Label: "Compliance Notification"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_CN_Compliance_CL_DAC_ComplianceNotification, ComplianceNotification

# PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup (EntityType)

Label: "Compliance Preferences"
Singletons: PX_Objects_CN_Compliance_CL_DAC_LienWaiverSetup, CompliancePreferences, LienWaiverSetup

PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.Tstamp : Edm.Binary
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.CreatedById : Edm.Guid "Created By"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.CreatedByScreenId : Edm.String
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.LastModifiedByScreenId : Edm.String
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.NoteID : Edm.Guid
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.NoteText : Edm.String "Note Text"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.ShouldWarnOnBillEntry : Edm.Boolean [required] "Warn Users During AP Bill Entry"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.ShouldWarnOnPayment : Edm.Boolean [required] "Warn Users During Bill Selection for Payment"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.ShouldStopPayments : Edm.Boolean [required] "Prevent AP Bill Payment"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.ShouldGenerateConditional : Edm.Boolean [required] "Automatically Generate Lien Waivers"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.ShouldGenerateUnconditional : Edm.Boolean [required] "Automatically Generate Lien Waivers"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.GenerateWithoutCommitmentConditional : Edm.Boolean [required] "Generate for AP Documents Not Linked to Commitments"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.GenerateWithoutCommitmentUnconditional : Edm.Boolean [required] "Generate for AP Documents Not Linked to Commitments"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.GenerationEventConditional : Edm.String "Generate Lien Waivers on"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.GenerationEventUnconditional : Edm.String "Generate Lien Waivers on"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.ThroughDateSourceConditional : Edm.String "Through Date"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.ThroughDateSourceUnconditional : Edm.String "Through Date"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.GroupByConditional : Edm.String "Calculate Amount By"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.GroupByUnconditional : Edm.String "Calculate Amount By"
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CN.Compliance.CL.DAC.LienWaiverSetup.UsersByLastModifiedByID -> PX.SM.Users

# PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient (EntityType)

Label: "Lien Waiver Recipient"
Key: ProjectId, VendorClassId
Entity sets: PX_Objects_CN_Compliance_PM_DAC_LienWaiverRecipient, LienWaiverRecipient
Non-filterable, non-selectable: NoteText

PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.Tstamp : Edm.Binary
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.CreatedById : Edm.Guid "Created By"
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.CreatedByScreenId : Edm.String
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.LastModifiedByScreenId : Edm.String
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.NoteID : Edm.Guid
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.NoteText : Edm.String "Note Text"
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.LienWaiverRecipientId : Edm.Int32
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.ProjectId : Edm.Int32 [key]
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.VendorClassId : Edm.String [key] "Vendor Class"
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.MinimumCommitmentAmount : Edm.Decimal "Minimum Commitment Amount"
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.PMProjectByProjectId -> PX.Objects.PM.PMProject (ProjectId=ContractID)
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.UsersByCreatedByID -> PX.SM.Users
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient.VendorClassByVendorClassId -> PX.Objects.AP.VendorClass (VendorClassId=VendorClassID)

# PX.Objects.CN.CRM.CR.DAC.MultipleQuote (EntityType)

Label: "Multiple Customers"
Key: MultipleQuoteID
Entity sets: PX_Objects_CN_CRM_CR_DAC_MultipleQuote, MultipleCustomers, MultipleQuote
Non-filterable, non-selectable: Tstamp, CreatedByScreenId, CreatedDateTime, LastModifiedByScreenId, LastModifiedDateTime, NoteID, NoteText, GrossMarginAbsolute, GrossMarginPercentage, FinalGrossMarginAbsolute, FinalGrossMarginPercentage

PX.Objects.CN.CRM.CR.DAC.MultipleQuote.Tstamp : Edm.Binary
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.CreatedByScreenId : Edm.String
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.LastModifiedByScreenId : Edm.String
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.NoteID : Edm.Guid
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.NoteText : Edm.String "Note Text"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.MultipleQuoteID : Edm.Int32 [key]
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.OpportunityID : Edm.String
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.BusinessAccountID : Edm.Int32 "Business Account"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.ContactID : Edm.Int32 "Contact"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.QuotedAmount : Edm.Decimal [required] "Quoted Amount"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.CostEstimate : Edm.Decimal [required] "Cost Estimate"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.GrossMarginAbsolute : Edm.Decimal "Gross Margin"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.GrossMarginPercentage : Edm.Decimal "Gross Margin, %"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.QuotedOn : Edm.DateTimeOffset "Quoted On"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.IsSelected : Edm.Boolean "Selected"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.FinalAmount : Edm.Decimal "Final Amount"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.FinalGrossMarginAbsolute : Edm.Decimal "Final Gross Margin"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.FinalGrossMarginPercentage : Edm.Decimal "Final Gross Margin, %"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.CreatedById : Edm.Guid "Created By"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.LastModifiedById : Edm.Guid "Last Modified By"
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.BAccountByBusinessAccountID -> PX.Objects.CR.BAccount (BusinessAccountID=BAccountID)
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.UsersByCreatedById -> PX.SM.Users (CreatedById=PKID)
PX.Objects.CN.CRM.CR.DAC.MultipleQuote.UsersByLastModifiedById -> PX.SM.Users (LastModifiedById=PKID)

# PX.Objects.CN.JointChecks.JointPayee (EntityType)

Label: "Joint Payee"
Key: JointPayeeId
Entity sets: PX_Objects_CN_JointChecks_JointPayee, JointPayee
Non-filterable, non-selectable: BillLineAmount, CanDelete, NoteText

PX.Objects.CN.JointChecks.JointPayee.JointPayeeId : Edm.Int32 [key]
PX.Objects.CN.JointChecks.JointPayee.IsMainPayee : Edm.Boolean [required]
PX.Objects.CN.JointChecks.JointPayee.JointPayeeInternalId : Edm.Int32 "Joint Payee (Vendor)"
PX.Objects.CN.JointChecks.JointPayee.JointPayeeExternalName : Edm.String "Joint Payee"
PX.Objects.CN.JointChecks.JointPayee.CuryInfoID : Edm.Int64
PX.Objects.CN.JointChecks.JointPayee.CuryJointAmountOwed : Edm.Decimal "Joint Amount Owed"
PX.Objects.CN.JointChecks.JointPayee.JointAmountOwed : Edm.Decimal
PX.Objects.CN.JointChecks.JointPayee.CuryJointAmountPaid : Edm.Decimal "Joint Amount Paid"
PX.Objects.CN.JointChecks.JointPayee.JointAmountPaid : Edm.Decimal
PX.Objects.CN.JointChecks.JointPayee.CuryJointBalance : Edm.Decimal "Joint Balance"
PX.Objects.CN.JointChecks.JointPayee.JointBalance : Edm.Decimal
PX.Objects.CN.JointChecks.JointPayee.APDocType : Edm.String
PX.Objects.CN.JointChecks.JointPayee.APRefNbr : Edm.String
PX.Objects.CN.JointChecks.JointPayee.APLineNbr : Edm.Int32 "Bill Line Nbr."
PX.Objects.CN.JointChecks.JointPayee.BillLineAmount : Edm.Decimal "Bill Line Amount"
PX.Objects.CN.JointChecks.JointPayee.LinkedToPayment : Edm.Boolean [required]
PX.Objects.CN.JointChecks.JointPayee.CanDelete : Edm.Boolean
PX.Objects.CN.JointChecks.JointPayee.NoteID : Edm.Guid
PX.Objects.CN.JointChecks.JointPayee.NoteText : Edm.String "Note Text"
PX.Objects.CN.JointChecks.JointPayee.tstamp : Edm.Binary
PX.Objects.CN.JointChecks.JointPayee.CreatedByID : Edm.Guid "Created By"
PX.Objects.CN.JointChecks.JointPayee.CreatedByScreenID : Edm.String
PX.Objects.CN.JointChecks.JointPayee.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CN.JointChecks.JointPayee.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CN.JointChecks.JointPayee.LastModifiedByScreenID : Edm.String
PX.Objects.CN.JointChecks.JointPayee.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CN.JointChecks.JointPayee.BAccountByJointPayeeInternalId -> PX.Objects.CR.BAccount (JointPayeeInternalId=BAccountID)
PX.Objects.CN.JointChecks.JointPayee.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CN.JointChecks.JointPayee.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CN.JointChecks.JointPayee.APTranByAPLineNbr -> PX.Objects.AP.APTran (APLineNbr=LineNbr)
PX.Objects.CN.JointChecks.JointPayee.JointPayeePaymentCollection -> Collection(PX.Objects.CN.JointChecks.JointPayeePayment)

# PX.Objects.CN.JointChecks.JointPayeePayment (EntityType)

Label: "Joint Payee Payment"
Key: JointPayeePaymentId
Entity sets: PX_Objects_CN_JointChecks_JointPayeePayment, JointPayeePayment
Non-filterable, non-selectable: BillLineNumber, NoteText

PX.Objects.CN.JointChecks.JointPayeePayment.JointPayeePaymentId : Edm.Int32 [key]
PX.Objects.CN.JointChecks.JointPayeePayment.JointPayeeId : Edm.Int32
PX.Objects.CN.JointChecks.JointPayeePayment.BillLineNumber : Edm.Int32 "Bill Line Nbr."
PX.Objects.CN.JointChecks.JointPayeePayment.PaymentRefNbr : Edm.String
PX.Objects.CN.JointChecks.JointPayeePayment.PaymentDocType : Edm.String
PX.Objects.CN.JointChecks.JointPayeePayment.InvoiceRefNbr : Edm.String "AP Bill Nbr."
PX.Objects.CN.JointChecks.JointPayeePayment.InvoiceDocType : Edm.String
PX.Objects.CN.JointChecks.JointPayeePayment.AdjustmentNumber : Edm.Int32
PX.Objects.CN.JointChecks.JointPayeePayment.CuryJointAmountToPay : Edm.Decimal "Joint Amount To Pay"
PX.Objects.CN.JointChecks.JointPayeePayment.JointAmountToPay : Edm.Decimal
PX.Objects.CN.JointChecks.JointPayeePayment.IsVoided : Edm.Boolean [required]
PX.Objects.CN.JointChecks.JointPayeePayment.NoteID : Edm.Guid
PX.Objects.CN.JointChecks.JointPayeePayment.NoteText : Edm.String "Note Text"
PX.Objects.CN.JointChecks.JointPayeePayment.tstamp : Edm.Binary
PX.Objects.CN.JointChecks.JointPayeePayment.CreatedByID : Edm.Guid "Created By"
PX.Objects.CN.JointChecks.JointPayeePayment.CreatedByScreenID : Edm.String
PX.Objects.CN.JointChecks.JointPayeePayment.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CN.JointChecks.JointPayeePayment.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CN.JointChecks.JointPayeePayment.LastModifiedByScreenID : Edm.String
PX.Objects.CN.JointChecks.JointPayeePayment.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CN.JointChecks.JointPayeePayment.APInvoiceByInvoiceRefNbr -> PX.Objects.AP.APInvoice (InvoiceRefNbr=RefNbr)
PX.Objects.CN.JointChecks.JointPayeePayment.APPaymentByPaymentRefNbr -> PX.Objects.AP.APPayment (PaymentDocType=DocType, PaymentRefNbr=RefNbr)
PX.Objects.CN.JointChecks.JointPayeePayment.JointPayeeByJointPayeeId -> PX.Objects.CN.JointChecks.JointPayee (JointPayeeId=JointPayeeId)
PX.Objects.CN.JointChecks.JointPayeePayment.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CN.JointChecks.JointPayeePayment.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CN.PMReportProject (EntityType)

Label: "PM Report Project"
Key: BaseType, ContractCD
Entity sets: PX_Objects_CN_PMReportProject, PMReportProject

PX.Objects.CN.PMReportProject.ContractID : Edm.Int32
PX.Objects.CN.PMReportProject.BaseType : Edm.String [key]
PX.Objects.CN.PMReportProject.ContractCD : Edm.String [key]
PX.Objects.CN.PMReportProject.Description : Edm.String
PX.Objects.CN.PMReportProject.DefaultBranchID : Edm.Int32 "Branch"
PX.Objects.CN.PMReportProject.Status : Edm.String
PX.Objects.CN.PMReportProject.StartDate : Edm.DateTimeOffset
PX.Objects.CN.PMReportProject.ExpireDate : Edm.DateTimeOffset
PX.Objects.CN.PMReportProject.IsActive : Edm.Boolean
PX.Objects.CN.PMReportProject.IsCompleted : Edm.Boolean
PX.Objects.CN.PMReportProject.IsCancelled : Edm.Boolean
PX.Objects.CN.PMReportProject.NonProject : Edm.Boolean
PX.Objects.CN.PMReportProject.CuryID : Edm.String
PX.Objects.CN.PMReportProject.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList
PX.Objects.CN.PMReportProject.CurrencyListByCuryID -> PX.Objects.CM.CurrencyList (CuryID=CuryID)
PX.Objects.CN.PMReportProject.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.CN.PMReportProject.ARInvoiceExtCollection -> Collection(PX.Objects.AR.ARInvoiceExt)
PX.Objects.CN.PMReportProject.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.CN.PMReportProject.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CN.PMReportProject.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CN.PMReportProject.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CN.PMReportProject.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.CN.PMReportProject.APInvoiceExtCollection -> Collection(PX.Objects.AP.APInvoiceExt)
PX.Objects.CN.PMReportProject.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CN.PMReportProject.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.CN.PMReportProject.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.Objects.CN.PMReportProject.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CN.PMReportProject.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.Objects.CN.PMReportProject.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CN.PMReportProject.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.CN.PMReportProject.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CN.PMReportProject.PMBudgetCollection -> Collection(PX.Objects.PM.PMBudget)
PX.Objects.CN.PMReportProject.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.CN.PMReportProject.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.CN.PMReportProject.PMProgressWorksheetLineCollection -> Collection(PX.Objects.PM.PMProgressWorksheetLine)
PX.Objects.CN.PMReportProject.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.CN.PMReportProject.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.CN.PMReportProject.LienWaiverRecipientCollection -> Collection(PX.Objects.CN.Compliance.PM.DAC.LienWaiverRecipient)
PX.Objects.CN.PMReportProject.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.CN.PMReportProject.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CN.PMReportProject.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.CN.PMReportProject.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.Objects.CN.PMReportProject.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CN.PMReportProject.DRScheduleDetailCollection -> Collection(PX.Objects.DR.DRScheduleDetail)
PX.Objects.CN.PMReportProject.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CN.PMReportProject.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.CN.PMReportProject.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.CN.PMReportProject.AMMTranCollection -> Collection(PX.Objects.AM.AMMTran)
PX.Objects.CN.PMReportProject.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CN.PMReportProject.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.CN.PMReportProject.FSScheduleCollection -> Collection(PX.Objects.FS.FSSchedule)
PX.Objects.CN.PMReportProject.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.CN.PMReportProject.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CN.PMReportProject.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.CN.PMReportProject.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.CN.PMReportProject.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.CN.PMReportProject.PhotoLogCollection -> Collection(PX.Objects.PJ.PhotoLogs.PJ.DAC.PhotoLog)
PX.Objects.CN.PMReportProject.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.CN.PMReportProject.EPEquipmentDetailCollection -> Collection(PX.Objects.EP.EPEquipmentDetail)
PX.Objects.CN.PMReportProject.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.CN.PMReportProject.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.CN.PMReportProject.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.CN.PMReportProject.PMForecastDetailCollection -> Collection(PX.Objects.PM.PMForecastDetail)
PX.Objects.CN.PMReportProject.PMSetupCollection -> Collection(PX.Objects.PM.PMSetup)
PX.Objects.CN.PMReportProject.PMCommitmentCollection -> Collection(PX.Objects.PM.PMCommitment)
PX.Objects.CN.PMReportProject.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.CN.PMReportProject.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.Objects.CN.PMReportProject.PMRecurringItemCollection -> Collection(PX.Objects.PM.PMRecurringItem)
PX.Objects.CN.PMReportProject.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CN.PMReportProject.EPTimeCardItemCollection -> Collection(PX.Objects.EP.EPTimeCardItem)
PX.Objects.CN.PMReportProject.PRBenefitDetailCollection -> Collection(PX.Objects.PR.PRBenefitDetail)
PX.Objects.CN.PMReportProject.PRTaxDetailCollection -> Collection(PX.Objects.PR.PRTaxDetail)
PX.Objects.CN.PMReportProject.PREarningDetailCollection -> Collection(PX.Objects.PR.PREarningDetail)
PX.Objects.CN.PMReportProject.SOFreightDetailCollection -> Collection(PX.Objects.SO.SOFreightDetail)
PX.Objects.CN.PMReportProject.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.CN.PMReportProject.SOShipLineCollection -> Collection(PX.Objects.SO.SOShipLine)
PX.Objects.CN.PMReportProject.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CN.PMReportProject.PMAccountTaskCollection -> Collection(PX.Objects.PM.PMAccountTask)
PX.Objects.CN.PMReportProject.PMAllocationDetailCollection -> Collection(PX.Objects.PM.PMAllocationDetail)
PX.Objects.CN.PMReportProject.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)
PX.Objects.CN.PMReportProject.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.CN.PMReportProject.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.CN.PMReportProject.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.Objects.CN.PMReportProject.PMCostProjectionByDateLineCollection -> Collection(PX.Objects.PM.PMCostProjectionByDateLine)
PX.Objects.CN.PMReportProject.PMCostProjectionLineCollection -> Collection(PX.Objects.PM.PMCostProjectionLine)
PX.Objects.CN.PMReportProject.PMForecastCollection -> Collection(PX.Objects.PM.PMForecast)
PX.Objects.CN.PMReportProject.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.CN.PMReportProject.PMMarkupCollection -> Collection(PX.Objects.PM.PMMarkup)
PX.Objects.CN.PMReportProject.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CN.PMReportProject.PMProgressWorksheetCollection -> Collection(PX.Objects.PM.PMProgressWorksheet)
PX.Objects.CN.PMReportProject.PMProjectBudgetHistoryCollection -> Collection(PX.Objects.PM.PMProjectBudgetHistory)
PX.Objects.CN.PMReportProject.PMProjectCostSpreadLineCollection -> Collection(PX.Objects.PM.PMProjectCostSpreadLine)
PX.Objects.CN.PMReportProject.PMRetainageStepCollection -> Collection(PX.Objects.PM.PMRetainageStep)
PX.Objects.CN.PMReportProject.PMWipAdjustmentLineCollection -> Collection(PX.Objects.PM.PMWipAdjustmentLine)
PX.Objects.CN.PMReportProject.PMWorkCodeProjectTaskSourceCollection -> Collection(PX.Objects.PM.PMWorkCodeProjectTaskSource)
PX.Objects.CN.PMReportProject.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.CN.PMReportProject.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.CN.PMReportProject.INCostCenterCollection -> Collection(PX.Objects.IN.INCostCenter)
PX.Objects.CN.PMReportProject.INLocationCollection -> Collection(PX.Objects.IN.INLocation)
PX.Objects.CN.PMReportProject.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.CN.PMReportProject.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.CN.PMReportProject.CASplitCollection -> Collection(PX.Objects.CA.CASplit)
PX.Objects.CN.PMReportProject.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.Objects.CN.PMReportProject.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CN.PMReportProject.ARPaymentChargeTranCollection -> Collection(PX.Objects.AR.ARPaymentChargeTran)
PX.Objects.CN.PMReportProject.EPEarningTypeCollection -> Collection(PX.Objects.EP.EPEarningType)
PX.Objects.CN.PMReportProject.EPEquipmentRateCollection -> Collection(PX.Objects.EP.EPEquipmentRate)
PX.Objects.CN.PMReportProject.EPEquipmentSummaryCollection -> Collection(PX.Objects.EP.EPEquipmentSummary)
PX.Objects.CN.PMReportProject.AMClockItemCollection -> Collection(PX.Objects.AM.AMClockItem)
PX.Objects.CN.PMReportProject.AMClockTranCollection -> Collection(PX.Objects.AM.AMClockTran)
PX.Objects.CN.PMReportProject.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.CN.PMReportProject.AMVendorShipLineCollection -> Collection(PX.Objects.AM.AMVendorShipLine)
PX.Objects.CN.PMReportProject.AMWrkMatlCollection -> Collection(PX.Objects.AM.AMWrkMatl)
PX.Objects.CN.PMReportProject.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.CN.PMReportProject.FSContractForecastDetCollection -> Collection(PX.Objects.FS.FSContractForecastDet)
PX.Objects.CN.PMReportProject.FSScheduleDetCollection -> Collection(PX.Objects.FS.FSScheduleDet)
PX.Objects.CN.PMReportProject.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.CN.PMReportProject.PRDeductionAndBenefitProjectPackageCollection -> Collection(PX.Objects.PR.PRDeductionAndBenefitProjectPackage)
PX.Objects.CN.PMReportProject.PROvertimeRuleCollection -> Collection(PX.Objects.PR.PROvertimeRule)
PX.Objects.CN.PMReportProject.PRPaymentFringeBenefitCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefit)
PX.Objects.CN.PMReportProject.PRPaymentFringeBenefitDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeBenefitDecreasingRate)
PX.Objects.CN.PMReportProject.PRPaymentFringeEarningDecreasingRateCollection -> Collection(PX.Objects.PR.PRPaymentFringeEarningDecreasingRate)
PX.Objects.CN.PMReportProject.PRPaymentProjectPackageDeductCollection -> Collection(PX.Objects.PR.PRPaymentProjectPackageDeduct)
PX.Objects.CN.PMReportProject.PRProjectFringeBenefitRateCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRate)
PX.Objects.CN.PMReportProject.PRProjectFringeBenefitRateReducingDeductCollection -> Collection(PX.Objects.PR.PRProjectFringeBenefitRateReducingDeduct)
PX.Objects.CN.PMReportProject.PRPTODetailCollection -> Collection(PX.Objects.PR.PRPTODetail)
PX.Objects.CN.PMReportProject.SVOrderDetailCollection -> Collection(PX.Objects.SV.SVOrderDetail)
PX.Objects.CN.PMReportProject.FSContractPeriodDetCollection -> Collection(PX.Objects.FS.FSContractPeriodDet)
PX.Objects.CN.PMReportProject.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CN.PMReportProject.INKitRegisterCollection -> Collection(PX.Objects.IN.INKitRegister)
PX.Objects.CN.PMReportProject.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CN.PMReportProject.POLineRSCollection -> Collection(PX.Objects.PO.POLineRS)
PX.Objects.CN.PMReportProject.POLineSCollection -> Collection(PX.Objects.PO.POLineS)
PX.Objects.CN.PMReportProject.POReceiptLineSCollection -> Collection(PX.Objects.PO.POReceiptLineS)
PX.Objects.CN.PMReportProject.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CN.PMReportProject.ProjectARTranCollection -> Collection(PX.Objects.PM.ProjectARTran)
PX.Objects.CN.PMReportProject.RMDataSourceCollection -> Collection(PX.CS.RMDataSource)
PX.Objects.CN.PMReportProject.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.CN.PMReportProject.DRExpenseBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRExpenseBalanceByPeriod)
PX.Objects.CN.PMReportProject.DRExpenseProjectionCollection -> Collection(PX.Objects.DR.DRExpenseProjection)
PX.Objects.CN.PMReportProject.DRRevenueBalanceByPeriodCollection -> Collection(PX.Objects.DR.DRRevenueBalanceByPeriod)
PX.Objects.CN.PMReportProject.DRRevenueProjectionCollection -> Collection(PX.Objects.DR.DRRevenueProjection)
PX.Objects.CN.PMReportProject.INOverheadTranCollection -> Collection(PX.Objects.IN.INOverheadTran)
PX.Objects.CN.PMReportProject.PMProgressLineTotalCollection -> Collection(PX.Objects.PM.PMProgressLineTotal)
PX.Objects.CN.PMReportProject.PMProjectRateCollection -> Collection(PX.Objects.PM.PMProjectRate)
PX.Objects.CN.PMReportProject.PMProjectUnionCollection -> Collection(PX.Objects.PM.PMProjectUnion)
PX.Objects.CN.PMReportProject.PMHistoryByDateCollection -> Collection(PX.Objects.PM.PMHistoryByDate)
PX.Objects.CN.PMReportProject.ProjectPMTranCollection -> Collection(PX.Objects.PM.ProjectPMTran)
PX.Objects.CN.PMReportProject.ProjectGLTranCollection -> Collection(PX.Objects.PM.ProjectGLTran)
PX.Objects.CN.PMReportProject.ProjectAPTranCollection -> Collection(PX.Objects.PM.ProjectAPTran)
PX.Objects.CN.PMReportProject.ProjectINTranCollection -> Collection(PX.Objects.PM.ProjectINTran)
PX.Objects.CN.PMReportProject.ProjectCASplitCollection -> Collection(PX.Objects.PM.ProjectCASplit)
PX.Objects.CN.PMReportProject.ContactForCurrentProjectCollection -> Collection(PX.Objects.PJ.Common.DAC.ContactForCurrentProject)
PX.Objects.CN.PMReportProject.PMMaterialListCollection -> Collection(PX.Objects.PM.MaterialManagement.MaterialList.PMMaterialList)
PX.Objects.CN.PMReportProject.DRExpenseBalanceCollection -> Collection(PX.Objects.DR.DRExpenseBalance)
PX.Objects.CN.PMReportProject.DRExpenseBalance2Collection -> Collection(PX.Objects.DR.DRExpenseBalance2)
PX.Objects.CN.PMReportProject.DRRevenueBalanceCollection -> Collection(PX.Objects.DR.DRRevenueBalance)
PX.Objects.CN.PMReportProject.DRRevenueBalance2Collection -> Collection(PX.Objects.DR.DRRevenueBalance2)

# PX.Objects.CN.PMSubAuditReportChangeOrderLine (EntityType)

Label: "PM Subcontract Audit Report Change Order Line"
Key: LineNbr, OrderNbr
Entity sets: PX_Objects_CN_PMSubAuditReportChangeOrderLine, PMSubcontractAuditReportChangeOrderLine, PMSubAuditReportChangeOrderLine

PX.Objects.CN.PMSubAuditReportChangeOrderLine.OrderNbr : Edm.String [key]
PX.Objects.CN.PMSubAuditReportChangeOrderLine.LineNbr : Edm.Int32 [key]
PX.Objects.CN.PMSubAuditReportChangeOrderLine.Date : Edm.DateTimeOffset
PX.Objects.CN.PMSubAuditReportChangeOrderLine.ChangeOrderQty : Edm.Decimal
PX.Objects.CN.PMSubAuditReportChangeOrderLine.ChangeOrderAmount : Edm.Decimal
PX.Objects.CN.PMSubAuditReportChangeOrderLine.ChangeOrderRetainage : Edm.Decimal
PX.Objects.CN.PMSubAuditReportChangeOrderLine.POOrderByOrderNbr -> PX.Objects.PO.POOrder (OrderNbr=OrderNbr)
PX.Objects.CN.PMSubAuditReportChangeOrderLine.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)

# PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract (EntityType)

Label: "PM Subcontract Audit Report Retainage Not Linked to Subcontract"
Key: DocType, RefNbr
Entity sets: PX_Objects_CN_PMSubAuditReportRetainageNotLinkedToSubcontract, PMSubcontractAuditReportRetainageNotLinkedtoSubcontract, PMSubAuditReportRetainageNotLinkedToSubcontract

PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.RefNbr : Edm.String [key]
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.DocType : Edm.String [key]
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APPaymentChargeTranCollection -> Collection(PX.Objects.AP.APPaymentChargeTran)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APTranPostGLCollection -> Collection(PX.Objects.AP.APTranPostGL)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.ARTaxCollection -> Collection(PX.Objects.AR.ARTax)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APTaxCollection -> Collection(PX.Objects.AP.APTax)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.POOrderPrepaymentCollection -> Collection(PX.Objects.PO.POOrderPrepayment)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APInvoiceDiscountDetailCollection -> Collection(PX.Objects.AP.APInvoiceDiscountDetail)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.PPExternalTranCollection -> Collection(PX.PaymentProcessor.ProcessorBase.DAC.PPExternalTran)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.PPBillcomBillCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomBill)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.PPAvidChildPaymentCollection -> Collection(PX.PaymentProcessor.AvidXchange.DAC.PPAvidChildPayment)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.POBlanketOrderAPDocCollection -> Collection(PX.Objects.PO.DAC.Projections.POBlanketOrderAPDoc)
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontract.APTranPostGLwithLinesCollection -> Collection(PX.Objects.AP.APTranPostGLwithLines)

# PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontractGrouped (ComplexType)


PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontractGrouped.RefNbr : Edm.String
PX.Objects.CN.PMSubAuditReportRetainageNotLinkedToSubcontractGrouped.DocType : Edm.String

# PX.Objects.CN.PMSubAuditReportUnappliedPrepayments (EntityType)

Label: "PM Subcontract Audit Report Unapplied Prepayments"
Key: PONbr, RefNbr
Entity sets: PX_Objects_CN_PMSubAuditReportUnappliedPrepayments, PMSubcontractAuditReportUnappliedPrepayments, PMSubAuditReportUnappliedPrepayments

PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.PONbr : Edm.String [key]
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.RefNbr : Edm.String [key]
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.ProjectID : Edm.Int32
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.VendorID : Edm.Int32
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.Description : Edm.String
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.TranType : Edm.String
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.Date : Edm.DateTimeOffset
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.CuryAmount : Edm.Decimal
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.APInvoiceByRefNbr -> PX.Objects.AP.APInvoice (TranType=DocType, RefNbr=RefNbr)
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.APPaymentByRefNbr -> PX.Objects.AP.APPayment (TranType=DocType, RefNbr=RefNbr)
PX.Objects.CN.PMSubAuditReportUnappliedPrepayments.APRegisterByRefNbr -> PX.Objects.AP.APRegister (TranType=DocType, RefNbr=RefNbr)

# PX.Objects.CN.PMWipBudget (EntityType)

Label: "PM WIP Budget"
Key: AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_CN_PMWipBudget, PMWIPBudget

PX.Objects.CN.PMWipBudget.ProjectID : Edm.Int32 [key]
PX.Objects.CN.PMWipBudget.ProjectTaskID : Edm.Int32 [key]
PX.Objects.CN.PMWipBudget.CostCodeID : Edm.Int32 [key]
PX.Objects.CN.PMWipBudget.AccountGroupID : Edm.Int32 [key]
PX.Objects.CN.PMWipBudget.InventoryID : Edm.Int32 [key]
PX.Objects.CN.PMWipBudget.Type : Edm.String
PX.Objects.CN.PMWipBudget.CuryAmount : Edm.Decimal
PX.Objects.CN.PMWipBudget.OriginalContractAmount : Edm.Decimal
PX.Objects.CN.PMWipBudget.OriginalCostAmount : Edm.Decimal
PX.Objects.CN.PMWipBudget.CuryChangeOrderAmount : Edm.Decimal
PX.Objects.CN.PMWipBudget.ChangeOrderContractAmount : Edm.Decimal
PX.Objects.CN.PMWipBudget.ChangeOrderCostAmount : Edm.Decimal
PX.Objects.CN.PMWipBudget.CuryCostToComplete : Edm.Decimal
PX.Objects.CN.PMWipBudget.CostToComplete : Edm.Decimal
PX.Objects.CN.PMWipBudget.CostProjectionCostAtCompletion : Edm.Decimal
PX.Objects.CN.PMWipBudget.CostProjectionCostToComplete : Edm.Decimal
PX.Objects.CN.PMWipBudget.CuryCommittedOrigAmount : Edm.Decimal
PX.Objects.CN.PMWipBudget.CuryCommittedCOAmount : Edm.Decimal
PX.Objects.CN.PMWipBudget.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.PMWipBudget.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.CN.PMWipBudget.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.CN.PMWipBudget.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.CN.PMWipBudget.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.CN.PMWipBudget.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.CN.PMWipBudget.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)

# PX.Objects.CN.PMWipChangeOrder (EntityType)

Label: "PM WIP Change Order"
Key: RefNbr
Entity sets: PX_Objects_CN_PMWipChangeOrder, PMWIPChangeOrder

PX.Objects.CN.PMWipChangeOrder.RefNbr : Edm.String [key]
PX.Objects.CN.PMWipChangeOrder.ProjectID : Edm.Int32
PX.Objects.CN.PMWipChangeOrder.Approved : Edm.Boolean
PX.Objects.CN.PMWipChangeOrder.Released : Edm.Boolean
PX.Objects.CN.PMWipChangeOrder.Date : Edm.DateTimeOffset
PX.Objects.CN.PMWipChangeOrder.CompletionDate : Edm.DateTimeOffset
PX.Objects.CN.PMWipChangeOrder.CostTotal : Edm.Decimal
PX.Objects.CN.PMWipChangeOrder.RevenueTotal : Edm.Decimal
PX.Objects.CN.PMWipChangeOrder.CommitmentTotal : Edm.Decimal
PX.Objects.CN.PMWipChangeOrder.Status : Edm.String
PX.Objects.CN.PMWipChangeOrder.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.PMWipChangeOrder.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)
PX.Objects.CN.PMWipChangeOrder.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.CN.PMWipChangeOrder.PMChangeOrderTaxTranCollection -> Collection(PX.Objects.PM.PMChangeOrderTaxTran)
PX.Objects.CN.PMWipChangeOrder.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.CN.PMWipChangeOrder.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.CN.PMWipChangeOrder.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.CN.PMWipChangeOrder.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.CN.PMWipChangeOrder.DailyFieldReportChangeOrderCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder)

# PX.Objects.CN.PMWipChangeOrderBudget (EntityType)

Label: "PM WIP Change Order Budget"
Key: AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID, RefNbr
Entity sets: PX_Objects_CN_PMWipChangeOrderBudget, PMWIPChangeOrderBudget

PX.Objects.CN.PMWipChangeOrderBudget.RefNbr : Edm.String [key]
PX.Objects.CN.PMWipChangeOrderBudget.ProjectID : Edm.Int32 [key]
PX.Objects.CN.PMWipChangeOrderBudget.ProjectTaskID : Edm.Int32 [key]
PX.Objects.CN.PMWipChangeOrderBudget.CostCodeID : Edm.Int32 [key]
PX.Objects.CN.PMWipChangeOrderBudget.AccountGroupID : Edm.Int32 [key]
PX.Objects.CN.PMWipChangeOrderBudget.InventoryID : Edm.Int32 [key]
PX.Objects.CN.PMWipChangeOrderBudget.Type : Edm.String
PX.Objects.CN.PMWipChangeOrderBudget.Date : Edm.DateTimeOffset
PX.Objects.CN.PMWipChangeOrderBudget.CompletionDate : Edm.DateTimeOffset
PX.Objects.CN.PMWipChangeOrderBudget.ContractAmount : Edm.Decimal
PX.Objects.CN.PMWipChangeOrderBudget.CostAmount : Edm.Decimal
PX.Objects.CN.PMWipChangeOrderBudget.Status : Edm.String
PX.Objects.CN.PMWipChangeOrderBudget.PMProjectByRefNbr -> PX.Objects.PM.PMProject (RefNbr=ContractID)
PX.Objects.CN.PMWipChangeOrderBudget.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.PMWipChangeOrderBudget.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.CN.PMWipChangeOrderBudget.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.CN.PMWipChangeOrderBudget.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.CN.PMWipChangeOrderBudget.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.CN.PMWipChangeOrderBudget.PMChangeOrderByRefNbr -> PX.Objects.PM.PMChangeOrder (RefNbr=RefNbr)
PX.Objects.CN.PMWipChangeOrderBudget.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)

# PX.Objects.CN.PMWipChangeOrderLine (EntityType)

Label: "PM WIP Change Order Line"
Key: LineNbr, RefNbr
Entity sets: PX_Objects_CN_PMWipChangeOrderLine, PMWIPChangeOrderLine

PX.Objects.CN.PMWipChangeOrderLine.RefNbr : Edm.String [key]
PX.Objects.CN.PMWipChangeOrderLine.LineNbr : Edm.Int32 [key]
PX.Objects.CN.PMWipChangeOrderLine.Status : Edm.String
PX.Objects.CN.PMWipChangeOrderLine.Approved : Edm.Boolean
PX.Objects.CN.PMWipChangeOrderLine.Released : Edm.Boolean
PX.Objects.CN.PMWipChangeOrderLine.Date : Edm.DateTimeOffset
PX.Objects.CN.PMWipChangeOrderLine.CompletionDate : Edm.DateTimeOffset
PX.Objects.CN.PMWipChangeOrderLine.ProjectID : Edm.Int32
PX.Objects.CN.PMWipChangeOrderLine.TaskID : Edm.Int32
PX.Objects.CN.PMWipChangeOrderLine.CostCodeID : Edm.Int32
PX.Objects.CN.PMWipChangeOrderLine.AmountInProjectCury : Edm.Decimal
PX.Objects.CN.PMWipChangeOrderLine.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.CN.PMWipChangeOrderLine.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.PMWipChangeOrderLine.PMChangeOrderTaxCollection -> Collection(PX.Objects.PM.PMChangeOrderTax)
PX.Objects.CN.PMWipChangeOrderLine.PMChangeOrderBudgetCollection -> Collection(PX.Objects.PM.PMChangeOrderBudget)
PX.Objects.CN.PMWipChangeOrderLine.PMChangeOrderTaxTranCollection -> Collection(PX.Objects.PM.PMChangeOrderTaxTran)
PX.Objects.CN.PMWipChangeOrderLine.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.CN.PMWipChangeOrderLine.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.CN.PMWipChangeOrderLine.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.CN.PMWipChangeOrderLine.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.CN.PMWipChangeOrderLine.DailyFieldReportChangeOrderCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportChangeOrder)

# PX.Objects.CN.PMWipCommitment (EntityType)

Label: "PM WIP Commitment"
Key: CommitmentID
Entity sets: PX_Objects_CN_PMWipCommitment, PMWIPCommitment

PX.Objects.CN.PMWipCommitment.CommitmentID : Edm.Guid [key]
PX.Objects.CN.PMWipCommitment.ProjectID : Edm.Int32
PX.Objects.CN.PMWipCommitment.ProjectTaskID : Edm.Int32
PX.Objects.CN.PMWipCommitment.CostCodeID : Edm.Int32
PX.Objects.CN.PMWipCommitment.OrigAmount : Edm.Decimal
PX.Objects.CN.PMWipCommitment.Amount : Edm.Decimal
PX.Objects.CN.PMWipCommitment.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.PMWipCommitment.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.CN.PMWipCommitment.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.CN.PMWipCommitment.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)

# PX.Objects.CN.PMWipCostProjection (EntityType)

Label: "PM WIP Cost Projection"
Key: ProjectID
Entity sets: PX_Objects_CN_PMWipCostProjection, PMWIPCostProjection

PX.Objects.CN.PMWipCostProjection.ProjectID : Edm.Int32 [key]
PX.Objects.CN.PMWipCostProjection.TaskID : Edm.Int32
PX.Objects.CN.PMWipCostProjection.CostCodeID : Edm.Int32
PX.Objects.CN.PMWipCostProjection.AccountGroupID : Edm.Int32
PX.Objects.CN.PMWipCostProjection.InventoryID : Edm.Int32
PX.Objects.CN.PMWipCostProjection.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.PMWipCostProjection.PMTaskByTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, TaskID=TaskID)
PX.Objects.CN.PMWipCostProjection.PMTaskByProjectID -> PX.Objects.PM.PMTask (TaskID=TaskID, ProjectID=ProjectID)
PX.Objects.CN.PMWipCostProjection.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.CN.PMWipCostProjection.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.CN.PMWipCostProjection.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.CN.PMWipCostProjection.PMCostProjectionByRevisionID -> PX.Objects.PM.PMCostProjection (ProjectID=ProjectID)

# PX.Objects.CN.PMWipCostProjectionBudget (EntityType)

Label: "PM WIP Cost Projection Budget"
Key: AccountGroupID, CostCodeID, InventoryID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_CN_PMWipCostProjectionBudget, PMWIPCostProjectionBudget

PX.Objects.CN.PMWipCostProjectionBudget.ProjectID : Edm.Int32 [key]
PX.Objects.CN.PMWipCostProjectionBudget.ProjectTaskID : Edm.Int32 [key]
PX.Objects.CN.PMWipCostProjectionBudget.CostCodeID : Edm.Int32 [key]
PX.Objects.CN.PMWipCostProjectionBudget.AccountGroupID : Edm.Int32 [key]
PX.Objects.CN.PMWipCostProjectionBudget.InventoryID : Edm.Int32 [key]
PX.Objects.CN.PMWipCostProjectionBudget.Type : Edm.String
PX.Objects.CN.PMWipCostProjectionBudget.CuryAmount : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.OriginalContractAmount : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.OriginalCostAmount : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.CuryChangeOrderAmount : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.ChangeOrderContractAmount : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.ChangeOrderCostAmount : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.CuryCostToComplete : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.CostToComplete : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.CostProjectionCostAtCompletion : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.CostProjectionCostToComplete : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.CuryCommittedOrigAmount : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.CuryCommittedCOAmount : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.ProjectedCostAtCompletion : Edm.Decimal
PX.Objects.CN.PMWipCostProjectionBudget.PMProjectByProjectID -> PX.Objects.PM.PMProject (ProjectID=ContractID)
PX.Objects.CN.PMWipCostProjectionBudget.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectID=ProjectID, ProjectTaskID=TaskID)
PX.Objects.CN.PMWipCostProjectionBudget.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID, ProjectID=ProjectID)
PX.Objects.CN.PMWipCostProjectionBudget.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.CN.PMWipCostProjectionBudget.PMAccountGroupByAccountGroupID -> PX.Objects.PM.PMAccountGroup (AccountGroupID=GroupID)
PX.Objects.CN.PMWipCostProjectionBudget.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.CN.PMWipCostProjectionBudget.PMBudgetProductionCollection -> Collection(PX.Objects.PM.PMBudgetProduction)

# PX.Objects.CN.PMWipDetailTotalForecastHistory (ComplexType)


PX.Objects.CN.PMWipDetailTotalForecastHistory.ProjectID : Edm.Int32
PX.Objects.CN.PMWipDetailTotalForecastHistory.ProjectTaskID : Edm.Int32
PX.Objects.CN.PMWipDetailTotalForecastHistory.CostCodeID : Edm.Int32
PX.Objects.CN.PMWipDetailTotalForecastHistory.PeriodID : Edm.String
PX.Objects.CN.PMWipDetailTotalForecastHistory.AccountGroupID : Edm.Int32
PX.Objects.CN.PMWipDetailTotalForecastHistory.ActualCostAmount : Edm.Decimal
PX.Objects.CN.PMWipDetailTotalForecastHistory.ActualRevenueAmount : Edm.Decimal
PX.Objects.CN.PMWipDetailTotalForecastHistory.ArRevenueAmount : Edm.Decimal
PX.Objects.CN.PMWipDetailTotalForecastHistory.ArRevenueInclTaxAmount : Edm.Decimal
PX.Objects.CN.PMWipDetailTotalForecastHistory.CuryARAllAmount : Edm.Decimal

# PX.Objects.CN.PMWipForecastHistory (EntityType)

Label: "PM WIP Forecast History"
Key: AccountGroupID, CostCodeID, InventoryID, PeriodID, ProjectID, ProjectTaskID
Entity sets: PX_Objects_CN_PMWipForecastHistory, PMWIPForecastHistory

PX.Objects.CN.PMWipForecastHistory.ProjectID : Edm.Int32 [key]
PX.Objects.CN.PMWipForecastHistory.ProjectTaskID : Edm.Int32 [key]
PX.Objects.CN.PMWipForecastHistory.AccountGroupID : Edm.Int32 [key]
PX.Objects.CN.PMWipForecastHistory.InventoryID : Edm.Int32 [key]
PX.Objects.CN.PMWipForecastHistory.CostCodeID : Edm.Int32 [key]
PX.Objects.CN.PMWipForecastHistory.PeriodID : Edm.String [key]
PX.Objects.CN.PMWipForecastHistory.Type : Edm.String
PX.Objects.CN.PMWipForecastHistory.IsExpense : Edm.Boolean
PX.Objects.CN.PMWipForecastHistory.ActualCostAmount : Edm.Decimal
PX.Objects.CN.PMWipForecastHistory.ActualRevenueAmount : Edm.Decimal
PX.Objects.CN.PMWipForecastHistory.ArRevenueAmount : Edm.Decimal
PX.Objects.CN.PMWipForecastHistory.ArRevenueInclTaxAmount : Edm.Decimal
PX.Objects.CN.PMWipForecastHistory.CuryARAllAmount : Edm.Decimal

# PX.Objects.CN.PMWipTotalBudget (ComplexType)


PX.Objects.CN.PMWipTotalBudget.ProjectID : Edm.Int32
PX.Objects.CN.PMWipTotalBudget.OriginalContractAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.OriginalCostAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.ChangeOrderContractAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.ChangeOrderCostAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.CostToComplete : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.CostProjectionCostAtCompletion : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.CostProjectionCostToComplete : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.CuryCommittedOrigAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.CuryCommittedCOAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalBudget.ProjectedCostAtCompletion : Edm.Decimal

# PX.Objects.CN.PMWipTotalForecastHistory (ComplexType)


PX.Objects.CN.PMWipTotalForecastHistory.ProjectID : Edm.Int32
PX.Objects.CN.PMWipTotalForecastHistory.PeriodID : Edm.String
PX.Objects.CN.PMWipTotalForecastHistory.ActualCostAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalForecastHistory.ActualRevenueAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalForecastHistory.ArRevenueAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalForecastHistory.ArRevenueInclTaxAmount : Edm.Decimal
PX.Objects.CN.PMWipTotalForecastHistory.CuryARAllAmount : Edm.Decimal

# PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField (EntityType)

Label: "ComplianceRequirementField"
Key: FieldID, RequirementID
Entity sets: PX_Objects_CN_Requirements_ComplianceRequirementFields_ComplianceRequirementField, ComplianceRequirementField

PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.RequirementID : Edm.String [key]
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.FieldID : Edm.String [key] "Attribute"
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.IsRequired : Edm.Boolean [required] "Required"
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.SortOrder : Edm.Int32
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.CreatedByID : Edm.Guid "Created By"
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.CreatedByScreenID : Edm.String
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.LastModifiedByScreenID : Edm.String
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField.VendorDocumentRequirementByRequirementID -> PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement (RequirementID=RequirementID)

# PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance (EntityType)

Label: "Vendor Document Requirement Compliance"
Key: ReqComplianceID
Entity sets: PX_Objects_CN_Requirements_DAC_VendorDocumentReqCompliance, VendorDocumentRequirementCompliance, VendorDocumentReqCompliance
Non-filterable, non-selectable: ComplianceDocumentDisplayName, ExpirationWarningText, ComplianceLimitText, IsExpired, StatusWithExpiration, ProjectCD, RelatedTo

PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ReqComplianceID : Edm.Guid [key] "ID"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.RequirementID : Edm.String "Requirement ID"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.RequirementType : Edm.String "Requirement Applies To"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.RequirementLevel : Edm.String "Validated Record"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ComplianceDocumentID : Edm.Int32 "Compliance Document"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ComplianceDocumentDisplayName : Edm.String "Document"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.DocumentTypeID : Edm.Int32 "Document Type"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.DocumentCategoryID : Edm.Int32 "Document Category"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ExpirationWarningText : Edm.String "Warning"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ComplianceLimitText : Edm.String "Limit"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.IsExpired : Edm.Boolean "Expired"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.Status : Edm.String "Status"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.StatusWithExpiration : Edm.String "Status"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.VendorID : Edm.Int32 "Vendor"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.RefNoteID : Edm.Guid "Ref. Nbr."
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ProjectCD : Edm.String "Related Project"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.RelatedTo : Edm.Int32 "Related To"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.RejectReason : Edm.String "Rejection Reason"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.Tstamp : Edm.Binary
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.CreatedByID : Edm.Guid "Created By"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.CreatedByScreenID : Edm.String
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.LastModifiedByScreenID : Edm.String
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.VendorByVendorID -> PX.Objects.AP.Vendor (VendorID=BAccountID)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ComplianceAttributeByDocumentTypeID -> PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute (DocumentCategoryID=AttributeId, DocumentTypeID=Type)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.VendorDocumentRequirementByRequirementID -> PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement (RequirementID=RequirementID)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ComplianceDocumentByComplianceDocumentID -> PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument (ComplianceDocumentID=ComplianceDocumentID)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance.ComplianceAttributeTypeByDocumentTypeID -> PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType (DocumentTypeID=ComplianceAttributeTypeID)

# PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow (EntityType)

Label: "Vendor Document Requirement Condition Row"
Key: LineNbr, RequirementID
Entity sets: PX_Objects_CN_Requirements_DAC_VendorDocumentReqConditionRow, VendorDocumentRequirementConditionRow, VendorDocumentReqConditionRow
Non-filterable, non-selectable: ConditionName

PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.RequirementID : Edm.String [key] "Requirement ID"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.LineNbr : Edm.Int32 [key] "Line Nbr"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.OpenBrackets : Edm.Int32
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.DataField : Edm.String "Data Field"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.Condition : Edm.Byte "Condition"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.ConditionName : Edm.String "Condition Name"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.Value : Edm.String "Value 1"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.Value2 : Edm.String "Value 2"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.CloseBrackets : Edm.Int32
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.OrOperator : Edm.Boolean
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.Tstamp : Edm.Binary
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.CreatedByID : Edm.Guid "Created By"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.CreatedByScreenID : Edm.String
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.LastModifiedByScreenID : Edm.String
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow.VendorDocumentRequirementByRequirementID -> PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement (RequirementID=RequirementID)

# PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement (EntityType)

Label: "Vendor Document Requirement"
Key: RequirementID
Entity sets: PX_Objects_CN_Requirements_DAC_VendorDocumentRequirement, VendorDocumentRequirement
Non-filterable, non-selectable: NoteText

PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.RequirementID : Edm.String [key] "Requirement ID"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.Description : Edm.String "Description"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.RequirementType : Edm.String "Requirement Applies To"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.RequirementLevel : Edm.String "Validated Record"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.DocumentTypeID : Edm.Int32 "Document Type"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.DocumentCategoryID : Edm.Int32 "Document Category"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.LineCntr : Edm.Int32 [required]
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.NoteID : Edm.Guid
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.NoteText : Edm.String "Note Text"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.Tstamp : Edm.Binary
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.CreatedByID : Edm.Guid "Created By"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.CreatedByScreenID : Edm.String
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.LastModifiedByScreenID : Edm.String
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.ComplianceAttributeByDocumentTypeID -> PX.Objects.CN.Compliance.CL.DAC.ComplianceAttribute (DocumentCategoryID=AttributeId, DocumentTypeID=Type)
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.ComplianceAttributeTypeByDocumentTypeID -> PX.Objects.CN.Compliance.CL.DAC.ComplianceAttributeType (DocumentTypeID=ComplianceAttributeTypeID)
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.VendorDocumentReqConditionRowCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqConditionRow)
PX.Objects.CN.Requirements.DAC.VendorDocumentRequirement.ComplianceRequirementFieldCollection -> Collection(PX.Objects.CN.Requirements.ComplianceRequirementFields.ComplianceRequirementField)

# PX.Objects.CN.SCSetup (EntityType)

Label: "Subcontract Preferences"
Singletons: PX_Objects_CN_SCSetup, SubcontractPreferences, SCSetup

PX.Objects.CN.SCSetup.SubcontractNumberingID : Edm.String "Subcontract Numbering Sequence"
PX.Objects.CN.SCSetup.RequireSubcontractControlTotal : Edm.Boolean "Validate Total on Entry"
PX.Objects.CN.SCSetup.AssignmentMapID : Edm.Int32 "Approval Map"
PX.Objects.CN.SCSetup.AssignmentNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.CN.SCSetup.IsActive : Edm.Boolean "IsActive"
PX.Objects.CN.SCSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.CN.SCSetup.CreatedByScreenID : Edm.String
PX.Objects.CN.SCSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CN.SCSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CN.SCSetup.LastModifiedByScreenID : Edm.String
PX.Objects.CN.SCSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CN.SCSetup.tstamp : Edm.Binary
PX.Objects.CN.SCSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CN.SCSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CN.SCSetup.NotificationByAssignmentNotificationID -> PX.SM.Notification (AssignmentNotificationID=NotificationID)
PX.Objects.CN.SCSetup.NumberingBySubcontractNumberingID -> PX.Objects.CS.Numbering (SubcontractNumberingID=NumberingID)
PX.Objects.CN.SCSetup.EPAssignmentMapByAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (AssignmentMapID=AssignmentMapID)

# PX.Objects.CN.Subcontracts.SC.DAC.Subcontract (EntityType)

Label: "Subcontract"
BaseType: PX.Objects.PO.POOrder
Key: OrderNbr, OrderType (inherited from PX.Objects.PO.POOrder)
Entity sets: PX_Objects_CN_Subcontracts_SC_DAC_Subcontract, Subcontract

# PX.Objects.CN.Subcontracts.SC.DAC.SubcontractInventoryItem (EntityType)

Label: "Subcontract Inventory Item"
BaseType: PX.Objects.IN.InventoryItem
Key: InventoryCD (inherited from PX.Objects.IN.InventoryItem)
Entity sets: PX_Objects_CN_Subcontracts_SC_DAC_SubcontractInventoryItem, SubcontractInventoryItem

# PX.Objects.CN.Subcontracts.SC.DAC.SubcontractNotification (EntityType)

Label: "Subcontract Notification"
BaseType: PX.Objects.CS.NotificationSetup
Key: SetupID (inherited from PX.Objects.CS.NotificationSetup)
Entity sets: PX_Objects_CN_Subcontracts_SC_DAC_SubcontractNotification, SubcontractNotification

# PX.Objects.Common.DAC.DropShipLink (EntityType)

Label: "Drop-Ship Link"
Key: POLineNbr, POOrderNbr, POOrderType, SOLineNbr, SOOrderNbr, SOOrderType
Entity sets: PX_Objects_Common_DAC_DropShipLink, DropShipLink

PX.Objects.Common.DAC.DropShipLink.SOOrderType : Edm.String [key]
PX.Objects.Common.DAC.DropShipLink.SOOrderNbr : Edm.String [key]
PX.Objects.Common.DAC.DropShipLink.SOLineNbr : Edm.Int32 [key]
PX.Objects.Common.DAC.DropShipLink.POOrderType : Edm.String [key]
PX.Objects.Common.DAC.DropShipLink.POOrderNbr : Edm.String [key]
PX.Objects.Common.DAC.DropShipLink.POLineNbr : Edm.Int32 [key]
PX.Objects.Common.DAC.DropShipLink.Active : Edm.Boolean [required]
PX.Objects.Common.DAC.DropShipLink.InReceipt : Edm.Boolean [required]
PX.Objects.Common.DAC.DropShipLink.SOCompleted : Edm.Boolean [required]
PX.Objects.Common.DAC.DropShipLink.SOInventoryID : Edm.Int32
PX.Objects.Common.DAC.DropShipLink.SOSiteID : Edm.Int32
PX.Objects.Common.DAC.DropShipLink.SOBaseOrderQty : Edm.Decimal
PX.Objects.Common.DAC.DropShipLink.POCompleted : Edm.Boolean [required]
PX.Objects.Common.DAC.DropShipLink.POInventoryID : Edm.Int32
PX.Objects.Common.DAC.DropShipLink.POSiteID : Edm.Int32
PX.Objects.Common.DAC.DropShipLink.POBaseOrderQty : Edm.Decimal
PX.Objects.Common.DAC.DropShipLink.BaseReceivedQty : Edm.Decimal
PX.Objects.Common.DAC.DropShipLink.CreatedByID : Edm.Guid "Created By"
PX.Objects.Common.DAC.DropShipLink.CreatedByScreenID : Edm.String
PX.Objects.Common.DAC.DropShipLink.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.Common.DAC.DropShipLink.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.Common.DAC.DropShipLink.LastModifiedByScreenID : Edm.String
PX.Objects.Common.DAC.DropShipLink.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.Common.DAC.DropShipLink.tstamp : Edm.Binary
PX.Objects.Common.DAC.DropShipLink.POLineByPOLineNbr -> PX.Objects.PO.POLine (POOrderType=OrderType, POOrderNbr=OrderNbr, POLineNbr=LineNbr)
PX.Objects.Common.DAC.DropShipLink.POOrderByPOOrderNbr -> PX.Objects.PO.POOrder (POOrderType=OrderType, POOrderNbr=OrderNbr)
PX.Objects.Common.DAC.DropShipLink.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.Common.DAC.DropShipLink.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.Common.DAC.DropShipLink.SOLineBySOLineNbr -> PX.Objects.SO.SOLine (SOOrderType=OrderType, SOOrderNbr=OrderNbr, SOLineNbr=LineNbr)
PX.Objects.Common.DAC.DropShipLink.SupplyPOLineByPOLineNbr -> PX.Objects.SO.SupplyPOLine (POOrderType=OrderType, POOrderNbr=OrderNbr, POLineNbr=LineNbr)

# PX.Objects.Common.DAC.ReportParameters.BAccountNoMask (EntityType)

Key: AcctCD, BAccountID
Entity sets: PX_Objects_Common_DAC_ReportParameters_BAccountNoMask

PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.BAccountID : Edm.Int32 [key]
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AcctCD : Edm.String [key]
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AcctName : Edm.String
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AcctReferenceNbr : Edm.String
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.OwnerID : Edm.Int32
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.Type : Edm.String
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.DefContactID : Edm.Int32
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.DefLocationID : Edm.Int32
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.DefAddressID : Edm.Int32
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.IsBranch : Edm.Boolean
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.COrgBAccountID : Edm.Int32
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.VOrgBAccountID : Edm.Int32
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxRegistrationID : Edm.String
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.VendorByOwnerID -> PX.Objects.AP.Vendor (OwnerID=BAccountID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.BAccountByParentBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.BAccountByCOrgBAccountID -> PX.Objects.CR.BAccount (COrgBAccountID=BAccountID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ContactByDefContactID -> PX.Objects.CR.Contact (DefContactID=ContactID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ContactByPrimaryContactID -> PX.Objects.CR.Contact
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ContactByBAccountID -> PX.Objects.CR.Contact (BAccountID=BAccountID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AddressByDefAddressID -> PX.Objects.CR.Address (DefAddressID=AddressID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.UsersByCreatedByID -> PX.SM.Users
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.UsersByLastModifiedByID -> PX.SM.Users
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.LocationByDefLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID, DefLocationID=LocationID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.LocationByBAccountID -> PX.Objects.CR.Location (DefLocationID=LocationID, BAccountID=BAccountID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PRCRAPayrollAccountCollection -> Collection(PX.Objects.PR.PRCRAPayrollAccount)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PRTaxReportingAccountCollection -> Collection(PX.Objects.PR.PRTaxReportingAccount)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CanadianOrganizationSettingsCollection -> Collection(PX.Objects.Localizations.CA.CanadianOrganizationSettings)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AUScheduleCollection -> Collection(PX.SM.AUSchedule)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.GLTrialBalanceImportMapCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportMap)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CISMasterTableCollection -> Collection(PX.Objects.Localizations.GB.CISMasterTable)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PRAcaCompanyYearlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyYearlyInformation)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PRTaxFormBatchCollection -> Collection(PX.Objects.PR.PRTaxFormBatch)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SVATConversionHistExtCollection -> Collection(PX.Objects.TX.SVATConversionHistExt)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RQRequestLineOwnedCollection -> Collection(PX.Objects.RQ.RQRequestLineOwned)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.MultipleQuoteCollection -> Collection(PX.Objects.CN.CRM.CR.DAC.MultipleQuote)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.DailyFieldReportVisitorCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSLicenseCollection -> Collection(PX.Objects.SV.FSLicense)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.JointPayeeCollection -> Collection(PX.Objects.CN.JointChecks.JointPayee)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.T5018MasterTableCollection -> Collection(PX.Objects.Localizations.CA.T5018MasterTable)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxYearCollection -> Collection(PX.Objects.TX.TaxYear)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxPeriodCollection -> Collection(PX.Objects.TX.TaxPeriod)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxReportCollection -> Collection(PX.Objects.TX.TaxReport)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMProjectContactCollection -> Collection(PX.Objects.PM.PMProjectContact)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMUnionCollection -> Collection(PX.Objects.PM.PMUnion)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CarrierPluginCustomerCollection -> Collection(PX.Objects.CS.CarrierPluginCustomer)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.INReplenishmentOrderCollection -> Collection(PX.Objects.IN.INReplenishmentOrder)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.DiscountCustomerCollection -> Collection(PX.Objects.AR.DiscountCustomer)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSGeoZoneEmpCollection -> Collection(PX.Objects.FS.FSGeoZoneEmp)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.T4ASlipCollection -> Collection(PX.Objects.Localizations.CA.T4ASlip)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PREmployeeDeductCollection -> Collection(PX.Objects.PR.PREmployeeDeduct)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PRTaxRegistrationAttributeCollection -> Collection(PX.Objects.PR.PRTaxRegistrationAttribute)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SVServiceLocationCustomerCollection -> Collection(PX.Objects.SV.SVServiceLocationCustomer)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CustomerProcessingCenterIDCollection -> Collection(PX.Objects.CA.CustomerProcessingCenterID)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSSOEmployeeCollection -> Collection(PX.Objects.FS.FSSOEmployee)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSAppointmentStaffMemberCollection -> Collection(PX.Objects.FS.FSAppointmentStaffMember)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POAddressCollection -> Collection(PX.Objects.PO.POAddress)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.POContactCollection -> Collection(PX.Objects.PO.POContact)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AddressCollection -> Collection(PX.Objects.CR.Address)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRAddressCollection -> Collection(PX.Objects.CR.CRAddress)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSAddressCollection -> Collection(PX.Objects.FS.FSAddress)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.FSContactCollection -> Collection(PX.Objects.FS.FSContact)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.VendorPaymentMethodDetailCollection -> Collection(PX.Objects.AP.VendorPaymentMethodDetail)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRRelationCollection -> Collection(PX.Objects.CR.CRRelation)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.SelContractWatcherCollection -> Collection(PX.Objects.CT.SelContractWatcher)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CABankTranBAccountMappingCollection -> Collection(PX.Objects.CA.CABankTranBAccountMapping)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.RecognizedVendorMappingCollection -> Collection(PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.TaxRegistrationCollection -> Collection(PX.Objects.Localizations.CA.TaxRegistration)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CISSubcontractorCollection -> Collection(PX.Objects.Localizations.GB.CISSubcontractor)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PREntityCompanyTaxAttributeCollection -> Collection(PX.Objects.PR.PREntityCompanyTaxAttribute)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.PREntityTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PREntityTaxCodeAttribute)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.BAccountLocationCollection -> Collection(PX.Objects.FS.BAccountLocation)
PX.Objects.Common.DAC.ReportParameters.BAccountNoMask.CanadianVendorCollection -> Collection(PX.Objects.Localizations.CA.CanadianVendor)

# PX.Objects.CR.Address (EntityType)

Label: "Address"
Key: AddressID
Entity sets: PX_Objects_CR_Address, Address
Non-filterable, non-selectable: NoteText

PX.Objects.CR.Address.AddressID : Edm.Int32 [key] "Address ID"
PX.Objects.CR.Address.BAccountID : Edm.Int32 "Business Account ID"
PX.Objects.CR.Address.RevisionID : Edm.Int32
PX.Objects.CR.Address.DisplayName : Edm.String "Address"
PX.Objects.CR.Address.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.CR.Address.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.CR.Address.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.CR.Address.City : Edm.String "City"
PX.Objects.CR.Address.CountryID : Edm.String "Country"
PX.Objects.CR.Address.State : Edm.String "State"
PX.Objects.CR.Address.PostalCode : Edm.String "Postal Code"
PX.Objects.CR.Address.Department : Edm.String "Department"
PX.Objects.CR.Address.SubDepartment : Edm.String "Subdepartment"
PX.Objects.CR.Address.StreetName : Edm.String "Street Name"
PX.Objects.CR.Address.BuildingNumber : Edm.String "Building Number"
PX.Objects.CR.Address.BuildingName : Edm.String "Building Name"
PX.Objects.CR.Address.Floor : Edm.String "Floor"
PX.Objects.CR.Address.UnitNumber : Edm.String "Unit Number"
PX.Objects.CR.Address.PostBox : Edm.String "Post Box"
PX.Objects.CR.Address.Room : Edm.String "Room"
PX.Objects.CR.Address.TownLocationName : Edm.String "Town Location Name"
PX.Objects.CR.Address.DistrictName : Edm.String "District Name"
PX.Objects.CR.Address.AddressType : Edm.String "Address Type"
PX.Objects.CR.Address.CareOf : Edm.String "Care Of"
PX.Objects.CR.Address.NoteID : Edm.Guid
PX.Objects.CR.Address.NoteText : Edm.String "Note Text"
PX.Objects.CR.Address.TaxLocationCode : Edm.String "Tax Location Code"
PX.Objects.CR.Address.TaxLocationCodeFull : Edm.String "Full Tax Location Code"
PX.Objects.CR.Address.TaxMunicipalCode : Edm.String "Tax Municipal Code"
PX.Objects.CR.Address.TaxSchoolCode : Edm.String "Tax School Code"
PX.Objects.CR.Address.tstamp : Edm.Binary
PX.Objects.CR.Address.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.Address.CreatedByScreenID : Edm.String
PX.Objects.CR.Address.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.Address.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.Address.LastModifiedByScreenID : Edm.String
PX.Objects.CR.Address.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.Address.Latitude : Edm.Decimal "Latitude"
PX.Objects.CR.Address.Longitude : Edm.Decimal "Longitude"
PX.Objects.CR.Address.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CR.Address.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.Address.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.Address.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.CR.Address.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.CR.Address.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.CR.Address.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CR.Address.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CR.Address.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CR.Address.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CR.Address.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CR.Address.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.CR.Address.POAddressCollection -> Collection(PX.Objects.PO.POAddress)
PX.Objects.CR.Address.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.CR.Address.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.CR.Address.CRAddressCollection -> Collection(PX.Objects.CR.CRAddress)
PX.Objects.CR.Address.ARAddressCollection -> Collection(PX.Objects.AR.ARAddress)
PX.Objects.CR.Address.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CR.Address.INSiteBuildingCollection -> Collection(PX.Objects.IN.INSiteBuilding)
PX.Objects.CR.Address.APAddressCollection -> Collection(PX.Objects.AP.APAddress)
PX.Objects.CR.Address.PRLocationCollection -> Collection(PX.Objects.PR.PRLocation)
PX.Objects.CR.Address.PRRecordOfEmploymentCollection -> Collection(PX.Objects.PR.PRRecordOfEmployment)

# PX.Objects.CR.BAccount (EntityType)

Label: "Business Account"
Key: AcctCD
Entity sets: PX_Objects_CR_BAccount, BusinessAccount, BAccount
Non-filterable, non-selectable: NoteText, NotePopupText, ViewInCrm, HSEntityTypeID, EntityTypeID, Secured, DeletedDatabaseRecord

PX.Objects.CR.BAccount.BAccountID : Edm.Int32 "Business Account ID"
PX.Objects.CR.BAccount.AcctCD : Edm.String [key] "Account ID"
PX.Objects.CR.BAccount.AcctName : Edm.String "Account Name"
PX.Objects.CR.BAccount.ClassID : Edm.String "Business Account Class"
PX.Objects.CR.BAccount.LegalName : Edm.String "Legal Name"
PX.Objects.CR.BAccount.Type : Edm.String "Type"
PX.Objects.CR.BAccount.IsCustomerOrCombined : Edm.Boolean
PX.Objects.CR.BAccount.IsBranch : Edm.Boolean
PX.Objects.CR.BAccount.AcctReferenceNbr : Edm.String "Ext. Ref. Nbr."
PX.Objects.CR.BAccount.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.CR.BAccount.ConsolidateToParent : Edm.Boolean [required] "Consolidate Balance"
PX.Objects.CR.BAccount.ConsolidatingBAccountID : Edm.Int32
PX.Objects.CR.BAccount.BaseCuryID : Edm.String "Base Currency ID"
PX.Objects.CR.BAccount.CuryID : Edm.String "Currency ID"
PX.Objects.CR.BAccount.CuryRateTypeID : Edm.String "Curr. Rate Type"
PX.Objects.CR.BAccount.AllowOverrideCury : Edm.Boolean [required] "Enable Currency Override"
PX.Objects.CR.BAccount.AllowOverrideRate : Edm.Boolean [required] "Enable Rate Override"
PX.Objects.CR.BAccount.Status : Edm.String "Customer Status"
PX.Objects.CR.BAccount.VStatus : Edm.String "Vendor Status"
PX.Objects.CR.BAccount.CampaignSourceID : Edm.String "Source Campaign"
PX.Objects.CR.BAccount.DefAddressID : Edm.Int32 "Default Address"
PX.Objects.CR.BAccount.DefContactID : Edm.Int32 "Default Contact"
PX.Objects.CR.BAccount.DefLocationID : Edm.Int32 "Default Location"
PX.Objects.CR.BAccount.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.CR.BAccount.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.BAccount.PrimaryContactID : Edm.Int32 "Primary Contact"
PX.Objects.CR.BAccount.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.BAccount.NoteID : Edm.Guid
PX.Objects.CR.BAccount.NoteText : Edm.String "Note Text"
PX.Objects.CR.BAccount.NotePopupText : Edm.String "Note Text"
PX.Objects.CR.BAccount.tstamp : Edm.Binary
PX.Objects.CR.BAccount.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.BAccount.CreatedByScreenID : Edm.String
PX.Objects.CR.BAccount.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.BAccount.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.BAccount.LastModifiedByScreenID : Edm.String
PX.Objects.CR.BAccount.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.BAccount.ViewInCrm : Edm.Boolean "View In CRM"
PX.Objects.CR.BAccount.LocaleName : Edm.String "Language/Locale"
PX.Objects.CR.BAccount.HSEntityTypeID : Edm.Int32
PX.Objects.CR.BAccount.EntityTypeID : Edm.Int32
PX.Objects.CR.BAccount.Secured : Edm.Boolean "Secured"
PX.Objects.CR.BAccount.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CR.BAccount.VendorByOwnerID -> PX.Objects.AP.Vendor (OwnerID=BAccountID)
PX.Objects.CR.BAccount.BAccountByParentBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID)
PX.Objects.CR.BAccount.BAccountByCOrgBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CR.BAccount.ContactByDefContactID -> PX.Objects.CR.Contact (DefContactID=ContactID)
PX.Objects.CR.BAccount.ContactByPrimaryContactID -> PX.Objects.CR.Contact (PrimaryContactID=ContactID)
PX.Objects.CR.BAccount.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.BAccount.ContactByBAccountID -> PX.Objects.CR.Contact (PrimaryContactID=ContactID, BAccountID=BAccountID)
PX.Objects.CR.BAccount.CRCustomerClassByClassID -> PX.Objects.CR.CRCustomerClass (ClassID=CRCustomerClassID)
PX.Objects.CR.BAccount.AddressByDefAddressID -> PX.Objects.CR.Address (DefAddressID=AddressID)
PX.Objects.CR.BAccount.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.BAccount.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.BAccount.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.BAccount.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CR.BAccount.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CR.BAccount.CurrencyListByBaseCuryID -> PX.Objects.CM.CurrencyList (BaseCuryID=CuryID)
PX.Objects.CR.BAccount.CurrencyRateTypeByCuryRateTypeID -> PX.Objects.CM.CurrencyRateType (CuryRateTypeID=CuryRateTypeID)
PX.Objects.CR.BAccount.LocationByDefLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID, DefLocationID=LocationID)
PX.Objects.CR.BAccount.LocationByBAccountID -> PX.Objects.CR.Location (DefLocationID=LocationID, BAccountID=BAccountID)
PX.Objects.CR.BAccount.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign (CampaignSourceID=CampaignID)
PX.Objects.CR.BAccount.LocaleByLocaleName -> PX.SM.Locale (LocaleName=LocaleName)
PX.Objects.CR.BAccount.OrganizationCollection -> Collection(PX.Objects.GL.DAC.Organization)
PX.Objects.CR.BAccount.PRCRAPayrollAccountCollection -> Collection(PX.Objects.PR.PRCRAPayrollAccount)
PX.Objects.CR.BAccount.PRTaxReportingAccountCollection -> Collection(PX.Objects.PR.PRTaxReportingAccount)
PX.Objects.CR.BAccount.CanadianOrganizationSettingsCollection -> Collection(PX.Objects.Localizations.CA.CanadianOrganizationSettings)
PX.Objects.CR.BAccount.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CR.BAccount.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CR.BAccount.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CR.BAccount.AUScheduleCollection -> Collection(PX.SM.AUSchedule)
PX.Objects.CR.BAccount.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CR.BAccount.EPEmployeeClassCollection -> Collection(PX.Objects.EP.EPEmployeeClass)
PX.Objects.CR.BAccount.VendorClassCollection -> Collection(PX.Objects.AP.VendorClass)
PX.Objects.CR.BAccount.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CR.BAccount.GLTrialBalanceImportMapCollection -> Collection(PX.Objects.GL.GLTrialBalanceImportMap)
PX.Objects.CR.BAccount.CustomerClassCollection -> Collection(PX.Objects.AR.CustomerClass)
PX.Objects.CR.BAccount.CISMasterTableCollection -> Collection(PX.Objects.Localizations.GB.CISMasterTable)
PX.Objects.CR.BAccount.PRAcaCompanyYearlyInformationCollection -> Collection(PX.Objects.PR.PRAcaCompanyYearlyInformation)
PX.Objects.CR.BAccount.PRTaxFormBatchCollection -> Collection(PX.Objects.PR.PRTaxFormBatch)
PX.Objects.CR.BAccount.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.CR.BAccount.DiscrepancyByAccountEnqResultCollection -> Collection(ReconciliationTools.DiscrepancyByAccountEnqResult)
PX.Objects.CR.BAccount.TaxTranCollection -> Collection(PX.Objects.TX.TaxTran)
PX.Objects.CR.BAccount.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CR.BAccount.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CR.BAccount.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CR.BAccount.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CR.BAccount.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.CR.BAccount.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CR.BAccount.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CR.BAccount.SVATConversionHistExtCollection -> Collection(PX.Objects.TX.SVATConversionHistExt)
PX.Objects.CR.BAccount.RQRequestLineOwnedCollection -> Collection(PX.Objects.RQ.RQRequestLineOwned)
PX.Objects.CR.BAccount.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CR.BAccount.RQRequestLineCollection -> Collection(PX.Objects.RQ.RQRequestLine)
PX.Objects.CR.BAccount.INItemPlanCollection -> Collection(PX.Objects.IN.INItemPlan)
PX.Objects.CR.BAccount.POLineCollection -> Collection(PX.Objects.PO.POLine)
PX.Objects.CR.BAccount.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CR.BAccount.PMProformaLineCollection -> Collection(PX.Objects.PM.PMProformaLine)
PX.Objects.CR.BAccount.PMTaskCollection -> Collection(PX.Objects.PM.PMTask)
PX.Objects.CR.BAccount.FADetailsCollection -> Collection(PX.Objects.FA.FADetails)
PX.Objects.CR.BAccount.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CR.BAccount.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.CR.BAccount.MultipleQuoteCollection -> Collection(PX.Objects.CN.CRM.CR.DAC.MultipleQuote)
PX.Objects.CR.BAccount.GLTranCollection -> Collection(PX.Objects.GL.GLTran)
PX.Objects.CR.BAccount.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.CR.BAccount.APAdjustCollection -> Collection(PX.Objects.AP.APAdjust)
PX.Objects.CR.BAccount.CATranCollection -> Collection(PX.Objects.CA.CATran)
PX.Objects.CR.BAccount.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.CR.BAccount.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.CR.BAccount.ARAdjustCollection -> Collection(PX.Objects.AR.ARAdjust)
PX.Objects.CR.BAccount.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CR.BAccount.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.CR.BAccount.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CR.BAccount.DRScheduleCollection -> Collection(PX.Objects.DR.DRSchedule)
PX.Objects.CR.BAccount.CABankTranCollection -> Collection(PX.Objects.CA.CABankTran)
PX.Objects.CR.BAccount.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CR.BAccount.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.CR.BAccount.AMProdOperCollection -> Collection(PX.Objects.AM.AMProdOper)
PX.Objects.CR.BAccount.SOLineCollection -> Collection(PX.Objects.SO.SOLine)
PX.Objects.CR.BAccount.AMProdMatlCollection -> Collection(PX.Objects.AM.AMProdMatl)
PX.Objects.CR.BAccount.FSAppointmentDetCollection -> Collection(PX.Objects.FS.FSAppointmentDet)
PX.Objects.CR.BAccount.FSSODetCollection -> Collection(PX.Objects.FS.FSSODet)
PX.Objects.CR.BAccount.DailyFieldReportVisitorCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReportVisitor)
PX.Objects.CR.BAccount.FSLicenseCollection -> Collection(PX.Objects.SV.FSLicense)
PX.Objects.CR.BAccount.POReceiptLineCollection -> Collection(PX.Objects.PO.POReceiptLine)
PX.Objects.CR.BAccount.POVendorInventoryCollection -> Collection(PX.Objects.PO.POVendorInventory)
PX.Objects.CR.BAccount.APTranCollection -> Collection(PX.Objects.AP.APTran)
PX.Objects.CR.BAccount.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.CR.BAccount.INItemXRefCollection -> Collection(PX.Objects.IN.INItemXRef)
PX.Objects.CR.BAccount.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.CR.BAccount.JointPayeeCollection -> Collection(PX.Objects.CN.JointChecks.JointPayee)
PX.Objects.CR.BAccount.CashAccountCollection -> Collection(PX.Objects.CA.CashAccount)
PX.Objects.CR.BAccount.ARSalesPriceCollection -> Collection(PX.Objects.AR.ARSalesPrice)
PX.Objects.CR.BAccount.TaxCollection -> Collection(PX.Objects.TX.Tax)
PX.Objects.CR.BAccount.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.CR.BAccount.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.CR.BAccount.CustSalesPeopleCollection -> Collection(PX.Objects.AR.CustSalesPeople)
PX.Objects.CR.BAccount.T5018MasterTableCollection -> Collection(PX.Objects.Localizations.CA.T5018MasterTable)
PX.Objects.CR.BAccount.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.CR.BAccount.BranchCollection -> Collection(PX.Objects.GL.Branch)
PX.Objects.CR.BAccount.CuryAPHistoryCollection -> Collection(PX.Objects.AP.CuryAPHistory)
PX.Objects.CR.BAccount.CuryARHistoryCollection -> Collection(PX.Objects.AR.CuryARHistory)
PX.Objects.CR.BAccount.ARHistoryCollection -> Collection(PX.Objects.AR.ARHistory)
PX.Objects.CR.BAccount.ARTranPostCollection -> Collection(PX.Objects.AR.ARTranPost)
PX.Objects.CR.BAccount.APHistoryCollection -> Collection(PX.Objects.AP.APHistory)
PX.Objects.CR.BAccount.ARDunningLetterDetailCollection -> Collection(PX.Objects.AR.ARDunningLetterDetail)
PX.Objects.CR.BAccount.TaxYearCollection -> Collection(PX.Objects.TX.TaxYear)
PX.Objects.CR.BAccount.TaxPeriodCollection -> Collection(PX.Objects.TX.TaxPeriod)
PX.Objects.CR.BAccount.TaxAdjustmentCollection -> Collection(PX.Objects.TX.TaxAdjustment)
PX.Objects.CR.BAccount.TaxReportCollection -> Collection(PX.Objects.TX.TaxReport)
PX.Objects.CR.BAccount.TaxZoneCollection -> Collection(PX.Objects.TX.TaxZone)
PX.Objects.CR.BAccount.SOOrderShipmentCollection -> Collection(PX.Objects.SO.SOOrderShipment)
PX.Objects.CR.BAccount.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CR.BAccount.RQBiddingCollection -> Collection(PX.Objects.RQ.RQBidding)
PX.Objects.CR.BAccount.RQBiddingVendorCollection -> Collection(PX.Objects.RQ.RQBiddingVendor)
PX.Objects.CR.BAccount.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.CR.BAccount.PRDeductCodeCollection -> Collection(PX.Objects.PR.PRDeductCode)
PX.Objects.CR.BAccount.PRTaxCodeCollection -> Collection(PX.Objects.PR.PRTaxCode)
PX.Objects.CR.BAccount.LandedCostCodeCollection -> Collection(PX.Objects.PO.LandedCostCode)
PX.Objects.CR.BAccount.POAccrualDetailCollection -> Collection(PX.Objects.PO.POAccrualDetail)
PX.Objects.CR.BAccount.POAccrualStatusCollection -> Collection(PX.Objects.PO.POAccrualStatus)
PX.Objects.CR.BAccount.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CR.BAccount.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CR.BAccount.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CR.BAccount.PMChangeOrderLineCollection -> Collection(PX.Objects.PM.PMChangeOrderLine)
PX.Objects.CR.BAccount.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.CR.BAccount.PMChangeRequestLineCollection -> Collection(PX.Objects.PM.PMChangeRequestLine)
PX.Objects.CR.BAccount.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CR.BAccount.PMProjectContactCollection -> Collection(PX.Objects.PM.PMProjectContact)
PX.Objects.CR.BAccount.PMUnionCollection -> Collection(PX.Objects.PM.PMUnion)
PX.Objects.CR.BAccount.MNMaterialListCollection -> Collection(PX.Objects.MN.MNMaterialList)
PX.Objects.CR.BAccount.MNMaterialListLineCollection -> Collection(PX.Objects.MN.MNMaterialListLine)
PX.Objects.CR.BAccount.FAAccrualTranCollection -> Collection(PX.Objects.FA.FAAccrualTran)
PX.Objects.CR.BAccount.FAServiceCollection -> Collection(PX.Objects.FA.FAService)
PX.Objects.CR.BAccount.ContractBillingScheduleCollection -> Collection(PX.Objects.CT.ContractBillingSchedule)
PX.Objects.CR.BAccount.CarrierPluginCustomerCollection -> Collection(PX.Objects.CS.CarrierPluginCustomer)
PX.Objects.CR.BAccount.INReplenishmentLineCollection -> Collection(PX.Objects.IN.INReplenishmentLine)
PX.Objects.CR.BAccount.INReplenishmentOrderCollection -> Collection(PX.Objects.IN.INReplenishmentOrder)
PX.Objects.CR.BAccount.InventoryItemCurySettingsCollection -> Collection(PX.Objects.IN.InventoryItemCurySettings)
PX.Objects.CR.BAccount.VendorDocumentReqComplianceCollection -> Collection(PX.Objects.CN.Requirements.DAC.VendorDocumentReqCompliance)
PX.Objects.CR.BAccount.ComplianceDocumentCollection -> Collection(PX.Objects.CN.Compliance.CL.DAC.ComplianceDocument)
PX.Objects.CR.BAccount.CashAccountCheckCollection -> Collection(PX.Objects.CA.CashAccountCheck)
PX.Objects.CR.BAccount.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CR.BAccount.ARPriceWorksheetDetailCollection -> Collection(PX.Objects.AR.ARPriceWorksheetDetail)
PX.Objects.CR.BAccount.ARStatementCollection -> Collection(PX.Objects.AR.ARStatement)
PX.Objects.CR.BAccount.CustomerPaymentMethodCollection -> Collection(PX.Objects.AR.CustomerPaymentMethod)
PX.Objects.CR.BAccount.DiscountCustomerCollection -> Collection(PX.Objects.AR.DiscountCustomer)
PX.Objects.CR.BAccount.APPriceWorksheetDetailCollection -> Collection(PX.Objects.AP.APPriceWorksheetDetail)
PX.Objects.CR.BAccount.APVendorPriceCollection -> Collection(PX.Objects.AP.APVendorPrice)
PX.Objects.CR.BAccount.AMBomOperCollection -> Collection(PX.Objects.AM.AMBomOper)
PX.Objects.CR.BAccount.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.CR.BAccount.AMEstimateOperCollection -> Collection(PX.Objects.AM.AMEstimateOper)
PX.Objects.CR.BAccount.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.CR.BAccount.AMForecastCollection -> Collection(PX.Objects.AM.AMForecast)
PX.Objects.CR.BAccount.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.CR.BAccount.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.CR.BAccount.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.CR.BAccount.AMVendorShipmentCollection -> Collection(PX.Objects.AM.AMVendorShipment)
PX.Objects.CR.BAccount.FSGeoZoneEmpCollection -> Collection(PX.Objects.FS.FSGeoZoneEmp)
PX.Objects.CR.BAccount.T4ASlipCollection -> Collection(PX.Objects.Localizations.CA.T4ASlip)
PX.Objects.CR.BAccount.PREmployeeDeductCollection -> Collection(PX.Objects.PR.PREmployeeDeduct)
PX.Objects.CR.BAccount.PRTaxRegistrationAttributeCollection -> Collection(PX.Objects.PR.PRTaxRegistrationAttribute)
PX.Objects.CR.BAccount.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CR.BAccount.SVOrderActualCollection -> Collection(PX.Objects.SV.SVOrderActual)
PX.Objects.CR.BAccount.SVServiceLocationCustomerCollection -> Collection(PX.Objects.SV.SVServiceLocationCustomer)
PX.Objects.CR.BAccount.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)
PX.Objects.CR.BAccount.SOInvoiceCollection -> Collection(PX.Objects.SO.SOInvoice)
PX.Objects.CR.BAccount.PMPOHistoryByDateCollection -> Collection(PX.Objects.PM.PMPOHistoryByDate)
PX.Objects.CR.BAccount.ARStatementDetailInfoCollection -> Collection(PX.Objects.AR.ARStatementDetailInfo)
PX.Objects.CR.BAccount.APTranPostCollection -> Collection(PX.Objects.AP.APTranPost)
PX.Objects.CR.BAccount.CCSynchronizeCardCollection -> Collection(PX.Objects.CA.CCSynchronizeCard)
PX.Objects.CR.BAccount.CustomerProcessingCenterIDCollection -> Collection(PX.Objects.CA.CustomerProcessingCenterID)
PX.Objects.CR.BAccount.AMOrderCrossRefCollection -> Collection(PX.Objects.AM.AMOrderCrossRef)
PX.Objects.CR.BAccount.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.CR.BAccount.FSLogCollection -> Collection(PX.Objects.FS.FSLog)
PX.Objects.CR.BAccount.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CR.BAccount.FSAppointmentCollection -> Collection(PX.Objects.FS.FSAppointment)
PX.Objects.CR.BAccount.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.CR.BAccount.RouteAppointmentInfoCollection -> Collection(PX.Objects.FS.RouteAppointmentInfo)
PX.Objects.CR.BAccount.FSAppointmentEmployeeCollection -> Collection(PX.Objects.FS.FSAppointmentEmployee)
PX.Objects.CR.BAccount.FSSOEmployeeCollection -> Collection(PX.Objects.FS.FSSOEmployee)
PX.Objects.CR.BAccount.FSAppointmentStaffDistinctCollection -> Collection(PX.Objects.FS.FSAppointmentStaffDistinct)
PX.Objects.CR.BAccount.FSAppointmentStaffExtItemLineCollection -> Collection(PX.Objects.FS.FSAppointmentStaffExtItemLine)
PX.Objects.CR.BAccount.POEnabledFSSODetCollection -> Collection(PX.Objects.FS.POEnabledFSSODet)
PX.Objects.CR.BAccount.FSAppointmentStaffMemberCollection -> Collection(PX.Objects.FS.FSAppointmentStaffMember)
PX.Objects.CR.BAccount.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.CR.BAccount.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.CR.BAccount.POAddressCollection -> Collection(PX.Objects.PO.POAddress)
PX.Objects.CR.BAccount.POContactCollection -> Collection(PX.Objects.PO.POContact)
PX.Objects.CR.BAccount.INTranCollection -> Collection(PX.Objects.IN.INTran)
PX.Objects.CR.BAccount.AddressCollection -> Collection(PX.Objects.CR.Address)
PX.Objects.CR.BAccount.CRAddressCollection -> Collection(PX.Objects.CR.CRAddress)
PX.Objects.CR.BAccount.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.Objects.CR.BAccount.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.Objects.CR.BAccount.FSAddressCollection -> Collection(PX.Objects.FS.FSAddress)
PX.Objects.CR.BAccount.FSContactCollection -> Collection(PX.Objects.FS.FSContact)
PX.Objects.CR.BAccount.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CR.BAccount.CABatchCollection -> Collection(PX.Objects.CA.CABatch)
PX.Objects.CR.BAccount.PPBillcomVendorCollection -> Collection(PX.PaymentProcessor.BillCom.DAC.PPBillcomVendor)
PX.Objects.CR.BAccount.VendorPaymentMethodDetailCollection -> Collection(PX.Objects.AP.VendorPaymentMethodDetail)
PX.Objects.CR.BAccount.CRRelationCollection -> Collection(PX.Objects.CR.CRRelation)
PX.Objects.CR.BAccount.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CR.BAccount.GLTranDocCollection -> Collection(PX.Objects.GL.GLTranDoc)
PX.Objects.CR.BAccount.SelContractWatcherCollection -> Collection(PX.Objects.CT.SelContractWatcher)
PX.Objects.CR.BAccount.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)
PX.Objects.CR.BAccount.PMLaborCostRateCollection -> Collection(PX.Objects.PM.PMLaborCostRate)
PX.Objects.CR.BAccount.CABankTranBAccountMappingCollection -> Collection(PX.Objects.CA.CABankTranBAccountMapping)
PX.Objects.CR.BAccount.CABankTranDetailCollection -> Collection(PX.Objects.CA.CABankTranDetail)
PX.Objects.CR.BAccount.CAEntryTypeCollection -> Collection(PX.Objects.CA.CAEntryType)
PX.Objects.CR.BAccount.RecognizedVendorMappingCollection -> Collection(PX.Objects.AP.InvoiceRecognition.DAC.RecognizedVendorMapping)
PX.Objects.CR.BAccount.TaxRegistrationCollection -> Collection(PX.Objects.Localizations.CA.TaxRegistration)
PX.Objects.CR.BAccount.CISSubcontractorCollection -> Collection(PX.Objects.Localizations.GB.CISSubcontractor)
PX.Objects.CR.BAccount.PREntityCompanyTaxAttributeCollection -> Collection(PX.Objects.PR.PREntityCompanyTaxAttribute)
PX.Objects.CR.BAccount.PREntityTaxCodeAttributeCollection -> Collection(PX.Objects.PR.PREntityTaxCodeAttribute)
PX.Objects.CR.BAccount.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.BAccount.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CR.BAccount.RequestForInformationRelationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation)
PX.Objects.CR.BAccount.CABankTranMatchCollection -> Collection(PX.Objects.CA.CABankTranMatch)
PX.Objects.CR.BAccount.AMRPDetailFPCollection -> Collection(PX.Objects.AM.AMRPDetailFP)
PX.Objects.CR.BAccount.AMRPDetailPlanCollection -> Collection(PX.Objects.AM.AMRPDetailPlan)
PX.Objects.CR.BAccount.BAccountLocationCollection -> Collection(PX.Objects.FS.BAccountLocation)
PX.Objects.CR.BAccount.CanadianVendorCollection -> Collection(PX.Objects.Localizations.CA.CanadianVendor)

# PX.Objects.CR.BAccount2 (EntityType)

Label: "Business Account"
BaseType: PX.Objects.CR.BAccount
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_CR_BAccount2

# PX.Objects.CR.BAccountParent (EntityType)

Label: "Parent Business Account"
BaseType: PX.Objects.CR.BAccount
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_CR_BAccountParent, ParentBusinessAccount, BAccountParent

# PX.Objects.CR.Building (EntityType)

Key: BranchID, BuildingCD
Entity sets: PX_Objects_CR_Building

PX.Objects.CR.Building.BuildingID : Edm.Int32 "BuildingID"
PX.Objects.CR.Building.BranchID : Edm.Int32 [key] "Branch"
PX.Objects.CR.Building.BuildingCD : Edm.String [key] "Building"
PX.Objects.CR.Building.Description : Edm.String "Description"
PX.Objects.CR.Building.tstamp : Edm.Binary
PX.Objects.CR.Building.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.Building.CreatedByScreenID : Edm.String
PX.Objects.CR.Building.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.Building.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.Building.LastModifiedByScreenID : Edm.String
PX.Objects.CR.Building.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.Building.BranchByBranchID -> PX.Objects.GL.Branch (BranchID=BranchID)
PX.Objects.CR.Building.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.Building.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.Building.FALocationHistoryCollection -> Collection(PX.Objects.FA.FALocationHistory)

# PX.Objects.CR.Contact (EntityType)

Label: "Contact"
Key: ContactID
Entity sets: PX_Objects_CR_Contact, Contact
Non-filterable, non-selectable: IsAddressSameAsMain, OverrideAddress, IsPrimary, NoteText, IsNotEmployee, HSEntityTypeID, EntityTypeID, CanBeMadePrimary, IsAddedAsExt

PX.Objects.CR.Contact.DisplayName : Edm.String "Contact"
PX.Objects.CR.Contact.MemberName : Edm.String "Member Name"
PX.Objects.CR.Contact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.CR.Contact.RevisionID : Edm.Int32 [required]
PX.Objects.CR.Contact.IsAddressSameAsMain : Edm.Boolean "Same as in Account"
PX.Objects.CR.Contact.OverrideAddress : Edm.Boolean "Override Address"
PX.Objects.CR.Contact.DefAddressID : Edm.Int32 "Address"
PX.Objects.CR.Contact.IsPrimary : Edm.Boolean "Primary"
PX.Objects.CR.Contact.Title : Edm.String "Title"
PX.Objects.CR.Contact.FirstName : Edm.String "First Name"
PX.Objects.CR.Contact.MidName : Edm.String "Middle Name"
PX.Objects.CR.Contact.LastName : Edm.String "Last Name"
PX.Objects.CR.Contact.Salutation : Edm.String "Job Title"
PX.Objects.CR.Contact.Attention : Edm.String "Attention"
PX.Objects.CR.Contact.BAccountID : Edm.Int32 "Business Account"
PX.Objects.CR.Contact.FullName : Edm.String "Account Name"
PX.Objects.CR.Contact.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.CR.Contact.EMail : Edm.String "Email"
PX.Objects.CR.Contact.WebSite : Edm.String "Web"
PX.Objects.CR.Contact.Fax : Edm.String "Fax"
PX.Objects.CR.Contact.FaxType : Edm.String "Fax Type"
PX.Objects.CR.Contact.Phone1 : Edm.String "Phone 1"
PX.Objects.CR.Contact.Phone1Type : Edm.String "Phone 1 Type"
PX.Objects.CR.Contact.Phone2 : Edm.String "Phone 2"
PX.Objects.CR.Contact.Phone2Type : Edm.String "Phone 2 Type"
PX.Objects.CR.Contact.Phone3 : Edm.String "Phone 3"
PX.Objects.CR.Contact.Phone3Type : Edm.String "Phone 3 Type"
PX.Objects.CR.Contact.DateOfBirth : Edm.DateTimeOffset "Date Of Birth"
PX.Objects.CR.Contact.NoteID : Edm.Guid "NoteID"
PX.Objects.CR.Contact.NoteText : Edm.String "Note Text"
PX.Objects.CR.Contact.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CR.Contact.IsNotEmployee : Edm.Boolean "Is Not Employee"
PX.Objects.CR.Contact.Gender : Edm.String "Gender"
PX.Objects.CR.Contact.MaritalStatus : Edm.String "Marital Status"
PX.Objects.CR.Contact.Spouse : Edm.String "Spouse/Partner Name"
PX.Objects.CR.Contact.Img : Edm.String "Image"
PX.Objects.CR.Contact.ContactType : Edm.String "Type"
PX.Objects.CR.Contact.ContactPriority : Edm.Int32 "Type"
PX.Objects.CR.Contact.DuplicateFound : Edm.Boolean "Duplicate Found"
PX.Objects.CR.Contact.Status : Edm.String "Status"
PX.Objects.CR.Contact.Resolution : Edm.String "Reason"
PX.Objects.CR.Contact.AssignDate : Edm.DateTimeOffset "Assignment Date"
PX.Objects.CR.Contact.ClassID : Edm.String "Contact Class"
PX.Objects.CR.Contact.Source : Edm.String "Source"
PX.Objects.CR.Contact.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.Contact.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.Contact.UserID : Edm.Guid
PX.Objects.CR.Contact.CampaignID : Edm.String "Source Campaign"
PX.Objects.CR.Contact.Method : Edm.String "Contact Method"
PX.Objects.CR.Contact.GrammValidationDateTime : Edm.DateTimeOffset
PX.Objects.CR.Contact.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.Contact.CreatedByScreenID : Edm.String
PX.Objects.CR.Contact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.Contact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.Contact.LastModifiedByScreenID : Edm.String
PX.Objects.CR.Contact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.Contact.SearchSuggestion : Edm.String "Search Suggestion"
PX.Objects.CR.Contact.ExtRefNbr : Edm.String "Ext. Ref. Nbr."
PX.Objects.CR.Contact.LanguageID : Edm.String "Language/Locale"
PX.Objects.CR.Contact.tstamp : Edm.Binary
PX.Objects.CR.Contact.DeletedDatabaseRecord : Edm.Boolean [required]
PX.Objects.CR.Contact.HSEntityTypeID : Edm.Int32
PX.Objects.CR.Contact.EntityTypeID : Edm.Int32
PX.Objects.CR.Contact.CanBeMadePrimary : Edm.Boolean "Can be made Primary"
PX.Objects.CR.Contact.IsMeaningfull : Edm.Boolean
PX.Objects.CR.Contact.IsAddedAsExt : Edm.Boolean
PX.Objects.CR.Contact.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CR.Contact.BAccountByParentBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID)
PX.Objects.CR.Contact.CRContactClassByClassID -> PX.Objects.CR.CRContactClass (ClassID=ClassID)
PX.Objects.CR.Contact.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.Contact.AddressByDefAddressID -> PX.Objects.CR.Address (DefAddressID=AddressID)
PX.Objects.CR.Contact.UsersByUserID -> PX.SM.Users (UserID=PKID)
PX.Objects.CR.Contact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.Contact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.Contact.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.Contact.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CR.Contact.CRCampaignByCampaignID -> PX.Objects.CR.CRCampaign (CampaignID=CampaignID)
PX.Objects.CR.Contact.LocaleByLanguageID -> PX.SM.Locale (LanguageID=LocaleName)
PX.Objects.CR.Contact.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CR.Contact.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CR.Contact.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CR.Contact.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.CR.Contact.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.CR.Contact.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CR.Contact.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CR.Contact.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CR.Contact.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.CR.Contact.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.CR.Contact.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CR.Contact.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CR.Contact.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.CR.Contact.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.Objects.CR.Contact.APPaymentCollection -> Collection(PX.Objects.AP.APPayment)
PX.Objects.CR.Contact.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.Objects.CR.Contact.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CR.Contact.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CR.Contact.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CR.Contact.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CR.Contact.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.CR.Contact.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.CR.Contact.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.CR.Contact.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.CR.Contact.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.CR.Contact.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.CR.Contact.CRMarketingListCollection -> Collection(PX.Objects.CR.CRMarketingList)
PX.Objects.CR.Contact.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CR.Contact.EPRuleCollection -> Collection(PX.Objects.EP.EPRule)
PX.Objects.CR.Contact.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.CR.Contact.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CR.Contact.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.Objects.CR.Contact.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.Objects.CR.Contact.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CR.Contact.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.CR.Contact.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.CR.Contact.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.CR.Contact.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.CR.Contact.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CR.Contact.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.CR.Contact.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.CR.Contact.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.Objects.CR.Contact.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.CR.Contact.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.Objects.CR.Contact.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CR.Contact.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.CR.Contact.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CR.Contact.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CR.Contact.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CR.Contact.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.CR.Contact.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.Objects.CR.Contact.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CR.Contact.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.CR.Contact.CRReminderCollection -> Collection(PX.Objects.CR.CRReminder)
PX.Objects.CR.Contact.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.CR.Contact.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.Objects.CR.Contact.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CR.Contact.EPAssignmentRouteCollection -> Collection(PX.Objects.EP.EPAssignmentRoute)
PX.Objects.CR.Contact.EPRuleApproverCollection -> Collection(PX.Objects.EP.DAC.EPRuleApprover)
PX.Objects.CR.Contact.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.CR.Contact.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.CR.Contact.AMEstimateClassCollection -> Collection(PX.Objects.AM.AMEstimateClass)
PX.Objects.CR.Contact.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.CR.Contact.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.CR.Contact.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.CR.Contact.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.CR.Contact.VendorRCollection -> Collection(PX.Objects.AP.VendorR)
PX.Objects.CR.Contact.ContactExtAddressCollection -> Collection(PX.Objects.CR.ContactExtAddress)
PX.Objects.CR.Contact.APQuickCheckCollection -> Collection(PX.Objects.AP.Standalone.APQuickCheck)
PX.Objects.CR.Contact.POContactCollection -> Collection(PX.Objects.PO.POContact)
PX.Objects.CR.Contact.MultipleQuoteCollection -> Collection(PX.Objects.CN.CRM.CR.DAC.MultipleQuote)
PX.Objects.CR.Contact.INSiteCollection -> Collection(PX.Objects.IN.INSite)
PX.Objects.CR.Contact.NotificationRecipientCollection -> Collection(PX.Objects.CS.NotificationRecipient)
PX.Objects.CR.Contact.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.Objects.CR.Contact.ARContactCollection -> Collection(PX.Objects.AR.ARContact)
PX.Objects.CR.Contact.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.CR.Contact.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CR.Contact.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.CR.Contact.SVEventCollection -> Collection(PX.Objects.SV.SVEvent)
PX.Objects.CR.Contact.CRCampaignMembersCollection -> Collection(PX.Objects.CR.CRCampaignMembers)
PX.Objects.CR.Contact.CRMarketingListMemberCollection -> Collection(PX.Objects.CR.CRMarketingListMember)
PX.Objects.CR.Contact.LocationCollection -> Collection(PX.Objects.CR.Location)
PX.Objects.CR.Contact.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CR.Contact.SMTeamsMemberCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsMember)
PX.Objects.CR.Contact.VPComplianceNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent)
PX.Objects.CR.Contact.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)
PX.Objects.CR.Contact.EPCompanyTreeMemberCollection -> Collection(PX.TM.EPCompanyTreeMember)
PX.Objects.CR.Contact.PMProjectContactCollection -> Collection(PX.Objects.PM.PMProjectContact)
PX.Objects.CR.Contact.CRMassMailMemberCollection -> Collection(PX.Objects.CR.CRMassMailMember)
PX.Objects.CR.Contact.EPAttendeeCollection -> Collection(PX.Objects.EP.EPAttendee)
PX.Objects.CR.Contact.APContactCollection -> Collection(PX.Objects.AP.APContact)
PX.Objects.CR.Contact.HSMarketingListMemberCollection -> Collection(PX.DataSync.HubSpot.HSMarketingListMember)
PX.Objects.CR.Contact.ESignRecipientCollection -> Collection(PX.ESign.ESignRecipient)
PX.Objects.CR.Contact.FSManufacturerCollection -> Collection(PX.Objects.FS.FSManufacturer)
PX.Objects.CR.Contact.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.CR.Contact.PRTaxReportingAccountCollection -> Collection(PX.Objects.PR.PRTaxReportingAccount)
PX.Objects.CR.Contact.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CR.Contact.SVServiceLocationContactCollection -> Collection(PX.Objects.SV.SVServiceLocationContact)
PX.Objects.CR.Contact.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.Contact.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CR.Contact.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)
PX.Objects.CR.Contact.BCRoleAssignmentCollection -> Collection(PX.Commerce.Shopify.BCRoleAssignment)
PX.Objects.CR.Contact.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)
PX.Objects.CR.Contact.RequestForInformationRelationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformationRelation)

# PX.Objects.CR.Contact2 (EntityType)

Label: "Contact"
BaseType: PX.Objects.CR.Contact
Key: ContactID (inherited from PX.Objects.CR.Contact)
Entity sets: PX_Objects_CR_Contact2, Contact1, Contact2

# PX.Objects.CR.ContactAccount (EntityType)

Label: "Contact"
BaseType: PX.Objects.CR.Contact
Key: ContactID (inherited from PX.Objects.CR.Contact)
Entity sets: PX_Objects_CR_ContactAccount

PX.Objects.CR.ContactAccount.AcctName : Edm.String "Account Name"
PX.Objects.CR.ContactAccount.Type : Edm.String "Type"
PX.Objects.CR.ContactAccount.AccountStatus : Edm.String "Status"
PX.Objects.CR.ContactAccount.DefContactID : Edm.Int32
PX.Objects.CR.ContactAccount.PrimaryContactID : Edm.Int32 "Primary Contact"
PX.Objects.CR.ContactAccount.ContactByDefContactID -> PX.Objects.CR.Contact (DefContactID=ContactID)
PX.Objects.CR.ContactAccount.ContactByPrimaryContactID -> PX.Objects.CR.Contact (PrimaryContactID=ContactID)
PX.Objects.CR.ContactAccount.ContactByBAccountID -> PX.Objects.CR.Contact (PrimaryContactID=ContactID, BAccountID=BAccountID)

# PX.Objects.CR.ContactExtAddress (EntityType)

Label: "Contact with Address"
BaseType: PX.Objects.CR.Address
Key: AddressID (inherited from PX.Objects.CR.Address)
Entity sets: PX_Objects_CR_ContactExtAddress, ContactwithAddress, ContactExtAddress
Non-filterable, non-selectable: IsDefault, IsAddressSameAsMain

PX.Objects.CR.ContactExtAddress.ContactBAccountID : Edm.Int32 "Business Account ID"
PX.Objects.CR.ContactExtAddress.ContactID : Edm.Int32 "ContactID"
PX.Objects.CR.ContactExtAddress.DefAddressID : Edm.Int32 "Default Address"
PX.Objects.CR.ContactExtAddress.Title : Edm.String "Position"
PX.Objects.CR.ContactExtAddress.Salutation : Edm.String "Job Title"
PX.Objects.CR.ContactExtAddress.FirstName : Edm.String "First Name"
PX.Objects.CR.ContactExtAddress.MidName : Edm.String "Middle Name"
PX.Objects.CR.ContactExtAddress.LastName : Edm.String "Last Name"
PX.Objects.CR.ContactExtAddress.FullName : Edm.String
PX.Objects.CR.ContactExtAddress.EMail : Edm.String "Email"
PX.Objects.CR.ContactExtAddress.WebSite : Edm.String "Web"
PX.Objects.CR.ContactExtAddress.Fax : Edm.String "Fax"
PX.Objects.CR.ContactExtAddress.FaxType : Edm.String "Fax"
PX.Objects.CR.ContactExtAddress.Phone1 : Edm.String "Phone 1"
PX.Objects.CR.ContactExtAddress.Phone1Type : Edm.String "Phone 1"
PX.Objects.CR.ContactExtAddress.Phone2 : Edm.String "Phone 2"
PX.Objects.CR.ContactExtAddress.Phone2Type : Edm.String "Phone 2"
PX.Objects.CR.ContactExtAddress.Phone3 : Edm.String "Phone 3"
PX.Objects.CR.ContactExtAddress.Phone3Type : Edm.String "Phone 3"
PX.Objects.CR.ContactExtAddress.DateOfBirth : Edm.DateTimeOffset "Date Of Birth"
PX.Objects.CR.ContactExtAddress.ContactType : Edm.String
PX.Objects.CR.ContactExtAddress.IsActive : Edm.Boolean "Active"
PX.Objects.CR.ContactExtAddress.ContactNoteID : Edm.Guid
PX.Objects.CR.ContactExtAddress.ContactCreatedByID : Edm.Guid "Created By"
PX.Objects.CR.ContactExtAddress.ContactCreatedByScreenID : Edm.String
PX.Objects.CR.ContactExtAddress.ContactCreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.ContactExtAddress.ContactLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.ContactExtAddress.ContactLastModifiedByScreenID : Edm.String
PX.Objects.CR.ContactExtAddress.ContactLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.ContactExtAddress.IsDefault : Edm.Boolean "Is Default"
PX.Objects.CR.ContactExtAddress.IsAddressSameAsMain : Edm.Boolean "Same as Main"
PX.Objects.CR.ContactExtAddress.ContactDisplayName : Edm.String "Name"
PX.Objects.CR.ContactExtAddress.ContactByContactDisplayName -> PX.Objects.CR.Contact (ContactDisplayName=DisplayName)
PX.Objects.CR.ContactExtAddress.BAccountByParentBAccountID -> PX.Objects.CR.BAccount
PX.Objects.CR.ContactExtAddress.AddressByDefAddressID -> PX.Objects.CR.Address (DefAddressID=AddressID)
PX.Objects.CR.ContactExtAddress.UsersByUserID -> PX.SM.Users
PX.Objects.CR.ContactExtAddress.EPEmployeeFSRouteEmployeeCollection -> Collection(PX.Objects.FS.EPEmployeeFSRouteEmployee)
PX.Objects.CR.ContactExtAddress.ARRetainageWithApplicationsCollection -> Collection(PX.Objects.AR.ARRetainageWithApplications)
PX.Objects.CR.ContactExtAddress.ARPaymentCollection -> Collection(PX.Objects.AR.ARPayment)
PX.Objects.CR.ContactExtAddress.PMProjectCollection -> Collection(PX.Objects.PM.PMProject)
PX.Objects.CR.ContactExtAddress.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.CR.ContactExtAddress.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.CR.ContactExtAddress.ARInvoiceCollection -> Collection(PX.Objects.AR.ARInvoice)
PX.Objects.CR.ContactExtAddress.APInvoiceCollection -> Collection(PX.Objects.AP.APInvoice)
PX.Objects.CR.ContactExtAddress.RequestForInformationCollection -> Collection(PX.Objects.PJ.RequestsForInformation.PJ.DAC.RequestForInformation)
PX.Objects.CR.ContactExtAddress.ProjectIssueCollection -> Collection(PX.Objects.PJ.ProjectsIssue.PJ.DAC.ProjectIssue)
PX.Objects.CR.ContactExtAddress.DrawingLogCollection -> Collection(PX.Objects.PJ.DrawingLogs.PJ.DAC.DrawingLog)
PX.Objects.CR.ContactExtAddress.ARRegisterCollection -> Collection(PX.Objects.AR.ARRegister)
PX.Objects.CR.ContactExtAddress.SOOrderCollection -> Collection(PX.Objects.SO.SOOrder)
PX.Objects.CR.ContactExtAddress.POOrderCollection -> Collection(PX.Objects.PO.POOrder)
PX.Objects.CR.ContactExtAddress.ContractCollection -> Collection(PX.Objects.CT.Contract)
PX.Objects.CR.ContactExtAddress.INItemClassCollection -> Collection(PX.Objects.IN.INItemClass)
PX.Objects.CR.ContactExtAddress.InventoryItemCollection -> Collection(PX.Objects.IN.InventoryItem)
PX.Objects.CR.ContactExtAddress.INRegisterCollection -> Collection(PX.Objects.IN.INRegister)
PX.Objects.CR.ContactExtAddress.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.CR.ContactExtAddress.CRMarketingListCollection -> Collection(PX.Objects.CR.CRMarketingList)
PX.Objects.CR.ContactExtAddress.APRegisterCollection -> Collection(PX.Objects.AP.APRegister)
PX.Objects.CR.ContactExtAddress.EPRuleCollection -> Collection(PX.Objects.EP.EPRule)
PX.Objects.CR.ContactExtAddress.EPExpenseClaimCollection -> Collection(PX.Objects.EP.EPExpenseClaim)
PX.Objects.CR.ContactExtAddress.RQRequisitionCollection -> Collection(PX.Objects.RQ.RQRequisition)
PX.Objects.CR.ContactExtAddress.PMCostProjectionByDateCollection -> Collection(PX.Objects.PM.PMCostProjectionByDate)
PX.Objects.CR.ContactExtAddress.EPApprovalCollection -> Collection(PX.Objects.EP.EPApproval)
PX.Objects.CR.ContactExtAddress.EPExpenseClaimDetailsCollection -> Collection(PX.Objects.EP.EPExpenseClaimDetails)
PX.Objects.CR.ContactExtAddress.AMProdItemCollection -> Collection(PX.Objects.AM.AMProdItem)
PX.Objects.CR.ContactExtAddress.AMBomItemCollection -> Collection(PX.Objects.AM.AMBomItem)
PX.Objects.CR.ContactExtAddress.PJSubmittalCollection -> Collection(PX.Objects.PJ.Submittals.PJ.DAC.PJSubmittal)
PX.Objects.CR.ContactExtAddress.DailyFieldReportCollection -> Collection(PX.Objects.PJ.DailyFieldReports.PJ.DAC.DailyFieldReport)
PX.Objects.CR.ContactExtAddress.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CR.ContactExtAddress.PMChangeOrderCollection -> Collection(PX.Objects.PM.PMChangeOrder)
PX.Objects.CR.ContactExtAddress.INItemSiteCollection -> Collection(PX.Objects.IN.INItemSite)
PX.Objects.CR.ContactExtAddress.PMProjectCostSpreadCollection -> Collection(PX.Objects.PM.PMProjectCostSpread)
PX.Objects.CR.ContactExtAddress.AMEstimateItemCollection -> Collection(PX.Objects.AM.AMEstimateItem)
PX.Objects.CR.ContactExtAddress.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.Objects.CR.ContactExtAddress.SOShipmentCollection -> Collection(PX.Objects.SO.SOShipment)
PX.Objects.CR.ContactExtAddress.RQRequestCollection -> Collection(PX.Objects.RQ.RQRequest)
PX.Objects.CR.ContactExtAddress.POLandedCostDocCollection -> Collection(PX.Objects.PO.POLandedCostDoc)
PX.Objects.CR.ContactExtAddress.POReceiptCollection -> Collection(PX.Objects.PO.POReceipt)
PX.Objects.CR.ContactExtAddress.POLandedCostDocSCollection -> Collection(PX.Objects.PO.POLandedCostDocS)
PX.Objects.CR.ContactExtAddress.PMChangeRequestCollection -> Collection(PX.Objects.PM.PMChangeRequest)
PX.Objects.CR.ContactExtAddress.PMCostProjectionCollection -> Collection(PX.Objects.PM.PMCostProjection)
PX.Objects.CR.ContactExtAddress.PMProformaCollection -> Collection(PX.Objects.PM.PMProforma)
PX.Objects.CR.ContactExtAddress.PMWipAdjustmentCollection -> Collection(PX.Objects.PM.PMWipAdjustment)
PX.Objects.CR.ContactExtAddress.CRReminderCollection -> Collection(PX.Objects.CR.CRReminder)
PX.Objects.CR.ContactExtAddress.CADepositCollection -> Collection(PX.Objects.CA.CADeposit)
PX.Objects.CR.ContactExtAddress.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)
PX.Objects.CR.ContactExtAddress.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CR.ContactExtAddress.EPAssignmentRouteCollection -> Collection(PX.Objects.EP.EPAssignmentRoute)
PX.Objects.CR.ContactExtAddress.EPRuleApproverCollection -> Collection(PX.Objects.EP.DAC.EPRuleApprover)
PX.Objects.CR.ContactExtAddress.AMECOItemCollection -> Collection(PX.Objects.AM.AMECOItem)
PX.Objects.CR.ContactExtAddress.AMECRItemCollection -> Collection(PX.Objects.AM.AMECRItem)
PX.Objects.CR.ContactExtAddress.AMEstimateClassCollection -> Collection(PX.Objects.AM.AMEstimateClass)
PX.Objects.CR.ContactExtAddress.AMMRPBucketInqCollection -> Collection(PX.Objects.AM.AMMRPBucketInq)
PX.Objects.CR.ContactExtAddress.AMRPDetailCollection -> Collection(PX.Objects.AM.AMRPDetail)
PX.Objects.CR.ContactExtAddress.AMRPItemSiteCollection -> Collection(PX.Objects.AM.AMRPItemSite)
PX.Objects.CR.ContactExtAddress.AMRPExceptionsCollection -> Collection(PX.Objects.AM.AMRPExceptions)
PX.Objects.CR.ContactExtAddress.POContactCollection -> Collection(PX.Objects.PO.POContact)
PX.Objects.CR.ContactExtAddress.MultipleQuoteCollection -> Collection(PX.Objects.CN.CRM.CR.DAC.MultipleQuote)
PX.Objects.CR.ContactExtAddress.NotificationRecipientCollection -> Collection(PX.Objects.CS.NotificationRecipient)
PX.Objects.CR.ContactExtAddress.CRContactCollection -> Collection(PX.Objects.CR.CRContact)
PX.Objects.CR.ContactExtAddress.ARContactCollection -> Collection(PX.Objects.AR.ARContact)
PX.Objects.CR.ContactExtAddress.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.CR.ContactExtAddress.FSServiceOrderCollection -> Collection(PX.Objects.FS.FSServiceOrder)
PX.Objects.CR.ContactExtAddress.FSAppointmentFSServiceOrderCollection -> Collection(PX.Objects.FS.FSAppointmentFSServiceOrder)
PX.Objects.CR.ContactExtAddress.SVEventCollection -> Collection(PX.Objects.SV.SVEvent)
PX.Objects.CR.ContactExtAddress.CRCampaignMembersCollection -> Collection(PX.Objects.CR.CRCampaignMembers)
PX.Objects.CR.ContactExtAddress.CRMarketingListMemberCollection -> Collection(PX.Objects.CR.CRMarketingListMember)
PX.Objects.CR.ContactExtAddress.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CR.ContactExtAddress.SMTeamsMemberCollection -> Collection(PX.MSTeams.DAC.SM.SMTeamsMember)
PX.Objects.CR.ContactExtAddress.VPComplianceNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPComplianceNotificationEvent)
PX.Objects.CR.ContactExtAddress.VPSecurityNotificationEventCollection -> Collection(PX.Objects.Portals.Vendor.Configuration.VPSecurityNotificationEvent)
PX.Objects.CR.ContactExtAddress.EPCompanyTreeMemberCollection -> Collection(PX.TM.EPCompanyTreeMember)
PX.Objects.CR.ContactExtAddress.PMProjectContactCollection -> Collection(PX.Objects.PM.PMProjectContact)
PX.Objects.CR.ContactExtAddress.CRMassMailMemberCollection -> Collection(PX.Objects.CR.CRMassMailMember)
PX.Objects.CR.ContactExtAddress.EPAttendeeCollection -> Collection(PX.Objects.EP.EPAttendee)
PX.Objects.CR.ContactExtAddress.APContactCollection -> Collection(PX.Objects.AP.APContact)
PX.Objects.CR.ContactExtAddress.HSMarketingListMemberCollection -> Collection(PX.DataSync.HubSpot.HSMarketingListMember)
PX.Objects.CR.ContactExtAddress.ESignRecipientCollection -> Collection(PX.ESign.ESignRecipient)
PX.Objects.CR.ContactExtAddress.FSManufacturerCollection -> Collection(PX.Objects.FS.FSManufacturer)
PX.Objects.CR.ContactExtAddress.FSServiceContractCollection -> Collection(PX.Objects.FS.FSServiceContract)
PX.Objects.CR.ContactExtAddress.PRTaxReportingAccountCollection -> Collection(PX.Objects.PR.PRTaxReportingAccount)
PX.Objects.CR.ContactExtAddress.SVOrderCollection -> Collection(PX.Objects.SV.SVOrder)
PX.Objects.CR.ContactExtAddress.SVServiceLocationContactCollection -> Collection(PX.Objects.SV.SVServiceLocationContact)
PX.Objects.CR.ContactExtAddress.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.ContactExtAddress.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CR.ContactExtAddress.CustomerMasterCollection -> Collection(PX.Objects.AR.CustomerMaster)
PX.Objects.CR.ContactExtAddress.BCRoleAssignmentCollection -> Collection(PX.Commerce.Shopify.BCRoleAssignment)
PX.Objects.CR.ContactExtAddress.SchedulerServiceOrderCollection -> Collection(PX.Objects.FS.SchedulerServiceOrder)

# PX.Objects.CR.ContactNotification (EntityType)

Label: "Contact Notification"
BaseType: PX.Objects.CS.NotificationRecipient
Key: NotificationID (inherited from PX.Objects.CS.NotificationRecipient)
Entity sets: PX_Objects_CR_ContactNotification, ContactNotification
Non-filterable, non-selectable: EntityDescription

PX.Objects.CR.ContactNotification.EntityDescription : Edm.String "Description"
PX.Objects.CR.ContactNotification.SourceClassID : Edm.String
PX.Objects.CR.ContactNotification.ReportID : Edm.String "Report"
PX.Objects.CR.ContactNotification.TemplateID : Edm.Int32 "Email Template"
PX.Objects.CR.ContactNotification.KeySourceID : Edm.Int32
PX.Objects.CR.ContactNotification.KeySetupID : Edm.Guid
PX.Objects.CR.ContactNotification.NotificationByTemplateID -> PX.SM.Notification (TemplateID=NotificationID)

# PX.Objects.CR.CRActivity (EntityType)

Label: "Activity"
Key: NoteID
Entity sets: PX_Objects_CR_CRActivity, Activity, CRActivity
Non-filterable, non-selectable: NoteText, Source, ClassIcon, ClassInfo, PriorityIcon, IsOverdue, IsCompleteIcon, DayOfWeek, SelectorDescription, EntityDescription, IsPinned

PX.Objects.CR.CRActivity.NoteID : Edm.Guid [key] "ID"
PX.Objects.CR.CRActivity.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRActivity.ParentNoteID : Edm.Guid "Parent Activity"
PX.Objects.CR.CRActivity.RefNoteIDType : Edm.String "Related Entity Type"
PX.Objects.CR.CRActivity.RefNoteID : Edm.Guid "Related Entity"
PX.Objects.CR.CRActivity.DocumentNoteID : Edm.Guid "Related Document"
PX.Objects.CR.CRActivity.Source : Edm.String "Related Entity"
PX.Objects.CR.CRActivity.ClassID : Edm.Int32 [required] "Class"
PX.Objects.CR.CRActivity.ClassIcon : Edm.String "Class Icon"
PX.Objects.CR.CRActivity.ClassInfo : Edm.String "Type"
PX.Objects.CR.CRActivity.Type : Edm.String "Type"
PX.Objects.CR.CRActivity.Subject : Edm.String "Summary"
PX.Objects.CR.CRActivity.Location : Edm.String "Location"
PX.Objects.CR.CRActivity.Body : Edm.String "Activity Details"
PX.Objects.CR.CRActivity.Priority : Edm.Int32 "Priority"
PX.Objects.CR.CRActivity.PriorityIcon : Edm.String "Priority Icon"
PX.Objects.CR.CRActivity.UIStatus : Edm.String "Status"
PX.Objects.CR.CRActivity.IsOverdue : Edm.Boolean
PX.Objects.CR.CRActivity.IsCompleteIcon : Edm.String "Complete Icon"
PX.Objects.CR.CRActivity.CategoryID : Edm.Int32 "Category"
PX.Objects.CR.CRActivity.AllDay : Edm.Boolean "All Day"
PX.Objects.CR.CRActivity.TimeZone : Edm.String "Time Zone"
PX.Objects.CR.CRActivity.CompletedDate : Edm.DateTimeOffset "Completed On"
PX.Objects.CR.CRActivity.DayOfWeek : Edm.Int32 "Day Of Week"
PX.Objects.CR.CRActivity.PercentCompletion : Edm.Int32 "Completion (%)"
PX.Objects.CR.CRActivity.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.CRActivity.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.CR.CRActivity.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.CR.CRActivity.SelectorDescription : Edm.String "Description"
PX.Objects.CR.CRActivity.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.CRActivity.IsExternal : Edm.Boolean "IsExternal"
PX.Objects.CR.CRActivity.IsPrivate : Edm.Boolean "Internal"
PX.Objects.CR.CRActivity.ProvidesCaseSolution : Edm.Boolean [required] "Case Solution Provided"
PX.Objects.CR.CRActivity.Incoming : Edm.Boolean "Incoming"
PX.Objects.CR.CRActivity.Outgoing : Edm.Boolean "Outgoing"
PX.Objects.CR.CRActivity.Synchronize : Edm.Boolean "Synchronize"
PX.Objects.CR.CRActivity.BAccountID : Edm.Int32 "Related Account"
PX.Objects.CR.CRActivity.ContactID : Edm.Int32 "Related Contact"
PX.Objects.CR.CRActivity.EntityDescription : Edm.String "Entity"
PX.Objects.CR.CRActivity.MarketingCategoryID : Edm.String "Marketing Category"
PX.Objects.CR.CRActivity.ShowAsID : Edm.Int32 "Show As"
PX.Objects.CR.CRActivity.IsLocked : Edm.Boolean [required] "Is Locked"
PX.Objects.CR.CRActivity.Application : Edm.Int32 "Originated By"
PX.Objects.CR.CRActivity.DeletedDatabaseRecord : Edm.Boolean [required]
PX.Objects.CR.CRActivity.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.CR.CRActivity.CreatedByScreenID : Edm.String
PX.Objects.CR.CRActivity.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.CRActivity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRActivity.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRActivity.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRActivity.tstamp : Edm.Binary
PX.Objects.CR.CRActivity.IsPinned : Edm.String "Is Pinned"
PX.Objects.CR.CRActivity.VendorByOwnerID -> PX.Objects.AP.Vendor (OwnerID=BAccountID)
PX.Objects.CR.CRActivity.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CR.CRActivity.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CR.CRActivity.ContactByParentNoteID -> PX.Objects.CR.Contact (ParentNoteID=ContactID)
PX.Objects.CR.CRActivity.ContactByResponseActivityNoteID -> PX.Objects.CR.Contact
PX.Objects.CR.CRActivity.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.CRActivity.CRActivityByParentNoteID -> PX.Objects.CR.CRActivity (ParentNoteID=NoteID)
PX.Objects.CR.CRActivity.CRActivityByOutgoing -> PX.Objects.CR.CRActivity (Outgoing=Incoming)
PX.Objects.CR.CRActivity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRActivity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRActivity.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.CRActivity.CRMarketingCategoryByMarketingCategoryID -> PX.Objects.CR.CRMarketingCategory (MarketingCategoryID=MarketingCategoryID)
PX.Objects.CR.CRActivity.EPEventCategoryByCategoryID -> PX.Objects.EP.EPEventCategory (CategoryID=CategoryID)
PX.Objects.CR.CRActivity.EPActivityTypeByType -> PX.Objects.EP.EPActivityType (Type=Type)
PX.Objects.CR.CRActivity.EPActivityTypeByClassID -> PX.Objects.EP.EPActivityType (Type=Type, ClassID=ClassID)
PX.Objects.CR.CRActivity.CRActivityStatisticsByRefNoteID -> PX.Objects.CR.CRActivityStatistics (RefNoteID=NoteID)
PX.Objects.CR.CRActivity.SMTeamsActivityCollection -> Collection(PX.Objects.CR.SMTeamsActivity)
PX.Objects.CR.CRActivity.CRReminderCollection -> Collection(PX.Objects.CR.CRReminder)
PX.Objects.CR.CRActivity.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CR.CRActivity.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.CR.CRActivity.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.CR.CRActivity.EPActivityReleaseCollection -> Collection(PX.Objects.EP.EPActivityRelease)
PX.Objects.CR.CRActivity.EPActivityApprove2Collection -> Collection(PX.Objects.EP.EPActivityApprove2)
PX.Objects.CR.CRActivity.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.CR.CRActivity.PMTimeActivityCollection -> Collection(PX.Objects.CR.PMTimeActivity)
PX.Objects.CR.CRActivity.EPTimeCardSummaryCollection -> Collection(PX.Objects.EP.EPTimeCardSummary)
PX.Objects.CR.CRActivity.SMEmailCollection -> Collection(PX.Objects.CR.SMEmail)
PX.Objects.CR.CRActivity.EPAttendeeCollection -> Collection(PX.Objects.EP.EPAttendee)

# PX.Objects.CR.CRActivityStatistics (EntityType)

Label: "Activity Statistics"
Key: NoteID
Entity sets: PX_Objects_CR_CRActivityStatistics, ActivityStatistics, CRActivityStatistics

PX.Objects.CR.CRActivityStatistics.NoteID : Edm.Guid [key]
PX.Objects.CR.CRActivityStatistics.LastIncomingActivityNoteID : Edm.Guid
PX.Objects.CR.CRActivityStatistics.LastOutgoingActivityNoteID : Edm.Guid
PX.Objects.CR.CRActivityStatistics.LastIncomingActivityDate : Edm.DateTimeOffset "Last Incoming Activity"
PX.Objects.CR.CRActivityStatistics.LastOutgoingActivityDate : Edm.DateTimeOffset "Last Outgoing Activity"
PX.Objects.CR.CRActivityStatistics.InitialOutgoingActivityCompletedAtNoteID : Edm.Guid
PX.Objects.CR.CRActivityStatistics.InitialOutgoingActivityCompletedAtDate : Edm.DateTimeOffset "First Outgoing Activity"
PX.Objects.CR.CRActivityStatistics.LastActivityDate : Edm.DateTimeOffset "Last Activity"
PX.Objects.CR.CRActivityStatistics.LastActivityAging : Edm.Int32 "Last Activity Aging"
PX.Objects.CR.CRActivityStatistics.InitialIncomingActivityNoteID : Edm.Guid
PX.Objects.CR.CRActivityStatistics.InitialIncomingActivityDate : Edm.DateTimeOffset
PX.Objects.CR.CRActivityStatistics.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)

# PX.Objects.CR.CRAddress (EntityType)

Label: "Opportunity Address"
Key: AddressID
Entity sets: PX_Objects_CR_CRAddress, OpportunityAddress, CRAddress
Non-filterable, non-selectable: OverrideAddress

PX.Objects.CR.CRAddress.AddressID : Edm.Int32 [key] "Address ID"
PX.Objects.CR.CRAddress.BAccountID : Edm.Int32
PX.Objects.CR.CRAddress.BAccountAddressID : Edm.Int32
PX.Objects.CR.CRAddress.IsDefaultAddress : Edm.Boolean "Default Customer Address"
PX.Objects.CR.CRAddress.OverrideAddress : Edm.Boolean "Override Address"
PX.Objects.CR.CRAddress.RevisionID : Edm.Int32
PX.Objects.CR.CRAddress.AddressLine1 : Edm.String "Address Line 1"
PX.Objects.CR.CRAddress.AddressLine2 : Edm.String "Address Line 2"
PX.Objects.CR.CRAddress.AddressLine3 : Edm.String "Address Line 3"
PX.Objects.CR.CRAddress.City : Edm.String "City"
PX.Objects.CR.CRAddress.CountryID : Edm.String "Country"
PX.Objects.CR.CRAddress.State : Edm.String "State"
PX.Objects.CR.CRAddress.PostalCode : Edm.String "Postal Code"
PX.Objects.CR.CRAddress.Department : Edm.String "Department"
PX.Objects.CR.CRAddress.SubDepartment : Edm.String "Subdepartment"
PX.Objects.CR.CRAddress.StreetName : Edm.String "Street Name"
PX.Objects.CR.CRAddress.BuildingNumber : Edm.String "Building Number"
PX.Objects.CR.CRAddress.BuildingName : Edm.String "Building Name"
PX.Objects.CR.CRAddress.Floor : Edm.String "Floor"
PX.Objects.CR.CRAddress.UnitNumber : Edm.String "Unit Number"
PX.Objects.CR.CRAddress.PostBox : Edm.String "Post Box"
PX.Objects.CR.CRAddress.Room : Edm.String "Room"
PX.Objects.CR.CRAddress.TownLocationName : Edm.String "Town Location Name"
PX.Objects.CR.CRAddress.DistrictName : Edm.String "District Name"
PX.Objects.CR.CRAddress.AddressType : Edm.String "Address Type"
PX.Objects.CR.CRAddress.CareOf : Edm.String "Care Of"
PX.Objects.CR.CRAddress.NoteID : Edm.Guid
PX.Objects.CR.CRAddress.tstamp : Edm.Binary
PX.Objects.CR.CRAddress.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRAddress.CreatedByScreenID : Edm.String
PX.Objects.CR.CRAddress.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRAddress.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRAddress.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRAddress.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRAddress.Latitude : Edm.Decimal "Latitude"
PX.Objects.CR.CRAddress.Longitude : Edm.Decimal "Longitude"
PX.Objects.CR.CRAddress.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CR.CRAddress.AddressByBAccountAddressID -> PX.Objects.CR.Address (BAccountAddressID=AddressID)
PX.Objects.CR.CRAddress.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRAddress.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRAddress.CountryByCountryID -> PX.Objects.CS.Country (CountryID=CountryID)
PX.Objects.CR.CRAddress.StateByState -> PX.Objects.CS.State (CountryID=CountryID, State=StateID)
PX.Objects.CR.CRAddress.StateByCountryID -> PX.Objects.CS.State (State=StateID, CountryID=CountryID)
PX.Objects.CR.CRAddress.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.CRAddress.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)

# PX.Objects.CR.CRBillingAddress (EntityType)

Label: "Bill-To Address"
BaseType: PX.Objects.CR.CRAddress
Key: AddressID (inherited from PX.Objects.CR.CRAddress)
Entity sets: PX_Objects_CR_CRBillingAddress, BillToAddress, CRBillingAddress

# PX.Objects.CR.CRBillingContact (EntityType)

Label: "Bill-To Contact"
BaseType: PX.Objects.CR.CRContact
Key: ContactID (inherited from PX.Objects.CR.CRContact)
Entity sets: PX_Objects_CR_CRBillingContact, BillToContact, CRBillingContact

# PX.Objects.CR.CRCampaign (EntityType)

Label: "Campaign"
Key: CampaignID
Entity sets: PX_Objects_CR_CRCampaign, Campaign, CRCampaign
Non-filterable, non-selectable: DescriptionAsPlainText, SendFilter, NoteText

PX.Objects.CR.CRCampaign.CampaignID : Edm.String [key] "Campaign ID"
PX.Objects.CR.CRCampaign.CampaignName : Edm.String "Campaign Name"
PX.Objects.CR.CRCampaign.Description : Edm.String "Description"
PX.Objects.CR.CRCampaign.DescriptionAsPlainText : Edm.String "DescriptionAsPlainText"
PX.Objects.CR.CRCampaign.CampaignType : Edm.String "Campaign Class"
PX.Objects.CR.CRCampaign.Status : Edm.String "Stage"
PX.Objects.CR.CRCampaign.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CR.CRCampaign.StartDate : Edm.DateTimeOffset "Start Date"
PX.Objects.CR.CRCampaign.EndDate : Edm.DateTimeOffset "End Date"
PX.Objects.CR.CRCampaign.ExpectedRevenue : Edm.Decimal "Expected Return"
PX.Objects.CR.CRCampaign.PlannedBudget : Edm.Decimal "Planned Budget"
PX.Objects.CR.CRCampaign.ExpectedResponse : Edm.Int32 "Expected Response"
PX.Objects.CR.CRCampaign.MailsSent : Edm.Int32 "Mails Sent"
PX.Objects.CR.CRCampaign.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.CRCampaign.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.CRCampaign.PromoCodeID : Edm.String "Promo Code"
PX.Objects.CR.CRCampaign.SendFilter : Edm.String "Sent Emails Filter"
PX.Objects.CR.CRCampaign.ProjectTaskID : Edm.Int32 "Project Task ID"
PX.Objects.CR.CRCampaign.tstamp : Edm.Binary
PX.Objects.CR.CRCampaign.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.CRCampaign.CreatedByScreenID : Edm.String
PX.Objects.CR.CRCampaign.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRCampaign.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRCampaign.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRCampaign.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.CRCampaign.NoteID : Edm.Guid
PX.Objects.CR.CRCampaign.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRCampaign.PMProjectByProjectID -> PX.Objects.PM.PMProject
PX.Objects.CR.CRCampaign.PMTaskByProjectTaskID -> PX.Objects.PM.PMTask (ProjectTaskID=TaskID)
PX.Objects.CR.CRCampaign.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.CRCampaign.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRCampaign.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRCampaign.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.CRCampaign.CRCampaignTypeByCampaignType -> PX.Objects.CR.CRCampaignType (CampaignType=TypeID)
PX.Objects.CR.CRCampaign.EPEmployeeCollection -> Collection(PX.Objects.EP.EPEmployee)
PX.Objects.CR.CRCampaign.VendorCollection -> Collection(PX.Objects.AP.Vendor)
PX.Objects.CR.CRCampaign.CustomerCollection -> Collection(PX.Objects.AR.Customer)
PX.Objects.CR.CRCampaign.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CR.CRCampaign.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.CR.CRCampaign.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.CR.CRCampaign.CRCampaignMembersCollection -> Collection(PX.Objects.CR.CRCampaignMembers)
PX.Objects.CR.CRCampaign.CROpportunityRevisionCollection -> Collection(PX.Objects.CR.Standalone.CROpportunityRevision)
PX.Objects.CR.CRCampaign.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.CRCampaign.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CR.CRCampaign.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)
PX.Objects.CR.CRCampaign.CRCampaignToCRMarketingListLinkCollection -> Collection(PX.Objects.CR.CRCampaignToCRMarketingListLink)

# PX.Objects.CR.CRCampaignMembers (EntityType)

Label: "Campaign Members"
Key: CampaignID, ContactID
Entity sets: PX_Objects_CR_CRCampaignMembers, CampaignMembers, CRCampaignMembers

PX.Objects.CR.CRCampaignMembers.CampaignID : Edm.String [key] "Campaign ID"
PX.Objects.CR.CRCampaignMembers.ContactID : Edm.Int32 [key] "Member Name"
PX.Objects.CR.CRCampaignMembers.OpportunityCreatedCount : Edm.Int32 "Opportunities Created"
PX.Objects.CR.CRCampaignMembers.IncomingActivitiesLogged : Edm.Int32 "Incoming Activities Logged"
PX.Objects.CR.CRCampaignMembers.OutgoingActivitiesLogged : Edm.Int32 "Outgoing Activities Logged"
PX.Objects.CR.CRCampaignMembers.ActivitiesLogged : Edm.Int32 "Activities Logged"
PX.Objects.CR.CRCampaignMembers.EmailSendCount : Edm.Int32 "Emails Sent"
PX.Objects.CR.CRCampaignMembers.MarketingListID : Edm.Int32 "MarketingListID"
PX.Objects.CR.CRCampaignMembers.tstamp : Edm.Binary
PX.Objects.CR.CRCampaignMembers.CreatedByScreenID : Edm.String
PX.Objects.CR.CRCampaignMembers.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRCampaignMembers.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCampaignMembers.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRCampaignMembers.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRCampaignMembers.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCampaignMembers.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CR.CRCampaignMembers.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRCampaignMembers.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRCampaignMembers.CRCampaignByCampaignID -> PX.Objects.CR.CRCampaign (CampaignID=CampaignID)
PX.Objects.CR.CRCampaignMembers.CRMarketingListByMarketingListID -> PX.Objects.CR.CRMarketingList (MarketingListID=MarketingListID)

# PX.Objects.CR.CRCampaignToCRMarketingListLink (EntityType)

Label: "CRCampaign To CRMarketingList Link"
Key: CampaignID, MarketingListID
Entity sets: PX_Objects_CR_CRCampaignToCRMarketingListLink, CRCampaignToCRMarketingListLink

PX.Objects.CR.CRCampaignToCRMarketingListLink.SelectedForCampaign : Edm.Boolean [required] "Selected"
PX.Objects.CR.CRCampaignToCRMarketingListLink.CampaignID : Edm.String [key] "Campaign ID"
PX.Objects.CR.CRCampaignToCRMarketingListLink.MarketingListID : Edm.Int32 [key] "MarketingListID"
PX.Objects.CR.CRCampaignToCRMarketingListLink.LastUpdateDate : Edm.DateTimeOffset "Last Updated On"
PX.Objects.CR.CRCampaignToCRMarketingListLink.CRCampaignByCampaignID -> PX.Objects.CR.CRCampaign (CampaignID=CampaignID)
PX.Objects.CR.CRCampaignToCRMarketingListLink.CRMarketingListByMarketingListID -> PX.Objects.CR.CRMarketingList (MarketingListID=MarketingListID)

# PX.Objects.CR.CRCampaignType (EntityType)

Label: "Campaign Class"
Key: TypeID
Entity sets: PX_Objects_CR_CRCampaignType, CampaignClass, CRCampaignType
Non-filterable, non-selectable: NoteText

PX.Objects.CR.CRCampaignType.TypeID : Edm.String [key] "Campaign Class ID"
PX.Objects.CR.CRCampaignType.Description : Edm.String "Description"
PX.Objects.CR.CRCampaignType.NoteID : Edm.Guid "NoteID"
PX.Objects.CR.CRCampaignType.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRCampaignType.CreatedByScreenID : Edm.String
PX.Objects.CR.CRCampaignType.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRCampaignType.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCampaignType.tstamp : Edm.Binary
PX.Objects.CR.CRCampaignType.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRCampaignType.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRCampaignType.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCampaignType.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRCampaignType.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRCampaignType.CRCampaignCollection -> Collection(PX.Objects.CR.CRCampaign)

# PX.Objects.CR.CRCase (EntityType)

Label: "Case"
Key: CaseCD
Entity sets: PX_Objects_CR_CRCase, Case, CRCase
Non-filterable, non-selectable: DescriptionAsPlainText, SLAETA, LastActivity, LastModified, TimeSpentInt, OvertimeSpentInt, TimeBillableInt, OvertimeBillableInt, TimeResolutionMinutes, Age, NoteText, EntityTypeID, DeletedDatabaseRecord

PX.Objects.CR.CRCase.CaseCD : Edm.String [key] "Case ID"
PX.Objects.CR.CRCase.CreatedDateTime : Edm.DateTimeOffset "Date Reported"
PX.Objects.CR.CRCase.CaseClassID : Edm.String "Case Class"
PX.Objects.CR.CRCase.Subject : Edm.String "Subject"
PX.Objects.CR.CRCase.Description : Edm.String "Description"
PX.Objects.CR.CRCase.DescriptionAsPlainText : Edm.String "DescriptionAsPlainText"
PX.Objects.CR.CRCase.CustomerID : Edm.Int32 "Business Account"
PX.Objects.CR.CRCase.ContractID : Edm.Int32 "Contract"
PX.Objects.CR.CRCase.ContactID : Edm.Int32 "Contact"
PX.Objects.CR.CRCase.Status : Edm.String "Status"
PX.Objects.CR.CRCase.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CR.CRCase.Released : Edm.Boolean "Released"
PX.Objects.CR.CRCase.Resolution : Edm.String "Reason"
PX.Objects.CR.CRCase.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.CRCase.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.CRCase.AssignDate : Edm.DateTimeOffset "Assignment Date"
PX.Objects.CR.CRCase.Source : Edm.String "Source"
PX.Objects.CR.CRCase.Severity : Edm.String "Severity"
PX.Objects.CR.CRCase.Priority : Edm.String "Priority"
PX.Objects.CR.CRCase.ReportedOnDateTime : Edm.DateTimeOffset "Reported On"
PX.Objects.CR.CRCase.SLAETA : Edm.DateTimeOffset "SLA"
PX.Objects.CR.CRCase.TimeEstimated : Edm.Int32 "Estimation"
PX.Objects.CR.CRCase.ClosureNotes : Edm.String "Closure Notes"
PX.Objects.CR.CRCase.LastActivity : Edm.DateTimeOffset "Last Activity"
PX.Objects.CR.CRCase.LastModified : Edm.DateTimeOffset "Last Modified"
PX.Objects.CR.CRCase.InitResponse : Edm.Int32 "Init. Response"
PX.Objects.CR.CRCase.TimeSpent : Edm.Int32 "Time Spent"
PX.Objects.CR.CRCase.TimeSpentInt : Edm.Int32
PX.Objects.CR.CRCase.OvertimeSpent : Edm.Int32 "Overtime Spent"
PX.Objects.CR.CRCase.OvertimeSpentInt : Edm.Int32
PX.Objects.CR.CRCase.TimeBillableInt : Edm.Int32
PX.Objects.CR.CRCase.OvertimeBillableInt : Edm.Int32
PX.Objects.CR.CRCase.ResolutionDate : Edm.DateTimeOffset "Closed On"
PX.Objects.CR.CRCase.TimeResolution : Edm.Int32 "Resolution Time"
PX.Objects.CR.CRCase.TimeResolutionMinutes : Edm.Int32 "Resolution Time (Minutes)"
PX.Objects.CR.CRCase.ARRefNbr : Edm.String "AR Reference Nbr."
PX.Objects.CR.CRCase.Date : Edm.DateTimeOffset "Billing Date"
PX.Objects.CR.CRCase.Age : Edm.Int32 "Age"
PX.Objects.CR.CRCase.StatusDate : Edm.DateTimeOffset
PX.Objects.CR.CRCase.StatusRevision : Edm.Int32
PX.Objects.CR.CRCase.NoteID : Edm.Guid
PX.Objects.CR.CRCase.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRCase.tstamp : Edm.Binary
PX.Objects.CR.CRCase.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRCase.CreatedByScreenID : Edm.String
PX.Objects.CR.CRCase.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRCase.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRCase.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.CRCase.EntityTypeID : Edm.Int32
PX.Objects.CR.CRCase.DeletedDatabaseRecord : Edm.Boolean [required] "DeletedDatabaseRecord"
PX.Objects.CR.CRCase.ARInvoiceByARRefNbr -> PX.Objects.AR.ARInvoice (ARRefNbr=RefNbr)
PX.Objects.CR.CRCase.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CR.CRCase.ContractByLocationID -> PX.Objects.CT.Contract (ContractID=ContractID, CustomerID=CustomerID)
PX.Objects.CR.CRCase.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)
PX.Objects.CR.CRCase.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CR.CRCase.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.CRCase.CRActivityByNoteID -> PX.Objects.CR.CRActivity (NoteID=RefNoteID)
PX.Objects.CR.CRCase.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRCase.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRCase.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.CRCase.LocationByLocationID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.CR.CRCase.LocationByCustomerID -> PX.Objects.CR.Location (CustomerID=BAccountID)
PX.Objects.CR.CRCase.CRCaseClassByCaseClassID -> PX.Objects.CR.CRCaseClass (CaseClassID=CaseClassID)
PX.Objects.CR.CRCase.ARTranCollection -> Collection(PX.Objects.AR.ARTran)
PX.Objects.CR.CRCase.PMTranCollection -> Collection(PX.Objects.PM.PMTran)
PX.Objects.CR.CRCase.CRCaseReferenceCollection -> Collection(PX.Objects.CR.CRCaseReference)
PX.Objects.CR.CRCase.CRCaseCommitmentsCollection -> Collection(PX.Objects.CR.CRCaseCommitments)

# PX.Objects.CR.CRCaseClass (EntityType)

Label: "Case Class"
Key: CaseClassID
Entity sets: PX_Objects_CR_CRCaseClass, CaseClass, CRCaseClass
Non-filterable, non-selectable: NoteText

PX.Objects.CR.CRCaseClass.CaseClassID : Edm.String [key] "Case Class ID"
PX.Objects.CR.CRCaseClass.Description : Edm.String "Description"
PX.Objects.CR.CRCaseClass.CalendarID : Edm.String "Work Calendar"
PX.Objects.CR.CRCaseClass.IsBillable : Edm.Boolean [required] "Billable"
PX.Objects.CR.CRCaseClass.AllowOverrideBillable : Edm.Boolean [required] "Enable Billable Option Override"
PX.Objects.CR.CRCaseClass.RequireCustomer : Edm.Boolean [required] "Require Customer"
PX.Objects.CR.CRCaseClass.RequireContact : Edm.Boolean [required] "Require Contact"
PX.Objects.CR.CRCaseClass.RequireVendor : Edm.Boolean [required] "Require Vendor"
PX.Objects.CR.CRCaseClass.AllowEmployeeAsContact : Edm.Boolean [required] "Allow Selecting Employee as Case Contact"
PX.Objects.CR.CRCaseClass.RequireContract : Edm.Boolean [required] "Require Contract"
PX.Objects.CR.CRCaseClass.RequireClosureNotes : Edm.Boolean [required] "Require Case Closure Notes"
PX.Objects.CR.CRCaseClass.PerItemBilling : Edm.Int32 [required] "Billing Mode"
PX.Objects.CR.CRCaseClass.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.CR.CRCaseClass.OvertimeItemID : Edm.Int32 "Overtime Labor Item"
PX.Objects.CR.CRCaseClass.DefaultEMailAccountID : Edm.Int32 "Default Email Account"
PX.Objects.CR.CRCaseClass.TrackSolutionsInActivities : Edm.Boolean [required] "Track Solutions in Activities"
PX.Objects.CR.CRCaseClass.RoundingInMinutes : Edm.Int32 "Round Time By"
PX.Objects.CR.CRCaseClass.MinBillTimeInMinutes : Edm.Int32 "Min. Billable Time"
PX.Objects.CR.CRCaseClass.ReopenCaseTimeInDays : Edm.Int32 "Days Allowed to Reopen Case"
PX.Objects.CR.CRCaseClass.IsInternal : Edm.Boolean [required] "Internal"
PX.Objects.CR.CRCaseClass.IncludeSystemActivitiesResponseTimeCalculation : Edm.Boolean [required] "Include System Activities in Response Time Calculation"
PX.Objects.CR.CRCaseClass.NoteID : Edm.Guid
PX.Objects.CR.CRCaseClass.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRCaseClass.tstamp : Edm.Binary
PX.Objects.CR.CRCaseClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRCaseClass.CreatedByScreenID : Edm.String
PX.Objects.CR.CRCaseClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCaseClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRCaseClass.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRCaseClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCaseClass.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.CR.CRCaseClass.InventoryItemByOvertimeItemID -> PX.Objects.IN.InventoryItem (OvertimeItemID=InventoryID)
PX.Objects.CR.CRCaseClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRCaseClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRCaseClass.EMailAccountByDefaultEMailAccountID -> PX.SM.EMailAccount (DefaultEMailAccountID=EmailAccountID)
PX.Objects.CR.CRCaseClass.CSCalendarByCalendarID -> PX.Objects.CS.CSCalendar (CalendarID=CalendarID)
PX.Objects.CR.CRCaseClass.CRCaseCollection -> Collection(PX.Objects.CR.CRCase)
PX.Objects.CR.CRCaseClass.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.Objects.CR.CRCaseClass.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CR.CRCaseClass.EMailAccountCollection -> Collection(PX.SM.EMailAccount)
PX.Objects.CR.CRCaseClass.CRCaseClassLaborMatrixCollection -> Collection(PX.Objects.CR.CRCaseClassLaborMatrix)
PX.Objects.CR.CRCaseClass.CRClassSeverityTimeCollection -> Collection(PX.Objects.CR.CRClassSeverityTime)

# PX.Objects.CR.CRCaseClassLaborMatrix (EntityType)

Label: "Case Class Labor"
Key: CaseClassID, EarningType
Entity sets: PX_Objects_CR_CRCaseClassLaborMatrix, CaseClassLabor, CRCaseClassLaborMatrix

PX.Objects.CR.CRCaseClassLaborMatrix.CaseClassID : Edm.String [key]
PX.Objects.CR.CRCaseClassLaborMatrix.EarningType : Edm.String [key] "Earning Type"
PX.Objects.CR.CRCaseClassLaborMatrix.LabourItemID : Edm.Int32 "Labor Item"
PX.Objects.CR.CRCaseClassLaborMatrix.tstamp : Edm.Binary
PX.Objects.CR.CRCaseClassLaborMatrix.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRCaseClassLaborMatrix.CreatedByScreenID : Edm.String
PX.Objects.CR.CRCaseClassLaborMatrix.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCaseClassLaborMatrix.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRCaseClassLaborMatrix.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRCaseClassLaborMatrix.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCaseClassLaborMatrix.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.CR.CRCaseClassLaborMatrix.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRCaseClassLaborMatrix.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRCaseClassLaborMatrix.CRCaseClassByCaseClassID -> PX.Objects.CR.CRCaseClass (CaseClassID=CaseClassID)
PX.Objects.CR.CRCaseClassLaborMatrix.EPEarningTypeByEarningType -> PX.Objects.EP.EPEarningType (EarningType=TypeCD)

# PX.Objects.CR.CRCaseCommitments (EntityType)

Label: "Case Commitments"
Key: CaseCD
Entity sets: PX_Objects_CR_CRCaseCommitments, CaseCommitments, CRCaseCommitments
Non-filterable, non-selectable: HeaderInitialResponseDueDateTime, HeaderResolutionDueDateTime, HeaderResponseDueDateTime

PX.Objects.CR.CRCaseCommitments.CaseCD : Edm.String [key] "Case ID"
PX.Objects.CR.CRCaseCommitments.OriginalInitialResponseDueDateTime : Edm.DateTimeOffset "Initial Response Due"
PX.Objects.CR.CRCaseCommitments.InitialResponseDueDateTime : Edm.DateTimeOffset "Initial Response Due"
PX.Objects.CR.CRCaseCommitments.HeaderInitialResponseDueDateTime : Edm.DateTimeOffset "Initial Response Due"
PX.Objects.CR.CRCaseCommitments.OriginalResolutionDueDateTime : Edm.DateTimeOffset "Resolution Due"
PX.Objects.CR.CRCaseCommitments.ResolutionDueDateTime : Edm.DateTimeOffset "Resolution Due"
PX.Objects.CR.CRCaseCommitments.HeaderResolutionDueDateTime : Edm.DateTimeOffset "Resolution Due"
PX.Objects.CR.CRCaseCommitments.ResponseDueDateTime : Edm.DateTimeOffset "Response Due"
PX.Objects.CR.CRCaseCommitments.HeaderResponseDueDateTime : Edm.DateTimeOffset "Response Due"
PX.Objects.CR.CRCaseCommitments.CRCaseByCaseCD -> PX.Objects.CR.CRCase (CaseCD=CaseCD)

# PX.Objects.CR.CRCaseReference (EntityType)

Label: "Case Reference"
Key: ChildCaseCD, ParentCaseCD
Entity sets: PX_Objects_CR_CRCaseReference, CaseReference, CRCaseReference

PX.Objects.CR.CRCaseReference.ParentCaseCD : Edm.String [key] "ParentCaseCD"
PX.Objects.CR.CRCaseReference.ChildCaseCD : Edm.String [key] "Case ID"
PX.Objects.CR.CRCaseReference.RelationType : Edm.String "Relation Type"
PX.Objects.CR.CRCaseReference.tstamp : Edm.Binary
PX.Objects.CR.CRCaseReference.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRCaseReference.CreatedByScreenID : Edm.String
PX.Objects.CR.CRCaseReference.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCaseReference.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRCaseReference.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRCaseReference.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCaseReference.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRCaseReference.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRCaseReference.CRCaseByChildCaseCD -> PX.Objects.CR.CRCase (ChildCaseCD=CaseCD)

# PX.Objects.CR.CRClassSeverityTime (EntityType)

Label: "Time Reaction By Severity"
Key: CaseClassID, Severity
Entity sets: PX_Objects_CR_CRClassSeverityTime, TimeReactionBySeverity, CRClassSeverityTime

PX.Objects.CR.CRClassSeverityTime.CaseClassID : Edm.String [key] "Case Class"
PX.Objects.CR.CRClassSeverityTime.Severity : Edm.String [key] "Severity"
PX.Objects.CR.CRClassSeverityTime.TrackInitialResponseTime : Edm.Boolean [required] "Enable"
PX.Objects.CR.CRClassSeverityTime.InitialResponseTimeTarget : Edm.Int32 [required] "Target Initial Response Time"
PX.Objects.CR.CRClassSeverityTime.InitialResponseGracePeriod : Edm.Int32 [required] "Initial Response Extension"
PX.Objects.CR.CRClassSeverityTime.TrackResponseTime : Edm.Boolean [required] "Enable"
PX.Objects.CR.CRClassSeverityTime.ResponseTimeTarget : Edm.Int32 [required] "Target Response Time"
PX.Objects.CR.CRClassSeverityTime.ResponseGracePeriod : Edm.Int32 [required] "Response Extension"
PX.Objects.CR.CRClassSeverityTime.TrackResolutionTime : Edm.Boolean [required] "Enable"
PX.Objects.CR.CRClassSeverityTime.ResolutionTimeTarget : Edm.Int32 [required] "Target Resolution Time"
PX.Objects.CR.CRClassSeverityTime.ResolutionGracePeriod : Edm.Int32 [required] "Resolution Extension"
PX.Objects.CR.CRClassSeverityTime.tstamp : Edm.Binary
PX.Objects.CR.CRClassSeverityTime.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRClassSeverityTime.CreatedByScreenID : Edm.String
PX.Objects.CR.CRClassSeverityTime.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRClassSeverityTime.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRClassSeverityTime.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRClassSeverityTime.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRClassSeverityTime.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRClassSeverityTime.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRClassSeverityTime.CRCaseClassByCaseClassID -> PX.Objects.CR.CRCaseClass (CaseClassID=CaseClassID)

# PX.Objects.CR.CRContact (EntityType)

Label: "Opportunity Contact"
Key: ContactID
Entity sets: PX_Objects_CR_CRContact, OpportunityContact, CRContact
Non-filterable, non-selectable: OverrideContact

PX.Objects.CR.CRContact.ContactID : Edm.Int32 [key] "Contact ID"
PX.Objects.CR.CRContact.FirstName : Edm.String "First Name"
PX.Objects.CR.CRContact.LastName : Edm.String "Last Name"
PX.Objects.CR.CRContact.MidName : Edm.String "Middle Name"
PX.Objects.CR.CRContact.DisplayName : Edm.String "Display Name"
PX.Objects.CR.CRContact.WebSite : Edm.String "Web"
PX.Objects.CR.CRContact.BAccountID : Edm.Int32
PX.Objects.CR.CRContact.BAccountContactID : Edm.Int32
PX.Objects.CR.CRContact.BAccountLocationID : Edm.Int32
PX.Objects.CR.CRContact.IsDefaultContact : Edm.Boolean
PX.Objects.CR.CRContact.OverrideContact : Edm.Boolean
PX.Objects.CR.CRContact.RevisionID : Edm.Int32
PX.Objects.CR.CRContact.Title : Edm.String "Title"
PX.Objects.CR.CRContact.Salutation : Edm.String "Job Title"
PX.Objects.CR.CRContact.Attention : Edm.String "Attention"
PX.Objects.CR.CRContact.FullName : Edm.String "Account Name"
PX.Objects.CR.CRContact.Email : Edm.String "Email"
PX.Objects.CR.CRContact.Fax : Edm.String "Fax"
PX.Objects.CR.CRContact.FaxType : Edm.String "Fax"
PX.Objects.CR.CRContact.Phone1 : Edm.String "Phone 1"
PX.Objects.CR.CRContact.Phone1Type : Edm.String "Phone 1"
PX.Objects.CR.CRContact.Phone2 : Edm.String "Phone 2"
PX.Objects.CR.CRContact.Phone2Type : Edm.String "Phone 2"
PX.Objects.CR.CRContact.Phone3 : Edm.String "Phone 3"
PX.Objects.CR.CRContact.Phone3Type : Edm.String "Phone 3"
PX.Objects.CR.CRContact.NoteID : Edm.Guid
PX.Objects.CR.CRContact.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRContact.CreatedByScreenID : Edm.String
PX.Objects.CR.CRContact.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.CRContact.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRContact.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRContact.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.CRContact.tstamp : Edm.Binary
PX.Objects.CR.CRContact.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CR.CRContact.ContactByBAccountContactID -> PX.Objects.CR.Contact (BAccountContactID=ContactID)
PX.Objects.CR.CRContact.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRContact.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRContact.LocationByBAccountLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID, BAccountLocationID=LocationID)
PX.Objects.CR.CRContact.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.CRContact.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)

# PX.Objects.CR.CRContactClass (EntityType)

Label: "Contact Class"
Key: ClassID
Entity sets: PX_Objects_CR_CRContactClass, ContactClass, CRContactClass
Non-filterable, non-selectable: NoteText

PX.Objects.CR.CRContactClass.ClassID : Edm.String [key] "Contact Class ID"
PX.Objects.CR.CRContactClass.IsInternal : Edm.Boolean [required] "Internal"
PX.Objects.CR.CRContactClass.Description : Edm.String "Description"
PX.Objects.CR.CRContactClass.DefaultOwner : Edm.String "Default Owner"
PX.Objects.CR.CRContactClass.DefaultAssignmentMapID : Edm.Int32 "Assignment Map"
PX.Objects.CR.CRContactClass.TargetLeadClassID : Edm.String "Lead Class"
PX.Objects.CR.CRContactClass.TargetBAccountClassID : Edm.String "Business Account Class"
PX.Objects.CR.CRContactClass.TargetOpportunityClassID : Edm.String "Opportunity Class"
PX.Objects.CR.CRContactClass.TargetOpportunityStage : Edm.String "Opportunity Stage"
PX.Objects.CR.CRContactClass.DefaultEMailAccountID : Edm.Int32 "Default Email Account"
PX.Objects.CR.CRContactClass.NoteID : Edm.Guid "NoteID"
PX.Objects.CR.CRContactClass.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRContactClass.tstamp : Edm.Binary
PX.Objects.CR.CRContactClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRContactClass.CreatedByScreenID : Edm.String
PX.Objects.CR.CRContactClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRContactClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRContactClass.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRContactClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRContactClass.CRCustomerClassByTargetBAccountClassID -> PX.Objects.CR.CRCustomerClass (TargetBAccountClassID=CRCustomerClassID)
PX.Objects.CR.CRContactClass.CRLeadClassByTargetLeadClassID -> PX.Objects.CR.CRLeadClass (TargetLeadClassID=ClassID)
PX.Objects.CR.CRContactClass.CROpportunityClassByTargetOpportunityClassID -> PX.Objects.CR.CROpportunityClass (TargetOpportunityClassID=CROpportunityClassID)
PX.Objects.CR.CRContactClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRContactClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRContactClass.EMailAccountByDefaultEMailAccountID -> PX.SM.EMailAccount (DefaultEMailAccountID=EmailAccountID)
PX.Objects.CR.CRContactClass.EPAssignmentMapByDefaultAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultAssignmentMapID=AssignmentMapID)
PX.Objects.CR.CRContactClass.ContactCollection -> Collection(PX.Objects.CR.Contact)
PX.Objects.CR.CRContactClass.CRLeadClassCollection -> Collection(PX.Objects.CR.CRLeadClass)
PX.Objects.CR.CRContactClass.CROpportunityClassCollection -> Collection(PX.Objects.CR.CROpportunityClass)
PX.Objects.CR.CRContactClass.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.Objects.CR.CRContactClass.SPPortalCollection -> Collection(PX.Objects.Portals.SPPortal)
PX.Objects.CR.CRContactClass.EMailSyncPolicyCollection -> Collection(PX.SM.EMailSyncPolicy)

# PX.Objects.CR.CRCustomerClass (EntityType)

Label: "Business Account Class"
Key: CRCustomerClassID
Entity sets: PX_Objects_CR_CRCustomerClass, BusinessAccountClass, CRCustomerClass
Non-filterable, non-selectable: NoteText

PX.Objects.CR.CRCustomerClass.CRCustomerClassID : Edm.String [key] "Business Account Class ID"
PX.Objects.CR.CRCustomerClass.Description : Edm.String "Description"
PX.Objects.CR.CRCustomerClass.DefaultOwner : Edm.String "Default Owner"
PX.Objects.CR.CRCustomerClass.DefaultAssignmentMapID : Edm.Int32 "Assignment Map"
PX.Objects.CR.CRCustomerClass.DefaultEMailAccountID : Edm.Int32 "Default Email Account"
PX.Objects.CR.CRCustomerClass.IsInternal : Edm.Boolean [required] "Internal"
PX.Objects.CR.CRCustomerClass.CuryID : Edm.String "Currency ID"
PX.Objects.CR.CRCustomerClass.AllowOverrideCury : Edm.Boolean [required] "Enable Currency Override"
PX.Objects.CR.CRCustomerClass.NoteID : Edm.Guid
PX.Objects.CR.CRCustomerClass.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRCustomerClass.tstamp : Edm.Binary
PX.Objects.CR.CRCustomerClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRCustomerClass.CreatedByScreenID : Edm.String
PX.Objects.CR.CRCustomerClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCustomerClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRCustomerClass.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRCustomerClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRCustomerClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRCustomerClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRCustomerClass.EMailAccountByDefaultEMailAccountID -> PX.SM.EMailAccount (DefaultEMailAccountID=EmailAccountID)
PX.Objects.CR.CRCustomerClass.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CR.CRCustomerClass.EPAssignmentMapByDefaultAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultAssignmentMapID=AssignmentMapID)
PX.Objects.CR.CRCustomerClass.BAccountCollection -> Collection(PX.Objects.CR.BAccount)
PX.Objects.CR.CRCustomerClass.CRContactClassCollection -> Collection(PX.Objects.CR.CRContactClass)
PX.Objects.CR.CRCustomerClass.CRLeadClassCollection -> Collection(PX.Objects.CR.CRLeadClass)
PX.Objects.CR.CRCustomerClass.CROpportunityClassCollection -> Collection(PX.Objects.CR.CROpportunityClass)
PX.Objects.CR.CRCustomerClass.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)

# PX.Objects.CR.CREmployee (EntityType)

Label: "Employee"
BaseType: PX.Objects.CR.BAccount
Key: AcctCD (inherited from PX.Objects.CR.BAccount)
Entity sets: PX_Objects_CR_CREmployee, Employee, CREmployee

PX.Objects.CR.CREmployee.DepartmentID : Edm.String "Department"
PX.Objects.CR.CREmployee.SupervisorID : Edm.Int32 "Reports to"
PX.Objects.CR.CREmployee.UserID : Edm.Guid "Employee Login"

# PX.Objects.CR.CRLead (EntityType)

Label: "Lead"
BaseType: PX.Objects.CR.Contact
Key: ContactID (inherited from PX.Objects.CR.Contact)
Entity sets: PX_Objects_CR_CRLead, Lead, CRLead

PX.Objects.CR.CRLead.RefContactID : Edm.Int32 "Contact"
PX.Objects.CR.CRLead.OverrideRefContact : Edm.Boolean [required] "Override"
PX.Objects.CR.CRLead.Description : Edm.String "Description"
PX.Objects.CR.CRLead.QualificationDate : Edm.DateTimeOffset "Qualification Date"
PX.Objects.CR.CRLead.ConvertedBy : Edm.Guid "Converted By"
PX.Objects.CR.CRLead.LeadContactID : Edm.Int32 "LeadContactID"
PX.Objects.CR.CRLead.LeadNoteID : Edm.Guid "LeadNoteID"
PX.Objects.CR.CRLead.LeadCreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRLead.LeadCreatedByScreenID : Edm.String
PX.Objects.CR.CRLead.LeadCreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRLead.LeadLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRLead.LeadLastModifiedByScreenID : Edm.String
PX.Objects.CR.CRLead.LeadLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRLead.ContactByRefContactID -> PX.Objects.CR.Contact (RefContactID=ContactID)
PX.Objects.CR.CRLead.ContactByDisplayName -> PX.Objects.CR.Contact (DisplayName=DisplayName)
PX.Objects.CR.CRLead.CRLeadClassByClassID -> PX.Objects.CR.CRLeadClass (ClassID=ClassID)
PX.Objects.CR.CRLead.UsersByConvertedBy -> PX.SM.Users (ConvertedBy=PKID)

# PX.Objects.CR.CRLeadClass (EntityType)

Label: "Lead Class"
Key: ClassID
Entity sets: PX_Objects_CR_CRLeadClass, LeadClass, CRLeadClass
Non-filterable, non-selectable: NoteText

PX.Objects.CR.CRLeadClass.ClassID : Edm.String [key] "Lead Class ID"
PX.Objects.CR.CRLeadClass.IsInternal : Edm.Boolean [required] "Internal"
PX.Objects.CR.CRLeadClass.Description : Edm.String "Description"
PX.Objects.CR.CRLeadClass.DefaultSource : Edm.String "Default Source"
PX.Objects.CR.CRLeadClass.DefaultOwner : Edm.String "Default Owner"
PX.Objects.CR.CRLeadClass.DefaultAssignmentMapID : Edm.Int32 "Assignment Map"
PX.Objects.CR.CRLeadClass.TargetContactClassID : Edm.String "Contact Class"
PX.Objects.CR.CRLeadClass.TargetBAccountClassID : Edm.String "Business Account Class"
PX.Objects.CR.CRLeadClass.RequireBAccountCreation : Edm.Boolean [required] "Require Account for Conversion to Opportunity"
PX.Objects.CR.CRLeadClass.TargetOpportunityClassID : Edm.String "Opportunity Class"
PX.Objects.CR.CRLeadClass.TargetOpportunityStage : Edm.String "Opportunity Stage"
PX.Objects.CR.CRLeadClass.DefaultEMailAccountID : Edm.Int32 "Default Email Account"
PX.Objects.CR.CRLeadClass.NoteID : Edm.Guid "NoteID"
PX.Objects.CR.CRLeadClass.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRLeadClass.tstamp : Edm.Binary
PX.Objects.CR.CRLeadClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRLeadClass.CreatedByScreenID : Edm.String
PX.Objects.CR.CRLeadClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRLeadClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRLeadClass.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRLeadClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRLeadClass.CRContactClassByTargetContactClassID -> PX.Objects.CR.CRContactClass (TargetContactClassID=ClassID)
PX.Objects.CR.CRLeadClass.CRCustomerClassByTargetBAccountClassID -> PX.Objects.CR.CRCustomerClass (TargetBAccountClassID=CRCustomerClassID)
PX.Objects.CR.CRLeadClass.CROpportunityClassByTargetOpportunityClassID -> PX.Objects.CR.CROpportunityClass (TargetOpportunityClassID=CROpportunityClassID)
PX.Objects.CR.CRLeadClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRLeadClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRLeadClass.EMailAccountByDefaultEMailAccountID -> PX.SM.EMailAccount (DefaultEMailAccountID=EmailAccountID)
PX.Objects.CR.CRLeadClass.EPAssignmentMapByDefaultAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultAssignmentMapID=AssignmentMapID)
PX.Objects.CR.CRLeadClass.CRContactClassCollection -> Collection(PX.Objects.CR.CRContactClass)
PX.Objects.CR.CRLeadClass.CRLeadCollection -> Collection(PX.Objects.CR.CRLead)
PX.Objects.CR.CRLeadClass.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.Objects.CR.CRLeadClass.EMailAccountCollection -> Collection(PX.SM.EMailAccount)

# PX.Objects.CR.CRLeadStatistics (EntityType)

Label: "Lead Statistics"
Key: ContactID
Entity sets: PX_Objects_CR_CRLeadStatistics, LeadStatistics, CRLeadStatistics

PX.Objects.CR.CRLeadStatistics.ContactID : Edm.Int32 [key] "Lead ID"
PX.Objects.CR.CRLeadStatistics.LeadQualificationTime : Edm.Int32 "Lead Qualification Time"
PX.Objects.CR.CRLeadStatistics.LeadResponseTime : Edm.Int32 "Lead Response Time"
PX.Objects.CR.CRLeadStatistics.ContactByRefContactID -> PX.Objects.CR.Contact
PX.Objects.CR.CRLeadStatistics.ContactByDisplayName -> PX.Objects.CR.Contact

# PX.Objects.CR.CRMarketingCategory (EntityType)

Label: "Marketing Category"
Key: MarketingCategoryID
Entity sets: PX_Objects_CR_CRMarketingCategory, MarketingCategory, CRMarketingCategory

PX.Objects.CR.CRMarketingCategory.MarketingCategoryID : Edm.String [key] "Marketing Category"
PX.Objects.CR.CRMarketingCategory.Description : Edm.String "Description"
PX.Objects.CR.CRMarketingCategory.IsEnabled : Edm.Boolean [required] "Active"
PX.Objects.CR.CRMarketingCategory.Channel : Edm.String "Channel"
PX.Objects.CR.CRMarketingCategory.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRMarketingCategory.CreatedByScreenID : Edm.String
PX.Objects.CR.CRMarketingCategory.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.CRMarketingCategory.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRMarketingCategory.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRMarketingCategory.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.CRMarketingCategory.tstamp : Edm.Binary
PX.Objects.CR.CRMarketingCategory.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRMarketingCategory.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRMarketingCategory.CRPMTimeActivityCollection -> Collection(PX.Objects.CR.CRPMTimeActivity)
PX.Objects.CR.CRMarketingCategory.CRSMEmailCollection -> Collection(PX.Objects.CR.CRSMEmail)
PX.Objects.CR.CRMarketingCategory.CRActivityCollection -> Collection(PX.Objects.CR.CRActivity)
PX.Objects.CR.CRMarketingCategory.CRMassMailCollection -> Collection(PX.Objects.CR.CRMassMail)
PX.Objects.CR.CRMarketingCategory.CRUnsubscribedPreferencesCollection -> Collection(PX.Objects.CR.CRUnsubscribedPreferences)
PX.Objects.CR.CRMarketingCategory.SMSendGridSuppressionGroupCollection -> Collection(PX.DataSync.SendGrid.SMSendGridSuppressionGroup)

# PX.Objects.CR.CRMarketingList (EntityType)

Label: "Marketing List"
Key: MailListCode
Entity sets: PX_Objects_CR_CRMarketingList, MarketingList, CRMarketingList
Non-filterable, non-selectable: NoteText, HSEntityTypeID

PX.Objects.CR.CRMarketingList.MarketingListID : Edm.Int32 "MarketingListID"
PX.Objects.CR.CRMarketingList.MailListCode : Edm.String [key] "Marketing List ID"
PX.Objects.CR.CRMarketingList.Name : Edm.String "List Name"
PX.Objects.CR.CRMarketingList.Description : Edm.String "Description"
PX.Objects.CR.CRMarketingList.Status : Edm.String "Status"
PX.Objects.CR.CRMarketingList.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.CRMarketingList.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.CRMarketingList.Method : Edm.String "Contact Method"
PX.Objects.CR.CRMarketingList.Type : Edm.String "List Type"
PX.Objects.CR.CRMarketingList.GIDesignID : Edm.Guid "Generic Inquiry"
PX.Objects.CR.CRMarketingList.SharedGIFilter : Edm.Guid "Shared Filter"
PX.Objects.CR.CRMarketingList.NoteID : Edm.Guid
PX.Objects.CR.CRMarketingList.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRMarketingList.CreatedByScreenID : Edm.String
PX.Objects.CR.CRMarketingList.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRMarketingList.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.CRMarketingList.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRMarketingList.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRMarketingList.LastModifiedDateTime : Edm.DateTimeOffset "Modified Date"
PX.Objects.CR.CRMarketingList.tstamp : Edm.Binary
PX.Objects.CR.CRMarketingList.HSEntityTypeID : Edm.Int32
PX.Objects.CR.CRMarketingList.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.CRMarketingList.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRMarketingList.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRMarketingList.GIDesignByGIDesignID -> PX.Data.Maintenance.GI.GIDesign (GIDesignID=DesignID)
PX.Objects.CR.CRMarketingList.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.CRMarketingList.CRMarketingListByMarketingListID -> PX.Objects.CR.CRMarketingList (MarketingListID=MailListCode)
PX.Objects.CR.CRMarketingList.CRMarketingListCollection -> Collection(PX.Objects.CR.CRMarketingList)
PX.Objects.CR.CRMarketingList.CRCampaignMembersCollection -> Collection(PX.Objects.CR.CRCampaignMembers)
PX.Objects.CR.CRMarketingList.CRMarketingListMemberCollection -> Collection(PX.Objects.CR.CRMarketingListMember)
PX.Objects.CR.CRMarketingList.CRCampaignToCRMarketingListLinkCollection -> Collection(PX.Objects.CR.CRCampaignToCRMarketingListLink)

# PX.Objects.CR.CRMarketingListAlias (EntityType)

Label: "Marketing List"
BaseType: PX.Objects.CR.CRMarketingList
Key: MailListCode (inherited from PX.Objects.CR.CRMarketingList)
Entity sets: PX_Objects_CR_CRMarketingListAlias, MarketingList1, CRMarketingListAlias

# PX.Objects.CR.CRMarketingListMember (EntityType)

Label: "Marketing List Member"
Key: ContactID, MarketingListID
Entity sets: PX_Objects_CR_CRMarketingListMember, MarketingListMember, CRMarketingListMember
Non-filterable, non-selectable: IsVirtual, Type

PX.Objects.CR.CRMarketingListMember.ContactID : Edm.Int32 [key] "Member Name"
PX.Objects.CR.CRMarketingListMember.MarketingListID : Edm.Int32 [key] "Marketing List ID"
PX.Objects.CR.CRMarketingListMember.IsSubscribed : Edm.Boolean [required] "Subscribed"
PX.Objects.CR.CRMarketingListMember.IsVirtual : Edm.Boolean "Virtual"
PX.Objects.CR.CRMarketingListMember.Type : Edm.String "List Type"
PX.Objects.CR.CRMarketingListMember.Format : Edm.String "Format"
PX.Objects.CR.CRMarketingListMember.CreatedByScreenID : Edm.String
PX.Objects.CR.CRMarketingListMember.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRMarketingListMember.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRMarketingListMember.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRMarketingListMember.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRMarketingListMember.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRMarketingListMember.tstamp : Edm.Binary
PX.Objects.CR.CRMarketingListMember.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CR.CRMarketingListMember.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRMarketingListMember.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRMarketingListMember.CRMarketingListByMarketingListID -> PX.Objects.CR.CRMarketingList (MarketingListID=MarketingListID)

# PX.Objects.CR.CRMassMail (EntityType)

Label: "Mass Emails"
Key: MassMailCD
Entity sets: PX_Objects_CR_CRMassMail, MassEmails, CRMassMail
Non-filterable, non-selectable: SourceType, NoteText

PX.Objects.CR.CRMassMail.MassMailID : Edm.Int32
PX.Objects.CR.CRMassMail.MassMailCD : Edm.String [key] "Mass Mail ID"
PX.Objects.CR.CRMassMail.Status : Edm.String "Status"
PX.Objects.CR.CRMassMail.Source : Edm.Int32 [required] "Source"
PX.Objects.CR.CRMassMail.SourceType : Edm.String "Source Type"
PX.Objects.CR.CRMassMail.PlannedDate : Edm.DateTimeOffset "Planned"
PX.Objects.CR.CRMassMail.SentDateTime : Edm.DateTimeOffset "Sent"
PX.Objects.CR.CRMassMail.MailSubject : Edm.String "Subject"
PX.Objects.CR.CRMassMail.MailAccountID : Edm.Int32 "From"
PX.Objects.CR.CRMassMail.MailTo : Edm.String "To"
PX.Objects.CR.CRMassMail.MailCc : Edm.String "CC"
PX.Objects.CR.CRMassMail.MailBcc : Edm.String "BCC"
PX.Objects.CR.CRMassMail.MailContent : Edm.String "Content"
PX.Objects.CR.CRMassMail.MarketingCategoryID : Edm.String "Marketing Category"
PX.Objects.CR.CRMassMail.NoteID : Edm.Guid
PX.Objects.CR.CRMassMail.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRMassMail.tstamp : Edm.Binary
PX.Objects.CR.CRMassMail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRMassMail.CreatedByScreenID : Edm.String
PX.Objects.CR.CRMassMail.CreatedDateTime : Edm.DateTimeOffset "Created On"
PX.Objects.CR.CRMassMail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRMassMail.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRMassMail.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.CRMassMail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRMassMail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRMassMail.EMailAccountByMailAccountID -> PX.SM.EMailAccount (MailAccountID=EmailAccountID)
PX.Objects.CR.CRMassMail.CRMarketingCategoryByMarketingCategoryID -> PX.Objects.CR.CRMarketingCategory (MarketingCategoryID=MarketingCategoryID)
PX.Objects.CR.CRMassMail.CRMassMailMarketingListCollection -> Collection(PX.Objects.CR.CRMassMailMarketingList)
PX.Objects.CR.CRMassMail.CRMassMailMemberCollection -> Collection(PX.Objects.CR.CRMassMailMember)
PX.Objects.CR.CRMassMail.CRMassMailCampaignCollection -> Collection(PX.Objects.CR.CRMassMailCampaign)
PX.Objects.CR.CRMassMail.CRMassMailMessageCollection -> Collection(PX.Objects.CR.CRMassMailMessage)

# PX.Objects.CR.CRMassMailCampaign (EntityType)

Label: "Mass Mail Campaign Member"
Key: CampaignID, MassMailID
Entity sets: PX_Objects_CR_CRMassMailCampaign, MassMailCampaignMember, CRMassMailCampaign

PX.Objects.CR.CRMassMailCampaign.MassMailID : Edm.Int32 [key]
PX.Objects.CR.CRMassMailCampaign.CampaignID : Edm.String [key]
PX.Objects.CR.CRMassMailCampaign.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRMassMailCampaign.CreatedByScreenID : Edm.String
PX.Objects.CR.CRMassMailCampaign.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRMassMailCampaign.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRMassMailCampaign.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRMassMailCampaign.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRMassMailCampaign.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRMassMailCampaign.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRMassMailCampaign.CRMassMailByMassMailID -> PX.Objects.CR.CRMassMail (MassMailID=MassMailID)

# PX.Objects.CR.CRMassMailMarketingList (EntityType)

Label: "Mass Mail Marketing List Member"
Key: MailListID, MassMailID
Entity sets: PX_Objects_CR_CRMassMailMarketingList, MassMailMarketingListMember, CRMassMailMarketingList

PX.Objects.CR.CRMassMailMarketingList.MassMailID : Edm.Int32 [key]
PX.Objects.CR.CRMassMailMarketingList.MailListID : Edm.Int32 [key]
PX.Objects.CR.CRMassMailMarketingList.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRMassMailMarketingList.CreatedByScreenID : Edm.String
PX.Objects.CR.CRMassMailMarketingList.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRMassMailMarketingList.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRMassMailMarketingList.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRMassMailMarketingList.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRMassMailMarketingList.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRMassMailMarketingList.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRMassMailMarketingList.CRMassMailByMassMailID -> PX.Objects.CR.CRMassMail (MassMailID=MassMailID)

# PX.Objects.CR.CRMassMailMember (EntityType)

Label: "Mass Mail Members"
Key: ContactID, MassMailID
Entity sets: PX_Objects_CR_CRMassMailMember, MassMailMembers, CRMassMailMember

PX.Objects.CR.CRMassMailMember.MassMailID : Edm.Int32 [key]
PX.Objects.CR.CRMassMailMember.ContactID : Edm.Int32 [key]
PX.Objects.CR.CRMassMailMember.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRMassMailMember.CreatedByScreenID : Edm.String
PX.Objects.CR.CRMassMailMember.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRMassMailMember.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRMassMailMember.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRMassMailMember.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRMassMailMember.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CR.CRMassMailMember.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRMassMailMember.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRMassMailMember.CRMassMailByMassMailID -> PX.Objects.CR.CRMassMail (MassMailID=MassMailID)

# PX.Objects.CR.CRMassMailMessage (EntityType)

Label: "Mass Mail Message"
Key: MassMailID, MessageID
Entity sets: PX_Objects_CR_CRMassMailMessage, MassMailMessage, CRMassMailMessage

PX.Objects.CR.CRMassMailMessage.MassMailID : Edm.Int32 [key]
PX.Objects.CR.CRMassMailMessage.MessageID : Edm.Guid [key]
PX.Objects.CR.CRMassMailMessage.CRMassMailByMassMailID -> PX.Objects.CR.CRMassMail (MassMailID=MassMailID)

# PX.Objects.CR.CROpportunity (EntityType)

Label: "Opportunity"
Key: OpportunityID
Entity sets: PX_Objects_CR_CROpportunity, Opportunity, CROpportunity
Non-filterable, non-selectable: AllowOverrideBillingContactAddress, CuryWgtAmount, NoteText, PrimaryQuoteNbr, SuggestRelatedItems, CuryRate, EntityTypeID

PX.Objects.CR.CROpportunity.OpportunityID : Edm.String [key] "Opportunity ID"
PX.Objects.CR.CROpportunity.OpportunityAddressID : Edm.Int32
PX.Objects.CR.CROpportunity.OpportunityContactID : Edm.Int32
PX.Objects.CR.CROpportunity.TermsID : Edm.String "Credit Terms"
PX.Objects.CR.CROpportunity.AllowOverrideContactAddress : Edm.Boolean "Override"
PX.Objects.CR.CROpportunity.BAccountID : Edm.Int32 "Business Account"
PX.Objects.CR.CROpportunity.ContactID : Edm.Int32 "Contact"
PX.Objects.CR.CROpportunity.LeadID : Edm.Guid "Source Lead"
PX.Objects.CR.CROpportunity.ClassID : Edm.String "Opportunity Class"
PX.Objects.CR.CROpportunity.Subject : Edm.String "Description"
PX.Objects.CR.CROpportunity.Details : Edm.String "Details"
PX.Objects.CR.CROpportunity.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.CR.CROpportunity.ShipContactID : Edm.Int32
PX.Objects.CR.CROpportunity.ShipAddressID : Edm.Int32
PX.Objects.CR.CROpportunity.BillContactID : Edm.Int32
PX.Objects.CR.CROpportunity.BillAddressID : Edm.Int32
PX.Objects.CR.CROpportunity.AllowOverrideShippingContactAddress : Edm.Boolean "Override Shipping Info"
PX.Objects.CR.CROpportunity.AllowOverrideBillingContactAddress : Edm.Boolean
PX.Objects.CR.CROpportunity.DocumentDate : Edm.DateTimeOffset "Document Date"
PX.Objects.CR.CROpportunity.CloseDate : Edm.DateTimeOffset "Estimated Close Date"
PX.Objects.CR.CROpportunity.StageID : Edm.String "Stage"
PX.Objects.CR.CROpportunity.StageChangedDate : Edm.DateTimeOffset "Stage Change Date"
PX.Objects.CR.CROpportunity.CampaignSourceID : Edm.String "Source Campaign"
PX.Objects.CR.CROpportunity.Status : Edm.String "Status"
PX.Objects.CR.CROpportunity.IsActive : Edm.Boolean [required] "Active"
PX.Objects.CR.CROpportunity.Resolution : Edm.String "Reason"
PX.Objects.CR.CROpportunity.AssignDate : Edm.DateTimeOffset "Assignment Date"
PX.Objects.CR.CROpportunity.ClosingDate : Edm.DateTimeOffset "Actual Close Date"
PX.Objects.CR.CROpportunity.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.CROpportunity.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.CROpportunity.CuryID : Edm.String "Currency"
PX.Objects.CR.CROpportunity.CuryInfoID : Edm.Int64
PX.Objects.CR.CROpportunity.ExtPriceTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.CuryExtPriceTotal : Edm.Decimal "Detail Total"
PX.Objects.CR.CROpportunity.LineTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.CuryLineTotal : Edm.Decimal "Detail Total"
PX.Objects.CR.CROpportunity.LineDiscountTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.CuryLineDiscountTotal : Edm.Decimal "Line Discounts"
PX.Objects.CR.CROpportunity.LineDocDiscountTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.CuryLineDocDiscountTotal : Edm.Decimal "CuryLineDocDiscountTotal"
PX.Objects.CR.CROpportunity.IsTaxValid : Edm.Boolean "Tax Is Up to Date"
PX.Objects.CR.CROpportunity.TaxTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.CR.CROpportunity.ManualTotalEntry : Edm.Boolean "Manual Amount"
PX.Objects.CR.CROpportunity.Amount : Edm.Decimal
PX.Objects.CR.CROpportunity.DiscTot : Edm.Decimal
PX.Objects.CR.CROpportunity.CuryAmount : Edm.Decimal "Detail Total"
PX.Objects.CR.CROpportunity.CuryDiscTot : Edm.Decimal "Document Discounts"
PX.Objects.CR.CROpportunity.RawAmount : Edm.Decimal
PX.Objects.CR.CROpportunity.CuryRawAmount : Edm.Decimal
PX.Objects.CR.CROpportunity.ProductsAmount : Edm.Decimal "Products Amount"
PX.Objects.CR.CROpportunity.CuryProductsAmount : Edm.Decimal "Total"
PX.Objects.CR.CROpportunity.CuryOrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.CR.CROpportunity.OrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.CR.CROpportunity.CuryWgtAmount : Edm.Decimal "Weight Total"
PX.Objects.CR.CROpportunity.CuryVatExemptTotal : Edm.Decimal "VAT Exempt Total"
PX.Objects.CR.CROpportunity.VatExemptTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.CuryVatTaxableTotal : Edm.Decimal "VAT Taxable Total"
PX.Objects.CR.CROpportunity.VatTaxableTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.CR.CROpportunity.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.CROpportunity.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.CR.CROpportunity.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.CR.CROpportunity.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.CR.CROpportunity.NoteID : Edm.Guid
PX.Objects.CR.CROpportunity.NoteText : Edm.String "Note Text"
PX.Objects.CR.CROpportunity.QuoteNoteID : Edm.Guid
PX.Objects.CR.CROpportunity.QuoteOpportunityID : Edm.String
PX.Objects.CR.CROpportunity.PrimaryQuoteID : Edm.Guid
PX.Objects.CR.CROpportunity.PrimaryQuoteNbr : Edm.String "Primary Quote Nbr."
PX.Objects.CR.CROpportunity.PrimaryQuoteType : Edm.String "Primary Quote Type"
PX.Objects.CR.CROpportunity.Source : Edm.String "Source"
PX.Objects.CR.CROpportunity.ExternalRef : Edm.String "Ext. Ref. Nbr."
PX.Objects.CR.CROpportunity.tstamp : Edm.Binary
PX.Objects.CR.CROpportunity.CreatedByScreenID : Edm.String
PX.Objects.CR.CROpportunity.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CROpportunity.CreatedDateTime : Edm.DateTimeOffset "Date Created"
PX.Objects.CR.CROpportunity.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CROpportunity.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CROpportunity.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date"
PX.Objects.CR.CROpportunity.DefQuoteID : Edm.Guid
PX.Objects.CR.CROpportunity.ProductCntr : Edm.Int32
PX.Objects.CR.CROpportunity.LineCntr : Edm.Int32
PX.Objects.CR.CROpportunity.RCreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CROpportunity.RCreatedByScreenID : Edm.String
PX.Objects.CR.CROpportunity.RCreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunity.RLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CROpportunity.RLastModifiedByScreenID : Edm.String
PX.Objects.CR.CROpportunity.RLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunity.LanguageID : Edm.String "Language/Locale"
PX.Objects.CR.CROpportunity.SiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.CROpportunity.CarrierID : Edm.String "Ship Via"
PX.Objects.CR.CROpportunity.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.CROpportunity.ShipZoneID : Edm.String "Shipping Zone"
PX.Objects.CR.CROpportunity.FOBPointID : Edm.String "FOB Point"
PX.Objects.CR.CROpportunity.Resedential : Edm.Boolean "Residential Delivery"
PX.Objects.CR.CROpportunity.SaturdayDelivery : Edm.Boolean "Saturday Delivery"
PX.Objects.CR.CROpportunity.Insurance : Edm.Boolean "Insurance"
PX.Objects.CR.CROpportunity.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.CR.CROpportunity.CuryMarginAmt : Edm.Decimal "Est. Margin Amount"
PX.Objects.CR.CROpportunity.MarginAmt : Edm.Decimal
PX.Objects.CR.CROpportunity.MarginPct : Edm.Decimal "Est. Margin (%)"
PX.Objects.CR.CROpportunity.CuryNetSalesTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.NetSalesTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.CurySalesCostTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.SalesCostTotal : Edm.Decimal
PX.Objects.CR.CROpportunity.SuggestRelatedItems : Edm.Boolean
PX.Objects.CR.CROpportunity.CuryRate : Edm.Decimal
PX.Objects.CR.CROpportunity.EntityTypeID : Edm.Int32
PX.Objects.CR.CROpportunity.CloseDateYear : Edm.Int32 "Year of Estimated Close Date"
PX.Objects.CR.CROpportunity.CloseDateQuarter : Edm.Int32 "Quarter of Estimated Close Date"
PX.Objects.CR.CROpportunity.CloseDateMonth : Edm.Int32 "Month of Estimated Close Date"
PX.Objects.CR.CROpportunity.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CR.CROpportunity.BAccountByParentBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID)
PX.Objects.CR.CROpportunity.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CR.CROpportunity.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.CROpportunity.ContactByLeadID -> PX.Objects.CR.Contact (LeadID=NoteID)
PX.Objects.CR.CROpportunity.CROpportunityClassByClassID -> PX.Objects.CR.CROpportunityClass (ClassID=CROpportunityClassID)
PX.Objects.CR.CROpportunity.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CR.CROpportunity.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CROpportunity.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CROpportunity.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.CROpportunity.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.CR.CROpportunity.CarrierByCarrierID -> PX.Objects.CS.Carrier (CarrierID=CarrierID)
PX.Objects.CR.CROpportunity.FOBPointByFOBPointID -> PX.Objects.CS.FOBPoint (FOBPointID=FOBPointID)
PX.Objects.CR.CROpportunity.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CR.CROpportunity.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.CR.CROpportunity.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.CR.CROpportunity.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.CR.CROpportunity.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.CR.CROpportunity.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CR.CROpportunity.LocationByLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.CR.CROpportunity.CRAddressByOpportunityAddressID -> PX.Objects.CR.CRAddress (OpportunityAddressID=AddressID)
PX.Objects.CR.CROpportunity.CRAddressByShipAddressID -> PX.Objects.CR.CRAddress (ShipAddressID=AddressID)
PX.Objects.CR.CROpportunity.CRAddressByBillAddressID -> PX.Objects.CR.CRAddress (BillAddressID=AddressID)
PX.Objects.CR.CROpportunity.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign (CampaignSourceID=CampaignID)
PX.Objects.CR.CROpportunity.CRContactByOpportunityContactID -> PX.Objects.CR.CRContact (OpportunityContactID=ContactID)
PX.Objects.CR.CROpportunity.CRContactByShipContactID -> PX.Objects.CR.CRContact (ShipContactID=ContactID)
PX.Objects.CR.CROpportunity.CRContactByBillContactID -> PX.Objects.CR.CRContact (BillContactID=ContactID)
PX.Objects.CR.CROpportunity.LocaleByLanguageID -> PX.SM.Locale (LanguageID=LocaleName)
PX.Objects.CR.CROpportunity.CRTaxTranCollection -> Collection(PX.Objects.CR.CRTaxTran)
PX.Objects.CR.CROpportunity.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.CR.CROpportunity.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.CR.CROpportunity.CROpportunityDiscountDetailCollection -> Collection(PX.Objects.CR.CROpportunityDiscountDetail)
PX.Objects.CR.CROpportunity.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)
PX.Objects.CR.CROpportunity.AMEstimateReferenceCollection -> Collection(PX.Objects.AM.AMEstimateReference)
PX.Objects.CR.CROpportunity.PMQuoteCollection -> Collection(PX.Objects.PM.PMQuote)
PX.Objects.CR.CROpportunity.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)

# PX.Objects.CR.CROpportunityClass (EntityType)

Label: "Opportunity Class"
Key: CROpportunityClassID
Entity sets: PX_Objects_CR_CROpportunityClass, OpportunityClass, CROpportunityClass
Non-filterable, non-selectable: NoteText

PX.Objects.CR.CROpportunityClass.CROpportunityClassID : Edm.String [key] "Opportunity Class ID"
PX.Objects.CR.CROpportunityClass.Description : Edm.String "Description"
PX.Objects.CR.CROpportunityClass.DefaultOwner : Edm.String "Default Owner"
PX.Objects.CR.CROpportunityClass.DefaultAssignmentMapID : Edm.Int32 "Assignment Map"
PX.Objects.CR.CROpportunityClass.DefaultEMailAccountID : Edm.Int32 "Default Email Account"
PX.Objects.CR.CROpportunityClass.IsInternal : Edm.Boolean [required] "Internal"
PX.Objects.CR.CROpportunityClass.ShowContactActivities : Edm.Boolean [required] "Show Activities from Source Lead"
PX.Objects.CR.CROpportunityClass.NoteID : Edm.Guid
PX.Objects.CR.CROpportunityClass.NoteText : Edm.String "Note Text"
PX.Objects.CR.CROpportunityClass.TargetContactClassID : Edm.String "Contact Class"
PX.Objects.CR.CROpportunityClass.TargetBAccountClassID : Edm.String "Business Account Class"
PX.Objects.CR.CROpportunityClass.tstamp : Edm.Binary
PX.Objects.CR.CROpportunityClass.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CROpportunityClass.CreatedByScreenID : Edm.String
PX.Objects.CR.CROpportunityClass.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityClass.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CROpportunityClass.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CROpportunityClass.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityClass.CRContactClassByTargetContactClassID -> PX.Objects.CR.CRContactClass (TargetContactClassID=ClassID)
PX.Objects.CR.CROpportunityClass.CRCustomerClassByTargetBAccountClassID -> PX.Objects.CR.CRCustomerClass (TargetBAccountClassID=CRCustomerClassID)
PX.Objects.CR.CROpportunityClass.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CROpportunityClass.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CROpportunityClass.EMailAccountByDefaultEMailAccountID -> PX.SM.EMailAccount (DefaultEMailAccountID=EmailAccountID)
PX.Objects.CR.CROpportunityClass.EPAssignmentMapByDefaultAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultAssignmentMapID=AssignmentMapID)
PX.Objects.CR.CROpportunityClass.CRContactClassCollection -> Collection(PX.Objects.CR.CRContactClass)
PX.Objects.CR.CROpportunityClass.CRLeadClassCollection -> Collection(PX.Objects.CR.CRLeadClass)
PX.Objects.CR.CROpportunityClass.CRSetupCollection -> Collection(PX.Objects.CR.CRSetup)
PX.Objects.CR.CROpportunityClass.CROpportunityClassProbabilityCollection -> Collection(PX.Objects.CR.CROpportunityClassProbability)
PX.Objects.CR.CROpportunityClass.CROpportunityCollection -> Collection(PX.Objects.CR.CROpportunity)
PX.Objects.CR.CROpportunityClass.CRQuoteCollection -> Collection(PX.Objects.CR.CRQuote)

# PX.Objects.CR.CROpportunityClassProbability (EntityType)

Key: ClassID, StageID
Entity sets: PX_Objects_CR_CROpportunityClassProbability

PX.Objects.CR.CROpportunityClassProbability.ClassID : Edm.String [key]
PX.Objects.CR.CROpportunityClassProbability.StageID : Edm.String [key]
PX.Objects.CR.CROpportunityClassProbability.tstamp : Edm.Binary
PX.Objects.CR.CROpportunityClassProbability.CreatedByScreenID : Edm.String
PX.Objects.CR.CROpportunityClassProbability.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CROpportunityClassProbability.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityClassProbability.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CROpportunityClassProbability.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CROpportunityClassProbability.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityClassProbability.CROpportunityClassByClassID -> PX.Objects.CR.CROpportunityClass (ClassID=CROpportunityClassID)
PX.Objects.CR.CROpportunityClassProbability.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CROpportunityClassProbability.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CROpportunityClassProbability.CROpportunityProbabilityByStageID -> PX.Objects.CR.CROpportunityProbability (StageID=StageCode)

# PX.Objects.CR.CROpportunityDiscountDetail (EntityType)

Label: "Opportunity Discount"
Key: QuoteID, RecordID
Entity sets: PX_Objects_CR_CROpportunityDiscountDetail, OpportunityDiscount, CROpportunityDiscountDetail
Non-filterable, non-selectable: IsOrigDocDiscount

PX.Objects.CR.CROpportunityDiscountDetail.QuoteID : Edm.Guid [key]
PX.Objects.CR.CROpportunityDiscountDetail.RecordID : Edm.Int32 [key]
PX.Objects.CR.CROpportunityDiscountDetail.LineNbr : Edm.Int32
PX.Objects.CR.CROpportunityDiscountDetail.SkipDiscount : Edm.Boolean [required] "Skip Discount"
PX.Objects.CR.CROpportunityDiscountDetail.DiscountID : Edm.String "Discount Code"
PX.Objects.CR.CROpportunityDiscountDetail.DiscountSequenceID : Edm.String "Sequence ID"
PX.Objects.CR.CROpportunityDiscountDetail.Type : Edm.String "Type"
PX.Objects.CR.CROpportunityDiscountDetail.CuryInfoID : Edm.Int64
PX.Objects.CR.CROpportunityDiscountDetail.DiscountableAmt : Edm.Decimal
PX.Objects.CR.CROpportunityDiscountDetail.CuryDiscountableAmt : Edm.Decimal "Discountable Amt."
PX.Objects.CR.CROpportunityDiscountDetail.DiscountableQty : Edm.Decimal "Discountable Qty."
PX.Objects.CR.CROpportunityDiscountDetail.DiscountAmt : Edm.Decimal
PX.Objects.CR.CROpportunityDiscountDetail.CuryDiscountAmt : Edm.Decimal "Discount Amt."
PX.Objects.CR.CROpportunityDiscountDetail.DiscountPct : Edm.Decimal "Discount Percent"
PX.Objects.CR.CROpportunityDiscountDetail.FreeItemID : Edm.Int32 "Free Item"
PX.Objects.CR.CROpportunityDiscountDetail.FreeItemQty : Edm.Decimal "Free Item Qty."
PX.Objects.CR.CROpportunityDiscountDetail.IsManual : Edm.Boolean [required] "Manual Discount"
PX.Objects.CR.CROpportunityDiscountDetail.IsOrigDocDiscount : Edm.Boolean
PX.Objects.CR.CROpportunityDiscountDetail.ExtDiscCode : Edm.String "External Discount Code"
PX.Objects.CR.CROpportunityDiscountDetail.Description : Edm.String "Description"
PX.Objects.CR.CROpportunityDiscountDetail.tstamp : Edm.Binary
PX.Objects.CR.CROpportunityDiscountDetail.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CROpportunityDiscountDetail.CreatedByScreenID : Edm.String
PX.Objects.CR.CROpportunityDiscountDetail.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityDiscountDetail.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CROpportunityDiscountDetail.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CROpportunityDiscountDetail.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityDiscountDetail.InventoryItemByFreeItemID -> PX.Objects.IN.InventoryItem (FreeItemID=InventoryID)
PX.Objects.CR.CROpportunityDiscountDetail.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CROpportunityDiscountDetail.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CROpportunityDiscountDetail.DiscountSequenceByDiscountSequenceID -> PX.Objects.AR.DiscountSequence (DiscountID=DiscountID, DiscountSequenceID=DiscountSequenceID)
PX.Objects.CR.CROpportunityDiscountDetail.DiscountSequenceByDiscountID -> PX.Objects.AR.DiscountSequence (DiscountSequenceID=DiscountSequenceID, DiscountID=DiscountID)
PX.Objects.CR.CROpportunityDiscountDetail.CROpportunityByQuoteID -> PX.Objects.CR.CROpportunity (QuoteID=QuoteNoteID)

# PX.Objects.CR.CROpportunityProbability (EntityType)

Label: "Opportunity Probability"
Key: StageCode
Entity sets: PX_Objects_CR_CROpportunityProbability, OpportunityProbability, CROpportunityProbability
Non-filterable, non-selectable: IsActive, NoteText

PX.Objects.CR.CROpportunityProbability.StageCode : Edm.String [key] "Stage ID"
PX.Objects.CR.CROpportunityProbability.Probability : Edm.Int32 [required] "Probability"
PX.Objects.CR.CROpportunityProbability.Name : Edm.String "Name"
PX.Objects.CR.CROpportunityProbability.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.CR.CROpportunityProbability.IsActive : Edm.Boolean "Active"
PX.Objects.CR.CROpportunityProbability.CreatedByScreenID : Edm.String
PX.Objects.CR.CROpportunityProbability.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CROpportunityProbability.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityProbability.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CROpportunityProbability.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CROpportunityProbability.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityProbability.NoteID : Edm.Guid
PX.Objects.CR.CROpportunityProbability.NoteText : Edm.String "Note Text"
PX.Objects.CR.CROpportunityProbability.tstamp : Edm.Binary
PX.Objects.CR.CROpportunityProbability.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CROpportunityProbability.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CROpportunityProbability.CROpportunityClassProbabilityCollection -> Collection(PX.Objects.CR.CROpportunityClassProbability)

# PX.Objects.CR.CROpportunityProducts (EntityType)

Label: "Opportunity Products"
Key: LineNbr, QuoteID
Entity sets: PX_Objects_CR_CROpportunityProducts, OpportunityProducts, CROpportunityProducts
Non-filterable, non-selectable: CalculateDiscountsOnImport, TextForProductsGrid, PreferredVendorID, NoteText, StockItemType

PX.Objects.CR.CROpportunityProducts.QuoteID : Edm.Guid [key]
PX.Objects.CR.CROpportunityProducts.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CR.CROpportunityProducts.SortOrder : Edm.Int32 "Sort Order"
PX.Objects.CR.CROpportunityProducts.GroupLineNbr : Edm.Int32 "Group Line Nbr."
PX.Objects.CR.CROpportunityProducts.IsGroup : Edm.Boolean [required] "Group"
PX.Objects.CR.CROpportunityProducts.LineType : Edm.String "Type"
PX.Objects.CR.CROpportunityProducts.CuryInfoID : Edm.Int64
PX.Objects.CR.CROpportunityProducts.InventoryID : Edm.Int32 "Inventory ID"
PX.Objects.CR.CROpportunityProducts.ExpenseAccountGroupID : Edm.Int32 "Cost Account Group"
PX.Objects.CR.CROpportunityProducts.RevenueAccountGroupID : Edm.Int32 "Revenue Account Group"
PX.Objects.CR.CROpportunityProducts.EmployeeID : Edm.Int32 "Employee ID"
PX.Objects.CR.CROpportunityProducts.UOM : Edm.String "UOM"
PX.Objects.CR.CROpportunityProducts.Quantity : Edm.Decimal "Quantity"
PX.Objects.CR.CROpportunityProducts.BaseQuantity : Edm.Decimal "Base Qty."
PX.Objects.CR.CROpportunityProducts.CuryUnitPrice : Edm.Decimal [required] "Unit Price"
PX.Objects.CR.CROpportunityProducts.UnitPrice : Edm.Decimal [required]
PX.Objects.CR.CROpportunityProducts.POCreate : Edm.Boolean [required] "Mark for PO"
PX.Objects.CR.CROpportunityProducts.CuryUnitCost : Edm.Decimal [required] "Unit Cost"
PX.Objects.CR.CROpportunityProducts.CalculateDiscountsOnImport : Edm.Boolean "Calculate automatic discounts on import"
PX.Objects.CR.CROpportunityProducts.UnitCost : Edm.Decimal [required]
PX.Objects.CR.CROpportunityProducts.ManualDisc : Edm.Boolean "Manual Discount"
PX.Objects.CR.CROpportunityProducts.DiscPct : Edm.Decimal "Discount, %"
PX.Objects.CR.CROpportunityProducts.CuryExtPrice : Edm.Decimal "Ext. Price"
PX.Objects.CR.CROpportunityProducts.ExtPrice : Edm.Decimal
PX.Objects.CR.CROpportunityProducts.CuryExtCost : Edm.Decimal "Ext. Cost"
PX.Objects.CR.CROpportunityProducts.ExtCost : Edm.Decimal
PX.Objects.CR.CROpportunityProducts.CuryDiscAmt : Edm.Decimal "Discount Amount"
PX.Objects.CR.CROpportunityProducts.DiscAmt : Edm.Decimal
PX.Objects.CR.CROpportunityProducts.CuryAmount : Edm.Decimal "Amount"
PX.Objects.CR.CROpportunityProducts.Amount : Edm.Decimal
PX.Objects.CR.CROpportunityProducts.CustomerID : Edm.Int32
PX.Objects.CR.CROpportunityProducts.Descr : Edm.String "Description"
PX.Objects.CR.CROpportunityProducts.TaxCategoryID : Edm.String "Tax Category"
PX.Objects.CR.CROpportunityProducts.ProjectID : Edm.Int32
PX.Objects.CR.CROpportunityProducts.TaskCD : Edm.String "Project Task"
PX.Objects.CR.CROpportunityProducts.IsFree : Edm.Boolean [required] "Free Item"
PX.Objects.CR.CROpportunityProducts.ManualPrice : Edm.Boolean "Manual Price"
PX.Objects.CR.CROpportunityProducts.TextForProductsGrid : Edm.String "Availability footer"
PX.Objects.CR.CROpportunityProducts.PreferredVendorID : Edm.Int32
PX.Objects.CR.CROpportunityProducts.VendorID : Edm.Int32 "Vendor ID"
PX.Objects.CR.CROpportunityProducts.NoteID : Edm.Guid
PX.Objects.CR.CROpportunityProducts.NoteText : Edm.String "Note Text"
PX.Objects.CR.CROpportunityProducts.tstamp : Edm.Binary
PX.Objects.CR.CROpportunityProducts.GroupDiscountRate : Edm.Decimal
PX.Objects.CR.CROpportunityProducts.DocumentDiscountRate : Edm.Decimal
PX.Objects.CR.CROpportunityProducts.DiscountID : Edm.String "Discount Code"
PX.Objects.CR.CROpportunityProducts.DiscountSequenceID : Edm.String "Discount Sequence"
PX.Objects.CR.CROpportunityProducts.SkipLineDiscounts : Edm.Boolean [required] "Ignore Automatic Line Discounts"
PX.Objects.CR.CROpportunityProducts.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CROpportunityProducts.CreatedByScreenID : Edm.String
PX.Objects.CR.CROpportunityProducts.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityProducts.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CROpportunityProducts.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CROpportunityProducts.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityProducts.StockItemType : Edm.String
PX.Objects.CR.CROpportunityProducts.CuryMarginAmt : Edm.Decimal "Est. Margin Amount"
PX.Objects.CR.CROpportunityProducts.MarginAmt : Edm.Decimal
PX.Objects.CR.CROpportunityProducts.MarginPct : Edm.Decimal "Est. Margin (%)"
PX.Objects.CR.CROpportunityProducts.CuryNetSales : Edm.Decimal [required]
PX.Objects.CR.CROpportunityProducts.NetSales : Edm.Decimal [required]
PX.Objects.CR.CROpportunityProducts.SubstitutionRequired : Edm.Boolean [required] "Substitution Required"
PX.Objects.CR.CROpportunityProducts.EPEmployeeByEmployeeID -> PX.Objects.EP.EPEmployee (EmployeeID=BAccountID)
PX.Objects.CR.CROpportunityProducts.PMTaskByProjectID -> PX.Objects.PM.PMTask (ProjectID=ProjectID)
PX.Objects.CR.CROpportunityProducts.BAccountByVendorID -> PX.Objects.CR.BAccount (VendorID=BAccountID)
PX.Objects.CR.CROpportunityProducts.InventoryItemByInventoryID -> PX.Objects.IN.InventoryItem (InventoryID=InventoryID)
PX.Objects.CR.CROpportunityProducts.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CROpportunityProducts.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CROpportunityProducts.TaxCategoryByTaxCategoryID -> PX.Objects.TX.TaxCategory (TaxCategoryID=TaxCategoryID)
PX.Objects.CR.CROpportunityProducts.INSiteBySiteID -> PX.Objects.IN.INSite
PX.Objects.CR.CROpportunityProducts.INSubItemBySubItemID -> PX.Objects.IN.INSubItem
PX.Objects.CR.CROpportunityProducts.INUnitByInventoryID -> PX.Objects.IN.INUnit (UOM=FromUnit, InventoryID=InventoryID)
PX.Objects.CR.CROpportunityProducts.ARDiscountByDiscountID -> PX.Objects.AR.ARDiscount (DiscountID=DiscountID)
PX.Objects.CR.CROpportunityProducts.CROpportunityByQuoteID -> PX.Objects.CR.CROpportunity (QuoteID=QuoteNoteID)
PX.Objects.CR.CROpportunityProducts.CRQuoteByQuoteID -> PX.Objects.CR.CRQuote (QuoteID=NoteID)
PX.Objects.CR.CROpportunityProducts.CROpportunityTaxCollection -> Collection(PX.Objects.CR.CROpportunityTax)
PX.Objects.CR.CROpportunityProducts.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)
PX.Objects.CR.CROpportunityProducts.AMConfigurationResultsCollection -> Collection(PX.Objects.AM.AMConfigurationResults)

# PX.Objects.CR.CROpportunityTax (EntityType)

Label: "CR Tax Detail"
Key: LineNbr, QuoteID, TaxID
Entity sets: PX_Objects_CR_CROpportunityTax, CRTaxDetail, CROpportunityTax
Non-filterable, non-selectable: NonDeductibleTaxRate, ExpenseAmt

PX.Objects.CR.CROpportunityTax.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.CR.CROpportunityTax.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.CR.CROpportunityTax.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CR.CROpportunityTax.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CR.CROpportunityTax.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CROpportunityTax.CreatedByScreenID : Edm.String
PX.Objects.CR.CROpportunityTax.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityTax.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CROpportunityTax.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CROpportunityTax.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CROpportunityTax.QuoteID : Edm.Guid [key]
PX.Objects.CR.CROpportunityTax.LineNbr : Edm.Int32 [key] "Line Nbr."
PX.Objects.CR.CROpportunityTax.TaxID : Edm.String [key] "Tax ID"
PX.Objects.CR.CROpportunityTax.CuryInfoID : Edm.Int64
PX.Objects.CR.CROpportunityTax.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CR.CROpportunityTax.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CR.CROpportunityTax.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CR.CROpportunityTax.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CR.CROpportunityTax.tstamp : Edm.Binary
PX.Objects.CR.CROpportunityTax.CROpportunityProductsByLineNbr -> PX.Objects.CR.CROpportunityProducts (QuoteID=QuoteID, LineNbr=LineNbr)
PX.Objects.CR.CROpportunityTax.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CROpportunityTax.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CROpportunityTax.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.CR.CROpportunityTax.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.CR.CROpportunityTax.CROpportunityRevisionByQuoteID -> PX.Objects.CR.Standalone.CROpportunityRevision (QuoteID=NoteID)

# PX.Objects.CR.CRPMSMEmail (EntityType)

Label: "Activity"
BaseType: PX.Objects.CR.CRActivity
Key: NoteID (inherited from PX.Objects.CR.CRActivity)
Entity sets: PX_Objects_CR_CRPMSMEmail

PX.Objects.CR.CRPMSMEmail.TimeActivityNoteID : Edm.Guid
PX.Objects.CR.CRPMSMEmail.EmailNoteID : Edm.Guid
PX.Objects.CR.CRPMSMEmail.ResponseToNoteID : Edm.Guid "In Response To"
PX.Objects.CR.CRPMSMEmail.IsBillable : Edm.Boolean
PX.Objects.CR.CRPMSMEmail.CostCodeID : Edm.Int32
PX.Objects.CR.CRPMSMEmail.TimeCardCD : Edm.String
PX.Objects.CR.CRPMSMEmail.MPStatus : Edm.String
PX.Objects.CR.CRPMSMEmail.IsArchived : Edm.Boolean
PX.Objects.CR.CRPMSMEmail.TrackingID : Edm.String "TrackingID"
PX.Objects.CR.CRPMSMEmail.MessageId : Edm.String "MessageId"
PX.Objects.CR.CRPMSMEmail.PMCostCodeByCostCodeID -> PX.Objects.PM.PMCostCode (CostCodeID=CostCodeID)
PX.Objects.CR.CRPMSMEmail.EPTimeCardByTimeCardCD -> PX.Objects.EP.EPTimeCard (TimeCardCD=TimeCardCD)

# PX.Objects.CR.CRPMTimeActivity (EntityType)

Label: "Activity"
BaseType: PX.Objects.CR.CRActivity
Key: NoteID (inherited from PX.Objects.CR.CRActivity)
Entity sets: PX_Objects_CR_CRPMTimeActivity
Non-filterable, non-selectable: ARDocType, ARRefNbr, ChildKey

PX.Objects.CR.CRPMTimeActivity.TimeActivityNoteID : Edm.Guid
PX.Objects.CR.CRPMTimeActivity.TimeActivityRefNoteID : Edm.Guid
PX.Objects.CR.CRPMTimeActivity.ParentTaskNoteID : Edm.Guid "Task"
PX.Objects.CR.CRPMTimeActivity.TrackTime : Edm.Boolean "Track Time"
PX.Objects.CR.CRPMTimeActivity.TimeCardCD : Edm.String "TimeCardCD"
PX.Objects.CR.CRPMTimeActivity.TimeSheetCD : Edm.String "TimeSheetCD"
PX.Objects.CR.CRPMTimeActivity.Summary : Edm.String "Summary"
PX.Objects.CR.CRPMTimeActivity.Date : Edm.DateTimeOffset "Date"
PX.Objects.CR.CRPMTimeActivity.TimeActivityOwner : Edm.Int32 "Owner"
PX.Objects.CR.CRPMTimeActivity.ApproverID : Edm.Int32 "Approver"
PX.Objects.CR.CRPMTimeActivity.ApprovalStatus : Edm.String "Approval Status"
PX.Objects.CR.CRPMTimeActivity.ApprovedDate : Edm.DateTimeOffset "Approved Date"
PX.Objects.CR.CRPMTimeActivity.EarningTypeID : Edm.String "Earning Type"
PX.Objects.CR.CRPMTimeActivity.ExtRefNbr : Edm.String "External Ref. Nbr"
PX.Objects.CR.CRPMTimeActivity.ContractID : Edm.Int32 "Contract"
PX.Objects.CR.CRPMTimeActivity.TimeSpent : Edm.Int32 "Time Spent"
PX.Objects.CR.CRPMTimeActivity.OvertimeSpent : Edm.Int32 "Overtime"
PX.Objects.CR.CRPMTimeActivity.IsCorrected : Edm.Boolean
PX.Objects.CR.CRPMTimeActivity.OrigNoteID : Edm.Guid
PX.Objects.CR.CRPMTimeActivity.TranID : Edm.Int64
PX.Objects.CR.CRPMTimeActivity.ReportedInTimeZoneID : Edm.String "Reported in Time Zone"
PX.Objects.CR.CRPMTimeActivity.TimeCardPeriodType : Edm.String "Frequency"
PX.Objects.CR.CRPMTimeActivity.WeekID : Edm.Int32 "Time Card Week"
PX.Objects.CR.CRPMTimeActivity.LabourItemID : Edm.Int32 "LabourItemID"
PX.Objects.CR.CRPMTimeActivity.OvertimeItemID : Edm.Int32 "OvertimeItemID"
PX.Objects.CR.CRPMTimeActivity.JobID : Edm.Int32
PX.Objects.CR.CRPMTimeActivity.ShiftID : Edm.Int32
PX.Objects.CR.CRPMTimeActivity.EmployeeRate : Edm.Decimal "EmployeeRate"
PX.Objects.CR.CRPMTimeActivity.SummaryLineNbr : Edm.Int32
PX.Objects.CR.CRPMTimeActivity.ARDocType : Edm.String "Type"
PX.Objects.CR.CRPMTimeActivity.ARRefNbr : Edm.String "Reference Nbr."
PX.Objects.CR.CRPMTimeActivity.TimeActivityCreatedByID : Edm.Guid "TimeActivityCreatedByID"
PX.Objects.CR.CRPMTimeActivity.TimeActivityCreatedByScreenID : Edm.String
PX.Objects.CR.CRPMTimeActivity.TimeActivityCreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.CRPMTimeActivity.TimeActivityLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRPMTimeActivity.TimeActivityLastModifiedByScreenID : Edm.String
PX.Objects.CR.CRPMTimeActivity.TimeActivityLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRPMTimeActivity.ChildKey : Edm.Guid
PX.Objects.CR.CRPMTimeActivity.EPEmployeeByApproverID -> PX.Objects.EP.EPEmployee (ApproverID=BAccountID)
PX.Objects.CR.CRPMTimeActivity.ContractByContractID -> PX.Objects.CT.Contract (ContractID=ContractID)
PX.Objects.CR.CRPMTimeActivity.CRActivityBySubject -> PX.Objects.CR.CRActivity (Subject=Subject)
PX.Objects.CR.CRPMTimeActivity.CRActivityByRefNoteID -> PX.Objects.CR.CRActivity (RefNoteID=NoteID)
PX.Objects.CR.CRPMTimeActivity.EPEarningTypeByEarningTypeID -> PX.Objects.EP.EPEarningType (EarningTypeID=TypeCD)
PX.Objects.CR.CRPMTimeActivity.EPShiftCodeByShiftID -> PX.Objects.EP.EPShiftCode (ShiftID=ShiftID)
PX.Objects.CR.CRPMTimeActivity.VendorByApproverID -> PX.Objects.AP.Vendor (ApproverID=BAccountID)
PX.Objects.CR.CRPMTimeActivity.PMTimeActivityByOrigNoteID -> PX.Objects.CR.PMTimeActivity (OrigNoteID=NoteID)
PX.Objects.CR.CRPMTimeActivity.InventoryItemByLabourItemID -> PX.Objects.IN.InventoryItem (LabourItemID=InventoryID)
PX.Objects.CR.CRPMTimeActivity.InventoryItemByOvertimeItemID -> PX.Objects.IN.InventoryItem (OvertimeItemID=InventoryID)
PX.Objects.CR.CRPMTimeActivity.CRActivityByParentTaskNoteID -> PX.Objects.CR.CRActivity (ParentTaskNoteID=NoteID)
PX.Objects.CR.CRPMTimeActivity.EPTimeCardByTimeCardCD -> PX.Objects.EP.EPTimeCard (TimeCardCD=TimeCardCD)

# PX.Objects.CR.CRQuote (EntityType)

Label: "Sales Quote"
Key: QuoteNbr
Entity sets: PX_Objects_CR_CRQuote, SalesQuote, CRQuote
Non-filterable, non-selectable: IsPrimary, AllowOverrideBillingContactAddress, Hold, IsSetupApprovalRequired, IsDisabled, TextForProductsGrid, CuryWgtAmount, NoteText, SuggestRelatedItems, CuryRate

PX.Objects.CR.CRQuote.QuoteID : Edm.Guid
PX.Objects.CR.CRQuote.OpportunityID : Edm.String "Opportunity ID"
PX.Objects.CR.CRQuote.QuoteNbr : Edm.String [key] "Quote Nbr."
PX.Objects.CR.CRQuote.QuoteNbrUnq : Edm.String "Original Quote Nbr."
PX.Objects.CR.CRQuote.QuoteType : Edm.String "Type"
PX.Objects.CR.CRQuote.DefQuoteID : Edm.Guid
PX.Objects.CR.CRQuote.IsPrimary : Edm.Boolean "Primary"
PX.Objects.CR.CRQuote.ExternalRef : Edm.String "Ext. Ref. Nbr."
PX.Objects.CR.CRQuote.ManualTotalEntry : Edm.Boolean "Manual Amount"
PX.Objects.CR.CRQuote.TermsID : Edm.String "Credit Terms"
PX.Objects.CR.CRQuote.DocumentDate : Edm.DateTimeOffset "Date"
PX.Objects.CR.CRQuote.ExpirationDate : Edm.DateTimeOffset "Expiration Date"
PX.Objects.CR.CRQuote.Status : Edm.String "Status"
PX.Objects.CR.CRQuote.OpportunityAddressID : Edm.Int32
PX.Objects.CR.CRQuote.OpportunityContactID : Edm.Int32
PX.Objects.CR.CRQuote.AllowOverrideContactAddress : Edm.Boolean "Override"
PX.Objects.CR.CRQuote.BAccountID : Edm.Int32 "Business Account"
PX.Objects.CR.CRQuote.ShipContactID : Edm.Int32
PX.Objects.CR.CRQuote.ShipAddressID : Edm.Int32
PX.Objects.CR.CRQuote.AllowOverrideShippingContactAddress : Edm.Boolean "Override Shipping Info"
PX.Objects.CR.CRQuote.AllowOverrideBillingContactAddress : Edm.Boolean
PX.Objects.CR.CRQuote.BillContactID : Edm.Int32
PX.Objects.CR.CRQuote.BillAddressID : Edm.Int32
PX.Objects.CR.CRQuote.ContactID : Edm.Int32 "Contact"
PX.Objects.CR.CRQuote.Subject : Edm.String "Description"
PX.Objects.CR.CRQuote.ParentBAccountID : Edm.Int32 "Parent Account"
PX.Objects.CR.CRQuote.QuoteProjectID : Edm.Int32 "Project ID"
PX.Objects.CR.CRQuote.CampaignSourceID : Edm.String "Source Campaign"
PX.Objects.CR.CRQuote.WorkgroupID : Edm.Int32 "Workgroup"
PX.Objects.CR.CRQuote.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.CRQuote.Approved : Edm.Boolean "Approved"
PX.Objects.CR.CRQuote.Rejected : Edm.Boolean "Rejected"
PX.Objects.CR.CRQuote.Hold : Edm.Boolean "Hold"
PX.Objects.CR.CRQuote.IsSetupApprovalRequired : Edm.Boolean "Approvable Setup"
PX.Objects.CR.CRQuote.IsDisabled : Edm.Boolean "Disabled"
PX.Objects.CR.CRQuote.CuryID : Edm.String "Currency"
PX.Objects.CR.CRQuote.CuryInfoID : Edm.Int64
PX.Objects.CR.CRQuote.ExtPriceTotal : Edm.Decimal
PX.Objects.CR.CRQuote.CuryExtPriceTotal : Edm.Decimal "Detail Total"
PX.Objects.CR.CRQuote.LineTotal : Edm.Decimal
PX.Objects.CR.CRQuote.CuryLineTotal : Edm.Decimal "Detail Total"
PX.Objects.CR.CRQuote.LineDiscountTotal : Edm.Decimal
PX.Objects.CR.CRQuote.CuryLineDiscountTotal : Edm.Decimal "Line Discounts"
PX.Objects.CR.CRQuote.LineDocDiscountTotal : Edm.Decimal
PX.Objects.CR.CRQuote.CuryLineDocDiscountTotal : Edm.Decimal "CuryLineDocDiscountTotal"
PX.Objects.CR.CRQuote.TextForProductsGrid : Edm.String "Availability footer"
PX.Objects.CR.CRQuote.IsTaxValid : Edm.Boolean "Tax Is Up to Date"
PX.Objects.CR.CRQuote.TaxTotal : Edm.Decimal
PX.Objects.CR.CRQuote.CuryTaxTotal : Edm.Decimal "Tax Total"
PX.Objects.CR.CRQuote.Amount : Edm.Decimal
PX.Objects.CR.CRQuote.CuryAmount : Edm.Decimal "Detail Total"
PX.Objects.CR.CRQuote.DiscTot : Edm.Decimal
PX.Objects.CR.CRQuote.CuryDiscTot : Edm.Decimal "Document Discounts"
PX.Objects.CR.CRQuote.CuryProductsAmount : Edm.Decimal "Total"
PX.Objects.CR.CRQuote.CuryOrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.CR.CRQuote.OrderDiscTotal : Edm.Decimal "Discount Total"
PX.Objects.CR.CRQuote.ProductsAmount : Edm.Decimal
PX.Objects.CR.CRQuote.CuryWgtAmount : Edm.Decimal "Wgt. Total"
PX.Objects.CR.CRQuote.CuryVatExemptTotal : Edm.Decimal "VAT Exempt Total"
PX.Objects.CR.CRQuote.VatExemptTotal : Edm.Decimal
PX.Objects.CR.CRQuote.CuryVatTaxableTotal : Edm.Decimal "VAT Taxable Total"
PX.Objects.CR.CRQuote.VatTaxableTotal : Edm.Decimal
PX.Objects.CR.CRQuote.TaxZoneID : Edm.String "Tax Zone"
PX.Objects.CR.CRQuote.TaxCalcMode : Edm.String "Tax Calculation Mode"
PX.Objects.CR.CRQuote.TaxRegistrationID : Edm.String "Tax Registration ID"
PX.Objects.CR.CRQuote.ExternalTaxExemptionNumber : Edm.String "Tax Exemption Number"
PX.Objects.CR.CRQuote.AvalaraCustomerUsageType : Edm.String "Tax Exemption Type"
PX.Objects.CR.CRQuote.NoteID : Edm.Guid
PX.Objects.CR.CRQuote.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRQuote.RNoteID : Edm.Guid
PX.Objects.CR.CRQuote.ProductCntr : Edm.Int32
PX.Objects.CR.CRQuote.LineCntr : Edm.Int32
PX.Objects.CR.CRQuote.RefOpportunityID : Edm.String
PX.Objects.CR.CRQuote.OpportunityClassID : Edm.String "Opportunity Class"
PX.Objects.CR.CRQuote.OpportunityStageChangedDate : Edm.DateTimeOffset "Opportunity Stage Change Date"
PX.Objects.CR.CRQuote.OpportunityStageID : Edm.String "Opportunity Stage"
PX.Objects.CR.CRQuote.OpportunityIsActive : Edm.Boolean "Opportunity Is Active"
PX.Objects.CR.CRQuote.OpportunityStatus : Edm.String "Opportunity Status"
PX.Objects.CR.CRQuote.tstamp : Edm.Binary
PX.Objects.CR.CRQuote.CreatedByScreenID : Edm.String
PX.Objects.CR.CRQuote.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRQuote.CreatedDateTime : Edm.DateTimeOffset "Date Created"
PX.Objects.CR.CRQuote.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRQuote.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRQuote.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified Date"
PX.Objects.CR.CRQuote.RCreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRQuote.RCreatedByScreenID : Edm.String
PX.Objects.CR.CRQuote.RCreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRQuote.RLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRQuote.RLastModifiedByScreenID : Edm.String
PX.Objects.CR.CRQuote.RLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRQuote.SiteID : Edm.Int32 "Warehouse"
PX.Objects.CR.CRQuote.CarrierID : Edm.String "Ship Via"
PX.Objects.CR.CRQuote.ShipTermsID : Edm.String "Shipping Terms"
PX.Objects.CR.CRQuote.ShipZoneID : Edm.String "Shipping Zone"
PX.Objects.CR.CRQuote.FOBPointID : Edm.String "FOB Point"
PX.Objects.CR.CRQuote.Resedential : Edm.Boolean "Residential Delivery"
PX.Objects.CR.CRQuote.SaturdayDelivery : Edm.Boolean "Saturday Delivery"
PX.Objects.CR.CRQuote.Insurance : Edm.Boolean "Insurance"
PX.Objects.CR.CRQuote.ShipComplete : Edm.String "Shipping Rule"
PX.Objects.CR.CRQuote.CuryMarginAmt : Edm.Decimal "Est. Margin Amount"
PX.Objects.CR.CRQuote.MarginAmt : Edm.Decimal
PX.Objects.CR.CRQuote.MarginPct : Edm.Decimal "Est. Margin (%)"
PX.Objects.CR.CRQuote.CuryNetSalesTotal : Edm.Decimal
PX.Objects.CR.CRQuote.NetSalesTotal : Edm.Decimal
PX.Objects.CR.CRQuote.CurySalesCostTotal : Edm.Decimal
PX.Objects.CR.CRQuote.SalesCostTotal : Edm.Decimal
PX.Objects.CR.CRQuote.SuggestRelatedItems : Edm.Boolean
PX.Objects.CR.CRQuote.CuryRate : Edm.Decimal
PX.Objects.CR.CRQuote.PMProjectByQuoteProjectID -> PX.Objects.PM.PMProject (QuoteProjectID=ContractID)
PX.Objects.CR.CRQuote.BAccountByBAccountID -> PX.Objects.CR.BAccount (BAccountID=BAccountID)
PX.Objects.CR.CRQuote.BAccountByParentBAccountID -> PX.Objects.CR.BAccount (ParentBAccountID=BAccountID)
PX.Objects.CR.CRQuote.ContactByContactID -> PX.Objects.CR.Contact (ContactID=ContactID)
PX.Objects.CR.CRQuote.ContactByOwnerID -> PX.Objects.CR.Contact (OwnerID=ContactID)
PX.Objects.CR.CRQuote.CROpportunityClassByOpportunityClassID -> PX.Objects.CR.CROpportunityClass (OpportunityClassID=CROpportunityClassID)
PX.Objects.CR.CRQuote.CurrencyInfoByCuryInfoID -> PX.Objects.CM.CurrencyInfo (CuryInfoID=CuryInfoID)
PX.Objects.CR.CRQuote.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRQuote.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRQuote.EPCompanyTreeByWorkgroupID -> PX.TM.EPCompanyTree (WorkgroupID=WorkGroupID)
PX.Objects.CR.CRQuote.TaxZoneByTaxZoneID -> PX.Objects.TX.TaxZone (TaxZoneID=TaxZoneID)
PX.Objects.CR.CRQuote.CarrierByCarrierID -> PX.Objects.CS.Carrier (CarrierID=CarrierID)
PX.Objects.CR.CRQuote.FOBPointByFOBPointID -> PX.Objects.CS.FOBPoint (FOBPointID=FOBPointID)
PX.Objects.CR.CRQuote.SalesTerritoryBySalesTerritoryID -> PX.Objects.CS.SalesTerritory
PX.Objects.CR.CRQuote.ShippingZoneByShipZoneID -> PX.Objects.CS.ShippingZone (ShipZoneID=ZoneID)
PX.Objects.CR.CRQuote.ShipTermsByShipTermsID -> PX.Objects.CS.ShipTerms (ShipTermsID=ShipTermsID)
PX.Objects.CR.CRQuote.TermsByTermsID -> PX.Objects.CS.Terms (TermsID=TermsID)
PX.Objects.CR.CRQuote.INSiteBySiteID -> PX.Objects.IN.INSite (SiteID=SiteID)
PX.Objects.CR.CRQuote.CurrencyByCuryID -> PX.Objects.CM.Currency (CuryID=CuryID)
PX.Objects.CR.CRQuote.LocationByLocationID -> PX.Objects.CR.Location (BAccountID=BAccountID)
PX.Objects.CR.CRQuote.CRAddressByOpportunityAddressID -> PX.Objects.CR.CRAddress (OpportunityAddressID=AddressID)
PX.Objects.CR.CRQuote.CRAddressByShipAddressID -> PX.Objects.CR.CRAddress (ShipAddressID=AddressID)
PX.Objects.CR.CRQuote.CRAddressByBillAddressID -> PX.Objects.CR.CRAddress (BillAddressID=AddressID)
PX.Objects.CR.CRQuote.CRCampaignByCampaignSourceID -> PX.Objects.CR.CRCampaign (CampaignSourceID=CampaignID)
PX.Objects.CR.CRQuote.CRContactByOpportunityContactID -> PX.Objects.CR.CRContact (OpportunityContactID=ContactID)
PX.Objects.CR.CRQuote.CRContactByShipContactID -> PX.Objects.CR.CRContact (ShipContactID=ContactID)
PX.Objects.CR.CRQuote.CRContactByBillContactID -> PX.Objects.CR.CRContact (BillContactID=ContactID)
PX.Objects.CR.CRQuote.CROpportunityByOpportunityID -> PX.Objects.CR.CROpportunity (OpportunityID=OpportunityID)
PX.Objects.CR.CRQuote.CROpportunityProductsCollection -> Collection(PX.Objects.CR.CROpportunityProducts)
PX.Objects.CR.CRQuote.RelatedItemHistoryCollection -> Collection(PX.Objects.IN.RelatedItems.RelatedItemHistory)

# PX.Objects.CR.CRRelation (EntityType)

Label: "Relations"
Key: RelationID
Entity sets: PX_Objects_CR_CRRelation, Relations, CRRelation
Non-filterable, non-selectable: EntityCD, Name, ContactName, Email, Status, Description, OwnerID, DocumentDate

PX.Objects.CR.CRRelation.RelationID : Edm.Int32 [key] "RelationID"
PX.Objects.CR.CRRelation.RefNoteID : Edm.Guid
PX.Objects.CR.CRRelation.RefEntityType : Edm.String "Ref Type"
PX.Objects.CR.CRRelation.Role : Edm.String "Role"
PX.Objects.CR.CRRelation.IsPrimary : Edm.Boolean [required] "Primary"
PX.Objects.CR.CRRelation.TargetType : Edm.String "Type"
PX.Objects.CR.CRRelation.TargetNoteID : Edm.Guid "Document"
PX.Objects.CR.CRRelation.DocNoteID : Edm.Guid
PX.Objects.CR.CRRelation.EntityID : Edm.Int32 "Account"
PX.Objects.CR.CRRelation.ContactID : Edm.Int32 "Contact"
PX.Objects.CR.CRRelation.AddToCC : Edm.Boolean [required] "Add to CC"
PX.Objects.CR.CRRelation.CreatedByID : Edm.Guid "Creator"
PX.Objects.CR.CRRelation.CreatedByScreenID : Edm.String
PX.Objects.CR.CRRelation.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.CRRelation.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRRelation.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRRelation.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRRelation.EntityCD : Edm.String "Account/Employee"
PX.Objects.CR.CRRelation.Name : Edm.String "Name"
PX.Objects.CR.CRRelation.ContactName : Edm.String "Contact"
PX.Objects.CR.CRRelation.Email : Edm.String "Email"
PX.Objects.CR.CRRelation.Status : Edm.String "Status"
PX.Objects.CR.CRRelation.Description : Edm.String "Description"
PX.Objects.CR.CRRelation.OwnerID : Edm.Int32 "Owner"
PX.Objects.CR.CRRelation.DocumentDate : Edm.DateTimeOffset "Document Date"
PX.Objects.CR.CRRelation.ARInvoiceByRefNoteID -> PX.Objects.AR.ARInvoice (RefNoteID=NoteID)
PX.Objects.CR.CRRelation.BAccountByEntityID -> PX.Objects.CR.BAccount (EntityID=BAccountID)
PX.Objects.CR.CRRelation.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRRelation.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CR.CRReminder (EntityType)

Label: "Reminder"
Key: NoteID
Entity sets: PX_Objects_CR_CRReminder, Reminder, CRReminder
Non-filterable, non-selectable: IsReminderOn, ReminderIcon, NoteText

PX.Objects.CR.CRReminder.IsReminderOn : Edm.Boolean "Reminder"
PX.Objects.CR.CRReminder.ReminderIcon : Edm.String "Reminder Icon"
PX.Objects.CR.CRReminder.NoteID : Edm.Guid [key]
PX.Objects.CR.CRReminder.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRReminder.RefNoteID : Edm.Guid
PX.Objects.CR.CRReminder.ReminderDate : Edm.DateTimeOffset "Remind At"
PX.Objects.CR.CRReminder.RemindAt : Edm.String "Remind At"
PX.Objects.CR.CRReminder.Owner : Edm.Int32 "Owner"
PX.Objects.CR.CRReminder.Dismiss : Edm.Boolean
PX.Objects.CR.CRReminder.CreatedByID : Edm.Guid "CreatedByID"
PX.Objects.CR.CRReminder.CreatedByScreenID : Edm.String
PX.Objects.CR.CRReminder.CreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.CRReminder.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRReminder.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRReminder.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRReminder.tstamp : Edm.Binary
PX.Objects.CR.CRReminder.ContactByOwner -> PX.Objects.CR.Contact (Owner=ContactID)
PX.Objects.CR.CRReminder.CRActivityByRefNoteID -> PX.Objects.CR.CRActivity (RefNoteID=NoteID)
PX.Objects.CR.CRReminder.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRReminder.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)

# PX.Objects.CR.CRSetup (EntityType)

Label: "Customer Management Preferences"
Singletons: PX_Objects_CR_CRSetup, CustomerManagementPreferences, CRSetup

PX.Objects.CR.CRSetup.CampaignNumberingID : Edm.String "Campaign Numbering Sequence"
PX.Objects.CR.CRSetup.OpportunityNumberingID : Edm.String "Opportunity Numbering Sequence"
PX.Objects.CR.CRSetup.QuoteNumberingID : Edm.String "Quote Numbering Sequence"
PX.Objects.CR.CRSetup.CaseNumberingID : Edm.String "Case Numbering Sequence"
PX.Objects.CR.CRSetup.MassMailNumberingID : Edm.String "Mass Mail Numbering Sequence"
PX.Objects.CR.CRSetup.DefaultCaseClassID : Edm.String "Default Case Class"
PX.Objects.CR.CRSetup.DefaultOpportunityClassID : Edm.String "Default Opportunity Class"
PX.Objects.CR.CRSetup.DefaultRateTypeID : Edm.String "Default Rate Type"
PX.Objects.CR.CRSetup.AllowOverrideRate : Edm.Boolean [required] "Enable Rate Override"
PX.Objects.CR.CRSetup.LeadDefaultAssignmentMapID : Edm.Int32 "Lead Assignment Map"
PX.Objects.CR.CRSetup.ContactDefaultAssignmentMapID : Edm.Int32 "Contact Assignment Map"
PX.Objects.CR.CRSetup.DefaultCaseAssignmentMapID : Edm.Int32 "Case Assignment Map"
PX.Objects.CR.CRSetup.DefaultBAccountAssignmentMapID : Edm.Int32 "Business Account Assignment Map"
PX.Objects.CR.CRSetup.DefaultOpportunityAssignmentMapID : Edm.Int32 "Opportunity Assignment Map"
PX.Objects.CR.CRSetup.QuoteApprovalMapID : Edm.Int32 "Approval Map"
PX.Objects.CR.CRSetup.QuoteApprovalNotificationID : Edm.Int32 "Pending Approval Notification"
PX.Objects.CR.CRSetup.DefaultLeadClassID : Edm.String "Default Lead Class"
PX.Objects.CR.CRSetup.DefaultContactClassID : Edm.String "Default Contact Class"
PX.Objects.CR.CRSetup.DefaultCustomerClassID : Edm.String "Default Business Account Class"
PX.Objects.CR.CRSetup.CopyNotes : Edm.Boolean [required] "Copy Notes"
PX.Objects.CR.CRSetup.CopyFiles : Edm.Boolean [required] "Copy Attachments"
PX.Objects.CR.CRSetup.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRSetup.CreatedByScreenID : Edm.String
PX.Objects.CR.CRSetup.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRSetup.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRSetup.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRSetup.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRSetup.tstamp : Edm.Binary
PX.Objects.CR.CRSetup.NoteID : Edm.Guid
PX.Objects.CR.CRSetup.NoteText : Edm.String "Note Text"
PX.Objects.CR.CRSetup.CRContactClassByDefaultContactClassID -> PX.Objects.CR.CRContactClass (DefaultContactClassID=ClassID)
PX.Objects.CR.CRSetup.CRCustomerClassByDefaultCustomerClassID -> PX.Objects.CR.CRCustomerClass (DefaultCustomerClassID=CRCustomerClassID)
PX.Objects.CR.CRSetup.CRLeadClassByDefaultLeadClassID -> PX.Objects.CR.CRLeadClass (DefaultLeadClassID=ClassID)
PX.Objects.CR.CRSetup.CROpportunityClassByDefaultOpportunityClassID -> PX.Objects.CR.CROpportunityClass (DefaultOpportunityClassID=CROpportunityClassID)
PX.Objects.CR.CRSetup.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRSetup.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRSetup.NotificationByQuoteApprovalNotificationID -> PX.SM.Notification (QuoteApprovalNotificationID=NotificationID)
PX.Objects.CR.CRSetup.NumberingByCampaignNumberingID -> PX.Objects.CS.Numbering (CampaignNumberingID=NumberingID)
PX.Objects.CR.CRSetup.NumberingByOpportunityNumberingID -> PX.Objects.CS.Numbering (OpportunityNumberingID=NumberingID)
PX.Objects.CR.CRSetup.NumberingByQuoteNumberingID -> PX.Objects.CS.Numbering (QuoteNumberingID=NumberingID)
PX.Objects.CR.CRSetup.NumberingByCaseNumberingID -> PX.Objects.CS.Numbering (CaseNumberingID=NumberingID)
PX.Objects.CR.CRSetup.NumberingByMassMailNumberingID -> PX.Objects.CS.Numbering (MassMailNumberingID=NumberingID)
PX.Objects.CR.CRSetup.CurrencyRateTypeByDefaultRateTypeID -> PX.Objects.CM.CurrencyRateType (DefaultRateTypeID=CuryRateTypeID)
PX.Objects.CR.CRSetup.CRCaseClassByDefaultCaseClassID -> PX.Objects.CR.CRCaseClass (DefaultCaseClassID=CaseClassID)
PX.Objects.CR.CRSetup.EPAssignmentMapByLeaddefaultAssignmentMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.CR.CRSetup.EPAssignmentMapByContactdefaultAssignmentMapID -> PX.Objects.EP.EPAssignmentMap
PX.Objects.CR.CRSetup.EPAssignmentMapByDefaultCaseAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultCaseAssignmentMapID=AssignmentMapID)
PX.Objects.CR.CRSetup.EPAssignmentMapByDefaultBAccountAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultBAccountAssignmentMapID=AssignmentMapID)
PX.Objects.CR.CRSetup.EPAssignmentMapByDefaultOpportunityAssignmentMapID -> PX.Objects.EP.EPAssignmentMap (DefaultOpportunityAssignmentMapID=AssignmentMapID)
PX.Objects.CR.CRSetup.EPAssignmentMapByQuoteApprovalMapID -> PX.Objects.EP.EPAssignmentMap (QuoteApprovalMapID=AssignmentMapID)

# PX.Objects.CR.CRShippingAddress (EntityType)

Label: "Shipping Address"
BaseType: PX.Objects.CR.CRAddress
Key: AddressID (inherited from PX.Objects.CR.CRAddress)
Entity sets: PX_Objects_CR_CRShippingAddress, ShippingAddress, CRShippingAddress

# PX.Objects.CR.CRShippingContact (EntityType)

Label: "Shipping Contact"
BaseType: PX.Objects.CR.CRContact
Key: ContactID (inherited from PX.Objects.CR.CRContact)
Entity sets: PX_Objects_CR_CRShippingContact, ShippingContact, CRShippingContact

# PX.Objects.CR.CRSMEmail (EntityType)

Label: "Email Activity"
BaseType: PX.Objects.CR.CRActivity
Key: NoteID (inherited from PX.Objects.CR.CRActivity)
Entity sets: PX_Objects_CR_CRSMEmail, EmailActivity, CRSMEmail
Non-filterable, non-selectable: DocumentSource, ClearedBody

PX.Objects.CR.CRSMEmail.DocumentSource : Edm.String "Related Document"
PX.Objects.CR.CRSMEmail.MPStatus : Edm.String "Email Status"
PX.Objects.CR.CRSMEmail.IsArchived : Edm.Boolean "Archived"
PX.Objects.CR.CRSMEmail.EmailNoteID : Edm.Guid
PX.Objects.CR.CRSMEmail.ResponseToNoteID : Edm.Guid "In Response To"
PX.Objects.CR.CRSMEmail.EmailRefNoteID : Edm.Guid
PX.Objects.CR.CRSMEmail.EmailSubject : Edm.String "Summary"
PX.Objects.CR.CRSMEmail.ImcUID : Edm.Guid "ImcUID"
PX.Objects.CR.CRSMEmail.Pop3UID : Edm.String "Pop3UID"
PX.Objects.CR.CRSMEmail.ImapUID : Edm.Int32 "ImapUID"
PX.Objects.CR.CRSMEmail.MailAccountID : Edm.Int32 "From"
PX.Objects.CR.CRSMEmail.MailFrom : Edm.String "From"
PX.Objects.CR.CRSMEmail.MailReply : Edm.String "Reply"
PX.Objects.CR.CRSMEmail.MailDate : Edm.DateTimeOffset
PX.Objects.CR.CRSMEmail.MailTo : Edm.String "To"
PX.Objects.CR.CRSMEmail.MailCc : Edm.String "CC"
PX.Objects.CR.CRSMEmail.MailBcc : Edm.String "BCC"
PX.Objects.CR.CRSMEmail.RetryCount : Edm.Int32 "RetryCount"
PX.Objects.CR.CRSMEmail.MessageId : Edm.String "MessageId"
PX.Objects.CR.CRSMEmail.MessageReference : Edm.String "MessageReference"
PX.Objects.CR.CRSMEmail.InReplyTo : Edm.String "InReplyTo"
PX.Objects.CR.CRSMEmail.Exception : Edm.String "Error Message"
PX.Objects.CR.CRSMEmail.Format : Edm.String "Format"
PX.Objects.CR.CRSMEmail.ReportFormat : Edm.String "Format"
PX.Objects.CR.CRSMEmail.TrackingID : Edm.String "TrackingID"
PX.Objects.CR.CRSMEmail.Ticket : Edm.String "Ticket"
PX.Objects.CR.CRSMEmail.IsIncome : Edm.Boolean "Is Income"
PX.Objects.CR.CRSMEmail.EmailCreatedByID : Edm.Guid "EmailCreatedByID"
PX.Objects.CR.CRSMEmail.EmailCreatedByScreenID : Edm.String
PX.Objects.CR.CRSMEmail.EmailCreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.CRSMEmail.EmailLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRSMEmail.EmailLastModifiedByScreenID : Edm.String
PX.Objects.CR.CRSMEmail.EmailLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRSMEmail.ClearedBody : Edm.String "Cleared Body"
PX.Objects.CR.CRSMEmail.CRSMEmailBySubject -> PX.Objects.CR.CRSMEmail (Subject=EmailSubject)
PX.Objects.CR.CRSMEmail.CRActivityBySubject -> PX.Objects.CR.CRActivity (Subject=Subject)
PX.Objects.CR.CRSMEmail.EMailAccountByMailAccountID -> PX.SM.EMailAccount (MailAccountID=EmailAccountID)
PX.Objects.CR.CRSMEmail.SMEmailByResponseToNoteID -> PX.Objects.CR.SMEmail (ResponseToNoteID=NoteID)
PX.Objects.CR.CRSMEmail.SMSendGridRecipientCollection -> Collection(PX.DataSync.SendGrid.SMSendGridRecipient)

# PX.Objects.CR.CRSMTeamsActivity (EntityType)

Label: "Teams Activity"
BaseType: PX.Objects.CR.CRActivity
Key: NoteID (inherited from PX.Objects.CR.CRActivity)
Entity sets: PX_Objects_CR_CRSMTeamsActivity, TeamsActivity, CRSMTeamsActivity
Non-filterable, non-selectable: DocumentSource

PX.Objects.CR.CRSMTeamsActivity.DocumentSource : Edm.String "Related Document"
PX.Objects.CR.CRSMTeamsActivity.MPStatus : Edm.String "Message Status"
PX.Objects.CR.CRSMTeamsActivity.TeamsActivityNoteID : Edm.Guid
PX.Objects.CR.CRSMTeamsActivity.TeamsActivityRefNoteID : Edm.Guid
PX.Objects.CR.CRSMTeamsActivity.TeamsActivitySubject : Edm.String "Summary"
PX.Objects.CR.CRSMTeamsActivity.ChannelID : Edm.String "Channel"
PX.Objects.CR.CRSMTeamsActivity.MemberID : Edm.Guid "Member"
PX.Objects.CR.CRSMTeamsActivity.IsIncome : Edm.Boolean "Is Income"
PX.Objects.CR.CRSMTeamsActivity.TeamsActivityCreatedByID : Edm.Guid "TeamsActivityCreatedByID"
PX.Objects.CR.CRSMTeamsActivity.TeamsActivityCreatedByScreenID : Edm.String
PX.Objects.CR.CRSMTeamsActivity.TeamsActivityCreatedDateTime : Edm.DateTimeOffset "Created At"
PX.Objects.CR.CRSMTeamsActivity.TeamsActivityLastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRSMTeamsActivity.TeamsActivityLastModifiedByScreenID : Edm.String
PX.Objects.CR.CRSMTeamsActivity.TeamsActivityLastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRSMTeamsActivity.CRSMTeamsActivityByTeamsActivitySubject -> PX.Objects.CR.CRSMTeamsActivity (TeamsActivitySubject=Subject)
PX.Objects.CR.CRSMTeamsActivity.CRSMTeamsActivityCollection -> Collection(PX.Objects.CR.CRSMTeamsActivity)

# PX.Objects.CR.CRTaxTran (EntityType)

Key: LineNbr, QuoteID, RecordID, TaxID
Entity sets: PX_Objects_CR_CRTaxTran
Non-filterable, non-selectable: TaxRate, NonDeductibleTaxRate, ExpenseAmt, CuryExpenseAmt, TaxZoneID

PX.Objects.CR.CRTaxTran.TaxRate : Edm.Decimal "Tax Rate"
PX.Objects.CR.CRTaxTran.NonDeductibleTaxRate : Edm.Decimal "Deductible Tax Rate"
PX.Objects.CR.CRTaxTran.ExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CR.CRTaxTran.CuryExpenseAmt : Edm.Decimal "Expense Amount"
PX.Objects.CR.CRTaxTran.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRTaxTran.CreatedByScreenID : Edm.String
PX.Objects.CR.CRTaxTran.CreatedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRTaxTran.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRTaxTran.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRTaxTran.LastModifiedDateTime : Edm.DateTimeOffset
PX.Objects.CR.CRTaxTran.RecordID : Edm.Int32 [key]
PX.Objects.CR.CRTaxTran.QuoteID : Edm.Guid [key]
PX.Objects.CR.CRTaxTran.LineNbr : Edm.Int32 [key required] "Line Nbr."
PX.Objects.CR.CRTaxTran.TaxID : Edm.String [key] "Tax ID"
PX.Objects.CR.CRTaxTran.JurisType : Edm.String "Tax Jurisdiction Type"
PX.Objects.CR.CRTaxTran.JurisName : Edm.String "Tax Jurisdiction Name"
PX.Objects.CR.CRTaxTran.CuryInfoID : Edm.Int64
PX.Objects.CR.CRTaxTran.CuryTaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CR.CRTaxTran.TaxableAmt : Edm.Decimal "Taxable Amount"
PX.Objects.CR.CRTaxTran.CuryTaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CR.CRTaxTran.TaxAmt : Edm.Decimal "Tax Amount"
PX.Objects.CR.CRTaxTran.TaxZoneID : Edm.String
PX.Objects.CR.CRTaxTran.tstamp : Edm.Binary
PX.Objects.CR.CRTaxTran.IsTaxInclusive : Edm.Boolean [required] "Tax Inclusive"
PX.Objects.CR.CRTaxTran.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRTaxTran.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRTaxTran.TaxByTaxID -> PX.Objects.TX.Tax (TaxID=TaxID)
PX.Objects.CR.CRTaxTran.INUnitByTaxUOM -> PX.Objects.IN.INUnit
PX.Objects.CR.CRTaxTran.CROpportunityByQuoteID -> PX.Objects.CR.CROpportunity (QuoteID=QuoteNoteID)

# PX.Objects.CR.CRUnsubscribedPreferences (EntityType)

Label: "Marketing Unsubscribed Contact"
Key: MarketingCategoryID, RecipientContact
Entity sets: PX_Objects_CR_CRUnsubscribedPreferences, MarketingUnsubscribedContact, CRUnsubscribedPreferences
Non-filterable, non-selectable: CategoryChannel

PX.Objects.CR.CRUnsubscribedPreferences.RecipientContact : Edm.String [key] "Recipient"
PX.Objects.CR.CRUnsubscribedPreferences.MarketingCategoryID : Edm.String [key] "Marketing Category"
PX.Objects.CR.CRUnsubscribedPreferences.CategoryChannel : Edm.String "Channel"
PX.Objects.CR.CRUnsubscribedPreferences.Source : Edm.String "Source"
PX.Objects.CR.CRUnsubscribedPreferences.CreatedByID : Edm.Guid "Created By"
PX.Objects.CR.CRUnsubscribedPreferences.CreatedByScreenID : Edm.String
PX.Objects.CR.CRUnsubscribedPreferences.CreatedDateTime : Edm.DateTimeOffset "Created"
PX.Objects.CR.CRUnsubscribedPreferences.LastModifiedByID : Edm.Guid "Last Modified By"
PX.Objects.CR.CRUnsubscribedPreferences.LastModifiedByScreenID : Edm.String
PX.Objects.CR.CRUnsubscribedPreferences.LastModifiedDateTime : Edm.DateTimeOffset "Last Modified On"
PX.Objects.CR.CRUnsubscribedPreferences.tstamp : Edm.Binary
PX.Objects.CR.CRUnsubscribedPreferences.UsersByCreatedByID -> PX.SM.Users (CreatedByID=PKID)
PX.Objects.CR.CRUnsubscribedPreferences.UsersByLastModifiedByID -> PX.SM.Users (LastModifiedByID=PKID)
PX.Objects.CR.CRUnsubscribedPreferences.CRMarketingCategoryByMarketingCategoryID -> PX.Objects.CR.CRMarketingCategory (MarketingCategoryID=MarketingCategoryID)
