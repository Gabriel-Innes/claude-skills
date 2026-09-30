# UT module - compiled AOM dictionary

## UTAULE - Local Tax Update EE Audit Header (view UT0034)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RUNDATE Date Update Run Date
  OPERATION Integer Operation

## UTAULED - Local Tax Update EE Audit Detail (view UT0035)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+EMPLOYEE+TAXID+FIELDIDX
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence Number
  EMPLOYEE String*12 Employee
  TAXID String*6 Tax
  FIELDIDX Long Field Index
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EMPLNAME String*60 Employee Name
  TAXDESC String*60 Tax Description
  FIELDNAME String*10 Field Name
  ECALCMTHD Integer Employee Calculation Method
  RCALCMTHD Integer Employer Calculation Method
  OLDVALUE String*60 Old Field Value
  NEWVALUE String*60 New Field Value

## UTAULT - Local Tax Update Audit Header (view UT0017)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXID String*6 Tax
  TAXDESC String*60 Tax Description
  ECALCMTHD Integer Employee Calculation Method
  RCALCMTHD Integer Employer Calculation Method
  ELIMITON Integer Employee Limit
  RLIMITON Integer Employer Limit
  ECLCMINWRK Boolean Employee Minimum Weeks Worked
  RCLCMINWRK Boolean Employer Minimum Weeks Worked
  RUNDATE Date Update Run Date
  OPERATION Integer Operation

## UTAULTD - Local Tax Update Audit Detail (view UT0018)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+TAXID+FIELDIDX
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence Number
  TAXID String*6 Tax
  FIELDIDX Long Field Index
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FIELDNAME String*10 Field Name
  OLDVALUE String*60 Old Field Value
  NEWVALUE String*60 New Field Value

## UTESID - Employee Suppl. Info Details (view UT0015)
Keys (first = PK; D=dups allowed, M=modifiable): REPORTAUTH+EMPLOYEE
Fields (NAME type description [values]):
  REPORTAUTH String*6 Report Authority ID
  EMPLOYEE String*12 Employee
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COUNTYLIVE String*2 County Code
  COUNTYTAX String*6 County Tax ID
  OFFICER Boolean Corporate Officer [0=No,1=Yes]
  SEASONAL Boolean Seasonal [0=No,1=Yes]
  PROBATION Boolean Probationary [0=No,1=Yes]
  WAGEPLAN String*1 Wage Plan Code
  PLANTCODE String*15 Plant/Location Code
  UNITNUMBER String*10 Unit Number
  COUNTYWORK String*3 Worksite County Code
  INDUSTCODE String*6 Industry Code
  OCCUPCODE String*10 Occupational Code
  GEOCODE String*2 Geographic Code
  HOURLYEMP Boolean Hourly Employee [0=No,1=Yes]
  HOURLYWAGE BCD*10.3 Hourly Wages
  SEASONCODE String*2 Seasonal Code
  LOCALCODE1 String*4 School District Code 1
  LOCALTAX1 String*6 Local Tax ID 1
  LOCALCODE2 String*4 School District Code 2
  LOCALTAX2 String*6 Local Tax ID 2
  LOCALCODE3 String*4 School District Code 3
  LOCALTAX3 String*6 Local Tax ID 3
  LOCALCODE4 String*4 School District Code 4
  LOCALTAX4 String*6 Local Tax ID 4
  LOCALCODE5 String*4 School District Code 5
  LOCALTAX5 String*6 Local Tax ID 5
  FAMILYSTAT String*1 Family Status
  LASTNAME2 String*16 2nd Last Name
  ADJUSTCODE String*1 Adjustment Reason Code
  WORKRLCODE String*1 Worker Relationship Code
  WAGETYPE Integer Wage Type [1=]
  LTERMCARE Boolean WA Cares Exemption [0=No,1=Yes]

