# PO module - compiled AOM dictionary

## POAAPC - Payables Clearing Audit (view PO0250)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+HEADSEQ+LINESEQ+CURRENCY; CNTLACCT+FISCYEAR+FISCPERIOD+CURRENCY+TRANSDATE+DOCNUMBER [D]; DOCZSEQ+DAYENDSEQ+HEADSEQ+LINESEQ+CURRENCY
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  HEADSEQ BCD*10.0 Header Sequence
  LINESEQ BCD*10.0 Line Number
  CURRENCY String*3 Currency
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CNTLACCT String*6 Control Account
  GLCLEARING String*45 Payables Clearing Account
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  TRANSDATE Date Transaction Date
  DOCNUMBER String*22 Document Number
  TRANSTYPE Integer Transaction Type [1=Requisition,2=Purchase Order,3=Receipt,4=Return,5=Invoice,6=Credit Note,7=Debit Note]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  ITEMNO String*24 Item Number
  SCEXTENDED BCD*10.3 Extended Amount
  FCEXTENDED BCD*10.3 Func. Extended Amount
  DTLTYPE Integer Detail Type [0=Line,1=Cost]
  ADDCOST String*6 Additional Cost
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  DOCZSEQ BCD*10.0 Document Link
  DATEBUS Date Posting Date

## POACD - Additional Cost Taxes (view PO0290)
Keys (first = PK; D=dups allowed, M=modifiable): ADDCOST+TAXAUTH
Fields (NAME type description [values]):
  ADDCOST String*6 Additional Cost
  TAXAUTH String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CURRENCY String*3 Currency
  TAXCLASS Integer Tax Class

## POACST - Additional Costs (view PO0300)
Keys (first = PK; D=dups allowed, M=modifiable): ADDCOST; VDCODE+ADDCOST
Fields (NAME type description [values]):
  ADDCOST String*6 Additional Cost
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  GLEXPACCT String*45 Expense Account
  AMOUNT BCD*10.3 Amount
  DATELASTMN Date Date Last Maintained
  INACTIVE Boolean Status [0=Active,1=Inactive]
  DATEINACTV Date Date Inactive
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDCODE String*12 Vendor
  CURRENCY String*3 Currency
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method [1=Leave,2=Prorate,3=Expense]
  GLRETACCT String*45 Return Account
  LINES Long Lines
  VALUES Long Optional Fields

## POACSTO - Additional Cost Optional Fields (view PO0299)
Keys (first = PK; D=dups allowed, M=modifiable): ADDCOST+OPTFIELD; OPTFIELD+ADDCOST
Fields (NAME type description [values]):
  ADDCOST String*6 Additional Cost
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

## POCOCA - Committed Costs Audit (view PO0293)
Keys (first = PK; D=dups allowed, M=modifiable): CONTRACT+PROJECT+CCATEGORY+ITEMNO+TRANSDATE+TRANSTYPE+DAYENDSEQ+HEADSEQ+LINESEQ
Fields (NAME type description [values]):
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  ITEMNO String*24 Item Number
  TRANSDATE Date Transaction Date
  TRANSTYPE Integer Transaction Type [1=Requisition,2=Purchase Order,3=Receipt,4=Return,5=Invoice,6=Credit Note,7=Debit Note]
  DAYENDSEQ BCD*10.0 Day End Number
  HEADSEQ BCD*10.0 Header Sequence
  LINESEQ BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60 Item Description
  DOCNUMBER String*22 Document Number
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  OQCOMMIT BCD*10.4 Ordered Committed Quantity
  FCCOMMIT BCD*10.3 Func. Committed Cost
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount

## POCOSTZ - Generic Cost Data (view PO0295)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ+COSTSEQ; COSTSEQ; CRNSSEQ [D,M]; INVSSEQ [D,M]; RCPSSEQ [D,M]; RETSSEQ [D,M]
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Prorate Sequence
  COSTSEQ BCD*10.0 Cost Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  RETSSEQ BCD*10.0 Return Cost Sequence
  CRNSSEQ BCD*10.0 Credit/Debit Note Cost Sequence
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  RETNUMBER String*22 Return Number
  INVNUMBER String*22 Invoice Number
  CRNNUMBER String*22 Credit/Debit Note Number
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  PRORMETHOD Integer Proration Method
  REPRORATE Integer Reproration Method
  MTOPRORATE BCD*10.3 Manual To Prorate
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  FORPRIMARY Integer Primary Vendor
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXVCLASS1 Integer Vendor Tax Class 1
  TAXVCLASS2 Integer Vendor Tax Class 2
  TAXVCLASS3 Integer Vendor Tax Class 3
  TAXVCLASS4 Integer Vendor Tax Class 4
  TAXVCLASS5 Integer Vendor Tax Class 5
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  CURRENCY String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation
  RATEOVER Boolean Rate Overridden
  SCURNDECML Integer Decimal Places
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  INVSSEQG BCD*10.0 Invoice Cost Group Sequence
  NOPRORTOGL Boolean Exp. Add'l Cost G/L data posted?
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class
  RESOURCE String*24 Resource
  BILLTYPE Integer Billing Type
  BILLCURR String*3 Billing Currency
  BCRATEDATE Date Billing Currency Conv. Rate Date
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  CALCOVRHD Boolean Calculate Overhead
  CALCLABOR Boolean Calculate Labor
  HASRTG Boolean Has Retainage
  RTGRATE Integer Retainage Exchange Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  PMTRANSNUM Long PJC Transaction Number
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation
  RATERCOVER Boolean Tax Reporting Rate Overridden
  RCURNDECML Integer Tax Reporting Decimal Places

## POCRAHO - CR/DR Note Audit Hdr. Opt. Flds (view PO0331)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+CRNAHSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+CRNAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  CRNAHSEQ BCD*10.0 Processing Sequence
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

## POCRALO - CR/DR Note Audit Line Opt. Flds (view PO0332)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+CRNAHSEQ+CRNALSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+CRNAHSEQ+CRNALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  CRNAHSEQ BCD*10.0 Processing Sequence
  CRNALSEQ BCD*10.0 Line Number
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

## POCRASO - CR/DR Note Audit Cost Opt. Flds (view PO0333)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+CRNAHSEQ+CRNASSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+CRNAHSEQ+CRNASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  CRNAHSEQ BCD*10.0 Processing Sequence
  CRNASSEQ BCD*10.0 Cost Number
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

## POCRNAH - Credit/Debit Note Audit Headers (view PO0304)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+CRNAHSEQ; VENDOR+DAYENDSEQ+CRNAHSEQ; TRANSDATE+DAYENDSEQ+CRNAHSEQ; CRNNUMBER+DAYENDSEQ+CRNAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  CRNAHSEQ BCD*10.0 Processing Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ISPRINTED Boolean Printed [0=No,1=Yes]
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  POSTDATE Date Last Posting Date
  DAYENDDATE Date Day End Processing Date
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  DESCRIPTIO String*60 Description
  TRANSTYPE Integer Transaction Type [1=Credit,2=Debit,6=Adjustment]
  FROMDOC Integer From Document [4=Return,5=Invoice]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  CRNNUMBER String*22 Credit/Debit Note Number
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  RETNUMBER String*22 Return Number
  INVNUMBER String*22 Invoice Number
  RETCURR String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  FCDOCTOTAL BCD*10.3 Functional Total Cost
  SCDOCTOTAL BCD*10.3 Source Document Total
  FCAPTOTAL BCD*10.3 Functional Transferred Cost
  SCAPTOTAL BCD*10.3 Transferred Cost
  F1099CLASS String*6 1099/CPRS Class
  F1099AMT BCD*10.3 The 1099/CPRS Amount
  COMPLETE Boolean Completed [0=No,1=Yes]
  PRINTED Boolean Printed [0=No,1=Yes]
  VALUES Long Optional Fields
  ONHOLD Boolean On Hold [0=No,1=Yes]
  PGMVER String*3 Program Version
  VERPRORATE Integer Proration Version [1=3.0A,2=5.3B]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGBASE Integer Retainage Base [0=Total After Taxes,1=Total Before Taxes]
  SCRTGAMT BCD*10.3 Retainage Amount
  SCAPRTGAMT BCD*10.3 Transferred Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percentage
  HASJOB Boolean Job Related [0=No,1=Yes]
  FCAPRTGAMT BCD*10.3 Func. Transferred Rtg. Amount
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  DATEBUS Date Posting Date
  VDACCTSET String*6 Vendor Account Set

## POCRNAL - Credit/Debit Note Audit Lines (view PO0305)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+CRNAHSEQ+CRNALSEQ; DAYENDSEQ+CRNAHSEQ+DETAILNUM+CRNALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  CRNAHSEQ BCD*10.0 Processing Sequence
  CRNALSEQ BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  OEONUMBER String*22 Order Number
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  CNTLACCT String*6 Control Account
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  RQRETURNED BCD*10.4 Quantity Returned
  RETUNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor to Stocking
  COSTCONV BCD*10.6 Cost unit conversion
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  STOCKUNIT String*10 Unit of Measure
  COSTUNIT String*10 Costing unit of measure
  UNITCOST BCD*10.6 Unit Cost
  PRUNITCOST BCD*10.6 Unit Cost
  LOADEDCOST BCD*10.6 Fully-loaded cost
  FCEXTENDED BCD*10.3 Func. Extended Amount
  SCEXTENDED BCD*10.3 Extended Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCPRORATED BCD*10.3 Func. Total Prorate Allocated
  SCPRORATED BCD*10.3 Total Prorate Allocated
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  FCTAXEXCL BCD*10.3 Func. Tax Excluded from Price
  SCTAXEXCL BCD*10.3 Tax Excluded from Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  GLCLEARING String*45 Receipt Clearing Account
  GLITEM String*45 G/L Item
  GLISPOSTED Boolean G/L data to be posted? [0=No,1=Yes]
  GLISDEBIT Boolean Normal G/L debit convention? [0=No,1=Yes]
  RQRETTOTAL BCD*10.4 Total Quantity Returned
  SQRETTOTAL BCD*10.4 Total Stock Quantity Returned
  FCEXTTOTAL BCD*10.3 Functional Total Cost
  SCEXTTOTAL BCD*10.3 Total Cost
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  DISCPCT BCD*5.5 Discount Percentage
  FCDISCOUNT BCD*10.3 Func. Discount Amount
  SCDISCOUNT BCD*10.3 Discount Amount
  FCDISCTOT BCD*10.3 Functional Total Discount
  SCDISCTOT BCD*10.3 Total Discount
  VALUES Long Optional Fields
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  RETLSEQ BCD*10.0 Return Line Sequence
  INVLSEQ BCD*10.0 Invoice Line Sequence
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  SCRTGAMT BCD*10.3 Retainage Amount
  FCRTGAMTOT BCD*10.3 Func. Total Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  RTGDDTOVER Boolean Retainage Due Date Overridden [0=No,1=Yes]
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  DFCUNITCST BCD*10.6 Func. Unit Cost Difference
  DSCUNITCST BCD*10.6 Unit Cost Difference
  DBILLRATE BCD*10.6 Billing Rate Difference
  PMTRANSNUM Long PJC Transaction Number
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed
  RFAPALLO BCD*10.3 Func. A/P Retainage Tax Allocd.
  RFAPEXPS BCD*10.3 Func. A/P Retainage Tax Expensed
  RFAPAMT1 BCD*10.3 Func. A/P Retainage Tax Amount 1
  RFAPAMT2 BCD*10.3 Func. A/P Retainage Tax Amount 2
  RFAPAMT3 BCD*10.3 Func. A/P Retainage Tax Amount 3
  RFAPAMT4 BCD*10.3 Func. A/P Retainage Tax Amount 4
  RFAPAMT5 BCD*10.3 Func. A/P Retainage Tax Amount 5
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  TOTDEFEXWT BCD*10.4 Total Def. Ext. Weight
  DETAILNUM Integer Detail Number

## POCRNAQ - CR/DR Note Audit Prorate Lines (view PO0306)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+CRNAHSEQ+CRNALSEQ+CRNASSEQ; DAYENDSEQ+CRNAHSEQ+CRNALSEQ+CURRENCY+CRNASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  CRNAHSEQ BCD*10.0 Processing Sequence
  CRNALSEQ BCD*10.0 Line Number
  CRNASSEQ BCD*10.0 Cost Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  GLITEM String*45 G/L Item
  GLEXPENSE String*45 Return Account
  GLCLEARING String*45 Receipt Clearing Account
  POSTCLEARI Boolean Post to clearing account? [0=No,1=Yes]
  CURRENCY String*3 Currency
  SCURNDECML Integer Decimal Places
  FCITEM BCD*10.3 Func. Item Amount
  SCITEM BCD*10.3 Item amount
  FCEXPENSE BCD*10.3 Func. Expensed Amount
  SCEXPENSE BCD*10.3 Expensed amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  BILLRATE BCD*10.6 Billing Rate
  BCBILLRATE BCD*10.6 (BC) Billing Rate
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  TXBASETOT1 BCD*10.3 Total Tax Base 1
  TXBASETOT2 BCD*10.3 Total Tax Base 2
  TXBASETOT3 BCD*10.3 Total Tax Base 3
  TXBASETOT4 BCD*10.3 Total Tax Base 4
  TXBASETOT5 BCD*10.3 Total Tax Base 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  BLRTTOT BCD*10.6 Total Billing Rate
  BCBLRTTOT BCD*10.6 (BC) Total Billing Rate
  FCRTGAMTOT BCD*10.3 Func. Total Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percentage
  BCRATE BCD*8.7 Billing Currency Conversion Rate
  BCRATEDATE Date Billing Currency Conv. Rate Date
  BCRATETYPE String*2 Billing Currency Conv. Rate Type
  BCRATEOPER Integer Billing Curr. Cv. Rate Operation [1=Multiply,2=Divide]
  BCRATEXIST Boolean Billing Curr. Conv. Rate Exists [0=No,1=Yes]
  PMTRANSNUM Long PJC Transaction Number
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  SCAPAMOUNT BCD*10.3 A/P Amount
  FCAPAMOUNT BCD*10.3 Func. A/P Amount
  RXAPALLO BCD*10.3 A/P Retainage Tax Allocated
  RFAPALLO BCD*10.3 Func. A/P Retainage Tax Allocd.
  RXAPEXPS BCD*10.3 A/P Retainage Tax Expensed
  RFAPEXPS BCD*10.3 Func. A/P Retainage Tax Expensed
  RXAPBASE1 BCD*10.3 A/P Retainage Tax Base 1
  RXAPBASE2 BCD*10.3 A/P Retainage Tax Base 2
  RXAPBASE3 BCD*10.3 A/P Retainage Tax Base 3
  RXAPBASE4 BCD*10.3 A/P Retainage Tax Base 4
  RXAPBASE5 BCD*10.3 A/P Retainage Tax Base 5
  RXAPAMT1 BCD*10.3 A/P Retainage Tax Amount 1
  RXAPAMT2 BCD*10.3 A/P Retainage Tax Amount 2
  RXAPAMT3 BCD*10.3 A/P Retainage Tax Amount 3
  RXAPAMT4 BCD*10.3 A/P Retainage Tax Amount 4
  RXAPAMT5 BCD*10.3 A/P Retainage Tax Amount 5
  RFAPAMT1 BCD*10.3 Func. A/P Retainage Tax Amount 1
  RFAPAMT2 BCD*10.3 Func. A/P Retainage Tax Amount 2
  RFAPAMT3 BCD*10.3 Func. A/P Retainage Tax Amount 3
  RFAPAMT4 BCD*10.3 Func. A/P Retainage Tax Amount 4
  RFAPAMT5 BCD*10.3 Func. A/P Retainage Tax Amount 5

## POCRNAS - CR/DR Note Audit Costs (view PO0307)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+CRNAHSEQ+CRNASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  CRNAHSEQ BCD*10.0 Processing Sequence
  CRNASSEQ BCD*10.0 Cost Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  INVNUMBER String*22 Invoice Number
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  CRNNUMBER String*22 Credit/Debit Note Number
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method [1=Leave,2=Prorate,3=Expense]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXVCLASS1 Integer Vendor Tax Class 1
  TAXVCLASS2 Integer Vendor Tax Class 2
  TAXVCLASS3 Integer Vendor Tax Class 3
  TAXVCLASS4 Integer Vendor Tax Class 4
  TAXVCLASS5 Integer Vendor Tax Class 5
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  CURRENCY String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  FCTAXEXCL BCD*10.3 Func. Tax Excluded from Price
  SCTAXEXCL BCD*10.3 Tax Excluded from Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  INVSSEQG BCD*10.0 Invoice Cost Group Sequence
  VALUES Long Optional Fields
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  CRNSSEQ BCD*10.0 Credit/Debit Note Cost Sequence
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  GLNOPRORCR String*45 Expensed Add'l Cost Clr. Acct.
  NOPRORTOGL Boolean Exp. Add'l Cost G/L data posted? [0=No,1=Yes]
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  CALCOVRHD Boolean Calculate Overhead [0=No,1=Yes]
  CALCLABOR Boolean Calculate Labor [0=No,1=Yes]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  SCRTGAMT BCD*10.3 Retainage Amount
  FCRTGAMTOT BCD*10.3 Func. Total Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  RTGDDTOVER Boolean Retainage Due Date Overridden [0=No,1=Yes]
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  PMTRANSNUM Long PJC Transaction Number
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  FCAPAMOUNT BCD*10.3 Func. A/P Amount
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed
  RFAPALLO BCD*10.3 Func. A/P Retainage Tax Allocd.
  RFAPEXPS BCD*10.3 Func. A/P Retainage Tax Expensed
  RFAPAMT1 BCD*10.3 Func. A/P Retainage Tax Amount 1
  RFAPAMT2 BCD*10.3 Func. A/P Retainage Tax Amount 2
  RFAPAMT3 BCD*10.3 Func. A/P Retainage Tax Amount 3
  RFAPAMT4 BCD*10.3 Func. A/P Retainage Tax Amount 4
  RFAPAMT5 BCD*10.3 Func. A/P Retainage Tax Amount 5

## POCRNC - Credit/Debit Note Comments (view PO0309)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNCREV; CRNHSEQ+CRNCSEQ [D]
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNCREV BCD*10.0 Comment Identifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CRNCSEQ BCD*10.0 CR/DR Note Comment Sequence
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  COMMENTTYP Integer Line Type [1=Comment,2=Instruction]
  COMMENT String*80 Comment

## POCRND - CR/DR Note Cost Distributions (view PO0326)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNSREV+LSEQ
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNSREV BCD*10.0 Line Number
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]

## POCRNE - CR/DR Note Posting Cost Dists. (view PO0327)
Keys (first = PK; D=dups allowed, M=modifiable): CRNISEQ+CRNHSEQ+CRNSSEQ+LSEQ
Fields (NAME type description [values]):
  CRNISEQ BCD*10.0 Header Sequence
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNSSEQ BCD*10.0 Credit/Debit Note Cost Sequence
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate

## POCRNF - CR/DR Note Day-end Cost Dists. (view PO0328)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNSSEQ+LSEQ
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNSSEQ BCD*10.0 Credit/Debit Note Cost Sequence
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate

## POCRNH1 - Credit/Debit Notes (view PO0311)
Physical tables of this view: POCRNH1, POCRNH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ; CRNNUMBER [D]; VDCODE+CRNHSEQ [M]; RETHSEQ [D]; INVHSEQ [D]; VDCODE+CRNNUMBER [D,M]
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTLSEQ BCD*10.0 Next Line Sequence
  LINES Long Lines
  LINESCMPL Long Lines Complete
  COSTS Long Costs
  COSTSCMPL Long Costs Complete
  TAXLINES Long Lines Tax Calculation Sees
  EXTRANEOUS Long Extraneous Line Count
  TAXAUTOCAL Boolean Auto. tax calculation on save [0=No,1=Yes]
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  POSTDATE Date Last Posting Date
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PONUMBER String*22 Purchase Order Number
  DATE Date Credit/Debit Note Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  CRNNUMBER String*22 Credit/Debit Note Number
  TRANSTYPE Integer Transaction Type [6=Credit Note,7=Debit Note]
  FROMDOC Integer From Document [4=Return,5=Invoice]
  VDCODE String*12 Vendor
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDNAME String*60 Name
  VDADDRESS1 String*60 Address 1
  VDADDRESS2 String*60 Address 2
  VDADDRESS3 String*60 Address 3
  VDADDRESS4 String*60 Address 4
  VDCITY String*30 City
  VDSTATE String*30 State/Province
  VDZIP String*20 Zip/Postal Code
  VDCOUNTRY String*30 Country
  VDPHONE String*30 Phone Number
  VDFAX String*30 Fax Number
  VDCONTACT String*60 Contact
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RETHSEQ BCD*10.0 Return Sequence Key
  RETNUMBER String*22 Return Number
  RETDATE Date Return Date
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVNUMBER String*22 Invoice Number
  INVDATE Date Invoice Date
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  SPREAD BCD*8.7 Rate Spread
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  EXTWEIGHT BCD*10.4 Extended Weight
  EXTENDED BCD*10.3 Extended Cost
  DOCTOTAL BCD*10.3 Total
  AMOUNT BCD*10.3 Amount
  RQRETURNED BCD*10.4 Quantity Returned
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXEXCLUDE1 BCD*10.3 Excluded Tax Amount 1
  TXEXCLUDE2 BCD*10.3 Excluded Tax Amount 2
  TXEXCLUDE3 BCD*10.3 Excluded Tax Amount 3
  TXEXCLUDE4 BCD*10.3 Excluded Tax Amount 4
  TXEXCLUDE5 BCD*10.3 Excluded Tax Amount 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  F1099CLASS String*6 1099/CPRS Class
  F1099AMT BCD*10.3 The 1099/CPRS Amount
  MPRORATED BCD*10.3 Manual Proration Total
  MTOPRORATE BCD*10.3 Manual To Prorate
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  VDEMAIL String*50 E-mail
  VDPHONEC String*30 Contact Phone
  VDFAXC String*30 Contact Fax
  VDEMAILC String*50 Contact E-mail
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  VALUES Long Optional Fields
  ONHOLD Boolean On Hold [0=No,1=Yes]
  VERPRORATE Integer Proration Version [1=3.0A,2=5.3B]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGBASE Integer Retainage Base [0=Total After Taxes,1=Total Before Taxes]
  RTGAMOUNT BCD*10.3 Retainage Amount
  JOBLINES Long Job Related Lines
  JOBCOSTS Long Job Related Costs
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  SPREADRC BCD*8.7 Tax Reporting Rate Spread
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEMTCHRC Integer Tax Reporting Rate Match Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TREXCLUDE1 BCD*10.3 Tax Reporting Excluded Amount 1
  TREXCLUDE2 BCD*10.3 Tax Reporting Excluded Amount 2
  TREXCLUDE3 BCD*10.3 Tax Reporting Excluded Amount 3
  TREXCLUDE4 BCD*10.3 Tax Reporting Excluded Amount 4
  TREXCLUDE5 BCD*10.3 Tax Reporting Excluded Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RTGTAXREP Integer Report Retainage Tax [0=At Time of Original Document,1=As Per Tax Authority]
  TAXVERSION Long Tax State Version
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## POCRNH2 - Credit/Debit Notes (view PO0311)
Physical tables of this view: POCRNH1, POCRNH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BTCODE String*6 Bill-To Location
  BTDESC String*60 Bill-To Location Description
  BTADDRESS1 String*60 Bill-To Address 1
  BTADDRESS2 String*60 Bill-To Address 2
  BTADDRESS3 String*60 Bill-To Address 3
  BTADDRESS4 String*60 Bill-To Address 4
  BTCITY String*30 Bill-To City
  BTSTATE String*30 Bill-To State/Province
  BTZIP String*20 Bill-To Zip/Postal Code
  BTCOUNTRY String*30 Bill-To Country
  BTPHONE String*30 Bill-To Phone Number
  BTFAX String*30 Bill-To Fax Number
  BTCONTACT String*60 Bill-To Contact
  STCODE String*6 Ship-To Location
  STDESC String*60 Ship-To Location Description
  STADDRESS1 String*60 Ship-To Address 1
  STADDRESS2 String*60 Ship-To Address 2
  STADDRESS3 String*60 Ship-To Address 3
  STADDRESS4 String*60 Ship-To Address 4
  STCITY String*30 Ship-To City
  STSTATE String*30 Ship-To State/Province
  STZIP String*20 Ship-To Zip/Postal Code
  STCOUNTRY String*30 Ship-To Country
  STPHONE String*30 Ship-To Phone Number
  STFAX String*30 Ship-To Fax Number
  STCONTACT String*60 Ship-To Contact
  RTCODE String*6 Remit-To Location
  RTDESC String*60 Remit-To Location Description
  RTADDRESS1 String*60 Remit-To Address 1
  RTADDRESS2 String*60 Remit-To Address 2
  RTADDRESS3 String*60 Remit-To Address 3
  RTADDRESS4 String*60 Remit-To Address 4
  RTCITY String*30 Remit-To City
  RTSTATE String*30 Remit-To State/Province
  RTZIP String*20 Remit-To Zip/Postal Code
  RTCOUNTRY String*30 Remit-To Country
  RTPHONE String*30 Remit-To Phone Number
  RTFAX String*30 Remit-To Fax Number
  RTCONTACT String*60 Remit-To Contact
  PDRATE BCD*8.7 Predecessor's Exchange Rate
  PDRATETYPE String*2 Predecessor's Rate Type
  PDRATEDATE Date Predecessor's Rate Date
  PDRATEOPER Integer Predecessor's Rate Operation [1=Multiply,2=Divide]
  PDRATEOVER Boolean Predecessor's Rate Overridden [0=No,1=Yes]
  BTEMAIL String*50 Bill-To E-mail
  BTPHONEC String*30 Bill-To Contact Phone
  BTFAXC String*30 Bill-To Contact Fax
  BTEMAILC String*50 Bill-To Contact E-mail
  STEMAIL String*50 Ship-To E-mail
  STPHONEC String*30 Ship-To Contact Phone
  STFAXC String*30 Ship-To Contact Fax
  STEMAILC String*50 Ship-To Contact E-mail
  RTEMAIL String*50 Remit-To E-mail
  RTPHONEC String*30 Remit-To Contact Phone
  RTFAXC String*30 Remit-To Contact Fax
  RTEMAILC String*50 Remit-To Contact E-mail
  PDRATERC BCD*8.7 Pred. Tax Reporting Exch. Rate
  PDRATTYPRC String*2 Pred. Tax Reporting Rate Type
  PDRATEDTRC Date Pred. Tax Reporting Rate Date
  PDRATEOPRC Integer Pred. Tax Reporting Rate Oper. [1=Multiply,2=Divide]
  PDRATERCOV Boolean Pred. Tax Reporting Rate Overrd. [0=No,1=Yes]
  VDACCTSET String*6 Vendor Account Set
  DATEBUS Date Posting Date
  ENTEREDBY String*8 Entered By
  DETAILNEXT Integer Next Detail Number

