# UP module - compiled AOM dictionary

## UPACCO - Accrual Carry-over Log File (view UP0115)
Keys (first = PK; D=dups allowed, M=modifiable): YEAR+EMPLOYEE+EARNDED
Fields (NAME type description [values]):
  YEAR Integer Year
  EMPLOYEE String*12 Employee
  EARNDED String*6 Earning/Deduction
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PEREND Date Period End Date
  ENTRYSEQ Long Check Sequence No.
  TRANSNUM BCD*8.0 Check Transaction Number
  TRANSDATE Date Check Transaction Date
  CLASS1 String*6 Class 1
  CLASS2 String*6 Class 2
  CLASS3 String*6 Class 3
  CLASS4 String*6 Class 4
  ENTRYTYPE Integer Entry Type
  BALANCE BCD*10.3 Previous Balance
  ACCRUED BCD*10.3 Previous Accrued
  PAID BCD*10.3 Previous Paid
  CARRYDATE Date Carry-over date
  MAXONREM Boolean Base on Remaining Balance
  BEGINNING BCD*10.3 Beginning Increment
  MAXACCR BCD*10.3 Maximum Accrual
  MAXCARRY BCD*10.3 Maximum Carry-over

## UPAUDA - Assign Earn/Ded Audit (view UP0227)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EARNDED String*6 Earning/Deduction
  EDDESC String*60 Earning/Deduction Description
  SELTYPE Integer Employee Selection Type [0=Employee Number,1=Class,2=Selection List,3=Set Criteria]
  EMPLISTID String*8 Selection List
  FEMPLOYEE String*12 From Employee
  TEMPLOYEE String*12 To Employee
  CLASS Integer Class [1=Class 1,2=Class 2,3=Class 3,4=Class 4]
  FCLASSCOD String*6 From Class Code
  TCLASSCOD String*6 To Class Code
  EBROWSE String*250 Employee Browse Filter
  EMPUPDATED Long Employees Updated
  RUNDATE Date Run Date
  ECALCMETH Integer Employee Calculation Method
  RCALCMETH Integer Employer Calculation Method
  USEDEFAULT Boolean Use Employee Defaults [0=No,1=Yes]
  CATEGORY Integer Category
  ORGUSERID String*8 Original User ID

## UPAUDAB - Assign Earn/Ded Audit Billing (view UP0229)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+EMPLOYEE+FIELDIDX+CURRCODE
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  EMPLOYEE String*12 Employee
  FIELDIDX Long Field Index
  CURRCODE String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CURRNAME String*30 Currency Description
  DECIMALS Integer Decimals
  THOUSSEP String*1 Thousands Separator
  DECSEP String*1 Decimals Separator
  BILLRATE1 BCD*10.6 Billing Rate 1
  BILLRATE2 BCD*10.6 Billing Rate 2
  BILLRATE3 BCD*10.6 Billing Rate 3
  BILLRATE4 BCD*10.6 Billing Rate 4
  BILLRATE5 BCD*10.6 Billing Rate 5
  BILLRATE6 BCD*10.6 Billing Rate 6

## UPAUDAD - Assign Earn/Ded Audit Details (view UP0228)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+EMPLOYEE+FIELDIDX
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  EMPLOYEE String*12 Employee
  FIELDIDX Long Field Index
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FIELDNAME String*32 Field Name
  EMPLNAME String*60 Employee Name
  FIELDTYPE Integer Field Type [0=Undefined,1=String,2=Byte,3=Date,4=Time,5=IEEE Long Real,6=Amount,7=Integer,8=Long Integer,9=Boolean]
  FIELDLEN Integer Field Length
  FIELDSIZE Integer Field Size
  FIELDDECS Integer Field Decimals
  BCDTYPE Integer Type of BCD Field [0=N/A,1=Rate,2=Amount,3=Percent,4=Billing Rate]
  NEWSTRING String*60 New String Value
  NEWDATE Date New Date Value
  NEWINT Integer New Integer Value
  NEWAMT BCD*9.5 New Amount
  NEWLONG Long New Long Value
  NEWBILLRAT BCD*10.6 New Billing Rate

## UPAUDE - Update Earn/Ded Audit (view UP0223)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EARNDED String*6 Earning/Deduction
  EDDESC String*60 Earning/Deduction Description
  SELTYPE Integer Employee Selection Type [0=Employee Number,1=Class,2=Selection List,3=Set Criteria]
  EMPLISTID String*8 Selection List
  FEMPLOYEE String*12 From Employee
  TEMPLOYEE String*12 To Employee
  CLASS Integer Class [1=Class 1,2=Class 2,3=Class 3,4=Class 4]
  FCLASSCOD String*6 From Class Code
  TCLASSCOD String*6 To Class Code
  EBROWSE String*250 Employee Browse Filter
  EMPUPDATED Long Employees Updated
  RUNDATE Date Run Date
  ECALCMETH Integer Employee Calculation Method
  RCALCMETH Integer Employer Calculation Method
  CURRCODE String*3 Currency Code
  CURRDESC String*30 Currency Description
  DECIMALS Integer Decimals
  THOUSSEP String*1 Thousands Separator
  DECSEP String*1 Decimal Separator
  CATEGORY Integer Category
  ORGUSERID String*8 Original User ID

## UPAUDED - Update Earn/Ded Audit Details (view UP0224)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+EMPLOYEE+FIELDIDX
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  EMPLOYEE String*12 Employee
  FIELDIDX Long Field Index
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FIELDNAME String*32 Field Name
  EMPLNAME String*60 Employee Name
  FIELDTYPE Integer Field Type [0=Undefined,1=String,2=Byte,3=Date,4=Time,5=IEEE Long Real,6=Amount,7=Integer,8=Long Integer,9=Boolean]
  FIELDLEN Integer Field Length
  FIELDSIZE Integer Field Size
  FIELDDECS Integer Field Decimals
  BCDTYPE Integer Type of BCD Field [0=N/A,1=Rate,2=Amount,3=Percent,4=Billing Rate]
  OPERATION Integer Operation [1=,2=Replace,3=Increase,4=Decrease,5=Pct Inc,6=Pct Dec,7=Replace,8=Increase,9=Decrease,10=Replace,11=Replace,12=Replace,13=Replace,14=Replace,15=Replace,16=Increase,17=Decrease,18=Pct Inc,19=Pct Dec]
  TESTOLD Boolean Test Old Value
  OLDSTRING String*60 Old String Value
  NEWSTRING String*60 New String Value
  OLDDATE Date Old Date Value
  NEWDATE Date New Date Value
  OLDINT Integer Old Integer Value
  NEWINT Integer New Integer Value
  OLDAMTPCT BCD*9.5 Old Amount or Percent
  AMTPCTCHG BCD*9.5 Amount/Percent Change
  OLDWCCGRUP String*6 Old WC Group
  NEWWCCGRUP String*6 New WC Group
  OLDBILLRAT BCD*10.6 Old Billing Rate
  NEWBILLRAT BCD*10.6 New Billing Rate

## UPAUDM - Delete Inactive Records Audit (view UP0220)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CLEARDATE Date Clearing Date
  DELHIST Boolean Delete Employee History [0=No,1=Yes]
  DELEMPS Boolean Delete Terminated Employees [0=No,1=Yes]
  DELEARNDED Boolean Delete Inactive Earnings/Deductions [0=No,1=Yes]
  DELTAXTBLS Boolean Delete Inactive Taxes [0=No,1=Yes]
  RECSCLEARD Boolean Records were cleared [0=No,1=Yes]
  HSTARTEMPL String*12 Delete History From Employee
  HENDEMPL String*12 Delete History To Employee
  DSTARTEMPL String*12 Delete Employees From
  DENDEMPL String*12 Delete Employees To
  DSTARTED String*6 Delete Earn/Ded From
  DENDED String*6 Delete Earn/Ded To
  DSTARTTAX String*6 Delete Taxes From
  DENDTAX String*6 Delete Taxes To
  INACDELCNT Long Total Inactive Records Deleted
  TERMDELCNT Long Total Employees Deleted
  HISTDELCNT Long Total Transactions Deleted
  RUNDATE Date Run Date
  ORGUSERID String*8 Original User ID

## UPAUDMH - Delete Audit Transaction Details (view UP0222)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+EMPLOYEE+PEREND+ENTRYSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSDATE Date Transaction Date
  BANK String*8 Bank ID
  TRANSAMT BCD*10.3 Transaction Amt
  EMPLNAME String*60 Employee Name

## UPAUDMI - Delete Audit Inactive Details (view UP0221)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+DELTYPE+DELCODE
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  DELTYPE Integer Deletion Type [1=Terminated Employee,2=Inactive Earning/Deduction,3=Inactive Taxes]
  DELCODE String*15 Deletion Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CODEDESC String*60 Code Description
  LASTMAINT Date Last Maintained

## UPAUDS - Assign Tax Audit (view UP0230)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXID String*6 Tax
  TAXDESC String*60 Tax Description
  SELTYPE Integer Employee Selection Type [0=Employee Number,1=Class,2=Selection List,3=Set Criteria]
  EMPLISTID String*8 Selection List
  FEMPLOYEE String*12 From Employee
  TEMPLOYEE String*12 To Employee
  CLASS Integer Class [1=Class 1,2=Class 2,3=Class 3,4=Class 4]
  FCLASSCOD String*6 From Class Code
  TCLASSCOD String*6 To Class Code
  EBROWSE String*250 Employee Browse Filter
  EMPUPDATED Long Employees Updated
  RUNDATE Date Run Date
  ECALCMETH Integer Employee Calculation Method
  RCALCMETH Integer Employer Calculation Method
  CATEGORY Integer Category
  ORGUSERID String*8 Original User ID

## UPAUDSD - Tax Audit Details (view UP0231)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+EMPLOYEE+FIELDIDX
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  EMPLOYEE String*12 Employee
  FIELDIDX Long Field Index
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FIELDNAME String*32 Field Name
  EMPLNAME String*60 Employee Name
  FIELDTYPE Integer Field Type [0=Undefined,1=String,2=Byte,3=Date,4=Time,5=IEEE Long Real,6=Amount,7=Integer,8=Long Integer,9=Boolean]
  FIELDLEN Integer Field Length
  FIELDSIZE Integer Field Size
  FIELDDECS Integer Field Decimals
  BCDTYPE Integer Type of BCD Field [0=N/A,1=Rate,2=Amount,3=Percent,4=Billing Rate]
  NEWSTRING String*60 New String Value
  NEWDATE Date New Date Value
  NEWINT Integer New Integer Value
  NEWAMT BCD*9.5 New Amount
  NEWLONG Long New Long Value

## UPAUDT - Update Taxes Audit (view UP0225)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXID String*6 Tax
  TAXDESC String*60 Tax Description
  SELTYPE Integer Employee Selection Type [0=Employee Number,1=Class,2=Selection List,3=Set Criteria]
  EMPLISTID String*8 Selection List
  FEMPLOYEE String*12 From Employee
  TEMPLOYEE String*12 To Employee
  CLASS Integer Class [1=Class 1,2=Class 2,3=Class 3,4=Class 4]
  FCLASSCOD String*6 From Class Code
  TCLASSCOD String*6 To Class Code
  EBROWSE String*250 Employee Browse Filter
  EMPUPDATED Long Employees Updated
  RUNDATE Date Run Date
  ECALCMETH Integer Employee Calculation Method
  RCALCMETH Integer Employer Calculation Method
  ORGUSERID String*8 Original User ID

## UPAUDTD - Update Taxes Audit Details (view UP0226)
Keys (first = PK; D=dups allowed, M=modifiable): RUNSEQ+EMPLOYEE+FIELDIDX
Fields (NAME type description [values]):
  RUNSEQ Long Run Sequence
  EMPLOYEE String*12 Employee
  FIELDIDX Long Field Index
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FIELDNAME String*32 Field Name
  EMPLNAME String*60 Employee Name
  FIELDTYPE Integer Field Type [0=Undefined,1=String,2=Byte,3=Date,4=Time,5=IEEE Long Real,6=Amount,7=Integer,8=Long Integer,9=Boolean]
  FIELDLEN Integer Field Length
  FIELDSIZE Integer Field Size
  FIELDDECS Integer Field Decimals
  BCDTYPE Integer Type of BCD Field [0=N/A,1=Rate,2=Amount,3=Percent]
  OPERATION Integer Operation [1=,2=Replace,3=Increase,4=Decrease,5=Pct Inc,6=Pct Dec,7=Replace,8=Increase,9=Decrease,10=Replace,11=Replace,12=Replace,13=Replace,14=Replace]
  TESTOLD Boolean Test Old Value
  OLDSTRING String*60 Old String Value
  NEWSTRING String*60 New String Value
  OLDDATE Date Old Date Value
  NEWDATE Date New Date Value
  OLDINT Integer Old Integer Value
  NEWINT Integer New Integer Value
  OLDAMTPCT BCD*9.5 Old Amount or Percent
  AMTPCTCHG BCD*9.5 Amount/Percent Change
  EMPTTYPE Integer Employee Tax Type [1=No EMPT Processing,2=Withholding Amount Override,3=Withholding Percent Override,4=Employee Tax Amount,5=Employee Tax Percent]

## UPCALA - Cost Center Allocations (view UP0086)
Keys (first = PK; D=dups allowed, M=modifiable): GLSEG1+GLSEG2+GLSEG3+GLSEG4+GLSEG5+GLSEG6
Fields (NAME type description [values]):
  GLSEG1 String*15 Cost Center Segment 1
  GLSEG2 String*15 Cost Center Segment 2
  GLSEG3 String*15 Cost Center Segment 3
  GLSEG4 String*15 Cost Center Segment 4
  GLSEG5 String*15 Cost Center Segment 5
  GLSEG6 String*15 Cost Center Segment 6
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EAMOUNT BCD*10.3 Employee Amount
  ECNTBASE BCD*10.3 Employee Cnt/Base Amount
  RAMOUNT BCD*10.3 Employer Amount
  RCNTBASE BCD*10.3 Employer Cnt/Base Amount

