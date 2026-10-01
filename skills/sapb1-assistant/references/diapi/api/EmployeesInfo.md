<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeesInfo (Object)

EmployeesInfo is a business object that represents the employee master data in the Human Resources module. This object enables you to: - Add employee's details. - Retrieve employee's details by its key. - Update employee's details. - Save the object in XML format. Source table: OHEM.

**Remarks:** Mandatory fields in SAP Business One: FirstName and LastName. To display the form in the application: - Select Human Resources --> Employee Master Data.

## Properties (127)
- `Public Property AbsenceInfo() As EmployeeAbsenceInfo` [R] Returns the EmployeeAbsenceInfo object.
- `Public Property AccountantResponsible() As BoYesNoEnum` [R/W] property AccountantResponsible
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property AdditionalAmount() As Double` [R/W] The additional benefit amount of the employee. Field: AddiAmnt.
- `Public Property AdditionalCurrency() As String` [R/W] The currency of the additional benefit amount. Field: AddiCurr.
- `Public Property AdditionalUnit() As EmployeeExemptionUnitEnum` [R/W] The time period unit of the additional benefit. Field: AddiUnit.
- `Public Property ApplicationUserID() As Long` [R/W] Sets or returns the employee user code of SAP Business One application. Field name: userId. This is a foreign key to the Users object.
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the Attachment Entry. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property AuthorizationForRetrieveFromSEFAZ() As BoYesNoEnum` [R/W] Authorization to Retrieve NFe from SEFAZ. Field name: ARetSEFAZ.
- `Public Property BankAccount() As String` [R/W] Sets or returns the bank account number of the employee . Field name: bankAcount. Length: 100 characters.
- `Public Property BankBranch() As String` [R/W] Sets or returns the bank branch name of the employee . Field name: branch Length: 100 characters
- `Public Property BankBranchNum() As String` [R/W] Sets or returns the bank branch number of the employee . Field name: bankBranNo. Length: 30 characters.
- `Public Property BankCode() As String` [R/W] Sets or returns the employee bank name. Field name: bankCode. Length: 30 characters.
- `Public Property BankCodeForDATEV() As String` [R/W] The bank code for DATEV. Field name: BCodeDateV. Length: 20 characters.
- `Public Property BirthPlace() As String` [R/W] The birth place of the employee. Field: BirthPlace.
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Branch() As Long` [R/W] Sets or returns the branch office of the employee. Field name: branch.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CitizenshipCountryCode() As String` [R/W] Sets or returns the citizenship country code. Field name: citizenshp. This is a foreign key to the Countries table (OCRY - not exposed through the DI API). Length: 3 characters.
- `Public Property CompanyNumber() As String` [R/W] Indicate the company number to which the employee belongs, in case there are various numbers available within the company. Field name: CompanyNum. Length: 20 characters.
- `Public Property CostCenterCode() As String` [R/W] Sets or returns the cost center to which the employee belongs. Field name: CostCenter.
- `Public Property CountryOfBirth() As String` [R/W] Sets or returns the country of birth of the employee. Field name: brthCountr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property CPF() As String` [R/W] property CPF
- `Public Property CRCNumber() As String` [R/W] property CRCNumber
- `Public Property CRCState() As String` [R/W] property CRCState
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property CreateTime() As Date` [R] property CreateTime
- `Public Property DateOfBirth() As Date` [R/W] Sets or returns the birth date of the employee. Field name: birthDate.
- `Public Property Department() As Long` [R/W] Sets or returns the employee department. Field name: dept This is a foreign key to the Departments table (OUDP), which is exposed via the DepartmentsService object.
- `Public Property DeviatingBankAccountOwner() As BoYesNoEnum` [R/W] Indicate whether the bank account owner is a person other than the employee, for example, the spouse of the employee. Field: DevBAOwner.
- `Public Property DIRFResponsible() As BoYesNoEnum` [R/W] property DIRFResponsible
- `Public Property EducationInfo() As EmployeeEducationInfo` [R] Returns the EmployeeEducationInfo object.
- `Public Property EducationStatus() As String` [R/W] The education level of the employee. 1 - Without Profession 2 - With Profession 3 - High school without profession 4 - High school with profession 5 - Professional skilled exam 6 - University 7 - Indication not possible Field: StatusOfE.
- `Public Property eMail() As String` [R/W] Sets or returns the e-mail address. Field name: email. Length: 100 characters.
- `Public Property EmployeeBranchAssignment() As EmployeeBranchAssignment` [R] property EmployeeBranchAssignment
- `Public Property EmployeeCode() As String` [R/W] property EmployeeCode
- `Public Property EmployeeCosts() As Double` [R/W] Sets or returns the employee costs. Field name: empCostCur.
- `Public Property EmployeeCostsCurrency() As String` [R/W] Sets or returns the currency of the employee cost. Field name: empCostCur. Length: 3 characters.
- `Public Property EmployeeCostUnit() As BoSalaryCostUnits` [R/W] Sets or returns a valid value of BoSalaryCostUnits type that specifies the employee cost unit (for example: per hour, per day, per month, and so on). Field name: empCostUnt.
- `Public Property EmployeeID() As Long` [R] Returns the employee ID. Field name: empID.
  - remarks: SAP Business One generates a consequent ID number automatically when adding a new employee.