## POCRNHO - Credit/Debit Note Opt. Fields (view PO0314)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+OPTFIELD; OPTFIELD+CRNHSEQ
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
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

## POCRNI - Credit/Debit Note Postings (view PO0312)
Keys (first = PK; D=dups allowed, M=modifiable): CRNISEQ; CRNHSEQ [D]
Fields (NAME type description [values]):
  CRNISEQ BCD*10.0 Header Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  POSTDATE Date Last Posting Date
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  TRANSTYPE Integer Transaction Type
  FROMDOC Integer From Document
  INVHSEQ BCD*10.0 Invoice Sequence Key
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RETHSEQ BCD*10.0 Return Sequence Key
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate
  SCRTGAMT BCD*10.3 Retainage Amount

## POCRNJ - Credit/Debit Note Day-ends (view PO0313)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRORATESEQ BCD*10.0 Prorate Model Sequence
  POSTDATE Date Last Posting Date
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  ISCOMPLETE Boolean Completed
  DTCOMPLETE Date Date Completed
  SCRTGAMT BCD*10.3 Retainage Amount

## POCRNL - Credit/Debit Note Lines (view PO0315)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNLREV; CRNHSEQ+CRNLSEQ; INVLSEQ [D,M]; RETLSEQ [D,M]; RCPLSEQ [D,M]; CRNHSEQ+DETAILNUM+CRNLSEQ [D]
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNLREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence
  CRNCSEQ BCD*10.0 CR/DR Note Comment Sequence
  OEONUMBER String*22 Order Number
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLSEQ BCD*10.0 Return Line Sequence
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLSEQ BCD*10.0 Invoice Line Sequence
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  VENDITEMNO String*24 Vendor Item Number
  HASCOMMENT Boolean Comments [0=No,1=Yes]
  RETUNIT String*10 Unit of Measure
  RETCONV BCD*10.6 Returning Conversion Factor
  RETDECML Integer Returning Unit Decimals
  STOCKDECML Integer Stock Unit Decimals
  RQRETURNED BCD*10.4 Quantity
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Recoverable Tax
  TXEXPSAMT BCD*10.3 Expensed Tax
  TXALLOAMT BCD*10.3 Allocated Tax
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  FCEXTENDED BCD*10.3 Func. Extended Amount
  GLACEXPENS String*45 Expense Account
  MPRORATED BCD*10.3 Manual Proration
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  RCPNUMBER String*22 Receipt Number
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORLSEQ BCD*10.0 Purchase Order Line Sequence
  PONUMBER String*22 Purchase Order Number
  GLNONSTKCR String*45 Non-Stock Clearing Account
  MANITEMNO String*24 Manufacturer's Item Number
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  VALUES Long Optional Fields
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  RTGDDTOVER Boolean Retainage Due Date Overridden [0=No,1=Yes]
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  UCISMANUAL Boolean Unit Cost is Manual [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]
  DETAILNUM Integer Detail Number

## POCRNLL - Credit/Debit Note Line Lots (view PO0829)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNLREV+LOTNUMF; LOTNUMF+CRNHSEQ+CRNLREV
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNLREV BCD*10.0 Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Lot Quantity
  QTYSQ BCD*10.4 Stock Lot Quantity

## POCRNLO - CR/DR Note Line Optional Fields (view PO0318)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNLREV+OPTFIELD; OPTFIELD+CRNHSEQ+CRNLREV
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNLREV BCD*10.0 Line Number
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

## POCRNLS - Credit/Debit Note Line Serials (view PO0820)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNLREV+SERIALNUMF; SERIALNUMF+CRNHSEQ+CRNLREV
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNLREV BCD*10.0 Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence

## POCRNM - Credit/Debit Note Posting Lines (view PO0316)
Keys (first = PK; D=dups allowed, M=modifiable): CRNISEQ+CRNHSEQ+CRNLSEQ
Fields (NAME type description [values]):
  CRNISEQ BCD*10.0 Header Sequence
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLSEQ BCD*10.0 Return Line Sequence
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLSEQ BCD*10.0 Invoice Line Sequence
  ITEMDESC String*60 Item Description
  STOCKUNIT String*10 Unit of Measure
  RETUNIT String*10 Unit of Measure
  RETCONV BCD*10.6 Returning Conversion Factor
  RETDECML Integer Returning Unit Decimals
  STOCKDECML Integer Stock Unit Decimals
  RQRETURNED BCD*10.4 Quantity Returned
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.3 Extended Weight
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  GLACEXPENS String*45 Expense Account
  GLNONSTKCR String*45 Non-Stock Clearing Account
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden
  RTGDDTOVER Boolean Retainage Due Date Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  QTYPOSTED Boolean Is Quantity Posted?

## POCRNML - Return Posting Lines Lots (view PO0828)
Keys (first = PK; D=dups allowed, M=modifiable): CRNISEQ+CRNHSEQ+CRNLSEQ+LOTNUMF; LOTNUMF+CRNISEQ+CRNHSEQ+CRNLSEQ
Fields (NAME type description [values]):
  CRNISEQ BCD*10.0 Header Sequence
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RQPREV BCD*10.4 Old Quantity
  RQCURR BCD*10.4 Current Quantity
  SQPREV BCD*10.4 Old Stock Quantity
  SQCURR BCD*10.4 Current Stock Quantity
  OPERATION Integer Operation To Post

## POCRNMS - Return Posting Lines Serials (view PO0821)
Keys (first = PK; D=dups allowed, M=modifiable): CRNISEQ+CRNHSEQ+CRNLSEQ+SERIALNUMF; SERIALNUMF+CRNISEQ+CRNHSEQ+CRNLSEQ
Fields (NAME type description [values]):
  CRNISEQ BCD*10.0 Header Sequence
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post

## POCRNN - Credit/Debit Note Day-end Lines (view PO0317)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNLSEQ
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  RETLSEQ BCD*10.0 Return Line Sequence
  ITEMDESC String*60 Item Description
  STOCKUNIT String*10 Unit of Measure
  RETUNIT String*10 Unit of Measure
  RETCONV BCD*10.6 Returning Conversion Factor
  RETDECML Integer Returning Unit Decimals
  RQRECEIVED BCD*10.4 Receiving Quantity Received
  RQRETURNED BCD*10.4 Quantity Returned
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Integer Tax Includable 1
  TAXINCLUD2 Integer Tax Includable 2
  TAXINCLUD3 Integer Tax Includable 3
  TAXINCLUD4 Integer Tax Includable 4
  TAXINCLUD5 Integer Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden
  RTGDDTOVER Boolean Retainage Due Date Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight

## POCRNS - CR/DR Note Additional Costs (view PO0320)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNSREV; CRNHSEQ+CRNSSEQ; CRNSSEQ+CRNHSEQ
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNSREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CRNSSEQ BCD*10.0 Credit/Debit Note Cost Sequence
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  ADDCOST String*6 Additional Cost
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method [1=No Proration]
  REPRORATE Integer Reproration Method [1=Leave,2=Prorate,3=Expense]
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  RCPNUMBER String*22 Receipt Number
  RCPHSEQA BCD*10.0 Apply To Receipt Sequence Key
  RCPNUMBERA String*22 Apply To Receipt Number
  INVSSEQG BCD*10.0 Invoice Cost Group Sequence
  VALUES Long Optional Fields
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  CALCOVRHD Boolean Calculate Overhead [0=No,1=Yes]
  CALCLABOR Boolean Calculate Labor [0=No,1=Yes]
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  RTGDDTOVER Boolean Retainage Due Date Overridden [0=No,1=Yes]
  COSTDISTS Long Cost Distributions
  MANDISTS Long Manual Cost Distributions
  EXTDISTS Long Extraneous Cost Distributions
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## POCRNSO - CR/DR Note Add. Cost Opt. Fields (view PO0323)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNSREV+OPTFIELD; OPTFIELD+CRNHSEQ+CRNSREV
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNSREV BCD*10.0 Line Number
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

## POCRNT - CR/DR Note Posting Add. Costs (view PO0321)
Keys (first = PK; D=dups allowed, M=modifiable): CRNISEQ+CRNHSEQ+CRNSSEQ
Fields (NAME type description [values]):
  CRNISEQ BCD*10.0 Header Sequence
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNSSEQ BCD*10.0 Credit/Debit Note Cost Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  RCPHSEQC BCD*10.0 Receipt/Apply To Receipt Seq Key
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden
  RTGDDTOVER Boolean Retainage Due Date Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## POCRNU - CR/DR Note Day-end Additional Costs (view PO0322)
Keys (first = PK; D=dups allowed, M=modifiable): CRNHSEQ+CRNSSEQ
Fields (NAME type description [values]):
  CRNHSEQ BCD*10.0 Credit/Debit Note Sequence Key
  CRNSSEQ BCD*10.0 Credit/Debit Note Cost Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method
  REPRORATE Integer Reproration Method
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden
  RTGDDTOVER Boolean Retainage Due Date Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## PODISTZ - Generic Distribution Data (view PO0337)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ+LINESEQ+COSTSEQ; LINESEQ+COSTSEQ
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Prorate Sequence
  LINESEQ BCD*10.0 Line Sequence
  COSTSEQ BCD*10.0 Cost Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BCRATE BCD*8.7 Billing Currency Conversion Rate
  BCRATEDATE Date Billing Currency Conv. Rate Date
  BCRATETYPE String*2 Billing Currency Conv. Rate Type
  BCRATEOPER Integer Billing Curr. Cv. Rate Operation
  BCRATEXIST Boolean Billing Curr. Conv. Rate Exists
  PMTRANSNUM Long PJC Transaction Number