## UPCHDO - Check Details Optional Fields (view UP0134)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ+CATEGORY+EARNDED+LINETYPE+LINENO+OPTFIELD; OPTFIELD+EMPLOYEE+PEREND+ENTRYSEQ+CATEGORY+EARNDED+LINETYPE+LINENO
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  CATEGORY Integer Category Code [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARNDED String*6 Earning/Deduction-Tax
  LINETYPE Integer Type [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  LINENO Integer Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPCHHO - Check Header Optional Field Values (view UP0133)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ+OPTFIELD; OPTFIELD+EMPLOYEE+PEREND+ENTRYSEQ
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPCHJB - Check Job Details (view UP0056)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ+CATEGORY+EARNDED+LINETYPE+LINENO+JOBLINE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARNDED String*6 Earning/Deduction
  LINETYPE Integer Type [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  LINENO Integer Line Number
  JOBLINE Integer Job Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CCATEGORY String*16 Category Code
  IDCUST String*12 Customer
  CURRCODE String*3 Billing Currency
  STARTTIME Integer Start Time
  STOPTIME Integer Stop Time
  HOURS BCD*4.3 Hours
  CNTBASE BCD*10.3 Pieces/Sales/Amt
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Item UOM
  WIPACCT String*45 WIP/COS Acct
  VALUES Long Number of Optional Fields
  CURRDESC String*30 Currency Description
  UFMTCONTNO String*16 Unformatted Contract Code
  PROJSTYLE Integer Project Style [0=,1=Standard,2=Basic]
  PROJTYPE Integer Project Type [0=,1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [0=,1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,7=Completed Contract,8=Accrual-Basis]
  BEXTEND BCD*10.3 Extended Billing Amount
  EEXTEND BCD*10.3 Employee Extended Amount
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 (FC) Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 (FC) Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  PMTRANSNUM Long PJC Transaction Number
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  RESDESC String*60 Resource Description

## UPCHJO - Check Jobs Optional Fields Values (view UP0144)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ+CATEGORY+EARNDED+LINETYPE+LINENO+JOBLINE+OPTFIELD; OPTFIELD+EMPLOYEE+PEREND+ENTRYSEQ+CATEGORY+EARNDED+LINETYPE+LINENO+JOBLINE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARNDED String*6 Earning/Deduction
  LINETYPE Integer Type [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  LINENO Integer Line Number
  JOBLINE Integer Job Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPCHKC - Check Comment Detail (view UP0052)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ+UNIQUE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  UNIQUE Integer Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMMENT String*250 Comment

## UPCHKD - Check Details (view UP0049)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ+CATEGORY+EARNDED+LINETYPE+LINENO; EMPLOYEE+PEREND+ENTRYSEQ+PCATEGORY+PLINETYPE+EARNDED+LINETYPE+LINENO
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARNDED String*6 Earning/Deduction-Tax
  LINETYPE Integer Type [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EARDEDTYPE Integer Earning/Deduction-Tax Type [1=Salary & Wages,2=Reported Tips,3=Allocated Tips,7=Vacation,8=Sick,9=Compensatory Time,13=Cash,14=Noncash,18=Insurance Tax,19=Income Tax,20=Unemployment Tax,21=Pension Plan Tax,22=Health Tax,23=Other Tax,25=n/a]
  EARDEDDATE Date Earning/Deduction Date
  HOURS BCD*4.3 Hours
  ECNTBASE BCD*10.3 Employee Pieces/Sales/Base
  ERATE BCD*9.5 Employee Rate/Amt/Pct
  EEXTEND BCD*10.3 Employee Extended Amount
  EREGRATE BCD*9.5 Regular Rate
  RCNTBASE BCD*10.3 Employer Pieces/Base
  RRATE BCD*9.5 Employer Amt/Pct
  REXTEND BCD*10.3 Employer Extended Amount
  EXPACCT String*45 Regular Pay Expense G/L Account
  ELIABACCT String*45 Employee Liability G/L Account
  RLIABACCT String*45 Employer Liability G/L Account
  WCC String*6 Workers' Compensation Code
  GLSEG1 String*15 Cost Center Segment One
  GLSEG2 String*15 Cost Center Segment Two
  GLSEG3 String*15 Cost Center Segment Three
  PARTIAL Boolean Detail Was Partially Taken or Not
  TAXWEEKS BCD*4.3 Weeks Worked
  TAXEARNS BCD*10.3 Earn Subj to Tax (No Ceiling)
  TXEARNCEIL BCD*10.3 Earn Subj to Tax
  TAXTIPS BCD*10.3 No Ceiling Tips
  TXTIPSCEIL BCD*10.3 Ceiling Tips
  TAXONTIPS BCD*10.3 Tax on Tips
  UNCOLLTAX BCD*10.3 Uncollected Tax on Tips
  PCATEGORY Integer Print Category [1=CHKD Earnings,2=CHKD Deductions,3=CHKD Taxes,4=CHKD Other,5=CHKD Benefits]
  PLINETYPE Integer Print Line Type [11=CHKD Regular Line,11=CHKD Overtime Line,11=CHKD Shift Diff Line,14=CHKD Disbursed Tips,15=CHKD Vacation Payment,16=CHKD Sick Payment,17=CHKD Comp. Time Payment,21=CHKD Deduction Entry,31=CHKD Federal Income Entry,32=CHKD Federal Insurance Entry,33=CHKD Federal UI Entry,34=CHKD Federal Pension Entry,35=CHKD Federal Health Entry,36=CHKD Federal Other Entry,41=CHKD State Income Entry,42=CHKD State Insurance Entry,43=CHKD State UI Entry,44=CHKD State Pension Entry,45=CHKD State Health Entry,46=CHKD State Other Entry,51=CHKD Local Income Entry,52=CHKD Local Insurance Entry,53=CHKD Local UI Entry,54=CHKD Local Pension Entry,55=CHKD Local Health Entry,56=CHKD Local Other Entry,61=CHKD User Income Entry,62=CHKD User Insurance Entry,63=CHKD User UI Entry,64=CHKD User Pension Entry,65=CHKD User Health Entry,66=CHKD User Other Entry,71=CHKD Exp Reimbursement,72=CHKD Cash Advance,73=CHKD Reported Tips,74=CHKD Allocated Tips,75=CHKD Noncash Advance,76=CHKD Vac Accrual,77=CHKD Sick Accrual,78=CHKD Comp Accrual,81=CHKD Cash Benefit,82=CHKD Noncash Benefit]
  PCONTENTS Integer Print Line Contents [1=CHKD Employee Only,2=CHKD Both EmpE And EmpR,3=CHKD Employer Only,4=CHKD Historical Entry,5=CHKD Tax Info Only Entry]
  TAXNONPER BCD*10.3 RESERVED - Cdn Only
  TAXEARNBD BCD*10.3 RESERVED - Cdn Only
  POOLEDTIPS BCD*10.3 RESERVED - Cdn Only
  DETAILDATE Date Detail Date
  STARTTIME Integer Start Time
  STOPTIME Integer Stop Time
  WCCGROUP String*6 Workers Comp. Group
  VALUES Long Number of Optional Fields
  SWFLSA Boolean Included in FLSA Overtime Calc
  DAYS Integer Days Worked
  OTSCHED String*6 Overtime Schedule
  OTHOURS BCD*4.3 Overtime Hours Override
  STAMOUNT BCD*10.3 Straight Time Earnings
  PREMIUMRT BCD*5.5 Overtime Rate Multiplier
  JOBS Long Jobs
  WORKCODE String*6 Work Classification Code
  LOCTAXCODE String*10 Local Tax Code
  WCBASE BCD*10.3 WC Base
  WCRATE BCD*6.6 WC Rate
  WCEXTEND BCD*10.5 WC Assessment
  WCEXPACCT String*45 WC Expense Account
  WCLIABACCT String*45 WC Liability Account
  CSEFTSTAT Integer Child Support EFT Status [0=Not EFTed,1=EFTed]
  DISTCODE String*6 Distribution Code
  DISTRNAME String*15 Distribution Description
  GLSEG4 String*15 Cost Center Segment Four
  GLSEG5 String*15 Cost Center Segment Fix
  GLSEG6 String*15 Cost Center Segment Six
  TAXNONDED BCD*10.3 RESERVED - Cdn Only
  TAXREPAY BCD*10.3 RESERVED - Cdn Only

## UPCHKE - Check EFT Details (view UP0202)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ+CATEGORY+LINENO+BKACCTCODE+LINETYPE; EMPLOYEE+PEREND+ENTRYSEQ+PCATEGORY+PLINETYPE+LINENO+BKACCTCODE+LINETYPE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence By Employee
  CATEGORY Integer Category code [11=EFT Entry]
  LINENO Integer Unique Key Field
  BKACCTCODE String*6 Bank Account Code
  LINETYPE Integer Presentation List Type Pay [6=n/a]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BASEAMT BCD*10.3 Base Amount
  AMTPCT BCD*9.5 Amt/Pct to be deposited
  DEPOSITAMT BCD*10.3 Deposit Amount
  PCATEGORY Integer Print Category [6=CHKE EFT Entries]
  PLINETYPE Integer Print Line Type [91=CHKE EFT Entry - Fixed Amount,92=CHKE EFT Entry - % of Gross Earnings,93=CHKE EFT Entry - % of Net Pay]
  PCONTENTS Integer Print Line Contents [1=CHKD Employee Only]

## UPCHKH - Check Header (view UP0048)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ; TRANSDATE+EMPLOYEE+ENTRYSEQ; PRPOSTSTAT+PEREND+EMPLOYEE+ENTRYSEQ [M]; POSTSEQ+EMPLOYEE+PEREND+ENTRYSEQ [M]; BANK+TRANSNUM+SERIAL [D,M]; PRPOSTSTAT+PAYFREQ+EMPLOYEE+PEREND+ENTRYSEQ [M]; PRPOSTSTAT+CLASS1+EMPLOYEE+PEREND+ENTRYSEQ [M]; PRPOSTSTAT+CLASS2+EMPLOYEE+PEREND+ENTRYSEQ [M]; PRPOSTSTAT+CLASS3+EMPLOYEE+PEREND+ENTRYSEQ [M]; PRPOSTSTAT+CLASS4+EMPLOYEE+PEREND+ENTRYSEQ [M]; PRPOSTSTAT+EMPLOYEE+PEREND+ENTRYSEQ [M]; GLDRDWNLNK [D,M]
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ENTRYTYPE Integer Type of Check [1=System Check,2=Manual Check,3=Adjustment,4=History Entry,5=Reversed Check]
  BANK String*8 Bank ID
  TRANSNUM BCD*8.0 Transaction Number
  TRANSDATE Date Transaction Date
  PERSTART Date Period Start Date
  TIMESLATE Integer Times Late This Period/Timecard
  CHECKSTAT Integer Check Status [1=Align,2=Void,3=Outstanding,4=Reversed,5=Cleared,6=Cleared With Error,7=Non-negotiable,8=Continuation]
  PRPOSTSTAT Integer PR Post Status [1=Not Posted,2=Posted]
  GLPOSTSTAT Integer Sent to G/L [1=Not sent,2=Sent,3=Not to be sent]
  PAYFREQ Integer Pay Frequency [2=Daily,3=Weekly,4=Biweekly,5=Semimonthly,10=Twenty-two per Year,9=Thirteen per Year,6=Monthly,8=Ten per Year,7=Quarterly]
  CLASS1 String*6 Class 1
  CLASS2 String*6 Class 2
  CLASS3 String*6 Class 3
  CLASS4 String*6 Class 4
  SERIAL ??? Bank Serial Number
  CALCSEQ Long Calculation Sequence
  POSTSEQ Long Posting Sequence
  PRPERIOD Integer Payroll Period
  TRANSAMT BCD*10.3 Transaction Amt
  GLSEG1 String*15 G/L Segment One
  GLSEG2 String*15 G/L Segment Two
  GLSEG3 String*15 G/L Segment Three
  BANKACCT String*45 Bank General Ledger Account
  WORKPROV Integer RESERVED - Cdn Only
  TAXPLAN String*6 Employee EI ID
  EXRATE BCD*8.7 Exchange Rate
  RATEOP Integer Rate Operator
  EFTSTAT Integer EFT Status [0=Not to be EFTed,1=Not EFTed,2=EFTed]
  EFTRUNSEQ Long EFT Run Sequence
  VALUES Long Number of Optional Fields
  GLDRDWNLNK BCD*10.0 G/L Drilldown Link
  OTOVERRIDE Boolean Overtime Override
  OTCALCTYPE Integer Overtime Calculation [0=Hourly Rate,1=Minimum Wage,2=Shift Rate,3=FLSA-Hourly,4=FLSA-Salary Fixed Hours,5=FLSA-Salary Fluctuating Hours]
  SWEXTERNTC Integer Based on External Timecards [0=No,1=Yes]
  SWJOB Boolean Job Related
  EXRATEDATE Date Exchange Rate Date
  ORGTYPE Integer Original Type [1=System Check,2=Manual Check,3=Adjustment,4=History Entry,5=Reversed Check]
  CSEFTSTAT Integer Child Support EFT Status [0=Not EFTed,1=EFTed]
  GLSEG4 String*15 G/L Segment Four
  GLSEG5 String*15 G/L Segment Five
  GLSEG6 String*15 G/L Segment Six

## UPCHKL - Check Selection List (view UP0113)
Keys (first = PK; D=dups allowed, M=modifiable): SELSEQ+EMPLOYEE+PEREND+ENTRYSEQ; SELSEQ+LASTNAME+EMPLOYEE+PEREND+ENTRYSEQ; SELSEQ+STRSORT+EMPLOYEE+PEREND+ENTRYSEQ; SELSEQ+STRSORT+LASTNAME+EMPLOYEE+PEREND+ENTRYSEQ; SELSEQ+LONGSORT+EMPLOYEE+PEREND+ENTRYSEQ; SELSEQ+LONGSORT+LASTNAME+EMPLOYEE+PEREND+ENTRYSEQ; SELSEQ+DATESORT+EMPLOYEE+PEREND+ENTRYSEQ; SELSEQ+DATESORT+LASTNAME+EMPLOYEE+PEREND+ENTRYSEQ; SELSEQ+NUMSORT+EMPLOYEE+PEREND+ENTRYSEQ
Fields (NAME type description [values]):
  SELSEQ Long Selection Sequence
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LASTNAME String*20 Last Name
  FIRSTNAME String*15 First Name
  MIDDLENAME String*15 Middle Name
  STRSORT String*20 String Sort
  LONGSORT Long Long Sort
  NUMSORT BCD*8.0 Number Sort
  DATESORT Date Date Sort
  CLASS String*6 Class
  PAYFREQ Integer Pay Frequency
  TRANSNUM BCD*8.0 Check Number
  TRANSDATE Date Check Date
  POSTSEQ Long Posting Sequence

## UPCHKO - Check Run Optional Field Values (view UP0139)
Keys (first = PK; D=dups allowed, M=modifiable): CALCSEQ+OPTFIELD; OPTFIELD+CALCSEQ
Fields (NAME type description [values]):
  CALCSEQ Long Calculation Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPCHKR - Check Run Header (view UP0088)
Keys (first = PK; D=dups allowed, M=modifiable): CALCSEQ
Fields (NAME type description [values]):
  CALCSEQ Long Calculation Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BEGEMP String*12 Beginning Employee
  ENDEMP String*12 Ending Employee
  BEGCLASS1 String*6 Beginning Class 1
  ENDCLASS1 String*6 Ending Class 1
  BEGCLASS2 String*6 Beginning Class 2
  ENDCLASS2 String*6 Ending Class 2
  BEGCLASS3 String*6 Beginning Class 3
  ENDCLASS3 String*6 Ending Class 3
  BEGCLASS4 String*6 Beginning Class 4
  ENDCLASS4 String*6 Ending Class 4
  SELECTLIST String*8 Selection List
  RUNDATE Date Run Date
  ENDDATE Date End Date
  CHECKDATE Date Check Date
  PRPERIOD Integer Pay period
  ADVANCERUN Boolean Advance run only
  UNPOST Boolean Delete current activity
  EDAILY Boolean Employee frequency - daily
  EWEEKLY Boolean Employee frequency - Weekly
  EBIWEEKLY Boolean Employee frequency - BiWeekly
  ESEMIMONTH Boolean Employee frequency - Semimonthly
  E22PERIODS Boolean Employee frequency - 22 Periods
  E13PERIODS Boolean Employee frequency - 13 Periods
  EMONTHLY Boolean Employee frequency - Monthly
  E10PERIODS Boolean Employee frequency - 10 Period
  EQUARTERLY Boolean Employee frequency - Quarterly
  EDDAILY Boolean Earn/Ded freq - daily
  EDWEEKLY Boolean Earn/Ded freq - weekly
  EDBIWEEKLY Boolean Earn/Ded freq - biweekly
  EDSEMIMTH Boolean Earn/Ded freq - semimonthly
  ED22PERIOD Boolean Earn/Ded freq - 22 periods per year
  ED13PERIOD Boolean Earn/Ded freq - 13 periods per year
  EDMONTHLY Boolean Earn/Ded freq - monthly
  ED10PERIOD Boolean Earn/Ded freq - 10 periods per year
  EDQTRLY Boolean Earn/Ded freq - quarterly
  EWWEEKLY Boolean Earn/Ded freq - weekly
  EWBIWEEKLY Boolean Earn/Ded freq - biweekly
  EWSEMIMTH Boolean Earn/Ded freq - semimonthly
  EW22PERIOD Boolean Earn/Ded freq - 22 periods per year
  EW13PERIOD Boolean Earn/Ded freq - 13 periods per year
  EWMONTHLY Boolean Earn/Ded freq - monthly
  EW10PERIOD Boolean Earn/Ded freq - 10 periods per year
  EWQTRLY Boolean Earn/Ded freq - quarterly
  EBBIWEEKLY Boolean Earn/Ded freq - biweekly
  EBSEMIMTH Boolean Earn/Ded freq - semimonthly
  EB22PERIOD Boolean Earn/Ded freq - 22 periods per year
  EB13PERIOD Boolean Earn/Ded freq - 13 periods per year
  EBMONTHLY Boolean Earn/Ded freq - monthly
  EB10PERIOD Boolean Earn/Ded freq - 10 periods per year
  EBQTRLY Boolean Earn/Ded freq - quarterly
  ESSEMIMTH Boolean Earn/Ded freq - semimonthly
  ES22PERIOD Boolean Earn/Ded freq - 22 periods per year
  ES13PERIOD Boolean Earn/Ded freq - 13 periods per year
  ESMONTHLY Boolean Earn/Ded freq - monthly
  ES10PERIOD Boolean Earn/Ded freq - 10 periods per year
  ESQTRLY Boolean Earn/Ded freq - quarterly
  EC22PERIOD Boolean Earn/Ded freq - 22 periods per year
  EC13PERIOD Boolean Earn/Ded freq - 13 periods per year
  ECMONTHLY Boolean Earn/Ded freq - monthly
  EC10PERIOD Boolean Earn/Ded freq - 10 periods per year
  ECQTRLY Boolean Earn/Ded freq - quarterly
  EX13PERIOD Boolean Earn/Ded freq - 13 periods per year
  EXMONTHLY Boolean Earn/Ded freq - monthly
  EX10PERIOD Boolean Earn/Ded freq - 10 periods per year
  EXQTRLY Boolean Earn/Ded freq - quarterly
  EMMONTHLY Boolean Earn/Ded freq - monthly
  EM10PERIOD Boolean Earn/Ded freq - 10 periods per year
  EMQTRLY Boolean Earn/Ded freq - quarterly
  EA10PERIOD Boolean Earn/Ded freq - 10 periods per year
  EAQTRLY Boolean Earn/Ded freq - quarterly
  EQQTRLY Boolean Earn/Ded freq - quarterly
  BDDAILY Date Period start date for Daily period
  BDWEEKLY Date Period start date for Weekly period
  BDBIWEEKLY Date Period start date for Biweekly period
  BDSEMIMTH Date Period start date for Semimonthly period
  BD22PERIOD Date Period start date for 22 period
  BD13PERIOD Date Period start date for 13 period
  BDMONTHLY Date Period start date for Monthly period
  BD10PERIOD Date Period start date for 10 period
  BDQTRLY Date Period start date for Quarterly period
  GLSEGREPOP Integer Segment replacement option
  GLSEG1 String*6 Segment Code 1
  GLSEG2 String*6 Segment Code 2
  GLSEG3 String*6 Segment Code 3
  NETPRACCT String*45 Net Payroll Account
  SUSPACCT String*45 Payroll Suspense Account
  ENTRYTYPE Integer Entry Type [1=System Check,2=Manual Check,3=Adjustment,4=History Entry,5=Reversed Check]
  DOEFTCALC Boolean Do EFT Calculation?
  CALCOPTION Integer Calculation Option [1=All Checks,2=Advance Only,3=Ignore Zero and Negative Checks,4=Ignore Negative Checks]
  DIFFACCT String*45 Exchange Rounding Difference Account
  VALUES Long Number of Optional Fields
  GLSEG4 String*6 Segment Code 4
  GLSEG5 String*6 Segment Code 5
  GLSEG6 String*6 Segment Code 6

## UPCHKS - Check History Summary (view UP0077)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+ENTRYSEQ; USERSORT [D,M]
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  ENTRYSEQ Long Entry Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSDATE Date Transaction Date
  USERSORT String*100 User Sort
  BANK String*8 Bank
  TRANSNUM BCD*8.0 Check Number
  PERSTART Date Period Start Date
  TRANSAMT BCD*10.3 Transaction Amt
  CHECKSTAT Integer Check Status
  EXRATE BCD*8.7 Exchange Rate
  RATEOP Integer Rate Operator
  GLDRDWNLNK BCD*10.0 Drilldown Link
  EXRATEDATE Date Exchange Rate Date

## UPCLAS - Class Codes (view UP0006)
Keys (first = PK; D=dups allowed, M=modifiable): CLASS+CLASSCODE
Fields (NAME type description [values]):
  CLASS Integer Class
  CLASSCODE String*6 Class Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CLASSDESC String*20 Description

## UPCLCO - Calculate Payroll Optional Fields (view UP0137)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY+OPTFIELD; OPTFIELD+DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy Field
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPCOBK - Company EFT Banks (view UP0200)
Keys (first = PK; D=dups allowed, M=modifiable): BANKID
Fields (NAME type description [values]):
  BANKID String*8 Company EFT Bank
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BANKFORMAT Integer Bank Format [21=ACH (NACHA) Standard,22=ACH (NACHA) Non Standard with Offset Record,23=CSB CoreState Bank,24=IAT Transfers]
  ORIGNUM String*10 Originator Number
  COMPABREV String*16 Company Abbreviated Name
  COMPLNAME String*30 RESERVED - Cdn Only
  DATACENTER String*5 RESERVED - Cdn Only
  INSTIDRTN String*9 RESERVED - Cdn Only
  ACCTNORTN String*18 RESERVED - Cdn Only
  RESERVDORG String*15 RESERVED - Cdn Only
  ELEMENTID String*11 RESERVED - Cdn Only
  REGLECODE String*2 RESERVED - Cdn Only
  CPATRNCODE String*3 RESERVED - Cdn Only
  CODISCDATA String*20 Company Discretionary Name
  SERVCLASS String*3 Service Class Code
  ORIGSTATUS Integer Originator Status Code [1=1 - Bound,2=2 - Unbound]
  ORIGDFIID String*9 Originator DFI ID
  ALTIMMDEST Boolean Use Alternative Imm. Dest. ID?
  IMMDESTID String*10 Immediate Destination ID
  IMMDESTNAM String*23 Immediate Destination Name
  ALTIMMORIG Boolean Use Alternative Imm. Origin No.?
  IMMORIGNUM String*10 Immediate Origin No.
  IMMORIGNAM String*23 Immediate Origin Name
  OFFRECTYPE String*1 Offset Record Type Code
  OFFTRNCODE Integer Offset Transaction Code [0=,27=27 - Checking,37=37 - Savings]
  OFFRDFIID String*9 Offset Receiving DFI ID
  OFFRDFIACC String*17 Offset DFI Account No.
  OFFINDVID String*15 Offset Individual ID No.
  OFFINDVNAM String*22 Offset Individual Name
  OFFDISDATA String*2 Offset Discretionary Data
  APPENDCRLF Boolean Append CR/LF to Each Record?
  FILEHEADER String*250 Deposit File Header
  FILEFOOTER String*250 Deposit File Footer
  DPFILENAME String*8 Deposit File Name
  DPFILEEXT String*3 Deposit File Extension
  EFTRUNSEQ Long Last EFT Run Sequence
  RERUNSEQ Long Last EFT Rerun Sequence
  CREATDATE Date Last File Creation Date
  FILCREATNO String*4 Last File Creation Number
  FILIDMODIF String*1 Last File ID Modifier
  ENTRYDESC String*10 Last File Entry Description
  LASTMAINT Date Last Maintained
  CMBFILECNO String*4 Last Combine File Creation Number
  FREXIND Integer Foreign Exchange Indicator [1=Fixed to Variable,2=Fixed to Fixed]
  FRREFIND Integer Foreign Reference Indicator [1=Foreign Exchange Rate,2=Foreign Exchange Reference Number,3=Space Filled]
  FREXREF String*15 Foreign Exchange Reference
  TRANSTYPE Integer Transaction Type [0=ANN- Annuity,1=DEP- Deposit,2=LOA- Loan,3=MIS- Miscellaneous,4=MOR- Mortgage,5=PEN- Pension,6=RLS- Rent/Lease,7=SAL- Salary/Payroll,8=TAX- Tax,9=TEL- Telephone Initiated Entry,10=WEB- Web Initiated Entry]
  CMPENTDESC String*10 Company Entry Description
  ITMTRANUM Integer RESERVED - Cdn Only
  ORIGDFICTY String*3 Originator DFI Country Code
  EFTTYPE Integer EFT Type [1=Direct Deposit EFT,2=Child Support EFT]
  CASESTATE String*2 Case State

## UPDDOPTS - Direct Deposit Options (view UP0213)
Keys (first = PK; D=dups allowed, M=modifiable): PROPTID
Fields (NAME type description [values]):
  PROPTID String*4 Option Record ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SPRCOMPID String*36 Sage 300 Direct Deposit ID
  FEEBANK String*8 Fees Bank
  FEEEXPACCT String*45 Fees G/L Expense Account

## UPDIST - Distribution (view UP0009)
Keys (first = PK; D=dups allowed, M=modifiable): EARNDED+DISTCODE
Fields (NAME type description [values]):
  EARNDED String*6 Earning/Deduction
  DISTCODE String*6 Distribution Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISTRNAME String*15 Distribution Description
  EXPACCT String*45 Regular Expense G/L Account
  OTACCT String*45 Overtime Expense G/L Account
  SHIFTACCT String*45 Shift Differential Exp G/L Acct
  ELIABACCT String*45 Employee Liability G/L Account
  RLIABACCT String*45 Employer Liability G/L Account
  ASSETACCT String*45 Advances Receivable G/L Account

## UPDTLB - Earnings Billing Detail (view UP0040)
Keys (first = PK; D=dups allowed, M=modifiable): EARNDED+CURRCODE
Fields (NAME type description [values]):
  EARNDED String*6 Earning Code
  CURRCODE String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BILLRATE1 BCD*10.6 Billing Rate 1
  BILLRATE2 BCD*10.6 Billing Rate 2
  BILLRATE3 BCD*10.6 Billing Rate 3
  BILLRATE4 BCD*10.6 Billing Rate 4
  BILLRATE5 BCD*10.6 Billing Rate 5
  BILLRATE6 BCD*10.6 Billing Rate 6

## UPDTLM - Earnings/Deductions (view UP0007)
Keys (first = PK; D=dups allowed, M=modifiable): EARNDED; CATEGORY+EARDEDTYPE+EARNDED
Fields (NAME type description [values]):
  EARNDED String*6 Earning/Deduction
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LONGDESC String*60 Earning/Deduction Description
  SHORTDESC String*15 Earning/Deduction Short Description
  INACTIVE Boolean Inactive
  ASOF Date Inactive As Of
  LASTMAINT Date Last Maintained
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit]
  EARDEDTYPE Integer Type [1=Salary & Wages,2=Reported Tips,3=Allocated Tips]
  FREQUENCY Integer Frequency [1=Float,2=Daily,3=Weekly,4=Biweekly,5=Semimonthly,10=Twenty-two per Year,9=Thirteen per Year,6=Monthly,8=Ten per Year,7=Quarterly]
  STARTS Integer Starts [1=Specific Month/Day,2=Date of Hire,3=Months after Hire,4=Days after Hire]
  STARTMONTH Integer Start Month
  STARTDAY Integer Start Day
  ENDS Date Ends
  PRNTONCHK Boolean Print On Check
  PRNTIF0 Boolean RESERVED Print If Current Zero.
  PRNTYTDIF0 Boolean RESERVED Print YTD If Current Zero
  ECALCMETH Integer Employee Calculation Method [2=Flat,3=Fixed,4=Hourly Rate,5=Amount per Hour,6=Piece Rate Table,7=Percentage of Base,8=Sales Commission Table]
  EW2BOX Integer Employee W-2 Box [1=Not Applicable,2=Other Information Box,3=Dependent Care,4=Employee 401(k),5=Employee 403(b),6=Employee 408(k)(6),7=Employee 457,8=Employee 501(c)(18)(d),9=SIMPLE Retirement Acct,10=Deferrals under section 409A,11=Roth contributions to Employee 401(k),12=Roth contributions to Employee 403(b),13=Health Savings Account,14=Employer Provided Health Care,15=Roth contributions under governmental 457(b)]
  ERATE BCD*9.5 Employee Rate
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
  E10PPPYMIN BCD*10.3 Employee Ten Period/Year Minimum
  E10PPPYMAX BCD*10.3 Employee Ten Period/Year Maximum
  E13PPPYMIN BCD*10.3 Employee Thirteen Period/Year Minimum
  E13PPPYMAX BCD*10.3 Employee Thirteen Period/Year Maximum
  E22PPPYMIN BCD*10.3 Employee Twentytwo Period/Year Minimum
  E22PPPYMAX BCD*10.3 Employee Twentytwo Period/Year Maximum
  ELIMITBASE Integer Employee Base Limit [1=No Limit]
  WGBRACK1 BCD*10.3 Wage Bracket 1
  WGADDAMT1 BCD*10.3 Add Amount 1
  WGPCTOVR1 BCD*5.5 Percnt. of Excess 1
  WGBRACK2 BCD*10.3 Wage Bracket 2
  WGADDAMT2 BCD*10.3 Add Amount 2
  WGPCTOVR2 BCD*5.5 Percnt. of Excess 2
  WGBRACK3 BCD*10.3 Wage Bracket 3
  WGADDAMT3 BCD*10.3 Add Amount 3
  WGPCTOVR3 BCD*5.5 Percnt. of Excess 3
  WGBRACK4 BCD*10.3 Wage Bracket 4
  WGADDAMT4 BCD*10.3 Add Amount 4
  WGPCTOVR4 BCD*5.5 Percnt. of Excess 4
  WGBRACK5 BCD*10.3 Wage Bracket 5
  WGADDAMT5 BCD*10.3 Add Amount 5
  WGPCTOVR5 BCD*5.5 Percnt. of Excess 5
  WGBRACK6 BCD*10.3 Wage Bracket 6
  WGADDAMT6 BCD*10.3 Add Amount 6
  WGPCTOVR6 BCD*5.5 Percnt. of Excess 6
  WGBRACK7 BCD*10.3 Wage Bracket 7
  WGADDAMT7 BCD*10.3 Add Amount 7
  WGPCTOVR7 BCD*5.5 Percnt. of Excess 7
  WGBRACK8 BCD*10.3 Wage Bracket 8
  WGADDAMT8 BCD*10.3 Add Amount 8
  WGPCTOVR8 BCD*5.5 Percnt. of Excess 8
  WGBRACK9 BCD*10.3 Wage Bracket 9
  WGADDAMT9 BCD*10.3 Add Amount 9
  WGPCTOVR9 BCD*5.5 Percnt. of Excess 9
  WGBRACK10 BCD*10.3 Wage Bracket 10
  WGADDAMT10 BCD*10.3 Add Amount 10
  WGPCTOVR10 BCD*5.5 Percnt. of Excess 10
  WGBRACK11 BCD*10.3 Wage Bracket 11
  WGADDAMT11 BCD*10.3 Add Amount 11
  WGPCTOVR11 BCD*5.5 Percnt. of Excess 11
  WGBRACK12 BCD*10.3 Wage Bracket 12
  WGADDAMT12 BCD*10.3 Add Amount 12
  WGPCTOVR12 BCD*5.5 Percnt. of Excess 12
  WGBRACK13 BCD*10.3 Wage Bracket 13
  WGADDAMT13 BCD*10.3 Add Amount 13
  WGPCTOVR13 BCD*5.5 Percnt. of Excess 13
  WGBRACK14 BCD*10.3 Wage Bracket 14
  WGADDAMT14 BCD*10.3 Add Amount 14
  WGPCTOVR14 BCD*5.5 Percnt. of Excess 14
  WGBRACK15 BCD*10.3 Wage Bracket 15
  WGADDAMT15 BCD*10.3 Add Amount 15
  WGPCTOVR15 BCD*5.5 Percnt. of Excess 15
  WGBRACK16 BCD*10.3 Wage Bracket 16
  WGADDAMT16 BCD*10.3 Add Amount 16
  WGPCTOVR16 BCD*5.5 Percnt. of Excess 16
  WGBRACK17 BCD*10.3 Wage Bracket 17
  WGADDAMT17 BCD*10.3 Add Amount 17
  WGPCTOVR17 BCD*5.5 Percnt. of Excess 17
  WGBRACK18 BCD*10.3 Wage Bracket 18
  WGADDAMT18 BCD*10.3 Add Amount 18
  WGPCTOVR18 BCD*5.5 Percnt. of Excess 18
  WGBRACK19 BCD*10.3 Wage Bracket 19
  WGADDAMT19 BCD*10.3 Add Amount 19
  WGPCTOVR19 BCD*5.5 Percnt. of Excess 19
  WGBRACK20 BCD*10.3 Wage Bracket 20
  WGADDAMT20 BCD*10.3 Add Amount 20
  WGPCTOVR20 BCD*5.5 Percnt. of Excess 20
  RCALCMETH Integer Employer Calculation Method [2=Flat,5=Amount per Hour,6=Piece Rate Table,7=Percentage of Base,8=Sales Commission Table,9=Wage Bracket Table]
  RW2BOX Integer Employer W-2 Box [1=Not Applicable,2=Other Information Box,3=Allocated Tips,4=Dependent Care,5=Fringe Benefit,6=Cost of Group Term over $50,000,7=Uncollected Soc Sec Tax on Cost of Group Term over $50,000,8=Uncollected Medicare Tax on Cost of Group Term over $50,000,9=Sick Pay Not Includible as Income (3rd Party Sick Pay),10=Excess Golden,11=Allowed per Diem,12=Nonqualified Plan,13=Section 457,14=Excludable Moving Expense Reimbursements,15=Nontaxable combat pay,16=Medical Savings Acct,17=Adoption Benefit,18=Non-statutory Stock Options,19=Health Savings Account,20=Income under section 409A,21=Employer Provided Health Care,22=Permitted Benefits Under a QSEHRA]
  RRATE BCD*9.5 Employer Rate
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
  R10PPPYMIN BCD*10.3 Employer Ten Per/Year Minimum
  R10PPPYMAX BCD*10.3 Employer Ten Per/Year Maximum
  R13PPPYMIN BCD*10.3 Employer Thirteen Per/Year Minimum
  R13PPPYMAX BCD*10.3 Employer Thirteen Per/Year Maximum
  R22PPPYMIN BCD*10.3 Employer TwentyTwo Per/Year Minimum
  R22PPPYMAX BCD*10.3 Employer TwentyTwo Per/Year Maximum
  RLIMITBASE Integer Employer Base Limit [1=No Limit]
  ALLOWWCC Boolean Subject to Workers' Compensation
  COMMAMT1 BCD*10.3 Commission Amt. 1
  COMMPCT1 BCD*5.5 Commission Pct. 1
  COMMAMT2 BCD*10.3 Commission Amt. 2
  COMMPCT2 BCD*5.5 Commission Pct. 2
  COMMAMT3 BCD*10.3 Commission Amt. 3
  COMMPCT3 BCD*5.5 Commission Pct. 3
  COMMAMT4 BCD*10.3 Commission Amt. 4
  COMMPCT4 BCD*5.5 Commission Pct. 4
  COMMAMT5 BCD*10.3 Commission Amt. 5
  COMMPCT5 BCD*5.5 Commission Pct. 5
  COMMPCTX BCD*5.5 Commission Amt. excess
  PIECNUM1 BCD*10.3 Piece count 1
  PIECAMT1 BCD*9.5 Piece amount 1
  PIECNUM2 BCD*10.3 Piece count 2
  PIECAMT2 BCD*9.5 Piece amount 2
  PIECNUM3 BCD*10.3 Piece count 3
  PIECAMT3 BCD*9.5 Piece amount 3
  PIECNUM4 BCD*10.3 Piece count 4
  PIECAMT4 BCD*9.5 Piece amount 4
  PIECNUM5 BCD*10.3 Piece count 5
  PIECAMT5 BCD*9.5 Piece amount 5
  PIECAMTX BCD*9.5 Max Piece Rate Amt.
  TIPDISB Boolean Tip Disbursement
  PAYDOWNDED Boolean Repayment Deduction
  REPAYID String*6 Advance to Be Repaid
  CARRYOVER Integer Carry-over [1=Specific Month/Day,2=Date of Hire,3=Months after Hire,4=Days after Hire]
  COVERDAY Integer Carry-over Day
  COVERMONTH Integer Carry-over Month
  POSTLIAB Boolean Post Liab.
  SVCYEAR1 Integer Service Year 1
  BEGHRS1 BCD*10.3 Beginning Hours 1
  INCRHRS1 BCD*9.5 Increment Hours 1
  MAXACCR1 BCD*10.3 Max. Annual Accrual 1
  MAXCARRY1 BCD*10.3 Max. Carry-over Hours 1
  SVCYEAR2 Integer Service Year 2
  BEGHRS2 BCD*10.3 Beginning Hours 2
  INCRHRS2 BCD*9.5 Increment Hours 2
  MAXACCR2 BCD*10.3 Max. Annual Accrual 2
  MAXCARRY2 BCD*10.3 Max. Carry-over Hours 2
  SVCYEAR3 Integer Service Year 3
  BEGHRS3 BCD*10.3 Beginning Hours 3
  INCRHRS3 BCD*9.5 Increment Hours 3
  MAXACCR3 BCD*10.3 Max. Annual Accrual 3
  MAXCARRY3 BCD*10.3 Max. Carry-over Hours 3
  SVCYEAR4 Integer Service Year 4
  BEGHRS4 BCD*10.3 Beginning Hours 4
  INCRHRS4 BCD*9.5 Increment Hours 4
  MAXACCR4 BCD*10.3 Max. Annual Accrual 4
  MAXCARRY4 BCD*10.3 Max. Carry-over Hours 4
  LEVEL Integer Level
  LISTUSEBHI Integer Base Hours List Use
  REGULARBHI Integer Base Hours Regular
  OVRTIMEBHI Integer Base Hours Overtime
  LISTUSEBEI Integer Base Earnings List Use
  REGULARBEI Integer Base Earnings Regular
  OVRTIMEBEI Integer Base Earnings Overtime
  SHIFTBEI Integer Base Earnings Shift
  LISTUSEBDI Integer Base Deductions List Use
  LISTUSEBTI Integer Base Tax List Use
  LISTUSETTW Integer List Use of Type of Taxable Wages
  WHMETHTTW Integer Withholding Method for Taxable Wages [1=Regular Rate,4=Taxable, No Withholding,6=Supplemental Withholding]
  LISTUSETDB Integer Take Deduction Before List Use
  ET4BOX Integer RESERVED - Cdn Only
  RT4BOX Integer RESERVED - Cdn Only
  ER1BOX Integer RESERVED - Cdn Only
  RR1BOX Integer RESERVED - Cdn Only
  EASSOCW2SW Boolean Associate W-2 printing
  EASSOCTAX String*6 Associated Tax
  RASSOCW2SW Boolean Associate W-2 printing
  RASSOCTAX String*6 Associated Tax
  POSTBENE Boolean Post Benefit
  PAYACCRUAL Boolean Pay Accrual
  NONPERPYMT Boolean RESERVED - Cdn Only
  LINKEARN String*6 Linked Earning
  VALUES Long Number of Optional Fields
  SWFLSA Boolean Include in FLSA Overtime Calc
  COMMINCREM Boolean Progressive Calc - Commissions
  WGANNUALIZ Boolean Annualized Wage Brackets
  WGBRINCREM Boolean Progressive Calc - Wage Brackets
  PIECINCREM Boolean Progressive Calc - Piece Rate
  ELIFETMMAX BCD*10.3 Employee Lifetime Maximum
  RLIFETMMAX BCD*10.3 Employer Lifetime Maximum
  E2NDRATEIN Integer Employee Sec. Rate Effective [0=Never,1=After Annual Maximum Reached]
  R2NDRATEIN Integer Employer Sec. Rate Effective [0=Never,1=After Annual Maximum Reached]
  E2NDRATE BCD*9.5 Employee Secondary Rate
  R2NDRATE BCD*9.5 Employer Secondary Rate
  SVCYEAR5 Integer Service Year 5
  BEGHRS5 BCD*10.3 Beginning Hours 5
  INCRHRS5 BCD*9.5 Increment Hours 5
  MAXACCR5 BCD*10.3 Max. Annual Accrual 5
  MAXCARRY5 BCD*10.3 Max. Carry-over Hours 5
  SVCYEAR6 Integer Service Year 6
  BEGHRS6 BCD*10.3 Beginning Hours 6
  INCRHRS6 BCD*9.5 Increment Hours 6
  MAXACCR6 BCD*10.3 Max. Annual Accrual 6
  MAXCARRY6 BCD*10.3 Max. Carry-over Hours 6
  SVCYEAR7 Integer Service Year 7
  BEGHRS7 BCD*10.3 Beginning Hours 7
  INCRHRS7 BCD*9.5 Increment Hours 7
  MAXACCR7 BCD*10.3 Max. Annual Accrual 7
  MAXCARRY7 BCD*10.3 Max. Carry-over Hours 7
  SVCYEAR8 Integer Service Year 8
  BEGHRS8 BCD*10.3 Beginning Hours 8
  INCRHRS8 BCD*9.5 Increment Hours 8
  MAXACCR8 BCD*10.3 Max. Annual Accrual 8
  MAXCARRY8 BCD*10.3 Max. Carry-over Hours 8
  SVCYEAR9 Integer Service Year 9
  BEGHRS9 BCD*10.3 Beginning Hours 9
  INCRHRS9 BCD*9.5 Increment Hours 9
  MAXACCR9 BCD*10.3 Max. Annual Accrual 9
  MAXCARRY9 BCD*10.3 Max. Carry-over Hours 9
  SVCYEAR10 Integer Service Year 10
  BEGHRS10 BCD*10.3 Beginning Hours 10
  INCRHRS10 BCD*9.5 Increment Hours 10
  MAXACCR10 BCD*10.3 Max. Annual Accrual 10
  MAXCARRY10 BCD*10.3 Max. Carry-over Hours 10
  CCOVERRIDE Boolean Cost Center Override Based on Calc Base
  BILLINGS Long Billing Rates
  BILLPCT1 BCD*5.5 Billing Percentage 1
  BILLPCT2 BCD*5.5 Billing Percentage 2
  BILLPCT3 BCD*5.5 Billing Percentage 3
  BILLPCT4 BCD*5.5 Billing Percentage 4
  BILLPCT5 BCD*5.5 Billing Percentage 5
  BILLPCT6 BCD*5.5 Billing Percentage 6
  MAXONREM Boolean Calc. Max. Carry-over based on Remaining Balance
  MAXONACCR Boolean Cap Accrual at Max. Accrual
  COVID Integer Report as [0=None,10=Form W-2 - Exempt Overtime Pay (Alabama Only),1=Form 941 - Emergency Paid Sick Leave,8=Form 941 - Emergency Paid Sick Leave for Others,2=Form 941 - Emergency Paid Family Leave,3=Form 941 - Qualified Retention Credit Earnings]
  OTHERBOX Integer RESERVED - CDN Only [1=028 - Other income,2=032 - Registered pension plan contributions...,3=104 - Research grants,4=105 - Scholarships, bursaries, fellowships...,5=107 - Payments from a wage-loss replacement...,6=130 - Apprenticeship, incentive grant or...,7=144 - Indian (exempt income)  Other income,8=152 - SUBP qualified under the Income Tax Act]

## UPDTLO - Earnings/Deductions Opt Fields (view UP0123)
Keys (first = PK; D=dups allowed, M=modifiable): EARNDED+OPTFIELD; OPTFIELD+EARNDED
Fields (NAME type description [values]):
  EARNDED String*6 Earning/Deduction
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPECMM - Employee Comments (view UP0119)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+ENTERED+UNIQUIFIER; EMPLOYEE+FOLLOWUP+UNIQUIFIER [M]
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  ENTERED Date Date Entered
  UNIQUIFIER Long Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRES Date Expiry Date
  FOLLOWUP Date Follow-up Date
  USERID String*8 User ID
  COMMENTTYP String*8 Comment Type
  COMMENT0 String*250 Reserved (comment0)
  COMMENT1 String*250 Reserved (comment1)
  COMMENT2 String*250 Reserved (comment2)
  COMMENT3 String*250 Reserved (comment3)
  COMMENT4 String*250 Reserved (comment4)
  COMMENT5 String*250 Reserved (comment5)
  COMMENT6 String*250 Reserved (comment6)
  COMMENT7 String*250 Reserved (comment7)
  COMMENT8 String*250 Reserved (comment8)
  COMMENT9 String*250 Reserved (comment9)

## UPEDUP - Duplicate SSN (view UP0106)
Keys (first = PK; D=dups allowed, M=modifiable): SSN+EMPLOYEE
Fields (NAME type description [values]):
  SSN String*11 Social Security Number
  EMPLOYEE String*12 Employee
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RESERVED Integer Reserved
  ORGUSERID String*8 Original User ID

## UPEHRP - Earnings Hourly Report (view UP0093)
Keys (first = PK; D=dups allowed, M=modifiable): RPTTIME+RPTSUMRY+EMPLOYEE+SORTORDER+PLINETYPE+EARNDED+LINETYPE+CLASSSUM+CLASS; RPTTIME+RPTSUMRY+CLASS+CLASSSUM+EMPLOYEE+SORTORDER+PLINETYPE+EARNDED+LINETYPE
Fields (NAME type description [values]):
  RPTTIME Long Time
  RPTSUMRY Boolean Report Summary
  EMPLOYEE String*12 Employee
  SORTORDER Integer Sort Order [1=n/a,2=Earning,3=Gross Pay,4=Cash Benefit,5=Total Earnings,6=Expense Reimbursemnt,7=Cash Advance,8=Taxes and Deductions,9=Net Pay,10=NonCash Item,11=NonCash Advance,12=Accural,13=Hours,14=Hours,15=Pieces,16=Sales]
  PLINETYPE Integer P Line Type [11=CHKD Regular Line,11=CHKD Overtime Line,11=CHKD Shift Diff Line,14=CHKD Disbursed Tips,15=CHKD Vacation Payment,16=CHKD Sick Payment,17=CHKD Comp. Time Payment,21=CHKD Deduction Entry,31=CHKD Federal Income Entry,32=CHKD Federal Insurance Entry,33=CHKD Federal UI Entry,34=CHKD Federal Pension Entry,35=CHKD Federal Health Entry,36=CHKD Federal Other Entry,41=CHKD State Income Entry,42=CHKD State Insurance Entry,43=CHKD State UI Entry,44=CHKD State Pension Entry,45=CHKD State Health Entry,46=CHKD State Other Entry,51=CHKD Local Income Entry,52=CHKD Local Insurance Entry,53=CHKD Local UI Entry,54=CHKD Local Pension Entry,55=CHKD Local Health Entry,56=CHKD Local Other Entry,61=CHKD User Income Entry,62=CHKD User Insurance Entry,63=CHKD User UI Entry,64=CHKD User Pension Entry,65=CHKD User Health Entry,66=CHKD User Other Entry,71=CHKD Exp Reimbursement,72=CHKD Cash Advance,73=CHKD Reported Tips,74=CHKD Allocated Tips,75=CHKD Noncash Advance,76=CHKD Vac Accrual,77=CHKD Sick Accrual,78=CHKD Comp Accrual,81=CHKD Cash Benefit,82=CHKD Noncash Benefit]
  EARNDED String*6 E/D or Tax
  LINETYPE Integer Line Type [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  CLASSSUM Boolean Class Summary Line
  CLASS String*6 Class Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MONTHAMT BCD*10.3 Month Amt
  QUARTERAMT BCD*10.3 Quarter Amt
  YEARAMT BCD*10.3 Year Amt
  MHOURS BCD*9.3 Month Hours
  QHOURS BCD*9.3 Quarter Hours
  YHOURS BCD*9.3 Year Hours
  LASTNAME String*20 Last Name
  FIRSTNAME String*15 First Name
  MIDDLENAME String*15 Middle Name
  SHORTDESC String*15 Description

## UPELST - EFT Combine File List (view UP0208)
Keys (first = PK; D=dups allowed, M=modifiable): LISTITEM; COMPNAME+BANKID+LISTITEM
Fields (NAME type description [values]):
  LISTITEM Integer File List Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  USEITEM Boolean Use File List Item [0=No,1=Yes]
  FILENAME String*32 File Name
  COMPNAME String*6 Company ID
  FILEDATE Date File Date
  EFTRUNSEQ Long EFT Run Sequence
  RERUNSEQ Long EFT Rerun Sequence
  BANKID String*8 Company EFT Bank ID
  FILETOTAL BCD*10.3 File Total Amt
  FILCREATNO String*4 File Creation Number
  PROCESSED Boolean Processed [0=No,1=Yes]

## UPEMBK - Employee EFT Banks (view UP0201)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+BKACCTCODE; EMPLOYEE+EFTCALCTYP+BKACCTCODE [M]
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  BKACCTCODE String*6 Employee EFT Bank
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BKACCTDESC String*15 Employee EFT Bank Description
  INSTITUTID String*9 Receiving DFI ID
  ACCTNUM String*18 Account Number
  TRANSCODE Integer Transaction Code [22=22 - Checking,32=32 - Savings]
  EFTCALCTYP Integer EFT Calculation Type [1=Fixed Amount,2=% of Gross Earnings,3=% of Net Pay]
  AMTPCT BCD*9.5 Amt/Pct to be deposited
  STARTDATE Date Start Date
  ENDDATE Date End Date
  DCOUNTRY String*3 Destination Country
  DCURRENCY String*3 Destination Currency
  BKIDQUALIF Integer Bank ID Qualifier [1=01- (NACHA) National Clearing System Number,2=02- BIC Bank Identification Number,3=03- IBAN- International Bank Account Number]
  PRENOTE Integer Prenote Status [0=Not Sent,1=Pending,2=Approved,3=Declined]
  TRANSGUID String*36 Sync Transaction GUID

## UPEMCS - Employee Garnishment (view UP0118)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+DEDCODE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  DEDCODE String*6 Deduction Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEDDESC String*60 Deduction's Description
  EFTSTATUS Integer EFT Status [0=Pre-notification,1=Deposit,2=Inactive]
  INSTITUTID String*9 SDU Routing Number
  ACCTNUM String*18 SDU Account Number
  TRANSCODE Integer Transcation Code [22=22 - Checking,32=32 - Savings]
  TRNSFRNAME String*30 SDU Name
  REFERENCE String*19 Reference
  DISCREDATA String*2 Discretionary Data
  CASEID String*20 Case Identifier
  CASESTATE String*2 Case State
  JURISDICTN String*30 Case Jurisdiction
  FIPSCODE String*7 FIPS Code
  CUSTPARENT String*30 Custodial Parent
  MEDINSUAVL Boolean Is family health insurance available? [0=No,1=Yes]
  MEDINSUREQ Boolean Is family health insurance required? [0=No,1=Yes]
  ORDERDATE Date Date of Order

## UPEMDB - Employee Billing Details (view UP0041)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+EARNDED+CURRCODE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  EARNDED String*6 Earning Code
  CURRCODE String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BILLRATE1 BCD*10.6 Billing Rate 1
  BILLRATE2 BCD*10.6 Billing Rate 2
  BILLRATE3 BCD*10.6 Billing Rate 3
  BILLRATE4 BCD*10.6 Billing Rate 4
  BILLRATE5 BCD*10.6 Billing Rate 5
  BILLRATE6 BCD*10.6 Billing Rate 6

## UPEMDO - Empl Earn/Ded Optional Fields (view UP0125)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+EARNDED+OPTFIELD; OPTFIELD+EMPLOYEE+EARNDED
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  EARNDED String*6 Employee Earning/Deduction
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPEMPC - Employee Notes (view UP0053)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+LINENO
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NOTES String*250 Notes

## UPEMPD - Employee Earnings/Deductions (view UP0008)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+EARNDED; EMPLOYEE+CATEGORY+EARDEDTYPE+EARNDED; EARNDED+DISTCODE [D,M]; EARNDED+EMPLOYEE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  EARNDED String*6 Employee Earning/Deduction
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CALCULATE Boolean Calculate [0=No,1=Yes]
  STARTS Date Start date
  ENDS Date End date
  GLSEG1 String*15 Segment Name 1
  GLSEG2 String*15 Segment Name 2
  GLSEG3 String*15 Segment Name 3
  DISTCODE String*6 Distribution code
  ERATE BCD*9.5 Employee Rate/Amt/Pct.
  RRATE BCD*9.5 Employer Amt/Pct.
  WCC String*6 Workers' Compensation Code
  REPAYID String*6 Advance To Be Repaid
  CARRYDATE Date Carry-over
  BALANCE BCD*10.3 Balance
  ACCRUED BCD*10.3 Accrued
  PAID BCD*10.3 Paid
  DEFAULTHRS BCD*4.3 Default hours
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit]
  EARDEDTYPE Integer Type [7=Vacation,8=Sick,9=Compensatory Time]
  AMTPAID BCD*10.3 Amount Paid
  USERTC Boolean Available in Employee Timecards [0=No,1=Yes]
  WCCGROUP String*6 Workers Comp. Group
  VALUES Long Number of Optional Fields
  SWFLSA Boolean Include in FLSA Overtime Calc
  EPERIODMIN BCD*10.3 Employee Period Minimum
  EPERIODMAX BCD*10.3 Employee Period Maximum
  EANNUALMAX BCD*10.3 Employee Annual Maximum
  ELIFETMMAX BCD*10.3 Employee Lifetime Maximum
  ELTDAMT BCD*10.3 Employee Lifetime Accumulation
  E2NDRATE BCD*9.5 Employee Secondary Rate/Amt/Pct.
  RPERIODMIN BCD*10.3 Employer Period Minimum
  RPERIODMAX BCD*10.3 Employer Period Maximum
  RANNUALMAX BCD*10.3 Employer Annual Maximum
  RLIFETMMAX BCD*10.3 Employer Lifetime Maximum
  RLTDAMT BCD*10.3 Employer Lifetime Accumulation
  R2NDRATE BCD*9.5 Employer Secondary Amt/Pct.
  BILLINGS Long Billing Rates
  BILLPCT1 BCD*5.5 Billing Percentage 1
  BILLPCT2 BCD*5.5 Billing Percentage 2
  BILLPCT3 BCD*5.5 Billing Percentage 3
  BILLPCT4 BCD*5.5 Billing Percentage 4
  BILLPCT5 BCD*5.5 Billing Percentage 5
  BILLPCT6 BCD*5.5 Billing Percentage 6
  SWALLOCJOB Boolean Jobs Alloc Based on Calc Base
  GLSEG4 String*15 RESERVED - Segment Name 4
  GLSEG5 String*15 RESERVED - Segment Name 5
  GLSEG6 String*15 RESERVED - Segment Name 6

## UPEMPL - Employees (view UP0014)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE; LASTNAME+FIRSTNAME+MIDDLENAME+EMPLOYEE [M]; CLASS1+EMPLOYEE [M]; CLASS2+EMPLOYEE [M]; CLASS3+EMPLOYEE [M]; CLASS4+EMPLOYEE [M]; TCUSERID+EMPLOYEE [D,M]; MASTGUID [M]
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LASTMAINT Date Last Maintained
  TEMPLATE String*12 Employee Template
  LASTNAME String*20 Last Name
  FIRSTNAME String*15 First Name
  MIDDLENAME String*15 Middle Name
  FULLNAME String*60 Full Name
  ADDRESS1 String*60 Address Line 1
  ADDRESS2 String*60 Address Line 2
  ADDRESS3 String*60 Address Line 3
  ADDRESS4 String*60 Address Line 4
  CITY String*30 City
  STATE String*30 State/Province
  ZIP String*20 ZIP Code
  COUNTRY String*30 Country
  SSN String*11 Social Security Number
  BIRTHDATE Date Birth Date
  STATUS Integer Employment Status [1=Active,2=Inactive,3=Terminated]
  HIREDATE Date Hire Date
  FIREDATE Date Termination Date
  POSITION String*25 Position
  PARTTIME Boolean Part-Time
  PAYFREQ Integer Pay Frequency [2=Daily,3=Weekly,4=Biweekly,5=Semimonthly,10=Twenty-two per Year,9=Thirteen per Year,6=Monthly,8=Ten per Year,7=Quarterly]
  CHECKLANG Integer Check Language [5658=English,7092=French,5845=Spanish,738=Australian,15719=Mexican,2857=Chinese (Simplified),2863=Chinese (Traditional)]
  HRSPERPER BCD*4.3 Hours per Period
  WCC String*6 Workers' Compensation Code
  OTSCHED String*6 Overtime Schedule
  SHIFTSCHED String*6 Shift Differential Schedule
  SHIFTNUM Integer Shift Number
  TIMESLATE Integer Times Late
  ENTRYSEQ Long Entry Sequence
  CLASS1 String*6 Class 1
  CLASS2 String*6 Class 2
  CLASS3 String*6 Class 3
  CLASS4 String*6 Class 4
  GLSEG1 String*15 Segment Code 1
  GLSEG2 String*15 Segment Code 2
  GLSEG3 String*15 Segment Code 3
  PHONE String*30 Phone
  SUPERVSR String*25 Manager
  REVWDATE Date Last Review Date
  LASTRAISE Date Date of Last Raise
  ALTADDR1 String*60 Alternate Address Line 1
  ALTADDR2 String*60 Alternate Address Line 2
  ALTADDR3 String*60 Alternate Address Line 3
  ALTADDR4 String*60 Alternate Address Line 4
  ALTCITY String*30 Alternate City
  ALTSTATE String*30 Alternate State/Province
  ALTZIP String*20 Alternate ZIP/Postal Code
  ALTCNTRY String*30 Alternate Country
  GENDER Integer Gender [1=,2=Male,3=Female,4=Non-binary]
  ETHNIC Integer
  EMERNAME String*60 Emergency Contact
  EMERPHON String*30 Emergency Phone
  MINWAGE BCD*10.3 Minimum Wage
  VACATION String*6 Vacation ID
  SICK String*6 Sick Pay ID
  COMPTIME String*6 Comp. Time ID
  SSNFORMAT Integer SSN Format
  DISABILITY String*6 RESERVED - Cdn Only
  RPP String*7 RESERVED - Cdn Only
  WORKPROV Integer State of Hire
  TCUSERID String*8 Timecard User ID
  DEPOSIT Boolean Direct Deposit
  TRNSFRNAME String*30 Bank Transfer Name
  REFERENCE String*19 Reference
  DISCREDATA String*2 Discretionary Data
  WCCGROUP String*6 Workers Comp. Group
  INACTDATE Date Inactive Date
  VALUES Long Number of Optional Fields
  HRSPERDAY BCD*4.3 Regular Hours Per Day
  OTCALCTYPE Integer Overtime Calculation [0=Hourly Rate,1=Minimum Wage,2=Shift Rate,3=FLSA-Hourly,4=FLSA-Salary Fixed Hours]
  CNTRYCODE String*3 Country Code
  WORKCODE String*6 Work Classification Code
  HRSPERWEEK BCD*4.3 Hours per Week
  SRCEAPPL String*2 Source Application
  EMAIL String*50 E-mail
  WKLYFLSA Boolean Calc OT on a Weekly Basis
  USCITIZEN Boolean US Citizen
  WORKLOC String*50 Work Location
  WLADDR2 String*60 Work Location Address 2
  WLADDR3 String*60 Work Location Address 3
  WLADDR4 String*60 Work Location Address 4
  WLCITY String*30 Work Location City
  WLSTATE String*30 Work Location State/Prov
  WLPOSTAL String*20 Work Location Zip/Postal Code
  WLCOUNTRY String*30 Work Location Country
  GLSEG4 String*15 RESERVED - Segment Code 4
  GLSEG5 String*15 RESERVED - Segment Code 5
  GLSEG6 String*15 RESERVED - Segment Code 6
  MASTGUID String*36 Sync Master GUID
  ELECW2 Integer Employee Electronic W-2 Consent [0=No,1=Yes]
  EEOJOBCATE Integer Job Category [0=,1=Executive/Senior Level Officials and Managers,2=First/Mid-Level Officials and Managers,3=Professionals,4=Technicians,5=Sales Workers,6=Administrative Support Workers,7=Craft Workers,8=Operatives,9=Laborers and Helpers,10=Service Workers]
  EEOETHNIC Integer Ethnicity [0=,1=A - Hispanic or Latino Male,2=B - Hispanic or Latino Female,3=C - White Male,4=D - Black or African American Male,5=E - Native Hawaiian or Pacific Islander Male,6=F - Asian Male,7=G - Native American or Alaska Native Male,8=H - Two or more races Male,9=I - White Female,10=J - Black or African American Female,11=K - Native Hawaiian or Pacific Islander Female,12=L - Asian Female,13=M - Native American or Alaska Native Female,14=N - Two or more races Female]
  CAEEOETHN Integer CA Ethnicity [0=,1=A10 - Hispanic/Latino - Male,2=A20 - Hispanic/Latino - Female,3=A30 - Hispanic/Latino - Non-Binary,4=B10 - Non-Hispanic/Non-Latino - Male - White,5=B20 - Non-Hispanic/Non-Latino - Male - Black or African American,6=B30 - Non-Hispanic/Non-Latino - Male - Native Hawaiian or Other Pacific Islander,7=B40 - Non-Hispanic/Non-Latino - Male - Asian,8=B50 - Non-Hispanic/Non-Latino - Male - American Indian or Alaskan Native,9=B60 - Non-Hispanic/Non-Latino - Male - Two or more races,10=C10 - Non-Hispanic/Non-Latino - Female - White,11=C20 - Non-Hispanic/Non-Latino - Female - Black or African American,12=C30 - Non-Hispanic/Non-Latino - Female - Native Hawaiian or Other Pacific Islander,13=C40 - Non-Hispanic/Non-Latino - Female - Asian,14=C50 - Non-Hispanic/Non-Latino - Female - American Indian or Alaskan Native,15=C60 - Non-Hispanic/Non-Latino - Female - Two or more races,16=D10 - Non-Hispanic/Non-Latino - Non-Binary - White,17=D20 - Non-Hispanic/Non-Latino - Non-Binary - Black or African American,18=D30 - Non-Hispanic/Non-Latino - Non-Binary - Native Hawaiian or Other Pacific Islander,19=D40 - Non-Hispanic/Non-Latino - Non-Binary - Asian,20=D50 - Non-Hispanic/Non-Latino - Non-Binary - American Indian or Alaskan Native,21=D60 - Non-Hispanic/Non-Latino - Non-Binary - Two or more races]
  EMPLERDENT Integer RESERVED - Cdn Only [0=1 - No dental insurance or coverage of any kind,1=2 - Payee only,2=3 - Payee, spouse and dependent children,3=4 - Payee and their spouse,4=5 - Payee and their dependent children]
  PAYERDENT Integer RESERVED - Cdn Only [0=1 - No dental insurance or coverage of any kind,1=2 - Payee only,2=3 - Payee, spouse and dependent children,3=4 - Payee and their spouse,4=5 - Payee and their dependent children]
  WLCOUNTY String*30 Work Location County

## UPEMPO - Employee Optional Field Values (view UP0122)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+OPTFIELD; OPTFIELD+EMPLOYEE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPEMPT - Employee Taxes (view UP0010)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+TAXID; EMPLOYEE+CATEGORY+TAXTYPE+TAXID; TAXID+DISTCODE [D,M]
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  TAXID String*6 Tax Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXTRAWH BCD*10.3 Extra Withholding
  CALCMTHD Integer Withholding Method [1=Standard Calculation,2=Amount Override,3=Percent Override,4=Taxable, No Withholding,7=Calculation Base Only]
  OVERRATE BCD*9.5 Amount/Percent Override
  DISTCODE String*6 Distribution Code
  OCCASIONAL Boolean INTERNAL USE - Occasional Tax
  EFFECTDATE Date INTERNAL USE - Tax Table Effective Date
  EMPPARMVER Integer INTERNAL USE - Employee Tax Table Parameter Version
  EMPPARMCNT Integer INTERNAL USE - Employee Tax Table Parameter Count
  CATEGORY Integer INTERNAL USE - Category
  TAXTYPE Integer INTERNAL USE - Tax Type
  VALUES Long Number of Optional Fields

## UPEMRGD - EFT Files Combine Setup Detail (view UP0210)
Keys (first = PK; D=dups allowed, M=modifiable): MERGEEFT+COMPANYID
Fields (NAME type description [values]):
  MERGEEFT String*8 Combine EFT Key
  COMPANYID String*6 Company ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPDESC String*60 Company Name
  HOMECOMP Boolean Home Company

## UPEMRGH - EFT Files Combine Setup Header (view UP0209)
Keys (first = PK; D=dups allowed, M=modifiable): MERGEEFT
Fields (NAME type description [values]):
  MERGEEFT String*8 Combine EFT Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MERGENUM String*4 Last Combine File Number
  MERGEDATE Date Last Combine File Date
  MERGEPATH String*128 Last Combine File Path

## UPEMTF - Employee Tax Fields (view UP0062)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+TAXID+PARMUSE+PARMSEQ
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  TAXID String*6 Tax Code
  PARMUSE Integer Field Use Type
  PARMSEQ Integer Field Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PARMNBR Integer Tax Table Field Number
  PARMTYPE Integer Field Data Type
  PARMLEN Integer Field Length
  PARMDECS Integer Number of Decimal Places
  PARMVAL String*24 Value

## UPEMTO - Empl Taxes Optional Fields (view UP0126)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+TAXID+OPTFIELD; OPTFIELD+EMPLOYEE+TAXID
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  TAXID String*6 Tax Code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPEMULD - EFT Combine File Detail (view UP0207)
Keys (first = PK; D=dups allowed, M=modifiable): BANKID+COMBRUNSEQ+COMPANYID+EFTRUNSEQ+RERUNSEQ
Fields (NAME type description [values]):
  BANKID String*8 Bank ID
  COMBRUNSEQ Long Combine Run Sequence
  COMPANYID String*6 Company ID
  EFTRUNSEQ Long EFT Run Sequence
  RERUNSEQ Long EFT Rerun Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FILEDATE Date EFT File Date
  FILENAME String*32 EFT File Name
  FILENUMBER String*4 EFT File Number
  TOTCREDIT BCD*10.3 EFT File Total Credit

## UPEMULH - EFT Combine File Header (view UP0206)
Keys (first = PK; D=dups allowed, M=modifiable): BANKID+COMBRUNSEQ; BANKID+MULTINUM+COMBRUNSEQ
Fields (NAME type description [values]):
  BANKID String*8 Bank ID
  COMBRUNSEQ Long Combine Run Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MULTINUM String*4 Combine File Number
  MULTIDATE Date Combine File Date
  MULTINAME String*8 Combine File Name
  MULTIPATH String*128 Combine File Path
  EXTENSION String*3 Extension
  MULTIDESC String*60 Description

## UPEREG - EFT Run History Header (view UP0204)
Keys (first = PK; D=dups allowed, M=modifiable): EFTRUNSEQ+RERUNSEQ; LASTRERUN+EFTRUNSEQ+RERUNSEQ [M]
Fields (NAME type description [values]):
  EFTRUNSEQ Long EFT Run Sequence
  RERUNSEQ Long EFT Rerun Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LASTRERUN Boolean Last Rerun
  BANKID String*8 Company EFT Bank ID
  SELECTLIST String*8 Selection List
  EMPFROM String*12 From Employee
  EMPTO String*12 To Employee
  PEDATEFROM Date From Period End Date
  PEDATETO Date To Period End Date
  USEDEFDATE Boolean Use Default Funds Available Date
  DEFDATE Date Default Funds Available Date
  CREATDATE Date File Creation Date
  FILCREATNO String*4 File Creation Number
  FILIDMODIF String*1 File ID Modifier
  ENTRYDESC String*10 Entry Description
  USERLANG String*1 User Language
  BANKFORMAT Integer Bank Format
  ORIGNUM String*10 Originator #
  COMPABREV String*16 Company EFT Short Name
  COMPLNAME String*30 RESERVED - Cdn Only
  DATACENTER String*5 RESERVED - Cdn Only
  INSTIDRTN String*9 RESERVED - Cdn Only
  ACCTNORTN String*18 RESERVED - Cdn Only
  RESERVDORG String*15 RESERVED - Cdn Only
  ELEMENTID String*11 RESERVED - Cdn Only
  REGLECODE String*2 RESERVED - Cdn Only
  CPATRNCODE String*3 RESERVED - Cdn Only
  CODISCDATA String*20 Company Discretionary Data
  SERVCLASS String*3 Service Class Code
  ORIGSTATUS String*1 Originator Status Code
  ORIGDFIID String*9 Originator DFI ID
  ALTIMMDEST Boolean Use Alternative Imm. Dest. ID?
  IMMDESTID String*10 Immediate Destination ID
  IMMDESTNAM String*23 Immediate Destination Name
  ALTIMMORIG Boolean Use Alternative Imm. Origin #?
  IMMORIGNUM String*10 Immediate Origin #
  IMMORIGNAM String*23 Immediate Origin Name
  OFFRECTYPE String*1 Offset Record Type Code
  OFFTRNCODE String*2 Offset Transaction Code
  OFFRDFIID String*9 Offset Receiving DFI ID
  OFFRDFIACC String*17 Offset DFI Account #
  OFFINDVID String*15 Offset Individual ID #
  OFFINDVNAM String*22 Offset Individual Name
  OFFDISDATA String*2 Offset Discretionary Data
  APPENDCRLF Boolean Append CR/LF to Each Record?
  FILEHEADER String*250 Deposit File Header
  FILEFOOTER String*250 Deposit File Footer
  DPFILENAME String*8 Deposit File Name
  DPFILEEXT String*3 Deposit File Extension
  MERGEUSED Boolean Used in Merge File
  MERGENUM String*4 Merge File Number
  EFTTYPE Integer EFT Type
  CASESTATE String*2 Case State

## UPESLD - Employee Selection List Members (view UP0046)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLISTID+EMPLOYEE; EMPLOYEE+EMPLISTID
Fields (NAME type description [values]):
  EMPLISTID String*8 Employee List
  EMPLOYEE String*12 Employee
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## UPESLH - Employee Selection Lists (view UP0045)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLISTID
Fields (NAME type description [values]):
  EMPLISTID String*8 Employee List
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EMPLISTDSC String*60 Employee List Description
  LASTMAINT Date Date Last Edited

## UPETRN - EFT Run History Details (view UP0205)
Keys (first = PK; D=dups allowed, M=modifiable): EFTRUNSEQ+RERUNSEQ+EMPLOYEE+TRANSNO; EFTRUNSEQ+RERUNSEQ+ENTRYDATE+EMPLOYEE+TRANSNO; EFTRUNSEQ+RERUNSEQ+ENTRYDATE+EMPLOYEE+BKACCTCODE+TRANSNO
Fields (NAME type description [values]):
  EFTRUNSEQ Long EFT Run Sequence
  RERUNSEQ Long EFT Rerun Sequence
  EMPLOYEE String*12 Employee
  TRANSNO Long Unique Key Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LASTNAME String*20 Last Name
  FIRSTNAME String*15 First Name
  MIDDLENAME String*15 Middle Name
  TRNSFRNAME String*30 Bank Transfer Name
  REFERENCE String*19 Reference
  DISCREDATA String*2 Discretionary Data
  BKACCTCODE String*6 Employee EFT Bank ID
  BKACCTDESC String*15 Employee EFT Bank Description
  INSTITUTID String*9 Receiving DFI ID
  ACCTNUM String*18 Account Number
  TRANSCODE String*2 Transaction Code
  DEPOSITAMT BCD*10.3 Deposit Amount
  ENTRYDATE Date EFT Entry Effective Date
  CHECKNUM BCD*8.0 Check Number
  CASEID String*20 Case Identifier
  CASESTATE String*2 Case State
  JURISDICTN String*30 Case Jurisdiction
  FIPSCODE String*7 FIPS Code
  CUSTPARENT String*30 Custodial Parent
  MEDINSUAVL Boolean Family Health Insurance is Available?
  MEDINSUREQ Boolean Family Health Insurance is Required?
  ORDERDATE Date Date of Order
  CHECKDATE Date Check Date/Cheque Date
  SSN String*9 Non-Custodial Parent Social Security Number
  TERMINATED Boolean Employment Termination Indicator

## UPGLBM - Globally Modify List (view UP0051)
Keys (first = PK; D=dups allowed, M=modifiable): FIELDIDX+FIELDNAME; OPERATION+FIELDIDX [D,M]
Fields (NAME type description [values]):
  FIELDIDX Long Field Index
  FIELDNAME String*32 Field Name
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FIELDTYPE Integer Field Type [0=Undefined,1=String,2=Byte,3=Date,4=Time,5=IEEE Long Real,6=Amount,7=Integer,8=Long Integer,9=Boolean]
  FIELDLEN Integer Field Length
  FIELDSIZE Integer Field Size
  FIELDDECS Integer Field Decimals
  BCDTYPE Integer Type of BCD Field [0=N/A,1=Rate,2=Amount,3=Percent,4=Billing Rate]
  OPERATION Integer Operation [1=,2=Replace,3=Increase,4=Decrease,5=Pct Inc,6=Pct Dec,7=Replace,8=Increase,9=Decrease,10=Replace,11=Replace,12=Replace,13=Replace,14=Replace]
  TESTOLD Boolean Test Old Value
  OLDSTRING String*60 Old String Value
  NEWSTRING String*60 New String Value
  OLDDATE Date Old Date Value
  NEWDATE Date New Date Value
  OLDINT Integer Old Integer Value
  NEWINT Integer New Integer Value
  OLDAMTPCT BCD*9.5 Old Amount or Percent
  AMTPCTCHG BCD*9.5 Amount/Percent Change
  EMPTTYPE Integer Employee Tax Type [1=No EMPT Processing,2=Withholding Amount Override,3=Withholding Percent Override,4=Employee Tax Amount,5=Employee Tax Percent]
  ISTAX Boolean Is Tax?
  ID2CHANGE String*6 ID To Change
  ECALCMETH Integer Employee Calculation Method
  RCALCMETH Integer Employer Calculation Method
  OLDWCCGRUP String*6 Old WCC Group
  NEWWCCGRUP String*6 New WCC Group
  OLDBILLRAT BCD*10.6 Old Billing Rate
  NEWBILLRAT BCD*10.6 New Billing Rate

## UPGLDD - G/L Acct Desc Report List (view UP0060)
Keys (first = PK; D=dups allowed, M=modifiable): SELSEQ+ACCTID; SELSEQ+ACCTFMTTD [D]
Fields (NAME type description [values]):
  SELSEQ Long Selection Sequence
  ACCTID String*45 Unformatted Account
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCTFMTTD String*45 Account Number
  ACCTDESC String*60 Description

## UPGLREF - G/L Reference Integration (view UP0057)
Keys (first = PK; D=dups allowed, M=modifiable): SOURCE+GLDEST
Fields (NAME type description [values]):
  SOURCE Integer Source Transaction Type [0=System Checks,1=System Checks Detail,2=System Checks PJC Detail,3=Manual Checks,4=Manual Checks Detail,5=Manual Checks PJC Detail]
  GLDEST Integer G/L Transaction Field [0=G/L Entry Description,1=G/L Detail Reference,2=G/L Detail Description,3=G/L Detail Comment]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEPARATOR Integer Separator [0=* Asterisk,1=- Hyphen,2=/ Forward Slash,3=\ Back Slash,4=. Period,5={ Left Parenthesis,6=} Right Parenthesis,7=# Number Sign,8=Space]
  SEGMENT1 Integer Included Segment 1 [0=None,1=Posting Sequence,2=Calculation Sequence,3=Employee Number,4=Employee Name,5=Check Number,6=Check Date,7=Posting Date,8=Pay Period Start Date,9=Pay Period End Date,10=Bank Code,11=Pay Frequency,12=Class 1 Value,13=Class 2 Value,14=Class 3 Value,15=Class 4 Value]
  SEGMENT2 Integer Included Segment 2 [0=None,1=Posting Sequence,2=Calculation Sequence,3=Employee Number,4=Employee Name,5=Check Number,6=Check Date,7=Posting Date,8=Pay Period Start Date,9=Pay Period End Date,10=Bank Code,11=Pay Frequency,12=Class 1 Value,13=Class 2 Value,14=Class 3 Value,15=Class 4 Value]
  SEGMENT3 Integer Included Segment 3 [0=None,1=Posting Sequence,2=Calculation Sequence,3=Employee Number,4=Employee Name,5=Check Number,6=Check Date,7=Posting Date,8=Pay Period Start Date,9=Pay Period End Date,10=Bank Code,11=Pay Frequency,12=Class 1 Value,13=Class 2 Value,14=Class 3 Value,15=Class 4 Value]
  SEGMENT4 Integer Included Segment 4 [0=None,1=Posting Sequence,2=Calculation Sequence,3=Employee Number,4=Employee Name,5=Check Number,6=Check Date,7=Posting Date,8=Pay Period Start Date,9=Pay Period End Date,10=Bank Code,11=Pay Frequency,12=Class 1 Value,13=Class 2 Value,14=Class 3 Value,15=Class 4 Value]
  SEGMENT5 Integer Included Segment 5 [0=None,1=Posting Sequence,2=Calculation Sequence,3=Employee Number,4=Employee Name,5=Check Number,6=Check Date,7=Posting Date,8=Pay Period Start Date,9=Pay Period End Date,10=Bank Code,11=Pay Frequency,12=Class 1 Value,13=Class 2 Value,14=Class 3 Value,15=Class 4 Value]

## UPHDAU - History Audit Details (view UP0024)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+EDITDATE+EDITTIME+CATEGORY1+EARNDED1+LINETYPE1+LINENO
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  EDITDATE Date Edit Date
  EDITTIME Time Edit Time
  CATEGORY1 Integer Category code - new [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARNDED1 String*6 Earn/Ded/Tax - new
  LINETYPE1 Integer Transaction Type - new [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  HISTDATE Date History Date
  OPERATION Integer Operation [1=Add,2=Modify,3=Delete]
  EDTYPE1 Integer Earn/Ded/Tax Type - new [1=Salary & Wages,2=Reported Tips,3=Allocated Tips,7=Vacation,8=Sick,9=Compensatory Time,13=Cash,14=Noncash,18=Insurance Tax,19=Income Tax,20=Unemployment Tax,21=Pension Plan Tax,22=Health Tax,23=Other Tax,25=n/a]
  ECNTBASE1 BCD*10.3 Employee Count or Base - new
  ERATE1 BCD*9.5 Employee Rate - new
  EEXTEND1 BCD*10.3 Employee Amount - new
  RCNTBASE1 BCD*10.3 Employee Count or Base - new
  RRATE1 BCD*9.5 Employee Rate - new
  REXTEND1 BCD*10.3 Employee Amount - new
  WCC1 String*6 Workers' Compensation Code - new
  GLSEG1A String*15 G/L Segment One - new
  GLSEG2A String*15 G/L Segment Two - new
  GLSEG3A String*15 G/L Segment Three - new
  TAXWEEKS1 BCD*4.3 Weeks Worked for Tax Auth - new
  TAXEARNS1 BCD*10.3 Taxable Earnings - new
  TXEARNCL1 BCD*10.3 Taxable Earnings Ceiling - new
  TAXTIPS1 BCD*10.3 Taxable Tips Without Ceil - new
  TXTIPSCL1 BCD*10.3 Taxable Tips With a Ceil - new
  TXONTIPS1 BCD*10.3 Amount of Tax Calc on Tips - new
  UNCOLLTX1 BCD*10.3 For Uncollected SS/Med - new
  DESC1 String*15 Description - new
  HOURS1 BCD*4.3 Hours - new
  REGRATE1 BCD*9.5 Regular Rate - new
  CATEGORY2 Integer Category code - old [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARNDED2 String*6 Earn/Ded/Tax - old
  LINETYPE2 Integer Transaction Type - old [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  EDTYPE2 Integer Earn/Ded/Tax Type - old [1=Salary & Wages,2=Reported Tips,3=Allocated Tips,7=Vacation,8=Sick,9=Compensatory Time,13=Cash,14=Noncash,18=Insurance Tax,19=Income Tax,20=Unemployment Tax,21=Pension Plan Tax,22=Health Tax,23=Other Tax,25=n/a]
  ECNTBASE2 BCD*10.3 Employee Count or Base - old
  ERATE2 BCD*9.5 Employee Rate - old
  EEXTEND2 BCD*10.3 Employee Amount - old
  RCNTBASE2 BCD*10.3 Employee Count or Base - old
  RRATE2 BCD*9.5 Employee Rate - old
  REXTEND2 BCD*10.3 Employee Amount - old
  WCC2 String*6 Workers' Compensation Code - old
  GLSEG1B String*15 G/L Segment One - old
  GLSEG2B String*15 G/L Segment Two - old
  GLSEG3B String*15 G/L Segment Three - old
  TAXWEEKS2 BCD*4.3 Weeks Worked for Tax Auth - old
  TAXEARNS2 BCD*10.3 Taxable Earnings - old
  TXEARNCL2 BCD*10.3 Taxable Earnings Ceiling - old
  TAXTIPS2 BCD*10.3 Taxable Tips Without Ceil - old
  TXTIPSCL2 BCD*10.3 Taxable Tips With a Ceil - old
  TXONTIPS2 BCD*10.3 Amount of Tax Calc on Tips - old
  UNCOLLTX2 BCD*10.3 For Uncollected SS/Med - old
  DESC2 String*15 Description - old
  HOURS2 BCD*4.3 Hours - old
  REGRATE2 BCD*9.5 Regular Rate - old
  TAXNONPER1 BCD*10.3 Taxable Non-periodic Earn - new
  TAXNONPER2 BCD*10.3 Taxable Non-periodic Earn - old
  TAXEARNBD1 BCD*10.3 Subject to Inc tax bef ded - new
  TAXEARNBD2 BCD*10.3 Subject to Inc tax bef ded - old
  WCCGROUP1 String*6 Workers Comp. Group - new
  WCCGROUP2 String*6 Workers Comp. Group - old
  POOLEDTIP1 BCD*10.3 RESERVED - Cdn Only
  POOLEDTIP2 BCD*10.3 RESERVED - Cdn Only
  EARDEDDAT1 Date Earning/Deduction Date - new
  EARDEDDAT2 Date Earning/Deduction Date - old
  STARTTIME1 Integer Start Time - new
  STARTTIME2 Integer Start Time - old
  STOPTIME1 Integer Stop Time - new
  STOPTIME2 Integer Stop Time - old
  VALUES Long Number of Optional Fields
  ECALCMETH Integer Employee Calculation Method
  RCALCMETH Integer Employer Calculation Method
  WCBASE1 BCD*10.3 WC Base - new
  WCBASE2 BCD*10.3 WC Base - old
  WCRATE1 BCD*6.6 WC Rate - new
  WCRATE2 BCD*6.6 WC Rate - old
  WCEXTEND1 BCD*10.5 WC Assessment - new
  WCEXTEND2 BCD*10.5 WC Assessment - old
  GLSEG4A String*15 G/L Segment Four - new
  GLSEG5A String*15 G/L Segment Five - new
  GLSEG6A String*15 G/L Segment Six - new
  GLSEG4B String*15 G/L Segment Four - old
  GLSEG5B String*15 G/L Segment Five - old
  GLSEG6B String*15 G/L Segment Six - old

## UPHDOA - History Audit Detail Opt Fields (view UP0136)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+EDITDATE+EDITTIME+CATEGORY+EARNDED+LINETYPE+LINENO+OPTFIELD
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  EDITDATE Date Edit Date
  EDITTIME Time Edit Time
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARNDED String*6 Earn/Ded/Tax
  LINETYPE Integer Transaction Type [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  LINENO Integer Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation [1=Add,2=Modify,3=Delete]
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  FDESC String*60 Optional Field Description
  VALUE1 String*60 Value - new
  VDESC1 String*60 Value Description - new
  VALUE2 String*60 Value - old
  VDESC2 String*60 Value Description - old

## UPHHAU - History Audit Headers (view UP0021)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+EDITDATE+EDITTIME
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  EDITDATE Date Edit Date
  EDITTIME Time Edit Time
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  HISTDATE Date History Date
  OPERATION Integer Operation [1=Add,2=Modify,3=Delete]
  CLASS1A String*6 Class 1 - new
  CLASS2A String*6 Class 2 - new
  CLASS3A String*6 Class 3 - new
  CLASS4A String*6 Class 4 - new
  DESC1 String*250 Description - new
  NETPAY1 BCD*10.3 Net Pay - new
  CLASS1B String*6 Class 1 - old
  CLASS2B String*6 Class 2 - old
  CLASS3B String*6 Class 3 - old
  CLASS4B String*6 Class 4 - old
  DESC2 String*250 Description - old
  NETPAY2 BCD*10.3 Net Pay - old
  LASTNAME String*20 Last Name
  FIRSTNAME String*15 First Name
  MIDDLENAME String*15 Middle Name
  WORKPROV1 Integer Province of Employment - new [1=Alberta,2=British Columbia,3=Manitoba,4=New Brunswick,5=Newfoundland & Labrador,6=Northwest Territories,7=Nova Scotia,8=Ontario,9=Outside Canada,10=Prince Edward Island,11=Quebec,12=Saskatchewan,13=Yukon Territory,14=Nunavut]
  WORKPROV2 Integer Province of Employment - old [1=Alberta,2=British Columbia,3=Manitoba,4=New Brunswick,5=Newfoundland & Labrador,6=Northwest Territories,7=Nova Scotia,8=Ontario,9=Outside Canada,10=Prince Edward Island,11=Quebec,12=Saskatchewan,13=Yukon Territory,14=Nunavut]
  VALUES Long Number of Optional Fields
  ORGUSERID String*8 Original User ID

## UPHHOA - History Audit Header Opt Fields (view UP0135)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+EDITDATE+EDITTIME+OPTFIELD
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  EDITDATE Date Edit Date
  EDITTIME Time Edit Time
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation [1=Add,2=Modify,3=Delete]
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  FDESC String*60 Optional Field Description
  VALUE1 String*60 Value - new
  VDESC1 String*60 Value Description - new
  VALUE2 String*60 Value - old
  VDESC2 String*60 Value Description - old

## UPINCL - Include List (view UP0015)
Keys (first = PK; D=dups allowed, M=modifiable): OWNERID+OWNERTYPE+LISTTYPE+CATEGORY+INCLUDEID; INCLUDEID+OWNERTYPE+LISTTYPE+OWNERID
Fields (NAME type description [values]):
  OWNERID String*6 Owner ID
  OWNERTYPE Integer Owner Type [1=Earning/Deduction,2=Tax]
  LISTTYPE Integer List Type [1=Base Hours Include,2=Base Earnings Include,3=Base Deductions Include,4=Base Taxes Include]
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  INCLUDEID String*6 Include ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WHMETHOD Integer Withholding Method [1=Regular Rate,4=Taxable, No Withholding,6=Supplemental Withholding]

## UPLIMD - Deduction Group Details (view UP0117)
Keys (first = PK; D=dups allowed, M=modifiable): EDGROUP+ORDER; EARNDED [M]
Fields (NAME type description [values]):
  EDGROUP String*6 Deduction Group
  ORDER Long Order
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EARNDED String*6 Deduction

## UPLIMH - Deduction Groups (view UP0116)
Keys (first = PK; D=dups allowed, M=modifiable): EDGROUP
Fields (NAME type description [values]):
  EDGROUP String*6 Deduction Group
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LONGDESC String*60 Description
  INACTIVE Boolean Inactive
  ASOF Date Inactive As Of
  LASTMAINT Date Last Maintained
  EMPLISTID String*8 Selection List
  EANNMAX BCD*10.3 Employee Annual Maximum
  ELIFEMAX BCD*10.3 Employee Lifetime Maximum
  RANNMAX BCD*10.3 Employer Annual Maximum
  RLIFEMAX BCD*10.3 Employer Lifetime Maximum

## UPMCDO - MC Details Opt Field Values (view UP0130)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+LINENUM+OPTFIELD; OPTFIELD+EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+LINENUM
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  BANK String*8 Bank Code
  CHECKNUM BCD*8.0 Check Number
  PEREND Date Period End Date
  CHECKDATE Date Check Date
  LINENUM Integer Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPMCDT - Manual Check Detail (view UP0020)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+LINENUM; EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+EARNDED+LINENUM
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  BANK String*8 Bank ID
  CHECKNUM BCD*8.0 Check Number
  PEREND Date Period End Date
  CHECKDATE Date Check Date
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EARNDED String*6 Earning/Deduction
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARDEDTYPE Integer Type [1=Salary & Wages,2=Reported Tips,3=Allocated Tips,7=Vacation,8=Sick,9=Compensatory Time,13=Cash,14=Noncash,18=Insurance Tax,19=Income Tax,20=Unemployment Tax,21=Pension Plan Tax,22=Health Tax,23=Other Tax,25=n/a]
  LINETYPE Integer Transaction Type [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Diff.,6=n/a]
  EARDEDDATE Date Date
  GLSEG1 String*15 G/L Segment One
  GLSEG2 String*15 G/L Segment Two
  GLSEG3 String*15 G/L Segment Three
  HOURS BCD*4.3 Hours
  CALCMETH Integer Calculation Method
  LIMITBASE Integer Base Limit
  CNTBASE BCD*10.3 Pieces/Base
  RATE BCD*9.5 Rate/Amt/Percent
  EXTEND BCD*10.3 Extended Amt
  EXPACCT String*45 Regular Pay Expense G/L Account
  LIABACCT String*45 Liability G/L Account
  OTACCT String*45 Overtime Expense G/L Account
  SHIFTACCT String*45 Shift Diff. Expense G/L Account
  ASSETACCT String*45 Asset G/L Account
  WCC String*6 Workers' Compensation Code
  TAXWEEKS BCD*4.3 Weeks Worked
  TAXANNUAL BCD*5.5 Annualization Factor
  WEEKLYNTRY Boolean INTERNAL USE
  ENTRYTYPE Integer Entry Type
  CALCSS Integer Calculate Social Security tax
  CALCMED Integer Calculate Medicare tax
  POOLEDTIPS BCD*10.3 RESERVED - Cdn Only
  WCCGROUP String*6 Workers Comp. Group
  VALUES Long Number of Optional Fields
  DISTCODE String*6 Distribution Code
  REXPACCT String*45 Employer Expense G/L Account
  RLIABACCT String*45 Employer Liability G/L Account
  JOBS Long Jobs
  WORKCODE String*6 Work Classification Code
  JOBHOURS BCD*4.3 Total Job Hours
  JOBBASE BCD*10.3 Total Job Pieces/Sales/Amt
  RCALCMETH Integer Employer Calc. Method
  RLIMITBASE Integer Employer Base Limit
  RRATEOVER Boolean Override Employer Rate/Amt/Pct
  RRATE BCD*9.5 Employer Rate/Amt/Pct
  GLSEG4 String*15 RESERVED - G/L Segment Four
  GLSEG5 String*15 RESERVED - G/L Segment Five
  GLSEG6 String*15 RESERVED - G/L Segment Six

## UPMCHD - Manual Check Header (view UP0019)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE; EMPLOYEE+BANK+CHECKNUM [D]; EMPLOYEE+PEREND+CHECKNUM [D]
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  BANK String*8 Bank Code
  CHECKNUM BCD*8.0 Check Number
  PEREND Date Period End Date
  CHECKDATE Date Check Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CHECKDESC String*15 Description
  PERSTART Date Period Start Date
  TIMESLATE Integer Times Late
  ACTIVE Boolean Check Active
  PRINT Boolean Print Check
  BANKFORM String*6 Check Stock Code
  PROCESSED Integer Processed
  GROSSPAY BCD*10.3 Gross Pay
  CONTRIBS BCD*10.3 Benefits
  DEDUCTIONS BCD*10.3 Deductions
  TAXES BCD*10.3 Taxes
  NETPAY BCD*10.3 Net Pay
  VALUES Long Number of Optional Fields
  MCDLINES Integer Manual Check Lines
  SWJOB Boolean Job Related

## UPMCHO - Manual Check Optional Field Values (view UP0129)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+OPTFIELD; OPTFIELD+EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  BANK String*8 Bank Code
  CHECKNUM BCD*8.0 Check Number
  PEREND Date Period End Date
  CHECKDATE Date Check Date
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPMCJB - Manual Check Job Details (view UP0043)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+LINENUM+JOBLINE; EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+LINENUM+CONTRACT+PROJECT+CCATEGORY+JOBLINE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  BANK String*8 Bank ID
  CHECKNUM BCD*8.0 Check Number
  PEREND Date Period End Date
  CHECKDATE Date Check Date
  LINENUM Integer Line Number
  JOBLINE Integer Job Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CCATEGORY String*16 Category Code
  IDCUST String*12 Customer
  CURRCODE String*3 Billing Currency
  STARTTIME Integer Start Time
  STOPTIME Integer Stop Time
  HOURS BCD*4.3 Hours
  CNTBASE BCD*10.3 Pieces/Sales/Amt
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Item UOM
  WIPACCT String*45 Regular WIP/COS Acct
  OTWIPACCT String*45 Overtime WIP/COS Acct
  STWIPACCT String*45 Shift WIP/COS Acct
  VALUES Long Number of Optional Fields
  PROJSTYLE Integer Project Style [0=,1=Standard,2=Basic]
  PROJTYPE Integer Project Type [0=,1=Time and Materials,2=Fixed Price,3=Cost Plus]
  UFMTCONTNO String*16 Unformatted Contract Code
  REVREC Integer Accounting Method [0=,1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,7=Completed Contract,8=Accrual-Basis]
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  RESDESC String*60 Resource Description

## UPMCJO - Manual Check Jobs Opt Fields (view UP0142)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+LINENUM+JOBLINE+OPTFIELD; OPTFIELD+EMPLOYEE+BANK+CHECKNUM+PEREND+CHECKDATE+LINENUM+JOBLINE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  BANK String*8 Bank ID
  CHECKNUM BCD*8.0 Check Number
  PEREND Date Period End Date
  CHECKDATE Date Check Date
  LINENUM Integer Line Number
  JOBLINE Integer Job Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPOFD - Optional Field Values (view UP0121)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [1=Employees,2=Earnings/Deductions,3=Taxes,4=Employee Earnings/Deductions,5=Employee Taxes,6=Timecards,7=Timecard Earnings/Deductions,8=Timecard Taxes,16=Timecard PJC Details,9=Manual Checks,10=Manual Check Earnings/Deductions,11=Manual Check Taxes,17=Manual Check PJC Details,12=Transactions,13=Transaction Earnings/Deductions,14=Transaction Taxes,18=Transaction PJC Details,15=Payroll Processing]
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEFVAL String*60 Default Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  INITFLAG Integer Auto Insert [0=No,1=Yes]
  SWBANK Integer Bank [99=Not Applicable]
  SWSALARY Integer Salary and Wages Payable [99=Not Applicable]
  SWSUSPENSE Integer Suspense [99=Not Applicable]
  SWEXCHANGE Integer Exchange Rounding Difference [99=Not Applicable]
  SWREGEXP Integer Regular Expense [99=Not Applicable]
  SWOTEXP Integer Overtime Expense [99=Not Applicable]
  SWSHIFTEXP Integer Shift Expense [99=Not Applicable]
  SWADVANCE Integer Advances Receivable [99=Not Applicable]
  SWEELIAB Integer Employee Liability [99=Not Applicable]
  SWERLIAB Integer Employer Liability [99=Not Applicable]
  SWEREXP Integer Employer Expense [99=Not Applicable]
  SWLABOR Integer Labor [99=Not Applicable]
  SWOVERHEAD Integer Overhead [99=Not Applicable]
  SWCOSTTRX Integer PJC External Cost Transactions [99=Not Applicable]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]

## UPOFH - Optional Field Locations (view UP0120)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [1=Employees,2=Earnings/Deductions,3=Taxes,4=Employee Earnings/Deductions,5=Employee Taxes,6=Timecards,7=Timecard Earnings/Deductions,8=Timecard Taxes,16=Timecard PJC Details,9=Manual Checks,10=Manual Check Earnings/Deductions,11=Manual Check Taxes,17=Manual Check PJC Details,12=Transactions,13=Transaction Earnings/Deductions,14=Transaction Taxes,18=Transaction PJC Details,15=Payroll Processing]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

## UPOPTS - Company Options (view UP0023)
Keys (first = PK; D=dups allowed, M=modifiable): PROPTID
Fields (NAME type description [values]):
  PROPTID String*4 Option Record ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTRYCODE String*3 Payroll Country Code
  CONTACT String*60 Contact Person's Name
  PHONENBR String*30 Contact's Phone Number
  FAXNBR String*30 Contact's Fax Number
  PRTNONETSW Boolean Print Zero Net Checks
  MINWAGE BCD*10.3 Minimum Wage
  MAXPTHRS BCD*4.3 Maximum Annual Part-Time Hours
  YEARSHIST Integer Years of History to Keep
  EXCPTPCT BCD*5.5 Exception for Increase Percent
  EXCPTDLR BCD*10.3 Exception for Dollar Increase
  HRLYRTEDEC Integer Number of Decimal Places for Hourly Rates
  TCARDTIME Integer Timecard Fractional Hours [1=Minutes,2=Hundredths of an Hour]
  DAILYHRS BCD*4.3 Hours per Pay Frequency in Daily
  WEEKLYHRS BCD*4.3 Hours per Pay Frequency in Weekly
  BIWKLYHRS BCD*4.3 Hours per Pay Frequency in Biweekly
  SEMIMONHRS BCD*4.3 Hours per Pay Frequency in Semimonthly
  MONTHLYHRS BCD*4.3 Hours per Pay Frequency in Monthly
  QRTRLYHRS BCD*4.3 Hours per Pay Frequency in Quarterly
  PP10PYHRS BCD*4.3 Hours per Pay Frequency in 10 Periods
  PP13PYHRS BCD*4.3 Hours per Pay Frequency in 13 Periods
  PP22PYHRS BCD*4.3 Hours per Pay Frequency in 22 Periods
  DAILYPPPY Integer Daily Pay Periods per Year
  WEEKLYPPPY Integer Weekly Pay Periods per Year
  BIWKLYPPPY Integer Biweekly Pay Periods per Year
  GLONLINESW Integer Create G/L Trans or Not [1=During Posting,2=On Request Using Create G/L Batch Icon]
  APPENDGLSW Integer G/L Trans Append to Batch [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  GLBTCHTYPE Integer G/L Batch Type [1=Do Not Consolidate,2=Consolidate by Acct/Fiscal Period,3=Consolidate by Acct/Fiscal Period and Source Code]
  POSTDATCOD Integer Check or Period End Date [1=Use Check Date as Journal Entry Date,2=Use Pay Period End Date as Journal Entry Date]
  SALPAYACCT String*45 Salary and Wages Payable Account
  SUSPACCT String*45 Suspense Account
  COSTCTRSW Boolean Cost Center Switch
  GLSEG1 String*6 G/L Segment One
  GLSEG2 String*6 G/L Segment Two
  GLSEG3 String*6 G/L Segment Three
  GLSEGREPOP Integer Active Segment Replace Option [1=None,2=Expense Accounts,3=Expense and Liability Accounts]
  DEFBANK String*8 Default Bank
  DEFFORM String*6 Default MC Check Stock Code
  PRCURR String*3 Payroll Currency
  RATETYPE String*2 Rate Type
  EXDIFFACCT String*45 Exchange Rounding Difference Account
  ORGDTRVSE Boolean Use Original Dates When Reversing Checks
  PJCCOSTCTR Boolean PJC Cost Center Override
  PRINTSIN Boolean Print Masked SSN
  EMPLSEC Boolean Employee Level Security Flag
  TAXNUMBER String*20 Tax Number
  WCSTART Date WC Start Date
  GLSEG4 String*6 G/L Segment Four
  GLSEG5 String*6 G/L Segment Five
  GLSEG6 String*6 G/L Segment Six
  EEOESTNUM String*20 Establishment Number
  EEONAICS String*20 NAICS Code
  FLUPDAYS Integer Default Number of Days for Follow Up on Employee Comments
  CMNTDAYS Integer RESERVED - Default Number of Days for Expiry
  CMNTTYPE String*8 RESERVED - Default Comment Type
  SWCMNTTY Integer RESERVED - Allow Blank Comment Type

## UPOTSC - Overtime Schedules (view UP0022)
Keys (first = PK; D=dups allowed, M=modifiable): OTSCHED
Fields (NAME type description [values]):
  OTSCHED String*6 Overtime Schedule
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OTSDESC String*60 Description
  PAYOTAS Integer Pay Overtime As [2=Overtime Rate Pay,1=Compensatory Time Hours]
  COMPTOREG Boolean Pay Reg from Comp. Time Accrual
  OTSCINACT Boolean Inactive Flag
  OTSCINACTD Date Inactive Date
  LASTMAINT Date Last Maintained
  HRSOVER1 BCD*4.3 Hours Over One
  PERDAYS1 Integer Period One Days
  PREMIUMRT1 BCD*5.5 Rate Multiplier One
  HRSOVER2 BCD*4.3 Hours Over Two
  PERDAYS2 Integer Period Two Days
  PREMIUMRT2 BCD*5.5 Rate Multiplier Two
  HRSOVER3 BCD*4.3 Hours Over Three
  PERDAYS3 Integer Period Three Days
  PREMIUMRT3 BCD*5.5 Rate Multiplier Three
  HRSOVER4 BCD*4.3 Hours Over Four
  PERDAYS4 Integer Period Four Days
  PREMIUMRT4 BCD*5.5 Rate Multiplier Four
  HRSOVER5 BCD*4.3 Hours Over Five
  PERDAYS5 Integer Period Five Days
  PREMIUMRT5 BCD*5.5 Rate Multiplier Five
  HRSOVER6 BCD*4.3 Hours Over Six
  PERDAYS6 Integer Period Six Days
  PREMIUMRT6 BCD*5.5 Rate Multiplier Six
  BILLRATE1 BCD*10.6 Billing Rate One
  BILLRATE2 BCD*10.6 Billing Rate Two
  BILLRATE3 BCD*10.6 Billing Rate Three
  BILLRATE4 BCD*10.6 Billing Rate Four
  BILLRATE5 BCD*10.6 Billing Rate Five
  BILLRATE6 BCD*10.6 Billing Rate Six

## UPPCKD - Print Checks Detail Extension (view UP0080)
Keys (first = PK; D=dups allowed, M=modifiable): SORTCODE+CATEGORY+EARNDED+LINETYPE+LINENO; SORTCODE+PCATEGORY+PLINETYPE+EARNDED+LINETYPE+LINENO
Fields (NAME type description [values]):
  SORTCODE BCD*10.0 Sort Code
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax,11=EFT Entry]
  EARNDED String*6 Earning/Deduction/Tax Code
  LINETYPE Integer Line Type [1=Payment,2=Accrual,3=Regular,4=Overtime,5=Shift Differential,6=n/a,7=Normal Withholding,8=Backup Withholding,9=Supplemental Withholding]
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHORTDESC String*15 Short Desc
  HOURS BCD*4.3 Number of Hours
  ECNTBASE BCD*10.3 Base Amount
  RATEFMT Integer Rate Format
  RATE BCD*9.5 Hourly Rate/Percent/Amount
  CURRAMT BCD*10.3 Current Amount
  YTDAMT BCD*10.3 YTD Amount
  BALANCE BCD*10.3 Accrual Balance
  PCATEGORY Integer Printing Category [1=CHKD Earnings,2=CHKD Deductions,3=CHKD Taxes,4=CHKD Other,5=CHKD Benefits,6=CHKE EFT Entries]
  PLINETYPE Integer Printing Line type [11=CHKD Regular Line,11=CHKD Overtime Line,11=CHKD Shift Diff Line,14=CHKD Disbursed Tips,15=CHKD Vacation Payment,16=CHKD Sick Payment,17=CHKD Comp. Time Payment,21=CHKD Deduction Entry,31=CHKD Federal Income Entry,32=CHKD Federal Insurance Entry,33=CHKD Federal UI Entry,34=CHKD Federal Pension Entry,35=CHKD Federal Health Entry,36=CHKD Federal Other Entry,41=CHKD State Income Entry,42=CHKD State Insurance Entry,43=CHKD State UI Entry,44=CHKD State Pension Entry,45=CHKD State Health Entry,46=CHKD State Other Entry,51=CHKD Local Income Entry,52=CHKD Local Insurance Entry,53=CHKD Local UI Entry,54=CHKD Local Pension Entry,55=CHKD Local Health Entry,56=CHKD Local Other Entry,61=CHKD User Income Entry,62=CHKD User Insurance Entry,63=CHKD User UI Entry,64=CHKD User Pension Entry,65=CHKD User Health Entry,66=CHKD User Other Entry,71=CHKD Exp Reimbursement,72=CHKD Cash Advance,73=CHKD Reported Tips,74=CHKD Allocated Tips,75=CHKD Noncash Advance,76=CHKD Vac Accrual,77=CHKD Sick Accrual,78=CHKD Comp Accrual,81=CHKD Cash Benefit,82=CHKD Noncash Benefit,91=CHKE EFT Entry - Fixed Amount,92=CHKE EFT Entry - % of Gross Earnings,93=CHKE EFT Entry - % of Net Pay]
  POOLEDTIPS BCD*10.3 Pooled Tips
  DISTCODE String*6 Distribution Code
  DISTRNAME String*15 Distribution Description
  OYTDAMT BCD*10.3 Other YTD Amount - RESERVED

## UPPCKH - Print Checks Header Extension (view UP0079)
Keys (first = PK; D=dups allowed, M=modifiable): SORTCODE; EMPLOYEE [D,M]
Fields (NAME type description [values]):
  SORTCODE BCD*10.0 Sort Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LASTNAME String*20 Employee Last Name
  FIRSTNAME String*15 Employee First Name
  MIDDLENAME String*15 Employee Middle Name
  ADDRESS1 String*60 Employee Address 1
  ADDRESS2 String*60 Employee Address 2
  ADDRESS3 String*60 Employee Address 3
  ADDRESS4 String*60 Employee Address 4
  CITY String*30 City
  STATE String*30 State
  ZIP String*20 Zip/Postal Code
  COUNTRY String*30 Country
  SSN String*11 SSN/SIN
  GLSEG1 String*15 G/L Segment One
  GLSEG2 String*15 G/L Segment Two
  GLSEG3 String*15 G/L Segment Three
  GPAYCUR BCD*10.3 Current Gross Pay
  GPAYYTD BCD*10.3 YTD Gross Pay
  TOTEARNCUR BCD*10.3 Current Total Earnings
  TOTEARNYTD BCD*10.3 YTD Total Earnings
  TOTTAXCUR BCD*10.3 Current Total Taxes
  TOTTAXYTD BCD*10.3 YTD Total Taxes
  TOTDEDCUR BCD*10.3 Current Total Deductions
  TOTDEDYTD BCD*10.3 YTD Total Deductions
  TOTCBCUR BCD*10.3 Current Total Cash Benefits
  TOTCBYTD BCD*10.3 YTD Total Cash Benefits
  TOTNCCUR BCD*10.3 Current Total Non-cash Benefits
  TOTNCYTD BCD*10.3 YTD Total Non-cash Benefits
  TOTTBCUR BCD*10.3 Total Taxable Benefits
  TOTNTCUR BCD*10.3 Total Non-taxable Benefits
  FITYTD BCD*10.3 YTD Wages Subject to FIT
  NETPAYCUR BCD*10.3 Current Net Pay
  NETPAYYTD BCD*10.3 YTD Net Pay
  VACUSEDC BCD*10.3 Current Vacation Used
  VACUSEDY BCD*10.3 YTD Vacation Used
  VACLEFT BCD*10.3 Vacation Left
  SICKUSEDC BCD*10.3 Current Sick Used
  SICKUSEDY BCD*10.3 YTD Sick Used
  SICKLEFT BCD*10.3 Sick Left
  COMPUSEDC BCD*10.3 Current Comp. Used
  COMPUSEDY BCD*10.3 YTD Comp. Used
  COMPLEFT BCD*10.3 Comp. Left
  TOTHOURS BCD*10.3 Total Hours
  TOTREGHRS BCD*10.3 Total Regular Hours
  TOTOTHRS BCD*10.3 Total Overtime Hours
  COMPANYNAM String*60 Company Name
  CADDRESS1 String*60 Company Address 1
  CADDRESS2 String*60 Company Address 2
  CADDRESS3 String*60 Company Address 3
  CADDRESS4 String*60 Company Address 4
  CCITY String*30 Company City
  CSTATE String*30 Company State
  CPOSTALC String*20 Company Zip/Postal Code
  CCOUNTRY String*30 Company Country
  PERSTART Date Period Start Date
  PEREND Date Period End Date
  PRPERIOD Integer Period
  EMPLOYEE String*12 Employee
  GLSEG4 String*15 G/L Segment Four
  GLSEG5 String*15 G/L Segment Five
  GLSEG6 String*15 G/L Segment Six

## UPPMCO - Process Manual Check Optional Fields (view UP0138)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY+OPTFIELD; OPTFIELD+DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy Field
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPSHFB - Shift Differential Billing Detail (view UP0039)
Keys (first = PK; D=dups allowed, M=modifiable): SHIFTSCHED+SHIFTNUM+CURRCODE
Fields (NAME type description [values]):
  SHIFTSCHED String*6 Shift Differential Schedule
  SHIFTNUM Integer Shift Number
  CURRCODE String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BILLRATE BCD*10.6 Billing Rate

## UPSHFD - Shift Differential Detail (view UP0038)
Keys (first = PK; D=dups allowed, M=modifiable): SHIFTSCHED+SHIFTNUM
Fields (NAME type description [values]):
  SHIFTSCHED String*6 Shift Differential Schedule
  SHIFTNUM Integer Shift Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHIFTDIFF BCD*9.5 Rate per Hour
  BILLINGS Long Billing Rates

## UPSHFT - Shift Differential Schedule (view UP0025)
Keys (first = PK; D=dups allowed, M=modifiable): SHIFTSCHED
Fields (NAME type description [values]):
  SHIFTSCHED String*6 Shift Differential Schedule
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHFTSDESC String*60 Description
  SHFTINACT Boolean Schedule Inactive
  SHFTINACTD Date Inactive As Of
  LASTMAINT Date Last Maintained

## UPSTAT - Status (view UP0017)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LAST941YR Integer Last 941 Year
  LAST941QTR Integer Last 941 Quarter
  POSTSEQ Long Payroll Posting Sequence
  CALCSEQ Long Payroll Calculation Sequence
  LASTMMW2YR Integer Last Magnetic Media Year
  LASTPPW2YR Integer Last Printed Paper Year
  CALC941 Boolean Calculated 942 Flag
  EFTRUNSEQ Long EFT Run Sequence
  NEXTGLLNK BCD*10.0 Next G/L Drilldown Link
  DELRUNSEQ Long Delete Inactive Run Sequence
  AUDERUNSEQ Long Audit Earn/Deduct Run Sequence
  AUDTRUNSEQ Long Audit Tax/TD1 Claim Run Seq
  AUDARUNSEQ Long Audit Assign E/D Run Sequence
  EFTCOMBSEQ Long Next EFT Combine Run Sequence
  RL1START Long RL-1 Starting Number
  LCTXRUNSEQ Long Local Tax Audit Run Sequence
  AUDSRUNSEQ Long Audit Assign Tax Run Sequence
  LCTXEMRSEQ Long Local Tax Employee Audit Run Sequence

## UPTCDO - Timecard Details Optional Field Values (view UP0128)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+TIMECARD+LINENUM+OPTFIELD; OPTFIELD+EMPLOYEE+PEREND+TIMECARD+LINENUM
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  TIMECARD String*6 Timecard
  LINENUM Integer Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPTCDT - Timecard Detail (view UP0032)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+TIMECARD+LINENUM; EMPLOYEE+PEREND+TIMECARD+CATEGORY+EARNDED+LINENUM; EARNDED+EMPLOYEE+PEREND+TIMECARD+CATEGORY+LINENUM
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  TIMECARD String*6 Timecard
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax]
  EARNDED String*6 Earnings/Deduction
  EARDEDTYPE Integer Type [1=Salary & Wages,2=Reported Tips,3=Allocated Tips,7=Vacation,8=Sick,9=Compensatory Time,13=Cash,14=Noncash,18=Insurance Tax,19=Income Tax,20=Unemployment Tax,21=Pension Plan Tax,22=Health Tax,23=Other Tax,25=n/a]
  EARDEDDATE Date Date
  STARTTIME Integer Start Time
  STOPTIME Integer Stop Time
  GLSEG1 String*15 G/L Segment One
  GLSEG2 String*15 G/L Segment Two
  GLSEG3 String*15 G/L Segment Three
  HOURS BCD*4.3 Hours
  CALCMETH Integer Calculation Method [1=None,2=Flat,3=Fixed,4=Hourly Rate,5=Amount per Hour,6=Piece Rate Table,7=Percentage of Base,8=Sales Commission Table,9=Wage Bracket Table,10=Hours per Hour Worked,12=Hours per Frequency,13=Tax Bracket Table,14=Percentage of Another Tax]
  LIMITBASE Integer Base Limit
  CNTBASE BCD*10.3 Pieces/Sales/Base
  RATE BCD*9.5 E/D/Tax Rate/Amt/Percent
  PAYORACCR Integer Pay/Accrue Hours [1=Payment,2=Accrual,6=n/a]
  EXPACCT String*45 Regular Pay Expense G/L Account
  LIABACCT String*45 Liability G/L Account
  OTACCT String*45 Overtime Expense G/L Account
  SHIFTACCT String*45 Shift Differential G/L Account
  ASSETACCT String*45 Asset Account
  OTSCHED String*6 Overtime Schedule
  SHIFTSCHED String*6 Shift Differential Schedule
  SHIFTNUM Integer Shift Number
  WCC String*6 Workers Compensation Code
  TAXWEEKS BCD*4.3 Weeks Worked
  TAXANNLIZ BCD*5.5 Tax Annualization Factor
  WEEKLYNTRY Boolean INTERNAL USE
  ENTRYTYPE Integer Entry Type
  POOLEDTIPS BCD*10.3 RESERVED - Cdn Only
  DAYS Integer Days Worked
  WCCGROUP String*6 Workers Comp. Group
  VALUES Long Number of Optional Fields
  OTHOURS BCD*4.3 Overtime Hours Override
  OTRATE BCD*9.5 Overtime Rate Override
  SWFLSA Boolean Include in FLSA Overtime Calc
  DISTCODE String*6 Distribution Code
  REXPACCT String*45 Employer Expense G/L Account
  RLIABACCT String*45 Employer Liability G/L Account
  SWALLOCJOB Boolean Jobs Alloc Based on Calc Base
  JOBS Long Jobs
  WORKCODE String*6 Work Classification Code
  JOBHOURS BCD*4.3 Total Job Hours
  JOBBASE BCD*10.3 Total Job Pieces/Sales/Amt
  RCALCMETH Integer Employer Calc. Method
  RLIMITBASE Integer Employer Base Limit
  RRATEOVER Boolean Override Employer Rate/Amt/Pct
  RRATE BCD*9.5 Employer Rate/Amt/Pct
  GLSEG4 String*15 RESERVED - G/L Segment Four
  GLSEG5 String*15 RESERVED - G/L Segment Five
  GLSEG6 String*15 RESERVED - G/L Segment Six

## UPTCHD - Timecard Header (view UP0031)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+TIMECARD; TIMECARD+EMPLOYEE+PEREND
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  TIMECARD String*6 Timecard
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TCARDDESC String*15 Description
  TIMESLATE Integer Times late
  REUSECARD Boolean Reusable
  ACTIVE Boolean Active flag
  SEPARATECK Boolean Separate Check flag
  PROCESSED Boolean Processed Flag
  CREGHRS BCD*4.3 Regular Hours
  CSHIFTHRS BCD*4.3 Shift Hours
  CVACHRSP BCD*4.3 Vacation Hours Paid
  CVACHRSA BCD*4.3 Vacation Hours Accrued
  CSICKHRSP BCD*4.3 Sick Hours Paid
  CSICKHRSA BCD*4.3 Sick Hours Accrued
  CCOMPHRSP BCD*4.3 Compensatory Time Hours Paid
  CCOMPHRSA BCD*4.3 Comp. Time Hours Accrued
  CVACAMTP BCD*10.3 Vacation Dollars Paid
  CVACAMTA BCD*10.3 Vacation Dollars Accrued
  CSICKAMTP BCD*10.3 Sick Time Dollars Paid
  CSICKAMTA BCD*10.3 Sick Time Dollars Accrued
  CCOMPAMTP BCD*10.3 Comp. Time Dollars Paid
  CCOMPAMTA BCD*10.3 Comp. Time Dollars Accrued
  CDISIHRSP BCD*4.3 RESERVED - Cdn Only
  CDISIHRSA BCD*4.3 RESERVED - Cdn Only
  CDISIAMTP BCD*10.3 RESERVED - Cdn Only
  CDISIAMTA BCD*10.3 RESERVED - Cdn Only
  VALUES Long Number of Optional Fields
  OTOVERRIDE Boolean Overtime Override
  COTHOURS BCD*4.3 Overtime Hours
  TCDLINES Integer Timecard Lines
  SWJOB Boolean Job Related
  SRCEAPPL String*2 Source Application

## UPTCHO - Timecard Optional Field Values (view UP0127)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+TIMECARD+OPTFIELD; OPTFIELD+EMPLOYEE+PEREND+TIMECARD
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  TIMECARD String*6 Timecard
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPTCJB - Timecard Job Details (view UP0042)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+TIMECARD+LINENUM+JOBLINE; EMPLOYEE+PEREND+TIMECARD+LINENUM+CONTRACT+PROJECT+CCATEGORY+IDCUST+JOBLINE; EMPLOYEE+PEREND+TIMECARD+LINENUM+STARTTIME+JOBLINE [M]
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  TIMECARD String*6 Timecard
  LINENUM Integer Timecard Line Number
  JOBLINE Integer Job Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CCATEGORY String*16 Category Code
  IDCUST String*12 Customer
  CURRCODE String*3 Billing Currency
  STARTTIME Integer Start Time
  STOPTIME Integer Stop Time
  HOURS BCD*4.3 Hours
  CNTBASE BCD*10.3 Pieces/Sales/Amt
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Item UOM
  WIPACCT String*45 Regular WIP/COS Acct
  OTWIPACCT String*45 Overtime WIP/COS Acct
  STWIPACCT String*45 Shift WIP/COS Acct
  OTHOURS BCD*4.3 Overtime Hours Override
  OTBILLRATE BCD*10.6 Overtime Billing Rate Override
  VALUES Long Number of Optional Fields
  PROJSTYLE Integer Project Style [0=,1=Standard,2=Basic]
  PROJTYPE Integer Project Type [0=,1=Time and Materials,2=Fixed Price,3=Cost Plus]
  UFMTCONTNO String*16 Unformatted Contract Code
  REVREC Integer Accounting Method [0=,1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,7=Completed Contract,8=Accrual-Basis]
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  RESDESC String*60 Resource Description

## UPTCJO - Timecard Jobs Optional Field Values (view UP0141)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+PEREND+TIMECARD+LINENUM+JOBLINE+OPTFIELD; OPTFIELD+EMPLOYEE+PEREND+TIMECARD+LINENUM+JOBLINE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  PEREND Date Period End Date
  TIMECARD String*6 Timecard
  LINENUM Integer Timecard Line Number
  JOBLINE Integer Job Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPTXMO - Taxes Optional Field Values (view UP0124)
Keys (first = PK; D=dups allowed, M=modifiable): TAXID+OPTFIELD; OPTFIELD+TAXID
Fields (NAME type description [values]):
  TAXID String*6 Tax
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPTXMS - Company Payroll Taxes (view UP0029)
Keys (first = PK; D=dups allowed, M=modifiable): TAXID; CATEGORY+TAXTYPE+TAXID [M]
Fields (NAME type description [values]):
  TAXID String*6 Tax
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CATEGORY Integer Category
  TAXTYPE Integer Type [19=Income Tax,20=Unemployment Tax,18=Insurance Tax,21=Pension Plan Tax,22=Health Tax,23=Other Tax]
  LONGDESC String*60 Description
  SHORTDESC String*15 Short Description
  REPORTID String*20 Reporting ID
  ACTIVESW Boolean Tax Inactive
  INACTASOF Date Inactive Date
  LASTMAINT Date Last Maintained
  BASEMULT BCD*5.5 Base Multiplier
  SURTAXMULT BCD*5.5 Surtax Multiplier
  ROUNDTAXSW Boolean Round Tax
  DAILYPPY Integer Daily Pay Periods per Year
  TAXCREDITS Boolean RESERVED - Tax Credits
  TAXCRPCNT BCD*5.5 RESERVED - Tax Credit Percent
  STDARDDED1 BCD*10.3 Standard Deduction
  STDARDDED2 BCD*10.3 RESERVED - Standard Deduction
  STDARDDED3 BCD*10.3 RESERVED - Standard Deduction
  STDARDDED4 BCD*10.3 RESERVED - Standard Deduction
  EXMPTNAMT1 BCD*10.3 Amount per Exemption
  EXMPTNAMT2 BCD*10.3 RESERVED - Amount per Exemption
  EXMPTNAMT3 BCD*10.3 RESERVED - Amount per Exemption
  EXMPTNAMT4 BCD*10.3 RESERVED - Amount per Exemption
  EXMPTCRSW Boolean Tax Credit Exemption switch
  ANNMAXHRS BCD*4.3 Annual Maximum Hours
  ANNMAXERN BCD*10.3 Annual Maximum Earnings
  ANNUALMIN BCD*10.3 Annual Minimum Earnings
  W2BOXTYP Integer W-2 Box Type [1=Not Applicable,2=Other Information Box,3=Combine with Another Tax,4=Local Tax Box,5=Suppress W2 Reporting]
  W2WITHTAX String*6 Combine with Tax
  ASSOCW2SW Boolean Associate with W-2 printing
  ASSOCTAX String*6 Associated Tax
  ECALCMTHD Integer Employee Calculation Method [1=None,2=Flat,5=Amount per Hour,7=Percentage of Base,13=Tax Bracket Table,14=Percentage of Another Tax]
  ESUPPRATE BCD*5.5 Employee Supplemental Rate
  EBASETAX String*6 Employee Base Tax
  EAMTORPCT BCD*9.5 Employee Amount/Percent
  ELIMITON Integer Employee Limit [1=No Limit,4=Withholding,5=Base]
  EANNUALMAX BCD*10.3 Employee Annual Maximum
  ECLCMINWRK Boolean Employee Minimum Weeks Worked
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
  RCALCMTHD Integer Employer Calculation Method [1=None,2=Flat,5=Amount per Hour,7=Percentage of Base,13=Tax Bracket Table,15=Percentage of Employee Withholding]
  RBASETAX String*6 Employer Base Tax
  RAMTORPCT BCD*9.5 Employer Amount/Percent
  RLIMITON Integer Employer Limit [1=No Limit,4=Withholding,5=Base]
  RANNUALMAX BCD*10.3 Employer Annual Maximum
  RCLCMINWRK Boolean Employer Minimum Weeks Worked
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
  LEVEL Integer Level
  LISTUSEBHI Integer List Usage for Base Hours Include
  LISTUSEBEI Integer List Usage for Base Earnings Include
  WHMETHBEI Integer Withholding Method for Base Earnings Include [1=Regular Rate,4=Taxable, No Withholding,6=Supplemental Withholding]
  LISTUSEBDI Integer List Usage for Base Deductions Include
  EFFECTDATE Date INTERNAL USE - Tax Table Effective Date
  FIPSNBR Integer INTERNAL USE - Tax Table FIPS Number
  FIPSCODE String*2 INTERNAL USE - Tax Table FIPS Code
  CFGPARMVER Integer INTERNAL USE - Tax Table Parameter Version
  CFGPARMCNT Integer INTERNAL USE - Tax Table Parameter Count
  VALUES Long Number of Optional Fields
  AUTOUPDATE Boolean Automatically Update Local Tax
  LOCSTATE String*30 State
  LOCTAXCODE String*10 Local Tax Code
  ATXTYPE Integer RESERVED - Aatrix Tax Type
  EMPDEFAULT Boolean Automatically Populate Employee
  EMPDEFDIST String*6 Default Distribution Code

## UPUSLD - UPUSLD
Keys (first = PK; D=dups allowed, M=modifiable): USERID+EMPLISTID; EMPLISTID+MAIN+USERID [M]; EMPLISTID+USERID+MAIN [M]
Fields (NAME type description [values]):
  USERID String*8
  EMPLISTID String*8
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MAIN Boolean

## UPUSLH - UPUSLH
Keys (first = PK; D=dups allowed, M=modifiable): USERID; MAINLISTID+USERID [M]
Fields (NAME type description [values]):
  USERID String*8
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCESSTYPE Integer
  VIEWESL Boolean
  MAINLISTID String*8
  TCEMPLOYEE String*12

## UPUTCD - Employee Timecard Detail (view UP0103)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+ENDDATE+PAYDATE+EARNDED+UNIQUE; EMPLOYEE+ENDDATE+EARNDED+UNIQUE+PAYDATE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  ENDDATE Date End Date
  PAYDATE Date Pay Date
  EARNDED String*6 Earning/Exp/Tip/Accrual Code
  UNIQUE Integer Unique Key Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CATEGORY Integer Category [0=Hours,1=Tips,2=Expense,3=Piece Rate,4=Sales Commissions,5=Sick Accrual Payment,6=Vacation Accrual Payment]
  STARTTIME Integer Start Time
  STOPTIME Integer Stop Time
  HOURS BCD*4.3 Hours Worked
  TIPSEXP BCD*9.5 Tips/Expense/Pieces/Sales Amount
  SHIFTSCHED String*6 Shift Differential Schedule
  SHIFTNUM Integer Shift Number
  VALUES Long Number of Optional Fields
  POOLEDTIPS BCD*10.3 RESERVED - Cdn Only
  TIPSBASE BCD*10.3 RESERVED - Cdn Only
  JOBS Long Jobs
  WORKCODE String*6 Work Classification Code
  JOBHOURS BCD*4.3 Total Job Hours
  JOBBASE BCD*10.3 Total Job Pieces/Sales/Amt

## UPUTCH - Employee Timecard Header (view UP0102)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+ENDDATE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  ENDDATE Date End Date
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TCARDDESC String*15 Description
  STATUS Integer Status [0=New,1=Ready for Approval,3=Reviewed,2=Approved]
  VALUES Long Number of Optional Fields
  UNIQUE Integer Unique Key Field
  SWJOB Boolean Job Related

## UPUTDO - Empl Timecard Details Opt Flds (view UP0132)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+ENDDATE+PAYDATE+EARNDED+UNIQUE+OPTFIELD; OPTFIELD+EMPLOYEE+ENDDATE+PAYDATE+EARNDED+UNIQUE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  ENDDATE Date End Date
  PAYDATE Date Pay Date
  EARNDED String*6 Earnings/Tips Code
  UNIQUE Integer Unique Key Field
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPUTHO - Empl Timecard Optional Fields (view UP0131)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+ENDDATE+OPTFIELD; OPTFIELD+EMPLOYEE+ENDDATE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  ENDDATE Date End Date
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPUTJB - Employee Timecard Job Details (view UP0044)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+ENDDATE+PAYDATE+EARNDED+UNIQUE+JOBLINE; EMPLOYEE+ENDDATE+PAYDATE+EARNDED+UNIQUE+CONTRACT+PROJECT+CCATEGORY+IDCUST+JOBLINE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  ENDDATE Date End Date
  PAYDATE Date Pay Date
  EARNDED String*6 Earning/Expense/Tip Code
  UNIQUE Integer Unique Key Field
  JOBLINE Integer Job Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CCATEGORY String*16 Category Code
  IDCUST String*12 Customer
  CURRCODE String*3 Billing Currency
  STARTTIME Integer Start Time
  STOPTIME Integer Stop Time
  HOURS BCD*4.3 Hours
  CNTBASE BCD*10.3 Pieces/Sales/Amt
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Item UOM
  WIPACCT String*45 Regular WIP/COS Acct
  OTWIPACCT String*45 Overtime WIP/COS Acct
  STWIPACCT String*45 Shift WIP/COS Acct
  VALUES Long Number of Optional Fields
  PROJSTYLE Integer Project Style [0=,1=Standard,2=Basic]
  PROJTYPE Integer Project Type [0=,1=Time and Materials,2=Fixed Price,3=Cost Plus]
  UFMTCONTNO String*16 Unformatted Contract Code
  REVREC Integer Accounting Method [0=,1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,7=Completed Contract,8=Accrual-Basis]
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  RESDESC String*60 Resource Description

## UPUTJO - Employee TC Jobs Opt Field Values (view UP0143)
Keys (first = PK; D=dups allowed, M=modifiable): EMPLOYEE+ENDDATE+PAYDATE+EARNDED+UNIQUE+JOBLINE+OPTFIELD; OPTFIELD+EMPLOYEE+ENDDATE+PAYDATE+EARNDED+UNIQUE+JOBLINE
Fields (NAME type description [values]):
  EMPLOYEE String*12 Employee
  ENDDATE Date End Date
  PAYDATE Date Pay Date
  EARNDED String*6 Earning/Expense/Tip Code
  UNIQUE Integer Unique Key Field
  JOBLINE Integer Job Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## UPWCCD - Workers Compensation Codes (view UP0037)
Keys (first = PK; D=dups allowed, M=modifiable): WCCGROUP+WCC
Fields (NAME type description [values]):
  WCCGROUP String*6 Workers Comp. Group
  WCC String*6 Workers Compensation Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  RATE BCD*6.6 Rate
  PRATE BCD*6.6 Previous Rate

## UPWCCH - Workers Compensation Master (view UP0036)
Keys (first = PK; D=dups allowed, M=modifiable): WCCGROUP
Fields (NAME type description [values]):
  WCCGROUP String*6 Workers Comp. Group
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POLICYNO String*60 Policy Number
  POLICYDESC String*60 Description
  CEILING BCD*10.3 Ceiling
  LIABACCT String*45 Liability Account
  EXPACCT String*45 Expense Account
  STARTDATE Date Start Date
  CALCMETHOD Integer Calculation Method [1=Rate per 100 Dollars,2=Rate per Hour Worked]
  GENERATEGL Boolean RESERVED - Generate Entry to GL
  ADJOTTOREG Boolean Adjust Overtime to Reg Rate
  LASTMAINT Date Last Maintained
  PROV Integer RESERVED - Canada Only
  PCEILING BCD*10.3 Previous Ceiling
  PSTARTDATE Date Previous Start Date

## UPWRKC - Work Classification Codes (view UP0027)
Keys (first = PK; D=dups allowed, M=modifiable): WORKCODE
Fields (NAME type description [values]):
  WORKCODE String*6 Work Classification Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WORKDESC String*60 Description
  LASTMAINT Date Last Maintained
  COMMENTS String*250 Comments

## UPXCPT - Calc PR Exceptions (view UP0064)
Keys (first = PK; D=dups allowed, M=modifiable): CALCSEQ+EMPLOYEE+UNIQUE
Fields (NAME type description [values]):
  CALCSEQ Long Calculation sequence
  EMPLOYEE String*12 Employee
  UNIQUE Integer Unique Key Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EARNDED String*6 Earning/Deduction
  COMMENT String*70 Exception comment
  ORGUSERID String*8 Original User ID

## UPYTDS - Employee YTD Summaries (view UP0047)
Keys (first = PK; D=dups allowed, M=modifiable): YEARYTDS+EMPLOYEE+EARNDED+EARDEDCLAS; YEARYTDS+EMPLOYEE+CATEGORY+EARNDED+EARDEDCLAS [D]; EMPLOYEE+YEARYTDS+EARNDED+EARDEDCLAS [D]; EARNDED [D]
Fields (NAME type description [values]):
  YEARYTDS Integer Year
  EMPLOYEE String*12 Employee
  EARNDED String*6 Earning/Deduction
  EARDEDCLAS Integer Earning/Deduction Class [1=YTD Amount,2=Employer Contribution,3=Wages Subject To,4=Wages Subject To, Ceiling,5=Not Withheld,6=Tips Subject To,7=Tips Subject To, Ceiling,8=Tax On Tips,9=Base Hours,10=Base Count,11=Base Amount,12=Base Sales,16=Weeks Worked,17=Hours Worked,18=Backup Withholding,13=Accrued Dollars,14=Accrued Hours,15=Accrued Hours Paid,19=Taxable Non-periodic Earnings,20=Subject to Income tax before deductions,21=WC Base,22=Non-Periodic Deduction Before Tax,23=Repayment deductions before Income Tax]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CATEGORY Integer Category [1=Accrual,2=Earning,3=Advance,4=Deduction,5=Expense Reimbursement,6=Benefit,7=Federal Tax,8=State Tax,9=Local Tax,10=User Tax,11=n/a]
  EARDEDTYPE Integer Earning/Deduction Type [1=Salary & Wages,2=Reported Tips,3=Allocated Tips,7=Vacation,8=Sick,9=Compensatory Time,13=Cash,14=Noncash,18=Insurance Tax,19=Income Tax,20=Unemployment Tax,21=Pension Plan Tax,22=Health Tax,23=Other Tax,25=n/a]
  UNPSTEDAMT BCD*10.3 Sum of All Unposted Amounts
  POSTEDAMT BCD*10.3 Sum of All YTD Posted Amounts