- `Public Property EmployeeRolesInfo() As EmployeeRolesInfo` [R] Returns the EmployeeRolesInfo child object.
- `Public Property EmployeeType() As Long` [R/W] Sets or returns the default role ID of the employee. Field name: type. This is a foreign key to the Employee Type table (OHTY - not exposed through the DI API).
  - remarks: To set a default role ID, first set the RoleID in the EmployeeRolesInfo child object.
- `Public Property ExemptionAmount() As Double` [R/W] The amount of the exemption benefit of the employee. Field: ExemptAmnt.
- `Public Property ExemptionCurrency() As String` [R/W] The currency of the exemption benefit amount. Field: ExemptCurr.
- `Public Property ExemptionUnit() As EmployeeExemptionUnitEnum` [R/W] The time period unit of the exemption benefit. Field: ExemptUnit.
- `Public Property ExternalEmployeeNumber() As String` [R/W] The external employee number. Field: ExtEmpNo.
- `Public Property Fax() As String` [R/W] Sets or returns the fax number. Field name: fax. Length: 50 characters.
- `Public Property FirstName() As String` [R/W] Sets or returns the employee first name. Field name: firstName. Mandatory property. Length: 50 characters.
- `Public Property Gender() As BoGenderTypes` [R/W] Sets or returns a valid value of BoGenderTypes type that specifies the employee gender type. Field name: sex.
- `Public Property HealthInsuranceCode() As String` [R/W] The health insurance code of the employee. Field name: HeaInsCode. Length: 50 characters.
- `Public Property HealthInsuranceName() As String` [R/W] The health insurance name of the employee. Field name: HeaInsName. Length: 50 characters.
- `Public Property HealthInsuranceType() As String` [R/W] Indicate the type of the employee's health insurance. - AOK - Allgemeine Ortskrankenkasse (AOK) - IKK - Innungskrankenkasse (IKK) - EKK - Ersatzkasse (EKK) - BKK - Betriebskrankenkasse (BKK) - BKS - Bundesknappschaft (BKS) - LKK - Landeskrankenkasse (LKK) Field name: HeaInsType. Length: 20 characters.
- `Public Property HomeBlock() As String` [R/W] Sets or returns the block of the home address. Field name: homeBlock. Length: 100 characters.
- `Public Property HomeBuildingFloorRoom() As String` [R/W] Sets or returns additional details of the home address, such as building number, floor number, and room number. Field name: HomeBuild. Length: 64,000 characters.
- `Public Property HomeCity() As String` [R/W] Sets or returns the city of the home address. Field name: homeCity. Length: 100 characters.
- `Public Property HomeCountry() As String` [R/W] Sets or returns the country of the home address. Field name: homeCountr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property HomeCounty() As String` [R/W] Sets or returns the county part of the home address. Field name: homeCounty. Length: 100 characters.
- `Public Property HomePhone() As String` [R/W] Sets or returns the home phone number. Field name: homeTel. Length: 50 characters.
- `Public Property HomeState() As String` [R/W] Sets or returns the state of the home address. Field name: homeState. Length: 3 characters. This is a foreign key to the Countries table (OCST - not exposed through the DI API).
- `Public Property HomeStreet() As String` [R/W] Sets or returns the street of the home address. Field name: homeStreet. Length: 100 characters.
- `Public Property HomeStreetNumber() As String` [R/W] property HomeStreetNumber
- `Public Property HomeZipCode() As String` [R/W] Sets or returns the zip code of the home address. Field name: homeZip. Length: 20 characters.
- `Public Property IdNumber() As String` [R/W] Sets or returns the personal ID number of the employee (such as, government ID number or social security number). Field name: govID. Length: 20 characters.
- `Public Property IDType() As String` [R/W] property IDType
- `Public Property IncomeTaxLiability() As String` [R/W] Indicate the income tax liability code: 1 - Unlimited 2 - Restricted 3 - Flat-rate tax 4 - Not liable Field: InTaxLiabi.
- `Public Property JobTitle() As String` [R/W] Sets or returns the employee job title. Field name: jobTitle. Length: 20 characters.
- `Public Property JobTitleCode() As String` [R/W] The job title of the employee. Field name: JTCode. Length: 5 characters.
- `Public Property LastName() As String` [R/W] Sets or returns the employee last name. Field name: lastName. Mandatory property. Length: 50 characters.
- `Public Property LegalRepresentative() As BoYesNoEnum` [R/W] property LegalRepresentative
- `Public Property LinkedVendor() As String` [R/W] property LinkedVendor
- `Public Property Manager() As Long` [R/W] Sets or returns the manager's employee-ID of the employee. Field name: manager. This is a key to the OHEM object.
- `Public Property MartialStatus() As BoMeritalStatuses` [R/W] Sets or returns a valid value of BoMeritalStatuses type that specifies the merital status. Field name: martStatus.
- `Public Property MiddleName() As String` [R/W] Sets or returns the employee middle name. Field name: middleName. Length: 50 characters.
- `Public Property MobilePhone() As String` [R/W] Sets or returns the mobile phone number. Field name: mobile. Length: 50 characters.
- `Public Property MunicipalityKey() As String` [R/W] The key of the municipality to which the employee belongs. Field name: MunKey. Length: 20 characters.
- `Public Property NumOfChildren() As Long` [R/W] Sets or returns the number of children. Field name: nChildren.
- `Public Property OfficeExtension() As String` [R/W] Sets or returns the extension of the office phone number. Field name: officeExt. Length: 50 characters.
- `Public Property OfficePhone() As String` [R/W] Sets or returns the office phone number. Field name: officeTel. Length: 50 characters.
- `Public Property Pager() As String` [R/W] Sets or returns the pager number. Field name: pager. Length: 50 characters.
- `Public Property PartnerReligion() As String` [R/W] Indicates the religion of the employee's spouse. -- - No church tax liability AK - Old catholic EV - Protestant FA - Non-denomination Alzey FB - Non-denominational regional congregation Baden FG - Non-denominational regional congregation Palatinate FM - Non-denominational congregation Mainz FR - French-reformed FS - Non-denominational congregation Offenbach/Mainz IB - Israelite Religious Community Baden IL - Israelite Rural IS - Israelite IW - Israelite religious community Wuerttemberg JD - Jewish religion tax JH - Jewish religion tax JS - Jewish religion tax LT - Lutheran RF - Reformed RK - Roman catholic Field: RelPartner.
- `Public Property PassportExpirationDate() As Date` [R/W] Sets or returns the expiration date of the passport. Field name: passportEx.
- `Public Property PassportIssueDate() As Date` [R/W] property PassportIssueDate
- `Public Property PassportIssuer() As String` [R/W] property PassportIssuer
- `Public Property PassportNumber() As String` [R/W] Sets or returns the employee passport number. Field name: passportNo. Length: 20 characters.
- `Public Property PaymentMethod() As EmployeePaymentMethodEnum` [R/W] The payment method of the employee. Field name: PymMeth.
- `Public Property PersonGroup() As String` [R/W] The person group of the employee. 101 - Social insurance obliged without characteristic 102 - Apprentice 104 - Home worker 105 - Trainee 106 - Student 108 - Early retirement 109 - Part time occupied employee 110 - Short time occupied 112 - Family related person agriculture 113 - Additio. income agriculture 114 - Additio. income agriculture seasonal 116 - Receiver of clearing cash 118 - Unregular occupied 119 - Pensioner 997 - Not specified Field: PersGroup.
- `Public Property Picture() As String` [R/W] Sets or returns the picture file name (without the path). Field name: picture. Length: 200 characters.
  - remarks: All picture files must be stored in the /Bitmaps sub-directory of SAP Business One. The following are supported formats: JPG, BMP, PNG, PCX.
- `Public Property Position() As Long` [R/W] Sets or returns a value that specifies the employee position. This property This is a foreign key to OHPS table, which is not exposed through the DI API. Field name: Position.
- `Public Property PreviousEmpoymentInfo() As EmployeePrevEmpoymentInfo` [R] Returns the EmployeePrevEmpoymentInfo object.
- `Public Property PreviousPRWebAccess() As BoYesNoEnum` [R] property PreviousPRWebAccess
- `Public Property ProfessionStatus() As String` [R/W] The profession of the employee. 0 - Trainee 1 - Worker 2 - Skilled Worker 3 - Supervisor/Foreman 4 - Clerk 5 - Youthhelp/Sheltered Workshop 6 - Participation for profession focused measures 7 - Homeworker 8 - Part time < 18 hrs 9 - Part time > 18 hrs Field: StatusOfP.
- `Public Property PRWebAccess() As BoYesNoEnum` [R/W] property PRWebAccess
- `Public Property QualificationCode() As SPEDContabilQualificationCodeEnum` [R/W] property QualificationCode
- `Public Property Religion() As String` [R/W] Indicates the religion of the employee. -- - No church tax liability AK - Old catholic EV - Protestant FA - Non-denomination Alzey FB - Non-denominational regional congregation Baden FG - Non-denominational regional congregation Palatinate FM - Non-denominational congregation Mainz FR - French-reformed FS - Non-denominational congregation Offenbach/Mainz IB - Israelite Religious Community Baden IL - Israelite Rural IS - Israelite IW - Israelite religious community Wuerttemberg JD - Jewish religion tax JH - Jewish religion tax JS - Jewish religion tax LT - Lutheran RF - Reformed RK - Roman catholic Field: EmTaxCCode.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks on the employee. Field name: remark. Length: 64,000 characters.
- `Public Property ReviewsInfo() As EmployeeReviewsInfo` [R] Returns the EmployeeReviewsInfo object.
- `Public Property Salary() As Double` [R/W] Sets or returns the employee salary. Field name: salary.
- `Public Property SalaryCurrency() As String` [R/W] Sets or returns the currency of the salary. Field name: salaryCurr. Length: 3 characters.
- `Public Property SalaryUnit() As BoSalaryCostUnits` [R/W] Sets or returns a valid value of BoSalaryCostUnits type that specifies the salary unit (for example: per hour, per day, per month, and so on). Field name: salaryUnit.
- `Public Property SalesPersonCode() As Long` [R/W] Sets or returns the sales person code. Field name: salesPrson. This is a foreign key to the SalesPersons Object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property SavingsPaymentInfo() As EmployeeSavingsPaymentInfo` [R] Returns the EmployeeSavingsPaymentInfo child object.
- `Public Property SocialInsuranceNumber() As String` [R/W] The social insurance number of the employee. Field name: SInsurNum. Length: 20 characters.
- `Public Property SpouseFirstName() As String` [R/W] The first name of the employee's spouse. Field name: FNameSP. Length: 50 characters.
- `Public Property SpouseSurname() As String` [R/W] The surname of the employee's spouse. Field name: SurnameSP. Length: 50 characters.
- `Public Property StartDate() As Date` [R/W] Sets or returns the date when the employee started the work in the company. Field name: startDate.
- `Public Property StatusCode() As Long` [R/W] Sets or returns the employee status code. Field name: status.
- `Public Property STDCode() As Long` [R/W] property STDCode
- `Public Property TaxClass() As String` [R/W] Indicates the tax class of the employee: 1 - Tax Class I 2 - Tax Class II 3 - Tax Class III 4 - Tax Class IV 5 - Tax Class V 6 - Tax Class VI Field name: TaxClass.
- `Public Property TaxOfficeName() As String` [R/W] The tax office name of the employee. Field name: TaxOName. Length: 50 characters.
- `Public Property TaxOfficeNumber() As String` [R/W] The tax office number of the employee. Field name: TaxONum. Length: 20 characters.
- `Public Property TerminationDate() As Date` [R/W] Sets or returns the date when the employee terminated the work in the company. Field name: termDate.
- `Public Property TreminationReason() As Long` [R/W] Sets or returns the termination reason. Field name: termReason. This is a foreign key to the Termination Reason table (OHTR - not exposed through the DI API).
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Date` [R] property UpdateTime
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VacationCurrentYear() As Long` [R/W] The employee's vacation information of the current year. Field name: VacCurYear. Length: 3 characters.
- `Public Property VacationPreviousYear() As Long` [R/W] The employee's vacation information of the previous year. Field name: VacPreYear. Length: 3 characters.
- `Public Property WorkBlock() As String` [R/W] Sets or returns the block of the workplace address. Field name: workBlock. Length: 100 characters.
- `Public Property WorkBuildingFloorRoom() As String` [R/W] Sets or returns additional details of the workplace address, such as building number, floor number, and room number. Field name: WorkBuild. Length: 64,000 characters.
- `Public Property WorkCity() As String` [R/W] Sets or returns the city of the workplace address. Field name: workCity. Length: 100 characters.
- `Public Property WorkCountryCode() As String` [R/W] Sets or returns the country of the workplace address. Field name: workCountr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property WorkCounty() As String` [R/W] Sets or returns the county of the workplace address. Field name: workCounty. Length: 100 characters.
- `Public Property WorkStateCode() As String` [R/W] Sets or returns the state of the workplace address. Field name: workState. Length: 3 characters. This is a foreign key to the States table (OCST - not exposed through the DI API).
- `Public Property WorkStreet() As String` [R/W] Sets or returns the street of the workplace address. Field name: workStreet. Length: 100 characters.
- `Public Property WorkStreetNumber() As String` [R/W] property WorkStreetNumber
- `Public Property WorkZipCode() As String` [R/W] Sets or returns the zip code of the workplace address. Field name: workZip. Length: 20 characters.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal EmployeeID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `EmployeeID`: Specifies the employee ID in the database.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
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
