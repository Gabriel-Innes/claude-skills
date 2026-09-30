# CT module - compiled AOM dictionary

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
  ADDBOX1 String*6 Additional Info Box 1
  ADDAMT1 BCD*10.3 Additional Info Amount 1
  ADDBOX2 String*6 Additional Info Box 2
  ADDAMT2 BCD*10.3 Additional Info Amount 2
  ADDBOX3 String*6 Additional Info Box 3
  ADDAMT3 BCD*10.3 Additional Info Amount 3
  ADDBOX4 String*6 Additional Info Box 4
  ADDAMT4 BCD*10.3 Additional Info Amount 4
  CPENSION2C BCD*10.3 CPP2 Contributions
  QPENSION2C BCD*10.3 QPP2 Contributions

## CTR1PH - Paper R1 Information (view CT0099)
Keys (first = PK; D=dups allowed, M=modifiable): PAYYEAR+EMPLOYEE
Fields (NAME type description [values]):
  PAYYEAR Integer Payment Year
  EMPLOYEE String*12 Employee ID
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
  ADDBOX1 String*6 Additional Info Box 1
  ADDAMT1 BCD*10.3 Additional Info Amount 1
  ADDBOX2 String*6 Additional Info Box 2
  ADDAMT2 BCD*10.3 Additional Info Amount 2
  ADDBOX3 String*6 Additional Info Box 3
  ADDAMT3 BCD*10.3 Additional Info Amount 3
  ADDBOX4 String*6 Additional Info Box 4
  ADDAMT4 BCD*10.3 Additional Info Amount 4
  CPENSION2C BCD*10.3 CPP2 Contributions
  QPENSION2C BCD*10.3 QPP2 Contributions

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
  INSPPVAC BCD*10.3 Vacation Pay Amount
  INSOMONIES BCD*10.3 Total Other Monies Amount

