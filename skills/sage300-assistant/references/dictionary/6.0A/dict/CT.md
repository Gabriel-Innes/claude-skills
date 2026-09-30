# CT module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## CTR1PD - Paper R1 Information (view CT0007)
Keys (first = PK; D=dups allowed, M=modifiable): SORTPARAM+SEQUENCE
Fields (NAME type description [values]):
  SORTPARAM String*94 Sort Parameter
  SEQUENCE Integer Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EMPLRACCNO String*20 Employer Account Number
  EMPLRNAME String*60 Employer Name
  EMPLRADDR1 String*60 Employer Address 1
  EMPLRADDR2 String*60 Employer Address 2
  EMPLRADDR3 String*60 Employer Address 3
  EMPLRADDR4 String*60 Employer Address 4
  EMPLRCITY String*30 Employer City
  EMPLRSTATE String*30 Employer Province
  EMPLRZIP String*20 Employer Postal Code
  EMPLOYEE String*12 Employee ID
  SSN String*11 Employee SIN
  LASTNAME String*20 Employee Last Name
  FIRSTNAME String*15 Employee First Name
  MIDDLENAME String*15 Employee Middle Name
  ADDRESS1 String*60 Employee Address 1
  ADDRESS2 String*60 Employee Address 2
  ADDRESS3 String*60 Employee Address 3
  ADDRESS4 String*60 Employee Address 4
  CITY String*30 Employee City
  STATE String*30 Employee Province
  ZIP String*20 Employee Postal Code
  WAGESTIPS BCD*10.3 Employee Income
  QPENSIONC BCD*10.3 QPP Contributions
  UIPREMIUM BCD*10.3 EI Premium
  RPENSIONC BCD*10.3 Registered Pension Plan Deduction
  INCOMETAX BCD*10.3 Income Tax Deducted
  UNIONDUES BCD*10.3 Unions Dues Deduction
  QPPEARNING BCD*10.3 QPP Pensionable Earnings
  HOUSINGBEN BCD*10.3 Housing, Board, Lodging
  COAUTOBEN BCD*10.3 Personal Use of Employer's Auto
  HEALTHBEN BCD*10.3 Private Health Plan Benefit
  TRAVELBEN BCD*10.3 Travel in Designated Areas
  OTHERBEN BCD*10.3 Other Taxable Allowances/Benefits
  COMMISSION BCD*10.3 Employment Commissions
  CHARITYDED BCD*10.3 Charitable Contribution Deductions
  OTHEREARN BCD*10.3 Other Taxable Income
  MULTEMPINS BCD*10.3 Multi-Employer Insuance Plan Contrib.
  DEFEREARN BCD*10.3 Deferred Earnings
  INDIANPAY BCD*10.3 Indian Pay
  TIPS BCD*10.3 Tips
  ALLOCTIPS BCD*10.3 Allocated Tips
  RETIREMENT BCD*10.3 Phased Retirement
  NOTES String*250 Notes
  COUNTRY String*30 Country
  ER1BOX Integer O-Code Box
  EFILENO String*9 eFile Number
  CPENSIONC BCD*10.3 CPP Contributions
  BOXGBLANK Boolean Box G is blank
  RL1NO String*9 RL1 Slip Number
  PIPEARNING BCD*10.3 Parental Insurance Earnings
  PIPPREMIUM BCD*10.3 Parental Insurance Premium
  RECORDTYPE Integer Record Type
  ORGEFILENO String*9 Original EFile Number

## CTROED - Record of Employment Detail (view CT0055)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+DATESORT+UIENDDATE+CHECKDATE+ENTRYSEQ
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee ID
  DATESORT Long Date Sorting
  UIENDDATE Date EI Period End Date
  CHECKDATE Date Cheque Date
  ENTRYSEQ Long Entry Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INSEARNING BCD*10.3 Insurable Earnings in PP
  INSHOURS BCD*4.3 Insurable Hours in PP
  PPINSWEEKS BCD*4.3 Insurable Weeks in PP
  PAYFREQ Integer Pay Frequency
  EXCEPTION Boolean Exception Record
  COMMENTRY Integer Comment Entry
  PRTONROE Boolean Print on ROE
  INSEARNPRT BCD*10.3 Ins. Earnings Printed on ROE
  PPEXCPRT BCD*4.3 Exception Entry Printed on ROE

