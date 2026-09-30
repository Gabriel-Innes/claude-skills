# PM module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## PMACCT - Account Sets (view PM0017)
Keys (first = PK; D=dups allowed, M=modifiable): IDACCTSET
Fields (NAME type description [values]):
  IDACCTSET String*6 Account Set Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  DATEINACTV Date Date Inactive
  WIPACCT String*45 Work in Progress
  COSTACCT String*45 Cost of Sales
  BILLACCT String*45 Billings
  DEFRACCT String*45 Deferred Revenue
  REVACCT String*45 Revenue
  PAYACCT String*45 Payroll Expense
  OHACCT String*45 Overhead
  LABACCT String*45 Labor
  EQUIPACCT String*45 Equipment
  EXPACCT String*45 Employee Expense
  PROACCT String*45 Profit
  LOSSACCT String*45 Loss
  CURNCODE String*3 Currency Code
  CEACCT String*45 Cost

## PMADJD - Adjustments Detail (view PM0063)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; ADJUSTNO+LINENO [D,M]; SEQ+DETAILNUM [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ADJUSTNO String*16 Adjustment Number
  ADJTYPE Integer Adjustment Type [0=Transfer,1=Adjustment]
  FMTCONTNO String*16 Original ^1
  CONTRACT String*16 Original ^1
  PROJECT String*16 Original ^2
  CATEGORY String*16 Original ^3
  RESOURCE String*24 Original Resource
  ITEMNO String*24 From Unformatted Item Number
  COSTREV Integer Cost or Revenue [0=None,1=Cost,2=Revenue,3=Both]
  COSTNUM Long Cost No.
  REVNUM Long Revenue No.
  DOCNUM String*24 Document No.
  OBILLTYPE Integer Original Billing Type [2=Billable,3=No Charge,1=Non-billable]
  OARITEM String*16 Original A/R Item Number
  OARUOM String*10 Original A/R Unit of Measure
  OICUOM String*10 Original ^7
  OQUANTITY BCD*10.5 Original Quantity
  OUNITCOST BCD*10.6 Original Unit Cost
  OBILLRATE BCD*10.6 Original Billing Rate
  OEXTCOSTHM BCD*10.3 Original Extended Cost
  OEXTCOSTSR BCD*10.3 Original Extended Cost
  OEXTBILLSR BCD*10.3 Original Extended Billing Amount
  OLABOR Integer Original Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  OLABORRATE BCD*10.6 Original Labor Rate
  OLABORPER BCD*5.5 Original Labor Percentage
  OLABORAMT BCD*10.3 Original Labor Amount
  OOVERHD Integer Original Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OOHEADRATE BCD*10.6 Original Overhead Rate
  OHEADPER BCD*5.5 Original Overhead Percentage
  OOHAMT BCD*10.3 Original Overhead Amount
  OTOTAMTHM BCD*10.3 Original Total Amount
  OBILLCCY String*3 Original Billing Currency
  OCONTSTYLE Integer Original ^2 Style [1=Standard,2=Basic]
  OPROJTYPE Integer Original ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  OCUSTOMER String*12 Original Customer No.
  OREVREC Integer Original Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  OINVTYPE Integer Original Invoice Type [1=Item,2=Summary]
  OWIPACCT String*45 From WIP Account
  OTRANACCT String*45 From Transaction Account
  OREVACCT String*45 From Revenue Account
  OOHACCT String*45 From Overhead Account
  OLABACCT String*45 From Labor Account
  OCVACCT String*45 From Cost Variance Account
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  VENDORID String*12 Vendor
  MODULE String*2 Module
  DOCTYPE Integer Document Type [0=,7=Material Usage,8=Material Return,9=Equipment Usage,10=Timecard,11=Charges,24=Cost]
  TRANSTYPE Integer Transaction Type [1=Posted,2=Discount,3=Write-off,4=Apply From,5=Apply To,6=Payment/Receipt Reversal,7=Rounding (multicurrency),8=Exchange Gain/Loss,9=Unrealized Exchange Gain/Loss,10=Adjustment,11=Receipt/Payment]
  COSTCCY String*3 Cost Currency
  USERID String*8 User ID
  DETAILNUM Long Detail Number
  TIMETYPE Integer Time Type [1=N/A,2=Time,3=Expense]
  DWIPACCT String*45 To WIP Account
  DTRANACCT String*45 To Transaction Account
  DREVACCT String*45 To Revenue Account
  DOHACCT String*45 To Overhead Account
  DLABACCT String*45 To Labor Account
  DCVACCT String*45 To Cost Variance Account
  DFMTCONTNO String*16 Revised ^1
  DCONTRACT String*16 Revised ^1
  DPROJECT String*16 Revised ^2
  DCATEGORY String*16 Revised ^3
  DCOSTTYPE Integer Cost Type [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  DRESOURCE String*24 Revised Resource
  DITEMNO String*24 To Unformatted Item Number
  DICBTYPE Integer I/C Bucket Type [0=]
  DICDOCNUM String*22 I/C Document Number
  DICCMETHOD Integer I/C Costing Method [0=NA,1=Moving Average,2=FIFO,3=LIFO,4=Standard Cost,5=Most Recent Cost,6=User-Specified]
  DICDATE Date I/C Transaction Date
  DICLOCAT String*6 I/C Location
  DBILLTYPE Integer Revised Billing Type [2=Billable,3=No Charge,1=Non-billable]
  DARITEM String*16 Revised A/R Item Number
  DARUOM String*10 Revised A/R Unit of Measure
  DICUOM String*10 Revised ^7
  DQUANTITY BCD*10.5 Revised Quantity
  DUNITCOST BCD*10.6 Revised Unit Cost
  DBILLRATE BCD*10.6 Revised Billing Rate
  DEXTCOSTHM BCD*10.3 Revised Extended Cost
  DEXTCOSTSR BCD*10.3 Revised Extended Cost
  DEXTBILLSR BCD*10.3 Revised Extended Billing Amount
  DLABOR Integer Revised Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  DLABORRATE BCD*10.6 Revised Labor Rate
  DLABORPER BCD*5.5 Revised Labor Percentage
  DLABORAMT BCD*10.3 Revised Labor Amount
  DOHAMT BCD*10.3 Revised Overhead Amount
  DOVERHD Integer Revised Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  DOHEADRATE BCD*10.6 Revised Overhead Rate
  DHEADPER BCD*5.5 Revised Overhead Percentage
  DTOTAMTHM BCD*10.3 Revised Total Amount
  DBILLCCY String*3 Revised Billing Currency
  DCONTSTYLE Integer Revised ^2 Style [1=Standard,2=Basic]
  DPROJTYPE Integer Revised ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  DCUSTOMER String*12 Revised Customer No.
  DREVREC Integer Revised Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  DINVTYPE Integer Revised Invoice Type [1=Item,2=Summary]
  MANITEM String*24
  VALUES Long Optional Fields
  OEARNINGS String*16 Original Earnings Code
  DEARNINGS String*16 Revised Earnings Code
  OPAYTYPE Integer Original Pay Type [3=None,1=US Payroll,2=Canadian Payroll]
  DPAYTYPE Integer Revised Pay Type [3=None,1=US Payroll,2=Canadian Payroll]
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment
  CLOSESN Boolean Close SN
  PROID Long SN inter-communication ID
  POPUPSN Integer Popup SN
  POPUPLT Integer Popup LT
  CLOSELT Boolean Close LT
  LTSETID Long LT inter-communication ID
  FORCEPOPSN Boolean Force popup SN
  FORCEPOPLT Boolean Force popup LT
  GENICSEQ Boolean Generate IC Seq.
  OSTAFFCODE String*24 Original Employee No.
  DSTAFFCODE String*24 Revised Employee No.

## PMADJDA - Adjustments Audit Detail (view PM0065)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ADJUSTNO String*16 Adjustment Number
  ADJTYPE Integer Adjustment Type
  SEQ Long Sequence
  FMTCONTNO String*16 Original ^1
  CONTRACT String*16 Original ^1
  PROJECT String*16 Original ^2
  CATEGORY String*16 Original ^3
  RESOURCE String*24 Original Resource
  ITEMNO String*24 From Unformatted Item Number
  COSTREV Integer Cost or Revenue
  COSTNUM Long Cost No.
  REVNUM Long Revenue No.
  DOCNUM String*24 Document No.
  OBILLTYPE Integer Original Billing Type
  OARITEM String*16 Original A/R Item Number
  OARUOM String*10 Original A/R Unit of Measure
  OICUOM String*10 Original ^7
  OQUANTITY BCD*10.5 Original Quantity
  OUNITCOST BCD*10.6 Original Unit Cost
  OBILLRATE BCD*10.6 Original Billing Rate
  OEXTCOSTHM BCD*10.3 Original Extended Cost
  OEXTCOSTSR BCD*10.3 Original Extended Cost
  OEXTBILLSR BCD*10.3 Original Extended Billing Amount
  OLABOR Integer Original Labor Type
  OLABORRATE BCD*10.6 Original Labor Rate
  OLABORPER BCD*5.5 Original Labor Percentage
  OLABORAMT BCD*10.3 Original Labor Amount
  OOVERHD Integer Original Overhead Type
  OOHEADRATE BCD*10.6 Original Overhead Rate
  OHEADPER BCD*5.5 Original Overhead Percentage
  OOHAMT BCD*10.3 Original Overhead Amount
  OTOTAMTHM BCD*10.3 Original Total Amount
  OBILLCCY String*3 Original Billing Currency
  OCONTSTYLE Integer Original ^2 Style
  OPROJTYPE Integer Original ^2 Type
  OCUSTOMER String*12 Original Customer No.
  OREVREC Integer Original Accounting Method
  OINVTYPE Integer Original Invoice Type
  OWIPACCT String*45 From WIP Account
  OTRANACCT String*45 From Transaction Account
  OREVACCT String*45 From Revenue Account
  OOHACCT String*45 From Overhead Account
  OLABACCT String*45 From Labor Account
  OCVACCT String*45 From Cost Variance Account
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  VENDORID String*12 Vendor
  MODULE String*2 Module
  DOCTYPE Integer Document Type
  TRANSTYPE Integer Transaction Type
  COSTCCY String*3 Cost Currency
  USERID String*8 User ID
  DETAILNUM Long Detail Number
  TIMETYPE Integer Time Type
  DWIPACCT String*45 To WIP Account
  DTRANACCT String*45 To Transaction Account
  DREVACCT String*45 To Revenue Account
  DOHACCT String*45 To Overhead Account
  DLABACCT String*45 To Labor Account
  DCVACCT String*45 To Cost Variance Account
  DFMTCONTNO String*16 To ^1
  DCONTRACT String*16 To ^1
  DPROJECT String*16 To ^2
  DCATEGORY String*16 To ^3
  DCOSTTYPE Integer Cost Type
  DRESOURCE String*24 To Resource
  DITEMNO String*24 To Unformatted Item Number
  DICBTYPE Integer I/C Bucket Type
  DICDOCNUM String*22 I/C Document Number
  DICCMETHOD Integer I/C Costing Method
  DICDATE Date I/C Transaction Date
  DICLOCAT String*6 I/C Location
  DBILLTYPE Integer Revised Billing Type
  DARITEM String*16 Revised A/R Item Number
  DARUOM String*10 Revised A/R Unit of Measure
  DICUOM String*10 Revised ^7
  DQUANTITY BCD*10.5 Revised Quantity
  DUNITCOST BCD*10.6 Revised Unit Cost
  DBILLRATE BCD*10.6 Revised Billing Rate
  DEXTCOSTHM BCD*10.3 Revised Extended Cost
  DEXTCOSTSR BCD*10.3 Revised Extended Cost
  DEXTBILLSR BCD*10.3 Revised Extended Billing Amount
  DLABOR Integer Revised Labor Type
  DLABORRATE BCD*10.6 Revised Labor Rate
  DLABORPER BCD*5.5 Revised Labor Percentage
  DLABORAMT BCD*10.3 Revised Labor Amount
  DOHAMT BCD*10.3 Revised Overhead Amount
  DOVERHD Integer Revised Overhead Type
  DOHEADRATE BCD*10.6 Revised Overhead Rate
  DHEADPER BCD*5.5 Revised Overhead Percentage
  DTOTAMTHM BCD*10.3 Revised Total Amount
  DBILLCCY String*3 Revised Billing Currency
  DCONTSTYLE Integer Revised ^2 Style
  DPROJTYPE Integer Revised ^2 Type
  DCUSTOMER String*12 Revised Customer No.
  DREVREC Integer Revised Accounting Method
  DINVTYPE Integer Revised Invoice Type
  MANITEM String*24
  VALUES Long Optional Fields
  OEARNINGS String*16
  DEARNINGS String*16
  OPAYTYPE Integer Original Pay Type
  DPAYTYPE Integer Revised Pay Type
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment
  OSTAFFCODE String*24 Original Employee No.
  DSTAFFCODE String*24 Revised Employee No.

## PMADJDAO - Adjustment Audit Detail OF (view PM0529)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO+OPTFIELD; OPTFIELD+POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMADJDO - Adjustment Detail Optional Field (view PM0527)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMADJH - Adjustments (view PM0062)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; ADJUSTNO; ADJUSTNO+TRANSTAT; ADJUSTNO+COMPLETE [M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ADJUSTNO String*16 Adjustment Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  ICSEQ Long
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMADJHA - Adjustments Audit (view PM0064)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; SEQ+POSTSEQNO; ADJUSTNO [D]; SEQ+TRANSDATE
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  POSTDATE Date Post Date
  ADJUSTNO String*16 Adjustment Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  REFERENCE String*60 Reference
  DESC String*60 Description
  PRINTSTAT Boolean Printed
  TRANSTAT Integer Transaction Status
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  DATEBUS Date Posting Date

## PMADJHAO - Adjustment Audit Optional Field (view PM0530)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+OPTFIELD; OPTFIELD+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMADJHO - Adjustment Optional Field (view PM0528)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMAGET - Age WIP Report Temporary File (view PM0488)
Keys (first = PK; D=dups allowed, M=modifiable): CONTRACT+PROJECT+CUSTOMER
Fields (NAME type description [values]):
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CUSTOMER String*12 Customer
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CUSTCCY String*3 Customer Currency
  BILLDATE Date Project Billing Date
  TOTALAMT BCD*10.3 Total Amount
  CURAMT BCD*10.3 Current Amount
  AGE1AMT BCD*10.3 Aging Period 1 Amount
  AGE2AMT BCD*10.3 Aging Period 2 Amount
  AGE3AMT BCD*10.3 Aging Period 3 Amount
  OVERAMT BCD*10.3 Over Aging Period 3 Amount
  NAMECUST String*60 Customer Name

## PMAIAST - AIA Superview Temporary File (view PM0472)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+CONTRACT+PROJECT+CATEGORY
Fields (NAME type description [values]):
  SEQ Long Column A
  CONTRACT String*16 Unformatted ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FMTCONTNO String*16 ^1
  TARRECTSSR BCD*10.3 Total A/R Customer Receipts
  COLUMNB String*60 Column B
  COLUMNC BCD*10.3 Column C
  COLUMND BCD*10.3 Column D
  COLUMNE BCD*10.3 Column E
  COLUMNF BCD*10.3 Column F
  COLUMNG BCD*10.3 Column G
  COLUMNH BCD*10.3 Column H
  COLUMNI BCD*10.3 Column I

## PMAIAT - AIA Report Temporary File (view PM0469)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+CONTRACT
Fields (NAME type description [values]):
  SEQ Long Sequence - Column A
  CONTRACT String*16 Unformatted ^1
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FMTCONTNO String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  TARRECTSSR BCD*10.3 Total A/R Customer Receipts
  COLUMNB String*60 Column B
  COLUMNC BCD*10.3 Column C
  COLUMND BCD*10.3 Column D
  COLUMNE BCD*10.3 Column E
  COLUMNF BCD*10.3 Column F
  COLUMNG BCD*10.3 Column G
  COLUMNH BCD*10.3 Column H
  COLUMNI BCD*10.3 Column I
  CONTDESC String*60
  PROJDESC String*60
  CATDESC String*60

## PMAP - A/P Superview (view PM0302)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTENT BCD*4.0 Batch Entry Number
  CNTLINE BCD*3.0 Batch Line Number
  TRANSDATE Date Transaction Date
  DTEBTCH Date Batch Date
  DOCDATE Date Entry Date
  POSTSEQ Long Posting Sequence
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  DOCNUM String*22 Document Number
  VENDORID String*12 Vendor Number
  CCY String*3 Transaction Currency
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator
  RATEOVER Boolean Rate Override [0=False,1=True]
  RATE BCD*8.7 Exchange Rate
  DOCTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Prepayment,6=Unapplied Cash,7=Material Usage,8=Material Return,9=Equipment Usage,10=Timecard,11=Charges,12=Adjustment,13=Retainage Invoice,14=Retainage Credit Note,15=Retainage Debit Note,16=Purchase Order,17=P/O Receipt,18=P/O Return,19=P/O Invoice,20=P/O Credit Note,21=P/O Debit Note,22=Opening Balance,23=Manual Check,24=Cost,25=Check Reversal,26=Material Internal Usage,27=Order Entry,28=O/E Shipment,29=O/E Invoice,30=O/E Debit Note,31=O/E Credit Note]
  TRANSTYPE Integer Transaction Type [1=Posted,2=Discount,3=Write-off,4=Apply From,5=Apply To,6=Payment/Receipt Reversal,7=Rounding (multicurrency),8=Exchange Gain/Loss,9=Unrealized Exchange Gain/Loss,10=Adjustment,11=Receipt/Payment,20=Retainage Rounding,21=Retainage Exchange Gain/Loss,22=Retainage Unrealized Exchange Gain/Loss,23=Opening Retainage Receivable,24=Opening Retainage Payable,25=Invoice Retainage Receivable,26=Invoice Retainage Payable,28=Opening Balance Reversal,29=Refund,30=Refund Reversal,31=Exchange Gain/Loss,32=Retainage Gain/Loss,12=Insert,13=Delete,14=Edit]
  TRANSNUM Long Transaction Number
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  ARITEM String*16 A/R Item Number
  ARUOM String*10 Unit of Measure
  REFERENCE String*60 Reference
  DESC String*60 Description
  QUANTITY BCD*10.5 Quantity
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  TOTAMTSR BCD*10.3 Total Amount (ex tax)
  TOTAMTHM BCD*10.3 Total Amount (ex tax)
  TAXAMTSR BCD*10.3 Tax Amount
  TAXAMTHM BCD*10.3 Tax Amount
  RTAXAMTSR BCD*10.3 Recoverable Tax
  RTAXAMTHM BCD*10.3 Recoverable Tax
  TAMTSR BCD*10.3 Total Amount (inc tax)
  TAMTHM BCD*10.3 Total Amount (inc tax)
  PAYAMTSR BCD*10.3 Amount Paid
  PAYAMTHM BCD*10.3 Amount Paid
  REFDOC String*22 Reference Document
  WIPACCT String*45 Work in Progress Account
  COSTACCT String*45 Cost Account
  OHACCT String*45 Overhead Account
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  LABACCT String*45 Labor Account
  LABORSR BCD*10.3 Labor Amount
  LABORHM BCD*10.3 Labor Amount
  BILLTYPE Integer Billing Type
  COMMENTS String*250 Comments
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Customer/Vendor Tax Class 1
  TCLASS2 Integer Customer/Vendor Tax Class 2
  TCLASS3 Integer Customer/Vendor Tax Class 3
  TCLASS4 Integer Customer/Vendor Tax Class 4
  TCLASS5 Integer Customer/Vendor Tax Class 5
  TITMCLSS1 Integer Item Tax Class 1
  TITMCLSS2 Integer Item Tax Class 2
  TITMCLSS3 Integer Item Tax Class 3
  TITMCLSS4 Integer Item Tax Class 4
  TITMCLSS5 Integer Item Tax Class 5
  TINCLUDE1 Integer Tax Included 1
  TINCLUDE2 Integer Tax Included 2
  TINCLUDE3 Integer Tax Included 3
  TINCLUDE4 Integer Tax Included 4
  TINCLUDE5 Integer Tax Included 5
  TAXBASES1 BCD*10.3 Tax Base 1 Source Currency
  TAXBASES2 BCD*10.3 Tax Base 2 Source Currency
  TAXBASES3 BCD*10.3 Tax Base 3 Source Currency
  TAXBASES4 BCD*10.3 Tax Base 4 Source Currency
  TAXBASES5 BCD*10.3 Tax Base 5 Source Currency
  TAXBASEH1 BCD*10.3 Tax Base 1 Functional Currency
  TAXBASEH2 BCD*10.3 Tax Base 2 Functional Currency
  TAXBASEH3 BCD*10.3 Tax Base 3 Functional Currency
  TAXBASEH4 BCD*10.3 Tax Base 4 Functional Currency
  TAXBASEH5 BCD*10.3 Tax Base 5 Functional Currency
  TAXAMTS1 BCD*10.3 Tax Amount 1 Source Currency
  TAXAMTS2 BCD*10.3 Tax Amount 2 Source Currency
  TAXAMTS3 BCD*10.3 Tax Amount 3 Source Currency
  TAXAMTS4 BCD*10.3 Tax Amount 4 Source Currency
  TAXAMTS5 BCD*10.3 Tax Amount 5 Source Currency
  TAXAMTH1 BCD*10.3 Tax Amount 1 Functional Currency
  TAXAMTH2 BCD*10.3 Tax Amount 2 Functional Currency
  TAXAMTH3 BCD*10.3 Tax Amount 3 Functional Currency
  TAXAMTH4 BCD*10.3 Tax Amount 4 Functional Currency
  TAXAMTH5 BCD*10.3 Tax Amount 5 Functional Currency
  TRANSREF Long Transaction Reference
  TAMTRETSR BCD*10.3 Retainage Amount (Source)
  TAMTRETHM BCD*10.3 Retainage Amount (Functional)
  RETDUEDT Date Retainage Due Date
  ORIGDOC String*24 Original Document Number
  OVERHD Integer Overhead Type
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  LABOR Integer Labor Type
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  ORIGAPP String*2 Original Application
  VALUES Long Optional Fields
  DRILLSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link
  DRILLAPP String*2 Drill Down Application
  EXPTAXSR BCD*10.3 Expensed Tax (source)
  EXPTAXHM BCD*10.3 Expensed Tax (functional)
  TXEXPCOMSR BCD*10.3 Tax (exp) Committed (source)
  TXEXPCOMHM BCD*10.3 Tax (exp) Committed (func)
  TXALLCOMSR BCD*10.3 Tax (all) Committed (source)
  TXALLCOMHM BCD*10.3 Tax (all) Committed (func)
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  STAGE Integer Stage [1=Starting,2=Ending]
  DATEBUS Date Posting Date

## PMAPO - A/P Optional Field (view PM0520)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+OPTFIELD; OPTFIELD+CNTBTCH
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMAR - A/R Superview (view PM0301)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTENT BCD*4.0 Batch Entry Number
  CNTLINE BCD*3.0 Batch Line Number
  TRANSDATE Date Transaction Date
  DTEBTCH Date Batch Date
  DOCDATE Date Entry Date
  POSTSEQ Long Posting Sequence
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  DOCNUM String*22 Document Number
  IDCUST String*12 Customer Number
  CCY String*3 Transaction Currency
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Override [0=False,1=True]
  RATE BCD*8.7 Exchange Rate
  CSTREV Integer Cost/Revenue [1=Cost,2=Revenue]
  DOCTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Prepayment,6=Unapplied Cash,7=Material Usage,8=Material Return,9=Equipment Usage,10=Timecard,11=Charges,12=Adjustment,13=Retainage Invoice,14=Retainage Credit Note,15=Retainage Debit Note,16=Purchase Order,17=P/O Receipt,18=P/O Return,19=P/O Invoice,20=P/O Credit Note,21=P/O Debit Note,22=Opening Balance,23=Manual Check,24=Cost,25=Check Reversal,26=Material Internal Usage,27=Order Entry,28=O/E Shipment,29=O/E Invoice,30=O/E Debit Note,31=O/E Credit Note]
  TRANSTYPE Integer Transactions Type [1=Posted,2=Discount,3=Write-off,4=Apply From,5=Apply To,6=Payment/Receipt Reversal,7=Rounding (multicurrency),8=Exchange Gain/Loss,9=Unrealized Exchange Gain/Loss,10=Adjustment,11=Receipt/Payment,20=Retainage Rounding,21=Retainage Exchange Gain/Loss,22=Retainage Unrealized Exchange Gain/Loss,23=Opening Retainage Receivable,24=Opening Retainage Payable,25=Invoice Retainage Receivable,26=Invoice Retainage Payable,28=Opening Balance Reversal,29=Refund,30=Refund Reversal,31=Exchange Gain/Loss,32=Retainage Gain/Loss,12=Insert,13=Delete,14=Edit]
  TRANSNUM Long Transaction Number
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  ARITEM String*16 A/R Item Number
  ARUOM String*10 Unit of Measure
  REFERENCE String*60 Reference
  DESC String*60 Description
  QUANTITY BCD*10.5 Quantity
  UNITRATE BCD*10.6 Unit Price/Unit Cost
  EXTAMTSR BCD*10.3 Extended Amount
  EXTAMTHM BCD*10.3 Extended Amount
  TOTAMTSR BCD*10.3 Total Amount (ex tax)
  TOTAMTHM BCD*10.3 Total Amount (ex tax)
  TAXAMTSR BCD*10.3 Tax Amount
  TAXAMTHM BCD*10.3 Tax Amount
  TAMTSR BCD*10.3 Total Amount (inc tax)
  TAMTHM BCD*10.3 Total Amount (inc tax)
  RCPAMTSR BCD*10.3 Amount Received
  RCPAMTHM BCD*10.3 Amount Received
  REFDOC String*22 Reference Document
  WIPACCT String*45 Work in Progress Account
  REVACCT String*45 Billings/Sales Account
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Customer/Vendor Tax Class 1
  TCLASS2 Integer Customer/Vendor Tax Class 2
  TCLASS3 Integer Customer/Vendor Tax Class 3
  TCLASS4 Integer Customer/Vendor Tax Class 4
  TCLASS5 Integer Customer/Vendor Tax Class 5
  TITMCLSS1 Integer Item Tax Class 1
  TITMCLSS2 Integer Item Tax Class 2
  TITMCLSS3 Integer Item Tax Class 3
  TITMCLSS4 Integer Item Tax Class 4
  TITMCLSS5 Integer Item Tax Class 5
  TINCLUDE1 Integer Tax Included 1
  TINCLUDE2 Integer Tax Included 2
  TINCLUDE3 Integer Tax Included 3
  TINCLUDE4 Integer Tax Included 4
  TINCLUDE5 Integer Tax Included 5
  TAXBASES1 BCD*10.3 Tax Base 1 Source Currency
  TAXBASES2 BCD*10.3 Tax Base 2 Source Currency
  TAXBASES3 BCD*10.3 Tax Base 3 Source Currency
  TAXBASES4 BCD*10.3 Tax Base 4 Source Currency
  TAXBASES5 BCD*10.3 Tax Base 5 Source Currency
  TAXBASEH1 BCD*10.3 Tax Base 1 Functional Currency
  TAXBASEH2 BCD*10.3 Tax Base 2 Functional Currency
  TAXBASEH3 BCD*10.3 Tax Base 3 Functional Currency
  TAXBASEH4 BCD*10.3 Tax Base 4 Functional Currency
  TAXBASEH5 BCD*10.3 Tax Base 5 Functional Currency
  TAXAMTS1 BCD*10.3 Tax Amount 1 Source Currency
  TAXAMTS2 BCD*10.3 Tax Amount 2 Source Currency
  TAXAMTS3 BCD*10.3 Tax Amount 3 Source Currency
  TAXAMTS4 BCD*10.3 Tax Amount 4 Source Currency
  TAXAMTS5 BCD*10.3 Tax Amount 5 Source Currency
  TAXAMTH1 BCD*10.3 Tax Amount 1 Functional Currency
  TAXAMTH2 BCD*10.3 Tax Amount 2 Functional Currency
  TAXAMTH3 BCD*10.3 Tax Amount 3 Functional Currency
  TAXAMTH4 BCD*10.3 Tax Amount 4 Functional Currency
  TAXAMTH5 BCD*10.3 Tax Amount 5 Functional Currency
  RTAXSR BCD*10.3 Recoverable Tax Amount
  RTAXHM BCD*10.3 Recoverable Tax Amount
  TRANSREF Long Transaction Reference
  COMMENTS String*250 Comments
  TAMTRETSR BCD*10.3 Retainage Amount (Source)
  TAMTRETHM BCD*10.3 Retainage Amount (Functional)
  RETDUEDT Date Retainage Due Date
  ORIGDOC String*24 Original Document Number
  ORIGAPP String*2 Original Application
  VALUES Long Optional Fields
  DRILLSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link
  DRILLAPP String*2 Drill Down Application
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  COSTQTY BCD*10.5 Cost Quantity
  UNITCOST BCD*10.6 Not in Use
  EXTCOSTSR BCD*10.3 Extended Cost (Source)
  EXTCOSTHM BCD*10.3 Extended Cost (Functional)
  OHEADACCT String*45 Overhead Account
  OHEADSR BCD*10.3 Overhead Amount
  OHEADHM BCD*10.3 Overhead Amount
  LABACCT String*45 Labor Account
  LABSR BCD*10.3 Labor Amount
  LABHM BCD*10.3 Labor Amount
  OHTYPE Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHRATE BCD*10.6 Overhead Rate
  OHPER BCD*5.5 Overhead Percentage
  LABTYPE Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABRATE BCD*10.6 Labor Rate
  LABPER BCD*5.5 Labor Percentage
  TOTCOSTSR BCD*10.3 Total Cost Amount (Source)
  TOTCOSTHM BCD*10.3 Total Cost Amount (Functional)
  DETAILTYPE Integer O/E Detail Line Type [0=Item,1=Miscellaneous Charges]
  STAGE Integer Stage [1=Starting,2=Ending]
  DATEBUS Date Posting Date

## PMARO - A/R Optional Field (view PM0521)
Keys (first = PK; D=dups allowed, M=modifiable): CNTBTCH+OPTFIELD; OPTFIELD+CNTBTCH
Fields (NAME type description [values]):
  CNTBTCH BCD*5.0 Batch Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMBUDA - Budget Audit (view PM0126)
Keys (first = PK; D=dups allowed, M=modifiable): BUDSEQ; CONTRACT [D,M]
Fields (NAME type description [values]):
  BUDSEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POSTDATE Date Posting Date
  POSTTIME Time Posting Time
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  BUDGET Integer Budget Set
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  COSTCCY String*3 Cost Currency
  QUANTITY BCD*10.5 Quantity
  COSTS BCD*10.3 Cost (Source)
  COSTH BCD*10.3 Cost (Functional)
  REVENUES BCD*10.3 Revenue (Source)
  REVENUEH BCD*10.3 Revenue (Functional)
  MODULE String*4 Module
  DOCNUM String*24 Document Number