## CTROEH - Record of Employment Header (view CT0054)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMENDEDNBR String*9 Amended or Replaced Serial No.
  RREFERNBR String*26 Employer Payroll Reference No.
  COMPANYNAM String*60 Company Name
  CADDRESS1 String*60 Company Address 1
  CADDRESS2 String*60 Company Address 2
  CADDRESS3 String*60 Company Address 3
  CADDRESS4 String*60 Company Address 4
  CCITY String*30 Company Address City
  CPROVINCE String*30 Company Address Province
  CPOSTALC String*20 Company Postal Code
  RCTID String*20 CRA Business No. (BN)
  LANGUAGE Integer Communication Preferred in [1=English,2=French]
  PAYFREQ Integer Pay Period Type [2=Daily,3=Weekly,4=Biweekly,5=Semimonthly,10=22 pay periods,9=13 pay periods,6=Monthly,8=10 pay periods]
  EMPNAME String*60 INTERNAL USE - Employee Name
  EADDRESS1 String*60 INTERNAL USE - Employee Address 1
  EADDRESS2 String*60 INTERNAL USE - Employee Address 2
  EADDRESS3 String*60 INTERNAL USE - Employee Address 3
  EADDRESS4 String*60 INTERNAL USE - Employee Address 4
  ECITY String*30 INTERNAL USE - Employee Address City
  EPROVINCE String*30 INTERNAL USE - Employee Address Province
  COUNTRY String*30 Employee Country
  EPOSTALC String*10 Employee Postal Code
  POSITION String*40 Employee Occupation
  SIN String*11 Social Insurance Number
  FIRSTDAY Date First Day Worked
  LASTDAY Date Last Day for Which Paid
  UIPAYTO Date EI Premiums Payable up to
  PPENDDATE Date Final Period Ending Date
  ALLMAX Boolean Maximum for Each Pay Period
  UITOTEARN BCD*10.3 Total Insurable Earnings
  INSWEEKS Integer Insurable Weeks
  VACPAY BCD*10.3 Vacation Pay
  HOLDATE1 Date Holiday 1 Date
  HOLPAY1 BCD*10.3 Holiday 1 Amount
  HOLDATE2 Date Holiday 2 Date
  HOLPAY2 BCD*10.3 Holiday 2 Amount
  HOLDATE3 Date Holiday 3 Date
  HOLPAY3 BCD*10.3 Holiday 3 Amount
  OMONEY1D String*15 INTERNAL USE - Other Monies 1 Description
  OMONEY1 BCD*10.3 Other Monies 1 Amount
  OMONEY2D String*15 INTERNAL USE - Other Monies 2 Description
  OMONEY2 BCD*10.3 Other Monies 2 Amount
  OMONEY3D String*15 INTERNAL USE - Other Monies 3 Description
  OMONEY3 BCD*10.3 Other Monies 3 Amount
  ALLOCATED Integer Allocated Details
  SICKSTART Date Special Payment 1 Start Date
  SICKLENGTH Integer INTERNAL USE - Sick Leave Length
  BEWEEKS Integer Special Payment 1 Period
  SICKAMT BCD*10.3 Special Payment 1 Amount
  ROEREASONS Integer Reasons for Issuing [1=A00 - Shortage of work/End of contract or season,2=A01 - Employer bankruptcy or receivership,3=B00 - Strike or lock-out,4=D00 - Illness or injury,5=E00 - Quit,6=E02 - Quit/Follow spouse,7=E03 - Quit/Return to school,8=E04 - Quit/Health reasons,9=E05 - Quit/Voluntary retirement,10=E06 - Quit/Take another job,11=E09 - Quit/Employer relocation,12=E10 - Quit/Care for a dependant,13=E11 - Quit/To become self-employed,14=F00 - Maternity,15=G00 - Mandatory Retirement,16=G07 - Retirement/Approved workforce reduction,17=H00 - Work Sharing,18=J00 - Apprentice training,19=K00 - Other,20=K12 - Other/Change of payroll frequency,21=K13 - Other/Change of ownership,22=K14 - Other/Requested by Employment Insurance,23=K15 - Other/Canadian Forces - Queen's Regulations/Orders,24=K16 - Other/At the employee's request,25=K17 - Other/Change of Service Provider,26=M00 - Dismissal,27=M08 - Dismissal/Terminated within probationary period,28=N00 - Leave of absence,29=P00 - Parental,30=Z00 - Compassionate Care]
  ROEREASON String*3 Reason for Issuing This ROE
  CONTACT String*60 INTERNAL USE - For further Info. Contact
  TELEPHONE String*30 Contact Telephone No.
  RECALLDATE Date Expected Date of Recall
  NOTRETURN Boolean INTERNAL USE - Not Returning
  UNKNOWN Boolean INTERNAL USE - Unknown Date
  COMMENTS String*160 Comments
  ISSUERNAME String*60 Issuer Name
  ISSUEPHONE String*30 Issuer's Phone No.
  ISSUEDATE Date Date of Issue
  WHICHCNTRY Integer Which Country
  UITOTHRS BCD*4.3 EI Total Hrs
  UI96EARN BCD*10.3 Insurable Earnings for 1996
  BUSEUIDTL Boolean Print Insurable Earnings Detail?
  ROE53WEEKS Boolean 53 weeks ROE?
  USERID String*8 User ID
  SICKEND Date Special Payment 1 End Date
  VACPAYCODE Integer Vacation Pay type [0=,1=Included with each pay,2=Paid because no longer working,3=Paid for a vacation leave period,4=Anniversary (Paid on a specific date each year)]
  VACSTART Date Vacation Pay Start Date
  VACEND Date Vacation Pay End Date
  OMONEY1C Integer Other Monies 1 Code [0=,1=B05 - Bonus (Holiday),2=B06 - Bonus (Production/Incentive),3=B07 - Bonus (Event),4=B08 - Bonus (Staying/Contract complete/End of season),5=B09 - Bonus (Separation or retirement),6=B10 - Bonus (Closure),7=B11 - Bonus (Other),8=E00 - Severance pay,9=G00 - Gratuities,10=H00 - Honorariums,11=I00 - Sick leave credits,12=J00 - Retroactive pay adjustment,13=O00 - Other,14=Q00 - Profit sharing,15=R00 - Retiring allowance / Retirement leave credits,16=S00 - Settlement pay,17=T00 - Payout of banked overtime,18=U12 - SUB Maternity/Parental/Compassionate Care/Parents of Critically Ill Children,19=U13 - SUB Layoff,20=U14 - SUB Illness,21=U15 - SUB Training,22=Y00 - Pay in lieu of notice]
  OMONEY2C Integer Other Monies 2 Code [0=,1=B05 - Bonus (Holiday),2=B06 - Bonus (Production/Incentive),3=B07 - Bonus (Event),4=B08 - Bonus (Staying/Contract complete/End of season),5=B09 - Bonus (Separation or retirement),6=B10 - Bonus (Closure),7=B11 - Bonus (Other),8=E00 - Severance pay,9=G00 - Gratuities,10=H00 - Honorariums,11=I00 - Sick leave credits,12=J00 - Retroactive pay adjustment,13=O00 - Other,14=Q00 - Profit sharing,15=R00 - Retiring allowance / Retirement leave credits,16=S00 - Settlement pay,17=T00 - Payout of banked overtime,18=U12 - SUB Maternity/Parental/Compassionate Care/Parents of Critically Ill Children,19=U13 - SUB Layoff,20=U14 - SUB Illness,21=U15 - SUB Training,22=Y00 - Pay in lieu of notice]
  OMONEY3C Integer Other Monies 3 Code [0=,1=B05 - Bonus (Holiday),2=B06 - Bonus (Production/Incentive),3=B07 - Bonus (Event),4=B08 - Bonus (Staying/Contract complete/End of season),5=B09 - Bonus (Separation or retirement),6=B10 - Bonus (Closure),7=B11 - Bonus (Other),8=E00 - Severance pay,9=G00 - Gratuities,10=H00 - Honorariums,11=I00 - Sick leave credits,12=J00 - Retroactive pay adjustment,13=O00 - Other,14=Q00 - Profit sharing,15=R00 - Retiring allowance / Retirement leave credits,16=S00 - Settlement pay,17=T00 - Payout of banked overtime,18=U12 - SUB Maternity/Parental/Compassionate Care/Parents of Critically Ill Children,19=U13 - SUB Layoff,20=U14 - SUB Illness,21=U15 - SUB Training,22=Y00 - Pay in lieu of notice]
  OMONEY1ST Date Other Monies 1 Start Date
  OMONEY1EN Date Other Monies 1 End Date
  OMONEY2ST Date Other Monies 2 Start Date
  OMONEY2EN Date Other Monies 2 End Date
  OMONEY3ST Date Other Monies 3 Start Date
  OMONEY3EN Date Other Monies 3 End Date
  HOLDATE4 Date Holiday 4 Date
  HOLPAY4 BCD*10.3 Holiday 4 Amount
  HOLDATE5 Date Holiday 5 Date
  HOLPAY5 BCD*10.3 Holiday 5 Amount
  HOLDATE6 Date Holiday 6 Date
  HOLPAY6 BCD*10.3 Holiday 6 Amount
  HOLDATE7 Date Holiday 7 Date
  HOLPAY7 BCD*10.3 Holiday 7 Amount
  HOLDATE8 Date Holiday 8 Date
  HOLPAY8 BCD*10.3 Holiday 8 Amount
  HOLDATE9 Date Holiday 9 Date
  HOLPAY9 BCD*10.3 Holiday 9 Amount
  HOLDATE10 Date Holiday 10 Date
  HOLPAY10 BCD*10.3 Holiday 10 Amount
  SICKTYPE Integer Special Payment 1 type [0=,1=Paid Sick Leave,2=Wage Loss Indemnity (Not EI Insurable),3=Wage Loss Indemnity (EI Insurable),4=Paid Maternity/Parental/Compassionate Care/Parents of Critically Ill Children Leave]
  SICKTYPE2 Integer Special Payment 2 type [0=,1=Paid Sick Leave,2=Wage Loss Indemnity (Not EI Insurable),3=Wage Loss Indemnity (EI Insurable),4=Paid Maternity/Parental/Compassionate Care/Parents of Critically Ill Children Leave]
  SICKTYPE3 Integer Special Payment 3 type [0=,1=Paid Sick Leave,2=Wage Loss Indemnity (Not EI Insurable),3=Wage Loss Indemnity (EI Insurable),4=Paid Maternity/Parental/Compassionate Care/Parents of Critically Ill Children Leave]
  SICKTYPE4 Integer Special Payment 4 type [0=,1=Paid Sick Leave,2=Wage Loss Indemnity (Not EI Insurable),3=Wage Loss Indemnity (EI Insurable),4=Paid Maternity/Parental/Compassionate Care/Parents of Critically Ill Children Leave]
  SICKSTART2 Date Special Payment 2 Start Date
  SICKEND2 Date Special Payment 2 End Date
  SICKLEN2 Integer INTERNAL USE - Sick Leave 2 Length
  BEWEEKS2 Integer Special Payment 2 Period
  SICKAMT2 BCD*10.3 Special Payment 2 Amount
  SICKSTART3 Date Special Payment 3 Start Date
  SICKEND3 Date Special Payment 3 End Date
  SICKLEN3 Integer INTERNAL USE - Sick Leave 3 Length
  BEWEEKS3 Integer Special Payment 3 Period
  SICKAMT3 BCD*10.3 Special Payment 3 Amount
  SICKSTART4 Date Special Payment 4 Start Date
  SICKEND4 Date Special Payment 4 End Date
  SICKLEN4 Integer INTERNAL USE - Sick Leave 4 Length
  BEWEEKS4 Integer Special Payment 4 Period
  SICKAMT4 BCD*10.3 Special Payment 4 Amount
  PRINTLANG Integer Print Language [1=English,2=French]
  RECALLOPTS Integer Recall Options [0=U - Unknown,1=N - Not Returning,2=Y - Expected date of recall (specify the date below)]
  AREACODE String*3 Area Code
  EXTENSION String*8 Extension
  EMPFNAME String*20 Employee First Name
  EMPLNAME String*28 Employee Last Name
  EMPINITIAL String*4 Employee's name, including an initial
  EMPADDR1 String*35 Employee Address 1
  EMPADDR2 String*35 Employee Address 2
  EMPADDR3 String*35 Employee Address 3
  CNTCTFNAME String*20 Contact person's First Name
  CNTCTLNAME String*28 Contact person's Last Name