## UTESIH - Employee Suppl. Info Headers (view UT0014)
Keys (first = PK; D=dups allowed, M=modifiable): REPORTAUTH; REPORTTYPE+REPORTAUTH
Fields (NAME type description [values]):
  REPORTAUTH String*6 Report Authority ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RPTAUTHDSC String*60 Description
  REPORTTYPE Integer Report Type [2=Qtrly PFML & Cares,3=Qtrly Wage on Disk(ette),4=W-2s on Disk(ette)]
  LASTMAINT Date Last Maintained
  COUNTYLIVE String*2 County Code
  COUNTYTAX String*6 County Tax ID
  RPTBLS3020 Boolean Report Multiple Worksite Data
  OFFICER Boolean Corporate Officer
  SEASONAL Boolean Seasonal
  PROBATION Boolean Probationary
  WAGEPLAN String*1 Wage Plan Code
  PLANTCODE String*15 Plant/Location Code
  UNITNUMBER String*10 Unit Number
  COUNTYWORK String*3 Worksite County Code
  INDUSTCODE String*6 Industry Code
  OCCUPCODE String*10 Occupational Code
  GEOCODE String*2 Geographic Code
  HOURLYEMP Boolean Hourly Employee
  HOURLYWAGE BCD*10.3 Hourly Wages
  SEASONCODE String*2 Seasonal Code
  LOCALCODE String*4 School District Code
  LOCALTAX String*6 Local Tax ID
  FAMILYSTAT String*1 Family Status
  LASTNAME2 String*16 2nd Last Name
  ADJUSTCODE String*1 Adjustment Reason Code
  WORKRLCODE String*1 Worker Relationship Code
  WAGETYPE Integer Wage Type [2=]
  LTERMCARE Boolean WA Cares Exemption