## CTROEH - Record of Employment Header (view CT0054)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMENDEDNBR String*20 Amended or Replaced Serial No.
  RREFERNBR String*20 Employer Payroll Reference No.
  COMPANYNAM String*60 Company Name
  CADDRESS1 String*60 Company Address 1
  CADDRESS2 String*60 Company Address 2
  CADDRESS3 String*60 Company Address 3
  CADDRESS4 String*60 Company Address 4
  CCITY String*30 Company Address City
  CPROVINCE String*30 Company Address Province
  CPOSTALC String*20 Company Postal Code
  RCTID String*20 CCRA Business No. (BN)
  LANGUAGE Integer Communication Preferred in [1=English,2=French]
  PAYFREQ Integer Pay Period Type [2=Daily,3=Weekly,4=Biweekly,5=Semimonthly,10=22 pay periods,9=13 pay periods,6=Monthly,8=10 pay periods]
  EMPNAME String*60 Employee Name
  EADDRESS1 String*60 Employee Address 1
  EADDRESS2 String*60 Employee Address 2
  EADDRESS3 String*60 Employee Address 3
  EADDRESS4 String*60 Employee Address 4
  ECITY String*30 Employee Address City
  EPROVINCE String*30 Employee Address Province
  COUNTRY String*30 Employee Country
  EPOSTALC String*20 Employee Postal Code
  POSITION String*25 Employee Occupation
  SIN String*11 Social Insurance Number
  FIRSTDAY Date First Day Worked
  LASTDAY Date Last Day Worked
  UIPAYTO Date EI Premiums Payable up to
  PPENDDATE Date Final Pay Period Ending Date
  ALLMAX Boolean Maximum for Each Pay Period
  UITOTEARN BCD*10.3 Total Insurable Earnings
  INSWEEKS Integer Insurable Weeks
  VACPAY BCD*10.3 Vacation Pay
  HOLDATE1 Date Holiday 1 Date
  HOLPAY1 BCD*10.3 Holiday 1 Pay
  HOLDATE2 Date Holiday 2 Date
  HOLPAY2 BCD*10.3 Holiday 2 Pay
  HOLDATE3 Date Holiday 3 Date
  HOLPAY3 BCD*10.3 Holiday 3 Pay
  OMONEY1D String*15 Other Money 1 Description
  OMONEY1 BCD*10.3 Other Money 1
  OMONEY2D String*15 Other Money 2 Description
  OMONEY2 BCD*10.3 Other Money 2
  OMONEY3D String*15 Other Money 3 Description
  OMONEY3 BCD*10.3 Other Money 3
  ALLOCATED Integer Allocated Details
  SICKSTART Date Payment Start Date for Sick
  SICKLENGTH Integer Sick Leave Length
  BEWEEKS Boolean Sick Leave Weeks/Days
  SICKAMT BCD*10.3 Amount of Sick Benifits
  ROEREASONS Integer Reasons for Issuing [1=A - Shortage of work,2=B - Strike or lock-out,3=C - Return to school,4=D - Illness or injury,5=E - Quit,6=F - Maternity,7=G - Retirement,8=H - Work Sharing,9=J - Apprentice training,10=M - Dismissal,11=N - Leave of absence,13=P - Parental,14=Z - Compassionate Care,12=K - Other]
  ROEREASON String*1 Reason for Issuing This ROE
  CONTACT String*60 For further Info. Contact
  TELEPHONE String*30 Phone No. to Contact
  RECALLDATE Date Expected Date of Recall
  NOTRETURN Boolean Not Returning
  UNKNOWN Boolean Unknown Date
  COMMENTS String*200 Comments
  ISSUERNAME String*60 Issuer Name
  ISSUEPHONE String*30 Issuer's Phone No.
  ISSUEDATE Date Date of Issue
  WHICHCNTRY Integer Which Country
  UITOTHRS BCD*4.3 EI Total Hrs
  UI96EARN BCD*10.3 Insurable Earnings for 1996
  BUSEUIDTL Boolean Print Insurable Earnings Detail?
  ROE53WEEKS Boolean 53 weeks ROE?
  USERID String*8 User ID