## CTT4AD - Paper T4A Information (view CT0097)
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
  COUNTRY String*30 Country
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
  PENSION BCD*10.3 Pension or Superannuation
  LUMPSUM BCD*10.3 Lump-Sum Payments
  SELFEMPCOM BCD*10.3 Self-Employed Commissions
  ANNUITIES BCD*10.3 Annuities
  INCOMETAX BCD*10.3 Income Tax Deducted
  FEES BCD*10.3 Fees for Services
  OTHBOX1 String*3 Other Box 1
  OTHAMT1 BCD*10.3 Other Amount 1
  OTHBOX2 String*3 Other Box 2
  OTHAMT2 BCD*10.3 Other Amount 2
  OTHBOX3 String*3 Other Box 3
  OTHAMT3 BCD*10.3 Other Amount 3
  OTHBOX4 String*3 Other Box 4
  OTHAMT4 BCD*10.3 Other Amount 4
  OTHBOX5 String*3 Other Box 5
  OTHAMT5 BCD*10.3 Other Amount 5
  OTHBOX6 String*3 Other Box 6
  OTHAMT6 BCD*10.3 Other Amount 6
  OTHBOX7 String*3 Other Box 7
  OTHAMT7 BCD*10.3 Other Amount 7
  OTHBOX8 String*3 Other Box 8
  OTHAMT8 BCD*10.3 Other Amount 8
  OTHBOX9 String*3 Other Box 9
  OTHAMT9 BCD*10.3 Other Amount 9
  OTHBOX10 String*3 Other Box 10
  OTHAMT10 BCD*10.3 Other Amount 10
  OTHBOX11 String*3 Other Box 11
  OTHAMT11 BCD*10.3 Other Amount 11
  OTHBOX12 String*3 Other Box 12
  OTHAMT12 BCD*10.3 Other Amount 12
  PAYERDENT Integer Payer Offered Dental