## UTI941 - 941 Information (view UT0009)
Keys (first = PK; D=dups allowed, M=modifiable): YEAR941+QUARTER941
Fields (NAME type description [values]):
  YEAR941 Integer Year
  QUARTER941 Integer Quarter
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STATUS Integer Status
  NUMOFEMPS Long Number of Employees
  TTLWAGES BCD*10.3 Earnings subject to FIT
  TTLTAXWH BCD*10.3 Total FIT Tax Withheld
  INCTAXADJ BCD*10.3 FIT adjustment from previous reports
  ADJINTXWH BCD*10.3 Adjusted total of FIT withheld
  SSWAGES BCD*10.3 Earnings subject to Soc. Sec.
  SSTAX BCD*10.3 Tax on Soc. Sec. Wages
  SSTIPS BCD*10.3 Tips subject to Soc. Sec.
  SSTAXONTIP BCD*10.3 Tax on Soc. Sec. Tips
  MEDWAGES BCD*10.3 Earnings subject to Medicare
  MEDTAX BCD*10.3 Tax on Medicare Earnings
  SUMOFCALC BCD*10.3 Total Soc. Sec. and Medicare Taxes
  SUBJECTTO Boolean Wages are not subject to SS/Med
  SICKPAY BCD*10.3 Sick Pay
  FRACTIONS BCD*10.3 Fractions
  OTHER BCD*10.3 Earnings
  SSMEDADJ BCD*10.3 Adjustment of Soc. Sec. and Medicare Taxes
  ADJUSTED BCD*10.3 Adjusted Total of Soc. Sec. and Medicare Taxes
  TTLTAX BCD*10.3 Total Taxes
  TTLADVEIC BCD*10.3 Advance EIC payments
  NETTAXES BCD*10.3 Net Taxes
  TTLDEPOSIT BCD*10.3 Deposits for Quarter
  BALANCEDUE BCD*10.3 Balance Due
  OVERPAYMNT BCD*10.3 Overpayment
  APLYOVRPAY Integer Apply Overpayment to next 941
  CALC941 Boolean Calculate the 941
  MEDPCNT BCD*9.5 Medicare Tax Percent
  SSPCNT BCD*9.5 Soc. Sec. Tax Percent
  TTLMONTH1 BCD*10.3 Total Liability - Month 1
  TTLMONTH2 BCD*10.3 Total Liability - Month 2
  TTLMONTH3 BCD*10.3 Total Liability - Month 3
  TTLQUARTER BCD*10.3 Total Liability - Quarter
  TTLMONTH1A BCD*10.3 Total Liability - Month 1
  TTLMONTH2A BCD*10.3 Total Liability - Month 2
  TTLMONTH3A BCD*10.3 Total Liability - Month 3
  TTLQUARTRA BCD*10.3 Total Liability - Quarter
  MNTH1DAY01 BCD*10.3 Liability - Month 1, Day 1
  MNTH1DAY02 BCD*10.3 Liability - Month 1, Day 2
  MNTH1DAY03 BCD*10.3 Liability - Month 1, Day 3
  MNTH1DAY04 BCD*10.3 Liability - Month 1, Day 4
  MNTH1DAY05 BCD*10.3 Liability - Month 1, Day 5
  MNTH1DAY06 BCD*10.3 Liability - Month 1, Day 6
  MNTH1DAY07 BCD*10.3 Liability - Month 1, Day 7
  MNTH1DAY08 BCD*10.3 Liability - Month 1, Day 8
  MNTH1DAY09 BCD*10.3 Liability - Month 1, Day 9
  MNTH1DAY10 BCD*10.3 Liability - Month 1, Day 10
  MNTH1DAY11 BCD*10.3 Liability - Month 1, Day 11
  MNTH1DAY12 BCD*10.3 Liability - Month 1, Day 12
  MNTH1DAY13 BCD*10.3 Liability - Month 1, Day 13
  MNTH1DAY14 BCD*10.3 Liability - Month 1, Day 14
  MNTH1DAY15 BCD*10.3 Liability - Month 1, Day 15
  MNTH1DAY16 BCD*10.3 Liability - Month 1, Day 16
  MNTH1DAY17 BCD*10.3 Liability - Month 1, Day 17
  MNTH1DAY18 BCD*10.3 Liability - Month 1, Day 18
  MNTH1DAY19 BCD*10.3 Liability - Month 1, Day 19
  MNTH1DAY20 BCD*10.3 Liability - Month 1, Day 20
  MNTH1DAY21 BCD*10.3 Liability - Month 1, Day 21
  MNTH1DAY22 BCD*10.3 Liability - Month 1, Day 22
  MNTH1DAY23 BCD*10.3 Liability - Month 1, Day 23
  MNTH1DAY24 BCD*10.3 Liability - Month 1, Day 24
  MNTH1DAY25 BCD*10.3 Liability - Month 1, Day 25
  MNTH1DAY26 BCD*10.3 Liability - Month 1, Day 26
  MNTH1DAY27 BCD*10.3 Liability - Month 1, Day 27
  MNTH1DAY28 BCD*10.3 Liability - Month 1, Day 28
  MNTH1DAY29 BCD*10.3 Liability - Month 1, Day 29
  MNTH1DAY30 BCD*10.3 Liability - Month 1, Day 30
  MNTH1DAY31 BCD*10.3 Liability - Month 1, Day 31
  MNTH2DAY01 BCD*10.3 Liability - Month 2, Day 1
  MNTH2DAY02 BCD*10.3 Liability - Month 2, Day 2
  MNTH2DAY03 BCD*10.3 Liability - Month 2, Day 3
  MNTH2DAY04 BCD*10.3 Liability - Month 2, Day 4
  MNTH2DAY05 BCD*10.3 Liability - Month 2, Day 5
  MNTH2DAY06 BCD*10.3 Liability - Month 2, Day 6
  MNTH2DAY07 BCD*10.3 Liability - Month 2, Day 7
  MNTH2DAY08 BCD*10.3 Liability - Month 2, Day 8
  MNTH2DAY09 BCD*10.3 Liability - Month 2, Day 9
  MNTH2DAY10 BCD*10.3 Liability - Month 2, Day 10
  MNTH2DAY11 BCD*10.3 Liability - Month 2, Day 11
  MNTH2DAY12 BCD*10.3 Liability - Month 2, Day 12
  MNTH2DAY13 BCD*10.3 Liability - Month 2, Day 13
  MNTH2DAY14 BCD*10.3 Liability - Month 2, Day 14
  MNTH2DAY15 BCD*10.3 Liability - Month 2, Day 15
  MNTH2DAY16 BCD*10.3 Liability - Month 2, Day 16
  MNTH2DAY17 BCD*10.3 Liability - Month 2, Day 17
  MNTH2DAY18 BCD*10.3 Liability - Month 2, Day 18
  MNTH2DAY19 BCD*10.3 Liability - Month 2, Day 19
  MNTH2DAY20 BCD*10.3 Liability - Month 2, Day 20
  MNTH2DAY21 BCD*10.3 Liability - Month 2, Day 21
  MNTH2DAY22 BCD*10.3 Liability - Month 2, Day 22
  MNTH2DAY23 BCD*10.3 Liability - Month 2, Day 23
  MNTH2DAY24 BCD*10.3 Liability - Month 2, Day 24
  MNTH2DAY25 BCD*10.3 Liability - Month 2, Day 25
  MNTH2DAY26 BCD*10.3 Liability - Month 2, Day 26
  MNTH2DAY27 BCD*10.3 Liability - Month 2, Day 27
  MNTH2DAY28 BCD*10.3 Liability - Month 2, Day 28
  MNTH2DAY29 BCD*10.3 Liability - Month 2, Day 29
  MNTH2DAY30 BCD*10.3 Liability - Month 2, Day 30
  MNTH2DAY31 BCD*10.3 Liability - Month 2, Day 31
  MNTH3DAY01 BCD*10.3 Liability - Month 3, Day 1
  MNTH3DAY02 BCD*10.3 Liability - Month 3, Day 2
  MNTH3DAY03 BCD*10.3 Liability - Month 3, Day 3
  MNTH3DAY04 BCD*10.3 Liability - Month 3, Day 4
  MNTH3DAY05 BCD*10.3 Liability - Month 3, Day 5
  MNTH3DAY06 BCD*10.3 Liability - Month 3, Day 6
  MNTH3DAY07 BCD*10.3 Liability - Month 3, Day 7
  MNTH3DAY08 BCD*10.3 Liability - Month 3, Day 8
  MNTH3DAY09 BCD*10.3 Liability - Month 3, Day 9
  MNTH3DAY10 BCD*10.3 Liability - Month 3, Day 10
  MNTH3DAY11 BCD*10.3 Liability - Month 3, Day 11
  MNTH3DAY12 BCD*10.3 Liability - Month 3, Day 12
  MNTH3DAY13 BCD*10.3 Liability - Month 3, Day 13
  MNTH3DAY14 BCD*10.3 Liability - Month 3, Day 14
  MNTH3DAY15 BCD*10.3 Liability - Month 3, Day 15
  MNTH3DAY16 BCD*10.3 Liability - Month 3, Day 16
  MNTH3DAY17 BCD*10.3 Liability - Month 3, Day 17
  MNTH3DAY18 BCD*10.3 Liability - Month 3, Day 18
  MNTH3DAY19 BCD*10.3 Liability - Month 3, Day 19
  MNTH3DAY20 BCD*10.3 Liability - Month 3, Day 20
  MNTH3DAY21 BCD*10.3 Liability - Month 3, Day 21
  MNTH3DAY22 BCD*10.3 Liability - Month 3, Day 22
  MNTH3DAY23 BCD*10.3 Liability - Month 3, Day 23
  MNTH3DAY24 BCD*10.3 Liability - Month 3, Day 24
  MNTH3DAY25 BCD*10.3 Liability - Month 3, Day 25
  MNTH3DAY26 BCD*10.3 Liability - Month 3, Day 26
  MNTH3DAY27 BCD*10.3 Liability - Month 3, Day 27
  MNTH3DAY28 BCD*10.3 Liability - Month 3, Day 28
  MNTH3DAY29 BCD*10.3 Liability - Month 3, Day 29
  MNTH3DAY30 BCD*10.3 Liability - Month 3, Day 30
  MNTH3DAY31 BCD*10.3 Liability - Month 3, Day 31
  STATDPCODE String*2 State
  ADDRCHANGE Boolean Changed Address
  NAME String*60 Name
  TRADENAME String*60 Trade Name
  ADDRESS1 String*60 Address 1
  ADDRESS2 String*60 Address 2
  ADDRESS3 String*60 Address 3
  ADDRESS4 String*60 Address 4
  CITY String*30 City
  COUNTRY String*30 Country
  STATE String*30 State/Province
  ZIP String*20 Zip Code/Postal Code
  QRTEND Date Date Quarter Ended
  EIN String*20 Employee Identification Number
  NOFUTURE Boolean Future Filing
  LASTDATE Date Date of Final Filing
  SEASONAL Boolean Seasonal Employer
  SEMIWKLY Boolean Semiweekly Depositor
  MONTHLY Boolean Monthly Depositor
  PRIORSSMED BCD*10.3 Prior quarter's social security and Medicare taxes
  ADDFIT BCD*10.3 Special additions to federal income tax
  ADDSSMED BCD*10.3 Special additions to social security and Medicare
  COBRAPMT BCD*10.3 COBRA premium assistance payments
  NOFCOBRAS Long Number of individuals provided COBRA premium assistance
  TDEPCOBRA BCD*10.3 Add lines 11 and 12a
  UNRPTTIPS BCD*10.3 Tax due on unreported tips
  HMEDPCNT BCD*9.5 Excess Medicare Tax Percent
  HMEDWAGES BCD*10.3 Excess Medicare Wage
  HMEDTAX BCD*10.3 Tax on Excess Medicare Wage
  FRGNADD Boolean Foreign Address

