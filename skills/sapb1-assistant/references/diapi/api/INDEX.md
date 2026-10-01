<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# DI API classes

1378 classes. Each is in `api/<File>` from line `Line` for `Lines` lines (read exactly that range, or grep `^# <Class> (`); enumerations are in `../enums/`. Kind is the CHM's own label (Object or Collection).

| Class | Kind | Props | Methods | Source table | File | Line | Lines | Description |
|---|---|---|---|---|---|---|---|---|
| AccountCategoriesParams | Collection | 1 | 5 |  | classes-01.md | 3 | 15 | A data collection of AccountCategoryParams. |
| AccountCategory | Object | 3 | 5 | OACG | classes-01.md | 19 | 18 | A data structure object related to the AccountCategoryService service. |
| AccountCategoryParams | Object | 2 | 5 |  | classes-01.md | 38 | 17 | Holds identification parameters for the AccountCategoryService (CategoryCode, CategoryName). |
| AccountCategoryService | Object | 0 | 8 | OACG | classes-01.md | 56 | 149 | This service allows you to manage account categories (add, delete, get by key, get list, and update) for use with the Copy Express add-on. |
| AccountSegmentationCategories | Object | 6 | 7 | OASC | classes-01.md | 206 | 67 | The AccountSegmentationCategories object represents the categories for each of the account segments in the Financials module. |
| AccountSegmentations | Object | 7 | 7 | OASG | classes-01.md | 274 | 67 | The AccountSegmentations object represents the account segments in the Financials module. |
| AccountsService | Object | 0 | 4 |  | classes-01.md | 342 | 166 | The AccountsService enables to transfer credit or debit amounts from a specified opening balance account to one or more G/L accounts. |
| AccrualType | Object | 6 | 5 | OACR | classes-01.md | 509 | 25 | Represents an accrual type. |
| AccrualTypeParams | Object | 1 | 5 | OACR | classes-01.md | 535 | 18 | Holds the key of an accrual type. |
| AccrualTypes | Collection | 1 | 5 |  | classes-01.md | 554 | 18 | A collection of AccrualType objects. |
| AccrualTypesParams | Collection | 1 | 5 |  | classes-01.md | 573 | 18 | A collection of AccrualTypeParams objects. |
| AccrualTypesService | Object | 0 | 8 | OACR | classes-01.md | 592 | 70 | An accrual type is a set of conditions used to represent the differences between cost accounting and financial accounting. |
| AcctSegmnt_Categories | Object | 4 | 2 | OASC | classes-01.md | 663 | 16 | The category of the account segmentation. |
| ActivitiesParams | Collection | 1 | 5 |  | classes-01.md | 680 | 18 | A collection of ActivityParams objects. |
| ActivitiesService | Object | 0 | 13 | OCLG | classes-01.md | 699 | 151 | The ActivitiesService service enables you to add, look up, remove, and update single activities and recurring activities. |
| Activity | Object | 74 | 5 | OCLG | classes-01.md | 851 | 103 | Activities refer to interactions you have with business partners, such as phone calls, meetings, tasks, and so on. |
| ActivityCheckIn | Object | 8 | 5 |  | classes-01.md | 955 | 23 | ActivityCheckIn Class |
| ActivityCheckInCollection | Collection | 1 | 5 |  | classes-01.md | 979 | 15 | ActivityCheckInCollection Class |
| ActivityInstanceParams | Object | 2 | 5 | OCLG | classes-01.md | 995 | 19 | Holds the key and date of an instance in a recurring activity. |
| ActivityInstancesListParams | Object | 2 | 5 |  | classes-01.md | 1015 | 21 | You can get the top N activity instances from certain date. |
| ActivityInstancesParams | Collection | 1 | 5 |  | classes-01.md | 1037 | 18 | A collection of ActivityInstanceParams objects. |
| ActivityLocations | Object | 4 | 6 | OCLO | classes-01.md | 1056 | 61 | ActivityLocations is a business object that represents activity locations in the Business Partners module. |
| ActivityMultipleRecipient | Object | 3 | 5 | CLG2 | classes-01.md | 1118 | 22 | List of the recipients when you select the Multiple Recipients option. |
| ActivityMultipleRecipientCollection | Collection | 1 | 6 | CLG2 | classes-01.md | 1141 | 22 | Properties of the recipients when you select the Multiple Recipients option. |
| ActivityParams | Object | 24 | 5 | OCLG | classes-01.md | 1164 | 41 | Holds the key of an activity. |
| ActivityRecipient | Object | 3 | 5 |  | classes-01.md | 1206 | 18 | ActivityRecipient Class |
| ActivityRecipientCollection | Collection | 1 | 6 |  | classes-01.md | 1225 | 17 | ActivityRecipientCollection Class |
| ActivityRecipientList | Object | 5 | 5 |  | classes-01.md | 1243 | 20 | ActivityRecipientList Class |
| ActivityRecipientListParams | Object | 4 | 5 |  | classes-01.md | 1264 | 19 | ActivityRecipientParams Class |
| ActivityRecipientListParamsCollection | Collection | 1 | 5 |  | classes-01.md | 1284 | 15 | ActivityRecipientParamsCollection Class |
| ActivityRecipientListsService | Object | 0 | 8 |  | classes-01.md | 1300 | 21 | ActivityRecipientListsService Class |
| ActivityStatus | Object | 5 | 6 | OCLA | classes-01.md | 1322 | 61 | ActivityStatus is a business object that enables to define statuses for Task type activities in the Business Partners module. |
| ActivitySubject | Object | 4 | 5 |  | classes-01.md | 1384 | 19 | ActivitySubject Class |
| ActivitySubjectParams | Object | 2 | 5 |  | classes-01.md | 1404 | 17 | ActivitySubjectParams Class |
| ActivitySubjectService | Object | 0 | 8 |  | classes-01.md | 1422 | 21 | ActivitySubjectService Class |
| ActivitySubjectsParams | Collection | 1 | 5 |  | classes-01.md | 1444 | 15 | ActivitySubjectsParams Class |
| ActivityTypes | Object | 5 | 6 | OCLT | classes-01.md | 1460 | 62 | ActivityTypes is a business object that represents activity types in the Business Partners module. |
| AdditionalExpenses | Object | 30 | 8 | OEXD | classes-01.md | 1523 | 90 | AdditionalExpenses is a business object that represents the additional expenses defined in the Administration module. |
| AddressExtension | Object | 60 | 0 | INV12 | classes-01.md | 1614 | 104 | The Bill To and Ship To address for a marketing document. |
| AddressFormat | Object | 3 | 5 | OADF | classes-01.md | 1719 | 20 | The address formats for business partners. |
| AddressFormatParams | Object | 2 | 5 |  | classes-01.md | 1740 | 19 | Holds the key of an address format. |
| AddressFormatParamsCollection | Collection | 1 | 5 |  | classes-01.md | 1760 | 18 | A collection of AddressFormatParams objects. |
| AddressParams | Object | 14 | 5 | SCL7 | classes-01.md | 1779 | 31 | Holds the key of an address. |
| AddressReturnParams | Object | 1 | 5 |  | classes-01.md | 1811 | 18 | Holds the key of a full address. |
| AddressService | Object | 0 | 5 | OADF | classes-01.md | 1830 | 102 | The AddressService service enables you to retrieve Address Format and full address. |
| AdminInfo | Object | 274 | 5 | OADM | classes-02.md | 3 | 478 | The AdminInfo is a data structure related to the CompanyService. |
| AdvancedGLAccountParams | Object | 15 | 5 |  | classes-02.md | 482 | 30 | AdvancedGLAccountParams Class |
| AdvancedGLAccountReturnParams | Object | 1 | 5 |  | classes-02.md | 513 | 16 | AdvancedGLAccountReturnParams Class |
| AlertManagement | Object | 19 | 5 | OALT | classes-02.md | 530 | 34 | AlertManagement is Data structure related to the AlertManagementService. |
| AlertManagementDocument | Object | 2 | 5 | OALT | classes-02.md | 565 | 17 | AlertManagementDocument is a data structure related to the AlertManagementService. |
| AlertManagementDocuments | Collection | 1 | 5 | OALT | classes-02.md | 583 | 15 | AlertManagementDocuments is a Data Collection of AlertManagementDocument data structures. |
| AlertManagementParams | Object | 3 | 5 | OALT | classes-02.md | 599 | 18 | This object specifies the identification key combination (Code, Name and Type) for which the AlertManagementService is related. |
| AlertManagementParamsCollection | Collection | 1 | 5 | ALT1 | classes-02.md | 618 | 15 | AlertManagementParamsCollection is a Data Collection of AlertManagementParams Identification Keys. |
| AlertManagementRecipient | Object | 6 | 5 | ALT1 | classes-02.md | 634 | 21 | AlertManagementRecipient is a data structure related to the AlertManagementService and defines the properties of the AlertManagementService's recipient. |
| AlertManagementRecipients | Collection | 1 | 5 | ALT1 | classes-02.md | 656 | 15 | AlertManagementRecipients is a Data Collection of AlertManagementRecipient data structures. |
| AlertManagementService | Object | 0 | 7 | OALT | classes-02.md | 672 | 179 | AlertManagementService is a business object that manages alert system for SAP Business One application. |
| AlternateCatNum | Object | 8 | 7 | OSCN | classes-02.md | 852 | 78 | AlternateCatNum is a business object that represents the alternative catalog numbers in the Business Partners module. |
| AlternativeItem | Object | 3 | 5 | OALI | classes-02.md | 931 | 18 | A data structure object related to the AlternativeItemsService service. |
| AlternativeItems | Collection | 1 | 6 |  | classes-02.md | 950 | 17 | A data collection of AlternativeItem object. |
| AlternativeItemsService | Object | 0 | 7 | OALI | classes-02.md | 968 | 146 | This service manages alternative items in SAP Business One (add, delete, get by key, and update). |
| ApprovalRequest | Object | 15 | 5 | OWDD | classes-02.md | 1115 | 32 | Represents an approval request. |
| ApprovalRequestDecision | Object | 4 | 5 |  | classes-02.md | 1148 | 21 | ApprovalRequestDecision is a child object of the ApprovalRequest object that represents the approval decision of an approval request. |
| ApprovalRequestDecisions | Collection | 1 | 5 |  | classes-02.md | 1170 | 18 | A collection of ApprovalRequestDecision objects. |
| ApprovalRequestLine | Object | 8 | 5 | WDD1 | classes-02.md | 1189 | 25 | ApprovalRequestLine is a child object of the ApprovalRequest object. |
| ApprovalRequestLines | Collection | 1 | 5 |  | classes-02.md | 1215 | 18 | A collection of ApprovalRequestLine objects. |
| ApprovalRequestParams | Object | 3 | 5 | OWDD | classes-02.md | 1234 | 20 | Holds the key, remarks, and status of an approval request. |
| ApprovalRequestsParams | Collection | 1 | 5 |  | classes-02.md | 1255 | 18 | A collection of ApprovalRequestParams objects. |
| ApprovalRequestsService | Object | 0 | 10 | OWDD | classes-02.md | 1274 | 164 | ApprovalRequestsService is a business object that manages the approval requests process in the SAP Business One environment. |
| ApprovalStage | Object | 5 | 5 | OWST | classes-02.md | 1439 | 20 | ApprovalStage is a Data structure related to the ApprovalStagesService. |
| ApprovalStageApprover | Object | 1 | 5 | WST1 | classes-02.md | 1460 | 16 | ApprovalStageApprover is a Data structure that define the user Id of the ApprovalStage approver. |
| ApprovalStageApprovers | Collection | 1 | 5 |  | classes-02.md | 1477 | 15 | ApprovalStageApprovers is a Data Collection of ApprovalStageApprover data structures. |
| ApprovalStageParams | Object | 2 | 5 | OWST | classes-03.md | 3 | 17 | The ApprovalStageParams specifies the identification key combination (Code and Name) for which the ApprovalStagesService is related. |
| ApprovalStages | Collection | 1 | 5 | OWST | classes-03.md | 21 | 15 | The ApprovalStages is a Data Collection of ApprovalStage data structure. |
| ApprovalStagesParams | Collection | 1 | 5 | OWST | classes-03.md | 37 | 15 | ApprovalStagesParams is a Data Collection of ApprovalStageParams identification keys. |
| ApprovalStagesService | Object | 0 | 8 | OWST | classes-03.md | 53 | 156 | ApprovalStagesService is a business object that manages the Approval stages Process in SAP Business One environment. |
| ApprovalTemplate | Object | 11 | 5 | OWTM | classes-03.md | 210 | 82 | ApprovalTemplate is a data structure related to the ApprovalTemplatesService. |
| ApprovalTemplateDocument | Object | 1 | 5 | WTM3 | classes-03.md | 293 | 16 | ApprovalTemplateDocument is a data structure related to the ApprovalTemplatesService. |
| ApprovalTemplateDocuments | Collection | 1 | 5 | WTM3 | classes-03.md | 310 | 15 | ApprovalTemplateDocuments is a Data Collection of ApprovalTemplateDocument data structures. |
| ApprovalTemplateParams | Object | 2 | 5 | OWTM | classes-03.md | 326 | 17 | The ApprovalTemplateParams specifies the identification key combination (Code and Name) for which the ApprovalTemplatesService is related. |
| ApprovalTemplateQueries | Collection | 1 | 5 | WTM5 | classes-03.md | 344 | 15 | ApprovalTemplateQueries is a Data Collection of ApprovalTemplateQuery data structures. |
| ApprovalTemplateQuery | Object | 1 | 5 |  | classes-03.md | 360 | 16 | ApprovalTemplateQuery is a data structure related to the ApprovalTemplatesService. |
| ApprovalTemplates | Collection | 1 | 5 | OWTM | classes-03.md | 377 | 15 | ApprovalTemplates is a Data Collection of ApprovalTemplate data structures. |
| ApprovalTemplatesParams | Collection | 1 | 5 | OWTM | classes-03.md | 393 | 15 | ApprovalTemplatesParams is a Data Collection of ApprovalTemplateParams identification keys. |
| ApprovalTemplatesService | Object | 0 | 8 | OWTM | classes-03.md | 409 | 153 | ApprovalTemplatesService is a business object that manages the Approval of deviations from organization limitations. |
| ApprovalTemplateStage | Object | 3 | 5 | WTM2 | classes-03.md | 563 | 18 | ApprovalTemplateStage is a data structure related to the ApprovalTemplatesService. |
| ApprovalTemplateStages | Collection | 1 | 5 | WTM2 | classes-03.md | 582 | 15 | ApprovalTemplateStages is a Data Collection of ApprovalTemplateStage data structures. |
| ApprovalTemplateTerm | Object | 3 | 5 | WTM4 | classes-03.md | 598 | 18 | ApprovalTemplateTerm is a data structure related to the ApprovalTemplatesService. |
| ApprovalTemplateTerms | Collection | 1 | 5 | WTM4 | classes-03.md | 617 | 15 | ApprovalTemplateTerms is a Data Collection of ApprovalTemplateTerm data structures. |
| ApprovalTemplateUser | Object | 1 | 5 | WTM1 | classes-03.md | 633 | 16 | ApprovalTemplateUser is a Data structure related to the ApprovalTemplatesService. |
| ApprovalTemplateUsers | Collection | 1 | 5 | WTM1 | classes-03.md | 650 | 15 | ApprovalTemplateUsers is a Data Collection of ApprovalTemplateUser data structures. |
| AssetClass | Object | 8 | 5 | OACS | classes-03.md | 666 | 25 | With SAP Business One, you can use asset classes to classify fixed assets according to business and legal requirements. |
| AssetClassCollection | Collection | 1 | 5 |  | classes-03.md | 692 | 18 | A collection of AssetClassLine objects. |
| AssetClassesService | Object | 0 | 8 | OACS | classes-03.md | 711 | 70 | The AssetClassesService service enables you to create, update and view asset classes. |
| AssetClassLine | Object | 7 | 5 | ACS1 | classes-03.md | 782 | 24 | AssetClassLine is a child object of AssetClass object and represents the depreciation area fields of an asset class. |
| AssetClassParams | Object | 2 | 5 |  | classes-03.md | 807 | 19 | Holds the key to an existing asset class. |
| AssetClassParamsCollection | Collection | 1 | 5 |  | classes-03.md | 827 | 18 | A collection of AssetClassParams objects. |
| AssetDepreciationGroup | Object | 3 | 5 |  | classes-03.md | 846 | 20 | AssetDepreciationGroup Class |
| AssetDepreciationGroupParams | Object | 2 | 5 |  | classes-03.md | 867 | 19 | AssetDepreciationGroupParams Class |
| AssetDepreciationGroupParamsCollection | Collection | 1 | 5 |  | classes-03.md | 887 | 18 | AssetDepreciationGroupParamsCollection Class |
| AssetDepreciationGroupsService | Object | 0 | 8 |  | classes-03.md | 906 | 21 | AssetDepreciationGroupsService Class |
| AssetDocument | Object | 31 | 5 | OACQ | classes-03.md | 928 | 48 | AssetDocument is a business object that represents the header data of asset documents in the Fixed Asset function of SAP Business One application. |
| AssetDocumentAreaJournal | Object | 7 | 5 | ACQ2 | classes-03.md | 977 | 24 | AssetDocumentAreaJournal is a child object of AssetDocument object and represents the Accounting tab fields of an asset document. |
| AssetDocumentAreaJournalCollection | Collection | 1 | 5 |  | classes-03.md | 1002 | 18 | A collection of AssetDocumentAreaJournal objects. |
| AssetDocumentLine | Object | 20 | 5 | ACQ1 | classes-03.md | 1021 | 37 | AssetDocumentLine is a child object of AssetDocument object and represents the line entries of an asset document. |
| AssetDocumentLineCollection | Collection | 1 | 5 |  | classes-03.md | 1059 | 18 | A collection of AssetDocumentLine objects. |
| AssetDocumentParams | Object | 3 | 5 |  | classes-03.md | 1078 | 20 | Holds the key and cancellation information to an existing asset document. |
| AssetDocumentParamsCollection | Collection | 1 | 5 |  | classes-03.md | 1099 | 18 | A collection of AssetDocumentParams objects. |
| AssetDocumentService | Object | 0 | 9 | OACQ | classes-03.md | 1118 | 111 | The AssetDocumentService service enables you to add, look up, update, cancel, and remove asset documents. |
| AssetGroup | Object | 2 | 5 | OAGS | classes-03.md | 1230 | 19 | The asset group to which the asset belongs. |
| AssetGroupParams | Object | 2 | 5 |  | classes-03.md | 1250 | 19 | Holds the key to an existing asset group. |
| AssetGroupParamsCollection | Collection | 1 | 5 |  | classes-03.md | 1270 | 18 | A collection of AssetGroupParams objects. |
| AssetGroupsService | Object | 0 | 8 | OAGS | classes-03.md | 1289 | 70 | The AssetGroupsService service enables you to add, look up, update, and remove asset groups. |
| AssetRevaluation | Object | 19 | 5 | OFAR | classes-03.md | 1360 | 38 | Use the object to revaluate assets. |
| AssetRevaluationLine | Object | 7 | 5 | FAR1 | classes-03.md | 1399 | 24 | Source table: FAR1. |
| AssetRevaluationLineCollection | Collection | 1 | 5 |  | classes-03.md | 1424 | 18 | AssetRevaluationLineCollection Class |
| AssetRevaluationParams | Object | 1 | 5 |  | classes-03.md | 1443 | 18 | AssetRevaluationParams Class |
| AssetRevaluationParamsCollection | Collection | 1 | 5 |  | classes-03.md | 1462 | 18 | AssetRevaluationParamsCollection Class |
| AssetRevaluationService | Object | 0 | 8 | OFAR | classes-03.md | 1481 | 91 | Use the AssetRevaluationService service to revaluate assets. |
| Attachment | Object | 1 | 0 |  | classes-03.md | 1573 | 7 | The Attachment object represents an external file that is attached to business objects, such as, Contacts, Messages, and ServiceContracts. |
| Attachments | Collection | 1 | 3 |  | classes-03.md | 1581 | 17 | Attachments is a collection of one or more Attachment objects. |
| Attachments2 | Object | 4 | 6 | OATC | classes-03.md | 1599 | 58 | The Attachments2 object enables to copy files from a source folder to the Attachments folder that is defined through the application. |
| Attachments2_Lines | Object | 13 | 2 | ATC1 | classes-03.md | 1658 | 35 | The Attachments2_Lines is a child object of the Attachments2 object. |
| AttributeGroup | Object | 4 | 5 | OFAA | classes-03.md | 1694 | 21 | Source table: OFAA. |
| AttributeGroupCollection | Collection | 1 | 5 |  | classes-03.md | 1716 | 18 | AttributeGroupCollection Class |
| AttributeGroupLine | Object | 6 | 5 | FAA1 | classes-03.md | 1735 | 23 | Source table: FAA1. |
| AttributeGroupParams | Object | 2 | 5 |  | classes-03.md | 1759 | 19 | AttributeGroupParams Class |
| AttributeGroupParamsCollection | Collection | 1 | 5 |  | classes-03.md | 1779 | 18 | AttributeGroupParamsCollection Class |
| AttributeGroupsService | Object | 0 | 8 |  | classes-03.md | 1798 | 21 | AttributeGroupsService Class |
| BankChargesAllocationCode | Object | 2 | 5 | OBCA | classes-03.md | 1820 | 19 | Represents codes for the allocation of bank charges. |
| BankChargesAllocationCodeParams | Object | 2 | 5 |  | classes-03.md | 1840 | 19 | Holds the key and name to a bank charges allocation code. |
| BankChargesAllocationCodesParams | Collection | 1 | 5 |  | classes-03.md | 1860 | 18 | A collection of BankChargesAllocationCodeParams objects. |
| BankChargesAllocationCodesService | Object | 0 | 9 | OBCA | classes-03.md | 1879 | 91 | The BankChargesAllocationCodesService service enables you to add, look up, update, and remove allocation codes for bank charges. |
| BankPages | Object | 24 | 7 | OBNK | classes-03.md | 1971 | 124 | BankPages is a business object that represents external bank statements in the Banking module. |
| Banks | Object | 13 | 7 | ODSC | classes-04.md | 3 | 73 | The Banks object enables to define banks, which can be used by the HouseBankAccounts and BPBankAccounts objects. |
| BankStatement | Object | 14 | 5 | OBNH | classes-04.md | 77 | 29 | A data structure related with the BankStatementService holding the bank statement header properties. |
| BankStatementParams | Object | 11 | 5 |  | classes-04.md | 107 | 26 | A data structure holding idnetification properties for the BankStatementService. |
| BankStatementRow | Object | 52 | 5 | OBNK | classes-04.md | 134 | 105 | A data structure related to the BankStatementService holding the properties of a bank statement line. |
| BankStatementRows | Collection | 1 | 6 |  | classes-04.md | 240 | 17 | A data collection of BankStatementRow objects. |
| BankStatements | Collection | 1 | 5 |  | classes-04.md | 258 | 15 | A data collection of BankStatement objects. |
| BankStatementsFilter | Object | 3 | 5 |  | classes-04.md | 274 | 18 | This object fefines filtering properties for GetBankStatementList |
| BankStatementsImportFile | Object | 4 | 5 |  | classes-04.md | 293 | 19 | This object defines the properties of the external file you want to import in BankStatementFromFile. |
| BankStatementsParams | Collection | 1 | 5 |  | classes-04.md | 313 | 15 | A data collection of BankStatementParams. |
| BankStatementsService | Object | 0 | 8 | OBNH, OBNK, BNK1 | classes-04.md | 329 | 239 | This service manages bank statements drafts that can be posted in SAP Business One. |
| BarCode | Object | 5 | 5 | OBCD | classes-04.md | 569 | 24 | The bar codes for your items. |
| BarCodeParams | Object | 4 | 5 |  | classes-04.md | 594 | 21 | Holds the key to an existing bar code. |
| BarCodeParamsCollection | Collection | 1 | 5 |  | classes-04.md | 616 | 18 | A collection of BarCodeParams objects. |
| BarCodesService | Object | 0 | 8 | OBCD | classes-04.md | 635 | 70 | The BarCodesService service enables you to add, look up, update, and remove bar codes. |
| BatchNumberDetail | Object | 13 | 5 | OBTN, OITL, ITL1 | classes-04.md | 706 | 30 | The batch details for the item. |
| BatchNumberDetailParams | Object | 1 | 5 |  | classes-04.md | 737 | 18 | Holds the key to the batch number details for the item. |
| BatchNumberDetailsService | Object | 0 | 5 | OBTN, OITL, ITL1 | classes-04.md | 756 | 65 | The BatchNumberDetailsService service enables you to look up and update batch details for the item. |
| BatchNumbers | Object | 16 | 2 | OBTN, OBTW, OBTQ, OITL, ITL1 | classes-04.md | 822 | 29 | BatchNumbers is a business object that represents the batch numbers of an item in the Inventory and Production module. |
| BillOfExchange | Object | 29 | 0 | OBOE | classes-04.md | 852 | 44 | BillOfExchange is a business object that represents the Bill Of Exchange table in the Banking module. |
| BillOfExchangeTrans_BankPages | Object | 3 | 0 |  | classes-04.md | 897 | 8 | For internal use. |
| BillOfExchangeTrans_Deposits | Object | 7 | 0 | ODPS | classes-04.md | 906 | 15 | BillOfExchangeTrans_Deposits is a child object of the BillOfExchangeTransaction object and represents the deposits information for incoming payments. |
| BillOfExchangeTransaction | Object | 14 | 5 | OBOT | classes-04.md | 922 | 68 | BillOfExchangeTransaction is a business object that represents the Bill Of Exchange Transaction table in the Banking module. |
| BillOfExchangeTransaction_Lines | Object | 5 | 2 | BOT1 | classes-04.md | 991 | 18 | BillOfExchangeTransaction_Lines is a child object of the BillOfExchangeTransaction object, and represents the line entries of the Bill Of Exchange Transaction. |
| BinLocation | Object | 41 | 5 | OBIN | classes-04.md | 1010 | 58 | A bin location is the smallest addressable unit of space in a warehouse where your goods are stored. |
| BinLocationAttribute | Object | 3 | 5 | OBAT | classes-04.md | 1069 | 20 | You can set up different codes for each bin location attribute. |
| BinLocationAttributeCollectionParams | Collection | 1 | 5 |  | classes-04.md | 1090 | 18 | A collection of BinLocationAttributeParams objects. |
| BinLocationAttributeParams | Object | 3 | 5 |  | classes-04.md | 1109 | 20 | Holds the key to an existing bin location attribute code. |
| BinLocationAttributesService | Object | 0 | 8 | OBAT | classes-04.md | 1130 | 70 | The BinLocationAttributesService service enables you to add, look up, update, and remove bin location attributes codes. |
| BinLocationCollectionParams | Collection | 1 | 5 |  | classes-04.md | 1201 | 18 | A collection of BinLocationParams objects. |
| BinLocationField | Object | 6 | 5 | OBFC | classes-04.md | 1220 | 25 | The bin location field you can specify and activate. |
| BinLocationFieldCollectionParams | Collection | 1 | 5 |  | classes-04.md | 1246 | 18 | A collection of BinLocationFieldParams objects. |
| BinLocationFieldParams | Object | 1 | 5 |  | classes-04.md | 1265 | 18 | Holds the key to an existing bin location field. |
| BinLocationFieldsService | Object | 0 | 6 | OBFC | classes-04.md | 1284 | 66 | The BinLocationFieldsService service enables you to look up and update bin location fields. |
| BinLocationParams | Object | 2 | 5 |  | classes-04.md | 1351 | 19 | Holds the key to an existing bin location. |
| BinLocationsService | Object | 0 | 8 | OBIN | classes-04.md | 1371 | 70 | The BinLocationsService service enables you to add, look up, update, and remove bin locations. |
| BlanketAgreement | Object | 37 | 5 | OOAT | classes-04.md | 1442 | 54 | A blanket agreement is a longer-term arrangement between a purchasing organization and a vendor, or a sales organization and a customer, for the supply of items or provision of services over a period of time based on pre |
| BlanketAgreementParams | Object | 1 | 5 |  | classes-04.md | 1497 | 18 | Holds the key to an existing blanket agreement. |
| BlanketAgreements_DetailsLine | Object | 14 | 5 | OAT2 | classes-04.md | 1516 | 31 | BlanketAgreements_DetailsLine is a child object of the BlanketAgreements_ItemsLine object and represents the details of a delivery plan for an item. |
| BlanketAgreements_DetailsLines | Collection | 1 | 6 |  | classes-04.md | 1548 | 20 | A collection of BlanketAgreements_DetailsLine objects. |
| BlanketAgreements_ItemsLine | Object | 34 | 5 | OAT1 | classes-04.md | 1569 | 51 | BlanketAgreements_ItemsLine is a child object of the BlanketAgreement object and represents the items that can be purchased or sold within the scope of the blanket agreement. |
| BlanketAgreements_ItemsLines | Collection | 1 | 6 |  | classes-04.md | 1621 | 20 | A collection of BlanketAgreements_ItemsLine objects. |
| BlanketAgreementsDocument | Object | 15 | 5 | OAT4V | classes-04.md | 1642 | 32 | BlanketAgreementsDocument is a child object of the BlanketAgreement object and you can view the documents associated with the blanket agreement. |
| BlanketAgreementsDocuments | Collection | 1 | 5 |  | classes-04.md | 1675 | 18 | A collection of BlanketAgreementsDocument objects. |
| BlanketAgreementsParams | Collection | 1 | 5 |  | classes-04.md | 1694 | 18 | A collection of BlanketAgreementParams objects. |
| BlanketAgreementsService | Object | 0 | 9 | OOAT | classes-04.md | 1713 | 72 | The BlanketAgreementsService service enables you to add, look up, cancel, and update blanket agreements. |
| Blob | Object | 1 | 5 |  | classes-04.md | 1786 | 18 | Holds blob content to be added to or retrieved from a blob field in the SAP Business One database. |
| BlobParams | Object | 4 | 5 |  | classes-04.md | 1805 | 21 | Specifies a set of blob fields, as follows: - The Table property specifies the database table. |
| BlobTableKeySegment | Object | 2 | 5 |  | classes-04.md | 1827 | 19 | Specifies the record whose blob field is to be set. |
| BlobTableKeySegments | Collection | 1 | 5 |  | classes-04.md | 1847 | 18 | A collection of BlobTableKeySegment objects. |
| BOEDocumentType | Object | 3 | 5 | ODTY | classes-04.md | 1866 | 18 | A data structure object holding properties for the BOEDocumentTypesService. |
| BOEDocumentTypeParams | Object | 2 | 5 | ODTY | classes-04.md | 1885 | 17 | This object holds identification properties for the BOEDocumentTypesService object. |
| BOEDocumentTypes | Collection | 1 | 5 |  | classes-04.md | 1903 | 15 | This is a data collection of BOEDocumentType data structures. |
| BOEDocumentTypesParams | Collection | 1 | 5 |  | classes-04.md | 1919 | 15 | This is a data collection of BOEDocumentTypeParams data structure. |
| BOEDocumentTypesService | Object | 0 | 8 | ODTY | classes-05.md | 3 | 21 | This service manages document types in SAP Business One. |
| BOEInstruction | Object | 4 | 5 |  | classes-05.md | 25 | 19 | A data structure object holding properties for the BOEInstructionsService. |
| BOEInstructionParams | Object | 2 | 5 |  | classes-05.md | 45 | 17 | This object holds identification properties for the BOEInstructionsService object. |
| BOEInstructions | Collection | 1 | 5 |  | classes-05.md | 63 | 15 | This is a data collection of BOEInstruction data structure. |
| BOEInstructionsParams | Collection | 1 | 5 |  | classes-05.md | 79 | 15 | This is a data collection of BOEInstructionParams data structure. |
| BOEInstructionsService | Object | 0 | 8 | OIST | classes-05.md | 95 | 21 | This service manages instructions in SAP Business One. |
| BOELine | Object | 9 | 5 | OBOE | classes-05.md | 117 | 28 | Represents the deposits for bills of exchange. |
| BOELineParams | Object | 1 | 5 |  | classes-05.md | 146 | 18 | Holds the key of a bill of exchange. |
| BOELines | Collection | 1 | 5 |  | classes-05.md | 165 | 18 | A data collection of BOELine objects. |
| BOELinesParams | Collection | 1 | 5 |  | classes-05.md | 184 | 18 | A data collection of BOELineParams objects. |
| BOELinesService | Object | 0 | 4 | OBOE | classes-05.md | 203 | 63 | The BOELinesService service enables you to get a deposit for bill of exchange. |
| BOEPortfolio | Object | 5 | 5 | OPTF | classes-05.md | 267 | 20 | A data structure object holding properties for the BOEPortfoliosService. |
| BOEPortfolioParams | Object | 3 | 5 |  | classes-05.md | 288 | 18 | This object holds identification properties for the BOEPortfoliosService object. |
| BOEPortfolios | Collection | 1 | 5 |  | classes-05.md | 307 | 15 | This is a data collection of BOEPortfolio data structures. |
| BOEPortfoliosParams | Collection | 1 | 5 |  | classes-05.md | 323 | 15 | This object is a collection of BOEPortfolioParams. |
| BOEPortfoliosService | Object | 0 | 8 | OPTF | classes-05.md | 339 | 21 | This service manages Portfolios in SAP Business One. |
| Boxes1099 | Object | 6 | 2 | TNN1 | classes-05.md | 361 | 19 | Boxes1099 is a child object of the Forms1099 object. |
| BPAccountReceivablePayble | Object | 4 | 2 | CRD3 | classes-05.md | 381 | 17 | BPAccountReceivablePayble is a child object of the BusinessPartners object and represents the Business Partner Account Receivable Payable table in the Business Partner module. |
| BPAddresses | Object | 29 | 3 | CRD1 | classes-05.md | 399 | 130 | BPAddresses is a child object of the BusinessPartners and represents the Ship To and Bill To addresses list of the business partner. |
| BPBankAccounts | Object | 36 | 3 | OCRB | classes-05.md | 530 | 66 | BPBankAccounts is a business object that represents the bank accounts of the business partner. |
| BPBlockSendingMarketingContents | Object | 3 | 3 |  | classes-05.md | 597 | 75 | Block sending marketing contnet to the business partner. |
| BPBranchAssignment | Object | 4 | 3 |  | classes-05.md | 673 | 15 | BPBranchAssignment Class |
| BPCode | Object | 10 | 5 | OPB1 | classes-05.md | 689 | 27 | BPCode is a data structure related to the BusinessPartnersService. |
| BPCodes | Collection | 1 | 5 |  | classes-05.md | 717 | 15 | BPCodes is a collection of BPCode data structures. |
| BPCurrencies | Object | 3 | 1 | CRD13 | classes-05.md | 733 | 23 | Business Partners currency. |
| BPFiscalRegistryID | Object | 5 | 7 | OCNA | classes-05.md | 757 | 24 | BPFiscalRegistryID is a data structure related to the BusinessPartnersService. |
| BPFiscalTaxID | Object | 22 | 2 | CRD7 | classes-05.md | 782 | 35 | BPFiscalTaxID is a child object of the BusinessPartners and indicates the Brazilian Fiscal IDs info for each business partner. |
| BPIntrastatExtension | Object | 9 | 0 |  | classes-05.md | 818 | 14 | BPIntrastatExtension Class |
| BPPaymentDates | Object | 4 | 3 | CRD5 | classes-05.md | 833 | 29 | BPPaymentDates is a child object of BusinessPartners object that represents the payment days in the month for the business partner. |
| BPPaymentMethods | Object | 5 | 3 | CRD2 | classes-05.md | 863 | 17 | BPPaymentMethods is a child object of the BusinessPartners object that represents the payment methods related to the business partner. |
| BPPriorities | Object | 4 | 7 | OBPP | classes-05.md | 881 | 62 | The BPPriorities object enables to define business partner priorities for payment terms. |
| BPVatExemptions | Object | 4 | 5 |  | classes-05.md | 944 | 19 | BPVatExemptions Class |
| BPVatExemptionsLine | Object | 15 | 5 |  | classes-05.md | 964 | 30 | BPVatExemptionsLine Class |
| BPVatExemptionsLines | Collection | 1 | 6 |  | classes-05.md | 995 | 17 | BPVatExemptionsLines Class |
| BPVatExemptionsParams | Object | 2 | 5 |  | classes-05.md | 1013 | 17 | BPVatExemptionsParams Class |
| BPVatExemptionsParamsCollection | Collection | 1 | 5 |  | classes-05.md | 1031 | 15 | BPVatExemptionsParamsCollection Class |
| BPVatExemptionsService | Object | 0 | 8 |  | classes-05.md | 1047 | 21 | BPVatExemptionsService Class |
| BPWithholdingTax | Object | 4 | 2 | CRD4 | classes-05.md | 1069 | 15 | BPWithholdingTax is a child object of the BusinessPartners object that represents the withholding tax data related to the business partner. |
| Branch | Object | 3 | 5 | OUBR | classes-05.md | 1085 | 20 | Represents a branch. |
| BranchesParams | Collection | 1 | 5 |  | classes-05.md | 1106 | 17 | A collection of BranchParams objects. |
| BranchesService | Object | 0 | 8 | OUBR | classes-05.md | 1124 | 164 | The BranchesService service enables you to add, look up and remove branches in the branches master data table. |
| BranchParams | Object | 2 | 5 |  | classes-05.md | 1289 | 19 | Holds the key and name to an existing branch. |
| BrazilBeverageIndexer | Object | 4 | 5 |  | classes-05.md | 1309 | 19 | BrazilBeverageIndexer Class |
| BrazilBeverageIndexerParams | Object | 3 | 5 |  | classes-05.md | 1329 | 18 | BrazilBeverageIndexerParams Class |
| BrazilBeverageIndexersParams | Collection | 1 | 5 |  | classes-05.md | 1348 | 15 | BrazilBeverageIndexersParams Class |
| BrazilBeverageIndexersService | Object | 0 | 7 |  | classes-05.md | 1364 | 19 | BrazilBeverageIndexersService Class |
| BrazilFuelIndexer | Object | 4 | 5 |  | classes-05.md | 1384 | 19 | BrazilFuelIndexer Class |
| BrazilFuelIndexerParams | Object | 4 | 5 |  | classes-05.md | 1404 | 19 | BrazilFuelIndexerParams Class |
| BrazilFuelIndexersParams | Collection | 1 | 5 |  | classes-05.md | 1424 | 15 | BrazilFuelIndexersParams Class |
| BrazilFuelIndexersService | Object | 0 | 7 |  | classes-05.md | 1440 | 19 | BrazilFuelIndexersService Class |
| BrazilMultiIndexer | Object | 7 | 6 |  | classes-05.md | 1460 | 26 | BrazilMultiIndexer Class |
| BrazilMultiIndexerParams | Object | 6 | 5 |  | classes-05.md | 1487 | 21 | BrazilMultiIndexerParams Class |
| BrazilMultiIndexersParams | Collection | 1 | 5 |  | classes-05.md | 1509 | 15 | BrazilMultiIndexersParams Class |
| BrazilMultiIndexersService | Object | 0 | 7 |  | classes-05.md | 1525 | 20 | BrazilMultiIndexersService Class |
| BrazilNumericIndexer | Object | 4 | 5 |  | classes-05.md | 1546 | 19 | BrazilNumericIndexer Class |
| BrazilNumericIndexerParams | Object | 3 | 5 |  | classes-05.md | 1566 | 18 | BrazilNumericIndexerParams Class |
| BrazilNumericIndexersParams | Collection | 1 | 5 |  | classes-05.md | 1585 | 15 | BrazilNumericIndexersParams Class |
| BrazilNumericIndexersService | Object | 0 | 7 |  | classes-05.md | 1601 | 20 | BrazilNumericIndexersService Class |
| BrazilStringIndexer | Object | 4 | 5 |  | classes-05.md | 1622 | 19 | BrazilStringIndexer Class |
| BrazilStringIndexerParams | Object | 3 | 5 |  | classes-05.md | 1642 | 18 | BrazilStringIndexerParams Class |
| BrazilStringIndexersParams | Collection | 1 | 5 |  | classes-05.md | 1661 | 15 | BrazilStringIndexersParams Class |
| BrazilStringIndexersService | Object | 0 | 7 |  | classes-05.md | 1677 | 20 | BrazilStringIndexersService Class |
| Budget | Object | 27 | 7 | OBGT | classes-05.md | 1698 | 90 | Budget is a business object that represents the budget management in the Finance module. |
| Budget_Lines | Object | 23 | 2 | BGT1 | classes-05.md | 1789 | 35 | Budget_Lines is a child object of Budget object and represents the budget item details of an account. |
| BudgetCostAccounting_Lines | Object | 8 | 3 |  | classes-05.md | 1825 | 19 | BudgetCostAccounting_Lines Class |
| BudgetDistribution | Object | 17 | 8 | OBGD | classes-05.md | 1845 | 77 | BudgetDistribution is a business object that represents the budget distribution methods used by the budget management in the Finance module. |
| BudgetScenarios | Object | 14 | 8 | OBGS | classes-05.md | 1923 | 75 | BudgetScenarios is a business object that represents the budget scenarios used by the budget management in the Finance module. |
| BusinessPartnerGroups | Object | 5 | 7 | OCRG | classes-05.md | 1999 | 26 | BusinessPartnerGroups represents the setup of customer and vendor Groups. |
| BusinessPartnerPropertiesParams | Collection | 1 | 5 |  | classes-05.md | 2026 | 17 | A collection of BusinessPartnerPropertyParams objects. |
| BusinessPartnerPropertiesService | Object | 0 | 6 | OCQG | classes-05.md | 2044 | 106 | The BusinessPartnerPropertiesService service enables you to update and look up business partner properties in the business partner properties master data table. |
| BusinessPartnerProperty | Object | 3 | 5 | OCQG | classes-05.md | 2151 | 21 | Represents a business partner property that can be assigned to a business partner. |
| BusinessPartnerPropertyParams | Object | 2 | 5 |  | classes-05.md | 2173 | 19 | Holds the key and name of a business partner property. |
| BusinessPartners | Object | 249 | 10 | OCRD | classes-06.md | 3 | 434 | BusinessPartners is a business object that represents the Business Partners Master Data in the Business Partners module. |
| BusinessPartnersService | Object | 0 | 4 | OCRD | classes-06.md | 438 | 229 | The BusinessPartnersService enables to transfer credit or debit amounts from a specified opening balance account to one or more business partner accounts. |
| BusinessPlaceIENumbers | Object | 4 | 3 |  | classes-06.md | 668 | 15 | BusinessPlaceIENumbers Class |
| BusinessPlaces | Object | 53 | 7 | OBPL | classes-06.md | 684 | 107 | BusinessPlaces is a business object that represents a company's business locations. |
| BusinessPlaceTributaryInfos | Object | 9 | 3 |  | classes-06.md | 792 | 20 | BusinessPlaceTributaryInfos Class |
| CallArgument | Object | 2 | 5 | REQ2 | classes-06.md | 813 | 17 | This object represents the list of request arguments related to the request call. |
| CallArguments | Collection | 1 | 5 |  | classes-06.md | 831 | 15 | A collection of CallArgument objects. |
| CallMessage | Object | 8 | 5 | REQ1 | classes-06.md | 847 | 23 | This object represents the response message to the request call. |
| CallMessageArgument | Object | 2 | 5 | REQ3 | classes-06.md | 871 | 17 | This object represents the list of arguments related to the response message. |
| CallMessageArguments | Collection | 1 | 5 |  | classes-06.md | 889 | 15 | A collection of CallMessageArgument objects. |
| CallMessages | Collection | 1 | 5 |  | classes-06.md | 905 | 15 | A collection of CallMessage objects. |
| Campaign | Object | 16 | 5 | OCPN | classes-06.md | 921 | 33 | You can create, maintain, and analyze your marketing event information using the campaign management feature. |
| CampaignBusinessPartner | Object | 43 | 5 | CPN1 | classes-06.md | 955 | 62 | The relevant business partners for the campaign. |
| CampaignBusinessPartners | Collection | 1 | 6 |  | classes-06.md | 1018 | 20 | A collection of CampaignBusinessPartner objects. |
| CampaignItem | Object | 7 | 5 | CPN2 | classes-06.md | 1039 | 26 | The relevant items for the campaign. |
| CampaignItems | Collection | 1 | 6 |  | classes-06.md | 1066 | 20 | A collection of CampaignItem objects. |
| CampaignParams | Object | 2 | 5 |  | classes-06.md | 1087 | 19 | Holds the key to an existing campaign. |
| CampaignPartner | Object | 7 | 5 | CPN3 | classes-06.md | 1107 | 26 | The relevant partners for the campaign. |
| CampaignPartners | Collection | 1 | 6 |  | classes-06.md | 1134 | 20 | A collection of CampaignPartner objects. |
| CampaignResponseType | Object | 3 | 5 |  | classes-06.md | 1155 | 18 | CampaignResponseType Class |
| CampaignResponseTypeParams | Object | 3 | 5 |  | classes-06.md | 1174 | 18 | CampaignResponseTypeParams Class |
| CampaignResponseTypeParamsCollection | Collection | 1 | 5 |  | classes-06.md | 1193 | 15 | CampaignResponseTypeParamsCollection Class |
| CampaignResponseTypeService | Object | 0 | 8 |  | classes-06.md | 1209 | 21 | CampaignResponseTypeService Class |
| CampaignsParams | Collection | 1 | 5 |  | classes-06.md | 1231 | 17 | A collection of CampaignParams objects. |
| CampaignsService | Object | 0 | 9 | OCPN | classes-06.md | 1249 | 72 | The CampaignsService service enables you to add, look up, update, cancel, and remove campaigns. |
| CancelCheckRowParams | Object | 2 | 5 |  | classes-06.md | 1322 | 19 | Holds the key to an existing check. |
| CashDiscount | Object | 6 | 5 | OCDC | classes-06.md | 1342 | 26 | Defines a cash discount policy. |
| CashDiscountParams | Object | 2 | 5 |  | classes-06.md | 1369 | 19 | Holds the key and name to an existing cash discount. |
| CashDiscountsParams | Collection | 1 | 5 |  | classes-06.md | 1389 | 17 | A collection of CashDiscountParams objects. |
| CashDiscountsService | Object | 0 | 8 | OCDC | classes-06.md | 1407 | 124 | The CashDiscountsService service enables you to add, look up and remove cash discount policies. |
| CashFlowAssignments | Object | 8 | 3 |  | classes-06.md | 1532 | 19 | CashFlowAssignments Class |
| CashFlowLineItem | Object | 6 | 5 |  | classes-06.md | 1552 | 21 | CashFlowLineItem Class |
| CashFlowLineItemParams | Object | 2 | 5 |  | classes-06.md | 1574 | 17 | CashFlowLineItemParams Class |
| CashFlowLineItemsParams | Collection | 1 | 5 |  | classes-06.md | 1592 | 15 | CashFlowLineItemsParams Class |
| CashFlowLineItemsService | Object | 0 | 5 |  | classes-06.md | 1608 | 15 | CashFlowLineItemsService Class |
| CategoryGroup | Object | 2 | 5 |  | classes-06.md | 1624 | 17 | CategoryGroup Class |
| CategoryGroupCollection | Collection | 1 | 6 |  | classes-06.md | 1642 | 17 | CategoryGroupCollection Class |
| CCDNumber | Object | 9 | 5 |  | classes-06.md | 1660 | 24 | CCDNumber Class |
| CCDNumbers | Object | 10 | 2 |  | classes-06.md | 1685 | 20 | CCDNumbers Class |
| CertificateSeries | Object | 6 | 5 | OCSN | classes-06.md | 1706 | 26 | Represents a series for TDS (withholding tax) reports. |
| CertificateSeriesParams | Object | 4 | 5 |  | classes-06.md | 1733 | 23 | Holds the key and name to an existing certificate series for TDS (withholding tax) reports. |
| CertificateSeriesParamsCollection | Collection | 1 | 5 |  | classes-06.md | 1757 | 19 | A collection of CertificateSeriesParams objects. |
| CertificateSeriesService | Object | 0 | 8 | OCSN | classes-06.md | 1777 | 125 | The CertificateSeriesService service enables you to add, look up and remove certificate series. |
| CESTCodeData | Object | 3 | 5 | OCEST | classes-06.md | 1903 | 22 | In Brazil CEST Code identify material items which are subject to ST taxation. |
| CESTCodeParams | Object | 1 | 5 |  | classes-06.md | 1926 | 18 | Holds the key to existing CEST code data. |
| CESTCodeService | Object | 0 | 7 | OCEST | classes-07.md | 3 | 69 | The CESTCodeService service enables you to add, look up, update and remove CEST code data. |
| ChangeLogDifferenceParams | Object | 7 | 5 |  | classes-07.md | 73 | 24 | Holds the detailed change information about the selected instances. |
| ChangeLogDifferencesParams | Collection | 1 | 5 |  | classes-07.md | 98 | 17 | A collection of ChangeLogDifferencesParam objects. |
| ChangeLogParams | Object | 4 | 5 |  | classes-07.md | 116 | 21 | Holds the detailed log information of an object. |
| ChangeLogsParams | Collection | 1 | 5 |  | classes-07.md | 138 | 17 | A collection of ChangeLogParams objects. |
| ChangeLogsService | Object | 0 | 5 | OGCL | classes-07.md | 156 | 122 | You can use the change log to gain an overview of changes in most windows of SAP Business One. |
| ChartOfAccounts | Object | 78 | 7 | OACT | classes-07.md | 279 | 192 | ChartOfAccounts is a business object that represents the General Ledger (G/L) accounts in the Finance module. |
| CheckLine | Object | 15 | 5 | OCHH | classes-07.md | 472 | 32 | Represents the deposits for received checks. |
| CheckLineParams | Object | 1 | 5 |  | classes-07.md | 505 | 18 | Holds the key of a received check. |
| CheckLines | Collection | 1 | 5 |  | classes-07.md | 524 | 18 | A data collection of CheckLine objects. |
| CheckLinesParams | Collection | 1 | 5 |  | classes-07.md | 543 | 18 | A data collection of CheckLineParams objects. |
| CheckLinesService | Object | 0 | 5 | OCHH | classes-07.md | 562 | 64 | The CheckLinesService service enables you to get deposits for received checks. |
| ChecksforPayment | Object | 44 | 9 | OCHO | classes-07.md | 627 | 110 | Represents checks that are not tied to a document. |
| ChecksforPaymentDocumentReferences | Object | 9 | 2 | CHO3 | classes-07.md | 738 | 19 | The document references of checks for payment. |
| ChecksforPaymentLines | Object | 10 | 2 | CHO1 | classes-07.md | 758 | 23 | ChecksforPaymentLines is a child object of the ChecksforPayment object that represents the appendix of the check. |
| ChecksforPaymentPrintStatus | Object | 6 | 2 | CHO2 | classes-07.md | 782 | 29 | Represents the print status of Checks for Payment. |
| ChooseFromList | Object | 4 | 7 | OCHF | classes-07.md | 812 | 61 | The ChooseFromList object enables to set the display of the Choose From List for a specified object. |
| ChooseFromList_Lines | Object | 9 | 2 | CHFL | classes-07.md | 874 | 21 | ChooseFromList_Lines is a child object of ChooseFromList. |
| ClosingDateProcedure | Object | 8 | 4 | OCDP | classes-07.md | 896 | 27 | The ClosingDateProcedure object enables to retrieve the closing date procedure definition. |
| Cockpit | Object | 10 | 5 | OCPT | classes-07.md | 924 | 28 | Represents a cockpit, which is a personalized work center where you can view, search, organize, and perform your regular work and related activities. |
| CockpitParams | Object | 2 | 5 |  | classes-07.md | 953 | 19 | Holds the key to an existing cockpit. |
| CockpitsParams | Collection | 1 | 5 |  | classes-07.md | 973 | 18 | A collection of CockpitParams objects. |
| CockpitsService | Object | 0 | 11 | OCPT | classes-07.md | 992 | 121 | The CockpitsService service enables you to add, look up, update, and remove cockpits. |
| ColumnPreferences | Object | 11 | 5 | CPRF | classes-07.md | 1114 | 30 | ColumnPreferences is a Data structure related to the FormPreferencesService. |
| ColumnsPreferences | Collection | 1 | 5 |  | classes-07.md | 1145 | 15 | ColumnsPreferences is a collection of ColumnPreferences data structures. |
| ColumnsPreferencesParams | Object | 2 | 5 | CPRF | classes-07.md | 1161 | 20 | The ColumnsPreferencesParams specifies the identification key combination (user and FormId) for which the FormPreferencesService is related. |
| Command | Object | 2 | 1 |  | classes-07.md | 1182 | 12 | The Command object enables to run SQL stored procedures located in the company database. |
| CommandParam | Object | 4 | 0 |  | classes-07.md | 1195 | 9 | CommandParam is a child object of the Command object and used to retrieve single parameter of the stored procedure. |
| CommandParams | Collection | 1 | 1 |  | classes-07.md | 1205 | 10 | CommandParams is a collection of CommandParam objects. |
| CommissionGroups | Object | 5 | 7 | OCOG | classes-07.md | 1216 | 63 | The CommissionGroups object enables to define commission groups for a sales employee, an item, or a customer. |
| Company | Object | 28 | 28 |  | classes-07.md | 1280 | 291 | Company is the primary DI API object that represents a single SAP Business One company database. |
| CompanyInfo | Object | 35 | 5 | CINF | classes-07.md | 1572 | 76 | The CompanyInfo is a data structure related to the CompanyService. |
| CompanyService | Object | 0 | 30 |  | classes-08.md | 3 | 564 | The CompanyService enables to manage the company administration data. |
| ContactEmployeeBlockSendingMarketingContents | Object | 3 | 3 |  | classes-08.md | 568 | 75 | Block sending marketing contnet to the contact employee. |
| ContactEmployees | Object | 36 | 3 | OCPR | classes-08.md | 644 | 66 | ContactEmployees is a business object that represents the contact employees in the Business Partners module. |
| Contacts | Object | 48 | 6 | OCLG | classes-08.md | 711 | 117 | Contacts is a business object that represents the activities with customers and vendors in the Business Partners module. |
| ContractTemplates | Object | 42 | 8 | OCTT | classes-08.md | 829 | 100 | ContractTemplates is a business object that represents the contract templates in the Service module. |
| CostCenterType | Object | 3 | 5 | OCCT | classes-08.md | 930 | 20 | Represents a cost center type. |
| CostCenterTypeParams | Object | 1 | 5 | OCCT | classes-08.md | 951 | 18 | Holds the key of a cost center type. |
| CostCenterTypes | Collection | 1 | 5 |  | classes-08.md | 970 | 18 | A collection of CostCenterType objects. |
| CostCenterTypesParams | Collection | 1 | 5 |  | classes-08.md | 989 | 18 | A collection of CostCenterTypeParams objects. |
| CostCenterTypesService | Object | 0 | 8 | OCCT | classes-08.md | 1008 | 70 | A cost center type is for selection by future reports and analyses. |
| CostElement | Object | 3 | 5 |  | classes-08.md | 1079 | 18 | CostElement Class |
| CostElementParams | Object | 2 | 5 |  | classes-08.md | 1098 | 17 | CostElementParams Class |
| CostElementService | Object | 0 | 8 |  | classes-08.md | 1116 | 21 | CostElementService Class |
| CostElementsParams | Collection | 1 | 5 |  | classes-08.md | 1138 | 15 | CostElementsParams Class |
| CountriesParams | Collection | 1 | 5 |  | classes-08.md | 1154 | 15 | A data collection of CountryParams identification properties. |
| CountriesService | Object | 0 | 8 | OCRY | classes-08.md | 1170 | 36 | The CountriesService manages the setting of each country in SAP Business One. |
| Country | Object | 19 | 5 | OCRY | classes-08.md | 1207 | 34 | A data structure object holding properties for the CountriesService object. |
| CountryParams | Object | 2 | 5 | OCRY | classes-08.md | 1242 | 17 | This object holds identification properties for the CountriesService object. |
| CreditCardPayments | Object | 23 | 7 | OCDT | classes-08.md | 1260 | 100 | The CreditCardPayments object enables to define dates for incoming payments from the credit card company. |
| CreditCards | Object | 8 | 6 | OCRC | classes-08.md | 1361 | 62 | The CreditCards object enables to define credit cards that the company can use for incoming and outgoing payments. |
| CreditLine | Object | 12 | 5 | OCRH | classes-08.md | 1424 | 29 | Represents the deposits for credit card vouchers. |
| CreditLineParams | Object | 1 | 5 |  | classes-08.md | 1454 | 18 | Holds the key of a credit card payment. |
| CreditLines | Collection | 1 | 5 |  | classes-08.md | 1473 | 18 | A data collection of CreditLine objects. |
| CreditLinesParams | Collection | 1 | 5 |  | classes-08.md | 1492 | 18 | A data collection of CreditLineParams objects. |
| CreditLinesService | Object | 0 | 5 | OCRH | classes-08.md | 1511 | 64 | The CreditLinesService service enables you to get deposits for credit card vouchers. |
| CreditPaymentMethods | Object | 10 | 7 | OCRP | classes-08.md | 1576 | 72 | The CreditPaymentMethods object enables to define payment methods by credit cards. |
| Currencies | Object | 20 | 7 | OCRN | classes-08.md | 1649 | 80 | Currencies is a business object that represents the currency codes in the Administration module. |
| CurrencyRestrictions | Object | 6 | 2 | PYM1 | classes-08.md | 1730 | 19 | The CurrencyRestrictions is a child object of the WizardPaymentMethods object. |
| CustomerEquipmentCards | Object | 37 | 8 | OINS | classes-08.md | 1750 | 96 | CustomerEquipmentCards is a business object that represents the customer equipment cards in the Services module. |
| CustomerEquipmentCards_BusinessPartners | Object | 3 | 3 |  | classes-08.md | 1847 | 14 | Items_PreferredVendors Class |
| CustomsDeclaration | Object | 10 | 5 | OCCD | classes-08.md | 1862 | 25 | A data structure related with the CustomsDeclarationService holding the information about a Cargo Customs Declaration (CCD). |
| CustomsDeclarationParams | Object | 1 | 5 |  | classes-08.md | 1888 | 16 | A data structure holding identification properties for the CustomsDeclarationService. |
| CustomsDeclarationService | Object | 0 | 7 | OCCD | classes-08.md | 1905 | 20 | The CustomsDeclarationService enables to manage the Cargo Customs Declarations (CCD). |
| CustomsGroups | Object | 14 | 7 | OARG | classes-09.md | 3 | 72 | The CustomsGroups object enables to define custom groups, which specify the customs duty for items purchased abroad that are liable for customs. |
| CycleCountDetermination | Object | 3 | 5 |  | classes-09.md | 76 | 19 | CycleCountDetermination Class |
| CycleCountDeterminationParams | Object | 2 | 5 |  | classes-09.md | 96 | 17 | CycleCountDeterminationParams Class |
| CycleCountDeterminationParamsCollection | Collection | 1 | 5 |  | classes-09.md | 114 | 15 | CycleCountDeterminationParamsCollection Class |
| CycleCountDeterminationSetup | Object | 9 | 5 |  | classes-09.md | 130 | 27 | This object enables setting up cycle count determination. |
| CycleCountDeterminationSetupCollection | Collection | 1 | 5 |  | classes-09.md | 158 | 15 | CycleCountDeterminationSetupCollection Class |
| CycleCountDeterminationsService | Object | 0 | 6 |  | classes-09.md | 174 | 37 | You can setup cycle count determinations via this service. |
| DashboardPackageImportParams | Object | 4 | 5 |  | classes-09.md | 212 | 19 | DashboardPackageImportParams Class |
| DashboardPackageParams | Object | 1 | 5 |  | classes-09.md | 232 | 16 | DashboardPackageParams Class |
| DashboardPackagesParams | Collection | 1 | 5 |  | classes-09.md | 249 | 15 | DashboardPackagesParams Class |
| DashboardPackagesService | Object | 0 | 4 |  | classes-09.md | 265 | 14 | DashboardPackagesService Class |
| DataBrowser | Object | 4 | 7 |  | classes-09.md | 280 | 25 | The DataBrowser enables to navigate between records that are selected from the database or from XML formatted data. |
| DataSensitiveStatus | Object | 1 | 5 |  | classes-09.md | 306 | 16 | DataSensitiveStatus Class |
| DecimalData | Object | 3 | 5 |  | classes-09.md | 323 | 20 | Represents the data before rounding. |
| DeductionTaxGroups | Object | 7 | 6 | ODDG | classes-09.md | 344 | 61 | Represents withholding tax groups. |
| DeductionTaxHierarchies | Object | 12 | 6 | ODDT | classes-09.md | 406 | 68 | The DeductionTaxHierarchies object enables to define taxation levels to withhold from payments to vendors. |
| DeductionTaxHierarchies_Lines | Object | 5 | 2 | DDT1 | classes-09.md | 475 | 18 | The DeductionTaxHierarchies_Lines is a child object of DeductionTaxHierarchies object. |
| DeductionTaxSubGroup | Object | 2 | 5 |  | classes-09.md | 494 | 19 | DeductionTaxSubGroup Class |
| DeductionTaxSubGroupParams | Object | 2 | 5 |  | classes-09.md | 514 | 19 | DeductionTaxSubGroupParams Class |
| DeductionTaxSubGroupsParams | Collection | 1 | 5 |  | classes-09.md | 534 | 18 | DeductionTaxSubGroupsParams Class |
| DeductionTaxSubGroupsService | Object | 0 | 7 |  | classes-09.md | 553 | 66 | DeductionTaxSubGroupsService Class |
| DefaultCreditCards | Object | 5 | 2 | UDG2 | classes-09.md | 620 | 18 | The DefaultCreditCards is a child object of the UserDefaultGroups object. |
| DefaultDocuments | Object | 15 | 2 | UDG1 | classes-09.md | 639 | 39 | The DefaultDocuments is a child object of the UserDefaultGroups object. |
| DefaultElectronicSeriesParams | Object | 2 | 5 |  | classes-09.md | 679 | 17 | DefaultElectronicSeriesParams Class |
| DefaultElementsforCR | Object | 2 | 5 | OMLP | classes-09.md | 697 | 21 | With default elements in SAP Business One, you can maintain unified translations for Crystal Reports layouts according to different document languages. |
| DefaultElementsforCRParams | Object | 2 | 5 |  | classes-09.md | 719 | 19 | Holds the key of a default elements for Crystal Reports. |
| DefaultElementsforCRService | Object | 0 | 5 | OMLP | classes-09.md | 739 | 63 | The DefaultElementsforCRService service enables you to add and look up default elements for Crystal Reports. |
| DefaultPTICodes | Object | 4 | 2 |  | classes-09.md | 803 | 14 | DefaultPTICodes Class |
| DefaultReportParams | Object | 4 | 5 | RDFL | classes-09.md | 818 | 23 | Specifies the default report layout for a document type. |
| Department | Object | 3 | 5 | OUDP | classes-09.md | 842 | 21 | Represents a department that can be assigned to a user or employee. |
| DepartmentParams | Object | 2 | 5 |  | classes-09.md | 864 | 18 | Holds the key and name of a department. |
| DepartmentsParams | Collection | 1 | 5 |  | classes-09.md | 883 | 17 | A collection of DepartmentParams objects. |
| DepartmentsService | Object | 0 | 8 | OUDP | classes-09.md | 901 | 118 | The DepartmentsService service enables you to add, look up and remove departments in the departments master data table. |
| Deposit | Object | 49 | 5 | ODPS | classes-09.md | 1020 | 71 | Represents the deposits for received checks, credit card vouchers, and cash. |
| DepositParams | Object | 3 | 5 |  | classes-09.md | 1092 | 20 | Holds the key to an existing deposit. |
| DepositsParams | Collection | 1 | 5 |  | classes-09.md | 1113 | 18 | A collection of DepositParams objects. |
| DepositsService | Object | 0 | 11 | ODPS | classes-09.md | 1132 | 172 | The DepositsService service enables you to add, look up, update and cancel deposits for: - Cash - Checks - Credit card vouchers For Chile, France, Italy, Portugal, and Spain localizations, you can view deposited bills of |
| DepreciationArea | Object | 13 | 5 | ODPA | classes-09.md | 1305 | 30 | In SAP Business One, you can use different depreciation areas for showing the value of fixed assets for a specific purpose. |
| DepreciationAreaParams | Object | 2 | 5 |  | classes-09.md | 1336 | 19 | Holds the key to an existing depreciation area. |
| DepreciationAreaParamsCollection | Collection | 1 | 5 |  | classes-09.md | 1356 | 18 | A collection of DepreciationAreaParams objects. |
| DepreciationAreasService | Object | 0 | 8 | ODPA | classes-09.md | 1375 | 23 | The DepreciationAreasService service enables you to create, update, and view depreciation areas. |
| DepreciationLevel | Object | 5 | 5 | DTP1 | classes-09.md | 1399 | 22 | DepreciationLevel is a child object of DepreciationType object. |
| DepreciationLevelCollection | Collection | 1 | 5 |  | classes-09.md | 1422 | 18 | A collection of DepreciationLevel objects. |
| DepreciationType | Object | 44 | 5 | ODTP | classes-09.md | 1441 | 67 | In SAP Business One, you can use depreciation types to define different depreciation calculation methods for your fixed assets. |
| DepreciationTypeParams | Object | 2 | 5 |  | classes-09.md | 1509 | 19 | DepreciationTypeParams Class |
| DepreciationTypeParamsCollection | Collection | 1 | 5 |  | classes-09.md | 1529 | 18 | DepreciationTypeParamsCollection Class |
| DepreciationTypePool | Object | 2 | 5 | ODPP | classes-09.md | 1548 | 19 | Source table: ODPP. |
| DepreciationTypePoolParams | Object | 2 | 5 |  | classes-09.md | 1568 | 19 | DepreciationTypePoolParams Class |
| DepreciationTypePoolParamsCollection | Collection | 1 | 5 |  | classes-09.md | 1588 | 18 | DepreciationTypePoolParamsCollection Class |
| DepreciationTypePoolsService | Object | 0 | 8 | ODPP | classes-09.md | 1607 | 21 | Source table: ODPP. |
| DepreciationTypesService | Object | 0 | 8 | ODTP | classes-09.md | 1629 | 23 | The DepreciationTypesService service enables you to create, update, and view depreciation types. |
| DeterminationCriteria | Object | 4 | 5 | ODMC | classes-09.md | 1653 | 21 | The available determination criteria are predefined (you cannot define additional determination criteria): Item Group Item Code Warehouse Code Business Partner Group Ship-to Country Ship-to State You can activate and pri |
| DeterminationCriteriaParams | Object | 1 | 5 |  | classes-09.md | 1675 | 18 | Holds the key to an existing determination criteria. |
| DeterminationCriteriaParamsCollection | Collection | 1 | 5 |  | classes-09.md | 1694 | 18 | A collection of DeterminationCriteriaParams objects. |
| DeterminationCriteriasService | Object | 0 | 6 | ODMC | classes-09.md | 1713 | 86 | The DeterminationCriteriasService service enables you to look up and update determination criteria. |
| Dimension | Object | 5 | 5 | ODIM | classes-09.md | 1800 | 25 | Represents one of the five system-defined dimensions, which can be assigned to a profit center or distribution rule. |
| DimensionParams | Object | 2 | 5 |  | classes-09.md | 1826 | 19 | Holds the key and name of a dimension. |
| DimensionsParams | Collection | 1 | 5 |  | classes-09.md | 1846 | 17 | A collection of DimensionParams objects. |
| DimensionsService | Object | 0 | 6 | ODIM | classes-09.md | 1864 | 99 | The DimensionsService service enables you to activate dimensions, as well as change a dimension's description. |
| DiscountGroupLine | Object | 8 | 5 |  | classes-09.md | 1964 | 23 | DiscountGroupLine Class |
| DiscountGroupLineCollection | Collection | 1 | 6 |  | classes-09.md | 1988 | 17 | DiscountGroupLineCollection Class |
| DiscountGroups | Object | 5 | 3 | OEDG | classes-09.md | 2006 | 41 | Represents a set of item discounts for a specific business partner. |
| DiscountLine | Object | 6 | 5 | CDC1 | classes-09.md | 2048 | 27 | Defines a single criteria for applying a cash discount, as well as the discount percentage. |
| DiscountLines | Collection | 1 | 6 |  | classes-10.md | 3 | 19 | A collection of DiscountLine objects. |
| DistributionRule | Object | 9 | 5 | OOCR | classes-10.md | 23 | 29 | Represents a distribution rule for spreading a specific expense, account, journal entry, or other entity among profit centers. |
| DistributionRuleLine | Object | 4 | 5 | OCR1 | classes-10.md | 53 | 23 | Specifies a profit center to which to assign part of any cost or expense that is tied to a distribution rule. |
| DistributionRuleLines | Collection | 1 | 5 |  | classes-10.md | 77 | 17 | A collection of DistributionRuleLine objects. |
| DistributionRuleParams | Object | 2 | 5 |  | classes-10.md | 95 | 19 | Holds the key and name of a distribution rule. |
| DistributionRulesParams | Collection | 1 | 5 |  | classes-10.md | 115 | 17 | A collection of DistributionRuleParams objects. |
| DistributionRulesService | Object | 0 | 8 | OOCR | classes-10.md | 133 | 210 | The DistributionRulesService service enables you to add, look up and remove distribution rules for spreading a specific expense, account, journal entry, or other entity among profit centers. |
| DNFCodeSetup | Object | 5 | 5 | ODNF | classes-10.md | 344 | 26 | Represents a DNF code that can be assigned to an item. |
| DNFCodeSetupParams | Object | 3 | 5 |  | classes-10.md | 371 | 20 | Holds the key and name of a DNF code. |
| DNFCodeSetupParamsCollection | Collection | 1 | 5 |  | classes-10.md | 392 | 17 | A collection of DNFCodeSetupParams objects. |
| DNFCodeSetupService | Object | 0 | 8 | ODNF | classes-10.md | 410 | 114 | The DNFCodeSetupService service enables you to add, look up and remove DNF codes in the DNF codes master data table. |
| DocsInWTGroups | Object | 9 | 1 |  | classes-10.md | 525 | 18 | DocsInWTGroups Class |
| Document_ApprovalRequests | Object | 5 | 1 | OWDDV | classes-10.md | 544 | 14 | Documents_ApprovalRequests is a child object of the Documents object. |
| Document_DocumentReferences | Object | 18 | 3 |  | classes-10.md | 559 | 29 | Document_DocumentReferences Class |
| Document_EWayBillDetails | Object | 35 | 0 |  | classes-10.md | 589 | 40 | Document_EWayBillDetails Class |
| Document_Installments | Object | 10 | 3 | INV6, OPCH6 | classes-10.md | 630 | 103 | A child object of Documents object representing the installments feature in marketing documents. |
| Document_Lines | Object | 230 | 3 |  | classes-10.md | 734 | 368 | Document_Lines is a child object of Documents object and represents the line entries of a document in the Marketing Documents and Receipts module and the Inventory and Production module. |
| Document_LinesAdditionalExpenses | Object | 48 | 2 |  | classes-10.md | 1103 | 65 | Document_LinesAdditionalExpenses is a child object of Document_Lines and represents the line entries of the additional expenses document in the Marketing Documents module. |
| Document_SpecialLines | Object | 24 | 3 | INV10 and IN10V | classes-10.md | 1169 | 77 | This object represents text and subtotal lines in marketing documents. |
| DocumentChangeMenuName | Object | 3 | 5 |  | classes-10.md | 1247 | 22 | Represents the user-defined menu name for a specific document type/document subtype. |
| DocumentLinesBinAllocations | Object | 6 | 2 | INV19 | classes-10.md | 1270 | 18 | DocumentLinesBinAllocations is a child object of the Document_Lines object that represents the bin allocation of items or serial items or batch items. |
| DocumentPackageItems | Object | 7 | 3 | DLN8 | classes-10.md | 1289 | 79 | A data structure holding the properties of items in a package. |
| DocumentPackages | Object | 7 | 3 | DLN7, DLN8, INV7, INV8 | classes-10.md | 1369 | 89 | This object holds a collection of packaging types you can attach to items in Delivery or A/R Invoice documents. |
| Documents | Object | 290 | 17 |  | classes-11.md | 3 | 633 | Documents is a business object that represents the header data of documents in the Marketing Documents and Receipts module and the Inventory and Production module of SAP Business One application. |
| DocumentsAdditionalExpenses | Object | 60 | 2 |  | classes-11.md | 637 | 81 | DocumentsAdditionalExpenses is a child object of Documents object and represents the documents of additional expenses in the Marketing Documents module. |
| DocumentSeriesParams | Object | 3 | 5 | NNM1 | classes-11.md | 719 | 20 | The DocumentSeriesParams specifies the identification key combination (Document and Series) for which the Documents is related. |
| DocumentSeriesUserParams | Object | 4 | 5 | NNM2 | classes-11.md | 740 | 19 | The DocumentSeriesUserParams specifies the identification key combination (Document, Series and Users) for which Documents is related. |
| DocumentTypeParams | Object | 2 | 5 | NNM2 | classes-11.md | 760 | 17 | The DocumentTypeParams specifies the identification key combination (Document and DocumentSubType) for which the Documents object is related. |
| DownPaymentsToDraw | Object | 21 | 2 | INV9, PCH9, RIN9, RPC9, DRF9 | classes-11.md | 778 | 35 | Represents down payments drawn into A/R or A/P invoices. |
| DownPaymentsToDrawDetails | Object | 19 | 2 | INV11, PCH11, RIN11, RPC11, DRF11 | classes-11.md | 814 | 128 | Represents detail lines for the DownPaymentsToDraw object. |
| DppChangeParams | Object | 3 | 5 |  | classes-11.md | 943 | 18 | DppChangeParams Class |
| DunningLetters | Object | 10 | 7 | ODUN | classes-11.md | 962 | 70 | Represents a list of dunning levels that is used as a template when creating a new dunning term. |
| DunningTerm | Object | 19 | 5 | ODUT | classes-11.md | 1033 | 40 | Represents a dunning term, which defines a set of dunning levels that determine when to send dunning letters for past-due balances. |
| DunningTermLine | Object | 8 | 5 | DUT1 | classes-11.md | 1074 | 25 | Represents a criterion for sending out a dunning letter. |
| DunningTermLines | Collection | 1 | 6 |  | classes-11.md | 1100 | 19 | A collection of DunningTermLine objects. |
| DunningTermParams | Object | 2 | 5 |  | classes-11.md | 1120 | 19 | Holds the key and name of a dunning term. |
| DunningTermsParams | Collection | 1 | 5 |  | classes-11.md | 1140 | 17 | A collection of DunningTermParams objects. |
| DunningTermsService | Object | 0 | 8 | ODUT | classes-11.md | 1158 | 184 | The DunningTermsService service enables you to add, look up and remove dunning terms for defining when to send out dunning terms for delinquent balances. |
| DynamicSystemStrings | Object | 8 | 7 | SDIS | classes-11.md | 1343 | 70 | The DynamicSystemStrings object enables to modify the field name and format in the interface to match the terms used in your company. |
| EBooks | Object | 19 | 5 | OEBK | classes-11.md | 1414 | 36 | Source table: OEBK. |
| EBooks_Doc_Details | Object | 15 | 0 |  | classes-11.md | 1451 | 20 | EBooks_Doc_Details Class |
| EBooksLine | Object | 10 | 5 | EBK1 | classes-11.md | 1472 | 27 | Source table: EBK1. |
| EBooksLines | Collection | 1 | 5 |  | classes-11.md | 1500 | 17 | EBooksLines Class |
| EBooksParams | Object | 3 | 5 |  | classes-11.md | 1518 | 20 | EBooksParams Class |
| EBooksParamsCollection | Collection | 1 | 5 |  | classes-11.md | 1539 | 17 | EBooksParamsCollection Class |
| EBooksService | Object | 0 | 7 | OEBK | classes-11.md | 1557 | 20 | Source table: OEBK. |
| EcmAction | Object | 25 | 5 |  | classes-11.md | 1578 | 40 | EcmAction Class |
| EcmActionDocParams | Object | 3 | 5 |  | classes-12.md | 3 | 18 | EcmActionDocParams Class |
| EcmActionLog | Object | 9 | 5 |  | classes-12.md | 22 | 24 | EcmActionLog Class |
| EcmActionLogCollection | Collection | 1 | 5 |  | classes-12.md | 47 | 15 | EcmActionLogCollection Class |
| EcmActionLogParams | Object | 2 | 5 |  | classes-12.md | 63 | 17 | EcmActionLogParams Class |
| EcmActionParams | Object | 1 | 5 |  | classes-12.md | 81 | 16 | EcmActionParams Class |
| ECMActionStatusData | Object | 5 | 5 |  | classes-12.md | 98 | 20 | ECMActionStatusData Class |
| ECMCodeParams | Object | 1 | 5 |  | classes-12.md | 119 | 16 | ECMCodeParams Class |
| ECMCodeParamsCollection | Collection | 1 | 5 |  | classes-12.md | 136 | 15 | ECMCodeParamsCollection Class |
| EDFDocMapping | Object | 3 | 5 |  | classes-12.md | 152 | 18 | EDFDocMapping Class |
| EDFDocMappingInputParams | Object | 2 | 5 |  | classes-12.md | 171 | 17 | EDFDocMappingInputParams Class |
| EDFDocMappingsCollection | Collection | 1 | 5 |  | classes-12.md | 189 | 15 | EDFDocMappingsCollection Class |
| EDFEntriesCollection | Collection | 1 | 5 |  | classes-12.md | 205 | 15 | EDFEntriesCollection Class |
| EDFEntry | Object | 40 | 5 |  | classes-12.md | 221 | 55 | EDFEntry Class |
| EDFEntryAddLogInputParams | Object | 9 | 5 |  | classes-12.md | 277 | 24 | EDFEntryAddLogInputParams Class |
| EDFEntryInputParams | Object | 2 | 5 |  | classes-12.md | 302 | 17 | EDFEntryInputParams Class |
| EDFEntryListInputParams | Object | 14 | 5 |  | classes-12.md | 320 | 29 | EDFEntryListInputParams Class |
| EDFEntryLog | Object | 9 | 5 |  | classes-12.md | 350 | 24 | EDFEntryLog Class |
| EDFEntryLogInputParams | Object | 7 | 5 |  | classes-12.md | 375 | 22 | EDFEntryLogInputParams Class |
| EDFEntryLogsCollection | Collection | 1 | 5 |  | classes-12.md | 398 | 15 | EDFEntryLogsCollection Class |
| EDFImportEntry | Object | 17 | 5 | ECM8 | classes-12.md | 414 | 36 | Electronic document import files. |
| EDFMapping | Object | 4 | 5 |  | classes-12.md | 451 | 19 | EDFMapping Class |
| EDFMappingInputParams | Object | 1 | 5 |  | classes-12.md | 471 | 16 | EDFMappingInputParams Class |
| EDFProtocol | Object | 3 | 5 |  | classes-12.md | 488 | 18 | EDFProtocol Class |
| EDFProtocolInputParams | Object | 3 | 5 |  | classes-12.md | 507 | 18 | EDFProtocolInputParams Class |
| EDFProtocolParameter | Object | 6 | 5 |  | classes-12.md | 526 | 21 | EDFProtocolParameter Class |
| EDFProtocolParametersCollection | Collection | 1 | 5 |  | classes-12.md | 548 | 15 | EDFProtocolParametersCollection Class |
| EDFProtocolsCollection | Collection | 1 | 5 |  | classes-12.md | 564 | 15 | EDFProtocolsCollection Class |
| EDFProtocolWithParameters | Object | 4 | 5 |  | classes-12.md | 580 | 19 | EDFProtocolWithParameters Class |
| ElectronicCommunicationActionService | Object | 0 | 8 |  | classes-12.md | 600 | 22 | ElectronicCommunicationActionService Class |
| ElectronicCommunicationActionsService | Object | 0 | 11 |  | classes-12.md | 623 | 28 | ElectronicCommunicationActionsService Class |
| ElectronicDocumentService | Object | 0 | 16 |  | classes-12.md | 652 | 37 | ElectronicDocumentService Class |
| ElectronicFileFormat | Object | 8 | 5 | OLLF | classes-12.md | 690 | 25 | Represents the generic electronic file formats in SAP Business One. |
| ElectronicFileFormatParams | Object | 2 | 5 |  | classes-12.md | 716 | 19 | Holds the key and name to an existing electronic file format. |
| ElectronicFileFormatsParams | Collection | 1 | 5 |  | classes-12.md | 736 | 18 | A collection of ElectronicFileFormatParams objects. |
| ElectronicFileFormatsService | Object | 0 | 7 | OLLF | classes-12.md | 755 | 68 | The ElectronicFileFormatsService service enables you to import, look up, and delete the generic electronic file formats in SAP Business One. |
| ElectronicProtocol | Object | 12 | 5 |  | classes-12.md | 824 | 27 | ElectronicProtocol Class |
| ElectronicProtocolCollection | Collection | 1 | 5 |  | classes-12.md | 852 | 15 | ElectronicProtocolCollection Class |
| ElectronicProtocols | Object | 27 | 3 |  | classes-12.md | 868 | 38 | ElectronicProtocols Class |
| ElectronicReportInfo | Object | 2 | 0 |  | classes-12.md | 907 | 19 | Setup values for electronic reports. |
| ElectronicSeries | Object | 10 | 5 |  | classes-12.md | 927 | 25 | ElectronicSeries Class |
| ElectronicSeriesCollection | Collection | 1 | 5 |  | classes-12.md | 953 | 15 | ElectronicSeriesCollection Class |
| ElectronicSeriesParams | Object | 1 | 5 |  | classes-12.md | 969 | 16 | ElectronicSeriesParams Class |
| EmailGroup | Object | 2 | 5 |  | classes-12.md | 986 | 17 | EmailGroup Class |
| EmailGroupParams | Object | 2 | 5 |  | classes-12.md | 1004 | 17 | EmailGroupParams Class |
| EmailGroupParamsCollection | Collection | 1 | 5 |  | classes-12.md | 1022 | 15 | EmailGroupParamsCollection Class |
| EmailGroupsService | Object | 0 | 8 |  | classes-12.md | 1038 | 21 | EmailGroupsService Class |
| EmployeeAbsenceInfo | Object | 9 | 2 | HEM1 | classes-12.md | 1060 | 22 | EmployeeAbsenceInfo is a child object of the EmployeesInfo object and represents the employee absence information. |
| EmployeeBranchAssignment | Object | 3 | 3 |  | classes-12.md | 1083 | 14 | EmployeeBranchAssignment Class |
| EmployeeEducationInfo | Object | 10 | 2 | HEM2 | classes-12.md | 1098 | 22 | EmployeeEducationInfo is a child object of the EmployeesInfo object and represents the employee education information. |
| EmployeeFullNamesParams | Object | 2 | 0 |  | classes-12.md | 1121 | 7 | EmployeeFullNamesParams Class |
| EmployeeFullNamesParamsCollection | Collection | 1 | 5 |  | classes-12.md | 1129 | 15 | EmployeeFullNamesParamsCollection Class |
| EmployeeIDType | Object | 1 | 5 |  | classes-12.md | 1145 | 16 | EmployeeIDType Class |
| EmployeeIDTypeParams | Object | 1 | 5 |  | classes-12.md | 1162 | 16 | EmployeeIDTypeParams Class |
| EmployeeIDTypeParamsCollection | Collection | 1 | 5 |  | classes-12.md | 1179 | 15 | EmployeeIDTypeParamsCollection Class |
| EmployeeIDTypeService | Object | 0 | 8 |  | classes-12.md | 1195 | 21 | EmployeeIDTypeService Class |
| EmployeePosition | Object | 3 | 5 |  | classes-12.md | 1217 | 18 | EmployeePosition Class |
| EmployeePositionParams | Object | 3 | 5 |  | classes-12.md | 1236 | 18 | EmployeePositionParams Class |
| EmployeePositionParamsCollection | Collection | 1 | 5 |  | classes-12.md | 1255 | 15 | EmployeePositionParamsCollection Class |
| EmployeePositionService | Object | 0 | 8 |  | classes-12.md | 1271 | 21 | EmployeePositionService Class |
| EmployeePrevEmpoymentInfo | Object | 9 | 2 | HEM4 | classes-12.md | 1293 | 21 | EmployeePrevEmploymentInfo is a child object of the EmployeesInfo object and represents the employee previous employment information. |
| EmployeeReviewsInfo | Object | 9 | 2 | HEM3 | classes-12.md | 1315 | 21 | EmployeeReviewsInfo is a child object of the EmployeesInfo object and represents the employee reviews information. |
| EmployeeRoleSetup | Object | 3 | 5 | OHTY | classes-12.md | 1337 | 20 | Represents an employee role. |
| EmployeeRoleSetupParams | Object | 2 | 5 |  | classes-12.md | 1358 | 19 | Holds the key and name to an existing employee role. |
| EmployeeRoleSetupParamsCollection | Collection | 1 | 5 |  | classes-12.md | 1378 | 17 | A collection of EmployeeRoleSetupParams objects. |
| EmployeeRolesInfo | Object | 5 | 2 | HEM6 | classes-12.md | 1396 | 17 | A child object of the EmployeesInfo object that represents the employee roles, for example, technician, sales employee and purchasing. |
| EmployeeRolesSetupService | Object | 0 | 8 | OHTY | classes-12.md | 1414 | 142 | The EmployeeRolesSetupService service enables you to add, look up and remove roles in the employee roles master data table. |
| EmployeeSavingsPaymentInfo | Object | 14 | 2 | HEM7 | classes-12.md | 1557 | 27 | A child object of the EmployeesInfo object that represents the employee's capital formation savings payments. |
| EmployeesInfo | Object | 127 | 8 | OHEM | classes-12.md | 1585 | 191 | EmployeesInfo is a business object that represents the employee master data in the Human Resources module. |
| EmployeeStatus | Object | 3 | 5 |  | classes-12.md | 1777 | 18 | EmployeeStatus Class |
| EmployeeStatusParams | Object | 3 | 5 |  | classes-12.md | 1796 | 18 | EmployeeStatusParams Class |
| EmployeeStatusParamsCollection | Collection | 1 | 5 |  | classes-12.md | 1815 | 15 | EmployeeStatusParamsCollection Class |
| EmployeeStatusService | Object | 0 | 8 |  | classes-12.md | 1831 | 21 | EmployeeStatusService Class |
| EmployeeTransfer | Object | 8 | 5 | OHET | classes-12.md | 1853 | 25 | Represents the employee transfer record to the payroll provider. |
| EmployeeTransferDetail | Object | 6 | 5 | HET1 | classes-12.md | 1879 | 23 | EmployeeTransferDetail is a child object of the EmployeeTransfer object. |
| EmployeeTransferDetails | Collection | 1 | 5 |  | classes-12.md | 1903 | 17 | A collection of EmployeeTransferDetail objects. |
| EmployeeTransferParams | Object | 1 | 5 | OHET | classes-12.md | 1921 | 18 | Holds the key of an employee transfer. |
| EmployeeTransfersParams | Collection | 1 | 5 |  | classes-12.md | 1940 | 17 | A collection of EmployeeTransferParams objects. |
| EmployeeTransfersService | Object | 0 | 8 | OHET | classes-12.md | 1958 | 74 | EmployeeTransfersService is a business object that manages employee master data transfers from SAP Business One to the DATEV HR client application. |
| EmploymentCategory | Object | 2 | 5 | OETC | classes-12.md | 2033 | 19 | Source table: OETC. |
| EmploymentCategoryParams | Object | 1 | 5 |  | classes-12.md | 2053 | 18 | EmploymentCategoryParams Class |
| EmploymentCategoryService | Object | 0 | 7 | OETC | classes-12.md | 2072 | 21 | Source table: OETC. |
| EmploymentCategorysParams | Collection | 1 | 5 |  | classes-12.md | 2094 | 18 | EmploymentCategorysParams Class |
| EnhancedDiscountGroup | Object | 8 | 5 |  | classes-12.md | 2113 | 23 | EnhancedDiscountGroup Class |
| EnhancedDiscountGroupCollectionParams | Collection | 1 | 5 |  | classes-12.md | 2137 | 15 | EnhancedDiscountGroupCollectionParams Class |
| EnhancedDiscountGroupParams | Object | 3 | 5 |  | classes-12.md | 2153 | 18 | EnhancedDiscountGroupParams Class |
| EnhancedDiscountGroupsService | Object | 0 | 8 |  | classes-12.md | 2172 | 21 | EnhancedDiscountGroupsService Class |
| EWBTransporter | Object | 5 | 5 |  | classes-12.md | 2194 | 20 | EWBTransporter Class |
| EWBTransporter_Line | Object | 5 | 5 |  | classes-12.md | 2215 | 20 | EWBTransporter_Line Class |
| EWBTransporter_Lines | Collection | 1 | 6 |  | classes-12.md | 2236 | 17 | EWBTransporter_Lines Class |
| EWBTransporterParams | Object | 4 | 5 |  | classes-12.md | 2254 | 19 | EWBTransporterParams Class |
| EWBTransporterParamsCollection | Collection | 1 | 5 |  | classes-12.md | 2274 | 15 | EWBTransporterParamsCollection Class |
| EWBTransporterService | Object | 0 | 8 |  | classes-12.md | 2290 | 21 | EWBTransporterService Class |
| ExceptionalEvent | Object | 2 | 5 | OEPE | classes-12.md | 2312 | 19 | Source table: OEPE. |
| ExceptionalEventParams | Object | 1 | 5 |  | classes-12.md | 2332 | 18 | ExceptionalEventParams Class |
| ExceptionalEventService | Object | 0 | 8 | OEPE | classes-12.md | 2351 | 23 | Source table: OEPE. |
| ExceptionalEventsParams | Collection | 1 | 5 |  | classes-12.md | 2375 | 18 | ExceptionalEventsParams Class |
| ExpenseTypeData | Object | 5 | 5 |  | classes-12.md | 2394 | 20 | ExpenseTypeData Class |
| ExpenseTypeParams | Object | 1 | 5 |  | classes-12.md | 2415 | 16 | ExpenseTypeParams Class |
| ExpenseTypeService | Object | 0 | 6 |  | classes-12.md | 2432 | 18 | ExpenseTypeService Class |
| ExportDetermination | Object | 10 | 5 |  | classes-12.md | 2451 | 25 | ExportDetermination Class |
| ExportDeterminationParams | Object | 7 | 5 |  | classes-12.md | 2477 | 22 | ExportDeterminationParams Class |
| ExportDeterminationsCollection | Collection | 1 | 5 |  | classes-12.md | 2500 | 15 | ExportDeterminationsCollection Class |
| ExportDeterminationService | Object | 0 | 8 |  | classes-13.md | 3 | 22 | ExportDeterminationService Class |
| ExportDeterminationsParams | Object | 1 | 5 |  | classes-13.md | 26 | 16 | ExportDeterminationsParams Class |
| ExportProcesses | Object | 14 | 0 | DOC18 | classes-13.md | 43 | 19 | Source table: DOC18. |
| ExtendedAdminInfo | Object | 35 | 0 | ADM1 | classes-13.md | 63 | 67 | Enables you to set and get additional administration properties, in addition to the properties accessed via the AdminInfo object. |
| ExtendedTranslation | Object | 8 | 5 |  | classes-13.md | 131 | 23 | ExtendedTranslation Class |
| ExtendedTranslation_ItemLine | Object | 9 | 5 |  | classes-13.md | 155 | 24 | ExtendedTranslation_ItemLine Class |
| ExtendedTranslation_ItemLines | Collection | 1 | 6 |  | classes-13.md | 180 | 17 | ExtendedTranslation_ItemLines Class |
| ExtendedTranslation_ResultLine | Object | 5 | 5 |  | classes-13.md | 198 | 20 | ExtendedTranslation_ResultLine Class |
| ExtendedTranslation_ResultLines | Collection | 1 | 6 |  | classes-13.md | 219 | 17 | ExtendedTranslation_ResultLines Class |
| ExtendedTranslationParams | Object | 4 | 5 |  | classes-13.md | 237 | 19 | ExtendedTranslationParams Class |
| ExtendedTranslationsParams | Collection | 1 | 5 |  | classes-13.md | 257 | 15 | ExtendedTranslationsParams Class |
| ExtendedTranslationsService | Object | 0 | 8 |  | classes-13.md | 273 | 21 | ExtendedTranslationsService Class |
| ExternalCall | Object | 10 | 5 | OREQ | classes-13.md | 295 | 25 | ExternalCall object is a request initiated by SAP Business One application that requires to be processed by external applications (e.g. |
| ExternalCallParams | Object | 1 | 5 |  | classes-13.md | 321 | 16 | This object holds identification properties to get an ExternalCall instance. |
| ExternalCallsService | Object | 0 | 6 | OREQ | classes-13.md | 338 | 18 | External Call Service is used as an communication mechanism between Business One and any 3rd party or external applications. |
| ExternalReconciliation | Object | 10 | 5 | OMTH | classes-13.md | 357 | 27 | Represents external reconciliation, which is the comparison of open transactions within SAP Business One with an external account statement. |
| ExternalReconciliationFilterParams | Object | 7 | 5 |  | classes-13.md | 385 | 26 | Specifies the selection criteria for viewing, canceling, or re-creating previous external reconciliations created for business partners or G/L accounts. |
| ExternalReconciliationParams | Object | 2 | 5 |  | classes-13.md | 412 | 19 | Holds the key to an existing parameter set. |
| ExternalReconciliationsParamsCollection | Collection | 1 | 5 |  | classes-13.md | 432 | 18 | A collection of ExternalReconciliationParams objects. |
| ExternalReconciliationsService | Object | 0 | 7 | OMTH | classes-13.md | 451 | 132 | The ExternalReconciliationsService service enables you to add, look up, and cancel external reconciliations. |
| FAAccountDetermination | Object | 21 | 5 | OADT | classes-13.md | 584 | 38 | Account determination enables the system to automatically determine the relevant general ledger accounts for a fixed asset when an asset transaction takes place. |
| FAAccountDeterminationParams | Object | 2 | 5 |  | classes-13.md | 623 | 19 | Holds the key to an existing account determination rule for your fixed assets. |
| FAAccountDeterminationParamsCollection | Collection | 1 | 5 |  | classes-13.md | 643 | 18 | A collection of FAAccountDeterminationParams objects. |
| FAAccountDeterminationsService | Object | 0 | 8 | OADT | classes-13.md | 662 | 70 | The FAAccountDeterminationsService service enables you to define and view different sets of G/L accounts for your fixed assets. |
| FactoringIndicators | Object | 4 | 6 | OIDC | classes-13.md | 733 | 58 | The FactoringIndicators object enables to define a key that can be recorded in certain journal entries and used as a selection criterion in various reports. |
| FeatureStatus | Object | 2 | 5 |  | classes-13.md | 792 | 19 | This object represents the status of a specified feature in the application, whether it is blocked or not according to the installation type: new 2007 release installation or upgrade installation prior to 2007 release. |
| FeatureStatusCollection | Collection | 1 | 5 |  | classes-13.md | 812 | 15 | FeatureStatusCollection is a Data Collection of FeatureStatus data structures. |
| Field | Object | 13 | 2 |  | classes-13.md | 828 | 39 | The Field object contains both standard and custom data access properties. |
| Fields | Collection | 1 | 1 |  | classes-13.md | 868 | 11 | The Fields object is a collection of Field objects. |
| FIFOLayers | Object | 7 | 2 | MRV2 | classes-13.md | 880 | 21 | Specifies the FIFO layers to be updated, and the new values for the quantity and price. |
| FinancePeriod | Object | 15 | 5 | OFPR | classes-13.md | 902 | 30 | The FinancePeriod object is a data structure related to the CompanyService. |
| FinancePeriodParams | Object | 2 | 5 |  | classes-13.md | 933 | 17 | The FinancePeriodParams specifies the identification key(system number, period indicator ) for which the CompanyService is related. |
| FinancePeriods | Collection | 1 | 5 |  | classes-13.md | 951 | 16 | FinancePeriods is a collection of FinancePeriod objects. |
| FinancialYear | Object | 7 | 5 | OFYM | classes-13.md | 968 | 28 | Represents a financial year for TDS (withholding tax) reports. |
| FinancialYearParams | Object | 3 | 5 |  | classes-13.md | 997 | 22 | Holds the key and name to an existing financial period for TDS (withholding tax) reports. |
| FinancialYearsParams | Collection | 1 | 5 |  | classes-13.md | 1020 | 19 | A collection of FinancialYearParams objects. |
| FinancialYearsService | Object | 0 | 8 | OFYM | classes-13.md | 1040 | 143 | The FinancialYearsService service enables you to add, look up and remove financial roles for TDS (withholding tax) reports. |
| FiscalPrinter | Object | 6 | 5 |  | classes-13.md | 1184 | 21 | FiscalPrinter Class |
| FiscalPrinterParams | Object | 1 | 5 |  | classes-13.md | 1206 | 16 | FiscalPrinterParams Class |
| FiscalPrinterService | Object | 0 | 8 |  | classes-13.md | 1223 | 21 | FiscalPrinterService Class |
| FiscalPrintersParams | Collection | 1 | 5 |  | classes-13.md | 1245 | 15 | FiscalPrintersParams Class |
| FixedAssetEndBalance | Object | 10 | 5 | OFEV | classes-13.md | 1261 | 27 | Source table: OFEV. |
| FixedAssetItemsService | Object | 0 | 6 | OFDV, OFEV | classes-13.md | 1289 | 19 | The FixedAssetItemsService service enables you to look up and update the end balance of an asset. |
| FixedAssetValues | Object | 10 | 5 | OFDV | classes-13.md | 1309 | 27 | You can monitor the changes in the value of an asset over the course of one year. |
| FixedAssetValuesParams | Object | 3 | 5 |  | classes-13.md | 1337 | 20 | FixedAssetValuesParams Class |
| FixedAssetValuesParamsCollection | Collection | 1 | 5 |  | classes-13.md | 1358 | 18 | FixedAssetValuesCollection Class |
| FormattedSearches | Object | 15 | 7 | CSHS | classes-13.md | 1377 | 77 | The FormattedSearches object enables to assign a formatted search function to a specified field, so that SAP Business One users can enter values, originated by a pre-defined search process, to the field. |
| FormattedSearchFields | Object | 2 | 3 |  | classes-13.md | 1455 | 13 | FormattedSearchFields Class |
| FormPreferencesService | Object | 0 | 5 |  | classes-13.md | 1469 | 123 | The FormPreferencesService manages the display preferences of a specified form for a specified user. |
| Forms1099 | Object | 5 | 7 | OTNN | classes-13.md | 1593 | 61 | Forms1099 object enables to define new Form 1099 types in addition to the existing types: 1099 Miscellaneous, 1099 Interest, and 1099 Dividends. |
| GeneralCollectionParams | Collection | 1 | 5 |  | classes-13.md | 1655 | 17 | A collection of GeneralDataParams objects. |
| GeneralData | Object | 0 | 8 |  | classes-13.md | 1673 | 25 | Represents a single record of a UDO or a child UDO. |
| GeneralDataCollection | Collection | 1 | 6 |  | classes-13.md | 1699 | 20 | A collection of GeneralData objects, each of which represents a record in a child UDO for a specific record of the main UDO. |
| GeneralDataParams | Object | 0 | 2 |  | classes-13.md | 1720 | 11 | Holds the keys to rows in database tables linked to a UDO data. |
| GeneralService | Object | 0 | 12 |  | classes-13.md | 1732 | 303 | The GeneralService provides access to UDOs. |
| GeneratedAssets | Object | 10 | 3 |  | classes-13.md | 2036 | 21 | GeneratedAssets Class |
| GetChangeLogParams | Object | 3 | 5 |  | classes-13.md | 2058 | 20 | Holds the key to an existing change log. |
| GLAccount | Object | 9 | 5 |  | classes-13.md | 2079 | 26 | GLAccount is a data structure related to the AccountsService. |
| GLAccountAdvancedRule | Object | 81 | 5 | OGAR | classes-14.md | 3 | 100 | The set of rules according to which the G/L account determination takes place. |
| GLAccountAdvancedRuleParams | Object | 10 | 5 |  | classes-14.md | 104 | 27 | Holds the key to an existing advanced G/L account determination rule. |
| GLAccountAdvancedRuleParamsCollection | Collection | 1 | 5 |  | classes-14.md | 132 | 18 | A collection of GLAccountAdvancedRuleParams objects. |
| GLAccountAdvancedRulesService | Object | 0 | 8 | OGAR | classes-14.md | 151 | 98 | The GLAccountAdvancedRulesService service enables you to add, look up, update, and remove advanced G/L account determination rules. |
| GLAccounts | Collection | 1 | 5 |  | classes-14.md | 250 | 15 | GLAccounts is a collection of GLAccount data structures. |
| GovPayCode | Object | 6 | 5 |  | classes-14.md | 266 | 21 | GovPayCode Class |
| GovPayCodeAuthorities | Collection | 1 | 6 |  | classes-14.md | 288 | 17 | GovPayCodeAuthorities Class |
| GovPayCodeAuthority | Object | 4 | 5 |  | classes-14.md | 306 | 19 | GovPayCodeAuthority Class |
| GovPayCodeParams | Object | 2 | 5 |  | classes-14.md | 326 | 17 | GovPayCodeParams Class |
| GovPayCodeParamsCollection | Collection | 1 | 5 |  | classes-14.md | 344 | 15 | GovPayCodeParamsCollection Class |
| GovPayCodesService | Object | 0 | 8 |  | classes-14.md | 360 | 21 | GovPayCodesService Class |
| GTIParams | Object | 2 | 5 |  | classes-14.md | 382 | 17 | GTIParams Class |
| GTIParamsCollection | Collection | 1 | 5 |  | classes-14.md | 400 | 15 | GTIParamsCollection Class |
| GTIsService | Object | 0 | 4 |  | classes-14.md | 416 | 14 | GTIsService Class |
| Holiday | Object | 7 | 5 | OHLD | classes-14.md | 431 | 26 | Specify a set of company holidays. |
| HolidayDate | Object | 4 | 5 | HLD1 | classes-14.md | 458 | 21 | Specify a set of company holiday dates as defined in the Holiday Dates window. |
| HolidayDates | Collection | 1 | 5 |  | classes-14.md | 480 | 18 | A collection of HolidayDate objects. |
| HolidayParams | Object | 1 | 5 |  | classes-14.md | 499 | 18 | Holds the key of a holiday. |
| HolidayService | Object | 0 | 8 | OHLD | classes-14.md | 518 | 154 | The HolidayService service enables you to add, look up, remove, and update holidays. |
| HolidaysParams | Collection | 1 | 5 |  | classes-14.md | 673 | 18 | A collection of HolidayParams objects. |
| HouseBankAccounts | Object | 64 | 7 | DSC1 | classes-14.md | 692 | 144 | The HouseBankAccounts object enables to define the company bank accounts. |
| IdentificationCode | Object | 6 | 5 |  | classes-14.md | 837 | 21 | IdentificationCode Class |
| IdentificationCodeParams | Object | 1 | 5 |  | classes-14.md | 859 | 16 | IdentificationCodeParams Class |
| IdentificationCodes | Collection | 1 | 5 |  | classes-14.md | 876 | 15 | IdentificationCodes Class |
| IdentificationCodeService | Object | 0 | 8 |  | classes-14.md | 892 | 21 | IdentificationCodeService Class |
| ImportDetermination | Object | 9 | 5 |  | classes-14.md | 914 | 24 | ImportDetermination Class |
| ImportDeterminationParams | Object | 3 | 5 |  | classes-14.md | 939 | 18 | ImportDeterminationParams Class |
| ImportDeterminationsCollection | Collection | 1 | 5 |  | classes-14.md | 958 | 15 | ImportDeterminationsCollection Class |
| ImportDeterminationService | Object | 0 | 8 |  | classes-14.md | 974 | 22 | ImportDeterminationService Class |
| ImportDeterminationsParams | Object | 1 | 5 |  | classes-14.md | 997 | 16 | ImportDeterminationsParams Class |
| ImportFileParam | Object | 1 | 5 |  | classes-14.md | 1014 | 18 | Borrows an existing field to input the EFM file path. |
| ImportProcesses | Object | 11 | 0 | DOC17 | classes-14.md | 1033 | 16 | Source table: DOC17. |
| IndiaHsn | Object | 6 | 5 | OCHP | classes-14.md | 1050 | 25 | India HSN master data. |
| IndiaHsnParams | Object | 2 | 5 |  | classes-14.md | 1076 | 19 | The parameters needed for searching HSN |
| IndiaHsnParamsCollection | Collection | 1 | 5 |  | classes-14.md | 1096 | 18 | IndiaHsnParamsCollection Class |
| IndiaHsnService | Object | 0 | 8 | OCHP | classes-14.md | 1115 | 84 | India HSN master data. |
| IndiaSacCode | Object | 3 | 5 |  | classes-14.md | 1200 | 18 | IndiaSacCode Class |
| IndiaSacCodeParams | Object | 2 | 5 |  | classes-14.md | 1219 | 17 | IndiaSacCodeParams Class |
| IndiaSacCodeParamsCollection | Collection | 1 | 5 |  | classes-14.md | 1237 | 15 | IndiaSacCodeParamsCollection Class |
| IndiaSacCodeService | Object | 0 | 8 |  | classes-14.md | 1253 | 21 | IndiaSacCodeService Class |
| IndividualCounter | Object | 6 | 5 | INC8 | classes-14.md | 1275 | 23 | Individual counters conduct independent counting of an item at a storage location. |
| IndividualCounters | Collection | 1 | 6 |  | classes-14.md | 1299 | 20 | A collection of IndividualCounter objects. |
| Industries | Object | 5 | 6 | OOND | classes-14.md | 1320 | 61 | Industries is a business object that represents the industries list from which an industry can be associated with a sales opportunity. |
| IntegrationPackageConfigure | Object | 4 | 5 |  | classes-14.md | 1382 | 19 | IntegrationPackageConfigure Class |
| IntegrationPackageParams | Object | 1 | 5 |  | classes-14.md | 1402 | 16 | IntegrationPackageParams Class |
| IntegrationPackagesConfigureService | Object | 0 | 6 |  | classes-14.md | 1419 | 17 | IntegrationPackagesConfigureService Class |
| IntegrationPackagesParams | Collection | 1 | 5 |  | classes-14.md | 1437 | 15 | IntegrationPackagesParams Class |
| InternalReconciliation | Object | 8 | 5 |  | classes-14.md | 1453 | 23 | InternalReconciliation Class |
| InternalReconciliationBP | Object | 1 | 5 |  | classes-14.md | 1477 | 16 | InternalReconciliationBP Class |
| InternalReconciliationBPs | Collection | 1 | 5 |  | classes-14.md | 1494 | 15 | InternalReconciliationBPs Class |
| InternalReconciliationOpenTrans | Object | 5 | 5 |  | classes-14.md | 1510 | 20 | InternalReconciliationOpenTrans Class |
| InternalReconciliationOpenTransParams | Object | 7 | 5 |  | classes-14.md | 1531 | 22 | InternalReconciliationOpenTransParams Class |
| InternalReconciliationOpenTransRow | Object | 9 | 5 |  | classes-14.md | 1554 | 24 | InternalReconciliationOpenTransRow Class |
| InternalReconciliationOpenTransRows | Collection | 1 | 5 |  | classes-14.md | 1579 | 15 | InternalReconciliationOpenTransRows Class |
| InternalReconciliationParams | Object | 1 | 5 |  | classes-14.md | 1595 | 16 | InternalReconciliationParams Class |
| InternalReconciliationRow | Object | 9 | 5 |  | classes-14.md | 1612 | 24 | InternalReconciliationRow Class |
| InternalReconciliationRows | Collection | 1 | 6 |  | classes-14.md | 1637 | 17 | InternalReconciliationRows Class |
| InternalReconciliationsService | Object | 0 | 9 |  | classes-14.md | 1655 | 24 | InternalReconciliationsService Class |
| IntrastatConfiguration | Object | 14 | 5 |  | classes-14.md | 1680 | 29 | IntrastatConfiguration Class |
| IntrastatConfigurationCollectionParams | Collection | 1 | 5 |  | classes-14.md | 1710 | 15 | IntrastatConfigurationCollectionParams Class |
| IntrastatConfigurationParams | Object | 6 | 5 |  | classes-14.md | 1726 | 21 | IntrastatConfigurationParams Class |
| IntrastatConfigurationService | Object | 0 | 8 |  | classes-14.md | 1748 | 21 | IntrastatConfigurationService Class |
| InventoryCounting | Object | 22 | 5 | OINC | classes-14.md | 1770 | 43 | You can use this object to specify items for inventory counting and record the counting results. |
| InventoryCountingBatchNumber | Object | 16 | 5 | BTNT1 | classes-14.md | 1814 | 33 | InventoryCountingBatchNumber is a child object of the InventoryCountingLine object and enables you to count inventory by batch number. |
| InventoryCountingBatchNumbers | Collection | 1 | 6 |  | classes-14.md | 1848 | 20 | A collection of InventoryCountingBatchNumber objects. |
| InventoryCountingDocumentReference | Object | 8 | 5 |  | classes-14.md | 1869 | 23 | InventoryCountingDocumentReference Class |
| InventoryCountingDocumentReferences | Collection | 1 | 6 |  | classes-14.md | 1893 | 17 | InventoryCountingDocumentReferences Class |
| InventoryCountingLine | Object | 39 | 5 | INC1V, INC1 | classes-14.md | 1911 | 59 | InventoryCountingLine is a child object of the InventoryCounting object and represents the line entries of the inventory counting transaction. |
| InventoryCountingLines | Collection | 1 | 6 |  | classes-14.md | 1971 | 20 | A collection of InventoryCountingLine objects. |
| InventoryCountingLineUoM | Object | 12 | 5 | INC2V, INC2 | classes-14.md | 1992 | 29 | InventoryCountingLineUoM is a child object of the InventoryCountingLine object and enables you to count inventory by unit of measure (UoM). |
| InventoryCountingLineUoMs | Collection | 1 | 6 |  | classes-14.md | 2022 | 19 | A collection of InventoryCountingLineUoM objects. |
| InventoryCountingParams | Object | 2 | 5 |  | classes-14.md | 2042 | 19 | Holds the key to an existing inventory counting transaction. |
| InventoryCountingParamsCollection | Collection | 1 | 5 |  | classes-14.md | 2062 | 18 | A collection of InventoryCountingParams objects. |
| InventoryCountingSerialNumber | Object | 19 | 5 | SRNT1 | classes-14.md | 2081 | 36 | InventoryCountingSerialNumber is a child object of the InventoryCountingLine object and enables you to count inventory by serial number. |
| InventoryCountingSerialNumbers | Collection | 1 | 6 |  | classes-14.md | 2118 | 18 | A collection of InventoryCountingSerialNumber objects. |
| InventoryCountingsService | Object | 0 | 8 | OINC | classes-14.md | 2137 | 46 | The InventoryCountingsService service enables you to add, look up, update, and close inventory counting transactions. |
| InventoryCycles | Object | 24 | 7 | OCYC | classes-15.md | 3 | 82 | The InventoryCycles object enables to setup cycles of inventory counts and order intervals. |
| InventoryOpeningBalance | Object | 17 | 5 |  | classes-15.md | 86 | 34 | InventoryOpeningBalance Class |
| InventoryOpeningBalanceBatchNumber | Object | 13 | 5 |  | classes-15.md | 121 | 30 | InventoryOpeningBalanceBatchNumber Class |
| InventoryOpeningBalanceBatchNumbers | Collection | 1 | 5 |  | classes-15.md | 152 | 18 | InventoryOpeningBalanceBatchNumbers Class |
| InventoryOpeningBalanceCCDNumber | Object | 9 | 5 |  | classes-15.md | 171 | 24 | InventoryOpeningBalanceCCDNumber Class |
| InventoryOpeningBalanceCCDNumbers | Collection | 1 | 5 |  | classes-15.md | 196 | 15 | InventoryOpeningBalanceCCDNumbers Class |
| InventoryOpeningBalanceLine | Object | 32 | 5 |  | classes-15.md | 212 | 49 | InventoryOpeningBalanceLine Class |
| InventoryOpeningBalanceLines | Collection | 1 | 5 |  | classes-15.md | 262 | 18 | InventoryOpeningBalanceLines Class |
| InventoryOpeningBalanceParams | Object | 2 | 5 |  | classes-15.md | 281 | 19 | InventoryOpeningBalanceParams Class |
| InventoryOpeningBalanceParamsCollection | Collection | 1 | 5 |  | classes-15.md | 301 | 18 | InventoryOpeningBalanceParamsCollection Class |
| InventoryOpeningBalanceSerialNumber | Object | 16 | 5 |  | classes-15.md | 320 | 33 | InventoryOpeningBalanceSerialNumber Class |
| InventoryOpeningBalanceSerialNumbers | Collection | 1 | 5 |  | classes-15.md | 354 | 18 | InventoryOpeningBalanceSerialNumbers Class |
| InventoryOpeningBalancesService | Object | 0 | 7 |  | classes-15.md | 373 | 19 | InventoryOpeningBalancesService Class |
| InventoryPosting | Object | 20 | 5 | OIQR | classes-15.md | 393 | 37 | If there are differences between the inventory counting results and the item quantities recorded in SAP Business One, you may need to reconcile the quantities so as not to distort your inventory valuation results. |
| InventoryPostingBatchNumber | Object | 13 | 5 | BTNT | classes-15.md | 431 | 30 | InventoryPostingBatchNumber is a child object of the IInventoryPostingLine object. |
| InventoryPostingBatchNumbers | Collection | 1 | 5 |  | classes-15.md | 462 | 18 | A collection of InventoryPostingBatchNumber objects. |
| InventoryPostingCCDNumber | Object | 9 | 5 |  | classes-15.md | 481 | 24 | InventoryPostingCCDNumber Class |
| InventoryPostingCCDNumbers | Collection | 1 | 5 |  | classes-15.md | 506 | 15 | InventoryPostingCCDNumbers Class |
| InventoryPostingCopyOption | Object | 2 | 5 |  | classes-15.md | 522 | 19 | InventoryPostingCopyOption Class |
| InventoryPostingDocumentReference | Object | 8 | 5 |  | classes-15.md | 542 | 23 | InventoryPostingDocumentReference Class |
| InventoryPostingDocumentReferences | Collection | 1 | 6 |  | classes-15.md | 566 | 17 | InventoryPostingDocumentReferences Class |
| InventoryPostingLine | Object | 45 | 5 | IQR1 | classes-15.md | 584 | 64 | InventoryPostingLine is a child object of the InventoryPosting object and represents the line entries of the inventory posting transaction. |
| InventoryPostingLines | Collection | 1 | 5 |  | classes-15.md | 649 | 18 | A collection of InventoryPostingLine objects. |
| InventoryPostingLineUoM | Object | 9 | 5 | IQR2 | classes-15.md | 668 | 26 | InventoryPostingLineUoM is a child object of the InventoryPostingLine object and enables you to specify the unit of measure (UoM) information for the items you want to post. |
| InventoryPostingLineUoMs | Collection | 1 | 5 |  | classes-15.md | 695 | 18 | A collection of InventoryPostingLineUoM objects. |
| InventoryPostingParams | Object | 2 | 5 |  | classes-15.md | 714 | 19 | Holds the key to an existing inventory posting transaction. |
| InventoryPostingParamsCollection | Collection | 1 | 5 |  | classes-15.md | 734 | 18 | A collection of InventoryPostingParams objects. |
| InventoryPostingSerialNumber | Object | 16 | 5 | SRNT | classes-15.md | 753 | 33 | InventoryPostingSerialNumber is a child object of the IInventoryPostingLine object. |
| InventoryPostingSerialNumbers | Collection | 1 | 5 |  | classes-15.md | 787 | 18 | A collection of InventoryPostingSerialNumber objects. |
| InventoryPostingsService | Object | 0 | 8 | OIQR | classes-15.md | 806 | 70 | The InventoryPostingsService service enables you to add, look up, and update inventory posting transactions. |
| InvokeParams | Object | 1 | 0 |  | classes-15.md | 877 | 6 | Holds a single string value. |
| ItemBarCodes | Object | 5 | 3 |  | classes-15.md | 884 | 16 | ItemBarCodes Class |
| ItemCycleCount | Object | 8 | 0 | ITW1 | classes-15.md | 901 | 47 | ItemCycleCount object hold the information when an item will go through cycle counting. |
| ItemGroups | Object | 66 | 7 | OITB | classes-15.md | 949 | 135 | ItemGroups is a business object that represents the item groups definition in the Inventory and Production module. |
| ItemGroups_WarehouseInfo | Object | 5 | 2 | OIGW | classes-15.md | 1085 | 17 | ItemGroups_WarehouseInfo is a child object of the ItemGroups object that represents the items in the warehouse. |
| ItemIntrastatExtension | Object | 20 | 0 |  | classes-15.md | 1103 | 25 | ItemIntrastatExtension Class |
| ItemLocalizationInfos | Object | 3 | 3 |  | classes-15.md | 1129 | 14 | ItemLocalizationInfos Class |
| ItemPriceParams | Object | 10 | 5 |  | classes-15.md | 1144 | 27 | The item |
| ItemPriceReturnParams | Object | 3 | 5 |  | classes-15.md | 1172 | 20 | Returns the item price. |
| ItemProperties | Object | 4 | 5 | OITG | classes-15.md | 1193 | 57 | The ItemProperties object enables to update the property names that can be used for sorting or grouping items in reports. |
| Items | Object | 223 | 10 | OITM | classes-15.md | 1251 | 375 | Items is a business object that represents the items master data in the Inventory and Production module. |
| Items_PreferredVendors | Object | 3 | 3 | ITM2 | classes-15.md | 1627 | 76 | Items_PreferredVendors is a child object of the Items object that represents the preferred vendor for the item. |
| Items_Prices | Object | 13 | 1 | ITM1 | classes-15.md | 1704 | 91 | Items_Prices is a child object of the Items object that represents the items' prices in the Inventory and Production module. |
| ItemsAttributeGroups | Object | 65 | 3 | ITM13 | classes-16.md | 3 | 140 | ItemsAttributeGroups is a child object of the Items object. |
| ItemsDepreciationParameters | Object | 11 | 2 | ITM7 | classes-16.md | 144 | 25 | ItemsDepreciationParameters is a child object of the Items object. |
| ItemsDistributionRules | Object | 9 | 3 | ITM6 | classes-16.md | 170 | 84 | ItemsDistributionRules is a child object of the Items object. |
| ItemsPeriodControls | Object | 7 | 2 | ITM11 | classes-16.md | 255 | 21 | ItemsPeriodControls is a child object of the Items object. |
| ItemsProjects | Object | 5 | 3 | ITM5 | classes-16.md | 277 | 81 | ItemsProjects is a child object of the Items object. |
| ItemUnitOfMeasurements | Object | 24 | 3 | ITM12 | classes-16.md | 359 | 97 | Unit of measurement for the item. |
| ItemUoMPackages | Object | 23 | 3 | ITM4 | classes-16.md | 457 | 96 | The item UoM package. |
| ItemWarehouseInfo | Object | 66 | 3 | OITW | classes-16.md | 554 | 102 | ItemWarehouseInfo is a child object of the Items object that represents the items in the warehouse. |
| JournalEntries | Object | 62 | 10 | OJDT | classes-16.md | 657 | 132 | JournalEntries is a business object that represents the journal transactions in the Finance module. |
| JournalEntries_Lines | Object | 67 | 2 | JDT1 | classes-16.md | 790 | 91 | Journal_Entries_Lines is a child object of the JournalEntries object, and represents the line entries of each transaction. |
| JournalEntryDocumentType | Object | 3 | 5 |  | classes-16.md | 882 | 18 | JournalEntryDocumentType Class |
| JournalEntryDocumentTypeParams | Object | 3 | 5 |  | classes-16.md | 901 | 18 | JournalEntryDocumentTypeParams Class |
| JournalEntryDocumentTypeParamsCollection | Collection | 1 | 5 |  | classes-16.md | 920 | 15 | JournalEntryDocumentTypeParamsCollection Class |
| JournalEntryDocumentTypeService | Object | 0 | 8 |  | classes-16.md | 936 | 21 | JournalEntryDocumentTypeService Class |
| JournalVouchers | Object | 1 | 3 | OBTD | classes-16.md | 958 | 15 | JournalVouchers is a business object that represents the journal vouchers in the Finance module. |
| KnowledgeBaseSolutions | Object | 16 | 8 | OSLT | classes-16.md | 974 | 78 | KnowledgeBaseSolutions is a business object that represents the knowledge base solutions in the Service module. |
| KPI | Object | 5 | 5 | OKPI | classes-16.md | 1053 | 22 | A KPI set is a parameter set that you can define or modify parameters for dashboards. |
| KPI_ItemLine | Object | 33 | 5 | KPI1 | classes-16.md | 1076 | 50 | KPI_ItemLine is a child object of the KPI object and represents the line entries of a parameter set. |
| KPI_ItemLines | Collection | 1 | 5 |  | classes-16.md | 1127 | 17 | A collection of KPI_ItemLine objects. |
| KPIParams | Object | 2 | 5 |  | classes-16.md | 1145 | 19 | Holds the key to an existing parameter set. |
| KPIsParams | Collection | 1 | 5 |  | classes-16.md | 1165 | 18 | A collection of KPIParams objects. |
| KPIsService | Object | 0 | 8 | OKPI | classes-16.md | 1184 | 70 | The KPIsService service enables you to add, look up, update, and remove dashboard parameters. |
| LandedCost | Object | 40 | 5 | OIPF | classes-16.md | 1255 | 62 | Represents a landed costs document, which is used for recording and allocating the costs incurred when importing goods. |
| LandedCost_CostLine | Object | 14 | 5 | IPF2 | classes-16.md | 1318 | 34 | The LandedCost_CostLine object enables you to allocate landed costs to the various items according to specific criteria, for example volume, weight, or quantity. |
| LandedCost_CostLines | Collection | 1 | 5 |  | classes-16.md | 1353 | 18 | A collection of LandedCost_CostLine objects. |
| LandedCost_ItemLine | Object | 80 | 5 | IPF1 | classes-16.md | 1372 | 106 | The LandedCost_ItemLine object enables you to display the data regarding the imported goods as copied from goods receipt PO documents. |
| LandedCost_ItemLines | Collection | 1 | 6 |  | classes-16.md | 1479 | 20 | A collection of LandedCost_ItemLine objects. |
| LandedCostParams | Object | 1 | 5 |  | classes-16.md | 1500 | 18 | Holds the key to an existing landed costs document. |
| LandedCostsCodes | Object | 6 | 6 | OALC | classes-16.md | 1519 | 61 | The LandedCostsCodes object enables to define codes for landed costs and their distribution type. |
| LandedCostsParams | Collection | 1 | 5 |  | classes-16.md | 1581 | 17 | A collection of LandedCostParams objects. |
| LandedCostsService | Object | 0 | 9 | OIPF | classes-16.md | 1599 | 72 | The LandedCostsService service enables you to add, look up, update, cancel, and close landed costs documents. |
| Layer | Object | 7 | 5 |  | classes-16.md | 1672 | 26 | Represents a FIFO layer for a specific item and location. |
| Layers | Collection | 1 | 5 |  | classes-16.md | 1699 | 17 | A collection of Layer objects that represent the FIFO layers for a specific item. |
| LegalData | Object | 15 | 5 |  | classes-16.md | 1717 | 30 | LegalData Class |
| LegalDataDetail | Object | 6 | 5 |  | classes-16.md | 1748 | 21 | LegalDataDetail Class |
| LegalDataDetailCollection | Collection | 1 | 5 |  | classes-16.md | 1770 | 15 | LegalDataDetailCollection Class |
| LegalDataParams | Object | 3 | 5 |  | classes-16.md | 1786 | 18 | LegalDataParams Class |
| LegalDataParamsCollection | Collection | 1 | 5 |  | classes-16.md | 1805 | 15 | LegalDataParamsCollection Class |
| LegalDataService | Object | 0 | 6 |  | classes-16.md | 1821 | 18 | LegalDataService Class |
| LengthMeasures | Object | 7 | 7 | OLGT | classes-17.md | 3 | 64 | The LengthMeasures object enables to define the length and width measure units that are used for item records. |
| LocalEra | Object | 5 | 4 | OJPE | classes-17.md | 68 | 25 | LocalEra is a business object that represents the Local Era. |
| Manufacturers | Object | 4 | 7 | OMRC | classes-17.md | 94 | 61 | The Manufacturers object enables to define manufacturers used in the Item master data. |
| MaterialGroup | Object | 3 | 5 | OMGP | classes-17.md | 156 | 22 | Represents a material group, which is used for the automatic tax code determination for materials. |
| MaterialGroupParams | Object | 2 | 5 |  | classes-17.md | 179 | 19 | Holds the key and name to an existing material group. |
| MaterialGroupsParams | Collection | 1 | 5 |  | classes-17.md | 199 | 18 | A collection of MaterialGroupParams objects. |
| MaterialGroupsService | Object | 0 | 8 | OMGP | classes-17.md | 218 | 70 | The MaterialGroupsService service enables you to add, look up, update, and remove material groups. |
| MaterialRevaluation | Object | 25 | 9 | OMRV | classes-17.md | 289 | 62 | MaterialRevaluation is a business object that enables you to update the items' price (average price or standard price only), revaluate the stock, and create journal entries accordingly. |
| MaterialRevaluation_lines | Object | 23 | 2 | MRV1 | classes-17.md | 352 | 35 | MaterialRevaluation_Lines is a child object of the MaterialRevaluation object representing the line entries of each transaction. |
| MaterialRevaluationDocumentReferences | Object | 9 | 3 |  | classes-17.md | 388 | 20 | MaterialRevaluationDocumentReferences Class |
| MaterialRevaluationFIFO | Object | 1 | 5 |  | classes-17.md | 409 | 18 | A specific item's FIFO layers. |
| MaterialRevaluationFIFOParams | Object | 4 | 5 |  | classes-17.md | 428 | 21 | Contains parameters for retrieving FIFO layers using the MaterialRevaluationFIFOService service. |
| MaterialRevaluationFIFOService | Object | 0 | 4 |  | classes-17.md | 450 | 125 | The MaterialRevaluationFIFOService service enables you to retrieve the FIFO layers for a specific item and location. |
| MaterialRevaluationSNBParam | Object | 1 | 5 |  | classes-17.md | 576 | 16 | MaterialRevaluationSNBParam Class |
| MaterialRevaluationSNBParams | Object | 8 | 5 |  | classes-17.md | 593 | 23 | MaterialRevaluationSNBParams Class |
| MaterialRevaluationSNBParamsCollection | Collection | 1 | 5 |  | classes-17.md | 617 | 15 | MaterialRevaluationSNBParamsCollection Class |
| MaterialRevaluationSNBService | Object | 0 | 5 |  | classes-17.md | 633 | 16 | MaterialRevaluationSNBService Class |
| Message | Object | 7 | 5 | OALR | classes-17.md | 650 | 24 | Message is a data structure related to the MessagesService. |
| MessageDataColumn | Object | 3 | 5 | ALR2 | classes-17.md | 675 | 20 | MessageDataColumn is a data structure related to the MessagesService. |
| MessageDataColumns | Collection | 1 | 5 |  | classes-17.md | 696 | 15 | MessageDataColumns is a collection of MessageDataColumn data stractures. |
| MessageDataLine | Object | 3 | 5 | ALR3 | classes-17.md | 712 | 18 | The MessageDataLine is a child data structure related to the MessageDataColumn. |
| MessageDataLines | Collection | 1 | 5 |  | classes-17.md | 731 | 15 | MessageDataLines is a collection of the MessageDataLine data structures. |
| MessageHeader | Object | 7 | 5 |  | classes-17.md | 747 | 22 | MessageHeader is a data structure related to the MessagesService. |
| MessageHeaders | Collection | 1 | 5 |  | classes-17.md | 770 | 15 | MessageHeaders is a collection of MessageHeader. |
| Messages | Object | 6 | 2 | OALR | classes-17.md | 786 | 23 | Messages is a business object that represents the messages in the Administration module. |
| MessagesService | Object | 0 | 8 |  | classes-17.md | 810 | 363 | This service enables to manage the Inbox and Outbox messages, and to send messages. |
| MobileAddOnSetting | Object | 11 | 5 |  | classes-17.md | 1174 | 26 | MobileAddOnSetting Class |
| MobileAddOnSettingParams | Object | 2 | 5 |  | classes-17.md | 1201 | 17 | MobileAddOnSettingParams Class |
| MobileAddOnSettingParamsCollection | Collection | 1 | 5 |  | classes-17.md | 1219 | 15 | MobileAddOnSettingParamsCollection Class |
| MobileAddOnSettingService | Object | 0 | 8 |  | classes-17.md | 1235 | 21 | MobileAddOnSettingService Class |
| MobileAppService | Object | 0 | 17 |  | classes-17.md | 1257 | 40 | MobileAppService Class |
| MobileServerDateTime | Object | 2 | 5 |  | classes-17.md | 1298 | 17 | MobileServerDateTime Class |
| MultiLanguageTranslations | Object | 7 | 7 | OMLT | classes-17.md | 1316 | 65 | The MultiLanguageTranslation object enables to translate alphanumeric data of specified fields in master data objects (such as, BusinessPartners and Items) to foreign languages and then print documents in the translated  |
| MultiplePayment | Object | 6 | 5 | BNK1 | classes-17.md | 1382 | 21 | A data structure related to BankStatementService holding properties for a multiple payment on a bank statement line. |
| MultiplePayments | Collection | 1 | 6 |  | classes-17.md | 1404 | 17 | A data collection of MultiplePayment objects related to the BankStatementService. |
| NatureOfAssessee | Object | 4 | 5 | ONOA | classes-17.md | 1422 | 23 | Represents a type of assessee in order to determine the tax rate for TDS (withholding tax). |
| NatureOfAssesseeParams | Object | 3 | 5 |  | classes-17.md | 1446 | 20 | Holds the key and code to an existing assessee type. |
| NatureOfAssesseesParams | Collection | 1 | 5 |  | classes-17.md | 1467 | 17 | A collection of NatureOfAssesseeParams objects. |
| NatureOfAssesseesService | Object | 0 | 8 | ONOA | classes-17.md | 1485 | 135 | The NatureOfAssesseesService service enables you to add, look up and remove nature of assessees in the nature of assessee master data table. |
| NCMCodeSetup | Object | 4 | 5 | ONCM | classes-17.md | 1621 | 25 | Represents an NCM code that can be assigned to an item. |
| NCMCodeSetupParams | Object | 3 | 5 |  | classes-17.md | 1647 | 20 | Holds the key and name to an existing NCM code. |
| NCMCodeSetupParamsCollection | Collection | 1 | 5 |  | classes-17.md | 1668 | 17 | A collection of NCMCodeSetupParams objects. |
| NCMCodesSetupService | Object | 0 | 8 | ONCM | classes-17.md | 1686 | 121 | The NCMCodesSetupService service enables you to add, look up and remove NCM codes in the NCM codes master data table. |
| NFModel | Object | 4 | 5 |  | classes-17.md | 1808 | 19 | NFModel Class |
| NFModelParams | Object | 4 | 5 |  | classes-17.md | 1828 | 19 | NFModelParams Class |
| NFModelsParams | Collection | 1 | 5 |  | classes-17.md | 1848 | 15 | NFModelsParams Class |
| NFModelsService | Object | 0 | 8 |  | classes-17.md | 1864 | 21 | NFModelsService Class |
| NFTaxCategoriesService | Object | 0 | 8 |  | classes-17.md | 1886 | 21 | NFTaxCategoriesService Class |
| NFTaxCategory | Object | 5 | 5 |  | classes-17.md | 1908 | 20 | NFTaxCategory Class |
| NFTaxCategoryParams | Object | 2 | 5 |  | classes-17.md | 1929 | 17 | NFTaxCategoryParams Class |
| NFTaxCategoryParamsCollection | Collection | 1 | 5 |  | classes-17.md | 1947 | 15 | NFTaxCategoryParamsCollection Class |
| NotaFiscalCFOP | Object | 5 | 7 | OCFP | classes-17.md | 1963 | 32 | Represents CFOP codes for Nota Fiscal documents. |
| NotaFiscalCST | Object | 7 | 7 | OTSC | classes-17.md | 1996 | 34 | Represents CST codes for Nota Fiscal documents. |
| NotaFiscalUsage | Object | 13 | 7 | OUSG | classes-17.md | 2031 | 40 | Represents a usage for specifying tax codes for Nota Fiscal documents. |
| OccurenceCode | Object | 6 | 5 |  | classes-17.md | 2072 | 21 | OccurenceCode Class |
| OccurenceCodeParams | Object | 6 | 5 |  | classes-17.md | 2094 | 21 | OccurenceCodeParams Class |
| OccurenceCodeParamsCollection | Collection | 1 | 5 |  | classes-17.md | 2116 | 15 | OccurenceCodeParamsCollection Class |
| OccurrenceCodesService | Object | 0 | 8 |  | classes-17.md | 2132 | 21 | OccurrenceCodesService Class |
| OpenningBalanceAccount | Object | 6 | 5 |  | classes-17.md | 2154 | 23 | OpenningBalanceAccount is a data structure related to the AccountsService and BusinessPartnersService. |
| OriginalItem | Object | 3 | 5 |  | classes-17.md | 2178 | 18 | A data structure object holding properties fo the AlternativeItemService. |
| OriginalItemParams | Object | 2 | 5 |  | classes-17.md | 2197 | 17 | This object holds identification properties for the AlternativeItemsService (ItemCode and ItemName). |
| PackagesTypes | Object | 22 | 7 | OPKG | classes-17.md | 2215 | 81 | PackagesTypes is a business object that represents the list of package types for deliveries in the Inventory and Production module. |
| PartnersSetup | Object | 5 | 5 | OPRT | classes-17.md | 2297 | 22 | Define partners for sales opportunities. |
| PartnersSetupParams | Object | 5 | 5 |  | classes-17.md | 2320 | 22 | Holds the key to an existing partner. |
| PartnersSetupsParams | Collection | 1 | 5 |  | classes-17.md | 2343 | 18 | A collection of PartnersSetupParams objects. |
| PartnersSetupsService | Object | 0 | 8 | OPRT | classes-18.md | 3 | 70 | The PartnersSetupsService service enables you to add, look up, update, and remove partners. |
| PathAdmin | Object | 5 | 5 | OADP | classes-18.md | 74 | 41 | An object for setting and getting directory paths for storing various files. |
| PaymentAmountParams | Object | 10 | 5 |  | classes-18.md | 116 | 25 | PaymentAmountParams Class |
| PaymentAmountParamsCollection | Collection | 1 | 5 |  | classes-18.md | 142 | 15 | PaymentAmountParamsCollection Class |
| PaymentBlock | Object | 2 | 5 | OPYB | classes-18.md | 158 | 21 | Represents the payment blocks. |
| PaymentBlockParams | Object | 2 | 5 |  | classes-18.md | 180 | 19 | Holds the key and name to an existing payment block. |
| PaymentBlocksParams | Collection | 1 | 5 |  | classes-18.md | 200 | 18 | A collection of PaymentBlockParams objects. |
| PaymentBlocksService | Object | 0 | 8 | OPYB | classes-18.md | 219 | 70 | The PaymentBlocksService service enables you to add, look up, update, and remove payment blocks. |
| PaymentBPCode | Object | 2 | 5 |  | classes-18.md | 290 | 17 | PaymentBPCode Class |
| PaymentCalculationService | Object | 0 | 4 |  | classes-18.md | 308 | 15 | PaymentCalculationService Class |
| PaymentInvoiceEntries | Collection | 1 | 5 |  | classes-18.md | 324 | 15 | PaymentInvoiceEntries Class |
| PaymentInvoiceEntry | Object | 4 | 5 |  | classes-18.md | 340 | 19 | PaymentInvoiceEntry Class |
| PaymentReasonCode | Object | 1 | 5 | OPTR | classes-18.md | 360 | 18 | Source table: OPTR. |
| PaymentReasonCodeParams | Object | 1 | 5 |  | classes-18.md | 379 | 18 | PaymentReasonCodeParams Class |
| PaymentReasonCodeService | Object | 0 | 7 | OPTR | classes-18.md | 398 | 21 | Source table: OPTR. |
| PaymentReasonCodesParams | Collection | 1 | 5 |  | classes-18.md | 420 | 18 | PaymentReasonCodesParams Class |
| PaymentRunExport | Object | 97 | 4 | OPEX | classes-18.md | 439 | 153 | PaymentRunExport is a business object that enables you to export data of automatic payments for both incoming payments and outgoing payments to vendors. |
| PaymentRunExport_Lines | Object | 32 | 1 | PEX1 | classes-18.md | 593 | 41 | PaymentRunExport_Lines is a child object of the PaymentRunExport object and represents the line entries of each payment. |
| Payments | Object | 101 | 13 | ORCT | classes-18.md | 635 | 250 | Payments is a business object that represents payment methods in the Banking module. |
| Payments_Accounts | Object | 18 | 2 | RCT4 | classes-18.md | 886 | 34 | Payments_Accounts is a child object of the Payments object and represents the payments through account transfers in the Banking module. |
| Payments_ApprovalRequests | Object | 5 | 1 | OWDDV | classes-18.md | 921 | 14 | Payments_ApprovalRequests is a child object of the Payments object. |
| Payments_Checks | Object | 20 | 2 | RCT1 | classes-18.md | 936 | 35 | Represents checks that are tied to an outgoing payment document. |
| Payments_CreditCards | Object | 20 | 2 | RCT3 | classes-18.md | 972 | 39 | Payments_CreditCards is a child object of the Payments object and represents the payments by credit cards in the Banking module. |
| Payments_DocumentReferences | Object | 9 | 3 |  | classes-18.md | 1012 | 20 | Payments_DocumentReferences Class |
| Payments_Invoices | Object | 24 | 2 | RCT2 | classes-18.md | 1033 | 47 | Payments_Invoices is a child object of the Payments object and represents the invoices related to the payments in the Banking module. |
| PaymentTermsTypes | Object | 18 | 9 | OCTG | classes-18.md | 1081 | 89 | PaymentTermsTypes is a business object that represents the types of payment terms in the Banking module. |
| PeriodCategory | Object | 127 | 5 |  | classes-18.md | 1171 | 147 | The PeriodCategory object is a data structure related to the CompanyService. |
| PeriodCategoryParams | Object | 1 | 5 |  | classes-18.md | 1319 | 16 | The PeriodCategoryParams specifies the identification key (AbsoluteEntry) for which the DocumentSeriesParams service is related. |
| PeriodCategoryParamsCollection | Collection | 1 | 5 |  | classes-18.md | 1336 | 15 | PeriodCategoryParamsCollection is a collection of PeriodCategoryParams identification keys. |
| PickLists | Object | 12 | 9 | OPKL | classes-18.md | 1352 | 37 | The PickLists object supports the picking process of items from the warehouse. |
| PickLists_Lines | Object | 14 | 2 | PKL1 | classes-18.md | 1390 | 29 | The PickLists_Lines is a child object of the PickLists object. |
| PM_ActivitiesCollection | Collection | 1 | 5 |  | classes-18.md | 1420 | 15 | PM_ActivitiesCollection Class |
| PM_ActivityData | Object | 4 | 5 | PMG6 | classes-18.md | 1436 | 19 | Source table: PMG6. |
| PM_DocAttachement | Object | 6 | 5 | OPMG | classes-18.md | 1456 | 21 | Source table: OPMG.AtcEntry. |
| PM_DocAttachements | Collection | 1 | 5 |  | classes-18.md | 1478 | 15 | PM_DocAttachements Class |
| PM_DocumentData | Object | 12 | 5 | PMG4 | classes-19.md | 3 | 27 | Source table: PMG4. |
| PM_DocumentsCollection | Collection | 1 | 5 |  | classes-19.md | 31 | 15 | PM_DocumentsCollection Class |
| PM_OpenIssueData | Object | 12 | 5 | PMG2 | classes-19.md | 47 | 27 | Source table: PMG2. |
| PM_OpenIssuesCollection | Collection | 1 | 5 |  | classes-19.md | 75 | 15 | PM_OpenIssuesCollection Class |
| PM_ProjectDocumentData | Object | 31 | 5 | OPMG | classes-19.md | 91 | 46 | Source table: OPMG. |
| PM_ProjectDocumentParams | Object | 1 | 5 | OPMG | classes-19.md | 138 | 16 | Source table: OPMG.AbsEntry. |
| PM_StageAttachement | Object | 6 | 5 | PMG1 | classes-19.md | 155 | 21 | Source table: PMG1.AtcEntry. |
| PM_StageAttachements | Collection | 1 | 5 |  | classes-19.md | 177 | 15 | PM_StageAttachements Class |
| PM_StageData | Object | 31 | 5 | PMG1 | classes-19.md | 193 | 46 | Source table: PMG1. |
| PM_StagesCollection | Collection | 1 | 5 |  | classes-19.md | 240 | 15 | PM_StagesCollection Class |
| PM_SubprojectDocumentData | Object | 25 | 5 | OPHA | classes-19.md | 256 | 40 | Source table: OPHA. |
| PM_SubprojectDocumentParams | Object | 1 | 5 | OPHA | classes-19.md | 297 | 16 | Source table: OPHA.AbsEntry. |
| PM_SubprojectDocumentsCollection | Collection | 1 | 5 |  | classes-19.md | 314 | 15 | PM_SubprojectDocumentsCollection Class |
| PM_SubprojectParams | Object | 2 | 5 | OPMG/OPHA | classes-19.md | 330 | 17 | Source table: OPMG/OPHA.AbsEntry + IsSubproject. |
| PM_SummaryData | Object | 34 | 5 |  | classes-19.md | 348 | 49 | PM_SummaryData Class |
| PM_TimeSheetData | Object | 14 | 5 |  | classes-19.md | 398 | 29 | PM_TimeSheetData Class |
| PM_TimeSheetLineData | Object | 22 | 5 |  | classes-19.md | 428 | 37 | PM_TimeSheetLineData Class |
| PM_TimeSheetLineDataCollection | Collection | 1 | 6 |  | classes-19.md | 466 | 17 | PM_TimeSheetLineDataCollection Class |
| PM_TimeSheetParams | Object | 1 | 5 |  | classes-19.md | 484 | 16 | PM_TimeSheetParams Class |
| PM_WorkOrderData | Object | 5 | 5 | PMG7 | classes-19.md | 501 | 20 | Source table: PMG7. |
| PM_WorkOrdersCollection | Collection | 1 | 5 |  | classes-19.md | 522 | 15 | PM_WorkOrdersCollection Class |
| PMC_ActivityCollection | Collection | 1 | 5 |  | classes-19.md | 538 | 15 | PMC_ActivityCollection Class |
| PMC_ActivityData | Object | 5 | 5 |  | classes-19.md | 554 | 20 | PMC_ActivityData Class |
| PMC_AreaCollection | Collection | 1 | 5 |  | classes-19.md | 575 | 15 | PMC_AreaCollection Class |
| PMC_AreaData | Object | 2 | 5 |  | classes-19.md | 591 | 17 | PMC_AreaData Class |
| PMC_PriorityCollection | Collection | 1 | 5 |  | classes-19.md | 609 | 15 | PMC_PriorityCollection Class |
| PMC_PriorityData | Object | 2 | 5 |  | classes-19.md | 625 | 17 | PMC_PriorityData Class |
| PMC_StageTypeCollection | Collection | 1 | 5 |  | classes-19.md | 643 | 15 | PMC_StageTypeCollection Class |
| PMC_StageTypeData | Object | 3 | 5 |  | classes-19.md | 659 | 18 | PMC_StageTypeData Class |
| PMC_SubprojectTypeData | Object | 2 | 5 |  | classes-19.md | 678 | 17 | PMC_SubprojectTypeData Class |
| PMC_SubprojectTypesCollection | Collection | 1 | 5 |  | classes-19.md | 696 | 15 | PMC_SubprojectTypesCollection Class |
| PMC_TaskCollection | Collection | 1 | 5 |  | classes-19.md | 712 | 15 | PMC_TaskCollection Class |
| PMC_TaskData | Object | 2 | 5 |  | classes-19.md | 728 | 17 | PMC_TaskData Class |
| PMS_ActivitiesCollection | Collection | 1 | 5 |  | classes-19.md | 746 | 15 | PMS_ActivitiesCollection Class |
| PMS_ActivityData | Object | 4 | 5 | PHA6 | classes-19.md | 762 | 19 | Source table: PHA6. |
| PMS_DocAttachement | Object | 6 | 5 | OPHA | classes-19.md | 782 | 21 | Source table: OPHA.AtcEntry. |
| PMS_DocAttachements | Collection | 1 | 5 |  | classes-19.md | 804 | 15 | PMS_DocAttachements Class |
| PMS_DocumentData | Object | 12 | 5 | PHA4 | classes-19.md | 820 | 27 | Source table: PHA4. |
| PMS_DocumentsCollection | Collection | 1 | 5 |  | classes-19.md | 848 | 15 | PMS_DocumentsCollection Class |
| PMS_OpenIssueData | Object | 12 | 5 | PHA2 | classes-19.md | 864 | 27 | Source table: PHA2. |
| PMS_OpenIssuesCollection | Collection | 1 | 5 |  | classes-19.md | 892 | 15 | PMS_OpenIssuesCollection Class |
| PMS_StageAttachement | Object | 6 | 5 | PHA1 | classes-19.md | 908 | 21 | Source table: PHA1.AtcEntry. |
| PMS_StageAttachements | Collection | 1 | 5 |  | classes-19.md | 930 | 15 | PMS_StageAttachements Class |
| PMS_StageData | Object | 31 | 5 | PHA1 | classes-19.md | 946 | 46 | Source table: PHA1. |
| PMS_StagesCollection | Collection | 1 | 5 |  | classes-19.md | 993 | 15 | PMS_StagesCollection Class |
| PMS_SummaryData | Object | 34 | 5 | PHA8 | classes-19.md | 1009 | 49 | Source table: PHA8. |
| PMS_WorkOrderData | Object | 5 | 5 | PHA7 | classes-19.md | 1059 | 20 | Source table: PHA7. |
| PMS_WorkOrdersCollection | Collection | 1 | 5 |  | classes-19.md | 1080 | 15 | PMS_WorkOrdersCollection Class |
| POSDailySummary | Object | 11 | 5 |  | classes-19.md | 1096 | 26 | POSDailySummary Class |
| POSDailySummaryParams | Object | 1 | 5 |  | classes-19.md | 1123 | 16 | POSDailySummaryParams Class |
| POSDailySummaryService | Object | 0 | 7 |  | classes-19.md | 1140 | 20 | POSDailySummaryService Class |
| PostingTemplates | Object | 7 | 5 |  | classes-19.md | 1161 | 22 | PostingTemplates Class |
| PostingTemplatesLine | Object | 21 | 5 |  | classes-19.md | 1184 | 36 | PostingTemplatesLine Class |
| PostingTemplatesLineCollection | Collection | 1 | 6 |  | classes-19.md | 1221 | 17 | PostingTemplatesLineCollection Class |
| PostingTemplatesParams | Object | 2 | 5 |  | classes-19.md | 1239 | 17 | PostingTemplatesParams Class |
| PostingTemplatesParamsCollection | Collection | 1 | 5 |  | classes-19.md | 1257 | 15 | PostingTemplatesParamsCollection Class |
| PostingTemplatesService | Object | 0 | 8 |  | classes-19.md | 1273 | 21 | PostingTemplatesService Class |
| POSTotalizer | Object | 5 | 5 |  | classes-19.md | 1295 | 20 | POSTotalizer Class |
| POSTotalizerCollection | Collection | 1 | 6 |  | classes-19.md | 1316 | 17 | POSTotalizerCollection Class |
| PredefinedText | Object | 3 | 5 | OPDT | classes-19.md | 1334 | 20 | Represents a predefined text. |
| PredefinedTextParams | Object | 2 | 5 |  | classes-19.md | 1355 | 19 | Holds the key and name to an existing predefined text. |
| PredefinedTextsParams | Collection | 1 | 5 |  | classes-19.md | 1375 | 17 | A collection of PredefinedTextParams objects. |
| PredefinedTextsService | Object | 0 | 8 | OPDT | classes-19.md | 1393 | 85 | The PredefinedTextsService service enables you to add, look up and remove predefined texts in the predefined texts master data table. |
| PriceLists | Object | 19 | 7 | OPLN | classes-19.md | 1479 | 48 | PriceLists is a business object that represents the management of price lists in the Inventory module. |
| ProductionOrders | Object | 45 | 7 | OWOR | classes-19.md | 1528 | 109 | The ProductionOrders object supports the creation and maintenance of production orders. |
| ProductionOrders_DocumentReferences | Object | 9 | 3 |  | classes-19.md | 1638 | 20 | ProductionOrders_DocumentReferences Class |
| ProductionOrders_Lines | Object | 32 | 3 | WOR1 | classes-19.md | 1659 | 64 | The ProductionOrders_Lines is a child object of the ProductionOrders object. |
| ProductionOrders_SalesOrderLines | Object | 5 | 1 | WOR2 | classes-19.md | 1724 | 17 | The ProductionOrders_SalesOrderLines is a child object of the ProductionOrders object. |
| ProductionOrders_Stages | Object | 11 | 3 | WOR4 | classes-19.md | 1742 | 84 | The ProductionOrders_Stages is a child object of the ProductionOrders object. |
| ProductTrees | Object | 18 | 10 | OITT | classes-19.md | 1827 | 124 | ProductTrees is a business object that represents a completed product comprising parts and raw materials, which is described by means of a bill of materials. |
| ProductTrees_Lines | Object | 26 | 3 | ITT1 | classes-19.md | 1952 | 59 | ProductTrees_Lines is a child object of the ProductTrees object and it represents the line entries of each product tree. |
| ProductTrees_Stages | Object | 7 | 3 |  | classes-19.md | 2012 | 79 | ProductTrees_Stages Class |
| ProfitCenter | Object | 10 | 5 | OPRC | classes-19.md | 2092 | 32 | Represents a profit center. |
| ProfitCenterParams | Object | 2 | 5 |  | classes-19.md | 2125 | 19 | Holds the key and name to an existing profit center. |
| ProfitCentersParams | Collection | 1 | 5 |  | classes-19.md | 2145 | 17 | A collection of ProfitCenterParams objects. |
| ProfitCentersService | Object | 0 | 8 | OPRC | classes-19.md | 2163 | 120 | The ProfitCentersService service enables you to add, look up and remove profit centers. |
| Project | Object | 6 | 5 | OPRJ | classes-19.md | 2284 | 21 | A data structure object holding properties for the ProjectsService (Code and Name). |
| ProjectManagementConfigurationService | Object | 0 | 27 |  | classes-19.md | 2306 | 54 | ProjectManagementConfigurationService Class |
| ProjectManagementService | Object | 0 | 12 | OPMG | classes-20.md | 3 | 260 | This service is for project management in SAP Business One. |
| ProjectManagementTimeSheetService | Object | 0 | 7 |  | classes-20.md | 264 | 20 | ProjectManagementTimeSheetService Class |
| ProjectParams | Object | 2 | 5 |  | classes-20.md | 285 | 17 | This object holds identification properties for the ProjectsService object (Code and Name). |
| ProjectsParams | Collection | 1 | 5 |  | classes-20.md | 303 | 15 | A data collection of ProjectParams identification properties. |
| ProjectsService | Object | 0 | 8 | OPRJ | classes-20.md | 319 | 139 | This service manages projects in SAP Business One. |
| QRCodeCollection | Collection | 1 | 5 |  | classes-20.md | 459 | 15 | QRCodeCollection Class |
| QRCodeData | Object | 4 | 5 |  | classes-20.md | 475 | 19 | QRCodeData Class |
| QRCodeService | Object | 0 | 4 |  | classes-20.md | 495 | 14 | QRCodeService Class |
| QueryAuthGroup | Object | 4 | 5 |  | classes-20.md | 510 | 19 | QueryAuthGroup Class |
| QueryAuthGroupCollection | Collection | 1 | 5 |  | classes-20.md | 530 | 15 | QueryAuthGroupCollection Class |
| QueryAuthGroupParams | Object | 2 | 5 |  | classes-20.md | 546 | 17 | QueryAuthGroupParams Class |
| QueryAuthGroupService | Object | 0 | 8 |  | classes-20.md | 564 | 21 | QueryAuthGroupService Class |
| QueryCategories | Object | 5 | 6 | OQCN | classes-20.md | 586 | 60 | QueryCategories is a business object that represents the query categories in the Queries Manager. |
| Queue | Object | 8 | 7 | OQUE | classes-20.md | 647 | 66 | Queue is a business object that represents the queues list in the Service module from which you can assign a queue member to a service call. |
| QueueMembers | Object | 4 | 2 | QUE1 | classes-20.md | 714 | 17 | QueueMembers is a child object of Queue object and represents SAP Business One users that are members of the queue. |
| RclRecurringExecutionParams | Object | 1 | 5 |  | classes-20.md | 732 | 16 | RclRecurringExecutionParams Class |
| RclRecurringTransaction | Object | 7 | 5 |  | classes-20.md | 749 | 22 | RclRecurringTransaction Class |
| RclRecurringTransactionCollection | Collection | 1 | 5 |  | classes-20.md | 772 | 15 | RclRecurringTransactionCollection Class |
| RclRecurringTransactionParams | Object | 2 | 5 |  | classes-20.md | 788 | 17 | RclRecurringTransactionParams Class |
| RclRecurringTransactionParamsCollection | Collection | 1 | 5 |  | classes-20.md | 806 | 15 | RclRecurringTransactionParamsCollection Class |
| Recipient | Object | 10 | 5 | AOB1 | classes-20.md | 822 | 25 | Recipient is a data structure related to the MessagesService. |
| RecipientCollection | Collection | 1 | 5 |  | classes-20.md | 848 | 15 | RecipientCollection is a collection of Recipient data structures. |
| Recipients | Object | 11 | 2 | AOB1 | classes-20.md | 864 | 25 | Recipients is a business object that represents the recipients' list of a message or alert. |
| ReconciliationBankStatementLine | Object | 6 | 5 | OBNK | classes-20.md | 890 | 23 | Represents open transactions to be reconciled in external bank statement. |
| ReconciliationBankStatementLines | Collection | 1 | 5 |  | classes-20.md | 914 | 18 | A collection of ReconciliationBankStatementLine objects. |
| ReconciliationJournalEntryLine | Object | 10 | 5 | JDT1 | classes-20.md | 933 | 27 | Represents open transactions to be reconciled in journal entry. |
| ReconciliationJournalEntryLines | Collection | 1 | 5 |  | classes-20.md | 961 | 18 | A collection of ReconciliationJournalEntryLine objects. |
| Recordset | Object | 6 | 10 |  | classes-20.md | 980 | 97 | Recordset is a raw data access object that enables you to select data from the database, navigate through the result set, and manipulate user tables, which are not exposed by the DI API. |
| RecordsetEx | Object | 3 | 4 |  | classes-20.md | 1078 | 56 | RecordsetEx is a raw data access object that enables you to fetch data from the database table. |
| RecurringPostings | Object | 19 | 5 |  | classes-20.md | 1135 | 34 | RecurringPostings Class |
| RecurringPostingsDocumentReference | Object | 8 | 5 |  | classes-20.md | 1170 | 23 | RecurringPostingsDocumentReference Class |
| RecurringPostingsDocumentReferenceCollection | Collection | 1 | 6 |  | classes-20.md | 1194 | 17 | RecurringPostingsDocumentReferenceCollection Class |
| RecurringPostingsLine | Object | 22 | 5 |  | classes-20.md | 1212 | 37 | RecurringPostingsLine Class |
| RecurringPostingsLineCollection | Collection | 1 | 6 |  | classes-20.md | 1250 | 17 | RecurringPostingsLineCollection Class |
| RecurringPostingsParams | Object | 3 | 5 |  | classes-20.md | 1268 | 18 | RecurringPostingsParams Class |
| RecurringPostingsParamsCollection | Collection | 1 | 5 |  | classes-20.md | 1287 | 15 | RecurringPostingsParamsCollection Class |
| RecurringPostingsService | Object | 0 | 8 |  | classes-20.md | 1303 | 21 | RecurringPostingsService Class |
| RecurringTransactionService | Object | 0 | 7 |  | classes-20.md | 1325 | 20 | RecurringTransactionService Class |
| RelatedDocument | Object | 3 | 5 |  | classes-20.md | 1346 | 18 | RelatedDocument Class |
| RelatedDocumentCollection | Collection | 1 | 5 |  | classes-20.md | 1365 | 15 | RelatedDocumentCollection Class |
| RelatedDocuments | Object | 4 | 3 |  | classes-20.md | 1381 | 15 | RelatedDocuments Class |
| Relationships | Object | 4 | 7 | OORL | classes-20.md | 1397 | 63 | Relationships is a business object that represents the relationships list from which a relationship definition can be associated with a partner in a sales opportunity. |
| ReportFilterService | Object | 0 | 8 | OVTR | classes-20.md | 1461 | 122 | The Report Filter Service is a business object that manages the information displaied by tax report. |
| ReportLayout | Object | 48 | 5 | RDOC | classes-20.md | 1584 | 67 | Represents a layout for PLD or a layout/report for Crystal Reports. |
| ReportLayout_TranslationLine | Object | 8 | 5 |  | classes-20.md | 1652 | 23 | ReportLayout_TranslationLine Class |
| ReportLayout_TranslationLines | Collection | 1 | 6 |  | classes-20.md | 1676 | 17 | ReportLayout_TranslationLines Class |
| ReportLayoutItem | Object | 69 | 5 | RITM | classes-20.md | 1694 | 87 | Represents an element in a PLD report layout. |
| ReportLayoutItems | Collection | 1 | 5 |  | classes-20.md | 1782 | 18 | A collection of ReportLayoutItem objects. |
| ReportLayoutParams | Object | 3 | 5 |  | classes-20.md | 1801 | 20 | Holds the key, name, and type of report/report layout. |
| ReportLayoutPrintParams | Object | 2 | 5 |  | classes-20.md | 1822 | 17 | ReportLayoutPrintParams Class |
| ReportLayoutsParams | Collection | 1 | 5 |  | classes-20.md | 1840 | 18 | A collection of ReportLayoutParams objects. |
| ReportLayoutsService | Object | 0 | 15 | RDOC | classes-20.md | 1859 | 265 | The ReportLayoutsService service enables you to do the following: - Copy a PLD report layout from one company to another. |
| ReportParams | Object | 3 | 5 |  | classes-20.md | 2125 | 20 | Indicates which reports to retrieve, for example in the GetDefaultReport method of the ReportLayoutsService. |
| ReportType | Object | 6 | 5 | RTYP | classes-20.md | 2146 | 23 | Represent the report type to which a layout is assigned. |
| ReportTypeParams | Object | 5 | 5 |  | classes-20.md | 2170 | 22 | Holds the key to an existing report type. |
| ReportTypesParams | Collection | 1 | 5 |  | classes-20.md | 2193 | 18 | A collection of ReportTypeParams objects. |
| ReportTypesService | Object | 0 | 8 | RTYP | classes-20.md | 2212 | 81 | The ReportTypesService service enables you to add, look up, and delete the report types in SAP Business One. |
| Resource | Object | 110 | 5 | ORSC | classes-21.md | 3 | 158 | A resource is defined as a commodity, machine, labor, or other asset used to produce goods and services. |
| ResourceCapacitiesService | Object | 0 | 8 |  | classes-21.md | 162 | 21 | ResourceCapacitiesService Class |
| ResourceCapacity | Object | 24 | 5 | ORCJ | classes-21.md | 184 | 43 | Source table: ORCJ. |
| ResourceCapacityParams | Object | 24 | 5 |  | classes-21.md | 228 | 41 | ResourceCapacityParams Class |
| ResourceCapacityParamsCollection | Collection | 1 | 5 |  | classes-21.md | 270 | 18 | ResourceCapacityParamsCollection Class |
| ResourceCapacityWithFilterParams | Object | 4 | 5 |  | classes-21.md | 289 | 21 | ResourceCapacityWithFilterParams Class |
| ResourceDailyCapacities | Collection | 1 | 6 |  | classes-21.md | 311 | 20 | A collection of ResourceDailyCapacity objects. |
| ResourceDailyCapacity | Object | 9 | 5 | RSC6 | classes-21.md | 332 | 28 | You can plan daily internal capacity which you can later set as default values in the Resources --> Set Daily Internal Capacity window. |
| ResourceEmployee | Object | 2 | 5 | RSC4 | classes-21.md | 361 | 19 | If the resource type is Labor, you can associate employees with the resource. |
| ResourceEmployees | Collection | 1 | 6 |  | classes-21.md | 381 | 20 | A collection of ResourceEmployee objects. |
| ResourceFixedAsset | Object | 2 | 5 | RSC3 | classes-21.md | 402 | 20 | If the resource type is Machine, you can associate fixed assets with the resource. |
| ResourceFixedAssets | Collection | 1 | 6 |  | classes-21.md | 423 | 20 | A collection of ResourceFixedAsset objects. |
| ResourceGroup | Object | 24 | 5 |  | classes-21.md | 444 | 41 | ResourceGroup Class |
| ResourceGroupParams | Object | 2 | 5 |  | classes-21.md | 486 | 19 | ResourceGroupParams Class |
| ResourceGroupParamsCollection | Collection | 1 | 5 |  | classes-21.md | 506 | 18 | ResourceGroupParamsCollection Class |
| ResourceGroupsService | Object | 0 | 8 |  | classes-21.md | 525 | 21 | ResourceGroupsService Class |
| ResourceParams | Object | 1 | 5 |  | classes-21.md | 547 | 18 | This object is used to pass keys to and retrieve keys from ResourcesService methods. |
| ResourceParamsCollection | Collection | 1 | 5 |  | classes-21.md | 566 | 18 | A collection of ResourceParams objects. |
| ResourcePropertiesService | Object | 0 | 6 |  | classes-21.md | 585 | 17 | ResourcePropertiesService Class |
| ResourceProperty | Object | 2 | 5 | ORSG | classes-21.md | 603 | 19 | Source table: ORSG. |
| ResourcePropertyParams | Object | 2 | 5 |  | classes-21.md | 623 | 19 | ResourcePropertyParams Class |
| ResourcePropertyParamsCollection | Collection | 1 | 5 |  | classes-21.md | 643 | 18 | ResourcePropertyParamsCollection Class |
| ResourcesService | Object | 0 | 9 | ORSC | classes-21.md | 662 | 97 | The ResourcesService service enables you to add, look up, update, and delete resources in SAP Business One. |
| ResourceWarehouse | Object | 4 | 5 | RSC1 | classes-21.md | 760 | 21 | Define warehouses for the resource. |
| ResourceWarehouses | Collection | 1 | 6 |  | classes-21.md | 782 | 20 | A collection of ResourceWarehouse objects. |
| RetornoCode | Object | 8 | 5 |  | classes-21.md | 803 | 23 | RetornoCode Class |
| RetornoCodeParams | Object | 8 | 5 |  | classes-21.md | 827 | 23 | RetornoCodeParams Class |
| RetornoCodeParamsCollection | Collection | 1 | 5 |  | classes-21.md | 851 | 15 | RetornoCodeParamsCollection Class |
| RetornoCodesService | Object | 0 | 8 |  | classes-21.md | 867 | 21 | RetornoCodesService Class |
| RoundedData | Object | 1 | 5 |  | classes-21.md | 889 | 18 | Represents the data after rounding. |
| RouteStage | Object | 6 | 5 |  | classes-21.md | 908 | 23 | RouteStage Class |
| RouteStageParams | Object | 6 | 5 |  | classes-21.md | 932 | 23 | RouteStageParams Class |
| RouteStageParamsCollection | Collection | 1 | 5 |  | classes-21.md | 956 | 17 | RouteStageParamsCollection Class |
| RouteStagesService | Object | 0 | 8 |  | classes-21.md | 974 | 21 | RouteStagesService Class |
| RoutingDateCalculationInput | Object | 9 | 5 |  | classes-21.md | 996 | 26 | RoutingDateCalculationInput Class |
| RoutingDateCalculationOutput | Object | 2 | 5 |  | classes-21.md | 1023 | 19 | RoutingDateCalculationOutput Class |
| RoutingDateCalculationService | Object | 0 | 4 |  | classes-21.md | 1043 | 14 | RoutingDateCalculationService Class |
| SalesAppSetting | Object | 4 | 5 |  | classes-21.md | 1058 | 19 | SalesAppSetting Class |
| SalesAppSettingParams | Object | 2 | 5 |  | classes-21.md | 1078 | 17 | SalesAppSettingParams Class |
| SalesForecast | Object | 9 | 7 | OFCT | classes-21.md | 1096 | 72 | SalesForecast is a business object that represents the sales forecast for a specified period. |
| SalesForecast_Lines | Object | 6 | 3 | FCT1 | classes-21.md | 1169 | 79 | SalesForecast_Lines is a child object of SalesForecast object and represents sales forecast of items and their quantity for a specified day. |
| SalesOpportunities | Object | 55 | 8 | OOPR | classes-21.md | 1249 | 168 | SalesOpportunities is a business object that represents the sales opportunities data in SAP Business One. |
| SalesOpportunitiesCompetition | Object | 8 | 3 | OPR3 | classes-21.md | 1418 | 83 | SalesOpportunityCompetition is a child object of the SalesOpportunities object that represents the competitors of the sales opportunity. |
| SalesOpportunitiesInterests | Object | 6 | 3 | OPR4 | classes-21.md | 1502 | 80 | SalesOpportunitiesInterests is a child object of the SalesOpportunities object and represents the interests range of sales opportunity. |
| SalesOpportunitiesLines | Object | 24 | 2 | OPR1 | classes-21.md | 1583 | 47 | SalesOpportunityLines is a child object of the SalesOpportunities object and represents the stages of the sales opportunity. |
| SalesOpportunitiesPartners | Object | 7 | 3 | OPR2 | classes-21.md | 1631 | 82 | SalesOpportunityPartner is a child object of the SalesOpportunities object that represents the partners of the sales opportunity. |
| SalesOpportunitiesReasons | Object | 5 | 3 | OPR5 | classes-21.md | 1714 | 79 | SalesOpportunitiesReasons is a child object of the SalesOpportunities object and represents the reasons for failures of sales opportunity. |
| SalesOpportunityCompetitorSetup | Object | 4 | 5 | OCMT | classes-21.md | 1794 | 24 | Represents a competitor. |
| SalesOpportunityCompetitorSetupParams | Object | 3 | 5 |  | classes-21.md | 1819 | 20 | Holds the key and name to an existing competitor. |
| SalesOpportunityCompetitorSetupParamsCollection | Collection | 1 | 5 |  | classes-21.md | 1840 | 17 | A collection of SalesOpportunityCompetitorSetup objects. |
| SalesOpportunityCompetitorsSetupService | Object | 0 | 8 | OCMT | classes-21.md | 1858 | 153 | The SalesOpportunityCompetitorsSetupService service enables you to add, look up and remove competitors in the competitors master data table. |
| SalesOpportunityInterestSetup | Object | 3 | 5 | OOIN | classes-21.md | 2012 | 24 | Represents an area of interest for the sales opportunity. |
| SalesOpportunityInterestSetupParams | Object | 2 | 5 |  | classes-21.md | 2037 | 19 | Holds the key and name to an interest. |
| SalesOpportunityInterestSetupParamsCollection | Collection | 1 | 5 |  | classes-21.md | 2057 | 17 | A collection of SalesOpportunityInterestSetupParams objects. |
| SalesOpportunityInterestsSetupService | Object | 0 | 8 | OOIN | classes-22.md | 3 | 139 | The SalesOpportunityInterestsSetupService service enables you to add, look up and remove interests in the interests master data table. |
| SalesOpportunityReasonSetup | Object | 3 | 5 | OOFR | classes-22.md | 143 | 24 | Represents a reason for a successful or unsuccessful sales opportunity. |
| SalesOpportunityReasonSetupParams | Object | 2 | 5 |  | classes-22.md | 168 | 19 | Holds the key and name to an existing reason. |
| SalesOpportunityReasonSetupParamsCollection | Collection | 1 | 5 |  | classes-22.md | 188 | 17 | A collection of SalesOpportunityReasonSetupParams objects. |
| SalesOpportunityReasonsSetupService | Object | 0 | 8 | OOFR | classes-22.md | 206 | 147 | The SalesOpportunityReasonsSetupService service enables you to add, look up and remove reasons in the reasons master data table. |
| SalesOpportunitySourceSetup | Object | 3 | 5 | OOSR | classes-22.md | 354 | 22 | Represents a source from which sales opportunities can be generated. |
| SalesOpportunitySourceSetupParams | Object | 2 | 5 |  | classes-22.md | 377 | 19 | Holds the key and name to a source. |
| SalesOpportunitySourceSetupParamsCollection | Collection | 1 | 5 |  | classes-22.md | 397 | 17 | A collection of SalesOpportunitySourceSetupParams objects. |
| SalesOpportunitySourcesSetupService | Object | 0 | 8 | OOSR | classes-22.md | 415 | 137 | The SalesOpportunitySourcesSetupService service enables you to add, look up and remove sources in the sources master data table. |
| SalesPersons | Object | 14 | 7 | OSLP | classes-22.md | 553 | 75 | The SalesPersons object enables to define sales employees and their commision percentage. |
| SalesStages | Object | 9 | 6 | OOST | classes-22.md | 629 | 67 | The SalesStages object enables defining sales stages and their probability percentage. |
| SalesTaxAuthorities | Object | 30 | 6 | OSTA | classes-22.md | 697 | 92 | SalesTaxAuthorities is a business object that represents the sales tax jurisdictions data for US and Canada localizations, or sales tax types for Latin America localization. |
| SalesTaxAuthoritiesTypes | Object | 9 | 6 | OSTT | classes-22.md | 790 | 66 | SalesTaxAuthoritiesTypes is a business object that represents the type of sales tax authorities. |
| SalesTaxCodes | Object | 17 | 6 | OSTC | classes-22.md | 857 | 153 | SalesTaxCodes is a business object that represents the inclusive sales tax codes. |
| SalesTaxCodes_Lines | Object | 12 | 2 | STC1 | classes-22.md | 1011 | 24 | TaxCodes_Lines is a child object of the SalesTaxCodes object and represents the tax authorities/types from which the tax code is combined. |
| SBObob | Object | 0 | 29 |  | classes-22.md | 1036 | 168 | The SBObob object is raw data access object that enables you to retrieve information quickly and easily. |
| Section | Object | 4 | 5 | OSEC | classes-22.md | 1205 | 23 | Represents a section of the tax code that defines the type of business transaction subject to TDS (withholding tax). |
| SectionParams | Object | 3 | 5 |  | classes-22.md | 1229 | 20 | Holds the key and code to an existing section. |
| SectionsParams | Collection | 1 | 5 |  | classes-22.md | 1250 | 17 | A collection of SectionParams objects. |
| SectionsService | Object | 0 | 8 | OSEC | classes-22.md | 1268 | 125 | The SectionsService service enables you to add, look up and remove sections in the section master data table. |
| SensitiveDataAccess | Object | 8 | 5 |  | classes-22.md | 1394 | 23 | SensitiveDataAccess Class |
| SensitiveDataAccessService | Object | 0 | 5 |  | classes-22.md | 1418 | 16 | SensitiveDataAccessService Class |
| SerialNumberDetail | Object | 15 | 5 | OSRN, OITL, ITL1 | classes-22.md | 1435 | 32 | The serial number details for the item. |
| SerialNumberDetailParams | Object | 1 | 5 |  | classes-22.md | 1468 | 18 | Holds the key to the serial details for the item. |
| SerialNumberDetailsService | Object | 0 | 5 | OSRN, OITL, ITL1 | classes-22.md | 1487 | 65 | The SerialNumberDetailsService service enables you to look up and update serial number details for the item. |
| SerialNumbers | Object | 18 | 2 | OSRN, OSRW, OSRQ, OITL, ITL1 | classes-22.md | 1553 | 34 | SerialNumbers is a business object that represents the serial numbers and additional tracking information of items. |
| Series | Object | 27 | 5 | NNM1 | classes-22.md | 1588 | 42 | Series is a data structure related to the SeriesService. |
| SeriesCollection | Collection | 1 | 5 | NNM1 | classes-22.md | 1631 | 15 | SeriesCollection is a data collection of Series data structures. |
| SeriesLine | Object | 5 | 5 | CSN1 | classes-22.md | 1647 | 27 | Contains the details of a certificate series. |
| SeriesLines | Collection | 1 | 6 |  | classes-22.md | 1675 | 22 | A collection of SeriesLine objects. |
| SeriesParams | Object | 1 | 5 |  | classes-22.md | 1698 | 16 | The SeriesParams specifies an identification key (Series) for which the SeriesService is related. |
| SeriesService | Object | 0 | 22 | NNM1 | classes-22.md | 1715 | 528 | SeriesService manages the Series object, a component of the document numbering system. |
| ServiceAppReport | Object | 4 | 5 |  | classes-22.md | 2244 | 19 | ServiceAppReport Class |
| ServiceAppReportContent | Object | 1 | 5 |  | classes-22.md | 2264 | 16 | ServiceAppReportContent Class |
| ServiceAppReportParams | Object | 2 | 5 |  | classes-22.md | 2281 | 17 | ServiceAppReportParams Class |
| ServiceCallActivities | Object | 4 | 3 | SCL5 | classes-22.md | 2299 | 31 | ServiceCallActivities is a child object of the ServiceCalls object in the Service module. |
| ServiceCallBPAddressComponents | Object | 27 | 0 |  | classes-23.md | 3 | 32 | ServiceCallBPAddressComponents Class |
| ServiceCallInventoryExpenses | Object | 9 | 3 | SCL4 | classes-23.md | 36 | 35 | ServiceCallInventoryExpenses is a child object of the ServiceCalls object in the Service module. |
| ServiceCallOrigin | Object | 4 | 5 | OSCO | classes-23.md | 72 | 22 | Represents a service call origin, that is, the channel through which a call was made, such as by telephone or via the Web. |
| ServiceCallOriginParams | Object | 2 | 5 |  | classes-23.md | 95 | 19 | Holds the key and name to an existing service call origin. |
| ServiceCallOriginParamsCollection | Collection | 1 | 5 |  | classes-23.md | 115 | 17 | A collection of ServiceCallOriginParams objects. |
| ServiceCallOriginsService | Object | 0 | 8 | OSCO | classes-23.md | 133 | 133 | The ServiceCallOriginsService service enables you to add, look up and remove service call origins in the service call origin master data table. |
| ServiceCallProblemSubType | Object | 4 | 5 |  | classes-23.md | 267 | 19 | ServiceCallProblemSubType Class |
| ServiceCallProblemSubTypeParams | Object | 2 | 5 |  | classes-23.md | 287 | 17 | ServiceCallProblemSubTypeParams Class |
| ServiceCallProblemSubTypeParamsCollection | Collection | 1 | 5 |  | classes-23.md | 305 | 15 | ServiceCallProblemSubTypeParamsCollection Class |
| ServiceCallProblemSubTypesService | Object | 0 | 8 |  | classes-23.md | 321 | 21 | ServiceCallProblemSubTypesService Class |
| ServiceCallProblemType | Object | 4 | 5 | OSCP | classes-23.md | 343 | 22 | Represents a service call problem type. |
| ServiceCallProblemTypeParams | Object | 2 | 5 |  | classes-23.md | 366 | 20 | Holds the key and name to an existing service call problem type. |
| ServiceCallProblemTypeParamsCollection | Collection | 1 | 5 |  | classes-23.md | 387 | 17 | A collection of ServiceCallProblemTypeParams objects. |
| ServiceCallProblemTypesService | Object | 0 | 8 | OSCP | classes-23.md | 405 | 143 | The ServiceCallProblemTypesService service enables you to add, look up and remove service call problem types in the service call problem type master data table. |
| ServiceCalls | Object | 90 | 8 | OSCL | classes-23.md | 549 | 159 | ServiceCalls is a business object that represents the service calls table in the Service module. |
| ServiceCallSchedulings | Object | 50 | 2 |  | classes-23.md | 709 | 60 | ServiceCallSchedulings Class |
| ServiceCallSolutions | Object | 4 | 3 | SCL1 | classes-23.md | 770 | 31 | ServiceCallSolutions is a child object of the ServiceCalls object in the Service module. |
| ServiceCallSolutionStatus | Object | 4 | 5 | OSST | classes-23.md | 802 | 22 | Represents a service call solution status. |
| ServiceCallSolutionStatusParams | Object | 2 | 5 |  | classes-23.md | 825 | 20 | Holds the key and name to an existing service call solution status. |
| ServiceCallSolutionStatusParamsCollection | Collection | 1 | 5 |  | classes-23.md | 846 | 17 | A collection of ServiceCallSolutionStatusParams objects. |
| ServiceCallSolutionStatusService | Object | 0 | 8 | OSST | classes-23.md | 864 | 114 | The ServiceCallSolutionStatusService service enables you to add, look up and remove service call solution statuses in the service call solution status master data table. |
| ServiceCallStatus | Object | 4 | 5 | OSCS | classes-23.md | 979 | 22 | Represents a service call status. |
| ServiceCallStatusParams | Object | 2 | 5 |  | classes-23.md | 1002 | 20 | Holds the key and name to an existing service call solution status. |
| ServiceCallStatusParamsCollection | Collection | 1 | 5 |  | classes-23.md | 1023 | 17 | A collection of ServiceCallStatusParams objects. |
| ServiceCallStatusService | Object | 0 | 8 | OSCS | classes-23.md | 1041 | 110 | The ServiceCallStatusService service enables you to add, look up and remove service call statuses in the service call status master data table. |
| ServiceCallType | Object | 4 | 5 | OSCT | classes-23.md | 1152 | 22 | Represents a service call type. |
| ServiceCallTypeParams | Object | 2 | 5 |  | classes-23.md | 1175 | 19 | Holds the key and name to an existing service call type. |
| ServiceCallTypeParamsCollection | Collection | 1 | 5 |  | classes-23.md | 1195 | 17 | A collection of ServiceCallTypeParams objects. |
| ServiceCallTypesService | Object | 0 | 8 | OSCT | classes-23.md | 1213 | 126 | The ServiceCallTypesService service enables you to add, look up and remove service call types in the service call type master data table. |
| ServiceContract_Lines | Object | 12 | 2 | CTR1 | classes-23.md | 1340 | 30 | ServiceContract_Lines is a child object of the ServiceContracts object that represents the line entries of each service contract. |
| ServiceContracts | Object | 54 | 8 | OCTR | classes-23.md | 1371 | 113 | ServiceContracts is a business object that represents the service contracts table in the Service module of SAP Business One application. |
| ServiceGroup | Object | 3 | 5 | OSGP | classes-23.md | 1485 | 22 | Represents a service group that can be used for the automatic determination of tax codes for services. |
| ServiceGroupParams | Object | 2 | 5 |  | classes-23.md | 1508 | 19 | Holds the key and name to an existing service group. |
| ServiceGroupsParams | Collection | 1 | 5 |  | classes-23.md | 1528 | 18 | A collection of ServiceGroupParams objects. |
| ServiceGroupsService | Object | 0 | 8 | OSGP | classes-23.md | 1547 | 70 | The ServiceGroupsService service enables you to add, look up, update, and remove service groups. |
| ServiceTaxPostingParams | Object | 1 | 5 |  | classes-23.md | 1618 | 16 | ServiceTaxPostingParams Class |
| ServiceTaxPostingParamsCollection | Collection | 1 | 5 |  | classes-23.md | 1635 | 15 | ServiceTaxPostingParamsCollection Class |
| ServiceTaxPostingService | Object | 0 | 5 |  | classes-23.md | 1651 | 15 | ServiceTaxPostingService Class |
| ShippingTypes | Object | 5 | 7 | OSHP | classes-23.md | 1667 | 62 | The ShippingTypes object enables to define transportation methods (for example, air cargo and courier) to carry out deliveries. |
| ShowDifferenceParams | Object | 5 | 5 |  | classes-23.md | 1730 | 22 | Holds the key to an existing change log that contains several log instances. |
| SingleUserConnection | Object | 2 | 5 |  | classes-23.md | 1753 | 17 | SingleUserConnection Class |
| SingleUserConnectionParams | Object | 1 | 5 |  | classes-23.md | 1771 | 16 | SingleUserConnectionParams Class |
| SingleUserConnectionService | Object | 0 | 5 |  | classes-23.md | 1788 | 16 | SingleUserConnectionService Class |
| SNBLines | Object | 10 | 2 |  | classes-23.md | 1805 | 20 | SNBLines Class |
| SpecialPrices | Object | 14 | 8 | OSPP | classes-23.md | 1826 | 167 | Represents a discount for a specific item in a specific price list. |
| SpecialPricesDataAreas | Object | 13 | 3 | SPP1 | classes-23.md | 1994 | 90 | SpecialPricesDataAreas is a child object of SpecialPrices object and represents special prices that are valid only for specified periods such as, holidays and season sales. |
| SpecialPricesQuantityAreas | Object | 11 | 3 | SPP2 | classes-24.md | 3 | 85 | SpecialPricesQuantityAreas is a child object of SpecialPricesDataAreas object and represents special prices that are valid only for specified quantities and above. |
| State | Object | 5 | 5 | OCST | classes-24.md | 89 | 26 | Represents a state that can be included, for example, in an address for a business partner. |
| StateParams | Object | 3 | 5 |  | classes-24.md | 116 | 22 | Holds the key and name to an existing state. |
| StatesParams | Collection | 1 | 5 |  | classes-24.md | 139 | 17 | A collection of StateParams objects. |
| StatesService | Object | 0 | 8 | OCST | classes-24.md | 157 | 83 | The StatesService service enables you to add, look up and remove states in the states master data table. |
| StockTaking | Object | 5 | 5 | OITW | classes-24.md | 241 | 57 | This function is abandoned in SAP Business One 9.0. |
| StockTransfer | Object | 56 | 12 | OWTR | classes-24.md | 299 | 167 | StockTransfer is a business object that represents items to transfer from one warehouse to another. |
| StockTransfer_ApprovalRequests | Object | 5 | 1 | OWDDV | classes-24.md | 467 | 14 | StockTransfer_ApprovalRequests is a child object of the StockTransfer object. |
| StockTransfer_Lines | Object | 42 | 3 | WTR1 | classes-24.md | 482 | 129 | StockTransfer_Lines is a child object of the StockTransfer object that represents the line entries of each stock transfer. |
| StockTransfer_TaxExtension | Object | 4 | 0 | WTR12 | classes-24.md | 612 | 10 | StockTransfer_TaxExtension is a child object of the StockTransfer object. |
| StockTransferLinesBinAllocations | Object | 7 | 2 | INV19 | classes-24.md | 623 | 19 | StockTransferLinesBinAllocations is a child object of the StockTransfer_Lines object that represents the bin allocation of items or serial items or batch items. |
| TargetGroup | Object | 4 | 5 | OTTG | classes-24.md | 643 | 21 | A target group is a list of prospects. |
| TargetGroupParams | Object | 2 | 5 |  | classes-24.md | 665 | 19 | Holds the key to an existing target group. |
| TargetGroupsDetail | Object | 22 | 5 | TTG1 | classes-24.md | 685 | 39 | The detailed information of the potential customers or leads for the target group. |
| TargetGroupsDetails | Collection | 1 | 6 |  | classes-24.md | 725 | 20 | A collection of TargetGroupsDetail objects. |
| TargetGroupsParams | Collection | 1 | 5 |  | classes-24.md | 746 | 17 | A collection of TargetGroupParams objects. |
| TargetGroupsService | Object | 0 | 8 | OTTG | classes-24.md | 764 | 23 | The TargetGroupsService service enables you to add, look up, update, and remove target groups. |
| TaxCodeDetermination | Object | 38 | 5 | OTCX | classes-24.md | 788 | 59 | Represents the tax code determination rules according to which the application proposes tax codes in sales and purchasing document lines. |
| TaxCodeDeterminationParams | Object | 1 | 5 |  | classes-24.md | 848 | 18 | Holds the key to an existing tax code determination rule. |
| TaxCodeDeterminationsParams | Collection | 1 | 5 |  | classes-24.md | 867 | 18 | A collection of TaxCodeDeterminationParams objects. |
| TaxCodeDeterminationsService | Object | 0 | 8 | OTCX | classes-24.md | 886 | 70 | The TaxCodeDeterminationsService service enables you to add, look up, update, and remove tax code determination rules. |
| TaxCodeDeterminationsTCDParams | Collection | 1 | 5 |  | classes-24.md | 957 | 15 | Legal Text on Tax Code Determination - Setup form. |
| TaxCodeDeterminationsTCDService | Object | 0 | 6 |  | classes-24.md | 973 | 17 | TaxCodeDeterminationsTCDService Class |
| TaxCodeDeterminationTCD | Object | 7 | 5 |  | classes-24.md | 991 | 22 | TaxCodeDeterminationTCD Class |
| TaxCodeDeterminationTCDByUsage | Object | 6 | 5 |  | classes-24.md | 1014 | 21 | TaxCodeDeterminationTCDByUsage Class |
| TaxCodeDeterminationTCDByUsages | Collection | 1 | 6 |  | classes-24.md | 1036 | 17 | TaxCodeDeterminationTCDByUsages Class |
| TaxCodeDeterminationTCDDefaultWT | Object | 3 | 5 |  | classes-24.md | 1054 | 18 | TaxCodeDeterminationTCDDefaultWT Class |
| TaxCodeDeterminationTCDDefaultWTs | Collection | 1 | 6 |  | classes-24.md | 1073 | 17 | TaxCodeDeterminationTCDDefaultWTs Class |
| TaxCodeDeterminationTCDKeyField | Object | 17 | 5 |  | classes-24.md | 1091 | 32 | TaxCodeDeterminationTCDKeyField Class |
| TaxCodeDeterminationTCDKeyFields | Collection | 1 | 6 |  | classes-24.md | 1124 | 17 | TaxCodeDeterminationTCDKeyFields Class |
| TaxCodeDeterminationTCDParams | Object | 1 | 5 |  | classes-24.md | 1142 | 16 | TaxCodeDeterminationTCDParams Class |
| TaxCodeDeterminationTCDPeriod | Object | 5 | 5 |  | classes-24.md | 1159 | 20 | TaxCodeDeterminationTCDPeriod Class |
| TaxCodeDeterminationTCDPeriods | Collection | 1 | 6 |  | classes-24.md | 1180 | 17 | TaxCodeDeterminationTCDPeriods Class |
| TaxCodeDeterminationTCDValue | Object | 8 | 5 |  | classes-24.md | 1198 | 23 | TaxCodeDeterminationTCDValue Class |
| TaxCodeDeterminationTCDValues | Collection | 1 | 6 |  | classes-24.md | 1222 | 17 | TaxCodeDeterminationTCDValues Class |
| TaxDefinitions | Object | 3 | 3 | STA1 | classes-24.md | 1240 | 77 | A set of tax rates for different time periods for a particular sales tax jurisdiction. |
| TaxExtension | Object | 58 | 0 | CPI12, CPV12, CSI12, CSV12, DLN12, DRF12, IGE12, IGN12, INV12, PCH12, PDN12, POR12, QUT12, RDN12, RDR12, RIN12, RPC12, RPD12 | classes-24.md | 1318 | 65 | TaxExtension is a child object of the Documents object. |
| TaxInvoice_DocumentReferences | Object | 10 | 2 |  | classes-24.md | 1384 | 21 | TaxInvoice_DocumentReferences Class |
| TaxInvoice_Lines | Object | 6 | 2 | TSI1 | classes-24.md | 1406 | 19 | TaxInvoice_Lines is a child object of the TaxInvoices object that represents the line entries of each tax invoice document. |
| TaxInvoice_LinkedDownPayments | Object | 22 | 1 | TSI4 | classes-24.md | 1426 | 69 | Link to tax invoices from down payments for Russia localization. |
| TaxInvoice_OperationCodes | Object | 5 | 2 |  | classes-24.md | 1496 | 17 | TaxInvoice_OperationCodes is a child object of the TaxInvoices object that represents the operation codes of the tax invoice document. |
| TaxInvoiceReport | Object | 16 | 5 |  | classes-24.md | 1514 | 31 | TaxInvoiceReport Class |
| TaxInvoiceReportLine | Object | 18 | 5 |  | classes-24.md | 1546 | 33 | TaxInvoiceReportLine Class |
| TaxInvoiceReportLineCollection | Collection | 1 | 5 |  | classes-24.md | 1580 | 15 | TaxInvoiceReportLineCollection Class |
| TaxInvoiceReportParams | Object | 1 | 5 |  | classes-24.md | 1596 | 16 | TaxInvoiceReportParams Class |
| TaxInvoiceReportService | Object | 0 | 6 |  | classes-24.md | 1613 | 18 | TaxInvoiceReportService Class |
| TaxInvoices | Object | 36 | 7 | OTSI | classes-24.md | 1632 | 177 | TaxInvoices is a business object that represents the header data of a Tax Invoice document. |
| TaxJurisdictions | Object | 15 | 2 | PCH4 | classes-24.md | 1810 | 57 | Represents the tax amount of a document. |
| TaxReplStateSubData | Object | 2 | 5 | OTRSS | classes-24.md | 1868 | 21 | Tax replacement state subscription data. |
| TaxReplStateSubParams | Object | 1 | 5 |  | classes-24.md | 1890 | 18 | Holds the key to existing tax replacement state subscription data. |
| TaxReplStateSubService | Object | 0 | 7 | OTRSS | classes-24.md | 1909 | 69 | The TaxReplStateSubService service enables you to add, look up, update, and remove tax replacement state subscription. |
| TaxReportAccount | Object | 1 | 5 | VTR5 | classes-24.md | 1979 | 16 | TaxReportAccount is a data structure related to the TaxReportsService. |
| TaxReportAccounts | Collection | 1 | 5 | VTR5 | classes-24.md | 1996 | 15 | TaxReportAccounts is a Data Collection of TaxReportAccount data structures. |
| TaxReportBusinessPartner | Object | 1 | 5 |  | classes-24.md | 2012 | 16 | TaxReportBusinessPartner is a data structure related to the TaxReportsService. |
| TaxReportBusinessPartners | Collection | 1 | 5 | VTR4 | classes-24.md | 2029 | 15 | TaxReportBusinessPartners is a Data Collection of TaxReportBusinessPartner data structures. |
| TaxReportDocument | Object | 3 | 5 | VTR2 | classes-24.md | 2045 | 18 | TaxReportDocument is a data structure related to the TaxReportsService. |
| TaxReportDocuments | Collection | 1 | 5 | VTR2 | classes-24.md | 2064 | 15 | TaxReportDocuments is a Data Collection of TaxReportDocument data structures. |
| TaxReportFilter | Object | 35 | 5 | OVTR | classes-25.md | 3 | 50 | TaxReportFilter is a data structure related to the TaxReportsService. |
| TaxReportFilterParams | Object | 3 | 5 | OVTR | classes-25.md | 54 | 18 | The TaxReportFilterParams specifies the identification key combination(Code, Filter-Type and Name) for which the TaxReportsService is related. |
| TaxReportFiltersParams | Collection | 1 | 5 | OVTR | classes-25.md | 73 | 15 | TaxReportFiltersParams is a Data Collection of TaxReportFilterParams Identification key combination. |
| TaxReportGroup | Object | 2 | 5 | VTR1 | classes-25.md | 89 | 17 | TaxReportGroup is a data structure related to the TaxReportsService. |
| TaxReportGroups | Collection | 1 | 5 | VTR1 | classes-25.md | 107 | 15 | TaxReportGroups is a Data Collection of TaxReportGroupss. |
| TaxReportSeries | Object | 2 | 5 | VTR3 | classes-25.md | 123 | 17 | TaxReportSeries is a data structure related to the TaxReportsService. |
| TaxReportSeriesCollection | Collection | 1 | 5 | VTR3 | classes-25.md | 141 | 15 | TaxReportSeriesCollection is a Data Collection of TaxReportSeries. |
| TaxWebSite | Object | 4 | 5 |  | classes-25.md | 157 | 19 | TaxWebSite Class |
| TaxWebSiteParams | Object | 2 | 5 |  | classes-25.md | 177 | 17 | TaxWebSiteParams Class |
| TaxWebSitesParams | Collection | 1 | 5 |  | classes-25.md | 195 | 15 | TaxWebSitesParams Class |
| TaxWebSitesService | Object | 0 | 10 |  | classes-25.md | 211 | 24 | TaxWebSitesService Class |
| TeamCounter | Object | 6 | 5 | INC4 | classes-25.md | 236 | 23 | A group of counters' counting results of an item at a storage location add up to its total quantity. |
| TeamCounters | Collection | 1 | 6 |  | classes-25.md | 260 | 20 | A collection of TeamCounter objects. |
| TeamMembers | Object | 5 | 2 | HTM1 | classes-25.md | 281 | 19 | TeamMembers is a child object of the Teams object that represents the membership role in a team of an employee. |
| Teams | Object | 6 | 7 | OHTM | classes-25.md | 301 | 66 | Teams is a business object that represents the list of teams from which team memberships of an employee can be selected. |
| TechnicianSchedulings | Object | 5 | 5 |  | classes-25.md | 368 | 20 | TechnicianSchedulings Class |
| TechnicianSchedulingsCollection | Collection | 1 | 5 |  | classes-25.md | 389 | 15 | TechnicianSchedulingsCollection Class |
| TechnicianSchedulingsParams | Object | 3 | 5 |  | classes-25.md | 405 | 18 | TechnicianSchedulingsParams Class |
| TechnicianSettings | Object | 2 | 5 |  | classes-25.md | 424 | 17 | TechnicianSettings Class |
| TechnicianSettingsGroup | Object | 11 | 5 |  | classes-25.md | 442 | 26 | TechnicianSettingsGroup Class |
| TechnicianSettingsGroupParams | Object | 2 | 5 |  | classes-25.md | 469 | 17 | TechnicianSettingsGroupParams Class |
| TechnicianSettingsParams | Object | 1 | 5 |  | classes-25.md | 487 | 16 | TechnicianSettingsParams Class |
| TerminationReason | Object | 3 | 5 |  | classes-25.md | 504 | 18 | TerminationReason Class |
| TerminationReasonParams | Object | 3 | 5 |  | classes-25.md | 523 | 18 | TerminationReasonParams Class |
| TerminationReasonParamsCollection | Collection | 1 | 5 |  | classes-25.md | 542 | 15 | TerminationReasonParamsCollection Class |
| TerminationReasonService | Object | 0 | 8 |  | classes-25.md | 558 | 21 | TerminationReasonService Class |
| Territories | Object | 7 | 7 | OTER | classes-25.md | 580 | 66 | Territories is a business object that represents the territory segmentation. |
| TrackingNote | Object | 8 | 5 |  | classes-25.md | 647 | 23 | TrackingNote Class |
| TrackingNoteBroker | Object | 4 | 5 |  | classes-25.md | 671 | 19 | TrackingNoteBroker Class |
| TrackingNoteBrokerCollection | Collection | 1 | 5 |  | classes-25.md | 691 | 15 | TrackingNoteBrokerCollection Class |
| TrackingNoteItem | Object | 10 | 5 |  | classes-25.md | 707 | 25 | TrackingNoteItem Class |
| TrackingNoteItemCollection | Collection | 1 | 5 |  | classes-25.md | 733 | 15 | TrackingNoteItemCollection Class |
| TrackingNoteParams | Object | 2 | 5 |  | classes-25.md | 749 | 17 | TrackingNoteParams Class |
| TrackingNoteParamsCollection | Collection | 1 | 5 |  | classes-25.md | 767 | 15 | TrackingNoteParamsCollection Class |
| TrackingNotesService | Object | 0 | 8 |  | classes-25.md | 783 | 21 | TrackingNotesService Class |
| TransactionCode | Object | 2 | 5 |  | classes-25.md | 805 | 17 | TransactionCode Class |
| TransactionCodeParams | Object | 2 | 5 |  | classes-25.md | 823 | 17 | TransactionCodeParams Class |
| TransactionCodeParamsCollection | Collection | 1 | 5 |  | classes-25.md | 841 | 15 | TransactionCodeParamsCollection Class |
| TransactionCodesService | Object | 0 | 8 |  | classes-25.md | 857 | 21 | TransactionCodesService Class |
| TranslationsInUserLanguages | Object | 5 | 2 | MLT1 | classes-25.md | 879 | 17 | TranslationsInUserLanguages is a child object of the MultiLanguageTranslations object. |
| TransportationDocumentCollection | Collection | 1 | 5 |  | classes-25.md | 897 | 15 | TransportationDocumentCollection Class |
| TransportationDocumentData | Object | 19 | 5 |  | classes-25.md | 913 | 34 | TransportationDocumentData Class |
| TransportationDocumentLineData | Object | 8 | 5 |  | classes-25.md | 948 | 23 | TransportationDocumentLineData Class |
| TransportationDocumentLineDataCollection | Collection | 1 | 5 |  | classes-25.md | 972 | 15 | TransportationDocumentLineDataCollection Class |
| TransportationDocumentParams | Object | 1 | 5 |  | classes-25.md | 988 | 16 | TransportationDocumentParams Class |
| TransportationDocumentParamsCollection | Collection | 1 | 5 |  | classes-25.md | 1005 | 15 | TransportationDocumentParamsCollection Class |
| TransportationDocumentService | Object | 0 | 7 |  | classes-25.md | 1021 | 20 | TransportationDocumentService Class |
| UnitOfMeasurement | Object | 28 | 5 | OUOM | classes-25.md | 1042 | 64 | To manage inventory items by different UoMs (units of measurement) applicable to your business, you need to define the individual UoMs. |
| UnitOfMeasurementGroup | Object | 5 | 5 | OUGP | classes-25.md | 1107 | 24 | A UoM (Unit of Measurement) group is a set of UoMs that you want to use for a certain type of product. |
| UnitOfMeasurementGroupParams | Object | 2 | 5 |  | classes-25.md | 1132 | 19 | Holds the key to an existing unit of measurement group. |
| UnitOfMeasurementGroupParamsCollection | Collection | 1 | 5 |  | classes-25.md | 1152 | 17 | A collection of UnitOfMeasurementGroupParams objects. |
| UnitOfMeasurementGroupsService | Object | 0 | 8 | OUGP | classes-25.md | 1170 | 70 | The UnitOfMeasurementGroupsService service enables you to add, look up, update, and remove unit of measurement groups. |
| UnitOfMeasurementParams | Object | 2 | 5 |  | classes-25.md | 1241 | 19 | Holds the key to an existing unit of measurement. |
| UnitOfMeasurementParamsCollection | Collection | 1 | 5 |  | classes-25.md | 1261 | 17 | A collection of UnitOfMeasurement objects. |
| UnitOfMeasurementsService | Object | 0 | 8 | OUOM | classes-25.md | 1279 | 70 | The UnitOfMeasurementsService service enables you to add, look up, update, and remove unit of measurements. |
| UoMGroupDefinition | Object | 6 | 5 | UGP1 | classes-25.md | 1350 | 23 | Defines the unit of measurement group. |
| UoMGroupDefinitionCollection | Collection | 1 | 6 |  | classes-25.md | 1374 | 20 | A collection of UoMGroupDefinition objects. |
| UoMPrices | Object | 13 | 3 |  | classes-25.md | 1395 | 24 | UoMPrices Class |
| UserActionRecord | Object | 14 | 1 | USR5 | classes-25.md | 1420 | 50 | Displays the access details and the actions of SAP Business One users who have logged on and logged off with the SAP Business One client or the DI API. |
| UserBranchAssignment | Object | 3 | 3 |  | classes-25.md | 1471 | 14 | UserBranchAssignment Class |
| UserDefaultGroups | Object | 36 | 7 | OUDG | classes-25.md | 1486 | 118 | The UserDefaultGroups object enables to define default values (such as, default documents, default address in printed documents, windows color, and so on). |
| UserFields | Object | 1 | 0 |  | classes-25.md | 1605 | 6 | The UserFields object is a collection of Fields objects, which are user defined fields. |
| UserFieldsMD | Object | 15 | 7 | CUFD | classes-25.md | 1612 | 44 | UserFieldsMD is a business object that enables you to manage user-defined fields in user and system tables. |
| UserGroup | Object | 7 | 5 |  | classes-25.md | 1657 | 22 | UserGroup Class |
| UserGroupByUser | Object | 4 | 3 |  | classes-25.md | 1680 | 15 | UserGroupByUser Class |
| UserGroupParams | Object | 2 | 5 |  | classes-25.md | 1696 | 17 | UserGroupParams Class |
| UserGroupService | Object | 0 | 8 |  | classes-25.md | 1714 | 21 | UserGroupService Class |
| UserGroupsParams | Collection | 1 | 5 |  | classes-25.md | 1736 | 15 | UserGroupsParams Class |
| UserKeysMD | Object | 6 | 6 | OUKD | classes-25.md | 1752 | 29 | The UserKeysMD object enables to mange user defined keys of user tables. |
| UserKeysMD_Elements | Object | 3 | 2 | UKD1 | classes-25.md | 1782 | 13 | UserKeysMD_Elements is a child object of the UserKeysMD object. |
| UserLanguages | Object | 6 | 7 | OLNG | classes-25.md | 1796 | 64 | The UserLanguages object represents the languages setup and enables to define new languages or modify the exisiting ones. |
| UserLicenseParams | Object | 3 | 5 |  | classes-25.md | 1861 | 20 | Contains the parameters for assigning licenses. |
| UserMenuItem | Object | 9 | 5 | CUMI | classes-25.md | 1882 | 24 | UserMenuItem is a Data structure related to the UserMenuService. |
| UserMenuItems | Collection | 1 | 6 | CUMI | classes-25.md | 1907 | 17 | UserMenuItems is a Data Collection of UserMenuItem data structures. |
| UserMenuParams | Object | 1 | 5 | CUMI | classes-25.md | 1925 | 16 | The UserMenuParams specifies the identification key (UserID) for which the UserMenuService is related. |
| UserMenuService | Object | 0 | 7 | CUMI | classes-25.md | 1942 | 97 | UserMenuService manages the user menu. |
| UserObjectMD_ChildTables | Object | 6 | 2 | UDO1 | classes-25.md | 2040 | 18 | UserObjectMD_ChildTables is child object of the UserObjectsMD object that represents child user tables and their related history log tables. |
| UserObjectMD_EnhancedFormColumns | Object | 8 | 2 | UDO4 | classes-25.md | 2059 | 21 | UserObjectMD_EnhancedFormColumns is a child object of the UserObjectsMD object that represents the default fields (columns) to display in the UDO enhanced default form (UDO form with the header-line style). |
| UserObjectMD_FindColumns | Object | 5 | 2 | UDO2 | classes-25.md | 2081 | 16 | UserObjectMD_FindColumns is a child object of the UserObjectsMD object that represents the fields (columns) to display in the Find Form (Choose From List form). |
| UserObjectMD_FormColumns | Object | 7 | 2 | UDO3 | classes-25.md | 2098 | 43 | UserObjectMD_FormColumns is child object of the UserObjectsMD object that represents the default fields (columns) to display in the default form (UDO form with the matrix style). |
| UserObjectsMD | Object | 32 | 6 | OUDO | classes-26.md | 3 | 87 | The UserObjectsMD object represents the registration data settings, such as table name and supported services, of a user defined object. |
| UserPermission | Object | 5 | 2 | USR3 | classes-26.md | 91 | 18 | UserPermission is a business object that enables to set the authorization of a specified user to a UserPermissionTree. |
| UserPermissionForms | Object | 5 | 2 | UPT1 | classes-26.md | 110 | 17 | UserPermissionForms is a child object of UserPermissionTree object and enables to add a user permission to a collection of forms. |
| UserPermissionTree | Object | 11 | 7 | OUPT | classes-26.md | 128 | 203 | UserPermissionTree is a business object that represents the User Authorization Form. |
| UserQueries | Object | 14 | 7 | OUQR | classes-26.md | 332 | 72 | The UserQueries object enables to define user queries in the Queries Manager. |
| Users | Object | 30 | 9 | OUSR | classes-26.md | 405 | 90 | Users is a business object that represents the users table of the SAP Business One application. |
| UserTable | Object | 6 | 7 |  | classes-26.md | 496 | 175 | The UserTable object represents records of a user-defined table. |
| UserTables | Collection | 1 | 1 |  | classes-26.md | 672 | 10 | UserTables is a collection of UserTable objects. |
| UserTablesMD | Object | 7 | 7 | OUTB | classes-26.md | 683 | 32 | The UserTablesMD object enables to manage user defined tables as follows: - Add a user table. |
| UserValidValues | Object | 3 | 2 | CUVV | classes-26.md | 716 | 17 | UserValidValues is an object related to the FormattedSearches object. |
| ValidValue | Object | 2 | 0 |  | classes-26.md | 734 | 7 | The ValidValue object represents a single valid value element of a specified user field. |
| ValidValues | Collection | 1 | 1 |  | classes-26.md | 742 | 10 | ValidValues is a collection of ValidValue objects. |
| ValidValuesMD | Object | 3 | 3 | UFD1 | classes-26.md | 753 | 28 | ValidValuesMD enables you to add valid values to a specified user defined field (UserFieldsMD). |
| ValueMappingCommunicationData | Object | 10 | 5 |  | classes-26.md | 782 | 25 | ValueMappingCommunicationData Class |
| ValueMappingCommunicationParams | Object | 1 | 5 |  | classes-26.md | 808 | 16 | ValueMappingCommunicationParams Class |
| ValueMappingCommunicationService | Object | 0 | 6 |  | classes-26.md | 825 | 18 | ValueMappingCommunicationService Class |
| ValueMappingParams | Object | 1 | 5 |  | classes-26.md | 844 | 16 | ValueMappingParams Class |
| ValueMappingService | Object | 0 | 10 |  | classes-26.md | 861 | 26 | ValueMappingService Class |
| VatGroups | Object | 31 | 7 | OVTG | classes-26.md | 888 | 98 | The VatGroups object enables to define tax groups that can be assigned to business partners and items in sales and purchase documents. |
| VatGroups_Lines | Object | 6 | 2 | VTG1 | classes-26.md | 987 | 21 | VatGroups_Lines is a child object of the VatGroups_Lines object. |
| VM_B1ValuesCollection | Collection | 1 | 5 |  | classes-26.md | 1009 | 15 | VM_B1ValuesCollection Class |
| VM_B1ValuesData | Object | 4 | 5 |  | classes-26.md | 1025 | 19 | VM_B1ValuesData Class |
| VM_ThirdPartyValuesCollection | Collection | 1 | 5 |  | classes-26.md | 1045 | 15 | VM_ThirdPartyValuesCollection Class |
| VM_ThirdPartyValuesData | Object | 4 | 5 |  | classes-26.md | 1061 | 19 | VM_ThirdPartyValuesData Class |
| WarehouseLocations | Object | 34 | 6 | OLCT | classes-26.md | 1081 | 88 | The WarehouseLocations object enables to define geographical locations for warehouses. |
| Warehouses | Object | 92 | 7 | OWHS | classes-26.md | 1170 | 165 | Warehouses is a business object that represents the warehouses information in the Inventory module. |
| WarehouseSublevelCode | Object | 4 | 5 | OBSL | classes-26.md | 1336 | 21 | You can set up different codes for each warehouse sublevel. |
| WarehouseSublevelCodeCollectionParams | Collection | 1 | 5 |  | classes-26.md | 1358 | 18 | A collection of WarehouseSublevelCodeParams objects. |
| WarehouseSublevelCodeParams | Object | 3 | 5 |  | classes-26.md | 1377 | 20 | Holds the key to an existing warehouse sublevel code. |
| WarehouseSublevelCodesService | Object | 0 | 8 | OBSL | classes-26.md | 1398 | 70 | The WarehouseSublevelCodesService service enables you to add, look up, update, and remove warehouse sublevel codes. |
| WeightMeasures | Object | 6 | 7 | OWGT | classes-26.md | 1469 | 63 | The WeightMeasures object enables to define the weight measure units that are used for item records. |
| WIPMapping | Object | 4 | 5 |  | classes-26.md | 1533 | 19 | WIPMapping Class |
| WIPMappingCollection | Collection | 1 | 6 |  | classes-26.md | 1553 | 17 | WIPMappingCollection Class |
| WithholdingTaxCertificates | Object | 16 | 2 |  | classes-26.md | 1571 | 26 | WithholdingTaxCertificates Class |
| WithholdingTaxCodes | Object | 59 | 7 | OWHT | classes-26.md | 1598 | 134 | The WithholdingTaxCodes object enables to define the system withholding tax codes that can be applied to business partners, payments, and documents. |
| WithholdingTaxCodes_Lines | Object | 22 | 3 | WHT1 | classes-26.md | 1733 | 42 | WithholdingTaxCodes_Lines is a child object of the WithholdingTaxCodes object. |
| WithholdingTaxCodes_ProgressiveTax_Lines | Object | 5 | 3 |  | classes-26.md | 1776 | 16 | WithHoldingTaxCodes_ProgressiveTax_Lines Class |
| WithholdingTaxCodes_ValueRange_Lines | Object | 5 | 3 |  | classes-26.md | 1793 | 16 | WithHoldingTaxCodes_ValueRange_Lines Class |
| WithholdingTaxData | Object | 24 | 2 | INV5, RIN5, RDN5, RDN5, PCH5, RPC5, DPI5, DPO5, DRF5 | classes-27.md | 3 | 49 | WithholdingTaxData is a child object of Documents object and represents the Withholding tax table related to the document. |
| WithholdingTaxDataWTX | Object | 38 | 2 |  | classes-27.md | 53 | 48 | WithholdingTaxDataWTX Class |
| WithholdingTaxLines | Object | 22 | 2 | INV5 | classes-27.md | 102 | 38 | WithholdingTaxLines is a child object of Document_Lines object and supports Withholding Tax in a line level (as opposed to WithholdingTaxData object, which supports Withholding Tax in a document level). |
| WitholdingTaxDefinitionService | Object | 0 | 7 |  | classes-27.md | 141 | 20 | WitholdingTaxDefinitionService Class |
| WizardPaymentMethods | Object | 54 | 7 | OPYM | classes-27.md | 162 | 128 | The WizardPaymentMethods object enables to define payment methods, such as check, bank transfer, or bill-of-exchange. |
| WorkflowApprovalTaskListParams | Object | 1 | 5 |  | classes-27.md | 291 | 18 | This object specifies the identification key of the GetApprovalTaskList method. |
| WorkflowTask | Object | 14 | 5 | OWLS | classes-27.md | 310 | 31 | WorkflowTask is a data object holding properties for workflow tasks. |
| WorkflowTaskCollection | Collection | 1 | 5 |  | classes-27.md | 342 | 18 | WorkflowTaskCollection is a collection of WorkflowTask objects. |
| WorkflowTaskCompleteParams | Object | 3 | 5 |  | classes-27.md | 361 | 19 | This object specifies the identification key of the Complete method. |
| WorkflowTaskInputObject | Object | 6 | 5 | WLS2 | classes-27.md | 381 | 23 | WorkflowTaskInputObject is a data object holding properties for workflow task input data objects. |
| WorkflowTaskInputObjectCollection | Collection | 1 | 5 |  | classes-27.md | 405 | 18 | WorkflowTaskInputObjectCollection is a collection of WorkflowTaskInputObject objects. |
| WorkflowTaskNote | Object | 5 | 5 | WLS3 | classes-27.md | 424 | 22 | WorkflowTaskNote is a data object holding properties for the workflow task note. |
| WorkflowTaskNoteCollection | Collection | 1 | 5 |  | classes-27.md | 447 | 18 | WorkflowTaskNoteCollection is a collection of the WorkflowTaskNote objects. |
| WorkflowTaskOutputObject | Object | 5 | 5 | WLS4 | classes-27.md | 466 | 22 | WorkflowTaskOutputObject is a data object holding properties for the workflow task output data object. |
| WorkflowTaskOutputObjectCollection | Collection | 1 | 5 |  | classes-27.md | 489 | 18 | WorkflowTaskOutputObjectCollection is a collection of the WorkflowTaskOutputObject objects. |
| WorkflowTaskService | Object | 0 | 5 | OWLS | classes-27.md | 508 | 146 | WorkflowTaskService is a business object that manages the tasks of the SAP Business One Workflow component. |
| WorkOrder_Lines | Object | 11 | 2 | WKO1 | classes-27.md | 655 | 27 | WorkOrder_Lines is child object of the WorkOrders object that represents a collection of parent items in a work order. |
| WorkOrders | Object | 26 | 7 | OWKO | classes-27.md | 683 | 54 | WorkOrders is a business object that represents the work orders in the Inventory and Production module. |
| WTaxTypeCode | Object | 2 | 5 | OWXT | classes-27.md | 738 | 19 | Source table: OWXT. |
| WTaxTypeCodeParams | Object | 1 | 5 |  | classes-27.md | 758 | 18 | WTaxTypeCodeParams Class |
| WTaxTypeCodeService | Object | 0 | 8 | OWXT | classes-27.md | 777 | 23 | Source table: OWXT. |
| WTaxTypeCodesParams | Collection | 1 | 5 |  | classes-27.md | 801 | 18 | WTaxTypeCodesParams Class |
| WTDBP | Object | 8 | 5 |  | classes-27.md | 820 | 23 | WTDBP Class |
| WTDBPCollection | Collection | 1 | 5 |  | classes-27.md | 844 | 15 | WTDBPCollection Class |
| WTDCode | Object | 18 | 5 |  | classes-27.md | 860 | 33 | WTDCode Class |
| WTDCodeParams | Object | 3 | 5 |  | classes-27.md | 894 | 18 | WTDCodeParams Class |
| WTDCodeParamsCollection | Collection | 1 | 5 |  | classes-27.md | 913 | 15 | WTDCodeParamsCollection Class |
| WTDEffectiveDate | Object | 5 | 5 |  | classes-27.md | 929 | 20 | WTDEffectiveDate Class |
| WTDEffectiveDateCollection | Collection | 1 | 5 |  | classes-27.md | 950 | 15 | WTDEffectiveDateCollection Class |
| WTDFreight | Object | 5 | 5 |  | classes-27.md | 966 | 20 | WTDFreight Class |
| WTDFreightCollection | Collection | 1 | 5 |  | classes-27.md | 987 | 15 | WTDFreightCollection Class |
| WTDItem | Object | 5 | 5 |  | classes-27.md | 1003 | 20 | WTDItem Class |
| WTDItemCollection | Collection | 1 | 5 |  | classes-27.md | 1024 | 15 | WTDItemCollection Class |
| WTDValueRange | Object | 5 | 5 |  | classes-27.md | 1040 | 20 | WTDValueRange Class |
| WTDValueRangeCollection | Collection | 1 | 5 |  | classes-27.md | 1061 | 15 | WTDValueRangeCollection Class |
| WTGroups | Object | 9 | 1 |  | classes-27.md | 1077 | 18 | WTGroups Class |