## CTT4PD - Paper T4 Information (view CT0005)
Keys (first = PK; D=dups allowed, M=modifiable): SORTPARAM+SEQUENCE
Fields (NAME type description [values]):
  SORTPARAM String*94 Sort Parameter
  SEQUENCE Integer Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EMPLRACCNO String*15 Employer Account Number
  EMPLRNAME String*60 Employer Name
  EMPLRADDR1 String*60 Employer Address 1
  EMPLRADDR2 String*60 Employer Address 2
  EMPLRADDR3 String*60 Employer Address 3
  EMPLRADDR4 String*60 Employer Address 4
  EMPLRCITY String*30 Employer City
  EMPLRSTATE String*30 Employer Province
  EMPLRZIP String*20 Employer Postal Code
  EMPLOYEE String*12 Employee ID
  SSN String*11 Employee SIN
  LASTNAME String*20 Employee Last Name
  FIRSTNAME String*15 Employee First Name
  MIDDLENAME String*15 Employee Middle Name
  ADDRESS1 String*60 Employee Address 1
  ADDRESS2 String*60 Employee Address 2
  ADDRESS3 String*60 Employee Address 3
  ADDRESS4 String*60 Employee Address 4
  CITY String*30 Employee City
  STATE String*30 Employee Province
  ZIP String*20 Employee Postal Code
  WAGESTIPS BCD*10.3 Employee Income
  CPENSIONC BCD*10.3 Pension Contributions - Canada plan
  QPENSIONC BCD*10.3 Pension Contributions - Quebec plan
  UIPREMIUM BCD*10.3 EI Premium
  RPENSIONC BCD*10.3 Registered Pension Plan Deduction
  INCOMETAX BCD*10.3 Income Tax Deducted
  UIEARNING BCD*10.3 EI Insurable Earnings
  CPPEARNING BCD*10.3 CPP Pensionable Earnings
  HOUSINGBEN BCD*10.3 Housing, Board, Lodging
  TRAVELBEN BCD*10.3 Travel in Designated Areas
  COAUTOBEN BCD*10.3 Personal Use of Employer's Auto
  LOANBEN BCD*10.3 Interest Free/Low Interest Loans
  STOCKBEN BCD*10.3 Stock Option Benefits
  OTHERBEN BCD*10.3 Other Taxable Allowances/Benefits
  COMMISSION BCD*10.3 Employment Commissions
  UNIONDUES BCD*10.3 Unions Dues Deduction
  CHARITYDED BCD*10.3 Charitable Contribution Deductions
  PENSIONADJ BCD*10.3 Pension Plan Adjustment
  STOCKBEND BCD*10.3 Stock Option and Shares Ded(110(1)(d))
  STOCKBEND1 BCD*10.3 Stock Option and Shares Ded(110(1)(d.1))
  INDIANPAY BCD*10.3 Status Indian
  EXEMPTCPP Boolean Exempt CPP/QPP
  EXEMPTUI Boolean Exempt EI
  RPPID String*9 Pension Plan Registration Number (RPP)
  EMPPROV String*2 Province of Employment
  NOTES String*250 Notes
  COUNTRY String*30 Country
  WCBREPAID BCD*10.3 WCB Repaid
  RCPENSION BCD*10.3 Employer's CPP Contributions
  RUIPREMIUM BCD*10.3 Employer's UI premiums
  PPIPTAX BCD*10.3 Provincial Parental Insurance Plan
  PPIPEARN BCD*10.3 PPIP Insurable Earnings
  EXEMPTPPIP Boolean Exempt PPIP
  MEDITRAVEL BCD*10.3 Medical Travel
  TRANSPASS BCD*10.3 Public Transit Pass
  FISHGROSS BCD*10.3 Fishers, Gross Income
  FISHNET BCD*10.3 Fishers, Net Income
  FISHSHARE BCD*10.3 Fishers, Shared Income
  OFFICEREXP BCD*10.3 Officer's expense Allowance
  EMPAGENCY BCD*10.3 Employment Agency
  TAXIDRIVER BCD*10.3 Taxi Driver
  BARBER BCD*10.3 Barbers and Hairdressers
  HEALTHPLAN BCD*10.3 Private Health Plan
  EMPCODE String*2 Employment Code
  OTHBOX1 String*2 Other Box 1
  OTHAMT1 BCD*10.3 Other Amount 1
  OTHBOX2 String*2 Other Box 2
  OTHAMT2 BCD*10.3 Other Amount 2
  OTHBOX3 String*2 Other Box 3
  OTHAMT3 BCD*10.3 Other Amount 3
  OTHBOX4 String*2 Other Box 4
  OTHAMT4 BCD*10.3 Other Amount 4
  OTHBOX5 String*2 Other Box 5
  OTHAMT5 BCD*10.3 Other Amount 5
  OTHBOX6 String*2 Other Box 6
  OTHAMT6 BCD*10.3 Other Amount 6
  OTHBOX7 String*2 Other Box 7
  OTHAMT7 BCD*10.3 Other Amount 7
  OTHBOX8 String*2 Other Box 8
  OTHAMT8 BCD*10.3 Other Amount 8
  OTHBOX9 String*2 Other Box 9
  OTHAMT9 BCD*10.3 Other Amount 9
  OTHBOX10 String*2 Other Box 10
  OTHAMT10 BCD*10.3 Other Amount 10
  OTHBOX11 String*2 Other Box 11
  OTHAMT11 BCD*10.3 Other Amount 11
  OTHBOX12 String*2 Other Box 12
  OTHAMT12 BCD*10.3 Other Amount 12

## CTUTDA - Update TD1 Claim Audit (view CT0017)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXID String*6 Tax
  TAXDESC String*60 Tax Description
  RUNDATE Date Run Date
  SELTYPE Integer Employee Selection Type [0=Employee Number,1=Class,2=Selection List,3=Set Criteria]
  FROMEMP String*12 From Employee
  TOEMP String*12 To Employee
  EMPLISTID String*8 Selection List
  CLASS Integer Class [1=Class 1,2=Class 2,3=Class 3,4=Class 4]
  FCLASSCOD String*6 From Class Code
  TCLASSCOD String*6 To Class Code
  EMPFILTER String*250 Employee Browse Filter
  CHANGETYPE Integer Change By [0=Cost of Living Factor,1=Amount Increase/Decrease]
  CHANGEAMT BCD*10.3 Amount
  IDXFACTOR BCD*9.5 Percent
  EMPUPDATED Long Employees Updated
  ORGUSERID String*8 Original User ID

## CTUTDAD - Update TD1 Claim Audit Details (view CT0018)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+EMPLOYEE
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  EMPLOYEE String*12 Employee
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EMPLNAME String*60 Employee Name
  OLDTD1AMT BCD*10.3 Old TD1 Claim Amt
  NEWTD1AMT BCD*10.3 New TD1 Claim Amt