## PMBUDD - Budget Detail (view PM0122)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENUM; CTUNIQ+FISCALYEAR+BUDGET+LINENUM; CONTRACT+FISCALYEAR+BUDGET+LINENUM; CONTRACT+PROJECT+CATEGORY+RESOURCE+FISCALYEAR+BUDGET+COSTCCY+CCYTYPE
Fields (NAME type description [values]):
  SEQ Long
  LINENUM Long
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CTUNIQ BCD*10.0 ^1 Uniq
  FISCALYEAR String*4 Fiscal Year
  BUDGET Integer Budget Set [1=1,2=2,3=3,4=4,5=5,500=Actuals,501=Recognized]
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  REVCCY String*3 Revenue Currency
  COSTCCY String*3 Cost Currency
  CCYTYPE Integer Currency Type
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  Q1 BCD*10.5 Quantity For Period 1
  Q2 BCD*10.5 Quantity For Period 2
  Q3 BCD*10.5 Quantity For Period 3
  Q4 BCD*10.5 Quantity For Period 4
  Q5 BCD*10.5 Quantity For Period 5
  Q6 BCD*10.5 Quantity For Period 6
  Q7 BCD*10.5 Quantity For Period 7
  Q8 BCD*10.5 Quantity For Period 8
  Q9 BCD*10.5 Quantity For Period 9
  Q10 BCD*10.5 Quantity For Period 10
  Q11 BCD*10.5 Quantity For Period 11
  Q12 BCD*10.5 Quantity For Period 12
  Q13 BCD*10.5 Quantity For Period 13
  Q14 BCD*10.5
  Q15 BCD*10.5
  QTOTAL BCD*10.5 Total Quantity For The Year
  CS1 BCD*10.3 Total Cost (Source) For Period 1
  CS2 BCD*10.3 Total Cost (Source) For Period 2
  CS3 BCD*10.3 Total Cost (Source) For Period 3
  CS4 BCD*10.3 Total Cost (Source) For Period 4
  CS5 BCD*10.3 Total Cost (Source) For Period 5
  CS6 BCD*10.3 Total Cost (Source) For Period 6
  CS7 BCD*10.3 Total Cost (Source) For Period 7
  CS8 BCD*10.3 Total Cost (Source) For Period 8
  CS9 BCD*10.3 Total Cost (Source) For Period 9
  CS10 BCD*10.3 Total Cost (Source) For Period 10
  CS11 BCD*10.3 Total Cost (Source) For Period 11
  CS12 BCD*10.3 Total Cost (Source) For Period 12
  CS13 BCD*10.3 Total Cost (Source) For Period 13
  CS14 BCD*10.3
  CS15 BCD*10.3
  CSTOTAL BCD*10.3 Total Cost (Source) For The Year
  CH1 BCD*10.3 Total Cost (Functional) For Period 1
  CH2 BCD*10.3 Total Cost (Functional) For Period 2
  CH3 BCD*10.3 Total Cost (Functional) For Period 3
  CH4 BCD*10.3 Total Cost (Functional) For Period 4
  CH5 BCD*10.3 Total Cost (Functional) For Period 5
  CH6 BCD*10.3 Total Cost (Functional) For Period 6
  CH7 BCD*10.3 Total Cost (Functional) For Period 7
  CH8 BCD*10.3 Total Cost (Functional) For Period 8
  CH9 BCD*10.3 Total Cost (Functional) For Period 9
  CH10 BCD*10.3 Total Cost (Functional) For Period 10
  CH11 BCD*10.3 Total Cost (Functional) For Period 11
  CH12 BCD*10.3 Total Cost (Functional) For Period 12
  CH13 BCD*10.3 Total Cost (Functional) For Period 13
  CH14 BCD*10.3
  CH15 BCD*10.3
  CHTOTAL BCD*10.3 Total Cost (Functional) For The Year
  RS1 BCD*10.3 Total Revenue (Source) For Period 1
  RS2 BCD*10.3 Total Revenue (Source) For Period 2
  RS3 BCD*10.3 Total Revenue (Source) For Period 3
  RS4 BCD*10.3 Total Revenue (Source) For Period 4
  RS5 BCD*10.3 Total Revenue (Source) For Period 5
  RS6 BCD*10.3 Total Revenue (Source) For Period 6
  RS7 BCD*10.3 Total Revenue (Source) For Period 7
  RS8 BCD*10.3 Total Revenue (Source) For Period 8
  RS9 BCD*10.3 Total Revenue (Source) For Period 9
  RS10 BCD*10.3 Total Revenue (Source) For Period 10
  RS11 BCD*10.3 Total Revenue (Source) For Period 11
  RS12 BCD*10.3 Total Revenue (Source) For Period 12
  RS13 BCD*10.3 Total Revenue (Source) For Period 13
  RS14 BCD*10.3
  RS15 BCD*10.3
  RSTOTAL BCD*10.3 Total Revenue (Source) For The Year
  RH1 BCD*10.3 Total Revenue (Functional) For Period 1
  RH2 BCD*10.3 Total Revenue (Functional) For Period 2
  RH3 BCD*10.3 Total Revenue (Functional) For Period 3
  RH4 BCD*10.3 Total Revenue (Functional) For Period 4
  RH5 BCD*10.3 Total Revenue (Functional) For Period 5
  RH6 BCD*10.3 Total Revenue (Functional) For Period 6
  RH7 BCD*10.3 Total Revenue (Functional) For Period 7
  RH8 BCD*10.3 Total Revenue (Functional) For Period 8
  RH9 BCD*10.3 Total Revenue (Functional) For Period 9
  RH10 BCD*10.3 Total Revenue (Functional) For Period 10
  RH11 BCD*10.3 Total Revenue (Functional) For Period 11
  RH12 BCD*10.3 Total Revenue (Functional) For Period 12
  RH13 BCD*10.3 Total Revenue (Functional) For Period 13
  RH14 BCD*10.3
  RH15 BCD*10.3
  RHTOTAL BCD*10.3 Total Revenue (Functional) For The Year
  INQ1 BCD*10.5 Inquiry Quantity For Period 1
  INQ2 BCD*10.5 Inquiry Quantity For Period 2
  INQ3 BCD*10.5 Inquiry Quantity For Period 3
  INQ4 BCD*10.5 Inquiry Quantity For Period 4
  INQ5 BCD*10.5 Inquiry Quantity For Period 5
  INQ6 BCD*10.5 Inquiry Quantity For Period 6
  INQ7 BCD*10.5 Inquiry Quantity For Period 7
  INQ8 BCD*10.5 Inquiry Quantity For Period 8
  INQ9 BCD*10.5 Inquiry Quantity For Period 9
  INQ10 BCD*10.5 Inquiry Quantity For Period 10
  INQ11 BCD*10.5 Inquiry Quantity For Period 11
  INQ12 BCD*10.5 Inquiry Quantity For Period 12
  INQ13 BCD*10.5 Inquiry Quantity For Period 13
  INQ14 BCD*10.5
  INQ15 BCD*10.5
  INQTOTAL BCD*10.5 Inquiry Total Quantity For The Year
  INCS1 BCD*10.3 Inquiry Total Cost (Source) For Period 1
  INCS2 BCD*10.3 Inquiry Total Cost (Source) For Period 2
  INCS3 BCD*10.3 Inquiry Total Cost (Source) For Period 3
  INCS4 BCD*10.3 Inquiry Total Cost (Source) For Period 4
  INCS5 BCD*10.3 Inquiry Total Cost (Source) For Period 5
  INCS6 BCD*10.3 Inquiry Total Cost (Source) For Period 6
  INCS7 BCD*10.3 Inquiry Total Cost (Source) For Period 7
  INCS8 BCD*10.3 Inquiry Total Cost (Source) For Period 8
  INCS9 BCD*10.3 Inquiry Total Cost (Source) For Period 9
  INCS10 BCD*10.3 Inquiry Total Cost (Source) For Period 10
  INCS11 BCD*10.3 Inquiry Total Cost (Source) For Period 11
  INCS12 BCD*10.3 Inquiry Total Cost (Source) For Period 12
  INCS13 BCD*10.3 Inquiry Total Cost (Source) For Period 13
  INCS14 BCD*10.3
  INCS15 BCD*10.3
  INCSTOTAL BCD*10.3 Inquiry Total Cost (Source) For The Year
  INCH1 BCD*10.3 Inquiry Total Cost (Functional) For Period 1
  INCH2 BCD*10.3 Inquiry Total Cost (Functional) For Period 2
  INCH3 BCD*10.3 Inquiry Total Cost (Functional) For Period 3
  INCH4 BCD*10.3 Inquiry Total Cost (Functional) For Period 4
  INCH5 BCD*10.3 Inquiry Total Cost (Functional) For Period 5
  INCH6 BCD*10.3 Inquiry Total Cost (Functional) For Period 6
  INCH7 BCD*10.3 Inquiry Total Cost (Functional) For Period 7
  INCH8 BCD*10.3 Inquiry Total Cost (Functional) For Period 8
  INCH9 BCD*10.3 Inquiry Total Cost (Functional) For Period 9
  INCH10 BCD*10.3 Inquiry Total Cost (Functional) For Period 10
  INCH11 BCD*10.3 Inquiry Total Cost (Functional) For Period 11
  INCH12 BCD*10.3 Inquiry Total Cost (Functional) For Period 12
  INCH13 BCD*10.3 Inquiry Total Cost (Functional) For Period 13
  INCH14 BCD*10.3
  INCH15 BCD*10.3
  INCHTOTAL BCD*10.3 Inquiry Total Cost (Functional) For The Year
  INRS1 BCD*10.3 Inquiry Total Revenue (Source) For Period 1
  INRS2 BCD*10.3 Inquiry Total Revenue (Source) For Period 2
  INRS3 BCD*10.3 Inquiry Total Revenue (Source) For Period 3
  INRS4 BCD*10.3 Inquiry Total Revenue (Source) For Period 4
  INRS5 BCD*10.3 Inquiry Total Revenue (Source) For Period 5
  INRS6 BCD*10.3 Inquiry Total Revenue (Source) For Period 6
  INRS7 BCD*10.3 Inquiry Total Revenue (Source) For Period 7
  INRS8 BCD*10.3 Inquiry Total Revenue (Source) For Period 8
  INRS9 BCD*10.3 Inquiry Total Revenue (Source) For Period 9
  INRS10 BCD*10.3 Inquiry Total Revenue (Source) For Period 10
  INRS11 BCD*10.3 Inquiry Total Revenue (Source) For Period 11
  INRS12 BCD*10.3 Inquiry Total Revenue (Source) For Period 12
  INRS13 BCD*10.3 Inquiry Total Revenue (Source) For Period 13
  INRS14 BCD*10.3
  INRS15 BCD*10.3
  INRSTOTAL BCD*10.3 Inquiry Total Revenue (Source) For The Year
  INRH1 BCD*10.3 Inquiry Total Revenue (Functional) For Period 1
  INRH2 BCD*10.3 Inquiry Total Revenue (Functional) For Period 2
  INRH3 BCD*10.3 Inquiry Total Revenue (Functional) For Period 3
  INRH4 BCD*10.3 Inquiry Total Revenue (Functional) For Period 4
  INRH5 BCD*10.3 Inquiry Total Revenue (Functional) For Period 5
  INRH6 BCD*10.3 Inquiry Total Revenue (Functional) For Period 6
  INRH7 BCD*10.3 Inquiry Total Revenue (Functional) For Period 7
  INRH8 BCD*10.3 Inquiry Total Revenue (Functional) For Period 8
  INRH9 BCD*10.3 Inquiry Total Revenue (Functional) For Period 9
  INRH10 BCD*10.3 Inquiry Total Revenue (Functional) For Period 10
  INRH11 BCD*10.3 Inquiry Total Revenue (Functional) For Period 11
  INRH12 BCD*10.3 Inquiry Total Revenue (Functional) For Period 12
  INRH13 BCD*10.3 Inquiry Total Revenue (Functional) For Period 13
  INRH14 BCD*10.3
  INRH15 BCD*10.3
  INRHTOTAL BCD*10.3 Inquiry Total Revenue (Functional) For The Year
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATE BCD*8.7 Rate

## PMBUDH - Budget Header (view PM0123)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; CTUNIQ+FISCALYEAR+BUDGET; CONTRACT+FISCALYEAR+BUDGET; FMTCONTNO+FISCALYEAR+BUDGET
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CTUNIQ BCD*10.0 ^1 Uniq
  FISCALYEAR String*4 Fiscal Year
  BUDGET Integer Budget Set [1=1,2=2,3=3,4=4,5=5,500=Actuals,501=Recognized]
  CONTRACT String*16 ^1
  FMTCONTNO String*16 ^1
  BUDUNIQ Long
  FROMPMBUDS Integer
  ENTEREDBY String*8 Entered By

## PMBWC - Billing Worksheet Customer (view PM0083)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENUM; WORKID+CUSTLINE; WORKID+CUSTOMER [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WORKID String*30 Worksheet Number
  CUSTLINE Long Customer Line Number
  CUSTOMER String*12 Customer
  NAMECUST String*60 Customer Name
  BILSTATUS Integer Status [1=Invoice,2=Hold]
  BILAMTSR BCD*10.3 Document Amount
  BILAMTHM BCD*10.3 Document Amount
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  PONUMBER String*22 P/O Number
  CURRENCY String*3 Currency
  TEXTOPFL1 String*2 Reserved
  TEXTOPFL2 String*3 Reserved
  TEXTOPFL3 String*4 Reserved
  TEXTOPFL4 String*12 Reserved
  TEXTOPFL5 String*15 Reserved
  TEXTOPFL6 String*30 Reserved
  OPFLDATE Date Reserved
  OPFLAMT BCD*10.3 Reserved
  RATESPREAD BCD*8.7
  RETRATE Integer [1=Use Original Document Exchange Rate,2=Use Current Exchange Rate]
  CONTRACT String*16 ^1
  FMTCONTNO String*16 ^1
  PROJECT String*16 ^2
  NUMDTL Long
  CODETAXGRP String*12 Tax Group
  TCLASS1 Integer Customer Tax Class 1
  TCLASS2 Integer Customer Tax Class 2
  TCLASS3 Integer Customer Tax Class 3
  TCLASS4 Integer Customer Tax Class 4
  TCLASS5 Integer Customer Tax Class 5
  TAUTH1 String*12 Customer Tax Authority 1
  TAUTH2 String*12 Customer Tax Authority 2
  TAUTH3 String*12 Customer Tax Authority 3
  TAUTH4 String*12 Customer Tax Authority 4
  TAUTH5 String*12 Customer Tax Authority 5
  RCURRENCY String*3 Tax Reporting Currency
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEOPRC Integer Tax Reporting Rate Operator
  RATEOVERRC Boolean Tax Reporting Override
  RATEOVER Boolean Rate Override
  ARACCTSET String*6 A/R Account Set

## PMBWD - Billing Worksheet Detail (view PM0082)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENUM; WORKID+DETAILNUM; WORKID+CUSTOMER+CONTRACT+PROJECT+CATEGORY+TRANSNUM; TRANSDATE [D,M]; WORKID+CUSTLINE+INVTYPE [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WORKID String*30 Worksheet Number
  CUSTLINE Long Customer Line Number
  DETAILNUM Long Detail Line Number
  CUSTOMER String*12 Customer
  NAMECUST String*60 Customer Name
  TEXTDESC String*60 Description
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  COSTTYPE Integer Cost Class
  PROJTYPE Integer Project Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  TRANSNUM Long Transaction Number
  BILSTATUS Integer Status [1=Invoice,2=Hold]
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  GLACCT String*45 G/L Account
  ACCTDESC String*60 Account Description
  QUANTITY BCD*10.5 Quantity
  UNITPRICE BCD*10.6 Unit Price
  BILLPER BCD*5.5 Percentage Complete
  BILAMTSR BCD*10.3 Extended Amount (Source)
  BILAMTHM BCD*10.3 Extended Amount (Functional)
  ARITEM String*16 A/R Item Number
  ARUOM String*10 A/R Unit of Measure
  COMMENT String*250 Comment
  STATUS Integer Status [1=Not Posted,2=Posted]
  TRANSDATE Date Transaction Date
  RETPERCENT BCD*5.5 Retainage Percentage
  RETPERIOD Integer Retention Period
  FMTCONTNO String*16 ^1
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  REFERENCE String*60 Reference
  MODULE String*4 Module
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  DOCTYPE Integer Document Type [0=None,1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Prepayment,6=Unapplied Cash,7=Material Usage,8=Material Return,9=Equipment Usage,10=Timecard,11=Charges,12=Adjustment,13=Retainage Invoice,14=Retainage Credit Note,15=Retainage Debit Note,16=Purchase Order,17=P/O Receipt,18=P/O Return,19=P/O Invoice,20=P/O Credit Note,21=P/O Debit Note,22=Opening Balance,23=Manual Check,24=Cost,25=Check Reversal,26=Material Internal Usage,27=Order Entry,28=O/E Shipment,29=O/E Invoice,30=O/E Debit Note,31=O/E Credit Note]
  DOCNUM String*24 Document Number
  EXTAMTSR BCD*10.3 Amount Originally on PMTRAN
  BILLAMTC BCD*10.3 Amount BILLAMTC was updated by
  VALUES Long Optional Fields