## POGLREF - G/L Reference Integration (view PO0351)
Keys (first = PK; D=dups allowed, M=modifiable): SOURCE+GLDEST
Fields (NAME type description [values]):
  SOURCE Integer Source Transaction Type [0=Receipt,1=Receipt Detail,2=Receipt Expensed Additional Cost Detail,3=Invoice,4=Invoice Detail,5=Invoice Expensed Additional Cost Detail,6=Return,7=Return Detail,8=Credit Note,9=Credit Note Detail,10=Credit Note Expensed Additional Cost Detail,11=Debit Note,12=Debit Note Detail,13=Debit Note Expensed Additional Cost Detail]
  GLDEST Integer G/L Transaction Field [0=G/L Entry Description,1=G/L Detail Reference,2=G/L Detail Description,3=G/L Detail Comment]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEPARATOR Integer Separator [0=* Asterisk,1=- Hyphen,2=/ Forward Slash,3=\ Back Slash,4=. Period,5=( Left Parenthesis,6=) Right Parenthesis,7=# Number Sign,8=Space]
  SEGMENT1 Integer Included Segment 1 [0=None,1=Additional Cost,2=Additional Cost Description,3=Bill-To Description,4=Bill-To Location,5=Category,6=Comments,7=Contact Name,8=Contract,37=Credit Note Number,9=Day End Number,38=Debit Note Number,10=Description,11=Detail Description,12=Document Number,13=Document Type,14=Entry Number,15=From Document,16=Invoice Number,17=Item Number,18=Location,19=Location Name,20=Manufacturer's Item Number,21=Order Number,22=Project,23=Purchase Order Number,24=Receipt Number,25=Reference,26=Remit-To Location,27=Return Number,28=Return/Invoice Number,29=Ship-To Location,30=Ship-Via,31=Ship-Via Description,32=Source Code,33=Unformatted Item Number,34=Vendor Item Number,35=Vendor Name,36=Vendor Number]
  SEGMENT2 Integer Included Segment 2 [0=None,1=Additional Cost,2=Additional Cost Description,3=Bill-To Description,4=Bill-To Location,5=Category,6=Comments,7=Contact Name,8=Contract,37=Credit Note Number,9=Day End Number,38=Debit Note Number,10=Description,11=Detail Description,12=Document Number,13=Document Type,14=Entry Number,15=From Document,16=Invoice Number,17=Item Number,18=Location,19=Location Name,20=Manufacturer's Item Number,21=Order Number,22=Project,23=Purchase Order Number,24=Receipt Number,25=Reference,26=Remit-To Location,27=Return Number,28=Return/Invoice Number,29=Ship-To Location,30=Ship-Via,31=Ship-Via Description,32=Source Code,33=Unformatted Item Number,34=Vendor Item Number,35=Vendor Name,36=Vendor Number]
  SEGMENT3 Integer Included Segment 3 [0=None,1=Additional Cost,2=Additional Cost Description,3=Bill-To Description,4=Bill-To Location,5=Category,6=Comments,7=Contact Name,8=Contract,37=Credit Note Number,9=Day End Number,38=Debit Note Number,10=Description,11=Detail Description,12=Document Number,13=Document Type,14=Entry Number,15=From Document,16=Invoice Number,17=Item Number,18=Location,19=Location Name,20=Manufacturer's Item Number,21=Order Number,22=Project,23=Purchase Order Number,24=Receipt Number,25=Reference,26=Remit-To Location,27=Return Number,28=Return/Invoice Number,29=Ship-To Location,30=Ship-Via,31=Ship-Via Description,32=Source Code,33=Unformatted Item Number,34=Vendor Item Number,35=Vendor Name,36=Vendor Number]
  SEGMENT4 Integer Included Segment 4 [0=None,1=Additional Cost,2=Additional Cost Description,3=Bill-To Description,4=Bill-To Location,5=Category,6=Comments,7=Contact Name,8=Contract,37=Credit Note Number,9=Day End Number,38=Debit Note Number,10=Description,11=Detail Description,12=Document Number,13=Document Type,14=Entry Number,15=From Document,16=Invoice Number,17=Item Number,18=Location,19=Location Name,20=Manufacturer's Item Number,21=Order Number,22=Project,23=Purchase Order Number,24=Receipt Number,25=Reference,26=Remit-To Location,27=Return Number,28=Return/Invoice Number,29=Ship-To Location,30=Ship-Via,31=Ship-Via Description,32=Source Code,33=Unformatted Item Number,34=Vendor Item Number,35=Vendor Name,36=Vendor Number]
  SEGMENT5 Integer Included Segment 5 [0=None,1=Additional Cost,2=Additional Cost Description,3=Bill-To Description,4=Bill-To Location,5=Category,6=Comments,7=Contact Name,8=Contract,37=Credit Note Number,9=Day End Number,38=Debit Note Number,10=Description,11=Detail Description,12=Document Number,13=Document Type,14=Entry Number,15=From Document,16=Invoice Number,17=Item Number,18=Location,19=Location Name,20=Manufacturer's Item Number,21=Order Number,22=Project,23=Purchase Order Number,24=Receipt Number,25=Reference,26=Remit-To Location,27=Return Number,28=Return/Invoice Number,29=Ship-To Location,30=Ship-Via,31=Ship-Via Description,32=Source Code,33=Unformatted Item Number,34=Vendor Item Number,35=Vendor Name,36=Vendor Number]

## POGNLOC - Item Quantities on Hand (view PO0354)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+LOCATION
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ALLOWED Boolean Item Allowed at this Location [0=No,1=Yes]
  QTYONHAND BCD*10.4 Quantity on Hand
  QTYPO BCD*10.4 Quantity on POs

## POGNOE - Create POs From O/E Orders by Vendor (view PO0355)
Keys (first = PK; D=dups allowed, M=modifiable): VDCODE+ITEMNO+LOCATION+ORDERUNIT+ORDUNIQ+LINENUM+PRNCOMPNO+COMPNO
Fields (NAME type description [values]):
  VDCODE String*12 Vendor
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ORDERUNIT String*10 Unit of Measure
  ORDUNIQ BCD*10.0 Order Unique Number
  LINENUM Integer Line Number
  PRNCOMPNO Long Parent Component Number
  COMPNO Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDERCONV BCD*10.6 Order Unit Conversion
  OEONUMBER String*22 Order Number
  OQORDERED BCD*10.4 Ordered Quantity Ordered
  QTYBO BCD*10.4 Quantity Backorderd
  QTYPO BCD*10.4 Quantity on POs
  QTYNEEDED BCD*10.4 Quantity Needed for this Order
  POONHOLD Boolean On Hold [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  UNITWEIGHT BCD*10.4 Unit Weight

## POGNOEB - Create POs From O/E Orders by Order (view PO0357)
Keys (first = PK; D=dups allowed, M=modifiable): VDCODE+ORDUNIQ+ITEMNO+LOCATION+ORDERUNIT+LINENUM+PRNCOMPNO+COMPNO
Fields (NAME type description [values]):
  VDCODE String*12 Vendor
  ORDUNIQ BCD*10.0 Order Unique Number
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ORDERUNIT String*10 Unit of Measure
  LINENUM Integer Line Number
  PRNCOMPNO Long Parent Component Number
  COMPNO Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDERCONV BCD*10.6 Order Unit Conversion
  OEONUMBER String*22 Order Number
  OQORDERED BCD*10.4 Ordered Quantity Ordered
  QTYBO BCD*10.4 Quantity Backorderd
  QTYPO BCD*10.4 Quantity on POs
  QTYNEEDED BCD*10.4 Quantity Needed for this Order
  POONHOLD Boolean On Hold [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  UNITWEIGHT BCD*10.4 Unit Weight

## POGNVD - Create POs From Requisitions by Vendor (view PO0361)
Keys (first = PK; D=dups allowed, M=modifiable): VDCODE+RQNHSEQ
Fields (NAME type description [values]):
  VDCODE String*12 Vendor
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## POHSTH - Purchase History (view PO0380)
Keys (first = PK; D=dups allowed, M=modifiable): VENDOR+ITEMNO+FISCYEAR+FISCPERIOD; ITEMNO+VENDOR+FISCYEAR+FISCPERIOD
Fields (NAME type description [values]):
  VENDOR String*12 Vendor
  ITEMNO String*24 Item Number
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CURRENCY String*3 Currency
  RCPCOUNT Long No. of Receipts
  SQRECEIVED BCD*10.4 Quantity Received
  FCRECEIVED BCD*10.3 Func. Total Received
  SCRECEIVED BCD*10.3 Srce. Total Received
  INVCOUNT Long No. of Invoices
  SQINVADJ BCD*10.4 Quantity Adjusted on Invoices
  FCINVADJ BCD*10.3 Func. Adjusted on Invoices
  SCINVADJ BCD*10.3 Srce. Adjusted on Invoices
  RETCOUNT Long No. of Returns
  SQRETURNED BCD*10.4 Quantity Returned
  FCRETURNED BCD*10.3 Func. Return Amount
  SCRETURNED BCD*10.3 Srce. Return Amount
  CRNCOUNT Long No. of Credit Notes
  SQCRNADJ BCD*10.4 Quantity Credited
  FCCRNADJ BCD*10.3 Func. Credit Note Amount
  SCCRNADJ BCD*10.3 Srce. Credit Note Amount
  DEBCOUNT Long No. of Debit Notes
  SQDEBADJ BCD*10.4 Quantity Debited
  FCDEBADJ BCD*10.3 Func. Debit Note Amount
  SCDEBADJ BCD*10.3 Srce. Debit Note Amount
  SQINVTOTAL BCD*10.4 Quantity Invoiced
  FCINVTOTAL BCD*10.3 Func. Total Invoiced
  SCINVTOTAL BCD*10.3 Srce. Total Invoiced
  SQCRNTOTAL BCD*10.4 Total Credited Quantity
  FCCRNTOTAL BCD*10.3 Func. Total Credited
  SCCRNTOTAL BCD*10.3 Srce. Total Credited
  SQDEBTOTAL BCD*10.4 Total Debited Quantity
  FCDEBTOTAL BCD*10.3 Func. Total Debited
  SCDEBTOTAL BCD*10.3 Srce. Total Debited

## POHSTL - Purchase History Detail (view PO0384)
Keys (first = PK; D=dups allowed, M=modifiable): VENDOR+ITEMNO+FISCYEAR+FISCPERIOD+TRANSDATE+POSTSEQNUM+ENTRYNUM+LINESEQ; ITEMNO+VENDOR+FISCYEAR+FISCPERIOD+TRANSDATE+POSTSEQNUM+ENTRYNUM+LINESEQ; VENDOR+ITEMNO+TRANSDATE+FISCYEAR+FISCPERIOD+POSTSEQNUM+ENTRYNUM+LINESEQ; ITEMNO+VENDOR+TRANSDATE+FISCYEAR+FISCPERIOD+POSTSEQNUM+ENTRYNUM+LINESEQ; ITEMNO+VENDOR+TRANSDATE+FISCYEAR+FISCPERIOD+POSTSEQNUM+ENTRYNUM+DETAILNUM+LINESEQ
Fields (NAME type description [values]):
  VENDOR String*12 Vendor
  ITEMNO String*24 Item Number
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  TRANSDATE Date Transaction Date
  POSTSEQNUM Long Day End Number
  ENTRYNUM Long Transaction Sequence
  LINESEQ BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  HEADSEQ BCD*10.0 Header Sequence
  CURRENCY String*3 Currency
  TRANSTYPE Integer Transaction Type [1=Requisition,2=Purchase Order,3=Receipt,4=Return,5=Invoice,6=Credit Note,7=Debit Note]
  DOCNUMBER String*22 Document Number
  LOCATION String*6 Location
  RQPOSTED BCD*10.4 Quantity
  SQPOSTED BCD*10.4 Stocking Quantity
  UNIT String*10 Unit of Measure
  CONV BCD*10.6 Conversion Factor
  SCEXTENDED BCD*10.3 Srce. Cost
  FCEXTENDED BCD*10.3 Func. Cost
  RCPDAYS Integer Days To Receive
  RQTOTAL BCD*10.4 Total Quantity
  SQTOTAL BCD*10.4 Stocking Total Quantity
  SCTOTAL BCD*10.3 Srce. Total Cost
  FCTOTAL BCD*10.3 Func. Total Cost
  SCDISCOUNT BCD*10.3 Discount Amount
  FCDISCOUNT BCD*10.3 Func. Discount Amount
  SCDISCTOT BCD*10.3 Total Discount
  FCDISCTOT BCD*10.3 Functional Total Discount
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  DETAILNUM Integer Detail Number

## POINAHO - Invoice Audit Hdr. Opt. Fields (view PO0447)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+INVAHSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+INVAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  INVAHSEQ BCD*10.0 Processing Sequence
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

## POINALO - Invoice Audit Line Opt. Fields (view PO0448)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+INVAHSEQ+INVALSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+INVAHSEQ+INVALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  INVAHSEQ BCD*10.0 Processing Sequence
  INVALSEQ BCD*10.0 Line Number
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

## POINASO - Invoice Audit Cost Opt. Fields (view PO0449)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+INVAHSEQ+INVASSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+INVAHSEQ+INVASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  INVAHSEQ BCD*10.0 Processing Sequence
  INVASSEQ BCD*10.0 Cost Number
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

## POINVAH - Invoice Audit Headers (view PO0409)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+INVAHSEQ; VENDOR+DAYENDSEQ+INVAHSEQ; TRANSDATE+DAYENDSEQ+INVAHSEQ; INVNUMBER+DAYENDSEQ+INVAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  INVAHSEQ BCD*10.0 Processing Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ISPRINTED Boolean Printed [0=No,1=Yes]
  INVHSEQ BCD*10.0 Invoice Sequence Key
  POSTDATE Date Last Posting Date
  DAYENDDATE Date Day End Processing Date
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  DESCRIPTIO String*60 Description
  TRANSTYPE Integer Transaction Type [1=Invoice,2=Invoice Adjustment,99=Sequence Placeholder (?)]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  INVNUMBER String*22 Invoice Number
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  RCPCURR String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  FCDOCTOTAL BCD*10.3 Functional Total Cost
  SCDOCTOTAL BCD*10.3 Source Document Total
  FCAPTOTAL BCD*10.3 Functional Transferred Cost
  SCAPTOTAL BCD*10.3 Transferred Cost
  F1099CLASS String*6 1099/CPRS Class
  F1099AMT BCD*10.3 The 1099/CPRS Amount
  COMPLETE Boolean Completed [0=No,1=Yes]
  PRINTED Boolean Printed [0=No,1=Yes]
  MULTIRCP Boolean Multiple Receipts [0=No,1=Yes]
  VALUES Long Optional Fields
  ONHOLD Boolean On Hold [0=No,1=Yes]
  PGMVER String*3 Program Version
  TRANSNUM BCD*10.0 Transaction Number
  VERPRORATE Integer Proration Version [1=3.0A,2=5.3B]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGBASE Integer Retainage Base [0=Total After Taxes,1=Total Before Taxes]
  SCRTGAMT BCD*10.3 Retainage Amount
  SCAPRTGAMT BCD*10.3 Transferred Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percentage
  HASJOB Boolean Job Related [0=No,1=Yes]
  FCAPRTGAMT BCD*10.3 Func. Transferred Rtg. Amount
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  DATEBUS Date Posting Date
  VDACCTSET String*6 Vendor Account Set
  IDN String*30 Import Declaration Number
  CAXAMOUNT BCD*10.3 Reverse Charges Total Amount

## POINVAL - Invoice Audit Lines (view PO0410)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+INVAHSEQ+INVALSEQ; DAYENDSEQ+INVAHSEQ+DETAILNUM+INVALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  INVAHSEQ BCD*10.0 Processing Sequence
  INVALSEQ BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  OEONUMBER String*22 Order Number
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  CNTLACCT String*6 Control Account
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  RQRECEIVED BCD*10.4 Quantity Received
  RCPUNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor to Stocking
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  STOCKUNIT String*10 Unit of Measure
  COSTUNIT String*10 Costing unit of measure
  UNITCOST BCD*10.6 Unit Cost
  PRUNITCOST BCD*10.6 Unit Cost
  LOADEDCOST BCD*10.6 Fully-loaded cost
  FCEXTENDED BCD*10.3 Func. Extended Amount
  SCEXTENDED BCD*10.3 Extended Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCPRORATED BCD*10.3 Func. Total Prorate Allocated
  SCPRORATED BCD*10.3 Total Prorate Allocated
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  FCTAXEXCL BCD*10.3 Func. Tax Excluded from Price
  SCTAXEXCL BCD*10.3 Tax Excluded from Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  GLCLEARING String*45 Receipt Clearing Account
  GLITEM String*45 G/L Item
  GLISPOSTED Boolean G/L data to be posted? [0=No,1=Yes]
  RQRECTOTAL BCD*10.4 Total Quantity Received
  SQRECTOTAL BCD*10.4 Total Stock Quantity Received
  FCEXTTOTAL BCD*10.3 Functional Total Cost
  SCEXTTOTAL BCD*10.3 Total Cost
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  DISCPCT BCD*5.5 Discount Percentage
  FCDISCOUNT BCD*10.3 Func. Discount Amount
  SCDISCOUNT BCD*10.3 Discount Amount
  FCDISCTOT BCD*10.3 Functional Total Discount
  SCDISCTOT BCD*10.3 Total Discount
  VALUES Long Optional Fields
  TERMDISCBL Integer Payment Discountable [0=No,1=Yes]
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  INVLSEQ BCD*10.0 Invoice Line Sequence
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  SCRTGAMT BCD*10.3 Retainage Amount
  FCRTGAMTOT BCD*10.3 Func. Total Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  RTGDDTOVER Boolean Retainage Due Date Overridden [0=No,1=Yes]
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  DFCUNITCST BCD*10.6 Func. Unit Cost Difference
  DSCUNITCST BCD*10.6 Unit Cost Difference
  DBILLRATE BCD*10.6 Billing Rate Difference
  PMTRANSNUM Long PJC Transaction Number
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed
  RFAPALLO BCD*10.3 Func. A/P Retainage Tax Allocd.
  RFAPEXPS BCD*10.3 Func. A/P Retainage Tax Expensed
  RFAPAMT1 BCD*10.3 Func. A/P Retainage Tax Amount 1
  RFAPAMT2 BCD*10.3 Func. A/P Retainage Tax Amount 2
  RFAPAMT3 BCD*10.3 Func. A/P Retainage Tax Amount 3
  RFAPAMT4 BCD*10.3 Func. A/P Retainage Tax Amount 4
  RFAPAMT5 BCD*10.3 Func. A/P Retainage Tax Amount 5
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  TOTDEFEXWT BCD*10.4 Total Def. Ext. Weight
  DETAILNUM Integer Detail Number

## POINVAQ - Invoice Audit Prorate Lines (view PO0411)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+INVAHSEQ+INVALSEQ+INVASSEQ; DAYENDSEQ+INVAHSEQ+INVALSEQ+CURRENCY+INVASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  INVAHSEQ BCD*10.0 Processing Sequence
  INVALSEQ BCD*10.0 Line Number
  INVASSEQ BCD*10.0 Cost Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  GLITEM String*45 G/L Item
  GLEXPENSE String*45 Return Account
  GLCLEARING String*45 Receipt Clearing Account
  POSTCLEARI Boolean Post to clearing account? [0=No,1=Yes]
  CURRENCY String*3 Currency
  SCURNDECML Integer Decimal Places
  FCITEM BCD*10.3 Func. Item Amount
  SCITEM BCD*10.3 Item amount
  FCEXPENSE BCD*10.3 Func. Expensed Amount
  SCEXPENSE BCD*10.3 Expensed amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  BILLRATE BCD*10.6 Billing Rate
  BCBILLRATE BCD*10.6 (BC) Billing Rate
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  TXBASETOT1 BCD*10.3 Total Tax Base 1
  TXBASETOT2 BCD*10.3 Total Tax Base 2
  TXBASETOT3 BCD*10.3 Total Tax Base 3
  TXBASETOT4 BCD*10.3 Total Tax Base 4
  TXBASETOT5 BCD*10.3 Total Tax Base 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  BLRTTOT BCD*10.6 Total Billing Rate
  BCBLRTTOT BCD*10.6 (BC) Total Billing Rate
  FCRTGAMTOT BCD*10.3 Func. Total Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percentage
  BCRATE BCD*8.7 Billing Currency Conversion Rate
  BCRATEDATE Date Billing Currency Conv. Rate Date
  BCRATETYPE String*2 Billing Currency Conv. Rate Type
  BCRATEOPER Integer Billing Curr. Cv. Rate Operation [1=Multiply,2=Divide]
  BCRATEXIST Boolean Billing Curr. Conv. Rate Exists [0=No,1=Yes]
  PMTRANSNUM Long PJC Transaction Number
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  SCAPAMOUNT BCD*10.3 A/P Amount
  FCAPAMOUNT BCD*10.3 Func. A/P Amount
  RXAPALLO BCD*10.3 A/P Retainage Tax Allocated
  RFAPALLO BCD*10.3 Func. A/P Retainage Tax Allocd.
  RXAPEXPS BCD*10.3 A/P Retainage Tax Expensed
  RFAPEXPS BCD*10.3 Func. A/P Retainage Tax Expensed
  RXAPBASE1 BCD*10.3 A/P Retainage Tax Base 1
  RXAPBASE2 BCD*10.3 A/P Retainage Tax Base 2
  RXAPBASE3 BCD*10.3 A/P Retainage Tax Base 3
  RXAPBASE4 BCD*10.3 A/P Retainage Tax Base 4
  RXAPBASE5 BCD*10.3 A/P Retainage Tax Base 5
  RXAPAMT1 BCD*10.3 A/P Retainage Tax Amount 1
  RXAPAMT2 BCD*10.3 A/P Retainage Tax Amount 2
  RXAPAMT3 BCD*10.3 A/P Retainage Tax Amount 3
  RXAPAMT4 BCD*10.3 A/P Retainage Tax Amount 4
  RXAPAMT5 BCD*10.3 A/P Retainage Tax Amount 5
  RFAPAMT1 BCD*10.3 Func. A/P Retainage Tax Amount 1
  RFAPAMT2 BCD*10.3 Func. A/P Retainage Tax Amount 2
  RFAPAMT3 BCD*10.3 Func. A/P Retainage Tax Amount 3
  RFAPAMT4 BCD*10.3 Func. A/P Retainage Tax Amount 4
  RFAPAMT5 BCD*10.3 Func. A/P Retainage Tax Amount 5

## POINVAS - Invoice Audit Costs (view PO0412)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+INVAHSEQ+INVASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  INVAHSEQ BCD*10.0 Processing Sequence
  INVASSEQ BCD*10.0 Cost Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  INVNUMBER String*22 Invoice Number
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method [1=Leave,2=Prorate,3=Expense]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXVCLASS1 Integer Vendor Tax Class 1
  TAXVCLASS2 Integer Vendor Tax Class 2
  TAXVCLASS3 Integer Vendor Tax Class 3
  TAXVCLASS4 Integer Vendor Tax Class 4
  TAXVCLASS5 Integer Vendor Tax Class 5
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  CURRENCY String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  FCTAXEXCL BCD*10.3 Func. Tax Excluded from Price
  SCTAXEXCL BCD*10.3 Tax Excluded from Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  INVSSEQG BCD*10.0 Invoice Cost Group Sequence
  VALUES Long Optional Fields
  TERMDISCBL Integer Payment Discountable [0=No,1=Yes]
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  GLNOPRORCR String*45 Expensed Add'l Cost Clr. Acct.
  NOPRORTOGL Boolean Exp. Add'l Cost G/L data posted? [0=No,1=Yes]
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  CALCOVRHD Boolean Calculate Overhead [0=No,1=Yes]
  CALCLABOR Boolean Calculate Labor [0=No,1=Yes]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  SCRTGAMT BCD*10.3 Retainage Amount
  FCRTGAMTOT BCD*10.3 Func. Total Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  RTGDDTOVER Boolean Retainage Due Date Overridden [0=No,1=Yes]
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  PMTRANSNUM Long PJC Transaction Number
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  FCAPAMOUNT BCD*10.3 Func. A/P Amount
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed
  RFAPALLO BCD*10.3 Func. A/P Retainage Tax Allocd.
  RFAPEXPS BCD*10.3 Func. A/P Retainage Tax Expensed
  RFAPAMT1 BCD*10.3 Func. A/P Retainage Tax Amount 1
  RFAPAMT2 BCD*10.3 Func. A/P Retainage Tax Amount 2
  RFAPAMT3 BCD*10.3 Func. A/P Retainage Tax Amount 3
  RFAPAMT4 BCD*10.3 Func. A/P Retainage Tax Amount 4
  RFAPAMT5 BCD*10.3 Func. A/P Retainage Tax Amount 5

## POINVC - Invoice Comments (view PO0416)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVCREV; INVHSEQ+INVCSEQ [D]
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVCREV BCD*10.0 Comment Identifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INVCSEQ BCD*10.0 Invoice Comment Sequence
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  COMMENTTYP Integer Line Type [1=Comment,2=Instruction]
  COMMENT String*80 Comment

## POINVD - Invoice Cost Distributions (view PO0415)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVSREV+LSEQ
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSREV BCD*10.0 Line Number
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  FROMPRED Boolean From Predecessor [0=No,1=Yes]

## POINVE - Invoice Posting Cost Distribs. (view PO0417)
Keys (first = PK; D=dups allowed, M=modifiable): INVISEQ+INVHSEQ+INVSSEQ+LSEQ
Fields (NAME type description [values]):
  INVISEQ BCD*10.0 Invoice Sequence Key
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate

## POINVF - Invoice Day-end Cost Distribs. (view PO0418)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVSSEQ+LSEQ
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate

## POINVH1 - Invoices (view PO0420)
Physical tables of this view: POINVH1, POINVH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ; INVNUMBER [D]; RCPNUMBER [D]; VDCODE+INVHSEQ; RETNUMBER [D]; RCPHSEQ [D]; VDCODE+INVNUMBER [D,M]
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTLSEQ BCD*10.0 Next Line Sequence
  LINES Long Lines
  LINESCMPL Long Lines Complete
  COSTS Long Costs
  COSTSCMPL Long Costs Complete
  PAYMENTS Long Payments
  TAXLINES Long Lines Tax Calculation Sees
  TAXAUTOCAL Boolean Auto. tax calculation on save [0=No,1=Yes]
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  POSTDATE Date Last Posting Date
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PONUMBER String*22 Purchase Order Number
  DATE Date Invoice Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  INVNUMBER String*22 Invoice Number
  VDCODE String*12 Vendor
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDNAME String*60 Name
  VDADDRESS1 String*60 Address 1
  VDADDRESS2 String*60 Address 2
  VDADDRESS3 String*60 Address 3
  VDADDRESS4 String*60 Address 4
  VDCITY String*30 City
  VDSTATE String*30 State/Province
  VDZIP String*20 Zip/Postal Code
  VDCOUNTRY String*30 Country
  VDPHONE String*30 Phone Number
  VDFAX String*30 Fax Number
  VDCONTACT String*60 Contact
  TERMSCODE String*6 Terms Code
  FROMDOC Integer From Document [3=Receipt,4=Return]
  FORPRIMARY Integer Primary Vendor [1=Primary Vendor,2=Secondary Vendor,3=New Vendor]
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPNUMBER String*22 Receipt Number
  RCPDATE Date Receipt Date
  RETHSEQ BCD*10.0 Return Sequence Key
  RETNUMBER String*22 Return Number
  RETDATE Date Return Date
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  SPREAD BCD*8.7 Rate Spread
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  DTPYMTASOF Date Payment As Of Date
  TERMDUEAMT BCD*10.3 Total Terms Amount Due
  EXTWEIGHT BCD*10.4 Extended Weight
  EXTENDED BCD*10.3 Extended Cost
  DOCTOTAL BCD*10.3 Total
  AMOUNT BCD*10.3 Additional Costs
  RQRECEIVED BCD*10.4 Quantity Received
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXEXCLUDE1 BCD*10.3 Excluded Tax Amount 1
  TXEXCLUDE2 BCD*10.3 Excluded Tax Amount 2
  TXEXCLUDE3 BCD*10.3 Excluded Tax Amount 3
  TXEXCLUDE4 BCD*10.3 Excluded Tax Amount 4
  TXEXCLUDE5 BCD*10.3 Excluded Tax Amount 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  F1099CLASS String*6 1099/CPRS Class
  F1099AMT BCD*10.3 The 1099/CPRS Amount
  MPRORATED BCD*10.3 Manual Proration Total
  MTOPRORATE BCD*10.3 Manual To Prorate
  MEXPENSED BCD*10.3 Manual Proration Expensed
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  MULTIRCP Boolean Multiple Receipts [0=No,1=Yes]
  RCPS Long Receipts
  VDEMAIL String*50 E-mail
  VDPHONEC String*30 Contact Phone
  VDFAXC String*30 Contact Fax
  VDEMAILC String*50 Contact E-mail
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  VALUES Long Optional Fields
  ONHOLD Boolean On Hold [0=No,1=Yes]
  TERMDBWT BCD*10.3 Payment Discount Base With Tax
  TERMDBNT BCD*10.3 Payment Discount Base Without Tax
  VERPRORATE Integer Proration Version [1=3.0A,2=5.3B]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGBASE Integer Retainage Base [0=Total After Taxes,1=Total Before Taxes]
  RTGTERMS String*6 Retainage Terms Code
  RTGAMOUNT BCD*10.3 Retainage Amount
  JOBLINES Long Job Related Lines
  JOBCOSTS Long Job Related Costs
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  SPREADRC BCD*8.7 Tax Reporting Rate Spread
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEMTCHRC Integer Tax Reporting Rate Match Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TREXCLUDE1 BCD*10.3 Tax Reporting Excluded Amount 1
  TREXCLUDE2 BCD*10.3 Tax Reporting Excluded Amount 2
  TREXCLUDE3 BCD*10.3 Tax Reporting Excluded Amount 3
  TREXCLUDE4 BCD*10.3 Tax Reporting Excluded Amount 4
  TREXCLUDE5 BCD*10.3 Tax Reporting Excluded Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RTGTAXREP Integer Report Retainage Tax [0=At Time of Original Document,1=As Per Tax Authority]
  TAXVERSION Long Tax State Version
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## POINVH2 - Invoices (view PO0420)
Physical tables of this view: POINVH1, POINVH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BTCODE String*6 Bill-To Location
  BTDESC String*60 Bill-To Location Description
  BTADDRESS1 String*60 Bill-To Address 1
  BTADDRESS2 String*60 Bill-To Address 2
  BTADDRESS3 String*60 Bill-To Address 3
  BTADDRESS4 String*60 Bill-To Address 4
  BTCITY String*30 Bill-To City
  BTSTATE String*30 Bill-To State/Province
  BTZIP String*20 Bill-To Zip/Postal Code
  BTCOUNTRY String*30 Bill-To Country
  BTPHONE String*30 Bill-To Phone Number
  BTFAX String*30 Bill-To Fax Number
  BTCONTACT String*60 Bill-To Contact
  STCODE String*6 Ship-To Location
  STDESC String*60 Ship-To Location Description
  STADDRESS1 String*60 Ship-To Address 1
  STADDRESS2 String*60 Ship-To Address 2
  STADDRESS3 String*60 Ship-To Address 3
  STADDRESS4 String*60 Ship-To Address 4
  STCITY String*30 Ship-To City
  STSTATE String*30 Ship-To State/Province
  STZIP String*20 Ship-To Zip/Postal Code
  STCOUNTRY String*30 Ship-To Country
  STPHONE String*30 Ship-To Phone Number
  STFAX String*30 Ship-To Fax Number
  STCONTACT String*60 Ship-To Contact
  RTCODE String*6 Remit-To Location
  RTDESC String*60 Remit-To Location Description
  RTADDRESS1 String*60 Remit-To Address 1
  RTADDRESS2 String*60 Remit-To Address 2
  RTADDRESS3 String*60 Remit-To Address 3
  RTADDRESS4 String*60 Remit-To Address 4
  RTCITY String*30 Remit-To City
  RTSTATE String*30 Remit-To State/Province
  RTZIP String*20 Remit-To Zip/Postal Code
  RTCOUNTRY String*30 Remit-To Country
  RTPHONE String*30 Remit-To Phone Number
  RTFAX String*30 Remit-To Fax Number
  RTCONTACT String*60 Remit-To Contact
  PDRATE BCD*8.7 Predecessor's Exchange Rate
  PDRATETYPE String*2 Predecessor's Rate Type
  PDRATEDATE Date Predecessor's Rate Date
  PDRATEOPER Integer Predecessor's Rate Operation [1=Multiply,2=Divide]
  PDRATEOVER Boolean Predecessor's Rate Overridden [0=No,1=Yes]
  BTEMAIL String*50 Bill-To E-mail
  BTPHONEC String*30 Bill-To Contact Phone
  BTFAXC String*30 Bill-To Contact Fax
  BTEMAILC String*50 Bill-To Contact E-mail
  STEMAIL String*50 Ship-To E-mail
  STPHONEC String*30 Ship-To Contact Phone
  STFAXC String*30 Ship-To Contact Fax
  STEMAILC String*50 Ship-To Contact E-mail
  RTEMAIL String*50 Remit-To E-mail
  RTPHONEC String*30 Remit-To Contact Phone
  RTFAXC String*30 Remit-To Contact Fax
  RTEMAILC String*50 Remit-To Contact E-mail
  PDRATERC BCD*8.7 Pred. Tax Reporting Exch. Rate
  PDRATTYPRC String*2 Pred. Tax Reporting Rate Type
  PDRATEDTRC Date Pred. Tax Reporting Rate Date
  PDRATEOPRC Integer Pred. Tax Reporting Rate Oper. [1=Multiply,2=Divide]
  PDRATERCOV Boolean Pred. Tax Reporting Rate Overrd. [0=No,1=Yes]
  VDACCTSET String*6 Vendor Account Set
  DATEBUS Date Posting Date
  ENTEREDBY String*8 Entered By
  DETAILNEXT Integer Next Detail Number
  IDN String*30 Import Declaration Number
  CAXBASE1 BCD*10.3 Reverse Charges Base 1
  CAXBASE2 BCD*10.3 Reverse Charges Base 2
  CAXBASE3 BCD*10.3 Reverse Charges Base 3
  CAXBASE4 BCD*10.3 Reverse Charges Base 4
  CAXBASE5 BCD*10.3 Reverse Charges Base 5
  CAXDTAMT1 BCD*10.3 Reverse Charges Detail Amount 1
  CAXDTAMT2 BCD*10.3 Reverse Charges Detail Amount 2
  CAXDTAMT3 BCD*10.3 Reverse Charges Detail Amount 3
  CAXDTAMT4 BCD*10.3 Reverse Charges Detail Amount 4
  CAXDTAMT5 BCD*10.3 Reverse Charges Detail Amount 5
  CAXAPPLY1 Boolean Reverse Charges Applied 1 [0=No,1=Yes]
  CAXAPPLY2 Boolean Reverse Charges Applied 2 [0=No,1=Yes]
  CAXAPPLY3 Boolean Reverse Charges Applied 3 [0=No,1=Yes]
  CAXAPPLY4 Boolean Reverse Charges Applied 4 [0=No,1=Yes]
  CAXAPPLY5 Boolean Reverse Charges Applied 5 [0=No,1=Yes]
  CAXAMOUNT1 BCD*10.3 Reverse Charges Amount 1
  CAXAMOUNT2 BCD*10.3 Reverse Charges Amount 2
  CAXAMOUNT3 BCD*10.3 Reverse Charges Amount 3
  CAXAMOUNT4 BCD*10.3 Reverse Charges Amount 4
  CAXAMOUNT5 BCD*10.3 Reverse Charges Amount 5

## POINVHO - Invoice Optional Fields (view PO0423)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+OPTFIELD; OPTFIELD+INVHSEQ
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
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

## POINVI - Invoice Postings (view PO0421)
Keys (first = PK; D=dups allowed, M=modifiable): INVISEQ; INVHSEQ [D]
Fields (NAME type description [values]):
  INVISEQ BCD*10.0 Invoice Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  POSTDATE Date Last Posting Date
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  INVHSEQ BCD*10.0 Invoice Sequence Key
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RETHSEQ BCD*10.0 Return Sequence Key
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate
  SCRTGAMT BCD*10.3 Retainage Amount
  CAXAMOUNT BCD*10.3 Reverse Charges Total Amount

## POINVJ - Invoice Day-ends (view PO0422)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRORATESEQ BCD*10.0 Prorate Model Sequence
  POSTDATE Date Last Posting Date
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  ISCOMPLETE Boolean Completed
  DTCOMPLETE Date Date Completed
  SCRTGAMT BCD*10.3 Retainage Amount
  CAXAMOUNT BCD*10.3 Reverse Charges Total Amount

## POINVL - Invoice Lines (view PO0430)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVLREV; INVHSEQ+INVLSEQ; RCPLSEQ [D,M]; INVHSEQ+DETAILNUM+INVLSEQ [D]
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INVLSEQ BCD*10.0 Invoice Line Sequence
  INVCSEQ BCD*10.0 Invoice Comment Sequence
  OEONUMBER String*22 Order Number
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  POSTEDTOIC Boolean Posted to I/C [0=No,1=Yes]
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  VENDITEMNO String*24 Vendor Item Number
  HASCOMMENT Boolean Comments [0=No,1=Yes]
  ORDERUNIT String*10 Unit of Measure
  ORDERCONV BCD*10.6 Order Unit Conversion
  ORDERDECML Integer Order Unit Decimals
  RCPUNIT String*10 Unit of Measure
  RCPCONV BCD*10.6 Receiving Conversion Factor
  RCPDECML Integer Receiving Unit Decimals
  STOCKDECML Integer Stock Unit Decimals
  RQRECEIVED BCD*10.4 Quantity Received
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  OQRECEIVED BCD*10.4 Ordered Quantity Received
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Recoverable Tax
  TXEXPSAMT BCD*10.3 Expensed Tax
  TXALLOAMT BCD*10.3 Allocated Tax
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  FCEXTENDED BCD*10.3 Func. Extended Amount
  GLACEXPENS String*45 Expense Account
  MPRORATED BCD*10.3 Manual Proration
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  RCPNUMBER String*22 Receipt Number
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORLSEQ BCD*10.0 Purchase Order Line Sequence
  PONUMBER String*22 Purchase Order Number
  GLNONSTKCR String*45 Non-Stock Clearing Account
  MANITEMNO String*24 Manufacturer's Item Number
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  XRRQRECEVD BCD*10.4 Part. Inv. Orig. Qty. Received
  XIRQRECEVD BCD*10.4 Part. Inv. Pv. Qty. Invoicied.
  PVINVLINES Long Previous Invoice Lines
  FULLYINV Boolean Fully Invoiced [0=No,1=Yes]
  VALUES Long Optional Fields
  TERMDISCBL Integer Payment Discountable [0=No,1=Yes]
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  RTGDDTOVER Boolean Retainage Due Date Overridden [0=No,1=Yes]
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  UCISMANUAL Boolean Unit Cost is Manual [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]
  DETAILNUM Integer Detail Number
  CAXABLE1 Boolean Reverse Chargeable 1 [0=No,1=Yes]
  CAXABLE2 Boolean Reverse Chargeable 2 [0=No,1=Yes]
  CAXABLE3 Boolean Reverse Chargeable 3 [0=No,1=Yes]
  CAXABLE4 Boolean Reverse Chargeable 4 [0=No,1=Yes]
  CAXABLE5 Boolean Reverse Chargeable 5 [0=No,1=Yes]

## POINVLL - Invoice Line Lots (view PO0819)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVLREV+LOTNUMF; LOTNUMF+INVHSEQ+INVLREV
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLREV BCD*10.0 Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INVLSEQ BCD*10.0 Invoice Line Sequence
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Lot Quantity
  QTYSQ BCD*10.4 Lot Stock Quantity

## POINVLO - Invoice Detail Optional Fields (view PO0433)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVLREV+OPTFIELD; OPTFIELD+INVHSEQ+INVLREV
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLREV BCD*10.0 Line Number
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

## POINVLS - Invoice Line Serials (view PO0810)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVLREV+SERIALNUMF; SERIALNUMF+INVHSEQ+INVLREV
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLREV BCD*10.0 Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INVLSEQ BCD*10.0 Invoice Line Sequence

## POINVM - Invoice Posting Lines (view PO0431)
Keys (first = PK; D=dups allowed, M=modifiable): INVISEQ+INVHSEQ+INVLSEQ
Fields (NAME type description [values]):
  INVISEQ BCD*10.0 Invoice Sequence Key
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLSEQ BCD*10.0 Invoice Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  ITEMDESC String*60 Item Description
  STOCKUNIT String*10 Unit of Measure
  RCPUNIT String*10 Unit of Measure
  RCPCONV BCD*10.6 Receiving Conversion Factor
  RCPDECML Integer Receiving Unit Decimals
  RQRECEIVED BCD*10.4 Receiving Quantity Received
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  OQRECEIVED BCD*10.4 Ordered Quantity Received
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  GLACEXPENS String*45 Expense Account
  GLNONSTKCR String*45 Non-Stock Clearing Account
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  FULLYINV Boolean Fully Invoiced
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden
  RTGDDTOVER Boolean Retainage Due Date Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  QTYPOSTED Boolean Is Quantity Posted?

## POINVML - Invoice Posting Lines Lots (view PO0818)
Keys (first = PK; D=dups allowed, M=modifiable): INVISEQ+INVHSEQ+INVLSEQ+LOTNUMF; LOTNUMF+INVISEQ+INVHSEQ+INVLSEQ
Fields (NAME type description [values]):
  INVISEQ BCD*10.0 Invoice Sequence Key
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLSEQ BCD*10.0 Invoice Line Sequence
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RQPREV BCD*10.4 Old Quantity
  RQCURR BCD*10.4 Current Quantity
  SQPREV BCD*10.4 Old Stocking Quantity
  SQCURR BCD*10.4 Current Stocking Quantity
  OPERATION Integer Operation To Post

## POINVMS - Invoice Posting Lines Serials (view PO0811)
Keys (first = PK; D=dups allowed, M=modifiable): INVISEQ+INVHSEQ+INVLSEQ+SERIALNUMF; SERIALNUMF+INVISEQ+INVHSEQ+INVLSEQ
Fields (NAME type description [values]):
  INVISEQ BCD*10.0 Invoice Sequence Key
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLSEQ BCD*10.0 Invoice Line Sequence
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post

## POINVN - Invoice Day-end Lines (view PO0432)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVLSEQ
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVLSEQ BCD*10.0 Invoice Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60 Item Description
  STOCKUNIT String*10 Unit of Measure
  RCPUNIT String*10 Unit of Measure
  RCPCONV BCD*10.6 Receiving Conversion Factor
  RCPDECML Integer Receiving Unit Decimals
  RQRECEIVED BCD*10.4 Receiving Quantity Received
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  OQRECEIVED BCD*10.4 Ordered Quantity Received
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Integer Tax Includable 1
  TAXINCLUD2 Integer Tax Includable 2
  TAXINCLUD3 Integer Tax Includable 3
  TAXINCLUD4 Integer Tax Includable 4
  TAXINCLUD5 Integer Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  FULLYINV Boolean Fully Invoiced
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden
  RTGDDTOVER Boolean Retainage Due Date Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight

## POINVP - Invoice Payment Schedules (view PO0436)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVPREV
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVPREV BCD*10.0 Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  DISCBASE BCD*10.3 Base for Discount
  DISCDATE Date Discount Date
  DISCPER BCD*5.5 Discount Percentage
  DISCAMT BCD*10.3 Discount Amount
  DUEBASE BCD*10.3 Due Base
  DUEDATE Date Due Date
  DUEPER BCD*5.5 Percentage Due
  DUEAMT BCD*10.3 Amount Due

## POINVR - Invoice Receipts (view PO0438)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVRREV; INVHSEQ+RCPHSEQ; RCPHSEQ [D]
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVRREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPNUMBER String*22 Receipt Number
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]

## POINVS - Invoice Additional Costs (view PO0440)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVSREV; INVHSEQ+INVSSEQ; INVSSEQ+INVHSEQ
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  RETHSEQ BCD*10.0 Return Sequence Key
  RETSSEQ BCD*10.0 Return Cost Sequence
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  ADDCOST String*6 Additional Cost
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method [1=Leave,2=Prorate,3=Expense]
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  RCPNUMBER String*22 Receipt Number
  RCPHSEQA BCD*10.0 Apply To Receipt Sequence Key
  RCPNUMBERA String*22 Apply To Receipt Number
  INVSSEQG BCD*10.0 Invoice Cost Group Sequence
  VALUES Long Optional Fields
  TERMDISCBL Integer Payment Discountable [0=No,1=Yes]
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  CALCOVRHD Boolean Calculate Overhead [0=No,1=Yes]
  CALCLABOR Boolean Calculate Labor [0=No,1=Yes]
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  RTGDDTOVER Boolean Retainage Due Date Overridden [0=No,1=Yes]
  COSTDISTS Long Cost Distributions
  MANDISTS Long Manual Cost Distributions
  EXTDISTS Long Extraneous Cost Distributions
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## POINVSO - Invoice Add. Cost Opt. Fields (view PO0443)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVSREV+OPTFIELD; OPTFIELD+INVHSEQ+INVSREV
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSREV BCD*10.0 Line Number
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

## POINVT - Invoice Posting Cost Lines (view PO0441)
Keys (first = PK; D=dups allowed, M=modifiable): INVISEQ+INVHSEQ+INVSSEQ
Fields (NAME type description [values]):
  INVISEQ BCD*10.0 Invoice Sequence Key
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  MTOPRORATE BCD*10.3 Manual To Prorate
  RCPHSEQC BCD*10.0 Receipt/Apply To Receipt Seq Key
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden
  RTGDDTOVER Boolean Retainage Due Date Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## POINVU - Invoice Day-end Additional Costs (view PO0442)
Keys (first = PK; D=dups allowed, M=modifiable): INVHSEQ+INVSSEQ
Fields (NAME type description [values]):
  INVHSEQ BCD*10.0 Invoice Sequence Key
  INVSSEQ BCD*10.0 Invoice Cost Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method
  REPRORATE Integer Reproration Method
  MTOPRORATE BCD*10.3 Manual To Prorate
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGDATEDUE Date Retainage Due Date
  RTGAMTOVER Boolean Retainage Amount Overridden
  RTGDDTOVER Boolean Retainage Due Date Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## POLINEZ - Generic Line Data (view PO0520)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ+LINESEQ; LINESEQ; CRNLSEQ [D,M]; INVLSEQ [D,M]; RCPLSEQ [D,M]; RETLSEQ [D,M]
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Prorate Sequence
  LINESEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  INVLSEQ BCD*10.0 Invoice Line Sequence
  RETLSEQ BCD*10.0 Return Line Sequence
  CRNLSEQ BCD*10.0 Credit/Debit Note Line Sequence
  OEONUMBER String*22 Order Number
  ITEMEXISTS Boolean Item Exists
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  RCPUNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor to Stocking
  STOCKUNIT String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  GLACEXPENS String*45 Expense Account
  GLISPOSTED Boolean G/L data to be posted?
  MPRORATED BCD*10.3 Manual Proration
  LASTLOADED BCD*10.6 Last Loaded Cost
  TRANSDATE Date Transaction Date
  COSTSEQNUM Long Cost Sequence Number
  STOCKITEM Boolean Stock Item
  GLNONSTKCR String*45 Non-Stock Clearing Account
  DISCPCT BCD*5.5 Discount Percentage
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class
  BILLTYPE Integer Billing Type
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  PMTRANSNUM Long PJC Transaction Number

## POLOTZ - Lot Prorate Data (view PO0522)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ+LINESEQ+LOTNUMF
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Prorate Sequence
  LINESEQ BCD*10.0 Line Sequence
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SQRECEIVED BCD*10.4 Quantity Received
  SQRETURNED BCD*10.4 Quantity Returned

## POMSG - E-mail Messages (view PO0540)
Keys (first = PK; D=dups allowed, M=modifiable): MSGTYPE+MSGID
Fields (NAME type description [values]):
  MSGTYPE Integer Message Type [0=Purchase Order,1=Return]
  MSGID String*16 Message ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTIVESW Boolean Status [0=Inactive,1=Active]
  DATEINAC Date Date Inactive
  DTELSTMNTN Date Date Last Maintained
  SUBJECT String*250 E-mail Subject
  BODY1 String*250 E-mail Body Text (1 of 10)
  BODY2 String*250 E-mail Body Text (2 of 10)
  BODY3 String*250 E-mail Body Text (3 of 10)
  BODY4 String*250 E-mail Body Text (4 of 10)
  BODY5 String*250 E-mail Body Text (5 of 10)
  BODY6 String*250 E-mail Body Text (6 of 10)
  BODY7 String*250 E-mail Body Text (7 of 10)
  BODY8 String*250 E-mail Body Text (8 of 10)
  BODY9 String*250 E-mail Body Text (9 of 10)
  BODY10 String*250 E-mail Body Text (10 of 10)

## POOFD - P/O Optional Fields (view PO0580)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Additional Costs,1=Requisitions,2=Requisition Details,3=Purchase Orders,4=Purchase Order Details,5=Receipts,6=Receipt Details,7=Receipt Additional Costs,8=Receipt Additional Cost Details,9=Invoices,10=Invoice Details,11=Invoice Additional Cost Details,12=Returns,13=Return Details,14=Credit/Debit Notes,15=Credit/Debit Note Details,16=Credit/Debit Note Additional Cost Details]
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
  SWPM Integer External Cost Transactions [99=Not Applicable]
  SWPAYCLRPO Integer Payables Clearing [99=Not Applicable]
  SWPAYCLRAP Integer Payables Clearing [99=Not Applicable]
  SWICCTL Integer Inventory Control [99=Not Applicable]
  SWNSCLR Integer Non-Stock Clearing [99=Not Applicable]
  SWNIPCLRPO Integer Non-Inventory Payables Clearing [99=Not Applicable]
  SWNIPCLRAP Integer Non-Inventory Payables Clearing [99=Not Applicable]
  SWNIEXPPO Integer Non-Inventory Expense [99=Not Applicable]
  SWNIEXPAP Integer Non-Inventory Expense [99=Not Applicable]
  SWACEXPPO Integer Additional Cost Expense [99=Not Applicable]
  SWACEXPAP Integer Additional Cost Expense [99=Not Applicable]
  SWAPINV Integer Invoices Optional Fields [99=Not Applicable]
  SWPMLABOR Integer Labor [99=Not Applicable]
  SWPMOH Integer Overhead [99=Not Applicable]
  SWACPCLRPO Integer Additional Cost Expense Payables Clearing [99=Not Applicable]
  SWACPCLRAP Integer Additional Cost Expense Payables Clearing [99=Not Applicable]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]

## POOFH - P/O Optional Field Locations (view PO0585)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Additional Costs,1=Requisitions,2=Requisition Details,3=Purchase Orders,4=Purchase Order Details,5=Receipts,6=Receipt Details,7=Receipt Additional Costs,8=Receipt Additional Cost Details,9=Invoices,10=Invoice Details,11=Invoice Additional Cost Details,12=Returns,13=Return Details,14=Credit/Debit Notes,15=Credit/Debit Note Details,16=Credit/Debit Note Additional Cost Details]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Optional Fields

## POOPT - Purchase Order Options (view PO0600)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer (key field)
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTSEQ BCD*10.0 Next Control Sequence
  PHONE String*30 Phone Number
  FAX String*30 Fax Number
  CONTACT String*60 Contact
  RATETYPE String*2 Default Rate Type
  NOXITEMPER Boolean Allow Non-Inventory Items [0=No,1=Yes]
  ORDHIST Boolean Keep Purchase History [0=No,1=Yes]
  TRANHIST Boolean Keep Transaction History [0=No,1=Yes]
  KEEPSTAT Boolean Keep Statistics [0=No,1=Yes]
  EDITSTAT Boolean Edit Statistics [0=No,1=Yes]
  ORDYEAR Integer Accumulate History By [1=Calendar Year,2=Fiscal Year]
  ORDPERIOD Integer History Periods By [1=Weekly,2=Seven Days,3=Bi-weekly,4=Four Weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Annually,10=Fiscal Period]
  STATYEAR Integer Accumulate Statistics By [1=Calendar Year,2=Fiscal Year]
  STATPERIOD Integer Statistics Periods By [1=Weekly,2=Seven Days,3=Bi-weekly,4=Four Weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Annually,10=Fiscal Period]
  AGEDAYS1 Integer Aging Period 1
  AGEDAYS2 Integer Aging Period 2
  AGEDAYS3 Integer Aging Period 3
  RQNNUMBERL Integer Requisition Length
  RQNPREFIXD String*6 Requisition Prefix
  RQNBODYD String*22 Requisition Number
  PORNUMBERL Integer Purchase Order Length
  PORPREFIXD String*6 Purchase Order Prefix
  PORBODYD String*22 Purchase Order Number
  RCPNUMBERL Integer Receipt Length
  RCPPREFIXD String*6 Receipt Prefix
  RCPBODYD String*22 Receipt Number
  RETNUMBERL Integer Return Length
  RETPREFIXD String*6 Return Prefix
  RETBODYD String*22 Return Number
  DEFTEMP String*6 Default Template Code
  LGENDAYEND BCD*10.0 Last G/L Day-End Sequence
  APPENDGL Integer Append to Existing G/L Batch [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  CONSOLGL Integer G/L Consolidation [1=Do Not Consolidate,9=Consolidate Transaction Details by Account,2=Consolidate by Account and Fiscal Period,3=Consolidate by Account, Fiscal Period, and Source]
  DEFERGL Boolean Generate G/L Batches On Demand [0=No,1=Yes]
  REFERENCGL Integer Contents of G/L Reference [1=Document Number,2=Source Code/Day End Number/Entry Number,3=Description,4=Reference,5=Vendor Number,6=Vendor Name,7=PO Number]
  DESCRIPTGL Integer Contents of G/L Description [1=Document Number,2=Source Code/Day End Number/Entry Number,3=Description,4=Reference,5=Vendor Number,6=Vendor Name,7=PO Number]
  GLACEXPENS String*45 Default Inventory Exp. Account
  GLCSTACCT String*45 Default Cost Expense Account
  DEFCOST Integer Default Cost [28=Most Recent Cost,20=Standard Cost,65=Average Cost,31=Last Unit Cost,8=Vendor Cost,29=Landed]
  NIPAYBACCT String*45 Non Inv. Payable Clr. Account
  NONINVTOGL Boolean Post to Non-Inv. Pb. Clr. Acct. [0=No,1=Yes]
  EAPAYBACCT String*45 Exp. Add. Cost Pay. Clr. Acct.
  EXPADDTOGL Boolean Post to Exp. Add'l Cost Pb. Clr. Acct. [0=No,1=Yes]
  DEFERAPPST Integer Deferred A/P Posting [0=During Day End Processing,1=On Request Using Create Batch Icon]
  SRCTYPEAD String*2 P/O Adjustments
  SRCTYPECO String*2 P/O Consolidation
  SRCTYPECR String*2 P/O Credit Notes
  SRCTYPEDB String*2 P/O Debit Notes
  SRCTYPEIN String*2 P/O Invoices
  SRCTYPERA String*2 P/O Receipt Adjustments
  SRCTYPERC String*2 P/O Receipts
  SRCTYPERJ String*2 P/O Return Adjustments
  SRCTYPERT String*2 P/O Returns
  ALLOWNXVD Boolean Allow Non-Existing Vendors [0=No,1=Yes]
  WARNNOITEM Boolean Warn if Non-Existing Item [0=No,1=Yes]
  DATEBUSDFT Integer Default Posting Date [1=Document Date,2=Session Date]
  POSTRECENT Integer Recent/Last Cost Posting At [1=Receipt Costing,2=Invoice Costing]
  CPCOSTTOPO Boolean Default Copy Cost to Purchase Order [0=No,1=Yes]
  RQNMANAPPR Boolean Requisition Manual Approval [0=No,1=Yes]
  RCPNEGINV Integer Allow Receipts In Negative Inventory [0=No,1=Yes]

## POPLAT - Purchase Order Templates (view PO0605)
Keys (first = PK; D=dups allowed, M=modifiable): TEMPLATE
Fields (NAME type description [values]):
  TEMPLATE String*6 Template Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PLATEDESC String*60 Description
  ORDTYPE Integer Purchase Order Type [1=Active,2=Standing,3=Future,4=Blanket]
  FOB String*60 FOB Point
  ONHOLD Boolean On Hold [0=No,1=Yes]
  STLOC String*6 Ship-To Location
  BTLOC String*6 Bill-To Location
  DESC String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  SHIPVIA String*6 Ship-Via
  TAXGROUP String*12 Tax Group
  TERMS String*6 Terms Code

## POPOAHO - PO Audit Hdr. Optional Fields (view PO0611)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+PORAHSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+PORAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  PORAHSEQ BCD*10.0 Processing Sequence
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

## POPOALO - PO Audit Line Optional Fields (view PO0613)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+PORAHSEQ+PORALSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+PORAHSEQ+PORALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  PORAHSEQ BCD*10.0 Processing Sequence
  PORALSEQ BCD*10.0 Line Number
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

## POPOGH - Create POs Header (view PO0606)
Keys (first = PK; D=dups allowed, M=modifiable): HEADSEQ
Fields (NAME type description [values]):
  HEADSEQ BCD*10.0 Header Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Optional Fields

## POPOGHO - Create POs Header Opt. Fields (view PO0607)
Keys (first = PK; D=dups allowed, M=modifiable): HEADSEQ+OPTFIELD; OPTFIELD+HEADSEQ
Fields (NAME type description [values]):
  HEADSEQ BCD*10.0 Header Sequence
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

## POPOGL - Create POs Detail (view PO0608)
Keys (first = PK; D=dups allowed, M=modifiable): HEADSEQ+LINESEQ
Fields (NAME type description [values]):
  HEADSEQ BCD*10.0 Header Sequence
  LINESEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Optional Fields

## POPOGLO - Create POs Detail Opt. Fields (view PO0609)
Keys (first = PK; D=dups allowed, M=modifiable): HEADSEQ+LINESEQ+OPTFIELD; OPTFIELD+HEADSEQ+LINESEQ
Fields (NAME type description [values]):
  HEADSEQ BCD*10.0 Header Sequence
  LINESEQ BCD*10.0 Line Sequence
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

## POPORAH - Purchase Order Audit Headers (view PO0612)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+PORAHSEQ; VENDOR+DAYENDSEQ+PORAHSEQ; TRANSDATE+DAYENDSEQ+PORAHSEQ; PONUMBER+DAYENDSEQ+PORAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  PORAHSEQ BCD*10.0 Processing Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ISPRINTED Boolean Printed [0=No,1=Yes]
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  POSTDATE Date Last Posting Date
  DAYENDDATE Date Day End Processing Date
  TRANSDATE Date Transaction Date
  PORTYPE Integer Purchase Order Type [1=Active,2=Standing,3=Future,4=Blanket]
  ONHOLD Boolean On Hold [0=No,1=Yes]
  REFERENCE String*60 Reference
  DESCRIPTIO String*60 Description
  TRANSTYPE Integer Transaction Type [1=Purchase Order,2=Purchase Order Adjustment,3=Purchase Order Deletion]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  PONUMBER String*22 Purchase Order Number
  LASTRECEIP String*22 Last Receipt Number
  RCPCOUNT Integer Number of Posted Receipts
  POCURR String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  FCDOCTOTAL BCD*10.3 Functional Total Cost
  SCDOCTOTAL BCD*10.3 Source Document Total
  COMPLETE Boolean Completed [0=No,1=Yes]
  PRINTED Boolean Printed [0=No,1=Yes]
  HASRQNDATA Boolean Requisitions [0=No,1=Yes]
  PGMVER String*3 Program Version
  VALUES Long Optional Fields
  HASJOB Boolean Job Related [0=No,1=Yes]
  PVTRANDATE Date Previous Transaction Date
  PVEXRATE BCD*8.7 Previous Exchange Rate
  PVRATEDATE Date Previous Rate Date
  PVRATETYPE String*2 Previous Rate Type
  PVRATEOPER Integer Previous Rate Operation [1=Multiply,2=Divide]
  AGENTTTYPE Integer Agent Transaction Type [99=None,3=Receipt,5=Invoice]
  AGENTHSEQ BCD*10.0 Agent Sequence Key
  AGTRANSNUM BCD*10.0 Agent Dayend Transaction Number
  AGDOCNUM String*22 Agent Document Number
  AGSRCDOC String*22 Agent Source Document
  AGMULTIDOC Boolean Agent Is From Multiple Documents [0=No,1=Yes]
  AGDATE Date Agent Date
  AGFISCYEAR String*4 Agent Fiscal Year
  AGFISCPER Integer Agent Fiscal Period
  AGDESC String*60 Agent Description
  AGREF String*60 Agent Reference
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  VDACCTSET String*6 Vendor Account Set

## POPORAL - Purchase Order Audit Lines (view PO0614)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+PORAHSEQ+PORALSEQ; DAYENDSEQ+PORAHSEQ+DETAILNUM+PORALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  PORAHSEQ BCD*10.0 Processing Sequence
  PORALSEQ BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  AGENTLSEQ BCD*10.0 Agent Line Sequence
  OEONUMBER String*22 Order Number
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  PVLOCATION String*6 Previous Location
  PVORDUNIT String*10 Previous Order Unit
  PVORDCONV BCD*10.6 Previous Order Unit Conversion
  PVBILLTYPE Integer Previous Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  DBILLRATE BCD*10.6 Billing Rate Difference
  PVARITEMNO String*16 Previous A/R Item Number
  PVARUNIT String*10 Previous A/R Unit of Measure
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  OQORDERED BCD*10.4 Quantity Ordered
  OQRECEIVED BCD*10.4 Quantity Received
  OQCANCELED BCD*10.4 Quantity Canceled
  OQOUTSTAND BCD*10.4 Quantity Outstanding
  ORDERUNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor to Stocking
  SQOUTSTAND BCD*10.4 Stocking Quantity Outstanding
  STOCKUNIT String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  DFCUNITCST BCD*10.6 Func. Unit Cost Difference
  DSCUNITCST BCD*10.6 Unit Cost Difference
  FCEXTENDED BCD*10.3 Func. Extended Amount
  SCEXTENDED BCD*10.3 Extended Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  FCTAXEXCL BCD*10.3 Func. Tax Excluded from Price
  SCTAXEXCL BCD*10.3 Tax Excluded from Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  OQOUTTOTAL BCD*10.4 Total Quantity Outstanding
  SQOUTTOTAL BCD*10.4 Total Stock Quantity Outstanding
  FCEXTTOTAL BCD*10.3 Functional Total Cost
  SCEXTTOTAL BCD*10.3 Total Cost
  DISCPCT BCD*5.5 Discount Percentage
  FCDISCOUNT BCD*10.3 Func. Discount Amount
  SCDISCOUNT BCD*10.3 Discount Amount
  FCDISCTOT BCD*10.3 Functional Total Discount
  SCDISCTOT BCD*10.3 Total Discount
  COMMENT String*250 Comment
  VALUES Long Optional Fields
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  ISRECEIVED Boolean Received [0=No,1=Yes]
  GLITEM String*45 G/L Item
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  TOTDEFEXWT BCD*10.4 Total Def. Ext. Weight
  DQOUTSTAND BCD*10.4 Delta Quantity Outstanding
  DELTACONVE BCD*10.6 Delta Unit Conversion
  DELTAUNIT String*10 Delta Unit
  DETAILNUM Integer Detail Number

## POPORC - Purchase Order Comments (view PO0610)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ+PORCREV; PORHSEQ+PORCSEQ [D]
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORCREV BCD*10.0 Comment Identifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PORCSEQ BCD*10.0 Purchase Order Comment Sequence
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  COMMENTTYP Integer Line Type [1=Comment,2=Instruction]
  COMMENT String*80 Comments/Instructions

## POPORH1 - Purchase Orders (view PO0620)
Physical tables of this view: POPORH1, POPORH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ; PONUMBER; VDCODE+PORHSEQ [M]; VDCODE+PONUMBER [M]; VDCODE+DATE+PORTYPE+ONHOLD [D,M]
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTLSEQ BCD*10.0 Next Line Sequence
  LINES Long Lines
  LINESCMPL Long Lines Complete
  TAXLINES Long Lines Tax Calculation Sees
  RQNS Long Requisitions
  RQNSCMPL Long Requisitions Completed
  ISPRINTED Boolean Printed [0=No,1=Yes]
  TAXAUTOCAL Boolean Auto. tax calculation on save [0=No,1=Yes]
  LABELPRINT Boolean Labels Printed [0=No,1=Yes]
  LABELCOUNT Integer Number of Labels
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  POSTDATE Date Last Posting Date
  DATE Date Purchase Order Date
  PONUMBER String*22 Purchase Order Number
  TEMPLATE String*6 Template Code
  FOBPOINT String*60 FOB Point
  VDCODE String*12 Vendor
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDNAME String*60 Name
  VDADDRESS1 String*60 Address 1
  VDADDRESS2 String*60 Address 2
  VDADDRESS3 String*60 Address 3
  VDADDRESS4 String*60 Address 4
  VDCITY String*30 City
  VDSTATE String*30 State/Province
  VDZIP String*20 Zip/Postal Code
  VDCOUNTRY String*30 Country
  VDPHONE String*30 Phone Number
  VDFAX String*30 Fax Number
  VDCONTACT String*60 Contact
  TERMSCODE String*6 Terms Code
  HASRQNDATA Boolean Requisitions [0=No,1=Yes]
  PORTYPE Integer Purchase Order Type [1=Active,2=Standing,3=Future,4=Blanket]
  ONHOLD Boolean On Hold [0=No,1=Yes]
  ORDEREDON Date Order Date
  EXPARRIVAL Date Expected Arrival Date
  VCORIGINAL BCD*10.3 Amount Originally Authorized
  VCAVAILABL BCD*10.3 Amount Remaining
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  VIACODE String*6 Ship-Via
  VIANAME String*60 Ship-Via Name
  LASTRECEIP String*22 Last Receipt Number
  RCPDATE Date Receipt Date
  RCPCOUNT Integer Number of Posted Receipts
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  SPREAD BCD*8.7 Rate Spread
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  EXTWEIGHT BCD*10.4 Extended Weight
  EXTENDED BCD*10.3 Extended Cost
  DOCTOTAL BCD*10.3 Total
  EXTRECEIVE BCD*10.3 Extended Received Amount
  EXTCANCEL BCD*10.3 Extended Canceled Amount
  OQORDERED BCD*10.4 Quantity Ordered
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXEXCLUDE1 BCD*10.3 Excluded Tax Amount 1
  TXEXCLUDE2 BCD*10.3 Excluded Tax Amount 2
  TXEXCLUDE3 BCD*10.3 Excluded Tax Amount 3
  TXEXCLUDE4 BCD*10.3 Excluded Tax Amount 4
  TXEXCLUDE5 BCD*10.3 Excluded Tax Amount 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  DOCSOURCE Integer Document Source [0=Entered,1=Internet]
  VDEMAIL String*50 E-mail
  VDPHONEC String*30 Contact Phone
  VDFAXC String*30 Contact Fax
  VDEMAILC String*50 Contact E-mail
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  VALUES Long Optional Fields
  RQNNUMBER String*22 Requisition Number
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  JOBLINES Long Job Related Lines
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  SPREADRC BCD*8.7 Tax Reporting Rate Spread
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEMTCHRC Integer Tax Reporting Rate Match Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TREXCLUDE1 BCD*10.3 Tax Reporting Excluded Amount 1
  TREXCLUDE2 BCD*10.3 Tax Reporting Excluded Amount 2
  TREXCLUDE3 BCD*10.3 Tax Reporting Excluded Amount 3
  TREXCLUDE4 BCD*10.3 Tax Reporting Excluded Amount 4
  TREXCLUDE5 BCD*10.3 Tax Reporting Excluded Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5

## POPORH2 - Purchase Orders (view PO0620)
Physical tables of this view: POPORH1, POPORH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SRRECEIVED BCD*10.3 Amount Received To Date
  SREXTORDER BCD*10.3 Extended Order Amount
  BTCODE String*6 Bill-To Location
  BTDESC String*60 Bill-To Location Description
  BTADDRESS1 String*60 Bill-To Address 1
  BTADDRESS2 String*60 Bill-To Address 2
  BTADDRESS3 String*60 Bill-To Address 3
  BTADDRESS4 String*60 Bill-To Address 4
  BTCITY String*30 Bill-To City
  BTSTATE String*30 Bill-To State/Province
  BTZIP String*20 Bill-To Zip/Postal Code
  BTCOUNTRY String*30 Bill-To Country
  BTPHONE String*30 Bill-To Phone Number
  BTFAX String*30 Bill-To Fax Number
  BTCONTACT String*60 Bill-To Contact
  STCODE String*6 Ship-To Location
  STDESC String*60 Ship-To Location Description
  STADDRESS1 String*60 Ship-To Address 1
  STADDRESS2 String*60 Ship-To Address 2
  STADDRESS3 String*60 Ship-To Address 3
  STADDRESS4 String*60 Ship-To Address 4
  STCITY String*30 Ship-To City
  STSTATE String*30 Ship-To State/Province
  STZIP String*20 Ship-To Zip/Postal Code
  STCOUNTRY String*30 Ship-To Country
  STPHONE String*30 Ship-To Phone Number
  STFAX String*30 Ship-To Fax Number
  STCONTACT String*60 Ship-To Contact
  BTEMAIL String*50 Bill-To E-mail
  BTPHONEC String*30 Bill-To Contact Phone
  BTFAXC String*30 Bill-To Contact Fax
  BTEMAILC String*50 Bill-To Contact E-mail
  STEMAIL String*50 Ship-To E-mail
  STPHONEC String*30 Ship-To Contact Phone
  STFAXC String*30 Ship-To Contact Fax
  STEMAILC String*50 Ship-To Contact E-mail
  VDACCTSET String*6 Vendor Account Set
  ENTEREDBY String*8 Entered By
  DETAILNEXT Integer Next Detail Number
  CAXBASE1 BCD*10.3 Reverse Charges Base 1
  CAXBASE2 BCD*10.3 Reverse Charges Base 2
  CAXBASE3 BCD*10.3 Reverse Charges Base 3
  CAXBASE4 BCD*10.3 Reverse Charges Base 4
  CAXBASE5 BCD*10.3 Reverse Charges Base 5
  CAXDTAMT1 BCD*10.3 Reverse Charges Detail Amount 1
  CAXDTAMT2 BCD*10.3 Reverse Charges Detail Amount 2
  CAXDTAMT3 BCD*10.3 Reverse Charges Detail Amount 3
  CAXDTAMT4 BCD*10.3 Reverse Charges Detail Amount 4
  CAXDTAMT5 BCD*10.3 Reverse Charges Detail Amount 5
  CAXAPPLY1 Boolean Reverse Charges Applied 1 [0=No,1=Yes]
  CAXAPPLY2 Boolean Reverse Charges Applied 2 [0=No,1=Yes]
  CAXAPPLY3 Boolean Reverse Charges Applied 3 [0=No,1=Yes]
  CAXAPPLY4 Boolean Reverse Charges Applied 4 [0=No,1=Yes]
  CAXAPPLY5 Boolean Reverse Charges Applied 5 [0=No,1=Yes]
  CAXAMOUNT1 BCD*10.3 Reverse Charges Amount 1
  CAXAMOUNT2 BCD*10.3 Reverse Charges Amount 2
  CAXAMOUNT3 BCD*10.3 Reverse Charges Amount 3
  CAXAMOUNT4 BCD*10.3 Reverse Charges Amount 4
  CAXAMOUNT5 BCD*10.3 Reverse Charges Amount 5

## POPORHO - Purchase Order Hdr Opt. Fields (view PO0623)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ+OPTFIELD; OPTFIELD+PORHSEQ
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
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

## POPORI - Purchase Order Postings (view PO0621)
Keys (first = PK; D=dups allowed, M=modifiable): PORISEQ; PORHSEQ [D]
Fields (NAME type description [values]):
  PORISEQ BCD*10.0 Purchase Order Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  DATE Date Date
  POSTDATE Date Last Posting Date
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  CURRENCY String*3 Currency
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SCDOCTOTAL BCD*10.3 Source Document Total
  ISPRINTED Boolean Printed [0=No,1=Yes]
  PONUMBER String*22 Purchase Order Number
  LASTRECEIP String*22 Last Receipt Number
  RCPCOUNT Integer Number of Posted Receipts
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  HASRQNDATA Boolean Requisitions [0=No,1=Yes]
  PORTYPE Integer Purchase Order Type
  ONHOLD Boolean On Hold [0=No,1=Yes]
  RQNNUMBER String*22 Requisition Number
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  VDCODE String*12 Vendor
  VDNAME String*60 Name
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  HASJOB Boolean Job Related [0=No,1=Yes]
  AGENTTTYPE Integer Agent Transaction Type
  AGENTHSEQ BCD*10.0 Agent Sequence Key
  AGTRANSNUM BCD*10.0 Agent Dayend Transaction Number
  AGDOCNUM String*22 Agent Document Number
  AGSRCDOC String*22 Agent Source Document
  AGMULTIDOC Boolean Agent Is From Multiple Documents [0=No,1=Yes]
  AGDATE Date Agent Date
  AGFISCYEAR String*4 Agent Fiscal Year
  AGFISCPER Integer Agent Fiscal Period
  AGDESC String*60 Agent Description
  AGREF String*60 Agent Reference
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places

## POPORJ - Purchase Order Day-ends (view PO0622)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATE Date Date
  POSTDATE Date Last Posting Date
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  ISCOMPLETE Boolean Completed
  DTCOMPLETE Date Date Completed
  LASTRECEIP String*22 Last Receipt Number
  RCPCOUNT Integer Number of Posted Receipts
  PORTYPE Integer Purchase Order Type
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation
  RATEOVER Boolean Rate Overridden

## POPORL - Purchase Order Lines (view PO0630)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ+PORLREV; PORHSEQ+PORLSEQ; OEONUMBER+PORHSEQ+PORLSEQ [M]; ITEMNO+EXPARRIVAL+PORHSEQ+PORLSEQ [M]; EXPARRIVAL+OQORDERED+ITEMNO+LOCATION [D,M]; EXPARRIVAL+ITEMNO+COMPLETION [D,M]; EXPARRIVAL+OQOUTSTAND+ITEMNO [D,M]; ITEMNO+EXPARRIVAL+LOCATION+COMPLETION [D,M]; PORHSEQ+DETAILNUM+PORLSEQ [M]; PORHSEQ+EXPARRIVAL+LOCATION+COMPLETION [D,M]
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORLREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PORLSEQ BCD*10.0 Purchase Order Line Sequence
  PORCSEQ BCD*10.0 Purchase Order Comment Sequence
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  CONSOLSEQ BCD*10.0 Consolidated to line
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  RQNLSEQ BCD*10.0 Requisition Line Sequence
  OEONUMBER String*22 Order Number
  POSTEDTOIC Boolean Posted to I/C [0=No,1=Yes]
  TOPOSTTOIC Boolean To Post to I/C [0=No,1=Yes]
  STPRINT Boolean Print Status [0=No,1=Yes]
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  EXPARRIVAL Date Expected Arrival Date
  VENDITEMNO String*24 Vendor Item Number
  HASCOMMENT Boolean Comments/Instructions [0=No,1=Yes]
  ORDERUNIT String*10 Unit of Measure
  ORDERCONV BCD*10.6 Order Unit Conversion
  ORDERDECML Integer Order Unit Decimals
  STOCKDECML Integer Stock Unit Decimals
  OQORDERED BCD*10.4 Quantity Ordered
  OQRECEIVED BCD*10.4 Quantity Received
  OQCANCELED BCD*10.4 Quantity Canceled
  OQRCPEXTRA BCD*10.4 Received Extra
  OQOUTSTAND BCD*10.4 Quantity Outstanding
  SQORDERED BCD*10.4 Stocking Quantity Ordered
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  SQCANCELED BCD*10.4 Stocking Quantity Canceled
  SQRCPEXTRA BCD*10.4 Stocking Quantity Received Extra
  SQSETTLED BCD*10.4 Stocking Quantity Settled
  SQOUTSTAND BCD*10.4 Stocking Quantity Outstanding
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  OQRCPDAYS BCD*10.4 Days * Quantity Received
  EXTRECEIVE BCD*10.3 Extended Received Amount
  EXTCANCEL BCD*10.3 Extended Canceled Amount
  SRRECEIVED BCD*10.3 Amount Received To Date
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Recoverable Tax
  TXEXPSAMT BCD*10.3 Expensed Tax
  TXALLOAMT BCD*10.3 Allocated Tax
  FCEXTENDED BCD*10.3 Rcp. Ext. Amt.
  GLACEXPENS String*45 Expense Account
  HASDROPSHI Boolean Drop-Ship [0=No,1=Yes]
  DROPTYPE Integer Drop-Ship Type [2=Address Entered,3=Inventory Location Address,4=Customer Address,5=Customer Ship-To Address]
  IDCUST String*12 Drop-Ship Customer
  IDCUSTSHPT String*6 Customer Ship-To Address
  DLOCATION String*6 Drop-Ship Location
  DESC String*60 Drop-Ship Description
  ADDRESS1 String*60 Drop-Ship Address 1
  ADDRESS2 String*60 Drop-Ship Address 2
  ADDRESS3 String*60 Drop-Ship Address 3
  ADDRESS4 String*60 Drop-Ship Address 4
  CITY String*30 Drop-Ship City
  STATE String*30 Drop-Ship State/Province
  ZIP String*20 Drop-Ship Zip/Postal Code
  COUNTRY String*30 Drop-Ship Country
  PHONE String*30 Drop-Ship Phone Number
  FAX String*30 Drop-Ship Fax Number
  CONTACT String*60 Drop-Ship Contact
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  EMAIL String*50 Drop-Ship E-mail
  PHONEC String*30 Drop-Ship Contact Phone
  FAXC String*30 Drop-Ship Contact Fax
  EMAILC String*50 Drop-Ship Contact E-mail
  GLNONSTKCR String*45 Non-Stock Clearing Account
  MANITEMNO String*24 Manufacturer's Item Number
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  VALUES Long Optional Fields
  DISCOUNTF BCD*10.3 Func. Discount Amount
  ISRECEIVED Boolean Received [0=No,1=Yes]
  AGENTLSEQ BCD*10.0 Agent Line Sequence
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  UCISMANUAL Boolean Unit Cost is Manual [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  COPYDETAIL Boolean Copy This Detail Line? [0=No,1=Yes]
  DETAILNUM Integer Detail Number
  CAXABLE1 Boolean Reverse Chargeable 1 [0=No,1=Yes]
  CAXABLE2 Boolean Reverse Chargeable 2 [0=No,1=Yes]
  CAXABLE3 Boolean Reverse Chargeable 3 [0=No,1=Yes]
  CAXABLE4 Boolean Reverse Chargeable 4 [0=No,1=Yes]
  CAXABLE5 Boolean Reverse Chargeable 5 [0=No,1=Yes]

## POPORLO - Purchase Order Det. Opt. Fields (view PO0633)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ+PORLREV+OPTFIELD; OPTFIELD+PORHSEQ+PORLREV
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORLREV BCD*10.0 Line Number
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

## POPORM - Purchase Order Posting Lines (view PO0631)
Keys (first = PK; D=dups allowed, M=modifiable): PORISEQ+PORHSEQ+PORLSEQ
Fields (NAME type description [values]):
  PORISEQ BCD*10.0 Purchase Order Sequence Key
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORLSEQ BCD*10.0 Purchase Order Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  RQNLSEQ BCD*10.0 Requisition Line Sequence
  AGENTLSEQ BCD*10.0 Agent Line Sequence
  ISCOMPLETE Boolean Completed
  ISRECEIVED Boolean Received
  TOPOSTTOIC Boolean To Post to I/C
  ITEMEXISTS Boolean Item Exists
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  STOCKITEM Boolean Stock Item
  ORDERUNIT String*10 Unit of Measure
  ORDERCONV BCD*10.6 Order Unit Conversion
  ORDERDECML Integer Order Unit Decimals
  STOCKUNIT String*10 Unit of Measure
  SQORDERED BCD*10.4 Stocking Quantity Ordered
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  SQCANCELED BCD*10.4 Stocking Quantity Canceled
  SQOUTSTAND BCD*10.4 Stocking Quantity Outstanding
  OQORDERED BCD*10.4 Ordered Quantity Ordered
  OQRECEIVED BCD*10.4 Ordered Quantity Received
  OQCANCELED BCD*10.4 Ordered Quantity Canceled
  OQOUTSTAND BCD*10.4 Ordered Quantity Outstanding
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  GLACEXPENS String*45 Expense Account
  GLNONSTKCR String*45 Non-Stock Clearing Account
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  OEONUMBER String*22 Order Number
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class
  BILLTYPE Integer Billing Type
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  QTYPOSTED Boolean Is Quantity Posted?

## POPORN - Purchase Order Day-end Lines (view PO0629)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ+PORLSEQ
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORLSEQ BCD*10.0 Purchase Order Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ISCOMPLETE Boolean Completed
  ISRECEIVED Boolean Received
  TOPOSTTOIC Boolean To Post to I/C
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  ORDERUNIT String*10 Unit of Measure
  ORDERCONV BCD*10.6 Order Unit Conversion
  ORDERDECML Integer Order Unit Decimals
  STOCKUNIT String*10 Unit of Measure
  SQORDERED BCD*10.4 Stocking Quantity Ordered
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  SQCANCELED BCD*10.4 Stocking Quantity Canceled
  SQOUTSTAND BCD*10.4 Stocking Quantity Outstanding
  OQORDERED BCD*10.4 Ordered Quantity Ordered
  OQRECEIVED BCD*10.4 Ordered Quantity Received
  OQCANCELED BCD*10.4 Ordered Quantity Canceled
  OQOUTSTAND BCD*10.4 Ordered Quantity Outstanding
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  BILLTYPE Integer Billing Type
  BILLRATE BCD*10.6 Billing Rate
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight

## POPORR - Purchase Order Requisitions (view PO0632)
Keys (first = PK; D=dups allowed, M=modifiable): PORHSEQ+PORRREV; RQNHSEQ [D]
Fields (NAME type description [values]):
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORRREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  RQNNUMBER String*22 Requisition Number
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Ordered
  BLNKVDCODE Boolean Use Blank Vendors [0=No,1=Yes]
  USEVDTYPE Integer Use I/C Vendor [0=No,1=Vendor 1,2=Vendor 2,3=Vendor 3,4=Vendor 4,5=Vendor 5,6=Vendor 6,7=Vendor 7,8=Vendor 8,9=Vendor 9]
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]

## POPRXC - Line Cost Proration Details (view PO0650)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ+COSTSEQ
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Proration sequence
  COSTSEQ BCD*10.0 Cost sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRORATE Integer Proration method
  REPRORATE Integer Reproration Method
  SDECIMALS Integer Srce. decimals
  FDECIMALS Integer Func. decimals
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  COSTFLAGS Long Control Flags
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  BILLRATE BCD*10.6 Billing Rate
  AMOUNT BCD*10.3 Amount
  RDECIMALS Integer Rptg. decimals
  RCAMOUNT BCD*10.3 Conversion Tax Reporting Amount
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  SCRTGAMT BCD*10.3 Retainage Amount
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5

## POPRXH - Cost Proration Headers (view PO0656)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Proration sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TOTCBASE BCD*10.3 Total Cost Received
  TOTQBASE BCD*10.4 Total Quantity Received
  TOTWBASE BCD*10.4 Total Weight Received
  TOTCRTNS BCD*10.3 Total Cost Returned
  TOTQRTNS BCD*10.4 Total Quantity Returned
  TOTWRTNS BCD*10.4 Total Weight Returned
  PRVCBASE BCD*10.3 Previous Cost Received
  PRVQBASE BCD*10.4 Previous Quantity Received
  PRVWBASE BCD*10.4 Previous Weight Received
  PRVCRTNS BCD*10.3 Previous Cost Returned
  PRVQRTNS BCD*10.4 Previous Quantity Returned
  PRVWRTNS BCD*10.4 Previous Weight Returned
  REFERENCES BCD*10.0 Number of References
  VERPRORATE Integer Proration Version
  TOTCBASEB BCD*10.3 Billrate Pror. Tot. Cost Rcvd.
  TOTQBASEB BCD*10.4 Billrate Pror. Tot. Qty. Rcvd.
  TOTWBASEB BCD*10.4 Billrate Pror. Tot. Wgt. Rcvd.
  TOTCRTNSB BCD*10.3 Billrate Pror. Tot. Cost Rtrnd.
  TOTQRTNSB BCD*10.4 Billrate Pror. Tot. Qty. Rtrnd.
  TOTWRTNSB BCD*10.4 Billrate Pror. Tot. Wgt. Rtrnd.
  PRVCBASEB BCD*10.3 Billrate Pror. Prv. Cost Rcvd.
  PRVQBASEB BCD*10.4 Billrate Pror. Prv. Qty. Rcvd.
  PRVWBASEB BCD*10.4 Billrate Pror. Prv. Wgt. Rcvd.
  PRVCRTNSB BCD*10.3 Billrate Pror. Prv. Cost Rtrnd.
  PRVQRTNSB BCD*10.4 Billrate Pror. Prv. Qty. Rtrnd.
  PRVWRTNSB BCD*10.4 Billrate Pror. Prv. Wgt. Rtrnd.
  RTGBASE Integer Retainage Base

## POPRXL - Cost Proration Details (view PO0658)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ+LINESEQ
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Proration sequence
  LINESEQ BCD*10.0 Line sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SCEXTENDED BCD*10.3 Amount received
  WTEXTENDED BCD*10.4 Weight received
  RQEXTENDED BCD*10.4 Quantity received
  SCRETURNED BCD*10.3 Amount returned
  WTRETURNED BCD*10.4 Weight returned
  RQRETURNED BCD*10.4 Quantity Returned
  SCEXTENDPR BCD*10.3 Previous Amount Received
  WTEXTENDPR BCD*10.4 Previous Weight Received
  RQEXTENDPR BCD*10.4 Previous Quantity Received
  SCRETURNPR BCD*10.3 Previous Amount Returned
  WTRETURNPR BCD*10.4 Previous Weight Returned
  RQRETURNPR BCD*10.4 Previous Quantity Returned
  LINEFLAGS Long Control Flags
  FORPRORATE Integer Used in Proration
  SCEXTENDPB BCD*10.3 Billrate Pror. Prv. Amt. Rcvd.
  WTEXTENDPB BCD*10.4 Billrate Pror. Prv. Wgt. Rcvd.
  RQEXTENDPB BCD*10.4 Billrate Pror. Prv. Qty. Rcvd.
  SCRETURNPB BCD*10.3 Billrate Pror. Prv. Amt. Rtrnd.
  WTRETURNPB BCD*10.4 Billrate Pror. Prv. Wgt. Rtrnd.
  RQRETURNPB BCD*10.4 Billrate Pror. Prv. Qty. Rtrnd.

## POPRXP - Line Cost Proration Details (view PO0660)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ+LINESEQ+COSTSEQ; PRORSEQ+COSTSEQ+LINESEQ
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Proration sequence
  LINESEQ BCD*10.0 Line sequence
  COSTSEQ BCD*10.0 Cost sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SCVPRORATE BCD*10.3 Srce. Line proration
  FCVPRORATE BCD*10.3 Func. Line proration
  SCDPRORATE BCD*10.3 Srce. Line proration difference
  FCDPRORATE BCD*10.3 Func. Line proration difference
  SCVEXPENSE BCD*10.3 Srce. Line expense
  FCVEXPENSE BCD*10.3 Func. Line expense
  SCDEXPENSE BCD*10.3 Srce. Line expense difference
  FCDEXPENSE BCD*10.3 Func. Line expense difference
  RUNTOTAMT BCD*10.0 Amount proration running total
  SCMPRORATE BCD*10.3 Srce. manual prorate allocated
  RUNTOTBRT BCD*10.0 Billing rate pror. running total
  MBILLRATE BCD*10.6 Manual billing rate pror. alloc.

## PORCAHO - Receipt Audit Hdr. Opt. Fields (view PO0681)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RCPAHSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+RCPAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RCPAHSEQ BCD*10.0 Processing Sequence
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

## PORCALO - Receipt Audit Line Opt. Fields (view PO0682)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RCPAHSEQ+RCPALSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+RCPAHSEQ+RCPALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RCPAHSEQ BCD*10.0 Processing Sequence
  RCPALSEQ BCD*10.0 Line Number
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

## PORCASO - Receipt Audit Cost Opt. Fields (view PO0683)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RCPAHSEQ+RCPASSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+RCPAHSEQ+RCPASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RCPAHSEQ BCD*10.0 Processing Sequence
  RCPASSEQ BCD*10.0 Cost Number
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

## PORCPAH - Receipt Audit Headers (view PO0686)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RCPAHSEQ; VENDOR+DAYENDSEQ+RCPAHSEQ; TRANSDATE+DAYENDSEQ+RCPAHSEQ; RCPNUMBER+DAYENDSEQ+RCPAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RCPAHSEQ BCD*10.0 Processing Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ISPRINTED Boolean Printed [0=No,1=Yes]
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  POSTDATE Date Last Posting Date
  DAYENDDATE Date Day End Processing Date
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  DESCRIPTIO String*60 Description
  TRANSTYPE Integer Transaction Type [1=Receipt,2=Receipt Adjustment,99=Sequence Placeholder (?)]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  RCPCURR String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  FCDOCTOTAL BCD*10.3 Functional Total Cost
  SCDOCTOTAL BCD*10.3 Source Document Total
  COMPLETE Boolean Completed [0=No,1=Yes]
  PRINTED Boolean Printed [0=No,1=Yes]
  MULTIPOR Boolean Multiple Purchase Orders [0=No,1=Yes]
  VALUES Long Optional Fields
  PGMVER String*3 Program Version
  TRANSNUM BCD*10.0 Transaction Number
  VERPRORATE Integer Proration Version [1=3.0A,2=5.3B]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGBASE Integer Retainage Base [0=Total After Taxes,1=Total Before Taxes]
  SCRTGAMT BCD*10.3 Retainage Amount
  HASJOB Boolean Job Related [0=No,1=Yes]
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  DATEBUS Date Posting Date
  VDACCTSET String*6 Vendor Account Set
  CAXAMOUNT BCD*10.3 Reverse Charges Total Amount

## PORCPAL - Receipt Audit Lines (view PO0688)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RCPAHSEQ+RCPALSEQ; DAYENDSEQ+RCPAHSEQ+DETAILNUM+RCPALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RCPAHSEQ BCD*10.0 Processing Sequence
  RCPALSEQ BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  OEONUMBER String*22 Order Number
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  CNTLACCT String*6 Control Account
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  RQRECEIVED BCD*10.4 Quantity Received
  RQCANCELED BCD*10.4 Quantity Canceled
  RCPUNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor to Stocking
  COSTCONV BCD*10.6 Cost unit conversion
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  STOCKUNIT String*10 Unit of Measure
  COSTUNIT String*10 Costing unit of measure
  UNITCOST BCD*10.6 Unit Cost
  PRUNITCOST BCD*10.6 Unit Cost
  LOADEDCOST BCD*10.6 Fully-loaded cost
  RECENTCOST BCD*10.6 Most recent cost
  FCEXTENDED BCD*10.3 Func. Extended Amount
  SCEXTENDED BCD*10.3 Extended Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCPRORATED BCD*10.3 Func. Total Prorate Allocated
  SCPRORATED BCD*10.3 Total Prorate Allocated
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  FCTAXEXCL BCD*10.3 Func. Tax Excluded from Price
  SCTAXEXCL BCD*10.3 Tax Excluded from Price
  FCMPRORATE BCD*10.3 Func. Manual Prorate Allocated
  SCMPRORATE BCD*10.3 Manual Prorate Allocated
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  GLCLEARING String*45 Receipt Clearing Account
  GLITEM String*45 G/L Item
  GLISPOSTED Boolean G/L data to be posted? [0=No,1=Yes]
  RQRECTOTAL BCD*10.4 Total Quantity Received
  SQRECTOTAL BCD*10.4 Total Stock Quantity Received
  FCEXTTOTAL BCD*10.3 Functional Total Cost
  SCEXTTOTAL BCD*10.3 Total Cost
  RCPDAYS Integer Days to Receive
  LASTCOST BCD*10.6 Last Unit Cost
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  PONUMBER String*22 Purchase Order Number
  QIVALINSTK Boolean Item Valuation Qty. In Stocking [0=No,1=Yes]
  DISCPCT BCD*5.5 Discount Percentage
  FCDISCOUNT BCD*10.3 Func. Discount Amount
  SCDISCOUNT BCD*10.3 Discount Amount
  FCDISCTOT BCD*10.3 Functional Total Discount
  SCDISCTOT BCD*10.3 Total Discount
  VALUES Long Optional Fields
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  SCRTGAMT BCD*10.3 Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  DFCUNITCST BCD*10.6 Func. Unit Cost Difference
  DSCUNITCST BCD*10.6 Unit Cost Difference
  DBILLRATE BCD*10.6 Billing Rate Difference
  PMTRANSNUM Long PJC Transaction Number
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  TOTDEFEXWT BCD*10.4 Total Def. Ext. Weight
  DQRECEIVED BCD*10.4 Delta Quantity Received
  DELTACONVE BCD*10.6 Delta Unit Conversion
  DELTAUNIT String*10 Delta Unit
  DETAILNUM Integer Detail Number

## PORCPAQ - Receipt Audit Prorate Lines (view PO0690)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RCPAHSEQ+RCPALSEQ+RCPASSEQ; DAYENDSEQ+RCPAHSEQ+RCPALSEQ+CURRENCY+RCPASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RCPAHSEQ BCD*10.0 Processing Sequence
  RCPALSEQ BCD*10.0 Line Number
  RCPASSEQ BCD*10.0 Cost Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  GLITEM String*45 G/L Item
  GLEXPENSE String*45 Return Account
  GLCLEARING String*45 Receipt Clearing Account
  POSTCLEARI Boolean Post to clearing account? [0=No,1=Yes]
  CURRENCY String*3 Currency
  SCURNDECML Integer Decimal Places
  FCITEM BCD*10.3 Func. Item Amount
  SCITEM BCD*10.3 Item amount
  FCEXPENSE BCD*10.3 Func. Expensed Amount
  SCEXPENSE BCD*10.3 Expensed amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  BILLRATE BCD*10.6 Billing Rate
  BCBILLRATE BCD*10.6 (BC) Billing Rate
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  BCRATE BCD*8.7 Billing Currency Conversion Rate
  BCRATEDATE Date Billing Currency Conv. Rate Date
  BCRATETYPE String*2 Billing Currency Conv. Rate Type
  BCRATEOPER Integer Billing Curr. Cv. Rate Operation [1=Multiply,2=Divide]
  BCRATEXIST Boolean Billing Curr. Conv. Rate Exists [0=No,1=Yes]
  PMTRANSNUM Long PJC Transaction Number
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed

## PORCPAS - Receipt Audit Costs (view PO0692)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RCPAHSEQ+RCPASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RCPAHSEQ BCD*10.0 Processing Sequence
  RCPASSEQ BCD*10.0 Cost Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  INVNUMBER String*22 Invoice Number
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method [1=Leave,2=Prorate,3=Expense]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXVCLASS1 Integer Vendor Tax Class 1
  TAXVCLASS2 Integer Vendor Tax Class 2
  TAXVCLASS3 Integer Vendor Tax Class 3
  TAXVCLASS4 Integer Vendor Tax Class 4
  TAXVCLASS5 Integer Vendor Tax Class 5
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  CURRENCY String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  FCTAXEXCL BCD*10.3 Func. Tax Excluded from Price
  SCTAXEXCL BCD*10.3 Tax Excluded from Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  VALUES Long Optional Fields
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  GLNOPRORCR String*45 Expensed Add'l Cost Clr. Acct.
  NOPRORTOGL Boolean Exp. Add'l Cost G/L data posted? [0=No,1=Yes]
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  CALCOVRHD Boolean Calculate Overhead [0=No,1=Yes]
  CALCLABOR Boolean Calculate Labor [0=No,1=Yes]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  SCRTGAMT BCD*10.3 Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  PMTRANSNUM Long PJC Transaction Number
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed

## PORCPC - Receipt Comments (view PO0695)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPCREV; RCPHSEQ+RCPCSEQ [D]
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPCREV BCD*10.0 Comment Identifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCPCSEQ BCD*10.0 Receipt Comment Sequence
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  COMMENTTYP Integer Line Type [1=Comment,2=Instruction]
  COMMENT String*80 Comment

## PORCPD - Receipt Cost Distributions (view PO0696)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+VDCODE+RCPSREV+LSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  VDCODE String*12 Vendor
  RCPSREV BCD*10.0 Line Number
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]

## PORCPE - Receipt Posting Cost Distribs. (view PO0697)
Keys (first = PK; D=dups allowed, M=modifiable): RCPISEQ+RCPHSEQ+RCPSSEQ+LSEQ
Fields (NAME type description [values]):
  RCPISEQ BCD*10.0 Header Sequence
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate

## PORCPF - Receipt Day-end Cost Distribs. (view PO0698)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPSSEQ+LSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  LSEQ BCD*10.0 Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AMOUNT BCD*10.3 Amount
  BILLRATE BCD*10.6 Billing Rate

## PORCPH1 - Receipts (view PO0700)
Physical tables of this view: PORCPH1, PORCPH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ; RCPNUMBER; PONUMBER+RCPNUMBER; VDCODE+RCPHSEQ [M]; PORHSEQ [D]; VDCODE+RCPNUMBER [M]
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTLSEQ BCD*10.0 Next Line Sequence
  LINES Long Lines
  LINESPRORA Long Number of Lines Prorated
  LINESCMPL Long Lines Complete
  COSTS Long Costs
  COSTSPRORA Long Number of Costs Prorated
  COSTSCMPL Long Costs Complete
  VENDS Long Vendors
  VENDSCMPL Long Vendors Completed
  VENDSINVC Long Vendors Invoiced
  TAXLINES Long Lines Tax Calculation Sees
  EXTRANEOUS Long Extraneous Line Count
  TAXAUTOCAL Boolean Auto. tax calculation on save [0=No,1=Yes]
  ISPRINTED Boolean Printed [0=No,1=Yes]
  ISINVOICED Boolean Invoiced [0=No,1=Yes]
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  POSTDATE Date Last Posting Date
  DATE Date Receipt Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  RCPNUMBER String*22 Receipt Number
  TEMPLATE String*6 Template Code
  FOBPOINT String*60 FOB Point
  VDCODE String*12 Vendor
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDNAME String*60 Name
  VDADDRESS1 String*60 Address 1
  VDADDRESS2 String*60 Address 2
  VDADDRESS3 String*60 Address 3
  VDADDRESS4 String*60 Address 4
  VDCITY String*30 City
  VDSTATE String*30 State/Province
  VDZIP String*20 Zip/Postal Code
  VDCOUNTRY String*30 Country
  VDPHONE String*30 Phone Number
  VDFAX String*30 Fax Number
  VDCONTACT String*60 Contact
  TERMSCODE String*6 Terms Code
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PONUMBER String*22 Purchase Order Number
  INVNUMBER String*22 Invoice Number
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  VIACODE String*6 Ship-Via
  VIANAME String*60 Ship-Via Name
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  SPREAD BCD*8.7 Rate Spread
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  EXTWEIGHT BCD*10.4 Extended Weight
  EXTENDED BCD*10.3 Extended Cost
  DOCTOTAL BCD*10.3 Total
  AMOUNT BCD*10.3 Additional Costs
  RQRECEIVED BCD*10.4 Quantity Received
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXEXCLUDE1 BCD*10.3 Excluded Tax Amount 1
  TXEXCLUDE2 BCD*10.3 Excluded Tax Amount 2
  TXEXCLUDE3 BCD*10.3 Excluded Tax Amount 3
  TXEXCLUDE4 BCD*10.3 Excluded Tax Amount 4
  TXEXCLUDE5 BCD*10.3 Excluded Tax Amount 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  MPRORATED BCD*10.3 Manual Proration Total
  MTOPRORATE BCD*10.3 Manual To Prorate
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  MULTIPOR Boolean Multiple Purchase Orders [0=No,1=Yes]
  PORS Long Purchase Orders
  VDEMAIL String*50 E-mail
  VDPHONEC String*30 Contact Phone
  VDFAXC String*30 Contact Fax
  VDEMAILC String*50 Contact E-mail
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  VALUES Long Optional Fields
  VERPRORATE Integer Proration Version [1=3.0A,2=5.3B]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGTERMS String*6 Retainage Terms Code
  JOBLINES Long Job Related Lines
  JOBCOSTS Long Job Related Costs
  BILLLINES Long Billable Lines
  COSTSBLPRO Long Cost Billing Rates Prorated
  RTGBASE Integer Retainage Base [0=Total After Taxes,1=Total Before Taxes]
  RTGAMOUNT BCD*10.3 Retainage Amount
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  SPREADRC BCD*8.7 Tax Reporting Rate Spread
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEMTCHRC Integer Tax Reporting Rate Match Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TREXCLUDE1 BCD*10.3 Tax Reporting Excluded Amount 1
  TREXCLUDE2 BCD*10.3 Tax Reporting Excluded Amount 2
  TREXCLUDE3 BCD*10.3 Tax Reporting Excluded Amount 3
  TREXCLUDE4 BCD*10.3 Tax Reporting Excluded Amount 4
  TREXCLUDE5 BCD*10.3 Tax Reporting Excluded Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RTGTAXREP Integer Report Retainage Tax [0=At Time of Original Document,1=As Per Tax Authority]
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## PORCPH2 - Receipts (view PO0700)
Physical tables of this view: PORCPH1, PORCPH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BTCODE String*6 Bill-To Location
  BTDESC String*60 Bill-To Location Description
  BTADDRESS1 String*60 Bill-To Address 1
  BTADDRESS2 String*60 Bill-To Address 2
  BTADDRESS3 String*60 Bill-To Address 3
  BTADDRESS4 String*60 Bill-To Address 4
  BTCITY String*30 Bill-To City
  BTSTATE String*30 Bill-To State/Province
  BTZIP String*20 Bill-To Zip/Postal Code
  BTCOUNTRY String*30 Bill-To Country
  BTPHONE String*30 Bill-To Phone Number
  BTFAX String*30 Bill-To Fax Number
  BTCONTACT String*60 Bill-To Contact
  STCODE String*6 Ship-To Location
  STDESC String*60 Ship-To Location Description
  STADDRESS1 String*60 Ship-To Address 1
  STADDRESS2 String*60 Ship-To Address 2
  STADDRESS3 String*60 Ship-To Address 3
  STADDRESS4 String*60 Ship-To Address 4
  STCITY String*30 Ship-To City
  STSTATE String*30 Ship-To State/Province
  STZIP String*20 Ship-To Zip/Postal Code
  STCOUNTRY String*30 Ship-To Country
  STPHONE String*30 Ship-To Phone Number
  STFAX String*30 Ship-To Fax Number
  STCONTACT String*60 Ship-To Contact
  PDRATE BCD*8.7 Predecessor's Exchange Rate
  PDRATETYPE String*2 Predecessor's Rate Type
  PDRATEDATE Date Predecessor's Rate Date
  PDRATEOPER Integer Predecessor's Rate Operation [1=Multiply,2=Divide]
  PDRATEOVER Boolean Predecessor's Rate Overridden [0=No,1=Yes]
  BTEMAIL String*50 Bill-To E-mail
  BTPHONEC String*30 Bill-To Contact Phone
  BTFAXC String*30 Bill-To Contact Fax
  BTEMAILC String*50 Bill-To Contact E-mail
  STEMAIL String*50 Ship-To E-mail
  STPHONEC String*30 Ship-To Contact Phone
  STFAXC String*30 Ship-To Contact Fax
  STEMAILC String*50 Ship-To Contact E-mail
  PDRATERC BCD*8.7 Pred. Tax Reporting Exch. Rate
  PDRATTYPRC String*2 Pred. Tax Reporting Rate Type
  PDRATEDTRC Date Pred. Tax Reporting Rate Date
  PDRATEOPRC Integer Pred. Tax Reporting Rate Oper. [1=Multiply,2=Divide]
  PDRATERCOV Boolean Pred. Tax Reporting Rate Overrd. [0=No,1=Yes]
  VDACCTSET String*6 Vendor Account Set
  DATEBUS Date Posting Date
  ENTEREDBY String*8 Entered By
  DETAILNEXT Integer Next Detail Number
  CAXBASE1 BCD*10.3 Reverse Charges Base 1
  CAXBASE2 BCD*10.3 Reverse Charges Base 2
  CAXBASE3 BCD*10.3 Reverse Charges Base 3
  CAXBASE4 BCD*10.3 Reverse Charges Base 4
  CAXBASE5 BCD*10.3 Reverse Charges Base 5
  CAXDTAMT1 BCD*10.3 Reverse Charges Detail Amount 1
  CAXDTAMT2 BCD*10.3 Reverse Charges Detail Amount 2
  CAXDTAMT3 BCD*10.3 Reverse Charges Detail Amount 3
  CAXDTAMT4 BCD*10.3 Reverse Charges Detail Amount 4
  CAXDTAMT5 BCD*10.3 Reverse Charges Detail Amount 5
  CAXAPPLY1 Boolean Reverse Charges Applied 1 [0=No,1=Yes]
  CAXAPPLY2 Boolean Reverse Charges Applied 2 [0=No,1=Yes]
  CAXAPPLY3 Boolean Reverse Charges Applied 3 [0=No,1=Yes]
  CAXAPPLY4 Boolean Reverse Charges Applied 4 [0=No,1=Yes]
  CAXAPPLY5 Boolean Reverse Charges Applied 5 [0=No,1=Yes]
  CAXAMOUNT1 BCD*10.3 Reverse Charges Amount 1
  CAXAMOUNT2 BCD*10.3 Reverse Charges Amount 2
  CAXAMOUNT3 BCD*10.3 Reverse Charges Amount 3
  CAXAMOUNT4 BCD*10.3 Reverse Charges Amount 4
  CAXAMOUNT5 BCD*10.3 Reverse Charges Amount 5

## PORCPHO - Receipt Optional Fields (view PO0703)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+OPTFIELD; OPTFIELD+RCPHSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
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

## PORCPI - Receipt Postings (view PO0701)
Keys (first = PK; D=dups allowed, M=modifiable): RCPISEQ; RCPHSEQ [D]
Fields (NAME type description [values]):
  RCPISEQ BCD*10.0 Header Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  POSTDATE Date Last Posting Date
  ISPRINTED Boolean Printed [0=No,1=Yes]
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate
  SCRTGAMT BCD*10.3 Retainage Amount
  CAXAMOUNT BCD*10.3 Reverse Charges Total Amount

## PORCPJ - Receipt Day-ends (view PO0702)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRORATESEQ BCD*10.0 Prorate Model Sequence
  POSTDATE Date Last Posting Date
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  ISCOMPLETE Boolean Completed
  DTCOMPLETE Date Date Completed
  SCRTGAMT BCD*10.3 Retainage Amount
  CAXAMOUNT BCD*10.3 Reverse Charges Total Amount

## PORCPL - Receipt Lines (view PO0710)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPLREV; RCPHSEQ+RCPLSEQ; OEONUMBER+RCPHSEQ+RCPLSEQ [M]; RCPLSEQ [D,M]; PORHSEQ+PORLSEQ+RCPHSEQ+RCPLSEQ; RCPHSEQ+DETAILNUM+RCPLSEQ [M]
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  RCPCSEQ BCD*10.0 Receipt Comment Sequence
  OEONUMBER String*22 Order Number
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  POSTEDTOIC Boolean Posted to I/C [0=No,1=Yes]
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORLSEQ BCD*10.0 Purchase Order Line Sequence
  POCOMPLETE Boolean Completes PO [0=No,1=Yes]
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  VENDITEMNO String*24 Vendor Item Number
  HASCOMMENT Boolean Comments [0=No,1=Yes]
  ORDERUNIT String*10 Unit of Measure
  ORDERCONV BCD*10.6 Order Unit Conversion
  ORDERDECML Integer Order Unit Decimals
  RCPUNIT String*10 Unit of Measure
  RCPCONV BCD*10.6 Receiving Conversion Factor
  RCPDECML Integer Receiving Unit Decimals
  STOCKDECML Integer Stock Unit Decimals
  OQORDERED BCD*10.4 Ordered Quantity Ordered
  OQPREVRECV BCD*10.4 Ordered Previously Received
  OQOUTSTPO BCD*10.4 Ordered Outstanding on PO
  RQRECEIVED BCD*10.4 Quantity Received
  RQCANCELED BCD*10.4 Quantity Canceled
  RQOUTSTAND BCD*10.4 Quantity Outstanding
  SQORDERED BCD*10.4 Stocking Quantity Ordered
  SQPREVRECV BCD*10.4 Stocking Previously Received
  SQOUTSTPO BCD*10.4 Stocking Outstanding on PO
  RQORDERED BCD*10.4 Quantity Ordered
  RQPREVRECV BCD*10.4 Received to Date
  RQOUTSTPO BCD*10.4 Quantity Outstanding
  RQRCPEXTRA BCD*10.4 Receiving Qty. Received Extra
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  SQCANCELED BCD*10.4 Stocking Quantity Canceled
  SQOUTSTAND BCD*10.4 Stocking Quantity Outstanding
  SQRCPEXTRA BCD*10.4 Stocking Quantity Received Extra
  OQRECEIVED BCD*10.4 Ordered Quantity Received
  OQCANCELED BCD*10.4 Ordered Quantity Canceled
  OQOUTSTAND BCD*10.4 Ordered Quantity Outstanding
  OQRCPEXTRA BCD*10.4 Received Extra
  RQRETURNED BCD*10.4 Quantity Returned
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  OQRETURNED BCD*10.4 Ordered Quantity Returned
  RQSTOCKED BCD*10.4 Quantity Stocked
  SQSTOCKED BCD*10.4 Stocking Quantity Stocked
  OQSTOCKED BCD*10.4 Ordered Quantity Stocked
  RQINADJUST BCD*10.4 Quantity Adjusted by Invoice
  SQINADJUST BCD*10.4 Stocking Qty. Adj. by Invoice
  OQINADJUST BCD*10.4 Ordered Quantity Adj. by Invoice
  RQPOFILLED BCD*10.4 Quantity Filled on PO
  SQPOFILLED BCD*10.4 Stocking Quantity Filled on PO
  OQPOFILLED BCD*10.4 Ordered Quantity Filled on PO
  RQSETTLED BCD*10.4 Quantity Settled
  SQSETTLED BCD*10.4 Stocking Quantity Settled
  OQSETTLED BCD*10.4 Ordered Quantity Settled
  RQUSTOCKED BCD*10.4 Quantity Unstocked
  SQUSTOCKED BCD*10.4 Stocking Quantity Unstocked
  OQUSTOCKED BCD*10.4 Ordered Quantity Unstocked
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Recoverable Tax
  TXEXPSAMT BCD*10.3 Expensed Tax
  TXALLOAMT BCD*10.3 Allocated Tax
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  GLACEXPENS String*45 Expense Account
  DTARRIVAL Date Arrival Date
  LABELCOUNT Integer Number of Labels
  MPRORATED BCD*10.3 Manual Proration
  HASDROPSHI Boolean Drop-Ship [0=No,1=Yes]
  DROPTYPE Integer Drop-Ship Type [2=Address Entered,3=Inventory Location Address,4=Customer Address,5=Customer Ship-To Address]
  IDCUST String*12 Drop-Ship Customer
  IDCUSTSHPT String*6 Customer Ship-To Address
  DLOCATION String*6 Drop-Ship Location
  DESC String*60 Drop-Ship Description
  ADDRESS1 String*60 Drop-Ship Address 1
  ADDRESS2 String*60 Drop-Ship Address 2
  ADDRESS3 String*60 Drop-Ship Address 3
  ADDRESS4 String*60 Drop-Ship Address 4
  CITY String*30 Drop-Ship City
  STATE String*30 Drop-Ship State/Province
  ZIP String*20 Drop-Ship Zip/Postal Code
  COUNTRY String*30 Drop-Ship Country
  PHONE String*30 Drop-Ship Phone Number
  FAX String*30 Drop-Ship Fax Number
  CONTACT String*60 Drop-Ship Contact
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  PONUMBER String*22 Purchase Order Number
  EMAIL String*50 Drop-Ship E-mail
  PHONEC String*30 Drop-Ship Contact Phone
  FAXC String*30 Drop-Ship Contact Fax
  EMAILC String*50 Drop-Ship Contact E-mail
  GLNONSTKCR String*45 Non-Stock Clearing Account
  MANITEMNO String*24 Manufacturer's Item Number
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  XIRQRECEVD BCD*10.4 Part. Inv. Pv. Qty. Invoicied.
  XIEXTWGHT BCD*10.4 Part. Inv. Pv. Ext. Wgt. Invcd.
  XINETXTEND BCD*10.3 Part. Inv. Pv. Net Cost Invoiced
  INVLINES Long Invoice Lines
  VALUES Long Optional Fields
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  UCISMANUAL Boolean Unit Cost is Manual [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  XIDEFEXTWT BCD*10.4 Part. Inv. Pv. Def. Ext. W. Inv.
  FASDETAIL Boolean Fixed Asset [0=No,1=Yes]
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]
  DETAILNUM Integer Detail Number
  CAXABLE1 Boolean Reverse Chargeable 1 [0=No,1=Yes]
  CAXABLE2 Boolean Reverse Chargeable 2 [0=No,1=Yes]
  CAXABLE3 Boolean Reverse Chargeable 3 [0=No,1=Yes]
  CAXABLE4 Boolean Reverse Chargeable 4 [0=No,1=Yes]
  CAXABLE5 Boolean Reverse Chargeable 5 [0=No,1=Yes]

## PORCPLF - Receipt Sage Fixed Assets Details (view PO0709)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPLSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  FASCREATED Boolean Asset Created [0=No,1=Yes]
  FASDB String*32 Sage Fixed Assets Database
  FASCMP String*32 Sage Fixed Assets Company/Org.
  FASTMPL String*25 Sage Fixed Assets Template
  TEXTDESC String*80 Sage Fixed Assets Asset Description
  SEPQTY Boolean Separate Assets [0=No,1=Yes]
  FASQTY BCD*10.5 Sage Fixed Assets Quantity
  UOM String*10 Sage Fixed Assets Unit of Measure
  AMTSC BCD*10.3 Sage Fixed Assets Asset Value

## PORCPLL - Receipt Line Lots (view PO0789)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPLREV+LOTNUMF; LOTNUMF+RCPHSEQ+RCPLREV
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLREV BCD*10.0 Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Lot Quantity
  QTYSQ BCD*10.4 Lot Stock Quantity

## PORCPLO - Receipt Detail Optional Fields (view PO0717)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPLREV+OPTFIELD; OPTFIELD+RCPHSEQ+RCPLREV
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLREV BCD*10.0 Line Number
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

## PORCPLS - Receipt Line Serials (view PO0780)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPLREV+SERIALNUMF; SERIALNUMF+RCPHSEQ+RCPLREV
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLREV BCD*10.0 Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCPLSEQ BCD*10.0 Receipt Line Sequence

## PORCPM - Receipt Posting Lines (view PO0711)
Keys (first = PK; D=dups allowed, M=modifiable): RCPISEQ+RCPHSEQ+RCPLSEQ
Fields (NAME type description [values]):
  RCPISEQ BCD*10.0 Header Sequence
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  ITEMDESC String*60 Item Description
  STOCKUNIT String*10 Unit of Measure
  RCPUNIT String*10 Unit of Measure
  RCPCONV BCD*10.6 Receiving Conversion Factor
  RCPDECML Integer Receiving Unit Decimals
  RQRECEIVED BCD*10.4 Quantity Received
  RQRETURNED BCD*10.4 Quantity Returned
  RQCANCELED BCD*10.4 Quantity Canceled
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  SQCANCELED BCD*10.4 Stocking Quantity Canceled
  OQRECEIVED BCD*10.4 Ordered Quantity Received
  OQCANCELED BCD*10.4 Ordered Quantity Canceled
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.3 Extended Weight
  RCPDAYS Integer Days to Receive
  MPRORATED BCD*10.3 Manual Proration
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXINCLUD1 Integer Tax Includable 1
  TAXINCLUD2 Integer Tax Includable 2
  TAXINCLUD3 Integer Tax Includable 3
  TAXINCLUD4 Integer Tax Includable 4
  TAXINCLUD5 Integer Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  QTYPOSTED Boolean Is Quantity Posted?
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity

## PORCPML - Receipt Posting Lines Lots (view PO0781)
Keys (first = PK; D=dups allowed, M=modifiable): RCPISEQ+RCPHSEQ+RCPLSEQ+LOTNUMF; LOTNUMF+RCPISEQ+RCPHSEQ+RCPLSEQ
Fields (NAME type description [values]):
  RCPISEQ BCD*10.0 Header Sequence
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RQPREV BCD*10.4 Old Quantity
  RQCURR BCD*10.4 Current Quantity
  SQPREV BCD*10.4 Old Stocking Quantity
  SQCURR BCD*10.4 Current Stocking Quantity
  OPERATION Integer Operation To Post

## PORCPMS - Receipt Posting Lines Serials (view PO0788)
Keys (first = PK; D=dups allowed, M=modifiable): RCPISEQ+RCPHSEQ+RCPLSEQ+SERIALNUMF; SERIALNUMF+RCPISEQ+RCPHSEQ+RCPLSEQ
Fields (NAME type description [values]):
  RCPISEQ BCD*10.0 Header Sequence
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post

## PORCPN - Receipt Day-end Lines (view PO0712)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPLSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60 Item Description
  STOCKUNIT String*10 Unit of Measure
  RCPUNIT String*10 Unit of Measure
  RCPCONV BCD*10.6 Receiving Conversion Factor
  RCPDECML Integer Receiving Unit Decimals
  RQRECEIVED BCD*10.4 Receiving Quantity Received
  RQRETURNED BCD*10.4 Quantity Returned
  RQCANCELED BCD*10.4 Receiving Quantity Canceled
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  SQCANCELED BCD*10.4 Stocking Quantity Canceled
  OQRECEIVED BCD*10.4 Ordered Quantity Received
  OQCANCELED BCD*10.4 Ordered Quantity Canceled
  RQPOFILLED BCD*10.4 Receiving Quantity Filled on PO
  SQPOFILLED BCD*10.4 Stocking Quantity Filled on PO
  OQPOFILLED BCD*10.4 Ordered Quantity Filled on PO
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  MPRORATED BCD*10.3 Manual Proration
  RCPDAYS Integer Days to Receive
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Integer Tax Includable 1
  TAXINCLUD2 Integer Tax Includable 2
  TAXINCLUD3 Integer Tax Includable 3
  TAXINCLUD4 Integer Tax Includable 4
  TAXINCLUD5 Integer Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight

## PORCPR - Receipt Purchase Orders (view PO0705)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPRREV; RCPHSEQ+PORHSEQ; PORHSEQ [D]
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPRREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PONUMBER String*22 Purchase Order Number
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]

## PORCPS - Receipt Additional Costs (view PO0713)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+VDCODE+RCPSREV; RCPHSEQ+RCPSSEQ; RCPHSEQ+VDCODE+RCPSSEQ; RCPSSEQ+RCPHSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  VDCODE String*12 Vendor
  RCPSREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  ADDCOST String*6 Additional Cost
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method [1=Leave,2=Prorate,3=Expense]
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  VALUES Long Optional Fields
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  CALCOVRHD Boolean Calculate Overhead [0=No,1=Yes]
  CALCLABOR Boolean Calculate Labor [0=No,1=Yes]
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  COSTDISTS Long Cost Distributions
  MANDISTS Long Manual Cost Distributions
  EXTDISTS Long Extraneous Cost Distributions
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## PORCPSO - Receipt Add. Cost Opt. Field (view PO0719)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+VDCODE+RCPSREV+OPTFIELD; OPTFIELD+RCPHSEQ+VDCODE+RCPSREV
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  VDCODE String*12 Vendor
  RCPSREV BCD*10.0 Line Number
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

## PORCPT - Receipt Posting Additional Costs (view PO0715)
Keys (first = PK; D=dups allowed, M=modifiable): RCPISEQ+RCPHSEQ+RCPSSEQ
Fields (NAME type description [values]):
  RCPISEQ BCD*10.0 Header Sequence
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method
  REPRORATE Integer Reproration Method
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation
  RATEOVER Boolean Rate Overridden
  SCURNDECML Integer Decimal Places
  VDCODE String*12 Vendor
  VDNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXVCLASS1 Integer Vendor Tax Class 1
  TAXVCLASS2 Integer Vendor Tax Class 2
  TAXVCLASS3 Integer Vendor Tax Class 3
  TAXVCLASS4 Integer Vendor Tax Class 4
  TAXVCLASS5 Integer Vendor Tax Class 5
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  MTOPRORATE BCD*10.3 Manual To Prorate
  BILLRATE BCD*10.6 Billing Rate
  HASRTG Boolean Has Retainage
  RTGRATE Integer Retainage Exchange Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEMTCHRC Integer Tax Reporting Rate Match Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation
  RATERCOVER Boolean Tax Reporting Rate Overridden
  RCURNDECML Integer Tax Reporting Decimal Places
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## PORCPU - Receipt Day-end Additional Costs (view PO0716)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+RCPSSEQ
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPSSEQ BCD*10.0 Receipt Cost Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  GLEXPACCT String*45 Expense Account
  GLRETACCT String*45 Return Account
  AMOUNT BCD*10.3 Amount
  PRORMETHOD Integer Proration Method
  REPRORATE Integer Reproration Method
  MTOPRORATE BCD*10.3 Manual To Prorate
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation
  SCURNDECML Integer Decimal Places
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEMTCHRC Integer Tax Reporting Rate Match Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation
  RCURNDECML Integer Tax Reporting Decimal Places
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## PORCPV - Receipt Vendors (view PO0718)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+VDCODE
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  VDCODE String*12 Vendor
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COSTS Long Costs
  COSTSPRORA Long Number of Costs Prorated
  COSTSCMPL Long Costs Complete
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  TAXAUTOCAL Boolean Auto. tax calculation on save [0=No,1=Yes]
  ISINVOICED Boolean Invoiced [0=No,1=Yes]
  INVNUMBER String*22 Invoice Number
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDNAME String*60 Name
  VDADDRESS1 String*60 Address 1
  VDADDRESS2 String*60 Address 2
  VDADDRESS3 String*60 Address 3
  VDADDRESS4 String*60 Address 4
  VDCITY String*30 City
  VDSTATE String*30 State/Province
  VDZIP String*20 Zip/Postal Code
  VDCOUNTRY String*30 Country
  VDPHONE String*30 Phone Number
  VDFAX String*30 Fax Number
  VDCONTACT String*60 Contact
  TERMSCODE String*6 Terms Code
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  SPREAD BCD*8.7 Rate Spread
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  DOCTOTAL BCD*10.3 Total
  AMOUNT BCD*10.3 Amount
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXEXCLUDE1 BCD*10.3 Excluded Tax Amount 1
  TXEXCLUDE2 BCD*10.3 Excluded Tax Amount 2
  TXEXCLUDE3 BCD*10.3 Excluded Tax Amount 3
  TXEXCLUDE4 BCD*10.3 Excluded Tax Amount 4
  TXEXCLUDE5 BCD*10.3 Excluded Tax Amount 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  MTOPRORATE BCD*10.3 Manual To Prorate
  TAXLINES Long Lines Tax Calculation Sees
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  VDEMAIL String*50 E-mail
  VDPHONEC String*30 Contact Phone
  VDFAXC String*30 Contact Fax
  VDEMAILC String*50 Contact E-mail
  VALUES Long Optional Fields
  JOBCOSTS Long Job Related Costs
  COSTSBLPRO Long Cost Billing Rates Prorated
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGTERMS String*6 Retainage Terms Code
  RTGAMOUNT BCD*10.3 Retainage Amount
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  SPREADRC BCD*8.7 Tax Reporting Rate Spread
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEMTCHRC Integer Tax Reporting Rate Match Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TREXCLUDE1 BCD*10.3 Tax Reporting Excluded Amount 1
  TREXCLUDE2 BCD*10.3 Tax Reporting Excluded Amount 2
  TREXCLUDE3 BCD*10.3 Tax Reporting Excluded Amount 3
  TREXCLUDE4 BCD*10.3 Tax Reporting Excluded Amount 4
  TREXCLUDE5 BCD*10.3 Tax Reporting Excluded Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  VDACCTSET String*6 Vendor Account Set

## PORCPVO - Receipt Vendors Optional Fields (view PO0721)
Keys (first = PK; D=dups allowed, M=modifiable): RCPHSEQ+VDCODE+OPTFIELD; OPTFIELD+RCPHSEQ+VDCODE
Fields (NAME type description [values]):
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  VDCODE String*12 Vendor
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

## POREAHO - Return Audit Hdr. Opt. Fields (view PO0740)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RETAHSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+RETAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RETAHSEQ BCD*10.0 Processing Sequence
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

## POREALO - Return Audit Line Opt. Fields (view PO0741)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RETAHSEQ+RETALSEQ+OPTFIELD; OPTFIELD+DAYENDSEQ+RETAHSEQ+RETALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RETAHSEQ BCD*10.0 Processing Sequence
  RETALSEQ BCD*10.0 Line Number
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

## PORETAH - Return Audit Headers (view PO0724)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RETAHSEQ; VENDOR+DAYENDSEQ+RETAHSEQ; TRANSDATE+DAYENDSEQ+RETAHSEQ; RETNUMBER+DAYENDSEQ+RETAHSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RETAHSEQ BCD*10.0 Processing Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ISPRINTED Boolean Printed [0=No,1=Yes]
  RETHSEQ BCD*10.0 Return Sequence Key
  POSTDATE Date Last Posting Date
  DAYENDDATE Date Day End Processing Date
  TRANSDATE Date Transaction Date
  REFERENCE String*60 Reference
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period
  DESCRIPTIO String*60 Description
  TRANSTYPE Integer Transaction Type [1=Receipt,2=Receipt Adjustment,3=Return,99=Sequence Placeholder (?)]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  RETNUMBER String*22 Return Number
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  RCPCURR String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  FCDOCTOTAL BCD*10.3 Functional Total Cost
  SCDOCTOTAL BCD*10.3 Source Document Total
  COMPLETE Boolean Completed [0=No,1=Yes]
  PRINTED Boolean Printed [0=No,1=Yes]
  VALUES Long Optional Fields
  PGMVER String*3 Program Version
  VERPRORATE Integer Proration Version [1=3.0A,2=5.3B]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGBASE Integer Retainage Base [0=Total After Taxes,1=Total Before Taxes]
  SCRTGAMT BCD*10.3 Retainage Amount
  HASJOB Boolean Job Related [0=No,1=Yes]
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  DATEBUS Date Posting Date
  VDACCTSET String*6 Vendor Account Set

## PORETAL - Return Audit Lines (view PO0726)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RETAHSEQ+RETALSEQ; DAYENDSEQ+RETAHSEQ+DETAILNUM+RETALSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RETAHSEQ BCD*10.0 Processing Sequence
  RETALSEQ BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  OEONUMBER String*22 Order Number
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  CNTLACCT String*6 Control Account
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  RQRETURNED BCD*10.4 Quantity Returned
  RETUNIT String*10 Unit of Measure
  CONVERSION BCD*10.6 Conversion Factor to Stocking
  COSTCONV BCD*10.6 Cost unit conversion
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  STOCKUNIT String*10 Unit of Measure
  COSTUNIT String*10 Costing unit of measure
  UNITCOST BCD*10.6 Unit Cost
  PRUNITCOST BCD*10.6 Unit Cost
  LOADEDCOST BCD*10.6 Fully-loaded cost
  FCEXTENDED BCD*10.3 Func. Extended Amount
  SCEXTENDED BCD*10.3 Extended Amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCPRORATED BCD*10.3 Func. Total Prorate Allocated
  SCPRORATED BCD*10.3 Total Prorate Allocated
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  FCTAXEXCL BCD*10.3 Func. Tax Excluded from Price
  SCTAXEXCL BCD*10.3 Tax Excluded from Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  GLCLEARING String*45 Receipt Clearing Account
  GLITEM String*45 G/L Item
  GLISPOSTED Boolean G/L data to be posted? [0=No,1=Yes]
  GLISDEBIT Boolean Normal G/L debit convention? [0=No,1=Yes]
  RQRETTOTAL BCD*10.4 Total Quantity Returned
  SQRETTOTAL BCD*10.4 Total Stock Quantity Returned
  FCEXTTOTAL BCD*10.3 Functional Total Cost
  SCEXTTOTAL BCD*10.3 Total Cost
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  PONUMBER String*22 Purchase Order Number
  DISCPCT BCD*5.5 Discount Percentage
  FCDISCOUNT BCD*10.3 Func. Discount Amount
  SCDISCOUNT BCD*10.3 Discount Amount
  FCDISCTOT BCD*10.3 Functional Total Discount
  SCDISCTOT BCD*10.3 Total Discount
  VALUES Long Optional Fields
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  RETLSEQ BCD*10.0 Return Line Sequence
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  SCRTGAMT BCD*10.3 Retainage Amount
  SCRTGAMTOT BCD*10.3 Total Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  DFCUNITCST BCD*10.6 Func. Unit Cost Difference
  DSCUNITCST BCD*10.6 Unit Cost Difference
  DBILLRATE BCD*10.6 Billing Rate Difference
  PMTRANSNUM Long PJC Transaction Number
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  TOTDEFEXWT BCD*10.4 Total Def. Ext. Weight
  DETAILNUM Integer Detail Number

## PORETAQ - Return Audit Prorate Lines (view PO0727)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RETAHSEQ+RETALSEQ+RETASSEQ; DAYENDSEQ+RETAHSEQ+RETALSEQ+CURRENCY+RETASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RETAHSEQ BCD*10.0 Processing Sequence
  RETALSEQ BCD*10.0 Line Number
  RETASSEQ BCD*10.0 Cost Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  GLITEM String*45 G/L Item
  GLEXPENSE String*45 Return Account
  GLCLEARING String*45 Receipt Clearing Account
  POSTCLEARI Boolean Post to clearing account? [0=No,1=Yes]
  CURRENCY String*3 Currency
  SCURNDECML Integer Decimal Places
  FCITEM BCD*10.3 Func. Item Amount
  SCITEM BCD*10.3 Item amount
  FCEXPENSE BCD*10.3 Func. Expensed Amount
  SCEXPENSE BCD*10.3 Expensed amount
  FCBASEALLO BCD*10.3 Func. Base to Allocate
  SCBASEALLO BCD*10.3 Base to Allocate
  FCTAXALLO BCD*10.3 Func. Total Tax Allocated
  SCTAXALLO BCD*10.3 Total Tax Allocated
  FCTAXRECV BCD*10.3 Func. Total Tax Recoverable
  SCTAXRECV BCD*10.3 Total Tax Recoverable
  FCTAXEXPS BCD*10.3 Func. Total Tax Expensed
  SCTAXEXPS BCD*10.3 Total Tax Expensed
  FCTAXINCL BCD*10.3 Func. Tax Included in Price
  SCTAXINCL BCD*10.3 Tax Included in Price
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  FCTAXAMT1 BCD*10.3 Func. Tax Amount 1
  FCTAXAMT2 BCD*10.3 Func. Tax Amount 2
  FCTAXAMT3 BCD*10.3 Func. Tax Amount 3
  FCTAXAMT4 BCD*10.3 Func. Tax Amount 4
  FCTAXAMT5 BCD*10.3 Func. Tax Amount 5
  BILLRATE BCD*10.6 Billing Rate
  BCBILLRATE BCD*10.6 (BC) Billing Rate
  GLOVERHEAD String*45 Overhead Account
  GLLABOR String*45 Labor Burden Account
  FCOVRHDAMT BCD*10.3 Func. Overhead Amount
  SCOVRHDAMT BCD*10.3 Overhead Amount
  FCLABORAMT BCD*10.3 Func. Labor Burden Amount
  SCLABORAMT BCD*10.3 Labor Burden Amount
  BCRATE BCD*8.7 Billing Currency Conversion Rate
  BCRATEDATE Date Billing Currency Conv. Rate Date
  BCRATETYPE String*2 Billing Currency Conv. Rate Type
  BCRATEOPER Integer Billing Curr. Cv. Rate Operation [1=Multiply,2=Divide]
  BCRATEXIST Boolean Billing Curr. Conv. Rate Exists [0=No,1=Yes]
  PMTRANSNUM Long PJC Transaction Number
  RCTAXALLO BCD*10.3 Rptg. Total Tax Allocated
  RCTAXRECV BCD*10.3 Rptg. Total Tax Recoverable
  RCTAXEXPS BCD*10.3 Rptg. Total Tax Expensed
  RCTAXINCL BCD*10.3 Rptg. Total Tax Included
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  SCRAXALLO BCD*10.3 Total Rtg. Tax Allocated
  FCRAXALLO BCD*10.3 Func. Total Rtg. Tax Allocated
  SCRAXEXPS BCD*10.3 Total Rtg. Tax Expensed
  FCRAXEXPS BCD*10.3 Func. Total Rtg. Tax Expensed

## PORETAS - Return Audit Costs (view PO0728)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDSEQ+RETAHSEQ+RETASSEQ
Fields (NAME type description [values]):
  DAYENDSEQ BCD*10.0 Day End Number
  RETAHSEQ BCD*10.0 Processing Sequence
  RETASSEQ BCD*10.0 Cost Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANSTYPE Integer Transaction Type
  PONUMBER String*22 Purchase Order Number
  RCPNUMBER String*22 Receipt Number
  INVNUMBER String*22 Invoice Number
  CRNNUMBER String*22 Credit/Debit Note Number
  ADDCOST String*6 Additional Cost
  DESCRIPTIO String*60 Description
  PRORMETHOD Integer Proration Method [1=No Proration,2=Prorate by Quantity,3=Prorate by Cost,4=Prorate by Weight,5=Prorate Manually]
  REPRORATE Integer Reproration Method [1=Leave,2=Prorate,3=Expense]
  VENDOR String*12 Vendor
  VENDORNAME String*60 Name
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  CURRENCY String*3 Currency
  EXRATE BCD*8.7 Exchange Rate
  RATEDATE Date Rate Date
  RATETYPE String*2 Rate Type
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  TAXVCLASS1 Integer Vendor Tax Class 1
  TAXVCLASS2 Integer Vendor Tax Class 2
  TAXVCLASS3 Integer Vendor Tax Class 3
  TAXVCLASS4 Integer Vendor Tax Class 4
  TAXVCLASS5 Integer Vendor Tax Class 5
  TAXICLASS1 Integer Cost Tax Class 1
  TAXICLASS2 Integer Cost Tax Class 2
  TAXICLASS3 Integer Cost Tax Class 3
  TAXICLASS4 Integer Cost Tax Class 4
  TAXICLASS5 Integer Cost Tax Class 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  NOPRORTOGL Boolean Exp. Add'l Cost G/L data posted? [0=No,1=Yes]
  COMMENT String*250 Comment
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  RESOURCE String*24 Resource
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  CALCOVRHD Boolean Calculate Overhead [0=No,1=Yes]
  CALCLABOR Boolean Calculate Labor [0=No,1=Yes]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  PMTRANSNUM Long PJC Transaction Number
  TRCURRENCY String*3 Tax Reporting Currency
  EXRATERC BCD*8.7 Tax Reporting Exchange Rate
  RATEDATERC Date Tax Reporting Rate Date
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places

## PORETC - Return Comments (view PO0729)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ+RETCREV; RETHSEQ+RETCSEQ [D]
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  RETCREV BCD*10.0 Comment Identifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RETCSEQ BCD*10.0 Return Comment Sequence
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  COMMENTTYP Integer Line Type [1=Comment,2=Instruction]
  COMMENT String*80 Comment

## PORETH1 - Returns (view PO0731)
Physical tables of this view: PORETH1, PORETH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ; RETNUMBER; VDCODE+RETHSEQ [M]; RCPHSEQ [D]; VDCODE+RETNUMBER [M]
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTLSEQ BCD*10.0 Next Line Sequence
  LINES Long Lines
  LINESCMPL Long Lines Complete
  TAXLINES Long Lines Tax Calculation Sees
  EXTRANEOUS Long Extraneous Line Count
  TAXAUTOCAL Boolean Auto. tax calculation on save [0=No,1=Yes]
  ISPRINTED Boolean Printed [0=No,1=Yes]
  ISCREDITED Boolean Is Credited [0=No,1=Yes]
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  POSTDATE Date Last Posting Date
  LABELPRINT Boolean Labels Printed [0=No,1=Yes]
  LABELCOUNT Integer Number of Labels
  DATE Date Return Date
  FISCYEAR String*4 Fiscal Year
  FISCPERIOD Integer Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  RETNUMBER String*22 Return Number
  TEMPLATE String*6 Template Code
  VDCODE String*12 Vendor
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDNAME String*60 Name
  VDADDRESS1 String*60 Address 1
  VDADDRESS2 String*60 Address 2
  VDADDRESS3 String*60 Address 3
  VDADDRESS4 String*60 Address 4
  VDCITY String*30 City
  VDSTATE String*30 State/Province
  VDZIP String*20 Zip/Postal Code
  VDCOUNTRY String*30 Country
  VDPHONE String*30 Phone Number
  VDFAX String*30 Fax Number
  VDCONTACT String*60 Contact
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPNUMBER String*22 Receipt Number
  RCPDATE Date Receipt Date
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PONUMBER String*22 Purchase Order Number
  PORDATE Date Purchase Order Date
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  VIACODE String*6 Ship-Via
  VIANAME String*60 Ship-Via Name
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  SPREAD BCD*8.7 Rate Spread
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  EXTWEIGHT BCD*10.4 Extended Weight
  EXTENDED BCD*10.3 Return Cost
  DOCTOTAL BCD*10.3 Total
  AMOUNT BCD*10.3 Amount
  RQRETURNED BCD*10.4 Quantity Returned
  TAXGROUP String*12 Tax Group
  TAXAUTH1 String*12 Tax Authority 1
  TAXAUTH2 String*12 Tax Authority 2
  TAXAUTH3 String*12 Tax Authority 3
  TAXAUTH4 String*12 Tax Authority 4
  TAXAUTH5 String*12 Tax Authority 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXEXCLUDE1 BCD*10.3 Excluded Tax Amount 1
  TXEXCLUDE2 BCD*10.3 Excluded Tax Amount 2
  TXEXCLUDE3 BCD*10.3 Excluded Tax Amount 3
  TXEXCLUDE4 BCD*10.3 Excluded Tax Amount 4
  TXEXCLUDE5 BCD*10.3 Excluded Tax Amount 5
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Total Tax Recoverable
  TXEXPSAMT BCD*10.3 Total Tax Expensed
  TXALLOAMT BCD*10.3 Total Tax Allocated
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  VDEMAIL String*50 E-mail
  VDPHONEC String*30 Contact Phone
  VDFAXC String*30 Contact Fax
  VDEMAILC String*50 Contact E-mail
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  VALUES Long Optional Fields
  VERPRORATE Integer Proration Version [1=3.0A,2=5.3B]
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGBASE Integer Retainage Base [0=Total After Taxes,1=Total Before Taxes]
  RTGAMOUNT BCD*10.3 Retainage Amount
  JOBLINES Long Job Related Lines
  TRCURRENCY String*3 Tax Reporting Currency
  RATERC BCD*8.7 Tax Reporting Exchange Rate
  SPREADRC BCD*8.7 Tax Reporting Rate Spread
  RATETYPERC String*2 Tax Reporting Rate Type
  RATEMTCHRC Integer Tax Reporting Rate Match Type
  RATEDATERC Date Tax Reporting Rate Date
  RATEOPERRC Integer Tax Reporting Rate Operation [1=Multiply,2=Divide]
  RATERCOVER Boolean Tax Reporting Rate Overridden [0=No,1=Yes]
  RCURNDECML Integer Tax Reporting Decimal Places
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TREXCLUDE1 BCD*10.3 Tax Reporting Excluded Amount 1
  TREXCLUDE2 BCD*10.3 Tax Reporting Excluded Amount 2
  TREXCLUDE3 BCD*10.3 Tax Reporting Excluded Amount 3
  TREXCLUDE4 BCD*10.3 Tax Reporting Excluded Amount 4
  TREXCLUDE5 BCD*10.3 Tax Reporting Excluded Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RTGTAXREP Integer Report Retainage Tax [0=At Time of Original Document,1=As Per Tax Authority]
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5

## PORETH2 - Returns (view PO0731)
Physical tables of this view: PORETH1, PORETH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BTCODE String*6 Bill-To Location
  BTDESC String*60 Bill-To Location Description
  BTADDRESS1 String*60 Bill-To Address 1
  BTADDRESS2 String*60 Bill-To Address 2
  BTADDRESS3 String*60 Bill-To Address 3
  BTADDRESS4 String*60 Bill-To Address 4
  BTCITY String*30 Bill-To City
  BTSTATE String*30 Bill-To State/Province
  BTZIP String*20 Bill-To Zip/Postal Code
  BTCOUNTRY String*30 Bill-To Country
  BTPHONE String*30 Bill-To Phone Number
  BTFAX String*30 Bill-To Fax Number
  BTCONTACT String*60 Bill-To Contact
  STCODE String*6 Ship-To Location
  STDESC String*60 Ship-To Location Description
  STADDRESS1 String*60 Ship-To Address 1
  STADDRESS2 String*60 Ship-To Address 2
  STADDRESS3 String*60 Ship-To Address 3
  STADDRESS4 String*60 Ship-To Address 4
  STCITY String*30 Ship-To City
  STSTATE String*30 Ship-To State/Province
  STZIP String*20 Ship-To Zip/Postal Code
  STCOUNTRY String*30 Ship-To Country
  STPHONE String*30 Ship-To Phone Number
  STFAX String*30 Ship-To Fax Number
  STCONTACT String*60 Ship-To Contact
  PDRATE BCD*8.7 Predecessor's Exchange Rate
  PDRATETYPE String*2 Predecessor's Rate Type
  PDRATEDATE Date Predecessor's Rate Date
  PDRATEOPER Integer Predecessor's Rate Operation [1=Multiply,2=Divide]
  PDRATEOVER Boolean Predecessor's Rate Overridden [0=No,1=Yes]
  BTEMAIL String*50 Bill-To E-mail
  BTPHONEC String*30 Bill-To Contact Phone
  BTFAXC String*30 Bill-To Contact Fax
  BTEMAILC String*50 Bill-To Contact E-mail
  STEMAIL String*50 Ship-To E-mail
  STPHONEC String*30 Ship-To Contact Phone
  STFAXC String*30 Ship-To Contact Fax
  STEMAILC String*50 Ship-To Contact E-mail
  PDRATERC BCD*8.7 Pred. Tax Reporting Exch. Rate
  PDRATTYPRC String*2 Pred. Tax Reporting Rate Type
  PDRATEDTRC Date Pred. Tax Reporting Rate Date
  PDRATEOPRC Integer Pred. Tax Reporting Rate Oper. [1=Multiply,2=Divide]
  PDRATERCOV Boolean Pred. Tax Reporting Rate Overrd. [0=No,1=Yes]
  VDACCTSET String*6 Vendor Account Set
  DATEBUS Date Posting Date
  ENTEREDBY String*8 Entered By
  DETAILNEXT Integer Next Detail Number

## PORETHO - Return Optional Fields (view PO0738)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ+OPTFIELD; OPTFIELD+RETHSEQ
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
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

## PORETI - Return Postings (view PO0732)
Keys (first = PK; D=dups allowed, M=modifiable): RETISEQ; RETHSEQ [D]
Fields (NAME type description [values]):
  RETISEQ BCD*10.0 Header Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  POSTDATE Date Last Posting Date
  ISPRINTED Boolean Printed [0=No,1=Yes]
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  RETHSEQ BCD*10.0 Return Sequence Key
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGRATE Integer Retainage Exchange Rate
  SCRTGAMT BCD*10.3 Retainage Amount

## PORETJ - Return Day-ends (view PO0733)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRORATESEQ BCD*10.0 Prorate Model Sequence
  POSTDATE Date Last Posting Date
  SCAMOUNT BCD*10.3 Conversion Source Amount
  FCAMOUNT BCD*10.3 Conversion Functional Amount
  SCDOCTOTAL BCD*10.3 Source Document Total
  ISCOMPLETE Boolean Completed
  DTCOMPLETE Date Date Completed
  SCRTGAMT BCD*10.3 Retainage Amount

## PORETL - Return Lines (view PO0735)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ+RETLREV; RETHSEQ+RETLSEQ; RCPHSEQ [D,M]; RETHSEQ+DETAILNUM+RETLSEQ [M]
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RETLSEQ BCD*10.0 Return Line Sequence
  RETCSEQ BCD*10.0 Return Comment Sequence
  OEONUMBER String*22 Order Number
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  POSTEDTOIC Boolean Posted to I/C [0=No,1=Yes]
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  VENDITEMNO String*24 Vendor Item Number
  HASCOMMENT Boolean Comments [0=No,1=Yes]
  RETUNIT String*10 Unit of Measure
  RETCONV BCD*10.6 Returning Conversion Factor
  RETDECML Integer Returning Unit Decimals
  STOCKDECML Integer Stock Unit Decimals
  RQRECEIVED BCD*10.4 Quantity Received
  SQRECEIVED BCD*10.4 Stocking Quantity Received
  SCRECEIVED BCD*10.3 Extended Cost
  RQPREVRETN BCD*10.4 Quantity Previously Returned
  RQRETURNED BCD*10.4 Quantity Returned
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Return Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXINCLUD1 Boolean Tax Includable 1 [0=No,1=Yes]
  TAXINCLUD2 Boolean Tax Includable 2 [0=No,1=Yes]
  TAXINCLUD3 Boolean Tax Includable 3 [0=No,1=Yes]
  TAXINCLUD4 Boolean Tax Includable 4 [0=No,1=Yes]
  TAXINCLUD5 Boolean Tax Includable 5 [0=No,1=Yes]
  TAXAMOUNT1 BCD*10.3 Tax Amount 1
  TAXAMOUNT2 BCD*10.3 Tax Amount 2
  TAXAMOUNT3 BCD*10.3 Tax Amount 3
  TAXAMOUNT4 BCD*10.3 Tax Amount 4
  TAXAMOUNT5 BCD*10.3 Tax Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDED BCD*10.3 Tax Included
  TXEXCLUDED BCD*10.3 Tax Excluded
  TAXAMOUNT BCD*10.3 Total Tax
  TXRECVAMT BCD*10.3 Recoverable Tax
  TXEXPSAMT BCD*10.3 Expensed Tax
  TXALLOAMT BCD*10.3 Allocated Tax
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  GLACEXPENS String*45 Expense Account
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  PORHSEQ BCD*10.0 Purchase Order Sequence Key
  PORLSEQ BCD*10.0 Purchase Order Line Sequence
  PONUMBER String*22 Purchase Order Number
  GLNONSTKCR String*45 Non-Stock Clearing Account
  MANITEMNO String*24 Manufacturer's Item Number
  SCDISCRCVD BCD*10.3 Discount Received
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  VALUES Long Optional Fields
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  BILLRATE BCD*10.6 Billing Rate
  BILLCURR String*3 Billing Currency
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Unit of Measure
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden [0=No,1=Yes]
  TARAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TARAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TARAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TARAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TARAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RAXAMOUNT1 BCD*10.3 Retainage Tax Amount 1
  RAXAMOUNT2 BCD*10.3 Retainage Tax Amount 2
  RAXAMOUNT3 BCD*10.3 Retainage Tax Amount 3
  RAXAMOUNT4 BCD*10.3 Retainage Tax Amount 4
  RAXAMOUNT5 BCD*10.3 Retainage Tax Amount 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  UCISMANUAL Boolean Unit Cost is Manual [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]
  DETAILNUM Integer Detail Number

## PORETLL - Return Line Lots (view PO0799)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ+RETLREV+LOTNUMF; LOTNUMF+RETHSEQ+RETLREV
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLREV BCD*10.0 Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RETLSEQ BCD*10.0 Return Line Sequence
  EXPIRYDATE Date Expiry Date
  QTY BCD*10.4 Lot Quantity
  QTYSQ BCD*10.4 Lot Stock Quantity
  QTYMOVED BCD*10.4 Returned
  QTYMOVEDSQ BCD*10.4 Returned Stock

## PORETLO - Return Detail Optional Fields (view PO0739)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ+RETLREV+OPTFIELD; OPTFIELD+RETHSEQ+RETLREV
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLREV BCD*10.0 Line Number
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

## PORETLS - Return Line Serials (view PO0790)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ+RETLREV+SERIALNUMF; SERIALNUMF+RETHSEQ+RETLREV
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLREV BCD*10.0 Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RETLSEQ BCD*10.0 Return Line Sequence
  MOVED Boolean Returned

## PORETM - Return Posting Lines (view PO0736)
Keys (first = PK; D=dups allowed, M=modifiable): RETISEQ+RETHSEQ+RETLSEQ
Fields (NAME type description [values]):
  RETISEQ BCD*10.0 Header Sequence
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLSEQ BCD*10.0 Return Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post
  RCPHSEQ BCD*10.0 Receipt Sequence Key
  RCPLSEQ BCD*10.0 Receipt Line Sequence
  ITEMDESC String*60 Item Description
  STOCKUNIT String*10 Unit of Measure
  RETUNIT String*10 Unit of Measure
  RETCONV BCD*10.6 Returning Conversion Factor
  RETDECML Integer Returning Unit Decimals
  RQRETURNED BCD*10.4 Quantity Returned
  RQUSTOCKED BCD*10.4 Receiving Unstocked
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  SQUSTOCKED BCD*10.4 Stocking Unstocked
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Extended Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.3 Extended Weight
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXCLASS1 Integer Tax Class 1
  TAXCLASS2 Integer Tax Class 2
  TAXCLASS3 Integer Tax Class 3
  TAXCLASS4 Integer Tax Class 4
  TAXCLASS5 Integer Tax Class 5
  TAXRATE1 BCD*8.5 Tax Rate 1
  TAXRATE2 BCD*8.5 Tax Rate 2
  TAXRATE3 BCD*8.5 Tax Rate 3
  TAXRATE4 BCD*8.5 Tax Rate 4
  TAXRATE5 BCD*8.5 Tax Rate 5
  TAXINCLUD1 Boolean Tax Includable 1
  TAXINCLUD2 Boolean Tax Includable 2
  TAXINCLUD3 Boolean Tax Includable 3
  TAXINCLUD4 Boolean Tax Includable 4
  TAXINCLUD5 Boolean Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  QTYPOSTED Boolean Is Quantity Posted?

## PORETML - Return Posting Lines Lots (view PO0798)
Keys (first = PK; D=dups allowed, M=modifiable): RETISEQ+RETHSEQ+RETLSEQ+LOTNUMF; LOTNUMF+RETISEQ+RETHSEQ+RETLSEQ
Fields (NAME type description [values]):
  RETISEQ BCD*10.0 Header Sequence
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLSEQ BCD*10.0 Return Line Sequence
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RQPREV BCD*10.4 Old Quantity
  RQCURR BCD*10.4 Current Quantity
  SQPREV BCD*10.4 Old Stock Quantity
  SQCURR BCD*10.4 Current Stock Quantity
  OPERATION Integer Operation To Post

## PORETMS - Return Posting Lines Serials (view PO0791)
Keys (first = PK; D=dups allowed, M=modifiable): RETISEQ+RETHSEQ+RETLSEQ+SERIALNUMF; SERIALNUMF+RETISEQ+RETHSEQ+RETLSEQ
Fields (NAME type description [values]):
  RETISEQ BCD*10.0 Header Sequence
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLSEQ BCD*10.0 Return Line Sequence
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation To Post

## PORETN - Return Day-end Lines (view PO0734)
Keys (first = PK; D=dups allowed, M=modifiable): RETHSEQ+RETLSEQ
Fields (NAME type description [values]):
  RETHSEQ BCD*10.0 Return Sequence Key
  RETLSEQ BCD*10.0 Return Line Sequence
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60 Item Description
  STOCKUNIT String*10 Unit of Measure
  RETUNIT String*10 Unit of Measure
  RETCONV BCD*10.6 Returning Conversion Factor
  RETDECML Integer Returning Unit Decimals
  RQRETURNED BCD*10.4 Quantity Returned
  SQRETURNED BCD*10.4 Stocking Quantity Returned
  RQUSTOCKED BCD*10.4 Receiving Unstocked
  SQUSTOCKED BCD*10.4 Stocking Unstocked
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  UNITCOST BCD*10.6 Unit Cost
  EXTENDED BCD*10.3 Return Cost
  PRUNITCOST BCD*10.6 Unit Cost
  TAXBASE1 BCD*10.3 Tax Base 1
  TAXBASE2 BCD*10.3 Tax Base 2
  TAXBASE3 BCD*10.3 Tax Base 3
  TAXBASE4 BCD*10.3 Tax Base 4
  TAXBASE5 BCD*10.3 Tax Base 5
  TAXINCLUD1 Integer Tax Includable 1
  TAXINCLUD2 Integer Tax Includable 2
  TAXINCLUD3 Integer Tax Includable 3
  TAXINCLUD4 Integer Tax Includable 4
  TAXINCLUD5 Integer Tax Includable 5
  TXBASEALLO BCD*10.3 Net of Tax
  TXINCLUDE1 BCD*10.3 Included Tax Amount 1
  TXINCLUDE2 BCD*10.3 Included Tax Amount 2
  TXINCLUDE3 BCD*10.3 Included Tax Amount 3
  TXINCLUDE4 BCD*10.3 Included Tax Amount 4
  TXINCLUDE5 BCD*10.3 Included Tax Amount 5
  TXRECVAMT1 BCD*10.3 Tax Recoverable Amount 1
  TXRECVAMT2 BCD*10.3 Tax Recoverable Amount 2
  TXRECVAMT3 BCD*10.3 Tax Recoverable Amount 3
  TXRECVAMT4 BCD*10.3 Tax Recoverable Amount 4
  TXRECVAMT5 BCD*10.3 Tax Recoverable Amount 5
  TXEXPSAMT1 BCD*10.3 Tax Expense Amount 1
  TXEXPSAMT2 BCD*10.3 Tax Expense Amount 2
  TXEXPSAMT3 BCD*10.3 Tax Expense Amount 3
  TXEXPSAMT4 BCD*10.3 Tax Expense Amount 4
  TXEXPSAMT5 BCD*10.3 Tax Expense Amount 5
  TXALLOAMT1 BCD*10.3 Tax Allocated Amount 1
  TXALLOAMT2 BCD*10.3 Tax Allocated Amount 2
  TXALLOAMT3 BCD*10.3 Tax Allocated Amount 3
  TXALLOAMT4 BCD*10.3 Tax Allocated Amount 4
  TXALLOAMT5 BCD*10.3 Tax Allocated Amount 5
  TFBASEALLO BCD*10.3 Func. Net of Tax
  TFINCLUDE1 BCD*10.3 Func. Tax Included Amount 1
  TFINCLUDE2 BCD*10.3 Func. Tax Included Amount 2
  TFINCLUDE3 BCD*10.3 Func. Tax Included Amount 3
  TFINCLUDE4 BCD*10.3 Func. Tax Included Amount 4
  TFINCLUDE5 BCD*10.3 Func. Tax Included Amount 5
  TFALLOAMT1 BCD*10.3 Func. Tax Allocated Amount 1
  TFALLOAMT2 BCD*10.3 Func. Tax Allocated Amount 2
  TFALLOAMT3 BCD*10.3 Func. Tax Allocated Amount 3
  TFALLOAMT4 BCD*10.3 Func. Tax Allocated Amount 4
  TFALLOAMT5 BCD*10.3 Func. Tax Allocated Amount 5
  TFRECVAMT1 BCD*10.3 Func. Tax Recoverable Amount 1
  TFRECVAMT2 BCD*10.3 Func. Tax Recoverable Amount 2
  TFRECVAMT3 BCD*10.3 Func. Tax Recoverable Amount 3
  TFRECVAMT4 BCD*10.3 Func. Tax Recoverable Amount 4
  TFRECVAMT5 BCD*10.3 Func. Tax Recoverable Amount 5
  TFEXPSAMT1 BCD*10.3 Func. Tax Expense Amount 1
  TFEXPSAMT2 BCD*10.3 Func. Tax Expense Amount 2
  TFEXPSAMT3 BCD*10.3 Func. Tax Expense Amount 3
  TFEXPSAMT4 BCD*10.3 Func. Tax Expense Amount 4
  TFEXPSAMT5 BCD*10.3 Func. Tax Expense Amount 5
  DISCPCT BCD*5.5 Discount Percentage
  DISCOUNT BCD*10.3 Discount Amount
  DISCOUNTF BCD*10.3 Func. Discount Amount
  BILLRATE BCD*10.6 Billing Rate
  RTGPERCENT BCD*5.5 Retainage Percentage
  RTGDAYS Integer Retention Period
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGAMTOVER Boolean Retainage Amount Overridden
  TRINCLUDE1 BCD*10.3 Tax Reporting Included Amount 1
  TRINCLUDE2 BCD*10.3 Tax Reporting Included Amount 2
  TRINCLUDE3 BCD*10.3 Tax Reporting Included Amount 3
  TRINCLUDE4 BCD*10.3 Tax Reporting Included Amount 4
  TRINCLUDE5 BCD*10.3 Tax Reporting Included Amount 5
  TRRECVAMT1 BCD*10.3 Tax Reporting Recoverable Amt. 1
  TRRECVAMT2 BCD*10.3 Tax Reporting Recoverable Amt. 2
  TRRECVAMT3 BCD*10.3 Tax Reporting Recoverable Amt. 3
  TRRECVAMT4 BCD*10.3 Tax Reporting Recoverable Amt. 4
  TRRECVAMT5 BCD*10.3 Tax Reporting Recoverable Amt. 5
  TREXPSAMT1 BCD*10.3 Tax Reporting Expense Amount 1
  TREXPSAMT2 BCD*10.3 Tax Reporting Expense Amount 2
  TREXPSAMT3 BCD*10.3 Tax Reporting Expense Amount 3
  TREXPSAMT4 BCD*10.3 Tax Reporting Expense Amount 4
  TREXPSAMT5 BCD*10.3 Tax Reporting Expense Amount 5
  TRALLOAMT1 BCD*10.3 Tax Reporting Allocated Amount 1
  TRALLOAMT2 BCD*10.3 Tax Reporting Allocated Amount 2
  TRALLOAMT3 BCD*10.3 Tax Reporting Allocated Amount 3
  TRALLOAMT4 BCD*10.3 Tax Reporting Allocated Amount 4
  TRALLOAMT5 BCD*10.3 Tax Reporting Allocated Amount 5
  RAXBASE1 BCD*10.3 Retainage Tax Base 1
  RAXBASE2 BCD*10.3 Retainage Tax Base 2
  RAXBASE3 BCD*10.3 Retainage Tax Base 3
  RAXBASE4 BCD*10.3 Retainage Tax Base 4
  RAXBASE5 BCD*10.3 Retainage Tax Base 5
  RXRECVAMT1 BCD*10.3 Retainage Tax Recoverable Amt. 1
  RXRECVAMT2 BCD*10.3 Retainage Tax Recoverable Amt. 2
  RXRECVAMT3 BCD*10.3 Retainage Tax Recoverable Amt. 3
  RXRECVAMT4 BCD*10.3 Retainage Tax Recoverable Amt. 4
  RXRECVAMT5 BCD*10.3 Retainage Tax Recoverable Amt. 5
  RXEXPSAMT1 BCD*10.3 Retainage Tax Expense Amount 1
  RXEXPSAMT2 BCD*10.3 Retainage Tax Expense Amount 2
  RXEXPSAMT3 BCD*10.3 Retainage Tax Expense Amount 3
  RXEXPSAMT4 BCD*10.3 Retainage Tax Expense Amount 4
  RXEXPSAMT5 BCD*10.3 Retainage Tax Expense Amount 5
  RXALLOAMT1 BCD*10.3 Retainage Tax Allocated Amount 1
  RXALLOAMT2 BCD*10.3 Retainage Tax Allocated Amount 2
  RXALLOAMT3 BCD*10.3 Retainage Tax Allocated Amount 3
  RXALLOAMT4 BCD*10.3 Retainage Tax Allocated Amount 4
  RXALLOAMT5 BCD*10.3 Retainage Tax Allocated Amount 5
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight

## PORQNC - Requisition Comments (view PO0750)
Keys (first = PK; D=dups allowed, M=modifiable): RQNHSEQ+RQNCREV; RQNHSEQ+RQNCSEQ [D]
Fields (NAME type description [values]):
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  RQNCREV BCD*10.0 Comment Identifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RQNCSEQ BCD*10.0 Requisition Comment Sequence
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  COMMENTTYP Integer Line Type [1=Comment,2=Instruction]
  COMMENT String*80 Comments/Instructions

## PORQNH1 - Requisitions (view PO0760)
Physical tables of this view: PORQNH1, PORQNH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): RQNHSEQ; RQNNUMBER; VDCODE+RQNHSEQ [M]; REQUESTBY+RQNNUMBER [M]; VDCODE+RQNNUMBER [M]
Fields (NAME type description [values]):
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEXTLSEQ BCD*10.0 Next Line Sequence
  LINES Long Lines
  LINESCMPL Long Lines Complete
  LINESORDER Long Lines Ordered
  ISPRINTED Boolean Printed [0=No,1=Yes]
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed
  POSTDATE Date Last Posting Date
  DATE Date Requisition Date
  RQNNUMBER String*22 Requisition Number
  VDCODE String*12 Vendor
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDNAME String*60 Name
  ONHOLD Boolean On Hold [0=No,1=Yes]
  ORDEREDON Date Order Date
  EXPARRIVAL Date Date Required
  EXPIRATION Date Expiration Date
  DESCRIPTIO String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  OQORDERED BCD*10.4 Quantity Ordered
  REQUESTBY String*60 Requested by
  DOCSOURCE Integer Document Source [0=Entered,1=Internet]
  VALUES Long Optional Fields
  JOBLINES Long Job Related Lines

## PORQNH2 - Requisitions (view PO0760)
Physical tables of this view: PORQNH1, PORQNH2 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): RQNHSEQ
Fields (NAME type description [values]):
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STCODE String*6 Location
  STDESC String*60 Location Description
  APPROVED Integer Approval Status [11=Entered,12=Approved]
  APPROVER String*8 Approver ID
  ENTEREDBY String*8 Entered By
  EXTWEIGHT BCD*10.4 Extended Weight
  FCEXTENDED BCD*10.3 Func. Extended Amount
  DETAILNEXT Integer Next Detail Number

## PORQNHO - Requisition Header Opt. Fields (view PO0763)
Keys (first = PK; D=dups allowed, M=modifiable): RQNHSEQ+OPTFIELD; OPTFIELD+RQNHSEQ
Fields (NAME type description [values]):
  RQNHSEQ BCD*10.0 Requisition Sequence Key
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

## PORQNL - Requisition Lines (view PO0770)
Keys (first = PK; D=dups allowed, M=modifiable): RQNHSEQ+RQNLREV; RQNHSEQ+RQNLSEQ; RQNHSEQ+VDCODE+RQNLSEQ [M]; VDCODE+RQNHSEQ+RQNLSEQ [M]; RQNHSEQ+DETAILNUM+RQNLSEQ [M]
Fields (NAME type description [values]):
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  RQNLREV BCD*10.0 Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RQNLSEQ BCD*10.0 Requisition Line Sequence
  LINEORDER Long Line Ordered
  RQNCSEQ BCD*10.0 Requisition Comment Sequence
  OEONUMBER String*22 Order Number
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  VDCODE String*12 Vendor
  VDNAME String*60 Name
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  COMPLETION Integer Completion Status [1=No,2=Yes,3=Yes]
  DTCOMPLETE Date Date Completed
  ITEMEXISTS Boolean Item Exists [0=No,1=Yes]
  ITEMNO String*24 Item Number
  LOCATION String*6 Location
  ITEMDESC String*60 Item Description
  EXPARRIVAL Date Expected Arrival Date
  VENDITEMNO String*24 Vendor Item Number
  HASCOMMENT Boolean Comments/Instructions [0=No,1=Yes]
  ORDERUNIT String*10 Unit of Measure
  ORDERCONV BCD*10.6 Order Unit Conversion
  ORDERDECML Integer Order Unit Decimals
  STOCKDECML Integer Stock Unit Decimals
  OQORDERED BCD*10.4 Quantity Ordered
  HASDROPSHI Boolean Drop-Ship [0=No,1=Yes]
  DROPTYPE Integer Drop-Ship Type [2=Address Entered,3=Inventory Location Address,4=Customer Address,5=Customer Ship-To Address]
  IDCUST String*12 Drop-Ship Customer
  IDCUSTSHPT String*6 Customer Ship-To Address
  DLOCATION String*6 Drop-Ship Location
  DESC String*60 Drop-Ship Description
  ADDRESS1 String*60 Drop-Ship Address 1
  ADDRESS2 String*60 Drop-Ship Address 2
  ADDRESS3 String*60 Drop-Ship Address 3
  ADDRESS4 String*60 Drop-Ship Address 4
  CITY String*30 Drop-Ship City
  STATE String*30 Drop-Ship State/Province
  ZIP String*20 Drop-Ship Zip/Postal Code
  COUNTRY String*30 Drop-Ship Country
  PHONE String*30 Drop-Ship Phone Number
  FAX String*30 Drop-Ship Fax Number
  CONTACT String*60 Drop-Ship Contact
  STOCKITEM Boolean Stock Item [0=No,1=Yes]
  EMAIL String*50 Drop-Ship E-mail
  PHONEC String*30 Drop-Ship Contact Phone
  FAXC String*30 Drop-Ship Contact Fax
  EMAILC String*50 Drop-Ship Contact E-mail
  MANITEMNO String*24 Manufacturer's Item Number
  VALUES Long Optional Fields
  CONTRACT String*16 Contract
  PROJECT String*16 Project
  CCATEGORY String*16 (Cost) Category
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  UNITCOST BCD*10.6 Unit Cost
  CPCOSTTOPO Boolean Copy Cost To Purchase Order [0=No,1=Yes]
  UCISMANUAL Boolean Unit Cost is Manual [0=No,1=Yes]
  EXTENDED BCD*10.3 Extended Cost
  FCEXTENDED BCD*10.3 Functional Extended
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion
  DEFUWEIGHT BCD*10.4 Default Unit Weight
  DEFEXTWGHT BCD*10.4 Default Extended Weight
  DETAILNUM Integer Detail Number

## PORQNLO - Requisition Detail Opt. Fields (view PO0773)
Keys (first = PK; D=dups allowed, M=modifiable): RQNHSEQ+RQNLREV+OPTFIELD; OPTFIELD+RQNHSEQ+RQNLREV
Fields (NAME type description [values]):
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  RQNLREV BCD*10.0 Line Number
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

## PORQNLV - Requisition Vendors (view PO0777)
Keys (first = PK; D=dups allowed, M=modifiable): RQNHSEQ+VDCODE
Fields (NAME type description [values]):
  RQNHSEQ BCD*10.0 Requisition Sequence Key
  VDCODE String*12 Vendor
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LINES Long Lines
  LINESCMPL Long Lines Complete
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  VDEXISTS Boolean Vendor Exists [0=No,1=Yes]
  CURRENCY String*3 Currency
  RATE BCD*8.7 Exchange Rate
  SPREAD BCD*8.7 Rate Spread
  RATETYPE String*2 Rate Type
  RATEMATCH Integer Rate Match Type
  RATEDATE Date Rate Date
  RATEOPER Integer Rate Operation [1=Multiply,2=Divide]
  RATEOVER Boolean Rate Overridden [0=No,1=Yes]
  SCURNDECML Integer Decimal Places
  EXTENDED BCD*10.3 Extended Cost
  FCEXTENDED BCD*10.3 Func. Extended Amount
  ISCOMPLETE Boolean Completed [0=No,1=Yes]
  DTCOMPLETE Date Date Completed

## PORSTRT - Restart (view PO0785)
Keys (first = PK; D=dups allowed, M=modifiable): KEY+USERID
Fields (NAME type description [values]):
  KEY String*50 Key
  USERID String*8 User ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Data Block 1

## POSERZ - Serial Prorate Data (view PO0526)
Keys (first = PK; D=dups allowed, M=modifiable): PRORSEQ+LINESEQ+SERIALNUMF
Fields (NAME type description [values]):
  PRORSEQ BCD*10.0 Prorate Sequence
  LINESEQ BCD*10.0 Line Sequence
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RECEIVED Boolean Received
  RETURNED Boolean Returned

## POSTTL - Statistics (view PO0800)
Keys (first = PK; D=dups allowed, M=modifiable): FISCYEAR+PERIOD+CURRENCY
Fields (NAME type description [values]):
  FISCYEAR String*4 Fiscal Year
  PERIOD Integer Fiscal Period
  CURRENCY String*3 Currency
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  POCOUNT Long Number of Purchase Orders
  RECPCOUNT Long Number of Receipts
  QTYPURCH BCD*10.4 Net Quantity Purchased
  PURCHAMTF BCD*10.3 Func. Net Purchase Amount
  PURCHAMTS BCD*10.3 Srce. Net Purchase Amount
  INVAMTF BCD*10.3 Func. Invoice Amount
  INVAMTS BCD*10.3 Srce. Invoice Amount
  INVCOUNT Long Number of Invoices
  AVGINVF BCD*10.3 Func. Average Invoice
  AVGINVS BCD*10.3 Srce. Average Invoice
  LARGSTINF BCD*10.3 Func. Largest Invoice
  LARGSTINS BCD*10.3 Srce. Largest Invoice
  LINVVEND String*12 Largest Invoice Vendor
  SMALSTINF BCD*10.3 Func. Smallest Invoice
  SMALSTINS BCD*10.3 Srce. Smallest Invoice
  SINVVEND String*12 Smallest Invoice Vendor
  CNAMTF BCD*10.3 Func. Credit Note Amount
  CNAMTS BCD*10.3 Srce. Credit Note Amount
  CNCOUNT Long Number of Credit Notes
  AVGCNF BCD*10.3 Func. Average Credit Note
  AVGCNS BCD*10.3 Srce. Average Credit Note
  LARGSTCNF BCD*10.3 Func. Largest Credit Note
  LARGSTCNS BCD*10.3 Srce. Largest Credit Note
  LCNVEND String*12 Largest Credit Note Vendor
  SMALSTCNF BCD*10.3 Func. Smallest Credit Note
  SMALSTCNS BCD*10.3 Srce. Smallest Credit Note
  SCNVEND String*12 Smallest Credit Note Vendor
  DNAMTF BCD*10.3 Func. Debit Note Amount
  DNAMTS BCD*10.3 Srce. Debit Note Amount
  DNCOUNT Long Number of Debit Notes
  AVGDNF BCD*10.3 Func. Average Debit Note
  AVGDNS BCD*10.3 Srce. Average Debit Note
  LARGSTDNF BCD*10.3 Func. Largest Debit Note
  LARGSTDNS BCD*10.3 Srce. Largest Debit Note
  LDNVEND String*12 Largest Debit Note Vendor
  SMALSTDNF BCD*10.3 Func. Smallest Debit Note
  SMALSTDNS BCD*10.3 Srce. Smallest Debit Note
  SDNVEND String*12 Smallest Debit Note Vendor

## POVIA - Ship-Via Addresses (view PO0900)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*6 Ship-Via
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*60 Ship-Via Name
  ADDRESS1 String*60 Address 1
  ADDRESS2 String*60 Address 2
  ADDRESS3 String*60 Address 3
  ADDRESS4 String*60 Address 4
  CITY String*30 City
  STATE String*30 State/Province
  ZIP String*20 Zip/Postal Code
  COUNTRY String*30 Country
  PHONE String*30 Phone Number
  FAX String*30 Fax Number
  CONTACT String*60 Contact
  COMMENT String*80 Comment
  EMAIL String*50 E-mail
  PHONEC String*30 Contact Phone
  FAXC String*30 Contact Fax
  EMAILC String*50 Contact E-mail

## POVUMB - Vendor Contract Cost Base Units (view PO0191)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+VDCODE+UNIT
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  VDCODE String*12 Vendor
  UNIT String*10 Unit of Measure
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONVERSION BCD*10.6 Conversion Factor to Stocking
  BAMOUNT BCD*10.6 Base Amount

## POVUMS - Vendor Contract Cost Sale Units (view PO0192)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+VDCODE+UNIT
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  VDCODE String*12 Vendor
  UNIT String*10 Unit of Measure
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CONVERSION BCD*10.6 Conversion Factor to Stocking
  SUSING Integer Sale Cost Calculated Using [1=Base Unit Cost Minus a Percentage,2=Base Unit Cost Minus an Amount,3=Fixed Amount]
  SPERCENT BCD*5.5 Discount Percent
  SDAMOUNT BCD*10.6 Discount Amount
  SFAMOUNT BCD*10.6 Fixed Amount
  SALESTART Date Sale Start Date
  SALEEND Date Sale End Date

## POVUPR - Vendor Contract Costs (view PO0181)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+VDCODE; VDCODE+ITEMNO
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  VDCODE String*12 Vendor Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VCPDESC String*60 Contract Cost Description
  BCOSTTYPE Integer Base Cost Type [1=Base Unit Cost for Single Unit of Measure,2=Base Unit Cost for Multiple Units of Measure]
  BAMOUNT BCD*10.6 Base Cost Amount
  DEFBUNIT String*10 Base Unit
  BASECONV BCD*10.6 Base Unit Conversion
  SCOSTTYPE Integer Sale Cost Type [1=Sale Unit Cost for Single Unit of Measure,2=Sale Unit Cost for Multiple Units of Measure]
  SDEFUSING Integer Sale Cost Based On [1=Base Unit Cost Minus a Percentage,2=Base Unit Cost Minus an Amount,3=Fixed Amount]
  SPERCENT BCD*5.5 Percentage of Base
  SDAMOUNT BCD*10.6 Discount Amount
  SFAMOUNT BCD*10.6 Fixed Amount
  DEFSUNIT String*10 Sale Unit
  SALECONV BCD*10.6 Sale Unit Conversion
  SALESTART Date Sale Starts
  SALEEND Date Sale Ends
  COSTFMT Integer Discount Based On [1=Percentage,2=Amount]
  COSTQTY0 BCD*10.4 Quantity Level 0
  COSTQTY1 BCD*10.4 Quantity Level 1
  COSTQTY2 BCD*10.4 Quantity Level 2
  COSTQTY3 BCD*10.4 Quantity Level 3
  COSTQTY4 BCD*10.4 Quantity Level 4
  COSTQTY5 BCD*10.4 Quantity Level 5
  COSTQTY6 BCD*10.4 Quantity Level 6
  COSTQTY7 BCD*10.4 Quantity Level 7
  COSTQTY8 BCD*10.4 Quantity Level 8
  COSTQTY9 BCD*10.4 Quantity Level 9
  PRCNTLVL0 BCD*5.5 Percentage Level 0
  PRCNTLVL1 BCD*5.5 Percentage Level 1
  PRCNTLVL2 BCD*5.5 Percentage Level 2
  PRCNTLVL3 BCD*5.5 Percentage Level 3
  PRCNTLVL4 BCD*5.5 Percentage Level 4
  PRCNTLVL5 BCD*5.5 Percentage Level 5
  PRCNTLVL6 BCD*5.5 Percentage Level 6
  PRCNTLVL7 BCD*5.5 Percentage Level 7
  PRCNTLVL8 BCD*5.5 Percentage Level 8
  PRCNTLVL9 BCD*5.5 Percentage Level 9
  AMOUNTLVL0 BCD*10.6 Amount Level 0
  AMOUNTLVL1 BCD*10.6 Amount Level 1
  AMOUNTLVL2 BCD*10.6 Amount Level 2
  AMOUNTLVL3 BCD*10.6 Amount Level 3
  AMOUNTLVL4 BCD*10.6 Amount Level 4
  AMOUNTLVL5 BCD*10.6 Amount Level 5
  AMOUNTLVL6 BCD*10.6 Amount Level 6
  AMOUNTLVL7 BCD*10.6 Amount Level 7
  AMOUNTLVL8 BCD*10.6 Amount Level 8
  AMOUNTLVL9 BCD*10.6 Amount Level 9
  ROUNDMETHD Integer Rounding Method [1=No Rounding,2=Round Up,3=Round Down]
  ROUNDAMT BCD*10.6 Round to a Multiple Of

## POVUTX - Vendor Contract Included Taxes (view PO0183)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+VDCODE+TAXAUTH
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  VDCODE String*12 Vendor
  TAXAUTH String*12 Tax Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXCLASS Integer Tax Class
