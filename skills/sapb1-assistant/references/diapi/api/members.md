<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# DI API members (flat index)

17798 members. One line each: `Class.Property : VBType [R/W]`, `Class.Method(params) -> VBType`, `Class.Sub(params)`. VB types map to C# per di-api-guide.md § 9 (Long -> int). Grep the class name followed by a dot for a class (for example `^Documents[.]`), a dot plus the member name for a member everywhere (`[.]CardCode `). Full description, remarks and samples: the class entry located through INDEX.md.

AccountCategoriesParams.Count : Long [R]
AccountCategoriesParams.Add() -> AccountCategoryParams
AccountCategoriesParams.GetXMLSchema() -> String
AccountCategoriesParams.Item(ByVal vtIndex As Variant) -> AccountCategoryParams
AccountCategoriesParams.ToXMLFile(ByVal bstrFileName As String)
AccountCategoriesParams.ToXMLString() -> String
AccountCategory.CategoryCode : Long [R]
AccountCategory.CategoryName : String [R/W]
AccountCategory.CategorySource : AccountCategorySourceEnum [R/W]
AccountCategory.FromXMLFile(ByVal bstrFileName As String)
AccountCategory.FromXMLString(ByVal bstrXML As String)
AccountCategory.GetXMLSchema() -> String
AccountCategory.ToXMLFile(ByVal bstrFileName As String)
AccountCategory.ToXMLString() -> String
AccountCategoryParams.CategoryCode : Long [R/W]
AccountCategoryParams.CategoryName : String [R]
AccountCategoryParams.FromXMLFile(ByVal bstrFileName As String)
AccountCategoryParams.FromXMLString(ByVal bstrXML As String)
AccountCategoryParams.GetXMLSchema() -> String
AccountCategoryParams.ToXMLFile(ByVal bstrFileName As String)
AccountCategoryParams.ToXMLString() -> String
AccountCategoryService.AddCategory(ByVal pIAccountCategory As AccountCategory) -> AccountCategoryParams
AccountCategoryService.DeleteCategory(ByVal pIAccountCategoryParams As AccountCategoryParams)
AccountCategoryService.GetCategory(ByVal pIAccountCategoryParams As AccountCategoryParams) -> AccountCategory
AccountCategoryService.GetCategoryList() -> AccountCategoriesParams
AccountCategoryService.GetDataInterface(ByVal enumMSDI As AccountCategoryServiceDataInterfaces) -> Object
AccountCategoryService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AccountCategoryService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AccountCategoryService.UpdateCategory(ByVal pIAccountCategory As AccountCategory)
AccountSegmentationCategories.Browser : DataBrowser [R]
AccountSegmentationCategories.Code : String [R/W]
AccountSegmentationCategories.Name : String [R/W]
AccountSegmentationCategories.SegmentID : Long [R/W]
AccountSegmentationCategories.ShortName : String [R/W]
AccountSegmentationCategories.UserFields : UserFields [R]
AccountSegmentationCategories.Add() -> Long
AccountSegmentationCategories.GetAsXML() -> String
AccountSegmentationCategories.GetByKey(ByVal lSegmentId As Long, ByVal bstrCode As String) -> Boolean
AccountSegmentationCategories.Remove() -> Long
AccountSegmentationCategories.SaveToFile(ByVal bstrFileName As String)
AccountSegmentationCategories.SaveXML(ByRef pbstrFileName As String)
AccountSegmentationCategories.Update() -> Long
AccountSegmentations.Browser : DataBrowser [R]
AccountSegmentations.Categories : AcctSegmnt_Categories [R]
AccountSegmentations.Name : String [R/W]
AccountSegmentations.Numerator : Long [R]
AccountSegmentations.Size : Long [R/W]
AccountSegmentations.Type : AccountSegmentationTypeEnum [R/W]
AccountSegmentations.UserFields : UserFields [R]
AccountSegmentations.Add() -> Long
AccountSegmentations.GetAsXML() -> String
AccountSegmentations.GetByKey(ByVal lAbsID As Long) -> Boolean
AccountSegmentations.Remove() -> Long
AccountSegmentations.SaveToFile(ByVal bstrFileName As String)
AccountSegmentations.SaveXML(ByRef pbstrFileName As String)
AccountSegmentations.Update() -> Long
AccountsService.CreateOpenBalance(ByVal pIOpenningBalanceAccount As OpenningBalanceAccount, ByVal pGLAccounts As GLAccounts)
AccountsService.GetDataInterface(ByVal enumMSDI As AccountsServiceDataInterfaces) -> Object
AccountsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AccountsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AccrualType.CalculationAccount : String [R/W]
AccrualType.Code : String [R/W]
AccrualType.InterimAccount : String [R/W]
AccrualType.Name : String [R/W]
AccrualType.PostingAccount : String [R/W]
AccrualType.UserFields : Fields [R]
AccrualType.FromXMLFile(ByVal bstrFileName As String)
AccrualType.FromXMLString(ByVal bstrXML As String)
AccrualType.GetXMLSchema() -> String
AccrualType.ToXMLFile(ByVal bstrFileName As String)
AccrualType.ToXMLString() -> String
AccrualTypeParams.Code : String [R/W]
AccrualTypeParams.FromXMLFile(ByVal bstrFileName As String)
AccrualTypeParams.FromXMLString(ByVal bstrXML As String)
AccrualTypeParams.GetXMLSchema() -> String
AccrualTypeParams.ToXMLFile(ByVal bstrFileName As String)
AccrualTypeParams.ToXMLString() -> String
AccrualTypes.Count : Long [R]
AccrualTypes.Add() -> AccrualType
AccrualTypes.GetXMLSchema() -> String
AccrualTypes.Item(ByVal vtIndex As Variant) -> AccrualType
AccrualTypes.ToXMLFile(ByVal bstrFileName As String)
AccrualTypes.ToXMLString() -> String
AccrualTypesParams.Count : Long [R]
AccrualTypesParams.Add() -> AccrualTypeParams
AccrualTypesParams.GetXMLSchema() -> String
AccrualTypesParams.Item(ByVal vtIndex As Variant) -> AccrualTypeParams
AccrualTypesParams.ToXMLFile(ByVal bstrFileName As String)
AccrualTypesParams.ToXMLString() -> String
AccrualTypesService.AddAccrualType(ByVal pIAccrualType As AccrualType) -> AccrualTypeParams
AccrualTypesService.DeleteAccrualType(ByVal pIAccrualTypeParams As AccrualTypeParams)
AccrualTypesService.GetAccrualType(ByVal pIAccrualTypeParams As AccrualTypeParams) -> AccrualType
AccrualTypesService.GetAccrualTypeList() -> AccrualTypesParams
AccrualTypesService.GetDataInterface(ByVal enumMSDI As AccrualTypesServiceDataInterfaces) -> Object
AccrualTypesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AccrualTypesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AccrualTypesService.UpdateAccrualType(ByVal pIAccrualType As AccrualType)
AcctSegmnt_Categories.Code : String [R/W]
AcctSegmnt_Categories.Name : String [R/W]
AcctSegmnt_Categories.SegmentID : Long [R/W]
AcctSegmnt_Categories.ShortName : String [R/W]
AcctSegmnt_Categories.Add()
AcctSegmnt_Categories.SetCurrentLine(ByVal LineNum As Long)
ActivitiesParams.Count : Long [R]
ActivitiesParams.Add() -> ActivityParams
ActivitiesParams.GetXMLSchema() -> String
ActivitiesParams.Item(ByVal vtIndex As Variant) -> ActivityParams
ActivitiesParams.ToXMLFile(ByVal bstrFileName As String)
ActivitiesParams.ToXMLString() -> String
ActivitiesService.AddActivity(ByVal pIActivity As Activity) -> ActivityParams
ActivitiesService.DeleteActivity(ByVal pIActivityParams As ActivityParams)
ActivitiesService.DeleteSingleInstanceFromSeries(ByVal pIActivityInstanceParams As ActivityInstanceParams)
ActivitiesService.GetActivity(ByVal pIActivityParams As ActivityParams) -> Activity
ActivitiesService.GetActivityList() -> ActivitiesParams
ActivitiesService.GetDataInterface(ByVal enumMSDI As ActivitiesServiceDataInterfaces) -> Object
ActivitiesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ActivitiesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ActivitiesService.GetListByAttendUser(ByVal pIActivity As Activity) -> ActivitiesParams
ActivitiesService.GetSingleInstanceFromSeries(ByVal pIActivityInstanceParams As ActivityInstanceParams) -> Activity
ActivitiesService.GetTopNActivityInstances(ByVal pActivityInstancesListParams As ActivityInstancesListParams) -> ActivityInstancesParams
ActivitiesService.UpdateActivity(ByVal pIActivity As Activity)
ActivitiesService.UpdateSingleInstanceInSeries(ByVal pIActivity As Activity) -> ActivityParams
Activity.Activity : BoActivities [R/W]
Activity.ActivityCheckIns : ActivityCheckInCollection [R]
Activity.ActivityCode : Long [R]
Activity.ActivityDate : Date [R/W]
Activity.ActivityRecipients : ActivityMultipleRecipientCollection [R]
Activity.ActivityTime : Date [R/W]
Activity.ActivityType : Long [R/W]
Activity.AddressName : String [R/W]
Activity.AddressType : BoAddressType [R/W]
Activity.AttachmentEntry : Long [R/W]
Activity.BelongedSeriesNum : Long [R]
Activity.CardCode : String [R/W]
Activity.City : String [R/W]
Activity.Closed : BoYesNoEnum [R/W]
Activity.CloseDate : Date [R/W]
Activity.ContactPersonCode : Long [R/W]
Activity.Country : String [R/W]
Activity.Details : String [R/W]
Activity.DocEntry : String [R/W]
Activity.DocNum : String [R]
Activity.DocType : String [R/W]
Activity.DocTypeEx : String [R/W]
Activity.Duration : Double [R/W]
Activity.DurationType : BoDurations [R/W]
Activity.EndDuedate : Date [R/W]
Activity.EndTime : Date [R/W]
Activity.endType : EndTypeEnum [R/W]
Activity.Fax : String [R/W]
Activity.Friday : BoYesNoEnum [R/W]
Activity.HandledBy : Long [R/W]
Activity.HandledByEmployee : Long [R/W]
Activity.HandledByRecipientList : Long [R/W]
Activity.Inactiveflag : BoYesNoEnum [R/W]
Activity.Interval : Long [R/W]
Activity.IsRemoved : BoYesNoEnum [R]
Activity.Location : Long [R/W]
Activity.MaxOccurrence : Long [R/W]
Activity.Monday : BoYesNoEnum [R/W]
Activity.Notes : String [R/W]
Activity.Office365EventId : String [R/W]
Activity.ParentobjectId : Long [R]
Activity.Parentobjecttype : String [R]
Activity.Personalflag : BoYesNoEnum [R/W]
Activity.Phone : String [R/W]
Activity.PreviousActivity : Long [R/W]
Activity.Priority : BoMsgPriorities [R/W]
Activity.RecurrenceDayInMonth : Long [R/W]
Activity.RecurrenceDayOfWeek : RecurrenceDayOfWeekEnum [R/W]
Activity.RecurrenceMonth : Long [R/W]
Activity.RecurrencePattern : RecurrencePatternEnum [R/W]
Activity.RecurrenceSequenceSpecifier : RecurrenceSequenceSpecifierEnum [R/W]
Activity.Reminder : BoYesNoEnum [R/W]
Activity.ReminderPeriod : Double [R/W]
Activity.ReminderType : BoDurations [R/W]
Activity.RepeatOption : RepeatOptionEnum [R/W]
Activity.Room : String [R/W]
Activity.SalesEmployee : Long [R/W]
Activity.SalesOpportunityId : Long [R/W]
Activity.SalesOpportunityLine : Long [R/W]
Activity.Saturday : BoYesNoEnum [R/W]
Activity.SeriesEndDate : Date [R/W]
Activity.SeriesStartDate : Date [R]
Activity.StartDate : Date [R/W]
Activity.StartTime : Date [R/W]
Activity.State : String [R/W]
Activity.Status : Long [R/W]
Activity.Street : String [R/W]
Activity.Subject : Long [R/W]
Activity.Sunday : BoYesNoEnum [R/W]
Activity.Tentativeflag : BoYesNoEnum [R/W]
Activity.Thursday : BoYesNoEnum [R/W]
Activity.Tuesday : BoYesNoEnum [R/W]
Activity.UserFields : Fields [R]
Activity.Wednesday : BoYesNoEnum [R/W]
Activity.FromXMLFile(ByVal bstrFileName As String)
Activity.FromXMLString(ByVal bstrXML As String)
Activity.GetXMLSchema() -> String
Activity.ToXMLFile(ByVal bstrFileName As String)
Activity.ToXMLString() -> String
ActivityCheckIn.Date : Date [R]
ActivityCheckIn.HandledBy : Long [R]
ActivityCheckIn.HandledByEmployee : Long [R]
ActivityCheckIn.Latitude : String [R/W]
ActivityCheckIn.LineNumber : Long [R]
ActivityCheckIn.Location : String [R/W]
ActivityCheckIn.Longitude : String [R/W]
ActivityCheckIn.Time : Date [R]
ActivityCheckIn.FromXMLFile(ByVal bstrFileName As String)
ActivityCheckIn.FromXMLString(ByVal bstrXML As String)
ActivityCheckIn.GetXMLSchema() -> String
ActivityCheckIn.ToXMLFile(ByVal bstrFileName As String)
ActivityCheckIn.ToXMLString() -> String
ActivityCheckInCollection.Count : Long [R]
ActivityCheckInCollection.Add() -> ActivityCheckIn
ActivityCheckInCollection.GetXMLSchema() -> String
ActivityCheckInCollection.Item(ByVal vtIndex As Variant) -> ActivityCheckIn
ActivityCheckInCollection.ToXMLFile(ByVal bstrFileName As String)
ActivityCheckInCollection.ToXMLString() -> String
ActivityInstanceParams.ActivityCode : Long [R/W]
ActivityInstanceParams.InstanceDate : Date [R/W]
ActivityInstanceParams.FromXMLFile(ByVal bstrFileName As String)
ActivityInstanceParams.FromXMLString(ByVal bstrXML As String)
ActivityInstanceParams.GetXMLSchema() -> String
ActivityInstanceParams.ToXMLFile(ByVal bstrFileName As String)
ActivityInstanceParams.ToXMLString() -> String
ActivityInstancesListParams.InstanceCount : Long [R/W]
ActivityInstancesListParams.StartDate : Date [R/W]
ActivityInstancesListParams.FromXMLFile(ByVal bstrFileName As String)
ActivityInstancesListParams.FromXMLString(ByVal bstrXML As String)
ActivityInstancesListParams.GetXMLSchema() -> String
ActivityInstancesListParams.ToXMLFile(ByVal bstrFileName As String)
ActivityInstancesListParams.ToXMLString() -> String
ActivityInstancesParams.Count : Long [R]
ActivityInstancesParams.Add() -> ActivityInstanceParams
ActivityInstancesParams.GetXMLSchema() -> String
ActivityInstancesParams.Item(ByVal vtIndex As Variant) -> ActivityInstanceParams
ActivityInstancesParams.ToXMLFile(ByVal bstrFileName As String)
ActivityInstancesParams.ToXMLString() -> String
ActivityLocations.Browser : DataBrowser [R]
ActivityLocations.Code : Long [R]
ActivityLocations.Name : String [R/W]
ActivityLocations.UserFields : UserFields [R]
ActivityLocations.Add() -> Long
ActivityLocations.GetAsXML() -> String
ActivityLocations.GetByKey(ByVal lID As Long) -> Boolean
ActivityLocations.SaveToFile(ByVal FileName As String)
ActivityLocations.SaveXML(ByRef FileName As String)
ActivityLocations.Update() -> Long
ActivityMultipleRecipient.LineNumber : Long [R]
ActivityMultipleRecipient.RecipientCode : String [R/W]
ActivityMultipleRecipient.RecipientType : ActivityRecipientObjTypeEnum [R/W]
ActivityMultipleRecipient.FromXMLFile(ByVal bstrFileName As String)
ActivityMultipleRecipient.FromXMLString(ByVal bstrXML As String)
ActivityMultipleRecipient.GetXMLSchema() -> String
ActivityMultipleRecipient.ToXMLFile(ByVal bstrFileName As String)
ActivityMultipleRecipient.ToXMLString() -> String
ActivityMultipleRecipientCollection.Count : Long [R]
ActivityMultipleRecipientCollection.Add() -> ActivityMultipleRecipient
ActivityMultipleRecipientCollection.GetXMLSchema() -> String
ActivityMultipleRecipientCollection.Item(ByVal vtIndex As Variant) -> ActivityMultipleRecipient
ActivityMultipleRecipientCollection.Remove(ByVal vtIndex As Variant)
ActivityMultipleRecipientCollection.ToXMLFile(ByVal bstrFileName As String)
ActivityMultipleRecipientCollection.ToXMLString() -> String
ActivityParams.Activity : BoActivities [R]
ActivityParams.ActivityCode : Long [R/W]
ActivityParams.CardCode : String [R]
ActivityParams.City : String [R]
ActivityParams.Closed : BoYesNoEnum [R]
ActivityParams.Country : String [R]
ActivityParams.Details : String [R]
ActivityParams.DocEntry : String [R]
ActivityParams.DocNum : String [R]
ActivityParams.DocType : String [R]
ActivityParams.EndDuedate : Date [R]
ActivityParams.EndTime : Date [R]
ActivityParams.HandledBy : Long [R]
ActivityParams.Inactiveflag : BoYesNoEnum [R]
ActivityParams.Notes : String [R]
ActivityParams.Priority : BoMsgPriorities [R]
ActivityParams.Room : String [R]
ActivityParams.SalesOpportunityId : Long [R]
ActivityParams.SalesOpportunityLine : Long [R]
ActivityParams.StartDate : Date [R]
ActivityParams.StartTime : Date [R]
ActivityParams.State : String [R]
ActivityParams.Street : String [R]
ActivityParams.Tentativeflag : BoYesNoEnum [R]
ActivityParams.FromXMLFile(ByVal bstrFileName As String)
ActivityParams.FromXMLString(ByVal bstrXML As String)
ActivityParams.GetXMLSchema() -> String
ActivityParams.ToXMLFile(ByVal bstrFileName As String)
ActivityParams.ToXMLString() -> String
ActivityRecipient.LineNumber : Long [R]
ActivityRecipient.RecipientCode : String [R/W]
ActivityRecipient.RecipientType : RecipientTypeEnum [R/W]
ActivityRecipient.FromXMLFile(ByVal bstrFileName As String)
ActivityRecipient.FromXMLString(ByVal bstrXML As String)
ActivityRecipient.GetXMLSchema() -> String
ActivityRecipient.ToXMLFile(ByVal bstrFileName As String)
ActivityRecipient.ToXMLString() -> String
ActivityRecipientCollection.Count : Long [R]
ActivityRecipientCollection.Add() -> ActivityRecipient
ActivityRecipientCollection.GetXMLSchema() -> String
ActivityRecipientCollection.Item(ByVal vtIndex As Variant) -> ActivityRecipient
ActivityRecipientCollection.Remove(ByVal vtIndex As Variant)
ActivityRecipientCollection.ToXMLFile(ByVal bstrFileName As String)
ActivityRecipientCollection.ToXMLString() -> String
ActivityRecipientList.Active : BoYesNoEnum [R/W]
ActivityRecipientList.ActivityRecipientCollection : ActivityRecipientCollection [R]
ActivityRecipientList.Code : Long [R]
ActivityRecipientList.IsMultiple : BoYesNoEnum [R]
ActivityRecipientList.Name : String [R/W]
ActivityRecipientList.FromXMLFile(ByVal bstrFileName As String)
ActivityRecipientList.FromXMLString(ByVal bstrXML As String)
ActivityRecipientList.GetXMLSchema() -> String
ActivityRecipientList.ToXMLFile(ByVal bstrFileName As String)
ActivityRecipientList.ToXMLString() -> String
ActivityRecipientListParams.Active : BoYesNoEnum [R]
ActivityRecipientListParams.Code : Long [R/W]
ActivityRecipientListParams.IsMultiple : BoYesNoEnum [R]
ActivityRecipientListParams.Name : String [R]
ActivityRecipientListParams.FromXMLFile(ByVal bstrFileName As String)
ActivityRecipientListParams.FromXMLString(ByVal bstrXML As String)
ActivityRecipientListParams.GetXMLSchema() -> String
ActivityRecipientListParams.ToXMLFile(ByVal bstrFileName As String)
ActivityRecipientListParams.ToXMLString() -> String
ActivityRecipientListParamsCollection.Count : Long [R]
ActivityRecipientListParamsCollection.Add() -> ActivityRecipientListParams
ActivityRecipientListParamsCollection.GetXMLSchema() -> String
ActivityRecipientListParamsCollection.Item(ByVal vtIndex As Variant) -> ActivityRecipientListParams
ActivityRecipientListParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ActivityRecipientListParamsCollection.ToXMLString() -> String
ActivityRecipientListsService.Add(ByVal pIActivityRecipientList As ActivityRecipientList) -> ActivityRecipientListParams
ActivityRecipientListsService.Delete(ByVal pIActivityRecipientListParams As ActivityRecipientListParams)
ActivityRecipientListsService.Get(ByVal pIActivityRecipientListParams As ActivityRecipientListParams) -> ActivityRecipientList
ActivityRecipientListsService.GetDataInterface(ByVal enumMSDI As ActivityRecipientListsServiceDataInterfaces) -> Object
ActivityRecipientListsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ActivityRecipientListsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ActivityRecipientListsService.GetList() -> ActivityRecipientListParamsCollection
ActivityRecipientListsService.Update(ByVal pIActivityRecipientList As ActivityRecipientList)
ActivityStatus.Browser : DataBrowser [R]
ActivityStatus.StatusDescription : String [R/W]
ActivityStatus.StatusId : Long [R]
ActivityStatus.StatusName : String [R/W]
ActivityStatus.UserFields : UserFields [R]
ActivityStatus.Add() -> Long
ActivityStatus.GetAsXML() -> String
ActivityStatus.GetByKey(ByVal ActivityID As Long) -> Boolean
ActivityStatus.SaveToFile(ByVal FileName As String)
ActivityStatus.SaveXML(ByRef FileName As String)
ActivityStatus.Update() -> Long
ActivitySubject.ActivityType : Long [R/W]
ActivitySubject.Code : Long [R]
ActivitySubject.Description : String [R/W]
ActivitySubject.IsActive : BoYesNoEnum [R/W]
ActivitySubject.FromXMLFile(ByVal bstrFileName As String)
ActivitySubject.FromXMLString(ByVal bstrXML As String)
ActivitySubject.GetXMLSchema() -> String
ActivitySubject.ToXMLFile(ByVal bstrFileName As String)
ActivitySubject.ToXMLString() -> String
ActivitySubjectParams.Code : Long [R/W]
ActivitySubjectParams.Description : String [R]
ActivitySubjectParams.FromXMLFile(ByVal bstrFileName As String)
ActivitySubjectParams.FromXMLString(ByVal bstrXML As String)
ActivitySubjectParams.GetXMLSchema() -> String
ActivitySubjectParams.ToXMLFile(ByVal bstrFileName As String)
ActivitySubjectParams.ToXMLString() -> String
ActivitySubjectService.AddActivitySubject(ByVal pIActivitySubject As ActivitySubject) -> ActivitySubjectParams
ActivitySubjectService.GetActivitySubject(ByVal pIActivitySubjectParams As ActivitySubjectParams) -> ActivitySubject
ActivitySubjectService.GetActivitySubjectList() -> ActivitySubjectsParams
ActivitySubjectService.GetDataInterface(ByVal enumMSDI As ActivitySubjectServiceDataInterfaces) -> Object
ActivitySubjectService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ActivitySubjectService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ActivitySubjectService.GetListByTypeCode(ByVal pIActivitySubject As ActivitySubject) -> ActivitySubjectsParams
ActivitySubjectService.UpdateActivitySubject(ByVal pIActivitySubject As ActivitySubject)
ActivitySubjectsParams.Count : Long [R]
ActivitySubjectsParams.Add() -> ActivitySubjectParams
ActivitySubjectsParams.GetXMLSchema() -> String
ActivitySubjectsParams.Item(ByVal vtIndex As Variant) -> ActivitySubjectParams
ActivitySubjectsParams.ToXMLFile(ByVal bstrFileName As String)
ActivitySubjectsParams.ToXMLString() -> String
ActivityTypes.Active : BoYesNoEnum [R/W]
ActivityTypes.Browser : DataBrowser [R]
ActivityTypes.Code : Long [R]
ActivityTypes.Name : String [R/W]
ActivityTypes.UserFields : UserFields [R]
ActivityTypes.Add() -> Long
ActivityTypes.GetAsXML() -> String
ActivityTypes.GetByKey(ByVal lID As Long) -> Boolean
ActivityTypes.SaveToFile(ByVal FileName As String)
ActivityTypes.SaveXML(ByRef FileName As String)
ActivityTypes.Update() -> Long
AdditionalExpenses.Browser : DataBrowser [R]
AdditionalExpenses.DistributionMethod : BoAeDistMthd [R/W]
AdditionalExpenses.DistributionRule : String [R/W]
AdditionalExpenses.DistributionRule2 : String [R/W]
AdditionalExpenses.DistributionRule3 : String [R/W]
AdditionalExpenses.DistributionRule4 : String [R/W]
AdditionalExpenses.DistributionRule5 : String [R/W]
AdditionalExpenses.DrawingMethod : DrawingMethodEnum [R/W]
AdditionalExpenses.ExpensCode : Long [R]
AdditionalExpenses.ExpenseAccount : String [R/W]
AdditionalExpenses.ExpenseExemptedAccount : String [R/W]
AdditionalExpenses.FixedAmountExpenses : Double [R/W]
AdditionalExpenses.FixedAmountRevenues : Double [R/W]
AdditionalExpenses.FreightOffsetAccount : String [R/W]
AdditionalExpenses.FreightType : FreightTypeEnum [R/W]
AdditionalExpenses.FreightTypeForBollo : FreightTypeForBolloEnum [R/W]
AdditionalExpenses.GrossFreight : BoYesNoEnum [R/W]
AdditionalExpenses.Includein1099 : BoYesNoEnum [R/W]
AdditionalExpenses.InputVATGroup : String [R/W]
AdditionalExpenses.LastPurchasePrice : BoYesNoEnum [R/W]
AdditionalExpenses.Name : String [R/W]
AdditionalExpenses.OutputVATGroup : String [R/W]
AdditionalExpenses.Project : String [R/W]
AdditionalExpenses.RevenuesAccount : String [R/W]
AdditionalExpenses.RevenuesExemptedAccount : String [R/W]
AdditionalExpenses.SACCode : String [R/W]
AdditionalExpenses.Stock : BoYesNoEnum [R/W]
AdditionalExpenses.TaxLiable : BoYesNoEnum [R/W]
AdditionalExpenses.UserFields : UserFields [R]
AdditionalExpenses.WTLiable : String [R]
AdditionalExpenses.Add() -> Long
AdditionalExpenses.Close() -> Long
AdditionalExpenses.GetAsXML() -> String
AdditionalExpenses.GetByKey(ByVal ExpnsCode As Long) -> Boolean
AdditionalExpenses.Remove() -> Long
AdditionalExpenses.SaveToFile(ByVal FileName As String)
AdditionalExpenses.SaveXML(ByRef FileName As String)
AdditionalExpenses.Update() -> Long
AddressExtension.BillToAddress2 : String [R/W]
AddressExtension.BillToAddress3 : String [R/W]
AddressExtension.BillToAddressType : String [R/W]
AddressExtension.BillToBlock : String [R/W]
AddressExtension.BillToBuilding : String [R/W]
AddressExtension.BillToCity : String [R/W]
AddressExtension.BillToCountry : String [R/W]
AddressExtension.BillToCounty : String [R/W]
AddressExtension.BillToGlobalLocationNumber : String [R/W]
AddressExtension.BillToState : String [R/W]
AddressExtension.BillToStreet : String [R/W]
AddressExtension.BillToStreetNo : String [R/W]
AddressExtension.BillToZipCode : String [R/W]
AddressExtension.DeliveryPlaceBlock : String [R/W]
AddressExtension.DeliveryPlaceBP : String [R/W]
AddressExtension.DeliveryPlaceBuilding : String [R/W]
AddressExtension.DeliveryPlaceCity : String [R/W]
AddressExtension.DeliveryPlaceCNPJ : String [R/W]
AddressExtension.DeliveryPlaceCountry : String [R/W]
AddressExtension.DeliveryPlaceCounty : String [R/W]
AddressExtension.DeliveryPlaceCPF : String [R/W]
AddressExtension.DeliveryPlaceDepartureDate : String [R/W]
AddressExtension.DeliveryPlaceEMail : String [R/W]
AddressExtension.DeliveryPlacePhone : String [R/W]
AddressExtension.DeliveryPlaceState : String [R/W]
AddressExtension.DeliveryPlaceStreet : String [R/W]
AddressExtension.DeliveryPlaceStreetNo : String [R/W]
AddressExtension.DeliveryPlaceZip : String [R/W]
AddressExtension.DocEntry : Long [R]
AddressExtension.GoodsIssuePlaceBlock : String [R/W]
AddressExtension.GoodsIssuePlaceBP : String [R/W]
AddressExtension.GoodsIssuePlaceBuilding : String [R/W]
AddressExtension.GoodsIssuePlaceCity : String [R/W]
AddressExtension.GoodsIssuePlaceCNPJ : String [R/W]
AddressExtension.GoodsIssuePlaceCountry : String [R/W]
AddressExtension.GoodsIssuePlaceCounty : String [R/W]
AddressExtension.GoodsIssuePlaceCPF : String [R/W]
AddressExtension.GoodsIssuePlaceDepartureDate : String [R/W]
AddressExtension.GoodsIssuePlaceEMail : String [R/W]
AddressExtension.GoodsIssuePlacePhone : String [R/W]
AddressExtension.GoodsIssuePlaceState : String [R/W]
AddressExtension.GoodsIssuePlaceStreet : String [R/W]
AddressExtension.GoodsIssuePlaceStreetNo : String [R/W]
AddressExtension.GoodsIssuePlaceZip : String [R/W]
AddressExtension.PlaceOfSupply : String [R/W]
AddressExtension.PurchasePlaceOfSupply : String [R/W]
AddressExtension.ShipToAddress2 : String [R/W]
AddressExtension.ShipToAddress3 : String [R/W]
AddressExtension.ShipToAddressType : String [R/W]
AddressExtension.ShipToBlock : String [R/W]
AddressExtension.ShipToBuilding : String [R/W]
AddressExtension.ShipToCity : String [R/W]
AddressExtension.ShipToCountry : String [R/W]
AddressExtension.ShipToCounty : String [R/W]
AddressExtension.ShipToGlobalLocationNumber : String [R/W]
AddressExtension.ShipToState : String [R/W]
AddressExtension.ShipToStreet : String [R/W]
AddressExtension.ShipToStreetNo : String [R/W]
AddressExtension.ShipToZipCode : String [R/W]
AddressExtension.UserFields : UserFields [R]
AddressFormat.Code : Long [R]
AddressFormat.Format : String [R/W]
AddressFormat.Name : String [R/W]
AddressFormat.FromXMLFile(ByVal bstrFileName As String)
AddressFormat.FromXMLString(ByVal bstrXML As String)
AddressFormat.GetXMLSchema() -> String
AddressFormat.ToXMLFile(ByVal bstrFileName As String)
AddressFormat.ToXMLString() -> String
AddressFormatParams.Code : Long [R/W]
AddressFormatParams.Name : String [R]
AddressFormatParams.FromXMLFile(ByVal bstrFileName As String)
AddressFormatParams.FromXMLString(ByVal bstrXML As String)
AddressFormatParams.GetXMLSchema() -> String
AddressFormatParams.ToXMLFile(ByVal bstrFileName As String)
AddressFormatParams.ToXMLString() -> String
AddressFormatParamsCollection.Count : Long [R]
AddressFormatParamsCollection.Add() -> AddressFormatParams
AddressFormatParamsCollection.GetXMLSchema() -> String
AddressFormatParamsCollection.Item(ByVal vtIndex As Variant) -> AddressFormatParams
AddressFormatParamsCollection.ToXMLFile(ByVal bstrFileName As String)
AddressFormatParamsCollection.ToXMLString() -> String
AddressParams.Address2 : String [R/W]
AddressParams.Address3 : String [R/W]
AddressParams.AddressType : String [R/W]
AddressParams.Block : String [R/W]
AddressParams.Building : String [R/W]
AddressParams.City : String [R/W]
AddressParams.Country : String [R/W]
AddressParams.County : String [R/W]
AddressParams.GlobalLocationNumber : String [R/W]
AddressParams.State : String [R/W]
AddressParams.Street : String [R/W]
AddressParams.StreetNo : String [R/W]
AddressParams.UserFields : Fields [R]
AddressParams.ZipCode : String [R/W]
AddressParams.FromXMLFile(ByVal bstrFileName As String)
AddressParams.FromXMLString(ByVal bstrXML As String)
AddressParams.GetXMLSchema() -> String
AddressParams.ToXMLFile(ByVal bstrFileName As String)
AddressParams.ToXMLString() -> String
AddressReturnParams.FullAddress : String [R]
AddressReturnParams.FromXMLFile(ByVal bstrFileName As String)
AddressReturnParams.FromXMLString(ByVal bstrXML As String)
AddressReturnParams.GetXMLSchema() -> String
AddressReturnParams.ToXMLFile(ByVal bstrFileName As String)
AddressReturnParams.ToXMLString() -> String
AddressService.GetAddressFormat(ByVal pIAddressFormatParams As AddressFormatParams) -> AddressFormat
AddressService.GetDataInterface(ByVal enumMSDI As AddressServiceDataInterfaces) -> Object
AddressService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AddressService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AddressService.GetFullAddress(ByVal pIAddressParams As AddressParams) -> AddressReturnParams
AdminInfo.Account : String [R/W]
AdminInfo.AccountSegmentsSeparator : String [R/W]
AdminInfo.AccuracyofQuantities : Long [R/W]
AdminInfo.ActionWhenDeviateFromBAForAccounting : BADivationAlertLevelEnum [R/W]
AdminInfo.ActionWhenDeviateFromBAForGRPO : BADivationAlertLevelEnum [R/W]
AdminInfo.ActionWhenDeviateFromBAForPO : BADivationAlertLevelEnum [R/W]
AdminInfo.AdditionalIdNumber : String [R/W]
AdminInfo.Address : String [R]
AdminInfo.AddressinForeignLanguage : String [R/W]
AdminInfo.AdressFromWH : BoYesNoEnum [R/W]
AdminInfo.AdvancesonCorpIncomeTax : Double [R/W]
AdminInfo.AlertbyWarehouse : BoYesNoEnum [R/W]
AdminInfo.AlertTypeforWHStock : BoAlertTypeforWHStockEnum [R/W]
AdminInfo.AliasName : String [R/W]
AdminInfo.AllowBPWithNoOwner : BoYesNoEnum [R/W]
AdminInfo.AllowClosedSalesQuotations : BoYesNoEnum [R/W]
AdminInfo.AllowFuturePostingDate : BoYesNoEnum [R/W]
AdminInfo.AllowInBoundPostingWithZeroPrice : BoYesNoEnum [R/W]
AdminInfo.AllowMultipleBAOnSamePeriod : BoYesNoEnum [R/W]
AdminInfo.AltNameForApInvoice : String [R/W]
AdminInfo.AltNameforCreditMemo : String [R/W]
AdminInfo.AltNameForGoodsReceipt : String [R/W]
AdminInfo.AltNameForGoodsReturn : String [R/W]
AdminInfo.AltNameForPurchase : String [R/W]
AdminInfo.ApplicationOfIFRS : BoYesNoEnum [R/W]
AdminInfo.ApplyBaseInactiveStatusToPeriodVolumeDiscounts : BoYesNoEnum [R/W]
AdminInfo.ApplyBaseInactiveStatusToPriceLists : BoYesNoEnum [R/W]
AdminInfo.ApplyBaseInactiveStatusToSpecialPrices : BoYesNoEnum [R/W]
AdminInfo.AutoAddPackage : BoYesNoEnum [R/W]
AdminInfo.AutoAddUoM : BoYesNoEnum [R/W]
AdminInfo.AutoAssignOnlyValidAPBA : BoYesNoEnum [R/W]
AdminInfo.AutoAssignOnlyValidARBA : BoYesNoEnum [R/W]
AdminInfo.BankCountry : String [R/W]
AdminInfo.BankStatementInstalled : BoYesNoEnum [R]
AdminInfo.BaseField : BoYesNoEnum [R/W]
AdminInfo.BlockBookkeeping : BoYesNoEnum [R/W]
AdminInfo.BlockBudget : BoBlockBudget [R/W]
AdminInfo.BlockDelNotesforPurchase : BoYesNoEnum [R/W]
AdminInfo.BlockMultipleBAOnSameAPDocument : BoYesNoEnum [R/W]
AdminInfo.BlockMultipleBAOnSameARDocument : BoYesNoEnum [R/W]
AdminInfo.BlockPostingDateEditing : BoYesNoEnum [R/W]
AdminInfo.BlockPurchaseOrders : BoYesNoEnum [R/W]
AdminInfo.BlockStockNegativeQuantity : BoYesNoEnum [R/W]
AdminInfo.BlockSystemCurrencyEditing : BoYesNoEnum [R/W]
AdminInfo.BlockTaxDate : BoYesNoEnum [R/W]
AdminInfo.BoletoFolderPath : String [R/W]
AdminInfo.BPTypeCode : String [R/W]
AdminInfo.BudgetAlert : BoBudgetAlert [R/W]
AdminInfo.CalculateBudget : BoYesNoEnum [R/W]
AdminInfo.CalculateGrossProfitperTra : BoYesNoEnum [R/W]
AdminInfo.CalculateInWhseQtyBasedOnPostingDate : BoYesNoEnum [R/W]
AdminInfo.CalculateRowDiscount : BoYesNoEnum [R/W]
AdminInfo.CalculateTaxinSalesQuotati : BoYesNoEnum [R/W]
AdminInfo.CertificateNo : String [R/W]
AdminInfo.ChangeDefReconAPAccounts : BoYesNoEnum [R/W]
AdminInfo.ChangeDefReconARAccounts : BoYesNoEnum [R/W]
AdminInfo.ChangedExistingOrders : BoYesNoEnum [R/W]
AdminInfo.ChartofAccountsTemplate : String [R/W]
AdminInfo.CloseCountedRowsWithoutConfirmation : BoYesNoEnum [R/W]
AdminInfo.CloseCountedRowsWithZeroDifference : BoYesNoEnum [R/W]
AdminInfo.Code : Long [R]
AdminInfo.CommitmentRestriction : BoYesNoEnum [R/W]
AdminInfo.CompanyColor : Long [R/W]
AdminInfo.CompanyName : String [R/W]
AdminInfo.ConsiderDelNotesinSalesR : BoYesNoEnum [R/W]
AdminInfo.ConsumeForecast : BoYesNoEnum [R/W]
AdminInfo.ConsumptionMethod : BoConsumptionMethod [R/W]
AdminInfo.ContinuousStockManagement : BoYesNoEnum [R/W]
AdminInfo.ContinuousStockSystem : BoInventorySystem [R/W]
AdminInfo.CopyAttachmentsFromBaseToTarget : BoYesNoEnum [R/W]
AdminInfo.CopyAttachmentsFromBOM : BoYesNoEnum [R/W]
AdminInfo.CopyExchangeRateInCopyTo : BoYesNoEnum [R/W]
AdminInfo.CopyOpenRowsToDelivery : BoYesNoEnum [R/W]
AdminInfo.CopySingleCounterToIndividualCounter : BoYesNoEnum [R/W]
AdminInfo.Country : String [R/W]
AdminInfo.CreateAutoVATLineinJDT : BoYesNoEnum [R/W]
AdminInfo.CreateOnlineQuotation : BoYesNoEnum [R/W]
AdminInfo.CreditBalancewithMinusSign : BoYesNoEnum [R/W]
AdminInfo.CreditDepositType : BoYesNoEnum [R/W]
AdminInfo.CreditRestriction : BoYesNoEnum [R/W]
AdminInfo.CustomerIdNumber : String [R/W]
AdminInfo.CustomersDeductionatSource : BoYesNoEnum [R/W]
AdminInfo.DataOwnershipManageBy : BoDataOwnershipManageMethodEnum [R/W]
AdminInfo.DateSeparator : String [R/W]
AdminInfo.DateTemplate : BoDateTemplate [R/W]
AdminInfo.DaysBackward : Long [R/W]
AdminInfo.DaysForward : Long [R/W]
AdminInfo.DecimalSeparator : String [R/W]
AdminInfo.DeductionFileNo : String [R/W]
AdminInfo.DefaultAccountCurrency : BoYesNoEnum [R/W]
AdminInfo.DefaultBankAccount : String [R/W]
AdminInfo.DefaultBankAccountKey : Long [R/W]
AdminInfo.DefaultBankNo : String [R/W]
AdminInfo.DefaultBranch : String [R]
AdminInfo.DefaultBudgetCostAssessMt : Long [R/W]
AdminInfo.DefaultCustomerPaymentTerms : Long [R/W]
AdminInfo.DefaultCustomerPriceList : Long [R/W]
AdminInfo.DefaultDunningTerm : String [R/W]
AdminInfo.DefaultforBatchStatus : BoDefaultBatchStatus [R/W]
AdminInfo.DefaultTaxCode : String [R/W]
AdminInfo.DefaultVendorPaymentTerms : Long [R/W]
AdminInfo.DefaultVendorPriceList : Long [R/W]
AdminInfo.DefaultWarehouse : String [R/W]
AdminInfo.DeferredTax : BoYesNoEnum [R/W]
AdminInfo.DeferredTaxforVendors : BoYesNoEnum [R/W]
AdminInfo.DirectIndirectRate : BoYesNoEnum [R/W]
AdminInfo.DisplayBatchQtyUoMBy : DisplayBatchQtyUoMByEnum [R/W]
AdminInfo.DisplayBookkeepingWindow : BoYesNoEnum [R/W]
AdminInfo.DisplayCancelDocInReport : BoYesNoEnum [R/W]
AdminInfo.DisplayCurrencyontheRight : BoYesNoEnum [R/W]
AdminInfo.DisplayInactivePriceListInDocuments : BoYesNoEnum [R/W]
AdminInfo.DisplayInactivePriceListInReports : BoYesNoEnum [R/W]
AdminInfo.DisplayInactivePriceListInSettings : BoYesNoEnum [R/W]
AdminInfo.DisplayPriceforPriceOnly : BoYesNoEnum [R/W]
AdminInfo.DisplayRoundingRemark : BoYesNoEnum [R/W]
AdminInfo.DocConfirmation : BoYesNoEnum [R/W]
AdminInfo.DontOverwriteAtcWithSameName : BoYesNoEnum [R/W]
AdminInfo.ElectronicReportInfo : ElectronicReportInfo [R]
AdminInfo.eMail : String [R/W]
AdminInfo.EmployerReference : String [R/W]
AdminInfo.EnableAdvancedGLAccountDetermination : BoYesNoEnum [R]
AdminInfo.EnableApprovalProcedureInDI : BoYesNoEnum [R/W]
AdminInfo.EnableAuthorizerUpdatePendingDraft : BoYesNoEnum [R/W]
AdminInfo.EnableBranches : BoYesNoEnum [R/W]
AdminInfo.EnableCentralizedIncomingPayments : BoYesNoEnum [R/W]
AdminInfo.EnableCentralizedOutgoingPayments : BoYesNoEnum [R/W]
AdminInfo.EnableExternalTax : BoYesNoEnum [R/W]
AdminInfo.EnableMultipleSchedulings : BoYesNoEnum [R/W]
AdminInfo.EnablePaymentDueDates : BoYesNoEnum [R/W]
AdminInfo.EnableSeparatePriceMode : BoYesNoEnum [R/W]
AdminInfo.EnableUpdateBAPriceAndPlannedAmount : BoYesNoEnum [R/W]
AdminInfo.EnableUpdateDocAfterApproval : BoYesNoEnum [R/W]
AdminInfo.EnableUpdateDraftDuringApproval : BoYesNoEnum [R/W]
AdminInfo.EORINumber : String [R/W]
AdminInfo.ExcelFolderPath : String [R/W]
AdminInfo.ExpirationDate : Date [R/W]
AdminInfo.ExtendedAdminInfo : ExtendedAdminInfo [R]
AdminInfo.FaxNumber : String [R/W]
AdminInfo.FaxNumberForeignLang : String [R/W]
AdminInfo.FCCheckAccount : BoCurrencyCheck [R/W]
AdminInfo.FederalTaxID : String [R/W]
AdminInfo.FederalTaxID2 : String [R/W]
AdminInfo.FederalTaxID3 : String [R/W]
AdminInfo.FileNumberinIncomeTax : String [R/W]
AdminInfo.GeneralManager : String [R/W]
AdminInfo.GeneralManagerForeignLanguage : String [R/W]
AdminInfo.GLMethod : BoGLMethods [R/W]
AdminInfo.GrossProfitAfterSale : BoYesNoEnum [R/W]
AdminInfo.GrossProfitPercentForServiceDocuments : Double [R/W]
AdminInfo.GTSDefaultChecker : Long [R/W]
AdminInfo.GTSDefaultPayee : Long [R/W]
AdminInfo.GTSInboundFolder : String [R/W]
AdminInfo.GTSMaxAmount : Double [R/W]
AdminInfo.GTSOutboundFolder : String [R/W]
AdminInfo.GTSResponseToExceeding : GTSResponseToExceedingEnum [R/W]
AdminInfo.GTSSeparateCode : String [R/W]
AdminInfo.HolidaysName : String [R/W]
AdminInfo.IEMandatoryValidation : BoYesNoEnum [R/W]
AdminInfo.InstitutionCode : String [R/W]
AdminInfo.InventoryCountingHighlightCountersDifference : Double [R/W]
AdminInfo.InventoryCountingHighlightMaxVariance : Double [R/W]
AdminInfo.InventoryCountingHighlightVariance : Double [R/W]
AdminInfo.InventoryPostingHighlightVariance : Double [R/W]
AdminInfo.InventoryPostingReleaseOnlySerialAndBatch : BoYesNoEnum [R/W]
AdminInfo.IsPrinterConnected : BoYesNoEnum [R/W]
AdminInfo.ISRBillerID : String [R/W]
AdminInfo.IsRemoveUnpricedValue : BoYesNoEnum [R]
AdminInfo.ISRType : Long [R/W]
AdminInfo.IssuePrimarilyBy : IssuePrimarilyByEnum [R/W]
AdminInfo.LetterHeaderinForeignLangu : String [R/W]
AdminInfo.LocalCurrency : String [R/W]
AdminInfo.ManagingDirector : String [R/W]
AdminInfo.ManagingDirectorForeignLan : String [R/W]
AdminInfo.MaxDaysForCancel : Long [R/W]
AdminInfo.MaxHistory : Long [R/W]
AdminInfo.MaximumNumberOfDaysForDueDate : Long [R/W]
AdminInfo.MeasuringAccuracy : Long [R/W]
AdminInfo.MinimumAmountfor347Report : Double [R/W]
AdminInfo.MultiCurrencyCheck : BoCurrencyCheck [R/W]
AdminInfo.MultiLanguageSupportEnable : BoYesNoEnum [R/W]
AdminInfo.NationalInsuranceNo : String [R/W]
AdminInfo.NumberOfCharInMonth : Long [R/W]
AdminInfo.OrderBlock : String [R/W]
AdminInfo.OrderingParty : String [R/W]
AdminInfo.OrganizationNumber : String [R/W]
AdminInfo.ParamFolderPath : String [R/W]
AdminInfo.PBSGroupNumber : String [R/W]
AdminInfo.PBSNumber : String [R/W]
AdminInfo.PDefaultWTCode : String [R/W]
AdminInfo.PDfltITWT : String [R/W]
AdminInfo.PercentageAccuracy : Long [R/W]
AdminInfo.PeriodStatusAutoChange : BoYesNoEnum [R/W]
AdminInfo.PeriodStatusChangeDelay : Long [R/W]
AdminInfo.PhoneNumber1 : String [R/W]
AdminInfo.PhoneNumber1ForeignLang : String [R/W]
AdminInfo.PhoneNumber2 : String [R/W]
AdminInfo.PhoneNumber2ForeignLang : String [R/W]
AdminInfo.PickList : BoYesNoEnum [R/W]
AdminInfo.PriceAccuracy : Long [R/W]
AdminInfo.PriceListforCostPrice : Long [R/W]
AdminInfo.PriceProceedMethod : PriceProceedMethodEnum [R/W]
AdminInfo.PriceSystem : BoYesNoEnum [R/W]
AdminInfo.PrintingHeader : String [R/W]
AdminInfo.PurchaseApplyExhRatesLnWTax : BoYesNoEnum [R/W]
AdminInfo.PurchaseLnWTax : BoYesNoEnum [R/W]
AdminInfo.PurchaseOrderConfirmed : BoYesNoEnum [R/W]
AdminInfo.PurchasePostPaymentCategoryLnWTax : BoYesNoEnum [R/W]
AdminInfo.QueryAccuracy : Long [R/W]
AdminInfo.RateAccuracy : Long [R/W]
AdminInfo.RefreshInWhseQtyInDI : BoYesNoEnum [R/W]
AdminInfo.RemoveUpdatePricesBasedOnNonStandardPriceLists : BoYesNoEnum [R/W]
AdminInfo.ReportAccordingTo : Long [R/W]
AdminInfo.RestrictDelNotesPO : BoYesNoEnum [R/W]
AdminInfo.RestrictOrders : BoYesNoEnum [R/W]
AdminInfo.RestrictSales : BoYesNoEnum [R/W]
AdminInfo.ReuseDocumentNum : BoYesNoEnum [R/W]
AdminInfo.ReuseNotaFiscalNum : BoYesNoEnum [R/W]
AdminInfo.RoundingMethod : BoYesNoEnum [R/W]
AdminInfo.RoundTaxAmounts : BoYesNoEnum [R/W]
AdminInfo.SalesApplyExhRatesLnWTax : BoYesNoEnum [R/W]
AdminInfo.SalesLnWTax : BoYesNoEnum [R/W]
AdminInfo.SalesOrderConfirmed : BoYesNoEnum [R/W]
AdminInfo.SalesPostPaymentCategoryLnWTax : BoYesNoEnum [R/W]
AdminInfo.SDefaultWTCode : String [R/W]
AdminInfo.SDfltITWT : String [R/W]
AdminInfo.SEPACreditorID : String [R/W]
AdminInfo.Series : Long [R/W]
AdminInfo.ServiceCode : String [R/W]
AdminInfo.ServicePassword : String [R/W]
AdminInfo.SetCommissionbyCustomer : BoYesNoEnum [R/W]
AdminInfo.SetCommissionbyItem : BoYesNoEnum [R/W]
AdminInfo.SetCommissionbySE : BoYesNoEnum [R/W]
AdminInfo.SetItemsWarehouses : BoYesNoEnum [R/W]
AdminInfo.SetResourcesWarehouses : BoYesNoEnum [R/W]
AdminInfo.SHandleWT : BoYesNoEnum [R/W]
AdminInfo.SirenNo : String [R/W]
AdminInfo.SplitPO : BoYesNoEnum [R/W]
AdminInfo.StandardUnitofLength : Long [R/W]
AdminInfo.StartingInFiscalYear : Long [R/W]
AdminInfo.State : String [R/W]
AdminInfo.SystemCurrency : String [R/W]
AdminInfo.TaxCollection : BoYesNoEnum [R/W]
AdminInfo.TaxDefinition : BoYesNoEnum [R/W]
AdminInfo.TaxDefinitionforVatitem : String [R/W]
AdminInfo.TaxDefinitionforVatservice : String [R/W]
AdminInfo.TaxGroupforPurchaseItem : String [R/W]
AdminInfo.TaxGroupforServicePurchase : String [R/W]
AdminInfo.TaxOffice : String [R/W]
AdminInfo.TaxPercentage : Double [R/W]
AdminInfo.TaxRateDetermination : TaxRateDeterminationEnum [R/W]
AdminInfo.ThousandsSeparator : String [R/W]
AdminInfo.TimeTemplate : BoTimeTemplate [R/W]
AdminInfo.TotalsAccuracy : Long [R/W]
AdminInfo.UniqueSerialNo : BoUniqueSerialNumber [R/W]
AdminInfo.UniqueTaxPayerReference : String [R/W]
AdminInfo.UseDefaultPriceList : BoYesNoEnum [R/W]
AdminInfo.UseNegativeAmounts : BoYesNoEnum [R/W]
AdminInfo.UseParentWIPInComponents : BoYesNoEnum [R/W]
AdminInfo.UsePASystem : BoYesNoEnum [R/W]
AdminInfo.UseProductionProfitAndLossAccount : BoYesNoEnum [R/W]
AdminInfo.UserConversionCode : BoYesNoEnum [R/W]
AdminInfo.UseTax : BoYesNoEnum [R/W]
AdminInfo.WeightUnitDefault : Long [R/W]
AdminInfo.WholdingTaxDedHierarchy : BoYesNoEnum [R/W]
AdminInfo.WithholdingTaxDdctExpired : Date [R/W]
AdminInfo.WithholdingTaxDdctOffice : String [R/W]
AdminInfo.WithholdingTaxPHandle : String [R/W]
AdminInfo.WithholdingTaxTdctPercnt : Double [R/W]
AdminInfo.WithholdingTaxVendorDdct : BoYesNoEnum [R/W]
AdminInfo.WithTax : Double [R/W]
AdminInfo.WTAccumAmountAP : Double [R/W]
AdminInfo.WTAccumAmountAR : Double [R/W]
AdminInfo.WTLiableExpense : BoYesNoEnum [R/W]
AdminInfo.XMLFileFolderPath : String [R/W]
AdminInfo.FromXMLFile(ByVal bstrFileName As String)
AdminInfo.FromXMLString(ByVal bstrXML As String)
AdminInfo.GetXMLSchema() -> String
AdminInfo.ToXMLFile(ByVal bstrFileName As String)
AdminInfo.ToXMLString() -> String
AdvancedGLAccountParams.AccountType : InventoryAccountTypeEnum [R/W]
AdvancedGLAccountParams.BPCode : String [R/W]
AdvancedGLAccountParams.FederalTaxID : String [R/W]
AdvancedGLAccountParams.ItemCode : String [R/W]
AdvancedGLAccountParams.PostingDate : Date [R/W]
AdvancedGLAccountParams.ShipToCountry : String [R/W]
AdvancedGLAccountParams.ShipToState : String [R/W]
AdvancedGLAccountParams.UDF1 : String [R/W]
AdvancedGLAccountParams.UDF2 : String [R/W]
AdvancedGLAccountParams.UDF3 : String [R/W]
AdvancedGLAccountParams.UDF4 : String [R/W]
AdvancedGLAccountParams.UDF5 : String [R/W]
AdvancedGLAccountParams.Usage : Long [R/W]
AdvancedGLAccountParams.VatGroup : String [R/W]
AdvancedGLAccountParams.Warehouse : String [R/W]
AdvancedGLAccountParams.FromXMLFile(ByVal bstrFileName As String)
AdvancedGLAccountParams.FromXMLString(ByVal bstrXML As String)
AdvancedGLAccountParams.GetXMLSchema() -> String
AdvancedGLAccountParams.ToXMLFile(ByVal bstrFileName As String)
AdvancedGLAccountParams.ToXMLString() -> String
AdvancedGLAccountReturnParams.AccountCode : String [R]
AdvancedGLAccountReturnParams.FromXMLFile(ByVal bstrFileName As String)
AdvancedGLAccountReturnParams.FromXMLString(ByVal bstrXML As String)
AdvancedGLAccountReturnParams.GetXMLSchema() -> String
AdvancedGLAccountReturnParams.ToXMLFile(ByVal bstrFileName As String)
AdvancedGLAccountReturnParams.ToXMLString() -> String
AlertManagement.Active : BoYesNoEnum [R/W]
AlertManagement.AlertManagementDocuments : AlertManagementDocuments [R]
AlertManagement.AlertManagementRecipients : AlertManagementRecipients [R]
AlertManagement.Code : Long [R]
AlertManagement.DayOfExecution : Long [R/W]
AlertManagement.ExecutionTime : Date [R/W]
AlertManagement.FrequencyInterval : Long [R/W]
AlertManagement.FrequencyType : AlertManagementFrequencyType [R/W]
AlertManagement.LastExecutionDate : Date [R]
AlertManagement.LastExecutionTime : Long [R]
AlertManagement.Name : String [R/W]
AlertManagement.NextExecutionDate : Date [R]
AlertManagement.NextExecutionTime : Date [R]
AlertManagement.Param : String [R/W]
AlertManagement.Priority : AlertManagementPriorityEnum [R/W]
AlertManagement.QueryID : Long [R/W]
AlertManagement.SaveHistory : BoYesNoEnum [R/W]
AlertManagement.Type : AlertManagementTypeEnum [R]
AlertManagement.UserFields : Fields [R]
AlertManagement.FromXMLFile(ByVal bstrFileName As String)
AlertManagement.FromXMLString(ByVal bstrXML As String)
AlertManagement.GetXMLSchema() -> String
AlertManagement.ToXMLFile(ByVal bstrFileName As String)
AlertManagement.ToXMLString() -> String
AlertManagementDocument.Active : BoYesNoEnum [R/W]
AlertManagementDocument.Document : AlertManagementDocumentEnum [R/W]
AlertManagementDocument.FromXMLFile(ByVal bstrFileName As String)
AlertManagementDocument.FromXMLString(ByVal bstrXML As String)
AlertManagementDocument.GetXMLSchema() -> String
AlertManagementDocument.ToXMLFile(ByVal bstrFileName As String)
AlertManagementDocument.ToXMLString() -> String
AlertManagementDocuments.Count : Long [R]
AlertManagementDocuments.Add() -> AlertManagementDocument
AlertManagementDocuments.GetXMLSchema() -> String
AlertManagementDocuments.Item(ByVal vtIndex As Variant) -> AlertManagementDocument
AlertManagementDocuments.ToXMLFile(ByVal bstrFileName As String)
AlertManagementDocuments.ToXMLString() -> String
AlertManagementParams.Code : Long [R/W]
AlertManagementParams.Name : String [R]
AlertManagementParams.Type : AlertManagementTypeEnum [R/W]
AlertManagementParams.FromXMLFile(ByVal bstrFileName As String)
AlertManagementParams.FromXMLString(ByVal bstrXML As String)
AlertManagementParams.GetXMLSchema() -> String
AlertManagementParams.ToXMLFile(ByVal bstrFileName As String)
AlertManagementParams.ToXMLString() -> String
AlertManagementParamsCollection.Count : Long [R]
AlertManagementParamsCollection.Add() -> AlertManagementParams
AlertManagementParamsCollection.GetXMLSchema() -> String
AlertManagementParamsCollection.Item(ByVal vtIndex As Variant) -> AlertManagementParams
AlertManagementParamsCollection.ToXMLFile(ByVal bstrFileName As String)
AlertManagementParamsCollection.ToXMLString() -> String
AlertManagementRecipient.Code : Long [R]
AlertManagementRecipient.SendEmail : BoYesNoEnum [R/W]
AlertManagementRecipient.SendFax : BoYesNoEnum [R/W]
AlertManagementRecipient.SendInternal : BoYesNoEnum [R/W]
AlertManagementRecipient.SendSMS : BoYesNoEnum [R/W]
AlertManagementRecipient.UserCode : Long [R/W]
AlertManagementRecipient.FromXMLFile(ByVal bstrFileName As String)
AlertManagementRecipient.FromXMLString(ByVal bstrXML As String)
AlertManagementRecipient.GetXMLSchema() -> String
AlertManagementRecipient.ToXMLFile(ByVal bstrFileName As String)
AlertManagementRecipient.ToXMLString() -> String
AlertManagementRecipients.Count : Long [R]
AlertManagementRecipients.Add() -> AlertManagementRecipient
AlertManagementRecipients.GetXMLSchema() -> String
AlertManagementRecipients.Item(ByVal vtIndex As Variant) -> AlertManagementRecipient
AlertManagementRecipients.ToXMLFile(ByVal bstrFileName As String)
AlertManagementRecipients.ToXMLString() -> String
AlertManagementService.AddAlertManagement(ByVal pAlertManagement As AlertManagement) -> AlertManagementParams
AlertManagementService.GetAlertManagement(ByVal pAlertManagementParams As AlertManagementParams) -> AlertManagement
AlertManagementService.GetAlertManagementList(ByVal pAlertManagementParams As AlertManagementParams) -> AlertManagementParamsCollection
AlertManagementService.GetDataInterface(ByVal enumMSDI As AlertManagementServiceDataInterfaces) -> Object
AlertManagementService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AlertManagementService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AlertManagementService.UpdateAlertManagement(ByVal pIAlertManagement As AlertManagement)
AlternateCatNum.Browser : DataBrowser [R]
AlternateCatNum.CardCode : String [R/W]
AlternateCatNum.Description : String [R/W]
AlternateCatNum.DisplayBPCatalogNumber : BoYesNoEnum [R/W]
AlternateCatNum.IsDefault : BoYesNoEnum [R/W]
AlternateCatNum.ItemCode : String [R/W]
AlternateCatNum.Substitute : String [R/W]
AlternateCatNum.UserFields : UserFields [R]
AlternateCatNum.Add() -> Long
AlternateCatNum.GetAsXML() -> String
AlternateCatNum.GetByKey(ByVal ItemCode As String, ByVal CardCode As String, ByVal Substitute As String) -> Boolean
AlternateCatNum.Remove() -> Long
AlternateCatNum.SaveToFile(ByVal FileName As String)
AlternateCatNum.SaveXML(ByRef FileName As String)
AlternateCatNum.Update() -> Long
AlternativeItem.AlternativeItemCode : String [R/W]
AlternativeItem.MatchFactor : Double [R/W]
AlternativeItem.Remarks : String [R/W]
AlternativeItem.FromXMLFile(ByVal bstrFileName As String)
AlternativeItem.FromXMLString(ByVal bstrXML As String)
AlternativeItem.GetXMLSchema() -> String
AlternativeItem.ToXMLFile(ByVal bstrFileName As String)
AlternativeItem.ToXMLString() -> String
AlternativeItems.Count : Long [R]
AlternativeItems.Add() -> AlternativeItem
AlternativeItems.GetXMLSchema() -> String
AlternativeItems.Item(ByVal vtIndex As Variant) -> AlternativeItem
AlternativeItems.Remove(ByVal vtIndex As Variant)
AlternativeItems.ToXMLFile(ByVal bstrFileName As String)
AlternativeItems.ToXMLString() -> String
AlternativeItemsService.AddItem(ByVal pIOriginalItem As OriginalItem) -> OriginalItemParams
AlternativeItemsService.DeleteItem(ByVal pIOriginalItemParams As OriginalItemParams)
AlternativeItemsService.GetDataInterface(ByVal enumMSDI As AlternativeItemsServiceDataInterfaces) -> Object
AlternativeItemsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AlternativeItemsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AlternativeItemsService.GetItem(ByVal pIOriginalItemParams As OriginalItemParams) -> OriginalItem
AlternativeItemsService.UpdateItem(ByVal pIOriginalItem As OriginalItem)
ApprovalRequest.ApprovalRequestDecisions : ApprovalRequestDecisions [R]
ApprovalRequest.ApprovalRequestLines : ApprovalRequestLines [R]
ApprovalRequest.ApprovalTemplatesID : Long [R]
ApprovalRequest.Code : Long [R]
ApprovalRequest.CreationDate : Date [R]
ApprovalRequest.CreationTime : Date [R]
ApprovalRequest.CurrentStage : Long [R]
ApprovalRequest.DraftEntry : Long [R]
ApprovalRequest.DraftType : String [R]
ApprovalRequest.IsDraft : String [R]
ApprovalRequest.ObjectEntry : Long [R]
ApprovalRequest.ObjectType : String [R]
ApprovalRequest.OriginatorID : Long [R]
ApprovalRequest.Remarks : String [R]
ApprovalRequest.Status : BoApprovalRequestStatusEnum [R]
ApprovalRequest.FromXMLFile(ByVal bstrFileName As String)
ApprovalRequest.FromXMLString(ByVal bstrXML As String)
ApprovalRequest.GetXMLSchema() -> String
ApprovalRequest.ToXMLFile(ByVal bstrFileName As String)
ApprovalRequest.ToXMLString() -> String
ApprovalRequestDecision.ApproverPassword : String [R/W]
ApprovalRequestDecision.ApproverUserName : String [R/W]
ApprovalRequestDecision.Remarks : String [R/W]
ApprovalRequestDecision.Status : BoApprovalRequestDecisionEnum [R/W]
ApprovalRequestDecision.FromXMLFile(ByVal bstrFileName As String)
ApprovalRequestDecision.FromXMLString(ByVal bstrXML As String)
ApprovalRequestDecision.GetXMLSchema() -> String
ApprovalRequestDecision.ToXMLFile(ByVal bstrFileName As String)
ApprovalRequestDecision.ToXMLString() -> String
ApprovalRequestDecisions.Count : Long [R]
ApprovalRequestDecisions.Add() -> ApprovalRequestDecision
ApprovalRequestDecisions.GetXMLSchema() -> String
ApprovalRequestDecisions.Item(ByVal vtIndex As Variant) -> ApprovalRequestDecision
ApprovalRequestDecisions.ToXMLFile(ByVal bstrFileName As String)
ApprovalRequestDecisions.ToXMLString() -> String
ApprovalRequestLine.CreationDate : Date [R]
ApprovalRequestLine.CreationTime : Date [R]
ApprovalRequestLine.Remarks : String [R]
ApprovalRequestLine.StageCode : Long [R]
ApprovalRequestLine.Status : BoApprovalRequestDecisionEnum [R]
ApprovalRequestLine.UpdateDate : Date [R]
ApprovalRequestLine.UpdateTime : Date [R]
ApprovalRequestLine.UserID : Long [R]
ApprovalRequestLine.FromXMLFile(ByVal bstrFileName As String)
ApprovalRequestLine.FromXMLString(ByVal bstrXML As String)
ApprovalRequestLine.GetXMLSchema() -> String
ApprovalRequestLine.ToXMLFile(ByVal bstrFileName As String)
ApprovalRequestLine.ToXMLString() -> String
ApprovalRequestLines.Count : Long [R]
ApprovalRequestLines.Add() -> ApprovalRequestLine
ApprovalRequestLines.GetXMLSchema() -> String
ApprovalRequestLines.Item(ByVal vtIndex As Variant) -> ApprovalRequestLine
ApprovalRequestLines.ToXMLFile(ByVal bstrFileName As String)
ApprovalRequestLines.ToXMLString() -> String
ApprovalRequestParams.Code : Long [R/W]
ApprovalRequestParams.Remarks : String [R]
ApprovalRequestParams.Status : BoApprovalRequestStatusEnum [R]
ApprovalRequestParams.FromXMLFile(ByVal bstrFileName As String)
ApprovalRequestParams.FromXMLString(ByVal bstrXML As String)
ApprovalRequestParams.GetXMLSchema() -> String
ApprovalRequestParams.ToXMLFile(ByVal bstrFileName As String)
ApprovalRequestParams.ToXMLString() -> String
ApprovalRequestsParams.Count : Long [R]
ApprovalRequestsParams.Add() -> ApprovalRequestParams
ApprovalRequestsParams.GetXMLSchema() -> String
ApprovalRequestsParams.Item(ByVal vtIndex As Variant) -> ApprovalRequestParams
ApprovalRequestsParams.ToXMLFile(ByVal bstrFileName As String)
ApprovalRequestsParams.ToXMLString() -> String
ApprovalRequestsService.CancelApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams)
ApprovalRequestsService.GetAllApprovalRequestsList() -> ApprovalRequestsParams
ApprovalRequestsService.GetApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams) -> ApprovalRequest
ApprovalRequestsService.GetApprovalRequestList() -> ApprovalRequestsParams
ApprovalRequestsService.GetDataInterface(ByVal enumMSDI As ApprovalRequestsServiceDataInterfaces) -> Object
ApprovalRequestsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ApprovalRequestsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ApprovalRequestsService.GetOpenApprovalRequestList() -> ApprovalRequestsParams
ApprovalRequestsService.RestoreApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams)
ApprovalRequestsService.UpdateRequest(ByVal pIApprovalRequest As ApprovalRequest)
ApprovalStage.ApprovalStageApprovers : ApprovalStageApprovers [R]
ApprovalStage.Code : Long [R]
ApprovalStage.Name : String [R/W]
ApprovalStage.NoOfApproversRequired : Long [R/W]
ApprovalStage.Remarks : String [R/W]
ApprovalStage.FromXMLFile(ByVal bstrFileName As String)
ApprovalStage.FromXMLString(ByVal bstrXML As String)
ApprovalStage.GetXMLSchema() -> String
ApprovalStage.ToXMLFile(ByVal bstrFileName As String)
ApprovalStage.ToXMLString() -> String
ApprovalStageApprover.UserID : Long [R/W]
ApprovalStageApprover.FromXMLFile(ByVal bstrFileName As String)
ApprovalStageApprover.FromXMLString(ByVal bstrXML As String)
ApprovalStageApprover.GetXMLSchema() -> String
ApprovalStageApprover.ToXMLFile(ByVal bstrFileName As String)
ApprovalStageApprover.ToXMLString() -> String
ApprovalStageApprovers.Count : Long [R]
ApprovalStageApprovers.Add() -> ApprovalStageApprover
ApprovalStageApprovers.GetXMLSchema() -> String
ApprovalStageApprovers.Item(ByVal vtIndex As Variant) -> ApprovalStageApprover
ApprovalStageApprovers.ToXMLFile(ByVal bstrFileName As String)
ApprovalStageApprovers.ToXMLString() -> String
ApprovalStageParams.Code : Long [R/W]
ApprovalStageParams.Name : String [R]
ApprovalStageParams.FromXMLFile(ByVal bstrFileName As String)
ApprovalStageParams.FromXMLString(ByVal bstrXML As String)
ApprovalStageParams.GetXMLSchema() -> String
ApprovalStageParams.ToXMLFile(ByVal bstrFileName As String)
ApprovalStageParams.ToXMLString() -> String
ApprovalStages.Count : Long [R]
ApprovalStages.Add() -> ApprovalStage
ApprovalStages.GetXMLSchema() -> String
ApprovalStages.Item(ByVal vtIndex As Variant) -> ApprovalStage
ApprovalStages.ToXMLFile(ByVal bstrFileName As String)
ApprovalStages.ToXMLString() -> String
ApprovalStagesParams.Count : Long [R]
ApprovalStagesParams.Add() -> ApprovalStageParams
ApprovalStagesParams.GetXMLSchema() -> String
ApprovalStagesParams.Item(ByVal vtIndex As Variant) -> ApprovalStageParams
ApprovalStagesParams.ToXMLFile(ByVal bstrFileName As String)
ApprovalStagesParams.ToXMLString() -> String
ApprovalStagesService.AddApprovalStage(ByVal pApprovalStage As ApprovalStage) -> ApprovalStageParams
ApprovalStagesService.GetApprovalStage(ByVal pIApprovalStageParams As ApprovalStageParams) -> ApprovalStage
ApprovalStagesService.GetApprovalStageList() -> ApprovalStagesParams
ApprovalStagesService.GetDataInterface(ByVal enumMSDI As ApprovalStagesServiceDataInterfaces) -> Object
ApprovalStagesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ApprovalStagesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ApprovalStagesService.RemoveApprovalStage(ByVal pIApprovalStageParams As ApprovalStageParams)
ApprovalStagesService.UpdateApprovalStage(ByVal pIApprovalStage As ApprovalStage)
ApprovalTemplate.ApprovalTemplateDocuments : ApprovalTemplateDocuments [R]
ApprovalTemplate.ApprovalTemplateQueries : ApprovalTemplateQueries [R]
ApprovalTemplate.ApprovalTemplateStages : ApprovalTemplateStages [R]
ApprovalTemplate.ApprovalTemplateTerms : ApprovalTemplateTerms [R]
ApprovalTemplate.ApprovalTemplateUsers : ApprovalTemplateUsers [R]
ApprovalTemplate.Code : Long [R]
ApprovalTemplate.IsActive : BoYesNoEnum [R/W]
ApprovalTemplate.IsActiveWhenUpdatingDocuments : BoYesNoEnum [R/W]
ApprovalTemplate.Name : String [R/W]
ApprovalTemplate.Remarks : String [R/W]
ApprovalTemplate.UseTerms : BoYesNoEnum [R/W]
ApprovalTemplate.FromXMLFile(ByVal bstrFileName As String)
ApprovalTemplate.FromXMLString(ByVal bstrXML As String)
ApprovalTemplate.GetXMLSchema() -> String
ApprovalTemplate.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplate.ToXMLString() -> String
ApprovalTemplateDocument.DocumentType : ApprovalTemplatesDocumentTypeEnum [R/W]
ApprovalTemplateDocument.FromXMLFile(ByVal bstrFileName As String)
ApprovalTemplateDocument.FromXMLString(ByVal bstrXML As String)
ApprovalTemplateDocument.GetXMLSchema() -> String
ApprovalTemplateDocument.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateDocument.ToXMLString() -> String
ApprovalTemplateDocuments.Count : Long [R]
ApprovalTemplateDocuments.Add() -> ApprovalTemplateDocument
ApprovalTemplateDocuments.GetXMLSchema() -> String
ApprovalTemplateDocuments.Item(ByVal vtIndex As Variant) -> ApprovalTemplateDocument
ApprovalTemplateDocuments.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateDocuments.ToXMLString() -> String
ApprovalTemplateParams.Code : Long [R/W]
ApprovalTemplateParams.Name : String [R]
ApprovalTemplateParams.FromXMLFile(ByVal bstrFileName As String)
ApprovalTemplateParams.FromXMLString(ByVal bstrXML As String)
ApprovalTemplateParams.GetXMLSchema() -> String
ApprovalTemplateParams.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateParams.ToXMLString() -> String
ApprovalTemplateQueries.Count : Long [R]
ApprovalTemplateQueries.Add() -> ApprovalTemplateQuery
ApprovalTemplateQueries.GetXMLSchema() -> String
ApprovalTemplateQueries.Item(ByVal vtIndex As Variant) -> ApprovalTemplateQuery
ApprovalTemplateQueries.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateQueries.ToXMLString() -> String
ApprovalTemplateQuery.QueryID : Long [R/W]
ApprovalTemplateQuery.FromXMLFile(ByVal bstrFileName As String)
ApprovalTemplateQuery.FromXMLString(ByVal bstrXML As String)
ApprovalTemplateQuery.GetXMLSchema() -> String
ApprovalTemplateQuery.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateQuery.ToXMLString() -> String
ApprovalTemplates.Count : Long [R]
ApprovalTemplates.Add() -> ApprovalTemplate
ApprovalTemplates.GetXMLSchema() -> String
ApprovalTemplates.Item(ByVal vtIndex As Variant) -> ApprovalTemplate
ApprovalTemplates.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplates.ToXMLString() -> String
ApprovalTemplatesParams.Count : Long [R]
ApprovalTemplatesParams.Add() -> ApprovalTemplateParams
ApprovalTemplatesParams.GetXMLSchema() -> String
ApprovalTemplatesParams.Item(ByVal vtIndex As Variant) -> ApprovalTemplateParams
ApprovalTemplatesParams.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplatesParams.ToXMLString() -> String
ApprovalTemplatesService.AddApprovalTemplate(ByVal pApprovalTemplate As ApprovalTemplate) -> ApprovalTemplateParams
ApprovalTemplatesService.GetApprovalTemplate(ByVal pIApprovalTemplateParams As ApprovalTemplateParams) -> ApprovalTemplate
ApprovalTemplatesService.GetApprovalTemplateList() -> ApprovalTemplatesParams
ApprovalTemplatesService.GetDataInterface(ByVal enumMSDI As ApprovalTemplatesServiceDataInterfaces) -> Object
ApprovalTemplatesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ApprovalTemplatesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ApprovalTemplatesService.RemoveApprovalTemplate(ByVal pIApprovalTemplateParams As ApprovalTemplateParams)
ApprovalTemplatesService.UpdateApprovalTemplate(ByVal pIApprovalTemplate As ApprovalTemplate)
ApprovalTemplateStage.ApprovalStageCode : Long [R/W]
ApprovalTemplateStage.Remarks : String [R/W]
ApprovalTemplateStage.SortID : Long [R/W]
ApprovalTemplateStage.FromXMLFile(ByVal bstrFileName As String)
ApprovalTemplateStage.FromXMLString(ByVal bstrXML As String)
ApprovalTemplateStage.GetXMLSchema() -> String
ApprovalTemplateStage.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateStage.ToXMLString() -> String
ApprovalTemplateStages.Count : Long [R]
ApprovalTemplateStages.Add() -> ApprovalTemplateStage
ApprovalTemplateStages.GetXMLSchema() -> String
ApprovalTemplateStages.Item(ByVal vtIndex As Variant) -> ApprovalTemplateStage
ApprovalTemplateStages.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateStages.ToXMLString() -> String
ApprovalTemplateTerm.ConditionType : ApprovalTemplateConditionTypeEnum [R/W]
ApprovalTemplateTerm.OperationType : ApprovalTemplateOperationTypeEnum [R/W]
ApprovalTemplateTerm.Value : String [R/W]
ApprovalTemplateTerm.FromXMLFile(ByVal bstrFileName As String)
ApprovalTemplateTerm.FromXMLString(ByVal bstrXML As String)
ApprovalTemplateTerm.GetXMLSchema() -> String
ApprovalTemplateTerm.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateTerm.ToXMLString() -> String
ApprovalTemplateTerms.Count : Long [R]
ApprovalTemplateTerms.Add() -> ApprovalTemplateTerm
ApprovalTemplateTerms.GetXMLSchema() -> String
ApprovalTemplateTerms.Item(ByVal vtIndex As Variant) -> ApprovalTemplateTerm
ApprovalTemplateTerms.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateTerms.ToXMLString() -> String
ApprovalTemplateUser.UserID : Long [R/W]
ApprovalTemplateUser.FromXMLFile(ByVal bstrFileName As String)
ApprovalTemplateUser.FromXMLString(ByVal bstrXML As String)
ApprovalTemplateUser.GetXMLSchema() -> String
ApprovalTemplateUser.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateUser.ToXMLString() -> String
ApprovalTemplateUsers.Count : Long [R]
ApprovalTemplateUsers.Add() -> ApprovalTemplateUser
ApprovalTemplateUsers.GetXMLSchema() -> String
ApprovalTemplateUsers.Item(ByVal vtIndex As Variant) -> ApprovalTemplateUser
ApprovalTemplateUsers.ToXMLFile(ByVal bstrFileName As String)
ApprovalTemplateUsers.ToXMLString() -> String
AssetClass.AssetClassCollection : AssetClassCollection [R]
AssetClass.AssetType : AssetTypeEnum [R/W]
AssetClass.AttributeGroup : Long [R/W]
AssetClass.BPLID : Long [R/W]
AssetClass.Code : String [R/W]
AssetClass.Description : String [R/W]
AssetClass.ValueLimitFrom : Double [R/W]
AssetClass.ValueLimitTo : Double [R/W]
AssetClass.FromXMLFile(ByVal bstrFileName As String)
AssetClass.FromXMLString(ByVal bstrXML As String)
AssetClass.GetXMLSchema() -> String
AssetClass.ToXMLFile(ByVal bstrFileName As String)
AssetClass.ToXMLString() -> String
AssetClassCollection.Count : Long [R]
AssetClassCollection.Add() -> AssetClassLine
AssetClassCollection.GetXMLSchema() -> String
AssetClassCollection.Item(ByVal vtIndex As Variant) -> AssetClassLine
AssetClassCollection.ToXMLFile(ByVal bstrFileName As String)
AssetClassCollection.ToXMLString() -> String
AssetClassesService.Add(ByVal pIAssetClass As AssetClass) -> AssetClassParams
AssetClassesService.Delete(ByVal pIAssetClassParams As AssetClassParams)
AssetClassesService.Get(ByVal pIAssetClassParams As AssetClassParams) -> AssetClass
AssetClassesService.GetDataInterface(ByVal enumMSDI As AssetClassesServiceDataInterfaces) -> Object
AssetClassesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AssetClassesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AssetClassesService.GetList() -> AssetClassParamsCollection
AssetClassesService.Update(ByVal pIAssetClass As AssetClass)
AssetClassLine.AccountDetermination : String [R/W]
AssetClassLine.ActiveStatus : BoYesNoEnum [R/W]
AssetClassLine.Code : String [R]
AssetClassLine.DepreciationAreaID : String [R/W]
AssetClassLine.DepreciationTypeID : String [R/W]
AssetClassLine.LineNumber : Long [R]
AssetClassLine.UseLife : Long [R/W]
AssetClassLine.FromXMLFile(ByVal bstrFileName As String)
AssetClassLine.FromXMLString(ByVal bstrXML As String)
AssetClassLine.GetXMLSchema() -> String
AssetClassLine.ToXMLFile(ByVal bstrFileName As String)
AssetClassLine.ToXMLString() -> String
AssetClassParams.Code : String [R/W]
AssetClassParams.Description : String [R]
AssetClassParams.FromXMLFile(ByVal bstrFileName As String)
AssetClassParams.FromXMLString(ByVal bstrXML As String)
AssetClassParams.GetXMLSchema() -> String
AssetClassParams.ToXMLFile(ByVal bstrFileName As String)
AssetClassParams.ToXMLString() -> String
AssetClassParamsCollection.Count : Long [R]
AssetClassParamsCollection.Add() -> AssetClassParams
AssetClassParamsCollection.GetXMLSchema() -> String
AssetClassParamsCollection.Item(ByVal vtIndex As Variant) -> AssetClassParams
AssetClassParamsCollection.ToXMLFile(ByVal bstrFileName As String)
AssetClassParamsCollection.ToXMLString() -> String
AssetDepreciationGroup.Code : String [R/W]
AssetDepreciationGroup.Description : String [R/W]
AssetDepreciationGroup.Group : String [R/W]
AssetDepreciationGroup.FromXMLFile(ByVal bstrFileName As String)
AssetDepreciationGroup.FromXMLString(ByVal bstrXML As String)
AssetDepreciationGroup.GetXMLSchema() -> String
AssetDepreciationGroup.ToXMLFile(ByVal bstrFileName As String)
AssetDepreciationGroup.ToXMLString() -> String
AssetDepreciationGroupParams.Code : String [R/W]
AssetDepreciationGroupParams.Description : String [R]
AssetDepreciationGroupParams.FromXMLFile(ByVal bstrFileName As String)
AssetDepreciationGroupParams.FromXMLString(ByVal bstrXML As String)
AssetDepreciationGroupParams.GetXMLSchema() -> String
AssetDepreciationGroupParams.ToXMLFile(ByVal bstrFileName As String)
AssetDepreciationGroupParams.ToXMLString() -> String
AssetDepreciationGroupParamsCollection.Count : Long [R]
AssetDepreciationGroupParamsCollection.Add() -> AssetDepreciationGroupParams
AssetDepreciationGroupParamsCollection.GetXMLSchema() -> String
AssetDepreciationGroupParamsCollection.Item(ByVal vtIndex As Variant) -> AssetDepreciationGroupParams
AssetDepreciationGroupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
AssetDepreciationGroupParamsCollection.ToXMLString() -> String
AssetDepreciationGroupsService.Add(ByVal pIAssetDepreciationGroup As AssetDepreciationGroup) -> AssetDepreciationGroupParams
AssetDepreciationGroupsService.Delete(ByVal pIAssetDepreciationGroupParams As AssetDepreciationGroupParams)
AssetDepreciationGroupsService.Get(ByVal pIAssetDepreciationGroupParams As AssetDepreciationGroupParams) -> AssetDepreciationGroup
AssetDepreciationGroupsService.GetDataInterface(ByVal enumMSDI As AssetDepreciationGroupsServiceDataInterfaces) -> Object
AssetDepreciationGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AssetDepreciationGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AssetDepreciationGroupsService.GetList() -> AssetDepreciationGroupParamsCollection
AssetDepreciationGroupsService.Update(ByVal pIAssetDepreciationGroup As AssetDepreciationGroup)
AssetDocument.AssetDocumentAreaJournalCollection : AssetDocumentAreaJournalCollection [R]
AssetDocument.AssetDocumentLineCollection : AssetDocumentLineCollection [R]
AssetDocument.AssetValueDate : Date [R/W]
AssetDocument.BaseReference : String [R]
AssetDocument.BPLID : Long [R/W]
AssetDocument.BPLName : String [R/W]
AssetDocument.CancellationDate : Date [R/W]
AssetDocument.CancellationOption : ClosingOptionEnum [R/W]
AssetDocument.Currency : String [R/W]
AssetDocument.DepreciationArea : String [R/W]
AssetDocument.DocEntry : Long [R]
AssetDocument.DocNum : Long [R/W]
AssetDocument.DocumentDate : Date [R/W]
AssetDocument.DocumentRate : Double [R/W]
AssetDocument.DocumentTotal : Double [R]
AssetDocument.DocumentTotalFC : Double [R]
AssetDocument.DocumentTotalSC : Double [R]
AssetDocument.DocumentType : AssetDocumentTypeEnum [R/W]
AssetDocument.HandWritten : BoYesNoEnum [R/W]
AssetDocument.LowValueAssetRetirement : BoYesNoEnum [R/W]
AssetDocument.ManualDepreciationType : String [R/W]
AssetDocument.Origin : Long [R]
AssetDocument.OriginalType : AssetOriginalTypeEnum [R]
AssetDocument.PostingDate : Date [R/W]
AssetDocument.Reference : String [R/W]
AssetDocument.Remarks : String [R/W]
AssetDocument.Series : Long [R/W]
AssetDocument.Status : AssetDocumentStatusEnum [R]
AssetDocument.SummerizeByDistributionRules : BoYesNoEnum [R/W]
AssetDocument.SummerizeByProjects : BoYesNoEnum [R/W]
AssetDocument.VATRegNum : String [R/W]
AssetDocument.FromXMLFile(ByVal bstrFileName As String)
AssetDocument.FromXMLString(ByVal bstrXML As String)
AssetDocument.GetXMLSchema() -> String
AssetDocument.ToXMLFile(ByVal bstrFileName As String)
AssetDocument.ToXMLString() -> String
AssetDocumentAreaJournal.CancellationJournalRemarks : String [R/W]
AssetDocumentAreaJournal.CancellationTransactionNumber : Long [R]
AssetDocumentAreaJournal.DepreciationArea : String [R/W]
AssetDocumentAreaJournal.DocEntry : Long [R]
AssetDocumentAreaJournal.JournalRemarks : String [R/W]
AssetDocumentAreaJournal.LineNumber : Long [R/W]
AssetDocumentAreaJournal.TransactionNumber : Long [R]
AssetDocumentAreaJournal.FromXMLFile(ByVal bstrFileName As String)
AssetDocumentAreaJournal.FromXMLString(ByVal bstrXML As String)
AssetDocumentAreaJournal.GetXMLSchema() -> String
AssetDocumentAreaJournal.ToXMLFile(ByVal bstrFileName As String)
AssetDocumentAreaJournal.ToXMLString() -> String
AssetDocumentAreaJournalCollection.Count : Long [R]
AssetDocumentAreaJournalCollection.Add() -> AssetDocumentAreaJournal
AssetDocumentAreaJournalCollection.GetXMLSchema() -> String
AssetDocumentAreaJournalCollection.Item(ByVal vtIndex As Variant) -> AssetDocumentAreaJournal
AssetDocumentAreaJournalCollection.ToXMLFile(ByVal bstrFileName As String)
AssetDocumentAreaJournalCollection.ToXMLString() -> String
AssetDocumentLine.APC : Double [R/W]
AssetDocumentLine.AssetNumber : String [R/W]
AssetDocumentLine.DepreciationArea : String [R]
AssetDocumentLine.DistributionRule : String [R/W]
AssetDocumentLine.DistributionRule2 : String [R/W]
AssetDocumentLine.DistributionRule3 : String [R/W]
AssetDocumentLine.DistributionRule4 : String [R/W]
AssetDocumentLine.DistributionRule5 : String [R/W]
AssetDocumentLine.DocEntry : Long [R]
AssetDocumentLine.GLAccount : String [R/W]
AssetDocumentLine.LineNumber : Long [R/W]
AssetDocumentLine.NewAssetClass : String [R/W]
AssetDocumentLine.NewAssetNumber : String [R/W]
AssetDocumentLine.Partial : BoYesNoEnum [R/W]
AssetDocumentLine.Project : String [R/W]
AssetDocumentLine.Quantity : Double [R/W]
AssetDocumentLine.Remarks : String [R/W]
AssetDocumentLine.TotalFC : Double [R/W]
AssetDocumentLine.TotalLC : Double [R/W]
AssetDocumentLine.TotalSC : Double [R]
AssetDocumentLine.FromXMLFile(ByVal bstrFileName As String)
AssetDocumentLine.FromXMLString(ByVal bstrXML As String)
AssetDocumentLine.GetXMLSchema() -> String
AssetDocumentLine.ToXMLFile(ByVal bstrFileName As String)
AssetDocumentLine.ToXMLString() -> String
AssetDocumentLineCollection.Count : Long [R]
AssetDocumentLineCollection.Add() -> AssetDocumentLine
AssetDocumentLineCollection.GetXMLSchema() -> String
AssetDocumentLineCollection.Item(ByVal vtIndex As Variant) -> AssetDocumentLine
AssetDocumentLineCollection.ToXMLFile(ByVal bstrFileName As String)
AssetDocumentLineCollection.ToXMLString() -> String
AssetDocumentParams.CancellationDate : Date [R/W]
AssetDocumentParams.CancellationOption : ClosingOptionEnum [R/W]
AssetDocumentParams.Code : Long [R/W]
AssetDocumentParams.FromXMLFile(ByVal bstrFileName As String)
AssetDocumentParams.FromXMLString(ByVal bstrXML As String)
AssetDocumentParams.GetXMLSchema() -> String
AssetDocumentParams.ToXMLFile(ByVal bstrFileName As String)
AssetDocumentParams.ToXMLString() -> String
AssetDocumentParamsCollection.Count : Long [R]
AssetDocumentParamsCollection.Add() -> AssetDocumentParams
AssetDocumentParamsCollection.GetXMLSchema() -> String
AssetDocumentParamsCollection.Item(ByVal vtIndex As Variant) -> AssetDocumentParams
AssetDocumentParamsCollection.ToXMLFile(ByVal bstrFileName As String)
AssetDocumentParamsCollection.ToXMLString() -> String
AssetDocumentService.Add(ByVal pIAssetDocument As AssetDocument) -> AssetDocumentParams
AssetDocumentService.Cancel(ByVal pIAssetDocumentParams As AssetDocumentParams)
AssetDocumentService.Delete(ByVal pIAssetDocumentParams As AssetDocumentParams)
AssetDocumentService.Get(ByVal pIAssetDocumentParams As AssetDocumentParams) -> AssetDocument
AssetDocumentService.GetDataInterface(ByVal enumMSDI As AssetDocumentServiceDataInterfaces) -> Object
AssetDocumentService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AssetDocumentService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AssetDocumentService.GetList() -> AssetDocumentParamsCollection
AssetDocumentService.Update(ByVal pIAssetDocument As AssetDocument)
AssetGroup.Code : String [R/W]
AssetGroup.Description : String [R/W]
AssetGroup.FromXMLFile(ByVal bstrFileName As String)
AssetGroup.FromXMLString(ByVal bstrXML As String)
AssetGroup.GetXMLSchema() -> String
AssetGroup.ToXMLFile(ByVal bstrFileName As String)
AssetGroup.ToXMLString() -> String
AssetGroupParams.Code : String [R/W]
AssetGroupParams.Description : String [R]
AssetGroupParams.FromXMLFile(ByVal bstrFileName As String)
AssetGroupParams.FromXMLString(ByVal bstrXML As String)
AssetGroupParams.GetXMLSchema() -> String
AssetGroupParams.ToXMLFile(ByVal bstrFileName As String)
AssetGroupParams.ToXMLString() -> String
AssetGroupParamsCollection.Count : Long [R]
AssetGroupParamsCollection.Add() -> AssetGroupParams
AssetGroupParamsCollection.GetXMLSchema() -> String
AssetGroupParamsCollection.Item(ByVal vtIndex As Variant) -> AssetGroupParams
AssetGroupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
AssetGroupParamsCollection.ToXMLString() -> String
AssetGroupsService.Add(ByVal pIAssetGroup As AssetGroup) -> AssetGroupParams
AssetGroupsService.Delete(ByVal pIAssetGroupParams As AssetGroupParams)
AssetGroupsService.Get(ByVal pIAssetGroupParams As AssetGroupParams) -> AssetGroup
AssetGroupsService.GetDataInterface(ByVal enumMSDI As AssetGroupsServiceDataInterfaces) -> Object
AssetGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AssetGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AssetGroupsService.GetList() -> AssetGroupParamsCollection
AssetGroupsService.Update(ByVal pIAssetGroup As AssetGroup)
AssetRevaluation.AssetRevaluationLineCollection : AssetRevaluationLineCollection [R]
AssetRevaluation.AssetValueDate : Date [R/W]
AssetRevaluation.BPLID : Long [R/W]
AssetRevaluation.BPLName : String [R]
AssetRevaluation.DepreciationArea : String [R/W]
AssetRevaluation.DocEntry : Long [R]
AssetRevaluation.DocNum : Long [R]
AssetRevaluation.DocumentDate : Date [R/W]
AssetRevaluation.HandWritten : BoYesNoEnum [R/W]
AssetRevaluation.IfrsPosting : BoYesNoEnum [R/W]
AssetRevaluation.JournalRemarks : String [R/W]
AssetRevaluation.PeriodIndicator : String [R]
AssetRevaluation.PostingDate : Date [R/W]
AssetRevaluation.Reference : String [R/W]
AssetRevaluation.Remarks : String [R/W]
AssetRevaluation.RevaluationPercent : Double [R/W]
AssetRevaluation.Series : Long [R/W]
AssetRevaluation.TransId : Long [R]
AssetRevaluation.VATRegNum : String [R/W]
AssetRevaluation.FromXMLFile(ByVal bstrFileName As String)
AssetRevaluation.FromXMLString(ByVal bstrXML As String)
AssetRevaluation.GetXMLSchema() -> String
AssetRevaluation.ToXMLFile(ByVal bstrFileName As String)
AssetRevaluation.ToXMLString() -> String
AssetRevaluationLine.AssetNumber : String [R/W]
AssetRevaluationLine.CurrentNBV : Double [R]
AssetRevaluationLine.DocEntry : Long [R]
AssetRevaluationLine.LineNumber : Long [R]
AssetRevaluationLine.NewNBV : Double [R/W]
AssetRevaluationLine.Remarks : String [R/W]
AssetRevaluationLine.RevaluationPercent : Double [R/W]
AssetRevaluationLine.FromXMLFile(ByVal bstrFileName As String)
AssetRevaluationLine.FromXMLString(ByVal bstrXML As String)
AssetRevaluationLine.GetXMLSchema() -> String
AssetRevaluationLine.ToXMLFile(ByVal bstrFileName As String)
AssetRevaluationLine.ToXMLString() -> String
AssetRevaluationLineCollection.Count : Long [R]
AssetRevaluationLineCollection.Add() -> AssetRevaluationLine
AssetRevaluationLineCollection.GetXMLSchema() -> String
AssetRevaluationLineCollection.Item(ByVal vtIndex As Variant) -> AssetRevaluationLine
AssetRevaluationLineCollection.ToXMLFile(ByVal bstrFileName As String)
AssetRevaluationLineCollection.ToXMLString() -> String
AssetRevaluationParams.DocEntry : Long [R/W]
AssetRevaluationParams.FromXMLFile(ByVal bstrFileName As String)
AssetRevaluationParams.FromXMLString(ByVal bstrXML As String)
AssetRevaluationParams.GetXMLSchema() -> String
AssetRevaluationParams.ToXMLFile(ByVal bstrFileName As String)
AssetRevaluationParams.ToXMLString() -> String
AssetRevaluationParamsCollection.Count : Long [R]
AssetRevaluationParamsCollection.Add() -> AssetRevaluationParams
AssetRevaluationParamsCollection.GetXMLSchema() -> String
AssetRevaluationParamsCollection.Item(ByVal vtIndex As Variant) -> AssetRevaluationParams
AssetRevaluationParamsCollection.ToXMLFile(ByVal bstrFileName As String)
AssetRevaluationParamsCollection.ToXMLString() -> String
AssetRevaluationService.Add(ByVal pIAssetRevaluation As AssetRevaluation) -> AssetRevaluationParams
AssetRevaluationService.Delete(ByVal pIAssetRevaluationParams As AssetRevaluationParams)
AssetRevaluationService.Get(ByVal pIAssetRevaluationParams As AssetRevaluationParams) -> AssetRevaluation
AssetRevaluationService.GetDataInterface(ByVal enumMSDI As AssetRevaluationServiceDataInterfaces) -> Object
AssetRevaluationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AssetRevaluationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AssetRevaluationService.GetList() -> AssetRevaluationParamsCollection
AssetRevaluationService.Update(ByVal pIAssetRevaluation As AssetRevaluation)
Attachment.FileName : String [R/W]
Attachments.Count : Long [R]
Attachments.Add()
Attachments.Item(ByVal Index As Variant) -> Attachment
Attachments.Refresh()
Attachments2.AbsoluteEntry : Long [R]
Attachments2.Browser : DataBrowser [R]
Attachments2.Lines : Attachments2_Lines [R]
Attachments2.UserFields : UserFields [R]
Attachments2.Add() -> Long
Attachments2.GetAsXML() -> String
Attachments2.GetByKey(ByVal lAbsoluteEntry As Long) -> Boolean
Attachments2.SaveToFile(ByVal bstrFileName As String)
Attachments2.SaveXML(ByRef pbstrFileName As String)
Attachments2.Update() -> Long
Attachments2_Lines.AbsoluteEntry : Long [R]
Attachments2_Lines.AttachmentDate : Date [R]
Attachments2_Lines.CopyToProductionOrder : BoYesNoEnum [R/W]
Attachments2_Lines.CopyToTargetDoc : BoYesNoEnum [R/W]
Attachments2_Lines.Count : Long [R]
Attachments2_Lines.FileExtension : String [R/W]
Attachments2_Lines.FileName : String [R/W]
Attachments2_Lines.FreeText : String [R/W]
Attachments2_Lines.LineNum : Long [R/W]
Attachments2_Lines.Override : BoYesNoEnum [R/W]
Attachments2_Lines.SourcePath : String [R/W]
Attachments2_Lines.UserFields : UserFields [R]
Attachments2_Lines.UserID : Long [R]
Attachments2_Lines.Add()
Attachments2_Lines.SetCurrentLine(ByVal LineNum As Long)
AttributeGroup.AttributeGroupCollection : AttributeGroupCollection [R]
AttributeGroup.Code : Long [R]
AttributeGroup.Locked : BoYesNoEnum [R]
AttributeGroup.Name : String [R/W]
AttributeGroup.FromXMLFile(ByVal bstrFileName As String)
AttributeGroup.FromXMLString(ByVal bstrXML As String)
AttributeGroup.GetXMLSchema() -> String
AttributeGroup.ToXMLFile(ByVal bstrFileName As String)
AttributeGroup.ToXMLString() -> String
AttributeGroupCollection.Count : Long [R]
AttributeGroupCollection.Add() -> AttributeGroupLine
AttributeGroupCollection.GetXMLSchema() -> String
AttributeGroupCollection.Item(ByVal vtIndex As Variant) -> AttributeGroupLine
AttributeGroupCollection.ToXMLFile(ByVal bstrFileName As String)
AttributeGroupCollection.ToXMLString() -> String
AttributeGroupLine.AttributeID : Long [R/W]
AttributeGroupLine.AttributeName : String [R/W]
AttributeGroupLine.Code : Long [R]
AttributeGroupLine.DefaultValue : String [R/W]
AttributeGroupLine.FieldType : AttributeGroupFieldTypeEnum [R]
AttributeGroupLine.SortNumber : Long [R/W]
AttributeGroupLine.FromXMLFile(ByVal bstrFileName As String)
AttributeGroupLine.FromXMLString(ByVal bstrXML As String)
AttributeGroupLine.GetXMLSchema() -> String
AttributeGroupLine.ToXMLFile(ByVal bstrFileName As String)
AttributeGroupLine.ToXMLString() -> String
AttributeGroupParams.Code : Long [R/W]
AttributeGroupParams.Name : String [R]
AttributeGroupParams.FromXMLFile(ByVal bstrFileName As String)
AttributeGroupParams.FromXMLString(ByVal bstrXML As String)
AttributeGroupParams.GetXMLSchema() -> String
AttributeGroupParams.ToXMLFile(ByVal bstrFileName As String)
AttributeGroupParams.ToXMLString() -> String
AttributeGroupParamsCollection.Count : Long [R]
AttributeGroupParamsCollection.Add() -> AttributeGroupParams
AttributeGroupParamsCollection.GetXMLSchema() -> String
AttributeGroupParamsCollection.Item(ByVal vtIndex As Variant) -> AttributeGroupParams
AttributeGroupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
AttributeGroupParamsCollection.ToXMLString() -> String
AttributeGroupsService.Add(ByVal pIAttributeGroup As AttributeGroup) -> AttributeGroupParams
AttributeGroupsService.Delete(ByVal pIAttributeGroupParams As AttributeGroupParams)
AttributeGroupsService.Get(ByVal pIAttributeGroupParams As AttributeGroupParams) -> AttributeGroup
AttributeGroupsService.GetDataInterface(ByVal enumMSDI As AttributeGroupsServiceDataInterfaces) -> Object
AttributeGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
AttributeGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
AttributeGroupsService.GetList() -> AttributeGroupParamsCollection
AttributeGroupsService.Update(ByVal pIAttributeGroup As AttributeGroup)
BankChargesAllocationCode.Code : String [R/W]
BankChargesAllocationCode.Description : String [R/W]
BankChargesAllocationCode.FromXMLFile(ByVal bstrFileName As String)
BankChargesAllocationCode.FromXMLString(ByVal bstrXML As String)
BankChargesAllocationCode.GetXMLSchema() -> String
BankChargesAllocationCode.ToXMLFile(ByVal bstrFileName As String)
BankChargesAllocationCode.ToXMLString() -> String
BankChargesAllocationCodeParams.Code : String [R/W]
BankChargesAllocationCodeParams.Description : String [R]
BankChargesAllocationCodeParams.FromXMLFile(ByVal bstrFileName As String)
BankChargesAllocationCodeParams.FromXMLString(ByVal bstrXML As String)
BankChargesAllocationCodeParams.GetXMLSchema() -> String
BankChargesAllocationCodeParams.ToXMLFile(ByVal bstrFileName As String)
BankChargesAllocationCodeParams.ToXMLString() -> String
BankChargesAllocationCodesParams.Count : Long [R]
BankChargesAllocationCodesParams.Add() -> BankChargesAllocationCodeParams
BankChargesAllocationCodesParams.GetXMLSchema() -> String
BankChargesAllocationCodesParams.Item(ByVal vtIndex As Variant) -> BankChargesAllocationCodeParams
BankChargesAllocationCodesParams.ToXMLFile(ByVal bstrFileName As String)
BankChargesAllocationCodesParams.ToXMLString() -> String
BankChargesAllocationCodesService.AddBankChargesAllocationCode(ByVal pIBankChargesAllocationCode As BankChargesAllocationCode) -> BankChargesAllocationCodeParams
BankChargesAllocationCodesService.DeleteBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams)
BankChargesAllocationCodesService.GetBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams) -> BankChargesAllocationCode
BankChargesAllocationCodesService.GetBankChargesAllocationCodeList() -> BankChargesAllocationCodesParams
BankChargesAllocationCodesService.GetDataInterface(ByVal enumMSDI As BankChargesAllocationCodesServiceDataInterfaces) -> Object
BankChargesAllocationCodesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BankChargesAllocationCodesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BankChargesAllocationCodesService.SetDefaultBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams)
BankChargesAllocationCodesService.UpdateBankChargesAllocationCode(ByVal pIBankChargesAllocationCode As BankChargesAllocationCode)
BankPages.AccountCode : String [R/W]
BankPages.AccountName : String [R]
BankPages.BankMatch : Long [R]
BankPages.BICSwiftCode : String [R/W]
BankPages.Browser : DataBrowser [R]
BankPages.CardCode : String [R/W]
BankPages.CardName : String [R/W]
BankPages.CreditAmount : Double [R/W]
BankPages.DataSource : String [R]
BankPages.DebitAmount : Double [R/W]
BankPages.DocNumberType : BoBpsDocTypes [R/W]
BankPages.DueDate : Date [R/W]
BankPages.ExternalCode : String [R/W]
BankPages.InvoiceNumber : Long [R/W]
BankPages.InvoiceNumberEx : String [R/W]
BankPages.Memo : String [R/W]
BankPages.PaymentCreated : BoYesNoEnum [R/W]
BankPages.PaymentReference : String [R/W]
BankPages.Reference : String [R/W]
BankPages.Sequence : Long [R]
BankPages.StatementNumber : Long [R/W]
BankPages.UserFields : UserFields [R]
BankPages.UserSignature : Long [R]
BankPages.VisualOrder : Long [R/W]
BankPages.Add() -> Long
BankPages.GetAsXML() -> String
BankPages.GetByKey(ByVal AccountCode As String, ByVal Sequence As Long) -> Boolean
BankPages.Remove() -> Long
BankPages.SaveToFile(ByVal FileName As String)
BankPages.SaveXML(ByRef FileName As String)
BankPages.Update() -> Long
Banks.AbsoluteEntry : Long [R]
Banks.AccountforOutgoingChecks : String [R]
Banks.BankCode : String [R/W]
Banks.BankName : String [R/W]
Banks.BranchforOutgoingChecks : String [R]
Banks.Browser : DataBrowser [R]
Banks.CountryCode : String [R/W]
Banks.DefaultBankAccountKey : Long [R/W]
Banks.IBAN : String [R/W]
Banks.NextCheckNumber : Long [R]
Banks.PostOffice : BoYesNoEnum [R/W]
Banks.SwiftNo : String [R/W]
Banks.UserFields : UserFields [R]
Banks.Add() -> Long
Banks.GetAsXML() -> String
Banks.GetByKey(ByVal lAbsEntry As Long) -> Boolean
Banks.Remove() -> Long
Banks.SaveToFile(ByVal bstrFileName As String)
Banks.SaveXML(ByRef pbstrFileName As String)
Banks.Update() -> Long
BankStatement.BankAccountKey : Long [R/W]
BankStatement.BankStatementFileHash : String [R/W]
BankStatement.BankStatementGUID : String [R/W]
BankStatement.BankStatementRows : BankStatementRows [R]
BankStatement.Currency : String [R/W]
BankStatement.EndingBalanceF : Double [R/W]
BankStatement.EndingBalanceL : Double [R/W]
BankStatement.Imported : BoYesNoEnum [R]
BankStatement.InternalNumber : Long [R]
BankStatement.StartingBalanceF : Double [R/W]
BankStatement.StartingBalanceL : Double [R/W]
BankStatement.StatementDate : Date [R/W]
BankStatement.StatementNumber : String [R/W]
BankStatement.Status : BankStatementStatusEnum [R]
BankStatement.FromXMLFile(ByVal bstrFileName As String)
BankStatement.FromXMLString(ByVal bstrXML As String)
BankStatement.GetXMLSchema() -> String
BankStatement.ToXMLFile(ByVal bstrFileName As String)
BankStatement.ToXMLString() -> String
BankStatementParams.BankAccountKey : Long [R]
BankStatementParams.Currency : String [R]
BankStatementParams.EndingBalanceF : Double [R]
BankStatementParams.EndingBalanceL : Double [R]
BankStatementParams.Imported : BoYesNoEnum [R]
BankStatementParams.InternalNumber : Long [R/W]
BankStatementParams.StartingBalanceF : Double [R]
BankStatementParams.StartingBalanceL : Double [R]
BankStatementParams.StatementDate : Date [R]
BankStatementParams.StatementNumber : String [R]
BankStatementParams.Status : BankStatementStatusEnum [R]
BankStatementParams.FromXMLFile(ByVal bstrFileName As String)
BankStatementParams.FromXMLString(ByVal bstrXML As String)
BankStatementParams.GetXMLSchema() -> String
BankStatementParams.ToXMLFile(ByVal bstrFileName As String)
BankStatementParams.ToXMLString() -> String
BankStatementRow.AccountName : String [R/W]
BankStatementRow.AccountNumber : String [R]
BankStatementRow.Balance : Double [R/W]
BankStatementRow.BankStmtDueDate : Date [R/W]
BankStatementRow.BankStmtLineDate : Date [R/W]
BankStatementRow.BPBankAccount : String [R/W]
BankStatementRow.BPBankCode : String [R/W]
BankStatementRow.BPBICSwiftCode : String [R/W]
BankStatementRow.BPCode : String [R/W]
BankStatementRow.BPName : String [R/W]
BankStatementRow.CreateMethod : CreateMethodEnum [R]
BankStatementRow.CreditAmountFC : Double [R/W]
BankStatementRow.CreditAmountLC : Double [R/W]
BankStatementRow.CreditCurrency : String [R/W]
BankStatementRow.DebitAmountFC : Double [R/W]
BankStatementRow.DebitAmountLC : Double [R/W]
BankStatementRow.Details : String [R/W]
BankStatementRow.Details2 : String [R/W]
BankStatementRow.DocNumType : BoBpsDocTypes [R/W]
BankStatementRow.DocumentType : BankStatementDocTypeEnum [R]
BankStatementRow.DueDate : Date [R/W]
BankStatementRow.ExchangeRate : Double [R/W]
BankStatementRow.ExternalBankStatementNo : Long [R]
BankStatementRow.ExternalCode : String [R/W]
BankStatementRow.FeeDistributionRule : String [R/W]
BankStatementRow.FeeDistributionRule2 : String [R/W]
BankStatementRow.FeeDistributionRule3 : String [R/W]
BankStatementRow.FeeDistributionRule4 : String [R/W]
BankStatementRow.FeeDistributionRule5 : String [R/W]
BankStatementRow.FeeOnTheLine : Double [R/W]
BankStatementRow.FeeProfitCenter : String [R]
BankStatementRow.FeeProject : String [R]
BankStatementRow.FolioNumber : Long [R/W]
BankStatementRow.FolioPrefixString : String [R/W]
BankStatementRow.GLAccountforFee : String [R]
BankStatementRow.IBANofBPBankAccount : String [R/W]
BankStatementRow.InternalBankOpCode : Long [R]
BankStatementRow.JournalEntryID : Long [R]
BankStatementRow.MultiplePayments : MultiplePayments [R]
BankStatementRow.PaymentID : Long [R]
BankStatementRow.PaymentReferenceNo : String [R/W]
BankStatementRow.PostingMethod : PostingMethodEnum [R]
BankStatementRow.ReconciliationNo : Long [R]
BankStatementRow.Reference : String [R/W]
BankStatementRow.RowStatus : String [R]
BankStatementRow.SequenceNo : Long [R]
BankStatementRow.Source : BankStatementRowSourceEnum [R]
BankStatementRow.StatementNumber : Long [R]
BankStatementRow.UserFields : Fields [R]
BankStatementRow.VATAmountFC : Double [R/W]
BankStatementRow.VATAmountLC : Double [R/W]
BankStatementRow.VisualOrder : Long [R/W]
BankStatementRow.FromXMLFile(ByVal bstrFileName As String)
BankStatementRow.FromXMLString(ByVal bstrXML As String)
BankStatementRow.GetXMLSchema() -> String
BankStatementRow.ToXMLFile(ByVal bstrFileName As String)
BankStatementRow.ToXMLString() -> String
BankStatementRows.Count : Long [R]
BankStatementRows.Add() -> BankStatementRow
BankStatementRows.GetXMLSchema() -> String
BankStatementRows.Item(ByVal vtIndex As Variant) -> BankStatementRow
BankStatementRows.Remove(ByVal vtIndex As Variant)
BankStatementRows.ToXMLFile(ByVal bstrFileName As String)
BankStatementRows.ToXMLString() -> String
BankStatements.Count : Long [R]
BankStatements.Add() -> BankStatement
BankStatements.GetXMLSchema() -> String
BankStatements.Item(ByVal vtIndex As Variant) -> BankStatement
BankStatements.ToXMLFile(ByVal bstrFileName As String)
BankStatements.ToXMLString() -> String
BankStatementsFilter.Account : String [R/W]
BankStatementsFilter.Bank : String [R/W]
BankStatementsFilter.Country : String [R/W]
BankStatementsFilter.FromXMLFile(ByVal bstrFileName As String)
BankStatementsFilter.FromXMLString(ByVal bstrXML As String)
BankStatementsFilter.GetXMLSchema() -> String
BankStatementsFilter.ToXMLFile(ByVal bstrFileName As String)
BankStatementsFilter.ToXMLString() -> String
BankStatementsImportFile.Account : String [R/W]
BankStatementsImportFile.Bank : String [R/W]
BankStatementsImportFile.Country : String [R/W]
BankStatementsImportFile.FileName : String [R/W]
BankStatementsImportFile.FromXMLFile(ByVal bstrFileName As String)
BankStatementsImportFile.FromXMLString(ByVal bstrXML As String)
BankStatementsImportFile.GetXMLSchema() -> String
BankStatementsImportFile.ToXMLFile(ByVal bstrFileName As String)
BankStatementsImportFile.ToXMLString() -> String
BankStatementsParams.Count : Long [R]
BankStatementsParams.Add() -> BankStatementParams
BankStatementsParams.GetXMLSchema() -> String
BankStatementsParams.Item(ByVal vtIndex As Variant) -> BankStatementParams
BankStatementsParams.ToXMLFile(ByVal bstrFileName As String)
BankStatementsParams.ToXMLString() -> String
BankStatementsService.AddBankStatement(ByVal pIBankStatement As BankStatement) -> BankStatementParams
BankStatementsService.DeleteBankStatement(ByVal pIBankStatementParams As BankStatementParams)
BankStatementsService.GetBankStatement(ByVal pIBankStatementParams As BankStatementParams) -> BankStatement
BankStatementsService.GetBankStatementList(ByVal pIBankStatementsFilter As BankStatementsFilter) -> BankStatementsParams
BankStatementsService.GetDataInterface(ByVal enumMSDI As BankStatementsServiceDataInterfaces) -> Object
BankStatementsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BankStatementsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BankStatementsService.UpdateBankStatement(ByVal pIBankStatement As BankStatement)
BarCode.AbsEntry : Long [R]
BarCode.BarCode : String [R/W]
BarCode.FreeText : String [R/W]
BarCode.ItemNo : String [R/W]
BarCode.UoMEntry : Long [R/W]
BarCode.FromXMLFile(ByVal bstrFileName As String)
BarCode.FromXMLString(ByVal bstrXML As String)
BarCode.GetXMLSchema() -> String
BarCode.ToXMLFile(ByVal bstrFileName As String)
BarCode.ToXMLString() -> String
BarCodeParams.AbsEntry : Long [R/W]
BarCodeParams.BarCode : String [R]
BarCodeParams.ItemNo : String [R]
BarCodeParams.UoMEntry : Long [R]
BarCodeParams.FromXMLFile(ByVal bstrFileName As String)
BarCodeParams.FromXMLString(ByVal bstrXML As String)
BarCodeParams.GetXMLSchema() -> String
BarCodeParams.ToXMLFile(ByVal bstrFileName As String)
BarCodeParams.ToXMLString() -> String
BarCodeParamsCollection.Count : Long [R]
BarCodeParamsCollection.Add() -> BarCodeParams
BarCodeParamsCollection.GetXMLSchema() -> String
BarCodeParamsCollection.Item(ByVal vtIndex As Variant) -> BarCodeParams
BarCodeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
BarCodeParamsCollection.ToXMLString() -> String
BarCodesService.Add(ByVal pIBarcode As BarCode) -> BarCodeParams
BarCodesService.Delete(ByVal pIBarcodeParams As BarCodeParams)
BarCodesService.Get(ByVal pIBarcodeParams As BarCodeParams) -> BarCode
BarCodesService.GetDataInterface(ByVal enumMSDI As BarCodesServiceDataInterfaces) -> Object
BarCodesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BarCodesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BarCodesService.GetList() -> BarCodeParamsCollection
BarCodesService.Update(ByVal pIBarcode As BarCode)
BatchNumberDetail.AdmissionDate : Date [R/W]
BatchNumberDetail.Batch : String [R]
BatchNumberDetail.BatchAttribute1 : String [R/W]
BatchNumberDetail.BatchAttribute2 : String [R/W]
BatchNumberDetail.Details : String [R/W]
BatchNumberDetail.DocEntry : Long [R]
BatchNumberDetail.ExpirationDate : Date [R/W]
BatchNumberDetail.ItemCode : String [R]
BatchNumberDetail.ItemDescription : String [R]
BatchNumberDetail.ManufacturingDate : Date [R/W]
BatchNumberDetail.Status : BoDefaultBatchStatus [R/W]
BatchNumberDetail.SystemNumber : Long [R]
BatchNumberDetail.UserFields : Fields [R]
BatchNumberDetail.FromXMLFile(ByVal bstrFileName As String)
BatchNumberDetail.FromXMLString(ByVal bstrXML As String)
BatchNumberDetail.GetXMLSchema() -> String
BatchNumberDetail.ToXMLFile(ByVal bstrFileName As String)
BatchNumberDetail.ToXMLString() -> String
BatchNumberDetailParams.DocEntry : Long [R/W]
BatchNumberDetailParams.FromXMLFile(ByVal bstrFileName As String)
BatchNumberDetailParams.FromXMLString(ByVal bstrXML As String)
BatchNumberDetailParams.GetXMLSchema() -> String
BatchNumberDetailParams.ToXMLFile(ByVal bstrFileName As String)
BatchNumberDetailParams.ToXMLString() -> String
BatchNumberDetailsService.Get(ByVal pIBatchNumberDetailParams As BatchNumberDetailParams) -> BatchNumberDetail
BatchNumberDetailsService.GetDataInterface(ByVal enumMSDI As BatchNumberDetailsServiceDataInterfaces) -> Object
BatchNumberDetailsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BatchNumberDetailsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BatchNumberDetailsService.Update(ByVal pIBatchNumberDetail As BatchNumberDetail)
BatchNumbers.AddmisionDate : Date [R/W]
BatchNumbers.BaseLineNumber : Long [R/W]
BatchNumbers.BatchNumber : String [R/W]
BatchNumbers.Count : Long [R]
BatchNumbers.ExpiryDate : Date [R/W]
BatchNumbers.InternalSerialNumber : String [R/W]
BatchNumbers.ItemCode : String [R/W]
BatchNumbers.Location : String [R/W]
BatchNumbers.ManufacturerSerialNumber : String [R/W]
BatchNumbers.ManufacturingDate : Date [R/W]
BatchNumbers.Notes : String [R/W]
BatchNumbers.Quantity : Double [R/W]
BatchNumbers.SystemSerialNumber : Long [R/W]
BatchNumbers.TrackingNote : Long [R/W]
BatchNumbers.TrackingNoteLine : Long [R/W]
BatchNumbers.UserFields : UserFields [R]
BatchNumbers.Add()
BatchNumbers.SetCurrentLine(ByVal LineNum As Long)
BillOfExchange.BillOfExchangeDueDate : Date [R/W]
BillOfExchange.BillOfExchangeNo : String [R/W]
BillOfExchange.BPBankAct : String [R/W]
BillOfExchange.BPBankCode : String [R/W]
BillOfExchange.BPBankCountry : String [R/W]
BillOfExchange.ControlKey : String [R]
BillOfExchange.Details : String [R/W]
BillOfExchange.DiscountAmount : Double [R/W]
BillOfExchange.DiscountDate : Date [R/W]
BillOfExchange.FineAmount : Double [R/W]
BillOfExchange.FineDate : Date [R/W]
BillOfExchange.FolioNumber : Long [R/W]
BillOfExchange.FolioPrefixString : String [R/W]
BillOfExchange.InterestAmount : Double [R/W]
BillOfExchange.InterestDate : Date [R/W]
BillOfExchange.IOFAmount : Double [R/W]
BillOfExchange.LastPageFolioNumber : Long [R]
BillOfExchange.OtherExpensesAmount : Double [R/W]
BillOfExchange.OtherIncomesAmount : Double [R/W]
BillOfExchange.PaymentEngineStatus1 : String [R/W]
BillOfExchange.PaymentEngineStatus2 : String [R/W]
BillOfExchange.PaymentEngineStatus3 : String [R/W]
BillOfExchange.PaymentMethodCode : String [R/W]
BillOfExchange.ReferenceNo : String [R/W]
BillOfExchange.Remarks : String [R/W]
BillOfExchange.ServiceFeeAmount : Double [R/W]
BillOfExchange.StampTaxAmount : Double [R/W]
BillOfExchange.StampTaxCode : String [R/W]
BillOfExchange.UserFields : UserFields [R]
BillOfExchangeTrans_BankPages.AccountCode : String [R/W]
BillOfExchangeTrans_BankPages.Sequence : Long [R/W]
BillOfExchangeTrans_BankPages.UserFields : UserFields [R]
BillOfExchangeTrans_Deposits.BankAccount : String [R/W]
BillOfExchangeTrans_Deposits.BankBranch : String [R/W]
BillOfExchangeTrans_Deposits.BankCountry : String [R/W]
BillOfExchangeTrans_Deposits.BankDepositAccount : String [R/W]
BillOfExchangeTrans_Deposits.DepositNorm : String [R/W]
BillOfExchangeTrans_Deposits.PostingType : BoDepositPostingTypes [R/W]
BillOfExchangeTrans_Deposits.UserFields : UserFields [R]
BillOfExchangeTransaction.BankPages : BillOfExchangeTrans_BankPages [R]
BillOfExchangeTransaction.BOETransactionkey : Long [R]
BillOfExchangeTransaction.Browser : DataBrowser [R]
BillOfExchangeTransaction.Deposits : BillOfExchangeTrans_Deposits [R]
BillOfExchangeTransaction.IsBoeReconciled : BoYesNoEnum [R/W]
BillOfExchangeTransaction.Lines : BillOfExchangeTransaction_Lines [R]
BillOfExchangeTransaction.PostingDate : Date [R/W]
BillOfExchangeTransaction.StatusFrom : BoBOTFromStatus [R/W]
BillOfExchangeTransaction.StatusTo : BoBOTToStatus [R/W]
BillOfExchangeTransaction.TaxDate : Date [R/W]
BillOfExchangeTransaction.TransactionDate : Date [R]
BillOfExchangeTransaction.TransactionNumber : Long [R]
BillOfExchangeTransaction.TransactionTime : Date [R]
BillOfExchangeTransaction.UserFields : UserFields [R]
BillOfExchangeTransaction.Add() -> Long
BillOfExchangeTransaction.GetAsXML() -> String
BillOfExchangeTransaction.GetByKey(ByVal InternalKey As Long) -> Boolean
BillOfExchangeTransaction.SaveToFile(ByVal FileName As String)
BillOfExchangeTransaction.SaveXML(ByRef FileName As String)
BillOfExchangeTransaction_Lines.BillOfExchangeDueDate : Date [R]
BillOfExchangeTransaction_Lines.BillOfExchangeNo : Long [R/W]
BillOfExchangeTransaction_Lines.BillOfExchangeType : BoBOETypes [R/W]
BillOfExchangeTransaction_Lines.Count : Long [R]
BillOfExchangeTransaction_Lines.UserFields : UserFields [R]
BillOfExchangeTransaction_Lines.Add()
BillOfExchangeTransaction_Lines.SetCurrentLine(ByVal LineNum As Long)
BinLocation.AbsEntry : Long [R]
BinLocation.AlternativeSortCode : String [R/W]
BinLocation.Attribute1 : String [R/W]
BinLocation.Attribute10 : String [R/W]
BinLocation.Attribute2 : String [R/W]
BinLocation.Attribute3 : String [R/W]
BinLocation.Attribute4 : String [R/W]
BinLocation.Attribute5 : String [R/W]
BinLocation.Attribute6 : String [R/W]
BinLocation.Attribute7 : String [R/W]
BinLocation.Attribute8 : String [R/W]
BinLocation.Attribute9 : String [R/W]
BinLocation.BarCode : String [R/W]
BinLocation.BatchRestrictions : BinRestrictionBatchEnum [R/W]
BinLocation.BinCode : String [R]
BinLocation.DateRestrictionChanged : Date [R]
BinLocation.Description : String [R/W]
BinLocation.ExcludeAutoAllocOnIssue : BoYesNoEnum [R/W]
BinLocation.Inactive : BoYesNoEnum [R/W]
BinLocation.IsSystemBin : BoYesNoEnum [R]
BinLocation.MaximumQty : Double [R/W]
BinLocation.MaximumWeight : Double [R/W]
BinLocation.MaximumWeight1 : Double [R/W]
BinLocation.MaximumWeightUnit : Long [R/W]
BinLocation.MaximumWeightUnit1 : Long [R/W]
BinLocation.MinimumQty : Double [R/W]
BinLocation.ReceivingBinLocation : BoYesNoEnum [R/W]
BinLocation.RestrictedItemType : BinRestrictItemEnum [R/W]
BinLocation.RestrictedTransType : BinRestrictTransactionEnum [R/W]
BinLocation.RestrictedUoMType : BinRestrictUoMEnum [R/W]
BinLocation.RestrictionReason : String [R/W]
BinLocation.SpecificItem : String [R/W]
BinLocation.SpecificItemGroup : Long [R/W]
BinLocation.SpecificUoM : Long [R/W]
BinLocation.SpecificUoMGroup : Long [R/W]
BinLocation.Sublevel1 : String [R/W]
BinLocation.Sublevel2 : String [R/W]
BinLocation.Sublevel3 : String [R/W]
BinLocation.Sublevel4 : String [R/W]
BinLocation.UserFields : Fields [R]
BinLocation.Warehouse : String [R/W]
BinLocation.FromXMLFile(ByVal bstrFileName As String)
BinLocation.FromXMLString(ByVal bstrXML As String)
BinLocation.GetXMLSchema() -> String
BinLocation.ToXMLFile(ByVal bstrFileName As String)
BinLocation.ToXMLString() -> String
BinLocationAttribute.AbsEntry : Long [R]
BinLocationAttribute.Attribute : Long [R/W]
BinLocationAttribute.Code : String [R/W]
BinLocationAttribute.FromXMLFile(ByVal bstrFileName As String)
BinLocationAttribute.FromXMLString(ByVal bstrXML As String)
BinLocationAttribute.GetXMLSchema() -> String
BinLocationAttribute.ToXMLFile(ByVal bstrFileName As String)
BinLocationAttribute.ToXMLString() -> String
BinLocationAttributeCollectionParams.Count : Long [R]
BinLocationAttributeCollectionParams.Add() -> BinLocationAttributeParams
BinLocationAttributeCollectionParams.GetXMLSchema() -> String
BinLocationAttributeCollectionParams.Item(ByVal vtIndex As Variant) -> BinLocationAttributeParams
BinLocationAttributeCollectionParams.ToXMLFile(ByVal bstrFileName As String)
BinLocationAttributeCollectionParams.ToXMLString() -> String
BinLocationAttributeParams.AbsEntry : Long [R/W]
BinLocationAttributeParams.Attribute : Long [R/W]
BinLocationAttributeParams.Code : String [R/W]
BinLocationAttributeParams.FromXMLFile(ByVal bstrFileName As String)
BinLocationAttributeParams.FromXMLString(ByVal bstrXML As String)
BinLocationAttributeParams.GetXMLSchema() -> String
BinLocationAttributeParams.ToXMLFile(ByVal bstrFileName As String)
BinLocationAttributeParams.ToXMLString() -> String
BinLocationAttributesService.Add(ByVal pIBinLocationAttribute As BinLocationAttribute) -> BinLocationAttributeParams
BinLocationAttributesService.Delete(ByVal pIBinLocationAttributeParams As BinLocationAttributeParams)
BinLocationAttributesService.Get(ByVal pIBinLocationAttributeParams As BinLocationAttributeParams) -> BinLocationAttribute
BinLocationAttributesService.GetDataInterface(ByVal enumMSDI As BinLocationAttributesServiceDataInterfaces) -> Object
BinLocationAttributesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BinLocationAttributesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BinLocationAttributesService.GetList() -> BinLocationAttributeCollectionParams
BinLocationAttributesService.Update(ByVal pIBinLocationAttribute As BinLocationAttribute)
BinLocationCollectionParams.Count : Long [R]
BinLocationCollectionParams.Add() -> BinLocationParams
BinLocationCollectionParams.GetXMLSchema() -> String
BinLocationCollectionParams.Item(ByVal vtIndex As Variant) -> BinLocationParams
BinLocationCollectionParams.ToXMLFile(ByVal bstrFileName As String)
BinLocationCollectionParams.ToXMLString() -> String
BinLocationField.AbsEntry : Long [R]
BinLocationField.Activated : BoYesNoEnum [R/W]
BinLocationField.DefaultFieldName : String [R]
BinLocationField.FieldNumber : Long [R]
BinLocationField.FieldType : BinLocationFieldTypeEnum [R]
BinLocationField.Name : String [R/W]
BinLocationField.FromXMLFile(ByVal bstrFileName As String)
BinLocationField.FromXMLString(ByVal bstrXML As String)
BinLocationField.GetXMLSchema() -> String
BinLocationField.ToXMLFile(ByVal bstrFileName As String)
BinLocationField.ToXMLString() -> String
BinLocationFieldCollectionParams.Count : Long [R]
BinLocationFieldCollectionParams.Add() -> BinLocationFieldParams
BinLocationFieldCollectionParams.GetXMLSchema() -> String
BinLocationFieldCollectionParams.Item(ByVal vtIndex As Variant) -> BinLocationFieldParams
BinLocationFieldCollectionParams.ToXMLFile(ByVal bstrFileName As String)
BinLocationFieldCollectionParams.ToXMLString() -> String
BinLocationFieldParams.AbsEntry : Long [R/W]
BinLocationFieldParams.FromXMLFile(ByVal bstrFileName As String)
BinLocationFieldParams.FromXMLString(ByVal bstrXML As String)
BinLocationFieldParams.GetXMLSchema() -> String
BinLocationFieldParams.ToXMLFile(ByVal bstrFileName As String)
BinLocationFieldParams.ToXMLString() -> String
BinLocationFieldsService.Get(ByVal pIBinLocationFieldParams As BinLocationFieldParams) -> BinLocationField
BinLocationFieldsService.GetDataInterface(ByVal enumMSDI As BinLocationFieldsServiceDataInterfaces) -> Object
BinLocationFieldsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BinLocationFieldsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BinLocationFieldsService.GetList() -> BinLocationFieldCollectionParams
BinLocationFieldsService.Update(ByVal pIBinLocationField As BinLocationField)
BinLocationParams.AbsEntry : Long [R/W]
BinLocationParams.BinCode : String [R/W]
BinLocationParams.FromXMLFile(ByVal bstrFileName As String)
BinLocationParams.FromXMLString(ByVal bstrXML As String)
BinLocationParams.GetXMLSchema() -> String
BinLocationParams.ToXMLFile(ByVal bstrFileName As String)
BinLocationParams.ToXMLString() -> String
BinLocationsService.Add(ByVal pIBinLocation As BinLocation) -> BinLocationParams
BinLocationsService.Delete(ByVal pIBinLocationParams As BinLocationParams)
BinLocationsService.Get(ByVal pIBinLocationParams As BinLocationParams) -> BinLocation
BinLocationsService.GetDataInterface(ByVal enumMSDI As BinLocationsServiceDataInterfaces) -> Object
BinLocationsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BinLocationsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BinLocationsService.GetList() -> BinLocationCollectionParams
BinLocationsService.Update(ByVal pIBinLocation As BinLocation)
BlanketAgreement.AgreementMethod : BlanketAgreementMethodEnum [R/W]
BlanketAgreement.AgreementNo : Long [R]
BlanketAgreement.AgreementType : BlanketAgreementTypeEnum [R/W]
BlanketAgreement.AmendmentTo : Long [R/W]
BlanketAgreement.AttachmentEntry : Long [R/W]
BlanketAgreement.BlanketAgreements_ItemsLines : BlanketAgreements_ItemsLines [R]
BlanketAgreement.BPCode : String [R/W]
BlanketAgreement.BPCurrency : String [R/W]
BlanketAgreement.BPName : String [R]
BlanketAgreement.ContactPersonCode : Long [R/W]
BlanketAgreement.Description : String [R/W]
BlanketAgreement.DocNum : Long [R/W]
BlanketAgreement.EndDate : Date [R/W]
BlanketAgreement.ExchangeRate : Double [R/W]
BlanketAgreement.HandWritten : BoYesNoEnum [R/W]
BlanketAgreement.IgnorePricesInAgreement : BoYesNoEnum [R]
BlanketAgreement.NumAtCard : String [R/W]
BlanketAgreement.Owner : Long [R/W]
BlanketAgreement.PaymentMethod : String [R/W]
BlanketAgreement.PaymentTerms : Long [R/W]
BlanketAgreement.PeriodIndicator : String [R]
BlanketAgreement.PriceList : Long [R/W]
BlanketAgreement.PriceMode : PriceModeEnum [R/W]
BlanketAgreement.Project : String [R/W]
BlanketAgreement.Remarks : String [R/W]
BlanketAgreement.RemindTime : Long [R/W]
BlanketAgreement.RemindUnit : BoRemindUnits [R/W]
BlanketAgreement.Renewal : BoYesNoEnum [R/W]
BlanketAgreement.SAPPassport : String [R]
BlanketAgreement.Series : Long [R/W]
BlanketAgreement.SettlementProbability : Double [R/W]
BlanketAgreement.ShippingType : Long [R/W]
BlanketAgreement.SigningDate : Date [R/W]
BlanketAgreement.StartDate : Date [R/W]
BlanketAgreement.Status : BlanketAgreementStatusEnum [R/W]
BlanketAgreement.TerminateDate : Date [R/W]
BlanketAgreement.UserFields : Fields [R]
BlanketAgreement.FromXMLFile(ByVal bstrFileName As String)
BlanketAgreement.FromXMLString(ByVal bstrXML As String)
BlanketAgreement.GetXMLSchema() -> String
BlanketAgreement.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreement.ToXMLString() -> String
BlanketAgreementParams.AgreementNo : Long [R/W]
BlanketAgreementParams.FromXMLFile(ByVal bstrFileName As String)
BlanketAgreementParams.FromXMLString(ByVal bstrXML As String)
BlanketAgreementParams.GetXMLSchema() -> String
BlanketAgreementParams.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreementParams.ToXMLString() -> String
BlanketAgreements_DetailsLine.AgreementEffectiveRowNumber : Long [R]
BlanketAgreements_DetailsLine.AgreementNo : Long [R]
BlanketAgreements_DetailsLine.AgreementRowNumber : Long [R]
BlanketAgreements_DetailsLine.ConsumeSalesForecast : BoYesNoEnum [R/W]
BlanketAgreements_DetailsLine.FreeText : String [R/W]
BlanketAgreements_DetailsLine.Frequency : BlanketAgreementDatePeriodsEnum [R/W]
BlanketAgreements_DetailsLine.From : Date [R/W]
BlanketAgreements_DetailsLine.PlannedAmountFC : Double [R/W]
BlanketAgreements_DetailsLine.PlannedAmountLC : Double [R/W]
BlanketAgreements_DetailsLine.Quantity : Double [R/W]
BlanketAgreements_DetailsLine.ReleaseInformation : String [R/W]
BlanketAgreements_DetailsLine.To : Date [R/W]
BlanketAgreements_DetailsLine.UserFields : Fields [R]
BlanketAgreements_DetailsLine.Warehouse : String [R/W]
BlanketAgreements_DetailsLine.FromXMLFile(ByVal bstrFileName As String)
BlanketAgreements_DetailsLine.FromXMLString(ByVal bstrXML As String)
BlanketAgreements_DetailsLine.GetXMLSchema() -> String
BlanketAgreements_DetailsLine.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreements_DetailsLine.ToXMLString() -> String
BlanketAgreements_DetailsLines.Count : Long [R]
BlanketAgreements_DetailsLines.Add() -> BlanketAgreements_DetailsLine
BlanketAgreements_DetailsLines.GetXMLSchema() -> String
BlanketAgreements_DetailsLines.Item(ByVal vtIndex As Variant) -> BlanketAgreements_DetailsLine
BlanketAgreements_DetailsLines.Remove(ByVal vtIndex As Variant)
BlanketAgreements_DetailsLines.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreements_DetailsLines.ToXMLString() -> String
BlanketAgreements_ItemsLine.AgreementNo : Long [R]
BlanketAgreements_ItemsLine.AgreementRowNumber : Long [R]
BlanketAgreements_ItemsLine.BlanketAgreements_DetailsLines : BlanketAgreements_DetailsLines [R]
BlanketAgreements_ItemsLine.CumulativeAmountFC : Double [R]
BlanketAgreements_ItemsLine.CumulativeAmountLC : Double [R]
BlanketAgreements_ItemsLine.CumulativeQuantity : Double [R]
BlanketAgreements_ItemsLine.CumulativeVATAmountFC : Double [R]
BlanketAgreements_ItemsLine.CumulativeVATAmountLC : Double [R]
BlanketAgreements_ItemsLine.EndOfWarranty : Date [R/W]
BlanketAgreements_ItemsLine.FreeText : String [R/W]
BlanketAgreements_ItemsLine.InventoryUOM : String [R]
BlanketAgreements_ItemsLine.ItemDescription : String [R/W]
BlanketAgreements_ItemsLine.ItemGroup : Long [R]
BlanketAgreements_ItemsLine.ItemNo : String [R/W]
BlanketAgreements_ItemsLine.LineDiscount : Double [R/W]
BlanketAgreements_ItemsLine.PlannedAmountFC : Double [R/W]
BlanketAgreements_ItemsLine.PlannedAmountLC : Double [R/W]
BlanketAgreements_ItemsLine.PlannedQuantity : Double [R/W]
BlanketAgreements_ItemsLine.PlannedVATAmountFC : Double [R/W]
BlanketAgreements_ItemsLine.PlannedVATAmountLC : Double [R/W]
BlanketAgreements_ItemsLine.PortionOfReturns : Double [R/W]
BlanketAgreements_ItemsLine.PriceCurrency : String [R/W]
BlanketAgreements_ItemsLine.Project : String [R/W]
BlanketAgreements_ItemsLine.ShippingType : Long [R/W]
BlanketAgreements_ItemsLine.TaxCode : String [R/W]
BlanketAgreements_ItemsLine.TaxRate : Double [R]
BlanketAgreements_ItemsLine.UndeliveredCumulativeAmountFC : Double [R]
BlanketAgreements_ItemsLine.UndeliveredCumulativeAmountLC : Double [R]
BlanketAgreements_ItemsLine.UndeliveredCumulativeQuantity : Double [R]
BlanketAgreements_ItemsLine.UnitPrice : Double [R/W]
BlanketAgreements_ItemsLine.UnitsOfMeasurement : Double [R]
BlanketAgreements_ItemsLine.UoMCode : String [R]
BlanketAgreements_ItemsLine.UoMEntry : Long [R/W]
BlanketAgreements_ItemsLine.UserFields : Fields [R]
BlanketAgreements_ItemsLine.FromXMLFile(ByVal bstrFileName As String)
BlanketAgreements_ItemsLine.FromXMLString(ByVal bstrXML As String)
BlanketAgreements_ItemsLine.GetXMLSchema() -> String
BlanketAgreements_ItemsLine.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreements_ItemsLine.ToXMLString() -> String
BlanketAgreements_ItemsLines.Count : Long [R]
BlanketAgreements_ItemsLines.Add() -> BlanketAgreements_ItemsLine
BlanketAgreements_ItemsLines.GetXMLSchema() -> String
BlanketAgreements_ItemsLines.Item(ByVal vtIndex As Variant) -> BlanketAgreements_ItemsLine
BlanketAgreements_ItemsLines.Remove(ByVal vtIndex As Variant)
BlanketAgreements_ItemsLines.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreements_ItemsLines.ToXMLString() -> String
BlanketAgreementsDocument.AgreementRowNumber : Long [R]
BlanketAgreementsDocument.Discount : Double [R]
BlanketAgreementsDocument.DocStatus : BADocumentStatus [R]
BlanketAgreementsDocument.DocumentDate : Date [R]
BlanketAgreementsDocument.DocumentNo : Long [R]
BlanketAgreementsDocument.DocumentRowNumber : Long [R]
BlanketAgreementsDocument.DocumentType : BlanketAgreementDocTypeEnum [R]
BlanketAgreementsDocument.ItemDescription : String [R]
BlanketAgreementsDocument.ItemNo : String [R]
BlanketAgreementsDocument.Quantity : Double [R]
BlanketAgreementsDocument.RowStatus : BoStatus [R]
BlanketAgreementsDocument.UnitPrice : Double [R]
BlanketAgreementsDocument.UnitsOfMeasurement : Double [R]
BlanketAgreementsDocument.UoM : String [R]
BlanketAgreementsDocument.UoMCode : String [R]
BlanketAgreementsDocument.FromXMLFile(ByVal bstrFileName As String)
BlanketAgreementsDocument.FromXMLString(ByVal bstrXML As String)
BlanketAgreementsDocument.GetXMLSchema() -> String
BlanketAgreementsDocument.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreementsDocument.ToXMLString() -> String
BlanketAgreementsDocuments.Count : Long [R]
BlanketAgreementsDocuments.Add() -> BlanketAgreementsDocument
BlanketAgreementsDocuments.GetXMLSchema() -> String
BlanketAgreementsDocuments.Item(ByVal vtIndex As Variant) -> BlanketAgreementsDocument
BlanketAgreementsDocuments.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreementsDocuments.ToXMLString() -> String
BlanketAgreementsParams.Count : Long [R]
BlanketAgreementsParams.Add() -> BlanketAgreementParams
BlanketAgreementsParams.GetXMLSchema() -> String
BlanketAgreementsParams.Item(ByVal vtIndex As Variant) -> BlanketAgreementParams
BlanketAgreementsParams.ToXMLFile(ByVal bstrFileName As String)
BlanketAgreementsParams.ToXMLString() -> String
BlanketAgreementsService.AddBlanketAgreement(ByVal pIBlanketAgreement As BlanketAgreement) -> BlanketAgreementParams
BlanketAgreementsService.CancelBlanketAgreement(ByVal pIBlanketAgreementParams As BlanketAgreementParams)
BlanketAgreementsService.GetBlanketAgreement(ByVal pIBlanketAgreementParams As BlanketAgreementParams) -> BlanketAgreement
BlanketAgreementsService.GetBlanketAgreementList() -> BlanketAgreementsParams
BlanketAgreementsService.GetDataInterface(ByVal enumMSDI As BlanketAgreementsServiceDataInterfaces) -> Object
BlanketAgreementsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BlanketAgreementsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BlanketAgreementsService.GetRelatedDocuments(ByVal pIBlanketAgreementParams As BlanketAgreementParams) -> BlanketAgreementsDocuments
BlanketAgreementsService.UpdateBlanketAgreement(ByVal pIBlanketAgreement As BlanketAgreement)
Blob.Content : String [R/W]
Blob.FromXMLFile(ByVal bstrFileName As String)
Blob.FromXMLString(ByVal bstrXML As String)
Blob.GetXMLSchema() -> String
Blob.ToXMLFile(ByVal bstrFileName As String)
Blob.ToXMLString() -> String
BlobParams.BlobTableKeySegments : BlobTableKeySegments [R]
BlobParams.Field : String [R/W]
BlobParams.FileName : String [R/W]
BlobParams.Table : String [R/W]
BlobParams.FromXMLFile(ByVal bstrFileName As String)
BlobParams.FromXMLString(ByVal bstrXML As String)
BlobParams.GetXMLSchema() -> String
BlobParams.ToXMLFile(ByVal bstrFileName As String)
BlobParams.ToXMLString() -> String
BlobTableKeySegment.Name : String [R/W]
BlobTableKeySegment.Value : String [R/W]
BlobTableKeySegment.FromXMLFile(ByVal bstrFileName As String)
BlobTableKeySegment.FromXMLString(ByVal bstrXML As String)
BlobTableKeySegment.GetXMLSchema() -> String
BlobTableKeySegment.ToXMLFile(ByVal bstrFileName As String)
BlobTableKeySegment.ToXMLString() -> String
BlobTableKeySegments.Count : Long [R]
BlobTableKeySegments.Add() -> BlobTableKeySegment
BlobTableKeySegments.GetXMLSchema() -> String
BlobTableKeySegments.Item(ByVal vtIndex As Variant) -> BlobTableKeySegment
BlobTableKeySegments.ToXMLFile(ByVal bstrFileName As String)
BlobTableKeySegments.ToXMLString() -> String
BOEDocumentType.DocDescription : String [R/W]
BOEDocumentType.DocEntry : Long [R]
BOEDocumentType.DocType : String [R/W]
BOEDocumentType.FromXMLFile(ByVal bstrFileName As String)
BOEDocumentType.FromXMLString(ByVal bstrXML As String)
BOEDocumentType.GetXMLSchema() -> String
BOEDocumentType.ToXMLFile(ByVal bstrFileName As String)
BOEDocumentType.ToXMLString() -> String
BOEDocumentTypeParams.DocEntry : Long [R/W]
BOEDocumentTypeParams.DocType : String [R]
BOEDocumentTypeParams.FromXMLFile(ByVal bstrFileName As String)
BOEDocumentTypeParams.FromXMLString(ByVal bstrXML As String)
BOEDocumentTypeParams.GetXMLSchema() -> String
BOEDocumentTypeParams.ToXMLFile(ByVal bstrFileName As String)
BOEDocumentTypeParams.ToXMLString() -> String
BOEDocumentTypes.Count : Long [R]
BOEDocumentTypes.Add() -> BOEDocumentType
BOEDocumentTypes.GetXMLSchema() -> String
BOEDocumentTypes.Item(ByVal vtIndex As Variant) -> BOEDocumentType
BOEDocumentTypes.ToXMLFile(ByVal bstrFileName As String)
BOEDocumentTypes.ToXMLString() -> String
BOEDocumentTypesParams.Count : Long [R]
BOEDocumentTypesParams.Add() -> BOEDocumentTypeParams
BOEDocumentTypesParams.GetXMLSchema() -> String
BOEDocumentTypesParams.Item(ByVal vtIndex As Variant) -> BOEDocumentTypeParams
BOEDocumentTypesParams.ToXMLFile(ByVal bstrFileName As String)
BOEDocumentTypesParams.ToXMLString() -> String
BOEDocumentTypesService.AddBOEDocumentType(ByVal pIBOEDocumentType As BOEDocumentType) -> BOEDocumentTypeParams
BOEDocumentTypesService.DeleteBOEDocumentType(ByVal pIBOEDocumentTypeParams As BOEDocumentTypeParams)
BOEDocumentTypesService.GetBOEDocumentType(ByVal pIBOEDocumentTypeParams As BOEDocumentTypeParams) -> BOEDocumentType
BOEDocumentTypesService.GetBOEDocumentTypeList() -> BOEDocumentTypesParams
BOEDocumentTypesService.GetDataInterface(ByVal enumMSDI As BOEDocumentTypesServiceDataInterfaces) -> Object
BOEDocumentTypesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BOEDocumentTypesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BOEDocumentTypesService.UpdateBOEDocumentType(ByVal pIBOEDocumentType As BOEDocumentType)
BOEInstruction.InstructionCode : String [R/W]
BOEInstruction.InstructionDesc : String [R/W]
BOEInstruction.InstructionEntry : Long [R]
BOEInstruction.IsCancelInstruction : BoYesNoEnum [R/W]
BOEInstruction.FromXMLFile(ByVal bstrFileName As String)
BOEInstruction.FromXMLString(ByVal bstrXML As String)
BOEInstruction.GetXMLSchema() -> String
BOEInstruction.ToXMLFile(ByVal bstrFileName As String)
BOEInstruction.ToXMLString() -> String
BOEInstructionParams.InstructionCode : String [R]
BOEInstructionParams.InstructionEntry : Long [R/W]
BOEInstructionParams.FromXMLFile(ByVal bstrFileName As String)
BOEInstructionParams.FromXMLString(ByVal bstrXML As String)
BOEInstructionParams.GetXMLSchema() -> String
BOEInstructionParams.ToXMLFile(ByVal bstrFileName As String)
BOEInstructionParams.ToXMLString() -> String
BOEInstructions.Count : Long [R]
BOEInstructions.Add() -> BOEInstruction
BOEInstructions.GetXMLSchema() -> String
BOEInstructions.Item(ByVal vtIndex As Variant) -> BOEInstruction
BOEInstructions.ToXMLFile(ByVal bstrFileName As String)
BOEInstructions.ToXMLString() -> String
BOEInstructionsParams.Count : Long [R]
BOEInstructionsParams.Add() -> BOEInstructionParams
BOEInstructionsParams.GetXMLSchema() -> String
BOEInstructionsParams.Item(ByVal vtIndex As Variant) -> BOEInstructionParams
BOEInstructionsParams.ToXMLFile(ByVal bstrFileName As String)
BOEInstructionsParams.ToXMLString() -> String
BOEInstructionsService.AddBOEInstruction(ByVal pIBOEInstruction As BOEInstruction) -> BOEInstructionParams
BOEInstructionsService.DeleteBOEInstruction(ByVal pIBOEInstructionParams As BOEInstructionParams)
BOEInstructionsService.GetBOEInstruction(ByVal pIBOEInstructionParams As BOEInstructionParams) -> BOEInstruction
BOEInstructionsService.GetBOEInstructionList() -> BOEInstructionsParams
BOEInstructionsService.GetDataInterface(ByVal enumMSDI As BOEInstructionsServiceDataInterfaces) -> Object
BOEInstructionsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BOEInstructionsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BOEInstructionsService.UpdateBOEInstruction(ByVal pIBOEInstruction As BOEInstruction)
BOELine.AccountNumber : String [R]
BOELine.amount : Double [R]
BOELine.Bank : String [R]
BOELine.BOEKey : Long [R]
BOELine.BOENumber : Long [R]
BOELine.BOEStatus : BoBoeStatus [R]
BOELine.Branch : String [R]
BOELine.DueDate : Date [R]
BOELine.Transferred : BoYesNoEnum [R]
BOELine.FromXMLFile(ByVal bstrFileName As String)
BOELine.FromXMLString(ByVal bstrXML As String)
BOELine.GetXMLSchema() -> String
BOELine.ToXMLFile(ByVal bstrFileName As String)
BOELine.ToXMLString() -> String
BOELineParams.BOEKey : Long [R/W]
BOELineParams.FromXMLFile(ByVal bstrFileName As String)
BOELineParams.FromXMLString(ByVal bstrXML As String)
BOELineParams.GetXMLSchema() -> String
BOELineParams.ToXMLFile(ByVal bstrFileName As String)
BOELineParams.ToXMLString() -> String
BOELines.Count : Long [R]
BOELines.Add() -> BOELine
BOELines.GetXMLSchema() -> String
BOELines.Item(ByVal vtIndex As Variant) -> BOELine
BOELines.ToXMLFile(ByVal bstrFileName As String)
BOELines.ToXMLString() -> String
BOELinesParams.Count : Long [R]
BOELinesParams.Add() -> BOELineParams
BOELinesParams.GetXMLSchema() -> String
BOELinesParams.Item(ByVal vtIndex As Variant) -> BOELineParams
BOELinesParams.ToXMLFile(ByVal bstrFileName As String)
BOELinesParams.ToXMLString() -> String
BOELinesService.GetBOELine(ByVal pIBOELineParams As BOELineParams) -> BOELine
BOELinesService.GetDataInterface(ByVal enumMSDI As BOELinesServiceDataInterfaces) -> Object
BOELinesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BOELinesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BOEPortfolio.PortfolioCode : String [R/W]
BOEPortfolio.PortfolioDescription : String [R/W]
BOEPortfolio.PortfolioEntry : Long [R]
BOEPortfolio.PortfolioID : String [R/W]
BOEPortfolio.PortfolioNum : String [R/W]
BOEPortfolio.FromXMLFile(ByVal bstrFileName As String)
BOEPortfolio.FromXMLString(ByVal bstrXML As String)
BOEPortfolio.GetXMLSchema() -> String
BOEPortfolio.ToXMLFile(ByVal bstrFileName As String)
BOEPortfolio.ToXMLString() -> String
BOEPortfolioParams.PortfolioCode : String [R]
BOEPortfolioParams.PortfolioEntry : Long [R/W]
BOEPortfolioParams.PortfolioID : String [R]
BOEPortfolioParams.FromXMLFile(ByVal bstrFileName As String)
BOEPortfolioParams.FromXMLString(ByVal bstrXML As String)
BOEPortfolioParams.GetXMLSchema() -> String
BOEPortfolioParams.ToXMLFile(ByVal bstrFileName As String)
BOEPortfolioParams.ToXMLString() -> String
BOEPortfolios.Count : Long [R]
BOEPortfolios.Add() -> BOEPortfolio
BOEPortfolios.GetXMLSchema() -> String
BOEPortfolios.Item(ByVal vtIndex As Variant) -> BOEPortfolio
BOEPortfolios.ToXMLFile(ByVal bstrFileName As String)
BOEPortfolios.ToXMLString() -> String
BOEPortfoliosParams.Count : Long [R]
BOEPortfoliosParams.Add() -> BOEPortfolioParams
BOEPortfoliosParams.GetXMLSchema() -> String
BOEPortfoliosParams.Item(ByVal vtIndex As Variant) -> BOEPortfolioParams
BOEPortfoliosParams.ToXMLFile(ByVal bstrFileName As String)
BOEPortfoliosParams.ToXMLString() -> String
BOEPortfoliosService.AddBOEPortfolio(ByVal pIBOEPortfolio As BOEPortfolio) -> BOEPortfolioParams
BOEPortfoliosService.DeleteBOEPortfolio(ByVal pIBOEPortfolioParams As BOEPortfolioParams)
BOEPortfoliosService.GetBOEPortfolio(ByVal pIBOEPortfolioParams As BOEPortfolioParams) -> BOEPortfolio
BOEPortfoliosService.GetBOEPortfolioList() -> BOEPortfoliosParams
BOEPortfoliosService.GetDataInterface(ByVal enumMSDI As BOEPortfoliosServiceDataInterfaces) -> Object
BOEPortfoliosService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BOEPortfoliosService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BOEPortfoliosService.UpdateBOEPortfolio(ByVal pIBOEPortfolio As BOEPortfolio)
Boxes1099.Box1099 : String [R/W]
Boxes1099.BoxDescription : String [R/W]
Boxes1099.Count : Long [R]
Boxes1099.FormCode : Long [R]
Boxes1099.Minimum1099Amount : Double [R/W]
Boxes1099.UserFields : UserFields [R]
Boxes1099.Add()
Boxes1099.SetCurrentLine(ByVal LineNum As Long)
BPAccountReceivablePayble.AccountCode : String [R/W]
BPAccountReceivablePayble.AccountType : BoBpAccountTypes [R/W]
BPAccountReceivablePayble.BPCode : String [R]
BPAccountReceivablePayble.Count : Long [R]
BPAccountReceivablePayble.Add()
BPAccountReceivablePayble.SetCurrentLine(ByVal LineNum As Long)
BPAddresses.AddressName : String [R/W]
BPAddresses.AddressName2 : String [R/W]
BPAddresses.AddressName3 : String [R/W]
BPAddresses.AddressType : BoAddressType [R/W]
BPAddresses.Block : String [R/W]
BPAddresses.BPCode : String [R]
BPAddresses.BuildingFloorRoom : String [R/W]
BPAddresses.City : String [R/W]
BPAddresses.Count : Long [R]
BPAddresses.Country : String [R/W]
BPAddresses.County : String [R/W]
BPAddresses.CreateDate : Date [R]
BPAddresses.CreateTime : Date [R]
BPAddresses.FederalTaxID : String [R/W]
BPAddresses.GlobalLocationNumber : String [R/W]
BPAddresses.GSTIN : String [R/W]
BPAddresses.GstType : BoGSTRegnTypeEnum [R/W]
BPAddresses.MYFType : BoMYFTypeEnum [R/W]
BPAddresses.Nationality : String [R/W]
BPAddresses.RowNum : Long [R]
BPAddresses.State : String [R/W]
BPAddresses.Street : String [R/W]
BPAddresses.StreetNo : String [R/W]
BPAddresses.TaasEnabled : BoYesNoEnum [R/W]
BPAddresses.TaxCode : String [R/W]
BPAddresses.TaxOffice : String [R/W]
BPAddresses.TypeOfAddress : String [R/W]
BPAddresses.UserFields : UserFields [R]
BPAddresses.ZipCode : String [R/W]
BPAddresses.Add()
BPAddresses.Delete()
BPAddresses.SetCurrentLine(ByVal LineNum As Long)
BPBankAccounts.ABARoutingNumber : String [R/W]
BPBankAccounts.AccountName : String [R/W]
BPBankAccounts.AccountNo : String [R/W]
BPBankAccounts.BankCode : String [R/W]
BPBankAccounts.BICSwiftCode : String [R/W]
BPBankAccounts.BIK : String [R/W]
BPBankAccounts.Block : String [R/W]
BPBankAccounts.BPCode : String [R/W]
BPBankAccounts.Branch : String [R/W]
BPBankAccounts.BuildingFloorRoom : String [R/W]
BPBankAccounts.City : String [R/W]
BPBankAccounts.ControlKey : String [R/W]
BPBankAccounts.CorrespondentAccount : String [R/W]
BPBankAccounts.Count : Long [R]
BPBankAccounts.Country : String [R/W]
BPBankAccounts.County : String [R/W]
BPBankAccounts.CustomerIdNumber : String [R/W]
BPBankAccounts.Fax : String [R/W]
BPBankAccounts.IBAN : String [R/W]
BPBankAccounts.InternalKey : Long [R/W]
BPBankAccounts.ISRBillerID : String [R/W]
BPBankAccounts.ISRType : Long [R/W]
BPBankAccounts.LogInstance : Long [R/W]
BPBankAccounts.MandateExpDate : Date [R/W]
BPBankAccounts.MandateID : String [R/W]
BPBankAccounts.Phone : String [R/W]
BPBankAccounts.SEPASeqType : SEPASequenceTypeEnum [R/W]
BPBankAccounts.SignatureDate : Date [R/W]
BPBankAccounts.State : String [R/W]
BPBankAccounts.Street : String [R/W]
BPBankAccounts.UserFields : UserFields [R]
BPBankAccounts.UserNo1 : String [R/W]
BPBankAccounts.UserNo2 : String [R/W]
BPBankAccounts.UserNo3 : String [R/W]
BPBankAccounts.UserNo4 : String [R/W]
BPBankAccounts.ZipCode : String [R/W]
BPBankAccounts.Add()
BPBankAccounts.Delete()
BPBankAccounts.SetCurrentLine(ByVal LineNum As Long)
BPBlockSendingMarketingContents.CardCode : String [R]
BPBlockSendingMarketingContents.Choose : BoYesNoEnum [R/W]
BPBlockSendingMarketingContents.CommunicationMediaId : Long [R/W]
BPBlockSendingMarketingContents.Add()
BPBlockSendingMarketingContents.Delete()
BPBlockSendingMarketingContents.SetCurrentLine(ByVal LineNum As Long)
BPBranchAssignment.BPCode : String [R]
BPBranchAssignment.BPLID : Long [R/W]
BPBranchAssignment.Count : Long [R]
BPBranchAssignment.DisabledForBP : BoYesNoEnum [R/W]
BPBranchAssignment.Add()
BPBranchAssignment.Delete()
BPBranchAssignment.SetCurrentLine(ByVal LineNum As Long)
BPCode.BpCtrlAcct : String [R/W]
BPCode.Code : String [R/W]
BPCode.Credit : Double [R/W]
BPCode.Debit : Double [R/W]
BPCode.DueDate : Date [R/W]
BPCode.ForeignCredit : Double [R/W]
BPCode.ForeignCurrency : String [R/W]
BPCode.ForeignDebit : Double [R/W]
BPCode.SystemCredit : Double [R/W]
BPCode.SystemDebit : Double [R/W]
BPCode.FromXMLFile(ByVal bstrFileName As String)
BPCode.FromXMLString(ByVal bstrXML As String)
BPCode.GetXMLSchema() -> String
BPCode.ToXMLFile(ByVal bstrFileName As String)
BPCode.ToXMLString() -> String
BPCodes.Count : Long [R]
BPCodes.Add() -> BPCode
BPCodes.GetXMLSchema() -> String
BPCodes.Item(ByVal vtIndex As Variant) -> BPCode
BPCodes.ToXMLFile(ByVal bstrFileName As String)
BPCodes.ToXMLString() -> String
BPCurrencies.Count : Long [R]
BPCurrencies.CurrencyCode : String [R]
BPCurrencies.Include : BoYesNoEnum [R/W]
BPCurrencies.SetCurrentLine(ByVal LineNum As Long)
BPFiscalRegistryID.Browser : DataBrowser [R]
BPFiscalRegistryID.CNAECode : String [R/W]
BPFiscalRegistryID.Description : String [R/W]
BPFiscalRegistryID.Numerator : Long [R]
BPFiscalRegistryID.UserFields : UserFields [R]
BPFiscalRegistryID.Add() -> Long
BPFiscalRegistryID.GetAsXML() -> String
BPFiscalRegistryID.GetByKey(ByVal lGroupCode As Long) -> Boolean
BPFiscalRegistryID.Remove() -> Long
BPFiscalRegistryID.SaveToFile(ByVal bstrFileName As String)
BPFiscalRegistryID.SaveXML(ByRef pbstrFileName As String)
BPFiscalRegistryID.Update() -> Long
BPFiscalTaxID.Address : String [R/W]
BPFiscalTaxID.AddrType : BoAddressType [R]
BPFiscalTaxID.AuthorizationForRetrieveFromSEFAZ : BoYesNoEnum [R/W]
BPFiscalTaxID.BPCode : String [R]
BPFiscalTaxID.CNAECode : Long [R/W]
BPFiscalTaxID.Count : Long [R]
BPFiscalTaxID.TaxId0 : String [R/W]
BPFiscalTaxID.TaxId1 : String [R/W]
BPFiscalTaxID.TaxId10 : String [R/W]
BPFiscalTaxID.TaxId11 : String [R/W]
BPFiscalTaxID.TaxId12 : String [R/W]
BPFiscalTaxID.TaxId13 : String [R/W]
BPFiscalTaxID.TaxId14 : String [R/W]
BPFiscalTaxID.TaxId2 : String [R/W]
BPFiscalTaxID.TaxId3 : String [R/W]
BPFiscalTaxID.TaxId4 : String [R/W]
BPFiscalTaxID.TaxId5 : String [R/W]
BPFiscalTaxID.TaxId6 : String [R/W]
BPFiscalTaxID.TaxId7 : String [R/W]
BPFiscalTaxID.TaxId8 : String [R/W]
BPFiscalTaxID.TaxId9 : String [R/W]
BPFiscalTaxID.UserFields : UserFields [R]
BPFiscalTaxID.Add()
BPFiscalTaxID.SetCurrentLine(ByVal LineNum As Long)
BPIntrastatExtension.CardCode : String [R]
BPIntrastatExtension.CustomsProcedure : Long [R/W]
BPIntrastatExtension.DomesticOrForeignID : String [R/W]
BPIntrastatExtension.Incoterms : Long [R/W]
BPIntrastatExtension.IntrastatRelevant : BoYesNoEnum [R/W]
BPIntrastatExtension.NatureOfTransactions : Long [R/W]
BPIntrastatExtension.PortOfEntryOrExit : Long [R/W]
BPIntrastatExtension.StatisticalProcedure : Long [R/W]
BPIntrastatExtension.TransportMode : Long [R/W]
BPPaymentDates.BPCode : String [R]
BPPaymentDates.Count : Long [R]
BPPaymentDates.PaymentDate : String [R/W]
BPPaymentDates.UserFields : UserFields [R]
BPPaymentDates.Add()
BPPaymentDates.Delete()
BPPaymentDates.SetCurrentLine(ByVal LineNum As Long)
BPPaymentMethods.BPCode : String [R]
BPPaymentMethods.Count : Long [R]
BPPaymentMethods.PaymentMethodCode : String [R/W]
BPPaymentMethods.RowNumber : Long [R]
BPPaymentMethods.UserFields : UserFields [R]
BPPaymentMethods.Add()
BPPaymentMethods.Delete()
BPPaymentMethods.SetCurrentLine(ByVal LineNum As Long)
BPPriorities.Browser : DataBrowser [R]
BPPriorities.Priority : Long [R/W]
BPPriorities.PriorityDescription : String [R/W]
BPPriorities.UserFields : UserFields [R]
BPPriorities.Add() -> Long
BPPriorities.GetAsXML() -> String
BPPriorities.GetByKey(ByVal lCode As Long) -> Boolean
BPPriorities.Remove() -> Long
BPPriorities.SaveToFile(ByVal bstrFileName As String)
BPPriorities.SaveXML(ByRef pbstrFileName As String)
BPPriorities.Update() -> Long
BPVatExemptions.AbsoluteEntry : Long [R]
BPVatExemptions.BPCode : String [R/W]
BPVatExemptions.BPVatExemptionsLines : BPVatExemptionsLines [R]
BPVatExemptions.Remarks : String [R/W]
BPVatExemptions.FromXMLFile(ByVal bstrFileName As String)
BPVatExemptions.FromXMLString(ByVal bstrXML As String)
BPVatExemptions.GetXMLSchema() -> String
BPVatExemptions.ToXMLFile(ByVal bstrFileName As String)
BPVatExemptions.ToXMLString() -> String
BPVatExemptionsLine.AbsoluteEntry : Long [R]
BPVatExemptionsLine.ApplyAllItems : BoYesNoEnum [R/W]
BPVatExemptionsLine.AuthoritiesName : String [R/W]
BPVatExemptionsLine.ExemptionDocNum : String [R/W]
BPVatExemptionsLine.ExemptionType : Long [R/W]
BPVatExemptionsLine.IssueDate : Date [R/W]
BPVatExemptionsLine.IssueTime : Date [R/W]
BPVatExemptionsLine.ItemCode : String [R/W]
BPVatExemptionsLine.ItemDescription : String [R]
BPVatExemptionsLine.LineNumber : Long [R]
BPVatExemptionsLine.TaxCode : String [R/W]
BPVatExemptionsLine.ValidFrom : Date [R/W]
BPVatExemptionsLine.ValidTo : Date [R/W]
BPVatExemptionsLine.VATRate : Double [R/W]
BPVatExemptionsLine.VisualOrder : Long [R]
BPVatExemptionsLine.FromXMLFile(ByVal bstrFileName As String)
BPVatExemptionsLine.FromXMLString(ByVal bstrXML As String)
BPVatExemptionsLine.GetXMLSchema() -> String
BPVatExemptionsLine.ToXMLFile(ByVal bstrFileName As String)
BPVatExemptionsLine.ToXMLString() -> String
BPVatExemptionsLines.Count : Long [R]
BPVatExemptionsLines.Add() -> BPVatExemptionsLine
BPVatExemptionsLines.GetXMLSchema() -> String
BPVatExemptionsLines.Item(ByVal vtIndex As Variant) -> BPVatExemptionsLine
BPVatExemptionsLines.Remove(ByVal vtIndex As Variant)
BPVatExemptionsLines.ToXMLFile(ByVal bstrFileName As String)
BPVatExemptionsLines.ToXMLString() -> String
BPVatExemptionsParams.AbsoluteEntry : Long [R/W]
BPVatExemptionsParams.BPCode : String [R]
BPVatExemptionsParams.FromXMLFile(ByVal bstrFileName As String)
BPVatExemptionsParams.FromXMLString(ByVal bstrXML As String)
BPVatExemptionsParams.GetXMLSchema() -> String
BPVatExemptionsParams.ToXMLFile(ByVal bstrFileName As String)
BPVatExemptionsParams.ToXMLString() -> String
BPVatExemptionsParamsCollection.Count : Long [R]
BPVatExemptionsParamsCollection.Add() -> BPVatExemptionsParams
BPVatExemptionsParamsCollection.GetXMLSchema() -> String
BPVatExemptionsParamsCollection.Item(ByVal vtIndex As Variant) -> BPVatExemptionsParams
BPVatExemptionsParamsCollection.ToXMLFile(ByVal bstrFileName As String)
BPVatExemptionsParamsCollection.ToXMLString() -> String
BPVatExemptionsService.Add(ByVal pIBPVatExemptions As BPVatExemptions) -> BPVatExemptionsParams
BPVatExemptionsService.Delete(ByVal pIBPVatExemptionsParams As BPVatExemptionsParams)
BPVatExemptionsService.Get(ByVal pIBPVatExemptionsParams As BPVatExemptionsParams) -> BPVatExemptions
BPVatExemptionsService.GetDataInterface(ByVal enumMSDI As BPVatExemptionsServiceDataInterfaces) -> Object
BPVatExemptionsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BPVatExemptionsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BPVatExemptionsService.GetList() -> BPVatExemptionsParamsCollection
BPVatExemptionsService.Update(ByVal pIBPVatExemptions As BPVatExemptions)
BPWithholdingTax.BPCode : String [R]
BPWithholdingTax.Count : Long [R]
BPWithholdingTax.UserFields : UserFields [R]
BPWithholdingTax.WTCode : String [R/W]
BPWithholdingTax.Add()
BPWithholdingTax.SetCurrentLine(ByVal LineNum As Long)
Branch.Code : Long [R]
Branch.Description : String [R/W]
Branch.Name : String [R/W]
Branch.FromXMLFile(ByVal bstrFileName As String)
Branch.FromXMLString(ByVal bstrXML As String)
Branch.GetXMLSchema() -> String
Branch.ToXMLFile(ByVal bstrFileName As String)
Branch.ToXMLString() -> String
BranchesParams.Count : Long [R]
BranchesParams.Add() -> BranchParams
BranchesParams.GetXMLSchema() -> String
BranchesParams.Item(ByVal vtIndex As Variant) -> BranchParams
BranchesParams.ToXMLFile(ByVal bstrFileName As String)
BranchesParams.ToXMLString() -> String
BranchesService.AddBranch(ByVal pIBranch As Branch) -> BranchParams
BranchesService.DeleteBranch(ByVal pIBranchParams As BranchParams)
BranchesService.GetBranch(ByVal pIBranchParams As BranchParams) -> Branch
BranchesService.GetBranchList() -> BranchesParams
BranchesService.GetDataInterface(ByVal enumMSDI As BranchesServiceDataInterfaces) -> Object
BranchesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BranchesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BranchesService.UpdateBranch(ByVal pIBranch As Branch)
BranchParams.Code : Long [R/W]
BranchParams.Name : String [R]
BranchParams.FromXMLFile(ByVal bstrFileName As String)
BranchParams.FromXMLString(ByVal bstrXML As String)
BranchParams.GetXMLSchema() -> String
BranchParams.ToXMLFile(ByVal bstrFileName As String)
BranchParams.ToXMLString() -> String
BrazilBeverageIndexer.BeverageCommercialBrandCode : Long [R/W]
BrazilBeverageIndexer.BeverageGroupCode : String [R/W]
BrazilBeverageIndexer.BeverageID : Long [R]
BrazilBeverageIndexer.BeverageTableCode : String [R/W]
BrazilBeverageIndexer.FromXMLFile(ByVal bstrFileName As String)
BrazilBeverageIndexer.FromXMLString(ByVal bstrXML As String)
BrazilBeverageIndexer.GetXMLSchema() -> String
BrazilBeverageIndexer.ToXMLFile(ByVal bstrFileName As String)
BrazilBeverageIndexer.ToXMLString() -> String
BrazilBeverageIndexerParams.BeverageCommercialBrandCode : Long [R/W]
BrazilBeverageIndexerParams.BeverageGroupCode : String [R/W]
BrazilBeverageIndexerParams.BeverageTableCode : String [R/W]
BrazilBeverageIndexerParams.FromXMLFile(ByVal bstrFileName As String)
BrazilBeverageIndexerParams.FromXMLString(ByVal bstrXML As String)
BrazilBeverageIndexerParams.GetXMLSchema() -> String
BrazilBeverageIndexerParams.ToXMLFile(ByVal bstrFileName As String)
BrazilBeverageIndexerParams.ToXMLString() -> String
BrazilBeverageIndexersParams.Count : Long [R]
BrazilBeverageIndexersParams.Add() -> BrazilBeverageIndexerParams
BrazilBeverageIndexersParams.GetXMLSchema() -> String
BrazilBeverageIndexersParams.Item(ByVal vtIndex As Variant) -> BrazilBeverageIndexerParams
BrazilBeverageIndexersParams.ToXMLFile(ByVal bstrFileName As String)
BrazilBeverageIndexersParams.ToXMLString() -> String
BrazilBeverageIndexersService.Add(ByVal pIBrazilBeverageIndexer As BrazilBeverageIndexer) -> BrazilBeverageIndexerParams
BrazilBeverageIndexersService.Delete(ByVal pIBrazilBeverageIndexerParams As BrazilBeverageIndexerParams)
BrazilBeverageIndexersService.Get(ByVal pIBrazilBeverageIndexerParams As BrazilBeverageIndexerParams) -> BrazilBeverageIndexer
BrazilBeverageIndexersService.GetDataInterface(ByVal enumMSDI As BrazilBeverageIndexersServiceDataInterfaces) -> Object
BrazilBeverageIndexersService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BrazilBeverageIndexersService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BrazilBeverageIndexersService.GetList() -> BrazilBeverageIndexersParams
BrazilFuelIndexer.Description : String [R/W]
BrazilFuelIndexer.FuelCode : String [R/W]
BrazilFuelIndexer.FuelGroupCode : Long [R/W]
BrazilFuelIndexer.FuelID : Long [R]
BrazilFuelIndexer.FromXMLFile(ByVal bstrFileName As String)
BrazilFuelIndexer.FromXMLString(ByVal bstrXML As String)
BrazilFuelIndexer.GetXMLSchema() -> String
BrazilFuelIndexer.ToXMLFile(ByVal bstrFileName As String)
BrazilFuelIndexer.ToXMLString() -> String
BrazilFuelIndexerParams.Description : String [R]
BrazilFuelIndexerParams.FuelCode : String [R]
BrazilFuelIndexerParams.FuelGroupCode : Long [R]
BrazilFuelIndexerParams.FuelID : Long [R/W]
BrazilFuelIndexerParams.FromXMLFile(ByVal bstrFileName As String)
BrazilFuelIndexerParams.FromXMLString(ByVal bstrXML As String)
BrazilFuelIndexerParams.GetXMLSchema() -> String
BrazilFuelIndexerParams.ToXMLFile(ByVal bstrFileName As String)
BrazilFuelIndexerParams.ToXMLString() -> String
BrazilFuelIndexersParams.Count : Long [R]
BrazilFuelIndexersParams.Add() -> BrazilFuelIndexerParams
BrazilFuelIndexersParams.GetXMLSchema() -> String
BrazilFuelIndexersParams.Item(ByVal vtIndex As Variant) -> BrazilFuelIndexerParams
BrazilFuelIndexersParams.ToXMLFile(ByVal bstrFileName As String)
BrazilFuelIndexersParams.ToXMLString() -> String
BrazilFuelIndexersService.Add(ByVal pIBrazilFuelIndexer As BrazilFuelIndexer) -> BrazilFuelIndexerParams
BrazilFuelIndexersService.Delete(ByVal pIBrazilFuelIndexerParams As BrazilFuelIndexerParams)
BrazilFuelIndexersService.Get(ByVal pIBrazilFuelIndexerParams As BrazilFuelIndexerParams) -> BrazilFuelIndexer
BrazilFuelIndexersService.GetDataInterface(ByVal enumMSDI As BrazilFuelIndexersServiceDataInterfaces) -> Object
BrazilFuelIndexersService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BrazilFuelIndexersService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BrazilFuelIndexersService.GetList() -> BrazilFuelIndexersParams
BrazilMultiIndexer.Code : String [R/W]
BrazilMultiIndexer.Description : String [R/W]
BrazilMultiIndexer.FirstRefIndexerCode : String [R/W]
BrazilMultiIndexer.ID : Long [R]
BrazilMultiIndexer.IndexerType : BrazilMultiIndexerTypes [R/W]
BrazilMultiIndexer.SecondRefIndexerCode : String [R/W]
BrazilMultiIndexer.ThirdRefIndexerCode : String [R/W]
BrazilMultiIndexer.FromXMLFile(ByVal bstrFileName As String)
BrazilMultiIndexer.FromXMLString(ByVal bstrXML As String)
BrazilMultiIndexer.GetReferencedIndexerType(ByVal referenceIndex As Long, ByRef penumRsltType As BrazilIndexerTypes, ByRef plRsltValue As Long) -> Boolean
BrazilMultiIndexer.GetXMLSchema() -> String
BrazilMultiIndexer.ToXMLFile(ByVal bstrFileName As String)
BrazilMultiIndexer.ToXMLString() -> String
BrazilMultiIndexerParams.Code : String [R/W]
BrazilMultiIndexerParams.Description : String [R]
BrazilMultiIndexerParams.FirstRefIndexerCode : String [R]
BrazilMultiIndexerParams.IndexerType : BrazilMultiIndexerTypes [R/W]
BrazilMultiIndexerParams.SecondRefIndexerCode : String [R]
BrazilMultiIndexerParams.ThirdRefIndexerCode : String [R]
BrazilMultiIndexerParams.FromXMLFile(ByVal bstrFileName As String)
BrazilMultiIndexerParams.FromXMLString(ByVal bstrXML As String)
BrazilMultiIndexerParams.GetXMLSchema() -> String
BrazilMultiIndexerParams.ToXMLFile(ByVal bstrFileName As String)
BrazilMultiIndexerParams.ToXMLString() -> String
BrazilMultiIndexersParams.Count : Long [R]
BrazilMultiIndexersParams.Add() -> BrazilMultiIndexerParams
BrazilMultiIndexersParams.GetXMLSchema() -> String
BrazilMultiIndexersParams.Item(ByVal vtIndex As Variant) -> BrazilMultiIndexerParams
BrazilMultiIndexersParams.ToXMLFile(ByVal bstrFileName As String)
BrazilMultiIndexersParams.ToXMLString() -> String
BrazilMultiIndexersService.Add(ByVal pIBrazilMultiIndexer As BrazilMultiIndexer) -> BrazilMultiIndexerParams
BrazilMultiIndexersService.Delete(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams)
BrazilMultiIndexersService.Get(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams) -> BrazilMultiIndexer
BrazilMultiIndexersService.GetDataInterface(ByVal enumMSDI As BrazilMultiIndexersServiceDataInterfaces) -> Object
BrazilMultiIndexersService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BrazilMultiIndexersService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BrazilMultiIndexersService.GetIndexerTypeList(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams) -> BrazilMultiIndexersParams
BrazilNumericIndexer.Code : Long [R/W]
BrazilNumericIndexer.Description : String [R/W]
BrazilNumericIndexer.ID : Long [R]
BrazilNumericIndexer.IndexerType : BrazilNumericIndexerTypes [R/W]
BrazilNumericIndexer.FromXMLFile(ByVal bstrFileName As String)
BrazilNumericIndexer.FromXMLString(ByVal bstrXML As String)
BrazilNumericIndexer.GetXMLSchema() -> String
BrazilNumericIndexer.ToXMLFile(ByVal bstrFileName As String)
BrazilNumericIndexer.ToXMLString() -> String
BrazilNumericIndexerParams.Code : Long [R/W]
BrazilNumericIndexerParams.Description : String [R]
BrazilNumericIndexerParams.IndexerType : BrazilNumericIndexerTypes [R/W]
BrazilNumericIndexerParams.FromXMLFile(ByVal bstrFileName As String)
BrazilNumericIndexerParams.FromXMLString(ByVal bstrXML As String)
BrazilNumericIndexerParams.GetXMLSchema() -> String
BrazilNumericIndexerParams.ToXMLFile(ByVal bstrFileName As String)
BrazilNumericIndexerParams.ToXMLString() -> String
BrazilNumericIndexersParams.Count : Long [R]
BrazilNumericIndexersParams.Add() -> BrazilNumericIndexerParams
BrazilNumericIndexersParams.GetXMLSchema() -> String
BrazilNumericIndexersParams.Item(ByVal vtIndex As Variant) -> BrazilNumericIndexerParams
BrazilNumericIndexersParams.ToXMLFile(ByVal bstrFileName As String)
BrazilNumericIndexersParams.ToXMLString() -> String
BrazilNumericIndexersService.Add(ByVal pIBrazilNumericIndexer As BrazilNumericIndexer) -> BrazilNumericIndexerParams
BrazilNumericIndexersService.Delete(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams)
BrazilNumericIndexersService.Get(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams) -> BrazilNumericIndexer
BrazilNumericIndexersService.GetDataInterface(ByVal enumMSDI As BrazilNumericIndexersServiceDataInterfaces) -> Object
BrazilNumericIndexersService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BrazilNumericIndexersService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BrazilNumericIndexersService.GetIndexerTypeList(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams) -> BrazilNumericIndexersParams
BrazilStringIndexer.Code : String [R/W]
BrazilStringIndexer.Description : String [R/W]
BrazilStringIndexer.ID : Long [R]
BrazilStringIndexer.IndexerType : BrazilStringIndexerTypes [R/W]
BrazilStringIndexer.FromXMLFile(ByVal bstrFileName As String)
BrazilStringIndexer.FromXMLString(ByVal bstrXML As String)
BrazilStringIndexer.GetXMLSchema() -> String
BrazilStringIndexer.ToXMLFile(ByVal bstrFileName As String)
BrazilStringIndexer.ToXMLString() -> String
BrazilStringIndexerParams.Code : String [R/W]
BrazilStringIndexerParams.Description : String [R]
BrazilStringIndexerParams.IndexerType : BrazilStringIndexerTypes [R/W]
BrazilStringIndexerParams.FromXMLFile(ByVal bstrFileName As String)
BrazilStringIndexerParams.FromXMLString(ByVal bstrXML As String)
BrazilStringIndexerParams.GetXMLSchema() -> String
BrazilStringIndexerParams.ToXMLFile(ByVal bstrFileName As String)
BrazilStringIndexerParams.ToXMLString() -> String
BrazilStringIndexersParams.Count : Long [R]
BrazilStringIndexersParams.Add() -> BrazilStringIndexerParams
BrazilStringIndexersParams.GetXMLSchema() -> String
BrazilStringIndexersParams.Item(ByVal vtIndex As Variant) -> BrazilStringIndexerParams
BrazilStringIndexersParams.ToXMLFile(ByVal bstrFileName As String)
BrazilStringIndexersParams.ToXMLString() -> String
BrazilStringIndexersService.Add(ByVal pIBrazilStringIndexer As BrazilStringIndexer) -> BrazilStringIndexerParams
BrazilStringIndexersService.Delete(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams)
BrazilStringIndexersService.Get(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams) -> BrazilStringIndexer
BrazilStringIndexersService.GetDataInterface(ByVal enumMSDI As BrazilStringIndexersServiceDataInterfaces) -> Object
BrazilStringIndexersService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BrazilStringIndexersService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BrazilStringIndexersService.GetIndexerTypeList(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams) -> BrazilStringIndexersParams
Budget.AccountCode : String [R/W]
Budget.Browser : DataBrowser [R]
Budget.BudgetBalanceCreditLoc : Double [R]
Budget.BudgetBalanceCreditSys : Double [R]
Budget.BudgetBalanceDebitLoc : Double [R]
Budget.BudgetBalanceDebitSys : Double [R]
Budget.BudgetScenario : Long [R/W]
Budget.CostAccountingLines : BudgetCostAccounting_Lines [R]
Budget.DivisionCode : Long [R/W]
Budget.FutureAnnualExpensesCreditLoc : Double [R]
Budget.FutureAnnualExpensesCreditSys : Double [R]
Budget.FutureAnnualExpensesDebitLoc : Double [R]
Budget.FutureAnnualExpensesDebitSys : Double [R]
Budget.FutureAnnualRevenuesCredit : Double [R]
Budget.FutureAnnualRevenuesDebit : Double [R]
Budget.FutureRevenuesDebitLoc : Double [R]
Budget.FutureRevenuesDebitSys : Double [R]
Budget.Lines : Budget_Lines [R]
Budget.Numerator : Long [R]
Budget.ParentAccountKey : String [R/W]
Budget.ParentAccPercent : Double [R/W]
Budget.StartofFiscalYear : Date [R]
Budget.TotalAnnualBudgetCreditLoc : Double [R/W]
Budget.TotalAnnualBudgetCreditSys : Double [R/W]
Budget.TotalAnnualBudgetDebitLoc : Double [R/W]
Budget.TotalAnnualBudgetDebitSys : Double [R/W]
Budget.UserFields : UserFields [R]
Budget.Add() -> Long
Budget.GetAsXML() -> String
Budget.GetByKey(ByVal Key As Long) -> Boolean
Budget.Remove() -> Long
Budget.SaveToFile(ByVal FileName As String)
Budget.SaveXML(ByRef FileName As String)
Budget.Update() -> Long
Budget_Lines.AccountCode : String [R]
Budget_Lines.BalSysTotCredit : Double [R]
Budget_Lines.BalSysTotDebit : Double [R]
Budget_Lines.BalTotCredit : Double [R]
Budget_Lines.BalTotDebit : Double [R]
Budget_Lines.BudgetKey : Long [R]
Budget_Lines.BudgetSysTotCredit : Double [R/W]
Budget_Lines.BudgetSysTotDebit : Double [R/W]
Budget_Lines.BudgetTotCredit : Double [R/W]
Budget_Lines.BudgetTotDebit : Double [R/W]
Budget_Lines.Count : Long [R]
Budget_Lines.FutExpenCredit : Double [R]
Budget_Lines.FutExpenDebit : Double [R]
Budget_Lines.FutExpenSysCredit : Double [R]
Budget_Lines.FutExpenSysDebit : Double [R]
Budget_Lines.FutIncomesCredit : Double [R]
Budget_Lines.FutIncomesSysCredit : Double [R]
Budget_Lines.FutIncomesSysDebit : Double [R]
Budget_Lines.FutureIncomeDeb : Double [R]
Budget_Lines.PrecentOfAnnualBudgetAmount : Double [R]
Budget_Lines.RowDetails : String [R/W]
Budget_Lines.RowNumber : Long [R]
Budget_Lines.UserFields : UserFields [R]
Budget_Lines.Add()
Budget_Lines.SetCurrentLine(ByVal LineNum As Long)
BudgetCostAccounting_Lines.Count : Long [R]
BudgetCostAccounting_Lines.Dimension : Long [R/W]
BudgetCostAccounting_Lines.DistrRuleCode : String [R/W]
BudgetCostAccounting_Lines.DistrRuleCreditLC : Double [R/W]
BudgetCostAccounting_Lines.DistrRuleCreditSC : Double [R/W]
BudgetCostAccounting_Lines.DistrRuleDebitLC : Double [R/W]
BudgetCostAccounting_Lines.DistrRuleDebitSC : Double [R/W]
BudgetCostAccounting_Lines.UserFields : UserFields [R]
BudgetCostAccounting_Lines.Add()
BudgetCostAccounting_Lines.Delete()
BudgetCostAccounting_Lines.SetCurrentLine(ByVal LineNum As Long)
BudgetDistribution.April : Double [R/W]
BudgetDistribution.August : Double [R/W]
BudgetDistribution.Browser : DataBrowser [R]
BudgetDistribution.BudgetAmount : Double [R/W]
BudgetDistribution.December : Double [R/W]
BudgetDistribution.Description : String [R/W]
BudgetDistribution.DivisionCode : Long [R]
BudgetDistribution.February : Double [R/W]
BudgetDistribution.January : Double [R/W]
BudgetDistribution.July : Double [R/W]
BudgetDistribution.June : Double [R/W]
BudgetDistribution.March : Double [R/W]
BudgetDistribution.May : Double [R/W]
BudgetDistribution.November : Double [R/W]
BudgetDistribution.October : Double [R/W]
BudgetDistribution.September : Double [R/W]
BudgetDistribution.UserFields : UserFields [R]
BudgetDistribution.Add() -> Long
BudgetDistribution.Cancel() -> Long
BudgetDistribution.GetAsXML() -> String
BudgetDistribution.GetByKey(ByVal lBgdCode As Long) -> Boolean
BudgetDistribution.Remove() -> Long
BudgetDistribution.SaveToFile(ByVal FileName As String)
BudgetDistribution.SaveXML(ByRef FileName As String)
BudgetDistribution.Update() -> Long
BudgetScenarios.BasicBudget : Long [R/W]
BudgetScenarios.Browser : DataBrowser [R]
BudgetScenarios.DistributionRule : String [R/W]
BudgetScenarios.DistributionRule2 : String [R/W]
BudgetScenarios.DistributionRule3 : String [R/W]
BudgetScenarios.DistributionRule4 : String [R/W]
BudgetScenarios.DistributionRule5 : String [R/W]
BudgetScenarios.InitialRatioPercentage : Double [R/W]
BudgetScenarios.Name : String [R/W]
BudgetScenarios.Numerator : Long [R]
BudgetScenarios.Project : String [R/W]
BudgetScenarios.RoundingMethod : BoRoundingMethod [R/W]
BudgetScenarios.StartofFiscalYear : Date [R/W]
BudgetScenarios.UserFields : UserFields [R]
BudgetScenarios.Add() -> Long
BudgetScenarios.Cancel() -> Long
BudgetScenarios.GetAsXML() -> String
BudgetScenarios.GetByKey(ByVal lAbsID As Long) -> Boolean
BudgetScenarios.Remove() -> Long
BudgetScenarios.SaveToFile(ByVal FileName As String)
BudgetScenarios.SaveXML(ByRef FileName As String)
BudgetScenarios.Update() -> Long
BusinessPartnerGroups.Browser : DataBrowser [R]
BusinessPartnerGroups.Code : Long [R]
BusinessPartnerGroups.Name : String [R/W]
BusinessPartnerGroups.Type : BoBusinessPartnerGroupTypes [R/W]
BusinessPartnerGroups.UserFields : UserFields [R]
BusinessPartnerGroups.Add() -> Long
BusinessPartnerGroups.GetAsXML() -> String
BusinessPartnerGroups.GetByKey(ByVal lGroupCode As Long) -> Boolean
BusinessPartnerGroups.Remove() -> Long
BusinessPartnerGroups.SaveToFile(ByVal bstrFileName As String)
BusinessPartnerGroups.SaveXML(ByRef pbstrFileName As String)
BusinessPartnerGroups.Update() -> Long
BusinessPartnerPropertiesParams.Count : Long [R]
BusinessPartnerPropertiesParams.Add() -> BusinessPartnerPropertyParams
BusinessPartnerPropertiesParams.GetXMLSchema() -> String
BusinessPartnerPropertiesParams.Item(ByVal vtIndex As Variant) -> BusinessPartnerPropertyParams
BusinessPartnerPropertiesParams.ToXMLFile(ByVal bstrFileName As String)
BusinessPartnerPropertiesParams.ToXMLString() -> String
BusinessPartnerPropertiesService.GetBusinessPartnerProperty(ByVal pIBusinessPartnerPropertyParams As BusinessPartnerPropertyParams) -> BusinessPartnerProperty
BusinessPartnerPropertiesService.GetBusinessPartnerPropertyList() -> BusinessPartnerPropertiesParams
BusinessPartnerPropertiesService.GetDataInterface(ByVal enumMSDI As BusinessPartnerPropertiesServiceDataInterfaces) -> Object
BusinessPartnerPropertiesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BusinessPartnerPropertiesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BusinessPartnerPropertiesService.UpdateBusinessPartnerProperty(ByVal pIBusinessPartnerProperty As BusinessPartnerProperty)
BusinessPartnerProperty.PropertyCode : Long [R]
BusinessPartnerProperty.PropertyName : String [R/W]
BusinessPartnerProperty.UserFields : Fields [R]
BusinessPartnerProperty.FromXMLFile(ByVal bstrFileName As String)
BusinessPartnerProperty.FromXMLString(ByVal bstrXML As String)
BusinessPartnerProperty.GetXMLSchema() -> String
BusinessPartnerProperty.ToXMLFile(ByVal bstrFileName As String)
BusinessPartnerProperty.ToXMLString() -> String
BusinessPartnerPropertyParams.PropertyCode : Long [R/W]
BusinessPartnerPropertyParams.PropertyName : String [R]
BusinessPartnerPropertyParams.FromXMLFile(ByVal bstrFileName As String)
BusinessPartnerPropertyParams.FromXMLString(ByVal bstrXML As String)
BusinessPartnerPropertyParams.GetXMLSchema() -> String
BusinessPartnerPropertyParams.ToXMLFile(ByVal bstrFileName As String)
BusinessPartnerPropertyParams.ToXMLString() -> String
BusinessPartners.AcceptsEndorsedChecks : BoYesNoEnum [R/W]
BusinessPartners.AccountRecivablePayables : BPAccountReceivablePayble [R]
BusinessPartners.AccrualCriteria : BoYesNoEnum [R/W]
BusinessPartners.AdditionalID : String [R/W]
BusinessPartners.Address : String [R/W]
BusinessPartners.Addresses : BPAddresses [R]
BusinessPartners.Affiliate : BoYesNoEnum [R/W]
BusinessPartners.AgentCode : String [R/W]
BusinessPartners.AliasName : String [R/W]
BusinessPartners.AttachmentEntry : Long [R/W]
BusinessPartners.AutomaticPosting : AutomaticPostingEnum [R/W]
BusinessPartners.AvarageLate : Long [R/W]
BusinessPartners.BackOrder : BoYesNoEnum [R/W]
BusinessPartners.BankChargesAllocationCode : String [R/W]
BusinessPartners.BankCountry : String [R/W]
BusinessPartners.BillofExchangeonCollection : String [R/W]
BusinessPartners.BillToBuildingFloorRoom : String [R/W]
BusinessPartners.BilltoDefault : String [R/W]
BusinessPartners.BillToState : String [R/W]
BusinessPartners.Block : String [R/W]
BusinessPartners.BlockDunning : BoYesNoEnum [R/W]
BusinessPartners.BlockSendingMarketingContent : BoYesNoEnum [R/W]
BusinessPartners.BookkeepingCertified : BoYesNoEnum [R/W]
BusinessPartners.Box1099 : String [R/W]
BusinessPartners.BPBankAccounts : BPBankAccounts [R]
BusinessPartners.BPBlockSendingMarketingContents : BPBlockSendingMarketingContents [R]
BusinessPartners.BPBranchAssignment : BPBranchAssignment [R]
BusinessPartners.BPCurrencies : BPCurrencies [R]
BusinessPartners.BPPaymentDates : BPPaymentDates [R]
BusinessPartners.BPPaymentMethods : BPPaymentMethods [R]
BusinessPartners.BPWithholdingTax : BPWithholdingTax [R]
BusinessPartners.Browser : DataBrowser [R]
BusinessPartners.BusinessType : String [R/W]
BusinessPartners.CampaignNumber : Long [R/W]
BusinessPartners.CardCode : String [R/W]
BusinessPartners.CardForeignName : String [R/W]
BusinessPartners.CardName : String [R/W]
BusinessPartners.CardType : BoCardTypes [R/W]
BusinessPartners.Cellular : String [R/W]
BusinessPartners.CertificateDetails : String [R/W]
BusinessPartners.CertificateNumber : String [R/W]
BusinessPartners.ChannelBP : String [R/W]
BusinessPartners.City : String [R/W]
BusinessPartners.ClosingDateProcedureNumber : Long [R/W]
BusinessPartners.CollectionAuthorization : BoYesNoEnum [R/W]
BusinessPartners.CommissionGroupCode : Long [R/W]
BusinessPartners.CommissionPercent : Double [R/W]
BusinessPartners.CompanyPrivate : BoCardCompanyTypes [R/W]
BusinessPartners.CompanyRegistrationNumber : String [R/W]
BusinessPartners.ContactEmployees : ContactEmployees [R]
BusinessPartners.ContactPerson : String [R/W]
BusinessPartners.Country : String [R/W]
BusinessPartners.County : String [R/W]
BusinessPartners.CreateDate : Date [R]
BusinessPartners.CreateTime : Date [R]
BusinessPartners.CreditCardCode : Long [R/W]
BusinessPartners.CreditCardExpiration : Date [R/W]
BusinessPartners.CreditCardNum : String [R/W]
BusinessPartners.CreditLimit : Double [R/W]
BusinessPartners.Currency : String [R/W]
BusinessPartners.CurrentAccountBalance : Double [R]
BusinessPartners.CustomerBillofExchangDisc : String [R/W]
BusinessPartners.CustomerBillofExchangPres : String [R/W]
BusinessPartners.DatevAccount : String [R/W]
BusinessPartners.DatevFirstDataEntry : BoYesNoEnum [R/W]
BusinessPartners.DebitorAccount : String [R/W]
BusinessPartners.DeductibleAtSource : BoYesNoEnum [R/W]
BusinessPartners.DeductionOffice : String [R/W]
BusinessPartners.DeductionPercent : Double [R/W]
BusinessPartners.DeductionValidUntil : Date [R/W]
BusinessPartners.DefaultAccount : String [R/W]
BusinessPartners.DefaultBankCode : String [R/W]
BusinessPartners.DefaultBlanketAgreementNumber : Long [R/W]
BusinessPartners.DefaultBranch : String [R/W]
BusinessPartners.DefaultCurrency : String [R/W]
BusinessPartners.DefaultTechnician : Long [R/W]
BusinessPartners.DefaultTransporterEntry : Long [R/W]
BusinessPartners.DefaultTransporterLineNumber : Long [R/W]
BusinessPartners.DeferCommitmentLimitOnDueDate : BoDeferCommitmentLimitOnDueDateTypes [R/W]
BusinessPartners.DeferCommitmentLimitOnDueDateDays : Long [R/W]
BusinessPartners.DeferCommitmentLimitOnDueDateMonths : Long [R/W]
BusinessPartners.DeferredTax : BoYesNoEnum [R/W]
BusinessPartners.DiscountBaseObject : DiscountGroupBaseObjectEnum [R/W]
BusinessPartners.DiscountGroups : DiscountGroups [R]
BusinessPartners.DiscountPercent : Double [R/W]
BusinessPartners.DiscountRelations : DiscountGroupRelationsEnum [R/W]
BusinessPartners.DME : String [R/W]
BusinessPartners.DownPaymentClearAct : String [R/W]
BusinessPartners.DownPaymentInterimAccount : String [R/W]
BusinessPartners.DunningDate : Date [R]
BusinessPartners.DunningLevel : Long [R]
BusinessPartners.DunningTerm : String [R/W]
BusinessPartners.EBooksVATExemptionCause : Long [R/W]
BusinessPartners.ECommerceMerchantID : String [R/W]
BusinessPartners.EDIRecipientID : String [R/W]
BusinessPartners.EDISenderID : String [R/W]
BusinessPartners.EDocBuildingNumber : Long [R/W]
BusinessPartners.EDocCity : String [R/W]
BusinessPartners.EDocCountry : String [R/W]
BusinessPartners.EDocDistrict : String [R/W]
BusinessPartners.EDocGenerationType : EDocGenerationTypeEnum [R/W]
BusinessPartners.EDocPECAddress : String [R/W]
BusinessPartners.EDocRepresentativeAdditionalId : String [R/W]
BusinessPartners.EDocRepresentativeCompany : String [R/W]
BusinessPartners.EDocRepresentativeFirstName : String [R/W]
BusinessPartners.EDocRepresentativeFiscalCode : String [R/W]
BusinessPartners.EDocRepresentativeSurname : String [R/W]
BusinessPartners.EDocStreet : String [R/W]
BusinessPartners.EDocStreetNumber : String [R/W]
BusinessPartners.EDocZipCode : String [R/W]
BusinessPartners.EffectiveDiscount : DiscountGroupRelationsEnum [R/W]
BusinessPartners.EffectivePrice : EffectivePriceEnum [R/W]
BusinessPartners.EffectivePriceConsidersPriceBeforeDiscount : BoYesNoEnum [R/W]
BusinessPartners.ElectronicProtocols : ElectronicProtocols [R]
BusinessPartners.EmailAddress : String [R/W]
BusinessPartners.EndorsableChecksFromBP : BoYesNoEnum [R/W]
BusinessPartners.EORINumber : String [R/W]
BusinessPartners.Equalization : BoYesNoEnum [R/W]
BusinessPartners.ETaxWebSite : Long [R/W]
BusinessPartners.ExchangeRateForIncomingPayment : BoYesNoEnum [R/W]
BusinessPartners.ExchangeRateForOutgoingPayment : BoYesNoEnum [R/W]
BusinessPartners.ExemptionMaxAmountValidationType : ExemptionMaxAmountValidationTypeEnum [R/W]
BusinessPartners.ExemptionValidityDateFrom : Date [R/W]
BusinessPartners.ExemptionValidityDateTo : Date [R/W]
BusinessPartners.ExemptNum : String [R/W]
BusinessPartners.ExpirationDate : Date [R/W]
BusinessPartners.ExportCode : String [R/W]
BusinessPartners.FatherCard : String [R/W]
BusinessPartners.FatherType : BoFatherCardTypes [R/W]
BusinessPartners.Fax : String [R/W]
BusinessPartners.FCEAsPaymentMeans : BoYesNoEnum [R/W]
BusinessPartners.FCERelevant : BoYesNoEnum [R/W]
BusinessPartners.FCEValidateBaseDelivery : BoYesNoEnum [R/W]
BusinessPartners.FederalTaxID : String [R/W]
BusinessPartners.FeeAccount : String [R/W]
BusinessPartners.FiscalTaxID : BPFiscalTaxID [R]
BusinessPartners.FormCode1099 : Long [R/W]
BusinessPartners.FreeText : String [R/W]
BusinessPartners.Frozen : BoYesNoEnum [R/W]
BusinessPartners.FrozenFrom : Date [R/W]
BusinessPartners.FrozenRemarks : String [R/W]
BusinessPartners.FrozenTo : Date [R/W]
BusinessPartners.GlobalLocationNumber : String [R/W]
BusinessPartners.GroupCode : Long [R/W]
BusinessPartners.GTSBankAccountNo : String [R/W]
BusinessPartners.GTSBillingAddrTel : String [R/W]
BusinessPartners.GTSRegNo : String [R/W]
BusinessPartners.HierarchicalDeduction : BoYesNoEnum [R/W]
BusinessPartners.HouseBank : String [R/W]
BusinessPartners.HouseBankAccount : String [R/W]
BusinessPartners.HouseBankBranch : String [R/W]
BusinessPartners.HouseBankCountry : String [R/W]
BusinessPartners.HouseBankIBAN : String [R]
BusinessPartners.IBAN : String [R/W]
BusinessPartners.Indicator : String [R/W]
BusinessPartners.Industry : Long [R/W]
BusinessPartners.IndustryType : String [R/W]
BusinessPartners.InstructionKey : String [R/W]
BusinessPartners.InsuranceOperation347 : BoYesNoEnum [R/W]
BusinessPartners.InterestAccount : String [R/W]
BusinessPartners.IntrastatExtension : BPIntrastatExtension [R]
BusinessPartners.IntrestRatePercent : Double [R/W]
BusinessPartners.IPACodeForPA : String [R/W]
BusinessPartners.ISRBillerID : String [R/W]
BusinessPartners.LanguageCode : Long [R/W]
BusinessPartners.LastMultiReconciliationNum : Long [R/W]
BusinessPartners.LegalText : String [R/W]
BusinessPartners.LinkedBusinessPartner : String [R/W]
BusinessPartners.MailAddress : String [R/W]
BusinessPartners.MailCity : String [R/W]
BusinessPartners.MailCountry : String [R/W]
BusinessPartners.MailCounty : String [R/W]
BusinessPartners.MailZipCode : String [R/W]
BusinessPartners.MainUsage : Long [R/W]
BusinessPartners.MaxAmountOfExemption : Double [R/W]
BusinessPartners.MaxCommitment : Double [R/W]
BusinessPartners.MinIntrest : Double [R/W]
BusinessPartners.NationalInsuranceNum : String [R/W]
BusinessPartners.NoDiscounts : BoYesNoEnum [R/W]
BusinessPartners.Notes : String [R/W]
BusinessPartners.OpenChecksBalance : Double [R]
BusinessPartners.OpenDeliveryNotesBalance : Double [R]
BusinessPartners.OpenOpportunities : Long [R]
BusinessPartners.OpenOrdersBalance : Double [R]
BusinessPartners.OperationCode347 : OperationCode347Enum [R/W]
BusinessPartners.OtherReceivablePayable : String [R/W]
BusinessPartners.OwnerCode : Long [R/W]
BusinessPartners.OwnerIDNumber : String [R/W]
BusinessPartners.Pager : String [R/W]
BusinessPartners.PartialDelivery : BoYesNoEnum [R/W]
BusinessPartners.Password : String [R/W]
BusinessPartners.PaymentBlock : BoYesNoEnum [R/W]
BusinessPartners.PaymentBlockDescription : Long [R/W]
BusinessPartners.PayTermsGrpCode : Long [R/W]
BusinessPartners.PeymentMethodCode : String [R/W]
BusinessPartners.Phone1 : String [R/W]
BusinessPartners.Phone2 : String [R/W]
BusinessPartners.Picture : String [R/W]
BusinessPartners.PlanningGroup : String [R/W]
BusinessPartners.PriceListNum : Long [R/W]
BusinessPartners.PriceMode : PriceModeEnum [R/W]
BusinessPartners.Priority : Long [R/W]
BusinessPartners.Profession : String [R/W]
BusinessPartners.ProjectCode : String [R/W]
BusinessPartners.Properties : BoYesNoEnum [R/W]
BusinessPartners.RateDiffAccount : String [R/W]
BusinessPartners.ReferenceDetails : String [R/W]
BusinessPartners.RelationshipCode : String [R/W]
BusinessPartners.RelationshipDateFrom : Date [R/W]
BusinessPartners.RelationshipDateTill : Date [R/W]
BusinessPartners.RepresentativeName : String [R/W]
BusinessPartners.ResidenNumber : ResidenceNumberTypeEnum [R/W]
BusinessPartners.SalesPersonCode : Long [R/W]
BusinessPartners.Series : Long [R/W]
BusinessPartners.ShaamGroup : ShaamGroupEnum [R/W]
BusinessPartners.ShippingType : Long [R/W]
BusinessPartners.ShipToBuildingFloorRoom : String [R/W]
BusinessPartners.ShipToDefault : String [R/W]
BusinessPartners.SinglePayment : BoYesNoEnum [R/W]
BusinessPartners.SubjectToWithholdingTax : BoYesNoNoneEnum [R/W]
BusinessPartners.SurchargeOverlook : BoYesNoEnum [R/W]
BusinessPartners.TaxExemptionLetterNum : String [R/W]
BusinessPartners.TaxRoundingRule : BoTaxRoundingRuleTypes [R/W]
BusinessPartners.Territory : Long [R/W]
BusinessPartners.ThresholdOverlook : BoYesNoEnum [R/W]
BusinessPartners.TypeOfOperation : TypeOfOperationEnum [R/W]
BusinessPartners.TypeReport : AssesseeTypeEnum [R/W]
BusinessPartners.UnifiedFederalTaxID : String [R/W]
BusinessPartners.UnpaidBillofExchange : String [R/W]
BusinessPartners.UpdateDate : Date [R]
BusinessPartners.UpdateTime : Date [R]
BusinessPartners.UseBillToAddrToDetermineTax : BoYesNoEnum [R/W]
BusinessPartners.UserFields : UserFields [R]
BusinessPartners.UseShippedGoodsAccount : BoYesNoEnum [R/W]
BusinessPartners.Valid : BoYesNoEnum [R/W]
BusinessPartners.ValidFrom : Date [R/W]
BusinessPartners.ValidRemarks : String [R/W]
BusinessPartners.ValidTo : Date [R/W]
BusinessPartners.VatGroup : String [R/W]
BusinessPartners.VatGroupLatinAmerica : String [R/W]
BusinessPartners.VatIDNum : String [R/W]
BusinessPartners.VatLiable : BoVatStatus [R/W]
BusinessPartners.VATRegistrationNumber : String [R/W]
BusinessPartners.VerificationNumber : String [R/W]
BusinessPartners.Website : String [R/W]
BusinessPartners.WithholdingTaxCertified : BoYesNoEnum [R/W]
BusinessPartners.WithholdingTaxDeductionGroup : Long [R/W]
BusinessPartners.WTCode : String [R/W]
BusinessPartners.ZipCode : String [R/W]
BusinessPartners.Add() -> Long
BusinessPartners.Cancel() -> Long
BusinessPartners.Close() -> Long
BusinessPartners.GetAsXML() -> String
BusinessPartners.GetByKey(ByVal CardCode As String) -> Boolean
BusinessPartners.Remove() -> Long
BusinessPartners.SaveToFile(ByVal FileName As String)
BusinessPartners.SaveXML(ByRef FileName As String)
BusinessPartners.Update() -> Long
BusinessPartners.UpdateFromXML(ByVal FileName As String) -> Long
BusinessPartnersService.CreateOpenBalance(ByVal pIOpenningBalanceAccount As OpenningBalanceAccount, ByVal pBPCodes As BPCodes)
BusinessPartnersService.GetDataInterface(ByVal enumMSDI As BusinessPartnersServiceDataInterfaces) -> Object
BusinessPartnersService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
BusinessPartnersService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
BusinessPlaceIENumbers.BPLID : Long [R]
BusinessPlaceIENumbers.Count : Long [R]
BusinessPlaceIENumbers.IENumber : String [R/W]
BusinessPlaceIENumbers.State : String [R/W]
BusinessPlaceIENumbers.Add()
BusinessPlaceIENumbers.Delete()
BusinessPlaceIENumbers.SetCurrentLine(ByVal LineNum As Long)
BusinessPlaces.AdditionalIdNumber : String [R/W]
BusinessPlaces.Address : String [R/W]
BusinessPlaces.Addressforeign : String [R/W]
BusinessPlaces.AddressType : String [R/W]
BusinessPlaces.AliasName : String [R/W]
BusinessPlaces.Block : String [R/W]
BusinessPlaces.BPLID : Long [R]
BusinessPlaces.BPLName : String [R/W]
BusinessPlaces.BPLNameForeign : String [R/W]
BusinessPlaces.Browser : DataBrowser [R]
BusinessPlaces.Building : String [R/W]
BusinessPlaces.Business : String [R/W]
BusinessPlaces.City : String [R/W]
BusinessPlaces.CommercialRegister : String [R/W]
BusinessPlaces.CompanyQualificationCode : Long [R/W]
BusinessPlaces.CooperativeAssociationTypeCode : Long [R/W]
BusinessPlaces.Country : String [R/W]
BusinessPlaces.County : String [R/W]
BusinessPlaces.CreditContributionOriginCode : String [R/W]
BusinessPlaces.DateOfIncorporation : Date [R/W]
BusinessPlaces.DeclarerTypeCode : Long [R/W]
BusinessPlaces.DefaultCustomerID : String [R/W]
BusinessPlaces.DefaultResourceWarehouseID : String [R/W]
BusinessPlaces.DefaultTaxCode : String [R/W]
BusinessPlaces.DefaultVendorID : String [R/W]
BusinessPlaces.DefaultWarehouseID : String [R/W]
BusinessPlaces.Disabled : BoYesNoEnum [R/W]
BusinessPlaces.EconomicActivityTypeCode : Long [R/W]
BusinessPlaces.EnvironmentType : Long [R/W]
BusinessPlaces.FederalTaxID : String [R/W]
BusinessPlaces.FederalTaxID2 : String [R/W]
BusinessPlaces.FederalTaxID3 : String [R/W]
BusinessPlaces.GlobalLocationNumber : String [R/W]
BusinessPlaces.IENumbers : BusinessPlaceIENumbers [R]
BusinessPlaces.Industry : String [R/W]
BusinessPlaces.IPIPeriodCode : String [R/W]
BusinessPlaces.MainBPL : BoYesNoEnum [R/W]
BusinessPlaces.NatureOfCompanyCode : Long [R/W]
BusinessPlaces.Opting4ICMS : BoYesNoEnum [R/W]
BusinessPlaces.PaymentClearingAccount : String [R/W]
BusinessPlaces.PreferredStateCode : String [R/W]
BusinessPlaces.ProfitTaxationCode : Long [R/W]
BusinessPlaces.RepName : String [R/W]
BusinessPlaces.SPEDProfile : String [R/W]
BusinessPlaces.State : String [R/W]
BusinessPlaces.Street : String [R/W]
BusinessPlaces.StreetNo : String [R/W]
BusinessPlaces.TaxOffice : String [R/W]
BusinessPlaces.TaxOfficeNo : String [R/W]
BusinessPlaces.TributaryInfos : BusinessPlaceTributaryInfos [R]
BusinessPlaces.UserFields : UserFields [R]
BusinessPlaces.VATRegNum : String [R/W]
BusinessPlaces.ZipCode : String [R/W]
BusinessPlaces.Add() -> Long
BusinessPlaces.GetAsXML() -> String
BusinessPlaces.GetByKey(ByVal lBplId As Long) -> Boolean
BusinessPlaces.Remove() -> Long
BusinessPlaces.SaveToFile(ByVal bstrFileName As String)
BusinessPlaces.SaveXML(ByRef pbstrFileName As String)
BusinessPlaces.Update() -> Long
BusinessPlaceTributaryInfos.BPLID : Long [R]
BusinessPlaceTributaryInfos.Count : Long [R]
BusinessPlaceTributaryInfos.TRCEndDate : Date [R/W]
BusinessPlaceTributaryInfos.TRCStartDate : Date [R/W]
BusinessPlaceTributaryInfos.TributaryID : Long [R]
BusinessPlaceTributaryInfos.TributaryRegimeCode : Long [R/W]
BusinessPlaceTributaryInfos.TributaryType : Long [R/W]
BusinessPlaceTributaryInfos.TTEndDate : Date [R/W]
BusinessPlaceTributaryInfos.TTStartDate : Date [R/W]
BusinessPlaceTributaryInfos.Add()
BusinessPlaceTributaryInfos.Delete()
BusinessPlaceTributaryInfos.SetCurrentLine(ByVal LineNumber As Long)
CallArgument.Name : String [R/W]
CallArgument.Value : String [R/W]
CallArgument.FromXMLFile(ByVal bstrFileName As String)
CallArgument.FromXMLString(ByVal bstrXML As String)
CallArgument.GetXMLSchema() -> String
CallArgument.ToXMLFile(ByVal bstrFileName As String)
CallArgument.ToXMLString() -> String
CallArguments.Count : Long [R]
CallArguments.Add() -> CallArgument
CallArguments.GetXMLSchema() -> String
CallArguments.Item(ByVal vtIndex As Variant) -> CallArgument
CallArguments.ToXMLFile(ByVal bstrFileName As String)
CallArguments.ToXMLString() -> String
CallMessage.CallMessageArguments : CallMessageArguments [R]
CallMessage.CreationDate : Date [R/W]
CallMessage.CreationTime : Long [R/W]
CallMessage.ErrorCode : String [R/W]
CallMessage.ID : Long [R]
CallMessage.MessageBody : String [R/W]
CallMessage.Status : CallMessageStatusEnum [R]
CallMessage.Type : CallMessageTypeEnum [R/W]
CallMessage.FromXMLFile(ByVal bstrFileName As String)
CallMessage.FromXMLString(ByVal bstrXML As String)
CallMessage.GetXMLSchema() -> String
CallMessage.ToXMLFile(ByVal bstrFileName As String)
CallMessage.ToXMLString() -> String
CallMessageArgument.Name : String [R/W]
CallMessageArgument.Value : String [R/W]
CallMessageArgument.FromXMLFile(ByVal bstrFileName As String)
CallMessageArgument.FromXMLString(ByVal bstrXML As String)
CallMessageArgument.GetXMLSchema() -> String
CallMessageArgument.ToXMLFile(ByVal bstrFileName As String)
CallMessageArgument.ToXMLString() -> String
CallMessageArguments.Count : Long [R]
CallMessageArguments.Add() -> CallMessageArgument
CallMessageArguments.GetXMLSchema() -> String
CallMessageArguments.Item(ByVal vtIndex As Variant) -> CallMessageArgument
CallMessageArguments.ToXMLFile(ByVal bstrFileName As String)
CallMessageArguments.ToXMLString() -> String
CallMessages.Count : Long [R]
CallMessages.Add() -> CallMessage
CallMessages.GetXMLSchema() -> String
CallMessages.Item(ByVal vtIndex As Variant) -> CallMessage
CallMessages.ToXMLFile(ByVal bstrFileName As String)
CallMessages.ToXMLString() -> String
Campaign.AttachementsEntry : Long [R/W]
Campaign.CampaignBusinessPartners : CampaignBusinessPartners [R]
Campaign.CampaignItems : CampaignItems [R]
Campaign.CampaignName : String [R/W]
Campaign.CampaignNumber : Long [R]
Campaign.CampaignPartners : CampaignPartners [R]
Campaign.CampaignType : CampaignTypeEnum [R/W]
Campaign.FinishDate : Date [R/W]
Campaign.GeneratedByWizard : BoYesNoEnum [R/W]
Campaign.Owner : Long [R/W]
Campaign.Remarks : String [R/W]
Campaign.StartDate : Date [R/W]
Campaign.Status : CampaignStatusEnum [R/W]
Campaign.TargetGroup : String [R/W]
Campaign.TargetGroupType : TargetGroupTypeEnum [R/W]
Campaign.UserFields : Fields [R]
Campaign.FromXMLFile(ByVal bstrFileName As String)
Campaign.FromXMLString(ByVal bstrXML As String)
Campaign.GetXMLSchema() -> String
Campaign.ToXMLFile(ByVal bstrFileName As String)
Campaign.ToXMLString() -> String
CampaignBusinessPartner.AddressID : String [R/W]
CampaignBusinessPartner.AddressName2 : String [R/W]
CampaignBusinessPartner.AddressName3 : String [R/W]
CampaignBusinessPartner.AddressType : String [R/W]
CampaignBusinessPartner.AssignName : Long [R/W]
CampaignBusinessPartner.AssignTo : CampaignAssignToEnum [R/W]
CampaignBusinessPartner.Block : String [R/W]
CampaignBusinessPartner.BPCode : String [R/W]
CampaignBusinessPartner.BPGroupName : String [R]
CampaignBusinessPartner.BPIndustryName : String [R]
CampaignBusinessPartner.BPName : String [R/W]
CampaignBusinessPartner.BPStatus : String [R]
CampaignBusinessPartner.Building : String [R/W]
CampaignBusinessPartner.CampaignLineNumber : Long [R]
CampaignBusinessPartner.CampaignNumber : Long [R]
CampaignBusinessPartner.City : String [R/W]
CampaignBusinessPartner.ContactAddress : String [R/W]
CampaignBusinessPartner.ContactCode : String [R/W]
CampaignBusinessPartner.ContactEmail : String [R/W]
CampaignBusinessPartner.ContactFax : String [R/W]
CampaignBusinessPartner.ContactMobile : String [R/W]
CampaignBusinessPartner.ContactPosition : String [R/W]
CampaignBusinessPartner.ContactTelephone : String [R/W]
CampaignBusinessPartner.ContactTitle : String [R/W]
CampaignBusinessPartner.Country : String [R/W]
CampaignBusinessPartner.County : String [R/W]
CampaignBusinessPartner.CreateActivity : BoYesNoEnum [R/W]
CampaignBusinessPartner.DocEntry : Long [R/W]
CampaignBusinessPartner.DocNumber : Long [R]
CampaignBusinessPartner.DocType : LinkedDocTypeEnum [R/W]
CampaignBusinessPartner.FederalTaxID : String [R/W]
CampaignBusinessPartner.FirstName : String [R/W]
CampaignBusinessPartner.IsShowLinkedDoc : BoYesNoEnum [R/W]
CampaignBusinessPartner.LastName : String [R/W]
CampaignBusinessPartner.MiddleName : String [R/W]
CampaignBusinessPartner.RelatedSalesOpportunity : Long [R/W]
CampaignBusinessPartner.Response : BoYesNoEnum [R/W]
CampaignBusinessPartner.ResponseType : String [R/W]
CampaignBusinessPartner.State : String [R/W]
CampaignBusinessPartner.Street : String [R/W]
CampaignBusinessPartner.StreetNo : String [R/W]
CampaignBusinessPartner.UserFields : Fields [R]
CampaignBusinessPartner.ZipCode : String [R/W]
CampaignBusinessPartner.FromXMLFile(ByVal bstrFileName As String)
CampaignBusinessPartner.FromXMLString(ByVal bstrXML As String)
CampaignBusinessPartner.GetXMLSchema() -> String
CampaignBusinessPartner.ToXMLFile(ByVal bstrFileName As String)
CampaignBusinessPartner.ToXMLString() -> String
CampaignBusinessPartners.Count : Long [R]
CampaignBusinessPartners.Add() -> CampaignBusinessPartner
CampaignBusinessPartners.GetXMLSchema() -> String
CampaignBusinessPartners.Item(ByVal vtIndex As Variant) -> CampaignBusinessPartner
CampaignBusinessPartners.Remove(ByVal vtIndex As Variant)
CampaignBusinessPartners.ToXMLFile(ByVal bstrFileName As String)
CampaignBusinessPartners.ToXMLString() -> String
CampaignItem.CampaignLineNumber : Long [R]
CampaignItem.CampaignNumber : Long [R]
CampaignItem.ItemCode : String [R/W]
CampaignItem.ItemGroup : String [R]
CampaignItem.ItemName : String [R/W]
CampaignItem.ItemType : CampaignItemTypeEnum [R]
CampaignItem.UserFields : Fields [R]
CampaignItem.FromXMLFile(ByVal bstrFileName As String)
CampaignItem.FromXMLString(ByVal bstrXML As String)
CampaignItem.GetXMLSchema() -> String
CampaignItem.ToXMLFile(ByVal bstrFileName As String)
CampaignItem.ToXMLString() -> String
CampaignItems.Count : Long [R]
CampaignItems.Add() -> CampaignItem
CampaignItems.GetXMLSchema() -> String
CampaignItems.Item(ByVal vtIndex As Variant) -> CampaignItem
CampaignItems.Remove(ByVal vtIndex As Variant)
CampaignItems.ToXMLFile(ByVal bstrFileName As String)
CampaignItems.ToXMLString() -> String
CampaignParams.CampaignName : String [R/W]
CampaignParams.CampaignNumber : Long [R/W]
CampaignParams.FromXMLFile(ByVal bstrFileName As String)
CampaignParams.FromXMLString(ByVal bstrXML As String)
CampaignParams.GetXMLSchema() -> String
CampaignParams.ToXMLFile(ByVal bstrFileName As String)
CampaignParams.ToXMLString() -> String
CampaignPartner.CampaignLineNumber : Long [R]
CampaignPartner.CampaignNumber : Long [R]
CampaignPartner.Details : String [R/W]
CampaignPartner.PartnerID : Long [R/W]
CampaignPartner.RelatedBP : String [R/W]
CampaignPartner.RelationshipCode : Long [R/W]
CampaignPartner.UserFields : Fields [R]
CampaignPartner.FromXMLFile(ByVal bstrFileName As String)
CampaignPartner.FromXMLString(ByVal bstrXML As String)
CampaignPartner.GetXMLSchema() -> String
CampaignPartner.ToXMLFile(ByVal bstrFileName As String)
CampaignPartner.ToXMLString() -> String
CampaignPartners.Count : Long [R]
CampaignPartners.Add() -> CampaignPartner
CampaignPartners.GetXMLSchema() -> String
CampaignPartners.Item(ByVal vtIndex As Variant) -> CampaignPartner
CampaignPartners.Remove(ByVal vtIndex As Variant)
CampaignPartners.ToXMLFile(ByVal bstrFileName As String)
CampaignPartners.ToXMLString() -> String
CampaignResponseType.IsActive : BoYesNoEnum [R/W]
CampaignResponseType.ResponseType : String [R/W]
CampaignResponseType.ResponseTypeDescription : String [R/W]
CampaignResponseType.FromXMLFile(ByVal bstrFileName As String)
CampaignResponseType.FromXMLString(ByVal bstrXML As String)
CampaignResponseType.GetXMLSchema() -> String
CampaignResponseType.ToXMLFile(ByVal bstrFileName As String)
CampaignResponseType.ToXMLString() -> String
CampaignResponseTypeParams.IsActive : BoYesNoEnum [R]
CampaignResponseTypeParams.ResponseType : String [R/W]
CampaignResponseTypeParams.ResponseTypeDescription : String [R]
CampaignResponseTypeParams.FromXMLFile(ByVal bstrFileName As String)
CampaignResponseTypeParams.FromXMLString(ByVal bstrXML As String)
CampaignResponseTypeParams.GetXMLSchema() -> String
CampaignResponseTypeParams.ToXMLFile(ByVal bstrFileName As String)
CampaignResponseTypeParams.ToXMLString() -> String
CampaignResponseTypeParamsCollection.Count : Long [R]
CampaignResponseTypeParamsCollection.Add() -> CampaignResponseTypeParams
CampaignResponseTypeParamsCollection.GetXMLSchema() -> String
CampaignResponseTypeParamsCollection.Item(ByVal vtIndex As Variant) -> CampaignResponseTypeParams
CampaignResponseTypeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
CampaignResponseTypeParamsCollection.ToXMLString() -> String
CampaignResponseTypeService.AddResponseType(ByVal pICampaignResponseType As CampaignResponseType) -> CampaignResponseTypeParams
CampaignResponseTypeService.DeleteResponseType(ByVal pICampaignResponseTypeParams As CampaignResponseTypeParams)
CampaignResponseTypeService.GetDataInterface(ByVal enumMSDI As CampaignResponseTypeServiceDataInterfaces) -> Object
CampaignResponseTypeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CampaignResponseTypeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CampaignResponseTypeService.GetResponseType(ByVal pICampaignResponseTypeParams As CampaignResponseTypeParams) -> CampaignResponseType
CampaignResponseTypeService.GetResponseTypeList() -> CampaignResponseTypeParamsCollection
CampaignResponseTypeService.UpdateResponseType(ByVal pICampaignResponseType As CampaignResponseType)
CampaignsParams.Count : Long [R]
CampaignsParams.Add() -> CampaignParams
CampaignsParams.GetXMLSchema() -> String
CampaignsParams.Item(ByVal vtIndex As Variant) -> CampaignParams
CampaignsParams.ToXMLFile(ByVal bstrFileName As String)
CampaignsParams.ToXMLString() -> String
CampaignsService.Add(ByVal pICampaign As Campaign) -> CampaignParams
CampaignsService.Cancel(ByVal pICampaignParams As CampaignParams)
CampaignsService.Delete(ByVal pICampaignParams As CampaignParams)
CampaignsService.Get(ByVal pICampaignParams As CampaignParams) -> Campaign
CampaignsService.GetDataInterface(ByVal enumMSDI As CampaignsServiceDataInterfaces) -> Object
CampaignsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CampaignsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CampaignsService.GetList() -> CampaignsParams
CampaignsService.Update(ByVal pICampaign As Campaign)
CancelCheckRowParams.CheckID : Long [R/W]
CancelCheckRowParams.DepositID : Long [R/W]
CancelCheckRowParams.FromXMLFile(ByVal bstrFileName As String)
CancelCheckRowParams.FromXMLString(ByVal bstrXML As String)
CancelCheckRowParams.GetXMLSchema() -> String
CancelCheckRowParams.ToXMLFile(ByVal bstrFileName As String)
CancelCheckRowParams.ToXMLString() -> String
CashDiscount.ByDate : BoYesNoEnum [R/W]
CashDiscount.Code : String [R/W]
CashDiscount.DiscountLines : DiscountLines [R]
CashDiscount.Freight : BoYesNoEnum [R/W]
CashDiscount.Name : String [R/W]
CashDiscount.Tax : BoYesNoEnum [R/W]
CashDiscount.FromXMLFile(ByVal bstrFileName As String)
CashDiscount.FromXMLString(ByVal bstrXML As String)
CashDiscount.GetXMLSchema() -> String
CashDiscount.ToXMLFile(ByVal bstrFileName As String)
CashDiscount.ToXMLString() -> String
CashDiscountParams.Code : String [R/W]
CashDiscountParams.Name : String [R]
CashDiscountParams.FromXMLFile(ByVal bstrFileName As String)
CashDiscountParams.FromXMLString(ByVal bstrXML As String)
CashDiscountParams.GetXMLSchema() -> String
CashDiscountParams.ToXMLFile(ByVal bstrFileName As String)
CashDiscountParams.ToXMLString() -> String
CashDiscountsParams.Count : Long [R]
CashDiscountsParams.Add() -> CashDiscountParams
CashDiscountsParams.GetXMLSchema() -> String
CashDiscountsParams.Item(ByVal vtIndex As Variant) -> CashDiscountParams
CashDiscountsParams.ToXMLFile(ByVal bstrFileName As String)
CashDiscountsParams.ToXMLString() -> String
CashDiscountsService.AddCashDiscount(ByVal pICashDiscount As CashDiscount) -> CashDiscountParams
CashDiscountsService.DeleteCashDiscount(ByVal pICashDiscountParams As CashDiscountParams)
CashDiscountsService.GetCashDiscount(ByVal pICashDiscountParams As CashDiscountParams) -> CashDiscount
CashDiscountsService.GetCashDiscountList() -> CashDiscountsParams
CashDiscountsService.GetDataInterface(ByVal enumMSDI As CashDiscountsServiceDataInterfaces) -> Object
CashDiscountsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CashDiscountsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CashDiscountsService.UpdateCashDiscount(ByVal pICashDiscount As CashDiscount)
CashFlowAssignments.AmountFC : Double [R/W]
CashFlowAssignments.AmountLC : Double [R/W]
CashFlowAssignments.CashFlowAssignmentsID : Long [R]
CashFlowAssignments.CashFlowLineItemID : Long [R/W]
CashFlowAssignments.CheckNumber : String [R/W]
CashFlowAssignments.Count : Long [R]
CashFlowAssignments.JDTLineId : Long [R/W]
CashFlowAssignments.PaymentMeans : PaymentMeansTypeEnum [R/W]
CashFlowAssignments.Add()
CashFlowAssignments.Delete()
CashFlowAssignments.SetCurrentLine(ByVal LineNum As Long)
CashFlowLineItem.ActiveLineItem : BoYesNoEnum [R]
CashFlowLineItem.Drawer : Long [R]
CashFlowLineItem.Level : Long [R]
CashFlowLineItem.LineItemID : Long [R]
CashFlowLineItem.LineItemName : String [R]
CashFlowLineItem.ParentArticle : Long [R]
CashFlowLineItem.FromXMLFile(ByVal bstrFileName As String)
CashFlowLineItem.FromXMLString(ByVal bstrXML As String)
CashFlowLineItem.GetXMLSchema() -> String
CashFlowLineItem.ToXMLFile(ByVal bstrFileName As String)
CashFlowLineItem.ToXMLString() -> String
CashFlowLineItemParams.LineItemID : Long [R/W]
CashFlowLineItemParams.LineItemName : String [R]
CashFlowLineItemParams.FromXMLFile(ByVal bstrFileName As String)
CashFlowLineItemParams.FromXMLString(ByVal bstrXML As String)
CashFlowLineItemParams.GetXMLSchema() -> String
CashFlowLineItemParams.ToXMLFile(ByVal bstrFileName As String)
CashFlowLineItemParams.ToXMLString() -> String
CashFlowLineItemsParams.Count : Long [R]
CashFlowLineItemsParams.Add() -> CashFlowLineItemParams
CashFlowLineItemsParams.GetXMLSchema() -> String
CashFlowLineItemsParams.Item(ByVal vtIndex As Variant) -> CashFlowLineItemParams
CashFlowLineItemsParams.ToXMLFile(ByVal bstrFileName As String)
CashFlowLineItemsParams.ToXMLString() -> String
CashFlowLineItemsService.GetCashFlowLineItem(ByVal pICashFlowLineItemParams As CashFlowLineItemParams) -> CashFlowLineItem
CashFlowLineItemsService.GetCashFlowLineItemList() -> CashFlowLineItemsParams
CashFlowLineItemsService.GetDataInterface(ByVal enumMSDI As CashFlowLineItemsServiceDataInterfaces) -> Object
CashFlowLineItemsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CashFlowLineItemsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CategoryGroup.AuthGroupId : Long [R/W]
CategoryGroup.CategoryId : Long [R/W]
CategoryGroup.FromXMLFile(ByVal bstrFileName As String)
CategoryGroup.FromXMLString(ByVal bstrXML As String)
CategoryGroup.GetXMLSchema() -> String
CategoryGroup.ToXMLFile(ByVal bstrFileName As String)
CategoryGroup.ToXMLString() -> String
CategoryGroupCollection.Count : Long [R]
CategoryGroupCollection.Add() -> CategoryGroup
CategoryGroupCollection.GetXMLSchema() -> String
CategoryGroupCollection.Item(ByVal vtIndex As Variant) -> CategoryGroup
CategoryGroupCollection.Remove(ByVal vtIndex As Variant)
CategoryGroupCollection.ToXMLFile(ByVal bstrFileName As String)
CategoryGroupCollection.ToXMLString() -> String
CCDNumber.BaseLineNumber : Long [R/W]
CCDNumber.CCDNumber : String [R/W]
CCDNumber.ChildNumber : Long [R/W]
CCDNumber.CountryOfOrigin : String [R/W]
CCDNumber.DocumentEntry : Long [R]
CCDNumber.Quantity : Double [R/W]
CCDNumber.SubLineNumber : Long [R/W]
CCDNumber.TrackingNote : Long [R/W]
CCDNumber.TrackingNoteLine : Long [R/W]
CCDNumber.FromXMLFile(ByVal bstrFileName As String)
CCDNumber.FromXMLString(ByVal bstrXML As String)
CCDNumber.GetXMLSchema() -> String
CCDNumber.ToXMLFile(ByVal bstrFileName As String)
CCDNumber.ToXMLString() -> String
CCDNumbers.BaseLineNumber : Long [R/W]
CCDNumbers.CCDNumber : String [R/W]
CCDNumbers.ChildNumber : Long [R/W]
CCDNumbers.Count : Long [R]
CCDNumbers.CountryOfOrigin : String [R/W]
CCDNumbers.DocumentEntry : Long [R]
CCDNumbers.Quantity : Double [R/W]
CCDNumbers.SubLineNumber : Long [R/W]
CCDNumbers.TrackingNote : Long [R/W]
CCDNumbers.TrackingNoteLine : Long [R/W]
CCDNumbers.Add()
CCDNumbers.SetCurrentLine(ByVal LineNum As Long)
CertificateSeries.AbsEntry : Long [R]
CertificateSeries.Code : String [R/W]
CertificateSeries.DefaultSeries : Long [R/W]
CertificateSeries.Location : Long [R/W]
CertificateSeries.Section : Long [R/W]
CertificateSeries.SeriesLines : SeriesLines [R]
CertificateSeries.FromXMLFile(ByVal bstrFileName As String)
CertificateSeries.FromXMLString(ByVal bstrXML As String)
CertificateSeries.GetXMLSchema() -> String
CertificateSeries.ToXMLFile(ByVal bstrFileName As String)
CertificateSeries.ToXMLString() -> String
CertificateSeriesParams.AbsEntry : Long [R/W]
CertificateSeriesParams.Code : String [R]
CertificateSeriesParams.Location : Long [R]
CertificateSeriesParams.Section : Long [R]
CertificateSeriesParams.FromXMLFile(ByVal bstrFileName As String)
CertificateSeriesParams.FromXMLString(ByVal bstrXML As String)
CertificateSeriesParams.GetXMLSchema() -> String
CertificateSeriesParams.ToXMLFile(ByVal bstrFileName As String)
CertificateSeriesParams.ToXMLString() -> String
CertificateSeriesParamsCollection.Count : Long [R]
CertificateSeriesParamsCollection.Add() -> CertificateSeriesParams
CertificateSeriesParamsCollection.GetXMLSchema() -> String
CertificateSeriesParamsCollection.Item(ByVal vtIndex As Variant) -> CertificateSeriesParams
CertificateSeriesParamsCollection.ToXMLFile(ByVal bstrFileName As String)
CertificateSeriesParamsCollection.ToXMLString() -> String
CertificateSeriesService.AddCertificateSeries(ByVal pICertificateSeries As CertificateSeries) -> CertificateSeriesParams
CertificateSeriesService.DeleteCertificateSeries(ByVal pICertificateSeriesParams As CertificateSeriesParams)
CertificateSeriesService.GetCertificateSeries(ByVal pICertificateSeriesParams As CertificateSeriesParams) -> CertificateSeries
CertificateSeriesService.GetCertificateSeriesList() -> CertificateSeriesParamsCollection
CertificateSeriesService.GetDataInterface(ByVal enumMSDI As CertificateSeriesServiceDataInterfaces) -> Object
CertificateSeriesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CertificateSeriesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CertificateSeriesService.UpdateCertificateSeries(ByVal pICertificateSeries As CertificateSeries)
CESTCodeData.AbsEntry : Long [R/W]
CESTCodeData.Code : String [R/W]
CESTCodeData.Description : String [R/W]
CESTCodeData.FromXMLFile(ByVal bstrFileName As String)
CESTCodeData.FromXMLString(ByVal bstrXML As String)
CESTCodeData.GetXMLSchema() -> String
CESTCodeData.ToXMLFile(ByVal bstrFileName As String)
CESTCodeData.ToXMLString() -> String
CESTCodeParams.AbsEntry : Long [R/W]
CESTCodeParams.FromXMLFile(ByVal bstrFileName As String)
CESTCodeParams.FromXMLString(ByVal bstrXML As String)
CESTCodeParams.GetXMLSchema() -> String
CESTCodeParams.ToXMLFile(ByVal bstrFileName As String)
CESTCodeParams.ToXMLString() -> String
CESTCodeService.Add(ByVal pICESTCodeData As CESTCodeData) -> CESTCodeParams
CESTCodeService.Delete(ByVal pICESTCodeParams As CESTCodeParams)
CESTCodeService.GetByParams(ByVal pICESTCodeParams As CESTCodeParams) -> CESTCodeData
CESTCodeService.GetDataInterface(ByVal enumMSDI As CESTCodeServiceDataInterfaces) -> Object
CESTCodeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CESTCodeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CESTCodeService.Update(ByVal pICESTCodeData As CESTCodeData)
ChangeLogDifferenceParams.ArrayOffset : Long [R]
ChangeLogDifferenceParams.ChangedField : String [R]
ChangeLogDifferenceParams.Date : Date [R]
ChangeLogDifferenceParams.LineNumber : String [R]
ChangeLogDifferenceParams.NewValue : String [R]
ChangeLogDifferenceParams.OldValue : String [R]
ChangeLogDifferenceParams.UserName : String [R]
ChangeLogDifferenceParams.FromXMLFile(ByVal bstrFileName As String)
ChangeLogDifferenceParams.FromXMLString(ByVal bstrXML As String)
ChangeLogDifferenceParams.GetXMLSchema() -> String
ChangeLogDifferenceParams.ToXMLFile(ByVal bstrFileName As String)
ChangeLogDifferenceParams.ToXMLString() -> String
ChangeLogDifferencesParams.Count : Long [R]
ChangeLogDifferencesParams.Add() -> ChangeLogDifferenceParams
ChangeLogDifferencesParams.GetXMLSchema() -> String
ChangeLogDifferencesParams.Item(ByVal vtIndex As Variant) -> ChangeLogDifferenceParams
ChangeLogDifferencesParams.ToXMLFile(ByVal bstrFileName As String)
ChangeLogDifferencesParams.ToXMLString() -> String
ChangeLogParams.LogInstance : Long [R]
ChangeLogParams.ObjectCode : String [R]
ChangeLogParams.UpdatedDate : Date [R]
ChangeLogParams.UserName : String [R]
ChangeLogParams.FromXMLFile(ByVal bstrFileName As String)
ChangeLogParams.FromXMLString(ByVal bstrXML As String)
ChangeLogParams.GetXMLSchema() -> String
ChangeLogParams.ToXMLFile(ByVal bstrFileName As String)
ChangeLogParams.ToXMLString() -> String
ChangeLogsParams.Count : Long [R]
ChangeLogsParams.Add() -> ChangeLogParams
ChangeLogsParams.GetXMLSchema() -> String
ChangeLogsParams.Item(ByVal vtIndex As Variant) -> ChangeLogParams
ChangeLogsParams.ToXMLFile(ByVal bstrFileName As String)
ChangeLogsParams.ToXMLString() -> String
ChangeLogsService.GetChangeLog(ByVal pIGetChangeLogParams As GetChangeLogParams) -> ChangeLogsParams
ChangeLogsService.GetChangeLogDifferences(ByVal pIShowDifferenceParams As ShowDifferenceParams) -> ChangeLogDifferencesParams
ChangeLogsService.GetDataInterface(ByVal enumMSDI As ChangeLogsServiceDataInterfaces) -> Object
ChangeLogsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ChangeLogsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ChartOfAccounts.AccountLevel : Long [R]
ChartOfAccounts.AccountPurposeCode : SPEDContabilAccountPurposeCode [R/W]
ChartOfAccounts.AccountType : BoAccountTypes [R/W]
ChartOfAccounts.AcctCurrency : String [R/W]
ChartOfAccounts.ActiveAccount : BoYesNoEnum [R/W]
ChartOfAccounts.AllowChangeVatGroup : BoYesNoEnum [R/W]
ChartOfAccounts.AllowMultipleLinking : BoYesNoEnum [R/W]
ChartOfAccounts.Balance : Double [R]
ChartOfAccounts.Balance_FrgnCurr : Double [R]
ChartOfAccounts.Balance_syscurr : Double [R]
ChartOfAccounts.BlockManualPosting : BoYesNoEnum [R/W]
ChartOfAccounts.BPLID : Long [R/W]
ChartOfAccounts.BPLName : String [R]
ChartOfAccounts.Browser : DataBrowser [R]
ChartOfAccounts.BudgetAccount : BoYesNoEnum [R/W]
ChartOfAccounts.CashAccount : BoYesNoEnum [R/W]
ChartOfAccounts.CashFlowRelevant : BoYesNoEnum [R/W]
ChartOfAccounts.Category : Long [R/W]
ChartOfAccounts.Code : String [R/W]
ChartOfAccounts.CostAccountingOnly : BoYesNoEnum [R/W]
ChartOfAccounts.CostElementCode : String [R/W]
ChartOfAccounts.CostElementRelevant : BoYesNoEnum [R/W]
ChartOfAccounts.DataExportCode : String [R/W]
ChartOfAccounts.DatevAccount : String [R/W]
ChartOfAccounts.DatevAutoAccount : BoYesNoEnum [R/W]
ChartOfAccounts.DatevFirstDataEntry : BoYesNoEnum [R/W]
ChartOfAccounts.DefaultVatGroup : String [R/W]
ChartOfAccounts.Details : String [R/W]
ChartOfAccounts.DistributionRule2Relevant : BoYesNoEnum [R/W]
ChartOfAccounts.DistributionRule3Relevant : BoYesNoEnum [R/W]
ChartOfAccounts.DistributionRule4Relevant : BoYesNoEnum [R/W]
ChartOfAccounts.DistributionRule5Relevant : BoYesNoEnum [R/W]
ChartOfAccounts.DistributionRuleRelevant : BoYesNoEnum [R/W]
ChartOfAccounts.ExpenseClassificationCategory : Long [R/W]
ChartOfAccounts.ExpenseClassificationType : Long [R/W]
ChartOfAccounts.ExternalCode : String [R/W]
ChartOfAccounts.ExternalReconNo : Long [R]
ChartOfAccounts.FatherAccountKey : String [R/W]
ChartOfAccounts.ForeignName : String [R/W]
ChartOfAccounts.FormatCode : String [R/W]
ChartOfAccounts.FrozenFor : BoYesNoEnum [R/W]
ChartOfAccounts.FrozenFrom : Date [R/W]
ChartOfAccounts.FrozenRemarks : String [R/W]
ChartOfAccounts.FrozenTo : Date [R/W]
ChartOfAccounts.IncomeClassificationCategory : Long [R/W]
ChartOfAccounts.IncomeClassificationType : Long [R/W]
ChartOfAccounts.InternalReconNo : Long [R]
ChartOfAccounts.LiableForAdvances : BoYesNoEnum [R/W]
ChartOfAccounts.LoadingFactorCode : String [R/W]
ChartOfAccounts.LoadingFactorCode2 : String [R/W]
ChartOfAccounts.LoadingFactorCode3 : String [R/W]
ChartOfAccounts.LoadingFactorCode4 : String [R/W]
ChartOfAccounts.LoadingFactorCode5 : String [R/W]
ChartOfAccounts.LoadingType : BoYesNoEnum [R/W]
ChartOfAccounts.LockManualTransaction : BoYesNoEnum [R/W]
ChartOfAccounts.Name : String [R/W]
ChartOfAccounts.PCN874ReportRelevant : BoYesNoEnum [R/W]
ChartOfAccounts.PlanningLevel : String [R/W]
ChartOfAccounts.PrimaryAccount : BoYesNoEnum [R]
ChartOfAccounts.PrimaryClosingAccount : String [R/W]
ChartOfAccounts.ProjectCode : String [R/W]
ChartOfAccounts.ProjectRelevant : BoYesNoEnum [R/W]
ChartOfAccounts.Protected : BoYesNoEnum [R/W]
ChartOfAccounts.RateConversion : BoYesNoEnum [R/W]
ChartOfAccounts.ReconciledAccount : BoYesNoEnum [R/W]
ChartOfAccounts.ReferentialAccountCode : String [R/W]
ChartOfAccounts.RevaluationCoordinated : BoYesNoEnum [R/W]
ChartOfAccounts.StandardAccountCode : String [R/W]
ChartOfAccounts.TaxExemptAccount : BoYesNoEnum [R/W]
ChartOfAccounts.TaxLiableAccount : BoYesNoEnum [R/W]
ChartOfAccounts.TaxonomyCode : String [R/W]
ChartOfAccounts.TransactionCode : String [R/W]
ChartOfAccounts.UserFields : UserFields [R]
ChartOfAccounts.ValidFor : BoYesNoEnum [R/W]
ChartOfAccounts.ValidFrom : Date [R/W]
ChartOfAccounts.ValidRemarks : String [R/W]
ChartOfAccounts.ValidTo : Date [R/W]
ChartOfAccounts.VATRegNum : String [R]
ChartOfAccounts.Add() -> Long
ChartOfAccounts.GetAsXML() -> String
ChartOfAccounts.GetByKey(ByVal AccountCode As String) -> Boolean
ChartOfAccounts.Remove() -> Long
ChartOfAccounts.SaveToFile(ByVal FileName As String)
ChartOfAccounts.SaveXML(ByRef FileName As String)
ChartOfAccounts.Update() -> Long
CheckLine.AccountNumber : String [R]
CheckLine.Bank : String [R]
CheckLine.Branch : String [R]
CheckLine.CashCheck : String [R]
CheckLine.CheckAmount : Double [R]
CheckLine.CheckCurrency : String [R]
CheckLine.CheckDate : Date [R]
CheckLine.CheckKey : Long [R/W]
CheckLine.CheckNumber : Long [R]
CheckLine.Customer : String [R]
CheckLine.Deposited : BoDepositCheckEnum [R]
CheckLine.FiscalID : String [R]
CheckLine.OriginallyIssuedBy : String [R]
CheckLine.RejectedByBank : BoYesNoEnum [R]
CheckLine.Transferred : BoYesNoEnum [R]
CheckLine.FromXMLFile(ByVal bstrFileName As String)
CheckLine.FromXMLString(ByVal bstrXML As String)
CheckLine.GetXMLSchema() -> String
CheckLine.ToXMLFile(ByVal bstrFileName As String)
CheckLine.ToXMLString() -> String
CheckLineParams.CheckKey : Long [R/W]
CheckLineParams.FromXMLFile(ByVal bstrFileName As String)
CheckLineParams.FromXMLString(ByVal bstrXML As String)
CheckLineParams.GetXMLSchema() -> String
CheckLineParams.ToXMLFile(ByVal bstrFileName As String)
CheckLineParams.ToXMLString() -> String
CheckLines.Count : Long [R]
CheckLines.Add() -> CheckLine
CheckLines.GetXMLSchema() -> String
CheckLines.Item(ByVal vtIndex As Variant) -> CheckLine
CheckLines.ToXMLFile(ByVal bstrFileName As String)
CheckLines.ToXMLString() -> String
CheckLinesParams.Count : Long [R]
CheckLinesParams.Add() -> CheckLineParams
CheckLinesParams.GetXMLSchema() -> String
CheckLinesParams.Item(ByVal vtIndex As Variant) -> CheckLineParams
CheckLinesParams.ToXMLFile(ByVal bstrFileName As String)
CheckLinesParams.ToXMLString() -> String
CheckLinesService.GetCheckLine(ByVal pICheckLineParams As CheckLineParams) -> CheckLine
CheckLinesService.GetDataInterface(ByVal enumMSDI As CheckLinesServiceDataInterfaces) -> Object
CheckLinesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CheckLinesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CheckLinesService.GetValidCheckLineList() -> CheckLinesParams
ChecksforPayment.AccountNumber : String [R/W]
ChecksforPayment.Address : String [R/W]
ChecksforPayment.AddressName : String [R/W]
ChecksforPayment.AttachmentEntry : Long [R/W]
ChecksforPayment.BankCode : String [R/W]
ChecksforPayment.BankName : String [R]
ChecksforPayment.Branch : String [R/W]
ChecksforPayment.Browser : DataBrowser [R]
ChecksforPayment.Canceled : BoYesNoEnum [R]
ChecksforPayment.CardOrAccount : BoCpCardAcct [R/W]
ChecksforPayment.CheckAmount : Double [R]
ChecksforPayment.CheckCurrency : String [R]
ChecksforPayment.CheckDate : Date [R/W]
ChecksforPayment.CheckKey : Long [R]
ChecksforPayment.CheckNumber : Long [R/W]
ChecksforPayment.CountryCode : String [R/W]
ChecksforPayment.CreateJournalEntry : BoYesNoEnum [R/W]
ChecksforPayment.CreationDate : Date [R]
ChecksforPayment.CustomerAccountCode : String [R/W]
ChecksforPayment.DeductionRefundAmount : Double [R/W]
ChecksforPayment.Details : String [R/W]
ChecksforPayment.DocumentReferences : ChecksforPaymentDocumentReferences [R]
ChecksforPayment.ECheck : BoYesNoEnum [R/W]
ChecksforPayment.JournalEntryReference : String [R/W]
ChecksforPayment.Lines : ChecksforPaymentLines [R]
ChecksforPayment.ManualCheck : BoYesNoEnum [R/W]
ChecksforPayment.PaymentDate : Date [R/W]
ChecksforPayment.PaymentNo : Long [R]
ChecksforPayment.PrintConfirm : BoYesNoEnum [R/W]
ChecksforPayment.Printed : BoYesNoEnum [R/W]
ChecksforPayment.PrintedBy : Long [R]
ChecksforPayment.PrintStatus : ChecksforPaymentPrintStatus [R]
ChecksforPayment.Signature : String [R/W]
ChecksforPayment.TaxDate : Date [R]
ChecksforPayment.TaxTotal : Double [R]
ChecksforPayment.TotalinWords : String [R/W]
ChecksforPayment.TransactionNumber : Long [R]
ChecksforPayment.Transferable : BoYesNoEnum [R/W]
ChecksforPayment.UpdateDate : Date [R]
ChecksforPayment.UserFields : UserFields [R]
ChecksforPayment.VendorCode : String [R/W]
ChecksforPayment.VendorName : String [R]
ChecksforPayment.WithholdingTaxAmount : Double [R]
ChecksforPayment.WithholdingTaxPercentage : Double [R/W]
ChecksforPayment.Add() -> Long
ChecksforPayment.Cancel() -> Long
ChecksforPayment.Close() -> Long
ChecksforPayment.GetAsXML() -> String
ChecksforPayment.GetByKey(ByVal CheckKey As Long) -> Boolean
ChecksforPayment.Remove() -> Long
ChecksforPayment.SaveToFile(ByVal FileName As String)
ChecksforPayment.SaveXML(ByRef FileName As String)
ChecksforPayment.Update() -> Long
ChecksforPaymentDocumentReferences.Count : Long [R]
ChecksforPaymentDocumentReferences.DocEntry : Long [R]
ChecksforPaymentDocumentReferences.ExternalReferencedDocNumber : String [R/W]
ChecksforPaymentDocumentReferences.IssueDate : Date [R/W]
ChecksforPaymentDocumentReferences.LineNumber : Long [R]
ChecksforPaymentDocumentReferences.ReferencedDocEntry : Long [R/W]
ChecksforPaymentDocumentReferences.ReferencedDocNumber : Long [R]
ChecksforPaymentDocumentReferences.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
ChecksforPaymentDocumentReferences.Remark : String [R/W]
ChecksforPaymentDocumentReferences.Add()
ChecksforPaymentDocumentReferences.SetCurrentLine(ByVal LineNum As Long)
ChecksforPaymentLines.Count : Long [R]
ChecksforPaymentLines.CreditedAccount : String [R/W]
ChecksforPaymentLines.LineTotal : Double [R]
ChecksforPaymentLines.RowCurrency : String [R/W]
ChecksforPaymentLines.RowDetails : String [R/W]
ChecksforPaymentLines.RowNumber : Long [R]
ChecksforPaymentLines.RowTotal : Double [R/W]
ChecksforPaymentLines.TaxDefinition : String [R/W]
ChecksforPaymentLines.TaxPercent : Double [R]
ChecksforPaymentLines.UserFields : UserFields [R]
ChecksforPaymentLines.Add()
ChecksforPaymentLines.SetCurrentLine(ByVal LineNum As Long)
ChecksforPaymentPrintStatus.CheckNumber : Long [R/W]
ChecksforPaymentPrintStatus.Count : Long [R]
ChecksforPaymentPrintStatus.DocEntry : Long [R/W]
ChecksforPaymentPrintStatus.LineNumber : Long [R/W]
ChecksforPaymentPrintStatus.PrintedBy : Long [R/W]
ChecksforPaymentPrintStatus.PrintStatus : String [R/W]
ChecksforPaymentPrintStatus.Add()
ChecksforPaymentPrintStatus.SetCurrentLine(ByVal LineNum As Long)
ChooseFromList.Browser : DataBrowser [R]
ChooseFromList.ChooseFromList_Lines : ChooseFromList_Lines [R]
ChooseFromList.ObjectName : String [R/W]
ChooseFromList.UserFields : UserFields [R]
ChooseFromList.Add() -> Long
ChooseFromList.GetAsXML() -> String
ChooseFromList.GetByKey(ByVal bstrObjectName As String) -> Boolean
ChooseFromList.Remove() -> Long
ChooseFromList.SaveToFile(ByVal bstrFileName As String)
ChooseFromList.SaveXML(ByRef pbstrFileName As String)
ChooseFromList.Update() -> Long
ChooseFromList_Lines.Count : Long [R]
ChooseFromList_Lines.DisplayedName : String [R/W]
ChooseFromList_Lines.FieldNo : String [R/W]
ChooseFromList_Lines.GroupBy : BoYesNoEnum [R/W]
ChooseFromList_Lines.ShowType : BoYesNoEnum [R/W]
ChooseFromList_Lines.SortOrder : SortOrderEnum [R/W]
ChooseFromList_Lines.UserFields : UserFields [R]
ChooseFromList_Lines.Visible : BoYesNoEnum [R/W]
ChooseFromList_Lines.VisualIndex : Long [R/W]
ChooseFromList_Lines.Add()
ChooseFromList_Lines.SetCurrentLine(ByVal LineNum As Long)
ClosingDateProcedure.BaselineDate : BoClosingDateProcedureBaseDateEnum [R]
ClosingDateProcedure.Browser : DataBrowser [R]
ClosingDateProcedure.ClosingDateCode : String [R]
ClosingDateProcedure.ClosingDateNum : Long [R]
ClosingDateProcedure.DueMonth : BoClosingDateProcedureDueMonthEnum [R]
ClosingDateProcedure.ExtraDay : Long [R]
ClosingDateProcedure.ExtraMonth : Long [R]
ClosingDateProcedure.UserFields : UserFields [R]
ClosingDateProcedure.GetAsXML() -> String
ClosingDateProcedure.GetByKey(ByVal ClosingDateNum As Long) -> Boolean
ClosingDateProcedure.SaveToFile(ByVal FileName As String)
ClosingDateProcedure.SaveXML(ByRef FileName As String)
Cockpit.AbsEntry : Long [R]
Cockpit.CockpitType : BoCockpitTypeEnum [R]
Cockpit.Code : Long [R]
Cockpit.Date : Date [R]
Cockpit.Description : String [R/W]
Cockpit.Manufacturer : String [R/W]
Cockpit.Name : String [R/W]
Cockpit.Publisher : String [R]
Cockpit.Time : Date [R]
Cockpit.UserSignature : Long [R]
Cockpit.FromXMLFile(ByVal bstrFileName As String)
Cockpit.FromXMLString(ByVal bstrXML As String)
Cockpit.GetXMLSchema() -> String
Cockpit.ToXMLFile(ByVal bstrFileName As String)
Cockpit.ToXMLString() -> String
CockpitParams.AbsEntry : Long [R/W]
CockpitParams.CockpitType : BoCockpitTypeEnum [R]
CockpitParams.FromXMLFile(ByVal bstrFileName As String)
CockpitParams.FromXMLString(ByVal bstrXML As String)
CockpitParams.GetXMLSchema() -> String
CockpitParams.ToXMLFile(ByVal bstrFileName As String)
CockpitParams.ToXMLString() -> String
CockpitsParams.Count : Long [R]
CockpitsParams.Add() -> CockpitParams
CockpitsParams.GetXMLSchema() -> String
CockpitsParams.Item(ByVal vtIndex As Variant) -> CockpitParams
CockpitsParams.ToXMLFile(ByVal bstrFileName As String)
CockpitsParams.ToXMLString() -> String
CockpitsService.AddCockpit(ByVal pICockpit As Cockpit) -> CockpitParams
CockpitsService.DeleteCockpit(ByVal pICockpitParams As CockpitParams)
CockpitsService.GetCockpit(ByVal pICockpitParams As CockpitParams) -> Cockpit
CockpitsService.GetCockpitList() -> CockpitsParams
CockpitsService.GetDataInterface(ByVal enumMSDI As CockpitsServiceDataInterfaces) -> Object
CockpitsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CockpitsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CockpitsService.GetTemplateCockpitList() -> CockpitsParams
CockpitsService.GetUserCockpitList() -> CockpitsParams
CockpitsService.PublishCockpit(ByVal pICockpit As Cockpit)
CockpitsService.UpdateCockpit(ByVal pICockpit As Cockpit)
ColumnPreferences.Column : String [R/W]
ColumnPreferences.EditableInExpanded : BoYesNoEnum [R/W]
ColumnPreferences.EditableInForm : BoYesNoEnum [R/W]
ColumnPreferences.ExpandedIndex : Long [R/W]
ColumnPreferences.FormID : String [R/W]
ColumnPreferences.ItemNumber : String [R/W]
ColumnPreferences.TabsLayout : Long [R/W]
ColumnPreferences.User : Long [R/W]
ColumnPreferences.VisibleInExpanded : BoYesNoEnum [R/W]
ColumnPreferences.VisibleInForm : BoYesNoEnum [R/W]
ColumnPreferences.Width : Long [R/W]
ColumnPreferences.FromXMLFile(ByVal bstrFileName As String)
ColumnPreferences.FromXMLString(ByVal bstrXML As String)
ColumnPreferences.GetXMLSchema() -> String
ColumnPreferences.ToXMLFile(ByVal bstrFileName As String)
ColumnPreferences.ToXMLString() -> String
ColumnsPreferences.Count : Long [R]
ColumnsPreferences.Add() -> ColumnPreferences
ColumnsPreferences.GetXMLSchema() -> String
ColumnsPreferences.Item(ByVal vtIndex As Variant) -> ColumnPreferences
ColumnsPreferences.ToXMLFile(ByVal bstrFileName As String)
ColumnsPreferences.ToXMLString() -> String
ColumnsPreferencesParams.FormID : String [R/W]
ColumnsPreferencesParams.User : Long [R/W]
ColumnsPreferencesParams.FromXMLFile(ByVal bstrFileName As String)
ColumnsPreferencesParams.FromXMLString(ByVal bstrXML As String)
ColumnsPreferencesParams.GetXMLSchema() -> String
ColumnsPreferencesParams.ToXMLFile(ByVal bstrFileName As String)
ColumnsPreferencesParams.ToXMLString() -> String
Command.Name : String [R/W]
Command.Parameters : CommandParams [R]
Command.Execute()
CommandParam.Direction : BoRecCommParamTypes [R]
CommandParam.Name : String [R]
CommandParam.Type : BoFieldTypes [R]
CommandParam.Value : Variant [R/W]
CommandParams.Count : Long [R]
CommandParams.Item(ByVal Index As Variant) -> CommandParam
CommissionGroups.Browser : DataBrowser [R]
CommissionGroups.CommissionGroupCode : Long [R]
CommissionGroups.CommissionGroupName : String [R/W]
CommissionGroups.CommissionPercentage : Double [R/W]
CommissionGroups.UserFields : UserFields [R]
CommissionGroups.Add() -> Long
CommissionGroups.GetAsXML() -> String
CommissionGroups.GetByKey(ByVal lGroupCode As Long) -> Boolean
CommissionGroups.Remove() -> Long
CommissionGroups.SaveToFile(ByVal bstrFileName As String)
CommissionGroups.SaveXML(ByRef pbstrFileName As String)
CommissionGroups.Update() -> Long
Company.AddonIdentifier : String [R/W]
Company.Application : Object [W]
Company.AttachMentPath : String [R]
Company.BitMapPath : String [R]
Company.CompanyDB : String [R/W]
Company.CompanyName : String [R]
Company.Connected : Boolean [R]
Company.DbPassword : String [R/W]
Company.DbServerType : BoDataServerTypes [R/W]
Company.DbUserName : String [R/W]
Company.DTCTransactionObject : Unknown [R/W]
Company.ExcelDocsPath : String [R]
Company.InTransaction : Boolean [R]
Company.language : BoSuppLangs [R/W]
Company.LicenseServer : String [R/W]
Company.MinimalSupportedVersion : Long [R]
Company.Password : String [R/W]
Company.SecurityCode : String [R/W]
Company.Server : String [R/W]
Company.SLDServer : String [R/W]
Company.UserName : String [R/W]
Company.UserSignature : Long [R]
Company.UserTables : UserTables [R]
Company.UseTrusted : Boolean [R/W]
Company.Version : Long [R]
Company.WordDocsPath : String [R]
Company.XMLAsString : Boolean [R/W]
Company.XmlExportType : BoXmlExportTypes [R/W]
Company.AuthenticateUser(ByVal bstrUserName As String, ByVal bstrPassword As String) -> AuthenticateUserResultsEnum
Company.ChangePassword(ByVal NewPassword As String) -> Long
Company.Connect() -> Long
Company.Disconnect()
Company.EndTransaction(ByVal endType As BoWfTransOpt)
Company.GetBusinessObject(ByVal Object As BoObjectTypes) -> Object
Company.GetBusinessObjectFromXML(ByVal FileName As String, ByVal Index As Long) -> Object
Company.GetBusinessObjectXmlSchema(ByVal Object As BoObjectTypes) -> String
Company.GetCompanyDate() -> Date
Company.GetCompanyList() -> Recordset
Company.GetCompanyService() -> CompanyService
Company.GetCompanyTime() -> String
Company.GetContextCookie() -> String
Company.GetDBServerDate() -> Date
Company.GetDBServerTime() -> String
Company.GetLastError(ByRef errCode As Long, ByRef errMsg As String)
Company.GetLastErrorCode() -> Long
Company.GetLastErrorContext() -> String
Company.GetLastErrorDescription() -> String
Company.GetNewObjectCode(ByRef ObjectCode As String)
Company.GetNewObjectKey() -> String
Company.GetNewObjectType() -> String
Company.GetRegisteredServersList() -> Recordset
Company.GetXMLelementCount(ByVal FileName As String) -> Long
Company.GetXMLobjectType(ByVal FileName As String, ByVal Index As Long) -> BoObjectTypes
Company.IsDTCTransactionObjectSet() -> Boolean
Company.SetSboLoginContext(ByVal conStr As String) -> Long
Company.StartTransaction()
CompanyInfo.AutoCreateCustomerEqCard : BoYesNoEnum [R/W]
CompanyInfo.AutoSRICreationOnReceipt : BoYesNoEnum [R/W]
CompanyInfo.B1iTimeOut : Long [R/W]
CompanyInfo.BaseDateForExchangeRate : BoBaseDateRateEnum [R/W]
CompanyInfo.BISRBankAccount : String [R]
CompanyInfo.BISRBankActKey : Long [R/W]
CompanyInfo.BISRBankCountry : String [R]
CompanyInfo.BISRBankNo : String [R]
CompanyInfo.BISRBranch : String [R]
CompanyInfo.BlockStockNegativeQuantity : BoYesNoEnum [R/W]
CompanyInfo.CompanyName : String [R]
CompanyInfo.DataOwnershipIndication : BoYesNoEnum [R/W]
CompanyInfo.DefaultDaysForOrdCanc : Long [R/W]
CompanyInfo.DefaultStampTax : String [R/W]
CompanyInfo.DisplayTransactionsByDflt : BoYesNoEnum [R/W]
CompanyInfo.EnableAccountSegmentation : BoYesNoEnum [R/W]
CompanyInfo.EnableBillOfExchange : BoYesNoEnum [R/W]
CompanyInfo.EnableCheckQuantityInRDR : BoYesNoEnum [R/W]
CompanyInfo.EnableConversionDifferentAcct : BoYesNoEnum [R]
CompanyInfo.EnableExpensesManagement : BoYesNoEnum [R/W]
CompanyInfo.EnableStockRelNoCostPrice : BoYesNoEnum [R/W]
CompanyInfo.EnableTransactionNotification : BoYesNoEnum [R/W]
CompanyInfo.GroupLinesInVATCalculation : BoYesNoEnum [R]
CompanyInfo.IEPSPayer : BoYesNoEnum [R/W]
CompanyInfo.LanguageCode : BoSuppLangs [R/W]
CompanyInfo.Localization : String [R]
CompanyInfo.MaxNumberOfDocumentsInPmt : Long [R/W]
CompanyInfo.MaxRecordsInChooseFromList : Long [R/W]
CompanyInfo.MinimumAmountForAnnualList : Double [R/W]
CompanyInfo.MinimumAmountForAppndixOP : Double [R/W]
CompanyInfo.MinimumBaseAmountPerDoc : Double [R/W]
CompanyInfo.PercentOfTotalAcquisition : Double [R/W]
CompanyInfo.SRIManagementSystem : BoManageMethod [R/W]
CompanyInfo.TaxCalculationSystem : TaxCalcSysEnum [R]
CompanyInfo.Version : Long [R]
CompanyInfo.FromXMLFile(ByVal bstrFileName As String)
CompanyInfo.FromXMLString(ByVal bstrXML As String)
CompanyInfo.GetXMLSchema() -> String
CompanyInfo.ToXMLFile(ByVal bstrFileName As String)
CompanyInfo.ToXMLString() -> String
CompanyService.CreatePeriod(ByVal pIPeriodCategory As PeriodCategory) -> PeriodCategoryParams
CompanyService.CreatePeriodWithFinanceParams(ByVal pIPeriodCategory As PeriodCategory, ByVal pIFinancePeriodParams As FinancePeriodParams) -> PeriodCategoryParams
CompanyService.GetAdminInfo() -> AdminInfo
CompanyService.GetAdvancedGLAccount(ByVal pIAdvancedGLAccountParams As AdvancedGLAccountParams) -> AdvancedGLAccountReturnParams
CompanyService.GetBlob(ByVal pIBlobParams As BlobParams) -> Blob
CompanyService.GetBusinessService(ByVal enumServiceType As ServiceTypes) -> Object
CompanyService.GetCompanyInfo() -> CompanyInfo
CompanyService.GetDataInterface(ByVal enumMSDI As CompanyServiceDataInterfaces) -> Object
CompanyService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CompanyService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CompanyService.GetFeaturesStatus() -> FeatureStatusCollection
CompanyService.GetFinancePeriod(ByVal pIFinancePeriodParams As FinancePeriodParams) -> FinancePeriod
CompanyService.GetFinancePeriods(ByVal pIPeriodCategoryParams As PeriodCategoryParams) -> FinancePeriods
CompanyService.GetGeneralService(ByVal sServiceCode As String) -> GeneralService
CompanyService.GetItemPrice(ByVal pIItemPriceParams As ItemPriceParams) -> ItemPriceReturnParams
CompanyService.GetPathAdmin() -> PathAdmin
CompanyService.GetPeriod(ByVal pIPeriodCategoryParams As PeriodCategoryParams) -> PeriodCategory
CompanyService.GetPeriods() -> PeriodCategoryParamsCollection
CompanyService.GetServiceMetaData(ByVal ServiceCode As ServiceTypes) -> String
CompanyService.IsUserLicensed(ByVal bstrUserName As String, ByVal bstrLicType As String) -> Boolean
CompanyService.LoadBlobFromFile(ByVal pIBlobParams As BlobParams)
CompanyService.RoundDecimal(ByVal pIDecimalData As DecimalData) -> RoundedData
CompanyService.SaveBlobToFile(ByVal pIBlobParams As BlobParams)
CompanyService.SetBlob(ByVal pIBlobParams As BlobParams, ByVal pIBlob As Blob)
CompanyService.UpdateAdminInfo(ByVal pIAdminInfo As AdminInfo)
CompanyService.UpdateCompanyInfo(ByVal pICompanyInfo As CompanyInfo)
CompanyService.UpdateFinancePeriod(ByVal pIFinancePeriod As FinancePeriod)
CompanyService.UpdatePathAdmin(ByVal pIPathAdmin As PathAdmin)
CompanyService.UpdatePeriod(ByVal pIPeriodCategory As PeriodCategory)
CompanyService.UpdateUserLicense(ByVal pIUserLicenseParams As UserLicenseParams)
ContactEmployeeBlockSendingMarketingContents.Choose : BoYesNoEnum [R/W]
ContactEmployeeBlockSendingMarketingContents.CommunicationMediaId : Long [R/W]
ContactEmployeeBlockSendingMarketingContents.ContactEmployeeAbsEntry : Long [R/W]
ContactEmployeeBlockSendingMarketingContents.Add()
ContactEmployeeBlockSendingMarketingContents.Delete()
ContactEmployeeBlockSendingMarketingContents.SetCurrentLine(ByVal LineNum As Long)
ContactEmployees.Active : BoYesNoEnum [R/W]
ContactEmployees.Address : String [R/W]
ContactEmployees.BlockSendingMarketingContent : BoYesNoEnum [R/W]
ContactEmployees.CardCode : String [R]
ContactEmployees.CityOfBirth : String [R/W]
ContactEmployees.ConnectedAddressName : String [R/W]
ContactEmployees.ConnectedAddressType : BoAddressType [R/W]
ContactEmployees.ContactEmployeeBlockSendingMarketingContents : ContactEmployeeBlockSendingMarketingContents [R]
ContactEmployees.Count : Long [R]
ContactEmployees.CreateDate : Date [R]
ContactEmployees.CreateTime : Date [R]
ContactEmployees.DateOfBirth : Date [R/W]
ContactEmployees.E_Mail : String [R/W]
ContactEmployees.EmailGroupCode : String [R/W]
ContactEmployees.Fax : String [R/W]
ContactEmployees.FirstName : String [R/W]
ContactEmployees.ForeignCountry : String [R/W]
ContactEmployees.Gender : BoGenderTypes [R/W]
ContactEmployees.InternalCode : Long [R]
ContactEmployees.LastName : String [R/W]
ContactEmployees.MiddleName : String [R/W]
ContactEmployees.MobilePhone : String [R/W]
ContactEmployees.Name : String [R/W]
ContactEmployees.Pager : String [R/W]
ContactEmployees.Password : String [R/W]
ContactEmployees.Phone1 : String [R/W]
ContactEmployees.Phone2 : String [R/W]
ContactEmployees.PlaceOfBirth : String [R/W]
ContactEmployees.Position : String [R/W]
ContactEmployees.Profession : String [R/W]
ContactEmployees.Remarks1 : String [R/W]
ContactEmployees.Remarks2 : String [R/W]
ContactEmployees.Title : String [R/W]
ContactEmployees.UpdateDate : Date [R]
ContactEmployees.UpdateTime : Date [R]
ContactEmployees.UserFields : UserFields [R]
ContactEmployees.Add()
ContactEmployees.Delete()
ContactEmployees.SetCurrentLine(ByVal LineNum As Long)
Contacts.Activity : BoActivities [R/W]
Contacts.ActivityType : Long [R/W]
Contacts.AttachmentEntry : Long [R/W]
Contacts.Attachments : Attachments [R]
Contacts.Browser : DataBrowser [R]
Contacts.CardCode : String [R/W]
Contacts.City : String [R/W]
Contacts.Closed : BoYesNoEnum [R/W]
Contacts.CloseDate : Date [R/W]
Contacts.ContactCode : Long [R]
Contacts.ContactDate : Date [R/W]
Contacts.ContactPersonCode : Long [R/W]
Contacts.ContactTime : Date [R/W]
Contacts.Country : String [R/W]
Contacts.Details : String [R/W]
Contacts.DocEntry : String [R/W]
Contacts.DocNum : String [R]
Contacts.DocType : Long [R/W]
Contacts.DocTypeEx : String [R/W]
Contacts.Duration : Double [R/W]
Contacts.DurationType : BoDurations [R/W]
Contacts.EndDuedate : Date [R/W]
Contacts.EndTime : Date [R/W]
Contacts.Fax : String [R/W]
Contacts.HandledBy : Long [R/W]
Contacts.Inactiveflag : BoYesNoEnum [R/W]
Contacts.Location : Long [R/W]
Contacts.Notes : String [R/W]
Contacts.ParentobjectId : Long [R]
Contacts.Parentobjecttype : String [R]
Contacts.Personalflag : BoYesNoEnum [R/W]
Contacts.Phone : String [R/W]
Contacts.PreviousActivity : Long [R/W]
Contacts.Priority : BoMsgPriorities [R/W]
Contacts.Recontact : Date [R/W]
Contacts.Reminder : BoYesNoEnum [R/W]
Contacts.ReminderPeriod : Double [R/W]
Contacts.ReminderType : BoDurations [R/W]
Contacts.Room : String [R/W]
Contacts.SalesEmployee : Long [R/W]
Contacts.StartDate : Date [R/W]
Contacts.StartTime : Date [R/W]
Contacts.State : String [R/W]
Contacts.Status : Long [R/W]
Contacts.Street : String [R/W]
Contacts.Subject : String [R/W]
Contacts.Tentativeflag : BoYesNoEnum [R/W]
Contacts.UserFields : UserFields [R]
Contacts.Add() -> Long
Contacts.GetAsXML() -> String
Contacts.GetByKey(ByVal ContactCode As Long) -> Boolean
Contacts.SaveToFile(ByVal FileName As String)
Contacts.SaveXML(ByRef FileName As String)
Contacts.Update() -> Long
ContractTemplates.AttachmentEntry : Long [R/W]
ContractTemplates.Attachments : Attachments [R]
ContractTemplates.Browser : DataBrowser [R]
ContractTemplates.ContractType : BoContractTypes [R/W]
ContractTemplates.Description : String [R/W]
ContractTemplates.DurationOfCoverage : Long [R/W]
ContractTemplates.FridayEnabled : BoYesNoEnum [R/W]
ContractTemplates.FridayEnd : Date [R/W]
ContractTemplates.FridayStart : Date [R/W]
ContractTemplates.IncludeHolidays : BoYesNoEnum [R/W]
ContractTemplates.IncludeLabor : BoYesNoEnum [R/W]
ContractTemplates.IncludeParts : BoYesNoEnum [R/W]
ContractTemplates.IncludeTravel : BoYesNoEnum [R/W]
ContractTemplates.MondayEnabled : BoYesNoEnum [R/W]
ContractTemplates.MondayEnd : Date [R/W]
ContractTemplates.MondayStart : Date [R/W]
ContractTemplates.Remarks : String [R/W]
ContractTemplates.RemindBeforeRenewal : Long [R/W]
ContractTemplates.RemindUnit : BoRemindUnits [R/W]
ContractTemplates.ResolutionTime : Long [R/W]
ContractTemplates.ResolutionUnit : BoResolutionUnits [R/W]
ContractTemplates.ResponseUnit : BoResponseUnit [R/W]
ContractTemplates.ResponseValue : Long [R/W]
ContractTemplates.SaturdayEnabled : BoYesNoEnum [R/W]
ContractTemplates.SaturdayEnd : Date [R/W]
ContractTemplates.SaturdayStart : Date [R/W]
ContractTemplates.SundayEnabled : BoYesNoEnum [R/W]
ContractTemplates.SundayEnd : Date [R/W]
ContractTemplates.SundayStart : Date [R/W]
ContractTemplates.TemplateIsDeleted : BoYesNoEnum [R/W]
ContractTemplates.TemplateIsRenewal : BoYesNoEnum [R/W]
ContractTemplates.TemplateName : String [R/W]
ContractTemplates.ThursdayEnabled : BoYesNoEnum [R/W]
ContractTemplates.ThursdayEnd : Date [R/W]
ContractTemplates.ThursdayStart : Date [R/W]
ContractTemplates.TuesdayEnabled : BoYesNoEnum [R/W]
ContractTemplates.TuesdayEnd : Date [R/W]
ContractTemplates.TuesdayStart : Date [R/W]
ContractTemplates.UserFields : UserFields [R]
ContractTemplates.WednesdayEnabled : BoYesNoEnum [R/W]
ContractTemplates.WednesdayEnd : Date [R/W]
ContractTemplates.WednesdayStart : Date [R/W]
ContractTemplates.Add() -> Long
ContractTemplates.Close() -> Long
ContractTemplates.GetAsXML() -> String
ContractTemplates.GetByKey(ByVal TemplateName As String) -> Boolean
ContractTemplates.Remove() -> Long
ContractTemplates.SaveToFile(ByVal FileName As String)
ContractTemplates.SaveXML(ByRef FileName As String)
ContractTemplates.Update() -> Long
CostCenterType.CostCenterTypeCode : String [R/W]
CostCenterType.CostCenterTypeName : String [R/W]
CostCenterType.UserFields : Fields [R]
CostCenterType.FromXMLFile(ByVal bstrFileName As String)
CostCenterType.FromXMLString(ByVal bstrXML As String)
CostCenterType.GetXMLSchema() -> String
CostCenterType.ToXMLFile(ByVal bstrFileName As String)
CostCenterType.ToXMLString() -> String
CostCenterTypeParams.CostCenterTypeCode : String [R/W]
CostCenterTypeParams.FromXMLFile(ByVal bstrFileName As String)
CostCenterTypeParams.FromXMLString(ByVal bstrXML As String)
CostCenterTypeParams.GetXMLSchema() -> String
CostCenterTypeParams.ToXMLFile(ByVal bstrFileName As String)
CostCenterTypeParams.ToXMLString() -> String
CostCenterTypes.Count : Long [R]
CostCenterTypes.Add() -> CostCenterType
CostCenterTypes.GetXMLSchema() -> String
CostCenterTypes.Item(ByVal vtIndex As Variant) -> CostCenterType
CostCenterTypes.ToXMLFile(ByVal bstrFileName As String)
CostCenterTypes.ToXMLString() -> String
CostCenterTypesParams.Count : Long [R]
CostCenterTypesParams.Add() -> CostCenterTypeParams
CostCenterTypesParams.GetXMLSchema() -> String
CostCenterTypesParams.Item(ByVal vtIndex As Variant) -> CostCenterTypeParams
CostCenterTypesParams.ToXMLFile(ByVal bstrFileName As String)
CostCenterTypesParams.ToXMLString() -> String
CostCenterTypesService.AddCostCenterType(ByVal pICostCenterType As CostCenterType) -> CostCenterTypeParams
CostCenterTypesService.DeleteCostCenterType(ByVal pICostCenterTypeParams As CostCenterTypeParams)
CostCenterTypesService.GetCostCenterType(ByVal pICostCenterTypeParams As CostCenterTypeParams) -> CostCenterType
CostCenterTypesService.GetCostCenterTypeList() -> CostCenterTypesParams
CostCenterTypesService.GetDataInterface(ByVal enumMSDI As CostCenterTypesServiceDataInterfaces) -> Object
CostCenterTypesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CostCenterTypesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CostCenterTypesService.UpdateCostCenterType(ByVal pICostCenterType As CostCenterType)
CostElement.Code : String [R/W]
CostElement.Description : String [R/W]
CostElement.IsActive : BoYesNoEnum [R/W]
CostElement.FromXMLFile(ByVal bstrFileName As String)
CostElement.FromXMLString(ByVal bstrXML As String)
CostElement.GetXMLSchema() -> String
CostElement.ToXMLFile(ByVal bstrFileName As String)
CostElement.ToXMLString() -> String
CostElementParams.Code : String [R/W]
CostElementParams.Description : String [R]
CostElementParams.FromXMLFile(ByVal bstrFileName As String)
CostElementParams.FromXMLString(ByVal bstrXML As String)
CostElementParams.GetXMLSchema() -> String
CostElementParams.ToXMLFile(ByVal bstrFileName As String)
CostElementParams.ToXMLString() -> String
CostElementService.AddCostElement(ByVal pICostElement As CostElement) -> CostElementParams
CostElementService.DeleteCostElement(ByVal pICostElementParams As CostElementParams)
CostElementService.GetCostElement(ByVal pICostElementParams As CostElementParams) -> CostElement
CostElementService.GetCostElementList() -> CostElementsParams
CostElementService.GetDataInterface(ByVal enumMSDI As CostElementServiceDataInterfaces) -> Object
CostElementService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CostElementService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CostElementService.UpdateCostElement(ByVal pICostElement As CostElement)
CostElementsParams.Count : Long [R]
CostElementsParams.Add() -> CostElementParams
CostElementsParams.GetXMLSchema() -> String
CostElementsParams.Item(ByVal vtIndex As Variant) -> CostElementParams
CostElementsParams.ToXMLFile(ByVal bstrFileName As String)
CostElementsParams.ToXMLString() -> String
CountriesParams.Count : Long [R]
CountriesParams.Add() -> CountryParams
CountriesParams.GetXMLSchema() -> String
CountriesParams.Item(ByVal vtIndex As Variant) -> CountryParams
CountriesParams.ToXMLFile(ByVal bstrFileName As String)
CountriesParams.ToXMLString() -> String
CountriesService.AddCountry(ByVal pICountry As Country) -> CountryParams
CountriesService.DeleteCountry(ByVal pICountryParams As CountryParams)
CountriesService.GetCountry(ByVal pICountryParams As CountryParams) -> Country
CountriesService.GetCountryList() -> CountriesParams
CountriesService.GetDataInterface(ByVal enumMSDI As CountriesServiceDataInterfaces) -> Object
CountriesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CountriesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CountriesService.UpdateCountry(ByVal pICountry As Country)
Country.AddressFormat : Long [R/W]
Country.BankAccountDigits : Long [R/W]
Country.BankBranchDigits : Long [R/W]
Country.BankCodeDigits : Long [R/W]
Country.BankControlKeyDigits : Long [R/W]
Country.Blacklisted : BoYesNoEnum [R/W]
Country.Code : String [R/W]
Country.CodeForReports : String [R/W]
Country.DomesticAccountValidation : DomesticBankAccountValidationEnum [R/W]
Country.EAEU : BoYesNoEnum [R/W]
Country.EU : BoYesNoEnum [R/W]
Country.IbanValidation : BoYesNoEnum [R/W]
Country.ISOAlpha2Code : String [R/W]
Country.ISOAlpha3Code : String [R/W]
Country.ISONumeric : String [R/W]
Country.Name : String [R/W]
Country.NumberOfDigitsForTaxID : Long [R/W]
Country.UICCountryCode : String [R/W]
Country.UserFields : Fields [R]
Country.FromXMLFile(ByVal bstrFileName As String)
Country.FromXMLString(ByVal bstrXML As String)
Country.GetXMLSchema() -> String
Country.ToXMLFile(ByVal bstrFileName As String)
Country.ToXMLString() -> String
CountryParams.Code : String [R/W]
CountryParams.Name : String [R]
CountryParams.FromXMLFile(ByVal bstrFileName As String)
CountryParams.FromXMLString(ByVal bstrXML As String)
CountryParams.GetXMLSchema() -> String
CountryParams.ToXMLFile(ByVal bstrFileName As String)
CountryParams.ToXMLString() -> String
CreditCardPayments.Browser : DataBrowser [R]
CreditCardPayments.DueDateCode : String [R/W]
CreditCardPayments.DueDateName : String [R/W]
CreditCardPayments.DueDatesType : DueDateTypesEnum [R/W]
CreditCardPayments.FromDay1 : Long [R/W]
CreditCardPayments.FromDay2 : Long [R/W]
CreditCardPayments.FromDay3 : Long [R/W]
CreditCardPayments.FromDay4 : Long [R/W]
CreditCardPayments.NoOfMonths1 : Long [R/W]
CreditCardPayments.NoOfMonths2 : Long [R/W]
CreditCardPayments.NoOfMonths3 : Long [R/W]
CreditCardPayments.NoOfMonths4 : Long [R/W]
CreditCardPayments.PaymentAfterDays : Long [R/W]
CreditCardPayments.PaymentAfterMonths : Long [R/W]
CreditCardPayments.PaymentDay1 : Long [R/W]
CreditCardPayments.PaymentDay2 : Long [R/W]
CreditCardPayments.PaymentDay3 : Long [R/W]
CreditCardPayments.PaymentDay4 : Long [R/W]
CreditCardPayments.ToDay1 : Long [R/W]
CreditCardPayments.ToDay2 : Long [R/W]
CreditCardPayments.ToDay3 : Long [R/W]
CreditCardPayments.ToDay4 : Long [R/W]
CreditCardPayments.UserFields : UserFields [R]
CreditCardPayments.Add() -> Long
CreditCardPayments.GetAsXML() -> String
CreditCardPayments.GetByKey(ByVal bstrCode As String) -> Boolean
CreditCardPayments.Remove() -> Long
CreditCardPayments.SaveToFile(ByVal bstrFileName As String)
CreditCardPayments.SaveXML(ByRef pbstrFileName As String)
CreditCardPayments.Update() -> Long
CreditCards.Browser : DataBrowser [R]
CreditCards.CompanyID : String [R/W]
CreditCards.CountryCode : String [R/W]
CreditCards.CreditCardCode : Long [R]
CreditCards.CreditCardName : String [R/W]
CreditCards.GLAccount : String [R/W]
CreditCards.Telephone : String [R/W]
CreditCards.UserFields : UserFields [R]
CreditCards.Add() -> Long
CreditCards.GetAsXML() -> String
CreditCards.GetByKey(ByVal lCardCode As Long) -> Boolean
CreditCards.SaveToFile(ByVal bstrFileName As String)
CreditCards.SaveXML(ByRef pbstrFileName As String)
CreditCards.Update() -> Long
CreditLine.AbsId : Long [R/W]
CreditLine.CreditCard : Long [R]
CreditLine.CreditCurrency : String [R]
CreditLine.Customer : String [R]
CreditLine.Deposited : BoYesNoEnum [R]
CreditLine.NumOfPayments : Long [R]
CreditLine.PayDate : Date [R]
CreditLine.PaymentMethodCode : Long [R]
CreditLine.Reference : String [R]
CreditLine.Total : Double [R]
CreditLine.Transferred : BoYesNoEnum [R]
CreditLine.VoucherNumber : String [R]
CreditLine.FromXMLFile(ByVal bstrFileName As String)
CreditLine.FromXMLString(ByVal bstrXML As String)
CreditLine.GetXMLSchema() -> String
CreditLine.ToXMLFile(ByVal bstrFileName As String)
CreditLine.ToXMLString() -> String
CreditLineParams.AbsId : Long [R/W]
CreditLineParams.FromXMLFile(ByVal bstrFileName As String)
CreditLineParams.FromXMLString(ByVal bstrXML As String)
CreditLineParams.GetXMLSchema() -> String
CreditLineParams.ToXMLFile(ByVal bstrFileName As String)
CreditLineParams.ToXMLString() -> String
CreditLines.Count : Long [R]
CreditLines.Add() -> CreditLine
CreditLines.GetXMLSchema() -> String
CreditLines.Item(ByVal vtIndex As Variant) -> CreditLine
CreditLines.ToXMLFile(ByVal bstrFileName As String)
CreditLines.ToXMLString() -> String
CreditLinesParams.Count : Long [R]
CreditLinesParams.Add() -> CreditLineParams
CreditLinesParams.GetXMLSchema() -> String
CreditLinesParams.Item(ByVal vtIndex As Variant) -> CreditLineParams
CreditLinesParams.ToXMLFile(ByVal bstrFileName As String)
CreditLinesParams.ToXMLString() -> String
CreditLinesService.GetCreditLine(ByVal pICreditLineParams As CreditLineParams) -> CreditLine
CreditLinesService.GetDataInterface(ByVal enumMSDI As CreditLinesServiceDataInterfaces) -> Object
CreditLinesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CreditLinesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CreditLinesService.GetValidCreditLineList() -> CreditLinesParams
CreditPaymentMethods.AssignedtoCreditCard : Long [R/W]
CreditPaymentMethods.Browser : DataBrowser [R]
CreditPaymentMethods.InstallmentPaymentsPossible : InstallmentPaymentsPossiblityEnum [R/W]
CreditPaymentMethods.MaxQtyWithoutApproval : Double [R/W]
CreditPaymentMethods.MinimumCreditAmount : Double [R/W]
CreditPaymentMethods.MinimumPaymentAmount : Double [R/W]
CreditPaymentMethods.Name : String [R/W]
CreditPaymentMethods.PaymentCode : String [R/W]
CreditPaymentMethods.PaymentMethodCode : Long [R]
CreditPaymentMethods.UserFields : UserFields [R]
CreditPaymentMethods.Add() -> Long
CreditPaymentMethods.GetAsXML() -> String
CreditPaymentMethods.GetByKey(ByVal lCode As Long) -> Boolean
CreditPaymentMethods.Remove() -> Long
CreditPaymentMethods.SaveToFile(ByVal bstrFileName As String)
CreditPaymentMethods.SaveXML(ByRef pbstrFileName As String)
CreditPaymentMethods.Update() -> Long
Currencies.Browser : DataBrowser [R]
Currencies.Code : String [R/W]
Currencies.Decimals : CurrenciesDecimalsEnum [R/W]
Currencies.DocumentsCode : String [R/W]
Currencies.EnglishHundredthName : String [R/W]
Currencies.EnglishName : String [R/W]
Currencies.HundredthName : String [R/W]
Currencies.InternationalDescription : String [R/W]
Currencies.MaxIncomingAmtDiff : Double [R/W]
Currencies.MaxIncomingAmtDiffPercent : Double [R/W]
Currencies.MaxOutgoingAmtDiff : Double [R/W]
Currencies.MaxOutgoingAmtDiffPercent : Double [R/W]
Currencies.Name : String [R/W]
Currencies.PluralEnglishHundredthName : String [R/W]
Currencies.PluralEnglishName : String [R/W]
Currencies.PluralHundredthName : String [R/W]
Currencies.PluralInternationalDescription : String [R/W]
Currencies.Rounding : RoundingSysEnum [R/W]
Currencies.RoundingInPayment : BoYesNoEnum [R/W]
Currencies.UserFields : UserFields [R]
Currencies.Add() -> Long
Currencies.GetAsXML() -> String
Currencies.GetByKey(ByVal Currency As String) -> Boolean
Currencies.Remove() -> Long
Currencies.SaveToFile(ByVal FileName As String)
Currencies.SaveXML(ByRef FileName As String)
Currencies.Update() -> Long
CurrencyRestrictions.Choose : BoYesNoEnum [R/W]
CurrencyRestrictions.Count : Long [R]
CurrencyRestrictions.CurrencyCode : String [R/W]
CurrencyRestrictions.CurrencyName : String [R]
CurrencyRestrictions.PaymentMethodCode : String [R]
CurrencyRestrictions.UserFields : UserFields [R]
CurrencyRestrictions.Add()
CurrencyRestrictions.SetCurrentLine(ByVal LineNum As Long)
CustomerEquipmentCards.AttachmentEntry : Long [R/W]
CustomerEquipmentCards.Attachments : Attachments [R]
CustomerEquipmentCards.Block : String [R/W]
CustomerEquipmentCards.Browser : DataBrowser [R]
CustomerEquipmentCards.BuildingFloorRoom : String [R/W]
CustomerEquipmentCards.BusinessPartners : CustomerEquipmentCards_BusinessPartners [R]
CustomerEquipmentCards.City : String [R/W]
CustomerEquipmentCards.ContactEmployeeCode : Long [R/W]
CustomerEquipmentCards.ContactPhone : String [R]
CustomerEquipmentCards.CountryCode : String [R/W]
CustomerEquipmentCards.County : String [R/W]
CustomerEquipmentCards.CustomerCode : String [R/W]
CustomerEquipmentCards.CustomerName : String [R/W]
CustomerEquipmentCards.DefaultTechnician : Long [R/W]
CustomerEquipmentCards.Defaultterritory : Long [R/W]
CustomerEquipmentCards.DeliveryCode : Long [R/W]
CustomerEquipmentCards.DeliveryDate : Date [R]
CustomerEquipmentCards.DeliveryNumber : Long [R]
CustomerEquipmentCards.DirectCustomerCode : String [R/W]
CustomerEquipmentCards.DirectCustomerName : String [R/W]
CustomerEquipmentCards.EquipmentCardNum : Long [R]
CustomerEquipmentCards.InstallLocation : String [R/W]
CustomerEquipmentCards.InternalSerialNum : String [R/W]
CustomerEquipmentCards.InvoiceCode : Long [R/W]
CustomerEquipmentCards.InvoiceNumber : Long [R]
CustomerEquipmentCards.ItemCode : String [R/W]
CustomerEquipmentCards.ItemDescription : String [R/W]
CustomerEquipmentCards.ManufacturerSerialNum : String [R/W]
CustomerEquipmentCards.ReplacedBySN : Long [R/W]
CustomerEquipmentCards.ReplaceSN : Long [R/W]
CustomerEquipmentCards.ServiceBPType : BoEquipmentBPType [R/W]
CustomerEquipmentCards.StateCode : String [R/W]
CustomerEquipmentCards.StatusOfSerialNumber : BoSerialNumberStatus [R/W]
CustomerEquipmentCards.Street : String [R/W]
CustomerEquipmentCards.StreetNo : String [R/W]
CustomerEquipmentCards.UserFields : UserFields [R]
CustomerEquipmentCards.ZipCode : String [R/W]
CustomerEquipmentCards.Add() -> Long
CustomerEquipmentCards.Close() -> Long
CustomerEquipmentCards.GetAsXML() -> String
CustomerEquipmentCards.GetByKey(ByVal EquipmentCardNum As Long) -> Boolean
CustomerEquipmentCards.Remove() -> Long
CustomerEquipmentCards.SaveToFile(ByVal FileName As String)
CustomerEquipmentCards.SaveXML(ByRef FileName As String)
CustomerEquipmentCards.Update() -> Long
CustomerEquipmentCards_BusinessPartners.BPCode : String [R/W]
CustomerEquipmentCards_BusinessPartners.Count : Long [R]
CustomerEquipmentCards_BusinessPartners.UserFields : UserFields [R]
CustomerEquipmentCards_BusinessPartners.Add()
CustomerEquipmentCards_BusinessPartners.Delete()
CustomerEquipmentCards_BusinessPartners.SetCurrentLine(ByVal LineNum As Long)
CustomsDeclaration.CCDNum : String [R/W]
CustomsDeclaration.CustomsBroker : String [R/W]
CustomsDeclaration.CustomsTerminal : String [R/W]
CustomsDeclaration.Date : Date [R/W]
CustomsDeclaration.DocDate : Date [R/W]
CustomsDeclaration.DocNum : String [R/W]
CustomsDeclaration.PaymentKey : String [R/W]
CustomsDeclaration.SupplyDate : Date [R/W]
CustomsDeclaration.SupplyNum : String [R/W]
CustomsDeclaration.UserFields : Fields [R]
CustomsDeclaration.FromXMLFile(ByVal bstrFileName As String)
CustomsDeclaration.FromXMLString(ByVal bstrXML As String)
CustomsDeclaration.GetXMLSchema() -> String
CustomsDeclaration.ToXMLFile(ByVal bstrFileName As String)
CustomsDeclaration.ToXMLString() -> String
CustomsDeclarationParams.CCDNum : String [R/W]
CustomsDeclarationParams.FromXMLFile(ByVal bstrFileName As String)
CustomsDeclarationParams.FromXMLString(ByVal bstrXML As String)
CustomsDeclarationParams.GetXMLSchema() -> String
CustomsDeclarationParams.ToXMLFile(ByVal bstrFileName As String)
CustomsDeclarationParams.ToXMLString() -> String
CustomsDeclarationService.AddCustomsDeclaration(ByVal pICustomsDeclaration As CustomsDeclaration) -> CustomsDeclarationParams
CustomsDeclarationService.DeleteCustomsDeclaration(ByVal pICustomsDeclarationParams As CustomsDeclarationParams)
CustomsDeclarationService.GetCustomsDeclaration(ByVal pICustomsDeclarationParams As CustomsDeclarationParams) -> CustomsDeclaration
CustomsDeclarationService.GetDataInterface(ByVal enumMSDI As CustomsDeclarationServiceDataInterfaces) -> Object
CustomsDeclarationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CustomsDeclarationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CustomsDeclarationService.UpdateCustomsDeclaration(ByVal pICustomsDeclaration As CustomsDeclaration)
CustomsGroups.Browser : DataBrowser [R]
CustomsGroups.Code : Long [R]
CustomsGroups.Customs : Double [R/W]
CustomsGroups.CustomsAllocationAccount : String [R/W]
CustomsGroups.CustomsExpenseAccount : String [R/W]
CustomsGroups.Locked : BoYesNoEnum [R]
CustomsGroups.Name : String [R/W]
CustomsGroups.Number : String [R/W]
CustomsGroups.Other : Double [R/W]
CustomsGroups.PortAddress : String [R/W]
CustomsGroups.PortState : String [R/W]
CustomsGroups.Purchase : Double [R/W]
CustomsGroups.Total : Double [R/W]
CustomsGroups.UserFields : UserFields [R]
CustomsGroups.Add() -> Long
CustomsGroups.GetAsXML() -> String
CustomsGroups.GetByKey(ByVal lGroupCode As Long) -> Boolean
CustomsGroups.Remove() -> Long
CustomsGroups.SaveToFile(ByVal bstrFileName As String)
CustomsGroups.SaveXML(ByRef pbstrFileName As String)
CustomsGroups.Update() -> Long
CycleCountDetermination.CycleBy : CycleCountDeterminationCycleByEnum [R/W]
CycleCountDetermination.CycleCountDeterminationSetupCollection : CycleCountDeterminationSetupCollection [R]
CycleCountDetermination.WarehouseCode : String [R/W]
CycleCountDetermination.FromXMLFile(ByVal bstrFileName As String)
CycleCountDetermination.FromXMLString(ByVal bstrXML As String)
CycleCountDetermination.GetXMLSchema() -> String
CycleCountDetermination.ToXMLFile(ByVal bstrFileName As String)
CycleCountDetermination.ToXMLString() -> String
CycleCountDeterminationParams.CycleBy : Long [R]
CycleCountDeterminationParams.WarehouseCode : String [R/W]
CycleCountDeterminationParams.FromXMLFile(ByVal bstrFileName As String)
CycleCountDeterminationParams.FromXMLString(ByVal bstrXML As String)
CycleCountDeterminationParams.GetXMLSchema() -> String
CycleCountDeterminationParams.ToXMLFile(ByVal bstrFileName As String)
CycleCountDeterminationParams.ToXMLString() -> String
CycleCountDeterminationParamsCollection.Count : Long [R]
CycleCountDeterminationParamsCollection.Add() -> CycleCountDeterminationParams
CycleCountDeterminationParamsCollection.GetXMLSchema() -> String
CycleCountDeterminationParamsCollection.Item(ByVal vtIndex As Variant) -> CycleCountDeterminationParams
CycleCountDeterminationParamsCollection.ToXMLFile(ByVal bstrFileName As String)
CycleCountDeterminationParamsCollection.ToXMLString() -> String
CycleCountDeterminationSetup.Alert : BoYesNoEnum [R/W]
CycleCountDeterminationSetup.ChangeExistingItems : BoYesNoEnum [R/W]
CycleCountDeterminationSetup.CycleCode : Long [R/W]
CycleCountDeterminationSetup.DestinationUser : Long [R/W]
CycleCountDeterminationSetup.Entry : Long [R/W]
CycleCountDeterminationSetup.ExcludeItemsWithZeroQuantity : BoYesNoEnum [R/W]
CycleCountDeterminationSetup.NextCountingDate : Date [R]
CycleCountDeterminationSetup.Time : Date [R]
CycleCountDeterminationSetup.WarehouseCode : String [R/W]
CycleCountDeterminationSetup.FromXMLFile(ByVal bstrFileName As String)
CycleCountDeterminationSetup.FromXMLString(ByVal bstrXML As String)
CycleCountDeterminationSetup.GetXMLSchema() -> String
CycleCountDeterminationSetup.ToXMLFile(ByVal bstrFileName As String)
CycleCountDeterminationSetup.ToXMLString() -> String
CycleCountDeterminationSetupCollection.Count : Long [R]
CycleCountDeterminationSetupCollection.Add() -> CycleCountDeterminationSetup
CycleCountDeterminationSetupCollection.GetXMLSchema() -> String
CycleCountDeterminationSetupCollection.Item(ByVal vtIndex As Variant) -> CycleCountDeterminationSetup
CycleCountDeterminationSetupCollection.ToXMLFile(ByVal bstrFileName As String)
CycleCountDeterminationSetupCollection.ToXMLString() -> String
CycleCountDeterminationsService.Get(ByVal pICycleCountDeterminationParams As CycleCountDeterminationParams) -> CycleCountDetermination
CycleCountDeterminationsService.GetDataInterface(ByVal enumMSDI As CycleCountDeterminationsServiceDataInterfaces) -> Object
CycleCountDeterminationsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
CycleCountDeterminationsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
CycleCountDeterminationsService.GetList() -> CycleCountDeterminationParamsCollection
CycleCountDeterminationsService.Update(ByVal pICycleCountDetermination As CycleCountDetermination)
DashboardPackageImportParams.ForceOverwritePackage : BoYesNoEnum [R/W]
DashboardPackageImportParams.ForceOverwriteQuery : BoYesNoEnum [R/W]
DashboardPackageImportParams.ImportQueries : BoYesNoEnum [R/W]
DashboardPackageImportParams.PackageFilePath : String [R/W]
DashboardPackageImportParams.FromXMLFile(ByVal bstrFileName As String)
DashboardPackageImportParams.FromXMLString(ByVal bstrXML As String)
DashboardPackageImportParams.GetXMLSchema() -> String
DashboardPackageImportParams.ToXMLFile(ByVal bstrFileName As String)
DashboardPackageImportParams.ToXMLString() -> String
DashboardPackageParams.AbsEntry : Long [R/W]
DashboardPackageParams.FromXMLFile(ByVal bstrFileName As String)
DashboardPackageParams.FromXMLString(ByVal bstrXML As String)
DashboardPackageParams.GetXMLSchema() -> String
DashboardPackageParams.ToXMLFile(ByVal bstrFileName As String)
DashboardPackageParams.ToXMLString() -> String
DashboardPackagesParams.Count : Long [R]
DashboardPackagesParams.Add() -> DashboardPackageParams
DashboardPackagesParams.GetXMLSchema() -> String
DashboardPackagesParams.Item(ByVal vtIndex As Variant) -> DashboardPackageParams
DashboardPackagesParams.ToXMLFile(ByVal bstrFileName As String)
DashboardPackagesParams.ToXMLString() -> String
DashboardPackagesService.GetDataInterface(ByVal enumMSDI As DashboardPackagesServiceDataInterfaces) -> Object
DashboardPackagesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DashboardPackagesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DashboardPackagesService.ImportDashboardPackage(ByVal pIDashboardPackageImportParams As DashboardPackageImportParams) -> DashboardPackageParams
DataBrowser.BoF : Boolean [R]
DataBrowser.EoF : Boolean [R]
DataBrowser.RecordCount : Long [R]
DataBrowser.Recordset : Recordset [W]
DataBrowser.GetByKeys(ByVal keysStr As String) -> Boolean
DataBrowser.MoveFirst()
DataBrowser.MoveLast()
DataBrowser.MoveNext()
DataBrowser.MovePrevious()
DataBrowser.ReadXml(ByVal XmlFileStr As String, ByVal Index As Long)
DataBrowser.Refresh()
DataSensitiveStatus.DataSensitiveStatus : DataSensitiveStatusEnum [R]
DataSensitiveStatus.FromXMLFile(ByVal bstrFileName As String)
DataSensitiveStatus.FromXMLString(ByVal bstrXML As String)
DataSensitiveStatus.GetXMLSchema() -> String
DataSensitiveStatus.ToXMLFile(ByVal bstrFileName As String)
DataSensitiveStatus.ToXMLString() -> String
DecimalData.Context : RoundingContextEnum [R/W]
DecimalData.Currency : String [R/W]
DecimalData.Value : Double [R/W]
DecimalData.FromXMLFile(ByVal bstrFileName As String)
DecimalData.FromXMLString(ByVal bstrXML As String)
DecimalData.GetXMLSchema() -> String
DecimalData.ToXMLFile(ByVal bstrFileName As String)
DecimalData.ToXMLString() -> String
DeductionTaxGroups.Browser : DataBrowser [R]
DeductionTaxGroups.GroupCode : BoDeductionTaxGroupCodeEnum [R/W]
DeductionTaxGroups.GroupExtendedCode : String [R/W]
DeductionTaxGroups.GroupKey : Long [R]
DeductionTaxGroups.GroupName : String [R/W]
DeductionTaxGroups.MaxRedin : Double [R/W]
DeductionTaxGroups.UserFields : UserFields [R]
DeductionTaxGroups.Add() -> Long
DeductionTaxGroups.GetAsXML() -> String
DeductionTaxGroups.GetByKey(ByVal lGroupKey As Long) -> Boolean
DeductionTaxGroups.SaveToFile(ByVal bstrFileName As String)
DeductionTaxGroups.SaveXML(ByRef pbstrFileName As String)
DeductionTaxGroups.Update() -> Long
DeductionTaxHierarchies.AbsEntry : Long [R]
DeductionTaxHierarchies.BPCode : String [R/W]
DeductionTaxHierarchies.Browser : DataBrowser [R]
DeductionTaxHierarchies.DeductionPercent : Double [R/W]
DeductionTaxHierarchies.HierarchyCode : String [R/W]
DeductionTaxHierarchies.HierarchyName : String [R/W]
DeductionTaxHierarchies.LastUpdated : Date [R]
DeductionTaxHierarchies.Lines : DeductionTaxHierarchies_Lines [R]
DeductionTaxHierarchies.MaximumTotal : Double [R/W]
DeductionTaxHierarchies.UserFields : UserFields [R]
DeductionTaxHierarchies.ValidFrom : Date [R/W]
DeductionTaxHierarchies.ValidUntil : Date [R/W]
DeductionTaxHierarchies.Add() -> Long
DeductionTaxHierarchies.GetAsXML() -> String
DeductionTaxHierarchies.GetByKey(ByVal lAbsEntry As Long) -> Boolean
DeductionTaxHierarchies.SaveToFile(ByVal bstrFileName As String)
DeductionTaxHierarchies.SaveXML(ByRef pbstrFileName As String)
DeductionTaxHierarchies.Update() -> Long
DeductionTaxHierarchies_Lines.Count : Long [R]
DeductionTaxHierarchies_Lines.DeductionPercent : Long [R/W]
DeductionTaxHierarchies_Lines.MaximumTotal : Double [R/W]
DeductionTaxHierarchies_Lines.RowNumber : Long [R]
DeductionTaxHierarchies_Lines.UserFields : UserFields [R]
DeductionTaxHierarchies_Lines.Add()
DeductionTaxHierarchies_Lines.SetCurrentLine(ByVal LineNum As Long)
DeductionTaxSubGroup.GroupCode : String [R/W]
DeductionTaxSubGroup.GroupName : String [R/W]
DeductionTaxSubGroup.FromXMLFile(ByVal bstrFileName As String)
DeductionTaxSubGroup.FromXMLString(ByVal bstrXML As String)
DeductionTaxSubGroup.GetXMLSchema() -> String
DeductionTaxSubGroup.ToXMLFile(ByVal bstrFileName As String)
DeductionTaxSubGroup.ToXMLString() -> String
DeductionTaxSubGroupParams.GroupCode : String [R/W]
DeductionTaxSubGroupParams.GroupName : String [R]
DeductionTaxSubGroupParams.FromXMLFile(ByVal bstrFileName As String)
DeductionTaxSubGroupParams.FromXMLString(ByVal bstrXML As String)
DeductionTaxSubGroupParams.GetXMLSchema() -> String
DeductionTaxSubGroupParams.ToXMLFile(ByVal bstrFileName As String)
DeductionTaxSubGroupParams.ToXMLString() -> String
DeductionTaxSubGroupsParams.Count : Long [R]
DeductionTaxSubGroupsParams.Add() -> DeductionTaxSubGroupParams
DeductionTaxSubGroupsParams.GetXMLSchema() -> String
DeductionTaxSubGroupsParams.Item(ByVal vtIndex As Variant) -> DeductionTaxSubGroupParams
DeductionTaxSubGroupsParams.ToXMLFile(ByVal bstrFileName As String)
DeductionTaxSubGroupsParams.ToXMLString() -> String
DeductionTaxSubGroupsService.AddDeductionTaxSubGroup(ByVal pIDeductionTaxSubGroup As DeductionTaxSubGroup) -> DeductionTaxSubGroupParams
DeductionTaxSubGroupsService.GetDataInterface(ByVal enumMSDI As DeductionTaxSubGroupsServiceDataInterfaces) -> Object
DeductionTaxSubGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DeductionTaxSubGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DeductionTaxSubGroupsService.GetDeductionTaxSubGroup(ByVal pIDeductionTaxSubGroupParams As DeductionTaxSubGroupParams) -> DeductionTaxSubGroup
DeductionTaxSubGroupsService.GetDeductionTaxSubGroupList() -> DeductionTaxSubGroupsParams
DeductionTaxSubGroupsService.UpdateDeductionTaxSubGroup(ByVal pIDeductionTaxSubGroup As DeductionTaxSubGroup)
DefaultCreditCards.Code : String [R]
DefaultCreditCards.Count : Long [R]
DefaultCreditCards.CreditAccountCode : String [R/W]
DefaultCreditCards.CreditCardCode : Long [R/W]
DefaultCreditCards.UserFields : UserFields [R]
DefaultCreditCards.Add()
DefaultCreditCards.SetCurrentLine(ByVal LineNum As Long)
DefaultDocuments.AddExport : BoYesNoEnum [R/W]
DefaultDocuments.AddPrint : BoYesNoEnum [R/W]
DefaultDocuments.Code : String [R]
DefaultDocuments.Count : Long [R]
DefaultDocuments.EnglishKeyboardEnteringBPC : BoYesNoEnum [R/W]
DefaultDocuments.EnglishKeyboardEnteringItem : BoYesNoEnum [R/W]
DefaultDocuments.NoofCopies : Long [R/W]
DefaultDocuments.NoofCopiesforManualDoc : Long [R/W]
DefaultDocuments.ObjectType : String [R/W]
DefaultDocuments.PermanentRemark : String [R/W]
DefaultDocuments.PrintDiscountData : BoYesNoEnum [R/W]
DefaultDocuments.PrintTotals : BoYesNoEnum [R/W]
DefaultDocuments.PrintVendorCatalogNo : BoYesNoEnum [R/W]
DefaultDocuments.TotalsRounding : BoYesNoEnum [R/W]
DefaultDocuments.UserFields : UserFields [R]
DefaultDocuments.Add()
DefaultDocuments.SetCurrentLine(ByVal LineNum As Long)
DefaultElectronicSeriesParams.ElectronicSeries : Long [R/W]
DefaultElectronicSeriesParams.Series : Long [R/W]
DefaultElectronicSeriesParams.FromXMLFile(ByVal bstrFileName As String)
DefaultElectronicSeriesParams.FromXMLString(ByVal bstrXML As String)
DefaultElectronicSeriesParams.GetXMLSchema() -> String
DefaultElectronicSeriesParams.ToXMLFile(ByVal bstrFileName As String)
DefaultElectronicSeriesParams.ToXMLString() -> String
DefaultElementsforCR.Code : Long [R]
DefaultElementsforCR.Name : String [R/W]
DefaultElementsforCR.FromXMLFile(ByVal bstrFileName As String)
DefaultElementsforCR.FromXMLString(ByVal bstrXML As String)
DefaultElementsforCR.GetXMLSchema() -> String
DefaultElementsforCR.ToXMLFile(ByVal bstrFileName As String)
DefaultElementsforCR.ToXMLString() -> String
DefaultElementsforCRParams.Code : Long [R/W]
DefaultElementsforCRParams.Name : String [R]
DefaultElementsforCRParams.FromXMLFile(ByVal bstrFileName As String)
DefaultElementsforCRParams.FromXMLString(ByVal bstrXML As String)
DefaultElementsforCRParams.GetXMLSchema() -> String
DefaultElementsforCRParams.ToXMLFile(ByVal bstrFileName As String)
DefaultElementsforCRParams.ToXMLString() -> String
DefaultElementsforCRService.Add(ByVal pIDefaultElementsforCR As DefaultElementsforCR) -> DefaultElementsforCRParams
DefaultElementsforCRService.Get(ByVal pIDefaultElementsforCRParams As DefaultElementsforCRParams) -> DefaultElementsforCR
DefaultElementsforCRService.GetDataInterface(ByVal enumMSDI As DefaultElementsforCRServiceDataInterfaces) -> Object
DefaultElementsforCRService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DefaultElementsforCRService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DefaultPTICodes.Count : Long [R]
DefaultPTICodes.DefaultPTICode : String [R/W]
DefaultPTICodes.DocObjectCode : BoObjectTypes [R/W]
DefaultPTICodes.DocumentSubType : BoDocumentSubType [R/W]
DefaultPTICodes.Add()
DefaultPTICodes.SetCurrentLine(ByVal LineNum As Long)
DefaultReportParams.CardCode : String [R/W]
DefaultReportParams.LayoutCode : String [R/W]
DefaultReportParams.ReportCode : String [R/W]
DefaultReportParams.UserID : Long [R/W]
DefaultReportParams.FromXMLFile(ByVal bstrFileName As String)
DefaultReportParams.FromXMLString(ByVal bstrXML As String)
DefaultReportParams.GetXMLSchema() -> String
DefaultReportParams.ToXMLFile(ByVal bstrFileName As String)
DefaultReportParams.ToXMLString() -> String
Department.Code : Long [R]
Department.Description : String [R/W]
Department.Name : String [R/W]
Department.FromXMLFile(ByVal bstrFileName As String)
Department.FromXMLString(ByVal bstrXML As String)
Department.GetXMLSchema() -> String
Department.ToXMLFile(ByVal bstrFileName As String)
Department.ToXMLString() -> String
DepartmentParams.Code : Long [R/W]
DepartmentParams.Name : String [R]
DepartmentParams.FromXMLFile(ByVal bstrFileName As String)
DepartmentParams.FromXMLString(ByVal bstrXML As String)
DepartmentParams.GetXMLSchema() -> String
DepartmentParams.ToXMLFile(ByVal bstrFileName As String)
DepartmentParams.ToXMLString() -> String
DepartmentsParams.Count : Long [R]
DepartmentsParams.Add() -> DepartmentParams
DepartmentsParams.GetXMLSchema() -> String
DepartmentsParams.Item(ByVal vtIndex As Variant) -> DepartmentParams
DepartmentsParams.ToXMLFile(ByVal bstrFileName As String)
DepartmentsParams.ToXMLString() -> String
DepartmentsService.AddDepartment(ByVal pIDepartment As Department) -> DepartmentParams
DepartmentsService.DeleteDepartment(ByVal pIDepartmentParams As DepartmentParams)
DepartmentsService.GetDataInterface(ByVal enumMSDI As DepartmentsServiceDataInterfaces) -> Object
DepartmentsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DepartmentsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DepartmentsService.GetDepartment(ByVal pIDepartmentParams As DepartmentParams) -> Department
DepartmentsService.GetDepartmentList() -> DepartmentsParams
DepartmentsService.UpdateDepartment(ByVal pIDepartment As Department)
Deposit.AbsEntry : Long [R]
Deposit.AllocationAccount : String [R/W]
Deposit.AttachmentEntry : Long [R/W]
Deposit.Bank : String [R/W]
Deposit.BankAccountNum : String [R/W]
Deposit.BankBranch : String [R/W]
Deposit.BankReference : String [R/W]
Deposit.BOEs : BOELines [R]
Deposit.BPLID : Long [R/W]
Deposit.CheckDepositType : BoCheckDepositTypeEnum [R/W]
Deposit.Checks : CheckLines [R]
Deposit.Commission : Double [R/W]
Deposit.CommissionAccount : String [R/W]
Deposit.CommissionCurrency : String [R/W]
Deposit.CommissionDate : Date [R/W]
Deposit.CommissionFC : Double [R]
Deposit.CommissionSC : Double [R]
Deposit.Credits : CreditLines [R]
Deposit.DepositAccount : String [R/W]
Deposit.DepositAccountType : BoDepositAccountTypeEnum [R/W]
Deposit.DepositCurrency : String [R/W]
Deposit.DepositDate : Date [R/W]
Deposit.DepositNumber : Long [R]
Deposit.DepositorName : String [R/W]
Deposit.DepositType : BoDepositTypeEnum [R/W]
Deposit.DistributionRule : String [R/W]
Deposit.DistributionRule2 : String [R/W]
Deposit.DistributionRule3 : String [R/W]
Deposit.DistributionRule4 : String [R/W]
Deposit.DistributionRule5 : String [R/W]
Deposit.DocRate : Double [R/W]
Deposit.IncomeTaxAccount : String [R/W]
Deposit.IncomeTaxAmount : Double [R/W]
Deposit.IncomeTaxAmountFC : Double [R]
Deposit.IncomeTaxAmountSC : Double [R]
Deposit.JournalRemarks : String [R/W]
Deposit.Project : String [R/W]
Deposit.ReconcileAfterDeposit : BoYesNoEnum [R/W]
Deposit.Series : Long [R/W]
Deposit.TaxAccount : String [R/W]
Deposit.TaxAmount : Double [R/W]
Deposit.TaxAmountFC : Double [R]
Deposit.TaxAmountSC : Double [R]
Deposit.TaxCode : String [R/W]
Deposit.TotalFC : Double [R]
Deposit.TotalLC : Double [R/W]
Deposit.TotalSC : Double [R]
Deposit.UserFields : Fields [R]
Deposit.VoucherAccount : String [R/W]
Deposit.FromXMLFile(ByVal bstrFileName As String)
Deposit.FromXMLString(ByVal bstrXML As String)
Deposit.GetXMLSchema() -> String
Deposit.ToXMLFile(ByVal bstrFileName As String)
Deposit.ToXMLString() -> String
DepositParams.AbsEntry : Long [R/W]
DepositParams.DepositNumber : Long [R/W]
DepositParams.Series : Long [R/W]
DepositParams.FromXMLFile(ByVal bstrFileName As String)
DepositParams.FromXMLString(ByVal bstrXML As String)
DepositParams.GetXMLSchema() -> String
DepositParams.ToXMLFile(ByVal bstrFileName As String)
DepositParams.ToXMLString() -> String
DepositsParams.Count : Long [R]
DepositsParams.Add() -> DepositParams
DepositsParams.GetXMLSchema() -> String
DepositsParams.Item(ByVal vtIndex As Variant) -> DepositParams
DepositsParams.ToXMLFile(ByVal bstrFileName As String)
DepositsParams.ToXMLString() -> String
DepositsService.AddDeposit(ByVal pIDeposit As Deposit) -> DepositParams
DepositsService.CancelCheckRow(ByVal pICancelCheckRowParams As CancelCheckRowParams)
DepositsService.CancelCheckRowbyCurrentSystemDate(ByVal pICancelCheckRowParams As CancelCheckRowParams)
DepositsService.CancelDeposit(ByVal pIDepositParams As DepositParams)
DepositsService.CancelDepositbyCurrentSystemDate(ByVal pIDepositParams As DepositParams)
DepositsService.GetDataInterface(ByVal enumMSDI As DepositsServiceDataInterfaces) -> Object
DepositsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DepositsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DepositsService.GetDeposit(ByVal pIDepositParams As DepositParams) -> Deposit
DepositsService.GetDepositList() -> DepositsParams
DepositsService.UpdateDeposit(ByVal pIDeposit As Deposit)
DepreciationArea.AreaType : AreaTypeEnum [R/W]
DepreciationArea.BPForTaxCorrection : String [R/W]
DepreciationArea.Code : String [R/W]
DepreciationArea.DerivedArea : String [R/W]
DepreciationArea.Description : String [R/W]
DepreciationArea.DirectRevenuePosting : BoYesNoEnum [R/W]
DepreciationArea.ItemForTaxCorrection : String [R/W]
DepreciationArea.MainBookingArea : BoYesNoEnum [R/W]
DepreciationArea.PostingOfDepreciation : PostingOfDepreciationEnum [R/W]
DepreciationArea.RetirementMethod : RetirementMethodEnum [R/W]
DepreciationArea.TaxCreditControl : BoYesNoEnum [R/W]
DepreciationArea.TaxType : Long [R/W]
DepreciationArea.UsageForTaxCorrection : Long [R/W]
DepreciationArea.FromXMLFile(ByVal bstrFileName As String)
DepreciationArea.FromXMLString(ByVal bstrXML As String)
DepreciationArea.GetXMLSchema() -> String
DepreciationArea.ToXMLFile(ByVal bstrFileName As String)
DepreciationArea.ToXMLString() -> String
DepreciationAreaParams.Code : String [R/W]
DepreciationAreaParams.Description : String [R]
DepreciationAreaParams.FromXMLFile(ByVal bstrFileName As String)
DepreciationAreaParams.FromXMLString(ByVal bstrXML As String)
DepreciationAreaParams.GetXMLSchema() -> String
DepreciationAreaParams.ToXMLFile(ByVal bstrFileName As String)
DepreciationAreaParams.ToXMLString() -> String
DepreciationAreaParamsCollection.Count : Long [R]
DepreciationAreaParamsCollection.Add() -> DepreciationAreaParams
DepreciationAreaParamsCollection.GetXMLSchema() -> String
DepreciationAreaParamsCollection.Item(ByVal vtIndex As Variant) -> DepreciationAreaParams
DepreciationAreaParamsCollection.ToXMLFile(ByVal bstrFileName As String)
DepreciationAreaParamsCollection.ToXMLString() -> String
DepreciationAreasService.Add(ByVal pIDepreciationArea As DepreciationArea) -> DepreciationAreaParams
DepreciationAreasService.Delete(ByVal pIDepreciationAreaParams As DepreciationAreaParams)
DepreciationAreasService.Get(ByVal pIDepreciationAreaParams As DepreciationAreaParams) -> DepreciationArea
DepreciationAreasService.GetDataInterface(ByVal enumMSDI As DepreciationAreasServiceDataInterfaces) -> Object
DepreciationAreasService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DepreciationAreasService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DepreciationAreasService.GetList() -> DepreciationAreaParamsCollection
DepreciationAreasService.Update(ByVal pIDepreciationArea As DepreciationArea)
DepreciationLevel.amount : Double [R/W]
DepreciationLevel.DepreciationCalculationBase : DepreciationCalculationBaseEnum [R/W]
DepreciationLevel.Level : Long [R]
DepreciationLevel.NumberOfYears : Long [R/W]
DepreciationLevel.Percentage : Double [R/W]
DepreciationLevel.FromXMLFile(ByVal bstrFileName As String)
DepreciationLevel.FromXMLString(ByVal bstrXML As String)
DepreciationLevel.GetXMLSchema() -> String
DepreciationLevel.ToXMLFile(ByVal bstrFileName As String)
DepreciationLevel.ToXMLString() -> String
DepreciationLevelCollection.Count : Long [R]
DepreciationLevelCollection.Add() -> DepreciationLevel
DepreciationLevelCollection.GetXMLSchema() -> String
DepreciationLevelCollection.Item(ByVal vtIndex As Variant) -> DepreciationLevel
DepreciationLevelCollection.ToXMLFile(ByVal bstrFileName As String)
DepreciationLevelCollection.ToXMLString() -> String
DepreciationType.AcquisitionPeriodControl : AcquisitionPeriodControlEnum [R/W]
DepreciationType.AcquisitionProRataType : AcquisitionProRataTypeEnum [R/W]
DepreciationType.CalculationBase : CalculationBaseEnum [R/W]
DepreciationType.Code : String [R/W]
DepreciationType.DecliningChangeTo : String [R/W]
DepreciationType.DecliningFactor : Double [R/W]
DepreciationType.DecliningPercentage : Double [R/W]
DepreciationType.DeltaCoefficient : Long [R]
DepreciationType.DepreciationEndAtLastFullYear : BoYesNoEnum [R/W]
DepreciationType.DepreciationLevelCollection : DepreciationLevelCollection [R]
DepreciationType.DepreciationMethod : DepreciationMethodEnum [R/W]
DepreciationType.DepreciationTypePool : String [R/W]
DepreciationType.Description : String [R/W]
DepreciationType.FactorOnlyRelevantToFirstFiscalYear : BoYesNoEnum [R/W]
DepreciationType.IncludePreviousDepreciationInCapitalizationPeriod : BoYesNoEnum [R/W]
DepreciationType.IncludeSalvageInDepreciation : BoYesNoEnum [R/W]
DepreciationType.ManualDepreciationReduceDepreciationBase : BoYesNoEnum [R/W]
DepreciationType.MaximumDepreciableValue : Double [R/W]
DepreciationType.MinimumDepreciatedValue : Double [R/W]
DepreciationType.PercentageOfDepreciationReversedInRetirementYear : Double [R/W]
DepreciationType.RetirementPeriodControl : RetirementPeriodControlEnum [R/W]
DepreciationType.RetirementProRataType : RetirementProRataTypeEnum [R/W]
DepreciationType.RoundingMethod : DepreciationRoundingMethodEnum [R/W]
DepreciationType.RoundYearEndBookValue : BoYesNoEnum [R/W]
DepreciationType.SalvagePercentage : Double [R/W]
DepreciationType.SpecialDepreciationAlternativeDepreciation : String [R/W]
DepreciationType.SpecialDepreciationCalculationMethod : SpecialDepreciationCalculationMethodEnum [R]
DepreciationType.SpecialDepreciationConcessionPeriodYears : Long [R/W]
DepreciationType.SpecialDepreciationMaximumAmount : Double [R/W]
DepreciationType.SpecialDepreciationMaximumFlag : SpecialDepreciationMaximumFlagEnum [R/W]
DepreciationType.SpecialDepreciationMaximumPercentage : Double [R/W]
DepreciationType.SpecialDepreciationNormalDepreciation : String [R/W]
DepreciationType.StraightLineCalculationMethod : StraightLineCalculationMethodEnum [R/W]
DepreciationType.StraightLinePercentage : Double [R/W]
DepreciationType.StraightLinePeriodControlDepreciationPeriods : StraightLinePeriodControlDepreciationPeriodsEnum [R/W]
DepreciationType.StraightLinePeriodControlFactor : Double [R/W]
DepreciationType.SubsequentAcquisitionPeriodControl : SubsequentAcquisitionPeriodControlEnum [R/W]
DepreciationType.SubsequentAcquisitionProRataType : SubsequentAcquisitionProRataTypeEnum [R/W]
DepreciationType.TransferSourcePeriodControl : TransferSourcePeriodControlEnum [R/W]
DepreciationType.TransferSourceProRataType : TransferSourceProRataTypeEnum [R/W]
DepreciationType.TransferTargetPeriodControl : TransferTargetPeriodControlEnum [R/W]
DepreciationType.TransferTargetProRataType : TransferTargetProRataTypeEnum [R/W]
DepreciationType.ValidFrom : Date [R/W]
DepreciationType.ValidTo : Date [R/W]
DepreciationType.FromXMLFile(ByVal bstrFileName As String)
DepreciationType.FromXMLString(ByVal bstrXML As String)
DepreciationType.GetXMLSchema() -> String
DepreciationType.ToXMLFile(ByVal bstrFileName As String)
DepreciationType.ToXMLString() -> String
DepreciationTypeParams.Code : String [R/W]
DepreciationTypeParams.Description : String [R]
DepreciationTypeParams.FromXMLFile(ByVal bstrFileName As String)
DepreciationTypeParams.FromXMLString(ByVal bstrXML As String)
DepreciationTypeParams.GetXMLSchema() -> String
DepreciationTypeParams.ToXMLFile(ByVal bstrFileName As String)
DepreciationTypeParams.ToXMLString() -> String
DepreciationTypeParamsCollection.Count : Long [R]
DepreciationTypeParamsCollection.Add() -> DepreciationTypeParams
DepreciationTypeParamsCollection.GetXMLSchema() -> String
DepreciationTypeParamsCollection.Item(ByVal vtIndex As Variant) -> DepreciationTypeParams
DepreciationTypeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
DepreciationTypeParamsCollection.ToXMLString() -> String
DepreciationTypePool.Code : String [R/W]
DepreciationTypePool.Description : String [R/W]
DepreciationTypePool.FromXMLFile(ByVal bstrFileName As String)
DepreciationTypePool.FromXMLString(ByVal bstrXML As String)
DepreciationTypePool.GetXMLSchema() -> String
DepreciationTypePool.ToXMLFile(ByVal bstrFileName As String)
DepreciationTypePool.ToXMLString() -> String
DepreciationTypePoolParams.Code : String [R/W]
DepreciationTypePoolParams.Description : String [R]
DepreciationTypePoolParams.FromXMLFile(ByVal bstrFileName As String)
DepreciationTypePoolParams.FromXMLString(ByVal bstrXML As String)
DepreciationTypePoolParams.GetXMLSchema() -> String
DepreciationTypePoolParams.ToXMLFile(ByVal bstrFileName As String)
DepreciationTypePoolParams.ToXMLString() -> String
DepreciationTypePoolParamsCollection.Count : Long [R]
DepreciationTypePoolParamsCollection.Add() -> DepreciationTypePoolParams
DepreciationTypePoolParamsCollection.GetXMLSchema() -> String
DepreciationTypePoolParamsCollection.Item(ByVal vtIndex As Variant) -> DepreciationTypePoolParams
DepreciationTypePoolParamsCollection.ToXMLFile(ByVal bstrFileName As String)
DepreciationTypePoolParamsCollection.ToXMLString() -> String
DepreciationTypePoolsService.Add(ByVal pIDepreciationTypePool As DepreciationTypePool) -> DepreciationTypePoolParams
DepreciationTypePoolsService.Delete(ByVal pIDepreciationTypePoolParams As DepreciationTypePoolParams)
DepreciationTypePoolsService.Get(ByVal pIDepreciationTypePoolParams As DepreciationTypePoolParams) -> DepreciationTypePool
DepreciationTypePoolsService.GetDataInterface(ByVal enumMSDI As DepreciationTypePoolsServiceDataInterfaces) -> Object
DepreciationTypePoolsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DepreciationTypePoolsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DepreciationTypePoolsService.GetList() -> DepreciationTypePoolParamsCollection
DepreciationTypePoolsService.Update(ByVal pIDepreciationTypePool As DepreciationTypePool)
DepreciationTypesService.Add(ByVal pIDepreciationType As DepreciationType) -> DepreciationTypeParams
DepreciationTypesService.Delete(ByVal pIDepreciationTypeParams As DepreciationTypeParams)
DepreciationTypesService.Get(ByVal pIDepreciationTypeParams As DepreciationTypeParams) -> DepreciationType
DepreciationTypesService.GetDataInterface(ByVal enumMSDI As DepreciationTypesServiceDataInterfaces) -> Object
DepreciationTypesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DepreciationTypesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DepreciationTypesService.GetList() -> DepreciationTypeParamsCollection
DepreciationTypesService.Update(ByVal pIDepreciationType As DepreciationType)
DeterminationCriteria.DeterminationCriteria : String [R]
DeterminationCriteria.DmcId : Long [R]
DeterminationCriteria.IsActive : BoYesNoEnum [R/W]
DeterminationCriteria.Priority : Long [R/W]
DeterminationCriteria.FromXMLFile(ByVal bstrFileName As String)
DeterminationCriteria.FromXMLString(ByVal bstrXML As String)
DeterminationCriteria.GetXMLSchema() -> String
DeterminationCriteria.ToXMLFile(ByVal bstrFileName As String)
DeterminationCriteria.ToXMLString() -> String
DeterminationCriteriaParams.DmcId : Long [R/W]
DeterminationCriteriaParams.FromXMLFile(ByVal bstrFileName As String)
DeterminationCriteriaParams.FromXMLString(ByVal bstrXML As String)
DeterminationCriteriaParams.GetXMLSchema() -> String
DeterminationCriteriaParams.ToXMLFile(ByVal bstrFileName As String)
DeterminationCriteriaParams.ToXMLString() -> String
DeterminationCriteriaParamsCollection.Count : Long [R]
DeterminationCriteriaParamsCollection.Add() -> DeterminationCriteriaParams
DeterminationCriteriaParamsCollection.GetXMLSchema() -> String
DeterminationCriteriaParamsCollection.Item(ByVal vtIndex As Variant) -> DeterminationCriteriaParams
DeterminationCriteriaParamsCollection.ToXMLFile(ByVal bstrFileName As String)
DeterminationCriteriaParamsCollection.ToXMLString() -> String
DeterminationCriteriasService.Get(ByVal pIDeterminationCriteriaParams As DeterminationCriteriaParams) -> DeterminationCriteria
DeterminationCriteriasService.GetDataInterface(ByVal enumMSDI As DeterminationCriteriasServiceDataInterfaces) -> Object
DeterminationCriteriasService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DeterminationCriteriasService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DeterminationCriteriasService.GetList() -> DeterminationCriteriaParamsCollection
DeterminationCriteriasService.Update(ByVal pIDeterminationCriteria As DeterminationCriteria)
Dimension.DimensionCode : Long [R]
Dimension.DimensionDescription : String [R/W]
Dimension.DimensionName : String [R]
Dimension.IsActive : BoYesNoEnum [R/W]
Dimension.UserFields : Fields [R]
Dimension.FromXMLFile(ByVal bstrFileName As String)
Dimension.FromXMLString(ByVal bstrXML As String)
Dimension.GetXMLSchema() -> String
Dimension.ToXMLFile(ByVal bstrFileName As String)
Dimension.ToXMLString() -> String
DimensionParams.DimensionCode : Long [R/W]
DimensionParams.DimensionName : String [R]
DimensionParams.FromXMLFile(ByVal bstrFileName As String)
DimensionParams.FromXMLString(ByVal bstrXML As String)
DimensionParams.GetXMLSchema() -> String
DimensionParams.ToXMLFile(ByVal bstrFileName As String)
DimensionParams.ToXMLString() -> String
DimensionsParams.Count : Long [R]
DimensionsParams.Add() -> DimensionParams
DimensionsParams.GetXMLSchema() -> String
DimensionsParams.Item(ByVal vtIndex As Variant) -> DimensionParams
DimensionsParams.ToXMLFile(ByVal bstrFileName As String)
DimensionsParams.ToXMLString() -> String
DimensionsService.GetDataInterface(ByVal enumMSDI As DimensionsServiceDataInterfaces) -> Object
DimensionsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DimensionsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DimensionsService.GetDimension(ByVal pIDimensionParams As DimensionParams) -> Dimension
DimensionsService.GetDimensionList() -> DimensionsParams
DimensionsService.UpdateDimension(ByVal pIDimension As Dimension)
DiscountGroupLine.AbsEntry : Long [R]
DiscountGroupLine.Discount : Double [R/W]
DiscountGroupLine.DiscountType : DiscountGroupDiscountTypeEnum [R]
DiscountGroupLine.FreeQuantity : Double [R/W]
DiscountGroupLine.MaximumFreeQuantity : Double [R/W]
DiscountGroupLine.ObjectCode : String [R/W]
DiscountGroupLine.ObjectType : DiscountGroupBaseObjectEnum [R/W]
DiscountGroupLine.PaidQuantity : Double [R/W]
DiscountGroupLine.FromXMLFile(ByVal bstrFileName As String)
DiscountGroupLine.FromXMLString(ByVal bstrXML As String)
DiscountGroupLine.GetXMLSchema() -> String
DiscountGroupLine.ToXMLFile(ByVal bstrFileName As String)
DiscountGroupLine.ToXMLString() -> String
DiscountGroupLineCollection.Count : Long [R]
DiscountGroupLineCollection.Add() -> DiscountGroupLine
DiscountGroupLineCollection.GetXMLSchema() -> String
DiscountGroupLineCollection.Item(ByVal vtIndex As Variant) -> DiscountGroupLine
DiscountGroupLineCollection.Remove(ByVal vtIndex As Variant)
DiscountGroupLineCollection.ToXMLFile(ByVal bstrFileName As String)
DiscountGroupLineCollection.ToXMLString() -> String
DiscountGroups.BaseObjectType : DiscountGroupBaseObjectEnum [R]
DiscountGroups.BPCode : String [R]
DiscountGroups.Count : Long [R]
DiscountGroups.DiscountPercentage : Double [R/W]
DiscountGroups.ObjectEntry : String [R/W]
DiscountGroups.Add()
DiscountGroups.Delete()
DiscountGroups.SetCurrentLine(ByVal LineNum As Long)
DiscountLine.Day : Long [R/W]
DiscountLine.Discount : Double [R/W]
DiscountLine.DiscountCode : String [R]
DiscountLine.LineId : Long [R]
DiscountLine.Month : Long [R/W]
DiscountLine.NumOfDays : Long [R/W]
DiscountLine.FromXMLFile(ByVal bstrFileName As String)
DiscountLine.FromXMLString(ByVal bstrXML As String)
DiscountLine.GetXMLSchema() -> String
DiscountLine.ToXMLFile(ByVal bstrFileName As String)
DiscountLine.ToXMLString() -> String
DiscountLines.Count : Long [R]
DiscountLines.Add() -> DiscountLine
DiscountLines.GetXMLSchema() -> String
DiscountLines.Item(ByVal vtIndex As Variant) -> DiscountLine
DiscountLines.Remove(ByVal vtIndex As Variant)
DiscountLines.ToXMLFile(ByVal bstrFileName As String)
DiscountLines.ToXMLString() -> String
DistributionRule.Active : BoYesNoEnum [R/W]
DistributionRule.Direct : String [R/W]
DistributionRule.DistributionRuleLines : DistributionRuleLines [R]
DistributionRule.FactorCode : String [R/W]
DistributionRule.FactorDescription : String [R/W]
DistributionRule.InWhichDimension : Long [R/W]
DistributionRule.IsFixedAmount : BoYesNoEnum [R/W]
DistributionRule.TotalFactor : Double [R/W]
DistributionRule.UserFields : Fields [R]
DistributionRule.FromXMLFile(ByVal bstrFileName As String)
DistributionRule.FromXMLString(ByVal bstrXML As String)
DistributionRule.GetXMLSchema() -> String
DistributionRule.ToXMLFile(ByVal bstrFileName As String)
DistributionRule.ToXMLString() -> String
DistributionRuleLine.CenterCode : String [R/W]
DistributionRuleLine.Effectivefrom : Date [R/W]
DistributionRuleLine.EffectiveTo : Date [R/W]
DistributionRuleLine.TotalInCenter : Double [R/W]
DistributionRuleLine.FromXMLFile(ByVal bstrFileName As String)
DistributionRuleLine.FromXMLString(ByVal bstrXML As String)
DistributionRuleLine.GetXMLSchema() -> String
DistributionRuleLine.ToXMLFile(ByVal bstrFileName As String)
DistributionRuleLine.ToXMLString() -> String
DistributionRuleLines.Count : Long [R]
DistributionRuleLines.Add() -> DistributionRuleLine
DistributionRuleLines.GetXMLSchema() -> String
DistributionRuleLines.Item(ByVal vtIndex As Variant) -> DistributionRuleLine
DistributionRuleLines.ToXMLFile(ByVal bstrFileName As String)
DistributionRuleLines.ToXMLString() -> String
DistributionRuleParams.FactorCode : String [R/W]
DistributionRuleParams.FactorDescription : String [R]
DistributionRuleParams.FromXMLFile(ByVal bstrFileName As String)
DistributionRuleParams.FromXMLString(ByVal bstrXML As String)
DistributionRuleParams.GetXMLSchema() -> String
DistributionRuleParams.ToXMLFile(ByVal bstrFileName As String)
DistributionRuleParams.ToXMLString() -> String
DistributionRulesParams.Count : Long [R]
DistributionRulesParams.Add() -> DistributionRuleParams
DistributionRulesParams.GetXMLSchema() -> String
DistributionRulesParams.Item(ByVal vtIndex As Variant) -> DistributionRuleParams
DistributionRulesParams.ToXMLFile(ByVal bstrFileName As String)
DistributionRulesParams.ToXMLString() -> String
DistributionRulesService.AddDistributionRule(ByVal pIDistributionRule As DistributionRule) -> DistributionRuleParams
DistributionRulesService.DeleteDistributionRule(ByVal pIDistributionRuleParams As DistributionRuleParams)
DistributionRulesService.GetDataInterface(ByVal enumMSDI As DistributionRulesServiceDataInterfaces) -> Object
DistributionRulesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DistributionRulesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DistributionRulesService.GetDistributionRule(ByVal pIDistributionRuleParams As DistributionRuleParams) -> DistributionRule
DistributionRulesService.GetDistributionRuleList() -> DistributionRulesParams
DistributionRulesService.UpdateDistributionRule(ByVal pIDistributionRule As DistributionRule)
DNFCodeSetup.AbsEntry : Long [R]
DNFCodeSetup.DNFCode : String [R/W]
DNFCodeSetup.Factor : Double [R/W]
DNFCodeSetup.NCMCode : Long [R/W]
DNFCodeSetup.UoM : String [R/W]
DNFCodeSetup.FromXMLFile(ByVal bstrFileName As String)
DNFCodeSetup.FromXMLString(ByVal bstrXML As String)
DNFCodeSetup.GetXMLSchema() -> String
DNFCodeSetup.ToXMLFile(ByVal bstrFileName As String)
DNFCodeSetup.ToXMLString() -> String
DNFCodeSetupParams.AbsEntry : Long [R/W]
DNFCodeSetupParams.DNFCode : String [R]
DNFCodeSetupParams.NCMCode : Long [R]
DNFCodeSetupParams.FromXMLFile(ByVal bstrFileName As String)
DNFCodeSetupParams.FromXMLString(ByVal bstrXML As String)
DNFCodeSetupParams.GetXMLSchema() -> String
DNFCodeSetupParams.ToXMLFile(ByVal bstrFileName As String)
DNFCodeSetupParams.ToXMLString() -> String
DNFCodeSetupParamsCollection.Count : Long [R]
DNFCodeSetupParamsCollection.Add() -> DNFCodeSetupParams
DNFCodeSetupParamsCollection.GetXMLSchema() -> String
DNFCodeSetupParamsCollection.Item(ByVal vtIndex As Variant) -> DNFCodeSetupParams
DNFCodeSetupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
DNFCodeSetupParamsCollection.ToXMLString() -> String
DNFCodeSetupService.AddDNFCodeSetup(ByVal pIDNFCodeSetup As DNFCodeSetup) -> DNFCodeSetupParams
DNFCodeSetupService.DeleteDNFCodeSetup(ByVal pIDNFCodeSetupParams As DNFCodeSetupParams)
DNFCodeSetupService.GetDataInterface(ByVal enumMSDI As DNFCodeSetupServiceDataInterfaces) -> Object
DNFCodeSetupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DNFCodeSetupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DNFCodeSetupService.GetDNFCodeSetup(ByVal pIDNFCodeSetupParams As DNFCodeSetupParams) -> DNFCodeSetup
DNFCodeSetupService.GetDNFCodeSetupList() -> DNFCodeSetupParamsCollection
DNFCodeSetupService.UpdateDNFCodeSetup(ByVal pIDNFCodeSetup As DNFCodeSetup)
DocsInWTGroups.AccumulatedAmount : Double [R]
DocsInWTGroups.BaseAmount : Double [R]
DocsInWTGroups.Count : Long [R]
DocsInWTGroups.DocEntry : Long [R]
DocsInWTGroups.DocObjType : String [R]
DocsInWTGroups.DocTotal : Double [R]
DocsInWTGroups.Percent : Double [R]
DocsInWTGroups.PerceptAmount : Double [R]
DocsInWTGroups.VatAmount : Double [R]
DocsInWTGroups.SetCurrentLine(ByVal LineNum As Long)
Document_ApprovalRequests.ActiveForUpdate : BoYesNoEnum [R]
Document_ApprovalRequests.ApprovalTemplatesID : Long [R]
Document_ApprovalRequests.ApprovalTemplatesName : String [R]
Document_ApprovalRequests.Count : Long [R]
Document_ApprovalRequests.Remarks : String [R/W]
Document_ApprovalRequests.SetCurrentLine(ByVal LineNum As Long)
Document_DocumentReferences.AccessKey : String [R/W]
Document_DocumentReferences.DocEntry : Long [R]
Document_DocumentReferences.ExternalReferencedDocNumber : String [R/W]
Document_DocumentReferences.FiscalDocumentModel : String [R/W]
Document_DocumentReferences.FiscalDocumentNumber : Long [R/W]
Document_DocumentReferences.FiscalDocumentSeries : String [R/W]
Document_DocumentReferences.FiscalDocumentSubseries : String [R/W]
Document_DocumentReferences.IssueDate : Date [R/W]
Document_DocumentReferences.IssuerCNPJ : String [R/W]
Document_DocumentReferences.IssuerCode : String [R/W]
Document_DocumentReferences.LineNumber : Long [R]
Document_DocumentReferences.LinkReferenceType : LinkReferenceTypeEnum [R/W]
Document_DocumentReferences.ReferencedAccessKey : String [R/W]
Document_DocumentReferences.ReferencedAmount : Double [R/W]
Document_DocumentReferences.ReferencedDocEntry : Long [R/W]
Document_DocumentReferences.ReferencedDocNumber : Long [R]
Document_DocumentReferences.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
Document_DocumentReferences.Remark : String [R/W]
Document_DocumentReferences.Add()
Document_DocumentReferences.Delete()
Document_DocumentReferences.SetCurrentLine(ByVal LineNum As Long)
Document_EWayBillDetails.BillFromGSTIN : String [R/W]
Document_EWayBillDetails.BillFromName : String [R/W]
Document_EWayBillDetails.BillFromStateGSTCode : String [R/W]
Document_EWayBillDetails.BillToGSTIN : String [R/W]
Document_EWayBillDetails.BillToName : String [R/W]
Document_EWayBillDetails.BillToStateGSTCode : String [R/W]
Document_EWayBillDetails.DispatchFromAddress1 : String [R/W]
Document_EWayBillDetails.DispatchFromAddress2 : String [R/W]
Document_EWayBillDetails.DispatchFromPlace : String [R/W]
Document_EWayBillDetails.DispatchFromStateGSTCode : String [R/W]
Document_EWayBillDetails.DispatchFromZipCode : String [R/W]
Document_EWayBillDetails.Distance : Double [R/W]
Document_EWayBillDetails.DocEntry : Long [R]
Document_EWayBillDetails.DocumentType : String [R/W]
Document_EWayBillDetails.EWayBillDate : Date [R/W]
Document_EWayBillDetails.EWayBillExpirationDate : Date [R/W]
Document_EWayBillDetails.EWayBillNo : String [R/W]
Document_EWayBillDetails.MainHSNEntry : Long [R/W]
Document_EWayBillDetails.ShipToAddress1 : String [R/W]
Document_EWayBillDetails.ShipToAddress2 : String [R/W]
Document_EWayBillDetails.ShipToPlace : String [R/W]
Document_EWayBillDetails.ShipToStateGSTCode : String [R/W]
Document_EWayBillDetails.ShipToZipCode : String [R/W]
Document_EWayBillDetails.SubType : Long [R/W]
Document_EWayBillDetails.SupplyType : EWBSupplyTypeEnum [R/W]
Document_EWayBillDetails.TransactionType : EWBTransactionTypeEnum [R/W]
Document_EWayBillDetails.TransportationMode : Long [R/W]
Document_EWayBillDetails.TransporterDocDate : Date [R/W]
Document_EWayBillDetails.TransporterDocNo : String [R/W]
Document_EWayBillDetails.TransporterEntry : Long [R/W]
Document_EWayBillDetails.TransporterID : String [R/W]
Document_EWayBillDetails.TransporterLineNumber : Long [R/W]
Document_EWayBillDetails.TransporterName : String [R/W]
Document_EWayBillDetails.VehicleNo : String [R/W]
Document_EWayBillDetails.VehicleType : String [R/W]
Document_Installments.Count : Long [R]
Document_Installments.DueDate : Date [R/W]
Document_Installments.DunningLevel : Long [R/W]
Document_Installments.InstallmentId : Long [R]
Document_Installments.LastDunningDate : Date [R]
Document_Installments.PaymentOrdered : BoYesNoEnum [R]
Document_Installments.Percentage : Double [R/W]
Document_Installments.Total : Double [R/W]
Document_Installments.TotalFC : Double [R/W]
Document_Installments.UserFields : UserFields [R]
Document_Installments.Add()
Document_Installments.Delete()
Document_Installments.SetCurrentLine(ByVal LineNum As Long)
Document_Lines.AccountCode : String [R/W]
Document_Lines.ActualBaseEntry : Long [R/W]
Document_Lines.ActualBaseLine : Long [R/W]
Document_Lines.ActualDeliveryDate : Date [R/W]
Document_Lines.Address : String [R/W]
Document_Lines.AgreementNo : Long [R/W]
Document_Lines.AgreementRowNumber : Long [R/W]
Document_Lines.AppliedTax : Double [R]
Document_Lines.AppliedTaxFC : Double [R]
Document_Lines.AppliedTaxSC : Double [R]
Document_Lines.BackOrder : BoYesNoEnum [R/W]
Document_Lines.BarCode : String [R/W]
Document_Lines.BaseEntry : Long [R/W]
Document_Lines.BaseLine : Long [R/W]
Document_Lines.BaseOpenQuantity : Double [R]
Document_Lines.BaseType : Long [R/W]
Document_Lines.BatchNumbers : BatchNumbers [R]
Document_Lines.BinAllocations : DocumentLinesBinAllocations [R]
Document_Lines.CCDNumbers : CCDNumbers [R]
Document_Lines.CESTCode : Long [R/W]
Document_Lines.CFOPCode : String [R/W]
Document_Lines.ChangeAssemlyBoMWarehouse : String [R/W]
Document_Lines.ChangeInventoryQuantityIndependently : BoYesNoEnum [R/W]
Document_Lines.CNJPOfManufacturer : String [R/W]
Document_Lines.COGSAccountCode : String [R/W]
Document_Lines.COGSCostingCode : String [R/W]
Document_Lines.COGSCostingCode2 : String [R/W]
Document_Lines.COGSCostingCode3 : String [R/W]
Document_Lines.COGSCostingCode4 : String [R/W]
Document_Lines.COGSCostingCode5 : String [R/W]
Document_Lines.CommisionPercent : Double [R/W]
Document_Lines.CommodityClassification : Long [R/W]
Document_Lines.ConsiderQuantity : BoYesNoEnum [R/W]
Document_Lines.ConsumerSalesForecast : BoYesNoEnum [R/W]
Document_Lines.CorrectionInvoiceItem : BoCorInvItemStatus [R/W]
Document_Lines.CorrInvAmountToDiffAcct : Double [R/W]
Document_Lines.CorrInvAmountToStock : Double [R/W]
Document_Lines.CostingCode : String [R/W]
Document_Lines.CostingCode2 : String [R/W]
Document_Lines.CostingCode3 : String [R/W]
Document_Lines.CostingCode4 : String [R/W]
Document_Lines.CostingCode5 : String [R/W]
Document_Lines.Count : Long [R]
Document_Lines.CountryOrg : String [R/W]
Document_Lines.CreditOriginCode : String [R/W]
Document_Lines.CSTCode : String [R/W]
Document_Lines.CSTforCOFINS : String [R/W]
Document_Lines.CSTforIPI : String [R/W]
Document_Lines.CSTforPIS : String [R/W]
Document_Lines.CtrSealQty : Double [R/W]
Document_Lines.Currency : String [R/W]
Document_Lines.CUSplit : BoYesNoEnum [R/W]
Document_Lines.DefectAndBreakup : Double [R/W]
Document_Lines.DeferredTax : BoYesNoEnum [R/W]
Document_Lines.DestinationCountryForImport : String [R/W]
Document_Lines.DestinationRegionForImport : Long [R/W]
Document_Lines.DiscountPercent : Double [R/W]
Document_Lines.DistributeExpense : BoYesNoEnum [R/W]
Document_Lines.DocEntry : Long [R]
Document_Lines.EBooksDetails : EBooks_Doc_Details [R]
Document_Lines.EnableReturnCost : BoYesNoEnum [R/W]
Document_Lines.EqualizationTaxPercent : Double [R]
Document_Lines.ExciseAmount : Double [R/W]
Document_Lines.ExLineNo : String [R/W]
Document_Lines.ExpenseOperationType : BoExpenseOperationTypeEnum [R/W]
Document_Lines.Expenses : Document_LinesAdditionalExpenses [R]
Document_Lines.ExpenseType : String [R/W]
Document_Lines.ExportProcesses : ExportProcesses [R]
Document_Lines.ExternalCalcTaxAmount : Double [R/W]
Document_Lines.ExternalCalcTaxAmountFC : Double [R]
Document_Lines.ExternalCalcTaxAmountSC : Double [R]
Document_Lines.ExternalCalcTaxRate : Double [R/W]
Document_Lines.Factor1 : Double [R/W]
Document_Lines.Factor2 : Double [R/W]
Document_Lines.Factor3 : Double [R/W]
Document_Lines.Factor4 : Double [R/W]
Document_Lines.FederalTaxID : String [R/W]
Document_Lines.FreeOfChargeBP : BoYesNoEnum [R/W]
Document_Lines.FreeText : String [R/W]
Document_Lines.GeneratedAssets : GeneratedAssets [R]
Document_Lines.GrossBase : Long [R/W]
Document_Lines.GrossBuyPrice : Double [R/W]
Document_Lines.GrossPrice : Double [R/W]
Document_Lines.GrossProfit : Double [R]
Document_Lines.GrossProfitFC : Double [R]
Document_Lines.GrossProfitSC : Double [R]
Document_Lines.GrossProfitTotalBasePrice : Double [R/W]
Document_Lines.GrossTotal : Double [R/W]
Document_Lines.GrossTotalFC : Double [R/W]
Document_Lines.GrossTotalSC : Double [R]
Document_Lines.Height1 : Double [R/W]
Document_Lines.Height2 : Double [R/W]
Document_Lines.Height2Unit : Long [R/W]
Document_Lines.Hight1Unit : Long [R/W]
Document_Lines.HSNEntry : Long [R/W]
Document_Lines.ImportProcesses : ImportProcesses [R]
Document_Lines.Incoterms : Long [R/W]
Document_Lines.IndicatorForRelevantScale : BoYesNoEnum [R/W]
Document_Lines.InventoryQuantity : Double [R/W]
Document_Lines.ItemCode : String [R/W]
Document_Lines.ItemDescription : String [R/W]
Document_Lines.ItemDetails : String [R/W]
Document_Lines.ItemType : BoDocItemType [R]
Document_Lines.LastBuyDistributeSum : Double [R]
Document_Lines.LastBuyDistributeSumFc : Double [R]
Document_Lines.LastBuyDistributeSumSc : Double [R]
Document_Lines.LastBuyInmPrice : Double [R]
Document_Lines.Lengh1 : Double [R/W]
Document_Lines.Lengh1Unit : Long [R/W]
Document_Lines.Lengh2 : Double [R/W]
Document_Lines.Lengh2Unit : Long [R/W]
Document_Lines.LineNum : Long [R]
Document_Lines.LineStatus : BoStatus [R/W]
Document_Lines.LineTotal : Double [R/W]
Document_Lines.LineType : BoDocLineType [R/W]
Document_Lines.LineVendor : String [R/W]
Document_Lines.ListNum : Long [R]
Document_Lines.LocationCode : Long [R/W]
Document_Lines.MeasureUnit : String [R/W]
Document_Lines.NatureOfTransaction : Long [R/W]
Document_Lines.NCMCode : Long [R/W]
Document_Lines.NetTaxAmount : Double [R/W]
Document_Lines.NetTaxAmountFC : Double [R/W]
Document_Lines.NetTaxAmountSC : Double [R]
Document_Lines.NVECode : String [R/W]
Document_Lines.OpenAmount : Double [R]
Document_Lines.OpenAmountFC : Double [R]
Document_Lines.OpenAmountSC : Double [R]
Document_Lines.OriginalItem : String [R]
Document_Lines.OriginCountryForExport : String [R/W]
Document_Lines.OriginRegionForExport : Long [R/W]
Document_Lines.OwnerCode : Long [R/W]
Document_Lines.PackageQuantity : Double [R/W]
Document_Lines.ParentLineNum : Long [R/W]
Document_Lines.PartialRetirement : BoYesNoEnum [R/W]
Document_Lines.PickListIdNumber : Long [R]
Document_Lines.PickQuantity : Double [R]
Document_Lines.PickStatus : BoYesNoEnum [R]
Document_Lines.PickStatusEx : BoDocumentLinePickStatus [R]
Document_Lines.PoItemNum : Long [R/W]
Document_Lines.PoNum : String [R/W]
Document_Lines.POTargetEntry : String [R]
Document_Lines.POTargetNum : Long [R]
Document_Lines.POTargetRowNum : String [R]
Document_Lines.Price : Double [R/W]
Document_Lines.PriceAfterVAT : Double [R/W]
Document_Lines.ProjectCode : String [R/W]
Document_Lines.Quantity : Double [R/W]
Document_Lines.Rate : Double [R/W]
Document_Lines.ReceiptNumber : String [R/W]
Document_Lines.RemainingOpenInventoryQuantity : Double [R]
Document_Lines.RemainingOpenQuantity : Double [R]
Document_Lines.RequiredDate : Date [R/W]
Document_Lines.RequiredQuantity : Double [R/W]
Document_Lines.RetirementAPC : Double [R/W]
Document_Lines.RetirementQuantity : Double [R/W]
Document_Lines.ReturnAction : Long [R/W]
Document_Lines.ReturnCost : Double [R/W]
Document_Lines.ReturnReason : Long [R/W]
Document_Lines.ReverseCharge : BoYesNoEnum [R/W]
Document_Lines.RowTotalFC : Double [R/W]
Document_Lines.RowTotalSC : Double [R]
Document_Lines.SACEntry : Long [R/W]
Document_Lines.SalesPersonCode : Long [R/W]
Document_Lines.SerialNum : String [R/W]
Document_Lines.SerialNumbers : SerialNumbers [R]
Document_Lines.ShipDate : Date [R/W]
Document_Lines.ShipFromCode : String [R/W]
Document_Lines.ShipFromDescription : String [R/W]
Document_Lines.ShippingMethod : Long [R/W]
Document_Lines.ShipToCode : String [R/W]
Document_Lines.ShipToDescription : String [R/W]
Document_Lines.Shortages : Double [R/W]
Document_Lines.StandardItemIdentification : Long [R/W]
Document_Lines.StgDesc : String [R]
Document_Lines.StgEntry : Long [R]
Document_Lines.StgSeqNum : Long [R]
Document_Lines.StockDistributesum : Double [R]
Document_Lines.StockDistributesumForeign : Double [R]
Document_Lines.StockDistributesumSystem : Double [R]
Document_Lines.StockInmPrice : Double [R]
Document_Lines.SupplierCatNum : String [R/W]
Document_Lines.Surpluses : Double [R/W]
Document_Lines.SWW : String [R/W]
Document_Lines.TaxBeforeDPM : Double [R]
Document_Lines.TaxBeforeDPMFC : Double [R]
Document_Lines.TaxBeforeDPMSC : Double [R]
Document_Lines.TaxCode : String [R/W]
Document_Lines.TaxJurisdictions : TaxJurisdictions [R]
Document_Lines.TaxLiable : BoYesNoEnum [R/W]
Document_Lines.TaxOnly : BoYesNoEnum [R/W]
Document_Lines.TaxPercentagePerRow : Double [R/W]
Document_Lines.TaxPerUnit : Double [R]
Document_Lines.TaxTotal : Double [R/W]
Document_Lines.TaxType : BoTaxTypes [R/W]
Document_Lines.Text : String [R]
Document_Lines.ThirdParty : BoYesNoEnum [R/W]
Document_Lines.TotalEqualizationTax : Double [R]
Document_Lines.TotalEqualizationTaxFC : Double [R]
Document_Lines.TotalEqualizationTaxSC : Double [R]
Document_Lines.TotalInclTax : Double [R]
Document_Lines.TransactionType : BoTransactionTypeEnum [R/W]
Document_Lines.TransportMode : Long [R/W]
Document_Lines.TreeType : BoItemTreeTypes [R]
Document_Lines.UFFiscalBenefitCode : String [R/W]
Document_Lines.UnencumberedReason : Long [R/W]
Document_Lines.UnitPrice : Double [R/W]
Document_Lines.UnitsOfMeasurment : Double [R/W]
Document_Lines.UoMCode : String [R]
Document_Lines.UoMEntry : Long [R/W]
Document_Lines.Usage : String [R/W]
Document_Lines.UseBaseUnits : BoYesNoEnum [R/W]
Document_Lines.UserFields : UserFields [R]
Document_Lines.VatGroup : String [R/W]
Document_Lines.VendorNum : String [R/W]
Document_Lines.VisualOrder : Long [R]
Document_Lines.Volume : Double [R/W]
Document_Lines.VolumeUnit : Long [R/W]
Document_Lines.WarehouseCode : String [R/W]
Document_Lines.Weight1 : Double [R/W]
Document_Lines.Weight1Unit : Long [R/W]
Document_Lines.Weight2 : Double [R/W]
Document_Lines.Weight2Unit : Long [R/W]
Document_Lines.Width1 : Double [R/W]
Document_Lines.Width1Unit : Long [R/W]
Document_Lines.Width2 : Double [R/W]
Document_Lines.Width2Unit : Long [R/W]
Document_Lines.WithholdingTaxLines : WithholdingTaxLines [R]
Document_Lines.WithoutInventoryMovement : BoYesNoEnum [R/W]
Document_Lines.WTLiable : BoYesNoEnum [R/W]
Document_Lines.Add()
Document_Lines.Delete()
Document_Lines.SetCurrentLine(ByVal LineNum As Long)
Document_LinesAdditionalExpenses.AquisitionTax : BoYesNoEnum [R]
Document_LinesAdditionalExpenses.BaseGroup : Long [R/W]
Document_LinesAdditionalExpenses.Count : Long [R]
Document_LinesAdditionalExpenses.CUSplit : BoYesNoEnum [R/W]
Document_LinesAdditionalExpenses.DeductibleTaxSum : Double [R]
Document_LinesAdditionalExpenses.DeductibleTaxSumFC : Double [R]
Document_LinesAdditionalExpenses.DeductibleTaxSumSys : Double [R]
Document_LinesAdditionalExpenses.DistributionRule : String [R/W]
Document_LinesAdditionalExpenses.DistributionRule2 : String [R/W]
Document_LinesAdditionalExpenses.DistributionRule3 : String [R/W]
Document_LinesAdditionalExpenses.DistributionRule4 : String [R/W]
Document_LinesAdditionalExpenses.DistributionRule5 : String [R/W]
Document_LinesAdditionalExpenses.EBooksDetails : EBooks_Doc_Details [R]
Document_LinesAdditionalExpenses.EqualizationTaxFC : Double [R]
Document_LinesAdditionalExpenses.EqualizationTaxPercent : Double [R]
Document_LinesAdditionalExpenses.EqualizationTaxSum : Double [R]
Document_LinesAdditionalExpenses.EqualizationTaxSys : Double [R]
Document_LinesAdditionalExpenses.ExpenseCode : Long [R/W]
Document_LinesAdditionalExpenses.ExternalCalcTaxAmount : Double [R/W]
Document_LinesAdditionalExpenses.ExternalCalcTaxAmountFC : Double [R]
Document_LinesAdditionalExpenses.ExternalCalcTaxAmountSC : Double [R]
Document_LinesAdditionalExpenses.ExternalCalcTaxRate : Double [R/W]
Document_LinesAdditionalExpenses.GroupCode : Long [R/W]
Document_LinesAdditionalExpenses.LineNumber : Long [R/W]
Document_LinesAdditionalExpenses.LineTotal : Double [R/W]
Document_LinesAdditionalExpenses.LineTotalFC : Double [R]
Document_LinesAdditionalExpenses.LineTotalSys : Double [R]
Document_LinesAdditionalExpenses.PaidToDate : Double [R]
Document_LinesAdditionalExpenses.PaidToDateFC : Double [R]
Document_LinesAdditionalExpenses.PaidToDateSys : Double [R]
Document_LinesAdditionalExpenses.Project : String [R/W]
Document_LinesAdditionalExpenses.TaxCode : String [R/W]
Document_LinesAdditionalExpenses.TaxJurisdictions : TaxJurisdictions [R]
Document_LinesAdditionalExpenses.TaxLiable : BoYesNoEnum [R]
Document_LinesAdditionalExpenses.TaxPaid : Double [R]
Document_LinesAdditionalExpenses.TaxPaidFC : Double [R]
Document_LinesAdditionalExpenses.TaxPaidSys : Double [R]
Document_LinesAdditionalExpenses.TaxPercent : Double [R]
Document_LinesAdditionalExpenses.TaxSum : Double [R/W]
Document_LinesAdditionalExpenses.TaxSumFC : Double [R]
Document_LinesAdditionalExpenses.TaxSumSys : Double [R]
Document_LinesAdditionalExpenses.TaxTotalSum : Double [R]
Document_LinesAdditionalExpenses.TaxTotalSumFC : Double [R]
Document_LinesAdditionalExpenses.TaxTotalSumSys : Double [R]
Document_LinesAdditionalExpenses.TaxType : BoAdEpnsTaxTypes [R/W]
Document_LinesAdditionalExpenses.UserFields : UserFields [R]
Document_LinesAdditionalExpenses.VatGroup : String [R/W]
Document_LinesAdditionalExpenses.WTLiable : BoYesNoEnum [R/W]
Document_LinesAdditionalExpenses.Add()
Document_LinesAdditionalExpenses.SetCurrentLine(ByVal LineNum As Long)
Document_SpecialLines.AfterLineNumber : Long [R/W]
Document_SpecialLines.Count : Long [R]
Document_SpecialLines.Freight1 : Double [R]
Document_SpecialLines.Freight1FC : Double [R]
Document_SpecialLines.Freight1SC : Double [R]
Document_SpecialLines.Freight2 : Double [R]
Document_SpecialLines.Freight2FC : Double [R]
Document_SpecialLines.Freight2SC : Double [R]
Document_SpecialLines.Freight3 : Double [R]
Document_SpecialLines.Freight3FC : Double [R]
Document_SpecialLines.Freight3SC : Double [R]
Document_SpecialLines.GrossTotal : Double [R]
Document_SpecialLines.GrossTotalFC : Double [R]
Document_SpecialLines.GrossTotalSC : Double [R]
Document_SpecialLines.LineNum : Long [R]
Document_SpecialLines.LineText : String [R/W]
Document_SpecialLines.LineType : BoDocSpecialLineType [R/W]
Document_SpecialLines.OrderNumber : Long [R]
Document_SpecialLines.Subtotal : Double [R]
Document_SpecialLines.SubtotalFC : Double [R]
Document_SpecialLines.SubtotalSC : Double [R]
Document_SpecialLines.TaxAmount : Double [R]
Document_SpecialLines.TaxAmountFC : Double [R]
Document_SpecialLines.TaxAmountSC : Double [R]
Document_SpecialLines.Add()
Document_SpecialLines.Delete()
Document_SpecialLines.SetCurrentLine(ByVal LineNum As Long)
DocumentChangeMenuName.ChangedMenuName : String [R/W]
DocumentChangeMenuName.Document : String [R/W]
DocumentChangeMenuName.DocumentSubType : String [R/W]
DocumentChangeMenuName.FromXMLFile(ByVal bstrFileName As String)
DocumentChangeMenuName.FromXMLString(ByVal bstrXML As String)
DocumentChangeMenuName.GetXMLSchema() -> String
DocumentChangeMenuName.ToXMLFile(ByVal bstrFileName As String)
DocumentChangeMenuName.ToXMLString() -> String
DocumentLinesBinAllocations.AllowNegativeQuantity : BoYesNoEnum [R/W]
DocumentLinesBinAllocations.BaseLineNumber : Long [R/W]
DocumentLinesBinAllocations.BinAbsEntry : Long [R/W]
DocumentLinesBinAllocations.Count : Long [R]
DocumentLinesBinAllocations.Quantity : Double [R/W]
DocumentLinesBinAllocations.SerialAndBatchNumbersBaseLine : Long [R/W]
DocumentLinesBinAllocations.Add()
DocumentLinesBinAllocations.SetCurrentLine(ByVal LineNum As Long)
DocumentPackageItems.Count : Long [R]
DocumentPackageItems.ItemCode : String [R/W]
DocumentPackageItems.MeasureUnit : String [R]
DocumentPackageItems.Quantity : Double [R/W]
DocumentPackageItems.UnitsOfMeasurement : Double [R/W]
DocumentPackageItems.UoMEntry : Long [R/W]
DocumentPackageItems.UserFields : UserFields [R]
DocumentPackageItems.Add()
DocumentPackageItems.Delete()
DocumentPackageItems.SetCurrentLine(ByVal LineNum As Long)
DocumentPackages.Count : Long [R]
DocumentPackages.Items : DocumentPackageItems [R]
DocumentPackages.Number : Long [R/W]
DocumentPackages.TotalWeight : Double [R]
DocumentPackages.Type : String [R/W]
DocumentPackages.Units : Long [R/W]
DocumentPackages.UserFields : UserFields [R]
DocumentPackages.Add()
DocumentPackages.Delete()
DocumentPackages.SetCurrentLine(ByVal LineNum As Long)
Documents.AdditionalLegalInformation : String [R/W]
Documents.Address : String [R/W]
Documents.Address2 : String [R/W]
Documents.AddressExtension : AddressExtension [R]
Documents.AgentCode : String [R/W]
Documents.AnnualInvoiceDeclarationReference : Long [R/W]
Documents.ApplyCurrentVATRatesForDownPaymentsToDraw : BoYesNoEnum [R/W]
Documents.ApplyTaxOnFirstInstallment : BoYesNoEnum [R/W]
Documents.ArchiveNonremovableSalesQuotation : BoYesNoEnum [R/W]
Documents.AssetValueDate : Date [R/W]
Documents.ATDocumentType : String [R/W]
Documents.AttachmentEntry : Long [R/W]
Documents.AuthorizationCode : String [R/W]
Documents.AuthorizationStatus : DocumentAuthorizationStatusEnum [R]
Documents.BaseAmount : Double [R]
Documents.BaseAmountFC : Double [R]
Documents.BaseAmountSC : Double [R]
Documents.BaseEntry : Long [R/W]
Documents.BaseType : Long [R/W]
Documents.BillOfExchangeReserved : BoYesNoEnum [R]
Documents.BlanketAgreementNumber : Long [R/W]
Documents.BlockDunning : BoYesNoEnum [R/W]
Documents.Box1099 : String [R/W]
Documents.BPChannelCode : String [R/W]
Documents.BPChannelContact : Long [R/W]
Documents.BPL_IDAssignedToInvoice : Long [R/W]
Documents.BPLName : String [R]
Documents.Browser : DataBrowser [R]
Documents.CancelDate : Date [R/W]
Documents.Cancelled : BoYesNoEnum [R]
Documents.CancelStatus : CancelStatusEnum [R]
Documents.CardCode : String [R/W]
Documents.CardName : String [R/W]
Documents.CashDiscountDateOffset : Long [R/W]
Documents.CentralBankIndicator : String [R/W]
Documents.CertificationNumber : String [R]
Documents.Cig : Long [R/W]
Documents.ClosingDate : Date [R/W]
Documents.ClosingOption : ClosingOptionEnum [R/W]
Documents.ClosingRemarks : String [R/W]
Documents.Comments : String [R/W]
Documents.CommissionTrade : CommissionTradeTypeEnum [R/W]
Documents.CommissionTradeReturn : BoYesNoEnum [R/W]
Documents.Confirmed : BoYesNoEnum [R/W]
Documents.ContactPersonCode : Long [R/W]
Documents.ControlAccount : String [R/W]
Documents.CreateOnlineQuotation : BoYesNoEnum [R/W]
Documents.CreateQRCodeFrom : String [R/W]
Documents.CreationDate : Date [R]
Documents.Cup : Long [R/W]
Documents.CustOffice : String [R/W]
Documents.DANFELegalText : String [R]
Documents.DateOfReportingControlStatementVAT : Date [R/W]
Documents.DeferredTax : BoYesNoEnum [R/W]
Documents.DiscountPercent : Double [R/W]
Documents.DocCurrency : String [R/W]
Documents.DocDate : Date [R/W]
Documents.DocDueDate : Date [R/W]
Documents.DocEntry : Long [R]
Documents.DocNum : Long [R/W]
Documents.DocObjectCode : BoObjectTypes [R/W]
Documents.DocObjectCodeEx : String [R/W]
Documents.DocRate : Double [R/W]
Documents.DocTime : Date [R/W]
Documents.DocTotal : Double [R/W]
Documents.DocTotalFc : Double [R/W]
Documents.DocTotalSys : Double [R]
Documents.DocType : BoDocumentTypes [R/W]
Documents.Document_ApprovalRequests : Document_ApprovalRequests [R]
Documents.DocumentDelivery : DocumentDeliveryTypeEnum [R/W]
Documents.DocumentReferences : Document_DocumentReferences [R]
Documents.DocumentsOwner : Long [R/W]
Documents.DocumentStatus : BoStatus [R]
Documents.DocumentSubType : BoDocumentSubType [R/W]
Documents.DocumentTaxID : String [R/W]
Documents.DownPayment : Double [R/W]
Documents.DownPaymentAmount : Double [R/W]
Documents.DownPaymentAmountFC : Double [R/W]
Documents.DownPaymentAmountSC : Double [R/W]
Documents.DownPaymentPercentage : Double [R/W]
Documents.DownPaymentStatus : BoSoStatus [R/W]
Documents.DownPaymentsToDraw : DownPaymentsToDraw [R]
Documents.DownPaymentTrasactionID : String [R/W]
Documents.DownPaymentType : DownPaymentTypeEnum [R/W]
Documents.ECommerceGSTIN : String [R/W]
Documents.ECommerceOperator : String [R/W]
Documents.EDocErrorCode : String [R/W]
Documents.EDocErrorMessage : String [R/W]
Documents.EDocExportFormat : Long [R/W]
Documents.EDocGenerationType : EDocGenerationTypeEnum [R/W]
Documents.EDocNum : String [R/W]
Documents.EDocSeries : Long [R/W]
Documents.EDocStatus : EDocStatusEnum [R/W]
Documents.EDocType : EDocTypeEnum [R/W]
Documents.ElecCommMessage : String [R]
Documents.ElecCommStatus : ElecCommStatusEnum [R/W]
Documents.ElectronicProtocols : ElectronicProtocols [R]
Documents.EndDeliveryDate : Date [R/W]
Documents.EndDeliveryTime : Date [R/W]
Documents.ETaxNumber : String [R/W]
Documents.ETaxWebSite : Long [R/W]
Documents.EWayBillDetails : Document_EWayBillDetails [R]
Documents.ExcludeFromTaxReportControlStatementVAT : BoYesNoEnum [R/W]
Documents.ExemptionValidityDateFrom : Date [R/W]
Documents.ExemptionValidityDateTo : Date [R/W]
Documents.Expenses : DocumentsAdditionalExpenses [R]
Documents.ExternalCorrectedDocNum : String [R/W]
Documents.ExtraDays : Long [R/W]
Documents.ExtraMonth : Long [R/W]
Documents.FatherCard : String [R/W]
Documents.FatherType : BoFatherCardTypes [R/W]
Documents.FCEAsPaymentMeans : BoYesNoEnum [R/W]
Documents.FCI : String [R/W]
Documents.FederalTaxID : String [R/W]
Documents.FinancialPeriod : Long [R]
Documents.FiscalDocNum : String [R/W]
Documents.FolioNumber : Long [R/W]
Documents.FolioNumberFrom : Long [R/W]
Documents.FolioNumberTo : Long [R/W]
Documents.FolioPrefixString : String [R/W]
Documents.Form1099 : Long [R/W]
Documents.GroupHandWritten : BoYesNoEnum [R/W]
Documents.GroupNumber : Long [R/W]
Documents.GroupSeries : Long [R/W]
Documents.GSTTransactionType : GSTTransactionTypeEnum [R/W]
Documents.GTSChecker : Long [R/W]
Documents.GTSPayee : Long [R/W]
Documents.HandWritten : BoYesNoEnum [R/W]
Documents.ImportFileNum : Long [R/W]
Documents.Indicator : String [R/W]
Documents.IndicatorForFinalConsumer : BoYesNoEnum [R/W]
Documents.Installments : Document_Installments [R]
Documents.InsuranceOperation347 : BoYesNoEnum [R/W]
Documents.InterimType : BoInterimDocTypes [R/W]
Documents.InternalCorrectedDocNum : Long [R/W]
Documents.InventoryStatus : BoStatus [R]
Documents.InvoicePayment : BoYesNoEnum [R]
Documents.IsAlteration : BoYesNoEnum [R/W]
Documents.IsPayToBank : BoYesNoEnum [R/W]
Documents.IssuingReason : Long [R/W]
Documents.JournalMemo : String [R/W]
Documents.LanguageCode : Long [R/W]
Documents.LastPageFolioNumber : Long [R]
Documents.LegalTextFormat : Long [R/W]
Documents.Letter : FolioLetterEnum [R/W]
Documents.Lines : Document_Lines [R]
Documents.ManualNumber : String [R/W]
Documents.MaximumCashDiscount : BoYesNoEnum [R/W]
Documents.NetProcedure : BoYesNoEnum [R]
Documents.NextCorrectingDocument : Long [R]
Documents.NTSApproved : BoYesNoEnum [R/W]
Documents.NTSApprovedNumber : String [R/W]
Documents.NumAtCard : String [R/W]
Documents.NumberOfInstallments : Long [R/W]
Documents.OpenForLandedCosts : BoYesNoEnum [R/W]
Documents.OpeningRemarks : String [R/W]
Documents.OriginalCreditOrDebitDate : Date [R/W]
Documents.OriginalCreditOrDebitNo : String [R/W]
Documents.OriginalRefDate : Date [R/W]
Documents.OriginalRefNo : String [R/W]
Documents.Packages : DocumentPackages [R]
Documents.PaidToDate : Double [R]
Documents.PaidToDateFC : Double [R]
Documents.PaidToDateSys : Double [R]
Documents.PartialSupply : BoYesNoEnum [R/W]
Documents.PaymentBlock : BoYesNoEnum [R/W]
Documents.PaymentBlockEntry : Long [R/W]
Documents.PaymentGroupCode : Long [R/W]
Documents.PaymentMethod : String [R/W]
Documents.PaymentReference : String [R/W]
Documents.PayToBankAccountNo : String [R/W]
Documents.PayToBankBranch : String [R/W]
Documents.PayToBankCode : String [R/W]
Documents.PayToBankCountry : String [R/W]
Documents.PayToCode : String [R/W]
Documents.PeriodIndicator : String [R]
Documents.Pick : BoYesNoEnum [R/W]
Documents.PickRemark : String [R/W]
Documents.PickStatus : BoYesNoEnum [R]
Documents.PlasticPackagingTaxRelevant : BoYesNoEnum [R/W]
Documents.PointOfIssueCode : String [R/W]
Documents.POS_CashRegister : Long [R/W]
Documents.POSCashierNumber : Long [R/W]
Documents.POSDailySummaryNo : Long [R/W]
Documents.POSEquipmentNumber : String [R/W]
Documents.POSManufacturerSerialNumber : String [R/W]
Documents.POSReceiptNo : Long [R/W]
Documents.PriceMode : PriceModeDocumentEnum [R/W]
Documents.Printed : PrintStatusEnum [R/W]
Documents.PrintSEPADirect : BoYesNoEnum [R/W]
Documents.PrivateKeyVersion : Long [R]
Documents.Project : String [R/W]
Documents.Receiver : Long [R/W]
Documents.Reference1 : String [R/W]
Documents.Reference2 : String [R/W]
Documents.RelatedEntry : Long [R/W]
Documents.RelatedType : Long [R/W]
Documents.Releaser : Long [R/W]
Documents.RelevantToGTS : BoYesNoEnum [R/W]
Documents.ReopenManuallyClosedOrCanceledDocument : BoYesNoEnum [R/W]
Documents.ReopenOriginalDocument : BoYesNoEnum [R/W]
Documents.ReportingSectionControlStatementVAT : String [R/W]
Documents.ReqCode : String [R/W]
Documents.ReqType : Long [R/W]
Documents.Requester : String [R/W]
Documents.RequesterBranch : Long [R/W]
Documents.RequesterDepartment : Long [R/W]
Documents.RequesterEmail : String [R/W]
Documents.RequesterName : String [R/W]
Documents.RequriedDate : Date [R/W]
Documents.Reserve : BoYesNoEnum [R]
Documents.ReserveInvoice : BoYesNoEnum [R/W]
Documents.ReuseDocumentNum : BoYesNoEnum [R/W]
Documents.ReuseNotaFiscalNum : BoYesNoEnum [R/W]
Documents.Revision : BoYesNoEnum [R/W]
Documents.RevisionPo : BoYesNoEnum [R/W]
Documents.Rounding : BoYesNoEnum [R/W]
Documents.RoundingDiffAmount : Double [R/W]
Documents.RoundingDiffAmountFC : Double [R]
Documents.RoundingDiffAmountSC : Double [R]
Documents.SalesPersonCode : Long [R/W]
Documents.SAPPassport : String [R]
Documents.Segment : Long [R]
Documents.SendNotification : BoYesNoEnum [R/W]
Documents.SequenceCode : Long [R/W]
Documents.SequenceModel : String [R/W]
Documents.SequenceSerial : Long [R/W]
Documents.Series : Long [R/W]
Documents.SeriesString : String [R/W]
Documents.ServiceGrossProfitPercent : Double [R/W]
Documents.ShipFrom : String [R/W]
Documents.ShipPlace : String [R/W]
Documents.ShipState : String [R/W]
Documents.ShipToCode : String [R/W]
Documents.ShowSCN : BoYesNoEnum [R/W]
Documents.SignatureDigest : String [R]
Documents.SignatureInputMessage : String [R]
Documents.SOIWizardId : Long [R]
Documents.SpecialLines : Document_SpecialLines [R]
Documents.SpecifiedClosingDate : Date [R/W]
Documents.StartDeliveryDate : Date [R/W]
Documents.StartDeliveryTime : Date [R/W]
Documents.StartFrom : BoPayTermDueTypes [R/W]
Documents.Submitted : BoYesNoEnum [R]
Documents.SubSeriesString : String [R/W]
Documents.SummeryType : BoDocSummaryTypes [R/W]
Documents.Supplier : String [R/W]
Documents.TaxDate : Date [R/W]
Documents.TaxExemptionLetterNum : String [R/W]
Documents.TaxExtension : TaxExtension [R]
Documents.TaxInvoiceDate : Date [R/W]
Documents.TaxInvoiceNo : String [R/W]
Documents.TotalDiscount : Double [R]
Documents.TotalDiscountFC : Double [R]
Documents.TotalDiscountSC : Double [R]
Documents.TotalEqualizationTax : Double [R]
Documents.TotalEqualizationTaxFC : Double [R]
Documents.TotalEqualizationTaxSC : Double [R]
Documents.TrackingNumber : String [R/W]
Documents.TransNum : Long [R]
Documents.TransportationCode : Long [R/W]
Documents.UpdateDate : Date [R]
Documents.UpdateTime : Date [R]
Documents.UseBillToAddrToDetermineTax : BoYesNoEnum [R/W]
Documents.UseCorrectionVATGroup : BoYesNoEnum [R/W]
Documents.UserFields : UserFields [R]
Documents.UserSign : Long [R]
Documents.UseShpdGoodsAct : BoYesNoEnum [R/W]
Documents.VatDate : Date [R/W]
Documents.VatPercent : Double [R/W]
Documents.VATRegNum : String [R]
Documents.VatSum : Double [R]
Documents.VatSumFc : Double [R]
Documents.VatSumSys : Double [R]
Documents.VehiclePlate : String [R/W]
Documents.WareHouseUpdateType : BoDocWhsUpdateTypes [R/W]
Documents.WithholdingTaxData : WithholdingTaxData [R]
Documents.WithholdingTaxDataWTX : WithholdingTaxDataWTX [R]
Documents.WTAmount : Double [R]
Documents.WTAmountFC : Double [R]
Documents.WTAmountSC : Double [R]
Documents.WTApplied : Double [R]
Documents.WTAppliedFC : Double [R]
Documents.WTAppliedSC : Double [R]
Documents.WTExemptedAmount : Double [R]
Documents.WTExemptedAmountFC : Double [R]
Documents.WTExemptedAmountSC : Double [R]
Documents.WTNonSubjectAmount : Double [R]
Documents.WTNonSubjectAmountFC : Double [R]
Documents.WTNonSubjectAmountSC : Double [R]
Documents.Add() -> Long
Documents.Cancel() -> Long
Documents.Close() -> Long
Documents.CreateCancellationDocument() -> Documents
Documents.ExportEWayBill() -> Long
Documents.GetApprovalTemplates() -> Long
Documents.GetAsXML() -> String
Documents.GetByKey(ByVal AbsEntry As Long) -> Boolean
Documents.HandleApprovalRequest() -> Long
Documents.Remove() -> Long
Documents.Reopen() -> Long
Documents.RequestApproveCancellation() -> Long
Documents.SaveDraftToDocument() -> Long
Documents.SaveToFile(ByVal FileName As String)
Documents.SaveXML(ByRef FileName As String)
Documents.Update() -> Long
Documents.UpdateFromXML(ByVal FileName As String) -> Long
DocumentsAdditionalExpenses.AquisitionTax : BoYesNoEnum [R]
DocumentsAdditionalExpenses.BaseDocEntry : Long [R/W]
DocumentsAdditionalExpenses.BaseDocLine : Long [R/W]
DocumentsAdditionalExpenses.BaseDocType : Long [R/W]
DocumentsAdditionalExpenses.BaseDocumentReference : Long [R]
DocumentsAdditionalExpenses.Count : Long [R]
DocumentsAdditionalExpenses.CUSplit : BoYesNoEnum [R/W]
DocumentsAdditionalExpenses.DeductibleTaxSum : Double [R/W]
DocumentsAdditionalExpenses.DeductibleTaxSumFC : Double [R]
DocumentsAdditionalExpenses.DeductibleTaxSumSys : Double [R]
DocumentsAdditionalExpenses.DistributionMethod : BoAdEpnsDistribMethods [R/W]
DocumentsAdditionalExpenses.DistributionRule : String [R/W]
DocumentsAdditionalExpenses.DistributionRule2 : String [R/W]
DocumentsAdditionalExpenses.DistributionRule3 : String [R/W]
DocumentsAdditionalExpenses.DistributionRule4 : String [R/W]
DocumentsAdditionalExpenses.DistributionRule5 : String [R/W]
DocumentsAdditionalExpenses.EBooksDetails : EBooks_Doc_Details [R]
DocumentsAdditionalExpenses.EqualizationTaxFC : Double [R]
DocumentsAdditionalExpenses.EqualizationTaxPercent : Double [R]
DocumentsAdditionalExpenses.EqualizationTaxSum : Double [R]
DocumentsAdditionalExpenses.EqualizationTaxSys : Double [R]
DocumentsAdditionalExpenses.ExpenseCode : Long [R/W]
DocumentsAdditionalExpenses.ExternalCalcTaxAmount : Double [R/W]
DocumentsAdditionalExpenses.ExternalCalcTaxAmountFC : Double [R]
DocumentsAdditionalExpenses.ExternalCalcTaxAmountSC : Double [R]
DocumentsAdditionalExpenses.ExternalCalcTaxRate : Double [R/W]
DocumentsAdditionalExpenses.LastPurchasePrice : BoYesNoEnum [R/W]
DocumentsAdditionalExpenses.LineGross : Double [R/W]
DocumentsAdditionalExpenses.LineGrossFC : Double [R]
DocumentsAdditionalExpenses.LineGrossSys : Double [R]
DocumentsAdditionalExpenses.LineNum : Long [R]
DocumentsAdditionalExpenses.LineTotal : Double [R/W]
DocumentsAdditionalExpenses.LineTotalFC : Double [R]
DocumentsAdditionalExpenses.LineTotalSys : Double [R]
DocumentsAdditionalExpenses.PaidToDate : Double [R]
DocumentsAdditionalExpenses.PaidToDateFC : Double [R]
DocumentsAdditionalExpenses.PaidToDateSys : Double [R]
DocumentsAdditionalExpenses.Project : String [R/W]
DocumentsAdditionalExpenses.Remarks : String [R/W]
DocumentsAdditionalExpenses.Status : BoStatus [R]
DocumentsAdditionalExpenses.Stock : BoYesNoEnum [R/W]
DocumentsAdditionalExpenses.TargetAbsEntry : Long [R]
DocumentsAdditionalExpenses.TargetType : Long [R]
DocumentsAdditionalExpenses.TaxCode : String [R/W]
DocumentsAdditionalExpenses.TaxJurisdictions : TaxJurisdictions [R]
DocumentsAdditionalExpenses.TaxLiable : BoYesNoEnum [R]
DocumentsAdditionalExpenses.TaxPaid : Double [R]
DocumentsAdditionalExpenses.TaxPaidFC : Double [R]
DocumentsAdditionalExpenses.TaxPaidSys : Double [R]
DocumentsAdditionalExpenses.TaxPercent : Double [R]
DocumentsAdditionalExpenses.TaxSum : Double [R/W]
DocumentsAdditionalExpenses.TaxSumFC : Double [R]
DocumentsAdditionalExpenses.TaxSumSys : Double [R]
DocumentsAdditionalExpenses.TaxTotalSum : Double [R]
DocumentsAdditionalExpenses.TaxTotalSumFC : Double [R]
DocumentsAdditionalExpenses.TaxTotalSumSys : Double [R]
DocumentsAdditionalExpenses.TaxType : BoAdEpnsTaxTypes [R]
DocumentsAdditionalExpenses.UserFields : UserFields [R]
DocumentsAdditionalExpenses.VatGroup : String [R/W]
DocumentsAdditionalExpenses.WTLiable : BoYesNoEnum [R/W]
DocumentsAdditionalExpenses.Add()
DocumentsAdditionalExpenses.SetCurrentLine(ByVal LineNum As Long)
DocumentSeriesParams.Document : String [R/W]
DocumentSeriesParams.DocumentSubType : String [R/W]
DocumentSeriesParams.Series : Long [R/W]
DocumentSeriesParams.FromXMLFile(ByVal bstrFileName As String)
DocumentSeriesParams.FromXMLString(ByVal bstrXML As String)
DocumentSeriesParams.GetXMLSchema() -> String
DocumentSeriesParams.ToXMLFile(ByVal bstrFileName As String)
DocumentSeriesParams.ToXMLString() -> String
DocumentSeriesUserParams.Document : String [R/W]
DocumentSeriesUserParams.DocumentSubType : String [R/W]
DocumentSeriesUserParams.Series : Long [R/W]
DocumentSeriesUserParams.User : Long [R/W]
DocumentSeriesUserParams.FromXMLFile(ByVal bstrFileName As String)
DocumentSeriesUserParams.FromXMLString(ByVal bstrXML As String)
DocumentSeriesUserParams.GetXMLSchema() -> String
DocumentSeriesUserParams.ToXMLFile(ByVal bstrFileName As String)
DocumentSeriesUserParams.ToXMLString() -> String
DocumentTypeParams.Document : String [R/W]
DocumentTypeParams.DocumentSubType : String [R/W]
DocumentTypeParams.FromXMLFile(ByVal bstrFileName As String)
DocumentTypeParams.FromXMLString(ByVal bstrXML As String)
DocumentTypeParams.GetXMLSchema() -> String
DocumentTypeParams.ToXMLFile(ByVal bstrFileName As String)
DocumentTypeParams.ToXMLString() -> String
DownPaymentsToDraw.AmountToDraw : Double [R/W]
DownPaymentsToDraw.AmountToDrawFC : Double [R/W]
DownPaymentsToDraw.AmountToDrawSC : Double [R/W]
DownPaymentsToDraw.Count : Long [R]
DownPaymentsToDraw.Details : String [R]
DownPaymentsToDraw.DocEntry : Long [R/W]
DownPaymentsToDraw.DocInternalID : Long [R]
DownPaymentsToDraw.DocNumber : Long [R]
DownPaymentsToDraw.DownPaymentsToDrawDetails : DownPaymentsToDrawDetails [R]
DownPaymentsToDraw.DownPaymentType : DownPaymentTypeEnum [R]
DownPaymentsToDraw.DueDate : Date [R]
DownPaymentsToDraw.GrossAmountToDraw : Double [R/W]
DownPaymentsToDraw.GrossAmountToDrawFC : Double [R/W]
DownPaymentsToDraw.GrossAmountToDrawSC : Double [R/W]
DownPaymentsToDraw.IsGrossLine : BoYesNoEnum [R]
DownPaymentsToDraw.Name : String [R]
DownPaymentsToDraw.PostingDate : Date [R]
DownPaymentsToDraw.RowNum : Long [R]
DownPaymentsToDraw.Tax : Double [R]
DownPaymentsToDraw.TaxFC : Double [R]
DownPaymentsToDraw.TaxSC : Double [R]
DownPaymentsToDraw.Add()
DownPaymentsToDraw.SetCurrentLine(ByVal LineNum As Long)
DownPaymentsToDrawDetails.AmountToDraw : Double [R/W]
DownPaymentsToDrawDetails.AmountToDrawFC : Double [R/W]
DownPaymentsToDrawDetails.AmountToDrawSC : Double [R/W]
DownPaymentsToDrawDetails.Count : Long [R]
DownPaymentsToDrawDetails.DocEntry : Long [R]
DownPaymentsToDrawDetails.DocInternalID : Long [R]
DownPaymentsToDrawDetails.GrossAmountToDraw : Double [R/W]
DownPaymentsToDrawDetails.GrossAmountToDrawFC : Double [R/W]
DownPaymentsToDrawDetails.GrossAmountToDrawSC : Double [R/W]
DownPaymentsToDrawDetails.IsGrossLine : BoYesNoEnum [R]
DownPaymentsToDrawDetails.LineType : LineTypeEnum [R/W]
DownPaymentsToDrawDetails.RowNum : Long [R/W]
DownPaymentsToDrawDetails.SeqNum : Long [R]
DownPaymentsToDrawDetails.Tax : Double [R/W]
DownPaymentsToDrawDetails.TaxAdjust : BoYesNoEnum [R]
DownPaymentsToDrawDetails.TaxFC : Double [R/W]
DownPaymentsToDrawDetails.TaxSC : Double [R/W]
DownPaymentsToDrawDetails.VatGroupCode : String [R/W]
DownPaymentsToDrawDetails.VatPercent : Double [R]
DownPaymentsToDrawDetails.Add()
DownPaymentsToDrawDetails.SetCurrentLine(ByVal LineNum As Long)
DppChangeParams.FromDate : Date [R/W]
DppChangeParams.FromTime : Date [R/W]
DppChangeParams.HasChanged : BoYesNoEnum [R]
DppChangeParams.FromXMLFile(ByVal bstrFileName As String)
DppChangeParams.FromXMLString(ByVal bstrXML As String)
DppChangeParams.GetXMLSchema() -> String
DppChangeParams.ToXMLFile(ByVal bstrFileName As String)
DppChangeParams.ToXMLString() -> String
DunningLetters.Browser : DataBrowser [R]
DunningLetters.CalcInterest : BoYesNoEnum [R/W]
DunningLetters.Effectiveafter : String [R/W]
DunningLetters.FeeCurrency : String [R/W]
DunningLetters.Feeperletter : Double [R/W]
DunningLetters.LetterFormat : String [R/W]
DunningLetters.MinimumBalance : Double [R/W]
DunningLetters.MinimumBalanceCurrency : String [R/W]
DunningLetters.RowNumber : Long [R/W]
DunningLetters.UserFields : UserFields [R]
DunningLetters.Add() -> Long
DunningLetters.GetAsXML() -> String
DunningLetters.GetByKey(ByVal lID As Long) -> Boolean
DunningLetters.Remove() -> Long
DunningLetters.SaveToFile(ByVal FileName As String)
DunningLetters.SaveXML(ByRef FileName As String)
DunningLetters.Update() -> Long
DunningTerm.ApplyHighestLetterTemplate : BoYesNoEnum [R/W]
DunningTerm.AutomaticPosting : AutomaticPostingEnum [R/W]
DunningTerm.BaseDateSelect : BaseDateSelectEnum [R/W]
DunningTerm.CalculateInterestMethod : CalculateInterestMethodEnum [R/W]
DunningTerm.Code : String [R/W]
DunningTerm.DaysInMonth : Long [R/W]
DunningTerm.DaysInYear : Long [R/W]
DunningTerm.DunningTermLines : DunningTermLines [R]
DunningTerm.ExchangeRateSelect : ExchangeRateSelectEnum [R/W]
DunningTerm.FeeAccount : String [R/W]
DunningTerm.GroupingMethod : GroupingMethodEnum [R/W]
DunningTerm.IncludeInterest : BoYesNoEnum [R/W]
DunningTerm.InterestAccount : String [R/W]
DunningTerm.LetterFee : Double [R/W]
DunningTerm.LetterFeeCurrency : String [R/W]
DunningTerm.MinimumBalance : Double [R/W]
DunningTerm.MinimumBalanceCurrency : String [R/W]
DunningTerm.Name : String [R/W]
DunningTerm.YearlyInterestRate : Double [R/W]
DunningTerm.FromXMLFile(ByVal bstrFileName As String)
DunningTerm.FromXMLString(ByVal bstrXML As String)
DunningTerm.GetXMLSchema() -> String
DunningTerm.ToXMLFile(ByVal bstrFileName As String)
DunningTerm.ToXMLString() -> String
DunningTermLine.CalculateInterest : BoYesNoEnum [R/W]
DunningTermLine.Effectiveafter : String [R/W]
DunningTermLine.LetterFee : Double [R/W]
DunningTermLine.LetterFeeCurrency : String [R/W]
DunningTermLine.LetterFormat : DunningLetterTypeEnum [R/W]
DunningTermLine.LevelNum : Long [R]
DunningTermLine.MininumBalance : Double [R/W]
DunningTermLine.MininumBalanceCurrency : String [R/W]
DunningTermLine.FromXMLFile(ByVal bstrFileName As String)
DunningTermLine.FromXMLString(ByVal bstrXML As String)
DunningTermLine.GetXMLSchema() -> String
DunningTermLine.ToXMLFile(ByVal bstrFileName As String)
DunningTermLine.ToXMLString() -> String
DunningTermLines.Count : Long [R]
DunningTermLines.Add() -> DunningTermLine
DunningTermLines.GetXMLSchema() -> String
DunningTermLines.Item(ByVal vtIndex As Variant) -> DunningTermLine
DunningTermLines.Remove(ByVal vtIndex As Variant)
DunningTermLines.ToXMLFile(ByVal bstrFileName As String)
DunningTermLines.ToXMLString() -> String
DunningTermParams.Code : String [R/W]
DunningTermParams.Name : String [R]
DunningTermParams.FromXMLFile(ByVal bstrFileName As String)
DunningTermParams.FromXMLString(ByVal bstrXML As String)
DunningTermParams.GetXMLSchema() -> String
DunningTermParams.ToXMLFile(ByVal bstrFileName As String)
DunningTermParams.ToXMLString() -> String
DunningTermsParams.Count : Long [R]
DunningTermsParams.Add() -> DunningTermParams
DunningTermsParams.GetXMLSchema() -> String
DunningTermsParams.Item(ByVal vtIndex As Variant) -> DunningTermParams
DunningTermsParams.ToXMLFile(ByVal bstrFileName As String)
DunningTermsParams.ToXMLString() -> String
DunningTermsService.AddDunningTerm(ByVal pIDunningTerm As DunningTerm) -> DunningTermParams
DunningTermsService.DeleteDunningTerm(ByVal pIDunningTermParams As DunningTermParams)
DunningTermsService.GetDataInterface(ByVal enumMSDI As DunningTermsServiceDataInterfaces) -> Object
DunningTermsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
DunningTermsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
DunningTermsService.GetDunningTerm(ByVal pIDunningTermParams As DunningTermParams) -> DunningTerm
DunningTermsService.GetDunningTermList() -> DunningTermsParams
DunningTermsService.UpdateDunningTerm(ByVal pIDunningTerm As DunningTerm)
DynamicSystemStrings.Browser : DataBrowser [R]
DynamicSystemStrings.ColumnID : String [R/W]
DynamicSystemStrings.FormID : String [R/W]
DynamicSystemStrings.IsBold : BoYesNoEnum [R/W]
DynamicSystemStrings.IsItalics : BoYesNoEnum [R/W]
DynamicSystemStrings.ItemID : String [R/W]
DynamicSystemStrings.ItemString : String [R/W]
DynamicSystemStrings.UserFields : UserFields [R]
DynamicSystemStrings.Add() -> Long
DynamicSystemStrings.GetAsXML() -> String
DynamicSystemStrings.GetByKey(ByVal bstrFormId As String, ByVal bstrItemNum As String, ByVal bstrColNum As String) -> Boolean
DynamicSystemStrings.Remove() -> Long
DynamicSystemStrings.SaveToFile(ByVal bstrFileName As String)
DynamicSystemStrings.SaveXML(ByRef pbstrFileName As String)
DynamicSystemStrings.Update() -> Long
EBooks.AA : String [R]
EBooks.AbsEntry : Long [R]
EBooks.CancelMARK : String [R]
EBooks.CPVATID : String [R]
EBooks.Currency : String [R]
EBooks.EBooksLines : EBooksLines [R]
EBooks.InvoiceType : String [R]
EBooks.IsNegativeMark : BoYesNoEnum [R/W]
EBooks.IssueDate : Date [R]
EBooks.IssuerVATID : String [R]
EBooks.LinkedDocEntry : Long [R/W]
EBooks.LinkedDocType : Long [R/W]
EBooks.MARK : String [R]
EBooks.Series : String [R]
EBooks.TotalGrossValue : Double [R]
EBooks.TotalNetValue : Double [R]
EBooks.TotalVatAmount : Double [R]
EBooks.TotalWithheldAmount : Double [R]
EBooks.UID : String [R]
EBooks.FromXMLFile(ByVal bstrFileName As String)
EBooks.FromXMLString(ByVal bstrXML As String)
EBooks.GetXMLSchema() -> String
EBooks.ToXMLFile(ByVal bstrFileName As String)
EBooks.ToXMLString() -> String
EBooks_Doc_Details.ExpensesClassificationCategory : Long [R/W]
EBooks_Doc_Details.ExpensesClassificationType : Long [R/W]
EBooks_Doc_Details.IncomeClassificationCategory : Long [R/W]
EBooks_Doc_Details.IncomeClassificationType : Long [R/W]
EBooks_Doc_Details.NetValueFC : Double [R]
EBooks_Doc_Details.NetValueLC : Double [R]
EBooks_Doc_Details.NetValueSC : Double [R]
EBooks_Doc_Details.VatCategory : Long [R]
EBooks_Doc_Details.VatClassificationCategory : Long [R/W]
EBooks_Doc_Details.VatClassificationType : Long [R/W]
EBooks_Doc_Details.VATExemptionCause : Long [R/W]
EBooks_Doc_Details.WithheldAmountFC : Double [R]
EBooks_Doc_Details.WithheldAmountLC : Double [R]
EBooks_Doc_Details.WithheldAmountSC : Double [R]
EBooks_Doc_Details.WithheldPercentCategory : Long [R]
EBooksLine.ExpenseClassificationCategory : Long [R/W]
EBooksLine.ExpenseClassificationType : Long [R/W]
EBooksLine.LineNumber : Long [R]
EBooksLine.NetValue : Double [R]
EBooksLine.VatAmount : Double [R]
EBooksLine.VatCategory : Long [R]
EBooksLine.VatClassificationCategory : Long [R/W]
EBooksLine.VatClassificationType : Long [R/W]
EBooksLine.WithheldAmount : Double [R]
EBooksLine.WithheldPercentCategory : Long [R]
EBooksLine.FromXMLFile(ByVal bstrFileName As String)
EBooksLine.FromXMLString(ByVal bstrXML As String)
EBooksLine.GetXMLSchema() -> String
EBooksLine.ToXMLFile(ByVal bstrFileName As String)
EBooksLine.ToXMLString() -> String
EBooksLines.Count : Long [R]
EBooksLines.Add() -> EBooksLine
EBooksLines.GetXMLSchema() -> String
EBooksLines.Item(ByVal vtIndex As Variant) -> EBooksLine
EBooksLines.ToXMLFile(ByVal bstrFileName As String)
EBooksLines.ToXMLString() -> String
EBooksParams.LinkedDocEntry : Long [R/W]
EBooksParams.LinkedDocType : Long [R/W]
EBooksParams.MARK : String [R/W]
EBooksParams.FromXMLFile(ByVal bstrFileName As String)
EBooksParams.FromXMLString(ByVal bstrXML As String)
EBooksParams.GetXMLSchema() -> String
EBooksParams.ToXMLFile(ByVal bstrFileName As String)
EBooksParams.ToXMLString() -> String
EBooksParamsCollection.Count : Long [R]
EBooksParamsCollection.Add() -> EBooksParams
EBooksParamsCollection.GetXMLSchema() -> String
EBooksParamsCollection.Item(ByVal vtIndex As Variant) -> EBooksParams
EBooksParamsCollection.ToXMLFile(ByVal bstrFileName As String)
EBooksParamsCollection.ToXMLString() -> String
EBooksService.Get(ByVal pIEBooksParams As EBooksParams) -> EBooks
EBooksService.GetByDocKey(ByVal pIEBooksParams As EBooksParams) -> EBooksParamsCollection
EBooksService.GetByMark(ByVal pIEBooksParams As EBooksParams) -> EBooks
EBooksService.GetDataInterface(ByVal enumMSDI As EBooksServiceDataInterfaces) -> Object
EBooksService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EBooksService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EBooksService.Update(ByVal pIEBooks As EBooks)
EcmAction.ActionID : Long [R]
EcmAction.AssignedID : String [R/W]
EcmAction.BusinessPlace : Long [R/W]
EcmAction.Description : String [R/W]
EcmAction.DocumentBatch : String [R/W]
EcmAction.DocumentBatchLine : Long [R/W]
EcmAction.Environment : Long [R/W]
EcmAction.GenerationType : EcmActionGenerationTypeEnum [R/W]
EcmAction.IsCanceled : BoYesNoEnum [R]
EcmAction.IsRemoved : BoYesNoEnum [R]
EcmAction.Message : String [R/W]
EcmAction.ObjectID : String [R/W]
EcmAction.PeriodDateFrom : Date [R/W]
EcmAction.PeriodDateTo : Date [R/W]
EcmAction.PeriodNumber : Long [R/W]
EcmAction.PeriodType : EcmActionPeriodTypeEnum [R/W]
EcmAction.PeriodYear : Long [R/W]
EcmAction.Protocol : String [R/W]
EcmAction.ReportID : String [R/W]
EcmAction.SourceObject : Long [R/W]
EcmAction.SourceType : String [R/W]
EcmAction.Status : EcmActionStatusEnum [R/W]
EcmAction.Submits : Long [R/W]
EcmAction.Type : EcmActionTypeEnum [R/W]
EcmAction.UserFields : Fields [R]
EcmAction.FromXMLFile(ByVal bstrFileName As String)
EcmAction.FromXMLString(ByVal bstrXML As String)
EcmAction.GetXMLSchema() -> String
EcmAction.ToXMLFile(ByVal bstrFileName As String)
EcmAction.ToXMLString() -> String
EcmActionDocParams.Protocol : String [R/W]
EcmActionDocParams.SourceObject : Long [R/W]
EcmActionDocParams.SourceType : String [R/W]
EcmActionDocParams.FromXMLFile(ByVal bstrFileName As String)
EcmActionDocParams.FromXMLString(ByVal bstrXML As String)
EcmActionDocParams.GetXMLSchema() -> String
EcmActionDocParams.ToXMLFile(ByVal bstrFileName As String)
EcmActionDocParams.ToXMLString() -> String
EcmActionLog.ActionID : Long [R/W]
EcmActionLog.Data : String [R/W]
EcmActionLog.ExportFile : String [R/W]
EcmActionLog.ExportFormat : Long [R/W]
EcmActionLog.LogDate : Date [R/W]
EcmActionLog.LogID : Long [R]
EcmActionLog.LogTime : Long [R/W]
EcmActionLog.Message : String [R/W]
EcmActionLog.Type : EcmActionLogTypeEnum [R/W]
EcmActionLog.FromXMLFile(ByVal bstrFileName As String)
EcmActionLog.FromXMLString(ByVal bstrXML As String)
EcmActionLog.GetXMLSchema() -> String
EcmActionLog.ToXMLFile(ByVal bstrFileName As String)
EcmActionLog.ToXMLString() -> String
EcmActionLogCollection.Count : Long [R]
EcmActionLogCollection.Add() -> EcmActionLog
EcmActionLogCollection.GetXMLSchema() -> String
EcmActionLogCollection.Item(ByVal vtIndex As Variant) -> EcmActionLog
EcmActionLogCollection.ToXMLFile(ByVal bstrFileName As String)
EcmActionLogCollection.ToXMLString() -> String
EcmActionLogParams.ActionID : Long [R/W]
EcmActionLogParams.LogID : Long [R/W]
EcmActionLogParams.FromXMLFile(ByVal bstrFileName As String)
EcmActionLogParams.FromXMLString(ByVal bstrXML As String)
EcmActionLogParams.GetXMLSchema() -> String
EcmActionLogParams.ToXMLFile(ByVal bstrFileName As String)
EcmActionLogParams.ToXMLString() -> String
EcmActionParams.ActionID : Long [R/W]
EcmActionParams.FromXMLFile(ByVal bstrFileName As String)
EcmActionParams.FromXMLString(ByVal bstrXML As String)
EcmActionParams.GetXMLSchema() -> String
EcmActionParams.ToXMLFile(ByVal bstrFileName As String)
EcmActionParams.ToXMLString() -> String
ECMActionStatusData.AbsEntry : Long [R]
ECMActionStatusData.ActMessage : String [R/W]
ECMActionStatusData.ActStatus : EcmActionStatusEnum [R/W]
ECMActionStatusData.ReceivDate : Date [R/W]
ECMActionStatusData.ReportID : String [R/W]
ECMActionStatusData.FromXMLFile(ByVal bstrFileName As String)
ECMActionStatusData.FromXMLString(ByVal bstrXML As String)
ECMActionStatusData.GetXMLSchema() -> String
ECMActionStatusData.ToXMLFile(ByVal bstrFileName As String)
ECMActionStatusData.ToXMLString() -> String
ECMCodeParams.AbsEntry : Long [R/W]
ECMCodeParams.FromXMLFile(ByVal bstrFileName As String)
ECMCodeParams.FromXMLString(ByVal bstrXML As String)
ECMCodeParams.GetXMLSchema() -> String
ECMCodeParams.ToXMLFile(ByVal bstrFileName As String)
ECMCodeParams.ToXMLString() -> String
ECMCodeParamsCollection.Count : Long [R]
ECMCodeParamsCollection.Add() -> ECMCodeParams
ECMCodeParamsCollection.GetXMLSchema() -> String
ECMCodeParamsCollection.Item(ByVal vtIndex As Variant) -> ECMCodeParams
ECMCodeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ECMCodeParamsCollection.ToXMLString() -> String
EDFDocMapping.Description : String [R]
EDFDocMapping.ID : Long [R]
EDFDocMapping.Name : String [R]
EDFDocMapping.FromXMLFile(ByVal bstrFileName As String)
EDFDocMapping.FromXMLString(ByVal bstrXML As String)
EDFDocMapping.GetXMLSchema() -> String
EDFDocMapping.ToXMLFile(ByVal bstrFileName As String)
EDFDocMapping.ToXMLString() -> String
EDFDocMappingInputParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFDocMappingInputParams.DocType : String [R/W]
EDFDocMappingInputParams.FromXMLFile(ByVal bstrFileName As String)
EDFDocMappingInputParams.FromXMLString(ByVal bstrXML As String)
EDFDocMappingInputParams.GetXMLSchema() -> String
EDFDocMappingInputParams.ToXMLFile(ByVal bstrFileName As String)
EDFDocMappingInputParams.ToXMLString() -> String
EDFDocMappingsCollection.Count : Long [R]
EDFDocMappingsCollection.Add() -> EDFDocMapping
EDFDocMappingsCollection.GetXMLSchema() -> String
EDFDocMappingsCollection.Item(ByVal vtIndex As Variant) -> EDFDocMapping
EDFDocMappingsCollection.ToXMLFile(ByVal bstrFileName As String)
EDFDocMappingsCollection.ToXMLString() -> String
EDFEntriesCollection.Count : Long [R]
EDFEntriesCollection.Add() -> EDFEntry
EDFEntriesCollection.GetXMLSchema() -> String
EDFEntriesCollection.Item(ByVal vtIndex As Variant) -> EDFEntry
EDFEntriesCollection.ToXMLFile(ByVal bstrFileName As String)
EDFEntriesCollection.ToXMLString() -> String
EDFEntry.AbsEntry : Long [R]
EDFEntry.AssignedID : String [R/W]
EDFEntry.Authority : String [R/W]
EDFEntry.BranchID : Long [R/W]
EDFEntry.CancellationStatus : ElectronicDocumentEntryCancellationStatusEnum [R/W]
EDFEntry.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFEntry.CreateDate : Date [R]
EDFEntry.CreateTime : Long [R]
EDFEntry.Description : String [R/W]
EDFEntry.DocBatchID : String [R/W]
EDFEntry.DocBatchIndex : Long [R/W]
EDFEntry.EDocNum : String [R/W]
EDFEntry.EDocType : Long [R/W]
EDFEntry.Environment : Long [R/W]
EDFEntry.GenerationType : ElectronicDocGenTypeEnum [R/W]
EDFEntry.Guid : String [R/W]
EDFEntry.IsCancelation : BoYesNoEnum [R]
EDFEntry.IsRemoved : BoYesNoEnum [R]
EDFEntry.Message : String [R/W]
EDFEntry.ObjectID : String [R/W]
EDFEntry.ParentAbsEntry : Long [R/W]
EDFEntry.PeriodDateFrom : Date [R/W]
EDFEntry.PeriodDateTo : Date [R/W]
EDFEntry.PeriodNumber : Long [R/W]
EDFEntry.PeriodType : ElectronicDocumentEntryPeriodTypeEnum [R/W]
EDFEntry.PeriodYear : Long [R/W]
EDFEntry.ProcessingTarget : String [R/W]
EDFEntry.ReportID : String [R/W]
EDFEntry.ScheduledJobID : Long [R/W]
EDFEntry.SrcAbsEntry : Long [R/W]
EDFEntry.SrcObjType : String [R/W]
EDFEntry.Status : ElectronicDocumentEntryStatusEnum [R/W]
EDFEntry.Submits : Long [R/W]
EDFEntry.TestMode : BoYesNoEnum [R/W]
EDFEntry.Type : ElectronicDocumentEntryTypeEnum [R/W]
EDFEntry.UpdateDate : Date [R]
EDFEntry.UpdateTime : Long [R]
EDFEntry.User : Long [R]
EDFEntry.User2 : Long [R]
EDFEntry.UserFields : Fields [R]
EDFEntry.FromXMLFile(ByVal bstrFileName As String)
EDFEntry.FromXMLString(ByVal bstrXML As String)
EDFEntry.GetXMLSchema() -> String
EDFEntry.ToXMLFile(ByVal bstrFileName As String)
EDFEntry.ToXMLString() -> String
EDFEntryAddLogInputParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFEntryAddLogInputParams.ExportFile : String [R/W]
EDFEntryAddLogInputParams.ExportFormat : Long [R/W]
EDFEntryAddLogInputParams.Guid : String [R/W]
EDFEntryAddLogInputParams.LogData : String [R/W]
EDFEntryAddLogInputParams.LogDataContentType : ElectronicDocumentBlobContentTypeEnum [R/W]
EDFEntryAddLogInputParams.LogMessage : String [R/W]
EDFEntryAddLogInputParams.LogType : ElectronicDocumentEntryLogTypeEnum [R/W]
EDFEntryAddLogInputParams.ZipLogData : BoYesNoEnum [R/W]
EDFEntryAddLogInputParams.FromXMLFile(ByVal bstrFileName As String)
EDFEntryAddLogInputParams.FromXMLString(ByVal bstrXML As String)
EDFEntryAddLogInputParams.GetXMLSchema() -> String
EDFEntryAddLogInputParams.ToXMLFile(ByVal bstrFileName As String)
EDFEntryAddLogInputParams.ToXMLString() -> String
EDFEntryInputParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFEntryInputParams.Guid : String [R/W]
EDFEntryInputParams.FromXMLFile(ByVal bstrFileName As String)
EDFEntryInputParams.FromXMLString(ByVal bstrXML As String)
EDFEntryInputParams.GetXMLSchema() -> String
EDFEntryInputParams.ToXMLFile(ByVal bstrFileName As String)
EDFEntryInputParams.ToXMLString() -> String
EDFEntryListInputParams.Ascending : BoYesNoEnum [R/W]
EDFEntryListInputParams.BranchID : Long [R/W]
EDFEntryListInputParams.CancellationStatusSet : String [R/W]
EDFEntryListInputParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFEntryListInputParams.FromDate : Date [R/W]
EDFEntryListInputParams.FromEntryID : Long [R/W]
EDFEntryListInputParams.FromTime : Long [R/W]
EDFEntryListInputParams.MaxLines : Long [R/W]
EDFEntryListInputParams.ProcessingTarget : ElectronicDocProcessingTargetEnum [R/W]
EDFEntryListInputParams.ProcessingTargetStr : String [R/W]
EDFEntryListInputParams.StoreEntryStatusSet : String [R/W]
EDFEntryListInputParams.StoreEntryTypeSet : String [R/W]
EDFEntryListInputParams.ToDate : Date [R/W]
EDFEntryListInputParams.ToTime : Long [R/W]
EDFEntryListInputParams.FromXMLFile(ByVal bstrFileName As String)
EDFEntryListInputParams.FromXMLString(ByVal bstrXML As String)
EDFEntryListInputParams.GetXMLSchema() -> String
EDFEntryListInputParams.ToXMLFile(ByVal bstrFileName As String)
EDFEntryListInputParams.ToXMLString() -> String
EDFEntryLog.AbsEntry : Long [R]
EDFEntryLog.ExportFile : String [R/W]
EDFEntryLog.ExportFormat : Long [R/W]
EDFEntryLog.LogData : String [R/W]
EDFEntryLog.LogMessage : String [R/W]
EDFEntryLog.LogNumber : Long [R]
EDFEntryLog.LogOperationDate : Date [R/W]
EDFEntryLog.LogOperationTime : Long [R/W]
EDFEntryLog.LogType : ElectronicDocumentEntryLogTypeEnum [R/W]
EDFEntryLog.FromXMLFile(ByVal bstrFileName As String)
EDFEntryLog.FromXMLString(ByVal bstrXML As String)
EDFEntryLog.GetXMLSchema() -> String
EDFEntryLog.ToXMLFile(ByVal bstrFileName As String)
EDFEntryLog.ToXMLString() -> String
EDFEntryLogInputParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFEntryLogInputParams.FileName : String [R/W]
EDFEntryLogInputParams.Guid : String [R/W]
EDFEntryLogInputParams.KeepLogDataPrefix : BoYesNoEnum [R/W]
EDFEntryLogInputParams.LogDataContentType : ElectronicDocumentBlobContentTypeEnum [R/W]
EDFEntryLogInputParams.LogType : ElectronicDocumentEntryLogTypeEnum [R/W]
EDFEntryLogInputParams.UnzipLogData : BoYesNoEnum [R/W]
EDFEntryLogInputParams.FromXMLFile(ByVal bstrFileName As String)
EDFEntryLogInputParams.FromXMLString(ByVal bstrXML As String)
EDFEntryLogInputParams.GetXMLSchema() -> String
EDFEntryLogInputParams.ToXMLFile(ByVal bstrFileName As String)
EDFEntryLogInputParams.ToXMLString() -> String
EDFEntryLogsCollection.Count : Long [R]
EDFEntryLogsCollection.Add() -> EDFEntryLog
EDFEntryLogsCollection.GetXMLSchema() -> String
EDFEntryLogsCollection.Item(ByVal vtIndex As Variant) -> EDFEntryLog
EDFEntryLogsCollection.ToXMLFile(ByVal bstrFileName As String)
EDFEntryLogsCollection.ToXMLString() -> String
EDFImportEntry.AbsEntry : Long [R]
EDFImportEntry.Authority : String [R/W]
EDFImportEntry.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFImportEntry.CreateDate : Date [R]
EDFImportEntry.CreateTime : Long [R]
EDFImportEntry.FileName : String [R/W]
EDFImportEntry.Guid : String [R/W]
EDFImportEntry.Message : String [R/W]
EDFImportEntry.MetaData : String [R/W]
EDFImportEntry.MimeType : String [R/W]
EDFImportEntry.ProcessingSource : String [R/W]
EDFImportEntry.Status : ElectronicDocumentEntryStatusEnum [R/W]
EDFImportEntry.TestMode : String [R/W]
EDFImportEntry.UpdateDate : Date [R]
EDFImportEntry.UpdateTime : Long [R]
EDFImportEntry.User : Long [R]
EDFImportEntry.User2 : Long [R]
EDFImportEntry.FromXMLFile(ByVal bstrFileName As String)
EDFImportEntry.FromXMLString(ByVal bstrXML As String)
EDFImportEntry.GetXMLSchema() -> String
EDFImportEntry.ToXMLFile(ByVal bstrFileName As String)
EDFImportEntry.ToXMLString() -> String
EDFMapping.FormatID : Long [R]
EDFMapping.Hash : String [R]
EDFMapping.Mapping : String [R]
EDFMapping.Name : String [R]
EDFMapping.FromXMLFile(ByVal bstrFileName As String)
EDFMapping.FromXMLString(ByVal bstrXML As String)
EDFMapping.GetXMLSchema() -> String
EDFMapping.ToXMLFile(ByVal bstrFileName As String)
EDFMapping.ToXMLString() -> String
EDFMappingInputParams.Hash : String [R/W]
EDFMappingInputParams.FromXMLFile(ByVal bstrFileName As String)
EDFMappingInputParams.FromXMLString(ByVal bstrXML As String)
EDFMappingInputParams.GetXMLSchema() -> String
EDFMappingInputParams.ToXMLFile(ByVal bstrFileName As String)
EDFMappingInputParams.ToXMLString() -> String
EDFProtocol.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFProtocol.Description : String [R]
EDFProtocol.IsActive : BoYesNoEnum [R]
EDFProtocol.FromXMLFile(ByVal bstrFileName As String)
EDFProtocol.FromXMLString(ByVal bstrXML As String)
EDFProtocol.GetXMLSchema() -> String
EDFProtocol.ToXMLFile(ByVal bstrFileName As String)
EDFProtocol.ToXMLString() -> String
EDFProtocolInputParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
EDFProtocolInputParams.Description : String [R]
EDFProtocolInputParams.IsActive : BoYesNoEnum [R]
EDFProtocolInputParams.FromXMLFile(ByVal bstrFileName As String)
EDFProtocolInputParams.FromXMLString(ByVal bstrXML As String)
EDFProtocolInputParams.GetXMLSchema() -> String
EDFProtocolInputParams.ToXMLFile(ByVal bstrFileName As String)
EDFProtocolInputParams.ToXMLString() -> String
EDFProtocolParameter.BranchID : Long [R]
EDFProtocolParameter.Code : ElectronicDocProtocolCodeStrEnum [R]
EDFProtocolParameter.ParameterID : Long [R]
EDFProtocolParameter.ParamName : String [R]
EDFProtocolParameter.ParamParameters : String [R]
EDFProtocolParameter.ParamValue : String [R]
EDFProtocolParameter.FromXMLFile(ByVal bstrFileName As String)
EDFProtocolParameter.FromXMLString(ByVal bstrXML As String)
EDFProtocolParameter.GetXMLSchema() -> String
EDFProtocolParameter.ToXMLFile(ByVal bstrFileName As String)
EDFProtocolParameter.ToXMLString() -> String
EDFProtocolParametersCollection.Count : Long [R]
EDFProtocolParametersCollection.Add() -> EDFProtocolParameter
EDFProtocolParametersCollection.GetXMLSchema() -> String
EDFProtocolParametersCollection.Item(ByVal vtIndex As Variant) -> EDFProtocolParameter
EDFProtocolParametersCollection.ToXMLFile(ByVal bstrFileName As String)
EDFProtocolParametersCollection.ToXMLString() -> String
EDFProtocolsCollection.Count : Long [R]
EDFProtocolsCollection.Add() -> EDFProtocol
EDFProtocolsCollection.GetXMLSchema() -> String
EDFProtocolsCollection.Item(ByVal vtIndex As Variant) -> EDFProtocol
EDFProtocolsCollection.ToXMLFile(ByVal bstrFileName As String)
EDFProtocolsCollection.ToXMLString() -> String
EDFProtocolWithParameters.Code : ElectronicDocProtocolCodeStrEnum [R]
EDFProtocolWithParameters.Description : String [R/W]
EDFProtocolWithParameters.EDFProtocolParametersCollection : EDFProtocolParametersCollection [R]
EDFProtocolWithParameters.IsActive : BoYesNoEnum [R/W]
EDFProtocolWithParameters.FromXMLFile(ByVal bstrFileName As String)
EDFProtocolWithParameters.FromXMLString(ByVal bstrXML As String)
EDFProtocolWithParameters.GetXMLSchema() -> String
EDFProtocolWithParameters.ToXMLFile(ByVal bstrFileName As String)
EDFProtocolWithParameters.ToXMLString() -> String
ElectronicCommunicationActionService.ConfirmSuccessOfCommunication(ByVal pIECMCodeParams As ECMCodeParams)
ElectronicCommunicationActionService.GetAction(ByVal pIECMCodeParams As ECMCodeParams) -> ECMActionStatusData
ElectronicCommunicationActionService.GetDataInterface(ByVal enumMSDI As ElectronicCommunicationActionServiceDataInterfaces) -> Object
ElectronicCommunicationActionService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ElectronicCommunicationActionService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ElectronicCommunicationActionService.ReportErrorAndContinue(ByVal pIECMCodeParams As ECMCodeParams)
ElectronicCommunicationActionService.ReportErrorAndStop(ByVal pIECMCodeParams As ECMCodeParams)
ElectronicCommunicationActionService.UpdateAction(ByVal pActionStatusData As ECMActionStatusData)
ElectronicCommunicationActionsService.AddEcmAction(ByVal pIEcmAction As EcmAction) -> EcmAction
ElectronicCommunicationActionsService.AddEcmActionLog(ByVal pIEcmActionLog As EcmActionLog) -> EcmActionLog
ElectronicCommunicationActionsService.DeleteEcmAction(ByVal pIEcmAction As EcmAction)
ElectronicCommunicationActionsService.GetDataInterface(ByVal enumMSDI As ElectronicCommunicationActionsServiceDataInterfaces) -> Object
ElectronicCommunicationActionsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ElectronicCommunicationActionsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ElectronicCommunicationActionsService.GetEcmAction(ByVal pIEcmActionParams As EcmActionParams) -> EcmAction
ElectronicCommunicationActionsService.GetEcmActionByDoc(ByVal pIEcmActionDocParams As EcmActionDocParams) -> EcmAction
ElectronicCommunicationActionsService.GetEcmActionLog(ByVal pIEcmActionLogParams As EcmActionLogParams) -> EcmActionLog
ElectronicCommunicationActionsService.GetEcmActionLogList(ByVal pIEcmAction As EcmAction) -> EcmActionLogCollection
ElectronicCommunicationActionsService.UpdateEcmAction(ByVal pIEcmAction As EcmAction)
ElectronicDocumentService.AddImportEntry(ByVal pIEDFImportEntry As EDFImportEntry)
ElectronicDocumentService.AddLog(ByVal pIEDFEntryLogInputParams As EDFEntryAddLogInputParams)
ElectronicDocumentService.ExportEntryLog(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams)
ElectronicDocumentService.GetDataInterface(ByVal enumMSDI As ElectronicDocumentServiceDataInterfaces) -> Object
ElectronicDocumentService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ElectronicDocumentService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ElectronicDocumentService.GetDocMappingList(ByVal pIEDFDocMappingInputParams As EDFDocMappingInputParams) -> EDFDocMappingsCollection
ElectronicDocumentService.GetEntry(ByVal pIEDFEntryInputParams As EDFEntryInputParams) -> EDFEntry
ElectronicDocumentService.GetEntryList(ByVal pIEDFEntryListInputParams As EDFEntryListInputParams) -> EDFEntriesCollection
ElectronicDocumentService.GetLastLog(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams) -> EDFEntryLog
ElectronicDocumentService.GetLogs(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams) -> EDFEntryLogsCollection
ElectronicDocumentService.GetMappingByHash(ByVal pIEDFMappingInputParams As EDFMappingInputParams) -> EDFMapping
ElectronicDocumentService.GetProtocol(ByVal pIEDFProtocolInputParams As EDFProtocolInputParams) -> EDFProtocol
ElectronicDocumentService.GetProtocolParameters(ByVal pIEDFProtocolInputParams As EDFProtocolInputParams) -> EDFProtocolWithParameters
ElectronicDocumentService.GetProtocols() -> EDFProtocolsCollection
ElectronicDocumentService.UpdateEntry(ByVal pIEDFEntry As EDFEntry)
ElectronicFileFormat.Description : String [R]
ElectronicFileFormat.FormatID : Long [R]
ElectronicFileFormat.MenuName : String [R]
ElectronicFileFormat.MenuPath : String [R]
ElectronicFileFormat.Name : String [R]
ElectronicFileFormat.OutputFilePath : String [R]
ElectronicFileFormat.SchemaVersion : String [R]
ElectronicFileFormat.Version : String [R]
ElectronicFileFormat.FromXMLFile(ByVal bstrFileName As String)
ElectronicFileFormat.FromXMLString(ByVal bstrXML As String)
ElectronicFileFormat.GetXMLSchema() -> String
ElectronicFileFormat.ToXMLFile(ByVal bstrFileName As String)
ElectronicFileFormat.ToXMLString() -> String
ElectronicFileFormatParams.FormatID : Long [R/W]
ElectronicFileFormatParams.Name : String [R/W]
ElectronicFileFormatParams.FromXMLFile(ByVal bstrFileName As String)
ElectronicFileFormatParams.FromXMLString(ByVal bstrXML As String)
ElectronicFileFormatParams.GetXMLSchema() -> String
ElectronicFileFormatParams.ToXMLFile(ByVal bstrFileName As String)
ElectronicFileFormatParams.ToXMLString() -> String
ElectronicFileFormatsParams.Count : Long [R]
ElectronicFileFormatsParams.Add() -> ElectronicFileFormatParams
ElectronicFileFormatsParams.GetXMLSchema() -> String
ElectronicFileFormatsParams.Item(ByVal vtIndex As Variant) -> ElectronicFileFormatParams
ElectronicFileFormatsParams.ToXMLFile(ByVal bstrFileName As String)
ElectronicFileFormatsParams.ToXMLString() -> String
ElectronicFileFormatsService.AddElectronicFileFormat(ByVal pIImportFileParam As ImportFileParam) -> ElectronicFileFormatParams
ElectronicFileFormatsService.DeleteElectronicFileFormat(ByVal pIElectronicFileFormatParams As ElectronicFileFormatParams)
ElectronicFileFormatsService.GetDataInterface(ByVal enumMSDI As ElectronicFileFormatsServiceDataInterfaces) -> Object
ElectronicFileFormatsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ElectronicFileFormatsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ElectronicFileFormatsService.GetElectronicFileFormat(ByVal pIElectronicFileFormatParams As ElectronicFileFormatParams) -> ElectronicFileFormat
ElectronicFileFormatsService.GetElectronicFileFormatList() -> ElectronicFileFormatsParams
ElectronicProtocol.Confirmation : String [R/W]
ElectronicProtocol.EBooksInvoiceType : String [R/W]
ElectronicProtocol.EBooksInvoiceTypeofNegative : String [R/W]
ElectronicProtocol.EBooksMARK : String [R]
ElectronicProtocol.EBooksMARKofNegative : String [R]
ElectronicProtocol.EBooksRelevant : BoYesNoEnum [R/W]
ElectronicProtocol.EDocType : Long [R/W]
ElectronicProtocol.GenerationType : ElectronicDocGenTypeEnum [R/W]
ElectronicProtocol.MappingID : Long [R/W]
ElectronicProtocol.ProtocolCode : ElectronicDocProtocolCodeEnum [R/W]
ElectronicProtocol.RelatedDocuments : RelatedDocumentCollection [R]
ElectronicProtocol.TestingMode : BoYesNoEnum [R]
ElectronicProtocol.FromXMLFile(ByVal bstrFileName As String)
ElectronicProtocol.FromXMLString(ByVal bstrXML As String)
ElectronicProtocol.GetXMLSchema() -> String
ElectronicProtocol.ToXMLFile(ByVal bstrFileName As String)
ElectronicProtocol.ToXMLString() -> String
ElectronicProtocolCollection.Count : Long [R]
ElectronicProtocolCollection.Add() -> ElectronicProtocol
ElectronicProtocolCollection.GetXMLSchema() -> String
ElectronicProtocolCollection.Item(ByVal vtIndex As Variant) -> ElectronicProtocol
ElectronicProtocolCollection.ToXMLFile(ByVal bstrFileName As String)
ElectronicProtocolCollection.ToXMLString() -> String
ElectronicProtocols.Confirmation : String [R/W]
ElectronicProtocols.Count : Long [R]
ElectronicProtocols.EBillingIRN : String [R/W]
ElectronicProtocols.EBooksInvoiceType : String [R/W]
ElectronicProtocols.EBooksInvoiceTypeofNegative : String [R/W]
ElectronicProtocols.EBooksMARK : String [R]
ElectronicProtocols.EBooksMARKofNegative : String [R]
ElectronicProtocols.EBooksRelevant : BoYesNoEnum [R/W]
ElectronicProtocols.EDocType : Long [R/W]
ElectronicProtocols.EETBKP : String [R/W]
ElectronicProtocols.EETPKP : String [R/W]
ElectronicProtocols.FechaTimbrado : String [R]
ElectronicProtocols.FPAProgressivo : String [R]
ElectronicProtocols.FPASendDateSDI : Date [R]
ElectronicProtocols.FPASequenceNumber : Long [R]
ElectronicProtocols.GenerationType : ElectronicDocGenTypeEnum [R/W]
ElectronicProtocols.MappingID : Long [R/W]
ElectronicProtocols.NoCertificadoSAT : String [R]
ElectronicProtocols.PaymentMethod : String [R]
ElectronicProtocols.ProtocolCode : ElectronicDocProtocolCodeEnum [R/W]
ElectronicProtocols.ProtocolDescription : String [R]
ElectronicProtocols.RelatedDocuments : RelatedDocuments [R]
ElectronicProtocols.RfcProvCertif : String [R]
ElectronicProtocols.SelloSAT : String [R]
ElectronicProtocols.SignatureDigest : String [R]
ElectronicProtocols.SignatureInputMessage : String [R]
ElectronicProtocols.TestingMode : BoYesNoEnum [R]
ElectronicProtocols.Add()
ElectronicProtocols.Delete()
ElectronicProtocols.SetCurrentLine(ByVal LineNum As Long)
ElectronicReportInfo.CompanyType : String [R/W]
ElectronicReportInfo.ShareCapitalAmount : Double [R/W]
ElectronicSeries.ApprovalNumber : Long [R/W]
ElectronicSeries.ApprovalYear : Long [R/W]
ElectronicSeries.ElectronicSeries : Long [R]
ElectronicSeries.InitialNumber : String [R/W]
ElectronicSeries.LastNumber : String [R/W]
ElectronicSeries.Name : String [R/W]
ElectronicSeries.NextNumber : String [R]
ElectronicSeries.Prefix : String [R/W]
ElectronicSeries.Remarks : String [R/W]
ElectronicSeries.Series : Long [R/W]
ElectronicSeries.FromXMLFile(ByVal bstrFileName As String)
ElectronicSeries.FromXMLString(ByVal bstrXML As String)
ElectronicSeries.GetXMLSchema() -> String
ElectronicSeries.ToXMLFile(ByVal bstrFileName As String)
ElectronicSeries.ToXMLString() -> String
ElectronicSeriesCollection.Count : Long [R]
ElectronicSeriesCollection.Add() -> ElectronicSeries
ElectronicSeriesCollection.GetXMLSchema() -> String
ElectronicSeriesCollection.Item(ByVal vtIndex As Variant) -> ElectronicSeries
ElectronicSeriesCollection.ToXMLFile(ByVal bstrFileName As String)
ElectronicSeriesCollection.ToXMLString() -> String
ElectronicSeriesParams.ElectronicSeries : Long [R/W]
ElectronicSeriesParams.FromXMLFile(ByVal bstrFileName As String)
ElectronicSeriesParams.FromXMLString(ByVal bstrXML As String)
ElectronicSeriesParams.GetXMLSchema() -> String
ElectronicSeriesParams.ToXMLFile(ByVal bstrFileName As String)
ElectronicSeriesParams.ToXMLString() -> String
EmailGroup.EmailGroupCode : String [R/W]
EmailGroup.EmailGroupName : String [R/W]
EmailGroup.FromXMLFile(ByVal bstrFileName As String)
EmailGroup.FromXMLString(ByVal bstrXML As String)
EmailGroup.GetXMLSchema() -> String
EmailGroup.ToXMLFile(ByVal bstrFileName As String)
EmailGroup.ToXMLString() -> String
EmailGroupParams.EmailGroupCode : String [R/W]
EmailGroupParams.EmailGroupName : String [R]
EmailGroupParams.FromXMLFile(ByVal bstrFileName As String)
EmailGroupParams.FromXMLString(ByVal bstrXML As String)
EmailGroupParams.GetXMLSchema() -> String
EmailGroupParams.ToXMLFile(ByVal bstrFileName As String)
EmailGroupParams.ToXMLString() -> String
EmailGroupParamsCollection.Count : Long [R]
EmailGroupParamsCollection.Add() -> EmailGroupParams
EmailGroupParamsCollection.GetXMLSchema() -> String
EmailGroupParamsCollection.Item(ByVal vtIndex As Variant) -> EmailGroupParams
EmailGroupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
EmailGroupParamsCollection.ToXMLString() -> String
EmailGroupsService.Add(ByVal pIEmailGroup As EmailGroup) -> EmailGroupParams
EmailGroupsService.Delete(ByVal pIEmailGroupParams As EmailGroupParams)
EmailGroupsService.Get(ByVal pIEmailGroupParams As EmailGroupParams) -> EmailGroup
EmailGroupsService.GetDataInterface(ByVal enumMSDI As EmailGroupsServiceDataInterfaces) -> Object
EmailGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EmailGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EmailGroupsService.GetList() -> EmailGroupParamsCollection
EmailGroupsService.Update(ByVal pIEmailGroup As EmailGroup)
EmployeeAbsenceInfo.ApprovedBy : String [R/W]
EmployeeAbsenceInfo.ConfirmerNumber : Long [R/W]
EmployeeAbsenceInfo.Count : Long [R]
EmployeeAbsenceInfo.EmployeeID : Long [R/W]
EmployeeAbsenceInfo.FromDate : Date [R/W]
EmployeeAbsenceInfo.LineNum : Long [R]
EmployeeAbsenceInfo.Reason : String [R/W]
EmployeeAbsenceInfo.ToDate : Date [R/W]
EmployeeAbsenceInfo.UserFields : UserFields [R]
EmployeeAbsenceInfo.Add()
EmployeeAbsenceInfo.SetCurrentLine(ByVal LineNum As Long)
EmployeeBranchAssignment.BPLID : Long [R/W]
EmployeeBranchAssignment.Count : Long [R]
EmployeeBranchAssignment.EmployeeID : Long [R]
EmployeeBranchAssignment.Add()
EmployeeBranchAssignment.Delete()
EmployeeBranchAssignment.SetCurrentLine(ByVal LineNum As Long)
EmployeeEducationInfo.Count : Long [R]
EmployeeEducationInfo.Diploma : String [R/W]
EmployeeEducationInfo.EducationType : Long [R/W]
EmployeeEducationInfo.EmployeeNo : Long [R/W]
EmployeeEducationInfo.FromDate : Date [R/W]
EmployeeEducationInfo.Institute : String [R/W]
EmployeeEducationInfo.LineNum : Long [R]
EmployeeEducationInfo.Major : String [R/W]
EmployeeEducationInfo.ToDate : Date [R/W]
EmployeeEducationInfo.UserFields : UserFields [R]
EmployeeEducationInfo.Add()
EmployeeEducationInfo.SetCurrentLine(ByVal LineNum As Long)
EmployeeFullNamesParams.EmployeeFullName : String [R/W]
EmployeeFullNamesParams.EmployeeID : Long [R/W]
EmployeeFullNamesParamsCollection.Count : Long [R]
EmployeeFullNamesParamsCollection.Add() -> EmployeeFullNamesParams
EmployeeFullNamesParamsCollection.GetXMLSchema() -> String
EmployeeFullNamesParamsCollection.Item(ByVal vtIndex As Variant) -> EmployeeFullNamesParams
EmployeeFullNamesParamsCollection.ToXMLFile(ByVal bstrFileName As String)
EmployeeFullNamesParamsCollection.ToXMLString() -> String
EmployeeIDType.IDType : String [R/W]
EmployeeIDType.FromXMLFile(ByVal bstrFileName As String)
EmployeeIDType.FromXMLString(ByVal bstrXML As String)
EmployeeIDType.GetXMLSchema() -> String
EmployeeIDType.ToXMLFile(ByVal bstrFileName As String)
EmployeeIDType.ToXMLString() -> String
EmployeeIDTypeParams.IDType : String [R/W]
EmployeeIDTypeParams.FromXMLFile(ByVal bstrFileName As String)
EmployeeIDTypeParams.FromXMLString(ByVal bstrXML As String)
EmployeeIDTypeParams.GetXMLSchema() -> String
EmployeeIDTypeParams.ToXMLFile(ByVal bstrFileName As String)
EmployeeIDTypeParams.ToXMLString() -> String
EmployeeIDTypeParamsCollection.Count : Long [R]
EmployeeIDTypeParamsCollection.Add() -> EmployeeIDTypeParams
EmployeeIDTypeParamsCollection.GetXMLSchema() -> String
EmployeeIDTypeParamsCollection.Item(ByVal vtIndex As Variant) -> EmployeeIDTypeParams
EmployeeIDTypeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
EmployeeIDTypeParamsCollection.ToXMLString() -> String
EmployeeIDTypeService.Add(ByVal pIEmployeeIDType As EmployeeIDType) -> EmployeeIDTypeParams
EmployeeIDTypeService.Delete(ByVal pIEmployeeIDTypeParams As EmployeeIDTypeParams)
EmployeeIDTypeService.Get(ByVal pIEmployeeIDTypeParams As EmployeeIDTypeParams) -> EmployeeIDType
EmployeeIDTypeService.GetDataInterface(ByVal enumMSDI As EmployeeIDTypeServiceDataInterfaces) -> Object
EmployeeIDTypeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EmployeeIDTypeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EmployeeIDTypeService.GetList() -> EmployeeIDTypeParamsCollection
EmployeeIDTypeService.Update(ByVal pIEmployeeIDType As EmployeeIDType)
EmployeePosition.Description : String [R/W]
EmployeePosition.Name : String [R/W]
EmployeePosition.PositionID : Long [R]
EmployeePosition.FromXMLFile(ByVal bstrFileName As String)
EmployeePosition.FromXMLString(ByVal bstrXML As String)
EmployeePosition.GetXMLSchema() -> String
EmployeePosition.ToXMLFile(ByVal bstrFileName As String)
EmployeePosition.ToXMLString() -> String
EmployeePositionParams.Description : String [R]
EmployeePositionParams.Name : String [R]
EmployeePositionParams.PositionID : Long [R/W]
EmployeePositionParams.FromXMLFile(ByVal bstrFileName As String)
EmployeePositionParams.FromXMLString(ByVal bstrXML As String)
EmployeePositionParams.GetXMLSchema() -> String
EmployeePositionParams.ToXMLFile(ByVal bstrFileName As String)
EmployeePositionParams.ToXMLString() -> String
EmployeePositionParamsCollection.Count : Long [R]
EmployeePositionParamsCollection.Add() -> EmployeePositionParams
EmployeePositionParamsCollection.GetXMLSchema() -> String
EmployeePositionParamsCollection.Item(ByVal vtIndex As Variant) -> EmployeePositionParams
EmployeePositionParamsCollection.ToXMLFile(ByVal bstrFileName As String)
EmployeePositionParamsCollection.ToXMLString() -> String
EmployeePositionService.Add(ByVal pIEmployeePosition As EmployeePosition) -> EmployeePositionParams
EmployeePositionService.Delete(ByVal pIEmployeePositionParams As EmployeePositionParams)
EmployeePositionService.Get(ByVal pIEmployeePositionParams As EmployeePositionParams) -> EmployeePosition
EmployeePositionService.GetDataInterface(ByVal enumMSDI As EmployeePositionServiceDataInterfaces) -> Object
EmployeePositionService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EmployeePositionService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EmployeePositionService.GetList() -> EmployeePositionParamsCollection
EmployeePositionService.Update(ByVal pIEmployeePosition As EmployeePosition)
EmployeePrevEmpoymentInfo.Count : Long [R]
EmployeePrevEmpoymentInfo.EmployeeNo : Long [R/W]
EmployeePrevEmpoymentInfo.Employer : String [R/W]
EmployeePrevEmpoymentInfo.FromDtae : Date [R/W]
EmployeePrevEmpoymentInfo.LineNum : Long [R]
EmployeePrevEmpoymentInfo.Position : String [R/W]
EmployeePrevEmpoymentInfo.Remarks : String [R/W]
EmployeePrevEmpoymentInfo.ToDate : Date [R/W]
EmployeePrevEmpoymentInfo.UserFields : UserFields [R]
EmployeePrevEmpoymentInfo.Add()
EmployeePrevEmpoymentInfo.SetCurrentLine(ByVal LineNum As Long)
EmployeeReviewsInfo.Count : Long [R]
EmployeeReviewsInfo.Date : Date [R/W]
EmployeeReviewsInfo.EmployeeNo : Long [R/W]
EmployeeReviewsInfo.Grade : String [R/W]
EmployeeReviewsInfo.LineNum : Long [R]
EmployeeReviewsInfo.Manager : Long [R/W]
EmployeeReviewsInfo.Remarks : String [R/W]
EmployeeReviewsInfo.ReviewDescription : String [R/W]
EmployeeReviewsInfo.UserFields : UserFields [R]
EmployeeReviewsInfo.Add()
EmployeeReviewsInfo.SetCurrentLine(ByVal LineNum As Long)
EmployeeRoleSetup.Description : String [R/W]
EmployeeRoleSetup.Name : String [R/W]
EmployeeRoleSetup.TypeID : Long [R]
EmployeeRoleSetup.FromXMLFile(ByVal bstrFileName As String)
EmployeeRoleSetup.FromXMLString(ByVal bstrXML As String)
EmployeeRoleSetup.GetXMLSchema() -> String
EmployeeRoleSetup.ToXMLFile(ByVal bstrFileName As String)
EmployeeRoleSetup.ToXMLString() -> String
EmployeeRoleSetupParams.Name : String [R]
EmployeeRoleSetupParams.TypeID : Long [R/W]
EmployeeRoleSetupParams.FromXMLFile(ByVal bstrFileName As String)
EmployeeRoleSetupParams.FromXMLString(ByVal bstrXML As String)
EmployeeRoleSetupParams.GetXMLSchema() -> String
EmployeeRoleSetupParams.ToXMLFile(ByVal bstrFileName As String)
EmployeeRoleSetupParams.ToXMLString() -> String
EmployeeRoleSetupParamsCollection.Count : Long [R]
EmployeeRoleSetupParamsCollection.Add() -> EmployeeRoleSetupParams
EmployeeRoleSetupParamsCollection.GetXMLSchema() -> String
EmployeeRoleSetupParamsCollection.Item(ByVal vtIndex As Variant) -> EmployeeRoleSetupParams
EmployeeRoleSetupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
EmployeeRoleSetupParamsCollection.ToXMLString() -> String
EmployeeRolesInfo.Count : Long [R]
EmployeeRolesInfo.EmployeeID : Long [R/W]
EmployeeRolesInfo.LineNum : Long [R]
EmployeeRolesInfo.RoleID : Long [R/W]
EmployeeRolesInfo.UserFields : UserFields [R]
EmployeeRolesInfo.Add()
EmployeeRolesInfo.SetCurrentLine(ByVal LineNum As Long)
EmployeeRolesSetupService.AddEmployeeRoleSetup(ByVal pIEmployeeRoleSetup As EmployeeRoleSetup) -> EmployeeRoleSetupParams
EmployeeRolesSetupService.DeleteEmployeeRoleSetup(ByVal pIEmployeeRoleSetupParams As EmployeeRoleSetupParams)
EmployeeRolesSetupService.GetDataInterface(ByVal enumMSDI As EmployeeRolesSetupServiceDataInterfaces) -> Object
EmployeeRolesSetupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EmployeeRolesSetupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EmployeeRolesSetupService.GetEmployeeRoleSetup(ByVal pIEmployeeRoleSetupParams As EmployeeRoleSetupParams) -> EmployeeRoleSetup
EmployeeRolesSetupService.GetEmployeeRoleSetupList() -> EmployeeRoleSetupParamsCollection
EmployeeRolesSetupService.UpdateEmployeeRoleSetup(ByVal pIEmployeeRoleSetup As EmployeeRoleSetup)
EmployeeSavingsPaymentInfo.AG : String [R/W]
EmployeeSavingsPaymentInfo.AGcurrency : String [R/W]
EmployeeSavingsPaymentInfo.AN : String [R/W]
EmployeeSavingsPaymentInfo.ANcurrency : String [R/W]
EmployeeSavingsPaymentInfo.BankAccount : String [R/W]
EmployeeSavingsPaymentInfo.BankCode : String [R/W]
EmployeeSavingsPaymentInfo.BankName : String [R/W]
EmployeeSavingsPaymentInfo.ContractName : String [R/W]
EmployeeSavingsPaymentInfo.Count : Long [R]
EmployeeSavingsPaymentInfo.EmployeeID : Long [R/W]
EmployeeSavingsPaymentInfo.LineNum : Long [R]
EmployeeSavingsPaymentInfo.PaymentNotes : String [R/W]
EmployeeSavingsPaymentInfo.Sequence : ContractSequenceEnum [R/W]
EmployeeSavingsPaymentInfo.UserFields : UserFields [R]
EmployeeSavingsPaymentInfo.Add()
EmployeeSavingsPaymentInfo.SetCurrentLine(ByVal LineNum As Long)
EmployeesInfo.AbsenceInfo : EmployeeAbsenceInfo [R]
EmployeesInfo.AccountantResponsible : BoYesNoEnum [R/W]
EmployeesInfo.Active : BoYesNoEnum [R/W]
EmployeesInfo.AdditionalAmount : Double [R/W]
EmployeesInfo.AdditionalCurrency : String [R/W]
EmployeesInfo.AdditionalUnit : EmployeeExemptionUnitEnum [R/W]
EmployeesInfo.ApplicationUserID : Long [R/W]
EmployeesInfo.AttachmentEntry : Long [R/W]
EmployeesInfo.Attachments : Attachments [R]
EmployeesInfo.AuthorizationForRetrieveFromSEFAZ : BoYesNoEnum [R/W]
EmployeesInfo.BankAccount : String [R/W]
EmployeesInfo.BankBranch : String [R/W]
EmployeesInfo.BankBranchNum : String [R/W]
EmployeesInfo.BankCode : String [R/W]
EmployeesInfo.BankCodeForDATEV : String [R/W]
EmployeesInfo.BirthPlace : String [R/W]
EmployeesInfo.BPLID : Long [R/W]
EmployeesInfo.Branch : Long [R/W]
EmployeesInfo.Browser : DataBrowser [R]
EmployeesInfo.CitizenshipCountryCode : String [R/W]
EmployeesInfo.CompanyNumber : String [R/W]
EmployeesInfo.CostCenterCode : String [R/W]
EmployeesInfo.CountryOfBirth : String [R/W]
EmployeesInfo.CPF : String [R/W]
EmployeesInfo.CRCNumber : String [R/W]
EmployeesInfo.CRCState : String [R/W]
EmployeesInfo.CreateDate : Date [R]
EmployeesInfo.CreateTime : Date [R]
EmployeesInfo.DateOfBirth : Date [R/W]
EmployeesInfo.Department : Long [R/W]
EmployeesInfo.DeviatingBankAccountOwner : BoYesNoEnum [R/W]
EmployeesInfo.DIRFResponsible : BoYesNoEnum [R/W]
EmployeesInfo.EducationInfo : EmployeeEducationInfo [R]
EmployeesInfo.EducationStatus : String [R/W]
EmployeesInfo.eMail : String [R/W]
EmployeesInfo.EmployeeBranchAssignment : EmployeeBranchAssignment [R]
EmployeesInfo.EmployeeCode : String [R/W]
EmployeesInfo.EmployeeCosts : Double [R/W]
EmployeesInfo.EmployeeCostsCurrency : String [R/W]
EmployeesInfo.EmployeeCostUnit : BoSalaryCostUnits [R/W]
EmployeesInfo.EmployeeID : Long [R]
EmployeesInfo.EmployeeRolesInfo : EmployeeRolesInfo [R]
EmployeesInfo.EmployeeType : Long [R/W]
EmployeesInfo.ExemptionAmount : Double [R/W]
EmployeesInfo.ExemptionCurrency : String [R/W]
EmployeesInfo.ExemptionUnit : EmployeeExemptionUnitEnum [R/W]
EmployeesInfo.ExternalEmployeeNumber : String [R/W]
EmployeesInfo.Fax : String [R/W]
EmployeesInfo.FirstName : String [R/W]
EmployeesInfo.Gender : BoGenderTypes [R/W]
EmployeesInfo.HealthInsuranceCode : String [R/W]
EmployeesInfo.HealthInsuranceName : String [R/W]
EmployeesInfo.HealthInsuranceType : String [R/W]
EmployeesInfo.HomeBlock : String [R/W]
EmployeesInfo.HomeBuildingFloorRoom : String [R/W]
EmployeesInfo.HomeCity : String [R/W]
EmployeesInfo.HomeCountry : String [R/W]
EmployeesInfo.HomeCounty : String [R/W]
EmployeesInfo.HomePhone : String [R/W]
EmployeesInfo.HomeState : String [R/W]
EmployeesInfo.HomeStreet : String [R/W]
EmployeesInfo.HomeStreetNumber : String [R/W]
EmployeesInfo.HomeZipCode : String [R/W]
EmployeesInfo.IdNumber : String [R/W]
EmployeesInfo.IDType : String [R/W]
EmployeesInfo.IncomeTaxLiability : String [R/W]
EmployeesInfo.JobTitle : String [R/W]
EmployeesInfo.JobTitleCode : String [R/W]
EmployeesInfo.LastName : String [R/W]
EmployeesInfo.LegalRepresentative : BoYesNoEnum [R/W]
EmployeesInfo.LinkedVendor : String [R/W]
EmployeesInfo.Manager : Long [R/W]
EmployeesInfo.MartialStatus : BoMeritalStatuses [R/W]
EmployeesInfo.MiddleName : String [R/W]
EmployeesInfo.MobilePhone : String [R/W]
EmployeesInfo.MunicipalityKey : String [R/W]
EmployeesInfo.NumOfChildren : Long [R/W]
EmployeesInfo.OfficeExtension : String [R/W]
EmployeesInfo.OfficePhone : String [R/W]
EmployeesInfo.Pager : String [R/W]
EmployeesInfo.PartnerReligion : String [R/W]
EmployeesInfo.PassportExpirationDate : Date [R/W]
EmployeesInfo.PassportIssueDate : Date [R/W]
EmployeesInfo.PassportIssuer : String [R/W]
EmployeesInfo.PassportNumber : String [R/W]
EmployeesInfo.PaymentMethod : EmployeePaymentMethodEnum [R/W]
EmployeesInfo.PersonGroup : String [R/W]
EmployeesInfo.Picture : String [R/W]
EmployeesInfo.Position : Long [R/W]
EmployeesInfo.PreviousEmpoymentInfo : EmployeePrevEmpoymentInfo [R]
EmployeesInfo.PreviousPRWebAccess : BoYesNoEnum [R]
EmployeesInfo.ProfessionStatus : String [R/W]
EmployeesInfo.PRWebAccess : BoYesNoEnum [R/W]
EmployeesInfo.QualificationCode : SPEDContabilQualificationCodeEnum [R/W]
EmployeesInfo.Religion : String [R/W]
EmployeesInfo.Remarks : String [R/W]
EmployeesInfo.ReviewsInfo : EmployeeReviewsInfo [R]
EmployeesInfo.Salary : Double [R/W]
EmployeesInfo.SalaryCurrency : String [R/W]
EmployeesInfo.SalaryUnit : BoSalaryCostUnits [R/W]
EmployeesInfo.SalesPersonCode : Long [R/W]
EmployeesInfo.SavingsPaymentInfo : EmployeeSavingsPaymentInfo [R]
EmployeesInfo.SocialInsuranceNumber : String [R/W]
EmployeesInfo.SpouseFirstName : String [R/W]
EmployeesInfo.SpouseSurname : String [R/W]
EmployeesInfo.StartDate : Date [R/W]
EmployeesInfo.StatusCode : Long [R/W]
EmployeesInfo.STDCode : Long [R/W]
EmployeesInfo.TaxClass : String [R/W]
EmployeesInfo.TaxOfficeName : String [R/W]
EmployeesInfo.TaxOfficeNumber : String [R/W]
EmployeesInfo.TerminationDate : Date [R/W]
EmployeesInfo.TreminationReason : Long [R/W]
EmployeesInfo.UpdateDate : Date [R]
EmployeesInfo.UpdateTime : Date [R]
EmployeesInfo.UserFields : UserFields [R]
EmployeesInfo.VacationCurrentYear : Long [R/W]
EmployeesInfo.VacationPreviousYear : Long [R/W]
EmployeesInfo.WorkBlock : String [R/W]
EmployeesInfo.WorkBuildingFloorRoom : String [R/W]
EmployeesInfo.WorkCity : String [R/W]
EmployeesInfo.WorkCountryCode : String [R/W]
EmployeesInfo.WorkCounty : String [R/W]
EmployeesInfo.WorkStateCode : String [R/W]
EmployeesInfo.WorkStreet : String [R/W]
EmployeesInfo.WorkStreetNumber : String [R/W]
EmployeesInfo.WorkZipCode : String [R/W]
EmployeesInfo.Add() -> Long
EmployeesInfo.Close() -> Long
EmployeesInfo.GetAsXML() -> String
EmployeesInfo.GetByKey(ByVal EmployeeID As Long) -> Boolean
EmployeesInfo.Remove() -> Long
EmployeesInfo.SaveToFile(ByVal FileName As String)
EmployeesInfo.SaveXML(ByRef FileName As String)
EmployeesInfo.Update() -> Long
EmployeeStatus.Description : String [R/W]
EmployeeStatus.Name : String [R/W]
EmployeeStatus.StatusId : Long [R]
EmployeeStatus.FromXMLFile(ByVal bstrFileName As String)
EmployeeStatus.FromXMLString(ByVal bstrXML As String)
EmployeeStatus.GetXMLSchema() -> String
EmployeeStatus.ToXMLFile(ByVal bstrFileName As String)
EmployeeStatus.ToXMLString() -> String
EmployeeStatusParams.Description : String [R]
EmployeeStatusParams.Name : String [R]
EmployeeStatusParams.StatusId : Long [R/W]
EmployeeStatusParams.FromXMLFile(ByVal bstrFileName As String)
EmployeeStatusParams.FromXMLString(ByVal bstrXML As String)
EmployeeStatusParams.GetXMLSchema() -> String
EmployeeStatusParams.ToXMLFile(ByVal bstrFileName As String)
EmployeeStatusParams.ToXMLString() -> String
EmployeeStatusParamsCollection.Count : Long [R]
EmployeeStatusParamsCollection.Add() -> EmployeeStatusParams
EmployeeStatusParamsCollection.GetXMLSchema() -> String
EmployeeStatusParamsCollection.Item(ByVal vtIndex As Variant) -> EmployeeStatusParams
EmployeeStatusParamsCollection.ToXMLFile(ByVal bstrFileName As String)
EmployeeStatusParamsCollection.ToXMLString() -> String
EmployeeStatusService.Add(ByVal pIEmployeeStatus As EmployeeStatus) -> EmployeeStatusParams
EmployeeStatusService.Delete(ByVal pIEmployeeStatusParams As EmployeeStatusParams)
EmployeeStatusService.Get(ByVal pIEmployeeStatusParams As EmployeeStatusParams) -> EmployeeStatus
EmployeeStatusService.GetDataInterface(ByVal enumMSDI As EmployeeStatusServiceDataInterfaces) -> Object
EmployeeStatusService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EmployeeStatusService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EmployeeStatusService.GetList() -> EmployeeStatusParamsCollection
EmployeeStatusService.Update(ByVal pIEmployeeStatus As EmployeeStatus)
EmployeeTransfer.Comment : String [R/W]
EmployeeTransfer.EmployeeTransferDetails : EmployeeTransferDetails [R]
EmployeeTransfer.Status : EmployeeTransferStatusEnum [R/W]
EmployeeTransfer.TransEndDate : Date [R/W]
EmployeeTransfer.TransEndTime : Date [R/W]
EmployeeTransfer.TransferID : Long [R/W]
EmployeeTransfer.TransStartDate : Date [R/W]
EmployeeTransfer.TransStartTime : Date [R/W]
EmployeeTransfer.FromXMLFile(ByVal bstrFileName As String)
EmployeeTransfer.FromXMLString(ByVal bstrXML As String)
EmployeeTransfer.GetXMLSchema() -> String
EmployeeTransfer.ToXMLFile(ByVal bstrFileName As String)
EmployeeTransfer.ToXMLString() -> String
EmployeeTransferDetail.Comment : String [R/W]
EmployeeTransferDetail.EmployeeID : Long [R/W]
EmployeeTransferDetail.Status : EmployeeTransferProcessingStatusEnum [R/W]
EmployeeTransferDetail.TransferedDate : Date [R/W]
EmployeeTransferDetail.TransferedTime : Date [R/W]
EmployeeTransferDetail.TransferID : Long [R]
EmployeeTransferDetail.FromXMLFile(ByVal bstrFileName As String)
EmployeeTransferDetail.FromXMLString(ByVal bstrXML As String)
EmployeeTransferDetail.GetXMLSchema() -> String
EmployeeTransferDetail.ToXMLFile(ByVal bstrFileName As String)
EmployeeTransferDetail.ToXMLString() -> String
EmployeeTransferDetails.Count : Long [R]
EmployeeTransferDetails.Add() -> EmployeeTransferDetail
EmployeeTransferDetails.GetXMLSchema() -> String
EmployeeTransferDetails.Item(ByVal vtIndex As Variant) -> EmployeeTransferDetail
EmployeeTransferDetails.ToXMLFile(ByVal bstrFileName As String)
EmployeeTransferDetails.ToXMLString() -> String
EmployeeTransferParams.TransferID : Long [R/W]
EmployeeTransferParams.FromXMLFile(ByVal bstrFileName As String)
EmployeeTransferParams.FromXMLString(ByVal bstrXML As String)
EmployeeTransferParams.GetXMLSchema() -> String
EmployeeTransferParams.ToXMLFile(ByVal bstrFileName As String)
EmployeeTransferParams.ToXMLString() -> String
EmployeeTransfersParams.Count : Long [R]
EmployeeTransfersParams.Add() -> EmployeeTransferParams
EmployeeTransfersParams.GetXMLSchema() -> String
EmployeeTransfersParams.Item(ByVal vtIndex As Variant) -> EmployeeTransferParams
EmployeeTransfersParams.ToXMLFile(ByVal bstrFileName As String)
EmployeeTransfersParams.ToXMLString() -> String
EmployeeTransfersService.AddEmployeeTransfer(ByVal pIEmployeeTransfer As EmployeeTransfer) -> EmployeeTransferParams
EmployeeTransfersService.DeleteEmployeeTransfer(ByVal pIEmployeeTransferParams As EmployeeTransferParams)
EmployeeTransfersService.GetDataInterface(ByVal enumMSDI As EmployeeTransfersServiceDataInterfaces) -> Object
EmployeeTransfersService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EmployeeTransfersService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EmployeeTransfersService.GetEmployeeTransfer(ByVal pIEmployeeTransferParams As EmployeeTransferParams) -> EmployeeTransfer
EmployeeTransfersService.GetEmployeeTransferList() -> EmployeeTransfersParams
EmployeeTransfersService.UpdateEmployeeTransfer(ByVal pIEmployeeTransfer As EmployeeTransfer)
EmploymentCategory.Code : String [R/W]
EmploymentCategory.Description : String [R/W]
EmploymentCategory.FromXMLFile(ByVal bstrFileName As String)
EmploymentCategory.FromXMLString(ByVal bstrXML As String)
EmploymentCategory.GetXMLSchema() -> String
EmploymentCategory.ToXMLFile(ByVal bstrFileName As String)
EmploymentCategory.ToXMLString() -> String
EmploymentCategoryParams.Code : String [R/W]
EmploymentCategoryParams.FromXMLFile(ByVal bstrFileName As String)
EmploymentCategoryParams.FromXMLString(ByVal bstrXML As String)
EmploymentCategoryParams.GetXMLSchema() -> String
EmploymentCategoryParams.ToXMLFile(ByVal bstrFileName As String)
EmploymentCategoryParams.ToXMLString() -> String
EmploymentCategoryService.AddEmploymentCategory(ByVal pIEmploymentCategory As EmploymentCategory) -> EmploymentCategoryParams
EmploymentCategoryService.GetDataInterface(ByVal enumMSDI As EmploymentCategoryServiceDataInterfaces) -> Object
EmploymentCategoryService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EmploymentCategoryService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EmploymentCategoryService.GetEmploymentCategory(ByVal pIEmploymentCategoryParams As EmploymentCategoryParams) -> EmploymentCategory
EmploymentCategoryService.GetEmploymentCategoryList() -> EmploymentCategorysParams
EmploymentCategoryService.UpdateEmploymentCategory(ByVal pIEmploymentCategory As EmploymentCategory)
EmploymentCategorysParams.Count : Long [R]
EmploymentCategorysParams.Add() -> EmploymentCategoryParams
EmploymentCategorysParams.GetXMLSchema() -> String
EmploymentCategorysParams.Item(ByVal vtIndex As Variant) -> EmploymentCategoryParams
EmploymentCategorysParams.ToXMLFile(ByVal bstrFileName As String)
EmploymentCategorysParams.ToXMLString() -> String
EnhancedDiscountGroup.AbsEntry : Long [R]
EnhancedDiscountGroup.Active : BoYesNoEnum [R/W]
EnhancedDiscountGroup.DiscountGroupLineCollection : DiscountGroupLineCollection [R]
EnhancedDiscountGroup.DiscountRelations : DiscountGroupRelationsEnum [R/W]
EnhancedDiscountGroup.ObjectCode : String [R/W]
EnhancedDiscountGroup.Type : DiscountGroupTypeEnum [R/W]
EnhancedDiscountGroup.ValidFrom : Date [R/W]
EnhancedDiscountGroup.ValidTo : Date [R/W]
EnhancedDiscountGroup.FromXMLFile(ByVal bstrFileName As String)
EnhancedDiscountGroup.FromXMLString(ByVal bstrXML As String)
EnhancedDiscountGroup.GetXMLSchema() -> String
EnhancedDiscountGroup.ToXMLFile(ByVal bstrFileName As String)
EnhancedDiscountGroup.ToXMLString() -> String
EnhancedDiscountGroupCollectionParams.Count : Long [R]
EnhancedDiscountGroupCollectionParams.Add() -> EnhancedDiscountGroupParams
EnhancedDiscountGroupCollectionParams.GetXMLSchema() -> String
EnhancedDiscountGroupCollectionParams.Item(ByVal vtIndex As Variant) -> EnhancedDiscountGroupParams
EnhancedDiscountGroupCollectionParams.ToXMLFile(ByVal bstrFileName As String)
EnhancedDiscountGroupCollectionParams.ToXMLString() -> String
EnhancedDiscountGroupParams.AbsEntry : Long [R/W]
EnhancedDiscountGroupParams.ObjectCode : String [R]
EnhancedDiscountGroupParams.Type : DiscountGroupTypeEnum [R]
EnhancedDiscountGroupParams.FromXMLFile(ByVal bstrFileName As String)
EnhancedDiscountGroupParams.FromXMLString(ByVal bstrXML As String)
EnhancedDiscountGroupParams.GetXMLSchema() -> String
EnhancedDiscountGroupParams.ToXMLFile(ByVal bstrFileName As String)
EnhancedDiscountGroupParams.ToXMLString() -> String
EnhancedDiscountGroupsService.Add(ByVal pIEnhancedDiscountGroup As EnhancedDiscountGroup) -> EnhancedDiscountGroupParams
EnhancedDiscountGroupsService.Delete(ByVal pIEnhancedDiscountGroupParams As EnhancedDiscountGroupParams)
EnhancedDiscountGroupsService.Get(ByVal pIEnhancedDiscountGroupParams As EnhancedDiscountGroupParams) -> EnhancedDiscountGroup
EnhancedDiscountGroupsService.GetDataInterface(ByVal enumMSDI As EnhancedDiscountGroupsServiceDataInterfaces) -> Object
EnhancedDiscountGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EnhancedDiscountGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EnhancedDiscountGroupsService.GetList() -> EnhancedDiscountGroupCollectionParams
EnhancedDiscountGroupsService.Update(ByVal pIEnhancedDiscountGroup As EnhancedDiscountGroup)
EWBTransporter.AbsEntry : Long [R]
EWBTransporter.EWBTransporter_Lines : EWBTransporter_Lines [R]
EWBTransporter.TransporterCode : String [R/W]
EWBTransporter.TransporterID : String [R/W]
EWBTransporter.TransporterName : String [R/W]
EWBTransporter.FromXMLFile(ByVal bstrFileName As String)
EWBTransporter.FromXMLString(ByVal bstrXML As String)
EWBTransporter.GetXMLSchema() -> String
EWBTransporter.ToXMLFile(ByVal bstrFileName As String)
EWBTransporter.ToXMLString() -> String
EWBTransporter_Line.AbsEntry : Long [R]
EWBTransporter_Line.LineNumber : Long [R]
EWBTransporter_Line.Mode : Long [R/W]
EWBTransporter_Line.VehicleNo : String [R/W]
EWBTransporter_Line.VehicleType : String [R/W]
EWBTransporter_Line.FromXMLFile(ByVal bstrFileName As String)
EWBTransporter_Line.FromXMLString(ByVal bstrXML As String)
EWBTransporter_Line.GetXMLSchema() -> String
EWBTransporter_Line.ToXMLFile(ByVal bstrFileName As String)
EWBTransporter_Line.ToXMLString() -> String
EWBTransporter_Lines.Count : Long [R]
EWBTransporter_Lines.Add() -> EWBTransporter_Line
EWBTransporter_Lines.GetXMLSchema() -> String
EWBTransporter_Lines.Item(ByVal vtIndex As Variant) -> EWBTransporter_Line
EWBTransporter_Lines.Remove(ByVal vtIndex As Variant)
EWBTransporter_Lines.ToXMLFile(ByVal bstrFileName As String)
EWBTransporter_Lines.ToXMLString() -> String
EWBTransporterParams.AbsEntry : Long [R/W]
EWBTransporterParams.TransporterCode : String [R]
EWBTransporterParams.TransporterID : String [R]
EWBTransporterParams.TransporterName : String [R]
EWBTransporterParams.FromXMLFile(ByVal bstrFileName As String)
EWBTransporterParams.FromXMLString(ByVal bstrXML As String)
EWBTransporterParams.GetXMLSchema() -> String
EWBTransporterParams.ToXMLFile(ByVal bstrFileName As String)
EWBTransporterParams.ToXMLString() -> String
EWBTransporterParamsCollection.Count : Long [R]
EWBTransporterParamsCollection.Add() -> EWBTransporterParams
EWBTransporterParamsCollection.GetXMLSchema() -> String
EWBTransporterParamsCollection.Item(ByVal vtIndex As Variant) -> EWBTransporterParams
EWBTransporterParamsCollection.ToXMLFile(ByVal bstrFileName As String)
EWBTransporterParamsCollection.ToXMLString() -> String
EWBTransporterService.AddTransporter(ByVal pIEWBTransporter As EWBTransporter) -> EWBTransporterParams
EWBTransporterService.DeleteTransporter(ByVal pIEWBTransporterParams As EWBTransporterParams)
EWBTransporterService.GetDataInterface(ByVal enumMSDI As EWBTransporterServiceDataInterfaces) -> Object
EWBTransporterService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
EWBTransporterService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
EWBTransporterService.GetEWBTransporterList() -> EWBTransporterParamsCollection
EWBTransporterService.GetTransporter(ByVal pIEWBTransporterParams As EWBTransporterParams) -> EWBTransporter
EWBTransporterService.UpdateTransporter(ByVal pIEWBTransporter As EWBTransporter)
ExceptionalEvent.Code : String [R/W]
ExceptionalEvent.Description : String [R/W]
ExceptionalEvent.FromXMLFile(ByVal bstrFileName As String)
ExceptionalEvent.FromXMLString(ByVal bstrXML As String)
ExceptionalEvent.GetXMLSchema() -> String
ExceptionalEvent.ToXMLFile(ByVal bstrFileName As String)
ExceptionalEvent.ToXMLString() -> String
ExceptionalEventParams.Code : String [R/W]
ExceptionalEventParams.FromXMLFile(ByVal bstrFileName As String)
ExceptionalEventParams.FromXMLString(ByVal bstrXML As String)
ExceptionalEventParams.GetXMLSchema() -> String
ExceptionalEventParams.ToXMLFile(ByVal bstrFileName As String)
ExceptionalEventParams.ToXMLString() -> String
ExceptionalEventService.AddExceptionalEvent(ByVal pIExceptionalEvent As ExceptionalEvent) -> ExceptionalEventParams
ExceptionalEventService.DeleteExceptionalEvent(ByVal pIExceptionalEventParams As ExceptionalEventParams)
ExceptionalEventService.GetDataInterface(ByVal enumMSDI As ExceptionalEventServiceDataInterfaces) -> Object
ExceptionalEventService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ExceptionalEventService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ExceptionalEventService.GetExceptionalEvent(ByVal pIExceptionalEventParams As ExceptionalEventParams) -> ExceptionalEvent
ExceptionalEventService.GetExceptionalEventList() -> ExceptionalEventsParams
ExceptionalEventService.UpdateExceptionalEvent(ByVal pIExceptionalEvent As ExceptionalEvent)
ExceptionalEventsParams.Count : Long [R]
ExceptionalEventsParams.Add() -> ExceptionalEventParams
ExceptionalEventsParams.GetXMLSchema() -> String
ExceptionalEventsParams.Item(ByVal vtIndex As Variant) -> ExceptionalEventParams
ExceptionalEventsParams.ToXMLFile(ByVal bstrFileName As String)
ExceptionalEventsParams.ToXMLString() -> String
ExpenseTypeData.ExpenseAccount : String [R/W]
ExpenseTypeData.ExpenseName : String [R/W]
ExpenseTypeData.ExpenseType : String [R/W]
ExpenseTypeData.PaidByCompany : BoYesNoEnum [R/W]
ExpenseTypeData.VatGroup : String [R/W]
ExpenseTypeData.FromXMLFile(ByVal bstrFileName As String)
ExpenseTypeData.FromXMLString(ByVal bstrXML As String)
ExpenseTypeData.GetXMLSchema() -> String
ExpenseTypeData.ToXMLFile(ByVal bstrFileName As String)
ExpenseTypeData.ToXMLString() -> String
ExpenseTypeParams.ExpenseType : String [R/W]
ExpenseTypeParams.FromXMLFile(ByVal bstrFileName As String)
ExpenseTypeParams.FromXMLString(ByVal bstrXML As String)
ExpenseTypeParams.GetXMLSchema() -> String
ExpenseTypeParams.ToXMLFile(ByVal bstrFileName As String)
ExpenseTypeParams.ToXMLString() -> String
ExpenseTypeService.Add(ByVal pIExpenseTypeData As ExpenseTypeData) -> ExpenseTypeParams
ExpenseTypeService.Get(ByVal pIExpenseTypeParams As ExpenseTypeParams) -> ExpenseTypeData
ExpenseTypeService.GetDataInterface(ByVal enumMSDI As ExpenseTypeServiceDataInterfaces) -> Object
ExpenseTypeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ExpenseTypeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ExpenseTypeService.Update(ByVal pIExpenseTypeData As ExpenseTypeData)
ExportDetermination.AbsEntry : Long [R]
ExportDetermination.BusinessPartner : String [R/W]
ExportDetermination.Code : ElectronicDocProtocolCodeStrEnum [R/W]
ExportDetermination.Country : String [R/W]
ExportDetermination.DocumentSubType : String [R/W]
ExportDetermination.DocumentType : String [R/W]
ExportDetermination.ExportFormat : Long [R/W]
ExportDetermination.PathFileName : String [R/W]
ExportDetermination.Priority : Long [R/W]
ExportDetermination.Series : Long [R/W]
ExportDetermination.FromXMLFile(ByVal bstrFileName As String)
ExportDetermination.FromXMLString(ByVal bstrXML As String)
ExportDetermination.GetXMLSchema() -> String
ExportDetermination.ToXMLFile(ByVal bstrFileName As String)
ExportDetermination.ToXMLString() -> String
ExportDeterminationParams.AbsEntry : Long [R/W]
ExportDeterminationParams.BusinessPartner : String [R/W]
ExportDeterminationParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
ExportDeterminationParams.Country : String [R/W]
ExportDeterminationParams.DocumentSubType : String [R/W]
ExportDeterminationParams.DocumentType : String [R/W]
ExportDeterminationParams.Series : Long [R/W]
ExportDeterminationParams.FromXMLFile(ByVal bstrFileName As String)
ExportDeterminationParams.FromXMLString(ByVal bstrXML As String)
ExportDeterminationParams.GetXMLSchema() -> String
ExportDeterminationParams.ToXMLFile(ByVal bstrFileName As String)
ExportDeterminationParams.ToXMLString() -> String
ExportDeterminationsCollection.Count : Long [R]
ExportDeterminationsCollection.Add() -> ExportDetermination
ExportDeterminationsCollection.GetXMLSchema() -> String
ExportDeterminationsCollection.Item(ByVal vtIndex As Variant) -> ExportDetermination
ExportDeterminationsCollection.ToXMLFile(ByVal bstrFileName As String)
ExportDeterminationsCollection.ToXMLString() -> String
ExportDeterminationService.AddDetermination(ByVal pIExportDetermination As ExportDetermination)
ExportDeterminationService.DeleteDetermination(ByVal pIExportDeterminationParams As ExportDeterminationParams)
ExportDeterminationService.GetDataInterface(ByVal enumMSDI As ExportDeterminationServiceDataInterfaces) -> Object
ExportDeterminationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ExportDeterminationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ExportDeterminationService.GetDetermination(ByVal pIExportDeterminationParams As ExportDeterminationParams) -> ExportDetermination
ExportDeterminationService.GetDeterminations(ByVal pIExportDeterminationsParams As ExportDeterminationsParams) -> ExportDeterminationsCollection
ExportDeterminationService.UpdateDetermination(ByVal pIExportDetermination As ExportDetermination)
ExportDeterminationsParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
ExportDeterminationsParams.FromXMLFile(ByVal bstrFileName As String)
ExportDeterminationsParams.FromXMLString(ByVal bstrXML As String)
ExportDeterminationsParams.GetXMLSchema() -> String
ExportDeterminationsParams.ToXMLFile(ByVal bstrFileName As String)
ExportDeterminationsParams.ToXMLString() -> String
ExportProcesses.AdditionalItemSequentialNumber : Long [R/W]
ExportProcesses.DrawbackSuspensionRegime : String [R/W]
ExportProcesses.ExportationDeclarationDate : Date [R/W]
ExportProcesses.ExportationDeclarationNumber : Long [R/W]
ExportProcesses.ExportationDocumentTypeCode : Long [R/W]
ExportProcesses.ExportationNatureCode : Long [R/W]
ExportProcesses.ExportationRegistryDate : Date [R/W]
ExportProcesses.ExportationRegistryNumber : Long [R/W]
ExportProcesses.LadingBillDate : Date [R/W]
ExportProcesses.LadingBillNumber : String [R/W]
ExportProcesses.LadingBillTypeCode : Long [R/W]
ExportProcesses.MerchandiseLeftCustomsDate : Date [R/W]
ExportProcesses.NatureOfExport : String [R/W]
ExportProcesses.QuantityOfExportedItems : Double [R/W]
ExtendedAdminInfo.AddressType : String [R/W]
ExtendedAdminInfo.AllowInactiveItemsInInventoryCountingAndPosting : BoYesNoEnum [R/W]
ExtendedAdminInfo.AllowInactiveItemsInInventoryOpeningBalance : BoYesNoEnum [R/W]
ExtendedAdminInfo.AuthorityPassword : String [R/W]
ExtendedAdminInfo.AuthorityUser : String [R/W]
ExtendedAdminInfo.AutoAssignNewBranchToBP : BoYesNoEnum [R/W]
ExtendedAdminInfo.CNPJofITCompany : String [R/W]
ExtendedAdminInfo.CommercialRegister : String [R/W]
ExtendedAdminInfo.CompanyQualificationCode : Long [R/W]
ExtendedAdminInfo.ContactPerson : String [R/W]
ExtendedAdminInfo.ContactPersonEMail : String [R/W]
ExtendedAdminInfo.ContactPersonPhone : String [R/W]
ExtendedAdminInfo.CooperativeAssociationTypeCode : Long [R/W]
ExtendedAdminInfo.CreditContributionOriginCode : String [R/W]
ExtendedAdminInfo.DateOfIncorporation : Date [R/W]
ExtendedAdminInfo.DeclarerTypeCode : Long [R/W]
ExtendedAdminInfo.DocumentRemarksInclude : DocumentRemarksIncludeTypeEnum [R/W]
ExtendedAdminInfo.EconomicActivityTypeCode : Long [R/W]
ExtendedAdminInfo.ElectronicApprovalForGoodsTransEnabled : BoYesNoEnum [R/W]
ExtendedAdminInfo.ElectronicApprovalForInvoiceEnabled : BoYesNoEnum [R/W]
ExtendedAdminInfo.EnableIntrastat : BoYesNoEnum [R/W]
ExtendedAdminInfo.EnvironmentType : Long [R/W]
ExtendedAdminInfo.GlobalLocationNumber : String [R/W]
ExtendedAdminInfo.IPIPeriodCode : String [R/W]
ExtendedAdminInfo.IPITaxContributor : BoYesNoEnum [R/W]
ExtendedAdminInfo.NatureOfCompanyCode : Long [R/W]
ExtendedAdminInfo.OKDPNumber : String [R/W]
ExtendedAdminInfo.Opting4ICMS : BoYesNoEnum [R/W]
ExtendedAdminInfo.ProfitTaxationCode : Long [R/W]
ExtendedAdminInfo.SPEDProfile : String [R/W]
ExtendedAdminInfo.STDCode : Long [R/W]
ExtendedAdminInfo.STDCodeForeign : Long [R/W]
ExtendedAdminInfo.StreetNo : String [R/W]
ExtendedAdminInfo.URLforGoodsTransportService : String [R/W]
ExtendedAdminInfo.URLforInvoiceTypeService : String [R/W]
ExtendedTranslation.Category : TranslationCategoryEnum [R/W]
ExtendedTranslation.CreateDate : Date [R]
ExtendedTranslation.DocEntry : Long [R]
ExtendedTranslation.ExtendedTranslation_ItemLines : ExtendedTranslation_ItemLines [R]
ExtendedTranslation.ID : String [R/W]
ExtendedTranslation.SecondaryID : String [R/W]
ExtendedTranslation.SourceLanguage : Long [R/W]
ExtendedTranslation.UpdateDate : Date [R]
ExtendedTranslation.FromXMLFile(ByVal bstrFileName As String)
ExtendedTranslation.FromXMLString(ByVal bstrXML As String)
ExtendedTranslation.GetXMLSchema() -> String
ExtendedTranslation.ToXMLFile(ByVal bstrFileName As String)
ExtendedTranslation.ToXMLString() -> String
ExtendedTranslation_ItemLine.DocEntry : Long [R]
ExtendedTranslation_ItemLine.ExtendedTranslation_ResultLines : ExtendedTranslation_ResultLines [R]
ExtendedTranslation_ItemLine.ItemCode : String [R/W]
ExtendedTranslation_ItemLine.ItemType : String [R/W]
ExtendedTranslation_ItemLine.LineNumber : Long [R]
ExtendedTranslation_ItemLine.MaxLength : Long [R/W]
ExtendedTranslation_ItemLine.Memo : String [R/W]
ExtendedTranslation_ItemLine.SlimType : String [R/W]
ExtendedTranslation_ItemLine.SourceText : String [R/W]
ExtendedTranslation_ItemLine.FromXMLFile(ByVal bstrFileName As String)
ExtendedTranslation_ItemLine.FromXMLString(ByVal bstrXML As String)
ExtendedTranslation_ItemLine.GetXMLSchema() -> String
ExtendedTranslation_ItemLine.ToXMLFile(ByVal bstrFileName As String)
ExtendedTranslation_ItemLine.ToXMLString() -> String
ExtendedTranslation_ItemLines.Count : Long [R]
ExtendedTranslation_ItemLines.Add() -> ExtendedTranslation_ItemLine
ExtendedTranslation_ItemLines.GetXMLSchema() -> String
ExtendedTranslation_ItemLines.Item(ByVal vtIndex As Variant) -> ExtendedTranslation_ItemLine
ExtendedTranslation_ItemLines.Remove(ByVal vtIndex As Variant)
ExtendedTranslation_ItemLines.ToXMLFile(ByVal bstrFileName As String)
ExtendedTranslation_ItemLines.ToXMLString() -> String
ExtendedTranslation_ResultLine.DocEntry : Long [R]
ExtendedTranslation_ResultLine.LanguageCode : Long [R/W]
ExtendedTranslation_ResultLine.LineNumber : Long [R]
ExtendedTranslation_ResultLine.SubLineNumber : Long [R]
ExtendedTranslation_ResultLine.TranslatedText : String [R/W]
ExtendedTranslation_ResultLine.FromXMLFile(ByVal bstrFileName As String)
ExtendedTranslation_ResultLine.FromXMLString(ByVal bstrXML As String)
ExtendedTranslation_ResultLine.GetXMLSchema() -> String
ExtendedTranslation_ResultLine.ToXMLFile(ByVal bstrFileName As String)
ExtendedTranslation_ResultLine.ToXMLString() -> String
ExtendedTranslation_ResultLines.Count : Long [R]
ExtendedTranslation_ResultLines.Add() -> ExtendedTranslation_ResultLine
ExtendedTranslation_ResultLines.GetXMLSchema() -> String
ExtendedTranslation_ResultLines.Item(ByVal vtIndex As Variant) -> ExtendedTranslation_ResultLine
ExtendedTranslation_ResultLines.Remove(ByVal vtIndex As Variant)
ExtendedTranslation_ResultLines.ToXMLFile(ByVal bstrFileName As String)
ExtendedTranslation_ResultLines.ToXMLString() -> String
ExtendedTranslationParams.Category : TranslationCategoryEnum [R/W]
ExtendedTranslationParams.DocEntry : Long [R/W]
ExtendedTranslationParams.ID : String [R/W]
ExtendedTranslationParams.SecondaryID : String [R/W]
ExtendedTranslationParams.FromXMLFile(ByVal bstrFileName As String)
ExtendedTranslationParams.FromXMLString(ByVal bstrXML As String)
ExtendedTranslationParams.GetXMLSchema() -> String
ExtendedTranslationParams.ToXMLFile(ByVal bstrFileName As String)
ExtendedTranslationParams.ToXMLString() -> String
ExtendedTranslationsParams.Count : Long [R]
ExtendedTranslationsParams.Add() -> ExtendedTranslationParams
ExtendedTranslationsParams.GetXMLSchema() -> String
ExtendedTranslationsParams.Item(ByVal vtIndex As Variant) -> ExtendedTranslationParams
ExtendedTranslationsParams.ToXMLFile(ByVal bstrFileName As String)
ExtendedTranslationsParams.ToXMLString() -> String
ExtendedTranslationsService.AddExtendedTranslation(ByVal pIExtendedTranslation As ExtendedTranslation) -> ExtendedTranslationParams
ExtendedTranslationsService.DeleteExtendedTranslation(ByVal pIExtendedTranslationParams As ExtendedTranslationParams)
ExtendedTranslationsService.GetDataInterface(ByVal enumMSDI As ExtendedTranslationsServiceDataInterfaces) -> Object
ExtendedTranslationsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ExtendedTranslationsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ExtendedTranslationsService.GetExtendedTranslation(ByVal pIExtendedTranslationParams As ExtendedTranslationParams) -> ExtendedTranslation
ExtendedTranslationsService.GetExtendedTranslationList() -> ExtendedTranslationsParams
ExtendedTranslationsService.UpdateExtendedTranslation(ByVal pIExtendedTranslation As ExtendedTranslation)
ExternalCall.CallArguments : CallArguments [R]
ExternalCall.CallMessages : CallMessages [R]
ExternalCall.Category : Long [R/W]
ExternalCall.CreationDate : Date [R]
ExternalCall.CreationTime : Long [R]
ExternalCall.ID : Long [R]
ExternalCall.LastUpdateDate : Date [R/W]
ExternalCall.LastUpdateTime : Long [R/W]
ExternalCall.LastUpdateUserCode : String [R/W]
ExternalCall.Status : ExternalCallStatusEnum [R/W]
ExternalCall.FromXMLFile(ByVal bstrFileName As String)
ExternalCall.FromXMLString(ByVal bstrXML As String)
ExternalCall.GetXMLSchema() -> String
ExternalCall.ToXMLFile(ByVal bstrFileName As String)
ExternalCall.ToXMLString() -> String
ExternalCallParams.ID : Long [R/W]
ExternalCallParams.FromXMLFile(ByVal bstrFileName As String)
ExternalCallParams.FromXMLString(ByVal bstrXML As String)
ExternalCallParams.GetXMLSchema() -> String
ExternalCallParams.ToXMLFile(ByVal bstrFileName As String)
ExternalCallParams.ToXMLString() -> String
ExternalCallsService.GetCall(ByVal pIExternalCallParams As ExternalCallParams) -> ExternalCall
ExternalCallsService.GetDataInterface(ByVal enumMSDI As ExternalCallsServiceDataInterfaces) -> Object
ExternalCallsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ExternalCallsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ExternalCallsService.SendCall(ByVal pIExternalCall As ExternalCall) -> ExternalCallParams
ExternalCallsService.UpdateCall(ByVal pIExternalCall As ExternalCall)
ExternalReconciliation.AccountCode : String [R]
ExternalReconciliation.amount : Double [R]
ExternalReconciliation.CreationDate : Date [R]
ExternalReconciliation.CurrencyType : String [R]
ExternalReconciliation.ReconciliationAccountType : ReconciliationAccountTypeEnum [R/W]
ExternalReconciliation.ReconciliationBankStatementLines : ReconciliationBankStatementLines [R]
ExternalReconciliation.ReconciliationDate : Date [R]
ExternalReconciliation.ReconciliationJournalEntryLines : ReconciliationJournalEntryLines [R]
ExternalReconciliation.ReconciliationNo : Long [R]
ExternalReconciliation.ReconciliationType : String [R]
ExternalReconciliation.FromXMLFile(ByVal bstrFileName As String)
ExternalReconciliation.FromXMLString(ByVal bstrXML As String)
ExternalReconciliation.GetXMLSchema() -> String
ExternalReconciliation.ToXMLFile(ByVal bstrFileName As String)
ExternalReconciliation.ToXMLString() -> String
ExternalReconciliationFilterParams.AccountCodeFrom : String [R/W]
ExternalReconciliationFilterParams.AccountCodeTo : String [R/W]
ExternalReconciliationFilterParams.ReconciliationAccountType : ReconciliationAccountTypeEnum [R/W]
ExternalReconciliationFilterParams.ReconciliationDateFrom : Date [R/W]
ExternalReconciliationFilterParams.ReconciliationDateTo : Date [R/W]
ExternalReconciliationFilterParams.ReconciliationNoFrom : Long [R/W]
ExternalReconciliationFilterParams.ReconciliationNoTo : Long [R/W]
ExternalReconciliationFilterParams.FromXMLFile(ByVal bstrFileName As String)
ExternalReconciliationFilterParams.FromXMLString(ByVal bstrXML As String)
ExternalReconciliationFilterParams.GetXMLSchema() -> String
ExternalReconciliationFilterParams.ToXMLFile(ByVal bstrFileName As String)
ExternalReconciliationFilterParams.ToXMLString() -> String
ExternalReconciliationParams.AccountCode : String [R/W]
ExternalReconciliationParams.ReconciliationNo : Long [R/W]
ExternalReconciliationParams.FromXMLFile(ByVal bstrFileName As String)
ExternalReconciliationParams.FromXMLString(ByVal bstrXML As String)
ExternalReconciliationParams.GetXMLSchema() -> String
ExternalReconciliationParams.ToXMLFile(ByVal bstrFileName As String)
ExternalReconciliationParams.ToXMLString() -> String
ExternalReconciliationsParamsCollection.Count : Long [R]
ExternalReconciliationsParamsCollection.Add() -> ExternalReconciliationParams
ExternalReconciliationsParamsCollection.GetXMLSchema() -> String
ExternalReconciliationsParamsCollection.Item(ByVal vtIndex As Variant) -> ExternalReconciliationParams
ExternalReconciliationsParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ExternalReconciliationsParamsCollection.ToXMLString() -> String
ExternalReconciliationsService.CancelReconciliation(ByVal pIExternalReconciliationParams As ExternalReconciliationParams)
ExternalReconciliationsService.GetDataInterface(ByVal enumMSDI As ExternalReconciliationsServiceDataInterfaces) -> Object
ExternalReconciliationsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ExternalReconciliationsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ExternalReconciliationsService.GetReconciliation(ByVal pIExternalReconciliationParams As ExternalReconciliationParams) -> ExternalReconciliation
ExternalReconciliationsService.GetReconciliationList(ByVal pIExternalReconciliationFilterParams As ExternalReconciliationFilterParams) -> ExternalReconciliationsParamsCollection
ExternalReconciliationsService.Reconcile(ByVal pIExternalReconciliation As ExternalReconciliation)
FAAccountDetermination.AccumulatedOrdinaryDepr : String [R/W]
FAAccountDetermination.AccumulatedSpecialDepr : String [R/W]
FAAccountDetermination.AccumulatedUnplannedDepr : String [R/W]
FAAccountDetermination.AssetBalanceSheetAccount : String [R/W]
FAAccountDetermination.ClearingAccountAcquisition : String [R/W]
FAAccountDetermination.Code : String [R/W]
FAAccountDetermination.Description : String [R/W]
FAAccountDetermination.LeavewithExpenseNBVGross : String [R/W]
FAAccountDetermination.LeavewithRevenueNBVGross : String [R/W]
FAAccountDetermination.OrdinaryDepreciation : String [R/W]
FAAccountDetermination.RetirementwithExpenseNet : String [R/W]
FAAccountDetermination.RetirementwithRevenueNet : String [R/W]
FAAccountDetermination.RevaluationAccount : String [R/W]
FAAccountDetermination.RevaluationLossAcct : String [R/W]
FAAccountDetermination.RevaluationReserveAccount : String [R/W]
FAAccountDetermination.RevaluationReserveClearing : String [R/W]
FAAccountDetermination.RevenueAccountforRetirement : String [R/W]
FAAccountDetermination.RevenueClearingAccount : String [R/W]
FAAccountDetermination.RevenuefromAssetSalesNet : String [R/W]
FAAccountDetermination.SpecialDepreciation : String [R/W]
FAAccountDetermination.UnplannedDepreciation : String [R/W]
FAAccountDetermination.FromXMLFile(ByVal bstrFileName As String)
FAAccountDetermination.FromXMLString(ByVal bstrXML As String)
FAAccountDetermination.GetXMLSchema() -> String
FAAccountDetermination.ToXMLFile(ByVal bstrFileName As String)
FAAccountDetermination.ToXMLString() -> String
FAAccountDeterminationParams.Code : String [R/W]
FAAccountDeterminationParams.Description : String [R]
FAAccountDeterminationParams.FromXMLFile(ByVal bstrFileName As String)
FAAccountDeterminationParams.FromXMLString(ByVal bstrXML As String)
FAAccountDeterminationParams.GetXMLSchema() -> String
FAAccountDeterminationParams.ToXMLFile(ByVal bstrFileName As String)
FAAccountDeterminationParams.ToXMLString() -> String
FAAccountDeterminationParamsCollection.Count : Long [R]
FAAccountDeterminationParamsCollection.Add() -> FAAccountDeterminationParams
FAAccountDeterminationParamsCollection.GetXMLSchema() -> String
FAAccountDeterminationParamsCollection.Item(ByVal vtIndex As Variant) -> FAAccountDeterminationParams
FAAccountDeterminationParamsCollection.ToXMLFile(ByVal bstrFileName As String)
FAAccountDeterminationParamsCollection.ToXMLString() -> String
FAAccountDeterminationsService.Add(ByVal pIFAAccountDetermination As FAAccountDetermination) -> FAAccountDeterminationParams
FAAccountDeterminationsService.Delete(ByVal pIFAAccountDeterminationParams As FAAccountDeterminationParams)
FAAccountDeterminationsService.Get(ByVal pIFAAccountDeterminationParams As FAAccountDeterminationParams) -> FAAccountDetermination
FAAccountDeterminationsService.GetDataInterface(ByVal enumMSDI As FAAccountDeterminationsServiceDataInterfaces) -> Object
FAAccountDeterminationsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
FAAccountDeterminationsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
FAAccountDeterminationsService.GetList() -> FAAccountDeterminationParamsCollection
FAAccountDeterminationsService.Update(ByVal pIFAAccountDetermination As FAAccountDetermination)
FactoringIndicators.Browser : DataBrowser [R]
FactoringIndicators.IndicatorCode : String [R/W]
FactoringIndicators.IndicatorName : String [R/W]
FactoringIndicators.UserFields : UserFields [R]
FactoringIndicators.Add() -> Long
FactoringIndicators.GetAsXML() -> String
FactoringIndicators.GetByKey(ByVal bstrCode As String) -> Boolean
FactoringIndicators.SaveToFile(ByVal bstrFileName As String)
FactoringIndicators.SaveXML(ByRef pbstrFileName As String)
FactoringIndicators.Update() -> Long
FeatureStatus.Blocked : BoYesNoEnum [R]
FeatureStatus.FeatureID : String [R]
FeatureStatus.FromXMLFile(ByVal bstrFileName As String)
FeatureStatus.FromXMLString(ByVal bstrXML As String)
FeatureStatus.GetXMLSchema() -> String
FeatureStatus.ToXMLFile(ByVal bstrFileName As String)
FeatureStatus.ToXMLString() -> String
FeatureStatusCollection.Count : Long [R]
FeatureStatusCollection.Add() -> FeatureStatus
FeatureStatusCollection.GetXMLSchema() -> String
FeatureStatusCollection.Item(ByVal vtIndex As Variant) -> FeatureStatus
FeatureStatusCollection.ToXMLFile(ByVal bstrFileName As String)
FeatureStatusCollection.ToXMLString() -> String
Field.DefaultValue : String [R]
Field.Description : String [R]
Field.FieldID : Long [R]
Field.LinkedTable : String [R]
Field.Mandatory : BoYesNoEnum [R]
Field.Name : String [R]
Field.Size : Long [R]
Field.SubType : BoFldSubTypes [R]
Field.Table : String [R]
Field.Type : BoFieldTypes [R]
Field.ValidValue : String [R/W]
Field.ValidValues : ValidValues [R]
Field.Value : Variant [R/W]
Field.IsNull() -> BoYesNoEnum
Field.SetNullValue() -> Long
Fields.Count : Long [R]
Fields.Item(ByVal Index As Variant) -> Field
FIFOLayers.BaseLine : Long [R/W]
FIFOLayers.Count : Long [R]
FIFOLayers.LayerID : Long [R/W]
FIFOLayers.LineTotal : Double [R/W]
FIFOLayers.Price : Double [R/W]
FIFOLayers.Quantity : Double [R/W]
FIFOLayers.TransactionSequenceNum : Long [R/W]
FIFOLayers.Add()
FIFOLayers.SetCurrentLine(ByVal LineNum As Long)
FinancePeriod.AbsoluteEntry : Long [R]
FinancePeriod.ActiveforFeed : BoYesNoEnum [R/W]
FinancePeriod.AdditionalSubPeriods : BoYesNoEnum [R]
FinancePeriod.Locked : BoYesNoEnum [R/W]
FinancePeriod.PeriodCode : String [R/W]
FinancePeriod.PeriodIndicator : String [R/W]
FinancePeriod.PeriodName : String [R/W]
FinancePeriod.PeriodStatus : PeriodStatusEnum [R/W]
FinancePeriod.PostingDateFrom : Date [R/W]
FinancePeriod.PostingDateTo : Date [R/W]
FinancePeriod.SubNum : Long [R]
FinancePeriod.TaxDateFrom : Date [R/W]
FinancePeriod.TaxDateTo : Date [R/W]
FinancePeriod.ValueDateFrom : Date [R/W]
FinancePeriod.ValueDateTo : Date [R/W]
FinancePeriod.FromXMLFile(ByVal bstrFileName As String)
FinancePeriod.FromXMLString(ByVal bstrXML As String)
FinancePeriod.GetXMLSchema() -> String
FinancePeriod.ToXMLFile(ByVal bstrFileName As String)
FinancePeriod.ToXMLString() -> String
FinancePeriodParams.AbsoluteEntry : Long [R/W]
FinancePeriodParams.PeriodIndicator : String [R/W]
FinancePeriodParams.FromXMLFile(ByVal bstrFileName As String)
FinancePeriodParams.FromXMLString(ByVal bstrXML As String)
FinancePeriodParams.GetXMLSchema() -> String
FinancePeriodParams.ToXMLFile(ByVal bstrFileName As String)
FinancePeriodParams.ToXMLString() -> String
FinancePeriods.Count : Long [R]
FinancePeriods.Add() -> FinancePeriod
FinancePeriods.GetXMLSchema() -> String
FinancePeriods.Item(ByVal vtIndex As Variant) -> FinancePeriod
FinancePeriods.ToXMLFile(ByVal bstrFileName As String)
FinancePeriods.ToXMLString() -> String
FinancialYear.AbsEntry : Long [R]
FinancialYear.AssessYear : String [R/W]
FinancialYear.Code : String [R/W]
FinancialYear.Description : String [R/W]
FinancialYear.EndDate : Date [R]
FinancialYear.StartDate : Date [R/W]
FinancialYear.TCSAccumulationBase : TCSAccumulationBaseEnum [R/W]
FinancialYear.FromXMLFile(ByVal bstrFileName As String)
FinancialYear.FromXMLString(ByVal bstrXML As String)
FinancialYear.GetXMLSchema() -> String
FinancialYear.ToXMLFile(ByVal bstrFileName As String)
FinancialYear.ToXMLString() -> String
FinancialYearParams.AbsEntry : Long [R/W]
FinancialYearParams.Code : String [R]
FinancialYearParams.Description : String [R]
FinancialYearParams.FromXMLFile(ByVal bstrFileName As String)
FinancialYearParams.FromXMLString(ByVal bstrXML As String)
FinancialYearParams.GetXMLSchema() -> String
FinancialYearParams.ToXMLFile(ByVal bstrFileName As String)
FinancialYearParams.ToXMLString() -> String
FinancialYearsParams.Count : Long [R]
FinancialYearsParams.Add() -> FinancialYearParams
FinancialYearsParams.GetXMLSchema() -> String
FinancialYearsParams.Item(ByVal vtIndex As Variant) -> FinancialYearParams
FinancialYearsParams.ToXMLFile(ByVal bstrFileName As String)
FinancialYearsParams.ToXMLString() -> String
FinancialYearsService.AddFinancialYear(ByVal pIFinancialYear As FinancialYear) -> FinancialYearParams
FinancialYearsService.DeleteFinancialYear(ByVal pIFinancialYearParams As FinancialYearParams)
FinancialYearsService.GetDataInterface(ByVal enumMSDI As FinancialYearsServiceDataInterfaces) -> Object
FinancialYearsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
FinancialYearsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
FinancialYearsService.GetFinancialYear(ByVal pIFinancialYearParams As FinancialYearParams) -> FinancialYear
FinancialYearsService.GetFinancialYearList() -> FinancialYearsParams
FinancialYearsService.UpdateFinancialYear(ByVal pIFinancialYear As FinancialYear)
FiscalPrinter.EquipmentNo : String [R/W]
FiscalPrinter.FiscalDocumentModel : String [R/W]
FiscalPrinter.FiscalPrintersParams : FiscalPrintersParams [R]
FiscalPrinter.ManufacturerSerialN : String [R/W]
FiscalPrinter.Model : String [R/W]
FiscalPrinter.RegisterNo : Long [R/W]
FiscalPrinter.FromXMLFile(ByVal bstrFileName As String)
FiscalPrinter.FromXMLString(ByVal bstrXML As String)
FiscalPrinter.GetXMLSchema() -> String
FiscalPrinter.ToXMLFile(ByVal bstrFileName As String)
FiscalPrinter.ToXMLString() -> String
FiscalPrinterParams.EquipmentNo : String [R/W]
FiscalPrinterParams.FromXMLFile(ByVal bstrFileName As String)
FiscalPrinterParams.FromXMLString(ByVal bstrXML As String)
FiscalPrinterParams.GetXMLSchema() -> String
FiscalPrinterParams.ToXMLFile(ByVal bstrFileName As String)
FiscalPrinterParams.ToXMLString() -> String
FiscalPrinterService.AddFiscalPrinter(ByVal pIFiscalPrinter As FiscalPrinter) -> FiscalPrinterParams
FiscalPrinterService.DeleteFiscalPrinter(ByVal pIFiscalPrinterParams As FiscalPrinterParams)
FiscalPrinterService.GetDataInterface(ByVal enumMSDI As FiscalPrinterServiceDataInterfaces) -> Object
FiscalPrinterService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
FiscalPrinterService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
FiscalPrinterService.GetFiscalPrinter(ByVal pIFiscalPrinterParams As FiscalPrinterParams) -> FiscalPrinter
FiscalPrinterService.GetFiscalPrinterList() -> FiscalPrintersParams
FiscalPrinterService.UpdateFiscalPrinter(ByVal pIFiscalPrinter As FiscalPrinter)
FiscalPrintersParams.Count : Long [R]
FiscalPrintersParams.Add() -> FiscalPrinterParams
FiscalPrintersParams.GetXMLSchema() -> String
FiscalPrintersParams.Item(ByVal vtIndex As Variant) -> FiscalPrinterParams
FiscalPrintersParams.ToXMLFile(ByVal bstrFileName As String)
FiscalPrintersParams.ToXMLString() -> String
FixedAssetEndBalance.AcquisitionCost : Double [R]
FixedAssetEndBalance.HistoricalAPC : Double [R/W]
FixedAssetEndBalance.HistoricalNBV : Double [R]
FixedAssetEndBalance.NetBookValue : Double [R]
FixedAssetEndBalance.OrdinaryDepreciationValue : Double [R]
FixedAssetEndBalance.Quantity : Double [R]
FixedAssetEndBalance.SalvageValue : Double [R/W]
FixedAssetEndBalance.SpecialDepreciationValue : Double [R]
FixedAssetEndBalance.UnplanedDepreciationValue : Double [R]
FixedAssetEndBalance.WriteUp : Double [R]
FixedAssetEndBalance.FromXMLFile(ByVal bstrFileName As String)
FixedAssetEndBalance.FromXMLString(ByVal bstrXML As String)
FixedAssetEndBalance.GetXMLSchema() -> String
FixedAssetEndBalance.ToXMLFile(ByVal bstrFileName As String)
FixedAssetEndBalance.ToXMLString() -> String
FixedAssetItemsService.GetAssetEndBalance(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams) -> FixedAssetEndBalance
FixedAssetItemsService.GetAssetValuesList(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams) -> FixedAssetValuesParamsCollection
FixedAssetItemsService.GetDataInterface(ByVal enumMSDI As FixedAssetItemsServiceDataInterfaces) -> Object
FixedAssetItemsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
FixedAssetItemsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
FixedAssetItemsService.UpdateAssetEndBalance(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams, ByVal pIFixedAssetEndBalance As FixedAssetEndBalance)
FixedAssetValues.AcquisitionCost : Double [R]
FixedAssetValues.Appreciation : Double [R]
FixedAssetValues.DepreciationValue : Double [R]
FixedAssetValues.NetBookValue : Double [R]
FixedAssetValues.OrdinaryDepreciationValue : Double [R]
FixedAssetValues.Quantity : Double [R]
FixedAssetValues.SpecialDepreciationValue : Double [R]
FixedAssetValues.TransactionType : AssetTransactionTypeEnum [R]
FixedAssetValues.UnplanedDepreciationValue : Double [R]
FixedAssetValues.WriteUp : Double [R]
FixedAssetValues.FromXMLFile(ByVal bstrFileName As String)
FixedAssetValues.FromXMLString(ByVal bstrXML As String)
FixedAssetValues.GetXMLSchema() -> String
FixedAssetValues.ToXMLFile(ByVal bstrFileName As String)
FixedAssetValues.ToXMLString() -> String
FixedAssetValuesParams.DepreciationArea : String [R/W]
FixedAssetValuesParams.FiscalYear : String [R/W]
FixedAssetValuesParams.ItemCode : String [R/W]
FixedAssetValuesParams.FromXMLFile(ByVal bstrFileName As String)
FixedAssetValuesParams.FromXMLString(ByVal bstrXML As String)
FixedAssetValuesParams.GetXMLSchema() -> String
FixedAssetValuesParams.ToXMLFile(ByVal bstrFileName As String)
FixedAssetValuesParams.ToXMLString() -> String
FixedAssetValuesParamsCollection.Count : Long [R]
FixedAssetValuesParamsCollection.Add() -> FixedAssetValues
FixedAssetValuesParamsCollection.GetXMLSchema() -> String
FixedAssetValuesParamsCollection.Item(ByVal vtIndex As Variant) -> FixedAssetValues
FixedAssetValuesParamsCollection.ToXMLFile(ByVal bstrFileName As String)
FixedAssetValuesParamsCollection.ToXMLString() -> String
FormattedSearches.Action : BoFormattedSearchActionEnum [R/W]
FormattedSearches.Browser : DataBrowser [R]
FormattedSearches.ByField : BoYesNoEnum [R/W]
FormattedSearches.ByFieldEx : FormattedSearchByFieldEnum [R/W]
FormattedSearches.ColumnID : String [R/W]
FormattedSearches.FieldID : String [R/W]
FormattedSearches.FieldIDs : FormattedSearchFields [R]
FormattedSearches.ForceRefresh : BoYesNoEnum [R/W]
FormattedSearches.FormID : String [R/W]
FormattedSearches.Index : Long [R]
FormattedSearches.ItemID : String [R/W]
FormattedSearches.QueryID : Long [R/W]
FormattedSearches.Refresh : BoYesNoEnum [R/W]
FormattedSearches.UserFields : UserFields [R]
FormattedSearches.UserValidValues : UserValidValues [R]
FormattedSearches.Add() -> Long
FormattedSearches.GetAsXML() -> String
FormattedSearches.GetByKey(ByVal lIndex As Long) -> Boolean
FormattedSearches.Remove() -> Long
FormattedSearches.SaveToFile(ByVal bstrFileName As String)
FormattedSearches.SaveXML(ByRef pbstrFileName As String)
FormattedSearches.Update() -> Long
FormattedSearchFields.Count : Long [R]
FormattedSearchFields.FieldID : String [R/W]
FormattedSearchFields.Add()
FormattedSearchFields.Remove()
FormattedSearchFields.SetCurrentLine(ByVal LineNum As Long)
FormPreferencesService.GetColumnsPreferences(ByVal pIColumnsPreferencesParams As ColumnsPreferencesParams) -> ColumnsPreferences
FormPreferencesService.GetDataInterface(ByVal enumMSDI As FormPreferencesServiceDataInterfaces) -> Object
FormPreferencesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
FormPreferencesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
FormPreferencesService.UpdateColumnsPreferences(ByVal pIColumnsPreferencesParams As ColumnsPreferencesParams, ByVal pIColumnsPreferences As ColumnsPreferences)
Forms1099.Boxes1099 : Boxes1099 [R]
Forms1099.Browser : DataBrowser [R]
Forms1099.Form1099 : String [R/W]
Forms1099.FormCode : Long [R]
Forms1099.UserFields : UserFields [R]
Forms1099.Add() -> Long
Forms1099.GetAsXML() -> String
Forms1099.GetByKey(ByVal lFormCode As Long) -> Boolean
Forms1099.Remove() -> Long
Forms1099.SaveToFile(ByVal bstrFileName As String)
Forms1099.SaveXML(ByRef pbstrFileName As String)
Forms1099.Update() -> Long
GeneralCollectionParams.Count : Long [R]
GeneralCollectionParams.Add() -> GeneralDataParams
GeneralCollectionParams.GetXMLSchema() -> String
GeneralCollectionParams.Item(ByVal vtIndex As Variant) -> GeneralDataParams
GeneralCollectionParams.ToXMLFile(ByVal bstrFileName As String)
GeneralCollectionParams.ToXMLString() -> String
GeneralData.Child(ByVal bstrDataName As String) -> GeneralDataCollection
GeneralData.FromXMLFile(ByVal bstrFileName As String)
GeneralData.FromXMLString(ByVal bstrXML As String)
GeneralData.GetProperty(ByVal bstrPropertyName As String) -> Variant
GeneralData.GetXMLSchema() -> String
GeneralData.SetProperty(ByVal bstrPropertyName As String, ByVal vtValue As Variant)
GeneralData.ToXMLFile(ByVal bstrFileName As String)
GeneralData.ToXMLString() -> String
GeneralDataCollection.Count : Long [R]
GeneralDataCollection.Add() -> GeneralData
GeneralDataCollection.GetXMLSchema() -> String
GeneralDataCollection.Item(ByVal vtIndex As Variant) -> GeneralData
GeneralDataCollection.Remove(ByVal vtIndex As Variant)
GeneralDataCollection.ToXMLFile(ByVal bstrFileName As String)
GeneralDataCollection.ToXMLString() -> String
GeneralDataParams.GetProperty(ByVal bstrPropertyName As String) -> Variant
GeneralDataParams.SetProperty(ByVal bstrPropertyName As String, ByVal vtValue As Variant)
GeneralService.Add(ByVal pIGeneralData As GeneralData) -> GeneralDataParams
GeneralService.Cancel(ByVal pIGeneralDataParams As GeneralDataParams)
GeneralService.Close(ByVal pIGeneralDataParams As GeneralDataParams)
GeneralService.Delete(ByVal pIGeneralDataParams As GeneralDataParams)
GeneralService.DoCommand(ByVal pGeneralData As GeneralData, ByVal Command_Name As String) -> GeneralData
GeneralService.GetByParams(ByVal pIGeneralDataParams As GeneralDataParams) -> GeneralData
GeneralService.GetDataInterface(ByVal enumMSDI As GeneralServiceDataInterfaces) -> Object
GeneralService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
GeneralService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
GeneralService.GetList() -> GeneralCollectionParams
GeneralService.InvokeMethod(ByVal pIInvokeParams As InvokeParams, ByVal pIGeneralData As GeneralData) -> InvokeParams
GeneralService.Update(ByVal pIGeneralData As GeneralData)
GeneratedAssets.amount : Double [R]
GeneratedAssets.amountSC : Double [R]
GeneratedAssets.AssetCode : String [R/W]
GeneratedAssets.Count : Long [R]
GeneratedAssets.DocEntry : Long [R]
GeneratedAssets.LineNumber : Long [R/W]
GeneratedAssets.Remarks : String [R/W]
GeneratedAssets.SerialNumber : String [R/W]
GeneratedAssets.Status : GeneratedAssetStatusEnum [R]
GeneratedAssets.VisOrder : Long [R]
GeneratedAssets.Add()
GeneratedAssets.Delete()
GeneratedAssets.SetCurrentLine(ByVal LineNum As Long)
GetChangeLogParams.Object : BoChangeLogEnum [R/W]
GetChangeLogParams.PrimaryKey : String [R/W]
GetChangeLogParams.UDOObjectCode : String [R/W]
GetChangeLogParams.FromXMLFile(ByVal bstrFileName As String)
GetChangeLogParams.FromXMLString(ByVal bstrXML As String)
GetChangeLogParams.GetXMLSchema() -> String
GetChangeLogParams.ToXMLFile(ByVal bstrFileName As String)
GetChangeLogParams.ToXMLString() -> String
GLAccount.Code : String [R/W]
GLAccount.Credit : Double [R/W]
GLAccount.Debit : Double [R/W]
GLAccount.DueDate : Date [R/W]
GLAccount.ForeignCredit : Double [R/W]
GLAccount.ForeignCurrency : String [R/W]
GLAccount.ForeignDebit : Double [R/W]
GLAccount.SystemCredit : Double [R/W]
GLAccount.SystemDebit : Double [R/W]
GLAccount.FromXMLFile(ByVal bstrFileName As String)
GLAccount.FromXMLString(ByVal bstrXML As String)
GLAccount.GetXMLSchema() -> String
GLAccount.ToXMLFile(ByVal bstrFileName As String)
GLAccount.ToXMLString() -> String
GLAccountAdvancedRule.AbsoluteEntry : Long [R]
GLAccountAdvancedRule.BeginningofFinancialYear : Date [R/W]
GLAccountAdvancedRule.BPCode : String [R/W]
GLAccountAdvancedRule.BPGroup : Long [R/W]
GLAccountAdvancedRule.BusinessPartnerType : BoBusinessPartnerTypes [R/W]
GLAccountAdvancedRule.Code : String [R/W]
GLAccountAdvancedRule.CostAccount : String [R/W]
GLAccountAdvancedRule.CostInflationAccount : String [R/W]
GLAccountAdvancedRule.CostInflationOffsetAccount : String [R/W]
GLAccountAdvancedRule.DecreasingAccount : String [R/W]
GLAccountAdvancedRule.Description : String [R/W]
GLAccountAdvancedRule.EUExpensesAccount : String [R/W]
GLAccountAdvancedRule.EUPurchaseCreditAcc : String [R/W]
GLAccountAdvancedRule.EURevenuesAccount : String [R/W]
GLAccountAdvancedRule.ExchangeRateDifferencesAcct : String [R/W]
GLAccountAdvancedRule.ExemptedCredits : String [R/W]
GLAccountAdvancedRule.ExemptIncomeAcc : String [R/W]
GLAccountAdvancedRule.ExpenseClearingAct : String [R/W]
GLAccountAdvancedRule.ExpenseOffsettingAccount : String [R/W]
GLAccountAdvancedRule.ExpensesAccount : String [R/W]
GLAccountAdvancedRule.FederalTaxID : String [R/W]
GLAccountAdvancedRule.FinancialYear : Long [R/W]
GLAccountAdvancedRule.ForeignExpensAcc : String [R/W]
GLAccountAdvancedRule.ForeignPurchaseCreditAcc : String [R/W]
GLAccountAdvancedRule.ForeignRevenueAcc : String [R/W]
GLAccountAdvancedRule.FromDate : Date [R/W]
GLAccountAdvancedRule.FromDocumentDate : Date [R/W]
GLAccountAdvancedRule.FromDueDate : Date [R/W]
GLAccountAdvancedRule.FromPostingDate : Date [R/W]
GLAccountAdvancedRule.GetGLAccountBy : GetGLAccountByEnum [R/W]
GLAccountAdvancedRule.GLDecreaseAcct : String [R/W]
GLAccountAdvancedRule.GLIncreaseAcct : String [R/W]
GLAccountAdvancedRule.GoodsClearingAcct : String [R/W]
GLAccountAdvancedRule.IncreasingAccount : String [R/W]
GLAccountAdvancedRule.InventoryAccount : String [R/W]
GLAccountAdvancedRule.InventoryOffsetProfitAndLossAccount : String [R/W]
GLAccountAdvancedRule.IsActive : BoYesNoEnum [R/W]
GLAccountAdvancedRule.ItemCode : String [R/W]
GLAccountAdvancedRule.ItemGroup : Long [R/W]
GLAccountAdvancedRule.NegativeInventoryAdjustmentAccount : String [R/W]
GLAccountAdvancedRule.NumberOfPeriods : Long [R/W]
GLAccountAdvancedRule.PAReturnAcct : String [R/W]
GLAccountAdvancedRule.Period : String [R/W]
GLAccountAdvancedRule.PeriodName : String [R/W]
GLAccountAdvancedRule.PriceDifferenceAcc : String [R/W]
GLAccountAdvancedRule.PurchaseAcct : String [R/W]
GLAccountAdvancedRule.PurchaseBalanceAccount : String [R/W]
GLAccountAdvancedRule.PurchaseCreditAcc : String [R/W]
GLAccountAdvancedRule.PurchaseOffsetAcct : String [R/W]
GLAccountAdvancedRule.ReturningAccount : String [R/W]
GLAccountAdvancedRule.RevenuesAccount : String [R/W]
GLAccountAdvancedRule.SalesCreditAcc : String [R/W]
GLAccountAdvancedRule.SalesCreditEUAcc : String [R/W]
GLAccountAdvancedRule.SalesCreditForeignAcc : String [R/W]
GLAccountAdvancedRule.ShippedGoodsAccount : String [R/W]
GLAccountAdvancedRule.ShipToCountry : String [R/W]
GLAccountAdvancedRule.ShipToState : String [R/W]
GLAccountAdvancedRule.StockInflationAdjustAccount : String [R/W]
GLAccountAdvancedRule.StockInflationOffsetAccount : String [R/W]
GLAccountAdvancedRule.StockInTransitAccount : String [R/W]
GLAccountAdvancedRule.SubPeriodType : BoSubPeriodTypeEnum [R/W]
GLAccountAdvancedRule.ToDate : Date [R/W]
GLAccountAdvancedRule.ToDocumentDate : Date [R/W]
GLAccountAdvancedRule.ToDueDate : Date [R/W]
GLAccountAdvancedRule.ToPostingDate : Date [R/W]
GLAccountAdvancedRule.TransferAccount : String [R/W]
GLAccountAdvancedRule.UDF1 : String [R/W]
GLAccountAdvancedRule.UDF2 : String [R/W]
GLAccountAdvancedRule.UDF3 : String [R/W]
GLAccountAdvancedRule.UDF4 : String [R/W]
GLAccountAdvancedRule.UDF5 : String [R/W]
GLAccountAdvancedRule.Usage : Long [R/W]
GLAccountAdvancedRule.VarienceAccount : String [R/W]
GLAccountAdvancedRule.VatGroup : String [R/W]
GLAccountAdvancedRule.VATInRevenueAccount : String [R/W]
GLAccountAdvancedRule.Warehouse : String [R/W]
GLAccountAdvancedRule.WHIncomingCenvatAccount : String [R/W]
GLAccountAdvancedRule.WHOutgoingCenvatAccount : String [R/W]
GLAccountAdvancedRule.WipAccount : String [R/W]
GLAccountAdvancedRule.WipOffsetProfitAndLossAccount : String [R/W]
GLAccountAdvancedRule.WipVarianceAccount : String [R/W]
GLAccountAdvancedRule.FromXMLFile(ByVal bstrFileName As String)
GLAccountAdvancedRule.FromXMLString(ByVal bstrXML As String)
GLAccountAdvancedRule.GetXMLSchema() -> String
GLAccountAdvancedRule.ToXMLFile(ByVal bstrFileName As String)
GLAccountAdvancedRule.ToXMLString() -> String
GLAccountAdvancedRuleParams.AbsoluteEntry : Long [R/W]
GLAccountAdvancedRuleParams.BPGroup : Long [R/W]
GLAccountAdvancedRuleParams.Code : String [R/W]
GLAccountAdvancedRuleParams.FederalTaxID : String [R/W]
GLAccountAdvancedRuleParams.ItemCode : String [R/W]
GLAccountAdvancedRuleParams.ItemGroup : Long [R/W]
GLAccountAdvancedRuleParams.Period : String [R/W]
GLAccountAdvancedRuleParams.ShipToCountry : String [R/W]
GLAccountAdvancedRuleParams.ShipToState : String [R/W]
GLAccountAdvancedRuleParams.Warehouse : String [R/W]
GLAccountAdvancedRuleParams.FromXMLFile(ByVal bstrFileName As String)
GLAccountAdvancedRuleParams.FromXMLString(ByVal bstrXML As String)
GLAccountAdvancedRuleParams.GetXMLSchema() -> String
GLAccountAdvancedRuleParams.ToXMLFile(ByVal bstrFileName As String)
GLAccountAdvancedRuleParams.ToXMLString() -> String
GLAccountAdvancedRuleParamsCollection.Count : Long [R]
GLAccountAdvancedRuleParamsCollection.Add() -> GLAccountAdvancedRuleParams
GLAccountAdvancedRuleParamsCollection.GetXMLSchema() -> String
GLAccountAdvancedRuleParamsCollection.Item(ByVal vtIndex As Variant) -> GLAccountAdvancedRuleParams
GLAccountAdvancedRuleParamsCollection.ToXMLFile(ByVal bstrFileName As String)
GLAccountAdvancedRuleParamsCollection.ToXMLString() -> String
GLAccountAdvancedRulesService.Add(ByVal pIGLAccountAdvancedRule As GLAccountAdvancedRule) -> GLAccountAdvancedRuleParams
GLAccountAdvancedRulesService.Delete(ByVal pIGLAccountAdvancedRuleParams As GLAccountAdvancedRuleParams)
GLAccountAdvancedRulesService.Get(ByVal pIGLAccountAdvancedRuleParams As GLAccountAdvancedRuleParams) -> GLAccountAdvancedRule
GLAccountAdvancedRulesService.GetDataInterface(ByVal enumMSDI As GLAccountAdvancedRulesServiceDataInterfaces) -> Object
GLAccountAdvancedRulesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
GLAccountAdvancedRulesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
GLAccountAdvancedRulesService.GetList() -> GLAccountAdvancedRuleParamsCollection
GLAccountAdvancedRulesService.Update(ByVal pIGLAccountAdvancedRule As GLAccountAdvancedRule)
GLAccounts.Count : Long [R]
GLAccounts.Add() -> GLAccount
GLAccounts.GetXMLSchema() -> String
GLAccounts.Item(ByVal vtIndex As Variant) -> GLAccount
GLAccounts.ToXMLFile(ByVal bstrFileName As String)
GLAccounts.ToXMLString() -> String
GovPayCode.AbsId : Long [R]
GovPayCode.Authorities : GovPayCodeAuthorities [R]
GovPayCode.Code : String [R/W]
GovPayCode.Description : String [R/W]
GovPayCode.Periodicity : GovPayCodePeriodicityEnum [R/W]
GovPayCode.StateTax : BoYesNoEnum [R/W]
GovPayCode.FromXMLFile(ByVal bstrFileName As String)
GovPayCode.FromXMLString(ByVal bstrXML As String)
GovPayCode.GetXMLSchema() -> String
GovPayCode.ToXMLFile(ByVal bstrFileName As String)
GovPayCode.ToXMLString() -> String
GovPayCodeAuthorities.Count : Long [R]
GovPayCodeAuthorities.Add() -> GovPayCodeAuthority
GovPayCodeAuthorities.GetXMLSchema() -> String
GovPayCodeAuthorities.Item(ByVal vtIndex As Variant) -> GovPayCodeAuthority
GovPayCodeAuthorities.Remove(ByVal vtIndex As Variant)
GovPayCodeAuthorities.ToXMLFile(ByVal bstrFileName As String)
GovPayCodeAuthorities.ToXMLString() -> String
GovPayCodeAuthority.AbsId : Long [R]
GovPayCodeAuthority.BPLID : Long [R/W]
GovPayCodeAuthority.CardCode : String [R/W]
GovPayCodeAuthority.State : String [R/W]
GovPayCodeAuthority.FromXMLFile(ByVal bstrFileName As String)
GovPayCodeAuthority.FromXMLString(ByVal bstrXML As String)
GovPayCodeAuthority.GetXMLSchema() -> String
GovPayCodeAuthority.ToXMLFile(ByVal bstrFileName As String)
GovPayCodeAuthority.ToXMLString() -> String
GovPayCodeParams.AbsId : Long [R/W]
GovPayCodeParams.Code : String [R/W]
GovPayCodeParams.FromXMLFile(ByVal bstrFileName As String)
GovPayCodeParams.FromXMLString(ByVal bstrXML As String)
GovPayCodeParams.GetXMLSchema() -> String
GovPayCodeParams.ToXMLFile(ByVal bstrFileName As String)
GovPayCodeParams.ToXMLString() -> String
GovPayCodeParamsCollection.Count : Long [R]
GovPayCodeParamsCollection.Add() -> GovPayCodeParams
GovPayCodeParamsCollection.GetXMLSchema() -> String
GovPayCodeParamsCollection.Item(ByVal vtIndex As Variant) -> GovPayCodeParams
GovPayCodeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
GovPayCodeParamsCollection.ToXMLString() -> String
GovPayCodesService.Add(ByVal pIGovPayCode As GovPayCode) -> GovPayCodeParams
GovPayCodesService.Delete(ByVal pIGovPayCodeParams As GovPayCodeParams)
GovPayCodesService.Get(ByVal pIGovPayCodeParams As GovPayCodeParams) -> GovPayCode
GovPayCodesService.GetDataInterface(ByVal enumMSDI As GovPayCodesServiceDataInterfaces) -> Object
GovPayCodesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
GovPayCodesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
GovPayCodesService.GetList() -> GovPayCodeParamsCollection
GovPayCodesService.Update(ByVal pIGovPayCode As GovPayCode)
GTIParams.AbsEntry : Long [R]
GTIParams.InboundFile : String [R/W]
GTIParams.FromXMLFile(ByVal bstrFileName As String)
GTIParams.FromXMLString(ByVal bstrXML As String)
GTIParams.GetXMLSchema() -> String
GTIParams.ToXMLFile(ByVal bstrFileName As String)
GTIParams.ToXMLString() -> String
GTIParamsCollection.Count : Long [R]
GTIParamsCollection.Add() -> GTIParams
GTIParamsCollection.GetXMLSchema() -> String
GTIParamsCollection.Item(ByVal vtIndex As Variant) -> GTIParams
GTIParamsCollection.ToXMLFile(ByVal bstrFileName As String)
GTIParamsCollection.ToXMLString() -> String
GTIsService.GetDataInterface(ByVal enumMSDI As GTIsServiceDataInterfaces) -> Object
GTIsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
GTIsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
GTIsService.Import(ByVal pIGTIParams As GTIParams) -> GTIParamsCollection
Holiday.HolidayCode : String [R/W]
Holiday.HolidayDates : HolidayDates [R]
Holiday.SetWeekendsAsWorkDays : String [R/W]
Holiday.ValidForOneYearOnly : BoYesNoEnum [R/W]
Holiday.WeekendFrom : BoWeekEnum [R/W]
Holiday.WeekendTO : BoWeekEnum [R/W]
Holiday.WeekNoRule : BoWeekNoRuleEnum [R/W]
Holiday.FromXMLFile(ByVal bstrFileName As String)
Holiday.FromXMLString(ByVal bstrXML As String)
Holiday.GetXMLSchema() -> String
Holiday.ToXMLFile(ByVal bstrFileName As String)
Holiday.ToXMLString() -> String
HolidayDate.EndDate : Date [R/W]
HolidayDate.HolidayCode : String [R/W]
HolidayDate.Remarks : String [R/W]
HolidayDate.StartDate : Date [R/W]
HolidayDate.FromXMLFile(ByVal bstrFileName As String)
HolidayDate.FromXMLString(ByVal bstrXML As String)
HolidayDate.GetXMLSchema() -> String
HolidayDate.ToXMLFile(ByVal bstrFileName As String)
HolidayDate.ToXMLString() -> String
HolidayDates.Count : Long [R]
HolidayDates.Add() -> HolidayDate
HolidayDates.GetXMLSchema() -> String
HolidayDates.Item(ByVal vtIndex As Variant) -> HolidayDate
HolidayDates.ToXMLFile(ByVal bstrFileName As String)
HolidayDates.ToXMLString() -> String
HolidayParams.HolidayCode : String [R/W]
HolidayParams.FromXMLFile(ByVal bstrFileName As String)
HolidayParams.FromXMLString(ByVal bstrXML As String)
HolidayParams.GetXMLSchema() -> String
HolidayParams.ToXMLFile(ByVal bstrFileName As String)
HolidayParams.ToXMLString() -> String
HolidayService.AddHoliday(ByVal pIHoliday As Holiday) -> HolidayParams
HolidayService.DeleteHoliday(ByVal pIHolidayParams As HolidayParams)
HolidayService.GetDataInterface(ByVal enumMSDI As HolidayServiceDataInterfaces) -> Object
HolidayService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
HolidayService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
HolidayService.GetHoliday(ByVal pIHolidayParams As HolidayParams) -> Holiday
HolidayService.GetHolidayList() -> HolidaysParams
HolidayService.UpdateHoliday(ByVal pIHoliday As Holiday)
HolidaysParams.Count : Long [R]
HolidaysParams.Add() -> HolidayParams
HolidaysParams.GetXMLSchema() -> String
HolidaysParams.Item(ByVal vtIndex As Variant) -> HolidayParams
HolidaysParams.ToXMLFile(ByVal bstrFileName As String)
HolidaysParams.ToXMLString() -> String
HouseBankAccounts.AbsoluteEntry : Long [R]
HouseBankAccounts.AccNo : String [R/W]
HouseBankAccounts.AccountCheckDigit : String [R/W]
HouseBankAccounts.AccountName : String [R/W]
HouseBankAccounts.AddressType : String [R/W]
HouseBankAccounts.AgreementNumber : String [R/W]
HouseBankAccounts.BankCode : String [R]
HouseBankAccounts.BankKey : Long [R/W]
HouseBankAccounts.BankonCollection : String [R/W]
HouseBankAccounts.BankonDiscounted : String [R/W]
HouseBankAccounts.BICSwiftCode : String [R/W]
HouseBankAccounts.BISR : BoYesNoEnum [R/W]
HouseBankAccounts.Block : String [R/W]
HouseBankAccounts.Branch : String [R/W]
HouseBankAccounts.BranchCheckDigit : String [R/W]
HouseBankAccounts.Browser : DataBrowser [R]
HouseBankAccounts.Building : String [R/W]
HouseBankAccounts.City : String [R/W]
HouseBankAccounts.CollectionCode : String [R/W]
HouseBankAccounts.ControlKey : String [R/W]
HouseBankAccounts.Country : String [R]
HouseBankAccounts.County : String [R/W]
HouseBankAccounts.CustomerIdNumber : String [R/W]
HouseBankAccounts.DaysInAdvance : Long [R/W]
HouseBankAccounts.DebtofDiscountedBillofExc : String [R/W]
HouseBankAccounts.DiscountAccount : String [R/W]
HouseBankAccounts.DiscountLimit : Double [R/W]
HouseBankAccounts.ECheck : BoYesNoEnum [R/W]
HouseBankAccounts.FileSeqNextNumber : Long [R/W]
HouseBankAccounts.FineAccount : String [R/W]
HouseBankAccounts.GLAccount : String [R/W]
HouseBankAccounts.GLInterimAccount : String [R/W]
HouseBankAccounts.IBAN : String [R/W]
HouseBankAccounts.ImportFileName : String [R/W]
HouseBankAccounts.IncomingPaymentSeries : Long [R/W]
HouseBankAccounts.InterestAccount : String [R/W]
HouseBankAccounts.IOFTaxAccount : String [R/W]
HouseBankAccounts.ISRBillerID : String [R/W]
HouseBankAccounts.ISRType : Long [R/W]
HouseBankAccounts.JournalEntrySeries : Long [R/W]
HouseBankAccounts.LockChecksPrinting : BoYesNoEnum [R/W]
HouseBankAccounts.MaxAmountofBillofExchan : Double [R/W]
HouseBankAccounts.MaximumLines : Long [R/W]
HouseBankAccounts.MinAmountofBillofExchang : Double [R/W]
HouseBankAccounts.NextCheckNo : Long [R/W]
HouseBankAccounts.NoValidationForStartingEndingBal : BoYesNoEnum [R/W]
HouseBankAccounts.OtherExpensesAccount : String [R/W]
HouseBankAccounts.OtherIncomesAccount : String [R/W]
HouseBankAccounts.OurNumber : Long [R/W]
HouseBankAccounts.OutgoingPaymentSeries : Long [R/W]
HouseBankAccounts.PrintOn : PrintOnEnum [R/W]
HouseBankAccounts.RetornoFileName : String [R/W]
HouseBankAccounts.ServiceFeeAccount : String [R/W]
HouseBankAccounts.State : String [R/W]
HouseBankAccounts.Street : String [R/W]
HouseBankAccounts.StreetNo : String [R/W]
HouseBankAccounts.TemplateName : String [R/W]
HouseBankAccounts.ToleranceDays : Long [R/W]
HouseBankAccounts.UserFields : UserFields [R]
HouseBankAccounts.UserNo1 : String [R/W]
HouseBankAccounts.UserNo2 : String [R/W]
HouseBankAccounts.UserNo3 : String [R/W]
HouseBankAccounts.UserNo4 : String [R/W]
HouseBankAccounts.ZipCode : String [R/W]
HouseBankAccounts.Add() -> Long
HouseBankAccounts.GetAsXML() -> String
HouseBankAccounts.GetByKey(ByVal lAbsEntry As Long) -> Boolean
HouseBankAccounts.Remove() -> Long
HouseBankAccounts.SaveToFile(ByVal bstrFileName As String)
HouseBankAccounts.SaveXML(ByRef pbstrFileName As String)
HouseBankAccounts.Update() -> Long
IdentificationCode.AbsEntry : Long [R]
IdentificationCode.Code : String [R/W]
IdentificationCode.Codelist : IdentificationCodeTypeEnum [R/W]
IdentificationCode.Description : String [R/W]
IdentificationCode.SchemaCode : String [R/W]
IdentificationCode.SchemaDesc : String [R/W]
IdentificationCode.FromXMLFile(ByVal bstrFileName As String)
IdentificationCode.FromXMLString(ByVal bstrXML As String)
IdentificationCode.GetXMLSchema() -> String
IdentificationCode.ToXMLFile(ByVal bstrFileName As String)
IdentificationCode.ToXMLString() -> String
IdentificationCodeParams.AbsEntry : Long [R/W]
IdentificationCodeParams.FromXMLFile(ByVal bstrFileName As String)
IdentificationCodeParams.FromXMLString(ByVal bstrXML As String)
IdentificationCodeParams.GetXMLSchema() -> String
IdentificationCodeParams.ToXMLFile(ByVal bstrFileName As String)
IdentificationCodeParams.ToXMLString() -> String
IdentificationCodes.Count : Long [R]
IdentificationCodes.Add() -> IdentificationCode
IdentificationCodes.GetXMLSchema() -> String
IdentificationCodes.Item(ByVal vtIndex As Variant) -> IdentificationCode
IdentificationCodes.ToXMLFile(ByVal bstrFileName As String)
IdentificationCodes.ToXMLString() -> String
IdentificationCodeService.Add(ByVal pIIdentificationCode As IdentificationCode) -> IdentificationCodeParams
IdentificationCodeService.GetByParams(ByVal pIIdentificationCodeParams As IdentificationCodeParams) -> IdentificationCode
IdentificationCodeService.GetDataInterface(ByVal enumMSDI As IdentificationCodeServiceDataInterfaces) -> Object
IdentificationCodeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
IdentificationCodeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
IdentificationCodeService.GetList() -> IdentificationCodes
IdentificationCodeService.Remove(ByVal pIIdentificationCodeParams As IdentificationCodeParams)
IdentificationCodeService.Update(ByVal pIIdentificationCode As IdentificationCode)
ImportDetermination.AbsEntry : Long [R]
ImportDetermination.Code : ElectronicDocProtocolCodeStrEnum [R/W]
ImportDetermination.DefaultDigitalSeries : Long [R/W]
ImportDetermination.FieldType : ImportFieldTypeEnum [R/W]
ImportDetermination.FieldTypeXPath : String [R/W]
ImportDetermination.ImportFormat : Long [R/W]
ImportDetermination.LineNumber : Long [R/W]
ImportDetermination.ObjectType : String [R/W]
ImportDetermination.ObjectTypeXPath : String [R/W]
ImportDetermination.FromXMLFile(ByVal bstrFileName As String)
ImportDetermination.FromXMLString(ByVal bstrXML As String)
ImportDetermination.GetXMLSchema() -> String
ImportDetermination.ToXMLFile(ByVal bstrFileName As String)
ImportDetermination.ToXMLString() -> String
ImportDeterminationParams.AbsEntry : Long [R/W]
ImportDeterminationParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
ImportDeterminationParams.ObjectType : String [R/W]
ImportDeterminationParams.FromXMLFile(ByVal bstrFileName As String)
ImportDeterminationParams.FromXMLString(ByVal bstrXML As String)
ImportDeterminationParams.GetXMLSchema() -> String
ImportDeterminationParams.ToXMLFile(ByVal bstrFileName As String)
ImportDeterminationParams.ToXMLString() -> String
ImportDeterminationsCollection.Count : Long [R]
ImportDeterminationsCollection.Add() -> ImportDetermination
ImportDeterminationsCollection.GetXMLSchema() -> String
ImportDeterminationsCollection.Item(ByVal vtIndex As Variant) -> ImportDetermination
ImportDeterminationsCollection.ToXMLFile(ByVal bstrFileName As String)
ImportDeterminationsCollection.ToXMLString() -> String
ImportDeterminationService.AddDetermination(ByVal pIImportDetermination As ImportDetermination)
ImportDeterminationService.DeleteDetermination(ByVal pIImportDeterminationParams As ImportDeterminationParams)
ImportDeterminationService.GetDataInterface(ByVal enumMSDI As ImportDeterminationServiceDataInterfaces) -> Object
ImportDeterminationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ImportDeterminationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ImportDeterminationService.GetDetermination(ByVal pIImportDeterminationParams As ImportDeterminationParams) -> ImportDetermination
ImportDeterminationService.GetDeterminations(ByVal pIImportDeterminationsParams As ImportDeterminationsParams) -> ImportDeterminationsCollection
ImportDeterminationService.UpdateDetermination(ByVal pIImportDetermination As ImportDetermination)
ImportDeterminationsParams.Code : ElectronicDocProtocolCodeStrEnum [R/W]
ImportDeterminationsParams.FromXMLFile(ByVal bstrFileName As String)
ImportDeterminationsParams.FromXMLString(ByVal bstrXML As String)
ImportDeterminationsParams.GetXMLSchema() -> String
ImportDeterminationsParams.ToXMLFile(ByVal bstrFileName As String)
ImportDeterminationsParams.ToXMLString() -> String
ImportFileParam.FilePath : String [R/W]
ImportFileParam.FromXMLFile(ByVal bstrFileName As String)
ImportFileParam.FromXMLString(ByVal bstrXML As String)
ImportFileParam.GetXMLSchema() -> String
ImportFileParam.ToXMLFile(ByVal bstrFileName As String)
ImportFileParam.ToXMLString() -> String
ImportProcesses.AdditionalFreightToNavyAuthority : Double [R/W]
ImportProcesses.AdditionalItemDiscountValue : Double [R/W]
ImportProcesses.AdditionalItemSequentialNumber : Long [R/W]
ImportProcesses.AdditionalNumber : String [R/W]
ImportProcesses.CustomsClearanceDate : Date [R/W]
ImportProcesses.DateOfRegistry_DI_DSI_DA : Date [R/W]
ImportProcesses.DrawbackRegimeConcessionAccountNumber : String [R/W]
ImportProcesses.DrawbackSuspensionRegime : String [R/W]
ImportProcesses.ImportationDocumentNumber : String [R/W]
ImportProcesses.ImportationDocumentTypeCode : String [R/W]
ImportProcesses.TypeOfImport : String [R/W]
IndiaHsn.AbsEntry : Long [R]
IndiaHsn.Chapter : String [R/W]
IndiaHsn.ChapterID : String [R]
IndiaHsn.Description : String [R/W]
IndiaHsn.Heading : String [R/W]
IndiaHsn.SubHeading : String [R/W]
IndiaHsn.FromXMLFile(ByVal bstrFileName As String)
IndiaHsn.FromXMLString(ByVal bstrXML As String)
IndiaHsn.GetXMLSchema() -> String
IndiaHsn.ToXMLFile(ByVal bstrFileName As String)
IndiaHsn.ToXMLString() -> String
IndiaHsnParams.AbsEntry : Long [R/W]
IndiaHsnParams.ChapterID : String [R]
IndiaHsnParams.FromXMLFile(ByVal bstrFileName As String)
IndiaHsnParams.FromXMLString(ByVal bstrXML As String)
IndiaHsnParams.GetXMLSchema() -> String
IndiaHsnParams.ToXMLFile(ByVal bstrFileName As String)
IndiaHsnParams.ToXMLString() -> String
IndiaHsnParamsCollection.Count : Long [R]
IndiaHsnParamsCollection.Add() -> IndiaHsnParams
IndiaHsnParamsCollection.GetXMLSchema() -> String
IndiaHsnParamsCollection.Item(ByVal vtIndex As Variant) -> IndiaHsnParams
IndiaHsnParamsCollection.ToXMLFile(ByVal bstrFileName As String)
IndiaHsnParamsCollection.ToXMLString() -> String
IndiaHsnService.Add(ByVal pIIndiaHsn As IndiaHsn) -> IndiaHsnParams
IndiaHsnService.Delete(ByVal pIIndiaHsnParams As IndiaHsnParams)
IndiaHsnService.Get(ByVal pIIndiaHsnParams As IndiaHsnParams) -> IndiaHsn
IndiaHsnService.GetDataInterface(ByVal enumMSDI As IndiaHsnServiceDataInterfaces) -> Object
IndiaHsnService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
IndiaHsnService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
IndiaHsnService.GetList() -> IndiaHsnParamsCollection
IndiaHsnService.Update(ByVal pIIndiaHsn As IndiaHsn)
IndiaSacCode.AbsEntry : Long [R]
IndiaSacCode.ServiceCode : String [R/W]
IndiaSacCode.ServiceName : String [R/W]
IndiaSacCode.FromXMLFile(ByVal bstrFileName As String)
IndiaSacCode.FromXMLString(ByVal bstrXML As String)
IndiaSacCode.GetXMLSchema() -> String
IndiaSacCode.ToXMLFile(ByVal bstrFileName As String)
IndiaSacCode.ToXMLString() -> String
IndiaSacCodeParams.AbsEntry : Long [R/W]
IndiaSacCodeParams.ServiceCode : String [R/W]
IndiaSacCodeParams.FromXMLFile(ByVal bstrFileName As String)
IndiaSacCodeParams.FromXMLString(ByVal bstrXML As String)
IndiaSacCodeParams.GetXMLSchema() -> String
IndiaSacCodeParams.ToXMLFile(ByVal bstrFileName As String)
IndiaSacCodeParams.ToXMLString() -> String
IndiaSacCodeParamsCollection.Count : Long [R]
IndiaSacCodeParamsCollection.Add() -> IndiaSacCodeParams
IndiaSacCodeParamsCollection.GetXMLSchema() -> String
IndiaSacCodeParamsCollection.Item(ByVal vtIndex As Variant) -> IndiaSacCodeParams
IndiaSacCodeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
IndiaSacCodeParamsCollection.ToXMLString() -> String
IndiaSacCodeService.Add(ByVal pIIndiaSacCode As IndiaSacCode) -> IndiaSacCodeParams
IndiaSacCodeService.Delete(ByVal pIIndiaSacCodeParams As IndiaSacCodeParams)
IndiaSacCodeService.Get(ByVal pIIndiaSacCodeParams As IndiaSacCodeParams) -> IndiaSacCode
IndiaSacCodeService.GetDataInterface(ByVal enumMSDI As IndiaSacCodeServiceDataInterfaces) -> Object
IndiaSacCodeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
IndiaSacCodeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
IndiaSacCodeService.GetList() -> IndiaSacCodeParamsCollection
IndiaSacCodeService.Update(ByVal pIIndiaSacCode As IndiaSacCode)
IndividualCounter.CounterID : Long [R/W]
IndividualCounter.CounterName : String [R]
IndividualCounter.CounterNumber : Long [R/W]
IndividualCounter.CounterType : CounterTypeEnum [R/W]
IndividualCounter.CounterVisualOrder : Long [R]
IndividualCounter.DocumentEntry : Long [R]
IndividualCounter.FromXMLFile(ByVal bstrFileName As String)
IndividualCounter.FromXMLString(ByVal bstrXML As String)
IndividualCounter.GetXMLSchema() -> String
IndividualCounter.ToXMLFile(ByVal bstrFileName As String)
IndividualCounter.ToXMLString() -> String
IndividualCounters.Count : Long [R]
IndividualCounters.Add() -> IndividualCounter
IndividualCounters.GetXMLSchema() -> String
IndividualCounters.Item(ByVal vtIndex As Variant) -> IndividualCounter
IndividualCounters.Remove(ByVal vtIndex As Variant)
IndividualCounters.ToXMLFile(ByVal bstrFileName As String)
IndividualCounters.ToXMLString() -> String
Industries.Browser : DataBrowser [R]
Industries.IndustryCode : Long [R]
Industries.IndustryDescription : String [R/W]
Industries.IndustryName : String [R/W]
Industries.UserFields : UserFields [R]
Industries.Add() -> Long
Industries.GetAsXML() -> String
Industries.GetByKey(ByVal Code As Long) -> Boolean
Industries.SaveToFile(ByVal FileName As String)
Industries.SaveXML(ByRef FileName As String)
Industries.Update() -> Long
IntegrationPackageConfigure.AbsEntry : Long [R]
IntegrationPackageConfigure.Code : String [R]
IntegrationPackageConfigure.IsEnable : BoYesNoEnum [R/W]
IntegrationPackageConfigure.Name : String [R]
IntegrationPackageConfigure.FromXMLFile(ByVal bstrFileName As String)
IntegrationPackageConfigure.FromXMLString(ByVal bstrXML As String)
IntegrationPackageConfigure.GetXMLSchema() -> String
IntegrationPackageConfigure.ToXMLFile(ByVal bstrFileName As String)
IntegrationPackageConfigure.ToXMLString() -> String
IntegrationPackageParams.Code : String [R/W]
IntegrationPackageParams.FromXMLFile(ByVal bstrFileName As String)
IntegrationPackageParams.FromXMLString(ByVal bstrXML As String)
IntegrationPackageParams.GetXMLSchema() -> String
IntegrationPackageParams.ToXMLFile(ByVal bstrFileName As String)
IntegrationPackageParams.ToXMLString() -> String
IntegrationPackagesConfigureService.Get(ByVal pIIntegrationPackageParams As IntegrationPackageParams) -> IntegrationPackageConfigure
IntegrationPackagesConfigureService.GetDataInterface(ByVal enumMSDI As IntegrationPackagesConfigureServiceDataInterfaces) -> Object
IntegrationPackagesConfigureService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
IntegrationPackagesConfigureService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
IntegrationPackagesConfigureService.GetList() -> IntegrationPackagesParams
IntegrationPackagesConfigureService.Update(ByVal pIIntegrationPackageConfigure As IntegrationPackageConfigure)
IntegrationPackagesParams.Count : Long [R]
IntegrationPackagesParams.Add() -> IntegrationPackageParams
IntegrationPackagesParams.GetXMLSchema() -> String
IntegrationPackagesParams.Item(ByVal vtIndex As Variant) -> IntegrationPackageParams
IntegrationPackagesParams.ToXMLFile(ByVal bstrFileName As String)
IntegrationPackagesParams.ToXMLString() -> String
InternalReconciliation.CancelAbs : Long [R]
InternalReconciliation.CardOrAccount : CardOrAccountEnum [R]
InternalReconciliation.ElectronicProtocols : ElectronicProtocolCollection [R]
InternalReconciliation.InternalReconciliationRows : InternalReconciliationRows [R]
InternalReconciliation.ReconDate : Date [R]
InternalReconciliation.ReconNum : Long [R]
InternalReconciliation.ReconType : ReconTypeEnum [R]
InternalReconciliation.Total : Double [R]
InternalReconciliation.FromXMLFile(ByVal bstrFileName As String)
InternalReconciliation.FromXMLString(ByVal bstrXML As String)
InternalReconciliation.GetXMLSchema() -> String
InternalReconciliation.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliation.ToXMLString() -> String
InternalReconciliationBP.BPCode : String [R/W]
InternalReconciliationBP.FromXMLFile(ByVal bstrFileName As String)
InternalReconciliationBP.FromXMLString(ByVal bstrXML As String)
InternalReconciliationBP.GetXMLSchema() -> String
InternalReconciliationBP.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationBP.ToXMLString() -> String
InternalReconciliationBPs.Count : Long [R]
InternalReconciliationBPs.Add() -> InternalReconciliationBP
InternalReconciliationBPs.GetXMLSchema() -> String
InternalReconciliationBPs.Item(ByVal vtIndex As Variant) -> InternalReconciliationBP
InternalReconciliationBPs.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationBPs.ToXMLString() -> String
InternalReconciliationOpenTrans.BPLID : Long [R/W]
InternalReconciliationOpenTrans.CardOrAccount : CardOrAccountEnum [R/W]
InternalReconciliationOpenTrans.ElectronicProtocols : ElectronicProtocolCollection [R]
InternalReconciliationOpenTrans.InternalReconciliationOpenTransRows : InternalReconciliationOpenTransRows [R]
InternalReconciliationOpenTrans.ReconDate : Date [R/W]
InternalReconciliationOpenTrans.FromXMLFile(ByVal bstrFileName As String)
InternalReconciliationOpenTrans.FromXMLString(ByVal bstrXML As String)
InternalReconciliationOpenTrans.GetXMLSchema() -> String
InternalReconciliationOpenTrans.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationOpenTrans.ToXMLString() -> String
InternalReconciliationOpenTransParams.AccountNo : String [R/W]
InternalReconciliationOpenTransParams.CardOrAccount : CardOrAccountEnum [R/W]
InternalReconciliationOpenTransParams.DateType : ReconSelectDateTypeEnum [R/W]
InternalReconciliationOpenTransParams.FromDate : Date [R/W]
InternalReconciliationOpenTransParams.InternalReconciliationBPs : InternalReconciliationBPs [R]
InternalReconciliationOpenTransParams.ReconDate : Date [R/W]
InternalReconciliationOpenTransParams.ToDate : Date [R/W]
InternalReconciliationOpenTransParams.FromXMLFile(ByVal bstrFileName As String)
InternalReconciliationOpenTransParams.FromXMLString(ByVal bstrXML As String)
InternalReconciliationOpenTransParams.GetXMLSchema() -> String
InternalReconciliationOpenTransParams.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationOpenTransParams.ToXMLString() -> String
InternalReconciliationOpenTransRow.CashDiscount : Double [R/W]
InternalReconciliationOpenTransRow.CreditOrDebit : CreditOrDebitEnum [R]
InternalReconciliationOpenTransRow.ReconcileAmount : Double [R/W]
InternalReconciliationOpenTransRow.Selected : BoYesNoEnum [R/W]
InternalReconciliationOpenTransRow.ShortName : String [R]
InternalReconciliationOpenTransRow.SrcObjAbs : Long [R]
InternalReconciliationOpenTransRow.SrcObjTyp : String [R]
InternalReconciliationOpenTransRow.TransId : Long [R/W]
InternalReconciliationOpenTransRow.TransRowId : Long [R/W]
InternalReconciliationOpenTransRow.FromXMLFile(ByVal bstrFileName As String)
InternalReconciliationOpenTransRow.FromXMLString(ByVal bstrXML As String)
InternalReconciliationOpenTransRow.GetXMLSchema() -> String
InternalReconciliationOpenTransRow.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationOpenTransRow.ToXMLString() -> String
InternalReconciliationOpenTransRows.Count : Long [R]
InternalReconciliationOpenTransRows.Add() -> InternalReconciliationOpenTransRow
InternalReconciliationOpenTransRows.GetXMLSchema() -> String
InternalReconciliationOpenTransRows.Item(ByVal vtIndex As Variant) -> InternalReconciliationOpenTransRow
InternalReconciliationOpenTransRows.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationOpenTransRows.ToXMLString() -> String
InternalReconciliationParams.ReconNum : Long [R/W]
InternalReconciliationParams.FromXMLFile(ByVal bstrFileName As String)
InternalReconciliationParams.FromXMLString(ByVal bstrXML As String)
InternalReconciliationParams.GetXMLSchema() -> String
InternalReconciliationParams.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationParams.ToXMLString() -> String
InternalReconciliationRow.CashDiscount : Double [R]
InternalReconciliationRow.CreditOrDebit : CreditOrDebitEnum [R]
InternalReconciliationRow.LineSeq : Long [R]
InternalReconciliationRow.ReconcileAmount : Double [R]
InternalReconciliationRow.ShortName : String [R]
InternalReconciliationRow.SrcObjAbs : Long [R]
InternalReconciliationRow.SrcObjTyp : String [R]
InternalReconciliationRow.TransId : Long [R]
InternalReconciliationRow.TransRowId : Long [R]
InternalReconciliationRow.FromXMLFile(ByVal bstrFileName As String)
InternalReconciliationRow.FromXMLString(ByVal bstrXML As String)
InternalReconciliationRow.GetXMLSchema() -> String
InternalReconciliationRow.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationRow.ToXMLString() -> String
InternalReconciliationRows.Count : Long [R]
InternalReconciliationRows.Add() -> InternalReconciliationRow
InternalReconciliationRows.GetXMLSchema() -> String
InternalReconciliationRows.Item(ByVal vtIndex As Variant) -> InternalReconciliationRow
InternalReconciliationRows.Remove(ByVal vtIndex As Variant)
InternalReconciliationRows.ToXMLFile(ByVal bstrFileName As String)
InternalReconciliationRows.ToXMLString() -> String
InternalReconciliationsService.Add(ByVal pIInternalReconciliationOpenTrans As InternalReconciliationOpenTrans) -> InternalReconciliationParams
InternalReconciliationsService.Cancel(ByVal pIInternalReconciliationParams As InternalReconciliationParams)
InternalReconciliationsService.Get(ByVal pIInternalReconciliationParams As InternalReconciliationParams) -> InternalReconciliation
InternalReconciliationsService.GetDataInterface(ByVal enumMSDI As InternalReconciliationsServiceDataInterfaces) -> Object
InternalReconciliationsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
InternalReconciliationsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
InternalReconciliationsService.GetOpenTransactions(ByVal pInternalReconciliationOpenTransParams As InternalReconciliationOpenTransParams) -> InternalReconciliationOpenTrans
InternalReconciliationsService.RequestApproveCancellation(ByVal pIInternalReconciliationParams As InternalReconciliationParams)
InternalReconciliationsService.Update(ByVal pIInternalReconciliation As InternalReconciliation)
IntrastatConfiguration.AbsEntry : Long [R]
IntrastatConfiguration.Code : String [R/W]
IntrastatConfiguration.ConfID : String [R]
IntrastatConfiguration.ConfType : IntrastatConfigurationEnum [R/W]
IntrastatConfiguration.Country : String [R/W]
IntrastatConfiguration.Description : String [R/W]
IntrastatConfiguration.PercentageValue : Double [R/W]
IntrastatConfiguration.StatisticalCode : String [R/W]
IntrastatConfiguration.SupplementaryUnit : Long [R/W]
IntrastatConfiguration.TriangDeal : IntrastatConfigurationTriangDealEnum [R/W]
IntrastatConfiguration.ValidExport : BoYesNoEnum [R/W]
IntrastatConfiguration.ValidFrom : Date [R/W]
IntrastatConfiguration.ValidImport : BoYesNoEnum [R/W]
IntrastatConfiguration.ValidTo : Date [R/W]
IntrastatConfiguration.FromXMLFile(ByVal bstrFileName As String)
IntrastatConfiguration.FromXMLString(ByVal bstrXML As String)
IntrastatConfiguration.GetXMLSchema() -> String
IntrastatConfiguration.ToXMLFile(ByVal bstrFileName As String)
IntrastatConfiguration.ToXMLString() -> String
IntrastatConfigurationCollectionParams.Count : Long [R]
IntrastatConfigurationCollectionParams.Add() -> IntrastatConfigurationParams
IntrastatConfigurationCollectionParams.GetXMLSchema() -> String
IntrastatConfigurationCollectionParams.Item(ByVal vtIndex As Variant) -> IntrastatConfigurationParams
IntrastatConfigurationCollectionParams.ToXMLFile(ByVal bstrFileName As String)
IntrastatConfigurationCollectionParams.ToXMLString() -> String
IntrastatConfigurationParams.AbsEntry : Long [R/W]
IntrastatConfigurationParams.Code : String [R/W]
IntrastatConfigurationParams.ConfType : IntrastatConfigurationEnum [R/W]
IntrastatConfigurationParams.Country : String [R/W]
IntrastatConfigurationParams.StatisticalCode : String [R/W]
IntrastatConfigurationParams.ValidFrom : Date [R/W]
IntrastatConfigurationParams.FromXMLFile(ByVal bstrFileName As String)
IntrastatConfigurationParams.FromXMLString(ByVal bstrXML As String)
IntrastatConfigurationParams.GetXMLSchema() -> String
IntrastatConfigurationParams.ToXMLFile(ByVal bstrFileName As String)
IntrastatConfigurationParams.ToXMLString() -> String
IntrastatConfigurationService.Add(ByVal pIIntrastatConfiguration As IntrastatConfiguration) -> IntrastatConfigurationParams
IntrastatConfigurationService.Delete(ByVal pIIntrastatConfigurationParams As IntrastatConfigurationParams)
IntrastatConfigurationService.Get(ByVal pIIntrastatConfigurationParams As IntrastatConfigurationParams) -> IntrastatConfiguration
IntrastatConfigurationService.GetDataInterface(ByVal enumMSDI As IntrastatConfigurationServiceDataInterfaces) -> Object
IntrastatConfigurationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
IntrastatConfigurationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
IntrastatConfigurationService.GetList() -> IntrastatConfigurationCollectionParams
IntrastatConfigurationService.Update(ByVal pIIntrastatConfiguration As IntrastatConfiguration)
InventoryCounting.AttachmentEntry : Long [R/W]
InventoryCounting.BranchID : Long [R/W]
InventoryCounting.CountDate : Date [R/W]
InventoryCounting.CountingType : CountingTypeEnum [R/W]
InventoryCounting.CountTime : Date [R/W]
InventoryCounting.DocObjectCodeEx : String [R]
InventoryCounting.DocumentEntry : Long [R]
InventoryCounting.DocumentNumber : Long [R]
InventoryCounting.DocumentReferences : InventoryCountingDocumentReferences [R]
InventoryCounting.DocumentStatus : CountingDocumentStatusEnum [R]
InventoryCounting.FinancialPeriod : Long [R]
InventoryCounting.IndividualCounters : IndividualCounters [R]
InventoryCounting.InventoryCountingLines : InventoryCountingLines [R]
InventoryCounting.PeriodIndicator : String [R]
InventoryCounting.Reference2 : String [R/W]
InventoryCounting.Remarks : String [R/W]
InventoryCounting.Series : Long [R/W]
InventoryCounting.SingleCounterID : Long [R/W]
InventoryCounting.SingleCounterType : CounterTypeEnum [R/W]
InventoryCounting.TeamCounters : TeamCounters [R]
InventoryCounting.UserFields : Fields [R]
InventoryCounting.YearEndDate : Date [R/W]
InventoryCounting.FromXMLFile(ByVal bstrFileName As String)
InventoryCounting.FromXMLString(ByVal bstrXML As String)
InventoryCounting.GetXMLSchema() -> String
InventoryCounting.ToXMLFile(ByVal bstrFileName As String)
InventoryCounting.ToXMLString() -> String
InventoryCountingBatchNumber.AddmisionDate : Date [R/W]
InventoryCountingBatchNumber.BaseLineNumber : Long [R/W]
InventoryCountingBatchNumber.BatchNumber : String [R/W]
InventoryCountingBatchNumber.CounterID : Long [R/W]
InventoryCountingBatchNumber.CounterType : CounterTypeEnum [R/W]
InventoryCountingBatchNumber.DocumentEntry : Long [R]
InventoryCountingBatchNumber.ExpiryDate : Date [R/W]
InventoryCountingBatchNumber.InternalSerialNumber : String [R/W]
InventoryCountingBatchNumber.Location : String [R/W]
InventoryCountingBatchNumber.ManufactureDate : Date [R/W]
InventoryCountingBatchNumber.ManufacturerSerialNumber : String [R/W]
InventoryCountingBatchNumber.MultipleCounterRole : MultipleCounterRoleEnum [R/W]
InventoryCountingBatchNumber.Notes : String [R/W]
InventoryCountingBatchNumber.Quantity : Double [R/W]
InventoryCountingBatchNumber.TrackingNote : Long [R/W]
InventoryCountingBatchNumber.TrackingNoteLine : Long [R/W]
InventoryCountingBatchNumber.FromXMLFile(ByVal bstrFileName As String)
InventoryCountingBatchNumber.FromXMLString(ByVal bstrXML As String)
InventoryCountingBatchNumber.GetXMLSchema() -> String
InventoryCountingBatchNumber.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingBatchNumber.ToXMLString() -> String
InventoryCountingBatchNumbers.Count : Long [R]
InventoryCountingBatchNumbers.Add() -> InventoryCountingBatchNumber
InventoryCountingBatchNumbers.GetXMLSchema() -> String
InventoryCountingBatchNumbers.Item(ByVal vtIndex As Variant) -> InventoryCountingBatchNumber
InventoryCountingBatchNumbers.Remove(ByVal vtIndex As Variant)
InventoryCountingBatchNumbers.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingBatchNumbers.ToXMLString() -> String
InventoryCountingDocumentReference.DocEntry : Long [R]
InventoryCountingDocumentReference.ExternalReferencedDocNumber : String [R/W]
InventoryCountingDocumentReference.IssueDate : Date [R/W]
InventoryCountingDocumentReference.LineNumber : Long [R]
InventoryCountingDocumentReference.ReferencedDocEntry : Long [R/W]
InventoryCountingDocumentReference.ReferencedDocNumber : Long [R]
InventoryCountingDocumentReference.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
InventoryCountingDocumentReference.Remark : String [R/W]
InventoryCountingDocumentReference.FromXMLFile(ByVal bstrFileName As String)
InventoryCountingDocumentReference.FromXMLString(ByVal bstrXML As String)
InventoryCountingDocumentReference.GetXMLSchema() -> String
InventoryCountingDocumentReference.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingDocumentReference.ToXMLString() -> String
InventoryCountingDocumentReferences.Count : Long [R]
InventoryCountingDocumentReferences.Add() -> InventoryCountingDocumentReference
InventoryCountingDocumentReferences.GetXMLSchema() -> String
InventoryCountingDocumentReferences.Item(ByVal vtIndex As Variant) -> InventoryCountingDocumentReference
InventoryCountingDocumentReferences.Remove(ByVal vtIndex As Variant)
InventoryCountingDocumentReferences.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingDocumentReferences.ToXMLString() -> String
InventoryCountingLine.BarCode : String [R/W]
InventoryCountingLine.BinEntry : Long [R/W]
InventoryCountingLine.CostingCode : String [R/W]
InventoryCountingLine.CostingCode2 : String [R/W]
InventoryCountingLine.CostingCode3 : String [R/W]
InventoryCountingLine.CostingCode4 : String [R/W]
InventoryCountingLine.CostingCode5 : String [R/W]
InventoryCountingLine.Counted : BoYesNoEnum [R/W]
InventoryCountingLine.CountedQuantity : Double [R/W]
InventoryCountingLine.CounterID : Long [R/W]
InventoryCountingLine.CounterType : CounterTypeEnum [R/W]
InventoryCountingLine.DocumentEntry : Long [R]
InventoryCountingLine.Freeze : BoYesNoEnum [R/W]
InventoryCountingLine.InventoryCountingBatchNumbers : InventoryCountingBatchNumbers [R]
InventoryCountingLine.InventoryCountingLineUoMs : InventoryCountingLineUoMs [R]
InventoryCountingLine.InventoryCountingSerialNumbers : InventoryCountingSerialNumbers [R]
InventoryCountingLine.InWarehouseQuantity : Double [R]
InventoryCountingLine.ItemCode : String [R/W]
InventoryCountingLine.ItemDescription : String [R/W]
InventoryCountingLine.ItemsPerUnit : Double [R]
InventoryCountingLine.LineNumber : Long [R/W]
InventoryCountingLine.LineStatus : CountingLineStatusEnum [R/W]
InventoryCountingLine.Manufacturer : Long [R/W]
InventoryCountingLine.MultipleCounterRole : MultipleCounterRoleEnum [R/W]
InventoryCountingLine.PreferredVendor : String [R/W]
InventoryCountingLine.ProjectCode : String [R/W]
InventoryCountingLine.Remarks : String [R/W]
InventoryCountingLine.SupplierCatalogNo : String [R/W]
InventoryCountingLine.TargetEntry : Long [R]
InventoryCountingLine.TargetLine : Long [R]
InventoryCountingLine.TargetReference : String [R]
InventoryCountingLine.TargetType : Long [R]
InventoryCountingLine.UoMCode : String [R/W]
InventoryCountingLine.UoMCountedQuantity : Double [R/W]
InventoryCountingLine.UserFields : Fields [R]
InventoryCountingLine.Variance : Double [R]
InventoryCountingLine.VariancePercentage : Double [R]
InventoryCountingLine.VisualOrder : Long [R]
InventoryCountingLine.WarehouseCode : String [R/W]
InventoryCountingLine.FromXMLFile(ByVal bstrFileName As String)
InventoryCountingLine.FromXMLString(ByVal bstrXML As String)
InventoryCountingLine.GetXMLSchema() -> String
InventoryCountingLine.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingLine.ToXMLString() -> String
InventoryCountingLines.Count : Long [R]
InventoryCountingLines.Add() -> InventoryCountingLine
InventoryCountingLines.GetXMLSchema() -> String
InventoryCountingLines.Item(ByVal vtIndex As Variant) -> InventoryCountingLine
InventoryCountingLines.Remove(ByVal vtIndex As Variant)
InventoryCountingLines.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingLines.ToXMLString() -> String
InventoryCountingLineUoM.BarCode : String [R/W]
InventoryCountingLineUoM.ChildNumber : Long [R]
InventoryCountingLineUoM.CountedQuantity : Double [R/W]
InventoryCountingLineUoM.CounterID : Long [R/W]
InventoryCountingLineUoM.CounterType : CounterTypeEnum [R/W]
InventoryCountingLineUoM.DocumentEntry : Long [R]
InventoryCountingLineUoM.ItemsPerUnit : Double [R]
InventoryCountingLineUoM.LineNumber : Long [R/W]
InventoryCountingLineUoM.MultipleCounterRole : MultipleCounterRoleEnum [R/W]
InventoryCountingLineUoM.UoMCode : String [R/W]
InventoryCountingLineUoM.UoMCountedQuantity : Double [R/W]
InventoryCountingLineUoM.UserFields : Fields [R]
InventoryCountingLineUoM.FromXMLFile(ByVal bstrFileName As String)
InventoryCountingLineUoM.FromXMLString(ByVal bstrXML As String)
InventoryCountingLineUoM.GetXMLSchema() -> String
InventoryCountingLineUoM.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingLineUoM.ToXMLString() -> String
InventoryCountingLineUoMs.Count : Long [R]
InventoryCountingLineUoMs.Add() -> InventoryCountingLineUoM
InventoryCountingLineUoMs.GetXMLSchema() -> String
InventoryCountingLineUoMs.Item(ByVal vtIndex As Variant) -> InventoryCountingLineUoM
InventoryCountingLineUoMs.Remove(ByVal vtIndex As Variant)
InventoryCountingLineUoMs.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingLineUoMs.ToXMLString() -> String
InventoryCountingParams.DocumentEntry : Long [R/W]
InventoryCountingParams.DocumentNumber : Long [R]
InventoryCountingParams.FromXMLFile(ByVal bstrFileName As String)
InventoryCountingParams.FromXMLString(ByVal bstrXML As String)
InventoryCountingParams.GetXMLSchema() -> String
InventoryCountingParams.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingParams.ToXMLString() -> String
InventoryCountingParamsCollection.Count : Long [R]
InventoryCountingParamsCollection.Add() -> InventoryCountingParams
InventoryCountingParamsCollection.GetXMLSchema() -> String
InventoryCountingParamsCollection.Item(ByVal vtIndex As Variant) -> InventoryCountingParams
InventoryCountingParamsCollection.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingParamsCollection.ToXMLString() -> String
InventoryCountingSerialNumber.BaseLineNumber : Long [R/W]
InventoryCountingSerialNumber.BatchID : String [R/W]
InventoryCountingSerialNumber.CounterID : Long [R/W]
InventoryCountingSerialNumber.CounterType : CounterTypeEnum [R/W]
InventoryCountingSerialNumber.DocumentEntry : Long [R]
InventoryCountingSerialNumber.ExpiryDate : Date [R/W]
InventoryCountingSerialNumber.InternalSerialNumber : String [R/W]
InventoryCountingSerialNumber.Location : String [R/W]
InventoryCountingSerialNumber.ManufactureDate : Date [R/W]
InventoryCountingSerialNumber.ManufacturerSerialNumber : String [R/W]
InventoryCountingSerialNumber.MultipleCounterRole : MultipleCounterRoleEnum [R/W]
InventoryCountingSerialNumber.Notes : String [R/W]
InventoryCountingSerialNumber.Quantity : Double [R/W]
InventoryCountingSerialNumber.ReceptionDate : Date [R/W]
InventoryCountingSerialNumber.SystemSerialNumber : Long [R/W]
InventoryCountingSerialNumber.TrackingNote : Long [R/W]
InventoryCountingSerialNumber.TrackingNoteLine : Long [R/W]
InventoryCountingSerialNumber.WarrantyEnd : Date [R/W]
InventoryCountingSerialNumber.WarrantyStart : Date [R/W]
InventoryCountingSerialNumber.FromXMLFile(ByVal bstrFileName As String)
InventoryCountingSerialNumber.FromXMLString(ByVal bstrXML As String)
InventoryCountingSerialNumber.GetXMLSchema() -> String
InventoryCountingSerialNumber.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingSerialNumber.ToXMLString() -> String
InventoryCountingSerialNumbers.Count : Long [R]
InventoryCountingSerialNumbers.Add() -> InventoryCountingSerialNumber
InventoryCountingSerialNumbers.GetXMLSchema() -> String
InventoryCountingSerialNumbers.Item(ByVal vtIndex As Variant) -> InventoryCountingSerialNumber
InventoryCountingSerialNumbers.Remove(ByVal vtIndex As Variant)
InventoryCountingSerialNumbers.ToXMLFile(ByVal bstrFileName As String)
InventoryCountingSerialNumbers.ToXMLString() -> String
InventoryCountingsService.Add(ByVal pIInventoryCounting As InventoryCounting) -> InventoryCountingParams
InventoryCountingsService.Close(ByVal pIInventoryCountingParams As InventoryCountingParams)
InventoryCountingsService.Get(ByVal pIInventoryCountingParams As InventoryCountingParams) -> InventoryCounting
InventoryCountingsService.GetDataInterface(ByVal enumMSDI As InventoryCountingsServiceDataInterfaces) -> Object
InventoryCountingsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
InventoryCountingsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
InventoryCountingsService.GetList() -> InventoryCountingParamsCollection
InventoryCountingsService.Update(ByVal pIInventoryCounting As InventoryCounting)
InventoryCycles.Browser : DataBrowser [R]
InventoryCycles.CycleCode : Long [R]
InventoryCycles.CycleName : String [R/W]
InventoryCycles.Day : Long [R/W]
InventoryCycles.endType : EndTypeEnum [R/W]
InventoryCycles.Frequency : BoFrequency [R/W]
InventoryCycles.Friday : BoYesNoEnum [R/W]
InventoryCycles.Hour : Date [R/W]
InventoryCycles.Interval : Long [R/W]
InventoryCycles.MaxOccurrence : Long [R/W]
InventoryCycles.Monday : BoYesNoEnum [R/W]
InventoryCycles.NextCountingDate : Date [R/W]
InventoryCycles.RecurrenceDayInMonth : Long [R/W]
InventoryCycles.RecurrenceDayOfWeek : RecurrenceDayOfWeekEnum [R/W]
InventoryCycles.RecurrenceMonth : Long [R/W]
InventoryCycles.RecurrenceSequenceSpecifier : RecurrenceSequenceSpecifierEnum [R/W]
InventoryCycles.RepeatOption : RepeatOptionEnum [R/W]
InventoryCycles.Saturday : BoYesNoEnum [R/W]
InventoryCycles.SeriesEndDate : Date [R/W]
InventoryCycles.Sunday : BoYesNoEnum [R/W]
InventoryCycles.Thursday : BoYesNoEnum [R/W]
InventoryCycles.Tuesday : BoYesNoEnum [R/W]
InventoryCycles.UserFields : UserFields [R]
InventoryCycles.Wednesday : BoYesNoEnum [R/W]
InventoryCycles.Add() -> Long
InventoryCycles.GetAsXML() -> String
InventoryCycles.GetByKey(ByVal lCode As Long) -> Boolean
InventoryCycles.Remove() -> Long
InventoryCycles.SaveToFile(ByVal bstrFileName As String)
InventoryCycles.SaveXML(ByRef pbstrFileName As String)
InventoryCycles.Update() -> Long
InventoryOpeningBalance.AttachmentEntry : Long [R/W]
InventoryOpeningBalance.BranchID : Long [R/W]
InventoryOpeningBalance.DocObjectCodeEx : String [R]
InventoryOpeningBalance.DocumentDate : Date [R/W]
InventoryOpeningBalance.DocumentEntry : Long [R]
InventoryOpeningBalance.DocumentNumber : Long [R]
InventoryOpeningBalance.FinancialPeriod : Long [R]
InventoryOpeningBalance.InventoryOpeningBalanceLines : InventoryOpeningBalanceLines [R]
InventoryOpeningBalance.JournalRemark : String [R/W]
InventoryOpeningBalance.PeriodIndicator : String [R]
InventoryOpeningBalance.PostingDate : Date [R/W]
InventoryOpeningBalance.PriceList : Long [R/W]
InventoryOpeningBalance.PriceSource : InventoryOpeningBalancePriceSourceEnum [R/W]
InventoryOpeningBalance.Reference2 : String [R/W]
InventoryOpeningBalance.Remarks : String [R/W]
InventoryOpeningBalance.Series : Long [R/W]
InventoryOpeningBalance.UserFields : Fields [R]
InventoryOpeningBalance.FromXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalance.FromXMLString(ByVal bstrXML As String)
InventoryOpeningBalance.GetXMLSchema() -> String
InventoryOpeningBalance.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalance.ToXMLString() -> String
InventoryOpeningBalanceBatchNumber.AddmisionDate : Date [R/W]
InventoryOpeningBalanceBatchNumber.BaseLineNumber : Long [R/W]
InventoryOpeningBalanceBatchNumber.BatchNumber : String [R/W]
InventoryOpeningBalanceBatchNumber.DocumentEntry : Long [R]
InventoryOpeningBalanceBatchNumber.ExpiryDate : Date [R/W]
InventoryOpeningBalanceBatchNumber.InternalSerialNumber : String [R/W]
InventoryOpeningBalanceBatchNumber.Location : String [R/W]
InventoryOpeningBalanceBatchNumber.ManufactureDate : Date [R/W]
InventoryOpeningBalanceBatchNumber.ManufacturerSerialNumber : String [R/W]
InventoryOpeningBalanceBatchNumber.Notes : String [R/W]
InventoryOpeningBalanceBatchNumber.Quantity : Double [R/W]
InventoryOpeningBalanceBatchNumber.TrackingNote : Long [R/W]
InventoryOpeningBalanceBatchNumber.TrackingNoteLine : Long [R/W]
InventoryOpeningBalanceBatchNumber.FromXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceBatchNumber.FromXMLString(ByVal bstrXML As String)
InventoryOpeningBalanceBatchNumber.GetXMLSchema() -> String
InventoryOpeningBalanceBatchNumber.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceBatchNumber.ToXMLString() -> String
InventoryOpeningBalanceBatchNumbers.Count : Long [R]
InventoryOpeningBalanceBatchNumbers.Add() -> InventoryOpeningBalanceBatchNumber
InventoryOpeningBalanceBatchNumbers.GetXMLSchema() -> String
InventoryOpeningBalanceBatchNumbers.Item(ByVal vtIndex As Variant) -> InventoryOpeningBalanceBatchNumber
InventoryOpeningBalanceBatchNumbers.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceBatchNumbers.ToXMLString() -> String
InventoryOpeningBalanceCCDNumber.BaseLineNumber : Long [R/W]
InventoryOpeningBalanceCCDNumber.CCDNumber : String [R/W]
InventoryOpeningBalanceCCDNumber.ChildNumber : Long [R/W]
InventoryOpeningBalanceCCDNumber.CountryOfOrigin : String [R/W]
InventoryOpeningBalanceCCDNumber.DocumentEntry : Long [R]
InventoryOpeningBalanceCCDNumber.Quantity : Double [R/W]
InventoryOpeningBalanceCCDNumber.SubLineNumber : Long [R/W]
InventoryOpeningBalanceCCDNumber.TrackingNote : Long [R/W]
InventoryOpeningBalanceCCDNumber.TrackingNoteLine : Long [R/W]
InventoryOpeningBalanceCCDNumber.FromXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceCCDNumber.FromXMLString(ByVal bstrXML As String)
InventoryOpeningBalanceCCDNumber.GetXMLSchema() -> String
InventoryOpeningBalanceCCDNumber.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceCCDNumber.ToXMLString() -> String
InventoryOpeningBalanceCCDNumbers.Count : Long [R]
InventoryOpeningBalanceCCDNumbers.Add() -> InventoryOpeningBalanceCCDNumber
InventoryOpeningBalanceCCDNumbers.GetXMLSchema() -> String
InventoryOpeningBalanceCCDNumbers.Item(ByVal vtIndex As Variant) -> InventoryOpeningBalanceCCDNumber
InventoryOpeningBalanceCCDNumbers.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceCCDNumbers.ToXMLString() -> String
InventoryOpeningBalanceLine.ActualPrice : Double [R]
InventoryOpeningBalanceLine.AllowBinNegativeQuantity : BoYesNoEnum [R/W]
InventoryOpeningBalanceLine.BarCode : String [R/W]
InventoryOpeningBalanceLine.BinEntry : Long [R/W]
InventoryOpeningBalanceLine.CostingCode : String [R/W]
InventoryOpeningBalanceLine.CostingCode2 : String [R/W]
InventoryOpeningBalanceLine.CostingCode3 : String [R/W]
InventoryOpeningBalanceLine.CostingCode4 : String [R/W]
InventoryOpeningBalanceLine.CostingCode5 : String [R/W]
InventoryOpeningBalanceLine.Currency : String [R/W]
InventoryOpeningBalanceLine.DocumentEntry : Long [R]
InventoryOpeningBalanceLine.InventoryOpeningBalanceBatchNumbers : InventoryOpeningBalanceBatchNumbers [R]
InventoryOpeningBalanceLine.InventoryOpeningBalanceCCDNumbers : InventoryOpeningBalanceCCDNumbers [R]
InventoryOpeningBalanceLine.InventoryOpeningBalanceSerialNumbers : InventoryOpeningBalanceSerialNumbers [R]
InventoryOpeningBalanceLine.InWarehouseQuantity : Double [R]
InventoryOpeningBalanceLine.ItemCode : String [R/W]
InventoryOpeningBalanceLine.ItemDescription : String [R/W]
InventoryOpeningBalanceLine.LineNumber : Long [R/W]
InventoryOpeningBalanceLine.Manufacturer : Long [R/W]
InventoryOpeningBalanceLine.OpeningBalance : Double [R/W]
InventoryOpeningBalanceLine.OpenInventoryAccount : String [R/W]
InventoryOpeningBalanceLine.PostedValueLC : Double [R]
InventoryOpeningBalanceLine.PostedValueSC : Double [R]
InventoryOpeningBalanceLine.PreferredVendor : String [R/W]
InventoryOpeningBalanceLine.Price : Double [R/W]
InventoryOpeningBalanceLine.ProjectCode : String [R/W]
InventoryOpeningBalanceLine.Remarks : String [R/W]
InventoryOpeningBalanceLine.SupplierCatalogNo : String [R/W]
InventoryOpeningBalanceLine.Total : Double [R]
InventoryOpeningBalanceLine.UserFields : Fields [R]
InventoryOpeningBalanceLine.VisualOrder : Long [R]
InventoryOpeningBalanceLine.WarehouseCode : String [R/W]
InventoryOpeningBalanceLine.FromXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceLine.FromXMLString(ByVal bstrXML As String)
InventoryOpeningBalanceLine.GetXMLSchema() -> String
InventoryOpeningBalanceLine.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceLine.ToXMLString() -> String
InventoryOpeningBalanceLines.Count : Long [R]
InventoryOpeningBalanceLines.Add() -> InventoryOpeningBalanceLine
InventoryOpeningBalanceLines.GetXMLSchema() -> String
InventoryOpeningBalanceLines.Item(ByVal vtIndex As Variant) -> InventoryOpeningBalanceLine
InventoryOpeningBalanceLines.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceLines.ToXMLString() -> String
InventoryOpeningBalanceParams.DocumentEntry : Long [R/W]
InventoryOpeningBalanceParams.DocumentNumber : Long [R]
InventoryOpeningBalanceParams.FromXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceParams.FromXMLString(ByVal bstrXML As String)
InventoryOpeningBalanceParams.GetXMLSchema() -> String
InventoryOpeningBalanceParams.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceParams.ToXMLString() -> String
InventoryOpeningBalanceParamsCollection.Count : Long [R]
InventoryOpeningBalanceParamsCollection.Add() -> InventoryOpeningBalanceParams
InventoryOpeningBalanceParamsCollection.GetXMLSchema() -> String
InventoryOpeningBalanceParamsCollection.Item(ByVal vtIndex As Variant) -> InventoryOpeningBalanceParams
InventoryOpeningBalanceParamsCollection.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceParamsCollection.ToXMLString() -> String
InventoryOpeningBalanceSerialNumber.BaseLineNumber : Long [R/W]
InventoryOpeningBalanceSerialNumber.BatchID : String [R/W]
InventoryOpeningBalanceSerialNumber.DocumentEntry : Long [R]
InventoryOpeningBalanceSerialNumber.ExpiryDate : Date [R/W]
InventoryOpeningBalanceSerialNumber.InternalSerialNumber : String [R/W]
InventoryOpeningBalanceSerialNumber.Location : String [R/W]
InventoryOpeningBalanceSerialNumber.ManufactureDate : Date [R/W]
InventoryOpeningBalanceSerialNumber.ManufacturerSerialNumber : String [R/W]
InventoryOpeningBalanceSerialNumber.Notes : String [R/W]
InventoryOpeningBalanceSerialNumber.Quantity : Double [R/W]
InventoryOpeningBalanceSerialNumber.ReceptionDate : Date [R/W]
InventoryOpeningBalanceSerialNumber.SystemSerialNumber : Long [R/W]
InventoryOpeningBalanceSerialNumber.TrackingNote : Long [R/W]
InventoryOpeningBalanceSerialNumber.TrackingNoteLine : Long [R/W]
InventoryOpeningBalanceSerialNumber.WarrantyEnd : Date [R/W]
InventoryOpeningBalanceSerialNumber.WarrantyStart : Date [R/W]
InventoryOpeningBalanceSerialNumber.FromXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceSerialNumber.FromXMLString(ByVal bstrXML As String)
InventoryOpeningBalanceSerialNumber.GetXMLSchema() -> String
InventoryOpeningBalanceSerialNumber.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceSerialNumber.ToXMLString() -> String
InventoryOpeningBalanceSerialNumbers.Count : Long [R]
InventoryOpeningBalanceSerialNumbers.Add() -> InventoryOpeningBalanceSerialNumber
InventoryOpeningBalanceSerialNumbers.GetXMLSchema() -> String
InventoryOpeningBalanceSerialNumbers.Item(ByVal vtIndex As Variant) -> InventoryOpeningBalanceSerialNumber
InventoryOpeningBalanceSerialNumbers.ToXMLFile(ByVal bstrFileName As String)
InventoryOpeningBalanceSerialNumbers.ToXMLString() -> String
InventoryOpeningBalancesService.Add(ByVal pIInventoryOpeningBalance As InventoryOpeningBalance) -> InventoryOpeningBalanceParams
InventoryOpeningBalancesService.Get(ByVal pIInventoryOpeningBalanceParams As InventoryOpeningBalanceParams) -> InventoryOpeningBalance
InventoryOpeningBalancesService.GetDataInterface(ByVal enumMSDI As InventoryOpeningBalancesServiceDataInterfaces) -> Object
InventoryOpeningBalancesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
InventoryOpeningBalancesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
InventoryOpeningBalancesService.GetList() -> InventoryOpeningBalanceParamsCollection
InventoryOpeningBalancesService.Update(ByVal pIInventoryOpeningBalance As InventoryOpeningBalance)
InventoryPosting.AttachmentEntry : Long [R/W]
InventoryPosting.BranchID : Long [R/W]
InventoryPosting.CountDate : Date [R/W]
InventoryPosting.CountTime : Date [R/W]
InventoryPosting.DocObjectCodeEx : String [R]
InventoryPosting.DocumentEntry : Long [R]
InventoryPosting.DocumentNumber : Long [R]
InventoryPosting.DocumentReferences : InventoryPostingDocumentReferences [R]
InventoryPosting.FinancialPeriod : Long [R]
InventoryPosting.InventoryPostingLines : InventoryPostingLines [R]
InventoryPosting.JournalRemark : String [R/W]
InventoryPosting.PeriodIndicator : String [R]
InventoryPosting.PostingDate : Date [R/W]
InventoryPosting.PriceList : Long [R/W]
InventoryPosting.PriceSource : InventoryPostingPriceSourceEnum [R/W]
InventoryPosting.Reference2 : String [R/W]
InventoryPosting.Remarks : String [R/W]
InventoryPosting.Series : Long [R/W]
InventoryPosting.UserFields : Fields [R]
InventoryPosting.YearEndDate : Date [R/W]
InventoryPosting.FromXMLFile(ByVal bstrFileName As String)
InventoryPosting.FromXMLString(ByVal bstrXML As String)
InventoryPosting.GetXMLSchema() -> String
InventoryPosting.ToXMLFile(ByVal bstrFileName As String)
InventoryPosting.ToXMLString() -> String
InventoryPostingBatchNumber.AddmisionDate : Date [R/W]
InventoryPostingBatchNumber.BaseLineNumber : Long [R/W]
InventoryPostingBatchNumber.BatchNumber : String [R/W]
InventoryPostingBatchNumber.DocumentEntry : Long [R]
InventoryPostingBatchNumber.ExpiryDate : Date [R/W]
InventoryPostingBatchNumber.InternalSerialNumber : String [R/W]
InventoryPostingBatchNumber.Location : String [R/W]
InventoryPostingBatchNumber.ManufactureDate : Date [R/W]
InventoryPostingBatchNumber.ManufacturerSerialNumber : String [R/W]
InventoryPostingBatchNumber.Notes : String [R/W]
InventoryPostingBatchNumber.Quantity : Double [R/W]
InventoryPostingBatchNumber.TrackingNote : Long [R/W]
InventoryPostingBatchNumber.TrackingNoteLine : Long [R/W]
InventoryPostingBatchNumber.FromXMLFile(ByVal bstrFileName As String)
InventoryPostingBatchNumber.FromXMLString(ByVal bstrXML As String)
InventoryPostingBatchNumber.GetXMLSchema() -> String
InventoryPostingBatchNumber.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingBatchNumber.ToXMLString() -> String
InventoryPostingBatchNumbers.Count : Long [R]
InventoryPostingBatchNumbers.Add() -> InventoryPostingBatchNumber
InventoryPostingBatchNumbers.GetXMLSchema() -> String
InventoryPostingBatchNumbers.Item(ByVal vtIndex As Variant) -> InventoryPostingBatchNumber
InventoryPostingBatchNumbers.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingBatchNumbers.ToXMLString() -> String
InventoryPostingCCDNumber.BaseLineNumber : Long [R/W]
InventoryPostingCCDNumber.CCDNumber : String [R/W]
InventoryPostingCCDNumber.ChildNumber : Long [R/W]
InventoryPostingCCDNumber.CountryOfOrigin : String [R/W]
InventoryPostingCCDNumber.DocumentEntry : Long [R]
InventoryPostingCCDNumber.Quantity : Double [R/W]
InventoryPostingCCDNumber.SubLineNumber : Long [R/W]
InventoryPostingCCDNumber.TrackingNote : Long [R/W]
InventoryPostingCCDNumber.TrackingNoteLine : Long [R/W]
InventoryPostingCCDNumber.FromXMLFile(ByVal bstrFileName As String)
InventoryPostingCCDNumber.FromXMLString(ByVal bstrXML As String)
InventoryPostingCCDNumber.GetXMLSchema() -> String
InventoryPostingCCDNumber.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingCCDNumber.ToXMLString() -> String
InventoryPostingCCDNumbers.Count : Long [R]
InventoryPostingCCDNumbers.Add() -> InventoryPostingCCDNumber
InventoryPostingCCDNumbers.GetXMLSchema() -> String
InventoryPostingCCDNumbers.Item(ByVal vtIndex As Variant) -> InventoryPostingCCDNumber
InventoryPostingCCDNumbers.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingCCDNumbers.ToXMLString() -> String
InventoryPostingCopyOption.BaseEntry : Long [R/W]
InventoryPostingCopyOption.CopyOption : InventoryPostingCopyOptionEnum [R/W]
InventoryPostingCopyOption.FromXMLFile(ByVal bstrFileName As String)
InventoryPostingCopyOption.FromXMLString(ByVal bstrXML As String)
InventoryPostingCopyOption.GetXMLSchema() -> String
InventoryPostingCopyOption.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingCopyOption.ToXMLString() -> String
InventoryPostingDocumentReference.DocEntry : Long [R]
InventoryPostingDocumentReference.ExternalReferencedDocNumber : String [R/W]
InventoryPostingDocumentReference.IssueDate : Date [R/W]
InventoryPostingDocumentReference.LineNumber : Long [R]
InventoryPostingDocumentReference.ReferencedDocEntry : Long [R/W]
InventoryPostingDocumentReference.ReferencedDocNumber : Long [R]
InventoryPostingDocumentReference.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
InventoryPostingDocumentReference.Remark : String [R/W]
InventoryPostingDocumentReference.FromXMLFile(ByVal bstrFileName As String)
InventoryPostingDocumentReference.FromXMLString(ByVal bstrXML As String)
InventoryPostingDocumentReference.GetXMLSchema() -> String
InventoryPostingDocumentReference.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingDocumentReference.ToXMLString() -> String
InventoryPostingDocumentReferences.Count : Long [R]
InventoryPostingDocumentReferences.Add() -> InventoryPostingDocumentReference
InventoryPostingDocumentReferences.GetXMLSchema() -> String
InventoryPostingDocumentReferences.Item(ByVal vtIndex As Variant) -> InventoryPostingDocumentReference
InventoryPostingDocumentReferences.Remove(ByVal vtIndex As Variant)
InventoryPostingDocumentReferences.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingDocumentReferences.ToXMLString() -> String
InventoryPostingLine.ActualPrice : Double [R]
InventoryPostingLine.AllowBinNegativeQuantity : BoYesNoEnum [R/W]
InventoryPostingLine.BarCode : String [R/W]
InventoryPostingLine.BaseEntry : Long [R/W]
InventoryPostingLine.BaseLine : Long [R/W]
InventoryPostingLine.BaseReference : String [R/W]
InventoryPostingLine.BaseType : Long [R/W]
InventoryPostingLine.BinEntry : Long [R/W]
InventoryPostingLine.CostingCode : String [R/W]
InventoryPostingLine.CostingCode2 : String [R/W]
InventoryPostingLine.CostingCode3 : String [R/W]
InventoryPostingLine.CostingCode4 : String [R/W]
InventoryPostingLine.CostingCode5 : String [R/W]
InventoryPostingLine.CountDate : Date [R/W]
InventoryPostingLine.CountedQuantity : Double [R/W]
InventoryPostingLine.CountTime : Date [R/W]
InventoryPostingLine.Currency : String [R/W]
InventoryPostingLine.DocumentEntry : Long [R]
InventoryPostingLine.InventoryOffsetDecreaseAccount : String [R/W]
InventoryPostingLine.InventoryOffsetIncreaseAccount : String [R/W]
InventoryPostingLine.InventoryPostingBatchNumbers : InventoryPostingBatchNumbers [R]
InventoryPostingLine.InventoryPostingCCDNumbers : InventoryPostingCCDNumbers [R]
InventoryPostingLine.InventoryPostingLineUoMs : InventoryPostingLineUoMs [R]
InventoryPostingLine.InventoryPostingSerialNumbers : InventoryPostingSerialNumbers [R]
InventoryPostingLine.InWarehouseQuantity : Double [R]
InventoryPostingLine.ItemCode : String [R/W]
InventoryPostingLine.ItemDescription : String [R/W]
InventoryPostingLine.ItemsPerUnit : Double [R]
InventoryPostingLine.LineNumber : Long [R/W]
InventoryPostingLine.Manufacturer : Long [R/W]
InventoryPostingLine.PostedValueLC : Double [R]
InventoryPostingLine.PostedValueSC : Double [R]
InventoryPostingLine.PreferredVendor : String [R/W]
InventoryPostingLine.Price : Double [R/W]
InventoryPostingLine.ProjectCode : String [R/W]
InventoryPostingLine.Remarks : String [R/W]
InventoryPostingLine.SupplierCatalogNo : String [R/W]
InventoryPostingLine.Total : Double [R]
InventoryPostingLine.UoMCode : String [R/W]
InventoryPostingLine.UoMCountedQuantity : Double [R/W]
InventoryPostingLine.UserFields : Fields [R]
InventoryPostingLine.Variance : Double [R/W]
InventoryPostingLine.VariancePercentage : Double [R]
InventoryPostingLine.VisualOrder : Long [R]
InventoryPostingLine.WarehouseCode : String [R/W]
InventoryPostingLine.FromXMLFile(ByVal bstrFileName As String)
InventoryPostingLine.FromXMLString(ByVal bstrXML As String)
InventoryPostingLine.GetXMLSchema() -> String
InventoryPostingLine.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingLine.ToXMLString() -> String
InventoryPostingLines.Count : Long [R]
InventoryPostingLines.Add() -> InventoryPostingLine
InventoryPostingLines.GetXMLSchema() -> String
InventoryPostingLines.Item(ByVal vtIndex As Variant) -> InventoryPostingLine
InventoryPostingLines.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingLines.ToXMLString() -> String
InventoryPostingLineUoM.BarCode : String [R/W]
InventoryPostingLineUoM.ChildNumber : Long [R]
InventoryPostingLineUoM.CountedQuantity : Double [R/W]
InventoryPostingLineUoM.DocumentEntry : Long [R]
InventoryPostingLineUoM.ItemsPerUnit : Double [R]
InventoryPostingLineUoM.LineNumber : Long [R]
InventoryPostingLineUoM.UoMCode : String [R/W]
InventoryPostingLineUoM.UoMCountedQuantity : Double [R/W]
InventoryPostingLineUoM.UserFields : Fields [R]
InventoryPostingLineUoM.FromXMLFile(ByVal bstrFileName As String)
InventoryPostingLineUoM.FromXMLString(ByVal bstrXML As String)
InventoryPostingLineUoM.GetXMLSchema() -> String
InventoryPostingLineUoM.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingLineUoM.ToXMLString() -> String
InventoryPostingLineUoMs.Count : Long [R]
InventoryPostingLineUoMs.Add() -> InventoryPostingLineUoM
InventoryPostingLineUoMs.GetXMLSchema() -> String
InventoryPostingLineUoMs.Item(ByVal vtIndex As Variant) -> InventoryPostingLineUoM
InventoryPostingLineUoMs.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingLineUoMs.ToXMLString() -> String
InventoryPostingParams.DocumentEntry : Long [R/W]
InventoryPostingParams.DocumentNumber : Long [R]
InventoryPostingParams.FromXMLFile(ByVal bstrFileName As String)
InventoryPostingParams.FromXMLString(ByVal bstrXML As String)
InventoryPostingParams.GetXMLSchema() -> String
InventoryPostingParams.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingParams.ToXMLString() -> String
InventoryPostingParamsCollection.Count : Long [R]
InventoryPostingParamsCollection.Add() -> InventoryPostingParams
InventoryPostingParamsCollection.GetXMLSchema() -> String
InventoryPostingParamsCollection.Item(ByVal vtIndex As Variant) -> InventoryPostingParams
InventoryPostingParamsCollection.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingParamsCollection.ToXMLString() -> String
InventoryPostingSerialNumber.BaseLineNumber : Long [R/W]
InventoryPostingSerialNumber.BatchID : String [R/W]
InventoryPostingSerialNumber.DocumentEntry : Long [R]
InventoryPostingSerialNumber.ExpiryDate : Date [R/W]
InventoryPostingSerialNumber.InternalSerialNumber : String [R/W]
InventoryPostingSerialNumber.Location : String [R/W]
InventoryPostingSerialNumber.ManufactureDate : Date [R/W]
InventoryPostingSerialNumber.ManufacturerSerialNumber : String [R/W]
InventoryPostingSerialNumber.Notes : String [R/W]
InventoryPostingSerialNumber.Quantity : Double [R/W]
InventoryPostingSerialNumber.ReceptionDate : Date [R/W]
InventoryPostingSerialNumber.SystemSerialNumber : Long [R/W]
InventoryPostingSerialNumber.TrackingNote : Long [R/W]
InventoryPostingSerialNumber.TrackingNoteLine : Long [R/W]
InventoryPostingSerialNumber.WarrantyEnd : Date [R/W]
InventoryPostingSerialNumber.WarrantyStart : Date [R/W]
InventoryPostingSerialNumber.FromXMLFile(ByVal bstrFileName As String)
InventoryPostingSerialNumber.FromXMLString(ByVal bstrXML As String)
InventoryPostingSerialNumber.GetXMLSchema() -> String
InventoryPostingSerialNumber.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingSerialNumber.ToXMLString() -> String
InventoryPostingSerialNumbers.Count : Long [R]
InventoryPostingSerialNumbers.Add() -> InventoryPostingSerialNumber
InventoryPostingSerialNumbers.GetXMLSchema() -> String
InventoryPostingSerialNumbers.Item(ByVal vtIndex As Variant) -> InventoryPostingSerialNumber
InventoryPostingSerialNumbers.ToXMLFile(ByVal bstrFileName As String)
InventoryPostingSerialNumbers.ToXMLString() -> String
InventoryPostingsService.Add(ByVal pIInventoryPosting As InventoryPosting) -> InventoryPostingParams
InventoryPostingsService.Get(ByVal pIInventoryPostingParams As InventoryPostingParams) -> InventoryPosting
InventoryPostingsService.GetDataInterface(ByVal enumMSDI As InventoryPostingsServiceDataInterfaces) -> Object
InventoryPostingsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
InventoryPostingsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
InventoryPostingsService.GetList() -> InventoryPostingParamsCollection
InventoryPostingsService.SetCopyOption(ByVal pIInventoryPostingCopyOption As InventoryPostingCopyOption)
InventoryPostingsService.Update(ByVal pIInventoryPosting As InventoryPosting)
InvokeParams.Value : String [R/W]
ItemBarCodes.AbsEntry : Long [R/W]
ItemBarCodes.BarCode : String [R/W]
ItemBarCodes.Count : Long [R]
ItemBarCodes.FreeText : String [R/W]
ItemBarCodes.UoMEntry : Long [R/W]
ItemBarCodes.Add()
ItemBarCodes.Delete()
ItemBarCodes.SetCurrentLine(ByVal LineNum As Long)
ItemCycleCount.Alert : BoYesNoEnum [R/W]
ItemCycleCount.AlertTime : Date [R/W]
ItemCycleCount.Count : Long [R]
ItemCycleCount.CycleCode : Long [R/W]
ItemCycleCount.DestinationUser : Long [R/W]
ItemCycleCount.NextCountingDate : Date [R/W]
ItemCycleCount.UserFields : UserFields [R]
ItemCycleCount.WarehouseCode : String [R/W]
ItemGroups.Alert : BoYesNoEnum [R/W]
ItemGroups.Browser : DataBrowser [R]
ItemGroups.ComponentWarehouse : BoMRPComponentWarehouse [R/W]
ItemGroups.CostAccount : String [R/W]
ItemGroups.CostInflationAccount : String [R/W]
ItemGroups.CostInflationOffsetAccount : String [R/W]
ItemGroups.CycleCode : Long [R/W]
ItemGroups.DecreaseGLAccount : String [R/W]
ItemGroups.DecreasingAccount : String [R/W]
ItemGroups.DefaultInventoryUoM : Long [R/W]
ItemGroups.DefaultUoMGroup : Long [R/W]
ItemGroups.EUExpensesAccount : String [R/W]
ItemGroups.EUPurchaseCreditAcc : String [R/W]
ItemGroups.EURevenuesAccount : String [R/W]
ItemGroups.ExchangeRateDifferencesAccount : String [R/W]
ItemGroups.ExemptedCredits : String [R/W]
ItemGroups.ExemptRevenuesAccount : String [R/W]
ItemGroups.ExpenseClearingAct : String [R/W]
ItemGroups.ExpenseOffsetAccount : String [R/W]
ItemGroups.ExpensesAccount : String [R/W]
ItemGroups.ForeignExpensesAccount : String [R/W]
ItemGroups.ForeignPurchaseCreditAcc : String [R/W]
ItemGroups.ForeignRevenuesAccount : String [R/W]
ItemGroups.GoodsClearingAccount : String [R/W]
ItemGroups.GroupName : String [R/W]
ItemGroups.IncreaseGLAccount : String [R/W]
ItemGroups.IncreasingAccount : String [R/W]
ItemGroups.InventoryAccount : String [R/W]
ItemGroups.InventoryOffsetProfitAndLossAccount : String [R/W]
ItemGroups.InventorySystem : BoInventorySystem [R/W]
ItemGroups.ItemClass : ItemClassEnum [R/W]
ItemGroups.LeadTime : Long [R/W]
ItemGroups.MinimumOrderQuantity : Double [R/W]
ItemGroups.NegativeInventoryAdjustmentAccount : String [R/W]
ItemGroups.Number : Long [R]
ItemGroups.OrderInterval : Long [R/W]
ItemGroups.OrderMultiple : Double [R/W]
ItemGroups.PAReturnAccount : String [R/W]
ItemGroups.PlanningSystem : BoPlanningSystem [R/W]
ItemGroups.PriceDifferencesAccount : String [R/W]
ItemGroups.ProcurementMethod : BoProcurementMethod [R/W]
ItemGroups.PurchaseAccount : String [R/W]
ItemGroups.PurchaseBalanceAccount : String [R/W]
ItemGroups.PurchaseCreditAcc : String [R/W]
ItemGroups.PurchaseOffsetAccount : String [R/W]
ItemGroups.RawMaterial : BoYesNoEnum [R/W]
ItemGroups.ReturningAccount : String [R/W]
ItemGroups.RevenuesAccount : String [R/W]
ItemGroups.SalesCreditAcc : String [R/W]
ItemGroups.SalesCreditEUAcc : String [R/W]
ItemGroups.SalesCreditForeignAcc : String [R/W]
ItemGroups.ShippedGoodsAccount : String [R/W]
ItemGroups.StockInflationAdjustAccount : String [R/W]
ItemGroups.StockInflationOffsetAccount : String [R/W]
ItemGroups.StockInTransitAccount : String [R/W]
ItemGroups.ToleranceDays : Long [R/W]
ItemGroups.TransfersAccount : String [R/W]
ItemGroups.UserFields : UserFields [R]
ItemGroups.VarianceAccount : String [R/W]
ItemGroups.VATInRevenueAccount : String [R/W]
ItemGroups.WarehouseInfo : ItemGroups_WarehouseInfo [R]
ItemGroups.WHIncomingCenvatAccount : String [R/W]
ItemGroups.WHOutgoingCenvatAccount : String [R/W]
ItemGroups.WIPMaterialAccount : String [R/W]
ItemGroups.WIPMaterialVarianceAccount : String [R/W]
ItemGroups.WipOffsetProfitAndLossAccount : String [R/W]
ItemGroups.Add() -> Long
ItemGroups.GetAsXML() -> String
ItemGroups.GetByKey(ByVal GroupCode As Long) -> Boolean
ItemGroups.Remove() -> Long
ItemGroups.SaveToFile(ByVal FileName As String)
ItemGroups.SaveXML(ByRef FileName As String)
ItemGroups.Update() -> Long
ItemGroups_WarehouseInfo.Count : Long [R]
ItemGroups_WarehouseInfo.DefaultBin : Long [R/W]
ItemGroups_WarehouseInfo.DefaultBinEnforced : BoYesNoEnum [R/W]
ItemGroups_WarehouseInfo.ItemGroupCode : Long [R]
ItemGroups_WarehouseInfo.WarehouseCode : String [R/W]
ItemGroups_WarehouseInfo.Add()
ItemGroups_WarehouseInfo.SetCurrentLine(ByVal LineNum As Long)
ItemIntrastatExtension.CommodityCode : Long [R/W]
ItemIntrastatExtension.CountryOfOrigin : String [R/W]
ItemIntrastatExtension.ExportNatureOfTransaction : Long [R/W]
ItemIntrastatExtension.ExportRegionCountry : String [R/W]
ItemIntrastatExtension.ExportRegionState : Long [R/W]
ItemIntrastatExtension.ExportStatisticalProcedure : Long [R/W]
ItemIntrastatExtension.FactorOfSupplementaryUnit : Double [R/W]
ItemIntrastatExtension.ImportNatureOfTransaction : Long [R/W]
ItemIntrastatExtension.ImportRegionCountry : String [R/W]
ItemIntrastatExtension.ImportRegionState : Long [R/W]
ItemIntrastatExtension.ImportStatisticalProcedure : Long [R/W]
ItemIntrastatExtension.IntrastatRelevant : BoYesNoEnum [R/W]
ItemIntrastatExtension.ItemCode : String [R]
ItemIntrastatExtension.ServiceCode : Long [R/W]
ItemIntrastatExtension.ServicePaymentMethod : BoServicePaymentMethods [R/W]
ItemIntrastatExtension.ServiceSupplyMethod : BoServiceSupplyMethods [R/W]
ItemIntrastatExtension.StatisticalCode : String [R]
ItemIntrastatExtension.SupplementaryUnit : Long [R/W]
ItemIntrastatExtension.Type : BoDocumentTypes [R/W]
ItemIntrastatExtension.UseWeightInCalculation : BoYesNoEnum [R/W]
ItemLocalizationInfos.Count : Long [R]
ItemLocalizationInfos.IncomeNature : String [R/W]
ItemLocalizationInfos.ItemCode : String [R]
ItemLocalizationInfos.Add()
ItemLocalizationInfos.Delete()
ItemLocalizationInfos.SetCurrentLine(ByVal LineNumber As Long)
ItemPriceParams.BlanketAgreementLine : Long [R/W]
ItemPriceParams.BlanketAgreementNumber : Long [R/W]
ItemPriceParams.CardCode : String [R/W]
ItemPriceParams.Currency : String [R/W]
ItemPriceParams.Date : Date [R/W]
ItemPriceParams.InventoryQuantity : Double [R/W]
ItemPriceParams.ItemCode : String [R/W]
ItemPriceParams.PriceList : Long [R/W]
ItemPriceParams.UoMEntry : Long [R/W]
ItemPriceParams.UoMQuantity : Double [R/W]
ItemPriceParams.FromXMLFile(ByVal bstrFileName As String)
ItemPriceParams.FromXMLString(ByVal bstrXML As String)
ItemPriceParams.GetXMLSchema() -> String
ItemPriceParams.ToXMLFile(ByVal bstrFileName As String)
ItemPriceParams.ToXMLString() -> String
ItemPriceReturnParams.Currency : String [R]
ItemPriceReturnParams.Discount : Double [R]
ItemPriceReturnParams.Price : Double [R]
ItemPriceReturnParams.FromXMLFile(ByVal bstrFileName As String)
ItemPriceReturnParams.FromXMLString(ByVal bstrXML As String)
ItemPriceReturnParams.GetXMLSchema() -> String
ItemPriceReturnParams.ToXMLFile(ByVal bstrFileName As String)
ItemPriceReturnParams.ToXMLString() -> String
ItemProperties.Browser : DataBrowser [R]
ItemProperties.Number : Long [R]
ItemProperties.PropertyName : String [R/W]
ItemProperties.UserFields : UserFields [R]
ItemProperties.GetAsXML() -> String
ItemProperties.GetByKey(ByVal lGroupCode As Long) -> Boolean
ItemProperties.SaveToFile(ByVal bstrFileName As String)
ItemProperties.SaveXML(ByRef pbstrFileName As String)
ItemProperties.Update() -> Long
Items.ApTaxCode : String [R/W]
Items.ArTaxCode : String [R/W]
Items.AssessableValue : Double [R/W]
Items.AssetClass : String [R/W]
Items.AssetGroup : String [R/W]
Items.AssetItem : BoYesNoEnum [R/W]
Items.AssetSerialNumber : String [R/W]
Items.AssetStatus : AssetStatusEnum [R]
Items.AssVal4WTR : Double [R/W]
Items.AttachmentEntry : Long [R/W]
Items.AttributeGroups : ItemsAttributeGroups [R]
Items.AutoCreateSerialNumbersOnRelease : BoYesNoEnum [R/W]
Items.AvgStdPrice : Double [R/W]
Items.BarCode : String [R/W]
Items.BarCodes : ItemBarCodes [R]
Items.BaseUnitName : String [R/W]
Items.BeverageCommercialBrandCode : Long [R/W]
Items.BeverageGroupCode : String [R/W]
Items.BeverageTableCode : String [R/W]
Items.Browser : DataBrowser [R]
Items.CapitalGoodsOnHoldLimit : Double [R/W]
Items.CapitalGoodsOnHoldPercent : Double [R/W]
Items.CapitalizationDate : Date [R/W]
Items.Cession : BoYesNoEnum [R/W]
Items.CESTCode : Long [R/W]
Items.ChapterID : Long [R/W]
Items.CommissionGroup : Long [R/W]
Items.CommissionPercent : Double [R/W]
Items.CommissionSum : Double [R/W]
Items.CommodityClassification : Long [R/W]
Items.ComponentWarehouse : BoMRPComponentWarehouse [R/W]
Items.CostAccountingMethod : BoInventorySystem [R/W]
Items.CountingItemsPerUnit : Double [R]
Items.CreateDate : Date [R]
Items.CreateQRCodeFrom : String [R/W]
Items.CreateTime : Date [R]
Items.CtrSealQty : Double [R/W]
Items.CustomsGroupCode : Long [R/W]
Items.DataExportCode : String [R/W]
Items.DeactivateAfterUsefulLife : BoYesNoEnum [R/W]
Items.DefaultCountingUnit : String [R]
Items.DefaultCountingUoMEntry : Long [R/W]
Items.DefaultPurchasingUoMEntry : Long [R/W]
Items.DefaultSalesUoMEntry : Long [R/W]
Items.DefaultWarehouse : String [R/W]
Items.DepreciationGroup : String [R/W]
Items.DepreciationParameters : ItemsDepreciationParameters [R]
Items.DesiredInventory : Double [R/W]
Items.DistributionRules : ItemsDistributionRules [R]
Items.DNFEntry : Long [R/W]
Items.ECExpensesAccount : String [R/W]
Items.ECRevenuesAccount : String [R/W]
Items.Employee : Long [R/W]
Items.EnforceAssetSerialNumbers : BoYesNoEnum [R/W]
Items.Excisable : BoYesNoEnum [R/W]
Items.ExemptIncomeAccount : String [R/W]
Items.ExpanseAccount : String [R/W]
Items.ForceSelectionOfSerialNumber : BoYesNoEnum [R/W]
Items.ForeignExpensesAccount : String [R/W]
Items.ForeignName : String [R/W]
Items.ForeignRevenuesAccount : String [R/W]
Items.Frozen : BoYesNoEnum [R/W]
Items.FrozenFrom : Date [R/W]
Items.FrozenRemarks : String [R/W]
Items.FrozenTo : Date [R/W]
Items.FuelID : Long [R/W]
Items.GLMethod : BoGLMethods [R/W]
Items.GSTRelevnt : BoYesNoEnum [R/W]
Items.GSTTaxCategory : GSTTaxCategoryEnum [R/W]
Items.GTSItemSpec : String [R/W]
Items.GTSItemTaxCategory : String [R/W]
Items.ImportedItem : BoYesNoEnum [R/W]
Items.IncomeAccount : String [R/W]
Items.IncomingServiceCode : Long [R/W]
Items.InCostRollup : BoYesNoEnum [R/W]
Items.IndirectTax : BoYesNoEnum [R/W]
Items.IntrastatExtension : ItemIntrastatExtension [R]
Items.InventoryItem : BoYesNoEnum [R/W]
Items.InventoryNumber : String [R/W]
Items.InventoryUOM : String [R/W]
Items.InventoryUoMEntry : Long [R/W]
Items.InventoryWeight : Double [R/W]
Items.InventoryWeight1 : Double [R/W]
Items.InventoryWeightUnit : Long [R/W]
Items.InventoryWeightUnit1 : Long [R/W]
Items.IsPhantom : BoYesNoEnum [R/W]
Items.IssueMethod : BoIssueMethod [R/W]
Items.IssuePrimarilyBy : IssuePrimarilyByEnum [R/W]
Items.ItemClass : ItemClassEnum [R/W]
Items.ItemCode : String [R/W]
Items.ItemCountryOrg : String [R/W]
Items.ItemName : String [R/W]
Items.ItemsGroupCode : Long [R/W]
Items.ItemType : ItemTypeEnum [R/W]
Items.LeadTime : Long [R/W]
Items.LegalText : String [R/W]
Items.LinkedResource : String [R]
Items.LocalizationInfos : ItemLocalizationInfos [R]
Items.Location : Long [R/W]
Items.Mainsupplier : String [R/W]
Items.ManageBatchNumbers : BoYesNoEnum [R/W]
Items.ManageByQuantity : BoYesNoEnum [R]
Items.ManageSerialNumbers : BoYesNoEnum [R/W]
Items.ManageSerialNumbersOnReleaseOnly : BoYesNoEnum [R/W]
Items.ManageStockByWarehouse : BoYesNoEnum [R/W]
Items.Manufacturer : Long [R/W]
Items.MaterialGroup : Long [R/W]
Items.MaterialType : BoMaterialTypes [R/W]
Items.MaxInventory : Double [R/W]
Items.MinInventory : Double [R/W]
Items.MinOrderQuantity : Double [R/W]
Items.MovingAveragePrice : Double [R]
Items.NCMCode : Long [R/W]
Items.NoDiscounts : BoYesNoEnum [R/W]
Items.NVECode : String [R/W]
Items.OrderIntervals : String [R/W]
Items.OrderMultiple : Double [R/W]
Items.OutgoingServiceCode : Long [R/W]
Items.PeriodControls : ItemsPeriodControls [R]
Items.Picture : String [R/W]
Items.PlanningSystem : BoPlanningSystem [R/W]
Items.PreferredVendors : Items_PreferredVendors [R]
Items.PriceList : Items_Prices [R]
Items.PricingUnit : Long [R/W]
Items.ProcurementMethod : BoProcurementMethod [R/W]
Items.ProdStdCost : Double [R/W]
Items.ProductSource : Long [R/W]
Items.Projects : ItemsProjects [R]
Items.Properties : BoYesNoEnum [R/W]
Items.PurchaseFactor1 : Double [R/W]
Items.PurchaseFactor2 : Double [R/W]
Items.PurchaseFactor3 : Double [R/W]
Items.PurchaseFactor4 : Double [R/W]
Items.PurchaseHeightUnit : Long [R/W]
Items.PurchaseHeightUnit1 : Long [R/W]
Items.PurchaseItem : BoYesNoEnum [R/W]
Items.PurchaseItemsPerUnit : Double [R/W]
Items.PurchaseLengthUnit : Long [R/W]
Items.PurchaseLengthUnit1 : Long [R/W]
Items.PurchasePackagingUnit : String [R/W]
Items.PurchaseQtyPerPackUnit : Double [R/W]
Items.PurchaseUnit : String [R/W]
Items.PurchaseUnitHeight : Double [R/W]
Items.PurchaseUnitHeight1 : Double [R/W]
Items.PurchaseUnitLength : Double [R/W]
Items.PurchaseUnitLength1 : Double [R/W]
Items.PurchaseUnitVolume : Double [R/W]
Items.PurchaseUnitWeight : Double [R/W]
Items.PurchaseUnitWeight1 : Double [R/W]
Items.PurchaseUnitWidth : Double [R/W]
Items.PurchaseUnitWidth1 : Double [R/W]
Items.PurchaseVATGroup : String [R/W]
Items.PurchaseVolumeUnit : Long [R/W]
Items.PurchaseWeightUnit : Long [R/W]
Items.PurchaseWeightUnit1 : Long [R/W]
Items.PurchaseWidthUnit : Long [R/W]
Items.PurchaseWidthUnit1 : Long [R/W]
Items.QuantityOnStock : Double [R]
Items.QuantityOrderedByCustomers : Double [R]
Items.QuantityOrderedFromVendors : Double [R]
Items.SACEntry : Long [R/W]
Items.SalesFactor1 : Double [R/W]
Items.SalesFactor2 : Double [R/W]
Items.SalesFactor3 : Double [R/W]
Items.SalesFactor4 : Double [R/W]
Items.SalesHeightUnit : Long [R/W]
Items.SalesHeightUnit1 : Long [R/W]
Items.SalesItem : BoYesNoEnum [R/W]
Items.SalesItemsPerUnit : Double [R/W]
Items.SalesLengthUnit : Long [R/W]
Items.SalesLengthUnit1 : Long [R/W]
Items.SalesPackagingUnit : String [R/W]
Items.SalesQtyPerPackUnit : Double [R/W]
Items.SalesUnit : String [R/W]
Items.SalesUnitHeight : Double [R/W]
Items.SalesUnitHeight1 : Double [R/W]
Items.SalesUnitLength : Double [R/W]
Items.SalesUnitLength1 : Double [R/W]
Items.SalesUnitVolume : Double [R/W]
Items.SalesUnitWeight : Double [R/W]
Items.SalesUnitWeight1 : Double [R/W]
Items.SalesUnitWidth : Double [R/W]
Items.SalesUnitWidth1 : Double [R/W]
Items.SalesVATGroup : String [R/W]
Items.SalesVolumeUnit : Long [R/W]
Items.SalesWeightUnit : Long [R/W]
Items.SalesWeightUnit1 : Long [R/W]
Items.SalesWidthUnit : Long [R/W]
Items.SalesWidthUnit1 : Long [R/W]
Items.ScsCode : String [R/W]
Items.SerialNum : String [R/W]
Items.Series : Long [R/W]
Items.ServiceCategoryEntry : Long [R/W]
Items.ServiceGroup : Long [R/W]
Items.ShipType : Long [R/W]
Items.SOIExcisable : SOIExcisableTypeEnum [R/W]
Items.SpProdType : SpecialProductTypeEnum [R/W]
Items.SRIAndBatchManageMethod : BoManageMethod [R/W]
Items.StatisticalAsset : BoYesNoEnum [R/W]
Items.SupplierCatalogNo : String [R/W]
Items.SWW : String [R/W]
Items.TaxType : BoTaxTypes [R/W]
Items.Technician : Long [R/W]
Items.TNVED : String [R/W]
Items.ToleranceDays : Long [R/W]
Items.TraceableItem : BoYesNoEnum [R/W]
Items.TreeType : BoItemTreeTypes [R]
Items.TypeOfAdvancedRules : TypeOfAdvancedRulesEnum [R/W]
Items.UnitOfMeasurements : ItemUnitOfMeasurements [R]
Items.UoMGroupEntry : Long [R/W]
Items.UpdateDate : Date [R]
Items.UpdateTime : Date [R]
Items.User_Text : String [R/W]
Items.UserFields : UserFields [R]
Items.Valid : BoYesNoEnum [R/W]
Items.ValidFrom : Date [R/W]
Items.ValidRemarks : String [R/W]
Items.ValidTo : Date [R/W]
Items.VatLiable : BoYesNoEnum [R/W]
Items.VirtualAssetItem : BoYesNoEnum [R/W]
Items.WarrantyTemplate : String [R/W]
Items.WhsInfo : ItemWarehouseInfo [R]
Items.WTLiable : BoYesNoEnum [R/W]
Items.Add() -> Long
Items.Cancel() -> Long
Items.Close() -> Long
Items.GetAsXML() -> String
Items.GetByKey(ByVal ItemCode As String) -> Boolean
Items.Remove() -> Long
Items.SaveToFile(ByVal FileName As String)
Items.SaveXML(ByRef FileName As String)
Items.Update() -> Long
Items.UpdateFromXML(ByVal FileName As String) -> Long
Items_PreferredVendors.BPCode : String [R/W]
Items_PreferredVendors.Count : Long [R]
Items_PreferredVendors.UserFields : UserFields [R]
Items_PreferredVendors.Add()
Items_PreferredVendors.Delete()
Items_PreferredVendors.SetCurrentLine(ByVal LineNum As Long)
Items_Prices.AdditionalCurrency1 : String [R/W]
Items_Prices.AdditionalCurrency2 : String [R/W]
Items_Prices.AdditionalPrice1 : Double [R/W]
Items_Prices.AdditionalPrice2 : Double [R/W]
Items_Prices.BasePriceList : Long [R/W]
Items_Prices.Count : Long [R]
Items_Prices.Currency : String [R/W]
Items_Prices.Factor : Double [R/W]
Items_Prices.Price : Double [R/W]
Items_Prices.PriceList : Long [R]
Items_Prices.PriceListName : String [R]
Items_Prices.UoMPrices : UoMPrices [R]
Items_Prices.UserFields : UserFields [R]
Items_Prices.SetCurrentLine(ByVal LineNum As Long)
ItemsAttributeGroups.Attribute1 : String [R/W]
ItemsAttributeGroups.Attribute10 : String [R/W]
ItemsAttributeGroups.Attribute11 : String [R/W]
ItemsAttributeGroups.Attribute12 : String [R/W]
ItemsAttributeGroups.Attribute13 : String [R/W]
ItemsAttributeGroups.Attribute14 : String [R/W]
ItemsAttributeGroups.Attribute15 : String [R/W]
ItemsAttributeGroups.Attribute16 : String [R/W]
ItemsAttributeGroups.Attribute17 : String [R/W]
ItemsAttributeGroups.Attribute18 : String [R/W]
ItemsAttributeGroups.Attribute19 : String [R/W]
ItemsAttributeGroups.Attribute2 : String [R/W]
ItemsAttributeGroups.Attribute20 : String [R/W]
ItemsAttributeGroups.Attribute21 : String [R/W]
ItemsAttributeGroups.Attribute22 : String [R/W]
ItemsAttributeGroups.Attribute23 : String [R/W]
ItemsAttributeGroups.Attribute24 : String [R/W]
ItemsAttributeGroups.Attribute25 : String [R/W]
ItemsAttributeGroups.Attribute26 : String [R/W]
ItemsAttributeGroups.Attribute27 : String [R/W]
ItemsAttributeGroups.Attribute28 : String [R/W]
ItemsAttributeGroups.Attribute29 : String [R/W]
ItemsAttributeGroups.Attribute3 : String [R/W]
ItemsAttributeGroups.Attribute30 : String [R/W]
ItemsAttributeGroups.Attribute31 : String [R/W]
ItemsAttributeGroups.Attribute32 : String [R/W]
ItemsAttributeGroups.Attribute33 : Long [R/W]
ItemsAttributeGroups.Attribute34 : Long [R/W]
ItemsAttributeGroups.Attribute35 : Long [R/W]
ItemsAttributeGroups.Attribute36 : Long [R/W]
ItemsAttributeGroups.Attribute37 : Long [R/W]
ItemsAttributeGroups.Attribute38 : Long [R/W]
ItemsAttributeGroups.Attribute39 : Long [R/W]
ItemsAttributeGroups.Attribute4 : String [R/W]
ItemsAttributeGroups.Attribute40 : Long [R/W]
ItemsAttributeGroups.Attribute41 : Long [R/W]
ItemsAttributeGroups.Attribute42 : Long [R/W]
ItemsAttributeGroups.Attribute43 : Date [R/W]
ItemsAttributeGroups.Attribute44 : Date [R/W]
ItemsAttributeGroups.Attribute45 : Date [R/W]
ItemsAttributeGroups.Attribute46 : Date [R/W]
ItemsAttributeGroups.Attribute47 : Date [R/W]
ItemsAttributeGroups.Attribute48 : Double [R/W]
ItemsAttributeGroups.Attribute49 : Double [R/W]
ItemsAttributeGroups.Attribute5 : String [R/W]
ItemsAttributeGroups.Attribute50 : Double [R/W]
ItemsAttributeGroups.Attribute51 : Double [R/W]
ItemsAttributeGroups.Attribute52 : Double [R/W]
ItemsAttributeGroups.Attribute53 : Double [R/W]
ItemsAttributeGroups.Attribute54 : Double [R/W]
ItemsAttributeGroups.Attribute55 : Double [R/W]
ItemsAttributeGroups.Attribute56 : Double [R/W]
ItemsAttributeGroups.Attribute57 : Double [R/W]
ItemsAttributeGroups.Attribute58 : Double [R/W]
ItemsAttributeGroups.Attribute59 : Double [R/W]
ItemsAttributeGroups.Attribute6 : String [R/W]
ItemsAttributeGroups.Attribute60 : Double [R/W]
ItemsAttributeGroups.Attribute61 : Double [R/W]
ItemsAttributeGroups.Attribute62 : Double [R/W]
ItemsAttributeGroups.Attribute63 : Double [R/W]
ItemsAttributeGroups.Attribute64 : Double [R/W]
ItemsAttributeGroups.Attribute7 : String [R/W]
ItemsAttributeGroups.Attribute8 : String [R/W]
ItemsAttributeGroups.Attribute9 : String [R/W]
ItemsAttributeGroups.Count : Long [R]
ItemsAttributeGroups.Add()
ItemsAttributeGroups.Delete()
ItemsAttributeGroups.SetCurrentLine(ByVal LineNum As Long)
ItemsDepreciationParameters.Count : Long [R]
ItemsDepreciationParameters.DepreciationArea : String [R/W]
ItemsDepreciationParameters.DepreciationEndDate : Date [R]
ItemsDepreciationParameters.DepreciationStartDate : Date [R/W]
ItemsDepreciationParameters.DepreciationType : String [R/W]
ItemsDepreciationParameters.FiscalYear : String [R/W]
ItemsDepreciationParameters.RemainingLife : Double [R]
ItemsDepreciationParameters.RemainingUnits : Long [R]
ItemsDepreciationParameters.StandardUnits : Long [R]
ItemsDepreciationParameters.TotalUnitsInUsefulLife : Long [R/W]
ItemsDepreciationParameters.UsefulLife : Long [R/W]
ItemsDepreciationParameters.Add()
ItemsDepreciationParameters.SetCurrentLine(ByVal LineNum As Long)
ItemsDistributionRules.Count : Long [R]
ItemsDistributionRules.DistributionRule : String [R/W]
ItemsDistributionRules.DistributionRule2 : String [R/W]
ItemsDistributionRules.DistributionRule3 : String [R/W]
ItemsDistributionRules.DistributionRule4 : String [R/W]
ItemsDistributionRules.DistributionRule5 : String [R/W]
ItemsDistributionRules.LineNumber : Long [R]
ItemsDistributionRules.ValidFrom : Date [R/W]
ItemsDistributionRules.ValidTo : Date [R/W]
ItemsDistributionRules.Add()
ItemsDistributionRules.Delete()
ItemsDistributionRules.SetCurrentLine(ByVal LineNum As Long)
ItemsPeriodControls.ActualUnits : Long [R/W]
ItemsPeriodControls.Count : Long [R]
ItemsPeriodControls.DepreciationArea : String [R/W]
ItemsPeriodControls.DepreciationStatus : BoYesNoEnum [R/W]
ItemsPeriodControls.Factor : Double [R/W]
ItemsPeriodControls.FiscalYear : String [R/W]
ItemsPeriodControls.SubPeriod : Long [R/W]
ItemsPeriodControls.Add()
ItemsPeriodControls.SetCurrentLine(ByVal LineNum As Long)
ItemsProjects.Count : Long [R]
ItemsProjects.LineNumber : Long [R]
ItemsProjects.Project : String [R/W]
ItemsProjects.ValidFrom : Date [R/W]
ItemsProjects.ValidTo : Date [R/W]
ItemsProjects.Add()
ItemsProjects.Delete()
ItemsProjects.SetCurrentLine(ByVal LineNum As Long)
ItemUnitOfMeasurements.Count : Long [R]
ItemUnitOfMeasurements.DefaultBarcode : Long [R/W]
ItemUnitOfMeasurements.DefaultPackage : Long [R/W]
ItemUnitOfMeasurements.Height1 : Double [R/W]
ItemUnitOfMeasurements.Height1Unit : Long [R/W]
ItemUnitOfMeasurements.Height2 : Double [R/W]
ItemUnitOfMeasurements.Height2Unit : Long [R/W]
ItemUnitOfMeasurements.Length1 : Double [R/W]
ItemUnitOfMeasurements.Length1Unit : Long [R/W]
ItemUnitOfMeasurements.Length2 : Double [R/W]
ItemUnitOfMeasurements.Length2Unit : Long [R/W]
ItemUnitOfMeasurements.Packages : ItemUoMPackages [R]
ItemUnitOfMeasurements.UoMEntry : Long [R/W]
ItemUnitOfMeasurements.UoMType : ItemUoMTypeEnum [R/W]
ItemUnitOfMeasurements.Volume : Double [R/W]
ItemUnitOfMeasurements.VolumeUnit : Long [R/W]
ItemUnitOfMeasurements.Weight1 : Double [R/W]
ItemUnitOfMeasurements.Weight1Unit : Long [R/W]
ItemUnitOfMeasurements.Weight2 : Double [R/W]
ItemUnitOfMeasurements.Weight2Unit : Long [R/W]
ItemUnitOfMeasurements.Width1 : Double [R/W]
ItemUnitOfMeasurements.Width1Unit : Long [R/W]
ItemUnitOfMeasurements.Width2 : Double [R/W]
ItemUnitOfMeasurements.Width2Unit : Long [R/W]
ItemUnitOfMeasurements.Add()
ItemUnitOfMeasurements.Delete()
ItemUnitOfMeasurements.SetCurrentLine(ByVal LineNum As Long)
ItemUoMPackages.Count : Long [R]
ItemUoMPackages.Height1 : Double [R/W]
ItemUoMPackages.Height1Unit : Long [R/W]
ItemUoMPackages.Height2 : Double [R/W]
ItemUoMPackages.Height2Unit : Long [R/W]
ItemUoMPackages.Length1 : Double [R/W]
ItemUoMPackages.Length1Unit : Long [R/W]
ItemUoMPackages.Length2 : Double [R/W]
ItemUoMPackages.Length2Unit : Long [R/W]
ItemUoMPackages.PackageTypeEntry : Long [R/W]
ItemUoMPackages.QuantityPerPackage : Double [R/W]
ItemUoMPackages.UoMEntry : Long [R/W]
ItemUoMPackages.UoMType : ItemUoMTypeEnum [R/W]
ItemUoMPackages.Volume : Double [R/W]
ItemUoMPackages.VolumeUnit : Long [R/W]
ItemUoMPackages.Weight1 : Double [R/W]
ItemUoMPackages.Weight1Unit : Long [R/W]
ItemUoMPackages.Weight2 : Double [R/W]
ItemUoMPackages.Weight2Unit : Long [R/W]
ItemUoMPackages.Width1 : Double [R/W]
ItemUoMPackages.Width1Unit : Long [R/W]
ItemUoMPackages.Width2 : Double [R/W]
ItemUoMPackages.Width2Unit : Long [R/W]
ItemUoMPackages.Add()
ItemUoMPackages.Delete()
ItemUoMPackages.SetCurrentLine(ByVal LineNum As Long)
ItemWarehouseInfo.CNJPOfManufacturer : String [R/W]
ItemWarehouseInfo.Committed : Double [R]
ItemWarehouseInfo.CostAccount : String [R/W]
ItemWarehouseInfo.CostInflationAccount : String [R/W]
ItemWarehouseInfo.CostInflationOffsetAccount : String [R/W]
ItemWarehouseInfo.Count : Long [R]
ItemWarehouseInfo.Counted : Double [R]
ItemWarehouseInfo.CountedQuantity : Double [R]
ItemWarehouseInfo.DecreasingAccount : String [R/W]
ItemWarehouseInfo.DefaultBin : Long [R/W]
ItemWarehouseInfo.DefaultBinEnforced : BoYesNoEnum [R/W]
ItemWarehouseInfo.EUExpensesAccount : String [R/W]
ItemWarehouseInfo.EUPurchaseCreditAcc : String [R/W]
ItemWarehouseInfo.EURevenuesAccount : String [R/W]
ItemWarehouseInfo.ExchangeRateDifferencesAcct : String [R/W]
ItemWarehouseInfo.ExemptedCredits : String [R/W]
ItemWarehouseInfo.ExemptIncomeAcc : String [R/W]
ItemWarehouseInfo.ExpenseClearingAct : String [R/W]
ItemWarehouseInfo.ExpenseOffsettingAccount : String [R/W]
ItemWarehouseInfo.ExpensesAccount : String [R/W]
ItemWarehouseInfo.ForeignExpensAcc : String [R/W]
ItemWarehouseInfo.ForeignPurchaseCreditAcc : String [R/W]
ItemWarehouseInfo.ForeignRevenueAcc : String [R/W]
ItemWarehouseInfo.GLDecreaseAcct : String [R/W]
ItemWarehouseInfo.GLIncreaseAcct : String [R/W]
ItemWarehouseInfo.GoodsClearingAcct : String [R/W]
ItemWarehouseInfo.IncreasingAccount : String [R/W]
ItemWarehouseInfo.IndicatorForRelevantScale : BoYesNoEnum [R/W]
ItemWarehouseInfo.InStock : Double [R]
ItemWarehouseInfo.InventoryAccount : String [R/W]
ItemWarehouseInfo.InventoryOffsetProfitAndLossAccount : String [R/W]
ItemWarehouseInfo.ItemCode : String [R]
ItemWarehouseInfo.ItemCycleCount : ItemCycleCount [R]
ItemWarehouseInfo.Locked : BoYesNoEnum [R/W]
ItemWarehouseInfo.MaximalStock : Double [R/W]
ItemWarehouseInfo.MinimalOrder : Double [R/W]
ItemWarehouseInfo.MinimalStock : Double [R/W]
ItemWarehouseInfo.NegativeInventoryAdjustmentAccount : String [R/W]
ItemWarehouseInfo.Ordered : Double [R]
ItemWarehouseInfo.PAReturnAcct : String [R/W]
ItemWarehouseInfo.PriceDifferenceAcc : String [R/W]
ItemWarehouseInfo.PurchaseAcct : String [R/W]
ItemWarehouseInfo.PurchaseBalanceAccount : String [R/W]
ItemWarehouseInfo.PurchaseCreditAcc : String [R/W]
ItemWarehouseInfo.PurchaseOffsetAcct : String [R/W]
ItemWarehouseInfo.ReturningAccount : String [R/W]
ItemWarehouseInfo.RevenuesAccount : String [R/W]
ItemWarehouseInfo.SalesCreditAcc : String [R/W]
ItemWarehouseInfo.SalesCreditEUAcc : String [R/W]
ItemWarehouseInfo.SalesCreditForeignAcc : String [R/W]
ItemWarehouseInfo.ShippedGoodsAccount : String [R/W]
ItemWarehouseInfo.StandardAveragePrice : Double [R/W]
ItemWarehouseInfo.StockInflationAdjustAccount : String [R/W]
ItemWarehouseInfo.StockInflationOffsetAccount : String [R/W]
ItemWarehouseInfo.StockInTransitAccount : String [R/W]
ItemWarehouseInfo.TransferAccount : String [R/W]
ItemWarehouseInfo.UserFields : UserFields [R]
ItemWarehouseInfo.VarienceAccount : String [R/W]
ItemWarehouseInfo.VATInRevenueAccount : String [R/W]
ItemWarehouseInfo.WarehouseCode : String [R/W]
ItemWarehouseInfo.WasCounted : BoYesNoEnum [R]
ItemWarehouseInfo.WHIncomingCenvatAccount : String [R/W]
ItemWarehouseInfo.WHOutgoingCenvatAccount : String [R/W]
ItemWarehouseInfo.WipAccount : String [R/W]
ItemWarehouseInfo.WipOffsetProfitAndLossAccount : String [R/W]
ItemWarehouseInfo.WipVarianceAccount : String [R/W]
ItemWarehouseInfo.Add()
ItemWarehouseInfo.Delete()
ItemWarehouseInfo.SetCurrentLine(ByVal LineNum As Long)
JournalEntries.AdjustTransaction : BoYesNoEnum [R/W]
JournalEntries.AttachmentEntry : Long [R/W]
JournalEntries.AutomaticWT : BoYesNoEnum [R/W]
JournalEntries.AutoVAT : BoYesNoEnum [R/W]
JournalEntries.BaseReference : String [R]
JournalEntries.BlanketAgreementNumber : Long [R]
JournalEntries.BlockDunningLetter : BoYesNoEnum [R/W]
JournalEntries.Browser : DataBrowser [R]
JournalEntries.CertificationNumber : String [R]
JournalEntries.Cig : Long [R/W]
JournalEntries.Corisptivi : BoYesNoEnum [R/W]
JournalEntries.Count : Long [R]
JournalEntries.Cup : Long [R/W]
JournalEntries.DeferredTax : BoYesNoEnum [R/W]
JournalEntries.DocumentType : String [R/W]
JournalEntries.DueDate : Date [R/W]
JournalEntries.ECDPostingType : ECDPostingTypeEnum [R/W]
JournalEntries.ElectronicProtocols : ElectronicProtocols [R]
JournalEntries.ExcludeFromTaxReportControlStatementVAT : BoYesNoEnum [R/W]
JournalEntries.ExposedTransNumber : Long [R/W]
JournalEntries.FolioNumber : Long [R]
JournalEntries.FolioNumberFrom : Long [R]
JournalEntries.FolioNumberTo : Long [R]
JournalEntries.FolioPrefixString : String [R]
JournalEntries.Indicator : String [R/W]
JournalEntries.IsCostCenterTransfer : BoYesNoEnum [R/W]
JournalEntries.JdtNum : Long [R]
JournalEntries.Letter : FolioLetterEnum [R]
JournalEntries.Lines : JournalEntries_Lines [R]
JournalEntries.LocationCode : Long [R/W]
JournalEntries.Memo : String [R/W]
JournalEntries.Number : Long [R]
JournalEntries.OperationCode : OperationCodeTypeEnum [R/W]
JournalEntries.Original : Long [R]
JournalEntries.OriginalJournal : TransTypesEnum [R]
JournalEntries.PointOfIssueCode : String [R]
JournalEntries.Printed : PrintStatusEnum [R]
JournalEntries.PrivateKeyVersion : Long [R]
JournalEntries.ProjectCode : String [R/W]
JournalEntries.Reference : String [R/W]
JournalEntries.Reference2 : String [R/W]
JournalEntries.Reference3 : String [R/W]
JournalEntries.ReferenceDate : Date [R/W]
JournalEntries.Report347 : BoYesNoEnum [R/W]
JournalEntries.ReportEU : BoYesNoEnum [R/W]
JournalEntries.ReportingSectionControlStatementVAT : String [R/W]
JournalEntries.ResidenceNumberType : ResidenceNumberTypeEnum [R/W]
JournalEntries.SAPPassport : String [R]
JournalEntries.Series : Long [R/W]
JournalEntries.SignatureDigest : String [R]
JournalEntries.SignatureInputMessage : String [R]
JournalEntries.StampTax : BoYesNoEnum [R/W]
JournalEntries.StornoDate : Date [R/W]
JournalEntries.TaxDate : Date [R/W]
JournalEntries.TransactionCode : String [R/W]
JournalEntries.UseAutoStorno : BoYesNoEnum [R/W]
JournalEntries.UserFields : UserFields [R]
JournalEntries.VatDate : Date [R/W]
JournalEntries.WithholdingTaxData : WithholdingTaxData [R]
JournalEntries.WTSum : Double [R]
JournalEntries.WTSumFC : Double [R]
JournalEntries.WTSumSC : Double [R]
JournalEntries.Add() -> Long
JournalEntries.Cancel() -> Long
JournalEntries.Close() -> Long
JournalEntries.GetAsXML() -> String
JournalEntries.GetByKey(ByVal JdtNum As Long) -> Boolean
JournalEntries.Remove() -> Long
JournalEntries.SaveToFile(ByVal FileName As String)
JournalEntries.SaveXML(ByRef FileName As String)
JournalEntries.SetCurrentLine(ByVal LineNum As Long)
JournalEntries.Update() -> Long
JournalEntries_Lines.AccountCode : String [R/W]
JournalEntries_Lines.AdditionalReference : String [R/W]
JournalEntries_Lines.BaseSum : Double [R/W]
JournalEntries_Lines.BlockReason : Long [R/W]
JournalEntries_Lines.BPLID : Long [R/W]
JournalEntries_Lines.BPLName : String [R]
JournalEntries_Lines.CheckAbs : Long [R]
JournalEntries_Lines.Cig : Long [R/W]
JournalEntries_Lines.ContraAccount : String [R/W]
JournalEntries_Lines.ControlAccount : String [R/W]
JournalEntries_Lines.CostElementCode : String [R]
JournalEntries_Lines.CostingCode : String [R/W]
JournalEntries_Lines.CostingCode2 : String [R/W]
JournalEntries_Lines.CostingCode3 : String [R/W]
JournalEntries_Lines.CostingCode4 : String [R/W]
JournalEntries_Lines.CostingCode5 : String [R/W]
JournalEntries_Lines.Count : Long [R]
JournalEntries_Lines.Credit : Double [R/W]
JournalEntries_Lines.CreditSys : Double [R/W]
JournalEntries_Lines.Cup : Long [R/W]
JournalEntries_Lines.Debit : Double [R/W]
JournalEntries_Lines.DebitSys : Double [R/W]
JournalEntries_Lines.DocumentArray : Long [R]
JournalEntries_Lines.DocumentLine : Long [R]
JournalEntries_Lines.DueDate : Date [R/W]
JournalEntries_Lines.EqualizationTaxAmount : Double [R]
JournalEntries_Lines.ExpensesClassificationCategory : Long [R/W]
JournalEntries_Lines.ExpensesClassificationType : Long [R/W]
JournalEntries_Lines.ExposedTransNumber : Long [R/W]
JournalEntries_Lines.FCCredit : Double [R/W]
JournalEntries_Lines.FCCurrency : String [R/W]
JournalEntries_Lines.FCDebit : Double [R/W]
JournalEntries_Lines.FederalTaxID : String [R/W]
JournalEntries_Lines.GrossValue : Double [R/W]
JournalEntries_Lines.IncomeClassificationCategory : Long [R/W]
JournalEntries_Lines.IncomeClassificationType : Long [R/W]
JournalEntries_Lines.Line_ID : Long [R]
JournalEntries_Lines.LineMemo : String [R/W]
JournalEntries_Lines.LocationCode : Long [R/W]
JournalEntries_Lines.PaymentBlock : BoYesNoEnum [R/W]
JournalEntries_Lines.PaymentOrdered : BoYesNoEnum [R]
JournalEntries_Lines.PrimaryFormItems : CashFlowAssignments [R]
JournalEntries_Lines.ProjectCode : String [R/W]
JournalEntries_Lines.Reference1 : String [R/W]
JournalEntries_Lines.Reference2 : String [R/W]
JournalEntries_Lines.ReferenceDate1 : Date [R/W]
JournalEntries_Lines.ReferenceDate2 : Date [R/W]
JournalEntries_Lines.ShortName : String [R/W]
JournalEntries_Lines.SystemBaseAmount : Double [R/W]
JournalEntries_Lines.SystemEqualizationTaxAmount : Double [R]
JournalEntries_Lines.SystemTotalTax : Double [R]
JournalEntries_Lines.SystemVatAmount : Double [R/W]
JournalEntries_Lines.TaxCode : String [R/W]
JournalEntries_Lines.TaxDate : Date [R/W]
JournalEntries_Lines.TaxGroup : String [R/W]
JournalEntries_Lines.TaxPostAccount : BoTaxPostAccEnum [R/W]
JournalEntries_Lines.TotalTax : Double [R]
JournalEntries_Lines.UserFields : UserFields [R]
JournalEntries_Lines.VatAmount : Double [R/W]
JournalEntries_Lines.VatClassificationCategory : Long [R/W]
JournalEntries_Lines.VatClassificationType : Long [R/W]
JournalEntries_Lines.VatDate : Date [R/W]
JournalEntries_Lines.VATExemptionCause : Long [R/W]
JournalEntries_Lines.VatLine : BoYesNoEnum [R/W]
JournalEntries_Lines.VATRegNum : String [R]
JournalEntries_Lines.WTLiable : BoYesNoEnum [R/W]
JournalEntries_Lines.WTRow : BoYesNoEnum [R/W]
JournalEntries_Lines.Add()
JournalEntries_Lines.SetCurrentLine(ByVal LineNum As Long)
JournalEntryDocumentType.DocTypeDescription : String [R/W]
JournalEntryDocumentType.JournalEntryType : String [R/W]
JournalEntryDocumentType.ShortName : String [R/W]
JournalEntryDocumentType.FromXMLFile(ByVal bstrFileName As String)
JournalEntryDocumentType.FromXMLString(ByVal bstrXML As String)
JournalEntryDocumentType.GetXMLSchema() -> String
JournalEntryDocumentType.ToXMLFile(ByVal bstrFileName As String)
JournalEntryDocumentType.ToXMLString() -> String
JournalEntryDocumentTypeParams.DocTypeDescription : String [R]
JournalEntryDocumentTypeParams.JournalEntryType : String [R/W]
JournalEntryDocumentTypeParams.ShortName : String [R]
JournalEntryDocumentTypeParams.FromXMLFile(ByVal bstrFileName As String)
JournalEntryDocumentTypeParams.FromXMLString(ByVal bstrXML As String)
JournalEntryDocumentTypeParams.GetXMLSchema() -> String
JournalEntryDocumentTypeParams.ToXMLFile(ByVal bstrFileName As String)
JournalEntryDocumentTypeParams.ToXMLString() -> String
JournalEntryDocumentTypeParamsCollection.Count : Long [R]
JournalEntryDocumentTypeParamsCollection.Add() -> JournalEntryDocumentTypeParams
JournalEntryDocumentTypeParamsCollection.GetXMLSchema() -> String
JournalEntryDocumentTypeParamsCollection.Item(ByVal vtIndex As Variant) -> JournalEntryDocumentTypeParams
JournalEntryDocumentTypeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
JournalEntryDocumentTypeParamsCollection.ToXMLString() -> String
JournalEntryDocumentTypeService.Add(ByVal pIJournalEntryDocumentType As JournalEntryDocumentType) -> JournalEntryDocumentTypeParams
JournalEntryDocumentTypeService.Delete(ByVal pIJournalEntryDocumentTypeParams As JournalEntryDocumentTypeParams)
JournalEntryDocumentTypeService.Get(ByVal pIJournalEntryDocumentTypeParams As JournalEntryDocumentTypeParams) -> JournalEntryDocumentType
JournalEntryDocumentTypeService.GetDataInterface(ByVal enumMSDI As JournalEntryDocumentTypeServiceDataInterfaces) -> Object
JournalEntryDocumentTypeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
JournalEntryDocumentTypeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
JournalEntryDocumentTypeService.GetList() -> JournalEntryDocumentTypeParamsCollection
JournalEntryDocumentTypeService.Update(ByVal pIJournalEntryDocumentType As JournalEntryDocumentType)
JournalVouchers.JournalEntries : JournalEntries [R]
JournalVouchers.Add() -> Long
JournalVouchers.LoadFromXML(ByVal FileName As String)
JournalVouchers.SaveToXMLHierarchy(ByVal FileName As String)
KnowledgeBaseSolutions.AttachmentEntry : Long [R/W]
KnowledgeBaseSolutions.Attachments : Attachments [R]
KnowledgeBaseSolutions.Browser : DataBrowser [R]
KnowledgeBaseSolutions.Cause : String [R/W]
KnowledgeBaseSolutions.CreatedBy : Long [R]
KnowledgeBaseSolutions.CreationDate : Date [R]
KnowledgeBaseSolutions.Description : String [R/W]
KnowledgeBaseSolutions.ItemCode : String [R/W]
KnowledgeBaseSolutions.LastUpdateDate : Date [R]
KnowledgeBaseSolutions.LastUpdatedBy : Long [R]
KnowledgeBaseSolutions.Owner : Long [R]
KnowledgeBaseSolutions.Solution : String [R/W]
KnowledgeBaseSolutions.SolutionCode : Long [R]
KnowledgeBaseSolutions.Status : Long [R/W]
KnowledgeBaseSolutions.Symptom : String [R/W]
KnowledgeBaseSolutions.UserFields : UserFields [R]
KnowledgeBaseSolutions.Add() -> Long
KnowledgeBaseSolutions.Close() -> Long
KnowledgeBaseSolutions.GetAsXML() -> String
KnowledgeBaseSolutions.GetByKey(ByVal SolutionCode As Long) -> Boolean
KnowledgeBaseSolutions.Remove() -> Long
KnowledgeBaseSolutions.SaveToFile(ByVal FileName As String)
KnowledgeBaseSolutions.SaveXML(ByRef FileName As String)
KnowledgeBaseSolutions.Update() -> Long
KPI.KPI_ItemLines : KPI_ItemLines [R]
KPI.KPICode : String [R/W]
KPI.KPIName : String [R/W]
KPI.KPIType : KPITypeEnum [R/W]
KPI.NumberOfColumns : Long [R/W]
KPI.FromXMLFile(ByVal bstrFileName As String)
KPI.FromXMLString(ByVal bstrXML As String)
KPI.GetXMLSchema() -> String
KPI.ToXMLFile(ByVal bstrFileName As String)
KPI.ToXMLString() -> String
KPI_ItemLine.KPICode : String [R]
KPI_ItemLine.KPILineNumber : Long [R]
KPI_ItemLine.KPIName : String [R/W]
KPI_ItemLine.KPIValue1 : Double [R/W]
KPI_ItemLine.KPIValue10 : Double [R/W]
KPI_ItemLine.KPIValue11 : Double [R/W]
KPI_ItemLine.KPIValue12 : Double [R/W]
KPI_ItemLine.KPIValue13 : Double [R/W]
KPI_ItemLine.KPIValue14 : Double [R/W]
KPI_ItemLine.KPIValue15 : Double [R/W]
KPI_ItemLine.KPIValue16 : Double [R/W]
KPI_ItemLine.KPIValue17 : Double [R/W]
KPI_ItemLine.KPIValue18 : Double [R/W]
KPI_ItemLine.KPIValue19 : Double [R/W]
KPI_ItemLine.KPIValue2 : Double [R/W]
KPI_ItemLine.KPIValue20 : Double [R/W]
KPI_ItemLine.KPIValue21 : Double [R/W]
KPI_ItemLine.KPIValue22 : Double [R/W]
KPI_ItemLine.KPIValue23 : Double [R/W]
KPI_ItemLine.KPIValue24 : Double [R/W]
KPI_ItemLine.KPIValue25 : Double [R/W]
KPI_ItemLine.KPIValue26 : Double [R/W]
KPI_ItemLine.KPIValue27 : Double [R/W]
KPI_ItemLine.KPIValue28 : Double [R/W]
KPI_ItemLine.KPIValue29 : Double [R/W]
KPI_ItemLine.KPIValue3 : Double [R/W]
KPI_ItemLine.KPIValue30 : Double [R/W]
KPI_ItemLine.KPIValue4 : Double [R/W]
KPI_ItemLine.KPIValue5 : Double [R/W]
KPI_ItemLine.KPIValue6 : Double [R/W]
KPI_ItemLine.KPIValue7 : Double [R/W]
KPI_ItemLine.KPIValue8 : Double [R/W]
KPI_ItemLine.KPIValue9 : Double [R/W]
KPI_ItemLine.FromXMLFile(ByVal bstrFileName As String)
KPI_ItemLine.FromXMLString(ByVal bstrXML As String)
KPI_ItemLine.GetXMLSchema() -> String
KPI_ItemLine.ToXMLFile(ByVal bstrFileName As String)
KPI_ItemLine.ToXMLString() -> String
KPI_ItemLines.Count : Long [R]
KPI_ItemLines.Add() -> KPI_ItemLine
KPI_ItemLines.GetXMLSchema() -> String
KPI_ItemLines.Item(ByVal vtIndex As Variant) -> KPI_ItemLine
KPI_ItemLines.ToXMLFile(ByVal bstrFileName As String)
KPI_ItemLines.ToXMLString() -> String
KPIParams.KPICode : String [R/W]
KPIParams.KPIName : String [R]
KPIParams.FromXMLFile(ByVal bstrFileName As String)
KPIParams.FromXMLString(ByVal bstrXML As String)
KPIParams.GetXMLSchema() -> String
KPIParams.ToXMLFile(ByVal bstrFileName As String)
KPIParams.ToXMLString() -> String
KPIsParams.Count : Long [R]
KPIsParams.Add() -> KPIParams
KPIsParams.GetXMLSchema() -> String
KPIsParams.Item(ByVal vtIndex As Variant) -> KPIParams
KPIsParams.ToXMLFile(ByVal bstrFileName As String)
KPIsParams.ToXMLString() -> String
KPIsService.Add(ByVal pIKPI As KPI) -> KPIParams
KPIsService.Delete(ByVal pIKPIParams As KPIParams)
KPIsService.Get(ByVal pIKPIParams As KPIParams) -> KPI
KPIsService.GetDataInterface(ByVal enumMSDI As KPIsServiceDataInterfaces) -> Object
KPIsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
KPIsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
KPIsService.GetList() -> KPIsParams
KPIsService.Update(ByVal pIKPI As KPI)
LandedCost.ActualCustoms : Double [R/W]
LandedCost.ActualCustomsFC : Double [R/W]
LandedCost.AmountToBalance : Double [R]
LandedCost.AmountToBalanceFC : Double [R]
LandedCost.AttachmentEntry : Long [R/W]
LandedCost.BeforeTax : Double [R]
LandedCost.BeforeTaxFC : Double [R]
LandedCost.BillofLadingNumber : String [R/W]
LandedCost.Broker : String [R/W]
LandedCost.BrokerName : String [R/W]
LandedCost.ClosedDocument : LandedCostDocStatusEnum [R/W]
LandedCost.CustomsAffectsInventory : BoYesNoEnum [R/W]
LandedCost.DocEntry : Long [R]
LandedCost.DocumentCurrency : String [R/W]
LandedCost.DocumentRate : Double [R/W]
LandedCost.DueDate : Date [R/W]
LandedCost.FileNumber : String [R/W]
LandedCost.JournalRemarks : String [R/W]
LandedCost.LandedCost_CostLines : LandedCost_CostLines [R]
LandedCost.LandedCost_ItemLines : LandedCost_ItemLines [R]
LandedCost.LandedCostNumber : Long [R]
LandedCost.PostingDate : Date [R/W]
LandedCost.ProjectedCustoms : Double [R]
LandedCost.ProjectedCustomsFC : Double [R]
LandedCost.Reference : String [R/W]
LandedCost.Remarks : String [R/W]
LandedCost.Series : Long [R/W]
LandedCost.Tax1 : Double [R/W]
LandedCost.Tax1FC : Double [R/W]
LandedCost.Tax2 : Double [R/W]
LandedCost.Tax2FC : Double [R/W]
LandedCost.Total : Double [R]
LandedCost.TotalFC : Double [R]
LandedCost.TotalFreightCharges : Double [R]
LandedCost.TotalFreightChargesFC : Double [R]
LandedCost.TransactionNumber : Long [R]
LandedCost.TransportType : Long [R/W]
LandedCost.UserFields : Fields [R]
LandedCost.VendorCode : String [R/W]
LandedCost.VendorName : String [R/W]
LandedCost.FromXMLFile(ByVal bstrFileName As String)
LandedCost.FromXMLString(ByVal bstrXML As String)
LandedCost.GetXMLSchema() -> String
LandedCost.ToXMLFile(ByVal bstrFileName As String)
LandedCost.ToXMLString() -> String
LandedCost_CostLine.AllocationBy : LandedCostAllocationByEnum [R/W]
LandedCost_CostLine.amount : Double [R/W]
LandedCost_CostLine.AmountFC : Double [R/W]
LandedCost_CostLine.Broker : String [R/W]
LandedCost_CostLine.BrokerName : String [R/W]
LandedCost_CostLine.CostCategory : LandedCostCostCategoryEnum [R/W]
LandedCost_CostLine.CostType : LCCostTypeEnum [R/W]
LandedCost_CostLine.DocEntry : Long [R]
LandedCost_CostLine.Factor : Double [R]
LandedCost_CostLine.IncludeForCustoms : BoYesNoEnum [R/W]
LandedCost_CostLine.LandedCostCode : String [R/W]
LandedCost_CostLine.OpenAmount : Double [R]
LandedCost_CostLine.OpenAmountFC : Double [R]
LandedCost_CostLine.UserFields : Fields [R]
LandedCost_CostLine.FromXMLFile(ByVal bstrFileName As String)
LandedCost_CostLine.FromXMLString(ByVal bstrXML As String)
LandedCost_CostLine.GetXMLSchema() -> String
LandedCost_CostLine.ToXMLFile(ByVal bstrFileName As String)
LandedCost_CostLine.ToXMLString() -> String
LandedCost_CostLines.Count : Long [R]
LandedCost_CostLines.Add() -> LandedCost_CostLine
LandedCost_CostLines.GetXMLSchema() -> String
LandedCost_CostLines.Item(ByVal vtIndex As Variant) -> LandedCost_CostLine
LandedCost_CostLines.ToXMLFile(ByVal bstrFileName As String)
LandedCost_CostLines.ToXMLString() -> String
LandedCost_ItemLine.AllocatedCostsLineTotal : Double [R]
LandedCost_ItemLine.AllocatedUnitCostsLineTotal : Double [R/W]
LandedCost_ItemLine.AllocatedUnitCostsLineTotalFC : Double [R/W]
LandedCost_ItemLine.AutomaticExpenditure : BoYesNoEnum [R/W]
LandedCost_ItemLine.BaseDocumentPrice : Double [R/W]
LandedCost_ItemLine.BaseDocumentType : LandedCostBaseDocumentTypeEnum [R/W]
LandedCost_ItemLine.BaseDocumentValueLineTotal : Double [R]
LandedCost_ItemLine.BaseDocumentValueLineTotalFC : Double [R]
LandedCost_ItemLine.BaseEntry : Long [R/W]
LandedCost_ItemLine.BaseLine : Long [R/W]
LandedCost_ItemLine.BlockNumber : String [R/W]
LandedCost_ItemLine.CCDNumber : String [R/W]
LandedCost_ItemLine.CorrectedBaseDocumentValue : Double [R/W]
LandedCost_ItemLine.CorrectedBaseDocumentValueFC : Double [R/W]
LandedCost_ItemLine.Currency : String [R/W]
LandedCost_ItemLine.Customs : Double [R]
LandedCost_ItemLine.CustomsAffectStock : BoYesNoEnum [R/W]
LandedCost_ItemLine.CustomsCost : Double [R/W]
LandedCost_ItemLine.CustomsCostFC : Double [R/W]
LandedCost_ItemLine.CustomsFC : Double [R]
LandedCost_ItemLine.CustomsGroupRate : Double [R]
LandedCost_ItemLine.CustomsValue : Double [R/W]
LandedCost_ItemLine.CustomsValueFC : Double [R/W]
LandedCost_ItemLine.CustomsVat : Double [R/W]
LandedCost_ItemLine.CustomsVatAffectStock : BoYesNoEnum [R/W]
LandedCost_ItemLine.CustomsVatFC : Double [R/W]
LandedCost_ItemLine.DistributionRule : String [R/W]
LandedCost_ItemLine.DistributionRule2 : String [R/W]
LandedCost_ItemLine.DistributionRule3 : String [R/W]
LandedCost_ItemLine.DistributionRule4 : String [R/W]
LandedCost_ItemLine.DistributionRule5 : String [R/W]
LandedCost_ItemLine.DocEntry : Long [R]
LandedCost_ItemLine.ExciseAffectStock : BoYesNoEnum [R/W]
LandedCost_ItemLine.ExciseSum : Double [R/W]
LandedCost_ItemLine.ExciseSumFC : Double [R/W]
LandedCost_ItemLine.Expenditure : Double [R/W]
LandedCost_ItemLine.ExpenditureFC : Double [R/W]
LandedCost_ItemLine.FactorWithCustoms : Double [R]
LandedCost_ItemLine.FactorWithoutCustoms : Double [R]
LandedCost_ItemLine.FixCosts : Double [R]
LandedCost_ItemLine.FixCostsFC : Double [R]
LandedCost_ItemLine.FOBandIncludedCosts : Double [R]
LandedCost_ItemLine.FOBandIncludedCostsFC : Double [R]
LandedCost_ItemLine.ImportLog : String [R/W]
LandedCost_ItemLine.InventoryUOM : String [R]
LandedCost_ItemLine.InventoryValuation : BoYesNoEnum [R/W]
LandedCost_ItemLine.ItemDescription : String [R]
LandedCost_ItemLine.LineNumber : Long [R]
LandedCost_ItemLine.LineTotal : Double [R]
LandedCost_ItemLine.LineTotalFC : Double [R]
LandedCost_ItemLine.Number : String [R]
LandedCost_ItemLine.OriginalWarehouse : String [R]
LandedCost_ItemLine.OriginLine : Long [R/W]
LandedCost_ItemLine.PriceList : Long [R/W]
LandedCost_ItemLine.Project : String [R/W]
LandedCost_ItemLine.ProjectedCustoms : Double [R/W]
LandedCost_ItemLine.ProjectedCustomsFC : Double [R/W]
LandedCost_ItemLine.Quantity : Double [R/W]
LandedCost_ItemLine.Rate : Double [R]
LandedCost_ItemLine.Reference : String [R]
LandedCost_ItemLine.ReleaseNumber : Long [R]
LandedCost_ItemLine.TotalCosts : Double [R]
LandedCost_ItemLine.TotalCostsFC : Double [R]
LandedCost_ItemLine.TotalLineProjectedCustoms : Double [R]
LandedCost_ItemLine.TotalVolume : Double [R/W]
LandedCost_ItemLine.UserFields : Fields [R]
LandedCost_ItemLine.VariantCosts : Double [R]
LandedCost_ItemLine.VariantCostsFC : Double [R]
LandedCost_ItemLine.VatGroup : String [R/W]
LandedCost_ItemLine.VatPercent : Double [R]
LandedCost_ItemLine.VendorCode : String [R]
LandedCost_ItemLine.Volume : Double [R/W]
LandedCost_ItemLine.VolumeUoM : Long [R/W]
LandedCost_ItemLine.Warehouse : String [R/W]
LandedCost_ItemLine.WarehousePrice : Double [R]
LandedCost_ItemLine.WarehousePriceFC : Double [R]
LandedCost_ItemLine.Weight1 : Double [R/W]
LandedCost_ItemLine.Weight1UnitCode : Long [R/W]
LandedCost_ItemLine.Weight2 : Double [R/W]
LandedCost_ItemLine.Weight2UnitCode : Long [R/W]
LandedCost_ItemLine.FromXMLFile(ByVal bstrFileName As String)
LandedCost_ItemLine.FromXMLString(ByVal bstrXML As String)
LandedCost_ItemLine.GetXMLSchema() -> String
LandedCost_ItemLine.ToXMLFile(ByVal bstrFileName As String)
LandedCost_ItemLine.ToXMLString() -> String
LandedCost_ItemLines.Count : Long [R]
LandedCost_ItemLines.Add() -> LandedCost_ItemLine
LandedCost_ItemLines.GetXMLSchema() -> String
LandedCost_ItemLines.Item(ByVal vtIndex As Variant) -> LandedCost_ItemLine
LandedCost_ItemLines.Remove(ByVal vtIndex As Variant)
LandedCost_ItemLines.ToXMLFile(ByVal bstrFileName As String)
LandedCost_ItemLines.ToXMLString() -> String
LandedCostParams.LandedCostNumber : Long [R/W]
LandedCostParams.FromXMLFile(ByVal bstrFileName As String)
LandedCostParams.FromXMLString(ByVal bstrXML As String)
LandedCostParams.GetXMLSchema() -> String
LandedCostParams.ToXMLFile(ByVal bstrFileName As String)
LandedCostParams.ToXMLString() -> String
LandedCostsCodes.AllocationBy : BoAllocationByEnum [R/W]
LandedCostsCodes.Browser : DataBrowser [R]
LandedCostsCodes.Code : String [R/W]
LandedCostsCodes.LandedCostsAllocationAccount : String [R/W]
LandedCostsCodes.Name : String [R/W]
LandedCostsCodes.UserFields : UserFields [R]
LandedCostsCodes.Add() -> Long
LandedCostsCodes.GetAsXML() -> String
LandedCostsCodes.GetByKey(ByVal bstrCode As String) -> Boolean
LandedCostsCodes.SaveToFile(ByVal bstrFileName As String)
LandedCostsCodes.SaveXML(ByRef pbstrFileName As String)
LandedCostsCodes.Update() -> Long
LandedCostsParams.Count : Long [R]
LandedCostsParams.Add() -> LandedCostParams
LandedCostsParams.GetXMLSchema() -> String
LandedCostsParams.Item(ByVal vtIndex As Variant) -> LandedCostParams
LandedCostsParams.ToXMLFile(ByVal bstrFileName As String)
LandedCostsParams.ToXMLString() -> String
LandedCostsService.AddLandedCost(ByVal pILandedCost As LandedCost) -> LandedCostParams
LandedCostsService.CancelLandedCost(ByVal pILandedCostParams As LandedCostParams)
LandedCostsService.CloseLandedCost(ByVal pILandedCostParams As LandedCostParams)
LandedCostsService.GetDataInterface(ByVal enumMSDI As LandedCostsServiceDataInterfaces) -> Object
LandedCostsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
LandedCostsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
LandedCostsService.GetLandedCost(ByVal pILandedCostParams As LandedCostParams) -> LandedCost
LandedCostsService.GetLandedCostList() -> LandedCostsParams
LandedCostsService.UpdateLandedCost(ByVal pILandedCost As LandedCost)
Layer.CurrentCost : Double [R]
Layer.DocNumber : String [R]
Layer.DocType : TransTypesEnum [R]
Layer.EntryDate : Date [R]
Layer.LayerID : Long [R/W]
Layer.OpenQty : Double [R]
Layer.TransactionSequenceNum : Long [R/W]
Layer.FromXMLFile(ByVal bstrFileName As String)
Layer.FromXMLString(ByVal bstrXML As String)
Layer.GetXMLSchema() -> String
Layer.ToXMLFile(ByVal bstrFileName As String)
Layer.ToXMLString() -> String
Layers.Count : Long [R]
Layers.Add() -> Layer
Layers.GetXMLSchema() -> String
Layers.Item(ByVal vtIndex As Variant) -> Layer
Layers.ToXMLFile(ByVal bstrFileName As String)
Layers.ToXMLString() -> String
LegalData.DateOfPrinting : Date [R/W]
LegalData.DocEntry : Long [R]
LegalData.DocumentNumber : String [R/W]
LegalData.FiscalNumber : String [R/W]
LegalData.FiscalSeries : String [R/W]
LegalData.FiscalUserID : Long [R/W]
LegalData.LegalDataDetailCollection : LegalDataDetailCollection [R]
LegalData.PrinterBrand : String [R/W]
LegalData.PrinterDllVersion : String [R/W]
LegalData.PrinterFirmwareVersion : String [R/W]
LegalData.PrinterModel : String [R/W]
LegalData.PrinterType : String [R/W]
LegalData.SourceObjectEntry : Long [R/W]
LegalData.SourceObjectType : BoAPARDocumentTypes [R/W]
LegalData.TimeOfPrinting : Date [R/W]
LegalData.FromXMLFile(ByVal bstrFileName As String)
LegalData.FromXMLString(ByVal bstrXML As String)
LegalData.GetXMLSchema() -> String
LegalData.ToXMLFile(ByVal bstrFileName As String)
LegalData.ToXMLString() -> String
LegalDataDetail.amount : Double [R/W]
LegalDataDetail.DocEntry : Long [R]
LegalDataDetail.LineSequence : Long [R]
LegalDataDetail.LineType : LegalDataLineTypeEnum [R/W]
LegalDataDetail.TaxCode : String [R/W]
LegalDataDetail.TaxRate : Double [R/W]
LegalDataDetail.FromXMLFile(ByVal bstrFileName As String)
LegalDataDetail.FromXMLString(ByVal bstrXML As String)
LegalDataDetail.GetXMLSchema() -> String
LegalDataDetail.ToXMLFile(ByVal bstrFileName As String)
LegalDataDetail.ToXMLString() -> String
LegalDataDetailCollection.Count : Long [R]
LegalDataDetailCollection.Add() -> LegalDataDetail
LegalDataDetailCollection.GetXMLSchema() -> String
LegalDataDetailCollection.Item(ByVal vtIndex As Variant) -> LegalDataDetail
LegalDataDetailCollection.ToXMLFile(ByVal bstrFileName As String)
LegalDataDetailCollection.ToXMLString() -> String
LegalDataParams.DocEntry : Long [R/W]
LegalDataParams.SourceObjectEntry : Long [R]
LegalDataParams.SourceObjectType : String [R]
LegalDataParams.FromXMLFile(ByVal bstrFileName As String)
LegalDataParams.FromXMLString(ByVal bstrXML As String)
LegalDataParams.GetXMLSchema() -> String
LegalDataParams.ToXMLFile(ByVal bstrFileName As String)
LegalDataParams.ToXMLString() -> String
LegalDataParamsCollection.Count : Long [R]
LegalDataParamsCollection.Add() -> LegalDataParams
LegalDataParamsCollection.GetXMLSchema() -> String
LegalDataParamsCollection.Item(ByVal vtIndex As Variant) -> LegalDataParams
LegalDataParamsCollection.ToXMLFile(ByVal bstrFileName As String)
LegalDataParamsCollection.ToXMLString() -> String
LegalDataService.Add(ByVal pILegalData As LegalData) -> LegalDataParams
LegalDataService.Get(ByVal pILegalDataParams As LegalDataParams) -> LegalData
LegalDataService.GetDataInterface(ByVal enumMSDI As LegalDataServiceDataInterfaces) -> Object
LegalDataService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
LegalDataService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
LegalDataService.Update(ByVal pILegalData As LegalData)
LengthMeasures.Browser : DataBrowser [R]
LengthMeasures.UnitCode : Long [R]
LengthMeasures.UnitCodeforQuantityDisplay : String [R/W]
LengthMeasures.UnitDisplay : String [R/W]
LengthMeasures.UnitLengthinmm : Double [R/W]
LengthMeasures.UnitName : String [R/W]
LengthMeasures.UserFields : UserFields [R]
LengthMeasures.Add() -> Long
LengthMeasures.GetAsXML() -> String
LengthMeasures.GetByKey(ByVal lUnitCode As Long) -> Boolean
LengthMeasures.Remove() -> Long
LengthMeasures.SaveToFile(ByVal bstrFileName As String)
LengthMeasures.SaveXML(ByRef pbstrFileName As String)
LengthMeasures.Update() -> Long
LocalEra.Browser : DataBrowser [R]
LocalEra.Code : String [R]
LocalEra.EraName : String [R]
LocalEra.StartDate : Date [R]
LocalEra.UserFields : UserFields [R]
LocalEra.GetAsXML() -> String
LocalEra.GetByKey(ByVal bstrCode As String) -> Boolean
LocalEra.SaveToFile(ByVal bstrFileName As String)
LocalEra.SaveXML(ByRef pbstrFileName As String)
Manufacturers.Browser : DataBrowser [R]
Manufacturers.Code : Long [R]
Manufacturers.ManufacturerName : String [R/W]
Manufacturers.UserFields : UserFields [R]
Manufacturers.Add() -> Long
Manufacturers.GetAsXML() -> String
Manufacturers.GetByKey(ByVal lCode As Long) -> Boolean
Manufacturers.Remove() -> Long
Manufacturers.SaveToFile(ByVal bstrFileName As String)
Manufacturers.SaveXML(ByRef pbstrFileName As String)
Manufacturers.Update() -> Long
MaterialGroup.AbsEntry : Long [R]
MaterialGroup.Description : String [R/W]
MaterialGroup.MaterialGroupCode : String [R/W]
MaterialGroup.FromXMLFile(ByVal bstrFileName As String)
MaterialGroup.FromXMLString(ByVal bstrXML As String)
MaterialGroup.GetXMLSchema() -> String
MaterialGroup.ToXMLFile(ByVal bstrFileName As String)
MaterialGroup.ToXMLString() -> String
MaterialGroupParams.AbsEntry : Long [R/W]
MaterialGroupParams.MaterialGroupCode : String [R]
MaterialGroupParams.FromXMLFile(ByVal bstrFileName As String)
MaterialGroupParams.FromXMLString(ByVal bstrXML As String)
MaterialGroupParams.GetXMLSchema() -> String
MaterialGroupParams.ToXMLFile(ByVal bstrFileName As String)
MaterialGroupParams.ToXMLString() -> String
MaterialGroupsParams.Count : Long [R]
MaterialGroupsParams.Add() -> MaterialGroupParams
MaterialGroupsParams.GetXMLSchema() -> String
MaterialGroupsParams.Item(ByVal vtIndex As Variant) -> MaterialGroupParams
MaterialGroupsParams.ToXMLFile(ByVal bstrFileName As String)
MaterialGroupsParams.ToXMLString() -> String
MaterialGroupsService.AddMaterialGroup(ByVal pIMaterialGroup As MaterialGroup) -> MaterialGroupParams
MaterialGroupsService.DeleteMaterialGroup(ByVal pIMaterialGroupParams As MaterialGroupParams)
MaterialGroupsService.GetDataInterface(ByVal enumMSDI As MaterialGroupsServiceDataInterfaces) -> Object
MaterialGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
MaterialGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
MaterialGroupsService.GetMaterialGroup(ByVal pIMaterialGroupParams As MaterialGroupParams) -> MaterialGroup
MaterialGroupsService.GetMaterialGroupList() -> MaterialGroupsParams
MaterialGroupsService.UpdateMaterialGroup(ByVal pIMaterialGroup As MaterialGroup)
MaterialRevaluation.Browser : DataBrowser [R]
MaterialRevaluation.CardCode : String [R/W]
MaterialRevaluation.CardName : String [R/W]
MaterialRevaluation.Comments : String [R/W]
MaterialRevaluation.CreationDate : Date [R]
MaterialRevaluation.DataSource : String [R]
MaterialRevaluation.DocDate : Date [R/W]
MaterialRevaluation.DocEntry : Long [R]
MaterialRevaluation.DocNum : Long [R]
MaterialRevaluation.DocTime : Date [R]
MaterialRevaluation.DocumentReferences : MaterialRevaluationDocumentReferences [R]
MaterialRevaluation.InflationRevaluation : BoYesNoEnum [R/W]
MaterialRevaluation.JournalMemo : String [R/W]
MaterialRevaluation.Lines : MaterialRevaluation_lines [R]
MaterialRevaluation.Reference1 : String [R]
MaterialRevaluation.Reference2 : String [R/W]
MaterialRevaluation.RevalType : String [R/W]
MaterialRevaluation.RevaluationExpenseAccount : String [R/W]
MaterialRevaluation.RevaluationIncomeAccount : String [R/W]
MaterialRevaluation.Series : Long [R/W]
MaterialRevaluation.TaxDate : Date [R/W]
MaterialRevaluation.TransNum : Long [R]
MaterialRevaluation.UpdateDate : Date [R]
MaterialRevaluation.UserFields : UserFields [R]
MaterialRevaluation.UserSignature : Long [R]
MaterialRevaluation.Add() -> Long
MaterialRevaluation.Cancel() -> Long
MaterialRevaluation.Close() -> Long
MaterialRevaluation.GetAsXML() -> String
MaterialRevaluation.GetByKey(ByVal AbsEntry As Long) -> Boolean
MaterialRevaluation.Remove() -> Long
MaterialRevaluation.SaveToFile(ByVal FileName As String)
MaterialRevaluation.SaveXML(ByRef FileName As String)
MaterialRevaluation.Update() -> Long
MaterialRevaluation_lines.ActualPrice : Double [R]
MaterialRevaluation_lines.Count : Long [R]
MaterialRevaluation_lines.DebitCredit : Double [R/W]
MaterialRevaluation_lines.DistributionRule : String [R/W]
MaterialRevaluation_lines.DistributionRule2 : String [R/W]
MaterialRevaluation_lines.DistributionRule3 : String [R/W]
MaterialRevaluation_lines.DistributionRule4 : String [R/W]
MaterialRevaluation_lines.DistributionRule5 : String [R/W]
MaterialRevaluation_lines.DocEntry : Long [R]
MaterialRevaluation_lines.FIFOLayers : FIFOLayers [R]
MaterialRevaluation_lines.ItemCode : String [R/W]
MaterialRevaluation_lines.ItemDescription : String [R]
MaterialRevaluation_lines.LineNum : Long [R]
MaterialRevaluation_lines.OnHand : Double [R]
MaterialRevaluation_lines.Price : Double [R/W]
MaterialRevaluation_lines.Project : String [R/W]
MaterialRevaluation_lines.Quantity : Double [R/W]
MaterialRevaluation_lines.RevalAmountToStock : Double [R]
MaterialRevaluation_lines.RevaluationDecrementAccount : String [R/W]
MaterialRevaluation_lines.RevaluationIncrementAccount : String [R/W]
MaterialRevaluation_lines.SNBLines : SNBLines [R]
MaterialRevaluation_lines.UserFields : UserFields [R]
MaterialRevaluation_lines.WarehouseCode : String [R/W]
MaterialRevaluation_lines.Add()
MaterialRevaluation_lines.SetCurrentLine(ByVal LineNum As Long)
MaterialRevaluationDocumentReferences.Count : Long [R]
MaterialRevaluationDocumentReferences.DocEntry : Long [R]
MaterialRevaluationDocumentReferences.ExternalReferencedDocNumber : String [R/W]
MaterialRevaluationDocumentReferences.IssueDate : Date [R/W]
MaterialRevaluationDocumentReferences.LineNumber : Long [R]
MaterialRevaluationDocumentReferences.ReferencedDocEntry : Long [R/W]
MaterialRevaluationDocumentReferences.ReferencedDocNumber : Long [R]
MaterialRevaluationDocumentReferences.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
MaterialRevaluationDocumentReferences.Remark : String [R/W]
MaterialRevaluationDocumentReferences.Add()
MaterialRevaluationDocumentReferences.Delete()
MaterialRevaluationDocumentReferences.SetCurrentLine(ByVal LineNum As Long)
MaterialRevaluationFIFO.Layers : Layers [R]
MaterialRevaluationFIFO.FromXMLFile(ByVal bstrFileName As String)
MaterialRevaluationFIFO.FromXMLString(ByVal bstrXML As String)
MaterialRevaluationFIFO.GetXMLSchema() -> String
MaterialRevaluationFIFO.ToXMLFile(ByVal bstrFileName As String)
MaterialRevaluationFIFO.ToXMLString() -> String
MaterialRevaluationFIFOParams.ItemCode : String [R/W]
MaterialRevaluationFIFOParams.LocationCode : String [R/W]
MaterialRevaluationFIFOParams.LocationType : String [R/W]
MaterialRevaluationFIFOParams.ShowIssuedLayers : BoYesNoEnum [R/W]
MaterialRevaluationFIFOParams.FromXMLFile(ByVal bstrFileName As String)
MaterialRevaluationFIFOParams.FromXMLString(ByVal bstrXML As String)
MaterialRevaluationFIFOParams.GetXMLSchema() -> String
MaterialRevaluationFIFOParams.ToXMLFile(ByVal bstrFileName As String)
MaterialRevaluationFIFOParams.ToXMLString() -> String
MaterialRevaluationFIFOService.GetDataInterface(ByVal enumMSDI As MaterialRevaluationFIFOServiceDataInterfaces) -> Object
MaterialRevaluationFIFOService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
MaterialRevaluationFIFOService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
MaterialRevaluationFIFOService.GetMaterialRevaluationFIFO(ByVal pIMaterialRevaluationFIFOParams As MaterialRevaluationFIFOParams) -> MaterialRevaluationFIFO
MaterialRevaluationSNBParam.ItemCode : String [R/W]
MaterialRevaluationSNBParam.FromXMLFile(ByVal bstrFileName As String)
MaterialRevaluationSNBParam.FromXMLString(ByVal bstrXML As String)
MaterialRevaluationSNBParam.GetXMLSchema() -> String
MaterialRevaluationSNBParam.ToXMLFile(ByVal bstrFileName As String)
MaterialRevaluationSNBParam.ToXMLString() -> String
MaterialRevaluationSNBParams.AdmissionDate : Date [R]
MaterialRevaluationSNBParams.DebitCredit : Double [R/W]
MaterialRevaluationSNBParams.ExpirationDate : Date [R]
MaterialRevaluationSNBParams.LotNumber : String [R]
MaterialRevaluationSNBParams.ManufactureNumber : String [R]
MaterialRevaluationSNBParams.NewCost : Double [R/W]
MaterialRevaluationSNBParams.SnbAbsEntry : Long [R/W]
MaterialRevaluationSNBParams.SystemNumber : Long [R]
MaterialRevaluationSNBParams.FromXMLFile(ByVal bstrFileName As String)
MaterialRevaluationSNBParams.FromXMLString(ByVal bstrXML As String)
MaterialRevaluationSNBParams.GetXMLSchema() -> String
MaterialRevaluationSNBParams.ToXMLFile(ByVal bstrFileName As String)
MaterialRevaluationSNBParams.ToXMLString() -> String
MaterialRevaluationSNBParamsCollection.Count : Long [R]
MaterialRevaluationSNBParamsCollection.Add() -> MaterialRevaluationSNBParams
MaterialRevaluationSNBParamsCollection.GetXMLSchema() -> String
MaterialRevaluationSNBParamsCollection.Item(ByVal vtIndex As Variant) -> MaterialRevaluationSNBParams
MaterialRevaluationSNBParamsCollection.ToXMLFile(ByVal bstrFileName As String)
MaterialRevaluationSNBParamsCollection.ToXMLString() -> String
MaterialRevaluationSNBService.Add(ByVal pIMaterialRevaluationSNBParam As MaterialRevaluationSNBParam) -> MaterialRevaluationSNBParams
MaterialRevaluationSNBService.GetDataInterface(ByVal enumMSDI As MaterialRevaluationSNBServiceDataInterfaces) -> Object
MaterialRevaluationSNBService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
MaterialRevaluationSNBService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
MaterialRevaluationSNBService.GetList(ByVal pIMaterialRevaluationSNBParam As MaterialRevaluationSNBParam) -> MaterialRevaluationSNBParamsCollection
Message.Attachment : Long [R/W]
Message.MessageDataColumns : MessageDataColumns [R/W]
Message.Priority : BoMsgPriorities [R/W]
Message.RecipientCollection : RecipientCollection [R/W]
Message.Subject : String [R/W]
Message.Text : String [R/W]
Message.User : Long [R/W]
Message.FromXMLFile(ByVal bstrFileName As String)
Message.FromXMLString(ByVal bstrXML As String)
Message.GetXMLSchema() -> String
Message.ToXMLFile(ByVal bstrFileName As String)
Message.ToXMLString() -> String
MessageDataColumn.ColumnName : String [R/W]
MessageDataColumn.Link : BoYesNoEnum [R/W]
MessageDataColumn.MessageDataLines : MessageDataLines [R/W]
MessageDataColumn.FromXMLFile(ByVal bstrFileName As String)
MessageDataColumn.FromXMLString(ByVal bstrXML As String)
MessageDataColumn.GetXMLSchema() -> String
MessageDataColumn.ToXMLFile(ByVal bstrFileName As String)
MessageDataColumn.ToXMLString() -> String
MessageDataColumns.Count : Long [R]
MessageDataColumns.Add() -> MessageDataColumn
MessageDataColumns.GetXMLSchema() -> String
MessageDataColumns.Item(ByVal vtIndex As Variant) -> MessageDataColumn
MessageDataColumns.ToXMLFile(ByVal bstrFileName As String)
MessageDataColumns.ToXMLString() -> String
MessageDataLine.Object : String [R/W]
MessageDataLine.ObjectKey : String [R/W]
MessageDataLine.Value : String [R/W]
MessageDataLine.FromXMLFile(ByVal bstrFileName As String)
MessageDataLine.FromXMLString(ByVal bstrXML As String)
MessageDataLine.GetXMLSchema() -> String
MessageDataLine.ToXMLFile(ByVal bstrFileName As String)
MessageDataLine.ToXMLString() -> String
MessageDataLines.Count : Long [R]
MessageDataLines.Add() -> MessageDataLine
MessageDataLines.GetXMLSchema() -> String
MessageDataLines.Item(ByVal vtIndex As Variant) -> MessageDataLine
MessageDataLines.ToXMLFile(ByVal bstrFileName As String)
MessageDataLines.ToXMLString() -> String
MessageHeader.Code : Long [R/W]
MessageHeader.Read : BoYesNoEnum [R]
MessageHeader.Received : BoYesNoEnum [R]
MessageHeader.ReceivedDate : Date [R]
MessageHeader.ReceivedTime : Date [R]
MessageHeader.SentDate : Date [R]
MessageHeader.SentTime : Date [R]
MessageHeader.FromXMLFile(ByVal bstrFileName As String)
MessageHeader.FromXMLString(ByVal bstrXML As String)
MessageHeader.GetXMLSchema() -> String
MessageHeader.ToXMLFile(ByVal bstrFileName As String)
MessageHeader.ToXMLString() -> String
MessageHeaders.Count : Long [R]
MessageHeaders.Add() -> MessageHeader
MessageHeaders.GetXMLSchema() -> String
MessageHeaders.Item(ByVal vtIndex As Variant) -> MessageHeader
MessageHeaders.ToXMLFile(ByVal bstrFileName As String)
MessageHeaders.ToXMLString() -> String
Messages.AttachmentEntry : Long [R/W]
Messages.Attachments : Attachments [R]
Messages.MessageText : String [R/W]
Messages.Priority : BoMsgPriorities [R/W]
Messages.Recipients : Recipients [R]
Messages.Subject : String [R/W]
Messages.Add() -> Long
Messages.AddDataColumn(ByVal Title As String, ByVal Text As String, ByVal Object As BoObjectTypes, ByVal ObjectKey As String)
MessagesService.GetDataInterface(ByVal enumMSDI As MessagesServiceDataInterfaces) -> Object
MessagesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
MessagesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
MessagesService.GetInbox() -> MessageHeaders
MessagesService.GetMessage(ByVal pMessageHeader As MessageHeader) -> Message
MessagesService.GetOutbox() -> MessageHeaders
MessagesService.GetSentMessages() -> MessageHeaders
MessagesService.SendMessage(ByVal pMessage As Message) -> MessageHeader
MobileAddOnSetting.B1MobileApp : BoYesNoEnum [R/W]
MobileAddOnSetting.B1SalesApp : BoYesNoEnum [R/W]
MobileAddOnSetting.B1ServiceApp : BoYesNoEnum [R/W]
MobileAddOnSetting.Code : String [R/W]
MobileAddOnSetting.Description : String [R/W]
MobileAddOnSetting.Enable : BoYesNoEnum [R/W]
MobileAddOnSetting.LogonMethod : LogonMethodEnum [R/W]
MobileAddOnSetting.Provider : String [R/W]
MobileAddOnSetting.Type : MobileAddonSettingTypeEnum [R/W]
MobileAddOnSetting.Url : String [R/W]
MobileAddOnSetting.ViewStyle : ViewStyleTypeEnum [R/W]
MobileAddOnSetting.FromXMLFile(ByVal bstrFileName As String)
MobileAddOnSetting.FromXMLString(ByVal bstrXML As String)
MobileAddOnSetting.GetXMLSchema() -> String
MobileAddOnSetting.ToXMLFile(ByVal bstrFileName As String)
MobileAddOnSetting.ToXMLString() -> String
MobileAddOnSettingParams.Code : String [R/W]
MobileAddOnSettingParams.Description : String [R]
MobileAddOnSettingParams.FromXMLFile(ByVal bstrFileName As String)
MobileAddOnSettingParams.FromXMLString(ByVal bstrXML As String)
MobileAddOnSettingParams.GetXMLSchema() -> String
MobileAddOnSettingParams.ToXMLFile(ByVal bstrFileName As String)
MobileAddOnSettingParams.ToXMLString() -> String
MobileAddOnSettingParamsCollection.Count : Long [R]
MobileAddOnSettingParamsCollection.Add() -> MobileAddOnSettingParams
MobileAddOnSettingParamsCollection.GetXMLSchema() -> String
MobileAddOnSettingParamsCollection.Item(ByVal vtIndex As Variant) -> MobileAddOnSettingParams
MobileAddOnSettingParamsCollection.ToXMLFile(ByVal bstrFileName As String)
MobileAddOnSettingParamsCollection.ToXMLString() -> String
MobileAddOnSettingService.AddMobileAddOnSetting(ByVal pIMobileAddOnSetting As MobileAddOnSetting) -> MobileAddOnSettingParams
MobileAddOnSettingService.DeleteMobileAddOnSetting(ByVal pIMobileAddOnSettingParams As MobileAddOnSettingParams)
MobileAddOnSettingService.GetDataInterface(ByVal enumMSDI As MobileAddOnSettingServiceDataInterfaces) -> Object
MobileAddOnSettingService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
MobileAddOnSettingService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
MobileAddOnSettingService.GetMobileAddOnSetting(ByVal pIMobileAddOnSettingParams As MobileAddOnSettingParams) -> MobileAddOnSetting
MobileAddOnSettingService.GetMobileAddOnSettingList() -> MobileAddOnSettingParamsCollection
MobileAddOnSettingService.UpdateMobileAddOnSetting(ByVal pIMobileAddOnSetting As MobileAddOnSetting)
MobileAppService.GetCurrentServerDateTime() -> MobileServerDateTime
MobileAppService.GetDataInterface(ByVal enumMSDI As MobileAppServiceDataInterfaces) -> Object
MobileAppService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
MobileAppService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
MobileAppService.GetDppChangeParams(ByVal pDppChangeParams As DppChangeParams) -> DppChangeParams
MobileAppService.GetEmployeeFullNames(ByVal pEmployeeFullNamesParamsCollection As EmployeeFullNamesParamsCollection) -> EmployeeFullNamesParamsCollection
MobileAppService.GetSalesAppSetting(ByVal pSalesAppSettingParams As SalesAppSettingParams) -> SalesAppSetting
MobileAppService.GetServiceAppReport(ByVal pServiceAppReportParams As ServiceAppReportParams) -> ServiceAppReport
MobileAppService.GetServiceAppReportContent(ByVal pServiceAppReportParams As ServiceAppReportParams) -> ServiceAppReportContent
MobileAppService.GetTechnicianSchedulings(ByVal pITechnicianSchedulingsParams As TechnicianSchedulingsParams) -> TechnicianSchedulingsCollection
MobileAppService.GetTechnicianSettings(ByVal pTechnicianSettingsParams As TechnicianSettingsParams) -> TechnicianSettings
MobileAppService.GetTechnicianSettingsGroup(ByVal pTechnicianSettingsGroupParams As TechnicianSettingsGroupParams) -> TechnicianSettingsGroup
MobileAppService.UpdateSalesAppSetting(ByVal pSalesAppSetting As SalesAppSetting)
MobileAppService.UpdateServiceAppReport(ByVal pServiceAppReport As ServiceAppReport)
MobileAppService.UpdateServiceAppReportContent(ByVal pServiceAppReportParams As ServiceAppReportParams, ByVal pServiceAppReportContent As ServiceAppReportContent)
MobileAppService.UpdateTechnicianSettings(ByVal ppTechnicianSettings As TechnicianSettings)
MobileAppService.UpdateTechnicianSettingsGroup(ByVal pTechnicianSettingsGroup As TechnicianSettingsGroup)
MobileServerDateTime.Date : Date [R]
MobileServerDateTime.Time : Date [R]
MobileServerDateTime.FromXMLFile(ByVal bstrFileName As String)
MobileServerDateTime.FromXMLString(ByVal bstrXML As String)
MobileServerDateTime.GetXMLSchema() -> String
MobileServerDateTime.ToXMLFile(ByVal bstrFileName As String)
MobileServerDateTime.ToXMLString() -> String
MultiLanguageTranslations.Browser : DataBrowser [R]
MultiLanguageTranslations.FieldAlias : String [R/W]
MultiLanguageTranslations.Numerator : Long [R]
MultiLanguageTranslations.PrimaryKeyofobject : String [R/W]
MultiLanguageTranslations.TableName : String [R/W]
MultiLanguageTranslations.TranslationsInUserLanguages : TranslationsInUserLanguages [R]
MultiLanguageTranslations.UserFields : UserFields [R]
MultiLanguageTranslations.Add() -> Long
MultiLanguageTranslations.GetAsXML() -> String
MultiLanguageTranslations.GetByKey(ByVal lAbsEntry As Long) -> Boolean
MultiLanguageTranslations.Remove() -> Long
MultiLanguageTranslations.SaveToFile(ByVal bstrFileName As String)
MultiLanguageTranslations.SaveXML(ByRef pbstrFileName As String)
MultiLanguageTranslations.Update() -> Long
MultiplePayment.AmountFC : Double [R/W]
MultiplePayment.AmountLC : Double [R/W]
MultiplePayment.BankStatmentLineID : Long [R]
MultiplePayment.DocumentIdentifier : String [R/W]
MultiplePayment.IsDebit : BoYesNoEnum [R/W]
MultiplePayment.ListLineID : Long [R]
MultiplePayment.FromXMLFile(ByVal bstrFileName As String)
MultiplePayment.FromXMLString(ByVal bstrXML As String)
MultiplePayment.GetXMLSchema() -> String
MultiplePayment.ToXMLFile(ByVal bstrFileName As String)
MultiplePayment.ToXMLString() -> String
MultiplePayments.Count : Long [R]
MultiplePayments.Add() -> MultiplePayment
MultiplePayments.GetXMLSchema() -> String
MultiplePayments.Item(ByVal vtIndex As Variant) -> MultiplePayment
MultiplePayments.Remove(ByVal vtIndex As Variant)
MultiplePayments.ToXMLFile(ByVal bstrFileName As String)
MultiplePayments.ToXMLString() -> String
NatureOfAssessee.AbsEntry : Long [R]
NatureOfAssessee.AssesseeType : AssesseeTypeEnum [R/W]
NatureOfAssessee.Code : String [R/W]
NatureOfAssessee.Description : String [R/W]
NatureOfAssessee.FromXMLFile(ByVal bstrFileName As String)
NatureOfAssessee.FromXMLString(ByVal bstrXML As String)
NatureOfAssessee.GetXMLSchema() -> String
NatureOfAssessee.ToXMLFile(ByVal bstrFileName As String)
NatureOfAssessee.ToXMLString() -> String
NatureOfAssesseeParams.AbsEntry : Long [R/W]
NatureOfAssesseeParams.Code : String [R]
NatureOfAssesseeParams.Description : String [R]
NatureOfAssesseeParams.FromXMLFile(ByVal bstrFileName As String)
NatureOfAssesseeParams.FromXMLString(ByVal bstrXML As String)
NatureOfAssesseeParams.GetXMLSchema() -> String
NatureOfAssesseeParams.ToXMLFile(ByVal bstrFileName As String)
NatureOfAssesseeParams.ToXMLString() -> String
NatureOfAssesseesParams.Count : Long [R]
NatureOfAssesseesParams.Add() -> NatureOfAssesseeParams
NatureOfAssesseesParams.GetXMLSchema() -> String
NatureOfAssesseesParams.Item(ByVal vtIndex As Variant) -> NatureOfAssesseeParams
NatureOfAssesseesParams.ToXMLFile(ByVal bstrFileName As String)
NatureOfAssesseesParams.ToXMLString() -> String
NatureOfAssesseesService.AddNatureOfAssessee(ByVal pINatureOfAssessee As NatureOfAssessee) -> NatureOfAssesseeParams
NatureOfAssesseesService.DeleteNatureOfAssessee(ByVal pINatureOfAssesseeParams As NatureOfAssesseeParams)
NatureOfAssesseesService.GetDataInterface(ByVal enumMSDI As NatureOfAssesseesServiceDataInterfaces) -> Object
NatureOfAssesseesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
NatureOfAssesseesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
NatureOfAssesseesService.GetNatureOfAssessee(ByVal pINatureOfAssesseeParams As NatureOfAssesseeParams) -> NatureOfAssessee
NatureOfAssesseesService.GetNatureOfAssesseeList() -> NatureOfAssesseesParams
NatureOfAssesseesService.UpdateNatureOfAssessee(ByVal pINatureOfAssessee As NatureOfAssessee)
NCMCodeSetup.AbsEntry : Long [R]
NCMCodeSetup.Description : String [R/W]
NCMCodeSetup.GroupCode : String [R/W]
NCMCodeSetup.NCMCode : String [R/W]
NCMCodeSetup.FromXMLFile(ByVal bstrFileName As String)
NCMCodeSetup.FromXMLString(ByVal bstrXML As String)
NCMCodeSetup.GetXMLSchema() -> String
NCMCodeSetup.ToXMLFile(ByVal bstrFileName As String)
NCMCodeSetup.ToXMLString() -> String
NCMCodeSetupParams.AbsEntry : Long [R/W]
NCMCodeSetupParams.Description : String [R]
NCMCodeSetupParams.NCMCode : String [R]
NCMCodeSetupParams.FromXMLFile(ByVal bstrFileName As String)
NCMCodeSetupParams.FromXMLString(ByVal bstrXML As String)
NCMCodeSetupParams.GetXMLSchema() -> String
NCMCodeSetupParams.ToXMLFile(ByVal bstrFileName As String)
NCMCodeSetupParams.ToXMLString() -> String
NCMCodeSetupParamsCollection.Count : Long [R]
NCMCodeSetupParamsCollection.Add() -> NCMCodeSetupParams
NCMCodeSetupParamsCollection.GetXMLSchema() -> String
NCMCodeSetupParamsCollection.Item(ByVal vtIndex As Variant) -> NCMCodeSetupParams
NCMCodeSetupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
NCMCodeSetupParamsCollection.ToXMLString() -> String
NCMCodesSetupService.AddNCMCodeSetup(ByVal pINCMCodeSetup As NCMCodeSetup) -> NCMCodeSetupParams
NCMCodesSetupService.DeleteNCMCodeSetup(ByVal pINCMCodeSetupParams As NCMCodeSetupParams)
NCMCodesSetupService.GetDataInterface(ByVal enumMSDI As NCMCodesSetupServiceDataInterfaces) -> Object
NCMCodesSetupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
NCMCodesSetupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
NCMCodesSetupService.GetNCMCodeSetup(ByVal pINCMCodeSetupParams As NCMCodeSetupParams) -> NCMCodeSetup
NCMCodesSetupService.GetNCMCodeSetupList() -> NCMCodeSetupParamsCollection
NCMCodesSetupService.UpdateNCMCodeSetup(ByVal pINCMCodeSetup As NCMCodeSetup)
NFModel.AbsEntry : String [R]
NFModel.NFMCode : String [R/W]
NFModel.NFMDescription : String [R/W]
NFModel.NFMName : String [R/W]
NFModel.FromXMLFile(ByVal bstrFileName As String)
NFModel.FromXMLString(ByVal bstrXML As String)
NFModel.GetXMLSchema() -> String
NFModel.ToXMLFile(ByVal bstrFileName As String)
NFModel.ToXMLString() -> String
NFModelParams.AbsEntry : String [R/W]
NFModelParams.NFMCode : String [R]
NFModelParams.NFMDescription : String [R]
NFModelParams.NFMName : String [R]
NFModelParams.FromXMLFile(ByVal bstrFileName As String)
NFModelParams.FromXMLString(ByVal bstrXML As String)
NFModelParams.GetXMLSchema() -> String
NFModelParams.ToXMLFile(ByVal bstrFileName As String)
NFModelParams.ToXMLString() -> String
NFModelsParams.Count : Long [R]
NFModelsParams.Add() -> NFModelParams
NFModelsParams.GetXMLSchema() -> String
NFModelsParams.Item(ByVal vtIndex As Variant) -> NFModelParams
NFModelsParams.ToXMLFile(ByVal bstrFileName As String)
NFModelsParams.ToXMLString() -> String
NFModelsService.Add(ByVal pINFModel As NFModel) -> NFModelParams
NFModelsService.Delete(ByVal pINFModelParams As NFModelParams)
NFModelsService.Get(ByVal pINFModelParams As NFModelParams) -> NFModel
NFModelsService.GetDataInterface(ByVal enumMSDI As NFModelsServiceDataInterfaces) -> Object
NFModelsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
NFModelsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
NFModelsService.GetList() -> NFModelsParams
NFModelsService.Update(ByVal pINFModel As NFModel)
NFTaxCategoriesService.Add(ByVal pINFTaxCategory As NFTaxCategory) -> NFTaxCategoryParams
NFTaxCategoriesService.Delete(ByVal pINFTaxCategoryParams As NFTaxCategoryParams)
NFTaxCategoriesService.Get(ByVal pINFTaxCategoryParams As NFTaxCategoryParams) -> NFTaxCategory
NFTaxCategoriesService.GetDataInterface(ByVal enumMSDI As NFTaxCategoriesServiceDataInterfaces) -> Object
NFTaxCategoriesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
NFTaxCategoriesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
NFTaxCategoriesService.GetList() -> NFTaxCategoryParamsCollection
NFTaxCategoriesService.Update(ByVal pINFTaxCategory As NFTaxCategory)
NFTaxCategory.AbsId : Long [R]
NFTaxCategory.CESTRelevant : BoYesNoEnum [R/W]
NFTaxCategory.Code : String [R/W]
NFTaxCategory.GPCId : Long [R/W]
NFTaxCategory.Locked : BoYesNoEnum [R/W]
NFTaxCategory.FromXMLFile(ByVal bstrFileName As String)
NFTaxCategory.FromXMLString(ByVal bstrXML As String)
NFTaxCategory.GetXMLSchema() -> String
NFTaxCategory.ToXMLFile(ByVal bstrFileName As String)
NFTaxCategory.ToXMLString() -> String
NFTaxCategoryParams.AbsId : Long [R/W]
NFTaxCategoryParams.Code : String [R/W]
NFTaxCategoryParams.FromXMLFile(ByVal bstrFileName As String)
NFTaxCategoryParams.FromXMLString(ByVal bstrXML As String)
NFTaxCategoryParams.GetXMLSchema() -> String
NFTaxCategoryParams.ToXMLFile(ByVal bstrFileName As String)
NFTaxCategoryParams.ToXMLString() -> String
NFTaxCategoryParamsCollection.Count : Long [R]
NFTaxCategoryParamsCollection.Add() -> NFTaxCategoryParams
NFTaxCategoryParamsCollection.GetXMLSchema() -> String
NFTaxCategoryParamsCollection.Item(ByVal vtIndex As Variant) -> NFTaxCategoryParams
NFTaxCategoryParamsCollection.ToXMLFile(ByVal bstrFileName As String)
NFTaxCategoryParamsCollection.ToXMLString() -> String
NotaFiscalCFOP.Application : String [R/W]
NotaFiscalCFOP.Browser : DataBrowser [R]
NotaFiscalCFOP.Code : String [R/W]
NotaFiscalCFOP.Description : String [R/W]
NotaFiscalCFOP.UserFields : UserFields [R]
NotaFiscalCFOP.Add() -> Long
NotaFiscalCFOP.GetAsXML() -> String
NotaFiscalCFOP.GetByKey(ByVal ID As Long) -> Boolean
NotaFiscalCFOP.Remove() -> Long
NotaFiscalCFOP.SaveToFile(ByVal FileName As String)
NotaFiscalCFOP.SaveXML(ByRef FileName As String)
NotaFiscalCFOP.Update() -> Long
NotaFiscalCST.Browser : DataBrowser [R]
NotaFiscalCST.Code : String [R/W]
NotaFiscalCST.CSTCodeOutgoing : String [R/W]
NotaFiscalCST.DescriptionOutgoing : String [R/W]
NotaFiscalCST.Situation : String [R/W]
NotaFiscalCST.TaxCategory : Long [R/W]
NotaFiscalCST.UserFields : UserFields [R]
NotaFiscalCST.Add() -> Long
NotaFiscalCST.GetAsXML() -> String
NotaFiscalCST.GetByKey(ByVal ID As Long) -> Boolean
NotaFiscalCST.Remove() -> Long
NotaFiscalCST.SaveToFile(ByVal FileName As String)
NotaFiscalCST.SaveXML(ByRef FileName As String)
NotaFiscalCST.Update() -> Long
NotaFiscalUsage.Adjustment : BoYesNoEnum [R/W]
NotaFiscalUsage.Browser : DataBrowser [R]
NotaFiscalUsage.Description : String [R/W]
NotaFiscalUsage.ID : Long [R]
NotaFiscalUsage.IncomingImportCFOPCode : String [R/W]
NotaFiscalUsage.IncomingInStateCFOPCode : String [R/W]
NotaFiscalUsage.IncomingOutStateCFOPCode : String [R/W]
NotaFiscalUsage.OutgoingExportCFOPCode : String [R/W]
NotaFiscalUsage.OutgoingInStateCFOPCode : String [R/W]
NotaFiscalUsage.OutgoingOutStateCFOPCode : String [R/W]
NotaFiscalUsage.ThirdParty : BoYesNoEnum [R/W]
NotaFiscalUsage.Usage : String [R/W]
NotaFiscalUsage.UserFields : UserFields [R]
NotaFiscalUsage.Add() -> Long
NotaFiscalUsage.GetAsXML() -> String
NotaFiscalUsage.GetByKey(ByVal ID As Long) -> Boolean
NotaFiscalUsage.Remove() -> Long
NotaFiscalUsage.SaveToFile(ByVal FileName As String)
NotaFiscalUsage.SaveXML(ByRef FileName As String)
NotaFiscalUsage.Update() -> Long
OccurenceCode.AbsEntry : Long [R]
OccurenceCode.Code : String [R/W]
OccurenceCode.Description : String [R/W]
OccurenceCode.IsMovement : BoYesNoEnum [R/W]
OccurenceCode.Note : String [R/W]
OccurenceCode.RequestedBoeStatus : BoBoeStatus [R/W]
OccurenceCode.FromXMLFile(ByVal bstrFileName As String)
OccurenceCode.FromXMLString(ByVal bstrXML As String)
OccurenceCode.GetXMLSchema() -> String
OccurenceCode.ToXMLFile(ByVal bstrFileName As String)
OccurenceCode.ToXMLString() -> String
OccurenceCodeParams.AbsEntry : Long [R/W]
OccurenceCodeParams.Code : String [R/W]
OccurenceCodeParams.Description : String [R]
OccurenceCodeParams.IsMovement : BoYesNoEnum [R/W]
OccurenceCodeParams.Note : String [R]
OccurenceCodeParams.RequestedBoeStatus : BoBoeStatus [R]
OccurenceCodeParams.FromXMLFile(ByVal bstrFileName As String)
OccurenceCodeParams.FromXMLString(ByVal bstrXML As String)
OccurenceCodeParams.GetXMLSchema() -> String
OccurenceCodeParams.ToXMLFile(ByVal bstrFileName As String)
OccurenceCodeParams.ToXMLString() -> String
OccurenceCodeParamsCollection.Count : Long [R]
OccurenceCodeParamsCollection.Add() -> OccurenceCodeParams
OccurenceCodeParamsCollection.GetXMLSchema() -> String
OccurenceCodeParamsCollection.Item(ByVal vtIndex As Variant) -> OccurenceCodeParams
OccurenceCodeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
OccurenceCodeParamsCollection.ToXMLString() -> String
OccurrenceCodesService.Add(ByVal pIOccurenceCode As OccurenceCode) -> OccurenceCodeParams
OccurrenceCodesService.Delete(ByVal pIOccurenceCodeParams As OccurenceCodeParams)
OccurrenceCodesService.Get(ByVal pIOccurenceCodeParams As OccurenceCodeParams) -> OccurenceCode
OccurrenceCodesService.GetDataInterface(ByVal enumMSDI As OccurrenceCodesServiceDataInterfaces) -> Object
OccurrenceCodesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
OccurrenceCodesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
OccurrenceCodesService.GetList() -> OccurenceCodeParamsCollection
OccurrenceCodesService.Update(ByVal pIOccurenceCode As OccurenceCode)
OpenningBalanceAccount.BPLID : Long [R/W]
OpenningBalanceAccount.Date : Date [R/W]
OpenningBalanceAccount.Details : String [R/W]
OpenningBalanceAccount.OpenBalanceAccount : String [R/W]
OpenningBalanceAccount.Ref1 : String [R/W]
OpenningBalanceAccount.Ref2 : String [R/W]
OpenningBalanceAccount.FromXMLFile(ByVal bstrFileName As String)
OpenningBalanceAccount.FromXMLString(ByVal bstrXML As String)
OpenningBalanceAccount.GetXMLSchema() -> String
OpenningBalanceAccount.ToXMLFile(ByVal bstrFileName As String)
OpenningBalanceAccount.ToXMLString() -> String
OriginalItem.AlternativeItems : AlternativeItems [R]
OriginalItem.ItemCode : String [R/W]
OriginalItem.ItemName : String [R]
OriginalItem.FromXMLFile(ByVal bstrFileName As String)
OriginalItem.FromXMLString(ByVal bstrXML As String)
OriginalItem.GetXMLSchema() -> String
OriginalItem.ToXMLFile(ByVal bstrFileName As String)
OriginalItem.ToXMLString() -> String
OriginalItemParams.ItemCode : String [R/W]
OriginalItemParams.ItemName : String [R]
OriginalItemParams.FromXMLFile(ByVal bstrFileName As String)
OriginalItemParams.FromXMLString(ByVal bstrXML As String)
OriginalItemParams.GetXMLSchema() -> String
OriginalItemParams.ToXMLFile(ByVal bstrFileName As String)
OriginalItemParams.ToXMLString() -> String
PackagesTypes.Browser : DataBrowser [R]
PackagesTypes.Code : Long [R]
PackagesTypes.Height1 : Double [R/W]
PackagesTypes.Height1Unit : Long [R/W]
PackagesTypes.Height2 : Double [R/W]
PackagesTypes.Height2Unit : Long [R/W]
PackagesTypes.Length1 : Double [R/W]
PackagesTypes.Length1Unit : Long [R/W]
PackagesTypes.Length2 : Double [R/W]
PackagesTypes.Length2Unit : Long [R/W]
PackagesTypes.Type : String [R/W]
PackagesTypes.UserFields : UserFields [R]
PackagesTypes.Volume : Double [R/W]
PackagesTypes.VolumeUnit : Long [R/W]
PackagesTypes.Weight1 : Double [R/W]
PackagesTypes.Weight1Unit : Long [R/W]
PackagesTypes.Weight2 : Double [R/W]
PackagesTypes.Weight2Unit : Long [R/W]
PackagesTypes.Width1 : Double [R/W]
PackagesTypes.Width1Unit : Long [R/W]
PackagesTypes.Width2 : Double [R/W]
PackagesTypes.Width2Unit : Long [R/W]
PackagesTypes.Add() -> Long
PackagesTypes.GetAsXML() -> String
PackagesTypes.GetByKey(ByVal lCode As Long) -> Boolean
PackagesTypes.Remove() -> Long
PackagesTypes.SaveToFile(ByVal FileName As String)
PackagesTypes.SaveXML(ByRef FileName As String)
PackagesTypes.Update() -> Long
PartnersSetup.DefaultRelationship : Long [R/W]
PartnersSetup.Details : String [R/W]
PartnersSetup.Name : String [R/W]
PartnersSetup.PartnerID : Long [R]
PartnersSetup.RelatedBP : String [R/W]
PartnersSetup.FromXMLFile(ByVal bstrFileName As String)
PartnersSetup.FromXMLString(ByVal bstrXML As String)
PartnersSetup.GetXMLSchema() -> String
PartnersSetup.ToXMLFile(ByVal bstrFileName As String)
PartnersSetup.ToXMLString() -> String
PartnersSetupParams.DefaultRelationship : Long [R]
PartnersSetupParams.Details : String [R]
PartnersSetupParams.Name : String [R]
PartnersSetupParams.PartnerID : Long [R/W]
PartnersSetupParams.RelatedBP : String [R]
PartnersSetupParams.FromXMLFile(ByVal bstrFileName As String)
PartnersSetupParams.FromXMLString(ByVal bstrXML As String)
PartnersSetupParams.GetXMLSchema() -> String
PartnersSetupParams.ToXMLFile(ByVal bstrFileName As String)
PartnersSetupParams.ToXMLString() -> String
PartnersSetupsParams.Count : Long [R]
PartnersSetupsParams.Add() -> PartnersSetupParams
PartnersSetupsParams.GetXMLSchema() -> String
PartnersSetupsParams.Item(ByVal vtIndex As Variant) -> PartnersSetupParams
PartnersSetupsParams.ToXMLFile(ByVal bstrFileName As String)
PartnersSetupsParams.ToXMLString() -> String
PartnersSetupsService.Add(ByVal pIPartnersSetup As PartnersSetup) -> PartnersSetupParams
PartnersSetupsService.Delete(ByVal pIPartnersSetupParams As PartnersSetupParams)
PartnersSetupsService.Get(ByVal pIPartnersSetupParams As PartnersSetupParams) -> PartnersSetup
PartnersSetupsService.GetDataInterface(ByVal enumMSDI As PartnersSetupsServiceDataInterfaces) -> Object
PartnersSetupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
PartnersSetupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
PartnersSetupsService.GetList() -> PartnersSetupsParams
PartnersSetupsService.Update(ByVal pIPartnersSetup As PartnersSetup)
PathAdmin.AttachmentsFolderPath : String [R/W]
PathAdmin.ExtensionsFolderPath : String [R/W]
PathAdmin.PicturesFolderPath : String [R/W]
PathAdmin.PrintId : String [R]
PathAdmin.WordTemplateFolderPath : String [R/W]
PathAdmin.FromXMLFile(ByVal bstrFileName As String)
PathAdmin.FromXMLString(ByVal bstrXML As String)
PathAdmin.GetXMLSchema() -> String
PathAdmin.ToXMLFile(ByVal bstrFileName As String)
PathAdmin.ToXMLString() -> String
PaymentAmountParams.CashDiscountAmount : Double [R]
PaymentAmountParams.CashDiscountAmountFC : Double [R]
PaymentAmountParams.CashDiscountAmountSC : Double [R]
PaymentAmountParams.CashDiscountPercentage : Double [R]
PaymentAmountParams.DocEntry : Long [R]
PaymentAmountParams.DocType : PaymentInvoiceTypeEnum [R]
PaymentAmountParams.InstallmentId : Long [R]
PaymentAmountParams.TotalPaymentAmount : Double [R]
PaymentAmountParams.TotalPaymentAmountFC : Double [R]
PaymentAmountParams.TotalPaymentAmountSC : Double [R]
PaymentAmountParams.FromXMLFile(ByVal bstrFileName As String)
PaymentAmountParams.FromXMLString(ByVal bstrXML As String)
PaymentAmountParams.GetXMLSchema() -> String
PaymentAmountParams.ToXMLFile(ByVal bstrFileName As String)
PaymentAmountParams.ToXMLString() -> String
PaymentAmountParamsCollection.Count : Long [R]
PaymentAmountParamsCollection.Add() -> PaymentAmountParams
PaymentAmountParamsCollection.GetXMLSchema() -> String
PaymentAmountParamsCollection.Item(ByVal vtIndex As Variant) -> PaymentAmountParams
PaymentAmountParamsCollection.ToXMLFile(ByVal bstrFileName As String)
PaymentAmountParamsCollection.ToXMLString() -> String
PaymentBlock.AbsEntry : Long [R]
PaymentBlock.PaymentBlockCode : String [R/W]
PaymentBlock.FromXMLFile(ByVal bstrFileName As String)
PaymentBlock.FromXMLString(ByVal bstrXML As String)
PaymentBlock.GetXMLSchema() -> String
PaymentBlock.ToXMLFile(ByVal bstrFileName As String)
PaymentBlock.ToXMLString() -> String
PaymentBlockParams.AbsEntry : Long [R/W]
PaymentBlockParams.PaymentBlockCode : String [R]
PaymentBlockParams.FromXMLFile(ByVal bstrFileName As String)
PaymentBlockParams.FromXMLString(ByVal bstrXML As String)
PaymentBlockParams.GetXMLSchema() -> String
PaymentBlockParams.ToXMLFile(ByVal bstrFileName As String)
PaymentBlockParams.ToXMLString() -> String
PaymentBlocksParams.Count : Long [R]
PaymentBlocksParams.Add() -> PaymentBlockParams
PaymentBlocksParams.GetXMLSchema() -> String
PaymentBlocksParams.Item(ByVal vtIndex As Variant) -> PaymentBlockParams
PaymentBlocksParams.ToXMLFile(ByVal bstrFileName As String)
PaymentBlocksParams.ToXMLString() -> String
PaymentBlocksService.AddPaymentBlock(ByVal pIPaymentBlock As PaymentBlock) -> PaymentBlockParams
PaymentBlocksService.DeletePaymentBlock(ByVal pIPaymentBlockParams As PaymentBlockParams)
PaymentBlocksService.GetDataInterface(ByVal enumMSDI As PaymentBlocksServiceDataInterfaces) -> Object
PaymentBlocksService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
PaymentBlocksService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
PaymentBlocksService.GetPaymentBlock(ByVal pIPaymentBlockParams As PaymentBlockParams) -> PaymentBlock
PaymentBlocksService.GetPaymentBlockList() -> PaymentBlocksParams
PaymentBlocksService.UpdatePaymentBlock(ByVal pIPaymentBlock As PaymentBlock)
PaymentBPCode.BPCode : String [R/W]
PaymentBPCode.Date : Date [R/W]
PaymentBPCode.FromXMLFile(ByVal bstrFileName As String)
PaymentBPCode.FromXMLString(ByVal bstrXML As String)
PaymentBPCode.GetXMLSchema() -> String
PaymentBPCode.ToXMLFile(ByVal bstrFileName As String)
PaymentBPCode.ToXMLString() -> String
PaymentCalculationService.GetDataInterface(ByVal enumMSDI As PaymentCalculationServiceDataInterfaces) -> Object
PaymentCalculationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
PaymentCalculationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
PaymentCalculationService.GetPaymentAmount(ByVal pIPaymentBPCode As PaymentBPCode, ByVal pIPaymentInvoiceEntries As PaymentInvoiceEntries) -> PaymentAmountParamsCollection
PaymentInvoiceEntries.Count : Long [R]
PaymentInvoiceEntries.Add() -> PaymentInvoiceEntry
PaymentInvoiceEntries.GetXMLSchema() -> String
PaymentInvoiceEntries.Item(ByVal vtIndex As Variant) -> PaymentInvoiceEntry
PaymentInvoiceEntries.ToXMLFile(ByVal bstrFileName As String)
PaymentInvoiceEntries.ToXMLString() -> String
PaymentInvoiceEntry.DocEntry : Long [R/W]
PaymentInvoiceEntry.DocNum : Long [R]
PaymentInvoiceEntry.DocType : PaymentInvoiceTypeEnum [R/W]
PaymentInvoiceEntry.InstallmentId : Long [R/W]
PaymentInvoiceEntry.FromXMLFile(ByVal bstrFileName As String)
PaymentInvoiceEntry.FromXMLString(ByVal bstrXML As String)
PaymentInvoiceEntry.GetXMLSchema() -> String
PaymentInvoiceEntry.ToXMLFile(ByVal bstrFileName As String)
PaymentInvoiceEntry.ToXMLString() -> String
PaymentReasonCode.Code : String [R/W]
PaymentReasonCode.FromXMLFile(ByVal bstrFileName As String)
PaymentReasonCode.FromXMLString(ByVal bstrXML As String)
PaymentReasonCode.GetXMLSchema() -> String
PaymentReasonCode.ToXMLFile(ByVal bstrFileName As String)
PaymentReasonCode.ToXMLString() -> String
PaymentReasonCodeParams.Code : String [R/W]
PaymentReasonCodeParams.FromXMLFile(ByVal bstrFileName As String)
PaymentReasonCodeParams.FromXMLString(ByVal bstrXML As String)
PaymentReasonCodeParams.GetXMLSchema() -> String
PaymentReasonCodeParams.ToXMLFile(ByVal bstrFileName As String)
PaymentReasonCodeParams.ToXMLString() -> String
PaymentReasonCodeService.AddPaymentReasonCode(ByVal pIPaymentReasonCode As PaymentReasonCode) -> PaymentReasonCodeParams
PaymentReasonCodeService.DeletePaymentReasonCode(ByVal pIPaymentReasonCodeParams As PaymentReasonCodeParams)
PaymentReasonCodeService.GetDataInterface(ByVal enumMSDI As PaymentReasonCodeServiceDataInterfaces) -> Object
PaymentReasonCodeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
PaymentReasonCodeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
PaymentReasonCodeService.GetPaymentReasonCode(ByVal pIPaymentReasonCodeParams As PaymentReasonCodeParams) -> PaymentReasonCode
PaymentReasonCodeService.GetPaymentReasonCodeList() -> PaymentReasonCodesParams
PaymentReasonCodesParams.Count : Long [R]
PaymentReasonCodesParams.Add() -> PaymentReasonCodeParams
PaymentReasonCodesParams.GetXMLSchema() -> String
PaymentReasonCodesParams.Item(ByVal vtIndex As Variant) -> PaymentReasonCodeParams
PaymentReasonCodesParams.ToXMLFile(ByVal bstrFileName As String)
PaymentReasonCodesParams.ToXMLString() -> String
PaymentRunExport.AdditionalIdNumber : String [R]
PaymentRunExport.BankAccount : String [R]
PaymentRunExport.BankCode : String [R]
PaymentRunExport.BankCountry : String [R]
PaymentRunExport.BankIBAN : String [R]
PaymentRunExport.Browser : DataBrowser [R]
PaymentRunExport.CollectionAuthorization : BoYesNoEnum [R]
PaymentRunExport.CompanyAddress : String [R]
PaymentRunExport.CompanyBlock : String [R]
PaymentRunExport.CompanyCity : String [R]
PaymentRunExport.CompanyCounty : String [R]
PaymentRunExport.CompanyName : String [R]
PaymentRunExport.CompanyState : String [R]
PaymentRunExport.CompanyStreet : String [R]
PaymentRunExport.CompanyTaxNum : String [R]
PaymentRunExport.CompanyZipCode : String [R]
PaymentRunExport.CompIsrBillerID : String [R]
PaymentRunExport.Countery : String [R]
PaymentRunExport.Currency : String [R]
PaymentRunExport.CustomerNum : String [R]
PaymentRunExport.DebitMemo : BoYesNoEnum [R]
PaymentRunExport.DocAmountForign : Double [R]
PaymentRunExport.DocAmountLocal : Double [R]
PaymentRunExport.DocCashDiscount : Double [R]
PaymentRunExport.DocCashDiscountForign : Double [R]
PaymentRunExport.DocCurrnecy : String [R]
PaymentRunExport.DocNum : Long [R]
PaymentRunExport.DocNumOffieldPaid : Long [R]
PaymentRunExport.DocRate : Double [R]
PaymentRunExport.EUInternalTransfer : BoYesNoEnum [R]
PaymentRunExport.FilePath : String [R]
PaymentRunExport.FiscalYear : Date [R]
PaymentRunExport.FormatName : String [R]
PaymentRunExport.FreeText1 : String [R]
PaymentRunExport.FreeText2 : String [R]
PaymentRunExport.FreeText3 : String [R]
PaymentRunExport.GLAccount : String [R]
PaymentRunExport.InstructionKey : String [R]
PaymentRunExport.Lines : PaymentRunExport_Lines [R]
PaymentRunExport.OrderingParty : String [R]
PaymentRunExport.OrganizationNumber : String [R]
PaymentRunExport.PayeeBankAccount : String [R]
PaymentRunExport.PayeeBankBISR : BoYesNoEnum [R]
PaymentRunExport.PayeeBankBlock : String [R]
PaymentRunExport.PayeeBankBranch : String [R]
PaymentRunExport.PayeeBankCity : String [R]
PaymentRunExport.PayeeBankCode : String [R]
PaymentRunExport.PayeeBankCountry : String [R]
PaymentRunExport.PayeeBankCounty : String [R]
PaymentRunExport.PayeeBankCtrlKey : String [R]
PaymentRunExport.PayeeBankHouseBank : BoYesNoEnum [R]
PaymentRunExport.PayeeBankIBAN : String [R]
PaymentRunExport.PayeeBankName : String [R]
PaymentRunExport.PayeeBankNextCheckNumber : Long [R]
PaymentRunExport.PayeeBankPostOffice : BoYesNoEnum [R]
PaymentRunExport.PayeeBankState : String [R]
PaymentRunExport.PayeeBankStreet : String [R]
PaymentRunExport.PayeeBankSwiftNum : String [R]
PaymentRunExport.PayeeBankUserNum1 : String [R]
PaymentRunExport.PayeeBankUserNum2 : String [R]
PaymentRunExport.PayeeBankUserNum3 : String [R]
PaymentRunExport.PayeeBankUserNum4 : String [R]
PaymentRunExport.PayeeBankZip : String [R]
PaymentRunExport.PayeeCity : String [R]
PaymentRunExport.PayeeCountry : String [R]
PaymentRunExport.PayeeName : String [R]
PaymentRunExport.PayeePostalCode : String [R]
PaymentRunExport.PayeeReferenceDetails : String [R]
PaymentRunExport.PayeeState : String [R]
PaymentRunExport.PayeeStreet : String [R]
PaymentRunExport.PayeeTaxNumber : String [R]
PaymentRunExport.PaymentBankBranch : String [R]
PaymentRunExport.PaymentBankCharges : String [R]
PaymentRunExport.PaymentBankChargesAllocationCode : String [R]
PaymentRunExport.PaymentBankControlKey : String [R]
PaymentRunExport.PaymentBankUserNo1 : String [R]
PaymentRunExport.PaymentBankUserNo2 : String [R]
PaymentRunExport.PaymentBankUserNo3 : String [R]
PaymentRunExport.PaymentBankUserNo4 : String [R]
PaymentRunExport.PaymentDonewithCheck : BoYesNoEnum [R]
PaymentRunExport.PaymentFormat : String [R]
PaymentRunExport.PaymentKeyCode : String [R]
PaymentRunExport.PaymentMethod : String [R]
PaymentRunExport.PaymentOrderNum : Long [R]
PaymentRunExport.PostingDate : Date [R]
PaymentRunExport.RowType : PaymentRunExportRowTypeEnum [R]
PaymentRunExport.RunDate : Date [R]
PaymentRunExport.Status : BoOpexStatus [R]
PaymentRunExport.UIPCode : String [R]
PaymentRunExport.UserDepartment : Long [R]
PaymentRunExport.UserEMail : String [R]
PaymentRunExport.UserFaxNumber : String [R]
PaymentRunExport.UserMobilePhoneNumber : String [R]
PaymentRunExport.UserName : String [R]
PaymentRunExport.VendorIsrBillerID : String [R]
PaymentRunExport.VendorNum : String [R]
PaymentRunExport.WizCode : Long [R]
PaymentRunExport.GetAsXML() -> String
PaymentRunExport.GetByKey(ByVal PaymentRunExportCode As Long) -> Boolean
PaymentRunExport.SaveToFile(ByVal FileName As String)
PaymentRunExport.SaveXML(ByRef FileName As String)
PaymentRunExport_Lines.BPDebitPayableAccount : String [R]
PaymentRunExport_Lines.Count : Long [R]
PaymentRunExport_Lines.CustomerNumber : String [R]
PaymentRunExport_Lines.DateOfPaymentRun : Date [R]
PaymentRunExport_Lines.DocumentCurrency : String [R]
PaymentRunExport_Lines.DocumentLocalCurrency : String [R]
PaymentRunExport_Lines.DocumentNumber : Long [R]
PaymentRunExport_Lines.DocumentObjectType : Long [R]
PaymentRunExport_Lines.DocumentObjectTypeEx : String [R]
PaymentRunExport_Lines.DocumentPaymentTerms : Long [R]
PaymentRunExport_Lines.DocumentPostingDate : Date [R]
PaymentRunExport_Lines.DocumentRate : Double [R]
PaymentRunExport_Lines.DocumentRemarks : String [R]
PaymentRunExport_Lines.DocumentTaxAmount : Double [R]
PaymentRunExport_Lines.DocumentTaxAmountFC : Double [R]
PaymentRunExport_Lines.DocumentTaxDate : Date [R]
PaymentRunExport_Lines.DocumentTotal : Double [R]
PaymentRunExport_Lines.DocumentTotalFC : Double [R]
PaymentRunExport_Lines.FiscalYear : Date [R]
PaymentRunExport_Lines.FreeText1 : String [R]
PaymentRunExport_Lines.FreeText2 : String [R]
PaymentRunExport_Lines.FreeText3 : String [R]
PaymentRunExport_Lines.PaymentDocNum : Long [R]
PaymentRunExport_Lines.PaymentDocReference : String [R]
PaymentRunExport_Lines.PaymentMeans : String [R]
PaymentRunExport_Lines.PaymentNumber : Long [R]
PaymentRunExport_Lines.PaymentOrderNum : Long [R]
PaymentRunExport_Lines.PaymentTermsPeriod : Long [R]
PaymentRunExport_Lines.PaymentWizardCode : String [R]
PaymentRunExport_Lines.RowNumber : Long [R]
PaymentRunExport_Lines.VendorNumber : String [R]
PaymentRunExport_Lines.VendorRefNum : String [R]
PaymentRunExport_Lines.SetCurrentLine(ByVal LineNum As Long)
Payments.AccountPayments : Payments_Accounts [R]
Payments.Address : String [R/W]
Payments.ApplyVAT : BoYesNoEnum [R/W]
Payments.AttachmentEntry : Long [R/W]
Payments.AuthorizationStatus : PaymentsAuthorizationStatusEnum [R]
Payments.BankAccount : String [R/W]
Payments.BankChargeAmount : Double [R/W]
Payments.BankChargeAmountInFC : Double [R]
Payments.BankChargeAmountInSC : Double [R]
Payments.BankCode : String [R/W]
Payments.BillOfExchange : BillOfExchange [R]
Payments.BillOfExchangeAgent : String [R/W]
Payments.BillOfExchangeAmount : Double [R/W]
Payments.BillOfExchangeAmountFC : Double [R]
Payments.BillOfExchangeAmountSC : Double [R]
Payments.BillofExchangeStatus : BoBoeStatus [R/W]
Payments.BlanketAgreement : Long [R/W]
Payments.BoeAccount : String [R/W]
Payments.BPLID : Long [R/W]
Payments.BPLName : String [R]
Payments.Browser : DataBrowser [R]
Payments.Cancelled : BoYesNoEnum [R]
Payments.CardCode : String [R/W]
Payments.CardName : String [R/W]
Payments.CashAccount : String [R/W]
Payments.CashSum : Double [R/W]
Payments.CashSumFC : Double [R]
Payments.CashSumSys : Double [R]
Payments.CertificationNumber : String [R]
Payments.CheckAccount : String [R/W]
Payments.Checks : Payments_Checks [R]
Payments.Cig : Long [R/W]
Payments.ContactPersonCode : Long [R/W]
Payments.ControlAccount : String [R/W]
Payments.CounterReference : String [R/W]
Payments.CreditCards : Payments_CreditCards [R]
Payments.Cup : Long [R/W]
Payments.DeductionPercent : Double [R/W]
Payments.DeductionSum : Double [R/W]
Payments.DocCurrency : String [R/W]
Payments.DocDate : Date [R/W]
Payments.DocEntry : Long [R]
Payments.DocNum : Long [R/W]
Payments.DocObjectCode : BoPaymentsObjectType [R/W]
Payments.DocRate : Double [R/W]
Payments.DocType : BoRcptTypes [R/W]
Payments.DocTypte : BoRcptTypes [R/W]
Payments.DocumentReferences : Payments_DocumentReferences [R]
Payments.DueDate : Date [R/W]
Payments.ElectronicProtocols : ElectronicProtocols [R]
Payments.HandWritten : BoYesNoEnum [R/W]
Payments.Invoices : Payments_Invoices [R]
Payments.IsPayToBank : BoYesNoEnum [R/W]
Payments.JournalRemarks : String [R/W]
Payments.LocalCurrency : BoYesNoEnum [R/W]
Payments.LocationCode : Long [R/W]
Payments.PaymentByWTCertif : BoYesNoEnum [R/W]
Payments.PaymentPriority : BoPaymentPriorities [R/W]
Payments.Payments_ApprovalRequests : Payments_ApprovalRequests [R]
Payments.PaymentType : BoORCTPaymentTypeEnum [R/W]
Payments.PayToBankAccountNo : String [R/W]
Payments.PayToBankBranch : String [R/W]
Payments.PayToBankCode : String [R/W]
Payments.PayToBankCountry : String [R/W]
Payments.PayToCode : String [R/W]
Payments.PrimaryFormItems : CashFlowAssignments [R]
Payments.Printed : BoYesNoEnum [R]
Payments.PrivateKeyVersion : Long [R]
Payments.Proforma : BoYesNoEnum [R/W]
Payments.ProjectCode : String [R/W]
Payments.Reference1 : String [R/W]
Payments.Reference2 : String [R/W]
Payments.Remarks : String [R/W]
Payments.Series : Long [R/W]
Payments.SignatureDigest : String [R]
Payments.SignatureInputMessage : String [R]
Payments.TaxDate : Date [R/W]
Payments.TaxGroup : String [R/W]
Payments.TransactionCode : String [R/W]
Payments.TransferAccount : String [R/W]
Payments.TransferDate : Date [R/W]
Payments.TransferRealAmount : Double [R/W]
Payments.TransferReference : String [R/W]
Payments.TransferSum : Double [R/W]
Payments.UnderOverpaymentdifference : Double [R]
Payments.UnderOverpaymentdiffFC : Double [R]
Payments.UnderOverpaymentdiffSC : Double [R]
Payments.UserFields : UserFields [R]
Payments.VatDate : Date [R/W]
Payments.VATRegNum : String [R]
Payments.WithholdingTaxCertificates : WithholdingTaxCertificates [R]
Payments.WithholdingTaxDataWTX : WithholdingTaxDataWTX [R]
Payments.WTAccount : String [R]
Payments.WTAmount : Double [R/W]
Payments.WTAmountFC : Double [R]
Payments.WTAmountSC : Double [R]
Payments.WtBaseSum : Double [R/W]
Payments.WtBaseSumFC : Double [R]
Payments.WtBaseSumSC : Double [R]
Payments.WTCode : String [R/W]
Payments.WTTaxableAmount : Double [R]
Payments.Add() -> Long
Payments.Cancel() -> Long
Payments.CancelbyCurrentSystemDate() -> Long
Payments.Close() -> Long
Payments.GetApprovalTemplates() -> Long
Payments.GetAsXML() -> String
Payments.GetByKey(ByVal RctEntry As Long) -> Boolean
Payments.Remove() -> Long
Payments.RequestApproveCancellation() -> Long
Payments.SaveDraftToDocument() -> Long
Payments.SaveToFile(ByVal FileName As String)
Payments.SaveXML(ByRef FileName As String)
Payments.Update() -> Long
Payments_Accounts.AccountCode : String [R/W]
Payments_Accounts.AccountName : String [R/W]
Payments_Accounts.Count : Long [R]
Payments_Accounts.Decription : String [R/W]
Payments_Accounts.EqualizationVatAmount : Double [R]
Payments_Accounts.GrossAmount : Double [R/W]
Payments_Accounts.LineNum : Long [R]
Payments_Accounts.LocationCode : Long [R]
Payments_Accounts.ProfitCenter : String [R/W]
Payments_Accounts.ProfitCenter2 : String [R/W]
Payments_Accounts.ProfitCenter3 : String [R/W]
Payments_Accounts.ProfitCenter4 : String [R/W]
Payments_Accounts.ProfitCenter5 : String [R/W]
Payments_Accounts.ProjectCode : String [R/W]
Payments_Accounts.SumPaid : Double [R/W]
Payments_Accounts.UserFields : UserFields [R]
Payments_Accounts.VatAmount : Double [R/W]
Payments_Accounts.VatGroup : String [R/W]
Payments_Accounts.Add()
Payments_Accounts.SetCurrentLine(ByVal LineNum As Long)
Payments_ApprovalRequests.ActiveForUpdate : BoYesNoEnum [R]
Payments_ApprovalRequests.ApprovalTemplatesID : Long [R]
Payments_ApprovalRequests.ApprovalTemplatesName : String [R]
Payments_ApprovalRequests.Count : Long [R]
Payments_ApprovalRequests.Remarks : String [R/W]
Payments_ApprovalRequests.SetCurrentLine(ByVal LineNum As Long)
Payments_Checks.AccounttNum : String [R/W]
Payments_Checks.BankCode : String [R/W]
Payments_Checks.Branch : String [R/W]
Payments_Checks.CheckAbsEntry : Long [R]
Payments_Checks.CheckAccount : String [R/W]
Payments_Checks.CheckNumber : Long [R/W]
Payments_Checks.CheckSum : Double [R/W]
Payments_Checks.Count : Long [R]
Payments_Checks.CountryCode : String [R/W]
Payments_Checks.Details : String [R/W]
Payments_Checks.DueDate : Date [R/W]
Payments_Checks.ECheck : BoYesNoEnum [R/W]
Payments_Checks.EndorsableCheckNo : Long [R/W]
Payments_Checks.Endorse : BoYesNoEnum [R/W]
Payments_Checks.FiscalID : String [R/W]
Payments_Checks.LineNum : Long [R]
Payments_Checks.ManualCheck : BoYesNoEnum [R/W]
Payments_Checks.OriginallyIssuedBy : String [R/W]
Payments_Checks.Trnsfrable : BoYesNoEnum [R/W]
Payments_Checks.UserFields : UserFields [R]
Payments_Checks.Add()
Payments_Checks.SetCurrentLine(ByVal LineNum As Long)
Payments_CreditCards.AdditionalPaymentSum : Double [R/W]
Payments_CreditCards.CardValidUntil : Date [R/W]
Payments_CreditCards.ConfirmationNum : String [R/W]
Payments_CreditCards.Count : Long [R]
Payments_CreditCards.CreditAcct : String [R/W]
Payments_CreditCards.CreditCard : Long [R/W]
Payments_CreditCards.CreditCardNumber : String [R/W]
Payments_CreditCards.CreditSum : Double [R/W]
Payments_CreditCards.CreditType : BoRcptCredTypes [R/W]
Payments_CreditCards.FirstPaymentDue : Date [R/W]
Payments_CreditCards.FirstPaymentSum : Double [R/W]
Payments_CreditCards.LineNum : Long [R]
Payments_CreditCards.NumOfCreditPayments : Long [R/W]
Payments_CreditCards.NumOfPayments : Long [R/W]
Payments_CreditCards.OwnerIdNum : String [R/W]
Payments_CreditCards.OwnerPhone : String [R/W]
Payments_CreditCards.PaymentMethodCode : Long [R/W]
Payments_CreditCards.SplitPayments : BoYesNoEnum [R/W]
Payments_CreditCards.UserFields : UserFields [R]
Payments_CreditCards.VoucherNum : String [R/W]
Payments_CreditCards.Add()
Payments_CreditCards.SetCurrentLine(ByVal LineNum As Long)
Payments_DocumentReferences.Count : Long [R]
Payments_DocumentReferences.DocEntry : Long [R]
Payments_DocumentReferences.ExternalReferencedDocNumber : String [R/W]
Payments_DocumentReferences.IssueDate : Date [R/W]
Payments_DocumentReferences.LineNumber : Long [R]
Payments_DocumentReferences.ReferencedDocEntry : Long [R/W]
Payments_DocumentReferences.ReferencedDocNumber : Long [R]
Payments_DocumentReferences.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
Payments_DocumentReferences.Remark : String [R/W]
Payments_DocumentReferences.Add()
Payments_DocumentReferences.Delete()
Payments_DocumentReferences.SetCurrentLine(ByVal LineNum As Long)
Payments_Invoices.AppliedFC : Double [R/W]
Payments_Invoices.Count : Long [R]
Payments_Invoices.DiscountPercent : Double [R/W]
Payments_Invoices.DistributionRule : String [R/W]
Payments_Invoices.DistributionRule2 : String [R/W]
Payments_Invoices.DistributionRule3 : String [R/W]
Payments_Invoices.DistributionRule4 : String [R/W]
Payments_Invoices.DistributionRule5 : String [R/W]
Payments_Invoices.DocEntry : Long [R/W]
Payments_Invoices.DocLine : Long [R/W]
Payments_Invoices.DocNum : Long [R]
Payments_Invoices.InstallmentId : Long [R/W]
Payments_Invoices.InvoiceType : BoRcptInvTypes [R/W]
Payments_Invoices.LineNum : Long [R]
Payments_Invoices.LinkDate : Date [R]
Payments_Invoices.PaidSum : Double [R]
Payments_Invoices.SumApplied : Double [R/W]
Payments_Invoices.TotalDiscount : Double [R/W]
Payments_Invoices.TotalDiscountFC : Double [R/W]
Payments_Invoices.TotalDiscountSC : Double [R]
Payments_Invoices.UserFields : UserFields [R]
Payments_Invoices.WitholdingTaxApplied : Double [R]
Payments_Invoices.WitholdingTaxAppliedFC : Double [R]
Payments_Invoices.WitholdingTaxAppliedSC : Double [R]
Payments_Invoices.Add()
Payments_Invoices.SetCurrentLine(ByVal LineNum As Long)
PaymentTermsTypes.BaselineDate : BoBaselineDate [R/W]
PaymentTermsTypes.Browser : DataBrowser [R]
PaymentTermsTypes.CreditLimit : Double [R/W]
PaymentTermsTypes.DiscountCode : String [R/W]
PaymentTermsTypes.DunningCode : String [R/W]
PaymentTermsTypes.GeneralDiscount : Double [R/W]
PaymentTermsTypes.GroupNumber : Long [R]
PaymentTermsTypes.InterestOnArrears : Double [R/W]
PaymentTermsTypes.LoadLimit : Double [R/W]
PaymentTermsTypes.NumberOfAdditionalDays : Long [R/W]
PaymentTermsTypes.NumberOfAdditionalMonths : Long [R/W]
PaymentTermsTypes.NumberOfInstallments : Long [R]
PaymentTermsTypes.NumberOfToleranceDays : Long [R/W]
PaymentTermsTypes.OpenReceipt : BoOpenIncPayment [R/W]
PaymentTermsTypes.PaymentTermsGroupName : String [R/W]
PaymentTermsTypes.PriceListNo : Long [R/W]
PaymentTermsTypes.StartFrom : BoPayTermDueTypes [R/W]
PaymentTermsTypes.UserFields : UserFields [R]
PaymentTermsTypes.Add() -> Long
PaymentTermsTypes.Close() -> Long
PaymentTermsTypes.GetAsXML() -> String
PaymentTermsTypes.GetByKey(ByVal GroupNum As Long) -> Boolean
PaymentTermsTypes.Remove() -> Long
PaymentTermsTypes.SaveToFile(ByVal FileName As String)
PaymentTermsTypes.SaveXML(ByRef FileName As String)
PaymentTermsTypes.Update() -> Long
PaymentTermsTypes.UpdateWithBPs() -> Long
PeriodCategory.AccountforCashReceipt : String [R/W]
PeriodCategory.AccountforCreditMemoPayme : String [R/W]
PeriodCategory.AccountforOutgoingChecks : String [R/W]
PeriodCategory.AcountforOpeningWHBalance : String [R/W]
PeriodCategory.AllocationAcc : String [R/W]
PeriodCategory.APCashDiscountAccount : String [R/W]
PeriodCategory.APCashDiscountInterim : String [R/W]
PeriodCategory.APExRateInterim : String [R/W]
PeriodCategory.APGainRealizedConversionDiff : String [R/W]
PeriodCategory.APGainRealizedExchngeDif : String [R/W]
PeriodCategory.APLossCashDiscountAccount : String [R/W]
PeriodCategory.APLossRealizedConversionDiff : String [R/W]
PeriodCategory.APLossRealizedExchangeDif : String [R/W]
PeriodCategory.ARCashDiscountAccount : String [R/W]
PeriodCategory.ARCashDiscountInterim : String [R/W]
PeriodCategory.ARExRateInterim : String [R/W]
PeriodCategory.ARGainRealizedConversionDiff : String [R/W]
PeriodCategory.ARGainRealizedExchngeDif : String [R/W]
PeriodCategory.ARLossRealizedConversionDiff : String [R/W]
PeriodCategory.ARLossRealizedExchangeDi : String [R/W]
PeriodCategory.BeginningofFinancialYear : Date [R/W]
PeriodCategory.BillofExchangeAccountsRece : String [R/W]
PeriodCategory.BoEAccountsPayable : String [R/W]
PeriodCategory.BoEAccountsPayable2 : String [R/W]
PeriodCategory.CommissionAccountDefault : String [R/W]
PeriodCategory.CostOfGoodsSold : String [R/W]
PeriodCategory.CostofSaleRevaluationAcct : String [R/W]
PeriodCategory.CostofSaleRevOffsetAcct : String [R/W]
PeriodCategory.CreditorsFollowUpAccount : String [R/W]
PeriodCategory.CustBillofExchangeonC : String [R/W]
PeriodCategory.CustomerBillofExchangePres : String [R/W]
PeriodCategory.CustomerBillofExchngeDisc : String [R/W]
PeriodCategory.CustomerDoubtfulDebtsAcct : String [R/W]
PeriodCategory.CustomerDownPaymentsAccount : String [R/W]
PeriodCategory.CustomersDeductionatSource : String [R/W]
PeriodCategory.CustomerUnpaidBoE : String [R/W]
PeriodCategory.DebitorsFollowUpAccount : String [R/W]
PeriodCategory.DecreaseGLAcc : String [R/W]
PeriodCategory.DefaultSaleAccount : String [R/W]
PeriodCategory.DownPaymentPClearingAcct : String [R/W]
PeriodCategory.DownPaymentSClearingAcct : String [R/W]
PeriodCategory.DownPaymentVATAcctPurch : String [R/W]
PeriodCategory.DownPaymentVATAcctSale : String [R/W]
PeriodCategory.DunningFeeAccount : String [R/W]
PeriodCategory.DunningInterestAccount : String [R/W]
PeriodCategory.EOYControlAccount : String [R/W]
PeriodCategory.EUAccountsPayable : String [R/W]
PeriodCategory.EUAccountsReceivable : String [R/W]
PeriodCategory.EUExpenseAccount : String [R/W]
PeriodCategory.EUPurchaseCreditAcc : String [R/W]
PeriodCategory.ExchangeRateDifferencesAcct : String [R/W]
PeriodCategory.ExemptedCredits : String [R/W]
PeriodCategory.ExhRatesDiffAcctLnWTax : String [R/W]
PeriodCategory.ExpenseAccountDefault : String [R/W]
PeriodCategory.ExpenseClearingAccount : String [R/W]
PeriodCategory.ExpenseOffsetAccount : String [R/W]
PeriodCategory.ExpensesAccountForeign : String [R/W]
PeriodCategory.ExpenseVarianceAccount : String [R/W]
PeriodCategory.FinancialYear : Long [R/W]
PeriodCategory.ForeignAccountsReceivables : String [R/W]
PeriodCategory.ForeignPurchaseCreditAcc : String [R/W]
PeriodCategory.FromDocumentDate : Date [R/W]
PeriodCategory.FromDueDate : Date [R/W]
PeriodCategory.FromPostingDate : Date [R/W]
PeriodCategory.GLGainRealizedConversionDiff : String [R/W]
PeriodCategory.GLLossRealizedConversionDiff : String [R/W]
PeriodCategory.GLRevaluationOffsetAccount : String [R/W]
PeriodCategory.GoodsClearingAcc : String [R/W]
PeriodCategory.IncreaseGLAccount : String [R/W]
PeriodCategory.InputTaxAccount : String [R/W]
PeriodCategory.InventoryOffsetDecrease : String [R/W]
PeriodCategory.InventoryOffsetIncrease : String [R/W]
PeriodCategory.InventoryOffsetProfitAndLossAccount : String [R/W]
PeriodCategory.InvoicePaymentBP : String [R/W]
PeriodCategory.NegativeInventoryAdjustmentAccount : String [R/W]
PeriodCategory.NumberOfPeriods : Long [R/W]
PeriodCategory.OpeningBalancesAccount : String [R/W]
PeriodCategory.OutgoingCashAccount : String [R/W]
PeriodCategory.OutgoingChecksAccount : String [R/W]
PeriodCategory.OutgoingTaxAccount : String [R/W]
PeriodCategory.OverpaymentsAPAccount : String [R/W]
PeriodCategory.OverpaymentsARAccount : String [R/W]
PeriodCategory.PeriodCategory : String [R/W]
PeriodCategory.PeriodName : String [R/W]
PeriodCategory.PriceDifferenceAccount : String [R/W]
PeriodCategory.PurchaseAccount : String [R/W]
PeriodCategory.PurchaseCreditAcc : String [R/W]
PeriodCategory.PurchaseDownPaymentInterimAccount : String [R/W]
PeriodCategory.PurchaseInterimAcctLnWTax : String [R/W]
PeriodCategory.PurchaseOffsetAccount : String [R/W]
PeriodCategory.PurchaseReturnAccount : String [R/W]
PeriodCategory.PurchaseTax : String [R/W]
PeriodCategory.RateDifferencesDefaultAcc : String [R/W]
PeriodCategory.ReconciliationDifference : String [R/W]
PeriodCategory.RepomoAccount : String [R/W]
PeriodCategory.RevenuesAccountForeign : String [R/W]
PeriodCategory.RoundingAccount : String [R/W]
PeriodCategory.SalesCreditAcc : String [R/W]
PeriodCategory.SalesCreditEUAcc : String [R/W]
PeriodCategory.SalesCreditForeignAcc : String [R/W]
PeriodCategory.SalesDownPaymentInterimAccount : String [R/W]
PeriodCategory.SalesInterimAcctLnWTax : String [R/W]
PeriodCategory.SalesReturns : String [R/W]
PeriodCategory.SalesRevenueEU : String [R/W]
PeriodCategory.SelfInvoiceExpenseAccount : String [R/W]
PeriodCategory.SelfInvoiceRevenueAccount : String [R/W]
PeriodCategory.StockAccount : String [R/W]
PeriodCategory.StockInTransitAccount : String [R/W]
PeriodCategory.StockRevaluationAccount : String [R/W]
PeriodCategory.StockRevaluationOffsetAcct : String [R/W]
PeriodCategory.SubPeriodType : BoSubPeriodTypeEnum [R/W]
PeriodCategory.TaxDefinition : String [R/W]
PeriodCategory.TaxExemptRevenuesDefault : String [R/W]
PeriodCategory.ToDocumentDate : Date [R/W]
PeriodCategory.ToDueDate : Date [R/W]
PeriodCategory.ToPostingDate : Date [R/W]
PeriodCategory.UnderpaymentsAPAccount : String [R/W]
PeriodCategory.UnderpaymentsARAccount : String [R/W]
PeriodCategory.VarianceAcc : String [R/W]
PeriodCategory.VendorAssetsAccount : String [R/W]
PeriodCategory.VendorDoubtfulDebtsAcct : String [R/W]
PeriodCategory.VendorDownPaymentsAccount : String [R/W]
PeriodCategory.WIPMappingCollection : WIPMappingCollection [R]
PeriodCategory.WIPMaterialAccount : String [R/W]
PeriodCategory.WIPMaterialVarianceAccount : String [R/W]
PeriodCategory.WipOffsetProfitAndLossAccount : String [R/W]
PeriodCategory.WithholodingTax : String [R/W]
PeriodCategory.FromXMLFile(ByVal bstrFileName As String)
PeriodCategory.FromXMLString(ByVal bstrXML As String)
PeriodCategory.GetXMLSchema() -> String
PeriodCategory.ToXMLFile(ByVal bstrFileName As String)
PeriodCategory.ToXMLString() -> String
PeriodCategoryParams.AbsoluteEntry : Long [R/W]
PeriodCategoryParams.FromXMLFile(ByVal bstrFileName As String)
PeriodCategoryParams.FromXMLString(ByVal bstrXML As String)
PeriodCategoryParams.GetXMLSchema() -> String
PeriodCategoryParams.ToXMLFile(ByVal bstrFileName As String)
PeriodCategoryParams.ToXMLString() -> String
PeriodCategoryParamsCollection.Count : Long [R]
PeriodCategoryParamsCollection.Add() -> PeriodCategoryParams
PeriodCategoryParamsCollection.GetXMLSchema() -> String
PeriodCategoryParamsCollection.Item(ByVal vtIndex As Variant) -> PeriodCategoryParams
PeriodCategoryParamsCollection.ToXMLFile(ByVal bstrFileName As String)
PeriodCategoryParamsCollection.ToXMLString() -> String
PickLists.AbsoluteEntry : Long [R]
PickLists.Browser : DataBrowser [R]
PickLists.Lines : PickLists_Lines [R]
PickLists.Name : String [R/W]
PickLists.ObjectType : String [R]
PickLists.OwnerCode : Long [R/W]
PickLists.OwnerName : String [R]
PickLists.PickDate : Date [R/W]
PickLists.Remarks : String [R/W]
PickLists.Status : BoPickStatus [R]
PickLists.UseBaseUnits : BoYesNoEnum [R/W]
PickLists.UserFields : UserFields [R]
PickLists.Add() -> Long
PickLists.Close() -> Long
PickLists.GetAsXML() -> String
PickLists.GetByKey(ByVal lAbsEntry As Long) -> Boolean
PickLists.GetReleasedAllocation(ByVal lAbsEntry As Long) -> Boolean
PickLists.SaveToFile(ByVal bstrFileName As String)
PickLists.SaveXML(ByRef pbstrFileName As String)
PickLists.Update() -> Long
PickLists.UpdateReleasedAllocation() -> Long
PickLists_Lines.AbsoluteEntry : Long [R]
PickLists_Lines.BaseObjectType : String [R/W]
PickLists_Lines.BatchNumbers : BatchNumbers [R]
PickLists_Lines.BinAllocations : DocumentLinesBinAllocations [R]
PickLists_Lines.Count : Long [R]
PickLists_Lines.LineNumber : Long [R]
PickLists_Lines.OrderEntry : Long [R/W]
PickLists_Lines.OrderRowID : Long [R/W]
PickLists_Lines.PickedQuantity : Double [R/W]
PickLists_Lines.PickStatus : BoPickStatus [R]
PickLists_Lines.PreviouslyReleasedQuantity : Double [R]
PickLists_Lines.ReleasedQuantity : Double [R/W]
PickLists_Lines.SerialNumbers : SerialNumbers [R]
PickLists_Lines.UserFields : UserFields [R]
PickLists_Lines.Add()
PickLists_Lines.SetCurrentLine(ByVal LineNum As Long)
PM_ActivitiesCollection.Count : Long [R]
PM_ActivitiesCollection.Add() -> PM_ActivityData
PM_ActivitiesCollection.GetXMLSchema() -> String
PM_ActivitiesCollection.Item(ByVal vtIndex As Variant) -> PM_ActivityData
PM_ActivitiesCollection.ToXMLFile(ByVal bstrFileName As String)
PM_ActivitiesCollection.ToXMLString() -> String
PM_ActivityData.ActivityID : Long [R/W]
PM_ActivityData.LineId : Long [R]
PM_ActivityData.StageID : Long [R/W]
PM_ActivityData.UserFields : Fields [R]
PM_ActivityData.FromXMLFile(ByVal bstrFileName As String)
PM_ActivityData.FromXMLString(ByVal bstrXML As String)
PM_ActivityData.GetXMLSchema() -> String
PM_ActivityData.ToXMLFile(ByVal bstrFileName As String)
PM_ActivityData.ToXMLString() -> String
PM_DocAttachement.AbsEntry : Long [R]
PM_DocAttachement.AttachementDate : Date [R/W]
PM_DocAttachement.FileExtension : String [R/W]
PM_DocAttachement.FileName : String [R/W]
PM_DocAttachement.LineId : Long [R]
PM_DocAttachement.SourcePath : String [R/W]
PM_DocAttachement.FromXMLFile(ByVal bstrFileName As String)
PM_DocAttachement.FromXMLString(ByVal bstrXML As String)
PM_DocAttachement.GetXMLSchema() -> String
PM_DocAttachement.ToXMLFile(ByVal bstrFileName As String)
PM_DocAttachement.ToXMLString() -> String
PM_DocAttachements.Count : Long [R]
PM_DocAttachements.Add() -> PM_DocAttachement
PM_DocAttachements.GetXMLSchema() -> String
PM_DocAttachements.Item(ByVal vtIndex As Variant) -> PM_DocAttachement
PM_DocAttachements.ToXMLFile(ByVal bstrFileName As String)
PM_DocAttachements.ToXMLString() -> String
PM_DocumentData.AmountCategory : AmountCatTypeEnum [R]
PM_DocumentData.Categorize : PMCategorizeTypeEnum [R/W]
PM_DocumentData.DocDate : Date [R]
PM_DocumentData.DocEntry : Long [R/W]
PM_DocumentData.DocType : PMDocumentTypeEnum [R/W]
PM_DocumentData.LineId : Long [R]
PM_DocumentData.LineNumber : Long [R/W]
PM_DocumentData.Operation : PMOperationTypeEnum [R/W]
PM_DocumentData.StageID : Long [R/W]
PM_DocumentData.Status : LineStatusTypeEnum [R]
PM_DocumentData.Total : Double [R]
PM_DocumentData.UserFields : Fields [R]
PM_DocumentData.FromXMLFile(ByVal bstrFileName As String)
PM_DocumentData.FromXMLString(ByVal bstrXML As String)
PM_DocumentData.GetXMLSchema() -> String
PM_DocumentData.ToXMLFile(ByVal bstrFileName As String)
PM_DocumentData.ToXMLString() -> String
PM_DocumentsCollection.Count : Long [R]
PM_DocumentsCollection.Add() -> PM_DocumentData
PM_DocumentsCollection.GetXMLSchema() -> String
PM_DocumentsCollection.Item(ByVal vtIndex As Variant) -> PM_DocumentData
PM_DocumentsCollection.ToXMLFile(ByVal bstrFileName As String)
PM_DocumentsCollection.ToXMLString() -> String
PM_OpenIssueData.Area : Long [R/W]
PM_OpenIssueData.Closed : BoYesNoEnum [R/W]
PM_OpenIssueData.Effort : Double [R/W]
PM_OpenIssueData.EnteredBy : Long [R/W]
PM_OpenIssueData.EnteredDate : Date [R/W]
PM_OpenIssueData.LineId : Long [R]
PM_OpenIssueData.Priority : Long [R/W]
PM_OpenIssueData.Remarks : String [R/W]
PM_OpenIssueData.Responsible : Long [R/W]
PM_OpenIssueData.SolutionID : Long [R/W]
PM_OpenIssueData.StageID : Long [R/W]
PM_OpenIssueData.UserFields : Fields [R]
PM_OpenIssueData.FromXMLFile(ByVal bstrFileName As String)
PM_OpenIssueData.FromXMLString(ByVal bstrXML As String)
PM_OpenIssueData.GetXMLSchema() -> String
PM_OpenIssueData.ToXMLFile(ByVal bstrFileName As String)
PM_OpenIssueData.ToXMLString() -> String
PM_OpenIssuesCollection.Count : Long [R]
PM_OpenIssuesCollection.Add() -> PM_OpenIssueData
PM_OpenIssuesCollection.GetXMLSchema() -> String
PM_OpenIssuesCollection.Item(ByVal vtIndex As Variant) -> PM_OpenIssueData
PM_OpenIssuesCollection.ToXMLFile(ByVal bstrFileName As String)
PM_OpenIssuesCollection.ToXMLString() -> String
PM_ProjectDocumentData.AbsEntry : Long [R/W]
PM_ProjectDocumentData.AllowSubprojects : BoYesNoEnum [R/W]
PM_ProjectDocumentData.AttachmentEntry : Long [R/W]
PM_ProjectDocumentData.BusinessPartner : String [R/W]
PM_ProjectDocumentData.BusinessPartnerName : String [R/W]
PM_ProjectDocumentData.ClosingDate : Date [R/W]
PM_ProjectDocumentData.ContactPerson : Long [R/W]
PM_ProjectDocumentData.DocNum : Long [R]
PM_ProjectDocumentData.DueDate : Date [R/W]
PM_ProjectDocumentData.FinancialProject : String [R/W]
PM_ProjectDocumentData.FinishedPercent : Double [R/W]
PM_ProjectDocumentData.Industry : Long [R/W]
PM_ProjectDocumentData.Owner : Long [R/W]
PM_ProjectDocumentData.PM_ActivitiesCollection : PM_ActivitiesCollection [R]
PM_ProjectDocumentData.PM_DocAttachements : PM_DocAttachements [R]
PM_ProjectDocumentData.PM_DocumentsCollection : PM_DocumentsCollection [R]
PM_ProjectDocumentData.PM_OpenIssuesCollection : PM_OpenIssuesCollection [R]
PM_ProjectDocumentData.PM_StageAttachements : PM_StageAttachements [R]
PM_ProjectDocumentData.PM_StagesCollection : PM_StagesCollection [R]
PM_ProjectDocumentData.PM_SummaryData : PM_SummaryData [R]
PM_ProjectDocumentData.PM_WorkOrdersCollection : PM_WorkOrdersCollection [R]
PM_ProjectDocumentData.ProjectName : String [R/W]
PM_ProjectDocumentData.ProjectStatus : ProjectStatusTypeEnum [R/W]
PM_ProjectDocumentData.ProjectType : ProjectTypeEnum [R/W]
PM_ProjectDocumentData.Reason : String [R/W]
PM_ProjectDocumentData.RiskLevel : RiskLevelTypeEnum [R/W]
PM_ProjectDocumentData.SalesEmployee : Long [R/W]
PM_ProjectDocumentData.Series : Long [R]
PM_ProjectDocumentData.StartDate : Date [R/W]
PM_ProjectDocumentData.Territory : Long [R/W]
PM_ProjectDocumentData.UserFields : Fields [R]
PM_ProjectDocumentData.FromXMLFile(ByVal bstrFileName As String)
PM_ProjectDocumentData.FromXMLString(ByVal bstrXML As String)
PM_ProjectDocumentData.GetXMLSchema() -> String
PM_ProjectDocumentData.ToXMLFile(ByVal bstrFileName As String)
PM_ProjectDocumentData.ToXMLString() -> String
PM_ProjectDocumentParams.AbsEntry : Long [R/W]
PM_ProjectDocumentParams.FromXMLFile(ByVal bstrFileName As String)
PM_ProjectDocumentParams.FromXMLString(ByVal bstrXML As String)
PM_ProjectDocumentParams.GetXMLSchema() -> String
PM_ProjectDocumentParams.ToXMLFile(ByVal bstrFileName As String)
PM_ProjectDocumentParams.ToXMLString() -> String
PM_StageAttachement.AbsEntry : Long [R]
PM_StageAttachement.AttachementDate : Date [R/W]
PM_StageAttachement.FileExtension : String [R/W]
PM_StageAttachement.FileName : String [R/W]
PM_StageAttachement.LineId : Long [R]
PM_StageAttachement.SourcePath : String [R/W]
PM_StageAttachement.FromXMLFile(ByVal bstrFileName As String)
PM_StageAttachement.FromXMLString(ByVal bstrXML As String)
PM_StageAttachement.GetXMLSchema() -> String
PM_StageAttachement.ToXMLFile(ByVal bstrFileName As String)
PM_StageAttachement.ToXMLString() -> String
PM_StageAttachements.Count : Long [R]
PM_StageAttachements.Add() -> PM_StageAttachement
PM_StageAttachements.GetXMLSchema() -> String
PM_StageAttachements.Item(ByVal vtIndex As Variant) -> PM_StageAttachement
PM_StageAttachements.ToXMLFile(ByVal bstrFileName As String)
PM_StageAttachements.ToXMLString() -> String
PM_StageData.AttachmentEntry : Long [R/W]
PM_StageData.CloseDate : Date [R/W]
PM_StageData.DependsOnStage1 : Long [R/W]
PM_StageData.DependsOnStage2 : Long [R/W]
PM_StageData.DependsOnStage3 : Long [R/W]
PM_StageData.DependsOnStage4 : Long [R/W]
PM_StageData.DependsOnStageID1 : Long [R/W]
PM_StageData.DependsOnStageID2 : Long [R/W]
PM_StageData.DependsOnStageID3 : Long [R/W]
PM_StageData.DependsOnStageID4 : Long [R/W]
PM_StageData.Description : String [R/W]
PM_StageData.ExpectedCosts : Double [R/W]
PM_StageData.FinishedDate : Date [R/W]
PM_StageData.InvoicedAmountPurchase : Double [R/W]
PM_StageData.InvoicedAmountSales : Double [R/W]
PM_StageData.IsFinished : BoYesNoEnum [R/W]
PM_StageData.LineId : Long [R]
PM_StageData.OpenAmountPurchase : Double [R/W]
PM_StageData.OpenAmountSales : Double [R/W]
PM_StageData.PercentualCompletness : Double [R/W]
PM_StageData.StageDependency1Type : StageDepTypeEnum [R/W]
PM_StageData.StageDependency2Type : StageDepTypeEnum [R/W]
PM_StageData.StageDependency3Type : StageDepTypeEnum [R/W]
PM_StageData.StageDependency4Type : StageDepTypeEnum [R/W]
PM_StageData.StageID : Long [R/W]
PM_StageData.StageOwner : Long [R/W]
PM_StageData.StageType : Long [R/W]
PM_StageData.StartDate : Date [R/W]
PM_StageData.Task : Long [R/W]
PM_StageData.UniqueID : String [R/W]
PM_StageData.UserFields : Fields [R]
PM_StageData.FromXMLFile(ByVal bstrFileName As String)
PM_StageData.FromXMLString(ByVal bstrXML As String)
PM_StageData.GetXMLSchema() -> String
PM_StageData.ToXMLFile(ByVal bstrFileName As String)
PM_StageData.ToXMLString() -> String
PM_StagesCollection.Count : Long [R]
PM_StagesCollection.Add() -> PM_StageData
PM_StagesCollection.GetXMLSchema() -> String
PM_StagesCollection.Item(ByVal vtIndex As Variant) -> PM_StageData
PM_StagesCollection.ToXMLFile(ByVal bstrFileName As String)
PM_StagesCollection.ToXMLString() -> String
PM_SubprojectDocumentData.AbsEntry : Long [R/W]
PM_SubprojectDocumentData.ActualCost : Double [R/W]
PM_SubprojectDocumentData.DueDate : Date [R/W]
PM_SubprojectDocumentData.FinishedPercent : Double [R/W]
PM_SubprojectDocumentData.Order : Long [R/W]
PM_SubprojectDocumentData.Owner : Long [R/W]
PM_SubprojectDocumentData.ParentID : Long [R/W]
PM_SubprojectDocumentData.PlannedCost : Double [R/W]
PM_SubprojectDocumentData.PMS_ActivitiesCollection : PMS_ActivitiesCollection [R]
PM_SubprojectDocumentData.PMS_DocAttachements : PMS_DocAttachements [R]
PM_SubprojectDocumentData.PMS_DocumentsCollection : PMS_DocumentsCollection [R]
PM_SubprojectDocumentData.PMS_OpenIssuesCollection : PMS_OpenIssuesCollection [R]
PM_SubprojectDocumentData.PMS_StageAttachements : PMS_StageAttachements [R]
PM_SubprojectDocumentData.PMS_StagesCollection : PMS_StagesCollection [R]
PM_SubprojectDocumentData.PMS_SummaryData : PMS_SummaryData [R]
PM_SubprojectDocumentData.PMS_WorkOrdersCollection : PMS_WorkOrdersCollection [R]
PM_SubprojectDocumentData.ProjectID : Long [R/W]
PM_SubprojectDocumentData.StartDate : Date [R/W]
PM_SubprojectDocumentData.SubprojectContribution : Double [R/W]
PM_SubprojectDocumentData.SubprojectDepth : Long [R]
PM_SubprojectDocumentData.SubprojectEndDate : Date [R/W]
PM_SubprojectDocumentData.SubprojectName : String [R/W]
PM_SubprojectDocumentData.SubprojectStatus : SubprojectStatusTypeEnum [R/W]
PM_SubprojectDocumentData.SubprojectType : Long [R/W]
PM_SubprojectDocumentData.UserFields : Fields [R]
PM_SubprojectDocumentData.FromXMLFile(ByVal bstrFileName As String)
PM_SubprojectDocumentData.FromXMLString(ByVal bstrXML As String)
PM_SubprojectDocumentData.GetXMLSchema() -> String
PM_SubprojectDocumentData.ToXMLFile(ByVal bstrFileName As String)
PM_SubprojectDocumentData.ToXMLString() -> String
PM_SubprojectDocumentParams.AbsEntry : Long [R/W]
PM_SubprojectDocumentParams.FromXMLFile(ByVal bstrFileName As String)
PM_SubprojectDocumentParams.FromXMLString(ByVal bstrXML As String)
PM_SubprojectDocumentParams.GetXMLSchema() -> String
PM_SubprojectDocumentParams.ToXMLFile(ByVal bstrFileName As String)
PM_SubprojectDocumentParams.ToXMLString() -> String
PM_SubprojectDocumentsCollection.Count : Long [R]
PM_SubprojectDocumentsCollection.Add() -> PM_SubprojectDocumentParams
PM_SubprojectDocumentsCollection.GetXMLSchema() -> String
PM_SubprojectDocumentsCollection.Item(ByVal vtIndex As Variant) -> PM_SubprojectDocumentParams
PM_SubprojectDocumentsCollection.ToXMLFile(ByVal bstrFileName As String)
PM_SubprojectDocumentsCollection.ToXMLString() -> String
PM_SubprojectParams.AbsEntry : Long [R/W]
PM_SubprojectParams.IsSubproject : BoYesNoEnum [R/W]
PM_SubprojectParams.FromXMLFile(ByVal bstrFileName As String)
PM_SubprojectParams.FromXMLString(ByVal bstrXML As String)
PM_SubprojectParams.GetXMLSchema() -> String
PM_SubprojectParams.ToXMLFile(ByVal bstrFileName As String)
PM_SubprojectParams.ToXMLString() -> String
PM_SummaryData.AccumInvoicedAmountPurchase : Double [R]
PM_SummaryData.AccumInvoicedAmountSales : Double [R]
PM_SummaryData.AccumOpenAmountPurchase : Double [R]
PM_SummaryData.AccumOpenAmountSales : Double [R]
PM_SummaryData.AccumPotentialSubprojectAmount : Double [R]
PM_SummaryData.AccumSubprojectBudget : Double [R]
PM_SummaryData.AccumTotalPurchase : Double [R]
PM_SummaryData.AccumTotalSales : Double [R]
PM_SummaryData.AccumTotalVariancePurchase : Double [R]
PM_SummaryData.AccumTotalVarianceSales : Double [R]
PM_SummaryData.AccumVariancePerceptionPurchase : Double [R]
PM_SummaryData.AccumVariancePerceptionSales : Double [R]
PM_SummaryData.ActualAdditionalCost : Double [R]
PM_SummaryData.ActualByProductCost : Double [R]
PM_SummaryData.ActualClosingDate : Date [R]
PM_SummaryData.ActualItemComponentCost : Double [R]
PM_SummaryData.ActualProductCost : Double [R]
PM_SummaryData.ActualResourceComponentCost : Double [R]
PM_SummaryData.DueDate : Date [R]
PM_SummaryData.LineId : Long [R]
PM_SummaryData.Overdue : Long [R]
PM_SummaryData.PotentialSubprojectAmount : Double [R/W]
PM_SummaryData.SubprojectBudget : Double [R]
PM_SummaryData.SumInvoicedAmountPurchase : Double [R]
PM_SummaryData.SumInvoicedAmountSales : Double [R]
PM_SummaryData.SumOpenAmountPurchase : Double [R]
PM_SummaryData.SumOpenAmountSales : Double [R]
PM_SummaryData.TotalAmountPurchase : Double [R]
PM_SummaryData.TotalAmountSales : Double [R]
PM_SummaryData.TotalVariance : Double [R]
PM_SummaryData.TotalVariancePurchase : Double [R]
PM_SummaryData.TotalVarianceSales : Double [R]
PM_SummaryData.VariancePerceptionPurchase : Double [R]
PM_SummaryData.VariancePerceptionSales : Double [R]
PM_SummaryData.FromXMLFile(ByVal bstrFileName As String)
PM_SummaryData.FromXMLString(ByVal bstrXML As String)
PM_SummaryData.GetXMLSchema() -> String
PM_SummaryData.ToXMLFile(ByVal bstrFileName As String)
PM_SummaryData.ToXMLString() -> String
PM_TimeSheetData.AbsEntry : Long [R/W]
PM_TimeSheetData.AttachmentEntry : Long [R/W]
PM_TimeSheetData.DateFrom : Date [R/W]
PM_TimeSheetData.Dateto : Date [R/W]
PM_TimeSheetData.Department : Long [R/W]
PM_TimeSheetData.DocNumber : Long [R]
PM_TimeSheetData.FirstName : String [R/W]
PM_TimeSheetData.LastName : String [R/W]
PM_TimeSheetData.PM_TimeSheetLineDataCollection : PM_TimeSheetLineDataCollection [R]
PM_TimeSheetData.SAPPassport : String [R]
PM_TimeSheetData.TimeSheetType : TimeSheetTypeEnum [R/W]
PM_TimeSheetData.UserCode : String [R/W]
PM_TimeSheetData.UserFields : Fields [R]
PM_TimeSheetData.UserID : Long [R/W]
PM_TimeSheetData.FromXMLFile(ByVal bstrFileName As String)
PM_TimeSheetData.FromXMLString(ByVal bstrXML As String)
PM_TimeSheetData.GetXMLSchema() -> String
PM_TimeSheetData.ToXMLFile(ByVal bstrFileName As String)
PM_TimeSheetData.ToXMLString() -> String
PM_TimeSheetLineData.ActivityType : Long [R/W]
PM_TimeSheetLineData.BillableTime : Date [R]
PM_TimeSheetLineData.Branch : Long [R/W]
PM_TimeSheetLineData.Break : Date [R/W]
PM_TimeSheetLineData.CostCenter : String [R/W]
PM_TimeSheetLineData.Date : Date [R/W]
PM_TimeSheetLineData.EffectiveTime : Date [R]
PM_TimeSheetLineData.EndTime : Date [R/W]
PM_TimeSheetLineData.FinancialProject : String [R/W]
PM_TimeSheetLineData.FullDay : BoYesNoEnum [R/W]
PM_TimeSheetLineData.GPSData : String [R/W]
PM_TimeSheetLineData.LaborItem : String [R/W]
PM_TimeSheetLineData.LineId : Long [R]
PM_TimeSheetLineData.Location : Long [R/W]
PM_TimeSheetLineData.NonBillableTime : Date [R/W]
PM_TimeSheetLineData.ProjectID : Long [R/W]
PM_TimeSheetLineData.ServiceCall : Long [R/W]
PM_TimeSheetLineData.StageID : Long [R/W]
PM_TimeSheetLineData.StartTime : Date [R/W]
PM_TimeSheetLineData.SubprojectID : Long [R/W]
PM_TimeSheetLineData.UserFields : Fields [R]
PM_TimeSheetLineData.Workorder : Long [R/W]
PM_TimeSheetLineData.FromXMLFile(ByVal bstrFileName As String)
PM_TimeSheetLineData.FromXMLString(ByVal bstrXML As String)
PM_TimeSheetLineData.GetXMLSchema() -> String
PM_TimeSheetLineData.ToXMLFile(ByVal bstrFileName As String)
PM_TimeSheetLineData.ToXMLString() -> String
PM_TimeSheetLineDataCollection.Count : Long [R]
PM_TimeSheetLineDataCollection.Add() -> PM_TimeSheetLineData
PM_TimeSheetLineDataCollection.GetXMLSchema() -> String
PM_TimeSheetLineDataCollection.Item(ByVal vtIndex As Variant) -> PM_TimeSheetLineData
PM_TimeSheetLineDataCollection.Remove(ByVal vtIndex As Variant)
PM_TimeSheetLineDataCollection.ToXMLFile(ByVal bstrFileName As String)
PM_TimeSheetLineDataCollection.ToXMLString() -> String
PM_TimeSheetParams.AbsEntry : Long [R/W]
PM_TimeSheetParams.FromXMLFile(ByVal bstrFileName As String)
PM_TimeSheetParams.FromXMLString(ByVal bstrXML As String)
PM_TimeSheetParams.GetXMLSchema() -> String
PM_TimeSheetParams.ToXMLFile(ByVal bstrFileName As String)
PM_TimeSheetParams.ToXMLString() -> String
PM_WorkOrderData.DocEntry : Long [R/W]
PM_WorkOrderData.DocNumber : Long [R/W]
PM_WorkOrderData.LineId : Long [R]
PM_WorkOrderData.StageID : Long [R/W]
PM_WorkOrderData.UserFields : Fields [R]
PM_WorkOrderData.FromXMLFile(ByVal bstrFileName As String)
PM_WorkOrderData.FromXMLString(ByVal bstrXML As String)
PM_WorkOrderData.GetXMLSchema() -> String
PM_WorkOrderData.ToXMLFile(ByVal bstrFileName As String)
PM_WorkOrderData.ToXMLString() -> String
PM_WorkOrdersCollection.Count : Long [R]
PM_WorkOrdersCollection.Add() -> PM_WorkOrderData
PM_WorkOrdersCollection.GetXMLSchema() -> String
PM_WorkOrdersCollection.Item(ByVal vtIndex As Variant) -> PM_WorkOrderData
PM_WorkOrdersCollection.ToXMLFile(ByVal bstrFileName As String)
PM_WorkOrdersCollection.ToXMLString() -> String
PMC_ActivityCollection.Count : Long [R]
PMC_ActivityCollection.Add() -> PMC_ActivityData
PMC_ActivityCollection.GetXMLSchema() -> String
PMC_ActivityCollection.Item(ByVal vtIndex As Variant) -> PMC_ActivityData
PMC_ActivityCollection.ToXMLFile(ByVal bstrFileName As String)
PMC_ActivityCollection.ToXMLString() -> String
PMC_ActivityData.ActivityID : Long [R/W]
PMC_ActivityData.ActivityType : String [R/W]
PMC_ActivityData.IsAbsence : BoYesNoEnum [R/W]
PMC_ActivityData.IsChargeable : BoYesNoEnum [R/W]
PMC_ActivityData.LaborItem : String [R/W]
PMC_ActivityData.FromXMLFile(ByVal bstrFileName As String)
PMC_ActivityData.FromXMLString(ByVal bstrXML As String)
PMC_ActivityData.GetXMLSchema() -> String
PMC_ActivityData.ToXMLFile(ByVal bstrFileName As String)
PMC_ActivityData.ToXMLString() -> String
PMC_AreaCollection.Count : Long [R]
PMC_AreaCollection.Add() -> PMC_AreaData
PMC_AreaCollection.GetXMLSchema() -> String
PMC_AreaCollection.Item(ByVal vtIndex As Variant) -> PMC_AreaData
PMC_AreaCollection.ToXMLFile(ByVal bstrFileName As String)
PMC_AreaCollection.ToXMLString() -> String
PMC_AreaData.AreaID : Long [R/W]
PMC_AreaData.AreaName : String [R/W]
PMC_AreaData.FromXMLFile(ByVal bstrFileName As String)
PMC_AreaData.FromXMLString(ByVal bstrXML As String)
PMC_AreaData.GetXMLSchema() -> String
PMC_AreaData.ToXMLFile(ByVal bstrFileName As String)
PMC_AreaData.ToXMLString() -> String
PMC_PriorityCollection.Count : Long [R]
PMC_PriorityCollection.Add() -> PMC_PriorityData
PMC_PriorityCollection.GetXMLSchema() -> String
PMC_PriorityCollection.Item(ByVal vtIndex As Variant) -> PMC_PriorityData
PMC_PriorityCollection.ToXMLFile(ByVal bstrFileName As String)
PMC_PriorityCollection.ToXMLString() -> String
PMC_PriorityData.PriorityID : Long [R/W]
PMC_PriorityData.PriorityName : String [R/W]
PMC_PriorityData.FromXMLFile(ByVal bstrFileName As String)
PMC_PriorityData.FromXMLString(ByVal bstrXML As String)
PMC_PriorityData.GetXMLSchema() -> String
PMC_PriorityData.ToXMLFile(ByVal bstrFileName As String)
PMC_PriorityData.ToXMLString() -> String
PMC_StageTypeCollection.Count : Long [R]
PMC_StageTypeCollection.Add() -> PMC_StageTypeData
PMC_StageTypeCollection.GetXMLSchema() -> String
PMC_StageTypeCollection.Item(ByVal vtIndex As Variant) -> PMC_StageTypeData
PMC_StageTypeCollection.ToXMLFile(ByVal bstrFileName As String)
PMC_StageTypeCollection.ToXMLString() -> String
PMC_StageTypeData.StageDescription : String [R/W]
PMC_StageTypeData.StageID : Long [R/W]
PMC_StageTypeData.StageName : String [R/W]
PMC_StageTypeData.FromXMLFile(ByVal bstrFileName As String)
PMC_StageTypeData.FromXMLString(ByVal bstrXML As String)
PMC_StageTypeData.GetXMLSchema() -> String
PMC_StageTypeData.ToXMLFile(ByVal bstrFileName As String)
PMC_StageTypeData.ToXMLString() -> String
PMC_SubprojectTypeData.SubprojectTypeID : Long [R/W]
PMC_SubprojectTypeData.SubprojectTypeName : String [R/W]
PMC_SubprojectTypeData.FromXMLFile(ByVal bstrFileName As String)
PMC_SubprojectTypeData.FromXMLString(ByVal bstrXML As String)
PMC_SubprojectTypeData.GetXMLSchema() -> String
PMC_SubprojectTypeData.ToXMLFile(ByVal bstrFileName As String)
PMC_SubprojectTypeData.ToXMLString() -> String
PMC_SubprojectTypesCollection.Count : Long [R]
PMC_SubprojectTypesCollection.Add() -> PMC_SubprojectTypeData
PMC_SubprojectTypesCollection.GetXMLSchema() -> String
PMC_SubprojectTypesCollection.Item(ByVal vtIndex As Variant) -> PMC_SubprojectTypeData
PMC_SubprojectTypesCollection.ToXMLFile(ByVal bstrFileName As String)
PMC_SubprojectTypesCollection.ToXMLString() -> String
PMC_TaskCollection.Count : Long [R]
PMC_TaskCollection.Add() -> PMC_TaskData
PMC_TaskCollection.GetXMLSchema() -> String
PMC_TaskCollection.Item(ByVal vtIndex As Variant) -> PMC_TaskData
PMC_TaskCollection.ToXMLFile(ByVal bstrFileName As String)
PMC_TaskCollection.ToXMLString() -> String
PMC_TaskData.TaskID : Long [R/W]
PMC_TaskData.TaskName : String [R/W]
PMC_TaskData.FromXMLFile(ByVal bstrFileName As String)
PMC_TaskData.FromXMLString(ByVal bstrXML As String)
PMC_TaskData.GetXMLSchema() -> String
PMC_TaskData.ToXMLFile(ByVal bstrFileName As String)
PMC_TaskData.ToXMLString() -> String
PMS_ActivitiesCollection.Count : Long [R]
PMS_ActivitiesCollection.Add() -> PMS_ActivityData
PMS_ActivitiesCollection.GetXMLSchema() -> String
PMS_ActivitiesCollection.Item(ByVal vtIndex As Variant) -> PMS_ActivityData
PMS_ActivitiesCollection.ToXMLFile(ByVal bstrFileName As String)
PMS_ActivitiesCollection.ToXMLString() -> String
PMS_ActivityData.ActivityID : Long [R/W]
PMS_ActivityData.LineId : Long [R]
PMS_ActivityData.StageID : Long [R/W]
PMS_ActivityData.UserFields : Fields [R]
PMS_ActivityData.FromXMLFile(ByVal bstrFileName As String)
PMS_ActivityData.FromXMLString(ByVal bstrXML As String)
PMS_ActivityData.GetXMLSchema() -> String
PMS_ActivityData.ToXMLFile(ByVal bstrFileName As String)
PMS_ActivityData.ToXMLString() -> String
PMS_DocAttachement.AbsEntry : Long [R]
PMS_DocAttachement.AttachementDate : Date [R/W]
PMS_DocAttachement.FileExtension : String [R/W]
PMS_DocAttachement.FileName : String [R/W]
PMS_DocAttachement.LineId : Long [R]
PMS_DocAttachement.SourcePath : String [R/W]
PMS_DocAttachement.FromXMLFile(ByVal bstrFileName As String)
PMS_DocAttachement.FromXMLString(ByVal bstrXML As String)
PMS_DocAttachement.GetXMLSchema() -> String
PMS_DocAttachement.ToXMLFile(ByVal bstrFileName As String)
PMS_DocAttachement.ToXMLString() -> String
PMS_DocAttachements.Count : Long [R]
PMS_DocAttachements.Add() -> PMS_DocAttachement
PMS_DocAttachements.GetXMLSchema() -> String
PMS_DocAttachements.Item(ByVal vtIndex As Variant) -> PMS_DocAttachement
PMS_DocAttachements.ToXMLFile(ByVal bstrFileName As String)
PMS_DocAttachements.ToXMLString() -> String
PMS_DocumentData.AmountCategory : AmountCatTypeEnum [R]
PMS_DocumentData.Categorize : PMCategorizeTypeEnum [R/W]
PMS_DocumentData.DocDate : Date [R]
PMS_DocumentData.DocEntry : Long [R/W]
PMS_DocumentData.DocType : PMDocumentTypeEnum [R/W]
PMS_DocumentData.LineId : Long [R]
PMS_DocumentData.LineNumber : Long [R/W]
PMS_DocumentData.Operation : PMOperationTypeEnum [R/W]
PMS_DocumentData.StageID : Long [R/W]
PMS_DocumentData.Status : LineStatusTypeEnum [R]
PMS_DocumentData.Total : Double [R]
PMS_DocumentData.UserFields : Fields [R]
PMS_DocumentData.FromXMLFile(ByVal bstrFileName As String)
PMS_DocumentData.FromXMLString(ByVal bstrXML As String)
PMS_DocumentData.GetXMLSchema() -> String
PMS_DocumentData.ToXMLFile(ByVal bstrFileName As String)
PMS_DocumentData.ToXMLString() -> String
PMS_DocumentsCollection.Count : Long [R]
PMS_DocumentsCollection.Add() -> PMS_DocumentData
PMS_DocumentsCollection.GetXMLSchema() -> String
PMS_DocumentsCollection.Item(ByVal vtIndex As Variant) -> PMS_DocumentData
PMS_DocumentsCollection.ToXMLFile(ByVal bstrFileName As String)
PMS_DocumentsCollection.ToXMLString() -> String
PMS_OpenIssueData.Area : Long [R/W]
PMS_OpenIssueData.Closed : BoYesNoEnum [R/W]
PMS_OpenIssueData.Effort : Double [R/W]
PMS_OpenIssueData.EnteredBy : Long [R/W]
PMS_OpenIssueData.EnteredDate : Date [R/W]
PMS_OpenIssueData.LineId : Long [R]
PMS_OpenIssueData.Priority : Long [R/W]
PMS_OpenIssueData.Remarks : String [R/W]
PMS_OpenIssueData.Responsible : Long [R/W]
PMS_OpenIssueData.SolutionID : Long [R/W]
PMS_OpenIssueData.StageID : Long [R/W]
PMS_OpenIssueData.UserFields : Fields [R]
PMS_OpenIssueData.FromXMLFile(ByVal bstrFileName As String)
PMS_OpenIssueData.FromXMLString(ByVal bstrXML As String)
PMS_OpenIssueData.GetXMLSchema() -> String
PMS_OpenIssueData.ToXMLFile(ByVal bstrFileName As String)
PMS_OpenIssueData.ToXMLString() -> String
PMS_OpenIssuesCollection.Count : Long [R]
PMS_OpenIssuesCollection.Add() -> PMS_OpenIssueData
PMS_OpenIssuesCollection.GetXMLSchema() -> String
PMS_OpenIssuesCollection.Item(ByVal vtIndex As Variant) -> PMS_OpenIssueData
PMS_OpenIssuesCollection.ToXMLFile(ByVal bstrFileName As String)
PMS_OpenIssuesCollection.ToXMLString() -> String
PMS_StageAttachement.AbsEntry : Long [R]
PMS_StageAttachement.AttachementDate : Date [R/W]
PMS_StageAttachement.FileExtension : String [R/W]
PMS_StageAttachement.FileName : String [R/W]
PMS_StageAttachement.LineId : Long [R]
PMS_StageAttachement.SourcePath : String [R/W]
PMS_StageAttachement.FromXMLFile(ByVal bstrFileName As String)
PMS_StageAttachement.FromXMLString(ByVal bstrXML As String)
PMS_StageAttachement.GetXMLSchema() -> String
PMS_StageAttachement.ToXMLFile(ByVal bstrFileName As String)
PMS_StageAttachement.ToXMLString() -> String
PMS_StageAttachements.Count : Long [R]
PMS_StageAttachements.Add() -> PMS_StageAttachement
PMS_StageAttachements.GetXMLSchema() -> String
PMS_StageAttachements.Item(ByVal vtIndex As Variant) -> PMS_StageAttachement
PMS_StageAttachements.ToXMLFile(ByVal bstrFileName As String)
PMS_StageAttachements.ToXMLString() -> String
PMS_StageData.AttachmentEntry : Long [R/W]
PMS_StageData.CloseDate : Date [R/W]
PMS_StageData.DependsOnStage1 : Long [R/W]
PMS_StageData.DependsOnStage2 : Long [R/W]
PMS_StageData.DependsOnStage3 : Long [R/W]
PMS_StageData.DependsOnStage4 : Long [R/W]
PMS_StageData.DependsOnStageID1 : Long [R/W]
PMS_StageData.DependsOnStageID2 : Long [R/W]
PMS_StageData.DependsOnStageID3 : Long [R/W]
PMS_StageData.DependsOnStageID4 : Long [R/W]
PMS_StageData.Description : String [R/W]
PMS_StageData.ExpectedCosts : Double [R/W]
PMS_StageData.FinishedDate : Date [R/W]
PMS_StageData.InvoicedAmountPurchase : Double [R/W]
PMS_StageData.InvoicedAmountSales : Double [R/W]
PMS_StageData.IsFinished : BoYesNoEnum [R/W]
PMS_StageData.LineId : Long [R]
PMS_StageData.OpenAmountPurchase : Double [R/W]
PMS_StageData.OpenAmountSales : Double [R/W]
PMS_StageData.PercentualCompletness : Double [R/W]
PMS_StageData.StageDependency1Type : StageDepTypeEnum [R/W]
PMS_StageData.StageDependency2Type : StageDepTypeEnum [R/W]
PMS_StageData.StageDependency3Type : StageDepTypeEnum [R/W]
PMS_StageData.StageDependency4Type : StageDepTypeEnum [R/W]
PMS_StageData.StageID : Long [R/W]
PMS_StageData.StageOwner : Long [R/W]
PMS_StageData.StageType : Long [R/W]
PMS_StageData.StartDate : Date [R/W]
PMS_StageData.Task : Long [R/W]
PMS_StageData.UniqueID : String [R/W]
PMS_StageData.UserFields : Fields [R]
PMS_StageData.FromXMLFile(ByVal bstrFileName As String)
PMS_StageData.FromXMLString(ByVal bstrXML As String)
PMS_StageData.GetXMLSchema() -> String
PMS_StageData.ToXMLFile(ByVal bstrFileName As String)
PMS_StageData.ToXMLString() -> String
PMS_StagesCollection.Count : Long [R]
PMS_StagesCollection.Add() -> PMS_StageData
PMS_StagesCollection.GetXMLSchema() -> String
PMS_StagesCollection.Item(ByVal vtIndex As Variant) -> PMS_StageData
PMS_StagesCollection.ToXMLFile(ByVal bstrFileName As String)
PMS_StagesCollection.ToXMLString() -> String
PMS_SummaryData.AccumInvoicedAmountPurchase : Double [R]
PMS_SummaryData.AccumInvoicedAmountSales : Double [R]
PMS_SummaryData.AccumOpenAmountPurchase : Double [R]
PMS_SummaryData.AccumOpenAmountSales : Double [R]
PMS_SummaryData.AccumPotentialSubprojectAmount : Double [R]
PMS_SummaryData.AccumSubprojectBudget : Double [R]
PMS_SummaryData.AccumTotalPurchase : Double [R]
PMS_SummaryData.AccumTotalSales : Double [R]
PMS_SummaryData.AccumTotalVariancePurchase : Double [R]
PMS_SummaryData.AccumTotalVarianceSales : Double [R]
PMS_SummaryData.AccumVariancePerceptionPurchase : Double [R]
PMS_SummaryData.AccumVariancePerceptionSales : Double [R]
PMS_SummaryData.ActualAdditionalCost : Double [R]
PMS_SummaryData.ActualByProductCost : Double [R]
PMS_SummaryData.ActualClosingDate : Date [R]
PMS_SummaryData.ActualItemComponentCost : Double [R]
PMS_SummaryData.ActualProductCost : Double [R]
PMS_SummaryData.ActualResourceComponentCost : Double [R]
PMS_SummaryData.DueDate : Date [R]
PMS_SummaryData.LineId : Long [R]
PMS_SummaryData.Overdue : Long [R]
PMS_SummaryData.PotentialSubprojectAmount : Double [R/W]
PMS_SummaryData.SubprojectBudget : Double [R]
PMS_SummaryData.SumInvoicedAmountPurchase : Double [R]
PMS_SummaryData.SumInvoicedAmountSales : Double [R]
PMS_SummaryData.SumOpenAmountPurchase : Double [R]
PMS_SummaryData.SumOpenAmountSales : Double [R]
PMS_SummaryData.TotalAmountPurchase : Double [R]
PMS_SummaryData.TotalAmountSales : Double [R]
PMS_SummaryData.TotalVariance : Double [R]
PMS_SummaryData.TotalVariancePurchase : Double [R]
PMS_SummaryData.TotalVarianceSales : Double [R]
PMS_SummaryData.VariancePerceptionPurchase : Double [R]
PMS_SummaryData.VariancePerceptionSales : Double [R]
PMS_SummaryData.FromXMLFile(ByVal bstrFileName As String)
PMS_SummaryData.FromXMLString(ByVal bstrXML As String)
PMS_SummaryData.GetXMLSchema() -> String
PMS_SummaryData.ToXMLFile(ByVal bstrFileName As String)
PMS_SummaryData.ToXMLString() -> String
PMS_WorkOrderData.DocEntry : Long [R/W]
PMS_WorkOrderData.DocNumber : Long [R/W]
PMS_WorkOrderData.LineId : Long [R]
PMS_WorkOrderData.StageID : Long [R/W]
PMS_WorkOrderData.UserFields : Fields [R]
PMS_WorkOrderData.FromXMLFile(ByVal bstrFileName As String)
PMS_WorkOrderData.FromXMLString(ByVal bstrXML As String)
PMS_WorkOrderData.GetXMLSchema() -> String
PMS_WorkOrderData.ToXMLFile(ByVal bstrFileName As String)
PMS_WorkOrderData.ToXMLString() -> String
PMS_WorkOrdersCollection.Count : Long [R]
PMS_WorkOrdersCollection.Add() -> PMS_WorkOrderData
PMS_WorkOrdersCollection.GetXMLSchema() -> String
PMS_WorkOrdersCollection.Item(ByVal vtIndex As Variant) -> PMS_WorkOrderData
PMS_WorkOrdersCollection.ToXMLFile(ByVal bstrFileName As String)
PMS_WorkOrdersCollection.ToXMLString() -> String
POSDailySummary.AbsEntry : Long [R]
POSDailySummary.COFINSTotal : Double [R/W]
POSDailySummary.CounterPosition : Long [R/W]
POSDailySummary.Date : Date [R/W]
POSDailySummary.EquipmentNo : String [R/W]
POSDailySummary.GrossSales : Double [R/W]
POSDailySummary.OperationCounter : Long [R/W]
POSDailySummary.PISTotal : Double [R/W]
POSDailySummary.POSTotalizerCollection : POSTotalizerCollection [R]
POSDailySummary.ResetCounterPosition : Long [R/W]
POSDailySummary.Total : Double [R/W]
POSDailySummary.FromXMLFile(ByVal bstrFileName As String)
POSDailySummary.FromXMLString(ByVal bstrXML As String)
POSDailySummary.GetXMLSchema() -> String
POSDailySummary.ToXMLFile(ByVal bstrFileName As String)
POSDailySummary.ToXMLString() -> String
POSDailySummaryParams.AbsEntry : Long [R/W]
POSDailySummaryParams.FromXMLFile(ByVal bstrFileName As String)
POSDailySummaryParams.FromXMLString(ByVal bstrXML As String)
POSDailySummaryParams.GetXMLSchema() -> String
POSDailySummaryParams.ToXMLFile(ByVal bstrFileName As String)
POSDailySummaryParams.ToXMLString() -> String
POSDailySummaryService.Add(ByVal pIPOSDailySummary As POSDailySummary) -> POSDailySummaryParams
POSDailySummaryService.Delete(ByVal pIPOSDailySummaryParams As POSDailySummaryParams)
POSDailySummaryService.Get(ByVal pIPOSDailySummaryParams As POSDailySummaryParams) -> POSDailySummary
POSDailySummaryService.GetDataInterface(ByVal enumMSDI As POSDailySummaryServiceDataInterfaces) -> Object
POSDailySummaryService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
POSDailySummaryService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
POSDailySummaryService.Update(ByVal pIPOSDailySummary As POSDailySummary)
PostingTemplates.AutomaticVAT : BoYesNoEnum [R/W]
PostingTemplates.Code : String [R/W]
PostingTemplates.DeferredTax : BoYesNoEnum [R/W]
PostingTemplates.Description : String [R/W]
PostingTemplates.ManageWTax : BoYesNoEnum [R/W]
PostingTemplates.PostingTemplatesLineCollection : PostingTemplatesLineCollection [R]
PostingTemplates.StampTax : BoYesNoEnum [R/W]
PostingTemplates.FromXMLFile(ByVal bstrFileName As String)
PostingTemplates.FromXMLString(ByVal bstrXML As String)
PostingTemplates.GetXMLSchema() -> String
PostingTemplates.ToXMLFile(ByVal bstrFileName As String)
PostingTemplates.ToXMLString() -> String
PostingTemplatesLine.AccountCode : String [R/W]
PostingTemplatesLine.AccountName : String [R/W]
PostingTemplatesLine.ControlAccount : String [R/W]
PostingTemplatesLine.CostElementCode : String [R]
PostingTemplatesLine.CostingCode1 : String [R/W]
PostingTemplatesLine.CostingCode2 : String [R/W]
PostingTemplatesLine.CostingCode3 : String [R/W]
PostingTemplatesLine.CostingCode4 : String [R/W]
PostingTemplatesLine.CostingCode5 : String [R/W]
PostingTemplatesLine.Credit : Double [R/W]
PostingTemplatesLine.Debit : Double [R/W]
PostingTemplatesLine.DistributionRule : String [R/W]
PostingTemplatesLine.LineNumber : Long [R]
PostingTemplatesLine.ProjectCode : String [R/W]
PostingTemplatesLine.TaxCode : String [R/W]
PostingTemplatesLine.TaxGroup : String [R/W]
PostingTemplatesLine.TaxPostingAccount : BoTaxPostingAccountTypeEnum [R/W]
PostingTemplatesLine.TrtCode : String [R]
PostingTemplatesLine.VatLine : BoYesNoEnum [R/W]
PostingTemplatesLine.WTaxLiable : BoYesNoEnum [R/W]
PostingTemplatesLine.WTaxLine : BoYesNoEnum [R/W]
PostingTemplatesLine.FromXMLFile(ByVal bstrFileName As String)
PostingTemplatesLine.FromXMLString(ByVal bstrXML As String)
PostingTemplatesLine.GetXMLSchema() -> String
PostingTemplatesLine.ToXMLFile(ByVal bstrFileName As String)
PostingTemplatesLine.ToXMLString() -> String
PostingTemplatesLineCollection.Count : Long [R]
PostingTemplatesLineCollection.Add() -> PostingTemplatesLine
PostingTemplatesLineCollection.GetXMLSchema() -> String
PostingTemplatesLineCollection.Item(ByVal vtIndex As Variant) -> PostingTemplatesLine
PostingTemplatesLineCollection.Remove(ByVal vtIndex As Variant)
PostingTemplatesLineCollection.ToXMLFile(ByVal bstrFileName As String)
PostingTemplatesLineCollection.ToXMLString() -> String
PostingTemplatesParams.Code : String [R/W]
PostingTemplatesParams.Description : String [R]
PostingTemplatesParams.FromXMLFile(ByVal bstrFileName As String)
PostingTemplatesParams.FromXMLString(ByVal bstrXML As String)
PostingTemplatesParams.GetXMLSchema() -> String
PostingTemplatesParams.ToXMLFile(ByVal bstrFileName As String)
PostingTemplatesParams.ToXMLString() -> String
PostingTemplatesParamsCollection.Count : Long [R]
PostingTemplatesParamsCollection.Add() -> PostingTemplatesParams
PostingTemplatesParamsCollection.GetXMLSchema() -> String
PostingTemplatesParamsCollection.Item(ByVal vtIndex As Variant) -> PostingTemplatesParams
PostingTemplatesParamsCollection.ToXMLFile(ByVal bstrFileName As String)
PostingTemplatesParamsCollection.ToXMLString() -> String
PostingTemplatesService.Add(ByVal pIPostingTemplates As PostingTemplates) -> PostingTemplatesParams
PostingTemplatesService.Delete(ByVal pIPostingTemplatesParams As PostingTemplatesParams)
PostingTemplatesService.Get(ByVal pIPostingTemplatesParams As PostingTemplatesParams) -> PostingTemplates
PostingTemplatesService.GetDataInterface(ByVal enumMSDI As PostingTemplatesServiceDataInterfaces) -> Object
PostingTemplatesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
PostingTemplatesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
PostingTemplatesService.GetList() -> PostingTemplatesParamsCollection
PostingTemplatesService.Update(ByVal pIPostingTemplates As PostingTemplates)
POSTotalizer.Code : String [R/W]
POSTotalizer.Description : String [R/W]
POSTotalizer.LineNum : Long [R]
POSTotalizer.Number : Long [R/W]
POSTotalizer.Total : Double [R/W]
POSTotalizer.FromXMLFile(ByVal bstrFileName As String)
POSTotalizer.FromXMLString(ByVal bstrXML As String)
POSTotalizer.GetXMLSchema() -> String
POSTotalizer.ToXMLFile(ByVal bstrFileName As String)
POSTotalizer.ToXMLString() -> String
POSTotalizerCollection.Count : Long [R]
POSTotalizerCollection.Add() -> POSTotalizer
POSTotalizerCollection.GetXMLSchema() -> String
POSTotalizerCollection.Item(ByVal vtIndex As Variant) -> POSTotalizer
POSTotalizerCollection.Remove(ByVal vtIndex As Variant)
POSTotalizerCollection.ToXMLFile(ByVal bstrFileName As String)
POSTotalizerCollection.ToXMLString() -> String
PredefinedText.Numerator : Long [R]
PredefinedText.Text : String [R/W]
PredefinedText.TextCode : String [R/W]
PredefinedText.FromXMLFile(ByVal bstrFileName As String)
PredefinedText.FromXMLString(ByVal bstrXML As String)
PredefinedText.GetXMLSchema() -> String
PredefinedText.ToXMLFile(ByVal bstrFileName As String)
PredefinedText.ToXMLString() -> String
PredefinedTextParams.Numerator : Long [R/W]
PredefinedTextParams.TextCode : String [R]
PredefinedTextParams.FromXMLFile(ByVal bstrFileName As String)
PredefinedTextParams.FromXMLString(ByVal bstrXML As String)
PredefinedTextParams.GetXMLSchema() -> String
PredefinedTextParams.ToXMLFile(ByVal bstrFileName As String)
PredefinedTextParams.ToXMLString() -> String
PredefinedTextsParams.Count : Long [R]
PredefinedTextsParams.Add() -> PredefinedTextParams
PredefinedTextsParams.GetXMLSchema() -> String
PredefinedTextsParams.Item(ByVal vtIndex As Variant) -> PredefinedTextParams
PredefinedTextsParams.ToXMLFile(ByVal bstrFileName As String)
PredefinedTextsParams.ToXMLString() -> String
PredefinedTextsService.AddPredefinedText(ByVal pIPredefinedText As PredefinedText) -> PredefinedTextParams
PredefinedTextsService.DeletePredefinedText(ByVal pIPredefinedTextParams As PredefinedTextParams)
PredefinedTextsService.GetDataInterface(ByVal enumMSDI As PredefinedTextsServiceDataInterfaces) -> Object
PredefinedTextsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
PredefinedTextsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
PredefinedTextsService.GetPredefinedText(ByVal pIPredefinedTextParams As PredefinedTextParams) -> PredefinedText
PredefinedTextsService.GetPredefinedTextList() -> PredefinedTextsParams
PredefinedTextsService.UpdatePredefinedText(ByVal pIPredefinedText As PredefinedText)
PriceLists.Active : BoYesNoEnum [R/W]
PriceLists.BasePriceList : Long [R/W]
PriceLists.Browser : DataBrowser [R]
PriceLists.DefaultAdditionalCurrency1 : String [R/W]
PriceLists.DefaultAdditionalCurrency2 : String [R/W]
PriceLists.DefaultPrimeCurrency : String [R/W]
PriceLists.Factor : Double [R/W]
PriceLists.FixedAmount : Double [R/W]
PriceLists.GroupNum : BoPriceListGroupNum [R/W]
PriceLists.IsGrossPrice : BoYesNoEnum [R/W]
PriceLists.PriceListName : String [R/W]
PriceLists.PriceListNo : Long [R]
PriceLists.RoundingFormatDecimalPart : String [R/W]
PriceLists.RoundingFormatIntegerPart : String [R/W]
PriceLists.RoundingMethod : BoRoundingMethod [R/W]
PriceLists.RoundingRule : BoRoundingRule [R/W]
PriceLists.UserFields : UserFields [R]
PriceLists.ValidFrom : Date [R/W]
PriceLists.ValidTo : Date [R/W]
PriceLists.Add() -> Long
PriceLists.GetAsXML() -> String
PriceLists.GetByKey(ByVal QueueID As String) -> Boolean
PriceLists.Remove() -> Long
PriceLists.SaveToFile(ByVal FileName As String)
PriceLists.SaveXML(ByRef FileName As String)
PriceLists.Update() -> Long
ProductionOrders.AbsoluteEntry : Long [R]
ProductionOrders.AttachmentEntry : Long [R/W]
ProductionOrders.Browser : DataBrowser [R]
ProductionOrders.ClosingDate : Date [R/W]
ProductionOrders.CompletedQuantity : Double [R]
ProductionOrders.CreationDate : Date [R]
ProductionOrders.CustomerCode : String [R/W]
ProductionOrders.DistributionRule : String [R/W]
ProductionOrders.DistributionRule2 : String [R/W]
ProductionOrders.DistributionRule3 : String [R/W]
ProductionOrders.DistributionRule4 : String [R/W]
ProductionOrders.DistributionRule5 : String [R/W]
ProductionOrders.DocumentNumber : Long [R]
ProductionOrders.DocumentReferences : ProductionOrders_DocumentReferences [R]
ProductionOrders.DueDate : Date [R/W]
ProductionOrders.InventoryUOM : String [R]
ProductionOrders.ItemNo : String [R/W]
ProductionOrders.JournalRemarks : String [R/W]
ProductionOrders.Lines : ProductionOrders_Lines [R]
ProductionOrders.PlannedQuantity : Double [R/W]
ProductionOrders.PostingDate : Date [R/W]
ProductionOrders.Printed : BoYesNoEnum [R]
ProductionOrders.Priority : Long [R/W]
ProductionOrders.ProductDescription : String [R/W]
ProductionOrders.ProductionOrderOrigin : BoProductionOrderOriginEnum [R/W]
ProductionOrders.ProductionOrderOriginEntry : Long [R/W]
ProductionOrders.ProductionOrderOriginNumber : Long [R]
ProductionOrders.ProductionOrderStatus : BoProductionOrderStatusEnum [R/W]
ProductionOrders.ProductionOrderType : BoProductionOrderTypeEnum [R/W]
ProductionOrders.Project : String [R/W]
ProductionOrders.RejectedQuantity : Double [R]
ProductionOrders.ReleaseDate : Date [R]
ProductionOrders.Remarks : String [R/W]
ProductionOrders.RoutingDateCalculation : ResourceAllocationEnum [R/W]
ProductionOrders.SalesOrderLines : ProductionOrders_SalesOrderLines [R]
ProductionOrders.SAPPassport : String [R]
ProductionOrders.Series : Long [R/W]
ProductionOrders.Stages : ProductionOrders_Stages [R]
ProductionOrders.StartDate : Date [R/W]
ProductionOrders.TransactionNumber : Long [R]
ProductionOrders.UoMEntry : Long [R]
ProductionOrders.UpdateAllocation : BoUpdateAllocationEnum [R/W]
ProductionOrders.UserFields : UserFields [R]
ProductionOrders.UserSignature : Long [R]
ProductionOrders.Warehouse : String [R/W]
ProductionOrders.Add() -> Long
ProductionOrders.Cancel() -> Long
ProductionOrders.GetAsXML() -> String
ProductionOrders.GetByKey(ByVal lAbsEntry As Long) -> Boolean
ProductionOrders.SaveToFile(ByVal bstrFileName As String)
ProductionOrders.SaveXML(ByRef pbstrFileName As String)
ProductionOrders.Update() -> Long
ProductionOrders_DocumentReferences.Count : Long [R]
ProductionOrders_DocumentReferences.DocEntry : Long [R]
ProductionOrders_DocumentReferences.ExternalReferencedDocNumber : String [R/W]
ProductionOrders_DocumentReferences.IssueDate : Date [R/W]
ProductionOrders_DocumentReferences.LineNumber : Long [R]
ProductionOrders_DocumentReferences.ReferencedDocEntry : Long [R/W]
ProductionOrders_DocumentReferences.ReferencedDocNumber : Long [R]
ProductionOrders_DocumentReferences.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
ProductionOrders_DocumentReferences.Remark : String [R/W]
ProductionOrders_DocumentReferences.Add()
ProductionOrders_DocumentReferences.Delete()
ProductionOrders_DocumentReferences.SetCurrentLine(ByVal LineNum As Long)
ProductionOrders_Lines.AdditionalQuantity : Double [R/W]
ProductionOrders_Lines.BaseQuantity : Double [R/W]
ProductionOrders_Lines.BatchNumbers : BatchNumbers [R]
ProductionOrders_Lines.Count : Long [R]
ProductionOrders_Lines.DistributionRule : String [R/W]
ProductionOrders_Lines.DistributionRule2 : String [R/W]
ProductionOrders_Lines.DistributionRule3 : String [R/W]
ProductionOrders_Lines.DistributionRule4 : String [R/W]
ProductionOrders_Lines.DistributionRule5 : String [R/W]
ProductionOrders_Lines.DocumentAbsoluteEntry : Long [R]
ProductionOrders_Lines.EndDate : Date [R/W]
ProductionOrders_Lines.IssuedQuantity : Double [R]
ProductionOrders_Lines.ItemName : String [R/W]
ProductionOrders_Lines.ItemNo : String [R/W]
ProductionOrders_Lines.ItemType : ProductionItemType [R/W]
ProductionOrders_Lines.LineNumber : Long [R]
ProductionOrders_Lines.LineText : String [R/W]
ProductionOrders_Lines.LocationCode : Long [R/W]
ProductionOrders_Lines.PlannedQuantity : Double [R/W]
ProductionOrders_Lines.ProductionOrderIssueType : BoIssueMethod [R/W]
ProductionOrders_Lines.Project : String [R/W]
ProductionOrders_Lines.RequiredDays : Double [R]
ProductionOrders_Lines.ResourceAllocation : ResourceAllocationEnum [R/W]
ProductionOrders_Lines.SerialNumbers : SerialNumbers [R]
ProductionOrders_Lines.StageID : Long [R/W]
ProductionOrders_Lines.StartDate : Date [R/W]
ProductionOrders_Lines.UoMCode : String [R]
ProductionOrders_Lines.UoMEntry : Long [R]
ProductionOrders_Lines.UserFields : UserFields [R]
ProductionOrders_Lines.VisualOrder : Long [R]
ProductionOrders_Lines.Warehouse : String [R/W]
ProductionOrders_Lines.WipAccount : String [R/W]
ProductionOrders_Lines.Add()
ProductionOrders_Lines.Delete()
ProductionOrders_Lines.SetCurrentLine(ByVal LineNum As Long)
ProductionOrders_SalesOrderLines.BaseAbsEntry : Long [R]
ProductionOrders_SalesOrderLines.BaseLine : Long [R]
ProductionOrders_SalesOrderLines.BaseNumber : Long [R]
ProductionOrders_SalesOrderLines.Count : Long [R]
ProductionOrders_SalesOrderLines.DocEntry : Long [R]
ProductionOrders_SalesOrderLines.SetCurrentLine(ByVal LineNum As Long)
ProductionOrders_Stages.CalculationProportion : Double [R/W]
ProductionOrders_Stages.Count : Long [R]
ProductionOrders_Stages.DocEntry : Long [R]
ProductionOrders_Stages.EndDate : Date [R/W]
ProductionOrders_Stages.Name : String [R/W]
ProductionOrders_Stages.RequiredDays : Double [R]
ProductionOrders_Stages.SequenceNumber : Long [R/W]
ProductionOrders_Stages.StageEntry : Long [R/W]
ProductionOrders_Stages.StageID : Long [R]
ProductionOrders_Stages.StartDate : Date [R/W]
ProductionOrders_Stages.WaitingDays : Double [R/W]
ProductionOrders_Stages.Add()
ProductionOrders_Stages.Delete()
ProductionOrders_Stages.SetCurrentLine(ByVal LineNum As Long)
ProductTrees.Browser : DataBrowser [R]
ProductTrees.DistributionRule : String [R/W]
ProductTrees.DistributionRule2 : String [R/W]
ProductTrees.DistributionRule3 : String [R/W]
ProductTrees.DistributionRule4 : String [R/W]
ProductTrees.DistributionRule5 : String [R/W]
ProductTrees.HideBOMComponentsInPrintout : BoYesNoEnum [R/W]
ProductTrees.Items : ProductTrees_Lines [R]
ProductTrees.PlanAvgProdSize : Double [R/W]
ProductTrees.PriceList : Long [R/W]
ProductTrees.ProductDescription : String [R/W]
ProductTrees.Project : String [R/W]
ProductTrees.Quantity : Double [R/W]
ProductTrees.Stages : ProductTrees_Stages [R]
ProductTrees.TreeCode : String [R/W]
ProductTrees.TreeType : BoItemTreeTypes [R/W]
ProductTrees.UserFields : UserFields [R]
ProductTrees.Warehouse : String [R/W]
ProductTrees.Add() -> Long
ProductTrees.Cancel() -> Long
ProductTrees.Close() -> Long
ProductTrees.GetAsXML() -> String
ProductTrees.GetByKey(ByVal Key As String) -> Boolean
ProductTrees.Remove() -> Long
ProductTrees.SaveToFile(ByVal FileName As String)
ProductTrees.SaveXML(ByRef FileName As String)
ProductTrees.Update() -> Long
ProductTrees.UpdateFromXML(ByVal FileName As String) -> Long
ProductTrees_Lines.AdditionalQuantity : Double [R/W]
ProductTrees_Lines.ChildNum : Long [R]
ProductTrees_Lines.Comment : String [R/W]
ProductTrees_Lines.Count : Long [R]
ProductTrees_Lines.Currency : String [R/W]
ProductTrees_Lines.DistributionRule : String [R/W]
ProductTrees_Lines.DistributionRule2 : String [R/W]
ProductTrees_Lines.DistributionRule3 : String [R/W]
ProductTrees_Lines.DistributionRule4 : String [R/W]
ProductTrees_Lines.DistributionRule5 : String [R/W]
ProductTrees_Lines.InventoryUOM : String [R]
ProductTrees_Lines.IssueMethod : BoIssueMethod [R/W]
ProductTrees_Lines.ItemCode : String [R/W]
ProductTrees_Lines.ItemName : String [R/W]
ProductTrees_Lines.ItemType : ProductionItemType [R/W]
ProductTrees_Lines.LineText : String [R/W]
ProductTrees_Lines.ParentItem : String [R/W]
ProductTrees_Lines.Price : Double [R/W]
ProductTrees_Lines.PriceList : Long [R/W]
ProductTrees_Lines.Project : String [R/W]
ProductTrees_Lines.Quantity : Double [R/W]
ProductTrees_Lines.StageID : Long [R/W]
ProductTrees_Lines.UserFields : UserFields [R]
ProductTrees_Lines.VisualOrder : Long [R]
ProductTrees_Lines.Warehouse : String [R/W]
ProductTrees_Lines.WipAccount : String [R/W]
ProductTrees_Lines.Add()
ProductTrees_Lines.Delete()
ProductTrees_Lines.SetCurrentLine(ByVal LineNum As Long)
ProductTrees_Stages.Count : Long [R]
ProductTrees_Stages.Father : String [R]
ProductTrees_Stages.Name : String [R/W]
ProductTrees_Stages.SequenceNumber : Long [R/W]
ProductTrees_Stages.StageEntry : Long [R/W]
ProductTrees_Stages.StageID : Long [R]
ProductTrees_Stages.WaitingDays : Double [R/W]
ProductTrees_Stages.Add()
ProductTrees_Stages.Delete()
ProductTrees_Stages.SetCurrentLine(ByVal LineNum As Long)
ProfitCenter.Active : BoYesNoEnum [R/W]
ProfitCenter.CenterCode : String [R/W]
ProfitCenter.CenterName : String [R/W]
ProfitCenter.CenterOwner : Long [R/W]
ProfitCenter.CostCenterType : String [R/W]
ProfitCenter.Effectivefrom : Date [R/W]
ProfitCenter.EffectiveTo : Date [R/W]
ProfitCenter.GroupCode : String [R/W]
ProfitCenter.InWhichDimension : Long [R/W]
ProfitCenter.UserFields : Fields [R]
ProfitCenter.FromXMLFile(ByVal bstrFileName As String)
ProfitCenter.FromXMLString(ByVal bstrXML As String)
ProfitCenter.GetXMLSchema() -> String
ProfitCenter.ToXMLFile(ByVal bstrFileName As String)
ProfitCenter.ToXMLString() -> String
ProfitCenterParams.CenterCode : String [R/W]
ProfitCenterParams.CenterName : String [R]
ProfitCenterParams.FromXMLFile(ByVal bstrFileName As String)
ProfitCenterParams.FromXMLString(ByVal bstrXML As String)
ProfitCenterParams.GetXMLSchema() -> String
ProfitCenterParams.ToXMLFile(ByVal bstrFileName As String)
ProfitCenterParams.ToXMLString() -> String
ProfitCentersParams.Count : Long [R]
ProfitCentersParams.Add() -> ProfitCenterParams
ProfitCentersParams.GetXMLSchema() -> String
ProfitCentersParams.Item(ByVal vtIndex As Variant) -> ProfitCenterParams
ProfitCentersParams.ToXMLFile(ByVal bstrFileName As String)
ProfitCentersParams.ToXMLString() -> String
ProfitCentersService.AddProfitCenter(ByVal pIProfitCenter As ProfitCenter) -> ProfitCenterParams
ProfitCentersService.DeleteProfitCenter(ByVal pIProfitCenterParams As ProfitCenterParams)
ProfitCentersService.GetDataInterface(ByVal enumMSDI As ProfitCentersServiceDataInterfaces) -> Object
ProfitCentersService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ProfitCentersService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ProfitCentersService.GetProfitCenter(ByVal pIProfitCenterParams As ProfitCenterParams) -> ProfitCenter
ProfitCentersService.GetProfitCenterList() -> ProfitCentersParams
ProfitCentersService.UpdateProfitCenter(ByVal pIProfitCenter As ProfitCenter)
Project.Active : BoYesNoEnum [R/W]
Project.Code : String [R/W]
Project.Name : String [R/W]
Project.UserFields : Fields [R]
Project.ValidFrom : Date [R/W]
Project.ValidTo : Date [R/W]
Project.FromXMLFile(ByVal bstrFileName As String)
Project.FromXMLString(ByVal bstrXML As String)
Project.GetXMLSchema() -> String
Project.ToXMLFile(ByVal bstrFileName As String)
Project.ToXMLString() -> String
ProjectManagementConfigurationService.AddActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)
ProjectManagementConfigurationService.AddAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)
ProjectManagementConfigurationService.AddPriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)
ProjectManagementConfigurationService.AddStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)
ProjectManagementConfigurationService.AddSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)
ProjectManagementConfigurationService.AddTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)
ProjectManagementConfigurationService.DeleteActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)
ProjectManagementConfigurationService.DeleteAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)
ProjectManagementConfigurationService.DeletePriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)
ProjectManagementConfigurationService.DeleteStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)
ProjectManagementConfigurationService.DeleteSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)
ProjectManagementConfigurationService.DeleteTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)
ProjectManagementConfigurationService.GetActivities() -> PMC_ActivityCollection
ProjectManagementConfigurationService.GetAreas() -> PMC_AreaCollection
ProjectManagementConfigurationService.GetDataInterface(ByVal enumMSDI As ProjectManagementConfigurationServiceDataInterfaces) -> Object
ProjectManagementConfigurationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ProjectManagementConfigurationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ProjectManagementConfigurationService.GetPriorities() -> PMC_PriorityCollection
ProjectManagementConfigurationService.GetStageTypes() -> PMC_StageTypeCollection
ProjectManagementConfigurationService.GetSubprojectTypes() -> PMC_SubprojectTypesCollection
ProjectManagementConfigurationService.GetTasks() -> PMC_TaskCollection
ProjectManagementConfigurationService.UpdateActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)
ProjectManagementConfigurationService.UpdateAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)
ProjectManagementConfigurationService.UpdatePriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)
ProjectManagementConfigurationService.UpdateStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)
ProjectManagementConfigurationService.UpdateSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)
ProjectManagementConfigurationService.UpdateTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)
ProjectManagementService.AddProject(ByVal pIPM_ProjectDocumentData As PM_ProjectDocumentData) -> PM_ProjectDocumentParams
ProjectManagementService.AddSubproject(ByVal pIPM_SubprojectDocumentData As PM_SubprojectDocumentData) -> PM_SubprojectDocumentParams
ProjectManagementService.CancelProject(ByVal pIPM_ProjectDocumentParams As PM_ProjectDocumentParams)
ProjectManagementService.DeleteSubproject(ByVal pIPM_SubprojectDocumentParams As PM_SubprojectDocumentParams)
ProjectManagementService.GetDataInterface(ByVal enumMSDI As ProjectManagementServiceDataInterfaces) -> Object
ProjectManagementService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ProjectManagementService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ProjectManagementService.GetProject(ByVal pIPM_ProjectDocumentParams As PM_ProjectDocumentParams) -> PM_ProjectDocumentData
ProjectManagementService.GetSubproject(ByVal pIPM_SubprojectDocumentParams As PM_SubprojectDocumentParams) -> PM_SubprojectDocumentData
ProjectManagementService.GetSubprojectsList(ByVal pIPM_SubprojectParams As PM_SubprojectParams) -> PM_SubprojectDocumentsCollection
ProjectManagementService.UpdateProject(ByVal pIPM_ProjectDocumentData As PM_ProjectDocumentData)
ProjectManagementService.UpdateSubproject(ByVal pIPM_SubprojectDocumentData As PM_SubprojectDocumentData)
ProjectManagementTimeSheetService.AddTimeSheet(ByVal pIPM_TimeSheetData As PM_TimeSheetData) -> PM_TimeSheetParams
ProjectManagementTimeSheetService.DeleteTimeSheet(ByVal pIPM_TimeSheetParams As PM_TimeSheetParams)
ProjectManagementTimeSheetService.GetDataInterface(ByVal enumMSDI As ProjectManagementTimeSheetServiceDataInterfaces) -> Object
ProjectManagementTimeSheetService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ProjectManagementTimeSheetService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ProjectManagementTimeSheetService.GetTimeSheet(ByVal pIPM_TimeSheetParams As PM_TimeSheetParams) -> PM_TimeSheetData
ProjectManagementTimeSheetService.UpdateTimeSheet(ByVal pIPM_TimeSheetData As PM_TimeSheetData)
ProjectParams.Code : String [R/W]
ProjectParams.Name : String [R]
ProjectParams.FromXMLFile(ByVal bstrFileName As String)
ProjectParams.FromXMLString(ByVal bstrXML As String)
ProjectParams.GetXMLSchema() -> String
ProjectParams.ToXMLFile(ByVal bstrFileName As String)
ProjectParams.ToXMLString() -> String
ProjectsParams.Count : Long [R]
ProjectsParams.Add() -> ProjectParams
ProjectsParams.GetXMLSchema() -> String
ProjectsParams.Item(ByVal vtIndex As Variant) -> ProjectParams
ProjectsParams.ToXMLFile(ByVal bstrFileName As String)
ProjectsParams.ToXMLString() -> String
ProjectsService.AddProject(ByVal pIProject As Project) -> ProjectParams
ProjectsService.DeleteProject(ByVal pIProjectParams As ProjectParams)
ProjectsService.GetDataInterface(ByVal enumMSDI As ProjectsServiceDataInterfaces) -> Object
ProjectsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ProjectsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ProjectsService.GetProject(ByVal pIProjectParams As ProjectParams) -> Project
ProjectsService.GetProjectList() -> ProjectsParams
ProjectsService.UpdateProject(ByVal pIProject As Project)
QRCodeCollection.Count : Long [R]
QRCodeCollection.Add() -> QRCodeData
QRCodeCollection.GetXMLSchema() -> String
QRCodeCollection.Item(ByVal vtIndex As Variant) -> QRCodeData
QRCodeCollection.ToXMLFile(ByVal bstrFileName As String)
QRCodeCollection.ToXMLString() -> String
QRCodeData.FieldName : String [R/W]
QRCodeData.ObjectAbsEntry : String [R/W]
QRCodeData.ObjectType : Long [R/W]
QRCodeData.QRCodeText : String [R/W]
QRCodeData.FromXMLFile(ByVal bstrFileName As String)
QRCodeData.FromXMLString(ByVal bstrXML As String)
QRCodeData.GetXMLSchema() -> String
QRCodeData.ToXMLFile(ByVal bstrFileName As String)
QRCodeData.ToXMLString() -> String
QRCodeService.AddOrUpdateQRCode(ByVal pIQRCodeData As QRCodeData)
QRCodeService.GetDataInterface(ByVal enumMSDI As QRCodeServiceDataInterfaces) -> Object
QRCodeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
QRCodeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
QueryAuthGroup.AuthGroupCode : String [R/W]
QueryAuthGroup.AuthGroupDes : String [R/W]
QueryAuthGroup.AuthGroupId : Long [R]
QueryAuthGroup.CategoryGroupCollection : CategoryGroupCollection [R]
QueryAuthGroup.FromXMLFile(ByVal bstrFileName As String)
QueryAuthGroup.FromXMLString(ByVal bstrXML As String)
QueryAuthGroup.GetXMLSchema() -> String
QueryAuthGroup.ToXMLFile(ByVal bstrFileName As String)
QueryAuthGroup.ToXMLString() -> String
QueryAuthGroupCollection.Count : Long [R]
QueryAuthGroupCollection.Add() -> QueryAuthGroup
QueryAuthGroupCollection.GetXMLSchema() -> String
QueryAuthGroupCollection.Item(ByVal vtIndex As Variant) -> QueryAuthGroup
QueryAuthGroupCollection.ToXMLFile(ByVal bstrFileName As String)
QueryAuthGroupCollection.ToXMLString() -> String
QueryAuthGroupParams.AuthGroupCode : String [R/W]
QueryAuthGroupParams.AuthGroupId : Long [R/W]
QueryAuthGroupParams.FromXMLFile(ByVal bstrFileName As String)
QueryAuthGroupParams.FromXMLString(ByVal bstrXML As String)
QueryAuthGroupParams.GetXMLSchema() -> String
QueryAuthGroupParams.ToXMLFile(ByVal bstrFileName As String)
QueryAuthGroupParams.ToXMLString() -> String
QueryAuthGroupService.AddQueryAuthGroup(ByVal pIQueryAuthGroup As QueryAuthGroup) -> QueryAuthGroup
QueryAuthGroupService.GetDataInterface(ByVal enumMSDI As QueryAuthGroupServiceDataInterfaces) -> Object
QueryAuthGroupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
QueryAuthGroupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
QueryAuthGroupService.GetQueryAuthGroup(ByVal pIQueryAuthGroupParams As QueryAuthGroupParams) -> QueryAuthGroup
QueryAuthGroupService.GetQueryAuthGroupList() -> QueryAuthGroupCollection
QueryAuthGroupService.RemoveQueryAuthGroup(ByVal pIQueryAuthGroupParams As QueryAuthGroupParams)
QueryAuthGroupService.UpdateQueryAuthGroup(ByVal pIQueryAuthGroup As QueryAuthGroup)
QueryCategories.Browser : DataBrowser [R]
QueryCategories.Code : Long [R]
QueryCategories.Name : String [R/W]
QueryCategories.Permissions : String [R/W]
QueryCategories.UserFields : UserFields [R]
QueryCategories.Add() -> Long
QueryCategories.GetAsXML() -> String
QueryCategories.GetByKey(ByVal lID As Long) -> Boolean
QueryCategories.SaveToFile(ByVal FileName As String)
QueryCategories.SaveXML(ByRef FileName As String)
QueryCategories.Update() -> Long
Queue.Browser : DataBrowser [R]
Queue.Description : String [R/W]
Queue.Inactive : BoYesNoEnum [R/W]
Queue.QueueEmail : String [R/W]
Queue.QueueID : String [R/W]
Queue.QueueManager : Long [R/W]
Queue.QueueMembers : QueueMembers [R]
Queue.UserFields : UserFields [R]
Queue.Add() -> Long
Queue.GetAsXML() -> String
Queue.GetByKey(ByVal bstrQueueID As String) -> Boolean
Queue.Remove() -> Long
Queue.SaveToFile(ByVal FileName As String)
Queue.SaveXML(ByRef FileName As String)
Queue.Update() -> Long
QueueMembers.Count : Long [R]
QueueMembers.MemberUserID : Long [R/W]
QueueMembers.QueueID : String [R/W]
QueueMembers.UserFields : UserFields [R]
QueueMembers.Add()
QueueMembers.SetCurrentLine(ByVal LineNum As Long)
RclRecurringExecutionParams.OnError : RclRecurringExecutionHandlingEnum [R/W]
RclRecurringExecutionParams.FromXMLFile(ByVal bstrFileName As String)
RclRecurringExecutionParams.FromXMLString(ByVal bstrXML As String)
RclRecurringExecutionParams.GetXMLSchema() -> String
RclRecurringExecutionParams.ToXMLFile(ByVal bstrFileName As String)
RclRecurringExecutionParams.ToXMLString() -> String
RclRecurringTransaction.DocEntry : Long [R]
RclRecurringTransaction.DocType : String [R]
RclRecurringTransaction.Instance : Long [R]
RclRecurringTransaction.PlannedDate : Date [R]
RclRecurringTransaction.Status : RclRecurringTransactionStatusEnum [R]
RclRecurringTransaction.TemplateID : Long [R]
RclRecurringTransaction.TransactionID : Long [R]
RclRecurringTransaction.FromXMLFile(ByVal bstrFileName As String)
RclRecurringTransaction.FromXMLString(ByVal bstrXML As String)
RclRecurringTransaction.GetXMLSchema() -> String
RclRecurringTransaction.ToXMLFile(ByVal bstrFileName As String)
RclRecurringTransaction.ToXMLString() -> String
RclRecurringTransactionCollection.Count : Long [R]
RclRecurringTransactionCollection.Add() -> RclRecurringTransaction
RclRecurringTransactionCollection.GetXMLSchema() -> String
RclRecurringTransactionCollection.Item(ByVal vtIndex As Variant) -> RclRecurringTransaction
RclRecurringTransactionCollection.ToXMLFile(ByVal bstrFileName As String)
RclRecurringTransactionCollection.ToXMLString() -> String
RclRecurringTransactionParams.PlannedDate : Date [R/W]
RclRecurringTransactionParams.TransactionID : Long [R/W]
RclRecurringTransactionParams.FromXMLFile(ByVal bstrFileName As String)
RclRecurringTransactionParams.FromXMLString(ByVal bstrXML As String)
RclRecurringTransactionParams.GetXMLSchema() -> String
RclRecurringTransactionParams.ToXMLFile(ByVal bstrFileName As String)
RclRecurringTransactionParams.ToXMLString() -> String
RclRecurringTransactionParamsCollection.Count : Long [R]
RclRecurringTransactionParamsCollection.Add() -> RclRecurringTransactionParams
RclRecurringTransactionParamsCollection.GetXMLSchema() -> String
RclRecurringTransactionParamsCollection.Item(ByVal vtIndex As Variant) -> RclRecurringTransactionParams
RclRecurringTransactionParamsCollection.ToXMLFile(ByVal bstrFileName As String)
RclRecurringTransactionParamsCollection.ToXMLString() -> String
Recipient.CellularNumber : String [R/W]
Recipient.EmailAddress : String [R/W]
Recipient.FaxNumber : String [R/W]
Recipient.NameTo : String [R/W]
Recipient.SendEmail : BoYesNoEnum [R/W]
Recipient.SendFax : BoYesNoEnum [R/W]
Recipient.SendInternal : BoYesNoEnum [R/W]
Recipient.SendSMS : BoYesNoEnum [R/W]
Recipient.UserCode : String [R/W]
Recipient.UserType : BoMsgRcpTypes [R/W]
Recipient.FromXMLFile(ByVal bstrFileName As String)
Recipient.FromXMLString(ByVal bstrXML As String)
Recipient.GetXMLSchema() -> String
Recipient.ToXMLFile(ByVal bstrFileName As String)
Recipient.ToXMLString() -> String
RecipientCollection.Count : Long [R]
RecipientCollection.Add() -> Recipient
RecipientCollection.GetXMLSchema() -> String
RecipientCollection.Item(ByVal vtIndex As Variant) -> Recipient
RecipientCollection.ToXMLFile(ByVal bstrFileName As String)
RecipientCollection.ToXMLString() -> String
Recipients.CellularNumber : String [R/W]
Recipients.Count : Long [R]
Recipients.EmailAddress : String [R/W]
Recipients.FaxNumber : String [R/W]
Recipients.NameTo : String [R/W]
Recipients.SendEmail : BoYesNoEnum [R/W]
Recipients.SendFax : BoYesNoEnum [R/W]
Recipients.SendInternal : BoYesNoEnum [R/W]
Recipients.SendSMS : BoYesNoEnum [R/W]
Recipients.UserCode : String [R/W]
Recipients.UserType : BoMsgRcpTypes [R/W]
Recipients.Add()
Recipients.SetCurrentLine(ByVal LineNum As Long)
ReconciliationBankStatementLine.amount : Double [R]
ReconciliationBankStatementLine.BankStatementAccountCode : String [R/W]
ReconciliationBankStatementLine.Date : Date [R]
ReconciliationBankStatementLine.Details : String [R]
ReconciliationBankStatementLine.Ref1 : String [R]
ReconciliationBankStatementLine.Sequence : Long [R/W]
ReconciliationBankStatementLine.FromXMLFile(ByVal bstrFileName As String)
ReconciliationBankStatementLine.FromXMLString(ByVal bstrXML As String)
ReconciliationBankStatementLine.GetXMLSchema() -> String
ReconciliationBankStatementLine.ToXMLFile(ByVal bstrFileName As String)
ReconciliationBankStatementLine.ToXMLString() -> String
ReconciliationBankStatementLines.Count : Long [R]
ReconciliationBankStatementLines.Add() -> ReconciliationBankStatementLine
ReconciliationBankStatementLines.GetXMLSchema() -> String
ReconciliationBankStatementLines.Item(ByVal vtIndex As Variant) -> ReconciliationBankStatementLine
ReconciliationBankStatementLines.ToXMLFile(ByVal bstrFileName As String)
ReconciliationBankStatementLines.ToXMLString() -> String
ReconciliationJournalEntryLine.CreditAmount : Double [R]
ReconciliationJournalEntryLine.DebitAmount : Double [R]
ReconciliationJournalEntryLine.Details : String [R]
ReconciliationJournalEntryLine.DueDate : Date [R]
ReconciliationJournalEntryLine.LineNumber : Long [R/W]
ReconciliationJournalEntryLine.PostingDate : Date [R]
ReconciliationJournalEntryLine.Ref1 : String [R]
ReconciliationJournalEntryLine.Ref2 : String [R]
ReconciliationJournalEntryLine.Ref3 : String [R]
ReconciliationJournalEntryLine.TransactionNumber : Long [R/W]
ReconciliationJournalEntryLine.FromXMLFile(ByVal bstrFileName As String)
ReconciliationJournalEntryLine.FromXMLString(ByVal bstrXML As String)
ReconciliationJournalEntryLine.GetXMLSchema() -> String
ReconciliationJournalEntryLine.ToXMLFile(ByVal bstrFileName As String)
ReconciliationJournalEntryLine.ToXMLString() -> String
ReconciliationJournalEntryLines.Count : Long [R]
ReconciliationJournalEntryLines.Add() -> ReconciliationJournalEntryLine
ReconciliationJournalEntryLines.GetXMLSchema() -> String
ReconciliationJournalEntryLines.Item(ByVal vtIndex As Variant) -> ReconciliationJournalEntryLine
ReconciliationJournalEntryLines.ToXMLFile(ByVal bstrFileName As String)
ReconciliationJournalEntryLines.ToXMLString() -> String
Recordset.BoF : Boolean [R]
Recordset.Command : Command [R]
Recordset.EoF : Boolean [R]
Recordset.Fields : Fields [R]
Recordset.RecordCount : Long [R]
Recordset.RecordSetAudit : Boolean [R/W]
Recordset.DoQuery(ByVal QueryStr As String)
Recordset.GetAsXML() -> String
Recordset.GetFixedSchema() -> String
Recordset.GetFixedXML(ByVal xmlMode As RecordsetXMLModeEnum) -> String
Recordset.MoveFirst()
Recordset.MoveLast()
Recordset.MoveNext()
Recordset.MovePrevious()
Recordset.SaveToFile(ByVal FileName As String)
Recordset.SaveXML(ByRef FileName As String)
RecordsetEx.ColumnsCount : Long [R]
RecordsetEx.EoF : Boolean [R]
RecordsetEx.RecordSetAudit : Boolean [R/W]
RecordsetEx.DoQuery(ByVal QueryStr As String)
RecordsetEx.GetColumnType(ByVal Index As Variant) -> BoFieldTypes
RecordsetEx.GetColumnValue(ByVal Index As Variant) -> Variant
RecordsetEx.MoveNext() -> Boolean
RecurringPostings.AutomaticVAT : BoYesNoEnum [R/W]
RecurringPostings.Code : String [R/W]
RecurringPostings.DeferredTax : BoYesNoEnum [R/W]
RecurringPostings.Description : String [R/W]
RecurringPostings.Frequency : BoFrequencyTypeEnum [R/W]
RecurringPostings.Instance : Long [R]
RecurringPostings.ManageWTax : BoYesNoEnum [R/W]
RecurringPostings.NextExecution : Date [R/W]
RecurringPostings.RecurringPostingsDocumentReferenceCollection : RecurringPostingsDocumentReferenceCollection [R]
RecurringPostings.RecurringPostingsLineCollection : RecurringPostingsLineCollection [R]
RecurringPostings.Reference1 : String [R/W]
RecurringPostings.Reference2 : String [R/W]
RecurringPostings.Reference3 : String [R/W]
RecurringPostings.Remarks : String [R/W]
RecurringPostings.StampTax : BoYesNoEnum [R/W]
RecurringPostings.SubFrequency : BoSubFrequencyTypeEnum [R/W]
RecurringPostings.TransactionCode : String [R/W]
RecurringPostings.ValidUntil : BoYesNoEnum [R/W]
RecurringPostings.ValidUntilDate : Date [R/W]
RecurringPostings.FromXMLFile(ByVal bstrFileName As String)
RecurringPostings.FromXMLString(ByVal bstrXML As String)
RecurringPostings.GetXMLSchema() -> String
RecurringPostings.ToXMLFile(ByVal bstrFileName As String)
RecurringPostings.ToXMLString() -> String
RecurringPostingsDocumentReference.ExternalReferencedDocNumber : String [R/W]
RecurringPostingsDocumentReference.IssueDate : Date [R/W]
RecurringPostingsDocumentReference.LineNumber : Long [R]
RecurringPostingsDocumentReference.RcrCode : String [R]
RecurringPostingsDocumentReference.ReferencedDocEntry : Long [R/W]
RecurringPostingsDocumentReference.ReferencedDocNumber : Long [R]
RecurringPostingsDocumentReference.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
RecurringPostingsDocumentReference.Remark : String [R/W]
RecurringPostingsDocumentReference.FromXMLFile(ByVal bstrFileName As String)
RecurringPostingsDocumentReference.FromXMLString(ByVal bstrXML As String)
RecurringPostingsDocumentReference.GetXMLSchema() -> String
RecurringPostingsDocumentReference.ToXMLFile(ByVal bstrFileName As String)
RecurringPostingsDocumentReference.ToXMLString() -> String
RecurringPostingsDocumentReferenceCollection.Count : Long [R]
RecurringPostingsDocumentReferenceCollection.Add() -> RecurringPostingsDocumentReference
RecurringPostingsDocumentReferenceCollection.GetXMLSchema() -> String
RecurringPostingsDocumentReferenceCollection.Item(ByVal vtIndex As Variant) -> RecurringPostingsDocumentReference
RecurringPostingsDocumentReferenceCollection.Remove(ByVal vtIndex As Variant)
RecurringPostingsDocumentReferenceCollection.ToXMLFile(ByVal bstrFileName As String)
RecurringPostingsDocumentReferenceCollection.ToXMLString() -> String
RecurringPostingsLine.AccountCode : String [R/W]
RecurringPostingsLine.AccountName : String [R]
RecurringPostingsLine.ControlAccount : String [R/W]
RecurringPostingsLine.CostElementCode : String [R]
RecurringPostingsLine.CostingCode1 : String [R/W]
RecurringPostingsLine.CostingCode2 : String [R/W]
RecurringPostingsLine.CostingCode3 : String [R/W]
RecurringPostingsLine.CostingCode4 : String [R/W]
RecurringPostingsLine.CostingCode5 : String [R/W]
RecurringPostingsLine.Credit : Double [R/W]
RecurringPostingsLine.Currency : String [R/W]
RecurringPostingsLine.Debit : Double [R/W]
RecurringPostingsLine.DistributionRule : String [R/W]
RecurringPostingsLine.LineNumber : Long [R]
RecurringPostingsLine.ProjectCode : String [R/W]
RecurringPostingsLine.RcrCode : String [R]
RecurringPostingsLine.TaxCode : String [R/W]
RecurringPostingsLine.TaxGroup : String [R/W]
RecurringPostingsLine.TaxPostingAccount : BoTaxPostingAccountTypeEnum [R/W]
RecurringPostingsLine.VatLine : BoYesNoEnum [R/W]
RecurringPostingsLine.WTaxLiable : BoYesNoEnum [R/W]
RecurringPostingsLine.WTaxLine : BoYesNoEnum [R/W]
RecurringPostingsLine.FromXMLFile(ByVal bstrFileName As String)
RecurringPostingsLine.FromXMLString(ByVal bstrXML As String)
RecurringPostingsLine.GetXMLSchema() -> String
RecurringPostingsLine.ToXMLFile(ByVal bstrFileName As String)
RecurringPostingsLine.ToXMLString() -> String
RecurringPostingsLineCollection.Count : Long [R]
RecurringPostingsLineCollection.Add() -> RecurringPostingsLine
RecurringPostingsLineCollection.GetXMLSchema() -> String
RecurringPostingsLineCollection.Item(ByVal vtIndex As Variant) -> RecurringPostingsLine
RecurringPostingsLineCollection.Remove(ByVal vtIndex As Variant)
RecurringPostingsLineCollection.ToXMLFile(ByVal bstrFileName As String)
RecurringPostingsLineCollection.ToXMLString() -> String
RecurringPostingsParams.Code : String [R/W]
RecurringPostingsParams.Description : String [R]
RecurringPostingsParams.Instance : Long [R/W]
RecurringPostingsParams.FromXMLFile(ByVal bstrFileName As String)
RecurringPostingsParams.FromXMLString(ByVal bstrXML As String)
RecurringPostingsParams.GetXMLSchema() -> String
RecurringPostingsParams.ToXMLFile(ByVal bstrFileName As String)
RecurringPostingsParams.ToXMLString() -> String
RecurringPostingsParamsCollection.Count : Long [R]
RecurringPostingsParamsCollection.Add() -> RecurringPostingsParams
RecurringPostingsParamsCollection.GetXMLSchema() -> String
RecurringPostingsParamsCollection.Item(ByVal vtIndex As Variant) -> RecurringPostingsParams
RecurringPostingsParamsCollection.ToXMLFile(ByVal bstrFileName As String)
RecurringPostingsParamsCollection.ToXMLString() -> String
RecurringPostingsService.Add(ByVal pIRecurringPostings As RecurringPostings) -> RecurringPostingsParams
RecurringPostingsService.Delete(ByVal pIRecurringPostingsParams As RecurringPostingsParams)
RecurringPostingsService.Get(ByVal pIRecurringPostingsParams As RecurringPostingsParams) -> RecurringPostings
RecurringPostingsService.GetDataInterface(ByVal enumMSDI As RecurringPostingsServiceDataInterfaces) -> Object
RecurringPostingsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
RecurringPostingsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
RecurringPostingsService.GetList() -> RecurringPostingsParamsCollection
RecurringPostingsService.Update(ByVal pIRecurringPostings As RecurringPostings)
RecurringTransactionService.DeleteRecurringTransactions(ByVal pIRclRecurringTransactionParamsCollection As RclRecurringTransactionParamsCollection)
RecurringTransactionService.ExecuteRecurringTransactions(ByVal pIRclRecurringTransactionParamsCollection As RclRecurringTransactionParamsCollection, ByVal pIRclRecurringExecutionParams As RclRecurringExecutionParams) -> RclRecurringTransactionCollection
RecurringTransactionService.GetAvailableRecurringTransactions() -> RclRecurringTransactionCollection
RecurringTransactionService.GetDataInterface(ByVal enumMSDI As RecurringTransactionServiceDataInterfaces) -> Object
RecurringTransactionService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
RecurringTransactionService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
RecurringTransactionService.GetRecurringTransaction(ByVal pIRclRecurringTransactionParams As RclRecurringTransactionParams) -> RclRecurringTransaction
RelatedDocument.AbsEntry : Long [R/W]
RelatedDocument.DocType : RelatedDocumentTypeEnum [R/W]
RelatedDocument.UUID : String [R]
RelatedDocument.FromXMLFile(ByVal bstrFileName As String)
RelatedDocument.FromXMLString(ByVal bstrXML As String)
RelatedDocument.GetXMLSchema() -> String
RelatedDocument.ToXMLFile(ByVal bstrFileName As String)
RelatedDocument.ToXMLString() -> String
RelatedDocumentCollection.Count : Long [R]
RelatedDocumentCollection.Add() -> RelatedDocument
RelatedDocumentCollection.GetXMLSchema() -> String
RelatedDocumentCollection.Item(ByVal vtIndex As Variant) -> RelatedDocument
RelatedDocumentCollection.ToXMLFile(ByVal bstrFileName As String)
RelatedDocumentCollection.ToXMLString() -> String
RelatedDocuments.AbsEntry : Long [R/W]
RelatedDocuments.Count : Long [R]
RelatedDocuments.DocType : RelatedDocumentTypeEnum [R/W]
RelatedDocuments.UUID : String [R]
RelatedDocuments.Add()
RelatedDocuments.Delete()
RelatedDocuments.SetCurrentLine(ByVal LineNum As Long)
Relationships.Browser : DataBrowser [R]
Relationships.RelationshipCode : Long [R]
Relationships.RelationshipDescription : String [R/W]
Relationships.UserFields : UserFields [R]
Relationships.Add() -> Long
Relationships.GetAsXML() -> String
Relationships.GetByKey(ByVal lID As Long) -> Boolean
Relationships.Remove() -> Long
Relationships.SaveToFile(ByVal FileName As String)
Relationships.SaveXML(ByRef FileName As String)
Relationships.Update() -> Long
ReportFilterService.AddTaxReportFilter(ByVal pITaxReportFilter As TaxReportFilter) -> TaxReportFilterParams
ReportFilterService.DeleteTaxReportFilter(ByVal pITaxReportFilterParams As TaxReportFilterParams)
ReportFilterService.GetDataInterface(ByVal enumMSDI As ReportFilterServiceDataInterfaces) -> Object
ReportFilterService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ReportFilterService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ReportFilterService.GetTaxReportFilter(ByVal pITaxReportFilterParams As TaxReportFilterParams) -> TaxReportFilter
ReportFilterService.GetTaxReportFilterList(ByVal pITaxReportFilterParams As TaxReportFilterParams) -> TaxReportFiltersParams
ReportFilterService.UpdateTaxReportFilter(ByVal pITaxReportFilter As TaxReportFilter)
ReportLayout.AllignFooterToBottom : BoYesNoEnum [R/W]
ReportLayout.Author : String [R/W]
ReportLayout.B1Version : String [R/W]
ReportLayout.BottomMargin : Long [R/W]
ReportLayout.Category : ReportLayoutCategoryEnum [R/W]
ReportLayout.ChangeFontSizeForEMail : Long [R/W]
ReportLayout.ChangeFontSizeInPreview : Long [R/W]
ReportLayout.ConvertFontForEMail : BoYesNoEnum [R/W]
ReportLayout.ConvertFontInPrintPreview : BoYesNoEnum [R/W]
ReportLayout.CRVersion : String [R/W]
ReportLayout.Editable : BoYesNoEnum [R]
ReportLayout.EMailFont : String [R/W]
ReportLayout.ExtensionErrorAction : BoExtensionErrorActionEnum [R/W]
ReportLayout.ExtensionName : String [R/W]
ReportLayout.FollowUpReport : String [R/W]
ReportLayout.ForeignLanguageReport : BoYesNoEnum [R/W]
ReportLayout.GridSize : Long [R/W]
ReportLayout.GridType : BoGridTypeEnum [R/W]
ReportLayout.Height : Long [R/W]
ReportLayout.ImpExpObjCode : Long [R/W]
ReportLayout.language : Long [R/W]
ReportLayout.LayoutCode : String [R]
ReportLayout.LeaderReport : String [R/W]
ReportLayout.LeftMargin : Long [R/W]
ReportLayout.Localization : String [R/W]
ReportLayout.Name : String [R/W]
ReportLayout.NumberOfCopies : Long [R/W]
ReportLayout.Orientation : BoOrientationEnum [R/W]
ReportLayout.PaperSize : String [R/W]
ReportLayout.Picture : String [R/W]
ReportLayout.PreviewPrintingFont : String [R/W]
ReportLayout.Printer : String [R/W]
ReportLayout.PrinterFirstPage : String [R/W]
ReportLayout.Query : String [R/W]
ReportLayout.QueryType : BoQueryTypeEnum [R/W]
ReportLayout.Remarks : String [R/W]
ReportLayout.RepetitiveAreasNumber : Long [R]
ReportLayout.ReportLayoutItems : ReportLayoutItems [R/W]
ReportLayout.RightMargin : Long [R/W]
ReportLayout.ShowGrid : BoYesNoEnum [R/W]
ReportLayout.SnapToGrid : BoYesNoEnum [R/W]
ReportLayout.Sortable : BoYesNoEnum [R]
ReportLayout.TopMargin : Long [R/W]
ReportLayout.TranslationLines : ReportLayout_TranslationLines [R]
ReportLayout.TypeCode : String [R/W]
ReportLayout.TypeDetail : String [R/W]
ReportLayout.UseFirstPrinter : BoYesNoEnum [R/W]
ReportLayout.Width : Long [R/W]
ReportLayout.FromXMLFile(ByVal bstrFileName As String)
ReportLayout.FromXMLString(ByVal bstrXML As String)
ReportLayout.GetXMLSchema() -> String
ReportLayout.ToXMLFile(ByVal bstrFileName As String)
ReportLayout.ToXMLString() -> String
ReportLayout_TranslationLine.CreateDate : Date [R/W]
ReportLayout_TranslationLine.CreateTime : Long [R/W]
ReportLayout_TranslationLine.DocEntry : String [R]
ReportLayout_TranslationLine.DocName : String [R/W]
ReportLayout_TranslationLine.LanguageCode : Long [R/W]
ReportLayout_TranslationLine.LineNumber : Long [R]
ReportLayout_TranslationLine.UpdateDate : Date [R/W]
ReportLayout_TranslationLine.UpdateTime : Long [R/W]
ReportLayout_TranslationLine.FromXMLFile(ByVal bstrFileName As String)
ReportLayout_TranslationLine.FromXMLString(ByVal bstrXML As String)
ReportLayout_TranslationLine.GetXMLSchema() -> String
ReportLayout_TranslationLine.ToXMLFile(ByVal bstrFileName As String)
ReportLayout_TranslationLine.ToXMLString() -> String
ReportLayout_TranslationLines.Count : Long [R]
ReportLayout_TranslationLines.Add() -> ReportLayout_TranslationLine
ReportLayout_TranslationLines.GetXMLSchema() -> String
ReportLayout_TranslationLines.Item(ByVal vtIndex As Variant) -> ReportLayout_TranslationLine
ReportLayout_TranslationLines.Remove(ByVal vtIndex As Variant)
ReportLayout_TranslationLines.ToXMLFile(ByVal bstrFileName As String)
ReportLayout_TranslationLines.ToXMLString() -> String
ReportLayoutItem.BackgroundBlue : Long [R/W]
ReportLayoutItem.BackgroundGreen : Long [R/W]
ReportLayoutItem.BackgroundRed : Long [R/W]
ReportLayoutItem.BarCodeStandard : BoBarCodeStandardEnum [R/W]
ReportLayoutItem.BlockFontChange : BoYesNoEnum [R/W]
ReportLayoutItem.BorderBlue : Long [R/W]
ReportLayoutItem.BorderGreen : Long [R/W]
ReportLayoutItem.BorderRed : Long [R/W]
ReportLayoutItem.BottomBorderLineThickness : Long [R/W]
ReportLayoutItem.BottomMargin : Long [R/W]
ReportLayoutItem.DataSource : BoDataSourceEnum [R/W]
ReportLayoutItem.DisplayDescription : BoYesNoEnum [R/W]
ReportLayoutItem.DisplayRepetitiveAreaFooterOnAllPages : BoYesNoEnum [R/W]
ReportLayoutItem.DisplayTotalAsAWord : BoYesNoEnum [R/W]
ReportLayoutItem.DistanceToRepetitiveDuplicate : Long [R/W]
ReportLayoutItem.DuplicateRepetitiveArea : BoYesNoEnum [R/W]
ReportLayoutItem.Editable : Long [R/W]
ReportLayoutItem.FieldIdentifier : String [R/W]
ReportLayoutItem.FieldName : String [R/W]
ReportLayoutItem.FontName : String [R/W]
ReportLayoutItem.FontSize : Long [R/W]
ReportLayoutItem.GroupNumber : Long [R/W]
ReportLayoutItem.Height : Long [R/W]
ReportLayoutItem.HeightAdjustments : BoYesNoEnum [R/W]
ReportLayoutItem.HideRepetitiveAreaIfEmpty : BoYesNoEnum [R/W]
ReportLayoutItem.HighlightBlue : Long [R/W]
ReportLayoutItem.HighlightGreen : Long [R/W]
ReportLayoutItem.HighlightRed : Long [R/W]
ReportLayoutItem.HorizontalAlignment : BoHorizontalAlignmentEnum [R/W]
ReportLayoutItem.ItemIndex : Long [R/W]
ReportLayoutItem.ItemNumber : Long [R/W]
ReportLayoutItem.Left : Long [R/W]
ReportLayoutItem.LeftBorderLineThickness : Long [R/W]
ReportLayoutItem.LeftMargin : Long [R/W]
ReportLayoutItem.LineBreak : BoLineBreakEnum [R/W]
ReportLayoutItem.LinkToField : String [R/W]
ReportLayoutItem.NewPage : BoYesNoEnum [R/W]
ReportLayoutItem.NextSegmentItemNumber : String [R/W]
ReportLayoutItem.NumberOfLinesInRepetitiveArea : Long [R/W]
ReportLayoutItem.ParentIndex : Long [R/W]
ReportLayoutItem.ParentType : Long [R/W]
ReportLayoutItem.PictureSize : BoPictureSizeEnum [R/W]
ReportLayoutItem.PrintAsBarCode : BoYesNoEnum [R/W]
ReportLayoutItem.RelateToField : String [R/W]
ReportLayoutItem.ReverseSort : BoYesNoEnum [R/W]
ReportLayoutItem.RightBorderLineThickness : Long [R/W]
ReportLayoutItem.RightMargin : Long [R/W]
ReportLayoutItem.SetAsGroup : BoYesNoEnum [R/W]
ReportLayoutItem.ShadowThickness : Long [R/W]
ReportLayoutItem.SortLevel : Long [R/W]
ReportLayoutItem.SortType : BoSortTypeEnum [R/W]
ReportLayoutItem.String : String [R/W]
ReportLayoutItem.StringFiller : String [R/W]
ReportLayoutItem.StringLength : Long [R/W]
ReportLayoutItem.SuppressZeros : BoYesNoEnum [R/W]
ReportLayoutItem.TableName : String [R/W]
ReportLayoutItem.TextBlue : Long [R/W]
ReportLayoutItem.TextGreen : Long [R/W]
ReportLayoutItem.TextRed : Long [R/W]
ReportLayoutItem.TextStyle : Long [R/W]
ReportLayoutItem.Top : Long [R/W]
ReportLayoutItem.TopBorderLineThickness : Long [R/W]
ReportLayoutItem.TopMargin : Long [R/W]
ReportLayoutItem.Type : BoReportLayoutItemTypeEnum [R/W]
ReportLayoutItem.Unique : BoYesNoEnum [R/W]
ReportLayoutItem.VariableNumber : Long [R/W]
ReportLayoutItem.VerticalAlignment : BoVerticalAlignmentEnum [R/W]
ReportLayoutItem.Visible : BoYesNoEnum [R/W]
ReportLayoutItem.Width : Long [R/W]
ReportLayoutItem.FromXMLFile(ByVal bstrFileName As String)
ReportLayoutItem.FromXMLString(ByVal bstrXML As String)
ReportLayoutItem.GetXMLSchema() -> String
ReportLayoutItem.ToXMLFile(ByVal bstrFileName As String)
ReportLayoutItem.ToXMLString() -> String
ReportLayoutItems.Count : Long [R]
ReportLayoutItems.Add() -> ReportLayoutItem
ReportLayoutItems.GetXMLSchema() -> String
ReportLayoutItems.Item(ByVal vtIndex As Variant) -> ReportLayoutItem
ReportLayoutItems.ToXMLFile(ByVal bstrFileName As String)
ReportLayoutItems.ToXMLString() -> String
ReportLayoutParams.Category : ReportLayoutCategoryEnum [R]
ReportLayoutParams.LayoutCode : String [R/W]
ReportLayoutParams.LayoutName : String [R]
ReportLayoutParams.FromXMLFile(ByVal bstrFileName As String)
ReportLayoutParams.FromXMLString(ByVal bstrXML As String)
ReportLayoutParams.GetXMLSchema() -> String
ReportLayoutParams.ToXMLFile(ByVal bstrFileName As String)
ReportLayoutParams.ToXMLString() -> String
ReportLayoutPrintParams.DocEntry : Long [R/W]
ReportLayoutPrintParams.LayoutCode : String [R/W]
ReportLayoutPrintParams.FromXMLFile(ByVal bstrFileName As String)
ReportLayoutPrintParams.FromXMLString(ByVal bstrXML As String)
ReportLayoutPrintParams.GetXMLSchema() -> String
ReportLayoutPrintParams.ToXMLFile(ByVal bstrFileName As String)
ReportLayoutPrintParams.ToXMLString() -> String
ReportLayoutsParams.Count : Long [R]
ReportLayoutsParams.Add() -> ReportLayoutParams
ReportLayoutsParams.GetXMLSchema() -> String
ReportLayoutsParams.Item(ByVal vtIndex As Variant) -> ReportLayoutParams
ReportLayoutsParams.ToXMLFile(ByVal bstrFileName As String)
ReportLayoutsParams.ToXMLString() -> String
ReportLayoutsService.AddReportLayout(ByVal pIReportLayout As ReportLayout) -> ReportLayoutParams
ReportLayoutsService.AddReportLayoutToMenu(ByVal ppIReportLayout As ReportLayout, ByVal MenuID As String) -> ReportLayoutParams
ReportLayoutsService.DeleteReportLayout(ByVal pIReportLayoutParams As ReportLayoutParams)
ReportLayoutsService.DeleteReportLayoutAndMenu(ByVal ppIReportLayoutParams As ReportLayoutParams)
ReportLayoutsService.GetDataInterface(ByVal enumMSDI As ReportLayoutsServiceDataInterfaces) -> Object
ReportLayoutsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ReportLayoutsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ReportLayoutsService.GetDefaultReport(ByVal pIReportParams As ReportParams) -> DefaultReportParams
ReportLayoutsService.GetDefaultReportLayout(ByVal pIReportParams As ReportParams) -> ReportLayout
ReportLayoutsService.GetReportLayout(ByVal pIReportLayoutParams As ReportLayoutParams) -> ReportLayout
ReportLayoutsService.GetReportLayoutList(ByVal pIReportParams As ReportParams) -> ReportLayoutsParams
ReportLayoutsService.Print(ByVal ppIReportLayoutPrintParams As ReportLayoutPrintParams)
ReportLayoutsService.SetDefaultReport(ByVal ppIDefaultReportParams As DefaultReportParams)
ReportLayoutsService.UpdateLanguageReport(ByVal ppIReportLayout As ReportLayout)
ReportLayoutsService.UpdatePrinterSettings(ByVal pIReportLayout As ReportLayout)
ReportParams.CardCode : String [R/W]
ReportParams.ReportCode : String [R/W]
ReportParams.UserID : Long [R/W]
ReportParams.FromXMLFile(ByVal bstrFileName As String)
ReportParams.FromXMLString(ByVal bstrXML As String)
ReportParams.GetXMLSchema() -> String
ReportParams.ToXMLFile(ByVal bstrFileName As String)
ReportParams.ToXMLString() -> String
ReportType.AddonFormType : String [R/W]
ReportType.AddonName : String [R/W]
ReportType.DefaultReportLayout : String [R/W]
ReportType.MenuID : String [R/W]
ReportType.TypeCode : String [R]
ReportType.TypeName : String [R/W]
ReportType.FromXMLFile(ByVal bstrFileName As String)
ReportType.FromXMLString(ByVal bstrXML As String)
ReportType.GetXMLSchema() -> String
ReportType.ToXMLFile(ByVal bstrFileName As String)
ReportType.ToXMLString() -> String
ReportTypeParams.AddonFormType : String [R]
ReportTypeParams.AddonName : String [R]
ReportTypeParams.MenuID : String [R]
ReportTypeParams.TypeCode : String [R/W]
ReportTypeParams.TypeName : String [R]
ReportTypeParams.FromXMLFile(ByVal bstrFileName As String)
ReportTypeParams.FromXMLString(ByVal bstrXML As String)
ReportTypeParams.GetXMLSchema() -> String
ReportTypeParams.ToXMLFile(ByVal bstrFileName As String)
ReportTypeParams.ToXMLString() -> String
ReportTypesParams.Count : Long [R]
ReportTypesParams.Add() -> ReportTypeParams
ReportTypesParams.GetXMLSchema() -> String
ReportTypesParams.Item(ByVal vtIndex As Variant) -> ReportTypeParams
ReportTypesParams.ToXMLFile(ByVal bstrFileName As String)
ReportTypesParams.ToXMLString() -> String
ReportTypesService.AddReportType(ByVal pIReportType As ReportType) -> ReportTypeParams
ReportTypesService.DeleteReportType(ByVal pIReportType As ReportType)
ReportTypesService.GetDataInterface(ByVal enumMSDI As ReportTypesServiceDataInterfaces) -> Object
ReportTypesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ReportTypesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ReportTypesService.GetReportType(ByVal pIReportTypeParams As ReportTypeParams) -> ReportType
ReportTypesService.GetReportTypeList() -> ReportTypesParams
ReportTypesService.UpdateReportType(ByVal pIReportType As ReportType)
Resource.Active : BoYesNoEnum [R/W]
Resource.ActiveFrom : Date [R/W]
Resource.ActiveRemarks : String [R/W]
Resource.ActiveTo : Date [R/W]
Resource.Allocation : ResourceAllocationEnum [R/W]
Resource.AttachmentEntry : String [R/W]
Resource.Code : String [R]
Resource.CodeBar : String [R/W]
Resource.Cost1 : Double [R/W]
Resource.Cost10 : Double [R/W]
Resource.Cost2 : Double [R/W]
Resource.Cost3 : Double [R/W]
Resource.Cost4 : Double [R/W]
Resource.Cost5 : Double [R/W]
Resource.Cost6 : Double [R/W]
Resource.Cost7 : Double [R/W]
Resource.Cost8 : Double [R/W]
Resource.Cost9 : Double [R/W]
Resource.DailyCapacities : ResourceDailyCapacities [R]
Resource.DefaultWarehouse : String [R/W]
Resource.Employees : ResourceEmployees [R]
Resource.FixedAssets : ResourceFixedAssets [R]
Resource.ForeignName : String [R/W]
Resource.Group : Long [R/W]
Resource.Inactive : BoYesNoEnum [R/W]
Resource.InactiveFrom : Date [R/W]
Resource.InactiveRemarks : String [R/W]
Resource.InactiveTo : Date [R/W]
Resource.IssueMethod : ResourceIssueMethodEnum [R/W]
Resource.LinkedItem : String [R]
Resource.Name : String [R/W]
Resource.Number : Long [R]
Resource.Picture : String [R/W]
Resource.Property1 : BoYesNoEnum [R/W]
Resource.Property10 : BoYesNoEnum [R/W]
Resource.Property11 : BoYesNoEnum [R/W]
Resource.Property12 : BoYesNoEnum [R/W]
Resource.Property13 : BoYesNoEnum [R/W]
Resource.Property14 : BoYesNoEnum [R/W]
Resource.Property15 : BoYesNoEnum [R/W]
Resource.Property16 : BoYesNoEnum [R/W]
Resource.Property17 : BoYesNoEnum [R/W]
Resource.Property18 : BoYesNoEnum [R/W]
Resource.Property19 : BoYesNoEnum [R/W]
Resource.Property2 : BoYesNoEnum [R/W]
Resource.Property20 : BoYesNoEnum [R/W]
Resource.Property21 : BoYesNoEnum [R/W]
Resource.Property22 : BoYesNoEnum [R/W]
Resource.Property23 : BoYesNoEnum [R/W]
Resource.Property24 : BoYesNoEnum [R/W]
Resource.Property25 : BoYesNoEnum [R/W]
Resource.Property26 : BoYesNoEnum [R/W]
Resource.Property27 : BoYesNoEnum [R/W]
Resource.Property28 : BoYesNoEnum [R/W]
Resource.Property29 : BoYesNoEnum [R/W]
Resource.Property3 : BoYesNoEnum [R/W]
Resource.Property30 : BoYesNoEnum [R/W]
Resource.Property31 : BoYesNoEnum [R/W]
Resource.Property32 : BoYesNoEnum [R/W]
Resource.Property33 : BoYesNoEnum [R/W]
Resource.Property34 : BoYesNoEnum [R/W]
Resource.Property35 : BoYesNoEnum [R/W]
Resource.Property36 : BoYesNoEnum [R/W]
Resource.Property37 : BoYesNoEnum [R/W]
Resource.Property38 : BoYesNoEnum [R/W]
Resource.Property39 : BoYesNoEnum [R/W]
Resource.Property4 : BoYesNoEnum [R/W]
Resource.Property40 : BoYesNoEnum [R/W]
Resource.Property41 : BoYesNoEnum [R/W]
Resource.Property42 : BoYesNoEnum [R/W]
Resource.Property43 : BoYesNoEnum [R/W]
Resource.Property44 : BoYesNoEnum [R/W]
Resource.Property45 : BoYesNoEnum [R/W]
Resource.Property46 : BoYesNoEnum [R/W]
Resource.Property47 : BoYesNoEnum [R/W]
Resource.Property48 : BoYesNoEnum [R/W]
Resource.Property49 : BoYesNoEnum [R/W]
Resource.Property5 : BoYesNoEnum [R/W]
Resource.Property50 : BoYesNoEnum [R/W]
Resource.Property51 : BoYesNoEnum [R/W]
Resource.Property52 : BoYesNoEnum [R/W]
Resource.Property53 : BoYesNoEnum [R/W]
Resource.Property54 : BoYesNoEnum [R/W]
Resource.Property55 : BoYesNoEnum [R/W]
Resource.Property56 : BoYesNoEnum [R/W]
Resource.Property57 : BoYesNoEnum [R/W]
Resource.Property58 : BoYesNoEnum [R/W]
Resource.Property59 : BoYesNoEnum [R/W]
Resource.Property6 : BoYesNoEnum [R/W]
Resource.Property60 : BoYesNoEnum [R/W]
Resource.Property61 : BoYesNoEnum [R/W]
Resource.Property62 : BoYesNoEnum [R/W]
Resource.Property63 : BoYesNoEnum [R/W]
Resource.Property64 : BoYesNoEnum [R/W]
Resource.Property7 : BoYesNoEnum [R/W]
Resource.Property8 : BoYesNoEnum [R/W]
Resource.Property9 : BoYesNoEnum [R/W]
Resource.RelevantForSingleRun1 : BoYesNoEnum [R/W]
Resource.RelevantForSingleRun2 : BoYesNoEnum [R/W]
Resource.RelevantForSingleRun3 : BoYesNoEnum [R/W]
Resource.RelevantForSingleRun4 : BoYesNoEnum [R/W]
Resource.Remarks : String [R/W]
Resource.Series : Long [R/W]
Resource.TimePerUnits : Long [R/W]
Resource.Type : ResourceTypeEnum [R/W]
Resource.UnitOfMeasure : String [R/W]
Resource.UnitsPerTime : Long [R/W]
Resource.UserFields : Fields [R]
Resource.VisCode : String [R/W]
Resource.Warehouses : ResourceWarehouses [R]
Resource.FromXMLFile(ByVal bstrFileName As String)
Resource.FromXMLString(ByVal bstrXML As String)
Resource.GetXMLSchema() -> String
Resource.ToXMLFile(ByVal bstrFileName As String)
Resource.ToXMLString() -> String
ResourceCapacitiesService.Add(ByVal pIResourceCapacity As ResourceCapacity) -> ResourceCapacityParams
ResourceCapacitiesService.Get(ByVal pIResourceCapacityParams As ResourceCapacityParams) -> ResourceCapacity
ResourceCapacitiesService.GetDataInterface(ByVal enumMSDI As ResourceCapacitiesServiceDataInterfaces) -> Object
ResourceCapacitiesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ResourceCapacitiesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ResourceCapacitiesService.GetList() -> ResourceCapacityParamsCollection
ResourceCapacitiesService.GetListWithFilter(ByVal pIResourceCapacityWithFilterParams As ResourceCapacityWithFilterParams) -> ResourceCapacityParamsCollection
ResourceCapacitiesService.Update(ByVal pIResourceCapacity As ResourceCapacity)
ResourceCapacity.Action : ResourceCapacityActionEnum [R/W]
ResourceCapacity.BaseEntry : Long [R/W]
ResourceCapacity.BaseLineNum : Long [R/W]
ResourceCapacity.BaseType : ResourceCapacityBaseTypeEnum [R/W]
ResourceCapacity.Capacity : Double [R/W]
ResourceCapacity.Code : String [R/W]
ResourceCapacity.Date : Date [R/W]
ResourceCapacity.ID : Long [R]
ResourceCapacity.Memo : String [R/W]
ResourceCapacity.MemoSource : ResourceCapacityMemoSourceEnum [R/W]
ResourceCapacity.OwningEntry : Long [R/W]
ResourceCapacity.OwningLineNum : Long [R/W]
ResourceCapacity.OwningType : ResourceCapacityOwningTypeEnum [R/W]
ResourceCapacity.RevertedEntry : Long [R/W]
ResourceCapacity.RevertedLineNum : Long [R/W]
ResourceCapacity.RevertedType : ResourceCapacityRevertedTypeEnum [R/W]
ResourceCapacity.SingleRunCapacity : Double [R/W]
ResourceCapacity.SingleRunMemo : String [R/W]
ResourceCapacity.SingleRunMemoSource : ResourceCapacityMemoSourceEnum [R/W]
ResourceCapacity.SourceEntry : Long [R/W]
ResourceCapacity.SourceLineNum : Long [R/W]
ResourceCapacity.SourceType : ResourceCapacitySourceTypeEnum [R/W]
ResourceCapacity.Type : ResourceCapacityTypeEnum [R/W]
ResourceCapacity.Warehouse : String [R/W]
ResourceCapacity.FromXMLFile(ByVal bstrFileName As String)
ResourceCapacity.FromXMLString(ByVal bstrXML As String)
ResourceCapacity.GetXMLSchema() -> String
ResourceCapacity.ToXMLFile(ByVal bstrFileName As String)
ResourceCapacity.ToXMLString() -> String
ResourceCapacityParams.Action : ResourceCapacityActionEnum [R]
ResourceCapacityParams.BaseEntry : Long [R]
ResourceCapacityParams.BaseLineNum : Long [R]
ResourceCapacityParams.BaseType : ResourceCapacityBaseTypeEnum [R]
ResourceCapacityParams.Capacity : Double [R]
ResourceCapacityParams.Code : String [R]
ResourceCapacityParams.Date : Date [R]
ResourceCapacityParams.ID : Long [R/W]
ResourceCapacityParams.Memo : String [R]
ResourceCapacityParams.MemoSource : ResourceCapacityMemoSourceEnum [R]
ResourceCapacityParams.OwningEntry : Long [R]
ResourceCapacityParams.OwningLineNum : Long [R]
ResourceCapacityParams.OwningType : ResourceCapacityOwningTypeEnum [R]
ResourceCapacityParams.RevertedEntry : Long [R]
ResourceCapacityParams.RevertedLineNum : Long [R]
ResourceCapacityParams.RevertedType : ResourceCapacityRevertedTypeEnum [R]
ResourceCapacityParams.SingleRunCapacity : Double [R]
ResourceCapacityParams.SingleRunMemo : String [R]
ResourceCapacityParams.SingleRunMemoSource : ResourceCapacityMemoSourceEnum [R]
ResourceCapacityParams.SourceEntry : Long [R]
ResourceCapacityParams.SourceLineNum : Long [R]
ResourceCapacityParams.SourceType : ResourceCapacitySourceTypeEnum [R]
ResourceCapacityParams.Type : ResourceCapacityTypeEnum [R]
ResourceCapacityParams.Warehouse : String [R]
ResourceCapacityParams.FromXMLFile(ByVal bstrFileName As String)
ResourceCapacityParams.FromXMLString(ByVal bstrXML As String)
ResourceCapacityParams.GetXMLSchema() -> String
ResourceCapacityParams.ToXMLFile(ByVal bstrFileName As String)
ResourceCapacityParams.ToXMLString() -> String
ResourceCapacityParamsCollection.Count : Long [R]
ResourceCapacityParamsCollection.Add() -> ResourceCapacityParams
ResourceCapacityParamsCollection.GetXMLSchema() -> String
ResourceCapacityParamsCollection.Item(ByVal vtIndex As Variant) -> ResourceCapacityParams
ResourceCapacityParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ResourceCapacityParamsCollection.ToXMLString() -> String
ResourceCapacityWithFilterParams.Code : String [R/W]
ResourceCapacityWithFilterParams.Date : Date [R/W]
ResourceCapacityWithFilterParams.Type : ResourceCapacityTypeEnum [R/W]
ResourceCapacityWithFilterParams.Warehouse : String [R/W]
ResourceCapacityWithFilterParams.FromXMLFile(ByVal bstrFileName As String)
ResourceCapacityWithFilterParams.FromXMLString(ByVal bstrXML As String)
ResourceCapacityWithFilterParams.GetXMLSchema() -> String
ResourceCapacityWithFilterParams.ToXMLFile(ByVal bstrFileName As String)
ResourceCapacityWithFilterParams.ToXMLString() -> String
ResourceDailyCapacities.Count : Long [R]
ResourceDailyCapacities.Add() -> ResourceDailyCapacity
ResourceDailyCapacities.GetXMLSchema() -> String
ResourceDailyCapacities.Item(ByVal vtIndex As Variant) -> ResourceDailyCapacity
ResourceDailyCapacities.Remove(ByVal vtIndex As Variant)
ResourceDailyCapacities.ToXMLFile(ByVal bstrFileName As String)
ResourceDailyCapacities.ToXMLString() -> String
ResourceDailyCapacity.Code : String [R]
ResourceDailyCapacity.Factor1 : Double [R/W]
ResourceDailyCapacity.Factor2 : Double [R/W]
ResourceDailyCapacity.Factor3 : Double [R/W]
ResourceDailyCapacity.Factor4 : Double [R/W]
ResourceDailyCapacity.Remarks : String [R/W]
ResourceDailyCapacity.SingleRun : Double [R/W]
ResourceDailyCapacity.Total : Double [R/W]
ResourceDailyCapacity.Weekday : ResourceDailyCapacityWeekdayEnum [R/W]
ResourceDailyCapacity.FromXMLFile(ByVal bstrFileName As String)
ResourceDailyCapacity.FromXMLString(ByVal bstrXML As String)
ResourceDailyCapacity.GetXMLSchema() -> String
ResourceDailyCapacity.ToXMLFile(ByVal bstrFileName As String)
ResourceDailyCapacity.ToXMLString() -> String
ResourceEmployee.Code : String [R]
ResourceEmployee.Employee : Long [R/W]
ResourceEmployee.FromXMLFile(ByVal bstrFileName As String)
ResourceEmployee.FromXMLString(ByVal bstrXML As String)
ResourceEmployee.GetXMLSchema() -> String
ResourceEmployee.ToXMLFile(ByVal bstrFileName As String)
ResourceEmployee.ToXMLString() -> String
ResourceEmployees.Count : Long [R]
ResourceEmployees.Add() -> ResourceEmployee
ResourceEmployees.GetXMLSchema() -> String
ResourceEmployees.Item(ByVal vtIndex As Variant) -> ResourceEmployee
ResourceEmployees.Remove(ByVal vtIndex As Variant)
ResourceEmployees.ToXMLFile(ByVal bstrFileName As String)
ResourceEmployees.ToXMLString() -> String
ResourceFixedAsset.Code : String [R]
ResourceFixedAsset.ItemCode : String [R/W]
ResourceFixedAsset.FromXMLFile(ByVal bstrFileName As String)
ResourceFixedAsset.FromXMLString(ByVal bstrXML As String)
ResourceFixedAsset.GetXMLSchema() -> String
ResourceFixedAsset.ToXMLFile(ByVal bstrFileName As String)
ResourceFixedAsset.ToXMLString() -> String
ResourceFixedAssets.Count : Long [R]
ResourceFixedAssets.Add() -> ResourceFixedAsset
ResourceFixedAssets.GetXMLSchema() -> String
ResourceFixedAssets.Item(ByVal vtIndex As Variant) -> ResourceFixedAsset
ResourceFixedAssets.Remove(ByVal vtIndex As Variant)
ResourceFixedAssets.ToXMLFile(ByVal bstrFileName As String)
ResourceFixedAssets.ToXMLString() -> String
ResourceGroup.Code : Long [R]
ResourceGroup.Cost1 : Double [R/W]
ResourceGroup.Cost10 : Double [R/W]
ResourceGroup.Cost2 : Double [R/W]
ResourceGroup.Cost3 : Double [R/W]
ResourceGroup.Cost4 : Double [R/W]
ResourceGroup.Cost5 : Double [R/W]
ResourceGroup.Cost6 : Double [R/W]
ResourceGroup.Cost7 : Double [R/W]
ResourceGroup.Cost8 : Double [R/W]
ResourceGroup.Cost9 : Double [R/W]
ResourceGroup.CostName1 : String [R/W]
ResourceGroup.CostName10 : String [R/W]
ResourceGroup.CostName2 : String [R/W]
ResourceGroup.CostName3 : String [R/W]
ResourceGroup.CostName4 : String [R/W]
ResourceGroup.CostName5 : String [R/W]
ResourceGroup.CostName6 : String [R/W]
ResourceGroup.CostName7 : String [R/W]
ResourceGroup.CostName8 : String [R/W]
ResourceGroup.CostName9 : String [R/W]
ResourceGroup.Name : String [R/W]
ResourceGroup.NumOfUnitsText : String [R/W]
ResourceGroup.Type : ResourceTypeEnum [R/W]
ResourceGroup.FromXMLFile(ByVal bstrFileName As String)
ResourceGroup.FromXMLString(ByVal bstrXML As String)
ResourceGroup.GetXMLSchema() -> String
ResourceGroup.ToXMLFile(ByVal bstrFileName As String)
ResourceGroup.ToXMLString() -> String
ResourceGroupParams.Code : Long [R/W]
ResourceGroupParams.Name : String [R]
ResourceGroupParams.FromXMLFile(ByVal bstrFileName As String)
ResourceGroupParams.FromXMLString(ByVal bstrXML As String)
ResourceGroupParams.GetXMLSchema() -> String
ResourceGroupParams.ToXMLFile(ByVal bstrFileName As String)
ResourceGroupParams.ToXMLString() -> String
ResourceGroupParamsCollection.Count : Long [R]
ResourceGroupParamsCollection.Add() -> ResourceGroupParams
ResourceGroupParamsCollection.GetXMLSchema() -> String
ResourceGroupParamsCollection.Item(ByVal vtIndex As Variant) -> ResourceGroupParams
ResourceGroupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ResourceGroupParamsCollection.ToXMLString() -> String
ResourceGroupsService.Add(ByVal pIResourceGroup As ResourceGroup) -> ResourceGroupParams
ResourceGroupsService.Delete(ByVal pIResourceGroupParams As ResourceGroupParams)
ResourceGroupsService.Get(ByVal pIResourceGroupParams As ResourceGroupParams) -> ResourceGroup
ResourceGroupsService.GetDataInterface(ByVal enumMSDI As ResourceGroupsServiceDataInterfaces) -> Object
ResourceGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ResourceGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ResourceGroupsService.GetList() -> ResourceGroupParamsCollection
ResourceGroupsService.Update(ByVal pIResourceGroup As ResourceGroup)
ResourceParams.Code : String [R/W]
ResourceParams.FromXMLFile(ByVal bstrFileName As String)
ResourceParams.FromXMLString(ByVal bstrXML As String)
ResourceParams.GetXMLSchema() -> String
ResourceParams.ToXMLFile(ByVal bstrFileName As String)
ResourceParams.ToXMLString() -> String
ResourceParamsCollection.Count : Long [R]
ResourceParamsCollection.Add() -> ResourceParams
ResourceParamsCollection.GetXMLSchema() -> String
ResourceParamsCollection.Item(ByVal vtIndex As Variant) -> ResourceParams
ResourceParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ResourceParamsCollection.ToXMLString() -> String
ResourcePropertiesService.Get(ByVal pIResourcePropertyParams As ResourcePropertyParams) -> ResourceProperty
ResourcePropertiesService.GetDataInterface(ByVal enumMSDI As ResourcePropertiesServiceDataInterfaces) -> Object
ResourcePropertiesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ResourcePropertiesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ResourcePropertiesService.GetList() -> ResourcePropertyParamsCollection
ResourcePropertiesService.Update(ByVal pIResourceProperty As ResourceProperty)
ResourceProperty.Code : Long [R]
ResourceProperty.Name : String [R/W]
ResourceProperty.FromXMLFile(ByVal bstrFileName As String)
ResourceProperty.FromXMLString(ByVal bstrXML As String)
ResourceProperty.GetXMLSchema() -> String
ResourceProperty.ToXMLFile(ByVal bstrFileName As String)
ResourceProperty.ToXMLString() -> String
ResourcePropertyParams.Code : Long [R/W]
ResourcePropertyParams.Name : String [R]
ResourcePropertyParams.FromXMLFile(ByVal bstrFileName As String)
ResourcePropertyParams.FromXMLString(ByVal bstrXML As String)
ResourcePropertyParams.GetXMLSchema() -> String
ResourcePropertyParams.ToXMLFile(ByVal bstrFileName As String)
ResourcePropertyParams.ToXMLString() -> String
ResourcePropertyParamsCollection.Count : Long [R]
ResourcePropertyParamsCollection.Add() -> ResourcePropertyParams
ResourcePropertyParamsCollection.GetXMLSchema() -> String
ResourcePropertyParamsCollection.Item(ByVal vtIndex As Variant) -> ResourcePropertyParams
ResourcePropertyParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ResourcePropertyParamsCollection.ToXMLString() -> String
ResourcesService.Add(ByVal pIResource As Resource) -> ResourceParams
ResourcesService.CreateLinkedItem(ByVal pIResourceParams As ResourceParams)
ResourcesService.Delete(ByVal pIResourceParams As ResourceParams)
ResourcesService.Get(ByVal pIResourceParams As ResourceParams) -> Resource
ResourcesService.GetDataInterface(ByVal enumMSDI As ResourcesServiceDataInterfaces) -> Object
ResourcesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ResourcesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ResourcesService.GetList() -> ResourceParamsCollection
ResourcesService.Update(ByVal pIResource As Resource)
ResourceWarehouse.Code : String [R]
ResourceWarehouse.Locked : BoYesNoEnum [R/W]
ResourceWarehouse.UserFields : Fields [R]
ResourceWarehouse.Warehouse : String [R/W]
ResourceWarehouse.FromXMLFile(ByVal bstrFileName As String)
ResourceWarehouse.FromXMLString(ByVal bstrXML As String)
ResourceWarehouse.GetXMLSchema() -> String
ResourceWarehouse.ToXMLFile(ByVal bstrFileName As String)
ResourceWarehouse.ToXMLString() -> String
ResourceWarehouses.Count : Long [R]
ResourceWarehouses.Add() -> ResourceWarehouse
ResourceWarehouses.GetXMLSchema() -> String
ResourceWarehouses.Item(ByVal vtIndex As Variant) -> ResourceWarehouse
ResourceWarehouses.Remove(ByVal vtIndex As Variant)
ResourceWarehouses.ToXMLFile(ByVal bstrFileName As String)
ResourceWarehouses.ToXMLString() -> String
RetornoCode.AbsEntry : Long [R]
RetornoCode.BankCode : String [R/W]
RetornoCode.BOEStatus : BoBoeStatus [R/W]
RetornoCode.Color : Long [R/W]
RetornoCode.Description : String [R/W]
RetornoCode.FileFormat : String [R/W]
RetornoCode.MovementCode : Long [R/W]
RetornoCode.OccurenceCode : Long [R/W]
RetornoCode.FromXMLFile(ByVal bstrFileName As String)
RetornoCode.FromXMLString(ByVal bstrXML As String)
RetornoCode.GetXMLSchema() -> String
RetornoCode.ToXMLFile(ByVal bstrFileName As String)
RetornoCode.ToXMLString() -> String
RetornoCodeParams.AbsEntry : Long [R/W]
RetornoCodeParams.BankCode : String [R]
RetornoCodeParams.BOEStatus : BoBoeStatus [R]
RetornoCodeParams.Color : Long [R]
RetornoCodeParams.Description : String [R]
RetornoCodeParams.FileFormat : String [R]
RetornoCodeParams.MovementCode : Long [R]
RetornoCodeParams.OccurenceCode : Long [R]
RetornoCodeParams.FromXMLFile(ByVal bstrFileName As String)
RetornoCodeParams.FromXMLString(ByVal bstrXML As String)
RetornoCodeParams.GetXMLSchema() -> String
RetornoCodeParams.ToXMLFile(ByVal bstrFileName As String)
RetornoCodeParams.ToXMLString() -> String
RetornoCodeParamsCollection.Count : Long [R]
RetornoCodeParamsCollection.Add() -> RetornoCodeParams
RetornoCodeParamsCollection.GetXMLSchema() -> String
RetornoCodeParamsCollection.Item(ByVal vtIndex As Variant) -> RetornoCodeParams
RetornoCodeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
RetornoCodeParamsCollection.ToXMLString() -> String
RetornoCodesService.Add(ByVal pIRetornoCode As RetornoCode) -> RetornoCodeParams
RetornoCodesService.Delete(ByVal pIRetornoCodeParams As RetornoCodeParams)
RetornoCodesService.Get(ByVal pIRetornoCodeParams As RetornoCodeParams) -> RetornoCode
RetornoCodesService.GetDataInterface(ByVal enumMSDI As RetornoCodesServiceDataInterfaces) -> Object
RetornoCodesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
RetornoCodesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
RetornoCodesService.GetList() -> RetornoCodeParamsCollection
RetornoCodesService.Update(ByVal pIRetornoCode As RetornoCode)
RoundedData.Value : Double [R]
RoundedData.FromXMLFile(ByVal bstrFileName As String)
RoundedData.FromXMLString(ByVal bstrXML As String)
RoundedData.GetXMLSchema() -> String
RoundedData.ToXMLFile(ByVal bstrFileName As String)
RoundedData.ToXMLString() -> String
RouteStage.Code : String [R/W]
RouteStage.CreationDate : Date [R]
RouteStage.DateOfUpdate : Date [R]
RouteStage.Description : String [R/W]
RouteStage.GenerationTime : Date [R]
RouteStage.InternalNumber : Long [R]
RouteStage.FromXMLFile(ByVal bstrFileName As String)
RouteStage.FromXMLString(ByVal bstrXML As String)
RouteStage.GetXMLSchema() -> String
RouteStage.ToXMLFile(ByVal bstrFileName As String)
RouteStage.ToXMLString() -> String
RouteStageParams.Code : String [R]
RouteStageParams.CreationDate : Date [R]
RouteStageParams.DateOfUpdate : Date [R]
RouteStageParams.Description : String [R]
RouteStageParams.GenerationTime : Date [R]
RouteStageParams.InternalNumber : Long [R/W]
RouteStageParams.FromXMLFile(ByVal bstrFileName As String)
RouteStageParams.FromXMLString(ByVal bstrXML As String)
RouteStageParams.GetXMLSchema() -> String
RouteStageParams.ToXMLFile(ByVal bstrFileName As String)
RouteStageParams.ToXMLString() -> String
RouteStageParamsCollection.Count : Long [R]
RouteStageParamsCollection.Add() -> RouteStageParams
RouteStageParamsCollection.GetXMLSchema() -> String
RouteStageParamsCollection.Item(ByVal vtIndex As Variant) -> RouteStageParams
RouteStageParamsCollection.ToXMLFile(ByVal bstrFileName As String)
RouteStageParamsCollection.ToXMLString() -> String
RouteStagesService.Add(ByVal pIRouteStage As RouteStage) -> RouteStageParams
RouteStagesService.Delete(ByVal pIRouteStageParams As RouteStageParams)
RouteStagesService.Get(ByVal pIRouteStageParams As RouteStageParams) -> RouteStage
RouteStagesService.GetDataInterface(ByVal enumMSDI As RouteStagesServiceDataInterfaces) -> Object
RouteStagesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
RouteStagesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
RouteStagesService.GetList() -> RouteStageParamsCollection
RouteStagesService.Update(ByVal pIRouteStage As RouteStage)
RoutingDateCalculationInput.CalculateFromDate : Date [R/W]
RoutingDateCalculationInput.CalculateUntilDate : Date [R/W]
RoutingDateCalculationInput.CapacitySum : Double [R/W]
RoutingDateCalculationInput.FirstDateProportion : Double [R/W]
RoutingDateCalculationInput.ResourceAlloc : ResourceAllocationEnum [R/W]
RoutingDateCalculationInput.ResourceCode : String [R/W]
RoutingDateCalculationInput.WarehouseCode : String [R/W]
RoutingDateCalculationInput.WORLine : Long [R/W]
RoutingDateCalculationInput.WORObjAbs : Long [R/W]
RoutingDateCalculationInput.FromXMLFile(ByVal bstrFileName As String)
RoutingDateCalculationInput.FromXMLString(ByVal bstrXML As String)
RoutingDateCalculationInput.GetXMLSchema() -> String
RoutingDateCalculationInput.ToXMLFile(ByVal bstrFileName As String)
RoutingDateCalculationInput.ToXMLString() -> String
RoutingDateCalculationOutput.Proportion : Double [R]
RoutingDateCalculationOutput.ResultDate : Date [R]
RoutingDateCalculationOutput.FromXMLFile(ByVal bstrFileName As String)
RoutingDateCalculationOutput.FromXMLString(ByVal bstrXML As String)
RoutingDateCalculationOutput.GetXMLSchema() -> String
RoutingDateCalculationOutput.ToXMLFile(ByVal bstrFileName As String)
RoutingDateCalculationOutput.ToXMLString() -> String
RoutingDateCalculationService.Calculate(ByVal pIRoutingDateCalculationInput As RoutingDateCalculationInput) -> RoutingDateCalculationOutput
RoutingDateCalculationService.GetDataInterface(ByVal enumMSDI As RoutingDateCalculationServiceDataInterfaces) -> Object
RoutingDateCalculationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
RoutingDateCalculationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SalesAppSetting.AdvancedDashBoard : Long [R/W]
SalesAppSetting.Code : Long [R]
SalesAppSetting.CustomerAdvancedDashBoard : Long [R/W]
SalesAppSetting.Name : String [R/W]
SalesAppSetting.FromXMLFile(ByVal bstrFileName As String)
SalesAppSetting.FromXMLString(ByVal bstrXML As String)
SalesAppSetting.GetXMLSchema() -> String
SalesAppSetting.ToXMLFile(ByVal bstrFileName As String)
SalesAppSetting.ToXMLString() -> String
SalesAppSettingParams.Code : Long [R/W]
SalesAppSettingParams.Name : String [R/W]
SalesAppSettingParams.FromXMLFile(ByVal bstrFileName As String)
SalesAppSettingParams.FromXMLString(ByVal bstrXML As String)
SalesAppSettingParams.GetXMLSchema() -> String
SalesAppSettingParams.ToXMLFile(ByVal bstrFileName As String)
SalesAppSettingParams.ToXMLString() -> String
SalesForecast.Browser : DataBrowser [R]
SalesForecast.ForecastCode : String [R/W]
SalesForecast.ForecastEndDate : Date [R/W]
SalesForecast.ForecastName : String [R/W]
SalesForecast.ForecastStartDate : Date [R/W]
SalesForecast.Lines : SalesForecast_Lines [R]
SalesForecast.Numerator : Long [R]
SalesForecast.UserFields : UserFields [R]
SalesForecast.View : ForecastViewTypeEnum [R/W]
SalesForecast.Add() -> Long
SalesForecast.GetAsXML() -> String
SalesForecast.GetByKey(ByVal lID As Long) -> Boolean
SalesForecast.Remove() -> Long
SalesForecast.SaveToFile(ByVal FileName As String)
SalesForecast.SaveXML(ByRef FileName As String)
SalesForecast.Update() -> Long
SalesForecast_Lines.Count : Long [R]
SalesForecast_Lines.ForecastedDay : Date [R/W]
SalesForecast_Lines.ItemNo : String [R/W]
SalesForecast_Lines.Quantity : Double [R/W]
SalesForecast_Lines.UserFields : UserFields [R]
SalesForecast_Lines.Warehouse : String [R/W]
SalesForecast_Lines.Add()
SalesForecast_Lines.Delete()
SalesForecast_Lines.SetCurrentLine(ByVal LineNum As Long)
SalesOpportunities.AttachmentEntry : Long [R/W]
SalesOpportunities.BPChanelCode : String [R/W]
SalesOpportunities.BPChanelName : String [R/W]
SalesOpportunities.BPChannelContact : Long [R/W]
SalesOpportunities.Browser : DataBrowser [R]
SalesOpportunities.CardCode : String [R/W]
SalesOpportunities.ClosingDate : Date [R/W]
SalesOpportunities.ClosingGrossProfitLocal : Double [R]
SalesOpportunities.ClosingGrossProfitSystem : Double [R]
SalesOpportunities.ClosingPercentage : Double [R]
SalesOpportunities.ClosingType : BoSoClosedInTypes [R/W]
SalesOpportunities.Competition : SalesOpportunitiesCompetition [R]
SalesOpportunities.ContactPerson : Long [R/W]
SalesOpportunities.CurrentStageNo : Double [R]
SalesOpportunities.CurrentStageNumber : Long [R]
SalesOpportunities.CustomerName : String [R/W]
SalesOpportunities.DataOwnershipfield : Long [R/W]
SalesOpportunities.DocumentCheckbox : String [R]
SalesOpportunities.GrossProfit : Double [R/W]
SalesOpportunities.GrossProfitTotalLocal : Double [R/W]
SalesOpportunities.GrossProfitTotalSystem : Double [R]
SalesOpportunities.Industry : Long [R/W]
SalesOpportunities.InterestField1 : Long [R/W]
SalesOpportunities.InterestField2 : Long [R/W]
SalesOpportunities.InterestField3 : Long [R/W]
SalesOpportunities.InterestLevel : Long [R/W]
SalesOpportunities.Interests : SalesOpportunitiesInterests [R]
SalesOpportunities.Lines : SalesOpportunitiesLines [R]
SalesOpportunities.LinkedDocumentNumber : String [R]
SalesOpportunities.LinkedDocumentType : Long [R]
SalesOpportunities.MaxLocalTotal : Double [R]
SalesOpportunities.MaxSystemTotal : Double [R]
SalesOpportunities.OpportunityName : String [R/W]
SalesOpportunities.OpportunityType : OpportunityTypeEnum [R/W]
SalesOpportunities.Partners : SalesOpportunitiesPartners [R]
SalesOpportunities.PredictedClosingDate : Date [R/W]
SalesOpportunities.ProjectCode : String [R/W]
SalesOpportunities.ReasonForClosing : Long [R/W]
SalesOpportunities.Reasons : SalesOpportunitiesReasons [R]
SalesOpportunities.Remarks : String [R/W]
SalesOpportunities.SalesPerson : Long [R/W]
SalesOpportunities.SequentialNo : Long [R]
SalesOpportunities.Source : Long [R/W]
SalesOpportunities.StartDate : Date [R/W]
SalesOpportunities.Status : BoSoOsStatus [R/W]
SalesOpportunities.StatusRemarks : String [R/W]
SalesOpportunities.Territory : Long [R/W]
SalesOpportunities.TotalAmounSystem : Double [R]
SalesOpportunities.TotalAmountLocal : Double [R/W]
SalesOpportunities.UpdateDate : Date [R]
SalesOpportunities.UpdateTime : Date [R]
SalesOpportunities.UserFields : UserFields [R]
SalesOpportunities.UserSignature : Long [R]
SalesOpportunities.WeightedSumLC : Double [R]
SalesOpportunities.WeightedSumSC : Double [R]
SalesOpportunities.Add() -> Long
SalesOpportunities.Close() -> Long
SalesOpportunities.GetAsXML() -> String
SalesOpportunities.GetByKey(ByVal OpprId As Long) -> Boolean
SalesOpportunities.Remove() -> Long
SalesOpportunities.SaveToFile(ByVal FileName As String)
SalesOpportunities.SaveXML(ByRef FileName As String)
SalesOpportunities.Update() -> Long
SalesOpportunitiesCompetition.Competition : Long [R/W]
SalesOpportunitiesCompetition.Count : Long [R]
SalesOpportunitiesCompetition.Details : String [R/W]
SalesOpportunitiesCompetition.RowNo : Long [R]
SalesOpportunitiesCompetition.SequenceNo : Long [R]
SalesOpportunitiesCompetition.ThreatLevel : ThreatLevelEnum [R/W]
SalesOpportunitiesCompetition.UserFields : UserFields [R]
SalesOpportunitiesCompetition.WonOrLost : String [R/W]
SalesOpportunitiesCompetition.Add()
SalesOpportunitiesCompetition.Delete()
SalesOpportunitiesCompetition.SetCurrentLine(ByVal LineNum As Long)
SalesOpportunitiesInterests.Count : Long [R]
SalesOpportunitiesInterests.InterestId : Long [R/W]
SalesOpportunitiesInterests.PrimaryInterest : BoYesNoEnum [R/W]
SalesOpportunitiesInterests.RowNo : Long [R]
SalesOpportunitiesInterests.SequenceNo : Long [R]
SalesOpportunitiesInterests.UserFields : UserFields [R]
SalesOpportunitiesInterests.Add()
SalesOpportunitiesInterests.Delete()
SalesOpportunitiesInterests.SetCurrentLine(ByVal LineNum As Long)
SalesOpportunitiesLines.BPChanelCode : String [R/W]
SalesOpportunitiesLines.BPChanelName : String [R/W]
SalesOpportunitiesLines.BPChannelContact : Long [R/W]
SalesOpportunitiesLines.ClosingDate : Date [R/W]
SalesOpportunitiesLines.Contact : BoYesNoEnum [R]
SalesOpportunitiesLines.ContactPerson : Long [R/W]
SalesOpportunitiesLines.Count : Long [R]
SalesOpportunitiesLines.DataOwnershipfield : Long [R/W]
SalesOpportunitiesLines.DocumentCheckbox : BoYesNoEnum [R/W]
SalesOpportunitiesLines.DocumentNumber : Long [R/W]
SalesOpportunitiesLines.DocumentType : BoAPARDocumentTypes [R/W]
SalesOpportunitiesLines.LineNum : Long [R]
SalesOpportunitiesLines.MaxLocalTotal : Double [R/W]
SalesOpportunitiesLines.MaxSystemTotal : Double [R]
SalesOpportunitiesLines.PercentageRate : Double [R/W]
SalesOpportunitiesLines.Remarks : String [R/W]
SalesOpportunitiesLines.SalesPerson : Long [R/W]
SalesOpportunitiesLines.SequenceNo : Long [R]
SalesOpportunitiesLines.StageKey : Long [R/W]
SalesOpportunitiesLines.StartDate : Date [R/W]
SalesOpportunitiesLines.Status : BoSoStatus [R]
SalesOpportunitiesLines.UserFields : UserFields [R]
SalesOpportunitiesLines.WeightedAmountLocal : Double [R]
SalesOpportunitiesLines.WeightedAmountSystem : Double [R]
SalesOpportunitiesLines.Add()
SalesOpportunitiesLines.SetCurrentLine(ByVal LineNum As Long)
SalesOpportunitiesPartners.Count : Long [R]
SalesOpportunitiesPartners.Details : String [R/W]
SalesOpportunitiesPartners.Partners : Long [R/W]
SalesOpportunitiesPartners.RelationshipCode : Long [R/W]
SalesOpportunitiesPartners.RowNo : Long [R]
SalesOpportunitiesPartners.SequenceNo : Long [R]
SalesOpportunitiesPartners.UserFields : UserFields [R]
SalesOpportunitiesPartners.Add()
SalesOpportunitiesPartners.Delete()
SalesOpportunitiesPartners.SetCurrentLine(ByVal LineNum As Long)
SalesOpportunitiesReasons.Count : Long [R]
SalesOpportunitiesReasons.Reason : Long [R/W]
SalesOpportunitiesReasons.RowNo : Long [R]
SalesOpportunitiesReasons.SequenceNo : Long [R]
SalesOpportunitiesReasons.UserFields : UserFields [R]
SalesOpportunitiesReasons.Add()
SalesOpportunitiesReasons.Delete()
SalesOpportunitiesReasons.SetCurrentLine(ByVal LineNum As Long)
SalesOpportunityCompetitorSetup.Details : String [R/W]
SalesOpportunityCompetitorSetup.Name : String [R/W]
SalesOpportunityCompetitorSetup.SequenceNo : Long [R]
SalesOpportunityCompetitorSetup.ThreatLevel : ThreatLevelEnum [R/W]
SalesOpportunityCompetitorSetup.FromXMLFile(ByVal bstrFileName As String)
SalesOpportunityCompetitorSetup.FromXMLString(ByVal bstrXML As String)
SalesOpportunityCompetitorSetup.GetXMLSchema() -> String
SalesOpportunityCompetitorSetup.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityCompetitorSetup.ToXMLString() -> String
SalesOpportunityCompetitorSetupParams.Name : String [R]
SalesOpportunityCompetitorSetupParams.SequenceNo : Long [R/W]
SalesOpportunityCompetitorSetupParams.ThreatLevel : ThreatLevelEnum [R]
SalesOpportunityCompetitorSetupParams.FromXMLFile(ByVal bstrFileName As String)
SalesOpportunityCompetitorSetupParams.FromXMLString(ByVal bstrXML As String)
SalesOpportunityCompetitorSetupParams.GetXMLSchema() -> String
SalesOpportunityCompetitorSetupParams.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityCompetitorSetupParams.ToXMLString() -> String
SalesOpportunityCompetitorSetupParamsCollection.Count : Long [R]
SalesOpportunityCompetitorSetupParamsCollection.Add() -> SalesOpportunityCompetitorSetupParams
SalesOpportunityCompetitorSetupParamsCollection.GetXMLSchema() -> String
SalesOpportunityCompetitorSetupParamsCollection.Item(ByVal vtIndex As Variant) -> SalesOpportunityCompetitorSetupParams
SalesOpportunityCompetitorSetupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityCompetitorSetupParamsCollection.ToXMLString() -> String
SalesOpportunityCompetitorsSetupService.AddSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetup As SalesOpportunityCompetitorSetup) -> SalesOpportunityCompetitorSetupParams
SalesOpportunityCompetitorsSetupService.DeleteSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetupParams As SalesOpportunityCompetitorSetupParams)
SalesOpportunityCompetitorsSetupService.GetDataInterface(ByVal enumMSDI As SalesOpportunityCompetitorsSetupServiceDataInterfaces) -> Object
SalesOpportunityCompetitorsSetupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SalesOpportunityCompetitorsSetupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SalesOpportunityCompetitorsSetupService.GetSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetupParams As SalesOpportunityCompetitorSetupParams) -> SalesOpportunityCompetitorSetup
SalesOpportunityCompetitorsSetupService.GetSalesOpportunityCompetitorSetupList() -> SalesOpportunityCompetitorSetupParamsCollection
SalesOpportunityCompetitorsSetupService.UpdateSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetup As SalesOpportunityCompetitorSetup)
SalesOpportunityInterestSetup.Description : String [R/W]
SalesOpportunityInterestSetup.SequenceNo : Long [R]
SalesOpportunityInterestSetup.Sort : Long [R/W]
SalesOpportunityInterestSetup.FromXMLFile(ByVal bstrFileName As String)
SalesOpportunityInterestSetup.FromXMLString(ByVal bstrXML As String)
SalesOpportunityInterestSetup.GetXMLSchema() -> String
SalesOpportunityInterestSetup.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityInterestSetup.ToXMLString() -> String
SalesOpportunityInterestSetupParams.Description : String [R]
SalesOpportunityInterestSetupParams.SequenceNo : Long [R/W]
SalesOpportunityInterestSetupParams.FromXMLFile(ByVal bstrFileName As String)
SalesOpportunityInterestSetupParams.FromXMLString(ByVal bstrXML As String)
SalesOpportunityInterestSetupParams.GetXMLSchema() -> String
SalesOpportunityInterestSetupParams.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityInterestSetupParams.ToXMLString() -> String
SalesOpportunityInterestSetupParamsCollection.Count : Long [R]
SalesOpportunityInterestSetupParamsCollection.Add() -> SalesOpportunityInterestSetupParams
SalesOpportunityInterestSetupParamsCollection.GetXMLSchema() -> String
SalesOpportunityInterestSetupParamsCollection.Item(ByVal vtIndex As Variant) -> SalesOpportunityInterestSetupParams
SalesOpportunityInterestSetupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityInterestSetupParamsCollection.ToXMLString() -> String
SalesOpportunityInterestsSetupService.AddSalesOpportunityInterestSetup(ByVal pISalesOpportunityInterestSetup As SalesOpportunityInterestSetup) -> SalesOpportunityInterestSetupParams
SalesOpportunityInterestsSetupService.DeleteSalesOpportunityInterestSetup(ByVal pISalesOpportunityInterestSetupParams As SalesOpportunityInterestSetupParams)
SalesOpportunityInterestsSetupService.GetDataInterface(ByVal enumMSDI As SalesOpportunityInterestsSetupServiceDataInterfaces) -> Object
SalesOpportunityInterestsSetupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SalesOpportunityInterestsSetupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SalesOpportunityInterestsSetupService.GetSalesOpportunityInterestSetup(ByVal pISalesOpportunityInterestSetupParams As SalesOpportunityInterestSetupParams) -> SalesOpportunityInterestSetup
SalesOpportunityInterestsSetupService.GetSalesOpportunityInterestSetupList() -> SalesOpportunityInterestSetupParamsCollection
SalesOpportunityInterestsSetupService.UpdateSalesOpportunityInterestSetup(ByVal pISalesOpportunityInterestSetup As SalesOpportunityInterestSetup)
SalesOpportunityReasonSetup.Description : String [R/W]
SalesOpportunityReasonSetup.SequenceNo : Long [R]
SalesOpportunityReasonSetup.Sort : Long [R/W]
SalesOpportunityReasonSetup.FromXMLFile(ByVal bstrFileName As String)
SalesOpportunityReasonSetup.FromXMLString(ByVal bstrXML As String)
SalesOpportunityReasonSetup.GetXMLSchema() -> String
SalesOpportunityReasonSetup.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityReasonSetup.ToXMLString() -> String
SalesOpportunityReasonSetupParams.Description : String [R]
SalesOpportunityReasonSetupParams.SequenceNo : Long [R/W]
SalesOpportunityReasonSetupParams.FromXMLFile(ByVal bstrFileName As String)
SalesOpportunityReasonSetupParams.FromXMLString(ByVal bstrXML As String)
SalesOpportunityReasonSetupParams.GetXMLSchema() -> String
SalesOpportunityReasonSetupParams.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityReasonSetupParams.ToXMLString() -> String
SalesOpportunityReasonSetupParamsCollection.Count : Long [R]
SalesOpportunityReasonSetupParamsCollection.Add() -> SalesOpportunityReasonSetupParams
SalesOpportunityReasonSetupParamsCollection.GetXMLSchema() -> String
SalesOpportunityReasonSetupParamsCollection.Item(ByVal vtIndex As Variant) -> SalesOpportunityReasonSetupParams
SalesOpportunityReasonSetupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunityReasonSetupParamsCollection.ToXMLString() -> String
SalesOpportunityReasonsSetupService.AddSalesOpportunityReasonSetup(ByVal pISalesOpportunityReasonSetup As SalesOpportunityReasonSetup) -> SalesOpportunityReasonSetupParams
SalesOpportunityReasonsSetupService.DeleteSalesOpportunityReasonSetup(ByVal pISalesOpportunityReasonSetupParams As SalesOpportunityReasonSetupParams)
SalesOpportunityReasonsSetupService.GetDataInterface(ByVal enumMSDI As SalesOpportunityReasonsSetupServiceDataInterfaces) -> Object
SalesOpportunityReasonsSetupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SalesOpportunityReasonsSetupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SalesOpportunityReasonsSetupService.GetSalesOpportunityReasonSetup(ByVal pISalesOpportunityReasonSetupParams As SalesOpportunityReasonSetupParams) -> SalesOpportunityReasonSetup
SalesOpportunityReasonsSetupService.GetSalesOpportunityReasonSetupList() -> SalesOpportunityReasonSetupParamsCollection
SalesOpportunityReasonsSetupService.UpdateSalesOpportunityReasonSetup(ByVal pISalesOpportunityReasonSetup As SalesOpportunityReasonSetup)
SalesOpportunitySourceSetup.Description : String [R/W]
SalesOpportunitySourceSetup.SequenceNo : Long [R]
SalesOpportunitySourceSetup.Sort : Long [R/W]
SalesOpportunitySourceSetup.FromXMLFile(ByVal bstrFileName As String)
SalesOpportunitySourceSetup.FromXMLString(ByVal bstrXML As String)
SalesOpportunitySourceSetup.GetXMLSchema() -> String
SalesOpportunitySourceSetup.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunitySourceSetup.ToXMLString() -> String
SalesOpportunitySourceSetupParams.Description : String [R]
SalesOpportunitySourceSetupParams.SequenceNo : Long [R/W]
SalesOpportunitySourceSetupParams.FromXMLFile(ByVal bstrFileName As String)
SalesOpportunitySourceSetupParams.FromXMLString(ByVal bstrXML As String)
SalesOpportunitySourceSetupParams.GetXMLSchema() -> String
SalesOpportunitySourceSetupParams.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunitySourceSetupParams.ToXMLString() -> String
SalesOpportunitySourceSetupParamsCollection.Count : Long [R]
SalesOpportunitySourceSetupParamsCollection.Add() -> SalesOpportunitySourceSetupParams
SalesOpportunitySourceSetupParamsCollection.GetXMLSchema() -> String
SalesOpportunitySourceSetupParamsCollection.Item(ByVal vtIndex As Variant) -> SalesOpportunitySourceSetupParams
SalesOpportunitySourceSetupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
SalesOpportunitySourceSetupParamsCollection.ToXMLString() -> String
SalesOpportunitySourcesSetupService.AddSalesOpportunitySourceSetup(ByVal pISalesOpportunitySourceSetup As SalesOpportunitySourceSetup) -> SalesOpportunitySourceSetupParams
SalesOpportunitySourcesSetupService.DeleteSalesOpportunitySourceSetup(ByVal pISalesOpportunitySourceSetupParams As SalesOpportunitySourceSetupParams)
SalesOpportunitySourcesSetupService.GetDataInterface(ByVal enumMSDI As SalesOpportunitySourcesSetupServiceDataInterfaces) -> Object
SalesOpportunitySourcesSetupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SalesOpportunitySourcesSetupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SalesOpportunitySourcesSetupService.GetSalesOpportunitySourceSetup(ByVal pISalesOpportunitySourceSetupParams As SalesOpportunitySourceSetupParams) -> SalesOpportunitySourceSetup
SalesOpportunitySourcesSetupService.GetSalesOpportunitySourceSetupList() -> SalesOpportunitySourceSetupParamsCollection
SalesOpportunitySourcesSetupService.UpdateSalesOpportunitySourceSetup(ByVal pISalesOpportunitySourceSetup As SalesOpportunitySourceSetup)
SalesPersons.Active : BoYesNoEnum [R/W]
SalesPersons.Browser : DataBrowser [R]
SalesPersons.CommissionForSalesEmployee : Double [R/W]
SalesPersons.CommissionGroup : Long [R/W]
SalesPersons.eMail : String [R/W]
SalesPersons.EmployeeID : Long [R]
SalesPersons.Fax : String [R/W]
SalesPersons.Locked : BoYesNoEnum [R]
SalesPersons.Mobile : String [R/W]
SalesPersons.Remarks : String [R/W]
SalesPersons.SalesEmployeeCode : Long [R]
SalesPersons.SalesEmployeeName : String [R/W]
SalesPersons.Telephone : String [R/W]
SalesPersons.UserFields : UserFields [R]
SalesPersons.Add() -> Long
SalesPersons.GetAsXML() -> String
SalesPersons.GetByKey(ByVal lSlpCode As Long) -> Boolean
SalesPersons.Remove() -> Long
SalesPersons.SaveToFile(ByVal bstrFileName As String)
SalesPersons.SaveXML(ByRef pbstrFileName As String)
SalesPersons.Update() -> Long
SalesStages.Browser : DataBrowser [R]
SalesStages.Cancelled : BoYesNoEnum [R/W]
SalesStages.ClosingPercentage : Double [R/W]
SalesStages.IsPurchasing : BoYesNoEnum [R/W]
SalesStages.IsSales : BoYesNoEnum [R/W]
SalesStages.Name : String [R/W]
SalesStages.SequenceNo : Long [R]
SalesStages.Stageno : Long [R/W]
SalesStages.UserFields : UserFields [R]
SalesStages.Add() -> Long
SalesStages.GetAsXML() -> String
SalesStages.GetByKey(ByVal lNum As Long) -> Boolean
SalesStages.SaveToFile(ByVal bstrFileName As String)
SalesStages.SaveXML(ByRef pbstrFileName As String)
SalesStages.Update() -> Long
SalesTaxAuthorities.AOrPTaxAccount : String [R/W]
SalesTaxAuthorities.AOrRTaxAccount : String [R/W]
SalesTaxAuthorities.APExpAccount : String [R/W]
SalesTaxAuthorities.ARExpAccount : String [R/W]
SalesTaxAuthorities.Browser : DataBrowser [R]
SalesTaxAuthorities.Code : String [R/W]
SalesTaxAuthorities.DeferredTaxAccount : String [R/W]
SalesTaxAuthorities.Exempt : BoYesNoEnum [R/W]
SalesTaxAuthorities.FlatTaxAmount : Double [R/W]
SalesTaxAuthorities.InclInFirstInstallment : BoYesNoEnum [R/W]
SalesTaxAuthorities.InclInGrossRevenue : BoYesNoEnum [R/W]
SalesTaxAuthorities.InclInPrice : BoYesNoEnum [R/W]
SalesTaxAuthorities.MaxTaxableAmount : Double [R/W]
SalesTaxAuthorities.MinTaxableAmount : Double [R/W]
SalesTaxAuthorities.Name : String [R/W]
SalesTaxAuthorities.NonDeductibleAccount : String [R/W]
SalesTaxAuthorities.NonDeductiblePrecent : Double [R/W]
SalesTaxAuthorities.Rate : Double [R/W]
SalesTaxAuthorities.ReverseChargePercent : Double [R/W]
SalesTaxAuthorities.SalesTaxRCMAccount : String [R/W]
SalesTaxAuthorities.SalesTaxRCMClrAccount : String [R/W]
SalesTaxAuthorities.TaxDefinitions : TaxDefinitions [R]
SalesTaxAuthorities.TextCode : Long [R/W]
SalesTaxAuthorities.Type : Long [R/W]
SalesTaxAuthorities.UserFields : UserFields [R]
SalesTaxAuthorities.UserSignature : Long [R]
SalesTaxAuthorities.UseTaxAccount : String [R/W]
SalesTaxAuthorities.VATExemption : BoYesNoEnum [R/W]
SalesTaxAuthorities.VATExemptionBasePercent : Double [R/W]
SalesTaxAuthorities.VATExemptionPercent : Double [R/W]
SalesTaxAuthorities.Add() -> Long
SalesTaxAuthorities.GetAsXML() -> String
SalesTaxAuthorities.GetByKey(ByVal Code As String, ByVal Type As Long) -> Boolean
SalesTaxAuthorities.SaveToFile(ByVal FileName As String)
SalesTaxAuthorities.SaveXML(ByRef FileName As String)
SalesTaxAuthorities.Update() -> Long
SalesTaxAuthoritiesTypes.Browser : DataBrowser [R]
SalesTaxAuthoritiesTypes.Name : String [R/W]
SalesTaxAuthoritiesTypes.NfTaxId : Long [R/W]
SalesTaxAuthoritiesTypes.Numerator : Long [R]
SalesTaxAuthoritiesTypes.TaxCreditControl : BoYesNoEnum [R/W]
SalesTaxAuthoritiesTypes.TaxParamSetId : Long [R/W]
SalesTaxAuthoritiesTypes.UserFields : UserFields [R]
SalesTaxAuthoritiesTypes.UserSignature : Long [R]
SalesTaxAuthoritiesTypes.VAT : BoYesNoEnum [R/W]
SalesTaxAuthoritiesTypes.Add() -> Long
SalesTaxAuthoritiesTypes.GetAsXML() -> String
SalesTaxAuthoritiesTypes.GetByKey(ByVal Key As Long) -> Boolean
SalesTaxAuthoritiesTypes.SaveToFile(ByVal FileName As String)
SalesTaxAuthoritiesTypes.SaveXML(ByRef FileName As String)
SalesTaxAuthoritiesTypes.Update() -> Long
SalesTaxCodes.Browser : DataBrowser [R]
SalesTaxCodes.CFOPIn : String [R/W]
SalesTaxCodes.CFOPOut : String [R/W]
SalesTaxCodes.Code : String [R/W]
SalesTaxCodes.FADebit : BoYesNoEnum [R/W]
SalesTaxCodes.Freight : BoYesNoEnum [R/W]
SalesTaxCodes.Inactive : BoYesNoEnum [R/W]
SalesTaxCodes.IsItemLevel : BoYesNoEnum [R/W]
SalesTaxCodes.Lines : SalesTaxCodes_Lines [R]
SalesTaxCodes.Name : String [R/W]
SalesTaxCodes.Rate : Double [R]
SalesTaxCodes.TypeFormulaCombId : Long [R/W]
SalesTaxCodes.UserFields : UserFields [R]
SalesTaxCodes.UserSignature : Long [R]
SalesTaxCodes.ValidForAP : BoYesNoEnum [R/W]
SalesTaxCodes.ValidForAR : BoYesNoEnum [R/W]
SalesTaxCodes.VATExemption : BoYesNoEnum [R/W]
SalesTaxCodes.Add() -> Long
SalesTaxCodes.GetAsXML() -> String
SalesTaxCodes.GetByKey(ByVal Key As String) -> Boolean
SalesTaxCodes.SaveToFile(ByVal FileName As String)
SalesTaxCodes.SaveXML(ByRef FileName As String)
SalesTaxCodes.Update() -> Long
SalesTaxCodes_Lines.Count : Long [R]
SalesTaxCodes_Lines.CSTCodeIn : String [R/W]
SalesTaxCodes_Lines.CSTSuffix : String [R/W]
SalesTaxCodes_Lines.EffectiveRate : Double [R]
SalesTaxCodes_Lines.FormulaId : Long [R/W]
SalesTaxCodes_Lines.RowNumber : Long [R]
SalesTaxCodes_Lines.STACode : String [R/W]
SalesTaxCodes_Lines.STATaxonTaxCode : String [R/W]
SalesTaxCodes_Lines.STATaxOnTaxType : Long [R/W]
SalesTaxCodes_Lines.STAType : Long [R/W]
SalesTaxCodes_Lines.STCCode : String [R]
SalesTaxCodes_Lines.UserFields : UserFields [R]
SalesTaxCodes_Lines.Add()
SalesTaxCodes_Lines.SetCurrentLine(ByVal LineNum As Long)
SBObob.ConvertEnumValueToValidValue(ByVal enumName As String, ByVal enumValue As Long) -> String
SBObob.ConvertValidValueToEnumValue(ByVal enumName As String, ByVal ValidValue As String) -> Long
SBObob.Format_DateToString(ByVal inDate As Date) -> Recordset
SBObob.Format_MoneyToString(ByVal inMoney As Double, ByVal inPrecision As BoMoneyPrecisionTypes) -> Recordset
SBObob.Format_StringToDate(ByVal inStr As String) -> Recordset
SBObob.GetAccountSegmentsByCode(ByVal AccountCode As String, ByVal AddSeperator As Boolean) -> Recordset
SBObob.GetBPList(ByVal CardType As BoCardTypes) -> Recordset
SBObob.GetContactEmployees(ByVal CardCode As String) -> Recordset
SBObob.GetCurrencyRate(ByVal Currency As String, ByVal Date As Date) -> Recordset
SBObob.GetDueDate(ByVal CardCode As String, ByVal refDate As Date) -> Recordset
SBObob.GetEwaParameters(ByVal bstrKey As String, ByRef pbstrRsltEwaUserName As String, ByRef pbstrRsltEwaPassword As String)
SBObob.GetFieldValidValues(ByVal TableName As String, ByVal FieldName As String) -> Recordset
SBObob.GetIndexRate(ByVal Index As String, ByVal Date As Date) -> Recordset
SBObob.GetItemList() -> Recordset
SBObob.GetItemPrice(ByVal CardCode As String, ByVal ItemCode As String, ByVal amount As Double, ByVal Date As Date) -> Recordset
SBObob.GetLicenseStatus(ByVal UserName As String, ByVal FormID As String) -> Long
SBObob.GetLocalCurrency() -> Recordset
SBObob.GetObjectKeyBySingleValue(ByVal ObjNum As BoObjectTypes, ByVal PropName As String, ByVal Value As String, ByVal Condition As BoQueryConditions) -> Recordset
SBObob.GetObjectPermission(ByVal Object As BoObjectTypes) -> Recordset
SBObob.GetSystemCurrency() -> Recordset
SBObob.GetSystemPermission(ByVal UserName As String, ByVal PermissionID As String) -> Recordset
SBObob.GetTableFieldList(ByVal TableName As String) -> Recordset
SBObob.GetTableList() -> Recordset
SBObob.GetUserList() -> Recordset
SBObob.GetValidValueDescription(ByVal ObjNum As BoObjectTypes, ByVal ObjectName As String, ByVal PropertyName As String, ByVal enumValue As Long) -> String
SBObob.GetWareHouseList() -> Recordset
SBObob.PutEwaParameters(ByVal bstrKey As String, ByVal bstrEwaUserName As String, ByVal bstrEwaPassword As String)
SBObob.SetCurrencyRate(ByVal Currency As String, ByVal Date As Date, ByVal Value As Double, Optional ByVal Update As Boolean = False)
SBObob.SetSystemPermission(ByVal UserName As String, ByVal PermissionID As String, ByVal Permission As Long)
Section.AbsEntry : Long [R]
Section.Code : String [R/W]
Section.Description : String [R/W]
Section.ECode : String [R/W]
Section.FromXMLFile(ByVal bstrFileName As String)
Section.FromXMLString(ByVal bstrXML As String)
Section.GetXMLSchema() -> String
Section.ToXMLFile(ByVal bstrFileName As String)
Section.ToXMLString() -> String
SectionParams.AbsEntry : Long [R/W]
SectionParams.Code : String [R]
SectionParams.Description : String [R]
SectionParams.FromXMLFile(ByVal bstrFileName As String)
SectionParams.FromXMLString(ByVal bstrXML As String)
SectionParams.GetXMLSchema() -> String
SectionParams.ToXMLFile(ByVal bstrFileName As String)
SectionParams.ToXMLString() -> String
SectionsParams.Count : Long [R]
SectionsParams.Add() -> SectionParams
SectionsParams.GetXMLSchema() -> String
SectionsParams.Item(ByVal vtIndex As Variant) -> SectionParams
SectionsParams.ToXMLFile(ByVal bstrFileName As String)
SectionsParams.ToXMLString() -> String
SectionsService.AddSection(ByVal pISection As Section) -> SectionParams
SectionsService.DeleteSection(ByVal pISectionParams As SectionParams)
SectionsService.GetDataInterface(ByVal enumMSDI As SectionsServiceDataInterfaces) -> Object
SectionsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SectionsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SectionsService.GetSection(ByVal pISectionParams As SectionParams) -> Section
SectionsService.GetSectionList() -> SectionsParams
SectionsService.UpdateSection(ByVal pISection As Section)
SensitiveDataAccess.Key1 : String [R/W]
SensitiveDataAccess.Key2 : String [R/W]
SensitiveDataAccess.Key3 : String [R/W]
SensitiveDataAccess.Key4 : String [R/W]
SensitiveDataAccess.PropertyID : Long [R/W]
SensitiveDataAccess.PropertyName : String [R/W]
SensitiveDataAccess.PropertyValue : String [R/W]
SensitiveDataAccess.Table : String [R/W]
SensitiveDataAccess.FromXMLFile(ByVal bstrFileName As String)
SensitiveDataAccess.FromXMLString(ByVal bstrXML As String)
SensitiveDataAccess.GetXMLSchema() -> String
SensitiveDataAccess.ToXMLFile(ByVal bstrFileName As String)
SensitiveDataAccess.ToXMLString() -> String
SensitiveDataAccessService.Access(ByVal pISensitiveDataAccess As SensitiveDataAccess) -> SensitiveDataAccess
SensitiveDataAccessService.GetDataInterface(ByVal enumMSDI As SensitiveDataAccessServiceDataInterfaces) -> Object
SensitiveDataAccessService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SensitiveDataAccessService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SensitiveDataAccessService.IsDataSensitive(ByVal pISensitiveDataAccess As SensitiveDataAccess) -> DataSensitiveStatus
SerialNumberDetail.AdmissionDate : Date [R/W]
SerialNumberDetail.Details : String [R/W]
SerialNumberDetail.DocEntry : Long [R]
SerialNumberDetail.ExpirationDate : Date [R/W]
SerialNumberDetail.ItemCode : String [R]
SerialNumberDetail.ItemDescription : String [R]
SerialNumberDetail.Location : String [R/W]
SerialNumberDetail.LotNumber : String [R/W]
SerialNumberDetail.ManufacturingDate : Date [R/W]
SerialNumberDetail.MfrSerialNo : String [R/W]
SerialNumberDetail.MFrWarrantyEnd : Date [R/W]
SerialNumberDetail.MfrWarrantyStart : Date [R/W]
SerialNumberDetail.SerialNumber : String [R/W]
SerialNumberDetail.SystemNumber : Long [R]
SerialNumberDetail.UserFields : Fields [R]
SerialNumberDetail.FromXMLFile(ByVal bstrFileName As String)
SerialNumberDetail.FromXMLString(ByVal bstrXML As String)
SerialNumberDetail.GetXMLSchema() -> String
SerialNumberDetail.ToXMLFile(ByVal bstrFileName As String)
SerialNumberDetail.ToXMLString() -> String
SerialNumberDetailParams.DocEntry : Long [R/W]
SerialNumberDetailParams.FromXMLFile(ByVal bstrFileName As String)
SerialNumberDetailParams.FromXMLString(ByVal bstrXML As String)
SerialNumberDetailParams.GetXMLSchema() -> String
SerialNumberDetailParams.ToXMLFile(ByVal bstrFileName As String)
SerialNumberDetailParams.ToXMLString() -> String
SerialNumberDetailsService.Get(ByVal pISerialNumberDetailParams As SerialNumberDetailParams) -> SerialNumberDetail
SerialNumberDetailsService.GetDataInterface(ByVal enumMSDI As SerialNumberDetailsServiceDataInterfaces) -> Object
SerialNumberDetailsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SerialNumberDetailsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SerialNumberDetailsService.Update(ByVal pISerialNumberDetail As SerialNumberDetail)
SerialNumbers.BaseLineNumber : Long [R/W]
SerialNumbers.BatchID : String [R/W]
SerialNumbers.Count : Long [R]
SerialNumbers.ExpiryDate : Date [R/W]
SerialNumbers.InternalSerialNumber : String [R/W]
SerialNumbers.ItemCode : String [R/W]
SerialNumbers.Location : String [R/W]
SerialNumbers.ManufactureDate : Date [R/W]
SerialNumbers.ManufacturerSerialNumber : String [R/W]
SerialNumbers.Notes : String [R/W]
SerialNumbers.Quantity : Double [R/W]
SerialNumbers.ReceptionDate : Date [R/W]
SerialNumbers.SystemSerialNumber : Long [R/W]
SerialNumbers.TrackingNote : Long [R/W]
SerialNumbers.TrackingNoteLine : Long [R/W]
SerialNumbers.UserFields : UserFields [R]
SerialNumbers.WarrantyEnd : Date [R/W]
SerialNumbers.WarrantyStart : Date [R/W]
SerialNumbers.Add()
SerialNumbers.SetCurrentLine(ByVal LineNum As Long)
Series.ATDocumentType : String [R/W]
Series.BPLID : Long [R/W]
Series.CostAccountOnly : BoYesNoEnum [R/W]
Series.DigitNumber : Long [R/W]
Series.Document : String [R/W]
Series.DocumentSubType : String [R/W]
Series.GroupCode : BoSeriesGroupEnum [R/W]
Series.InitialNumber : Long [R/W]
Series.InvoiceType : Long [R/W]
Series.InvoiceTypeOfNegativeInvoice : Long [R/W]
Series.IsDigitalSeries : BoYesNoEnum [R/W]
Series.IsElectronicCommEnabled : BoYesNoEnum [R/W]
Series.IsManual : BoYesNoEnum [R]
Series.LastNumber : Long [R/W]
Series.Locked : BoYesNoEnum [R/W]
Series.Name : String [R/W]
Series.NextNumber : Long [R/W]
Series.PeriodIndicator : String [R/W]
Series.PortugalSeriesAction : String [R/W]
Series.PortugalSeriesPhase : String [R]
Series.PortugalSeriesStatus : String [R]
Series.Prefix : String [R/W]
Series.Remarks : String [R/W]
Series.Series : Long [R]
Series.SeriesType : BoSeriesTypeEnum [R/W]
Series.Suffix : String [R/W]
Series.UserFields : Fields [R]
Series.FromXMLFile(ByVal bstrFileName As String)
Series.FromXMLString(ByVal bstrXML As String)
Series.GetXMLSchema() -> String
Series.ToXMLFile(ByVal bstrFileName As String)
Series.ToXMLString() -> String
SeriesCollection.Count : Long [R]
SeriesCollection.Add() -> Series
SeriesCollection.GetXMLSchema() -> String
SeriesCollection.Item(ByVal vtIndex As Variant) -> Series
SeriesCollection.ToXMLFile(ByVal bstrFileName As String)
SeriesCollection.ToXMLString() -> String
SeriesLine.FirstNum : Long [R/W]
SeriesLine.LastNum : Long [R/W]
SeriesLine.NextNum : Long [R]
SeriesLine.Prefix : String [R/W]
SeriesLine.Series : Long [R]
SeriesLine.FromXMLFile(ByVal bstrFileName As String)
SeriesLine.FromXMLString(ByVal bstrXML As String)
SeriesLine.GetXMLSchema() -> String
SeriesLine.ToXMLFile(ByVal bstrFileName As String)
SeriesLine.ToXMLString() -> String
SeriesLines.Count : Long [R]
SeriesLines.Add() -> SeriesLine
SeriesLines.GetXMLSchema() -> String
SeriesLines.Item(ByVal vtIndex As Variant) -> SeriesLine
SeriesLines.Remove(ByVal vtIndex As Variant)
SeriesLines.ToXMLFile(ByVal bstrFileName As String)
SeriesLines.ToXMLString() -> String
SeriesParams.Series : Long [R/W]
SeriesParams.FromXMLFile(ByVal bstrFileName As String)
SeriesParams.FromXMLString(ByVal bstrXML As String)
SeriesParams.GetXMLSchema() -> String
SeriesParams.ToXMLFile(ByVal bstrFileName As String)
SeriesParams.ToXMLString() -> String
SeriesService.AddElectronicSeries(ByVal pIElectronicSeries As ElectronicSeries) -> ElectronicSeriesParams
SeriesService.AddSeries(ByVal pISeries As Series) -> SeriesParams
SeriesService.AttachSeriesToDocument(ByVal pIDocumentSeriesParams As DocumentSeriesParams)
SeriesService.ChangeDocumentMenuName(ByVal pIDocumentChangeMenuName As DocumentChangeMenuName)
SeriesService.GetDataInterface(ByVal enumMSDI As SeriesServiceDataInterfaces) -> Object
SeriesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SeriesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SeriesService.GetDefaultElectronicSeries(ByVal pISeriesParams As SeriesParams) -> ElectronicSeriesParams
SeriesService.GetDefaultSeries(ByVal pIDocumentTypeParams As DocumentTypeParams) -> Series
SeriesService.GetDocumentChangedMenuName(ByVal pIDocumentTypeParams As DocumentTypeParams) -> DocumentChangeMenuName
SeriesService.GetDocumentSeries(ByVal pIDocumentTypeParams As DocumentTypeParams) -> SeriesCollection
SeriesService.GetElectronicSeries(ByVal pElectronicSeriesParams As ElectronicSeriesParams) -> ElectronicSeries
SeriesService.GetSeries(ByVal pSeriesParams As SeriesParams) -> Series
SeriesService.RemoveElectronicSeries(ByVal pIElectronicSeriesParam As ElectronicSeriesParams)
SeriesService.RemoveSeries(ByVal pISeriesParam As SeriesParams)
SeriesService.SetDefaultElectronicSeries(ByVal pIDefaultElectronicSeriesParams As DefaultElectronicSeriesParams)
SeriesService.SetDefaultSeriesForAllUsers(ByVal pIDocumentSeriesParams As DocumentSeriesParams)
SeriesService.SetDefaultSeriesForCurrentUser(ByVal pIDocumentSeriesParams As DocumentSeriesParams)
SeriesService.SetDefaultSeriesForUser(ByVal pIDocumentSeriesUserParams As DocumentSeriesUserParams)
SeriesService.UnattachSeriesFromDocument(ByVal pIDocumentSeriesParams As DocumentSeriesParams)
SeriesService.UpdateElectronicSeries(ByVal pIElectronicSeries As ElectronicSeries)
SeriesService.UpdateSeries(ByVal pISeries As Series)
ServiceAppReport.Code : Long [R]
ServiceAppReport.CustomizedReportName : String [R/W]
ServiceAppReport.ReportChoice : MobileAppReportChoiceEnum [R/W]
ServiceAppReport.SystemReportName : String [R/W]
ServiceAppReport.FromXMLFile(ByVal bstrFileName As String)
ServiceAppReport.FromXMLString(ByVal bstrXML As String)
ServiceAppReport.GetXMLSchema() -> String
ServiceAppReport.ToXMLFile(ByVal bstrFileName As String)
ServiceAppReport.ToXMLString() -> String
ServiceAppReportContent.ReportContent : String [R/W]
ServiceAppReportContent.FromXMLFile(ByVal bstrFileName As String)
ServiceAppReportContent.FromXMLString(ByVal bstrXML As String)
ServiceAppReportContent.GetXMLSchema() -> String
ServiceAppReportContent.ToXMLFile(ByVal bstrFileName As String)
ServiceAppReportContent.ToXMLString() -> String
ServiceAppReportParams.Code : Long [R/W]
ServiceAppReportParams.ReportChoice : MobileAppReportChoiceEnum [R/W]
ServiceAppReportParams.FromXMLFile(ByVal bstrFileName As String)
ServiceAppReportParams.FromXMLString(ByVal bstrXML As String)
ServiceAppReportParams.GetXMLSchema() -> String
ServiceAppReportParams.ToXMLFile(ByVal bstrFileName As String)
ServiceAppReportParams.ToXMLString() -> String
ServiceCallActivities.ActivityCode : Long [R/W]
ServiceCallActivities.Count : Long [R]
ServiceCallActivities.LineNum : Long [R]
ServiceCallActivities.UserFields : UserFields [R]
ServiceCallActivities.Add()
ServiceCallActivities.Delete()
ServiceCallActivities.SetCurrentLine(ByVal LineNum As Long)
ServiceCallBPAddressComponents.BillToAddress2 : String [R/W]
ServiceCallBPAddressComponents.BillToAddress3 : String [R/W]
ServiceCallBPAddressComponents.BillToAddressType : String [R/W]
ServiceCallBPAddressComponents.BillToBlock : String [R/W]
ServiceCallBPAddressComponents.BillToBuilding : String [R/W]
ServiceCallBPAddressComponents.BillToCity : String [R/W]
ServiceCallBPAddressComponents.BillToCountry : String [R/W]
ServiceCallBPAddressComponents.BillToCounty : String [R/W]
ServiceCallBPAddressComponents.BillToGlobalLocationNumber : String [R/W]
ServiceCallBPAddressComponents.BillToState : String [R/W]
ServiceCallBPAddressComponents.BillToStreet : String [R/W]
ServiceCallBPAddressComponents.BillToStreetNo : String [R/W]
ServiceCallBPAddressComponents.BillToZipCode : String [R/W]
ServiceCallBPAddressComponents.ShipToAddress2 : String [R/W]
ServiceCallBPAddressComponents.ShipToAddress3 : String [R/W]
ServiceCallBPAddressComponents.ShipToAddressType : String [R/W]
ServiceCallBPAddressComponents.ShipToBlock : String [R/W]
ServiceCallBPAddressComponents.ShipToBuilding : String [R/W]
ServiceCallBPAddressComponents.ShipToCity : String [R/W]
ServiceCallBPAddressComponents.ShipToCountry : String [R/W]
ServiceCallBPAddressComponents.ShipToCounty : String [R/W]
ServiceCallBPAddressComponents.ShipToGlobalLocationNumber : String [R/W]
ServiceCallBPAddressComponents.ShipToState : String [R/W]
ServiceCallBPAddressComponents.ShipToStreet : String [R/W]
ServiceCallBPAddressComponents.ShipToStreetNo : String [R/W]
ServiceCallBPAddressComponents.ShipToZipCode : String [R/W]
ServiceCallBPAddressComponents.UserFields : UserFields [R]
ServiceCallInventoryExpenses.Count : Long [R]
ServiceCallInventoryExpenses.DocEntry : Long [R/W]
ServiceCallInventoryExpenses.DocumentNumber : Long [R/W]
ServiceCallInventoryExpenses.DocumentPostingDate : Date [R]
ServiceCallInventoryExpenses.DocumentType : BoSvcEpxDocTypes [R/W]
ServiceCallInventoryExpenses.LineNum : Long [R]
ServiceCallInventoryExpenses.PartType : BoSvcExpPartTypes [R]
ServiceCallInventoryExpenses.StockTransferDirection : BoStckTrnDir [R/W]
ServiceCallInventoryExpenses.UserFields : UserFields [R]
ServiceCallInventoryExpenses.Add()
ServiceCallInventoryExpenses.Delete()
ServiceCallInventoryExpenses.SetCurrentLine(ByVal LineNum As Long)
ServiceCallOrigin.Active : BoYesNoEnum [R/W]
ServiceCallOrigin.Description : String [R/W]
ServiceCallOrigin.Name : String [R/W]
ServiceCallOrigin.OriginID : Long [R]
ServiceCallOrigin.FromXMLFile(ByVal bstrFileName As String)
ServiceCallOrigin.FromXMLString(ByVal bstrXML As String)
ServiceCallOrigin.GetXMLSchema() -> String
ServiceCallOrigin.ToXMLFile(ByVal bstrFileName As String)
ServiceCallOrigin.ToXMLString() -> String
ServiceCallOriginParams.Name : String [R]
ServiceCallOriginParams.OriginID : Long [R/W]
ServiceCallOriginParams.FromXMLFile(ByVal bstrFileName As String)
ServiceCallOriginParams.FromXMLString(ByVal bstrXML As String)
ServiceCallOriginParams.GetXMLSchema() -> String
ServiceCallOriginParams.ToXMLFile(ByVal bstrFileName As String)
ServiceCallOriginParams.ToXMLString() -> String
ServiceCallOriginParamsCollection.Count : Long [R]
ServiceCallOriginParamsCollection.Add() -> ServiceCallOriginParams
ServiceCallOriginParamsCollection.GetXMLSchema() -> String
ServiceCallOriginParamsCollection.Item(ByVal vtIndex As Variant) -> ServiceCallOriginParams
ServiceCallOriginParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ServiceCallOriginParamsCollection.ToXMLString() -> String
ServiceCallOriginsService.AddServiceCallOrigin(ByVal pIServiceCallOrigin As ServiceCallOrigin) -> ServiceCallOriginParams
ServiceCallOriginsService.DeleteServiceCallOrigin(ByVal pIServiceCallOriginParams As ServiceCallOriginParams)
ServiceCallOriginsService.GetDataInterface(ByVal enumMSDI As ServiceCallOriginsServiceDataInterfaces) -> Object
ServiceCallOriginsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ServiceCallOriginsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ServiceCallOriginsService.GetServiceCallOrigin(ByVal pIServiceCallOriginParams As ServiceCallOriginParams) -> ServiceCallOrigin
ServiceCallOriginsService.GetServiceCallOriginList() -> ServiceCallOriginParamsCollection
ServiceCallOriginsService.UpdateServiceCallOrigin(ByVal pIServiceCallOrigin As ServiceCallOrigin)
ServiceCallProblemSubType.Active : BoYesNoEnum [R/W]
ServiceCallProblemSubType.Description : String [R/W]
ServiceCallProblemSubType.Name : String [R/W]
ServiceCallProblemSubType.ProblemSubTypeID : Long [R]
ServiceCallProblemSubType.FromXMLFile(ByVal bstrFileName As String)
ServiceCallProblemSubType.FromXMLString(ByVal bstrXML As String)
ServiceCallProblemSubType.GetXMLSchema() -> String
ServiceCallProblemSubType.ToXMLFile(ByVal bstrFileName As String)
ServiceCallProblemSubType.ToXMLString() -> String
ServiceCallProblemSubTypeParams.Name : String [R]
ServiceCallProblemSubTypeParams.ProblemSubTypeID : Long [R/W]
ServiceCallProblemSubTypeParams.FromXMLFile(ByVal bstrFileName As String)
ServiceCallProblemSubTypeParams.FromXMLString(ByVal bstrXML As String)
ServiceCallProblemSubTypeParams.GetXMLSchema() -> String
ServiceCallProblemSubTypeParams.ToXMLFile(ByVal bstrFileName As String)
ServiceCallProblemSubTypeParams.ToXMLString() -> String
ServiceCallProblemSubTypeParamsCollection.Count : Long [R]
ServiceCallProblemSubTypeParamsCollection.Add() -> ServiceCallProblemSubTypeParams
ServiceCallProblemSubTypeParamsCollection.GetXMLSchema() -> String
ServiceCallProblemSubTypeParamsCollection.Item(ByVal vtIndex As Variant) -> ServiceCallProblemSubTypeParams
ServiceCallProblemSubTypeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ServiceCallProblemSubTypeParamsCollection.ToXMLString() -> String
ServiceCallProblemSubTypesService.AddServiceCallProblemSubType(ByVal pIServiceCallProblemSubType As ServiceCallProblemSubType) -> ServiceCallProblemSubTypeParams
ServiceCallProblemSubTypesService.DeleteServiceCallProblemSubType(ByVal pIServiceCallProblemSubTypeParams As ServiceCallProblemSubTypeParams)
ServiceCallProblemSubTypesService.GetDataInterface(ByVal enumMSDI As ServiceCallProblemSubTypesServiceDataInterfaces) -> Object
ServiceCallProblemSubTypesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ServiceCallProblemSubTypesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ServiceCallProblemSubTypesService.GetServiceCallProblemSubType(ByVal pIServiceCallProblemSubTypeParams As ServiceCallProblemSubTypeParams) -> ServiceCallProblemSubType
ServiceCallProblemSubTypesService.GetServiceCallProblemSubTypeList() -> ServiceCallProblemSubTypeParamsCollection
ServiceCallProblemSubTypesService.UpdateServiceCallProblemSubType(ByVal pIServiceCallProblemSubType As ServiceCallProblemSubType)
ServiceCallProblemType.Active : BoYesNoEnum [R/W]
ServiceCallProblemType.Description : String [R/W]
ServiceCallProblemType.Name : String [R/W]
ServiceCallProblemType.ProblemTypeID : Long [R]
ServiceCallProblemType.FromXMLFile(ByVal bstrFileName As String)
ServiceCallProblemType.FromXMLString(ByVal bstrXML As String)
ServiceCallProblemType.GetXMLSchema() -> String
ServiceCallProblemType.ToXMLFile(ByVal bstrFileName As String)
ServiceCallProblemType.ToXMLString() -> String
ServiceCallProblemTypeParams.Name : String [R]
ServiceCallProblemTypeParams.ProblemTypeID : Long [R/W]
ServiceCallProblemTypeParams.FromXMLFile(ByVal bstrFileName As String)
ServiceCallProblemTypeParams.FromXMLString(ByVal bstrXML As String)
ServiceCallProblemTypeParams.GetXMLSchema() -> String
ServiceCallProblemTypeParams.ToXMLFile(ByVal bstrFileName As String)
ServiceCallProblemTypeParams.ToXMLString() -> String
ServiceCallProblemTypeParamsCollection.Count : Long [R]
ServiceCallProblemTypeParamsCollection.Add() -> ServiceCallProblemTypeParams
ServiceCallProblemTypeParamsCollection.GetXMLSchema() -> String
ServiceCallProblemTypeParamsCollection.Item(ByVal vtIndex As Variant) -> ServiceCallProblemTypeParams
ServiceCallProblemTypeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ServiceCallProblemTypeParamsCollection.ToXMLString() -> String
ServiceCallProblemTypesService.AddServiceCallProblemType(ByVal pIServiceCallProblemType As ServiceCallProblemType) -> ServiceCallProblemTypeParams
ServiceCallProblemTypesService.DeleteServiceCallProblemType(ByVal pIServiceCallProblemTypeParams As ServiceCallProblemTypeParams)
ServiceCallProblemTypesService.GetDataInterface(ByVal enumMSDI As ServiceCallProblemTypesServiceDataInterfaces) -> Object
ServiceCallProblemTypesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ServiceCallProblemTypesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ServiceCallProblemTypesService.GetServiceCallProblemType(ByVal pIServiceCallProblemTypeParams As ServiceCallProblemTypeParams) -> ServiceCallProblemType
ServiceCallProblemTypesService.GetServiceCallProblemTypeList() -> ServiceCallProblemTypeParamsCollection
ServiceCallProblemTypesService.UpdateServiceCallProblemType(ByVal pIServiceCallProblemType As ServiceCallProblemType)
ServiceCalls.Activities : ServiceCallActivities [R]
ServiceCalls.AddressName : String [R/W]
ServiceCalls.AddressType : BoAddressType [R/W]
ServiceCalls.AssignedDate : Date [R]
ServiceCalls.AssignedTime : Long [R]
ServiceCalls.AssigneeCode : Long [R/W]
ServiceCalls.AttachmentEntry : Long [R/W]
ServiceCalls.BelongsToAQueue : BoYesNoEnum [R/W]
ServiceCalls.BPAddressComponents : ServiceCallBPAddressComponents [R]
ServiceCalls.BPBillToAddress : String [R/W]
ServiceCalls.BPBillToCode : String [R/W]
ServiceCalls.BPCellular : String [R/W]
ServiceCalls.BPContactPerson : String [R/W]
ServiceCalls.BPeMail : String [R/W]
ServiceCalls.BPFax : String [R/W]
ServiceCalls.BPPhone1 : String [R/W]
ServiceCalls.BPPhone2 : String [R/W]
ServiceCalls.BPProjectCode : String [R/W]
ServiceCalls.BPShipToAddress : String [R/W]
ServiceCalls.BPShipToCode : String [R/W]
ServiceCalls.BPTerritory : Long [R/W]
ServiceCalls.Browser : DataBrowser [R]
ServiceCalls.CallType : Long [R/W]
ServiceCalls.City : String [R/W]
ServiceCalls.ClosingDate : Date [R/W]
ServiceCalls.ClosingTime : Long [R/W]
ServiceCalls.ClosingTimeEx : Date [R/W]
ServiceCalls.ContactCode : Long [R/W]
ServiceCalls.ContractEndDate : Date [R]
ServiceCalls.ContractID : Long [R/W]
ServiceCalls.Country : String [R/W]
ServiceCalls.CreationDate : Date [R/W]
ServiceCalls.CreationTime : Date [R/W]
ServiceCalls.CustomerCode : String [R/W]
ServiceCalls.CustomerName : String [R/W]
ServiceCalls.CustomerRefNo : String [R/W]
ServiceCalls.Description : String [R/W]
ServiceCalls.DisplayInCalendar : BoYesNoEnum [R/W]
ServiceCalls.DocNum : Long [R/W]
ServiceCalls.Duration : Double [R/W]
ServiceCalls.DurationType : BoDurations [R/W]
ServiceCalls.EndDuedate : Date [R/W]
ServiceCalls.EndTime : Date [R/W]
ServiceCalls.EntitledforService : BoYesNoEnum [R]
ServiceCalls.Expenses : ServiceCallInventoryExpenses [R]
ServiceCalls.HandWritten : BoYesNoEnum [R/W]
ServiceCalls.InternalSerialNum : String [R/W]
ServiceCalls.ItemCode : String [R/W]
ServiceCalls.ItemDescription : String [R/W]
ServiceCalls.ItemGroupCode : Long [R]
ServiceCalls.Location : Long [R/W]
ServiceCalls.ManufacturerSerialNum : String [R/W]
ServiceCalls.Origin : Long [R/W]
ServiceCalls.PeriodIndicator : String [R]
ServiceCalls.Priority : BoSvcCallPriorities [R/W]
ServiceCalls.ProblemSubType : Long [R/W]
ServiceCalls.ProblemType : Long [R/W]
ServiceCalls.Queue : String [R/W]
ServiceCalls.Reminder : BoYesNoEnum [R/W]
ServiceCalls.ReminderPeriod : Double [R/W]
ServiceCalls.ReminderType : BoDurations [R/W]
ServiceCalls.Resolution : String [R/W]
ServiceCalls.ResolutionDate : Date [R/W]
ServiceCalls.ResolutionOnDate : Date [R]
ServiceCalls.ResolutionOnTime : Long [R]
ServiceCalls.ResolutionTime : Date [R/W]
ServiceCalls.Responder : Long [R]
ServiceCalls.ResponseAssignee : Long [R]
ServiceCalls.ResponseByDate : Date [R]
ServiceCalls.ResponseByTime : Long [R]
ServiceCalls.ResponseOnDate : Date [R]
ServiceCalls.ResponseOnTime : Long [R]
ServiceCalls.Room : String [R/W]
ServiceCalls.Schedulings : ServiceCallSchedulings [R]
ServiceCalls.Series : Long [R/W]
ServiceCalls.ServiceBPType : ServiceTypeEnum [R/W]
ServiceCalls.ServiceCallID : Long [R]
ServiceCalls.Solutions : ServiceCallSolutions [R]
ServiceCalls.StartDate : Date [R/W]
ServiceCalls.StartTime : Date [R/W]
ServiceCalls.State : String [R/W]
ServiceCalls.Status : Long [R/W]
ServiceCalls.Street : String [R/W]
ServiceCalls.Subject : String [R/W]
ServiceCalls.SupplementaryCode : String [R]
ServiceCalls.TechnicianCode : Long [R/W]
ServiceCalls.Telephone : String [R/W]
ServiceCalls.UpdateDate : Date [R]
ServiceCalls.UpdatedTime : Long [R]
ServiceCalls.UserFields : UserFields [R]
ServiceCalls.Add() -> Long
ServiceCalls.Close() -> Long
ServiceCalls.GetAsXML() -> String
ServiceCalls.GetByKey(ByVal ServiceCallID As Long) -> Boolean
ServiceCalls.Remove() -> Long
ServiceCalls.SaveToFile(ByVal FileName As String)
ServiceCalls.SaveXML(ByRef FileName As String)
ServiceCalls.Update() -> Long
ServiceCallSchedulings.ActualDuration : Double [R/W]
ServiceCallSchedulings.ActualDurationType : BoDurations [R/W]
ServiceCallSchedulings.Address2 : String [R/W]
ServiceCallSchedulings.Address3 : String [R/W]
ServiceCallSchedulings.AddressName : String [R/W]
ServiceCallSchedulings.AddressText : String [R/W]
ServiceCallSchedulings.AddressType : String [R/W]
ServiceCallSchedulings.AddressTypeBS : BoAddressType [R/W]
ServiceCallSchedulings.Block : String [R/W]
ServiceCallSchedulings.CheckInDate : Date [R/W]
ServiceCallSchedulings.CheckInLatitude : String [R/W]
ServiceCallSchedulings.CheckInLocation : String [R/W]
ServiceCallSchedulings.CheckInLongitude : String [R/W]
ServiceCallSchedulings.CheckInTime : Date [R/W]
ServiceCallSchedulings.CheckOutDate : Date [R/W]
ServiceCallSchedulings.CheckOutTime : Date [R/W]
ServiceCallSchedulings.City : String [R/W]
ServiceCallSchedulings.Count : Long [R]
ServiceCallSchedulings.Country : String [R/W]
ServiceCallSchedulings.County : String [R/W]
ServiceCallSchedulings.DisplayInCalendar : BoYesNoEnum [R/W]
ServiceCallSchedulings.Duration : Double [R/W]
ServiceCallSchedulings.DurationType : BoDurations [R/W]
ServiceCallSchedulings.EndDate : Date [R/W]
ServiceCallSchedulings.EndTime : Date [R/W]
ServiceCallSchedulings.GlobalLocNum : String [R/W]
ServiceCallSchedulings.HandledBy : Long [R/W]
ServiceCallSchedulings.IsClosed : BoYesNoEnum [R/W]
ServiceCallSchedulings.IsUnscheduled : BoYesNoEnum [R/W]
ServiceCallSchedulings.LineNum : Long [R]
ServiceCallSchedulings.Location : Long [R/W]
ServiceCallSchedulings.Remark : String [R/W]
ServiceCallSchedulings.Reminder : BoYesNoEnum [R/W]
ServiceCallSchedulings.ReminderDate : Date [R]
ServiceCallSchedulings.ReminderPeriod : Double [R/W]
ServiceCallSchedulings.ReminderSent : BoYesNoEnum [R]
ServiceCallSchedulings.ReminderTime : Date [R]
ServiceCallSchedulings.ReminderType : BoDurations [R/W]
ServiceCallSchedulings.Room : String [R/W]
ServiceCallSchedulings.SalesOrders : String [R/W]
ServiceCallSchedulings.SignatureName : String [R/W]
ServiceCallSchedulings.StartDate : Date [R/W]
ServiceCallSchedulings.StartTime : Date [R/W]
ServiceCallSchedulings.State : String [R/W]
ServiceCallSchedulings.Street : String [R/W]
ServiceCallSchedulings.StreetNo : String [R/W]
ServiceCallSchedulings.TaxOffice : String [R/W]
ServiceCallSchedulings.Technician : Long [R/W]
ServiceCallSchedulings.UserFields : UserFields [R]
ServiceCallSchedulings.ZipCode : String [R/W]
ServiceCallSchedulings.Add()
ServiceCallSchedulings.SetCurrentLine(ByVal LineNum As Long)
ServiceCallSolutions.Count : Long [R]
ServiceCallSolutions.LineNum : Long [R]
ServiceCallSolutions.SolutionID : Long [R/W]
ServiceCallSolutions.UserFields : UserFields [R]
ServiceCallSolutions.Add()
ServiceCallSolutions.Delete()
ServiceCallSolutions.SetCurrentLine(ByVal LineNum As Long)
ServiceCallSolutionStatus.Active : BoYesNoEnum [R/W]
ServiceCallSolutionStatus.Description : String [R/W]
ServiceCallSolutionStatus.Name : String [R/W]
ServiceCallSolutionStatus.StatusId : Long [R]
ServiceCallSolutionStatus.FromXMLFile(ByVal bstrFileName As String)
ServiceCallSolutionStatus.FromXMLString(ByVal bstrXML As String)
ServiceCallSolutionStatus.GetXMLSchema() -> String
ServiceCallSolutionStatus.ToXMLFile(ByVal bstrFileName As String)
ServiceCallSolutionStatus.ToXMLString() -> String
ServiceCallSolutionStatusParams.Name : String [R]
ServiceCallSolutionStatusParams.StatusId : Long [R/W]
ServiceCallSolutionStatusParams.FromXMLFile(ByVal bstrFileName As String)
ServiceCallSolutionStatusParams.FromXMLString(ByVal bstrXML As String)
ServiceCallSolutionStatusParams.GetXMLSchema() -> String
ServiceCallSolutionStatusParams.ToXMLFile(ByVal bstrFileName As String)
ServiceCallSolutionStatusParams.ToXMLString() -> String
ServiceCallSolutionStatusParamsCollection.Count : Long [R]
ServiceCallSolutionStatusParamsCollection.Add() -> ServiceCallSolutionStatusParams
ServiceCallSolutionStatusParamsCollection.GetXMLSchema() -> String
ServiceCallSolutionStatusParamsCollection.Item(ByVal vtIndex As Variant) -> ServiceCallSolutionStatusParams
ServiceCallSolutionStatusParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ServiceCallSolutionStatusParamsCollection.ToXMLString() -> String
ServiceCallSolutionStatusService.AddServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatus As ServiceCallSolutionStatus) -> ServiceCallSolutionStatusParams
ServiceCallSolutionStatusService.DeleteServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatusParams As ServiceCallSolutionStatusParams)
ServiceCallSolutionStatusService.GetDataInterface(ByVal enumMSDI As ServiceCallSolutionStatusServiceDataInterfaces) -> Object
ServiceCallSolutionStatusService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ServiceCallSolutionStatusService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ServiceCallSolutionStatusService.GetServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatusParams As ServiceCallSolutionStatusParams) -> ServiceCallSolutionStatus
ServiceCallSolutionStatusService.GetServiceCallSolutionStatusList() -> ServiceCallSolutionStatusParamsCollection
ServiceCallSolutionStatusService.UpdateServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatus As ServiceCallSolutionStatus)
ServiceCallStatus.Active : BoYesNoEnum [R/W]
ServiceCallStatus.Description : String [R/W]
ServiceCallStatus.Name : String [R/W]
ServiceCallStatus.StatusId : Long [R]
ServiceCallStatus.FromXMLFile(ByVal bstrFileName As String)
ServiceCallStatus.FromXMLString(ByVal bstrXML As String)
ServiceCallStatus.GetXMLSchema() -> String
ServiceCallStatus.ToXMLFile(ByVal bstrFileName As String)
ServiceCallStatus.ToXMLString() -> String
ServiceCallStatusParams.Name : String [R]
ServiceCallStatusParams.StatusId : Long [R/W]
ServiceCallStatusParams.FromXMLFile(ByVal bstrFileName As String)
ServiceCallStatusParams.FromXMLString(ByVal bstrXML As String)
ServiceCallStatusParams.GetXMLSchema() -> String
ServiceCallStatusParams.ToXMLFile(ByVal bstrFileName As String)
ServiceCallStatusParams.ToXMLString() -> String
ServiceCallStatusParamsCollection.Count : Long [R]
ServiceCallStatusParamsCollection.Add() -> ServiceCallStatusParams
ServiceCallStatusParamsCollection.GetXMLSchema() -> String
ServiceCallStatusParamsCollection.Item(ByVal vtIndex As Variant) -> ServiceCallStatusParams
ServiceCallStatusParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ServiceCallStatusParamsCollection.ToXMLString() -> String
ServiceCallStatusService.AddServiceCallStatus(ByVal pIServiceCallStatus As ServiceCallStatus) -> ServiceCallStatusParams
ServiceCallStatusService.DeleteServiceCallStatus(ByVal pIServiceCallStatusParams As ServiceCallStatusParams)
ServiceCallStatusService.GetDataInterface(ByVal enumMSDI As ServiceCallStatusServiceDataInterfaces) -> Object
ServiceCallStatusService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ServiceCallStatusService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ServiceCallStatusService.GetServiceCallStatus(ByVal pIServiceCallStatusParams As ServiceCallStatusParams) -> ServiceCallStatus
ServiceCallStatusService.GetServiceCallStatusList() -> ServiceCallStatusParamsCollection
ServiceCallStatusService.UpdateServiceCallStatus(ByVal pIServiceCallStatus As ServiceCallStatus)
ServiceCallType.Active : BoYesNoEnum [R/W]
ServiceCallType.CallTypeID : Long [R]
ServiceCallType.Description : String [R/W]
ServiceCallType.Name : String [R/W]
ServiceCallType.FromXMLFile(ByVal bstrFileName As String)
ServiceCallType.FromXMLString(ByVal bstrXML As String)
ServiceCallType.GetXMLSchema() -> String
ServiceCallType.ToXMLFile(ByVal bstrFileName As String)
ServiceCallType.ToXMLString() -> String
ServiceCallTypeParams.CallTypeID : Long [R/W]
ServiceCallTypeParams.Name : String [R]
ServiceCallTypeParams.FromXMLFile(ByVal bstrFileName As String)
ServiceCallTypeParams.FromXMLString(ByVal bstrXML As String)
ServiceCallTypeParams.GetXMLSchema() -> String
ServiceCallTypeParams.ToXMLFile(ByVal bstrFileName As String)
ServiceCallTypeParams.ToXMLString() -> String
ServiceCallTypeParamsCollection.Count : Long [R]
ServiceCallTypeParamsCollection.Add() -> ServiceCallTypeParams
ServiceCallTypeParamsCollection.GetXMLSchema() -> String
ServiceCallTypeParamsCollection.Item(ByVal vtIndex As Variant) -> ServiceCallTypeParams
ServiceCallTypeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ServiceCallTypeParamsCollection.ToXMLString() -> String
ServiceCallTypesService.AddServiceCallType(ByVal pIServiceCallType As ServiceCallType) -> ServiceCallTypeParams
ServiceCallTypesService.DeleteServiceCallType(ByVal pIServiceCallTypeParams As ServiceCallTypeParams)
ServiceCallTypesService.GetDataInterface(ByVal enumMSDI As ServiceCallTypesServiceDataInterfaces) -> Object
ServiceCallTypesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ServiceCallTypesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ServiceCallTypesService.GetServiceCallType(ByVal pIServiceCallTypeParams As ServiceCallTypeParams) -> ServiceCallType
ServiceCallTypesService.GetServiceCallTypeList() -> ServiceCallTypeParamsCollection
ServiceCallTypesService.UpdateServiceCallType(ByVal pIServiceCallType As ServiceCallType)
ServiceContract_Lines.Count : Long [R]
ServiceContract_Lines.EndDate : Date [R/W]
ServiceContract_Lines.InternalSerialNum : String [R/W]
ServiceContract_Lines.ItemCode : String [R/W]
ServiceContract_Lines.ItemGroup : Long [R/W]
ServiceContract_Lines.ItemGroupName : String [R]
ServiceContract_Lines.ItemName : String [R/W]
ServiceContract_Lines.LineNum : Long [R]
ServiceContract_Lines.ManufacturerSerialNum : String [R/W]
ServiceContract_Lines.StartDate : Date [R/W]
ServiceContract_Lines.TerminationDate : Date [R/W]
ServiceContract_Lines.UserFields : UserFields [R]
ServiceContract_Lines.Add()
ServiceContract_Lines.SetCurrentLine(ByVal LineNum As Long)
ServiceContracts.AttachmentEntry : Long [R/W]
ServiceContracts.Attachments : Attachments [R]
ServiceContracts.Browser : DataBrowser [R]
ServiceContracts.ContactCode : Long [R/W]
ServiceContracts.ContractID : Long [R]
ServiceContracts.ContractTemplate : String [R/W]
ServiceContracts.ContractType : BoContractTypes [R/W]
ServiceContracts.CustomerCode : String [R/W]
ServiceContracts.CustomerName : String [R/W]
ServiceContracts.Description : String [R/W]
ServiceContracts.DurationOfCoverage : Long [R]
ServiceContracts.EndDate : Date [R/W]
ServiceContracts.FridayEnabled : BoYesNoEnum [R/W]
ServiceContracts.FridayEnd : Date [R/W]
ServiceContracts.FridayStart : Date [R/W]
ServiceContracts.IncludeHolidays : BoYesNoEnum [R/W]
ServiceContracts.IncludeLabor : BoYesNoEnum [R/W]
ServiceContracts.IncludeParts : BoYesNoEnum [R/W]
ServiceContracts.IncludeTravel : BoYesNoEnum [R/W]
ServiceContracts.Lines : ServiceContract_Lines [R]
ServiceContracts.MondayEnabled : BoYesNoEnum [R/W]
ServiceContracts.MondayEnd : Date [R/W]
ServiceContracts.MondayStart : Date [R/W]
ServiceContracts.Owner : Long [R/W]
ServiceContracts.Remarks : String [R/W]
ServiceContracts.ReminderTime : Long [R/W]
ServiceContracts.RemindUnit : BoRemindUnits [R/W]
ServiceContracts.Renewal : BoYesNoEnum [R/W]
ServiceContracts.ResolutionTime : Long [R/W]
ServiceContracts.ResolutionUnit : BoResolutionUnits [R/W]
ServiceContracts.ResponseTime : Long [R/W]
ServiceContracts.ResponseUnit : BoResponseUnit [R/W]
ServiceContracts.SaturdayEnabled : BoYesNoEnum [R/W]
ServiceContracts.SaturdayEnd : Date [R/W]
ServiceContracts.SaturdayStart : Date [R/W]
ServiceContracts.ServiceBPType : ServiceTypeEnum [R/W]
ServiceContracts.ServiceType : BoServiceTypes [R/W]
ServiceContracts.StartDate : Date [R/W]
ServiceContracts.Status : BoSvcContractStatus [R/W]
ServiceContracts.SundayEnabled : BoYesNoEnum [R/W]
ServiceContracts.SundayEnd : Date [R/W]
ServiceContracts.SundayStart : Date [R/W]
ServiceContracts.TemplateRemarks : String [R]
ServiceContracts.TerminationDate : Date [R/W]
ServiceContracts.ThursdayEnabled : BoYesNoEnum [R/W]
ServiceContracts.ThursdayEnd : Date [R/W]
ServiceContracts.ThursdayStart : Date [R/W]
ServiceContracts.TuesdayEnabled : BoYesNoEnum [R/W]
ServiceContracts.TuesdayEnd : Date [R/W]
ServiceContracts.TuesdayStart : Date [R/W]
ServiceContracts.UserFields : UserFields [R]
ServiceContracts.WednesdayEnabled : BoYesNoEnum [R/W]
ServiceContracts.WednesdayEnd : Date [R/W]
ServiceContracts.WednesdayStart : Date [R/W]
ServiceContracts.Add() -> Long
ServiceContracts.Close() -> Long
ServiceContracts.GetAsXML() -> String
ServiceContracts.GetByKey(ByVal ContractID As Long) -> Boolean
ServiceContracts.Remove() -> Long
ServiceContracts.SaveToFile(ByVal FileName As String)
ServiceContracts.SaveXML(ByRef FileName As String)
ServiceContracts.Update() -> Long
ServiceGroup.AbsEntry : Long [R]
ServiceGroup.Description : String [R/W]
ServiceGroup.ServiceGroupCode : String [R/W]
ServiceGroup.FromXMLFile(ByVal bstrFileName As String)
ServiceGroup.FromXMLString(ByVal bstrXML As String)
ServiceGroup.GetXMLSchema() -> String
ServiceGroup.ToXMLFile(ByVal bstrFileName As String)
ServiceGroup.ToXMLString() -> String
ServiceGroupParams.AbsEntry : Long [R/W]
ServiceGroupParams.ServiceGroupCode : String [R]
ServiceGroupParams.FromXMLFile(ByVal bstrFileName As String)
ServiceGroupParams.FromXMLString(ByVal bstrXML As String)
ServiceGroupParams.GetXMLSchema() -> String
ServiceGroupParams.ToXMLFile(ByVal bstrFileName As String)
ServiceGroupParams.ToXMLString() -> String
ServiceGroupsParams.Count : Long [R]
ServiceGroupsParams.Add() -> ServiceGroupParams
ServiceGroupsParams.GetXMLSchema() -> String
ServiceGroupsParams.Item(ByVal vtIndex As Variant) -> ServiceGroupParams
ServiceGroupsParams.ToXMLFile(ByVal bstrFileName As String)
ServiceGroupsParams.ToXMLString() -> String
ServiceGroupsService.AddServiceGroup(ByVal pIServiceGroup As ServiceGroup) -> ServiceGroupParams
ServiceGroupsService.DeleteServiceGroup(ByVal pIServiceGroupParams As ServiceGroupParams)
ServiceGroupsService.GetDataInterface(ByVal enumMSDI As ServiceGroupsServiceDataInterfaces) -> Object
ServiceGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ServiceGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ServiceGroupsService.GetServiceGroup(ByVal pIServiceGroupParams As ServiceGroupParams) -> ServiceGroup
ServiceGroupsService.GetServiceGroupList() -> ServiceGroupsParams
ServiceGroupsService.UpdateServiceGroup(ByVal pIServiceGroup As ServiceGroup)
ServiceTaxPostingParams.DocEntry : Long [R/W]
ServiceTaxPostingParams.FromXMLFile(ByVal bstrFileName As String)
ServiceTaxPostingParams.FromXMLString(ByVal bstrXML As String)
ServiceTaxPostingParams.GetXMLSchema() -> String
ServiceTaxPostingParams.ToXMLFile(ByVal bstrFileName As String)
ServiceTaxPostingParams.ToXMLString() -> String
ServiceTaxPostingParamsCollection.Count : Long [R]
ServiceTaxPostingParamsCollection.Add() -> ServiceTaxPostingParams
ServiceTaxPostingParamsCollection.GetXMLSchema() -> String
ServiceTaxPostingParamsCollection.Item(ByVal vtIndex As Variant) -> ServiceTaxPostingParams
ServiceTaxPostingParamsCollection.ToXMLFile(ByVal bstrFileName As String)
ServiceTaxPostingParamsCollection.ToXMLString() -> String
ServiceTaxPostingService.GetDataInterface(ByVal enumMSDI As ServiceTaxPostingServiceDataInterfaces) -> Object
ServiceTaxPostingService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ServiceTaxPostingService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ServiceTaxPostingService.GetTaxableDeliveries() -> ServiceTaxPostingParamsCollection
ServiceTaxPostingService.PostServiceTax(ByVal pIServiceTaxPostingParams As ServiceTaxPostingParams)
ShippingTypes.Browser : DataBrowser [R]
ShippingTypes.Code : Long [R]
ShippingTypes.Name : String [R/W]
ShippingTypes.UserFields : UserFields [R]
ShippingTypes.Website : String [R/W]
ShippingTypes.Add() -> Long
ShippingTypes.GetAsXML() -> String
ShippingTypes.GetByKey(ByVal lCode As Long) -> Boolean
ShippingTypes.Remove() -> Long
ShippingTypes.SaveToFile(ByVal bstrFileName As String)
ShippingTypes.SaveXML(ByRef pbstrFileName As String)
ShippingTypes.Update() -> Long
ShowDifferenceParams.LogInstance : Long [R/W]
ShowDifferenceParams.LogInstance2 : Long [R/W]
ShowDifferenceParams.Object : BoChangeLogEnum [R/W]
ShowDifferenceParams.PrimaryKey : String [R/W]
ShowDifferenceParams.UDOObjectCode : String [R/W]
ShowDifferenceParams.FromXMLFile(ByVal bstrFileName As String)
ShowDifferenceParams.FromXMLString(ByVal bstrXML As String)
ShowDifferenceParams.GetXMLSchema() -> String
ShowDifferenceParams.ToXMLFile(ByVal bstrFileName As String)
ShowDifferenceParams.ToXMLString() -> String
SingleUserConnection.Action : SingleUserConnectionActionEnum [R/W]
SingleUserConnection.Code : Long [R]
SingleUserConnection.FromXMLFile(ByVal bstrFileName As String)
SingleUserConnection.FromXMLString(ByVal bstrXML As String)
SingleUserConnection.GetXMLSchema() -> String
SingleUserConnection.ToXMLFile(ByVal bstrFileName As String)
SingleUserConnection.ToXMLString() -> String
SingleUserConnectionParams.Code : Long [R/W]
SingleUserConnectionParams.FromXMLFile(ByVal bstrFileName As String)
SingleUserConnectionParams.FromXMLString(ByVal bstrXML As String)
SingleUserConnectionParams.GetXMLSchema() -> String
SingleUserConnectionParams.ToXMLFile(ByVal bstrFileName As String)
SingleUserConnectionParams.ToXMLString() -> String
SingleUserConnectionService.Get(ByVal pISingleUserConnectioParams As SingleUserConnectionParams) -> SingleUserConnection
SingleUserConnectionService.GetDataInterface(ByVal enumMSDI As SingleUserConnectionServiceDataInterfaces) -> Object
SingleUserConnectionService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
SingleUserConnectionService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
SingleUserConnectionService.Update(ByVal pISingleUserConnection As SingleUserConnection)
SNBLines.AdmissionDate : Date [R]
SNBLines.BaseLine : Long [R/W]
SNBLines.Count : Long [R]
SNBLines.DebitCredit : Double [R/W]
SNBLines.ExpirationDate : Date [R]
SNBLines.LotNumber : String [R]
SNBLines.ManufactureNumber : String [R]
SNBLines.NewCost : Double [R/W]
SNBLines.SnbAbsEntry : Long [R/W]
SNBLines.SystemNumber : Long [R]
SNBLines.Add()
SNBLines.SetCurrentLine(ByVal LineNum As Long)
SpecialPrices.AutoUpdate : BoYesNoEnum [R/W]
SpecialPrices.Browser : DataBrowser [R]
SpecialPrices.CardCode : String [R/W]
SpecialPrices.Currency : String [R/W]
SpecialPrices.DiscountPercent : Double [R/W]
SpecialPrices.ItemCode : String [R/W]
SpecialPrices.Price : Double [R/W]
SpecialPrices.PriceListNum : Long [R/W]
SpecialPrices.SourcePrice : SourceCurrencyEnum [R/W]
SpecialPrices.SpecialPricesDataAreas : SpecialPricesDataAreas [R]
SpecialPrices.UserFields : UserFields [R]
SpecialPrices.Valid : BoYesNoEnum [R/W]
SpecialPrices.ValidFrom : Date [R/W]
SpecialPrices.ValidTo : Date [R/W]
SpecialPrices.Add() -> Long
SpecialPrices.GetAsXML() -> String
SpecialPrices.GetByKey(ByVal ItemCode As String, ByVal CardCode As String) -> Boolean
SpecialPrices.GetByKeyDiscounts(ByVal ItemCode As String, ByVal PriceListNum As Long) -> Boolean
SpecialPrices.Remove() -> Long
SpecialPrices.SaveToFile(ByVal FileName As String)
SpecialPrices.SaveXML(ByRef FileName As String)
SpecialPrices.Update() -> Long
SpecialPricesDataAreas.AutoUpdate : BoYesNoEnum [R/W]
SpecialPricesDataAreas.BPCode : String [R]
SpecialPricesDataAreas.Count : Long [R]
SpecialPricesDataAreas.DateFrom : Date [R/W]
SpecialPricesDataAreas.Dateto : Date [R/W]
SpecialPricesDataAreas.Discount : Double [R/W]
SpecialPricesDataAreas.ItemNo : String [R]
SpecialPricesDataAreas.PriceCurrency : String [R/W]
SpecialPricesDataAreas.PriceListNo : Long [R/W]
SpecialPricesDataAreas.RowNumber : Long [R]
SpecialPricesDataAreas.SpecialPrice : Double [R/W]
SpecialPricesDataAreas.SpecialPricesQuantityAreas : SpecialPricesQuantityAreas [R]
SpecialPricesDataAreas.UserFields : UserFields [R]
SpecialPricesDataAreas.Add()
SpecialPricesDataAreas.Delete()
SpecialPricesDataAreas.SetCurrentLine(ByVal LineNum As Long)
SpecialPricesQuantityAreas.BPCode : String [R]
SpecialPricesQuantityAreas.Count : Long [R]
SpecialPricesQuantityAreas.Discountin : Double [R/W]
SpecialPricesQuantityAreas.ItemNo : String [R]
SpecialPricesQuantityAreas.PriceCurrency : String [R/W]
SpecialPricesQuantityAreas.Quantity : Double [R/W]
SpecialPricesQuantityAreas.RowNumber : Long [R]
SpecialPricesQuantityAreas.SPDARowNumber : Long [R]
SpecialPricesQuantityAreas.SpecialPrice : Double [R/W]
SpecialPricesQuantityAreas.UoMEntry : Long [R/W]
SpecialPricesQuantityAreas.UserFields : UserFields [R]
SpecialPricesQuantityAreas.Add()
SpecialPricesQuantityAreas.Delete()
SpecialPricesQuantityAreas.SetCurrentLine(ByVal LineNum As Long)
State.Code : String [R/W]
State.Country : String [R/W]
State.GSTCode : String [R/W]
State.IsUnionTerritory : BoYesNoEnum [R/W]
State.Name : String [R/W]
State.FromXMLFile(ByVal bstrFileName As String)
State.FromXMLString(ByVal bstrXML As String)
State.GetXMLSchema() -> String
State.ToXMLFile(ByVal bstrFileName As String)
State.ToXMLString() -> String
StateParams.Code : String [R/W]
StateParams.Country : String [R/W]
StateParams.Name : String [R]
StateParams.FromXMLFile(ByVal bstrFileName As String)
StateParams.FromXMLString(ByVal bstrXML As String)
StateParams.GetXMLSchema() -> String
StateParams.ToXMLFile(ByVal bstrFileName As String)
StateParams.ToXMLString() -> String
StatesParams.Count : Long [R]
StatesParams.Add() -> StateParams
StatesParams.GetXMLSchema() -> String
StatesParams.Item(ByVal vtIndex As Variant) -> StateParams
StatesParams.ToXMLFile(ByVal bstrFileName As String)
StatesParams.ToXMLString() -> String
StatesService.AddState(ByVal pIState As State) -> StateParams
StatesService.DeleteState(ByVal pIStateParams As StateParams)
StatesService.GetDataInterface(ByVal enumMSDI As StatesServiceDataInterfaces) -> Object
StatesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
StatesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
StatesService.GetState(ByVal pIStateParams As StateParams) -> State
StatesService.GetStateList() -> StatesParams
StatesService.UpdateState(ByVal pIState As State)
StockTaking.Browser : DataBrowser [R]
StockTaking.Counted : Double [R/W]
StockTaking.ItemCode : String [R/W]
StockTaking.UserFields : UserFields [R]
StockTaking.WarehouseCode : String [R/W]
StockTaking.Add() -> Long
StockTaking.GetAsXML() -> String
StockTaking.GetByKey(ByVal bstrItemCode As String, ByVal bstrWhsCode As String) -> Boolean
StockTaking.SaveToFile(ByVal FileName As String)
StockTaking.SaveXML(ByRef FileName As String)
StockTransfer.Address : String [R/W]
StockTransfer.ATDocumentType : String [R/W]
StockTransfer.AttachmentEntry : Long [R/W]
StockTransfer.AuthorizationCode : String [R/W]
StockTransfer.AuthorizationStatus : StockTransferAuthorizationStatusEnum [R]
StockTransfer.BPLID : Long [R]
StockTransfer.BPLName : String [R]
StockTransfer.Browser : DataBrowser [R]
StockTransfer.CardCode : String [R/W]
StockTransfer.CardName : String [R/W]
StockTransfer.Comments : String [R/W]
StockTransfer.ContactPerson : Long [R/W]
StockTransfer.CreationDate : Date [R]
StockTransfer.DocDate : Date [R/W]
StockTransfer.DocEntry : Long [R]
StockTransfer.DocNum : Long [R]
StockTransfer.DocObjectCode : BoObjectTypes [R/W]
StockTransfer.DocumentReferences : Document_DocumentReferences [R]
StockTransfer.DocumentStatus : BoStatus [R]
StockTransfer.DueDate : Date [R/W]
StockTransfer.EDocExportFormat : Long [R/W]
StockTransfer.ElecCommMessage : String [R]
StockTransfer.ElecCommStatus : ElecCommStatusEnum [R/W]
StockTransfer.ElectronicProtocols : ElectronicProtocols [R]
StockTransfer.EndDeliveryDate : Date [R/W]
StockTransfer.EndDeliveryTime : Date [R/W]
StockTransfer.FinancialPeriod : Long [R]
StockTransfer.FolioNumber : Long [R/W]
StockTransfer.FolioNumberFrom : Long [R/W]
StockTransfer.FolioNumberTo : Long [R/W]
StockTransfer.FolioPrefixString : String [R/W]
StockTransfer.FromWarehouse : String [R/W]
StockTransfer.JournalMemo : String [R/W]
StockTransfer.LastPageFolioNumber : Long [R]
StockTransfer.Letter : FolioLetterEnum [R/W]
StockTransfer.Lines : StockTransfer_Lines [R]
StockTransfer.PointOfIssueCode : String [R/W]
StockTransfer.PriceList : Long [R/W]
StockTransfer.Printed : BoYesNoEnum [R]
StockTransfer.Reference1 : String [R/W]
StockTransfer.Reference2 : String [R/W]
StockTransfer.SalesPersonCode : Long [R/W]
StockTransfer.SAPPassport : String [R]
StockTransfer.Series : Long [R/W]
StockTransfer.ShipToCode : String [R/W]
StockTransfer.StartDeliveryDate : Date [R/W]
StockTransfer.StartDeliveryTime : Date [R/W]
StockTransfer.StockTransfer_ApprovalRequests : StockTransfer_ApprovalRequests [R]
StockTransfer.TaxDate : Date [R/W]
StockTransfer.TaxExtension : StockTransfer_TaxExtension [R]
StockTransfer.ToWarehouse : String [R/W]
StockTransfer.TransNum : Long [R]
StockTransfer.UpdateDate : Date [R]
StockTransfer.UserFields : UserFields [R]
StockTransfer.VATRegNum : String [R]
StockTransfer.VehiclePlate : String [R/W]
StockTransfer.Add() -> Long
StockTransfer.Cancel() -> Long
StockTransfer.Close() -> Long
StockTransfer.GetApprovalTemplates() -> Long
StockTransfer.GetAsXML() -> String
StockTransfer.GetByKey(ByVal AbsEntry As Long) -> Boolean
StockTransfer.HandleApprovalRequest() -> Long
StockTransfer.Remove() -> Long
StockTransfer.SaveDraftToDocument() -> Long
StockTransfer.SaveToFile(ByVal FileName As String)
StockTransfer.SaveXML(ByRef FileName As String)
StockTransfer.Update() -> Long
StockTransfer_ApprovalRequests.ActiveForUpdate : BoYesNoEnum [R]
StockTransfer_ApprovalRequests.ApprovalTemplatesID : Long [R]
StockTransfer_ApprovalRequests.ApprovalTemplatesName : String [R]
StockTransfer_ApprovalRequests.Count : Long [R]
StockTransfer_ApprovalRequests.Remarks : String [R/W]
StockTransfer_ApprovalRequests.SetCurrentLine(ByVal LineNum As Long)
StockTransfer_Lines.BaseEntry : Long [R/W]
StockTransfer_Lines.BaseLine : Long [R/W]
StockTransfer_Lines.BaseType : InvBaseDocTypeEnum [R/W]
StockTransfer_Lines.BatchNumbers : BatchNumbers [R]
StockTransfer_Lines.BinAllocations : StockTransferLinesBinAllocations [R]
StockTransfer_Lines.CCDNumbers : CCDNumbers [R]
StockTransfer_Lines.Count : Long [R]
StockTransfer_Lines.Currency : String [R/W]
StockTransfer_Lines.DiscountPercent : Double [R/W]
StockTransfer_Lines.DistributionRule : String [R/W]
StockTransfer_Lines.DistributionRule2 : String [R/W]
StockTransfer_Lines.DistributionRule3 : String [R/W]
StockTransfer_Lines.DistributionRule4 : String [R/W]
StockTransfer_Lines.DistributionRule5 : String [R/W]
StockTransfer_Lines.DocEntry : Long [R]
StockTransfer_Lines.Factor : Double [R/W]
StockTransfer_Lines.Factor2 : Double [R/W]
StockTransfer_Lines.Factor3 : Double [R/W]
StockTransfer_Lines.Factor4 : Double [R/W]
StockTransfer_Lines.FromWarehouseCode : String [R/W]
StockTransfer_Lines.InventoryQuantity : Double [R/W]
StockTransfer_Lines.ItemCode : String [R/W]
StockTransfer_Lines.ItemDescription : String [R/W]
StockTransfer_Lines.LineNum : Long [R]
StockTransfer_Lines.LineStatus : BoStatus [R]
StockTransfer_Lines.MeasureUnit : String [R/W]
StockTransfer_Lines.Price : Double [R/W]
StockTransfer_Lines.ProjectCode : String [R/W]
StockTransfer_Lines.Quantity : Double [R/W]
StockTransfer_Lines.Rate : Double [R/W]
StockTransfer_Lines.RemainingOpenInventoryQuantity : Double [R]
StockTransfer_Lines.RemainingOpenQuantity : Double [R]
StockTransfer_Lines.SerialNumber : String [R/W]
StockTransfer_Lines.SerialNumbers : SerialNumbers [R]
StockTransfer_Lines.UnitPrice : Double [R/W]
StockTransfer_Lines.UnitsOfMeasurment : Double [R/W]
StockTransfer_Lines.UoMCode : String [R]
StockTransfer_Lines.UoMEntry : Long [R/W]
StockTransfer_Lines.UseBaseUnits : BoYesNoEnum [R/W]
StockTransfer_Lines.UserFields : UserFields [R]
StockTransfer_Lines.VendorNum : String [R/W]
StockTransfer_Lines.WarehouseCode : String [R/W]
StockTransfer_Lines.Add()
StockTransfer_Lines.Delete()
StockTransfer_Lines.SetCurrentLine(ByVal LineNum As Long)
StockTransfer_TaxExtension.FormNumber : String [R/W]
StockTransfer_TaxExtension.SupportVAT : BoYesNoEnum [R/W]
StockTransfer_TaxExtension.TransactionCategory : String [R/W]
StockTransfer_TaxExtension.UserFields : UserFields [R]
StockTransferLinesBinAllocations.AllowNegativeQuantity : BoYesNoEnum [R/W]
StockTransferLinesBinAllocations.BaseLineNumber : Long [R/W]
StockTransferLinesBinAllocations.BinAbsEntry : Long [R/W]
StockTransferLinesBinAllocations.BinActionType : BinActionTypeEnum [R/W]
StockTransferLinesBinAllocations.Count : Long [R]
StockTransferLinesBinAllocations.Quantity : Double [R/W]
StockTransferLinesBinAllocations.SerialAndBatchNumbersBaseLine : Long [R/W]
StockTransferLinesBinAllocations.Add()
StockTransferLinesBinAllocations.SetCurrentLine(ByVal LineNum As Long)
TargetGroup.TargetGroupCode : String [R/W]
TargetGroup.TargetGroupName : String [R/W]
TargetGroup.TargetGroupsDetails : TargetGroupsDetails [R]
TargetGroup.TargetGroupType : TargetGroupTypeEnum [R/W]
TargetGroup.FromXMLFile(ByVal bstrFileName As String)
TargetGroup.FromXMLString(ByVal bstrXML As String)
TargetGroup.GetXMLSchema() -> String
TargetGroup.ToXMLFile(ByVal bstrFileName As String)
TargetGroup.ToXMLString() -> String
TargetGroupParams.TargetGroupCode : String [R/W]
TargetGroupParams.TargetGroupName : String [R/W]
TargetGroupParams.FromXMLFile(ByVal bstrFileName As String)
TargetGroupParams.FromXMLString(ByVal bstrXML As String)
TargetGroupParams.GetXMLSchema() -> String
TargetGroupParams.ToXMLFile(ByVal bstrFileName As String)
TargetGroupParams.ToXMLString() -> String
TargetGroupsDetail.ActiveStatus : TargetGroupsDetailStatusEnum [R]
TargetGroupsDetail.Address : String [R]
TargetGroupsDetail.Block : String [R/W]
TargetGroupsDetail.Building : String [R/W]
TargetGroupsDetail.BusinessPartnerCode : String [R/W]
TargetGroupsDetail.BusinessPartnerName : String [R/W]
TargetGroupsDetail.City : String [R/W]
TargetGroupsDetail.ContactPerson : String [R/W]
TargetGroupsDetail.Country : String [R/W]
TargetGroupsDetail.County : String [R/W]
TargetGroupsDetail.E_Mail : String [R/W]
TargetGroupsDetail.Fax : String [R/W]
TargetGroupsDetail.GroupCode : String [R]
TargetGroupsDetail.Industry : String [R]
TargetGroupsDetail.MobilePhone : String [R/W]
TargetGroupsDetail.Position : String [R/W]
TargetGroupsDetail.State : String [R/W]
TargetGroupsDetail.Street : String [R/W]
TargetGroupsDetail.TargetGroupCode : String [R]
TargetGroupsDetail.Telephone : String [R/W]
TargetGroupsDetail.Title : String [R/W]
TargetGroupsDetail.ZipCode : String [R/W]
TargetGroupsDetail.FromXMLFile(ByVal bstrFileName As String)
TargetGroupsDetail.FromXMLString(ByVal bstrXML As String)
TargetGroupsDetail.GetXMLSchema() -> String
TargetGroupsDetail.ToXMLFile(ByVal bstrFileName As String)
TargetGroupsDetail.ToXMLString() -> String
TargetGroupsDetails.Count : Long [R]
TargetGroupsDetails.Add() -> TargetGroupsDetail
TargetGroupsDetails.GetXMLSchema() -> String
TargetGroupsDetails.Item(ByVal vtIndex As Variant) -> TargetGroupsDetail
TargetGroupsDetails.Remove(ByVal vtIndex As Variant)
TargetGroupsDetails.ToXMLFile(ByVal bstrFileName As String)
TargetGroupsDetails.ToXMLString() -> String
TargetGroupsParams.Count : Long [R]
TargetGroupsParams.Add() -> TargetGroupParams
TargetGroupsParams.GetXMLSchema() -> String
TargetGroupsParams.Item(ByVal vtIndex As Variant) -> TargetGroupParams
TargetGroupsParams.ToXMLFile(ByVal bstrFileName As String)
TargetGroupsParams.ToXMLString() -> String
TargetGroupsService.Add(ByVal pITargetGroup As TargetGroup) -> TargetGroupParams
TargetGroupsService.Delete(ByVal pITargetGroupParams As TargetGroupParams)
TargetGroupsService.Get(ByVal pITargetGroupParams As TargetGroupParams) -> TargetGroup
TargetGroupsService.GetDataInterface(ByVal enumMSDI As TargetGroupsServiceDataInterfaces) -> Object
TargetGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TargetGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TargetGroupsService.GetList() -> TargetGroupsParams
TargetGroupsService.Update(ByVal pITargetGroup As TargetGroup)
TaxCodeDetermination.BusinessArea : BoBusinessAreaEnum [R/W]
TaxCodeDetermination.Condition1 : BoTCDConditionEnum [R/W]
TaxCodeDetermination.Condition2 : BoTCDConditionEnum [R/W]
TaxCodeDetermination.Condition3 : BoTCDConditionEnum [R/W]
TaxCodeDetermination.Condition4 : BoTCDConditionEnum [R/W]
TaxCodeDetermination.Condition5 : BoTCDConditionEnum [R/W]
TaxCodeDetermination.Description : String [R/W]
TaxCodeDetermination.DocEntry : Long [R]
TaxCodeDetermination.DocumentType : BoTCDDocumentTypeEnum [R/W]
TaxCodeDetermination.FreightHeaderTax : String [R/W]
TaxCodeDetermination.FreightRowTax : String [R/W]
TaxCodeDetermination.LineNumber : Long [R/W]
TaxCodeDetermination.MoneyValue1 : Double [R/W]
TaxCodeDetermination.MoneyValue2 : Double [R/W]
TaxCodeDetermination.MoneyValue3 : Double [R/W]
TaxCodeDetermination.MoneyValue4 : Double [R/W]
TaxCodeDetermination.MoneyValue5 : Double [R/W]
TaxCodeDetermination.NumberValue1 : Long [R/W]
TaxCodeDetermination.NumberValue2 : Long [R/W]
TaxCodeDetermination.NumberValue3 : Long [R/W]
TaxCodeDetermination.NumberValue4 : Long [R/W]
TaxCodeDetermination.NumberValue5 : Long [R/W]
TaxCodeDetermination.StringValue1 : String [R/W]
TaxCodeDetermination.StringValue2 : String [R/W]
TaxCodeDetermination.StringValue3 : String [R/W]
TaxCodeDetermination.StringValue4 : String [R/W]
TaxCodeDetermination.StringValue5 : String [R/W]
TaxCodeDetermination.TaxCode : String [R/W]
TaxCodeDetermination.UDFAlias1 : String [R/W]
TaxCodeDetermination.UDFAlias2 : String [R/W]
TaxCodeDetermination.UDFAlias3 : String [R/W]
TaxCodeDetermination.UDFAlias4 : String [R/W]
TaxCodeDetermination.UDFAlias5 : String [R/W]
TaxCodeDetermination.UDFTable1 : String [R/W]
TaxCodeDetermination.UDFTable2 : String [R/W]
TaxCodeDetermination.UDFTable3 : String [R/W]
TaxCodeDetermination.UDFTable4 : String [R/W]
TaxCodeDetermination.UDFTable5 : String [R/W]
TaxCodeDetermination.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDetermination.FromXMLString(ByVal bstrXML As String)
TaxCodeDetermination.GetXMLSchema() -> String
TaxCodeDetermination.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDetermination.ToXMLString() -> String
TaxCodeDeterminationParams.DocEntry : Long [R/W]
TaxCodeDeterminationParams.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationParams.FromXMLString(ByVal bstrXML As String)
TaxCodeDeterminationParams.GetXMLSchema() -> String
TaxCodeDeterminationParams.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationParams.ToXMLString() -> String
TaxCodeDeterminationsParams.Count : Long [R]
TaxCodeDeterminationsParams.Add() -> TaxCodeDeterminationParams
TaxCodeDeterminationsParams.GetXMLSchema() -> String
TaxCodeDeterminationsParams.Item(ByVal vtIndex As Variant) -> TaxCodeDeterminationParams
TaxCodeDeterminationsParams.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationsParams.ToXMLString() -> String
TaxCodeDeterminationsService.AddTaxCodeDetermination(ByVal pITaxCodeDetermination As TaxCodeDetermination) -> TaxCodeDeterminationParams
TaxCodeDeterminationsService.DeleteTaxCodeDetermination(ByVal pITaxCodeDeterminationParams As TaxCodeDeterminationParams)
TaxCodeDeterminationsService.GetDataInterface(ByVal enumMSDI As TaxCodeDeterminationsServiceDataInterfaces) -> Object
TaxCodeDeterminationsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TaxCodeDeterminationsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TaxCodeDeterminationsService.GetTaxCodeDetermination(ByVal pITaxCodeDeterminationParams As TaxCodeDeterminationParams) -> TaxCodeDetermination
TaxCodeDeterminationsService.GetTaxCodeDeterminationList() -> TaxCodeDeterminationsParams
TaxCodeDeterminationsService.UpdateTaxCodeDetermination(ByVal pITaxCodeDetermination As TaxCodeDetermination)
TaxCodeDeterminationsTCDParams.Count : Long [R]
TaxCodeDeterminationsTCDParams.Add() -> TaxCodeDeterminationTCDParams
TaxCodeDeterminationsTCDParams.GetXMLSchema() -> String
TaxCodeDeterminationsTCDParams.Item(ByVal vtIndex As Variant) -> TaxCodeDeterminationTCDParams
TaxCodeDeterminationsTCDParams.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationsTCDParams.ToXMLString() -> String
TaxCodeDeterminationsTCDService.GetDataInterface(ByVal enumMSDI As TaxCodeDeterminationsTCDServiceDataInterfaces) -> Object
TaxCodeDeterminationsTCDService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TaxCodeDeterminationsTCDService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TaxCodeDeterminationsTCDService.GetTaxCodeDeterminationTCD(ByVal pITaxCodeDeterminationTCDParams As TaxCodeDeterminationTCDParams) -> TaxCodeDeterminationTCD
TaxCodeDeterminationsTCDService.GetTaxCodeDeterminationTCDList() -> TaxCodeDeterminationsTCDParams
TaxCodeDeterminationsTCDService.UpdateTaxCodeDeterminationTCD(ByVal pITaxCodeDeterminationTCD As TaxCodeDeterminationTCD)
TaxCodeDeterminationTCD.AbsId : Long [R]
TaxCodeDeterminationTCD.DefaultPurchase : String [R/W]
TaxCodeDeterminationTCD.DefaultSales : String [R/W]
TaxCodeDeterminationTCD.DefaultSalesAndPurchaseByUsages : TaxCodeDeterminationTCDByUsages [R]
TaxCodeDeterminationTCD.DefaultSalesAndPurchaseWTs : TaxCodeDeterminationTCDDefaultWTs [R]
TaxCodeDeterminationTCD.KeyFields : TaxCodeDeterminationTCDKeyFields [R]
TaxCodeDeterminationTCD.Type : TaxCodeDeterminationTCDTypeEnum [R]
TaxCodeDeterminationTCD.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCD.FromXMLString(ByVal bstrXML As String)
TaxCodeDeterminationTCD.GetXMLSchema() -> String
TaxCodeDeterminationTCD.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCD.ToXMLString() -> String
TaxCodeDeterminationTCDByUsage.AbsId : Long [R]
TaxCodeDeterminationTCDByUsage.FreightTaxCode : String [R/W]
TaxCodeDeterminationTCDByUsage.PurchaseTaxCode : String [R/W]
TaxCodeDeterminationTCDByUsage.TaxCode : String [R/W]
TaxCodeDeterminationTCDByUsage.Type : TaxCodeDeterminationTCDByUsageTypeEnum [R/W]
TaxCodeDeterminationTCDByUsage.UsageCode : Long [R/W]
TaxCodeDeterminationTCDByUsage.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDByUsage.FromXMLString(ByVal bstrXML As String)
TaxCodeDeterminationTCDByUsage.GetXMLSchema() -> String
TaxCodeDeterminationTCDByUsage.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDByUsage.ToXMLString() -> String
TaxCodeDeterminationTCDByUsages.Count : Long [R]
TaxCodeDeterminationTCDByUsages.Add() -> TaxCodeDeterminationTCDByUsage
TaxCodeDeterminationTCDByUsages.GetXMLSchema() -> String
TaxCodeDeterminationTCDByUsages.Item(ByVal vtIndex As Variant) -> TaxCodeDeterminationTCDByUsage
TaxCodeDeterminationTCDByUsages.Remove(ByVal vtIndex As Variant)
TaxCodeDeterminationTCDByUsages.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDByUsages.ToXMLString() -> String
TaxCodeDeterminationTCDDefaultWT.AbsId : Long [R]
TaxCodeDeterminationTCDDefaultWT.Type : TaxCodeDeterminationTCDDefaultWTTypeEnum [R/W]
TaxCodeDeterminationTCDDefaultWT.WTCode : String [R/W]
TaxCodeDeterminationTCDDefaultWT.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDDefaultWT.FromXMLString(ByVal bstrXML As String)
TaxCodeDeterminationTCDDefaultWT.GetXMLSchema() -> String
TaxCodeDeterminationTCDDefaultWT.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDDefaultWT.ToXMLString() -> String
TaxCodeDeterminationTCDDefaultWTs.Count : Long [R]
TaxCodeDeterminationTCDDefaultWTs.Add() -> TaxCodeDeterminationTCDDefaultWT
TaxCodeDeterminationTCDDefaultWTs.GetXMLSchema() -> String
TaxCodeDeterminationTCDDefaultWTs.Item(ByVal vtIndex As Variant) -> TaxCodeDeterminationTCDDefaultWT
TaxCodeDeterminationTCDDefaultWTs.Remove(ByVal vtIndex As Variant)
TaxCodeDeterminationTCDDefaultWTs.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDDefaultWTs.ToXMLString() -> String
TaxCodeDeterminationTCDKeyField.AbsId : Long [R]
TaxCodeDeterminationTCDKeyField.Description : String [R/W]
TaxCodeDeterminationTCDKeyField.KeyField1 : Long [R/W]
TaxCodeDeterminationTCDKeyField.KeyField2 : Long [R/W]
TaxCodeDeterminationTCDKeyField.KeyField3 : Long [R/W]
TaxCodeDeterminationTCDKeyField.KeyField4 : Long [R/W]
TaxCodeDeterminationTCDKeyField.LegalText : String [R/W]
TaxCodeDeterminationTCDKeyField.Priority : Long [R/W]
TaxCodeDeterminationTCDKeyField.UDFAlias1 : String [R/W]
TaxCodeDeterminationTCDKeyField.UDFAlias2 : String [R/W]
TaxCodeDeterminationTCDKeyField.UDFAlias3 : String [R/W]
TaxCodeDeterminationTCDKeyField.UDFAlias4 : String [R/W]
TaxCodeDeterminationTCDKeyField.UDFTable1 : String [R/W]
TaxCodeDeterminationTCDKeyField.UDFTable2 : String [R/W]
TaxCodeDeterminationTCDKeyField.UDFTable3 : String [R/W]
TaxCodeDeterminationTCDKeyField.UDFTable4 : String [R/W]
TaxCodeDeterminationTCDKeyField.Values : TaxCodeDeterminationTCDValues [R]
TaxCodeDeterminationTCDKeyField.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDKeyField.FromXMLString(ByVal bstrXML As String)
TaxCodeDeterminationTCDKeyField.GetXMLSchema() -> String
TaxCodeDeterminationTCDKeyField.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDKeyField.ToXMLString() -> String
TaxCodeDeterminationTCDKeyFields.Count : Long [R]
TaxCodeDeterminationTCDKeyFields.Add() -> TaxCodeDeterminationTCDKeyField
TaxCodeDeterminationTCDKeyFields.GetXMLSchema() -> String
TaxCodeDeterminationTCDKeyFields.Item(ByVal vtIndex As Variant) -> TaxCodeDeterminationTCDKeyField
TaxCodeDeterminationTCDKeyFields.Remove(ByVal vtIndex As Variant)
TaxCodeDeterminationTCDKeyFields.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDKeyFields.ToXMLString() -> String
TaxCodeDeterminationTCDParams.AbsId : Long [R/W]
TaxCodeDeterminationTCDParams.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDParams.FromXMLString(ByVal bstrXML As String)
TaxCodeDeterminationTCDParams.GetXMLSchema() -> String
TaxCodeDeterminationTCDParams.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDParams.ToXMLString() -> String
TaxCodeDeterminationTCDPeriod.AbsId : Long [R]
TaxCodeDeterminationTCDPeriod.ByUsages : TaxCodeDeterminationTCDByUsages [R]
TaxCodeDeterminationTCDPeriod.EffectFrom : Date [R/W]
TaxCodeDeterminationTCDPeriod.EffectTo : Date [R/W]
TaxCodeDeterminationTCDPeriod.TaxCode : String [R/W]
TaxCodeDeterminationTCDPeriod.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDPeriod.FromXMLString(ByVal bstrXML As String)
TaxCodeDeterminationTCDPeriod.GetXMLSchema() -> String
TaxCodeDeterminationTCDPeriod.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDPeriod.ToXMLString() -> String
TaxCodeDeterminationTCDPeriods.Count : Long [R]
TaxCodeDeterminationTCDPeriods.Add() -> TaxCodeDeterminationTCDPeriod
TaxCodeDeterminationTCDPeriods.GetXMLSchema() -> String
TaxCodeDeterminationTCDPeriods.Item(ByVal vtIndex As Variant) -> TaxCodeDeterminationTCDPeriod
TaxCodeDeterminationTCDPeriods.Remove(ByVal vtIndex As Variant)
TaxCodeDeterminationTCDPeriods.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDPeriods.ToXMLString() -> String
TaxCodeDeterminationTCDValue.AbsId : Long [R]
TaxCodeDeterminationTCDValue.DefaultWTs : TaxCodeDeterminationTCDDefaultWTs [R]
TaxCodeDeterminationTCDValue.DispOrder : Long [R/W]
TaxCodeDeterminationTCDValue.Periods : TaxCodeDeterminationTCDPeriods [R]
TaxCodeDeterminationTCDValue.Value1 : String [R/W]
TaxCodeDeterminationTCDValue.Value2 : String [R/W]
TaxCodeDeterminationTCDValue.Value3 : String [R/W]
TaxCodeDeterminationTCDValue.Value4 : String [R/W]
TaxCodeDeterminationTCDValue.FromXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDValue.FromXMLString(ByVal bstrXML As String)
TaxCodeDeterminationTCDValue.GetXMLSchema() -> String
TaxCodeDeterminationTCDValue.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDValue.ToXMLString() -> String
TaxCodeDeterminationTCDValues.Count : Long [R]
TaxCodeDeterminationTCDValues.Add() -> TaxCodeDeterminationTCDValue
TaxCodeDeterminationTCDValues.GetXMLSchema() -> String
TaxCodeDeterminationTCDValues.Item(ByVal vtIndex As Variant) -> TaxCodeDeterminationTCDValue
TaxCodeDeterminationTCDValues.Remove(ByVal vtIndex As Variant)
TaxCodeDeterminationTCDValues.ToXMLFile(ByVal bstrFileName As String)
TaxCodeDeterminationTCDValues.ToXMLString() -> String
TaxDefinitions.Effectivefrom : Date [R/W]
TaxDefinitions.Rate : Double [R/W]
TaxDefinitions.UserFields : UserFields [R]
TaxDefinitions.Add()
TaxDefinitions.Delete()
TaxDefinitions.SetCurrentLine(ByVal LineNum As Long)
TaxExtension.BillOfEntryDate : Date [R/W]
TaxExtension.BillOfEntryNo : String [R/W]
TaxExtension.BlockB : String [R/W]
TaxExtension.BlockS : String [R/W]
TaxExtension.BoEValue : Double [R/W]
TaxExtension.Brand : String [R/W]
TaxExtension.BuildingB : String [R/W]
TaxExtension.BuildingS : String [R/W]
TaxExtension.Carrier : String [R/W]
TaxExtension.CityB : String [R/W]
TaxExtension.CityS : String [R/W]
TaxExtension.ClaimRefund : BoYesNoEnum [R/W]
TaxExtension.CountryB : String [R/W]
TaxExtension.CountryS : String [R/W]
TaxExtension.County : String [R/W]
TaxExtension.CountyB : String [R/W]
TaxExtension.CountyS : String [R/W]
TaxExtension.DifferentialOfTaxRate : Long [R/W]
TaxExtension.DocEntry : Long [R]
TaxExtension.GlobalLocationNumberB : String [R/W]
TaxExtension.GlobalLocationNumberS : String [R/W]
TaxExtension.GrossWeight : Double [R/W]
TaxExtension.ImportOrExport : BoYesNoEnum [R/W]
TaxExtension.ImportOrExportType : ImportOrExportTypeEnum [R/W]
TaxExtension.Incoterms : String [R/W]
TaxExtension.IsIGSTAccount : BoYesNoEnum [R/W]
TaxExtension.MainUsage : Long [R/W]
TaxExtension.NetWeight : Double [R/W]
TaxExtension.NFRef : String [R/W]
TaxExtension.OriginalBillOfEntryDate : Date [R/W]
TaxExtension.OriginalBillOfEntryNo : String [R/W]
TaxExtension.PackDescription : String [R/W]
TaxExtension.PackQuantity : Long [R/W]
TaxExtension.PortCode : String [R/W]
TaxExtension.ShipUnitNo : Long [R/W]
TaxExtension.State : String [R/W]
TaxExtension.StateB : String [R/W]
TaxExtension.StateS : String [R/W]
TaxExtension.StreetB : String [R/W]
TaxExtension.StreetS : String [R/W]
TaxExtension.TaxId0 : String [R/W]
TaxExtension.TaxId1 : String [R/W]
TaxExtension.TaxId12 : String [R/W]
TaxExtension.TaxId13 : String [R/W]
TaxExtension.TaxId14 : String [R/W]
TaxExtension.TaxId2 : String [R/W]
TaxExtension.TaxId3 : String [R/W]
TaxExtension.TaxId4 : String [R/W]
TaxExtension.TaxId5 : String [R/W]
TaxExtension.TaxId6 : String [R/W]
TaxExtension.TaxId7 : String [R/W]
TaxExtension.TaxId8 : String [R/W]
TaxExtension.TaxId9 : String [R/W]
TaxExtension.UserFields : UserFields [R]
TaxExtension.Vehicle : String [R/W]
TaxExtension.VehicleState : String [R/W]
TaxExtension.ZipCodeB : String [R/W]
TaxExtension.ZipCodeS : String [R/W]
TaxInvoice_DocumentReferences.CardCode : String [R/W]
TaxInvoice_DocumentReferences.Count : Long [R]
TaxInvoice_DocumentReferences.DocEntry : Long [R]
TaxInvoice_DocumentReferences.ExternalReferencedDocNumber : String [R/W]
TaxInvoice_DocumentReferences.IssueDate : Date [R/W]
TaxInvoice_DocumentReferences.LineNumber : Long [R]
TaxInvoice_DocumentReferences.ReferencedDocEntry : Long [R/W]
TaxInvoice_DocumentReferences.ReferencedDocNumber : Long [R]
TaxInvoice_DocumentReferences.ReferencedObjectType : ReferencedObjectTypeEnum [R/W]
TaxInvoice_DocumentReferences.Remark : String [R/W]
TaxInvoice_DocumentReferences.Add()
TaxInvoice_DocumentReferences.SetCurrentLine(ByVal LineNum As Long)
TaxInvoice_Lines.BaseEntry : Long [R]
TaxInvoice_Lines.BaseType : BoTaxInvoiceTypes [R]
TaxInvoice_Lines.Count : Long [R]
TaxInvoice_Lines.LineNum : Long [R]
TaxInvoice_Lines.Reference : Long [R/W]
TaxInvoice_Lines.UserFields : UserFields [R]
TaxInvoice_Lines.Add()
TaxInvoice_Lines.SetCurrentLine(ByVal LineNum As Long)
TaxInvoice_LinkedDownPayments.AmountToDraw : Double [R]
TaxInvoice_LinkedDownPayments.AmountToDrawFC : Double [R]
TaxInvoice_LinkedDownPayments.AmountToDrawSC : Double [R]
TaxInvoice_LinkedDownPayments.Count : Long [R]
TaxInvoice_LinkedDownPayments.DocCurrency : String [R]
TaxInvoice_LinkedDownPayments.DocEntry : Long [R]
TaxInvoice_LinkedDownPayments.DownPaymentEntry : Long [R]
TaxInvoice_LinkedDownPayments.DownPaymentNum : Long [R]
TaxInvoice_LinkedDownPayments.DownPaymentType : Long [R]
TaxInvoice_LinkedDownPayments.GrossAmountToDraw : Double [R]
TaxInvoice_LinkedDownPayments.GrossAmountToDrawFC : Double [R]
TaxInvoice_LinkedDownPayments.GrossAmountToDrawSC : Double [R]
TaxInvoice_LinkedDownPayments.LineNum : Long [R]
TaxInvoice_LinkedDownPayments.PaymentEntry : Long [R]
TaxInvoice_LinkedDownPayments.PaymentNum : Long [R]
TaxInvoice_LinkedDownPayments.PaymentTaxDate : Date [R]
TaxInvoice_LinkedDownPayments.PaymentType : Long [R]
TaxInvoice_LinkedDownPayments.Tax : Double [R]
TaxInvoice_LinkedDownPayments.TaxFC : Double [R]
TaxInvoice_LinkedDownPayments.TaxSC : Double [R]
TaxInvoice_LinkedDownPayments.TransferDate : Date [R]
TaxInvoice_LinkedDownPayments.TransferReference : String [R]
TaxInvoice_LinkedDownPayments.SetCurrentLine(ByVal LineNum As Long)
TaxInvoice_OperationCodes.BaseEntry : Long [R]
TaxInvoice_OperationCodes.Count : Long [R]
TaxInvoice_OperationCodes.LineNum : Long [R/W]
TaxInvoice_OperationCodes.OpCode : Long [R/W]
TaxInvoice_OperationCodes.UserFields : UserFields [R]
TaxInvoice_OperationCodes.Add()
TaxInvoice_OperationCodes.SetCurrentLine(ByVal LineNum As Long)
TaxInvoiceReport.BaseAmount : Double [R]
TaxInvoiceReport.BPCode : String [R]
TaxInvoiceReport.BPName : String [R]
TaxInvoiceReport.BusinessPlace : Long [R]
TaxInvoiceReport.Canceled : String [R]
TaxInvoiceReport.Date : Date [R]
TaxInvoiceReport.ETaxNo : String [R/W]
TaxInvoiceReport.ETaxWebSite : Long [R/W]
TaxInvoiceReport.NTSApproval : TaxInvoiceReportNTSApprovedEnum [R/W]
TaxInvoiceReport.NTSApprovalNo : String [R/W]
TaxInvoiceReport.OriginalNTSApprovalNo : String [R/W]
TaxInvoiceReport.Remarks : String [R/W]
TaxInvoiceReport.ReportType : Long [R]
TaxInvoiceReport.TaxAmount : Double [R]
TaxInvoiceReport.TaxInvoiceReportLineCollection : TaxInvoiceReportLineCollection [R]
TaxInvoiceReport.TaxInvoiceReportNumber : String [R]
TaxInvoiceReport.FromXMLFile(ByVal bstrFileName As String)
TaxInvoiceReport.FromXMLString(ByVal bstrXML As String)
TaxInvoiceReport.GetXMLSchema() -> String
TaxInvoiceReport.ToXMLFile(ByVal bstrFileName As String)
TaxInvoiceReport.ToXMLString() -> String
TaxInvoiceReportLine.BaseAmount : Double [R]
TaxInvoiceReportLine.BPCode : String [R]
TaxInvoiceReportLine.BPName : String [R]
TaxInvoiceReportLine.BusinessPlace : Long [R]
TaxInvoiceReportLine.Currency : String [R]
TaxInvoiceReportLine.DocumentDate : Date [R]
TaxInvoiceReportLine.DocumentEntry : Long [R]
TaxInvoiceReportLine.DocumentType : Long [R]
TaxInvoiceReportLine.ItemDescription : String [R]
TaxInvoiceReportLine.ItemNo : String [R]
TaxInvoiceReportLine.ItemPrice : Double [R]
TaxInvoiceReportLine.ItemQuantity : Double [R]
TaxInvoiceReportLine.Legacy : String [R]
TaxInvoiceReportLine.LineNumber : Long [R]
TaxInvoiceReportLine.LineType : TaxInvoiceReportLineTypeEnum [R]
TaxInvoiceReportLine.TaxAmount : Double [R]
TaxInvoiceReportLine.TaxCode : String [R]
TaxInvoiceReportLine.TaxInvoiceReportNumber : String [R]
TaxInvoiceReportLine.FromXMLFile(ByVal bstrFileName As String)
TaxInvoiceReportLine.FromXMLString(ByVal bstrXML As String)
TaxInvoiceReportLine.GetXMLSchema() -> String
TaxInvoiceReportLine.ToXMLFile(ByVal bstrFileName As String)
TaxInvoiceReportLine.ToXMLString() -> String
TaxInvoiceReportLineCollection.Count : Long [R]
TaxInvoiceReportLineCollection.Add() -> TaxInvoiceReportLine
TaxInvoiceReportLineCollection.GetXMLSchema() -> String
TaxInvoiceReportLineCollection.Item(ByVal vtIndex As Variant) -> TaxInvoiceReportLine
TaxInvoiceReportLineCollection.ToXMLFile(ByVal bstrFileName As String)
TaxInvoiceReportLineCollection.ToXMLString() -> String
TaxInvoiceReportParams.TaxInvoiceReportNumber : String [R/W]
TaxInvoiceReportParams.FromXMLFile(ByVal bstrFileName As String)
TaxInvoiceReportParams.FromXMLString(ByVal bstrXML As String)
TaxInvoiceReportParams.GetXMLSchema() -> String
TaxInvoiceReportParams.ToXMLFile(ByVal bstrFileName As String)
TaxInvoiceReportParams.ToXMLString() -> String
TaxInvoiceReportService.CancelTaxInvoiceReport(ByVal pITaxInvoiceReportParams As TaxInvoiceReportParams)
TaxInvoiceReportService.GetDataInterface(ByVal enumMSDI As TaxInvoiceReportServiceDataInterfaces) -> Object
TaxInvoiceReportService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TaxInvoiceReportService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TaxInvoiceReportService.GetTaxInvoiceReport(ByVal pITaxInvoiceReportParams As TaxInvoiceReportParams) -> TaxInvoiceReport
TaxInvoiceReportService.UpdateTaxInvoiceReport(ByVal pITaxInvoiceReport As TaxInvoiceReport)
TaxInvoices.Address : String [R/W]
TaxInvoices.Address2 : String [R/W]
TaxInvoices.AlterationRevision : Long [R/W]
TaxInvoices.BPLID : Long [R]
TaxInvoices.BPLName : String [R]
TaxInvoices.Browser : DataBrowser [R]
TaxInvoices.CancelDate : Date [R]
TaxInvoices.CardCode : String [R/W]
TaxInvoices.Comments : String [R/W]
TaxInvoices.ContactPersonCode : Long [R/W]
TaxInvoices.CreationDate : Date [R]
TaxInvoices.CurrencySource : BoCurrencySources [R/W]
TaxInvoices.CustomerOrVendorName : String [R/W]
TaxInvoices.CustomerOrVendorRefNo : String [R/W]
TaxInvoices.DocCurrency : String [R/W]
TaxInvoices.DocDate : Date [R/W]
TaxInvoices.DocDueDate : Date [R/W]
TaxInvoices.DocEntry : Long [R]
TaxInvoices.DocNum : Long [R]
TaxInvoices.DocType : BoTaxInvoiceTypes [R/W]
TaxInvoices.DocumentReferences : TaxInvoice_DocumentReferences [R]
TaxInvoices.DocumentTotal : Double [R]
TaxInvoices.Lines : TaxInvoice_Lines [R]
TaxInvoices.LinkedDownPayments : TaxInvoice_LinkedDownPayments [R]
TaxInvoices.OperationCodes : TaxInvoice_OperationCodes [R]
TaxInvoices.PaymentRefDate : Date [R/W]
TaxInvoices.PaymentRefNo : String [R/W]
TaxInvoices.Printed : BoYesNoEnum [R]
TaxInvoices.Segment : Long [R]
TaxInvoices.Series : Long [R/W]
TaxInvoices.ShipToCode : String [R/W]
TaxInvoices.TaxDate : Date [R/W]
TaxInvoices.TaxTotal : Double [R]
TaxInvoices.UpdateDate : Date [R]
TaxInvoices.UserFields : UserFields [R]
TaxInvoices.VATRegNum : String [R]
TaxInvoices.Add() -> Long
TaxInvoices.Cancel() -> Long
TaxInvoices.GetAsXML() -> String
TaxInvoices.GetByKey(ByVal DocEntry As Long) -> Boolean
TaxInvoices.SaveToFile(ByVal FileName As String)
TaxInvoices.SaveXML(ByRef FileName As String)
TaxInvoices.Update() -> Long
TaxJurisdictions.Count : Long [R]
TaxJurisdictions.DocEntry : Long [R]
TaxJurisdictions.ExternalCalcTaxAmount : Double [R/W]
TaxJurisdictions.ExternalCalcTaxAmountFC : Double [R/W]
TaxJurisdictions.ExternalCalcTaxAmountSC : Double [R]
TaxJurisdictions.ExternalCalcTaxRate : Double [R/W]
TaxJurisdictions.JurisdictionCode : String [R/W]
TaxJurisdictions.JurisdictionType : Long [R/W]
TaxJurisdictions.LineNumber : Long [R/W]
TaxJurisdictions.RowSequence : Long [R]
TaxJurisdictions.TaxAmount : Double [R/W]
TaxJurisdictions.TaxAmountFC : Double [R]
TaxJurisdictions.TaxAmountSC : Double [R]
TaxJurisdictions.TaxRate : Double [R]
TaxJurisdictions.UserFields : UserFields [R]
TaxJurisdictions.Add()
TaxJurisdictions.SetCurrentLine(ByVal LineNum As Long)
TaxReplStateSubData.IEST : String [R/W]
TaxReplStateSubData.State : String [R/W]
TaxReplStateSubData.FromXMLFile(ByVal bstrFileName As String)
TaxReplStateSubData.FromXMLString(ByVal bstrXML As String)
TaxReplStateSubData.GetXMLSchema() -> String
TaxReplStateSubData.ToXMLFile(ByVal bstrFileName As String)
TaxReplStateSubData.ToXMLString() -> String
TaxReplStateSubParams.State : String [R/W]
TaxReplStateSubParams.FromXMLFile(ByVal bstrFileName As String)
TaxReplStateSubParams.FromXMLString(ByVal bstrXML As String)
TaxReplStateSubParams.GetXMLSchema() -> String
TaxReplStateSubParams.ToXMLFile(ByVal bstrFileName As String)
TaxReplStateSubParams.ToXMLString() -> String
TaxReplStateSubService.Add(ByVal pITaxReplStateSubData As TaxReplStateSubData) -> TaxReplStateSubParams
TaxReplStateSubService.Delete(ByVal pITaxReplStateSubParams As TaxReplStateSubParams)
TaxReplStateSubService.GetByParams(ByVal pITaxReplStateSubParams As TaxReplStateSubParams) -> TaxReplStateSubData
TaxReplStateSubService.GetDataInterface(ByVal enumMSDI As TaxReplStateSubServiceDataInterfaces) -> Object
TaxReplStateSubService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TaxReplStateSubService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TaxReplStateSubService.Update(ByVal pITaxReplStateSubData As TaxReplStateSubData)
TaxReportAccount.Code : String [R/W]
TaxReportAccount.FromXMLFile(ByVal bstrFileName As String)
TaxReportAccount.FromXMLString(ByVal bstrXML As String)
TaxReportAccount.GetXMLSchema() -> String
TaxReportAccount.ToXMLFile(ByVal bstrFileName As String)
TaxReportAccount.ToXMLString() -> String
TaxReportAccounts.Count : Long [R]
TaxReportAccounts.Add() -> TaxReportAccount
TaxReportAccounts.GetXMLSchema() -> String
TaxReportAccounts.Item(ByVal vtIndex As Variant) -> TaxReportAccount
TaxReportAccounts.ToXMLFile(ByVal bstrFileName As String)
TaxReportAccounts.ToXMLString() -> String
TaxReportBusinessPartner.Code : String [R/W]
TaxReportBusinessPartner.FromXMLFile(ByVal bstrFileName As String)
TaxReportBusinessPartner.FromXMLString(ByVal bstrXML As String)
TaxReportBusinessPartner.GetXMLSchema() -> String
TaxReportBusinessPartner.ToXMLFile(ByVal bstrFileName As String)
TaxReportBusinessPartner.ToXMLString() -> String
TaxReportBusinessPartners.Count : Long [R]
TaxReportBusinessPartners.Add() -> TaxReportBusinessPartner
TaxReportBusinessPartners.GetXMLSchema() -> String
TaxReportBusinessPartners.Item(ByVal vtIndex As Variant) -> TaxReportBusinessPartner
TaxReportBusinessPartners.ToXMLFile(ByVal bstrFileName As String)
TaxReportBusinessPartners.ToXMLString() -> String
TaxReportDocument.DocumentType : TaxReportFilterDocumentType [R/W]
TaxReportDocument.FromNumber : Long [R/W]
TaxReportDocument.ToNumber : Long [R/W]
TaxReportDocument.FromXMLFile(ByVal bstrFileName As String)
TaxReportDocument.FromXMLString(ByVal bstrXML As String)
TaxReportDocument.GetXMLSchema() -> String
TaxReportDocument.ToXMLFile(ByVal bstrFileName As String)
TaxReportDocument.ToXMLString() -> String
TaxReportDocuments.Count : Long [R]
TaxReportDocuments.Add() -> TaxReportDocument
TaxReportDocuments.GetXMLSchema() -> String
TaxReportDocuments.Item(ByVal vtIndex As Variant) -> TaxReportDocument
TaxReportDocuments.ToXMLFile(ByVal bstrFileName As String)
TaxReportDocuments.ToXMLString() -> String
TaxReportFilter.AppendixOorPSelection : BoYesNoEnum [R/W]
TaxReportFilter.Cancellation : BoYesNoEnum [R/W]
TaxReportFilter.Code : Long [R]
TaxReportFilter.DeclarationType : TaxReportFilterDeclarationType [R/W]
TaxReportFilter.DiplayCreditMemosInSeparateColumn : BoYesNoEnum [R/W]
TaxReportFilter.DocumentType : TaxReportFilterApArDocumentType [R/W]
TaxReportFilter.ExcludeWT : BoYesNoEnum [R/W]
TaxReportFilter.FilterType : TaxReportFilterType [R/W]
TaxReportFilter.FirstPrintedNumber : Long [R/W]
TaxReportFilter.FirstRegisterNumber : Long [R/W]
TaxReportFilter.FromDate : Date [R/W]
TaxReportFilter.FromSeries : Long [R/W]
TaxReportFilter.HideTaxWithoutTransaction : BoYesNoEnum [R/W]
TaxReportFilter.IncludeCustomers : BoYesNoEnum [R/W]
TaxReportFilter.IncludeDocumentType : BoYesNoEnum [R/W]
TaxReportFilter.IncludeGLAccounts : BoYesNoEnum [R/W]
TaxReportFilter.IncludeSeriesFilter : BoYesNoEnum [R/W]
TaxReportFilter.IncludeVendors : BoYesNoEnum [R/W]
TaxReportFilter.Name : String [R/W]
TaxReportFilter.OpeningAndClosingBalance : BoYesNoEnum [R/W]
TaxReportFilter.Period : TaxReportFilterPeriod [R/W]
TaxReportFilter.Quarter : Long [R/W]
TaxReportFilter.QuarterOrDates : TaxReportFilterQuarterOrDates [R/W]
TaxReportFilter.ReportLayout : TaxReportFilterReportLayoutType [R/W]
TaxReportFilter.RoundAmount : BoYesNoEnum [R/W]
TaxReportFilter.ShowPaymentsWithDeferredTax : BoYesNoEnum [R/W]
TaxReportFilter.TaxDate : BoYesNoEnum [R/W]
TaxReportFilter.TaxReportAccounts : TaxReportAccounts [R]
TaxReportFilter.TaxReportBusinessPartners : TaxReportBusinessPartners [R]
TaxReportFilter.TaxReportDocuments : TaxReportDocuments [R]
TaxReportFilter.TaxReportGroups : TaxReportGroups [R]
TaxReportFilter.TaxReportSeriesCollection : TaxReportSeriesCollection [R]
TaxReportFilter.ToDate : Date [R/W]
TaxReportFilter.ToSeries : Long [R/W]
TaxReportFilter.Year : Long [R/W]
TaxReportFilter.FromXMLFile(ByVal bstrFileName As String)
TaxReportFilter.FromXMLString(ByVal bstrXML As String)
TaxReportFilter.GetXMLSchema() -> String
TaxReportFilter.ToXMLFile(ByVal bstrFileName As String)
TaxReportFilter.ToXMLString() -> String
TaxReportFilterParams.Code : Long [R/W]
TaxReportFilterParams.FilterType : TaxReportFilterType [R/W]
TaxReportFilterParams.Name : String [R]
TaxReportFilterParams.FromXMLFile(ByVal bstrFileName As String)
TaxReportFilterParams.FromXMLString(ByVal bstrXML As String)
TaxReportFilterParams.GetXMLSchema() -> String
TaxReportFilterParams.ToXMLFile(ByVal bstrFileName As String)
TaxReportFilterParams.ToXMLString() -> String
TaxReportFiltersParams.Count : Long [R]
TaxReportFiltersParams.Add() -> TaxReportFilterParams
TaxReportFiltersParams.GetXMLSchema() -> String
TaxReportFiltersParams.Item(ByVal vtIndex As Variant) -> TaxReportFilterParams
TaxReportFiltersParams.ToXMLFile(ByVal bstrFileName As String)
TaxReportFiltersParams.ToXMLString() -> String
TaxReportGroup.Code : String [R/W]
TaxReportGroup.Sum : BoYesNoEnum [R/W]
TaxReportGroup.FromXMLFile(ByVal bstrFileName As String)
TaxReportGroup.FromXMLString(ByVal bstrXML As String)
TaxReportGroup.GetXMLSchema() -> String
TaxReportGroup.ToXMLFile(ByVal bstrFileName As String)
TaxReportGroup.ToXMLString() -> String
TaxReportGroups.Count : Long [R]
TaxReportGroups.Add() -> TaxReportGroup
TaxReportGroups.GetXMLSchema() -> String
TaxReportGroups.Item(ByVal vtIndex As Variant) -> TaxReportGroup
TaxReportGroups.ToXMLFile(ByVal bstrFileName As String)
TaxReportGroups.ToXMLString() -> String
TaxReportSeries.DocumentType : TaxReportFilterDocumentType [R/W]
TaxReportSeries.SeriesCode : Long [R/W]
TaxReportSeries.FromXMLFile(ByVal bstrFileName As String)
TaxReportSeries.FromXMLString(ByVal bstrXML As String)
TaxReportSeries.GetXMLSchema() -> String
TaxReportSeries.ToXMLFile(ByVal bstrFileName As String)
TaxReportSeries.ToXMLString() -> String
TaxReportSeriesCollection.Count : Long [R]
TaxReportSeriesCollection.Add() -> TaxReportSeries
TaxReportSeriesCollection.GetXMLSchema() -> String
TaxReportSeriesCollection.Item(ByVal vtIndex As Variant) -> TaxReportSeries
TaxReportSeriesCollection.ToXMLFile(ByVal bstrFileName As String)
TaxReportSeriesCollection.ToXMLString() -> String
TaxWebSite.AbsEntry : Long [R]
TaxWebSite.Description : String [R/W]
TaxWebSite.WebSiteName : String [R/W]
TaxWebSite.WebSiteURL : String [R/W]
TaxWebSite.FromXMLFile(ByVal bstrFileName As String)
TaxWebSite.FromXMLString(ByVal bstrXML As String)
TaxWebSite.GetXMLSchema() -> String
TaxWebSite.ToXMLFile(ByVal bstrFileName As String)
TaxWebSite.ToXMLString() -> String
TaxWebSiteParams.AbsEntry : Long [R/W]
TaxWebSiteParams.WebSiteName : String [R]
TaxWebSiteParams.FromXMLFile(ByVal bstrFileName As String)
TaxWebSiteParams.FromXMLString(ByVal bstrXML As String)
TaxWebSiteParams.GetXMLSchema() -> String
TaxWebSiteParams.ToXMLFile(ByVal bstrFileName As String)
TaxWebSiteParams.ToXMLString() -> String
TaxWebSitesParams.Count : Long [R]
TaxWebSitesParams.Add() -> TaxWebSiteParams
TaxWebSitesParams.GetXMLSchema() -> String
TaxWebSitesParams.Item(ByVal vtIndex As Variant) -> TaxWebSiteParams
TaxWebSitesParams.ToXMLFile(ByVal bstrFileName As String)
TaxWebSitesParams.ToXMLString() -> String
TaxWebSitesService.AddTaxWebSite(ByVal pITaxWebSite As TaxWebSite) -> TaxWebSiteParams
TaxWebSitesService.GetDataInterface(ByVal enumMSDI As TaxWebSitesServiceDataInterfaces) -> Object
TaxWebSitesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TaxWebSitesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TaxWebSitesService.GetDefaultWebSite() -> TaxWebSiteParams
TaxWebSitesService.GetTaxWebSite(ByVal pITaxWebSiteParams As TaxWebSiteParams) -> TaxWebSite
TaxWebSitesService.GetTaxWebSiteList() -> TaxWebSitesParams
TaxWebSitesService.RemoveTaxWebSite(ByVal pITaxWebSiteParams As TaxWebSiteParams)
TaxWebSitesService.SetAsDefault(ByVal pITaxWebSiteParams As TaxWebSiteParams)
TaxWebSitesService.UpdateTaxWebSite(ByVal pITaxWebSite As TaxWebSite)
TeamCounter.CounterID : Long [R/W]
TeamCounter.CounterName : String [R]
TeamCounter.CounterNumber : Long [R/W]
TeamCounter.CounterType : CounterTypeEnum [R/W]
TeamCounter.CounterVisualOrder : Long [R]
TeamCounter.DocumentEntry : Long [R]
TeamCounter.FromXMLFile(ByVal bstrFileName As String)
TeamCounter.FromXMLString(ByVal bstrXML As String)
TeamCounter.GetXMLSchema() -> String
TeamCounter.ToXMLFile(ByVal bstrFileName As String)
TeamCounter.ToXMLString() -> String
TeamCounters.Count : Long [R]
TeamCounters.Add() -> TeamCounter
TeamCounters.GetXMLSchema() -> String
TeamCounters.Item(ByVal vtIndex As Variant) -> TeamCounter
TeamCounters.Remove(ByVal vtIndex As Variant)
TeamCounters.ToXMLFile(ByVal bstrFileName As String)
TeamCounters.ToXMLString() -> String
TeamMembers.Count : Long [R]
TeamMembers.EmployeeID : Long [R/W]
TeamMembers.RoleInTeam : BoRoleInTeam [R/W]
TeamMembers.TeamID : Long [R]
TeamMembers.UserFields : UserFields [R]
TeamMembers.Add()
TeamMembers.SetCurrentLine(ByVal LineNum As Long)
Teams.Browser : DataBrowser [R]
Teams.Description : String [R/W]
Teams.TeamID : Long [R]
Teams.TeamMembers : TeamMembers [R]
Teams.TeamName : String [R/W]
Teams.UserFields : UserFields [R]
Teams.Add() -> Long
Teams.GetAsXML() -> String
Teams.GetByKey(ByVal lTeamID As Long) -> Boolean
Teams.Remove() -> Long
Teams.SaveToFile(ByVal bstrFileName As String)
Teams.SaveXML(ByRef pbstrFileName As String)
Teams.Update() -> Long
TechnicianSchedulings.EndDate : Date [R]
TechnicianSchedulings.IsClosed : BoYesNoEnum [R]
TechnicianSchedulings.SchedulingLineNum : Long [R]
TechnicianSchedulings.ServiceCallID : Long [R]
TechnicianSchedulings.StartDate : Date [R]
TechnicianSchedulings.FromXMLFile(ByVal bstrFileName As String)
TechnicianSchedulings.FromXMLString(ByVal bstrXML As String)
TechnicianSchedulings.GetXMLSchema() -> String
TechnicianSchedulings.ToXMLFile(ByVal bstrFileName As String)
TechnicianSchedulings.ToXMLString() -> String
TechnicianSchedulingsCollection.Count : Long [R]
TechnicianSchedulingsCollection.Add() -> TechnicianSchedulings
TechnicianSchedulingsCollection.GetXMLSchema() -> String
TechnicianSchedulingsCollection.Item(ByVal vtIndex As Variant) -> TechnicianSchedulings
TechnicianSchedulingsCollection.ToXMLFile(ByVal bstrFileName As String)
TechnicianSchedulingsCollection.ToXMLString() -> String
TechnicianSchedulingsParams.EndDate : Date [R/W]
TechnicianSchedulingsParams.StartDate : Date [R/W]
TechnicianSchedulingsParams.Technician : Long [R/W]
TechnicianSchedulingsParams.FromXMLFile(ByVal bstrFileName As String)
TechnicianSchedulingsParams.FromXMLString(ByVal bstrXML As String)
TechnicianSchedulingsParams.GetXMLSchema() -> String
TechnicianSchedulingsParams.ToXMLFile(ByVal bstrFileName As String)
TechnicianSchedulingsParams.ToXMLString() -> String
TechnicianSettings.GroupCode : Long [R/W]
TechnicianSettings.Technician : Long [R/W]
TechnicianSettings.FromXMLFile(ByVal bstrFileName As String)
TechnicianSettings.FromXMLString(ByVal bstrXML As String)
TechnicianSettings.GetXMLSchema() -> String
TechnicianSettings.ToXMLFile(ByVal bstrFileName As String)
TechnicianSettings.ToXMLString() -> String
TechnicianSettingsGroup.AdvancedDashBoard : Long [R/W]
TechnicianSettingsGroup.Code : Long [R]
TechnicianSettingsGroup.CustomizedGroup : BoYesNoEnum [R/W]
TechnicianSettingsGroup.EnableActualDuration : BoYesNoEnum [R/W]
TechnicianSettingsGroup.EnableEditTime : BoYesNoEnum [R/W]
TechnicianSettingsGroup.EnableFollowup : BoYesNoEnum [R/W]
TechnicianSettingsGroup.EnableReject : BoYesNoEnum [R/W]
TechnicianSettingsGroup.EnableResign : BoYesNoEnum [R/W]
TechnicianSettingsGroup.EnableSignature : BoYesNoEnum [R/W]
TechnicianSettingsGroup.EnableStarRating : BoYesNoEnum [R/W]
TechnicianSettingsGroup.Name : String [R/W]
TechnicianSettingsGroup.FromXMLFile(ByVal bstrFileName As String)
TechnicianSettingsGroup.FromXMLString(ByVal bstrXML As String)
TechnicianSettingsGroup.GetXMLSchema() -> String
TechnicianSettingsGroup.ToXMLFile(ByVal bstrFileName As String)
TechnicianSettingsGroup.ToXMLString() -> String
TechnicianSettingsGroupParams.Code : Long [R/W]
TechnicianSettingsGroupParams.Name : String [R/W]
TechnicianSettingsGroupParams.FromXMLFile(ByVal bstrFileName As String)
TechnicianSettingsGroupParams.FromXMLString(ByVal bstrXML As String)
TechnicianSettingsGroupParams.GetXMLSchema() -> String
TechnicianSettingsGroupParams.ToXMLFile(ByVal bstrFileName As String)
TechnicianSettingsGroupParams.ToXMLString() -> String
TechnicianSettingsParams.Technician : Long [R/W]
TechnicianSettingsParams.FromXMLFile(ByVal bstrFileName As String)
TechnicianSettingsParams.FromXMLString(ByVal bstrXML As String)
TechnicianSettingsParams.GetXMLSchema() -> String
TechnicianSettingsParams.ToXMLFile(ByVal bstrFileName As String)
TechnicianSettingsParams.ToXMLString() -> String
TerminationReason.Description : String [R/W]
TerminationReason.Name : String [R/W]
TerminationReason.ReasonID : Long [R]
TerminationReason.FromXMLFile(ByVal bstrFileName As String)
TerminationReason.FromXMLString(ByVal bstrXML As String)
TerminationReason.GetXMLSchema() -> String
TerminationReason.ToXMLFile(ByVal bstrFileName As String)
TerminationReason.ToXMLString() -> String
TerminationReasonParams.Description : String [R]
TerminationReasonParams.Name : String [R]
TerminationReasonParams.ReasonID : Long [R/W]
TerminationReasonParams.FromXMLFile(ByVal bstrFileName As String)
TerminationReasonParams.FromXMLString(ByVal bstrXML As String)
TerminationReasonParams.GetXMLSchema() -> String
TerminationReasonParams.ToXMLFile(ByVal bstrFileName As String)
TerminationReasonParams.ToXMLString() -> String
TerminationReasonParamsCollection.Count : Long [R]
TerminationReasonParamsCollection.Add() -> TerminationReasonParams
TerminationReasonParamsCollection.GetXMLSchema() -> String
TerminationReasonParamsCollection.Item(ByVal vtIndex As Variant) -> TerminationReasonParams
TerminationReasonParamsCollection.ToXMLFile(ByVal bstrFileName As String)
TerminationReasonParamsCollection.ToXMLString() -> String
TerminationReasonService.Add(ByVal pITerminationReason As TerminationReason) -> TerminationReasonParams
TerminationReasonService.Delete(ByVal pITerminationReasonParams As TerminationReasonParams)
TerminationReasonService.Get(ByVal pITerminationReasonParams As TerminationReasonParams) -> TerminationReason
TerminationReasonService.GetDataInterface(ByVal enumMSDI As TerminationReasonServiceDataInterfaces) -> Object
TerminationReasonService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TerminationReasonService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TerminationReasonService.GetList() -> TerminationReasonParamsCollection
TerminationReasonService.Update(ByVal pITerminationReason As TerminationReason)
Territories.Browser : DataBrowser [R]
Territories.Description : String [R/W]
Territories.Inactive : BoYesNoEnum [R/W]
Territories.LocationIndex : Long [R/W]
Territories.Parent : Long [R/W]
Territories.TerritoryID : Long [R]
Territories.UserFields : UserFields [R]
Territories.Add() -> Long
Territories.GetAsXML() -> String
Territories.GetByKey(ByVal lID As Long) -> Boolean
Territories.Remove() -> Long
Territories.SaveToFile(ByVal FileName As String)
Territories.SaveXML(ByRef FileName As String)
Territories.Update() -> Long
TrackingNote.CCDNumber : String [R/W]
TrackingNote.CountryOfOrigin : String [R/W]
TrackingNote.CustomsTerminal : String [R/W]
TrackingNote.Date : Date [R/W]
TrackingNote.IsDirectImport : BoYesNoEnum [R/W]
TrackingNote.TrackingNoteBrokerCollection : TrackingNoteBrokerCollection [R]
TrackingNote.TrackingNoteItemCollection : TrackingNoteItemCollection [R]
TrackingNote.TrackingNoteNumber : Long [R]
TrackingNote.FromXMLFile(ByVal bstrFileName As String)
TrackingNote.FromXMLString(ByVal bstrXML As String)
TrackingNote.GetXMLSchema() -> String
TrackingNote.ToXMLFile(ByVal bstrFileName As String)
TrackingNote.ToXMLString() -> String
TrackingNoteBroker.AgreementNumber : Long [R/W]
TrackingNoteBroker.BPCode : String [R/W]
TrackingNoteBroker.TrackingNoteLineNumber : Long [R]
TrackingNoteBroker.TrackingNoteNumber : Long [R]
TrackingNoteBroker.FromXMLFile(ByVal bstrFileName As String)
TrackingNoteBroker.FromXMLString(ByVal bstrXML As String)
TrackingNoteBroker.GetXMLSchema() -> String
TrackingNoteBroker.ToXMLFile(ByVal bstrFileName As String)
TrackingNoteBroker.ToXMLString() -> String
TrackingNoteBrokerCollection.Count : Long [R]
TrackingNoteBrokerCollection.Add() -> TrackingNoteBroker
TrackingNoteBrokerCollection.GetXMLSchema() -> String
TrackingNoteBrokerCollection.Item(ByVal vtIndex As Variant) -> TrackingNoteBroker
TrackingNoteBrokerCollection.ToXMLFile(ByVal bstrFileName As String)
TrackingNoteBrokerCollection.ToXMLString() -> String
TrackingNoteItem.AccumulatedAPQuantity : Double [R]
TrackingNoteItem.AccumulatedARQuantity : Double [R]
TrackingNoteItem.AccumulatedRelocatedQuantity : Double [R]
TrackingNoteItem.CountryOfOrigin : String [R/W]
TrackingNoteItem.CustomsGroupCode : Long [R/W]
TrackingNoteItem.ItemCCDNumber : String [R/W]
TrackingNoteItem.ItemCode : String [R/W]
TrackingNoteItem.Quantity : Double [R/W]
TrackingNoteItem.TrackingNoteLineNumber : Long [R]
TrackingNoteItem.TrackingNoteNumber : Long [R]
TrackingNoteItem.FromXMLFile(ByVal bstrFileName As String)
TrackingNoteItem.FromXMLString(ByVal bstrXML As String)
TrackingNoteItem.GetXMLSchema() -> String
TrackingNoteItem.ToXMLFile(ByVal bstrFileName As String)
TrackingNoteItem.ToXMLString() -> String
TrackingNoteItemCollection.Count : Long [R]
TrackingNoteItemCollection.Add() -> TrackingNoteItem
TrackingNoteItemCollection.GetXMLSchema() -> String
TrackingNoteItemCollection.Item(ByVal vtIndex As Variant) -> TrackingNoteItem
TrackingNoteItemCollection.ToXMLFile(ByVal bstrFileName As String)
TrackingNoteItemCollection.ToXMLString() -> String
TrackingNoteParams.CCDNumber : String [R/W]
TrackingNoteParams.TrackingNoteNumber : Long [R/W]
TrackingNoteParams.FromXMLFile(ByVal bstrFileName As String)
TrackingNoteParams.FromXMLString(ByVal bstrXML As String)
TrackingNoteParams.GetXMLSchema() -> String
TrackingNoteParams.ToXMLFile(ByVal bstrFileName As String)
TrackingNoteParams.ToXMLString() -> String
TrackingNoteParamsCollection.Count : Long [R]
TrackingNoteParamsCollection.Add() -> TrackingNoteParams
TrackingNoteParamsCollection.GetXMLSchema() -> String
TrackingNoteParamsCollection.Item(ByVal vtIndex As Variant) -> TrackingNoteParams
TrackingNoteParamsCollection.ToXMLFile(ByVal bstrFileName As String)
TrackingNoteParamsCollection.ToXMLString() -> String
TrackingNotesService.Add(ByVal pITrackingNote As TrackingNote) -> TrackingNoteParams
TrackingNotesService.Delete(ByVal pITrackingNoteParams As TrackingNoteParams)
TrackingNotesService.Get(ByVal pITrackingNoteParams As TrackingNoteParams) -> TrackingNote
TrackingNotesService.GetDataInterface(ByVal enumMSDI As TrackingNotesServiceDataInterfaces) -> Object
TrackingNotesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TrackingNotesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TrackingNotesService.GetList() -> TrackingNoteParamsCollection
TrackingNotesService.Update(ByVal pITrackingNote As TrackingNote)
TransactionCode.Code : String [R/W]
TransactionCode.Description : String [R/W]
TransactionCode.FromXMLFile(ByVal bstrFileName As String)
TransactionCode.FromXMLString(ByVal bstrXML As String)
TransactionCode.GetXMLSchema() -> String
TransactionCode.ToXMLFile(ByVal bstrFileName As String)
TransactionCode.ToXMLString() -> String
TransactionCodeParams.Code : String [R/W]
TransactionCodeParams.Description : String [R]
TransactionCodeParams.FromXMLFile(ByVal bstrFileName As String)
TransactionCodeParams.FromXMLString(ByVal bstrXML As String)
TransactionCodeParams.GetXMLSchema() -> String
TransactionCodeParams.ToXMLFile(ByVal bstrFileName As String)
TransactionCodeParams.ToXMLString() -> String
TransactionCodeParamsCollection.Count : Long [R]
TransactionCodeParamsCollection.Add() -> TransactionCodeParams
TransactionCodeParamsCollection.GetXMLSchema() -> String
TransactionCodeParamsCollection.Item(ByVal vtIndex As Variant) -> TransactionCodeParams
TransactionCodeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
TransactionCodeParamsCollection.ToXMLString() -> String
TransactionCodesService.Add(ByVal pITransactionCode As TransactionCode) -> TransactionCodeParams
TransactionCodesService.Delete(ByVal pITransactionCodeParams As TransactionCodeParams)
TransactionCodesService.Get(ByVal pITransactionCodeParams As TransactionCodeParams) -> TransactionCode
TransactionCodesService.GetDataInterface(ByVal enumMSDI As TransactionCodesServiceDataInterfaces) -> Object
TransactionCodesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TransactionCodesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TransactionCodesService.GetList() -> TransactionCodeParamsCollection
TransactionCodesService.Update(ByVal pITransactionCode As TransactionCode)
TranslationsInUserLanguages.Count : Long [R]
TranslationsInUserLanguages.KeyFromHeaderTable : Long [R]
TranslationsInUserLanguages.LanguageCodeOfUserLanguage : Long [R/W]
TranslationsInUserLanguages.Translationscontent : String [R/W]
TranslationsInUserLanguages.UserFields : UserFields [R]
TranslationsInUserLanguages.Add()
TranslationsInUserLanguages.SetCurrentLine(ByVal LineNum As Long)
TransportationDocumentCollection.Count : Long [R]
TransportationDocumentCollection.Add() -> TransportationDocumentData
TransportationDocumentCollection.GetXMLSchema() -> String
TransportationDocumentCollection.Item(ByVal vtIndex As Variant) -> TransportationDocumentData
TransportationDocumentCollection.ToXMLFile(ByVal bstrFileName As String)
TransportationDocumentCollection.ToXMLString() -> String
TransportationDocumentData.AttachmentEntry : Long [R/W]
TransportationDocumentData.Canceled : BoYesNoEnum [R/W]
TransportationDocumentData.CarrierCode : String [R/W]
TransportationDocumentData.ElDocExportFormat : Long [R/W]
TransportationDocumentData.ElDocGenType : ElectronicDocGenTypeEnum [R/W]
TransportationDocumentData.ExpirationDate : Date [R/W]
TransportationDocumentData.IssueGate : Long [R/W]
TransportationDocumentData.NextNumber : Long [R/W]
TransportationDocumentData.PostDate : Date [R/W]
TransportationDocumentData.TrailerID : String [R/W]
TransportationDocumentData.TranspDocNumber : Long [R]
TransportationDocumentData.TransportationDocumentLineDataCollection : TransportationDocumentLineDataCollection [R]
TransportationDocumentData.TransportationDocumentParamsCollection : TransportationDocumentParamsCollection [R]
TransportationDocumentData.TransportationNumber : String [R/W]
TransportationDocumentData.TransportedTotalLC : Double [R]
TransportationDocumentData.VehicleID : String [R/W]
TransportationDocumentData.WarehouseCode : String [R/W]
TransportationDocumentData.Weight : Double [R]
TransportationDocumentData.WeightUnit : Long [R]
TransportationDocumentData.FromXMLFile(ByVal bstrFileName As String)
TransportationDocumentData.FromXMLString(ByVal bstrXML As String)
TransportationDocumentData.GetXMLSchema() -> String
TransportationDocumentData.ToXMLFile(ByVal bstrFileName As String)
TransportationDocumentData.ToXMLString() -> String
TransportationDocumentLineData.DocLineNumber : Long [R/W]
TransportationDocumentLineData.DocNumber : Long [R/W]
TransportationDocumentLineData.DocOrderNum : Long [R/W]
TransportationDocumentLineData.DocType : DocumentObjectTypeEnum [R/W]
TransportationDocumentLineData.ItemCode : String [R]
TransportationDocumentLineData.LineId : Long [R]
TransportationDocumentLineData.TranspDocNumber : Long [R]
TransportationDocumentLineData.TransportedQuantity : Double [R/W]
TransportationDocumentLineData.FromXMLFile(ByVal bstrFileName As String)
TransportationDocumentLineData.FromXMLString(ByVal bstrXML As String)
TransportationDocumentLineData.GetXMLSchema() -> String
TransportationDocumentLineData.ToXMLFile(ByVal bstrFileName As String)
TransportationDocumentLineData.ToXMLString() -> String
TransportationDocumentLineDataCollection.Count : Long [R]
TransportationDocumentLineDataCollection.Add() -> TransportationDocumentLineData
TransportationDocumentLineDataCollection.GetXMLSchema() -> String
TransportationDocumentLineDataCollection.Item(ByVal vtIndex As Variant) -> TransportationDocumentLineData
TransportationDocumentLineDataCollection.ToXMLFile(ByVal bstrFileName As String)
TransportationDocumentLineDataCollection.ToXMLString() -> String
TransportationDocumentParams.TranspDocNumber : Long [R/W]
TransportationDocumentParams.FromXMLFile(ByVal bstrFileName As String)
TransportationDocumentParams.FromXMLString(ByVal bstrXML As String)
TransportationDocumentParams.GetXMLSchema() -> String
TransportationDocumentParams.ToXMLFile(ByVal bstrFileName As String)
TransportationDocumentParams.ToXMLString() -> String
TransportationDocumentParamsCollection.Count : Long [R]
TransportationDocumentParamsCollection.Add() -> TransportationDocumentParams
TransportationDocumentParamsCollection.GetXMLSchema() -> String
TransportationDocumentParamsCollection.Item(ByVal vtIndex As Variant) -> TransportationDocumentParams
TransportationDocumentParamsCollection.ToXMLFile(ByVal bstrFileName As String)
TransportationDocumentParamsCollection.ToXMLString() -> String
TransportationDocumentService.AddTransportationDocument(ByVal pITransportationDocumentData As TransportationDocumentData) -> TransportationDocumentParams
TransportationDocumentService.CancelTransportationDocument(ByVal pITransportationDocumentParams As TransportationDocumentParams)
TransportationDocumentService.GetDataInterface(ByVal enumMSDI As TransportationDocumentServiceDataInterfaces) -> Object
TransportationDocumentService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
TransportationDocumentService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
TransportationDocumentService.GetTransportationDocument(ByVal pITransportationDocumentParams As TransportationDocumentParams) -> TransportationDocumentData
TransportationDocumentService.UpdateTransportationDocument(ByVal pITransportationDocumentData As TransportationDocumentData)
UnitOfMeasurement.AbsEntry : Long [R]
UnitOfMeasurement.Code : String [R/W]
UnitOfMeasurement.EWBUnitEntry : Long [R/W]
UnitOfMeasurement.Height1 : Double [R/W]
UnitOfMeasurement.Height1Unit : Long [R/W]
UnitOfMeasurement.Height2 : Double [R/W]
UnitOfMeasurement.Height2Unit : Long [R/W]
UnitOfMeasurement.InternationalSymbol : String [R/W]
UnitOfMeasurement.Length1 : Double [R/W]
UnitOfMeasurement.Length1Unit : Long [R/W]
UnitOfMeasurement.Length2 : Double [R/W]
UnitOfMeasurement.Length2Unit : Long [R/W]
UnitOfMeasurement.Name : String [R/W]
UnitOfMeasurement.PPWe1Unit : Long [R/W]
UnitOfMeasurement.PPWe2Unit : Long [R/W]
UnitOfMeasurement.PPWeight1 : Double [R/W]
UnitOfMeasurement.PPWeight2 : Double [R/W]
UnitOfMeasurement.UserFields : Fields [R]
UnitOfMeasurement.Volume : Double [R/W]
UnitOfMeasurement.VolumeUnit : Long [R/W]
UnitOfMeasurement.Weight1 : Double [R/W]
UnitOfMeasurement.Weight1Unit : Long [R/W]
UnitOfMeasurement.Weight2 : Double [R/W]
UnitOfMeasurement.Weight2Unit : Long [R/W]
UnitOfMeasurement.Width1 : Double [R/W]
UnitOfMeasurement.Width1Unit : Long [R/W]
UnitOfMeasurement.Width2 : Double [R/W]
UnitOfMeasurement.Width2Unit : Long [R/W]
UnitOfMeasurement.FromXMLFile(ByVal bstrFileName As String)
UnitOfMeasurement.FromXMLString(ByVal bstrXML As String)
UnitOfMeasurement.GetXMLSchema() -> String
UnitOfMeasurement.ToXMLFile(ByVal bstrFileName As String)
UnitOfMeasurement.ToXMLString() -> String
UnitOfMeasurementGroup.AbsEntry : Long [R]
UnitOfMeasurementGroup.BaseUoM : Long [R/W]
UnitOfMeasurementGroup.Code : String [R/W]
UnitOfMeasurementGroup.GroupDefinitions : UoMGroupDefinitionCollection [R]
UnitOfMeasurementGroup.Name : String [R/W]
UnitOfMeasurementGroup.FromXMLFile(ByVal bstrFileName As String)
UnitOfMeasurementGroup.FromXMLString(ByVal bstrXML As String)
UnitOfMeasurementGroup.GetXMLSchema() -> String
UnitOfMeasurementGroup.ToXMLFile(ByVal bstrFileName As String)
UnitOfMeasurementGroup.ToXMLString() -> String
UnitOfMeasurementGroupParams.AbsEntry : Long [R/W]
UnitOfMeasurementGroupParams.Code : String [R/W]
UnitOfMeasurementGroupParams.FromXMLFile(ByVal bstrFileName As String)
UnitOfMeasurementGroupParams.FromXMLString(ByVal bstrXML As String)
UnitOfMeasurementGroupParams.GetXMLSchema() -> String
UnitOfMeasurementGroupParams.ToXMLFile(ByVal bstrFileName As String)
UnitOfMeasurementGroupParams.ToXMLString() -> String
UnitOfMeasurementGroupParamsCollection.Count : Long [R]
UnitOfMeasurementGroupParamsCollection.Add() -> UnitOfMeasurementGroupParams
UnitOfMeasurementGroupParamsCollection.GetXMLSchema() -> String
UnitOfMeasurementGroupParamsCollection.Item(ByVal vtIndex As Variant) -> UnitOfMeasurementGroupParams
UnitOfMeasurementGroupParamsCollection.ToXMLFile(ByVal bstrFileName As String)
UnitOfMeasurementGroupParamsCollection.ToXMLString() -> String
UnitOfMeasurementGroupsService.Add(ByVal pIUnitOfMeasurementGroup As UnitOfMeasurementGroup) -> UnitOfMeasurementGroupParams
UnitOfMeasurementGroupsService.Delete(ByVal pIUnitOfMeasurementGroupParams As UnitOfMeasurementGroupParams)
UnitOfMeasurementGroupsService.Get(ByVal pIUnitOfMeasurementGroupParams As UnitOfMeasurementGroupParams) -> UnitOfMeasurementGroup
UnitOfMeasurementGroupsService.GetDataInterface(ByVal enumMSDI As UnitOfMeasurementGroupsServiceDataInterfaces) -> Object
UnitOfMeasurementGroupsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
UnitOfMeasurementGroupsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
UnitOfMeasurementGroupsService.GetList() -> UnitOfMeasurementGroupParamsCollection
UnitOfMeasurementGroupsService.Update(ByVal pIUnitOfMeasurementGroup As UnitOfMeasurementGroup)
UnitOfMeasurementParams.AbsEntry : Long [R/W]
UnitOfMeasurementParams.Code : String [R/W]
UnitOfMeasurementParams.FromXMLFile(ByVal bstrFileName As String)
UnitOfMeasurementParams.FromXMLString(ByVal bstrXML As String)
UnitOfMeasurementParams.GetXMLSchema() -> String
UnitOfMeasurementParams.ToXMLFile(ByVal bstrFileName As String)
UnitOfMeasurementParams.ToXMLString() -> String
UnitOfMeasurementParamsCollection.Count : Long [R]
UnitOfMeasurementParamsCollection.Add() -> UnitOfMeasurementParams
UnitOfMeasurementParamsCollection.GetXMLSchema() -> String
UnitOfMeasurementParamsCollection.Item(ByVal vtIndex As Variant) -> UnitOfMeasurementParams
UnitOfMeasurementParamsCollection.ToXMLFile(ByVal bstrFileName As String)
UnitOfMeasurementParamsCollection.ToXMLString() -> String
UnitOfMeasurementsService.Add(ByVal pIUnitOfMeasurement As UnitOfMeasurement) -> UnitOfMeasurementParams
UnitOfMeasurementsService.Delete(ByVal pIUnitOfMeasurementParams As UnitOfMeasurementParams)
UnitOfMeasurementsService.Get(ByVal pIUnitOfMeasurementParams As UnitOfMeasurementParams) -> UnitOfMeasurement
UnitOfMeasurementsService.GetDataInterface(ByVal enumMSDI As UnitOfMeasurementsServiceDataInterfaces) -> Object
UnitOfMeasurementsService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
UnitOfMeasurementsService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
UnitOfMeasurementsService.GetList() -> UnitOfMeasurementParamsCollection
UnitOfMeasurementsService.Update(ByVal pIUnitOfMeasurement As UnitOfMeasurement)
UoMGroupDefinition.Active : BoYesNoEnum [R/W]
UoMGroupDefinition.AlternateQuantity : Double [R/W]
UoMGroupDefinition.AlternateUoM : Long [R/W]
UoMGroupDefinition.BaseQuantity : Double [R/W]
UoMGroupDefinition.UdfFactor : Long [R/W]
UoMGroupDefinition.WeightFactor : Long [R/W]
UoMGroupDefinition.FromXMLFile(ByVal bstrFileName As String)
UoMGroupDefinition.FromXMLString(ByVal bstrXML As String)
UoMGroupDefinition.GetXMLSchema() -> String
UoMGroupDefinition.ToXMLFile(ByVal bstrFileName As String)
UoMGroupDefinition.ToXMLString() -> String
UoMGroupDefinitionCollection.Count : Long [R]
UoMGroupDefinitionCollection.Add() -> UoMGroupDefinition
UoMGroupDefinitionCollection.GetXMLSchema() -> String
UoMGroupDefinitionCollection.Item(ByVal vtIndex As Variant) -> UoMGroupDefinition
UoMGroupDefinitionCollection.Remove(ByVal vtIndex As Variant)
UoMGroupDefinitionCollection.ToXMLFile(ByVal bstrFileName As String)
UoMGroupDefinitionCollection.ToXMLString() -> String
UoMPrices.AdditionalCurrency1 : String [R/W]
UoMPrices.AdditionalCurrency2 : String [R/W]
UoMPrices.AdditionalPrice1 : Double [R/W]
UoMPrices.AdditionalPrice2 : Double [R/W]
UoMPrices.AdditionalReduceBy1 : Double [R/W]
UoMPrices.AdditionalReduceBy2 : Double [R/W]
UoMPrices.Auto : BoYesNoEnum [R/W]
UoMPrices.Count : Long [R]
UoMPrices.Currency : String [R/W]
UoMPrices.Price : Double [R/W]
UoMPrices.PriceList : Long [R/W]
UoMPrices.ReduceBy : Double [R/W]
UoMPrices.UoMEntry : Long [R/W]
UoMPrices.Add()
UoMPrices.Delete()
UoMPrices.SetCurrentLine(ByVal LineNum As Long)
UserActionRecord.Action : UserActionTypeEnum [R]
UserActionRecord.ActionBy : String [R]
UserActionRecord.ActionDate : Date [R]
UserActionRecord.ActionTime : Date [R]
UserActionRecord.AliveDuration : Long [R]
UserActionRecord.ClientIP : String [R]
UserActionRecord.ClientName : String [R]
UserActionRecord.Count : Long [R]
UserActionRecord.ProcessID : Long [R]
UserActionRecord.ProcessName : String [R]
UserActionRecord.UserCode : String [R]
UserActionRecord.UserFields : UserFields [R]
UserActionRecord.WindowsSession : Long [R]
UserActionRecord.WindowsUser : String [R]
UserActionRecord.SetCurrentLine(ByVal LineNum As Long)
UserBranchAssignment.BPLID : Long [R/W]
UserBranchAssignment.Count : Long [R]
UserBranchAssignment.UserCode : String [R]
UserBranchAssignment.Add()
UserBranchAssignment.Delete()
UserBranchAssignment.SetCurrentLine(ByVal LineNum As Long)
UserDefaultGroups.AdditionalIdNumber : String [R/W]
UserDefaultGroups.Address : String [R/W]
UserDefaultGroups.AddressinForeignLanguage : String [R/W]
UserDefaultGroups.AssetInDoc : BoYesNoEnum [R/W]
UserDefaultGroups.BPforInvoicePayment : String [R/W]
UserDefaultGroups.BPLID : Long [R/W]
UserDefaultGroups.Browser : DataBrowser [R]
UserDefaultGroups.CashAccount : String [R/W]
UserDefaultGroups.CheckingAcct : String [R/W]
UserDefaultGroups.Code : String [R/W]
UserDefaultGroups.Country : String [R/W]
UserDefaultGroups.DefaultCreditCards : DefaultCreditCards [R]
UserDefaultGroups.DefaultDocuments : DefaultDocuments [R]
UserDefaultGroups.DefaultPTICode : String [R/W]
UserDefaultGroups.DefaultPTICodes : DefaultPTICodes [R]
UserDefaultGroups.DefaultTaxCode : String [R/W]
UserDefaultGroups.eMail : String [R/W]
UserDefaultGroups.FaxNumber : String [R/W]
UserDefaultGroups.FaxNumberForeignLang : String [R/W]
UserDefaultGroups.LanguageCode : BoSuppLangs [R/W]
UserDefaultGroups.Name : String [R/W]
UserDefaultGroups.PhoneNumber1 : String [R/W]
UserDefaultGroups.PhoneNumber1ForeignLang : String [R/W]
UserDefaultGroups.PhoneNumber2 : String [R/W]
UserDefaultGroups.PhoneNumber2ForeignLang : String [R/W]
UserDefaultGroups.PrintingHeader : String [R/W]
UserDefaultGroups.PrintingHeaderInForeignLangu : String [R/W]
UserDefaultGroups.PrintInvoiceandPaymentinS : BoYesNoEnum [R/W]
UserDefaultGroups.PrintReceipt : BoPrintReceiptEnum [R/W]
UserDefaultGroups.SalesEmployee : Long [R/W]
UserDefaultGroups.UserFields : UserFields [R]
UserDefaultGroups.UserSignature : Long [R]
UserDefaultGroups.UseTax : BoYesNoEnum [R/W]
UserDefaultGroups.UseWarehouseAddressinAPD : BoYesNoEnum [R/W]
UserDefaultGroups.Warehouse : String [R/W]
UserDefaultGroups.WindowsColor : Long [R/W]
UserDefaultGroups.Add() -> Long
UserDefaultGroups.GetAsXML() -> String
UserDefaultGroups.GetByKey(ByVal bstrCode As String) -> Boolean
UserDefaultGroups.Remove() -> Long
UserDefaultGroups.SaveToFile(ByVal bstrFileName As String)
UserDefaultGroups.SaveXML(ByRef pbstrFileName As String)
UserDefaultGroups.Update() -> Long
UserFields.Fields : Fields [R]
UserFieldsMD.Browser : DataBrowser [R]
UserFieldsMD.DefaultValue : String [R/W]
UserFieldsMD.Description : String [R/W]
UserFieldsMD.EditSize : Long [R/W]
UserFieldsMD.FieldID : Long [R]
UserFieldsMD.LinkedSystemObject : UDFLinkedSystemObjectTypesEnum [R/W]
UserFieldsMD.LinkedTable : String [R/W]
UserFieldsMD.LinkedUDO : String [R/W]
UserFieldsMD.Mandatory : BoYesNoEnum [R/W]
UserFieldsMD.Name : String [R/W]
UserFieldsMD.Size : Long [R/W]
UserFieldsMD.SubType : BoFldSubTypes [R/W]
UserFieldsMD.TableName : String [R/W]
UserFieldsMD.Type : BoFieldTypes [R/W]
UserFieldsMD.ValidValues : ValidValuesMD [R]
UserFieldsMD.Add() -> Long
UserFieldsMD.GetAsXML() -> String
UserFieldsMD.GetByKey(ByVal TableName As String, ByVal FieldID As Long) -> Boolean
UserFieldsMD.Remove() -> Long
UserFieldsMD.SaveToFile(ByVal FileName As String)
UserFieldsMD.SaveXML(ByRef FileName As String)
UserFieldsMD.Update() -> Long
UserGroup.DueDate : Date [R/W]
UserGroup.StartDate : Date [R/W]
UserGroup.TPLId : Long [R/W]
UserGroup.UserGroupDec : String [R/W]
UserGroup.UserGroupId : Long [R]
UserGroup.UserGroupName : String [R/W]
UserGroup.UserGroupType : UserGroupCategoryEnum [R/W]
UserGroup.FromXMLFile(ByVal bstrFileName As String)
UserGroup.FromXMLString(ByVal bstrXML As String)
UserGroup.GetXMLSchema() -> String
UserGroup.ToXMLFile(ByVal bstrFileName As String)
UserGroup.ToXMLString() -> String
UserGroupByUser.Count : Long [R]
UserGroupByUser.DueDate : Date [R/W]
UserGroupByUser.GroupId : Long [R/W]
UserGroupByUser.StartDate : Date [R/W]
UserGroupByUser.Add()
UserGroupByUser.Delete()
UserGroupByUser.SetCurrentLine(ByVal LineNum As Long)
UserGroupParams.UserGroupId : Long [R/W]
UserGroupParams.UserGroupName : String [R/W]
UserGroupParams.FromXMLFile(ByVal bstrFileName As String)
UserGroupParams.FromXMLString(ByVal bstrXML As String)
UserGroupParams.GetXMLSchema() -> String
UserGroupParams.ToXMLFile(ByVal bstrFileName As String)
UserGroupParams.ToXMLString() -> String
UserGroupService.AddUserGroup(ByVal pIUserGroup As UserGroup) -> UserGroupParams
UserGroupService.DeleteUserGroup(ByVal pIUserGroupParams As UserGroupParams)
UserGroupService.GetDataInterface(ByVal enumMSDI As UserGroupServiceDataInterfaces) -> Object
UserGroupService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
UserGroupService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
UserGroupService.GetUserGroup(ByVal pIUserGroupParams As UserGroupParams) -> UserGroup
UserGroupService.GetUserGroupList() -> UserGroupsParams
UserGroupService.UpdateUserGroup(ByVal pIUserGroup As UserGroup)
UserGroupsParams.Count : Long [R]
UserGroupsParams.Add() -> UserGroupParams
UserGroupsParams.GetXMLSchema() -> String
UserGroupsParams.Item(ByVal vtIndex As Variant) -> UserGroupParams
UserGroupsParams.ToXMLFile(ByVal bstrFileName As String)
UserGroupsParams.ToXMLString() -> String
UserKeysMD.Browser : DataBrowser [R]
UserKeysMD.Elements : UserKeysMD_Elements [R]
UserKeysMD.KeyIndex : Long [R]
UserKeysMD.KeyName : String [R/W]
UserKeysMD.TableName : String [R/W]
UserKeysMD.Unique : BoYesNoEnum [R/W]
UserKeysMD.Add() -> Long
UserKeysMD.GetAsXML() -> String
UserKeysMD.GetByKey(ByVal TableName As String, ByVal KeyIndex As Long) -> Boolean
UserKeysMD.Remove() -> Long
UserKeysMD.SaveToFile(ByVal FileName As String)
UserKeysMD.SaveXML(ByRef FileName As String)
UserKeysMD_Elements.ColumnAlias : String [R/W]
UserKeysMD_Elements.Count : Long [R]
UserKeysMD_Elements.SubKeyIndex : Long [R]
UserKeysMD_Elements.Add()
UserKeysMD_Elements.SetCurrentLine(ByVal LineNum As Long)
UserLanguages.Browser : DataBrowser [R]
UserLanguages.Code : Long [R]
UserLanguages.LanguageFullName : String [R/W]
UserLanguages.LanguageShortName : String [R/W]
UserLanguages.RelatedSystemLanguage : Long [R/W]
UserLanguages.UserFields : UserFields [R]
UserLanguages.Add() -> Long
UserLanguages.GetAsXML() -> String
UserLanguages.GetByKey(ByVal lCode As Long) -> Boolean
UserLanguages.Remove() -> Long
UserLanguages.SaveToFile(ByVal bstrFileName As String)
UserLanguages.SaveXML(ByRef pbstrFileName As String)
UserLanguages.Update() -> Long
UserLicenseParams.LicenseType : LicenseTypeEnum [R/W]
UserLicenseParams.LicenseUpdateType : LicenseUpdateTypeEnum [R/W]
UserLicenseParams.UserName : String [R/W]
UserLicenseParams.FromXMLFile(ByVal bstrFileName As String)
UserLicenseParams.FromXMLString(ByVal bstrXML As String)
UserLicenseParams.GetXMLSchema() -> String
UserLicenseParams.ToXMLFile(ByVal bstrFileName As String)
UserLicenseParams.ToXMLString() -> String
UserMenuItem.LinkedFormMenuID : Long [R/W]
UserMenuItem.LinkedFormNum : Long [R/W]
UserMenuItem.LinkedObjKey : String [R/W]
UserMenuItem.LinkedObjType : String [R/W]
UserMenuItem.Name : String [R/W]
UserMenuItem.Position : Long [R/W]
UserMenuItem.ReportPath : String [R/W]
UserMenuItem.Type : UserMenuItemTypeEnum [R/W]
UserMenuItem.UserMenuItems : UserMenuItems [R/W]
UserMenuItem.FromXMLFile(ByVal bstrFileName As String)
UserMenuItem.FromXMLString(ByVal bstrXML As String)
UserMenuItem.GetXMLSchema() -> String
UserMenuItem.ToXMLFile(ByVal bstrFileName As String)
UserMenuItem.ToXMLString() -> String
UserMenuItems.Count : Long [R]
UserMenuItems.Add() -> UserMenuItem
UserMenuItems.GetXMLSchema() -> String
UserMenuItems.Item(ByVal vtIndex As Variant) -> UserMenuItem
UserMenuItems.Remove(ByVal vtIndex As Variant)
UserMenuItems.ToXMLFile(ByVal bstrFileName As String)
UserMenuItems.ToXMLString() -> String
UserMenuParams.UserID : Long [R/W]
UserMenuParams.FromXMLFile(ByVal bstrFileName As String)
UserMenuParams.FromXMLString(ByVal bstrXML As String)
UserMenuParams.GetXMLSchema() -> String
UserMenuParams.ToXMLFile(ByVal bstrFileName As String)
UserMenuParams.ToXMLString() -> String
UserMenuService.GetCurrentUserMenu() -> UserMenuItems
UserMenuService.GetDataInterface(ByVal enumMSDI As UserMenuServiceDataInterfaces) -> Object
UserMenuService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
UserMenuService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
UserMenuService.GetUserMenu(ByVal pIUserMenuParams As UserMenuParams) -> UserMenuItems
UserMenuService.UpdateCurrentUserMenu(ByVal pIUserMenuItems As UserMenuItems)
UserMenuService.UpdateUserMenu(ByVal pIUserMenuParams As UserMenuParams, ByVal pIUserMenuItems As UserMenuItems)
UserObjectMD_ChildTables.Code : String [R]
UserObjectMD_ChildTables.Count : Long [R]
UserObjectMD_ChildTables.LogTableName : String [R/W]
UserObjectMD_ChildTables.ObjectName : String [R/W]
UserObjectMD_ChildTables.SonNumber : Long [R]
UserObjectMD_ChildTables.TableName : String [R/W]
UserObjectMD_ChildTables.Add()
UserObjectMD_ChildTables.SetCurrentLine(ByVal LineNum As Long)
UserObjectMD_EnhancedFormColumns.ChildNumber : Long [R/W]
UserObjectMD_EnhancedFormColumns.Code : String [R]
UserObjectMD_EnhancedFormColumns.ColumnAlias : String [R/W]
UserObjectMD_EnhancedFormColumns.ColumnDescription : String [R/W]
UserObjectMD_EnhancedFormColumns.ColumnIsUsed : BoYesNoEnum [R/W]
UserObjectMD_EnhancedFormColumns.ColumnNumber : Long [R/W]
UserObjectMD_EnhancedFormColumns.Count : Long [R]
UserObjectMD_EnhancedFormColumns.Editable : BoYesNoEnum [R/W]
UserObjectMD_EnhancedFormColumns.Add()
UserObjectMD_EnhancedFormColumns.SetCurrentLine(ByVal LineNum As Long)
UserObjectMD_FindColumns.Code : String [R]
UserObjectMD_FindColumns.ColumnAlias : String [R/W]
UserObjectMD_FindColumns.ColumnDescription : String [R/W]
UserObjectMD_FindColumns.ColumnNumber : Long [R]
UserObjectMD_FindColumns.Count : Long [R]
UserObjectMD_FindColumns.Add()
UserObjectMD_FindColumns.SetCurrentLine(ByVal LineNum As Long)
UserObjectMD_FormColumns.Code : String [R]
UserObjectMD_FormColumns.Count : Long [R]
UserObjectMD_FormColumns.Editable : BoYesNoEnum [R/W]
UserObjectMD_FormColumns.FormColumnAlias : String [R/W]
UserObjectMD_FormColumns.FormColumnDescription : String [R/W]
UserObjectMD_FormColumns.FormColumnNumber : Long [R]
UserObjectMD_FormColumns.SonNumber : Long [R/W]
UserObjectMD_FormColumns.Add()
UserObjectMD_FormColumns.SetCurrentLine(ByVal LineNum As Long)
UserObjectsMD.Browser : DataBrowser [R]
UserObjectsMD.CanApprove : BoYesNoEnum [R/W]
UserObjectsMD.CanArchive : BoYesNoEnum [R/W]
UserObjectsMD.CanCancel : BoYesNoEnum [R/W]
UserObjectsMD.CanClose : BoYesNoEnum [R/W]
UserObjectsMD.CanCreateDefaultForm : BoYesNoEnum [R/W]
UserObjectsMD.CanDelete : BoYesNoEnum [R/W]
UserObjectsMD.CanFind : BoYesNoEnum [R/W]
UserObjectsMD.CanLog : BoYesNoEnum [R/W]
UserObjectsMD.CanYearTransfer : BoYesNoEnum [R/W]
UserObjectsMD.ChildTables : UserObjectMD_ChildTables [R]
UserObjectsMD.Code : String [R/W]
UserObjectsMD.EnableEnhancedForm : BoYesNoEnum [R/W]
UserObjectsMD.EnhancedFormColumns : UserObjectMD_EnhancedFormColumns [R]
UserObjectsMD.ExtensionName : String [R/W]
UserObjectsMD.FatherMenuID : Long [R/W]
UserObjectsMD.FindColumns : UserObjectMD_FindColumns [R]
UserObjectsMD.FormColumns : UserObjectMD_FormColumns [R]
UserObjectsMD.FormSRF : String [R/W]
UserObjectsMD.LogTableName : String [R/W]
UserObjectsMD.ManageSeries : BoYesNoEnum [R/W]
UserObjectsMD.MenuCaption : String [R/W]
UserObjectsMD.MenuItem : BoYesNoEnum [R/W]
UserObjectsMD.MenuUID : String [R/W]
UserObjectsMD.Name : String [R/W]
UserObjectsMD.ObjectType : BoUDOObjType [R/W]
UserObjectsMD.OverwriteDllfile : BoYesNoEnum [R/W]
UserObjectsMD.Position : Long [R/W]
UserObjectsMD.RebuildEnhancedForm : BoYesNoEnum [R/W]
UserObjectsMD.TableName : String [R/W]
UserObjectsMD.TemplateID : String [R/W]
UserObjectsMD.UseUniqueFormType : BoYesNoEnum [R/W]
UserObjectsMD.Add() -> Long
UserObjectsMD.GetAsXML() -> String
UserObjectsMD.GetByKey(ByVal Code As String) -> Boolean
UserObjectsMD.Remove() -> Long
UserObjectsMD.SaveXML(ByRef FileName As String)
UserObjectsMD.Update() -> Long
UserPermission.Count : Long [R]
UserPermission.Permission : BoPermission [R/W]
UserPermission.PermissionID : String [R/W]
UserPermission.UserCode : Long [R]
UserPermission.UserFields : UserFields [R]
UserPermission.Add()
UserPermission.SetCurrentLine(ByVal LineNum As Long)
UserPermissionForms.Count : Long [R]
UserPermissionForms.DisplayOrder : Long [R/W]
UserPermissionForms.FormType : String [R/W]
UserPermissionForms.PermissionID : String [R]
UserPermissionForms.UserFields : UserFields [R]
UserPermissionForms.Add()
UserPermissionForms.SetCurrentLine(ByVal LineNum As Long)
UserPermissionTree.Browser : DataBrowser [R]
UserPermissionTree.DisplayOrder : Long [R]
UserPermissionTree.IsItem : BoYesNoEnum [R/W]
UserPermissionTree.Levels : Long [R]
UserPermissionTree.Name : String [R/W]
UserPermissionTree.Options : BoUPTOptions [R/W]
UserPermissionTree.ParentID : String [R/W]
UserPermissionTree.PermissionID : String [R/W]
UserPermissionTree.UserFields : UserFields [R]
UserPermissionTree.UserPermissionForms : UserPermissionForms [R]
UserPermissionTree.UserSignature : Long [R/W]
UserPermissionTree.Add() -> Long
UserPermissionTree.GetAsXML() -> String
UserPermissionTree.GetByKey(ByVal PermissionID As String) -> Boolean
UserPermissionTree.Remove() -> Long
UserPermissionTree.SaveToFile(ByVal FileName As String)
UserPermissionTree.SaveXML(ByRef FileName As String)
UserPermissionTree.Update() -> Long
UserQueries.Browser : DataBrowser [R]
UserQueries.EnableMenuEntry : BoYesNoEnum [R/W]
UserQueries.InternalKey : Long [R]
UserQueries.MenuCaption : String [R/W]
UserQueries.MenuPosition : Long [R/W]
UserQueries.MenuUniqueID : String [R/W]
UserQueries.ParentMenuID : Long [R/W]
UserQueries.ProcedureAlias : String [R/W]
UserQueries.ProcedureName : String [R/W]
UserQueries.Query : String [R/W]
UserQueries.QueryCategory : Long [R/W]
UserQueries.QueryDescription : String [R/W]
UserQueries.QueryType : UserQueryTypeEnum [R/W]
UserQueries.UserFields : UserFields [R]
UserQueries.Add() -> Long
UserQueries.GetAsXML() -> String
UserQueries.GetByKey(ByVal lInternalKey As Long, ByVal lQcategory As Long) -> Boolean
UserQueries.Remove() -> Long
UserQueries.SaveToFile(ByVal bstrFileName As String)
UserQueries.SaveXML(ByRef pbstrFileName As String)
UserQueries.Update() -> Long
Users.Branch : Long [R/W]
Users.Browser : DataBrowser [R]
Users.CashLimit : BoYesNoEnum [R/W]
Users.Defaults : String [R/W]
Users.Department : Long [R/W]
Users.eMail : String [R/W]
Users.FaxNumber : String [R/W]
Users.Group : BoUserGroup [R]
Users.InternalKey : Long [R]
Users.LanguageCode : BoSuppLangs [R/W]
Users.LastLoginTime : Date [R]
Users.LastLogoutDate : Date [R]
Users.LastLogoutTime : Date [R]
Users.LastPasswordChangedBy : String [R]
Users.LastPasswordChangeTime : Date [R]
Users.Locked : BoYesNoEnum [R/W]
Users.MaxCashAmtForIncmngPayts : Double [R/W]
Users.MaxDiscountGeneral : Double [R/W]
Users.MaxDiscountPurchase : Double [R/W]
Users.MaxDiscountSales : Double [R/W]
Users.MobilePhoneNumber : String [R/W]
Users.Superuser : BoYesNoEnum [R/W]
Users.UserActionRecord : UserActionRecord [R]
Users.UserBranchAssignment : UserBranchAssignment [R]
Users.UserCode : String [R/W]
Users.UserFields : UserFields [R]
Users.UserGroupByUser : UserGroupByUser [R]
Users.UserName : String [R/W]
Users.UserPassword : String [R/W]
Users.UserPermission : UserPermission [R]
Users.Add() -> Long
Users.Close() -> Long
Users.GetAsXML() -> String
Users.GetByKey(ByVal InternalKey As Long) -> Boolean
Users.Remove() -> Long
Users.RemoveUserAndLicense() -> Long
Users.SaveToFile(ByVal FileName As String)
Users.SaveXML(ByRef FileName As String)
Users.Update() -> Long
UserTable.ArchiveDate : Date [R/W]
UserTable.Code : String [R/W]
UserTable.Name : String [R/W]
UserTable.TableDescription : String [R]
UserTable.TableName : String [R]
UserTable.UserFields : UserFields [R]
UserTable.Add() -> Long
UserTable.GetAsXML() -> String
UserTable.GetByKey(ByVal Key As String) -> Boolean
UserTable.Remove() -> Long
UserTable.SaveToFile(ByVal FileName As String)
UserTable.SaveXML(ByRef FileName As String)
UserTable.Update() -> Long
UserTables.Count : Long [R]
UserTables.Item(ByVal Index As Variant) -> UserTable
UserTablesMD.Archivable : BoYesNoEnum [R/W]
UserTablesMD.ArchiveDateField : String [R/W]
UserTablesMD.Browser : DataBrowser [R]
UserTablesMD.DisplayMenu : BoYesNoEnum [R/W]
UserTablesMD.TableDescription : String [R/W]
UserTablesMD.TableName : String [R/W]
UserTablesMD.TableType : BoUTBTableType [R/W]
UserTablesMD.Add() -> Long
UserTablesMD.GetAsXML() -> String
UserTablesMD.GetByKey(ByVal TableName As String) -> Boolean
UserTablesMD.Remove() -> Long
UserTablesMD.SaveToFile(ByVal FileName As String)
UserTablesMD.SaveXML(ByRef FileName As String)
UserTablesMD.Update() -> Long
UserValidValues.Count : Long [R]
UserValidValues.FieldValue : String [R/W]
UserValidValues.UserFields : UserFields [R]
UserValidValues.Add()
UserValidValues.SetCurrentLine(ByVal LineNum As Long)
ValidValue.Description : String [R]
ValidValue.Value : String [R]
ValidValues.Count : Long [R]
ValidValues.Item(ByVal Index As Variant) -> ValidValue
ValidValuesMD.Count : Long [R]
ValidValuesMD.Description : String [R/W]
ValidValuesMD.Value : String [R/W]
ValidValuesMD.Add()
ValidValuesMD.Delete()
ValidValuesMD.SetCurrentLine(ByVal LineNum As Long)
ValueMappingCommunicationData.AbsEntry : Long [R/W]
ValueMappingCommunicationData.CommunicationType : VMCommunicationTypeEnum [R/W]
ValueMappingCommunicationData.EndDate : Date [R/W]
ValueMappingCommunicationData.EndTime : Long [R/W]
ValueMappingCommunicationData.Message : String [R/W]
ValueMappingCommunicationData.ObjectID : Long [R/W]
ValueMappingCommunicationData.StartDate : Date [R/W]
ValueMappingCommunicationData.StartTime : Long [R/W]
ValueMappingCommunicationData.Status : VMCommunicationStatusEnum [R/W]
ValueMappingCommunicationData.ThirdPartySystemId : Long [R/W]
ValueMappingCommunicationData.FromXMLFile(ByVal bstrFileName As String)
ValueMappingCommunicationData.FromXMLString(ByVal bstrXML As String)
ValueMappingCommunicationData.GetXMLSchema() -> String
ValueMappingCommunicationData.ToXMLFile(ByVal bstrFileName As String)
ValueMappingCommunicationData.ToXMLString() -> String
ValueMappingCommunicationParams.AbsEntry : Long [R/W]
ValueMappingCommunicationParams.FromXMLFile(ByVal bstrFileName As String)
ValueMappingCommunicationParams.FromXMLString(ByVal bstrXML As String)
ValueMappingCommunicationParams.GetXMLSchema() -> String
ValueMappingCommunicationParams.ToXMLFile(ByVal bstrFileName As String)
ValueMappingCommunicationParams.ToXMLString() -> String
ValueMappingCommunicationService.AddVMCommunicationObject(ByVal pIValueMappingCommunicationData As ValueMappingCommunicationData) -> ValueMappingCommunicationParams
ValueMappingCommunicationService.GetDataInterface(ByVal enumMSDI As ValueMappingCommunicationServiceDataInterfaces) -> Object
ValueMappingCommunicationService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ValueMappingCommunicationService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ValueMappingCommunicationService.GetVMCommunicationObject(ByVal pIValueMappingCommunicationParams As ValueMappingCommunicationParams) -> ValueMappingCommunicationData
ValueMappingCommunicationService.UpdateVMCommunicationObject(ByVal pIValueMappingCommunicationData As ValueMappingCommunicationData)
ValueMappingParams.AbsEntry : Long [R/W]
ValueMappingParams.FromXMLFile(ByVal bstrFileName As String)
ValueMappingParams.FromXMLString(ByVal bstrXML As String)
ValueMappingParams.GetXMLSchema() -> String
ValueMappingParams.ToXMLFile(ByVal bstrFileName As String)
ValueMappingParams.ToXMLString() -> String
ValueMappingService.AddVMObject(ByVal pIVM_B1ValuesData As VM_B1ValuesData) -> ValueMappingParams
ValueMappingService.GetDataInterface(ByVal enumMSDI As ValueMappingServiceDataInterfaces) -> Object
ValueMappingService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
ValueMappingService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
ValueMappingService.GetMappedB1Value(ByVal pIVM_B1ValuesData As VM_B1ValuesData) -> VM_B1ValuesCollection
ValueMappingService.GetThirdPartyValuesForB1Value(ByVal pIVM_B1ValuesData As VM_B1ValuesData) -> VM_ThirdPartyValuesCollection
ValueMappingService.GetVMObject(ByVal pIValueMappingParams As ValueMappingParams) -> VM_B1ValuesData
ValueMappingService.RemoveMappedValue(ByVal pIVM_ThirdPartyValuesData As VM_ThirdPartyValuesData)
ValueMappingService.RemoveVMObject(ByVal pIValueMappingParams As ValueMappingParams)
ValueMappingService.UpdateVMObject(ByVal pIVM_B1ValuesData As VM_B1ValuesData)
VatGroups.AcquisitionReverse : BoYesNoEnum [R/W]
VatGroups.AcquisitionReverseCorrespondingTaxCode : String [R/W]
VatGroups.AcquisitionTax : String [R/W]
VatGroups.Browser : DataBrowser [R]
VatGroups.CashDiscountAccount : String [R/W]
VatGroups.Category : BoVatCategoryEnum [R/W]
VatGroups.Code : String [R/W]
VatGroups.Correction : BoYesNoEnum [R/W]
VatGroups.DeferredTaxAcc : String [R/W]
VatGroups.DownPaymentTaxOffsetAccount : String [R/W]
VatGroups.EBooksVatCategory : Long [R/W]
VatGroups.EqualizationTaxAccount : String [R/W]
VatGroups.EU : BoYesNoEnum [R/W]
VatGroups.ExcludedTaxSummary : BoYesNoEnum [R/W]
VatGroups.GoodsShipment : String [R/W]
VatGroups.Inactive : BoYesNoEnum [R/W]
VatGroups.Name : String [R/W]
VatGroups.NonDeduct : Double [R/W]
VatGroups.NonDeductAcc : String [R/W]
VatGroups.Report349Code : Report349CodeListEnum [R/W]
VatGroups.ServiceSupply : String [R/W]
VatGroups.StandardTaxCode : String [R/W]
VatGroups.TaxAccount : String [R/W]
VatGroups.TaxRegion : VatGroupsTaxRegionEnum [R/W]
VatGroups.TaxTypeBlackList : TaxTypeBlackListEnum [R/W]
VatGroups.TriangularDeal : String [R/W]
VatGroups.UserFields : UserFields [R]
VatGroups.VatCorrection : String [R/W]
VatGroups.VATDeductibleAccount : String [R/W]
VatGroups.VatGroups_Lines : VatGroups_Lines [R]
VatGroups.VATInRevenueAccount : String [R/W]
VatGroups.Add() -> Long
VatGroups.GetAsXML() -> String
VatGroups.GetByKey(ByVal bstrGroupCode As String) -> Boolean
VatGroups.Remove() -> Long
VatGroups.SaveToFile(ByVal FileName As String)
VatGroups.SaveXML(ByRef FileName As String)
VatGroups.Update() -> Long
VatGroups_Lines.Count : Long [R]
VatGroups_Lines.DatevCode : Long [R/W]
VatGroups_Lines.Effectivefrom : Date [R/W]
VatGroups_Lines.EqualizationTax : Double [R/W]
VatGroups_Lines.Rate : Double [R/W]
VatGroups_Lines.UserFields : UserFields [R]
VatGroups_Lines.Add()
VatGroups_Lines.SetCurrentLine(ByVal LineNum As Long)
VM_B1ValuesCollection.Count : Long [R]
VM_B1ValuesCollection.Add() -> VM_B1ValuesData
VM_B1ValuesCollection.GetXMLSchema() -> String
VM_B1ValuesCollection.Item(ByVal vtIndex As Variant) -> VM_B1ValuesData
VM_B1ValuesCollection.ToXMLFile(ByVal bstrFileName As String)
VM_B1ValuesCollection.ToXMLString() -> String
VM_B1ValuesData.AbsEntry : Long [R]
VM_B1ValuesData.ObjectAbsEntry : String [R/W]
VM_B1ValuesData.ObjectID : Long [R/W]
VM_B1ValuesData.VM_ThirdPartyValuesCollection : VM_ThirdPartyValuesCollection [R]
VM_B1ValuesData.FromXMLFile(ByVal bstrFileName As String)
VM_B1ValuesData.FromXMLString(ByVal bstrXML As String)
VM_B1ValuesData.GetXMLSchema() -> String
VM_B1ValuesData.ToXMLFile(ByVal bstrFileName As String)
VM_B1ValuesData.ToXMLString() -> String
VM_ThirdPartyValuesCollection.Count : Long [R]
VM_ThirdPartyValuesCollection.Add() -> VM_ThirdPartyValuesData
VM_ThirdPartyValuesCollection.GetXMLSchema() -> String
VM_ThirdPartyValuesCollection.Item(ByVal vtIndex As Variant) -> VM_ThirdPartyValuesData
VM_ThirdPartyValuesCollection.ToXMLFile(ByVal bstrFileName As String)
VM_ThirdPartyValuesCollection.ToXMLString() -> String
VM_ThirdPartyValuesData.AbsEntry : Long [R]
VM_ThirdPartyValuesData.LineId : Long [R]
VM_ThirdPartyValuesData.ThirdPartySystemId : Long [R/W]
VM_ThirdPartyValuesData.ThirdPartyValue : String [R/W]
VM_ThirdPartyValuesData.FromXMLFile(ByVal bstrFileName As String)
VM_ThirdPartyValuesData.FromXMLString(ByVal bstrXML As String)
VM_ThirdPartyValuesData.GetXMLSchema() -> String
VM_ThirdPartyValuesData.ToXMLFile(ByVal bstrFileName As String)
VM_ThirdPartyValuesData.ToXMLString() -> String
WarehouseLocations.AssesseeType : String [R/W]
WarehouseLocations.Block : String [R/W]
WarehouseLocations.Browser : DataBrowser [R]
WarehouseLocations.BuildingFloorRoom : String [R/W]
WarehouseLocations.CECommissionerate : String [R/W]
WarehouseLocations.CEDivision : String [R/W]
WarehouseLocations.CERange : String [R/W]
WarehouseLocations.CERegisterNumber : String [R/W]
WarehouseLocations.City : String [R/W]
WarehouseLocations.Code : Long [R]
WarehouseLocations.CompanyType : String [R/W]
WarehouseLocations.Country : String [R/W]
WarehouseLocations.County : String [R/W]
WarehouseLocations.CSTNumber : String [R/W]
WarehouseLocations.EccNumber : String [R/W]
WarehouseLocations.ExemptionNumber : String [R/W]
WarehouseLocations.GSTIN : String [R/W]
WarehouseLocations.GSTISD : String [R/W]
WarehouseLocations.GSTTDS : String [R/W]
WarehouseLocations.GstType : BoGSTRegnTypeEnum [R/W]
WarehouseLocations.Jurisdiction : String [R/W]
WarehouseLocations.LSTVATNumber : String [R/W]
WarehouseLocations.ManufacturerCode : String [R/W]
WarehouseLocations.Name : String [R/W]
WarehouseLocations.NatureOfBusiness : String [R/W]
WarehouseLocations.PANNumber : String [R/W]
WarehouseLocations.RegistrationType : String [R]
WarehouseLocations.ServiceTaxNumber : String [R/W]
WarehouseLocations.State : String [R/W]
WarehouseLocations.Street : String [R/W]
WarehouseLocations.TANNumber : String [R/W]
WarehouseLocations.TINNumber : String [R/W]
WarehouseLocations.UserFields : UserFields [R]
WarehouseLocations.ZipCode : String [R/W]
WarehouseLocations.Add() -> Long
WarehouseLocations.GetAsXML() -> String
WarehouseLocations.GetByKey(ByVal lCode As Long) -> Boolean
WarehouseLocations.SaveToFile(ByVal bstrFileName As String)
WarehouseLocations.SaveXML(ByRef pbstrFileName As String)
WarehouseLocations.Update() -> Long
Warehouses.AddressName2 : String [R/W]
Warehouses.AddressName3 : String [R/W]
Warehouses.AddressType : String [R/W]
Warehouses.AllowUseTax : BoYesNoEnum [R/W]
Warehouses.AutoAllocOnIssue : BoDocWhsAutoIssueMethod [R/W]
Warehouses.AutoAllocOnReceipt : AutoAllocOnReceiptMethodEnum [R/W]
Warehouses.BinLocCodeSeparator : String [R/W]
Warehouses.Block : String [R/W]
Warehouses.Browser : DataBrowser [R]
Warehouses.BuildingFloorRoom : String [R/W]
Warehouses.BusinessPlaceID : Long [R/W]
Warehouses.City : String [R/W]
Warehouses.CostInflationAccount : String [R/W]
Warehouses.CostInflationOffsetAccount : String [R/W]
Warehouses.CostOfGoodsSold : String [R/W]
Warehouses.Country : String [R/W]
Warehouses.County : String [R/W]
Warehouses.DecreaseGLAccount : String [R/W]
Warehouses.DecreasingAccount : String [R/W]
Warehouses.DefaultBin : Long [R/W]
Warehouses.DefaultBinEnforced : BoYesNoEnum [R/W]
Warehouses.DropShip : BoYesNoEnum [R/W]
Warehouses.EnableBinLocations : BoYesNoEnum [R/W]
Warehouses.EnableReceivingBinLocations : BoYesNoEnum [R/W]
Warehouses.EUExpensesAccount : String [R/W]
Warehouses.EUPurchaseCreditAcc : String [R/W]
Warehouses.EURevenuesAccount : String [R/W]
Warehouses.ExchangeRateDifferencesAccount : String [R/W]
Warehouses.Excisable : BoYesNoEnum [R/W]
Warehouses.ExemptedCredits : String [R/W]
Warehouses.ExemptRevenuesAccount : String [R/W]
Warehouses.ExpenseAccount : String [R/W]
Warehouses.ExpenseOffsetingAct : String [R/W]
Warehouses.ExpensesClearingAccount : String [R/W]
Warehouses.External : BoYesNoEnum [R/W]
Warehouses.FederalTaxID : String [R/W]
Warehouses.ForeignExpensesAccount : String [R/W]
Warehouses.ForeignPurchaseCreditAcc : String [R/W]
Warehouses.ForeignRevenuesAcc : String [R/W]
Warehouses.GlobalLocationNumber : String [R/W]
Warehouses.GoodsClearingAcc : String [R/W]
Warehouses.Inactive : BoYesNoEnum [R/W]
Warehouses.IncreaseGLAccount : String [R/W]
Warehouses.IncreasingAcc : String [R/W]
Warehouses.InternalKey : Long [R]
Warehouses.InventoryOffsetProfitAndLossAccount : String [R/W]
Warehouses.LegalText : String [R/W]
Warehouses.Location : Long [R/W]
Warehouses.ManageSerialAndBatchNumbers : BoYesNoEnum [R/W]
Warehouses.NegativeInventoryAdjustmentAccount : String [R/W]
Warehouses.Nettable : BoYesNoEnum [R/W]
Warehouses.PriceDifferencesAccount : String [R/W]
Warehouses.PurchaseAccount : String [R/W]
Warehouses.PurchaseBalanceAccount : String [R/W]
Warehouses.PurchaseCreditAcc : String [R/W]
Warehouses.PurchaseOffsetAccount : String [R/W]
Warehouses.PurchaseReturningAccount : String [R/W]
Warehouses.ReceiveUpToMaxQuantity : BoYesNoEnum [R/W]
Warehouses.ReceiveUpToMaxWeight : BoYesNoEnum [R/W]
Warehouses.ReceiveUpToMethod : ReceivingUpToMethodEnum [R/W]
Warehouses.ReceivingBinLocationsBy : ReceivingBinLocationsMethodEnum [R/W]
Warehouses.RestrictReceiptToEmptyBinLocation : BoYesNoEnum [R/W]
Warehouses.ReturningAccount : String [R/W]
Warehouses.RevenuesAccount : String [R/W]
Warehouses.SalesCreditAcc : String [R/W]
Warehouses.SalesCreditEUAcc : String [R/W]
Warehouses.SalesCreditForeignAcc : String [R/W]
Warehouses.ShippedGoodsAccount : String [R/W]
Warehouses.Shipper : String [R/W]
Warehouses.State : String [R/W]
Warehouses.StockAccount : String [R/W]
Warehouses.StockInflationAdjustAccount : String [R/W]
Warehouses.StockInflationOffsetAccount : String [R/W]
Warehouses.StockInTransitAccount : String [R/W]
Warehouses.Storekeeper : Long [R/W]
Warehouses.Street : String [R/W]
Warehouses.StreetNo : String [R/W]
Warehouses.TaxGroup : String [R/W]
Warehouses.TaxOffice : String [R/W]
Warehouses.TransfersAcc : String [R/W]
Warehouses.UserFields : UserFields [R]
Warehouses.VarianceAccount : String [R/W]
Warehouses.VATInRevenueAccount : String [R/W]
Warehouses.WarehouseCode : String [R/W]
Warehouses.WarehouseName : String [R/W]
Warehouses.WHIncomingCenvatAccount : String [R/W]
Warehouses.WHOutgoingCenvatAccount : String [R/W]
Warehouses.WHShipToName : String [R/W]
Warehouses.WIPMaterialAccount : String [R/W]
Warehouses.WIPMaterialVarianceAccount : String [R/W]
Warehouses.WipOffsetProfitAndLossAccount : String [R/W]
Warehouses.ZipCode : String [R/W]
Warehouses.Add() -> Long
Warehouses.GetAsXML() -> String
Warehouses.GetByKey(ByVal WhsCode As String) -> Boolean
Warehouses.Remove() -> Long
Warehouses.SaveToFile(ByVal FileName As String)
Warehouses.SaveXML(ByRef FileName As String)
Warehouses.Update() -> Long
WarehouseSublevelCode.AbsEntry : Long [R]
WarehouseSublevelCode.Code : String [R/W]
WarehouseSublevelCode.Description : String [R/W]
WarehouseSublevelCode.WarehouseSublevel : Long [R/W]
WarehouseSublevelCode.FromXMLFile(ByVal bstrFileName As String)
WarehouseSublevelCode.FromXMLString(ByVal bstrXML As String)
WarehouseSublevelCode.GetXMLSchema() -> String
WarehouseSublevelCode.ToXMLFile(ByVal bstrFileName As String)
WarehouseSublevelCode.ToXMLString() -> String
WarehouseSublevelCodeCollectionParams.Count : Long [R]
WarehouseSublevelCodeCollectionParams.Add() -> WarehouseSublevelCodeParams
WarehouseSublevelCodeCollectionParams.GetXMLSchema() -> String
WarehouseSublevelCodeCollectionParams.Item(ByVal vtIndex As Variant) -> WarehouseSublevelCodeParams
WarehouseSublevelCodeCollectionParams.ToXMLFile(ByVal bstrFileName As String)
WarehouseSublevelCodeCollectionParams.ToXMLString() -> String
WarehouseSublevelCodeParams.AbsEntry : Long [R/W]
WarehouseSublevelCodeParams.Code : String [R/W]
WarehouseSublevelCodeParams.WarehouseSublevel : Long [R/W]
WarehouseSublevelCodeParams.FromXMLFile(ByVal bstrFileName As String)
WarehouseSublevelCodeParams.FromXMLString(ByVal bstrXML As String)
WarehouseSublevelCodeParams.GetXMLSchema() -> String
WarehouseSublevelCodeParams.ToXMLFile(ByVal bstrFileName As String)
WarehouseSublevelCodeParams.ToXMLString() -> String
WarehouseSublevelCodesService.Add(ByVal pIWarehouseSublevelCode As WarehouseSublevelCode) -> WarehouseSublevelCodeParams
WarehouseSublevelCodesService.Delete(ByVal pIWarehouseSublevelCodeParams As WarehouseSublevelCodeParams)
WarehouseSublevelCodesService.Get(ByVal pIWarehouseSublevelCodeParams As WarehouseSublevelCodeParams) -> WarehouseSublevelCode
WarehouseSublevelCodesService.GetDataInterface(ByVal enumMSDI As WarehouseSublevelCodesServiceDataInterfaces) -> Object
WarehouseSublevelCodesService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
WarehouseSublevelCodesService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
WarehouseSublevelCodesService.GetList() -> WarehouseSublevelCodeCollectionParams
WarehouseSublevelCodesService.Update(ByVal pIWarehouseSublevelCode As WarehouseSublevelCode)
WeightMeasures.Browser : DataBrowser [R]
WeightMeasures.UnitCode : Long [R]
WeightMeasures.UnitDisplay : String [R/W]
WeightMeasures.UnitName : String [R/W]
WeightMeasures.UnitWeightinmg : Double [R/W]
WeightMeasures.UserFields : UserFields [R]
WeightMeasures.Add() -> Long
WeightMeasures.GetAsXML() -> String
WeightMeasures.GetByKey(ByVal lUnitCode As Long) -> Boolean
WeightMeasures.Remove() -> Long
WeightMeasures.SaveToFile(ByVal bstrFileName As String)
WeightMeasures.SaveXML(ByRef pbstrFileName As String)
WeightMeasures.Update() -> Long
WIPMapping.AbsoluteEntry : Long [R]
WIPMapping.AccountFrom : String [R/W]
WIPMapping.AccountTo : String [R/W]
WIPMapping.LineNumber : Long [R]
WIPMapping.FromXMLFile(ByVal bstrFileName As String)
WIPMapping.FromXMLString(ByVal bstrXML As String)
WIPMapping.GetXMLSchema() -> String
WIPMapping.ToXMLFile(ByVal bstrFileName As String)
WIPMapping.ToXMLString() -> String
WIPMappingCollection.Count : Long [R]
WIPMappingCollection.Add() -> WIPMapping
WIPMappingCollection.GetXMLSchema() -> String
WIPMappingCollection.Item(ByVal vtIndex As Variant) -> WIPMapping
WIPMappingCollection.Remove(ByVal vtIndex As Variant)
WIPMappingCollection.ToXMLFile(ByVal bstrFileName As String)
WIPMappingCollection.ToXMLString() -> String
WithholdingTaxCertificates.Certificate : String [R/W]
WithholdingTaxCertificates.Count : Long [R]
WithholdingTaxCertificates.IssueDate : Date [R/W]
WithholdingTaxCertificates.Number : Long [R/W]
WithholdingTaxCertificates.PeriodIndicator : String [R]
WithholdingTaxCertificates.POICode : String [R/W]
WithholdingTaxCertificates.POICodeRef : String [R/W]
WithholdingTaxCertificates.Series : Long [R/W]
WithholdingTaxCertificates.SumAccumulatedAmount : Double [R]
WithholdingTaxCertificates.SumBaseAmount : Double [R]
WithholdingTaxCertificates.SumDocTotal : Double [R]
WithholdingTaxCertificates.SumPerceptAmount : Double [R]
WithholdingTaxCertificates.SumVATAmount : Double [R]
WithholdingTaxCertificates.WhtAbsId : Long [R/W]
WithholdingTaxCertificates.WTaxType : String [R]
WithholdingTaxCertificates.WTGroups : WTGroups [R]
WithholdingTaxCertificates.Add()
WithholdingTaxCertificates.SetCurrentLine(ByVal LineNum As Long)
WithholdingTaxCodes.Account : String [R/W]
WithholdingTaxCodes.APCessAccount : String [R/W]
WithholdingTaxCodes.APCessGSTAccount : String [R/W]
WithholdingTaxCodes.APCessInterimAccount : String [R/W]
WithholdingTaxCodes.APCGSTAccount : String [R/W]
WithholdingTaxCodes.APHSCAccount : String [R/W]
WithholdingTaxCodes.APHSCInterimAccount : String [R/W]
WithholdingTaxCodes.APIGSTAccount : String [R/W]
WithholdingTaxCodes.APSGSTAccount : String [R/W]
WithholdingTaxCodes.APSurchargeAccount : String [R/W]
WithholdingTaxCodes.APSurchargeInterimAccount : String [R/W]
WithholdingTaxCodes.APTCSInterimAccount : String [R/W]
WithholdingTaxCodes.APTDSAccount : String [R/W]
WithholdingTaxCodes.APUTGSTAccount : String [R/W]
WithholdingTaxCodes.ARCessAccount : String [R/W]
WithholdingTaxCodes.ARCessGSTAccount : String [R/W]
WithholdingTaxCodes.ARCessInterimAccount : String [R/W]
WithholdingTaxCodes.ARCGSTAccount : String [R/W]
WithholdingTaxCodes.ARHSCAccount : String [R/W]
WithholdingTaxCodes.ARHSCInterimAccount : String [R/W]
WithholdingTaxCodes.ARIGSTAccount : String [R/W]
WithholdingTaxCodes.ARSGSTAccount : String [R/W]
WithholdingTaxCodes.ARSurchargeAccount : String [R/W]
WithholdingTaxCodes.ARSurchargeInterimAccount : String [R/W]
WithholdingTaxCodes.ARTCSInterimAccount : String [R/W]
WithholdingTaxCodes.ARTDSAccount : String [R/W]
WithholdingTaxCodes.ARUTGSTAccount : String [R/W]
WithholdingTaxCodes.Assessee : Long [R/W]
WithholdingTaxCodes.BaseAmount : Double [R/W]
WithholdingTaxCodes.BaseType : WithholdingTaxCodeBaseTypeEnum [R/W]
WithholdingTaxCodes.Browser : DataBrowser [R]
WithholdingTaxCodes.Category : WithholdingTaxCodeCategoryEnum [R/W]
WithholdingTaxCodes.Concessional : BoYesNoEnum [R/W]
WithholdingTaxCodes.CSTCodeIncomingID : Long [R/W]
WithholdingTaxCodes.CSTCodeOutgoingID : Long [R/W]
WithholdingTaxCodes.Currency : String [R/W]
WithholdingTaxCodes.EBooksWTaxCategory : Long [R/W]
WithholdingTaxCodes.Effectivefrom : Date [R]
WithholdingTaxCodes.Inactive : BoYesNoEnum [R/W]
WithholdingTaxCodes.IsProgressiveTax : BoYesNoEnum [R/W]
WithholdingTaxCodes.Lines : WithholdingTaxCodes_Lines [R]
WithholdingTaxCodes.Location : Long [R/W]
WithholdingTaxCodes.MinimumTaxableAmount : Double [R/W]
WithholdingTaxCodes.NatureOfCalculationBaseCode : String [R/W]
WithholdingTaxCodes.NonDeductThreshold : BoYesNoEnum [R/W]
WithholdingTaxCodes.OfficialCode : String [R/W]
WithholdingTaxCodes.Rate : Double [R]
WithholdingTaxCodes.ReturnType : ReturnTypeEnum [R/W]
WithholdingTaxCodes.RoundingType : RoundingTypeEnum [R/W]
WithholdingTaxCodes.Section : Long [R/W]
WithholdingTaxCodes.Surcharge : Double [R/W]
WithholdingTaxCodes.TdsType : TdsTypeEnum [R/W]
WithholdingTaxCodes.Threshold : Double [R/W]
WithholdingTaxCodes.TransactonThreshold : Double [R/W]
WithholdingTaxCodes.TypeID : Long [R/W]
WithholdingTaxCodes.UserFields : UserFields [R]
WithholdingTaxCodes.WithholdingType : WithholdingTypeEnum [R/W]
WithholdingTaxCodes.WTCode : String [R/W]
WithholdingTaxCodes.WTName : String [R/W]
WithholdingTaxCodes.Add() -> Long
WithholdingTaxCodes.GetAsXML() -> String
WithholdingTaxCodes.GetByKey(ByVal bstrWtCode As String) -> Boolean
WithholdingTaxCodes.Remove() -> Long
WithholdingTaxCodes.SaveToFile(ByVal bstrFileName As String)
WithholdingTaxCodes.SaveXML(ByRef pbstrFileName As String)
WithholdingTaxCodes.Update() -> Long
WithholdingTaxCodes_Lines.CessGSTRate : Double [R/W]
WithholdingTaxCodes_Lines.CessRate : Double [R/W]
WithholdingTaxCodes_Lines.CGSTRate : Double [R/W]
WithholdingTaxCodes_Lines.Count : Long [R]
WithholdingTaxCodes_Lines.Currency : String [R/W]
WithholdingTaxCodes_Lines.Effectivefrom : Date [R/W]
WithholdingTaxCodes_Lines.FixedAmount : Double [R/W]
WithholdingTaxCodes_Lines.HSCRate : Double [R/W]
WithholdingTaxCodes_Lines.IGSTRate : Double [R/W]
WithholdingTaxCodes_Lines.ITRNonCompliantRate : Double [R/W]
WithholdingTaxCodes_Lines.LineNum : Long [R]
WithholdingTaxCodes_Lines.PANNonCompliantRate : Double [R/W]
WithholdingTaxCodes_Lines.ProgressiveTaxLines : WithholdingTaxCodes_ProgressiveTax_Lines [R]
WithholdingTaxCodes_Lines.Rate : Double [R/W]
WithholdingTaxCodes_Lines.SGSTRate : Double [R/W]
WithholdingTaxCodes_Lines.SurchargeRate : Double [R/W]
WithholdingTaxCodes_Lines.TDSRate : Double [R/W]
WithholdingTaxCodes_Lines.UoMCode : String [R]
WithholdingTaxCodes_Lines.UoMEntry : Long [R/W]
WithholdingTaxCodes_Lines.UserFields : UserFields [R]
WithholdingTaxCodes_Lines.UTGSTRate : Double [R/W]
WithholdingTaxCodes_Lines.ValueRangeLines : WithholdingTaxCodes_ValueRange_Lines [R]
WithholdingTaxCodes_Lines.Add()
WithholdingTaxCodes_Lines.Delete()
WithholdingTaxCodes_Lines.SetCurrentLine(ByVal LineNum As Long)
WithholdingTaxCodes_ProgressiveTax_Lines.Count : Long [R]
WithholdingTaxCodes_ProgressiveTax_Lines.MaxAmount : Double [R/W]
WithholdingTaxCodes_ProgressiveTax_Lines.MinAmount : Double [R/W]
WithholdingTaxCodes_ProgressiveTax_Lines.TaxRate : Double [R/W]
WithholdingTaxCodes_ProgressiveTax_Lines.UserFields : UserFields [R]
WithholdingTaxCodes_ProgressiveTax_Lines.Add()
WithholdingTaxCodes_ProgressiveTax_Lines.Delete()
WithholdingTaxCodes_ProgressiveTax_Lines.SetCurrentLine(ByVal LineNum As Long)
WithholdingTaxCodes_ValueRange_Lines.Count : Long [R]
WithholdingTaxCodes_ValueRange_Lines.Rate : Double [R/W]
WithholdingTaxCodes_ValueRange_Lines.UserFields : UserFields [R]
WithholdingTaxCodes_ValueRange_Lines.ValueFrom : Double [R/W]
WithholdingTaxCodes_ValueRange_Lines.WTaxToBeDeductible : Double [R/W]
WithholdingTaxCodes_ValueRange_Lines.Add()
WithholdingTaxCodes_ValueRange_Lines.Delete()
WithholdingTaxCodes_ValueRange_Lines.SetCurrentLine(ByVal LineNum As Long)
WithholdingTaxData.BaseDocEntry : Long [R/W]
WithholdingTaxData.BaseDocLine : Long [R/W]
WithholdingTaxData.BaseDocType : Long [R/W]
WithholdingTaxData.BaseDocumentReference : Long [R]
WithholdingTaxData.BaseType : String [R]
WithholdingTaxData.Category : String [R]
WithholdingTaxData.Count : Long [R]
WithholdingTaxData.Criteria : String [R]
WithholdingTaxData.GLAccount : String [R]
WithholdingTaxData.LineNum : Long [R]
WithholdingTaxData.Rate : Double [R]
WithholdingTaxData.RoundingType : String [R]
WithholdingTaxData.Status : BoStatus [R]
WithholdingTaxData.TargetAbsEntry : Long [R]
WithholdingTaxData.TargetDocumentType : Long [R]
WithholdingTaxData.TaxableAmount : Double [R/W]
WithholdingTaxData.TaxableAmountFC : Double [R/W]
WithholdingTaxData.TaxableAmountinSys : Double [R/W]
WithholdingTaxData.UserFields : UserFields [R]
WithholdingTaxData.WithholdingType : String [R]
WithholdingTaxData.WTAmount : Double [R/W]
WithholdingTaxData.WTAmountFC : Double [R/W]
WithholdingTaxData.WTAmountSys : Double [R/W]
WithholdingTaxData.WTCode : String [R/W]
WithholdingTaxData.Add()
WithholdingTaxData.SetCurrentLine(ByVal LineNum As Long)
WithholdingTaxDataWTX.AccumBaseAmount : Double [R]
WithholdingTaxDataWTX.AccumBaseAmountFC : Double [R]
WithholdingTaxDataWTX.AccumBaseAmountSys : Double [R]
WithholdingTaxDataWTX.AccumWTaxAmount : Double [R]
WithholdingTaxDataWTX.AccumWTaxAmountFC : Double [R]
WithholdingTaxDataWTX.AccumWTaxAmountSys : Double [R]
WithholdingTaxDataWTX.BaseDocEntry : Long [R]
WithholdingTaxDataWTX.BaseDocLine : Long [R]
WithholdingTaxDataWTX.BaseDocType : Long [R]
WithholdingTaxDataWTX.BaseDocumentReference : Long [R]
WithholdingTaxDataWTX.BaseNetAmount : Double [R]
WithholdingTaxDataWTX.BaseNetAmountFC : Double [R]
WithholdingTaxDataWTX.BaseNetAmountSys : Double [R]
WithholdingTaxDataWTX.BaseType : String [R]
WithholdingTaxDataWTX.BaseVatAmount : Double [R]
WithholdingTaxDataWTX.BaseVatAmountFC : Double [R]
WithholdingTaxDataWTX.BaseVatAmountSys : Double [R]
WithholdingTaxDataWTX.Category : String [R]
WithholdingTaxDataWTX.Count : Long [R]
WithholdingTaxDataWTX.Criteria : String [R]
WithholdingTaxDataWTX.ExemptRate : Double [R/W]
WithholdingTaxDataWTX.GLAccount : String [R]
WithholdingTaxDataWTX.LineNum : Long [R]
WithholdingTaxDataWTX.Rate : Double [R/W]
WithholdingTaxDataWTX.RoundingType : String [R]
WithholdingTaxDataWTX.Status : BoStatus [R]
WithholdingTaxDataWTX.TargetAbsEntry : Long [R]
WithholdingTaxDataWTX.TargetDocumentType : Long [R]
WithholdingTaxDataWTX.TaxableAmount : Double [R/W]
WithholdingTaxDataWTX.TaxableAmountFC : Double [R/W]
WithholdingTaxDataWTX.TaxableAmountinSys : Double [R/W]
WithholdingTaxDataWTX.UserFields : UserFields [R]
WithholdingTaxDataWTX.WithholdingType : String [R]
WithholdingTaxDataWTX.WTAbsId : String [R/W]
WithholdingTaxDataWTX.WTAmount : Double [R/W]
WithholdingTaxDataWTX.WTAmountFC : Double [R/W]
WithholdingTaxDataWTX.WTAmountSys : Double [R/W]
WithholdingTaxDataWTX.WTCode : String [R]
WithholdingTaxDataWTX.Add()
WithholdingTaxDataWTX.SetCurrentLine(ByVal LineNum As Long)
WithholdingTaxLines.BaseDocEntry : Long [R/W]
WithholdingTaxLines.BaseDocLine : Long [R/W]
WithholdingTaxLines.BaseDocType : Long [R/W]
WithholdingTaxLines.BaseType : String [R]
WithholdingTaxLines.Category : String [R]
WithholdingTaxLines.Count : Long [R]
WithholdingTaxLines.Criteria : String [R]
WithholdingTaxLines.CSTCodeIncoming : String [R/W]
WithholdingTaxLines.CSTCodeOutgoing : String [R/W]
WithholdingTaxLines.GLAccount : String [R]
WithholdingTaxLines.LineNum : Long [R]
WithholdingTaxLines.Rate : Double [R]
WithholdingTaxLines.RoundingType : String [R]
WithholdingTaxLines.TaxableAmount : Double [R/W]
WithholdingTaxLines.TaxableAmountFC : Double [R/W]
WithholdingTaxLines.TaxableAmountinSys : Double [R/W]
WithholdingTaxLines.UserFields : UserFields [R]
WithholdingTaxLines.WithholdingType : String [R]
WithholdingTaxLines.WTAmount : Double [R/W]
WithholdingTaxLines.WTAmountFC : Double [R/W]
WithholdingTaxLines.WTAmountSys : Double [R/W]
WithholdingTaxLines.WTCode : String [R/W]
WithholdingTaxLines.Add()
WithholdingTaxLines.SetCurrentLine(ByVal LineNum As Long)
WitholdingTaxDefinitionService.AddWTDCode(ByVal pIWTDCode As WTDCode) -> WTDCodeParamsCollection
WitholdingTaxDefinitionService.Delete(ByVal pIWTDCodeParamsCollection As WTDCodeParamsCollection)
WitholdingTaxDefinitionService.Get(ByVal pIWTDCodeParams As WTDCodeParams) -> WTDCode
WitholdingTaxDefinitionService.GetDataInterface(ByVal enumMSDI As WitholdingTaxDefinitionServiceDataInterfaces) -> Object
WitholdingTaxDefinitionService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
WitholdingTaxDefinitionService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
WitholdingTaxDefinitionService.UpdateWTDCode(ByVal pIWTDCode As WTDCode)
WizardPaymentMethods.Accepted : String [R/W]
WizardPaymentMethods.Active : BoYesNoEnum [R/W]
WizardPaymentMethods.AgentCollection : BoYesNoEnum [R/W]
WizardPaymentMethods.BankAccountKey : Long [R]
WizardPaymentMethods.BankChargeRate : Double [R/W]
WizardPaymentMethods.BankCountry : String [R/W]
WizardPaymentMethods.BarcodeDll : String [R/W]
WizardPaymentMethods.BlockForeignBank : BoYesNoEnum [R/W]
WizardPaymentMethods.BlockForeignPayment : BoYesNoEnum [R/W]
WizardPaymentMethods.Branch : String [R]
WizardPaymentMethods.Browser : DataBrowser [R]
WizardPaymentMethods.CancelInstruction : String [R/W]
WizardPaymentMethods.CheckAddress : BoYesNoEnum [R/W]
WizardPaymentMethods.CheckBankDetails : BoYesNoEnum [R/W]
WizardPaymentMethods.CollectionAuthorizationCheck : BoYesNoEnum [R/W]
WizardPaymentMethods.CreationDate : Date [R]
WizardPaymentMethods.CurCode : String [R/W]
WizardPaymentMethods.CurrencyRestriction : BoYesNoEnum [R/W]
WizardPaymentMethods.CurrencyRestrictions : CurrencyRestrictions [R]
WizardPaymentMethods.DebitMemo : BoYesNoEnum [R/W]
WizardPaymentMethods.DefaultAccount : String [R/W]
WizardPaymentMethods.DefaultBank : String [R/W]
WizardPaymentMethods.DepositNorm : String [R/W]
WizardPaymentMethods.Description : String [R/W]
WizardPaymentMethods.DirectDebit : DirectDebitTypeEnum [R/W]
WizardPaymentMethods.DocType : String [R/W]
WizardPaymentMethods.DueDateSelection : BoDueDateEnum [R/W]
WizardPaymentMethods.Format : String [R/W]
WizardPaymentMethods.GLAccount : String [R]
WizardPaymentMethods.GroupByDate : BoYesNoEnum [R/W]
WizardPaymentMethods.GroupByPaymentReference : BoYesNoEnum [R/W]
WizardPaymentMethods.GroupInvoicesByCurrency : BoYesNoEnum [R/W]
WizardPaymentMethods.GroupInvoicesbyPay : BoYesNoEnum [R/W]
WizardPaymentMethods.GroupInvoicesByPayToBank : BoYesNoEnum [R/W]
WizardPaymentMethods.Instruction1 : String [R/W]
WizardPaymentMethods.Instruction2 : String [R/W]
WizardPaymentMethods.KeyCode : String [R/W]
WizardPaymentMethods.MaximumAmount : Double [R/W]
WizardPaymentMethods.MinimumAmount : Double [R/W]
WizardPaymentMethods.MovementCode : String [R/W]
WizardPaymentMethods.OccurenceCode : String [R/W]
WizardPaymentMethods.PaymentMeans : BoPaymentMeansEnum [R/W]
WizardPaymentMethods.PaymentMethodCode : String [R/W]
WizardPaymentMethods.PaymentPlace : String [R/W]
WizardPaymentMethods.PaymentTermsCode : Long [R/W]
WizardPaymentMethods.PortfolioID : String [R/W]
WizardPaymentMethods.PostOfficeBank : BoYesNoEnum [R/W]
WizardPaymentMethods.PosttoGLInterimAccount : BoYesNoEnum [R/W]
WizardPaymentMethods.ReportCode : String [R/W]
WizardPaymentMethods.SendforAcceptance : BoYesNoEnum [R/W]
WizardPaymentMethods.TransactionType : String [R/W]
WizardPaymentMethods.Type : BoPaymentTypeEnum [R/W]
WizardPaymentMethods.UserFields : UserFields [R]
WizardPaymentMethods.UserSignature : Long [R]
WizardPaymentMethods.Add() -> Long
WizardPaymentMethods.GetAsXML() -> String
WizardPaymentMethods.GetByKey(ByVal bstrCode As String) -> Boolean
WizardPaymentMethods.Remove() -> Long
WizardPaymentMethods.SaveToFile(ByVal bstrFileName As String)
WizardPaymentMethods.SaveXML(ByRef pbstrFileName As String)
WizardPaymentMethods.Update() -> Long
WorkflowApprovalTaskListParams.Status : String [R/W]
WorkflowApprovalTaskListParams.FromXMLFile(ByVal bstrFileName As String)
WorkflowApprovalTaskListParams.FromXMLString(ByVal bstrXML As String)
WorkflowApprovalTaskListParams.GetXMLSchema() -> String
WorkflowApprovalTaskListParams.ToXMLFile(ByVal bstrFileName As String)
WorkflowApprovalTaskListParams.ToXMLString() -> String
WorkflowTask.Description : String [R]
WorkflowTask.InstanceID : Long [R]
WorkflowTask.Name : String [R]
WorkflowTask.Operation : String [R]
WorkflowTask.Owner : String [R]
WorkflowTask.Priority : Long [R]
WorkflowTask.Status : String [R]
WorkflowTask.TaskID : Long [R]
WorkflowTask.TemplateID : String [R]
WorkflowTask.TemplateName : String [R]
WorkflowTask.Type : String [R]
WorkflowTask.WorkflowTaskInputObjectCollection : WorkflowTaskInputObjectCollection [R]
WorkflowTask.WorkflowTaskNoteCollection : WorkflowTaskNoteCollection [R]
WorkflowTask.WorkflowTaskOutputObjectCollection : WorkflowTaskOutputObjectCollection [R]
WorkflowTask.FromXMLFile(ByVal bstrFileName As String)
WorkflowTask.FromXMLString(ByVal bstrXML As String)
WorkflowTask.GetXMLSchema() -> String
WorkflowTask.ToXMLFile(ByVal bstrFileName As String)
WorkflowTask.ToXMLString() -> String
WorkflowTaskCollection.Count : Long [R]
WorkflowTaskCollection.Add() -> WorkflowTask
WorkflowTaskCollection.GetXMLSchema() -> String
WorkflowTaskCollection.Item(ByVal vtIndex As Variant) -> WorkflowTask
WorkflowTaskCollection.ToXMLFile(ByVal bstrFileName As String)
WorkflowTaskCollection.ToXMLString() -> String
WorkflowTaskCompleteParams.Note : String [R/W]
WorkflowTaskCompleteParams.TaskID : Long [R/W]
WorkflowTaskCompleteParams.TriggerParams : String [R/W]
WorkflowTaskCompleteParams.FromXMLFile(ByVal bstrFileName As String)
WorkflowTaskCompleteParams.FromXMLString(ByVal bstrXML As String)
WorkflowTaskCompleteParams.GetXMLSchema() -> String
WorkflowTaskCompleteParams.ToXMLFile(ByVal bstrFileName As String)
WorkflowTaskCompleteParams.ToXMLString() -> String
WorkflowTaskInputObject.Detail : String [R]
WorkflowTaskInputObject.Key : String [R]
WorkflowTaskInputObject.LineId : Long [R]
WorkflowTaskInputObject.SubType : String [R]
WorkflowTaskInputObject.TaskID : Long [R]
WorkflowTaskInputObject.Type : String [R]
WorkflowTaskInputObject.FromXMLFile(ByVal bstrFileName As String)
WorkflowTaskInputObject.FromXMLString(ByVal bstrXML As String)
WorkflowTaskInputObject.GetXMLSchema() -> String
WorkflowTaskInputObject.ToXMLFile(ByVal bstrFileName As String)
WorkflowTaskInputObject.ToXMLString() -> String
WorkflowTaskInputObjectCollection.Count : Long [R]
WorkflowTaskInputObjectCollection.Add() -> WorkflowTaskInputObject
WorkflowTaskInputObjectCollection.GetXMLSchema() -> String
WorkflowTaskInputObjectCollection.Item(ByVal vtIndex As Variant) -> WorkflowTaskInputObject
WorkflowTaskInputObjectCollection.ToXMLFile(ByVal bstrFileName As String)
WorkflowTaskInputObjectCollection.ToXMLString() -> String
WorkflowTaskNote.Creator : String [R]
WorkflowTaskNote.LineId : Long [R]
WorkflowTaskNote.Note : String [R]
WorkflowTaskNote.NoteDate : Date [R]
WorkflowTaskNote.TaskID : Long [R]
WorkflowTaskNote.FromXMLFile(ByVal bstrFileName As String)
WorkflowTaskNote.FromXMLString(ByVal bstrXML As String)
WorkflowTaskNote.GetXMLSchema() -> String
WorkflowTaskNote.ToXMLFile(ByVal bstrFileName As String)
WorkflowTaskNote.ToXMLString() -> String
WorkflowTaskNoteCollection.Count : Long [R]
WorkflowTaskNoteCollection.Add() -> WorkflowTaskNote
WorkflowTaskNoteCollection.GetXMLSchema() -> String
WorkflowTaskNoteCollection.Item(ByVal vtIndex As Variant) -> WorkflowTaskNote
WorkflowTaskNoteCollection.ToXMLFile(ByVal bstrFileName As String)
WorkflowTaskNoteCollection.ToXMLString() -> String
WorkflowTaskOutputObject.Key : String [R]
WorkflowTaskOutputObject.LineId : String [R]
WorkflowTaskOutputObject.SubType : String [R]
WorkflowTaskOutputObject.TaskID : Long [R]
WorkflowTaskOutputObject.Type : String [R]
WorkflowTaskOutputObject.FromXMLFile(ByVal bstrFileName As String)
WorkflowTaskOutputObject.FromXMLString(ByVal bstrXML As String)
WorkflowTaskOutputObject.GetXMLSchema() -> String
WorkflowTaskOutputObject.ToXMLFile(ByVal bstrFileName As String)
WorkflowTaskOutputObject.ToXMLString() -> String
WorkflowTaskOutputObjectCollection.Count : Long [R]
WorkflowTaskOutputObjectCollection.Add() -> WorkflowTaskOutputObject
WorkflowTaskOutputObjectCollection.GetXMLSchema() -> String
WorkflowTaskOutputObjectCollection.Item(ByVal vtIndex As Variant) -> WorkflowTaskOutputObject
WorkflowTaskOutputObjectCollection.ToXMLFile(ByVal bstrFileName As String)
WorkflowTaskOutputObjectCollection.ToXMLString() -> String
WorkflowTaskService.Complete(ByVal pIWorkflowTaskCompleteParams As WorkflowTaskCompleteParams)
WorkflowTaskService.GetApprovalTaskList(ByVal pIWorkflowApprovalTaskListParams As WorkflowApprovalTaskListParams) -> WorkflowTaskCollection
WorkflowTaskService.GetDataInterface(ByVal enumMSDI As WorkflowTaskServiceDataInterfaces) -> Object
WorkflowTaskService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
WorkflowTaskService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
WorkOrder_Lines.ActiveAccountCode : String [R/W]
WorkOrder_Lines.Count : Long [R]
WorkOrder_Lines.ItemCode : String [R/W]
WorkOrder_Lines.ItemDescription : String [R]
WorkOrder_Lines.ItemPrice : Double [R/W]
WorkOrder_Lines.ItemQuantity : Double [R/W]
WorkOrder_Lines.ItemWarehouse : String [R/W]
WorkOrder_Lines.PriceCurrency : String [R/W]
WorkOrder_Lines.RowNumber : Long [R]
WorkOrder_Lines.UserFields : UserFields [R]
WorkOrder_Lines.WorkSum : Double [R/W]
WorkOrder_Lines.Add()
WorkOrder_Lines.SetCurrentLine(ByVal LineNum As Long)
WorkOrders.ActiveAccountCode : String [R/W]
WorkOrders.Browser : DataBrowser [R]
WorkOrders.Canceled : BoYesNoEnum [R]
WorkOrders.Comment : String [R/W]
WorkOrders.ContactPerson : Long [R/W]
WorkOrders.CustomerRefNo : String [R/W]
WorkOrders.ExpectedCompletionDate : Date [R/W]
WorkOrders.FinancialPeriod : Long [R]
WorkOrders.GenerationTime : Date [R/W]
WorkOrders.InstructionNumber : Long [R]
WorkOrders.JournalRemarks : String [R/W]
WorkOrders.Lines : WorkOrder_Lines [R]
WorkOrders.OrderDate : Date [R/W]
WorkOrders.OrdererCode : String [R/W]
WorkOrders.OrdererName : String [R/W]
WorkOrders.OrderNum : Long [R]
WorkOrders.OrderTotal : Double [R]
WorkOrders.PriceListNum : Long [R/W]
WorkOrders.ReceiverName : String [R/W]
WorkOrders.Series : Long [R/W]
WorkOrders.Status : BoWorkOrderStat [R/W]
WorkOrders.TotalCurrency : String [R]
WorkOrders.UserFields : UserFields [R]
WorkOrders.WorkFinishDate : Date [R/W]
WorkOrders.WorkStartDate : Date [R/W]
WorkOrders.WorkSum : Double [R/W]
WorkOrders.Add() -> Long
WorkOrders.Cancel() -> Long
WorkOrders.GetAsXML() -> String
WorkOrders.GetByKey(ByVal WkoKey As Long) -> Boolean
WorkOrders.SaveToFile(ByVal FileName As String)
WorkOrders.SaveXML(ByRef FileName As String)
WorkOrders.Update() -> Long
WTaxTypeCode.Code : Long [R/W]
WTaxTypeCode.Description : String [R/W]
WTaxTypeCode.FromXMLFile(ByVal bstrFileName As String)
WTaxTypeCode.FromXMLString(ByVal bstrXML As String)
WTaxTypeCode.GetXMLSchema() -> String
WTaxTypeCode.ToXMLFile(ByVal bstrFileName As String)
WTaxTypeCode.ToXMLString() -> String
WTaxTypeCodeParams.Code : Long [R/W]
WTaxTypeCodeParams.FromXMLFile(ByVal bstrFileName As String)
WTaxTypeCodeParams.FromXMLString(ByVal bstrXML As String)
WTaxTypeCodeParams.GetXMLSchema() -> String
WTaxTypeCodeParams.ToXMLFile(ByVal bstrFileName As String)
WTaxTypeCodeParams.ToXMLString() -> String
WTaxTypeCodeService.AddWTaxTypeCode(ByVal pIWTaxTypeCode As WTaxTypeCode) -> WTaxTypeCodeParams
WTaxTypeCodeService.DeleteWTaxTypeCode(ByVal pIWTaxTypeCodeParams As WTaxTypeCodeParams)
WTaxTypeCodeService.GetDataInterface(ByVal enumMSDI As WTaxTypeCodeServiceDataInterfaces) -> Object
WTaxTypeCodeService.GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) -> Object
WTaxTypeCodeService.GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) -> Object
WTaxTypeCodeService.GetWTaxTypeCode(ByVal pIWTaxTypeCodeParams As WTaxTypeCodeParams) -> WTaxTypeCode
WTaxTypeCodeService.GetWTaxTypeCodeList() -> WTaxTypeCodesParams
WTaxTypeCodeService.UpdateWTaxTypeCode(ByVal pIWTaxTypeCode As WTaxTypeCode)
WTaxTypeCodesParams.Count : Long [R]
WTaxTypeCodesParams.Add() -> WTaxTypeCodeParams
WTaxTypeCodesParams.GetXMLSchema() -> String
WTaxTypeCodesParams.Item(ByVal vtIndex As Variant) -> WTaxTypeCodeParams
WTaxTypeCodesParams.ToXMLFile(ByVal bstrFileName As String)
WTaxTypeCodesParams.ToXMLString() -> String
WTDBP.BPKeyPart1 : String [R/W]
WTDBP.BPKeyPart2 : String [R/W]
WTDBP.DetailType : WTDDetailType [R/W]
WTDBP.EffectiveDateFrom : Date [R/W]
WTDBP.EffectiveDateTo : Date [R/W]
WTDBP.Rate : Double [R/W]
WTDBP.UserFields : Fields [R]
WTDBP.WTaxCode : String [R/W]
WTDBP.FromXMLFile(ByVal bstrFileName As String)
WTDBP.FromXMLString(ByVal bstrXML As String)
WTDBP.GetXMLSchema() -> String
WTDBP.ToXMLFile(ByVal bstrFileName As String)
WTDBP.ToXMLString() -> String
WTDBPCollection.Count : Long [R]
WTDBPCollection.Add() -> WTDBP
WTDBPCollection.GetXMLSchema() -> String
WTDBPCollection.Item(ByVal vtIndex As Variant) -> WTDBP
WTDBPCollection.ToXMLFile(ByVal bstrFileName As String)
WTDBPCollection.ToXMLString() -> String
WTDCode.AbsEntry : Long [R]
WTDCode.BaseAmountPrct : Double [R/W]
WTDCode.BaseType : WithholdingTaxCodeBaseTypeEnum [R/W]
WTDCode.CalculateInAutomaticCM : BoYesNoEnum [R/W]
WTDCode.Category : WithholdingTaxCodeCategoryEnum [R/W]
WTDCode.FormulaId : Long [R/W]
WTDCode.Inactive : BoYesNoEnum [R/W]
WTDCode.MinAmount : Double [R/W]
WTDCode.OfficialCode : String [R/W]
WTDCode.SlidingScaleProgressiveTax : BoYesNoEnum [R/W]
WTDCode.Type : Long [R/W]
WTDCode.UserFields : Fields [R]
WTDCode.WTaxCode : String [R/W]
WTDCode.WTaxName : String [R/W]
WTDCode.WTDBPCollection : WTDBPCollection [R]
WTDCode.WTDEffectiveDateCollection : WTDEffectiveDateCollection [R]
WTDCode.WTDFreightCollection : WTDFreightCollection [R]
WTDCode.WTDItemCollection : WTDItemCollection [R]
WTDCode.FromXMLFile(ByVal bstrFileName As String)
WTDCode.FromXMLString(ByVal bstrXML As String)
WTDCode.GetXMLSchema() -> String
WTDCode.ToXMLFile(ByVal bstrFileName As String)
WTDCode.ToXMLString() -> String
WTDCodeParams.AbsEntry : Long [R/W]
WTDCodeParams.WTaxCode : String [R/W]
WTDCodeParams.WTaxName : String [R]
WTDCodeParams.FromXMLFile(ByVal bstrFileName As String)
WTDCodeParams.FromXMLString(ByVal bstrXML As String)
WTDCodeParams.GetXMLSchema() -> String
WTDCodeParams.ToXMLFile(ByVal bstrFileName As String)
WTDCodeParams.ToXMLString() -> String
WTDCodeParamsCollection.Count : Long [R]
WTDCodeParamsCollection.Add() -> WTDCodeParams
WTDCodeParamsCollection.GetXMLSchema() -> String
WTDCodeParamsCollection.Item(ByVal vtIndex As Variant) -> WTDCodeParams
WTDCodeParamsCollection.ToXMLFile(ByVal bstrFileName As String)
WTDCodeParamsCollection.ToXMLString() -> String
WTDEffectiveDate.Effectivefrom : Date [R/W]
WTDEffectiveDate.LineNumber : Long [R]
WTDEffectiveDate.Rate : Double [R/W]
WTDEffectiveDate.UserFields : Fields [R]
WTDEffectiveDate.WTDValueRangeCollection : WTDValueRangeCollection [R]
WTDEffectiveDate.FromXMLFile(ByVal bstrFileName As String)
WTDEffectiveDate.FromXMLString(ByVal bstrXML As String)
WTDEffectiveDate.GetXMLSchema() -> String
WTDEffectiveDate.ToXMLFile(ByVal bstrFileName As String)
WTDEffectiveDate.ToXMLString() -> String
WTDEffectiveDateCollection.Count : Long [R]
WTDEffectiveDateCollection.Add() -> WTDEffectiveDate
WTDEffectiveDateCollection.GetXMLSchema() -> String
WTDEffectiveDateCollection.Item(ByVal vtIndex As Variant) -> WTDEffectiveDate
WTDEffectiveDateCollection.ToXMLFile(ByVal bstrFileName As String)
WTDEffectiveDateCollection.ToXMLString() -> String
WTDFreight.EffectiveDateFrom : Date [R/W]
WTDFreight.EffectiveDateTo : Date [R/W]
WTDFreight.FreightCode : Long [R/W]
WTDFreight.UserFields : Fields [R]
WTDFreight.WTaxCode : String [R/W]
WTDFreight.FromXMLFile(ByVal bstrFileName As String)
WTDFreight.FromXMLString(ByVal bstrXML As String)
WTDFreight.GetXMLSchema() -> String
WTDFreight.ToXMLFile(ByVal bstrFileName As String)
WTDFreight.ToXMLString() -> String
WTDFreightCollection.Count : Long [R]
WTDFreightCollection.Add() -> WTDFreight
WTDFreightCollection.GetXMLSchema() -> String
WTDFreightCollection.Item(ByVal vtIndex As Variant) -> WTDFreight
WTDFreightCollection.ToXMLFile(ByVal bstrFileName As String)
WTDFreightCollection.ToXMLString() -> String
WTDItem.EffectiveDateFrom : Date [R/W]
WTDItem.EffectiveDateTo : Date [R/W]
WTDItem.ItemCode : String [R/W]
WTDItem.UserFields : Fields [R]
WTDItem.WTaxCode : String [R/W]
WTDItem.FromXMLFile(ByVal bstrFileName As String)
WTDItem.FromXMLString(ByVal bstrXML As String)
WTDItem.GetXMLSchema() -> String
WTDItem.ToXMLFile(ByVal bstrFileName As String)
WTDItem.ToXMLString() -> String
WTDItemCollection.Count : Long [R]
WTDItemCollection.Add() -> WTDItem
WTDItemCollection.GetXMLSchema() -> String
WTDItemCollection.Item(ByVal vtIndex As Variant) -> WTDItem
WTDItemCollection.ToXMLFile(ByVal bstrFileName As String)
WTDItemCollection.ToXMLString() -> String
WTDValueRange.Effectivefrom : Date [R/W]
WTDValueRange.LineNumber : Long [R]
WTDValueRange.Rate : Double [R/W]
WTDValueRange.SeqNum : Long [R]
WTDValueRange.ValueFrom : Double [R/W]
WTDValueRange.FromXMLFile(ByVal bstrFileName As String)
WTDValueRange.FromXMLString(ByVal bstrXML As String)
WTDValueRange.GetXMLSchema() -> String
WTDValueRange.ToXMLFile(ByVal bstrFileName As String)
WTDValueRange.ToXMLString() -> String
WTDValueRangeCollection.Count : Long [R]
WTDValueRangeCollection.Add() -> WTDValueRange
WTDValueRangeCollection.GetXMLSchema() -> String
WTDValueRangeCollection.Item(ByVal vtIndex As Variant) -> WTDValueRange
WTDValueRangeCollection.ToXMLFile(ByVal bstrFileName As String)
WTDValueRangeCollection.ToXMLString() -> String
WTGroups.Count : Long [R]
WTGroups.DocsInWTGroups : DocsInWTGroups [R]
WTGroups.Percent : Double [R]
WTGroups.SumAccumulatedAmount : Double [R]
WTGroups.SumBaseAmount : Double [R]
WTGroups.SumDocTotal : Double [R]
WTGroups.SumPerceptAmount : Double [R]
WTGroups.SumVATAmount : Double [R]
WTGroups.WhtAbsId : Long [R]
WTGroups.SetCurrentLine(ByVal LineNum As Long)