## CTT4AH - Paper T4A Information (view CT0100)
Keys (first = PK; D=dups allowed, M=modifiable): PAYYEAR+EMPLOYEE
Fields (NAME type description [values]):
  PAYYEAR Integer Payment Year
  EMPLOYEE String*12 Employee ID
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
  COUNTRY String*30 Country
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
  PENSION BCD*10.3 Pension or Superannuation
  LUMPSUM BCD*10.3 Lump-Sum Payments
  SELFEMPCOM BCD*10.3 Self-Employed Commissions
  ANNUITIES BCD*10.3 Annuities
  INCOMETAX BCD*10.3 Income Tax Deducted
  FEES BCD*10.3 Fees for Services
  OTHBOX1 String*3 Other Box 1
  OTHAMT1 BCD*10.3 Other Amount 1
  OTHBOX2 String*3 Other Box 2
  OTHAMT2 BCD*10.3 Other Amount 2
  OTHBOX3 String*3 Other Box 3
  OTHAMT3 BCD*10.3 Other Amount 3
  OTHBOX4 String*3 Other Box 4
  OTHAMT4 BCD*10.3 Other Amount 4
  OTHBOX5 String*3 Other Box 5
  OTHAMT5 BCD*10.3 Other Amount 5
  OTHBOX6 String*3 Other Box 6
  OTHAMT6 BCD*10.3 Other Amount 6
  OTHBOX7 String*3 Other Box 7
  OTHAMT7 BCD*10.3 Other Amount 7
  OTHBOX8 String*3 Other Box 8
  OTHAMT8 BCD*10.3 Other Amount 8
  OTHBOX9 String*3 Other Box 9
  OTHAMT9 BCD*10.3 Other Amount 9
  OTHBOX10 String*3 Other Box 10
  OTHAMT10 BCD*10.3 Other Amount 10
  OTHBOX11 String*3 Other Box 11
  OTHAMT11 BCD*10.3 Other Amount 11
  OTHBOX12 String*3 Other Box 12
  OTHAMT12 BCD*10.3 Other Amount 12
  PAYERDENT Integer Payer Offered Dental

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
  HRLBEN BCD*10.3 Employee Home-relocation Loan
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
  ELIGRET BCD*10.3 Eligible retiring allowances
  NOELIGRET BCD*10.3 Non-eligible retiring allowances
  XELIGRET BCD*10.3 Status Indian (exempt income) - Eligible retiring allowances
  XNOELIGRET BCD*10.3 Status Indian (exempt income) - Non-eligible retiring allowances
  FRFIGHTER BCD*10.3 Emergency services volunteer exempt amount
  SPWORKSITE BCD*10.3 Special Working Site
  EMPLERDENT Integer Employer Offered Dental
  CPENSION2C BCD*10.3 CPP2 Contributions
  RCPENSION2 BCD*10.3 Employer's CPP2 Contributions
  QPENSION2C BCD*10.3 QPP2 Contributions
  NSTKBEN BCD*10.3 Post 20240625 Stock Option Benefits
  NSTKBEND BCD*10.3 Post 20240625 Stock Option and Shares Ded(110(1)(d))
  NSTKBEND1 BCD*10.3 Post 20240625 Stock Option and Shares Ded(110(1)(d.1))
  INDRPP BCD*10.3 Indian (Exempt Income) RPP Contribution
  INDUNION BCD*10.3 Indian (Exempt Income) Union Dues