## PMBWDO - Billing Detail Optional Field (view PM0544)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENUM+OPTFIELD; OPTFIELD+SEQ+LINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENUM Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMBWH - Billing Worksheet (view PM0081)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; WORKID
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WORKID String*30 Worksheet Number
  RUNDATE Date Document Date
  DESC String*60 Description
  INVTYPE Integer Invoice Type [1=Item,2=Summary,3=Both]
  EXRATE Integer Exchange Rate
  NEXTCUST Long Next Customer Line Number
  NEXTDTL Long Next Detail Line Number
  POSTABLE Boolean Ready To Post
  POSTINAR Boolean Posted To A/R [0=No,1=Yes]
  RETRATE Integer [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  MANAGER String*16 Manager
  NUMCUST Long Number of Customer Lines
  NUMDTL Long Number of Detail Lines
  INVYEAR String*4 Invoice Fiscal Year
  INVPER Integer Invoice Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  DATEBUS Date Posting Date
  ENTEREDBY String*8 Entered By
  PRINTSTAT Boolean Printed

## PMBWHO - Billing Optional Field (view PM0542)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ; WORKID+OPTFIELD [D,M]; OPTFIELD+WORKID [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  WORKID String*30 Copying ^1...
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCATGT - ^1 ^6 (view PM0039)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+PLINENUM+CLINENUM; CTUNIQ+DNUM; CONTRACT+PROJECT+CATEGORY; CTUNIQ+DETAILNUM+DNUM; CONTRACT+CATEGORY+PLINENUM
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 ^1 Unique Code
  PLINENUM Long Project Line Number
  CLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  CCY String*3 Currency
  DETAILNUM Long ^2 Detail Number
  DNUM Long ^3 Detail Number
  DATELASTMN Date Last Maintained
  DESC String*60 Description
  COSTTYPE String*10 Cost Type
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  PONUMBER String*22 Last Purchase Order Number
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  ORJQTY BCD*10.5 Quantity
  CURQTY BCD*10.5 Current Quantity Estimate
  ACTQTY BCD*10.5 Actual Quantity
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  ORJCOSTSR BCD*10.3 Reserved
  ORJCOSTHM BCD*10.3 Extended Cost
  CURCOSTSR BCD*10.3 Reserved
  CURCOSTHM BCD*10.3 Current Cost Estimate
  ACTCOSTSR BCD*10.3 Reserved
  ACTCOSTHM BCD*10.3 Actual Cost
  BILLRATE BCD*10.6 Billing Rate
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  ORJOHSR BCD*10.3 Reserved
  ORJOHHM BCD*10.3 Original Overhead Estimate
  CUROHSR BCD*10.3 Reserved
  CUROHHM BCD*10.3 Current Overhead Estimate
  ACTOHSR BCD*10.3 Reserved
  ACTOHHM BCD*10.3 Actual Overhead
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  ORJLABORSR BCD*10.3 Reserved
  ORJLABORHM BCD*10.3 Original Labor Amount Estimate
  CURLABORSR BCD*10.3 Reserved
  CURLABORHM BCD*10.3 Current Labor Amount Estimate
  ACTLABORSR BCD*10.3 Reserved
  ACTLABORHM BCD*10.3 Actual Labor Amount
  COSTPLUSP BCD*5.5 Cost Plus Percentage
  ORJBILLSR BCD*10.3 Revenue
  ORJBILLHM BCD*10.3 Revenue
  CURBILLSR BCD*10.3 Current Revenue Estimate
  CURBILLHM BCD*10.3 Current Revenue Estimate
  ACTBILLHM BCD*10.3 Total Actual Revenue
  ACTBILLSR BCD*10.3 Total Actual Revenue
  ACTBILRRHM BCD*10.3 Total Revenue Recognized
  ACTBILRRSR BCD*10.3 Total Revenue Recognized
  CCYBILL String*3 Customer Currency
  TORJCOSTSR BCD*10.3 Reserved
  TORJCOSTHM BCD*10.3 Total Original Estimate Cost
  TCURCOSTSR BCD*10.3 Reserved
  TCURCOSTHM BCD*10.3 Total Current Estimate Cost
  TACTCOSTSR BCD*10.3 Reserved
  TACTCOSTHM BCD*10.3 Total Actual Cost
  TCOSTRRSR BCD*10.3 Reserved
  TCOSTRRHM BCD*10.3 Total Cost Recognized
  PERTOTCOST BCD*5.5 Percent Total Cost
  TARRECTSSR BCD*10.3 Total A/R Customer Receipts
  TARRECTSHM BCD*10.3 Total A/R Customer Receipts
  TAPPAYMTS BCD*10.3 A/P Vendor Payments
  PERRETPAID BCD*5.5 A/P Retainage Percentage
  RETPAIDD Integer A/P Retention Period
  RETARAMTSR BCD*10.3 Retainage Receivable
  RETARAMTHM BCD*10.3 Retainage Receivable
  RETARRECSR BCD*10.3 Retainage Amount Received in A/R
  RETARRECHM BCD*10.3 Retainage Amount Received in A/R
  RETAPAMT BCD*10.3 Retainage Payable
  RETAPPAID BCD*10.3 Retainage Amount Paid in A/P
  POAMOUNTSR BCD*10.3 Reserved
  POAMOUNTHM BCD*10.3 Reserved
  POQTY BCD*10.5 Committed P/O Quantity
  OEAMOUNTSR BCD*10.3 Reserved
  OEAMOUNTHM BCD*10.3 Recognized Loss
  OEQTY BCD*10.5 Reserved
  POSTDATE Date Last Posting Date
  WIPACCT String*45 Work in Progress
  COSTACCT String*45 Cost of Sales
  PAYACCT String*45 Payroll Expense
  EXPACCT String*45 Employee Expense
  EQUIPACCT String*45 Equipment
  OHACCT String*45 Overhead
  LABACCT String*45 Labor
  GAINACCT String*45 Unrecognized Gain/Loss
  LCSTAMT BCD*10.3 Last Cost Amount
  LCSTDATE Date Last Cost Date
  INVPEND BCD*10.3 Invoice Pending
  LRECAMT BCD*10.3 Last Amount Recognized
  LRECDATE Date Last Recognized Date
  LINVAMT BCD*10.3 Last Invoice Amount
  LINVDATE Date Last Invoice Date
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  TAXBASES1 BCD*10.3 Tax Base 1
  TAXBASES2 BCD*10.3 Tax Base 2
  TAXBASES3 BCD*10.3 Tax Base 3
  TAXBASES4 BCD*10.3 Tax Base 4
  TAXBASES5 BCD*10.3 Tax Base 5
  TAXBASEH1 BCD*10.3 Tax Base 1
  TAXBASEH2 BCD*10.3 Tax Base 2
  TAXBASEH3 BCD*10.3 Tax Base 3
  TAXBASEH4 BCD*10.3 Tax Base 4
  TAXBASEH5 BCD*10.3 Tax Base 5
  TAXAMTS1 BCD*10.3 Tax Amount 1
  TAXAMTS2 BCD*10.3 Tax Amount 2
  TAXAMTS3 BCD*10.3 Tax Amount 3
  TAXAMTS4 BCD*10.3 Tax Amount 4
  TAXAMTS5 BCD*10.3 Tax Amount 5
  TAXAMTH1 BCD*10.3 Tax Amount 1
  TAXAMTH2 BCD*10.3 Tax Amount 2
  TAXAMTH3 BCD*10.3 Tax Amount 3
  TAXAMTH4 BCD*10.3 Tax Amount 4
  TAXAMTH5 BCD*10.3 Tax Amount 5
  INVSTATE Integer Invoice Status [1=Not Processed,2=On Worksheet,3=On Invoice]
  BILLAMT BCD*10.3 Expected Billings
  LSTBILLPER BCD*5.5 Last Billings Percent Complete
  PRFTLOSSSR BCD*10.3 Recognized Profit / Loss
  PRFTLOSSHM BCD*10.3 Recognized Profit / Loss
  REVESTDATE Date Last Revised Posting Date
  LSTRRPER BCD*5.5 Last Rev. Recognition Percentage
  OOHTYPE Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OOHRATE BCD*10.6 Overhead Rate
  OOHPER BCD*5.5 Overhead Percentage
  COHTYPE Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  COHRATE BCD*10.6 Overhead Rate
  COHPER BCD*5.5 Overhead Percentage
  OLABORTYPE Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  OLABORRATE BCD*10.6 Labor Rate
  OLABORPER BCD*5.5 Labor Percentage
  CLABORTYPE Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  CLABORRATE BCD*10.6 Labor Rate
  CLABORPER BCD*5.5 Labor Percentage
  OUNITCOST BCD*10.6 Original Unit Cost
  OBILLRATE BCD*10.6 Original Billing Rate
  OCOSTPLUSP BCD*5.5 Original Cost Plus Percentage
  CUNITCOST BCD*10.6 Current Unit Cost
  CBILLRATE BCD*10.6 Current Billing Rate
  CCOSTPLUSP BCD*5.5 Current Cost Plus Percentage
  ODATEFROM Date Projected Start Date
  ODATETO Date Projected End Date
  CDATEFROM Date Current Start Date
  CDATETO Date Current End Date
  ORATETYPE String*2 Original Rate Type
  ORATEDATE Date Original Rate Date
  ORATE BCD*8.7 Original Rate
  CRATETYPE String*2 Current Rate Type
  CRATEDATE Date Current Rate Date
  CRATE BCD*8.7 Current Rate
  PLCODE String*16 Reserved
  DEFRETFROM Integer Default Retainage From [0=Category,1=Vendor]
  BILLAMTC BCD*10.3 Current Billings (AR and on BW)
  POCOSTHM BCD*10.3 Committed P/O Cost
  POOHHM BCD*10.3 Committed P/O Overhead
  POLABORHM BCD*10.3 Committed P/O Labor
  POTCOSTHM BCD*10.3 Committed P/O Total Cost
  VALUES Long Optional Fields
  TCUNITCOST Integer Default Unit Cost From [0=Use Default PJC Option,2=PJC Employee Setup,6=Category]
  TCBILLRATE Integer Default Billing Rate From [0=Use Default PJC Option,2=PJC Employee Setup,6=Category]
  CEACCT String*45 Cost
  STRDQTY BCD*10.5 Stored Quantity
  STRDCOSTHM BCD*10.3 Stored Cost
  STRDBILLSR BCD*10.3 Stored Billable Amount
  PRECOLEDSR BCD*10.3 Previous D + E
  STRDOHHM BCD*10.3 Overhead Amount
  STRDTCSTHM BCD*10.3 Total Stored Cost
  TXEXPCOMHM BCD*10.3 Tax (exp) Committed (func)
  TXALLCOMHM BCD*10.3 Tax (all) Committed (func)
  PREAIAPAY BCD*10.3 Previous Certificates for Payment
  PRESTORED BCD*10.3 G703 Column F from Last AIA Report
  PRERETAIN BCD*10.3 G703 Column I from Last AIA Report

## PMCATGTO - Category Optional Field (view PM0852)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+PLINENUM+CLINENUM+OPTFIELD; OPTFIELD+CTUNIQ+PLINENUM+CLINENUM [D]; CONTRACT+PROJECT+CATEGORY+OPTFIELD [D]
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 Contract Uniq
  PLINENUM Long Project Line Number
  CLINENUM Long Category Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CATEGORY String*16 Category
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCED - Cost Entries Detail (view PM0422)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; DOCNUM+LINENO; SEQ+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*24 Document Number
  LINETYPE Integer Line Type [1=Miscellaneous Cost,2=Time,3=Expense,4=Equipment,5=Material Usage,6=Material Return,7=Charge]
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  CHARGECODE String*16 Charge Code
  DESC String*60 Description
  QUANTITY BCD*10.5 Quantity
  ARITEM String*16 A/R Item No.
  ARUOM String*10 A/R Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  COSTCCY String*3 Cost Currency
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost (HM)
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount (HM)
  LABOR Integer Labor Type
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  LABORSR BCD*10.3 Transaction Labor Amount (Source)
  LABORHM BCD*10.3 Transaction Labor Amount (Functional)
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost (HM)
  COMMENTS String*250 Comments
  TRANACCT String*45 Cost Account
  OHACCT String*45 Overhead Account
  LABORACCT String*45 Labor Account
  WIPACCT String*45 Work in Progress Account
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  BILLRATE BCD*10.6 Billing Rate
  EXTBILLSR BCD*10.3 Billing Amount
  EXTBILLHM BCD*10.3 Billing Amount (HM)
  BILLCCY String*3 Billing Currency
  DETAILNUM Long Detail Number
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  CONTSTYLE Integer Contract Style [1=Standard,2=Basic]
  PROJTYPE Integer Project Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CUSTOMER String*12 Customer
  REVREC Integer Revenue Rec. Type [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Inventory Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  PAYTYPE Integer Pay Type
  TRANSDATE Date Transaction Date
  EXPENSE String*16 Expense
  EXPTYPE Integer Expense Type
  LOCATION String*6 Location
  ICUOM String*10 I/C Unit of Measure
  CONVERSION BCD*10.6
  STOCKITEM Boolean Stock Item
  COSTMETHOD Integer Cost Method
  UNFMTITEM String*24 Unformatted Item No.
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment

## PMCEDA - Cost Entries Detail Audit (view PM0426)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  DOCNUM String*24 Document Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  LINETYPE Integer Line Type
  TYPE Integer Cost Class
  DESC String*60 Description
  QUANTITY BCD*10.5 Quantity
  ARITEM String*16 A/R Item No.
  ARUOM String*10 A/R Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  COSTCCY String*3 Cost Currency
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost (HM)
  OVERHD Integer Overhead Type
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount (HM)
  LABOR Integer Labor Type
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  LABORSR BCD*10.3 Transaction Labor Amount (Source)
  LABORHM BCD*10.3 Transaction Labor Amount (Functional)
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost (HM)
  COMMENTS String*250 Comments
  TRANACCT String*45 Cost Account
  OHACCT String*45 Overhead Account
  LABORACCT String*45 Labor Account
  WIPACCT String*45 Work in Progress Account
  BILLTYPE Integer Billing Type
  BILLRATE BCD*10.6 Billing Rate
  EXTBILLSR BCD*10.3 Billing Amount
  EXTBILLHM BCD*10.3 Billing Amount (HM)
  BILLCCY String*3 Billing Currency
  DETAILNUM Long Detail Number
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  CONTSTYLE Integer Contract Style
  PROJTYPE Integer Project Type
  CUSTOMER String*12 Customer
  REVREC Integer Revenue Rec. Type
  INVTYPE Integer Inventory Type
  VALUES Long Optional Fields
  PAYTYPE Integer Pay Type
  TRANSDATE Date Transaction Date
  EXPENSE String*16 Expense
  EXPTYPE Integer Expense Type
  LOCATION String*6 Location
  ICUOM String*10 I/C Unit of Measure
  CONVERSION BCD*10.6
  STOCKITEM Boolean Stock Item
  COSTMETHOD Integer Cost Method
  UNFMTITEM String*24 Unformatted Item No.
  CHARGECODE String*16 Charge Code
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment

## PMCEDAO - Cost Entries Detail Audit Opt. (view PM0427)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO+OPTFIELD; OPTFIELD+POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCEDO - Cost Entries Detail Optional Field (view PM0423)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCEH - Cost Entries Header (view PM0420)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; DOCNUM; TRANSTAT+DOCNUM; COMPLETE+DOCNUM [M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*24 Document Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Total Cost
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  LABORSR BCD*10.3 Labor Amount
  LABORHM BCD*10.3 Labor Amount
  TOTCOSTSR BCD*10.3 Total Cost Amount
  TOTCOSTHM BCD*10.3 Total Cost Amount
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  TOTQTY BCD*10.5 Total Quantity
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  VALUES Long Optional Fields
  ICSTAT Integer I/C Stat
  NUMMC Long Number of Miscellaneous Costs
  NUMTC Long Number of Timecards
  NUMTE Long Number of Time Expenses
  NUMEQ Long Number of Equipment Usages
  NUMMU Long Number of Material Usages
  NUMMR Long Number of Material Returns
  NUMCH Long Number of Charges
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMCEHA - Cost Entries Audit (view PM0424)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; SEQ+POSTSEQNO; DOCNUM [D]; SEQ+TRANSDATE
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  POSTDATE Date Posting Date
  DOCNUM String*24 Document Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  REFERENCE String*60 Reference
  DESC String*60 Description
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Total Cost
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  TOTCOSTSR BCD*10.3 Total Cost Amount
  TOTCOSTHM BCD*10.3 Total Cost Amount
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  TOTQTY BCD*10.5 Total Quantity
  PRINTSTAT Boolean Printed
  TRANSTAT Integer Transaction Status
  VALUES Long Optional Fields
  ICSTAT Integer I/C Stat
  NUMMC Long Number of Miscellaneous Costs
  NUMTC Long Number of Timecards
  NUMTE Long Number of Time Expenses
  NUMEQ Long Number of Equipment Usages
  NUMMU Long Number of Material Usages
  NUMMR Long Number of Material Returns
  NUMCH Long Number of Charges
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  DATEBUS Date Posting Date

## PMCEHAO - Cost Entries Audit Optional Fld (view PM0425)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+OPTFIELD; OPTFIELD+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCEHO - Cost Entries Optional Field (view PM0421)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCHARG - Charge Codes (view PM0023)
Keys (first = PK; D=dups allowed, M=modifiable): CHARGECODE
Fields (NAME type description [values]):
  CHARGECODE String*16 Charge Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  DATEINACTV Date Date Inactive
  CHARGETYPE Integer Charge Type [1=Service,2=Fixed Amount]
  AMOUNT BCD*10.3 Billing Amount
  SCHCODE String*12 Schedule Code
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  VALUES Long Optional Fields

## PMCHARGD - Charge Codes Detail View (view PM0478)
Keys (first = PK; D=dups allowed, M=modifiable): CHARGECODE+CCY
Fields (NAME type description [values]):
  CHARGECODE String*16 Charge Code
  CCY String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMOUNT BCD*10.3 Billing Amount
  ARITEM String*16 AR Item
  UOM String*10 AR UOM
  DESC String*60 Currency Description

## PMCHARGO - Charges Optional Field (view PM0516)
Keys (first = PK; D=dups allowed, M=modifiable): CHARGECODE+OPTFIELD; OPTFIELD+CHARGECODE
Fields (NAME type description [values]):
  CHARGECODE String*16 Charge Code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCHGDA - Charges Audit Detail (view PM0057)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  CHRGNO String*16 Charge Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  CHARGECODE String*16 Charge Code
  DESC String*60 Description
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  QUANTITY BCD*10.5 Quantity
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  COMMENTS String*250 Comments
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  BILLRATE BCD*10.6 Billing Rate
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  BILLCCY String*3 Billing Currency
  DETAILNUM Long Detail Number
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  UNITCOST BCD*10.6
  COSTCCY String*3
  EXTCOSTHM BCD*10.3
  TOTCOSTHM BCD*10.3
  TRANACCT String*45
  WIPACCT String*45

## PMCHGDAO - Charges Audit Detail Opt. Field (view PM0525)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO+OPTFIELD; OPTFIELD+POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCHGDO - Charges Detail Optional Field (view PM0523)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCHGHA - Charges Audit (view PM0056)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; SEQ+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  POSTDATE Date Posting Date
  CHRGNO String*16 Charge Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  TOTQTY BCD*10.5 Total Quantity
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  PRINTSTAT Boolean
  EXTCOSTHM BCD*10.3
  TOTCOSTHM BCD*10.3
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  DATEBUS Date

## PMCHGHAO - Charges Audit Optional Field (view PM0526)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+OPTFIELD; OPTFIELD+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCHGHO - Charges Optional Field (view PM0524)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCHNDA - Revise Estimates Audit Detail (view PM0061)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  CHNGORDNO String*16 Revise Estimate Number
  DETAILNUM Long Detail Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  COSTTYPE Integer Cost Type
  TYPE Integer Type
  ACTION Integer Action
  CBILLTYPE Integer Billing Type
  RBILLTYPE Integer Billing Type
  COSTCCY String*3 Cost Currency
  BILLCCY String*3 Billing Currency
  CDESC String*60 Description
  RDESC String*60 Description
  CARITEM String*16 A/R Item No.
  RARITEM String*16 A/R Item No.
  CARUOM String*10 A/R Unit of Measure
  RARUOM String*10 A/R Unit of Measure
  CICUOM String*10 ^7
  RICUOM String*10 ^7
  CCONV BCD*10.6
  RCONV BCD*10.6
  CQUANTITY BCD*10.5 Quantity
  RQUANTITY BCD*10.5 Quantity
  CUNITCOST BCD*10.6 Unit Cost
  RUNITCOST BCD*10.6 Unit Cost
  CEXTCOSTSR BCD*10.3 Extended Cost
  REXTCOSTSR BCD*10.3 Extended Cost
  CEXTCOSTHM BCD*10.3 Extended Cost
  REXTCOSTHM BCD*10.3 Extended Cost
  CLABORTYPE Integer Labor Type
  RLABORTYPE Integer Labor Type
  CLABORRATE BCD*10.6 Labor Rate
  RLABORRATE BCD*10.6 Labor Rate
  CLABORPER BCD*5.5 Labor Percentage
  RLABORPER BCD*5.5 Labor Percentage
  CLABORAMT BCD*10.3 Labor Amount
  RLABORAMT BCD*10.3 Labor Amount
  COHTYPE Integer Overhead Type
  ROHTYPE Integer Overhead Type
  COHRATE BCD*10.6 Overhead Rate
  ROHRATE BCD*10.6 Overhead Rate
  COHPER BCD*5.5 Overhead Percentage
  ROHPER BCD*5.5 Overhead Percentage
  COHAMT BCD*10.3 Overhead Amount
  ROHAMT BCD*10.3 Overhead Amount
  CTOTCOSTSR BCD*10.3 Total Cost
  RTOTCOSTSR BCD*10.3 Total Cost
  CTOTCOSTHM BCD*10.3 Total Cost
  RTOTCOSTHM BCD*10.3 Total Cost
  CCOSTPLUSP BCD*5.5 Cost Plus Percentage
  RCOSTPLUSP BCD*5.5 Cost Plus Percentage
  CBILLRATE BCD*10.6 Billing Rate
  RBILLRATE BCD*10.6 Billing Rate
  CEXTBILLSR BCD*10.3 Extended Billing Amount
  REXTBILLSR BCD*10.3 Extended Billing Amount
  CEXTBILLHM BCD*10.3 Extended Billing Amount
  REXTBILLHM BCD*10.3 Extended Billing Amount
  CFPAMTSR BCD*10.3 Fixed Price Amount
  RFPAMTSR BCD*10.3 Fixed Price Amount
  CFPAMTHM BCD*10.3 Fixed Price Amount
  RFPAMTHM BCD*10.3 Fixed Price Amount
  CPROFITSR BCD*10.3 Profit
  RPROFITSR BCD*10.3 Profit
  CPROFITHM BCD*10.3 Profit
  RPROFITHM BCD*10.3 Profit
  CRATETYPE String*2 Rate Type
  CRATEDATE Date Rate Date
  CRATEOP Integer Rate Op
  CRATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operation
  RATE BCD*8.7 Rate
  RATESPREAD BCD*8.7 Rate Spread
  COMMENTS String*250 Comment
  CONTSTYLE Integer ^1 Style
  PROJTYPE Integer ^2 Type
  REVREC Integer Accounting Method
  CUSTOMER String*12 Customer
  INVTYPE Integer Invoice Type
  VALUES Long

## PMCHNGD - Revise Estimates Detail (view PM0059)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; CHNGORDNO+LINENO; SEQ+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CHNGORDNO String*16 Revise Estimate Number
  DETAILNUM Long Detail Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  COSTTYPE Integer Cost Type [0=None,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  TYPE Integer Type [0=None,1=Project,2=Category,3=Resource Category]
  ACTION Integer Action [1=Add New,2=Modify Existing]
  CBILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  RBILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  COSTCCY String*3 Cost Currency
  BILLCCY String*3 Billing Currency
  CDESC String*60 Description
  RDESC String*60 Description
  CARITEM String*16 A/R Item No.
  RARITEM String*16 A/R Item No.
  CARUOM String*10 A/R Unit of Measure
  RARUOM String*10 A/R Unit of Measure
  CICUOM String*10 ^7
  RICUOM String*10 ^7
  CCONV BCD*10.6
  RCONV BCD*10.6
  CQUANTITY BCD*10.5 Quantity
  RQUANTITY BCD*10.5 Quantity
  CUNITCOST BCD*10.6 Unit Cost
  RUNITCOST BCD*10.6 Unit Cost
  CEXTCOSTSR BCD*10.3 Extended Cost
  REXTCOSTSR BCD*10.3 Extended Cost
  CEXTCOSTHM BCD*10.3 Extended Cost
  REXTCOSTHM BCD*10.3 Extended Cost
  CLABORTYPE Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  RLABORTYPE Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  CLABORRATE BCD*10.6 Labor Rate
  RLABORRATE BCD*10.6 Labor Rate
  CLABORPER BCD*5.5 Labor Percentage
  RLABORPER BCD*5.5 Labor Percentage
  CLABORAMT BCD*10.3 Labor Amount
  RLABORAMT BCD*10.3 Labor Amount
  COHTYPE Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  ROHTYPE Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  COHRATE BCD*10.6 Overhead Rate
  ROHRATE BCD*10.6 Overhead Rate
  COHPER BCD*5.5 Overhead Percentage
  ROHPER BCD*5.5 Overhead Percentage
  COHAMT BCD*10.3 Overhead Amount
  ROHAMT BCD*10.3 Overhead Amount
  CTOTCOSTSR BCD*10.3 Total Cost
  RTOTCOSTSR BCD*10.3 Total Cost
  CTOTCOSTHM BCD*10.3 Total Cost
  RTOTCOSTHM BCD*10.3 Total Cost
  CCOSTPLUSP BCD*5.5 Cost Plus Percentage
  RCOSTPLUSP BCD*5.5 Cost Plus Percentage
  CBILLRATE BCD*10.6 Billing Rate
  RBILLRATE BCD*10.6 Billing Rate
  CEXTBILLSR BCD*10.3 Extended Billing Amount
  REXTBILLSR BCD*10.3 Extended Billing Amount
  CEXTBILLHM BCD*10.3 Extended Billing Amount
  REXTBILLHM BCD*10.3 Extended Billing Amount
  CFPAMTSR BCD*10.3 Fixed Price Amount
  RFPAMTSR BCD*10.3 Fixed Price Amount
  CFPAMTHM BCD*10.3 Fixed Price Amount
  RFPAMTHM BCD*10.3 Fixed Price Amount
  CPROFITSR BCD*10.3 Profit
  RPROFITSR BCD*10.3 Profit
  CPROFITHM BCD*10.3 Profit
  RPROFITHM BCD*10.3 Profit
  CRATETYPE String*2 Rate Type
  CRATEDATE Date Rate Date
  CRATEOP Integer Rate Op [1=Multiply,2=Divide]
  CRATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operation [1=Multiply,2=Divide]
  RATE BCD*8.7 Rate
  RATESPREAD BCD*8.7 Rate Spread
  COMMENTS String*250 Comment
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  CUSTOMER String*12 Customer
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long

## PMCHNGH - Revise Estimates (view PM0058)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; CHNGORDNO; COMPLETE+CHNGORDNO [M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CHNGORDNO String*16 Revise Estimate Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  CTOTQTY BCD*10.5 Total Quantity
  RTOTQTY BCD*10.5 Total Quantity
  CEXTCOSTSR BCD*10.3 Current Extended Cost
  REXTCOSTSR BCD*10.3 Revised Extended Cost
  CEXTCOSTHM BCD*10.3 Current Extended Cost
  REXTCOSTHM BCD*10.3 Revised Extended Cost
  CTOTCOSTSR BCD*10.3 Total Cost Estimate Amount
  RTOTCOSTSR BCD*10.3 Total Cost Estimate Amount
  CTOTCOSTHM BCD*10.3 Total Cost Estimate Amount
  RTOTCOSTHM BCD*10.3 Total Cost Estimate Amount
  CTOTBILLSR BCD*10.3 Total Billing Estimate Amount
  RTOTBILLSR BCD*10.3 Total Billing Estimate Amount
  CTOTBILLHM BCD*10.3 Total Billing Estimate Amount
  RTOTBILLHM BCD*10.3 Total Billing Estimate Amount
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMCHNHA - Revise Estimates Audit (view PM0060)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; SEQ+POSTSEQNO; CHNGORDNO [D]; SEQ+TRANSDATE
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  POSTDATE Date Posting Date
  CHNGORDNO String*16 Revise Estimate Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  REFERENCE String*60 Reference
  DESC String*60 Description
  CTOTQTY BCD*10.5 Total Quantity
  RTOTQTY BCD*10.5 Total Quantity
  CEXTCOSTSR BCD*10.3 Current Extended Cost
  REXTCOSTSR BCD*10.3 Revised Extended Cost
  CEXTCOSTHM BCD*10.3 Current Extended Cost
  REXTCOSTHM BCD*10.3 Revised Extended Cost
  CTOTCOSTSR BCD*10.3 Total Cost Estimate Amount
  RTOTCOSTSR BCD*10.3 Total Cost Estimate Amount
  CTOTCOSTHM BCD*10.3 Total Cost Estimate Amount
  RTOTCOSTHM BCD*10.3 Total Cost Estimate Amount
  CTOTBILLSR BCD*10.3 Total Billing Estimate Amount
  RTOTBILLSR BCD*10.3 Total Billing Estimate Amount
  CTOTBILLHM BCD*10.3 Total Billing Estimate Amount
  RTOTBILLHM BCD*10.3 Total Billing Estimate Amount
  COMPLETE Integer Status
  PRINTSTAT Boolean Printed
  TRANSTAT Integer Transaction Status
  NUMDTL Long Number of Details
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  DATEBUS Date Posting Date

## PMCHRGD - Charges Detail (view PM0055)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; CHRGNO+LINENO; SEQ+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CHRGNO String*16 Charge Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 Unformatted ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  CHARGECODE String*16 Charge Code
  DESC String*60 Description
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  QUANTITY BCD*10.5 Quantity
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  COMMENTS String*250 Comments
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  BILLRATE BCD*10.6 Billing Amount
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  BILLCCY String*3 Billing Currency
  DETAILNUM Long Detail Number
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields

## PMCHRGH - Charges (view PM0054)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; CHRGNO; TRANSTAT+CHRGNO; COMPLETE+CHRGNO [M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CHRGNO String*16 Charge Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  TOTQTY BCD*10.5 Total Quantity
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMCLOSE - G/L Closing Entries (view PM0209)
Keys (first = PK; D=dups allowed, M=modifiable): FMTCONTNO+PROJECT+CATEGORY+LINENUM
Fields (NAME type description [values]):
  FMTCONTNO String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  LINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACCT String*45 Account
  AMTSR BCD*10.3 Amount
  AMTHM BCD*10.3 Amount
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator
  CCY String*3 Currency
  TYPE Integer Description

## PMCOCA - Committed Costs Audit (view PM0320)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; CONTRACT+PROJECT+CATEGORY+TRANSDATE [D]; CONTRACT+PROJECT+CATEGORY+VENDORID+TRANSDATE [D]; CONTRACT+PROJECT+CATEGORY+MODULE+TRANSDATE [D]
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  RSCNAME String*60 Resource Name
  TRANSNUM Long Transaction Number
  MODULE String*4 Module
  SRCPOCOCA Integer
  TRANSDATE Date Transaction Date
  TRANSTYPE Integer Transaction Type
  DOCTYPE Integer Document Type
  DOCNUM String*24 Document Number
  APCNTBTCH BCD*5.0 Batch Number
  APCNTENT BCD*4.0 Batch Entry Number
  APCNTLINE BCD*3.0 Batch Line Number
  VENDORID String*12 Vendor ID
  VENDORNAME String*60 Vendor Name
  PODAYENDSQ Long Day End Sequence
  POSEQNO BCD*10.0 Sequence Key
  POLINENO BCD*10.0 Line Number
  QUANTITY BCD*10.5 Committed Quantity
  OHHM BCD*10.3 Committed OverHead
  LABORHM BCD*10.3 Committed Labor
  TXALLCOMHM BCD*10.3 Committed Allocated Tax
  TXEXPCOMHM BCD*10.3 Committed Expensed Tax
  COSTHM BCD*10.3 Committed Cost
  TCOSTHM BCD*10.3 Total Committed Cost
  DRILLSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link
  DRILLAPP String*2 Drill Down Application
  ICUOM String*10 I/C Unit of Measure
  CONVERSION BCD*10.6 Conversion

## PMCONO - Contract Optional Field (view PM0850)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+OPTFIELD; OPTFIELD+CTUNIQ; CONTRACT+OPTFIELD
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 Contract Uniq
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  CONTRACT String*16 Contract
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCONTS - ^4 (view PM0021)
Physical tables of this view: PMCONTS, PMCONTT (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ; CONTRACT; CUSTOMER+CONTRACT [M]; FMTCONTNO
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 ^1 Uniq
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 Unformatted ^1
  DESC String*60 Description
  DATELASTMN Date Last Maintained
  CONTBRKID String*6 Structure Code
  FMTCONTNO String*16 ^1
  CUSTOMER String*12 Customer Number
  MANAGER String*16 ^1 Manager
  PONUMBER String*22 P/O Number
  CONTACT String*60 Contact
  PHONE String*30 Telephone
  FAX String*30 Fax
  STARTDATE Date Start Date
  ORJENDDATE Date Original End Date
  CURENDDATE Date Projected End Date
  CLOSEDDATE Date Closed Date
  COMMENT String*250 Comment
  USERR Boolean Use ^1 Revenue Recognition Information
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  USEOVERH Boolean Use the ^1 Overhead Information
  OVERHEAD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  USELABOR Boolean Use the ^1 Labor Information
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  STATUS Integer ^1 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  USECOSTP Boolean Use the ^1 Cost Plus Percentage
  COSTPLUSP BCD*5.5 Cost Plus Percentage
  USEPTYPE Integer ^2 Type
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CHANGEORD Integer Number of Change Orders to the ^1
  NXTCHGORD Long Next Change Order Number
  IDACCTSET String*6 Account Set
  TEMPLAT String*16 Template
  USEBILL Boolean Use the ^1 Billing Type
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  SCHCODE String*12 Schedule
  USERETAIN Boolean Use the ^1 Retainage Information
  PERRETREC BCD*5.5 A/R Retainage Percentage
  RETRECD Integer A/R Retention Period
  PERRETPAID BCD*5.5 Reserved
  RETPAIDD Integer Reserved
  SEGMENT1 String*16 Segment 1
  SEGMENT2 String*16 Segment 2
  SEGMENT3 String*16 Segment 3
  SEGMENT4 String*16 Segment 4
  SEGMENT5 String*16 Segment 5
  CONSOLINV Boolean Consolidate ^5 onto the One Invoice
  FORMCODE String*6 Form Code
  NEXTNUM Long Next Detail Number
  NUMDETAILS Long Number of Details
  ESTBILLCCY Integer Revenue And Cost Currency [1=Revenue and Costs in Functional Currency,2=Revenue in Customer Currency,3=Revenue and Costs in Customer Currency]
  CUSTCCY String*3 Customer Currency
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  ORJTIMECSR BCD*10.3 Number of non percent projects
  ORJTIMECHM BCD*10.3 Orig. Labor Cost Est.
  CURTIMECSR BCD*10.3 Reserved
  CURTIMECHM BCD*10.3 Cur. Labor Cost Est.
  ACTTIMECSR BCD*10.3 Reserved
  ACTTIMECHM BCD*10.3 Actual Labor Costs
  RECTIMECSR BCD*10.3 Reserved
  RECTIMECHM BCD*10.3 Reserved
  ORJTIMEBSR BCD*10.3 Orig. Labor Billing Est.
  ORJTIMEBHM BCD*10.3 Orig. Labor Billing Est.
  CURTIMEBSR BCD*10.3 Cur. Labor Billing Est.
  CURTIMEBHM BCD*10.3 Cur. Labor Billing Est.
  ACTTIMEBSR BCD*10.3 Actual Labor Billings
  ACTTIMEBHM BCD*10.3 Actual Labor Billings
  RECTIMEBSR BCD*10.3 Reserved
  RECTIMEBHM BCD*10.3 Reserved
  ORJTIMEQTY BCD*10.5 Orig. Labor Qty Est.
  CURTIMEQTY BCD*10.5 Cur. Labor Qty Est.
  ACTTIMEQTY BCD*10.5 Actual Labor Qty
  PERTIMEQTY BCD*5.5 Labor Percentage Complete
  ORJMATECSR BCD*10.3 Reserved
  ORJMATECHM BCD*10.3 Orig. Material Estimated Cost
  CURMATECSR BCD*10.3 Reserved
  CURMATECHM BCD*10.3 Current Material Estimated Cost
  ACTMATECSR BCD*10.3 Reserved
  ACTMATECHM BCD*10.3 Actual Material Cost
  RECMATECSR BCD*10.3 Reserved
  RECMATECHM BCD*10.3 Reserved
  ORJMATEBSR BCD*10.3 Orig. Material Billing Est.
  ORJMATEBHM BCD*10.3 Orig. Material Billing Est.
  CURMATEBSR BCD*10.3 Cur. Material Billing Est.
  CURMATEBHM BCD*10.3 Cur. Material Billing Est.
  ACTMATEBSR BCD*10.3 Actual Material Amount Billed
  ACTMATEBHM BCD*10.3 Actual Material Amount Billed
  RECMATEBSR BCD*10.3 Reserved
  RECMATEBHM BCD*10.3 Reserved
  ORJMATEQTY BCD*10.5 Orig. Material Qty Est.
  CURMATEQTY BCD*10.5 Cur. Material Est.
  ACTMATEQTY BCD*10.5 Actual Material Qty
  ORJEQUICSR BCD*10.3 Reserved
  ORJEQUICHM BCD*10.3 Orig. Estimated Equipment Cost
  CUREQUICSR BCD*10.3 Reserved
  CUREQUICHM BCD*10.3 Cur. Estimated Equipment Cost
  ACTEQUICSR BCD*10.3 Reserved
  ACTEQUICHM BCD*10.3 Actual Equipment Cost
  RECEQUICSR BCD*10.3 Reserved
  RECEQUICHM BCD*10.3 Reserved
  ORJEQUIBSR BCD*10.3 Orig. Equipment Billing Est.
  ORJEQUIBHM BCD*10.3 Orig. Equipment Billing Est.
  CUREQUIBSR BCD*10.3 Cur. Equipment Billing Est.
  CUREQUIBHM BCD*10.3 Cur. Equipment Billing Est.
  ACTEQUIBSR BCD*10.3 Actual Equipment Amount Billed
  ACTEQUIBHM BCD*10.3 Actual Equipment Amount Billed
  RECEQUIBSR BCD*10.3 Reserved
  RECEQUIBHM BCD*10.3 Reserved
  ORJEQUIQTY BCD*10.5 Orig. Equipment Qty Est.
  CUREQUIQTY BCD*10.5 Cur. Equipment Est.
  ACTEQUIQTY BCD*10.5 Actual Equipment Qty

## PMCONTT - ^4 (view PM0021)
Physical tables of this view: PMCONTS, PMCONTT (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 ^1 Uniq
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORJSUBCCSR BCD*10.3 Reserved
  ORJSUBCCHM BCD*10.3 Orig. Subcontractor Est. Cost
  CURSUBCCSR BCD*10.3 Reserved
  CURSUBCCHM BCD*10.3 Cur. Subcontractor Est. Cost
  ACTSUBCCSR BCD*10.3 Reserved
  ACTSUBCCHM BCD*10.3 Actual Subcontractor Cost
  RECSUBCCSR BCD*10.3 Reserved
  RECSUBCCHM BCD*10.3 Reserved
  ORJSUBCBSR BCD*10.3 Orig. Subcontract Billing Est.
  ORJSUBCBHM BCD*10.3 Orig. Subcontract Billing Est.
  CURSUBCBSR BCD*10.3 Cur. Subcontract Billing Est.
  CURSUBCBHM BCD*10.3 Cur. Subcontract Billing Est.
  ACTSUBCBSR BCD*10.3 Actual Subcontract Amt Billed
  ACTSUBCBHM BCD*10.3 Actual Subcontract Amt Billed
  RECSUBCBSR BCD*10.3 Reserved
  RECSUBCBHM BCD*10.3 Reserved
  ORJSUBCQTY BCD*10.5 Orig. Subcontractor Qty Est.
  CURSUBCQTY BCD*10.5 Cur. Subcontractor Est.
  ACTSUBCQTY BCD*10.5 Actual Subcontractor Qty
  ORJOHEXCSR BCD*10.3 Reserved
  ORJOHEXCHM BCD*10.3 Orig. Est Overhead Expense Cost
  CUROHEXCSR BCD*10.3 Reserved
  CUROHEXCHM BCD*10.3 Cur. Est. Overhead Expense Cost
  ACTOHEXCSR BCD*10.3 Reserved
  ACTOHEXCHM BCD*10.3 Actual Overhead Expense Cost
  RECOHEXCSR BCD*10.3 Reserved
  RECOHEXCHM BCD*10.3 Reserved
  ORJOHEXBSR BCD*10.3 Orig. Overhead Billing Est.
  ORJOHEXBHM BCD*10.3 Orig. Overhead Billing Est.
  CUROHEXBSR BCD*10.3 Cur. Overhead Billing Est.
  CUROHEXBHM BCD*10.3 Cur. Overhead Billing Est.
  ACTOHEXBSR BCD*10.3 Actual Overhead Amount Billed
  ACTOHEXBHM BCD*10.3 Actual Overhead Billing Est.
  RECOHEXBSR BCD*10.3 Reserved
  RECOHEXBHM BCD*10.3 Reserved
  ORJOHEXQTY BCD*10.5 Orig. Overhead Qty Est.
  CUROHEXQTY BCD*10.5 Cur. Overhead Est.
  ACTOHEXQTY BCD*10.5 Actual Overhead Qty
  ORJMISCCSR BCD*10.3 Reserved
  ORJMISCCHM BCD*10.3 Orig. Est. Miscellaneous Cost
  CURMISCCSR BCD*10.3 Reserved
  CURMISCCHM BCD*10.3 Cur. Est. Miscellaneous Cost
  ACTMISCCSR BCD*10.3 Reserved
  ACTMISCCHM BCD*10.3 Actual Miscellaneous Cost
  RECMISCCSR BCD*10.3 Reserved
  RECMISCCHM BCD*10.3 Reserved
  ORJMISCBSR BCD*10.3 Orig. Miscellaneous Billing Est
  ORJMISCBHM BCD*10.3 Orig. Miscellaneous Billing Est
  CURMISCBSR BCD*10.3 Cur. Miscellaneous Billing Est.
  CURMISCBHM BCD*10.3 Cur. Miscellaneous Billing Est.
  ACTMISCBSR BCD*10.3 Actual Miscellaneous Amt Billed
  ACTMISCBHM BCD*10.3 Actual Miscellaneous Amt Billed
  RECMISCBSR BCD*10.3 Reserved
  RECMISCBHM BCD*10.3 Reserved
  ORJMISCQTY BCD*10.5 Orig. Miscellaneous Qty Est.
  CURMISCQTY BCD*10.5 Cur. Miscellaneous Est.
  ACTMISCQTY BCD*10.5 Actual Miscellaneous Qty
  ORJOHEADSR BCD*10.3 Reserved
  ORJOHEADHM BCD*10.3 Original Overhead Estimate
  CUROHEADSR BCD*10.3 Reserved
  CUROHEADHM BCD*10.3 Current Overhead Estimate
  ACTOHEADSR BCD*10.3 Reserved
  ACTOHEADHM BCD*10.3 Actual Overhead
  ORJLABSR BCD*10.3 Original Labor Amount Estimate
  ORJLABHM BCD*10.3 Original Labor Amount Estimate
  CURLABSR BCD*10.3 Current Labor Amount Estimate
  CURLABHM BCD*10.3 Current Labor Amount Estimate
  ACTLABSR BCD*10.3 Actual Labor Amount
  ACTLABHM BCD*10.3 Actual Labor Amount
  ORJCHRGSR BCD*10.3 Reserved
  ORJCHRGHM BCD*10.3 Reserved
  CURCHRGSR BCD*10.3 Reserved
  CURCHRGHM BCD*10.3 Reserved
  ACTCHRGSR BCD*10.3 Actual Charge Amount Billed
  ACTCHRGHM BCD*10.3 Actual Charge Amount Billed
  ACTCHRGDSR BCD*10.3 Act Chrg Amt Billed & Deferred
  ACTCHRGDHM BCD*10.3 Act Chrg Amt Billed & Deferred
  RECCHRGSR BCD*10.3 Reserved
  RECCHRGHM BCD*10.3 Reserved
  ACTSTKRESR BCD*10.3 Reserved
  ACTSTKREHM BCD*10.3 Act Cost Stock Ret to Inventory
  ACTSTKRQTY BCD*10.5 Act Qty Stock Ret to Inventory
  TARRECTSSR BCD*10.3 Total A/R Customer Receipts
  TARRECTSHM BCD*10.3 Total A/R Customer Receipts
  TAPPAYMTS BCD*10.3 Total A/P Vendor Payments
  TORJCOSTSR BCD*10.3 Reserved
  TORJCOSTHM BCD*10.3 Total Orig. Cost Est.
  TCURCOSTSR BCD*10.3 Reserved
  TCURCOSTHM BCD*10.3 Total Cur. Cost Est.
  TACTCOSTSR BCD*10.3 Reserved
  TACTCOSTHM BCD*10.3 Total Actual Cost
  TRECCOSTSR BCD*10.3 Reserved
  TRECCOSTHM BCD*10.3 Total Cost Recognized
  PERTCOST BCD*5.5 Percent Total Cost
  TORJREVSR BCD*10.3 Total Orig. Revenue Est.
  TORJREVHM BCD*10.3 Total Orig. Revenue Est.
  TCURREVSR BCD*10.3 Total Cur. Revenue Est.
  TCURREVHM BCD*10.3 Total Cur. Revenue Est.
  TACTREVSR BCD*10.3 Total Actual Revenue
  TACTREVHM BCD*10.3 Total Actual Revenue Est.
  TRECREVSR BCD*10.3 Total Revenue Recognized
  TRECREVHM BCD*10.3 Total Revenue Recognized
  RETARAMTSR BCD*10.3 Retainage Receivable
  RETARAMTHM BCD*10.3 Retainage Receivable
  RETARRECSR BCD*10.3 Retainage Amount Received in A/R
  RETARRECHM BCD*10.3 Retainage Amount Received in A/R
  RETAPAMT BCD*10.3 Retainage Payable
  RETAPPAID BCD*10.3 Retainage Amount Paid in A/P
  POAMOUNTSR BCD*10.3 Reserved
  POAMOUNTHM BCD*10.3 Reserved
  POQTY BCD*10.5 Reserved
  OEAMOUNTSR BCD*10.3 Reserved
  OEAMOUNTHM BCD*10.3 Recognized Loss
  OEQTY BCD*10.5 Reserved
  PCOMLETERR BCD*5.5 Recognized % Complete
  FPAMOUNTSR BCD*10.3 ^2 Amount
  FPAMOUNTHM BCD*10.3 ^2 Amount
  LSTBILLPER BCD*5.5 Last Billings Percent Complete
  BILLAMTSR BCD*10.3 Amt Bill Fixed Price ^1
  BILLAMTHM BCD*10.3 Amt Bill Fixed Price ^1
  COSTDATE Date Last Cost Posting Date
  BILLDATE Date Last Billings Posting Date
  OHDATE Date Last Overhead Posting Date
  CHARGEDATE Date Last Charge Posting Date
  REVRECDATE Date Last Rev. Recognition Posting Date
  ARRECDATE Date Last A/R Receipt Posting Date
  APPAYDATE Date Last A/P Payment Posting Date
  TIMEDATE Date Last Timecard Posting Date
  STKTRDATE Date Last Material Usage Posting Date
  STKRETDATE Date Last Material Return Posting Date
  EQUIPDATE Date Last Equipment Posting Date
  PODATE Date Last Purchase Order Date
  PORECDATE Date Last P/O Receipt Date
  PORETDATE Date Last P/O Return Date
  OEORDDATE Date Last O/E Order Date
  OEINVDATE Date Last O/E Invoice Date
  FUNCRND BCD*10.3 Functional Rounding Amount
  NEXTTRAN Long Next Transaction Number
  OPENPROJ Long Number of open ^5
  OPENED Boolean ^1 Has Been Opened [0=No,1=Yes]
  BILLAMT BCD*10.3 Expected Billings
  PCOMPLETEB BCD*5.5 Billings Percent Complete
  LSTRRPER BCD*5.5 Last Rev. Recognition Percentage
  PRFTLOSSSR BCD*10.3 Recognized Profit / Loss
  PRFTLOSSHM BCD*10.3 Recognized Profit / Loss
  REVESTDATE Date Last Revised Posting Date
  CDATEFROM Date Current Start Date
  PLCODE String*16 Reserved
  RRMETHOD Integer Percentage Complete Method [1=Clear Billings and WIP During Revenue Recognition,0=Clear Billings and WIP During Project Close,2=From Options]
  NUMPROJECT Long Number of Projects
  POCOSTHM BCD*10.3 Committed P/O Cost
  POOHHM BCD*10.3 Committed P/O Overhead
  POLABORHM BCD*10.3 Committed P/O Labor
  POTCOSTHM BCD*10.3 Committed P/O Total Cost
  VALUES Long Optional Fields
  CUSCONTACT String*60 Contact
  CTACTITTLE String*60 Position
  CTACPHONE String*30 Phone
  OTHERPHONE String*30 Other Phone
  CTACFAX String*30 Fax
  CTACEMAIL String*60 E-mail
  USETAXGRP Boolean Tax Group
  CODETAXGRP String*12 Tax Group
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TAUTH1 String*12 Customer Tax Authority 1
  TAUTH2 String*12 Customer Tax Authority 2
  TAUTH3 String*12 Customer Tax Authority 3
  TAUTH4 String*12 Customer Tax Authority 4
  TAUTH5 String*12 Customer Tax Authority 5
  STRDCOSTHM BCD*10.3 Stored Cost
  STRDBILLSR BCD*10.3 Stored Billable Amount
  STRDOHHM BCD*10.3 Overhead Amount
  STRDTCSTHM BCD*10.3 Total Stored Cost
  TXEXPCOMHM BCD*10.3 Tax (exp) Committed (func)
  TXALLCOMHM BCD*10.3 Tax (all) Committed (func)
  PREAIAPAY BCD*10.3 Previous Certificates for Payment
  PRESTORED BCD*10.3 G703 Column F from Last AIA Report
  PRERETAIN BCD*10.3 G703 Column I from Last AIA Report
  MULTICUST Integer Invoice to Multiple Customers
  CURVAR Integer Currency different from that on project?
  BONECUST Integer Allow Multiple Customers [1=Yes,0=No]
  ARACCTSET String*6 A/R Account Set

## PMCOST - Cost Types (view PM0001)
Keys (first = PK; D=dups allowed, M=modifiable): COSTTYPE
Fields (NAME type description [values]):
  COSTTYPE String*10 Cost Type Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  DATEINACTV Date Date Inactive
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]

## PMCP - Canadian Payroll Superview (view PM0450)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTBTCH BCD*5.0 Batch
  LINENO Integer Line Number
  CHECKNUM BCD*5.0 Check Number
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  JOURNLDATE Date G/L Journal Date
  TRANSDATE Date Transaction Date
  CURRENCY String*3 Currency
  EXCHRATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  EMPLOYEE String*24 Employee
  DOCTYPE Integer Document Type [1=System Check,2=Manual Check]
  TRANSTYPE Integer Transaction Type [1=Posted,2=Check Reversal]
  TRANSNUM Long PJC Transaction Number
  EARNINGS String*6 Earnings or Deduction Code
  QUANTITY BCD*10.5 Quantity
  HOURS BCD*4.3 Hours
  BASE BCD*10.3 Base
  UNITRATE BCD*9.5 Unit Rate
  PERCENT BCD*9.5 Percent
  EXTAMTHM BCD*10.3 Extended Amount (HM)
  EXTAMTSR BCD*10.3 Extended Amount (SR)
  BILLRATE BCD*10.6 Billing Rate
  BILLTYPE Integer Billing Type [0=None,2=Billable,3=No Charge,1=Non-billable]
  WIPACCT String*45 WIP Account
  TRANACCT String*45 Transaction Account
  OHACCT String*45 Overhead Account
  OHAMTSR BCD*10.3 Overhead Amount
  OHAMTHM BCD*10.3 Overhead Amount
  LABACCT String*45 Labor Account
  LABORSR BCD*10.3 Labor Amount
  LABORHM BCD*10.3 Labor Amount
  ARITEM String*16 A/R Item Number
  ARUOM String*10 A/R Unit of Measure
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  DRILLSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link
  DRILLAPP String*2 Drill Down Application
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  DIFF Integer Differential Record?
  EXPENSEREI Integer Exp. Reimbursement?
  RESOURCE String*24 Resource

## PMCPO - C/P Optional Field (view PM0452)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+OPTFIELD; OPTFIELD+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long None
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMCTG - Categories (view PM0018)
Keys (first = PK; D=dups allowed, M=modifiable): CATEGORY
Fields (NAME type description [values]):
  CATEGORY String*16 ^3
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  COSTTYPE String*10 Cost Type
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  DATEINACTV Date Date Inactive
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  PERRETPAID BCD*5.5 A/P Retainage Percentage
  RETPAIDD Integer A/P Retention Period
  SEGOVERRD Boolean Override G/L Account Segments
  SEGNUM1 String*6 Segment 1
  SEGVAL1 String*15 Segment Code 1
  SEGNUM2 String*6 Segment 2
  SEGVAL2 String*15 Segment Code 2
  SEGNUM3 String*6 Segment 3
  SEGVAL3 String*15 Segment Code 3
  SEGNUM4 String*6 Segment 4
  SEGVAL4 String*15 Segment Code 4
  SEGNUM5 String*6 Segment 5
  SEGVAL5 String*15 Segment Code 5
  SEGNUM6 String*6 Segment 6
  SEGVAL6 String*15 Segment Code 6
  SEGNUM7 String*6 Segment 7
  SEGVAL7 String*15 Segment Code 7
  SEGNUM8 String*6 Segment 8
  SEGVAL8 String*15 Segment Code 8
  SEGNUM9 String*6 Segment 9
  SEGVAL9 String*15 Segment Code 9
  PLCODE String*16 Reserved
  VALUES Long Optional Fields

## PMCTGD - Categories Detail View (view PM0475)
Keys (first = PK; D=dups allowed, M=modifiable): CATEGORY+CCY
Fields (NAME type description [values]):
  CATEGORY String*16 Category
  CCY String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ARITEM String*16 AR Item
  UOM String*10 AR UOM
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  DESC String*60 Currency Description

## PMCTGO - Category Optional Fields (view PM0510)
Keys (first = PK; D=dups allowed, M=modifiable): CATEGORY+OPTFIELD; OPTFIELD+CATEGORY
Fields (NAME type description [values]):
  CATEGORY String*16 Category
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMEQDAO - Equipment Audit Detail OF (view PM0508)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO+OPTFIELD; OPTFIELD+POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMEQDO - Equipment Detail Optional Field (view PM0506)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMEQHAO - Equipment Audit Optional Field (view PM0507)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+OPTFIELD; OPTFIELD+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMEQHO - Equipment Optional Field (view PM0505)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMEQIPD - Equipment Detail (view PM0031)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; EQUIPNO+LINENO; SEQ+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EQUIPNO String*16 Equipment Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Equipment Code
  DESC String*60 Description
  QUANTITY BCD*10.5 Quantity
  ARITEM String*16 A/R Item Number
  UOM String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  COSTCCY String*3 Cost Currency
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  COMMENTS String*250 Comments
  OHACCT String*45 Overhead Account
  EQUIPACCT String*45 Equipment Account
  WIPACCT String*45 WIP/COS Account
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  FIXEDBILL Integer Bill Amount Based On [1=Invoice This Amount,2=Invoice Based on Exchange Rate]
  ESTBILLCCY Integer Revenue And Cost Currency [1=Revenue and Costs in Functional Currency,2=Revenue in Customer Currency,3=Revenue and Costs in Customer Currency]
  BILLRATE BCD*10.6 Billing Rate
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  BILLCCY String*3 Billing Currency
  DETAILNUM Long Detail Number
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment

## PMEQIPH - Equipment (view PM0030)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; EQUIPNO; TRANSTAT+EQUIPNO; COMPLETE+EQUIPNO [M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EQUIPNO String*16 Equipment Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  EXTCOSTSR BCD*10.3 Total Cost
  EXTCOSTHM BCD*10.3 Total Cost
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  TOTQTY BCD*10.5 Total Quantity
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMEQMT - Equipment (view PM0025)
Keys (first = PK; D=dups allowed, M=modifiable): EQUIPMENT
Fields (NAME type description [values]):
  EQUIPMENT String*16 Equipment Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  DATEINACTV Date Date Inactive
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  VALUES Long Optional Fields

## PMEQMTD - Equipment Detail View (view PM0476)
Keys (first = PK; D=dups allowed, M=modifiable): EQUIPMENT+CCY
Fields (NAME type description [values]):
  EQUIPMENT String*16 Equipment
  CCY String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ARITEM String*16 AR Item
  UOM String*10 AR UOM
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  DESC String*60 Currency Description

## PMEQMTO - Equipment Optional Fields (view PM0512)
Keys (first = PK; D=dups allowed, M=modifiable): EQUIPMENT+OPTFIELD; OPTFIELD+EQUIPMENT
Fields (NAME type description [values]):
  EQUIPMENT String*16 Equipment
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMEQPDA - Equipment Audit Detail (view PM0033)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  EQUIPNO String*16 Equipment Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Equipment Code
  DESC String*60 Description
  QUANTITY BCD*10.5 Quantity
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  COSTCCY String*3 Cost Currency
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost
  OHACCT String*45 Overhead Account
  OVERHD Integer Overhead Type
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Transaction Overhead Amount
  OHHM BCD*10.3 Transaction Overhead Amount
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  COMMENTS String*250 Comments
  EQUIPACCT String*45 Equipment Account
  WIPACCT String*45 Work in Progress Account
  BILLTYPE Integer Billing Type
  FIXEDBILL Integer Bill Amount Based On
  ESTBILLCCY Integer Revenue And Cost Currency
  BILLRATE BCD*10.6 Billing Rate
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  BILLCCY String*3 Billing Currency
  DETAILNUM Long Detail Number
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  PROJTYPE Integer ^2 Type
  CONTSTYLE Integer ^1 Style
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method
  INVTYPE Integer Invoice Type
  VALUES Long Optional Fields
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment

## PMEQPHA - Equipment Audit (view PM0032)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; SEQ+POSTSEQNO; EQUIPNO [D]; SEQ+TRANSDATE
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  POSTDATE Date Posting Date
  EQUIPNO String*16 Equipment Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  REFERENCE String*60 Reference
  DESC String*60 Description
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  TOTQTY BCD*10.5 Total Quantity
  PRINTSTAT Boolean Printed
  TRANSTAT Integer Transaction Status
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  DATEBUS Date Posting Date

## PMGLIT - G/L Integration (view PM0600)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSTYPE+FLDTYPE
Fields (NAME type description [values]):
  TRANSTYPE Integer Transaction Type [1=Adjustments,2=Adjustments Detail,3=Costs,4=Costs Detail,5=Equipment Usage,6=Equipment Usage Detail,7=Reopen Closed Projects Worksheet,8=Reopen Closed Projects Worksheet Detail,9=Revenue Recognition,10=Revenue Recognition Detail,11=Timecard,12=Timecard Detail]
  FLDTYPE Integer G/L Transaction Field [1=G/L Entry Description,2=G/L Detail Reference,3=G/L Detail Description,4=G/L Detail Comment]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEPARATOR Integer Segment Separator [1=* Asterisk,2=- Hyphen,3=/ Forward slash,4=\ Back slash,5=. Period,6={ Left Parenthesis,7=} Right Parenthesis,8=# Number sign,9=  Space]
  SEGMENT1 Integer Segment 1 [1=Posting Sequence,2=Source Code,3=Description,4=Reference,5=Worksheet Number,6=Equipment Code,7=Equipment Usage Number,8=Revenue Recognition Number,9=Timecard Number,10=Employee Number,11=Adjustment Number,12=Contract Number,13=Contract Description,14=Contract Manager,15=Purchase Order Number,16=Project,17=Category,18=Resource,19=Comments,20=Adjustment Type,21=Document Number,22=Document Type,23=Project Type,24=Accounting Method,25=Project Description,26=Category Description,27=Resource Description,28=Cost Number,29=Equipment Code Description,26=Category Description,30=Employee Name]
  SEGMENT2 Integer Segment 2 [1=Posting Sequence,2=Source Code,3=Description,4=Reference,5=Worksheet Number,6=Equipment Code,7=Equipment Usage Number,8=Revenue Recognition Number,9=Timecard Number,10=Employee Number,11=Adjustment Number,12=Contract Number,13=Contract Description,14=Contract Manager,15=Purchase Order Number,16=Project,17=Category,18=Resource,19=Comments,20=Adjustment Type,21=Document Number,22=Document Type,23=Project Type,24=Accounting Method,25=Project Description,26=Category Description,27=Resource Description,28=Cost Number,29=Equipment Code Description,26=Category Description,30=Employee Name]
  SEGMENT3 Integer Segment 3 [1=Posting Sequence,2=Source Code,3=Description,4=Reference,5=Worksheet Number,6=Equipment Code,7=Equipment Usage Number,8=Revenue Recognition Number,9=Timecard Number,10=Employee Number,11=Adjustment Number,12=Contract Number,13=Contract Description,14=Contract Manager,15=Purchase Order Number,16=Project,17=Category,18=Resource,19=Comments,20=Adjustment Type,21=Document Number,22=Document Type,23=Project Type,24=Accounting Method,25=Project Description,26=Category Description,27=Resource Description,28=Cost Number,29=Equipment Code Description,26=Category Description,30=Employee Name]
  SEGMENT4 Integer Segment 4 [1=Posting Sequence,2=Source Code,3=Description,4=Reference,5=Worksheet Number,6=Equipment Code,7=Equipment Usage Number,8=Revenue Recognition Number,9=Timecard Number,10=Employee Number,11=Adjustment Number,12=Contract Number,13=Contract Description,14=Contract Manager,15=Purchase Order Number,16=Project,17=Category,18=Resource,19=Comments,20=Adjustment Type,21=Document Number,22=Document Type,23=Project Type,24=Accounting Method,25=Project Description,26=Category Description,27=Resource Description,28=Cost Number,29=Equipment Code Description,26=Category Description,30=Employee Name]
  SEGMENT5 Integer Segment 5 [1=Posting Sequence,2=Source Code,3=Description,4=Reference,5=Worksheet Number,6=Equipment Code,7=Equipment Usage Number,8=Revenue Recognition Number,9=Timecard Number,10=Employee Number,11=Adjustment Number,12=Contract Number,13=Contract Description,14=Contract Manager,15=Purchase Order Number,16=Project,17=Category,18=Resource,19=Comments,20=Adjustment Type,21=Document Number,22=Document Type,23=Project Type,24=Accounting Method,25=Project Description,26=Category Description,27=Resource Description,28=Cost Number,29=Equipment Code Description,26=Category Description,30=Employee Name]

## PMIC - IC Superview (view PM0304)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LINENO Integer Line Number
  DOCNUM String*22 Shipment Number
  HDRDESC String*60 Description
  TRANSDATE Date Ship Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  TRANSTYPE Integer Entry Type [1=Shipment,2=Return]
  CURRENCY String*3 Source Currency
  EXCHRATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATEOVRRD Boolean Rate Override
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  DETAILNUM Long Detail Number
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  QUANTITY BCD*10.5 Quantity
  UNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor
  PRICELIST String*6 Price List
  UNITPRICE BCD*10.6 Unit Price (Functional)
  SHIPPRICE BCD*10.3 Extended Price (Functional)
  UNITCOST BCD*10.6 Unit Cost (Functional)
  EXTCOST BCD*10.3 Extended Cost (Functional)
  OHAMT BCD*10.3 Overhead Amount
  OHACCT String*45 Overhead Account
  CVAMT BCD*10.3 Cost Variance Amount
  VALUES Long Optional Fields
  BINTERNAL Boolean
  DATEBUS Date

## PMICO - I/C Optional Field (view PM0541)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+OPTFIELD; OPTFIELD+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long None
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMMATD - Material Usage Detail (view PM0051)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; MATERIALNO+LINENO; MATERIALNO+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MATERIALNO String*16 Material Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Item Number
  DESC String*60 Description
  LOCATION String*6 Location
  QUANTITY BCD*10.5 Quantity
  UOM String*10 Item Unit of Measure
  CONVERSION BCD*10.6 Conversion
  UNITCOST BCD*10.6 Unit Cost
  ADJUNITCST BCD*10.5 Reserved
  ADJCOST BCD*10.5 Reserved
  COSTSEQNUM Long Reserved
  COSTDATE Date Reserved
  ADDCOST BCD*10.3 Additional Cost
  STOCKITEM Boolean Stock Item
  COSTMETHOD Integer Cost Method [1=Moving Average,2=FIFO,3=LIFO,4=Standard Cost,5=Most Recent Cost,6=User-specified,7=Serial,8=Lot]
  UNFMTITEM String*24 Item Number
  CHKBDLZERO Boolean Check Below Zero
  COSTCCY String*3 Cost Currency
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost
  COMMENTS String*250 Comments
  ICACCT String*45 I/C Account
  WIPACCT String*45 WIP/COS Account
  OHACCT String*45 Overhead Account
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  FIXEDBILL Integer Bill Amount Based On [1=Invoice This Amount,2=Invoice Based on Exchange Rate]
  ESTBILLCCY Integer Revenue And Cost Currency [1=Revenue and Costs in Functional Currency,2=Revenue in Customer Currency,3=Revenue and Costs in Customer Currency]
  BILLRATE BCD*10.6 Billing Rate
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  OVERHD Integer Overhead Type
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  BILLCCY String*3 Billing Currency
  DETAILNUM Long Detail Number
  ARITEM String*16 A/R Item Number
  ARUOM String*10 A/R Unit of Measure
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  FASDETAIL Boolean FAS Attached [0=No,1=Yes]
  FASDB String*32 Database
  FASCMP String*32 Company
  FASTMPL String*25 Template
  TEXTDESC String*80 Asset Description
  SEPQTY Boolean Seperate Quantities
  FASQTY BCD*10.5 Asset Quantity
  FASUOM String*10 Unit of Measure
  AMTHC BCD*10.3 Amount
  EMPLOYEENO String*60 Used By
  BINTERNAL Boolean Internal Usage
  CLOSESN Boolean Close SN
  PROID Long SN inter-communication ID
  POPUPSN Integer Popup SN
  POPUPLT Integer Popup LT
  CLOSELT Boolean Close LT
  LTSETID Long LT inter-communication ID
  FORCEPOPSN Boolean Force popup SN
  FORCEPOPLT Boolean Force popup LT
  GENICSEQ Boolean Generate IC Seq.
  PRICELIST String*6 Price List
  CUSTCCY String*3 Customer Currency
  SERIALQTY Long Number of Serials
  LOTQTY BCD*10.4 Number of Lots

## PMMATDL - Material Usage Detail Lot Numbers (view PM0484)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+LOTNUMF; LOTNUMF+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence Number
  LINENO Long Line Number
  LOTNUMF String*40 Formatted Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4

## PMMATDO - Material Usage Detail Opt. Field (view PM0537)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMMATDS - Material Usage Detail Serial Numbers (view PM0483)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+SERIALNUMF; SERIALNUMF+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence Number
  LINENO Long Line Number
  SERIALNUMF String*40 Formatted Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## PMMATH - Material Usage (view PM0050)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; MATERIALNO; ICSTAT+SEQ [D,M]; TRANSTAT+MATERIALNO; COMPLETE+MATERIALNO [M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MATERIALNO String*16 Material Usage Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  EXTCOSTSR BCD*10.3 Total Cost
  EXTCOSTHM BCD*10.3 Total Cost
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  TOTQTY BCD*10.5 Total Quantity
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  ADDCSTTYPE Integer Additional Cost Type
  ADDCOST BCD*10.3 Additional Cost
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  ICSTAT Integer I/C Status [1=not processed,2=ready to process,3=process complete]
  NUMDTL Long Number of Details
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  EMPLOYEENO String*60 Used By
  BINTERNAL Boolean Internal Usage [0=False,1=True]
  ICSEQ Long IC Shipment Sequence Number
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMMATHO - Material Usage Optional Field (view PM0538)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMMATRD - Material Returns Detail (view PM0047)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; MATERIALNO+LINENO; MATERIALNO+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MATERIALNO String*16 Material Return Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Item Number
  DESC String*60 Description
  LOCATION String*6 Location
  QUANTITY BCD*10.5 Quantity
  UOM String*10 Item Unit of Measure
  CONVERSION BCD*10.6 Conversion
  UNITCOST BCD*10.6 Unit Cost
  ADJUNITCST BCD*10.5
  ADJCOST BCD*10.5
  COSTSEQNUM Long
  COSTDATE Date
  ADDCOST BCD*10.3 Additional Cost
  STOCKITEM Boolean Stock Item
  COSTMETHOD Integer Cost Method
  UNFMTITEM String*24 Item Number
  CHKBDLZERO Boolean Check Below Zero
  COSTCCY String*3 Cost Currency
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost
  COMMENTS String*250 Comments
  ICACCT String*45 I/C Account
  WIPACCT String*45 WIP/COS Account
  OHACCT String*45 Overhead Account
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  FIXEDBILL Integer Bill Amount Based On [1=Invoice This Amount,2=Invoice Based on Exchange Rate]
  ESTBILLCCY Integer Revenue And Cost Currency [1=Moving Average,2=FIFO,3=LIFO,4=Standard Cost,5=Most Recent Cost,6=User-specified,7=Serial,8=Lot]
  BILLRATE BCD*10.6 Billing Rate
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  OVERHD Integer Overhead Type
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  BILLCCY String*3 Billing Currency
  DETAILNUM Long Detail Number
  ARITEM String*16 A/R Item No.
  ARUOM String*10 A/R Unit of Measure
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  CLOSESN Boolean Close SN
  PROID Long SN inter-communication ID
  POPUPSN Integer Popup SN
  POPUPLT Integer Popup LT
  CLOSELT Boolean Close LT
  LTSETID Long LT inter-communication ID
  FORCEPOPSN Boolean Force popup SN
  FORCEPOPLT Boolean Force popup LT
  GENICSEQ Boolean Generate IC Seq.
  PRICELIST String*6 Price List
  CUSTCCY String*3 Customer Currency
  SERIALQTY Long Number of Serials
  LOTQTY BCD*10.4 Number of Lots

## PMMATRDL - Material Return Detail Lot Numbers (view PM0486)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+LOTNUMF; LOTNUMF+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence Number
  LINENO Long Line Number
  LOTNUMF String*40 Formatted Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Transaction Quantity
  QTYSQ BCD*10.4

## PMMATRDO - Material Return Detail Opt. Fld (view PM0535)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMMATRDS - Material Return Detail Serial Number (view PM0485)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+SERIALNUMF; SERIALNUMF+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence Number
  LINENO Long Line Number
  SERIALNUMF String*40 Formatted Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## PMMATRH - Material Returns (view PM0046)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; MATERIALNO; TRANSTAT+MATERIALNO; COMPLETE+MATERIALNO [M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MATERIALNO String*16 Material Return Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  EXTCOSTSR BCD*10.3 Total Cost
  EXTCOSTHM BCD*10.3 Total Cost
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  TOTQTY BCD*10.5 Total Quantity
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  ADDCSTTYPE Integer Additional cost type
  ADDCOST BCD*10.3 Additional Cost
  NUMDETAILS Integer Number of Detail Lines
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  MATNO String*16 Material Usage Number
  ICSTAT Integer [1=not processed,2=ready to process,3=process complete]
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  ICSEQ Long IC Shipment Sequence Number
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMMATRHO - Material Return Optional Field (view PM0536)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMMIEXP - Miscellaneous Expenses (view PM0028)
Keys (first = PK; D=dups allowed, M=modifiable): MISCCODE
Fields (NAME type description [values]):
  MISCCODE String*16 Miscellaneous Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  DATEINACTV Date Date Inactive
  VALUES Long Optional Fields
  UNITCOST BCD*10.6 Unit Cost

## PMMIEXPD - Misc. Expenses Detail View (view PM0480)
Keys (first = PK; D=dups allowed, M=modifiable): MISCCODE+CCY
Fields (NAME type description [values]):
  MISCCODE String*16 Miscellaneous Code
  CCY String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ARITEM String*16 AR Item
  UOM String*10 AR UOM
  BILLRATE BCD*10.6 Billing Rate
  DESC String*60 Currency Description

## PMMIEXPO - Miscellaneous Expenses Optional Fields (view PM0513)
Keys (first = PK; D=dups allowed, M=modifiable): MISCCODE+OPTFIELD; OPTFIELD+MISCCODE
Fields (NAME type description [values]):
  MISCCODE String*16 Miscellaneous Code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMMTAD - Material Allocation Detail (view PM0461)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; MALLOCNO+LINENO; MALLOCNO+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MALLOCNO String*16 Material Allocation Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Item Number
  DESC String*60 Description
  LOCATION String*6 Location
  COSTMETHOD Integer Cost Method
  STOCKITEM Boolean Stock Item
  UOM String*10 UOM
  UNFMTITEM String*24 Unformatted Item Number
  DETAILNUM Long Detail Number
  QUANTITY BCD*10.5 Allocated Quantity
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHR BCD*10.3 Billing Amount (Func)
  BILLCCY String*3 Billing Currency
  COSTCCY String*3 Cost Currency
  APERCENT BCD*5.5 Percentage Allocated
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Allocated Cost
  TOTCOSTSR BCD*10.3 Total Cost(Source)
  TOTCOSTHM BCD*10.3 Total Cost(Func.)
  OVERHD Integer Reserved
  OHEADRATE BCD*10.6 Reserved
  HEADPER BCD*5.5 Reserved
  OHSR BCD*10.3 Stored Overhead
  OHHM BCD*10.3 Overhead Allocated
  COMMENTS String*250 Comments
  CONTSTYLE Integer Style
  PROJTYPE Integer Project Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  STRDQTY BCD*10.5 Stored Quantity
  STRDCOSTHM BCD*10.3 Extended Stored Cost
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  CONVERSION BCD*10.6 Conversion
  STRDUOM String*10 UOM
  STRDCONVER BCD*10.6 Stored Conversion Factor

## PMMTADA - Material Allocation Detail (view PM0465)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; CONTRACT+PROJECT+CATEGORY+TRANSDATE [D]; CONTRACT+PROJECT+TRANSDATE [D]
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  MALLOCNO String*16 Material Allocation Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Item Number
  DESC String*60 Description
  LOCATION String*6 Location
  COSTMETHOD Integer
  UOM String*10 Item Unit of Measure
  UNFMTITEM String*24
  DETAILNUM Long Detail Number
  ARITEM String*16
  ARUOM String*10
  QUANTITY BCD*10.5 Quantity Allocated
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  BILLTYPE Integer Billing Type
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHR BCD*10.3 Billing Amount (Func)
  BILLCCY String*3 Billing Currency
  COSTCCY String*3
  APERCENT BCD*5.5 Allocated Percentage
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3
  TOTCOSTSR BCD*10.3
  TOTCOSTHM BCD*10.3
  OVERHD Integer Overhead Type
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  COMMENTS String*250 Comments
  CONTSTYLE Integer
  PROJTYPE Integer
  CUSTOMER String*12
  REVREC Integer
  INVTYPE Integer
  TRANSDATE Date
  FISCALYEAR String*4
  FISCALPER Integer
  VALUES Long Optional Fields
  AIAPRINT Integer
  CONVERSION BCD*10.6 Conversion
  STRDUOM String*10 UOM
  STRDCONVER BCD*10.6 Stored Conversion Factor

## PMMTADAO - Material Allocation Detail Optional Field (view PM0467)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO+OPTFIELD; OPTFIELD+POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]

## PMMTADO - Material Allocation Dtl Optional (view PM0463)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMMTAH - Material Allocation (view PM0460)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; MALLOCNO; COMPLETE+MALLOCNO [M]; TRANSTAT+MALLOCNO
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MALLOCNO String*16 Material Allocation Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  NUMDTL Long Number of Details
  NEXTDTLNUM Long Next Detail Number
  TRANSTAT Integer Transaction Status
  PRINTSTAT Boolean Print Status [0=False,1=True]
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  DATEBUS Date Posting Date
  ENTEREDBY String*8 Entered By

## PMMTAHA - Material Allocation (view PM0464)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; MALLOCNO [D]; POSTSEQNO+TRANSDATE
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  POSTDATE Date Post Date
  MALLOCNO String*16 Material Allocation Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  REFERENCE String*60 Reference
  DESC String*60 Description
  NUMDTL Long Number of Details
  NEXTDTLNUM Long Next Detail Number
  TRANSTAT Integer
  PRINTSTAT Boolean Print Status
  COMPLETE Integer Status
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  DATEBUS Date Posting Date

## PMMTAHAO - Material Allocation Optional Field (view PM0466)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+OPTFIELD; OPTFIELD+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]

## PMMTAHO - Material Allocation Optional (view PM0462)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMOBD - Opening Balances Detail (view PM0402)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; DOCNUM+LINENO [M]; SEQ+DETAILNUM; OPENTYPE+CONTRACT+PROJECT+CATEGORY+RESOURCE [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*16 Document Number
  OPENTYPE Integer Opening Type [1=Actuals,2=Activity,3=Stored]
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  COSTREV Integer Actual Type [1=Cost,2=Revenue]
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  COSTTYPE Integer Cost Type [0=None,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  DETAILNUM Long Detail Number
  COMMENTS String*250 Comments
  CUSTOMER String*12 Customer
  BILLCCY String*3 Customer Currency
  RATETYPE String*2 Rate Type
  RATEOP Integer Rate Operation [1=Multiply,2=Divide]
  RATEDATE Date Rate Date
  RATE BCD*8.7 Rate
  RATESPREAD BCD*8.7 Rate Spread
  OQTY BCD*10.5 Original Quantity
  AQTY BCD*10.5 Actual Quantity
  OARITEM String*16 Original A/R Item Number
  OARUOM String*10 Original A/R Unit of Measure
  OUNITCOST BCD*10.6 Original Unit Cost
  OEXTCOSTSR BCD*10.3 Original Extended Cost
  OEXTCOSTHM BCD*10.3 Original Extended Cost
  AEXTCOSTSR BCD*10.3 Actual Extended Cost
  AEXTCOSTHM BCD*10.3 Actual Extended Cost
  OOHTYPE Integer Overhead Type [0=Unknown,1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OOHRATE BCD*10.6 Overhead Rate
  OOHPER BCD*5.5 Overhead Percentage
  OOHSR BCD*10.3 Original Overhead Estimate
  OOHHM BCD*10.3 Original Overhead Estimate
  AOHSR BCD*10.3 Actual Overhead
  AOHHM BCD*10.3 Actual Overhead
  OLABORTYPE Integer Labor Type [0=Unknown,1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  OLABORRATE BCD*10.6 Labor Rate
  OLABORPER BCD*5.5 Labor Percentage
  OLABORSR BCD*10.3 Original Labor Amount Estimate
  OLABORHM BCD*10.3 Original Labor Amount Estimate
  ALABORSR BCD*10.3 Actual Labor Amount
  ALABORHM BCD*10.3 Actual Labor Amount
  OTOTCOSTSR BCD*10.3 Original Total Cost
  OTOTCOSTHM BCD*10.3 Original Total Cost
  ATOTCOSTSR BCD*10.3 Actual Total Cost
  ATOTCOSTHM BCD*10.3 Actual Total Cost
  OBILLTYPE Integer Billing Type [0=Unknown,2=Billable,3=No Charge,1=Non-billable]
  OBILLRATE BCD*10.6 Original Billing Rate
  OBILLSR BCD*10.3 Original Total Revenue
  OBILLHM BCD*10.3 Original Total Revenue
  ABILLSR BCD*10.3 Actual Total Revenue
  ABILLHM BCD*10.3 Actual Total Revenue
  RBILLSR BCD*10.3 Remaining to be Billed
  OPROFITSR BCD*10.3 Original Profit
  OPROFITHM BCD*10.3 Original Profit
  APROFITSR BCD*10.3 Actual Profit
  APROFITHM BCD*10.3 Actual Profit
  TARRECTSSR BCD*10.3 Total A/R Customer Receipts
  ARRECDATE Date Last A/R Receipt Posting Date
  TAPPAYMTS BCD*10.3 Total A/P Vendor Payments
  APPAYDATE Date Last A/P Payment Posting Date
  COSTDATE Date Last Cost Posting Date
  BILLDATE Date Last Billings Posting Date
  REVRECDATE Date Last Rev. Recognition Posting Date
  REVESTDATE Date Last Revised Posting Date
  LSTBILLPER BCD*5.5 Last Billings Percent Complete
  PODATE Date Last Purchase Order Date
  PORECDATE Date Last P/O Receipt Date
  PORETDATE Date Last P/O Return Date
  PLSTPDATCP Date Last Canadian Payroll Posting Date
  PLSTPDATUP Date Last US Payroll Posting Date
  CONTSTYLE Integer ^2 Style [0=Unknown,1=Standard,2=Basic]
  PROJTYPE Integer ^2 Type [0=Unknown,1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [0=Unknown,1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [0=Unknown,1=Item,2=Summary]
  REVERSED Integer Reversed
  STRDQTY BCD*10.5 Stored Quantity
  STRDCOSTHM BCD*10.3 Stored Cost
  STRDBILLSR BCD*10.3 Stored Billable Amount
  PRECOLEDSR BCD*10.3 Previous Completed Work
  STRDOHHM BCD*10.3 Overhead Amount
  STRDTCSTHM BCD*10.3 Total Stored Cost
  COHTYPE Integer Overhead Type
  COHRATE BCD*10.6 Overhead Rate
  COHPER BCD*5.5 Overhead Percentage
  USEAIA Integer Use AIA Report
  PREAIAPAY BCD*10.3 Previous Certificates for Payment
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  PRESTORED BCD*10.3 G703 Column F from Last AIA Report
  PRERETAIN BCD*10.3 G703 Column I from Last AIA Report
  OESHPDATE Date Last O/E Shipment Date
  OEINVDATE Date Last O/E Invoice Date

## PMOBDA - Opening Balances Audit Detail (view PM0404)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM; CONTRACT+PROJECT+CATEGORY+TRANSDATE [D]; CONTRACT+PROJECT+TRANSDATE [D]
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  DOCNUM String*16 Document Number
  OPENTYPE Integer Opening Type
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  COSTREV Integer Actual Type
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  COSTTYPE Integer Cost Type
  DETAILNUM Long Detail Number
  COMMENTS String*250 Comments
  CUSTOMER String*12 Customer
  BILLCCY String*3 Customer Currency
  RATETYPE String*2 Rate Type
  RATEOP Integer Rate Operation
  RATEDATE Date Rate Date
  RATE BCD*8.7 Rate
  RATESPREAD BCD*8.7 Rate Spread
  OQTY BCD*10.5 Original Quantity
  AQTY BCD*10.5 Actual Quantity
  OARITEM String*16 Original A/R Item Number
  OARUOM String*10 Original A/R Unit of Measure
  OUNITCOST BCD*10.6 Original Unit Cost
  OEXTCOSTSR BCD*10.3 Original Extended Cost
  OEXTCOSTHM BCD*10.3 Original Extended Cost
  AEXTCOSTSR BCD*10.3 Actual Extended Cost
  AEXTCOSTHM BCD*10.3 Actual Extended Cost
  OOHTYPE Integer Overhead Type
  OOHRATE BCD*10.6 Overhead Rate
  OOHPER BCD*5.5 Overhead Percentage
  OOHSR BCD*10.3 Original Overhead Estimate
  OOHHM BCD*10.3 Original Overhead Estimate
  AOHSR BCD*10.3 Actual Overhead
  AOHHM BCD*10.3 Actual Overhead
  OLABORTYPE Integer Labor Type
  OLABORRATE BCD*10.6 Labor Rate
  OLABORPER BCD*5.5 Labor Percentage
  OLABORSR BCD*10.3 Original Labor Amount Estimate
  OLABORHM BCD*10.3 Original Labor Amount Estimate
  ALABORSR BCD*10.3 Actual Labor Amount
  ALABORHM BCD*10.3 Actual Labor Amount
  OTOTCOSTSR BCD*10.3 Original Total Cost
  OTOTCOSTHM BCD*10.3 Original Total Cost
  ATOTCOSTSR BCD*10.3 Actual Total Cost
  ATOTCOSTHM BCD*10.3 Actual Total Cost
  OBILLTYPE Integer Billing Type
  OBILLRATE BCD*10.6 Original Billing Rate
  OBILLSR BCD*10.3 Original Total Revenue
  OBILLHM BCD*10.3 Original Total Revenue
  ABILLSR BCD*10.3 Actual Total Revenue
  ABILLHM BCD*10.3 Actual Total Revenue
  RBILLSR BCD*10.3 Remaining to be Billed
  OPROFITSR BCD*10.3 Original Profit
  OPROFITHM BCD*10.3 Original Profit
  APROFITSR BCD*10.3 Actual Profit
  APROFITHM BCD*10.3 Actual Profit
  TARRECTSSR BCD*10.3 Total A/R Customer Receipts
  ARRECDATE Date Last A/R Receipt Posting Date
  TAPPAYMTS BCD*10.3 Total A/P Vendor Payments
  APPAYDATE Date Last A/P Payment Posting Date
  COSTDATE Date Last Cost Posting Date
  BILLDATE Date Last Billings Posting Date
  REVRECDATE Date Last Rev. Recognition Posting Date
  REVESTDATE Date Last Revised Posting Date
  LSTBILLPER BCD*5.5 Last Billings Percent Complete
  PODATE Date Last Purchase Order Date
  PORECDATE Date Last P/O Receipt Date
  PORETDATE Date Last P/O Return Date
  PLSTPDATCP Date Last Canadian Payroll Posting Date
  PLSTPDATUP Date Last US Payroll Posting Date
  CONTSTYLE Integer ^2 Style
  PROJTYPE Integer ^2 Type
  REVREC Integer Accounting Method
  INVTYPE Integer Invoice Type
  REVERSED Integer Reversed
  STRDQTY BCD*10.5 Stored Quantity
  STRDCOSTHM BCD*10.3 Stored Cost
  STRDBILLSR BCD*10.3 Stored Billable Amount
  PRECOLEDSR BCD*10.3 Previous Completed Work
  STRDOHHM BCD*10.3 Overhead Amount
  STRDTCSTHM BCD*10.3 Total Stored Cost
  COHTYPE Integer Overhead Type
  COHRATE BCD*10.6 Overhead Rate
  COHPER BCD*5.5 Overhead Percentage
  USEAIA Integer Use AIA Report
  PREAIAPAY BCD*10.3 Previous Certificates for Payment
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  PRESTORED BCD*10.3 G703 Column F from Last AIA Report
  PRERETAIN BCD*10.3 G703 Column I from Last AIA Report
  OESHPDATE Date Last O/E Shipment Date
  OEINVDATE Date Last O/E Invoice Date

## PMOBH - Opening Balances (view PM0401)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; DOCNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*16 Document Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMOBHA - Opening Balances Audit (view PM0403)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; SEQ+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  DOCNUM String*16 Document Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  REFERENCE String*60 Reference
  DESC String*60 Description
  COMPLETE Integer Status
  TRANSTAT Integer Transaction Status
  NEXTDTLNUM Long Next Detail Number
  NUMDTL Long Number of Details
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  DATEBUS Date Posting Date

## PMOE - O/E Superview (view PM0473)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DAYENDDATE Date Day End Date
  DOCTYPE Integer Document Type [1=Quote,2=Order Entry,3=Shipment]
  TRANSTYPE Integer Transaction Type [1=Posted,2=Adjustment]
  DETAILTYPE Integer Detail Line Type [0=Item,1=Miscellaneous Charges]
  MULTIFROM Integer From Multiple Documents [1=Yes,0=No]
  FROMDOC String*22 From Document Number
  FRMDOCTYPE Integer From Document Type [1=Quote,2=Order Entry,3=Shipment]
  SEQUENCENO BCD*10.0 Sequence Key
  LINENO BCD*10.0 Line Number
  DOCNUM String*22 Document Number
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  IDCUST String*12 Customer Number
  TRANSDATE Date Transaction Date
  CURRENCY String*3 Currency Code
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATE BCD*8.7 Rate
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  ARITEM String*16 A/R Item Number
  ARUOM String*10 A/R Unit of Measure
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  QUANTITY BCD*10.5 Quantity
  UNIT String*10 Unit Of Measure
  CONVERSION BCD*10.6 Conversion
  UNITCOSTSR BCD*10.6 Unit Cost (source)
  UNITCOSTHM BCD*10.6 Unit Cost (functional)
  DISCOUNTSR BCD*10.6 Discount Amount in source currency
  DISCOUNTHM BCD*10.6 Discount Amount in functional currency
  EXTAMTSR BCD*10.3 Extended Amount (source)
  EXTAMTHM BCD*10.3 Extended Amount (functional)
  TOTAMTSR BCD*10.3 Total Amount (source)
  TOTAMTHM BCD*10.3 Total Amount (fucntional)
  TAXAMTSR BCD*10.3 Total tax amout (source)
  TAXAMTHM BCD*10.3 Total tax amout (functional)
  TAMTSR BCD*10.3 Total Amount inc. tax (source)
  TAMTHM BCD*10.3 Total Amount inc. tax (functional)
  BILLRATE BCD*10.6 Billing Rate
  BILLTYPE Integer Billing Type [0=None,2=Billable,3=No Charge,1=Non-billable]
  EXTBILLSR BCD*10.3 Extended Billing Amount (source)
  EXTBILLHM BCD*10.3 Reserved
  WIPACCT String*45 Work In Process Account
  REVACCT String*45 Revenue/Billing Account
  CVACCT String*45 Cost Variance Account
  CALCOHEAD Integer Calculate Overhead? [1=Yes,0=No,2=Not Set]
  CALCLABOR Integer Calculate Labor? [1=Yes,0=No,2=Not Set]
  COMMENTS String*250 Comments
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TITMCLSS1 Integer Item Tax Class for Tax Authority 1
  TITMCLSS2 Integer Item Tax Class for Tax Authority 2
  TITMCLSS3 Integer Item Tax Class for Tax Authority 3
  TITMCLSS4 Integer Item Tax Class for Tax Authority 4
  TITMCLSS5 Integer Item Tax Class for Tax Authority 5
  TINCLUDE1 Integer Tax Included 1
  TINCLUDE2 Integer Tax Included 2
  TINCLUDE3 Integer Tax Included 3
  TINCLUDE4 Integer Tax Included 4
  TINCLUDE5 Integer Tax Included 5
  TAXBASES1 BCD*10.3 Tax Base 1 (source)
  TAXBASES2 BCD*10.3 Tax Base 2 (source)
  TAXBASES3 BCD*10.3 Tax Base 3 (source)
  TAXBASES4 BCD*10.3 Tax Base 4 (source)
  TAXBASES5 BCD*10.3 Tax Base 5 (source)
  TAXBASEH1 BCD*10.3 Tax Base 1 (functional)
  TAXBASEH2 BCD*10.3 Tax Base 2 (functional)
  TAXBASEH3 BCD*10.3 Tax Base 3 (functional)
  TAXBASEH4 BCD*10.3 Tax Base 4 (functional)
  TAXBASEH5 BCD*10.3 Tax Base 5 (functional)
  TAXAMTS1 BCD*10.3 Tax Amount 1 (source)
  TAXAMTS2 BCD*10.3 Tax Amount 2 (source)
  TAXAMTS3 BCD*10.3 Tax Amount 3 (source)
  TAXAMTS4 BCD*10.3 Tax Amount 4 (source)
  TAXAMTS5 BCD*10.3 Tax Amount 5 (source)
  TAXAMTH1 BCD*10.3 Tax Amount 1 (functional)
  TAXAMTH2 BCD*10.3 Tax Amount 2 (functional)
  TAXAMTH3 BCD*10.3 Tax Amount 3 (functional)
  TAXAMTH4 BCD*10.3 Tax Amount 4 (functional)
  TAXAMTH5 BCD*10.3 Tax Amount 5 (functional)
  DRILLSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link
  DRILLAPP String*2 Drill Down Application
  OHACCT String*45 Overhead Account
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  LABACCT String*45 Labor Account
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  LABORSR BCD*10.3 Labor Amount
  LABORHM BCD*10.3 Labor Amount
  TRANSNUM Long Transaction Number
  VALUES Long Optional Fields
  TAMTRETSR BCD*10.3 Source Retainage Amount
  TAMTRETHM BCD*10.3 Functional Retainage Amount
  RETDUEDT Date Retainage Due Date
  OHLABORQTY BCD*10.5 Quantity for Misc Charge
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  OEBILLABLE Boolean Invoiced in O/E?
  DATEBUS Date Posting Date
  CVAMT BCD*10.3 Cost Variance Amount

## PMOEO - O/E Optional Field (view PM0474)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMOFD - Optional Fields Detail (view PM0500)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [1=Contracts,2=Projects,3=Categories,4=Employees,5=Equipment,6=Miscellaneous Expenses,7=Overhead Expenses,8=Subcontractors,10=Charge Codes,9=Material,100=Material Usage,101=Material Usage Details,110=Material Return,111=Material Return Details,120=Timecards,121=Timecard Details,122=Timecard Expenses,130=Equipment Usage,131=Equipment Usage Details,140=Charges,141=Charges Details,150=Adjustment,151=Adjustment Details,160=Revenue Recognition,170=Billing,171=Billing Detail,181=External Cost Transactions,190=Reopening Projects,182=Costs,183=Cost Details,184=Material Allocation,185=Material Allocation Details]
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEFVAL String*60 Default Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate Optional Field [0=No,1=Yes]
  INITFLAG Integer Init Flag [0=No,1=Yes]
  SWICSHP Integer I/C Shipments
  SWICSHPD Integer I/C Shipments Details
  SWICADJ Integer I/C Adjustments
  SWICADJD Integer I/C Adjustments Detail
  SWPAYTC Integer Payroll Timecards
  SWPAYTCD Integer Payroll Timecard Details
  SWWIP Integer Work In Progress
  SWCOS Integer Cost of Sales
  SWPAYEXP Integer Payroll Expense
  SWLABOR Integer Labor
  SWOHEAD Integer Overhead
  SWEQUIP Integer Equipment
  SWEMPEXP Integer Employee Expense
  SWARINV Integer Accounts Receivable Invoices
  SWREV Integer Revenue
  SWBILL Integer Billings
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer [0=No,1=Yes]
  SWCOSTETRY Integer Cost

## PMOFH - Optional Fields Header (view PM0501)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [1=Contracts,2=Projects,3=Categories,4=Employees,5=Equipment,6=Miscellaneous Expenses,7=Overhead Expenses,8=Subcontractors,10=Charge Codes,9=Material,100=Material Usage,101=Material Usage Details,110=Material Return,111=Material Return Details,120=Timecards,121=Timecard Details,122=Timecard Expenses,130=Equipment Usage,131=Equipment Usage Details,140=Charges,141=Charges Details,150=Adjustment,151=Adjustment Details,160=Revenue Recognition,170=Billing,171=Billing Detail,181=External Cost Transactions,190=Reopening Projects,182=Costs,183=Cost Details,184=Material Allocation,185=Material Allocation Details]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Values

## PMOHEXP - Overhead Codes (view PM0029)
Keys (first = PK; D=dups allowed, M=modifiable): OHCODE
Fields (NAME type description [values]):
  OHCODE String*16 Overhead Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  DATEINACTV Date Date Inactive
  VALUES Long Optional Fields
  UNITCOST BCD*10.6 Unit Cost

## PMOHEXPD - Overhead Expenses Detail View (view PM0481)
Keys (first = PK; D=dups allowed, M=modifiable): OHCODE+CCY
Fields (NAME type description [values]):
  OHCODE String*16 Overhead Code
  CCY String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ARITEM String*16 AR Item
  UOM String*10 AR UOM
  BILLRATE BCD*10.6 Billing Rate
  DESC String*60 Currency Description

## PMOHEXPO - Overhead Optional Fields (view PM0514)
Keys (first = PK; D=dups allowed, M=modifiable): OHCODE+OPTFIELD; OPTFIELD+OHCODE
Fields (NAME type description [values]):
  OHCODE String*16 Overhead Code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMOPT - Options (view PM0003)
Keys (first = PK; D=dups allowed, M=modifiable): IDOPT01
Fields (NAME type description [values]):
  IDOPT01 Integer Dummy
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTACT String*60 Contact Name
  PHONE String*30 Telephone
  FAX String*30 Fax Number
  DATELASTMN Date Last Maintained
  MULTICURR Boolean Multicurrency
  HOMECURR String*3 Home Currency
  DEFOVERHD Integer Default Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  DEFLABOR Integer Default Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  SWEDITIMPT Boolean Edit Imported Batches
  SWFRCLST Boolean Force Listing of Transactions
  DEFREVREC Integer Default Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  PAYROLL Integer Payroll [3=None,1=US Payroll,2=Canadian Payroll]
  DEFERGLPST Boolean Create G/L Transactions [1=During Posting,0=On Request Using Create G/L Batch Icon]
  APPENDGL Integer Append G/L Batch [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  CONSOLGL Integer Consolidate G/L Batches [1=Do Not Consolidate,9=Consolidate Transaction Details by Account,2=Consolidate by Account and Fiscal Period,3=Consolidate by Account, Fiscal Period, and Source]
  CODEGLREF Integer G/L Reference Field - Not Used [1=Customer Number,2=Customer Name,3=Document Number,4=Contract Number,5=Project,6=Category,7=Contract-Project-Category,8=Type-Posting Seq.-Document Number,9=Resource,10=Purchase Order Number,11=Description,12=Reference]
  CODEGLDESC Integer G/L Description Field - Not Used [1=Customer Number,2=Customer Name,3=Document Number,4=Contract Number,5=Project,6=Category,7=Contract-Project-Category,8=Type-Posting Seq.-Document Number,9=Resource,10=Purchase Order Number,11=Description,12=Reference]
  NXTCHRGSEQ Long Charges
  NXTEQIPSEQ Long Equipment Usage
  NXTCHNGSEQ Long Revise Estimates
  NXTCARDSEQ Long Timecards
  NXTSTKASEQ Long Reserved
  NXTSTKRSEQ Long Reserved
  NXTRRSEQ Long Revenue Recognition
  NXTADJSEQ Long Adjustments
  COSTBTCH BCD*5.0 Cost
  INVBTCH BCD*5.0 Invoice
  TCARDBTCH BCD*5.0 Timecard
  STKABTCH BCD*5.0 Material Usage
  STKRBTCH BCD*5.0 Material Return
  PMSC String*2 Project and Job Costing
  STKALLSC String*2 Material Usage
  STKRETSC String*2 Material Returns
  TIMECARDSC String*2 Timecards
  RRSC String*2 Revenue Recognition
  EQUIPSC String*2 Equipment Usage
  CHRGSC String*2 Charges
  ADJSC String*2 Adjustments
  RETAR BCD*5.5 Default A/R Retainage Percentage
  RETDAYSAR Integer Default A/R Retainage No of Days
  RETAP BCD*5.5 Default A/P Retainage Percentage
  RETDAYSAP Integer Default A/P Retainage No of Days
  DATELASTRR Date Date Last Revenue Recognition
  TIMELASTRR Time Time Last Revenue Recognition
  DATELASTBB Date Date Last Billing Worksheet
  DATELASTAL Date Date Last Material Usage
  DATELASTRE Date Date Last Material Return
  DATELASTTC Date Date Last Timecard
  DATELASTCS Date Date Last Cost Batch Posted
  DATELASTIN Date Date Last Invoice Batch Posted
  DATELASTCH Date Date Last Charges Posted
  DATELASTEU Date Date Last Equipment Usage
  DATELASTES Date Date Last Revised Estimates Posted
  ARGLEDIT Boolean Allow Edit of G/L Codes in A/R
  APGLEDIT Boolean Allow Edit of G/L Codes in A/P
  AGINPERD1 BCD*3.0 Aging Period 1
  AGINPERD2 BCD*3.0 Aging Period 2
  AGINPERD3 BCD*3.0 Aging Period 3
  LEVEL1NAME String*30 Level 1 Name
  LEVEL2NAME String*30 Level 2 Name
  LEVEL3NAME String*30 Level 3 Name
  DEFSTRUCT String*6 Default Contract Structure
  HYPEN Boolean Use Hypen
  FWDSLASH Boolean Use Forward Slash
  BCKSLASH Boolean Use Back Slash
  ASTERISK Boolean Use Asterisk
  PERIOD Boolean Use Period
  LFTPARENS Boolean Use Left Parenthesis
  RGTPARENS Boolean Use Right Parenthesis
  POUNDSGN Boolean Use Pound Sign
  TEXTTCPF String*6 Time Card Prefix
  CNTTCPFLEN BCD*2.0 Timecard Number Length
  CNTTCSEQ String*16 Next Timecard Number
  TEXTSAPF String*6 Material Usage Prefix
  CNTSAPFLEN BCD*2.0 Material Usage Number Length
  CNTSASEQ String*16 Next Material Usage Number
  TEXTSRPF String*6 Material Return Prefix
  CNTSRPFLEN BCD*2.0 Material Return Number Length
  CNTSRSEQ String*16 Next Material Returns Number
  TEXTEQPF String*6 Equipment Usage Prefix
  CNTEQPFLEN BCD*2.0 Equipment Usage Number Length
  CNTEQSEQ String*16 Next Equipment Usage Number
  TEXTCOPF String*6 Revised Estimate Prefix
  CNTCOPFLEN BCD*2.0 Revised Estimate Number Length
  CNTCOSEQ String*16 Next Revised Estimate Number
  TEXTCHRGPF String*6 Charge Prefix
  TEXTADJPF String*6 Adjustments
  CNTADJLEN BCD*2.0 Adjustment Number Length
  CNTADJSEQ String*16 Next Adjustment Number
  CNTCHRGLEN BCD*2.0 Charge Number Length
  CNTCHRGSEQ String*16 Next Charge Number
  NEXTCTUNIQ BCD*10.0 Next Contract Unique
  CNTBBSEQ String*16 A/R Billing
  CNTRRSEQ String*16 Revenue Recognition
  TEXTBBPF String*6 A/R Billing Prefix
  TEXTRRPF String*6 Revenue Recognition Prefix
  CNTBBLEN BCD*2.0 A/R Billing Length
  CNTRRLEN BCD*2.0 Revenue Recognition Length
  PROJTYPE Boolean Allow Edit of Project Type
  ARITEM String*16 Default A/R Item Number
  ARUOM String*10 Default A/R Unit of Measure
  PAYROLLTC String*6 Payroll
  GLEQIPSEQ BCD*10.0 Equipment Usage
  GLCARDSEQ BCD*10.0 Timecards
  GLRRSEQ BCD*10.0 Revenue Recognition
  GLADJSEQ BCD*10.0 Adjustments
  LEVEL4NAME String*30 Level 1 Name - Plural
  LEVEL5NAME String*30 Level 2 Name - Plural
  LEVEL6NAME String*30 Level 3 Name - Plural
  CESC String*2 Costs
  ROSC String*2 Reopen Projects

## PMOPT2 - Options (view PM0003)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Last Maintained
  OPT001ACTV Boolean
  OPT001NAME String*32
  OPT001TBL String*8
  OPT002ACTV Boolean
  OPT002NAME String*32
  OPT002TBL String*8
  OPT003ACTV Boolean
  OPT003NAME String*32
  OPT003TBL String*8
  OPT004ACTV Boolean
  OPT004NAME String*32
  OPT004TBL String*8
  OPT005ACTV Boolean
  OPT005NAME String*32
  OPT005TBL String*8
  OPT006ACTV Boolean
  OPT006NAME String*32
  OPT006TBL String*8
  OPT007ACTV Boolean
  OPT007NAME String*32
  OPT007TBL String*8
  OPT008ACTV Boolean
  OPT008NAME String*32
  OPT008TBL String*8
  OPTDT1ACTV Boolean
  OPTDT1NAME String*32
  OPTDT2ACTV Boolean
  OPTDT2NAME String*32
  OPTAM1ACTV Boolean
  OPTAM1NAME String*32
  OPTAM2ACTV Boolean
  OPTAM2NAME String*32

## PMOPT3 - Options (view PM0003)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATELASTMN Date Last Maintained
  DEFCONT Integer
  APDARBTH Boolean
  ARDESCFLD Integer
  ARCOMFLD Integer
  CHRGUNIQ Long
  EQIPUNIQ Long
  CHNGUNIQ Long
  CARDUNIQ Long
  STKAUNIQ Long
  STKRUNIQ Long
  RRUNIQ Long
  ADJUNIQ Long
  BBSEQ Long
  ERRSEQ Long
  NUMCONTS Long
  PLCODE String*16
  RRMETHOD Integer
  BUDAUDIT Boolean
  BUDSEQ Long
  BUDUNIQ Long
  STATESEQ Long
  OBSEQ Long
  OBDOCNUML BCD*2.0
  OBPREFIX String*6
  OBNEXTNUM String*16
  URSEQ Long
  URDOCNUML BCD*2.0
  URPREFIX String*6
  URNEXTNUM String*16
  TCUCBASPAY Integer
  TCUCSTDPAY Integer
  TCUCBASPJC Integer
  TCUCSTDPJC Integer
  TCBRBASPAY Integer
  TCBRSTDPAY Integer
  TCBRBASPJC Integer
  TCBRSTDPJC Integer
  EQUCBAS Integer
  EQUCSTD Integer
  EQBRBAS Integer
  EQBRSTD Integer
  SCUCBAS Integer
  SCUCSTD Integer
  SCBRBAS Integer
  SCBRSTD Integer
  OBPOSTSEQ Long
  URPOSTSEQ Long
  CESEQ Long
  CEDOCNUML BCD*2.0
  CEPREFIX String*6
  CENEXTNUM String*16
  CEPOSTSEQ Long
  CEGLSEQ BCD*10.0
  ROSEQ Long
  RODOCNUML BCD*2.0
  ROPREFIX String*6
  RONEXTNUM String*16
  ROPOSTSEQ Long
  ROGLSEQ BCD*10.0
  MTALSEQ Long
  MTALDOCNOL BCD*2.0
  MTALPREFIX String*6
  MTALNEXTNO String*16
  MTALPSTSEQ Long
  COMCSTPSEQ Long
  USEBUDGET Boolean
  USEEXPACCT Boolean
  RECOGCOST Boolean
  DATEDEF Integer

## PMOPT4 - Options (view PM0003)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AAPROJECT Integer
  AACATEGORY Integer
  PBRWGEN Integer
  PBBWGEN Integer
  AIFPBCA Integer
  APROJSTYLE Integer

## PMPERR - Posting Errors (view PM0130)
Keys (first = PK; D=dups allowed, M=modifiable): DOCTYPE+ERRSEQ+SEQ+LINENO+ERRNUM
Fields (NAME type description [values]):
  DOCTYPE Integer Document Type [1=Material Usage,2=Material Returns,3=Timecards,4=Equipment Usage,5=Charges,6=Revise Estimates,7=Adjustments,9=Update Payroll,10=Create G/L Batch,11=Create Billing Worksheet,12=Billing Worksheets,13=Post Billing Worksheets,14=Create Rev Rec Worksheet,15=Revenue Recognition Worksheet,16=Use Current Exchange Rate,17=Update Retainage,18=Costs,19=Reopening Projects Generate,20=Reopening Projects Worksheet,21=Material Allocation,9999=Activation]
  ERRSEQ Long Error Sequence
  SEQ Long Sequence
  LINENO Long LINENO from detail
  ERRNUM Long Error number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCUMENT String*30 Document number
  DETAILNUM Long DETAILNUM from detail
  LINE Long Line number starting at 1
  ERR String*250 Description of Error
  SRCETYPE Integer Drilldown Transaction Type [0=None,1=Equipment Usage,2=Charges,3=Material Usage,4=Material Return,5=Timecard,6=Adjustment,7=Revenue Recognition,17=Costs,8=A/R Invoice Entry,9=A/P Invoice Entry,10=PJC Billing Worksheet,11=A/R Receipt,12=A/P Payment,13=A/R Adjustment,14=A/P Adjustment,18=Reopen Projects Worksheet,19=Refunds]
  DRILLDWNLK BCD*10.0 Drilldown Link
  DRILLKEY String*40 Document Key
  POSTDATE Date Posting Date
  POSTTIME Time Posting Time

## PMPO - P/O Superview (view PM0305)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DAYENDDATE Date Day End Date
  DOCTYPE Integer Document Type [1=Purchase Order,2=Receipt,3=Return,4=Invoice,5=Credit Note,6=Debit Note,7=Committed Receipt,9=Committed Invoice]
  TRANSTYPE Integer Transaction Type [1=Posted,2=Cost Adjustment,3=Commitment Update,4=Billing Adjustment]
  ADDCOST Integer Additional Cost Type [0=None (Item),1=Prorated,2=Prorated Manually,3=Expensed]
  MULTIFROM Integer From Multiple Documents [1=Yes,0=No]
  FROMDOC String*22 From Document Number
  FRMDOCTYPE Integer From Document Type [8=Requisition,1=Purchase Order,2=Receipt,3=Return,4=Invoice]
  SEQUENCENO BCD*10.0 Sequence Key
  LINENO BCD*10.0 Line Number
  COSTLINENO BCD*10.0 Additional Cost Line Number
  DOCNUM String*24 Document Number
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  REFERENCE String*60 Reference
  DESC String*60 Description
  VENDORID String*12 Vendor Number
  TRANSDATE Date Transaction Date
  CURRENCY String*3 Currency Code
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATE BCD*8.7 Rate
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  ARITEM String*16 A/R Item Number
  ARUOM String*10 A/R Unit of Measure
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  QUANTITY BCD*10.5 Quantity
  UNIT String*10 Unit Of Measure
  CONVERSION BCD*10.6 Conversion
  UNITCOSTSR BCD*10.6 Unit Cost (source)
  UNITCOSTHM BCD*10.6 Unit Cost (functional)
  DISCOUNTSR BCD*10.6 Discount Amount in source currency
  DISCOUNTHM BCD*10.6 Discount Amount in functional currency
  ALLOTAXSR BCD*10.3 Allocated Tax (source)
  ALLOTAXHM BCD*10.3 Allocated Tax (functional)
  EXPTAXSR BCD*10.3 Expensed Tax (source)
  EXPTAXHM BCD*10.3 Expensed Tax (functional)
  RTAXAMTSR BCD*10.3 Recoverable Tax (source)
  RTAXAMTHM BCD*10.3 Recoverable Tax (functional)
  EXTAMTSR BCD*10.3 Extended Amount (source)
  EXTAMTHM BCD*10.3 Extended Amount (functional)
  TOTAMTSR BCD*10.3 Total Amount (source)
  TOTAMTHM BCD*10.3 Total Amount (fucntional)
  TAXAMTSR BCD*10.3 Total tax amout (source)
  TAXAMTHM BCD*10.3 Total tax amout (functional)
  TAMTSR BCD*10.3 Total Amount inc. tax (source)
  TAMTHM BCD*10.3 Total Amount inc. tax (functional)
  BILLRATE BCD*10.6 Billing Rate
  BILLTYPE Integer Billing Type [0=None,2=Billable,3=No Charge,1=Non-billable]
  WIPACCT String*45 Work In Process Account
  CVACCT String*45 Cost Variance Account
  CALCOHEAD Integer Calculate Overhead? [1=Yes,0=No,2=Not Set]
  CALCLABOR Integer Calculate Labor? [1=Yes,0=No,2=Not Set]
  COMMENTS String*250 Comments
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TITMCLSS1 Integer Item Tax Class for Tax Authority 1
  TITMCLSS2 Integer Item Tax Class for Tax Authority 2
  TITMCLSS3 Integer Item Tax Class for Tax Authority 3
  TITMCLSS4 Integer Item Tax Class for Tax Authority 4
  TITMCLSS5 Integer Item Tax Class for Tax Authority 5
  TINCLUDE1 Integer Tax Included 1
  TINCLUDE2 Integer Tax Included 2
  TINCLUDE3 Integer Tax Included 3
  TINCLUDE4 Integer Tax Included 4
  TINCLUDE5 Integer Tax Included 5
  TAXBASES1 BCD*10.3 Tax Base 1 (source)
  TAXBASES2 BCD*10.3 Tax Base 2 (source)
  TAXBASES3 BCD*10.3 Tax Base 3 (source)
  TAXBASES4 BCD*10.3 Tax Base 4 (source)
  TAXBASES5 BCD*10.3 Tax Base 5 (source)
  TAXBASEH1 BCD*10.3 Tax Base 1 (functional)
  TAXBASEH2 BCD*10.3 Tax Base 2 (functional)
  TAXBASEH3 BCD*10.3 Tax Base 3 (functional)
  TAXBASEH4 BCD*10.3 Tax Base 4 (functional)
  TAXBASEH5 BCD*10.3 Tax Base 5 (functional)
  TAXAMTS1 BCD*10.3 Tax Amount 1 (source)
  TAXAMTS2 BCD*10.3 Tax Amount 2 (source)
  TAXAMTS3 BCD*10.3 Tax Amount 3 (source)
  TAXAMTS4 BCD*10.3 Tax Amount 4 (source)
  TAXAMTS5 BCD*10.3 Tax Amount 5 (source)
  TAXAMTH1 BCD*10.3 Tax Amount 1 (functional)
  TAXAMTH2 BCD*10.3 Tax Amount 2 (functional)
  TAXAMTH3 BCD*10.3 Tax Amount 3 (functional)
  TAXAMTH4 BCD*10.3 Tax Amount 4 (functional)
  TAXAMTH5 BCD*10.3 Tax Amount 5 (functional)
  DRILLSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link
  DRILLAPP String*2 Drill Down Application
  OHACCT String*45 Overhead Account
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Overhead Amount
  OHHM BCD*10.3 Overhead Amount
  LABACCT String*45 Labor Account
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  LABORSR BCD*10.3 Labor Amount
  LABORHM BCD*10.3 Labor Amount
  TRANSNUM Long Transaction Number
  VALUES Long Optional Fields
  TAMTRETSR BCD*10.3 Source Retainage Amount
  TAMTRETHM BCD*10.3 Functional Retainage Amount
  RETDUEDT Date Retainage Due Date
  OHLABORQTY BCD*10.5 Quantity for Additional Costs
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  TXEXPCOMSR BCD*10.3 Tax (exp) Committed (source)
  TXEXPCOMHM BCD*10.3 Tax (exp) Committed (func)
  TXALLCOMSR BCD*10.3 Tax (all) Committed (source)
  TXALLCOMHM BCD*10.3 Tax (all) Committed (func)
  TRANSREF Long Transaction Reference
  OTHERREF Long Cost/Revenue TRANSNUM
  DATEBUS Date

## PMPOO - P/O Optional Field (view PM0522)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ
Fields (NAME type description [values]):
  DAYENDSEQ Long Day End Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMPROJ - Project Code (view PM0006)
Keys (first = PK; D=dups allowed, M=modifiable): PROJECT
Fields (NAME type description [values]):
  PROJECT String*16 ^2
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  DATEINACTV Date Date Inactive
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [1=Completed Project,4=Billings and Costs,8=Accrual-Basis]
  COSTPLUSP BCD*5.5 Cost Plus Percentage
  CLOSEBILL Boolean Closed for Billings
  CLOSECOST Boolean Closed for Cost
  USEDEFREV Integer Revenue Type [0=Revenue,1=Deferred Revenue]
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  RETAR BCD*5.5 A/R Retainage Percentage
  RETDAYSAR Integer A/R Retention Period
  SEGOVERRD Boolean Override G/L Account Segments
  SEGNUM1 String*6 Segment 1
  SEGVAL1 String*15 Segment Code 1
  SEGNUM2 String*6 Segment 2
  SEGVAL2 String*15 Segment Code 2
  SEGNUM3 String*6 Segment 3
  SEGVAL3 String*15 Segment Code 3
  SEGNUM4 String*6 Segment 4
  SEGVAL4 String*15 Segment Code 4
  SEGNUM5 String*6 Segment 5
  SEGVAL5 String*15 Segment Code 5
  SEGNUM6 String*6 Segment 6
  SEGVAL6 String*15 Segment Code 6
  SEGNUM7 String*6 Segment 7
  SEGVAL7 String*15 Segment Code 7
  SEGNUM8 String*6 Segment 8
  SEGVAL8 String*15 Segment Code 8
  SEGNUM9 String*6 Segment 9
  SEGVAL9 String*15 Segment Code 9
  FORMCODE String*6 Form Code
  PLCODE String*16 Reserved
  VALUES Long Optional Fields

## PMPROJO - Project Optional Fields (view PM0509)
Keys (first = PK; D=dups allowed, M=modifiable): PROJECT+OPTFIELD; OPTFIELD+PROJECT
Fields (NAME type description [values]):
  PROJECT String*16 Project
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMPROJS - ^5 (view PM0022)
Physical tables of this view: PMPROJS, PMPROJT (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+PLINENUM; CTUNIQ+DETAILNUM; CONTRACT+PROJECT; CUSTOMER+CONTRACT+PROJECT [M]
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 ^1 Uniq
  PLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  DETAILNUM Long Detail Number
  DATELASTMN Date Last Maintained
  STARTDATE Date Projected Start Date
  ORJENDDATE Date Projected End Date
  CURENDDATE Date Current End Date
  CLOSEDDATE Date Date Closed
  DESC String*60 Description
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  COSTPLUSP BCD*5.5 Cost Plus Percentage
  CLOSEBILL Integer Closed to Billings [1=Yes,0=No]
  CLOSECOST Integer Closed to Costs [1=Yes,0=No]
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  USEDEFREV Integer Revenue Type [0=Revenue,1=Deferred Revenue]
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  PERRETREC BCD*5.5 A/R Retainage Percentage
  RETRECD Integer A/R Retention Period
  BILLACCT String*45 Billings
  DEFRACCT String*45 Deferred Revenue
  REVACCT String*45 Revenue
  PROFITACCT String*45 Profit
  LOSSACCT String*45 Loss
  GAINACCT String*45 Gain
  WIPACCT String*45 Work in Progress
  COGSACCT String*45 Cost of Sales
  PONUMBER String*22 P/O Number
  FORMCODE String*6 Form Code
  INVTYPE Integer A/R Invoice Type [1=Item,2=Summary]
  ORATE BCD*8.7 Original Exchange Rate
  ORATETYPE String*2 Original Rate Type
  ORATEDATE Date Original Rate Date
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATEDATE Date Rate Date
  RATESPREAD BCD*8.7 Rate Spread
  ESTBILLCCY Integer Revenue And Cost Currency [1=Revenue and Costs in Functional Currency,2=Revenue in Customer Currency,3=Revenue and Costs in Customer Currency]
  COSTCCY String*3 Cost Currency
  REVCCY String*3 Revenue Currency
  INVSTATE Integer Invoice Status [1=Not Processed,2=On Worksheet,3=On Invoice]
  NUMCATS Long Number of ^6
  ORJTIMECSR BCD*10.3 Reserved
  ORJTIMECHM BCD*10.3 Orig. Labor Cost Est.
  CURTIMECSR BCD*10.3 Reserved
  CURTIMECHM BCD*10.3 Cur. Labor Cost Est.
  ACTTIMECSR BCD*10.3 Reserved
  ACTTIMECHM BCD*10.3 Actual Labor Costs
  RECTIMECSR BCD*10.3 Reserved
  RECTIMECHM BCD*10.3 Reserved
  ORJTIMEBSR BCD*10.3 Orig. Labor Billing Est.
  ORJTIMEBHM BCD*10.3 Orig. Labor Billing Est.
  CURTIMEBSR BCD*10.3 Cur. Labor Billing Est.
  CURTIMEBHM BCD*10.3 Cur. Labor Billing Est.
  ACTTIMEBSR BCD*10.3 Actual Labor Billings
  ACTTIMEBHM BCD*10.3 Actual Labor Billings
  RECTIMEBSR BCD*10.3 Reserved
  RECTIMEBHM BCD*10.3 Reserved
  ORJTIMEQTY BCD*10.5 Orig. Labor Qty Est.
  CURTIMEQTY BCD*10.5 Cur. Labor Qty Est.
  ACTTIMEQTY BCD*10.5 Actual Labor Qty
  PERTIMEQTY BCD*5.5 Labor Percentage Complete
  ORJMATECSR BCD*10.3 Reserved
  ORJMATECHM BCD*10.3 Orig. Material Estimated Cost
  CURMATECSR BCD*10.3 Reserved
  CURMATECHM BCD*10.3 Current Material Estimated Cost
  ACTMATECSR BCD*10.3 Reserved
  ACTMATECHM BCD*10.3 Actual Material Cost
  RECMATECSR BCD*10.3 Reserved
  RECMATECHM BCD*10.3 Reserved
  ORJMATEBSR BCD*10.3 Orig. Material Billing Est.
  ORJMATEBHM BCD*10.3 Orig. Material Billing Est.
  CURMATEBSR BCD*10.3 Cur. Material Billing Est.
  CURMATEBHM BCD*10.3 Cur. Material Billing Est.
  ACTMATEBSR BCD*10.3 Actual Material Billed
  ACTMATEBHM BCD*10.3 Actual Material Billed
  RECMATEBSR BCD*10.3 Reserved
  RECMATEBHM BCD*10.3 Reserved
  ORJMATEQTY BCD*10.5 Orig. Material Qty Est.
  CURMATEQTY BCD*10.5 Cur. Material Est.
  ACTMATEQTY BCD*10.5 Actual Material Qty
  ORJEQUICSR BCD*10.3 Reserved
  ORJEQUICHM BCD*10.3 Orig. Estimated Equipment Cost
  CUREQUICSR BCD*10.3 Reserved
  CUREQUICHM BCD*10.3 Cur. Estimated Equipment Cost
  ACTEQUICSR BCD*10.3 Reserved
  ACTEQUICHM BCD*10.3 Actual Equipment Cost
  RECEQUICSR BCD*10.3 Reserved
  RECEQUICHM BCD*10.3 Reserved
  ORJEQUIBSR BCD*10.3 Orig. Equipment Billing Est.
  ORJEQUIBHM BCD*10.3 Orig. Equipment Billing Est.
  CUREQUIBSR BCD*10.3 Cur. Equipment Billing Est.
  CUREQUIBHM BCD*10.3 Cur. Equipment Billing Est.
  ACTEQUIBSR BCD*10.3 Actual Equipment Amount Billed
  ACTEQUIBHM BCD*10.3 Actual Equipment Amount Billed
  RECEQUIBSR BCD*10.3 Reserved
  RECEQUIBHM BCD*10.3 Reserved
  ORJEQUIQTY BCD*10.5 Orig. Equipment Qty Est.
  CUREQUIQTY BCD*10.5 Cur. Equipment Est.
  ACTEQUIQTY BCD*10.5 Actual Equipment Qty
  ORJSUBCCSR BCD*10.3 Reserved
  ORJSUBCCHM BCD*10.3 Orig. Subcontractor Est. Cost
  CURSUBCCSR BCD*10.3 Reserved
  CURSUBCCHM BCD*10.3 Cur. Subcontractor Est. Cost
  ACTSUBCCSR BCD*10.3 Reserved
  ACTSUBCCHM BCD*10.3 Actual Subcontractor Cost
  RECSUBCCSR BCD*10.3 Reserved
  RECSUBCCHM BCD*10.3 Reserved
  ORJSUBCBSR BCD*10.3 Orig. Subcontract Billing Est.
  ORJSUBCBHM BCD*10.3 Orig. Subcontract Billing Est.
  CURSUBCBSR BCD*10.3 Cur. Subcontract Billing Est.
  CURSUBCBHM BCD*10.3 Cur. Subcontract Billing Est.
  ACTSUBCBSR BCD*10.3 Actual Subcontract Amt Billed
  ACTSUBCBHM BCD*10.3 Actual Subcontract Amt Billed
  RECSUBCBSR BCD*10.3 Reserved
  RECSUBCBHM BCD*10.3 Reserved
  ORJSUBCQTY BCD*10.5 Orig. Subcontractor Qty Est.
  CURSUBCQTY BCD*10.5 Cur. Subcontractor Est.
  ACTSUBCQTY BCD*10.5 Actual Subcontractor Qty
  ORJOHEXCSR BCD*10.3 Reserved
  ORJOHEXCHM BCD*10.3 Orig. Est Overhead Expense Cost
  CUROHEXCSR BCD*10.3 Reserved
  CUROHEXCHM BCD*10.3 Cur. Est. Overhead Expense Cost
  ACTOHEXCSR BCD*10.3 Reserved
  ACTOHEXCHM BCD*10.3 Actual Overhead Expense Cost
  RECOHEXCSR BCD*10.3 Reserved
  RECOHEXCHM BCD*10.3 Reserved
  ORJOHEXBSR BCD*10.3 Orig. Overhead Billing Est.
  ORJOHEXBHM BCD*10.3 Orig. Overhead Billing Est.
  CUROHEXBSR BCD*10.3 Cur. Overhead Billing Est.
  CUROHEXBHM BCD*10.3 Cur. Overhead Billing Est.
  ACTOHEXBSR BCD*10.3 Actual Overhead Amount Billed
  ACTOHEXBHM BCD*10.3 Actual Overhead Billing Est.
  RECOHEXBSR BCD*10.3 Reserved
  RECOHEXBHM BCD*10.3 Reserved
  ORJOHEXQTY BCD*10.5 Orig. Overhead Qty Est.
  CUROHEXQTY BCD*10.5 Cur. Overhead Est.
  ACTOHEXQTY BCD*10.5 Actual Overhead Qty
  ORJMISCCSR BCD*10.3 Reserved
  ORJMISCCHM BCD*10.3 Orig. Est. Miscellaneous Cost
  CURMISCCSR BCD*10.3 Reserved
  CURMISCCHM BCD*10.3 Cur. Est. Miscellaneous Cost
  ACTMISCCSR BCD*10.3 Reserved
  ACTMISCCHM BCD*10.3 Actual Miscellaneous Cost
  RECMISCCSR BCD*10.3 Reserved
  RECMISCCHM BCD*10.3 Reserved
  ORJMISCBSR BCD*10.3 Orig. Miscellaneous Billing Est
  ORJMISCBHM BCD*10.3 Orig. Miscellaneous Billing Est
  CURMISCBSR BCD*10.3 Cur. Miscellaneous Billing Est.
  CURMISCBHM BCD*10.3 Cur. Miscellaneous Billing Est.
  ACTMISCBSR BCD*10.3 Actual Miscellaneous Amt Billed
  ACTMISCBHM BCD*10.3 Actual Miscellaneous Amt Billed
  RECMISCBSR BCD*10.3 Reserved
  RECMISCBHM BCD*10.3 Reserved
  ORJMISCQTY BCD*10.5 Orig. Miscellaneous Qty Est.
  CURMISCQTY BCD*10.5 Cur. Miscellaneous Qty Est.
  ACTMISCQTY BCD*10.5 Actual Miscellaneous Qty
  CUSTOMER String*12 Customer

## PMPROJSO - Project Optional Field (view PM0851)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+PLINENUM+OPTFIELD; OPTFIELD+CTUNIQ+PLINENUM [D]; CONTRACT+PROJECT+OPTFIELD [D]
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 Contract Uniq
  PLINENUM Long Project Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMPROJT - ^5 (view PM0022)
Physical tables of this view: PMPROJS, PMPROJT (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+PLINENUM
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 ^1 Uniq
  PLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORJOHEADSR BCD*10.3 Reserved
  ORJOHEADHM BCD*10.3 Original Overhead Estimate
  CUROHEADSR BCD*10.3 Reserved
  CUROHEADHM BCD*10.3 Current Overhead Estimate
  ACTOHEADSR BCD*10.3 Reserved
  ACTOHEADHM BCD*10.3 Actual Overhead
  ORJLABSR BCD*10.3 Reserved
  ORJLABHM BCD*10.3 Original Labor Amount Estimate
  CURLABSR BCD*10.3 Reserved
  CURLABHM BCD*10.3 Current Labor Amount Estimate
  ACTLABSR BCD*10.3 Reserved
  ACTLABHM BCD*10.3 Actual Labor Amount
  ORJCHRGSR BCD*10.3 Reserved
  ORJCHRGHM BCD*10.3 Reserved
  CURCHRGSR BCD*10.3 Reserved
  CURCHRGHM BCD*10.3 Reserved
  ACTCHRGSR BCD*10.3 Actual Charge Amount
  ACTCHRGHM BCD*10.3 Actual Charge Amount
  ACTCHRGDSR BCD*10.3 Act Chrg Amt Billed & Deferred
  ACTCHRGDHM BCD*10.3 Act Chrg Amt Billed & Deferred
  RECCHRGSR BCD*10.3 Reserved
  RECCHRGHM BCD*10.3 Reserved
  ACTSTKRESR BCD*10.3 Reserved
  ACTSTKREHM BCD*10.3 Act Cost Stock Ret to Inventory
  ACTSTKRQTY BCD*10.5 Act Qty Stock Ret to Inventory
  TARRECTSSR BCD*10.3 Total A/R Customer Receipts
  TARRECTSHM BCD*10.3 Total A/R Customer Receipts
  TAPPAYMTS BCD*10.3 Total A/P Vendor Payments
  TORJCOSTSR BCD*10.3 Reserved
  TORJCOSTHM BCD*10.3 Total Orig. Cost Est.
  TCURCOSTSR BCD*10.3 Reserved
  TCURCOSTHM BCD*10.3 Total Cur. Cost Est.
  TACTCOSTSR BCD*10.3 Reserved
  TACTCOSTHM BCD*10.3 Total Actual Cost
  TRECCOSTSR BCD*10.3 Reserved
  TRECCOSTHM BCD*10.3 Total Cost Recognized
  PERTCOST BCD*5.5 Percent Total Cost
  PERTREV BCD*5.5 Percent Total Revenue
  TORJREVSR BCD*10.3 Total Orig. Revenue Est.
  TORJREVHM BCD*10.3 Total Orig. Revenue Est.
  TCURREVSR BCD*10.3 Total Cur. Revenue Est.
  TCURREVHM BCD*10.3 Total Cur. Revenue Est.
  TACTREVSR BCD*10.3 Total Actual Revenue
  TACTREVHM BCD*10.3 Total Actual Revenue
  TRECREVSR BCD*10.3 Total Revenue Recognized
  TRECREVHM BCD*10.3 Total Revenue Recognized
  RETARAMTSR BCD*10.3 Retainage Receivable
  RETARAMTHM BCD*10.3 Retainage Receivable
  RETARRECSR BCD*10.3 Retainage Amount Received in A/R
  RETARRECHM BCD*10.3 Retainage Amount Received in A/R
  RETAPAMT BCD*10.3 Retainage Payable
  RETAPPAID BCD*10.3 Retainage Amount Paid in A/P
  POAMOUNTSR BCD*10.3 Reserved
  POAMOUNTHM BCD*10.3 Reserved
  POQTY BCD*10.5 Committed P/O Quantity
  OEAMOUNTSR BCD*10.3 Reserved
  OEAMOUNTHM BCD*10.3 Recognized Loss
  OEQTY BCD*10.5 Reserved
  PCOMPLETEB BCD*5.5 Billings Percent Complete
  PCOMPLETER BCD*5.5 RR Percent Complete
  FPAMOUNTSR BCD*10.3 Fixed Price Amount
  FPAMOUNTHM BCD*10.3 Fixed Price Amount
  LSTBILLPER BCD*5.5 Last Billings Percent Complete
  BILLAMTRSR BCD*10.3 Recognized Amount to Bill
  BILLAMTRHM BCD*10.3 Recognized Amount to Bill
  COSTDATE Date Last Cost Posting Date
  BILLDATE Date Last Billings Posting Date
  OHDATE Date Last Overhead Posting Date
  CHARGEDATE Date Last Charge Posting Date
  REVRECDATE Date Last Revenue Rec Posting Date
  ARRECDATE Date Last A/R Receipt Posting Date
  APPAYDATE Date Last A/P Payment Posting Date
  TIMEDATE Date Last Timecard Posting Date
  STKTRDATE Date Last Material Usage Posting Date
  STKRETDATE Date Last Material Return Posting Date
  EQUIPDATE Date Last Equipment Posting Date
  PODATE Date Last Purchase Order Date
  PORECDATE Date Last P/O Receipt Date
  PORETDATE Date Last P/O Return Date
  OEORDDATE Date Reserved
  OEINVDATE Date Last O/E Invoice Date
  PTAXTOTAL BCD*10.3 Project tax total
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  TAXBASES1 BCD*10.3 Tax Base 1
  TAXBASES2 BCD*10.3 Tax Base 2
  TAXBASES3 BCD*10.3 Tax Base 3
  TAXBASES4 BCD*10.3 Tax Base 4
  TAXBASES5 BCD*10.3 Tax Base 5
  TAXBASEH1 BCD*10.3 Tax Base 1
  TAXBASEH2 BCD*10.3 Tax Base 2
  TAXBASEH3 BCD*10.3 Tax Base 3
  TAXBASEH4 BCD*10.3 Tax Base 4
  TAXBASEH5 BCD*10.3 Tax Base 5
  TAXAMTS1 BCD*10.3 Tax Amount 1
  TAXAMTS2 BCD*10.3 Tax Amount 2
  TAXAMTS3 BCD*10.3 Tax Amount 3
  TAXAMTS4 BCD*10.3 Tax Amount 4
  TAXAMTS5 BCD*10.3 Tax Amount 5
  TAXAMTH1 BCD*10.3 Tax Amount 1
  TAXAMTH2 BCD*10.3 Tax Amount 2
  TAXAMTH3 BCD*10.3 Tax Amount 3
  TAXAMTH4 BCD*10.3 Tax Amount 4
  TAXAMTH5 BCD*10.3 Tax Amount 5
  ONBW Boolean On Billing Worksheet
  OPENED Boolean ^2 Has Been Opened [0=No,1=Yes]
  BILLAMT BCD*10.3 Expected Billings
  ORATEOP Integer Rate Operator [1=Multiply,2=Divide]
  LSTRRPER BCD*5.5 Last Rev. Recognition Percentage
  PRFTLOSSSR BCD*10.3 Recognized Profit / Loss
  PRFTLOSSHM BCD*10.3 Recognized Profit / Loss
  REVESTDATE Date Last Revised Posting Date
  ONRW Boolean On RR Worksheet
  OLABEMHM BCD*10.3 Original Employee Labor
  CLABEMHM BCD*10.3 Current Employee Labor
  ALABEMHM BCD*10.3 Actual Employee Labor
  OOHEMHM BCD*10.3 Original Employee Overhead
  COHEMHM BCD*10.3 Current Employee Overhead
  AOHEMHM BCD*10.3 Actual Employee Overhead
  OOHEQHM BCD*10.3 Original Equipment Overhead
  COHEQHM BCD*10.3 Current Equipment Overhead
  AOHEQHM BCD*10.3 Actual Equipment Overhead
  OOHSUHM BCD*10.3 Original Subcontractor Overhead
  COHSUHM BCD*10.3 Current Subcontractor Overhead
  AOHSUHM BCD*10.3 Actual Subcontractor Overhead
  OOHOHHM BCD*10.3 Original Overhead Overhead
  COHOHHM BCD*10.3 Current Overhead Overhead
  AOHOHHM BCD*10.3 Actual Overhead Overhead
  OOHMIHM BCD*10.3 Original Miscellaneous Overhead
  COHMIHM BCD*10.3 Current Miscellaneous Overhead
  AOHMIHM BCD*10.3 Actual Miscellaneous Overhead
  OOHMAHM BCD*10.3 Original Material Overhead
  COHMAHM BCD*10.3 Current Material Overhead
  AOHMAHM BCD*10.3 Actual Material Overhead
  CDATEFROM Date Current Start Date
  PROJSTYLE Integer ^2 Style [1=Standard,2=Basic]
  APTAXEXPHM BCD*10.3 Reserved
  APTAXRECHM BCD*10.3 Reserved
  APTAXEXCHM BCD*10.3 Reserved
  APDISCHM BCD*10.3 Reserved
  APINTHM BCD*10.3 Reserved
  ARTAXHM BCD*10.3 Reserved
  ARTAXSR BCD*10.3 Reserved
  ARDISCHM BCD*10.3 Reserved
  ARDISCSR BCD*10.3 Reserved
  ARINTHM BCD*10.3 Reserved
  ARINTSR BCD*10.3 Reserved
  ARWRITEHM BCD*10.3 Reserved
  ARWRITESR BCD*10.3 Reserved
  PLCODE String*16 Reserved
  BILLAMTC BCD*10.3 Current Billings (AR and on BW)
  POCOSTHM BCD*10.3 Committed P/O Cost
  POOHHM BCD*10.3 Committed P/O Overhead
  POLABORHM BCD*10.3 Committed P/O Labor
  POTCOSTHM BCD*10.3 Committed P/O Total Cost
  POEMQTY BCD*10.5 P/O Employee Quantity
  POEMOHHM BCD*10.3 P/O Employee Overhead
  POEMLABHM BCD*10.3 P/O Employee Labor
  POEMTCOSTH BCD*10.3 P/O Employee Total Cost
  POEQQTY BCD*10.5 P/O Equipment Quantity
  POEQOHHM BCD*10.3 P/O Equipment Overhead
  POEQTCOSTH BCD*10.3 P/O Equipment Total Cost
  POSUQTY BCD*10.5 P/O Subcontractor Quantity
  POSUOHHM BCD*10.3 P/O Subcontractor Overhead
  POSUTCOSTH BCD*10.3 P/O Subcontractor Total Cost
  POOHQTY BCD*10.5 P/O Overhead Quantity
  POOHOHHM BCD*10.3 P/O Overhead Overhead
  POOHTCOSTH BCD*10.3 P/O Overhead Total Cost
  POMIQTY BCD*10.5 P/O Miscellaneous Quantity
  POMIOHHM BCD*10.3 P/O Miscellaneous Overhead
  POMITCOSTH BCD*10.3 P/O Miscellaneous Total Cost
  POMAQTY BCD*10.5 P/O Material Quantity
  POMAOHHM BCD*10.3 P/O Material Overhead
  POMATCOSTH BCD*10.3 P/O Material Total Cost
  VALUES Long Optional Fields
  CLEARED Integer Transactions have been cleared [0=No,1=Yes]
  CODETAXGRP String*12 Tax Group
  CTCLASS1 Integer Customer Tax Class 1
  CTCLASS2 Integer Customer Tax Class 2
  CTCLASS3 Integer Customer Tax Class 3
  CTCLASS4 Integer Customer Tax Class 4
  CTCLASS5 Integer Customer Tax Class 5
  CTAUTH1 String*12 Customer Tax Authority 1
  CTAUTH2 String*12 Customer Tax Authority 2
  CTAUTH3 String*12 Customer Tax Authority 3
  CTAUTH4 String*12 Customer Tax Authority 4
  CTAUTH5 String*12 Customer Tax Authority 5
  LUPDATE Date Last US Payroll Posting Date
  LCPDATE Date Last Canadian Payroll Posting Date
  STRDCOSTHM BCD*10.3 Stored Cost
  STRDBILLSR BCD*10.3 Stored Billable Amount
  PRECOLEDSR BCD*10.3 Previous D + E
  STRDOHHM BCD*10.3 Overhead Amount
  STRDTCSTHM BCD*10.3 Total Stored Cost
  TXEXPCOMHM BCD*10.3 Tax (exp) Committed (func)
  TXALLCOMHM BCD*10.3 Tax (all) Committed (func)
  STRDQTY BCD*10.5 Stored Quantity
  PREAIAPAY BCD*10.3 Previous Certificates for Payment
  PRESTORED BCD*10.3 G703 Column F from Last AIA Report
  PRERETAIN BCD*10.3 G703 Column I from Last AIA Report
  IDACCTSET String*6 Account Set
  CUSTCCY String*3 Customer Currency
  CUSCONTACT String*60 Contact
  CTACTITTLE String*60 Position
  CTACPHONE String*30 Phone
  OTHERPHONE String*30 Other Phone
  CTACFAX String*30 Fax
  CTACEMAIL String*60 E-mail
  MULTICUST Integer Invoice to Multiple Customers [1=Yes,0=No]
  BILLED Integer Has this ^2 been billed?
  OESHPDATE Date Last O/E Shipment Date
  PRICEOPT Integer Default Billing Rate [1=Billing Rate,2=Use Customer Price List,3=Use Specified Price List]
  PRICELIST String*6 Price List
  OEMCHGOPT Integer O/E Miscellaneous Charges [0=Default Cost from Contract,1=Default Cost from Misc. Charges]
  ARACCTSET String*6 A/R Account Set

## PMRES - ^1 Resources (view PM0120)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+PLINENUM+CLINENUM; CTUNIQ+DNUM; CONTRACT+PROJECT+RESOURCE [D]; TYPE+CONTRACT+PROJECT+RESOURCE [D]
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 ^1 Uniq
  PLINENUM Long Project Line Number
  CLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  DETAILNUM Long ^2 Detail Number
  DATELASTMN Date Last Maintained
  DNUM Long Detail Number
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24
  ITEMNO String*24 Unformatted Item Number
  LOCATION String*6 Location
  NAME String*60 Name
  COMMENT String*60 Description
  ORJQTY BCD*10.5 Quantity
  CURQTY BCD*10.5 Current Quantity Estimate
  ACTQTY BCD*10.5 Actual Quantity
  ORJCOSTSR BCD*10.3 Reserved
  ORJCOSTHM BCD*10.3 Extended Cost
  CURCOSTSR BCD*10.3 Reserved
  CURCOSTHM BCD*10.3 Current Cost Estimate
  ACTCOSTSR BCD*10.3 Reserved
  ACTCOSTHM BCD*10.3 Actual Cost
  ORJOHSR BCD*10.3 Reserved
  ORJOHHM BCD*10.3 Original Overhead Estimate
  CUROHSR BCD*10.3 Reserved
  CUROHHM BCD*10.3 Current Overhead Estimate
  ACTOHSR BCD*10.3 Reserved
  ACTOHHM BCD*10.3 Actual Overhead
  ORJBILLSR BCD*10.3 Revenue
  ORJBILLHM BCD*10.3 Revenue
  CURBILLSR BCD*10.3 Current Revenue Estimate
  CURBILLHM BCD*10.3 Current Revenue Estimate
  ACTBILLSR BCD*10.3 Actual Revenue
  ACTBILLHM BCD*10.3 Actual Revenue
  ORJLABORSR BCD*10.3 Reserved
  ORJLABORHM BCD*10.3 Original Labor Amount Estimate
  CURLABORSR BCD*10.3 Reserved
  CURLABORHM BCD*10.3 Current Labor Amount Estimate
  ACTLABORSR BCD*10.3 Reserved
  ACTLABORHM BCD*10.3 Actual Labor Amount
  BILLAMT BCD*10.3 Expected Billings
  ODATEFROM Date Projected Start Date
  ODATETO Date Projected End Date
  CDATEFROM Date Current Start Date
  CDATETO Date Current End Date
  POQTY BCD*10.5 Committed P/O Quantity
  POCOSTHM BCD*10.3 Committed P/O Cost
  POOHHM BCD*10.3 Committed P/O Overhead
  POLABORHM BCD*10.3 Committed P/O Labor
  POTCOSTHM BCD*10.3 Committed P/O Total Cost
  VALUES Long Optional Fields
  TCUNITCOST Integer [0=Use Default PJC Option,1=Payroll,2=PJC Employee Setup,6=Resource Category]
  TCBILLRATE Integer [0=Use Default PJC Option,2=PJC Employee Setup,6=Resource Category]
  STRDQTY BCD*10.5 Stored Quantity
  STRDCOSTHM BCD*10.3 Stored Cost
  STRDBILLSR BCD*10.3 Stored Billable Amount
  PRECOLEDSR BCD*10.3 Previous Completed Work
  STRDOHHM BCD*10.3 Overhead Amount
  STRDTCSTHM BCD*10.3 Total Stored Cost
  TXEXPCOMHM BCD*10.3 Tax (exp) Committed (func)
  TXALLCOMHM BCD*10.3 Tax (all) Committed (func)
  PREAIAPAY BCD*10.3 Previous Certificates for Payment
  PRESTORED BCD*10.3 G703 Column F from Last AIA Report
  PRERETAIN BCD*10.3 G703 Column I from Last AIA Report

## PMRESC - ^1 Resource ^6 (view PM0121)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+PLINENUM+CLINENUM; CTUNIQ+DNUM; CONTRACT+PROJECT+RESOURCE+CATEGORY; CONTRACT+PROJECT+CATEGORY+RESOURCE; TYPE+CONTRACT+PROJECT+RESOURCE+CATEGORY [D]; TYPE+CONTRACT+PROJECT+CATEGORY+RESOURCE [D]
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 ^1 Uniq
  PLINENUM Long Project Line Number
  CLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  DETAILNUM Long ^2 Detail Number
  DATELASTMN Date Last Maintained
  PNUM Long Employee Detail Number
  DNUM Long Detail Number
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  ITEMNO String*24 Unformatted Item Number
  LOCATION String*6 Location
  CONVERSION BCD*10.6 Conversion Factor
  CATEGORY String*16 ^3
  COMMENT String*60 Description
  COSTTYPE String*10 Cost Type
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  ORJQTY BCD*10.5 Quantity
  CURQTY BCD*10.5 Current Quantity Estimate
  ACTQTY BCD*10.5 Actual Quantity
  UOM String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  ORJCOSTSR BCD*10.3 Reserved
  ORJCOSTHM BCD*10.3 Extended Cost
  CURCOSTSR BCD*10.3 Reserved
  CURCOSTHM BCD*10.3 Current Cost Estimate
  ACTCOSTSR BCD*10.3 Reserved
  ACTCOSTHM BCD*10.3 Actual Cost
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  ORJOHSR BCD*10.3 Reserved
  ORJOHHM BCD*10.3 Original Overhead Estimate
  CUROHSR BCD*10.3 Reserved
  CUROHHM BCD*10.3 Current Overhead Estimate
  ACTOHSR BCD*10.3 Reserved
  ACTOHHM BCD*10.3 Actual Overhead
  BILLRATE BCD*10.6 Billing Rate
  COSTPLUSP BCD*5.5 Cost Plus Percentage
  ORJBILLSR BCD*10.3 Revenue
  ORJBILLHM BCD*10.3 Revenue
  CURBILLSR BCD*10.3 Current Revenue Estimate
  CURBILLHM BCD*10.3 Current Revenue Estimate
  ACTBILLSR BCD*10.3 Actual Revenue
  ACTBILLHM BCD*10.3 Actual Revenue
  ARITEM String*16 A/R Item No.
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  ORJLABORSR BCD*10.3 Reserved
  ORJLABORHM BCD*10.3 Original Labor Amount Estimate
  CURLABORSR BCD*10.3 Reserved
  CURLABORHM BCD*10.3 Current Labor Amount Estimate
  ACTLABORSR BCD*10.3 Reserved
  ACTLABORHM BCD*10.3 Actual Labor Amount
  TORJCOSTSR BCD*10.3 Reserved
  TORJCOSTHM BCD*10.3 Original Total Cost
  TCURCOSTSR BCD*10.3 Reserved
  TCURCOSTHM BCD*10.3 Current Total Cost
  TACTCOSTSR BCD*10.3 Reserved
  TACTCOSTHM BCD*10.3 Actual Total Cost
  ADJUNITCST BCD*10.6 Reserved
  COSTSEQNUM Long Reserved
  COSTDATE Date Reserved
  STOCKITEM Boolean Reserved
  BILLAMT BCD*10.3 Expected Billings
  OOHTYPE Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OOHRATE BCD*10.6 Overhead Rate
  OOHPER BCD*5.5 Overhead Percentage
  COHTYPE Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  COHRATE BCD*10.6 Overhead Rate
  COHPER BCD*5.5 Overhead Percentage
  OLABORTYPE Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  OLABORRATE BCD*10.6 Labor Rate
  OLABORPER BCD*5.5 Labor Percentage
  CLABORTYPE Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  CLABORRATE BCD*10.6 Labor Rate
  CLABORPER BCD*5.5 Labor Percentage
  OUNITCOST BCD*10.6 Original Unit Cost
  OBILLRATE BCD*10.6 Original Billing Rate
  OCOSTPLUSP BCD*5.5 Original Cost Plus Percentage
  CUNITCOST BCD*10.6 Current Unit Cost
  CBILLRATE BCD*10.6 Current Billing Rate
  CCOSTPLUSP BCD*5.5 Current Cost Plus Percentage
  ICUOM String*10 ^7
  ODATEFROM Date Projected Start Date
  ODATETO Date Projected End Date
  CDATEFROM Date Current Start Date
  CDATETO Date Current End Date
  POQTY BCD*10.5 Committed P/O Quantity
  POCOSTHM BCD*10.3 Committed P/O Cost
  POOHHM BCD*10.3 Committed P/O Overhead
  POLABORHM BCD*10.3 Committed P/O Labor
  POTCOSTHM BCD*10.3 Committed P/O Total Cost
  TCUNITCOST Integer Default Unit Cost From [0=Use Default PJC Option]
  TCBILLRATE Integer Default Billing Rate From [0=Use Default PJC Option]
  PAYTYPE Integer [3=None,1=US Payroll,2=Canadian Payroll]
  STRDQTY BCD*10.5 Stored Quantity
  STRDCOSTHM BCD*10.3 Stored Cost
  STRDBILLSR BCD*10.3 Stored Billable Amount
  PRECOLEDSR BCD*10.3 Previous D + E
  STRDOHHM BCD*10.3 Overhead Amount
  STRDTCSTHM BCD*10.3 Total Stored Cost
  TXEXPCOMHM BCD*10.3 Tax (exp) Committed (func)
  TXALLCOMHM BCD*10.3 Tax (all) Committed (func)
  PREAIAPAY BCD*10.3 Previous Certificates for Payment
  PRESTORED BCD*10.3 G703 Column F from Last AIA Report
  PRERETAIN BCD*10.3 G703 Column I from Last AIA Report

## PMRESO - Resource Optional Field (view PM0853)
Keys (first = PK; D=dups allowed, M=modifiable): CTUNIQ+PLINENUM+CLINENUM+OPTFIELD; OPTFIELD+CTUNIQ+PLINENUM+CLINENUM [D]; CONTRACT+PROJECT+RESOURCE+OPTFIELD [D]
Fields (NAME type description [values]):
  CTUNIQ BCD*10.0 Contract Uniq
  PLINENUM Long Project Line Number
  CLINENUM Long Category Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  RESOURCE String*24 Resource
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMREVDAO - Revise Estimates Audit Detail OF (view PM0551)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO+OPTFIELD; OPTFIELD+POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMREVDO - Revise Estimates Detail Opt. Fld (view PM0550)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMROD - Reopen Worksheet Detail (view PM0202)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM; SEQ+DDETAIL [D,M]; SEQ+FMTCONTNO+PROJECT [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DDETAIL Long Detail Number
  FMTCONTNO String*16 ^1
  PROJECT String*16 ^2
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  ACCTMETD Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  CCY String*3 Currency
  TDEBIT BCD*10.3 Total Debits
  TCREDIT BCD*10.3 Total Credits
  VALUES Long Optional Fields
  GLDDESC String*60 G/L Detail Reference
  GLDREF String*60 G/L Detail Description
  GLCOMMENT String*250 G/L Detail Comment

## PMRODA - Reopen Worksheet Detail Audit (view PM0206)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM; SEQ+DDETAIL [D,M]; SEQ+FMTCONTNO+PROJECT [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DDETAIL Long Detail Number
  FMTCONTNO String*16 ^1
  PROJECT String*16 ^2
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  ACCTMETD Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  CCY String*3 Currency
  TDEBIT BCD*10.3 Total Debits
  TCREDIT BCD*10.3 Total Credits
  VALUES Long Optional Fields
  GLDDESC String*60 G/L Detail Reference
  GLDREF String*60 G/L Detail Description
  GLCOMMENT String*250 G/L Detail Comment

## PMRODD - Reopen Worksheet Accounts (view PM0204)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM+DDLINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Line Number
  DDLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DDETAIL Long Detail Number
  DDDETAIL Long Detail Number
  CATEGORY String*16 ^3
  ACCT String*45 Account
  AMTSR BCD*10.3 Amount
  AMTHM BCD*10.3 Amount
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  CCY String*3 Currency
  TYPE Integer Description [1=Revenue Recognition,101=Revenue Recognition,2=Revenue Recognition,102=Revenue Recognition,3=Revenue Recognition,103=Revenue Recognition,4=Revenue Recognition,104=Revenue Recognition,5=Revenue Recognition,6=Revenue Recognition,51=Closing Entry,151=Closing Entry,52=Closing Entry,152=Closing Entry,53=Closing Entry,153=Closing Entry,54=Closing Entry,154=Closing Entry,55=Closing Entry,56=Closing Entry]

## PMRODDA - Reopen Worksheet Accounts Audit (view PM0208)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM+DDLINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Line Number
  DDLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DDETAIL Long Detail Number
  DDDETAIL Long Detail Number
  CATEGORY String*16 ^3
  ACCT String*45 Account
  AMTSR BCD*10.3 Amount
  AMTHM BCD*10.3 Amount
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  CCY String*3 Currency
  TYPE Integer Description [1=Revenue Recognition,101=Revenue Recognition,2=Revenue Recognition,102=Revenue Recognition,3=Revenue Recognition,103=Revenue Recognition,4=Revenue Recognition,104=Revenue Recognition,51=Closing Entry,151=Closing Entry,52=Closing Entry,152=Closing Entry,53=Closing Entry,153=Closing Entry,54=Closing Entry,154=Closing Entry]

## PMRODO - Reopen Detail Optional Field (view PM0203)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM+OPTFIELD; OPTFIELD+SEQ+DLINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Timecard Expenses
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMRODOA - Reopen Detail OF Audit (view PM0207)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM+OPTFIELD; OPTFIELD+SEQ+DLINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Timecard Expenses
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]

## PMROH - Reopening Projects Worksheet (view PM0201)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; WORKID
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WORKID String*30 Worksheet Number
  DESC String*60 Description
  NEXTDTL Long Next Detail Number
  JOUDATE Date Worksheet Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [0=,1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  NUMDTL Long Number of Details
  PRINTSTAT Boolean Printed [0=False,1=True]
  REVERSE Integer Reverse Entries for Completed Project Account Method ^5
  TDEBIT BCD*10.3 Total Debits
  TCREDIT BCD*10.3 Total Credits
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  DATEBUS Date Posting Date
  ENTEREDBY String*8 Entered By

## PMROHA - Reopen Worksheet Header Audit (view PM0205)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; WORKID [D]; SEQ+JOUDATE
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WORKID String*30 Worksheet Number
  DESC String*60 Description
  NEXTDTL Long Next Detail Number
  JOUDATE Date Worksheet Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [0=,1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  NUMDTL Long Number of Details
  PRINTSTAT Boolean Printed [0=False,1=True]
  REVERSE Integer Reverse Entries for Completed Project Account Method ^5
  TDEBIT BCD*10.3 Total Debits
  TCREDIT BCD*10.3 Total Credits
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  DATEBUS Date Posting Date

## PMRSTRT - Restart (view PM0610)
Keys (first = PK; D=dups allowed, M=modifiable): KEY
Fields (NAME type description [values]):
  KEY String*50 Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Data Block 1

## PMRWD - RR Worksheet Detail (view PM0092)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM; SEQ+DDETAIL [D,M]; SEQ+CONTRACT+PROJECT+CATEGORY [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DDETAIL Long Detail Number
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  ACCTMETD Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  PERCOMP BCD*5.5 Percentage Complete
  TCURCOSTHM BCD*10.3 Current Total Cost
  TCURREVSR BCD*10.3 Total Cur. Revenue Est.
  TCURREVHM BCD*10.3 Total Cur. Revenue Est.
  TRECCOSTHM BCD*10.3 Total Cost Recognized
  TRECREVSR BCD*10.3 Total Revenue Recognized
  TRECREVHM BCD*10.3 Total Revenue Recognized
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  STATUS Integer ^1 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  CCY String*3 Currency
  VALUES Long Optional Fields
  TACTCOSTHM BCD*10.3 Actual Total Cost
  GLDDESC String*60 G/L Detail Reference
  GLDREF String*60 G/L Detail Description
  GLCOMMENT String*250 G/L Detail Comment
  UNREGCOST Boolean Reserved

## PMRWDA - RR Worksheet Detail Audit (view PM0096)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM; SEQ+DDETAIL [D,M]; SEQ+CONTRACT+PROJECT+CATEGORY [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DDETAIL Long Detail Number
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  ACCTMETD Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  PERCOMP BCD*5.5 Percentage Complete
  TCURCOSTHM BCD*10.3 Current Total Cost
  TCURREVSR BCD*10.3 Total Cur. Revenue Est.
  TCURREVHM BCD*10.3 Total Cur. Revenue Est.
  TRECCOSTHM BCD*10.3 Total Cost Recognized
  TRECREVSR BCD*10.3 Total Revenue Recognized
  TRECREVHM BCD*10.3 Total Revenue Recognized
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  STATUS Integer ^1 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  CCY String*3 Currency
  VALUES Long Optional Fields
  GLDDESC String*60 G/L Detail Reference
  GLDREF String*60 G/L Detail Description
  GLCOMMENT String*250 G/L Detail Comment

## PMRWDAO - RR Detail OF Audit (view PM0547)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM+OPTFIELD; OPTFIELD+SEQ+DLINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Timecard Expenses
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMRWDD - RR Worksheet Accounts (view PM0094)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM+DDLINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Line Number
  DDLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DDETAIL Long Detail Number
  DDDETAIL Long Detail Number
  ACCT String*45 Account
  AMTSR BCD*10.3 Amount
  AMTHM BCD*10.3 Amount
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  CCY String*3 Currency
  TYPE Integer Description [1=Revenue Recognition,101=Revenue Recognition,2=Revenue Recognition,102=Revenue Recognition,3=Revenue Recognition,103=Revenue Recognition,4=Revenue Recognition,104=Revenue Recognition,5=Revenue Recognition,6=Revenue Recognition,51=Closing Entry,151=Closing Entry,52=Closing Entry,152=Closing Entry,53=Closing Entry,153=Closing Entry,54=Closing Entry,154=Closing Entry,155=Closing Entry,156=Closing Entry]

## PMRWDDA - RR Worksheet Accounts Audit (view PM0097)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM+DDLINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Line Number
  DDLINENUM Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DDETAIL Long Detail Number
  DDDETAIL Long Detail Number
  ACCT String*45 Account
  AMTSR BCD*10.3 Amount
  AMTHM BCD*10.3 Amount
  RATE BCD*8.7 Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  CCY String*3 Currency
  TYPE Integer Description [1=Revenue Recognition,101=Revenue Recognition,2=Revenue Recognition,102=Revenue Recognition,3=Revenue Recognition,103=Revenue Recognition,4=Revenue Recognition,104=Revenue Recognition,5=Revenue Recognition,6=Revenue Recognition,51=Closing Entry,151=Closing Entry,52=Closing Entry,152=Closing Entry,53=Closing Entry,153=Closing Entry,54=Closing Entry,154=Closing Entry,155=Closing Entry,156=Closing Entry]

## PMRWDO - RR Detail Optional Field (view PM0546)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+DLINENUM+OPTFIELD; OPTFIELD+SEQ+DLINENUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  DLINENUM Long Timecard Expenses
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMRWH - Revenue Recognition Worksheet (view PM0091)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; WORKID
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WORKID String*30 Worksheet Number
  DESC String*60 Description
  NEXTDTL Long Next Detail Number
  CUTBY Integer Cutoff By [0=Transaction Date,1=Fiscal Year/Period]
  CUTDATE Date Cutoff Date
  FISCALYEAR String*4 Cutoff Fiscal Year
  FISCALPER Integer Cutoff Fiscal Period [0=,1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  JOUDATE Date Worksheet Date
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  NUMDTL Long Number of Details
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  JOUYEAR String*4 Fiscal Year
  JOUPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  DATEBUS Date Posting Date
  ENTEREDBY String*8 Entered By

## PMRWHA - RR Worksheet Header Audit (view PM0095)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; WORKID [D]; SEQ+JOUDATE
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  WORKID String*30 Worksheet Number
  DESC String*60 Description
  NEXTDTL Long Next Detail Number
  CUTBY Integer Cutoff By [0=Transaction Date,1=Fiscal Year/Period]
  CUTDATE Date Cutoff Date
  FISCALYEAR String*4 Cutoff Fiscal Year
  FISCALPER Integer Cutoff Fiscal Period [0=,1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  JOUDATE Date Worksheet Date
  JOUYEAR String*4 Fiscal Year
  JOUPER Integer Fiscal Period [0=,1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  NUMDTL Long Number of Details
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  POSTDATE Date Posted On
  POSTTIME Time Posted At
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  GLHDESC String*60 G/L Entry Description
  DATEBUS Date Posting Date

## PMSEG - Segments (view PM0013)
Keys (first = PK; D=dups allowed, M=modifiable): SEGMENT
Fields (NAME type description [values]):
  SEGMENT Integer Segment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  LENGTH Integer Length
  VALIDATE Boolean Validate

## PMSEGV - Segment Codes (view PM0014)
Keys (first = PK; D=dups allowed, M=modifiable): SEGMENT+SEGVAL
Fields (NAME type description [values]):
  SEGMENT Integer Segment Name [1=None]
  SEGVAL String*16 Segment Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description

## PMSTAFF - Employee (view PM0002)
Keys (first = PK; D=dups allowed, M=modifiable): STAFFCODE
Fields (NAME type description [values]):
  STAFFCODE String*16 Employee Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*60 Name
  COMMENT String*250 Comments
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  DATEINACTV Date Date Inactive
  GROUP String*10 Group
  UNITCOST BCD*10.6 Unit Cost
  PAYRATE Integer Pay Rate [1=Hour,2=Week,3=Month,4=Annum]
  STDHOURS BCD*10.2 Default Hours
  TYPE Integer Type [1=Salary,2=Timecard,3=Contractor]
  PAYROLL String*40 Payroll Code
  BILLRATE BCD*10.6 Billing Rate
  CCY String*3 Currency
  USERID String*8 User ID
  EMAIL1 String*50 E-mail
  EMAIL2 String*50 E-mail
  PAYTYPE Integer Payroll Type [3=None,1=US Payroll,2=Canadian Payroll]
  EARNCODE String*16 Earnings Code
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  STUNITCOST Integer Unit Cost
  STTOTCOST Integer Total Cost
  STUNITBILL Integer Billing Rate
  STTOTBILL Integer Billing Amount
  STBILLTYPE Integer Billing Type
  SETOTCOST Integer Total Cost
  SETOTBILL Integer Billing Amount
  SEBILLTYPE Integer Billing Type
  VALUES Long Optional Fields

## PMSTAFFD - Employee Detail View (view PM0479)
Keys (first = PK; D=dups allowed, M=modifiable): STAFFCODE+CCY
Fields (NAME type description [values]):
  STAFFCODE String*16 Staff Code
  CCY String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PAYTYPE Integer Pay Type
  BILLRATE BCD*10.6 Billing Rate
  DESC String*60 Currency Description

## PMSTAFFO - Employee Optional Fields (view PM0511)
Keys (first = PK; D=dups allowed, M=modifiable): STAFFCODE+OPTFIELD; OPTFIELD+STAFFCODE
Fields (NAME type description [values]):
  STAFFCODE String*16 Employee Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMSTRUC - Contract Structures (view PM0011)
Keys (first = PK; D=dups allowed, M=modifiable): JOBBRKID
Fields (NAME type description [values]):
  JOBBRKID String*6 Structure Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  DELIM0 Integer Prefix [1=None,2=- Hyphen,3=/ Forward Slash,4=\ Back Slash,5=* Asterisk,6=. Period,7=( Left Parenthesis,8=) Right Parenthesis,9=# Number Sign]
  SEGMENT1 Integer Segment 1
  OFFSET1 Integer Segment 1 Offset
  LENGTH1 Integer Segment 1 Length
  VALIDATE1 Boolean Validate Segment 1
  DELIM1 Integer Segment Separator 1 [1=None,2=- Hyphen,3=/ Forward Slash,4=\ Back Slash,5=* Asterisk,6=. Period,7=( Left Parenthesis,8=) Right Parenthesis,9=# Number Sign]
  SEGMENT2 Integer Segment 2
  OFFSET2 Integer Segment 2 Offset
  LENGTH2 Integer Segment 2 Length
  VALIDATE2 Boolean Validate Segment 2
  DELIM2 Integer Segment Separator 2 [1=None,2=- Hyphen,3=/ Forward Slash,4=\ Back Slash,5=* Asterisk,6=. Period,7=( Left Parenthesis,8=) Right Parenthesis,9=# Number Sign]
  SEGMENT3 Integer Segment 3
  OFFSET3 Integer Segment 3 Offset
  LENGTH3 Integer Segment 3 Length
  VALIDATE3 Boolean Validate Segment 3
  DELIM3 Integer Segment Separator 3 [1=None,2=- Hyphen,3=/ Forward Slash,4=\ Back Slash,5=* Asterisk,6=. Period,7=( Left Parenthesis,8=) Right Parenthesis,9=# Number Sign]
  SEGMENT4 Integer Segment 4
  OFFSET4 Integer Segment 4 Offset
  LENGTH4 Integer Segment 4 Length
  VALIDATE4 Boolean Validate Segment 4
  DELIM4 Integer Segment Separator 4 [1=None,2=- Hyphen,3=/ Forward Slash,4=\ Back Slash,5=* Asterisk,6=. Period,7=( Left Parenthesis,8=) Right Parenthesis,9=# Number Sign]
  SEGMENT5 Integer Segment 5
  OFFSET5 Integer Segment 5 Offset
  LENGTH5 Integer Segment 5 Length
  VALIDATE5 Boolean Validate Segment 5
  DELIM5 Integer Segment Separator 5 [1=None,2=- Hyphen,3=/ Forward Slash,4=\ Back Slash,5=* Asterisk,6=. Period,7=( Left Parenthesis,8=) Right Parenthesis,9=# Number Sign]

## PMSUBCN - Subcontractors (view PM0026)
Keys (first = PK; D=dups allowed, M=modifiable): SUBCONT
Fields (NAME type description [values]):
  SUBCONT String*16 Subcontractor Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*60 Subcontractor Name
  DESC String*60 Description
  VENDORID String*12 Vendor Number
  INACTIVE Integer Status [0=Active,1=Inactive]
  DATELASTMN Date Last Maintained
  DATEINACTV Date Date Inactive
  ADDR1 String*60 Address
  ADDR2 String*60 Address 2
  ADDR3 String*60 Address 3
  ADDR4 String*60 Address 4
  CITY String*30 City
  STATE String*30 State/Prov.
  ZIP String*20 Zip/Postal Code
  COUNTRY String*30 Country
  CONTACT String*60 Contact
  PHONE String*30 Telephone
  FAX String*30 Fax
  EMAIL1 String*50 Contact's E-mail
  EMAIL2 String*50 Vendor's E-mail
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  SCHCODE String*12 Schedule Code
  VALUES Long Optional Fields

## PMSUBCND - Subcontractors Detail View (view PM0477)
Keys (first = PK; D=dups allowed, M=modifiable): SUBCONT+CCY
Fields (NAME type description [values]):
  SUBCONT String*16 Subcontractor Code
  CCY String*3 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ARITEM String*16 AR Item
  UOM String*10 AR UOM
  UNITCOST BCD*10.6 Unit Cost
  BILLRATE BCD*10.6 Billing Rate
  DESC String*60 Currency Description

## PMSUBCNO - Subcontractor Optional Fields (view PM0515)
Keys (first = PK; D=dups allowed, M=modifiable): SUBCONT+OPTFIELD; OPTFIELD+SUBCONT
Fields (NAME type description [values]):
  SUBCONT String*16 Subcontractor Code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMTIMDA - Timecard Time Detail Audit (view PM0043)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM; TIMECARDNO+DETAILNUM [D]
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  TIMECARDNO String*16 Timecard Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  DETAILNUM Long Detail Number
  EARNINGS String*16 Earnings Code
  DESC String*60 Description
  TDATE Date Transaction Date
  TIMETYPE Integer Time Type
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  STARTTIME Time Start Time
  ENDTIME Time End Time
  QUANTITY BCD*10.2 Quantity
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  ESTBILLCCY Integer Revenue And Cost Currency [1=Revenue and Costs in Functional Currency,2=Revenue in Customer Currency,3=Revenue and Costs in Customer Currency]
  COSTCCY String*3 Cost Currency
  BILLCCY String*3 Billing Currency
  UNITCOST BCD*10.6 Unit Cost
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  LABACCT String*45 Labor Account
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  LABORSR BCD*10.3 Transaction Labor Amount
  LABORHM BCD*10.3 Transaction Labor Amount
  OHACCT String*45 Overhead Account
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Transaction Overhead Amount
  OHHM BCD*10.3 Transaction Overhead Amount
  BILLRATE BCD*10.6 Billing Rate
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  PAYRACCT String*45 Payroll Account
  WIPACCT String*45 Work in Progress Account
  COMMENTS String*250 Comments
  FIXEDBILL Integer Bill Amount Based On [1=Invoice This Amount,2=Invoice Based on Exchange Rate]
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Override [0=False,1=True]
  RATESPREAD BCD*8.7 Rate Spread
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  ADJUSTED Integer
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment
  RESOURCE String*24 Resource

## PMTIMDAO - Timecard Audit Detail OF (view PM0533)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO+OPTFIELD; OPTFIELD+POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Integer Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMTIMDO - Timecard Detail Optional Field (view PM0531)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Integer Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMTIMEA - Timecard Expense Detail Audit (view PM0114)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM; TIMECARDNO+DETAILNUM [D]
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  TIMECARDNO String*16 Timecard Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  DETAILNUM Long Detail Number
  EXPENSE String*16 Expense Code
  DESC String*60 Description
  TDATE Date Transaction Date
  EXPTYPE Integer Expense Type
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  QUANTITY BCD*10.2 Quantity
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  COSTCCY String*3 Cost Currency
  BILLCCY String*3 Billing Currency
  UNITCOST BCD*10.6 Unit Cost
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  LABACCT String*45 Labor Account
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  LABORSR BCD*10.3 Transaction Labor Amount
  LABORHM BCD*10.3 Transaction Labor Amount
  OHACCT String*45 Overhead Account
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Transaction Overhead Amount
  OHHM BCD*10.3 Transaction Overhead Amount
  BILLRATE BCD*10.6 Billing Rate
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  EXPACCT String*45 Employee Expense Account
  WIPACCT String*45 Work in Progress Account
  COMMENTS String*250 Comments
  CRATE BCD*8.7 Exchange Rate
  CRATETYPE String*2 Rate Type
  CRATEDATE Date Rate Date
  CRATEOP Integer Rate Operator
  CRATEOVER Boolean Rate Override
  FIXEDBILL Integer Bill Amount Based On [1=Invoice This Amount,2=Invoice Based on Exchange Rate]
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Override [0=False,1=True]
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  ADJUSTED Integer
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment
  RESOURCE String*24 Resource
  TYPE Integer Cost Class

## PMTIMEAO - Timecard Audit Expense OF (view PM0540)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO+OPTFIELD; OPTFIELD+POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Integer Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMTIMED - Timecard Time Detail (view PM0041)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; TIMECARDNO+LINENO; SEQ+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TIMECARDNO String*16 Timecard Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  DETAILNUM Long Detail Number
  EARNINGS String*16 Earnings Code
  DESC String*60 Description
  TDATE Date Transaction Date
  TIMETYPE Integer Time Type [1=Hour,2=Vacation,3=Sick]
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  STARTTIME Time Start Time
  ENDTIME Time End Time
  QUANTITY BCD*10.2 Hours
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  ESTBILLCCY Integer Revenue And Cost Currency [1=Revenue and Costs in Functional Currency,2=Revenue in Customer Currency,3=Revenue and Costs in Customer Currency]
  COSTCCY String*3 Cost Currency
  BILLCCY String*3 Billing Currency
  UNITCOST BCD*10.6 Unit Cost
  EXTCOSTSR BCD*10.3 Extended Cost
  EXTCOSTHM BCD*10.3 Extended Cost
  EXTBILLSR BCD*10.3 Extended Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  LABORSR BCD*10.3 Transaction Labor Amount
  LABORHM BCD*10.3 Transaction Labor Amount
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Transaction Overhead Amount
  OHHM BCD*10.3 Transaction Overhead Amount
  BILLRATE BCD*10.6 Billing Rate
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Total Billable Amount
  PAYRACCT String*45 Payroll Account
  WIPACCT String*45 Work In Progress Account
  OHACCT String*45 Overhead Account
  LABORACCT String*45 Labor Account
  COMMENTS String*250 Comments
  FIXEDBILL Integer Bill Amount Based On [1=Invoice This Amount,2=Invoice Based on Exchange Rate]
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment
  RESOURCE String*24 Resource

## PMTIMEE - Timecard Expense Detail (view PM0113)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; TIMECARDNO+LINENO; SEQ+DETAILNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TIMECARDNO String*16 Timecard Number
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  DETAILNUM Long Detail Number
  EXPENSE String*16 Expense Code
  DESC String*60 Description
  TDATE Date Transaction Date
  EXPTYPE Integer Expense Type [1=Airfares,2=Accommodation,3=Meals,4=Entertainment,5=Taxi/Hire Car,6=Tolls,7=Telephone,8=Parking,9=Other]
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  QUANTITY BCD*10.2 Quantity
  ARITEM String*16 A/R Item No.
  UOM String*10 Unit of Measure
  COSTCCY String*3 Cost Currency
  BILLCCY String*3 Billing Currency
  UNITCOST BCD*10.6 Cost Amount
  EXTCOSTSR BCD*10.3 Cost Amount
  EXTCOSTHM BCD*10.3 Cost Amount
  EXTBILLSR BCD*10.3 Billing Amount
  EXTBILLHM BCD*10.3 Reserved
  LABOR Integer Reserved [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Reserved
  LABORPER BCD*5.5 Reserved
  LABORSR BCD*10.3 Reserved
  LABORHM BCD*10.3 Reserved
  OVERHD Integer Reserved [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Reserved
  HEADPER BCD*5.5 Reserved
  OHSR BCD*10.3 Reserved
  OHHM BCD*10.3 Reserved
  BILLRATE BCD*10.6 Billing Amount
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable Amount
  TOTBILLHM BCD*10.3 Reserved
  EXPACCT String*45 Employee Expense Account
  WIPACCT String*45 WIP/COS Account
  OHACCT String*45 Reserved
  LABORACCT String*45 Reserved
  COMMENTS String*250 Comments
  FIXEDBILL Integer Bill Amount Based On
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  VALUES Long Optional Fields
  GLDDESC String*60 G/L Detail Description
  GLDREF String*60 G/L Detail Reference
  GLCOMMENT String*250 G/L Detail Comment
  RESOURCE String*24 Resource
  TYPE Integer Cost Class [1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESDESC String*60

## PMTIMEH - Timecard (view PM0040)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; TIMECARDNO; STAFFCODE+TIMECARDNO; TRANSTAT+TIMECARDNO; COMPLETE+TIMECARDNO [M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TIMECARDNO String*16 Timecard Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  STAFFCODE String*24 Employee Number
  NAME String*60 Name
  REFERENCE String*60 Reference
  DESC String*60 Description
  BEGINDATE Date Start Date
  ENDDATE Date End Date
  EXTCOSTSR BCD*10.3 Total Cost
  EXTCOSTHM BCD*10.3 Total Cost
  OHSR BCD*10.3 Transaction Overhead Amount
  OHHM BCD*10.3 Transaction Overhead Amount
  LABORSR BCD*10.3 Transaction Labor Amount
  LABORHM BCD*10.3 Transaction Labor Amount
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable
  TOTBILLHM BCD*10.3 Total Billable
  TOTQTY BCD*10.2 Total Hours
  ETOTCOSTSR BCD*10.3 Total Expense Cost
  ETOTCOSTHM BCD*10.3 Total Expense Cost
  ETOTBILLSR BCD*10.3 Total Expense Billable
  ETOTBILLHM BCD*10.3 Total Expense Billable
  ETOTQTY BCD*10.2 Total Expense Quantity
  GTOTCOSTSR BCD*10.3 Total Cost
  GTOTCOSTHM BCD*10.3 Total Cost
  GTOTBILLSR BCD*10.3 Total Billable Amount
  GTOTBILLHM BCD*10.3 Total Billable Amount
  CCY String*3 Staff Currency
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATESPREAD BCD*8.7 Rate Spread
  COMPLETE Integer Status [0=New,10=Entered,20=Ready For Approval,30=Approved,40=Posted]
  PRINTSTAT Boolean Print Status [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  NEXTDTLNUM Long Next Detail Number
  PAYTYPE Integer Payroll Type [3=None,1=US Payroll,2=Canadian Payroll]
  NUMDTL Long Number of Details
  HMON BCD*10.2 Monday Hours
  HTUE BCD*10.2 Tuesday Hours
  HWED BCD*10.2 Wednesday Hours
  HTHU BCD*10.2 Thursday Hours
  HFRI BCD*10.2 Friday Hours
  HSAT BCD*10.2 Saturday Hours
  HSUN BCD*10.2 Sunday Hours
  HWEEK BCD*10.2 Weekly Hours
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMTIMEO - Timecard Expense Optional Field (view PM0539)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO+OPTFIELD; OPTFIELD+SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Integer Line Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMTIMET - Timecard Time Totals (view PM0115)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  HMON BCD*10.2 Monday Hours
  HTUE BCD*10.2 Tuesday Hours
  HWED BCD*10.2 Wednesday Hours
  HTHU BCD*10.2 Thursday Hours
  HFRI BCD*10.2 Friday Hours
  HSAT BCD*10.2 Saturday Hours
  HSUN BCD*10.2 Sunday Hours
  HWEEK BCD*10.2 Weekly Hours
  NLMON Long Number of details - Monday
  NLTUE Long Number of details - Tuesday
  NLWED Long Number of details - Wednesday
  NLTHU Long Number of details - Thursday
  NLFRI Long Number of details - Friday
  NLSAT Long Number of details - Saturday
  NLSUN Long Number of details - Sunday
  DMON Long DETAILNUM - Monday
  DTUE Long DETAILNUM - Tuesday
  DWED Long DETAILNUM - Wednesday
  DTHU Long DETAILNUM - Thursday
  DFRI Long DETAILNUM - Friday
  DSAT Long DETAILNUM - Saturday
  DSUN Long DETAILNUM - Sunday
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  EARNINGS String*16 Earnings Code

## PMTIMHA - Timecard Audit (view PM0042)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; SEQ+POSTSEQNO; PAYUPDATED+TRANSDATE [D,M]; PAYUPDATED+PAYTYPE+ENDDATE [D,M]; TIMECARDNO [D]
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  POSTDATE Date Posting Date
  TIMECARDNO String*16 Time Card Number
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  STAFFCODE String*16 Employee Number
  NAME String*60 Name
  REFERENCE String*60 Reference
  DESC String*60 Description
  BEGINDATE Date Begin Date
  ENDDATE Date End Date
  TOTCOSTSR BCD*10.3 Total Cost
  TOTCOSTHM BCD*10.3 Total Cost
  TOTBILLSR BCD*10.3 Total Billable
  TOTBILLHM BCD*10.3 Total Billable
  TOTQTY BCD*10.2 Total Quantity
  ETOTCOSTSR BCD*10.3 Expenses Total Cost
  ETOTCOSTHM BCD*10.3 Expenses Total Cost
  ETOTBILLSR BCD*10.3 Expenses Total Billable
  ETOTBILLHM BCD*10.3 Expenses Total Billable
  ETOTQTY BCD*10.2 Expenses Total Quantity
  CCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATESPREAD BCD*8.7 Rate Spread
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  PAYUPDATED Boolean Payroll Updated ?
  PAYROLLTC String*6 Payroll Timecard Number
  PAYTYPE Integer Payroll Type [3=None,1=US Payroll,2=Canadian Payroll]
  HMON BCD*10.2 Monday Hours
  HTUE BCD*10.2 Tuesday Hours
  HWED BCD*10.2 Wednesday Hours
  HTHU BCD*10.2 Thursday Hours
  HFRI BCD*10.2 Friday Hours
  HSAT BCD*10.2 Saturday Hours
  HSUN BCD*10.2 Sunday Hours
  HWEEK BCD*10.2 Weekly Hours
  VALUES Long Optional Fields
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  GLHDESC String*60 G/L Entry Description
  DATEBUS Date Posting Date

## PMTIMHAO - Timecard Audit Optional Field (view PM0534)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+OPTFIELD; OPTFIELD+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMTIMHO - Timecard Optional Field (view PM0532)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+OPTFIELD; OPTFIELD+SEQ
Fields (NAME type description [values]):
  SEQ Long Sequence
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMTIMTA - Timecard Time Audit (view PM0117)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Long Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  HMON BCD*10.2 Monday Hours
  HTUE BCD*10.2 Tuesday Hours
  HWED BCD*10.2 Wednesday Hours
  HTHU BCD*10.2 Thursday Hours
  HFRI BCD*10.2 Friday Hours
  HSAT BCD*10.2 Saturday Hours
  HSUN BCD*10.2 Sunday Hours
  HWEEK BCD*10.2 Weekly Hours
  NLMON Long Number of details - Monday
  NLTUE Long Number of details - Tuesday
  NLWED Long Number of details - Wednesday
  NLTHU Long Number of details - Thursday
  NLFRI Long Number of details - Friday
  NLSAT Long Number of details - Saturday
  NLSUN Long Number of details - Sunday
  DMON Long DETAILNUM - Monday
  DTUE Long DETAILNUM - Tuesday
  DWED Long DETAILNUM - Wednesday
  DTHU Long DETAILNUM - Thursday
  DFRI Long DETAILNUM - Friday
  DSAT Long DETAILNUM - Saturday
  DSUN Long DETAILNUM - Sunday
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  CUSTOMER String*12 Customer
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]

## PMTRAN - ^1 Transactions (view PM0111)
Keys (first = PK; D=dups allowed, M=modifiable): CONTRACT+PROJECT+CATEGORY+RESOURCE+TRANSNUM; CONTRACT+PROJECT+CATEGORY+TRANSDATE [D,M]; CONTRACT+PROJECT+CATEGORY+RRCOMPLETE+TRANSDATE [D,M]; CONTRACT+PROJECT+CATEGORY+RRCOMPLETE+FISCALYEAR+FISCALPER [D,M]; CONTRACT+PROJECT+CATEGORY+RESOURCE+TRANSREF [D,M]; RRWORKID [D,M]; RRCOMPLETE+CONTRACT+PROJECT+TRANSDATE [D,M]; COSTREV+INVTYPE+BILLED+IDCUST+CONTRACT+PROJECT+CATEGORY+RESOURCE+TRANSDATE [D,M]; BILLED+BILLTYPE+IDCUST+CONTRACT+PROJECT+CATEGORY+RESOURCE+TRANSDATE [D,M]; BILLED+CONTRACT+PROJECT+CATEGORY+RESOURCE [D,M]
Fields (NAME type description [values]):
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  RESOURCE String*24 Resource
  TRANSNUM Long Transaction Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PROJTYPE Integer Project Type [0=None,1=Time and Materials,2=Fixed Price,3=Cost Plus]
  TRANSDATE Date Transaction Date
  DATELASTMN Date Last Maintained
  FMTCONTNO String*16 ^1
  IDCUST String*12 Customer Number
  VENDORID String*12 Vendor
  DOCNUM String*24 Document Number
  DOCDATE Date Document Date
  MODULE String*4 Source Module
  DOCTYPE Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest,5=Prepayment,6=Unapplied Cash,7=Material Usage,8=Material Return,9=Equipment Usage,10=Timecard,11=Charges,12=Adjustment,13=Retainage Invoice,14=Retainage Credit Note,15=Retainage Debit Note,16=Purchase Order,17=P/O Receipt,18=P/O Return,19=P/O Invoice,20=P/O Credit Note,21=P/O Debit Note,22=Opening Balance,23=Manual Check,24=Cost,25=Check Reversal,26=Material Internal Usage,27=Order Entry,28=O/E Shipment,29=O/E Invoice,30=O/E Debit Note,31=O/E Credit Note]
  TRANSTYPE Integer Transaction Type [1=Posted,2=Discount,3=Write-off,4=Apply From,5=Apply To,6=Payment/Receipt Reversal,7=Rounding (multicurrency),8=Exchange Gain/Loss,9=Unrealized Exchange Gain/Loss,10=Adjustment,11=Receipt/Payment,20=Retainage Rounding,21=Retainage Exchange Gain/Loss,22=Retainage Unrealized Exchange Gain/Loss,23=Opening Retainage Receivable,24=Opening Retainage Payable,25=Invoice Retainage Receivable,26=Invoice Retainage Payable,28=Opening Balance Reversal,29=Refund,30=Refund Reversal,31=Exchange Gain/Loss,32=Retainage Gain/Loss]
  COSTREV Integer Cost or Revenue [1=Cost,2=Revenue,3=Other]
  REFDOC String*24 Reference Document
  DTEBTCH Date Batch Date
  CNTBTCH BCD*5.0 Batch Number
  CNTENT BCD*4.0 Batch Entry Number
  CNTLINE BCD*3.0 Batch Line Number
  REFERENCE String*60 Document Reference
  DESC String*60 Document Description
  POSTSEQ Long Posting Sequence
  CCY String*3 Currency Code
  RATETYPE String*2 Rate Type Code
  RATEOVER Boolean Rate Override [0=False,1=True]
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  RATE BCD*8.7 Exchange Rate
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  BILLED Integer Has The Cost Component Been Billed [1=Not Billed,2=Selected for Processing,3=Invoice Created,4=Posted,5=Deleted,6=Moved,7=On Hold]
  QUANTITY BCD*10.5 Transaction Quantity
  CONVERSION BCD*10.6 Conversion Factor
  ICUOM String*10 ^7
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  BILLTYPE Integer Billing Type [2=Billable,3=No Charge,1=Non-billable]
  FIXEDBILL Integer Bill Amount Based On [1=Invoice This Amount,2=Invoice Based on Exchange Rate]
  EXPTYPE Integer Timecard Expense Type [0=N/A,1=Airfares,2=Accommodation,3=Meals,4=Entertainment,5=Taxi/Hire Car,6=Tolls,7=Telephone,8=Parking,9=Other]
  UNITRATE BCD*10.6 Unit Rate
  EXTAMTSR BCD*10.3 Extended Amount (Source)
  EXTAMTHM BCD*10.3 Extended Amount (Functional)
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  LABORSR BCD*10.3 Source Labor Amount
  LABORHM BCD*10.3 Functional Labor Amount
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  OHSR BCD*10.3 Source Overhead Amount
  OHHM BCD*10.3 Functional Overhead Amount
  COSTPLUS BCD*5.5 Cost Plus Percentage
  TOTAMTSR BCD*10.3 Srce. Total Amount Excl. Tax
  TOTAMTHM BCD*10.3 Func. Total Amount Excl. Tax
  TAXAMTSR BCD*10.3 Tax Amount (Source)
  TAXAMTHM BCD*10.3 Tax Amount (Functional)
  TAMTSR BCD*10.3 Srce. Total Amount Inc. Tax
  TAMTHM BCD*10.3 Func. Total Amount Inc. Tax
  RRCOMPLETE Integer Has Revenue Recognition Been Run [1=Not Processed,2=Selected for Processing,3=Posted]
  RCPAMTSR BCD*10.3 Amount Received (Source)
  RCPAMTHM BCD*10.3 Amount Received (Functional)
  PAYAMTSR BCD*10.3 Amount Paid (Source)
  PAYAMTHM BCD*10.3 Amount Paid
  USERID String*8 User ID
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Tax Class 1
  TCLASS2 Integer Tax Class 2
  TCLASS3 Integer Tax Class 3
  TCLASS4 Integer Tax Class 4
  TCLASS5 Integer Tax Class 5
  TICLASS1 Integer Item Tax Class 1
  TICLASS2 Integer Item Tax Class 2
  TICLASS3 Integer Item Tax Class 3
  TICLASS4 Integer Item Tax Class 4
  TICLASS5 Integer Item Tax Class 5
  TINCLUDED1 Boolean Tax Included 1
  TINCLUDED2 Boolean Tax Included 2
  TINCLUDED3 Boolean Tax Included 3
  TINCLUDED4 Boolean Tax Included 4
  TINCLUDED5 Boolean Tax Included 5
  TAXBASES1 BCD*10.3 Tax Base 1 (Source)
  TAXBASES2 BCD*10.3 Tax Base 2 (Source)
  TAXBASES3 BCD*10.3 Tax Base 3 (Source)
  TAXBASES4 BCD*10.3 Tax Base 4 (Source)
  TAXBASES5 BCD*10.3 Tax Base 5 (Source)
  TAXBASEH1 BCD*10.3 Tax Base 1 (Functional)
  TAXBASEH2 BCD*10.3 Tax Base 2 (Functional)
  TAXBASEH3 BCD*10.3 Tax Base 3 (Functional)
  TAXBASEH4 BCD*10.3 Tax Base 4 (Functional)
  TAXBASEH5 BCD*10.3 Tax Base 5 (Functional)
  TAXAMTS1 BCD*10.3 Tax Amount 1 (Source)
  TAXAMTS2 BCD*10.3 Tax Amount 2 (Source)
  TAXAMTS3 BCD*10.3 Tax Amount 3 (Source)
  TAXAMTS4 BCD*10.3 Tax Amount 4 (Source)
  TAXAMTS5 BCD*10.3 Tax Amount 5 (Source)
  TAXAMTH1 BCD*10.3 Tax Amount 1 (Functional)
  TAXAMTH2 BCD*10.3 Tax Amount 2 (Functional)
  TAXAMTH3 BCD*10.3 Tax Amount 3 (Functional)
  TAXAMTH4 BCD*10.3 Tax Amount 4 (Functional)
  TAXAMTH5 BCD*10.3 Tax Amount 5 (Functional)
  RTAXAMTSR BCD*10.3 Recoverable Tax (Source)
  RTAXAMTHM BCD*10.3 Recoverable Tax (Functional)
  CVAMT BCD*10.3 Cost Variance Amount
  WIPACCT String*45 WIP/COS Account
  TRANACCT String*45 Transaction Account
  LABORACCT String*45 Labor Account
  OHACCT String*45 Overhead Account
  REVACCT String*45 Revenue Account
  CVACCT String*45 Cost Variance Account
  ARITEM String*16 A/R Item No.
  ARUOM String*10 A/R Unit of Measure
  TRANSREF Long Transaction Reference
  OTHERREF Long Cost/Revenue TRANSNUM
  COMMENTS String*250 Comments
  TYPE Integer Cost Class [0=None,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  TRANSQTY BCD*10.5 Quantity
  RRWORKID String*30 RR Worksheet Number
  BWWORKID String*30 Billing Worksheet Number
  TAMTRETSR BCD*10.3 Source Retainage Amount
  TAMTRETHM BCD*10.3 Functional Retainage Amount
  RETDUEDT Date Retainage Due Date
  ORIGDOC String*24 Original Document Number
  REVREC Integer Accounting Method [1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,8=Accrual-Basis]
  INVTYPE Integer Invoice Type [1=Item,2=Summary]
  DAYENDSEQ Long Day End Sequence
  DAYENDDATE Date Day End Date
  ORIGAPP String*2 Original Application
  VALUES Long Optional Fields
  DRILLSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link
  DRILLAPP String*2 Drill Down Application
  EARNINGS String*16
  EXPTAXSR BCD*10.3 Expensed Tax (source)
  EXPTAXHM BCD*10.3 Expensed Tax (functional)
  COSTTYPE String*10
  ADDCOST Integer Additional Cost Type [0=None (Item),1=Prorated,2=Prorated Manually,3=Expensed]
  PMVERSION String*3 Current PM Version
  ADJREVTYPE Integer Adjustment Revenue Type
  DATEBUS Date Posting Date
  STAFFCODE String*24 Employee No.
  LINENO Integer

## PMTRANO - Transaction Optional Field (view PM0854)
Keys (first = PK; D=dups allowed, M=modifiable): CONTRACT+PROJECT+CATEGORY+RESOURCE+TRANSNUM+OPTFIELD; OPTFIELD+CONTRACT+PROJECT+CATEGORY+RESOURCE+TRANSNUM
Fields (NAME type description [values]):
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CATEGORY String*16 Category
  RESOURCE String*24 Resource
  TRANSNUM Long Transaction Number
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMUP - US Payroll Superview (view PM0451)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTBTCH BCD*5.0 Batch
  LINENO Integer Line Number
  CHECKNUM BCD*5.0 Check Number
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  JOURNLDATE Date G/L Journal Date
  TRANSDATE Date Transaction Date
  CURRENCY String*3 Currency
  EXCHRATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOP Integer Rate Operator [1=Multiply,2=Divide]
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  EMPLOYEE String*24 Employee
  DOCTYPE Integer Document Type [1=System Check,2=Manual Check]
  TRANSTYPE Integer Transaction Type [1=Posted,2=Check Reversal]
  TRANSNUM Long PJC Transaction Number
  EARNINGS String*6 Earnings or Deduction Code
  QUANTITY BCD*10.5 Quantity
  HOURS BCD*4.3 Hours
  BASE BCD*10.3 Base
  UNITRATE BCD*9.5 Unit Rate
  PERCENT BCD*9.5 Percent
  EXTAMTHM BCD*10.3 Extended Amount (HM)
  EXTAMTSR BCD*10.3 Extended Amount (SR)
  BILLRATE BCD*10.6 Billing Rate
  BILLTYPE Integer Billing Type [0=None,2=Billable,3=No Charge,1=Non-billable]
  WIPACCT String*45 WIP Account
  TRANACCT String*45 Transaction Account
  OHACCT String*45 Overhead Account
  OHAMTSR BCD*10.3 Overhead Amount
  OHAMTHM BCD*10.3 Overhead Amount
  LABACCT String*45 Labor Account
  LABORSR BCD*10.3 Labor Amount
  LABORHM BCD*10.3 Labor Amount
  ARITEM String*16 A/R Item Number
  ARUOM String*10 A/R Unit of Measure
  OVERHD Integer Overhead Type [1=None,2=Flat Rate Per Unit,5=Percentage of Cost]
  OHEADRATE BCD*10.6 Overhead Rate
  HEADPER BCD*5.5 Overhead Percentage
  LABOR Integer Labor Type [1=None,2=Flat Rate Per Labor Hour/Unit,3=Percentage of Labor Cost]
  LABORRATE BCD*10.6 Labor Rate
  LABORPER BCD*5.5 Labor Percentage
  DRILLSRCTY Integer Drill Down Type
  DRILLDWNLK BCD*10.0 Drill Down Link
  DRILLAPP String*2 Drill Down Application
  PROJSTAT Integer ^2 Status [10=Estimate,20=Approved,30=Open,40=On Hold,70=Inactive,60=Completed,50=Closed]
  DIFF Integer Differential Record?
  EXPENSEREI Integer Exp. Reimbursement?
  RESOURCE String*24 Resource

## PMUPO - U/P Optional Field (view PM0453)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCENO+OPTFIELD; OPTFIELD+SEQUENCENO
Fields (NAME type description [values]):
  SEQUENCENO Long None
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Data Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## PMURD - Update Retainage Detail (view PM0410)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ+LINENO; DOCNUM+LINENO [D,M]; SEQ+DETAILNUM [D,M]
Fields (NAME type description [values]):
  SEQ Long Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*24 Retainage Number
  RETTYPE Integer Retainage Type [1=Opening Retainage Receivable,2=Opening Retainage Payable,3=Invoice Retainage Receivable,4=Invoice Retainage Payable]
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  DETAILNUM Long Detail Number
  CONTSTYLE Integer ^1 Style [1=Standard,2=Basic]
  PROJTYPE Integer ^2 Type [1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method
  COMMENTS String*250 Comments
  ODOCNUM String*24 Original Document Number
  AMOUNT BCD*10.3 Retainage Amount
  CUSTCCY String*3 Currency

## PMURDA - Update Retainage Detail Audit (view PM0411)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO+LINENO; POSTSEQNO+DETAILNUM; SEQ+POSTSEQNO+DETAILNUM
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  DOCNUM String*24 Retainage Number
  RETTYPE Integer Retainage Type
  FMTCONTNO String*16 ^1
  CONTRACT String*16 ^1
  PROJECT String*16 ^2
  CATEGORY String*16 ^3
  DETAILNUM Long Detail Number
  CONTSTYLE Integer ^1 Style
  PROJTYPE Integer ^2 Type
  REVREC Integer Accounting Method
  COMMENTS String*250 Comments
  ODOCNUM String*24 Original Document Number
  AMOUNT BCD*10.3 Retainage Amount
  CUSTCCY String*3 Customer Currency

## PMURH - Update Retainage (view PM0412)
Keys (first = PK; D=dups allowed, M=modifiable): SEQ; DOCNUM
Fields (NAME type description [values]):
  SEQ Long Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCNUM String*24 Retainage Number
  RETTYPE Integer Retainage Type
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12,13=13]
  COMPLETE Integer Status [0=New,10=Entered,30=Approved,40=Posted]
  PRINTSTAT Boolean Printed [0=False,1=True]
  TRANSTAT Integer Transaction Status [1=Entered,2=Imported,3=Generated,4=Posted]
  REFERENCE String*60 Reference
  DESC String*60 Description
  NUMDTL Long Number of Details
  NEXTDTLNUM Long Next Detail Number
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## PMURHA - Update Retainage Audit (view PM0413)
Keys (first = PK; D=dups allowed, M=modifiable): POSTSEQNO; SEQ+POSTSEQNO
Fields (NAME type description [values]):
  POSTSEQNO Long Posting Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEQ Long Sequence
  DOCNUM String*24 Retainage Number
  RETTYPE Integer Retainage Type
  TRANSDATE Date Transaction Date
  FISCALYEAR String*4 Fiscal Year
  FISCALPER Integer Fiscal Period
  COMPLETE Integer Status
  PRINTSTAT Boolean Printed
  TRANSTAT Integer Transaction Status
  REFERENCE String*60 Reference
  DESC String*60 Description
  NUMDTL Long Number of Details
  NEXTDTLNUM Long Next Detail Number
  CREATEBY String*8 Created By
  CREATEDT Date Created On
  CREATETM Time Created At
  APPROVEBY String*8 Approved By
  APPROVEDT Date Approved On
  APPROVETM Time Approved At
  POSTEDBY String*8 Posted By
  POSTEDDT Date Posted On
  POSTEDTM Time Posted At
  DATEBUS Date
