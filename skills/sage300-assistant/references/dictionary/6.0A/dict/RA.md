# RA module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## RAAUT - Authorization Codes (view RA0010)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*12 User ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 User Name
  PASSWORD String*10 Password
  APPROVER Boolean Authorized to approve RMAs

## RABOMD - RMA BOM Details (view RA0026)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+LINENUM+PRNCOMPNUM+COMPNUM
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifer
  LINENUM Integer Linenum
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPONENT String*24 Component Item
  DESC String*60 Description
  QTY BCD*10.4 Component Quantity
  UNIT String*10 Unit of Measure
  QTYSHIPPED BCD*10.4 Quantity Returned

## RACOIN - RMA Comments/Instructions (view RA0020)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+UNIQUIFIER
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifier
  UNIQUIFIER Integer Line Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COINTYPE Integer Comments/Instructions Type [1=Comment,2=Instruction]
  COIN String*80 Comments/Instructions

## RACOMD - RMA Kitting Details (view RA0022)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+LINENUM+PRNCOMPNUM+COMPNUM
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifer
  LINENUM Integer Linenum
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COMPONENT String*24 Component Item
  DESC String*60 Description
  ACCTSET String*6 Item Account Set
  USERCOSTMD Boolean User-Specified Costing Method
  LOCATION String*6 Location
  PICKSEQ String*10 Picking Sequence
  STOCKITEM Boolean Stock Item
  QTY BCD*10.4 Quantity
  EXTQTY BCD*10.4 Extended Quantity
  UOM String*10 Unit of Measure
  UNITCONV BCD*10.6 Unit Conversion
  UNITCOST BCD*10.6 Unit Cost
  MOSTREC BCD*10.6 Most Recent Unit Cost
  STDCOST BCD*10.6 Standard Unit Cost
  COST1 BCD*10.6 Alternate Unit Cost 1
  COST2 BCD*10.6 Alternate Unit Cost 2
  AVGCOST BCD*10.6 Average Unit Cost
  LASTCOST BCD*10.6 Last Unit Cost
  COSTUNIT String*10 Costing Unit of Measure
  COSUNTCST BCD*10.6 Costing Unit Cost
  COSUNTCONV BCD*10.6 Costing Unit Conversion
  EXTCOST BCD*10.3 Extended Cost
  HAVESERIAL Boolean Use Item Serial Numbers [0=No,1=Yes]
  GLNONSTKCR String*45 Non-stock Clearing Account
  GLNONSTKCD String*60 Non-stock Clearing Acct. Desc.
  SERIALITEM Boolean Is Item Serialized?
  UNFMTITEM String*24 Unformatted Item Number
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  WEIGHTUNIT String*10 Weight UOM
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  ISLOTTRKED Boolean Is Lot Tracked [0=No,1=Yes]

## RACOMDL - RMA Kitting Lot Numbers (view RA0024)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+LOTNUM
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifer
  LINENUM Integer Linenum
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  LOTNUM String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  QTY BCD*10.4 Quantity
  UNIQUE Long Unique
  EXPIRYDATE Date Expiry Date

## RACOMDS - RMA Kitting Serial Numbers (view RA0023)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+SERIALNUM
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifer
  LINENUM Integer Linenum
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  SERIALNUM String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  QTY BCD*10.4 Quantity
  UNIQUE Long Unique