## UTLCTX - Local Tax Repository Table (view UT0016)
Keys (first = PK; D=dups allowed, M=modifiable): TAXID
Fields (NAME type description [values]):
  TAXID String*6 Tax
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXTYPE Integer Type
  LONGDESC String*60 Description
  ROUNDTAXSW Boolean Round Tax
  STDARDDED1 BCD*10.3 Standard Deduction
  EXMPTNAMT1 BCD*10.3 Amount per Exemption
  EXMPTCRSW Boolean Tax Credit Exemption switch
  ANNMAXERN BCD*10.3 Annual Maximum Earnings
  ANNUALMIN BCD*10.3 Annual Minimum Earnings
  W2BOXTYP Integer W2-Box Type
  W2WITHTAX String*6 Combine with Tax
  ECALCMTHD Integer Employee Calculation Method
  EAMTORPCT BCD*9.5 Employee Amount/Percent
  ELIMITON Integer Employee Limit
  EANNUALMAX BCD*10.3 Employee Annual Maximum
  EDAILYMIN BCD*10.3 Employee Daily Minimum
  EDAILYMAX BCD*10.3 Employee Daily Maximum
  EWEEKLYMIN BCD*10.3 Employee Weekly Minimum
  EWEEKLYMAX BCD*10.3 Employee Weekly Maximum
  EBIWKLYMIN BCD*10.3 Employee Biweekly Minimum
  EBIWKLYMAX BCD*10.3 Employee Biweekly Maximum
  ESEMIMNMIN BCD*10.3 Employee Semimonthly Minimum
  ESEMIMNMAX BCD*10.3 Employee Semimonthly Maximum
  EMNTHLYMIN BCD*10.3 Employee Monthly Minimum
  EMNTHLYMAX BCD*10.3 Employee Monthly Maximum
  EQRTRLYMIN BCD*10.3 Employee Quarterly Minimum
  EQRTRLYMAX BCD*10.3 Employee Quarterly Maximum
  E10PPPYMIN BCD*10.3 Employee 10 Pay Periods/Year Min
  E10PPPYMAX BCD*10.3 Employee 10 Pay Periods/Year Max
  E13PPPYMIN BCD*10.3 Employee 13 Pay Periods/Year Min
  E13PPPYMAX BCD*10.3 Employee 13 Pay Periods/Year Max
  E22PPPYMIN BCD*10.3 Employee 22 Pay Periods/Year Min
  E22PPPYMAX BCD*10.3 Employee 22 Pay Periods/Year Max
  RCALCMTHD Integer Employer Calculation Method
  RAMTORPCT BCD*9.5 Employer Amount/Percent
  RLIMITON Integer Employer Limit
  RANNUALMAX BCD*10.3 Employer Annual Maximum
  RDAILYMIN BCD*10.3 Employer Daily Minimum
  RDAILYMAX BCD*10.3 Employer Daily Maximum
  RWEEKLYMIN BCD*10.3 Employer Weekly Minimum
  RWEEKLYMAX BCD*10.3 Employer Weekly Maximum
  RBIWKLYMIN BCD*10.3 Employer Biweekly Minimum
  RBIWKLYMAX BCD*10.3 Employer Biweekly Maximum
  RSEMIMNMIN BCD*10.3 Employer Semimonthly Minimum
  RSEMIMNMAX BCD*10.3 Employer Semimonthly Maximum
  RMNTHLYMIN BCD*10.3 Employer Monthly Minimum
  RMNTHLYMAX BCD*10.3 Employer Monthly Maximum
  RQRTRLYMIN BCD*10.3 Employer Quarterly Minimum
  RQRTRLYMAX BCD*10.3 Employer Quarterly Maximum
  R10PPPYMIN BCD*10.3 Employer 10 Pay Periods/Year Min
  R10PPPYMAX BCD*10.3 Employer 10 Pay Periods/Year Max
  R13PPPYMIN BCD*10.3 Employer 13 Pay Periods/Year Min
  R13PPPYMAX BCD*10.3 Employer 13 Pay Periods/Year Max
  R22PPPYMIN BCD*10.3 Employer 22 Pay Periods/Year Min
  R22PPPYMAX BCD*10.3 Employer 22 Pay Periods/Year Max
  WGBRACK1 BCD*10.3 Wage Ceiling for Bracket 1
  WGADDAMT1 BCD*10.3 Tax Add Amount for Bracket 1
  WGPCTOVR1 BCD*5.5 Tax Percentage for Bracket 1
  WGBRACK2 BCD*10.3 Wage Ceiling for Bracket 2
  WGADDAMT2 BCD*10.3 Tax Add Amount for Bracket 2
  WGPCTOVR2 BCD*5.5 Tax Percentage for Bracket 2
  WGBRACK3 BCD*10.3 Wage Ceiling for Bracket 3
  WGADDAMT3 BCD*10.3 Tax Add Amount for Bracket 3
  WGPCTOVR3 BCD*5.5 Tax Percentage for Bracket 3
  WGBRACK4 BCD*10.3 Wage Ceiling for Bracket 4
  WGADDAMT4 BCD*10.3 Tax Add Amount for Bracket 4
  WGPCTOVR4 BCD*5.5 Tax Percentage for Bracket 4
  WGBRACK5 BCD*10.3 Wage Ceiling for Bracket 5
  WGADDAMT5 BCD*10.3 Tax Add Amount for Bracket 5
  WGPCTOVR5 BCD*5.5 Tax Percentage for Bracket 5
  WGBRACK6 BCD*10.3 Wage Ceiling for Bracket 6
  WGADDAMT6 BCD*10.3 Tax Add Amount for Bracket 6
  WGPCTOVR6 BCD*5.5 Tax Percentage for Bracket 6
  WGBRACK7 BCD*10.3 Wage Ceiling for Bracket 7
  WGADDAMT7 BCD*10.3 Tax Add Amount for Bracket 7
  WGPCTOVR7 BCD*5.5 Tax Percentage for Bracket 7
  WGBRACK8 BCD*10.3 Wage Ceiling for Bracket 8
  WGADDAMT8 BCD*10.3 Tax Add Amount for Bracket 8
  WGPCTOVR8 BCD*5.5 Tax Percentage for Bracket 8
  WGBRACK9 BCD*10.3 Wage Ceiling for Bracket 9
  WGADDAMT9 BCD*10.3 Tax Add Amount for Bracket 9
  WGPCTOVR9 BCD*5.5 Tax Percentage for Bracket 9
  WGBRACK10 BCD*10.3 Wage Ceiling for Bracket 10
  WGADDAMT10 BCD*10.3 Tax Add Amount for Bracket 10
  WGPCTOVR10 BCD*5.5 Tax Percentage for Bracket 10
  WGBRACK11 BCD*10.3 Wage Ceiling for Bracket 11
  WGADDAMT11 BCD*10.3 Tax Add Amount for Bracket 11
  WGPCTOVR11 BCD*5.5 Tax Percentage for Bracket 11
  WGBRACK12 BCD*10.3 Wage Ceiling for Bracket 12
  WGADDAMT12 BCD*10.3 Tax Add Amount for Bracket 12
  WGPCTOVR12 BCD*5.5 Tax Percentage for Bracket 12
  WGBRACK13 BCD*10.3 Wage Ceiling for Bracket 13
  WGADDAMT13 BCD*10.3 Tax Add Amount for Bracket 13
  WGPCTOVR13 BCD*5.5 Tax Percentage for Bracket 13
  WGBRACK14 BCD*10.3 Wage Ceiling for Bracket 14
  WGADDAMT14 BCD*10.3 Tax Add Amount for Bracket 14
  WGPCTOVR14 BCD*5.5 Tax Percentage for Bracket 14
  WGBRACK15 BCD*10.3 Wage Ceiling for Bracket 15
  WGADDAMT15 BCD*10.3 Tax Add Amount for Bracket 15
  WGPCTOVR15 BCD*5.5 Tax Percentage for Bracket 15
  WGBRACK16 BCD*10.3 Wage Ceiling for Bracket 16
  WGADDAMT16 BCD*10.3 Tax Add Amount for Bracket 16
  WGPCTOVR16 BCD*5.5 Tax Percentage for Bracket 16
  WGBRACK17 BCD*10.3 Wage Ceiling for Bracket 17
  WGADDAMT17 BCD*10.3 Tax Add Amount for Bracket 17
  WGPCTOVR17 BCD*5.5 Tax Percentage for Bracket 17
  WGBRACK18 BCD*10.3 Wage Ceiling for Bracket 18
  WGADDAMT18 BCD*10.3 Tax Add Amount for Bracket 18
  WGPCTOVR18 BCD*5.5 Tax Percentage for Bracket 18
  WGBRACK19 BCD*10.3 Wage Ceiling for Bracket 19
  WGADDAMT19 BCD*10.3 Tax Add Amount for Bracket 19
  WGPCTOVR19 BCD*5.5 Tax Percentage for Bracket 19
  WGBRACK20 BCD*10.3 Wage Ceiling for Bracket 20
  WGADDAMT20 BCD*10.3 Tax Add Amount for Bracket 20
  WGPCTOVR20 BCD*5.5 Tax Percentage for Bracket 20
  CLADID String*30 CLAD ID
  FLSCODE String*4 FLS Code
  LOCSTATE String*30 State
  LOCTAXCODE String*10 Political Subdivision Code
  LOCTYPE Integer Location Type. 0 - Unknown, 1 - Resident, 2 - Non-Resident
  TAXCAT String*10 Local Tax Category (PSD, LST, etc.)
  TCACODE String*10 Tax Collection Agency Code