## CTT4PH - Paper T4 Information (view CT0098)
Keys (first = PK; D=dups allowed, M=modifiable): PAYYEAR+EMPLOYEE
Fields (NAME type description [values]):
  PAYYEAR Integer Payment Year
  EMPLOYEE String*12 Employee ID
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
  HRLBEN BCD*10.3 Employee Home-relocation Loan
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
  ELIGRET BCD*10.3 Eligible retiring allowances
  NOELIGRET BCD*10.3 Non-eligible retiring allowances
  XELIGRET BCD*10.3 Status Indian (exempt income) - Eligible retiring allowances
  XNOELIGRET BCD*10.3 Status Indian (exempt income) - Non-eligible retiring allowances
  FRFIGHTER BCD*10.3 Emergency services volunteer exempt amount
  SPWORKSITE BCD*10.3 Special Working Site
  EMPLERDENT Integer Employer Offered Dental
  CPENSION2C BCD*10.3 CPP2 Contributions
  RCPENSION2 BCD*10.3 Employer's CPP2 Contributions
  QPENSION2C BCD*10.3 QPP2 Contributions
  NSTKBEN BCD*10.3 Post 20240625 Stock Option Benefits
  NSTKBEND BCD*10.3 Post 20240625 Stock Option and Shares Ded(110(1)(d))
  NSTKBEND1 BCD*10.3 Post 20240625 Stock Option and Shares Ded(110(1)(d.1))
  INDRPP BCD*10.3 Indian (Exempt Income) RPP Contribution
  INDUNION BCD*10.3 Indian (Exempt Income) Union Dues

## CTTXTYMP - Tax Type Mapping Table (view CT0032)
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
  W2CODE String*6 W2 Tax Code

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