## RADET - Return Authorization Details (view RA0002)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+LINENUM; RMAUNIQ+DETAILNUM
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RA Uniquifier
  LINENUM Integer RA Detail Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CSTORIGINV String*22 Customer Original Invoice
  VNDORIGREC String*22 Vendor Original Receipt
  VNDRECSEQ BCD*10.0 Vendor Original Receipt Sequence Number
  LINETYPE Integer Line Type [1=Item,2=Miscellaneous]
  ITEM String*24 Item Number
  UNFMTTITEM String*24 Unformatted Item Number
  MISCCHARGE String*6 Miscellaneous Charge Code
  DESC String*60 Description
  UNIT String*10 Unit of Measure
  UNITCONV BCD*10.6 Unit Conversion Factor
  QTY BCD*10.4 Quantity
  EXTSTATUS String*12 Status
  INTSTATUS String*12 Workflow Stage
  PROMISDATE Date Promised Receipt Date
  RECVDDATE Date Date Received
  COMPLETE Boolean Complete? [0=No,1=Yes]
  COMPLETDTE Date Date Completed
  RETURNSTCK Boolean Return to Stock? [0=No,1=Yes]
  PRICELIST String*6 Price List Code
  LOCATION String*6 Location
  CATEGORY String*6 Category
  FAULT String*12 Fault
  CSTRPINVNO String*22 Consumer Replacement Invoice No.
  CSTRPINVDT Date Consumer Replacement Inv. Date
  REJECTDATE Date Date Rejected
  REJECTCOMM String*200 Rejection Comment
  REPAIRAGNT String*12 Repair Agent
  REPAIRDATE Date Repair Date
  SERIALNUM String*40 Serial Number
  CSTWARRNTY Boolean Customer Warranty? [0=No,1=Yes]
  CSTWARREF String*22 Customer Warranty Reference
  CSTWAREXDT Date Customer Warranty Expiry Date
  VNDWARRNTY Boolean Vendor Warranty? [0=No,1=Yes]
  VNDWARREF String*22 Vendor Warranty Reference
  VNDWAREXDT Date Vendor Warranty Expiry Date
  COMMENT String*250 Comment
  CONSPURCDT Date Consumer Purchase Date
  CONSNAME String*60 Consumer Name
  CONSADDR1 String*60 Consumer Address 1
  CONSADDR2 String*60 Consumer Address 2
  CONSADDR3 String*60 Consumer Address 3
  CONSADDR4 String*60 Consumer Address 4
  CONSCITY String*30 Consumer City
  CONSSTATE String*30 Consumer State/Prov.
  CONSZIP String*20 Consumer Zip/Postal Code
  CONSCOUNTR String*30 Consumer Country
  CONSPHONE String*30 Consumer Phone
  CONSFAX String*30 Consumer Fax
  CONSCONTAC String*60 Consumer Contact
  UNITPRICE BCD*10.6 Unit Price
  PRICEUOM String*10 Pricing Unit of Measure
  PRICECONV BCD*10.6 Pricing Unit Conversion
  EXTPRICE BCD*10.3 Extended Price
  UNITCOST BCD*10.6 Unit Cost
  COSTUOM String*10 Costing Unit of Measure
  COSTCONV BCD*10.6 Costing Unit Conversion
  EXTCOST BCD*10.3 Extended Cost
  VNDUNITCST BCD*10.6 Vendor Unit Cost
  VNDCOSTUOM String*10 Vendor Costing Unit of Measure
  VNDCSTCONV BCD*10.6 Vendor Costing Unit Conversion
  VNDEXTCST BCD*10.3 Vendor Extended Cost
  DETAILNUM Integer Detail Number
  HAVESERIAL Boolean Have Serial Numbers? [0=No,1=Yes]
  SERIALITEM Boolean Is Item Serialized? [0=No,1=Yes]
  PUTONORD Boolean Put on Replacement Order [0=No,1=Yes]
  ZEROORD Boolean Zero value on Replacement Order [0=No,1=Yes]
  PUTONCRD Boolean Put Item/Misc. on Credit Note [0=No,1=Yes]
  ZEROCRD Boolean Zero value on Credit Note [0=No,1=Yes]
  PUTONRET Boolean Put Item on Vendor Return [0=No,1=Yes]
  ZERORET Boolean Zero value on Vendor Return [0=No,1=Yes]
  CSTORDDATE Date Customer Order Date
  CSTORDNUM String*22 Customer Order Number
  CSTCRDDATE Date Customer Credit Note Date
  CSTCRDNUM String*22 Customer Credit Note Number
  VNDRETDATE Date Vendor Return Date
  VNDRETNUM String*22 Vendor Return Number
  RESTOCKFEE Boolean Restocking Fee? [0=No,1=Yes]
  CSTINVUNIQ BCD*10.0 Customer Invoice Uniquifier
  HASCOIN Boolean Has comments/instructions [0=No,1=Yes]
  ISLOTTRKED Boolean Lot Tracked [0=No,1=Yes]
  VALUES Long Number of optional fields
  DDTLTYPE Integer Kitting/BOM [0=None,1=Kitting,2=BOM]
  DDTLNUM String*6 Kit/BOM Number
  NEXTCMPNUM Long Next Component Number
  APPROVED Boolean Approved
  XLINENUM Integer Document Line No.
  DISCPER BCD*5.5 Discount %
  EXTDSCAMNT BCD*10.3 Discount Amount
  EXTDSCPRIC BCD*10.3 Discounted Ext. Amount
  CONSCODE String*12 Consumer Code
  XDETAILNUM Integer Document Detailnum
  PRICEBY Integer Price By [1=Quantity,2=Weight]
  TRACKNO String*36 Shipment Tracking Number
  SHIPVIA String*6 Ship Via Code
  SHPVIADESC String*60 Ship Via Code Description
  MANITEMNO String*24 Manufacturer's Item Number
  CUSTITEMNO String*24 Customer's Item Number
  WEIGHTUNIT String*10 Weight UOM
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Unit Weight
  PRICEOVER Boolean Price Override [0=No,1=Yes]
  PRWGHTUNIT String*10 Pricing Weight UOM
  PRWGHTCONV BCD*10.6 Pricing Weight Conversion Factor
  JOBRELATED Boolean Is Detail Line Job Related? [0=No,1=Yes]
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CCATEGORY String*16 Category Code
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  PROJSTYLE Integer Project Style [0=,1=Standard,2=Basic]
  PROJTYPE Integer Project Type [0=,1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [0=,1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,7=Completed Contract,8=Accrual-Basis]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  REVBILL String*45 Revenue/Billing Account
  COGSWIP String*45 COGS/WIP Account
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percent
  RTGDAYS Integer Retainage Days
  PRICEOPT Integer Default O/E Price [0=,1=Billing Rate,2=Use Customer Price List,3=Use Specified Price List]
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Item Unit
  LVL1NAME String*30 Level 1 Name
  LVL2NAME String*30 Level 2 Name
  LVL3NAME String*30 Level 3 Name
  UFMTCONTNO String*16 Unformatted Contract Code

## RADETO - RMA Detail Optional Fields (view RA0034)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+LINENUM+OPTFIELD; OPTFIELD+RMAUNIQ+LINENUM
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifier
  LINENUM Integer Linenum
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
  SWSET Integer [0=No,1=Yes,99=]

## RAEXT - External Status (view RA0011)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*12 Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description

## RAFAU - Fault Codes (view RA0012)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*12 Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description

## RAHEAD - Return Authorizations (view RA0001)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ; RMANUMBER
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RA Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RMANUMBER String*24 RA Number
  RMADATE Date RA Date
  CUSTOMER String*12 Customer Number
  SHIPTO String*6 Ship-To Location
  SHIPNAME String*60 Ship-To Name
  BILNAME String*60 Bill-To Name
  BILADDR1 String*60 Bill-To Address Line 1
  BILADDR2 String*60 Bill-To Address Line 2
  BILADDR3 String*60 Bill-To Address Line 3
  BILADDR4 String*60 Bill-To Address Line 4
  BILCITY String*30 Bill-To City
  BILSTATE String*30 Bill-To State
  BILZIP String*20 Bill-To Zip / Post Code
  BILCOUNTRY String*30 Bill-To Country
  BILPHONE String*30 Bill-To Phone
  BILFAX String*30 Bill-To Fax
  BILEMAIL String*50 Bill-To E-mail
  BILCONTACT String*60 Bill-To Contact
  BILEMAILC String*50 Bill-To Contact E-mail
  BILPHONEC String*30 Bill-To Contact Phone
  BILFAXC String*30 Bill-To Contact Fax
  AUTHORSDBY String*12 Authorized By
  COMPLETE Boolean Complete?
  VENDOR String*12 Vendor Number
  VENDORNAME String*60 Vendor Name
  CSTCRDDATE Date Last Customer CN Date
  CSTCRDNUM String*22 Last Customer CN Number
  CSTORDDATE Date Last Customer Order Date
  CSTORDNUM String*22 Last Customer Order Number
  VNDRETDATE Date Vendor Return Date
  VNDRETNUM String*22 Vendor Return Number
  VNDRMADATE Date Vendor RA Date
  VNDRMANUM String*22 Vendor RA Number
  COMMENT String*250 Comment
  CSTCLAIMNO String*22 Customer Claim Number
  SHIPVIA String*6 Ship Via
  SHIPDATE Date Ship Date
  SHIPREF String*22 Shipping Reference
  CLAIMNOVND String*22 Claim Vendor Reference
  CLAIMVND String*12 Claim Vendor Number
  CLAIMAMTVN BCD*10.3 Claim Vendor Amount
  RASOURCURR String*3 Source Currency
  RATOTAMT BCD*10.3 Total Amount
  RATOTCOST BCD*10.3 Total Cost
  TOTVNDCOST BCD*10.3 Total Vendor Return Cost
  VENDCURR String*3 Vendor Source Currency
  CSTORIGINV String*22 Customer Sales Invoice
  RATEMPL String*12 RA Template Code
  DESC String*60 Description
  SHPADDR1 String*60 Ship-To Address 1
  SHPADDR2 String*60 Ship-To Address 2
  SHPADDR3 String*60 Ship-To Address 3
  SHPADDR4 String*60 Ship-To Address 4
  SHPCITY String*30 Ship-To City
  SHPSTATE String*30 Ship-To State
  SHPZIP String*20 Ship-To Zip
  SHPCOUNTRY String*30 Ship-To Country
  SHPPHONE String*30 Ship-To Phone
  SHPFAX String*30 Ship-To Fax
  SHPEMAIL String*50 Ship-To E-mail
  SHPCONTACT String*60 Ship-To Contact
  SHPPHONEC String*30 Ship-To Contact Phone
  SHPFAXC String*30 Ship-To Contact Fax
  SHPEMAILC String*50 Ship-To Contact E-mail
  DEFRMADOC String*24 Default RMA Document
  NEXTDTLNUM Integer Next Detail Number
  DTLFILLVAL String*250 Fill Details by Value
  DTLFILLOPT Integer Fill Details by [0=O/E Invoice,1=RMA Document,2=Serial No.,3=Item Lot,4=Item Number,5=Serial No.(No Invoice)]
  VALUES Long Number of optional fields
  PRICELIST String*6 Price List Code
  CALRSTKFEE Boolean Calculate Restocking Fee
  APPROVED Boolean Is RMA Approved
  APPROVEDBY String*12 Approved by
  APPPASSWRD String*10 Approver Password
  VNDBILLTO String*6 Vendor Bill-To Location
  VNDSHIPVIA String*6 Vendor Ship-Via Code
  HASJOB Boolean Job Related [0=No,1=Yes]
  JOBLINES Long Job Related Detail Lines
  NONINVABLE Boolean Project Invoicing? [0=No,1=Yes]
  LNINVABLE Long Invoiceable Detail Lines
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGTERMS String*6 Retainage Terms
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGTERMDSC String*60 Retainage Terms Description
  RATEOPT Integer Currency Rate Option [1=Use Original Document Exchange Rate,2=Use RMA Exchange Rate]
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATE BCD*8.7 Rate
  TERRITORY String*6 Territory
  CUSTDISC Integer Customer Type [0=Base,1=A,2=B,3=C,4=D,5=E]
  CUSACCTSET String*6 Cust. Acct. Set
  TAXGROUP String*12 Tax Group
  VIADESC String*60 Ship-Via Code Description
  TERMS String*6 Terms Code
  PROCESSCMD Integer

## RAHEADO - RMA Header Optional Fields (view RA0033)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+OPTFIELD; OPTFIELD+RMAUNIQ
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifier
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
  SWSET Integer [0=No,1=Yes,99=]

## RAINT - Workflow Stage (view RA0013)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*12 Stage Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description

## RAITEM - RMA Item Policies (view RA0019)
Keys (first = PK; D=dups allowed, M=modifiable): ITEM
Fields (NAME type description [values]):
  ITEM String*24 Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  NORETURN Boolean No Credit Notes Allowed [0=No,1=Yes]
  RETURNDAYS Integer day(s) beyond date of invoice
  NOREPAIR Boolean No Replacement Orders Allowed

## RALOTRA - RMA Lot Numbers (view RA0021)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+UNIQUIFIER; RMAUNIQ+DETAILNUM+LOTNUM [M]; LOTNUM+UNIQUE [D,M]
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifier
  UNIQUIFIER Integer Line Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  LOTNUM String*40 Lot Number
  ORIGQTY BCD*10.4 Original Quantity
  QTY BCD*10.4 Quantity
  UNIQUE Long Lot Uniquifier
  EXPIRYDATE Date Expiry Date

## RAOFD - Optional Fields (view RA0031)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=RMA Document Header,1=RMA Document Detail]
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEFVAL String*60
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  INITFLAG Integer Auto Insert [0=No,1=Yes]
  SWREQUIRED Integer [0=No,1=Yes]
  SWSET Integer [0=No,1=Yes]

## RAOFH - Optional Field Locations (view RA0030)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=RMA Document Header,1=RMA Document Detail]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

## RAOPT - Setup Options (view RA0015)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*12 Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  AUTONUMBER Boolean Autonumber RAs
  RANUMBERL BCD*10.0 RA Number Length
  RAPREFIXED String*6 RA Prefix
  NEXTRANUM String*24 Next RA Number
  NEXTRAUNIQ BCD*10.0 RA Uniquifier
  OEARICLINK Boolean OE/AR/IC Link
  POAPICLINK Boolean PO/AP/IC Link
  CONTACT String*60 RA Contact
  PHONE String*20 RA Contact Phone
  FAX String*20 RA Contact Fax
  EXTBLANK Boolean Allow Blank Status [0=No,1=Yes]
  INTBLANK Boolean Allow Blank Workflow Stage [0=No,1=Yes]
  FAULTBLANK Boolean Allow Blank Fault Code [0=No,1=Yes]
  REPBLANK Boolean Allow Blank Repair Agent [0=No,1=Yes]
  DEFTEMPL String*12 Default Template
  NODAYSEXP Integer Num. Days before RMA Expires

## RAREP - Repair Agent (view RA0014)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*12 Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description

## RASELRA - RMA Serial Numbers (view RA0018)
Keys (first = PK; D=dups allowed, M=modifiable): RMAUNIQ+UNIQUIFIER; RMAUNIQ+DETAILNUM+SERIALNUM
Fields (NAME type description [values]):
  RMAUNIQ BCD*10.0 RMA Uniquifier
  UNIQUIFIER Integer Line Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  SERIALNUM String*40 Serial Number
  QTY Long Qty

## RATEMPL - RMA Template Codes (view RA0017)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*12 Template Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  DEFAUTH String*12 Default Authorized by
  DEFDESC String*60 Default RMA Description
  DEFSHIPREF String*22 Default Shipping Reference
  DEFSHIPVIA String*6 Default Shipping Via
  DEFCOM String*250 Default comment
  AUTORESTK Boolean Automatic Item Restocking Charge [0=No,1=Yes]
  RESTKCODE String*6 Restocking Misc. Charge Code
  MATCHINCR Boolean Match Credit Note to Invoice [0=No,1=Yes]
  INVREQ Boolean Invoice required on all items [0=No,1=Yes]
  CHECKQTY Boolean Check Quantity already credited [0=No,1=Yes]
  DEFORIGQTY Boolean Default Orig. Invoice Quantity [0=No,1=Yes]
  ZEROORD Boolean Zero Dollar Replacement Order [0=No,1=Yes]
  COPYORD Boolean Copy RMA Comments to Replace Ord [0=No,1=Yes]
  COPYCRD Boolean Copy RMA Comments to Unmatched CR Note [0=No,1=Yes]
  COPYRET Boolean Copy RMA Comments to Vend Return [0=No,1=Yes]
  CREDDATE Integer Default Credit Note Date [1=RMA Date,2=Completion Date,3=Session Date]
  OVERRDPW String*10 Invoice Check Override password
  PUTORD Integer Put RMA Num in Replace Ord field [1=Reference,2=Description]
  PUTCRD Integer Put RMA Num in Credit Note field [1=Reference,2=Description]
  PUTRET Integer Put RMA Num in Vend Return field [1=Reference,2=Description]
  CRDSLSP Integer Salespeople on Credit Note from [1=Bill-To Salespeople,2=Ship-To Salespeople,3=Invoice,4=RMA Template Salesperson]
  ORDSLSP Integer Salespeople on Replace Ord from [1=Bill-To Salespeople,2=Ship-To Salespeople,3=Invoice,4=RMA Template Salesperson]
  MUSTCOMPL Boolean Complete Details before Header
  DEFITMCAT String*6 Default Item Category
  DEFITMLOC String*6 Default Item Location
  IEXTBLANK Boolean Allow Blank Item Status [0=No,1=Yes]
  IINTBLANK Boolean Allow Blank Item Workflow Stage [0=No,1=Yes]
  IFAUBLANK Boolean Allow Blank Item Fault Code [0=No,1=Yes]
  IREPBLANK Boolean Allow Blank Item Repair Agent [0=No,1=Yes]
  MEXTBLANK Boolean Allow Blank Misc Status [0=No,1=Yes]
  MINTBLANK Boolean Allow Blank Misc Workflow Stage [0=No,1=Yes]
  MFAUBLANK Boolean Allow Blank Misc Fault Code [0=No,1=Yes]
  MREPBLANK Boolean Allow Blank Misc Repair Agent [0=No,1=Yes]
  IDEFRETSTK Boolean Default Item Return to Stock? [0=No,1=Yes]
  DEFITEMEXT String*12 Default Item Status
  DEFITEMINT String*12 Default Item Workflow Stage
  DEFITEMFAU String*12 Default Item Fault Code
  DEFITEMREP String*12 Default Item Repair Agent
  DEFMISCEXT String*12 Default Misc Status
  DEFMISCINT String*12 Default Misc Workflow Stage
  DEFMISCFAU String*12 Default Misc Fault Code
  DEFMISCREP String*12 Default Misc Repair Agent
  IPUTONORD Boolean Put Item on Replacement Order [0=No,1=Yes]
  IZEROORD Boolean Default Item Zero Replace value [0=No,1=Yes]
  IPUTONCRD Boolean Put Item on Credit Note [0=No,1=Yes]
  IZEROCRD Boolean Default Item Zero CR Note value [0=No,1=Yes]
  IPUTONRET Boolean Put Item on Vendor Return [0=No,1=Yes]
  IZERORET Boolean Default Item Zero Return value [0=No,1=Yes]
  MPUTONORD Boolean Put Misc on Replacement Order [0=No,1=Yes]
  MZEROORD Boolean Default Misc Zero Replace value [0=No,1=Yes]
  MPUTONCRD Boolean Put Misc on Credit Note [0=No,1=Yes]
  MZEROCRD Boolean Default Misc Zero CR Note value [0=No,1=Yes]
  MPUTONRET Boolean Put Misc on Vendor Return [0=No,1=Yes]
  MZERORET Boolean Default Misc Zero Return value [0=No,1=Yes]
  RANUMBERL BCD*10.0 RA Number Length
  RAPREFIXED String*6 RA Prefix
  NEXTRANUM String*24 Next RA Number
  DEFRPT String*60 Default Return Instruction
  USEAUTO Boolean Use Template Autonumbering
  CODESLSP String*8 Salesperson
  RESTKFEE BCD*10.6 Restocking Fee %
  EDITONCMPL Boolean Allow field changes if complete
  RATEOPT Integer Currency Rate Option [1=Use Original Document Exchange Rate,2=Use RMA Exchange Rate]
  SWCOMMENT Boolean Overwrite RMA Comments to Matched CR Note
  SWINACTIVE Boolean Inactive [0=No,1=Yes]