## UTPAPSD - PA PSD Transaction Table (view UT0033)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ+TAXID; TRANSDATE+EMPLOYEE+ENTRYSEQ+TAXID
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  TAXID String*6 PSD Tax Identifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSDATE Date Check Date
  WITHHELD Boolean PSD Tax Withheld Indicator

## UTTXTYMP - Tax Type Mapping Table (view UT0032)
Keys (first = PK; D=dups allowed, M=modifiable): TAXID
Fields (NAME type description [values]):
  TAXID String*6 Tax ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXTYPE String*4 Tax Type
  STATEID String*2 State
  DESC String*100 Description
  ACCTABLE String*10 Sage Table Name
  ACCFIELD String*30 Sage Field Name
  FILTER String*100 Filter condition
  W2LOCTYP String*4 W2 Locality Tax Type (C,D,E,F)
  RECTYPE String*4 Aatrix AUF Record Type
  REPORTAUTH String*6 Report Authority ID

## UTW2PD - Paper W-2 Information (view UT0007)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCE+SORTPARAM+PRIMEKEY; SEQUENCE+SORTPARAM+CONTROL+SUBTOTAL [D,M]
Fields (NAME type description [values]):
  SEQUENCE Integer Sequence
  SORTPARAM String*94 Sort Parameter
  PRIMEKEY Long PrimeKey
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTROL Long Control
  SUBTOTAL Boolean Subtotal
  VOIDW2 Boolean Void W-2
  EMPLREIN String*9 Employer EIN
  EMPLRNAME String*60 Employer Name
  EMPLRADDR1 String*60 Employer Address 1
  EMPLRADDR2 String*60 Employer Address 2
  EMPLRADDR3 String*60 Employer Address 3
  EMPLRADDR4 String*60 Employer Address 4
  EMPLRCITY String*30 Employer City
  EMPLRSTATE String*30 Employer State
  EMPLRZIP String*20 Employer Zip Code
  SSN String*11 Employee SSN
  LASTNAME String*20 Employee Last Name
  FIRSTNAME String*15 Employee First Name
  MIDDLENAME String*15 Employee Middle Name
  ADDRESS1 String*60 Employee Address 1
  ADDRESS2 String*60 Employee Address 2
  ADDRESS3 String*60 Employee Address 3
  ADDRESS4 String*60 Employee Address 4
  CITY String*30 Employee City
  STATE String*30 Employee State
  ZIP String*20 Employee Zip Code
  WAGESTIPS BCD*10.3 Amount
  FIT BCD*10.3 Income Tax
  SSWAGES BCD*10.3 Wages
  SSTAXWHLD BCD*10.3 Tax Withheld
  MEDWAGETIP BCD*10.3 Med. Wage Tip
  MEDTAXWHLD BCD*10.3 Med. Tax Withheld
  SSTIPS BCD*10.3 Tips
  ALLOCTIPS BCD*10.3 Allocated Tips
  AEIC BCD*10.3 AEIC
  DEPCARE BCD*10.3 Dependent Care
  NONQUALCOD String*1 Nonqualified COD
  NONQUALPLN BCD*10.3 Nonqualified Plan
  BENEFITS BCD*10.3 Fringe Benefit
  FEDCODE1 String*2 Box 12 Code 1
  FEDAMT1 BCD*10.3 Box 12 Amount 1
  FEDCODE2 String*2 Box 12 Code 2
  FEDAMT2 BCD*10.3 Box 12 Amount 2
  FEDCODE3 String*2 Box 12 Code 3
  FEDAMT3 BCD*10.3 Box 12 Amount 3
  OTHCODE1 String*15 Box 14 Code 1
  OTHAMT1 BCD*10.3 Box 14 Amount 1
  OTHCODE2 String*15 Box 14 Code 2
  OTHAMT2 BCD*10.3 Box 14 Amount 2
  OTHCODE3 String*15 Box 14 Code 3
  OTHAMT3 BCD*10.3 Box 14 Amount 3
  STATUTEMP Boolean Statutory Employee
  DECEASED Boolean Deceased
  PENSIONPLN Boolean Pension Plan
  LEGALREP Boolean Legal Representative
  EMPLOY942 Boolean Hshld. Employee
  DEFERCOMP Boolean Deferred Comp. Contrib.
  FIPSCODE1 String*2 State Code 1
  REPORTID1 String*16 State Report ID 1
  SITWAGES1 BCD*10.3 State Amount 1
  SIT1 BCD*10.3 State Income Tax 1
  LOCNAME1 String*15 Local Report ID 1
  LOCWAGES1 BCD*10.3 Local Amount 1
  LOCTAX1 BCD*10.3 Local Income Tax 1
  FIPSCODE2 String*2 State Code 2
  REPORTID2 String*16 State Report ID 2
  SITWAGES2 BCD*10.3 State Amount 2
  SIT2 BCD*10.3 State Income Tax 2
  LOCNAME2 String*15 Local Report ID 2
  LOCWAGES2 BCD*10.3 Local Amount 2
  LOCTAX2 BCD*10.3 Local Income Tax 2
  COUNTRY String*30 Country
  FEDCODE4 String*2 Box 12 Code 4
  FEDAMT4 BCD*10.3 Box 12 Amount 4
  EMPLOYEE String*12 Employee
  OTHCODE4 String*15 Box 14 Code 4
  OTHAMT4 BCD*10.3 Box 14 Amount 4
  PHONENO String*15 Phone Number
  CONFIRMNO String*15 Confirmation Number
